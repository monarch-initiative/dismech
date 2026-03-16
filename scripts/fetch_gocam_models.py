#!/usr/bin/env python3
"""Fetch GO-CAM models for specified genes and export structured YAML.

Downloads the GO-CAM browser index to find models involving target genes,
then fetches full model data from the GO-CAM API to extract activity units
and causal edges.

Usage:
    # Fetch models for specific genes
    uv run python scripts/fetch_gocam_models.py PTCH1 SMO SUFU GLI1 GLI2 GLI3

    # Fetch models for genes from a disorder YAML
    uv run python scripts/fetch_gocam_models.py --from-disorder kb/disorders/Noonan_Syndrome.yaml

    # List models without fetching details
    uv run python scripts/fetch_gocam_models.py --list-only PTPN11 SOS1

    # Force refresh of the model index cache
    uv run python scripts/fetch_gocam_models.py --refresh-index PTCH1
"""

import argparse
import json
import sys
import time
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml


# --- Constants ---

INDEX_URL = "https://go-cam-browser.geneontology.org/data.json"
MODEL_API = "https://api.geneontology.org/api/go-cam"

CACHE_DIR = Path("causal_models/.cache/gocam")

# RO relations we care about for causal edges
CAUSAL_RELATIONS = {
    "RO:0002629": "directly positively regulates",
    "RO:0002630": "directly negatively regulates",
    "RO:0002407": "directly activates",
    "RO:0002409": "directly inhibits",
    "RO:0002411": "causally upstream of",
    "RO:0002413": "directly provides input for",
    "RO:0002578": "directly regulates",
    "RO:0012005": "is regulated by",
    "RO:0002304": "causally upstream of, positive effect",
    "RO:0002305": "causally upstream of, negative effect",
}

# Structural relations (not causal, but needed to build activity units)
STRUCTURAL_RELATIONS = {
    "RO:0002333": "enabled_by",
    "RO:0002233": "has_input",
    "RO:0002234": "has_output",
    "BFO:0000050": "part_of",
    "BFO:0000066": "occurs_in",
}

HUMAN_TAXON = "NCBITaxon:9606"


# --- Data classes ---


@dataclass
class Activity:
    """A single activity unit: gene product performing a molecular function."""

    node_id: str
    gene_symbol: str = ""
    gene_id: str = ""  # UniProtKB or other ID
    molecular_function_id: str = ""
    molecular_function_label: str = ""
    location_id: str = ""
    location_label: str = ""
    process_id: str = ""
    process_label: str = ""
    inputs: list = field(default_factory=list)  # [{id, label}]
    outputs: list = field(default_factory=list)  # [{id, label}]


@dataclass
class CausalEdge:
    """A causal relation between two activities."""

    source_id: str
    target_id: str
    relation_id: str
    relation_label: str


@dataclass
class GoCamModel:
    """A parsed GO-CAM model with activities and edges."""

    model_id: str
    title: str
    activities: list = field(default_factory=list)  # [Activity]
    edges: list = field(default_factory=list)  # [CausalEdge]
    date_modified: str = ""
    organism: str = ""


# --- Networking ---


def fetch_url(url: str, cache_path: Path | None = None) -> str:
    """Fetch URL with optional file-based caching."""
    if cache_path and cache_path.exists():
        return cache_path.read_text()

    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        text = resp.read().decode("utf-8")

    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text)
    return text


def fetch_json(url: str, cache_path: Path | None = None) -> dict | list:
    """Fetch JSON from URL with retry and optional caching."""
    text = fetch_url(url, cache_path)
    return json.loads(text)


def fetch_json_with_retry(url: str, cache_path: Path | None = None, retries: int = 3) -> dict | list:
    """Fetch JSON with retry on transient failures."""
    if cache_path and cache_path.exists():
        return json.loads(cache_path.read_text())

    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                text = resp.read().decode("utf-8")
            if cache_path:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(text)
            return json.loads(text)
        except (urllib.error.URLError, ConnectionResetError, TimeoutError) as e:
            if attempt < retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"  Retry {attempt + 1} after {wait}s ({e})", file=sys.stderr)
                time.sleep(wait)
            else:
                raise


# --- Index operations ---


def load_index(refresh: bool = False) -> list[dict]:
    """Load the GO-CAM browser index (all models with gene metadata)."""
    cache_path = CACHE_DIR / "index.json"
    if refresh and cache_path.exists():
        cache_path.unlink()

    print("Loading GO-CAM model index...", file=sys.stderr)
    data = fetch_json(INDEX_URL, cache_path)
    print(f"  {len(data)} models in index", file=sys.stderr)
    return data


def search_models_by_genes(
    index: list[dict],
    gene_symbols: list[str],
    human_only: bool = True,
) -> list[dict]:
    """Find models containing any of the specified genes.

    Returns index entries (not full model data) sorted by number of matching
    genes (descending), so models involving more of the target genes come first.
    """
    gene_set = {g.upper() for g in gene_symbols}
    matches = []

    for entry in index:
        if human_only and entry.get("taxon") != HUMAN_TAXON:
            continue
        labels = [g.upper() for g in entry.get("enabled_by_gene_labels", [])]
        overlap = gene_set & set(labels)
        if overlap:
            matches.append((len(overlap), entry))

    matches.sort(key=lambda x: -x[0])
    return [entry for _, entry in matches]


# --- Model parsing ---


def parse_model(raw: dict) -> GoCamModel:
    """Parse the raw API JSON into a structured GoCamModel."""
    model_id = raw.get("id", "")

    # Build individual lookup: short_id -> {types, root_types}
    individuals = {}
    for ind in raw.get("individuals", []):
        short_id = ind["id"].split("/")[-1]
        types = []
        for t in ind.get("type", []):
            types.append({"id": t.get("id", ""), "label": t.get("label", "")})
        root_types = [t.get("label", "") for t in ind.get("root-type", [])]
        individuals[short_id] = {"types": types, "root_types": root_types}

    # First pass: identify activity nodes via enabled_by relations
    # activity_id -> Activity
    activities = {}
    gene_product_of = {}  # activity_id -> gene_product individual id

    for fact in raw.get("facts", []):
        subj = fact["subject"].split("/")[-1]
        obj = fact["object"].split("/")[-1]
        prop = fact.get("property", "")

        if prop == "RO:0002333":  # enabled_by
            subj_info = individuals.get(subj, {})
            obj_info = individuals.get(obj, {})

            mf_types = subj_info.get("types", [])
            gp_types = obj_info.get("types", [])

            act = Activity(node_id=subj)
            if mf_types:
                act.molecular_function_id = mf_types[0].get("id", "")
                act.molecular_function_label = mf_types[0].get("label", "")
            if gp_types:
                act.gene_id = gp_types[0].get("id", "")
                # Clean gene label: strip " Hsap" suffix
                label = gp_types[0].get("label", "")
                act.gene_symbol = label.replace(" Hsap", "").strip()

            activities[subj] = act
            gene_product_of[subj] = obj

    # Second pass: fill in locations, processes, inputs, outputs
    for fact in raw.get("facts", []):
        subj = fact["subject"].split("/")[-1]
        obj = fact["object"].split("/")[-1]
        prop = fact.get("property", "")

        if subj not in activities:
            continue

        obj_info = individuals.get(obj, {})
        obj_types = obj_info.get("types", [])
        if not obj_types:
            continue

        if prop == "BFO:0000066":  # occurs_in
            activities[subj].location_id = obj_types[0].get("id", "")
            activities[subj].location_label = obj_types[0].get("label", "")
        elif prop == "BFO:0000050":  # part_of
            activities[subj].process_id = obj_types[0].get("id", "")
            activities[subj].process_label = obj_types[0].get("label", "")
        elif prop == "RO:0002233":  # has_input
            activities[subj].inputs.append(
                {"id": obj_types[0].get("id", ""), "label": obj_types[0].get("label", "")}
            )
        elif prop == "RO:0002234":  # has_output
            activities[subj].outputs.append(
                {"id": obj_types[0].get("id", ""), "label": obj_types[0].get("label", "")}
            )

    # Third pass: causal edges between activities
    edges = []
    for fact in raw.get("facts", []):
        prop = fact.get("property", "")
        if prop not in CAUSAL_RELATIONS:
            continue

        subj = fact["subject"].split("/")[-1]
        obj = fact["object"].split("/")[-1]

        # Only include edges where both endpoints are recognized activities
        if subj in activities and obj in activities:
            edges.append(
                CausalEdge(
                    source_id=subj,
                    target_id=obj,
                    relation_id=prop,
                    relation_label=CAUSAL_RELATIONS[prop],
                )
            )

    # Get title from annotations
    title = ""
    for ann in raw.get("annotations", []):
        if ann.get("key") == "title":
            title = ann.get("value", "")
            break

    return GoCamModel(
        model_id=model_id,
        title=title,
        activities=list(activities.values()),
        edges=edges,
    )


# --- Output formatting ---


def _activity_id(act: Activity) -> str:
    """Generate a readable activity ID from gene symbol and function."""
    gene = act.gene_symbol.lower() if act.gene_symbol else "unknown"
    func = act.molecular_function_label.split(",")[0].strip()
    # Shorten common suffixes
    func = func.replace(" activity", "").replace(" ", "_").lower()
    return f"{gene}_{func}"


def model_to_yaml_dict(model: GoCamModel, target_genes: set[str] | None = None) -> dict:
    """Convert a parsed GoCamModel to a dict matching the pheno-CAM module format."""
    # Build activity ID mapping (node_id -> readable_id)
    id_map = {}
    id_counts = defaultdict(int)

    for act in model.activities:
        readable = _activity_id(act)
        id_counts[readable] += 1
        if id_counts[readable] > 1:
            readable = f"{readable}_{id_counts[readable]}"
        id_map[act.node_id] = readable

    activities_out = []
    for act in model.activities:
        entry = {
            "id": id_map[act.node_id],
            "gene": {"symbol": act.gene_symbol},
        }
        if act.gene_id:
            entry["gene"]["id"] = act.gene_id
        if act.molecular_function_id:
            entry["molecular_function"] = {
                "id": act.molecular_function_id,
                "label": act.molecular_function_label,
            }
        if act.location_id:
            entry["location"] = {
                "id": act.location_id,
                "label": act.location_label,
            }
        if act.process_id:
            entry["process"] = {
                "id": act.process_id,
                "label": act.process_label,
            }
        if act.inputs:
            entry["inputs"] = act.inputs
        if act.outputs:
            entry["outputs"] = act.outputs

        # Mark whether this gene is in the target set
        if target_genes and act.gene_symbol.upper() in target_genes:
            entry["target_gene"] = True

        activities_out.append(entry)

    edges_out = []
    for edge in model.edges:
        source_readable = id_map.get(edge.source_id, edge.source_id)
        target_readable = id_map.get(edge.target_id, edge.target_id)
        edges_out.append(
            {
                "source": source_readable,
                "target": target_readable,
                "relation": {
                    "id": edge.relation_id,
                    "label": edge.relation_label,
                },
            }
        )

    return {
        "source": {
            "type": "go_cam",
            "id": model.model_id,
            "name": model.title,
        },
        "activities": activities_out,
        "edges": edges_out,
    }


def build_output(
    models: list[GoCamModel],
    gene_symbols: list[str],
) -> dict:
    """Build the full output YAML structure for all fetched models."""
    target_genes = {g.upper() for g in gene_symbols}

    model_sections = []
    for model in models:
        section = model_to_yaml_dict(model, target_genes)
        model_sections.append(section)

    return {
        "gocam_fetch": {
            "query_genes": gene_symbols,
            "total_models": len(models),
            "organism": "Homo sapiens (NCBITaxon:9606)",
            "models": model_sections,
        }
    }


# --- Gene extraction from disorder YAML ---


def genes_from_disorder(path: str) -> list[str]:
    """Extract gene symbols from a disorder YAML file."""
    with open(path) as f:
        data = yaml.safe_load(f)

    genes = set()

    # Check genetic_basis entries
    for gb in data.get("genetic_basis", []):
        for gene in gb.get("genes", []):
            symbol = gene.get("gene_symbol") or gene.get("symbol", "")
            if symbol:
                genes.add(symbol)

    # Check pathophysiology for gene mentions
    for path_entry in data.get("pathophysiology", []):
        for gene in path_entry.get("genes", []):
            symbol = gene.get("gene_symbol") or gene.get("symbol", "")
            if symbol:
                genes.add(symbol)

    if not genes:
        print(f"Warning: no genes found in {path}", file=sys.stderr)

    return sorted(genes)


# --- Main ---


def main():
    parser = argparse.ArgumentParser(
        description="Fetch GO-CAM models for specified genes",
    )
    parser.add_argument(
        "genes",
        nargs="*",
        help="Gene symbols to search for (e.g., PTCH1 SMO SUFU)",
    )
    parser.add_argument(
        "--from-disorder",
        help="Extract genes from a disorder YAML file",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Only list matching models, don't fetch details",
    )
    parser.add_argument(
        "--refresh-index",
        action="store_true",
        help="Force refresh of the model index cache",
    )
    parser.add_argument(
        "--human-only",
        action="store_true",
        default=True,
        help="Only include human models (default: True)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file (default: stdout)",
    )
    args = parser.parse_args()

    # Collect gene symbols
    gene_symbols = list(args.genes) if args.genes else []
    if args.from_disorder:
        gene_symbols.extend(genes_from_disorder(args.from_disorder))

    if not gene_symbols:
        parser.error("No genes specified. Provide gene symbols or --from-disorder.")

    gene_symbols = sorted(set(gene_symbols))
    print(f"Searching for GO-CAM models involving: {', '.join(gene_symbols)}", file=sys.stderr)

    # Load index and search
    index = load_index(refresh=args.refresh_index)
    matches = search_models_by_genes(index, gene_symbols, human_only=args.human_only)

    if not matches:
        print("No GO-CAM models found for the specified genes.", file=sys.stderr)
        sys.exit(0)

    print(f"Found {len(matches)} matching models:", file=sys.stderr)
    for entry in matches:
        genes_in_model = entry.get("enabled_by_gene_labels", [])
        target_set = {g.upper() for g in gene_symbols}
        overlap = [g for g in genes_in_model if g.upper() in target_set]
        print(
            f"  {entry['id']}: {entry['title']} (matching: {', '.join(overlap)})",
            file=sys.stderr,
        )

    if args.list_only:
        return

    # Fetch full model data for each match
    models = []
    for i, entry in enumerate(matches):
        model_id = entry["id"]
        print(
            f"Fetching model {i + 1}/{len(matches)}: {model_id}...",
            file=sys.stderr,
        )

        cache_path = CACHE_DIR / f"{model_id.replace(':', '_')}.json"
        try:
            raw = fetch_json_with_retry(f"{MODEL_API}/{model_id}", cache_path)
        except Exception as e:
            print(f"  ERROR fetching {model_id}: {e}", file=sys.stderr)
            continue

        parsed = parse_model(raw)
        parsed.date_modified = entry.get("date_modified", "")
        parsed.organism = entry.get("taxon_label", "")
        models.append(parsed)

        # Brief rate limiting
        if i < len(matches) - 1:
            time.sleep(0.5)

    if not models:
        print("No models could be fetched.", file=sys.stderr)
        sys.exit(1)

    # Build and output YAML
    output = build_output(models, gene_symbols)
    yaml_str = yaml.dump(output, default_flow_style=False, sort_keys=False, allow_unicode=True)

    if args.output:
        Path(args.output).write_text(yaml_str)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(yaml_str)


if __name__ == "__main__":
    main()
