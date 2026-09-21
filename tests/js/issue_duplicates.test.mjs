import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { fingerprint, prepareSearch, proposeDuplicates, eligibleDuplicate, closeDuplicates } =
  require('../../.github/scripts/issue-duplicates.js');

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
  const state = { issues: [issue, target], comments: [], reactions: [], events: [], writes: [], reads: [] };
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
          state.comments.push({ ...data, id: 1000, user: bot, created_at: warningTime });
        },
        update: async data => { state.writes.push(data); },
      },
      reactions: { listForIssueComment: 'reactions' },
    },
    paginate: async (method, args) => {
      assert.equal(args.per_page, 100);
      state.reads.push(method);
      if (method === 'issues') {
        assert.equal(args.labels, 'duplicate-pending');
        return state.issues.filter(issue => issue.labels.includes(args.labels));
      }
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

  it('rejects self, newer, malformed, repeated and excessive candidates', async () => {
    const { propose } = fixture();
    for (const number of [100, 101, -1, 0, '10', 1.5]) {
      await assert.rejects(propose([{ number, reason: 'same' }]));
    }
    await assert.rejects(propose([{ number: 10, reason: '' }]));
    await assert.rejects(propose([{ number: 10, reason: 'same' }, { number: 10, reason: 'same' }]));
    await assert.rejects(propose([1, 2, 3, 4].map(number => ({ number, reason: 'same' }))));
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
