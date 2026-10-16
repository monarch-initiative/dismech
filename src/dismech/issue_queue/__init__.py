"""Deterministic triage of the open GitHub issues that already exist.

`dismech.stubs` answers "what is left to curate" from the stub queue, and
`dismech.stubs.claims` answers "who is curating what" from `claim` issues. This
package answers the third question: of the ~1,200 open issues of every kind
(scan follow-ups, evidence reviews, schema, tooling, bugs, docs, and the many
hand-filed issues with no label), which can the current user pick up, and has
anyone already started?

- :mod:`.rules` -- pure functions: lane classification, the fixed-order
  exclusions, the ranking, and what a PR history means. No network, no git;
  everything here is tested against a fixture snapshot.
- :mod:`.github` -- the GitHub reads: one issue snapshot, PR linkage from the
  timeline and closing references (never the `#N` text search, which matches
  `ORPHA:N`), and issue comments for `--grep-comments`.
- :mod:`.cli` -- `just select-issues`, `just issue-prs`, `just check-issue-lanes`.
- :mod:`.launch` -- `just launch-issue-session`: one named issue as its own
  interactive Claude Code session in a worktree and a tmux window.

Used by the `next-issues` skill; `issue-prs` is also what `curate-next` uses
for its PR check.
"""
