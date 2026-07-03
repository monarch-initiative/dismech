"""Monkey-patch linkml-reference-validator to handle network errors gracefully.

The upstream PMIDSource._fetch_pmc_xml, _fetch_pmc_html, and _fetch_abstract
methods lack try/except around NCBI network calls. When NCBI returns an
incomplete response or the connection drops, an unhandled IncompleteRead (or
similar) exception crashes the entire validation run.

This module patches those methods so network errors are caught and retried
(with exponential backoff), allowing validation to continue with abstract-only
or degraded content rather than crashing.

Usage: import this module before running linkml-reference-validator, e.g.:
    python -c "import dismech.patch_reference_validator" && linkml-reference-validator ...
Or via the wrapper script in scripts/run_reference_validator.sh.
"""

import logging
import time
from functools import wraps

logger = logging.getLogger("linkml_reference_validator.patch")

MAX_RETRIES = 3
BACKOFF_BASE = 2  # seconds


def _coerce_author(author):
    """Coerce a single author value to a string, or ``None`` to drop it.

    Some cached reference records (written by older validator versions) store a
    corporate/consortium author whose name contains a colon -- e.g.
    ``"... Consortium. Electronic address: x@y"`` -- unquoted, so YAML reparses it
    as a *mapping* on the next load. Others carry a ``None`` or a nested list.
    Upstream ``ReferenceFetcher._save_to_disk`` assumes plain strings (it calls
    ``.strip()`` per author and ``", ".join(authors)``) and crashes on these, and
    it cannot even regenerate the affected records because it re-loads them first.
    Reconstruct a readable string so the record round-trips cleanly.
    """
    if author is None:
        return None
    if isinstance(author, str):
        return author
    if isinstance(author, dict):
        # A "Name. Electronic address: email" string reparsed as {name: email}.
        parts = []
        for key, value in author.items():
            key_text = "" if key is None else str(key)
            if value in (None, ""):
                parts.append(key_text)
            else:
                parts.append(f"{key_text}: {value}")
        text = ", ".join(p for p in parts if p)
        return text or None
    if isinstance(author, (list, tuple, set)):
        subs = [_coerce_author(item) for item in author]
        text = ", ".join(s for s in subs if s)
        return text or None
    return str(author)


def _coerce_authors(authors):
    """Normalize a reference's ``authors`` to a list of non-empty strings."""
    if not authors:
        return authors
    if isinstance(authors, str):
        return [authors]
    coerced = [_coerce_author(a) for a in authors]
    return [a for a in coerced if a]


def _wrap_network_method(original, method_name):
    """Wrap a method to retry on network errors, then return None on failure."""

    @wraps(original)
    def wrapper(*args, **kwargs):
        for attempt in range(MAX_RETRIES + 1):
            try:
                return original(*args, **kwargs)
            except Exception as exc:
                if attempt < MAX_RETRIES:
                    delay = BACKOFF_BASE ** (attempt + 1)
                    logger.warning(
                        "Network error in %s (attempt %d/%d, retrying in %ds): %s: %s",
                        method_name,
                        attempt + 1,
                        MAX_RETRIES + 1,
                        delay,
                        type(exc).__name__,
                        exc,
                    )
                    time.sleep(delay)
                else:
                    logger.warning(
                        "Network error in %s (all %d attempts failed, skipping): %s: %s",
                        method_name,
                        MAX_RETRIES + 1,
                        type(exc).__name__,
                        exc,
                    )
                    return None

    return wrapper


def _wrap_fulltext_method(original):
    """Wrap _fetch_pmc_fulltext which returns a tuple."""

    @wraps(original)
    def wrapper(*args, **kwargs):
        for attempt in range(MAX_RETRIES + 1):
            try:
                return original(*args, **kwargs)
            except Exception as exc:
                if attempt < MAX_RETRIES:
                    delay = BACKOFF_BASE ** (attempt + 1)
                    logger.warning(
                        "Network error in _fetch_pmc_fulltext (attempt %d/%d, retrying in %ds): %s: %s",
                        attempt + 1,
                        MAX_RETRIES + 1,
                        delay,
                        type(exc).__name__,
                        exc,
                    )
                    time.sleep(delay)
                else:
                    logger.warning(
                        "Network error in _fetch_pmc_fulltext (all %d attempts failed, skipping): %s: %s",
                        MAX_RETRIES + 1,
                        type(exc).__name__,
                        exc,
                    )
                    return None, "network_error"

    return wrapper


def apply_patch():
    """Apply monkey-patches for network resilience and cache compatibility."""
    try:
        from linkml_reference_validator.etl.sources.pmid import PMIDSource
        from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
    except ImportError:
        logger.debug("linkml-reference-validator not installed, skipping patch")
        return

    if not getattr(PMIDSource, "_network_patch_applied", False):
        PMIDSource._fetch_pmc_xml = _wrap_network_method(
            PMIDSource._fetch_pmc_xml, "PMIDSource._fetch_pmc_xml"
        )
        PMIDSource._fetch_pmc_html = _wrap_network_method(
            PMIDSource._fetch_pmc_html, "PMIDSource._fetch_pmc_html"
        )
        PMIDSource._fetch_abstract = _wrap_network_method(
            PMIDSource._fetch_abstract, "PMIDSource._fetch_abstract"
        )
        PMIDSource._fetch_pmc_fulltext = _wrap_fulltext_method(
            PMIDSource._fetch_pmc_fulltext
        )

        PMIDSource._network_patch_applied = True  # type: ignore[attr-defined]
        logger.debug("Applied network resilience patch to PMIDSource")

    if not getattr(ReferenceFetcher, "_clinicaltrials_cache_patch_applied", False):
        original_get_cache_path = ReferenceFetcher.get_cache_path

        @wraps(original_get_cache_path)
        def get_cache_path_with_clinicaltrials_compat(self, reference_id: str):
            if reference_id.upper().startswith("CLINICALTRIALS:"):
                _, identifier = reference_id.split(":", 1)
                reference_id = f"clinicaltrials:{identifier}"
            return original_get_cache_path(self, reference_id)

        ReferenceFetcher.get_cache_path = get_cache_path_with_clinicaltrials_compat
        ReferenceFetcher._clinicaltrials_cache_patch_applied = True  # type: ignore[attr-defined]
        logger.debug("Applied ClinicalTrials.gov cache path compatibility patch")

    if not getattr(ReferenceFetcher, "_author_coercion_patch_applied", False):
        original_save_to_disk = ReferenceFetcher._save_to_disk

        @wraps(original_save_to_disk)
        def save_to_disk_with_author_coercion(self, reference):
            # Normalize non-string authors (dict/None/nested-list from stale cache
            # records) before upstream serialization, which assumes plain strings.
            try:
                reference.authors = _coerce_authors(reference.authors)
            except Exception as exc:  # never let normalization abort the save
                logger.warning("Author normalization failed, dropping authors: %s", exc)
                reference.authors = None
            return original_save_to_disk(self, reference)

        ReferenceFetcher._save_to_disk = save_to_disk_with_author_coercion
        ReferenceFetcher._author_coercion_patch_applied = True  # type: ignore[attr-defined]
        logger.debug("Applied author-normalization patch to ReferenceFetcher._save_to_disk")


# Auto-apply on import
apply_patch()
