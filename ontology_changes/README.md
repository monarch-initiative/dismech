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

## Validate, query and export

From the repository root:

```bash
just validate-ontology-changes
just ontology-changes list --ontology MONDO --request-status NOT_FILED
just ontology-changes list --affected-record kb/disorders/FOXE3_Anterior_Segment_Dysgenesis.yaml
just ontology-changes export mondo-0019503-icd11-anterior-segment-broad-match
```

`list` returns complete JSON records; `export` writes a Markdown request to
stdout for review. Both validate the registry first. Neither publishes a
ticket, changes a mapping, or applies a KGCL patch. The validator checks the
LinkML schema, type-specific fields, lifecycle combinations, unique IDs,
evidence-source references, exact supporting excerpts, local paths and artifact
SHA-256 checksums. CI
runs it on every PR, including proposals-only edits.

Use `affected_records` to link diseases, groupings and analyses to a proposal.
The reverse query above gives the proposals for an entry without duplicating
their lifecycle state inside disease YAML. Existing `tracked_issues` remains
the place for links to filed tickets. `history/` records curation sessions;
this registry records the edits being requested. No change to the Disease
schema is required.

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
   | `REMOVE_MAPPING` | `mapping_target`, `mapping_representation`, `old_value` |
   | `NODE_RENAME`, `NODE_TEXT_DEFINITION_CHANGE` | `old_value`, `new_value` |
   | `EDGE_CREATION`, `EDGE_DELETION` | `predicate`, `edge_object` |

   Edges run from `about_node` to `edge_object`. A mapping target remains
   explicit even when only its precision changes. `MONDO_XREF_QUALIFIER` means
   the values are qualifiers such as `MONDO:equivalentTo` and
   `MONDO:mondoIsNarrowerThanSource`. The latter corresponds to a broader target
   (`skos:broadMatch` from MONDO); it is not a request to insert an OWL subclass
   edge in mondo-edit.obo. `REMOVE_MAPPING` withdraws the xref/mapping entirely.
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
`MAPPING_PREDICATE_CHANGE`. This pilot supports six edit kinds; add new kinds
with concrete cases and validation rules rather than parking them in OTHER.
New-term requests, merges and obsoletions are not modeled yet.

KGCL class meanings describe the kind of edit. They do not make this proposal
envelope valid executable KGCL. A future exporter must translate the source
representation, check the old value as a precondition, preserve unrelated
annotations, and be tested against the target ontology's tooling. The current
export is for human review only.
