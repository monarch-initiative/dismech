# IEMbase 0475: GALE-related galactose epimerase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 475 |
| Nosology | 3.1.02.02 |
| Gene | GALE |
| External IDs | OMIM:230350; ORPHA:308487; ORPHA:308473 |
| Generated mapping | UNMAPPED; low candidate `Galactosemia.yaml` |
| Candidate DisMech targets | `Galactosemia.yaml#Epimerase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GALE-related galactose epimerase
deficiency, also called galactosemia type 3. Biochemical rows include decreased
UDP-galactose epimerase activity in red blood cells and low-to-normal liver
activity, variably increased amino acids, transaminases, bilirubin, urine
glucose, plasma and urine galactose, urine reducing substances, and
erythrocyte galactose-1-phosphate, with decreased-to-normal coagulation factors.
Clinical rows are classic-galactosemia-like but variable: anorexia/anorexia
nervosa source label, cataract, early death, hepatomegaly, liver cirrhosis,
liver failure, and vomiting. IEMbase records galactose-restricted and
lactose-free diet as a nutritional treatment.

## DisMech phenotype coverage

`Galactosemia.yaml#Epimerase Deficiency` is the correct local target. The local
entry explicitly includes a GALE epimerase-deficiency subtype, GALE as the
causal gene, decreased UDP-glucose 4-epimerase activity, disturbed galactose
metabolism, and blood galactose-1-phosphate elevation. The broader
Galactosemia file also models shared galactosemia mechanisms such as galactose
metabolite accumulation, impaired glycosylation, galactitol-linked cataract,
and acute hepatic dysfunction.

## Concordance and completeness

Judgement: false negative; resolve IEMbase 475 to
`Galactosemia.yaml#Epimerase Deficiency`.

The local target captures the disease entity, gene, enzyme activity, and
shared galactosemia biochemical mechanism. IEMbase adds more granular
GALE-specific prompts, especially the distinction between red-blood-cell and
liver epimerase activity, variable systemic severity, diet treatment, and the
classic-like hepatic/coagulation phenotype.

## Curation actions

- Map IEMbase 475 to `Galactosemia.yaml#Epimerase Deficiency`.
- If importing IEMbase-derived prompts, verify the liver-versus-RBC enzyme
  activity distinction, galactose-restricted diet, coagulation-factor rows,
  hepatic rows, and the anorexia/anorexia-nervosa source label against source
  evidence.
