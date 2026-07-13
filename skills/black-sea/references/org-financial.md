# Lane: Organization & Financial Forensics

For "is this company legit," "who really owns it," "follow the money," fraud, and financial-statement
analysis. Pair with `collection.md` and `analytic-tradecraft.md`.

## A. Structure & ownership tracing

Goal: get from the public-facing name to the **ultimate beneficial owners** and the real control map.

- Build the corporate tree: parent/subsidiary/affiliate, jurisdiction of each, registration dates.
- Identify officers, directors, registered agents, and shareholders of record.
- Trace **control vs. ownership** — nominee directors and bearer arrangements hide real control.
- **Shell/opacity red flags:** incorporation in secrecy jurisdictions with no local operations;
  mass-registration agent addresses; circular or layered ownership; entities dormant then suddenly
  transacting; name near-collisions with reputable firms; officers tied to prior dissolved entities.

## B. Financial-statement forensics

Work the numbers as an adversary would hide in them. Compute, then interpret.

**Ratio & trend analysis** — liquidity, leverage, margin, turnover across periods and vs. peers.
Divergence between reported earnings and cash generation is the classic tell.

**Screening models — compute them, don't eyeball.** Run the bundled `scripts/forensics.py` (in
Claude Code: `python3 ${CLAUDE_SKILL_DIR}/scripts/forensics.py <input.json>`; feed the figures as
JSON, `--schema` prints the input shape) to get M-Score, Altman Z/Z'', Benford, and ratios in one
pass, then interpret. State assumptions and limits — these are indicators, not verdicts:

- **Beneish M-Score** — likelihood of earnings manipulation from 8 ratios (DSRI, GMI, AQI, SGI,
  DEPI, SGAI, LVGI, TATA). Above ≈ −1.78 warrants scrutiny.
- **Altman Z-Score** — distress/bankruptcy risk. Low scores flag solvency pressure (a motive).
- **Benford's Law** — first-digit distribution of a large figure set; deviation flags possible
  fabrication or rounding. Only valid on suitably large, naturally-occurring datasets — say so.
- **Accrual quality / Sloan** — high accruals vs. cash earnings signal low earnings quality.

**Revenue-recognition red flags:** channel stuffing, bill-and-hold, round-tripping, premature or
grossed-up revenue, growing receivables/DSO outpacing sales, big Q4 or quarter-end spikes.

**Balance-sheet & disclosure flags:** related-party transactions doing heavy lifting; goodwill that
never impairs; frequent auditor or CFO changes; restatements; late filings; off-balance-sheet
vehicles; complex structure with no business rationale.

## C. Fraud typologies (know the shape you're hunting)

- **Financial-statement fraud** — cook earnings/assets (above).
- **Asset misappropriation** — skimming, fake vendors, payroll ghosts, expense abuse.
- **Ponzi/affinity** — returns paid from new inflows; consistent above-market returns; opacity;
  pressure to reinvest; unregistered operators.
- **Procurement/kickback** — bid rigging, split purchases, vendor-employee collusion.
- **Trade-based money laundering** — over/under-invoicing, phantom shipments, circular trade.

For any fraud judgment, run **ACH**: the innocent explanation (bad luck, aggressive-but-legal
accounting, error) is a required competing hypothesis. Fraud requires opportunity + motive +
rationalization *and* evidence — not just a suspicious pattern.

## D. Deliverable block ("Financial Forensics")

In PART II, include: the ownership/control map; the ratio/model table with computed values and what
each indicates; red flags found (each confidence-graded and sourced); the fraud hypotheses tested via
ACH; and — non-negotiable — the data you *couldn't* get (ledgers, bank records, private filings) as
Collection Gaps. Screening-model outputs are **indicators that direct further collection**, never a
standalone accusation.
