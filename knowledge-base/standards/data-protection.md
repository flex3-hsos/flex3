# Datenschutz und Geheimnisse

Dieses Repository liegt auf GitHub. Was einmal eingecheckt ist, steht in der Versionsgeschichte und lässt sich praktisch nicht mehr entfernen, auch wenn die Datei später gelöscht wird. Deshalb gilt: **Was nicht hineindarf, kommt gar nicht erst hinein.**

## Nie im Repository

| Was | Warum | Stattdessen |
|---|---|---|
| Vorlesungsaufzeichnungen, Audiodateien | Personen sind zu sehen und zu hören; Einwilligung gilt nur für den Kurs | lokal unter `FLEX3_DATA_DIR` |
| echte Transkripte und Zusammenfassungen | enthalten Gesagtes von Lehrenden und Studierenden | ausgedachte, kurze Beispieltexte |
| Namen, Matrikelnummern, Kennungen von Studierenden | personenbezogene Daten | Platzhalter wie `student_01` |
| Nutzerregister mit echten Lehrenden und Freigaben | personenbezogen und vertraulich | Beispieldatei mit erfundenen Einträgen |
| API-Schlüssel, Tokens, Passwörter | Missbrauch kostet Geld und Vertrauen | `.env` lokal, `.env.example` im Repository |
| `.env`-Dateien | enthalten Geheimnisse | `.env.example` ohne Werte |

`.gitignore` fängt die häufigsten Fälle ab (Mediendateien, `.env`, `data/`, `local/`), ersetzt aber nicht das Hinsehen beim Review.

## Echtes Testmaterial

Für Benchmark und Entwicklung gibt es echte Vorlesungsaufzeichnungen aus dem Vorprojekt. Sie werden euch separat bereitgestellt, liegen auf eurem Rechner in dem Ordner, auf den `FLEX3_DATA_DIR` zeigt, und verlassen ihn nur in Richtung der vereinbarten Dienste. Nicht weitergeben, nicht hochladen, nicht in Chats kopieren.

## Externe Dienste

Für Transkription, KI-Inhalte und Dubbing werden Aufzeichnungen an externe Anbieter geschickt. Das ist nur mit den vom Projekt freigegebenen Anbietern und Zugängen erlaubt, nicht mit privaten Konten oder kostenlosen Testzugängen anderer Dienste.

## Wenn doch etwas hineingeraten ist

Sofort Nicolas Bescheid geben und nicht versuchen, es selbst aus der Versionsgeschichte zu entfernen. Ein versehentlich veröffentlichter Schlüssel wird beim Anbieter sofort ungültig gemacht und durch einen neuen ersetzt.
