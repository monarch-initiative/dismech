# Acute Hepatitis C Virus Infection Research Synthesis
## Compared sources
- Falcon: `Acute_Hepatitis_C_Virus_Infection-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-05-04T16:01:43.216037`; reported citation count `50`.
- OpenScientist: `Acute_Hepatitis_C_Virus_Infection-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-05T00:13:26.734680`; reported citation count `66`.
- Citation-file overlap: 0 shared refs, 14 Falcon-only refs, 66 OpenScientist-only refs.
- YAML integration after backfill: 11 references linked to Falcon outputs, 65 references linked to OpenScientist outputs, 0 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: Early HCV infection of hepatocytes; Immune-mediated viral clearance versus persistence; Chronic hepatitis C virus infection.
The structured phenotype surface used for curation includes: Jaundice; Nausea; Elevated hepatic transaminases.
Shared mechanistic vocabulary detected in both reports includes: acute, infection, hepatitis, clearance, chronic, weeks, viral, immune, spontaneous, phase, virus, genotype.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: Comprehensive Research Report: Acute Hepatitis C Virus (HCV) Infection (Infectious), Executive summary, 1. Disease information, 1.1 Overview / definition (current understanding), 1.2 Key identifiers and controlled vocabularies, 1.3 Synonyms / alternative names, 1.4 Evidence provenance (patient-level vs aggregated), 2. Etiology.
- *Table: This table summarizes high-yield evidence for defining, diagnosing, and managing acute hepatitis C virus infection, including diagnostic windows, natural history, risk groups, and current guideline-based treatment. It is useful as a concise knowledge-base-ready abstraction anchored to the gathered evidence contexts.*
- * **Acute / recently acquired HCV infection** is generally defined as the **first 6 months after initial exposure**; **chronic HCV infection** is defined by **persistence of viremia for >6 months**. (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6)
- * The term "acute hepatitis C" is used variably (biological vs clinical definitions are not completely standardized), and many incident infections are **clinically silent**. (fasano2024acutehepatitisc pages 4-5, liu2023acutehepatitisc pages 5-6)
- * **ICD-11:** Not directly retrievable for *acute* hepatitis C from the available sources in this run; one GBD-methods paper indicates ICD-11 codes for *chronic* hepatitis C and sequelae (cirrhosis/HCC), but does not provide a stem code for acute infection. (bai2025globalregionaland pages 1-2)
- * **Early phase of HCV infection** (fasano2024acutehepatitisc pages 1-2, fasano2024acutehepatitisc pages 4-5, fasano2024acutehepatitisc pages 2-4)
Falcon-only citations retained for curation include: DOI:10.1128/jcm.00832-24, DOI:10.1186/s12879-025-12396-y, DOI:10.1186/s12954-024-01115-6, DOI:10.14745/ccdr.v49i06a02, DOI:10.1515/cclm-2025-0501, DOI:10.21037/tgh-23-104, DOI:10.3350/cmh.2022.0349, DOI:10.3390/chemosensors13020031, DOI:10.3390/microorganisms12061035, DOI:10.3390/pathogens13100841, DOI:10.3390/v16111739, DOI:10.3390/v17081069, ...

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Comprehensive Disease Knowledge Base Report: Acute Hepatitis C Virus Infection, Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Acute HCV infection, Acute hepatitis C (AHC).
- **Primary Cause:** Infection with Hepatitis C Virus (HCV; NCBI Taxonomy ID: 11103), a blood-borne pathogen. HCV is an enveloped, positive-sense, single-stranded RNA virus of the family *Flaviviridae*. There are 8 major genotypes (1-8) and more than 90 subtypes with distinct geographic distributions.
- **Injection drug use (IDU):** The predominant mode of transmission globally, accounting for >60% of new infections in high-income countries. Equipment sharing (needles, syringes, cookers, cotton filters) is the primary risk behavior ([PMID: 25270261](https://pubmed.ncbi.nlm.nih.gov/25270261/)).
- **Vertical transmission:** Mother-to-child transmission occurs in 3-5% of pregnancies with HCV-positive mothers, rising to ~19.4% with HIV co-infection ([PMID: 24187446](https://pubmed.ncbi.nlm.nih.gov/24187446/)).
- **HIV co-infection:** Reduces spontaneous clearance rate from ~30-50% to ~15% ([PMID: 21139063](https://pubmed.ncbi.nlm.nih.gov/21139063/))
- **Alcohol consumption:** Accelerates liver disease progression via competition with retinol metabolism through the ADH-ALDH pathway ([PMID: 26638120](https://pubmed.ncbi.nlm.nih.gov/26638120/))
OpenScientist-only citations retained for curation include: PMID:10726057, PMID:11440409, PMID:12227687, PMID:18824553, PMID:19124916, PMID:20538002, PMID:21139063, PMID:21408083, PMID:22715213, PMID:23043385, PMID:23108300, PMID:23481134, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
