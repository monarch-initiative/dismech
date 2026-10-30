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

Two details differ from the non-streaming response:

* ``sonar-deep-research`` opens its output with a ``<think>...</think>``
  reasoning block. It is removed here, so it does not land in the committed
  ``research/*.md`` report.
* ``citations`` and ``search_results`` arrive on the streamed chunks rather
  than on one final object, so the last non-empty value seen is kept.
"""

from __future__ import annotations

import json
import logging
import re
from collections.abc import Iterable
from typing import Any

logger = logging.getLogger(__name__)

THINK_BLOCK = re.compile(r"^\s*<think>.*?</think>\s*", re.DOTALL)


def strip_think_block(content: str) -> str:
    """Remove a leading ``<think>...</think>`` reasoning block, if present."""
    return THINK_BLOCK.sub("", content, count=1)


def assemble_stream(lines: Iterable[str]) -> dict[str, Any]:
    """Fold Perplexity SSE lines into one non-streaming-shaped response dict.

    Returns a dict with ``choices[0].message.content`` plus whichever of
    ``citations`` and ``search_results`` the stream carried, so the upstream
    ``_extract_citations`` can read it unchanged.
    """
    parts: list[str] = []
    data: dict[str, Any] = {}
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
            delta = choice.get("delta") or {}
            if delta.get("content"):
                parts.append(delta["content"])
            elif not parts and (choice.get("message") or {}).get("content"):
                # A server that answers with one complete message object.
                parts.append(choice["message"]["content"])
    data["choices"] = [{"message": {"content": strip_think_block("".join(parts))}}]
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
        data_lines = [line for line in lines if line.startswith("data:")]
        tail = data_lines[-1][:300] if data_lines else (lines[-1][:300] if lines else "")
        raise ValueError(
            "Perplexity API error: the stream ended without any report content "
            f"({len(lines)} lines, {len(data_lines)} data events; last: {tail!r})"
        )
    citations = self._extract_citations(markdown, data)
    logger.info("Perplexity streaming request completed: %d chars, %d citations", len(markdown), len(citations))
    return ResearchResult(markdown=markdown, citations=citations, provider=self.name, query=query)


def install() -> bool:
    """Replace the upstream non-streaming Perplexity request with the streaming one.

    Returns ``False`` (and changes nothing) when the provider is not importable.
    Calling it twice is harmless.
    """
    try:
        from deep_research_client.providers.perplexity import PerplexityProvider
    except ImportError:
        return False
    if getattr(PerplexityProvider, "_dismech_streaming", False):
        return True
    PerplexityProvider.research = streaming_research
    PerplexityProvider._dismech_streaming = True
    return True
