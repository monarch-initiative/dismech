# Coverage audit: discriminating accessible nodes in the pathograph

**Question.** For a disease with no accessible confirmatory test, does its
dismech pathograph contain at least one node that (a) could be measured in an
accessible specimen and (b) appears in none of its differential diagnoses'
pathographs? Such a node is what the retrodiction task would need: something
the KB could point to as a candidate test that separates the disease from the
conditions it is confused with.

**Answer, in short.** Mostly not, and the KB can rarely tell. Of 2,554 diseases
audited, 42 (1.6%) have such a node by the audit's rules, two of them
spurious. For 2,319 (91%) the pathograph contains no node measurable in an
accessible specimen at all. Most of the rest list no differential diagnoses, so
the comparison cannot be made. None of the six negatives has a node the audit can
confirm as discriminating.

Regenerate with
`uv run python experiments/diagnostic_retrodiction/coverage_audit/audit.py`,
which writes `../coverage.tsv` (one row per disease).

## Which diseases

- **Negatives** (`negatives.tsv`, 6): hypermobile EDS, Kawasaki disease,
  sarcoidosis, Behçet's disease, CRPS type 1, Takayasu arteritis.
- **Frame entries without an accessible test** (2,548): every `frame.tsv`
  entry with no row where `flag_nongenetic_specimen` is TRUE. This is the
  frame's own definition of an accessible, non-germline test. An entry
  diagnosed by germline sequencing is therefore in this set, since the
  experiment excludes germline tests.

The KB is read at `PINNED_COMMIT` (`2a931df2ac7`), the tree the frame was built
from. All 2,554 entries resolved to a file at that commit.

## Definitions

These are fixed in `audit.py` and were not tuned per disease.

- **Nodes.** `dismech.graph.iter_graph_node_rows`, restricted to
  pathophysiology, phenotype, biochemical and genetic nodes. Treatments,
  exposures and model nodes do not describe a measurable state of the patient.
- **Measurable in an accessible specimen.** The node passes the test that set
  `flag_nongenetic_specimen` in the frame (`census.classify`). That test is
  applied to the node's name plus the labels of its own identity terms:
  phenotype, biomarker, LOINC, gene and chemical-entity bindings. Three
  restrictions came out of reading the first runs:
  - **No description or context terms.** Description prose and context terms
    (cell types, processes, locations) are not read. With them, every immune
    node whose cell type is a leukocyte, and every node mentioning a blood
    vessel, resolved to blood.
  - **Masked phrases.** Phrases in which a specimen word names no specimen
    are masked first: blood pressure, blood vessel, blood-*x* barrier,
    plasma membrane, urinary tract, urinary symptoms, CSF outflow, and
    tissue infiltration.
  - **Inferred specimens for phenotype and biochemical nodes only.** Census's
    analyte-class inference ("an enzyme activity is assayed in blood") is
    accepted only for those two node types. A pathophysiology node must state
    its specimen, because otherwise "CDK4/6 kinase activity" counted as a
    blood test.
- **Differentials.** Each `differential_diagnoses[]` item is matched to a kb
  entry by its MONDO term, or failing that by exact entry name. Unmatched
  items are listed in `unresolved_differentials` and cannot be compared.
- **Appears in a differential.** The primary (STRICT) rule counts a match on
  either of two things: the same normalised node name in a matched
  differential, or a shared identity-term CURIE. NAME_ONLY uses names alone
  and is reported in `status_name_only`.

## Results

| Status | Negatives | Frame entries | Meaning |
|---|---|---|---|
| NO_MEASURABLE_NODE | 3 | 2,316 | no node measurable in an accessible specimen |
| NO_DIFFERENTIALS | 3 | 154 | measurable nodes, but no differential listed |
| NO_RESOLVED_DIFFERENTIALS | 0 | 27 | differentials listed, none is a kb entry |
| NO_UNIQUE_NODE | 0 | 9 | every measurable node also appears in a differential |
| HAS_UNIQUE_NODE | 0 | 42 | at least one measurable node absent from all matched differentials |

Under NAME_ONLY, 46 entries are HAS_UNIQUE_NODE and 5 are NO_UNIQUE_NODE. The
four that move are cases where the differential carries the same term under a
different node name.

Two underlying coverage figures for the 2,548 frame entries:
- 232 have any measurable node.
- 1,035 list any differential.

### The negatives

| Disease | Measurable nodes | Differentials | Status |
|---|---|---|---|
| Hypermobile EDS | none | none | NO_MEASURABLE_NODE |
| Behçet's disease | none | none | NO_MEASURABLE_NODE |
| CRPS type 1 | none | CRPS type 2 (no kb entry) | NO_MEASURABLE_NODE |
| Kawasaki disease | leukocytosis; ESR; platelet count | none | NO_DIFFERENTIALS |
| Sarcoidosis | leukopenia | none | NO_DIFFERENTIALS |
| Takayasu arteritis | ESR | none | NO_DIFFERENTIALS |

- **No differentials recorded.** Five of the six list no differential
  diagnoses, at the pinned commit or on the current branch.
- **Only nonspecific readouts.** Where measurable nodes exist, they are
  inflammation or blood counts that no clinician would treat as
  discriminating.
- **CRPS type 1's one candidate.** It had a single candidate node, an
  autoantibody against autonomic receptors. It passed only through
  census's analyte-class inference, which this audit does not accept for
  pathophysiology nodes. Its one differential has no kb entry, so it
  could not have been compared anyway.
- **Flagged frame rows.** Kawasaki, sarcoidosis, Takayasu and CRPS-1 carry
  flagged frame rows: ESR, platelet count, ACE, soluble IL-2 receptor. These
  are accessible but not confirmatory, which is why the diseases are
  negatives.
- **A frame misclassification.** CRPS-1's flagged row is three-phase bone
  scintigraphy, labelled BLOOD in the frame. That label is wrong.

### What the 42 "unique" nodes are

I read every HAS_UNIQUE_NODE row.
- **Spurious (2).** Choroid plexus neoplasm's node is CSF *overproduction*,
  which no assay measures. Microcephaly-capillary malformation syndrome's
  nodes are "serum-insensitive" signalling and extra-axial CSF seen on
  imaging.
- **Real but nonspecific.** The remaining 40 name a real blood, urine or CSF
  readout, but most are nonspecific: elevated creatine kinase (8 entries),
  IgE, lymphopenia or leukopenia, ESR, immunoglobulin levels, vaccine
  antibody responses.
- **Why they count as unique.** They are unique only because the
  differentials' pathographs do not record them. Elevated CK is shared by
  nearly every myopathy, and the 7 NO_UNIQUE_NODE myopathy and neuropathy
  entries are exactly the ones whose differential happens to record CK too.
- **Plausibly specific (a handful):**
  - erythrocyte adenosine deaminase in bone marrow failure syndrome 4;
  - erythrocyte 2,3-DPG and phosphofructokinase in glycogen storage disease VII;
  - urinary VMA in melanotic neuroectodermal tumour of infancy;
  - CSF homovanillic acid in CDK8-related disorder;
  - acanthocyte membrane remodelling in chorea-acanthocytosis.

So "absent from every differential's pathograph" measures what the KB records,
not what discriminates. A node passes when the differential's entry is silent
about it, which says nothing about whether the analyte differs between the
two diseases.

## Limitations

- **Regex heuristics.** "Measurable" relies on census's specimen regexes and a
  hand-written mask list. Each fix in the definitions section removed a class
  of false positive found by reading output; two known spurious rows remain.
  It will also miss measurable nodes whose names do not mention a specimen or
  analyte class, for example "hyperammonaemia" bound to an HP term.
- **Literal matching.** Matching is by node name and identity CURIE. Two
  entries describing the same analyte under different names and unrelated
  terms count as different nodes, which inflates HAS_UNIQUE_NODE.
- **Differentials as recorded.** Only differentials the entry records and
  that resolve to a kb entry are compared. 154 entries with measurable nodes
  list no differential, and 27 list only differentials that have no kb entry.
- **Germline-tested entries included.** The frame-derived set includes every
  entry whose only accessible test is germline sequencing. For those,
  "lacking an accessible confirmatory test" is a property of the experiment's
  scope, not of the disease.
