"""Tests for the Perplexity request paths (dismech#9357)."""

import asyncio
import importlib
import json
import logging

import pytest

from dismech import perplexity_streaming
from dismech.perplexity_streaming import (
    assemble_stream,
    async_job_url,
    completed_job_data,
    install,
    selected_transport,
    signature_drift,
    strip_think_block,
)


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


def test_install_replaces_the_upstream_method_with_the_async_path(monkeypatch):
    perplexity = pytest.importorskip("deep_research_client.providers.perplexity")
    monkeypatch.delenv("DISMECH_PERPLEXITY_TRANSPORT", raising=False)
    perplexity = importlib.reload(perplexity)
    assert install() is True
    assert install() is True
    assert perplexity.PerplexityProvider.research.__name__ == "async_poll_research"


def test_stream_transport_selects_the_streaming_fallback(monkeypatch):
    perplexity = pytest.importorskip("deep_research_client.providers.perplexity")
    monkeypatch.setenv("DISMECH_PERPLEXITY_TRANSPORT", "stream")
    perplexity = importlib.reload(perplexity)
    assert install() is True
    assert perplexity.PerplexityProvider.research.__name__ == "streaming_research"
    monkeypatch.delenv("DISMECH_PERPLEXITY_TRANSPORT")
    importlib.reload(perplexity)


def test_selected_transport_defaults_to_async(monkeypatch):
    monkeypatch.delenv("DISMECH_PERPLEXITY_TRANSPORT", raising=False)
    assert selected_transport() == "async"
    monkeypatch.setenv("DISMECH_PERPLEXITY_TRANSPORT", " Stream ")
    assert selected_transport() == "stream"
    monkeypatch.setenv("DISMECH_PERPLEXITY_TRANSPORT", "bogus")
    assert selected_transport() == "async"


def test_async_job_url_is_derived_from_the_sync_endpoint():
    assert (
        async_job_url("https://api.perplexity.ai/chat/completions")
        == "https://api.perplexity.ai/async/chat/completions"
    )
    with pytest.raises(ValueError):
        async_job_url("https://example.org/v1/responses")


def test_completed_job_data_lifts_finish_reason_and_fills_content():
    job = {"status": "COMPLETED", "response": {"choices": [{"finish_reason": "refusal", "message": {}}]}}
    data = completed_job_data(job)
    assert data["finish_reason"] == "refusal"
    assert data["choices"][0]["message"]["content"] == ""
    assert completed_job_data({"status": "COMPLETED"})["choices"][0]["message"]["content"] == ""


class _FakeProvider:
    """Just enough of PerplexityProvider for the request paths."""

    name = "perplexity"
    model = "sonar-deep-research"
    api_url = "https://api.perplexity.ai/chat/completions"

    class config:  # noqa: N801 - mirrors the upstream attribute name
        api_key = "test-key"
        timeout = 600

    class params:  # noqa: N801
        system_prompt = "system"
        temperature = 0.1
        return_citations = True
        reasoning_effort = "medium"
        search_recency_filter = None
        search_domain_filter = None

    def is_available(self):
        return True

    def unavailable_reason(self):
        return ""

    def _extract_citations(self, content, data):
        return list(data.get("citations") or [])


def _run_async_path(monkeypatch, responses):
    """Run async_poll_research against a scripted sequence of job states."""
    httpx = pytest.importorskip("httpx")
    pytest.importorskip("deep_research_client.models")
    calls = []
    states = iter(responses)

    def handler(request):
        calls.append((request.method, str(request.url)))
        if request.method == "POST":
            body = json.loads(request.content)
            assert body["request"]["model"] == "sonar-deep-research"
            assert "stream" not in body["request"]
            return httpx.Response(200, json={"id": "job-1", "status": "CREATED"})
        status, payload = next(states)
        return httpx.Response(status, json=payload)

    real_client = httpx.AsyncClient
    monkeypatch.setattr(
        httpx, "AsyncClient", lambda **kw: real_client(transport=httpx.MockTransport(handler), **kw)
    )
    monkeypatch.setattr(perplexity_streaming, "POLL_INTERVAL_SECONDS", 0)
    result = asyncio.run(perplexity_streaming.async_poll_research(_FakeProvider(), "question"))
    return result, calls


def test_async_path_polls_until_completed_and_strips_reasoning(monkeypatch):
    done = {
        "id": "job-1",
        "status": "COMPLETED",
        "response": {
            "choices": [{"message": {"content": "<think>searching</think>\n# Report"}, "finish_reason": "stop"}],
            "citations": ["https://a"],
        },
    }
    result, calls = _run_async_path(
        monkeypatch,
        [(200, {"id": "job-1", "status": "IN_PROGRESS"}), (503, {}), (200, done)],
    )
    assert result.markdown == "# Report"
    assert result.citations == ["https://a"]
    assert calls[0] == ("POST", "https://api.perplexity.ai/async/chat/completions")
    assert calls[1:] == [("GET", "https://api.perplexity.ai/async/chat/completions/job-1")] * 3


def test_async_path_reports_a_failed_job(monkeypatch):
    with pytest.raises(ValueError, match="failed: 'boom'"):
        _run_async_path(monkeypatch, [(200, {"id": "job-1", "status": "FAILED", "error_message": "boom"})])


def test_async_path_names_a_refusal(monkeypatch):
    refused = {
        "id": "job-1",
        "status": "COMPLETED",
        "response": {"choices": [{"message": {"content": ""}, "finish_reason": "refusal"}]},
    }
    with pytest.raises(ValueError, match="refused"):
        _run_async_path(monkeypatch, [(200, refused)])


def test_signature_drift_compares_parameter_names_not_annotations():
    def annotated(self, query: str) -> dict:  # same parameters, annotated
        return {}

    def changed(self, query, *, stream=False):
        return {}

    assert signature_drift(annotated) is None
    assert signature_drift(changed) is not None


def test_install_logs_no_drift_warning_against_installed_version(caplog):
    perplexity = pytest.importorskip("deep_research_client.providers.perplexity")
    # Re-execute the module so the class carries the original, unpatched method.
    perplexity = importlib.reload(perplexity)
    assert not getattr(perplexity.PerplexityProvider, "_dismech_streaming", False)
    with caplog.at_level(logging.WARNING, logger="dismech.perplexity_streaming"):
        assert install() is True
    assert [r for r in caplog.records if r.levelno >= logging.WARNING] == []
