#!/usr/bin/env python
"""
Script to populate phenotype_term fields with HP IDs using OAK.

This script:
1. Searches HP for each phenotype name to find the HP ID
2. Updates the YAML files with the found terms
"""

import yaml
from pathlib import Path
from oaklib import get_adapter

# Initialize adapters
print("Loading HP ontology adapter...")
hp = get_adapter("sqlite:obo:hp")
print("Adapter loaded.")


def search_hp(phenotype_name: str) -> tuple[str, str] | None:
    """Search HP for a phenotype name and return (id, label) or None."""
    # Common mappings for phenotype names (case-insensitive)
    mappings = {
        # Cognitive/Neurological
        "memory loss": "Memory impairment",
        "confusion": "Confusion",
        "disorientation": "Disorientation",
        "dementia": "Dementia",
        "cognitive decline": "Cognitive impairment",
        "language impairment": "Impaired language",
        "aphasia": "Aphasia",
        "apraxia": "Apraxia",
        "agnosia": "Agnosia",
        "executive dysfunction": "Executive dysfunction",
        "behavioral changes": "Behavioral abnormality",
        "depression": "Depression",
        "anxiety": "Anxiety",
        "apathy": "Apathy",
        "psychosis": "Psychosis",
        "hallucinations": "Hallucinations",
        "delusions": "Delusions",
        "seizures": "Seizures",
        "tremor": "Tremor",
        "ataxia": "Ataxia",
        "dystonia": "Dystonia",
        "parkinsonism": "Parkinsonism",
        "headache": "Headache",

        # Gastrointestinal
        "abdominal pain": "Abdominal pain",
        "diarrhea": "Diarrhea",
        "constipation": "Constipation",
        "nausea": "Nausea",
        "vomiting": "Vomiting",
        "bloating": "Abdominal distention",
        "weight loss": "Weight loss",

        # Respiratory
        "cough": "Cough",
        "dyspnea": "Dyspnea",
        "wheezing": "Wheezing",
        "shortness of breath": "Dyspnea",
        "bronchospasm": "Bronchospasm",

        # Cardiovascular
        "chest pain": "Chest pain",
        "palpitations": "Palpitations",
        "hypertension": "Hypertension",
        "hypotension": "Hypotension",
        "tachycardia": "Tachycardia",
        "bradycardia": "Bradycardia",
        "arrhythmia": "Arrhythmia",
        "heart failure": "Heart failure",
        "cardiomegaly": "Cardiomegaly",

        # Musculoskeletal
        "joint pain": "Arthralgia",
        "arthralgia": "Arthralgia",
        "arthritis": "Arthritis",
        "myalgia": "Myalgia",
        "muscle weakness": "Muscle weakness",
        "muscle wasting": "Skeletal muscle atrophy",
        "fatigue": "Fatigue",

        # Dermatological
        "rash": "Skin rash",
        "pruritus": "Pruritus",
        "urticaria": "Urticaria",
        "erythema": "Erythema",

        # Ocular
        "visual impairment": "Visual impairment",
        "vision loss": "Visual impairment",
        "blindness": "Visual impairment",
        "photophobia": "Photophobia",
        "uveitis": "Uveitis",

        # Systemic
        "fever": "Fever",
        "malaise": "Malaise",
        "night sweats": "Night sweats",

        # Other common phenotypes
        "anemia": "Anemia",
        "thrombocytopenia": "Thrombocytopenia",
        "leukopenia": "Leukopenia",
        "lymphadenopathy": "Lymphadenopathy",
        "splenomegaly": "Splenomegaly",
        "hepatomegaly": "Hepatomegaly",
        "jaundice": "Jaundice",
        "edema": "Edema",
        "ascites": "Ascites",
    }

    # Try mapped term first (case-insensitive lookup)
    search_key = phenotype_name.lower()
    if search_key in mappings:
        search_term = mappings[search_key]
    else:
        search_term = phenotype_name

    results = list(hp.basic_search(search_term))
    # Filter to only HP terms
    hp_results = [r for r in results if r.startswith("HP:")]
    if hp_results:
        label = hp.label(hp_results[0])
        return (hp_results[0], label)

    # Try original term
    results = list(hp.basic_search(phenotype_name))
    hp_results = [r for r in results if r.startswith("HP:")]
    if hp_results:
        label = hp.label(hp_results[0])
        return (hp_results[0], label)

    return None


def process_file(file_path: Path) -> dict:
    """Process a single KB file and return update statistics."""
    stats = {"phenotypes_updated": 0, "file": str(file_path.name)}

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    if not data:
        return stats

    modified = False

    # Process phenotypes
    if "phenotypes" in data and isinstance(data["phenotypes"], list):
        for phenotype in data["phenotypes"]:
            if isinstance(phenotype, dict) and "name" in phenotype:
                # Only add phenotype_term if not already present
                if "phenotype_term" not in phenotype or phenotype.get("phenotype_term") is None:
                    name = phenotype["name"]
                    result = search_hp(name)
                    if result:
                        hp_id, label = result
                        phenotype["phenotype_term"] = {
                            "preferred_term": label,
                            "term": {
                                "id": hp_id,
                                "label": label
                            }
                        }
                        stats["phenotypes_updated"] += 1
                        modified = True
                        print(f"    Added phenotype_term: {hp_id} ({label}) for '{name}'")
                    else:
                        print(f"    WARNING: Could not find HP term for '{name}'")

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
        "phenotypes_updated": 0,
        "files_processed": 0,
        "files_modified": 0,
    }

    for file_path in files:
        print(f"Processing: {file_path.name}")
        stats = process_file(file_path)
        total_stats["files_processed"] += 1

        if stats["phenotypes_updated"] > 0:
            total_stats["files_modified"] += 1

        total_stats["phenotypes_updated"] += stats["phenotypes_updated"]

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Files processed: {total_stats['files_processed']}")
    print(f"Files modified: {total_stats['files_modified']}")
    print(f"Phenotypes updated: {total_stats['phenotypes_updated']}")


if __name__ == "__main__":
    main()
