#!/usr/bin/env python3
"""Audit ECTO/XCO ``exposure_term`` coverage on ``environmental:`` entries.

An ``environmental[]`` entry reaches the pathograph only via
``influences_mechanisms`` (see the "Linking Environmental Factors into the
Pathograph" section of ``CLAUDE.md``). Once it does, it renders as an input node
on the disorder page — so an entry that is *pathograph-linked but ontologically
unbound* shows up as free text in a graph where everything around it is grounded.
Those are the highest-value bindings, and this audit exists to find them.

Issue #8430 asked for exactly this census, and asked for it **before** any
curation pass: the issue's own worked example (``Aortitis`` / tobacco smoking)
turned out to be bound already, so an assumed gap was reported where none
existed. Counting what is already bound is therefore the first task, not the
last.

Four states per entry, from the presence of ``exposure_term`` and of a resolved
``exposure_term.term.id`` inside it:

* ``BOUND``   — ``exposure_term.term.id`` is present. Done.
* ``PARTIAL`` — an ``exposure_term`` block exists but carries only a free-text
  ``preferred_term``, with no ``term:``. Distinct from ``UNBOUND``: somebody
  reached for a binding and stopped, so the entry looks grounded in the YAML
  without being grounded in an ontology.
* ``UNBOUND`` — no ``exposure_term`` at all.

crossed with whether the entry is pathograph-linked (``influences_mechanisms``).

**Reuse candidates.** A large share of the gap is the same exposure concept
recurring across disorders — ultraviolet radiation, tobacco smoking, fasting.
When one instance is bound and another is not, the unbound one needs no ontology
research at all: the CURIE is already in the KB (and therefore already in
``cache/ecto/terms.csv`` and the ``exposureterm`` enum cache, so it validates
without a network round-trip). This audit matches unbound entries against bound
ones on a normalized name and reports the CURIE already in use.

That match is **advisory**. It is a string match on curator-written names, not a
semantic one, and the guardrail from ``.claude/skills/dismech-terms`` still
applies: *no term beats a bad one*. A suggestion is a starting point for a
curator, never an auto-fix — some exposures (microgravity, emotional stress)
correctly stay unbound because ECTO has nothing specific enough, and this audit
cannot tell that case apart from an un-researched one.

Usage::

    uv run python scripts/environmental_exposure_term_audit.py
    uv run python scripts/environmental_exposure_term_audit.py --format tsv --out out.tsv
    uv run python scripts/environmental_exposure_term_audit.py --linked-only --format list
    uv run python scripts/environmental_exposure_term_audit.py --strict
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path

#: KB subtrees that may carry ``environmental:`` entries, relative to the repo root.
_KB_GLOBS = (
    "kb/disorders/*.yaml",
    "kb/modules/*.yaml",
    "kb/comorbidities/*.yaml",
)

#: Words dropped when normalizing an exposure name for reuse matching. These are
#: framing words that curators add or omit freely for the same concept
#: ("Smoking" / "Cigarette smoking" / "Tobacco Smoking Exposure"), not words that
#: distinguish one exposure from another.
_NOISE_WORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "as",
        "context",
        "exposure",
        "exposures",
        "factor",
        "factors",
        "of",
        "or",
        "the",
        "to",
    }
)

_STATE_BOUND = "BOUND"
_STATE_PARTIAL = "PARTIAL"
_STATE_UNBOUND = "UNBOUND"


@dataclass
class _Exposure:
    """One ``environmental[]`` entry, with just the fields this audit reads."""

    path: str
    entry: str
    name: str
    linked: bool
    state: str
    curie: str = ""
    label: str = ""

    @property
    def slug(self) -> str:
        return Path(self.path).stem

    @property
    def priority(self) -> bool:
        """Pathograph-linked and not fully bound — the tranche worth curating."""
        return self.linked and self.state != _STATE_BOUND


def _normalize(name: str) -> str:
    """Collapse an exposure name to a key for reuse matching.

    Lowercases, drops punctuation and the framing words in :data:`_NOISE_WORDS`,
    then sorts the remaining tokens so word order does not matter ("Smoking,
    Tobacco" matches "Tobacco Smoking"). Deliberately conservative: it will miss
    synonyms it has no way to know about, which yields a missing suggestion
    rather than a wrong one.
    """
    tokens = re.split(r"[^a-z0-9]+", name.lower())
    kept = sorted(t for t in tokens if t and t not in _NOISE_WORDS)
    return " ".join(kept)


def _classify(env: dict) -> tuple[str, str, str]:
    """Return ``(state, curie, label)`` for one ``environmental[]`` entry."""
    exposure_term = env.get("exposure_term")
    if not isinstance(exposure_term, dict):
        return _STATE_UNBOUND, "", ""
    term = exposure_term.get("term")
    if not isinstance(term, dict) or not term.get("id"):
        return _STATE_PARTIAL, "", ""
    return _STATE_BOUND, str(term["id"]), str(term.get("label") or "")


def collect(repo_root: Path | None = None) -> list[_Exposure]:
    """Walk the KB and return every ``environmental[]`` entry, classified."""
    # Resolved at call time, not bound as a default, so tests can point the walk
    # at a fixture tree by patching the module-level root.
    repo_root = repo_root if repo_root is not None else _REPO_ROOT
    out: list[_Exposure] = []
    for pattern in _KB_GLOBS:
        for path in sorted(repo_root.glob(pattern)):
            try:
                doc = safe_load_path(path)
            except Exception as exc:  # report and keep auditing the rest
                print(f"WARNING: could not parse {path}: {exc}", file=sys.stderr)
                continue
            if not isinstance(doc, dict):
                continue
            entry_name = str(doc.get("name") or path.stem)
            for env in doc.get("environmental") or []:
                if not isinstance(env, dict):
                    continue
                state, curie, label = _classify(env)
                out.append(
                    _Exposure(
                        path=str(path.relative_to(repo_root)),
                        entry=entry_name,
                        name=str(env.get("name") or "(unnamed)"),
                        linked=bool(env.get("influences_mechanisms")),
                        state=state,
                        curie=curie,
                        label=label,
                    )
                )
    return out


def build_reuse_index(exposures: list[_Exposure]) -> dict[str, tuple[str, str, int]]:
    """Map a normalized name to the ``(curie, label, n)`` most used for it.

    Only bound entries contribute. When curators have bound the same concept to
    more than one CURIE, the most frequent wins and the disagreement is reported
    separately by :func:`find_conflicts` rather than silently resolved here.
    """
    votes: dict[str, Counter] = defaultdict(Counter)
    labels: dict[str, str] = {}
    for exp in exposures:
        if exp.state != _STATE_BOUND:
            continue
        key = _normalize(exp.name)
        if not key:
            continue
        votes[key][exp.curie] += 1
        labels.setdefault(exp.curie, exp.label)
    index: dict[str, tuple[str, str, int]] = {}
    for key, counter in votes.items():
        curie, count = counter.most_common(1)[0]
        index[key] = (curie, labels.get(curie, ""), count)
    return index


def find_conflicts(exposures: list[_Exposure]) -> dict[str, Counter]:
    """Normalized names bound to more than one CURIE across the KB.

    Not necessarily an error — the same words can name genuinely different
    exposures in different diseases — but each one is worth a curator's eye,
    since it is also the shape of an inconsistent binding.
    """
    votes: dict[str, Counter] = defaultdict(Counter)
    for exp in exposures:
        if exp.state == _STATE_BOUND and _normalize(exp.name):
            votes[_normalize(exp.name)][exp.curie] += 1
    return {k: v for k, v in votes.items() if len(v) > 1}


def _pct(part: int, whole: int) -> str:
    return f"{(100.0 * part / whole):.1f}%" if whole else "n/a"


def _print_summary(exposures: list[_Exposure], reuse: dict, top: int) -> None:
    total = len(exposures)
    linked = [e for e in exposures if e.linked]
    counts = Counter((e.linked, e.state) for e in exposures)

    subtrees = ", ".join(g.split("/")[1] for g in _KB_GLOBS)
    print(f"Environmental entries in kb/{{{subtrees}}}: {total}")
    print()
    print(f"{'pathograph-linked':>18} | {'state':<8} | {'count':>6}")
    print(f"{'-' * 18}-+-{'-' * 8}-+-{'-' * 6}")
    for is_linked in (True, False):
        for state in (_STATE_BOUND, _STATE_PARTIAL, _STATE_UNBOUND):
            print(
                f"{is_linked!s:>18} | {state:<8} | "
                f"{counts.get((is_linked, state), 0):>6}"
            )
    print()

    bound_linked = counts.get((True, _STATE_BOUND), 0)
    print(
        f"Pathograph-linked: {len(linked)} entries, {bound_linked} bound "
        f"({_pct(bound_linked, len(linked))}) — these render in the mechanism graph."
    )
    bound_all = sum(1 for e in exposures if e.state == _STATE_BOUND)
    print(
        f"All entries:       {total} entries, {bound_all} bound ({_pct(bound_all, total)})."
    )
    print()

    priority = [e for e in exposures if e.priority]
    with_suggestion = [e for e in priority if _normalize(e.name) in reuse]
    print(f"PRIORITY GAP (linked, not bound): {len(priority)}")
    print(
        f"  of which a CURIE is already in use elsewhere for the same "
        f"normalized name: {len(with_suggestion)} "
        f"({_pct(len(with_suggestion), len(priority))}) — no ontology research needed."
    )
    print(
        f"  needing a fresh ECTO lookup (or a documented "
        f"'no suitable term'): {len(priority) - len(with_suggestion)}"
    )
    print(
        "  NOTE: the reuse count is a FLOOR. Matching is exact-on-normalized-name,\n"
        "        so 'Ultraviolet exposure' (bound) does not match 'Ultraviolet\n"
        "        Radiation' (unbound). Read the concept table below for near-misses."
    )
    print()

    # Counted over ALL entries, not just unbound ones, so that a concept split
    # across phrasings shows its bound and unbound halves on adjacent rows —
    # which is how the exact-match floor above gets spotted by a human.
    per_key: dict[str, list[_Exposure]] = defaultdict(list)
    for exp in exposures:
        if _normalize(exp.name):
            per_key[_normalize(exp.name)].append(exp)
    ranked = sorted(
        per_key.items(),
        key=lambda kv: (-sum(1 for e in kv[1] if e.priority), -len(kv[1]), kv[0]),
    )
    print(f"Top {top} recurring exposure concepts, by size of their priority gap:")
    print(f"  {'gap':>4} {'bound':>5}  {'CURIE in use':<28}  concept")
    for key, entries in ranked[:top]:
        gap = sum(1 for e in entries if e.priority)
        if not gap:
            continue
        n_bound = sum(1 for e in entries if e.state == _STATE_BOUND)
        hit = reuse.get(key)
        in_use = f"{hit[0]} {hit[1]}"[:28] if hit else "-"
        print(f"  {gap:>4} {n_bound:>5}  {in_use:<28}  {key}")

    conflicts = find_conflicts(exposures)
    if conflicts:
        print()
        print(f"Normalized names bound to >1 CURIE ({len(conflicts)}) — review:")
        for key, counter in sorted(conflicts.items()):
            detail = ", ".join(f"{c} x{n}" for c, n in counter.most_common())
            print(f"  {key}: {detail}")


def _print_list(exposures: list[_Exposure], reuse: dict) -> None:
    for i, exp in enumerate(sorted(exposures, key=lambda e: (e.slug, e.name)), start=1):
        hit = reuse.get(_normalize(exp.name))
        suffix = f"  -> reuse {hit[0]} ({hit[1]})" if hit else ""
        print(f"{i:4d}. [{exp.state:<7}] {exp.slug:<55} | {exp.name}{suffix}")


def _write_tsv(exposures: list[_Exposure], reuse: dict, out) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "path",
            "entry",
            "exposure_name",
            "pathograph_linked",
            "state",
            "curie",
            "label",
            "normalized_name",
            "reuse_curie",
            "reuse_label",
        ]
    )
    for exp in sorted(exposures, key=lambda e: (e.path, e.name)):
        key = _normalize(exp.name)
        hit = reuse.get(key) if exp.state != _STATE_BOUND else None
        writer.writerow(
            [
                exp.path,
                exp.entry,
                exp.name,
                "yes" if exp.linked else "no",
                exp.state,
                exp.curie,
                exp.label,
                key,
                hit[0] if hit else "",
                hit[1] if hit else "",
            ]
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv"),
        default="summary",
        help="summary counts (default), a per-entry list, or a TSV table",
    )
    parser.add_argument(
        "--linked-only",
        action="store_true",
        help="restrict to pathograph-linked entries (those with influences_mechanisms). "
        "Applies to --format list/tsv; the summary is always the full census.",
    )
    parser.add_argument(
        "--unbound-only",
        action="store_true",
        help="restrict to entries that are not fully BOUND. Applies to "
        "--format list/tsv; the summary is always the full census.",
    )
    parser.add_argument(
        "--top", type=int, default=25, help="rows in the recurring-concept table"
    )
    parser.add_argument("--out", type=Path, help="write to this file instead of stdout")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any pathograph-linked entry is unbound (advisory by default)",
    )
    args = parser.parse_args(argv)

    all_exposures = collect()
    # The reuse index is always built over the WHOLE corpus: a filtered view must
    # still be able to suggest a CURIE bound on an entry the filter excluded.
    reuse = build_reuse_index(all_exposures)

    selected = all_exposures
    if args.linked_only:
        selected = [e for e in selected if e.linked]
    if args.unbound_only:
        selected = [e for e in selected if e.state != _STATE_BOUND]

    stream = args.out.open("w", encoding="utf-8") if args.out else sys.stdout
    try:
        if args.format == "tsv":
            _write_tsv(selected, reuse, stream)
        else:
            original = sys.stdout
            sys.stdout = stream
            try:
                if args.format == "list":
                    _print_list(selected, reuse)
                else:
                    # Always the full corpus: a "census" narrowed by a filter
                    # would report a coverage percentage of its own selection.
                    _print_summary(all_exposures, reuse, args.top)
            finally:
                sys.stdout = original
    finally:
        if args.out:
            stream.close()
            print(f"Wrote {args.out}", file=sys.stderr)

    if args.strict and any(e.priority for e in all_exposures):
        n = sum(1 for e in all_exposures if e.priority)
        print(
            f"STRICT: {n} pathograph-linked environmental entries are not bound "
            "to an ECTO/XCO term.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
