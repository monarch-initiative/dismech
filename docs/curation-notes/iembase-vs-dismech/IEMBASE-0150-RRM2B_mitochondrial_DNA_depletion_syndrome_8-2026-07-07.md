# IEMbase 0150: RRM2B-related mitochondrial DNA depletion syndrome 8

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 150 |
| Nosology | 9.1.07.01 |
| Gene | RRM2B |
| External IDs | OMIM:604712; ORPHA:298 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Partial local context in `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml#MNGIE-like RRM2B` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as RRM2B-related mitochondrial ribonucleotide reductase
subunit 2 deficiency, with alternate label mitochondrial DNA depletion syndrome
8A and 8B. Treatability is marked unknown.

The biochemical rows include increased plasma and CSF lactate, decreased muscle
cytochrome C oxidase, and increased histochemical mitochondrial proliferation.
Clinical rows include muscle mitochondrial DNA depletion, encephalomyopathy,
gastrointestinal dysmotility, hearing loss, hypotonia, peripheral neuropathy,
ophthalmoplegia, renal tubulopathy, and perinatal death.

## DisMech phenotype coverage

The generated table leaves this unmapped, but local partial coverage exists in
`Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml`, which includes a
`MNGIE-like RRM2B` subtype. That subtype records RRM2B as a rare MNGIE-type
gene and covers overlapping gastrointestinal dysmotility, ophthalmoplegia, and
peripheral neuropathy context.

The local MNGIE entry is still anchored on classic TYMP-related MNGIE. It does
not serve as a full standalone target for RRM2B mitochondrial DNA depletion
syndrome 8A/8B, especially for the perinatal, renal tubulopathy, lactate,
cytochrome C oxidase, and mtDNA-depletion details in IEMbase.

## Concordance and completeness

Judgement: partial false negative; local subtype context exists but no canonical
MTDPS8A/8B target.

RRM2B is present locally, so this should not be treated as complete absence of
coverage. But mapping the IEMbase record directly to classic MNGIE would also be
too broad, because IEMbase is focused on RRM2B mitochondrial depletion syndrome
rather than TYMP thymidine phosphorylase deficiency.

## Curation actions

- Record `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml#MNGIE-like RRM2B`
  as partial context, not an exact standalone mapping.
- Future curation should add or split a RRM2B/MTDPS8A-8B target with mtDNA
  depletion, lactic acidosis, COX deficiency, encephalomyopathy, renal
  tubulopathy, hearing loss, ophthalmoplegia, GI dysmotility, and perinatal
  lethality.
