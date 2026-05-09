# Acute Lichenoid Pityriasis Research Synthesis
## Compared sources
- Falcon: `Acute_Lichenoid_Pityriasis-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-05-04T16:01:54.708920`; reported citation count `39`.
- OpenScientist: `Acute_Lichenoid_Pityriasis-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-05T00:43:15.812091`; reported citation count `41`.
- Citation-file overlap: 0 shared refs, 9 Falcon-only refs, 41 OpenScientist-only refs.
- YAML integration after backfill: 3 references linked to Falcon outputs, 38 references linked to OpenScientist outputs, 0 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: T-cell-predominant lichenoid cutaneous inflammation; Keratinocyte injury and epidermal necrosis; Triggered immune reaction.
The structured phenotype surface used for curation includes: Papules; Skin ulcer; Scaling skin; Pruritus; Scarring; Hypopigmented skin patches.
Shared mechanistic vocabulary detected in both reports includes: ncbi, pleva, fumhd, patients, children, t-cell, case, cases, skin, pityriasis, studies, uberon.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: 1. Disease Information, 2. Etiology, Genetic risk factors (causal variants, susceptibility loci, modifier genes), Genetic protective factors (protective variants, modifier alleles), Environmental protective factors (diet, lifestyle, exposures that reduce risk), 3. Phenotypes, For each phenotype, provide, Age of symptom onset (neonatal, childhood, adult-onset, late-onset).
- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
- > **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
Falcon-only citations retained for curation include: DOI:10.1007/s13671-013-0054-x, DOI:10.1007/s13671-023-00380-1, DOI:10.1007/s40257-016-0216-2, DOI:10.1016/j.jped.2024.03.011, DOI:10.1111/bjd.18977, DOI:10.24875/bmhim.22000043, DOI:10.35755/jmedassocthai.2025.5.377-383-02606, DOI:10.4081/dr.2023.9742, DOI:10.70672/bcfbzp08.

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Pityriasis lichenoides et varioliformis acuta (PLEVA), Mucha-Habermann disease (MHD), Acute parapsoriasis.
- Degos disease (referring to the 1966 description by Degos of the febrile ulceronecrotic variant)
- **Streptococcal infections**: A case of PLC manifesting ten days after streptococcal pharyngitis has been documented ([PMID: 39365630](https://pubmed.ncbi.nlm.nih.gov/39365630/))
- **Varicella (chickenpox)**: FUMHD following suspected hemorrhagic chickenpox has been reported in a 20-month-old boy ([PMID: 25627543](https://pubmed.ncbi.nlm.nih.gov/25627543/))
- **SARS-CoV-2 infection/vaccination**: A systematic review identified 14 cases of PL following COVID-19 infection or vaccination, with one case recurring after vaccination suggesting a possible association ([PMID: 36688177](https://pubmed.ncbi.nlm.nih.gov/36688177/))
- PLEVA is not classified among the autoinflammatory keratinization diseases (AiKDs), unlike keratosis lichenoides chronica which involves NLRP1 mutations ([PMID: 38103162](https://pubmed.ncbi.nlm.nih.gov/38103162/))
OpenScientist-only citations retained for curation include: PMID:11974501, PMID:12203210, PMID:17456915, PMID:20408509, PMID:23488769, PMID:25627543, PMID:25816855, PMID:27502793, PMID:29210716, PMID:29851705, PMID:31032790, PMID:31318465, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
