# BLACK SEA — Special Investigation Unit / CID

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BLACK SEA // PROPRIETARY // ANALYST EYES
  SPECIAL INVESTIGATION UNIT / CID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PRODUCT:  README / FIELD MANUAL       VERSION: 3.0.0
  UNIT:     BLACK SEA                    STATUS:  OPERATIONAL
  SKILLS:   9 (orchestrator + 8)         LICENSE: MIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**BLUF.** BLACK SEA is an all-source **investigation unit** for Claude Code — a multi-skill plugin that
takes a target (an organization or a person) and produces a standardized, confidence-graded
intelligence **dossier** you can act on without redoing the work. Every case opens at the **WAYPOINT**
front door, which interviews you and turns the ask into an operator-approved **Collection Plan** before
any collection runs; the orchestrator then dispatches named **operatives** and assembles the dossier,
delivered into your Obsidian vault. Its one non-negotiable law is the **Prime Directive: never
fabricate** — every finding traces to a real source or is labeled an assessment/assumption, and
anything unobtainable is written down as a named **gap**.

> **Quick install (whole unit):** in Claude Code —
> `/plugin marketplace add iannn07/black-sea` then `/plugin install black-sea@black-sea`

---

## PART I — THE UNIT (roster)

Nine skills: an orchestrator, a front door, six investigation operatives, and one distinct
system-design skill.

| Callsign | Command | Role |
| --- | --- | --- |
| **BLACK SEA** | `/black-sea` | **Orchestrator** — frames the case, dispatches operatives, assembles and delivers the dossier. The entry point. |
| **WAYPOINT** | `/waypoint` | **Front door** — interviews you, decomposes the tasking into *specified / implied / adjacent* EEI, emits the operator-approved **Collection Plan**. |
| **DRY DOCK** | `/dry-dock` | Corporate structure & **beneficial-ownership / shell** tracing. |
| **PLIMSOLL** | `/plimsoll` | **Financial-statement forensics** + multi-period **back-testing** (`forensics.py`). |
| **HARBORMASTER** | `/harbormaster` | **Person profiling & due diligence** — behind a legitimate-purpose gate. |
| **HORIZON** | `/horizon` | **Competitor & market intelligence** (ethical CI only). |
| **GRASSHOPPER** | `/grasshopper` | **Link / entity / network** analysis; renders Mermaid graphs. |
| **PARLEY** | `/parley` | **Lawful source elicitation** — modelled on John Nolan's legal-CI method. |
| **BULKHEAD** | `/bulkhead` | **Access-control / RBAC system design** from agency security doctrine. A *distinct* skill — it produces a **design, not a dossier**. |

Shared doctrine (analytic tradecraft, collection & forensics, the operative contract) lives in
`skills/black-sea/references/` and is inherited by every operative.

---

## PART II — DEPLOYMENT

### Requirements

- **Claude Code** (recent version — plugin/skills support).
- **`python3` on PATH** — for PLIMSOLL's `forensics.py` calculator (standard library only, no pip installs).
- **Obsidian delivery (optional)** — an `mcp-obsidian` server reachable from Claude Code + the Obsidian
  Local REST API running. Without it, BLACK SEA renders the dossier in chat and marks delivery pending.

> **Before you install:** skills run scripts on your machine. Inspect
> `skills/black-sea/scripts/forensics.py` first — it is standard-library only and makes no network calls.

### Method A — Claude Code plugin marketplace (whole unit, recommended)

Installs all nine skills at once. Commands become `/black-sea:<callsign>` (e.g. `/black-sea:black-sea`).

```text
/plugin marketplace add iannn07/black-sea
/plugin install black-sea@black-sea
/reload-plugins
```

A local checkout also works: `/plugin marketplace add /absolute/path/to/black-sea`.

### Method B — Clone + bundled installer (whole unit)

```bash
git clone https://github.com/iannn07/black-sea.git
cd black-sea
./install.sh            # → ~/.claude/skills/   (all 9 skills; commands: /black-sea, /waypoint, ...)
./install.sh --project  # → ./.claude/skills/   (commit for your team)
```

### Method C — `npx skills add` (skills.sh)

The community **skills.sh** installer (not an Anthropic-official tool, but widely used). Pick the
skills and the agent(s) to install onto:

```bash
npx skills@latest add iannn07/black-sea
```

### Method D — Manual copy (individual skills)

```bash
git clone https://github.com/iannn07/black-sea.git
cp -r black-sea/skills/black-sea ~/.claude/skills/black-sea   # the orchestrator (personal, all projects)
# add the front door + any operatives you want, e.g.:
cp -r black-sea/skills/waypoint  ~/.claude/skills/waypoint
cp -r black-sea/skills/plimsoll  ~/.claude/skills/plimsoll
```

> The orchestrator dispatches to the operatives — for the full experience, install the **whole unit**
> (Method A or B). BULKHEAD is standalone and can be installed on its own.

---

## PART III — OPERATION

### Verify & use

```text
/skills          # confirm the BLACK SEA skills are listed
/black-sea       # (installer/manual) or /black-sea:black-sea (plugin)
```

Task it — the unit frames the case first, then works:

- `Black Sea — full package on Meridian Logistics. About to sign a 3-yr contract; are they legit?`
- `Black Sea, FLASH read on our main cold-chain competitor — threat over the next 18 months.`
- `Black Sea: due diligence on Daniel Okoro, incoming CFO. Is he clean?`
- `Bulkhead: design an RBAC model for a 3-tier claims app with maker/checker approval.`

### Output tiers

- **FLASH** — a compressed single-screen read: BLUF, 3–6 confidence-graded findings, top gaps.
- **FULL** — the complete standardized dossier (CIA-OPLAN-modeled template), all annexes.

Both keep BLUF, confidence grades, sourcing, and an honest gaps line. FLASH is *shorter*, never *sloppier*.

### Obsidian delivery

Default delivery is your vault at `Private/Black Sea/[CODENAME]/`, compliant with the vault standard
(frontmatter, full-path wikilinks, back-links, Mermaid diagrams, `NN-` naming, append-only audit log)
and the NIGHTSTALKER / DAGGER ONE protocols. Needs an `mcp-obsidian` server reachable from Claude Code
— example `~/.claude.json` entry (fill in your own key/port):

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

First run into a fresh vault triggers the adoption bootstrap — BLACK SEA asks for your go first.
`.docx` / `.pdf` only on request.

---

## PART IV — FORENSICS (PLIMSOLL)

PLIMSOLL computes **real** indicators from your figures only (never invented): Beneish M-Score, Altman
Z / Z'', Benford's Law, core ratios, and a **multi-period back-test** (ratio trend, rolling Beneish,
receivables-vs-sales divergence). Try the calculator standalone:

```bash
python3 skills/black-sea/scripts/forensics.py --demo     # runnable example (incl. time-series mode)
python3 skills/black-sea/scripts/forensics.py --schema    # the input shape
```

These are **indicators that direct collection, never verdicts** — a high M-Score is a reason to pull
the ledgers, not a finding of fraud.

---

## ANNEX A — SCOPE, ETHICS & HANDLING CAVEATS ⚠

**Read this before you point BLACK SEA at anyone.** BLACK SEA is an **open-source** unit with legal
footing. It is investigative intelligence for legitimate purposes — not a surveillance tool.

**In scope:** public/deep registries, court & regulatory records, procurement/sanctions/PEP lists,
patents/trademarks, document & image forensics, link analysis, financial forensics, and breach
-*exposure* flagging (the *fact* of exposure, never the stolen contents).

**Out of scope — refused by design:**

- Dark-web / Tor-market crawling or trafficking in stolen or leaked data.
- A dossier on a **private individual** from breached PII, or any package meant to enable stalking,
  harassment, or harm. Person work (HARBORMASTER) is gated on **legitimate purpose + lawful sources**
  and confined to public capacity; no profiling of minors.
- Pretexting, impersonation, unauthorized access, or anything that breaks a law or a terms-of-service.
  PARLEY elicits **honestly** — no misrepresentation of identity, no inducing NDA/duty breaches.

**Not suitable for:** any FCRA-regulated decision on its own (it is investigative intelligence, not a
regulated consumer report), and its screening outputs are indicators, not accusations. The
classification banners are a **notional handling caveat for your own filing** — styling, not a real
government classification. You are responsible for lawful use in your jurisdiction.

---

## ANNEX B — GOVERNANCE

- **Code of Conduct** — [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) (Contributor Covenant 2.1).
- **Security policy** — [`SECURITY.md`](./SECURITY.md) (how to report a vulnerability).
- **Contributing** — [`CONTRIBUTING.md`](./CONTRIBUTING.md) (the compliance guard + edit/versioning workflow).
- **Ubiquitous language** — [`CONTEXT.md`](./CONTEXT.md) · human overview — [`docs/black-sea.md`](./docs/black-sea.md).
- **Changelog** — [`CHANGELOG.md`](./CHANGELOG.md) (changesets format).
- **Citation** — [`CITATION.cff`](./CITATION.cff).

## License

MIT © iannn07 — see [`LICENSE`](./LICENSE).
