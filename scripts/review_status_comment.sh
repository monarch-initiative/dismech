#!/usr/bin/env bash
# Post or update the status comment for one `/review` request (dismech#18311).
#
# Usage: review_status_comment.sh <state>
#   queued     the request was accepted; the run is waiting for a runner
#   refused    the commenter is not allowed to request a review
#   started    the review job is running
#   success    the review job finished and published a verdict
#   failure    the review job finished without publishing a verdict
#   cancelled  the run was cancelled (usually by a newer /review on the PR)
#   skipped    the diff is too large for the review action
#
# One comment per workflow run, found by a hidden marker carrying the run id,
# so the jobs of one run edit the same comment and two runs never collide.
# `queued` never overwrites a comment that already exists, because the review
# job can reach a runner before the acknowledge job does. When a new request
# is accepted, older status comments still saying queued/started are marked
# superseded: the newer run's concurrency group cancelled them, and a run
# cancelled while still queued never gets to update its own comment.
#
# Required env: GH_TOKEN REPO PR_NUMBER RUN_ID
# Optional env: SERVER_URL (default https://github.com), REQUESTER, AUTHOR_ASSOCIATION
#
# Best effort: a failure to post never fails the calling job.
set -uo pipefail

state="${1:?usage: review_status_comment.sh <state>}"
: "${GH_TOKEN:?}" "${REPO:?}" "${PR_NUMBER:?}" "${RUN_ID:?}"
run_url="${SERVER_URL:-https://github.com}/${REPO}/actions/runs/${RUN_ID}"
requester="${REQUESTER:-}"
marker="<!-- claude-review-status run=${RUN_ID} -->"
marker_prefix="<!-- claude-review-status run="

limitation="A \`/review\` run uses \`main\`'s copy of the review workflow and records its check on \`main\`'s commit, so it cannot clear a failing \`claude-review\` check on this PR's own commit. To clear that check, re-run the failed job from the PR's Checks tab."
who=""
[[ -n "$requester" ]] && who=" requested by @${requester}"

case "$state" in
  queued)
    text="🕐 **Review queued.** The \`/review\`${who} was accepted. [The review run](${run_url}) is waiting for a GitHub Actions runner and starts when one is free, which can take a while when CI is busy. This comment will be updated when the review starts and when it finishes.

${limitation}" ;;
  refused)
    text="🚫 **Review not started.** Only repository owners, members and collaborators can request a review with \`/review\`. The comment${who} came from an account with association \`${AUTHOR_ASSOCIATION:-unknown}\`. Ask a maintainer to comment \`/review\` instead." ;;
  started)
    text="⏳ **Review running.** [The review run](${run_url})${who} has started. This comment will be updated when it finishes.

${limitation}" ;;
  success)
    text="✅ **Review finished.** [The review run](${run_url})${who} published its verdict; see the latest review on this PR." ;;
  failure)
    text="❌ **Review failed.** [The review run](${run_url})${who} ended without publishing a verdict. Its summary gives the reason. Comment \`/review\` to try again." ;;
  cancelled)
    text="⚪ **Review cancelled.** [The review run](${run_url})${who} was cancelled before it finished, usually because a newer \`/review\` on this PR replaced it." ;;
  skipped)
    text="⚠️ **Review skipped.** [The review run](${run_url})${who} found the diff too large for the review action. See the notice on this PR; it needs a human review." ;;
  *)
    echo "::warning::review_status_comment.sh: unknown state '${state}'" >&2
    exit 0 ;;
esac
body="${marker}
${text}"

comments="$(gh api --paginate "repos/${REPO}/issues/${PR_NUMBER}/comments" \
  --jq '.[] | select(.body | startswith("<!-- claude-review-status run=")) | "\(.id)\t\(.body | split("\n")[0])\t\(.body | split("\n")[1] // "")"')" || {
  echo "::warning::Could not list comments on PR #${PR_NUMBER}; status comment not updated." >&2
  exit 0
}

existing=""
while IFS=$'\t' read -r id first_line second_line; do
  [[ -z "${id:-}" ]] && continue
  if [[ "$first_line" == "$marker" ]]; then
    existing="$id"
  elif [[ "$state" == "queued" || "$state" == "started" ]] \
       && [[ "$first_line" == "$marker_prefix"* ]] \
       && [[ "$second_line" == "🕐 "* || "$second_line" == "⏳ "* ]]; then
    old_run="${first_line#"$marker_prefix"}"; old_run="${old_run%" -->"}"
    if [[ "$old_run" =~ ^[0-9]+$ && "$old_run" -lt "$RUN_ID" ]]; then
      gh api -X PATCH "repos/${REPO}/issues/comments/${id}" -f body="${first_line}
⚪ **Review superseded.** A newer \`/review\` on this PR replaced this request; see the newest status comment." >/dev/null \
        || echo "::warning::Could not mark status comment ${id} superseded." >&2
    fi
  fi
done <<< "$comments"

if [[ -n "$existing" ]]; then
  if [[ "$state" == "queued" ]]; then
    echo "Status comment ${existing} already exists for run ${RUN_ID}; leaving it as is."
    exit 0
  fi
  gh api -X PATCH "repos/${REPO}/issues/comments/${existing}" -f body="$body" >/dev/null \
    && echo "Updated status comment ${existing}: ${state}" \
    || echo "::warning::Could not update status comment ${existing}." >&2
else
  gh api -X POST "repos/${REPO}/issues/${PR_NUMBER}/comments" -f body="$body" >/dev/null \
    && echo "Posted status comment: ${state}" \
    || echo "::warning::Could not post a status comment on PR #${PR_NUMBER}." >&2
fi
exit 0
