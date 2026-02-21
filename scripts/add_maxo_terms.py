#!/usr/bin/env python3
"""
Add MAXO treatment terms to all disorder files.
"""

import re
from pathlib import Path
import yaml


# Mapping from treatment keywords to MAXO terms
# Order matters: more specific patterns should come first
MAXO_MAPPINGS = [
    # Specific therapies first
    (r"gene\s*therapy", {"id": "MAXO:0001001", "label": "gene therapy"}),
    (r"genetic\s*counseling", {"id": "MAXO:0000079", "label": "genetic counseling"}),
    (r"physical\s*therap", {"id": "MAXO:0000011", "label": "physical therapy"}),
    (r"radiation\s*therap", {"id": "MAXO:0000014", "label": "radiation therapy"}),
    (r"chemotherap", {"id": "MAXO:0000647", "label": "chemotherapy"}),
    (r"vaccinat", {"id": "MAXO:0001017", "label": "vaccination"}),
    (r"blood\s*transfusion", {"id": "MAXO:0000756", "label": "blood transfusion"}),
    (r"dialysis", {"id": "MAXO:0000601", "label": "renal dialysis"}),
    (r"insulin", {"id": "MAXO:0000259", "label": "insulin treatment"}),
    (r"pain\s*manage", {"id": "MAXO:0000457", "label": "pain management"}),
    # Transplants
    (r"organ\s*transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    (r"liver\s*transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    (r"kidney\s*transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    (r"heart\s*transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    (r"lung\s*transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    (r"transplant", {"id": "MAXO:0010039", "label": "organ transplantation"}),
    # Diet and lifestyle
    (r"diet", {"id": "MAXO:0000088", "label": "dietary intervention"}),
    (r"nutrition", {"id": "MAXO:0000088", "label": "dietary intervention"}),
    (r"lifestyle\s*modif", {"id": "MAXO:0000088", "label": "dietary intervention"}),
    # Surgeries
    (r"surgical", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"surgery", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Supportive/palliative care
    (r"supportive\s*care", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"supportive\s*therap", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"palliative", {"id": "MAXO:0000021", "label": "palliative care"}),
    (r"symptom\s*manage", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"symptomatic", {"id": "MAXO:0000950", "label": "supportive care"}),
    # Drug therapies - generic
    (r"pharmacother", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"medication", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    # Specific drug classes
    (r"beta.?block", {"id": "MAXO:0000186", "label": "beta adrenergic agent therapy"}),
    (
        r"bronchodilat",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    (
        r"inhaled\s*corticosteroid",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    (r"corticosteroid", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"steroid", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"immuno.?suppress", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"antibiotic", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"antiviral", {"id": "MAXO:0000168", "label": "antiviral agent therapy"}),
    (r"antiretroviral", {"id": "MAXO:0000573", "label": "antiretroviral therapy"}),
    (r"antipsychotic", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (
        r"antihypertensive",
        {"id": "MAXO:0000181", "label": "cardiovascular agent therapy"},
    ),
    (r"anticoagul", {"id": "MAXO:0000181", "label": "cardiovascular agent therapy"}),
    (r"aspirin", {"id": "MAXO:0000181", "label": "cardiovascular agent therapy"}),
    (r"statin", {"id": "MAXO:0000189", "label": "dyslipidemic agent therapy"}),
    (r"IVIG|immunoglobulin", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"biologic", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"targeted\s*therap", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"immunother", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    # Hormones
    (r"growth\s*hormone", {"id": "MAXO:0000283", "label": "hormone modifying therapy"}),
    (r"hormone", {"id": "MAXO:0000283", "label": "hormone modifying therapy"}),
    (r"thyroid", {"id": "MAXO:0000283", "label": "hormone modifying therapy"}),
    # Respiratory
    (r"oxygen\s*therap", {"id": "MAXO:0000503", "label": "artificial respiration"}),
    (r"oxygen", {"id": "MAXO:0000503", "label": "artificial respiration"}),
    (r"ventilat", {"id": "MAXO:0000503", "label": "artificial respiration"}),
    (
        r"airway\s*clearance",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    # Rehabilitation and support
    (r"occupational\s*therap", {"id": "MAXO:0000011", "label": "physical therapy"}),
    (r"speech\s*therap", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"behavioral", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"cognitive", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"psychotherap", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"counseling", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"educational", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    # Orthopedic
    (r"orthotic", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"orthoped", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Fluid therapy
    (r"rehydrat", {"id": "MAXO:0000458", "label": "hydrotherapy"}),
    (
        r"fluid\s*(resuscitation|replacement|therap)",
        {"id": "MAXO:0000458", "label": "hydrotherapy"},
    ),
    # More hormone therapies
    (
        r"testosterone\s*replacement",
        {"id": "MAXO:0000283", "label": "hormone modifying therapy"},
    ),
    (
        r"estrogen\s*replacement",
        {"id": "MAXO:0000283", "label": "hormone modifying therapy"},
    ),
    (
        r"glucocorticoid\s*replacement",
        {"id": "MAXO:0000283", "label": "hormone modifying therapy"},
    ),
    (
        r"mineralocorticoid\s*replacement",
        {"id": "MAXO:0000283", "label": "hormone modifying therapy"},
    ),
    (r"androgen", {"id": "MAXO:0000283", "label": "hormone modifying therapy"}),
    (
        r"replacement\s*therap",
        {"id": "MAXO:0000283", "label": "hormone modifying therapy"},
    ),
    # More respiratory
    (
        r"beta.?agonist",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    (
        r"leukotriene",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    (
        r"anti.?ig.?e",
        {"id": "MAXO:0000312", "label": "respiratory tract agent therapy"},
    ),
    (r"pulmonary\s*rehab", {"id": "MAXO:0000011", "label": "physical therapy"}),
    (r"photother", {"id": "MAXO:0000014", "label": "radiation therapy"}),
    # More cardiovascular
    (r"ACE\s*inhibitor", {"id": "MAXO:0000652", "label": "ACE inhibitor therapy"}),
    (r"ARB", {"id": "MAXO:0000181", "label": "cardiovascular agent therapy"}),
    (r"diuretic", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (
        r"calcium\s*channel\s*block",
        {"id": "MAXO:0000434", "label": "calcium channel blocking agent therapy"},
    ),
    (r"ICD|cardioverter", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"ablation", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Blood products
    (r"platelet\s*transfus", {"id": "MAXO:0000756", "label": "blood transfusion"}),
    (r"transfusion", {"id": "MAXO:0000756", "label": "blood transfusion"}),
    # Specific drugs as pharmacotherapy
    (r"colchicine", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"NSAID", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"DMARD", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"interferon", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"anti.?IL", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"tetrabenazine", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"SSRI", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"valproic", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"ethosuximide", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"levetiracetam", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"tafamidis", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"patisiran", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"inotersen", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"aminosalicylate", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"immunomodulator", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"phosphodiesterase", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"monobenzone", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    # Behavioral and avoidance
    (r"avoidance", {"id": "MAXO:0001014", "label": "medical action avoidance"}),
    (r"smoking\s*cessation", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"social\s*skill", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"vocational", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"caregiver", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"isolation", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    (r"infection\s*control", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    # Wound and skin
    (r"wound\s*care", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"skin\s*graft", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Procedures
    (r"pull.?through", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"ostomy", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"nerve\s*stimulants", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"VNS", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    (r"fertility\s*treatment", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Supplements
    (r"supplement", {"id": "MAXO:0000106", "label": "nutritional supplementation"}),
    (r"zinc", {"id": "MAXO:0000106", "label": "nutritional supplementation"}),
    (
        r"salt\s*supplement",
        {"id": "MAXO:0000106", "label": "nutritional supplementation"},
    ),
    # Monitoring/surveillance - no good MAXO term exists, skip these
    # (Monitoring is not really a "medical action" in MAXO)
    # (r'surveillance', ...),
    # (r'monitoring', ...),
    # (r'screening', ...),
    # Devices
    (r"hearing\s*aid", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"medical\s*id", {"id": "MAXO:0000950", "label": "supportive care"}),
    (r"glasses", {"id": "MAXO:0000950", "label": "supportive care"}),
    # Dental
    (r"dental", {"id": "MAXO:0000004", "label": "surgical procedure"}),
    # Pain
    (r"pain\s*relief", {"id": "MAXO:0000457", "label": "pain management"}),
    # Prophylaxis
    (r"prophylaxis", {"id": "MAXO:0000017", "label": "preventative therapy"}),
    (r"opportunistic\s*infection", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (r"latent\s*TB", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    # Blood glucose monitoring - no good MAXO term for monitoring
    # (r'blood\s*glucose', ...),
    # Vector control (environmental)
    (r"vector\s*control", {"id": "MAXO:0000077", "label": "behavioral counseling"}),
    # GI management
    (
        r"gastrointestinal\s*management",
        {"id": "MAXO:0000267", "label": "gastrointestinal agent therapy"},
    ),
    # More drugs
    (r"glucocorticoid", {"id": "MAXO:0000058", "label": "pharmacotherapy"}),
    (
        r"mineralocorticoid\s*receptor",
        {"id": "MAXO:0000058", "label": "pharmacotherapy"},
    ),
    (
        r"receptor\s*antagonist",
        {"id": "MAXO:0000161", "label": "receptor antagonist therapy"},
    ),
]


def find_maxo_term(treatment_name: str, treatment_desc: str = None) -> dict | None:
    """Find the best MAXO term for a treatment based on name and description."""
    text = treatment_name.lower()
    if treatment_desc:
        text += " " + treatment_desc.lower()

    for pattern, maxo_term in MAXO_MAPPINGS:
        if re.search(pattern, text, re.IGNORECASE):
            return maxo_term

    return None


def process_file(filepath: Path, dry_run: bool = False) -> dict:
    """Process a single disorder file and add MAXO terms to treatments."""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    if not data.get("treatments"):
        return {"file": filepath.name, "treatments": 0, "added": 0, "skipped": 0}

    stats = {
        "file": filepath.name,
        "treatments": len(data["treatments"]),
        "added": 0,
        "skipped": 0,
    }

    modified = False
    for tx in data["treatments"]:
        # Skip if already has treatment_term
        if tx.get("treatment_term"):
            stats["skipped"] += 1
            continue

        maxo = find_maxo_term(tx.get("name", ""), tx.get("description", ""))
        if maxo:
            tx["treatment_term"] = {
                "preferred_term": maxo["label"],
                "term": {"id": maxo["id"], "label": maxo["label"]},
            }
            stats["added"] += 1
            modified = True
        else:
            print(f"  No MAXO match for: {tx.get('name', 'UNNAMED')}")

    if modified and not dry_run:
        with open(filepath, "w") as f:
            yaml.dump(
                data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
            )

    return stats


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Add MAXO terms to disorder treatments"
    )
    parser.add_argument(
        "--dry-run", "-n", action="store_true", help="Do not write files"
    )
    parser.add_argument("--file", "-f", help="Process a single file")
    args = parser.parse_args()

    if args.file:
        files = [Path(args.file)]
    else:
        files = sorted(Path("kb/disorders").glob("*.yaml"))

    total_added = 0
    total_skipped = 0
    total_treatments = 0

    for f in files:
        # Skip backup files
        if f.name.endswith(".bak"):
            continue

        print(f"Processing: {f.name}")
        stats = process_file(f, args.dry_run)
        total_treatments += stats["treatments"]
        total_added += stats["added"]
        total_skipped += stats["skipped"]

        if stats["added"] > 0:
            print(f"  Added {stats['added']} MAXO terms")
        if stats["skipped"] > 0:
            print(f"  Skipped {stats['skipped']} (already have treatment_term)")

    print("\nSummary:")
    print(f"  Total treatments: {total_treatments}")
    print(f"  Added: {total_added}")
    print(f"  Skipped (existing): {total_skipped}")
    print(f"  Unmatched: {total_treatments - total_added - total_skipped}")


if __name__ == "__main__":
    main()
