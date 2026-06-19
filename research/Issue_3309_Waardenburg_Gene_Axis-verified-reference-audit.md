---
title: Issue 3309 Waardenburg Gene-Axis Verified Reference Audit
issue: https://github.com/monarch-initiative/dismech/issues/3309
date: 2026-05-28
status: local_verification_supplement
deep_research_provider: falcon
deep_research_output: research/Issue_3309_Waardenburg_Gene_Axis-deep-research-falcon.md
deep_research_status: completed
deep_research_citation_count: 42
deep_research_artifact_count: 2
---

# Issue 3309 Waardenburg Gene-Axis Verified Reference Audit

This supplement records the locally verified reference and ontology facts for
issue 3309. It is intended to guard against deep-research citation errors before
curation. PubMed and ClinGen cache files listed below were generated only with
repo commands (`just fetch-reference` and `just clingen-rebuild`), not hand
edited.

## Executive Curation Position

- Create three new entries:
  - `PAX3_Waardenburg_Spectrum.yaml`
  - `SOX10_Neurocristopathy_Spectrum.yaml`
  - `EDN3_EDNRB_Waardenburg_Shah.yaml`
- Keep `PCWH_syndrome.yaml` as a separate entry, but add an upstream SOX10
  NMD-escape/toxic truncation mechanism.
- Create a narrow `kb/modules/neural_crest_melanocyte_deficiency.yaml` module
  for shared melanocyte/SNHL biology. Defer an enteric neurocristopathy module.
- Do not create a standalone SNAI2 disease entry. Treat SNAI2 as a limited
  evidence mechanistic hypothesis or module note.
- Treat CDHS as a PAX3 allelic condition/differential note, not a PAX3
  Waardenburg subtype.

## Falcon Deep Research Result

Falcon was run for the consolidated Issue 3309 gene-axis question. The first
attempt failed during Edison polling with a transient DNS resolution error; a
rerun completed successfully.

Generated files:

- `research/Issue_3309_Waardenburg_Gene_Axis-deep-research-falcon.md`
- `research/Issue_3309_Waardenburg_Gene_Axis-deep-research-falcon.md.citations.md`
- `research/Issue_3309_Waardenburg_Gene_Axis-deep-research-falcon_artifacts/`

The Falcon report supports the same curation split as the local audit:
separate PAX3 and SOX10 spectrum entries, an EDN3/EDNRB signaling-axis entry,
PCWH as a SOX10 NMD-escape/truncation sub-spectrum, and SNAI2 as limited or
disputed evidence rather than a standalone disease entry.

Treat Falcon as a lead generator, not the source of record. Its ClinGen section
could not retrieve gene-by-gene verdicts, whereas the local audit below has
current structured ClinGen assertion IDs. Its artifact table is useful as a
summary, but context-ID snippets from Falcon artifacts should not be copied into
YAML evidence unless the exact text is also present in generated
`references_cache` content.

## Invalid PMIDs From Issue Comments

These identifiers were present in issue comments but do not support the stated
claims.

| Listed ID | Resolves to | Verdict |
|---|---|---|
| PMID:9747560 | Group D streptococcal throat infection. | Wrong ID for PMC9747560. Use PMID:36331148. |
| PMID:1301956 | Molecular genetics of the LDL receptor gene in familial hypercholesterolemia. | Wrong PAX3 discovery ID. Use PMID:1347148 and PMID:1347149. |
| PMID:8131751 | Stch encodes the ATPase core of a microsomal stress 70 protein. | Wrong PAX3 WS1/WS3 ID. Use PMID:8447316. |
| PMID:21120959 | PubMed summary unavailable. | Do not use. PAX3 review candidates include PMID:8533800 and PMID:20127975. |
| PMID:9758616 | Chromosome 21 disomy in spermatozoa of fathers of children with trisomy 21. | Wrong SOX10 discovery ID. Use PMID:9462749. |
| PMID:14695535 | Knobloch syndrome / COL18A1. | Wrong SOX10 NMD ID. Use PMID:15004559. |
| PMID:17690706 | HCV-related lymphomas. | Wrong SOX10 review ID. Use PMID:34667088 and/or PMID:17999358. |
| PMID:7916741 | Cytochrome b variation among Atlantic Alcidae. | Wrong EDNRB ID. Use PMID:8001158 plus EDNRB WS4 papers below. |
| PMID:8811180 | Protein prenylation review. | Wrong EDN3 ID. Use PMID:8630502 and PMID:8630503. |
| PMID:7651240 | Japanese encephalitis virus lymphocyte response. | Wrong endothelin pathway ID. Use PMID:11434563, PMID:16650841, PMID:12812796. |
| PMID:36047905 | Female sexually fluid identity management at work. | Wrong WS review ID. Use PMID:20127975 and PMID:34667088. |
| PMID:26633543 | Economic evaluation of whole-genome sequencing in healthy individuals. | Wrong SOX10 review ID. Use PMID:34667088. |
| PMID:10581041 | Murine cyclin A2 embryonic lethality. | Wrong PCWH/SOX10 ID. Use PMID:15004559 and PMID:29681101. |

## Corrected Core Literature

| Topic | Recommended reference | Use in curation |
|---|---|---|
| Six-gene WS NGS cohort | PMID:36331148 | Broad clinical/genetic overview; correct ID for PMC9747560. |
| PAX3 discovery | PMID:1347148; PMID:1347149 | Original PAX3/WS mutation reports. |
| PAX3 WS1/WS3 | PMID:8447316 | PAX3 paired-domain mutations cause both WS1 and WS3. |
| PAX3 mutation review | PMID:8533800; PMID:20127975 | PAX3 variant spectrum and broader WS mutation review. |
| PAX3/SOX10/MITF regulatory hierarchy | PMID:10982026; PMID:10942418; PMID:10938265 | Shared melanocyte transcriptional module. |
| PAX3 cochlear melanocytes | PMID:38278860 | PAX3 contribution to neural-crest-derived cochlear melanocytes. Model organism evidence. |
| SOX10 WS4 discovery | PMID:9462749 | SOX10 mutations in Waardenburg-Hirschsprung disease. |
| SOX10 NMD escape / PCWH | PMID:15004559 | Truncating SOX10 phenotypic split by NMD vs NMD escape. |
| SOX10 spectrum review | PMID:34667088 | WS2, WS4, PCWH, enteric and glial lineage spectrum. |
| SOX10 deletions WS2/WS4 | PMID:17999358 | Supports SOX10 spectrum across WS2 and WS4. |
| SOX10-EDN3-EDNRB interactions | PMID:16650841 | ENS, melanocyte, stria vascularis and hearing/pigment links. |
| EDNRB HSCR discovery | PMID:8001158 | EDNRB in multigenic Hirschsprung disease. |
| EDNRB Waardenburg-Hirschsprung | PMID:16237557; PMID:25852447; PMID:30394532 | EDNRB WS4A clinical genetics. |
| EDN3 WS4B discovery | PMID:8630502; PMID:8630503 | EDN3 mutations in Shah-Waardenburg syndrome. |
| Endothelin pathway review | PMID:11434563 | EDNRB/EDN3 shared melanocyte and enteric neural crest biology. |
| EDNRB migration mechanism | PMID:12812796 | EDNRB required for terminal migration of melanoblast and ENS precursors. |
| Cochlear melanocytes | PMID:11764294 | Stria vascularis melanocytes and MITF signaling in hearing. |
| SNAI2 limited evidence | PMID:12444107 | Original SLUG/SNAI2 deletion report; pair with ClinGen Limited assertion. |
| CDHS/PAX3 | PMID:8664898; PMID:14556253 | PAX3 allelic condition, clinically distinct from WS1/WS3. |
| ClinGen L&S framework | PMID:35754516 | Disease-entity lumping/splitting framework. |
| DNAC dyadic nomenclature | PMID:39241757 | `GENE-related phenotype` naming rationale. |
| Semidominant precedent | PMID:38016518 | ClinGen gene-disease curation with semidominant MOI examples. |
| Hearing-loss recuration | PMID:39987489 | GCEP recuration context; validity changes over time. |

## Falcon High-Signal Additions

These Falcon-cited references were cached with `just fetch-reference` after the
successful run. Use them only when the generated cache content supports the
claim being made.

| Topic | Cached reference | Use in curation |
|---|---|---|
| WS disease-mechanism review | DOI:10.1038/s41434-021-00240-2 | Modern review for PAX3/SOX10/MITF/EDN3/EDNRB mechanism overview; secondary support only. |
| 2024 undiagnosed WS cohort | DOI:10.1186/s13023-024-03220-y | Recent multi-data integration cohort; useful for PAX3/MITF/SOX10 prevalence and phenotype context. |
| 2024 diagnostic approach | DOI:10.3390/jpm14090906 | Recent NGS/MLPA diagnostic context, including CNV detection and MITF haploinsufficiency discussion. |
| 2023 NGS WS variants | DOI:10.3390/audiolres14010002 | Recent NGS case series and SNAI2 caution context. |
| EDNRB heterozygous WS2 | DOI:10.1002/humu.23206 | Key primary evidence for EDNRB heterozygous incomplete-penetrance WS2-like presentations. |
| Melanocyte development overview | DOI:10.1111/pde.13713 | Secondary background for melanocyte/neural-crest development and WS gene table. |
| SNAI2 dispute | DOI:10.1002/ajmg.a.61887 | Modern challenge to historical SNAI2/piebaldism/WS claims. |
| ClinGen HL framework | DOI:10.1038/s41436-019-0487-0 | GCEP framework paper; pair with live CGGV assertion caches for gene-specific verdicts. |
| WS NGS genotype/phenotype series | DOI:10.1155/2019/7143458 | Cohort context for subtype variability and MITF duplication/dosage discussion. |
| SOX10 functional analysis | DOI:10.1002/humu.21583 | SOX10 missense functional work; supports target-gene and variant-effect discussion. |
| PAX3/CDHS review background | DOI:10.1055/s-2006-947284 | Secondary support for PAX3 allele-specific CDHS/WS distinctions; do not use over primary evidence where possible. |
| PAX3/Splotch review | DOI:10.2174/1381612013397726 | Secondary model-organism/developmental background for PAX3 structure-function. |

## ClinGen Assertions

| Gene | Disease | MONDO | MOI | Classification | CGGV ID |
|---|---|---|---|---|---|
| PAX3 | Waardenburg syndrome | MONDO:0018094 | AD | Definitive | CGGV:assertion_594ef026-3730-43bc-b721-d15cf0bbbf26-2017-11-15T050000.000Z |
| MITF | Waardenburg syndrome type 2 | MONDO:0019517 | AD | Definitive | CGGV:assertion_bc5d40d2-44b5-49b6-97a9-7bdfc39bee49-2017-11-21T170000.000Z |
| SOX10 | Waardenburg syndrome type 4C | MONDO:0013202 | AD | Definitive | CGGV:assertion_00a5b707-a265-4af0-a7e1-f15734ea42b9-2018-06-19T160000.000Z |
| EDN3 | Waardenburg syndrome type 4B | MONDO:0013201 | AR | Moderate | CGGV:assertion_7f88c34c-a093-4fc8-b84a-49c7d2dd327f-2023-06-29T160000.000Z |
| EDN3 | Waardenburg syndrome type 4B | MONDO:0013201 | AD | Limited | CGGV:assertion_04e39ada-cd77-43f0-98f3-7b4a37668a96-2018-05-08T160000.000Z |
| EDNRB | Waardenburg syndrome type 4A | MONDO:0010192 | AR | Moderate | CGGV:assertion_d7abbd45-7915-437b-849b-dea876bfc2f5-2023-06-27T160000.000Z |
| EDNRB | Waardenburg syndrome type 4A | MONDO:0010192 | AD | Limited | CGGV:assertion_73ee9727-60c1-40fd-830f-08c2b513d2ee-2018-05-08T160000.000Z |
| SNAI2 | Waardenburg syndrome | MONDO:0018094 | AR | Limited | CGGV:assertion_9c01d8d8-40a4-4b11-ad9c-8283bb937c55-2024-10-31T160000.000Z |

Use the existing `external_assertions` slot for these; do not add an ad-hoc
`clingen_alignment` block unless the schema is extended separately.

## Ontology Anchors Checked With OAK

| Concept | Term |
|---|---|
| Waardenburg syndrome | MONDO:0018094 |
| Waardenburg syndrome type 1 | MONDO:0008670 |
| Waardenburg syndrome type 3 | MONDO:0007862 |
| Waardenburg syndrome type 2E | MONDO:0012698 |
| Waardenburg-Shah syndrome / WS4 | MONDO:0019518 |
| Waardenburg syndrome type 4A | MONDO:0010192 |
| Waardenburg syndrome type 4B | MONDO:0013201 |
| Waardenburg syndrome type 4C | MONDO:0013202 |
| PCWH syndrome | MONDO:0012198 |
| Craniofacial-deafness-hand syndrome | MONDO:0007395 |
| Semidominant inheritance | HP:0032113 |
| Melanoblast | CL:0000541 |
| Melanocyte | CL:0000148 |
| Neural crest cell | CL:0011012 |
| Stria vascularis of cochlear duct | UBERON:0002282 |
| Melanocyte differentiation | GO:0030318 |
| Neural crest cell migration | GO:0001755 |
| Enteric nervous system development | GO:0048484 |
| Pigmentation | GO:0043473 |

## Entry Plans

### PAX3_Waardenburg_Spectrum.yaml

Recommended disease label: `PAX3-related Waardenburg syndrome`.

Anchor: `MONDO:0018094` with subtypes `WS1` (`MONDO:0008670`) and `WS3`
(`MONDO:0007862`). Add an inheritance entry using `HP:0032113`
Semidominant inheritance to capture the monoallelic/biallelic dosage continuum.

Core pathograph:

1. PAX3 dosage-sensitive transcription factor dysfunction.
2. Reduced SOX10/PAX3/MITF melanocyte transcriptional program.
3. Melanoblast/melanocyte developmental deficiency.
4. Stria vascularis melanocyte deficiency -> sensorineural hearing impairment.
5. Cutaneous/hair/iris melanocyte deficiency -> pigmentary findings.
6. Limb muscle/progenitor developmental arm for WS3.

CDHS handling: add a note or differential/related condition only. It is PAX3
allelic, but MONDO describes it as distinguishable from Waardenburg syndrome and
ClinGen excludes it from the PAX3/WS assertion scope.

### SOX10_Neurocristopathy_Spectrum.yaml

Recommended disease label: `SOX10-related neurocristopathy spectrum`.

Anchor: `MONDO:0013202` as the ClinGen-aligned WS4C anchor. Include subtypes
`WS2E` (`MONDO:0012698`) and `WS4C` (`MONDO:0013202`). Keep `PCWH_syndrome.yaml`
separate and cross-reference it in notes/differential language rather than
absorbing it.

Core pathograph:

1. SOX10 neural crest and glial lineage transcriptional dysfunction.
2. NMD-sensitive truncation/haploinsufficiency arm.
3. Melanocyte lineage failure -> pigmentation and SNHL.
4. Enteric neural crest lineage failure -> Hirschsprung disease in WS4C.
5. NMD-escape truncation/dominant-negative or toxic arm -> PCWH glial/myelin
   involvement, represented mainly in the PCWH file.

### EDN3_EDNRB_Waardenburg_Shah.yaml

Recommended disease label: `EDN3/EDNRB-related Waardenburg-Shah syndrome`.

Anchor: `MONDO:0019518`. Include subtype terms `WS4A` (`MONDO:0010192`) and
`WS4B` (`MONDO:0013201`). Use `external_assertions` to record the AR Moderate
and AD Limited ClinGen assertions for both EDN3 and EDNRB.

Core pathograph:

1. EDN3 ligand / EDNRB receptor endothelin signaling deficiency.
2. Impaired terminal migration of melanoblast and enteric nervous system
   precursors.
3. Stria vascularis and cutaneous melanocyte deficiency -> SNHL and pigmentary
   findings.
4. Failed enteric neural crest colonization -> aganglionosis / Hirschsprung
   disease.
5. Modifier/penetrance notes for AD/AR and variable expressivity.

### PCWH_syndrome.yaml Update

Add a new upstream node before the existing `SOX10 developmental dysfunction`
or revise that node to make the NMD-escape mechanism explicit. Candidate node
name: `NMD-escaping truncated SOX10 protein`.

Use PMID:15004559 for the mechanism and retain PMID:29681101 for clinical PCWH
phenotype support.

### SNAI2

Do not create `SNAI2_Waardenburg_Spectrum.yaml`. Use a limited-evidence
mechanistic hypothesis in the PAX3/SOX10/MITF module notes or in the PAX3 entry
only if needed. Record the ClinGen Limited assertion through `external_assertions`
only when SNAI2 is explicitly discussed.

### Mechanism Module

Create `kb/modules/neural_crest_melanocyte_deficiency.yaml` if implementation
proceeds. Keep it small:

1. `Neural Crest Melanocyte Program Disruption`
2. `Melanoblast Migration and Survival Defect`
3. `Stria Vascularis Melanocyte Deficiency`
4. `Cutaneous and Iris Melanocyte Deficiency`

Use disorder-specific `conforms_to` nodes to substitute the initiating mechanism:
PAX3/SOX10/MITF transcriptional dysregulation vs EDN3/EDNRB signaling deficiency.
Do not include Hirschsprung/enteric biology in this first module; that should be
an extension or a separate enteric neurocristopathy module.

## Candidate Exact Snippets

These snippets were copied from generated cache files and should validate if
used unchanged or with normal YAML folding.

- PMID:36331148: "Waardenburg syndrome (WS) is a hereditary, genetically heterogeneous disorder characterized by variable presentations of sensorineural hearing impairment and pigmentation anomalies."
- PMID:1347148: "Waardenburg's syndrome (WS) is an autosomal dominant combination of deafness and pigmentary disturbances, probably caused by defective function of the embryonic neural crest."
- PMID:8447316: "Mutations in the paired domain of the human PAX3 gene cause Klein-Waardenburg syndrome (WS-III) as well as Waardenburg syndrome type I (WS-I)."
- PMID:10982026: "We show that SOX10 is capable of transactivating the MITF promoter 100-fold, and that this transactivation is further stimulated by PAX3."
- PMID:9462749: "Here we show that patients from four families with WS4 have mutations in SOX10, whereas no mutation could be detected in PAX3, MITF or EDNRB."
- PMID:15004559: "Our experiments show that triggering NMD and escaping NMD may cause distinct neurological phenotypes."
- PMID:34667088: "heterozygous mutations have been reported in Waardenburg syndrome type 2 (Waardenburg syndrome type without Hirschsprung disease), PCWH or PCW"
- PMID:16650841: "double mutants present with a severe increase in white spotting, absence of melanocytes within the inner ear, and in the stria vascularis in particular, and more severe ENS defects."
- PMID:12812796: "EDNRB signaling is exclusively required between E10.5 and E12.5 during the migratory phase of melanoblast and enteric neuron precursors."
- PMID:8630502: "EDN3 thus becomes the third known gene (after RET and EDNRB) predisposing to HSCR, supporting the view that the endothelin-signaling pathways play a major role in the development of neural crests."
- PMID:11434563: "Mutations in the genes encoding the endothelin type-B receptor (EDNRB) and its physiological ligand endothelin 3 (EDN3) are now known to account for the HSCR II phenotypes."
- PMID:11764294: "Intermediate cells play an important role for cochlear function: Na+K+-ATPase and potassium channels of intermediate cells are essential for production of endocochlear potential and for preparation of ionic milieu in the stria."
- PMID:12444107: "Here we show that two unrelated patients with WS2 have homozygous deletions in SLUG which result in absence of the SLUG product."
- PMID:8664898: "Craniofacial-deafness-hand syndrome (MIM 122880) is inherited as an autosomal dominant condition characterized by a flat facial profile, hypertelorism, profound sensorineural deafness"
- PMID:35754516: "Here, we outline the precuration process, the lumping and splitting guidelines with examples, and describe the ClinGen Lumping and Splitting Working Group."

## Validation Notes

- `PMID:38278860` is useful for PAX3/cochlear melanocyte mechanism, but it is
  mouse evidence and should be marked `MODEL_ORGANISM`.
- `PMID:16650841` and `PMID:12812796` are also model-organism/developmental
  evidence, not human clinical evidence.
- ClinGen structured snippets can be cited as `CGGV:` references once cache files
  are committed.
- If a desired claim is present only in full text and not in the generated
  PubMed abstract cache, do not use it as a `snippet` unless the cache content
  actually contains it.
- Falcon-generated citation handles and artifact context IDs are not valid
  reference identifiers for YAML curation. Convert them to DOI/PMID/CGGV
  references and verify snippets against generated cache files first.
