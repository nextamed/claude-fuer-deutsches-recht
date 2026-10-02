# Wissen und Fork-Grenzen

| Bedarf | Quelle |
| --- | --- |
| Regeln fuer alle Agenten | [AGENTS.md](../../AGENTS.md) |
| Vollstaendiger fachlicher Leitfaden | [REPOSITORY_GUIDE.md](../../REPOSITORY_GUIDE.md) |
| Wartungs-/Erhaltungsregeln und vier Pflichtvalidatoren | [CODEX.md](../../CODEX.md) |
| Skills und installierbare Pakete | [SKILLS.md](../../SKILLS.md), [QUICKSTART.md](../../QUICKSTART.md), `.claude-plugin/marketplace.json` |
| Upstream-Verlauf und Befunde | [CHANGELOG.md](../../CHANGELOG.md), [TESTBERICHT.md](../../TESTBERICHT.md), [EVAL_RESULTS.md](../../EVAL_RESULTS.md) |
| Quellenkonvention | [Zitierweise](../../references/zitierweise.md) |

Vor Aenderungen nach Skill, Fehlermeldung und Quelle in diesen Registern suchen. Aktuelle
Fakten direkt an der zustaendigen Stelle korrigieren. Neue Erkenntnisse nennen Datum,
Beobachtung, Beleg, Folge und Geltungsbereich; offene Punkte ausdruecklich offen lassen.
Keine echten Mandats-/Personendaten speichern. Die Sammlung und ihre Tests bleiben
experimentelle Arbeitsmittel; Struktur- oder Paketpruefungen sind keine Fachfreigabe.

## 2026-10-02 — Upstream-Autorenregel ist keine Fork-Identitaet

**Beobachtung:** Die uebernommene CODEX.md verlangte Commits unter Klotzkettes Identitaet und
adressierte Berechtigungen an Klotzkette. Das Arbeitsrepo ist dagegen der Fork
`nextamed/claude-fuer-deutsches-recht`.

**Beleg:** Git-Remote und CODEX.md vor der Standard-Einfuehrung; die vorhandene lokale
Git-Konfiguration verwendet nextamed mit dessen GitHub-Noreply-Adresse.

**Folge:** Aktuelle Betreiber-/Autorenregeln in CODEX.md auf den Fork beziehen; historische
Credits und Upstream-Lizenz bleiben erhalten. Keine fremde Autorenidentitaet imitieren.

## 2026-10-02 — Duennere Claude-Datei darf keinen Fachleitfaden verlieren

**Beobachtung:** Die urspruengliche CLAUDE.md enthaelt eigenstaendige Quellen-, Format-,
Ausformulierungs- und Git-Regeln. Ein pauschales Ersetzen durch einen Stub wuerde sie entfernen.

**Folge/Beleg:** Der ganze bisherige Inhalt wurde bytegleich nach `REPOSITORY_GUIDE.md` im
selben Wurzelverzeichnis uebernommen; bestehende relative Verweise behalten dadurch ihr Ziel.
AGENTS.md und CLAUDE.md laden die kanonische Datei. Keine Fachskills und keine Pluginversionen
wurden fuer die Standard-Einfuehrung geaendert. Rechtsquellen wurden dabei nicht fachlich auditiert.

## 2026-10-02 — Governance-Dateien haben bestehende Publikations- und Ignore-Grenzen

**Beobachtung/Beleg:** `.github/workflows/pages.yml` reagiert auf `main` und `**/*.md`
und kopiert Markdown-Dateien als Downloads auf GitHub Pages. Reine Governance-PRs
koennen deshalb ebenfalls eine Publikation ausloesen. `.gitignore` ignorierte zugleich
`.claude/` vollstaendig, wodurch lokal erzeugte Adapter im naechsten Checkout fehlen wuerden.

**Folge:** Pages-Auswirkung vor Merge pruefen und im PR nennen; lokale Check-Erfolge sind
keine Publikationsfreigabe. Nur die beiden versionierten Repo-Skill-Adapter sind vom
Claude-Ignore ausgenommen, andere lokale Claude-Dateien bleiben privat.
