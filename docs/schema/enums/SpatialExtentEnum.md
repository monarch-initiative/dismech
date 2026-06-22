# Enum: SpatialExtentEnum 




_Qualifiers for the spatial extent or distribution of a phenotype or process_



URI: [dismech:enum/SpatialExtentEnum](https://w3id.org/monarch-initiative/dismech/enum/SpatialExtentEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| FOCAL | None | Confined to a single location or region | Title: Focal<br>|
| MULTIFOCAL | None | Affecting multiple discrete locations | Title: Multifocal<br>|
| DIFFUSE | None | Widespread, continuous distribution | Title: Diffuse<br>|
| EXTENSIVE | None | Large extent, typically involving multiple segments or regions | Title: Extensive<br>|
| PATCHY | None | Irregular, discontinuous distribution | Title: Patchy<br>|
| SEGMENTAL | None | Affecting a specific segment or dermatome | Title: Segmental<br>|




## Slots

| Name | Description |
| ---  | --- |
| [spatial_extent](../slots/spatial_extent.md) | The spatial extent or distribution pattern applicable to this descriptor (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SpatialExtentEnum
description: Qualifiers for the spatial extent or distribution of a phenotype or process
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  FOCAL:
    text: FOCAL
    description: Confined to a single location or region
    title: Focal
  MULTIFOCAL:
    text: MULTIFOCAL
    description: Affecting multiple discrete locations
    title: Multifocal
  DIFFUSE:
    text: DIFFUSE
    description: Widespread, continuous distribution
    title: Diffuse
  EXTENSIVE:
    text: EXTENSIVE
    description: Large extent, typically involving multiple segments or regions
    title: Extensive
  PATCHY:
    text: PATCHY
    description: Irregular, discontinuous distribution
    title: Patchy
  SEGMENTAL:
    text: SEGMENTAL
    description: Affecting a specific segment or dermatome
    title: Segmental

```
</details>