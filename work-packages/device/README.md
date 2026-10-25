# 2 · Gerät (Track H)

Alles bis einschließlich Übergabepunkt: Mischer, Kamera, Ton, Steuerrechner und dessen Software, Bedienung, Gehäuse und Aufbauanleitung. Das ist überwiegend Konfiguration fertiger Programme und Mechanik statt eigener Code. Hintergrund: `knowledge-base/architecture/system-overview.md`.

## Wie das Gerät bedient wird

Die Lehrperson stellt das Gerät hin, schließt **vier Kabel** an (Strom, Netzwerk, HDMI vom Laptop, HDMI zum Beamer), nimmt die **Kamera** heraus, die an einem festen Kabel am Gerät hängt, stellt sie auf und drückt **Aufnahme**. Das Display zeigt dafür nur drei große Tasten: Aufnahme, Pause, Stopp.

## Ziel

- MediaMTX nimmt den RTMP-Stream des Mischers entgegen, `ffmpeg -c copy` schreibt `recording.mp4`.
- Bitfocus Companion als Bedienoberfläche im Kiosk-Browser mit den drei Tasten Aufnahme, Pause, Stopp.
- Die Zuordnung („Wer zeichnet auf?“, „Welche Veranstaltung?“) ist vorgesehen; wo sie neben den drei Tasten bedient wird, legt Nicolas noch fest.
- Beim Aufnahmestart entsteht ein Sitzungsordner nach `knowledge-base/architecture/session-folder.md`.
- Store and Forward: Warteschlange fertiger Sitzungen, Upload an den Ingest-Endpunkt, Aufräumen erst nach bestätigtem Upload.
- Speicherüberwachung mit Upload-Verriegelung.
- Mechanik: Anschlussblende, Fuß und Transportfach für die Kamera am Kabel, Zugentlastung, Beamer-Durchschleife.

Konfigurationsdateien liegen unter `config/` (`config/mediamtx/`, `config/companion/`), Skripte unter `scripts/`. Stückliste, Gehäusedaten und Aufbauanleitung folgen später unter `hardware/`.

## Fertig, wenn (Version 1)

Eine dem Projekt fremde Lehrperson zeichnet allein nach der Kurzanleitung auf, und die Aufnahme landet im richtigen Kurs.

## Stand

Noch nicht besetzt. Bis dahin wird die vorhandene Hardware von Hand bedient und die Aufnahme über den Simulator-Weg eingespielt.
