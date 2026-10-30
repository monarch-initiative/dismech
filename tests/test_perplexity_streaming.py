"""Tests for the streaming Perplexity request path (dismech#9357)."""

import json

import pytest

from dismech.perplexity_streaming import assemble_stream, install, strip_think_block


def _sse(chunk: dict) -> str:
    return "data: " + json.dumps(chunk)


def test_deltas_are_joined_and_think_block_removed():
    lines = [
        _sse({"choices": [{"delta": {"content": "<think>searching"}}]}),
        "",
        _sse({"choices": [{"delta": {"content": " more</think>\n\n# Report"}}]}),
        _sse({"choices": [{"delta": {"content": " body"}}]}),
        "data: [DONE]",
    ]
    data = assemble_stream(lines)
    assert data["choices"][0]["message"]["content"] == "# Report body"


def test_last_non_empty_citations_are_kept():
    lines = [
        _sse({"citations": ["https://a"], "choices": [{"delta": {"content": "x"}}]}),
        _sse({"citations": [], "choices": [{"delta": {"content": "y"}}]}),
        _sse({"citations": ["https://a", "https://b"], "search_results": [{"url": "https://b"}]}),
    ]
    data = assemble_stream(lines)
    assert data["citations"] == ["https://a", "https://b"]
    assert data["search_results"] == [{"url": "https://b"}]
    assert data["choices"][0]["message"]["content"] == "xy"


def test_comment_and_malformed_lines_are_ignored():
    lines = [": keep-alive", "event: message", "data: {not json", _sse({"choices": [{"delta": {"content": "ok"}}]})]
    assert assemble_stream(lines)["choices"][0]["message"]["content"] == "ok"


def test_think_block_only_stripped_at_start():
    text = "Intro mentions <think>tags</think> inline."
    assert strip_think_block(text) == text


def test_unclosed_think_block_is_dropped_to_empty():
    # A stream cut off mid-reasoning (no </think>) must not leak reasoning as report body.
    assert strip_think_block("<think>still reasoning and then the stream died") == ""
    assert assemble_stream(
        [_sse({"choices": [{"delta": {"content": "<think>reasoning only"}}]})]
    )["choices"][0]["message"]["content"] == ""


def test_refusal_finish_reason_is_recorded():
    lines = [
        _sse({"choices": [{"delta": {"content": ""}, "finish_reason": "refusal"}]}),
    ]
    assert assemble_stream(lines).get("finish_reason") == "refusal"


def test_last_finish_reason_wins_and_absent_when_none():
    assert "finish_reason" not in assemble_stream(
        [_sse({"choices": [{"delta": {"content": "ok"}}]})]
    )
    lines = [
        _sse({"choices": [{"delta": {"content": "a"}, "finish_reason": "length"}]}),
        _sse({"choices": [{"delta": {"content": "b"}, "finish_reason": "stop"}]}),
    ]
    assert assemble_stream(lines)["finish_reason"] == "stop"


def test_install_replaces_the_upstream_method():
    perplexity = pytest.importorskip("deep_research_client.providers.perplexity")
    assert install() is True
    assert install() is True
    assert perplexity.PerplexityProvider.research.__name__ == "streaming_research"
