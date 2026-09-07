# OpenScientist report assessment: plasmablast_autoantigen_fibrosis_driver_model

PARTIALLY_SUPPORTED — assessed 2026-09-04T23:52:33.426487+00:00

The adaptive cellular framework remains partially supported, with direct human-derived Tfh-to-B-cell and B-cell-to-fibroblast experiments strengthening components beyond the original report and prior assessment. B-lineage-to-CTL antigen presentation, CTL-specific fibroblast activation, organ tropism and obliterative phlebitis remain unresolved. The review corrects overinterpretation of clinical phenotype clusters, allergy prevalence, antibody isotypes, complement and biomarker correlations; distinguishes conditional mouse microbial amplification from human initiation; and adds omitted 2019 B-cell fibrosis experiments and the 2026 randomized nondepleting B-cell trial. Claims of exhaustive screening and generated figures remain unauditable. Both the report and its earlier assessment were reconciled against the expanded disease YAML.

The authoritative YAML preserves and updates the prior July 31 assessment. The disease review incorporates the validated mechanisms with explicit species, assay, denominator and temporal limits. No provider-executed raw-data reanalysis is established.

## Provenance and execution

- **Reported PubMed screening and literature synthesis (UNVERIFIABLE)**: The full report and citation sidecar were inspected. The report body links 33 distinct PMID records, while the provider claims 124 reviewed papers, 25 findings and 44 evidence items. No complete screening list, query responses, retrieval timestamps or execution logs establish provider search coverage. The assessor independently inspected all 51 unique PMID sources across both reports and additional primary/guideline studies; this does not verify provider execution.
- **ClinicalTrials.gov and claimed gene-curation searches (UNVERIFIABLE)**: No saved provider database queries establish negative search claims. Independent review checked six ClinicalTrials.gov protocols and status on 2026-09-04. NCT04660565 was registered in 2020, contradicting the innate report claim that belimumab has not been tested in IgG4-RD. GenCC/ClinGen Mendelian validity curation is not interchangeable with polygenic GWAS susceptibility.
- **Published human tissue, repertoire, cohort and mouse experiments (CITED_NOT_ACCESSED)**: Findings are taken from publications, not provider-generated analyses. No selected raw matrix, participant-level dataset, metadata harmonization, quality-control code or reproducible statistical run is supplied. Public GEO records in the disease YAML are independent curation, not evidence of provider access.
- **Provider figure and provenance bundle (UNVERIFIABLE)**: No artifact bundle is declared. Four figure placeholders refer to missing files: causal_model_iteration 4.png, evidence_summary_iteration 4.png, knowledge_gap_priority_final.png, final_investigation_summary.png. No code, environment manifest or checksums permit regeneration.
- **Proposed longitudinal, spatial, coculture, transfer and intervention studies (UNVERIFIABLE)**: Future designs only; no enrolled preclinical cohort, acquired raw tissues or executed perturbation dataset is documented.

## Claim assessment

### cellular-scaffold — QUALIFIED

The cellular scaffold has human association and functional Tfh-to-B-cell evidence, but not complete human causal mediation.

PMID:24815737 and PMID:26971690 establish plasmablast and CTL repertoire/tissue/treatment-associated findings; PMID:38092138 adds independent single-cell and spatial evidence. The report Tfh citations PMID:29253269 and PMID:35568079 primarily establish association and localization. Independently retrieved PMID:27411315, PMID:28916523 and PMID:29781221 provide functional patient-derived Tfh/B-cell coculture evidence for plasmablast differentiation or IgG4 production. These strengthen the earlier assessment, whose association-only description was incomplete. Lesional and circulating subsets and culture conditions differ; functional capacity in vitro does not establish universal in-vivo necessity.

Sources: [PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/), [PMID:26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/), [PMID:29253269](https://pubmed.ncbi.nlm.nih.gov/29253269/), [PMID:35568079](https://pubmed.ncbi.nlm.nih.gov/35568079/), [PMID:38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/), [PMID:27411315](https://pubmed.ncbi.nlm.nih.gov/27411315/), [PMID:28916523](https://pubmed.ncbi.nlm.nih.gov/28916523/), [PMID:29781221](https://pubmed.ncbi.nlm.nih.gov/29781221/).

### b-lineage-therapeutic-dependence — RETAINED

B-cell depletion supplies strong indirect support for B-lineage involvement, without identifying the function that sustains disease.

The report appropriately labels this evidence indirect. In PMID:38781535, all 33 patients responded at six months and deeper depletion predicted fewer later relapses. PMID:26971690 associates rituximab-induced remission with reduced disease-associated CTLs. These observations support B-lineage centrality but do not distinguish antigen presentation from cytokine, costimulatory, or other B-lineage effects.

Sources: [PMID:38781535](https://pubmed.ncbi.nlm.nih.gov/38781535/), [PMID:26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/).

### missing-apc-and-fibroblast-edges — RETAINED

The reviewed sources do not isolate B-lineage antigen presentation to CTLs or a CTL-specific fibroblast response; a direct B-cell-to-fibroblast route is established in culture.

PMID:27667138 calls continuous B-lineage antigen presentation "presumed." PMID:26971690 establishes CTL clonality and expression of IL-1beta and TGF-beta 1, not antigen-presenting-cell identity or fibroblast response. PMID:41766862 is a review that infers profibrotic activity from the available cellular evidence. These are the most consequential gaps in the integrated canonical chain. PMID:31319101, omitted by the report, directly shows patient B-cell/plasmablast stimulation of fibroblast collagen production and attenuation by PDGF-B blockade. This does not close the CTL-specific gap. The report search logs are absent, so a universal claim that no relevant study exists exceeds audited search coverage.

Sources: [PMID:27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/), [PMID:26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/), [PMID:41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/), [PMID:31319101](https://pubmed.ncbi.nlm.nih.gov/31319101/).

### pathogenic-autoantigen-count — QUALIFIED

Candidate autoantibody responses are documented, and anti-IL-1RA antibodies have functional in-vitro effects in a subset, but four broadly established pathogenic autoantigens have not been demonstrated.

In PMID:31612628, responses to PHB1, annexin A11, and laminin 511-E8 were infrequent and not significantly different from controls; broader autoreactivity correlated with severity, but causation was not tested. PMID:33974929 concerns a separate anti-IL-1RA specificity and shows neutralization plus inflammatory and fibrotic mediator production in vitro in a subset. The report conflates candidate autoreactivity, severity association, and functional pathogenicity.

Sources: [PMID:31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/), [PMID:33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/).

### phenotype-immune-subset-mapping — QUALIFIED

Four organ-distribution phenotypes are replicated, but the report does not provide primary phenotype-matched evidence that each is driven by a distinct immune-cell subset.

PMID:30612117 derives and replicates four clinical latent classes but does not immunophenotype their lesions. PMID:39306708 is explicitly a review that proposes phenotype-specific immune-cell interpretations. The synthesis is a useful lead, not a high-confidence human mechanistic result, and it cannot establish that the full seed chain applies mainly to retroperitoneal fibrosis or aortitis.

Sources: [PMID:30612117](https://pubmed.ncbi.nlm.nih.gov/30612117/), [PMID:39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/).

### igg1-contradicts-seed — REJECTED

Possible IgG1-mediated injury does not contradict a seed model that assigns IgG4-positive plasmablasts a marker and sustaining role while assigning fibrogenic effector activity to CD4-positive CTLs.

The seed description does not make the implied antibody-effector claim. PMID:39306708 is a review whose wording says Tfh1 and IgG1 "may be" important in an autoimmune phenotype; it is not primary evidence for a substantial IgG1-defined causal subset. PMID:41728618 is also a review and merely describes IgG4/IgG1 autoantibodies in organ-specific disease. IgG1 mechanisms remain a complementary lead, not a refutation.

Sources: [PMID:39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/), [PMID:41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/).

### atopy-establishes-copathogenesis — QUALIFIED

Allergy, eosinophilia, and hyper-IgE are common in IgG4-RD, but their causal or co-pathogenic contribution remains unresolved.

PMID:41912044 is a systematic review and meta-analysis of prevalence. Its abstract explicitly states that mechanistic connections and causality remain unclear and calls for controlled comparisons to establish whether the features are more prevalent than in other populations. Co-occurrence motivates stratified studies; it does not establish a competing driver or qualify CTL causality by itself.

Sources: [PMID:41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/).

### isolated-aortitis-phlebitis-inference — REJECTED

An isolated thoracic-aortitis series cannot establish the mechanism of obliterative phlebitis within confirmed IgG4-RD.

PMID:21036629 studied 11 patients with isolated thoracic aortitis; none had a history of IgG4-RD or developed it during follow-up. The authors concluded only that a subset "may represent" an aortic manifestation. IgG4-positive plasma cells outside confirmed IgG4-RD are not a counterfactual test of a plasma-cell-to-phlebitis edge in IgG4-RD. Moreover, the seed model does not claim that plasma-cell infiltration alone causes obliterative phlebitis.

Sources: [PMID:21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/).

### sil2r-proximate-driver — REJECTED

Soluble IL-2 receptor is an activity biomarker and cannot establish that T cells, rather than antibodies, are the proximate tissue-injury driver.

PMID:29465360 and PMID:29251035 correlate sIL-2R with disease activity, organ count, treatment response, or treatment requirement. PMID:25437196 correlates sIL-2R with PET total lesion glycolysis in 17 patients. None perturbs T-cell activity, measures tissue-injury mediation, or provides a fair mechanistic comparison with antibody effectors.

Sources: [PMID:29465360](https://pubmed.ncbi.nlm.nih.gov/29465360/), [PMID:29251035](https://pubmed.ncbi.nlm.nih.gov/29251035/), [PMID:25437196](https://pubmed.ncbi.nlm.nih.gov/25437196/).

### schema-status-recommendation — QUALIFIED

The model can remain CANONICAL while its unresolved edges are represented explicitly; CANONICAL-WITH-QUALIFICATIONS is not an available status.

The report's substantive point is sound: canonical does not mean every causal edge is established. Its proposed replacement value is not part of the disease schema. The scalable curation response is to retain CANONICAL, use qualified causal-link types and evidence, and record the missing APC, fibroblast, vascular, and organ-tropism mechanisms as explicit knowledge gaps.

### omitted-direct-b-fibrosis — QUALIFIED

Direct B-lineage profibrotic experiments provide a complementary route omitted from the purported complete model.

PMID:31319101 used patient and control B cells with primary pancreatic/skin fibroblasts, transwells, sorted subsets and PDGF-B blocking. Patient cells induced more collagen; control B cells also had activity, and comparable PDGF-B levels imply additional factors. LOXL2 expression was not exclusive to IgG4-positive plasma cells. Fibroblast EMT-related gene enrichment is not epithelial fate conversion, and the assay does not reconstruct storiform architecture. The YAML now separates B-lineage signaling, fibroblast activation and storiform matrix remodeling.

Sources: [PMID:31319101](https://pubmed.ncbi.nlm.nih.gov/31319101/).

### anti-il1ra-functional-scope — QUALIFIED

Anti-IL-1RA antibodies have functional activity in a subset, without proving IgG4-only pathogenicity.

The IL-1RA study expresses plasmablast-derived antibody, uses reporter assays and patient plasma with epithelial/fibroblast cultures, and measures inflammatory/profibrotic mediators. IgG4 predominates in many positive samples but other subclasses occur; mixed plasma assays do not isolate purified IgG4 effects or prove human tissue fibrosis. Anti-IL-1RA is also observed in SLE/RA. A scoped functional node and cell model were added.

Sources: [PMID:33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/).

### panel-denominator-and-temporality — QUALIFIED

A negative four-antigen panel neither excludes autoreactivity nor dates its onset.

PMID:31612628 included 100 patients overall, but the complete four-antigen panel used 86; 32/86 (37%) were positive and 12/86 (14%) had multiple reactivities. Frequencies for several antigens were low and not significantly different from controls. Cross-sectional severity associations cannot establish epitope spreading as a late event.

Sources: [PMID:31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/).

### isotype-transfer-precedent — QUALIFIED

IgG1-versus-IgG4 passive transfer has already been tested in a limited mouse system.

PMID:26964842 (2016) injected patient fractions into neonatal male BALB/c mice: both caused injury, IgG1 more strongly, and coadministered IgG4 reduced IgG1 injury. A humanized or phenotype-stratified follow-up is useful, but the experiment is not wholly novel and cannot assume IgG4 is universally inert or protective. The model records context-dependent isotype effects.

Sources: [PMID:26964842](https://pubmed.ncbi.nlm.nih.gov/26964842/).

### cholangiocyte-functional-specificity — QUALIFIED

Cholangiocyte experiments support protective machinery but do not establish pathogenicity of every candidate antibody.

PMID:34718050 uses ANXA11 knockdown and patient serum to show altered ANO1 trafficking and protection. PMID:38524667 shows laminin-knockdown and recombinant-laminin effects on bile-acid permeability/apoptosis, with 7/52 anti-laminin-positive patients. Gene knockdown is not equivalent to autoantibody neutralization. The YAML now represents this bounded biliary route.

Sources: [PMID:34718050](https://pubmed.ncbi.nlm.nih.gov/34718050/), [PMID:38524667](https://pubmed.ncbi.nlm.nih.gov/38524667/).

### allergy-distinct-denominators — QUALIFIED

Allergy, eosinophilia and hyper-IgE pooled estimates have different denominators.

PMID:41912044 gives allergy n=8233, eosinophilia n=4376 and hyper-IgE n=2353. Assigning all three estimates to 8233 patients is misleading; these prevalence estimates do not demonstrate Th2-mediated causal dominance. PMID:35568079 further distinguishes IL-10-positive LAG3-positive Tfh-rich IgG4-RD from IL-13-rich Kimura disease.

Sources: [PMID:41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/), [PMID:35568079](https://pubmed.ncbi.nlm.nih.gov/35568079/).

### phlebitis-anatomic-definition — REJECTED

Phlebitis is venous pathology and must not be conflated with arteritis.

Arterial/aortic inflammation is a distinct lesion. The isolated thoracic-aortitis cohort does not establish IgG4-RD or a venous mechanism. The YAML keeps obliterative phlebitis as an organ-variable histopathological hallmark with an explicit causal gap; no unsupported CTL-to-vascular-obliteration arrow was added.

Sources: [PMID:21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/), [PMID:22596100](https://pubmed.ncbi.nlm.nih.gov/22596100/).

### sil2r-cohort-attribution — REJECTED

The cited soluble IL-2 receptor study is mischaracterized numerically.

PMID:29465360 compared 43 IgG4-RD, 62 primary Sjogren and five sicca patients. The report n=26 label and quoted median 4667 versus 1515 pg/mL are not established by its cited abstract; supported correlations are retained without those values. sIL-2R is also an activity marker in Sjogren disease. PMID:29251035 normalization denominators and PMID:25437196 n=17 PET association cannot establish a proximate tissue-injury driver.

Sources: [PMID:29465360](https://pubmed.ncbi.nlm.nih.gov/29465360/), [PMID:29251035](https://pubmed.ncbi.nlm.nih.gov/29251035/), [PMID:25437196](https://pubmed.ncbi.nlm.nih.gov/25437196/).

### complement-mixed-complexes — QUALIFIED

Mixed immune-complex activation does not establish an IgG4-only causal renal pathway.

PMID:26357950 tests patient PEG-precipitated complexes with normal serum; classical and lectin-pathway consumption does not isolate antibody subclass. PMID:39798124 is a 70-person association study, with six cutaneous vasculitis cases and three skin biopsies, and anti-C1q did not predict relapse-free survival. Leukocytoclastic vasculitis is not obliterative phlebitis. The model adds complement activation and a complement readout, without declaring proven renal mediation.

Sources: [PMID:26357950](https://pubmed.ncbi.nlm.nih.gov/26357950/), [PMID:39798124](https://pubmed.ncbi.nlm.nih.gov/39798124/).

### conditional-microbiota-transfer — QUALIFIED

Microbiota transfer amplifies induced mouse pancreatitis rather than independently transmitting human disease.

Recipients also received low-dose 10-microgram poly(I:C), while donors received 100 micrograms. Barrier disruption and S. sciuri experiments also require the inducing context, and exacerbated pancreatitis but not sialadenitis. Human microbiome associations overlap systemic sclerosis and do not establish causal microbial specificity.

Sources: [PMID:31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/), [PMID:36044992](https://pubmed.ncbi.nlm.nih.gov/36044992/), [PMID:33648559](https://pubmed.ncbi.nlm.nih.gov/33648559/).

### marco-expression — QUALIFIED

MARCO upregulation identifies an associated cell program, not an initiating trigger.

PMID:26886650 expression and tissue-validation data do not perturb MARCO or establish human temporal ordering. MARCO is retained as a research lead rather than a causal initiating node.

Sources: [PMID:26886650](https://pubmed.ncbi.nlm.nih.gov/26886650/).

### fibrosis-autonomy — QUALIFIED

Self-sustaining fibrosis remains a hypothesis rather than a proven human feedback cycle.

PMID:41956965 is a review that proposes immune-stromal feedback; it does not demonstrate temporal autonomy after removal of immune input. The B-cell coculture supports one directed route, not a complete feedback cycle. The graph includes only the experimentally documented mouse pDC/T-cell return loop.

Sources: [PMID:41956965](https://pubmed.ncbi.nlm.nih.gov/41956965/), [PMID:31319101](https://pubmed.ncbi.nlm.nih.gov/31319101/), [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/).

### updated-b-cell-trial — QUALIFIED

Nondepleting B-cell inhibition adds randomized evidence without isolating the canonical APC-to-CTL pathway.

INDIGO PMID:42233621 was published June 2, 2026, before this June 4 report: 194 patients, obexelimab coengagement of CD19/Fc-gamma-RIIb without depletion, flare HR 0.44 with 26.8% versus 54.6% events. MITIGATE provides complementary CD19-depletion evidence and FDA adult approval followed in April 2025. Rilzabrutinib PMID:42481271 appeared after the report and is a small uncontrolled phase IIa study. The YAML distinguishes randomized efficacy, regulatory indication and preliminary activity.

Sources: [PMID:42233621](https://pubmed.ncbi.nlm.nih.gov/42233621/), [PMID:39541094](https://pubmed.ncbi.nlm.nih.gov/39541094/), [PMID:42481271](https://pubmed.ncbi.nlm.nih.gov/42481271/).

### exhaustive-search-provenance — NEEDS_VERIFICATION

Reported search counts and figure generation are not reproducible from committed evidence.

Only 33 PMID links and four missing figure placeholders are available. The omitted direct B-fibroblast and phase III studies constrain an exhaustive-coverage claim. No original numerical analysis is reproducible; later assessor retrieval does not establish provider execution.

### experimental-controls — QUALIFIED

The proposed studies need controls that separate cell depletion, antigen presentation and tissue-stage confounding.

Autologous B/CTL cocultures require viability, antigen-specificity, MHC-II, costimulation and cytokine controls. A positive coculture alone does not demonstrate in-vivo necessity. Spatial association does not date initiation; single-organ disease is not inherently early and multi-organ disease is not inherently late. Passive transfer must include pre-existing findings and evaluate species, Fc and isotype differences.

Sources: [PMID:26964842](https://pubmed.ncbi.nlm.nih.gov/26964842/), [PMID:31319101](https://pubmed.ncbi.nlm.nih.gov/31319101/), [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/).
