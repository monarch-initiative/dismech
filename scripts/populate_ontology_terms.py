#!/usr/bin/env python
"""
Script to populate disease_term and cell_types with ontology IDs using OAK.

This script:
1. Searches MONDO for each disease name to find the MONDO ID
2. Searches CL for each cell type preferred_term to find CL IDs
3. Updates the YAML files with the found terms
"""

import yaml
from pathlib import Path
from oaklib import get_adapter

# Initialize adapters
print("Loading ontology adapters...")
mondo = get_adapter("sqlite:obo:mondo")
cl = get_adapter("sqlite:obo:cl")
print("Adapters loaded.")


def search_mondo(disease_name: str) -> tuple[str, str] | None:
    """Search MONDO for a disease name and return (id, label) or None."""
    # Direct mappings for known problematic disease names (matching the actual 'name' field values)
    direct_mappings = {
        "ATTR_Amyloidosis": ("MONDO:0019155", "transthyretin amyloidosis"),
        "Acquired Immunodeficiency Syndrome": ("MONDO:0012268", "AIDS"),
        "Addison's Disease": ("MONDO:0015070", "Addison disease"),
        "Alhzeimer_Disease": ("MONDO:0004975", "Alzheimer disease"),
        "Axenfeld-Rieger_syndrome": ("MONDO:0019187", "Axenfeld-Rieger syndrome"),
        "Bardet-Biedl Syndrome": ("MONDO:0015229", "Bardet-Biedl syndrome"),
        "Crohn Disease": ("MONDO:0005011", "Crohn disease"),
        "Dengue": ("MONDO:0005502", "dengue disease"),
        "Ebola Virus Disease (EVD)": ("MONDO:0005737", "Ebola hemorrhagic fever"),
        "Ehlers-Danlos Syndrome": ("MONDO:0020066", "Ehlers-Danlos syndrome"),
        "Ehlers-Danlos Syndrome, COL5A1-related": ("MONDO:0007523", "classic Ehlers-Danlos syndrome"),
        "Familial Mediterranean Fever": ("MONDO:0018088", "familial Mediterranean fever"),
        "Fanconi_Anemia": ("MONDO:0019391", "Fanconi anemia"),
        "Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency": ("MONDO:0005775", "G6PD deficiency"),
        "Graves' Disease": ("MONDO:0005364", "Graves disease"),
        "Hepatitis B": ("MONDO:0005344", "hepatitis B virus infection"),
        "Hirschsprung Disease": ("MONDO:0018309", "Hirschsprung disease"),
        "Huntington's Disease": ("MONDO:0007739", "Huntington disease"),
        "Jeavons Syndrome": ("MONDO:0016532", "eyelid myoclonia with absences"),
        "Kawasaki Disease": ("MONDO:0012727", "Kawasaki disease"),
        "Non-Small Cell Lung Cancer": ("MONDO:0005233", "non-small cell lung carcinoma"),
        "Parvovirus B19 Infection": ("MONDO:0017801", "parvovirus B19 infection"),
        "Pick Disease": ("MONDO:0008243", "Pick disease"),
        "Primary_Tonsillar_Lymphoma": ("MONDO:0044884", "tonsillar lymphoma"),
        "Multisystem Inflammatory Syndrome in Children (MIS-C)": ("MONDO:0100163", "multisystem inflammatory syndrome in children"),
        "Transient Neonatal Pustular Melanosis": ("MONDO:0017440", "transient neonatal pustular melanosis"),
        "Type I Diabetes": ("MONDO:0005147", "type 1 diabetes mellitus"),
        "Asthma": ("MONDO:0004979", "asthma"),
    }

    # Check direct mapping first
    if disease_name in direct_mappings:
        return direct_mappings[disease_name]

    # Clean up the disease name for searching
    search_term = disease_name.replace("_", " ").replace("-", " ")

    # Try with common variations
    variations = [
        search_term,
        search_term.lower(),
        search_term.replace("'s", ""),
        search_term.replace("'s", ""),  # Different apostrophe
        search_term.replace(" Disease", ""),
        search_term.replace(" disease", ""),
        search_term.replace(" Syndrome", " syndrome"),
        search_term + " disease",
        search_term.lower() + " disease",
    ]

    for var in variations:
        results = list(mondo.basic_search(var))
        # Filter to only MONDO terms (not HP or other ontologies)
        mondo_results = [r for r in results if r.startswith("MONDO:")]
        if mondo_results:
            label = mondo.label(mondo_results[0])
            return (mondo_results[0], label)

    return None


def search_cl(cell_type_name: str) -> tuple[str, str] | None:
    """Search CL for a cell type name and return (id, label) or None."""
    # Common mappings for cell types (case-insensitive)
    mappings = {
        "neuron": "neuron",
        "neurons": "neuron",
        "microglia": "microglial cell",
        "astrocyte": "astrocyte",
        "astrocytes": "astrocyte",
        "mast cell": "mast cell",
        "eosinophil": "eosinophil",
        "t-lymphocyte": "T cell",
        "t lymphocyte": "T cell",
        "t cell": "T cell",
        "b cell": "B cell",
        "b-cell": "B cell",
        "b-lymphocyte": "B cell",
        "b lymphocyte": "B cell",
        "b-cell lymphocyte": "B cell",
        "t-cell lymphocyte": "T cell",
        "bronchial epithelial cell": "bronchial epithelial cell",
        "basophil": "basophil",
        "neutrophil": "neutrophil",
        "smooth muscle cell": "smooth muscle cell",
        "smooth muscle cells": "smooth muscle cell",
        "goblet cell": "goblet cell",
        "mucosal epithelial cell": "epithelial cell of mucosa",
        "fibroblast": "fibroblast",
        "endothelial cell": "endothelial cell",
        "endothelial cells": "endothelial cell",
        "pericyte": "pericyte",
        "pericytes": "pericyte",
        "cardiomyocyte": "cardiac muscle cell",
        "cardiac fibroblast": "cardiac fibroblast",
        "cd4 t-lymphocyte": "CD4-positive, alpha-beta T cell",
        "cd4+ t cell": "CD4-positive, alpha-beta T cell",
        "cd8+ t lymphocyte": "CD8-positive, alpha-beta T cell",
        "cd8+ t cell": "CD8-positive, alpha-beta T cell",
        "th17 cell": "T-helper 17 cell",
        "synoviocyte": "synovial cell",
        "nk cell": "natural killer cell",
        "memory b cell": "memory B cell",
        "pancreatic islet beta cell": "type B pancreatic cell",
        "excitatory glutamatergic neuron": "glutamatergic neuron",
    }

    # Try mapped term first (case-insensitive lookup)
    search_key = cell_type_name.lower()
    if search_key in mappings:
        search_term = mappings[search_key]
    else:
        # Clean up the cell type name for searching
        search_term = cell_type_name.lower()
        if search_term.endswith("s") and not search_term.endswith("ss"):
            search_term = search_term[:-1]  # Remove trailing 's' for plurals

    results = list(cl.basic_search(search_term))
    # Filter to only CL terms
    cl_results = [r for r in results if r.startswith("CL:")]
    if cl_results:
        label = cl.label(cl_results[0])
        return (cl_results[0], label)

    # Try original term
    results = list(cl.basic_search(cell_type_name))
    cl_results = [r for r in results if r.startswith("CL:")]
    if cl_results:
        label = cl.label(cl_results[0])
        return (cl_results[0], label)

    return None


def process_file(file_path: Path) -> dict:
    """Process a single KB file and return update statistics."""
    stats = {"disease_term_added": False, "cell_types_updated": 0, "file": str(file_path.name)}

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    if not data:
        return stats

    modified = False

    # Add disease_term if missing
    if "disease_term" not in data or data.get("disease_term") is None:
        disease_name = data.get("name", "")
        if disease_name:
            result = search_mondo(disease_name)
            if result:
                mondo_id, label = result
                data["disease_term"] = {
                    "preferred_term": label,
                    "term": {
                        "id": mondo_id,
                        "label": label
                    }
                }
                stats["disease_term_added"] = True
                modified = True
                print(f"  Added disease_term: {mondo_id} ({label})")
            else:
                print(f"  WARNING: Could not find MONDO term for '{disease_name}'")

    # Process cell_types in pathophysiology
    if "pathophysiology" in data and isinstance(data["pathophysiology"], list):
        for patho in data["pathophysiology"]:
            if "cell_types" in patho and isinstance(patho["cell_types"], list):
                for cell_type in patho["cell_types"]:
                    if isinstance(cell_type, dict) and "preferred_term" in cell_type:
                        # Only add term if not already present
                        if "term" not in cell_type or cell_type.get("term") is None:
                            preferred = cell_type["preferred_term"]
                            result = search_cl(preferred)
                            if result:
                                cl_id, label = result
                                cell_type["term"] = {
                                    "id": cl_id,
                                    "label": label
                                }
                                stats["cell_types_updated"] += 1
                                modified = True
                                print(f"    Added cell_type term: {cl_id} ({label}) for '{preferred}'")
                            else:
                                print(f"    WARNING: Could not find CL term for '{preferred}'")

    if modified:
        # Preserve order and formatting
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return stats


def main():
    kb_dir = Path(__file__).parent.parent / "kb" / "disorders"
    files = sorted(kb_dir.glob("*.yaml"))

    print(f"Found {len(files)} KB files to process.\n")

    total_stats = {
        "disease_terms_added": 0,
        "cell_types_updated": 0,
        "files_processed": 0,
        "files_modified": 0,
    }

    for file_path in files:
        print(f"Processing: {file_path.name}")
        stats = process_file(file_path)
        total_stats["files_processed"] += 1

        if stats["disease_term_added"] or stats["cell_types_updated"] > 0:
            total_stats["files_modified"] += 1

        if stats["disease_term_added"]:
            total_stats["disease_terms_added"] += 1

        total_stats["cell_types_updated"] += stats["cell_types_updated"]

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Files processed: {total_stats['files_processed']}")
    print(f"Files modified: {total_stats['files_modified']}")
    print(f"Disease terms added: {total_stats['disease_terms_added']}")
    print(f"Cell types updated: {total_stats['cell_types_updated']}")


if __name__ == "__main__":
    main()
