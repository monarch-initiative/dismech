#!/usr/bin/env python3
"""Warm the reference cache's full-text-attempt state.

Background
----------
`linkml-reference-validator` caches paper abstracts in ``references_cache/*.md``.
For any record still typed ``abstract_only`` (or ``unavailable`` / ``summary`` /
``no_pmc`` / ``pmc_restricted``) it will, on *every* validation run, re-enter the
full-text enrichment step: resolve the DOI through the provider chain
(PMC -> Europe PMC -> Unpaywall -> OpenAlex) and try to download the publisher
PDF. Closed-access publishers (Wiley, Hindawi, BMJ, ...) return HTTP 403, so the
same downloads are retried forever, wasting network on every ``just validate``.

The validator already knows how to stop this: once the provider chain completes
without a *raised* error it writes ``full_text_attempted: true`` into the cache
frontmatter, and thereafter skips the full-text step for that record
(``ReferenceFetcher._maybe_retry_full_text``). The only reason the retries keep
happening is that older cache files predate that flag.

What this script does
---------------------
Drive the *same* code path the validator uses (``ReferenceFetcher.fetch``) over
the cache records that still lack the flag, so each one is enriched with real
open-access full text where available and otherwise durably marked
``full_text_attempted: true``. It NEVER hand-edits cache files -- the fetcher
owns all writes, honoring the "never hand-edit references_cache" contract.

Because the work is gated on the flag, the sweep is **idempotent and resumable**:
records already flagged are skipped, so a bounded ``--limit`` run drains the
backlog incrementally and a periodic run only touches newly-added references.

Usage
-----
    uv run python scripts/warm_reference_cache.py --limit 200
    uv run python scripts/warm_reference_cache.py            # whole backlog
    uv run python scripts/warm_reference_cache.py --dry-run  # list targets only
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
import time
from pathlib import Path

from linkml_reference_validator.etl.reference_fetcher import (
    NEEDS_FULL_TEXT_TYPES,
    ReferenceFetcher,
)

# Applying the dismech network-resilience patch also imports the validator.
import dismech.patch_reference_validator  # noqa: F401
from dismech.frontmatter import split_frontmatter

try:
    # Reuse the CLI's config loader so we honor conf/reference_validator_config.yaml
    from linkml_reference_validator.cli.shared import load_validation_config
except Exception:  # pragma: no cover - defensive, layout differs across versions
    load_validation_config = None  # type: ignore[assignment]

logger = logging.getLogger("warm_reference_cache")

DEFAULT_CONFIG = Path("conf/reference_validator_config.yaml")

_CONTENT_TYPE_RE = re.compile(r'^content_type:\s*"?([A-Za-z_]+)"?\s*$', re.MULTILINE)
_REFERENCE_ID_RE = re.compile(r'^reference_id:\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)
_FLAG_RE = re.compile(r'^full_text_attempted:\s*true\s*$', re.MULTILINE)


def _frontmatter(path: Path) -> str | None:
    """Return the YAML frontmatter block of a cache markdown file, or None."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    # Delimiter-aware (issue #7697): a ``---`` inside a title used to truncate the
    # frontmatter here, hiding ``content_type:`` so the record could never be
    # selected for warming -- and the skip was unlogged.
    split = split_frontmatter(text)
    if split is None:
        return None
    return split.frontmatter


def find_targets(cache_dir: Path, content_types: set[str]) -> list[tuple[Path, str]]:
    """Cache records that need full text but have not yet been attempted.

    Returns ``(path, reference_id)`` pairs, sorted by filename for deterministic,
    resumable batching.
    """
    targets: list[tuple[Path, str]] = []
    for path in sorted(cache_dir.glob("*.md")):
        fm = _frontmatter(path)
        if fm is None:
            continue
        ct_match = _CONTENT_TYPE_RE.search(fm)
        if not ct_match or ct_match.group(1) not in content_types:
            continue
        if _FLAG_RE.search(fm):
            continue  # already durably attempted -- skip (the whole point)
        id_match = _REFERENCE_ID_RE.search(fm)
        if not id_match:
            logger.warning("Skipping %s: no reference_id in frontmatter", path.name)
            continue
        targets.append((path, id_match.group(1).strip()))
    return targets


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--config", type=Path, default=DEFAULT_CONFIG,
        help=f"reference-validator config file (default: {DEFAULT_CONFIG})",
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Max records to process this run (0 = no limit). Use a bounded "
             "limit for periodic/incremental sweeps.",
    )
    parser.add_argument(
        "--content-types", default=",".join(sorted(NEEDS_FULL_TEXT_TYPES)),
        help="Comma-separated content_types to warm (default: the validator's "
             "full-text-eligible set).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List the records that would be processed, then exit.",
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose logging.")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )

    if load_validation_config is None:
        print("ERROR: could not import load_validation_config from the validator.", file=sys.stderr)
        return 2

    config_file = args.config if args.config.exists() else None
    if args.config and config_file is None:
        logger.warning("Config %s not found; using validator defaults.", args.config)
    config = load_validation_config(config_file)

    cache_dir = Path(config.cache_dir)
    if not cache_dir.exists():
        print(f"ERROR: cache dir {cache_dir} does not exist.", file=sys.stderr)
        return 2

    content_types = {c.strip() for c in args.content_types.split(",") if c.strip()}
    targets = find_targets(cache_dir, content_types)

    total_backlog = len(targets)
    if args.limit > 0:
        targets = targets[: args.limit]

    print(
        f"Cache dir: {cache_dir}\n"
        f"Backlog (needs-full-text, flag unset): {total_backlog}\n"
        f"Processing this run: {len(targets)}"
        + (f" (--limit {args.limit})" if args.limit > 0 else " (all)")
    )

    if args.dry_run:
        for path, ref_id in targets:
            print(f"  {ref_id}  ({path.name})")
        return 0

    fetcher = ReferenceFetcher(config)

    processed = flagged = enriched = still_unset = errors = 0
    start = time.monotonic()

    for i, (path, ref_id) in enumerate(targets, 1):
        processed += 1
        try:
            # Return value is intentionally discarded; we re-read the persisted
            # frontmatter below to report the true on-disk outcome.
            fetcher.fetch(ref_id)
        except Exception as exc:  # a single bad record must not abort the sweep
            errors += 1
            logger.warning("fetch() raised for %s: %s: %s", ref_id, type(exc).__name__, exc)
            continue

        # Re-read the persisted state to report the true on-disk outcome.
        fm = _frontmatter(path) or ""
        now_flagged = bool(_FLAG_RE.search(fm))
        ct_match = _CONTENT_TYPE_RE.search(fm)
        now_ct = ct_match.group(1) if ct_match else None

        if now_ct not in content_types:
            enriched += 1  # content_type advanced to a full_text_* type
        elif now_flagged:
            flagged += 1
        else:
            # Chain hit a raised/transient error; stays retryable next run.
            still_unset += 1

        if args.verbose or i % 50 == 0:
            print(
                f"  [{i}/{len(targets)}] {ref_id} -> "
                f"{'full-text' if now_ct not in content_types else ('flagged' if now_flagged else 'unresolved')}",
                flush=True,
            )

    elapsed = time.monotonic() - start
    remaining = total_backlog - (flagged + enriched)
    print(
        "\nSummary:\n"
        f"  processed:            {processed}\n"
        f"  enriched (full text): {enriched}\n"
        f"  marked attempted:     {flagged}\n"
        f"  still unresolved:     {still_unset}   (transient error; retried next run)\n"
        f"  errors:               {errors}\n"
        f"  backlog remaining:    {remaining}\n"
        f"  elapsed:              {elapsed:.0f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
