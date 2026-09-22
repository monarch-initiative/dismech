# Structured-database reference sources

## Structured-Database Reference Sources

In addition to fetched literature references (PMID, DOI, NCT), dismech ingests
structured knowledge bases — currently **Orphanet** and **ClinGen** — into
`references_cache/` as deterministic line-oriented markdown files. Each file
holds one entity (one ORPHA disorder) and curators can quote individual rows
as evidence `snippet:` values.

**Available structured prefixes:**

| Prefix | Source | Coverage | License |
|--------|--------|----------|---------|
| `ORPHA:` | Orphadata bulk XML | 8,823 leaf disorders + subtypes | CC-BY 4.0 |
| `CGGV:` | ClinGen Gene-Disease Validity CSV | One record per gene-disease validity assertion | ClinGen terms |
| `CGDS:` | ClinGen Dosage Sensitivity downloads | One record per dosage-sensitive gene | ClinGen terms |
| `CIVIC_ASSERTION:`, `CIVIC_EID:` | CIViC accepted assertion and clinical evidence TSVs | One record per accepted CIViC assertion or evidence item | CIViC |
| `ICEES:` | ICEES Knowledge Graph (KGX, RENCI/UNC) | One record per disease/phenotype comorbidity pair (MONDO/HP both sides), with per-cohort chi-square rows | ICEES terms |
| `NCIT:` | NCI Thesaurus selected predicate edges (via OAK `sqlite:obo:ncit`) | One record per subject carrying a selected predicate; currently `NCIT:P302` (Accepted_Therapeutic_Use_For), 796 drug→indication assertions | NCIT terms |
| `ICTRP:` | WHO International Clinical Trials Registry Platform search portal | One record per trial, fetched per identifier on demand (no bulk file) | WHO ICTRP terms |

**Citing an NCIT P302 (Accepted_Therapeutic_Use_For) treatment indication:**

`NCIT:P302` links a drug to the free-text disease/condition it is an accepted
treatment for. It is ingested by the generic, manifest-driven
`OntologyEdgeSource` (`src/dismech/structured_sources/ontology_edges.py`), which
selects predicate edges out of the OAK-managed NCIT SQLite — the multi-hundred-MB
`.db` is **never committed**, only the selectively generated per-subject cache
files. Each `references_cache/NCIT_<Cxxxx>.md` body holds a unified edge table
(`| ID | LABEL | PRED | TARGET_ID | TARGET_LABEL | METADATA |`); for the string
predicate P302 the indication text is in the METADATA column:

```yaml
treatments:
- name: Midostaurin
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: midostaurin
      term:
        id: NCIT:C1872
        label: Midostaurin
  evidence:
  - reference: NCIT:C1872
    supports: SUPPORT
    evidence_source: OTHER
    snippet: "Midostaurin | Accepted_Therapeutic_Use_For | - | - | acute myeloid leukemia (AML) who are FLT3 mutation-positive (FLT3+)"
    explanation: NCI Thesaurus asserts accepted therapeutic use for FLT3+ AML.
```

As with ORPHA/ICEES rows, a quoted snippet may include or omit the leading and
trailing pipes. Build/refresh and audit coverage with:

```bash
just ncit-edges-refresh                 # ensure OAK NCIT db present, check pinned version
just ncit-edges-rebuild                 # rebuild all references_cache/NCIT_*.md
just ncit-edges-rebuild --id NCIT:C1872 # one drug
just ncit-p302-audit --format summary   # advisory treatment-coverage audit
```

See `projects/NCIT_TREATMENT_INDICATIONS.md` for the completeness project. The
coded molecular-target relation `NCIT:A7` (`Has_Target`) is a natural follow-on
predicate for the same source but is not yet ingested.

**Citing an Orphanet entry:**

```yaml
evidence:
  - reference: ORPHA:558
    supports: SUPPORT
    snippet: "Marfan syndrome is a systemic disease of connective tissue"
    explanation: Orphadata definition supports this characterization.
```

Snippets must be exact substrings of the cache file's body. The body uses
markdown section headings (`## Definition`, `## Inheritance`, `## Phenotypes`,
`## Genes`, `## Epidemiology`, `## Cross-references`, `## Source`) with
markdown tables for tabular data. Each table row is a stable quotable
substring across refreshes:

```
| HP:0002616 | Aortic root aneurysm | Very frequent (99-80%) |
| FBN1 | fibrillin-1 | hgnc:3603 | Disease-causing germline mutation(s) in |
| MONDO:0007947 | Exact |
```

A curator-quoted snippet may include or omit the leading and trailing
pipes — both substring-match against the cached body. Prefer the
unbracketed form for cleaner YAML:

```yaml
snippet: "HP:0002616 | Aortic root aneurysm | Very frequent (99-80%)"
```

**Citing a ClinGen gene-disease validity assertion:**

```yaml
evidence:
  - reference: CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z
    supports: SUPPORT
    snippet: "HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive"
    explanation: ClinGen classifies the HEXB-Sandhoff disease relationship as definitive.
```

ClinGen cache bodies contain a `## Evidence summary` section when the
assertion report page has ClinGen narrative text, plus a `## Gene-disease
validity` markdown table:

```
## Evidence summary

In summary, HEXB is definitively associated with Sandhoff disease.

## Gene-disease validity

| Gene | HGNC | Disease | MONDO | MOI | Classification | SOP | GCEP | Classification date |
| HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive | SOP9 | Lysosomal Diseases Gene Curation Expert Panel | 2022-09-15T16:00:00.000Z |
```

**Citing a ClinGen dosage sensitivity assertion:**

```yaml
evidence:
  - reference: CGDS:HGNC_9585
    supports: SUPPORT
    snippet: "PTCH1 | HGNC:9585 | 5727 | 9q22.32 | chr9:95442980-95516971 | 3 - Sufficient Evidence for Haploinsufficiency | 0 - No Evidence for Triplosensitivity | 2020-07-01"
    explanation: ClinGen dosage sensitivity supports PTCH1 haploinsufficiency as a disease mechanism.
```

ClinGen dosage cache bodies contain a `## Gene dosage sensitivity` table and,
when available, report-page narrative for haploinsufficiency and
triplosensitivity evidence.

**Citing an ICEES KG comorbidity pair:**

ICEES (Integrated Clinical and Environmental Exposures Service, RENCI/UNC) is
the EHR sibling of COHD: it exposes chi-square disease-disease co-occurrence
from single-site UNC Health EHR data, but its nodes are already MONDO/HP-coded.
The `ICEES:` prefix is the structured-source counterpart of the live COHD API
(`scripts/cohd_pair_to_signal.py`) — use ICEES when you want to **quote a cohort
statistic as a snippet-validated evidence row**, and use the COHD script when
you want hospital-wide co-occurrence metrics generated on the fly. A pair id is
`ICEES:<A>__<B>` with the two disease/phenotype CURIEs sorted and `:` → `_`:

```yaml
association_signals:
- source: ICEES
  method: EHR_COHORT_ASSOCIATION
  signal_disorder_a_id: MONDO:0004979
  signal_disorder_b_id: MONDO:0005002
  population: >-
    ICEES KG 8-20-2024, UNC Health primary-ciliary-dyskinesia cohort
    (condition-specific base population), chi-square contingency.
  statistics:
    metrics:
    - metric_type: CHI_SQUARE
      metric_value: 168.58533016733276
      p_value: 1.5071340388291068e-38
      notes: ICEES PCD 2016 cohort co-occurrence of asthma and COPD.
  evidence:
  - reference: ICEES:MONDO_0004979__MONDO_0005002
    supports: SUPPORT
    evidence_source: OTHER
    snippet: "PCD_UNC_patient_2016_v6_binned_deidentified | 168.58533016733276 | 1 | 1.5071340388291068e-38 | 5688"
    explanation: ICEES EHR cohort shows significant asthma-COPD co-occurrence.
```

Each `## Cohort statistics` row (`| cohort | chi-square | dof | p-value | N |`)
is a stable quotable substring. **Interpretation caveats:** ICEES cohorts are
*condition-specific* patient sets (asthma, PCD), so a statistic is conditioned
on that base population — not hospital-wide like COHD; and the chi-square values
are **not multiple-testing corrected** and are inflated by very large cohort N,
so apply the same FDR skepticism used for COHD signals.

**How the cache is built:**

```bash
# 1. Refresh the bulk XML pinned in data/orphadata/MANIFEST.yaml
just refresh-orphadata

# 2. Rebuild every references_cache/ORPHA_*.md
just structured-rebuild-orphanet

# Or rebuild a single ID
just structured-rebuild-orphanet --id 558

# ClinGen Gene-Disease Validity CSV
just clingen-refresh
just clingen-list
just clingen-rebuild
just clingen-rebuild --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# Use --csv-only to skip fetching report-page narrative during a fast rebuild
just clingen-rebuild --csv-only --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# ClinGen Dosage Sensitivity CSV/TSV
just clingen-dosage-refresh
just clingen-dosage-list
just clingen-dosage-rebuild
just clingen-dosage-rebuild --id CGDS:HGNC_9585

# ICEES KG (pinned by data/icees-kg/MANIFEST.yaml; emits MONDO/HP disease pairs)
just icees-refresh
just icees-list
just icees-rebuild
just icees-rebuild --id MONDO:0004979,MONDO:0005002
```

`data/orphadata/*.xml` is gitignored; `data/orphadata/MANIFEST.yaml` is
committed and pins the snapshot date + sha256 of each bulk file. To verify
no drift has occurred, run `just structured-rebuild-orphanet` locally and
check `git diff references_cache/ORPHA_*.md`. (A CI workflow that does this
automatically is a worthwhile follow-up but does not yet exist.)

**When a refresh fails on a checksum mismatch, repin — don't hand-edit.**

These manifests pin a sha256 against an **unversioned** upstream URL:
`https://www.orphadata.com/data/xml/en_product1.xml` is always the *current*
Orphanet release, not a versioned artifact. So the pin is guaranteed to stop
matching the next time upstream publishes, and the refresh hard-fails until
somebody re-pins it. That is ordinary release drift, not a corrupt download —
and it recurred four times in one week (#9687, #9897, #10150 for Orphadata,
#10081 for ClinGen) because the only recovery was a manual download-and-edit.

```bash
just refresh-orphadata            # strict: fails on drift, naming the remedy
just refresh-orphadata --repin    # accept the new release, rewrite the manifest
just clingen-refresh --repin
```

`--repin` downloads, records the new sha256, size and `snapshot_date` in the
manifest, and stops — leaving a diff of exactly those lines for you to review.
It is never implicit: the default still refuses, because a source changing under
a curator is precisely what the pin exists to catch. After repinning, rebuild the
cache and review that diff too:

```bash
just refresh-orphadata --repin && just structured-rebuild-orphanet
git diff data/orphadata/MANIFEST.yaml references_cache/ORPHA_*.md
```

Commit the manifest bump together with the cache diff it produced, so the change
in pinned release and the change in cached content are reviewable as one unit.

**Adding a new structured source:**

The framework is in `src/dismech/structured_sources/`. To add a new source
(OMIM, MONDO, HGNC, …):

1. Subclass `StructuredSource` (`base.py`) and implement `build_index`,
   `identifiers`, `serialize`.
2. Pin bulk-data files in `data/<source>/MANIFEST.yaml`.
3. Register a CLI entry in `src/dismech/structured_sources/cli.py`.
4. Use the same UniProt-flat-file-style line layout — fixed column widths,
   sorted within each tag block — so curator-quoted snippets remain valid
   across refreshes.

**Agent guardrail:** Like literature cache files, `references_cache/ORPHA_*.md`
must NEVER be hand-edited. Regenerate via `just structured-rebuild-orphanet`.
