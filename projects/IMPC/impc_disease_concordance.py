"""How much of a dismech disease does the IMPC knockout of its gene reproduce?

For every germline gene-disease pair in ``kb/disorders/`` this joins the human
gene to its mouse ortholog and compares the entry with the IMPC release pinned
in ``data/impc/MANIFEST.yaml`` (the same reports the ``IMPC:`` reference source
is built from). Four questions:

1. **Coverage.** Was the mouse gene phenotyped, did it give a significant
   call, was it lethal, and was any heterozygote tested (the directly relevant
   genotype for a dominant human disease)?
2. **System concordance.** For each organ system the entry's HPO phenotypes
   touch, IMPC either hit it, tested it without a call, or never tested it
   (from ``procedureCompletenessAndPhenotypeHits``). Recall is computed over
   tested systems only, so an untested system is not counted as a miss.
   Systems are compared through ``hp_mp_system_map.yaml``.
3. **Phenotype concordance.** Each HPO and MP term is reduced to the
   anatomical entity, cell type or process its OWL logical definition says the
   abnormality inheres in. A human phenotype is matched when some IMPC call for
   the gene shares a bearer with it (CL compared through its ``is_a``
   hierarchy, UBERON and GO exactly).
4. **Mechanism contact.** An IMPC call names, through its MP definition, a cell
   type or process that one of the entry's pathophysiology nodes binds. CL
   matches in either ``is_a`` direction (a node on B cells meets a call on
   marginal zone B cells); GO matches when the IMPC process is the node's term
   or one of its ancestors.

Each observed recall is set against the mean recall of 300 random phenotyped
IMPC genes scored against the same entry, because a gene with many calls
overlaps almost any profile.

Inputs (git-ignored): ``data/impc/*.csv.gz`` (``just impc-refresh``) and
``.cache/impc/{genes.tsv,mp.owl,hp.owl,go-basic.obo,hp.obo,cl-basic.obo}``
(see ``projects/IMPC.md``).

Outputs: ``projects/IMPC/results/pairs.tsv``, ``summary.yaml`` and
``CONCORDANCE.md``.

    uv run python projects/IMPC/impc_disease_concordance.py
"""

from __future__ import annotations

import csv
import gzip
import random
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
import yaml

from dismech import kb_cache

CACHE = Path(".cache/impc")
RELEASE = Path("data/impc")
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
LETHAL = ("preweaning lethality", "embryonic lethality", "prenatal lethality", "perinatal lethality")
# CL terms too general to count as contact when a node or call sits on them.
CL_STOP = {
    "CL:0000000",  # cell
    "CL:0000003",  # native cell
    "CL:0000255",  # eukaryotic cell
    "CL:0000548",  # animal cell
    "CL:0002371",  # somatic cell
    "CL:0000988",  # hematopoietic cell
    "CL:0000738",  # leukocyte
    "CL:0000763",  # myeloid cell
    "CL:0000542",  # lymphocyte
}
N_BACKGROUND = 300


# ---------------------------------------------------------------- ontologies
def curie(iri: str | None) -> str | None:
    if not iri or not iri.startswith(OBO):
        return None
    local = iri[len(OBO):]
    if "_" not in local:
        return None
    p, r = local.split("_", 1)
    return f"{p}:{r}"


def owl_bearers(path: Path, prefix: str) -> dict[str, set[str]]:
    """``prefix`` term -> CL/GO/UBERON bearers named in its equivalent-class axiom."""
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
        if cid and cid.startswith(prefix + ":"):
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


def obo_ancestors(path: Path, prefix: str, rels: tuple[str, ...] = ()) -> dict[str, set[str]]:
    parents: dict[str, set[str]] = defaultdict(set)
    cur = None
    n = len(prefix) + 8
    for line in path.read_text().splitlines():
        if line in ("[Term]", "[Typedef]"):
            cur = None
        elif line.startswith(f"id: {prefix}:"):
            cur = line[4:]
        elif cur and line.startswith(f"is_a: {prefix}:"):
            parents[cur].add(line[6:6 + n])
        elif cur and line.startswith("relationship: "):
            rel, tgt = line[14:].split(" ", 1)
            if rel in rels and tgt.startswith(prefix + ":"):
                parents[cur].add(tgt[:n])
    memo: dict[str, set[str]] = {}

    def anc(t: str) -> set[str]:
        if t not in memo:
            memo[t] = set()
            s: set[str] = set()
            for p in parents.get(t, ()):
                s.add(p)
                s |= anc(p)
            memo[t] = s
        return memo[t]

    return {t: anc(t) for t in list(parents)}


# ---------------------------------------------------------------- dismech
def term_id(desc) -> str | None:
    if not isinstance(desc, dict):
        return None
    t = desc.get("term")
    return t.get("id") if isinstance(t, dict) else None


def term_label(desc) -> str | None:
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
        hp = {term_id(p.get("phenotype_term")) for p in d.get("phenotypes") or []} - {None}
        inh = {INHERITANCE.get(term_id(i.get("inheritance_term"))) for i in d.get("inheritance") or []} - {None}
        nodes = d.get("pathophysiology") or []
        node_cl = {term_id(c) for n in nodes for c in n.get("cell_types") or []} - {None}
        node_go = {term_id(b) for n in nodes for b in n.get("biological_processes") or []} - {None}
        impact_by_gene: dict[str, set[str]] = defaultdict(set)
        for n in nodes:
            fic = (n.get("genetic_context") or {}).get("functional_impact_category")
            if fic:
                for g in n.get("genes") or []:
                    if term_label(g):
                        impact_by_gene[term_label(g)].add(fic)
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


# ---------------------------------------------------------------- IMPC
def read_gz(path: Path):
    with gzip.open(path, "rt", newline="") as fh:
        yield from csv.DictReader(fh)


class Mouse:
    """Per-gene IMPC facts from the pinned release reports."""

    def __init__(self) -> None:
        self.calls: dict[str, list[dict]] = defaultdict(list)
        self.tested: dict[str, set[str]] = defaultdict(set)
        self.tested_het: dict[str, set[str]] = defaultdict(set)
        self.phenotyped: set[str] = set()
        for r in read_gz(RELEASE / "genotype-phenotype-assertions-ALL.csv.gz"):
            self.calls[r["marker_accession_id"]].append(r)
        for r in read_gz(RELEASE / "procedureCompletenessAndPhenotypeHits.csv.gz"):
            g = r["Gene Accession Id"]
            systems = {s for s in (r["Top-level MP Name: Successful"] or "").split("|") if s and s != "None"}
            if systems:
                self.phenotyped.add(g)
                self.tested[g] |= systems
                if r["Zygosity"] == "heterozygote":
                    self.tested_het[g] |= systems

    def systems(self, g: str, het_only: bool = False) -> set[str]:
        out: set[str] = set()
        for c in self.calls.get(g, ()):
            if het_only and c["zygosity"] != "heterozygote":
                continue
            out |= {s for s in (c["top_level_mp_term_name"] or "").split("|") if s}
        return out


def main() -> None:
    kb_cache.default_off()
    RESULTS.mkdir(parents=True, exist_ok=True)
    smap = yaml.safe_load((HERE / "hp_mp_system_map.yaml").read_text())["systems"]
    sys_to_mp = {s["hp_id"]: set(s.get("mp_top_levels") or []) for s in smap}

    hp_anc = obo_ancestors(CACHE / "hp.obo", "HP")
    go_anc = obo_ancestors(CACHE / "go-basic.obo", "GO", rels=("part_of",))
    cl_anc = obo_ancestors(CACHE / "cl-basic.obo", "CL")
    mp_b = owl_bearers(CACHE / "mp.owl", "MP")
    hp_b = owl_bearers(CACHE / "hp.owl", "HP")
    mouse = Mouse()

    genes = pd.read_csv(CACHE / "genes.tsv", sep="\t", dtype=str)
    human_to_mouse: dict[str, set[str]] = defaultdict(set)
    for _, r in genes.iterrows():
        for h in str(r.human_gene_symbol or "").split("|"):
            if h and h != "nan":
                human_to_mouse[h].add(r.mgi_accession_id)

    def cl_related(a: str, b: str) -> bool:
        if a in CL_STOP or b in CL_STOP:
            return False
        return a == b or a in cl_anc.get(b, ()) or b in cl_anc.get(a, ())

    def bearer_match(hb: set[str], mb: set[str]) -> bool:
        for h in hb:
            for m in mb:
                if h == m:
                    return True
                if h.startswith("CL:") and m.startswith("CL:") and cl_related(h, m):
                    return True
        return False

    gene_bearers: dict[str, list[set[str]]] = {}

    def bearers_of(g: str) -> list[set[str]]:
        if g not in gene_bearers:
            mps = {c["mp_term_id"] for c in mouse.calls.get(g, ())}
            gene_bearers[g] = [mp_b[m] for m in mps if m in mp_b]
        return gene_bearers[g]

    def human_systems(hp: set[str]) -> set[str]:
        out = set()
        for h in hp:
            a = hp_anc.get(h, set()) | {h}
            out |= {s for s in sys_to_mp if s in a and sys_to_mp[s]}
        return out

    def system_status(hsys: set[str], hit: set[str], tested: set[str]) -> dict[str, str]:
        st = {}
        for s in hsys:
            if sys_to_mp[s] & hit:
                st[s] = "HIT"
            elif sys_to_mp[s] & tested:
                st[s] = "TESTED_NO_CALL"
            else:
                st[s] = "UNTESTED"
        return st

    def tested_recall(st: dict[str, str]) -> float | None:
        t = [v for v in st.values() if v != "UNTESTED"]
        return (sum(v == "HIT" for v in t) / len(t)) if t else None

    def pheno_recall(hp: set[str], g: str) -> float | None:
        hps = [hp_b[h] for h in hp if h in hp_b]
        if not hps:
            return None
        mb = bearers_of(g)
        return sum(any(bearer_match(h, m) for m in mb) for h in hps) / len(hps)

    rng = random.Random(0)
    background = rng.sample(sorted(mouse.phenotyped), N_BACKGROUND)

    rows = []
    for rec in disease_records():
        mgi = sorted(human_to_mouse.get(rec["gene"], set()))
        tested_genes = [m for m in mgi if m in mouse.phenotyped]
        call_genes = [m for m in mgi if m in mouse.calls]
        calls = [c for m in call_genes for c in mouse.calls[m]]
        hit = set().union(*(mouse.systems(m) for m in mgi)) if mgi else set()
        hit_het = set().union(*(mouse.systems(m, het_only=True) for m in mgi)) if mgi else set()
        tested = set().union(*(mouse.tested[m] for m in tested_genes)) if tested_genes else set()
        tested_het = set().union(*(mouse.tested_het[m] for m in tested_genes)) if tested_genes else set()
        hsys = human_systems(rec["hp"])
        st = system_status(hsys, hit, tested)
        st_het = system_status(hsys, hit_het, tested_het)
        obs = exp = pobs = pexp = None
        if tested_genes:
            obs = tested_recall(st)
            pobs = max(
                (v for v in (pheno_recall(rec["hp"], m) for m in tested_genes) if v is not None),
                default=None,
            )
            if obs is not None:
                vals = [tested_recall(system_status(hsys, mouse.systems(b), mouse.tested[b])) for b in background]
                vals = [v for v in vals if v is not None]
                exp = sum(vals) / len(vals) if vals else None
            if pobs is not None:
                vals = [pheno_recall(rec["hp"], b) for b in background]
                vals = [v for v in vals if v is not None]
                pexp = sum(vals) / len(vals) if vals else None
        impc_b = set().union(*(b for m in call_genes for b in bearers_of(m))) if call_genes else set()
        cl_hit = sorted(
            {n for n in rec["node_cl"] if any(cl_related(n, b) for b in impc_b if b.startswith("CL:"))}
        )
        go_impc = {b for b in impc_b if b.startswith("GO:")}
        go_hit = sorted({g for g in rec["node_go"] if go_impc & (go_anc.get(g, set()) | {g})})
        rows.append(
            {
                "disease": rec["disease"],
                "gene": rec["gene"],
                "relationship_type": rec["relationship_type"],
                "inheritance": rec["inheritance"],
                "impact": rec["impact"],
                "mouse_genes": "|".join(mgi),
                "impc_reference": "|".join(f"IMPC:{m}" for m in call_genes or tested_genes),
                "impc_tested": bool(tested_genes),
                "impc_significant": bool(calls),
                "n_calls": len(calls),
                "het_tested": bool(tested_het),
                "het_calls": sum(c["zygosity"] == "heterozygote" for c in calls),
                "lethal": any(str(c["mp_term_name"]).startswith(LETHAL) for c in calls),
                "systems_hit": sum(v == "HIT" for v in st.values()),
                "systems_tested_no_call": sum(v == "TESTED_NO_CALL" for v in st.values()),
                "systems_untested": sum(v == "UNTESTED" for v in st.values()),
                "system_status": "|".join(f"{k}={v}" for k, v in sorted(st.items())),
                "system_recall": obs,
                "background_recall": exp,
                "het_system_recall": tested_recall(st_het) if tested_het else None,
                "phenotype_recall": pobs,
                "background_phenotype_recall": pexp,
                "node_cl_matched": "|".join(cl_hit),
                "node_go_matched": "|".join(go_hit),
            }
        )
    pairs = pd.DataFrame(rows)
    pairs.to_csv(RESULTS / "pairs.tsv", sep="\t", index=False)
    summarise(pairs)


def impact_class(s: str) -> str:
    vals = set(filter(None, str(s).split("|"))) - {"nan"}
    if not vals:
        return "NOT_RECORDED"
    if vals <= LOF:
        return "LOSS_OF_FUNCTION"
    if vals & NON_LOF and not vals & LOF:
        return "NON_LOSS_OF_FUNCTION"
    if vals & NON_LOF:
        return "MIXED"
    return "UNKNOWN"


def _mean(s: pd.Series):
    s = s.dropna()
    return round(float(s.mean()), 3) if len(s) else None


def block(df: pd.DataFrame) -> dict:
    tested = df[df.impc_tested]
    sig = df[df.impc_significant]
    rec = tested.dropna(subset=["system_recall", "background_recall"])
    prec = tested.dropna(subset=["phenotype_recall", "background_phenotype_recall"])
    mech = sig[(sig.node_cl_matched.fillna("") != "") | (sig.node_go_matched.fillna("") != "")]
    sys_total = tested[["systems_hit", "systems_tested_no_call", "systems_untested"]].sum()
    return {
        "pairs": int(len(df)),
        "diseases": int(df.disease.nunique()),
        "genes": int(df.gene.nunique()),
        "mouse_ortholog": int((df.mouse_genes.fillna("") != "").sum()),
        "impc_phenotyped": int(len(tested)),
        "impc_significant_call": int(len(sig)),
        "impc_lethal_call": int(sig.lethal.sum()),
        "human_systems_hit": int(sys_total.systems_hit),
        "human_systems_tested_no_call": int(sys_total.systems_tested_no_call),
        "human_systems_untested": int(sys_total.systems_untested),
        "pairs_with_system_recall": int(len(rec)),
        "mean_system_recall": _mean(rec.system_recall),
        "mean_background_recall": _mean(rec.background_recall),
        "pairs_above_background": int((rec.system_recall > rec.background_recall).sum()),
        "pairs_with_phenotype_recall": int(len(prec)),
        "mean_phenotype_recall": _mean(prec.phenotype_recall),
        "mean_background_phenotype_recall": _mean(prec.background_phenotype_recall),
        "pairs_phenotype_above_background": int(
            (prec.phenotype_recall > prec.background_phenotype_recall).sum()
        ),
        "het_tested": int(tested.het_tested.sum()),
        "mean_het_system_recall": _mean(tested.het_system_recall),
        "pairs_with_mechanism_contact": int(len(mech)),
        "pairs_with_cl_contact": int((sig.node_cl_matched.fillna("") != "").sum()),
        "pairs_with_go_contact": int((sig.node_go_matched.fillna("") != "").sum()),
    }


def summarise(pairs: pd.DataFrame) -> None:
    pairs = pairs.copy()
    pairs["impact_class"] = pairs.impact.map(impact_class)
    caus = pairs[pairs.relationship_type == "CAUSATIVE"]
    cplx = pairs[pairs.relationship_type != "CAUSATIVE"]
    out = {
        "impc_release": yaml.safe_load(Path("data/impc/MANIFEST.yaml").read_text())["data_release"],
        "causative": block(caus),
        "susceptibility_risk_modifier": block(cplx),
        "causative_by_inheritance": {},
        "causative_by_impact": {},
    }
    for inh in ["AD", "AR", "XL"]:
        out["causative_by_inheritance"][inh] = block(caus[caus.inheritance.str.contains(inh, na=False)])
    for ic, df in caus.groupby("impact_class"):
        out["causative_by_impact"][ic] = block(df)
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

    a, b = out["causative"], out["susceptibility_risk_modifier"]
    lines = [
        "# IMPC knockouts against dismech diseases (generated)",
        "",
        f"Generated by `impc_disease_concordance.py` against IMPC release {out['impc_release']}; do not edit by hand.",
        "",
        "## Coverage, concordance and mechanism contact",
        "",
        "| | Causative (Mendelian) | Susceptibility / risk / modifier |",
        "|---|---:|---:|",
        f"| Gene-disease pairs | {a['pairs']:,} | {b['pairs']:,} |",
        f"| Mouse ortholog in IMPC gene table | {pct(a['mouse_ortholog'], a['pairs'])} | {pct(b['mouse_ortholog'], b['pairs'])} |",
        f"| Phenotyped by IMPC | {pct(a['impc_phenotyped'], a['pairs'])} | {pct(b['impc_phenotyped'], b['pairs'])} |",
        f"| At least one significant call | {pct(a['impc_significant_call'], a['pairs'])} | {pct(b['impc_significant_call'], b['pairs'])} |",
        f"| ...including a lethality call | {pct(a['impc_lethal_call'], a['impc_significant_call'])} | {pct(b['impc_lethal_call'], b['impc_significant_call'])} |",
        f"| Heterozygotes tested | {pct(a['het_tested'], a['impc_phenotyped'])} | {pct(b['het_tested'], b['impc_phenotyped'])} |",
    ]
    for label, key in [
        ("Human systems hit", "human_systems_hit"),
        ("Human systems tested, no call", "human_systems_tested_no_call"),
        ("Human systems never tested", "human_systems_untested"),
    ]:
        ta = a["human_systems_hit"] + a["human_systems_tested_no_call"] + a["human_systems_untested"]
        tb = b["human_systems_hit"] + b["human_systems_tested_no_call"] + b["human_systems_untested"]
        lines.append(f"| {label} (phenotyped pairs) | {pct(a[key], ta)} | {pct(b[key], tb)} |")
    lines += [
        f"| Mean system recall over tested systems | {a['mean_system_recall']} | {b['mean_system_recall']} |",
        f"| ...random phenotyped IMPC gene | {a['mean_background_recall']} | {b['mean_background_recall']} |",
        f"| Pairs above their random baseline | {pct(a['pairs_above_background'], a['pairs_with_system_recall'])} | {pct(b['pairs_above_background'], b['pairs_with_system_recall'])} |",
        f"| Mean phenotype recall (shared bearer) | {a['mean_phenotype_recall']} | {b['mean_phenotype_recall']} |",
        f"| ...random phenotyped IMPC gene | {a['mean_background_phenotype_recall']} | {b['mean_background_phenotype_recall']} |",
        f"| Pairs above their random baseline | {pct(a['pairs_phenotype_above_background'], a['pairs_with_phenotype_recall'])} | {pct(b['pairs_phenotype_above_background'], b['pairs_with_phenotype_recall'])} |",
        f"| Mean system recall, heterozygote calls only | {a['mean_het_system_recall']} | {b['mean_het_system_recall']} |",
        f"| Mechanism contact (CL or GO shared with a node) | {pct(a['pairs_with_mechanism_contact'], a['impc_significant_call'])} | {pct(b['pairs_with_mechanism_contact'], b['impc_significant_call'])} |",
        f"| ...through a cell type | {pct(a['pairs_with_cl_contact'], a['impc_significant_call'])} | {pct(b['pairs_with_cl_contact'], b['impc_significant_call'])} |",
        f"| ...through a process | {pct(a['pairs_with_go_contact'], a['impc_significant_call'])} | {pct(b['pairs_with_go_contact'], b['impc_significant_call'])} |",
        "",
        "## Causative pairs by mode of inheritance",
        "",
        "| Inheritance | Pairs | Phenotyped | With a call | Lethal | Hets tested | System recall | Baseline | Het-only recall | Phenotype recall | Baseline |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for inh, v in out["causative_by_inheritance"].items():
        lines.append(
            f"| {inh} | {v['pairs']:,} | {v['impc_phenotyped']:,} | {v['impc_significant_call']:,} | "
            f"{pct(v['impc_lethal_call'], v['impc_significant_call'])} | {pct(v['het_tested'], v['impc_phenotyped'])} | "
            f"{v['mean_system_recall']} | {v['mean_background_recall']} | {v['mean_het_system_recall']} | "
            f"{v['mean_phenotype_recall']} | {v['mean_background_phenotype_recall']} |"
        )
    lines += [
        "",
        "## Causative pairs by recorded functional impact",
        "",
        "| Impact | Pairs | Phenotyped | System recall | Baseline | Phenotype recall | Baseline |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for ic, v in out["causative_by_impact"].items():
        lines.append(
            f"| {ic} | {v['pairs']:,} | {v['impc_phenotyped']:,} | {v['mean_system_recall']} | "
            f"{v['mean_background_recall']} | {v['mean_phenotype_recall']} | {v['mean_background_phenotype_recall']} |"
        )
    lines += ["", "## Most frequent mechanism contacts (causative pairs)", ""]
    lines.append("Cell types: " + ", ".join(f"{k} ({v})" for k, v in out["top_cl_contacts"].items()))
    lines.append("")
    lines.append("Processes: " + ", ".join(f"{k} ({v})" for k, v in out["top_go_contacts"].items()))
    lines.append("")
    (RESULTS / "CONCORDANCE.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
