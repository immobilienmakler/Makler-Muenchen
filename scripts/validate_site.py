"""Offline checks for drift between HTML, JSON-LD, sitemap and AI profiles."""
import json
import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = ("index.html", "llms.txt", "llms-full.txt", "sitemap.xml", "quellen.json", "immobilien-vorbereitung.md")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalize(text):
    return " ".join(text.split())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.meta = {}
        self.ids = []
        self.links = []
        self.review_dates = []
        self.h1_count = 0
        self.hidden = None
        self.schema = ""
        self.visible = []
        self.faqs = []
        self.faq = None
        self.field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            require(attrs.get("lang") == "de", "Missing German document language")
        if tag in ("script", "style"):
            self.hidden = attrs.get("type", tag)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "time" and attrs.get("datetime"):
            self.review_dates.append(attrs["datetime"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property"))] = attrs.get("content")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "details":
            self.faq = {"question": "", "answer": ""}
        if self.faq is not None and tag in ("summary", "p"):
            self.field = "question" if tag == "summary" else "answer"

    def handle_data(self, data):
        if self.hidden == "application/ld+json":
            self.schema += data
        if not self.hidden:
            self.visible.append(data)
            if self.faq is not None and self.field:
                self.faq[self.field] += data

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = None
        if tag in ("summary", "p"):
            self.field = None
        if tag == "details":
            self.faqs.append(self.faq)
            self.faq = None


def validate():
    for filename in PUBLIC_FILES:
        require((ROOT / filename).is_file(), f"Missing public file: {filename}")
    page = Page()
    page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    require(page.h1_count == 1, "Expected one h1")
    require(len(page.ids) == len(set(page.ids)), "Duplicate HTML IDs")
    require(len(page.canonicals) == 1, "Expected one canonical URL")
    canonical = page.canonicals[0]
    parsed = urlsplit(canonical)
    require(parsed.scheme == "https" and parsed.netloc and canonical.endswith("/"), "Invalid canonical URL")
    require(not parsed.query and not parsed.fragment, "Canonical must not include a query or fragment")
    require(page.meta.get("og:url") == canonical, "Open Graph URL differs from canonical")
    require(page.meta.get("description"), "Missing meta description")
    require("noindex" not in page.meta.get("robots", ""), "Page must be indexable")
    for href in page.links:
        if href.startswith("#"):
            require(href[1:] in page.ids, f"Missing fragment target: {href}")
        elif not urlsplit(href).scheme and not href.startswith("//"):
            require((ROOT / href).is_file(), f"Missing local link target: {href}")
    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    locations = [node.text for node in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    require(locations == [canonical], "Sitemap must contain only the canonical HTML page")
    data = json.loads(page.schema)
    require(data.get("@context") == "https://schema.org", "Missing Schema.org context")
    graph = data["@graph"]
    by_type = {node["@type"]: node for node in graph}
    ids = {node["@id"] for node in graph}
    require(len(ids) == len(graph), "Duplicate JSON-LD IDs")
    require(by_type["CollectionPage"]["url"] == canonical, "CollectionPage URL differs from canonical")
    agent = by_type["RealEstateAgent"]
    services = [node for node in graph if node["@type"] == "Service"]
    require(len(services) == 5, "Expected five core services")
    for service in services:
        require(service["provider"]["@id"] == agent["@id"], "Service provider mismatch")
        require(service["url"] in page.links, f"Service has no visible source link: {service['name']}")
    questions = by_type["FAQPage"]["mainEntity"]
    require(len(questions) == len(page.faqs) and questions, "FAQ count differs from visible content")
    for question, visible in zip(questions, page.faqs):
        require(normalize(question["name"]) == normalize(visible["question"]), "FAQ question differs from HTML")
        require(normalize(question["acceptedAnswer"]["text"]) == normalize(visible["answer"]), "FAQ answer differs from HTML")
    text = normalize(" ".join(page.visible))
    facts = [agent["name"], agent["email"], agent["address"]["streetAddress"], agent["address"]["postalCode"]]
    for filename in ("llms.txt", "llms-full.txt"):
        profile = (ROOT / filename).read_text(encoding="utf-8")
        for fact in facts:
            require(fact in text and fact in profile, f"Inconsistent fact in {filename}: {fact}")
        for service in services:
            require(service["url"] in profile, f"Missing service source in {filename}")
        require(canonical + "llms" in profile, f"Incorrect project URL in {filename}")
        for url in re.findall(r"https://[^\s)]+", profile):
            if url.startswith(canonical):
                relative = url[len(canonical):]
                require(not relative or relative in PUBLIC_FILES, f"Unpublished AI-profile link: {url}")
    catalog = json.loads((ROOT / "quellen.json").read_text(encoding="utf-8"))
    resources = catalog["resources"]
    date.fromisoformat(catalog["reviewedOn"])
    require(catalog["reviewedOn"] in page.review_dates, "Source review date differs from visible date")
    require(catalog["publisher"] == agent["name"], "Source publisher differs from company")
    require(by_type["CollectionPage"]["mainEntity"]["@id"] == by_type["ItemList"]["@id"], "Collection does not reference source list")
    require(by_type["CollectionPage"]["citation"] == [r["url"] for r in resources], "Page citations differ from source catalog")
    items = by_type["ItemList"]["itemListElement"]
    require(len(resources) == len(items) == by_type["ItemList"]["numberOfItems"], "Source count mismatch")
    require(len({r["url"] for r in resources}) == len(resources), "Duplicate sources")
    for index, (resource, item) in enumerate(zip(resources, items), 1):
        require(item["position"] == index, "Incorrect source position")
        require(urlsplit(resource["url"]).hostname == "bayernwerte.de", "Source must be on primary website")
        require(resource["url"] in page.links, "Source is not linked in HTML")
        require(resource["id"] in page.ids, "Source has no visible HTML entry")
        for key, schema_key in (("title", "name"), ("url", "url"), ("description", "description")):
            require(resource[key] == item["item"][schema_key], "Source catalog differs from JSON-LD")
        require(resource["title"] in text and resource["description"] in text, "Source text missing from HTML")
        for filename in ("llms.txt", "llms-full.txt", "immobilien-vorbereitung.md"):
            require(resource["url"] in (ROOT / filename).read_text(encoding="utf-8"), f"Source missing from {filename}")
    require(by_type["DigitalDocument"]["url"] == canonical + "immobilien-vorbereitung.md", "Checklist URL differs")
    print("SEO checks passed: URLs, schema, FAQs, AI profiles, source catalog and checklist agree.")


if __name__ == "__main__":
    validate()
