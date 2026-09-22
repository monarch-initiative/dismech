# Hypothesis-based phenotype algorithms

### Hypothesis-Based Phenotype Algorithms

A `definitions[]` entry with `definition_type: PHENOTYPE_ALGORITHM` may be a
**computable EHR/OMOP case-finding query predicated on an unproven mechanism**
(e.g. scan for a new arrhythmia/seizure shortly after a fever to surface latent
CACNA1C carriers), not just a consensus/OHDSI-validated phenotype. Mark the
epistemic grounding so the two are never conflated (issue #6245):

- **`derivation_basis`** (`DefinitionDerivationBasisEnum`): `ESTABLISHED_CRITERIA`
  (default — consensus/validated), `MECHANISTIC_HYPOTHESIS` (predicated on an
  unproven mechanism), or `MODEL_SYSTEM_EXTRAPOLATION` (from an animal/in-vitro
  result not yet shown in humans).
- **`attaches_to`** (reused slot, `pathophysiology#<node>` grammar): for a
  `MECHANISTIC_HYPOTHESIS` definition, link the pathograph node(s)/edge(s) it is
  predicated on. The hypothesis basis is then inferred from those edges'
  `hypothesis_groups` → `mechanistic_hypotheses[].status` — do **not** add a
  standalone hypothesis id on the definition. A test
  (`check_hypothesis_based_definition_attaches_to_foreign_keys`) requires these
  refs to resolve.
- **`validation_status`** (`AlgorithmValidationStatus` object): `status`
  (`PROPOSED` / `UNVALIDATED` / `VALIDATED_AGAINST_GOLD_STANDARD`) + free-text
  `rationale` + optional `evidence` (standard EvidenceItem — PMID + verified
  snippet — e.g. the validation study reporting the query's PPV).

The trigger pathophysiology node itself is modeled normally (a node whose
`downstream` edges opt into `hypothesis_groups: [<id>]`) plus a disease-level
`mechanistic_hypotheses` entry (usually `status: EMERGING`). Two paired worked
examples span the spectrum: `Timothy_Syndrome` (`fever_exacerbated_cav1.2`;
`MECHANISTIC_HYPOTHESIS`/`PROPOSED`, zebrafish) and `Brugada_Syndrome`
(fever-unmasking of the type-1 ECG; `ESTABLISHED_CRITERIA`/`UNVALIDATED`, an
established-mechanism definition that still `attaches_to` its fever node). See
[`docs/hypothesis-based-phenotype-algorithms.md`](../../../../docs/hypothesis-based-phenotype-algorithms.md)
and the candidate register in
[`docs/reports/hypothesis-driven-ehr-case-finding-2026-07-12.md`](../../../../docs/reports/hypothesis-driven-ehr-case-finding-2026-07-12.md).
