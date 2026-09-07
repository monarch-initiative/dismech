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
 * Blank out fenced blocks and inline code spans so that merely *documenting* the
 * keyword (in a PR description, say) does not dispatch the agent. Only a real,
 * prose-level "@ai4c-agent please ..." qualifies.
 *
 * Each masked character is replaced one-for-one, and newlines are kept, so the
 * masked text is the same length as the original and every offset still lines
 * up. That is what lets the request itself keep its code: the mention is
 * *detected* in the masked text, and the prompt is then *read* from the
 * original, so `@ai4c-agent please apply this patch:` followed by a diff keeps
 * the diff. Blanking to a single space instead would collapse the offsets and
 * silently truncate the request at its first code block.
 */
function maskCodeSpans(text) {
  const blank = (segment) => segment.replace(/[^\n]/g, " ");
  return String(text || "")
    .replace(/```[\s\S]*?```/g, blank)
    .replace(/~~~[\s\S]*?~~~/g, blank)
    .replace(/`[^`]*`/g, blank);
}

/**
 * Does this text name one of the handles at all, whatever it does with it?
 *
 * Lets a caller tell "nobody addressed the agent" apart from "somebody
 * addressed the agent and it did not qualify" -- a mention with no `please`, or
 * one masked by a stray unmatched backtick pairing with a later one. Both are
 * correct refusals, but silently doing nothing is precisely the failure this
 * module exists to fix, so the caller should say so in the log.
 */
function mentionsHandle(content) {
  return new RegExp(`@(?:${handleAlternation()})`, "i").test(String(content || ""));
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
  const original = String(content || "");
  const match = maskCodeSpans(original).match(mentionRegExp());
  if (!match) {
    return { matched: false, handle: "", prompt: "", isLegacy: false };
  }
  const typed = match[1].toLowerCase();
  const handle = allHandles().find((h) => h.toLowerCase() === typed) || typed;
  // Masking preserves length, so the request text starts at the same offset in
  // the original as it does in the masked copy the match was found in.
  const promptStart = match.index + (match[0].length - match[2].length);
  return {
    matched: true,
    handle,
    prompt: original.slice(promptStart).trim(),
    isLegacy: handle !== AGENT_MENTION,
  };
}

module.exports = {
  AGENT_MENTION,
  LEGACY_AGENT_MENTIONS,
  allHandles,
  handleAlternation,
  maskCodeSpans,
  mentionRegExp,
  mentionsHandle,
  parseAgentMention,
};
