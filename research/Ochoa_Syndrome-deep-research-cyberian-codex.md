---
provider: cyberian-codex
model: codex-local-synthesis
cached: true
start_time: '2026-05-03T13:15:24Z'
end_time: '2026-05-03T13:15:24Z'
duration_seconds: 0.0
template_file: codex_supplement_local
template_variables:
  disease_name: Ochoa syndrome
  mondo_id: MONDO:0000463
  category: Mendelian
citation_count: 7
source_providers:
- codex-local-literature
provider_attempts:
- falcon: attempted; timed out after 900 seconds with no artifact produced
- openai: attempted; timed out after 900 seconds with no artifact produced
- cyberian-codex: local synthesis generated from cached Orphanet and PubMed evidence
---

## Question

Pathophysiology and clinical mechanisms of Ochoa syndrome, emphasizing direct
ORPHA:2704/MONDO:0000463 mapping, HPSE2/LRIG2 genetics, bladder autonomic nerve
patterning, functional outlet obstruction, renal complications, and
treatment-relevant mechanisms.

## Output

### Evidence Basis

This local Codex synthesis uses the generated Orphanet structured record for
ORPHA:2704 and the PubMed caches integrated into the YAML. Falcon and OpenAI
provider attempts both timed out without artifacts, so the curated YAML is based
on local review of the deterministic evidence caches listed below.

### Core Disease Mechanism

- Ochoa syndrome maps directly to MONDO:0000463 through ORPHA:2704, which uses
  the Orphanet preferred name Urofacial syndrome and lists Ochoa syndrome as a
  synonym.
- Orphanet records autosomal recessive inheritance and lists HPSE2 and LRIG2 as
  disease-causing genes.
- HPSE2 encodes inactive heparanase-2 and LRIG2 encodes leucine-rich repeats
  and immunoglobulin-like domains 2; both proteins have evidence of expression
  or localization in developing urinary-bladder nerves.
- Discovery studies identify HPSE2 and LRIG2 pathogenic variants in affected
  families, while GeneReviews summarizes biallelic variants in either gene as a
  route to molecular diagnosis.
- Mouse and human-development studies support a peripheral neurodevelopmental
  model: Lrig2 or Hpse2 mutant bladders have abnormal nerve density, reduced
  outflow-tract nitrergic innervation, and dysfunctional voiding.

### Clinical Interpretation

- The syndrome is defined clinically by urinary bladder voiding dysfunction and
  abnormal facial movement with expression. The YAML maps the abnormal
  co-contraction component to HP:0034979 Facial synkinesis while retaining the
  clinical preferred term for the inverted smile/grimace phenotype.
- Functional bladder outlet obstruction can present prenatally as megacystis
  and postnatally produces poor stream, residual urine, dribbling incontinence,
  and recurrent urinary tract infection risk.
- Urinary stasis and high-pressure dysfunction lead to vesicoureteral reflux,
  hydronephrosis, renal insufficiency, and in severe cases progressive kidney
  failure.
- Constipation and encopresis are part of the bowel-dysfunction spectrum, and
  nocturnal lagophthalmos has also been documented.
- Orphanet frequency annotations provide structured support for the HPO-coded
  phenotype set, including recurrent urinary tract infections, urinary
  incontinence, vesicoureteral reflux, hydronephrosis, urethral obstruction,
  constipation, bowel incontinence, cryptorchidism, renal insufficiency,
  hypertension, and polydipsia.

### Treatment-Relevant Mechanism

- Management is supportive and directed at preserving bladder emptying,
  preventing infection, and protecting kidney function.
- GeneReviews supports anticholinergic and alpha-1 adrenergic blocking
  medications to reduce bladder pressure and improve voiding.
- Catheterization or vesicostomy can improve bladder drainage when medication is
  insufficient.
- Acute urinary tract infections require rapid antibiotic therapy.
- Severe kidney failure may require dialysis or kidney transplantation.

### YAML Integration Notes

- The pathophysiology graph is intentionally compact: biallelic HPSE2/LRIG2
  dysfunction, aberrant bladder autonomic innervation, functional bladder outlet
  obstruction with incomplete emptying, urinary stasis/reflux/renal injury, and
  the hallmark abnormal facial movement outcome.
- Phenotypes are anchored primarily to ORPHA:2704 frequency annotations and
  reinforced by GeneReviews or mechanistic literature where useful.
- Genetics represent both causal genes separately, while the disease-level
  mechanism is modeled as a shared peripheral-neurodevelopmental pathway.

### Citation Inventory

- ORPHA:2704
- PMID:23967498
- PMID:20560210
- PMID:23313374
- PMID:30885509
- PMID:35812751
- PMID:23832138
