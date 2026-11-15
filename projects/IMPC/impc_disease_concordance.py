"""How much of a dismech disease does the IMPC knockout of its gene reproduce?

For every germline gene-disease pair in ``kb/disorders/`` this joins the human
gene to its mouse ortholog in IMPC and asks three questions:

1. **Coverage.** Was the mouse gene phenotyped, did it give any significant
   call, and in which zygosity (heterozygote calls are the directly relevant
   genotype for a dominant human disease)?
2. **System concordance.** Of the organ systems the entry's HPO phenotypes
   touch, how many does the IMPC knockout also hit? Systems are compared
   through the hand-curated ``hp_mp_system_map.yaml``. Observed recall is set
   against the recall of random IMPC genes, because a gene with many calls
   overlaps almost any phenotype profile.
3. **Mechanism contact.** Does any IMPC call for the gene name, in its MP
   term's logical definition, a cell type (CL) or biological process (GO) that
   one of the entry's pathophysiology nodes also binds? GO matches count an
   IMPC process that is the node's term or one of its ancestors.

Inputs (git-ignored, see ``README.md``): ``.cache/impc/genotype_phenotype.tsv``,
``genes.tsv``, ``mp.owl``, ``go-basic.obo``, ``hp.obo``.

Outputs: ``projects/IMPC/results/pairs.tsv`` (one row per disease-gene pair),
``summary.yaml`` and ``CONCORDANCE.md``.

    uv run python projects/IMPC/impc_disease_concordance.py
"""

from __future__ import annotations

import random
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import yaml

from dismech import kb_cache

CACHE = Path(".cache/impc")
HERE = Path(__file__).parent
RESULTS = HERE / "results"
KB = Path("kb/disorders")

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
OWL = "{http://www.w3.org/2002/07/owl#}"
OBO = "http://purl.obolibrary.org/obo/"
HAS_MODIFIER = OBO + "RO_0002573"

GERMLINE_TYPES = {"CAUSATIVE", "SUSCEPTIBILITY", "RISK_FACTOR", "MODIFIER"}
LOF = {"LOSS_OF_FUNCTION", "PARTIAL_LOSS_OF_FUNCTION"}
NON_LOF = {"GAIN_OF_FUNCTION", "DOMINANT_NEGATIVE", "NEOMORPHIC", "HYPERMORPHIC"}
INHERITANCE = {
    "HP:0000006": "AD",
    "HP:0000007": "AR",
    "HP:0001417": "XL",
    "HP:0001419": "XL",
    "HP:0001423": "XL",
}
LETHAL_MP_PREFIX = ("preweaning lethality", "embryonic lethality", "prenatal lethality", "perinatal lethality")


# ---------------------------------------------------------------- ontologies
def curie(iri: str | None) -> str | None:
    if not iri or not iri.startswith(OBO):
        return None
    local = iri[len(OBO):]
    if "_" not in local:
        return None
    p, r = local.split("_", 1)
    return f"{p}:{r}"


def mp_bearers(path: Path) -> dict[str, set[str]]:
    """MP id -> CL/GO/UBERON bearers named in its equivalent-class axiom."""
    out: dict[str, set[str]] = {}
    depth = 0
    for event, el in ET.iterparse(path, events=("start", "end")):
        if event == "start":
            depth += 1
            continue
        depth -= 1
        if depth != 1 or el.tag != OWL + "Class":
            continue
        cid = curie(el.get(RDF + "about"))
        if cid and cid.startswith("MP:"):
            found = set()
            for eq in el.findall(OWL + "equivalentClass"):
                for r in eq.iter(OWL + "Restriction"):
                    prop = r.find(OWL + "onProperty")
                    if prop is not None and prop.get(RDF + "resource") == HAS_MODIFIER:
                        continue
                    for node in r.iter():
                        c = curie(node.get(RDF + "resource")) or curie(node.get(RDF + "about"))
                        if c and c.split(":")[0] in {"CL", "GO", "UBERON"}:
                            found.add(c)
            if found:
                out[cid] = found
        el.clear()
    return out


def obo_ancestors(path: Path, prefix: str, rels: tuple[str, ...] = ("part_of",)) -> dict[str, set[str]]:
    parents: dict[str, set[str]] = defaultdict(set)
    cur = None
    n = len(prefix) + 8  # e.g. "GO:" + 7 digits
    for line in path.read_text().splitlines():
        if line == "[Term]" or line == "[Typedef]":
            cur = None
        elif line.startswith(f"id: {prefix}:"):
            cur = line[4:]
        elif cur and line.startswith("is_a: "):
            parents[cur].add(line[6:6 + n])
        elif cur and line.startswith("relationship: "):
            rel, tgt = line[14:].split(" ", 1)
            if rel in rels:
                parents[cur].add(tgt[:n])
    memo: dict[str, set[str]] = {}

    def anc(t: str) -> set[str]:
        if t not in memo:
            memo[t] = set()
            s = set()
            for p in parents.get(t, ()):
                s.add(p)
                s |= anc(p)
            memo[t] = s
        return memo[t]

    return {t: anc(t) for t in list(parents)}


# ---------------------------------------------------------------- dismech
def term_id(desc: dict | None) -> str | None:
    if not isinstance(desc, dict):
        return None
    t = desc.get("term")
    return t.get("id") if isinstance(t, dict) else None


def term_label(desc: dict | None) -> str | None:
    if not isinstance(desc, dict):
        return None
    t = desc.get("term")
    return t.get("label") if isinstance(t, dict) else None


def disease_records() -> list[dict]:
    recs = []
    for path in sorted(KB.glob("*.yaml")):
        d = kb_cache.load_document(path)
        if not isinstance(d, dict):
            continue
        hp = {term_id(p.get("phenotype_term")) for p in d.get("phenotypes") or []}
        hp.discard(None)
        inh = {
            INHERITANCE.get(term_id(i.get("inheritance_term")))
            for i in d.get("inheritance") or []
        }
        inh.discard(None)
        nodes = d.get("pathophysiology") or []
        node_cl = {term_id(c) for n in nodes for c in n.get("cell_types") or []}
        node_go = {term_id(b) for n in nodes for b in n.get("biological_processes") or []}
        node_cl.discard(None)
        node_go.discard(None)
        impact_by_gene: dict[str, set[str]] = defaultdict(set)
        for n in nodes:
            fic = (n.get("genetic_context") or {}).get("functional_impact_category")
            if not fic:
                continue
            for g in n.get("genes") or []:
                lab = term_label(g)
                if lab:
                    impact_by_gene[lab].add(fic)
        for g in d.get("genetic") or []:
            rt = g.get("relationship_type")
            if rt not in GERMLINE_TYPES or g.get("variant_origin") == "SOMATIC":
                continue
            sym = term_label(g.get("gene_term"))
            if not sym or not str(term_id(g.get("gene_term")) or "").lower().startswith("hgnc:"):
                continue
            recs.append(
                {
                    "disease": path.stem,
                    "gene": sym,
                    "relationship_type": rt,
                    "inheritance": "|".join(sorted(inh)),
                    "impact": "|".join(sorted(impact_by_gene.get(sym, ()))),
                    "hp": hp,
                    "node_cl": node_cl,
                    "node_go": node_go,
                }
            )
    return recs


# ---------------------------------------------------------------- main
def main() -> None:
    kb_cache.default_off()
    RESULTS.mkdir(parents=True, exist_ok=True)
    smap = yaml.safe_load((HERE / "hp_mp_system_map.yaml").read_text())["systems"]
    hp_system_to_mp = {s["hp_id"]: set(s.get("mp_top_levels") or []) for s in smap}

    hp_anc = obo_ancestors(CACHE / "hp.obo", "HP", rels=())
    go_anc = obo_ancestors(CACHE / "go-basic.obo", "GO")
    bearers = mp_bearers(CACHE / "mp.owl")

    gp = pd.read_csv(CACHE / "genotype_phenotype.tsv", sep="\t", dtype=str)
    genes = pd.read_csv(CACHE / "genes.tsv", sep="\t", dtype=str)

    human_to_mouse: dict[str, set[str]] = defaultdict(set)
    phenotyped: set[str] = set()
    for _, r in genes.iterrows():
        if str(r.phenotyping_data_available) == "True":
            phenotyped.add(r.mgi_accession_id)
        for h in str(r.human_gene_symbol or "").split("|"):
            if h and h != "nan":
                human_to_mouse[h].add(r.mgi_accession_id)

    calls_by_gene: dict[str, pd.DataFrame] = {k: v for k, v in gp.groupby("marker_accession_id")}
    mouse_systems: dict[str, set[str]] = {}
    for g, df in calls_by_gene.items():
        s = set()
        for v in df.top_level_mp_term_name.dropna():
            s |= set(v.split("|"))
        mouse_systems[g] = s
    genes_with_calls = sorted(calls_by_gene)

    def human_systems(hp: set[str]) -> set[str]:
        out = set()
        for h in hp:
            anc = hp_anc.get(h, set()) | {h}
            out |= {s for s in hp_system_to_mp if s in anc}
        return out

    def recall(hsys: set[str], msys: set[str]) -> float | None:
        mappable = {s for s in hsys if hp_system_to_mp[s]}
        if not mappable:
            return None
        hit = {s for s in mappable if hp_system_to_mp[s] & msys}
        return len(hit) / len(mappable)

    rng = random.Random(0)
    background = rng.sample(genes_with_calls, 300)

    rows = []
    for rec in disease_records():
        mice = human_to_mouse.get(rec["gene"], set())
        mgi = sorted(mice)
        tested = bool(mice & phenotyped)
        with_call = [m for m in mgi if m in calls_by_gene]
        calls = pd.concat([calls_by_gene[m] for m in with_call]) if with_call else gp.iloc[0:0]
        msys = set().union(*(mouse_systems[m] for m in with_call)) if with_call else set()
        hsys = human_systems(rec["hp"])
        obs = recall(hsys, msys) if with_call else None
        exp = None
        if with_call and obs is not None:
            vals = [recall(hsys, mouse_systems[b]) for b in background]
            exp = sum(vals) / len(vals)
        impc_bearers = set()
        for mp in calls.mp_term_id.dropna().unique():
            impc_bearers |= bearers.get(mp, set())
        cl_hit = sorted(rec["node_cl"] & {b for b in impc_bearers if b.startswith("CL:")})
        go_impc = {b for b in impc_bearers if b.startswith("GO:")}
        go_hit = sorted(
            {g for g in rec["node_go"] if go_impc & (go_anc.get(g, set()) | {g})}
        )
        lethal = any(
            str(n).startswith(LETHAL_MP_PREFIX) for n in calls.mp_term_name.dropna().unique()
        )
        rows.append(
            {
                "disease": rec["disease"],
                "gene": rec["gene"],
                "relationship_type": rec["relationship_type"],
                "inheritance": rec["inheritance"],
                "impact": rec["impact"],
                "mouse_genes": "|".join(mgi),
                "impc_tested": tested,
                "impc_significant": bool(with_call),
                "n_calls": int(len(calls)),
                "het_calls": int((calls.zygosity == "heterozygote").sum()),
                "lethal": lethal,
                "human_systems": "|".join(sorted(hsys)),
                "mouse_systems": "|".join(sorted(msys)),
                "system_recall": obs,
                "background_recall": exp,
                "node_cl_matched": "|".join(cl_hit),
                "node_go_matched": "|".join(go_hit),
            }
        )
    pairs = pd.DataFrame(rows)
    pairs.to_csv(RESULTS / "pairs.tsv", sep="\t", index=False)
    summarise(pairs)


def impact_class(s: str) -> str:
    vals = set(filter(None, str(s).split("|")))
    if not vals:
        return "NOT_RECORDED"
    if vals <= LOF:
        return "LOSS_OF_FUNCTION"
    if vals & NON_LOF and not vals & LOF:
        return "NON_LOSS_OF_FUNCTION"
    if vals & NON_LOF:
        return "MIXED"
    return "UNKNOWN"


def summarise(pairs: pd.DataFrame) -> None:
    pairs = pairs.copy()
    pairs["impact_class"] = pairs.impact.map(impact_class)
    pairs["mapped"] = pairs.mouse_genes.fillna("") != ""
    caus = pairs[pairs.relationship_type == "CAUSATIVE"]
    cplx = pairs[pairs.relationship_type != "CAUSATIVE"]

    def block(df: pd.DataFrame) -> dict:
        sig = df[df.impc_significant]
        rec = sig.dropna(subset=["system_recall"])
        mech = sig[(sig.node_cl_matched.fillna("") != "") | (sig.node_go_matched.fillna("") != "")]
        return {
            "pairs": int(len(df)),
            "diseases": int(df.disease.nunique()),
            "genes": int(df.gene.nunique()),
            "mouse_ortholog_in_impc": int(df.mapped.sum()),
            "impc_phenotyped": int(df.impc_tested.sum()),
            "impc_significant_call": int(df.impc_significant.sum()),
            "impc_lethal_call": int(df.lethal.sum()),
            "pairs_with_recall": int(len(rec)),
            "mean_system_recall": round(float(rec.system_recall.mean()), 3) if len(rec) else None,
            "mean_background_recall": round(float(rec.background_recall.mean()), 3) if len(rec) else None,
            "pairs_recall_above_background": int((rec.system_recall > rec.background_recall).sum()),
            "pairs_with_mechanism_contact": int(len(mech)),
            "pairs_with_cl_contact": int((sig.node_cl_matched.fillna("") != "").sum()),
            "pairs_with_go_contact": int((sig.node_go_matched.fillna("") != "").sum()),
        }

    out = {"causative": block(caus), "susceptibility_risk_modifier": block(cplx)}
    out["causative_by_inheritance"] = {}
    for inh in ["AD", "AR", "XL"]:
        df = caus[caus.inheritance.str.contains(inh, na=False)]
        sig = df[df.impc_significant]
        out["causative_by_inheritance"][inh] = {
            "pairs": int(len(df)),
            "impc_significant_call": int(len(sig)),
            "with_heterozygote_call": int((sig.het_calls > 0).sum()),
            "lethal": int(sig.lethal.sum()),
            "mean_system_recall": round(float(sig.system_recall.dropna().mean()), 3) if len(sig) else None,
        }
    out["causative_by_impact"] = {}
    for ic, df in caus.groupby("impact_class"):
        sig = df[df.impc_significant].dropna(subset=["system_recall"])
        out["causative_by_impact"][ic] = {
            "pairs": int(len(df)),
            "impc_significant_call": int(df.impc_significant.sum()),
            "mean_system_recall": round(float(sig.system_recall.mean()), 3) if len(sig) else None,
            "mean_background_recall": round(float(sig.background_recall.mean()), 3) if len(sig) else None,
        }
    cl = Counter(t for v in caus.node_cl_matched.dropna() for t in v.split("|") if t)
    go = Counter(t for v in caus.node_go_matched.dropna() for t in v.split("|") if t)
    out["top_cl_contacts"] = dict(cl.most_common(15))
    out["top_go_contacts"] = dict(go.most_common(15))
    (RESULTS / "summary.yaml").write_text(yaml.safe_dump(out, sort_keys=False))
    write_report(out)
    print(yaml.safe_dump(out, sort_keys=False))


def write_report(out: dict) -> None:
    def pct(a, b):
        return f"{a:,} ({100 * a / b:.0f}%)" if b else str(a)

    lines = [
        "# IMPC knockouts against dismech diseases (generated)",
        "",
        "Generated by `impc_disease_concordance.py`; do not edit by hand.",
        "",
        "## Coverage and concordance",
        "",
        "| | Causative (Mendelian) | Susceptibility / risk / modifier |",
        "|---|---:|---:|",
    ]
    a, b = out["causative"], out["susceptibility_risk_modifier"]
    keys = [
        ("Gene-disease pairs", "pairs", None),
        ("Mouse ortholog in IMPC gene table", "mouse_ortholog_in_impc", "pairs"),
        ("Phenotyped by IMPC", "impc_phenotyped", "pairs"),
        ("At least one significant call", "impc_significant_call", "pairs"),
        ("A lethality call", "impc_lethal_call", "impc_significant_call"),
        ("Mechanism contact (CL or GO shared with a node)", "pairs_with_mechanism_contact", "impc_significant_call"),
        ("...through a cell type", "pairs_with_cl_contact", "impc_significant_call"),
        ("...through a process", "pairs_with_go_contact", "impc_significant_call"),
    ]
    for label, k, denom in keys:
        fa = pct(a[k], a[denom]) if denom else f"{a[k]:,}"
        fb = pct(b[k], b[denom]) if denom else f"{b[k]:,}"
        lines.append(f"| {label} | {fa} | {fb} |")
    lines += [
        f"| Mean organ-system recall (pairs with a call) | {a['mean_system_recall']} | {b['mean_system_recall']} |",
        f"| Mean recall of random IMPC genes | {a['mean_background_recall']} | {b['mean_background_recall']} |",
        f"| Pairs above their random baseline | {pct(a['pairs_recall_above_background'], a['pairs_with_recall'])} | "
        f"{pct(b['pairs_recall_above_background'], b['pairs_with_recall'])} |",
        "",
        "## Causative pairs by mode of inheritance",
        "",
        "| Inheritance | Pairs | With a call | With a heterozygote call | Lethal | Mean recall |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for inh, v in out["causative_by_inheritance"].items():
        lines.append(
            f"| {inh} | {v['pairs']:,} | {v['impc_significant_call']:,} | "
            f"{pct(v['with_heterozygote_call'], v['impc_significant_call'])} | "
            f"{pct(v['lethal'], v['impc_significant_call'])} | {v['mean_system_recall']} |"
        )
    lines += [
        "",
        "## Causative pairs by recorded functional impact",
        "",
        "Impact is read from `genetic_context.functional_impact_category` on pathophysiology nodes that carry the gene.",
        "",
        "| Impact | Pairs | With a call | Mean recall | Random baseline |",
        "|---|---:|---:|---:|---:|",
    ]
    for ic, v in out["causative_by_impact"].items():
        lines.append(
            f"| {ic} | {v['pairs']:,} | {v['impc_significant_call']:,} | {v['mean_system_recall']} | {v['mean_background_recall']} |"
        )
    lines += ["", "## Most frequent mechanism contacts (causative pairs)", ""]
    lines.append("Cell types: " + ", ".join(f"{k} ({v})" for k, v in out["top_cl_contacts"].items()))
    lines.append("")
    lines.append("Processes: " + ", ".join(f"{k} ({v})" for k, v in out["top_go_contacts"].items()))
    lines.append("")
    (RESULTS / "CONCORDANCE.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
