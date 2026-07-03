"""Pluggable text-embedding backends.

An :class:`Embedder` maps a sequence of strings to a 2-D ``float32`` array of
shape ``(n_texts, dim)``. Backends are resolved by a ``"backend[:model]"``
spec string via :func:`get_embedder`, e.g.::

    get_embedder("model2vec")                       # local static, no torch
    get_embedder("model2vec:minishlab/potion-base-32M")
    get_embedder("openai")                          # text-embedding-3-small
    get_embedder("openai:text-embedding-ada-002")   # legacy ada
    get_embedder("openai:text-embedding-3-large")

New backends register with :func:`register_backend`. Heavy / optional
dependencies (``model2vec``, ``openai``) are imported lazily so this module
imports cleanly without them installed.
"""

from __future__ import annotations

import os
from typing import Protocol, Sequence, runtime_checkable

import numpy as np


@runtime_checkable
class Embedder(Protocol):
    """A text embedder. Implementations must be deterministic for a fixed model."""

    #: Stable identifier including the resolved model, e.g. ``"openai:ada-002"``.
    name: str

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        """Return an ``(len(texts), dim)`` float32 array of embeddings."""
        ...


class StaticEmbedder:
    """Local static embeddings via `model2vec` (fast, CPU-only, no torch)."""

    DEFAULT_MODEL = "minishlab/potion-base-8M"

    def __init__(self, model: str | None = None):
        self.model_id = model or self.DEFAULT_MODEL
        self.name = f"model2vec:{self.model_id}"
        self._model = None

    def _ensure(self):
        if self._model is None:
            from model2vec import StaticModel  # lazy optional dep

            self._model = StaticModel.from_pretrained(self.model_id)
        return self._model

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        vecs = self._ensure().encode(list(texts))
        return np.asarray(vecs, dtype=np.float32)


class OpenAIEmbedder:
    """OpenAI embeddings (``text-embedding-3-*`` or legacy ``ada-002``).

    Reads ``OPENAI_API_KEY`` from the environment unless ``api_key`` is passed.
    Requests are batched; empty strings are sent as a single space because the
    API rejects empty input.
    """

    DEFAULT_MODEL = "text-embedding-3-small"

    def __init__(
        self,
        model: str | None = None,
        *,
        batch_size: int = 256,
        api_key: str | None = None,
    ):
        self.model_id = model or self.DEFAULT_MODEL
        self.name = f"openai:{self.model_id}"
        self.batch_size = batch_size
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self._client = None

    def _ensure(self):
        if self._client is None:
            if not self._api_key:
                raise RuntimeError(
                    "OPENAI_API_KEY is not set; export it or pass api_key=..."
                )
            from openai import OpenAI  # lazy optional dep

            self._client = OpenAI(api_key=self._api_key)
        return self._client

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        client = self._ensure()
        texts = list(texts)
        out: list[list[float]] = []
        for i in range(0, len(texts), self.batch_size):
            chunk = [t if t else " " for t in texts[i : i + self.batch_size]]
            resp = client.embeddings.create(model=self.model_id, input=chunk)
            out.extend(item.embedding for item in resp.data)
        return np.asarray(out, dtype=np.float32)


_BACKENDS: dict[str, type] = {
    "model2vec": StaticEmbedder,
    "openai": OpenAIEmbedder,
}


def register_backend(name: str, cls: type) -> None:
    """Register a custom embedding backend under ``name``."""
    _BACKENDS[name] = cls


def available_backends() -> list[str]:
    return sorted(_BACKENDS)


def get_embedder(spec: str = "model2vec", **kwargs) -> Embedder:
    """Resolve a ``"backend[:model]"`` spec to an :class:`Embedder` instance.

    Extra keyword args are forwarded to the backend constructor (e.g.
    ``batch_size``, ``api_key``).
    """
    backend, _, model = spec.partition(":")
    if backend not in _BACKENDS:
        raise ValueError(
            f"unknown embedding backend {backend!r}; "
            f"available: {available_backends()}"
        )
    if model:
        kwargs.setdefault("model", model)
    return _BACKENDS[backend](**kwargs)
