# Checkliste für das Code-Review

Diese Liste arbeitet der Assistent bei `/review` ab. Jeder Befund wird eingestuft als **muss** (blockiert den Commit), **sollte** (deutlich besser, die Person entscheidet) oder **Hinweis** (zum Lernen).

## Automatisch

| Prüfung | Befehl | Einstufung bei Befund |
|---|---|---|
| Linting | `python -m ruff check <arbeitspaket>` | muss |
| Formatierung | `python -m ruff format --check <arbeitspaket>` | muss (darf automatisch behoben werden) |
| Tests | `python -m pytest <arbeitspaket>` | muss, wenn ein Test fehlschlägt |

## Umfang

- [ ] Alle vorgemerkten Dateien liegen im Ordner des eigenen Arbeitspakets. *(muss)*
- [ ] Keine Änderungen an `knowledge-base/`, `.claude/`, `CLAUDE.md`, `.github/`, `pyproject.toml`. *(muss)*
- [ ] Die Änderung hat ein erkennbares Thema; Fremdes ist ausgelagert. *(sollte)*

## Daten und Geheimnisse

- [ ] Keine API-Schlüssel, Tokens, Passwörter oder internen URLs mit Zugangsdaten, auch nicht in Tests, Kommentaren oder Beispielen. *(muss)*
- [ ] Keine Audio- oder Videodateien, keine echten Transkripte, keine Namen oder Kennungen von Studierenden. *(muss)*
- [ ] Keine `.env`-Datei; neue Umgebungsvariablen stehen in `.env.example`. *(muss)*
- [ ] Keine großen Dateien (über 1 MB) ohne Absprache. *(muss)*

## Korrektheit

- [ ] Der Code tut, was die Aufgabe verlangt; das „fertig, wenn …" aus dem README ist erfüllt. *(muss)*
- [ ] Keine Aufzeichnung kann verloren gehen: gelöscht wird erst nach bestätigtem nächsten Schritt. *(muss)*
- [ ] Freigaben aus `session.json` werden beachtet (`consent.publication`, `consent.voice_clone`). *(muss)*
- [ ] Fehler werden gezielt behandelt und protokolliert, nicht verschluckt. *(muss)*
- [ ] Externe Aufrufe haben ein Timeout. *(sollte)*
- [ ] Ein zweiter Lauf auf derselben Sitzung richtet keinen Schaden an und verursacht keine doppelten Kosten. *(sollte)*
- [ ] Randfälle bedacht: leere Datei, fehlendes Feld, kurze Aufnahme, Netz weg. *(sollte)*

## Konventionen

- [ ] Bezeichner, Kommentare, Logs und Commit-Message englisch; keine gemischtsprachigen Namen. *(muss)*
- [ ] Der Sitzungsordner-Vertrag ist unverändert, oder die Änderung ist mit Nicolas abgestimmt. *(muss)*
- [ ] Pfade mit `pathlib`, keine absoluten Pfade, Konfiguration über `FLEX3_`-Variablen. *(muss)*
- [ ] Typannotationen und Docstrings an öffentlichen Funktionen. *(sollte)*
- [ ] Neue Abhängigkeiten stehen mit fester Version in `requirements.txt` und sind begründet. *(sollte)*

## Verständlichkeit

- [ ] Namen sagen, was etwas ist oder tut. *(sollte)*
- [ ] Funktionen sind kurz und tun eine Sache. *(sollte)*
- [ ] Kein auskommentierter Code, keine vergessenen Debug-Ausgaben. *(sollte)*
- [ ] Gibt es eine fertige Bibliothek, die einen selbst geschriebenen Teil ersetzt? *(Hinweis)*

## Tests und Dokumentation

- [ ] Neue Logik hat Tests; externe Dienste sind darin ersetzt. *(sollte, bei Datenumformung und Freigaben: muss)*
- [ ] Das README des Arbeitspakets beschreibt den neuen Stand: was es kann, wie man es startet, welche Variablen es braucht. *(muss)*
- [ ] Eine zweite Person kann den Baustein auf einem anderen Rechner allein nach dem README einrichten und testen: Abhängigkeiten mit Version, alle Variablen in `.env.example`, Testdaten ohne echte Aufzeichnungen, ein Befehl für die Tests, nichts, was nur auf dem eigenen Rechner liegt (siehe `python.md`, Grundsatz 5). Im Zweifel die Schritte aus dem README gedanklich auf einem frischen Klon durchgehen. *(muss)*

## Ton des Reviews

Das Review ist zum Lernen da. Jeder Befund nennt Datei und Zeile, sagt, warum er wichtig ist, und zeigt, wie es besser geht. Gelungenes wird ebenfalls benannt.
