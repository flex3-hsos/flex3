# Fahrplan

## Ausbaustufen

Gebaut wird in sieben Stufen, von denen jede auf den vorherigen aufbaut. Die Reihenfolge weicht bewusst vom Förderantrag ab.

| Stufe | Inhalt | Warum an dieser Stelle |
|---|---|---|
| **S1** | Aufzeichnung und Upload nach Opencast/ILIAS | Basis, fast kein eigener Code |
| **S2** | Transkription und Sprungmarken | Grundlage für S3, S5 und S6 |
| **S3** | KI-Zusammenfassungen, einfache Sprache, Quiz | baut auf S2 auf und bringt Lehrenden sofort sichtbaren Nutzen |
| **S4** | Livestream | früher, schneller Erfolg |
| **S5** | Echtzeit-Untertitel | das schwierigste Stück des Projekts |
| **S6** | Echtzeit-Audiospur | Erweiterung von S5 um Sprachausgabe; nur ein Versuch, im Antrag nicht zugesagt |
| **S7** | Dubbing | reine Nachbearbeitung, die nichts blockiert und Freigaben mit Vorlauf braucht |

## Arbeitspakete

Gebaut wird nicht Stufe für Stufe, sondern in acht Arbeitspaketen, die entlang der Artefakte geschnitten sind (Sitzungsordner, `transcript.json`, Live-Stream). Jedes Paket kann eine Person mit wenigen Stunden pro Woche besitzen. Die Übersicht mit Ordnern steht in `work-packages/README.md`.

| Paket | Stufen |
|---|---|
| 1 Simulator und Testmaterial | – |
| 2 Gerät | S1 Geräteseite |
| 3 Ingest und Bereitstellung | S1 Serverseite |
| 4 Transkription | S2 |
| 5 KI-Inhalte | S3 |
| 6 Livestream | S4 |
| 7 Live-Untertitel | S5, als Versuch S6 |
| 8 Dubbing | S7 |

**Rangfolge bei knapper Besetzung:**

| Rang | Pakete | Warum |
|---|---|---|
| **1 · Kern** | Simulator, Transkription, Ingest und Bereitstellung, KI-Inhalte | Die Post-Pipeline wirkt für jede Aufzeichnung, auch ohne Gerät, und trägt Meilenstein M1. |
| **2 · gesetzt** | Live-Untertitel, Teil 7a: Anbieterwahl und Prototyp | läuft über eine Bachelorarbeit und nimmt Risiko aus dem schwersten Teil |
| **3 · günstig mitnehmen** | Livestream, Schritt 1: direkt zu YouTube | kostet keine Entwicklung |
| **4 · nächster Ausbau** | Live-Untertitel, Teil 7b: Untertitel im Hörsaal | größter Nutzen des Live-Pfads bei überschaubarem Aufwand |
| **5 · nur mit zusätzlicher Person** | Gerät über die vorhandene Hardware hinaus, eigene Stream-Auslieferung, Teil 7c, Audiospur, Dubbing | brauchen mehr Leute |

## Phasen

| Phase | Zeitraum | Software (Track S) | Gerät (Track H) |
|---|---|---|---|
| P0 Durchstich | Okt–Dez 2026 | S1, S2, S3 | Gerät V1, Bedienung mit drei Tasten, Store and Forward |
| P1 Härten | Jan–Mrz 2027 | S1–S3 produktionsreif, Player in ILIAS, S4 Livestream | V1 robust, Anschlussblende, Kamerafuß und Kamerafach gedruckt |
| P2 Live-Pfad | Apr–Jul 2027 | S5 Echtzeit-Untertitel | V2 im gedruckten Gehäuse, als Bausatz nachbaubar |
| P3 Ausbau | Aug–Sep 2027 | S6 Audiospur als Versuch, Aufräumen, Monitoring | Betrieb, zweites Gerät testen |
| P4 Vollbetrieb | Okt 2027–Jan 2028 | S7 Dubbing, Feinschliff | Regelbetrieb |
| P5 Abschluss | Feb–Mrz 2028 | Übergabe von Code und Deployment | Übergabe an Rechenzentrum und eLCC |

## Meilensteine

| | Termin | Ziel |
|---|---|---|
| **M1** | Dez 2026 | Eine echte Vorlesung wird aufgezeichnet, landet automatisch in Opencast/ILIAS und hat Transkript, Sprungmarken und KI-Zusammenfassung – roh, aber durchgängig |
| **M2** | Mrz 2027 | Aufzeichnung im Regelbetrieb einer Veranstaltung nutzbar, Livestream läuft |
| **M3** | Jul 2027 | Echtzeit-Untertitel im echten Betrieb; Gerät V2 von Dritten nachbaubar |
| **M4** | Sep 2027 | Übersetzte Audiospur (Versuch); Zwischenergebnisse veröffentlicht |
| **M5** | Jan 2028 | Alle sieben Stufen im Feld erprobt |
| **M6** | Mrz 2028 | Projektabschluss, Übergabe, Verstetigungskonzept |

Geplant ist bis März 2028. Das Budget ist fest; reicht das Personal nicht, um es in dieser Zeit auszugeben, kann die Laufzeit verlängert werden. Fehlende Leute verschieben dann die Phasen, statt Stufen zu streichen.

## Sprints

Gearbeitet wird in Monatssprints mit einem Review am Monatsende. Was im laufenden Sprint ansteht, steht im Projektboard: <https://github.com/orgs/flex3-hsos/projects/1>
