# Financial Back-Testing (PLIMSOLL)

Reading a single set of statements tells you what a company *says*. Back-testing tells you whether
the statements **hold up** — against the outside world, against their own history, against the
screens, and against a bottom-up reconstruction. Pair with `org-financial.md` (statement forensics),
`collection.md`, and `analytic-tradecraft.md`. Every output is an **indicator that directs
collection**, never a verdict.

The name is the load line on a ship's hull: it shows whether the vessel is riding true or is
overloaded and sitting false in the water.

## The four modes (run the ones the evidence supports)

### 1. Validate against reality

Reconcile the reported figures against **independent anchors** — never take the statements as their
own proof:

- Peer / industry benchmarks (margins, DSO, growth) — an outlier vs. the sector is a question.
- The same entity's filings in **other jurisdictions or registries** (a subsidiary's local accounts,
  tax filings, customs/trade data where public) — cross-filed numbers that disagree are a **finding**.
- Public bank / customer / supplier confirmations, procurement awards, headcount, physical footprint.
- Where numbers can't be anchored, that's a **gap** with a named next source — not a pass.

### 2. Test prior claims vs. actuals

Pull the **historical run** of statements and guidance, then check whether the past materialised:

- Did prior-year projections / guidance land, or quietly reset?
- Restatements, reclassifications, and one-off items that reappear every year (a "one-off" that
  recurs is recurring).
- Accruals that reverse, provisions taken and released to smooth a period.
- Auditor / CFO changes and late filings around the periods that matter.

### 3. Run + calibrate the screens across the whole series

Do not eyeball trends. Run the bundled calculator in **series mode** across every period at once:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/forensics.py <input.json>
python3 ${CLAUDE_SKILL_DIR}/scripts/forensics.py --schema   # shows the "series" shape
```

Feed a `"series"` list of periods, ordered oldest -> newest. The tool returns the ratio **trend**
(DSO, margins, current ratio), a **rolling Beneish** M-Score on each consecutive pair, and the
**receivables-vs-sales growth divergence** — the classic channel-stuffing / premature-recognition
tell. Calibrate the reading: a screen that flags every period may be mis-fed; a screen that would not
have caught a known prior problem is weak evidence. State the limits (estimated inputs, Benford needs
a large natural dataset).

### 4. Reconstruct the numbers bottom-up

Rebuild the key figure from **independent drivers** and compare to what was reported:

- Revenue from unit economics (units × price), disclosed segments, capacity, or headcount × revenue-per-head.
- Costs from input prices and volumes; margins from the reconstructed lines.
- A reconstruction that lands far from the reported figure is an **indicator to pull the ledgers** —
  report the method and the assumptions in the open so the reader can pressure-test them.

## Deliverable (PLIMSOLL findings packet, "Financial Forensics" block)

Return, per the operative contract: the ratio/screen table with **computed values and their
interpretation**; the trend and divergence read from series mode; the anchors that did / didn't
reconcile (validate-vs-reality); the reconstruction and its assumptions; each finding
confidence-graded and sourced; and — non-negotiable — the data you *couldn't* get (ledgers, bank
records, private filings) as **Collection Gaps**. Screening outputs are indicators that direct
further collection, never a standalone accusation.
