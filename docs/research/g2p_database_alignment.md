# G2P Database Alignment Against dismech

## Scope

This note covers how a Gene2Phenotype (G2P) row should be interpreted against
dismech's disease-centric model, using PTEN as the worked example and then
generalizing into a reusable audit workflow.

The immediate question is not "does one dismech disease file explain one G2P
row?" but "does the set of dismech disease entries for a gene explain the set
of G2P assertions for that gene?"

## Sources consulted

- G2P curation paper:
  https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-024-01398-1
- G2P FTP README:
  https://ftp.ebi.ac.uk/pub/databases/gene2phenotype/README
- G2P download format:
  https://ftp.ebi.ac.uk/pub/databases/gene2phenotype/G2P_data_downloads/Data_download_format_202511.txt
- Current G2P release used for the PTEN snapshot:
  `https://ftp.ebi.ac.uk/pub/databases/gene2phenotype/G2P_data_downloads/2026_03_28/allG2P_2026-03-28.csv.gz`

## Working model

G2P is row-centric. Each row is effectively a compact gene-to-disease assertion
bundle with:

- locus/gene identity
- disease label and optional MONDO/OMIM mapping
- allelic requirement
- confidence
- variant consequence and variant type constraints
- molecular mechanism and mechanism support
- HPO phenotype set
- reviewed publications

dismech is disease-centric. The equivalent information is distributed across a
disease file:

- `disease_term` for disease identity
- `genetic[]` for gene association, inheritance, variant notes, and evidence
- `pathophysiology[]` for mechanism nodes and evidence
- `phenotypes[]` for selected HPO-linked manifestations
- `evidence.reference` items spread across the disease file rather than bundled
  as a single row-level citation set

The main implication is that a G2P row can only be checked against dismech by
crosswalking one row into multiple disease-file sections, and a gene must be
audited across all relevant disease entries, not just one disease file.

## PTEN Snapshot

Command used:

```bash
uv run python -m dismech.g2p_gene_audit PTEN --format summary
```

Current G2P PTEN rows in the 2026-03-28 `allG2P` release:

| G2P ID | Disease name | MONDO | Reviewed PMIDs |
| --- | --- | --- | ---: |
| G2P00413 | PTEN-related hamartoma tumour syndrome (Cowden syndrome) | MONDO:0008021 | 17 |
| G2P01201 | PTEN-related Proteus syndrome | MONDO:0008021 | 3 |
| G2P02322 | PTEN-related Lhermitte-Duclos disease | MONDO:0008021 | 18 |

Important PTEN finding: all three current G2P PTEN rows reuse the same MONDO
identifier (`MONDO:0008021`) despite having different disease names. In other
words, exact MONDO matching is not sufficient as a primary join key for this
gene.

Current dismech PTEN matches from structured `genetic[]` slots:

| Match class | dismech disease | Notes |
| --- | --- | --- |
| Causative | `Cowden_Syndrome.yaml` | Direct PTEN disease anchor |
| Subtype-specific | `Juvenile_Polyposis_Syndrome.yaml` | PTEN-BMPR1A contiguous deletion partner |
| Secondary genetic | 6 cancer entries | Somatic/co-occurring/non-primary PTEN involvement |

Additional PTEN-related content exists in dismech but not as a direct PTEN
genetic anchor:

- [`Cowden_Syndrome.yaml`](/Users/cjm/worktrees/dismech-g2p-db/kb/disorders/Cowden_Syndrome.yaml)
  models Lhermitte-Duclos disease as a phenotype, not a separate PTEN disease file.
- [`Proteus_syndrome.yaml`](/Users/cjm/worktrees/dismech-g2p-db/kb/disorders/Proteus_syndrome.yaml)
  carries PTEN hamartoma tumor syndrome as a differential diagnosis, not as the
  primary genetic disease entity for that file.

This means PTEN is partly represented in dismech as:

- a direct disease root for Cowden syndrome
- a subtype modifier in juvenile polyposis of infancy
- a differential/spectrum mention in Proteus syndrome
- secondary somatic biology in multiple cancers

That is a useful disease-centric representation, but it is not yet a clean
one-row-per-G2P-assertion crosswalk.

## PTEN Coverage Findings

### Disease identity

- G2P `G2P00413` is best matched to [`Cowden_Syndrome.yaml`](/Users/cjm/worktrees/dismech-g2p-db/kb/disorders/Cowden_Syndrome.yaml)
  by disease name alias, not by exact MONDO.
- dismech's Cowden root uses `MONDO:0016063`.
- G2P PTEN rows use `MONDO:0008021`.
- The repo itself contains both identifiers in PTEN-related contexts, so MONDO
  normalization is currently a real audit issue, not a theoretical one.

### PMID coverage

For PTEN across all three current G2P rows:

- reviewed G2P PMIDs: 21
- dismech PMIDs from direct PTEN genetic anchors only: 2
  `21194675`, `33822054`
- dismech PMIDs from all direct-anchor disease files: 26
- PMID overlap between G2P reviewed PTEN PMIDs and direct dismech PTEN anchors: 0

For the PTEN/Cowden row alone (`G2P00413`):

- G2P reviewed PMIDs: 17
- all PMIDs in [`Cowden_Syndrome.yaml`](/Users/cjm/worktrees/dismech-g2p-db/kb/disorders/Cowden_Syndrome.yaml): 13
- overlap: 0

Interpretation:

- dismech currently explains the Cowden/PTEN biology conceptually, but not using
  the same publication bundle curated into G2P
- PMID coverage must therefore be measured separately from disease/mechanism
  coverage
- a disease can be "explained" in dismech while still having poor publication
  overlap with G2P

### Phenotype coverage

For `G2P00413`:

- G2P HPO terms: 84
- top-level dismech Cowden phenotypes: 7
- exact HPO overlap: 6

This is not necessarily a defect. It shows a structural difference:

- G2P stores broad phenotype enumerations for the assertion
- dismech stores a smaller explanatory phenotype subset tied to disease
  mechanism and clinical salience

### Mechanism alignment

PTEN is one of the better mechanism-alignment examples.

G2P says:

- monoallelic autosomal requirement
- LOF mechanism
- variant consequence: absent gene product / altered gene product structure
- variant types: truncating, missense, splice, regulatory, deletion
- mechanism evidence: biochemical/protein expression plus functional alteration
  and model support

dismech Cowden says:

- `genetic[].inheritance` contains autosomal dominant inheritance
- `genetic[].notes` explicitly describe germline PTEN loss-of-function variants
- `pathophysiology[]` models PTEN loss -> PI3K/AKT/mTOR activation -> hamartoma
  formation -> increased cancer risk
- evidence is attached to the genetic and pathophysiology claims separately

So the biology aligns well, but the packaging differs.

## Where dismech Aligns Well

- Disease-level modeling is strong when a gene has a well-curated disease root,
  as in [`Cowden_Syndrome.yaml`](/Users/cjm/worktrees/dismech-g2p-db/kb/disorders/Cowden_Syndrome.yaml).
- `genetic[]` maps reasonably well to G2P's disease-gene assertion, especially
  for causative genes and inheritance.
- `pathophysiology[]` is richer than G2P's single mechanism field and can often
  explain the mechanism in a more causal way.
- `phenotypes[]` with HPO mappings align cleanly when dismech has chosen to
  represent a phenotype explicitly.
- `evidence_source` in dismech supports some of the same evidence-type ideas
  that G2P encodes in molecular mechanism evidence.

## Where dismech Aligns Poorly

- There is no first-class row-level gene assertion object equivalent to a G2P row.
- PMIDs are distributed across disease sections, not bundled as "the citation set
  for the PTEN-Cowden assertion".
- A gene can appear in dismech as:
  causative, subtype-specific, secondary somatic, mechanistic, or differential.
  A naive gene search overcounts disease coverage.
- Disease identifiers are not stable enough for a MONDO-only join in the PTEN
  case.
- G2P phenotype breadth is often much larger than dismech's curated phenotype
  subset.
- dismech mechanism nodes do not always populate structured `gene`/`genes`
  fields, even when the node is obviously gene-specific by name.
- G2P's compact mechanism support fields
  (`molecular mechanism support`, `categorisation`, `evidence`) do not have a
  single direct home in dismech.

## Proposed Crosswalk Strategy

### 1. Treat each G2P row as an assertion bundle

For audit purposes, normalize each row into:

- gene symbol / HGNC ID
- disease label / MONDO / OMIM
- allelic requirement
- confidence
- variant consequence
- variant types
- molecular mechanism fields
- phenotype set
- reviewed PMIDs

### 2. Match into dismech by ordered evidence, not a single key

Use this order:

1. Exact disease MONDO match
2. Disease label or parenthetical alias match
3. Structured `genetic[]` match for the same gene
4. Structured subtype-specific match for the same gene
5. Heuristic spectrum/differential embedding

Important rule:

- keep direct disease anchors separate from secondary somatic or co-occurring
  gene mentions

### 3. Separate match classes

For every gene, classify dismech hits as:

- direct genetic anchor
  example: PTEN in Cowden syndrome
- subtype-specific genetic anchor
  example: PTEN-BMPR1A in juvenile polyposis of infancy
- secondary genetic mention
  example: PTEN loss in metastatic melanoma
- spectrum/differential embedding
  example: PTEN hamartoma tumor syndrome under Proteus differentials

Only the first two classes should count toward primary disease coverage.

### 4. Measure PMID coverage at two levels

For each gene, compute:

- G2P reviewed PMIDs
- dismech PMIDs from matched gene-specific sections only
- dismech PMIDs from the full matched disease files

This gives two answers:

- publication overlap for the exact gene assertion
- publication overlap for the broader disease explanation

### 5. Score mechanism alignment separately from PMID overlap

Per G2P row, grade:

- disease identity alignment
- inheritance alignment
- variant-type alignment
- molecular mechanism alignment
- phenotype-set alignment
- PMID overlap

A row can have:

- strong mechanism alignment with poor PMID overlap
- strong disease identity alignment with incomplete phenotype coverage
- weak disease identity alignment but strong spectrum embedding

### 6. Produce a compact audit artifact

Recommended table columns:

- gene
- g2p_id
- g2p_disease_name
- g2p_disease_mondo
- g2p_confidence
- g2p_mechanism
- g2p_reviewed_pmid_count
- dismech_match_class
- dismech_file
- dismech_disease_name
- dismech_disease_mondo
- dismech_gene_association
- dismech_gene_section_pmid_count
- dismech_disease_pmid_count
- pmid_overlap_count
- mechanism_alignment
- phenotype_alignment
- audit_note

## Script Scaffold

Added module:

- [`src/dismech/g2p_gene_audit.py`](/Users/cjm/worktrees/dismech-g2p-db/src/dismech/g2p_gene_audit.py)

Focused tests:

- [`tests/test_g2p_gene_audit.py`](/Users/cjm/worktrees/dismech-g2p-db/tests/test_g2p_gene_audit.py)

Usage:

```bash
uv run python -m dismech.g2p_gene_audit PTEN --format summary
uv run python -m dismech.g2p_gene_audit PTEN --format json
```

Behavior:

- defaults to the latest official `allG2P` FTP release
- uses structured `genetic[]` and `pathophysiology[].gene/genes` matches in dismech
- distinguishes causative/subtype-specific matches from secondary genetic matches
- reports G2P MONDO collisions within a gene
- reports PMID overlap for direct anchors and for all matched disorders

Current limitation:

- it does not yet count differential-diagnosis embeddings or unstructured gene
  mentions inside pathophysiology node names/descriptions

## Recommended Next Steps

- Add an explicit gene-assertion audit artifact to dismech outputs rather than
  deriving it ad hoc from disease YAML files.
- Normalize PTEN-related MONDO usage before relying on exact MONDO joins.
- Add structured `gene`/`genes` values to gene-specific pathophysiology nodes
  such as the PTEN loss node in Cowden syndrome.
- Decide whether PTEN-related Proteus syndrome and PTEN-related
  Lhermitte-Duclos disease should become first-class disease files or remain
  phenotype/spectrum embeddings.
- If G2P alignment becomes a recurring workflow, add a curated alias table for
  disease-spectrum names that are not safe to resolve by naive string matching.
