# UNIPEN Conventions

The cross-cutting rules every document UNIPEN produces must follow, regardless of doc type.
These are UNIPEN's own doctrine — self-contained, nothing here depends on any other skill.

## Trust ladder

Every file's frontmatter carries a `trust` value. This is the single most load-bearing piece of
metadata in the whole tree — it's how a reader or an agent knows how much to lean on a claim
without re-verifying it themselves.

| State | Meaning |
|---|---|
| `VERIFIED` | Confirmed against source, citations present |
| `PARTIAL` | Some claims cited; gaps named in a `## Gaps` section |
| `DRAFT` | Authored from inference, not source-confirmed |
| `RESERVED` | Empty placeholder for a later pass — must exist as a real (if empty) file, never a dangling link target |

Never assign `VERIFIED` to a file with an unresolved `## Gaps` section — that's a contradiction
in terms. If you're not sure a claim is right, the file is `PARTIAL` or `DRAFT`, not `VERIFIED`.

## Tiering

Every file's frontmatter also carries a `tier`, which sets the trust bar it must clear:

- **Tier 1** — the reader is harmed if this is wrong or missing (e.g. a runbook step, an auth
  flow, a data-retention rule). Must reach `VERIFIED` before the tree is considered done for
  that file.
- **Tier 2** — the reader is slowed if wrong or missing (most architecture/module docs).
  `VERIFIED` or `PARTIAL` is acceptable.
- **Tier 3** — nice to have (e.g. a roadmap, a deep-dive on a minor subsystem). Any trust state
  is acceptable, including `DRAFT`.

Tier is about consequence of being wrong, not about how interesting or central the topic is.

## Citation rule

Every behavioral claim — anything that describes what the code *does*, not what it's *supposed*
to do — cites `path/to/file:line` or a specific config path. If you can't point at the line,
the claim goes in `## Gaps` or gets left out. Never invent a citation, filename, version, or
owner to make a file look more complete than the collection actually supports.

The operator telling you something directly in the current conversation **is** a real source —
the rule against invention is about fabricating a citation, not about refusing one you were
actually just given. Cite it as such (e.g. *"per operator, 2026-07-22"*) and mark the file
`PARTIAL` rather than `VERIFIED`, since it hasn't been independently confirmed against the code
or a commit/PR yet. This matters most for Release Notes and Changelog entries, which are often
written from what the operator just told you happened, not from a fresh code read.

## Frontmatter — every file, no exceptions

```yaml
---
tier: 1
trust: VERIFIED
owner: <name>
last_verified: YYYY-MM-DD
---
```

This applies to every file in the tree, including `RESERVED` stubs (their `trust` is literally
`RESERVED`, but the four fields are still present).

## Breadcrumb — every file, first line of body

Below the frontmatter, above the H1: full-path Obsidian wikilinks, one per ancestor, plain text
for the current file (the current file never links to itself, since that's a self-loop with no
navigational value):

```markdown
[[Kalbe-SCM/00-MAP|SCM Digital Twin]] / [[Kalbe-SCM/02-Technical/00-Index|Technical]] / [[Kalbe-SCM/02-Technical/TD-01-Architecture/00-Overview|Architecture]] / System Architecture
```

The breadcrumb is what lets a reader (human or agent) land on any file with zero prior context
and immediately know where it sits in the tree.

## Index files — one extra requirement

Every `00-Index.md` (one per folder level) additionally carries a summary table, so an agent
that reads that one file knows the state of the whole folder without opening every child:

```markdown
| File | Tier | Trust | Owner |
|---|---|---|---|
| 01-System-Architecture | T1 | VERIFIED | Gunawan |
| 02-Connections | T1 | PARTIAL | Gunawan |
```

## Wikilink rules — hard constraints

- **Full path only, never short-form.** Write `[[Kalbe-SCM/02-Technical/00-Index]]`, never
  `[[00-Index]]`. Every project repeats filenames like `00-Overview` and `00-Index` at every
  folder level — a short-form link is ambiguous the moment more than one exists, which is
  always.
- **No node ever points outside its own project folder.** GDS trees are fully self-contained:
  zero cross-project links, zero shared layer, even across projects that share stack, org, or
  contributors. A link that reaches outside `{{PROJECT}}/` is a bug.
- **No node ever points to a nonexistent file.** If a section is deferred, create the
  `RESERVED` stub first (frontmatter + breadcrumb + `trust: RESERVED`, empty or one-line body)
  — then link to it. A link to nothing is worse than a `RESERVED` stub, because it silently
  breaks navigation instead of honestly saying "not written yet."

## "Elevate and link, never duplicate"

If content already has a canonical home elsewhere in the same project tree, link to it instead
of forking a second copy. This is why the folder structure has no separate Migration-Guides
folder (migration content lives inside each version's release folder instead), and why
`CD-06-Versioning-Policy.md` links to the deprecation timeline rather than restating it. Every
duplicated paragraph is a future place the tree can silently disagree with itself.

## Diagram governance

All diagrams are hand-authored and verified against source — never auto-generated from a live
pipeline, even where the source is technically machine-readable (e.g. a Supabase schema). A
diagram starts as a first draft (`trust: DRAFT`), gets checked against the actual source, and is
then promoted to `VERIFIED`. See `diagram-catalog.md` for which Mermaid syntax to use where.

## Human-only content and unconfirmable claims

Some content genuinely cannot be sourced from the codebase — who owns escalation, tenant-specific
business rules, historical context. Scaffold these sections with explicit questions for the
project owner, mark them `PARTIAL`, and never fabricate a plausible-sounding answer. If a claim
elsewhere can't be confirmed by any available source, write it as
`UNVERIFIABLE — <what's missing>. Confirm or abort.` rather than guessing — the pull to fill in
a reasonable-sounding detail is exactly the moment to write this line instead.
