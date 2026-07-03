# Enum: DiscussionKindEnum 




_Kind of unresolved/in-progress item captured by a Discussion. Discussions are thread-like objects that record open questions, controversies, curation todos, emerging hypotheses, or interpretation debates attached to a disease entry or sub-object. Knowledge gaps are represented as a discussion kind so they can reuse the existing pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved._



URI: [dismech:enum/DiscussionKindEnum](https://w3id.org/monarch-initiative/dismech/enum/DiscussionKindEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| OPEN_QUESTION | None | An unresolved scientific question posed by curators or experts |
| KNOWLEDGE_GAP | None | A missing causal, evidentiary, model-system, or translational assertion whose... |
| CONTROVERSY | None | A live disagreement or competing interpretation between published positions |
| CURATION_TODO | None | A curation task captured inline (e |
| EMERGING_HYPOTHESIS | None | A recently reported hypothesis under active discussion in the community |
| INTERPRETATION | None | A discussion about how to interpret existing evidence or model an edge |
| HUMAN_MODEL_MISMATCH | None | A knowledge gap where model-system evidence exists but its fidelity to human ... |




## Slots

| Name | Description |
| ---  | --- |
| [kind](../slots/kind.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DiscussionKindEnum
description: Kind of unresolved/in-progress item captured by a Discussion. Discussions
  are thread-like objects that record open questions, controversies, curation todos,
  emerging hypotheses, or interpretation debates attached to a disease entry or sub-object.
  Knowledge gaps are represented as a discussion kind so they can reuse the existing
  pointer, evidence, and lifecycle machinery, while optional proposed experiments
  capture how a gap could be resolved.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  OPEN_QUESTION:
    text: OPEN_QUESTION
    description: An unresolved scientific question posed by curators or experts
  KNOWLEDGE_GAP:
    text: KNOWLEDGE_GAP
    description: A missing causal, evidentiary, model-system, or translational assertion
      whose resolution would materially improve the disease mechanism model
  CONTROVERSY:
    text: CONTROVERSY
    description: A live disagreement or competing interpretation between published
      positions
  CURATION_TODO:
    text: CURATION_TODO
    description: A curation task captured inline (e.g., "phenotype needs HPO term
      refinement")
  EMERGING_HYPOTHESIS:
    text: EMERGING_HYPOTHESIS
    description: A recently reported hypothesis under active discussion in the community
  INTERPRETATION:
    text: INTERPRETATION
    description: A discussion about how to interpret existing evidence or model an
      edge
  HUMAN_MODEL_MISMATCH:
    text: HUMAN_MODEL_MISMATCH
    description: A knowledge gap where model-system evidence exists but its fidelity
      to human disease-relevant biology is uncertain — the model may recapitulate
      a proximal mechanism or phenotype only partially, or the relevant human cell
      type (e.g., outer radial glia) or anatomy (e.g., gyrencephalic cortex) is absent
      from the model. Distinct from KNOWLEDGE_GAP (which covers any missing assertion)
      in that some mechanistic evidence exists but translational validity is the open
      question. Use when a curator wants to flag that model-organism, organoid, or
      in vitro data support a node but it is unclear whether the same mechanism operates
      in the human disease context.

```
</details>