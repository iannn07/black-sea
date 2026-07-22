# AGENTS.md — BLACK SEA repo

Instructions for any coding agent working in this repository (Claude Code, Codex, Cursor, and other
`SKILL.md` / `AGENTS.md`-aware harnesses). Claude Code additionally reads `CLAUDE.md`; the two are
kept in sync and `CLAUDE.md` is the fuller copy.

## What this repo is

The **BLACK SEA** unit (Special Investigation Unit / CID) — a multi-skill plugin (orchestrator +
shared doctrine core + named operatives) that produces standardized, confidence-graded intelligence
dossiers on organizations and people. The **orchestrator** lives at `skills/black-sea/`; the
**WAYPOINT** front door at `skills/waypoint/`. The orchestrator frames a case via WAYPOINT, then
dispatches to operatives (DRY DOCK, PLIMSOLL, HARBORMASTER, HORIZON, GRASSHOPPER, PARLEY).

The repo also ships **BULKHEAD** (`skills/bulkhead/`) — a **distinct** access-control system-design
skill (RBAC / authorization from agency security doctrine). It produces a design, not a dossier; keep
it separate from the investigation unit.

This repo is also a **two-plugin marketplace**. Alongside `black-sea` (source `.`), it ships
**UNIPEN** (`unipen/`, source `./unipen`) — a fully independent, separately-installable plugin that
generates GDS-standard project documentation (Onboarding, Technical Documentation, Release Notes,
Code Documentation) into an Obsidian vault. UNIPEN is not part of the investigation unit, is never
dispatched by the orchestrator, and shares zero files with BLACK SEA, BULKHEAD, or the Handover Kit
standard — installing one plugin never pulls in the other.

## Non-negotiables

- **Prime Directive — never fabricate.** Every finding traces to a real source or is labeled
  ASSESSMENT / ASSUMPTION; anything unobtainable is a named **gap**. Validate against source-of-truth;
  never generate a source, figure, quote, record, or URL from memory. This governs both the skill's
  behaviour and your edits to it.
- **Collection boundaries stay open-source and clean.** No dark-web / stolen-data ingestion, no PII
  dossiers on private individuals, nothing that needs breaking a law or a terms-of-service.
- **Speak the ubiquitous language.** Use the leading words exactly as defined in `CONTEXT.md` and
  `skills/black-sea/references/glossary.md`; define any new one in both before using it.
- **Keep `SKILL.md` under ~500 lines.** Push detail into `references/` behind context pointers. Every
  workflow step ends on a checkable **Done when** criterion (exhaustive where marked).
- **Record changes.** Add a changeset and update `CHANGELOG.md` for any skill change (see
  `CONTRIBUTING.md`).

## Where to look

- `CLAUDE.md` — full repo instructions, structure, and conventions
- `CONTRIBUTING.md` — the compliance guard and the edit / versioning workflow
- `CONTEXT.md` — the domain vocabulary (BLACK SEA's — UNIPEN keeps its own terms self-contained)
- `skills/black-sea/SKILL.md` — the orchestrator spine; `skills/waypoint/SKILL.md` — the front door;
  `skills/black-sea/references/` for lane and core detail (incl. `operative-contract.md`)
- `unipen/skills/unipen/SKILL.md` — the UNIPEN spine; `unipen/skills/unipen/references/` for the
  folder structure, document contracts, conventions, and diagram catalog it implements
