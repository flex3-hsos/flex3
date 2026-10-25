# 7 · Live-Untertitel

Das schwerste Paket des Projekts: Untertitel live, optional übersetzt (Ausbaustufe S5, als Versuch S6). Deshalb in drei Teile geschnitten, die nacheinander nutzbar sind. Hintergrund: `knowledge-base/architecture/live-pipeline.md`.

## Ziel

| Teil | Inhalt | Wert für sich allein |
|---|---|---|
| **7a** Anbieterwahl und Prototyp | Evaluationsverfahren für Streaming-Spracherkennung, Anbieterranking, Prototyp mit `transcribe_stream` gegen die Schnittstelle aus `transcription` | Entscheidungsgrundlage, Risiko aus dem kritischen Pfad genommen |
| **7b** Untertitel im Hörsaal | Untertiteltext über WebSocket auf Laptop oder Handy, 1–2 Sekunden hinter der gesprochenen Sprache, optional übersetzt | das eigentliche Nutzungsszenario für internationale Studierende, ohne Video und ohne Synchronisationsproblem |
| **7c** Untertitel zu Hause | in LL-HLS eingebettet und um die Streamlatenz verzögert | erst mit eigener Auslieferung aus `livestream` |

Die **übersetzte Audiospur (S6)** ist eine Erweiterung von 7b um Sprachausgabe in der Zielsprache und gilt nur als Versuch.

**Noch offen:** Die Teile 7b und 7c folgen einer von drei Varianten, wie die Untertitel ausgespielt werden (getrennt nach Publikum, ein Videostream mit Untertiteln für alle, oder Untertitel im Beamerbild). Je nach Entscheidung ändert sich der Zuschnitt. Nicolas entscheidet vor P2.

## Fertig, wenn

- 7a: Ranking und Prototyp liegen vor; der Prototyp liefert aus dem Live-Simulator Untertitel.
- 7b: Mit dem Live-Simulator erscheinen Untertitel auf Laptop und Handy, höchstens zwei Sekunden hinter der Sprache.
- 7c: Untertitel laufen im Stream für Studierende zu Hause synchron zum Bild.

## Stand

7a läuft im Rahmen einer Bachelorarbeit; 7b geplant für P2 (April bis Juli 2027).
