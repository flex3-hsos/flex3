---
description: Erster Start im FLEX³-Repository – Werkzeuge prüfen, Python-Umgebung einrichten, Arbeitspaket festhalten
---

Führe die Person Schritt für Schritt durch den ersten Start. Erklär bei jedem Schritt in einem Satz, wozu er dient. Geh erst weiter, wenn der Schritt geklappt hat.

1. **Begrüßen und kennenlernen.** Frag nach dem Vornamen, wie die Person angesprochen werden möchte, und an welchem Arbeitspaket sie arbeitet. Zeig dazu die Liste aus `work-packages/README.md`. Weiß sie es nicht, verweis auf Nicolas.

2. **Werkzeuge prüfen.** Prüf `git --version`, `python --version` (mindestens 3.12) und `gh --version`. Fehlt etwas, nenn die Installationsquelle aus `README.md` und warte, bis die Person es installiert hat.

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
