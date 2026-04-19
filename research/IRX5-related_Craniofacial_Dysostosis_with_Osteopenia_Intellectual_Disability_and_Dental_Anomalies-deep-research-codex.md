# IRX5-related craniofacial dysostosis with osteopenia, intellectual disability, and dental anomalies

Date: 2026-04-16

## Scope

Manual curation note for a new disease-level dismech entry covering the
IRX5-associated Hamamy syndrome spectrum with emphasis on:

- conservative MONDO grounding
- exact PMID-backed snippets
- a small mechanism graph centered on craniofacial migration and osteogenic
  mineralization defects
- no unsupported treatment claims

## Naming and grounding checks

- Current public MONDO / ClinGen / GenCC anchor:
  - `MONDO:0012634`
  - public label: `craniofacial dysplasia - osteopenia syndrome`
- User-requested framing:
  - `IRX5-related craniofacial dysostosis with osteopenia, intellectual disability, and dental anomalies`
- Curation choice:
  - `name` and `disease_term.preferred_term` use the more explicit IRX5-related
    disease phrasing requested by the user and echoed in the recent ClinGen
    evidence summary.
  - `disease_term.term.label` stays exactly on the current public MONDO label
    `craniofacial dysplasia - osteopenia syndrome`.
  - `Hamamy syndrome` is carried as a synonym rather than the primary disease
    label.

## External grounding captured

- ClinGen gene validity:
  - `IRX5`
  - `HGNC:14361`
  - disease anchor `MONDO:0012634`
  - mode of inheritance `Autosomal recessive`
  - classification `Moderate`
  - curation id `CCID:009212`
- Orphanet / GenCC context:
  - disease submitted under Orphanet `ORPHA:314555`
  - submitted phrasing includes
    `facial dysmorphism-ocular anomalies-osteopenia-intellectual disability-dental anomalies syndrome`

## Evidence set selected

### Core clinical framing

- `PMID:17230486`
  - first syndrome description
  - strongest abstract quote for hypertelorism, enamel hypoplasia, osteopenia,
    fractures, myopia, hearing loss, and borderline intelligence

- `PMID:34899143`
  - fourth reported family
  - strongest abstract quote for developmental delay, intellectual disability,
    dentinogenesis imperfecta, bone fragility, and homozygous `IRX5` variant

### Molecular disease definition

- `PMID:22581230`
  - discovery paper linking the syndrome to `IRX5`
  - strongest abstract quote for:
    - recessive inheritance
    - homeodomain dysfunction
    - multisystem developmental framing
    - branchial-arch / progenitor migration via `SDF1`

### Experimental mechanism support

- `PMID:27453922`
  - osteoblast-lineage mouse work
  - strongest quote for cranial mineralization defects, enlarged sutures, and
    reduced osteogenic genes

- `PMID:32662900`
  - experimental skeletal biology support showing that `Irx3`/`Irx5` loss causes
    severe bone deficiency and supports a broader osteogenic role for `IRX5`

### Not central to YAML but useful context

- `PMID:30729910`
  - neuropsychological follow-up in Hamamy syndrome
  - supports that cognitive and language/attention phenotypes are measurable and
    clinically relevant, but not needed once `PMID:34899143` is used for the
    cleaner disease-level intellectual-disability statement

## Mechanism graph chosen

1. `Biallelic IRX5 homeodomain dysfunction`
2. `Impaired cranial neural crest and branchial arch progenitor migration`
3. `Craniofacial developmental defect`
4. `Impaired osteoblast maturation and cranial mineralization`
5. `Osteopenia and bone fragility`

Rationale:

- `PMID:22581230` gives the cleanest proximal molecular lesion and the
  craniofacial-migration mechanism via `SDF1`.
- `PMID:27453922` and `PMID:32662900` give the cleanest skeletal mechanism for
  osteogenic/mineralization failure.
- I did **not** add a dedicated mechanistic node for intellectual disability.
  The human phenotype is real and curated in `phenotypes`, but the available
  abstract-level mechanism evidence is still strongest for craniofacial and bone
  developmental programs rather than a directly demonstrated neural mechanism.

## Specific curation choices

- Included phenotype entries for:
  - `Hypertelorism`
  - `Osteopenia`
  - `Intellectual disability`
  - `Enamel hypoplasia`
  - `High myopia`

- Did **not** add frequency qualifiers.
  Reason: the published case count is too small and the abstracts do not provide
  robust quantitative support for frequency bands.

- Did **not** add treatment entries.
  Reason: available abstract-level evidence in the selected source set is aimed
  at syndrome characterization and mechanism, not disease-specific therapeutic
  efficacy.

- Did **not** split Hamamy syndrome into a separate root page.
  Reason: in current curated usage, Hamamy syndrome is the historical syndrome
  name for this `IRX5` disease entity rather than a clearly separable
  non-IRX5 umbrella.
