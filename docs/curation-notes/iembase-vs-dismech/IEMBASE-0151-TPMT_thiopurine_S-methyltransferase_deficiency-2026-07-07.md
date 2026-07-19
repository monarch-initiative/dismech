# IEMbase 0151: TPMT-related thiopurine S-methyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 151 |
| Nosology | 16.2.16.01 |
| Gene | TPMT |
| External IDs | OMIM:610460; OMIM:187680; ORPHA:413687 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No valid TPMT target found; GAMT deficiency candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as TPMT-related thiopurine S-methyltransferase
deficiency, with alternate label poor metabolism of thiopurines 1. Treatability
is marked unknown.

The cached IEMbase phenotype signal is minimal: the only clinical row records
decreased tolerance to thiopurines. No biochemical analyte panel or broader
multisystem phenotype is listed in the extracted symptom table.

## DisMech phenotype coverage

No local TPMT deficiency or thiopurine pharmacogenetic-trait entry was found.
TPMT appears only as pharmacogenetic screening context in diseases where
thiopurine therapy may be used. That is not disease-level coverage for a TPMT
metabolism trait.

The generated best candidate, guanidinoacetate methyltransferase deficiency, is
not valid. GAMT is a creatine-biosynthesis disorder and is unrelated to TPMT
thiopurine methylation.

## Concordance and completeness

Judgement: unmapped scope-review item.

This is not a typical multisystem inborn-error disease record in the local KB
sense; it is primarily a pharmacogenetic decreased-drug-tolerance trait. Current
DisMech has no canonical slot or disease entry for this trait. Whether it should
be curated as a disorder, treatment-toxicity modifier, or left outside disease
scope requires a scope decision.

## Curation actions

- Keep this record unmapped.
- Reject the GAMT deficiency candidate as a methyltransferase lexical false
  positive.
- Before adding a standalone entry, decide whether TPMT poor thiopurine
  metabolism belongs in DisMech as a pharmacogenetic trait or as treatment-risk
  context attached to thiopurine-using disease entries.
