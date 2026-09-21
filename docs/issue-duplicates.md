# Duplicate issue detection

New issues keep receiving the existing general research response from
`claude-issue-summarize.yml`. Label triage and the interactive `@claude` responder
also keep their existing behavior. Duplicate detection runs independently, so
research does not have to wait for search or stop when a potential match exists.

`claude-dedupe-issues.yml` uses `anthropics/claude-code-action@v1` and the search
method from [Anthropic's dedupe command](https://github.com/anthropics/claude-code/blob/7974a70773fa229e4cc65aa1b356cc21f5c216c4/.claude/commands/dedupe.md):
five parallel searches with different approaches, followed by a separate agent
that reads and verifies the candidates. Our `.claude/commands/dedupe.md` adapts
the criteria to dismech's research-notebook use: related diseases, mechanisms,
papers, and follow-up ideas are not automatically duplicates.

The agent has a read-only GitHub token and returns structured candidates. A
separate job checks that the issues are older and still open, and that no human
has added context while the search ran, then adds `duplicate-pending` and posts
up to three links with explanations. It records the oldest match as the canonical
issue. The model is selected through `.github/agent-config.yaml` (Sonnet by
default); manual dispatch accepts an issue number and optional model override.

The [upstream three-day closure pattern](https://github.com/anthropics/claude-code/blob/7974a70773fa229e4cc65aa1b356cc21f5c216c4/scripts/auto-close-duplicates.ts)
is implemented by `.github/scripts/issue-duplicates.js` using GitHub's REST API:

- The bot's duplicate notice starts a three-day objection window.
- Any subsequent human comment, or any human 👎 on the notice, prevents closure.
  Bot comments, including the normal research response, do not cancel it.
- Removing `duplicate-pending` also prevents closure. A rerun does not restore
  a removed label or reopen the objection window.
- Edited, locked, or reopened issues are left open. The canonical issue must
  still be open when the closure runs. Existing labels are preserved.
- A daily sweep closes eligible issues with GitHub's native duplicate reason
  and canonical issue ID. This happens on the first sweep after the full three
  days, not at an exact wall-clock deadline.
- Only notices carrying our marker and posted by `github-actions[bot]` count.
  Rerunning detection does not create another notice or restart the clock.
  Existing `duplicate` labels or comments from other workflows cannot trigger
  this closure process.

The sweep paginates open issues labeled `duplicate-pending`, plus their comments,
reactions, and timeline events directly through the API. This avoids scanning
every open issue's discussion and does not use GitHub's search index to find pending
closures. Candidate discovery remains agentic GitHub search, supplemented by a
list of recent issues. There is no local embedding index or hosted database.

The sweep's daily schedule is managed by `.github/cron-profiles.yaml`; the `off`
profile disables it. Manual dispatch defaults to a **dry run**, logging which
issues would close. To preview, run:

```bash
gh workflow run auto-close-duplicates.yml -f dry_run=true
```

Tests run offline with `node --test tests/js/issue_duplicates.test.mjs` and are
included in the existing `just test-search` CI check. These exercise the
lifecycle rules; they do not measure the model's duplicate-detection accuracy.
