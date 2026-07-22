# CLAUDE.md — BLACK SEA repo

This repository ships the **BLACK SEA** unit (Special Investigation Unit / CID): a multi-skill plugin
— an orchestrator + a shared doctrine core + named operatives — that produces standardized,
confidence-graded intelligence dossiers on organizations and people.

- The **orchestrator** lives at `skills/black-sea/` (`SKILL.md` + `references/` + `scripts/`). It is
  **model-invoked** (fires on investigation intent or the callsign "Black Sea"): it runs the
  **WAYPOINT** front door to frame the case, then dispatches to operatives.
- **WAYPOINT** (`skills/waypoint/`) is the front-door operative — it interviews the operator,
  decomposes the tasking into specified/implied/adjacent **EEI**, and emits an operator-approved
  **Collection Plan** before any collection. The three lanes (org-financial / competitor-market /
  person) are graduating into named operatives; until each has its own skill, a lane is reached by a
  context pointer into `skills/black-sea/references/`.
- Default dossier delivery is the operator's Obsidian vault at `Private/Black Sea/[CODENAME]/`,
  compliant with the vault standard and the NIGHTSTALKER / DAGGER ONE protocols.
- The **Prime Directive** governs everything: never fabricate. Findings trace to real sources or are
  labeled assessment/assumption; anything unobtainable is a named *gap*.
- The repo also ships **BULKHEAD** (`skills/bulkhead/`), a **distinct** access-control system-design
  skill (RBAC / authorization from agency security doctrine). It produces a *design*, not a dossier —
  a different job from the investigation unit; keep the two concerns separate when editing.
- The repo is also a **two-plugin marketplace**: alongside `black-sea` (source `.`, everything under
  `skills/`), it ships **UNIPEN** (`unipen/`) — a fully independent, separately-installable plugin
  (source `./unipen`) that generates GDS-standard project documentation (Onboarding, Technical
  Documentation, Release Notes, Code Documentation) into an Obsidian vault. UNIPEN is not dispatched
  by the orchestrator and has zero shared files with BLACK SEA/BULKHEAD or the Handover Kit standard —
  installing one plugin never pulls in the other.

When editing a skill, follow the discipline in `skills/black-sea/references/glossary.md` (leading
words) and keep each workflow step's **Done when** criterion checkable and, where marked, exhaustive.

## Repository structure & conventions

Two-plugin marketplace: the BLACK SEA unit (`black-sea`) and UNIPEN, independently installable.
Layout:

```text
skills/black-sea/         # the ORCHESTRATOR + shared doctrine core (black-sea plugin, source ".")
  SKILL.md                # the spine — under ~500 lines
  references/             # lane files + shared cores (collection, analytic-tradecraft,
                          #   operative-contract, financial-backtesting, network-analysis,
                          #   elicitation, ...), reached by context pointers
  scripts/forensics.py    # financial-forensics calculator (stdlib only, no network)
skills/waypoint/          # WAYPOINT — the front-door (Frame & Confirm) operative
skills/dry-dock/          # DRY DOCK — ownership / shell tracing
skills/plimsoll/          # PLIMSOLL — statement forensics + back-testing
skills/harbormaster/      # HARBORMASTER — person profiling (gated)
skills/horizon/           # HORIZON — competitor & market intel
skills/grasshopper/       # GRASSHOPPER — link / network analysis
skills/parley/            # PARLEY — lawful source elicitation
skills/bulkhead/          # BULKHEAD — access-control system design (a DISTINCT job, not investigation)
  SKILL.md
  references/             # access-control-doctrine (RBAC, Bell-LaPadula, need-to-know, ...)
unipen/                   # UNIPEN plugin root (source "./unipen") — independently installable
  .claude-plugin/
    plugin.json           # name: "unipen"
  skills/unipen/
    SKILL.md               # the spine — under ~500 lines
    references/             # folder-structure, document-contracts, conventions, diagram-catalog
docs/black-sea.md         # human-facing overview page (BLACK SEA)
docs/unipen.md            # human-facing overview page (UNIPEN)
.changeset/               # changesets versioning (config + pending entries)
CLAUDE.md · AGENTS.md     # agent instructions (this file is the fuller copy)
CONTEXT.md                # the ubiquitous language (leading words, entities) — BLACK SEA's, not UNIPEN's
CONTRIBUTING.md           # the compliance guard + edit/versioning workflow
CHANGELOG.md              # changesets-format history
SECURITY.md · CODE_OF_CONDUCT.md · CITATION.cff · LICENSE · .editorconfig
.github/                  # issue + PR templates
```

Conventions:

- **One repo, two plugins, no buckets.** There is no `engineering/` / `productivity/` bucketing and
  no `.agents/` tree — agent conventions live in `CLAUDE.md` + `AGENTS.md`. New BLACK SEA operatives
  are added as `skills/<callsign>/`. A plugin's skills are discovered only at
  `<plugin-source>/skills/*/SKILL.md` — never nest a new plugin's skill folder inside another
  plugin's source tree, or installing one will silently pull in the other.
- **Ubiquitous language — BLACK SEA only.** Leading words are defined in `CONTEXT.md` and mirrored in
  `skills/black-sea/references/glossary.md`; define a new one in both before using it. This is the
  investigation unit's vocabulary — UNIPEN (like BULKHEAD) keeps its own terms self-contained in its
  own `references/`, not in `CONTEXT.md`.
- **Versioning via changesets — shared across both plugins for now.** For any change, run
  `npx changeset` to add an entry, then `npx changeset version` to fold it into `CHANGELOG.md` and
  bump `package.json`. Keep the version in `package.json`, `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json` (both plugin entries), and `unipen/.claude-plugin/plugin.json` in
  lockstep. UNIPEN does not (yet) have an independent version lineage.
- **Docs page.** A human-facing overview lives at `docs/black-sea.md` and `docs/unipen.md`; re-sync
  the relevant one when a skill's behaviour changes.
- **Protected source-of-truth (Obsidian vault) — BLACK SEA only.** The guard-rail
  `Private/Black Sea/00-BLACK-SEA.md`, the NIGHTSTALKER §10 registry, and any `99-Audit-Log.md` row
  are propose-only — never self-applied. UNIPEN writes to a project's own `{{PROJECT}}/` tree
  instead, unrelated to this vault namespace.
