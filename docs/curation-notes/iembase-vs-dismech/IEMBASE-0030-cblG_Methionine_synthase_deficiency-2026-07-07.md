# IEMbase 0030: MTR-related methionine synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 30 |
| Nosology | 1.5.13.01 |
| Gene | MTR |
| External IDs | OMIM:250940 |
| Generated mapping | MAPPED by `alias_exact:cblg` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblG` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents methionine synthase deficiency, cblG type. Characteristic
features are megaloblastic anemia and neurologic symptoms. Additional features
include developmental delay, failure to thrive, ataxia, cerebral atrophy on
MRI, hypertonia or hypotonia, lethargy, adult myelopathy, nystagmus,
psychiatric disturbance, seizures, impaired vision, and vomiting.

The biochemical signature is isolated remethylation failure: elevated urinary
and plasma homocysteine, low-to-normal plasma methionine, normal plasma and
urine methylmalonic acid, and low S-adenosylmethionine in CSF and plasma.
Treatments listed are hydroxycobalamin and betaine.

## DisMech phenotype coverage

The generated subtype mapping is correct. DisMech includes cblG as an MTR
subtype within the cobalamin metabolism and transport umbrella. It models
impaired methionine synthase activity/remethylation, homocystinuria,
hyperhomocysteinemia, hypomethioninemia, megaloblastic anemia, intellectual
disability, seizures, hypotonia, global developmental delay, encephalopathy,
failure to thrive, and hydroxocobalamin/betaine therapy, with supportive
avoidance of nitrous oxide and methionine restriction.

## Concordance and completeness

Judgement: correct subtype mapping and good high-level concordance, but
DisMech is currently more umbrella-level than cblG-specific.

IEMbase adds cblG-specific normal methylmalonic acid, low CSF/plasma SAM,
cerebral atrophy, myelopathy, nystagmus, impaired vision, psychiatric
disturbance, vomiting, and explicit hydroxycobalamin/betaine treatment rows.
DisMech gives stronger mechanism and broader cobalamin-context coverage.

## Curation actions

- Keep the generated subtype mapping.
- Consider adding cblG-specific normal methylmalonic acid and low SAM markers.
- Consider whether cerebral atrophy, myelopathy, nystagmus, vision impairment,
  and vomiting should be added as cblG/cblE subtype-specific phenotypes.
