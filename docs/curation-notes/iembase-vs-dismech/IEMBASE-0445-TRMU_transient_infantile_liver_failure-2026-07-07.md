# IEMbase 0445: TRMU-related transient infantile liver failure

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 445 |
| Nosology | 10.1.12.01 |
| Gene | TRMU |
| External IDs | OMIM:613070; ORPHA:90641 |
| Generated mapping | UNMAPPED; low candidate `Guanidinoacetate_Methyltransferase_Deficiency.yaml` |
| Candidate DisMech targets | Partial TRMU context in `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TRMU-related
tRNA 5-methylaminomethyl-2-thiouridylate-methyltransferase deficiency, also
called transient infantile liver failure. It records autosomal recessive
inheritance. Biochemical rows include decreased multiple OXPHOS enzyme
activities in muscle. Clinical rows emphasize neonatal or infantile jaundice,
vomiting, coagulopathy, hepatosplenomegaly, liver failure, and pancreatic
failure. IEMbase records cysteine as a pharmacological treatment row.

## DisMech phenotype coverage

The generated `Guanidinoacetate_Methyltransferase_Deficiency.yaml` candidate is
a false positive. Local GAMT deficiency is a creatine-biosynthesis disorder with
guanidinoacetate accumulation and neurologic disease; it is unrelated to TRMU
mitochondrial tRNA modification and infantile liver failure.

`Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` contains relevant
TRMU context: it treats TRMU as genetic heterogeneity or a nuclear contributor
to a phenotypically similar reversible infantile respiratory-chain deficiency
and includes the L-cysteine/TRMU functional relationship. However, that local
file is centered on MT-TE reversible infantile cytochrome c oxidase deficiency,
not a dedicated TRMU transient infantile liver failure entity with liver,
coagulation, pancreatic, and hepatosplenomegaly rows.

## Concordance and completeness

Judgement: partial false negative/context mapping. The local reversible
infantile cytochrome c oxidase deficiency file captures TRMU-related mechanism
and cysteine context, but a dedicated TRMU transient infantile liver failure
target remains a gap if DisMech intends to model the liver-failure phenotype as
its own disease entity.

## Curation actions

- Do not map to `Guanidinoacetate_Methyltransferase_Deficiency.yaml`.
- Use `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml` only as
  TRMU-related heterogeneity and cysteine-mechanism context.
- Before importing the IEMbase liver-failure rows, decide whether to create a
  dedicated TRMU transient infantile liver failure target or an explicit subtype
  under an existing mitochondrial tRNA-modification/respiratory-chain disease
  file.
- If curated, include TRMU, autosomal recessive inheritance, mitochondrial tRNA
  thiolation or modification, decreased muscle OXPHOS enzyme activities,
  transient infantile liver failure, jaundice, vomiting, coagulopathy,
  hepatosplenomegaly, pancreatic failure, and cysteine responsiveness.
