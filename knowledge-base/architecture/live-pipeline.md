# Live-Pipeline

Die Live-Pipeline läuft während der Vorlesung: S4 (Livestream), S5 (Echtzeit-Untertitel) und S6 (übersetzte Audiospur).

## Aufbau

Der Steuerrechner schickt genau einen Stream an den FLEX³-Server. Der Server verteilt ihn an die Studierenden und schickt den Ton parallel an eine Realtime-API, die Untertitel und optional eine übersetzte Audiospur erzeugt. Zwei Varianten sind im Vorprojekt erprobt: eine Azure-Kette aus Spracherkennung, Übersetzung und Sprachausgabe sowie die OpenAI Realtime API.

## Das Latenzproblem

Das ist der wichtigste Stolperstein des Live-Pfads, denn zwei Zielgruppen haben widersprüchliche Anforderungen:

| Zielgruppe | braucht | Latenz |
|---|---|---|
| Studierende **im Hörsaal**, die auf dem Laptop mitlesen | nur Untertiteltext, kein Video | synchron zur **gesprochenen Sprache**: 1–2 Sekunden |
| Studierende **zu Hause** | Video und Untertitel | synchron zum **Stream** |

Ein Stream über YouTube hat 10 bis 30 Sekunden Verzögerung, während Untertitel nach ein bis zwei Sekunden da sind. Für die Zuschauer zu Hause liefen die Untertitel dem Bild also weit voraus. Dieselben Untertitel werden deshalb **in zwei Zeitbasen** gebraucht: sofort für den Hörsaal und um die Streamlatenz verzögert für die Ferne.

YouTube taugt daher für den reinen Livestream (S4), aber nicht mehr für die Untertitel-Stufe; ab S5 liefern wir selbst aus.

## Auslieferung getrennt nach Zielgruppe

| Zielgruppe | Auslieferung | Latenz | Serverlast |
|---|---|---|---|
| im Hörsaal | nur Untertiteltext über WebSocket | 1–2 s | winzig |
| zu Hause | Low-Latency-HLS mit eingebetteten, passend verzögerten Untertiteln | 3–6 s | über HTTP cachebar, skaliert billig |
| optional | WebRTC für einzelne Teilnehmende mit Rückfragen | ~1 s | nur für wenige |

WebRTC für alle wäre einfacher, skaliert aber nicht: Es verteilt an jeden einzeln, und 200 Zuhörende × 6 Mbit/s wären 1,2 Gbit/s aus einer Maschine.

## Server und Entwicklung

Der Server läuft im Rechenzentrum der Hochschule, alles in Containern. Entwickelt wird lokal mit `docker compose`; für den Live-Pfad liefert OBS als [Live-Simulator](device-simulator.md) den Eingangsstream.
