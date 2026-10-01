# Konventionen

## Sprache

**Alles Maschinenlesbare ist Englisch, alles für Menschen Geschriebene ist Deutsch.**

| Englisch | Deutsch |
|---|---|
| Variablen-, Funktions-, Klassen- und Dateinamen | README der Arbeitspakete |
| Feldnamen und deren Werte (`"status": "assigned"`, nicht `"zugeordnet"`) | Wissensbasis |
| Konfigurationsschlüssel, Umgebungsvariablen | Pull-Request-Beschreibungen |
| Kommentare und Docstrings im Code | Gespräche mit dem Assistenten |
| Log-Ausgaben und Fehlermeldungen im Code | Meldungen, die Lehrende oder Studierende in einer Oberfläche sehen |
| Commit-Messages, Zweignamen | |

Inhaltliche Nutzdaten behalten ihre Sprache: Ein Modultitel bleibt „Digitalisierung und Programmierung", eine deutsche Zusammenfassung bleibt deutsch.

**Keine gemischtsprachigen Bezeichner** wie `lehrperson_id` oder `get_vorlesung()`; richtig sind `instructor_id` und `get_lecture()`.

## Benennung

| Was | Schreibweise | Beispiel |
|---|---|---|
| Ordner und Dateien | Kleinbuchstaben, Bindestriche (Python-Module: Unterstriche) | `work-packages/s2-transcription/`, `transcript_writer.py` |
| Python-Funktionen und Variablen | `snake_case` | `extract_audio()` |
| Python-Klassen | `PascalCase` | `TranscriptSegment` |
| Konstanten | `UPPER_SNAKE_CASE` | `DEFAULT_LANGUAGE` |
| Umgebungsvariablen | `FLEX3_` + `UPPER_SNAKE_CASE` | `FLEX3_DATA_DIR`, `FLEX3_OPENCAST_URL` |
| JSON-Felder | `snake_case` | `recorded_at`, `duration_sec` |

## Aufbau eines Arbeitspakets

Jedes Arbeitspaket unter `work-packages/` folgt demselben Aufbau, soweit es die Teile braucht:

```
work-packages/<arbeitspaket>/
  README.md            Ziel, Stand, Bedienung, Schnittstellen – Deutsch
  requirements.txt     Laufzeitabhängigkeiten mit festen Versionen
  .env.example         benötigte Umgebungsvariablen, ohne echte Werte
  src/<paketname>/     der Code
  tests/               Tests mit pytest
  scripts/             kleine Kommandozeilenskripte
  prompts/             Prompt-Vorlagen (S3, S5, S6)
  config/              Konfigurationsdateien fertiger Programme (Companion, MediaMTX, OBS)
```

## Daten und Zeit

- Zeitpunkte im Format ISO 8601 mit Zeitzone: `2026-11-12T10:00:00+01:00`.
- Dauern als Zahl mit Einheit im Namen: `duration_sec`, `offset_ms`.
- Sprachen als ISO-639-1-Code: `de`, `en`, `uk`.
- Dateien in UTF-8.
