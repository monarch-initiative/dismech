---
provider: codex-local-synthesis
model: gpt-5
cached: true
start_time: '2026-04-19T22:15:00Z'
end_time: '2026-04-19T22:15:00Z'
duration_seconds: 0.0
template_file: codex_aip_review_response
template_variables:
  disease_name: AIP-related pituitary adenoma predisposition
  category: Mendelian
citation_count: 9
source_providers:
- pubmed
- github-pr-review
- mondo-ols
- local-term-cache
---

## Question

Curated deep-research synthesis for review-driven completion of the
`AIP-related pituitary adenoma predisposition` dismech entry, including disease
mechanism, diagnostic strategy, and treatment implications.

## Output

# AIP-Related Pituitary Adenoma Predisposition Curation Synthesis

## Disease framing and ontology context

- Preferred syndrome label requested upstream: `AIP-related pituitary adenoma
  predisposition` (MONDO NTR `#10131`).
- Current MONDO nearest terms used for provisional mapping:
  - `MONDO:0007052` `growth hormone secreting pituitary adenoma 1`
  - `MONDO:0017824` `familial isolated pituitary adenoma`
- Curation implication:
  - retain the gene-centered syndrome label locally
  - map with `skos:closeMatch` to the older growth-hormone-centric concept
  - keep `familial isolated pituitary adenoma` as a related broader family-level
    concept rather than an exact synonym.

## Exact PMID-backed quote inventory

### Core causation and inheritance

- PMID:16728643
  - `Combining chip-based technologies with genealogy data, we identified germline mutations in the aryl hydrocarbon receptor interacting protein (AIP) gene in individuals with pituitary adenoma predisposition (PAP).`
  - `Typically, PAP patients do not display a strong family history of pituitary adenoma; thus, AIP is an example of a low-penetrance tumor susceptibility gene.`

- PMID:23310926
  - `AIP mutations cause a low penetrance autosomal dominant disease with often a distinct phenotype characterized by young-onset, aggressive, large GH, mixed GH and PRL or PRL-secreting adenomas.`

### FIPA / clinical spectrum

- PMID:17893250
  - `Patients with FIPA are significantly younger at diagnosis and have significantly larger pituitary adenomas than matched sporadic pituitary adenoma counterparts.`
  - `In families with AIP mutations, pituitary adenomas have a penetrance of over 50%.`

- PMID:21753072
  - `Germline AIPmut occur in 11.7% of patients <30 years with sporadic pituitary macroadenomas and in 20.5% of pediatric patients.`
  - `AIPmut mutation testing in this population should be considered in order to optimize clinical genetic investigation and management.`

### AHR interaction and cAMP signaling

- PMID:16728643
  - `AIP acts in cytoplasmic retention of the latent form of the aryl hydrocarbon receptor and also has other functions.`

- PMID:24662816
  - `AIP deficiency leads to elevated cAMP concentrations through defective Gαi-2 and Gαi-3 proteins that normally inhibit cAMP synthesis.`
  - `This study implies for the first time that a failure to inhibit cAMP synthesis through dysfunctional Gαi signaling underlies the development of GH-secreting pituitary adenomas in AIP mutation carriers.`

### Diagnosis

- PMID:17360484
  - `AIP IHC staining levels proved to be a useful predictor of AIP status, with 75% sensitivity and 95% specificity for germ-line mutations.`
  - `AIP IHC, followed by genetic counseling and possible AIP mutation analysis in IHC-negative cases, a procedure similar to the diagnostics of the Lynch syndrome, appears feasible in identification of PAP.`

- PMID:22720333
  - `The diagnosis of AIP-FIPA is established in a proband with a PitNET by identification of a heterozygous germline pathogenic variant in AIP by molecular genetic testing.`

### Treatment and management

- PMID:22720333
  - `Large somatotropinomas are treated with transsphenoidal surgery, medical therapy, and/or radiotherapy.`
  - `Standard treatment of GH-producing microadenomas includes medical therapy (somatostatin receptor ligands [SRLs], GH receptor antagonists, and dopamine agonists), surgery, and/or radiotherapy.`
  - `Prolactinomas are treated with dopamine agonist therapy or surgery.`

- PMID:22659247
  - `Somatotroph adenomas harboring aryl hydrocarbon receptor interacting protein (AIP) mutations respond less well to somatostatin analogs, suggesting that the effects of somatostatin analogs may be mediated by AIP.`
  - `These results suggest that AIP may play a role in the mechanism of action of somatostatin analogs via ZAC1 in sporadic somatotroph tumors and may explain their lack of effectiveness in patients with AIP mutations.`

- PMID:29953972
  - `AIP mutations are found in 20-25% cases and cause aggressive somatotropinomas, often resistant to somatostatin analogues.`
  - `They were initially treated with a long-acting somatostatin analogue (octreotide LAR 30 mg/month) and cabergoline as a dopamine agonist, with the later addition of pegvisomant titrated up to 20 mg/day and with radiotherapy for long-term control.`
  - `Pegvisomant can safely be used, to normalize IGF-1 levels and help control disease.`

## Curation decisions derived from the evidence

- Keep the disease as an incompletely penetrant autosomal dominant hereditary
  pituitary tumor predisposition syndrome caused by germline `AIP`
  loss-of-function.
- Keep the mechanistic graph split into:
  - proximal germline AIP loss-of-function predisposition
  - disrupted AIP-AHR interaction / chaperone biology
  - defective Gi-cAMP restraint in somatotrophs leading to GH-secreting
    macroadenomas
- Reclassify mechanistic cAMP evidence from PMID:24662816 away from
  `HUMAN_CLINICAL` because the key cAMP experiments are explicitly in vitro /
  murine-system evidence.
- Add diagnosis coverage in three layers:
  - clinical selection of young-onset macroadenoma / FIPA cases for AIP workup
  - tumor AIP immunohistochemistry as prescreening
  - confirmatory germline molecular genetic testing
- Add treatment coverage focused on the review-requested items:
  - transsphenoidal surgery and multimodal local control
  - reduced first-generation somatostatin-analog effectiveness
  - dopamine agonist and pegvisomant escalation in resistant or mixed GH/PRL disease
  - radiotherapy for residual or recurrent tumors
- Expand the phenotype section modestly with mass-effect manifestations
  (`headache`, `visual field defect`) because these are directly supported by
  the management summary literature.

## Term shortlist used for grounding

- Disease:
  - pending MONDO NTR `#10131`
  - `MONDO:0007052` `growth hormone secreting pituitary adenoma 1`
  - `MONDO:0017824` `familial isolated pituitary adenoma`
- Genes:
  - `hgnc:358` `AIP`
  - `hgnc:348` `AHR`
- Cell type:
  - `CL:0002312` `somatotroph`
- Anatomy:
  - `UBERON:0000007` `pituitary gland`
- Biological process / function:
  - `GO:0141156` `cAMP/PKA signal transduction`
  - `GO:0007188` `adenylate cyclase-modulating G protein-coupled receptor signaling pathway`
  - `GO:0017162` `aryl hydrocarbon receptor binding`
- Phenotypes:
  - `HP:0002893` `Pituitary adenoma`
  - `HP:0025693` `Pituitary macroadenoma`
  - `HP:0000845` `Elevated circulating growth hormone concentration`
  - `HP:0000870` `Increased circulating prolactin concentration`
  - `HP:0002315` `Headache`
  - `HP:0001123` `Visual field defect`
- Diagnosis / treatment terms:
  - `MAXO:0000487` `clinical assessment`
  - `MAXO:0000533` `molecular genetic testing`
  - `MAXO:0000004` `surgical procedure`
  - `MAXO:0000058` `pharmacotherapy`
  - `MAXO:0000014` `radiation therapy`
