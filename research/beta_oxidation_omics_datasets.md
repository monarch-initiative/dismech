# Fatty-acid β-oxidation disorders: gap-filling entries + omics dataset survey

Provenance note for the β-oxidation curation sweep (branch
`claude/beta-oxidation-diseases-dz2wip`). Records (1) the new disorder entries
added to close membership gaps in the fatty-acid β-oxidation (FAO) pathway and
(2) the verified omics datasets attached to them and the underlying
"is-the-mechanism-known" assessment.

## New entries (gap fill)

| Entry | Gene (HGNC) | MONDO | Pathway role | Framing |
|-------|-------------|-------|--------------|---------|
| Short-Chain Acyl-CoA Dehydrogenase Deficiency | ACADS (hgnc:90) | MONDO:0008722 | 1st dehydrogenation, C4–C6 acyl-CoA | Completes the SCAD/MCAD/VLCAD chain-length series; clinical significance genuinely debated (often benign) |
| Carnitine Palmitoyltransferase 1A Deficiency | CPT1A (hgnc:2328) | MONDO:0009705 | Rate-limiting step of the carnitine shuttle (outer mitochondrial membrane) | Completes CPT1A→CACT→CPT2 shuttle; distinctive high-free-carnitine/low-acylcarnitine biochemistry; muscle-sparing (CPT1B) |
| ACAD9 Deficiency | ACAD9 (hgnc:21497) | MONDO:0012624 | Acyl-CoA-dehydrogenase-family member | Disease is a **mitochondrial complex I assembly defect**, not a primary FAO-flux block; often riboflavin-responsive |
| ECHS1 Deficiency | ECHS1 (hgnc:3151) | MONDO:0014563 | 2nd step (enoyl-CoA hydratase) of the spiral | Leigh-like; driven mainly by **toxic valine-pathway intermediates** (methacrylyl-/acryloyl-CoA), FAO flux largely preserved |

Not added (already represented): SCHAD/`HADH` deficiency is a subtype in
`Congenital_Isolated_Hyperinsulinism`; `HSD17B10` is covered by
`HSD10_Mitochondrial_Disease`.

## Is the mechanism already known?

For FAODs the **primary enzymology is firmly established**: each disorder maps
to a defined enzymatic step, and the unifying paradigm — dual pathology of
*energy deficit* (failed acetyl-CoA/ATP generation under fasting/catabolic
stress) plus *toxic accumulation* of chain-length-specific acyl-CoAs and their
acylcarnitines — is textbook. Acylcarnitine MS/MS profiling of dried blood
spots is the validated diagnostic backbone of newborn screening (C8/C10 in
MCAD, C14:1 in VLCAD, C4 in SCAD).

What omics is still actively **elucidating** is the secondary / systems-level
biology the classic enzymology does not predict:

- **Membrane / complex-lipid remodeling** — untargeted lipidomics repeatedly
  finds glycerophospholipid and sphingolipid depletion in patient serum/red
  cells (SCADd/combined, PMID:41477503; VLCADd biomarkers, PMID:37367883) not
  captured by acylcarnitine panels.
- **Secondary OXPHOS destabilization** — transcriptomics/proteomics of
  ECHS1-null human cells (PMID:35962613) show a β-oxidation/valine enzyme loss
  destabilizes OXPHOS complexes I and IV, explaining the Leigh-like phenotype
  as secondary mitochondrial failure.
- **Acyl-CoA-driven protein/histone lysine-acylation** — accumulated
  short-chain acyl-CoAs act as acyl donors reprogramming histone acylation
  (H4K16 in SCADd, PMID:41421336; ECHS1-linked crotonylation, PMID:33683949).
- **ACAD9's moonlighting assembly role** — complexome proteomics
  (PMID:33465056) resolves ACAD9 deficiency as a complex I *assembly* disorder.

**Verdict:** core enzymology and diagnostics are solved; omics is still needed
to explain tissue-specific lipid remodeling, secondary OXPHOS collapse,
epigenetic acyl-CoA signaling, and (for ECHS1/ACAD9) which downstream toxicity
truly drives disease.

## Verified datasets attached to the entries

Each accession below was confirmed by fetching its repository landing page /
API record; publication PMIDs were fetched into `references_cache/`.

| Entry | Accession | Type | Organism | PMID | Landing page |
|-------|-----------|------|----------|------|--------------|
| SCAD | geo:GSE296978 | RNA-seq | mouse | 41421336 | ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296978 |
| SCAD | geo:GSE35180 | microarray | mouse | 22936979 | ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE35180 |
| SCAD | massive:MSV000094418 | metabolomics/lipidomics | human | 41477503 | omicsdi.org/dataset/massive/MSV000094418 |
| ACAD9 | pride:PXD021386 | proteomics (complexome) | human | 33465056 | ebi.ac.uk/pride/archive/projects/PXD021386 |
| ECHS1 | geo:GSE200252 | RNA-seq | human | 35962613 | ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE200252 |
| ECHS1 | pride:PXD032761 | proteomics | human+mouse | 35962613 | ebi.ac.uk/pride/archive/projects/PXD032761 |
| ECHS1 | geo:GSE159039 | RNA-seq | rat | 33683949 | ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE159039 |

Negative finding: **CPT1A deficiency** has no public omics dataset specific to
the inborn-error phenotype — all GEO/PRIDE CPT1A hits concern CPT1A as a
metabolic lever in cancer/adipose/stem-cell biology, not the disease. No
dataset block was added rather than attaching off-target data.

General-FAOD context dataset (not attached to a new entry):
`metabolomicsworkbench:ST002560` (VLCADd hydroxy-acylcarnitine biomarkers,
PMID:37367883).

Two dataset accession prefixes new to the repo (`pride`, `massive`) were added
to `skip_prefixes` in `conf/reference_validator_config.yaml` (they are dataset
identifiers, not fetchable literature references).
