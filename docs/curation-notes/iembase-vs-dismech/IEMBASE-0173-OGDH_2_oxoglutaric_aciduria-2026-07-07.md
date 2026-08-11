# IEMbase 0173: OGDH-related 2-oxoglutaric aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 173 |
| Nosology | 5.2.13.01 |
| Gene | OGDH |
| External IDs | OMIM:203740; ORPHA:99742 |
| Generated mapping | UNMAPPED; best candidate `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Candidate DisMech targets | None valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as OGDH-related alpha-ketoglutarate dehydrogenase
deficiency, with alternate labels 2-oxoglutaric aciduria and Amish lethal
microcephaly. Treatability is marked unknown, and there are no treatment rows
in the extracted JSON.

The biochemical rows include increased urinary 2-ketoglutaric acid, increased
plasma lactate, increased lactate/pyruvate ratio, decreased plasma glucose,
decreased plasma and urinary ketones, and variable ASAT/ALAT. Clinical rows
include choreoathetosis, sensorineural deafness, depressed nasal bridge,
dolichocephaly, dystonia, dystrophic thumbs, epicanthus, failure to thrive,
long philtrum, low-set ears, osteodystrophy, pyramidal signs, short nose,
axial hypotonia, hypoglycemia, lactic acidosis, liver dysfunction, neurologic
symptoms, and psychomotor delay.

## DisMech phenotype coverage

No valid local DisMech target was found. The generated best candidate,
`D-2-Hydroxyglutaric_Aciduria.yaml`, is a pathway-neighbor false positive. It
mentions alpha-ketoglutarate as the substrate/product context for D2HGDH and
IDH2 disease, but it does not model OGDH, alpha-ketoglutarate dehydrogenase
complex deficiency, or primary 2-oxoglutaric aciduria.

## Concordance and completeness

Judgement: true local gap.

IEMbase points to a distinct Krebs-cycle enzyme deficiency with a recognizable
biochemical signal and syndromic neurologic/dysmorphic phenotype. The current
D-2-HGA entry should not be reused merely because both disorders involve
alpha-ketoglutarate-related metabolites.

## Curation actions

- Do not map this record to `D-2-Hydroxyglutaric_Aciduria.yaml`.
- Add a future OGDH/alpha-ketoglutarate dehydrogenase deficiency entry.
- Expected future coverage: OGDH, impaired 2-oxoglutarate dehydrogenase flux,
  urinary 2-ketoglutaric acid, lactic acidosis, increased lactate/pyruvate
  ratio, hypoglycemia with low ketones, liver dysfunction, psychomotor delay,
  hypotonia, dystonia/choreoathetosis, deafness, and Amish lethal microcephaly
  dysmorphology if supported.
