// Lifecycle companion to Anthropic's five-search + verification dedupe pattern.
// The model supplies candidates; only this deterministic code writes to GitHub.
const { createHash } = require('node:crypto');

const MARKER = 'dismech-duplicate:v1';
const PENDING_LABEL = 'duplicate-pending';
const GRACE_MS = 3 * 24 * 60 * 60 * 1000;
// Native duplicate linkage (duplicate_issue_id) requires this API version.
const API_HEADERS = { 'X-GitHub-Api-Version': '2026-03-10' };

function fingerprint(issue) {
  return createHash('sha256').update(JSON.stringify([issue.title, issue.body])).digest('hex');
}

function isHuman(user) {
  // Missing/deleted identities count as human: uncertainty must prevent closure.
  return user?.type !== 'Bot' && !user?.login?.endsWith('[bot]');
}

function lastHumanComment(comments) {
  return Math.max(0, ...comments.filter(comment => isHuman(comment.user)).map(comment => comment.id));
}

function isPending(issue) {
  return issue.labels?.some(label => (label.name || label) === PENDING_LABEL);
}

async function ensurePendingLabel(github, repo) {
  try {
    await github.rest.issues.getLabel({ ...repo, name: PENDING_LABEL });
  } catch (error) {
    if (error.status !== 404) throw error;
    try {
      await github.rest.issues.createLabel({
        ...repo, name: PENDING_LABEL, color: 'fbca04',
        description: 'Potential duplicate awaiting the three-day objection window',
      });
    } catch (creationError) {
      // Another issue's workflow may have created it in the meantime.
      if (creationError.status !== 422) throw creationError;
      await github.rest.issues.getLabel({ ...repo, name: PENDING_LABEL });
    }
  }
}

function proposal(comment) {
  if (comment.user?.login !== 'github-actions[bot]' || comment.user?.type !== 'Bot') return null;
  const match = comment.body?.match(/^<!-- dismech-duplicate:v1 (\{[^\n]+\}) -->$/m);
  if (!match) return null;
  try {
    const data = JSON.parse(match[1]);
    if (!Number.isSafeInteger(data.canonical) || data.canonical < 1 ||
        !/^[a-f0-9]{64}$/.test(data.fingerprint)) return null;
    return { ...data, comment };
  } catch {
    return null;
  }
}

async function commentsFor(github, repo, number) {
  return github.paginate(github.rest.issues.listComments, {
    ...repo, issue_number: number, per_page: 100,
  });
}

async function getIssue(github, repo, number) {
  return (await github.rest.issues.get({ ...repo, issue_number: number })).data;
}

async function prepareSearch(github, repo, value) {
  if (!/^[1-9][0-9]*$/.test(String(value)) || !Number.isSafeInteger(Number(value))) {
    throw new Error('Issue number must be a positive integer');
  }
  const issue = await getIssue(github, repo, Number(value));
  if (issue.state !== 'open' || issue.pull_request || issue.locked) return null;
  const comments = await commentsFor(github, repo, issue.number);
  if (comments.some(proposal)) return null;
  return { number: issue.number, fingerprint: fingerprint(issue), lastHumanComment: lastHumanComment(comments) };
}

function validateCandidates(result, number) {
  if (!Number.isSafeInteger(number) || number < 1 || !Array.isArray(result?.duplicates) ||
      result.duplicates.length > 3) throw new Error('Invalid duplicate results');
  const seen = new Set();
  const valid = [];
  for (const item of result.duplicates) {
    if (!Number.isSafeInteger(item?.number) || item.number < 1 || item.number >= number ||
        seen.has(item.number) || typeof item.reason !== 'string' ||
        !item.reason.trim() || item.reason.length > 1000) {
      // Plausible model mistakes should not discard other usable matches.
      continue;
    }
    seen.add(item.number);
    valid.push(item);
  }
  return valid.sort((a, b) => a.number - b.number);
}

function plainReason(reason) {
  // Keep model text in a single paragraph and prevent mentions/HTML instructions.
  return reason.replace(/\s+/g, ' ').trim().replace(/@/g, '@\u200b')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

async function proposeDuplicates(github, repo, { number, fingerprint: original, lastHumanComment: lastHuman, result }) {
  const candidates = validateCandidates(result, number);
  if (!candidates.length) return false;
  if (!Number.isSafeInteger(lastHuman) || lastHuman < 0) throw new Error('Missing discussion snapshot');
  const issue = await getIssue(github, repo, number);
  if (issue.state !== 'open' || issue.pull_request || issue.locked ||
      fingerprint(issue) !== original) return false;
  const valid = [];
  for (const item of candidates) {
    const target = await getIssue(github, repo, item.number);
    if (target.state === 'open' && !target.pull_request) valid.push(item);
  }
  if (!valid.length) return false;
  // A rerun must not post twice or restart an objection window.
  const comments = await commentsFor(github, repo, number);
  if (comments.some(proposal) || lastHumanComment(comments) !== lastHuman) return false;
  const canonical = valid[0].number;
  const body = [
    `This appears to duplicate work already tracked in #${canonical}.`,
    '',
    ...valid.map(item => `- #${item.number}: ${plainReason(item.reason)}`),
    '',
    `This issue will be closed as a duplicate of #${canonical} after three days.`,
    'To keep it open, add a comment explaining the difference or react 👎 to this notice. '
      + 'Any human reply or 👎 reaction stops automatic closure; automated replies do not.',
    'Maintainers can also remove the `duplicate-pending` label to keep it open.',
    '',
    `<!-- ${MARKER} ${JSON.stringify({ canonical, fingerprint: original })} -->`,
  ].join('\n');
  await ensurePendingLabel(github, repo);
  const notice = await github.rest.issues.createComment({ ...repo, issue_number: number, body });
  try {
    // Add, never replace, the labels managed by the existing triage workflow.
    await github.rest.issues.addLabels({ ...repo, issue_number: number, labels: [PENDING_LABEL] });
  } catch (error) {
    // A notice without its queue label would promise closure that cannot run.
    // Remove it so a retry can publish a complete proposal.
    await github.rest.issues.deleteComment({ ...repo, comment_id: notice.data.id });
    throw error;
  }
  return true;
}

async function assessDuplicate(github, repo, issue, now) {
  if (!isPending(issue) || issue.pull_request) return { status: 'skip' };
  if (issue.state !== 'open') return { status: 'cancelled', reason: 'issue is closed' };
  const comments = await commentsFor(github, repo, issue.number);
  const proposals = comments.map(proposal).filter(Boolean);
  // Ambiguous/multiple notices require human review, not a guessed deadline.
  if (proposals.length !== 1) return { status: 'cancelled', reason: 'missing or ambiguous notice' };
  const pending = proposals[0];
  const since = Date.parse(pending.comment.created_at);
  if (!Number.isFinite(since) || pending.canonical >= issue.number) {
    return { status: 'cancelled', reason: 'invalid notice' };
  }
  if (fingerprint(issue) !== pending.fingerprint) return { status: 'cancelled', reason: 'issue was edited' };
  if (comments.some(comment => comment.id > pending.comment.id && isHuman(comment.user))) {
    return { status: 'cancelled', reason: 'human reply' };
  }
  const reactions = await github.paginate(github.rest.reactions.listForIssueComment, {
    ...repo, comment_id: pending.comment.id, per_page: 100,
  });
  if (reactions.some(reaction => reaction.content === '-1' && isHuman(reaction.user))) {
    return { status: 'cancelled', reason: 'human thumbs-down' };
  }
  const events = await github.paginate(github.rest.issues.listEventsForTimeline, {
    ...repo, issue_number: issue.number, per_page: 100,
  });
  if (events.some(event => event.event === 'reopened' && Date.parse(event.created_at) >= since)) {
    return { status: 'cancelled', reason: 'issue was reopened' };
  }
  // Objections are cleaned up even while the three-day window is still open.
  if (issue.locked || now - since < GRACE_MS) return { status: 'waiting' };
  const target = await getIssue(github, repo, pending.canonical);
  if (target.state !== 'open' || target.pull_request) {
    return { status: 'cancelled', reason: 'canonical issue is no longer open' };
  }
  return { status: 'eligible', target };
}

async function removePendingLabel(github, repo, number) {
  try {
    await github.rest.issues.removeLabel({ ...repo, issue_number: number, name: PENDING_LABEL });
  } catch (error) {
    // Another actor may have removed it since our last read.
    if (error.status !== 404) throw error;
  }
}

async function closeDuplicates(github, repo, {
  dryRun = true, maxClosures = 5, now = Date.now(), log = console.log, warn = console.warn,
} = {}) {
  if (!Number.isSafeInteger(maxClosures) || maxClosures < 1 || maxClosures > 50) {
    throw new Error('maxClosures must be an integer between 1 and 50');
  }
  const issues = await github.paginate(github.rest.issues.listForRepo, {
    ...repo, state: 'open', labels: PENDING_LABEL, per_page: 100,
  });
  let count = 0;
  let attempts = 0;
  for (const listed of issues) {
    try {
      const decision = await assessDuplicate(github, repo, listed, now);
      if (decision.status === 'skip' || decision.status === 'waiting') continue;
      // Re-read the issue and vetoes before either closure or queue cleanup.
      const current = await getIssue(github, repo, listed.number);
      const confirmed = await assessDuplicate(github, repo, current, now);
      if (confirmed.status === 'cancelled') {
        log(`${dryRun ? 'Would remove' : 'Removing'} ${PENDING_LABEL} from #${current.number}: ${confirmed.reason}`);
        if (!dryRun) await removePendingLabel(github, repo, current.number);
        continue;
      }
      if (decision.status !== 'eligible' || confirmed.status !== 'eligible' ||
          confirmed.target.id !== decision.target.id) continue;
      if (attempts >= maxClosures) {
        log(`Deferring #${current.number}: closure budget of ${maxClosures} reached`);
        continue;
      }
      // Count attempts, including uncertain API failures, to bound mutations.
      attempts += 1;
      log(`${dryRun ? 'Would close' : 'Closing'} #${current.number} as duplicate of #${confirmed.target.number}`);
      if (!dryRun) {
        await github.rest.issues.update({
          ...repo, issue_number: current.number, state: 'closed',
          state_reason: 'duplicate', duplicate_issue_id: confirmed.target.id,
          headers: API_HEADERS,
        });
      }
      count += 1;
      if (!dryRun) await removePendingLabel(github, repo, current.number);
    } catch (error) {
      warn(`Duplicate sweep failed for #${listed.number}: ${error.message}`);
    }
  }
  log(`${dryRun ? 'Would close' : 'Closed'} duplicates: ${count}`);
  return count;
}

module.exports = { fingerprint, prepareSearch, proposeDuplicates, assessDuplicate, closeDuplicates };
