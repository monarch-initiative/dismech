"""Export the pathograph as an OWL TBox, using py-horned-owl.

Every pathograph node in ``kb/disorders/`` and ``kb/modules/`` becomes an OWL
**class** with its own IRI, and the candidate node-class tree in
``kb/node_classes/pathograph_node_classes.txt`` becomes the upper hierarchy the
pathophysiology nodes sit under. "Pathograph node" means what
:func:`dismech.graph.collect_graph_nodes` means -- pathophysiology, phenotype,
environmental, genetic (genes and variants), treatment, biochemical, and the
mechanism-linked experimental / animal / computational models -- and the edges
are :func:`dismech.graph.build_causal_graph`'s, so this export cannot drift from
the graph the pages draw.

Why classes and not individuals
-------------------------------
A curated node such as *Fanconi_Anemia: Genomic Instability* does not denote one
event; it denotes the kind of process that happens in every patient with the
disease. Modelling it as a class lets the node-class tree's logical definitions
classify it with an ordinary reasoner, lets ``conforms_to`` read as plain
subsumption (a disorder node is a specialisation of the module node it conforms
to), and keeps the ontology terms on its descriptors (GO, CL, UBERON, CHEBI,
HP ...) in the class position they already occupy in their own ontologies.

What is emitted
---------------
* **Node-class tree.** One class per tree class under ``dismech:PathophysiologyNode``,
  ``rdfs:label`` from the class name, ``skos:definition`` from the gloss, and
  the ``= expression`` line translated into a general class inclusion axiom
  ``<expression> SubClassOf <tree class>`` -- a *sufficient* condition, which
  is exactly what the tree's grammar says a definition is. ``some PREFIX``
  atoms (``locations some UBERON``) become a dismech placeholder class "any
  UBERON term", rather than a root CURIE written from memory.
* **Every node.** ``SubClassOf dismech:<Kind>Node`` (itself under
  ``dismech:PathographNode``), a label, the entry's MONDO term as
  ``dcterms:isPartOf``, and the description as ``skos:definition``.
* **Pathophysiology nodes** additionally get one existential per bound
  descriptor (``biological_processes some GO_0006281``, narrowed by
  ``modifier value DECREASED`` when the descriptor carries one),
  ``SubClassOf <module node>`` for ``conforms_to``, and ``SubClassOf <tree
  class>`` where the tree cites the node as a worked example.
* **Other kinds** relate to their bound term: a phenotype, exposure or treatment
  node is asserted a subclass of its HP / ECTO / NCIT term (a disease-specific
  seizure is a seizure); a genetic or biochemical node is not a gene or an
  analyte, so it gets ``gene_term some`` / ``biomarker_term some`` instead.
* **Edges.** Each graph edge becomes ``Source SubClassOf <predicate> some
  Target`` with a ``dismech:<predicate>`` object property (``causes``,
  ``leads_to``, ``treats``, ``targets``, ``triggers``, ``models``, ``readout`` ...).
* Optionally (``--scan``), the scanner's candidate tier assignment
  (:mod:`dismech.node_class_scan`) as an asserted ``SubClassOf``. Off by
  default: the scanner is a worklist, and its LOW-confidence rules are not
  claims anyone has reviewed.

Node IRIs are ``<base>node/<entry>/<kind>/<slug>`` where ``kind`` is the
graph node type (``pathophysiology``, ``phenotype``, ``treatment`` ...) and ``slug`` is the node name with runs of
non-alphanumerics folded to ``_``. A slug collision inside one entry gets a
``_2``/``_3`` suffix in file order, so IRIs are stable as long as the entry is.

The external ontologies are referenced, not imported. To let a reasoner use the
``some GO:...`` definitions over GO descendants, merge GO (or a GO slim) in
before reasoning, e.g. ``robot merge -i dismech-pathograph.owl -I <go.owl>``.

Usage::

    uv run python -m dismech.export.owl_tbox_export -o output/owl/dismech-pathograph.owl
    uv run python -m dismech.export.owl_tbox_export --scan --min-confidence MEDIUM -o out.owx
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pyhornedowl
import yaml
from pyhornedowl.model import (
    Annotation,
    AnnotationAssertion,
    DeclareAnnotationProperty,
    DeclareClass,
    DeclareNamedIndividual,
    DeclareObjectProperty,
    ObjectComplementOf,
    ObjectHasValue,
    ObjectIntersectionOf,
    ObjectSomeValuesFrom,
    ObjectUnionOf,
    SimpleLiteral,
    SubClassOf,
)

from dismech.graph import NODE_SECTIONS, animal_model_label, build_causal_graph, iter_variant_items
from dismech.node_class_definitions import DESCRIPTOR_SLOTS, SCHEMA_PATH, Atom, Definition
from dismech.node_class_scan import DEFAULT_SEED, classify_node, load_seed
from dismech.node_classes import ClassNode, iter_classes, parse_file

BASE = "https://w3id.org/monarch-initiative/dismech/"
ONTOLOGY_IRI = BASE + "pathograph-tbox.owl"
DEFAULT_TREE = Path("kb/node_classes/pathograph_node_classes.txt")
DEFAULT_KB_DIRS = (Path("kb/disorders"), Path("kb/modules"))

RDFS = "http://www.w3.org/2000/01/rdf-schema#"
SKOS = "http://www.w3.org/2004/02/skos/core#"
DCTERMS = "http://purl.org/dc/terms/"
OBO = "http://purl.obolibrary.org/obo/"

#: Scanner tier code -> top-level tree class id. The scanner and the tree name
#: the same tiers differently; this is the only place the two vocabularies meet.
SCAN_TIER_TO_TREE = {
    "GENOMIC": "GENOMIC_EFFECT",
    "ACTIVITY": "MOLECULAR_ACTIVITY_EFFECT",
    "SUBSTANCE": "MOLECULAR_SUBSTANCE_EFFECT",
    "PATHWAY": "PATHWAY_EFFECT",
    "CELLULAR": "CELLULAR_EFFECT",
    "TISSUE": "TISSUE_ORGAN_EFFECT",
    "SYSTEMIC": "SYSTEMIC_EFFECT",
    "OUTCOME": "OUTCOME",
}
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}

PATHO = "pathophysiology"
PHENO = "phenotype"

#: Endpoint resolution order for a bare-name edge target.
RESOLUTION_ORDER = (PATHO, PHENO) + tuple(
    k for _, k in NODE_SECTIONS if k not in (PATHO, PHENO)
) + ("animal_model",)

#: Per node kind: (slot, subsumes). ``subsumes`` means the node class is asserted
#: a subclass of the bound term; otherwise ``slot some term``.
KIND_TERM_SLOTS: dict[str, tuple[tuple[str, bool], ...]] = {
    PHENO: (("phenotype_term", True),),
    "environmental": (("exposure_term", True),),
    "treatment": (("treatment_term", True),),
    "genetic": (("gene_term", False),),
    "biochemical": (("biomarker_term", False),),
}


def slugify(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_") or "node"


def node_class_iri(class_id: str) -> str:
    return f"{BASE}node_class/{class_id}"


def load_prefixes(schema_path: Path = SCHEMA_PATH) -> dict[str, str]:
    """The schema's prefix map, plus the lowercase ``hgnc`` form the KB uses."""
    with Path(schema_path).open(encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)
    prefixes = {k: str(v) for k, v in (schema.get("prefixes") or {}).items()}
    if "HGNC" in prefixes:
        prefixes.setdefault("hgnc", prefixes["HGNC"])
    return prefixes


def load_modifier_meanings(schema_path: Path = SCHEMA_PATH) -> dict[str, str | None]:
    with Path(schema_path).open(encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)
    values = schema["enums"]["ModifierEnum"]["permissible_values"]
    return {str(k): (v or {}).get("meaning") for k, v in values.items()}


@dataclass
class NodeRecord:
    entry: str
    kind: str
    name: str
    iri: str
    data: dict[str, Any]


@dataclass
class ExportStats:
    counts: Counter = field(default_factory=Counter)
    unresolved_targets: list[tuple[str, str, str]] = field(default_factory=list)
    unresolved_examples: list[tuple[str, str]] = field(default_factory=list)
    unresolved_conforms_to: list[tuple[str, str, str]] = field(default_factory=list)


class TBoxBuilder:
    def __init__(self, prefixes: dict[str, str], modifier_meanings: dict[str, str | None]):
        self.prefixes = prefixes
        self.modifier_meanings = modifier_meanings
        self.stats = ExportStats()
        header = f"Prefix(dismech:=<{BASE}>)\nOntology(<{ONTOLOGY_IRI}>)\n"
        self.onto = pyhornedowl.open_ontology_from_string(header, "ofn")
        for pfx, ns in (
            ("dismech", BASE),
            ("dnc", BASE + "node_class/"),
            ("rdfs", RDFS),
            ("skos", SKOS),
            ("dcterms", DCTERMS),
            ("obo", OBO),
        ):
            self.onto.add_prefix_mapping(pfx, ns)
        for pfx in ("GO", "HP", "CL", "UBERON", "CHEBI", "MONDO", "ECTO", "PATO"):
            if pfx in prefixes:
                self.onto.add_prefix_mapping(pfx, prefixes[pfx])
        self._declared: set[str] = set()
        self._props: dict[str, Any] = {}
        self._aprops: dict[str, Any] = {}
        self.label = self._aprop(RDFS + "label")
        self.comment = self._aprop(RDFS + "comment")
        self.definition = self._aprop(SKOS + "definition")
        self.exact_match = self._aprop(SKOS + "exactMatch")
        self.is_part_of = self._aprop(DCTERMS + "isPartOf")
        self.source_entry = self._aprop(BASE + "source_entry")
        self.biological_scale = self._aprop(BASE + "biological_scale")
        self.node_name = self._aprop(BASE + "node_name")
        self.modifier = self._prop(BASE + "modifier", "modifier")
        self.graph_root = self._class(BASE + "PathographNode", "pathograph node")
        self.kind_root(PATHO)

    # --- primitives ------------------------------------------------------------

    def expand(self, curie: str) -> str:
        if curie.startswith(("http://", "https://")):
            return curie
        pfx, _, local = curie.partition(":")
        if pfx in self.prefixes:
            return self.prefixes[pfx] + local
        if pfx.upper() in self.prefixes:
            return self.prefixes[pfx.upper()] + local
        return f"{OBO}{pfx}_{local}"

    def _annotate(self, iri: str, prop: Any, value: str, *, as_iri: bool = False) -> None:
        val = self.onto.iri(value) if as_iri else SimpleLiteral(value)
        self.onto.add_axiom(AnnotationAssertion(self.onto.iri(iri), Annotation(prop, val)))

    def _aprop(self, iri: str) -> Any:
        if iri not in self._aprops:
            ap = self.onto.annotation_property(iri)
            if not iri.startswith((RDFS, SKOS, DCTERMS)):
                self.onto.add_axiom(DeclareAnnotationProperty(ap))
            self._aprops[iri] = ap
        return self._aprops[iri]

    def _prop(self, iri: str, label: str | None = None) -> Any:
        if iri not in self._props:
            op = self.onto.object_property(iri)
            self.onto.add_axiom(DeclareObjectProperty(op))
            if label:
                self._annotate(iri, self.label, label)
            self._props[iri] = op
        return self._props[iri]

    def _class(self, iri: str, label: str | None = None) -> Any:
        cls = self.onto.class_(iri)
        if iri not in self._declared:
            self.onto.add_axiom(DeclareClass(cls))
            self._declared.add(iri)
            if label:
                self._annotate(iri, self.label, label)
        return cls

    def term_class(self, curie: str, label: str | None = None) -> Any:
        return self._class(self.expand(curie), label)

    def slot_prop(self, slot: str) -> Any:
        return self._prop(BASE + slot, slot)

    def modifier_individual(self, value: str) -> Any:
        iri = f"{BASE}ModifierEnum/{value}"
        ind = self.onto.named_individual(iri)
        if iri not in self._declared:
            self.onto.add_axiom(DeclareNamedIndividual(ind))
            self._declared.add(iri)
            self._annotate(iri, self.label, value)
            meaning = self.modifier_meanings.get(value)
            if meaning:
                self._annotate(iri, self.exact_match, self.expand(meaning), as_iri=True)
        return ind

    def any_term_class(self, prefix: str) -> Any:
        """Placeholder for ``some PREFIX``: any term drawn from that ontology."""
        return self._class(f"{BASE}AnyTerm/{prefix.upper()}", f"any {prefix.upper()} term")

    def filler(self, term: str | Any, modifiers: Iterable[str]) -> Any:
        base = term if not isinstance(term, str) else self.term_class(term)
        mods = [ObjectHasValue(self.modifier, self.modifier_individual(m)) for m in modifiers]
        if not mods:
            return base
        mod_expr = mods[0] if len(mods) == 1 else ObjectUnionOf(mods)
        return ObjectIntersectionOf([base, mod_expr])

    # --- node-class tree ---------------------------------------------------------

    def atom_expr(self, atom: Atom) -> Any:
        term = self.any_term_class(atom.term) if atom.is_prefix else self.term_class(atom.term, atom.label)
        expr = ObjectSomeValuesFrom(self.slot_prop(atom.slot), self.filler(term, atom.modifiers))
        return ObjectComplementOf(expr) if atom.negated else expr

    def definition_expr(self, defn: Definition) -> Any:
        conjs = []
        for conj in defn.disjuncts:
            parts = [self.atom_expr(a) for a in conj]
            conjs.append(parts[0] if len(parts) == 1 else ObjectIntersectionOf(parts))
        return conjs[0] if len(conjs) == 1 else ObjectUnionOf(conjs)

    def add_tree(self, roots: list[ClassNode]) -> dict[str, ClassNode]:
        by_id: dict[str, ClassNode] = {}

        def visit(node: ClassNode, parent_iri: str, path: tuple[str, ...]) -> None:
            # Sibling names are unique but descendants of different parents may
            # share one, so the IRI is the id path, not the bare id.
            cid = "__".join((*path, node.id))
            iri = node_class_iri(cid)
            cls = self._class(iri, node.name)
            self.onto.add_axiom(SubClassOf(cls, self.onto.class_(parent_iri)))
            if node.gloss:
                self._annotate(iri, self.definition, node.gloss)
            for key, values in node.attributes.items():
                for v in values:
                    self._annotate(iri, self.comment, f"{key}: {v}")
            if node.definition:
                self._annotate(iri, self.comment, f"logical definition: {node.definition}")
                self.onto.add_axiom(SubClassOf(self.definition_expr(node.parsed_definition), cls))
                self.stats.counts["tree_definitions"] += 1
            by_id.setdefault(node.id, node)
            self._tree_iris[id(node)] = iri
            self.stats.counts["tree_classes"] += 1
            for child in node.children:
                visit(child, iri, (*path, node.id))

        self._tree_iris: dict[int, str] = {}
        for root in roots:
            visit(root, BASE + "PathophysiologyNode", ())
        return by_id

    # --- KB nodes -------------------------------------------------------------------

    def kind_root(self, kind: str) -> Any:
        """``dismech:<Kind>Node`` under ``dismech:PathographNode``."""
        camel = "".join(part.capitalize() for part in kind.split("_"))
        iri = f"{BASE}{camel}Node"
        if iri not in self._declared:
            cls = self._class(iri, f"{kind.replace('_', ' ')} node")
            self.onto.add_axiom(SubClassOf(cls, self.graph_root))
        return self.onto.class_(iri)

    def collect_nodes(self, kb_dirs: Iterable[Path]) -> dict[tuple[str, str, str], NodeRecord]:
        """One record per pathograph node, keyed ``(entry, kind, name)``.

        The node set is :func:`dismech.graph.collect_graph_nodes`'s: the
        :data:`~dismech.graph.NODE_SECTIONS`, mechanism-linked animal models and
        genetic variants. Unlike the graph, which keys nodes by bare name and so
        collapses a pathophysiology node and a phenotype that share a name, each
        section item here keeps its own IRI.
        """
        from dismech.yaml_io import safe_load

        records: dict[tuple[str, str, str], NodeRecord] = {}
        self._entries: dict[str, dict[str, Any]] = {}
        for kb_dir in kb_dirs:
            for path in sorted(Path(kb_dir).glob("*.yaml")):
                try:
                    data = safe_load(path.read_text(encoding="utf-8")) or {}
                except Exception:
                    self.stats.counts["unparsable_files"] += 1
                    continue
                entry = path.stem
                self._entries[entry] = data
                used: Counter = Counter()

                def add(kind: str, name: Any, item: dict[str, Any]) -> None:
                    name = str(name)
                    key = (entry, kind, name)
                    if key in records:
                        return
                    slug = slugify(name)
                    used[(kind, slug)] += 1
                    if used[(kind, slug)] > 1:
                        slug = f"{slug}_{used[(kind, slug)]}"
                    records[key] = NodeRecord(entry, kind, name, f"{BASE}node/{entry}/{kind}/{slug}", item)

                for section, kind in NODE_SECTIONS:
                    for item in data.get(section) or []:
                        if isinstance(item, dict) and item.get("name"):
                            add(kind, item["name"], item)
                for item in data.get("animal_models") or []:
                    label = animal_model_label(item) if isinstance(item, dict) else None
                    if label:
                        add("animal_model", label, item)
                for _parent, variant in iter_variant_items(data):
                    if variant.get("name"):
                        add("genetic", variant["name"], variant)
        return records

    def resolve(self, records: dict, entry: str, name: str, prefer: str | None = None) -> NodeRecord | None:
        """Resolve a bare-name edge endpoint, as :mod:`dismech.graph` does.

        ``prefer`` (the edge's source section) wins; otherwise pathophysiology,
        then phenotype, then the remaining kinds in graph order.
        """
        for kind in ([prefer] if prefer else []) + list(RESOLUTION_ORDER):
            rec = records.get((entry, kind, name))
            if rec is not None:
                return rec
        return None

    def add_node(self, rec: NodeRecord, records: dict) -> None:
        item = rec.data
        cls = self._class(rec.iri, f"{rec.name} ({rec.entry})")
        self.onto.add_axiom(SubClassOf(cls, self.kind_root(rec.kind)))
        self._annotate(rec.iri, self.node_name, rec.name)
        self._annotate(rec.iri, self.source_entry, rec.entry)
        disease = (self._entries.get(rec.entry) or {}).get("disease_term") or {}
        disease_id = (disease.get("term") or {}).get("id")
        if disease_id:
            self._annotate(rec.iri, self.is_part_of, self.expand(disease_id), as_iri=True)
        if item.get("description"):
            self._annotate(rec.iri, self.definition, " ".join(str(item["description"]).split()))

        if rec.kind == PATHO:
            if item.get("biological_scale"):
                self._annotate(rec.iri, self.biological_scale, str(item["biological_scale"]))
            for slot in sorted(DESCRIPTOR_SLOTS):
                for desc in item.get(slot) or []:
                    self._add_descriptor(cls, slot, desc)
            self._add_conforms_to(rec, cls, records)

        # The node *is* a kind of its bound term where the term names the same
        # kind of thing (a disease-specific seizure is a seizure); elsewhere the
        # term is related by its slot (a genetic node is not a gene).
        for slot, subsumes in KIND_TERM_SLOTS.get(rec.kind, ()):
            values = item.get(slot)
            for desc in values if isinstance(values, list) else [values]:
                term = (desc or {}).get("term") if isinstance(desc, dict) else None
                if not (term and term.get("id")):
                    continue
                tcls = self.term_class(str(term["id"]), term.get("label"))
                if subsumes:
                    self.onto.add_axiom(SubClassOf(cls, tcls))
                else:
                    self.onto.add_axiom(SubClassOf(cls, ObjectSomeValuesFrom(self.slot_prop(slot), tcls)))
                self.stats.counts["term_axioms"] += 1

    def _add_descriptor(self, cls: Any, slot: str, desc: Any) -> None:
        if not isinstance(desc, dict):
            return
        term = desc.get("term") or {}
        if not term.get("id"):
            return
        mods = [desc["modifier"]] if desc.get("modifier") in self.modifier_meanings else []
        filler = self.filler(self.term_class(str(term["id"]), term.get("label")), mods)
        self.onto.add_axiom(SubClassOf(cls, ObjectSomeValuesFrom(self.slot_prop(slot), filler)))
        self.stats.counts["descriptor_axioms"] += 1

    def add_edges(self, records: dict) -> None:
        """Every :func:`dismech.graph.build_causal_graph` edge, as ``S SubClassOf p some T``."""
        for entry, data in self._entries.items():
            for edge in build_causal_graph(data).edges:
                src = self.resolve(records, entry, str(edge.source), edge.source_type)
                tgt = self.resolve(records, entry, str(edge.target))
                if src is None or tgt is None:
                    self.stats.unresolved_targets.append((entry, str(edge.source), str(edge.target)))
                    continue
                prop = self._prop(BASE + slugify(edge.predicate), edge.predicate.replace("_", " "))
                self.onto.add_axiom(SubClassOf(self.onto.class_(src.iri),
                                               ObjectSomeValuesFrom(prop, self.onto.class_(tgt.iri))))
                self.stats.counts[f"edge_axioms_{edge.predicate}"] += 1

    def _add_conforms_to(self, rec: NodeRecord, cls: Any, records: dict) -> None:
        ref = rec.data.get("conforms_to")
        refs = ref if isinstance(ref, list) else [ref]
        for r in refs:
            if not isinstance(r, str) or "#" not in r:
                continue
            module, _, node = r.strip().partition("#")
            tgt = records.get((module, PATHO, node))
            if tgt is None:
                self.stats.unresolved_conforms_to.append((rec.entry, rec.name, r))
                continue
            self.onto.add_axiom(SubClassOf(cls, self.onto.class_(tgt.iri)))
            self.stats.counts["conforms_to_axioms"] += 1

    def add_examples(self, roots: list[ClassNode], records: dict) -> None:
        for _path, cnode in iter_classes(roots):
            iri = self._tree_iris[id(cnode)]
            for ex in cnode.examples:
                rec = records.get((ex.disease, PATHO, ex.node))
                if rec is None:
                    self.stats.unresolved_examples.append((ex.disease, ex.node))
                    continue
                self.onto.add_axiom(SubClassOf(self.onto.class_(rec.iri), self.onto.class_(iri)))
                self.stats.counts["example_axioms"] += 1

    def add_scan(self, roots: list[ClassNode], records: dict, seed_path: Path, min_conf: str) -> None:
        seed = load_seed(seed_path)
        top = {r.id: self._tree_iris[id(r)] for r in roots}
        floor = CONFIDENCE_RANK[min_conf]
        for rec in records.values():
            if rec.kind != PATHO:
                continue
            a = classify_node(rec.data, seed)
            tree_id = SCAN_TIER_TO_TREE.get(a.node_class or "")
            if not tree_id or tree_id not in top or CONFIDENCE_RANK.get(a.confidence, -1) < floor:
                continue
            self.onto.add_axiom(SubClassOf(self.onto.class_(rec.iri), self.onto.class_(top[tree_id])))
            self.stats.counts[f"scan_axioms_{a.confidence}"] += 1


def build(
    tree_path: Path = DEFAULT_TREE,
    kb_dirs: Iterable[Path] = DEFAULT_KB_DIRS,
    *,
    scan: bool = False,
    seed_path: Path = DEFAULT_SEED,
    min_confidence: str = "HIGH",
) -> TBoxBuilder:
    builder = TBoxBuilder(load_prefixes(), load_modifier_meanings())
    roots = parse_file(tree_path)
    builder.add_tree(roots)
    records = builder.collect_nodes(kb_dirs)
    for rec in records.values():
        builder.add_node(rec, records)
        builder.stats.counts[f"nodes_{rec.kind}"] += 1
    builder.add_edges(records)
    builder.add_examples(roots, records)
    if scan:
        builder.add_scan(roots, records, seed_path, min_confidence)
    return builder


def main(argv: list[str] | None = None) -> int:
    from dismech import kb_cache

    kb_cache.default_off()  # one walk of the corpus; the cache would be pure cost
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("-o", "--output", type=Path, default=Path("output/owl/dismech-pathograph.owl"),
                    help="output file; serialization from extension (.owl/.rdf = RDF/XML, .owx = OWL/XML)")
    ap.add_argument("--tree", type=Path, default=DEFAULT_TREE)
    ap.add_argument("--kb-dir", type=Path, action="append", dest="kb_dirs",
                    help="KB directory to read (repeatable; default kb/disorders and kb/modules)")
    ap.add_argument("--scan", action="store_true",
                    help="also assert the node-class scanner's candidate tier as SubClassOf")
    ap.add_argument("--min-confidence", choices=list(CONFIDENCE_RANK), default="HIGH",
                    help="lowest scanner confidence to assert with --scan (default HIGH)")
    ap.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    args = ap.parse_args(argv)
    suffix = args.output.suffix.lower()
    if suffix == ".ofn":
        # horned-owl 1.4's functional-syntax writer panics on a literal holding
        # a double quote followed by a multi-byte character (its quote() slices
        # by byte offset), and KB descriptions contain exactly that.
        ap.error("functional syntax (.ofn) is not supported: horned-owl's OFN writer "
                 "fails on KB text; use .owl (RDF/XML) or .owx (OWL/XML)")

    builder = build(args.tree, args.kb_dirs or DEFAULT_KB_DIRS, scan=args.scan,
                    seed_path=args.seed, min_confidence=args.min_confidence)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    serialization = {".owl": "rdf", ".rdf": "rdf", ".owx": "owx"}.get(suffix, "rdf")
    builder.onto.save_to_file(str(args.output), serialization)

    s = builder.stats
    for key in sorted(s.counts):
        print(f"{key}: {s.counts[key]}", file=sys.stderr)
    print(f"unresolved causal targets: {len(s.unresolved_targets)}", file=sys.stderr)
    print(f"unresolved tree examples: {len(s.unresolved_examples)}", file=sys.stderr)
    print(f"unresolved conforms_to: {len(s.unresolved_conforms_to)}", file=sys.stderr)
    print(f"wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
