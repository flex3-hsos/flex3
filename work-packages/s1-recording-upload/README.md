# S1 – Aufzeichnung und Upload

Bringt eine fertige Sitzung vom Gerät in den ILIAS-Kurs. Hintergrund: `knowledge-base/architecture/post-pipeline.md`.

## Ziel

- **Ingest-Endpunkt** auf dem FLEX³-Server, der Sitzungsordner vom Gerät annimmt, nur mit gültigem Geräte-Token.
- **Upload nach Opencast** über die External API, in die Series aus `session.json`; über die bestehende ILIAS-Opencast-Anbindung erscheint die Aufzeichnung im Kurs.
- Freigaben beachten: ohne `consent.publication` nicht im Kurs sichtbar; `unassigned`-Sitzungen in eine Warteschlange zur Nachbearbeitung.

Erster Schritt: den Upload einmal von Hand in Opencast durchspielen, dann als Skript. Die Spezifikation kommt von Nicolas.

## Fertig, wenn

Ein Video aus dem Simulator landet mit einem Befehl automatisch in Opencast und ist im ILIAS-Testkurs sichtbar.

## Stand

Noch nicht begonnen.
