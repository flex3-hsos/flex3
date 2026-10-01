---
description: Neuesten Stand von Wissensbasis und Projekt aus GitHub holen
---

Hol den aktuellen Stand von `main` und berichte, was sich geändert hat. Die Arbeit der Person darf dabei nicht verloren gehen.

1. **Lokale Änderungen sichern.** Prüf `git status --porcelain`.
   - Gibt es nicht eingecheckte Änderungen, frag, ob ihr sie zuerst mit `/ship` einchecken oder vorübergehend mit `git stash push -u -m "update <Datum>"` beiseitelegen sollt. Ohne Antwort nichts tun.

2. **Holen.** `git fetch origin`.

3. **Einspielen.**
   - Auf `main`: `git pull --ff-only origin main`.
   - Auf einem Aufgabenzweig: erst `main` aktualisieren (`git switch main`, `git pull --ff-only origin main`, `git switch -`), dann `git merge main` in den Aufgabenzweig. Kein Rebase, kein Force-Push.
   - Bei einem Konflikt: anhalten, die betroffenen Dateien zeigen und gemeinsam auflösen. Konflikte in `knowledge-base/`, `.claude/` oder `CLAUDE.md` immer zugunsten von `main` auflösen (`git checkout --theirs` beim Merge in den Aufgabenzweig), denn diese Dateien pflegt Nicolas.

4. **Zurückholen.** Wurde in Schritt 1 gestasht, `git stash pop` und prüfen, dass alles wieder da ist.

5. **Berichten.** Zeig mit `git log --oneline ORIG_HEAD..HEAD` bzw. dem Bereich vor und nach dem Pull, was neu ist, und fass zusammen:
   - neue oder geänderte Inhalte in `knowledge-base/`, in eigenen Worten und in zwei bis fünf Sätzen,
   - Änderungen am eigenen Arbeitspaket aus `local/profile.md`,
   - Änderungen an `CLAUDE.md` oder `.claude/`.

6. **Neu starten, wenn nötig.** Haben sich `CLAUDE.md` oder Dateien unter `.claude/` geändert, sag deutlich: Claude Code schließen und den Ordner neu öffnen, sonst gelten die alten Anweisungen weiter.
