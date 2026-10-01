# Glossar

| Begriff | Erklärung |
|---|---|
| **AAC** | verbreitetes Audioformat; im Projekt mit 48 kHz in der Videodatei |
| **ATEM Mini Pro ISO** | Videomischer von Blackmagic Design, das Herz des Geräts: mischt Kameras und Laptopbild, nimmt auf SSD auf und streamt per RTMP |
| **Batch** | Verarbeitung einer fertigen Datei auf einmal, im Gegensatz zu Streaming |
| **Bitfocus Companion** | Software, die Knöpfe auf einem Touch-Display mit Geräten wie dem ATEM verbindet; unsere Bedienoberfläche |
| **Diarisierung** | Sprechertrennung: erkennen, wer wann spricht |
| **docker compose** | startet mehrere Container mit einem Befehl; so läuft der Server lokal und im Rechenzentrum gleich |
| **Dubbing** | nachträgliche Vertonung einer Aufzeichnung in einer anderen Sprache |
| **eLCC** | E-Learning Competence Center der Hochschule |
| **ffmpeg** | Kommandozeilenwerkzeug zum Umwandeln, Schneiden und Zerlegen von Audio und Video |
| **H.264** | verbreitetes Videoformat |
| **HLS / LL-HLS** | Videoauslieferung über HTTP in kleinen Stücken; Low-Latency-HLS mit nur wenigen Sekunden Verzögerung |
| **ILIAS** | Lernplattform der Hochschule, in der die Kurse liegen |
| **Ingest-Endpunkt** | Adresse auf dem FLEX³-Server, an die das Gerät fertige Sitzungen liefert |
| **ISO** (beim ATEM) | Aufzeichnung jeder Kamera als eigene Datei zusätzlich zum Programm-Mix |
| **MediaMTX** | kleiner Medienserver, der RTMP-Streams annimmt und weiterreicht |
| **Nutzerregister** | zentrale Liste der Lehrenden mit ihren Veranstaltungen, Kurs-IDs und Freigaben |
| **OBS Studio** | kostenlose Software zum Aufnehmen und Streamen; unser Live-Simulator |
| **Opencast** | Videoplattform der Hochschule; speichert die Aufzeichnungen, ILIAS zeigt sie an |
| **Programm-Mix** | das fertig gemischte Bild mit Ton, wie es aufgezeichnet und gestreamt wird |
| **Realtime-API** | Schnittstelle, die Ton laufend entgegennimmt und laufend Text oder übersetzte Sprache zurückliefert |
| **RTMP** | Protokoll, mit dem Livestreams von einer Quelle an einen Server geschickt werden |
| **Sitzungsordner** | Übergabepunkt zwischen Gerät und Software: `recording.mp4` und `session.json` |
| **Sprungmarken** | Kapitelmarken in einem Video, über die man direkt zu einem Thema springt |
| **Steuerrechner** | kleiner Mini-PC im Gerät, der Aufzeichnungen entgegennimmt und hochlädt |
| **Store and Forward** | erst lokal speichern, dann weiterleiten, sobald das Netz da ist |
| **Track H / Track S** | die zwei Entwicklungsstränge: Hardware (das Gerät) und Software (die Pipelines) |
| **Totale** | Kamera, die den ganzen Raum oder die Tafel zeigt; optional |
| **TTS** | Text-to-Speech, Sprachausgabe aus Text |
| **WebRTC** | Echtzeit-Übertragung im Browser mit sehr wenig Verzögerung, skaliert aber schlecht auf viele Zuhörende |
| **WebSocket** | dauerhafte Verbindung zwischen Browser und Server; wir schicken darüber Live-Untertitel in den Hörsaal |
| **WebVTT** | Textformat für Untertitel mit Zeitangaben (`.vtt`) |
