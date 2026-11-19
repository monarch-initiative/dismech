"""The cache filenames ``linkml-reference-validator`` gives a reference id.

dismech used to derive a cache filename itself, by replacing ``:`` ``/`` ``?``
and ``=`` with ``_``. From linkml-reference-validator 0.5.0 the validator also
caps a name at 200 bytes, ending it in a hash of the id, and gives a reference
whose usual name another reference already holds a hashed name of its own
(linkml/linkml-reference-validator#131, #132). A local copy of the old rule
would miss both, so every dismech lookup asks the validator instead.

>>> cache_filenames("PMID:12345")[0]
'PMID_12345.md'
>>> long_id = "url:https://example.org/" + "x" * 250
>>> name = cache_filenames(long_id)[0]
>>> len(name.encode("utf-8")) <= 200
True
"""

from __future__ import annotations

from pathlib import Path

from linkml_reference_validator.cache import (
    cache_filename,
    disambiguated_cache_filename,
    legacy_cache_filename,
)


def cache_filenames(reference_id: str) -> tuple[str, ...]:
    """Every filename the validator reads or writes for ``reference_id``, best first.

    The writer's name comes first. After it come the name used before
    ``url:`` fragments were dropped from cache keys, and the hashed name a
    reference gets when its usual one is taken. Duplicates are removed.

    >>> cache_filenames("url:https://ex.org/a.pdf#page=3")[:2]
    ('url_https___ex.org_a.pdf.md', 'url_https___ex.org_a.pdf#page_3.md')
    """
    names = [
        cache_filename(reference_id),
        legacy_cache_filename(reference_id),
        disambiguated_cache_filename(reference_id),
    ]
    return tuple(dict.fromkeys(names))


def cache_stems(reference_id: str) -> tuple[str, ...]:
    """The stems of :func:`cache_filenames`, for stem-keyed indexes."""
    return tuple(Path(name).stem for name in cache_filenames(reference_id))
