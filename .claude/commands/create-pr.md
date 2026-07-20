---
description: Create a pull request (PR) from some work
argument-hint: [DISORDER_NAME (optional)]
---

Create a pull request from work that you have done. Typically this is a new disease, but in some cases it may be QC improvements or enhancements to existing diseases.

ALWAYS make sure your work has been validated (see justfile for targets). Best efforts should be made to reach high compliance with guidelines, but we can always iterate

Generally a PR should be about a single disease. However, in some cases it makes sense to batch changes together. Use judgment.

What SHOULD be included in a PR

- the yaml file (kb/disorders/DISORDER.yaml)
- the deep research results for that disorder (if a new disorder is created)
- any publications added to the cache
- term cache changes
- **a history record** under `history/` describing this curation session (see below)

## Record a history entry (required for KB changes)

Any PR that creates or edits a KB entry (`kb/disorders/`, `kb/modules/`, or
`kb/comorbidities/`) should also add an append-only history record so curation
provenance keeps pace with content. CI posts an advisory warning when a KB entry
changes without one.

Scaffold it with the helper (never hand-write the path/timestamp):

```bash
just new-history --kind disorder --slug DISORDER \
  --event CREATE --outcome changed \
  --summary "Create: DISORDER" \
  --agent-tool claude-code --model <model-id> \
  --sections phenotypes,pathophysiology,evidence,treatments \
  --pr <PR_NUMBER> --issue <ISSUE_NUMBER> \
  --details "One-paragraph summary of what was curated and how it was validated."
```

Use `--event EDIT` for enhancements to an existing entry, `--event REVIEW` for a
review, and `--kind module`/`--kind comorbidity` for those targets. Then edit the
emitted `details` if needed, validate, and stage it:

```bash
just validate-history <path-printed-by-new-history>
git add history/
```

See `docs/history.md` for the full format. The PR number may not exist yet when
you scaffold — either pass it after opening the PR, or add it to the record's
`links.prs` in a follow-up commit.

What should NOT be included

- derived browser files (e.g. app.js, HTML files); these are added later by a weekly job

## A note on schema extensions

Sometimes a PR involves extending the schema at the same time as using these new extensions. These should be flagged for review by @cmungall, and ideally discussed on an issue beforehand
