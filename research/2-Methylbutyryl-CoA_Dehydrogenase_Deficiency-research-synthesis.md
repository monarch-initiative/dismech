# 2-Methylbutyryl-CoA Dehydrogenase Deficiency Research Synthesis
## Compared sources
- Falcon: `2-Methylbutyryl-CoA_Dehydrogenase_Deficiency-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-02-23T23:38:51.539350`; reported citation count `34`.
- OpenScientist: `2-Methylbutyryl-CoA_Dehydrogenase_Deficiency-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-04T22:51:02.264138`; reported citation count `24`.
- Citation-file overlap: 0 shared refs, 11 Falcon-only refs, 24 OpenScientist-only refs.
- YAML integration after backfill: 3 references linked to Falcon outputs, 20 references linked to OpenScientist outputs, 2 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: ACADSB molecular function deficiency; Impaired isoleucine catabolism via SBCAD loss-of-function; Metabolic rerouting via the R-pathway of isoleucine oxidation; Stress-sensitive metabolic decompensation; ACAD substrate promiscuity and compensatory enzymology.
The structured phenotype surface used for curation includes: Developmental delay; Seizures; Muscular hypotonia; Failure to thrive; Microcephaly; Autism; Dyskinetic cerebral palsy; Skeletal muscle atrophy.
Shared mechanistic vocabulary detected in both reports includes: acid, metabolic, patients, acadsb, gene, sbcad, stress, screening, deficiency, mutations, hmong, asymptomatic.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: 1. Core Pathophysiology, 2. Key Molecular Players, 3. Biological Processes (for GO annotation), 4. Cellular Components, 5. Disease Progression, 6. Phenotypic Manifestations, Include direct quotes where possible to support key statements, Pathophysiology description.
- Comprehensive Research Report: 2-Methylbutyryl-CoA Dehydrogenase Deficiency (SBCAD deficiency; "2-methylbutyrylglycinuria")
- Disease entity: 2-methylbutyryl-CoA dehydrogenase deficiency (also called short/branched-chain acyl-CoA dehydrogenase deficiency; SBCADD/SBCAD deficiency). (porta2019clinicalbiochemicaland pages 1-2)
- MONDO: MONDO_0012392 (2-methylbutyryl-CoA dehydrogenase deficiency) (derived from Open Targets disease record for this entity; evidence snippets were not returned, but the MONDO identifier itself was returned by the tool call). (calcar2013prevalenceandmutation pages 1-3)
- OMIM: sources variably cite OMIM 600301 and/or 610006 for SBCAD deficiency; some texts also use OMIM 600301 for the gene entry and OMIM 610006 for the disease phenotype entry. (lin2019biochemicalclinicaland pages 1-2, porta2019clinicalbiochemicaland pages 1-2)
- SBCAD is a mitochondrial acyl-CoA dehydrogenase (ACAD) family enzyme. ACAD enzymes catalyze alpha,beta-dehydrogenation of acyl-CoAs and transfer electrons to electron transferring flavoprotein (ETF). (jaffar2010characterizationofnew pages 1-2)
Falcon-only citations retained for curation include: DOI:10.1002/jimd.12642, DOI:10.1007/978-1-4939-1923-9\_11, DOI:10.1016/j.ymgme.2006.07.010, DOI:10.1016/j.ymgme.2010.04.014, DOI:10.1016/j.ymgme.2013.03.021, DOI:10.1186/s13023-025-04163-8, DOI:10.1373/clinchem.2004.043265, DOI:10.1515/jpem-2018-0311, DOI:10.1542/peds.112.1.74, DOI:10.3389/fgene.2019.00802, DOI:10.3389/fgene.2024.1387423.

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Short/branched-chain acyl-CoA dehydrogenase deficiency (SBCADD), SBCAD deficiency, Information Sources.
- **Hmong ancestry**: The c.1165A>G founder mutation has extremely high carrier frequency in the Hmong population. In Wisconsin, "Of the remaining 92 confirmed SBCADD cases, 90 were of Hmong descent" ([PMID: 23712021](https://pubmed.ncbi.nlm.nih.gov/23712021/))
- **Somali/Eritrean ancestry**: The c.303+3A>G splice variant is "relatively prevalent in this population" ([PMID: 17883863](https://pubmed.ncbi.nlm.nih.gov/17883863/))
- **Consanguinity**: Increases risk for homozygous pathogenic variants, as shown in Iranian cases ([PMID: 41527137](https://pubmed.ncbi.nlm.nih.gov/41527137/), [PMID: 36604934](https://pubmed.ncbi.nlm.nih.gov/36604934/))
- **Metabolic stress**: Illness, fever, fasting, and catabolic states may trigger metabolic decompensation in susceptible individuals
- **Valproic acid exposure**: Valproyl-CoA competitively inhibits SBCAD activity (Ki = 249 +/- 29 uM) ([PMID: 21430231](https://pubmed.ncbi.nlm.nih.gov/21430231/)), potentially worsening the metabolic block
OpenScientist-only citations retained for curation include: PMID:12837870, PMID:15615815, PMID:17883863, PMID:17945527, PMID:20547083, PMID:21290185, PMID:21430231, PMID:22967964, PMID:23499962, PMID:23712021, PMID:27727436, PMID:29185933, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
