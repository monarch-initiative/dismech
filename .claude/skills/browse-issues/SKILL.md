---
name: browse-issues
description: Use when the user wants to browse the open dismech issues that already exist, of any kind (claims, lit/kgap/preprint scans, genetics passes, evidence reviews, curation follow-ups, schema, tooling, bugs, docs, unlabelled), and choose for themselves what to work on - filtering, searching or shortlisting them by author, assignee, lane, effort, PR state, or text in the title, body or comments, finding issues ready for cleanup, and then opening one issue they name as its own interactive Claude Code session in a tmux window. The listing is deterministic, from one snapshot with fixed rules and a reason code for every exclusion; the user does the choosing.
---

# browse-issues

This session is the **sorting session**: the user browses the open issues
here and decides what to work on. It lists and filters; it does not choose.
When the user names an issue, it opens that issue as a **separate, interactive Claude Code
session** in its own worktree and tmux window. The sorting session never does
the issue's work itself and never launches a session the user did not ask for.

| Recipe | Does | Changes anything? |
|---|---|---|
| `just select-issues` | deterministic shortlist over one snapshot | no |
| `just issue-prs N…` | the PRs attached to each issue, with state and relation | no |
| `just check-issue-lanes` | repository labels no lane rule reads | no |
| `just launch-issue-session N` | assign → worktree → tmux window running `claude` | yes; `--dry-run` shows it first |

The code is `src/dismech/issue_queue/`; the rules are pure functions tested in
`tests/test_issue_queue.py`.

## When to use this, and when not

| The user wants | Use |
|---|---|
| a new disease to curate, from the stub queue | `claim-disease` (files the claim issue) |
| a batch of their own assigned claim issues curated in parallel subagents | `curate-next` |
| one named disease curated now | `/curate <name>` |
| several agents in tmux, coordinated and monitored | `boss` |
| to sort, search or clean up **existing** issues of any kind, and open one as a session they drive | this skill |

This skill never files an issue, never reads `stubs/`, and never files,
retitles or reassigns a claim. `just check-claims` stays the authority on
claims; the selector reads claims through the same code
(`dismech.stubs.claims`), so the two cannot disagree about what a claim is.

## 1. Sort (read-only)

Run from the repo root:

```bash
just select-issues N [--author me] [--lane a,b] [--effort x,y] [--grep TEXT]
```

- **N**, 1–8, *or* `--list`. N picks the next few; `--list` shows every
  issue that passes the filters, still in rank order, plus a separate section
  for matched discussions, which cannot be launched. Use `--list` for "show me
  all my issues …", "review the titles of …"; use N for "what should I do
  next". If the user gave neither and the request does not say which, ask; do
  not default N.
- `--above M` / `--below M`: only issue numbers strictly above / below M.
- `--author me`: issues the current GitHub user opened, available when
  unassigned **or** assigned to them. Assigned to anyone else is their hold,
  whoever opened it.
- `--mine`: only issues assigned to the current user and nobody else
  (`NOT_MINE` otherwise). `curate-next` shortlists with `--mine --lane
  new-entry`.
- `--lane`: `new-entry`, `lit-scan`, `kgap-scan`, `preprint-scan`,
  `genetics-pass`, `evidence-review`, `entry-review`, `curation`, `schema`,
  `tooling`, `bug`, `docs`, `general`. Default all. `general` is the
  catch-all for issues no other rule places, so an issue labelled only
  `enhancement`, or nothing, is still offered.
- `--effort`: `low`, `medium`, `high`, `very-hard`, `unlabelled`. Default all.
  The curation-scanner treats unlabelled curation as high; to match it, pass
  `high,unlabelled`.
- `--grep TEXT`: only issues whose title or body contains TEXT, as a plain,
  case-insensitive substring (no regex, no word matching; one term per run).
  Offline, from the snapshot. Each listed issue says where it matched
  (`[text in title]` / `[text in body]`).
- `--grep-comments` (with `--grep`): also accept a match in the issue's
  comments. Comments are not in the snapshot, so they are read live, in
  batches of 25, and only for issues that passed every other filter; narrow
  with `--author`, `--lane` or a number range first if the run is slow.
  `--from` does not freeze comment matches. Never replace this with GitHub's
  `in:comments` search: its index lags and it matches words, not substrings.
- `--prs MODE`: which PRs hide an issue. An issue can need several PRs, so
  there is no single right rule; the mode is the user's choice, and every
  listed issue shows its PRs (`#N state/relation`) whatever the mode:

  | Mode | Hides an issue when | Code | Use for |
  |---|---|---|---|
  | `active` (default) | an **open** PR will close it or is linked to it | `PR_ACTIVE` | "what is free to pick up" |
  | `any-open` | any open PR, even one that only mentions it | `PR_OPEN` | being cautious about stepping on open work |
  | `none` (alias `--no-prs`) | any PR at all, any state or relation | `ANY_PR` | "issues nobody has touched" |
  | `ignore` | never | — | a full census with PR history |
  | `finished` | it has **no** PR, or **any open** PR | `NO_PR`, `PR_OPEN` | cleanup: only issues whose every PR is merged or closed |

  `finished` keeps only issues with PR history and nothing in flight, checks
  discussions too (cleanup is not launching), and tags each candidate,
  strongest first: `MERGED_CLOSES`, `MERGED_MENTIONS`, `ABANDONED`. For
  cleanup, fetch a fresh snapshot (no `--from`).

  A cleanup candidate is a question, not a conclusion. Read the issue and its
  PRs, then tell the user which look done (draft a closing comment naming the
  PRs that did it), which have work left (say what), and which are unclear.
  Never close an issue or post the comment without the user's go-ahead.

  Relations: `closes` (will close it on merge), `linked` (Development
  sidebar), `mentions` (cites `#N` without closing). States: `open`,
  `merged`, `closed` (unmerged).

Map the user's words to flags: "my low-effort scan issues" → `--author me
--lane lit-scan,kgap-scan,preprint-scan --effort low`; "everything I filed
since #14000, grouped by effort" → `--list --author me --above 14000`, then the
effort-grouping step below; "my issues whose PRs are all closed" → `--list
--author me --prs finished`; "issues that mention references_cache, including
in comments" → `--list --grep references_cache --grep-comments`. If the user
asks for a lane or tier the selector lacks, say so rather than approximating.

How the selector decides, so you can explain a result:

1. One `gh issue list` writes `tmp/issues.json` (gitignored); everything after
   reads it. `--from tmp/issues.json` re-reads the same snapshot, so a re-sort
   with different filters is over the same issues. A re-read snapshot goes
   stale: the selector prints its age, and issues opened, closed or reassigned
   since are not reflected. Fetch fresh before acting on an old one.
2. Each issue gets one lane, by the first rule that matches (`LANE_RULES` in
   `rules.py`): evidence-review labels; a claim (`claim` label, or a title
   `Curate <label> (MONDO:NNNNNNN)`); the scan title prefixes, kept in one
   table (`TITLE_PREFIXES`); genetics pass; discussion (labels, or a title
   starting `Proposal:` or `Decide `), checked before curation so a question is
   never offered as work; entry review (`Review …`); curation; schema; tooling;
   bug; docs; and `general` for the rest.
3. Offline exclusions in fixed order, first hit recorded: `DISPOSITIONED`,
   `NUMBER_RANGE`, `AUTHOR`, `ASSIGNED_OTHER`, `NOT_MINE`, `NON_ACTIONABLE`,
   `LANE_EXCLUDED`, `MULTI_EFFORT`, `EFFORT_EXCLUDED`, `TEXT_NO_MATCH`.
4. Rank: `high-priority` first, `low-priority` last, then oldest issue number.
   Nothing else.
5. Live vetoes, in rank order, batched: the `--prs` mode's code (from GitHub's
   own link and cross-reference records, never the `#N` text search, which
   matches `ORPHA:N`), and for claims `KB_COVERED` / `OPEN_PR`, for scan lanes
   `TARGET_MISSING`. `KB_COVERED` uses the coverage index `tidy-stubs` uses,
   so a MONDO ID named only in a sibling entry's `differential_diagnoses` does
   not count. It reads the local `kb/`; if the selector prints a NOTE that the
   checkout is behind `origin/main`, pass that on.
6. First N are the picks (or, with `--list`, all of them); fewer than N →
   `SHORTFALL`, never padded.

A claim issue can carry a note, shown beside it and never used to hide it:
`DOUBLE_CLAIM` (another open claim has the same MONDO ID), `UNKEYED_CLAIM` (a
`Curate …` claim with no MONDO ID, so it locks nothing) or `UNLABELLED_CLAIM`
(a claim-shaped title without the `claim` label, which `check-claims` cannot
see). Pass these on; fixing them is the claim owner's job.

Each run ends with how many issues landed in `general`. If that number jumps,
`just check-issue-lanes` lists the labels no rule reads; a new workflow label
that should route issues belongs in `LANE_LABELS` in `rules.py`.

### Reading an issue that already has PRs

A PR line is a fact to read, not a verdict. When presenting the list, call
out the listed issues that carry PRs and say what each pattern usually means,
without deciding for the user:

- **`merged/closes` and the issue is still open**: GitHub normally closes
  the issue on merge, so either it was reopened because work remains, or it
  closed after the snapshot. Check its state and last comments first.
- **`merged/mentions` only**: earlier work touched it, possibly a first
  installment, possibly a passing citation. Only the PR body or the issue
  thread says which.
- **`open/mentions`**: someone's open PR cites it. Not a hold, but worth a
  look so two PRs do not collide.
- **`closed/…`**: an abandoned attempt. Often useful to read, rarely a reason
  to skip.

### Optional: group by estimated effort

When the user asks for issues grouped by effort ("which are the easy ones"),
the labels are not enough: most hand-filed issues carry no effort label. After
the selector has run, read the body of each **launchable** issue from the
snapshot, not a fresh fetch:

```bash
jq -r '.[] | select(.number == 13789) | .body' tmp/issues.json
```

and place each in one of three groups:

| Group | Meaning |
|---|---|
| **Small** | one sitting: a few-line code or doc fix, or one bounded edit to one KB entry whose evidence is already in hand |
| **Medium** | about a day: several entries, a new report-only recipe, or re-reading sources to reconcile claims |
| **Large** | multi-session: a schema change with migration, new disease curation, wide promotion across many entries, or anything blocked on another issue |

Give each issue one line saying *why* it lands there, naming the concrete work.
For an issue with merged PRs, estimate the **remaining** work and say so. Say
plainly that this grouping is your estimate from the issue text: it does not
re-order, add, or drop issues, and an issue's effort **label** wins if the user
asks for the labelled tier. Point out where your estimate and a label disagree.
List the vetoed and not-launchable issues after the groups, with their reason.

Show the user the picks, the "vetoed by a live check" list, and the top of
"next in line". Then **stop and wait**. Do not assign, and do not offer to
launch all of them; ask which, if any, they want opened.

Do not re-rank by hand. If a pick looks wrong for a reason the selector cannot
see, say which and why, and let the user veto it or re-sort with a filter.

## 2. Launch, only on the user's word, one issue at a time

When the user names an issue ("open #14182", "launch the second one"), show
the dry run first unless they have already said to go ahead:

```bash
just launch-issue-session <N> --dry-run [--model opus|sonnet] [--note "<the user's instructions>"]
```

then, on the user's confirmation, the same command without `--dry-run`.

If the user says what the session should do with the issue ("open #13148, only
fix the error message, leave the retry logic alone"), pass their words with
`--note`, close to verbatim. It is appended to the first prompt and stated to
take precedence over the issue text where they conflict. Do not add your own
instructions to it. The note goes only to the new session; it is never posted
to the issue. The launcher:

1. checks that `gh`, `git`, `tmux` and `claude` are installed, before changing
   anything;
2. re-reads the issue live, and refuses one that is closed, assigned to
   someone else, or a discussion;
3. assigns it to the user running it, and says so: the curation-scanner only
   picks up unassigned issues, so this takes the issue out of its pool;
4. creates `<worktree-root>/dismech-issue-<N>` on branch `issue-<N>-<slug>`
   off `origin/main`, outside the repo and separate from this session's
   checkout;
5. opens tmux window `issue-<N>` running `claude` interactively there, with a
   short first prompt: the issue, read it and its comments, the lane's
   one-line hint, open one PR with `Closes #<N>`, ask before guessing. The new
   session inherits CLAUDE.md and every project skill, so the prompt does not
   restate SOPs.

Location and names are configurable, by flag or environment variable:
`--worktree-root` / `DISMECH_WORKTREE_ROOT` (default `~/worktrees`),
`--tmux-session` / `DISMECH_TMUX_SESSION` (default `dismech-issues`),
`--claude-bin` / `DISMECH_CLAUDE_BIN` (default `claude`). Without tmux there is
no launcher; create a worktree and start a session by hand.

The prompt is the `claude` command's argument; nothing is typed into a running
session. One launch per instruction: "open the first three" is three runs, but
only because the user asked for three.

Tell the user how to reach it:

```
tmux attach -t dismech-issues     # Ctrl-b w lists windows, Ctrl-b d detaches
```

The new session is the user's to drive. The sorting session does not monitor
it, send it instructions, or report on its PR unless asked.

## Afterwards

When an issue's PR has merged, its worktree and branch can go:
`git worktree remove <worktree-root>/dismech-issue-<N>` and
`git branch -d issue-<N>-<slug>`. A launch refuses if the worktree path already
exists, and says how to reattach.

## Common mistakes

- **Launching without being told which issue.** Shortlisting is not consent to
  start work. Wait for the user to name one.
- **Doing the issue's work in the sorting session.** It sorts and launches;
  the work happens in the launched session.
- **Launching an `ASSIGNED_OTHER` issue** by editing assignees first. The
  launcher refuses for a reason; stale holds are a question for the assignee.
- **Re-sorting without `--from`** while discussing a shortlist: a fresh fetch
  can reorder it under the user.
- **`tmux send-keys` to steer a launched session.** Not this skill's job; if
  the user wants orchestration, that is `boss`.
- **`gh pr list --search "closes #N"`** for linked PRs: it matches `ORPHA:N`.
  `just issue-prs N` is the check.
