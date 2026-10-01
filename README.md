# FLEX³ – Anytime, Anywhere, Any Language

Mobile Appliance für inklusive, hybride Lehre an der Hochschule Osnabrück: Vorlesungen aufzeichnen und automatisch bereitstellen, mit Transkript, KI-Zusammenfassung, Livestream, Echtzeit-Untertiteln und Übersetzung. Gefördert im Programm Flexcellence, Laufzeit 10/2026 bis 03/2028.

Dieses Repository ist der gemeinsame Arbeitsplatz des Projektteams. Es enthält den Code aller Arbeitspakete und einen Projektassistenten für Claude Code, der das Projektwissen kennt, beim Programmieren hilft und jede Änderung prüft, bevor sie eingecheckt wird.

## Was hier drin ist

| | |
|---|---|
| `work-packages/` | **eure Arbeit**: je Arbeitspaket ein Ordner mit Code, Tests und README |
| `knowledge-base/` | alles, was der Assistent über das Projekt wissen muss: Ziele, Architektur, Standards. Pflegt Nicolas. |
| `CLAUDE.md`, `.claude/` | Anweisungen, Befehle und Prüfregeln des Assistenten. Pflegt Nicolas. |
| `local/` | eure persönlichen Notizen und euer Profil; wird nicht eingecheckt |

## Loslegen

Einmal installieren:

1. **Git**: [git-scm.com/downloads](https://git-scm.com/downloads)
2. **Python 3.12 oder neuer**: [python.org/downloads](https://www.python.org/downloads/) – unter Windows beim Installieren *Add python.exe to PATH* anhaken
3. **GitHub CLI**: [cli.github.com](https://cli.github.com/)
4. **Claude Code**: [claude.com/claude-code](https://claude.com/claude-code), Anmeldung mit dem Projektzugang

Dann das Repository klonen und öffnen:

```bash
git clone https://github.com/flex3-hsos/flex3.git
```

Den Ordner `flex3` in Claude Code öffnen, eine Sitzung starten und `/onboarding` eingeben. Der Assistent prüft die Werkzeuge, richtet die Python-Umgebung ein, fragt nach eurem Arbeitspaket und führt euch von da an.

## Die Befehle

| Befehl | wofür |
|---|---|
| `/onboarding` | der erste Start |
| `/update` | neuesten Stand holen – immer, wenn Nicolas es ansagt, und vor jeder neuen Aufgabe |
| `/review` | eure Änderungen nach den Projektstandards prüfen lassen |
| `/ship` | fertige Lösung einchecken: Review, Commit, Push, Pull Request |

## Wie eine Änderung ins Projekt kommt

Ihr arbeitet nie direkt auf `main`, sondern auf einem eigenen Zweig je Aufgabe. `/ship` prüft eure Änderungen, checkt sie ein und öffnet einen Pull Request; Nicolas sieht ihn durch und führt ihn zusammen. Ohne bestandenes Review lässt der Assistent keinen Commit zu. Einzelheiten in `knowledge-base/standards/git-workflow.md`.

**Keine echten Daten ins Repository**: keine Vorlesungsaufzeichnungen, keine echten Transkripte, keine Namen, keine API-Schlüssel. Siehe `knowledge-base/standards/data-protection.md`.
