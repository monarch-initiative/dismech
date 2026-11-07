# Edge claim reading projections

`dismech.classifier.edge_reading` provides an opt-in reading of an existing frozen
`CausalEdge` or `TreatmentMechanismTarget` claim. It changes neither canonical
extraction nor the existing prompts. It makes the source, affected endpoint,
relationship and explicit scope visible in separate fields:

```python
from dismech.classifier.edge_reading import (
    edge_reading, edge_reading_task, edge_aspect_schema, edge_prompt,
)

state = edge_reading(claim)
task = edge_reading_task(claim, source_text=source_text)
output_schema = edge_aspect_schema(claim)
prompt = edge_prompt()  # edge_claim_aspects, version 1
```

The source must be the unique ancestor binding at the edge's containment parent
in `origin.assertion_path`. The target must have a unique explicit binding with
the exact bare node name. No ordering heuristic, name paraphrase or entity-reference
prefix conversion is used. Cited hypothesis IDs and endpoint subtype references
must resolve uniquely in the frozen bindings; missing, ambiguous or inconsistent
bindings raise `ValueError`. Add missing context through a new extraction or case
revision, rather than borrowing definitions from a later document version.

`reading` consists of a neutral source-to-target sentence followed by the **exact
authored edge description**, including whitespace. It adds no biomedical inference
and cannot narrow the other relationship fields. `subject` and `object` carry names,
document paths and explicit qualifiers; `relationship` retains every original edge
field except `target`, plus the neutral relationship kind. `scope` retains disease
identity, flat resolved subtype/hypothesis definitions with their document paths,
and remaining context. Endpoint `definitions` retain the frozen node descriptions,
ontology terms and biomedical qualifiers, excluding annotations and independent
outgoing relationships. They provide interpretation context, not extra edge claims
or independent evidence. The projection does not recover fields already omitted
by the original extractor. Every returned value is detached from the input.

The evidence view contains only `snippet`, `supports` and optional `directness`.
Evidence explanations, review notes and external evaluation records are not model
input. Accidentally nested evaluation metadata is rejected; legitimate ontology
labels, authored descriptions and notes are preserved.

Response keys retain the canonical aspect paths (`/`, `/about/disease`,
`/assertion/target`, etc.). Question descriptions instead name the actual reading
fields (`scope.disease`, `object.name`, `relationship.description`, etc.). The default
`EDGE_FIELDS` selects target, description, causal-link type, intermediates,
hypothesis groups and treatment effect when present and non-null; unknown selected
fields fail. Empty but present values follow the existing aspect compiler's rule.
The root assesses all relationship fields, endpoint identities/qualifiers and
explicit scope, not every independent observation in the endpoint definitions.
Target identity includes qualifications in the target name; unclear disease
attribution is assessed separately and does not by itself defeat endpoint identity.

The prompt distinguishes a causal chain from parallel effects of a shared cause,
causal topology from evidence directness, and provisional hypotheses from established
causation. Intermediates must be supported in their role on the source-to-target
route. The existing SUPPORT/REFUTE/NO_EVIDENCE and MATCH/MISMATCH/PARTIAL contracts
remain in effect; source text can contextualize the excerpt but cannot rescue it
with unrelated findings. This is a deterministic representation utility, not a new
knowledge-base section or a claim of improved classifier accuracy.
