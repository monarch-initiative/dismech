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

import io
import logging
import re
import time
from functools import wraps

from bs4 import BeautifulSoup
from ruamel.yaml import YAML

from dismech.frontmatter import contains_frontmatter_delimiter, split_frontmatter

logger = logging.getLogger("linkml_reference_validator.patch")

MAX_RETRIES = 3
BACKOFF_BASE = 2  # seconds

# PMIDSource methods that make NCBI network calls and so need retry wrapping.
# Names missing from the installed version are skipped; if *nothing* matches, the
# patch warns rather than crashing (see ``apply_patch``).
#
# Independent methods, each wrapped whenever present:
PMID_NETWORK_METHODS = ("_fetch_pmc_xml", "_fetch_pmc_html")
# Mutually exclusive spellings of the same PubMed fetch, newest first: 0.2.1
# split ``_fetch_abstract`` into ``_fetch_pubmed_xml`` (network) plus
# ``_parse_abstract`` (parsing). Only the FIRST match is wrapped. If a later
# release reintroduces ``_fetch_abstract`` as a thin shim over
# ``_fetch_pubmed_xml``, wrapping both would nest the retries -- 4 x 4 attempts
# with backoff, minutes per reference -- so this is a first-wins list, not a set.
PMID_FETCH_ALTERNATIVES = ("_fetch_pubmed_xml", "_fetch_abstract")

# A ClinicalTrials.gov registry id written without its ``clinicaltrials:`` prefix.
_BARE_NCT_RE = re.compile(r"^NCT\d+$", re.IGNORECASE)

_YAML_SAFE = YAML(typ="safe")
_YAML_SAFE.default_flow_style = False


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


def _wrap_save_to_disk(original):
    """Wrap ``ReferenceFetcher._save_to_disk`` to normalize ``authors`` first.

    Extra positional/keyword arguments are forwarded blind on purpose: this
    wrapper cares only about ``reference``, and pinning the rest of the signature
    turns every upstream parameter addition into a crash. 0.2.1 added ``private=``
    (passed from ``_save_by_access``), and because the wrapper had named its
    parameters exactly, every patched fetch of an *uncached* reference died with
    "unexpected keyword argument 'private'" -- i.e. ``just validate-disorders``
    on any entry citing something not already in ``references_cache/``. Do not
    re-narrow this signature.
    """

    @wraps(original)
    def wrapper(self, reference, *args, **kwargs):
        # Normalize non-string authors (dict/None/nested-list from stale cache
        # records) before upstream serialization, which assumes plain strings.
        try:
            reference.authors = _coerce_authors(reference.authors)
        except Exception as exc:  # never let normalization abort the save
            logger.warning("Author normalization failed, dropping authors: %s", exc)
            reference.authors = None
        return original(self, reference, *args, **kwargs)

    return wrapper


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

    # Ownership marker, checked by the tests instead of `__wrapped__`:
    # `functools.wraps` sets `__wrapped__` on anything it decorates, so if
    # upstream ever decorates one of these methods itself, a `__wrapped__` check
    # would pass while this patch was not applied at all -- a guard that has
    # silently stopped guarding.
    wrapper._dismech_network_retry = True
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


def _wrap_xml_extractor(original):
    """Recover JATS bodies carrying the harmless ``restricted-by`` metadata tag.

    Current PMC/Europe PMC JATS 1.4 documents can include
    ``<restricted-by>pmc</restricted-by>`` in ``processing-meta`` even when the
    complete article body is present.  Upstream treats any occurrence of the
    word ``restricted`` as an unavailable article and discards that body.  Keep
    its normal behavior first, then recover only documents that actually contain
    non-empty body paragraphs; genuinely restricted records still have no body
    and remain unavailable.
    """

    @wraps(original)
    def wrapper(self, data, *args, **kwargs):
        result = original(self, data, *args, **kwargs)
        if result is not None:
            return result

        text_data = data.decode("utf-8") if isinstance(data, bytes) else data
        if "<restricted-by" not in text_data:
            return None

        soup = BeautifulSoup(text_data, "xml")
        body = soup.find("body")
        if body is None:
            return None
        paragraphs = [
            paragraph.get_text()
            for paragraph in body.find_all("p")
            if paragraph.get_text().strip()
        ]
        return "\n\n".join(paragraphs) if paragraphs else None

    return wrapper


def _dump_frontmatter(data) -> str:
    """Serialize a frontmatter mapping back to YAML text."""
    buffer = io.StringIO()
    _YAML_SAFE.dump(data, buffer)
    return buffer.getvalue()


# Frontmatter keys upstream ``_load_markdown_format`` does not pass through
# verbatim: it wraps a scalar into a list, or stringifies it. A held-back value
# has to be normalized the same way, or restoring it would hand callers a bare
# ``str`` where upstream guarantees ``list[str]``.
_LIST_WRAPPED_KEYS = frozenset({"authors", "keywords"})
_STRINGIFIED_KEYS = frozenset({"year"})


def _normalize_deferred_value(key, value):
    """Apply upstream's own field normalization to a held-back value."""
    if key in _LIST_WRAPPED_KEYS:
        if not value:
            return None
        return value if isinstance(value, list) else [value]
    if key in _STRINGIFIED_KEYS:
        return str(value) if value else None
    return value


def _wrap_load_markdown_format(original):
    """Make the cache loader's frontmatter split delimiter-aware (issue #7697).

    Upstream ``_load_markdown_format`` starts with ``content_text.split("---", 2)``,
    which ends the frontmatter at the first ``---`` *substring* rather than at the
    first ``---`` *line*. Titles legitimately contain ``---`` (MMWR's
    ``Disease---Location, Year``; pre-1996 NLM ASCII arrows such as
    ``A----G(8344)``), so those records either crash the run with an unterminated
    quoted scalar or silently lose the title and every field after it.

    Rather than reimplement the upstream method — it maps two dozen frontmatter
    keys onto ``ReferenceContent`` and we do not want to track that — this wrapper
    only fixes the split. It parses the frontmatter correctly, holds back the
    entries whose values contain ``---``, hands upstream a reconstructed document
    that the naive split *does* read correctly, and then restores the held-back
    values onto the returned object. Files with no ``---`` inside their
    frontmatter (33,308 of 33,309 in this repo today) take an early return and are
    byte-for-byte unaffected.

    This is a stopgap for the pinned ``linkml-reference-validator``; the real fix
    belongs upstream, on both the read and the write side.
    """

    @wraps(original)
    def wrapper(self, content_text, reference_id, *args, **kwargs):
        split = split_frontmatter(content_text)
        if split is None or "---" not in split.frontmatter:
            return original(self, content_text, reference_id, *args, **kwargs)

        try:
            data = _YAML_SAFE.load(split.frontmatter)
        except Exception as exc:
            logger.warning(
                "Delimiter-aware frontmatter parse failed for %s, "
                "falling back to upstream behaviour: %s: %s",
                reference_id,
                type(exc).__name__,
                exc,
            )
            return original(self, content_text, reference_id, *args, **kwargs)

        if not isinstance(data, dict):
            return original(self, content_text, reference_id, *args, **kwargs)

        deferred = {
            key: value
            for key, value in data.items()
            if contains_frontmatter_delimiter(key)
            or contains_frontmatter_delimiter(value)
        }
        if not deferred:
            return original(self, content_text, reference_id, *args, **kwargs)

        safe = {key: value for key, value in data.items() if key not in deferred}
        try:
            sanitized = f"---\n{_dump_frontmatter(safe)}---\n{split.body}"
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning(
                "Could not re-serialize frontmatter for %s, "
                "falling back to upstream behaviour: %s: %s",
                reference_id,
                type(exc).__name__,
                exc,
            )
            return original(self, content_text, reference_id, *args, **kwargs)

        result = original(self, sanitized, reference_id, *args, **kwargs)
        if result is None:
            return result

        restored = []
        for key, value in deferred.items():
            if not isinstance(key, str) or not hasattr(result, key):
                continue
            try:
                setattr(result, key, _normalize_deferred_value(key, value))
            except Exception as exc:  # pragma: no cover - defensive
                logger.debug("Could not restore %r on %s: %s", key, reference_id, exc)
                continue
            restored.append(key)

        logger.debug(
            "Recovered frontmatter field(s) %s containing '---' for %s",
            ", ".join(restored) or "(none applicable)",
            reference_id,
        )
        return result

    return wrapper


def apply_patch():
    """Apply monkey-patches for network resilience and cache compatibility."""
    try:
        from linkml_reference_validator.etl.extract.xml import XMLExtractor
        from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
        from linkml_reference_validator.etl.sources.pmid import PMIDSource
    except ImportError:
        logger.debug("linkml-reference-validator not installed, skipping patch")
        return

    if not getattr(PMIDSource, "_network_patch_applied", False):
        # Upstream reshuffles these between releases: 0.2.1 split the old
        # ``_fetch_abstract`` into a network half (``_fetch_pubmed_xml``) and a
        # pure-parsing half (``_parse_abstract``). Wrap whichever of the known
        # NCBI-touching methods this version actually has, rather than raising
        # AttributeError at import time and taking every consumer down with it.
        wrapped = []

        def wrap_if_present(method_name):
            original = getattr(PMIDSource, method_name, None)
            if original is None:
                return False
            setattr(
                PMIDSource,
                method_name,
                _wrap_network_method(original, f"PMIDSource.{method_name}"),
            )
            wrapped.append(method_name)
            return True

        for method_name in PMID_NETWORK_METHODS:
            wrap_if_present(method_name)

        # First match only -- see PMID_FETCH_ALTERNATIVES on why wrapping both
        # spellings would nest the retries.
        for method_name in PMID_FETCH_ALTERNATIVES:
            if wrap_if_present(method_name):
                break

        if not wrapped:
            # Every known name is gone: the upstream API moved somewhere this
            # patch does not follow, and validation runs are now unprotected
            # against NCBI dropping a connection. Say so loudly.
            logger.warning(
                "None of the expected PMIDSource network methods (%s) are present; "
                "network-resilience patch not applied. linkml-reference-validator "
                "may have renamed them -- update PMID_NETWORK_METHODS / "
                "PMID_FETCH_ALTERNATIVES.",
                ", ".join(PMID_NETWORK_METHODS + PMID_FETCH_ALTERNATIVES),
            )

        if hasattr(PMIDSource, "_fetch_pmc_fulltext"):
            PMIDSource._fetch_pmc_fulltext = _wrap_fulltext_method(
                PMIDSource._fetch_pmc_fulltext
            )

        PMIDSource._network_patch_applied = True  # type: ignore[attr-defined]
        logger.debug("Applied network resilience patch to PMIDSource (%s)", wrapped)

    if not getattr(XMLExtractor, "_restricted_by_patch_applied", False):
        XMLExtractor.extract = _wrap_xml_extractor(XMLExtractor.extract)
        XMLExtractor._restricted_by_patch_applied = True  # type: ignore[attr-defined]
        logger.debug("Applied restricted-by metadata patch to XMLExtractor")

    if not getattr(ReferenceFetcher, "_clinicaltrials_cache_patch_applied", False):
        original_get_cache_path = ReferenceFetcher.get_cache_path

        @wraps(original_get_cache_path)
        def get_cache_path_with_clinicaltrials_compat(self, reference_id: str):
            if reference_id.upper().startswith("CLINICALTRIALS:"):
                _, identifier = reference_id.split(":", 1)
                reference_id = f"clinicaltrials:{identifier}"
            elif _BARE_NCT_RE.match(reference_id.strip()):
                # Upstream ``_parse_reference_id`` has no rule for a *bare* NCT id,
                # so it falls through to ("UNKNOWN", id) and the lookup derives
                # ``NCT….md``. The record is nevertheless *saved* under the
                # ClinicalTrials source's canonical id (``clinicaltrials_NCT….md``),
                # so read and write disagree and the reference is re-fetched from
                # ClinicalTrials.gov on every run. Align the read with the write.
                reference_id = f"clinicaltrials:{reference_id.strip().upper()}"
            return original_get_cache_path(self, reference_id)

        ReferenceFetcher.get_cache_path = get_cache_path_with_clinicaltrials_compat
        ReferenceFetcher._clinicaltrials_cache_patch_applied = True  # type: ignore[attr-defined]
        logger.debug(
            "Applied ClinicalTrials.gov cache path compatibility patch "
            "(prefixed case variants and bare NCT ids)"
        )

    if not getattr(ReferenceFetcher, "_author_coercion_patch_applied", False):
        ReferenceFetcher._save_to_disk = _wrap_save_to_disk(
            ReferenceFetcher._save_to_disk
        )
        ReferenceFetcher._author_coercion_patch_applied = True  # type: ignore[attr-defined]
        logger.debug(
            "Applied author-normalization patch to ReferenceFetcher._save_to_disk"
        )

    if not getattr(ReferenceFetcher, "_frontmatter_split_patch_applied", False):
        ReferenceFetcher._load_markdown_format = _wrap_load_markdown_format(
            ReferenceFetcher._load_markdown_format
        )
        ReferenceFetcher._frontmatter_split_patch_applied = True  # type: ignore[attr-defined]
        logger.debug(
            "Applied delimiter-aware frontmatter split patch to "
            "ReferenceFetcher._load_markdown_format"
        )


# Auto-apply on import
apply_patch()
