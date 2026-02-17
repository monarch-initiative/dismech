"""
Validate K562 Perturb-seq gene programs (Ota et al., Nature 2025) against
dismech blood disorder entries.

For each trait, loads the trait-to-disorder mapping and program-to-GO mapping,
then checks whether programs whose GO annotations match a disorder's
pathophysiology also contain genes documented in that disorder.

Produces a per-trait summary, per-program matches, coverage statistics,
and a curation gap list.
"""

import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
KB_DIR = PROJECT_DIR / "kb" / "disorders"
VALIDATION_DIR = PROJECT_DIR / "docs" / "assets" / "k562_validation"
TRAIT_FILE = VALIDATION_DIR / "trait_to_hpo.yaml"
PROGRAM_FILE = VALIDATION_DIR / "program_go_mapping.yaml"


def load_trait_mapping() -> dict:
    """Load the trait-to-HPO/disorder mapping."""
    with open(TRAIT_FILE) as f:
        raw = yaml.safe_load(f)
    # Filter out comment-only entries
    return {k: v for k, v in raw.items() if isinstance(v, dict)}


def load_program_mapping() -> dict:
    """Load the program-to-GO mapping."""
    with open(PROGRAM_FILE) as f:
        data = yaml.safe_load(f)
    return data["programs"]


def extract_genes_from_disorder(filepath: Path) -> set[str]:
    """Extract all gene names from a disorder YAML file."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    genes = set()
    for entry in data.get("genetic", []) or []:
        name = entry.get("name", "")
        if name:
            genes.add(name)

    for entry in data.get("pathophysiology", []) or []:
        for gene_entry in entry.get("genes", []) or []:
            if isinstance(gene_entry, dict):
                gname = gene_entry.get("preferred_term", "") or gene_entry.get("name", "")
            else:
                gname = str(gene_entry)
            if gname:
                genes.add(gname)

    return genes


def extract_go_terms_from_disorder(filepath: Path) -> dict[str, str]:
    """Extract GO term IDs and labels from pathophysiology biological_processes.

    Returns dict of go_id -> go_label.
    """
    with open(filepath) as f:
        data = yaml.safe_load(f)

    go_terms = {}
    for entry in data.get("pathophysiology", []) or []:
        for bp in entry.get("biological_processes", []) or []:
            term = bp.get("term", {})
            if term and term.get("id"):
                go_terms[term["id"]] = term.get("label", "")

    return go_terms


def load_disorder_data(disorder_name: str) -> dict | None:
    """Load gene and GO term data from a dismech disorder file."""
    filepath = KB_DIR / f"{disorder_name}.yaml"
    if not filepath.exists():
        return None

    return {
        "genes": extract_genes_from_disorder(filepath),
        "go_terms": extract_go_terms_from_disorder(filepath),
    }


def classify_match(go_overlap: set, gene_overlap: set) -> str:
    """Classify a program-disorder match."""
    if go_overlap and gene_overlap:
        return "CONFIRMED"
    elif go_overlap:
        return "PARTIAL_GO"
    elif gene_overlap:
        return "PARTIAL_GENE"
    else:
        return "NOVEL"


def validate():
    """Run the full K562 program validation."""
    traits = load_trait_mapping()
    programs = load_program_mapping()

    # Focus on RBC traits (primary K562 signal)
    rbc_traits = {k: v for k, v in traits.items() if v.get("group") == "RBC_traits"}
    other_traits = {k: v for k, v in traits.items() if v.get("group") != "RBC_traits"}

    # Pre-load all referenced disorders
    all_disorder_names = set()
    for t in traits.values():
        for d in t.get("related_disorders", []) or []:
            all_disorder_names.add(d)

    disorder_cache = {}
    missing_disorders = set()
    for dname in sorted(all_disorder_names):
        data = load_disorder_data(dname)
        if data:
            disorder_cache[dname] = data
        else:
            missing_disorders.add(dname)

    # Validate each trait
    print("=" * 80)
    print("VALIDATION REPORT: K562 Programs vs DisMech Blood Disorder Entries")
    print("=" * 80)
    print(f"\nPrograms: {len(programs)}")
    print(f"Traits: {len(traits)} ({len(rbc_traits)} RBC, {len(other_traits)} other)")
    print(f"Disorders referenced: {len(all_disorder_names)} "
          f"({len(disorder_cache)} curated, {len(missing_disorders)} missing)")
    if missing_disorders:
        print(f"Missing: {sorted(missing_disorders)}")

    trait_results = {}
    all_confirmed_genes = Counter()
    all_novel_programs = []

    # Process RBC traits first, then others
    trait_order = list(rbc_traits.keys()) + list(other_traits.keys())

    for trait_key in trait_order:
        trait = traits[trait_key]
        related = trait.get("related_disorders", []) or []

        # Aggregate genes and GO terms from all related disorders
        combined_genes = set()
        combined_go = {}
        curated_count = 0
        for dname in related:
            if dname in disorder_cache:
                d = disorder_cache[dname]
                combined_genes |= d["genes"]
                combined_go.update(d["go_terms"])
                curated_count += 1

        if not combined_genes and not combined_go:
            continue  # Skip traits with no curated disorder data

        # Match programs against combined disorder data
        matches = []
        for pid, pdata in sorted(programs.items()):
            prog_go_ids = {t["id"] for t in pdata.get("resolved_go_terms", [])}
            prog_genes = set(pdata.get("top10_genes", []))

            go_overlap = prog_go_ids & set(combined_go.keys())
            gene_overlap = prog_genes & combined_genes

            if go_overlap or gene_overlap:
                category = classify_match(go_overlap, gene_overlap)
                matches.append({
                    "program": pid,
                    "annotation": pdata["curated_annotation"],
                    "category": category,
                    "go_overlap": go_overlap,
                    "gene_overlap": gene_overlap,
                    "marker": pdata.get("marker_coexpression", "none"),
                })
                for g in gene_overlap:
                    all_confirmed_genes[g] += 1

        trait_results[trait_key] = {
            "full_name": trait["full_name"],
            "group": trait["group"],
            "n_disorders": len(related),
            "n_curated": curated_count,
            "n_genes": len(combined_genes),
            "n_go_terms": len(combined_go),
            "matches": matches,
            "n_confirmed": sum(1 for m in matches if m["category"] == "CONFIRMED"),
            "n_partial_go": sum(1 for m in matches if m["category"] == "PARTIAL_GO"),
            "n_partial_gene": sum(1 for m in matches if m["category"] == "PARTIAL_GENE"),
        }

    # Print per-trait results
    print(f"\n{'='*80}")
    print("PER-TRAIT RESULTS")
    print(f"{'='*80}")

    for trait_key in trait_order:
        if trait_key not in trait_results:
            continue
        r = trait_results[trait_key]
        total = r["n_confirmed"] + r["n_partial_go"] + r["n_partial_gene"]
        if total == 0:
            continue

        print(f"\n--- {r['full_name']} ({trait_key}) [{r['group']}] ---")
        print(f"  Disorders: {r['n_curated']}/{r['n_disorders']} curated, "
              f"{r['n_genes']} genes, {r['n_go_terms']} GO terms")
        print(f"  Matches: {r['n_confirmed']} CONFIRMED, "
              f"{r['n_partial_go']} PARTIAL_GO, "
              f"{r['n_partial_gene']} PARTIAL_GENE")

        for m in r["matches"]:
            go_labels = [combined_go.get(g, g) for g in m["go_overlap"]
                         if g in combined_go] if m["go_overlap"] else []
            # Rebuild combined_go for this trait
            trait_combined_go = {}
            for dname in traits[trait_key].get("related_disorders", []) or []:
                if dname in disorder_cache:
                    trait_combined_go.update(disorder_cache[dname]["go_terms"])

            go_labels = [trait_combined_go.get(g, g) for g in m["go_overlap"]]
            print(f"    {m['program']} ({m['annotation']}) [{m['category']}] "
                  f"marker={m['marker']}")
            if m["go_overlap"]:
                print(f"      GO: {go_labels}")
            if m["gene_overlap"]:
                print(f"      Genes: {sorted(m['gene_overlap'])}")

    # Summary table
    print(f"\n{'='*80}")
    print("SUMMARY TABLE")
    print(f"{'='*80}")
    print(f"\n{'Trait':<45} {'Group':<20} {'D':>3} {'G':>4} {'GO':>4} "
          f"{'CON':>4} {'PGO':>4} {'PGN':>4} {'Tot':>4}")
    print("-" * 100)

    for trait_key in trait_order:
        if trait_key not in trait_results:
            continue
        r = trait_results[trait_key]
        total = r["n_confirmed"] + r["n_partial_go"] + r["n_partial_gene"]
        print(f"  {r['full_name']:<43} {r['group']:<20} "
              f"{r['n_curated']:>3} {r['n_genes']:>4} {r['n_go_terms']:>4} "
              f"{r['n_confirmed']:>4} {r['n_partial_go']:>4} "
              f"{r['n_partial_gene']:>4} {total:>4}")

    # Unique confirmed genes
    print(f"\n{'='*80}")
    print("CONFIRMED GENES (appear in both program top10 and disorder)")
    print(f"{'='*80}")
    for gene, count in all_confirmed_genes.most_common():
        print(f"  {gene}: confirmed across {count} traits")

    # Program-centric view
    print(f"\n{'='*80}")
    print("PROGRAM-CENTRIC VIEW")
    print(f"{'='*80}")

    program_matches = defaultdict(list)
    for trait_key, r in trait_results.items():
        for m in r["matches"]:
            program_matches[m["program"]].append({
                "trait": trait_key,
                "category": m["category"],
            })

    for pid in sorted(program_matches.keys(), key=lambda x: int(x[1:])):
        pdata = programs[pid]
        matches = program_matches[pid]
        categories = Counter(m["category"] for m in matches)
        trait_names = [m["trait"] for m in matches]
        print(f"  {pid} ({pdata['curated_annotation']}) marker={pdata.get('marker_coexpression','none')}")
        print(f"    Matches {len(matches)} traits: {categories}")
        if len(trait_names) <= 10:
            print(f"    Traits: {trait_names}")

    # Curation gaps
    print(f"\n{'='*80}")
    print("CURATION GAPS")
    print(f"{'='*80}")

    if missing_disorders:
        print(f"\nMissing disorder files ({len(missing_disorders)}):")
        for d in sorted(missing_disorders):
            # Count how many traits reference this disorder
            trait_count = sum(1 for t in traits.values()
                              if d in (t.get("related_disorders", []) or []))
            print(f"  {d} (referenced by {trait_count} traits)")

    # Programs with RBC/erythroid marker but no matches
    rbc_programs = {pid for pid, pdata in programs.items()
                    if pdata.get("marker_coexpression", "none") in
                    ("RBC", "erythroid progenitor", "erythroid progenitor, RBC")}
    matched_programs = set(program_matches.keys())
    unmatched_rbc = rbc_programs - matched_programs
    if unmatched_rbc:
        print(f"\nRBC/erythroid programs with no disorder matches ({len(unmatched_rbc)}):")
        for pid in sorted(unmatched_rbc, key=lambda x: int(x[1:])):
            pdata = programs[pid]
            print(f"  {pid} ({pdata['curated_annotation']}) "
                  f"marker={pdata.get('marker_coexpression','none')}")
            print(f"    GO: {[t['label'] for t in pdata.get('resolved_go_terms', [])]}")
            print(f"    Genes: {pdata.get('top10_genes', [])[:5]}...")

    # Coverage statistics
    print(f"\n{'='*80}")
    print("COVERAGE STATISTICS")
    print(f"{'='*80}")
    traits_with_matches = sum(1 for r in trait_results.values()
                              if r["n_confirmed"] + r["n_partial_go"] + r["n_partial_gene"] > 0)
    print(f"Traits with any program match: {traits_with_matches}/{len(trait_results)}")
    print(f"Unique programs matching: {len(program_matches)}/{len(programs)}")
    print(f"Unique confirmed genes: {len(all_confirmed_genes)}")
    total_disorder_genes = set()
    for d in disorder_cache.values():
        total_disorder_genes |= d["genes"]
    if total_disorder_genes:
        rate = len(all_confirmed_genes) / len(total_disorder_genes) * 100
        print(f"Gene confirmation rate: {len(all_confirmed_genes)}/{len(total_disorder_genes)} "
              f"({rate:.1f}%)")


if __name__ == "__main__":
    validate()
