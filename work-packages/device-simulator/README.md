# Simulator

Erzeugt gültige Sitzungsordner ohne das echte Gerät, damit die Post- und Live-Pipeline von Anfang an entwickelt und getestet werden können. Hintergrund: `knowledge-base/architecture/device-simulator.md`.

## Ziel

**Stufe 1 – Datei-Simulator:** Ein Skript nimmt eine beliebige Videodatei und erzeugt daraus einen Sitzungsordner nach `knowledge-base/architecture/session-folder.md` (`recording.mp4` plus `session.json` mit plausiblen Metadaten, `device_id: "simulator"`). Damit werden die Aufzeichnungen aus dem Vorprojekt zu einem Vorrat realistischer Testfälle.

**Stufe 2 – Live-Simulator:** OBS-Profil und Szenensammlung, mit denen OBS sich gegenüber dem Server wie das Gerät verhält.

## Fertig, wenn

- Stufe 1: Aus jeder Videodatei unter `FLEX3_DATA_DIR` entsteht mit einem Befehl ein gültiger Sitzungsordner, den die Post-Pipeline ohne Anpassung verarbeitet. Die erzeugte `session.json` ist durch Tests abgesichert.
- Stufe 2: Profil und Szenensammlung liegen unter `config/obs/`, und eine Anleitung beschreibt den Import in drei Schritten.

## Stand

Noch nicht begonnen.
