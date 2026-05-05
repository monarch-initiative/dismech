# Acute Annular Outer Retinopathy Research Synthesis
## Compared sources
- Falcon: `Acute_Annular_Outer_Retinopathy-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-05-04T15:52:28.518206`; reported citation count `23`.
- OpenScientist: `Acute_Annular_Outer_Retinopathy-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-04T23:57:26.565227`; reported citation count `27`.
- Citation-file overlap: 0 shared refs, 8 Falcon-only refs, 27 OpenScientist-only refs.
- YAML integration after backfill: 4 references linked to Falcon outputs, 25 references linked to OpenScientist outputs, 2 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: Acute outer retinal photoreceptor injury; Retinal pigment epithelium disruption and atrophy; Suspected immune-mediated outer retinopathy.
The structured phenotype surface used for curation includes: Scotoma; Visual field loss; Photopsia; Color vision defect.
Shared mechanistic vocabulary detected in both reports includes: aaor, outer, azoor, patients, visual, acute, retinal, retinopathy, photoreceptor, annular, involvement, imaging.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: Comprehensive Disease Characteristics Report: Acute Annular Outer Retinopathy (AAOR), Scope and evidence base, 1. Disease Information, 1.1 What is the disease?, 1.2 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO), 1.3 Common synonyms / alternative names, Synonyms and near-synonyms appearing across sources include, 1.4 Evidence source type.
- *Table: This table compiles the main clinically relevant features of acute annular outer retinopathy from the available case-based literature and recent reviews. It is useful as a quick reference for disease definition, imaging, hypothesized mechanisms, and the limited treatment evidence.*
- **Acute annular outer retinopathy as a variant of AZOOR** (formulation used in classic title/description) (donald1995acuteannularouter pages 1-3)
- In some review contexts, AAOR is discussed as an **AZOOR-complex/AZOOR-variant** entity. (interlandi2023acuteonsetretinalconditions pages 10-11)
- AAOR's etiology remains **unknown** in primary reports, with leading hypotheses centered on **immune-mediated** and/or **post-viral** processes.
- The original report concluded: "The cause of this disorder, which affects primarily the outer retina, was not determined," while speculating that the gray border "represents an immune ring phenomenon". (donald1995acuteannularouter pages 1-3)
Falcon-only citations retained for curation include: DOI:10.1001/archophthalmol.2007.5, DOI:10.1016/s0002-9394(00, DOI:10.1016/s0002-9394(14, DOI:10.1038/eye.2009.252, DOI:10.1097/icb.0000000000000070, DOI:10.1111/j.1442-9071.2005.01047.x, DOI:10.1186/s12886-022-02647-w, DOI:10.3390/jcm12175720.

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Acute Annular Outer Retinopathy (AAOR) -- primary name, Acute Outer Retinopathy (AOR) -- expanded spectrum term, proposed 2025, AZOOR variant / AZOOR with annular pattern.
- The etiology of AAOR remains **unknown** ([PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/)). The condition is considered to have a complex, non-genetic, likely autoimmune or post-infectious pathogenesis. Key etiological hypotheses include:
- **Possible paraneoplastic association**: Gupta et al. (2022) reported the first case of AAOR in a patient with invasive ductal breast carcinoma, where "the patient presented with photopsias and visual loss approximately 3 weeks prior to a diagnosis of invasive ductal breast carcinoma" ([PMID: 36434575](https://pubmed.ncbi.nlm.nih.gov/36434575/)).
- Roy & Dutta Majumder (2024) stated that AZOOR is "distinct from genetic disorders like retinitis pigmentosa, lacks a hereditary basis" ([PMID: 38454854](https://pubmed.ncbi.nlm.nih.gov/38454854/))
- **HIV infection**: Garcia-Torre & Castro-Florez (2019) reported the first AAOR case in an HIV-positive patient ([PMID: 30455116](https://pubmed.ncbi.nlm.nih.gov/30455116/))
- No genetic or environmental protective factors have been identified. This reflects the unknown etiology and extreme rarity of the condition.
OpenScientist-only citations retained for curation include: PMID:11078842, PMID:18195232, PMID:19847620, PMID:21031137, PMID:21056448, PMID:23591538, PMID:23765682, PMID:24428923, PMID:24945598, PMID:25266678, PMID:25372319, PMID:25383859, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
