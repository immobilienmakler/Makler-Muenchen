# Makler München · Bayernwerte Immobilien

Statische, deutschsprachige Informationsseite für Bayernwerte Immobilien in München und Umgebung. Sie stellt Leistungen und Kontaktmöglichkeiten vor und verweist für aktuelle Immobilienangebote auf [bayernwerte.de](https://bayernwerte.de/).

## Projektstand

Dieses Repository enthält die eigenständige Landingpage `index.html` und den GitHub-Pages-Workflow. HTML und CSS funktionieren ohne JavaScript, externe Schriftarten, Tracking oder Build-Abhängigkeiten.

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
- Eine Canonical-URL oder `og:url` erst ergänzen, wenn die verbindliche öffentliche URL und das Verhältnis zur Hauptwebsite festgelegt sind.

## Veröffentlichung

In den Repository-Einstellungen unter **Pages → Build and deployment → Source** die Option **GitHub Actions** auswählen. Der vorhandene Workflow `.github/workflows/static.yml` veröffentlicht bei Pushes auf `main` oder manuellem Start die statische Seite. Änderungen über einen Pull Request werden erst nach dem Zusammenführen veröffentlicht.

Der Workflow lädt ausschließlich `index.html` aus einem eigenen Veröffentlichungsverzeichnis hoch. Dokumentation und interne Projektdateien werden dadurch nicht Teil der Website. Werden später lokale Bilder, Stylesheets oder weitere Seiten ergänzt, muss der Kopierschritt im Workflow entsprechend erweitert werden.

## Nutzungsrechte

Die bisherige Projektbeschreibung schließt eine kommerzielle Wiederverwendung aus. Eine separate Lizenzdatei liegt nicht vor; aus diesem Repository ergibt sich keine zusätzliche Nutzungserlaubnis. Fragen zu Nutzungsrechten bitte an Bayernwerte Immobilien richten.

## Kontakt

- Website: <https://bayernwerte.de/>
- E-Mail: <anfrage@bayernwerte.de>
- Telefon: [+49 89 21909733](tel:+498921909733)
- GitHub: [immobilienmakler](https://github.com/immobilienmakler)
