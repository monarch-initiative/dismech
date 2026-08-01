# Dataset Curation

How `datasets:` records get into dismech entries, and why the workflow is shaped
the way it is.

## The problem this solves

A `Dataset` record's `accession` is the one identifier class in dismech that had
no validator behind it. `linkml-reference-validator` checks PMIDs, DOIs, and
NCTs against real sources; nothing resolved `geo:GSE67472`. A fabricated
`geo:GSE9999999` passed `just qc` without complaint.

Dataset accessions are unusually easy to hallucinate — they are short, numeric,
and highly patterned, so a plausible-looking wrong answer costs a model nothing.
Any workflow that adds them in bulk needs a machine check, not a curator's eye.

## Two failure modes, two different guards

The distinction matters, because the second one defeats the first.

**1. The accession does not exist.** Caught by `just verify-datasets`, which
resolves each accession against the repository's own API.

**2. The accession exists, but it is the wrong disease.** *Not* caught by
verification — the accession resolves perfectly. Two routes lead here:

- *Gene-mediated*: searching the causal gene surfaces datasets about whatever
  disease that gene is famous for. `FTL` for neuroferritinopathy returns
  Alzheimer and medulloblastoma series; `FGFR3` for achondroplasia returns
  glioblastoma methylation data.
- *Sibling disease*: relaxing a precise entry name collapses it onto a
  different disease. `Acquired_Angioedema` attracts *hereditary* angioedema
  data; `Acquired_Partial_Lipodystrophy` attracts *familial* partial
  lipodystrophy data.

This is [Named Entity Confusion](../CLAUDE.md#2b-named-entity-confusion-nec--the-dr-report-describes-the-wrong-disease)
arriving through dataset search rather than through a deep-research report. The
tooling reduces it (candidates are tagged `DIRECT` / `GENE_ONLY` / `CONFLICT`)
but cannot eliminate it, so **relevance triage stays a human/model judgement**.

## The workflow

```bash
# 1. What still needs datasets?
just datasets-coverage

# 2. Candidates for one disorder, real by construction
just discover-datasets Asthma

# 3. Batch: search + verify + write a proposal file
uv run python scripts/build_dataset_records.py propose \
    --slugs-file batch.txt --out proposals/batch.json

# 4. Triage -- the step that cannot be skipped
uv run python scripts/triage_dataset_proposals.py show proposals/batch.json
uv run python scripts/triage_dataset_proposals.py reject proposals/batch.json \
    --accession geo:GSE219154 --reason "sibling disease"

# 5. Write approved records into the KB
uv run python scripts/build_dataset_records.py apply proposals/batch.json

# 6. Validate
just verify-datasets kb/disorders/Asthma.yaml
just validate kb/disorders/Asthma.yaml
```

For repositories GEO search cannot reach (PRIDE, MetaboLights, EGA, dbGaP,
cellxgene), use the deep-research path:

```bash
just research-datasets openscientist Marfan_Syndrome
```

Treat its output as **candidate accessions only** — every one must pass
`just verify-datasets --accession <acc>` before curation. The template is
written so that an empty answer is a safe answer, because the failure that
matters is an invented accession, not a short list.

## What a generated record contains

Every field comes from the repository's own metadata, so there is nothing for a
model to invent:

| Field | Source |
|---|---|
| `accession` | GEO, re-verified against NCBI E-utilities |
| `title` | GEO's title, verbatim |
| `description` | GEO's summary, trimmed at a sentence boundary |
| `organism` | GEO `taxon`, mapped to NCBITaxon |
| `data_type` | GEO `gdsType`, mapped to `DatasetTypeEnum` |
| `sample_count` | GEO `n_samples` |
| `publication` | GEO's own linked PMID |
| `notes` | provenance: how it was found and when it was verified |

### Why there is no `evidence:` block

A dismech evidence item requires an exact quote from the cited abstract.
Generating those in bulk is exactly where fabrication enters — it is the
[SOP](../CLAUDE.md#standard-operating-procedure-addingediting-evidence)'s
central warning. Bulk-generated dataset records therefore carry `publication:`
and provenance `notes` instead, and evidence enrichment is left as a deliberate
follow-up for a curator or a targeted, verified agent pass.

## Verification statuses

| Status | Meaning |
|---|---|
| `OK` | Resolved to a real record |
| `PREFIX_MISMATCH` | Record exists, filed under the wrong prefix (e.g. a BioProject ID as `sra:`) |
| `NOT_FOUND` | Did not resolve — treat as fabricated until shown otherwise |
| `MALFORMED` | Does not match any known accession pattern |
| `UNSUPPORTED` | No per-record public API (cellxgene, GTEx, ENCODE, TCGA) or a literature ID used as an accession |

`UNSUPPORTED` is not a pass. 82 records in the KB use a PMID or DOI as their
`accession`, which is a real data-quality problem: a paper is not a dataset.
They are reported rather than failed because fixing them needs a human.

## Supported repositories

NCBI GEO / SRA / BioProject / dbGaP, EBI BioStudies (ArrayExpress) / PRIDE /
MetaboLights / MGnify, EGA, MassIVE, and NASA OSDR. Adding another means writing
a resolver in `scripts/verify_dataset_accessions.py` and registering its
accession shape.
