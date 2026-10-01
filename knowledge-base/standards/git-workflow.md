# Git-Workflow

## Das Prinzip

`main` enthält nur geprüften Code, der zusammengeführt wurde. Niemand arbeitet direkt auf `main`. Jede Aufgabe bekommt einen eigenen Zweig, und eine fertige Lösung kommt über einen Pull Request zurück, den Nicolas prüft und zusammenführt.

```
main ──●──────────────●──────────────●──►
        \            / (Pull Request) \
         ●──●──●────●                  ●──●──► nächste Aufgabe
         s2-transcription/benchmark-script
```

Den Ablauf übernimmt der Assistent mit `/ship`; ihr müsst die Befehle nicht auswendig kennen.

## Zweige

**Name:** `<arbeitspaket>/<kurzes-thema>`, englisch, Kleinbuchstaben, Bindestriche.

```
s2-transcription/benchmark-script
s3-ai-content/summary-prompt
device-simulator/file-simulator
```

Ein Zweig gehört zu genau einer Aufgabe und lebt höchstens zwei Wochen. Ist der Pull Request zusammengeführt, beginnt die nächste Aufgabe auf einem neuen Zweig von einem aktuellen `main`.

## Commits

**Message:** englisch, Imperativ, mit dem Arbeitspaket als Präfix, höchstens 72 Zeichen in der ersten Zeile.

```
s2-transcription: add batch adapter for provider X
device-simulator: write session.json with consent defaults
s3-ai-content: fix empty summary for short transcripts
```

Bei Bedarf folgt nach einer Leerzeile eine kurze Erklärung, warum die Änderung nötig war.

- Ein Commit ist eine in sich stimmige Änderung, die durch `/review` gegangen ist.
- Vorgemerkt werden nur die Dateien, die zur Lösung gehören, einzeln mit `git add <datei>`, nie pauschal mit `git add .` oder `git commit -a`.
- Keine Commits, die nur „wip" oder „fix" heißen.

## Pull Requests

- Ziel ist immer `main`.
- Titel wie die Commit-Message, Beschreibung auf Deutsch nach der Vorlage: was die Änderung tut, wie sie geprüft wurde, was offen ist.
- Ein Pull Request betrifft nur ein Arbeitspaket.
- Nicolas prüft und führt zusammen. Gibt es Rückfragen, ergänzt ihr auf demselben Zweig und pusht erneut; der Pull Request aktualisiert sich von selbst.

## Was der Assistent durchsetzt

Ein Hook in `.claude/hooks/guard_git.py` blockiert:

- Commits ohne bestandenes `/review` für genau die vorgemerkten Änderungen,
- Commits auf `main`,
- `git commit -a`,
- Pushes nach `main` und Force-Pushes.

## Auf dem neuesten Stand bleiben

`/update` holt den aktuellen Stand von `main` und führt ihn in euren Zweig zusammen, ohne Rebase und ohne Force-Push. Macht das vor jeder neuen Aufgabe und immer, wenn Nicolas ein Update ansagt.

## Was ihr nicht ändert

`knowledge-base/`, `.claude/`, `CLAUDE.md`, `.github/` und `pyproject.toml` pflegt Nicolas. Fehler oder Wünsche dazu bringt ihr ins Weekly.
