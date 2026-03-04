#!/usr/bin/env python3
"""Fetch Reactome disease data and export as YAML or Markdown.

Downloads disease variant mappings, pathway associations, and gene participants
from Reactome's bulk download files and Content Service API.

Usage:
    # Export a disease by DOID
    uv run python scripts/fetch_reactome_disease.py DOID:13636  # Fanconi anemia

    # Export by disease name (searches Reactome disease list)
    uv run python scripts/fetch_reactome_disease.py "cystic fibrosis"

    # Output as markdown (default is YAML)
    uv run python scripts/fetch_reactome_disease.py DOID:13636 --format md

    # Save to file
    uv run python scripts/fetch_reactome_disease.py DOID:13636 -o output/fa_reactome.yaml
"""

import json
import sys
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml


VARIANT_TSV_URL = (
    "https://reactome.org/download/current/disease_variant_ewas_mapping.tsv"
)
DISEASE_PATHWAYS_URL = "https://reactome.org/download/current/HumanDiseasePathways.txt"
CONTENT_SERVICE = "https://reactome.org/ContentService"

CACHE_DIR = Path("pathways/reactome/.cache")


def fetch_url(url: str, cache_name: str | None = None) -> str:
    """Fetch URL with optional local caching."""
    if cache_name:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache_path = CACHE_DIR / cache_name
        if cache_path.exists():
            return cache_path.read_text()

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode("utf-8")

    if cache_name:
        cache_path.write_text(text)
    return text


def fetch_json(url: str) -> dict | list:
    import time

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except (urllib.error.URLError, ConnectionResetError, TimeoutError) as e:
            if attempt < 2:
                wait = 2 ** (attempt + 1)
                print(f"    Retry {attempt + 1} after {wait}s ({e})", file=sys.stderr)
                time.sleep(wait)
            else:
                raise


@dataclass
class VariantRecord:
    gene: str
    variant_name: str
    uniprot_id: str
    modification: str
    modification_class: str
    functional_status: str
    disease_reaction_id: str
    disease_reaction_name: str
    disease_pathway_id: str
    disease_pathway_name: str
    normal_reaction_id: str
    normal_reaction_name: str
    normal_pathway_name: str
    normal_pathway_id: str
    go_accession: str
    go_name: str
    pmids: list[str]


@dataclass
class DiseasePathway:
    stable_id: str
    name: str
    normal_pathway_id: str = ""
    normal_pathway_name: str = ""
    genes: list[str] = field(default_factory=list)
    variants: list[VariantRecord] = field(default_factory=list)
    go_processes: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class ReactomeDisease:
    doid: str
    name: str
    definition: str = ""
    synonyms: list[str] = field(default_factory=list)
    pathways: list[DiseasePathway] = field(default_factory=list)
    all_genes: set = field(default_factory=set)
    all_pmids: set = field(default_factory=set)


def find_disease(query: str) -> tuple[str, str]:
    """Find a disease by DOID or name search. Returns (doid, name)."""
    diseases = _get_diseases_list()

    if query.startswith("DOID:"):
        identifier = query.replace("DOID:", "")
        for d in diseases:
            if d.get("identifier") == identifier and d.get("databaseName") == "DOID":
                return query, d["displayName"]
        raise ValueError(f"Disease not found: {query}")

    query_lower = query.lower()
    matches = []
    for d in diseases:
        if d.get("databaseName") != "DOID":
            continue
        name = d["displayName"].lower()
        synonyms = [s.lower() for s in d.get("synonym", [])]
        if query_lower == name or query_lower in synonyms:
            return f"DOID:{d['identifier']}", d["displayName"]
        if query_lower in name:
            matches.append((f"DOID:{d['identifier']}", d["displayName"]))

    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(f"Multiple matches for '{query}':", file=sys.stderr)
        for doid, name in matches:
            print(f"  {doid} - {name}", file=sys.stderr)
        return matches[0]
    raise ValueError(f"Disease not found: {query}")


def parse_variant_tsv(doid: str) -> list[VariantRecord]:
    """Parse disease_variant_ewas_mapping.tsv for a specific DOID."""
    text = fetch_url(VARIANT_TSV_URL, "disease_variant_ewas_mapping.tsv")
    lines = text.strip().split("\n")
    header = lines[0].split("\t")

    records = []
    doid_bare = doid.replace("DOID:", "")

    for line in lines[1:]:
        fields = line.split("\t")
        if len(fields) < len(header):
            fields.extend([""] * (len(header) - len(fields)))

        row = dict(zip(header, fields))

        # disease_identifier can contain multiple DOIDs separated by |
        disease_ids = row.get("disease_identifier", "").split("|")
        if doid_bare not in disease_ids and doid not in disease_ids:
            continue

        # Extract PMIDs from reaction literature references
        pmid_str = row.get("reactionLikeEvent_literatureReference_pubMedIdentifier", "")
        pmids = [
            p.replace("pubmed:", "PMID:") for p in pmid_str.split("|") if p.strip()
        ]

        ref_parts = row.get("referenceEntity_id", "").split(":")
        uniprot = ref_parts[1] if len(ref_parts) > 1 else ref_parts[0]

        records.append(
            VariantRecord(
                gene=row.get("Genename", ""),
                variant_name=row.get("displayName", ""),
                uniprot_id=uniprot,
                modification=row.get("hasModifiedResidue_displayName", ""),
                modification_class=row.get("modifiedResidue_class", ""),
                functional_status=row.get(
                    "entityWithAccessionedSequence_reactionLikeEvent_"
                    "entityFunctionalStatus_functionalStatus_functionalStatusType_displayName",
                    "",
                ),
                disease_reaction_id=row.get(
                    "entityWithAccessionedSequence_reactionLikeEvent_stable_id", ""
                ),
                disease_reaction_name=row.get(
                    "entityWithAccessionedSequence_reactionLikeEvent_displayName", ""
                ),
                disease_pathway_id=row.get(
                    "entityWithAccessionedSequence_pathway_stable_id", ""
                ),
                disease_pathway_name=row.get(
                    "entityWithAccessionedSequence_pathway_displayName", ""
                ),
                normal_reaction_id=row.get(
                    "entityWithAccessionedSequence_reactionLikeEvent_normalReaction_stable_id",
                    "",
                ),
                normal_reaction_name=row.get(
                    "entityWithAccessionedSequence_reactionLikeEvent_normalReaction_displayName",
                    "",
                ),
                normal_pathway_name=row.get(
                    "entityWithAccessionedSequence_pathway_normalPathway_displayName",
                    "",
                ),
                normal_pathway_id=row.get(
                    "entityWithAccessionedSequence_pathway_normalPathway_stable_id", ""
                ),
                go_accession=row.get(
                    "entityWithAccessionedSequence_pathway_normalPathway_"
                    "goBiologicalProcess_accession",
                    "",
                ),
                go_name=row.get(
                    "entityWithAccessionedSequence_pathway_normalPathway_"
                    "goBiologicalProcess_displayName",
                    "",
                ),
                pmids=pmids,
            )
        )

    return records


def get_pathway_participants(pathway_id: str) -> list[str]:
    """Get gene names from pathway participants via Content Service API."""
    participants = fetch_json(f"{CONTENT_SERVICE}/data/participants/{pathway_id}")
    genes = set()
    for entity in participants:
        for r in entity.get("refEntities", []):
            rdn = r.get("displayName", "")
            parts = rdn.split(" ", 1)
            if len(parts) > 1 and parts[0].startswith("UniProt:"):
                genes.add(parts[1])
    return sorted(genes)


def get_pathway_events(pathway_id: str) -> list[dict]:
    """Get contained events (reactions) for a pathway."""
    events_raw = fetch_json(
        f"{CONTENT_SERVICE}/data/pathway/{pathway_id}/containedEvents"
    )
    events = []
    for e in events_raw:
        if isinstance(e, dict):
            events.append(
                {
                    "id": e.get("stId", ""),
                    "name": e.get("displayName", ""),
                    "type": e.get("schemaClass", ""),
                }
            )
        else:
            ev = fetch_json(f"{CONTENT_SERVICE}/data/query/{e}")
            events.append(
                {
                    "id": ev.get("stId", ""),
                    "name": ev.get("displayName", ""),
                    "type": ev.get("schemaClass", ""),
                }
            )
    return events


_diseases_cache: list | None = None


def _get_diseases_list() -> list:
    global _diseases_cache
    if _diseases_cache is None:
        _diseases_cache = fetch_json(f"{CONTENT_SERVICE}/data/diseases")
    return _diseases_cache


def build_disease_summary(query: str) -> ReactomeDisease:
    """Build a complete disease summary from Reactome data."""
    doid, name = find_disease(query)
    print(f"Found: {name} ({doid})", file=sys.stderr)

    disease = ReactomeDisease(doid=doid, name=name)

    # Get disease metadata
    diseases_list = _get_diseases_list()
    doid_bare = doid.replace("DOID:", "")
    for d in diseases_list:
        if d.get("identifier") == doid_bare and d.get("databaseName") == "DOID":
            disease.definition = d.get("definition", "")
            disease.synonyms = d.get("synonym", [])
            break

    # Parse variant data
    print("Fetching variant mappings...", file=sys.stderr)
    variants = parse_variant_tsv(doid)
    print(f"  Found {len(variants)} variant records", file=sys.stderr)

    # Group by disease pathway
    pathway_map: dict[str, DiseasePathway] = {}
    for v in variants:
        pid = v.disease_pathway_id
        if pid not in pathway_map:
            pathway_map[pid] = DiseasePathway(
                stable_id=pid,
                name=v.disease_pathway_name,
                normal_pathway_id=v.normal_pathway_id,
                normal_pathway_name=v.normal_pathway_name,
            )
        pw = pathway_map[pid]
        pw.variants.append(v)
        if v.gene:
            pw.genes.append(v.gene)
            disease.all_genes.add(v.gene)
        if v.go_accession:
            pw.go_processes.append((f"GO:{v.go_accession}", v.go_name))
        disease.all_pmids.update(v.pmids)

    # Deduplicate genes and GO processes per pathway
    for pw in pathway_map.values():
        pw.genes = sorted(set(pw.genes))
        pw.go_processes = sorted(set(pw.go_processes))

    disease.pathways = sorted(pathway_map.values(), key=lambda p: p.name)

    # If no variant data, try broader strategies
    if not disease.pathways:
        print("  No variant data; trying search API...", file=sys.stderr)
        disease.pathways = _search_disease_pathways(name, doid_bare)

    # For each disease pathway, optionally fetch participants from API
    for pw in disease.pathways:
        if pw.stable_id and not pw.genes:
            try:
                print(f"  Fetching participants for {pw.stable_id}...", file=sys.stderr)
                pw.genes = get_pathway_participants(pw.stable_id)
                disease.all_genes.update(pw.genes)
            except Exception as e:
                print(
                    f"    Warning: could not fetch participants: {e}", file=sys.stderr
                )

    return disease


def _search_disease_pathways(name: str, doid_bare: str) -> list[DiseasePathway]:
    """Find disease pathways via search API and HumanDiseasePathways.txt."""
    pathways: dict[str, DiseasePathway] = {}

    # Strategy 1: Search API for disease-tagged pathways
    # Use specific disease terms (drop generic words like "disease", "syndrome")
    import re as _re

    stop_words = {"disease", "syndrome", "disorder", "type", "the", "and", "with", "of"}
    # Strip punctuation for matching
    name_words = _re.findall(r"[a-z]+", name.lower())
    specific_terms = [t for t in name_words if t not in stop_words and len(t) > 2]
    queries = [name]
    if specific_terms:
        queries.append(" ".join(specific_terms))

    # Top-level pathways to exclude (too broad)
    exclude_ids = {
        "R-HSA-1643685",  # Disease (root)
        "R-HSA-5663205",  # Infectious disease
        "R-HSA-1226099",  # Signaling by FGFR in disease
        "R-HSA-5663202",  # Diseases of signal transduction...
        "R-HSA-9675126",  # Diseases of mitotic cell cycle
        "R-HSA-9675132",  # Diseases of cellular response to stress
        "R-HSA-9645723",  # Diseases of programmed cell death
        "R-HSA-9675135",  # Diseases of DNA repair
        "R-HSA-5619115",  # Disorders of transmembrane transporters
        "R-HSA-5668914",  # Diseases of metabolism
        "R-HSA-5260271",  # Diseases of Immune System
        "R-HSA-9675143",  # Diseases of the neuronal system
        "R-HSA-9675151",  # Disorders of Developmental Biology
        "R-HSA-9671793",  # Diseases of hemostasis
    }

    for query in queries:
        try:
            data = fetch_json(
                f"{CONTENT_SERVICE}/search/query"
                f"?query={urllib.request.quote(query)}"
                f"&types=Pathway&species=Homo+sapiens&cluster=true"
            )
            for r in data.get("results", []):
                for e in r.get("entries", []):
                    pid = e.get("stId", "")
                    if not e.get("isDisease") or not pid or pid in exclude_ids:
                        continue
                    # Check that at least one specific term appears in the pathway name
                    pname_raw = e.get("name", "")
                    pname_clean = (
                        pname_raw.replace('<span class="highlighting" >', "")
                        .replace("</span>", "")
                        .lower()
                    )
                    if specific_terms and not any(
                        t in pname_clean for t in specific_terms
                    ):
                        continue
                    if pid not in pathways:
                        pathways[pid] = DiseasePathway(
                            stable_id=pid,
                            name=pname_clean
                            if len(pname_clean) < 200
                            else pname_clean[:200],
                        )
        except Exception:
            pass

    # Strategy 2: HumanDiseasePathways.txt name match
    dp_text = fetch_url(DISEASE_PATHWAYS_URL, "HumanDiseasePathways.txt")
    name_lower = name.lower()
    # Also try key terms from the disease name
    name_terms = [t for t in name_lower.split() if len(t) > 3]
    for line in dp_text.strip().split("\n"):
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        pid, pname = parts[0], parts[1]
        pname_lower = pname.lower()
        if name_lower in pname_lower or doid_bare in line:
            if pid not in pathways:
                pathways[pid] = DiseasePathway(stable_id=pid, name=pname)
        elif len(name_terms) >= 2 and all(t in pname_lower for t in name_terms):
            if pid not in pathways:
                pathways[pid] = DiseasePathway(stable_id=pid, name=pname)

    return sorted(pathways.values(), key=lambda p: p.name)


def to_yaml(disease: ReactomeDisease) -> str:
    """Convert disease summary to YAML."""
    data = {
        "reactome_disease": {
            "doid": disease.doid,
            "name": disease.name,
            "definition": disease.definition,
            "synonyms": disease.synonyms or [],
            "total_genes": len(disease.all_genes),
            "total_pmids": len(disease.all_pmids),
            "genes": sorted(disease.all_genes),
            "pathways": [],
        }
    }

    for pw in disease.pathways:
        pathway_data = {
            "id": pw.stable_id,
            "name": pw.name,
            "genes": pw.genes,
            "url": f"https://reactome.org/PathwayBrowser/#/{pw.stable_id}",
        }
        if pw.normal_pathway_id:
            pathway_data["normal_pathway"] = {
                "id": pw.normal_pathway_id,
                "name": pw.normal_pathway_name,
            }
        if pw.go_processes:
            pathway_data["go_biological_processes"] = [
                {"id": gid, "name": gname} for gid, gname in pw.go_processes
            ]

        # Group variants by gene
        gene_variants: dict[str, list[dict]] = defaultdict(list)
        for v in pw.variants:
            gene_variants[v.gene].append(
                {
                    "variant": v.variant_name,
                    "modification": v.modification,
                    "functional_status": v.functional_status,
                    "disease_reaction": v.disease_reaction_name,
                    "normal_reaction": v.normal_reaction_name,
                    "pmids": v.pmids,
                }
            )

        if gene_variants:
            pathway_data["variant_genes"] = {
                gene: variants for gene, variants in sorted(gene_variants.items())
            }

        data["reactome_disease"]["pathways"].append(pathway_data)

    return yaml.dump(data, default_flow_style=False, sort_keys=False, width=120)


def to_markdown(disease: ReactomeDisease) -> str:
    """Convert disease summary to Markdown."""
    lines = [
        f"# {disease.name} — Reactome Disease Summary",
        "",
        f"**DOID**: {disease.doid}",
        f"**Definition**: {disease.definition}" if disease.definition else "",
        f"**Synonyms**: {', '.join(disease.synonyms)}" if disease.synonyms else "",
        f"**Total genes**: {len(disease.all_genes)}",
        f"**Total PMIDs**: {len(disease.all_pmids)}",
        "",
        f"## All Genes ({len(disease.all_genes)})",
        "",
        ", ".join(sorted(disease.all_genes)),
        "",
    ]

    for pw in disease.pathways:
        lines.append(f"## Pathway: {pw.name}")
        lines.append(
            f"- **ID**: [{pw.stable_id}](https://reactome.org/PathwayBrowser/#/{pw.stable_id})"
        )
        if pw.normal_pathway_id:
            lines.append(
                f"- **Normal pathway**: {pw.normal_pathway_name} ({pw.normal_pathway_id})"
            )
        lines.append(f"- **Genes**: {', '.join(pw.genes)}")

        if pw.go_processes:
            lines.append(
                f"- **GO processes**: {'; '.join(f'{gname} ({gid})' for gid, gname in pw.go_processes)}"
            )

        if pw.variants:
            lines.append("")
            lines.append("### Variants")
            lines.append("")
            lines.append("| Gene | Variant | Functional Status | Disease Reaction |")
            lines.append("|------|---------|-------------------|-----------------|")

            seen = set()
            for v in pw.variants:
                key = (v.gene, v.modification, v.functional_status)
                if key in seen:
                    continue
                seen.add(key)
                lines.append(
                    f"| {v.gene} | {v.modification} | {v.functional_status} | {v.disease_reaction_name} |"
                )

        lines.append("")

    if disease.all_pmids:
        lines.append("## References")
        lines.append("")
        for pmid in sorted(disease.all_pmids):
            lines.append(f"- {pmid}")

    return "\n".join(lines) + "\n"


PATHWAYS_DIR = Path("pathways/reactome")


def default_output_path(disease_name: str, fmt: str) -> Path:
    """Generate default output path from disease name."""
    slug = disease_name.replace(" ", "_").replace("'", "")
    return PATHWAYS_DIR / f"{slug}.{fmt}"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fetch Reactome disease data")
    parser.add_argument(
        "query", nargs="?", help="DOID (e.g. DOID:13636) or disease name"
    )
    parser.add_argument("--format", choices=["yaml", "md"], default="yaml")
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: pathways/reactome/<name>.<fmt>)",
    )
    parser.add_argument(
        "--all-overlap",
        action="store_true",
        help="Fetch all Reactome diseases that overlap with dismech KB",
    )
    args = parser.parse_args()

    if args.all_overlap:
        fetch_all_overlap(args.format)
        return

    if not args.query:
        parser.error("query is required unless --all-overlap is used")

    disease = build_disease_summary(args.query)

    if args.format == "yaml":
        text = to_yaml(disease)
    else:
        text = to_markdown(disease)

    output = (
        Path(args.output)
        if args.output
        else default_output_path(disease.name, args.format)
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text)
    print(f"Written to {output}", file=sys.stderr)


def fetch_all_overlap(fmt: str):
    """Fetch Reactome data for all diseases that overlap with dismech KB."""
    import re

    kb_dir = Path("kb/disorders")
    dismech_names = {
        re.sub(r"[^a-z0-9]", "", f.stem.lower()): f.stem
        for f in kb_dir.glob("*.yaml")
        if not f.name.endswith(".history.yaml")
    }

    diseases = _get_diseases_list()
    doid_diseases = [d for d in diseases if d.get("databaseName") == "DOID"]

    matches = []
    for d in doid_diseases:
        norm = re.sub(r"[^a-z0-9]", "", d["displayName"].lower())
        if norm in dismech_names:
            matches.append((f"DOID:{d['identifier']}", d["displayName"]))

    print(f"Found {len(matches)} overlapping diseases", file=sys.stderr)
    PATHWAYS_DIR.mkdir(parents=True, exist_ok=True)

    for doid, name in matches:
        outpath = default_output_path(name, fmt)
        if outpath.exists():
            print(f"  Skipping {name} (already cached)", file=sys.stderr)
            continue
        print(f"  Fetching {name} ({doid})...", file=sys.stderr)
        disease = build_disease_summary(doid)
        text = to_yaml(disease) if fmt == "yaml" else to_markdown(disease)
        outpath.write_text(text)
        print(f"  -> {outpath}", file=sys.stderr)


if __name__ == "__main__":
    main()
