# S5 – Echtzeit-Untertitel

Das schwierigste Stück des Projekts: übersetzte Untertitel live, für zwei Zielgruppen mit unterschiedlichen Zeitbasen. Hintergrund: `knowledge-base/architecture/live-pipeline.md`.

## Ziel

- Ton aus dem Live-Stream an eine Realtime-API, Untertitel und Übersetzung zurück; `transcribe_stream` gegen die Schnittstelle aus S2.
- **Im Hörsaal:** reiner Untertiteltext über WebSocket, 1–2 Sekunden hinter der gesprochenen Sprache.
- **Zu Hause:** Low-Latency-HLS mit eingebetteten Untertiteln, verzögert passend zum Bild.

## Fertig, wenn

Mit dem Live-Simulator laufen beide Ausspielwege gleichzeitig, und die Untertitel sind im jeweiligen Kanal synchron.

## Stand

Geplant für P2 (April bis Juli 2027).
