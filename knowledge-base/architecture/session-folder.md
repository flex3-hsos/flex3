# Der Sitzungsordner – Vertrag zwischen Gerät und Software

Jede Aufzeichnung ist ein Ordner. Erzeugt wird er vom Gerät, vom Simulator oder von FLEX3 Light (Software auf dem Rechner der Lehrperson, eine Alternative zum Gerät); die Post-Pipeline verarbeitet ihn. **Dieser Vertrag wird nur in Absprache mit Nicolas geändert.**

| Datei | Inhalt | |
|---|---|---|
| `recording.mp4` | Programm-Mix inklusive Ton, H.264 / AAC 48 kHz, 1080p: das, was die Studierenden sehen | Pflicht |
| `session.json` | Metadaten der Sitzung | Pflicht |
| weitere Spuren, z. B. `camera.mp4`, `screen.mp4` | einzelne Quellen getrennt vom Mix, etwa Kamera und Bildschirm | optional |

## Zusätzliche Spuren

Seit dem 26.10.2026 darf ein Erzeuger neben `recording.mp4` weitere Video- oder Tonspuren in den Ordner legen. Für sie gilt:

- Sie heißen sprechend und englisch, etwa `camera.mp4`, `screen.mp4` oder `audio-mic.wav`.
- Sie beginnen im selben Moment wie `recording.mp4`, damit Zeitstempel aus dem Transkript auf alle Spuren passen.
- Sie stehen in `session.json` unter `tracks`, je Spur mit Datei und Art.

Die Post-Pipeline verarbeitet weiterhin `recording.mp4`. Der Ingest nimmt die übrigen Spuren unverändert mit und legt sie bei der Sitzung ab, damit spätere Schritte sie nutzen können, etwa das Bildschirmbild für Folientext oder das Mikrofon allein für die Transkription. Code, der einen Sitzungsordner liest, darf an zusätzlichen Dateien nicht scheitern.

## `session.json`

```json
{
  "session_id": "2026-11-12_digiprog_vl07",
  "status": "assigned",
  "course_name": "Digitalisierung und Programmierung",
  "instructor_id": "nimeseth",
  "instructor_name": "Prof. Dr. Nicolas Meseth",
  "recorded_at": "2026-11-12T10:00:00+01:00",
  "duration_sec": 5400,
  "room": "...",
  "language": "de",
  "ilias_course_id": "...",
  "opencast_series_id": "...",
  "consent": {
    "recording": true,
    "publication": true,
    "voice_clone": false
  },
  "consent_source": "register",
  "device_id": "flex3-01",
  "software_version": "1.2.0",
  "tracks": [
    { "file": "camera.mp4", "kind": "camera" },
    { "file": "screen.mp4", "kind": "screen" }
  ]
}
```

| Feld | Bedeutung |
|---|---|
| `session_id` | eindeutig, Muster `<Datum>_<Kurskürzel>_<Sitzung>` |
| `status` | `assigned` (Kurs und Lehrperson bekannt) oder `unassigned` („Gast / später" am Gerät gewählt) |
| `recorded_at` | Beginn der Aufnahme, ISO 8601 mit Zeitzone |
| `duration_sec` | Länge in Sekunden |
| `language` | Sprache der Vorlesung als ISO-639-1-Code |
| `ilias_course_id`, `opencast_series_id` | Ziel der Bereitstellung, aus dem Nutzerregister |
| `consent.recording` | Aufzeichnung erlaubt |
| `consent.publication` | Veröffentlichung im Kurs erlaubt |
| `consent.voice_clone` | Dubbing mit nachgebildeter Stimme erlaubt; am Gerät nie setzbar |
| `consent_source` | `register` (Freigaben aus dem Nutzerregister) oder `restricted_on_device` (am Gerät für diese Sitzung eingeschränkt) |
| `device_id` | welches Gerät aufgezeichnet hat; der Simulator verwendet `simulator` |
| `software_version` | Version der Gerätesoftware bzw. des Simulators |
| `tracks` | optional: zusätzliche Spuren, je Eintrag `file` und `kind` (`camera`, `screen`, `audio` …); fehlt, wenn es nur `recording.mp4` gibt |

## Regeln für die Verarbeitung

- **Unzugeordnete Sitzungen** (`unassigned`) werden regulär hochgeladen, landen aber in einer Warteschlange zur Nachbearbeitung statt direkt im Kurs.
- **Freigaben sind verbindlich.** Ohne `consent.publication` wird nichts im Kurs sichtbar, ohne `consent.voice_clone` gibt es kein Dubbing mit nachgebildeter Stimme.
- **Unbekannte Felder** werden ignoriert, damit der Vertrag erweitert werden kann, ohne bestehenden Code zu brechen. **Fehlende Pflichtfelder** führen zu einem klaren Fehler im Log und nie zum stillen Verwerfen der Aufzeichnung.

## Abgeleitete Artefakte

Die Post-Pipeline legt ihre Ergebnisse neben die Eingabe, damit eine Sitzung jederzeit nachvollziehbar und jeder Schritt wiederholbar ist:

| Datei | erzeugt von | Inhalt |
|---|---|---|
| `audio.*` | S2 | aus dem Video extrahierte Tonspur |
| `transcript.json` | S2 | Rohtranskript mit Wort-Zeitstempeln; **das zentrale Artefakt**, aus dem alles Weitere abgeleitet wird |
| `subtitles.<sprache>.vtt` | S2 | Untertitel als WebVTT |
| `chapters.json` | S2 | Sprungmarken |
| `summary.<sprache>.md` und weitere | S3 | Zusammenfassung, einfache Sprache, Quiz |

Die genauen Formate legt das jeweilige Arbeitspaket in seinem README fest.
