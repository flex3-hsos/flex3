# S7 – Dubbing

Erzeugt nachträglich eine vertonte Fassung einer Aufzeichnung in einer anderen Sprache. Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „Dubbing".

## Ziel

Batch-Skript gegen die ElevenLabs-API. Es läuft **nur**, wenn `consent.voice_clone` in `session.json` gesetzt ist; ohne diese Freigabe ist höchstens eine neutrale Standardstimme denkbar. Das Ergebnis wird erst nach Freigabe durch die Lehrperson veröffentlicht.

## Fertig, wenn

Für eine Simulator-Sitzung mit Freigabe entsteht eine vertonte Fassung, und ohne Freigabe verweigert das Skript nachweislich die Arbeit.

## Stand

Geplant für P4 (ab Oktober 2027). Die rechtliche Prüfung des Stimmklons läuft vorher.
