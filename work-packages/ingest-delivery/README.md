# 3 · Ingest und Bereitstellung

Der Knoten der Post-Pipeline: Er nimmt Sitzungsordner an, steuert, welcher Schritt wann für welche Sitzung läuft, und bringt Video und Ergebnisse nach Opencast und ILIAS. **Das einzige Paket, das mit Opencast und ILIAS spricht.** Hintergrund: `knowledge-base/architecture/post-pipeline.md`.

## Ziel

- **Server-Grundgerüst** mit `docker compose`.
- **Ingest-Endpunkt**, der Sitzungsordner vom Gerät oder Simulator annimmt, nur mit gültigem Geräte-Token.
- **Ablaufsteuerung:** welcher Schritt (Transkription, KI-Inhalte, Dubbing) läuft wann für welche Sitzung. Der Upload selbst ist klein; die Ablaufsteuerung ist der eigentliche Teil.
- **Upload nach Opencast** über die External API, in die Series aus `session.json`; über die bestehende ILIAS-Opencast-Anbindung erscheint die Aufzeichnung im Kurs.
- **Ergebnisse anhängen:** Untertitel, Sprungmarken und KI-Inhalte aus dem Sitzungsordner an das Opencast-Ereignis.
- **Freigaben beachten:** ohne `consent.publication` nicht im Kurs sichtbar; `unassigned`-Sitzungen in eine Warteschlange zur Nachbearbeitung.
- **Weboberfläche für Lehrende:** Ergebnisse ansehen, Einstellungen je Lehrperson, Prüfung und Freigabe vor der Veröffentlichung. Wächst sie über eine schlichte Oberfläche hinaus, wird sie ein eigenes Paket.

Das Paket lässt sich in zwei Teile schneiden, die nacheinander laufen können: zuerst den Opencast-Upload des Videos, danach die Auslieferung der Ergebnisse. Erster Schritt: den Upload einmal von Hand in Opencast durchspielen, dann als Skript. Fachlich eng mit der technischen Beratung des Rechenzentrums abzustimmen. Die Spezifikation kommt von Nicolas.

## Fertig, wenn

- Teil 1: Ein Video aus dem Simulator landet mit einem Befehl automatisch in Opencast und ist im ILIAS-Testkurs sichtbar.
- Teil 2: Transkript, Untertitel und KI-Inhalte einer Sitzung erscheinen nach Freigabe am selben Ereignis.

## Stand

Noch nicht begonnen.
