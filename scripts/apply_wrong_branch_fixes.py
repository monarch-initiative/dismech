#!/usr/bin/env python3
"""Fix terms used in wrong ontology branches (e.g., molecular functions used as
biological processes, cellular components used as biological processes).

Usage:
    uv run python scripts/apply_wrong_branch_fixes.py
    uv run python scripts/apply_wrong_branch_fixes.py --dry-run
"""

import re
import sys
from pathlib import Path

# Mapping: wrong_curie -> (new_curie, new_label)
# These are molecular functions (MF) or cellular components (CC) incorrectly
# placed in biological_processes fields. Replacements use the closest BP term.
REPLACEMENTS = {
    # MF: catalytic activity -> context-dependent BP; most are enzyme deficiencies
    # For IEMs, the BP is the metabolic process that's disrupted
    "GO:0003824": ("GO:0008152", "metabolic process"),
    # MF: succinate dehydrogenase activity -> electron transport chain
    "GO:0000104": ("GO:0022900", "electron transport chain"),
    # MF: isocitrate dehydrogenase (NADP+) activity -> isocitrate metabolic process
    "GO:0004450": ("GO:0006102", "isocitrate metabolic process"),
    # MF: protein serine/threonine kinase activity -> protein phosphorylation
    "GO:0004674": ("GO:0006468", "protein phosphorylation"),
    # MF: protein tyrosine kinase activity -> protein phosphorylation
    "GO:0004713": ("GO:0006468", "protein phosphorylation"),
    # MF: protein tyrosine phosphatase activity -> protein dephosphorylation
    "GO:0004725": ("GO:0006470", "protein dephosphorylation"),
    # MF: VEGFR activity -> vascular endothelial growth factor signaling pathway
    "GO:0005021": ("GO:0048010", "vascular endothelial growth factor receptor signaling pathway"),
    # MF: Ras GEF activity -> Ras protein signal transduction
    "GO:0005088": ("GO:0007265", "Ras protein signal transduction"),
    # MF: structural constituent of cytoskeleton -> cytoskeleton organization
    "GO:0005200": ("GO:0007010", "cytoskeleton organization"),
    # MF: transporter activity -> transport
    "GO:0005215": ("GO:0006810", "transport"),
    # MF: voltage-gated sodium channel activity -> sodium ion transport
    "GO:0005248": ("GO:0006814", "sodium ion transport"),
    # MF: voltage-gated potassium channel activity -> potassium ion transport
    "GO:0005249": ("GO:0006813", "potassium ion transport"),
    # CC: glycine cleavage complex -> glycine catabolic process
    "GO:0005960": ("GO:0006546", "glycine catabolic process"),
    # None (GO:0007050) -> cell cycle arrest (closest existing term)
    "GO:0007050": ("GO:0007049", "cell cycle"),
    # MF: cytoskeletal anchor activity -> cytoskeleton organization
    "GO:0008093": ("GO:0007010", "cytoskeleton organization"),
    # MF: ATP hydrolysis activity -> ATP metabolic process
    "GO:0016887": ("GO:0046034", "ATP metabolic process"),
    # MF: transmembrane transporter activity -> transmembrane transport
    "GO:0022857": ("GO:0055085", "transmembrane transport"),
    # CC: type III protein secretion system complex -> type III protein secretion
    "GO:0030257": ("GO:0030254", "protein secretion by the type III secretion system"),
    # MF: spectrin binding -> cytoskeleton organization
    "GO:0030507": ("GO:0007010", "cytoskeleton organization"),
    # MF: arsenite methyltransferase activity -> methylation
    "GO:0030791": ("GO:0032259", "methylation"),
    # None (GO:0035326) -> regulation of DNA-templated transcription
    "GO:0035326": ("GO:0006355", "regulation of DNA-templated transcription"),
    # BP: protein demalonylation -> protein modification process
    "GO:0036046": ("GO:0036211", "protein modification process"),
    # None (GO:0043437) -> DNA damage response
    "GO:0043437": ("GO:0006974", "cellular response to DNA damage stimulus"),
    # CC: pyruvate dehydrogenase complex -> pyruvate metabolic process
    "GO:0045254": ("GO:0006090", "pyruvate metabolic process"),
    # MF: actin filament binding -> actin cytoskeleton organization
    "GO:0051015": ("GO:0030031", "cell projection assembly"),
    # CC: canonical inflammasome complex -> inflammatory response
    "GO:0061702": ("GO:0006954", "inflammatory response"),
    # MF: alpha-latrotoxin receptor binding -> signal transduction
    "GO:0061761": ("GO:0007165", "signal transduction"),
    # CC: tight junction -> cell-cell junction organization
    "GO:0070160": ("GO:0045216", "cell-cell junction organization"),
    # MF: medium-chain fatty acyl-CoA dehydrogenase activity -> fatty acid beta-oxidation
    "GO:0070991": ("GO:0006635", "fatty acid beta-oxidation"),
    # CC: NLRP3 inflammasome complex -> inflammatory response
    "GO:0072559": ("GO:0006954", "inflammatory response"),
    # CHEBI terms not in ChemicalEntityTerm enum
    # CHEBI:16033 -> None, likely wrong ID
    # CHEBI:37845 -> growth hormone (this is a protein, not chemical)
    # CHEBI:50114 -> estrogen (too generic?)
    # CHEBI:64357 -> None (doesn't exist)
    # UBERON:0008901 -> None
}

# CHEBI and UBERON wrong-ID fixes need special handling per file
CHEBI_FIXES = {
    # Jeavons_Syndrome: CHEBI:16033 doesn't exist -> use correct CHEBI for valproic acid
    ("Jeavons_Syndrome.yaml", "CHEBI:16033"): ("CHEBI:39867", "valproic acid"),
    # SADDAN: CHEBI:37845 = growth hormone -> use NCIT term (biologics not in CHEBI)
    ("SADDAN.yaml", "CHEBI:37845"): ("NCIT:C2288", "Somatotropin"),
    # Raynaud: CHEBI:50114 = estrogen -> use CHEBI:23965 (estradiol, specific estrogen)
    ("Raynaud_Disease.yaml", "CHEBI:50114"): ("CHEBI:23965", "estradiol"),
    # CHEBI:64357 doesn't exist - rituximab, use NCIT term
    ("Stiff_Person_Syndrome.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("IgG4-Related_Disease.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("Autoimmune_Encephalitis.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("Neuromyelitis_Optica_Spectrum_Disorder.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("Burkitt_Lymphoma.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("Multicentric_Castleman_Disease.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
    ("Systemic_Lupus_Erythematosus.yaml", "CHEBI:64357"): ("NCIT:C1702", "Rituximab"),
}

UBERON_FIXES = {
    # Pars_Planitis: UBERON:0008901 doesn't exist -> use UBERON:0000053 (macula lutea)
    ("Pars_Planitis.yaml", "UBERON:0008901"): ("UBERON:0000053", "macula lutea"),
}


def apply_replacements(filepath: Path, dry_run: bool = False) -> list[str]:
    """Replace wrong-branch terms in a YAML file."""
    content = filepath.read_text()
    lines = content.split("\n")
    changes = []
    new_lines = list(lines)
    fname = filepath.name

    i = 0
    while i < len(lines):
        id_match = re.match(
            r'^(\s+)id:\s+((?:GO|UBERON|CL|HP|MONDO|CHEBI|MAXO):\S+)\s*$',
            lines[i]
        )
        if id_match and i + 1 < len(lines):
            curie = id_match.group(2)
            indent = id_match.group(1)

            replacement = None

            # Check file-specific overrides
            file_key = (fname, curie)
            if file_key in CHEBI_FIXES:
                replacement = CHEBI_FIXES[file_key]
                if replacement is None:
                    i += 1
                    continue
            elif file_key in UBERON_FIXES:
                replacement = UBERON_FIXES[file_key]
            elif curie in REPLACEMENTS:
                replacement = REPLACEMENTS[curie]

            if replacement:
                new_curie, new_label = replacement
                label_match = re.match(r'^(\s+)label:\s+(.+)$', lines[i + 1])
                if label_match:
                    old_label = label_match.group(2).strip()
                    label_indent = label_match.group(1)
                    changes.append(
                        f"  {curie} ('{old_label}') -> {new_curie} ('{new_label}')"
                    )
                    if not dry_run:
                        new_lines[i] = f"{indent}id: {new_curie}"
                        new_lines[i + 1] = f"{label_indent}label: {new_label}"
        i += 1

    if not dry_run and changes:
        filepath.write_text("\n".join(new_lines))

    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    kb_dir = Path("kb/disorders")

    total = 0
    files_changed = 0

    for filepath in sorted(kb_dir.glob("*.yaml")):
        if filepath.name.endswith(".history.yaml"):
            continue
        changes = apply_replacements(filepath, dry_run=dry_run)
        if changes:
            files_changed += 1
            total += len(changes)
            print(f"{filepath.name}: {len(changes)} fixes")
            for c in changes:
                print(c)

    print(f"\n=== {total} fixes in {files_changed} files ===")
    if dry_run:
        print("(Dry run — no files modified)")


if __name__ == "__main__":
    main()
