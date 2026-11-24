#!/usr/bin/env python3
"""Check that treatment-to-node links say what their own text and evidence say.

A ``target_mechanisms`` link draws an arrow from a treatment to a pathograph
node. ``treatment_effect`` is the part of the claim a query or a graph can read;
the ``description`` and the evidence grades are not. So a link whose prose says
"does not act on this node" while its typed effect says it does is a false
arrow with an honest caveat nobody downstream sees (#10048), and a treatment
curated because it failed needs a typed way to say so (#10151).

Findings
--------
NEGATIVE_WITHOUT_EVIDENCE (gates)
    ``NO_EFFECT`` or ``EXACERBATES`` with no evidence on the link. Both are
    substantive negative claims, and neither can be inherited from the
    treatment's own evidence.
NEGATIVE_ALL_REFUTE (reported)
    A negative effect whose link evidence is REFUTE throughout. ``supports`` is
    graded against the link as typed, so a paper reporting the failure SUPPORTs a
    ``NO_EFFECT`` link.
REFUTED_EFFECT (reported)
    A therapeutic (or absent) effect whose link evidence is REFUTE throughout.
    Either the effect is negative, or the link belongs on another node.
DENIED_EFFECT (reported)
    The description negates the effect the link declares. ``BYPASSES`` and the
    negative values are exempt: "does not correct the lesion" restates them.
NON_THERAPEUTIC_TARGET (reported)
    Genetic counseling or testing with treatment-style target slots. The test
    suite gates this when ``action_category`` is filled in; this reads the bound
    NCIT term, so an untyped treatment is seen too.

The reported classes are leads and never fail. A description may negate
something other than the link, and the fix is a curator's: retype the effect,
move the link to the node the treatment does act on, or leave it.

    python scripts/check_treatment_effects.py                 # gate + counts
    python scripts/check_treatment_effects.py --format list   # every finding
    python scripts/check_treatment_effects.py --format tsv kb/disorders/X.yaml
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.graph import NEGATIVE_TREATMENT_EFFECT_PREDICATES
from dismech.kb_cache import load_document

PATTERNS = (
    "kb/disorders/**/*.yaml",
    "kb/modules/**/*.yaml",
    "kb/comorbidities/**/*.yaml",
)

NEGATIVE_EFFECTS = frozenset(NEGATIVE_TREATMENT_EFFECT_PREDICATES)

GATING = ("NEGATIVE_WITHOUT_EVIDENCE",)
KINDS = (
    *GATING,
    "NEGATIVE_ALL_REFUTE",
    "REFUTED_EFFECT",
    "DENIED_EFFECT",
    "NON_THERAPEUTIC_TARGET",
)

#: NCIT actions that inform rather than treat.
NON_THERAPEUTIC_TERMS = {
    "NCIT:C15240": "Genetic Counseling",
    "NCIT:C15709": "Genetic Testing",
}

_NEGATOR = (
    r"\b(?:does|do|did|is|are|was|were|has|have|can|could|will|would)(?:\s+not|n't)"
    r"\s+(?:\w+ly\s+|itself\s+|thereby\s+)?"
)
# A failure to work, which denies a link to any kind of node.
_FAILURE = re.compile(
    _NEGATOR + r"(?:work(?:ing)?|effective|benefit)\b"
    r"|\b(?:no|without)\s+(?:demonstrated\s+|clinical\s+|significant\s+)?"
    r"(?:effect|benefit|improvement|response|remission)\b"
    r"|\b(?:ineffective|failed\s+to|fails\s+to)\b",
    re.IGNORECASE,
)
# Not acting on something. Only a denial when the target is a mechanism: a
# hearing aid linked to the hearing loss "does not act on the hair cells", and
# the link is right.
_NO_ACTION = re.compile(
    _NEGATOR + r"(?:act(?:ing)?\s+on|target(?:ing)?|address(?:ing)?|affect(?:ing)?"
    r"|alter(?:ing)?|modif(?:y|ying)|chang(?:e|ing)|treat(?:ing)?)\b",
    re.IGNORECASE,
)
_EFFECT_VERBS = {
    "RESTORES": re.compile(
        _NEGATOR + r"(?:restor|correct|repair|replac|revers|normali[sz])\w*",
        re.IGNORECASE,
    ),
    "INHIBITS": re.compile(
        _NEGATOR + r"(?:inhibit|suppress|reduc|block|prevent|slow|halt|lower)\w*",
        re.IGNORECASE,
    ),
    "ACTIVATES": re.compile(
        _NEGATOR + r"(?:activat|increas|promot|stimulat|induc)\w*", re.IGNORECASE
    ),
}


@dataclass(frozen=True)
class Finding:
    kind: str
    path: Path
    treatment: str
    target: str
    effect: str
    detail: str


def denial(
    description: str, effect: str | None, *, mechanism_target: bool = True
) -> str | None:
    """The phrase in ``description`` that denies ``effect``, or None.

    >>> denial("It does not act on the migration defect.", "MODULATES")
    'does not act on'
    >>> denial("Substitutes for the pancreas; does not correct the lesion.", "BYPASSES")
    >>> denial("Lowers ammonia but does not restore the enzyme.", "INHIBITS")
    >>> denial("Lowers ammonia but does not restore the enzyme.", "RESTORES")
    'does not restore'
    >>> denial("It does not act on hair cells.", None, mechanism_target=False)
    >>> denial("It was ineffective.", None, mechanism_target=False)
    'ineffective'
    """
    if effect == "BYPASSES" or effect in NEGATIVE_EFFECTS:
        return None
    patterns = [_FAILURE]
    if mechanism_target:
        patterns.append(_NO_ACTION)
        if effect in _EFFECT_VERBS:
            patterns.append(_EFFECT_VERBS[effect])
    for pattern in patterns:
        match = pattern.search(" ".join(description.split()))
        if match:
            return match.group(0)
    return None


def check_treatment(
    path: Path, treatment: dict[str, Any], mechanisms: set[str]
) -> Iterator[Finding]:
    """Yield every finding for one treatment.

    ``mechanisms`` holds the entry's pathophysiology node names.
    """
    name = str(treatment.get("name") or "(unnamed)")
    links = [
        link
        for link in treatment.get("target_mechanisms") or []
        if isinstance(link, dict)
    ]
    for link in links:
        effect = link.get("treatment_effect")
        where = (path, name, str(link.get("target")), effect or "")
        evidence = [e for e in link.get("evidence") or [] if isinstance(e, dict)]
        all_refute = bool(evidence) and all(
            e.get("supports") == "REFUTE" for e in evidence
        )
        if effect in NEGATIVE_EFFECTS:
            if not evidence:
                yield Finding(
                    "NEGATIVE_WITHOUT_EVIDENCE",
                    *where,
                    f"{effect} is a negative claim and needs evidence on the link",
                )
            elif all_refute:
                yield Finding(
                    "NEGATIVE_ALL_REFUTE",
                    *where,
                    f"evidence grades REFUTE the {effect} claim itself",
                )
            continue
        if all_refute:
            yield Finding(
                "REFUTED_EFFECT", *where, "all link evidence is graded REFUTE"
            )
        phrase = denial(
            str(link.get("description") or ""),
            effect,
            mechanism_target=link.get("target") in mechanisms,
        )
        if phrase:
            yield Finding("DENIED_EFFECT", *where, f"description says {phrase!r}")

    term = ((treatment.get("treatment_term") or {}).get("term") or {}).get("id")
    slots = [s for s in ("target_mechanisms", "target_phenotypes") if treatment.get(s)]
    if term in NON_THERAPEUTIC_TERMS and slots:
        yield Finding(
            "NON_THERAPEUTIC_TARGET",
            path,
            name,
            "; ".join(str(link.get("target")) for link in links),
            "",
            f"{term} {NON_THERAPEUTIC_TERMS[term]} carries {', '.join(slots)}",
        )


def _files(paths: list[Path]) -> list[Path]:
    if paths:
        return paths
    return sorted({p for pattern in PATTERNS for p in ROOT.glob(pattern)})


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def scan(paths: list[Path]) -> tuple[list[Finding], Counter]:
    """Findings, and the number of links per treatment_effect."""
    findings: list[Finding] = []
    effects: Counter = Counter()
    for path in _files(paths):
        try:
            data = load_document(path)
        except FileNotFoundError:
            raise
        except Exception as exc:  # malformed YAML is check-duplicate-keys' job
            print(f"{_display(path)}: could not parse ({exc})", file=sys.stderr)
            continue
        if not isinstance(data, dict):
            continue
        mechanisms = {
            node.get("name")
            for node in data.get("pathophysiology") or []
            if isinstance(node, dict)
        }
        for treatment in data.get("treatments") or []:
            if not isinstance(treatment, dict):
                continue
            for link in treatment.get("target_mechanisms") or []:
                if isinstance(link, dict):
                    effects[link.get("treatment_effect") or "(absent)"] += 1
            findings.extend(check_treatment(path, treatment, mechanisms))
    findings.sort(key=lambda f: (KINDS.index(f.kind), str(f.path), f.treatment))
    return findings, effects


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()  # one walk, so the parsed-KB cache is pure cost
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", nargs="*", type=Path, help="default: all of kb/")
    parser.add_argument(
        "--format", choices=("summary", "list", "tsv"), default="summary"
    )
    parser.add_argument("--kind", choices=KINDS, help="show only this class")
    args = parser.parse_args(argv)

    try:
        findings, effects = scan(args.paths)
    except FileNotFoundError as exc:
        print(f"no such file: {exc.filename}", file=sys.stderr)
        return 2
    failures = [f for f in findings if f.kind in GATING]
    shown = [f for f in findings if args.kind in (None, f.kind)]
    if args.format == "summary":
        shown = [f for f in shown if f.kind in GATING]

    if args.format == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
        writer.writerow(["kind", "file", "treatment", "target", "effect", "detail"])
        for f in shown:
            writer.writerow(
                [f.kind, _display(f.path), f.treatment, f.target, f.effect, f.detail]
            )
        return 1 if failures else 0

    for f in shown:
        print(
            f"{f.kind}: {_display(f.path)}: {f.treatment} -> {f.target}"
            f"{f' [{f.effect}]' if f.effect else ''}: {f.detail}"
        )
    counts = Counter(f.kind for f in findings)
    print(f"\n{sum(effects.values())} target_mechanisms links:")
    print("  " + ", ".join(f"{k}={n}" for k, n in effects.most_common()))
    for kind in KINDS:
        print(f"  {kind}: {counts[kind]}{' (gates)' if kind in GATING else ''}")
    if failures:
        print("\nAdd evidence to the link, or drop the negative treatment_effect.")
        return 1
    print("OK. Reported classes are leads; --format list shows them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
