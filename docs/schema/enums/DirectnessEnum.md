# Enum: DirectnessEnum 




_How directly the quoted evidence bears on the claim it is attached to. The evidential counterpart of CausalLinkTypeEnum, which records the same notion of directness for a causal edge._



URI: [dismech:enum/DirectnessEnum](https://w3id.org/monarch-initiative/dismech/enum/DirectnessEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| DIRECT | None | The quoted text asserts the claim itself | Title: Direct<br>|
| INDIRECT | None | The quoted text asserts something from which the claim follows by an inferenc... | Title: Indirect<br>|
| UNKNOWN | None | Directness has not yet been assessed | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [directness](../slots/directness.md) | How directly the quoted text bears on the claim |








## Comments

* This is not a strength or quality grade. An indirect quote may come from a large, well-controlled study, and a direct one from a single case report. Directness is judgeable from the snippet and the claim alone, which is why it is a curated slot where strength is not.
* Deliberately has no PARTIAL value. "Supports part of the claim and contradicts another part" is not a point on a directness scale -- it is one evidence item making two claims, and the fix is to split it into a SUPPORT item and a REFUTE item, each quoting the sentence that carries it. That is the same remedy CLAUDE.md already prescribes for a paper that mixes evidence_source values.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DirectnessEnum
description: How directly the quoted evidence bears on the claim it is attached to.
  The evidential counterpart of CausalLinkTypeEnum, which records the same notion
  of directness for a causal edge.
comments:
- This is not a strength or quality grade. An indirect quote may come from a large,
  well-controlled study, and a direct one from a single case report. Directness is
  judgeable from the snippet and the claim alone, which is why it is a curated slot
  where strength is not.
- Deliberately has no PARTIAL value. "Supports part of the claim and contradicts another
  part" is not a point on a directness scale -- it is one evidence item making two
  claims, and the fix is to split it into a SUPPORT item and a REFUTE item, each quoting
  the sentence that carries it. That is the same remedy CLAUDE.md already prescribes
  for a paper that mixes evidence_source values.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  DIRECT:
    text: DIRECT
    description: The quoted text asserts the claim itself
    title: Direct
  INDIRECT:
    text: INDIRECT
    description: The quoted text asserts something from which the claim follows by
      an inference step -- for example a therapeutic response cited as validation
      of the mechanism it targets, or a result from an inverted or non-human model
      system.
    title: Indirect
  UNKNOWN:
    text: UNKNOWN
    description: Directness has not yet been assessed
    title: Unknown

```
</details>