# Canonical explicit edge claims

`dismech.classifier.edge_reading` classifies an explicit edge claim supplied as a
plain mapping, for example loaded from YAML. The canonical input is the model
state: inference validates it and makes a detached copy without projection,
rewriting, field removal or default insertion.

```python
from dismech.classifier.edge_reading import (
    edge_claim_task, edge_claim_aspect_schema, edge_prompt,
)

task = edge_claim_task(claim)
assert task.state == claim
output_schema = edge_claim_aspect_schema(claim)
prompt = edge_prompt()  # edge_claim_aspects, version 2
```

A minimal synthetic claim is:

```yaml
scope:
  disease: {name: Synthetic condition}
  subtypes: []
  hypotheses: []
  additional_context: []
subject:
  name: Synthetic source
  document_path: /pathophysiology/0
  qualifiers: {}
relationship:
  kind: causal influence
  description: A candidate effect observed in cultured cells.
object:
  name: Experimental endpoint in cultured cells
  document_path: /phenotypes/0
  qualifiers: {}
definitions:
  subject: {description: Proposed source in a model system.}
  object: {description: A model-specific measurement.}
selected_evidence:
  snippet: Synthetic observation in cultured cells.
  supports: SUPPORT
  directness: INDIRECT
```

`subject` is the source or intervention; `object` is the affected endpoint.
Their document paths are explicit stable identifiers. Names and explicit qualifiers
occur once, in these endpoint objects. `definitions` holds the remaining endpoint
background, including descriptions and ontology terms, without duplicated names
or qualifiers, annotations or independent outgoing edges. Background defines
referents and scope; it is neither independent evidence nor a bundle of extra
edge assertions. The claim has no redundant `reading` sentence.

`relationship.kind` is `causal influence` or `treatment effect`. Its remaining
fields follow the corresponding `CausalEdge` or `TreatmentMechanismTarget` slots,
except that the target is represented by `object`. Disease identity, resolved
subtypes and hypotheses, and other context belong in `scope`. Subtype and hypothesis
definitions are flat objects with `document_path` plus their original fields.
References in endpoint qualifiers or the relationship must resolve uniquely there.
Arbitrary scalar or collection context uses `{document_path, value}`.

Inference rejects malformed shapes, unsupported relationship/evidence values,
missing or ambiguous referenced scope, nested annotations or evaluation records,
and independent outgoing edges in endpoint definitions. It preserves legitimate
ontology labels, authored descriptions and notes. Evidence contains `snippet`,
`supports` and optional `directness`. Optional `source_text` is appended only when
explicitly passed to `edge_claim_task`; separate findings cannot rescue the excerpt.

Response paths refer directly to the supplied claim: `/scope/disease`,
`/object/name`, `/relationship/description`, and other selected relationship fields.
`/` denotes the complete relationship, endpoint identities/qualifiers and explicit
scope. `EDGE_FIELDS` selects target, description, causal-link type, intermediates,
hypothesis groups and treatment effect; `target` selects `/object/name`. Unknown
selected fields fail. Absent and null fields produce no question; present empty collections retain
questions, matching this pinned version of the aspect compiler. Target identity includes qualifications in
the name; missing disease attribution is assessed separately. The prompt preserves
the existing SUPPORT/REFUTE/NO_EVIDENCE and MATCH/MISMATCH/PARTIAL contracts,
distinguishes shared causes from directed edges, and respects provisional hypotheses.

## One-time extraction from legacy claims

For migration or initial authoring, `canonical_edge_claim(legacy_claim)` extracts
the canonical mapping from an existing frozen `StructuredClaim`. Save that result
as the explicit claim before inference. Inference functions never invoke extraction.
`edge_reading(legacy_claim)` remains an extraction diagnostic with the historical
orientation sentence and duplicated endpoint fields; its output is not valid
canonical inference input. There are no legacy inference adapters.

Extraction requires the unique ancestor binding at the containment parent of
`origin.assertion_path`, an exact bare target-name binding, and explicit unique
subtype and hypothesis definitions. It never guesses from binding order or fetches
missing context. It preserves the exact authored relationship description, including
whitespace, and all retained biomedical qualifiers. It removes evidence annotations
and independent outgoing edges, then removes the redundant sentence and duplicated
endpoint fields for the canonical form. It cannot recover content already omitted
by the original extractor. Missing context requires a new extraction or revision.

This utility does not alter existing extraction, legacy classifier prompts, the
public knowledge-base schema or curated records.
