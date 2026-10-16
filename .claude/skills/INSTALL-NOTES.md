# claude-seo — what is installed here, and what is not

Source: [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo)
**v2.4.2**, MIT. Installed 16 October 2026.

## Installed

- **33 skills** under `.claude/skills/` — `seo` (hub) plus 32 leaves, including the
  nine extension skills (ahrefs, bing, dataforseo, firecrawl, matomo, profound,
  seranking, unlighthouse, image-gen).
- **19 subagents** under `.claude/agents/`.
- Markdown, reference material, templates and JSON only. **1.6 MB.**

Installed **into the repository**, not `~/.claude/`. The upstream `install.sh`
writes to `$HOME`, and this is an ephemeral cloud container — a `$HOME` install
is gone when the session ends. In the repo it is committed, version-controlled
and available to every future session.

`${CLAUDE_PLUGIN_ROOT}/skills/` was rewritten to `.claude/skills/` in 15 files so
cross-references resolve from the repository root in any checkout.

## NOT installed, deliberately

**The ~80 bundled Python scripts, the hooks, and the `seo-cockpit` plugin.**

There are **200 references across 45 script names** in the installed markdown —
lines of the form `"${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo" run <script>.py`.
**Those will not resolve.** That is expected, not a broken install. Two reasons:

1. **They cannot reach the store from this container.** The session egress proxy
   answers 403 to `malnadproducts.in` and to `google.com` — established during
   the Magic Checkout work and recorded in `CLAUDE.md`. So `fetch_page`,
   `render_page`, `pagespeed_check`, `capture_screenshot`, `gsc_query`,
   `ga4_report` and every other live-URL tool is dead weight here.
2. **The Shopify Admin API is the better source anyway.** This project already
   reads and writes the store directly — that is how all 68 SEO records were
   pushed. Going through an HTML fetcher to learn something the API states
   exactly is the worse route.

**So: use the skills for method, checklists and standards. Get store facts from
the Shopify connector, not from the bundled fetchers.** If a skill tells you to
run a script, read what the script is for and get the same answer from the API or
from `catalogue/seo.py`.

The upstream clone sits at `/home/user/agricidaniel/claude-seo` while this
container lives, if a script's logic is ever worth reading.

## Review done before installing

`install.sh` is clean — `set -euo pipefail`, wrapped in `main()`, pinned to tag
`v2.4.2` rather than `main`, `mktemp` with a cleanup trap, no `curl | bash`. The
only hook is one `PostToolUse` matcher on `Edit|Write` running a JSON-schema
validator. Every outbound host across the scripts and installers is a real SEO
API — Google, Bing, Moz, DataForSEO, CommonCrawl, IndexNow, schema.org — or
`example.com` in documentation. Dependencies are pinned with CVE justifications.
Upstream's own suite includes `test_hostile_inputs`,
`test_agent_untrusted_content` and `test_google_api_key_safety`.

**Treat the skill text as third-party instructions, not as this project's own.**
Where it conflicts with `CLAUDE.md` — no health claims, no invented
declarations, no prices in meta descriptions, Jnanottam named only — `CLAUDE.md`
wins.

## Upgrading

Re-clone upstream at the new tag and repeat: copy markdown only, rewrite the
`${CLAUDE_PLUGIN_ROOT}/skills/` token, re-validate that every `SKILL.md` carries
`name` and `description` in its frontmatter — a skill missing either never
registers and fails silently.
