#!/usr/bin/env python3
"""Census of toxicokinetic (ADME) pathophysiology nodes in the dismech pathograph.

An AOP excludes absorption, distribution, metabolism and excretion by design:
ADME determines the dose arriving at the molecular initiating event, and folding
it into the pathway is what would make the pathway chemical-specific. A dismech
chain runs ADME steps and mechanism steps together and marks neither, so this
script measures what is actually there:

  1. How many entries route their environmental exposures into an ADME node,
     rather than into an initiating-event-shaped one.
  2. How many ADME nodes carry no ontology binding, and what stands in for the
     disposition concept where one is bound.
  3. Which ADME nodes sit at ORGANISM scale with nothing on them but a GO
     process term -- a whole-body disposition claim described by a molecular
     or cellular process, which is the proxy case made visible.

Backs the toxicokinetic sections of projects/AOP_EMOD_ALIGNMENT.md. Run it
rather than trusting the figures there, which move with every curation PR.

    just tk-node-census                     # the page's three tables
    just tk-node-census --format list       # those, plus the unclear tier
    just tk-node-census --format tsv        # one row per matched node
    just tk-node-census --section exposures # one table on its own
    just tk-node-census --section unclear   # the nodes it declines to classify

Report-only: it always exits 0. Nothing here is a defect. An unbound ADME node
is a vocabulary gap, not a curation error, and the entries that route exposures
through an intake node are following the convention correctly.
"""

from __future__ import annotations

import argparse
import collections
import csv
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from dismech import kb_cache

ROOTS = ("kb/disorders", "kb/modules")

# Slots on a Pathophysiology node that can carry an ontology term.
TERM_SLOTS = (
    "biological_processes",
    "molecular_functions",
    "chemical_entities",
    "cellular_components",
    "anatomical_entities",
    "cell_types",
    "phenotype_term",
    "triggers",
)

# ADME is the disposition of a *xenobiotic*, and nearly every word for it has a
# second, endogenous sense that is not ADME: mucociliary clearance, autophagic
# clearance, renal excretion of magnesium, nutritional intake, cardiovascular
# redistribution. Two filters separate them, and neither is a word match on its
# own:
#
#   1. The corpus is restricted structurally, to entries where an environmental
#      exposure is wired into the pathograph and no infectious agent is named.
#      That is the Lead_Poisoning shape: a substance from outside the body is
#      the pathograph's entry point.
#   2. Within it, ENDOGENOUS below removes the physiological senses that
#      survive the restriction.
#
# Bare "metabolism" is deliberately absent from the phase patterns: it matches
# endogenous intermediary metabolism (folate one-carbon, fatty-acid oxidation)
# far more often than xenobiotic biotransformation. The qualified forms are
# kept. Both filters drop real ADME nodes they cannot tell from a physiological
# one, so each headline figure is a floor rather than a count -- and
# `--format list` shows the judgement calls. Nothing is counted on a word match
# alone: a node reaches a headline figure only once the structural test in (2)
# has placed the substance among the entry's own recorded exposures.

# Physiological senses of the ADME vocabulary. Checked before the phase
# patterns, so a hit here disqualifies the node outright.
ENDOGENOUS = re.compile(
    r"\b(mucociliary|secretion clearance|autophagic|apoptotic|phagocyt\w+|"
    r"nutritional intake|food intake|caloric|oral intake|fluid intake|"
    r"dietary intake|net acid|acid excretion|"
    r"(?:magnesium|potassium|sodium|calcium|phosphate|urate|bicarbonate|water)\s+(?:excretion|clearance|wasting)|"
    r"cardiovascular redistribution|brain sparing|biliary (?:compression|cyst|atresia|carcinoma|"
    r"malignan\w+|cirrhotic|tract (?:injury|carcinoma)|infection)|"
    r"client protein binding|aggregate deposition|creatinine clearance|"
    r"(?:lipid|fat|fat-soluble|vitamin|iron|zinc|folate|glucose|protein|nutrient|"
    r"amino acid|bile (?:salt|acid))\s+(?:mal)?absorption|"
    r"malabsorption|amyloid|mucus|mucin|MUC5B|pathobiont\w*|cryptosporidi\w*|"
    r"cerebrospinal|\bCSF\b|perivascular clearance|acoustic|receptor redistribution|"
    r"(?:bacterial|microbial|fungal|viral|spore|conidia|cyst|oocyst)\s+\w*\s*"
    r"(?:ingestion|inhalation|uptake|clearance))\b",
    re.IGNORECASE,
)

# The hard edge the exclusion list above cannot reach: "impaired clearance of
# LDL", "glymphatic clearance", "alveolar fluid clearance" and "impaired renal
# methotrexate elimination" are the same words about different things, and no
# pattern over a node name separates the disposition of a xenobiotic from the
# physiological handling of an endogenous ligand.
#
# So the census does not try. It asks a structural question instead: does the
# node name the substance the entry says the patient was exposed to? A node
# sharing a content word with one of the entry's own `environmental[]` exposure
# names is reported as XENOBIOTIC; everything else is UNCLEAR and listed
# separately for a reader. Only the XENOBIOTIC tier carries the headline
# figures, and that applies to the exposure-landing table as much as to the
# bindings one: without it the landing count picks up endogenous handling
# (methylglyoxal detoxification, hepatic iron overload, free-water intake)
# whose nodes happen to use the ADME vocabulary.
STOPWORDS = {
    "acute",
    "chronic",
    "exposure",
    "exposures",
    "occupational",
    "environmental",
    "ingestion",
    "inhalation",
    "dermal",
    "oral",
    "dietary",
    "contaminated",
    "drinking",
    "water",
    "dust",
    "from",
    "with",
    "high",
    "long",
    "term",
    "low",
    "excess",
    "excessive",
    "repeated",
    "prolonged",
    "systemic",
    "cellular",
    "tissue",
    "human",
    "patient",
    "patients",
    "disease",
    "induced",
    "related",
    "mediated",
    "impaired",
    "reduced",
    "increased",
    "via",
    "and",
    "the",
    "of",
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]{3,}")


def content_words(text: str) -> set[str]:
    return {
        w.lower() for w in WORD_RE.findall(text or "") if w.lower() not in STOPWORDS
    }


PHASES: list[tuple[str, re.Pattern[str]]] = [
    (
        "ABSORPTION",
        re.compile(
            r"\b(absorption|absorbed|absorb|ingestion|ingested|inhalation|inhaled|"
            r"intake|uptake|dermal penetration|gastrointestinal transfer)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "DISTRIBUTION",
        re.compile(
            r"\b(systemic distribution|tissue distribution|redistribution|"
            r"systemic exposure|overexposure|over-exposure|body burden|"
            r"tissue burden|protein binding|plasma protein binding|"
            r"sequestration in|deposition in|crosses the (?:placenta|blood-brain barrier))\b",
            re.IGNORECASE,
        ),
    ),
    (
        "METABOLISM",
        re.compile(
            r"\b(bioactivation|biotransformation|first[- ]pass|xenobiotic metabolism|"
            r"drug metabolism|hepatic metabolism|glucuronidation|sulfation|"
            r"acetylation of|detoxification|detoxif\w+)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "EXCRETION",
        re.compile(
            r"\b(clearance|elimination|excretion|enterohepatic|biliary|urinary excretion)\b",
            re.IGNORECASE,
        ),
    ),
]

# Candidate PBPKO process classes per phase, read from OLS (pbpko 2026-07-15).
# Labels are verbatim, including the ontology's own misspelling on PBPKO:00148.
PBPKO_CANDIDATES = {
    "ABSORPTION": ["PBPKO:00140 absorption"],
    "DISTRIBUTION": [
        "PBPKO:00146 distribution process",
        "PBPKO:00148 protein binding mediated distributiion process",
    ],
    "METABOLISM": [
        "PBPKO:00191 phase I metabolism",
        "PBPKO:00210 first pass metabolism",
        "PBPKO:00215 gut metabolism",
    ],
    "EXCRETION": [
        "PBPKO:00322 elimination",
        "PBPKO:00223 renal excretion",
        "PBPKO:00224 hepatic excretion",
        "PBPKO:00225 fecal excretion",
        "PBPKO:00144 enterohepatic recirculation",
    ],
}

MOLECULAR_SCALES = {"MOLECULAR", "CELLULAR"}


def phase_of(name: str) -> str | None:
    """The ADME phase a node name expresses, or None. First match wins.

    First match in PHASES order, so a node naming two phases is filed under the
    earlier one: "Cadmium Absorption and Systemic Distribution" and "Uptake and
    Metabolism" both read as ABSORPTION. The per-phase counts are therefore not
    a partition of the phases a node describes.
    """
    if not name or ENDOGENOUS.search(name):
        return None
    for phase, pattern in PHASES:
        if pattern.search(name):
            return phase
    return None


def node_terms(node: dict) -> list[tuple[str, str, str, str | None]]:
    """Every (slot, curie, label, modifier) bound anywhere on a node."""
    found = []
    for slot in TERM_SLOTS:
        value = node.get(slot)
        if isinstance(value, dict):
            value = [value]
        for item in value or []:
            if not isinstance(item, dict):
                continue
            term = item.get("term") or {}
            if term.get("id"):
                found.append(
                    (slot, term["id"], term.get("label") or "", item.get("modifier"))
                )
    return found


def entry_files() -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for root in ROOTS:
        paths.extend(sorted(pathlib.Path(root).glob("*.yaml")))
    return paths


def scan() -> tuple[list[dict], list[dict]]:
    """Return (adme_nodes, exposure_landings).

    Reads each document through `kb_cache.load_document`, which returns a
    shared read-only parse. Nothing here mutates a document.
    """
    adme_nodes: list[dict] = []
    landings: list[dict] = []
    skipped: list[pathlib.Path] = []

    for path in entry_files():
        try:
            doc = kb_cache.load_document(path)
        except Exception:
            skipped.append(path)
            continue
        if not isinstance(doc, dict):
            skipped.append(path)
            continue
        slug = path.stem
        # An entry naming an infectious agent is modelling pathogen entry, not
        # the disposition of a chemical. Structural signal, not a word match.
        is_infection = bool(doc.get("infectious_agent"))
        # The corpus for the binding census: entries that record an exposure to
        # something from outside the body. Without this, the ADME vocabulary
        # matches its physiological senses across the whole KB.
        exposure_driven = bool(doc.get("environmental")) and not is_infection
        # Vocabulary of the substances this entry says the patient met.
        exposure_words: set[str] = set()
        for exposure in doc.get("environmental") or []:
            if not isinstance(exposure, dict):
                continue
            exposure_words |= content_words(exposure.get("name") or "")
            term = exposure.get("exposure_term") or {}
            if isinstance(term, dict):
                exposure_words |= content_words(term.get("preferred_term") or "")
                inner = term.get("term") or {}
                if isinstance(inner, dict):
                    exposure_words |= content_words(inner.get("label") or "")

        for node in doc.get("pathophysiology") or []:
            if not isinstance(node, dict):
                continue
            name = node.get("name") or ""
            phase = phase_of(name)
            if not phase:
                continue
            if not exposure_driven:
                continue
            terms = node_terms(node)
            scale = node.get("biological_scale")
            shared = content_words(name) & exposure_words
            adme_nodes.append(
                {
                    "entry": slug,
                    "node": name,
                    "phase": phase,
                    "scale": scale or "",
                    "infection_entry": is_infection,
                    "substance": "XENOBIOTIC" if shared else "UNCLEAR",
                    "shared_words": sorted(shared),
                    "terms": terms,
                    "bound": bool(terms),
                    "scale_mismatch": (
                        scale == "ORGANISM"
                        and bool(terms)
                        and all(t[1].split(":")[0] == "GO" for t in terms)
                    ),
                }
            )

        targets = [
            (link.get("target"), link.get("environmental_effect"))
            for exposure in doc.get("environmental") or []
            if isinstance(exposure, dict)
            for link in exposure.get("influences_mechanisms") or []
            if isinstance(link, dict) and link.get("target")
        ]
        if not targets:
            continue
        # Same substance test as the bindings census: a landing target counts
        # only when it names something the entry records an exposure to.
        adme_targets = sorted({t for t, _ in targets if phase_of(t)})
        xenobiotic_targets = [
            t for t in adme_targets if content_words(t) & exposure_words
        ]
        unclear_targets = [
            t for t in adme_targets if not (content_words(t) & exposure_words)
        ]
        landings.append(
            {
                "entry": slug,
                "exposures": len(doc.get("environmental") or []),
                "links": len(targets),
                "adme_targets": xenobiotic_targets,
                "unclear_targets": unclear_targets,
                "infection_entry": is_infection,
            }
        )

    # "Run it rather than trusting the figures" only holds if a file the
    # census could not read is visible rather than silently absent.
    if skipped:
        print(
            f"warning: skipped {len(skipped)} unreadable entry file(s): "
            + ", ".join(str(p) for p in skipped[:5])
            + (" ..." if len(skipped) > 5 else ""),
            file=sys.stderr,
        )

    return adme_nodes, landings


def report_exposures(landings: list[dict], out) -> None:
    linked = [r for r in landings if r["links"]]
    hits = [r for r in linked if r["adme_targets"]]
    chemical = [r for r in hits if not r["infection_entry"]]
    infection = [r for r in hits if r["infection_entry"]]

    print("\n## Where pathograph-linked exposures land\n", file=out)
    print(
        f"entries with at least one `influences_mechanisms` link : {len(linked)}",
        file=out,
    )
    print(
        f"  of those, at least one exposure lands on an ADME node : {len(hits)}",
        file=out,
    )
    print(
        f"    entry declares no infectious agent (toxicokinetic)  : {len(chemical)}",
        file=out,
    )
    print(
        f"    entry declares an infectious agent (pathogen entry) : {len(infection)}",
        file=out,
    )
    print(file=out)
    for row in sorted(chemical, key=lambda r: (-r["exposures"], r["entry"])):
        print(
            f"  {row['entry']}  ({row['exposures']} exposures, {row['links']} links)",
            file=out,
        )
        for target in row["adme_targets"]:
            print(f"        -> {target}   [{phase_of(target)}]", file=out)

    unclear = [r for r in linked if r["unclear_targets"] and not r["adme_targets"]]
    chemical_unclear = [r for r in unclear if not r["infection_entry"]]
    print(
        f"\n  Not counted above: {len(chemical_unclear)} entries whose exposure lands"
        f"\n  on a node using the ADME vocabulary for a substance the entry records no"
        f"\n  exposure to -- endogenous handling (methylglyoxal detoxification, hepatic"
        f"\n  iron overload, free-water intake) rather than xenobiotic disposition:",
        file=out,
    )
    for row in sorted(chemical_unclear, key=lambda r: r["entry"]):
        for target in row["unclear_targets"]:
            print(
                f"    [{phase_of(target)}] {row['entry']}: {target}",
                file=out,
            )


def report_bindings(nodes: list[dict], out) -> None:
    tk = [
        n for n in nodes if not n["infection_entry"] and n["substance"] == "XENOBIOTIC"
    ]
    unclear = [
        n for n in nodes if not n["infection_entry"] and n["substance"] == "UNCLEAR"
    ]
    unbound = [n for n in tk if not n["bound"]]

    print("\n## What binds an ADME node\n", file=out)
    print(
        f"ADME nodes naming a substance the entry records an exposure to : {len(tk)}",
        file=out,
    )
    print(
        f"  across entries                                               : {len({n['entry'] for n in tk})}",
        file=out,
    )
    pct = (100 * len(unbound) / len(tk)) if tk else 0
    print(
        f"  carrying no ontology term at all                             : {len(unbound)} ({pct:.0f}%)",
        file=out,
    )

    prefixes = collections.Counter(t[1].split(":")[0] for n in tk for t in n["terms"])
    print(
        f"  prefixes used where bound                                    : {dict(prefixes.most_common())}",
        file=out,
    )

    by_phase = collections.Counter(n["phase"] for n in tk)
    print(
        "\n  by ADME phase, with the PBPKO process class that would cover it:", file=out
    )
    for phase, _ in PHASES:
        count = by_phase.get(phase, 0)
        unb = sum(1 for n in tk if n["phase"] == phase and not n["bound"])
        print(f"    {phase:<13} {count:>3} nodes ({unb} unbound)", file=out)
        for candidate in PBPKO_CANDIDATES[phase]:
            print(f"                  {candidate}", file=out)

    print("\n  unbound:", file=out)
    for n in sorted(unbound, key=lambda n: (n["entry"], n["node"])):
        print(f"    {n['entry']}: {n['node']}  [{n['scale'] or 'no scale'}]", file=out)

    print("\n  bound, with what stands in for the disposition concept:", file=out)
    for n in sorted(
        (n for n in tk if n["bound"]), key=lambda n: (n["entry"], n["node"])
    ):
        print(f"    {n['entry']}: {n['node']}  [{n['scale'] or 'no scale'}]", file=out)
        for _slot, curie, label, modifier in n["terms"]:
            suffix = f" / {modifier}" if modifier else ""
            print(f"          {curie} {label!r}{suffix}", file=out)

    print(
        f"\n  Not counted above: {len(unclear)} nodes using the same vocabulary for a"
        f"\n  substance the entry records no exposure to. Most are physiological"
        f"\n  handling of an endogenous ligand (LDL clearance, glymphatic clearance,"
        f"\n  alveolar fluid clearance) rather than xenobiotic disposition, but the"
        f"\n  split is not reliable enough to assert. Read them with --format list.",
        file=out,
    )


def report_unclear(nodes: list[dict], out) -> None:
    unclear = [
        n for n in nodes if not n["infection_entry"] and n["substance"] == "UNCLEAR"
    ]
    print("\n## ADME vocabulary, substance not among the entry's exposures\n", file=out)
    print(f"  {len(unclear)} nodes, for a reader rather than a count\n", file=out)
    for n in sorted(unclear, key=lambda n: (n["entry"], n["node"])):
        print(f"    [{n['phase']}] {n['entry']}: {n['node']}", file=out)


def report_scale(nodes: list[dict], out) -> None:
    mismatched = [
        n
        for n in nodes
        if n["scale_mismatch"]
        and not n["infection_entry"]
        and n["substance"] == "XENOBIOTIC"
    ]
    print("\n## ORGANISM-scale ADME nodes bound only to GO terms\n", file=out)
    print(f"  {len(mismatched)} nodes", file=out)
    for n in sorted(mismatched, key=lambda n: (n["entry"], n["node"])):
        print(f"    {n['entry']}: {n['node']}", file=out)
        for _slot, curie, label, modifier in n["terms"]:
            suffix = f" / {modifier}" if modifier else ""
            print(f"          {curie} {label!r}{suffix}", file=out)


def write_tsv(nodes: list[dict], out) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "entry",
            "node",
            "phase",
            "scale",
            "substance",
            "shared_words",
            "infection_entry",
            "bound",
            "scale_mismatch",
            "terms",
        ]
    )
    for n in sorted(nodes, key=lambda n: (n["entry"], n["node"])):
        terms = "; ".join(f"{c} {l}" for _s, c, l, _m in n["terms"])
        writer.writerow(
            [
                n["entry"],
                n["node"],
                n["phase"],
                n["scale"],
                n["substance"],
                " ".join(n["shared_words"]),
                int(n["infection_entry"]),
                int(n["bound"]),
                int(n["scale_mismatch"]),
                terms,
            ]
        )


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--format", choices=("summary", "tsv", "list"), default="summary"
    )
    parser.add_argument(
        "--section",
        choices=("all", "exposures", "bindings", "unclear", "scale"),
        default="all",
        help="restrict the summary to one table",
    )
    parser.add_argument(
        "--out", type=pathlib.Path, help="write to a file instead of stdout"
    )
    args = parser.parse_args(argv)

    nodes, landings = scan()
    out = args.out.open("w", encoding="utf-8") if args.out else sys.stdout
    try:
        if args.format == "tsv":
            write_tsv(nodes, out)
        else:
            if args.section in ("all", "exposures"):
                report_exposures(landings, out)
            if args.section in ("all", "bindings"):
                report_bindings(nodes, out)
            if args.section in ("all", "scale"):
                report_scale(nodes, out)
            # The unclear tier is a reading list, not a figure: shown on
            # request, or in the full listing, never in the summary.
            if args.section == "unclear" or (
                args.section == "all" and args.format == "list"
            ):
                report_unclear(nodes, out)
    finally:
        if args.out:
            out.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
