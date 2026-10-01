---
description: Erster Start im FLEX³-Repository – Werkzeuge prüfen, Python-Umgebung einrichten, Arbeitspaket festhalten
---

Führe die Person Schritt für Schritt durch den ersten Start. Erklär bei jedem Schritt in einem Satz, wozu er dient. Geh erst weiter, wenn der Schritt geklappt hat.

1. **Begrüßen und kennenlernen.** Frag nach dem Vornamen, wie die Person angesprochen werden möchte, und an welchem Arbeitspaket sie arbeitet. Zeig dazu die Liste aus `work-packages/README.md`. Weiß sie es nicht, verweis auf Nicolas.

2. **Werkzeuge prüfen und fehlende installieren.** Die Person hat bisher nur Claude Code installiert; alles andere übernimmst du. Stell zuerst das Betriebssystem fest. Prüf dann:
   - `git --version`
   - `python --version`, mindestens 3.12; unter Windows auch `py --version`
   - `code --version` (VS Code)
   - `gh --version` (GitHub CLI)

   Fehlt etwas oder ist es zu alt, sag, was du installieren willst, und installier es nach ihrem Okay mit dem Paketmanager des Systems:

   | Werkzeug | Windows (`winget`) | macOS (`brew`) |
   |---|---|---|
   | Git | `winget install --id Git.Git -e` | `brew install git` |
   | Python | `winget install --id Python.Python.3.12 -e` | `brew install python@3.12` |
   | VS Code | `winget install --id Microsoft.VisualStudioCode -e` | `brew install --cask visual-studio-code` |
   | GitHub CLI | `winget install --id GitHub.cli -e` | `brew install gh` |

   Unter Windows fragt die Installation unter Umständen nach Administratorrechten; das bestätigt die Person selbst. Fehlt `brew` auf dem Mac, verweis auf [brew.sh](https://brew.sh) und warte. Nach einer Installation sind neue Befehle oft erst in einem neuen Terminal bekannt: Prüf mit dem vollen Pfad nach oder bitte die Person, Claude Code neu zu starten, und mach dann hier weiter.

   **Ist der Ordner kein Git-Repository** (`git status` scheitert, weil das Repository als ZIP heruntergeladen wurde), mach ihn nach der Installation von Git zu einem:
   `git init -b main`, `git remote add origin https://github.com/flex3-hsos/flex3.git`, `git fetch origin`, `git reset origin/main`, `git branch --set-upstream-to=origin/main main`. Danach zeigt `git status` keine Änderungen.

3. **Git-Identität.** Prüf `git config user.name` und `git config user.email`. Fehlt eines, lass die Person die beiden Befehle selbst ausführen. Empfiehl als E-Mail die GitHub-Noreply-Adresse aus den GitHub-Einstellungen unter *Emails*, damit die private Adresse nicht in öffentlichen Commits steht.

4. **GitHub-Anmeldung.** Prüf `gh auth status`. Ist die Person nicht angemeldet, lass sie selbst `! gh auth login` eingeben (GitHub.com, HTTPS, Anmeldung im Browser). Zugangsdaten gibst du nie selbst ein.

5. **Python-Umgebung.** Leg eine virtuelle Umgebung an und installier die Entwicklungswerkzeuge:
   - `python -m venv .venv`
   - Windows: `.venv/Scripts/python -m pip install -r requirements-dev.txt`
   - macOS/Linux: `.venv/bin/python -m pip install -r requirements-dev.txt`
   Prüf danach `python -m ruff --version` und `python -m pytest --version` mit dem Python aus `.venv`.

6. **Profil anlegen.** Schreib `local/profile.md` mit Vorname, Anrede, Arbeitspaket (Ordnername unter `work-packages/`), Betriebssystem und Datum des Onboardings. Der Ordner `local/` wird nicht eingecheckt.

7. **Einlesen.** Lies `knowledge-base/README.md` und das README des Arbeitspakets. Fass in fünf bis acht Sätzen zusammen, worum es im Projekt geht, was das Arbeitspaket beitragen soll und was als Nächstes ansteht.

8. **Zum Schluss** die vier Befehle aus `CLAUDE.md` kurz vorstellen und sagen, dass `/update` immer dann dran ist, wenn Nicolas ein Update ansagt.
