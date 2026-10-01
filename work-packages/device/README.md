# Gerät (Track H)

Alles, was auf dem Steuerrechner im Gerät läuft, bis einschließlich Übergabepunkt. Das ist überwiegend Konfiguration fertiger Programme statt eigener Code. Hintergrund: `knowledge-base/architecture/system-overview.md`.

## Ziel

- MediaMTX nimmt den RTMP-Stream des Mischers entgegen, `ffmpeg -c copy` schreibt `recording.mp4`.
- Bitfocus Companion als Bedienoberfläche im Kiosk-Browser, mit den zwei Seiten zur Zuordnung („Wer zeichnet auf?", „Welche Veranstaltung?").
- Beim Aufnahmestart entsteht ein Sitzungsordner nach `knowledge-base/architecture/session-folder.md`.
- Store and Forward: Warteschlange fertiger Sitzungen, Upload an den Ingest-Endpunkt, Aufräumen erst nach bestätigtem Upload.
- Speicherüberwachung mit Upload-Verriegelung.

Konfigurationsdateien liegen unter `config/` (`config/mediamtx/`, `config/companion/`), Skripte unter `scripts/`. Stückliste, Gehäusedaten und Aufbauanleitung folgen später unter `hardware/`.

## Fertig, wenn (Version 1, Dezember 2026)

Eine dem Projekt fremde Lehrperson zeichnet allein nach der Kurzanleitung auf, und die Aufnahme landet im richtigen Kurs.

## Stand

Noch nicht besetzt.
