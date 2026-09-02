#!/usr/bin/env python3
"""Audit how diet is represented in the KB, on both of its independent tracks.

Diet reaches a dismech entry two ways, and they are **separate claims that share
an ontology**, not two views of one fact:

* **Causal** — an ``environmental[]`` entry saying a food, nutrient, or dietary
  pattern acts on the disease. Grounded by ``food_source`` (FOODON/CHEBI) and/or
  ``exposure_term`` (ECTO/XCO); reaches the pathograph via
  ``influences_mechanisms``.
* **Intervention** — a ``treatments[]`` entry prescribing a dietary change.
  Grounded by ``treatment_term`` (NCIT) plus ``dietary_modifications``
  (action + FOODON/CHEBI food); reaches the pathograph via ``target_mechanisms``.

Phenylketonuria carries both against the same ``FOODON:00001006``: meat as an
exposure, and ``AVOID`` meat as a prescription. That duplication is correct. This
audit therefore never reconciles the two tracks against each other, and never
reports one as missing because the other exists.

**What the headline counts.** Not binding coverage. A diet annotation earns its
place in the mechanism graph when there is evidence for it, so the gap worth
working is *cited but unlinked*: an entry with a supporting, snippet-backed
citation that no ``influences_mechanisms`` / ``target_mechanisms`` link puts on
the pathograph. The reverse defect — linked but uncited — is counted separately
and is the more urgent of the two, since it is already rendering.

**Evidence tiers are structural, not a quality judgment.** This script cannot
read a paper. It reports the shape of the citation and nothing more:

* ``CITED_HUMAN`` — a ``SUPPORT`` item with a non-empty ``snippet`` and
  ``evidence_source: HUMAN_CLINICAL``. For a dietary claim about people this is
  the tier that usually carries it, which is why it is broken out.
* ``CITED`` — a ``SUPPORT`` item with a snippet, from any other source tier.
* ``REFUTE_ONLY`` — snippet-backed ``REFUTE`` evidence and no ``SUPPORT``. The
  entry is evidenced, just negatively: a treatment recorded as ineffective
  against a mechanism it was tried on is a real, useful annotation. It is not a
  reason to *add* a link, so it never counts toward the gap, and it is emphatically
  not an uncited link, so it never counts as the inverse defect either.
* ``UNCITED`` — no snippet-backed evidence in either direction.

A ``CITED_HUMAN`` row is a candidate for the pathograph, never a verdict. Read
the snippet before linking anything: an observational association is not a
mechanism, and this script cannot tell them apart.

**Free text is a legitimate terminal state.** ``FoodTerm`` is reachable only from
``FOODON:00001002`` (food product) and ``CHEBI:33284`` (nutrient), so food
*components* — gluten (``FOODON:03420177``), casein, purines — sit outside it and
are correctly rejected today; named dietary *patterns* have no ontology home at
all. Per ``.claude/skills/dismech-terms``, no term beats a bad one. So this audit
reports ``FREE_TEXT`` as a state to review, never as an error, and the binding
census is deliberately the secondary axis.

Usage::

    uv run python scripts/diet_audit.py
    uv run python scripts/diet_audit.py --track causal --format list
    uv run python scripts/diet_audit.py --format tsv --out diet.tsv
    uv run python scripts/diet_audit.py --gap-only --format list
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path

#: KB subtrees that may carry ``environmental:`` or ``treatments:`` entries.
_KB_GLOBS = (
    "kb/disorders/*.yaml",
    "kb/modules/*.yaml",
    "kb/comorbidities/*.yaml",
)

#: NCIT clinical-action terms whose own definition makes the treatment dietary.
#: ``NCIT:C15433`` (Nutritional Support) is included for *detection* only —
#: CLAUDE.md warns it names a specific vitamin or compound more often than a diet
#: change, so it is never used here to infer a modality.
_DIET_TREATMENT_TERMS = frozenset({"NCIT:C15447", "NCIT:C15433"})

#: Words that make an entry diet-related. Recall-oriented: the matched word is
#: carried through to the output so a reviewer can spot a false positive rather
#: than having to trust the regex.
#:
#: Bare "sodium" is deliberately ABSENT. It matched 48 entries, almost all of
#: them drugs -- sodium channel blockers, sodium valproate, dantrolene sodium,
#: sodium phenylbutyrate. Every genuinely dietary one ("Low-Sodium Diet",
#: "Dietary sodium restriction") carries "diet"/"dietary"/"salt"/"intake" as
#: well, so removing it costs no recall.
#:
#: The two tracks read different fields, because their prose differs in kind. An
#: ``environmental[]`` entry is short and wholly about its exposure, so its
#: description is signal. A ``treatments[]`` description is a clinical paragraph
#: that mentions diet incidentally all the time -- matching it pulled in ACE
#: inhibitors (on "sodium"), cleft palate repair (on "feeding") and beta
#: blockers. A dietary treatment names itself, so the intervention track matches
#: ``name`` only.
_DIET_WORDS = (
    r"diet|dietary|nutrition|nutritional|malnutrition|undernutrition|food|feeding|"
    r"breastfeed|breastfeeding|weaning|formula|enteral|parenteral|fasting|"
    r"ketogenic|caloric|calorie|obesogenic|micronutrient|supplement|supplementation|"
    r"vitamin|folate|folic|thiamine|riboflavin|pyridoxine|niacin|biotin|carnitine|"
    r"iodine|selenium|zinc|alcohol|ethanol|beer|wine|gluten|lactose|galactose|"
    r"fructose|sucrose|purine|oxalate|phenylalanine|protein intake|salt|"
    r"sugar|glycemic|meat|dairy|milk|shellfish|seafood|cassava|soy|peanut|"
    r"fruit|vegetable|grain|wheat|barley|rye|caffeine"
)
_DIET_RE = re.compile(rf"\b({_DIET_WORDS})\b", re.IGNORECASE)

#: Names that read as a dietary *pattern* rather than a specific food. These have
#: no FOODON home (FOODON describes food products, not eating patterns), so they
#: land on ``exposure_term`` and scatter across ECTO/XCO. Reported separately so
#: the scatter is visible and can be standardized on one CURIE per pattern.
_PATTERN_RE = re.compile(
    r"\b(diet|dietary pattern|intake|consumption|regimen|eating|nutrition)\b",
    re.IGNORECASE,
)

#: Names that carry a diet word for a non-dietary reason. Kept to cases actually
#: observed in the KB rather than speculated: ethanol as a sclerosant is a
#: cardiac procedure, a vitamin K antagonist is warfarin, and radioactive iodine
#: is a radiotherapy (unlike dietary iodine deficiency or excess, which are real
#: causal entries and must keep matching).
_EXCLUDE_RE = re.compile(
    r"septal ablation|vitamin k antagonist|radioactive iodine", re.IGNORECASE
)

_STATE_BOUND = "BOUND"
_STATE_PARTIAL = "PARTIAL"
_STATE_FREE_TEXT = "FREE_TEXT"

_TIER_HUMAN = "CITED_HUMAN"
_TIER_CITED = "CITED"
_TIER_REFUTE = "REFUTE_ONLY"
_TIER_UNCITED = "UNCITED"
_TIERS = (_TIER_HUMAN, _TIER_CITED, _TIER_REFUTE, _TIER_UNCITED)


@dataclass
class _DietItem:
    """One diet-related entry, on either track."""

    track: str  # "causal" or "intervention"
    path: str
    entry: str
    name: str
    linked: bool
    state: str
    tier: str
    curies: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    trigger: str = ""
    matched_in: str = ""
    modality: str = ""
    pattern_like: bool = False

    @property
    def slug(self) -> str:
        return Path(self.path).stem

    @property
    def gap(self) -> bool:
        """Supported but off the pathograph — the tranche this audit exists to find.

        ``REFUTE_ONLY`` is excluded: refuting evidence argues against the edge.
        """
        return self.tier in (_TIER_HUMAN, _TIER_CITED) and not self.linked

    @property
    def weak_match(self) -> bool:
        """Diet signal found only in free prose, not in a name or a bound slot."""
        return self.matched_in == "description"

    @property
    def unevidenced_link(self) -> bool:
        """On the pathograph with no evidence at all. Rendering already; fix first.

        A ``REFUTE_ONLY`` entry is NOT this: a treatment linked to a mechanism it
        demonstrably fails against is correctly curated, and flagging it would
        send a curator to "fix" an entry that is already right.
        """
        return self.linked and self.tier == _TIER_UNCITED


def _evidence_tier(items) -> str:
    """Grade a list of ``EvidenceItem`` dicts structurally. See module docstring."""
    if not isinstance(items, list):
        return _TIER_UNCITED
    tier = _TIER_UNCITED
    for item in items:
        if not isinstance(item, dict):
            continue
        if not str(item.get("snippet") or "").strip():
            continue
        supports = item.get("supports")
        # A REFUTE item is real evidence and must not read as "uncited", but it
        # is not a reason to draw a causal edge either. It therefore takes its
        # own tier, which SUPPORT always outranks.
        if supports == "REFUTE":
            if tier == _TIER_UNCITED:
                tier = _TIER_REFUTE
            continue
        if supports != "SUPPORT":
            continue
        if item.get("evidence_source") == "HUMAN_CLINICAL":
            return _TIER_HUMAN
        tier = _TIER_CITED
    return tier


def _descriptor_term(descriptor) -> tuple[str, str] | None:
    """Return ``(curie, label)`` from a descriptor, or None if it carries no term."""
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if not isinstance(term, dict) or not term.get("id"):
        return None
    return str(term["id"]), str(term.get("label") or "")


def _text_of(obj: dict, keys) -> str:
    return " ".join(str(obj.get(k) or "") for k in keys)


def _matched_word(text: str) -> str:
    hit = _DIET_RE.search(text)
    return hit.group(1).lower() if hit else ""


def _classify_causal(env: dict) -> _DietItem | None:
    """Classify one ``environmental[]`` entry, or None if it is not diet-related."""
    food = _descriptor_term(env.get("food_source"))
    exposure = _descriptor_term(env.get("exposure_term"))
    text = _text_of(env, ("name", "description", "notes", "effect"))
    trigger = _matched_word(text)

    # A food_source is a definitive signal regardless of wording. Otherwise fall
    # back to the label of a bound exposure term, then to the entry's own prose.
    has_food_block = isinstance(env.get("food_source"), dict)
    exposure_label_hit = _matched_word(exposure[1]) if exposure else ""
    env_name = str(env.get("name") or "")
    if _EXCLUDE_RE.search(env_name):
        return None
    name_hit = _matched_word(env_name)
    if not (has_food_block or exposure_label_hit or trigger):
        return None

    # Where the diet signal came from, strongest first. A ``food_source`` block
    # or a diet word in the entry's own NAME is decisive. A match found only in
    # the description is the weak tail -- it is what pulled in Ependymoma
    # ("high-dose ionizing radiation", whose description mentions diet) and CKD
    # tobacco smoking (on "glycemic"). Kept, because it also catches real
    # entries whose name is generic ("Dietary Factors"), but labelled so a
    # reviewer can filter it out.
    if has_food_block:
        matched_in = "food_source"
    elif name_hit:
        matched_in = "name"
    elif exposure_label_hit:
        matched_in = "term_label"
    else:
        matched_in = "description"

    curies = [c for c, _ in filter(None, (food, exposure))]
    labels = [label for _, label in filter(None, (food, exposure))]

    if food or exposure:
        state = _STATE_BOUND
    elif has_food_block or isinstance(env.get("exposure_term"), dict):
        # A block exists but carries only a free-text preferred_term. Distinct
        # from FREE_TEXT: somebody reached for a binding and stopped.
        state = _STATE_PARTIAL
    else:
        state = _STATE_FREE_TEXT

    name = str(env.get("name") or "(unnamed)")
    return _DietItem(
        track="causal",
        path="",
        entry="",
        name=name,
        linked=bool(env.get("influences_mechanisms")),
        state=state,
        tier=_evidence_tier(env.get("evidence")),
        curies=curies,
        labels=labels,
        trigger=name_hit or trigger or exposure_label_hit,
        matched_in=matched_in,
        pattern_like=bool(_PATTERN_RE.search(name)),
    )


def _classify_intervention(tx: dict) -> _DietItem | None:
    """Classify one ``treatments[]`` entry, or None if it is not diet-related."""
    term = tx.get("treatment_term")
    term = term if isinstance(term, dict) else {}
    tid = str(
        ((term.get("term") or {}) if isinstance(term.get("term"), dict) else {}).get(
            "id"
        )
        or ""
    )
    name = str(tx.get("name") or "(unnamed)")
    mods = term.get("dietary_modifications")
    has_mods = bool(mods) and isinstance(mods, list)
    # Name only -- see the note on _DIET_WORDS.
    trigger = "" if _EXCLUDE_RE.search(name) else _matched_word(name)

    if not (tid in _DIET_TREATMENT_TERMS or has_mods or trigger):
        return None

    matched_in = (
        "dietary_modifications"
        if has_mods
        else ("name" if trigger else "treatment_term")
    )

    curies: list[str] = []
    labels: list[str] = []
    for mod in mods or []:
        hit = _descriptor_term(mod.get("food")) if isinstance(mod, dict) else None
        if hit:
            curies.append(hit[0])
            labels.append(hit[1])

    if has_mods:
        state = _STATE_BOUND if curies else _STATE_PARTIAL
    else:
        state = _STATE_FREE_TEXT

    return _DietItem(
        track="intervention",
        path="",
        entry="",
        name=name,
        linked=bool(tx.get("target_mechanisms")),
        state=state,
        tier=_evidence_tier(tx.get("evidence")),
        curies=curies,
        labels=labels,
        trigger=trigger or tid,
        matched_in=matched_in,
        modality=str(tx.get("therapeutic_modality") or ""),
    )


def collect(repo_root: Path | None = None) -> list[_DietItem]:
    """Walk the KB and return every diet-related entry on both tracks."""
    # Resolved at call time, not bound as a default, so tests can point the walk
    # at a fixture tree.
    repo_root = repo_root if repo_root is not None else _REPO_ROOT
    out: list[_DietItem] = []
    for pattern in _KB_GLOBS:
        for path in sorted(repo_root.glob(pattern)):
            try:
                doc = safe_load_path(path)
            except Exception as exc:  # report and keep auditing the rest
                print(f"WARNING: could not parse {path}: {exc}", file=sys.stderr)
                continue
            if not isinstance(doc, dict):
                continue
            rel = str(path.relative_to(repo_root))
            entry_name = str(doc.get("name") or path.stem)
            for section, classify in (
                ("environmental", _classify_causal),
                ("treatments", _classify_intervention),
            ):
                for raw in doc.get(section) or []:
                    if not isinstance(raw, dict):
                        continue
                    item = classify(raw)
                    if item is None:
                        continue
                    item.path = rel
                    item.entry = entry_name
                    out.append(item)
    return out


def _pct(part: int, whole: int) -> str:
    return f"{(100.0 * part / whole):.1f}%" if whole else "n/a"


def _print_track(items: list[_DietItem], track: str, link_slot: str, top: int) -> None:
    rows = [i for i in items if i.track == track]
    if not rows:
        return
    total = len(rows)
    files = len({i.path for i in rows})
    linked = [i for i in rows if i.linked]
    print(f"=== {track.upper()} track — {total} entries in {files} files ===")
    print(
        f"  on the pathograph (via {link_slot}): {len(linked)} ({_pct(len(linked), total)})"
    )
    print()

    print(f"  {'evidence':<12} | {'on graph':>8} | {'off graph':>9} | {'total':>6}")
    print(f"  {'-' * 12}-+-{'-' * 8}-+-{'-' * 9}-+-{'-' * 6}")
    for tier in _TIERS:
        on = sum(1 for i in rows if i.tier == tier and i.linked)
        off = sum(1 for i in rows if i.tier == tier and not i.linked)
        print(f"  {tier:<12} | {on:>8} | {off:>9} | {on + off:>6}")
    print()

    gap = [i for i in rows if i.gap]
    human_gap = [i for i in gap if i.tier == _TIER_HUMAN]
    print(f"  GAP (cited, off the pathograph): {len(gap)}")
    print(f"    of which CITED_HUMAN — the strongest candidates: {len(human_gap)}")
    weak = [i for i in gap if i.weak_match]
    if weak:
        print(
            f"    minus {len(weak)} matched only on description prose — the "
            f"false-positive tail; filter with --strong-only"
        )
    unev = [i for i in rows if i.unevidenced_link]
    print(
        f"  INVERSE DEFECT (on the pathograph, uncited): {len(unev)} — already rendering"
    )
    print()

    print("  ontology binding (secondary; FREE_TEXT is a valid outcome):")
    for state in (_STATE_BOUND, _STATE_PARTIAL, _STATE_FREE_TEXT):
        n = sum(1 for i in rows if i.state == state)
        print(f"    {state:<10} {n:>5}  ({_pct(n, total)})")
    print()

    by_file = Counter(i.path for i in gap)
    if by_file:
        print(f"  Top {top} files by CITED-but-unlinked {track} entries:")
        for path, n in by_file.most_common(top):
            human = sum(1 for i in gap if i.path == path and i.tier == _TIER_HUMAN)
            print(f"    {n:>3} ({human} human)  {Path(path).stem}")
        print()


def _print_summary(items: list[_DietItem], top: int) -> None:
    files = len({i.path for i in items})
    print(f"Diet-related entries across kb/: {len(items)} in {files} files")
    print()
    _print_track(items, "causal", "influences_mechanisms", top)
    _print_track(items, "intervention", "target_mechanisms", top)

    # Dietary patterns have no FOODON home, so they land on exposure_term and
    # scatter. One CURIE per pattern is the fix; this shows where it is needed.
    patterns: dict[str, Counter] = defaultdict(Counter)
    for i in items:
        if i.track == "causal" and i.pattern_like and i.curies:
            patterns[i.trigger or "(unmatched)"][i.curies[0]] += 1
    scattered = {k: v for k, v in patterns.items() if len(v) > 1}
    if scattered:
        print("Dietary-pattern concepts bound to >1 CURIE — standardization targets:")
        for key, counter in sorted(
            scattered.items(), key=lambda kv: -sum(kv[1].values())
        ):
            detail = ", ".join(f"{c} x{n}" for c, n in counter.most_common())
            print(f"  {key}: {detail}")
        print()

    unbound_concepts = Counter(
        i.name.strip().lower()
        for i in items
        if i.state == _STATE_FREE_TEXT and i.track == "causal"
    )
    recurring = [(n, c) for n, c in unbound_concepts.most_common(top) if c > 1]
    if recurring:
        print("Recurring unbound causal concepts (review; free text may be correct):")
        for name, n in recurring:
            print(f"  {n:>3}  {name}")


def _print_list(items: list[_DietItem]) -> None:
    for i, item in enumerate(sorted(items, key=lambda x: (x.track, x.slug, x.name)), 1):
        link = "graph" if item.linked else "  -  "
        curies = ",".join(item.curies) or "-"
        print(
            f"{i:4d}. [{item.track[:4]}] [{item.tier:<11}] [{link}] "
            f"[{item.state:<9}] {item.slug:<44} | {item.name}  "
            f"({curies}; via {item.matched_in})"
        )


def _write_tsv(items: list[_DietItem], out) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "track",
            "path",
            "entry",
            "name",
            "pathograph_linked",
            "binding_state",
            "evidence_tier",
            "curies",
            "labels",
            "matched_on",
            "matched_in",
            "therapeutic_modality",
            "pattern_like",
        ]
    )
    for i in sorted(items, key=lambda x: (x.track, x.path, x.name)):
        writer.writerow(
            [
                i.track,
                i.path,
                i.entry,
                i.name,
                "yes" if i.linked else "no",
                i.state,
                i.tier,
                ";".join(i.curies),
                ";".join(i.labels),
                i.trigger,
                i.matched_in,
                i.modality,
                "yes" if i.pattern_like else "no",
            ]
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--track",
        choices=("both", "causal", "intervention"),
        default="both",
        help="which track to report on (default: both)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv"),
        default="summary",
        help="summary counts (default), a per-entry list, or a TSV table",
    )
    parser.add_argument(
        "--gap-only",
        action="store_true",
        help="restrict to CITED entries that are off the pathograph. Applies to "
        "--format list/tsv; the summary is always the full census.",
    )
    parser.add_argument(
        "--strong-only",
        action="store_true",
        help="drop entries whose only diet signal is a word in free prose. "
        "Applies to --format list/tsv.",
    )
    parser.add_argument(
        "--human-only",
        action="store_true",
        help="restrict to CITED_HUMAN entries. Applies to --format list/tsv.",
    )
    parser.add_argument(
        "--top", type=int, default=20, help="rows in the per-file and concept tables"
    )
    parser.add_argument("--out", type=Path, help="write to this file instead of stdout")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any diet entry is on the pathograph with no citation "
        "(advisory by default)",
    )
    args = parser.parse_args(argv)

    all_items = collect()

    selected = all_items
    if args.track != "both":
        selected = [i for i in selected if i.track == args.track]
    if args.gap_only:
        selected = [i for i in selected if i.gap]
    if args.strong_only:
        selected = [i for i in selected if not i.weak_match]
    if args.human_only:
        selected = [i for i in selected if i.tier == _TIER_HUMAN]

    summary_scope = (
        all_items
        if args.track == "both"
        else [i for i in all_items if i.track == args.track]
    )

    stream = args.out.open("w", encoding="utf-8") if args.out else sys.stdout
    try:
        if args.format == "tsv":
            _write_tsv(selected, stream)
        else:
            original = sys.stdout
            sys.stdout = stream
            try:
                if args.format == "list":
                    _print_list(selected)
                else:
                    # Always the full corpus for the chosen track: a census
                    # narrowed by a filter would report a percentage of its own
                    # selection.
                    _print_summary(summary_scope, args.top)
            finally:
                sys.stdout = original
    finally:
        if args.out:
            stream.close()
            print(f"Wrote {args.out}", file=sys.stderr)

    if args.strict:
        bad = [i for i in all_items if i.unevidenced_link]
        if bad:
            print(
                f"STRICT: {len(bad)} diet entries are on the pathograph with no "
                "supporting snippet-backed citation.",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
