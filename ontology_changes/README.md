# Ontology change proposals

This registry records precise proposed edits to external ontologies before a
ticket exists, and tracks what happens after filing. Each independently
reviewable edit has one `ontology_changes/<id>.yaml` record. Its stable `id`
matches the filename. The owning ontology can be MONDO or another resource.

The first record is
[`mondo-0019503-icd11-anterior-segment-broad-match.yaml`](mondo-0019503-icd11-anterior-segment-broad-match.yaml).
It proposes changing one MONDO xref qualifier, while retaining the xref and
its other provenance. It is **not filed upstream**. Current MONDO was checked
on 2026-11-25; WHO scope evidence comes from the separately dated 2026-01
Foundation snapshot captured on 2026-09-21 UTC.

## Boomer pilot follow-through

The registry now covers four investigated cases, with six atomic mapping edits.
The Gorlin and PRAAS moves each have a structured change set linking two edits:
remove the misplaced family xref and add it to the existing subtype. These are backfilled, applied requests,
not newly discovered corrections. MONDO and DO source snapshots and the three
upstream request states were checked on 2026-11-25 (America/Los_Angeles;
2026-11-26 UTC). The snapshots retain both timestamps.

| Case | Structured edits | Request state | Local adoption |
|---|---|---|---|
| Gorlin syndrome | [Move the PTCH1-specific DO mapping from family to subtype](change_sets/mondo-gorlin-ptch1-mapping-move.yaml) | Both edits ACCEPTED; [MONDO #10628](https://github.com/monarch-initiative/mondo/pull/10628) merged and verified in current source | No DisMech mapping migration needed |
| PRAAS | [Move the PRAAS1 DO mapping from family to subtype](change_sets/mondo-praas1-mapping-move.yaml) | Both edits ACCEPTED; [MONDO #10629](https://github.com/monarch-initiative/mondo/pull/10629) merged and verified in current source | No DisMech mapping migration needed |
| TPMT deficiency | [Qualify the poor-thiopurine-metabolism family as broader](mondo-0012503-thiopurine-family-broad-match.yaml) | ACKNOWLEDGED; [MONDO #10630](https://github.com/monarch-initiative/mondo/pull/10630) approved but still open, source unchanged | No DisMech mapping migration needed |
| Anterior segment dysgenesis (FOXE3 investigation) | [Qualify the structural-anomaly ICD-11 category as broader](mondo-0019503-icd11-anterior-segment-broad-match.yaml) | NOT_FILED | No DisMech mapping migration needed |

TPMT's review asks whether the DO family matches MONDO's thiopurine metabolic
disease and whether obsolete NUDT15 deficiency should be reinstated. The current
snapshot confirms that the NUDT15 term is still obsolete. Those questions remain
open; approval does not establish that the qualifier edit has been applied.

Waldenström remains a scope investigation, with no adjudicated ontology edit.
Its sensitivity experiment is not promoted into a removal request. Historical
Boomer inputs and scores remain frozen; later source captures must distinguish
the applied Gorlin/PRAAS changes from the simulated TPMT/FOXE3 repairs.

The mapping records identify the biological edits. Their linked upstream PRs
also document associated subset/synonym provenance cleanup, which these edit
types do not encode. They are not complete executable ontology patches.

The accepted moves do not resolve every subtype annotation on the families.
Current MONDO still cites DOID:0070365 on a Gorlin family inheritance edge and
DOID:0050553 on a PRAAS family inheritance edge. The PRAAS family also retains
the EXACT synonyms "JMP syndrome" and "Nakajo-Nishimura syndrome", with PRAAS1
DOID provenance. These residual annotations need separate scope review; no
synonym-scope or inheritance-edge correction is claimed by these records.

## Validate, query and export

From the repository root:

```bash
just validate-ontology-changes
just ontology-changes list --ontology MONDO --request-status NOT_FILED
just ontology-changes list --affected-record kb/disorders/FOXE3_Anterior_Segment_Dysgenesis.yaml
just ontology-changes export mondo-0019503-icd11-anterior-segment-broad-match
just ontology-changes list-change-sets
just ontology-changes list --change-set mondo-gorlin-ptch1-mapping-move
just ontology-changes export mondo-gorlin-ptch1-mapping-move
just ontology-changes refresh-change-set-views
```

`list` returns complete JSON records; `export` writes a Markdown request to
stdout for review. Both validate the registry first. Neither publishes a
ticket, changes a mapping, or applies a KGCL patch. The validator checks the
LinkML schema, type-specific fields, lifecycle combinations, unique IDs,
evidence-source references, exact supporting excerpts, local paths and artifact
SHA-256 checksums. CI
runs it on every PR, including proposals-only edits.

`list-change-sets` returns the grouping records as JSON. `list --change-set`
returns their atomic members and can be combined with the existing filters.
`export` accepts a change-set ID or any member ID: all produce the
same complete change set, with a before/after table and the full evidence and status
of all member edits. Standalone proposals still export individually. Any invalid
proposal or change set prevents listing/exporting an apparently valid subset.

Use `affected_records` to link diseases, groupings and analyses to a proposal.
The reverse query above gives the proposals for an entry without duplicating
their lifecycle state inside disease YAML. Existing `tracked_issues` remains
the place for links to filed tickets. `history/` records curation sessions;
this registry records the edits being requested. No change to the Disease
schema is required.

## Mapping changes as change sets

A removal has no `new_value`: its result is absence of that mapping. A creation
has no `old_value`: the mapping did not previously exist at that subject. To
represent their combined intent, add a record under `change_sets/`:

```yaml
id: mondo-gorlin-ptch1-mapping-move
title: Move the PTCH1-specific DO mapping from the Gorlin family to basal cell nevus syndrome 1
change_set_type: MAPPING_MOVE
justification: 'Gorlin syndrome is a family containing PTCH1-related and SUFU-related subtypes. DOID:0070365
  is explicitly PTCH1-related and shares OMIM:109400 with MONDO:0958174; DOID:2512 covers the broader
  family. The saved Boomer analysis has two equally weighted best solutions that exchange the family-to-subtype
  and family-to-family DO mappings. That tie identifies a scope conflict; source definitions, rather than
  the solver score, justify retaining the family mapping to DOID:2512 and moving DOID:0070365 to MONDO:0958174.
  The pinned before/current MONDO stanzas document the move applied in MONDO PR #10628. This record covers
  the mapping assertions, not all annotation cleanup: the checked family stanza still cites the subtype
  DOID on an inheritance edge, which requires separate review.'
ontology: MONDO
mapping_representation: MONDO_XREF_QUALIFIER
before:
- subject:
    id: MONDO:0007187
    label: nevoid basal cell carcinoma syndrome
  predicate: MONDO:equivalentTo
  object:
    id: DOID:0070365
    label: nevoid basal cell carcinoma syndrome 1
after:
- subject:
    id: MONDO:0958174
    label: basal cell nevus syndrome 1
  predicate: MONDO:equivalentTo
  object:
    id: DOID:0070365
    label: nevoid basal cell carcinoma syndrome 1
analysis_links:
- https://github.com/monarch-initiative/dismech/blob/main/analyses/boomer/remaining-low-confidence/Gorlin_Syndrome-alternatives.md
source_links:
- https://raw.githubusercontent.com/monarch-initiative/mondo/f1526eeae184f43741ca73ae0050d16f0061fd37/src/ontology/mondo-edit.obo
- https://raw.githubusercontent.com/monarch-initiative/mondo/d3bdb9d318f3913c41068660eb30682a7b193e28/src/ontology/mondo-edit.obo
- https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/fe7ad5dc278f47c9c133964892ca7ad80e5321b1/src/ontology/doid.obo
- https://github.com/monarch-initiative/mondo/pull/10628
upstream_requests:
- https://github.com/monarch-initiative/mondo/pull/10628
member_statuses:
- proposal_id: mondo-0007187-gorlin-remove-subtype-doid
  record_url: https://github.com/monarch-initiative/dismech/blob/main/ontology_changes/mondo-0007187-gorlin-remove-subtype-doid.yaml
  origin: SELF_PROPOSED
  confidence: HIGH
  request_status: ACCEPTED
  adoption_status: NOT_APPLICABLE
  adoption_notes: The DisMech entry already uses the family MONDO term; no asserted DisMech mapping to
    the misplaced DO subtype needs migration. The saved before/after Boomer experiment is a controlled
    source intervention, not a live source refresh. Preserve historical inputs and use corrected upstream
    mappings for future captures.
  ontology_state_verified: '2026-11-25'
- proposal_id: mondo-0958174-gorlin-add-subtype-doid
  record_url: https://github.com/monarch-initiative/dismech/blob/main/ontology_changes/mondo-0958174-gorlin-add-subtype-doid.yaml
  origin: SELF_PROPOSED
  confidence: HIGH
  request_status: ACCEPTED
  adoption_status: NOT_APPLICABLE
  adoption_notes: The DisMech entry already uses the family MONDO term; no asserted DisMech mapping to
    the misplaced DO subtype needs migration. The saved before/after Boomer experiment is a controlled
    source intervention, not a live source refresh. Preserve historical inputs and use corrected upstream
    mappings for future captures.
  ontology_state_verified: '2026-11-25'
affected_records:
- kb/disorders/Gorlin_Syndrome.yaml
- analyses/boomer/remaining-low-confidence/Gorlin_Syndrome-alternatives.md
- kb/disorders/PTCH1-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml
see_also:
- https://github.com/monarch-initiative/dismech/pull/18681
changes:
- mondo-0007187-gorlin-remove-subtype-doid
- mondo-0958174-gorlin-add-subtype-doid
```

`changes` references stable proposal IDs, not filenames or URLs. Every member
must be a `REMOVE_MAPPING`, `MAPPING_CREATION` or `MAPPING_PREDICATE_CHANGE`
proposal. All members share the owning ontology and source representation.
IDs must be unique, resolve to valid records, and belong to at most one set.
Mixed legacy/new membership, missing members and duplicate YAML keys fail
validation. Existing registries without change sets remain valid.

`MAPPING_RESTRUCTURE` supports N-to-M changes. `MAPPING_MOVE` is its constrained
one-for-one case: exactly one removal and one creation, with the same target ID
and predicate/qualifier and two distinct subject IDs. Do not split a coordinated
collapse into artificial pairwise moves.

`before` and `after` are lists of withdrawn and introduced assertions. They are
the **changed portion** of the mapping graph, not full ontology snapshots. A
predicate change contributes its old assertion to `before` and its new assertion
to `after`; a pure addition has `before: []`, and a pure removal has `after: []`.
Unchanged mappings remain in the ontology and can be explained in the rationale.
For `MONDO_XREF_QUALIFIER`, `predicate` is the xref qualifier, not an OWL edge.
These views describe the edit, not its current application status.

The list is a simultaneous delta, not an ordered program. Duplicate assertions
on either side, or an assertion both removed and added, are rejected even if the
proposal IDs differ. Resolve a sequential repair into its net edit before recording
it as one set. Assertion order follows member order for display; it does not pair
items by position or imply an execution sequence.

### Example: two mappings collapse into one

This is a synthetic example of the representation, not a proposed ontology edit:

```yaml
change_set_type: MAPPING_RESTRUCTURE
changes:
- example-remove-a
- example-remove-b
- example-add-c
before:
- subject: {id: 'EXAMPLE:A', label: Synthetic A}
  predicate: skos:exactMatch
  object: {id: 'EXAMPLE:X', label: Synthetic X}
- subject: {id: 'EXAMPLE:B', label: Synthetic B}
  predicate: skos:exactMatch
  object: {id: 'EXAMPLE:X', label: Synthetic X}
after:
- subject: {id: 'EXAMPLE:C', label: Synthetic C}
  predicate: skos:exactMatch
  object: {id: 'EXAMPLE:X', label: Synthetic X}
```

The three IDs resolve to two removal proposals and one creation proposal, each
with its own evidence and lifecycle. Exporting the set or **any** of those IDs
shows all three operations and their statuses. This does not merge or delete
concepts A or B. A concept merge or split requires an explicit operation of its
own; the registry does not yet model those operations, and a mapping change
must not be presented as implementing them.

### Migration and review context

Legacy `MAPPING_MOVE` records with `removal`/`creation` and single-object views
remain readable and validate via the compatibility `LegacyMappingMove` class.
`refresh-change-set-views` migrates them to `changes` and assertion lists,
preserving their IDs, curated rationale and atomic records. Normal reads do
not rewrite files. New curation uses `OntologyChangeSet`; do not mix the layouts.

The owning `ontology`, `mapping_representation`, `before` and `after` are
materialized from the atomic records so the YAML is readable on GitHub without
opening another file. Validation requires exact agreement, including labels.
After creating the atomic records and the change-set ID/title/references
and writing its `justification`,
run `just ontology-changes refresh-change-set-views` to populate these fields.
Run it again after updating a member. The command validates the full registry
with regenerated views before writing any files; it cannot repair an invalid
change set or missing evidence. It changes only change-set files, never the atomic
records. Normal validation and export reject missing or stale views.

For new curation, write a self-contained `justification` for the complete change set:
explain the source scope, what the analysis revealed, why the selected correction
follows, which mappings remain, and any unresolved annotations. Do not substitute
a solver score for a scope argument. This prose is curated and preserved by refresh;
validation checks that it is nonblank, not that its interpretation is correct.

Refresh also derives `analysis_links`, `source_links`, `upstream_requests`,
`member_statuses`, `affected_records` and `see_also`. It removes duplicate links
and links back to the change set itself. Analysis links browse the saved reports
on GitHub; their paths and SHA-256 checksums remain in the authoritative atomic
records. Source URLs preserve the versions captured by those records. Member statuses
include verification dates and adoption notes; they describe the checked state,
not a fresh upstream lookup. Every supplied context field must agree with its
members. Partial context or stale statuses/links block validation and export.
Legacy sets with no review context remain valid; adding `justification` and running
refresh migrates them. Refresh never invents the justification or drops other
schema-valid fields.

Membership is stored once, in the change set; reverse membership is derived.
The atomic records keep their IDs, source snapshots, request status and adoption
status. A set has **no aggregate status**:
if one edit is accepted while others are pending, the export displays that
partial application explicitly. The set is a coordinated review unit, not an
assertion that upstream applies every edit transactionally. A target or qualifier
change belongs in `MAPPING_RESTRUCTURE`, not the subject-only `MAPPING_MOVE` type.

## Curating a record

1. Search this registry by ontology, term and mapping target, and check the
   upstream tracker before creating another request for the same edit.
2. Copy the owning source's identifiers, labels and current values. For MONDO
   xrefs, use native `icd11.foundation:` identifiers, not OAK's `icd11f:` alias.
   Capture an immutable source version, lookup date and a local snapshot under
   `sources/`, or reference an existing saved analysis snapshot. Preserve
   existing artifacts; a later lookup creates a new snapshot.
3. Choose the change type and populate exactly its edit fields:

   | Change | Required edit fields |
   |---|---|
   | `MAPPING_PREDICATE_CHANGE` | `mapping_target`, `mapping_representation`, `old_value`, `new_value` |
   | `MAPPING_CREATION` | `mapping_target`, `mapping_representation`, `new_value` |
   | `REMOVE_MAPPING` | `mapping_target`, `mapping_representation`, `old_value` |
   | `NODE_RENAME`, `NODE_TEXT_DEFINITION_CHANGE` | `old_value`, `new_value` |
   | `EDGE_CREATION`, `EDGE_DELETION` | `predicate`, `edge_object` |

   Edges run from `about_node` to `edge_object`. A mapping target remains
   explicit even when only its precision changes. `MONDO_XREF_QUALIFIER` means
   the values are qualifiers such as `MONDO:equivalentTo` and
   `MONDO:mondoIsNarrowerThanSource`. The latter corresponds to a broader target
   (`skos:broadMatch` from MONDO); it is not a request to insert an OWL subclass
   edge in mondo-edit.obo. `REMOVE_MAPPING` withdraws the xref/mapping entirely.
   `MAPPING_CREATION` adds a previously absent mapping; verify its absence in
   the before snapshot and omit `old_value`. If a mapping already exists but
   has the wrong qualifier, use `MAPPING_PREDICATE_CHANGE`. A move to a different
   subject is recorded as removal and creation records referenced in the
   `changes` list of a `MAPPING_MOVE` set. Larger mapping restructurings use
   `MAPPING_RESTRUCTURE`, referencing every atomic edit in the same list. Link each atomic record's `see_also` to its change
   set for readers browsing the YAML; the set's ID references are authoritative.
   For an applied edit, preserve before and current snapshots rather than
   pretending that the historical `old_value` still holds in the current source.
4. Write a self-contained justification based on source scope or biological
   evidence. Each `evidence` item cites a snapshot key and a locator within its
   artifact. Include a verbatim `supporting_text` excerpt. Observations are
   summaries, not purported verbatim quotations.
   Inspect these locators during review: automated validation checks the
   source key, artifact bytes and exact excerpts, not whether the interpretation
   follows from the source.
5. Record curation `confidence`: HIGH for direct source support for the precise
   edit; MEDIUM when a material scope question remains; LOW for a candidate
   needing investigation. **Do not copy a Boomer probability into this field.**
   Put solver results in checksum-addressed `analysis_artifacts` and retain
   their priors, constraints, provenance and completion status there.
6. Set the lifecycle, affected records and adoption rationale, then validate.
   `ontology_state_verified` must match the lookup date of a snapshot of the
   owning ontology. It says when the state was checked, not that it is current
   forever. Recheck before filing or applying an old proposal.

## Two independent lifecycles

`SELF_PROPOSED` requires curator confidence and `request_status`:
`NOT_FILED`, `FILED`, `ACKNOWLEDGED`, `ACCEPTED`, or `DECLINED`.
Here `ACCEPTED` means the ontology actually made the change; a favorable
comment alone is `ACKNOWLEDGED`. Filed states require an upstream issue or PR
URL. Keep related discussions and DisMech analysis PRs in `see_also`, not in
the fields claiming that this exact edit has been submitted upstream.

`UPSTREAM_PROPOSED` and `UPSTREAM_APPLIED` require an upstream issue or PR,
and may record our `stance` (agree, partially agree, disagree, undecided).
They must not claim that we filed a request or grade our own confidence in
somebody else's decision. Snapshot dates still document what was checked.

Independently, `adoption_status` is `NOT_STARTED`, `IN_PROGRESS`, `COMPLETE`
or `NOT_APPLICABLE`. Always explain it in `adoption_notes`. Upstream can have
applied a correction while our affected entries still await migration.
Historical solver inputs must not be rewritten to make an old result appear
to have used corrected mappings.

## Schema lineage and limits

The standalone [LinkML schema](../src/dismech/schema/ontology_change.yaml)
adapts ai-gene-review's
[`ProposedOntologyChange` at b2696a6](https://github.com/ai4curation/ai-gene-review/blob/b2696a68614d4c57abbf5a663d82a681880c69b0/src/ai_gene_review/schema/gene_review.yaml#L804),
including the separation of origin, request progress and local adoption.
The mapping-target field closes the gap that schema documents for
`MAPPING_PREDICATE_CHANGE`. This pilot supports seven edit kinds; add new kinds
with concrete cases and validation rules rather than parking them in OTHER.
New-term requests, merges and obsoletions are not modeled yet.

KGCL class meanings describe the kind of edit. They do not make this proposal
envelope valid executable KGCL. `MAPPING_CREATION` is a registry extension with
explicit endpoint/qualifier semantics, not an asserted KGCL class mapping.
A future exporter must translate the source
representation, check the old value as a precondition, preserve unrelated
annotations, and be tested against the target ontology's tooling. The current
export is for human review only.
