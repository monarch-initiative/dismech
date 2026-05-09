# Autosomal Dominant Polycystic Liver Disease Deep Research Fallback

## Provider Attempts

- `falcon`: `timeout --foreground 120s just research-disorder falcon Autosomal_Dominant_Polycystic_Liver_Disease` produced no usable content and was terminated with signal 15.
- `openai`: `timeout --foreground 120s just research-disorder openai Autosomal_Dominant_Polycystic_Liver_Disease` produced no usable content and was terminated with signal 15.

Because the preferred deep-research providers did not return usable content in
bounded attempts, this fallback records the literature scope used for curation.
All YAML evidence was taken from generated Orphanet and PubMed reference
caches, not from hand-created reference text.

## Literature Scope

Autosomal dominant polycystic liver disease corresponds to MONDO:0000447 and
Orphanet ORPHA:2924. The Orphanet record for isolated polycystic liver disease
defines the condition as genetic PCLD with numerous cysts throughout the liver,
usually described as ADPCLD. It records adult onset, autosomal dominant
inheritance, a European point-prevalence band of 1-9 per 100,000, HPO
phenotype-frequency rows, and disease-causing gene assertions for ALG8, LRP5,
PRKCSH, and SEC63.

Human clinical reviews and cohorts were used to anchor the phenotype,
diagnosis, and management sections. PLD reviews define PCLD as distinct from
ADPKD-associated PLD but clinically similar in producing hepatomegaly from
multiple cysts with preserved liver function. They support ultrasonography as
the first imaging instrument, CT or MRI liver-volume assessment for severity
and risk stratification, molecular diagnostics when imaging or screening is
ambiguous, and management that ranges from conservative care to somatostatin
analogs, cyst-directed procedures, and liver transplantation.

The mechanistic pathophysiology is centered on the best-supported PRKCSH and
SEC63 branch. The principal mechanism review links PRKCSH and SEC63 to
endoplasmic-reticulum protein biogenesis and quality control, inefficient
polycystin maturation, and PC1 dosage as a rate-limiting component of cystic
disease in model systems. Human clinical and surgical sources then support the
downstream cholangiocyte-derived epithelial cysts, hepatic enlargement, and
mass-effect symptom burden.

## Curation Decisions

- Used MONDO:0000447 as the disease term because it carries the Orphanet:2924
  cross-reference and matches the ADPLD/PCLD scope.
- Included all ORPHA very frequent and frequent HPO phenotypes: polycystic
  liver disease, hepatomegaly, abdominal distention, multiple renal cysts, and
  early satiety.
- Added selected ORPHA occasional phenotypes with coherent clinical relevance
  to mass-effect, hepatobiliary, vascular, cardiac, or pancreatic involvement.
  Feeding difficulties in infancy and the broad respiratory-system parent row
  were not included because this entry is adult-onset and already includes the
  more specific dyspnea and respiratory insufficiency rows.
- Modeled subtypes for PRKCSH/PCLD1 and SEC63/PCLD2 with MONDO term bindings,
  and included ALG8-related and LRP5-related ADPLD as Orphanet-supported
  gene-defined subtypes without forcing unavailable local MONDO subtype terms.
- Represented somatostatin analog therapy with generic pharmacotherapy plus
  an NCIT somatostatin receptor agonist therapeutic-agent binding, and kept
  cyst-directed surgery and liver transplantation as separate treatment
  entries.
