# IEMbase 0088: MMADHC-related methylmalonic aciduria, cblDv2 type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 88 |
| Nosology | 21.9.11.01 |
| Gene | MMADHC |
| External IDs | OMIM:277410 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMADHC-related methylmalonic
aciduria, vitamin B12-responsive cblD variant 2 type, with alternate labels
cblD type and cblD-MMA. Treatability is marked yes.

The characteristic clinical rows include acidosis, dehydration, acute
encephalopathic crisis, failure to thrive, ketosis, life-threatening illness,
and vomiting.

The biochemical panel includes elevated urinary and plasma methylmalonic acid,
urinary methylcitric acid, urinary 3-hydroxypropionic acid, C3 propionylcarnitine
in blood or plasma, ammonia, anion gap, lactate, total plasma homocysteine, and
free carnitine in dried blood spot or plasma.

Treatment rows include antibiotics, avoidance of fasting, carnitine,
hemodialysis, hydroxycobalamin, liver and/or kidney transplantation,
carglumic acid, peritoneal dialysis, protein-defined diet, sick-day management,
and sodium benzoate.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local target is
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.

DisMech already has a cblD subtype for MMADHC deficiency, describing MMADHC
variants that can produce isolated methylmalonic acidemia, isolated
homocystinuria, or combined disease. The pathophysiology section includes
MMADHC in impaired intracellular cobalamin cofactor synthesis and cites the
variant 2 form of cblD as linked to adenosylcobalamin synthesis. This matches
IEMbase's cblDv2/cblD-MMA framing.

`Methylmalonic_Acidemia.yaml` is relevant for shared isolated-MMA phenotype and
treatment coverage, but it currently lists MMUT, MMAA, and MMAB explicitly and
does not provide an MMADHC/cblD genetic section. The cobalamin umbrella is
therefore the better canonical target for this IEMbase record.

## Concordance and completeness

Judgement: false-negative mapping with moderate-to-high local coverage.

The main local gap is subtype granularity: DisMech has a single cblD subtype
rather than separate cblD-MMA/cblDv2, cblD-HC/cblDv1, and combined cblD forms.
It also does not mirror all IEMbase acute-treatment rows for the isolated MMA
presentation.

## Curation actions

- Update the mapping logic or manual crosswalk to resolve this record to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.
- Consider splitting cblD into cblD-MMA, cblD-HC, and combined forms if subtype
  granularity becomes important.
- Consider adding MMADHC/cblD-v2 as explicit secondary genetic coverage in
  `Methylmalonic_Acidemia.yaml` if isolated MMA is kept as a broad entry.
