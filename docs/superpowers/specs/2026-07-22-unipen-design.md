# Spec — UNIPEN: GDS Documentation-Generation Skill (independently installable)

> **Superseded, 2026-07-22 (same day).** The independent-installability architecture below (the
> sibling `unipen/` plugin folder, the second `marketplace.json` entry) was built, then
> deliberately reversed: UNIPEN was folded into the single `black-sea` plugin at
> `skills/unipen/`, bundled alongside BULKHEAD, with no separate plugin/marketplace entry. The
> workflow, conventions, folder-structure, and document-contracts content below are all still
> accurate and unchanged — only the *installability* section (Design §1) no longer reflects
> reality. Kept here as the historical record of why the sibling-plugin pattern exists and how it
> works, for the next skill that might actually need it.

- **Date:** 2026-07-22
- **Status:** Approved design, pending interview-me pass + skill-creator build
- **Version target:** repo stays on a single shared version (currently 3.0.0); this ships as
  a `minor` changeset ("add UNIPEN plugin") once built
- **Source brief:** `07-GDS-Skill-Build-Brief.md` (pasted in full by the operator; reproduced
  and adapted below so this spec is self-contained)

---

## Program context

BLACK SEA is a git repo that is also a plugin **marketplace**. It currently ships one
installable plugin (`black-sea`, source `.`) bundling the investigation unit (orchestrator +
WAYPOINT + operatives) and the unrelated BULKHEAD access-control-design skill under a shared
`skills/` folder.

UNIPEN is a **second, independently-installable plugin** in the same marketplace/repo. It is
not an investigation operative and not dispatched by the BLACK SEA orchestrator — it is a
standalone documentation generator, a sibling job the same way BULKHEAD is, except BULKHEAD
today still ships bundled inside the `black-sea` plugin and UNIPEN must not be. A user running
this marketplace can install `black-sea`, `unipen`, or both, independently.

## Mission

Build **UNIPEN** — an installable Claude Skill that generates four documentation types for any
software project — Onboarding, Technical Documentation, Release Notes, Code Documentation —
each grounded in a named industry framework, each requiring hand-authored Mermaid diagrams, all
structured for an Obsidian vault and readable by both humans and agents with zero prior context.
UNIPEN's own name is the skill/callsign; **GDS — Gunawan Documentation Standard** is the named
methodology it implements (mirrors how BULKHEAD is the skill and "access-control doctrine" — NIST
RBAC, Bell-LaPadula, etc. — is the body of knowledge it applies).

**Out of scope for this build:** no pilot project. Nobody runs UNIPEN against a real project in
this session. The deliverable is the skill itself, ready to run later.

**Do not touch:** the operator's existing `Handover Kit` skill/standard. UNIPEN is a sibling, not
a replacement. No shared files, no shared folders, no modifications to it, no reference to it
anywhere in UNIPEN's own files (see *Conventions* decision below — the brief's source material
called these conventions "inherited from Handover Kit"; UNIPEN owns a self-contained copy
instead).

## Goals

- A working `unipen/` plugin, installable independently of `black-sea`, in the same repo/marketplace.
- `SKILL.md` (+ `references/`) that fully implements the GDS standard's four doc types, folder
  structure, document contracts, conventions, and diagram catalog from the source brief.
- Repo housekeeping (`CLAUDE.md`, `CONTRIBUTING.md`, `docs/unipen.md`, a changeset) so the new
  plugin is documented the same way `black-sea`/BULKHEAD are.

## Non-goals

- Running UNIPEN against a real project (SCM, CTMS, RIM, RIS, Automations, chatbot, or any
  other) — no pilot in this build.
- Making BULKHEAD independently installable too (establishes the pattern; not applied
  retroactively to BULKHEAD unless asked separately).
- Any dependency on or reference to the Handover Kit skill/standard.
- An operator approval gate before scaffolding/writing (see *Decisions* below — explicitly
  declined for this build).

---

## Decisions made in brainstorming (resolve the source brief's open assumptions)

The source brief flagged three open assumptions in its own closing section. Resolved here,
plus two additional decisions this repo's structure required:

1. **Naming.** UNIPEN is the skill/callsign; GDS remains the named standard it implements.
   Brief content referring to "GDS" throughout is kept as-is (it's the standard's name, not the
   skill's).
2. **Inherited conventions.** The brief describes the trust ladder (`VERIFIED`/`PARTIAL`/
   `DRAFT`/`RESERVED`), tiering (T1/T2/T3), and citation rule as "inherited from the Handover
   Kit." Since UNIPEN cannot actually depend on that separate, untouched skill, `references/
   conventions.md` defines all of this as **UNIPEN's own, self-contained doctrine** — same
   content, zero mention of Handover Kit or any external skill.
3. **Governance model.** The brief's proposed `RECON → PLAN → GO/NO-GO → EXECUTE (batched,
   verified) → ACCEPTANCE TEST` ceremony, carried over by pattern-matching from Handover Kit, is
   **declined**. UNIPEN recons the project (to decide which optional branches apply) and then
   writes directly — no pre-write operator approval gate, no batching ceremony, no formal
   acceptance test. It still never fabricates human-only content (see workflow step 4 below) —
   that survives independent of the governance ceremony.
4. **Vault destination.** The brief's folder tree starts at `{{PROJECT}}/` as if
   project-root-relative. Confirmed: UNIPEN writes directly to `{{PROJECT}}/` in the vault (or
   wherever the operator points it) — **not** nested under `Private/Black Sea/` or any other
   BLACK SEA vault namespace. UNIPEN's output has no relationship to BLACK SEA's dossier
   delivery tree.
5. **Repo architecture for independent installability** (new decision, not in the source
   brief — the brief assumed a single-plugin context). See below.
6. **Versioning.** Shared repo version across both plugins for now (see *Repo housekeeping*).

### Additional decisions from the interview-me pass

7. **Intake.** UNIPEN asks a small, fixed set of setup questions before scaffolding — project
   name / vault destination path, and whether this run is a fresh scaffold or filling gaps in
   an existing GDS tree. This is not the declined approval-gate ceremony (Decision 3); it's the
   minimum facts UNIPEN can't infer, the same way BULKHEAD asks "one or two sharp scoping
   questions" despite having no approval gate either.
8. **Incremental runs preserve by default.** When a project already has some GDS files, UNIPEN
   only adds what's missing (new files, RESERVED stubs) — existing files, especially anything
   already `VERIFIED`, are untouchable unless the operator names a specific file to update.
9. **Delivery mechanism.** UNIPEN prefers Obsidian MCP tools (`mcp__mcp-obsidian__*`) when
   available in the session, falling back to plain file writes to the given vault path
   otherwise — the same dual-path pattern `obsidian-delivery.md` uses for BLACK SEA dossiers.

---

## Design

### 1. Repo architecture — the `unipen/` plugin

Claude Code discovers a plugin's skills only at `<plugin-source>/skills/*/SKILL.md` — it does
not recurse into a sibling plugin's folder. Confirmed against the official Plugins reference
and Plugin marketplaces docs (code.claude.com/docs/en/plugins-reference,
code.claude.com/docs/en/plugin-marketplaces): a `source` path can be a subdirectory of the same
repo, and each plugin's skill discovery is scoped to its own `source`'s `skills/` folder only.

```text
Black Sea/                          (repo root = the marketplace)
├── .claude-plugin/
│   ├── plugin.json                 name: "black-sea"          (unchanged)
│   └── marketplace.json            "plugins": [
│                                      { "name": "black-sea", "source": "." , ... },
│                                      { "name": "unipen", "source": "./unipen", ... }
│                                    ]
├── skills/                         black-sea plugin's skills — UNCHANGED
│   ├── black-sea/ ...
│   ├── waypoint/ ...
│   ├── bulkhead/ ...
│   └── ...
└── unipen/                         NEW — its own plugin root, sibling to skills/
    ├── .claude-plugin/
    │   └── plugin.json             name: "unipen"
    └── skills/
        └── unipen/
            ├── SKILL.md
            └── references/
                ├── folder-structure.md
                ├── document-contracts.md
                ├── conventions.md
                └── diagram-catalog.md
```

Installing `black-sea` never pulls in `unipen/`; installing `unipen` never pulls in `skills/`.
Zero leakage either direction.

`unipen/.claude-plugin/plugin.json` shape (mirrors the root one):

```json
{
  "name": "unipen",
  "description": "<pushy trigger description — see SKILL.md frontmatter below>",
  "version": "3.0.0",
  "author": { "name": "Gunawan" },
  "keywords": ["documentation", "onboarding", "changelog", "api-reference", "diataxis", "c4-model", "adr", "gds"]
}
```

`marketplace.json` gains a second entry in its `"plugins"` array (`name: "unipen"`,
`source: "./unipen"`), same shape as the existing `black-sea` entry.

### 2. What GDS is — the standards it's built on

| Doc type | Framework adopted | Role |
|---|---|---|
| Onboarding | Diátaxis (tutorial mode) + Stripe/Twilio quickstart pattern | Time-to-first-success as the north star metric |
| Technical Documentation | C4 model (Context → Container → Component) + ADR (Nygard/MADR) | Architecture at the right zoom level per audience; decisions captured at decision time |
| Release Notes | Keep a Changelog 1.1.0 + Semantic Versioning | Changelog = canonical ledger; release notes = audience-facing derivative |
| Code Documentation | OpenAPI 3.x as source of truth (or the nearest equivalent for non-REST surfaces) | Generated reference, never hand-maintained prose that can drift from the code |

Diátaxis is the organizing logic across all four: Onboarding = tutorial (doing), Code
Documentation = reference (looking up), Technical Documentation = reference + explanation
(understanding why), Release Notes = the time-sliced diff of all three.

### 3. Cross-cutting conventions — `references/conventions.md` (self-contained, per Decision 2)

Apply to every document UNIPEN produces.

**Trust ladder**

| State | Meaning |
|---|---|
| `VERIFIED` | Confirmed against source, citations present |
| `PARTIAL` | Some claims cited; gaps named in a `## Gaps` section |
| `DRAFT` | Authored from inference, not source-confirmed |
| `RESERVED` | Empty placeholder for a later pass — must exist as a real (if empty) file, never a dangling link target |

**Tiering**

- **Tier 1** — reader is harmed if wrong/missing → must reach `VERIFIED`
- **Tier 2** — reader is slowed if wrong/missing → `VERIFIED` or `PARTIAL`
- **Tier 3** — nice to have → any state

**Citation rule**

Every behavioral claim cites `path/to/file:line` or a config path. Uncited claims go in
`## Gaps` or are omitted. Never invent a citation, filename, version, or owner.

**Frontmatter — every file, no exceptions**

```yaml
---
tier: 1
trust: VERIFIED
owner: <name>
last_verified: YYYY-MM-DD
---
```

**Breadcrumb — every file, first line of body (below frontmatter, above the H1)**

Full-path Obsidian wikilinks, one per ancestor, plain text for the current file (the current
file never links to itself):

```markdown
[[Kalbe-SCM/00-MAP|SCM Digital Twin]] / [[Kalbe-SCM/02-Technical/00-Index|Technical]] / [[Kalbe-SCM/02-Technical/TD-01-Architecture/00-Overview|Architecture]] / System Architecture
```

**Index files — one extra requirement**

Every `00-Index.md` (one per folder level) additionally carries a summary table so an agent
reads one file and knows the state of the whole folder:

```markdown
| File | Tier | Trust | Owner |
|---|---|---|---|
| 01-System-Architecture | T1 | VERIFIED | Gunawan |
| 02-Connections | T1 | PARTIAL | Gunawan |
```

**Wikilink rules — hard constraints**

- **Full path only**, never short-form (`[[Kalbe-SCM/02-Technical/00-Index]]`, not
  `[[00-Index]]`) — every project repeats filenames like `00-Overview` and `00-Index`,
  short-form links are ambiguous across the vault.
- **No node ever points outside its own project folder.** GDS trees are fully self-contained —
  zero cross-project links, zero shared layer.
- **No node ever points to a nonexistent file.** RESERVED sections must be created as real stub
  files (frontmatter + breadcrumb + `trust: RESERVED`, body empty or a one-line placeholder)
  before anything links to them.

**"Elevate and link, never duplicate"**

If content already has a canonical home elsewhere in the same project tree, link to it — never
fork a second copy. (This is why there is no Migration-Guides folder — see folder structure
below — and why Versioning-Policy links to the Deprecation-Timeline instead of restating it.)

**Diagram governance**

All diagrams are hand-authored and verified against source — never auto-generated from a live
pipeline, even where the source is technically machine-readable (e.g. a Supabase schema). A
diagram starts as a first draft, gets checked against source, then is promoted to `VERIFIED`.

### 4. Diagram catalog — `references/diagram-catalog.md`

| Diagram | Mermaid syntax | Used in |
|---|---|---|
| System context / use case | `flowchart` styled with actor nodes + boundary subgraphs | Onboarding orientation, module interfaces |
| Class diagram | `classDiagram` | Modules — **optional, ask before including per module** |
| Sequence | `sequenceDiagram` | Data flow, module communication, per-endpoint request lifecycle |
| Activity / data flow | `flowchart` or `stateDiagram-v2` | Data flow, business process topology |
| Architecture (C4-style) | `flowchart` with styled subgraphs for Context/Container/Component | Technical → Architecture |
| ERD | `erDiagram` | Technical → Data → Data Model |
| Release timeline | `timeline` or `gitGraph` | Release Notes |

**Known limitation to document inside the skill:** Mermaid has no native UML "use case diagram"
syntax. Any "Use Case" diagram in UNIPEN output is a `flowchart` approximation (actor shapes +
system-boundary subgraph) — note this explicitly wherever it appears so nobody expects a
textbook UML use-case diagram.

### 5. Folder structure — `references/folder-structure.md` (reproduce exactly)

```text
{{PROJECT}}/
├── 00-MAP.md
├── 00-README.md
├── 00-GLOSSARY.md
├── 99-Audit-Log.md
│
├── 01-Onboarding/
│   ├── 00-Index.md
│   ├── OB-01-Orientation/
│   │   ├── 00-Overview.md
│   │   ├── 01-System-Context.md
│   │   └── 02-Actors-and-Roles.md
│   ├── OB-02-Environment-Setup/
│   │   ├── 00-Prerequisites.md
│   │   ├── 01-Access-and-Credentials.md
│   │   ├── 02-Local-Environment.md
│   │   └── 03-Verify-Your-Setup.md
│   ├── OB-03-First-Contribution/
│   │   ├── 00-Overview.md
│   │   ├── 01-Guided-Walkthrough.md
│   │   └── 02-Where-To-Go-Next.md
│   ├── OB-04-Role-Based-Paths/
│   │   ├── 00-Index.md
│   │   ├── 01-Intern-Path.md
│   │   ├── 02-Junior-Dev-Path.md
│   │   ├── 03-Successor-Path.md
│   │   └── 04-Mentor-Reviewer-Path.md
│   └── OB-05-Ownership-and-Escalation.md
│
├── 02-Technical/
│   ├── 00-Index.md
│   ├── TD-01-Architecture/
│   │   ├── 00-Overview.md
│   │   ├── 01-System-Architecture.md
│   │   ├── 02-Connections.md
│   │   ├── 03-Business-Process-Topology.md
│   │   └── 04-Deployment.md
│   ├── TD-02-Data/
│   │   ├── 00-Overview.md
│   │   ├── 01-Data-Flow.md
│   │   ├── 02-Data-Model.md
│   │   ├── 03-Data-Lifecycle-and-Retention.md
│   │   └── 04-Data-Contracts.md
│   ├── TD-03-Modules/
│   │   ├── 00-Module-Index.md
│   │   └── NN-<Module-Name>/              (EVERY module gets a folder — no exceptions)
│   │       ├── 00-Overview.md
│   │       ├── 01-Architecture.md
│   │       ├── 02-Data-Flow.md
│   │       ├── 03-Interfaces.md            (cross-links into 04-Code-Documentation)
│   │       ├── 04-Gotchas.md               (cross-links into TD-06 register entries)
│   │       └── 05-Release-Status.md
│   ├── TD-04-Decisions/
│   │   ├── 00-Index.md
│   │   └── NN-<slug>.md                    (single file by default — see contracts §5.4)
│   │       └── NN-<slug>/                  (folder ONLY if real supporting artifacts exist)
│   ├── TD-05-Multi-Tenancy/
│   │   ├── 00-Overview.md
│   │   └── NN-<Tenant-or-Aspect>.md
│   ├── TD-06-Limitations-and-Gaps/
│   │   └── 00-Register.md
│   └── TD-07-Runbooks/
│       ├── 00-Index.md
│       └── NN-<Runbook-Name>.md            (ALWAYS single file — no exceptions, 2am-readability)
│
├── 03-Release-Notes/
│   ├── 00-Index.md
│   ├── RN-01-Changelog/
│   │   └── CHANGELOG.md                    (cumulative, Keep a Changelog format)
│   ├── RN-02-Releases/
│   │   └── <version>/                      (folder per version)
│   │       ├── 00-Release-Notes.md         (audience-facing, derived from changelog)
│   │       └── 01-Migration-Guide.md       (only if this version has breaking changes)
│   └── RN-03-Deprecation-and-Roadmap/
│       ├── 00-Deprecation-Timeline.md      (links into each version's migration guide — never duplicates it)
│       └── 01-Roadmap.md                   (RESERVED)
│
└── 04-Code-Documentation/
    ├── 00-Index.md
    ├── CD-01-REST-API/                     (only if this project has a REST surface)
    │   ├── 00-Overview.md
    │   └── NN-<Resource>.md                (generated from OpenAPI)
    ├── CD-02-RPC-Reference/                (only if this project has RPCs, e.g. Supabase)
    │   ├── 00-Overview.md
    │   └── NN-<Domain>.md                  (generated from SQL function signatures)
    ├── CD-03-Flow-Reference/               (only if this project has Power Automate flows)
    │   ├── 00-Overview.md
    │   └── NN-<Flow-Group>.md              (generated from exported flow JSON)
    ├── CD-04-Auth-and-Errors/
    │   ├── 00-Authentication.md
    │   ├── 01-Error-Code-Reference.md
    │   └── 02-Rate-Limits-and-Quotas.md
    ├── CD-05-Integration-Guides/
    │   ├── 00-Quickstart-First-Call.md     (Stripe/Twilio pattern — task-based, not endpoint-by-endpoint)
    │   └── NN-<Common-Scenario>.md
    └── CD-06-Versioning-Policy.md          (links to RN-03 timeline — never duplicates it)
```

**Depth rules (apply when scaffolding any project)**

- **Modules (TD-03):** every module gets a folder. No judgment call, no exceptions.
- **Decisions (TD-04):** single file per decision by default (this is the entire point of the
  ADR format — Nygard/MADR are deliberately one-to-two pages). Promote to a folder only when a
  decision has real supporting artifacts (a comparison table, a benchmark) — not for
  consistency with Modules.
- **Runbooks (TD-07):** always single file. No exceptions, ever — a runbook's value is being
  scannable in one place during an incident.
- **Code Documentation (CD-01/02/03):** branch by interface type. Only create the branches that
  actually apply — a pure-REST project has no `CD-02-RPC-Reference/` or `CD-03-Flow-Reference/`
  folder at all, not an empty one.
- **Release Notes (RN-02):** folder per version, bundling that version's release notes and (if
  applicable) its migration guide together. There is no separate top-level Migration-Guides
  folder — deliberately eliminated in favor of this.

**ID scheme:** type-prefixed — `OB-`, `TD-`, `RN-`, `CD-`, each independently numbered within
its own type. Not one continuous register across all four.

**Scope:** every project gets its own fully independent tree. No shared vault-level layer, no
cross-project glossary or ADR pool, no links crossing project boundaries — even though several
projects may share stack, org, or contributors.

### 6. Document contracts — `references/document-contracts.md` (fixed section shapes)

Consistency across instances of the same document type is what makes the standard navigable.
Improvised structure per file is what makes it a pile.

**`00-MAP.md`** — Hub note. Links to `00-README`, `00-GLOSSARY`, all four type-folder
`00-Index.md` files, `99-Audit-Log`. Includes one Mermaid `flowchart` showing the top-level
structure. Every other note links back here (hub-and-spoke).

**`00-README.md`** — Purpose & scope in plain prose. What is documented, what is deliberately
not. One paragraph on why this project's structure might diverge from the canonical shape (e.g.
"no REST surface, only RPCs").

**Onboarding — `OB-03-First-Contribution/01-Guided-Walkthrough.md`** (the Diátaxis tutorial
proper) — the one file in the whole standard that must read as a tutorial, not a reference:
second person, imperative steps, one path only (no branching "or you could..."), ends with a
concrete, checkable outcome ("you're done when you see X").

**`TD-04-Decisions/NN-<slug>.md`** (ADR — Nygard/MADR shape):

```text
# ADR-NN: <title>

Status: Proposed | Accepted | Deprecated | Superseded by ADR-NN
Date: YYYY-MM-DD

## Context
<the forces at play, plain statement of the problem>

## Decision
<what was decided, stated as a commitment, not a suggestion>

## Alternatives considered
<options + why each was rejected>

## Consequences
<positive and negative, including what becomes harder>
```

One decision per file. Under two pages. Superseding a decision means writing a new ADR that
references the old one — never edit an Accepted ADR's Decision section.

**`TD-06-Limitations-and-Gaps/00-Register.md`** (repeating block, one per entry):

```text
### L-nn — <limitation / gap / warning name>

- What it is:        <plain statement>
- Impact:             <what breaks or degrades; who is affected>
- How you'd know:     <observable symptom>
- Workaround:         <safe mitigation, if any>
- Gate:                <approval/key/sign-off required, if any>
- Source:              <citation>
```

Every entry sourced. Cross-linked from the relevant module's `04-Gotchas.md`.

**`TD-07-Runbooks/NN-<Runbook-Name>.md`:**

```text
Goal · Preconditions · Steps (numbered, copy-pasteable) · Verification · Rollback

| Symptom (observable) | Likely cause | Action | Escalate if |
|---|---|---|---|

Escalation → OB-05-Ownership-and-Escalation
```

No step requires inferring cause from symptom.

**Code Documentation — per-resource/domain/flow-group file.** Same contract shape regardless of
interface type (REST/RPC/Flow), fields adapted to the paradigm:

| Field | REST (CD-01) | RPC (CD-02) | Flow (CD-03) |
|---|---|---|---|
| Identity | Method + URL | Function signature | Trigger |
| Inputs | Parameters (path/query/body/header) | Parameters (name/type/required) | Inputs |
| Output | Example response (success) | Example return value | Actions taken |
| Failure | Example response (error) + error codes | Exceptions / error codes | Error handling behavior |
| Notes | Deprecation tag if applicable | RLS/security context | — |

Every entry has a real example, not a placeholder. Every field sourced from the generator
(OpenAPI spec / SQL signature / exported flow JSON) — never hand-typed from memory.

**`CD-05-Integration-Guides`** — task-based, not endpoint-based. Stripe/Twilio pattern: organize
by what the reader is trying to do ("save a card", "handle a webhook"), not by a flat list of
endpoints. Each guide is a short walkthrough that references the relevant CD-01/02/03 entries
rather than restating them.

**`RN-01-Changelog/CHANGELOG.md`** — Standard Keep a Changelog 1.1.0 format: `## [Unreleased]`
at top, then one `## [version] - YYYY-MM-DD` section per release, six category headings
(`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`) — only the categories that
apply, skip empty ones. SemVer noted at the top of the file.

**`RN-02-Releases/<version>/00-Release-Notes.md`** — Audience-facing derivative of the
changelog entry for this version — written for a PM or stakeholder, not a developer. Plain
language, no category headings, leads with impact.

### 7. UNIPEN's workflow (declined governance gate — Decision 3)

1. **Intake** — ask the fixed, minimal setup questions (Decision 7): project name / vault
   destination path, and fresh scaffold vs. filling gaps in an existing tree. Not an approval
   gate — just the facts UNIPEN cannot infer.
2. **Recon** — scan the target project (stack, existing docs, module list, interface types
   present) to decide which optional branches apply (REST/RPC/Flow under Code Documentation,
   per-module folders, etc.), and, on an incremental run, which files already exist. Analysis
   only — no operator approval wait before proceeding.
3. **Scaffold** — create the folder tree from `references/folder-structure.md`. On a fresh
   project, write every file, including RESERVED stubs (frontmatter + breadcrumb +
   `trust: RESERVED`, empty or one-line-placeholder body — created before anything links to
   them). On an incremental run, only create what's missing — existing files are untouchable
   by default (Decision 8) unless the operator names one to update.
4. **Fill each document type** against its contract in `references/document-contracts.md`,
   applying `references/conventions.md` (trust ladder, tiering, citation rule, frontmatter,
   breadcrumb, wikilink rules) and `references/diagram-catalog.md`.
5. **Human-only content** (`OB-05-Ownership-and-Escalation`, tenant specifics in
   `TD-05-Multi-Tenancy`) is scaffolded with explicit questions for the project owner, marked
   `PARTIAL`, never fabricated. Unconfirmable content elsewhere is marked
   `UNVERIFIABLE — <detail>. Confirm or abort.` rather than invented.
6. **Deliver** — write via Obsidian MCP tools (`mcp__mcp-obsidian__*`) when available in the
   session; fall back to plain file writes to the given vault path otherwise (Decision 9).
7. **Self-check** against the Definition of Done below before declaring the tree complete.

Writes happen directly, in whatever order is efficient — no batch/verify/approve ceremony, no
formal acceptance test phase.

### 8. `SKILL.md` structure (progressive disclosure)

```text
unipen/skills/unipen/
├── SKILL.md                       required — frontmatter + workflow, keep under ~500 lines
└── references/
    ├── folder-structure.md        the canonical tree from Design §5, verbatim
    ├── document-contracts.md      all contracts from Design §6
    ├── conventions.md             Design §3 in full — self-contained (Decision 2)
    └── diagram-catalog.md         Design §4 in full, including the Mermaid UML use-case caveat
```

`SKILL.md` frontmatter needs a **pushy** description — state both what it does and the specific
contexts that should invoke it (project documentation, onboarding docs, technical docs,
changelog, release notes, API reference, "document this project", "write onboarding for X",
etc.), even when the user doesn't say "UNIPEN" or "GDS" explicitly.

The `SKILL.md` body contains the **workflow** (Design §7), with clear pointers to each
`references/*.md` file and guidance on when to load which — not the full contracts inline.

### 9. Repo housekeeping

- `CLAUDE.md` — add `unipen/` to the repository-structure listing; document the two-plugin
  marketplace pattern (one repo, two independently-installable plugins: `black-sea` at `.`,
  `unipen` at `./unipen`).
- `CONTRIBUTING.md` — note the second plugin entry in `marketplace.json`; note both plugins
  share one repo version for now (Decision 6).
- `docs/unipen.md` — human-facing overview page, mirroring `docs/black-sea.md`.
- One changeset (`npx changeset`, `minor`) describing "add UNIPEN plugin," run once the skill
  files are built.

---

## Definition of Done (for this build)

```text
[ ] unipen/.claude-plugin/plugin.json exists, name "unipen", version matches repo version
[ ] marketplace.json's "plugins" array has a second entry: name "unipen", source "./unipen"
[ ] unipen/skills/unipen/SKILL.md frontmatter has a pushy, specific trigger description
[ ] SKILL.md body is under ~500 lines and points to references/ rather than inlining contracts
[ ] references/folder-structure.md matches Design §5 exactly, including the "only create
    branches that apply" rule for CD-01/02/03
[ ] references/document-contracts.md covers every document type in Design §6
[ ] references/conventions.md is self-contained: trust ladder, tiering, citation rule,
    frontmatter schema, breadcrumb format, and all wikilink rules — zero mention of Handover Kit
[ ] references/diagram-catalog.md includes the Mermaid UML use-case-diagram caveat verbatim
[ ] No operator-approval gate / batching ceremony baked into the workflow (Decision 3)
[ ] Vault output path is {{PROJECT}}/ directly, no Private/Black Sea/ nesting (Decision 4)
[ ] Nothing in the Handover Kit skill/files was read, modified, or referenced
[ ] No pilot project was scaffolded — this build produces the skill only
[ ] CLAUDE.md, CONTRIBUTING.md, docs/unipen.md updated; a changeset added
```

---

## Next steps (tool sequence, per operator instruction)

1. **interview-me** — one more one-at-a-time pass to squeeze out any remaining ambiguity in
   this spec before implementation starts.
2. **skill-creator** — author `unipen/skills/unipen/SKILL.md` + `references/*.md` following
   best-practice skill-authoring conventions, plus the repo housekeeping in Design §9.
