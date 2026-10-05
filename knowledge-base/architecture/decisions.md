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
| **Nahbildkamera fest im Gerät**, Totale optional | beide Kameras extern | Zwei Kameras aufzubauen ist Lehrenden nicht zumutbar. |
| **Zuordnung per Namenskachel**, zwei Tipps | PIN oder Login | Es ist ein Zuordnungs-, kein Authentifizierungsproblem. |
| **Freigaben aus dem Nutzerregister**, am Gerät nur einschränkbar | Freigaben je Sitzung am Display | Niemand darf per Tipp Rechte für eine andere Person erteilen. |
| **Aufnahme scheitert nie an der Zuordnung** | Zuordnung als Pflichtfeld | Eine fehlende Zuordnung ist reparierbar, eine fehlende Aufzeichnung nicht. |

## Software

| Entscheidung | verworfen | Warum |
|---|---|---|
| **Transkription vor Dubbing** | Reihenfolge des Antrags | Das Transkript ist die Grundlage für Untertitel, Übersetzung und Zusammenfassungen. |
| **Gerät liefert an eigenen Ingest-Endpunkt** | Direktupload nach Opencast | Das Gerät bleibt einfach; Opencast-Änderungen betreffen nur den Server. |
| **Eigene Transkriptionskomponente mit Adaptern**, `transcript.json` als Artefakt | Whisper-Integration von Opencast; fest verdrahteter Anbieter | eigene Modell- und Qualitätskontrolle, Anbieterwechsel als Konfiguration, kein doppeltes Transkribieren |
| **Server verteilt den Stream** | Gerät streamt an die Studierenden | Das Gerät ist hinter Firewall und NAT nicht erreichbar, und sein Uplink würde mit der Zahl der Zuhörenden wachsen. |
| **Offen:** Auslieferung der Live-Untertitel, Varianten A, B und C in [live-pipeline.md](live-pipeline.md); bisheriger Entwurf war die Trennung nach Zielgruppe | WebRTC für alle | WebRTC skaliert nicht in die Breite; welche der drei Varianten gilt, wird vor dem Sommersemester 2027 entschieden. |
| **Server von Anfang an im Rechenzentrum**, lokale Entwicklung mit `docker compose` | externe Cloud-VM als Zwischenstation | keine Migration am Projektende, Aufzeichnungen bleiben im Haus |
| **Alles in Containern** | Handkonfiguration auf der VM | lokale und gehostete Umgebung sind identisch, und die Übergabe 2028 wird zur Formalie. |
| **Test- und Produktivserver** | eine Maschine für Erprobung und Betrieb | Neue Stände lassen sich erproben, ohne laufende Veranstaltungen zu gefährden. |
| **Weboberfläche für Lehrende mit Prüfschritt** | KI-Inhalte ungeprüft direkt in ILIAS | Lehrende wollen Inhalte prüfen, bevor Studierende sie sehen, und selbst bestimmen, was entsteht. |
| **Cloud-Modelle zulässig, Qualität vor EU-Hosting** | nur in der EU gehostete Modelle | Eine funktionierende Lösung ist wichtiger als eine perfekte lokale; offengelegt wird, wohin Aufzeichnungen gehen. |
