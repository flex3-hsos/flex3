# Arbeitspakete

Jedes Arbeitspaket hat einen eigenen Ordner. Ihr arbeitet nur im Ordner eures Arbeitspakets; welches das ist, steht im Projektboard und nach `/onboarding` in `local/profile.md`.

**Geschnitten wird entlang der Artefakte, nicht entlang der Ausbaustufen.** Jedes Paket nimmt ein Artefakt entgegen und liefert eines ab, sodass es sich allein bauen und mit dem Simulator testen lässt, ohne auf ein anderes Paket zu warten. Die tragenden Artefakte sind der Sitzungsordner (`knowledge-base/architecture/session-folder.md`), `transcript.json` mit Wort-Zeitstempeln und der Live-Stream. Welche Ausbaustufe (S1 bis S7) in welchem Paket steckt, steht in der Spalte „Stufen“.

| # | Ordner | Stufen | Eingang → Ausgang | Rang |
|---|---|---|---|---|
| 1 | [simulator/](simulator/) | – | Videodatei → Sitzungsordner; OBS-Profil für den Live-Pfad | 1 |
| 2 | [device/](device/) | S1 Geräteseite | Kamera, Ton, Laptop → Sitzungsordner und Live-Stream | 5 |
| 3 | [ingest-delivery/](ingest-delivery/) | S1 Serverseite | Sitzungsordner und Ergebnisdateien → Opencast/ILIAS; Weboberfläche für Lehrende | 1 |
| 4 | [transcription/](transcription/) | S2 | Sitzungsordner → `transcript.json`, WebVTT, Sprungmarken | 1 |
| 5 | [ai-content/](ai-content/) | S3 | `transcript.json` → Zusammenfassung, einfache Sprache, Quiz | 1 |
| 6 | [livestream/](livestream/) | S4 | Live-Stream → Video für Studierende zu Hause | 3 |
| 7 | [live-subtitles/](live-subtitles/) | S5, als Versuch S6 | Audio-Abgriff → Untertitel, optional übersetzt | 2 und 4 |
| 8 | [dubbing/](dubbing/) | S7 | `transcript.json` + Freigabe → vertonte Fassung | 5 |

**Rang** ist die Reihenfolge bei knapper Besetzung: 1 ist der Kern, der Meilenstein M1 trägt (Simulator, Transkription, Ingest und Bereitstellung, KI-Inhalte); 2 Anbieterwahl und Prototyp der Live-Untertitel; 3 Livestream direkt zu YouTube, weil er nichts kostet; 4 Untertitel im Hörsaal; 5 alles, was eine zusätzliche Person braucht. Einzelheiten in `knowledge-base/project/roadmap.md`.

## Regeln, die für alle Pakete gelten

- **Nur ein Paket spricht mit Opencast und ILIAS:** `ingest-delivery`. Transkription, KI-Inhalte und Dubbing legen ihre Ergebnisse in den Sitzungsordner, ausgeliefert wird zentral. So bleibt das fremde System an einer Stelle gekapselt.
- **Die Schnittstellen gehören Nicolas.** `session.json` und `transcript.json` legt die Projektleitung fest; die Pakete entwickeln dagegen. Braucht ihr eine Änderung, haltet an und klärt es vorher.
- **Eine zweite Person muss jeden Baustein testen können**, auf einem anderen Rechner, nur mit dem README eures Pakets (`knowledge-base/standards/conventions.md`).

Wie ein Arbeitspaket aufgebaut ist, steht in `knowledge-base/standards/conventions.md`. Das README jedes Arbeitspakets ist seine Dokumentation und wird mit jeder Lösung aktualisiert.
