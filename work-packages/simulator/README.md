# 1 · Simulator und Testmaterial

Erzeugt gültige Sitzungsordner ohne das echte Gerät, damit die Post- und Live-Pipeline von Anfang an entwickelt und getestet werden können. Das kleinste Paket und zugleich die Voraussetzung für alle anderen, solange es kein Gerät gibt. Hintergrund: `knowledge-base/architecture/device-simulator.md`.

Derselbe Weg nimmt auch echte Aufzeichnungen an, die mit der vorhandenen Hardware von Hand entstanden sind. Die Post-Pipeline kann damit in Betrieb gehen, bevor das Gerät fertig ist.

## Ziel

**Stufe 1 – Datei-Simulator:** Ein Skript nimmt eine beliebige Videodatei und erzeugt daraus einen Sitzungsordner nach `knowledge-base/architecture/session-folder.md` (`recording.mp4` plus `session.json` mit plausiblen Metadaten, `device_id: "simulator"`). Damit werden die Aufzeichnungen aus dem Vorprojekt zu einem Vorrat realistischer Testfälle.

**Testmaterial:** Zwei von Hand gebaute Beispiel-Sitzungen liegen schon unter `testdata/sessions/` (Deutsch und Englisch, je rund fünf Minuten). Der Simulator soll Ordner im selben Format erzeugen. Weitere Aufzeichnungen liegen nicht im Repository, sondern unter `FLEX3_DATA_DIR`.

~~**Stufe 2 – Live-Simulator:** OBS-Profil und Szenensammlung, mit denen OBS sich gegenüber dem Server wie das Gerät verhält.~~ Entfällt: FLEX3 Light übernimmt Aufnahme und Stream (13.11.2026).

## Fertig, wenn

- Stufe 1: Aus jeder Videodatei unter `FLEX3_DATA_DIR` entsteht mit einem Befehl ein gültiger Sitzungsordner, den die Post-Pipeline ohne Anpassung verarbeitet. Die erzeugte `session.json` ist durch Tests abgesichert.

## Stand

Eine einfache Fassung von Stufe 1 gibt es (Stand 13.11.2026): Sie legt aus einer MP4-Datei und Angaben wie Datum und Sprache einen Sitzungsordner an. Weiter ausgebaut wird sie nicht, weil Nicolas **FLEX3 Light** bereitstellt, eine Desktop-Anwendung, die frische Aufnahmen samt Metadaten als Sitzungsordner liefert.
