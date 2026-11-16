# 5 · KI-Inhalte

Erzeugt aus `transcript.json` Inhalte, die Studierenden beim Nacharbeiten helfen (Ausbaustufe S3). Die Arbeit liegt im Formulieren und systematischen Prüfen der Ergebnisse, kaum im Code. Hintergrund: `knowledge-base/architecture/post-pipeline.md`, Abschnitt „KI-Inhalte".

## Ziel

- **Übersetzung** der Transkripte als erster Schritt (13.11.2026): vorschlagen, womit übersetzt wird, ein spezialisierter Dienst wie DeepL oder Azure Translator oder ein Sprachmodell, nach Qualität und Kosten. Möglichst dieselbe Technik wie bei der Live-Übersetzung (`live-subtitles`), damit es keine Qualitätsunterschiede gibt; dazu mit der Bachelorarbeit zu den Live-Untertiteln abstimmen.
- Zusammenfassung, Fassung in einfacher Sprache, Themenübersicht und Quiz aus einem Transkript.
- **Prompt-Bibliothek** unter `prompts/`: jede Vorlage als eigene Datei, versioniert und ohne Programmierkenntnis verbesserbar.
- **Fachbegriffslisten** aus den Foliensätzen der Pilotmodule, als Eingabe für die Transkription und die Prompts.
- Die Ergebnisse landen im Sitzungsordner, gekennzeichnet als KI-generiert. Ausgeliefert werden sie von `ingest-delivery`, nach Prüfung und Freigabe durch die Lehrperson.

## Fertig, wenn

Für eine Simulator-Sitzung mit Transkript entstehen mit einem Befehl alle vier Inhalte, und die Ergebnisse sind gut genug, dass eine Lehrperson sie freigeben würde.

## Stand

Recherche zu Übersetzungsdiensten begonnen; ein Transkript als Arbeitsgrundlage kommt aus dem Paket `transcription`. Offizieller Start ab Dezember 2026.
