# Contributing to BLACK SEA

Thanks for helping sharpen the unit. BLACK SEA is one skill — an all-source investigative analyst that
produces confidence-graded dossiers — and every contribution has to keep the discipline that makes its
output trustworthy. Read this before opening a PR.

## The compliance guard (non-negotiable)

Any change must keep all of these. A PR that weakens one will be asked to revise.

1. **The Prime Directive holds.** Never fabricate. Every finding the skill emits must trace to a real
   source or be labeled ASSESSMENT / ASSUMPTION; anything unobtainable is a named **gap**. Do not add
   behaviour that invents sources, figures, quotes, records, or URLs, or that reconstructs sourcing
   from memory as if it were collected.
2. **The collection boundaries stay.** Open-source and clean only. No dark-web / stolen-data
   ingestion, no PII dossiers on private individuals, nothing that requires pretexting, unauthorized
   access, or breaking a law or a terms-of-service. New collection guidance names the lawful source or
   it is a gap, not a task.
3. **New leading words are defined before use.** If you introduce a term of art, add it to both
   `CONTEXT.md` and `skills/black-sea/references/glossary.md`. Consistent language is what keeps runs
   predictable — an undefined word is a silent behaviour change.
4. **Every workflow step ends on a checkable `Done when`.** If you add or change a step in `SKILL.md`,
   give it a criterion a reader can verify (exhaustive on the collect and analyze steps).
5. **`SKILL.md` stays under ~500 lines.** Push detail into `references/` behind a context pointer; the
   spine routes, the references carry the depth.

## Repository layout

```text
skills/black-sea/
  SKILL.md              # the spine (routing, tiers, workflow, dossier template, failure modes)
  references/           # lane files + shared cores (collection, analytic-tradecraft, ...)
  scripts/forensics.py  # financial-forensics calculator — Python standard library only, no network
docs/black-sea.md       # human-facing overview
CONTEXT.md              # the ubiquitous language
CLAUDE.md · AGENTS.md   # agent instructions
```

## Editing the skill

- **Match the surrounding discipline.** Read `skills/black-sea/references/glossary.md` and
  `analytic-tradecraft.md` before changing behaviour, and use the leading words exactly.
- **`forensics.py` is standard-library only.** No third-party packages, no network calls. It computes
  indicators that *direct collection*, never verdicts — keep that framing in any new metric. Run the
  self-test before and after a change:

  ```bash
  python3 skills/black-sea/scripts/forensics.py --demo
  python3 skills/black-sea/scripts/forensics.py --schema
  ```

- **Keep the three tiers of claim honest.** FACT / ASSESSMENT / ASSUMPTION are never blurred;
  likelihood (odds) and confidence (how sure) stay separate axes.

## Versioning & changelog (changesets)

This repo versions with [changesets](https://github.com/changesets/changesets).

1. Make your change.
2. Add a changeset describing it: `npx changeset` — pick `patch` / `minor` / `major` and write the
   entry in plain language (what changed and why, from the reader's point of view).
3. When cutting a release, `npx changeset version` folds pending entries into `CHANGELOG.md` and bumps
   `package.json`. Keep the version in lockstep across `package.json`, `.claude-plugin/plugin.json`,
   and `.claude-plugin/marketplace.json`.

`major` = a breaking change to how the skill is invoked or behaves; `minor` = new capability;
`patch` = a fix or a docs sharpening.

## Pull requests

Use the PR template. Before requesting review, confirm:

- [ ] The compliance guard above still holds.
- [ ] New leading words are in `CONTEXT.md` and the glossary.
- [ ] Changed `SKILL.md` steps keep a checkable `Done when`; the file is under ~500 lines.
- [ ] `forensics.py` still passes `--demo` (if touched).
- [ ] A changeset is included; the docs page is re-synced if behaviour changed.

## Protected source-of-truth

BLACK SEA delivers into an operator's Obsidian vault. When working there, three things are
**propose-only** — never self-applied: the guard-rail `Private/Black Sea/00-BLACK-SEA.md`, the
NIGHTSTALKER §10 registry, and any `99-Audit-Log.md` row (append-only, immutable).

## Code of conduct

Participation is governed by our [Code of Conduct](./CODE_OF_CONDUCT.md).
