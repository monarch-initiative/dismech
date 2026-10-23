# Deep-Research Provider Fallback

A brief asks for falcon. No `EDISON_API_KEY` is set, the run fails, and the
curator substitutes `claude_code` by hand and writes a paragraph about it into
the history record. At least six committed history records say exactly that:

> DEEP-RESEARCH PROVIDER SUBSTITUTION. The brief specified falcon, but falcon is
> unavailable in this environment […] so the claude_code provider was
> substituted.

`deep-research-client` 0.2.11 can do that handoff itself, and record which
provider produced the report. This page covers how to ask for it and what the
repository does afterwards so the substitution stays visible in the data rather
than in prose.

## Asking for a fallback

```bash
# let the client choose who takes over
just dr_fallback='--fallback' research-disorder falcon Marfan_Syndrome

# name the order yourself
just dr_fallback='--fallback-provider openai --fallback-provider perplexity' \
    research-disorder falcon Marfan_Syndrome
```

A fallback is taken only when the provider cannot do the work at all — missing
or rejected credentials, no credit, spent quota. Since 0.2.11 those failures are
classified as non-retryable, so a run with a missing key gives up and hands over
instead of retrying its way through the timeout.

## Why it is off by default

`dr_fallback` is empty unless you set it, and that is a judgement rather than
caution.

`just research-missing-provider falcon` skips a disorder only when the **falcon**
report already exists. With fallback always on and no `EDISON_API_KEY`, a sweep
over 50 disorders would produce 50 `claude_code` reports, and the next sweep
would produce 50 more: falcon never becomes present, so nothing is ever skipped.
The queue would never drain and the reports would pile up.

Turning it on for a single run you are watching is the case it is built for.

## What the repository does afterwards

The provider is in the filename — `<Disorder>-deep-research-<provider>.md` — and
`scripts/deep_research_coverage.py` reads it back out of there. A fallback that
left the name alone would leave a `claude_code` report called `-falcon.md`, and
`just research-status` would then report falcon coverage that does not exist.

So every research recipe has the client write into a **staging directory**
(`tmp/research-staging/run.XXXXXX/`, which git ignores) and then runs one
placement step that moves the run's output into `research/`:

```
uv run python scripts/align_research_provider.py "$staged_file" \
    --requested "$provider" --into research
```

On a report that fell back, it names the report for the provider that wrote it:

| | |
|---|---|
| the report | `Foo-deep-research-falcon.md` → `Foo-deep-research-claude_code.md` |
| its citations sidecar | `…falcon.md.citations.md` → `…claude_code.md.citations.md` |
| its artifacts directory | `Foo-deep-research-falcon_artifacts/` → `…claude_code_artifacts/` |

and rewrites the report's links to that directory, in the body and in the
frontmatter `artifacts:` block, so nothing is left pointing at a path that no
longer exists.

The step is wired into `research-disorder`, `research-datasets`,
`research-module`, `research-comorbidity`, `research-surrogacy` and
`research-disorder-cyberian-codex`; the hypothesis path in
`scripts/hypothesis_deep_research.py` aligns in place instead (see below). Tests
(`test_every_research_recipe_aligns_the_provider_after_running`,
`test_no_research_recipe_lets_the_client_write_into_research`) keep it that way.

## A run never replaces an existing report

If the name the report should carry is already in use — by an earlier report,
its citations sidecar, or its `_artifacts/` directory — the new report is placed
**beside** it with the run date appended, and the existing files are not
touched:

| Already in `research/` | New run | Placed as |
|---|---|---|
| `Foo-deep-research-falcon.md` | falcon succeeds | `Foo-deep-research-falcon-2026-10-08.md` |
| `Foo-deep-research-falcon.md` | falcon fails, claude_code answers | `Foo-deep-research-claude_code.md` |
| `…-falcon.md` and `…-claude_code.md` | falcon fails, claude_code answers | `Foo-deep-research-claude_code-2026-10-08.md` |
| the above plus `…-claude_code-2026-10-08.md` | a second run the same day | `…-claude_code-2026-10-08-2.md` |

The citations sidecar and artifacts directory take the same dated stem, and the
artifact links are rewritten to match. `scripts/deep_research_coverage.py`
strips the `-YYYY-MM-DD[-N]` suffix when it reads the provider back out of the
name, so a dated report still counts as that provider's. The renderer takes the
provider from the frontmatter and lists every report.

**Why this exists (#12700).** The client used to write straight onto
`research/<Disorder>-deep-research-<provider>.md`. Re-running a provider for a
disorder that already had its report therefore overwrote the committed report
before anything else ran, and on a fallback the alignment step then renamed the
overwritten file — together with the *previous* run's `_artifacts/`, which it
found beside the report by name — onto the fallback provider's name. The
committed falcon report vanished and its artifacts were re-attributed to
claude_code. This was caught by eye on `RPE65-Related_Retinopathy` (PR #12699).

If placement fails, nothing in `research/` changes; the run's output stays in
its staging directory and the error names it, so a paid run is never lost.

## The trigger is `fell_back`, not a name mismatch

This is the part worth knowing before changing any of it. A filename slug that
differs from the frontmatter `provider` is **normal** and does not mean a
fallback happened:

- `just research-disorder edison Foo` writes `-edison.md` for a report whose
  provider is `falcon` — `edison` is an alias.
- `just research-disorder-cyberian-codex Foo` writes `-cyberian-codex.md` for a
  run whose provider is `cyberian` with an `agent_type` parameter.

Renaming whenever the name disagreed with the frontmatter would rewrite both of
those. The alignment step keys on `fell_back: true`, which upstream sets only
when a provider other than the first choice produced the report — exactly the
case where the filename is a lie.

## What a fallback leaves in the report

`fell_back`, `requested_provider` and `provider_attempts` appear in the
frontmatter **only** when a fallback was taken; their presence is the finding.
`provider` always names whoever produced the report.

```yaml
provider: claude_code
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
- provider: claude_code
  succeeded: true
```

Upstream withholds the provider's raw error text from `provider_attempts`, so
the record says that falcon did not run, not why. If the reason matters, it is
in the run's own output.

**This replaces the hand-written history paragraph.** Record the substitution by
letting the report carry it; a history record can then say what was curated
instead of re-explaining which key was missing.

## When alignment refuses

It exits non-zero and moves nothing, in these cases:

- **The source is committed content this run did not write.** In-place
  alignment (the hypothesis path, or calling the script without `--into`)
  refuses to move a report, citations sidecar or `_artifacts/` directory that
  git tracks and that nothing has modified since the last commit: it cannot be
  the output of the run that just finished. The case that matters is an
  `_artifacts/` directory left by an earlier provider beside a report the new
  run rewrote — moving it would attach one provider's artifacts to another's
  report (#12700). Restore or remove the stale file deliberately, then re-run
  the alignment.
- **The destination is taken** (in-place alignment only; placement with `--into`
  dates the name instead). A `claude_code` report for that disorder already
  exists. Both files stay on disk; decide which to keep rather than letting one
  overwrite the other.
- **The requested slug is not in the filename.** There is then no way to tell
  which part of the name is the provider, and guessing is worse than stopping.
- **The report records a fallback but names no provider.** Nothing to rename it
  to.

A failure here is loud on purpose: the file on disk is a report by one provider
carrying another's name, which is the defect the step exists to prevent.

## Related

- [`docs/deep-research-reference-validation.md`](deep-research-reference-validation.md)
- [`docs/deep-research-term-validation.md`](deep-research-term-validation.md)
- `just research-status` — the coverage table this keeps honest.
