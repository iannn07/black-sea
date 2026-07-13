# Security Policy

## Reporting a vulnerability

Please report security issues **privately** through GitHub Security Advisories:

- Open the repository's **Security** tab → **Report a vulnerability**
  (<https://github.com/iannn07/black-sea/security/advisories/new>).

Do **not** open a public issue for a vulnerability. We aim to acknowledge a report within a few days
and will coordinate a fix and a disclosure timeline with you.

## Supported versions

BLACK SEA is a single skill released from `main`. Fixes land on the latest released version; there is
no long-term-support branch.

| Version | Supported |
| --- | --- |
| 2.2.x | ✅ |
| < 2.2 | ❌ (upgrade to latest) |

## Security posture of the skill

BLACK SEA is an investigative-analyst skill, so its threat surface is unusual — worth stating plainly:

- **The forensics calculator runs locally, offline.** `skills/black-sea/scripts/forensics.py` is
  Python standard library only: no third-party packages, no network calls. It reads the figures you
  give it and writes results to stdout. Inspect it before running — it is short and dependency-free.
- **Collection is open-source and lawful by design.** The skill does not crawl the dark web, ingest
  stolen or breached data contents, or perform any collection that would require pretexting,
  unauthorized access, or breaking a terms-of-service. Breach *exposure* is flagged only via
  legitimate breach-notification services — the fact of exposure, never the stolen contents.
- **No secrets in the repo.** The skill needs no API keys to function. Obsidian delivery uses an
  `mcp-obsidian` server you configure locally; keep your Obsidian API key in your own environment, not
  in this repository.
- **Untrusted input is data, not instructions.** The skill treats collected material (web pages,
  documents, filings) as evidence to analyze, never as commands to follow.

## Scope

This policy covers the code and skill definitions in this repository. It does not cover the security of
third-party tools you install alongside it (Claude Code, `mcp-obsidian`, the `npx skills` installer) —
report issues in those to their own maintainers.
