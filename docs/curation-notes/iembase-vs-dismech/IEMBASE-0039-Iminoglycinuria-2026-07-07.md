# IEMbase 0039: SLC36A2/SLC6A20/SLC6A19-related iminoglycinuria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 39 |
| Nosology | 1.11.02.01 |
| Gene | SLC36A2; SLC6A20; SLC6A19 |
| External IDs | OMIM:242600 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents iminoglycinuria as a benign amino-acid transporter phenotype
involving urinary loss of imino acids and glycine. The biochemical signal is
increased urinary proline, increased urinary 4-hydroxyproline, and increased
urinary glycine. Prevalence is listed as 1:15,000, subtype is "benign form,"
and the characteristic clinical row is "No clinical significance." No
treatment rows are present.

## DisMech phenotype coverage

There is no current DisMech entry or subtype for iminoglycinuria. Although one
of the listed genes, SLC6A19, overlaps with Hartnup disease, Hartnup disease is
not a valid mapping target. The local Hartnup entry centers on SLC6A19/B0AT1
neutral amino-acid transport, tryptophan/nicotinamide biology, pellagra-like
rash, ataxia, neuropsychiatric episodes, and neutral aminoaciduria. IEMbase
iminoglycinuria instead tracks proline, hydroxyproline, and glycine loss and is
explicitly clinically benign.

## Concordance and completeness

Judgement: generated unmapped status is correct. This is not a hidden Hartnup
match despite partial gene overlap.

IEMbase has enough information to identify the biochemical transporter
phenotype, but the record does not describe a mechanism-rich clinical disorder.
Given DisMech's mechanism-first disease scope, this may be lower priority than
the severe serine, GABA, and glutamine metabolism disorders in the same batch.

## Curation actions

- Do not map this record to `Hartnup_Disease.yaml`.
- If curated, decide explicitly whether benign iminoglycinuria is in scope as a
  disease entry or better handled as a biochemical trait/transport phenotype.
- Preserve the multigene transporter framing rather than reducing the disease to
  SLC6A19 alone.
