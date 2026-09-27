# OpenScientist report assessment: innate_first_bystander_model

WEAKLY_SUPPORTED_UNRESOLVED — assessed 2026-09-04T23:52:33.449953+00:00

Innate component pathways are credible, but the defining human innate-first/bystander temporal sequence remains weakly supported and unresolved. Mouse perturbations and human-derived cultures demonstrate selected mechanisms; the human arm of the key cDC/T-cell/pDC study is serum association, not tissue validation. The prior assessment is retained and extended: the cited third-pathway review is misclassified, but a separate primary pDC/NET study does exist. The report also misstates healthy-control responses, autoantibody denominators, trial absence and genetic interpretation. Oligoclonality opposes a purely nonspecific adaptive response without excluding the seed hypothesis partly-bystander component. Missing artifacts and search records prevent reproducing provider analyses.

The authoritative YAML preserves and updates the prior July 31 assessment. The disease review incorporates the validated mechanisms with explicit species, assay, denominator and temporal limits. No provider-executed raw-data reanalysis is established.

## Provenance and execution

- **Reported PubMed screening and literature synthesis (UNVERIFIABLE)**: The full report and citation sidecar were inspected. The report body links 25 distinct PMID records, while the provider claims 79 primary papers and 15 findings; some cited records are reviews. No complete screening list, query responses, retrieval timestamps or execution logs establish provider search coverage. The assessor independently inspected all 51 unique PMID sources across both reports and additional primary/guideline studies; this does not verify provider execution.
- **ClinicalTrials.gov and claimed gene-curation searches (UNVERIFIABLE)**: No saved provider database queries establish negative search claims. Independent review checked six ClinicalTrials.gov protocols and status on 2026-09-04. NCT04660565 was registered in 2020, contradicting the innate report claim that belimumab has not been tested in IgG4-RD. GenCC/ClinGen Mendelian validity curation is not interchangeable with polygenic GWAS susceptibility.
- **Published human tissue, repertoire, cohort and mouse experiments (CITED_NOT_ACCESSED)**: Findings are taken from publications, not provider-generated analyses. No selected raw matrix, participant-level dataset, metadata harmonization, quality-control code or reproducible statistical run is supplied. Public GEO records in the disease YAML are independent curation, not evidence of provider access.
- **Provider figure and provenance bundle (UNVERIFIABLE)**: All 18 paths declared in frontmatter are absent: openscientist_artifacts/final_report.html, openscientist_artifacts/final_report.pdf, openscientist_artifacts/provenance_causal_chain_diagram.json, openscientist_artifacts/provenance_causal_chain_diagram.png, openscientist_artifacts/provenance_claim_classification.json, openscientist_artifacts/provenance_claim_classification.png, openscientist_artifacts/provenance_evidence_matrix.json, openscientist_artifacts/provenance_evidence_matrix.png, openscientist_artifacts/provenance_plot_1.json, openscientist_artifacts/provenance_plot_1.png, openscientist_artifacts/provenance_plot_2.json, openscientist_artifacts/provenance_plot_2.png, openscientist_artifacts/provenance_plot_3.json, openscientist_artifacts/provenance_plot_3.png, openscientist_artifacts/provenance_plot_4.json, openscientist_artifacts/provenance_plot_4.png, openscientist_artifacts/provenance_two_phase_model.json, openscientist_artifacts/provenance_two_phase_model.png. No code, environment manifest or checksums permit regeneration.
- **Proposed longitudinal, spatial, coculture, transfer and intervention studies (UNVERIFIABLE)**: Future designs only; no enrolled preclinical cohort, acquired raw tissues or executed perturbation dataset is documented.

## Claim assessment

### innate-first-temporal-ordering — QUALIFIED

Innate-first temporal ordering is demonstrated in one induced mouse model of autoimmune pancreatitis, but not in human IgG4-RD.

PMID:39264798 uses repeated poly(I:C) administration in MRL/MpJ mice to establish a cDC-to-T-cell-to-pDC sequence. Its human arm measured serum CXCL9, CXCL10, and CCL25 cross-sectionally in 33 AIP/IgG4-RD patients, with paired pre/post-prednisolone measurements in a 14-patient subset. It did not observe lesion initiation or temporal ordering in people. The paper itself says a similar human loop is possible, which is narrower than the report's claim of strong human-relevant temporal support.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/).

### slc29a3-model-specificity — QUALIFIED

Constitutive TLR7 activation is sufficient for autoimmune sialadenitis in Slc29a3-deficient mice, not for a faithful model of systemic human IgG4-RD.

PMID:41332187 demonstrates salivary dysfunction, acinar-cell injury, lymphocyte infiltration, and chemokine production in Slc29a3-deficient mice. The human comparison is shared salivary-gland chemokine expression. The study does not reproduce IgG4 biology, storiform fibrosis, obliterative phlebitis, or systemic IgG4-RD, and autoimmune sialadenitis is also a feature of Sjögren syndrome. It supports an innate TLR7 route to salivary inflammation, with disease-specific extrapolation unresolved. Injury includes Aqp5-positive intercalated duct cells, not only acinar cells. The mouse mechanistic conclusion concerns TLR7; the TLR8 statement concerns broader SLC29A3-associated innate biology. Presence of lymphocyte infiltration precludes claiming isolated innate-cell sufficiency without adaptive-compartment exclusion experiments.

Sources: [PMID:41332187](https://pubmed.ncbi.nlm.nih.gov/41332187/).

### three-independent-innate-pathways — QUALIFIED

Primary ex vivo studies support NOD2-monocyte and TLR-basophil routes to IgG4 production, but the report does not establish three independent in-vivo pathways in IgG4-RD.

PMID:21971969 and PMID:22744834 are primary PBMC or cell-culture studies showing BAFF-associated IgG4 production after innate-receptor stimulation, including experiments using healthy-control cells. PMID:27744509 is a review rather than a third independent primary study. These data establish biological plausibility for T-cell-independent IgG4 production in culture, but not redundant in-vivo operation, disease initiation, or temporal priority in patients. PMID:26297761, cited elsewhere in the same report, does provide primary patient-pDC/NET/control-B-cell culture evidence for IgG4 production. Thus the earlier assessment citation criticism stands, but should not imply no primary third component exists. T-cell-independent production assays are not direct demonstration of de-novo class-switch recombination or three redundant in-vivo pathways.

Sources: [PMID:21971969](https://pubmed.ncbi.nlm.nih.gov/21971969/), [PMID:22744834](https://pubmed.ncbi.nlm.nih.gov/22744834/), [PMID:27744509](https://pubmed.ncbi.nlm.nih.gov/27744509/), [PMID:26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/).

### adaptive-bystander-interpretation — QUALIFIED

The adaptive response is antigen-selected and cannot be described as purely bystander, while a concomitant or earlier bystander component has not been excluded.

PMID:24815737 directly shows oligoclonality, extensive somatic hypermutation, self-reactivity, and de novo clones at relapse; PMID:26971690 shows clonally expanded CD4-positive CTLs. Those findings strongly reject a purely nonspecific explanation for the established adaptive response. The seed hypothesis, however, says plasmablast expansion arises "partly" as a downstream bystander response. The repertoire data do not test or exclude a simultaneous nonspecific component, nor do they establish what initiated antigen selection.

Sources: [PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/), [PMID:26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/).

### anti-cd19-proves-necessity — REJECTED

Anti-CD19 efficacy establishes therapeutic relevance of the B-lineage compartment, not the biological necessity of antigen-specific adaptive responses for every form or phase of IgG4-RD.

The randomized MITIGATE trial (PMID:39541094) shows that inebilizumab markedly reduces flares and improves remission outcomes. That is strong interventional evidence that CD19-positive cells are therapeutically important. Anti-CD19 depletion affects several B-lineage functions, including antigen presentation, cytokine support, and plasmablast compartments; the trial does not isolate antigen-specific adaptation or prove that every untreated lesion requires that compartment. "Necessary" and "conclusively" exceed the trial's mechanistic resolution.

Sources: [PMID:39541094](https://pubmed.ncbi.nlm.nih.gov/39541094/).

### cytokines-not-epiphenomena — REJECTED

Serum IFN-alpha and IL-33 are activity-associated biomarkers, but their causal role in human disease is not established.

PMID:32938972 reports higher serum concentrations, correlation with serum IgG4, comparable diagnostic discrimination, and decline after prednisolone. Correlation and response to broad immunosuppression support biomarker utility; they cannot distinguish causal mediators from downstream markers that track inflammatory burden.

Sources: [PMID:32938972](https://pubmed.ncbi.nlm.nih.gov/32938972/).

### two-phase-transition-gap — RETAINED

The proposed innate-initiation to adaptive-amplification transition has not been observed longitudinally in humans.

The report correctly identifies the central missing edge. Mouse temporal data and human cross-sectional evidence can be arranged into a coherent two-phase narrative, but no study tracks an initially polyclonal human response becoming an oligoclonal, somatically hypermutated response. Retaining this gap prevents component-pathway evidence from being mistaken for validation of the integrated mechanism.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/), [PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/).

### two-phase-reframing — QUALIFIED

An innate-initiation/adaptive-amplification model is a useful hypothesis, but it is a substantive reframing rather than validation of the original bystander mechanism.

The reframing appropriately removes the pure-bystander implication and accommodates adaptive clonality. Its defining transition and temporal ordering in humans remain untested, so the synthesis should be retained as an alternative model and discriminating experiment, not promoted as a partially validated causal chain.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/), [PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/).

### status-recommendation — REJECTED

The original composite hypothesis should remain ALTERNATIVE until its defining temporal and transition claims are demonstrated in humans.

Component evidence supports innate involvement, but the report's own reframing removes the original bystander premise and introduces an unobserved two-phase transition. Promoting the composite status would conflate model-system and ex-vivo support for individual pathways with validation of human temporal ordering. ALTERNATIVE remains the calibrated status while the proposed longitudinal tests are outstanding.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/), [PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/).

### human-tissue-validation — REJECTED

The cDC-to-T-cell-to-pDC sequence was not validated in human tissue by the cited study.

PMID:39264798 performed temporal, depletion, receptor-blocking and sorted-cell coculture experiments in female MRL/MpJ mice. The human component was serum chemokines in 33 patients versus 12 chronic-pancreatitis and 8 healthy controls, with 14 paired prednisolone samples. No human tissue perturbation or preclinical trajectory was demonstrated. The mouse CXCR3-positive cells also lacked the SLAMF7/granzyme-B phenotype of the human CTLs.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/).

### innate-culture-controls — REJECTED

Healthy-control cells can respond to microbial ligands; disease enrichment is not absolute specificity.

PMID:39241273 reports broader microbial-motif responses in patients compared with limited motifs in controls, with both IgG1 and IgG4 outputs. NOD2 and basophil primary studies also demonstrate healthy-control responses. These findings support altered responsiveness, not a binary disease-exclusive switch.

Sources: [PMID:39241273](https://pubmed.ncbi.nlm.nih.gov/39241273/), [PMID:21971969](https://pubmed.ncbi.nlm.nih.gov/21971969/), [PMID:22744834](https://pubmed.ncbi.nlm.nih.gov/22744834/).

### igg4-production-vs-switching — QUALIFIED

IgG4 production assays do not by themselves demonstrate direct de-novo class switching.

PMID:21971969 and 22744834 measure antibody production after receptor stimulation; the pDC/NET experiment is separate. Evidence for BAFF-associated T-cell-independent output is useful but cannot substitute for tracking recombination, isotype transitions and precursor-cell fates in vivo.

Sources: [PMID:21971969](https://pubmed.ncbi.nlm.nih.gov/21971969/), [PMID:22744834](https://pubmed.ncbi.nlm.nih.gov/22744834/), [PMID:26297761](https://pubmed.ncbi.nlm.nih.gov/26297761/).

### autoantibody-denominator — QUALIFIED

The four-antigen frequencies use a complete-panel subset and cannot establish a secondary temporal event.

The overall cohort had 100 participants but the complete four-antigen panel had 86:32/86 positive and 12/86 multiple. A negative limited antigen panel is not absence of autoreactivity. Severity correlations do not date antibody appearance or show that diversification follows an innate initiating phase.

Sources: [PMID:31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/).

### conditional-microbiota — QUALIFIED

Microbiota experiments demonstrate conditional amplification, not spontaneous transfer of the whole human disease.

FMT recipients received 10-microgram poly(I:C), and gut-barrier/S. sciuri experiments required poly(I:C). The latter exacerbated pancreatitis but not sialadenitis. Their model-specific effects are incorporated without assigning a proven human microbial initiator.

Sources: [PMID:31287532](https://pubmed.ncbi.nlm.nih.gov/31287532/), [PMID:36044992](https://pubmed.ncbi.nlm.nih.gov/36044992/).

### fcgr2b-expression-direction — QUALIFIED

Susceptibility associations do not distinguish innate-first from adaptive-first causation.

The Japanese GWAS identifies HLA-DRB1 p 1.1e-11 and FCGR2B p 2.0e-8, with rs1340976 associated with increased FCGR2B expression p 2.7e-10. Fc-gamma-RIIb is also a B-cell receptor regulator, not an exclusively innate marker. Chinese data support polygenic risk but do not assign a causal gene/function to every locus. The YAML uses RISK_FACTOR, not Mendelian causation.

Sources: [PMID:38229354](https://pubmed.ncbi.nlm.nih.gov/38229354/), [PMID:41298177](https://pubmed.ncbi.nlm.nih.gov/41298177/).

### c4-copy-number-scope — QUALIFIED

C4 copy-number directions are nominal associations in a specific ancestry, not a proven causal complement pathway.

PMID:41197642 gives C4A protective beta-0.127 p 0.0079 and C4B risk beta 0.151 p 0.019 in joint analysis, not genome-wide-significant C4 tests. FCGR2B replication, HLA residues and Mikulicz-specific PTCH1/lncRNA loci have different scopes. Genetic association does not establish innate temporal priority.

Sources: [PMID:41197642](https://pubmed.ncbi.nlm.nih.gov/41197642/).

### fgfbp2-uncited — NEEDS_VERIFICATION

The proposed FGFBP2 family mechanism lacks a traceable supporting citation in the report.

The assertion says one-family evidence plus cohort enrichment but supplies no linked primary reference, variant, pedigree, assay or dataset. It is not promoted to a causative gene or proven CTL-to-fibroblast edge pending source verification.

### belimumab-trial-exists — REJECTED

A belimumab trial was registered years before the report.

NCT04660565 was first submitted September 2020 and describes randomized open-label maintenance treatment in IgG4-RD, with planned enrollment 60. Current status UNKNOWN and absent published efficacy do not negate its existence. This is a failed absence claim; the registry phase IV label does not prove disease-specific approval. BAFF intervention also affects B-cell survival and cannot independently discriminate innate versus adaptive initiation.

Sources: [clinicaltrials:NCT04660565](https://clinicaltrials.gov/study/NCT04660565).

### new-nondepleting-randomized-trial — QUALIFIED

The report omits a randomized nondepleting B-cell trial available before its search date.

INDIGO PMID:42233621 was published June 2 before the July 6 report:194 randomized, obexelimab coengaging CD19/Fc-gamma-RIIb without depletion, flare HR 0.44. This complements MITIGATE but does not isolate an antigen-specific adaptive function. Abatacept also had a published 10-person proof-of-concept trial; later rilzabrutinib phase IIa results are uncontrolled and postdate the report.

Sources: [PMID:42233621](https://pubmed.ncbi.nlm.nih.gov/42233621/), [PMID:35425928](https://pubmed.ncbi.nlm.nih.gov/35425928/), [PMID:42481271](https://pubmed.ncbi.nlm.nih.gov/42481271/).

### innate-th2-pathway-scope — QUALIFIED

TLR7/IL-33 and IL-33/ST2/MMP12 evidence supports amplification without establishing human initiation or treatment efficacy.

PMID:31339007 combines 15 human IgG4-RD glands with comparison groups, macrophage agonist cultures and huTLR7 mice. PMID:39299101 includes nine IgG4-related ophthalmic cases and a LatY136F mouse system. Tissue expression and experimental MMP12 induction do not prove storiform architecture or human therapeutic efficacy. The YAML encodes this bounded pathway and model limitations.

Sources: [PMID:31339007](https://pubmed.ncbi.nlm.nih.gov/31339007/), [PMID:39299101](https://pubmed.ncbi.nlm.nih.gov/39299101/).

### omics-and-curation-absence — QUALIFIED

Unlogged database searches and undefined large-scale thresholds cannot establish a broad absence of relevant curation or omics.

No saved query responses support the negative database claims. The disease already has two deposited GEO expression datasets, and published single-cell studies exist. Those do not prove a large integrated multi-omics resource exists, but the scope and size threshold must be explicit. GenCC gene-disease validity curation is not a general submission channel for polygenic GWAS loci.

Sources: [PMID:37561593](https://pubmed.ncbi.nlm.nih.gov/37561593/), [PMID:38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/).

### reported-79-primary-papers — NEEDS_VERIFICATION

The claimed 79-primary-paper review and figure bundle cannot be reproduced from the repository.

Only 25 distinct linked PMID records are present and include reviews. All 18 declared artifact files are missing, including final-report HTML/PDF and provenance JSON/PNG. No provider raw-data analysis or screening coverage is reproducible.

### study-design-discrimination — QUALIFIED

The proposed experiments must measure actual temporal order and distinguish overlapping intervention targets.

Diagnosis-time recruitment does not observe disease initiation, and a single-organ patient is not inherently early-stage. Spatial periphery is not temporal upstream. BAFF or BTK effects would not discriminate innate initiation from established adaptive amplification; receptor-specific mouse induction and antagonist matching must be considered. Longitudinal immune signatures at diagnosis, including the small diagnosis-time study (PMID:42277154), still do not provide preclinical onset trajectories.

Sources: [PMID:39264798](https://pubmed.ncbi.nlm.nih.gov/39264798/), [PMID:42277154](https://pubmed.ncbi.nlm.nih.gov/42277154/).
