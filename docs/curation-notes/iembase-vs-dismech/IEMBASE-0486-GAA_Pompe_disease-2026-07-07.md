# IEMbase 0486: GAA-related alpha-glucosidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 486 |
| Nosology | 20.6.05.01 |
| Gene | GAA |
| External IDs | OMIM:232300; ORPHA:420429 |
| Generated mapping | MAPPED; high candidate `Pompe_Disease.yaml` |
| Candidate DisMech targets | `Pompe_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GAA-related alpha-glucosidase deficiency
as Pompe disease / GSD IIa. Treatments are alglucosidase alpha and
avalglucosidase alfa. Biochemical rows include decreased alpha-1,4-glucosidase
activity in dried blood spot, fibroblast, and muscle assays; increased
transaminases; increased creatine kinase; increased glycogen; increased urinary
tetraglucoside; and variably increased vacuolated myocytes. Clinical rows
include abnormal EEG, sensorineural hearing loss, macroglossia, orthopnea, and
taurodontism.

## DisMech phenotype coverage

`Pompe_Disease.yaml` is the correct local target. The entry models biallelic GAA
deficiency, lysosomal glycogen accumulation, autophagy dysregulation, skeletal
and respiratory myofiber injury, infantile-onset and late-onset subtypes,
hypertrophic cardiomyopathy, generalized hypotonia, proximal myopathy,
respiratory insufficiency, hepatomegaly, macroglossia, failure to thrive,
exercise intolerance, hearing impairment, decreased acid alpha-glucosidase
activity, elevated creatine kinase, urinary total glucotetrasaccharide / Hex4,
enzyme replacement therapy, cipaglucosidase alfa plus miglustat, respiratory
support, rehabilitation, diet, and genetic counseling.

## Concordance and completeness

Judgement: correct Pompe disease mapping with high concordance.

The resources agree on GAA identity, recessive inheritance, acid
alpha-glucosidase deficiency, lysosomal glycogen storage, CK/transaminase
elevation, tetraglucoside/Hex4, macroglossia, hearing involvement, and approved
enzyme replacement therapies. DisMech is more complete on the infantile/late
onset split and respiratory/cardiac causal graph. IEMbase adds several specific
phenotype prompts not prominent locally, including abnormal EEG, orthopnea,
taurodontism, and explicit assay-compartment rows for DBS, fibroblast, and
muscle.

## Curation actions

- Keep the mapping to `Pompe_Disease.yaml`.
- If importing IEMbase prompts, verify abnormal EEG, orthopnea, taurodontism,
  and compartment-specific alpha-glucosidase assay rows.
- Note the Orphanet identifier difference in source metadata if relevant;
  disease identity is still clear through GAA/Pompe/OMIM:232300.
