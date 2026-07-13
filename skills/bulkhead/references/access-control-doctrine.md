# Access-Control Doctrine (BULKHEAD)

The reference models BULKHEAD designs from. These are **real, published standards** — cite them, don't
invent them. The through-line from intelligence-agency practice: access is never granted by rank
alone; it takes **clearance** (are you vetted to this level?) **and** **need-to-know** (do you require
*this* compartment for your task?). Software authorization is the same two-gate idea.

## 1. The two gates — clearance × need-to-know

- **Classification / sensitivity tiers** — label every asset by the damage its disclosure or
  corruption would cause (e.g. public / internal / confidential / restricted). This is the lattice
  access is granted against.
- **Clearance (level)** — the highest tier a subject is *vetted* to reach.
- **Need-to-know (compartment)** — access requires a task-based reason for *this specific* data, even
  at or below one's clearance. Clearance without need-to-know is not access.
- **Compartmentation / caveats** — orthogonal need-to-know groupings (like SCI compartments) that cut
  across levels. The bulkhead: a breach in one compartment does not flood the rest.

## 2. Principles (Saltzer & Schroeder, 1975; still the canon)

- **Least privilege** — the minimum rights to do the job, no more; the default posture.
- **Fail-safe defaults / deny-by-default** — absence of explicit permission is denial.
- **Complete mediation** — every access is checked, every time; no cached bypass.
- **Economy of mechanism** — keep the authorization logic small enough to audit.
- **Separation of privilege / separation of duties (SoD)** — no single subject can complete a
  sensitive action alone; split it (static SoD = mutually exclusive roles; dynamic SoD = not in the
  same session/transaction).
- **Auditability** — every grant and use is logged and reviewable.

## 3. Access-control models (choose and combine deliberately)

- **RBAC** (NIST / INCITS 359) — permissions attach to **roles**, subjects hold roles; add **sessions**
  and **constraints**. Levels: RBAC0 (flat), RBAC1 (+ **role hierarchy** — a senior role *inherits* the
  permissions of the junior roles beneath it: "roles passed down"), RBAC2 (+ constraints/SoD), RBAC3
  (both). The workhorse for most systems.
- **ABAC** (NIST SP 800-162) — decisions from **attributes** of subject, resource, action, and
  environment via policy. More expressive and dynamic than RBAC; harder to audit. Often RBAC for the
  coarse grant + ABAC for fine, contextual conditions.
- **MAC vs. DAC** — Mandatory (a central policy/label decides; the owner cannot override — the
  clearance model) vs. Discretionary (the resource owner grants at will). Agencies lean MAC for
  classified data; most apps are DAC with RBAC on top.

## 4. Formal models (when confidentiality or integrity must be provable)

- **Bell-LaPadula** (confidentiality) — *no read up, no write down* (the ★-property). Stops leakage
  from high to low.
- **Biba** (integrity, the dual) — *no read down, no write up*. Stops low-integrity data corrupting
  high-integrity.
- **Clark-Wilson** (commercial integrity) — access only through **well-formed transactions** on
  certified data items, with enforced **separation of duties**.
- **Brewer-Nash (Chinese Wall)** — dynamic conflict-of-interest walls (access to one client's data
  bars access to a competitor's). Useful for advisory/audit firms.

## 5. Common failure modes (design against these)

- **Role explosion** — a role per user; collapses RBAC's benefit. Design roles around *duties*, not
  people.
- **Privilege creep** — roles accrete and never shed permissions; schedule recertification.
- **Confused deputy / over-broad service accounts** — a component acting with more authority than the
  caller. Scope tokens; pass the caller's authority, not the service's.
- **Missing SoD** — the same subject requests *and* approves. Split it.
- **Implicit allow** — anything not explicitly denied is permitted. Invert to deny-by-default.
