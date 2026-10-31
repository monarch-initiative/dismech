"""Streaming request path for deep-research-client's Perplexity provider.

``deep_research_client.providers.perplexity.PerplexityProvider.research``
sends one non-streaming POST. ``sonar-deep-research`` spends several minutes
searching and reasoning before it returns anything, so no bytes cross the
connection in that time, and a path with an idle timeout (the Claude Code agent
proxy closes such connections at about five minutes) drops the request. The
run then fails with "Server disconnected without sending a response" or "No
response content received from Perplexity" (dismech#9357, dismech#15217).

With ``"stream": true`` the API sends server-sent events throughout the
reasoning phase, which keeps the connection open. This module assembles those
events into the same ``ResearchResult`` the upstream method returns, and
:func:`install` swaps it in for the upstream method. The wrapper
``scripts/run_deep_research_client.sh`` calls :func:`install` before the CLI
runs. Remove this module once the upstream provider streams.

Three details differ from the non-streaming response:

* ``sonar-deep-research`` opens its output with a ``<think>...</think>``
  reasoning block. It is removed here, so it does not land in the committed
  ``research/*.md`` report. A ``<think>`` that is never closed (a stream cut
  off mid-reasoning) is treated as all-reasoning and stripped to empty, so it
  cannot masquerade as report content.
* ``citations`` and ``search_results`` arrive on the streamed chunks rather
  than on one final object, so the last non-empty value seen is kept.
* The model can decline a query with ``finish_reason=refusal`` (seen for
  Rift Valley fever). That is a content decision, not a transport failure, so
  it is named as such in the raised error.

This patch was written against ``deep-research-client`` 0.2.12, whose
``PerplexityProvider.research(self, query)`` it replaces. If a later version
changes that signature or starts streaming itself, :func:`install` logs a
warning rather than silently overriding the newer method.
"""

from __future__ import annotations

import inspect
import json
import logging
import re
from collections.abc import Iterable
from typing import Any

logger = logging.getLogger(__name__)

THINK_BLOCK = re.compile(r"^\s*<think>.*?</think>\s*", re.DOTALL)
UNCLOSED_THINK = re.compile(r"^\s*<think>(?!.*</think>)", re.DOTALL)

# Parameter names of the upstream method this patch was written to replace.
# Names, not the signature string: ``str(inspect.signature(...))`` includes the
# annotations (``(self, query: str) -> ResearchResult``), which would never
# compare equal and would make the drift warning fire on every run.
_EXPECTED_PARAMETERS = ("self", "query")


def signature_drift(method: Any) -> str | None:
    """Return the signature of ``method`` if its parameters differ from the expected ones.

    Returns ``None`` when the parameter names match, or when the signature
    cannot be introspected.
    """
    try:
        sig = inspect.signature(method)
    except (ValueError, TypeError):
        return None
    if tuple(sig.parameters) == _EXPECTED_PARAMETERS:
        return None
    return str(sig)


def strip_think_block(content: str) -> str:
    """Remove a leading ``<think>`` reasoning block.

    A properly closed ``<think>...</think>`` prefix is removed. A ``<think>``
    that is never closed means the stream carried only reasoning (e.g. it was
    cut off before the report began), so the whole string is dropped — this
    stops leaked reasoning from passing the "non-empty content" check and
    landing in the report.
    """
    if UNCLOSED_THINK.match(content):
        return ""
    return THINK_BLOCK.sub("", content, count=1)


def assemble_stream(lines: Iterable[str]) -> dict[str, Any]:
    """Fold Perplexity SSE lines into one non-streaming-shaped response dict.

    Returns a dict with ``choices[0].message.content`` plus whichever of
    ``citations`` and ``search_results`` the stream carried, so the upstream
    ``_extract_citations`` can read it unchanged, and the last non-null
    ``finish_reason`` seen (so a content refusal can be named).
    """
    parts: list[str] = []
    data: dict[str, Any] = {}
    finish_reason: str | None = None
    for raw in lines:
        line = raw.strip()
        if not line.startswith("data:"):
            continue
        payload = line[len("data:"):].strip()
        if not payload or payload == "[DONE]":
            continue
        try:
            chunk = json.loads(payload)
        except json.JSONDecodeError:
            logger.debug("Skipping unparseable stream line: %.80s", payload)
            continue
        for key in ("citations", "search_results"):
            if chunk.get(key):
                data[key] = chunk[key]
        for choice in chunk.get("choices") or []:
            if choice.get("finish_reason"):
                finish_reason = choice["finish_reason"]
            delta = choice.get("delta") or {}
            if delta.get("content"):
                parts.append(delta["content"])
            elif not parts and (choice.get("message") or {}).get("content"):
                # A server that answers with one complete message object.
                parts.append(choice["message"]["content"])
    data["choices"] = [{"message": {"content": strip_think_block("".join(parts))}}]
    if finish_reason is not None:
        data["finish_reason"] = finish_reason
    return data


async def streaming_research(self, query: str):
    """Drop-in replacement for ``PerplexityProvider.research`` that streams."""
    import httpx
    from deep_research_client.exceptions import ProviderNotConfiguredError
    from deep_research_client.models import ResearchResult
    from deep_research_client.system_prompts import DEFAULT_RESEARCH_SYSTEM_PROMPT

    logger.info("Starting Perplexity research query (model: %s, streaming)", self.model)
    if not self.is_available():
        raise ProviderNotConfiguredError(self.name, self.unavailable_reason())

    payload: dict[str, Any] = {
        "model": self.model,
        "messages": [
            {"role": "system", "content": self.params.system_prompt or DEFAULT_RESEARCH_SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
        "temperature": self.params.temperature,
        "return_citations": self.params.return_citations,
        "stream": True,
    }
    if self.params.reasoning_effort != "medium":
        payload["reasoning_effort"] = self.params.reasoning_effort
    if self.params.search_recency_filter:
        payload["search_recency_filter"] = self.params.search_recency_filter
    if self.params.search_domain_filter:
        payload["search_domain_filter"] = self.params.search_domain_filter

    headers = {
        "Authorization": f"Bearer {self.config.api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
    }
    # The read timeout bounds the gap between chunks, not the whole run, so a
    # long report is not cut off while the stream is still moving.
    timeout = httpx.Timeout(connect=30.0, read=float(self.config.timeout or 600), write=60.0, pool=30.0)
    try:
        async with (
            httpx.AsyncClient(timeout=timeout) as client,
            client.stream("POST", self.api_url, json=payload, headers=headers) as response,
        ):
            if response.status_code >= 400:
                body = (await response.aread()).decode(errors="replace")
                raise ValueError(f"Perplexity API HTTP error: {response.status_code} - {body}")
            lines = [line async for line in response.aiter_lines()]
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Perplexity API error: {e}") from e

    data = assemble_stream(lines)
    markdown = data["choices"][0]["message"]["content"]
    if not markdown.strip():
        # Distinguish a content refusal (the model declined) from an empty or
        # truncated stream, so a curator does not chase a transport bug.
        if data.get("finish_reason") == "refusal":
            raise ValueError(
                "Perplexity API error: the model refused the query "
                "(finish_reason=refusal) — a content decision, not a transport failure"
            )
        data_lines = [line for line in lines if line.startswith("data:")]
        tail = data_lines[-1][:300] if data_lines else (lines[-1][:300] if lines else "")
        raise ValueError(
            "Perplexity API error: the stream ended without any report content "
            f"(finish_reason={data.get('finish_reason')!r}, {len(lines)} lines, "
            f"{len(data_lines)} data events; last: {tail!r})"
        )
    citations = self._extract_citations(markdown, data)
    logger.info("Perplexity streaming request completed: %d chars, %d citations", len(markdown), len(citations))
    return ResearchResult(markdown=markdown, citations=citations, provider=self.name, query=query)


def install() -> bool:
    """Replace the upstream non-streaming Perplexity request with the streaming one.

    Returns ``False`` (and changes nothing) when the provider is not importable,
    logging a warning so a silent fallback to the non-streaming (timeout-prone)
    path is visible. Also warns if the upstream ``research`` signature has
    drifted from what this patch was written against, since overriding a changed
    method could mask a newer upstream fix. Calling it twice is harmless.
    """
    try:
        from deep_research_client.providers.perplexity import PerplexityProvider
    except ImportError:
        logger.warning(
            "deep_research_client Perplexity provider not importable; "
            "streaming patch NOT applied — Perplexity runs may hit the idle timeout (dismech#9357)"
        )
        return False
    if getattr(PerplexityProvider, "_dismech_streaming", False):
        return True
    drifted = signature_drift(PerplexityProvider.research)
    if drifted is not None:
        logger.warning(
            "PerplexityProvider.research signature is %s, expected parameters %s; "
            "applying the dismech streaming patch anyway, but upstream may have "
            "changed — re-check whether this patch is still needed (dismech#9357)",
            drifted,
            ", ".join(_EXPECTED_PARAMETERS),
        )
    PerplexityProvider.research = streaming_research
    PerplexityProvider._dismech_streaming = True
    return True
