# 3-Hydroxy-3-Methylglutaric Aciduria Research Synthesis
## Compared sources
- Falcon: `3-Hydroxy-3-Methylglutaric_Aciduria-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-02-23T23:46:59.092195`; reported citation count `19`.
- OpenScientist: `3-Hydroxy-3-Methylglutaric_Aciduria-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-04T22:56:41.277250`; reported citation count `23`.
- Citation-file overlap: 0 shared refs, 7 Falcon-only refs, 23 OpenScientist-only refs.
- YAML integration after backfill: 2 references linked to Falcon outputs, 21 references linked to OpenScientist outputs, 0 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: HMGCL molecular function deficiency; Ketogenesis failure and energy crisis; Leucine catabolic block and organic acid accumulation; Acyl-CoA disequilibrium and secondary hyperammonemia; HMG-mediated neurotoxicity via mitochondrial dysfunction.
The structured phenotype surface used for curation includes: Metabolic acidosis; Hypoglycemia; Hyperammonemia; Seizures; Lethargy; Global developmental delay; Vomiting; Leukoencephalopathy.
Shared mechanistic vocabulary detected in both reports includes: metabolic, patients, acid, deficiency, hmgcld, gene, organic, stress, brain, lyase, hmgcl, oxidative.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: 1. Core Pathophysiology, 2. Key Molecular Players, 3. Biological Processes (for GO annotation), 4. Cellular Components, 5. Disease Progression, 6. Phenotypic Manifestations, Include direct quotes where possible to support key statements, Pathophysiology description.
- Title: Pathophysiology Research Report - 3-Hydroxy-3-Methylglutaric Aciduria (HMG-CoA Lyase Deficiency)
- OMIM/MIM. The disorder is reported as MIM/OMIM 246450 in a systematic review and in a large clinical cohort description. (grunert20203hydroxy3methylglutarylcoenzymealyase pages 1-2, alfadhel2022hmgcoalyasedeficiency pages 1-2)
- Causal gene/protein. Biallelic pathogenic variants in HMGCL cause deficiency of mitochondrial 3-hydroxy-3-methylglutaryl-CoA lyase (EC 4.1.3.4). HMGCL catalyzes cleavage of HMG-CoA to acetyl-CoA and acetoacetate, "the final step of ketogenesis and leucine degradation." (devanapalli2023useofsodium pages 1-3, devanapalli2023useofsodium pages 3-5)
- 2.1 Primary mechanism: ketogenesis failure -> energy failure in brain/heart during catabolic stress
- 2.2 Primary mechanism: leucine catabolic block -> accumulation of organic acids and acyl-CoA stress
Falcon-only citations retained for curation include: DOI:10.1186/s13023-020-1319-7, DOI:10.1371/journal.pone.0060581, DOI:10.20517/jtgg.2023.12, DOI:10.3389/fgene.2022.880464, DOI:10.3390/biomedicines12071563, DOI:10.3390/metabo14080421, DOI:10.3390/nu15030531.

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, HMG-CoA lyase deficiency, HMGCLD, Hydroxymethylglutaric aciduria.
- Comprehensive Disease Characterization: 3-Hydroxy-3-Methylglutaric Aciduria (HMG-CoA Lyase Deficiency)
- As described by Grnert et al. (2017): *"3-Hydroxy-3-methylglutaryl-coenzyme A lyase deficiency (HMGCLD) is a rare inborn error of ketone body synthesis and leucine degradation, caused by mutations in the HMGCL gene"* ([PMID: 28583327](https://pubmed.ncbi.nlm.nih.gov/28583327/)).
- Information is derived from aggregated disease-level resources (OMIM, Orphanet, GeneReviews, HPO, ClinVar) supplemented by published case series, cohort studies, and individual patient reports in the peer-reviewed literature.
- HMGCLD is exclusively a **genetic** disorder. The primary cause is biallelic (homozygous or compound heterozygous) loss-of-function mutations in the **HMGCL** gene located on chromosome 1p36.11. The gene encodes a 325-amino acid mitochondrial protein (UniProt: P35914) that functions as a homodimer.
- Codons 41 and 42 are mutational hotspots, accounting for 26% of all mutant alleles in one large study ([PMID: 9463337](https://pubmed.ncbi.nlm.nih.gov/9463337/))
OpenScientist-only citations retained for curation include: PMID:17173698, PMID:17391418, PMID:19932602, PMID:24706027, PMID:26041581, PMID:26997609, PMID:28220407, PMID:28396157, PMID:28583327, PMID:32685354, PMID:34329521, PMID:34573903, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
