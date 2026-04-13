# Choroid Plexus Carcinoma Deep Research

Date: 2026-04-13
Issue: #1217
Disease page target: `kb/disorders/Choroid_Plexus_Carcinoma.yaml`

## Modeling decisions applied from cancer curation issue `#1198`

- The dismech graph unit is the disease-level CPC entry, not every ontology subclass.
- The primary disease anchor is `MONDO:0016718` (`choroid plexus carcinoma`).
- I used NCIT where the cancer-specific term was materially better than a generic action or broad parent term:
  - `NCIT:C4715` Choroid Plexus Carcinoma
  - `NCIT:C131672` Gross Total Resection
  - `NCIT:C116437` Craniospinal Irradiation
- I initially evaluated `NCIT:C124292` (Childhood Choroid Plexus Carcinoma) and regimen-level NCIT treatment terms, but the current schema validators only accept the disease-term ontology set for `subtype_term` and the treatment-action enum set for `treatment_term`. The final YAML therefore uses:
  - `MONDO:0002685` for the childhood subtype facet
  - generic `chemotherapy` action terms plus explicitly named agents for CarbEV and high-dose methotrexate
- I kept subtype schemes flat and facet-like instead of treating them as separate disorder pages:
  - `Childhood` (`age_group`)
  - `TP53-Altered` / `TP53-Wildtype` (`molecular`)
  - `Li-Fraumeni-Associated` (`predisposition_context`)
- I did **not** split `Ped_CPC1` and `Ped_CPC2` into separate disease files. Current data support prognostic molecular clustering, but not a clearly separate causal program with stable ontology-backed disease classes.

## Disease framing

- CPC is rare and pediatric-predominant.
  - PMID:41198335: "Choroid Plexus Tumors (CPT) are rare (2-4% of all pediatric CNS tumors), predominantly early childhood brain neoplasms."
  - PMID:39364273: "Choroid plexus carcinoma (CPC) is an uncommon tumor that accounts for less than 1% of all pediatric brain tumors."
  - PMID:35592824: "Choroid Plexus Carcinomas (CPC) are rare malignant brain neoplasms of choroid plexus epithelium, with a tendency to occur in infants and children, especially those who are under two years of age."
- WHO/histology placement:
  - PMID:33717766: "Of the CPT subtypes, choroid plexus carcinomas (CPC) are highly aggressive and malignant and of World Health Organization (WHO) Grade III."

## Mechanism summary

- TP53 loss is the dominant recurrent lesion.
  - PMID:36534940: "All studied CPCs had smooth mutational profiles with the only recurrent event being TP53 variants, either germline or somatic, encountered in 13 cases."
- TP53 status is clinically decisive and should shape risk stratification.
  - PMID:33506206: "TP53-mutational status was the only significant prognostic variable and should form the basis of risk-stratification in future trials."
  - PMID:33506206: "Patients with TP53-wild-type tumors had a 5-year PFS of 100% as compared to 28.6 ± 17.1% for TP53-mutant tumors (P = .012)."
- CPC is genomically unstable at the chromosome scale.
  - PMID:36534940: "Unbalanced whole-chromosome aberrations, notably multiple monosomies, were highly typical."
  - PMID:36534940: "In 7 tumors, chromosome losses were combined with complex genomic rearrangements: segmental gains and losses or signs of chromothripsis."
- CPC has additional recurrent molecular features beyond TP53.
  - PMID:38867333: "Mutually exclusive TP53 and EPHA7 point mutations, coupled with the amplification of chromosome 1, were exclusively identified in CPC."
- Wnt/beta-catenin signaling is a mechanistic driver, not just a correlative marker.
  - PMID:39215664: "We discovered that Wnt/β-catenin signaling is activated in human CPTs, likely as a consequence of large-scale chromosomal instability events of the CPT genomes."
  - PMID:39215664: "We demonstrated that CPT-derived cells depend on autocrine Wnt/β-catenin signaling for survival."
  - PMID:39215664: "Increased activation of the Wnt/β-catenin pathway in ChP organoids, through treatment with a potent GSK3β inhibitor, reduced the differentiation of mature ChP epithelial cells."
- CPC adopts a proliferative and invasion-associated transcriptional program.
  - PMID:38867333: "Differential gene expression analysis uncovered a significant overexpression of genes related to cell cycle regulation and epithelial-mesenchymal transition pathways in CPC compared to CPP."
  - PMID:38867333: "Overexpression of genes associated with tumor metastasis and progression was observed in the CPC subgroup with leptomeningeal dissemination."

## Molecular subgroup evidence retained in research, not split into new disease pages

- PMID:39036437: "Preliminary data indicate that choroid plexus carcinomas comprise at least 2 epigenetic subgroups, one of which is associated with TP53 mutation status."
- PMID:36534940: "Transcriptomically, the cohort split into 2 polar clusters Ped_CPC1 and Ped_CPC2 differing by survival: 31.3 ± 17.8% vs 100%; P = .012."
- Rationale:
  - These data are important and were used to justify subtype **facets** and a methylation biomarker entry.
  - They do not yet justify separate dismech disease pages because the evidence base is still cohort-level risk stratification rather than a settled, distinct causal program with stable MONDO/NCIT disease subclasses.

## Clinical presentation and pathology

- Hydrocephalus is the dominant presenting syndrome for the choroid plexus tumor family.
  - PMID:34754533: "Hydrocephalus is the most common presentation of choroid plexus tumors; it is thought to be caused either by mass effect obstructing the cerebrospinal fluid pathways or secretory properties of the tumor."
- Common CPC symptoms:
  - PMID:35592824: "The Main symptoms of CPC include nausea, vomiting, headache, irritability, blurred vision, and seizures."
- Example pediatric presentation illustrating raised ICP and focal deficits:
  - PMID:39364273: "We report an extremely rare tumor arising from the choroid plexus of the third ventricle in a 6-year-old child with progressive headache, macrocephaly, left hemiparesis, and sunset eyes."

## Treatment evidence

- Surgery remains the core local treatment.
  - PMID:41736349: "Complete surgical resection offers the best chance of long-term survival, but this is often difficult due to excessive intraoperative bleeding."
  - PMID:38339361: "Meanwhile, in patients with CPC, gross total resection (GTR) was associated with significantly better OS than subtotal resection (STR) only."
- CarbEV/CEV is supported by the randomized CPC arm of CPT-SIOP-2000.
  - PMID:34997889: "For randomized CPC, the 5/10 year progression free survival (PFS) of patients on CarbEV (n = 20) were 62%/47%, respectively, compared to 27%/18%, on CycEV (n = 15), (intention-to-treat, HR 2.6, p = 0.032)."
  - PMID:34997889: "Chemotherapy for Choroid Plexus Carcinoma is feasible and effective. CarbEV is superior to CycEV. A subset of CPC can be cured without irradiation."
- High-dose methotrexate-containing therapy is a strong pediatric option.
  - PMID:33506206: "Non-myeloablative high-dose methotrexate-containing therapy with maximal surgical resection resulted in long-term PFS in more than half of patients with CPC."
- Radiotherapy needs context-sensitive use.
  - PMID:34997889: "Patients older than three years were recommended to receive irradiation: focal fields for non-metastatic CPC, incompletely resected atypical choroid plexus papilloma (APP) or metastatic choroid plexus papilloma (CPP); craniospinal fields for metastatic CPC/APP and non-responsive CPC."
- TP53-mutant/Li-Fraumeni disease changes the treatment conversation.
  - PMID:41198335: "Advances in molecular profiling have revealed that TP53-mutated CPCs have significantly worse outcomes."
  - PMID:41198335: "Preliminary evidence suggests that TP53-mutant patients may be getting less benefit from RT, but greater benefit from myeloablative chemotherapy approach with avoidance of RT."

## Biomarker/diagnostic evidence

- DNA methylation profiling adds real clinical value in CPC.
  - PMID:38962753: "There was good correlation (11/12, 92%) between methylation class and WHO histologic grade for choroid plexus carcinomas (CPC);"
  - PMID:38962753: "Results indicated that methylation profiling may serve as a valuable tool in the clinical decision-making process for patients with CPTs, providing additional prognostic information compared to WHO histologic grade alone."

## Evidence source choices used in the YAML

- `HUMAN_CLINICAL`
  - retrospective cohorts, trial reports, SEER analyses, and clinical molecular studies (PMIDs 34997889, 36534940, 33506206, 38867333, 38962753, 38339361, 39364273, 34754533)
- `IN_VITRO`
  - mechanistic cell/organoid experiments from PMID 39215664
- `OTHER`
  - narrative reviews or case-report introduction/background statements used only where they captured disease-wide framing better than a primary-study abstract (PMIDs 41198335, 35592824, 33717766, 41736349)

## Open curation note

- The schema currently exposes `mondo_mappings` but not an explicit `ncit_mappings` block, and it also restricts `subtype_term` and `treatment_term` to narrower ontology sets than ideal for some cancer facets/regimens. To respect the `#1198` guidance without inventing a schema extension, I placed NCIT grounding where the schema allowed it most cleanly:
  - disease/histopathology identity via `finding_term`
  - oncology-specific procedures via `treatment_term`
  - regimen specificity via named agents and evidence-backed descriptions
