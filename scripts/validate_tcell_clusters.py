"""
Validate Zhu/Dann T cell Perturb-seq regulator clusters against dismech
autoimmune disease entries.

For each significant cluster-disease pair (FDR < 0.05), checks whether the
intersecting genes (GWAS hits that are also downstream of cluster regulators)
appear in the corresponding dismech disorder entry's genetics or pathophysiology.
"""

import ast
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# Disease name mapping: Zhu/Dann name -> dismech YAML filename
DISEASE_MAP = {
    "rheumatoid arthritis": "Rheumatoid_Arthritis.yaml",
    "systemic lupus erythematosus": "Systemic_Lupus_Erythematosus.yaml",
    "inflammatory bowel disease": None,  # umbrella - use Crohn's + UC
    "multiple sclerosis": "Multiple_Sclerosis.yaml",
    "type 1 diabetes mellitus": "Type_I_Diabetes.yaml",
    "psoriasis": "Psoriasis.yaml",
    "ankylosing spondylitis": "Ankylosing_Spondylitis.yaml",
    "asthma": "Asthma.yaml",
    "Hashimoto's thyroiditis": "Hashimotos_Thyroiditis.yaml",
    "Crohn's disease": "Crohn_Disease.yaml",
    "ulcerative colitis": "Ulcerative_Colitis.yaml",
    "celiac disease": "Celiac_Disease.yaml",
    "atopic eczema": "Atopic_Dermatitis.yaml",
    "autoimmune disease": None,  # umbrella - skip
}

KB_DIR = Path("kb/disorders")
ENRICHMENT_FILE = Path(
    "docs/assets/zhu_dann_2025/cluster_autoimmune_enrichment_results.csv"
)
CLUSTER_FILE = Path("docs/assets/zhu_dann_2025/clustering_results_and_annotations.csv")


def extract_genes_from_disorder(filepath: Path) -> dict:
    """Extract all gene mentions from a disorder YAML file.

    Returns dict with keys:
        genetic_genes: genes from the genetic section
        pathophys_genes: genes mentioned in pathophysiology
        all_genes: union of both
        gene_details: dict of gene -> {section, association/role, notes}
    """
    with open(filepath) as f:
        data = yaml.safe_load(f)

    genetic_genes = set()
    pathophys_genes = set()
    gene_details = {}

    # Extract from genetic section
    for entry in data.get("genetic", []):
        name = entry.get("name", "")
        if name:
            genetic_genes.add(name)
            gene_details[name] = {
                "section": "genetic",
                "association": entry.get("association", ""),
                "notes": entry.get("notes", ""),
            }

    # Extract from pathophysiology section
    for entry in data.get("pathophysiology", []):
        # Genes mentioned directly
        for gene_entry in entry.get("genes", []):
            gname = (
                gene_entry.get("name", "")
                if isinstance(gene_entry, dict)
                else str(gene_entry)
            )
            if gname:
                pathophys_genes.add(gname)
                if gname not in gene_details:
                    gene_details[gname] = {
                        "section": "pathophysiology",
                        "context": entry.get("name", ""),
                    }

        # Also check description text for gene symbols (uppercase, 2-6 chars)
        desc = entry.get("description", "") or ""
        name_field = entry.get("name", "") or ""
        text = f"{name_field} {desc}"
        # Look for known gene-like patterns in text
        for token in re.findall(r"\b([A-Z][A-Z0-9]{1,10})\b", text):
            # Skip common non-gene uppercase words
            if token in {
                "THE",
                "AND",
                "FOR",
                "WITH",
                "FROM",
                "THIS",
                "THAT",
                "NOT",
                "BUT",
                "ARE",
                "HAS",
                "WAS",
                "MAY",
                "CAN",
                "DNA",
                "RNA",
                "MHC",
                "HLA",
                "TNF",
                "NF",
                "IGG",
                "IGE",
                "IGA",
                "IGM",
                "IFN",
                "TGF",
                "GWAS",
                "SNP",
                "INCREASED",
                "DECREASED",
                "ABNORMAL",
                "VIA",
                "LOSS",
                "TYPE",
                "CLASS",
            }:
                continue

    all_genes = genetic_genes | pathophys_genes

    # Also scan for gene symbols in treatment and phenotype descriptions
    # (lighter touch - just look for exact gene names we already know about)

    return {
        "genetic_genes": genetic_genes,
        "pathophys_genes": pathophys_genes,
        "all_genes": all_genes,
        "gene_details": gene_details,
    }


def extract_processes_from_disorder(filepath: Path) -> list[dict]:
    """Extract biological processes with GO terms from pathophysiology."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    processes = []
    for entry in data.get("pathophysiology", []):
        for bp in entry.get("biological_processes", []):
            term = bp.get("term", {})
            if term:
                processes.append(
                    {
                        "name": entry.get("name", ""),
                        "go_id": term.get("id", ""),
                        "go_label": term.get("label", ""),
                        "modifier": entry.get("modifier", ""),
                    }
                )
    return processes


def load_cluster_annotations() -> dict:
    """Load cluster annotations from the clustering results file."""
    clusters = {}
    with open(CLUSTER_FILE, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = int(row["cluster"])
            members = ast.literal_eval(row["cluster_member"])
            clusters[cid] = {
                "annotation": row["manual_annotation"],
                "gene_size": int(row["cluster_gene_size"]),
                "members": members,
                "condition": row["condition_specificity"],
            }
    return clusters


def load_significant_enrichments(fdr_threshold: float = 0.05) -> list[dict]:
    """Load significant cluster-disease enrichment results."""
    results = []
    with open(ENRICHMENT_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["negative_control_disease"] == "True":
                continue
            fdr = float(row["p_adj_fdr"])
            if fdr >= fdr_threshold:
                continue
            genes_str = row["intersecting_genes"]
            genes = ast.literal_eval(genes_str) if genes_str else []
            results.append(
                {
                    "cluster": int(row["cluster"]),
                    "disease": row["disease"],
                    "gene_set": row["gene_set"],
                    "odds_ratio": float(row["odds_ratio"]),
                    "fdr": fdr,
                    "n_intersect": int(float(row["in_cluster_in_disease"])),
                    "genes": set(genes),
                }
            )
    return results


def validate():
    """Run the full validation."""
    # Load data
    clusters = load_cluster_annotations()
    enrichments = load_significant_enrichments()

    # Load dismech gene sets for each disease
    dismech_data = {}
    for disease_name, yaml_file in DISEASE_MAP.items():
        if yaml_file is None:
            continue
        filepath = KB_DIR / yaml_file
        if not filepath.exists():
            print(f"WARNING: {filepath} not found", file=sys.stderr)
            continue
        dismech_data[disease_name] = {
            "genes": extract_genes_from_disorder(filepath),
            "processes": extract_processes_from_disorder(filepath),
            "file": yaml_file,
        }

    # For IBD umbrella, merge Crohn's + UC
    if "Crohn's disease" in dismech_data and "ulcerative colitis" in dismech_data:
        crohn_genes = dismech_data["Crohn's disease"]["genes"]["all_genes"]
        uc_genes = dismech_data["ulcerative colitis"]["genes"]["all_genes"]
        dismech_data["inflammatory bowel disease"] = {
            "genes": {
                "all_genes": crohn_genes | uc_genes,
                "genetic_genes": (
                    dismech_data["Crohn's disease"]["genes"]["genetic_genes"]
                    | dismech_data["ulcerative colitis"]["genes"]["genetic_genes"]
                ),
                "pathophys_genes": (
                    dismech_data["Crohn's disease"]["genes"]["pathophys_genes"]
                    | dismech_data["ulcerative colitis"]["genes"]["pathophys_genes"]
                ),
                "gene_details": {
                    **dismech_data["Crohn's disease"]["genes"]["gene_details"],
                    **dismech_data["ulcerative colitis"]["genes"]["gene_details"],
                },
            },
            "processes": (
                dismech_data["Crohn's disease"]["processes"]
                + dismech_data["ulcerative colitis"]["processes"]
            ),
            "file": "Crohn_Disease.yaml + Ulcerative_Colitis.yaml",
        }

    # Validate each significant enrichment
    results_by_disease = defaultdict(list)
    all_confirmed = []
    all_novel = []

    for enr in enrichments:
        disease = enr["disease"]
        if disease not in dismech_data:
            continue

        dm = dismech_data[disease]
        dm_genes = dm["genes"]["all_genes"]
        pipeline_genes = enr["genes"]

        confirmed = pipeline_genes & dm_genes
        novel = pipeline_genes - dm_genes

        cluster_info = clusters.get(enr["cluster"], {})

        result = {
            "cluster": enr["cluster"],
            "cluster_annotation": cluster_info.get("annotation", "unknown"),
            "gene_set": enr["gene_set"],
            "odds_ratio": enr["odds_ratio"],
            "fdr": enr["fdr"],
            "n_pipeline_genes": len(pipeline_genes),
            "n_confirmed": len(confirmed),
            "n_novel": len(novel),
            "confirmed_genes": sorted(confirmed),
            "novel_genes": sorted(novel),
            "confirmation_rate": len(confirmed) / len(pipeline_genes)
            if pipeline_genes
            else 0,
        }

        results_by_disease[disease].append(result)
        all_confirmed.extend(confirmed)
        all_novel.extend(novel)

    # Print report
    print("=" * 80)
    print("VALIDATION REPORT: Zhu/Dann T Cell Clusters vs DisMech Autoimmune Entries")
    print("=" * 80)
    print()

    total_pairs = sum(len(v) for v in results_by_disease.values())
    total_genes_tested = set()
    total_genes_confirmed = set()
    total_genes_novel = set()

    for disease in sorted(results_by_disease.keys()):
        entries = results_by_disease[disease]
        dm = dismech_data[disease]
        dm_genes = dm["genes"]["all_genes"]

        print(f"\n{'=' * 70}")
        print(f"  {disease.upper()}")
        print(f"  dismech file: {dm['file']}")
        print(f"  dismech genes: {sorted(dm_genes)}")
        print(f"  significant cluster-disease pairs: {len(entries)}")
        print(f"{'=' * 70}")

        for r in sorted(entries, key=lambda x: -x["odds_ratio"]):
            total_genes_tested.update(r["confirmed_genes"])
            total_genes_tested.update(r["novel_genes"])
            total_genes_confirmed.update(r["confirmed_genes"])
            total_genes_novel.update(r["novel_genes"])

            status = "CONFIRMED" if r["n_confirmed"] > 0 else "NOVEL"
            if r["n_confirmed"] > 0 and r["n_novel"] > 0:
                status = "PARTIAL"

            print(
                f"\n  Cluster {r['cluster']} ({r['cluster_annotation']}) "
                f"[{r['gene_set']}]"
            )
            print(
                f"    OR={r['odds_ratio']:.1f}, FDR={r['fdr']:.2e}, "
                f"genes={r['n_pipeline_genes']}"
            )
            print(
                f"    Status: {status} "
                f"({r['n_confirmed']}/{r['n_pipeline_genes']} confirmed, "
                f"{r['n_novel']} novel)"
            )
            if r["confirmed_genes"]:
                print(f"    Confirmed: {', '.join(r['confirmed_genes'])}")
            if r["novel_genes"]:
                # Show top 10 novel genes
                novel_display = r["novel_genes"][:15]
                suffix = (
                    f" ... +{len(r['novel_genes']) - 15} more"
                    if len(r["novel_genes"]) > 15
                    else ""
                )
                print(f"    Novel:     {', '.join(novel_display)}{suffix}")

    # Summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nDiseases evaluated: {len(results_by_disease)}")
    print(f"Significant cluster-disease pairs: {total_pairs}")
    print(f"Unique genes tested: {len(total_genes_tested)}")
    print(
        f"Genes confirmed in dismech: {len(total_genes_confirmed)} "
        f"({100 * len(total_genes_confirmed) / max(len(total_genes_tested), 1):.1f}%)"
    )
    print(
        f"Novel genes (not in dismech): {len(total_genes_novel)} "
        f"({100 * len(total_genes_novel) / max(len(total_genes_tested), 1):.1f}%)"
    )

    # Per-disease summary
    print(f"\n{'Disease':<35} {'Pairs':>5} {'Confirmed':>10} {'Novel':>8} {'Rate':>6}")
    print("-" * 70)
    for disease in sorted(results_by_disease.keys()):
        entries = results_by_disease[disease]
        all_conf = set()
        all_nov = set()
        for r in entries:
            all_conf.update(r["confirmed_genes"])
            all_nov.update(r["novel_genes"])
        total = len(all_conf | all_nov)
        rate = len(all_conf) / total * 100 if total else 0
        print(
            f"  {disease:<33} {len(entries):>5} {len(all_conf):>10} "
            f"{len(all_nov):>8} {rate:>5.1f}%"
        )

    # Most frequently confirmed genes
    from collections import Counter

    conf_counts = Counter(all_confirmed)
    print("\nTop confirmed genes (across diseases):")
    for gene, count in conf_counts.most_common(20):
        print(f"  {gene}: confirmed in {count} cluster-disease pairs")

    # Most frequently novel genes (curation candidates)
    nov_counts = Counter(all_novel)
    print("\nTop novel genes (curation candidates):")
    for gene, count in nov_counts.most_common(20):
        print(f"  {gene}: novel in {count} cluster-disease pairs")


if __name__ == "__main__":
    validate()
