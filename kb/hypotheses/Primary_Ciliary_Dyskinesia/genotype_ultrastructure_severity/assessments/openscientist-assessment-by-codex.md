# OpenScientist assessment: genotype_ultrastructure_severity

Updated 5 September 2026. This replaces and expands the July narrative while preserving its useful claim judgments. The assessment YAML is authoritative.

Genotype-associated group differences and CCDC39/CCDC40 cellular mechanisms are partly supported, but fixed severity tiers, uniform absent clearance, exclusive severe-group decline and clinical mechanistic mediation are not established. The report misidentifies a functional comparison and misses existing cross-genotype omics. This assessment expands and reconciles the July review after reading the complete provider report, citation sidecar, existing assessment, and disease YAML, and independently retrieving the material primary literature and current diagnostic/care guidance. No provider computation or primary omics analysis was reproduced.

## genotype-severity-extremes — RETAINED

A prospective cohort and a large registry support worse lung-function and growth measures for CCDC39/CCDC40-associated disease, while a matched RSPH1 series supports a milder phenotype. These are relative group associations, not deterministic prognoses for individuals.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/), [PMID:24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/)

## ccdc-worst-prognosis — QUALIFIED

The severe association is credible, but the evidentiary count is inflated: one cited item is a narrative review and another is a situs ambiguus outcome study that adjusts for a predefined severe-genotype category. Available cohorts do not compare every genotype longitudinally or show that every CCDC39/CCDC40 patient has the worst course.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/), [PMID:38072392](https://pubmed.ncbi.nlm.nih.gov/38072392/), [PMID:40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/)

## three-tier-model — QUALIFIED

The extremes are supported, but “most others” has not been established as a homogeneous standard tier, CCNO placement rests on limited and cross-sectional data, and the exact strata have not been prospectively validated. This is a useful testable proposal, not a curation-ready classification.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/), [PMID:26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/)

## rsph1-p-value — REJECTED

The source reports P=0.043 for the lung-function comparison. The effect estimate is correctly transcribed, but the P value is not.

[PMID:24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/)

## dnah5-dnah11-equivalence — QUALIFIED

A single-center study of 74 participants found no statistically significant lung-function or CT difference. A null, relatively small comparison does not establish equivalence, and the larger registry found milder cross-sectional lung function for DNAH11 relative to the overall PCD population. The middle remains unresolved rather than collapsed.

[PMID:38602513](https://pubmed.ncbi.nlm.nih.gov/38602513/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/)

## universal-clearance-absence — REJECTED

PMID:38076675 states that clearance was consistently absent in most patients regardless of genotype and reports one participant with residual clearance. The study challenges a simple residual-clearance explanation but does not support “uniformly” or “every.”

[PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/)

## proteostasis-clinical-mediation — QUALIFIED

Patient-cell and model experiments robustly show loss of an axonemal protein network, proteostasis disruption, cell-fate changes, and rescue by normal CCDC39. They do not yet demonstrate that this pathway mediates between genotype and longitudinal clinical severity; the source itself presents that link as an explanation the findings may provide.

[PMID:39879322](https://pubmed.ncbi.nlm.nih.gov/39879322/)

## nno-progression — REJECTED

The study measured nasal and exhaled NO, not lung-function decline or prognosis. Its authors state that lower nNO may be related to ultrastructural severity and that causality requires further study. Biomarker change cannot be substituted for demonstrated clinical progression.

[PMID:35777446](https://pubmed.ncbi.nlm.nih.gov/35777446/)

## ccno-severe-tier — QUALIFIED

Small pooled case series describe rapid deterioration, and the large registry reports low cross-sectional FEV1 for CCNO. These findings support concern but do not yet validate equal tier membership or a common mechanism with CCDC39/CCDC40.

[PMID:26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/), [PMID:31765523](https://pubmed.ncbi.nlm.nih.gov/31765523/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/)

## variant-type-prognosis — QUALIFIED

The direct cited evidence is a DNAH5 association with neonatal respiratory distress. That endpoint supports a gene- and phenotype-specific modifier, not a general within-gene rule for longitudinal PCD severity.

[PMID:40344341](https://pubmed.ncbi.nlm.nih.gov/40344341/)

## tas2r38-ceiling — QUALIFIED

The modifier study supports possible TAS2R38 effects in a mild subgroup but does not directly test or demonstrate a ceiling effect in CCDC39/CCDC40. The proposed interaction is a hypothesis.

[PMID:39181709](https://pubmed.ncbi.nlm.nih.gov/39181709/)

## ccdc40-mrna-clinical-validation — QUALIFIED

Human-cell and zebrafish experiments support molecular and functional rescue. They do not establish clinical efficacy, validate the proposed severity strata, or show that prioritization is evidence of relative prognosis; the report notes only that a phase 1 study is planned.

[PMID:42089334](https://pubmed.ncbi.nlm.nih.gov/42089334/)

## cell-ontology-mapping — REJECTED

CL:0000064 denotes the broader class “ciliated cell”; it does not encode the stated airway, epithelial, or multiciliated specificity. Depending on the intended anatomical scope, CL:4030034 (respiratory tract multiciliated cell) or CL:1000271 (lung multiciliated epithelial cell) provides a more specific replacement.

## go-ontology-label — QUALIFIED

The exact label is “establishment or maintenance of epithelial cell apical/basal polarity.” The report's shortened wording omits both the maintenance alternative and the apical/basal specificity.

## disease-ontology-proposal — REJECTED

This conflicts with the project's ontology policy: disease identity and mappings use MONDO, while OMIM identifiers are source records rather than newly invented subtype ontology nodes. A proposed severity tier also does not establish a new disease entity.

## literature-count-provenance — NEEDS_VERIFICATION

The citation manifest exposes 26 unique PMIDs and no search log or full screened corpus. The asserted total may reflect provider-internal work, but it cannot be reconstructed from the deposited artifacts.

## clearance-study-genotypes — REJECTED

PMID:41561107 actually compares seven RSPH1 patients, eight DNAH5 patients and eight healthy controls. RSPH1 is a radial-spoke defect, not an IDA/MTD cohort. The report matrix mislabels the groups and should not use this study as an ODA-versus-IDA mechanistic comparison.

[PMID:41561107](https://pubmed.ncbi.nlm.nih.gov/41561107/)

## cough-clearance-statistical-scope — QUALIFIED

Whole-lung cough clearance medians were 9.7% in RSPH1 versus 4.2% in DNAH5 (p=0.015), versus 8.3% in controls (RSPH1 p=0.88). The small comparisons were unadjusted; removing one participant with extra coughs retained a RSPH1/DNAH5 difference. Baseline whole-lung MCC did not differ significantly between genotypes (p=0.27), and RSPH1 versus controls was p=0.054, so universal complete absence or equally proven deficits are too absolute. Clinical severity mediation was not tested; albuterol did not clearly restore MCC.

[PMID:41561107](https://pubmed.ncbi.nlm.nih.gov/41561107/)

## longitudinal-cohort-denominator — REJECTED

PMID:30067075 enrolled 137 participants with 732 visits over five years. CCDC39/40 n=34 and DNAH5 n=36 comparisons are correctly quoted, but the report total of 118 is not the primary cohort denominator. Multiple visits are not independent people.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/)

## within-group-slope-inference — QUALIFIED

The average entire-cohort decline was 0.57±0.25 percentage points per year; the IDA/MTD/CA slope was the only subgroup slope significantly below zero in this study. A significant within-group slope versus a nonsignificant slope elsewhere is not itself a significant difference between slopes. Small group sizes and heterogeneous trajectories preclude asserting all other genotypes have stable disease.

[PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/)

## registry-cross-sectional-prognosis — QUALIFIED

PMID:38871375 is a cross-sectional registry analysis of 1236 genetically confirmed individuals, 908 pathogenic variants and 46 genes from 19 countries. It supports lower FEV1 z-scores in CCNO/CCDC39/CCDC40 and milder group values in DNAH11/ODAD1, but is not prospective validation of individual decline or three discrete tiers. Geography, founder alleles, age and diagnostic selection affect generalizability.

[PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/)

## omics-gap-contradicted — REJECTED

Published 2024 PMID:39558053 directly compares mouse tracheal scRNA-seq responses across Cfap221, Cfap54 and Spef2 mutants, with shared and genotype-specific DEGs (GSE254100). PMID:39042459 supplies DNAH5 patient/mother/control and iPSC omics (GSE272189), while PMID:39879322 supplies CCDC39/40 network proteomics. Robust multi-genotype human clinical-outcome-linked omics remain limited, but the blanket no-RNA-seq/proteomics comparison claim is false.

[PMID:39558053](https://pubmed.ncbi.nlm.nih.gov/39558053/), [PMID:39042459](https://pubmed.ncbi.nlm.nih.gov/39042459/), [PMID:39879322](https://pubmed.ncbi.nlm.nih.gov/39879322/)

## proteostasis-publication-independence — QUALIFIED

The CCDC39/40 work combines patient-derived material, Chlamydomonas structural/proteomic analysis and transgene rescue; calling all evidence only in vitro loses that model diversity. Nevertheless, it does not quantify human clinical mediation. PMID:38562900 is the preprint version of PMID:39879322, and PMID:40948093 is a review of existing evidence, not independent patient replication. Cohort overlap and publication versions must be checked before counting independent support.

[PMID:39879322](https://pubmed.ncbi.nlm.nih.gov/39879322/), [PMID:38562900](https://pubmed.ncbi.nlm.nih.gov/38562900/), [PMID:40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/), [PMID:30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/)

## ccno-pool-and-mcidas — QUALIFIED

The original 15 CCNO individuals came from 10/170 Israeli mucociliary-disorder families. Hydrocephalus 10% and female infertility 22% were calculated after pooling these with prior CCNO reports, not within the 15-person series alone. CCNO registry FEV1 supports severe group burden, but universal CCNO/MCIDAS tier placement is not prospectively validated; the mechanisms and residual-cilium phenotypes differ.

[PMID:26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/), [PMID:24747639](https://pubmed.ncbi.nlm.nih.gov/24747639/), [PMID:25048963](https://pubmed.ncbi.nlm.nih.gov/25048963/)

## neonatal-variant-endpoint — QUALIFIED

PMID:40344341 supports neonatal respiratory distress associations: DNAH11 OR0.35 versus ODA, and DNAH5 two loss-of-function variants OR3.06 versus genotypes allowing possible residual function. These are term-neonatal respiratory endpoints in 455 participants, not long-term FEV1 effects or direct molecular quantification of residual protein. The model preserves the endpoint distinction.

[PMID:40344341](https://pubmed.ncbi.nlm.nih.gov/40344341/)

## ent-intervention-endpoint — QUALIFIED

PMID:39989621 relates ultrastructure to earlier pressure-equalization tube placement in longitudinal ENT care. Intervention timing is influenced by clinician practice, local guidelines, hearing surveillance and patient selection; it is not a direct assay of ciliary biology or necessarily a validated proxy for pulmonary severity.

[PMID:39989621](https://pubmed.ncbi.nlm.nih.gov/39989621/)

## gene-validity-severity-category — QUALIFIED

The absence of a severe/standard/mild label in gene-validity resources is not evidence against a clinical association. Those frameworks grade whether a gene causes a disease, not outcome strata. Limited gene validity also cannot be upgraded merely because a functional C1d study includes the gene. Quantitative prognosis requires independent outcome data and validated prediction.

[PMID:41005984](https://pubmed.ncbi.nlm.nih.gov/41005984/), [PMID:38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/), [PMID:39362668](https://pubmed.ncbi.nlm.nih.gov/39362668/)

## ccdc40-restoration-outcomes — QUALIFIED

PMID:42089334 treated ALI cultures from five CCDC40-deficient people, with expression in 10–74% of ciliated cells, restoration of associated proteins, improved beating and particle transport. Zebrafish olfactory-pit motion/flow also improved. These are meaningful proximal and transport endpoints, but there is no human trial outcome or proof that the proposed severe tier predicts clinical treatment benefit.

[PMID:42089334](https://pubmed.ncbi.nlm.nih.gov/42089334/)

## future-tests-scope — RETAINED

Exploratory genotype reanalysis can generate hypotheses but the 123-person short crossover trial was not powered to establish all genotype-treatment interactions, and separate within-group p-values would not establish heterogeneity. Any new analysis needs prespecified contrasts, small-cell handling, multiplicity correction and confirmation. The provider did not access participant-level data or execute the proposal.

[PMID:37660715](https://pubmed.ncbi.nlm.nih.gov/37660715/)

## Dataset, artifact and analysis audit

The full Markdown report and its `.md.citations.md` sidecar were read. 3 figure placeholders have no corresponding committed images. The literature search remains reported-only and all 6 named discriminating tests are future proposals. No provider raw-data execution or reproducible computational result is established. Current disease datasets were independently checked at GEO and their publications; that metadata review is not provider access or a new omics analysis.
