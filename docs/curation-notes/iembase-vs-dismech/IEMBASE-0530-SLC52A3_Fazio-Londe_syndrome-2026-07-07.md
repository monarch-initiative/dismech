# IEMbase 0530: SLC52A3-related Fazio-Londe syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 530 |
| Nosology | 21.3.02.02 |
| Gene | SLC52A3 |
| External IDs | OMIM:211500; ORPHA:97229 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Brown-Vialetto-Van_Laere_Syndrome.yaml#Fazio-Londe spectrum context` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC52A3-related Fazio-Londe syndrome and notes that it is
allelic with Brown-Vialetto-Van Laere syndrome. The record is autosomal
recessive, subtype is marked idiopathic, treatability is marked yes, and no
treatment rows are listed.

Biochemical rows include normal-to-increased C4-C18 acylcarnitines, low or
normal free carnitine, normal-to-increased C6-C10 dicarboxylic acids,
ethylmalonic acid, and glutaric acid. Clinical rows emphasize early muscle
weakness, respiratory insufficiency from muscle weakness or diaphragm
paralysis, and pontobulbar palsy. Sensorineural deafness is absent from this
IEMbase record, matching the Fazio-Londe distinction.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. `Brown-Vialetto-Van_Laere_Syndrome.yaml`
explicitly states that Fazio-Londe disease is now regarded as part of the
riboflavin-transporter-deficiency spectrum and is distinguished clinically by
bulbar motor neuron disease without prominent deafness.

The local file covers the shared SLC52A3/SLC52A2 riboflavin transporter biology,
pontobulbar palsy, respiratory involvement, muscle weakness, and riboflavin
treatment rationale. It is broader than the IEMbase Fazio-Londe row because it
also covers the deafness-positive BVVL presentation.

## Concordance and completeness

Judgement: false negative; use the local Brown-Vialetto-Van Laere syndrome file
as the spectrum target, with Fazio-Londe-specific scope noted.

IEMbase is useful for preserving the deafness-absent Fazio-Londe phenotype and
for the acylcarnitine/organic-acid prompts. DisMech is stronger for the
riboflavin transporter mechanism and treatment rationale.

## Curation actions

- Map this record to `Brown-Vialetto-Van_Laere_Syndrome.yaml` as Fazio-Londe
  spectrum context, not as a separate unrelated disease.
- Preserve the absence of prominent deafness when comparing to the broader BVVL
  entry.
- Consider adding Fazio-Londe, OMIM:211500, and SLC52A3 Fazio-Londe aliases to
  future mapping support.
