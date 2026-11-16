# Designentscheidungen

Getroffene Entscheidungen mit Begründung. Sie gelten, bis Nicolas sie ändert. Wer eine davon für falsch hält, bringt das ins Weekly, statt im Code davon abzuweichen.

## Gerät

| Entscheidung | verworfen | Warum |
|---|---|---|
| **ATEM Mini Pro ISO als Mischer** | OBS auf dem Mini-PC; geschlossene Standalone-Geräte | Dedizierte Hardware stürzt nicht ab; bei OBS kostet ein USB- oder Bootproblem die Vorlesung. Geschlossene Geräte erschweren die Opencast-Automatisierung. |
| **Mini-PC mit Intel N100** | Raspberry Pi 5 | Der Pi 5 hat keinen Hardware-H.264-Encoder mehr. |
| **Steuerrechner ist reiner Kurier** | KI-Verarbeitung auf dem Gerät | Ein Mini-PC trägt Echtzeit-KI nicht, und Gerät und Software sollen getrennt bleiben. |
| **RTMP vom Mischer zum Rechner** | USB-HDMI-Capture-Stick | kein Neucodieren, keine Rechenlast; der Stick bleibt Rückfallweg |
| **Ton analog in den Mischer** | USB-Mikrofon am Rechner | Zwei Taktgeber driften, im Mischer ist der Versatz null. |
| **Bitfocus Companion für die Bedienung** | eigene Touch-Oberfläche | fertiges Modul, null Code für Version 1 |
| **Nahbildkamera an einem festen Kabel des Geräts**, wird aufgestellt; Totale optional | fest im Gehäuse verbaut und ausklappbar; beide Kameras extern | Niemand muss eine Kamera anschließen, sie lässt sich aber frei ausrichten; ein fester Blickwinkel hätte nicht in jedem Raum ein brauchbares Bild geliefert. |
| **Display mit drei großen Tasten**: Aufnahme, Pause, Stopp | Touch-Oberfläche mit vielen Funktionen | Bedienung ohne Einweisung; was darüber hinausgeht (Zuordnung, Livestream, Speicher), wird so untergebracht, dass es den Aufnahmestart nicht stört. |
| **Zuordnung per Namenskachel**, zwei Tipps; wo sie neben den drei Tasten bedient wird, ist offen | PIN oder Login | Es ist ein Zuordnungs-, kein Authentifizierungsproblem. |
| **Freigaben aus dem Nutzerregister**, am Gerät nur einschränkbar | Freigaben je Sitzung am Display | Niemand darf per Tipp Rechte für eine andere Person erteilen. |
| **Aufnahme scheitert nie an der Zuordnung** | Zuordnung als Pflichtfeld | Eine fehlende Zuordnung ist reparierbar, eine fehlende Aufzeichnung nicht. |

## Software

| Entscheidung | verworfen | Warum |
|---|---|---|
| **FLEX3 Light als zweiter Erzeuger** neben dem Gerät | nur das Gerät | Lehrende ohne Gerät im Raum können trotzdem aufzeichnen, und die Post-Pipeline bekommt früh echtes Material. Das Gerät bleibt. |
| **Gerät zurückgestellt, Software zuerst** (13.11.2026) | Gerät parallel entwickeln | Für das Gerät gibt es derzeit niemanden. Ein Laptop mit Kamera, Funkmikrofon und FLEX3 Light zeigt alles, was das Gerät tun soll; ein Gerät ohne Software zeigte nur eine gewöhnliche Aufzeichnung. Das Gerät folgt eher in der zweiten Projekthälfte. |
| **Transkript Wort für Wort mit Konfidenz**, Nachkorrektur durch ein Sprachmodell im Batch-Pfad (13.11.2026) | nur Fließtext oder Blöcke | Aus der feinsten Form lässt sich alles ableiten; die Konfidenz zeigt unsichere Stellen und Kandidaten für die Fachbegriffsliste. |
| **Live-Übersetzung im Browser per QR-Code** (13.11.2026) | Integration in Teams oder Zoom | unabhängig von der Plattform der Veranstaltung; ein Agent für Teams-Sitzungen wäre ein Schritt nach dem Projekt. |
| **Zusätzliche Spuren im Sitzungsordner erlaubt**, `recording.mp4` bleibt Pflicht | genau zwei Dateien je Ordner | Getrennte Quellen erlauben spätere Auswertungen, etwa Folientext aus dem Bildschirmbild oder sauberen Mikrofonton für die Transkription. |
| **Transkription vor Dubbing** | Reihenfolge des Antrags | Das Transkript ist die Grundlage für Untertitel, Übersetzung und Zusammenfassungen. |
| **Gerät liefert an eigenen Ingest-Endpunkt** | Direktupload nach Opencast | Das Gerät bleibt einfach; Opencast-Änderungen betreffen nur den Server. |
| **Eigene Transkriptionskomponente mit Adaptern**, `transcript.json` als Artefakt | Whisper-Integration von Opencast; fest verdrahteter Anbieter | eigene Modell- und Qualitätskontrolle, Anbieterwechsel als Konfiguration, kein doppeltes Transkribieren |
| **Server verteilt den Stream** | Gerät streamt an die Studierenden | Das Gerät ist hinter Firewall und NAT nicht erreichbar, und sein Uplink würde mit der Zahl der Zuhörenden wachsen. |
| **Offen:** Auslieferung der Live-Untertitel, Varianten A, B und C in [live-pipeline.md](live-pipeline.md); bisheriger Entwurf war die Trennung nach Zielgruppe | WebRTC für alle | WebRTC skaliert nicht in die Breite; welche der drei Varianten gilt, wird vor dem Sommersemester 2027 entschieden. |
| **Server im Rechenzentrum**, lokale Entwicklung mit `docker compose`; bis dahin Serverseite auf einer Workstation bei Nicolas (Anfrage zurückgestellt am 06.11.2026, Server frühestens 2027) | externe Cloud-VM als Zwischenstation | keine Migration am Projektende, Aufzeichnungen bleiben im Haus |
| **Alles in Containern** | Handkonfiguration auf der VM | lokale und gehostete Umgebung sind identisch, und die Übergabe 2028 wird zur Formalie. |
| **Test- und Produktivserver** | eine Maschine für Erprobung und Betrieb | Neue Stände lassen sich erproben, ohne laufende Veranstaltungen zu gefährden. |
| **Weboberfläche für Lehrende mit Prüfschritt** | KI-Inhalte ungeprüft direkt in ILIAS | Lehrende wollen Inhalte prüfen, bevor Studierende sie sehen, und selbst bestimmen, was entsteht. |
| **Cloud-Modelle zulässig, Qualität vor EU-Hosting** | nur in der EU gehostete Modelle | Eine funktionierende Lösung ist wichtiger als eine perfekte lokale; offengelegt wird, wohin Aufzeichnungen gehen. |
