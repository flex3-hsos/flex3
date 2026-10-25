# Systemüberblick

```
┌─ Track H: das Gerät ──────────────────────────────────┐
│                                                        │
│  Kamera Nahbild ─────┐  (am Kabel, wird aufgestellt)    │
│  Kamera Totale ──────┤  (extern, optional)              │
│  Funkmikrofon ───────┤►  ATEM Mini Pro ISO             │
│  Laptop der Lehrperson┘       │           │            │
│  (HDMI)                       │           └──► USB-SSD │
│                               │            (Sicherung) │
│                     RTMP über │ privates Geräte-LAN    │
│                               ▼                        │
│  Display 3 Tasten ◄──►  Steuerrechner (Mini-PC N100)   │
│                         MediaMTX · ffmpeg · Companion  │
│                               │                        │
└───────────────────────────────┼────────────────────────┘
                                │ ein Stream bzw. Upload
                                ▼
                     FLEX³-Server im Rechenzentrum
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
  Post-Pipeline                                  Live-Pipeline
  Transkript · Zusammenfassung · Dubbing         Verteilung · Untertitel · Audiospur
        │                                               │
        ▼                                               ▼
  Opencast → ILIAS                              Studierende (Laptop, Handy)
```

## Das Gerät (Track H)

Eine geschlossene Appliance mit Videomischer (ATEM Mini Pro ISO), einer Nahbildkamera an einem festen Kabel, optionalem Anschluss für eine zweite Kamera, Funkmikrofon und einem kleinen Steuerrechner. Die Lehrperson schließt **vier Kabel** an (Strom, Netzwerk, HDMI vom Laptop, HDMI zum Beamer), nimmt die Kamera heraus, stellt sie auf und drückt Aufnahme. Das Display zeigt dafür nur **drei große Tasten: Aufnahme, Pause, Stopp**; dahinter steckt Bitfocus Companion. Das Bild des Laptops läuft über eine Durchschleife weiter zum Beamer, auch wenn das Gerät ausfällt. Der Mischer zeichnet zur Sicherheit selbst auf eine SSD auf und schickt das Bild parallel per RTMP an den Steuerrechner.

Der Steuerrechner ist ein **reiner Kurier**: entgegennehmen, benennen, hochladen. Auf dem Gerät läuft keine KI. Er nimmt immer auf, auch ohne Netz, legt fertige Sitzungen in eine Warteschlange und lädt sie hoch, sobald eine Verbindung besteht (Store and Forward).

Zur Aufzeichnung gehört eine Zuordnung: wer zeichnet auf und welche Veranstaltung. Damit weiß die Software, in welchen Kurs die Aufzeichnung gehört und welche Freigaben gelten. Vorgesehen sind dafür zwei Tipps auf Namenskacheln; wo das neben den drei Tasten geschieht, legt Nicolas noch fest. Die Freigaben stammen aus einem zentral gepflegten Nutzerregister und können am Gerät nur eingeschränkt, nie erweitert werden.

## Der Übergabepunkt

Zwischen Gerät und Software liegt genau ein Artefakt, der Sitzungsordner. Einzelheiten in [session-folder.md](session-folder.md). Solange das Gerät nicht verfügbar ist, erzeugt der [Simulator](device-simulator.md) dieselben Ordner aus beliebigen Videodateien.

## Die Post-Pipeline (S1–S3, S7)

Läuft nach der Vorlesung. Das Video geht sofort nach Opencast und damit in den ILIAS-Kurs; Transkript, Untertitel, Sprungmarken und Zusammenfassungen werden danach erzeugt und an das bestehende Opencast-Ereignis angehängt. Bevor KI-Inhalte veröffentlicht werden, prüft und gibt die Lehrperson sie in einer Weboberfläche frei. Einzelheiten in [post-pipeline.md](post-pipeline.md).

## Die Live-Pipeline (S4–S6)

Läuft während der Vorlesung. Der Server verteilt den Stream an die Studierenden und schickt den Ton parallel an eine Realtime-API, die Untertitel und eine übersetzte Audiospur erzeugt. Einzelheiten in [live-pipeline.md](live-pipeline.md).

## Wo das alles läuft

Der FLEX³-Server läuft im Rechenzentrum der Hochschule, neben Opencast. Geplant sind ein Testserver und ein Produktivserver: Neue Stände laufen erst auf dem Testserver, dann im Betrieb. Alles läuft in Containern. Entwickelt wird lokal: Der gesamte Stack läuft per `docker compose` auf dem eigenen Laptop, und auf die Maschine im Rechenzentrum wird nur deployt.
