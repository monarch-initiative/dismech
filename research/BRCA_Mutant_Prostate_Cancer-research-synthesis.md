# BRCA-Mutant Prostate Cancer Research Synthesis

## Provider Coverage

- Falcon: `BRCA_Mutant_Prostate_Cancer-deep-research-falcon.md`
- OpenScientist: `BRCA_Mutant_Prostate_Cancer-deep-research-openscientist.md`

## Agreement

Both providers model BRCA-mutant prostate cancer as a molecularly defined prostate cancer subset driven by BRCA1/BRCA2 homologous recombination repair deficiency. They agree that BRCA2 alterations are more common and usually more clinically important than BRCA1 alterations, that HRR loss causes genomic instability and aggressive metastatic behavior, and that the same defect creates therapeutic sensitivity to PARP inhibition and platinum chemotherapy.

Both reports also converge on modern mCRPC treatment implementation: genomic testing identifies actionable HRR alterations, olaparib and rucaparib are established PARP inhibitor options, and first-line PARP inhibitor plus androgen receptor pathway inhibitor combinations are now part of the evidence base for HRR-mutated or BRCA-mutated mCRPC.

## Differences

Falcon emphasized clinical implementation: PROfound, TRITON, MAGNITUDE, TALAPRO-2, MRI/PSA screening in high-risk carriers, and pragmatic treatment pathway details. It also flagged ontology mappings for HRR, androgen receptor signaling, prostate epithelial cell context, and treatment annotations.

OpenScientist emphasized resistance biology and longitudinal disease behavior. Its strongest added value was the acquired-resistance section, especially BRCA reversion mutations after PARP inhibitor or platinum pressure, POLQ-mediated microhomology repair, and the need for serial ctDNA/resistance monitoring.

## YAML Integration

Integrated into `kb/disorders/BRCA_Mutant_Prostate_Cancer.yaml`:

- Added HGNC-backed `gene_term` annotations for BRCA1 and BRCA2.
- Added `PARP-Androgen Receptor Co-Dependency` to represent the PARP/AR crosstalk rationale for combination therapy.
- Added `BRCA Reversion-Mediated PARP Resistance` to capture acquired resistance through restored HRR.
- Added `PARP Inhibitor-AR Pathway Inhibitor Combination Therapy` with talazoparib, enzalutamide, niraparib, and abiraterone therapeutic agents.
- Backfilled top-level references with `found_in` provenance for Falcon and OpenScientist citation trails.

## Not Integrated

Detailed trial subgroup tables, exploratory POLQ inhibitor strategies, full ctDNA monitoring protocols, and non-BRCA HRR genes were not added as first-class YAML content. They are useful provenance, but the disorder entry is BRCA-focused and should not become a general HRR-mutated prostate cancer entry.
