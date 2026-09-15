#!/usr/bin/env python3
"""Guard the two homes a treatment's carrier facts can live in.

Why there are two homes
-----------------------
``delivery_platform`` and the targeting ligand used to exist only inside
``oligonucleotide_details``, so only an ASO or an siRNA could say what carried
it. That excluded every other nanomedicine in the KB: ``nab-sirolimus`` and
liposomal irinotecan were curated with the carrier visible nowhere but a
free-text ``preferred_term``, and ``MRNA_THERAPY`` -- a modality defined by its
carrier -- had no way to name one.

The fix was a Treatment-level ``delivery_system`` block. The nested copy was
kept valid rather than removed, because removing it would have invalidated ~44
in-flight oligonucleotide entries the way retiring ``supports: PARTIAL`` did in
#10061. So for a while both spellings are legal, and this check is what stops
them drifting apart.

What it gates on, and why each is a real defect
-----------------------------------------------
``CONFLICT``
    The same fact recorded in both places with *different* values. One of them
    is wrong and no reader -- renderer, exporter, or human -- can tell which.
    The renderer resolves ``delivery_system`` first, so a conflict silently
    hides the nested value rather than surfacing a disagreement.
``EMPTY``
    A ``delivery_system`` block carrying no carrier fact at all. It renders as
    nothing and asserts nothing; the absence of the block says the same thing
    more honestly.
``LIGANDLESS_TARGET``
    A ``targeting_receptor`` alongside ``targeting_ligand: UNCONJUGATED``. Those
    are contradictory claims: a receptor is named as the route of uptake while
    the carrier is said to have nothing on it that binds a receptor. Passive
    accumulation is a real and common delivery strategy -- a PEGylated liposome
    has no ligand -- but it is expressed by leaving the targeting slots absent,
    not by naming a receptor and then denying the means to reach it.

What it reports without gating
------------------------------
``DUPLICATE``
    The same fact in both places with the same value. Harmless today and
    one edit from becoming a ``CONFLICT``, so it is worth clearing, but nothing
    downstream reads it wrong.
``LEGACY``
    The carrier recorded only in the nested oligonucleotide block. This is the
    migration worklist, and it is the state of most of the KB's oligonucleotide
    formulations by design -- gating on it would turn every one of those entries
    red for a change none of their curators made.

Usage
-----
    python scripts/check_delivery_system.py                      # gate
    python scripts/check_delivery_system.py kb/disorders/Asthma.yaml
    python scripts/check_delivery_system.py --format list        # full census
    python scripts/check_delivery_system.py --strict             # also gate DUPLICATE
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.yaml_io import safe_load

#: Trees whose documents carry `treatments:` blocks validated against dismech.yaml.
PATTERNS = (
    "kb/disorders/**/*.yaml",
    "kb/modules/**/*.yaml",
    "kb/comorbidities/**/*.yaml",
)

#: The carrier facts that have two homes, as (delivery_system slot, nested slots).
#: `conjugation` is the deprecated spelling of `targeting_ligand` and is read as
#: an additional nested source for the same fact.
SHARED_FACTS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("delivery_platform", ("delivery_platform",)),
    ("targeting_ligand", ("targeting_ligand", "conjugation")),
)

GATING = ("CONFLICT", "EMPTY", "LIGANDLESS_TARGET")


class Finding:
    __slots__ = ("path", "location", "kind", "detail")

    def __init__(self, path: Path, location: str, kind: str, detail: str) -> None:
        self.path = path
        self.location = location
        self.kind = kind
        self.detail = detail


def _treatment_like(node: dict) -> bool:
    """Does this mapping carry any of the slots this check cares about?"""
    return any(
        key in node
        for key in ("delivery_system", "oligonucleotide_details", "aso_details")
    )


def _walk(node: object, path: str = "") -> "list[tuple[str, dict]]":
    """Every mapping in the document that looks like a Treatment, with its path.

    Generic recursion rather than a `treatments:` lookup on purpose: a Treatment
    can sit at the disease level, inside a module, or nested under a subtype, and
    a check that missed one of those would be worse than useless.
    """
    found: list[tuple[str, dict]] = []
    if isinstance(node, dict):
        if _treatment_like(node):
            name = node.get("name") or "<unnamed>"
            found.append((f"{path} ({name})" if path else str(name), node))
        for key, value in node.items():
            found.extend(_walk(value, f"{path}.{key}" if path else key))
    elif isinstance(node, list):
        for index, item in enumerate(node):
            found.extend(_walk(item, f"{path}[{index}]"))
    return found


def check_treatment(path: Path, location: str, tx: dict) -> list[Finding]:
    findings: list[Finding] = []
    ds = tx.get("delivery_system")
    ds = ds if isinstance(ds, dict) else None
    nested = tx.get("oligonucleotide_details") or tx.get("aso_details")
    nested = nested if isinstance(nested, dict) else None

    if ds is not None:
        carried = [
            slot
            for slot in ("delivery_platform", "targeting_ligand", "targeting_receptor", "target_cell_types")
            if ds.get(slot)
        ]
        if not carried:
            findings.append(
                Finding(path, location, "EMPTY", "delivery_system carries no carrier fact")
            )
        if ds.get("targeting_receptor") and ds.get("targeting_ligand") == "UNCONJUGATED":
            findings.append(
                Finding(
                    path,
                    location,
                    "LIGANDLESS_TARGET",
                    "targeting_receptor named while targeting_ligand is UNCONJUGATED",
                )
            )

    for ds_slot, nested_slots in SHARED_FACTS:
        ds_value = ds.get(ds_slot) if ds else None
        nested_value = next(
            (nested[s] for s in nested_slots if nested and nested.get(s)), None
        )
        nested_slot = next(
            (s for s in nested_slots if nested and nested.get(s)), nested_slots[0]
        )
        if ds_value and nested_value:
            if ds_value != nested_value:
                findings.append(
                    Finding(
                        path,
                        location,
                        "CONFLICT",
                        f"delivery_system.{ds_slot}={ds_value!r} vs "
                        f"oligonucleotide_details.{nested_slot}={nested_value!r}",
                    )
                )
            else:
                findings.append(
                    Finding(
                        path,
                        location,
                        "DUPLICATE",
                        f"{ds_slot}={ds_value!r} recorded in both places",
                    )
                )
        elif nested_value and not ds_value:
            findings.append(
                Finding(
                    path,
                    location,
                    "LEGACY",
                    f"oligonucleotide_details.{nested_slot}={nested_value!r}; "
                    f"prefer delivery_system.{ds_slot}",
                )
            )
    return findings


def _files(explicit: set[Path]) -> list[Path]:
    seen: dict[Path, None] = {}
    for pattern in PATTERNS:
        for candidate in sorted(ROOT.glob(pattern)):
            seen.setdefault(candidate, None)
    files = list(seen)
    if explicit:
        files = [f for f in files if f.resolve() in explicit]
    return files


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def scan_repo(paths: "list[Path] | None" = None) -> list[Finding]:
    explicit = {p.resolve() for p in paths} if paths else set()
    findings: list[Finding] = []
    for path in _files(explicit):
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:  # malformed YAML is check-duplicate-keys' job
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            continue
        for location, tx in _walk(data):
            findings.extend(check_treatment(path, location, tx))
    return findings


def main() -> int:
    # One walk, no second pass, so the parsed-KB cache is pure cost here.
    kb_cache.default_off()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="YAML files to check (default: all)")
    parser.add_argument(
        "--format",
        choices=("summary", "list"),
        default="summary",
        help="summary prints gating findings plus counts; list prints every finding",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="also fail on DUPLICATE (same fact in both homes)",
    )
    args = parser.parse_args()

    findings = scan_repo([Path(p) for p in args.paths] or None)
    counts = Counter(f.kind for f in findings)
    gating = set(GATING) | ({"DUPLICATE"} if args.strict else set())
    failures = [f for f in findings if f.kind in gating]

    shown = findings if args.format == "list" else failures
    for finding in sorted(shown, key=lambda f: (f.kind, str(f.path), f.location)):
        print(f"{finding.kind}: {_display(finding.path)}: {finding.location}: {finding.detail}")

    if args.format == "list" and not findings:
        print("No treatment in kb/ records a delivery platform or targeting ligand.")

    summary = ", ".join(f"{kind}={counts[kind]}" for kind in sorted(counts)) or "none"
    print(f"\ndelivery_system findings: {summary}")

    if failures:
        print(f"\n{len(failures)} gating finding(s). See the module docstring for why each is a defect.")
        return 1
    print("OK: no conflicting, empty, or ligandless delivery_system records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
