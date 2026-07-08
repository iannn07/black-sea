# BLACK SEA

The ubiquitous language of the BLACK SEA skill — a Special Investigation Unit / CID that takes a
target (an organization or a person) and produces a standardized, confidence-graded intelligence
dossier. This document exists so the skill, its references, and anyone editing them speak one
language; the leading words here are used *exactly* as defined. The in-skill copy is
`skills/black-sea/references/glossary.md` — keep the two in sync.

## Language

**Prime Directive**:
Never fabricate. Every finding traces to a real source or is labeled an assessment or assumption;
anything unobtainable is a named **gap**. The pull to "fill in" a plausible detail is the signal to
write a gap instead.
_Avoid_: accuracy policy, hallucination guard (too weak — this is the load-bearing rule)

**Target** (also **subject**):
The organization or person a case investigates.
_Avoid_: mark, suspect (each presumes a verdict the dossier has not reached)

**Tasking** (the **intelligence question**):
The single sharp question a case answers, fixed in writing before collection. "Investigate Acme" is a
direction; "Is Acme's revenue growth real or manufactured?" is a tasking.
_Avoid_: prompt, ask, request

**Lane**:
One of the three investigation branches — **org & financial forensics**, **competitor & market
intel**, **person profiling** — each reached by a context pointer to its reference file. A case may
run several.
_Avoid_: mode, track, module

**Shared core**:
The two references every lane draws on — **collection** and **analytic tradecraft**. Read on
essentially every case.
_Avoid_: common library, base

**Tier**:
The size of the product — **FLASH** (a compressed single-screen read) or **FULL** (the complete
standardized dossier). FLASH is *shorter*, never *sloppier*.
_Avoid_: mode, format, quick/deep

**Dossier**:
The standardized deliverable: BLUF, confidence-graded findings, real sourcing, and an honest gaps
line, against the fixed template.
_Avoid_: report, write-up, summary

**Codename**:
The all-caps case designation (e.g. `OP. MERIDIAN`). Targets are referred to by codename in the vault.
_Avoid_: case name, project name

**Evidence Register** (the **register**):
Annex A — source-by-source provenance and Admiralty grade. Every FACT points into it.
_Avoid_: sources list, bibliography

**FACT / ASSESSMENT / ASSUMPTION**:
The three labels every claim carries — sourced / reasoned-from-facts / unverified-premise. Never
blurred into one another.

**gap**:
A fact not lawfully obtainable this session; named, with a next-collection step. A named gap is a
professional result; a filled-in guess is fabrication.

**cold / confirmed**:
A finding with no independent corroboration is *cold*; a second, separate-origin source makes it
*confirmed*. Ten sites echoing one press release is one source, not ten.

**clean**:
Collection obtained without breaking a law or a terms-of-service. Anything that would need pretexting,
unauthorized access, or stolen data is a gap, not a task.

**the seam**:
Where anomalies live — shared officers/addresses/phones, impossible timelines, round-number
financials, metadata that contradicts a claim. Look here first.

**Admiralty grade**:
The two-axis source rating — reliability A–F × credibility 1–6 — on every register entry.

**ACH** (Analysis of Competing Hypotheses):
Test evidence against all plausible explanations, weighting disconfirmation hardest. The innocent
explanation is always a required hypothesis.

## Relationships

- A **case** answers one **tasking**, routes to one or more **lanes**, and every lane draws on the two **shared cores**.
- A case produces one **dossier** at one **tier** (FLASH or FULL), delivered under a **codename**.
- Every **FACT** in a dossier points into the **Evidence Register**; every register entry carries an **Admiralty grade**.
- Every claim is a **FACT**, an **ASSESSMENT**, or an **ASSUMPTION**; anything unobtainable is a **gap**.

## Flagged ambiguities

- "report" was ambiguous between the *deliverable* and a *status message to the operator* — resolved:
  the deliverable is the **dossier**; a status message is a NIGHTSTALKER comms report (`BLACK SEA → ACTUAL:`).
- "source" drifted between an *origin* and a *citation* — resolved: an **Evidence Register** entry is
  the citation; corroboration counts *origins*, so republishers of one origin are one source.
- "confidence" vs "likelihood" — resolved: kept as two axes. **Likelihood** (the estimative-probability
  ladder) is the odds a thing is true; **confidence** (High / Moderate / Low) is how sure the analyst
  is of that judgment. Never silently merged.

## Related

- `skills/black-sea/references/glossary.md` — the in-skill leading-words copy
- `CLAUDE.md` — repo instructions & conventions
- `CONTRIBUTING.md` — the compliance guard for edits
