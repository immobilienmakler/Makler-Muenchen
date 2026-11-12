# Makler München · Bayernwerte Immobilien

Statische, deutschsprachige Informationsseite für Bayernwerte Immobilien in München und Umgebung. Sie stellt Leistungen und Kontaktmöglichkeiten vor und verweist für aktuelle Immobilienangebote auf [bayernwerte.de](https://bayernwerte.de/).

## Projektstand

Dieses Repository enthält die eigenständige Landingpage `index.html` und den GitHub-Pages-Workflow. Die Darstellung funktioniert ohne ausführbares JavaScript, externe Schriftarten, Tracking oder Build-Abhängigkeiten. Ein nicht ausführbarer JSON-LD-Datenblock beschreibt Unternehmen, Leistungen und häufige Fragen.

Eine OpenImmo-/Ilogu-Anbindung, FTP-Übertragung, WordPress-CLI, Bildverarbeitung und automatische Angebotsimporte sind **nicht in diesem Repository implementiert**. Angebote werden auf der Hauptwebsite gepflegt und hier verlinkt.

## Lokal ansehen

Im Projektverzeichnis mit Python 3 starten:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Anschließend <http://127.0.0.1:8000> öffnen. Alternativ lässt sich `index.html` direkt im Browser öffnen.

## Pflege und Prüfung

- Inhalte, Kontaktdaten und Links in `index.html` bearbeiten; CSS steht im `<style>`-Block.
- Bei Inhaltsänderungen auch Seitentitel, Beschreibung und Open-Graph-Metadaten prüfen.
- Vor Veröffentlichung kleine und große Bildschirmbreiten sowie Tastaturbedienung prüfen: Navigation, „Zum Inhalt springen“, Kontakt und Angebotslinks.
- Externe Links regelmäßig auf Erreichbarkeit prüfen. Impressum und Datenschutz verweisen auf die Hauptwebsite; die Angaben müssen für den tatsächlichen Betrieb aktuell und passend sein.
- Bei Änderungen an Leistungen, Kontaktdaten oder FAQ auch JSON-LD, `llms.txt` und `llms-full.txt` aktualisieren. Die Übereinstimmung prüft `python3 scripts/validate_site.py` ohne zusätzliche Pakete.

## Veröffentlichung

In den Repository-Einstellungen unter **Pages → Build and deployment → Source** die Option **GitHub Actions** auswählen. Der vorhandene Workflow `.github/workflows/static.yml` veröffentlicht bei Pushes auf `main` oder manuellem Start die statische Seite. Änderungen über einen Pull Request werden erst nach dem Zusammenführen veröffentlicht.

Der Workflow prüft bei Pull Requests und vor einer Veröffentlichung die SEO-/KI-Konsistenz. Pull Requests lösen kein Deployment aus und erhalten nur Leserechte. Veröffentlicht werden ausschließlich `index.html`, `llms.txt`, `llms-full.txt` und `sitemap.xml` aus einem eigenen Verzeichnis; Dokumentation und Prüfscripts bleiben außerhalb der Website. Neue öffentliche Dateien müssen im Kopierschritt und in `PUBLIC_FILES` des Prüfscripts ergänzt werden.

## SEO und Auffindbarkeit für KI-Systeme

Die erreichbare Projektadresse ist <https://immobilienmakler.github.io/Makler-Muenchen/>. Die Seite ist eine eigenständige Übersicht zu Leistungen, Tätigkeitsgebiet und Quellen. Ihre Canonical-URL, `og:url`, JSON-LD-Seitenadresse und Sitemap verwenden diese Projektadresse. Die Unternehmens- und Leistungs-URLs verweisen dagegen auf die jeweils zuständigen Seiten von **bayernwerte.de**. Bei einem Domain- oder Pfadwechsel müssen diese Projektadressen in HTML, Sitemap und beiden Textprofilen gemeinsam angepasst werden.

- `index.html`: deutsche Dokumentstruktur, ein H1, Titel, Beschreibung, Open Graph, Twitter Card, sichtbare FAQ und verlinkte Primärquellen. Alle wesentlichen Inhalte sind direkt im HTML verfügbar.
- JSON-LD: `RealEstateAgent` mit Anschrift, Telefon und Tätigkeitsgebiet, `WebPage`, fünf `Service`-Einträge und `FAQPage`. FAQ-Antworten entsprechen exakt dem sichtbaren Inhalt. Es werden keine Bewertungen, Preise, Öffnungszeiten oder Auszeichnungen erfunden.
- `llms.txt`: kompakter Quellenindex mit Unternehmensprofil, Leistungen, Kontakt und Links auf die Hauptwebsite.
- `llms-full.txt`: ausführlichere, eigenständige Zusammenfassung mit Quellen, Abgrenzung und Hinweisen zu dynamischen Objektdaten.
- `sitemap.xml`: enthält ausschließlich die kanonische HTML-Projektseite. Die Angebote und Sitemaps der Hauptwebsite werden dort nicht als eigene Inhalte ausgegeben.

**Quellenabgleich vom 12. November 2026:** Leistungen und Regionen wurden mit [llms.txt](https://bayernwerte.de/llms.txt) und [llms-full.txt](https://bayernwerte.de/llms-full.txt) der Hauptwebsite abgeglichen. Anschrift, Telefon, E-Mail und Inhaber wurden anhand von [Kontakt](https://bayernwerte.de/kontakt/) und [Impressum](https://bayernwerte.de/impressum/) geprüft. Die fünf Leistungen verlinken jeweils ihre Primärseite. Preise und Verfügbarkeit werden nicht kopiert; maßgeblich bleibt die aktuelle Objektseite. Bei einer späteren Pflege den Quellenabgleich erneut durchführen und das Prüfdatum erst danach ändern.

### Grenzen von GitHub Project Pages

`robots.txt` gilt ausschließlich unter dem Host-Root, hier `https://immobilienmakler.github.io/robots.txt`. Eine Datei unter `/Makler-Muenchen/robots.txt` steuert keine Crawler. Deshalb wird keine wirkungslose Projekt-robots.txt veröffentlicht. Änderungen am Root benötigen das separate Repository für `immobilienmakler.github.io` oder einen eigenen Host. Die Projekt-Sitemap kann in einer passenden Search-Console-Property eingereicht werden; das ist nicht automatisch erfolgt.

Auch die KI-Textdateien liegen unter dem Projektpfad. Sie sind über HTML-Links erreichbar. Am Root der Hauptwebsite sind bereits <https://bayernwerte.de/llms.txt> und <https://bayernwerte.de/llms-full.txt> vorhanden; diese bleiben die zentralen Unternehmensquellen und werden durch dieses Repository nicht verändert.

`llms.txt` ist ein ergänzendes Quellenformat, keine allgemein verbindliche Crawlersteuerung oder Trainingslizenz. Ob Suchmaschinen oder KI-Systeme diese Dateien verwenden, entscheiden die jeweiligen Anbieter. Strukturierte Daten und FAQ-Markup garantieren weder Rankings noch KI-Zitate oder Google-Rich-Results. Insbesondere sind Google-FAQ-Rich-Results für Immobilienseiten üblicherweise nicht vorgesehen.

### Lokale Konsistenzprüfung

```sh
python3 scripts/validate_site.py
```

Die Prüfung validiert Canonical-/Open-Graph-/Sitemap-Adressen, lokale Links und Anker, JSON-LD, die Übereinstimmung der FAQ mit dem HTML sowie zentrale Unternehmensdaten und Leistungsquellen in beiden KI-Texten. Sie läuft offline und ersetzt weder eine Prüfung aktueller externer Quellen noch einen vollständigen HTML-, Schema.org- oder Barrierefreiheitsaudit.

## Nutzungsrechte

Die bisherige Projektbeschreibung schließt eine kommerzielle Wiederverwendung aus. Eine separate Lizenzdatei liegt nicht vor; aus diesem Repository ergibt sich keine zusätzliche Nutzungserlaubnis. Fragen zu Nutzungsrechten bitte an Bayernwerte Immobilien richten.

## Kontakt

- Website: <https://bayernwerte.de/>
- E-Mail: <anfrage@bayernwerte.de>
- Telefon: [+49 89 21909733](tel:+498921909733)
- GitHub: [immobilienmakler](https://github.com/immobilienmakler)
