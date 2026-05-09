# Acute Hypotension Research Synthesis
## Compared sources
- Falcon: `Acute_Hypotension-deep-research-falcon.md`; model `Edison Scientific Literature`; generated `2026-05-04T16:01:05.920712`; reported citation count `43`.
- OpenScientist: `Acute_Hypotension-deep-research-openscientist.md`; model `openscientist-autonomous`; generated `2026-05-05T00:19:52.068622`; reported citation count `66`.
- Citation-file overlap: 0 shared refs, 16 Falcon-only refs, 66 OpenScientist-only refs.
- YAML integration after backfill: 11 references linked to Falcon outputs, 66 references linked to OpenScientist outputs, 0 references linked to both.

## Convergent findings
Both reports were reconciled against the structured YAML entry, whose current pathophysiology focus includes: Reduced effective arterial perfusion; Shock physiology; Adrenergic compensation and vasopressor-responsive vascular tone.
The structured phenotype surface used for curation includes: Hypotension; Syncope; Acute kidney injury.
Shared mechanistic vocabulary detected in both reports includes: ncbi, hypotension, shock, acute, mortality, mmhg, septic, injury, patients, cardiac, hemorrhagic, hemodynamic.
No exact PMID/DOI overlap was detected in the citation files; integration therefore preserves provider-specific literature trails through `references[].found_in`.

## Falcon emphasis
Falcon used the pathophysiology-focused prompt and is most useful for mechanism-first curation: pathophysiology nodes, causal chains, molecular players, cell/process annotations, and concise mechanistic evidence. Parsed report sections included: 1. Disease Information, 2. Etiology, Genetic risk factors (causal variants, susceptibility loci, modifier genes), Genetic protective factors (protective variants, modifier alleles), Environmental protective factors (diet, lifestyle, exposures that reduce risk), 3. Phenotypes, For each phenotype, provide, Age of symptom onset (neonatal, childhood, adult-onset, late-onset).
- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
- > **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
Falcon-only citations retained for curation include: DOI:10.1002/emp2.13095, DOI:10.1007/s00134-023-07304-4, DOI:10.1097/aln.0000000000004958, DOI:10.1097/ccm.0000000000006135, DOI:10.1097/ta.0000000000004306, DOI:10.1186/s13049-023-01091-z, DOI:10.1186/s13054-020-03412-5, DOI:10.1371/journal.pone.0312966, DOI:10.21203/rs.3.rs-9541628/v1, DOI:10.2500/jfa.2024.6.240002, DOI:10.31744/einstein\_journal/2024rw0775, DOI:10.31744/einstein_journal/2024rw0775, ...

## OpenScientist emphasis
OpenScientist used the broader disease-characteristics prompt and is most useful as a breadth check across etiology, diagnostics, prognosis, treatment, model systems, and evidence gaps while still covering mechanisms. Parsed report sections included: Comprehensive Disease Characterization Report: Acute Hypotension, Summary, 1. Disease Information, Overview, Key Identifiers, Synonyms and Alternative Names, Low blood pressure (acute), Arterial hypotension.
- {{figure:acute_hypotension_overview.png|caption=Comprehensive overview of acute hypotension: classification by hemodynamic mechanism, blood pressure thresholds, organ damage associations, and management algorithm}}
- Data for this report are derived from aggregated disease-level resources including international clinical guidelines (Surviving Sepsis Campaign 2021), meta-analyses of clinical trials, observational cohort studies from electronic health records, animal model experiments, and systematic reviews indexed in PubMed.
- Acute hypotension arises from four fundamental hemodynamic mechanisms, each with distinct causal pathways:
- Acute hypotension is primarily an acquired syndrome, but genetic factors may influence susceptibility:
- **iNOS (NOS2) gene polymorphisms**: May influence the magnitude of NO-mediated vasodilation in sepsis, though definitive clinical associations remain under investigation.
OpenScientist-only citations retained for curation include: PMID:10551281, PMID:12709567, PMID:14529547, PMID:18980473, PMID:19628685, PMID:21326110, PMID:22483252, PMID:22942628, PMID:23114485, PMID:24944248, PMID:24994571, PMID:25600227, ...

## Contrast and curation implications
- Falcon and OpenScientist are complementary rather than interchangeable: Falcon is narrower and mechanism-oriented, while OpenScientist is broader and more clinical/contextual.
- Non-overlapping citations were kept because they point to different curator review paths: mechanistic substantiation from Falcon and broader clinical or translational substantiation from OpenScientist.
- The YAML integration preserves both trails through `references[].found_in`; references with cache-resolvable abstracts also received structured findings/evidence snippets during backfill.
- Provider disagreements or non-overlapping citations should be treated as prioritization cues for curator review rather than as direct contradictions unless the cited papers conflict on the same claim.

## Follow-up checks
- Review provider-specific citations with no shared PMID/DOI overlap for possible high-value additions to specific pathophysiology, phenotype, diagnostic, or treatment sections.
- Keep exact evidence snippets tied to fetched reference-cache text; do not promote report prose directly into YAML evidence without validating the cited abstract or source.
