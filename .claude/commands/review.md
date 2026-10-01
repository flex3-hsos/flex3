---
description: Aktuelle Änderungen nach den Projektstandards prüfen und bei Erfolg für den Commit freigeben
---

Prüf die Änderungen der Person, bevor sie eingecheckt werden. Maßstab ist `knowledge-base/standards/code-review.md`; lies die Datei jetzt, auch wenn du sie zu kennen glaubst.

1. **Umfang feststellen.** `git status` und `git diff` bzw. `git diff --cached`. Klär mit der Person, welche Dateien zur Lösung gehören, und merk genau diese mit `git add <dateien>` vor. Nichts mit `git add -A` oder `git add .` vormerken.

2. **Außerhalb des Arbeitspakets?** Liegen vorgemerkte Dateien außerhalb des Ordners aus `local/profile.md`, halt an. Änderungen an `knowledge-base/`, `.claude/` oder `CLAUDE.md` gehören nicht in einen Commit der Person.

3. **Werkzeuge laufen lassen** mit dem Python aus `.venv`, beschränkt auf den Ordner des Arbeitspakets:
   - `python -m ruff check <ordner>`
   - `python -m ruff format --check <ordner>`
   - `python -m pytest <ordner>`, wenn es dort Tests gibt
   Formatierungsfehler darfst du mit `python -m ruff format <ordner>` beheben; danach neu vormerken.

4. **Inhaltlich prüfen.** Lies den vorgemerkten Diff vollständig und geh die Checkliste aus `code-review.md` durch: Korrektheit, Verständlichkeit, Konventionen, Daten und Geheimnisse, Tests, Dokumentation.

5. **Ergebnis.** Gib die Befunde als Liste aus, jeweils mit Datei, Zeile und Begründung, geordnet nach:
   - **muss**: blockiert den Commit,
   - **sollte**: deutlich besser, die Person entscheidet,
   - **Hinweis**: zum Lernen, blockiert nichts.
   Erkläre jeden Befund so, dass die Person ihn versteht.

6. **Beheben.** Behebt mit der Person alle „muss"-Befunde und fang danach bei Schritt 3 neu an. Ein Review gilt nur für genau den Stand, den du geprüft hast.

7. **Freigeben.** Erst wenn kein „muss"-Befund übrig ist und die Werkzeuge ohne Fehler laufen: `python .claude/hooks/guard_git.py stamp`. Sag der Person, dass sie jetzt mit `/ship` einchecken kann, und dass jede weitere Änderung ein neues Review braucht.
