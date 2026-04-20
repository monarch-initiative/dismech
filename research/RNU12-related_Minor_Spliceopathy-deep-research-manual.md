---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-19T00:00:00Z'
end_time: '2026-04-19T00:45:00Z'
duration_seconds: 2700.0
citation_count: 2
notes: >
  Manual deep research was performed from the two primary RNU12 disease papers,
  local MONDO/GO/HPO/HGNC lookup, and the MONDO NTR framing for the umbrella
  concept. The goal of this first-pass artifact was to justify the umbrella
  disease scope, identify the minimum safe phenotype set for the initial PR, and
  document which additional subtype features were intentionally deferred.
---

## Question

Curate a mechanism-defined umbrella entry for RNU12-related minor spliceopathy
that spans the reported RNU12 clinical presentations, while documenting the
shared minor spliceosome mechanism, subtype framing, and the rationale for the
initial phenotype scope.

## Output

# RNU12-related Minor Spliceopathy Manual Deep-Research Note

## Scope

- Parent curation frame: local mechanism-defined umbrella disease for
  `RNU12-related minor spliceopathy`
- MONDO status: umbrella concept tracked as MONDO NTR `#9963`, not yet a stable
  local MONDO term
- Reported clinical presentations currently within scope:
  - `MONDO:0011287` craniosynostosis-anal anomalies-porokeratosis syndrome
    (`CDAGS`)
  - `MONDO:0859360` spinocerebellar ataxia, autosomal recessive 33 (`SCAR33`)
- Shared molecular mechanism in scope:
  - biallelic `RNU12` variation
  - minor spliceosome dysfunction
  - impaired U12-type intron splicing / minor intron retention

## Primary Sources Used

- PMID:34085356
  - Defines the CDAGS presentation and establishes biallelic `RNU12` variants
    with transcriptome/splicing abnormalities in lymphoblastoid cells.
- PMID:27863452
  - Defines the SCAR33 presentation and demonstrates selective disruption of
    U12-type intron splicing with minor intron retention in affected
    individuals.

## Core Curation Decisions

### Disease framing

- The two disease papers support a broader shared-disorder frame rather than two
  fully unrelated single-presentation entries, because both presentations are
  caused by biallelic `RNU12` disruption and converge on defective minor
  spliceosome function.
- The YAML therefore uses a mechanism-defined umbrella root with explicit
  `has_subtypes` entries for `CDAGS` and `SCAR33`.

### Initial phenotype scope

- This first-pass PR intentionally models one high-signal anchor phenotype per
  subtype:
  - `CDAGS` -> craniosynostosis
  - `SCAR33` -> early-onset cerebellar ataxia
- The purpose of this minimal phenotype set is to establish the umbrella entry
  and subtype foreign-key structure without over-claiming frequency or phenotype
  completeness from only two primary abstracts.

### Additional subtype features identified but deferred

- `CDAGS` features explicitly named in PMID:34085356 and suitable for later
  phenotype expansion:
  - delayed closure of the fontanelles
  - cranial defects
  - clavicular hypoplasia
  - anal malformations
  - genitourinary malformations
  - skin manifestations including porokeratosis
- `SCAR33` features named in the disease report / summary framing and suitable
  for later phenotype expansion:
  - delayed motor development
  - hypotonia
  - tremor
  - nystagmus
  - dysarthria
  - cerebellar hypoplasia or degeneration

## Evidence-Type Decision

- The transcriptome / alternative splicing result from PMID:34085356 comes from
  lymphoblastoid cells and should be treated as `IN_VITRO`, not
  `HUMAN_CLINICAL`, even though the variants were discovered in human families.

## Ontology Anchors Used

- Disease / subtype terms:
  - `MONDO:0011287` craniosynostosis-anal anomalies-porokeratosis syndrome
  - `MONDO:0859360` spinocerebellar ataxia, autosomal recessive 33
- Gene:
  - `hgnc:19380` RNU12
- Biological process:
  - `GO:0000398` mRNA splicing, via spliceosome
- Phenotypes:
  - `HP:0001363` Craniosynostosis
  - `HP:0001251` Ataxia, rendered with preferred term `Cerebellar ataxia`
    because the local HPO snapshot does not provide the reviewer-suggested
    `HP:0002070` label for this concept.

## Follow-up Work Deferred Beyond This PR

- Expand subtype phenotype coverage using exact abstract-backed evidence items
  for additional CDAGS and SCAR33 manifestations.
- Revisit whether a more specific GO term for minor/U12 spliceosome function is
  available and preferable to `GO:0000398`.
- Add phenotype-targeted downstream links if the entry is expanded into a denser
  connected pathograph.
