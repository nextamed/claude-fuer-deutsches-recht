---
name: claude-fuer-deutsches-recht-operate
description: Findet und verwendet passende bestehende Rechtsskills aus diesem Fork oder prueft deren installierte Pakete und Quellenstand. Fuer Skill-Anwendung und Paketdiagnose, ohne Git-Verfuegbarkeit als fachliche Freigabe auszugeben.
---

# 1. Zweck und Anwendungsfall

Lies `AGENTS.md` und `REPOSITORY_GUIDE.md`. Fuer Installation/Paketdiagnose nutze
`INSTALLATION_EINFACH.md`, `QUICKSTART.md` und `CONNECTORS.md`; fuer die passende Fachaufgabe
`SKILLS.md` und den konkreten `<plugin>/skills/<name>/SKILL.md`. Neues technisches Wissen
findest du ueber `ai/knowledge/README.md`.

# 2. Eingaben

Bestimme, ob Paketinstallation, Funktionsdiagnose oder ein juristisches Arbeitsergebnis gefragt
ist. Bei Facharbeit zuerst Rechtsgebiet, Gegenstand, relevante Zeitpunkte/Fristen und die vom
Nutzer bereitgestellten Tatsachen/Quellen einordnen. Keine fehlenden Mandatsangaben erfinden.

# 3. Ablauf

1. Passenden vorhandenen Skill auswaehlen und nur seine erforderlichen Referenzen laden.
   Nicht die gesamte Sammlung als Anweisung in eine Sitzung kopieren.
2. Bei Paketproblemen Repository, Version und tatsaechlich installierte Datei vergleichen.
   Upstream-Release, Fork-Commit und lokale Installation getrennt halten; keine Installation
   oder Aktualisierung allein deshalb ausloesen, weil eine Diagnose angefragt ist.
3. Bei Facharbeit den Ablauf des ausgewaehlten Skills und die zentralen Quellen-/Formatregeln
   anwenden. Erforderliche aktuelle Quellen verifizieren, Unbekanntes kennzeichnen und
   Rueckfragen auf die entscheidenden fehlenden Angaben begrenzen.
4. Paket-/Strukturtests nur als solche melden. Eine erfolgreiche Installation oder ein gruenes
   Eval einer Testakte belegt weder die aktuelle Rechtslage noch den konkreten Mandatsfall.
5. Versand, Einreichung, Signatur oder Verarbeitung echter Mandatsdaten durch externe Dienste
   sind keine automatische Folge der Skill-Auswahl; konkrete Nutzeranweisung und die
   vorhandenen Datenschutz-/Toolgrenzen des Leitfadens gelten.

# 4. Quellenpflicht

`references/zitierweise.md` ist verbindlich. Keine Aktenzeichen und Literaturfundstellen aus
Modellwissen erfinden. Amtliche/offene Quellen oder bereitgestellte beziehungsweise lizenziert
verifizierte Literatur verwenden; Quellenstand und verbleibende Unsicherheit kenntlich machen.

# 5. Ausgabe und Erkenntnisse

Ein juristisches Endprodukt wird ausformuliert und nach dem Formatstandard des Leitfadens
abgegeben, kein blosses Gliederungsskelett. Fehlende Tatsachen bleiben markierte Platzhalter.
Technische Befunde mit Datum, Version, Messweg und Folgerung im Wissensindex festhalten;
keine Mandantendaten ins Repo. Fachliche Verbesserung als nachvollziehbaren Skill-/Testfall-PR
vorschlagen, nicht ungeprueft als allgemeine Regel verbreiten.

# 6. Beispiel

Bei einer fehlerhaften Skill-Auswahl zuerst den Namen, die Beschreibung und den installierten
Dateipfad pruefen. Bei einer inhaltlich fraglichen Antwort die belegten Quellen und Tatsachen
pruefen; ein erneuter ZIP-Import loest keine fehlende Rechtsquelle.
