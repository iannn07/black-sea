# black-sea-skills

## 3.0.0

### Major Changes

- Rebuild BLACK SEA from a single skill into a multi-skill **unit** — an orchestrator, a shared
  doctrine core, and named operatives — and add the **WAYPOINT** front door. Every case now opens by
  framing before collecting: WAYPOINT interviews the operator (depth scaled to the tier, wrapping the
  `interview-me` skill on FULL cases), converts the tasking into a sharp intelligence question, and
  decomposes it into **specified / implied / adjacent** EEI — surfacing the adjacent lines an operator
  wouldn't think to ask for — then emits a **Collection Plan** the operator approves before any
  collection runs. Adds a divergent *Requirements Expansion / Anticipatory EEI* technique to the
  analytic-tradecraft core with an "anticipating what to collect is analysis, not fabrication"
  carve-out, and an **operative contract** (the Collection Plan and the findings packet) that future
  operatives plug into. The orchestrator (`skills/black-sea/`) now dispatches to operatives; the three
  lanes remain reference files the operatives read as their method. Breaking: the unit runs WAYPOINT
  first (no more collecting straight from the raw ask), and the repository is a multi-skill plugin
  rather than a single skill.
- Populate the operative roster: **DRY DOCK** (corporate structure & beneficial-ownership tracing),
  **PLIMSOLL** (statement forensics + multi-period back-testing), **HARBORMASTER** (person profiling
  behind a legitimate-purpose gate), **HORIZON** (competitor & market intel), **GRASSHOPPER**
  (link / entity / network analysis), and **PARLEY** (lawful source elicitation, modelled on John
  Nolan's legal-CI method). Adds the `financial-backtesting.md`, `network-analysis.md`, and
  `elicitation.md` references and an `operative-contract.md`, and extends `forensics.py` with a
  time-series mode (ratio trend, rolling Beneish per period pair, receivables-vs-sales divergence).
  BLACK SEA dispatches to these operatives per the approved Collection Plan.

## 2.2.0

### Minor Changes

- Complete the repository's documentation and governance spine. Adds the root-document set the project
  had specified but not yet shipped: `CONTEXT.md` (the BLACK SEA ubiquitous language), `CONTRIBUTING.md`
  (the compliance guard as contributor law — Prime Directive, collection boundaries, leading-words
  discipline, and checkable `Done when` criteria), `SECURITY.md`, `CODE_OF_CONDUCT.md` (Contributor
  Covenant 2.1), `CITATION.cff`, `AGENTS.md`, and `.editorconfig`. Adopts changesets for versioning
  (`.changeset/` + `package.json` scripts and dev-dependencies) and starts this hand-seeded changelog.
  Adds GitHub issue and pull-request templates and a human-facing docs page at `docs/black-sea.md`.
  Expands `CLAUDE.md` with a repository-structure & conventions section, and corrects the stale
  `LICENSE` note in `README.md`.

### Patch Changes

- Fix `forensics.py` crashing with a `UnicodeEncodeError` on consoles whose default code page is not
  UTF-8 (e.g. Windows cp1252). The script now reconfigures stdout/stderr to UTF-8 at startup, so the
  report's arrows and dashes print and `--demo` runs cleanly cross-platform.

## 2.1.0

### Minor Changes

- Add per-step completion criteria (a checkable `Done when` on every workflow step, exhaustive on the
  collect and analyze steps), a leading-words glossary, a failure-modes diagnostic section, and the
  invocation/branches framing. Remove an internal duplication and adopt a clean single-skill
  repository layout.

## 2.0.0

### Major Changes

- Add the FLASH/FULL output tiers, a worked example of a well-formed finding, and the `forensics.py`
  calculator (Beneish M-Score, Altman Z and Z'', Benford's Law, core ratios — Python standard library
  only, no network). Render link networks and timelines as Mermaid, add the registry-sources
  cheat-sheet, wire Obsidian vault delivery, and package the skill for the Claude Code plugin
  marketplace.

## 1.0.0

### Major Changes

- Initial spine: the Prime Directive (never fabricate), the standardized confidence-graded dossier
  template, the three investigation lanes (org & financial forensics, competitor & market intel, and
  gated person profiling), the analytic-tradecraft core (Admiralty grading, ICD-203 confidence, ACH,
  Key Assumptions Check), and the all-source collection core.
