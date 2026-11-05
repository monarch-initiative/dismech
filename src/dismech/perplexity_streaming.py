"""Long-running request paths for deep-research-client's Perplexity provider.

``deep_research_client.providers.perplexity.PerplexityProvider.research``
sends one non-streaming POST. ``sonar-deep-research`` spends several minutes
searching and reasoning before it returns anything, so no bytes cross the
connection in that time, and a path with an idle timeout (the Claude Code agent
proxy closes such connections at about five minutes) drops the request. The
run then fails with "Server disconnected without sending a response" or "No
response content received from Perplexity" (dismech#9357, dismech#15217).

Streaming alone does not fix this. Measured through the agent proxy,
``sonar-deep-research`` with ``"stream": true`` still sends nothing, not even
response headers, until its search phase ends: a research-sized prompt took
199 s to return its first byte. Any run whose search phase outlasts the idle
timeout is dropped the same way (dismech#9357 follow-up).

So the default path is now Perplexity's asynchronous API
(:func:`async_poll_research`): ``POST /async/chat/completions`` returns a job
id at once, and ``GET /async/chat/completions/{id}`` is polled with short
requests until the job is ``COMPLETED`` or ``FAILED``. No connection is held
open while the model works. A completed job carries the same
``choices``/``citations``/``search_results`` shape as the synchronous
response, so the upstream ``_extract_citations`` reads it unchanged.

The streaming path (:func:`streaming_research`) is kept as a fallback, chosen
with ``DISMECH_PERPLEXITY_TRANSPORT=stream``, for an account or endpoint
without the async API. :func:`install` swaps the chosen method in for the
upstream one. The wrapper ``scripts/run_deep_research_client.sh`` calls
:func:`install` before the CLI runs. Remove this module once the upstream
provider no longer holds one connection open for the whole run.

Three details differ from the upstream non-streaming handling:

* ``sonar-deep-research`` opens its output with a ``<think>...</think>``
  reasoning block. It is removed here, so it does not land in the committed
  ``research/*.md`` report. A ``<think>`` that is never closed (a stream cut
  off mid-reasoning) is treated as all-reasoning and stripped to empty, so it
  cannot masquerade as report content.
* On the streaming path, ``citations`` and ``search_results`` arrive on the
  streamed chunks rather than on one final object, so the last non-empty value
  seen is kept.
* The model can decline a query with ``finish_reason=refusal`` (seen for
  Rift Valley fever). That is a content decision, not a transport failure, so
  it is named as such in the raised error.

This patch was written against ``deep-research-client`` 0.2.12, whose
``PerplexityProvider.research(self, query)`` it replaces. If a later version
changes that signature or starts streaming itself, :func:`install` logs a
warning rather than silently overriding the newer method.
"""

from __future__ import annotations

import asyncio
import inspect
import json
import logging
import os
import re
import time
from collections.abc import Iterable
from typing import Any

logger = logging.getLogger(__name__)

THINK_BLOCK = re.compile(r"^\s*<think>.*?</think>\s*", re.DOTALL)
UNCLOSED_THINK = re.compile(r"^\s*<think>(?!.*</think>)", re.DOTALL)

#: Environment variable selecting the request path; ``stream`` picks the
#: streaming fallback, anything else (or unset) the async submit-and-poll path.
TRANSPORT_ENV = "DISMECH_PERPLEXITY_TRANSPORT"

#: Seconds between status polls of an async job.
POLL_INTERVAL_SECONDS = 15.0

#: Terminal statuses of a Perplexity async job.
_DONE_STATUSES = ("COMPLETED", "FAILED")

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


def _build_request(self, query: str) -> dict[str, Any]:
    """Return the chat-completions request body the upstream method would send."""
    from deep_research_client.system_prompts import DEFAULT_RESEARCH_SYSTEM_PROMPT

    payload: dict[str, Any] = {
        "model": self.model,
        "messages": [
            {"role": "system", "content": self.params.system_prompt or DEFAULT_RESEARCH_SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
        "temperature": self.params.temperature,
        "return_citations": self.params.return_citations,
    }
    if self.params.reasoning_effort != "medium":
        payload["reasoning_effort"] = self.params.reasoning_effort
    if self.params.search_recency_filter:
        payload["search_recency_filter"] = self.params.search_recency_filter
    if self.params.search_domain_filter:
        payload["search_domain_filter"] = self.params.search_domain_filter
    return payload


def _finalize(self, query: str, data: dict[str, Any], detail: str):
    """Turn a response dict into a ``ResearchResult``, or raise a named error.

    ``detail`` describes the response for the error raised when it holds no
    report content.
    """
    from deep_research_client.models import ResearchResult

    markdown = strip_think_block(data["choices"][0]["message"]["content"] or "")
    data["choices"][0]["message"]["content"] = markdown
    if not markdown.strip():
        # Distinguish a content refusal (the model declined) from an empty or
        # truncated response, so a curator does not chase a transport bug.
        if data.get("finish_reason") == "refusal":
            raise ValueError(
                "Perplexity API error: the model refused the query "
                "(finish_reason=refusal) — a content decision, not a transport failure"
            )
        raise ValueError(
            "Perplexity API error: the response held no report content "
            f"(finish_reason={data.get('finish_reason')!r}; {detail})"
        )
    citations = self._extract_citations(markdown, data)
    logger.info("Perplexity request completed: %d chars, %d citations", len(markdown), len(citations))
    return ResearchResult(markdown=markdown, citations=citations, provider=self.name, query=query)


def completed_job_data(job: dict[str, Any]) -> dict[str, Any]:
    """Return the response dict of a completed async job, shaped for :func:`_finalize`.

    Lifts the first choice's ``finish_reason`` to the top level, where the
    refusal check looks for it, and guarantees ``choices[0].message.content``
    exists so an empty job reports as empty rather than raising ``KeyError``.
    """
    response = dict(job.get("response") or {})
    choices = response.get("choices") or [{}]
    first = dict(choices[0])
    message = dict(first.get("message") or {})
    message.setdefault("content", "")
    first["message"] = message
    if first.get("finish_reason") and "finish_reason" not in response:
        response["finish_reason"] = first["finish_reason"]
    response["choices"] = [first, *choices[1:]]
    return response


def async_job_url(api_url: str) -> str:
    """Return the async-jobs endpoint for a synchronous chat-completions URL.

    ``https://api.perplexity.ai/chat/completions`` becomes
    ``https://api.perplexity.ai/async/chat/completions``.
    """
    base, sep, tail = api_url.rpartition("/chat/completions")
    if not sep:
        raise ValueError(f"cannot derive the Perplexity async endpoint from {api_url!r}")
    return f"{base}/async/chat/completions{tail}"


async def async_poll_research(self, query: str):
    """Drop-in replacement for ``PerplexityProvider.research`` using the async API.

    Submits the request as a job and polls its status with short requests, so
    no connection stays open while ``sonar-deep-research`` searches. The
    overall wait is bounded by the provider's configured timeout, defaulting to
    an hour, because a job can legitimately run for many minutes.
    """
    import httpx
    from deep_research_client.exceptions import ProviderNotConfiguredError

    logger.info("Starting Perplexity research query (model: %s, async job)", self.model)
    if not self.is_available():
        raise ProviderNotConfiguredError(self.name, self.unavailable_reason())

    headers = {"Authorization": f"Bearer {self.config.api_key}", "Content-Type": "application/json"}
    jobs_url = async_job_url(self.api_url)
    deadline = time.monotonic() + max(float(self.config.timeout or 0), 3600.0)
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
            submitted = await client.post(jobs_url, json={"request": _build_request(self, query)}, headers=headers)
            if submitted.status_code >= 400:
                raise ValueError(f"Perplexity API HTTP error: {submitted.status_code} - {submitted.text}")
            job = submitted.json()
            job_id = job.get("id")
            if not job_id:
                raise ValueError(f"Perplexity API error: async submit returned no job id: {submitted.text[:300]}")
            logger.info("Perplexity async job %s submitted", job_id)
            while job.get("status") not in _DONE_STATUSES:
                if time.monotonic() > deadline:
                    raise ValueError(
                        f"Perplexity API error: async job {job_id} still {job.get('status')!r} at the deadline"
                    )
                await asyncio.sleep(POLL_INTERVAL_SECONDS)
                if time.monotonic() > deadline:
                    # The sleep may have crossed the deadline; do not spend one more request.
                    raise ValueError(
                        f"Perplexity API error: async job {job_id} still {job.get('status')!r} at the deadline"
                    )
                try:
                    polled = await client.get(f"{jobs_url}/{job_id}", headers=headers)
                except httpx.TransportError as e:
                    # A dropped or timed-out poll is the proxy flakiness this path exists to
                    # survive: the job is still running server-side, so retry until the deadline.
                    logger.warning("Perplexity async poll for job %s raised %s; retrying", job_id, e)
                    continue
                if polled.status_code >= 500 or polled.status_code == 429:
                    # A transient server error or rate-limit on one poll is not the job failing.
                    logger.warning(
                        "Perplexity async poll for job %s returned %s; retrying", job_id, polled.status_code
                    )
                    continue
                if polled.status_code >= 400:
                    raise ValueError(
                        f"Perplexity API HTTP error: {polled.status_code} - {polled.text} (job {job_id})"
                    )
                job = polled.json()
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Perplexity API error: {e}") from e

    if job.get("status") == "FAILED":
        raise ValueError(f"Perplexity API error: async job {job_id} failed: {job.get('error_message')!r}")
    return _finalize(self, query, completed_job_data(job), f"async job {job_id}")


async def streaming_research(self, query: str):
    """Drop-in replacement for ``PerplexityProvider.research`` that streams.

    The fallback path (``DISMECH_PERPLEXITY_TRANSPORT=stream``). It keeps a
    connection alive only once the model starts emitting, so a long search
    phase can still hit an idle timeout; prefer :func:`async_poll_research`.
    """
    import httpx
    from deep_research_client.exceptions import ProviderNotConfiguredError

    logger.info("Starting Perplexity research query (model: %s, streaming)", self.model)
    if not self.is_available():
        raise ProviderNotConfiguredError(self.name, self.unavailable_reason())

    payload = _build_request(self, query)
    payload["stream"] = True
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

    data_lines = [line for line in lines if line.startswith("data:")]
    tail = data_lines[-1][:300] if data_lines else (lines[-1][:300] if lines else "")
    return _finalize(
        self,
        query,
        assemble_stream(lines),
        f"stream of {len(lines)} lines, {len(data_lines)} data events; last: {tail!r}",
    )


def selected_transport() -> str:
    """Return ``"stream"`` or ``"async"``, from :data:`TRANSPORT_ENV`."""
    return "stream" if os.environ.get(TRANSPORT_ENV, "").strip().lower() == "stream" else "async"


def install() -> bool:
    """Replace the upstream Perplexity request with the async (default) or streaming one.

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
    method = streaming_research if selected_transport() == "stream" else async_poll_research
    PerplexityProvider.research = method
    PerplexityProvider._dismech_streaming = True
    logger.info("Perplexity requests use the %s path", method.__name__)
    return True
