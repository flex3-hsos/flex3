# Live-Pipeline

Die Live-Pipeline läuft während der Vorlesung: S4 (Livestream), S5 (Echtzeit-Untertitel) und S6 (übersetzte Audiospur). S6 gilt als kaum machbar und wird nur versucht.

## Aufbau

Der Steuerrechner schickt genau einen Stream an den FLEX³-Server. Der Server verteilt ihn an die Studierenden und schickt den Ton parallel an eine Realtime-API, die Untertitel und optional eine übersetzte Audiospur erzeugt. Zwei Varianten sind im Vorprojekt erprobt: eine Azure-Kette aus Spracherkennung, Übersetzung und Sprachausgabe sowie die OpenAI Realtime API.

## Das Latenzproblem

Das ist der wichtigste Stolperstein des Live-Pfads, denn zwei Zielgruppen haben widersprüchliche Anforderungen:

| Zielgruppe | braucht | Latenz |
|---|---|---|
| Studierende **im Hörsaal**, die auf dem Laptop mitlesen | nur Untertiteltext, kein Video | synchron zur **gesprochenen Sprache**: 1–2 Sekunden |
| Studierende **zu Hause** | Video und Untertitel | synchron zum **Stream** |

Ein Stream über YouTube hat 10 bis 30 Sekunden Verzögerung, während Untertitel nach ein bis zwei Sekunden da sind. Für die Zuschauer zu Hause liefen die Untertitel dem Bild also weit voraus. Sollen beide Gruppen Untertitel bekommen, die zu dem passen, was sie gerade sehen und hören, werden dieselben Untertitel **in zwei Zeitbasen** gebraucht: sofort für den Hörsaal und um die Streamlatenz verzögert für die Ferne. Ob das Projekt diesen Aufwand treibt, ist offen (siehe unten).

YouTube taugt daher für den reinen Livestream (S4), aber nicht mehr für Untertitel, die für alle passen sollen.

## Wege für den Livestream (S4)

- das Gerät als Kamera- und Bildquelle in einer Teams- oder Zoom-Sitzung, wie sie für hybride Veranstaltungen heute schon läuft,
- YouTube für öffentliche Veranstaltungen,
- ein eigener Stream über den FLEX³-Server, falls Lehrende keine der Plattformen wollen.

Welche Plattform Lehrende bevorzugen, klärt eine Befragung.

## Auslieferung der Untertitel: noch nicht entschieden

Drei Varianten stehen zur Wahl; entschieden wird vor dem Sommersemester 2027, unter anderem auf Grundlage der Messungen aus der Bachelorarbeit zu den Live-Untertiteln.

**Variante A – getrennt nach Zielgruppe** (bisheriger Entwurf, Einzelheiten unten): im Hörsaal nur Text über WebSocket, zu Hause ein Video mit passend verzögerten Untertiteln.

**Variante B – ein Videostream mit Untertiteln für alle:** Alle schauen denselben Stream auf ihrem Gerät, im Saal wie zu Hause. Das ist ein einziger Weg und viel weniger zu bauen; dafür laufen die Untertitel im Saal der gesprochenen Sprache um die Streamlatenz hinterher, 3–6 Sekunden mit eigenem Stream, 10–30 Sekunden über YouTube.

**Variante C – Untertitel im Beamerbild:** Alle im Saal sehen sie ohne eigenes Gerät. Läuft das ganze Bild über den Server, kommen auch die Folien Sekunden zu spät (C1, kaum akzeptabel). Wird nur die Textzeile im Gerät über das Bild gelegt (C2), bleiben die Folien ohne Verzögerung; dafür braucht das Gerät einen Rückkanal vom Server, und es gibt nur eine Sprache für alle.

Die Varianten lassen sich kombinieren, etwa C2 im Saal und B für zu Hause.

### Variante A im Detail

| Zielgruppe | Auslieferung | Latenz | Serverlast |
|---|---|---|---|
| im Hörsaal | nur Untertiteltext über WebSocket | 1–2 s | winzig |
| zu Hause | Low-Latency-HLS mit eingebetteten, passend verzögerten Untertiteln | 3–6 s | über HTTP cachebar, skaliert billig |
| optional | WebRTC für einzelne Teilnehmende mit Rückfragen | ~1 s | nur für wenige |

WebRTC für alle wäre einfacher, skaliert aber nicht: Es verteilt an jeden einzeln, und 200 Zuhörende × 6 Mbit/s wären 1,2 Gbit/s aus einer Maschine.

## Server und Entwicklung

Der Server läuft im Rechenzentrum der Hochschule, alles in Containern. Entwickelt wird lokal mit `docker compose`; für den Live-Pfad liefert OBS als [Live-Simulator](device-simulator.md) den Eingangsstream.
