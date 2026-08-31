#!/usr/bin/env python3
"""Guard ontology terms nested inside ``qualifiers`` (issue #10197).

``Qualifier.predicate`` and ``Qualifier.value`` are both plain ``Descriptor``s,
so each carries a full ``term:`` block — a real CURIE-and-label ontology
binding, in the same shape the rest of the KB uses::

    qualifiers:
    - predicate:
        preferred_term: therapeutic agent
        term: {id: NCIT:C2259, label: Therapeutic Agent}
      value:
        preferred_term: vancomycin
        term: {id: NCIT:C925, label: Vancomycin}

**`linkml-term-validator` does not check them.** It validates slots whose range
is bound to an ontology-backed dynamic enum; the generic ``Descriptor`` used by
``Qualifier`` has no such binding, so everything nested under ``qualifiers`` is
invisible to it. Verified directly: replacing a qualifier term's label with
"Totally Bogus Fabricated Label" and running

    just validate-terms kb/disorders/Clostridioides_difficile_Infection.yaml

reports "✅ Validation passed".

That blind spot had already admitted a real defect. ``NCIT:C288`` was curated as
``vancomycin`` in ``Clostridioides_difficile_Infection``; NCIT's canonical label
for that code is **Azacitidine**, an antineoplastic. Vancomycin is ``NCIT:C925``.
Nothing in the stack objected, because nothing looked.

What this checks, and what it cannot
------------------------------------
Offline, against the committed ``cache/<prefix>/terms.csv`` label caches:

``wrong_label``
    The CURIE is cached and the YAML's label disagrees with the ontology's
    canonical one. This is the fabrication class, and it gates.

``unverified``
    The CURIE is in no cache, so this script has no opinion. Reported with a
    per-prefix count, never gated — the caches are populated as a side effect of
    validating a term, and a qualifier-only CURIE is never validated, so "absent"
    is the normal state here rather than evidence of a defect. The count is the
    honest size of the remaining coverage gap.

``RO`` and ``PR`` (109 of the KB's 424 qualifier terms) are not in
``conf/oak_config.yaml`` at all, so they cannot be validated by any current
tooling, offline or not. They are reported separately rather than folded into
``unverified``, because the fix is a config decision, not a cache refresh.

``--resolve`` consults the configured OAK adapters for the uncached CURIEs. It
needs network and is not part of the gate; use it when auditing, not in CI.

Usage
-----
    python scripts/check_qualifier_terms.py               # gate (offline)
    python scripts/check_qualifier_terms.py --report      # census, exit 0
    python scripts/check_qualifier_terms.py --resolve     # also check uncached
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from typing import Any, NamedTuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities", "kb/groupings")

# Prefixes with no adapter in conf/oak_config.yaml: unvalidatable by construction.
UNCONFIGURED_PREFIXES = {"RO", "PR"}


class Term(NamedTuple):
    path: str
    role: str  # "predicate" | "value"
    curie: str
    label: str


def load_label_cache() -> dict[str, str]:
    """Every committed CURIE -> canonical label, across all cache/<prefix>/."""
    cache: dict[str, str] = {}
    cache_root = ROOT / "cache"
    for terms_csv in sorted(cache_root.glob("*/terms.csv")):
        with terms_csv.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                curie = row.get("curie")
                if curie:
                    cache[curie] = row.get("label", "")
    return cache


def iter_qualifier_terms(data: Any, display: str) -> list[Term]:
    found: list[Term] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "qualifiers" and isinstance(value, list):
                    for qualifier in value:
                        if not isinstance(qualifier, dict):
                            continue
                        for role in ("predicate", "value"):
                            descriptor = qualifier.get(role)
                            if not isinstance(descriptor, dict):
                                continue
                            term = descriptor.get("term")
                            if isinstance(term, dict) and term.get("id"):
                                found.append(
                                    Term(
                                        display,
                                        role,
                                        str(term["id"]),
                                        str(term.get("label", "")),
                                    )
                                )
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


def iter_yaml_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p) for p in paths]
    files: list[Path] = []
    for root in DEFAULT_ROOTS:
        files.extend(sorted((ROOT / root).rglob("*.yaml")))
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def collect(paths: list[str]) -> list[Term]:
    terms: list[Term] = []
    for path in iter_yaml_files(paths):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        if isinstance(data, (dict, list)):
            terms.extend(iter_qualifier_terms(data, _display(path)))
    return terms


def classify(
    terms: list[Term], cache: dict[str, str]
) -> tuple[list[tuple[Term, str]], list[Term], list[Term], int]:
    """-> (wrong_label, unverified, unconfigured, ok_count)"""
    wrong: list[tuple[Term, str]] = []
    unverified: list[Term] = []
    unconfigured: list[Term] = []
    ok = 0
    for term in terms:
        prefix = term.curie.split(":", 1)[0]
        if prefix in UNCONFIGURED_PREFIXES:
            unconfigured.append(term)
        elif term.curie not in cache:
            unverified.append(term)
        elif term.label != cache[term.curie]:
            wrong.append((term, cache[term.curie]))
        else:
            ok += 1
    return wrong, unverified, unconfigured, ok


def resolve_remote(terms: list[Term]) -> list[tuple[Term, str]]:
    """Check uncached CURIEs against the configured OAK adapters. Needs network."""
    import yaml as _yaml
    from oaklib import get_adapter

    conf = _yaml.safe_load((ROOT / "conf" / "oak_config.yaml").read_text())
    adapters_conf = conf["ontology_adapters"]
    adapters: dict[str, Any] = {}
    wrong: list[tuple[Term, str]] = []
    checked = 0
    for term in terms:
        prefix = term.curie.split(":", 1)[0]
        spec = adapters_conf.get(prefix)
        if not spec:
            # No adapter configured: say so rather than silently passing. A
            # resolver that reports nothing because it looked at nothing is
            # worse than no resolver at all.
            print(f"  skipped (no adapter for {prefix}): {term.curie}", file=sys.stderr)
            continue
        if prefix not in adapters:
            adapters[prefix] = get_adapter(spec)
        # A CURIE that does not exist surfaces as an adapter exception (OLS
        # answers 404) rather than a None label, so both have to be caught --
        # a nonexistent code is the most serious finding this check can make.
        try:
            actual = adapters[prefix].label(term.curie)
        except Exception:  # any lookup failure is itself a finding
            actual = None
        checked += 1
        if actual is None:
            wrong.append((term, "<CURIE DOES NOT RESOLVE>"))
        elif actual != term.label:
            wrong.append((term, actual))
    print(f"resolved {checked} uncached CURIE(s) against OAK.", file=sys.stderr)
    return wrong


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help=f"default: {', '.join(DEFAULT_ROOTS)}")
    parser.add_argument("--report", action="store_true", help="census, exit 0")
    parser.add_argument(
        "--resolve",
        action="store_true",
        help="also check uncached CURIEs via OAK (needs network; not for CI)",
    )
    args = parser.parse_args()

    terms = collect(args.paths)
    cache = load_label_cache()
    wrong, unverified, unconfigured, ok = classify(terms, cache)

    resolved = 0
    if args.resolve:
        remote_wrong = resolve_remote(unverified)
        resolved = len(unverified)
        wrong = wrong + remote_wrong
        # Everything resolved and not flagged is now verified, just against the
        # ontology rather than the cache. Fold it into `ok` so the summary counts
        # what was actually checked instead of only the cache-backed subset.
        ok += resolved - len(remote_wrong)
        unverified = []

    if args.report:
        print(
            f"qualifier terms: {len(terms)} ({len({t.curie for t in terms})} distinct)"
        )
        print(f"  label verified against cache : {ok}")
        print(f"  label WRONG                  : {len(wrong)}")
        print(f"  not cached (no opinion)      : {len(unverified)}")
        for prefix, n in Counter(
            t.curie.split(":", 1)[0] for t in unverified
        ).most_common():
            print(f"      {prefix:10s} {n}")
        print(f"  prefix not in oak_config     : {len(unconfigured)}")
        for prefix, n in Counter(
            t.curie.split(":", 1)[0] for t in unconfigured
        ).most_common():
            print(f"      {prefix:10s} {n}")
        return 0

    if unverified:
        print(
            f"note: {len(unverified)} qualifier term(s) are in no cache, so their "
            "labels are unchecked here. Run with --resolve to check them online.\n"
        )
    if unconfigured:
        prefixes = ", ".join(sorted({t.curie.split(":", 1)[0] for t in unconfigured}))
        print(
            f"note: {len(unconfigured)} qualifier term(s) use prefixes with no adapter "
            f"in conf/oak_config.yaml ({prefixes}); no tooling can validate them.\n"
        )

    if not wrong:
        source = "the ontology" if args.resolve else "the ontology cache"
        extra = f" ({resolved} resolved online)" if resolved else ""
        print(f"OK: {ok} qualifier term label(s) match {source}{extra}.")
        return 0

    print("Wrong ontology label(s) on qualifier terms.\n")
    print(
        "`term.label` must be the ontology's canonical label for `term.id`.\n"
        "A mismatch means the CURIE and the name disagree — the binding points at\n"
        "a different concept than the text claims. `linkml-term-validator` does not\n"
        "reach inside `qualifiers`, so nothing else catches this (issue #10197).\n"
    )
    for term, actual in wrong:
        print(f"  {term.path}")
        print(f"     qualifiers.{term.role}: {term.curie}")
        print(f"     curated label : {term.label!r}")
        print(f"     ontology label: {actual!r}")
    print(f"\n{len(wrong)} finding(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
