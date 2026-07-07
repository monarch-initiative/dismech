# IEMbase 0206: TF-related hereditary transferrin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 206 |
| Nosology | 22.2.11.01 |
| Gene | TF |
| External IDs | OMIM:209300; ORPHA:1195 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No direct target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as TF-related hereditary transferrin deficiency, with
alternate labels atransferrinemia and TF. Treatability is marked unknown.

The biochemical rows include increased liver iron and decreased serum
transferrin. Characteristic clinical rows include hypochromic anemia, growth
retardation, hemosiderosis, and recurrent infections. The treatment row lists
plasma transfusion fortified with oral iron.

## DisMech phenotype coverage

No local DisMech entry covers TF-related atransferrinemia. `Hemochromatosis.yaml`
shares the downstream concept of tissue iron overload but is mechanistically
opposite in important ways: hereditary hemochromatosis is primarily
hepcidin-insufficient iron hyperabsorption with high transferrin saturation,
whereas atransferrinemia is a transferrin-deficiency disorder with severe
anemia plus tissue iron deposition. The anemia and transferrin replacement
logic make it unsuitable as a hemochromatosis subtype.

## Concordance and completeness

Judgement: true local disease gap.

IEMbase provides a small but distinctive transferrin-deficiency profile:
TF/atransferrinemia identity, very low serum transferrin, hypochromic anemia,
growth failure, infections, hemosiderosis, liver iron accumulation, and plasma
plus iron treatment. DisMech currently has no canonical target for this
mechanism.

## Curation actions

- Do not map this record to `Hemochromatosis.yaml`.
- Consider a future TF-related atransferrinemia entry under iron transport
  disorders.
- Seed that future entry with low transferrin, hypochromic anemia, paradoxical
  tissue/liver iron overload, growth retardation, recurrent infections,
  hemosiderosis, and plasma transfusion with iron replacement.
