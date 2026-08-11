# IEMbase 0031: MTRR-related methionine synthase reductase deficiency, cblE

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 31 |
| Nosology | 21.9.12.01 |
| Gene | MTRR |
| External IDs | OMIM:236270 |
| Generated mapping | MAPPED by `alias_exact:cble` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblE` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents methionine synthase reductase deficiency, cblE type.
Characteristic features are megaloblastic anemia and neurologic symptoms.
Additional clinical features include developmental delay, failure to thrive,
ataxia, cerebral atrophy on MRI, hypertonia or hypotonia, adult myelopathy,
nystagmus, psychiatric disturbance, seizures, and impaired vision.

The biochemical signal matches an isolated remethylation defect: elevated urine
and plasma homocysteine, low-to-normal methionine, normal plasma and urinary
methylmalonic acid, and low CSF/plasma S-adenosylmethionine. Treatments listed
are hydroxycobalamin and betaine.

## DisMech phenotype coverage

The generated subtype mapping is correct. DisMech includes cblE as an MTRR
subtype in `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml`, models
the MTRR role in reductive reactivation of methionine synthase, and covers the
shared remethylation phenotype: homocystinuria, hyperhomocysteinemia,
hypomethioninemia, megaloblastic anemia, neurologic injury, developmental
delay, seizures, hypotonia, encephalopathy, failure to thrive, hydroxocobalamin,
and betaine.

## Concordance and completeness

Judgement: correct subtype mapping and good high-level concordance, with the
same subtype-granularity limitation seen for cblG.

IEMbase adds cblE-specific normal methylmalonic acid, low SAM in CSF/plasma,
cerebral atrophy, myelopathy, nystagmus, impaired vision, psychiatric
disturbance, and treatment rows. DisMech is stronger for pathway mechanism and
the broader cobalamin-disorder context.

## Curation actions

- Keep the generated subtype mapping.
- Consider adding cblE-specific biochemical markers and selected neurologic or
  imaging findings if evidence supports them.
- Keep cblE and cblG grouped as isolated remethylation defects, but avoid
  importing methylmalonic acidemia features from cblC/cblA/cblB.
