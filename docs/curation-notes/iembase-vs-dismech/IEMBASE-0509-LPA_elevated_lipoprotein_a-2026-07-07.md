# IEMbase 0509: LPA-related elevated lipoprotein(a)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 509 |
| Nosology | 15.6.31.01 |
| Gene | LPA |
| External IDs | OMIM:152200; ORPHA:250831 |
| Generated mapping | UNMAPPED; best candidate `Tangier_Disease.yaml` |
| Candidate DisMech targets | No exact local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as LPA-related elevated lipoprotein(a). No treatments
are listed. The biochemical rows are highly specific for the lipid trait:
normal-to-increased serum cholesterol, normal HDL cholesterol, normal serum
triglycerides, and very increased plasma lipoprotein(a) across age groups.

The clinical rows are adult vascular disease: carotid artery disease, coronary
artery disease, and myocardial ischemia.

## DisMech phenotype coverage

No exact local target was found for LPA-related elevated lipoprotein(a).
`Tangier_Disease.yaml` is not a valid target: it models ABCA1-related HDL
biogenesis and cholesterol-efflux failure with very low or absent HDL, orange
tonsils, hepatosplenomegaly, and neuropathy. That is the opposite biochemical
direction from this IEMbase profile, where HDL is normal and lipoprotein(a) is
the isolated striking abnormality.

`Hyperlipidemia.yaml`, `Familial_Hypercholesterolemia.yaml`, `Heart_Failure.yaml`,
and `Peripheral_Artery_Disease.yaml` provide broad lipid or vascular context,
including atherogenic lipoprotein and coronary disease mechanisms, but they do
not model LPA gene dosage/isoform biology, isolated high lipoprotein(a), or
LPA-related elevated lipoprotein(a) as a distinct inherited lipid disorder.

## Concordance and completeness

Judgement: true local gap.

IEMbase is not simply describing general hypercholesterolemia. The defining
signal is very increased plasma lipoprotein(a) with normal HDL and triglycerides
and adult atherosclerotic outcomes. No local DisMech entry captures that exact
gene-trait-disease entity.

## Curation actions

- Track LPA-related elevated lipoprotein(a) as a local lipid-disorder gap.
- Reject `Tangier_Disease.yaml` as a false candidate driven by lipoprotein
  vocabulary overlap.
- If curated, seed the future entry with plasma lipoprotein(a), normal HDL and
  triglyceride contrast, carotid/coronary artery disease, myocardial ischemia,
  and links to vascular-disease mechanism context rather than substituting those
  context entries as the disease itself.
