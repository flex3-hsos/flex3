# Wissensbasis FLEX³

Alles, was der Projektassistent über FLEX³ wissen muss. Gepflegt von Nicolas; Änderungen kommen über `/update` zu euch.

## Lesereihenfolge

Für den Einstieg reichen die ersten vier Dateien. Den Rest liest der Assistent, wenn eine Aufgabe ihn braucht.

1. [project/overview.md](project/overview.md) – worum es geht und für wen
2. [architecture/design-principles.md](architecture/design-principles.md) – die drei Leitgedanken, nach denen alles gebaut wird
3. [architecture/system-overview.md](architecture/system-overview.md) – wie die Teile zusammenhängen
4. [standards/conventions.md](standards/conventions.md) – Sprache und Benennung

## Projekt

| Datei | Inhalt |
|---|---|
| [project/overview.md](project/overview.md) | Ziel, Funktionen, Zielgruppen, Pilotmodule |
| [project/roadmap.md](project/roadmap.md) | Ausbaustufen S1–S7, Phasen, Meilensteine |
| [project/team.md](project/team.md) | Rollen, Rhythmus, wie wir zusammenarbeiten |

## Architektur

| Datei | Inhalt |
|---|---|
| [architecture/design-principles.md](architecture/design-principles.md) | Leitgedanken: ein Übergabepunkt, kaufen statt bauen, die Aufzeichnung geht nie verloren |
| [architecture/system-overview.md](architecture/system-overview.md) | Gerät, Post-Pipeline und Live-Pipeline im Überblick |
| [architecture/session-folder.md](architecture/session-folder.md) | **der Vertrag** zwischen Gerät und Software: Sitzungsordner und `session.json` |
| [architecture/device-simulator.md](architecture/device-simulator.md) | wie ihr ohne Hardware entwickelt und testet |
| [architecture/post-pipeline.md](architecture/post-pipeline.md) | Ingest, Opencast, Transkription, KI-Inhalte, Dubbing |
| [architecture/live-pipeline.md](architecture/live-pipeline.md) | Livestream, Echtzeit-Untertitel, Audiospur |
| [architecture/decisions.md](architecture/decisions.md) | getroffene Designentscheidungen mit Begründung |

## Standards

| Datei | Inhalt |
|---|---|
| [standards/conventions.md](standards/conventions.md) | Sprache, Benennung, Ordner |
| [standards/python.md](standards/python.md) | Coding-Standards für Python |
| [standards/git-workflow.md](standards/git-workflow.md) | Zweige, Commits, Pull Requests |
| [standards/code-review.md](standards/code-review.md) | Checkliste für `/review` |
| [standards/data-protection.md](standards/data-protection.md) | was nie ins Repository darf |

## Nachschlagen

[glossary.md](glossary.md) erklärt die Begriffe, die im Projekt ständig fallen, etwa ATEM, RTMP, Opencast und WebVTT.
