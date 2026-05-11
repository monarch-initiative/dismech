---
provider: codex-local-synthesis
model: gpt-5
cached: true
start_time: '2026-05-11T00:00:00Z'
end_time: '2026-05-11T00:00:00Z'
duration_seconds: 0.0
template_file: codex_acromegaly_manual_curation
template_variables:
  disease_name: Acromegaly
  category: Endocrine Disorder
citation_count: 4
source_providers:
- pubmed
- mondo-cache
---

## Question

Curated deep-research synthesis for a disease-level acromegaly dismech entry
focused on FDA surrogate endpoint integration.

## Output

# Acromegaly Curation Synthesis

## Disease Identity

- MONDO cache check: `MONDO:0019933` has exact label `acromegaly`.
- Existing repo context: `AIP-related_pituitary_adenoma_predisposition.yaml`
  captures a genetic predisposition subset with GH excess but is not a general
  acromegaly disease entry.
- Curation implication: the FDA rows for acromegaly should map to a standalone
  `Acromegaly.yaml` entry rather than to the AIP-related predisposition page.

## Exact PMID-backed Quote Inventory

### Core Disease Mechanism

- PMID:33803429
  - `Acromegaly is a slowly progressive disease caused by persistent excess of circulating growth hormone (GH) and insulin-like growth factor-1 (IGF-1)`
  - `While most cases are secondary to a GH-secreting pituitary adenoma`
  - `High levels of IGF-1 are responsible for most of the clinical manifestations of acromegaly`

### Biochemical Diagnosis and Monitoring

- PMID:33803429
  - `The most important assays for the biochemical diagnosis and management of acromegaly are growth hormone (GH) and insulin-like growth factor-1 (IGF-1).`
  - `Measurement of IGF-1 levels is the key factor in the diagnosis and monitoring of acromegaly, but basal and nadir GH following OGTT are also important.`
  - `Basal GH levels are measured in the morning after fasting and are usually elevated in patients with acromegaly`
  - `Measurement of GH and IGF-1 levels is also used to determine surgical remission, response to medical treatment, and guide treatment decisions.`
  - `GH is a measure of the secretory activity of the tumor and provides a correlate of pituitary GH secretion, while IGF-1 is a measure of biochemical and biological activity of the disease`

### Phenotypes and Treatment Context

- PMID:33803429
  - `associated conditions, including sleep apnea, hypertension, type 2 diabetes mellitus, arthritis, carpal tunnel syndrome, and hyperhidrosis.`
- PMID:21123741
  - `Somatostatin analogs (SA) are widely used in acromegaly, either as first-line or adjuvant treatment after surgery.`
  - `Generally, the response to SA takes into account both control of GH and IGF-I excess, with consequent improvement of clinical symptoms directly related to GH and IGF-I excess, and tumor shrinkage.`
- PMID:27631335
  - `Pegvisomant is a genetically engineered, recombinant growth hormone receptor antagonist, which is effective in normalizing serum insulin-like growth factor 1 (IGF-1) levels in the majority of patients with acromegaly and ameliorating symptoms and signs associated with GH excess.`
  - `It mitigates excess GH action, as demonstrated by IGF-1 normalization, but has no direct effects on pituitary tumors causing acromegaly.`

### Guideline Context

- PMID:25356808
  - `The aim was to formulate clinical practice guidelines for acromegaly.`
  - `this acromegaly guideline addresses important clinical issues regarding the evaluation and management of acromegaly, including the appropriate biochemical assessment`

## Pathograph Decisions

- Proximal mechanism: `Somatotroph growth hormone hypersecretion`.
- Peripheral biochemical effector: `GH-driven IGF-1 overproduction`.
- Clinical consequence node: `GH/IGF-1 tissue overgrowth and metabolic morbidity`.
- Serum GH and serum IGF-1 are modeled as biochemical readouts, not causal
  nodes. They report on the GH/IGF-1 axis for diagnosis, monitoring, and
  pharmacodynamic treatment response.

## FDA Endpoint Mapping

- `FDA-SE-adult-noncancer-002`: serum IGF-1 for acromegaly treated with a GH
  receptor antagonist.
- `FDA-SE-adult-noncancer-003`: serum GH and serum IGF-1 for acromegaly treated
  with a somatostatin analog.
- `FDA-SE-pediatric-noncancer-003`: serum IGF-1 in pediatric acromegaly treated
  with a GH receptor antagonist.
- Disease YAML mapping:
  - `Serum IGF-1` -> `GH-driven IGF-1 overproduction`
  - `Serum growth hormone` -> `Somatotroph growth hormone hypersecretion`
  - relationship: `PHARMACODYNAMIC_MARKER_OF`
  - direction: `POSITIVE`
  - endpoint context: `PHARMACODYNAMIC`

## Completeness Notes

- Covered: GH-secreting somatotroph disease mechanism, GH-driven IGF-1
  overproduction, tissue overgrowth/metabolic morbidity, serum IGF-1, serum GH,
  common associated phenotypes, somatostatin receptor ligand therapy,
  pegvisomant therapy, and the three FDA endpoint rows.
- Not modeled here: rare ectopic GHRH/GH acromegaly, detailed surgical or
  radiotherapy management, dopamine agonist therapy, and genetic predisposition
  subtypes. AIP-related predisposition already has a separate focused repo
  entry.
