---
name: claim-disease
description: Use when claiming the next disease to curate in dismech. Two-phase pick — open `claim`-labelled issues for what is already taken, then the `stubs/` queue for what is left — then files a `Curate <label> (MONDO:NNNNNNN)` claim issue assigned to the current GitHub user. Accepts an optional integer 1–8 to claim N diseases at once. The skill should also start the curation process.
---

# claim-disease

Claim the next disease(s) to curate. The queue of remaining work is `stubs/`;
the live lock on who has what is an open GitHub issue labelled `claim`. This
skill checks both, then files the claim, and then commences work.

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

**The two phases do not see work that never filed a claim.** Claims and stubs
are one intake path; the `curation`-labelled literature-scan issues worked by
the curation-scanner are another, and the two do not talk. A scanner agent that
goes straight from a `curation` issue to a PR never files a claim issue, so its
work is absent from phase 1 — and absent from phase 2 too, since the stub
survives until that PR merges. That is why step 5 searches open PRs as a third
surface. Assume neither phase knows about a PR.

## The stub already holds the lump/split evidence

`just enrich-stubs` has **already** written `mondo_parents`, `mondo_descendants`,
`mondo_descendant_count` and `genes` into the stubs. That is the evidence the
`entry_type` decision turns on. Read the stub file. Do **not** re-derive it with
per-candidate ontology lookups.

**An empty block is omitted, not written as zero** (`render()` in
`scripts/enrich_curation_stubs.py` only emits a block when it has content), so
most stubs carry only some of these fields:

| field | stubs carrying it (of 1,842) |
|---|---|
| `mondo_parents` | 1,841 — 99.9% |
| `genes` | 1,317 — 71.5% |
| `mondo_descendants` / `mondo_descendant_count` | 178 — **9.7%** |

**Absence is the answer, not a missing answer.** No `mondo_descendant_count:`
line means MONDO records no descendants — the overwhelmingly common case, and a
*positive* signal that the term is a leaf rather than a grouping. No `genes:`
means no causal gene. Neither is a sign that enrichment was skipped, and neither
is a reason to reach for `runoak`.

This is the single largest avoidable cost in a claim run, and it is worse than
it looks:

- **It is slow.** A *warm* `runoak -i sqlite:obo:mondo info` call is ~28s, and
  the first one builds a 1.2 GB local MONDO database. Reading the stub is free.
  A run that looked up eight candidates spent minutes re-reading fields it had
  already printed.
- **It cannot help.** `enrich-stubs` reads the *same* MONDO release `runoak`
  does. Where a stub's `genes:` is empty, MONDO records no causal gene either —
  a blank stub means a blank ontology, not an unasked question. Re-querying
  returns the same blank, slowly.

So:

- **`mondo_descendant_count` is the grouping test, and so is its absence.**
  20 descendants, several already in `kb/disorders/`, is a GROUPING — decided,
  without a single query. No descendant block at all is the leaf case, and is
  equally decisive; it is what ~90% of the queue looks like.
- **`genes:` is the entity-identity anchor.** If it names one gene, that is the
  gene; do not "verify" it from memory-driven doubt. (One run guessed *SCN10A*,
  then spent a 28s lookup correcting itself, when the stub said `hgnc:10583
  SCN11A` on the line above.)
- **When the stub is blank and the decision hinges on identity**, go to the
  source MONDO *doesn't* have — Orphanet or OMIM via the stub's xrefs — not back
  to MONDO.
- **`just check-stubs` and `just tidy-stubs` already report duplicates** against
  `kb/`, for free, in one pass over the whole queue. Run them once, up front,
  instead of rediscovering the same overlap per candidate.

Reach for `runoak` only for a fact the stub genuinely lacks *and* the decision
turns on. Enriching an issue body with a definition or an OMIM ID is not that.

## Workflow

1. **Read N** from the user's argument (default 1).

2. **Resolve the current GitHub user**: `gh api user -q .login`, or
   `mcp__github__get_me` where there is no `gh`. This is the assignee — the
   person driving the agent, never a hardcoded name.

3. **Fetch the claims and pick, in one pass:**

   ```bash
   just fetch-claims                        # -> tmp/claims.json, one API call
   just check-claims                        # double-claims, unkeyed, stale
   just next-unclaimed $((N + 20))          # stubs minus claimed, as a pool
   ```

   `next-unclaimed` takes `--json` if you want it machine-readable. Ask for
   headroom (`N + 20`), because you will skip candidates.

   **No `gh` CLI (web and remote sessions).** `just fetch-claims` shells out to
   `gh`, which is absent there — and `curl https://api.github.com` fails too:
   the agent proxy denies it even though `GH_TOKEN` is set. GitHub is reachable
   only through the GitHub MCP server. Build the claims file from
   `mcp__github__list_issues` with `labels: ["claim"]`, `state: "OPEN"`,
   `perPage: 100`.

   Keep it minimal. `next-unclaimed` matches the MONDO ID out of the **title**
   and reads nothing else, so this is enough, and gives a byte-identical pool:

   ```json
   [{"title": "Curate scrub typhus (MONDO:0019365)"}, {"title": "..."}]
   ```

   Do not hand-transcribe full issue records — that is minutes of typing for
   fields nothing reads. `list_issues` takes a `fields` projection, so ask for
   `fields: ["number","title","created_at"]` — and keep only those — if you also
   want `check-claims`' hygiene report
   (double-claims, unkeyed titles); the parser already accepts REST-shaped
   `created_at`/`html_url`. Note `check-claims` cannot see linked PRs over this
   path, so its **stale** list over-reports — it errs toward flagging, and a
   stale claim is only ever reported for a human, never auto-taken.

4. **Read the pool and choose deliberately.** Do not take rows in order — within
   a priority band the order is an arbitrary hash spread. Prefer candidates you
   can curate well; apply the suspicion list above. Note what you skipped and
   why; you will report it.

5. **Duplicate preflight, for every candidate you intend to claim.** The claim
   check is by MONDO ID, so it cannot see a disease curated or claimed under a
   different term. Do this for **all** your candidates in one pass, not one
   candidate at a time:

   Search the **label as well as the MONDO ID**, and search both against
   `origin/main` — that is what the `git fetch` is for, and a disease curated
   under a different term is the whole case this step exists to catch. `git
   grep` takes many `-e` patterns at once, so the batched form is one process,
   not N:

   ```bash
   git fetch origin main
   git grep -l -i \
     -e "<MONDO_ID_1>" -e "<label_1>" \
     -e "<MONDO_ID_2>" -e "<label_2>" \
     -e "<MONDO_ID_3>" -e "<label_3>" \
     origin/main -- kb/disorders kb/groupings || true
   ```

   The `|| true` is load-bearing: `git grep` exits 1 on no match, which is the
   common (good) case, and without it the block aborts under `set -o pipefail`.
   If you want per-candidate attribution rather than one file list, loop — but
   keep both patterns per candidate: `git grep -l -i -e "$m" -e "$label" origin/main ...`.

   Also scan `tmp/claims.json` titles for the label and its synonyms — an
   agent may have claimed the same disease under a different MONDO ID. If a
   candidate turns out to be already curated, delete its stub in your PR; that
   is the fix, not just skipping it.

   **Then search open PRs — the two checks above cannot see one.** This is a
   separate surface, not a belt-and-braces repeat, and it is the one that fails
   silently:

   ```bash
   gh pr list --repo monarch-initiative/dismech --state open \
     --search "\"<MONDO_ID>\" OR \"<label>\"" \
     --json number,title,url,headRefName,reviewDecision --limit 50
   ```

   Search the **label as well as the MONDO ID** — a curation PR title often
   names the disease and no term at all, so an ID-only search misses it.

   Without `gh`, use `mcp__github__search_pull_requests` with the same query
   (`repo:monarch-initiative/dismech is:pr is:open "<MONDO_ID>" OR "<label>"`).

   If an open PR already curates the candidate, **do not claim it**. Say so,
   pick something else, and leave the stub alone — the stub is correct until
   that PR merges. If the PR is stalled on something you can supply, that is
   worth reporting to the user; it is usually more valuable than a fresh claim.

6. **File the claim issue.** This is the claim — file it *before* starting work,
   not after.

7. **Report**: the issue URLs, and — explicitly — every candidate you skipped
   with the reason. If you filed fewer than N, say so; do not pad the count.

8. **Do we the work**: start curating the entries. Unless the user says to
   hold off

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

Where there is no `gh`, file it with `mcp__github__issue_write`
(`method: "create"`, `labels: ["claim","curation","enhancement"]`, `assignees`
from `get_me`) — the title and label rules below are what matter, not the tool.

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

## Check comments on the issue

Although the primary purpose of filing the issue is to establish the claim,
a nice side effect is that you will have an agent (and possibly people) commenting
on the claim. This provides a "second opinion" mechanism.

It may take a few minutes for the agent comment to appear, so you can start
work and check back later.

## One PR per disease

**N diseases means N branches and N pull requests.** Never package a multi-disease
claim run into a single branch or a single commit. Each disease gets its own
branch off `main`, carrying only:

```
+ kb/disorders/<Disease>.yaml
+ history/disorders/<Disease>/...
+ references_cache/PMID_*.md        <- only the PMIDs THAT entry cites
  cache/**/*.csv                    <- only the term rows THAT entry introduced
- stubs/<Disease>.yaml
```

The shared files are the part people get wrong. `references_cache/` and
`cache/**/*.csv` are repository-wide, so a lazy `git add references_cache/ cache/`
sweeps another disease's rows into this PR. Derive the ownership instead of
eyeballing it: a reference belongs to the entry that cites its PMID, and a cache
row belongs to the entry that uses that CURIE. Rows land in canonical sorted
position (`just normalize-cache`), never appended at end-of-file — see the cache
ordering rules in `CLAUDE.md`.

Unrelated cleanup found along the way — a stale stub for a disease somebody else
already curated, say — is its own small PR. Do not attach it to a curation PR it
has nothing to do with.

**Why this matters and is not bookkeeping.** The claim/stub machinery is
per-disease: one `Closes #<issue>` releases one claim and retires one stub. A
combined PR cannot release three claims cleanly, presents reviewers with a diff
several thousand lines long, and lets one contested lump/split call block two
diseases that nobody disputes.

### When the environment hands you one branch

Some runners inject a single pre-named branch for the whole invocation (e.g.
`claude/claim-disease-3-<id>`) together with an instruction not to push anywhere
else without permission. That instruction does not scale with N, and it
**conflicts** with the rule above.

Do not resolve that conflict silently in either direction. Say so, and ask:

> The run gave me one branch, but dismech convention is one PR per disease.
> Shall I open three branches instead?

Raise it **before** committing, not after the work is packaged — re-splitting a
finished single commit is recoverable but wasteful, and a reviewer should never
be the one to discover the packaging is wrong.

## After the PRs are open

Opening the PR is not the end of the task. Keep the worktrees in place and stay
available to respond to review feedback — the automated reviewer usually comments
within a few minutes, and CI may go red.

Work each PR until it is **approved**, then stop:

- Address review comments and push fixes to that PR's branch.
- Fix CI failures that your diff caused.
- Reply where a reviewer asked something you are not going to change, with the
  reason.

Once a PR is approved, stop working it. Do not merge it yourself, do not dismiss
a review to clear a gate, and do not keep polishing an approved PR. Approved is
the finish line. Only tear the worktrees down once every PR in the run is
approved (or closed).

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
- **Re-deriving the stub's own fields with `runoak`.** `mondo_descendants`,
  `mondo_descendant_count` and `genes` are already in the file. A warm MONDO
  lookup costs ~28s, builds a 1.2 GB database, and reads the same release
  `enrich-stubs` did — so it cannot know anything the stub does not.
- **Hand-transcribing claim issues into `tmp/claims.json`.** When `gh` is
  missing, a titles-only array from MCP gives an identical pool. Typing out
  number/assignees/url/createdAt for 50 issues is minutes spent on fields
  `next-unclaimed` never reads.
- **Filing a curation issue for a grouping.** Check the suspicion list. Editing
  the stub's `entry_type` is the right output, and it counts as work done.
- **Hardcoding a username.** Always resolve via `gh api user -q .login`, or
  `mcp__github__get_me` where there is no `gh`.
- **Claiming a disease that already has a KB entry or claim.** Run the
  duplicate preflight. Both checks are by MONDO ID only;
  conceptual coverage under a different term (e.g. "Zellweger spectrum
  disorders" → `Peroxisome_Biogenesis_Disorder.yaml`) passes straight through.
- **Claiming a disease that already has an open curation PR.** This is the
  blind spot the other checks cannot cover, and it is silent — nothing looks
  wrong. A stub only goes stale when its PR **merges** (`tidy-stubs` reads
  `kb/disorders/` on main), the `git grep` in the preflight searches
  `origin/main`, and the claim check reads `claim`-labelled issues. An entry
  sitting on an unmerged PR branch is invisible to all three, so the stub stays
  in the pool and `next-unclaimed` will happily offer it. Search open PRs.
- **Starting work before filing the claim issue.** The issue *is* the lock. Work
  done before it exists is unprotected.
- **Filing a claim without the `claim` label or without the MONDO ID in the
  title.** Either one makes the issue invisible to the next person's check.
- **Editing the stub to record a claim.** The stub has no claim fields. Use the
  issue.
- **Treating an old claim as free.** A claim with an open PR is live however old
  it is. `just check-claims` flags old-with-no-PR claims; ask the assignee or
  the user before taking one — do not just take it.
- **Packaging N diseases into one branch or one commit.** One PR per disease. If
  the runner handed you a single branch, surface the conflict and ask rather than
  quietly accepting it — see "When the environment hands you one branch".
- **`git add references_cache/ cache/` on a multi-disease run.** That sweeps other
  diseases' reference and term-cache rows into this PR. Assign them by which entry
  cites the PMID / uses the CURIE.
- **Walking away once the PR is open.** Stay on it until approved — see
  "After the PRs are open".
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
