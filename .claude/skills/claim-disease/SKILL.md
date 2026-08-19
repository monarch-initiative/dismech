---
name: claim-disease
description: Use when claiming the next disease to curate in dismech. Two-phase pick — open `claim`-labelled issues for what is already taken, then the `stubs/` queue for what is left — then files a `Curate <label> (MONDO:NNNNNNN)` claim issue assigned to the current GitHub user. Accepts an optional integer 1–8 to claim N diseases at once.
---

# claim-disease

Claim the next disease(s) to curate. The queue of remaining work is `stubs/`;
the live lock on who has what is an open GitHub issue labelled `claim`. This
skill checks both, then files the claim.

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

## How claiming works

**An open GitHub issue labelled `claim` is the lock.** Not the stub file — a
stub edit only becomes visible when its PR merges, which is far too late to stop
two agents picking the same disease.

The two phases are cheap and, importantly, correct:

1. **Claims** — `gh issue list --label claim` hits GitHub's *list* endpoint,
   which is immediately consistent. An issue filed thirty seconds ago is already
   there. (The old preflight used `--search`, whose index lags creation by
   seconds to minutes — the exact width of the race it was meant to close.)
2. **Stubs** — `stubs/` says what is left to do at all.

One call fetches every claim, so the check costs one request no matter how big
the candidate pool is.

**A claim survives a long PR.** Curation PRs sit in review for weeks and that is
normal; the claim holds the whole time. Only a claim that is *old with no PR* is
questionable, and `just check-claims` reports those rather than releasing them.

## Workflow

1. **Read N** from the user's argument (default 1).

2. **Resolve the current GitHub user**: `gh api user -q .login`. This is the
   assignee — the person driving the agent, never a hardcoded name.

3. **Fetch the claims and pick, in one pass:**

   ```bash
   just fetch-claims                        # -> tmp/claims.json, one API call
   just check-claims                        # double-claims, unkeyed, stale
   just next-unclaimed $((N + 20))          # stubs minus claimed, as a pool
   ```

   `next-unclaimed` takes `--json` if you want it machine-readable. Ask for
   headroom (`N + 20`), because you will skip candidates.

4. **Read the pool and choose deliberately.** Do not take rows in order — within
   a priority band the order is an arbitrary hash spread. Prefer candidates you
   can curate well; apply the suspicion list above. Note what you skipped and
   why; you will report it.

5. **Duplicate preflight, for each candidate you intend to claim.** The claim
   check is by MONDO ID, so it cannot see a disease curated or claimed under a
   different term:

   ```bash
   git fetch origin main
   git grep -n -i -e "<MONDO_ID>" -e "<label>" origin/main -- kb/disorders kb/groupings || true
   grep -rli "<distinctive word from the label>" kb/disorders/ kb/groupings/
   ```

   Also scan `tmp/claims.json` titles for the label and its synonyms — an
   agent may have claimed the same disease under a different MONDO ID. If a
   candidate turns out to be already curated, delete its stub in your PR; that
   is the fix, not just skipping it.

6. **File the claim issue.** This is the claim — file it *before* starting work,
   not after.

7. **Report**: the issue URLs, and — explicitly — every candidate you skipped
   with the reason. If you filed fewer than N, say so; do not pad the count.

## Filing a claim

Two things make the issue a usable lock, and both are load-bearing:

- **The `claim` label.** It is what makes the check a fast, immediately
  consistent list query instead of a laggy search.
- **The MONDO ID in the title.** It is the key everything matches on. An issue
  titled `curate peripartum cardiomyopathy` locks nothing — `just check-claims`
  reports those separately so they can be retitled.

Title, exactly:

```
Curate <label> (<MONDO_ID>)
```

The `claim` label already exists in `monarch-initiative/dismech`. **Do not run
`gh label create --force` on it** — `--force` updates an existing label, so that
would silently overwrite its colour and description. If `gh issue create` fails
because the label is missing (a fork, a new repo), say so and ask; do not
recreate it yourself.

```bash
gh issue create \
  --title "Curate <label> (<MONDO_ID>)" \
  --assignee "$(gh api user -q .login)" \
  --label claim,curation,enhancement \
  --body "$(cat <<'EOF'
...body...
EOF
)"
```

Body:

```markdown
Curate a dismech entry for **<label>** ([<MONDO_ID>](https://monarchinitiative.org/<MONDO_ID>)) — <one-sentence biomedical context>.

**First decide what this should be**: a `kb/disorders/` Disease, a `kb/groupings/` Grouping, a `has_subtypes` entry on an existing disease, or out of scope. See the Disease Groupings section of `CLAUDE.md` and #8727 for the rule — a disorder entry needs one reasonably conserved pathograph. Record the decision in the stub's `entry_type` before curating.

<If you know of subtypes, name them and say whether they look like `has_subtypes` entries or separate diseases.>

Stub: `stubs/<file>.yaml`
Nominated by: <source_name from the stub>
```

**Do not edit the stub to record the claim.** The stub has no `claimed_by` or
`status: CLAIMED` — that was removed on purpose. Two sources of truth for one
fact is how they drift, and the YAML one is the slow, invisible one.

## Finishing a curation

The curation PR **should delete the stub** alongside adding the KB entry, and
close the claim issue:

```
- stubs/Yao_Syndrome.yaml
+ kb/disorders/Yao_Syndrome.yaml
+ history/disorders/Yao_Syndrome/...
```

Put `Closes #<issue>` in the PR body so merging releases the claim.

If you forget the stub, **nothing breaks** — stubs are informative, not curated
content, and a stale one is reported as an advisory that never gates. A periodic
`just tidy-stubs --apply` sweeps them. Do not go out of your way to service that
message mid-curation.

If the answer turns out to be `GROUPING` / `SUBTYPE` / `OUT_OF_SCOPE`, the PR
still deletes the stub — record the decision and reasoning in the PR body, and
close the claim issue explaining it. That is a completed curation.

## Common mistakes

- **Taking the first row because it is first.** Within a priority band the order
  is an arbitrary hash spread. It means nothing. Choose.
- **Filing a curation issue for a grouping.** Check the suspicion list. Editing
  the stub's `entry_type` is the right output, and it counts as work done.
- **Hardcoding a username.** Always resolve via `gh api user -q .login`.
- **Claiming a disease that already has a KB entry or claim.** Run the
  duplicate preflight. Both checks are by MONDO ID only;
  conceptual coverage under a different term (e.g. "Zellweger spectrum
  disorders" → `Peroxisome_Biogenesis_Disorder.yaml`) passes straight through.
- **Starting work before filing the claim issue.** The issue *is* the lock. Work
  done before it exists is unprotected.
- **Filing a claim without the `claim` label or without the MONDO ID in the
  title.** Either one makes the issue invisible to the next person's check.
- **Editing the stub to record a claim.** The stub has no claim fields. Use the
  issue.
- **Treating an old claim as free.** A claim with an open PR is live however old
  it is. `just check-claims` flags old-with-no-PR claims; ask the assignee or
  the user before taking one — do not just take it.
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

## Not a tracker issue

Do **not** add `Tracker: part of #1079` to the body. That EPIC is a static
keyword-scoped checklist covering four themes; most claims are not in it, so the
line was decorative. Progress is `just stub-stats` and the size of `stubs/`.
