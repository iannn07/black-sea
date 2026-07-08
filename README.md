# BLACK SEA — Special Investigation Unit / CID

All-source investigative analyst for Claude Code. Org & financial-fraud forensics, competitor/market
intelligence, and due-diligence person-profiling — producing standardized, confidence-graded
intelligence dossiers, delivered into your Obsidian vault.

**Callsign BLACK SEA.** Model-invoked. Prime Directive: *never fabricate* — every finding traces to a
real source or is labeled assessment/assumption; anything unobtainable is a named gap.

> **Quick install:** `npx skills@latest add iannn07/black-sea`

## Requirements

- Claude Code (recent version — plugin/skills support).
- `python3` on PATH (for the `forensics.py` calculator; standard library only, no pip installs).
- **Obsidian delivery (optional):** an `mcp-obsidian` server configured in Claude Code + the Obsidian
  Local REST API running. Without it, Black Sea renders the dossier in chat and marks delivery pending.

---

## Method 1 — `npx skills add` (skills.sh)

The `npx skills` tool is the community **skills.sh** installer. Not an Anthropic-official tool, but
widely used:

```bash
npx skills@latest add iannn07/black-sea
```

Pick the skill and the agent(s) to install onto. Skills run scripts on your machine — inspect
`skills/black-sea/scripts/forensics.py` first (stdlib only, no network calls).

## Method 2 — Clone + bundled installer

```bash
git clone https://github.com/iannn07/black-sea.git
cd black-sea
./install.sh            # → ~/.claude/skills/black-sea   (command: /black-sea)
./install.sh --project  # → ./.claude/skills/black-sea   (commit for your team)
```

## Method 3 — Manual copy

```bash
git clone https://github.com/iannn07/black-sea.git
cp -r black-sea/skills/black-sea ~/.claude/skills/black-sea   # personal (all projects)
# or, project-scoped:
cp -r black-sea/skills/black-sea .claude/skills/black-sea
```

## Method 4 — Claude Code plugin marketplace

Command becomes `/black-sea:black-sea`. In Claude Code:

```text
/plugin marketplace add iannn07/black-sea
/plugin install black-sea@black-sea
/reload-plugins
```

A local checkout also works: `/plugin marketplace add /absolute/path/to/black-sea`.

---

## Verify & use

```text
/skills          # confirm BLACK SEA is listed
/black-sea       # (manual/installer) or /black-sea:black-sea (plugin)
```

Task it:

- `Black Sea — full package on Meridian Logistics. About to sign a 3-yr contract; are they legit?`
- `Black Sea, FLASH read on our main cold-chain competitor — threat over next 18 months.`
- `Black Sea: due diligence on Daniel Okoro, incoming CFO. Is he clean?`

It works your files first and computes real forensic indicators via `scripts/forensics.py` (Beneish
M-Score, Altman Z/Z'', Benford, ratios). Try the calculator standalone:

```bash
python3 skills/black-sea/scripts/forensics.py --demo
```

## Output tiers

- **FLASH** — compressed single-screen read: BLUF, 3–6 confidence-graded findings, top gaps.
- **FULL** — the complete standardized dossier (CIA-OPLAN-modeled template), all annexes.

Both keep BLUF, confidence grades, sourcing, and an honest gaps line. FLASH is *shorter*, never *sloppier*.

## Obsidian delivery

Default delivery is your vault at `Private/Black Sea/[CODENAME]/`, compliant with your vault standard
(frontmatter, full-path wikilinks, back-links, Mermaid diagrams, `NN-` naming, append-only audit log)
and the NIGHTSTALKER / DAGGER ONE protocols. Needs an `mcp-obsidian` server reachable from Claude
Code — example `~/.claude.json` entry (fill in your own key/port):

```jsonc
{
  "mcpServers": {
    "mcp-obsidian": {
      "command": "uvx",
      "args": ["mcp-obsidian"],
      "env": { "OBSIDIAN_API_KEY": "<your-key>", "OBSIDIAN_HOST": "127.0.0.1", "OBSIDIAN_PORT": "27124" }
    }
  }
}
```

First run into a fresh vault triggers the adoption bootstrap (four DAGGER ONE baselines + a proposed
NIGHTSTALKER §10 registry row) — Black Sea asks for your go first. `.docx`/`.pdf` only on request.

## What's inside

```text
skills/black-sea/
├── SKILL.md                       # spine: invocation/branches, tiers, workflow (Done-when
│                                  #   completion criteria), dossier template, failure modes
├── references/
│   ├── glossary.md                # leading words — the vocabulary that keeps runs predictable
│   ├── analytic-tradecraft.md     # Admiralty grading, ICD-203 confidence, ACH, Key Assumptions
│   ├── collection.md              # all-source collection + doc/image forensics + breach-exposure
│   ├── org-financial.md           # ownership tracing, financial-statement forensics, fraud typologies
│   ├── competitor-market.md       # five forces, moat, indicators-&-warning, ethical CI
│   ├── person-profiling.md        # legitimate-purpose gate, lawful-source, public-capacity only
│   ├── registry-sources.md        # record-type → registry (incl. Indonesia: AHU, OJK, LPSE, PDKI)
│   └── obsidian-delivery.md       # vault-standard-compliant note writing + NIGHTSTALKER comms
└── scripts/
    └── forensics.py               # Beneish M / Altman Z,Z'' / Benford / ratios (stdlib only)
```

## Design notes

Harness conventions — per-step completion criteria, a leading-words glossary, and a failure-modes
diagnostic — are what keep runs predictable. The dossier template is modeled on a declassified CIA
OPLAN format.

## Scope & ethics

Open-source intelligence only. **In scope:** public registries, court/regulatory records, document &
image forensics, link analysis, breach-*exposure* flagging. **Out of scope:** dark-web crawling,
trafficking in stolen data, and dossiers on private individuals from breached PII. Person-profiling is
gated on legitimate purpose + lawful sources and confined to public capacity — not a surveillance tool.

## License

MIT © iannn07 — see [`LICENSE`](./LICENSE).
