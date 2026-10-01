# Leitgedanken

Drei Prinzipien prägen jede technische Entscheidung im Projekt. Wenn ihr zwischen zwei Lösungen schwankt, entscheidet die, die diesen Prinzipien besser folgt.

## 1. Ein einziger Übergabepunkt

Gerät (Track H) und Software (Track S) werden getrennt entwickelt und berühren sich an genau einem Artefakt: dem **Sitzungsordner** mit `recording.mp4` und `session.json` ([session-folder.md](session-folder.md)). Beide Seiten entwickeln gegen diesen Vertrag, nicht gegeneinander. Wer die Software baut, muss nichts über Kameras wissen, und wer das Gerät baut, nichts über Opencast.

Daraus folgt: **Den Vertrag ändert niemand allein.** Braucht eure Lösung ein neues Feld in `session.json`, klärt das mit Nicolas, bevor ihr es einbaut.

## 2. Kaufen statt bauen

Jede selbst geschriebene Zeile ist teuer, muss getestet und gewartet werden und wird zur Altlast, wenn die Person geht, die sie geschrieben hat. Deshalb nutzen wir fertige Programme, Bibliotheken und Dienste, wo immer es geht, und schreiben nur die dünne Schicht dazwischen selbst.

| Funktion | fertig genutzt | Eigenanteil |
|---|---|---|
| Aufzeichnung | ATEM nimmt auf; RTMP an den Steuerrechner, dort `ffmpeg -c copy` | fast null |
| Bedienung am Gerät | Bitfocus Companion im Kiosk-Browser | null |
| Upload nach Opencast | Opencast External API | kleines Skript |
| Bereitstellung in ILIAS | bestehende ILIAS-Opencast-Anbindung | Konfiguration |
| Transkription | gemietetes Modell über API | dünne Komponente mit Adaptern |
| Zusammenfassungen | LLM-API | Prompts und Vorlagen |
| Livestream | RTMP-Weiterleitung | fast null |
| Echtzeit-Untertitel | Realtime-API | **Ausspielung an die Studierenden – die eigentliche Entwicklungsarbeit** |
| Dubbing | ElevenLabs API | Batch-Skript |

Bevor ihr etwas selbst baut, fragt euch und den Assistenten: Gibt es dafür ein Werkzeug, eine Bibliothek oder einen Befehl, der das schon kann?

## 3. Die Aufzeichnung geht nie verloren

Alles andere ist nachholbar: ein fehlgeschlagener Upload, eine misslungene Transkription, ein abgebrochener Stream. Eine nicht aufgezeichnete Vorlesung ist dagegen unwiederbringlich. Die Architektur ist um diese Asymmetrie herum gebaut, und euer Code auch:

- Eine Datei wird erst gelöscht, wenn ihr erfolgreicher Upload bestätigt ist.
- Fehler werden sichtbar gemacht und protokolliert, statt sie zu verschlucken.
- Schritte sind so gebaut, dass man sie gefahrlos wiederholen kann.
- Eine fehlende Zuordnung zu Kurs oder Lehrperson darf eine Aufnahme nie verhindern; sie wird dann als `unassigned` markiert und später zugeordnet.
