# BLACK SEA — Special Investigation Unit / CID (Claude Code)

All-source investigative analyst for Claude Code. Org & financial-fraud forensics, competitor/market
intelligence, and due-diligence person-profiling — producing standardized, confidence-graded
intelligence dossiers, delivered into your Obsidian vault.

Repo layout follows the `mattpocock/skills` convention (`skills/<name>/` + `.claude-plugin/`), so one
tree installs four ways: `npx skills add`, `/plugin`, the bundled installer, or a manual copy.

## Requirements
- Claude Code (recent version — plugin/skills support).
- `python3` on PATH (for the `forensics.py` calculator; standard library only, no pip installs).
- **Obsidian delivery (optional):** an `mcp-obsidian` server configured in Claude Code + the Obsidian
  Local REST API running. Without it, Black Sea renders the dossier in chat and marks delivery pending.

---

## Method 1 — `npx skills add` (skills.sh)

The `npx skills` tool you had in mind is real — it's the community **skills.sh** installer (the same
one `mattpocock/skills` uses). It is not an Anthropic-official tool, but it's widely used. Push this
repo to GitHub, then:

```bash
npx skills@latest add <your-gh-username>/black-sea
```

Pick the skill and the agent(s) to install onto. Skills run scripts on your machine — inspect
`skills/black-sea/scripts/forensics.py` first (stdlib only, no network calls).

## Method 2 — Bundled installer (no hosting needed)

```bash
tar -xzf black-sea-claude-code.tar.gz
./black-sea-cc/install.sh            # → ~/.claude/skills/black-sea   (command: /black-sea)
./black-sea-cc/install.sh --project  # → ./.claude/skills/black-sea   (commit for your team)
```

## Method 3 — Manual copy / drop-in

```bash
cp -r black-sea-cc/skills/black-sea ~/.claude/skills/black-sea
# or from the zip:
unzip black-sea.skill -d ~/.claude/skills/
```

## Method 4 — Claude Code plugin marketplace

Command becomes `/black-sea:black-sea`. Push this repo to GitHub, then in Claude Code:

```text
/plugin marketplace add <your-gh-username>/black-sea
/plugin install black-sea@black-sea
/reload-plugins
```

A local checkout also works: `/plugin marketplace add /absolute/path/to/black-sea-cc`.

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
M-Score, Altman Z/Z'', Benford, ratios).

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

```
skills/black-sea/
├── SKILL.md                       # spine: invocation/branches, tiers, workflow (with Done-when
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
