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

## Which source to use

Sources are not interchangeable, and two of them mostly duplicate others.
Figures below are measured, not estimated.

| Source | Recipe | Coverage | Use it for |
|---|---|---|---|
| **EGA** | `discover_ega.py` | 10,453 studies | Controlled-access human cohorts GEO cannot index |
| **GEO** | `discover_datasets.py` | — | Common/complex disease. Poor for rare disease (see below) |
| **ArrayExpress** | `discover_arrayexpress.py` | 21,319 native of 80,697 | **73.6% are GEO re-imports** — native submissions only |
| **OmicsDI** | `discover_omicsdi.py` | aggregator | **89% duplicates other sources** — used only as a router to Metabolomics Workbench / MassIVE / dbGaP |

Two rules follow from the measurements:

**Never curate ArrayExpress `E-GEOD-*` records.** `E-GEOD-19431` *is* `GSE19431`.
Curating both puts one experiment in an entry twice under two accessions that
both resolve, which no verifier can detect.

**Never curate OmicsDI hits from GEO/ArrayExpress/PRIDE/MetaboLights/EGA.** Same
duplication problem, one aggregation layer further out.

### Why GEO stops working for rare disease

Measured over 140 Mendelian entries: 24% yielded anything and 40% of proposals
were rejected as wrong-disease. A GEO series carries no coded disease, so for a
rare disorder the only available signal is its causal gene — and a gene hit is
usually a study *about something else*. Prefer EGA and dbGaP there.

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

# 6. Confirm only `datasets:` moved
git diff kb/disorders/Asthma.yaml

# 7. Validate
just verify-datasets kb/disorders/Asthma.yaml
just validate kb/disorders/Asthma.yaml

# 8. Record the change (CLAUDE.md requires a history record per KB edit)
uv run python scripts/new_history.py --kind disorder --slug Asthma \
    --event EDIT --outcome changed --sections datasets \
    --summary "Add public dataset records from GEO" --details "..."
```

`apply` splices records in as text and then re-parses to confirm nothing but
`datasets:` changed, so step 6 should show a pure addition. Note that
`just new-history` cannot take multi-word argument values (`just`'s `*ARGS`
interpolation re-splits on whitespace) — scripted callers must invoke
`scripts/new_history.py` directly, as above.

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
MetaboLights / MGnify, EGA, MassIVE, NASA OSDR, and Metabolomics Workbench.
Adding another means writing a resolver in
`scripts/verify_dataset_accessions.py` and registering its accession shape.

For discovery, the ArrayExpress and EGA study indexes resolve offline against
committed retrieval metadata. Their bulk archives are gitignored and rebuilt with
`--refresh`; only the derived index or a retrieval stamp is committed.

## Known KB issues this tooling surfaced

Recorded here because they are curation problems rather than tooling ones:

- **`Dorsalgia` is bound to `MONDO:0000001`** ("disease", the ontology root).
  The only such entry. Its disease term matches essentially anything, which is
  why it attracted prostate-cancer and Parkinson datasets from GEO. The
  matchers now blocklist bare generic phrases, but the binding should be fixed.
- **Four entries are bound to a parent concept**, so searching the label
  retrieves the general disease: `BRCA_Mutant_Prostate_Cancer` → "prostate
  cancer", `NRAS_Mutant_Melanoma` → "cutaneous melanoma",
  `Arsenic_Related_Cancers` → "squamous cell carcinoma",
  `Hospital-Acquired_Acute_Kidney_Injury` → "kidney injury". The matchers drop
  an over-broad label; the bindings may still warrant review.
- **Two near-synonymous entry pairs** behave as one entity to any name- or
  gene-driven process: `Addisons_Disease` / `Chronic_Primary_Adrenal_Insufficiency`
  and `Neuromyelitis_Optica` / `Neuromyelitis_Optica_Spectrum_Disorder`.
- **OAK is unimportable under this project's Python** (`pyhornedowl` raises
  `AttributeError: 'typing.Union' object attribute '__doc__' is read-only`),
  which is why `scripts/run_term_validator.sh` exits 1 with no output on every
  file. Ontology lookups in the newer discovery scripts use the OLS4 REST API
  instead.
