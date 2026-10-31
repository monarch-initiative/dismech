"""Check that a grouping's member genes carry its GO activity in GO itself.

A grouping criterion such as ``HAS_MOLECULAR_FUNCTION GO:0005216`` (ion channel
activity) checks the GO terms an entry *curates* on its pathophysiology nodes.
It cannot tell whether the genes the entry names as causal are annotated with
that activity in the GO Consortium's own annotations: an entry can curate a
channel activity for a gene that GO has never called a channel, or the reverse.
This report asks the second question.

For every grouping that has at least one ``HAS_MOLECULAR_FUNCTION`` criterion,
it collects the criterion's GO roots, then for each disease member:

1. takes the member's causal genes: ``genetic[]`` records bound to an HGNC
   term whose ``relationship_type`` is ``CAUSATIVE`` or unset;
2. maps each gene to its UniProt accession through
   ``kb/genes/ingest/hgnc.tsv`` (falling back to the UniProt REST API for a
   gene the ingest table does not hold);
3. asks QuickGO for that protein's molecular-function annotations under any
   root, following ``is_a`` and ``part_of``;
4. reads the gene's ai-gene-review core molecular-function terms from the
   pinned ``kb/genes/ingest/ai_gene_review_core_function_terms.tsv`` and tests
   them against the roots through QuickGO's ontology ancestors.

A gene's verdict is the strongest class of support it has
(``NOT`` annotations are reported, never counted):

  EXPERIMENTAL   a GO annotation coded EXP, IDA, IPI, IMP, IGI, IEP or a
                 high-throughput code
  PHYLOGENETIC   a GO annotation coded IBA, IBD, IKR or IRD
  CURATED        a GO annotation coded TAS, NAS, IC or a sequence-similarity
                 code (ISS, ISO ...)
  GENE_REVIEW    an ai-gene-review core function under a root
  ELECTRONIC     a GO annotation coded IEA, and nothing stronger
  NONE           none of the above

The gene review counts as support because it is this project's own curation
of the gene's function. It is AI-generated and lives in a separate repository,
so it ranks below every curated GO evidence class. Where it states an activity
GO's annotations lack, the review is the answer, so the report lists those
genes separately rather than treating them as gaps. The ingest table is a snapshot (see
``kb/genes/ingest/sources.json``), so a review newer than the pin is not seen
until the ingest is refreshed (``just genes-ingest-refresh --repin`` then
``just genes-ingest-build``).

A ``member_type: SUBTYPE`` row names its parent entry, so the parent's genes
would rate it by its siblings' genes. A subtype is instead checked against the
genes its own row names in ``differentiating_mechanisms[].gene``, and reported
as ``SUBTYPE_UNSCOPED`` (no lookup) when the row names none, including a
subtype reached through a nested grouping.

A member is ``SUPPORTED`` when at least one causal gene has a verdict above
NONE (``GENE_REVIEW`` included), ``UNSUPPORTED`` when every causal gene is NONE, and ``NO_CAUSAL_GENE``
when the entry binds no causal HGNC gene at all. For a NO_CAUSAL_GENE member
the genes it does bind (``DISPUTED``, ``SUSCEPTIBILITY`` ...) are still looked
up and listed with their relationship type, because a grouping member whose
only gene is disputed is itself worth a look.

An UNSUPPORTED member is a lead, not a defect, and it can mean three different
things: the gene is not what the criterion says (the member does not belong),
the gene has no ai-gene-review review yet (or one newer than the ingest pin),
or the activity belongs to a different gene in a multi-gene entry. Read the
entry before changing anything.

Usage:
    uv run python scripts/grouping_gene_go_audit.py
    uv run python scripts/grouping_gene_go_audit.py --grouping Channelopathies
    uv run python scripts/grouping_gene_go_audit.py --format tsv
    uv run python scripts/grouping_gene_go_audit.py --strict

Needs network (EBI QuickGO, and UniProt for genes missing from the ingest
table). It is a report, not a gate: ``--strict`` exits 1 only when a member is
UNSUPPORTED.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

from dismech import kb_cache
from dismech.groupings import iter_disease_targets, iter_nodes, load_groupings_by_name

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPINGS_DIR = os.path.join(ROOT, "kb", "groupings")
DISORDERS_DIR = os.path.join(ROOT, "kb", "disorders")
HGNC_INGEST = os.path.join(ROOT, "kb", "genes", "ingest", "hgnc.tsv")
AIGR_CORE_TERMS = os.path.join(ROOT, "kb", "genes", "ingest", "ai_gene_review_core_function_terms.tsv")

QUICKGO_SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
QUICKGO_ANCESTORS = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/ancestors"
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
CAUSAL_RELATIONSHIPS = {None, "CAUSATIVE"}

EVIDENCE_CLASSES = {
    "EXPERIMENTAL": {
        "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
        "HTP", "HDA", "HMP", "HGI", "HEP",
    },
    "PHYLOGENETIC": {"IBA", "IBD", "IKR", "IRD"},
    "CURATED": {"TAS", "NAS", "IC", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA"},
    "ELECTRONIC": {"IEA"},
}
# Strongest first; NONE is the floor.
VERDICT_ORDER = ["EXPERIMENTAL", "PHYLOGENETIC", "CURATED", "GENE_REVIEW", "ELECTRONIC", "NONE"]


def evidence_class(code: str) -> str:
    for name, codes in EVIDENCE_CLASSES.items():
        if code in codes:
            return name
    # An unrecognised code is still a curator's statement; rank it with the
    # curated codes rather than dropping the annotation.
    return "CURATED"


@dataclass
class Annotation:
    go_id: str
    evidence: str
    negated: bool


@dataclass
class GeneVerdict:
    hgnc: str
    symbol: str
    uniprot: str | None
    relationship: str | None = None
    annotations: list[Annotation] = field(default_factory=list)
    lookup_failed: bool = False
    # ai-gene-review core MF terms that fall under a root (GENE_REVIEW support).
    review_terms: list[str] = field(default_factory=list)

    @property
    def causal(self) -> bool:
        return self.relationship in CAUSAL_RELATIONSHIPS

    @property
    def positive(self) -> list[Annotation]:
        return [a for a in self.annotations if not a.negated]

    @property
    def negated(self) -> list[Annotation]:
        return [a for a in self.annotations if a.negated]

    @property
    def verdict(self) -> str:
        classes = {evidence_class(a.evidence) for a in self.positive}
        if self.review_terms:
            # Keyed on the HGNC id, so it stands even when the GO lookup cannot.
            classes.add("GENE_REVIEW")
        for name in VERDICT_ORDER[:-1]:
            if name in classes:
                return name
        if self.lookup_failed:
            return "LOOKUP_FAILED"
        if self.uniprot is None:
            return "NO_UNIPROT"
        return "NONE"

    @property
    def go_supported(self) -> bool:
        """Whether GO's own annotations, not the gene review, support the gene."""
        return bool(self.positive)

    @property
    def go_ids(self) -> list[str]:
        return sorted({a.go_id for a in self.positive})


@dataclass
class MemberVerdict:
    disease: str
    via: str | None
    genes: list[GeneVerdict] = field(default_factory=list)
    # display_name of a SUBTYPE row; None for a whole-entry member.
    subtype: str | None = None
    unscoped: bool = False

    @property
    def label(self) -> str:
        return f"{self.disease} [subtype: {self.subtype}]" if self.subtype else self.disease

    @property
    def causal_genes(self) -> list[GeneVerdict]:
        return [g for g in self.genes if g.causal]

    @property
    def verdict(self) -> str:
        if self.unscoped:
            return "SUBTYPE_UNSCOPED"
        if not self.causal_genes:
            return "NO_CAUSAL_GENE"
        verdicts = {g.verdict for g in self.causal_genes}
        if verdicts & set(VERDICT_ORDER[:-1]):
            return "SUPPORTED"
        if verdicts & {"LOOKUP_FAILED", "NO_UNIPROT"}:
            return "UNRESOLVED"
        return "UNSUPPORTED"


@dataclass
class GroupingVerdict:
    grouping: str
    roots: list[str]
    members: list[MemberVerdict] = field(default_factory=list)
    review_lookup_failed: bool = False

    def by_verdict(self, verdict: str) -> list[MemberVerdict]:
        return [m for m in self.members if m.verdict == verdict]


def molecular_function_roots(grouping: dict) -> list[str]:
    """GO ids named by every HAS_MOLECULAR_FUNCTION leaf, in file order."""
    roots: list[str] = []
    for crit in grouping.get("membership_criteria") or []:
        for node in iter_nodes((crit or {}).get("logic") or {}):
            if node.get("criterion_predicate") != "HAS_MOLECULAR_FUNCTION":
                continue
            for desc in node.get("molecular_functions") or []:
                tid = ((desc or {}).get("term") or {}).get("id")
                if isinstance(tid, str) and tid.startswith("GO:") and tid not in roots:
                    roots.append(tid)
    return roots


def entry_genes(data: dict) -> list[tuple[str, str, str | None]]:
    """``(hgnc_id, symbol, relationship_type)`` for each HGNC-bound genetic record.

    A gene bound by several records keeps the first causal relationship it has,
    so a gene that is causal in one record and a modifier in another counts as
    causal.
    """
    out: dict[str, tuple[str, str, str | None]] = {}
    for rec in data.get("genetic") or []:
        if not isinstance(rec, dict):
            continue
        term = ((rec.get("gene_term") or {}).get("term")) or {}
        tid = term.get("id")
        if not (isinstance(tid, str) and tid.lower().startswith("hgnc:")):
            continue
        hgnc = "hgnc:" + tid.split(":", 1)[1]
        rel = rec.get("relationship_type")
        prior = out.get(hgnc)
        if prior is None or (prior[2] not in CAUSAL_RELATIONSHIPS and rel in CAUSAL_RELATIONSHIPS):
            out[hgnc] = (hgnc, str(term.get("label") or rec.get("name") or hgnc), rel)
    return list(out.values())


def disorder_index() -> dict[str, dict]:
    index: dict[str, dict] = {}
    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        data = kb_cache.load_document(path)
        if isinstance(data, dict) and data.get("name"):
            index[str(data["name"])] = data
    return index


def hgnc_uniprot_index(path: str = HGNC_INGEST) -> dict[str, str]:
    """Map lowercase ``hgnc:`` id -> first UniProt accession from the ingest table."""
    index: dict[str, str] = {}
    if not os.path.exists(path):
        return index
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            accs = [a for a in (row.get("uniprot_ids") or "").split("|") if a]
            if accs:
                index[row["hgnc_id"].lower()] = accs[0]
    return index


def review_mf_terms(path: str = AIGR_CORE_TERMS) -> dict[str, list[str]]:
    """Map lowercase ``hgnc:`` id -> ai-gene-review core molecular-function GO ids."""
    index: dict[str, list[str]] = {}
    if not os.path.exists(path):
        return index
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("relation") != "molecular_function":
                continue
            tid = row.get("term_id") or ""
            if tid.startswith("GO:"):
                index.setdefault(row["hgnc_id"].lower(), [])
                if tid not in index[row["hgnc_id"].lower()]:
                    index[row["hgnc_id"].lower()].append(tid)
    return index


def terms_under_roots(
    terms: list[str], roots: list[str], *, pause: float, batch: int = 50
) -> set[str] | None:
    """The subset of ``terms`` equal to or below a root (is_a/part_of), or None on failure."""
    root_set = set(roots)
    hits = {t for t in terms if t in root_set}
    pending = sorted(set(terms) - hits)
    for start in range(0, len(pending), batch):
        chunk = pending[start:start + batch]
        url = QUICKGO_ANCESTORS.format(ids=",".join(chunk)) + "?" + urllib.parse.urlencode(
            {"relations": "is_a,part_of"}
        )
        try:
            payload = _get_json(url)
        except (urllib.error.URLError, TimeoutError, ValueError):
            return None
        for row in payload.get("results") or []:
            if root_set & set(row.get("ancestors") or []):
                hits.add(str(row.get("id")))
        if pause:
            time.sleep(pause)
    return hits


def _get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def uniprot_for_hgnc(hgnc: str, *, pause: float) -> tuple[str | None, bool]:
    """Reviewed human UniProt accession cross-referenced to an HGNC id.

    Returns ``(accession, failed)``: a lookup that errors is ``(None, True)``,
    so the gene is reported as LOOKUP_FAILED rather than as having no entry.
    """
    query = f"xref:hgnc-{hgnc.split(':', 1)[1]} AND organism_id:9606 AND reviewed:true"
    url = f"{UNIPROT_SEARCH}?" + urllib.parse.urlencode(
        {"query": query, "fields": "accession", "format": "json", "size": 1}
    )
    try:
        results = _get_json(url).get("results") or []
    except (urllib.error.URLError, TimeoutError, ValueError):
        print(f"WARNING: UniProt lookup failed for {hgnc}", file=sys.stderr)
        return None, True
    finally:
        if pause:
            time.sleep(pause)
    return (results[0]["primaryAccession"] if results else None), False


def subtype_rows(grouping: dict) -> list[dict]:
    """Direct ``member_type: SUBTYPE`` rows, each kept separately."""
    return [
        m for m in grouping.get("members") or []
        if isinstance(m, dict) and m.get("member") and m.get("member_type") == "SUBTYPE"
    ]


def subtype_scope(row: dict) -> list[tuple[str, str]]:
    """``(hgnc_id, symbol)`` named by a SUBTYPE row's differentiating mechanisms."""
    out: list[tuple[str, str]] = []
    for mech in row.get("differentiating_mechanisms") or []:
        term = (((mech or {}).get("gene") or {}).get("term")) or {}
        tid = term.get("id")
        if isinstance(tid, str) and tid.lower().startswith("hgnc:"):
            hgnc = "hgnc:" + tid.split(":", 1)[1]
            if hgnc not in {h for h, _ in out}:
                out.append((hgnc, str(term.get("label") or hgnc)))
    return out


def fetch_annotations(
    accessions: list[str], roots: list[str], *, pause: float, batch: int = 20
) -> dict[str, list[Annotation]] | None:
    """MF annotations under ``roots`` for each accession, or None on failure.

    Fetches positive and NOT annotations alike; the caller separates them.
    """
    out: dict[str, list[Annotation]] = {acc: [] for acc in accessions}
    for start in range(0, len(accessions), batch):
        chunk = accessions[start:start + batch]
        page = 1
        while True:
            params = {
                "geneProductId": ",".join(f"UniProtKB:{a}" for a in chunk),
                "goId": ",".join(roots),
                "goUsage": "descendants",
                "goUsageRelationships": "is_a,part_of",
                "aspect": "molecular_function",
                "limit": 200,
                "page": page,
            }
            url = f"{QUICKGO_SEARCH}?" + urllib.parse.urlencode(params)
            try:
                payload = _get_json(url)
            except (urllib.error.URLError, TimeoutError, ValueError):
                return None
            for row in payload.get("results") or []:
                acc = str(row.get("geneProductId", "")).split(":", 1)[-1]
                if acc not in out:
                    continue
                qualifier = str(row.get("qualifier") or "")
                out[acc].append(
                    Annotation(
                        go_id=str(row.get("goId")),
                        evidence=str(row.get("goEvidence")),
                        negated=qualifier.startswith("NOT"),
                    )
                )
            total_pages = (payload.get("pageInfo") or {}).get("total") or 1
            if pause:
                time.sleep(pause)
            if page >= total_pages:
                break
            page += 1
    return out


def build_verdicts(only: str | None = None, *, pause: float = 0.2) -> list[GroupingVerdict]:
    groupings = load_groupings_by_name(sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))))
    diseases = disorder_index()
    uniprot_of = hgnc_uniprot_index()
    review_terms = review_mf_terms()
    out: list[GroupingVerdict] = []

    for name in sorted(groupings):
        if only and name != only:
            continue
        data = groupings[name]
        roots = molecular_function_roots(data)
        if not roots:
            continue
        gv = GroupingVerdict(name, roots)

        def add_gene(mv: MemberVerdict, hgnc: str, symbol: str, rel: str | None) -> None:
            acc, failed = uniprot_of.get(hgnc), False
            if acc is None:
                acc, failed = uniprot_for_hgnc(hgnc, pause=pause)
            mv.genes.append(GeneVerdict(hgnc, symbol, acc, rel, lookup_failed=failed))

        # Each SUBTYPE row is its own member, scoped to the genes it names;
        # iter_disease_targets would collapse it into the parent entry.
        for row in subtype_rows(data):
            mv = MemberVerdict(str(row["member"]), None,
                               subtype=str(row.get("display_name") or row["member"]))
            scope = subtype_scope(row)
            mv.unscoped = not scope
            for hgnc, symbol in scope:
                add_gene(mv, hgnc, symbol, None)
            gv.members.append(mv)

        direct_subtypes = {str(r["member"]) for r in subtype_rows(data)}
        for disease, mtype, via in iter_disease_targets(data, groupings):
            if mtype == "SUBTYPE":
                if via is None and disease in direct_subtypes:
                    continue
                gv.members.append(MemberVerdict(disease, via, subtype=disease, unscoped=True))
                continue
            mv = MemberVerdict(disease, via)
            genes = entry_genes(diseases.get(disease) or {})
            has_causal = any(rel in CAUSAL_RELATIONSHIPS for _h, _s, rel in genes)
            for hgnc, symbol, rel in genes:
                # Non-causal genes are only worth a lookup when they are all
                # the entry has; alongside a causal gene they are noise.
                if has_causal and rel not in CAUSAL_RELATIONSHIPS:
                    continue
                add_gene(mv, hgnc, symbol, rel)
            gv.members.append(mv)

        genes = [g for m in gv.members for g in m.genes if g.uniprot]
        accessions = sorted({g.uniprot for g in genes if g.uniprot})
        annotations = fetch_annotations(accessions, roots, pause=pause) if accessions else {}
        for g in genes:
            if annotations is None:
                g.lookup_failed = True
            else:
                g.annotations = list(annotations.get(g.uniprot or "", []))

        all_genes = [g for m in gv.members for g in m.genes]
        candidate_terms = sorted({t for g in all_genes for t in review_terms.get(g.hgnc, [])})
        under = terms_under_roots(candidate_terms, roots, pause=pause) if candidate_terms else set()
        if under is None:
            gv.review_lookup_failed = True
            # The review now carries verdicts, so a gene it might have supported
            # is unresolved, not unsupported, when the ancestor lookup fails.
            for g in all_genes:
                if review_terms.get(g.hgnc) and not g.go_supported:
                    g.lookup_failed = True
            print(
                f"WARNING: QuickGO ancestor lookup failed for {name}; ai-gene-review "
                "support could not be checked, so genes relying on it are reported "
                "as LOOKUP_FAILED and their members as UNRESOLVED.",
                file=sys.stderr,
            )
        for g in all_genes:
            g.review_terms = [t for t in review_terms.get(g.hgnc, []) if under and t in under]
        out.append(gv)
    return out


def _gene_line(g: GeneVerdict) -> str:
    terms = ", ".join(g.go_ids[:4]) + (" ..." if len(g.go_ids) > 4 else "")
    neg = f"  NOT: {', '.join(sorted({a.go_id for a in g.negated}))}" if g.negated else ""
    rel = "" if g.causal else f" [{g.relationship}]"
    review = f"  ai-gene-review core: {', '.join(g.review_terms)}" if g.review_terms else ""
    return (
        f"{g.symbol}{rel} ({g.uniprot or 'no UniProt'}) {g.verdict}"
        f"{'  ' + terms if terms else ''}{neg}{review}"
    )


def _print_summary(verdicts: list[GroupingVerdict]) -> None:
    for v in verdicts:
        print(f"\n=== {v.grouping}")
        print(f"    roots: {', '.join(v.roots)}")
        kinds = ("SUPPORTED", "UNSUPPORTED", "UNRESOLVED", "NO_CAUSAL_GENE", "SUBTYPE_UNSCOPED")
        counts = {k: len(v.by_verdict(k)) for k in kinds}
        print("    " + "  ".join(f"{k}={n}" for k, n in counts.items() if n or k != "SUBTYPE_UNSCOPED"))
        if v.review_lookup_failed:
            print("    NOTE: the ai-gene-review lookup failed; genes relying on it are LOOKUP_FAILED.")
        weakest = [
            m for m in v.by_verdict("SUPPORTED")
            if all(g.verdict in ("ELECTRONIC", "NONE", "NO_UNIPROT", "LOOKUP_FAILED") for g in m.causal_genes)
        ]
        for label, rows in (
            ("UNSUPPORTED (no causal gene supported by GO or its gene review)", v.by_verdict("UNSUPPORTED")),
            ("UNRESOLVED (lookup failed or no UniProt accession)", v.by_verdict("UNRESOLVED")),
            ("NO_CAUSAL_GENE (no causal HGNC gene; the genes it does bind are listed)",
             v.by_verdict("NO_CAUSAL_GENE")),
            ("SUPPORTED by electronic (IEA) annotation only", weakest),
            ("SUBTYPE_UNSCOPED (subtype row names no gene; not assessed)",
             v.by_verdict("SUBTYPE_UNSCOPED")),
        ):
            if not rows:
                continue
            print(f"\n    {label}:")
            for m in rows:
                via = f" (via {m.via})" if m.via else ""
                print(f"      {m.label}{via}")
                for g in m.genes:
                    print(f"        {_gene_line(g)}")
        mixed = [
            (m, g) for m in v.by_verdict("SUPPORTED") for g in m.genes if g.verdict == "NONE"
        ]
        if mixed:
            print("\n    Causal genes with no annotation under a root, in otherwise SUPPORTED members:")
            for m, g in mixed:
                print(f"      {m.label}: {g.symbol} ({g.uniprot})")
        review_only = [
            (m, g) for m in v.members for g in m.genes
            if g.review_terms and not g.go_supported
        ]
        if review_only:
            print("\n    Supported by the ai-gene-review core function, with no GO annotation under a root:")
            for m, g in review_only:
                print(f"      {g.symbol} ({g.uniprot or 'no UniProt'}) in {m.label}: {', '.join(g.review_terms)}")

    print("\n" + "-" * 72)
    print(
        "UNSUPPORTED is a lead, not a defect: the member may not belong, its gene\n"
        "may have no ai-gene-review review yet, or the activity may sit on another\n"
        "gene. Read the entry before changing anything."
    )


def _print_tsv(verdicts: list[GroupingVerdict]) -> None:
    print(
        "grouping\tmember\tvia\tmember_verdict\thgnc\tsymbol\trelationship_type\tuniprot\t"
        "gene_verdict\tgo_ids\tnot_go_ids\tai_gene_review_core_mf"
    )
    for v in verdicts:
        for m in v.members:
            rows = m.genes or [None]
            for g in rows:
                if g is None:
                    print(f"{v.grouping}\t{m.label}\t{m.via or ''}\t{m.verdict}" + "\t" * 8)
                    continue
                neg = ",".join(sorted({a.go_id for a in g.negated}))
                print(
                    f"{v.grouping}\t{m.label}\t{m.via or ''}\t{m.verdict}\t{g.hgnc}\t"
                    f"{g.symbol}\t{g.relationship or ''}\t{g.uniprot or ''}\t{g.verdict}\t"
                    f"{','.join(g.go_ids)}\t{neg}\t{','.join(g.review_terms)}"
                )


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", help="Only this grouping, by its `name`.")
    ap.add_argument("--format", choices=("summary", "tsv"), default="summary")
    ap.add_argument("--strict", action="store_true", help="Exit 1 if any member is UNSUPPORTED.")
    ap.add_argument("--pause", type=float, default=0.2, help="Seconds between requests (default 0.2).")
    args = ap.parse_args(argv)

    verdicts = build_verdicts(args.grouping, pause=args.pause)
    if not verdicts:
        target = f" matching {args.grouping!r}" if args.grouping else ""
        print(f"No grouping with a HAS_MOLECULAR_FUNCTION criterion{target}.")
        return 0

    if args.format == "tsv":
        _print_tsv(verdicts)
    else:
        _print_summary(verdicts)

    if any(v.by_verdict("UNRESOLVED") for v in verdicts):
        print(
            "\nWARNING: some members are UNRESOLVED (failed lookup or no UniProt "
            "accession); they are not counted as UNSUPPORTED.",
            file=sys.stderr,
        )
    if args.strict and any(v.by_verdict("UNSUPPORTED") for v in verdicts):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
