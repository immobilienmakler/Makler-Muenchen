# Immobilien Anbieter Webseite

Diese Repository enthält Dateien und Anleitungen für den Betrieb der Bayernwerte Immobilien-Website mit Anbindung an die Maklersoftware "Ilogu" über die OpenImmo-Schnittstelle.

## Projektübersicht

Die Website von [Bayernwerte Immobilien](https://www.bayernwerte.de) stellt Immobilienangebote in München und Umgebung dar und wird durch aktuelle Objektdaten aus Ilogu automatisch aktualisiert. Die Datenübertragung erfolgt via FTP, und Bilder werden mittels Bildbearbeitung optimiert. Über die **WordPress CLI und Iframe** werden alle Daten in die Website integriert, um Nutzern immer die aktuellsten Immobilienangebote präsentieren zu können.

## Technologie-Stack

- **Ilogu mit OpenImmo-Schnittstelle**: Übergabe von Objektdaten via FTP.
- **Bildbearbeitung**: Bildbearbeitung zur Optimierung der Darstellung.
- **WordPress CLI & Iframe**: Automatisierte Integration der Daten in die WordPress-Seite.
- **GitHub**: Versionskontrolle und Dokumentation des Projekts.
- **Werkzeuge**: BayernAtlas für Grundstücksinformationen

## Funktionen

### Immobilien in München

Bayernwerte Immobilien ist Ihr kompetenter Partner für Immobilien in München und Umgebung. Unser Standort in München bietet umfassende Beratung und Betreuung, von der Bewertung über die Vermarktung bis hin zur Vermittlung.

### Immobilienbewertung

Wir bieten zwei Bewertungsoptionen:
1. **Online-Bewertung** – kostenlos und direkt auf unserer Website verfügbar.
2. **Verkehrswertgutachten** – ausführliche und detaillierte Gutachten für höchste Entscheidungssicherheit.

## Einrichtung und Betrieb

1. **Ilogu-Datenintegration**: Die Objektdaten werden regelmäßig über die OpenImmo-Schnittstelle via FTP an den Webserver übertragen.
2. **Bildbearbeitung mit künstlicher Inteligenz**: Bilder werden automatisch für die optimale Darstellung auf der Website bearbeitet.
3. **WordPress CLI & Iframe**: Nach der Verarbeitung der Daten werden diese automatisiert in die WordPress-Installation eingepflegt.

## Lizenz

Dieses Projekt steht unter der Bayernwerte-Immobilien-Lizenz und ist nicht für die kommerzielle Wiederverwendung freigegeben.

## Kontakt

Für weitere Fragen und Informationen zu Bayernwerte Immobilien:
- **Website**: [www.bayernwerte.de](https://www.bayernwerte.de)
-  **Github**: [Immobilienmakler München](https://immobilienmakler.github.io/Makler-Muenchen/)
- **Email**: anfrage@bayernwerte.de
- **Telefon**: +49-(0)89-21909733

## DSGVO konforme Upstream-DNS-Server
- https://dns.mullvad.net/dns-query
- https://dns10.quad9.net/dns-query
- https://dns.quad9.net/dns-query
- https://doh.ffmuc.net/dns-query
- https://dnsforge.de/dns-query
- https://dns.digitale-gesellschaft.ch/dns-query
- https://unfiltered.adguard-dns.com/dns-query
- https://doh.libredns.gr/dns-query
- https://doh-de.blahdns.com/dns-query
