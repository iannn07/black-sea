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
