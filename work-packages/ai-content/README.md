# 5 · KI-Inhalte

Erzeugt aus `transcript.json` Inhalte, die Studierenden beim Nacharbeiten helfen (Ausbaustufe S3). Die Arbeit liegt im Formulieren und systematischen Prüfen der Ergebnisse, kaum im Code. Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „KI-Inhalte".

## Ziel

- Zusammenfassung, Fassung in einfacher Sprache, Themenübersicht und Quiz aus einem Transkript.
- **Prompt-Bibliothek** unter `prompts/`: jede Vorlage als eigene Datei, versioniert und ohne Programmierkenntnis verbesserbar.
- **Fachbegriffslisten** aus den Foliensätzen der Pilotmodule, als Eingabe für die Transkription und die Prompts.
- Die Ergebnisse landen im Sitzungsordner, gekennzeichnet als KI-generiert. Ausgeliefert werden sie von `ingest-delivery`, nach Prüfung und Freigabe durch die Lehrperson.

## Fertig, wenn

Für eine Simulator-Sitzung mit Transkript entstehen mit einem Befehl alle vier Inhalte, und die Ergebnisse sind gut genug, dass eine Lehrperson sie freigeben würde.

## Stand

Noch nicht begonnen.
