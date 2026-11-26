# Progressive supranuclear palsy: mechanism-led drug candidates

The fourth disease run with the method used for Sjögren's, IPF and ALS
(`../sjogren/README.md`, `../ipf/README.md`, `../als/README.md`). PSP is a Biomni Target
Atlas disease, a 4R tauopathy with no disease-modifying treatment, and a disease where
several tau-directed drugs have already failed, so candidates can be checked against
real trials. Done 2026-11-21.

## Method

1. `genes.tsv`: 24 genes. MAPT (the entry's only node gene), the entry's susceptibility
   loci (STX6, MOBP, SLCO1A2, DUSP10, APOE), the TRIM11 and LRRK2 modifier loci, and
   druggable genes for the nodes that bind none: tau kinases and modifiers for 4R-Tau
   Aggregation (GSK3B, CDK5, OGA, EP300), the integrated stress response (EIF2AK3,
   EIF2B1, PPP1R15A), neuroinflammation (NLRP3, CSF1R, C1QA, TREM2, TNF), autophagy
   (MTOR), microtubules (TUBB), VMAT2 for symptoms, and SIRT1.
2. `../repurposing_candidates.py` with
   `--disease MONDO_0019037 --pattern 'supranuclear palsy|\bPSP\b|Steele|tauopath'`.
   Output: `opentargets/candidates.tsv` (196 rows). The `tauopath` alternative counts a
   trial registered only for "tauopathies" as tested in PSP; no row in this run depends
   on it.
3. Four candidates assessed by OpenScientist with `../repurposing_template.md`; reports in
   `reports/`.

## What the table shows

Open Targets maps **no drugs** to 15 of the 24 genes, among them OGA, EP300, EIF2AK3,
EIF2B1, PPP1R15A, NLRP3, TREM2, C1QA and LRRK2, although drugs for several of them are in
clinical trials, including in PSP. It also misses the MAPT antisense drugs: BIIB080
(diranersen) and NIO752 are not listed under MAPT, and NIO752 is in a phase 3 PSP trial.
Salsalate, tested in PSP, does not appear because EP300 has no drugs.

Already tried in PSP, from the table: gosuranemab, tilavonemab and bepranemab (anti-tau
antibodies), tideglusib and lithium (GSK3B), davunetide (microtubules).

Untested in PSP, at phase 2 or beyond elsewhere, acting in the useful direction:

| Gene | Drug | Stage elsewhere |
|---|---|---|
| MAPT | semorinemab, zagotenemab, posdinemab | phase 2, Alzheimer disease |
| CSF1R | pexidartinib, axatilimab | approved |
| MTOR | rapamycin analogues (ridaforolimus); sirolimus is filed under FKBP1A | approved |
| CDK5 | dinaciclib, seliciclib | phase 2-3, cancer |

The anti-tau antibodies here share the mechanism of the three that failed in PSP, so
they are not new leads.

## OpenScientist assessments

All 120 cited references resolve (confabulation rate 0 in every report). Four quotes did
not match their cited source exactly in the validator's check: PMID:24252572 and
PMID:41606704 (eIF2B report), PMID:32373661 (MAPT report) and PMID:34385707 (mTOR
report). Read those
sentences against the source before reusing them. The six trial registrations the reports
lean on were checked against ClinicalTrials.gov on 2026-11-21 (status and phase below
are from the registry). The report's statement that BIIB080's CELIA trial (NCT05399888,
active, not recruiting) missed its primary endpoint comes from a company announcement,
not a publication.

| Candidate | Node in our entry | Verdict |
|---|---|---|
| eIF2B activator (ISRIB class) | Integrated Stress Response Activation | Mechanism active, drug unpromising. EIF2 signalling is activated in vulnerable PSP cell types and phosphorylated eIF2-alpha sits in p-tau-positive neurons and astrocytes (PMID:39648200). But the brain-penetrant eIF2B activator DNL343 lowered ISR biomarkers in ALS blood and CSF (PMID:40825784) and did not slow ALS in the HEALEY platform (NCT05842941, completed; PMID:42771346). Tau mouse models disagree on which direction helps: PERK inhibition protected rTg4510 mice (PMID:26450683), a PERK activator protected P301S mice (PMID:28148553). |
| OGA inhibitor | 4R-Tau Aggregation | Weak, and untested at the first step: no study has measured O-GlcNAc or OGA in PSP tissue; the deficit was shown in Alzheimer disease (PMID:39748851). Ceperognastat did not slow early Alzheimer disease (NCT05063539; PMID:42441396). A PSP phase 2, PROSPER (FNP-223, NCT06355531, 241 patients), completed in October 2026 with no results posted. |
| MAPT antisense (BIIB080) | MAPT H1 Haplotype and 4R Tau Splicing Imbalance | The premise holds: MAPT is a replicated PSP locus (PMID:39152475), and PSP cerebellum has more total and 4R tau mRNA, with 4R tau associated with H1 (PMID:39154163). The weak links are delivery, since intrathecal ASOs reach deep grey matter poorly (PMID:40857674), and the precedent of gosuranemab, which cut CSF tau without changing the PSP Rating Scale (PMID:34385707). The same mechanism is already in a PSP phase 3, NIO752 (PRESERVE, NCT07498426, recruiting, 300 patients). |
| mTOR inhibitor (sirolimus) | 4R-Tau Aggregation | Weak. mTORC1 inhibition lowers insoluble tau in P301S and PS19 mice (PMID:23667480, PMID:24880087), but PSP genetics points at autophagosome-lysosome fusion (STX6, PLEKHM1; PMID:40465013), downstream of where rapamycin acts. The sirolimus trial in multiple system atrophy (NCT03589976) was terminated for futility, with no evidence of brain mTOR engagement (PMID:37643509). Immunosuppression carries particular risk in a disease where pneumonia is a leading cause of death (PMID:28420838). |

## Recurring themes

- **Target engagement is not the bottleneck.** Gosuranemab, DNL343 and ceperognastat all
  reached and moved their targets in human brain or CSF and failed clinically. Three of
  the four reports conclude that the next experiment should be a human tissue or imaging
  measurement, not another efficacy trial.
- **Deep grey matter.** PSP disability arises in the basal ganglia, subthalamic nucleus
  and brainstem, where intrathecal drugs reach least.
- **Alzheimer evidence transfers poorly.** The O-GlcNAc deficit, the BIIB080 tau-PET
  result and most mouse models come from 3R/4R or mutant-tau settings, not sporadic 4R
  tauopathy with tufted astrocytes.

## Leads for the dismech entry

- PROSPER (NCT06355531) and PRESERVE (NCT07498426) as `clinical_trials` rows, and a
  MAPT antisense treatment entry (investigational) targeting the MAPT node.
- The Integrated Stress Response node binds no gene; EIF2AK3 (PERK) is a PSP GWAS locus
  and the natural binding, with the risk-haplotype evidence read from its source.
- STX6 and PLEKHM1 as autophagosome-lysosome fusion genes (PMID:40465013), for a node or
  a note on impaired tau clearance.
