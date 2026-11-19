# 4 · Transkription

Die dünne, anbieterunabhängige Hülle um ein gemietetes Transkriptionsmodell und alles, was direkt aus dem Transkript entsteht (Ausbaustufe S2). Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „Die Transkriptionskomponente".

## Ziel

1. **Anbieter-Benchmark** an echtem Vorlesungsmaterial nach den Kriterien aus der Wissensbasis, als Entscheidungsvorlage für Nicolas. Cloud-Modelle sind zulässig; die Qualität geht vor dem Hosting-Standort, solange offengelegt wird, wohin die Aufzeichnungen gehen.
2. **Transkriptionskomponente** mit interner Schnittstelle `transcribe_batch(audio, language, vocabulary) -> Transcript` und je einem Adapter pro Anbieter.
3. **Tonspur-Extraktion** aus `recording.mp4` mit ffmpeg.
4. **`transcript.json`** mit Wort-Zeitstempeln und Konfidenz je Wort als zentrales Artefakt, abgelegt im Sitzungsordner.
5. **Fachbegriffsliste** beim Aufruf mitgeben. Einstieg: Wörter mit niedriger Konfidenz auswerten; wiederholt sich derselbe Begriff, gehört er auf die Liste.
6. **Nachkorrektur** des Transkripts durch ein Sprachmodell, ohne den Inhalt zu verändern; das Rohtranskript bleibt erhalten.
7. Daraus abgeleitet: **WebVTT-Untertitel** und **Sprungmarken**, ebenfalls im Sitzungsordner. Ausgeliefert werden sie von `ingest-delivery`.

`transcribe_stream` für die Echtzeitvariante baut das Paket `live-subtitles`, gegen dieselbe Schnittstelle und mit demselben Kriterienkatalog.

## Vorgehen beim Benchmark

Erst ein Überblick über die Anbieter, Cloud und lokal, als Liste im Teams-Kanal; dann ein bis zwei Anbieter an den Beispiel-Sitzungen testen und Qualität, Geschwindigkeit, Kosten und den Umgang mit Fachbegriffen festhalten. Wort-Zeitstempel sind Pflicht. Cloud zuerst, lokal danach. Erster Kandidat ist AssemblyAI (Empfehlung von Nicolas, 27.10.2026), daneben Whisper von OpenAI. Schlüssel fragt ihr bei Nicolas in Teams an (OpenAI und ElevenLabs sofort, Azure und Google auf Nachfrage). Bevor ihr weitere Anbieter selbst testet, sucht nach unabhängigen Benchmarks: Unterscheiden sich die Anbieter kaum, lohnt es nicht, alle zu testen. Haltet die Evidenz fest (Fehlerrate, Preis, EU-Verarbeitung), denn kritische Fragen zur Qualität werden kommen und der Bericht braucht die Zahlen.

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

Benchmark begonnen (Stand 13.11.2026): Gegen ein von Hand korrigiertes Referenztranskript wird eine Wortfehlerrate berechnet und mit dem Preis je Audiominute verrechnet. AssemblyAI kam auf den Beispiel-Sitzungen auf 0 % (Englisch) und 0,6 % (Deutsch). Das Material ist sauber gesprochen und kurz; für belastbare Werte braucht es längere, realistischere Aufnahmen, etwa eigene Testaufnahmen mit FLEX3 Light. Andere Anbieter sind bisher nur nach Preis eingeordnet.
