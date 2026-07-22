# UNIPEN Diagram Catalog

Every diagram in a GDS tree is **hand-authored and verified against source** — never generated
from a live pipeline, even when the source is technically machine-readable (e.g. a Supabase
schema or an OpenAPI spec). Draft it, check it against the real code/config, then promote its
`trust` to `VERIFIED`. Use this table to pick the right Mermaid syntax for what you're drawing.

| Diagram | Mermaid syntax | Used in |
|---|---|---|
| System context / use case | `flowchart` styled with actor nodes + boundary subgraphs | Onboarding orientation, module interfaces |
| Class diagram | `classDiagram` | Modules — **optional, ask before including per module** |
| Sequence | `sequenceDiagram` | Data flow, module communication, per-endpoint request lifecycle |
| Activity / data flow | `flowchart` or `stateDiagram-v2` | Data flow, business process topology |
| Architecture (C4-style) | `flowchart` with styled subgraphs for Context/Container/Component | Technical → Architecture |
| ERD | `erDiagram` | Technical → Data → Data Model |
| Release timeline | `timeline` or `gitGraph` | Release Notes |

## The "use case diagram" caveat — document this wherever it applies

Mermaid has no native UML "use case diagram" syntax. Whenever a GDS tree needs a "Use Case"
diagram (typically `01-System-Context.md` under Onboarding), render it as a `flowchart`
approximation instead: actor shapes on the boundary, a subgraph for the system, edges for each
use case. **Note this explicitly in the file** — a one-line caveat like *"rendered as a flowchart
approximation; Mermaid has no native UML use-case syntax"* — so nobody reading it expects a
textbook UML diagram and wonders why it looks different from one.

## Class diagrams are opt-in

Unlike the other rows, a per-module class diagram is **not** default behavior. Ask the project
owner before including one for a given module — some modules don't have a class structure
worth diagramming (e.g. a thin functional wrapper), and a class diagram nobody asked for is
just another file that can drift from the code.

## Worked example — architecture flowchart with C4-style subgraphs

```text
flowchart TD
  subgraph Context[System Context]
    USER[End User] --> APP
    APP[This System]
  end
  subgraph Container[Containers]
    API[API Container]
    DB[(Database)]
    APP --> API --> DB
  end
  subgraph Component[Components — API Container]
    ROUTER[Router]
    SVC[Service Layer]
    API --> ROUTER --> SVC --> DB
  end
```

## Worked example — use-case flowchart approximation (with the caveat)

```text
%% Rendered as a flowchart approximation — Mermaid has no native UML use-case syntax.
flowchart LR
  ACTOR((Intern)) --> UC1[Clone the repo]
  ACTOR --> UC2[Run local environment]
  ACTOR --> UC3[Make first contribution]
  subgraph Boundary[This Project]
    UC1
    UC2
    UC3
  end
```
