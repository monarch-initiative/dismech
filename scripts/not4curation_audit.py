#!/usr/bin/env python3
"""Audit KB ontology bindings for terms their own maintainers flag ``Not4Curation``.

RGD-curated ontologies (XCO, and its siblings) keep terms they want for
hierarchy and structural completeness but do *not* want used for annotation, and
mark them with a related synonym literally reading ``Not4Curation``. It is a
synonym, not a ``deprecated``/``obsolete`` axiom, which is exactly why a flagged
term passes every check dismech performs (issue #8472):

* it exists in the ontology,
* its canonical label matches the ``term.label`` written in the YAML, and
* it is reachable from the dynamic enum's ``source_nodes``.

Three flagged XCO terms (``XCO:0000294`` estrogen/estrogen analog,
``XCO:0000950`` anticonvulsant, ``XCO:0000561`` antidepressant) reached the
#8430 binding tranches on exactly that basis. All three had proper ECTO
equivalents; nothing in the toolchain would have caught any of them, and only a
reviewer noticing one instance led to the other two being found by hand.

The cache layer is the subtle half. ``cache/enums/*.csv`` is the offline
positive-hit set for ``reachable_from``, so a flagged CURIE that was cached
before anyone noticed the flag validates offline forever, with no network call
that could surface it. Hand-deleting rows from a validator-written cache is the
wrong fix (see the cache guardrails in ``CLAUDE.md``), which is what makes a
separate gate the only clean answer. This audit therefore *also* reports flagged
CURIEs sitting in the caches but not used in ``kb/`` — as an advisory note, never
as a failure, since a cached-but-unused row harms nothing until a curator reaches
for it.

**Scope.** The marker check is a generic synonym-substring test, so it costs
nothing on ontologies that never use the convention: of everything dismech binds
against, only XCO carries the marker today (24 of its 1,816 terms), and ECTO,
GENO and OPL carry none. The check runs over prefixes whose ``conf/oak_config.yaml``
adapter is *local* (``sqlite:*``), which answers an alias query per term offline
in about a millisecond. Prefixes served over OLS are skipped by default and
reported as skipped: checking them means one network round trip per term, and the
KB binds ~18,000 of them. ``--include-remote`` opts in anyway.

**Stopgap.** This belongs upstream in ``linkml-term-validator``, alongside the
existence and label checks it already performs — any LinkML knowledge base
consuming RGD ontologies has the same gap. It lives here because the validator is
a pinned external dependency and this closes the gap now.

Usage::

    uv run python scripts/not4curation_audit.py
    uv run python scripts/not4curation_audit.py kb/disorders/Asthma.yaml
    uv run python scripts/not4curation_audit.py --warn-only
    uv run python scripts/not4curation_audit.py --list-flagged --prefix XCO
    uv run python scripts/not4curation_audit.py --format json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path

#: Files scanned when no explicit path is given: every curated KB entry plus the
#: schema, whose static ``meaning:`` values are ontology bindings too and are
#: validated by `just validate-terms-schema` under the same blind spot.
#: Every ``kb/`` subtree at any depth, deliberately rather than a hand-listed
#: few: a subtree added later carries bindings the moment somebody curates into
#: it, and a scope that silently omits it is the kind of gap this check exists
#: to close. Recursive because ``kb/hypotheses/`` nests three levels deep
#: (``<Disease>/<hypothesis>/assessments/*.yaml``).
DEFAULT_TARGETS = (
    "kb/**/*.yaml",
    "src/dismech/schema/dismech.yaml",
)

#: Synonym markers meaning "exists, but do not annotate with this". ``Not4Curation``
#: is RGD's; ``not_recommended_for_annotation`` is the equivalent convention used
#: by some other OBO ontologies. Compared against a synonym normalized to
#: lowercase alphanumerics, so spacing, casing and separators do not matter.
DEFAULT_MARKERS = ("not4curation", "notrecommendedforannotation")

_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9._]*):([A-Za-z0-9_][A-Za-z0-9_.\-]*)$")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def _normalize_marker(text: str) -> str:
    """Reduce a synonym to lowercase alphanumerics for marker matching."""
    return _NON_ALNUM_RE.sub("", str(text).lower())


@dataclass(frozen=True)
class Usage:
    """One occurrence of a CURIE in a scanned file."""

    curie: str
    path: str
    location: str

    def format(self) -> str:
        return f"{self.path}: {self.location}"


@dataclass
class Flagged:
    """A CURIE carrying a marker synonym, with wherever it is used."""

    curie: str
    label: str
    marker: str
    synonym: str
    usages: list[Usage] = field(default_factory=list)
    cached_in: list[str] = field(default_factory=list)


@dataclass
class Report:
    """Everything one audit run found, so callers can format it themselves."""

    checked_prefixes: dict[str, int] = field(default_factory=dict)
    #: Per prefix, how many of the checked CURIEs the adapter returned any synonym
    #: for. A prefix whose count is 0 was looked up but effectively not checked —
    #: a marker is a synonym, so an adapter returning none can never find one.
    synonym_hits: dict[str, int] = field(default_factory=dict)
    skipped_prefixes: dict[str, str] = field(default_factory=dict)
    #: The subset of ``skipped_prefixes`` skipped because the adapter would not
    #: build (offline, bucket outage), as opposed to being out of scope by
    #: choice. Kept as its own set so ``--require-adapters`` does not have to
    #: substring-match the wording of a human-readable reason.
    unavailable_prefixes: dict[str, str] = field(default_factory=dict)
    in_use: list[Flagged] = field(default_factory=list)
    cached_only: list[Flagged] = field(default_factory=list)
    inventory: list[Flagged] = field(default_factory=list)

    @property
    def curies_checked(self) -> int:
        return sum(self.checked_prefixes.values())


# --------------------------------------------------------------------------
# Collecting bound CURIEs
# --------------------------------------------------------------------------


def _walk(node: object, breadcrumb: str) -> Iterator[tuple[str, str]]:
    """Yield ``(scalar, breadcrumb)`` for every string scalar in a loaded document."""
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{breadcrumb}.{key}" if breadcrumb else str(key)
            yield from _walk(value, child)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _walk(value, f"{breadcrumb}[{index}]")
    elif isinstance(node, str):
        yield node, breadcrumb


def collect_usages(paths: Iterable[Path], prefixes: Iterable[str]) -> list[Usage]:
    """Collect every CURIE in ``paths`` whose prefix is in ``prefixes``.

    Restricting to in-scope ontology prefixes is what keeps this from matching
    the many other colon-shaped strings in a KB entry (``PMID:...``,
    ``clinicaltrials:...``, ``skos:exactMatch``): those prefixes are never bound
    to an ontology adapter, so they are never in scope.
    """
    wanted = set(prefixes)
    usages: list[Usage] = []
    for path in paths:
        try:
            document = safe_load_path(path)
        except (
            Exception
        ) as exc:  # pragma: no cover - malformed YAML is another check's job
            print(f"warning: could not parse {path}: {exc}", file=sys.stderr)
            continue
        rel = _relative(path)
        for scalar, breadcrumb in _walk(document, ""):
            match = _CURIE_RE.match(scalar)
            if match and match.group(1) in wanted:
                usages.append(Usage(curie=scalar, path=rel, location=breadcrumb or "-"))
    return usages


def collect_cached(cache_dir: Path, prefixes: Iterable[str]) -> dict[str, list[str]]:
    """Map each in-scope cached CURIE to the cache files holding it.

    Covers both caches that stand in for an authority: ``cache/<prefix>/terms.csv``
    (labels) and ``cache/enums/*.csv`` (dynamic-enum membership).
    """
    wanted = set(prefixes)
    cached: dict[str, list[str]] = {}
    if not cache_dir.is_dir():
        return cached
    # Same two globs (and the same ``enums`` exclusion) as
    # ``dismech.term_cache_integrity.discover_cache_files``, so the two scanners
    # cannot disagree about what the caches are.
    files = [
        path
        for path in sorted(cache_dir.glob("*/terms.csv"))
        if path.parent.name != "enums"
    ] + sorted((cache_dir / "enums").glob("*.csv"))
    for path in files:
        rel = _relative(path)
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:  # pragma: no cover - unreadable cache is another check's job
            continue
        for line in lines[1:]:
            curie = line.split(",", 1)[0].strip().strip('"')
            match = _CURIE_RE.match(curie)
            if match and match.group(1) in wanted:
                cached.setdefault(curie, []).append(rel)
    return cached


def _relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(_REPO_ROOT))
    except ValueError:
        return str(path)


# --------------------------------------------------------------------------
# Ontology lookups
# --------------------------------------------------------------------------


def load_adapter_map(oak_config: Path) -> dict[str, str]:
    """Read ``prefix -> adapter string`` out of the OAK config, dropping skips."""
    config = safe_load_path(oak_config) or {}
    adapters = config.get("ontology_adapters") or {}
    return {str(k): str(v) for k, v in adapters.items() if str(v).strip()}


def is_local(adapter: str) -> bool:
    """True for adapters that answer an alias query offline, per term.

    Everything else (today: ``ols:``) costs a network round trip per term, which
    is why remote prefixes are opt-in rather than default scope.
    """
    return adapter.startswith(("sqlite:", "simpleobo:", "obo:"))


def marker_hit(aliases: Iterable[object], markers: Iterable[str]) -> tuple[str, str]:
    """Return ``(marker, synonym)`` for the first alias carrying a marker, else ``("", "")``."""
    for alias in aliases or ():
        normalized = _normalize_marker(alias)
        for marker in markers:
            if marker in normalized:
                return marker, str(alias)
    return "", ""


class _AdapterCache:
    """Build each adapter once, remembering failures as a reason string."""

    def __init__(self, adapters: dict[str, str]) -> None:
        self._adapters = adapters
        self._built: dict[str, object] = {}
        self.failures: dict[str, str] = {}

    def get(self, prefix: str):
        if prefix in self._built or prefix in self.failures:
            return self._built.get(prefix)
        adapter_string = self._adapters[prefix]
        try:
            from oaklib import get_adapter

            self._built[prefix] = get_adapter(adapter_string)
        except Exception as exc:
            self.failures[prefix] = f"{adapter_string} unavailable: {exc}"
            return None
        return self._built[prefix]


def _prefix_of(curie: str) -> str:
    match = _CURIE_RE.match(curie)
    return match.group(1) if match else ""


def audit(
    paths: Iterable[Path],
    *,
    oak_config: Path,
    cache_dir: Path | None,
    prefixes: Iterable[str] | None = None,
    markers: Iterable[str] = DEFAULT_MARKERS,
    include_remote: bool = False,
    list_flagged: bool = False,
) -> Report:
    """Check every in-scope bound CURIE for a "do not annotate" marker synonym."""
    adapters = load_adapter_map(oak_config)
    if prefixes:
        requested = list(prefixes)
        unknown = [p for p in requested if p not in adapters]
        in_scope = [p for p in requested if p in adapters]
    else:
        unknown = []
        in_scope = [p for p in adapters if include_remote or is_local(adapters[p])]

    report = Report()
    for prefix in unknown:
        report.skipped_prefixes[prefix] = "no adapter in the OAK config"
    if not prefixes:
        for prefix, adapter in adapters.items():
            if prefix not in in_scope:
                report.skipped_prefixes[prefix] = (
                    f"{adapter} is remote (--include-remote to check)"
                )

    usages = collect_usages(paths, in_scope)
    cached = collect_cached(cache_dir, in_scope) if cache_dir else {}

    by_curie: dict[str, list[Usage]] = {}
    for usage in usages:
        by_curie.setdefault(usage.curie, []).append(usage)

    cache = _AdapterCache(adapters)
    # The repo writes gene CURIEs as lowercase ``hgnc:746`` while the ontology
    # holds ``HGNC:746``, so a lookup under the prefix casing as written finds no
    # aliases and would report a clean term. Try the other configured casings of
    # the same prefix. Only the *prefix* varies -- case-folding the local id
    # would be asking about a different term.
    by_folded: dict[str, list[str]] = {}
    for configured in adapters:
        by_folded.setdefault(configured.casefold(), []).append(configured)

    def lookup(curie: str) -> tuple[bool, tuple[str, str, str] | None]:
        """Return ``(had_synonyms, flag)``, where flag is ``(label, marker, synonym)``.

        ``had_synonyms`` is what separates "checked and clean" from "the adapter
        told us nothing": a marker *is* a synonym, so a term the adapter returns
        no synonyms for has not really been checked.
        """
        prefix = _prefix_of(curie)
        adapter = cache.get(prefix)
        if adapter is None:
            return False, None
        local = curie.split(":", 1)[1]
        variants = [
            prefix,
            *by_folded.get(prefix.casefold(), ()),
            prefix.upper(),
            prefix.lower(),
        ]
        for candidate in dict.fromkeys(f"{variant}:{local}" for variant in variants):
            try:
                aliases = adapter.entity_aliases(candidate)
            except Exception:  # pragma: no cover - adapter-specific lookup errors
                continue
            if not aliases:
                continue
            marker, synonym = marker_hit(aliases, markers)
            if marker:
                label = ""
                try:
                    label = adapter.label(candidate) or ""
                except Exception:  # pragma: no cover
                    label = ""
                return True, (label, marker, synonym)
            return True, None
        return False, None

    for curie in sorted(by_curie):
        prefix = _prefix_of(curie)
        report.checked_prefixes[prefix] = report.checked_prefixes.get(prefix, 0) + 1
        report.synonym_hits.setdefault(prefix, 0)
        had_synonyms, hit = lookup(curie)
        if had_synonyms:
            report.synonym_hits[prefix] += 1
        if hit:
            label, marker, synonym = hit
            report.in_use.append(
                Flagged(
                    curie=curie,
                    label=label,
                    marker=marker,
                    synonym=synonym,
                    usages=sorted(by_curie[curie], key=lambda u: (u.path, u.location)),
                    cached_in=cached.get(curie, []),
                )
            )

    for curie in sorted(cached):
        if curie in by_curie:
            continue
        _, hit = lookup(curie)
        if hit:
            label, marker, synonym = hit
            report.cached_only.append(
                Flagged(
                    curie=curie,
                    label=label,
                    marker=marker,
                    synonym=synonym,
                    cached_in=cached[curie],
                )
            )

    if list_flagged:
        report.inventory = _inventory(in_scope, cache, markers)

    for prefix, reason in cache.failures.items():
        report.skipped_prefixes[prefix] = reason
        report.unavailable_prefixes[prefix] = reason
        report.checked_prefixes.pop(prefix, None)
        report.synonym_hits.pop(prefix, None)

    return report


def _inventory(prefixes: Iterable[str], cache: _AdapterCache, markers) -> list[Flagged]:
    """Every flagged term in the in-scope ontologies, used or not.

    A full pass over each ontology, so it is the expensive path — reserved for
    ``--list-flagged``, where knowing the whole deny-list is the point.
    """
    found: list[Flagged] = []
    for prefix in prefixes:
        adapter = cache.get(prefix)
        if adapter is None:
            continue
        try:
            entities = list(adapter.entities())
        except Exception:  # pragma: no cover - adapter-specific iteration errors
            continue
        for entity in entities:
            curie = str(entity)
            if not curie.startswith(f"{prefix}:"):
                continue
            try:
                aliases = adapter.entity_aliases(curie)
            except Exception:  # pragma: no cover
                continue
            marker, synonym = marker_hit(aliases, markers)
            if marker:
                label = ""
                try:
                    label = adapter.label(curie) or ""
                except Exception:  # pragma: no cover
                    label = ""
                found.append(
                    Flagged(curie=curie, label=label, marker=marker, synonym=synonym)
                )
    return sorted(found, key=lambda f: f.curie)


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


def resolve_targets(raw: Iterable[str]) -> list[Path]:
    """Expand CLI arguments (files, directories, or globs) into YAML files.

    Overlapping arguments yield each file once. Deduplication is on the resolved
    path rather than the ``Path`` object, because an explicit relative argument
    and a glob expanded against the repo root name the same file with different
    objects -- so a plain ``set()`` would not collapse them, and the file would
    be scanned twice and reported twice.
    """
    targets: list[Path] = []
    seen: set[Path] = set()

    def add(candidates: Iterable[Path]) -> None:
        for candidate in candidates:
            if candidate.name.endswith(".history.yaml"):
                continue
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            targets.append(candidate)

    for item in raw:
        path = Path(item)
        if path.is_dir():
            add(sorted(path.rglob("*.yaml")))
        elif path.exists():
            add([path])
        else:
            # ``Path.glob`` rejects an absolute pattern outright, so split the
            # anchor off and glob relative to it; a relative pattern is resolved
            # against the repo root so `just check-not4curation 'kb/*/*.yaml'`
            # works from anywhere.
            if path.is_absolute():
                base = Path(path.anchor)
                pattern = path.relative_to(path.anchor).as_posix()
            else:
                base, pattern = _REPO_ROOT, item
            add(sorted(base.glob(pattern)))
    return targets


def _print_text(report: Report, stream) -> None:
    checked = ", ".join(
        f"{p} ({report.synonym_hits.get(p, 0)}/{n} with synonyms)"
        for p, n in sorted(report.checked_prefixes.items())
    )
    print(
        f"Checked {report.curies_checked} bound CURIE(s) across "
        f"{len(report.checked_prefixes)} prefix(es): {checked or 'none'}",
        file=stream,
    )
    silent = sorted(
        p
        for p, n in report.checked_prefixes.items()
        if n and not report.synonym_hits.get(p)
    )
    if silent:
        print(
            "WARNING: the adapter returned no synonyms at all for "
            f"{', '.join(silent)} — a marker is a synonym, so those prefixes were "
            "looked up but not effectively checked.",
            file=stream,
        )
    if report.skipped_prefixes:
        print("Not checked:", file=stream)
        for prefix, reason in sorted(report.skipped_prefixes.items()):
            print(f"  {prefix}: {reason}", file=stream)

    if report.inventory:
        print(
            f"\nFlagged terms in the in-scope ontologies ({len(report.inventory)}):",
            file=stream,
        )
        for item in report.inventory:
            print(f"  {item.curie}\t{item.label}\t[{item.synonym}]", file=stream)

    if report.cached_only:
        print(
            f"\nNOTE: {len(report.cached_only)} flagged CURIE(s) sit in the caches but are "
            "not used in the KB.\nThis is not a problem to fix — do NOT hand-delete rows "
            "from a validator-written cache.\nIt is recorded because such a row makes the "
            "term validate offline if a curator reaches\nfor it, which is why this audit "
            "exists (#8472):",
            file=stream,
        )
        for item in report.cached_only:
            where = ", ".join(item.cached_in)
            print(f"  {item.curie}\t{item.label}\t{where}", file=stream)

    if not report.in_use:
        print(
            "\nOK: no bound term carries a 'do not annotate' marker synonym.",
            file=stream,
        )
        return

    print(
        f"\nFAIL: {len(report.in_use)} bound term(s) are flagged by their own ontology "
        "as not for curation:",
        file=stream,
    )
    for item in report.in_use:
        print(f"\n  {item.curie}  {item.label}", file=stream)
        print(f"    marker synonym: {item.synonym}", file=stream)
        for usage in item.usages:
            print(f"    used at: {usage.format()}", file=stream)
        if item.cached_in:
            print(f"    cached in: {', '.join(item.cached_in)}", file=stream)
    print(
        "\nReplace each with a term intended for annotation — the three found in #8472 "
        "all had\nECTO equivalents (e.g. XCO:0000294 estrogen/estrogen analog -> "
        "ECTO:9000010 exposure to\nestrogens). See the dismech-terms skill for lookup "
        "guidance.",
        file=stream,
    )


def _print_tsv(report: Report, stream) -> None:
    print("state\tcurie\tlabel\tmarker_synonym\tlocation", file=stream)
    for item in report.in_use:
        for usage in item.usages:
            print(
                f"IN_USE\t{item.curie}\t{item.label}\t{item.synonym}\t{usage.format()}",
                file=stream,
            )
    for item in report.cached_only:
        print(
            f"CACHED_ONLY\t{item.curie}\t{item.label}\t{item.synonym}\t"
            f"{', '.join(item.cached_in)}",
            file=stream,
        )
    for item in report.inventory:
        print(f"FLAGGED\t{item.curie}\t{item.label}\t{item.synonym}\t", file=stream)


def _as_dict(item: Flagged) -> dict:
    return {
        "curie": item.curie,
        "label": item.label,
        "marker": item.marker,
        "synonym": item.synonym,
        "usages": [{"path": u.path, "location": u.location} for u in item.usages],
        "cached_in": item.cached_in,
    }


def _print_json(report: Report, stream) -> None:
    json.dump(
        {
            "checked_prefixes": report.checked_prefixes,
            "synonym_hits": report.synonym_hits,
            "unavailable_prefixes": report.unavailable_prefixes,
            "skipped_prefixes": report.skipped_prefixes,
            "in_use": [_as_dict(i) for i in report.in_use],
            "cached_only": [_as_dict(i) for i in report.cached_only],
            "flagged_inventory": [_as_dict(i) for i in report.inventory],
        },
        stream,
        indent=2,
        sort_keys=True,
    )
    print(file=stream)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths",
        nargs="*",
        help="files, directories or globs to scan (default: kb/ plus the schema)",
    )
    parser.add_argument(
        "--oak-config",
        type=Path,
        default=_REPO_ROOT / "conf" / "oak_config.yaml",
        help="OAK adapter config (default: conf/oak_config.yaml)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=_REPO_ROOT / "cache",
        help="term/enum cache root scanned for the advisory cached-only note",
    )
    parser.add_argument(
        "--no-cache-scan",
        action="store_true",
        help="skip the advisory scan of cache/ for flagged-but-unused CURIEs",
    )
    parser.add_argument(
        "--prefix",
        action="append",
        default=[],
        help="check exactly these ontology prefixes (repeatable). An explicit "
        "prefix is taken at face value, so it bypasses the local/remote scope "
        "rule -- naming an OLS-served prefix costs one network round trip per "
        "bound term",
    )
    parser.add_argument(
        "--marker",
        action="append",
        default=[],
        help="additional marker substring, matched case- and separator-insensitively",
    )
    parser.add_argument(
        "--include-remote",
        action="store_true",
        help="also check OLS-served prefixes (one network round trip per term)",
    )
    parser.add_argument(
        "--list-flagged",
        action="store_true",
        help="also list every flagged term in the in-scope ontologies (full pass)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "tsv", "json"),
        default="text",
        help="output format",
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="report flagged bindings without failing (exit 0)",
    )
    parser.add_argument(
        "--require-adapters",
        action="store_true",
        help="exit 2 if an in-scope adapter could not be built (offline runs)",
    )
    args = parser.parse_args(argv)

    raw = args.paths or list(DEFAULT_TARGETS)
    targets = resolve_targets(raw)
    if not targets:
        print(f"error: no YAML files matched {raw}", file=sys.stderr)
        return 2

    report = audit(
        targets,
        oak_config=args.oak_config,
        cache_dir=None if args.no_cache_scan else args.cache_dir,
        prefixes=args.prefix or None,
        markers=tuple(DEFAULT_MARKERS)
        + tuple(_normalize_marker(m) for m in args.marker),
        include_remote=args.include_remote,
        list_flagged=args.list_flagged,
    )

    stream = sys.stdout if not report.in_use else sys.stderr
    if args.format == "json":
        _print_json(report, sys.stdout)
    elif args.format == "tsv":
        _print_tsv(report, sys.stdout)
    else:
        _print_text(report, stream)

    unavailable = report.unavailable_prefixes
    if unavailable and args.require_adapters:
        print(
            "STRICT: could not build "
            f"{len(unavailable)} in-scope adapter(s); the audit could not verify "
            "those prefixes.",
            file=sys.stderr,
        )
        return 2
    if report.in_use and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
