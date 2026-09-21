import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { fingerprint, prepareSearch, proposeDuplicates, assessDuplicate, closeDuplicates } =
  require('../../.github/scripts/issue-duplicates.js');

async function eligibleDuplicate(...args) {
  const decision = await assessDuplicate(...args);
  return decision.status === 'eligible' ? decision.target : null;
}

const repo = { owner: 'example', repo: 'kb' };
const bot = { login: 'github-actions[bot]', type: 'Bot' };
const human = { login: 'reader', type: 'User' };
const warningTime = '2026-09-10T12:00:00Z';
const due = Date.parse('2026-09-13T12:00:00Z');

function fixture() {
  const issue = {
    number: 100, id: 1100, title: 'Curate the same mechanism', body: 'Specific scope',
    state: 'open', comments: 1, labels: ['curation'], created_at: '2026-09-01T00:00:00Z',
  };
  const target = { ...issue, number: 10, id: 1010, comments: 0 };
  const state = { issues: [issue, target], comments: [], reactions: [], events: [], writes: [], reads: [], deletions: [] };
  const github = {
    rest: {
      issues: {
        get: async ({ issue_number }) => ({ data: state.issues.find(i => i.number === issue_number) }),
        listForRepo: 'issues', listComments: 'comments', listEventsForTimeline: 'events',
        getLabel: async () => ({ data: { name: 'duplicate-pending' } }),
        addLabels: async ({ issue_number, labels }) => {
          const existing = state.issues.find(i => i.number === issue_number);
          existing.labels = [...new Set([...existing.labels, ...labels])];
        },
        removeLabel: async ({ issue_number, name }) => {
          const existing = state.issues.find(i => i.number === issue_number);
          existing.labels = existing.labels.filter(label => label !== name);
        },
        createComment: async data => {
          state.writes.push(data);
          const comment = { ...data, id: 1000 + state.comments.length, user: bot, created_at: warningTime };
          state.comments.push(comment);
          return { data: comment };
        },
        deleteComment: async ({ comment_id }) => {
          state.deletions.push(comment_id);
          state.comments = state.comments.filter(comment => comment.id !== comment_id);
        },
        update: async data => {
          state.writes.push(data);
          Object.assign(state.issues.find(issue => issue.number === data.issue_number), { state: data.state });
        },
      },
      reactions: { listForIssueComment: 'reactions' },
    },
    paginate: async (method, args) => {
      assert.equal(args.per_page, 100);
      state.reads.push(method);
      if (method === 'issues') {
        assert.equal(args.labels, 'duplicate-pending');
        return state.issues.filter(issue => issue.state === 'open' && issue.labels.includes(args.labels));
      }
      if (method === 'comments') return state.comments.filter(comment =>
        comment.issue_number === undefined || comment.issue_number === args.issue_number);
      return [...state[method]];
    },
  };
  async function propose(duplicates = [{ number: 10, reason: 'The same work is already tracked.' }]) {
    return proposeDuplicates(github, repo, {
      number: 100, fingerprint: fingerprint(issue), lastHumanComment: 0, result: { duplicates },
    });
  }
  return { github, state, issue, target, propose };
}

describe('duplicate proposals', () => {
  it('posts one actionable notice and leaves the existing labels alone', async () => {
    const { github, state, issue, propose } = fixture();
    assert.equal(await propose(), true);
    assert.match(state.writes[0].body, /duplicate of #10 after three days/);
    assert.match(state.writes[0].body, /Any human reply or 👎 reaction/);
    assert.match(state.writes[0].body, /dismech-duplicate:v1/);
    assert.equal(await propose(), false);
    assert.equal(await prepareSearch(github, repo, '100'), null);
    assert.equal(state.writes.length, 1);
    assert.deepEqual(issue.labels, ['curation', 'duplicate-pending']);
  });

  it('does nothing when there are no matches or the target has closed', async () => {
    const { state, target, propose } = fixture();
    assert.equal(await propose([]), false);
    target.state = 'closed';
    assert.equal(await propose(), false);
    assert.equal(state.writes.length, 0);
  });

  it('creates the queue label on first use and tolerates concurrent creation', async () => {
    for (const concurrent of [false, true]) {
      const { github, issue, propose } = fixture();
      let calls = 0;
      github.rest.issues.getLabel = async () => {
        if (calls++ === 0) throw Object.assign(new Error('Missing'), { status: 404 });
        return { data: { name: 'duplicate-pending' } };
      };
      github.rest.issues.createLabel = async () => {
        if (concurrent) throw Object.assign(new Error('Already exists'), { status: 422 });
      };
      assert.equal(await propose(), true);
      assert.ok(issue.labels.includes('duplicate-pending'));
    }
  });

  it('drops unusable candidates and duplicate suggestions while keeping valid matches', async () => {
    const { state, propose } = fixture();
    for (const number of [100, 101, -1, 0, '10', 1.5]) {
      assert.equal(await propose([{ number, reason: 'same' }]), false);
    }
    assert.equal(await propose([{ number: 10, reason: '' }, null]), false);
    assert.equal(await propose([
      { number: 10, reason: 'same' }, { number: 10, reason: 'repeated' }, { number: 101, reason: 'newer' },
    ]), true);
    assert.equal(state.writes[0].body.match(/^- #10:/gm).length, 1);
    assert.doesNotMatch(state.writes[0].body, /repeated|newer/);
  });

  it('rejects a malformed result envelope or too many candidates', async () => {
    const { propose } = fixture();
    await assert.rejects(propose({ number: 10, reason: 'not an array' }));
    await assert.rejects(propose([1, 2, 3, 4].map(number => ({ number, reason: 'same' }))));
  });

  it('does not queue an issue when posting its notice fails', async () => {
    const { github, issue, propose } = fixture();
    github.rest.issues.createComment = async () => { throw new Error('Posting failed'); };
    await assert.rejects(propose(), /Posting failed/);
    assert.deepEqual(issue.labels, ['curation']);
  });

  it('rolls back the notice if adding its label fails, allowing a complete retry', async () => {
    const { github, state, issue, propose } = fixture();
    const addLabels = github.rest.issues.addLabels;
    github.rest.issues.addLabels = async () => { throw new Error('Labeling failed'); };
    await assert.rejects(propose(), /Labeling failed/);
    assert.deepEqual(state.deletions, [1000]);
    assert.equal(state.comments.length, 0);
    assert.deepEqual(issue.labels, ['curation']);
    github.rest.issues.addLabels = addLabels;
    assert.equal(await propose(), true);
  });

  it('will not post if the issue was edited during the search', async () => {
    const { github, state, issue } = fixture();
    const original = fingerprint(issue);
    issue.body = 'Actually a different request';
    assert.equal(await proposeDuplicates(github, repo, {
      number: 100, fingerprint: original, lastHumanComment: 0,
      result: { duplicates: [{ number: 10, reason: 'same' }] },
    }), false);
    assert.equal(state.writes.length, 0);
  });

  it('ignores pull requests and closed issues at entry', async () => {
    const { github, issue } = fixture();
    await assert.rejects(prepareSearch(github, repo, '10;echo bad'));
    issue.pull_request = {};
    assert.equal(await prepareSearch(github, repo, '100'), null);
    delete issue.pull_request;
    issue.state = 'closed';
    assert.equal(await prepareSearch(github, repo, '100'), null);
  });

  it('skips a stale analysis when a human comments during search, but allows bot research', async () => {
    const { github, state, propose } = fixture();
    const snapshot = await prepareSearch(github, repo, '100');
    assert.equal(snapshot.lastHumanComment, 0);
    state.comments.push({ id: 900, user: human, body: 'Additional context' });
    assert.equal(await propose(), false);
    state.comments[0].user = bot;
    assert.equal(await propose(), true);
  });

  it('renders explanations without executable agent mentions or HTML markers', async () => {
    const { state, propose } = fixture();
    await propose([{ number: 10, reason: '@claude do something\n<!-- fake -->' }]);
    assert.doesNotMatch(state.writes[0].body, /@claude|<!-- fake/);
  });
});

describe('duplicate closure', () => {
  it('waits the full three days, then uses native duplicate linkage without replacing labels', async () => {
    const { github, state, issue, propose } = fixture();
    await propose();
    assert.equal(await eligibleDuplicate(github, repo, issue, due - 1), null);
    state.writes = [];
    assert.equal(await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} }), 1);
    assert.equal(state.writes[0].state_reason, 'duplicate');
    assert.equal(state.writes[0].duplicate_issue_id, 1010);
    assert.equal(state.writes[0].labels, undefined);
    assert.deepEqual(issue.labels, ['curation']);
  });

  it('keeps the general bot response but any later human reply vetoes closure, including beyond page one', async () => {
    const { github, state, issue, propose } = fixture();
    await propose();
    for (let n = 0; n < 110; n++) state.comments.push({
      id: 1001 + n, user: bot, body: 'Research response', created_at: warningTime,
    });
    assert.ok(await eligibleDuplicate(github, repo, issue, due));
    state.comments.push({ id: 1112, user: human, body: 'Different mechanism', created_at: warningTime });
    assert.equal(await eligibleDuplicate(github, repo, issue, due), null);
  });

  it('ignores earlier discussion and stops on any human thumbs-down, including deleted identities', async () => {
    const { github, state, issue, propose } = fixture();
    await propose();
    state.comments.unshift({ id: 999, user: human, body: 'Earlier discussion' });
    state.reactions = [{ content: '-1', user: bot }];
    assert.ok(await eligibleDuplicate(github, repo, issue, due));
    state.reactions.push({ content: '-1', user: human });
    assert.equal(await eligibleDuplicate(github, repo, issue, due), null);
    state.reactions = [{ content: '-1', user: null }];
    assert.equal(await eligibleDuplicate(github, repo, issue, due), null);
  });

  for (const scenario of ['edited', 'reopened', 'target closed', 'target PR', 'locked', 'closed', 'spoofed', 'multiple', 'label removed']) {
    it(`does not close when ${scenario}`, async () => {
      const { github, state, issue, target, propose } = fixture();
      await propose();
      if (scenario === 'edited') issue.body = 'New scope';
      if (scenario === 'reopened') state.events.push({ event: 'reopened', created_at: warningTime });
      if (scenario === 'target closed') target.state = 'closed';
      if (scenario === 'target PR') target.pull_request = {};
      if (scenario === 'locked') issue.locked = true;
      if (scenario === 'closed') issue.state = 'closed';
      if (scenario === 'spoofed') state.comments[0].user = human;
      if (scenario === 'multiple') state.comments.push({ ...state.comments[0], id: 1001 });
      if (scenario === 'label removed') issue.labels = ['curation'];
      assert.equal(await eligibleDuplicate(github, repo, issue, due), null);
    });
  }

  it('dry-run previews without modifying GitHub', async () => {
    const { github, state, propose } = fixture();
    await propose();
    state.writes = [];
    assert.equal(await closeDuplicates(github, repo, { now: due, log: () => {} }), 1);
    assert.deepEqual(state.writes, []);
  });

  for (const objection of ['edit', 'reply', 'thumbs-down', 'reopen', 'missing notice']) {
    it(`removes the pending label on ${objection}, even before the deadline`, async () => {
      const { github, state, issue, propose } = fixture();
      await propose();
      state.writes = [];
      issue.created_at = warningTime;
      if (objection === 'edit') issue.body = 'Different scope';
      if (objection === 'reply') state.comments.push({ id: 1001, user: human, body: 'Different scope' });
      if (objection === 'thumbs-down') state.reactions.push({ content: '-1', user: human });
      if (objection === 'reopen') state.events.push({ event: 'reopened', created_at: warningTime });
      if (objection === 'missing notice') { state.comments = []; issue.comments = 0; }
      assert.equal((await assessDuplicate(github, repo, issue, due - 1)).status, 'cancelled');
      assert.equal(await closeDuplicates(github, repo, { dryRun: false, now: due - 1, log: () => {} }), 0);
      assert.deepEqual(issue.labels, ['curation']);
      assert.equal(issue.state, 'open');
      assert.deepEqual(state.writes, []);
    });
  }

  it('previews cancellation without clearing labels in a dry run', async () => {
    const { github, issue, propose } = fixture();
    await propose();
    issue.body = 'Different scope';
    const logs = [];
    await closeDuplicates(github, repo, { now: due, log: line => logs.push(line) });
    assert.match(logs[0], /Would remove duplicate-pending/);
    assert.deepEqual(issue.labels, ['curation', 'duplicate-pending']);
  });

  it('does not requeue a cancelled proposal if the thumbs-down is later removed', async () => {
    const { github, state, issue, propose } = fixture();
    await propose();
    state.reactions.push({ content: '-1', user: human });
    await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} });
    state.reactions = [];
    assert.equal(await propose(), false);
    assert.equal(await prepareSearch(github, repo, '100'), null);
    assert.deepEqual(issue.labels, ['curation']);
  });

  it('keeps waiting issues queued and distinguishes locking from cancellation', async () => {
    const { github, issue, propose } = fixture();
    await propose();
    assert.equal((await assessDuplicate(github, repo, issue, due - 1)).status, 'waiting');
    issue.locked = true;
    assert.equal((await assessDuplicate(github, repo, issue, due)).status, 'waiting');
    await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} });
    assert.deepEqual(issue.labels, ['curation', 'duplicate-pending']);
  });

  it('rechecks replies arriving between the initial scan and closure', async () => {
    const { github, state, propose } = fixture();
    await propose();
    state.writes = [];
    const get = github.rest.issues.get;
    github.rest.issues.get = async args => {
      if (args.issue_number === 100) state.comments.push({ id: 1010, user: human, body: 'Please keep this' });
      return get(args);
    };
    assert.equal(await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} }), 0);
    assert.deepEqual(state.writes, []);
  });
});

async function batchFixture(size = 2) {
  const fixtureData = fixture();
  const { state, issue, propose } = fixtureData;
  await propose();
  for (let offset = 1; offset < size; offset++) {
    const number = issue.number + offset;
    state.issues.push({ ...issue, number, id: 1100 + offset, labels: [...issue.labels] });
    state.comments.push({ ...state.comments[0], issue_number: number, id: 1000 + offset });
  }
  state.writes = [];
  return fixtureData;
}

describe('duplicate sweep limits and errors', () => {
  it('defaults to five closures and leaves the remainder queued', async () => {
    const { github, state } = await batchFixture(7);
    assert.equal(await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} }), 5);
    assert.equal(state.writes.length, 5);
    assert.equal(state.issues.filter(issue => issue.state === 'open' && issue.labels.includes('duplicate-pending')).length, 2);
  });

  it('validates the closure budget before reading or writing issues', async () => {
    const { github, state } = fixture();
    for (const maxClosures of [0, -1, 51, 1.5, NaN]) {
      await assert.rejects(closeDuplicates(github, repo, { maxClosures }), /maxClosures/);
    }
    assert.deepEqual(state.reads, []);
    assert.deepEqual(state.writes, []);
  });

  it('continues cancellation cleanup after reaching the closure budget', async () => {
    const { github, state } = await batchFixture(3);
    state.comments.push({ issue_number: 102, id: 1010, user: human, body: 'Different scope' });
    assert.equal(await closeDuplicates(github, repo, {
      dryRun: false, maxClosures: 1, now: due, log: () => {},
    }), 1);
    assert.deepEqual(state.issues.find(issue => issue.number === 102).labels, ['curation']);
    assert.equal(state.issues.find(issue => issue.number === 102).state, 'open');
    assert.ok(state.issues.find(issue => issue.number === 101).labels.includes('duplicate-pending'));
  });

  it('honors the budget in dry runs without modifying issues', async () => {
    const { github, state } = await batchFixture(3);
    assert.equal(await closeDuplicates(github, repo, { maxClosures: 1, now: due, log: () => {} }), 1);
    assert.deepEqual(state.writes, []);
    assert.ok(state.issues.every(issue => issue.state === 'open'));
  });

  it('continues with later issues after an individual API failure', async () => {
    const { github, state } = await batchFixture();
    const get = github.rest.issues.get;
    github.rest.issues.get = async args => {
      if (args.issue_number === 100) throw new Error('Temporary API failure');
      return get(args);
    };
    const warnings = [];
    assert.equal(await closeDuplicates(github, repo, {
      dryRun: false, now: due, log: () => {}, warn: message => warnings.push(message),
    }), 1);
    assert.equal(state.writes[0].issue_number, 101);
    assert.match(warnings[0], /#100: Temporary API failure/);
  });

  it('tolerates a label removed concurrently with closure', async () => {
    const { github } = await batchFixture();
    const remove = github.rest.issues.removeLabel;
    github.rest.issues.removeLabel = async args => {
      await remove(args);
      if (args.issue_number === 100) throw Object.assign(new Error('Already removed'), { status: 404 });
    };
    assert.equal(await closeDuplicates(github, repo, { dryRun: false, now: due, log: () => {} }), 2);
  });

  it('counts uncertain failed closure requests against the budget', async () => {
    const { github, state } = await batchFixture();
    let attempts = 0;
    github.rest.issues.update = async () => { attempts += 1; throw new Error('Response lost'); };
    assert.equal(await closeDuplicates(github, repo, {
      dryRun: false, maxClosures: 1, now: due, log: () => {}, warn: () => {},
    }), 0);
    assert.equal(attempts, 1);
    assert.deepEqual(state.writes, []);
  });
});
