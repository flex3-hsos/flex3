# Coding-Standards für Python

Diese Standards gelten für allen Python-Code im Repository. Der Assistent prüft sie bei `/review`; was ruff automatisch prüfen kann, prüft ruff.

## Grundsätze

1. **Kaufen statt bauen.** Erst nach einer fertigen Bibliothek oder einem Werkzeug suchen, dann selbst schreiben. Weniger Code ist besserer Code.
2. **Lesbar vor clever.** Der Code wird von Personen weitergeführt, die ihn nicht geschrieben haben. Eine verständliche Schleife schlägt einen eleganten Einzeiler.
3. **Die Aufzeichnung geht nie verloren.** Nichts löschen, bevor der nächste Schritt bestätigt ist; Fehler nie verschlucken.
4. **Klein und einzeln testbar.** Funktionen tun eine Sache. Wer eine Funktion nicht in einem Satz beschreiben kann, teilt sie auf.
5. **Eine zweite Person auf einem anderen Rechner kann alles testen.** Jeder Baustein wird so gebaut und dokumentiert, dass jemand, der ihn nicht geschrieben hat, ihn auf einem anderen Rechner allein einrichten, starten und testen kann. Das heißt konkret:
   - Das README beschreibt Einrichten, Starten und Testen Schritt für Schritt, ab einem frisch geklonten Repository.
   - `requirements.txt` enthält jede Abhängigkeit mit fester Version; Werkzeuge außerhalb von Python (etwa ffmpeg) stehen mit Version im README.
   - `.env.example` nennt jede Umgebungsvariable, die der Baustein braucht, mit einer kurzen Erklärung und ohne echte Werte.
   - Testdaten liegen im Repository oder entstehen mit einem dokumentierten Befehl, etwa über den Simulator; echte Aufzeichnungen sind nie die einzige Möglichkeit zu testen.
   - Ein einziger Befehl führt die Tests aus.
   - Nichts hängt am eigenen Rechner: keine absoluten Pfade, keine Dateien, die nur lokal liegen, keine Einstellungen, die nirgends stehen.

## Werkzeuge

- **Python 3.12** oder neuer.
- **ruff** für Linting und Formatierung, eingestellt in `pyproject.toml` im Wurzelverzeichnis. Code ist erst fertig, wenn `python -m ruff check` und `python -m ruff format --check` ohne Befund durchlaufen.
- **pytest** für Tests.
- Eine virtuelle Umgebung `.venv` im Wurzelverzeichnis, angelegt bei `/onboarding`.

## Struktur

- Code liegt im Ordner des Arbeitspakets unter `src/<paketname>/`, Tests unter `tests/`.
- Eine Datei behandelt ein Thema. Ab etwa 300 Zeilen lohnt es sich, sie zu teilen.
- Ausführbare Skripte haben einen `if __name__ == "__main__":`-Block und eine `main()`-Funktion; Logik steckt in importierbaren Funktionen, damit sie testbar ist.
- Keine Logik auf Modulebene, die beim Import etwas tut (Dateien lesen, Netzaufrufe).

## Typen und Dokumentation

- **Typannotationen** an allen Funktionen, die außerhalb ihrer Datei benutzt werden: `def extract_audio(video: Path, target: Path) -> Path:`.
- **Docstrings** (englisch) an allen öffentlichen Funktionen und Klassen: ein Satz, was sie tut, bei Bedarf Argumente, Rückgabe und Fehler.
- **Kommentare** erklären das Warum, nicht das Was. `# Opencast rejects files above 4 GB, so we split` ist hilfreich, `# loop over files` nicht.
- Für strukturierte Daten `dataclasses` oder `pydantic`-Modelle statt verschachtelter Dictionaries. Für `session.json` und `transcript.json` gibt es je ein Modell, das alle benutzen.

## Dateien und Pfade

- Pfade immer mit `pathlib.Path`, nie als zusammengesetzte Strings.
- Keine absoluten Pfade im Code. Orte kommen aus der Konfiguration, etwa `FLEX3_DATA_DIR`.
- Dateien mit `encoding="utf-8"` öffnen.
- Schreiben in eine temporäre Datei und anschließend umbenennen, damit nie eine halb geschriebene Datei liegen bleibt.

## Konfiguration und Geheimnisse

- Konfiguration über Umgebungsvariablen mit dem Präfix `FLEX3_`. Lokal stehen sie in einer `.env`-Datei, die **nie** eingecheckt wird; eingecheckt wird eine `.env.example` mit allen Namen und ohne Werte.
- API-Schlüssel, Tokens und Passwörter stehen nie im Code, nie in Tests und nie in Logs.
- Beim Start prüfen, ob alle nötigen Variablen gesetzt sind, und sonst mit einer klaren Meldung abbrechen.

## Fehler und Logging

- `logging` statt `print()`. Je Modul `logger = logging.getLogger(__name__)`. Log-Meldungen sind englisch und nennen die Sitzung: `logger.info("Uploaded session %s to Opencast", session_id)`.
- Erwartbare Fehler (Netz weg, Datei fehlt, API antwortet mit Fehler) werden gezielt gefangen und mit Kontext protokolliert. Kein nacktes `except:` und kein `except Exception: pass`.
- Aufrufe externer Dienste haben ein Timeout und eine begrenzte Zahl von Wiederholungen mit wachsender Wartezeit.
- Schritte sind wiederholbar: Ein zweiter Lauf auf derselben Sitzung darf nichts kaputt machen und nichts doppelt bezahlen. Liegt das Ergebnis schon vor, wird der Schritt übersprungen.

## Externe Dienste

- Jeder externe Dienst (Opencast, Transkription, LLM, ElevenLabs) wird über eine eigene kleine Klasse oder ein Modul angesprochen, nie verstreut über den Code.
- Anbieter sind austauschbar: Der Rest des Codes kennt nur die interne Schnittstelle, nicht den Anbieter (siehe [post-pipeline.md](../architecture/post-pipeline.md)).
- Prompts liegen als Dateien unter `prompts/`, nicht als lange Strings im Code.

## Abhängigkeiten

- Laufzeitabhängigkeiten stehen in der `requirements.txt` des Arbeitspakets, mit fester Version (`requests==2.32.3`).
- Jede neue Abhängigkeit wird im Pull Request kurz begründet. Bevorzugt werden verbreitete, gepflegte Bibliotheken.

## Tests

- Logik, die Daten umformt oder Entscheidungen trifft, hat Tests: Parsen von `session.json`, Umrechnen von Zeitstempeln, Erzeugen von WebVTT, Auswerten der Freigaben.
- Externe Dienste werden in Tests ersetzt (Fake-Objekt oder `unittest.mock`), damit Tests ohne Netz und ohne Kosten laufen.
- Testdaten sind klein und synthetisch: eine Sekunde Stille statt einer Vorlesung, ein ausgedachtes Transkript statt eines echten.
- Ein Test prüft eine Sache und heißt danach: `test_unassigned_session_is_not_published`.

## Notebooks

Jupyter-Notebooks sind zum Ausprobieren erlaubt, gehören aber nur mit geleerten Ausgaben ins Repository und nie als einzige Fassung einer Lösung. Was funktioniert, wandert in eine Python-Datei.
