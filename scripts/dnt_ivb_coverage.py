#!/usr/bin/env python3
"""How far the DNT in vitro battery's endpoints reach into the dismech pathograph.

The developmental neurotoxicity in vitro battery (DNT-IVB) is a set of assays,
each scoring one process in nervous-system development, assembled so a chemical
can be screened against all of them. Figure 1 of the PARC work package 5 paper
(doi:10.3389/ftox.2024.1359507) shows two generations of it, v1.0 and v2.0, as
20 labelled boxes. Three endpoints appear in both, leaving **17 distinct
processes**, which are the rows this script counts.

For each endpoint it reports the pathophysiology and phenotype nodes whose
*name* carries that endpoint's vocabulary, the entries those nodes belong to,
and whether any experimental, animal or computational model is linked to the
node through ``modeled_mechanisms``.

What a match is, and is not
---------------------------
**This is lexical matching, not a mapping.** dismech records no crosswalk to
this battery. A match means a node's name contains the endpoint's vocabulary;
whether the biology corresponds is a judgement left to a reader, and for the
largest rows it frequently does not. Every count here is an upper bound on what
could be mapped.

Two filters shape the result, and each has already been wrong once:

* The endpoint patterns are substring regexes. ``cognit`` matched
  *re-cognit-ion* and pulled 23 pattern-recognition-receptor nodes into
  *Learning and memory* before the negative lookbehind below was added.
* ``NEURAL`` drops a node whose name, GO labels, cell types and file stem carry
  no neural vocabulary. It exists to keep immunological memory and cancer cell
  migration out of the behavioural and migration rows. It was also discarding
  ``nmda_receptor_hypofunction`` > *Learning and Memory Impairment*, which is
  bound to GO ``learning`` and GO ``memory`` and is the single most on-point
  node in the corpus for that endpoint, because nothing in it says "neuro".
  Neurotransmitter vocabulary was added to fix that.

Assume more of both kinds remain. ``--format tsv --table nodes`` prints every
matched node so the filters can be audited rather than trusted.

Links
-----
Each node is emitted with a deep link to its own card on the published page:
``…/pages/disorders/<slugify(name)>.html#pathophysiology-<node-slug>``. The page
filename comes from the entry's ``name``, **not** its file stem; the two differ
for a sixth of the matched entries, and using the stem yields pages that do not
exist. ``--check-anchors`` re-checks every link against a rendered ``pages/``
tree, because a fragment matching no element is a silent failure: the browser
loads the page, stays at the top and reports no error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, NamedTuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech import kb_cache  # noqa: E402
from dismech.export.utils import slugify  # noqa: E402

# The renderer owns anchor construction; importing keeps the two from drifting
# silently. If it moves, this fails loudly, which is the point.
from dismech.render import _make_anchor_id  # noqa: E402

SITE = "https://dismech.monarchinitiative.org/pages"
MODEL_SECTIONS = ("experimental_models", "animal_models", "computational_models")
MODEL_LABELS = {
    "experimental_models": "NAM",
    "animal_models": "animal",
    "computational_models": "in silico",
}


class Endpoint(NamedTuple):
    """One DNT-IVB process, and the node names it claims."""

    term: str
    version: str  # "v1.0", "v2.0" or "v1.0+v2.0"
    substrate: str  # assay substrate, as Figure 1's caption explains the colours
    pattern: re.Pattern[str]
    ambiguous: bool  # whether the neural filter applies to this row


def _ep(term: str, version: str, substrate: str, pattern: str, ambiguous: bool) -> Endpoint:
    return Endpoint(term, version, substrate, re.compile(pattern, re.I), ambiguous)


#: The 17 distinct processes of DNT-IVB v1.0 and v2.0. ``substrate`` records what
#: Figure 1's caption states: blue boxes are human cells, yellow are rat primary
#: cells, green are early life-stage zebrafish. The caption does not explain the
#: remaining v2.0 colours, so those are "unstated" rather than guessed at.
ENDPOINTS: tuple[Endpoint, ...] = (
    _ep("NPC proliferation", "v1.0", "human cells",
        r"(neural|neuronal|neuroepithel|progenitor|stem cell|neuroblast|NPC|NSC)"
        r"[^|]{0,40}prolifer|prolifer[^|]{0,40}(progenitor|neural stem|neuroblast|NPC)", True),
    _ep("NPC apoptosis", "v1.0", "human cells",
        r"(progenitor|neural stem|neuroblast|NPC|neuroepithel)[^|]{0,40}(apopto|cell death|death)"
        r"|apopto[^|]{0,40}(progenitor|neural stem|neuroblast)", True),
    _ep("NP-neuronal differentiation", "v1.0", "human cells",
        r"neuronal differentiation|neurogenesis|neuron(al)? (fate|specification|maturation)"
        r"|differentiation of neuron", False),
    _ep("NP-glial differentiation", "v1.0", "human cells",
        r"glial differentiation|gliogenesis|astrocyt\w+ differentiation"
        r"|oligodendrocyt\w+ differentiation|glial (fate|specification)|astrogliogenesis", False),
    _ep("Neurite outgrowth", "v1.0+v2.0", "human cells",
        r"neurite|axon(al)? (outgrowth|growth|extension|elongation|guidance|pathfinding)"
        r"|dendrit\w+ (outgrowth|growth|arboriz|development|morphogenesis)|growth cone", False),
    _ep("Cell migration", "v1.0", "human cells", r"migration|migratory", True),
    _ep("Synaptogenesis", "v1.0+v2.0", "rat primary cells",
        r"synaptogenesis|synapse formation|synaptic (formation|development|assembly|pruning|density)"
        r"|dendritic spine", False),
    _ep("Neural network formation", "v1.0+v2.0", "rat primary cells",
        r"neural network|neuronal network|network formation"
        r"|circuit (formation|assembly|development|wiring)|connectivity|synchron", True),
    _ep("Myelination", "v2.0", "unstated",
        r"myelin|demyelinat|dysmyelinat|hypomyelinat|remyelinat", True),
    _ep("BBB function", "v2.0", "unstated",
        r"blood[- ]brain barrier|blood[- ]nerve barrier|\bBBB\b|neurovascular unit", False),
    _ep("Mitochondrial dysfunction", "v2.0", "unstated", r"mitochondri", True),
    _ep("Motorneuron development", "v2.0", "zebrafish",
        r"motor ?neuron|motoneuron|anterior horn|corticospinal", True),
    # (?<!re) keeps "recognition"/"recognize" out: both contain the substring "cognit".
    _ep("Learning and memory", "v2.0", "zebrafish", r"learning|memory|(?<!re)cognit", True),
    _ep("Escape response", "v2.0", "zebrafish",
        r"escape response|startle|flight response|photomotor", True),
    _ep("Anxiety-like behavior", "v2.0", "zebrafish", r"anxiet|anxious", True),
    _ep("Epigenetic markers", "v2.0", "unstated",
        r"epigenet|DNA methylat|histone (methylat|acetylat|modif)"
        r"|chromatin (remodel|modif)|imprint", True),
    _ep("Sub-cellular morphology", "v2.0", "unstated",
        r"subcellular|sub-cellular|organelle (morpholog|structure)"
        r"|endoplasmic reticulum (morpholog|structure|stress)"
        r"|Golgi (morpholog|fragment|structure)"
        r"|cytoskelet\w+ (organiz|morpholog|structure)", True),
)

#: A node is neural if its name, GO labels, cell types or file stem say so. The
#: neurotransmitter terms at the end are neural by definition and cannot admit
#: the immune false positives this filter exists to remove.
NEURAL = re.compile(
    r"neur|glia|glial|astrocy|oligodendro|microglia|axon|dendri|synap|brain|cortic|cortex"
    r"|cerebr|cerebell|myelin|schwann|ganglion|spinal|nerve|hippocamp|striat|thalam|retina"
    r"|motoneuron|radial glia|progenitor|neural crest|CNS|PNS|behaviou?r|cognit|encephal"
    r"|white matter|grey matter|gray matter"
    r"|nmda|ampa|glutamat|gaba|dopamin|serotoner|cholinerg|adrenerg|neurotransmit|excitotox",
    re.I,
)

#: Immunological memory is the dominant false positive for "Learning and memory".
IMMUNE = re.compile(
    r"\b(T cell|B cell|CD8|CD4|lymphocyt|immunolog|antibod|plasma cell|NK cell|humoral|vaccin)",
    re.I,
)


class Node(NamedTuple):
    entry: str
    kind: str  # "disorder" or "module"
    section: str  # "pathophysiology" or "phenotypes"
    node: str
    url: str
    go: tuple[str, ...]
    cells: tuple[str, ...]
    scale: str
    models: tuple[str, ...]
    readouts: tuple[str, ...]


def _terms(descriptors: Any) -> list[str]:
    out = []
    for d in descriptors or []:
        if isinstance(d, dict) and isinstance(d.get("term"), dict):
            label = d["term"].get("label")
            if label:
                out.append(str(label))
    return out


def _model_links(document: dict) -> dict[str, list[dict]]:
    """Index a document's ``modeled_mechanisms`` by the bare node name they target."""
    links: dict[str, list[dict]] = {}
    for section in MODEL_SECTIONS:
        for model in document.get(section) or []:
            if not isinstance(model, dict):
                continue
            for link in model.get("modeled_mechanisms") or []:
                if not isinstance(link, dict) or not link.get("target"):
                    continue
                kind = (
                    model.get("experimental_model_type")
                    or model.get("species")
                    or "unspecified"
                )
                parts = [f"{MODEL_LABELS[section]}: {kind}"]
                for slot in ("relationship", "fidelity", "model_scale"):
                    if link.get(slot):
                        parts.append(str(link[slot]))
                links.setdefault(str(link["target"]), []).append(
                    {
                        "summary": " · ".join(parts),
                        "readouts": [
                            str(r["name"])
                            for r in link.get("readouts") or []
                            if isinstance(r, dict) and r.get("name")
                        ],
                    }
                )
    return links


def _page_url(kind: str, stem: str, name: str) -> str:
    # Module pages are named by file stem; disorder pages by slugify(entry name).
    if kind == "module":
        return f"{SITE}/modules/{stem}.html"
    return f"{SITE}/disorders/{slugify(name)}.html"


def _anchor(kind: str, section: str) -> str:
    if section == "phenotypes":
        return "phenotype"
    return "module-pathophysiology" if kind == "module" else "pathophysiology"


def collect(kb: Path) -> dict[str, list[Node]]:
    """Walk kb/disorders and kb/modules once each, matching every endpoint."""
    found: dict[str, list[Node]] = {e.term: [] for e in ENDPOINTS}
    for kind, directory in (("disorder", kb / "disorders"), ("module", kb / "modules")):
        if not directory.is_dir():
            continue
        for path, document in kb_cache.iter_documents(directory):
            if not isinstance(document, dict):
                continue
            entry = str(document.get("name") or path.stem)
            page = _page_url(kind, path.stem, entry)
            links = _model_links(document)
            for section in ("pathophysiology", "phenotypes"):
                for item in document.get(section) or []:
                    if not isinstance(item, dict) or not item.get("name"):
                        continue
                    name = str(item["name"])
                    go = tuple(_terms(item.get("biological_processes")))
                    cells = tuple(_terms(item.get("cell_types")))
                    blob = " ".join((name, *go, *cells, path.stem))
                    linked = links.get(name, [])
                    for endpoint in ENDPOINTS:
                        if not endpoint.pattern.search(name):
                            continue
                        if endpoint.ambiguous and not NEURAL.search(blob):
                            continue
                        if endpoint.term == "Learning and memory" and IMMUNE.search(name):
                            continue
                        found[endpoint.term].append(
                            Node(
                                entry=entry,
                                kind=kind,
                                section=section,
                                node=name,
                                url=f"{page}#{_make_anchor_id(_anchor(kind, section), name)}",
                                go=go,
                                cells=cells,
                                scale=str(item.get("biological_scale") or ""),
                                models=tuple(m["summary"] for m in linked),
                                readouts=tuple(
                                    r for m in linked for r in m["readouts"]
                                ),
                            )
                        )
    for term in found:
        # Modules first, then model-linked, then alphabetical: the head of each
        # list is what a summary row shows as the endpoint's representative node.
        found[term].sort(key=lambda n: (n.kind != "module", not n.models, n.entry, n.node))
    return found


def _model_kinds(nodes: Iterable[Node]) -> str:
    counts: Counter[str] = Counter()
    for node in nodes:
        for summary in node.models:
            counts[summary.split(":")[0]] += 1
    return ", ".join(f"{k} ×{n}" for k, n in counts.most_common()) or "none"


def render_markdown(found: dict[str, list[Node]], top: int) -> str:
    lines: list[str] = []
    w = lines.append
    w("| Endpoint | Battery | Assay substrate | Nodes | Model-linked | Entries | Representative node |")
    w("|---|---|---|---:|---:|---:|---|")
    for endpoint in ENDPOINTS:
        nodes = found[endpoint.term]
        linked = sum(1 for n in nodes if n.models)
        entries = len({n.entry for n in nodes})
        rep = f"[{nodes[0].entry} > {nodes[0].node}]({nodes[0].url})" if nodes else "—"
        w(
            f"| {endpoint.term} | {endpoint.version} | {endpoint.substrate} "
            f"| {len(nodes)} | {linked} | {entries} | {rep} |"
        )
    w("")
    w(f"**Totals.** {sum(len(v) for v in found.values())} matched node rows, "
      f"{len({n.url for v in found.values() for n in v})} distinct links, "
      f"{len({n.entry for v in found.values() for n in v})} distinct entries.")
    for endpoint in ENDPOINTS:
        nodes = found[endpoint.term]
        w("")
        w(f"### {endpoint.term}")
        w("")
        w(f"{len(nodes)} nodes across {len({n.entry for n in nodes})} entries; "
          f"{sum(1 for n in nodes if n.models)} carry a model link ({_model_kinds(nodes)}).")
        if nodes:
            w("")
            for node in nodes[:top]:
                badge = " *(module)*" if node.kind == "module" else ""
                models = f" — {'; '.join(node.models)}" if node.models else ""
                w(f"- [{node.entry} > {node.node}]({node.url}){badge}{models}")
            if len(nodes) > top:
                w(f"- …and {len(nodes) - top} more "
                  f"(`just dnt-ivb-coverage --format tsv --table nodes`)")
    return "\n".join(lines) + "\n"


def render_tsv(found: dict[str, list[Node]], table: str) -> str:
    rows: list[str] = []
    if table == "summary":
        rows.append("endpoint\tbattery\tsubstrate\tnodes\tmodel_linked\tentries\tmodules\trepresentative\turl")
        for endpoint in ENDPOINTS:
            nodes = found[endpoint.term]
            rows.append("\t".join((
                endpoint.term, endpoint.version, endpoint.substrate,
                str(len(nodes)), str(sum(1 for n in nodes if n.models)),
                str(len({n.entry for n in nodes})),
                str(sum(1 for n in nodes if n.kind == "module")),
                f"{nodes[0].entry} > {nodes[0].node}" if nodes else "",
                nodes[0].url if nodes else "",
            )))
    else:
        rows.append("endpoint\tentry\tentry_kind\tsection\tnode\turl\tgo_terms\tcell_types"
                    "\tbiological_scale\tmodels\treadouts")
        for endpoint in ENDPOINTS:
            for n in found[endpoint.term]:
                rows.append("\t".join((
                    endpoint.term, n.entry, n.kind, n.section, n.node, n.url,
                    "; ".join(n.go), "; ".join(n.cells), n.scale,
                    " | ".join(n.models), "; ".join(n.readouts),
                )))
    return "\n".join(rows) + "\n"


def check_anchors(found: dict[str, list[Node]], pages: Path) -> int:
    """Every link must name a page that exists and a fragment that page carries."""
    seen: dict[str, tuple[str, str]] = {}
    for nodes in found.values():
        for node in nodes:
            base, _, anchor = node.url.partition("#")
            sub = "modules" if "/modules/" in base else "disorders"
            seen[node.url] = (f"{sub}/{base.rsplit('/', 1)[1]}", anchor)
    bad_page = bad_anchor = 0
    for url, (relative, anchor) in sorted(seen.items()):
        path = pages / relative
        if not path.is_file():
            bad_page += 1
            print(f"PAGE   {url}")
            continue
        if f'id="{anchor}"' not in path.read_text(encoding="utf-8"):
            bad_anchor += 1
            print(f"ANCHOR {url}")
    print(
        f"{len(seen)} distinct links | ok {len(seen) - bad_page - bad_anchor} "
        f"| page absent {bad_page} | fragment absent {bad_anchor}"
    )
    return 1 if (bad_page or bad_anchor) else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", help="write here instead of stdout")
    parser.add_argument("--format", choices=("markdown", "tsv"), default="markdown",
                        help="output format (default: markdown)")
    parser.add_argument("--table", choices=("summary", "nodes"), default="summary",
                        help="which table --format tsv writes (default: summary)")
    parser.add_argument("--json", action="store_true",
                        help="emit the headline figures as JSON")
    parser.add_argument("--top", type=int, default=12,
                        help="nodes listed per endpoint in markdown (default: 12)")
    parser.add_argument("--kb", type=Path, default=Path("kb"),
                        help="knowledge base directory (default: kb)")
    parser.add_argument("--check-anchors", type=Path, metavar="PAGES",
                        help="verify every link against a rendered pages/ tree")
    args = parser.parse_args(argv)

    # Each directory is walked once, so the shared parse cache is pure cost.
    kb_cache.default_off()

    if not (args.kb / "disorders").is_dir():
        print(f"no disorder entries under {args.kb}/ — run from the repository root",
              file=sys.stderr)
        return 2

    found = collect(args.kb)

    if args.check_anchors:
        return check_anchors(found, args.check_anchors)

    if args.json:
        payload = {
            e.term: {
                "battery": e.version,
                "substrate": e.substrate,
                "nodes": len(found[e.term]),
                "model_linked": sum(1 for n in found[e.term] if n.models),
                "entries": len({n.entry for n in found[e.term]}),
            }
            for e in ENDPOINTS
        }
        text = json.dumps(payload, indent=2) + "\n"
    elif args.format == "tsv":
        text = render_tsv(found, args.table)
    else:
        text = render_markdown(found, args.top)

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
