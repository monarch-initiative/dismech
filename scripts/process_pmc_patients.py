#!/usr/bin/env python3
"""
Process PMC-Patients JSON and create test case YAML files.

Each YAML file contains:
- Original metadata from PMC-Patients
- A diagnosis term with MONDO ID
- A masked case description (diagnosis removed) for testing
"""

import json
import re
import yaml
from pathlib import Path
from typing import Optional
import subprocess


def search_mondo(query: str) -> Optional[dict]:
    """Search MONDO for a disease term using OAK."""
    try:
        result = subprocess.run(
            ["uv", "run", "runoak", "-i", "sqlite:obo:mondo", "search", query],
            capture_output=True,
            text=True,
            timeout=60,
        )
        # Check both stdout and stderr (OAK sometimes puts results in stdout with warnings)
        output = result.stdout + result.stderr
        if "MONDO:" in output:
            # Parse first MONDO result - format is "MONDO:0000001 ! Disease Name"
            for line in output.split("\n"):
                if "MONDO:" in line and "!" in line:
                    match = re.match(r".*(MONDO:\d+)\s+!\s+(.+)", line.strip())
                    if match:
                        return {"id": match.group(1), "label": match.group(2)}
    except subprocess.TimeoutExpired:
        print("  OAK search timed out")
    except Exception as e:
        print(f"  OAK search failed: {e}")
    return None


def extract_diagnosis_from_title(title: str) -> Optional[str]:
    """Extract a disease/diagnosis from the title."""
    # Common patterns
    patterns = [
        r"(?:case of|presenting with|diagnosed with|suffering from)\s+([A-Za-z\s\-']+?)(?:\s+(?:in|with|after|during|following|mimicking|presenting)|\s*$|:)",
        r"^([A-Za-z\s\-']+?)\s+(?:in a|in an|after|presenting|following|mimicking)",
        r"([A-Za-z\s\-]+(?:syndrome|disease|carcinoma|lymphoma|leukemia|sarcoma|cancer|tumor|deficiency|disorder|infection))",
    ]

    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            diagnosis = match.group(1).strip()
            # Clean up
            diagnosis = re.sub(r"^(a|an|the)\s+", "", diagnosis, flags=re.IGNORECASE)
            if len(diagnosis) > 3 and len(diagnosis) < 100:
                return diagnosis
    return None


def mask_diagnosis(text: str, diagnosis: str, mondo_label: str) -> str:
    """Mask the diagnosis in the case description."""
    masked = text

    # Mask variations of the diagnosis
    terms_to_mask = [diagnosis, mondo_label]

    # Add common abbreviations/variations
    for term in list(terms_to_mask):
        # Add plural/singular
        if term.endswith("s"):
            terms_to_mask.append(term[:-1])
        else:
            terms_to_mask.append(term + "s")

    for term in terms_to_mask:
        if term and len(term) > 2:
            # Case-insensitive replacement
            pattern = re.compile(re.escape(term), re.IGNORECASE)
            masked = pattern.sub("[DIAGNOSIS]", masked)

    return masked


def create_case_yaml(entry: dict, mondo_term: dict, output_dir: Path) -> bool:
    """Create a YAML case file."""
    patient_uid = entry["patient_uid"]
    filename = f"{patient_uid}.yaml"

    # Create masked description
    masked_patient = mask_diagnosis(
        entry["patient"],
        extract_diagnosis_from_title(entry["title"]) or "",
        mondo_term["label"],
    )

    case = {
        "patient_uid": patient_uid,
        "patient_id": entry["patient_id"],
        "pmid": entry["PMID"],
        "source_file": entry["file_path"],
        "title": entry["title"],
        "age": entry.get("age"),
        "gender": entry.get("gender"),
        "pub_date": entry.get("pub_date"),
        "diagnosis": {"term": {"id": mondo_term["id"], "label": mondo_term["label"]}},
        "original_case_description": entry["patient"],
        "masked_case_description": masked_patient,
    }

    output_path = output_dir / filename
    with open(output_path, "w") as f:
        yaml.dump(
            case,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=100,
        )

    return True


def main():
    input_file = Path("projects/PHENOPACKETS/files/pmc-patients-data/PMC-Patients.json")
    output_dir = Path("cases/pmc-patients")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {input_file}...")
    with open(input_file) as f:
        data = json.load(f)

    print(f"Loaded {len(data)} entries")

    # Process entries - aim for ~300 good cases
    processed = 0
    failed = 0
    target = 300

    for i, entry in enumerate(data):
        if processed >= target:
            break

        # Extract diagnosis from title
        diagnosis = extract_diagnosis_from_title(entry["title"])
        if not diagnosis:
            continue

        print(f"\n[{i}] Title: {entry['title'][:60]}...")
        print(f"  Extracted diagnosis: {diagnosis}")

        # Search MONDO
        mondo_term = search_mondo(diagnosis)
        if not mondo_term:
            print("  No MONDO match found")
            failed += 1
            continue

        print(f"  MONDO: {mondo_term['id']} - {mondo_term['label']}")

        # Create YAML
        if create_case_yaml(entry, mondo_term, output_dir):
            processed += 1
            print(f"  Created case {processed}/{target}")

    print(f"\n\nDone! Created {processed} cases, {failed} failed MONDO lookup")


if __name__ == "__main__":
    main()
