---
name: claude-fuer-deutsches-recht-develop
description: Pflegt den nextamed-Fork der deutschen Rechtsskills mit seinen vorhandenen Struktur-, Frontmatter- und Testaktenpruefungen. Fuer Repo-Wartung und gezielte Skill-Aenderungen, nicht fuer eine ungepruefte juristische Fallbearbeitung.
---

# 1. Zweck und Anwendungsfall

Lies `AGENTS.md`, `CODEX.md` und `REPOSITORY_GUIDE.md`. Der Fork hat einen eigenen Betreiber;
Upstream-Regeln zu Autorenidentitaet sind keine Erlaubnis, dessen Identitaet zu verwenden.
`ai/knowledge/README.md` nennt die erhaltenen Quellen und bekannten Stolperstellen.

# 2. Eingaben

Benoetigt werden Zielplugin/-skill, Anlass, Ausgangsrevision und das erwartete Ergebnis.
Pruefe vorhandene lokale Aenderungen sowie Unterschiede zwischen Fork und Upstream.
Repo-Governance unter `ai/` ist kein ausgelieferter Fachskill und braucht keinen Plugin-Bump.

# 3. Ablauf

1. Passenden Fachskill und referenzierte Quellen lesen; bei Wartung nur den beauftragten Scope
   aendern. Hilfsmaterial, Testakten, Indizes und Generatoren nach CODEX.md erhalten.
2. Frontmatter-Namen, Beschreibung und Ordnernamen nach den bestehenden Validatoren pruefen.
   Keine neuen Metadatenfelder erfinden; fuer neue Repo-Skills nur `name` und `description`.
3. Bei Produktversionen den bestehenden Synchronisationsweg fuer alle Manifeste verwenden.
   Ein Tag kann Release-ZIPs veroeffentlichen; keine Tags als Nebeneffekt eines Repo-Checks.
   Bereits Markdown auf `main` startet GitHub Pages samt Markdown-Downloads, auch bei
   Governance-PRs. Diese Publikationsfolge vor einem Merge am Workflow pruefen.
4. Vor Push `git fetch origin` und alle vier CODEX-Validatoren ausfuehren: Node-Marketplace,
   Python-Frontmatter, Node-Pluginstruktur, Python-Testakten-Gesamt-PDF. Fuer die letzten
   beiden Python-Pruefungen muessen PyYAML beziehungsweise pypdf vorhanden sein. Nie durch
   ein Sparse-Checkout mit fehlenden Plugins/Testakten einen grueneren Befund erzeugen.
5. Zusaetzlich `python3 ai/standard/validate_repo.py . --base origin/main --run-checks`.
   Fachliche Aenderungen brauchen passende anonymisierte Szenarien und Quellenpruefung;
   Verpackungsvalidatoren beweisen die fachliche Antwort nicht.

# 4. Quellenpflicht

Rechtliche Aussagen nach `references/zitierweise.md` und dem Repository-Leitfaden belegen.
Fremde Quellen brauchen Geltungsbereich, Stand und nachvollziehbare Fundstelle. Bestehende
Credits/Lizenzhinweise bei Uebernahmen erhalten. Fuer eine reine Codeaenderung keine
juristischen Aussagen oder Aktualitaetsbehauptungen hinzufuegen.

# 5. Ausgabe und Abschluss

PR gegen den Fork mit Aenderung, Pruefergebnissen und offenen Beweisen; Git-/Merge-Regeln und
aktuelle Nutzeranweisung beachten. Aktuelle Fakten in ihrer kanonischen Anleitung korrigieren;
neue technische Erkenntnisse in `ai/knowledge/README.md`, fachliche Befunde am betroffenen
Skill/Testfall. Juristische Endprodukte folgen Ausformulierung und Formatstandard des Leitfadens.

# 6. Beispiel

Ein neuer Repo-Betriebsskill bleibt in `ai/skills/` und in den Clientadaptern. Er wird nicht
als zusaetzliches Rechtsplugin in `.claude-plugin/marketplace.json` aufgenommen. Die bestehenden
Marketplace- und Strukturpruefungen muessen weiterhin bestehen.
