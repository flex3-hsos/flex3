# Testdaten

## `sessions/` – Beispiel-Sitzungen

Zwei fertige Sitzungsordner nach dem Vertrag in `knowledge-base/architecture/session-folder.md`, damit jedes Arbeitspaket sofort nach dem Klonen testen kann, ohne auf das Gerät oder den Simulator zu warten.

| Ordner | Veranstaltung | Sprache | Länge |
|---|---|---|---|
| `2026-10-06_pvwp_excerpt-de` | Planung und Vorbereitung wissenschaftlicher Projekte | Deutsch | 5:07 |
| `2026-10-22_aai_excerpt-en` | Applications of Artificial Intelligence | Englisch | 4:54 |

Je Ordner liegen `recording.mp4` (H.264, AAC 48 kHz, 1920 × 1080) und `session.json`.

**Woher sie kommen:** Ausschnitte aus Vorlesungen von Nicolas Meseth, die ohnehin öffentlich auf YouTube stehen. Zu sehen und zu hören ist nur er; Studierende kommen nicht vor. Nicolas hat die Ausschnitte am 26.10.2026 für dieses Repository freigegeben. Sie sind die einzige Ausnahme von der Regel, dass keine Aufzeichnungen ins Repository gehören (`knowledge-base/standards/data-protection.md`).

**Was ihr wissen müsst:**

- In `session.json` steht `consent.publication: false`. Die Ausschnitte dürfen verarbeitet werden, aber nie in einem echten Kurs erscheinen; Code, der Freigaben beachtet, darf sie also nicht veröffentlichen.
- `ilias_course_id`, `opencast_series_id` und `room` sind Platzhalter (`test`). Die Uhrzeit in `recorded_at` ist unbekannt und auf 00:00 gesetzt.
- Das Feld `test_note` erklärt die Herkunft. Unbekannte Felder ignoriert die Pipeline laut Vertrag.
- Was eure Pakete aus einer Sitzung erzeugen (`transcript.json`, Untertitel, Zusammenfassungen), schreibt ihr in eine **Kopie** der Ordner unter `FLEX3_DATA_DIR`, nicht hierher. Ergebnisse echter Aufzeichnungen gehören nicht ins Repository.
- Weitere Aufzeichnungen kommen nur mit ausdrücklicher Freigabe von Nicolas dazu.
