# IEMbase 0473: GALT-related galactose-1-phosphate uridyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 473 |
| Nosology | 3.1.01.02 |
| Gene | GALT |
| External IDs | OMIM:230400; ORPHA:79239 |
| Generated mapping | MAPPED; high candidate `Galactosemia.yaml#Classic Galactosemia` |
| Candidate DisMech targets | `Galactosemia.yaml#Classic Galactosemia` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GALT-related galactose-1-phosphate
uridyltransferase deficiency, also called classic galactosemia or galactosemia
type 1. Biochemical rows include decreased erythrocyte GALT activity, increased
erythrocyte galactose-1-phosphate, increased plasma and urine galactose,
increased urine galactitol, urine reducing substances, aminoaciduria,
transaminase elevation, bilirubin elevation, decreased coagulation factors,
urinary glucose/calcium/phosphate/protein abnormalities, and a type I
sialotransferrin pattern. Clinical rows include hemolytic anemia, brain edema
on MRI, E. coli sepsis, hepatocellular adenoma, hypergonadotropic hypogonadism,
ovarian failure, intellectual disability, cataracts, early death, hepatomegaly,
liver cirrhosis, liver failure, vomiting, and a source row labelled anorexia
nervosa. IEMbase records galactose-restricted and lactose-free diet as a
nutritional treatment.

## DisMech phenotype coverage

`Galactosemia.yaml#Classic Galactosemia` is the correct local target. The local
entry explicitly models GALT deficiency in the Leloir pathway, decreased GALT
enzyme activity, galactose-1-phosphate accumulation, UDP-hexose depletion,
impaired glycosylation, galactitol accumulation, acute hepatocellular
dysfunction, cataracts, E. coli sepsis, coagulopathy, renal tubular
dysfunction, intellectual disability, chronic brain dysfunction, premature
ovarian insufficiency, and dietary lactose/galactose restriction.

## Concordance and completeness

Judgement: correct GALT/classic galactosemia mapping with high concordance.

IEMbase and DisMech agree on gene, subtype, inheritance, biochemical markers,
acute neonatal toxicity, dietary treatment, and long-term neurologic/gonadal
complications. IEMbase adds or emphasizes several prompts that are not fully
represented locally, including hemolytic anemia, brain edema on MRI,
hepatocellular adenoma, urinary calcium/phosphate/protein abnormalities, and
type I sialotransferrin pattern. The source label "anorexia nervosa" should be
checked carefully before import because it may reflect feeding intolerance or
anorexia wording rather than a psychiatric diagnosis.

## Curation actions

- Keep the mapping to `Galactosemia.yaml#Classic Galactosemia`.
- If importing IEMbase-derived prompts, verify hemolytic anemia, brain edema,
  hepatocellular adenoma, urinary calcium/phosphate/protein abnormalities, type
  I sialotransferrin pattern, and the anorexia/anorexia-nervosa label against
  source evidence before adding them.
