#!/usr/bin/env python3
"""Taxonomic census of the animal models in the dismech knowledge base.

`species` on AnimalModel is free text, so "which entries are modelled only in
rodents?" cannot be answered by a grep. This script normalises the free-text
species strings into clades and reports, per entry, which clades carry a model
and which pathograph nodes any model is linked to.

Two uses. The census reports how many entries are mammal-only, which is the
shape of the gap an alternative-model research run sets out to close. The
per-entry mode prints one entry's nodes, models and the node-to-model links, and
generates the `existing_models` and `mechanism_nodes` variables of
templates/disease_alternative_models_research.md, so a prompt states the
record's current state rather than a remembered one.

Node links are read through `dismech.model_links.iter_model_links`, so a node
modelled by an organoid or an iPSC system counts as modelled. Clades are read
from `animal_models` alone, because only AnimalModel carries `species`.

Species strings that match no clade are never silently bucketed: they are
counted as `unclassified` and `--unclassified` lists them, so the mapping below
can be extended rather than guessed around.

    just model-taxon-census                        # the census tables
    just model-taxon-census --format tsv           # one row per entry
    just model-taxon-census --mammal-only          # entries with only mammalian models
    just model-taxon-census --unclassified         # species strings the mapping misses
    just model-taxon-census --entry Testicular_Dysgenesis_Syndrome
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
from dismech.model_links import iter_model_links

ROOTS = ("kb/disorders", "kb/modules")

# Ordered: the first clade whose pattern matches the lowercased species string wins.
# Patterns are substrings, not word-anchored, so "Mouse (Mus musculus)" and
# "mouse" both land in MAMMAL. Keep MAMMAL before the others: several strings
# name two species ("Rat and mouse", "Mouse and Drosophila melanogaster"), and
# a multi-species model is counted once, under the first clade matched.
CLADES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "mammal",
        (
            "mouse",
            "mus musculus",
            "murine",
            "rat",
            "rattus",
            "dog",
            "canis",
            "sheep",
            "ovis",
            "pig",
            "sus scrofa",
            "swine",
            "porcine",
            "rabbit",
            "oryctolagus",
            "cattle",
            "bovine",
            "bos taurus",
            "guinea pig",
            "cavia",
            "cat",
            "felis",
            "horse",
            "equus",
            "macaca",
            "macaque",
            "monkey",
            "marmoset",
            "callithrix",
            "baboon",
            "papio",
            "hamster",
            "mesocricetus",
            "peromyscus",
            "ferret",
            "mustela",
            "camel",
            "capra",
            "goat",
            "chlorocebus",
            "saimiri",
            "vervet",
            "lemur",
            "opossum",
            "monodelphis",
            "naked mole",
            "heterocephalus",
            "bat",
            "shrew",
            "rodent",
            "primate",
        ),
    ),
    (
        "fish",
        (
            "zebrafish",
            "danio",
            "medaka",
            "oryzias",
            "xiphophorus",
            "killifish",
            "fundulus",
            "nothobranchius",
            "tilapia",
            "oreochromis",
            "stickleback",
            "gasterosteus",
            "fathead minnow",
            "pimephales",
            "gambusia",
            "poecilia",
            "guppy",
            "cichlid",
            "astatotilapia",
            "trout",
            "oncorhynchus",
            "salmon",
            "salmo",
            "carp",
            "cyprinus",
            "catfish",
            "sea bass",
            "dicentrarchus",
            "skate",
            "leucoraja",
            "shark",
            "scyliorhinus",
            "dogfish",
            "lamprey",
            "petromyzon",
            "fish",
        ),
    ),
    (
        "amphibian",
        ("xenopus", "silurana", "frog", "rana", "toad", "bufo", "axolotl", "ambystoma", "newt", "salamander"),
    ),
    (
        "reptile",
        (
            "alligator",
            "crocodil",
            "caiman",
            "turtle",
            "trachemys",
            "lizard",
            "anolis",
            "pogona",
            "gecko",
            "snake",
            "python",
            "reptil",
        ),
    ),
    (
        "bird",
        (
            "chicken",
            "chick",
            "gallus",
            "quail",
            "coturnix",
            "duck",
            "anas",
            "zebra finch",
            "taeniopygia",
            "avian",
            "emu",
        ),
    ),
    (
        "invertebrate",
        (
            "drosophila",
            "fruit fly",
            "caenorhabditis",
            "nematode",
            "c. elegans",
            "daphnia",
            "planaria",
            "schmidtea",
            "aplysia",
            "sea urchin",
            "strongylocentrotus",
            "ciona",
            "hydra",
            "crustacean",
            "shrimp",
            "crayfish",
        ),
    ),
    (
        # Not an animal model at all. AnimalModel's own docstring sends
        # patient-derived and iPSC systems to `experimental_models`, so a human
        # species string here is a misfiling worth surfacing rather than hiding
        # in `unclassified`.
        "human",
        ("human", "homo sapiens", "patient-derived"),
    ),
    (
        "non-animal",
        (
            "saccharomyces",
            "yeast",
            "yarrowia",
            "schizosaccharomyces",
            "candida",
            "dictyostelium",
            "trypanosoma",
            "leishmania",
            "plasmodium",
            "toxoplasma",
            "chlamydomonas",
            "arabidopsis",
            "escherichia",
            "bacteri",
        ),
    ),
)

MAMMAL = "mammal"
NON_MAMMAL_ANIMAL = ("fish", "amphibian", "reptile", "bird", "invertebrate")


def classify(species: str) -> str:
    """Return the clade for a free-text `species` string, or "unclassified"."""
    text = re.sub(r"\s+", " ", (species or "").strip().lower())
    if not text:
        return "unclassified"
    for clade, needles in CLADES:
        if any(needle in text for needle in needles):
            return clade
    return "unclassified"


def model_sections(doc: dict) -> list[dict]:
    """Return the entry's animal models, tolerating a missing or null block."""
    models = doc.get("animal_models")
    return [m for m in models if isinstance(m, dict)] if isinstance(models, list) else []


def experimental_sections(doc: dict) -> list[dict]:
    """Return the entry's non-animal experimental models, if it has any."""
    models = doc.get("experimental_models")
    return [m for m in models if isinstance(m, dict)] if isinstance(models, list) else []


def linked_nodes_by_block(doc: dict) -> dict[str, set[str]]:
    """Map each modelled node name to the model blocks that link it.

    A model-to-mechanism link has more than one home -- `animal_models`,
    `experimental_models` and `computational_models` all carry
    `modeled_mechanisms` -- so a join that reads only `animal_models` marks an
    organoid- or iPSC-modelled node as unmodelled. That is the one fact this
    script exists to get right, since the research prompt sends the provider
    after exactly the nodes reported as unmodelled. `include_proposed=False`
    keeps the model systems of proposed experiments out: they have not been run,
    and this is a report about models that exist.
    """
    by_node: dict[str, set[str]] = {}
    for site in iter_model_links(doc, include_proposed=False):
        target = site.link.get("target")
        if target:
            by_node.setdefault(target, set()).add(site.path_prefix)
    return by_node


def render_existing_models(doc: dict) -> str:
    """The `existing_models` block for templates/disease_alternative_models_research.md.

    A deep-research prompt has to say what is already curated, or the provider
    spends its run re-deriving it. Both model blocks are listed, because
    AnimalModel keeps whole organisms and ExperimentalModel keeps organoids,
    organ-chips and iPSC systems, and "what models exist" spans the two.
    """
    lines: list[str] = []
    animals = model_sections(doc)
    if animals:
        lines.append("Animal models already curated:")
        lines.append("")
        for model in animals:
            label = model.get("name") or model.get("genotype") or "(unnamed)"
            species = model.get("species") or "species not stated"
            pub = model.get("publication") or "no publication recorded"
            lines.append(f"- **{label}** ({species}; {pub}), clade: {classify(species)}")
            targets = [
                m["target"]
                for m in (model.get("modeled_mechanisms") or [])
                if isinstance(m, dict) and m.get("target")
            ]
            if targets:
                lines.append(f"    - linked to: {', '.join(targets)}")
        lines.append("")
    else:
        lines.append("Animal models already curated: none. This entry has no `animal_models` block.")
        lines.append("")

    experimental = experimental_sections(doc)
    if experimental:
        lines.append("Non-animal experimental models already curated:")
        lines.append("")
        for model in experimental:
            label = model.get("name") or "(unnamed)"
            kind = model.get("experimental_model_type") or "type not stated"
            lines.append(f"- **{label}** ({kind})")
            targets = [
                m["target"]
                for m in (model.get("modeled_mechanisms") or [])
                if isinstance(m, dict) and m.get("target")
            ]
            if targets:
                lines.append(f"    - linked to: {', '.join(targets)}")
        lines.append("")
    else:
        lines.append(
            "Non-animal experimental models already curated: none. This entry has no "
            "`experimental_models` block, so organoid, organ-chip, slice and iPSC systems "
            "are an open field rather than a duplicate."
        )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_mechanism_nodes(doc: dict) -> str:
    """The `mechanism_nodes` block: every node, its scale, and whether anything models it.

    Printing the unmodelled ones matters more than printing the modelled ones.
    A node with no model link is where an alternative model has the most to
    add, and it is not visible from the YAML without this join.
    """
    nodes = doc.get("pathophysiology")
    if not isinstance(nodes, list):
        return "This entry has no `pathophysiology` block."

    linked = linked_nodes_by_block(doc)

    lines = ["| # | Node | Scale | Already modelled |", "|---|---|---|---|"]
    for index, node in enumerate(nodes, start=1):
        if not isinstance(node, dict):
            continue
        name = node.get("name") or "(unnamed)"
        scale = node.get("biological_scale") or "**not stated**"
        blocks = linked.get(name)
        # Naming the block is not decoration: an animal-modelled node and an
        # organoid-modelled one are differently open to an alternative model.
        state = f"yes ({', '.join(sorted(blocks))})" if blocks else "**no**"
        lines.append(f"| {index} | {name} | {scale} | {state} |")
    return "\n".join(lines)


def scan_entry(path: pathlib.Path, doc: dict) -> dict:
    """Summarise one entry's models and their links to pathograph nodes."""
    nodes = doc.get("pathophysiology")
    node_names = [n.get("name") for n in nodes if isinstance(n, dict)] if isinstance(nodes, list) else []

    # Clades are an AnimalModel question -- only that class carries `species` --
    # so the clade counters read `animal_models` alone, while the node links read
    # every model block. The two answer different questions; merging them would
    # make an organoid look like a taxon.
    models = model_sections(doc)
    clades: collections.Counter[str] = collections.Counter()
    unclassified: list[str] = []

    for model in models:
        species = model.get("species") or ""
        clade = classify(species)
        clades[clade] += 1
        if clade == "unclassified":
            unclassified.append(species)

    links_by_node = linked_nodes_by_block(doc)
    linked_nodes = set(links_by_node)

    present = {clade for clade, count in clades.items() if count}
    return {
        "file": path.name,
        "path": path,
        "entry": path.stem,
        "n_nodes": len(node_names),
        "node_names": node_names,
        "n_models": len(models),
        "clades": clades,
        "unclassified": unclassified,
        "linked_nodes": linked_nodes,
        "links_by_node": links_by_node,
        "unlinked_nodes": [n for n in node_names if n not in linked_nodes],
        "mammal_only": bool(models) and present <= {MAMMAL},
        "has_non_mammal": bool(present & set(NON_MAMMAL_ANIMAL)),
    }


def scan(roots: tuple[str, ...], only: str | None = None) -> list[dict]:
    """Scan the KB. `only` is an entry file stem, which skips parsing the rest."""
    rows = []
    for root in roots:
        directory = pathlib.Path(root)
        if not directory.is_dir():
            continue
        # `only` short-circuits the scan by filename. Without it, asking about one
        # entry parses every file in the KB -- thousands of them -- and the
        # template renderer asks twice per run.
        if only:
            candidate = directory / f"{only}.yaml"
            if candidate.is_file():
                doc = kb_cache.load_document(candidate)
                if isinstance(doc, dict):
                    rows.append(scan_entry(candidate, doc))
            continue
        for path, doc in kb_cache.iter_documents(directory):
            if isinstance(doc, dict):
                rows.append(scan_entry(path, doc))
    return rows


def print_entry(row: dict) -> None:
    """Per-entry detail: the query the TDS report's DisMech-side claims rest on."""
    print(f"# {row['entry']}")
    print(f"\n{row['n_nodes']} pathograph nodes, {row['n_models']} animal models.")

    if row["clades"]:
        spread = ", ".join(f"{clade} x{count}" for clade, count in sorted(row["clades"].items()))
        print(f"Model clades: {spread}")
        print(f"Mammal-only: {'yes' if row['mammal_only'] else 'no'}")
    else:
        print("Model clades: none - this entry has no animal_models block.")

    print("\n| Pathograph node | Model blocks linked to it |")
    print("|---|---|")
    for name in row["node_names"]:
        blocks = row["links_by_node"].get(name)
        print(f"| {name} | {', '.join(sorted(blocks)) if blocks else '-'} |")

    if row["unlinked_nodes"]:
        print(f"\nNodes with no model link ({len(row['unlinked_nodes'])}):")
        for name in row["unlinked_nodes"]:
            print(f"- {name}")

    if row["unclassified"]:
        print("\nSpecies strings this script's mapping does not cover:")
        for species in row["unclassified"]:
            print(f"- {species!r}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", action="append", dest="roots", metavar="DIR", help="KB directory (repeatable)")
    ap.add_argument("--entry", metavar="NAME", help="report one entry by file stem, e.g. Roberts_Syndrome")
    ap.add_argument("--format", choices=("markdown", "tsv"), default="markdown")
    ap.add_argument("--mammal-only", action="store_true", help="list entries whose models are all mammalian")
    ap.add_argument("--unclassified", action="store_true", help="list species strings the mapping misses")
    ap.add_argument(
        "--template-vars",
        choices=("existing_models", "mechanism_nodes"),
        metavar="VAR",
        help="with --entry, print one injectable block for "
        "templates/disease_alternative_models_research.md "
        "(existing_models or mechanism_nodes), for passing to deep-research-client --var",
    )
    args = ap.parse_args()
    if args.template_vars and not args.entry:
        ap.error("--template-vars requires --entry")

    kb_cache.default_off()
    rows = scan(tuple(args.roots) if args.roots else ROOTS, only=args.entry)
    if not rows:
        if args.entry:
            print(f"No entry named {args.entry!r} under {', '.join(args.roots or ROOTS)}.", file=sys.stderr)
        else:
            print("No entries found. Run from a dismech checkout, or pass --root.", file=sys.stderr)
        return 1

    if args.entry:
        wanted = [r for r in rows if r["entry"] == args.entry]
        if not wanted:
            print(f"No entry named {args.entry!r}.", file=sys.stderr)
            return 1
        if args.template_vars:
            doc = kb_cache.load_document(wanted[0]["path"])
            if args.template_vars == "existing_models":
                print(render_existing_models(doc))
            else:
                print(render_mechanism_nodes(doc))
            return 0
        print_entry(wanted[0])
        return 0

    if args.format == "tsv":
        writer = csv.writer(sys.stdout, delimiter="\t")
        writer.writerow(["entry", "n_nodes", "n_models", "mammal_only", "has_non_mammal", "clades"])
        for row in rows:
            writer.writerow(
                [
                    row["entry"],
                    row["n_nodes"],
                    row["n_models"],
                    int(row["mammal_only"]),
                    int(row["has_non_mammal"]),
                    ";".join(f"{c}={n}" for c, n in sorted(row["clades"].items())),
                ]
            )
        return 0

    if args.unclassified:
        missed: collections.Counter[str] = collections.Counter()
        for row in rows:
            missed.update(row["unclassified"])
        if not missed:
            print("Every species string matched a clade.")
            return 0
        print("| Species string | Models |")
        print("|---|---|")
        for species, count in missed.most_common():
            print(f"| {species} | {count} |")
        return 0

    if args.mammal_only:
        subset = [r for r in rows if r["mammal_only"]]
        print(f"{len(subset):,} entries carry animal models, all of them mammalian.\n")
        print("| Entry | Models | Nodes |")
        print("|---|---|---|")
        for row in sorted(subset, key=lambda r: -r["n_models"]):
            print(f"| {row['entry']} | {row['n_models']} | {row['n_nodes']} |")
        return 0

    totals: collections.Counter[str] = collections.Counter()
    entries_with: collections.Counter[str] = collections.Counter()
    for row in rows:
        totals.update(row["clades"])
        for clade in row["clades"]:
            entries_with[clade] += 1

    with_models = [r for r in rows if r["n_models"]]
    print(f"{len(rows):,} entries scanned. {len(with_models):,} carry at least one animal model.\n")

    print("| Clade | Models | Entries carrying one |")
    print("|---|---|---|")
    for clade, count in totals.most_common():
        print(f"| {clade} | {count:,} | {entries_with[clade]:,} |")

    mammal_only = sum(1 for r in with_models if r["mammal_only"])
    non_mammal = sum(1 for r in rows if r["has_non_mammal"])
    print(f"\n- {mammal_only:,} of {len(with_models):,} entries with models are mammal-only.")
    print(f"- {non_mammal:,} entries carry at least one non-mammalian animal model.")
    print(f"- {sum(1 for r in rows if not r['n_models']):,} entries carry no animal model at all.")
    if totals["human"]:
        print(
            f"- {totals['human']:,} model(s) name a human species string, which AnimalModel sends to experimental_models."
        )
    if totals["unclassified"]:
        print(
            f"- {totals['unclassified']:,} model(s) have a species string this mapping misses; see --unclassified."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
