# S2 – Transkription und Sprungmarken

Die dünne, anbieterunabhängige Hülle um ein gemietetes Transkriptionsmodell und alles, was direkt aus dem Transkript entsteht. Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „Die Transkriptionskomponente".

## Ziel

1. **Anbieter-Benchmark** an echtem Vorlesungsmaterial nach den Kriterien aus der Wissensbasis, als Entscheidungsvorlage für Nicolas.
2. **Transkriptionskomponente** mit interner Schnittstelle `transcribe_batch(audio, language, vocabulary) -> Transcript` und je einem Adapter pro Anbieter.
3. **Tonspur-Extraktion** aus `recording.mp4` mit ffmpeg.
4. **`transcript.json`** mit Wort-Zeitstempeln als zentrales Artefakt.
5. Daraus abgeleitet: **WebVTT-Untertitel** und **Sprungmarken**.

`transcribe_stream` für die Echtzeitvariante gehört zu S5 und wird dort gebaut, gegen dieselbe Schnittstelle.

## Fertig, wenn

- Benchmark: Die Entscheidungsvorlage liegt vor.
- Komponente: Für eine Simulator-Sitzung entstehen mit einem Befehl `transcript.json`, `.vtt` und Sprungmarken, und der Anbieter lässt sich per Konfiguration wechseln.

## Stand

Noch nicht begonnen.
