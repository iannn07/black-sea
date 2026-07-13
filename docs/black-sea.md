# BLACK SEA

## What it does

BLACK SEA is an all-source investigative-analyst **unit**: give it a target — an organization or a
person — and it produces a standardized, confidence-graded intelligence dossier you can act on without
redoing the work. Every case opens at the **WAYPOINT** front door, which interviews you and turns the
ask into an operator-approved **Collection Plan** — decomposing it into specified, implied, and
*adjacent* requirements (the adjacent ones you wouldn't think to ask for). The orchestrator then
dispatches to named **operatives** over the shared doctrine core, and delivers into your Obsidian
vault. Its defining constraint is the **Prime Directive**: it never fabricates — every finding traces
to a real source or is labeled an assessment or assumption, and anything it cannot lawfully obtain is
written down as a named gap rather than filled in.

## The unit

- **BLACK SEA** — the orchestrator: frames the case, dispatches operatives, assembles and delivers the dossier.
- **WAYPOINT** — the front door: interviews you and emits the operator-approved Collection Plan.
- **DRY DOCK** — corporate structure & beneficial-ownership / shell tracing.
- **PLIMSOLL** — financial-statement forensics + multi-period back-testing (`forensics.py`).
- **HARBORMASTER** — person profiling & due diligence, behind a legitimate-purpose gate.
- **HORIZON** — competitor & market intelligence.
- **GRASSHOPPER** — link / entity / network analysis.
- **PARLEY** — lawful source elicitation (modelled on John Nolan's legal-CI method).

## When to reach for it

- **Invocation.** Type `/black-sea` (or `/black-sea:black-sea` under the plugin), or the agent reaches
  for it automatically when a task looks like an investigation — "investigate", "dossier", "due
  diligence", "who really owns", "is this company legit", "follow the money", "OSINT", or a plain
  "look into X for me".
- **Reach for it when** you need a target worked hard and the result graded for confidence: a
  counterparty before you sign, a hire before an offer, a competitor's real posture, a set of filings
  or financials you suspect. For a single quick fact ("when was Acme founded"), just ask normally —
  that is not a case.

## Prerequisites

- **`python3` on PATH** — the `forensics.py` calculator (Beneish M-Score, Altman Z / Z'', Benford,
  ratios) is standard library only, no pip installs.
- **Obsidian delivery (optional)** — an `mcp-obsidian` server reachable from Claude Code. Without it,
  BLACK SEA renders the dossier in chat and marks vault delivery pending.

## The two tiers

Right-size the product before building it:

- **FLASH** — a compressed single-screen read: BLUF, 3–6 confidence-graded key findings with sourcing,
  and the top collection gaps. For a quick take or a time-boxed ask.
- **FULL** — the complete standardized dossier, all annexes. For high-stakes decisions and formal
  deliverables.

FLASH is *shorter*, never *sloppier* — both keep the BLUF, confidence grades, real sourcing, and an
honest gaps line.

## It's working if

- The case opened with a **WAYPOINT Collection Plan you approved** — including *adjacent* requirements
  you never named — before any collection ran.
- Every key finding is graded (High / Moderate / Low) and points at a source in the Evidence Register.
- Likelihood (the odds) and confidence (how sure) read as two separate axes, never merged.
- The dossier carries a populated, honest gaps section — a named gap, not a plausible fill-in.
- Link networks and timelines render as Mermaid, and (when a vault is present) the note lands in
  `Private/Black Sea/[CODENAME]/` with compliant frontmatter and an appended audit-log line.

## Where it fits

BLACK SEA is a reach-for-it-anytime unit: an orchestrator that runs a whole case end to end
(**WAYPOINT** framing → approved Collection Plan → operative dispatch → collection → tradecraft →
dossier → delivery). The depth lives in `skills/black-sea/references/` behind context pointers; the
vocabulary that keeps runs predictable lives in `CONTEXT.md` and the skill's `glossary.md`.
