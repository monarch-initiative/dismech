# IEMbase 0025: GNMT-related glycine N-methyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 25 |
| Nosology | 1.5.03.01 |
| Gene | GNMT |
| External IDs | OMIM:606664 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Guanidinoacetate_Methyltransferase_Deficiency.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents glycine N-methyltransferase deficiency as a sulfur
amino-acid/methylation disorder. The clinical signal is sparse: possible
failure to thrive in infancy and possible hepatomegaly in infancy or childhood.

The biochemical signal is much stronger than the clinical signal: markedly
elevated plasma methionine, markedly elevated plasma S-adenosylmethionine,
normal S-adenosylhomocysteine, normal urinary sarcosine, normal-to-mildly high
total plasma homocysteine, and mild transaminase elevation. No treatment rows
are present and treatability is listed as unknown.

## DisMech phenotype coverage

There is no current standalone DisMech entry or subtype for GNMT deficiency. The
best fuzzy candidate, `Guanidinoacetate_Methyltransferase_Deficiency.yaml`, is a
false positive driven by the word methyltransferase. GAMT deficiency is a
cerebral creatine deficiency disorder with guanidinoacetate accumulation,
creatine depletion, epilepsy, developmental delay, and creatine/substrate
reduction therapy. That is not the same disease mechanism or phenotype pattern
as GNMT-related hypermethioninemia and elevated SAM.

The broader methionine-cycle/sulfur amino-acid umbrella is conceptually closer
than the fuzzy GAMT candidate, but it does not currently list GNMT deficiency as
a subtype.

## Concordance and completeness

Judgement: generated status is appropriately unmapped, and the fuzzy GAMT
candidate should be rejected.

IEMbase supplies enough biochemical signal to define a future GNMT curation
target, but there is no local phenotype completeness comparison to make against
a valid DisMech disease entry. The closest local reusable context is the
methionine-cycle pathway group, not GAMT deficiency.

## Curation actions

- Do not map this record to `Guanidinoacetate_Methyltransferase_Deficiency.yaml`.
- Consider adding GNMT deficiency as a subtype or separate entry under the
  methionine-cycle/sulfur amino-acid area if it becomes a curation priority.
- Preserve the biochemical distinction from MAT1A and AHCY disease: high
  methionine and SAM with normal S-adenosylhomocysteine.
