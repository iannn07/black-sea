# UNIPEN Folder Structure

The canonical GDS tree. Reproduce this exactly — the shapes below (which folders exist, which
files are single-file-always, which branches are conditional) are fixed by the standard, not a
judgment call per project.

```text
{{PROJECT}}/
├── 00-MAP.md
├── 00-README.md
├── 00-GLOSSARY.md
├── 99-Audit-Log.md
│
├── 01-Onboarding/
│   ├── 00-Index.md
│   ├── OB-01-Orientation/
│   │   ├── 00-Overview.md
│   │   ├── 01-System-Context.md
│   │   └── 02-Actors-and-Roles.md
│   ├── OB-02-Environment-Setup/
│   │   ├── 00-Prerequisites.md
│   │   ├── 01-Access-and-Credentials.md
│   │   ├── 02-Local-Environment.md
│   │   └── 03-Verify-Your-Setup.md
│   ├── OB-03-First-Contribution/
│   │   ├── 00-Overview.md
│   │   ├── 01-Guided-Walkthrough.md
│   │   └── 02-Where-To-Go-Next.md
│   ├── OB-04-Role-Based-Paths/
│   │   ├── 00-Index.md
│   │   ├── 01-Intern-Path.md
│   │   ├── 02-Junior-Dev-Path.md
│   │   ├── 03-Successor-Path.md
│   │   └── 04-Mentor-Reviewer-Path.md
│   └── OB-05-Ownership-and-Escalation.md
│
├── 02-Technical/
│   ├── 00-Index.md
│   ├── TD-01-Architecture/
│   │   ├── 00-Overview.md
│   │   ├── 01-System-Architecture.md
│   │   ├── 02-Connections.md
│   │   ├── 03-Business-Process-Topology.md
│   │   └── 04-Deployment.md
│   ├── TD-02-Data/
│   │   ├── 00-Overview.md
│   │   ├── 01-Data-Flow.md
│   │   ├── 02-Data-Model.md
│   │   ├── 03-Data-Lifecycle-and-Retention.md
│   │   └── 04-Data-Contracts.md
│   ├── TD-03-Modules/
│   │   ├── 00-Module-Index.md
│   │   └── NN-<Module-Name>/              (EVERY module gets a folder — no exceptions)
│   │       ├── 00-Overview.md
│   │       ├── 01-Architecture.md
│   │       ├── 02-Data-Flow.md
│   │       ├── 03-Interfaces.md            (cross-links into 04-Code-Documentation)
│   │       ├── 04-Gotchas.md               (cross-links into TD-06 register entries)
│   │       └── 05-Release-Status.md
│   ├── TD-04-Decisions/
│   │   ├── 00-Index.md
│   │   └── NN-<slug>.md                    (single file by default — see document-contracts.md)
│   │       └── NN-<slug>/                  (folder ONLY if real supporting artifacts exist)
│   ├── TD-05-Multi-Tenancy/
│   │   ├── 00-Overview.md
│   │   └── NN-<Tenant-or-Aspect>.md
│   ├── TD-06-Limitations-and-Gaps/
│   │   └── 00-Register.md
│   └── TD-07-Runbooks/
│       ├── 00-Index.md
│       └── NN-<Runbook-Name>.md            (ALWAYS single file — no exceptions, 2am-readability)
│
├── 03-Release-Notes/
│   ├── 00-Index.md
│   ├── RN-01-Changelog/
│   │   └── CHANGELOG.md                    (cumulative, Keep a Changelog format)
│   ├── RN-02-Releases/
│   │   └── <version>/                      (folder per version)
│   │       ├── 00-Release-Notes.md         (audience-facing, derived from changelog)
│   │       └── 01-Migration-Guide.md       (only if this version has breaking changes)
│   └── RN-03-Deprecation-and-Roadmap/
│       ├── 00-Deprecation-Timeline.md      (links into each version's migration guide — never duplicates it)
│       └── 01-Roadmap.md                   (RESERVED)
│
└── 04-Code-Documentation/
    ├── 00-Index.md
    ├── CD-01-REST-API/                     (only if this project has a REST surface)
    │   ├── 00-Overview.md
    │   └── NN-<Resource>.md                (generated from OpenAPI)
    ├── CD-02-RPC-Reference/                (only if this project has RPCs, e.g. Supabase)
    │   ├── 00-Overview.md
    │   └── NN-<Domain>.md                  (generated from SQL function signatures)
    ├── CD-03-Flow-Reference/               (only if this project has Power Automate flows)
    │   ├── 00-Overview.md
    │   └── NN-<Flow-Group>.md              (generated from exported flow JSON)
    ├── CD-04-Auth-and-Errors/
    │   ├── 00-Authentication.md
    │   ├── 01-Error-Code-Reference.md
    │   └── 02-Rate-Limits-and-Quotas.md
    ├── CD-05-Integration-Guides/
    │   ├── 00-Quickstart-First-Call.md     (Stripe/Twilio pattern — task-based, not endpoint-by-endpoint)
    │   └── NN-<Common-Scenario>.md
    └── CD-06-Versioning-Policy.md          (links to RN-03 timeline — never duplicates it)
```

**Canonical home for versioning/deprecation content:** `RN-03-Deprecation-and-Roadmap/
00-Deprecation-Timeline.md` is the one place the actual deprecation/versioning narrative and
dates live. `CD-06-Versioning-Policy.md` states the *policy* (the rules of how versioning and
deprecation work in general) and links to the timeline for the *specifics* — it never restates
which versions are deprecated or when. If you're ever unsure which of the two files a fact
belongs in, ask "is this a rule, or an instance of a rule being applied?" — rules go in
`CD-06`, instances go in `RN-03`.

## Depth rules — apply when scaffolding any project

- **Modules (`TD-03`):** every module gets a folder. No judgment call, no exceptions — this is
  what keeps module docs navigable as the project grows past a handful of modules.
- **Decisions (`TD-04`):** single file per decision by default. This is the entire point of the
  ADR format (Nygard/MADR are deliberately one-to-two pages) — promote to a folder only when a
  decision has real supporting artifacts (a comparison table, a benchmark), never just for
  consistency with how Modules are folders.
- **Runbooks (`TD-07`):** always single file, no exceptions, ever. A runbook's entire value is
  being scannable in one place during an incident — splitting it across files defeats that.
- **Code Documentation (`CD-01`/`02`/`03`):** branch by interface type. Only create the branches
  that actually apply to this project — a pure-REST project has no `CD-02-RPC-Reference/` or
  `CD-03-Flow-Reference/` folder at all, not an empty one. If a project has none of the three
  (e.g. a pure library with no network surface), note why in `04-Code-Documentation/00-Index.md`
  rather than forcing a branch that doesn't fit.
- **Multi-Tenancy (`TD-05`):** unlike `CD-01`/`02`/`03`, this folder is **not conditional** —
  every project gets it, even a single-tenant one. For a single-tenant project, `00-Overview.md`
  simply states that plainly ("this project is single-tenant; there is no per-tenant variation")
  and no `NN-<Tenant-or-Aspect>.md` files are needed. That's a complete, `VERIFIED` answer, not
  an open gap — don't leave it dangling as an unanswered human-only question just because the
  answer is "not applicable."
- **Release Notes (`RN-02`):** folder per version, bundling that version's release notes and (if
  applicable) its migration guide together. There is no separate top-level Migration-Guides
  folder — that content lives inside the version folder it belongs to, per the "elevate and
  link, never duplicate" rule in `conventions.md`. Whether a version "has breaking changes" is a
  fact to confirm, not a number to infer — ask the operator or check the actual diff (API
  surface removed/changed incompatibly, a schema migration that isn't backward-compatible,
  etc.). A SemVer major-vs-minor bump is a useful first signal but not sufficient on its own:
  plenty of real-world minor bumps sneak in a breaking change, and plenty of majors are bumped
  for unrelated reasons. If you can't confirm either way, include the migration guide as
  `PARTIAL` with the open question named, rather than silently omitting it.

## ID scheme

Type-prefixed: `OB-`, `TD-`, `RN-`, `CD-`, each independently numbered within its own type. Not
one continuous register across all four — `OB-03` and `TD-03` are unrelated numbers that happen
to share a value.

## Scope

Every project gets its own fully independent tree. No shared vault-level layer, no
cross-project glossary or ADR pool, no links crossing project boundaries — even when several
projects share stack, org, or contributors. See the wikilink rules in `conventions.md` for the
hard constraint this implies.
