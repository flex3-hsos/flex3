# Post-Pipeline

Die Post-Pipeline verarbeitet eine fertige Aufzeichnung: S1 (Upload), S2 (Transkription), S3 (KI-Inhalte) und später S7 (Dubbing).

## Ablauf

Das Gerät kennt genau ein Ziel, einen Ingest-Endpunkt auf dem FLEX³-Server, und lädt nie direkt nach Opencast. Der Server entscheidet, was wohin geht.

```
Steuerrechner ──► Ingest-Endpunkt (FLEX³-Server, Zwischenablage)
                         │
                         ├──► sofort:     Video → Opencast → ILIAS
                         │
                         └──► danach:     Ton extrahieren (ffmpeg)
                                          → Transkriptionskomponente
                                          → transcript.json (Wort-Zeitstempel)
                                                ├─► WebVTT → an das Opencast-Ereignis
                                                ├─► Sprungmarken
                                                ├─► Zusammenfassung, einfache Sprache, Quiz
                                                └─► Dubbing (nur bei consent.voice_clone)
```

**Warum nicht direkt vom Gerät nach Opencast?** Weil das Gerät sonst Opencast-Zugangsdaten, Wiederholungslogik gegen ein fremdes System und Wissen über dessen Abläufe bräuchte, und jede Änderung an Opencast die Gerätesoftware beträfe. Mit dem eigenen Endpunkt bleibt das Gerät einfach, und der Server orchestriert.

**Warum das Video sofort und den Rest später?** Die Aufzeichnung soll schnell verfügbar sein. Studierende sehen zuerst das Video und wenig später Untertitel und Zusammenfassungen.

**Absicherung:** Der Ingest-Endpunkt nimmt nur Lieferungen mit einem Geräte-Token an, einem je Gerät.

## Die Transkriptionskomponente (S2)

Das Modell wird gemietet; gebaut wird nur die dünne Hülle darum. Vier Regeln:

**1. Anbieterunabhängig.** Eine interne Schnittstelle mit austauschbaren Adaptern dahinter:

```python
def transcribe_batch(audio: Path, language: str, vocabulary: list[str]) -> Transcript: ...
def transcribe_stream(
    chunks: Iterable[bytes], language: str, vocabulary: list[str]
) -> Iterator[TranscriptDelta]: ...
```

Batch (für die Post-Pipeline) und Streaming (für Echtzeit-Untertitel) sind getrennte Fälle, für die der beste Anbieter ein anderer sein kann. Ein Anbieterwechsel soll ein Konfigurationseintrag sein, kein Umbau.

**2. Das Transkript ist das Artefakt, nicht der Untertitel.** Gespeichert wird `transcript.json` in der feinsten Form: **jedes Wort mit Zeitstempel und Konfidenz**. Fließtext lässt sich daraus jederzeit zusammensetzen, umgekehrt nicht. WebVTT, Sprungmarken, Zusammenfassungen und Übersetzungen werden daraus abgeleitet. Sonst wird für jeden neuen Zweck neu transkribiert und doppelt bezahlt. Die Konfidenz erlaubt es, bei der Nachbearbeitung nur die unsicheren Wörter anzusehen.

**3. Fachbegriffe sind der größte Qualitätshebel.** Fast alle guten Anbieter erlauben, erwartete Begriffe vorzugeben. Die Begriffe werden je Modul als kurze Liste gepflegt, nie hochschulweit und nie als Wörterbuch mit Tausenden Einträgen. Pflegen wird sie die Lehrperson in der Weboberfläche: vorab eingetragen, aus den Foliensätzen übernommen oder nach einer Aufzeichnung aus einer Liste schlecht erkannter Wörter ausgewählt. Wird derselbe Begriff wiederholt mit niedriger Konfidenz erkannt, kennt das Modell ihn vermutlich nicht.

**4. Nachkorrektur durch ein Sprachmodell.** Nach der Transkription korrigiert ein Sprachmodell offensichtliche Erkennungsfehler, ohne den Inhalt zu verändern. Das korrigierte Transkript speist Untertitel und Zusammenfassungen; das Rohtranskript bleibt erhalten. Live gibt es diesen Schritt nicht, im Batch-Pfad ist Zeit dafür.

**Auswahl des Anbieters** per Benchmark an echtem Vorlesungsmaterial, nach diesen Kriterien: Qualität bei deutschem Fachvokabular, Wort-Zeitstempel, vorgebbare Fachbegriffe, Sprechertrennung, verfügbare Streaming-Variante und Preis je Audiostunde. Hosting-Region und Auftragsverarbeitungsvertrag werden erhoben und offengelegt, entscheiden aber nicht allein: Cloud-Modelle sind zulässig, auch außerhalb der EU, wenn sie deutlich besser sind. Ein schwächeres Modell nur wegen des Standorts wird nicht gewählt. **Cloud zuerst, lokal danach:** Mit Cloud-Diensten kommt das Projekt schneller zu Ergebnissen; eine lokale Variante folgt später als weiterer Adapter hinter derselben Schnittstelle. Nicolas empfiehlt **AssemblyAI** als ersten Kandidaten (Teams, 27.10.2026); weitere Kandidaten sind unter anderem Whisper von OpenAI. API-Schlüssel gibt Nicolas auf Nachfrage über Teams heraus, sie gehören nie ins Repository.

## KI-Inhalte (S3)

Aus `transcript.json` entstehen über eine LLM-API Zusammenfassung, Fassung in einfacher Sprache, Themenübersicht und Quiz. Die Arbeit steckt in Prompts und Vorlagen, nicht in Code. Prompts werden als Dateien versioniert (Prompt-Bibliothek), nicht in Python-Strings versteckt, damit man sie ohne Programmierkenntnis verbessern kann.

Alle KI-Inhalte werden als KI-generiert gekennzeichnet.

## Weboberfläche für Lehrende

Jede Lehrperson bekommt eine schlichte Weboberfläche auf dem FLEX³-Server. Dort sieht sie die Ergebnisse ihrer Aufzeichnungen, stellt ein, was künftig entstehen soll (etwa Quiz an oder aus, Zusammenfassung zusätzlich in einer weiteren Sprache), und prüft die KI-Inhalte, bevor sie veröffentlicht werden. Die Einstellungen gelten ab der nächsten Aufzeichnung. Sie ersetzen nicht die Freigaben in `session.json`: Was veröffentlicht werden darf und ob ein Stimmklon zulässig ist, kommt weiter aus dem Nutzerregister.

Offen ist, ob die Freigabe unmittelbar nach ILIAS veröffentlicht und ob auch das Video erst nach Prüfung erscheint.

## Dubbing (S7)

Ein Batch-Skript gegen die ElevenLabs-API erzeugt eine vertonte Fassung in einer anderen Sprache. Es läuft **nur**, wenn `consent.voice_clone` gesetzt ist, und das Ergebnis wird erst nach Freigabe durch die Lehrperson veröffentlicht.
