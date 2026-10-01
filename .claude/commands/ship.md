---
description: Fertige Lösung einchecken – Review, Commit, Push und Pull Request
argument-hint: "[kurze Beschreibung der Änderung]"
---

Bring eine fertige Lösung über einen Pull Request nach GitHub. Beschreibung der Person: $ARGUMENTS

1. **Zweig prüfen.** `git branch --show-current`. Steht dort `main`, leg einen Aufgabenzweig an, benannt nach `knowledge-base/standards/git-workflow.md` (`<arbeitspaket>/<kurzes-thema>`, englisch, Kleinbuchstaben, Bindestriche), mit `git switch -c <name>`. Vorhandene Änderungen wandern dabei mit.

2. **Review.** Führ das Verfahren aus `.claude/commands/review.md` vollständig durch. Ohne bestandenes Review geht es nicht weiter; der Git-Hook würde den Commit ohnehin ablehnen.

3. **Commit.** Formulier die Commit-Message nach `git-workflow.md` (englisch, Imperativ, mit Präfix des Arbeitspakets), zeig sie der Person und committe nach ihrem Okay mit `git commit -m "<message>"`. Kein `-a`.

4. **Push.** `git push -u origin <zweig>`. Nie nach `main`, nie mit `--force`.

5. **Pull Request.** Gibt es für den Zweig noch keinen (`gh pr view`), leg ihn mit `gh pr create --base main` an. Titel wie die Commit-Message, Beschreibung auf Deutsch nach `.github/pull_request_template.md`: was die Änderung tut, wie sie geprüft wurde, was offen ist. Gibt es schon einen, reicht der Push.

6. **Abschließen.** Zeig den Link zum Pull Request und sag, dass Nicolas ihn prüft und zusammenführt. Danach `/update`, um wieder auf dem neuesten Stand zu sein.
