# DepMap Synthetic-Lethality Structured Source

The `DEPMAP:` structured source ingests **synthetic-lethality and
selective-dependency relationships** derived from the Broad Institute's
[Cancer Dependency Map (DepMap)](https://depmap.org/portal/) — genome-scale
CRISPR knockout screens across ~1,000+ cancer cell lines — into
`references_cache/` as deterministic, line-oriented markdown so a disorder
entry can quote a dependency row as snippet-validated evidence.

It is the functional-genomics complement to the literature-based
`dna_repair_synthetic_lethality` module: where that module curates
"BRCA-loss → PARP dependency" from reviews and clinical trials, DepMap provides
the orthogonal cell-line CRISPR evidence for the same synthetic-lethal logic.

## What a DepMap dependency is

A gene's **dependency** (Chronos gene-effect score) measures how essential that
gene is for a model's fitness — a more negative score means stronger
dependency. A gene that is essential **only in a specific genomic context** — a
mutation, a copy-number loss, a lost paralog, or a lineage — is a *selective
dependency*, and the `context → dependency` relationship is the functional
definition of synthetic lethality.

Two record grains are emitted:

| Reference id | Meaning | Example |
|--------------|---------|---------|
| `DEPMAP:<SYMBOL>` | Selective dependency of one gene, aggregating every context it is selectively essential in | `DEPMAP:PARP1`, `DEPMAP:WRN` |
| `DEPMAP:<A>__<B>` | Gene-pair synthetic lethality (paralog SL, collateral lethality, or co-dependency); symbols sorted | `DEPMAP:MTAP__PRMT5`, `DEPMAP:SMARCA2__SMARCA4` |

Gene symbols are the curator-facing key; each gene's HGNC CURIE is carried
inside the body as a quotable row for machine linkage.

## Citing a DepMap dependency

DepMap is pooled cell-line CRISPR data, so `evidence_source: IN_VITRO` and — per
the project evidence policy — it must **never be the sole support for a human
phenotype**. Record the genomic context (the DepMap analog of an ICEES cohort
stratifier), because a dependency is conditioned on it.

```yaml
treatments:
- name: PARP Inhibitor Therapy
  # ... treatment_term / target_mechanisms linking to the synthetic-lethality node ...
  evidence:
  - reference: DEPMAP:PARP1
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: "BRCA1/BRCA2-mutant | DIFFERENTIAL_DEPENDENCY | 4.8 | -0.42 | 38"
    explanation: >-
      DepMap CRISPR screens show PARP1 as a selective dependency in
      BRCA1/BRCA2-mutant cancer models, corroborating the HRR-deficiency
      synthetic-lethal vulnerability.
```

As with ORPHA/ICEES rows, a quoted snippet may include or omit the leading and
trailing pipes; both substring-match against the cached body.

## Building the cache

```bash
just depmap-refresh                       # verify the pinned TSV checksum
just depmap-rebuild                        # rebuild all references_cache/DEPMAP_*.md
just depmap-rebuild --id DEPMAP:MTAP__PRMT5 # one relationship
just depmap-list                           # list available identifiers
```

## Input format and the derivation follow-up

Like the CIViC source, the manifest (`data/depmap/MANIFEST.yaml`, committed)
pins a **derived, line-oriented TSV** (`data/depmap/depmap_synthetic_lethality.tsv`,
gitignored) rather than the multi-hundred-MB `CRISPRGeneEffect` matrix. Each row
is one context-conditioned dependency observation:

```
gene_a_symbol  gene_a_hgnc  gene_b_symbol  gene_b_hgnc  relationship
context  metric_type  metric_value  effect_size  n_models  release
```

`gene_b_*` empty → a single-gene selective dependency (`DEPMAP:<A>`); both
present → a gene-pair record (`DEPMAP:<A>__<B>`). Multiple rows sharing a
reference id are aggregated into one cache file, mirroring how the ICEES source
merges per-cohort chi-square rows.

**Deliberately out of scope for this source:** *deriving* that TSV from a pinned
DepMap release — computing differential dependency between a genomic-feature-
positive and -negative group of models — is a separate, tracked follow-up (a
`scripts/derive_depmap_synthetic_lethality.py`). This module is the
ingestion/serialization half; it parses whatever the pinned TSV contains. A
small illustrative fixture under `tests/data/depmap/` drives the unit tests
(`tests/test_depmap_structured_source.py`); it is **not** real DepMap data and
is never written into the committed `references_cache/`.

## Related

- `kb/modules/dna_repair_synthetic_lethality.yaml` — the literature-based
  synthetic-lethality mechanism module DepMap evidence complements.
- Candidate follow-on modules DepMap discoveries motivate:
  `mtap_deletion_prmt5_dependency` (collateral lethality),
  `paralog_synthetic_lethality` (SMARCA4→SMARCA2, ARID1A→ARID1B),
  `wrn_msi_dependency` (WRN in MSI/MMR-deficient tumors).
