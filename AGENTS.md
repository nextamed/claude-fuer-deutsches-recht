# AGENTS.md – Repository-Regeln für alle Agenten

Dieses Repository enthält Plugins für deutsche Kanzleien. Diese Datei gilt für **jedes** Werkzeug, das hier arbeitet. Der vollständige Leitfaden steht in [`REPOSITORY_GUIDE.md`](REPOSITORY_GUIDE.md); halte dich an beide.

## Gliederung und Nummerierung (verbindlich für alle Vorlagen und Verträge)

Diese Regel gilt **dauerhaft und für jedes Werkzeug**. Sie ist nicht verhandelbar.

- **Ausschließlich dezimale Gliederung:** `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1` und so weiter, beliebig tief.
- **Niemals** römische Ziffern (`I`, `II`), Großbuchstaben (`A`, `B`, `C`), Kleinbuchstaben (`a`, `b`) oder gemischte Verlags-Gliederungen (`A. I. 1. a) aa)`). Genau diese Schemata sind verboten, weil man sich darin nicht zurechtfindet.
- **Leerzeile zwischen Gliederungspunkt und seinem Inhalt sowie zwischen Gliederungsebenen.** Überschrift bzw. Nummer und der folgende Text/Unterpunkt werden durch eine Leerzeile getrennt, sonst ist es nicht lesbar.
- **Einrückung sparsam.** Nur leicht einrücken, gerade so viel, dass die Hierarchie sichtbar bleibt und es gut aussieht – nie so tief, dass das Dokument zerfleddert wirkt.

Gilt für alle Vorlagen, Verträge, Memos, Schriftsätze und sonstigen Dokumente in diesem Repository.

## Pflicht-Hinweis für Testakten

Jede bestehende und jede künftig angelegte Testakte muss in allen drei Auslieferungsformen den folgenden Hinweis auf Deutsch und Englisch tragen:

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

- Im Gesamt-PDF steht der Hinweis genau einmal auf der ersten Seite.
- Im Einzel-PDF-ZIP steht der Hinweis genau einmal auf der ersten Seite jedes PDFs.
- Im ZIP mit den Originalformaten liegt der Hinweis als UTF-8-kodierte `README.txt` unmittelbar auf der ZIP-Wurzelebene.
- Die Hinweise werden ausschließlich durch die zentralen Testakten-Builder erzeugt. Änderungen an einer Testakte dürfen die zugehörigen Hinweisprüfungen nicht umgehen oder abschwächen.

## Fork-Entwicklung und Wissenspflege

Dieses Arbeitsrepo ist `nextamed/claude-fuer-deutsches-recht`, ein Fork von
`Klotzkette/claude-fuer-deutsches-recht`. Fuer Wartung gilt zusaetzlich [CODEX.md](CODEX.md).
Aktuelle Commit-/Freigabeidentitaet ist der Fork-Betreiber, nicht der Upstream-Autor.
Historische Quellenangaben, Credits, Lizenzen und Release-Tags bleiben erhalten.

Repo-Anleitungen liegen unter `ai/skills/`; ausgelieferte juristische Fachskills weiterhin
unter `<plugin>/skills/`. Die fachlichen Dokument-/Quellenregeln des Leitfadens gelten fuer
ihre juristischen Arbeitsergebnisse. Die neuen Repo-Anleitungen werden nicht in den
Marketplace aufgenommen. Entwicklung und Anwendung beginnen beim passenden lokalen Skill;
[ai/knowledge/README.md](ai/knowledge/README.md) erschliesst aktuelle Fakten und Erkenntnisse.

Bei reiner Governance-Pflege keine Plugin-Versionen, Fachinhalte oder Release-Tags aendern.
Vor jedem Push die vier Validatoren aus CODEX.md ausfuehren. Ein gruener Strukturcheck
belegt keine juristische Richtigkeit oder Aktualitaet von Fachquellen.

## Publikationsfolge eines Merge

`.github/workflows/pages.yml` startet bei Markdown-Aenderungen auf `main` das bestehende
GitHub-Pages-Deployment; dazu gehoeren auch reine Governance-Aenderungen und deren
Markdown-Downloads. Skill-ZIP-Releases werden gesondert durch Tags ausgeloest. Vor Merge
diese Publikationsfolge und den beauftragten Umfang pruefen; ein gruener Standardcheck
ist keine zusaetzliche Merge- oder Publikationsfreigabe.

<!-- repo-standard:begin -->
## Repository standard

Use [the shared core](ai/standard/core.md) and [the skills profile](ai/standard/profile.md) for applicable work.
[Repository configuration](ai/repo-standard.json) lists the local checks, knowledge sources, skills, and deployment boundaries. Existing repository-specific rules remain in force.

Load the relevant canonical skill when developing or operating this repository:
- [claude-fuer-deutsches-recht-develop](ai/skills/claude-fuer-deutsches-recht-develop/SKILL.md)
- [claude-fuer-deutsches-recht-operate](ai/skills/claude-fuer-deutsches-recht-operate/SKILL.md)
<!-- repo-standard:end -->
