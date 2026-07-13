# The Operative Contract

The stable interface between the **orchestrator** (BLACK SEA), the **front door** (WAYPOINT), and the
**operatives** (DRY DOCK, PLIMSOLL, HARBORMASTER, HORIZON, GRASSHOPPER, PARLEY). It exists so each
operative can be built and reasoned about independently: same input shape in, same **findings packet**
out, whatever the lane. WAYPOINT writes the Collection Plan; BLACK SEA slices it to operatives;
operatives return findings packets; BLACK SEA assembles the dossier.

## The Collection Plan (WAYPOINT's output)

The case's approved heading. No collection begins until the operator approves it.

```text
CODENAME · TIER (FLASH / FULL)
Intelligence question(s)  — one sentence each; the tasking the dossier answers
Scope & boundaries        — time window · entities in/out · jurisdictions · explicit exclusions
EEI table:
  | # | EEI item | tier (specified/implied/adjacent) | why (adjacent only) | operative | source class |
Anticipated gaps          — what we expect to be out of reach, and the lawful next step
Approval                  — operator sign-off (date)
```

- **specified** = literally asked for · **implied** = required by the objective though unstated ·
  **adjacent** = analyst-improvised, and only these carry the "why this serves your decision" line.
- Every EEI is routed to exactly one **operative** and a **source class** (the record type / registry
  it will be pursued in — see `registry-sources.md`).

## Operative input (the plan slice)

Each operative receives, from BLACK SEA:

- Its assigned **EEI** rows (with tiers and the source classes).
- The case **scope & boundaries**, **codename**, and **tier**.
- Any **provided material** relevant to its lane (worked first — highest signal, lowest cost).

## Operative output — the findings packet

Every operative returns the same five-part packet, in this order. It maps straight into the dossier's
PART II and Annexes.

1. **Findings** — each a claim · its label (**FACT** / **ASSESSMENT** / **ASSUMPTION**) · its
   **confidence** (High / Moderate / Low) *and the reason* · source refs (→ Evidence Register). Keep
   likelihood (odds) and confidence (how sure) as separate axes.
2. **Evidence-Register fragment** — source-by-source: ref#, what it is, where it's from, **Admiralty**
   grade (A–F / 1–6), what it supports.
3. **Entities discovered** — identifiers, role, connections — for the Entity Register.
4. **Gaps** — each named, with a next-collection step (including anything blocked by tools / offline /
   law). A named gap is a result; a filled-in guess is fabrication.
5. **Lane block** (optional) — the lane-specific deliverable (Financial Forensics / Competitor Posture
   / Subject Profile / etc.).

## Assembly (BLACK SEA)

BLACK SEA merges the packets: dedupe entities into one Entity Register, renumber evidence refs into one
Evidence Register, order findings by decision-relevance, and emit the standard dossier template at the
chosen tier. The pre-flight checklist runs before delivery — including the line that a WAYPOINT
Collection Plan was approved before any collection ran.

## The doctrine floor (every operative carries it)

An operative invoked on its own — outside the orchestrator — still holds the line:

- Label every claim **FACT** / **ASSESSMENT** / **ASSUMPTION**.
- Grade every source on the **Admiralty** scale.
- Name every **gap**; never fill it.

For the full technique set (source grading, ACH, the divergent Requirements-Expansion pass), read
`analytic-tradecraft.md`; for collection and forensics discipline, `collection.md`.
