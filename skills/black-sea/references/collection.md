# Collection

How BLACK SEA collects: aggressive, all-source, and lawful. Work provided material first, then fill
gaps from the open web. Log every source with an Admiralty grade as you collect — never reconstruct
sourcing afterward.

## Collection priority order

1. **Material the user provided** — filings, financials, data dumps, documents, images. Highest
   signal, lowest cost, and the metadata alone often breaks a case. Exhaust it before going wide.
2. **Primary public records** — official registries and filings beat any secondary summary.
3. **Secondary/open web** — news, industry data, aggregators. Corroborate, don't lead with these.

## Deep public source map (by category)

- **Corporate & ownership:** company registries (jurisdiction-specific), beneficial-ownership
  registers, filing/annual-report databases, securities regulators' EDGAR-style systems.
- **Legal:** court dockets and judgments, bankruptcy filings, liens/UCC, litigation databases.
- **Regulatory & compliance:** sanctions lists, PEP lists, debarment/exclusion lists, licensing
  boards, procurement/tender portals, import/export records where public.
- **IP & innovation:** patent and trademark offices, standards bodies, grant databases.
- **Financial:** disclosures, credit-rating actions, short-seller reports (treat as advocacy —
  grade accordingly), earnings transcripts.
- **Web infrastructure:** WHOIS/domain history, DNS, certificate transparency logs, archived
  snapshots — all legitimate and public.

Name the specific source class you'd query per finding. If you can't reach it live, that's a
Collection Gap with a named next step — not a place to guess.

## Document forensics (run on every provided file)

- **PDF:** producer/creator metadata, creation vs. modification dates, embedded fonts, incremental
  save/revision history, embedded objects/attachments, redaction that's really just a black box over
  live text. Mismatched producer or impossible dates are a finding.
- **Office docs:** author/last-modified-by, revision count, template origin, tracked-change remnants.
- **Cross-document:** consistent metadata across a "spontaneous" document set suggests a single
  origin/manufacture.

## Image forensics

- **EXIF/XMP:** camera/device, timestamps, GPS coordinates, editing-software fingerprints.
- **Geolocation:** shadows, signage, architecture, vegetation, licence-plate formats to place an
  image; corroborate against maps/imagery.
- **Reverse image search:** find earlier appearances (a "new" photo that's years old is a finding).
- **Manipulation signals:** error-level anomalies, cloning artifacts, inconsistent lighting.

## Link analysis & entity resolution

- **Resolve entities** before connecting them: is "J. Smith", "John Smith", and "Smith Holdings LLC"
  one node or three? Use identifiers (registration numbers, addresses, DOB where lawful) not just names.
- **Map relationships:** shared officers, addresses, phones, IPs, registration agents, funding flows.
- **Pattern flags:** circular ownership, mass-registration agents, addresses hosting hundreds of
  entities, directors appointed/resigned in suspicious clusters — classic shell-network signals.

## Breach *exposure* flagging (the lawful substitute for "dark web")

Legitimate breach-notification services report *whether* an email/domain **appears** in known-breach
corpora. Use that signal — the **fact of exposure and its scale** — as a security/exposure indicator
in Annex D.

- **Do:** note that a domain surfaces in N known breaches; read it as a credential-hygiene / attack-
  surface signal.
- **Do NOT:** retrieve, ingest, quote, or republish the leaked contents; and never compile leaked
  personal data into a profile of an individual. That's the boundary in SKILL.md — honor it.

## Hard boundaries (repeat, because they're load-bearing)

- No dark-web/Tor-market crawling. You can't reach it; claiming results would be fabrication.
- No stolen/leaked data ingestion; no PII dossiers on private individuals from breach data.
- No pretexting, impersonation, unauthorized access, or ToS/law-breaking collection. If a fact needs
  that to obtain, it is a **gap**, not a task.

When blocked, write the gap and the lawful next step (a subpoena-only record, a paywalled registry,
an in-person filing). Naming the gap is the professional move.
