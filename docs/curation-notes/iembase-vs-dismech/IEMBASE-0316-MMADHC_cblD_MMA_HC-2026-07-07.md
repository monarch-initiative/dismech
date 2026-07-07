# IEMbase 0316: MMADHC-related methylmalonic aciduria and homocystinuria, cblD type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 316 |
| Nosology | 21.9.11.03 |
| Gene | MMADHC |
| External IDs | OMIM:277410; ORPHA:79283 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Manual target `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as the combined MMADHC/cblD form with methylmalonic
aciduria and homocystinuria. Characteristic rows include megaloblastic anemia,
failure to thrive, life-threatening illness, neurologic dysfunction, and
impaired vision.

Additional clinical rows include cardiomyopathy, cerebral atrophy, dementia,
developmental delay, dysmorphic features, extrapyramidal signs, feeding
difficulties, hematuria, hemolytic uremic syndrome, hypotonia, liver
dysfunction, low weight, maculopathy, myelopathy, hypersegmented neutrophils,
nystagmus, psychiatric disturbance, retinopathy, and seizures.

The biochemical pattern spans both MMA and remethylation branches: elevated
urine and plasma homocysteine, low-to-normal plasma methionine, elevated C3
propionylcarnitine in blood and plasma, elevated urinary 3-hydroxypropionic
and methylcitric acids, elevated methylmalonic acid in plasma and urine, and
decreased S-adenosylmethionine in CSF and plasma. Treatment rows are
hydroxycobalamin, betaine, and carnitine.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local target is
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.

DisMech already has a cblD subtype for MMADHC deficiency and states that
MMADHC defects can produce isolated methylmalonic acidemia, isolated
homocystinuria, or combined disease. The same file covers methylmalonic
aciduria, homocystinuria, hyperhomocysteinemia, hypomethioninemia,
megaloblastic anemia, intellectual disability, seizures, hypotonia, global
developmental delay, encephalopathy, failure to thrive, renal thrombotic
microangiopathy, and hydroxocobalamin, betaine, and L-carnitine treatment.

Prior notes for IEMbase 88 and 89 already identify the isolated cblD-MMA and
cblD-HC records as false negatives to the same local cblD subtype. This record
is the combined branch of the same MMADHC spectrum.

## Concordance and completeness

Judgement: false-negative mapping with high umbrella-level local coverage.

Concordance is high for MMADHC/cblD identity, combined methylmalonic aciduria
and homocystinuria, megaloblastic anemia, developmental and neurologic
involvement, renal thrombotic microangiopathy or HUS-like disease, and
hydroxocobalamin, betaine, and carnitine therapy.

The main gap is subtype granularity. DisMech has one cblD subtype rather than
separate cblD-MMA, cblD-HC, and combined cblD-MMA/HC branches. IEMbase also
adds detailed biomarker compartment prompts for C3 propionylcarnitine,
3-hydroxypropionic acid, methylcitric acid, methylmalonic acid, homocysteine,
methionine, and S-adenosylmethionine.

## Curation actions

- Update the mapping logic or manual crosswalk to resolve this record to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.
- Consider splitting cblD into isolated MMA, isolated HC, and combined forms if
  subtype granularity becomes important.
- Preserve the combined biochemical signal when curating: MMA markers,
  homocysteine elevation, low-to-normal methionine, and low
  S-adenosylmethionine.
