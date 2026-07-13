# Link / Entity / Network Analysis (GRASSHOPPER)

How BLACK SEA resolves entities and maps the graph they sit in. Anomalies live at **the seam** —
shared officers, addresses, phones, registration agents, impossible timelines — so the network is
often where a case breaks. Pair with `collection.md`, `analytic-tradecraft.md`, and (for ownership
graphs) `org-financial.md`.

## 1. Resolve entities before you connect them

The cardinal error is merging two people (or splitting one) on a name match. Resolve on
**identifiers**, not names:

- Registration/company numbers, tax IDs, addresses, DOB (where lawful), domains, phone/email.
- Is "J. Smith", "John Smith", and "Smith Holdings LLC" one node or three? State your **identity
  confidence** for each merge, and never fold two records together on a name alone.
- Normalise before matching: transliteration variants, corporate suffixes (Ltd/LLC/GmbH), address
  formatting, maiden/married names.

## 2. Map the relationships (edge types)

Build the graph from edges you can source:

- **People ↔ entities:** officer, director, shareholder, registered agent, beneficial owner.
- **Entity ↔ entity:** parent/subsidiary, shared address, shared phone/IP/domain registrant, funding
  flow, contract/procurement award.
- **Shared attributes:** the same address, agent, or phone across entities is an edge — often the
  most revealing one.

Grade each edge like any source (Admiralty); an edge asserted by one aggregator is **cold** until a
second independent origin confirms it.

## 3. Read the structure

- **Hubs** — a node with many edges (a registered agent, a nominee director) may be infrastructure,
  not a principal. Say which.
- **Brokers** — a node connecting otherwise-separate clusters is high-value; it's where control or
  money crosses.
- **Clusters** — tightly-linked groups that should be independent but aren't.

## 4. Shell-network signals (the seam)

- Circular or layered ownership; entities owning each other through a ring.
- Mass-registration agent addresses; a single address hosting hundreds of entities.
- Directors appointed then resigned in suspicious clusters; dormant entities that suddenly transact.
- Name near-collisions with reputable firms; reused phones/emails/domains across a "diverse" set.

## 5. Render it (required)

Render the link network as a **Mermaid `flowchart`** and any sequence as a **Mermaid `timeline`** —
never ASCII; it renders in the dossier and is required by the Obsidian vault standard.

```text
flowchart LR
  P1[John Smith] -->|director| E1[Acme Ltd]
  P1 -->|director| E2[Beta Holdings]
  E2 -->|shares 62%| E1
  E1 -->|reg. address| A1((Suite 400 — 380 entities))
```

## Deliverable (GRASSHOPPER findings packet, "Link Analysis" block)

Return per the operative contract: the resolved **entity register** (identifiers, role, connections)
with identity-confidence; the **Mermaid** network and timeline; the seam findings (each
confidence-graded and sourced); and named **gaps** where an edge could not be independently
corroborated (stays **cold**).
