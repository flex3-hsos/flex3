# 1 · Simulator und Testmaterial

Erzeugt gültige Sitzungsordner ohne das echte Gerät, damit die Post- und Live-Pipeline von Anfang an entwickelt und getestet werden können. Das kleinste Paket und zugleich die Voraussetzung für alle anderen, solange es kein Gerät gibt. Hintergrund: `knowledge-base/architecture/device-simulator.md`.

Derselbe Weg nimmt auch echte Aufzeichnungen an, die mit der vorhandenen Hardware von Hand entstanden sind. Die Post-Pipeline kann damit in Betrieb gehen, bevor das Gerät fertig ist.

## Ziel

**Stufe 1 – Datei-Simulator:** Ein Skript nimmt eine beliebige Videodatei und erzeugt daraus einen Sitzungsordner nach `knowledge-base/architecture/session-folder.md` (`recording.mp4` plus `session.json` mit plausiblen Metadaten, `device_id: "simulator"`). Damit werden die Aufzeichnungen aus dem Vorprojekt zu einem Vorrat realistischer Testfälle.

**Testmaterial:** einige Beispiel-Sitzungsordner, mit denen jedes Paket sofort testen kann. Echte Aufzeichnungen liegen nie im Repository, sondern unter `FLEX3_DATA_DIR`; für Tests im Repository reichen kurze, unverfängliche Ausschnitte oder erzeugte Dateien.

**Stufe 2 – Live-Simulator:** OBS-Profil und Szenensammlung, mit denen OBS sich gegenüber dem Server wie das Gerät verhält.

## Fertig, wenn

- Stufe 1: Aus jeder Videodatei unter `FLEX3_DATA_DIR` entsteht mit einem Befehl ein gültiger Sitzungsordner, den die Post-Pipeline ohne Anpassung verarbeitet. Die erzeugte `session.json` ist durch Tests abgesichert.
- Stufe 2: Profil und Szenensammlung liegen unter `config/obs/`, und eine Anleitung beschreibt den Import in drei Schritten.

## Stand

Noch nicht begonnen. Wird zunächst nur so weit gebaut, wie die Transkription es braucht; notfalls reicht ein von Hand angelegter Beispielordner.
