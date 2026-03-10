"""Monkey-patch linkml-reference-validator to handle network errors gracefully.

The upstream PMIDSource._fetch_pmc_xml, _fetch_pmc_html, and _fetch_abstract
methods lack try/except around NCBI network calls. When NCBI returns an
incomplete response or the connection drops, an unhandled IncompleteRead (or
similar) exception crashes the entire validation run.

This module patches those methods so network errors are caught and logged as
warnings, allowing validation to continue with abstract-only or degraded content
rather than crashing.

Usage: import this module before running linkml-reference-validator, e.g.:
    python -c "import dismech.patch_reference_validator" && linkml-reference-validator ...
Or via the wrapper script in scripts/run_reference_validator.py.
"""

import logging
from functools import wraps
from typing import Optional

logger = logging.getLogger("linkml_reference_validator.patch")


def _wrap_network_method(original, method_name):
    """Wrap a method to catch network errors and return None."""

    @wraps(original)
    def wrapper(*args, **kwargs):
        try:
            return original(*args, **kwargs)
        except Exception as exc:
            logger.warning(
                "Network error in %s (non-fatal, skipping): %s: %s",
                method_name,
                type(exc).__name__,
                exc,
            )
            return None

    return wrapper


def _wrap_fulltext_method(original):
    """Wrap _fetch_pmc_fulltext which returns a tuple."""

    @wraps(original)
    def wrapper(*args, **kwargs):
        try:
            return original(*args, **kwargs)
        except Exception as exc:
            logger.warning(
                "Network error in _fetch_pmc_fulltext (non-fatal, skipping): %s: %s",
                type(exc).__name__,
                exc,
            )
            return None, "network_error"

    return wrapper


def apply_patch():
    """Apply the monkey-patch to PMIDSource."""
    try:
        from linkml_reference_validator.etl.sources.pmid import PMIDSource
    except ImportError:
        logger.debug("linkml-reference-validator not installed, skipping patch")
        return

    if getattr(PMIDSource, "_network_patch_applied", False):
        return  # Already patched

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


# Auto-apply on import
apply_patch()
