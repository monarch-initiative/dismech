/**
 * The handle curators type to summon the repository's mention-driven agent, and
 * the parser that both the dispatch workflow (dragon-ai.yml) and the comment
 * trust gate (github-trust-gate.js) share.
 *
 * `@ai4c-agent` is NOT a real GitHub account. The agent runs as the ai4c-agent
 * GitHub App, whose login is `ai4c-agent[bot]`, and Apps cannot be @-mentioned,
 * so the handle renders as plain text. That is fine: it is a text keyword, not a
 * notification. `@dragon-ai-agent` is the retired machine account's handle and
 * is still honoured so existing muscle memory and old threads keep working.
 *
 * Keep the handles here and nowhere else. The ai4c-agent alias was missed the
 * first time round precisely because the workflow carried its own copy of the
 * regex: PR #6979 switched the responder's identity to the App but left the
 * trigger text on the retired handle, so `@ai4c-agent please ...` was silently
 * ignored (tests/test_dragon_ai_workflow.py guards against a second copy).
 */
const AGENT_MENTION = "ai4c-agent";
const LEGACY_AGENT_MENTIONS = ["dragon-ai-agent"];

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function allHandles() {
  return [AGENT_MENTION, ...LEGACY_AGENT_MENTIONS];
}

/** Regex-source alternation of every accepted handle, canonical first. */
function handleAlternation() {
  return allHandles().map(escapeRegExp).join("|");
}

/**
 * Strip fenced blocks and inline code spans so that merely *documenting* the
 * keyword (in a PR description, say) does not dispatch the agent. Only a real,
 * prose-level "@ai4c-agent please ..." qualifies.
 */
function stripCodeSpans(text) {
  return String(text || "")
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/`[^`]*`/g, " ");
}

/**
 * A summon is the handle (any spelling in `allHandles()`), an optional `[bot]`
 * suffix (people paste back what they see the App signing as), then `please`
 * and the request. Dotall, so a multi-line request is captured whole.
 */
function mentionRegExp() {
  return new RegExp(
    `@(${handleAlternation()})(?:\\[bot\\])?\\s+please\\s+(.*)`,
    "is",
  );
}

/**
 * Parse a comment, issue, or PR body for a summon.
 *
 * @param {string|null|undefined} content
 * @returns {{matched: boolean, handle: string, prompt: string, isLegacy: boolean}}
 *   `handle` is the canonical lowercase spelling of whichever handle was typed;
 *   `isLegacy` is true when it was not the current `AGENT_MENTION`.
 */
function parseAgentMention(content) {
  const match = stripCodeSpans(content).match(mentionRegExp());
  if (!match) {
    return { matched: false, handle: "", prompt: "", isLegacy: false };
  }
  const typed = match[1].toLowerCase();
  const handle = allHandles().find((h) => h.toLowerCase() === typed) || typed;
  return {
    matched: true,
    handle,
    prompt: match[2].trim(),
    isLegacy: handle !== AGENT_MENTION,
  };
}

module.exports = {
  AGENT_MENTION,
  LEGACY_AGENT_MENTIONS,
  allHandles,
  handleAlternation,
  mentionRegExp,
  parseAgentMention,
  stripCodeSpans,
};
