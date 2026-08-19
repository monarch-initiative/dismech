---
name: claim-disease
description: Use when claiming the next disease to curate from the dismech curation stub queue in `stubs/`. Picks an open stub, opens a GitHub curation issue, assigns it to the current GitHub user, and marks the stub CLAIMED. Accepts an optional integer 1–8 to claim N diseases at once.
---

# claim-disease

Claim the next disease(s) to curate from the stub queue in `stubs/`. Opens GitHub
issues and assigns them to whoever is running the skill.

## When to use

- "What should I curate next?"
- "Claim the next disease"
- "Pick me the next 3 diseases and open issues"

Skip when:
- The user names a specific disease — just open that issue directly.

## The queue is a directory, not a ranking

`stubs/` holds one YAML per disease we intend to curate. There is no score. The
only ordering is a hand-set `priority` band (`HIGH` / `NORMAL` / `LOW`) that a
person put there in a pull request; within a band the order is an arbitrary
(hash-based, reproducible) spread and carries **no information**.

So `just next-stubs` gives you a *pool*, not a ruling. **Pick the disease you
actually know something about.** If the first row is outside what you can curate
well, skip it and say so. Skipping is expected, not a failure.

You are also allowed — encouraged — to stop and ask the user, especially when a
candidate looks like it should not be a disorder entry at all.

## Candidates to be suspicious of

Read the label and ask whether it names **one disease with one reasonably
conserved pathograph**. If it does not, do not file a curation issue. Instead,
edit the stub: set `entry_type` and explain in `notes`.

Watch for:

- **Groupings** — a union of distinct diseases. `lysosomal storage disease`,
  `RASopathy`, `B-cell non-Hodgkin lymphoma`. These belong in `kb/groupings/`
  (see the Disease Groupings section of `CLAUDE.md`), not `kb/disorders/`. Set
  `entry_type: GROUPING`.
- **Over-broad categories** — `soft tissue sarcoma` has roughly 800 NCIT
  subclasses. There is no single mechanism to curate. Set `entry_type: GROUPING`
  or `OUT_OF_SCOPE`.
- **Multiple mechanisms under one name** — `rickets` (nutritional, X-linked
  hypophosphatemic, vitamin-D-dependent) is several diseases sharing a
  radiographic finding. Usually `GROUPING`.
- **Phenotypes, not diseases** — `microcephaly` is a finding. `OUT_OF_SCOPE`,
  unless the specific disease entity is meant.
- **Susceptibility / predisposition terms** — usually `OUT_OF_SCOPE`.
- **Cancers** — deprioritize for now. The project does not yet have a settled
  lump/split strategy for neoplasms (see #7082). Prefer a non-cancer candidate,
  or ask the user.

Recording `GROUPING`, `SUBTYPE`, or `OUT_OF_SCOPE` on a stub and deleting it is a
**real curation outcome** — you have resolved the concept. It is not a way of
dodging work, and it should be reported as work done.

## Inputs

- Optional positional argument **N**: number of diseases to claim. Defaults to
  **1**, maximum **8**. If the argument is non-integer, `<= 0`, or `> 8`, stop and
  ask the user rather than guessing. Never silently cap a request for `N > 8`.

## Workflow

1. **Read N** from the user's argument (default 1).

2. **Resolve the current GitHub user**: `gh api user -q .login`. This is the assignee.

3. **Pull the candidate pool** — ask for headroom, since candidates get skipped:

   ```bash
   just next-stubs $((N + 20)) --json
   ```

   Each row gives `mondo_id`, `label`, `priority`, `proposed_name`, `rationale`,
   and `stub_path`. `next` already excludes stubs that are CLAIMED, BLOCKED,
   DEFERRED, or resolved as `GROUPING` / `SUBTYPE` / `OUT_OF_SCOPE`.

4. **Read the pool and choose deliberately.** Do not take rows in order. Prefer
   candidates you can curate well; apply the suspicion list above. Note which
   ones you skipped and why — you will report this.

5. **Duplicate preflight for each candidate you intend to claim.** `check-stubs`
   only catches exact MONDO-ID overlap. Conceptual coverage under a different
   term will not be caught, so check by hand:

   ```bash
   git fetch origin main

   # Still absent from the latest upstream KB?
   git grep -n -i -e "<MONDO_ID>" -e "<label>" origin/main -- kb/disorders kb/groupings || true

   # Lexical sweep for a synonym curated under another name.
   grep -rli "<distinctive word from the label>" kb/disorders/ kb/groupings/

   # PRs and issues, all states; repeat for important synonyms.
   gh pr list --repo monarch-initiative/dismech --state all \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,state,url,headRefName --limit 100
   gh issue list --repo monarch-initiative/dismech --state all \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,state,url,labels --limit 100
   ```

   Open *and* closed records both matter: a closed PR may already be merged, and
   a closed issue may explain why a similar target should not be curated
   separately. If a candidate turns out to be covered, delete its stub in the PR
   (that is the fix) rather than only skipping it.

6. **File the issue and mark the stub claimed**, for each of the N candidates.

7. **Report**: the issue URLs, the stubs you marked CLAIMED, and — explicitly —
   every candidate you skipped with the reason. If you filed fewer than N, say
   so; do not pad the count.

## Marking a stub claimed

Edit the stub file in place and commit it on a branch with the issue link:

```yaml
status: CLAIMED
claimed_by: <github-handle>
issue: <issue number or URL>
```

This is what stops two people claiming the same disease. `status` and
`claimed_by` are the only fields you should change when claiming — leave
`entry_type` as `UNDECIDED` until you have actually made the lump/split call.

## Issue template

Title:

```
Curate <label> (<MONDO_ID>)
```

Body:

```markdown
Curate a dismech entry for **<label>** ([<MONDO_ID>](https://monarchinitiative.org/<MONDO_ID>)) — <one-sentence biomedical context>.

**First decide what this should be**: a `kb/disorders/` Disease, a `kb/groupings/` Grouping, a `has_subtypes` entry on an existing disease, or out of scope. See the Disease Groupings section of `CLAUDE.md` and #8727 for the rule — a disorder entry needs one reasonably conserved pathograph. Record the decision in the stub's `entry_type` before curating.

<If you know of subtypes, name them and say whether they look like `has_subtypes` entries or separate diseases.>

Stub: `stubs/<file>.yaml`
Nominated by: <source_name from the stub>

Tracker: part of #1079.
```

Create with:

```bash
gh issue create \
  --title "Curate <label> (<MONDO_ID>)" \
  --assignee "$(gh api user -q .login)" \
  --label curation,enhancement \
  --body "$(cat <<'EOF'
...body...
EOF
)"
```

## Finishing a curation

The curation PR **deletes the stub and adds the KB entry** in the same PR:

```
- stubs/Yao_Syndrome.yaml
+ kb/disorders/Yao_Syndrome.yaml
+ history/disorders/Yao_Syndrome/...
```

`just check-stubs` (part of `just qc`, and enforced by
`tests/test_stubs.py::test_no_stub_survives_curation`) fails if you leave the
stub behind.

## Common mistakes

- **Taking the first row because it is first.** Within a priority band the order
  is an arbitrary hash spread. It means nothing. Choose.
- **Filing a curation issue for a grouping.** Check the suspicion list. Editing
  the stub's `entry_type` is the right output, and it counts as work done.
- **Hardcoding a username.** Always resolve via `gh api user -q .login`.
- **Claiming a disease that already has a KB entry, PR, or issue.** Run the
  duplicate preflight. Coverage detection in tooling is by MONDO ID only;
  conceptual coverage under a different term (e.g. "Zellweger spectrum
  disorders" → `Peroxisome_Biogenesis_Disorder.yaml`) passes straight through.
- **Claiming without marking the stub.** An unmarked stub gets claimed twice.
- **Filing fewer issues than requested without saying so.** Report the shortfall.

## Adding to the queue

If the user wants a disease curated that has no stub, add one — it is a two-field
YAML file:

```yaml
mondo_id: MONDO:0009770
label: 3MC syndrome 1
priority: HIGH
notes: Why this jumps the queue.
```

Filename is the label slugged (`3MC_Syndrome_1.yaml`); `just check-stubs` will
tell you if you got it wrong. See `docs/curation-stubs.md`.

## Tracker

The umbrella issue for priority curation is **#1079**. Always link new curation
issues back to it.
