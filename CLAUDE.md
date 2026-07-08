# CLAUDE.md — BLACK SEA repo

This repository ships one skill: **BLACK SEA** (Special Investigation Unit / CID), an all-source
investigative analyst that produces standardized, confidence-graded intelligence dossiers on
organizations and people.

- The skill lives at `skills/black-sea/` (`SKILL.md` + `references/` + `scripts/`).
- It is **model-invoked** (fires on investigation intent or the callsign "Black Sea") and acts as the
  router for a case; lanes and delivery are branches reached by context pointers into `references/`.
- Default dossier delivery is the operator's Obsidian vault at `Private/Black Sea/[CODENAME]/`,
  compliant with the vault standard and the NIGHTSTALKER / DAGGER ONE protocols.
- The **Prime Directive** governs everything: never fabricate. Findings trace to real sources or are
  labeled assessment/assumption; anything unobtainable is a named *gap*.

When editing the skill, follow the discipline in `skills/black-sea/references/glossary.md` (leading
words) and keep each workflow step's **Done when** criterion checkable and, where marked, exhaustive.

## Repository structure & conventions

Single-skill repo (not a multi-skill monorepo). Layout:

```
skills/black-sea/
  SKILL.md              # the spine — under ~500 lines
  references/           # lane files + shared cores, reached by context pointers
  scripts/forensics.py  # financial-forensics calculator (stdlib only, no network)
docs/black-sea.md       # human-facing overview page
.changeset/             # changesets versioning (config + pending entries)
CLAUDE.md · AGENTS.md   # agent instructions (this file is the fuller copy)
CONTEXT.md              # the ubiquitous language (leading words, entities)
CONTRIBUTING.md         # the compliance guard + edit/versioning workflow
CHANGELOG.md            # changesets-format history
SECURITY.md · CODE_OF_CONDUCT.md · CITATION.cff · LICENSE · .editorconfig
.github/                # issue + PR templates
```

Conventions:

- **One skill, no buckets.** This is a single-skill repo, so there is no `engineering/` /
  `productivity/` bucketing and no `.agents/` tree — agent conventions live in `CLAUDE.md` +
  `AGENTS.md`.
- **Ubiquitous language.** Leading words are defined in `CONTEXT.md` and mirrored in
  `skills/black-sea/references/glossary.md`; define a new one in both before using it.
- **Versioning via changesets.** For any skill change, run `npx changeset` to add an entry, then
  `npx changeset version` to fold it into `CHANGELOG.md` and bump `package.json`. Keep the version in
  `package.json`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` in lockstep.
- **Docs page.** A human-facing overview lives at `docs/black-sea.md`; re-sync it when the skill's
  behaviour changes.
- **Protected source-of-truth (Obsidian vault).** The guard-rail `Private/Black Sea/00-BLACK-SEA.md`,
  the NIGHTSTALKER §10 registry, and any `99-Audit-Log.md` row are propose-only — never self-applied.
