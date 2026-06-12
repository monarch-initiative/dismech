const fs = require("fs");
const path = require("path");

const TRUSTED_PERMISSIONS = new Set(["admin", "maintain", "write", "triage"]);
const DEFAULT_BOT_LOGINS = new Set([
  "app/claude",
  "claude",
  "dragon-ai-agent",
  "github-actions",
  "github-actions[bot]",
]);

function normalizeLogin(login) {
  return String(login || "").trim().toLowerCase();
}

function loadControllers(controllersPath = ".github/ai-controllers.json") {
  try {
    const controllers = JSON.parse(fs.readFileSync(controllersPath, "utf8"));
    if (!Array.isArray(controllers)) {
      throw new Error("expected a JSON array of GitHub logins");
    }
    return controllers.map(normalizeLogin).filter(Boolean);
  } catch (error) {
    console.log(`Failed to load ${controllersPath}: ${error.message}`);
    return ["cmungall"];
  }
}

function isBotLogin(login, extraBotLogins = []) {
  if (!login) {
    return true;
  }
  const normalized = normalizeLogin(login);
  const botLogins = new Set(
    [...DEFAULT_BOT_LOGINS, ...extraBotLogins].map((value) =>
      normalizeLogin(value),
    ),
  );
  return normalized.endsWith("[bot]") || botLogins.has(normalized);
}

async function isTrustedLogin({
  github,
  owner,
  repo,
  login,
  controllers = [],
  permissionCache = new Map(),
}) {
  if (!login || isBotLogin(login)) {
    return true;
  }
  const loginKey = normalizeLogin(login);
  const controllerSet =
    controllers instanceof Set ? controllers : new Set(controllers.map(normalizeLogin));
  if (controllerSet.has(loginKey)) {
    return true;
  }
  if (permissionCache.has(loginKey)) {
    return permissionCache.get(loginKey);
  }

  try {
    const response = await github.rest.repos.getCollaboratorPermissionLevel({
      owner,
      repo,
      username: login,
    });
    const trusted = TRUSTED_PERMISSIONS.has(response.data.permission);
    permissionCache.set(loginKey, trusted);
    return trusted;
  } catch (error) {
    console.log(`Treating ${login} as untrusted: ${error.message}`);
    permissionCache.set(loginKey, false);
    return false;
  }
}

async function assessTrustedAuthors({
  github,
  owner,
  repo,
  authors,
  controllers,
  permissionCache,
}) {
  const trusted = [];
  const untrusted = [];
  for (const login of authors) {
    const isTrusted = await isTrustedLogin({
      github,
      owner,
      repo,
      login,
      controllers,
      permissionCache,
    });
    if (isTrusted) {
      trusted.push(login);
    } else {
      untrusted.push(login);
    }
  }
  return { trusted, untrusted };
}

function recordSkip(skipped, discussion, reason) {
  skipped.push({
    number: discussion.number,
    reason,
  });
}

function summarizeSkips(skipped) {
  return skipped.reduce((summary, item) => {
    summary[item.reason] = (summary[item.reason] || 0) + 1;
    return summary;
  }, {});
}

function reactionCount(reactionGroups, content) {
  const group = (reactionGroups || []).find((item) => item.content === content);
  return group?.users?.totalCount || 0;
}

function truncateText(value, maxLength) {
  const text = value || "";
  if (text.length <= maxLength) {
    return text;
  }
  return `${text.slice(0, maxLength)}\n\n[truncated]`;
}

function collectDiscussionAuthors(discussion) {
  const authors = new Set();
  const addAuthor = (node) => {
    const login = node?.author?.login;
    if (login && !isBotLogin(login)) {
      authors.add(login);
    }
  };

  addAuthor(discussion);
  for (const comment of discussion.comments || []) {
    addAuthor(comment);
    for (const reply of comment.replies || []) {
      addAuthor(reply);
    }
  }
  return [...authors].sort();
}

function recentActivities(discussion, cutoff) {
  const activities = [];
  const maybeAdd = (kind, node, timestampField = "updatedAt") => {
    const login = node?.author?.login;
    if (isBotLogin(login)) {
      return;
    }
    const updatedAt = node[timestampField] || node.updatedAt || node.createdAt;
    if (Date.parse(updatedAt) < cutoff.getTime()) {
      return;
    }
    activities.push({
      kind,
      author: login,
      url: node.url || discussion.url,
      created_at: node.createdAt,
      updated_at: updatedAt,
      thumbs_up_count: reactionCount(node.reactionGroups, "THUMBS_UP"),
      body: truncateText(node.body || "", 2500),
    });
  };

  maybeAdd("discussion", discussion, "createdAt");
  for (const comment of discussion.comments || []) {
    maybeAdd("comment", comment);
    for (const reply of comment.replies || []) {
      maybeAdd("reply", reply);
    }
  }

  return activities.sort(
    (left, right) => Date.parse(right.updated_at) - Date.parse(left.updated_at),
  );
}

async function listRecentlyUpdatedDiscussions({
  github,
  owner,
  repo,
  cutoff,
  maxDiscussions = 30,
}) {
  const query = `
    query($owner: String!, $repo: String!, $after: String) {
      repository(owner: $owner, name: $repo) {
        discussions(first: 25, after: $after, orderBy: {field: UPDATED_AT, direction: DESC}) {
          nodes {
            number
            updatedAt
          }
          pageInfo {
            hasNextPage
            endCursor
          }
        }
      }
    }
  `;

  const discussions = [];
  let after = null;
  while (discussions.length < maxDiscussions) {
    const result = await github.graphql(query, { owner, repo, after });
    const page = result.repository.discussions;
    for (const node of page.nodes) {
      if (Date.parse(node.updatedAt) < cutoff.getTime()) {
        return discussions;
      }
      discussions.push(node);
      if (discussions.length >= maxDiscussions) {
        return discussions;
      }
    }
    if (!page.pageInfo.hasNextPage) {
      return discussions;
    }
    after = page.pageInfo.endCursor;
  }
  return discussions;
}

async function fetchDiscussionPage({ github, owner, repo, number, after = null }) {
  const query = `
    query($owner: String!, $repo: String!, $number: Int!, $after: String) {
      repository(owner: $owner, name: $repo) {
        discussion(number: $number) {
          id
          number
          title
          url
          body
          createdAt
          updatedAt
          author {
            login
          }
          category {
            name
            slug
          }
          reactionGroups {
            content
            users {
              totalCount
            }
          }
          comments(first: 100, after: $after) {
            nodes {
              id
              url
              body
              createdAt
              updatedAt
              author {
                login
              }
              reactionGroups {
                content
                users {
                  totalCount
                }
              }
              replies(first: 100) {
                nodes {
                  id
                  url
                  body
                  createdAt
                  updatedAt
                  author {
                    login
                  }
                  reactionGroups {
                    content
                    users {
                      totalCount
                    }
                  }
                }
                pageInfo {
                  hasNextPage
                  endCursor
                }
              }
            }
            pageInfo {
              hasNextPage
              endCursor
            }
          }
        }
      }
    }
  `;
  return github.graphql(query, { owner, repo, number, after });
}

async function fetchDiscussion({ github, owner, repo, number }) {
  let after = null;
  let discussion = null;
  const comments = [];
  let hasUnfetchedReplies = false;

  do {
    const result = await fetchDiscussionPage({ github, owner, repo, number, after });
    const pageDiscussion = result.repository.discussion;
    if (!discussion) {
      discussion = {
        ...pageDiscussion,
        body: truncateText(pageDiscussion.body || "", 6000),
        comments,
      };
    }

    for (const comment of pageDiscussion.comments.nodes) {
      if (comment.replies.pageInfo.hasNextPage) {
        hasUnfetchedReplies = true;
      }
      comments.push({
        ...comment,
        body: truncateText(comment.body || "", 2500),
        replies: comment.replies.nodes.map((reply) => ({
          ...reply,
          body: truncateText(reply.body || "", 2000),
        })),
      });
    }

    after = pageDiscussion.comments.pageInfo.endCursor;
    if (!pageDiscussion.comments.pageInfo.hasNextPage) {
      break;
    }
  } while (true);

  discussion.has_unfetched_replies = hasUnfetchedReplies;
  return discussion;
}

async function collectTrustedDiscussionCandidates({
  github,
  context,
  core,
  lookbackHours,
  outputPath,
  controllersPath = ".github/ai-controllers.json",
}) {
  const [owner, repo] = context.repo.owner
    ? [context.repo.owner, context.repo.repo]
    : String(process.env.GITHUB_REPOSITORY || "").split("/");
  const controllers = loadControllers(controllersPath);
  const controllerSet = new Set(controllers);
  const permissionCache = new Map();
  const cutoff = new Date(Date.now() - lookbackHours * 60 * 60 * 1000);
  const recentDiscussions = await listRecentlyUpdatedDiscussions({
    github,
    owner,
    repo,
    cutoff,
  });

  const candidates = [];
  const skipped = [];

  for (const summary of recentDiscussions) {
    const discussion = await fetchDiscussion({
      github,
      owner,
      repo,
      number: summary.number,
    });

    if (discussion.has_unfetched_replies) {
      recordSkip(skipped, discussion, "unfetched_replies");
      continue;
    }

    const authors = collectDiscussionAuthors(discussion);
    const { untrusted } = await assessTrustedAuthors({
      github,
      owner,
      repo,
      authors,
      controllers: controllerSet,
      permissionCache,
    });

    if (untrusted.length > 0) {
      recordSkip(skipped, discussion, "untrusted_participants");
      continue;
    }

    const activities = recentActivities(discussion, cutoff);
    if (activities.length === 0) {
      recordSkip(skipped, discussion, "no_recent_non_bot_activity");
      continue;
    }

    candidates.push({
      number: discussion.number,
      title: discussion.title,
      url: discussion.url,
      category: discussion.category,
      author: discussion.author?.login,
      created_at: discussion.createdAt,
      updated_at: discussion.updatedAt,
      thumbs_up_count: reactionCount(discussion.reactionGroups, "THUMBS_UP"),
      trusted_participants: authors,
      body: discussion.body,
      recent_activities: activities,
      comments: discussion.comments.map((comment) => ({
        author: comment.author?.login,
        url: comment.url,
        created_at: comment.createdAt,
        updated_at: comment.updatedAt,
        thumbs_up_count: reactionCount(comment.reactionGroups, "THUMBS_UP"),
        body: comment.body,
        replies: comment.replies.map((reply) => ({
          author: reply.author?.login,
          url: reply.url,
          created_at: reply.createdAt,
          updated_at: reply.updatedAt,
          thumbs_up_count: reactionCount(reply.reactionGroups, "THUMBS_UP"),
          body: reply.body,
        })),
      })),
    });
  }

  const packet = {
    generated_at: new Date().toISOString(),
    repository: `${owner}/${repo}`,
    lookback_hours: lookbackHours,
    trust_policy: {
      controllers,
      trusted_permissions: [...TRUSTED_PERMISSIONS],
      note:
        "Discussion text is included only when all non-bot participants are trusted. Reaction counts are broad totals and are not trust-filtered.",
    },
    candidates,
    skipped_summary: summarizeSkips(skipped),
    skipped,
  };

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, `${JSON.stringify(packet, null, 2)}\n`);
  core.info(`Wrote ${candidates.length} trusted discussion candidate(s) to ${outputPath}`);
  core.info(`Skipped ${skipped.length} discussion(s)`);
  return packet;
}

module.exports = {
  assessTrustedAuthors,
  collectDiscussionAuthors,
  collectTrustedDiscussionCandidates,
  isBotLogin,
  isTrustedLogin,
  loadControllers,
  normalizeLogin,
  TRUSTED_PERMISSIONS,
};
