"""
Browser data exporter for dismech.

Transforms disorder YAML files into JSON for the faceted search browser.
Each disorder becomes one record with aggregated searchable fields.
"""

import json
from pathlib import Path
from typing import Any

import yaml
from oaklib import get_adapter

from dismech.graph import build_causal_graph

# Direct children of HP:0000118 (Phenotypic abnormality) — the broad phenotype categories.
# Keys match PhenotypeCategoryEnum permissible_value keys in the schema.
HPO_TOP_LEVEL_CATEGORIES: dict[str, str] = {
    "HP:0001871": "Blood",
    "HP:0000769": "Breast",
    "HP:0001626": "Cardiovascular",
    "HP:0025031": "Digestive",
    "HP:0000598": "Ear",
    "HP:0000818": "Endocrine",
    "HP:0000478": "Eye",
    "HP:0000119": "Genitourinary",
    "HP:0000152": "Head and Neck",
    "HP:0002715": "Immune",
    "HP:0001574": "Integument",
    "HP:0040064": "Limbs",
    "HP:0001939": "Metabolism",
    "HP:0033127": "Musculoskeletal",
    "HP:0000707": "Nervous System",
    "HP:0001197": "Prenatal and Birth",
    "HP:0002086": "Respiratory",
    "HP:0045027": "Thoracic Cavity",
    "HP:0001608": "Voice",
    "HP:0025354": "Cellular",
    "HP:0025142": "Constitutional",
    "HP:0001507": "Growth",
    "HP:0002664": "Neoplasm",
}
_HPO_TOP_LEVEL_IDS = set(HPO_TOP_LEVEL_CATEGORIES.keys())


class HPOCategoryResolver:
    """Resolve HP term IDs to their broad top-level phenotype categories."""

    def __init__(self):
        self._adapter = None
        self._cache: dict[str, list[str]] = {}

    def _get_adapter(self):
        if self._adapter is None:
            self._adapter = get_adapter("sqlite:obo:hp")
        return self._adapter

    def resolve(self, hp_id: str) -> list[str]:
        """Return the top-level HPO category labels for a given HP term ID."""
        if hp_id in self._cache:
            return self._cache[hp_id]

        # If the term itself is a top-level category, return it directly
        if hp_id in _HPO_TOP_LEVEL_IDS:
            result = [HPO_TOP_LEVEL_CATEGORIES[hp_id]]
            self._cache[hp_id] = result
            return result

        adapter = self._get_adapter()
        ancestors = set(adapter.ancestors(
            hp_id, predicates=["rdfs:subClassOf"]))
        hits = ancestors & _HPO_TOP_LEVEL_IDS
        result = sorted(HPO_TOP_LEVEL_CATEGORIES[h] for h in hits)
        self._cache[hp_id] = result
        return result


def _build_adjacency(edges: list[tuple[str, str]]) -> tuple[dict[str, list[str]], set[str]]:
    adj: dict[str, list[str]] = {}
    nodes: set[str] = set()
    for source, target in edges:
        nodes.add(source)
        nodes.add(target)
        adj.setdefault(source, []).append(target)
    for node in nodes:
        adj.setdefault(node, [])
    return adj, nodes


def _topological_order(adj: dict[str, list[str]], nodes: set[str]) -> list[str] | None:
    indegree = {node: 0 for node in nodes}
    for source, targets in adj.items():
        for target in targets:
            indegree[target] += 1

    queue = [node for node, degree in indegree.items() if degree == 0]
    order: list[str] = []

    while queue:
        node = queue.pop()
        order.append(node)
        for target in adj.get(node, []):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

    if len(order) != len(nodes):
        return None
    return order


def _longest_simple_path_length(adj: dict[str, list[str]], nodes: set[str]) -> int:
    def dfs(node: str, visited: set[str]) -> int:
        visited.add(node)
        best = 0
        for target in adj.get(node, []):
            if target not in visited:
                best = max(best, 1 + dfs(target, visited))
        visited.remove(node)
        return best

    best = 0
    for node in nodes:
        best = max(best, dfs(node, set()))
    return best


def _longest_path_length(edges: list[tuple[str, str]]) -> int:
    if not edges:
        return 0

    adj, nodes = _build_adjacency(edges)
    order = _topological_order(adj, nodes)
    if order is None:
        return _longest_simple_path_length(adj, nodes)

    distances = {node: 0 for node in nodes}
    for node in order:
        for target in adj.get(node, []):
            candidate = distances[node] + 1
            if candidate > distances[target]:
                distances[target] = candidate

    return max(distances.values()) if distances else 0


def slugify(name: str) -> str:
    """Convert a disorder name to a filename-safe slug."""
    return name.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')


class BrowserExporter:
    """Export disorder data to browser-friendly JSON format."""

    def __init__(self):
        self._hpo_resolver = HPOCategoryResolver()

    def load_disorder(self, file_path: Path) -> dict[str, Any]:
        """Load a single disorder YAML file."""
        with open(file_path) as f:
            return yaml.safe_load(f)

    def extract_disorder(self, disorder: dict[str, Any], source_file: str) -> dict[str, Any]:
        """
        Extract a disorder into a single searchable record.
        """
        name = disorder.get("name", "Unknown")
        category = disorder.get("category", "")
        parents = disorder.get("parents", [])

        # Disease term
        disease_id = None
        if disorder.get("disease_term") and disorder["disease_term"].get("term"):
            disease_id = disorder["disease_term"]["term"].get("id")

        # Subtypes
        subtypes = [s.get("name", "") for s in (
            disorder.get("has_subtypes") or []) if s.get("name")]

        # Pathophysiology
        pathophysiology_names = []
        cell_types = []
        cell_type_ids = []
        biological_processes = []

        for patho in (disorder.get("pathophysiology") or []):
            if patho.get("name"):
                pathophysiology_names.append(patho["name"])
            for ct in (patho.get("cell_types") or []):
                ct_name = ct.get("preferred_term") or ct.get(
                    "term", {}).get("label", "")
                if ct_name and ct_name not in cell_types:
                    cell_types.append(ct_name)
                ct_id = ct.get("term", {}).get("id")
                if ct_id and ct_id not in cell_type_ids:
                    cell_type_ids.append(ct_id)
            for bp in (patho.get("biological_processes") or []):
                bp_name = bp.get("preferred_term", "")
                if bp_name and bp_name not in biological_processes:
                    biological_processes.append(bp_name)

        # Phenotypes
        phenotype_names = []
        phenotype_categories = []
        phenotype_ids = []
        frequencies = []
        hpo_broad_categories: set[str] = set()

        for pheno in (disorder.get("phenotypes") or []):
            if pheno.get("name"):
                phenotype_names.append(pheno["name"])
            if pheno.get("category") and pheno["category"] not in phenotype_categories:
                phenotype_categories.append(pheno["category"])
            freq = pheno.get("frequency")
            if freq and str(freq) not in frequencies:
                frequencies.append(str(freq))
            if pheno.get("phenotype_term") and pheno["phenotype_term"].get("term"):
                hp_id = pheno["phenotype_term"]["term"].get("id")
                if hp_id and hp_id not in phenotype_ids:
                    phenotype_ids.append(hp_id)
                if hp_id:
                    hpo_broad_categories.update(
                        self._hpo_resolver.resolve(hp_id))

        # Genetic associations
        genes = [g.get("name", "")
                 for g in (disorder.get("genetic") or []) if g.get("name")]

        # Treatments
        treatments = [t.get("name", "") for t in (
            disorder.get("treatments") or []) if t.get("name")]

        # Environmental factors
        environmental = [e.get("name", "") for e in (
            disorder.get("environmental") or []) if e.get("name")]

        # Biochemical markers
        biochemical = [b.get("name", "") for b in (
            disorder.get("biochemical") or []) if b.get("name")]

        # Build description from various sources
        description = disorder.get("description", "")
        if not description and disorder.get("pathophysiology"):
            # Use first pathophysiology description
            for p in disorder["pathophysiology"]:
                if p.get("description"):
                    description = p["description"]
                    break

        graph = build_causal_graph(disorder)
        causal_edges = len(graph.edges)
        causal_longest_path = _longest_path_length(
            [(edge.source, edge.target) for edge in graph.edges])

        return {
            "name": name,
            "disease_id": disease_id,
            "category": category,
            "parents": parents,
            "creation_date": disorder.get("creation_date"),
            "updated_date": disorder.get("updated_date"),
            "subtypes": subtypes,
            "description": description,
            "pathophysiology": pathophysiology_names,
            "cell_types": cell_types,
            "cell_type_ids": cell_type_ids,
            "biological_processes": biological_processes,
            "phenotypes": phenotype_names,
            "phenotype_categories": phenotype_categories,
            "phenotype_hpo_categories": sorted(hpo_broad_categories),
            "phenotype_ids": phenotype_ids,
            "frequencies": frequencies,
            "genes": genes,
            "treatments": treatments,
            "environmental": environmental,
            "biochemical": biochemical,
            "source_file": source_file,
            "page_url": f"../pages/disorders/{slugify(name)}.html",
            # Counts for display
            "num_phenotypes": len(phenotype_names),
            "num_pathophysiology": len(pathophysiology_names),
            "num_genes": len(genes),
            "num_treatments": len(treatments),
            "causal_graph_edges": str(causal_edges),
            "causal_graph_longest_path": str(causal_longest_path),
        }

    def _write_hpo_category_cache(self, output_path: Path) -> None:
        """Write the accumulated HP-to-category cache as JSON for use by the renderer."""
        cache_path = output_path.parent / "hpo_category_cache.json"
        with open(cache_path, "w") as f:
            json.dump(self._hpo_resolver._cache, f, indent=2, sort_keys=True)
        print(
            f"Wrote HPO category cache ({len(self._hpo_resolver._cache)} terms) to {cache_path}")

    def export_to_json(self, disorder_files: list[Path], output_path: Path) -> None:
        """Export all disorder files to a single JSON file."""
        records = []
        for file_path in disorder_files:
            disorder = self.load_disorder(file_path)
            record = self.extract_disorder(disorder, file_path.name)
            records.append(record)

        with open(output_path, "w") as f:
            json.dump(records, f, indent=2)

        self._write_hpo_category_cache(output_path)
        print(f"Exported {len(records)} disorders to {output_path}")

    def export_to_js(self, disorder_files: list[Path], output_path: Path) -> None:
        """Export all disorder files to a JavaScript data file."""
        records = []
        for file_path in disorder_files:
            disorder = self.load_disorder(file_path)
            record = self.extract_disorder(disorder, file_path.name)
            records.append(record)

        js_content = f"window.searchData = {json.dumps(records, indent=2)};\n"
        js_content += "window.dispatchEvent(new Event('searchDataReady'));\n"

        with open(output_path, "w") as f:
            f.write(js_content)

        self._write_hpo_category_cache(output_path)
        print(f"Exported {len(records)} disorders to {output_path}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Export disorder data for browser")
    parser.add_argument("--input-dir", "-i", default="kb/disorders",
                        help="Input directory with YAML files")
    parser.add_argument(
        "--output", "-o", default="app/data.js", help="Output file path")
    parser.add_argument(
        "--format", "-f", choices=["json", "js"], default="js", help="Output format")

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_path = Path(args.output)

    disorder_files = [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]

    exporter = BrowserExporter()
    if args.format == "json":
        exporter.export_to_json(disorder_files, output_path)
    else:
        exporter.export_to_js(disorder_files, output_path)


if __name__ == "__main__":
    main()
