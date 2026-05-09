# Acute Promyelocytic Leukemia, PML-RARA Research Synthesis
## Compared sources
- Falcon: `APL_PML_RARA-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-04-05T12:00:24.489449`; reported citation count `26`.
- OpenScientist: `APL_PML_RARA-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-04T23:51:31.744721`; reported citation count `52`.
- Citation-file overlap: 0 shared refs, 9 Falcon-only refs, 52 OpenScientist-only refs.
- YAML integration after backfill: 9 references linked to Falcon outputs, 52 references linked to OpenScientist outputs, 0 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: PML-RARA Fusion Oncogene Formation; Transcriptional Repression of Differentiation Genes; PML Nuclear Body Disruption; Impaired Tumor Suppression; Promyelocyte Accumulation; Coagulopathy.
The structured phenotype surface used for curation includes: Pancytopenia; Disseminated Intravascular Coagulation; Abnormal Bleeding; Fatigue; Recurrent Infections.
Shared mechanistic vocabulary detected in both reports includes: ncbi, atra, pml-rara, rara, acute, differentiation, early, risk, fusion, cases, leukemia, patients.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: 1. Disease Information, 2. Etiology, Genetic risk factors (causal variants, susceptibility loci, modifier genes), Genetic protective factors (protective variants, modifier alleles), Environmental protective factors (diet, lifestyle, exposures that reduce risk), 3. Phenotypes, For each phenotype, provide, Age of symptom onset (neonatal, childhood, adult-onset, late-onset).
- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
- > **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
Falcon-only citations retained for curation include: DOI:10.1007/s00277-023-05422-z, DOI:10.1038/s41418-023-01139-8, DOI:10.1186/s12885-023-10612-z, DOI:10.3389/fonc.2022.1062524, DOI:10.3390/cancers16061160, DOI:10.3390/cancers16071351, DOI:10.3390/cancers16183208, DOI:10.3390/cancers16244192, DOI:10.3390/futurepharmacol3010012.

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Comprehensive Disease Characterization: Acute Promyelocytic Leukemia (PML-RARA), Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Acute Promyelocytic Leukemia (APL), AML-M3 (FAB classification).
- As described by Tomita et al., "Since the introduction of all-trans retinoic acid (ATRA) and arsenic trioxide (As2O3) for the treatment of acute promyelocytic leukemia (APL), the overall survival rate has improved dramatically" ([PMID: 23670176](https://pubmed.ncbi.nlm.nih.gov/23670176/)).
- **FLT3-ITD mutations**: Present in approximately 20-40% of APL cases; associated with higher WBC counts and the microgranular variant. The prognostic significance is debated in the ATRA+ATO era ([PMID: 36539954](https://pubmed.ncbi.nlm.nih.gov/36539954/); [PMID: 26920716](https://pubmed.ncbi.nlm.nih.gov/26920716/)).
- **Prior radiation therapy**: Radiation combined with chemotherapy is the most common antecedent in t-APL ([PMID: 15899774](https://pubmed.ncbi.nlm.nih.gov/15899774/)).
- **Age**: Median age at diagnosis is approximately 40-44 years; both pediatric and elderly cases occur.
- **Obesity**: Some epidemiological data suggest association with AML risk generally, though APL-specific data are limited.
OpenScientist-only citations retained for curation include: PMID:10329918, PMID:15899774, PMID:16352814, PMID:18644863, PMID:18650449, PMID:19727242, PMID:20508621, PMID:22535601, PMID:23670176, PMID:24201752, PMID:24344243, PMID:24433507, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
