"""Structured-database reference sources for dismech.

Each source ingests a structured knowledge base (XML, JSON, TSV) and emits
deterministic line-oriented markdown files into ``references_cache/`` so they
can be cited from disorder YAMLs and snippet-validated by
``linkml-reference-validator``.

The flagship source is :class:`OrphanetSource`; the framework
(:mod:`dismech.structured_sources.base`) is designed so additional
structured sources (OMIM, MONDO, HGNC, ...) can be added with a single
subclass + manifest entry.
"""

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)
from dismech.structured_sources.orphanet import OrphanetSource

__all__ = [
    "BulkFile",
    "ReferenceCacheEntry",
    "StructuredSource",
    "OrphanetSource",
]
