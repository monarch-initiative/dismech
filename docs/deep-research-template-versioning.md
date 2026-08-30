# Deep-Research Template Versioning

A deep-research report records the prompt it came from as a bare path:

```yaml
template_file: templates/disease_pathophysiology_research.md
```

That is a path, not a version. The file behind it changes; the reference does
not. So a report cannot tell you what it was actually asked.

This is not a hypothetical. The disease template has four committed revisions,
and commit `0729e8e5b6` ("Remove MAXO ontology; remap all treatment/diagnosis
terms to NCIT") changed what it asks for without touching a single report. Every
report written before that commit was asked for MAXO terms; the file now asks
for NCIT; nothing in those reports records the difference. Issue #10183.

Two things follow that matter to curation:

- **Provider and time comparisons silently assume a fixed prompt.** Two reports
  for the same disease six months apart may have been asked materially different
  questions.
- **A curator reviewing a report cannot tell** whether a provider ignored an
  instruction or was never given it.

## What this adds

**Going forward, reports are stamped.** Every `just research-*` recipe now
records the template's git blob hash before the report is finalised:

```yaml
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
```

**Looking back, older reports are resolved rather than rewritten.** A report's
revision is recoverable from its `start_time` against the template's commit
history, so no backfill of committed reports is needed — see
[Why there is no backfill](#why-there-is-no-backfill).

## Using it

```bash
just template-version-audit                       # census across research/
just template-version-audit --stale-only --format list
just template-version-audit --template templates/disease_pathophysiology_research.md
just template-version-audit --format tsv --out /tmp/versions.tsv
```

The summary reports how each answer was reached:

```
Reports scanned: 2645

How the template revision was determined:
  stamped        0  0.0%
  inferred    2153  81.4%
  unknown      492  18.6%
```

The scan recurses: reports also live in `research/modules/`, `groupings/`,
`surrogacy/` and `datasets/`. It skips citation sidecars and the contents of
`*_artifacts/` directories, which hold the tables and figures a provider
returned beside a report — 993 of the 1,023 nested markdown files, and not
reports.

**`stamped` and `inferred` are not the same claim.** A stamp is a fact the
generator recorded. An inference is reconstructed from timestamps and assumes
the working tree matched a committed revision when the report ran — which an
uncommitted local template edit would break. Do not present an inferred answer
as a recorded one.

**`undetermined` is not `stale`.** They are separate rows for that reason. A
report whose revision could not be established has not been shown to be out of
date; it has not been shown to be anything.

### Finding what a hash means

The stamp is a git blob hash, so git resolves it directly:

```bash
git log --find-object=1e7ea4ee817a -- templates/
git cat-file blob 1e7ea4ee817a | head -40    # the prompt exactly as it ran
```

That is the reason for a hash over a hand-maintained `template_version:` string:
a version string goes stale the first time someone edits the template and forgets
to bump it, while a content hash cannot disagree with the content. The cost is
that a hash says nothing about *what* changed — `git log --find-object` and the
commit message carry that.

## Why there is no backfill

The obvious move is to write `template_sha` into all ~2,650 committed reports.
It was considered and rejected:

- The information is **already derivable**. A report's `start_time` plus the
  template's commit history gives the revision that was in effect, which is what
  the audit does on demand.
- The diff would be enormous, and would conflict with anything else touching
  `research/`, to record something computable.
- It would still leave every report whose file cannot be rewritten unanswered,
  so the resolver has to exist regardless.

Stamping earns its place for *new* reports because it is authoritative — it
records what actually happened rather than inferring it, and it survives a
template being edited without being committed.

## What the audit found

At the time of writing, on 2,645 reports:

| | |
|---|---:|
| Generated from a superseded revision | 1,974 |
| Undetermined | 491 |
| Current | 177 |

**Every report generated from the disease template predates the current
revision** — 980 from `630b0d5e4cd7`, 601 from `839c47271432`, 373 from
`c566b1bad3b8`, none from the current `1e7ea4ee817a`. This is expected: that
template changed in #10182, after all of them were written.

That is also why **staleness is reported, never gated**. A check that failed on
a superseded revision would be red on 1,974 reports the moment it was added, and
would go red again for the whole corpus after every prompt edit. Staleness here
is a fact about the corpus, not a defect in any one report.

The 491 undetermined split into honest categories rather than failures:

- **452 record no `template_file` at all** — mostly hand-written syntheses.
- **A dozen record a free-text label** rather than a path (`manual_curation`,
  `codex_supplement_local`, `provider_failure_fallback`). No path is invented for
  these; a label is not a template.
- **Two predate their template's first commit.** The comorbidity Jinja template's
  only commit is hours *after* the two reports that used it, so they genuinely ran
  against an uncommitted version. Reporting them as undetermined is correct;
  attributing them to a revision that did not yet exist would not be.

One quirk is repaired rather than reported: **20 reports record the path with
Windows separators** (`templates\disease_pathophysiology_research.md`). That names
the same template every other report names, so the separator is folded before
lookup.

## Scope

The mechanism is template-agnostic — it keys on whatever `template_file` a report
records, so all seven templates under `templates/` are covered by the same code
with nothing per-template to maintain.

## Follow-ups not done here

- **Surfacing staleness in `just qc-deep-research`.** Deferred deliberately: see
  above for why it cannot be a gate today. Worth adding as an advisory line once
  there is a view on what a curator should *do* about a superseded report.
- **A per-template changelog.** A hash says a prompt changed, not what changed.
  Commit messages carry that today; a `templates/CHANGELOG.md` would make it
  browsable, at the cost of discipline to keep it current.
- **Re-running on prompt change.** Almost certainly not automatic at this volume,
  but the audit now makes the affected set enumerable if that is ever wanted.
