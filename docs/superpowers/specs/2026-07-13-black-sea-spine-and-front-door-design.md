# Spec — BLACK SEA: Spine & Front Door (Sub-project 1)

- **Date:** 2026-07-13
- **Status:** Approved design, pending implementation plan
- **Version target:** 2.2.0 → **3.0.0** (major — structural re-architecture from single-skill to multi-skill plugin)
- **Sub-project:** 1 of the BLACK SEA suite rebuild (see *Program context*)

---

## Program context (the whole unit — for orientation, not all built here)

BLACK SEA is being rebuilt from **one skill that does everything** into a **multi-skill
plugin**: a unit orchestrator + a shared doctrine core + a roster of named operatives.
Callsigns are provisional (rename freely); the function and trigger are load-bearing.

```text
BLACK SEA  ─ the Unit / orchestrator (entry point + shared doctrine core)
Front door
  WAYPOINT      operator requirements-elicitation (Frame & Confirm)
Operatives
  DRY DOCK      corporate & ownership / shell / UBO tracing
  PLIMSOLL      financial-statement forensics + 4-mode back-testing + forensics.py
  HARBORMASTER  person profiling & due diligence (legitimate-purpose gate)
  HORIZON       competitor & market intelligence
  GRASSHOPPER   link / entity / network analysis
  PARLEY        HUMINT source elicitation (John Nolan baseline; legal line only)
```

**Build order** (each its own spec → plan → build): **(1) Spine & Front Door ← THIS SPEC**,
(2) PLIMSOLL, (3) DRY DOCK, (4) HARBORMASTER, (5) GRASSHOPPER, (6) HORIZON, (7) PARLEY.
Separately deferred: a doctrine/RBAC **system-design** skill (a *different job* from
investigation — produces a design, not a dossier; specced on its own later).

This sub-project builds the **spine and the front door only**, plus the **contract** the six
operatives will plug into. The operative lanes remain as today's reference files until each
graduates in its own sub-project; nothing about their discipline is lost in the interim.

---

## Problem (why this sub-project exists)

Two behavioural gaps confirmed at the source level in the current single skill:

1. **No intake / interview.** `SKILL.md` Step 1 actively caps questioning at *"ask **one**
   sharp scoping question … otherwise … proceed"* and the pre-flight checklist never checks
   that scope was confirmed with the operator. Result: the unit investigates *its own* reading
   of the ask.
2. **No requirements-decomposition / improvisation.** The workflow jumps from "state the
   question" straight to "collect." `analytic-tradecraft.md` carries only *convergent*
   techniques (ACH, Key Assumptions) that test what you already have; nothing *generates* the
   adjacent information a seasoned analyst would also pull. The Prime Directive's
   anti-fabrication ethos, unqualified, further suppresses legitimate anticipatory analysis.

## Goals

- Every case opens by **eliciting the operator's true intent** and **confirming scope** before
  any collection — depth scaled to stakes, never zero questions.
- The tasking is **decomposed into specified → implied → adjacent EEI**, with the adjacent
  (improvised) items each justified against the operator's real decision.
- A single **Collection Plan** artifact is produced and **operator-approved** before collection.
- A **divergent tradecraft technique** and an explicit **"anticipation is not fabrication"**
  carve-out are added to the shared doctrine.
- A **stable operative contract** (plan-slice in → findings packet out) is defined so the six
  operatives can each be specced independently against it.

## Non-goals (out of scope for this sub-project)

- Building DRY DOCK / PLIMSOLL / HARBORMASTER / HORIZON / GRASSHOPPER / PARLEY as skills.
- The financial back-testing depth and `forensics.py` multi-period extension (Sub-project 2).
- The doctrine/RBAC system-design skill (separate program, deferred).
- Changing the dossier template's substance, the Obsidian delivery protocol, or the boundaries.

---

## Design

### 1. BLACK SEA orchestrator (refactored)

Keeps: identity/aesthetic, Prime Directive, operating boundaries, negative triggers, FLASH/FULL
tiers, dossier template, worked example, pre-flight checklist, failure modes.

Changes — the workflow becomes a **dispatch** flow:

1. Fire on investigation intent / callsign.
2. **Run WAYPOINT** (frame & confirm) → obtain the approved Collection Plan.
3. **Route** to the operative(s) the plan assigns. Until an operative has graduated into its own
   skill, "route" means *read that lane's reference file* (today's behaviour) — so no discipline
   is lost mid-migration. Once graduated, "route" means *invoke that operative skill*.
4. Collect **findings packets** back from each lane/operative.
5. **Assemble** the dossier (merge packets, dedupe entities, order by decision-relevance).
6. **Pre-flight**, then **deliver** to the Obsidian vault (unchanged protocol).

Edits:

- Step 1 ("Establish the tasking") is replaced by "**Phase 1 — Frame & Confirm (delegates to
  WAYPOINT)**." The old "ask one sharp question" instruction is removed.
- The Step 2 routing table gains an **Operative** column (callsign) alongside the existing
  Reference column, so it reads as "route to `WAYPOINT`/`DRY DOCK`/… (ref: `references/…`)".
- Pre-flight gains one line: **"WAYPOINT Collection Plan was produced and operator-approved
  before any collection ran."**

### 2. Shared doctrine core + cross-skill mechanism

The canonical doctrine stays **single-source-of-truth in `black-sea/references/`**:
`analytic-tradecraft.md` (+ new divergent technique), `collection.md`, `registry-sources.md`,
document/image forensics, `glossary.md`.

**Mechanism (decided):** operatives reference the canonical files **by relative path**, and each
operative also embeds a **3-line "doctrine floor"** so standalone invocation degrades gracefully:

> Doctrine floor (present in every operative): (a) label every claim FACT / ASSESSMENT /
> ASSUMPTION; (b) grade every source (Admiralty A–F / 1–6); (c) name every gap — never fill it.
> For the full technique set, read `../black-sea/references/analytic-tradecraft.md`.

This keeps one authoritative doctrine (no drift) while ensuring an operative invoked outside the
orchestrator still keeps its spine. The relative-path assumption (sibling skills under a common
root) is documented in CONTRIBUTING and re-checked when the first operative graduates.

### 3. WAYPOINT — operator requirements-elicitation (the front door)

New skill. Fires when BLACK SEA delegates, or directly on an explicit call. Wraps the
`interview-me` skill for interview depth on FULL cases.

**Workflow:**

1. **Receive tasking** — the raw ask + any provided material.
2. **Assess tier** — FLASH vs FULL from stakes/deadline cues; when unsure, default FLASH and
   offer to escalate.
3. **Interview (depth scaled, never zero):**
   - FLASH: 1–2 sharp questions.
   - FULL: structured interview via `interview-me` — targets the *real decision* behind the ask,
     deadline/tier, entities in/out, jurisdictions, material already held, definition of "done,"
     sensitivity/legal constraints.
4. **Decompose requirements** into three tiers:
   - **Specified EEI** — literally asked for.
   - **Implied EEI** — logically required by the objective though unstated.
   - **Adjacent EEI** — the improvisation: what a seasoned analyst also pulls because it serves
     the operator's real decision; **each carries a one-line "why this serves your decision."**
5. **Draft the Collection Plan** (shape below).
6. **Confirm** — present the plan; operator approves / prunes adjacent items / adds. **No
   collection begins until approved.**
7. **Hand back** the approved plan to BLACK SEA.

**Done when:** an operator-approved Collection Plan exists with EEI decomposed into the three
tiers, each adjacent item justified and routed to an operative, and codename + scope fixed.

### 4. Divergent-EEI technique + carve-out (added to `analytic-tradecraft.md`)

New section: **Requirements Expansion / Anticipatory EEI (the divergent pass).** Before
narrowing, deliberately generate the adjacent information space: "what would a domain expert in
this area also want to know that the operator didn't say?", "what does this decision depend on
that isn't named?", a **pre-mortem** ("if this dossier misses the mark, what did we fail to look
at?"), and the **so-what/then-what** chain. Output feeds WAYPOINT's Adjacent EEI tier.

**The carve-out (the fix for over-suppression):**

> **Anticipating what to collect is analysis, not fabrication.** The Prime Directive forbids
> inventing *facts, sources, records, or figures* — it never forbids *reasoning about what to
> look for*. Adjacent EEI are **questions to pursue, not answers asserted**. The pull to fill in
> a fact is still a gap; the instinct to widen the collection net is tradecraft.

### 5. The operative contract (interface for all six)

- **Input:** the operative's slice of the approved Collection Plan — assigned EEI + scope &
  boundaries + codename + tier + relevant provided material.
- **Process:** read own lane discipline + shared doctrine; collect; run forensics/analysis; grade.
- **Output — a standard findings packet:**
  - Graded **findings** (claim · FACT/ASSESSMENT/ASSUMPTION · confidence High/Mod/Low + reason ·
    source refs).
  - **Evidence-Register fragment** (per-source, Admiralty A–F / 1–6).
  - **Entities discovered** (identifiers, role, connections) for the Entity Register.
  - **Gaps** (named, with next collection step).
  - Optional **lane-specific block** (e.g. Financial Forensics / Subject Profile).
- **Assembly:** BLACK SEA merges packets → dedupes entities → assembles the dossier's Part II +
  Annexes → pre-flight → delivers.

---

## Data shapes

**Collection Plan** (WAYPOINT output; markdown, lives in the case as an artifact):

```text
CODENAME · TIER (FLASH/FULL)
Intelligence question(s)  — the PIR(s), one sentence each
Scope & boundaries        — time window · entities in/out · jurisdictions · exclusions
EEI table:
  | # | EEI item | tier (specified/implied/adjacent) | why (adjacent only) | operative | source class |
Anticipated gaps          — what we expect to be out of reach, and the lawful next step
Approval                  — operator sign-off line (date)
```

**Findings packet** (operative output): the five bulleted elements in §5, in that order.

---

## Repo & versioning changes

- New skill directory for **WAYPOINT** (`skills/waypoint/` or plugin-appropriate location).
- Edits to `skills/black-sea/SKILL.md` (dispatch workflow, routing table, pre-flight line) and
  `skills/black-sea/references/analytic-tradecraft.md` (divergent technique + carve-out).
- **CLAUDE.md / AGENTS.md:** the "single-skill repo" convention is replaced with the multi-skill
  plugin layout and the shared-doctrine mechanism.
- **`docs/black-sea.md`:** re-synced to the unit/roster model.
- **Manifests in lockstep:** `package.json`, `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json` → **3.0.0**; add the WAYPOINT skill entry to the plugin +
  marketplace manifests.
- **Changeset:** one entry (major) via `npx changeset`, folded with `npx changeset version`.

## Verification

- **Trigger test:** an investigation ask fires BLACK SEA → BLACK SEA runs WAYPOINT before any
  collection language appears.
- **Interview test:** a FULL/high-stakes ask produces a structured interview; a FLASH ask asks
  1–2 questions — neither proceeds with zero.
- **Improvisation test:** a deliberately narrow ask (the operator's own "vendor legit?" case)
  yields a Collection Plan containing **adjacent EEI the operator did not name**, each justified.
- **Gate test:** no collection content is produced before the plan is marked approved.
- **Doctrine-floor test:** an operative reference invoked in isolation still labels
  FACT/ASSESSMENT/ASSUMPTION and grades sources.
- **Prime-Directive regression:** adjacent EEI appear as *questions*, never as asserted findings.

## Open items / deferred

- Exact install-layout for cross-skill relative paths — re-validated when the first operative
  (PLIMSOLL) graduates in Sub-project 2.
- Whether WAYPOINT should persist the approved Collection Plan into the vault case folder or hold
  it in-session — decide during implementation planning.
