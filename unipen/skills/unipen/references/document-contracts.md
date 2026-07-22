# UNIPEN Document Contracts

Fixed section shapes for every document type. Consistency across instances of the same type is
what makes the standard navigable — improvised structure per file is what turns it into a pile.
Apply `conventions.md` (frontmatter, breadcrumb, trust/tier, citation rule) to every file below
in addition to the shape given here.

## `00-MAP.md`

Hub note. Links to `00-README`, `00-GLOSSARY`, all four type-folder `00-Index.md` files, and
`99-Audit-Log`. Includes one Mermaid `flowchart` showing the top-level structure. Every other
note links back here — this is the hub in a hub-and-spoke tree, so a reader landing anywhere can
always get back to the center in one hop.

## `00-README.md`

Purpose & scope in plain prose: what is documented, what is deliberately not. One paragraph on
why this project's structure might diverge from the canonical shape (e.g. "no REST surface,
only RPCs, so there is no `CD-01-REST-API/` folder").

## Onboarding — `OB-03-First-Contribution/01-Guided-Walkthrough.md`

This is the one file in the whole standard that must read as a **tutorial**, not a reference —
the Diátaxis tutorial mode, in full: second person, imperative steps, one path only (no
branching "or you could..."), ends with a concrete, checkable outcome ("you're done when you see
X"). Every other document type can hedge or branch; this one can't — a tutorial that branches
mid-walkthrough stops being a tutorial.

## `TD-04-Decisions/NN-<slug>.md` — ADR (Nygard/MADR shape)

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

One decision per file. Under two pages — if it's running longer, the decision is probably two
decisions. Superseding a decision means writing a **new** ADR that references the old one; never
edit an Accepted ADR's Decision section after the fact — that section is the historical record of
what was actually decided, not a living document.

## `TD-06-Limitations-and-Gaps/00-Register.md`

Repeating block, one per entry:

```text
### L-nn — <limitation / gap / warning name>

- What it is:        <plain statement>
- Impact:             <what breaks or degrades; who is affected>
- How you'd know:     <observable symptom>
- Workaround:         <safe mitigation, if any>
- Gate:                <approval/key/sign-off required, if any>
- Source:              <citation>
```

Every entry sourced (per the citation rule in `conventions.md`). Cross-linked from the relevant
module's `04-Gotchas.md`, so a reader hitting a gotcha in a specific module can find the full
register entry without hunting.

## `TD-07-Runbooks/NN-<Runbook-Name>.md`

```text
Goal · Preconditions · Steps (numbered, copy-pasteable) · Verification · Rollback

| Symptom (observable) | Likely cause | Action | Escalate if |
|---|---|---|---|

Escalation → OB-05-Ownership-and-Escalation
```

No step requires inferring cause from symptom — a runbook is read at 2am under pressure, so the
symptom table has to point straight at an action, not require diagnostic judgment first.

## Code Documentation — per-resource/domain/flow-group file

Same contract shape regardless of interface type (REST/RPC/Flow), with fields adapted to the
paradigm:

| Field | REST (`CD-01`) | RPC (`CD-02`) | Flow (`CD-03`) |
|---|---|---|---|
| Identity | Method + URL | Function signature | Trigger |
| Inputs | Parameters (path/query/body/header) | Parameters (name/type/required) | Inputs |
| Output | Example response (success) | Example return value | Actions taken |
| Failure | Example response (error) + error codes | Exceptions / error codes | Error handling behavior |
| Notes | Deprecation tag if applicable | RLS/security context | — |

Every entry has a **real example**, not a placeholder — a `{ "example": "value" }` stub is worse
than no example, because it looks complete without being useful. Every field is sourced from the
generator (the OpenAPI spec, the SQL function signature, the exported flow JSON) — never
hand-typed from memory, since memory drifts from the code the moment either one changes.

## `CD-05-Integration-Guides` — task-based, not endpoint-based

Stripe/Twilio pattern: organize by what the reader is trying to *do* ("save a card", "handle a
webhook"), not by a flat list of endpoints. Each guide is a short walkthrough that references
the relevant `CD-01`/`02`/`03` entries rather than restating them — per "elevate and link, never
duplicate."

## `RN-01-Changelog/CHANGELOG.md`

Standard Keep a Changelog 1.1.0 format: `## [Unreleased]` at the top, then one
`## [version] - YYYY-MM-DD` section per release, using the six category headings (`Added`,
`Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`) — only the categories that actually
apply for that release; skip the empty ones rather than listing them with nothing under them.
Note the SemVer scheme at the top of the file.

## `RN-02-Releases/<version>/00-Release-Notes.md`

Audience-facing derivative of the changelog entry for this version — written for a PM or
stakeholder, not a developer. Plain language, no category headings, leads with impact ("what
changed for you"), not with the mechanics of what changed in the code.
