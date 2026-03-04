# Enum: ICDOMorphologyEnum 




_ICD-O morphology axis classification for cancer subtypes. Values link to NCI Thesaurus for formal definitions._



URI: [dismech:ICDOMorphologyEnum](https://w3id.org/monarch-initiative/dismech/ICDOMorphologyEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Carcinoma | NCIT:C2916 | Cancer arising from epithelial cells |
| Adenocarcinoma | NCIT:C2852 | Carcinoma arising from glandular epithelium |
| Squamous Cell Carcinoma | NCIT:C2929 | Carcinoma arising from squamous epithelium |
| Sarcoma | NCIT:C9118 | Cancer arising from mesenchymal tissue |
| Leukemia | NCIT:C3161 | Cancer of blood-forming tissues |
| Lymphoma | NCIT:C3208 | Cancer of the lymphatic system |
| Multiple Myeloma | NCIT:C3242 | Cancer of plasma cells |
| Melanoma | NCIT:C3224 | Cancer arising from melanocytes |
| Glioma | NCIT:C3059 | Cancer arising from glial cells |
| Embryonal Neoplasm | NCIT:C3264 | Cancer arising from embryonic tissue |




## Slots

| Name | Description |
| ---  | --- |
| [classification_value](classification_value.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ICDOMorphologyEnum
description: ICD-O morphology axis classification for cancer subtypes. Values link
  to NCI Thesaurus for formal definitions.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  Carcinoma:
    text: Carcinoma
    description: Cancer arising from epithelial cells
    meaning: NCIT:C2916
    exact_mappings:
    - MONDO:0004993
    - ICDO:8010/3
  Adenocarcinoma:
    text: Adenocarcinoma
    description: Carcinoma arising from glandular epithelium
    meaning: NCIT:C2852
    exact_mappings:
    - MONDO:0004970
    - ICDO:8140/3
  Squamous Cell Carcinoma:
    text: Squamous Cell Carcinoma
    description: Carcinoma arising from squamous epithelium
    meaning: NCIT:C2929
    exact_mappings:
    - MONDO:0005096
    - ICDO:8070/3
  Sarcoma:
    text: Sarcoma
    description: Cancer arising from mesenchymal tissue
    meaning: NCIT:C9118
    exact_mappings:
    - MONDO:0005089
    - ICDO:8800/3
  Leukemia:
    text: Leukemia
    description: Cancer of blood-forming tissues
    meaning: NCIT:C3161
    exact_mappings:
    - MONDO:0005059
    - ICDO:9800/3
  Lymphoma:
    text: Lymphoma
    description: Cancer of the lymphatic system
    meaning: NCIT:C3208
    exact_mappings:
    - MONDO:0005062
    - ICDO:9590/3
  Multiple Myeloma:
    text: Multiple Myeloma
    description: Cancer of plasma cells
    meaning: NCIT:C3242
    exact_mappings:
    - MONDO:0009693
    - ICDO:9732/3
  Melanoma:
    text: Melanoma
    description: Cancer arising from melanocytes
    meaning: NCIT:C3224
    exact_mappings:
    - MONDO:0005105
    - ICDO:8720/3
  Glioma:
    text: Glioma
    description: Cancer arising from glial cells
    meaning: NCIT:C3059
    exact_mappings:
    - MONDO:0021042
    - ICDO:9380/3
  Embryonal Neoplasm:
    text: Embryonal Neoplasm
    description: Cancer arising from embryonic tissue
    meaning: NCIT:C3264
    exact_mappings:
    - MONDO:0005564

```
</details>