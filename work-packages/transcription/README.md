# 4 · Transkription

Die dünne, anbieterunabhängige Hülle um ein gemietetes Transkriptionsmodell und alles, was direkt aus dem Transkript entsteht (Ausbaustufe S2). Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „Die Transkriptionskomponente".

## Ziel

1. **Anbieter-Benchmark** an echtem Vorlesungsmaterial nach den Kriterien aus der Wissensbasis, als Entscheidungsvorlage für Nicolas. Cloud-Modelle sind zulässig; die Qualität geht vor dem Hosting-Standort, solange offengelegt wird, wohin die Aufzeichnungen gehen.
2. **Transkriptionskomponente** mit interner Schnittstelle `transcribe_batch(audio, language, vocabulary) -> Transcript` und je einem Adapter pro Anbieter.
3. **Tonspur-Extraktion** aus `recording.mp4` mit ffmpeg.
4. **`transcript.json`** mit Wort-Zeitstempeln als zentrales Artefakt, abgelegt im Sitzungsordner.
5. Daraus abgeleitet: **WebVTT-Untertitel** und **Sprungmarken**, ebenfalls im Sitzungsordner. Ausgeliefert werden sie von `ingest-delivery`.

`transcribe_stream` für die Echtzeitvariante baut das Paket `live-subtitles`, gegen dieselbe Schnittstelle und mit demselben Kriterienkatalog.

## Testmaterial

Für dieses Paket gedacht sind die beiden Beispiel-Sitzungen unter `testdata/sessions/` (`testdata/README.md`):

| Sitzung | Sprache | Länge | Was sie prüft |
|---|---|---|---|
| `2026-10-06_pvwp_excerpt-de` | Deutsch | 5:07 | deutsche Vorlesung mit Fachbegriffen aus dem KI-Bereich; der Originalton hatte nur 16 kHz |
| `2026-10-22_aai_excerpt-en` | Englisch | 4:54 | englische Vorlesung eines deutschsprachigen Dozenten |

Beide nehmt ihr für die Entwicklung der Komponente und für die ersten Läufe des Benchmarks; die Sprache steht jeweils in `session.json` unter `language`. Für den vollständigen Benchmark kommen später längere Aufzeichnungen unter `FLEX3_DATA_DIR` dazu. Ergebnisse schreibt ihr in eine Kopie des Sitzungsordners unter `FLEX3_DATA_DIR`, nie nach `testdata/`.

## Fertig, wenn

- Benchmark: Die Entscheidungsvorlage liegt vor.
- Komponente: Für beide Beispiel-Sitzungen und für jede Simulator-Sitzung entstehen mit einem Befehl `transcript.json`, `.vtt` und Sprungmarken, und der Anbieter lässt sich per Konfiguration wechseln.

## Stand

Noch nicht begonnen.
