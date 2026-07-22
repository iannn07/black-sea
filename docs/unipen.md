# UNIPEN

## What it does

UNIPEN generates a complete, standardized documentation tree for a software project — four
document types (**Onboarding**, **Technical Documentation**, **Release Notes**, **Code
Documentation**), each grounded in a named industry framework, written into the operator's
Obsidian vault as a self-contained `{{PROJECT}}/` tree. It asks a small set of setup questions
up front (project name, vault destination, fresh scaffold vs. filling gaps in an existing tree),
then writes directly — no approval-gate ceremony, but existing files are never touched on an
incremental run unless the operator names one to update.

## The standard — GDS (Gunawan Documentation Standard)

| Doc type | Framework | Role |
|---|---|---|
| Onboarding | Diátaxis (tutorial mode) + Stripe/Twilio quickstart pattern | Time-to-first-success as the north star |
| Technical Documentation | C4 model (Context → Container → Component) + ADR (Nygard/MADR) | Architecture at the right zoom level; decisions captured at decision time |
| Release Notes | Keep a Changelog 1.1.0 + SemVer | Changelog = canonical ledger; release notes = audience-facing derivative |
| Code Documentation | OpenAPI 3.x as source of truth (or the nearest equivalent for RPC/Flow surfaces) | Generated reference, never hand-maintained prose that drifts from the code |

Diátaxis is the organizing logic across all four: Onboarding = tutorial (doing), Code
Documentation = reference (looking up), Technical Documentation = reference + explanation
(understanding why), Release Notes = the time-sliced diff of all three.

## Also in this plugin

- **BLACK SEA** — the investigation unit this repo's plugin also ships (`skills/black-sea/` +
  operatives). A completely separate job — investigation dossiers, not documentation. UNIPEN
  shares no files, conventions, or vocabulary with it.
- **BULKHEAD** — access-control system design (`skills/bulkhead/`). Also unrelated.

## When to reach for it

- **Invocation.** Type `/black-sea:unipen`, or the agent reaches for it automatically on
  "document this project", "write onboarding for X", "generate a changelog", "API reference
  docs", "ADR for this decision", "runbook for this incident", or any ask that's really "make
  this codebase legible to a newcomer or an agent with zero context."
- **Not for:** investigating an organization or a person — that's BLACK SEA.

## Installation

UNIPEN is bundled into the single `black-sea` plugin, alongside the investigation unit and
BULKHEAD — there's no separate install for it. Installing the `black-sea` plugin gets you all
of it; there's no way to pick up just UNIPEN on its own.

## Prerequisites

- **Obsidian delivery (optional)** — an `mcp-obsidian` server reachable from Claude Code. Without
  it, UNIPEN writes the tree as plain files at the given vault path instead.

## It's working if

- Every file carries the required frontmatter (`tier`, `trust`, `owner`, `last_verified`) and a
  full-path breadcrumb as the first line of its body.
- No wikilink is short-form, crosses out of `{{PROJECT}}/`, or points at a file that doesn't
  exist — `RESERVED` stubs exist before anything links to them.
- Every module has its own folder under Technical → Modules; every runbook and (by default)
  every ADR is a single file.
- Only the Code Documentation branches (REST/RPC/Flow) that actually apply to the project exist
  — no empty conditional folders.
- Diagrams are Mermaid, hand-verified against source, and the UML use-case caveat appears
  wherever a use-case diagram is approximated as a flowchart.
- An incremental run never touched a pre-existing file the operator didn't name.

## Where it fits

UNIPEN is a reach-for-it-anytime documentation generator: intake → recon → scaffold → fill →
human-only content → deliver → self-check. The depth lives in `skills/unipen/references/` —
folder structure, document contracts, conventions, and the diagram catalog, each loaded as the
workflow needs it.
