# Der Simulator

Es gibt genau ein Gerät, und es kann nicht gleichzeitig im Hörsaal stehen und auf eurem Schreibtisch liegen. Die meisten im Team werden die Hardware nie anfassen und sollen trotzdem von Anfang an produktiv sein. Dafür gibt es den Simulator: einen zweiten Erzeuger derselben Artefakte, der für die Software nicht vom echten Gerät zu unterscheiden ist.

Der Simulator lebt im Arbeitspaket `work-packages/device-simulator/`.

## Stufe 1: Datei-Simulator

Ein kleines Skript nimmt eine beliebige Videodatei und erzeugt daraus einen gültigen [Sitzungsordner](session-folder.md): Datei als `recording.mp4` ablegen, eine `session.json` mit plausiblen Metadaten daneben schreiben, `device_id` auf `simulator` setzen. Das reicht, um Upload, Transkription und Zusammenfassungen zu entwickeln.

Der eigentliche Wert liegt im Eingabematerial: Aufzeichnungen echter Vorlesungen aus dem Vorprojekt im Wintersemester 2025/26, mit echter Hörsaalakustik, Nachhall und Fachvokabular. Sie liegen **nicht** im Repository, sondern werden euch separat bereitgestellt (siehe [data-protection.md](../standards/data-protection.md)); der Pfad steht in der Umgebungsvariable `FLEX3_DATA_DIR`.

## Stufe 2: Live-Simulator mit OBS

OBS Studio ist eine kostenlose Software zum Aufnehmen und Streamen, die im Kern dasselbe tut wie der Videomischer, nur auf einem Laptop. Für die Live-Pipeline wird OBS so eingestellt, dass es sich wie das Gerät verhält:

| Parameter | muss mit dem Gerät übereinstimmen |
|---|---|
| Auflösung | 1920 × 1080 |
| Bildrate | fest, identisch zum Gerät (25 oder 50) |
| Videocodec | H.264 |
| Audiocodec | AAC, 48 kHz, Stereo |
| Ausgabeziel | RTMP an denselben MediaMTX-Endpunkt |

Profil und Szenensammlung liegen als Dateien im Arbeitspaket, damit alle dieselbe Umgebung importieren.

## Was der Simulator nicht abbildet

Damit niemand grüne Tests mit funktionierender Hardware verwechselt: Der Simulator bildet weder die Encoder-Eigenheiten des Mischers noch die SSD-Sicherung, Tonpegel, Netzabbrüche, Stromausfall, volle Speicher oder die Bedienung durch fremde Personen ab. Die Integration mit dem echten Gerät bleibt deshalb ein eigener Arbeitsschritt.

## Kein Wegwerfartefakt

Der Simulator bleibt über die gesamte Laufzeit die Testgrundlage der Pipeline: für Regressionstests nach Änderungen, für die Einarbeitung neuer Teammitglieder und für die Weiterentwicklung, während das Gerät im Hörsaal unterwegs ist. Er wird genauso sorgfältig gebaut und dokumentiert wie der übrige Code.
