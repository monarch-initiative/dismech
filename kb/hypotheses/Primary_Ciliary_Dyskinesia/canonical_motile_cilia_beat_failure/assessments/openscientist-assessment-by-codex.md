# OpenScientist assessment: canonical_motile_cilia_beat_failure

Updated 5 September 2026. This replaces and expands the July narrative while preserving its useful claim judgments. The assessment YAML is authoritative.

The canonical transport-failure mechanism is supported, with distinct upstream motor, multiciliogenesis and central-apparatus transport routes. Several report extensions remain unproven, and its absence claims, universal formulations and clinical-mechanistic inferences need correction. This assessment expands and reconciles the July review after reading the complete provider report, citation sidecar, existing assessment, and disease YAML, and independently retrieving the material primary literature and current diagnostic/care guidance. No provider computation or primary omics analysis was reproduced.

## canonical-core — RETAINED

Human genetic, structural, functional-clearance, and clinical evidence converge on this core mechanism. The verdict applies to the scoped core, not to every additional branch assembled in the report.

[PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/), [PMID:31772028](https://pubmed.ncbi.nlm.nih.gov/31772028/), [PMID:42026914](https://pubmed.ncbi.nlm.nih.gov/42026914/)

## reduced-multiciliogenesis-route — RETAINED

Both genes reduce cilia generation and converge on clearance failure. Residual cilia in CCNO can retain normal motor proteins and motility; the MCIDAS primary report explicitly identifies absent DNAH5/CCDC39 in residual cilia. This corrects the July assessment that inadvertently generalized CCNO residual normality to both genes.

[PMID:24747639](https://pubmed.ncbi.nlm.nih.gov/24747639/), [PMID:25048963](https://pubmed.ncbi.nlm.nih.gov/25048963/)

## universal-clearance-absence — REJECTED

PMID:38076675 reports that clearance was consistently absent in most patients, not universally absent. One CCDC103 participant retained measurable clearance. The defensible conclusion is that severe clearance impairment spans many genotypes.

[PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/)

## mrna-causal-chain — QUALIFIED

The mouse airway-culture experiment restored DNAI1 incorporation and ciliary beat frequency. It did not measure mucociliary clearance, infection, inflammation, lung disease, or a human clinical outcome, so it validates an important proximal link rather than the full disease chain.

[PMID:40963409](https://pubmed.ncbi.nlm.nih.gov/40963409/)

## azithromycin-mechanistic-validation — QUALIFIED

BESTCILIA established fewer respiratory exacerbations during azithromycin treatment. It did not distinguish antimicrobial from immunomodulatory effects and therefore does not, by itself, validate the proposed causal route.

[PMID:32380069](https://pubmed.ncbi.nlm.nih.gov/32380069/)

## intrinsic-nos-vulnerability — QUALIFIED

Small human studies support low bronchial/alveolar NO and deficient NOS2 induction in cultured PCD cells. They do not establish a shared molecular consequence of diverse PCD mutations or demonstrate that the signal is causally independent of chronic airway disease.

[PMID:23290188](https://pubmed.ncbi.nlm.nih.gov/23290188/), [PMID:24189859](https://pubmed.ncbi.nlm.nih.gov/24189859/)

## inflammation-independent-remodeling — QUALIFIED

Conditional IFT88 deletion produced remodeling without apparent inflammation or clearance defects in mice. IFT88 also affects nonmotile cilia and epithelial differentiation, and this model is not equivalent to a human axonemal PCD genotype. It is a mechanistic lead, not a demonstrated human PCD branch.

[PMID:24213915](https://pubmed.ncbi.nlm.nih.gov/24213915/)

## macrophage-endotype — QUALIFIED

Sputum from 27 people with PCD induced an M2-like phenotype in healthy monocyte-derived macrophages ex vivo. This does not establish a stable in-vivo endotype or displace the well-described neutrophil-dominant airway phenotype.

[PMID:41582098](https://pubmed.ncbi.nlm.nih.gov/41582098/)

## perinatal-fluid-clearance — QUALIFIED

Spag17-null mice develop neonatal lung-fluid accumulation, while neonatal respiratory distress is common in human PCD. The cross-species combination supports plausibility but does not directly establish the proposed mechanism in human infants.

[PMID:23418344](https://pubmed.ncbi.nlm.nih.gov/23418344/), [PMID:35011687](https://pubmed.ncbi.nlm.nih.gov/35011687/)

## rsph1-p-value — REJECTED

The source reports P=0.043 for this comparison. The effect estimate is correctly transcribed, but the reported P value is not.

[PMID:24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/)

## ontology-labels — REJECTED

CL:0000710 denotes neurecto-epithelial cell, not multiciliated cell, and CL:0000235 denotes macrophage without an M2 subtype. CL:0000158 and CL:0000065 are correctly labeled. CL:0005012 (multiciliated epithelial cell) is a suitable replacement for the report's intended generic multiciliated-cell concept. These ontology suggestions must not be copied into curated data as written.

## go-ontology-mapping — REJECTED

GO:0060271 denotes cilium assembly, not multiciliated-cell differentiation. This candidate ontology mapping must not be copied into curated data as written.

## literature-count-provenance — NEEDS_VERIFICATION

The citation manifest exposes 50 unique PMIDs and no search log or complete screened corpus. The larger count may be valid, but it cannot be reconstructed from the deposited artifacts and should not be used as an evidence-quality metric.

## multiciliogenesis-residual-cilium-distinction — QUALIFIED

CCNO patient cells retain residual cilia with appropriate axonemal motor proteins and motility. In contrast, PMID:25048963 explicitly reports that the one or two residual MCIDAS cilia lack DNAH5 and CCDC39, with loss of the upstream motor-expression program. Both reduce cilia number, but reduced number and residual-cilium beat dysfunction are not mutually exclusive. The previous assessment incorrectly extended CCNO residual normality to MCIDAS and has been corrected.

[PMID:24747639](https://pubmed.ncbi.nlm.nih.gov/24747639/), [PMID:25048963](https://pubmed.ncbi.nlm.nih.gov/25048963/)

## dominant-inheritance-omission — QUALIFIED

FOXJ1 is an important dominant exception, but TUBB4B dominant-negative respiratory PCD was already described in 2024 in a 12-person cohort with functional models. Relevant X-linked forms also exist. TUBB4B is allelically heterogeneous, so sensory-only or mixed variants must not be generalized to every respiratory case. The disease definition now covers these inheritance classes.

[PMID:34132502](https://pubmed.ncbi.nlm.nih.gov/34132502/), [PMID:38662826](https://pubmed.ncbi.nlm.nih.gov/38662826/), [PMID:41005984](https://pubmed.ncbi.nlm.nih.gov/41005984/)

## normal-beating-transport-dissociation — QUALIFIED

The report appropriately includes normal-TEM DNAH11 and RSPH1 frequency/waveform differences. Existing PMID:39362668 additionally demonstrates C1d-associated impaired patient-cell transport despite normal routine TEM, beat assessment and nasal NO. A transport defect is not synonymous with a detectable conventional beat defect. The nine-person characterization and available cultured samples do not establish every candidate gene at equal clinical-validity strength. Ascertainment selected situs-solitus cases, limiting laterality prevalence inference.

[PMID:39362668](https://pubmed.ncbi.nlm.nih.gov/39362668/), [PMID:24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/), [PMID:18022865](https://pubmed.ncbi.nlm.nih.gov/18022865/)

## longitudinal-data-absence — REJECTED

PMID:30067075 already followed 137 children and young adults over five years with 732 visits, stratified by ultrastructure and genotype; additional iPCD longitudinal evidence predates the report. Sparse adult/rare-genotype follow-up is a valid narrower gap, but categorical absence is false. The 24-year window in the radioaerosol series is the retrospective collection period, not 24 years of follow-up per participant.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/), [PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/)

## pcd-randomized-trial-gap — QUALIFIED

Few PCD trials exist, but the gap text calls BESTCILIA the only PCD-specific RCT while the same report cites CLEAN-PCD, a 123-participant randomized crossover trial. CLEAN-PCD showed a small combination-versus-hypertonic-saline ppFEV1 effect (1.5 points; CI below 0.1–3.0; p=0.044), with nonsignificant combination-versus-placebo and monotherapy-versus-placebo comparisons. Trial rarity and uncertain long-term benefit remain valid; absence of all other randomized evidence does not.

[PMID:32380069](https://pubmed.ncbi.nlm.nih.gov/32380069/), [PMID:37660715](https://pubmed.ncbi.nlm.nih.gov/37660715/)

## human-dnai1-pharmacodynamic-update — QUALIFIED

The cited DNAI1 replacement study is mouse airway-culture rescue, not human efficacy. The 2026 primary conference abstract for separate RCT1100-101/102 studies reports nine single-dose and seven multidose adults, no serious or grade ≥3 adverse events, and no post-treatment improvement in dynein-arm counts, movement or DNAI1 immunofluorescence. These small open-label pharmacodynamic findings do not prove efficacy or permanent failure of the platform. NCT06633757 is RCT1100-103, a distinct registry protocol, not the source of these reported outcomes.

[PMID:40963409](https://pubmed.ncbi.nlm.nih.gov/40963409/), [DOI:10.1093/ajrccm/aamag286.098](https://doi.org/10.1093/ajrccm/aamag286.098), clinicaltrials:NCT06633757

## enac-rationale-not-etiology — QUALIFIED

CLEAN-PCD tested mucus hydration through ENaC inhibition and hypertonic saline. Its rationale and comparator-specific FEV1 findings do not independently demonstrate primary mutation-intrinsic ENaC hyperabsorption across PCD genotypes. CFTR/ENaC airway physiology is relevant background, while a new universal PCD causal edge would require direct genotype-matched transport measurements.

[PMID:37660715](https://pubmed.ncbi.nlm.nih.gov/37660715/)

## infertility-denominators — QUALIFIED

Correct numerical estimates apply to 168 survey respondents who had tried to conceive, from 265/482 adult respondents. Infertility included use of medically assisted reproduction; clinical data were unvalidated self-report. The 7.6% ectopic estimate is per pregnancy, not per woman. Selection/recall bias and gene differences preclude universal prevalence or obligatory infertility. Shared ciliary machinery supports the organ mechanism, not identity of every respiratory and reproductive phenotype.

[PMID:38962571](https://pubmed.ncbi.nlm.nih.gov/38962571/), [PMID:26373788](https://pubmed.ncbi.nlm.nih.gov/26373788/)

## ccno-pooled-denominator — QUALIFIED

PMID:26777464 identified 15 people from 10/170 Israeli mucociliary-disorder families (6% of families). Its 10% hydrocephalus and 22% female-infertility estimates combine these with previously published CCNO cases, not just the 15 new participants, and are not general PCD frequencies.

[PMID:26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/)

## early-care-causal-inference — QUALIFIED

The 35-infant retrospective series shows substantial morbidity despite early care, including obstructive trends at age seven. There is no randomized early-versus-late diagnosis control, and hypertonic-saline exposure is strongly confounded by center. Disease persisting despite care does not establish care futility or quantify prevented harm.

[PMID:42112810](https://pubmed.ncbi.nlm.nih.gov/42112810/)

## pathogen-progression-causality — QUALIFIED

Pseudomonas isolation and more severe disease associate in observational cohorts; established structural disease also promotes infection. These data do not on their own identify which direction dominates or prove a pathogen-specific independent mediator. Culture-directed care and a qualified infection-injury pathway are justified.

[PMID:38072392](https://pubmed.ncbi.nlm.nih.gov/38072392/), [PMID:42112810](https://pubmed.ncbi.nlm.nih.gov/42112810/)

## infection-induced-epitranscriptomics — QUALIFIED

PMID:41738162 studies acquired Pseudomonas-induced lactate/YTHDF1/DNAH5 regulation in infection models, including conditional YTHDF1 knockout mice. It is not a demonstrated mutation-specific modifier pathway in congenital PCD. Existing DNAH5 patient-cell scRNA-seq/proteomics instead directly supports oxidative stress and adaptive GSTA1/2-NRF2 expression; GSTA2 loss slows motility, but antioxidant clinical benefit remains untested.

[PMID:41738162](https://pubmed.ncbi.nlm.nih.gov/41738162/), [PMID:39042459](https://pubmed.ncbi.nlm.nih.gov/39042459/)

## brensocatib-scope — QUALIFIED

ASPEN supports brensocatib in a broad non-CF bronchiectasis population, and FDA approval in August 2025 covers age ≥12 with non-CF bronchiectasis. This indication is not proof of a separately powered PCD treatment benefit; an etiologic subgroup cannot be assumed to share the overall effect. The report proposal should focus on PCD-specific precision and biological response rather than imply a new general indication or established PCD efficacy.

[PMID:40267423](https://pubmed.ncbi.nlm.nih.gov/40267423/)

## diagnostic-guidance-update — RETAINED

The 2025 joint ERS/ATS guideline places high-speed video, immunofluorescence and nasal NO as adjuncts to TEM/genetics, requires inheritance-consistent P/LP variants in adequately validated genes, and states that no single normal test excludes PCD. The 77 nL/min standardized velum-closure threshold is a diagnostic aid, not an emergency critical-low or genotype-independent exclusion boundary. Routine FeNO concentration is not nasal NO production rate.

[PMID:41005984](https://pubmed.ncbi.nlm.nih.gov/41005984/), [PMID:24024753](https://pubmed.ncbi.nlm.nih.gov/24024753/)

## Dataset, artifact and analysis audit

The full Markdown report and its `.md.citations.md` sidecar were read. 5 figure placeholders have no corresponding committed images. The literature search remains reported-only and all 6 named discriminating tests are future proposals. No provider raw-data execution or reproducible computational result is established. Current disease datasets were independently checked at GEO and their publications; that metadata review is not provider access or a new omics analysis.
