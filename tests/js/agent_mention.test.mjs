import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const {
  AGENT_MENTION,
  LEGACY_AGENT_MENTIONS,
  parseAgentMention,
} = require("../../.github/scripts/agent-mention.js");

describe("agent mention parsing", () => {
  it("dispatches on the canonical @ai4c-agent handle", () => {
    const result = parseAgentMention("@ai4c-agent please fix it's trivial");

    assert.equal(result.matched, true);
    assert.equal(result.handle, "ai4c-agent");
    assert.equal(result.prompt, "fix it's trivial");
    assert.equal(result.isLegacy, false);
  });

  it("still dispatches on the legacy @dragon-ai-agent handle and flags it", () => {
    const result = parseAgentMention("@dragon-ai-agent please rebase this PR");

    assert.equal(result.matched, true);
    assert.equal(result.handle, "dragon-ai-agent");
    assert.equal(result.prompt, "rebase this PR");
    assert.equal(result.isLegacy, true);
  });

  it("accepts the [bot] suffix people paste back from the App's signature", () => {
    const result = parseAgentMention("@ai4c-agent[bot] please summarize this thread");

    assert.equal(result.matched, true);
    assert.equal(result.handle, "ai4c-agent");
    assert.equal(result.prompt, "summarize this thread");
  });

  it("matches the handle and keyword case-insensitively", () => {
    const result = parseAgentMention("@AI4C-Agent PLEASE do the thing");

    assert.equal(result.matched, true);
    assert.equal(result.handle, "ai4c-agent");
    assert.equal(result.isLegacy, false);
  });

  it("captures a multi-line request whole", () => {
    const result = parseAgentMention(
      "@ai4c-agent please do two things:\n1. first\n2. second",
    );

    assert.equal(result.prompt, "do two things:\n1. first\n2. second");
  });

  it("keeps a fenced code block that is part of the request", () => {
    const result = parseAgentMention(
      "@ai4c-agent please apply this patch:\n\n```diff\n-old\n+new\n```\n\nthen run the tests.",
    );

    assert.equal(result.matched, true);
    assert.equal(
      result.prompt,
      "apply this patch:\n\n```diff\n-old\n+new\n```\n\nthen run the tests.",
    );
  });

  it("keeps an inline code span that is part of the request", () => {
    const result = parseAgentMention("@ai4c-agent please run `just qc` and report");

    assert.equal(result.matched, true);
    assert.equal(result.prompt, "run `just qc` and report");
  });

  it("ignores a mention inside a fenced code block", () => {
    const result = parseAgentMention(
      "Docs:\n```\n@ai4c-agent please do X\n```\nThat is how you call it.",
    );

    assert.equal(result.matched, false);
    assert.equal(result.prompt, "");
  });

  it("ignores a mention inside an inline code span", () => {
    const result = parseAgentMention("Type `@ai4c-agent please ...` to summon it.");

    assert.equal(result.matched, false);
  });

  it("does not match a bare handle without the please keyword", () => {
    const result = parseAgentMention("cc @ai4c-agent for visibility");

    assert.equal(result.matched, false);
  });

  it("does not match an unrelated handle", () => {
    const result = parseAgentMention("@claude please do X");

    assert.equal(result.matched, false);
  });

  it("tolerates an empty or missing body", () => {
    assert.equal(parseAgentMention("").matched, false);
    assert.equal(parseAgentMention(null).matched, false);
    assert.equal(parseAgentMention(undefined).matched, false);
  });

  it("exposes the handles the workflow advertises", () => {
    assert.equal(AGENT_MENTION, "ai4c-agent");
    assert.deepEqual(LEGACY_AGENT_MENTIONS, ["dragon-ai-agent"]);
  });
});
