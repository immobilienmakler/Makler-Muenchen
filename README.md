# Immobilien München · Themen- und Quellenhub von Bayernwerte

Statischer, deutschsprachiger Themen- und Quellenhub für Bayernwerte Immobilien in München und Umgebung. Er hilft Besuchern, ihr Vorhaben einzuordnen, Fragen vorzubereiten und die passenden Ratgeber, Fachleistungen oder Angebote auf [bayernwerte.de](https://bayernwerte.de/) zu finden.

## Projektstand

Dieses Repository enthält den eigenständigen Themenhub `index.html` und den GitHub-Pages-Workflow. Die Darstellung funktioniert ohne ausführbares JavaScript, externe Schriftarten, Tracking oder Build-Abhängigkeiten. Ein nicht ausführbarer JSON-LD-Datenblock beschreibt Unternehmen, Leistungen und häufige Fragen.

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

Der Workflow prüft bei Pull Requests und vor einer Veröffentlichung die SEO-/KI-Konsistenz. Pull Requests lösen kein Deployment aus und erhalten nur Leserechte. Veröffentlicht werden ausschließlich `index.html`, `llms.txt`, `llms-full.txt`, `sitemap.xml`, `quellen.json` und `immobilien-vorbereitung.md` aus einem eigenen Verzeichnis; Dokumentation und Prüfscripts bleiben außerhalb der Website. Neue öffentliche Dateien müssen im Kopierschritt und in `PUBLIC_FILES` des Prüfscripts ergänzt werden.

## SEO und Auffindbarkeit für KI-Systeme

Die erreichbare Projektadresse ist <https://immobilienmakler.github.io/Makler-Muenchen/>. Die Seite ist ein eigenständiger Themenwegweiser mit Vorbereitungspunkten, Quellen und weiterführenden Links. Ihre Canonical-URL, `og:url`, JSON-LD-Seitenadresse und Sitemap verwenden diese Projektadresse. Die Unternehmens- und Leistungs-URLs verweisen dagegen auf die jeweils zuständigen Seiten von **bayernwerte.de**. Bei einem Domain- oder Pfadwechsel müssen diese Projektadressen in HTML, Sitemap und beiden Textprofilen gemeinsam angepasst werden.

- `index.html`: deutsche Dokumentstruktur, ein H1, Titel, Beschreibung, Open Graph, Twitter Card, sichtbare FAQ und verlinkte Primärquellen. Alle wesentlichen Inhalte sind direkt im HTML verfügbar.
- JSON-LD: `RealEstateAgent` mit Anschrift, Telefon und Tätigkeitsgebiet, `CollectionPage`, fünf `Service`-Einträge, `FAQPage`, eine `ItemList` für die Fachquellen und ein `DigitalDocument` für die Vorbereitungsliste. FAQ-Antworten entsprechen exakt dem sichtbaren Inhalt. Es werden keine Bewertungen, Preise, Öffnungszeiten oder Auszeichnungen erfunden.
- `llms.txt`: kompakter Quellenindex mit Unternehmensprofil, Leistungen, Kontakt und Links auf die Hauptwebsite.
- `llms-full.txt`: ausführlichere, eigenständige Zusammenfassung mit Quellen, Abgrenzung und Hinweisen zu dynamischen Objektdaten.
- `quellen.json`: sechs kuratierte Ratgeber mit Thema, Einordnung, Quellenadresse und Datum des redaktionellen Abgleichs. Dieselben Einträge sind sichtbar im HTML und als JSON-LD vorhanden.
- `immobilien-vorbereitung.md`: herunterladbare Vorbereitungsliste mit Fragen zum Vorhaben und zum Erstgespräch; sie wird lokal ausgefüllt.
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

Die Prüfung validiert Canonical-/Open-Graph-/Sitemap-Adressen, lokale Links und Anker, JSON-LD, die Übereinstimmung der FAQ mit dem HTML sowie zentrale Unternehmensdaten und Leistungsquellen in beiden KI-Texten. Zusätzlich gleicht sie den Quellenkatalog mit sichtbarem HTML, JSON-LD, KI-Profilen und Vorbereitungsliste ab. Sie läuft offline und ersetzt weder eine Prüfung aktueller externer Quellen noch einen vollständigen HTML-, Schema.org- oder Barrierefreiheitsaudit.

## Wie der Hub bayernwerte.de unterstützt

Der eigene Nutzen liegt in der Auswahl nach Vorhaben und der Vorbereitung des Erstgesprächs. Fünf Einstiege führen zu thematisch passenden Quellen, sechs Ratgeber werden kurz eingeordnet und eine Gesprächsliste lässt sich herunterladen. Die Primärseiten der Hauptwebsite bleiben für Beratung, ausführliche Fachinhalte und aktuelle Angebote zuständig. Es werden keine Stadtteil-Duplikate oder austauschbaren Suchwortseiten erzeugt.

Die Links sind normale, beschreibende HTML-Links ohne Weiterleitungsdienst. Die Hauptwebsite erhält dadurch zusätzliche thematische Zugänge; daraus folgt keine garantierte Übertragung von Autorität. Der selbstreferenzierende Canonical kennzeichnet den eigenständigen Wegweiser und ist kein Signal, das die Rankings von bayernwerte.de automatisch steigert. Inhaltlich gleiche Zweitveröffentlichungen sollten auf Duplikate geprüft und gegebenenfalls zusammengeführt werden.

Die Wirkung lässt sich nach Veröffentlichung über folgende Daten beurteilen, sofern die entsprechenden Konten vorhanden sind:

- **Search Console der Projektseite:** Indexierungsstatus, verarbeitete Sitemap, Suchanfragen, Impressionen und Klicks. Für einen Vorher-nachher-Vergleich Ausgangsstand und Veröffentlichungsdatum notieren.
- **Statistik von bayernwerte.de:** Verweise von `immobilienmakler.github.io`, deren Zielseiten und daraus entstehende Anfragen. Der Hub verwendet selbst kein Tracking und hängt keine Kampagnenparameter an die kanonischen Fachquellen an.
- **KI-Antworten:** Bei gleichbleibenden Testfragen Quellenlinks und Testdatum protokollieren. Einzelne Antworten sind wechselhaft und kein belastbarer Nachweis eines Rankingeffekts.

Es wurde keine Search-Console-Property, kein Analytics-Zugriff und keine automatische Rankingmessung eingerichtet. Die Veröffentlichung erfolgt weiterhin über den Pull Request und den Pages-Workflow.

## Nutzungsrechte

Die bisherige Projektbeschreibung schließt eine kommerzielle Wiederverwendung aus. Eine separate Lizenzdatei liegt nicht vor; aus diesem Repository ergibt sich keine zusätzliche Nutzungserlaubnis. Fragen zu Nutzungsrechten bitte an Bayernwerte Immobilien richten.

## Kontakt

- Website: <https://bayernwerte.de/>
- E-Mail: <anfrage@bayernwerte.de>
- Telefon: [+49 89 21909733](tel:+498921909733)
- GitHub: [immobilienmakler](https://github.com/immobilienmakler)
