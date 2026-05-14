---
disorder: PTEN_Hamartoma_Tumor_Syndrome
research_status: fallback_after_provider_timeouts
last_updated: "2026-05-07T20:56:00Z"
provider_attempts:
  - provider: falcon
    command: "timeout 120s just research-disorder falcon PTEN_Hamartoma_Tumor_Syndrome"
    result: "timeout_exit_124"
  - provider: openai
    command: "timeout 120s just research-disorder openai PTEN_Hamartoma_Tumor_Syndrome"
    result: "timeout_exit_124"
  - provider: openai
    command: "timeout 300s just research-disorder openai PTEN_Hamartoma_Tumor_Syndrome"
    result: "timeout_exit_124"
manual_evidence_scope:
  - ORPHA:306498
  - PMID:18781191
  - PMID:20301661
  - PMID:26564076
  - PMID:31609537
  - PMID:33140411
  - PMID:35594551
  - clinicaltrials:NCT02991807
---

# PTEN Hamartoma Tumor Syndrome Evidence-Backed Research Fallback

## Provider Attempts

The primary deep-research provider attempts did not return usable research
documents within bounded command budgets. The review-requested longer command,
`timeout 300s just research-disorder openai PTEN_Hamartoma_Tumor_Syndrome`, also
timed out with exit code 124 after starting
`research/PTEN_Hamartoma_Tumor_Syndrome-deep-research-openai.md`. No partial
provider artifact was left on disk. The curation therefore uses a manual
evidence-backed synthesis from fetched structured and literature caches.

## Evidence Synthesis

ORPHA:306498 defines PTEN hamartoma tumor syndrome as a rare skin
tumor/hamartoma disease group characterized by germline PTEN mutation,
hamartomas, overgrowth, and increased neoplasia risk. The same Orphanet record
supplies the autosomal dominant inheritance, worldwide prevalence band, and the
PHTS group scope that includes Cowden syndrome, Bannayan-Riley-Ruvalcaba
syndrome, Proteus-like syndrome, Lhermitte-Duclos disease, and SOLAMEN syndrome.

PMID:18781191 anchors the core molecular mechanism: PTEN loss releases negative
regulation of PI3K/AKT/mTOR signaling, increasing cellular growth, migration,
proliferation, and survival. The YAML models this as PTEN loss and PI3K-AKT-mTOR
activation, with downstream hamartomatous tissue overgrowth and multiorgan
cancer predisposition. These mechanism nodes are intentionally atomic so the
graph separates molecular signaling from tissue-level and clinical consequences.

PMID:20301661 provides the GeneReviews clinical frame for PHTS. It supports the
PHTS subtype scope, the typical Cowden presentation with macrocephaly,
trichilemmomas, papillomatous papules, and benign/malignant tumors, the BRRS
presentation with macrocephaly, intestinal hamartomatous polyposis, lipomas, and
pigmented macules, molecular diagnosis by heterozygous germline PTEN pathogenic
variant testing, autosomal dominant counseling, cascade testing, and surveillance
recommendations for thyroid, skin, breast, endometrial, colon, and renal cancer
risk.

PMID:33140411 is the main human clinical cancer-risk source. It supports the
neoplastic phenotype set for breast carcinoma, endometrial carcinoma, thyroid
carcinoma, renal neoplasm, colorectal cancer, and melanoma, with cumulative
lifetime risk ranges drawn from cohort studies. The cancer-risk phenotypes and
surveillance treatment entry are therefore modeled as human clinical evidence
rather than mechanistic inference alone.

PMID:31609537 and PMID:26564076 cover the childhood and genomic-era
neurodevelopmental spectrum. They support macrocephaly, developmental delay,
autism spectrum manifestations, and broad neurodevelopmental overgrowth in PHTS.
PMID:26564076 also supports the genetic-counseling note that at least 10% and
perhaps as many as 44% of cases arise from de novo PTEN mutation.

PMID:35594551 and clinicaltrials:NCT02991807 support the investigational
everolimus entry. Everolimus targets mTOR overactivity and was studied in a
randomized phase II PHTS trial for neurocognitive symptoms, but the cited trial
did not meet the primary efficacy endpoint; it is therefore represented as
investigational pharmacotherapy rather than standard care.

## Scope Confirmation

The YAML intentionally centers on the syndrome-group PHTS entry rather than the
already-curated Cowden syndrome file. It includes PTEN as the defining causative
gene, Orphanet/GeneReviews subtype coverage, OAK-verified MONDO subtype
bindings, representative non-malignant manifestations, major cancer-risk
phenotypes, PTEN molecular testing, surveillance, genetic counseling, and the
completed everolimus trial. Reviewer-suggested subtype MONDO IDs were checked
with OAK and found to resolve to unrelated disorders locally, so the YAML uses
the verified local MONDO IDs instead.
