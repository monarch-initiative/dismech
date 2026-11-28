# African iron overload: curation review of the OpenScientist report

Reviewed 2026-11-28 by Codex, including a separate fresh-context scientific review.
This is a disease-curation assessment, not an independent reproduction of the
provider's computational analyses.

The [generated report](African_Iron_Overload-deep-research-openscientist.md),
[citation output](African_Iron_Overload-deep-research-openscientist.md.citations.md),
and [artifact provenance](African_Iron_Overload-deep-research-openscientist_artifacts/provenance.json)
are retained as generated. The provider job is
[d9032303-e42f-4291-b398-70187571e905](https://www.openscientist.io/job/d9032303-e42f-4291-b398-70187571e905).
Citation resolution does not validate a claim, its interpretation, or a calculation.

The report supplies useful literature leads but contains material errors. Only
claims checked against fetched sources were added to the
[disease entry](../kb/disorders/African_Iron_Overload.yaml).

| Lead | Source check and curation decision |
| --- | --- |
| Prevention through iron-free brewing containers | [PMID:20526004](../references_cache/PMID_20526004.md) explicitly recommends this for African dietary iron overload. Added environmental-source reduction, without claiming a trial effect size or reversal of established injury. |
| Follow-up mortality | [PMID:10554633](../references_cache/PMID_10554633.md) reports six deaths among 22 biopsy-confirmed subjects over median follow-up of 19 months. Added a qualified clinical-outcomes record; this is not population survival or proof of iron-attributable death. |
| Hepatocellular carcinoma | [PMID:9620327](../references_cache/PMID_9620327.md) reports a small adjusted case-control association accounting for alcohol, viral hepatitis and aflatoxin. Added supporting evidence while retaining wide confidence limits and causal uncertainty. |
| Tuberculosis death | [PMID:8605366](../references_cache/PMID_8605366.md) associates splenic iron at historical necropsy with TB death. Added to the existing hypothesis discussion, distinguishing tissue iron from dietary exposure and association from causation. |

Material claims that were not adopted:

- The report says survival data are absent. PMID:10554633 directly contradicts
  that statement; it was already among the entry's diagnostic references.
- The rat-model table says five of eight survivors developed carcinoma.
  [PMID:16278820](https://pubmed.ncbi.nlm.nih.gov/16278820/) instead reports
  preneoplastic nodules in five and hepatocellular carcinoma in one. No animal
  result was used to upgrade the human association to a demonstrated cause.
- A nonsignificant endocrine comparison in 30 cases and 30 controls
  ([PMID:14515008](https://pubmed.ncbi.nlm.nih.gov/14515008/)) does not establish
  universal absence of pituitary or gonadal involvement. Cortisol measurements
  within reference ranges do not justify a pathological hypercortisolism phenotype.
- gnomAD inclusion does not establish that homozygotes are healthy or
  asymptomatic. The report's independent ACMG classification and definite Q248H
  modifier claim were not adopted. The entry retains the disputed causal
  relationship and the positive and negative clinical evidence.
- Generic iron-balance models, HFE-derived fibrosis thresholds and cellular
  experiments do not establish disease-specific human mechanisms or temporal
  stages. No numerical staging scheme or specific hepcidin defect was imported.
- The report's recommendation to exclude cardiac manifestations conflicts with
  the Orphanet-backed congestive-heart-failure annotation, which is retained.
- MONDO:0011209 is incorrectly called ferroportin disease; it labels progeroid
  facial appearance with hand anomalies. HP:0040130 is incorrectly called
  elevated transferrin saturation; the curated entry uses HP:0012463. Report
  validation also records ontology-service timeouts, so it is not a clean term
  audit. No new term identifiers were copied from the report.

The five plot-provenance JSONs contain code, making parts of the calculations
inspectable. They do not include saved clinical/genomic API responses, an
audited table of independent cohorts, dependency specifications, execution
outputs, or a canonical manifest binding inputs to results. Plot 3 retrieves API
data but plots separately hard-coded frequencies. The scripts were not
independently replayed in this review; the results remain provider calculations.

The central genetic inference is particularly unsupported. In
[plot 5](African_Iron_Overload-deep-research-openscientist_artifacts/provenance_plot_5.json),
required absorption is defined as `(H / (365.25 * s * t) + loss) / (46 * volume)`.
The provider chooses 25 versus 45 years for affected and unaffected subjects.
Beer volume cancels from the ratio, and for positive inputs that ratio is bounded
between 1 and 45/25 = 1.8 by construction. Its stability across drinking volumes
therefore does not validate a measured genetic effect. The selected durations
and liver-retention fraction are assumptions, not identified causal parameters.
The pooled prevalence and allele analyses also lack a demonstrated audit of
cohort overlap and comparable case definitions. None of these calculated
estimates was imported as clinical evidence.

The final entry covers disease identity, environmental exposure, uncertain
genetics, tissue pathology, specific manifestations, diagnostics, prevention,
treatment limitations and observed outcomes. Its OMIMPS membership does not
imply a Mendelian cause. The original seven-member projection remains a frozen
analysis snapshot; this entry supplies its previously missing African iron
overload member.
