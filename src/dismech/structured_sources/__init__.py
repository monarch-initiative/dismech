"""Structured-database reference sources for dismech.

Each source ingests a structured knowledge base (XML, JSON, TSV) and emits
deterministic line-oriented markdown files into ``references_cache/`` so they
can be cited from disorder YAMLs and snippet-validated by
``linkml-reference-validator``.

The flagship source is :class:`OrphanetSource`; ClinGen Gene-Disease Validity
and Dosage Sensitivity assertions are also available.
"""

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)
from dismech.structured_sources.clingen import ClinGenSource
from dismech.structured_sources.clingen_dosage import ClinGenDosageSource
from dismech.structured_sources.orphanet import OrphanetSource

__all__ = [
    "BulkFile",
    "ReferenceCacheEntry",
    "StructuredSource",
    "ClinGenSource",
    "ClinGenDosageSource",
    "OrphanetSource",
]
