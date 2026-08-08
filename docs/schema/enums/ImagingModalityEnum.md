# Enum: ImagingModalityEnum 




_In-vivo medical imaging modality by which an ImagingFinding is detected. Meanings bind to the NCI Thesaurus Diagnostic Imaging branch._



URI: [dismech:enum/ImagingModalityEnum](https://w3id.org/monarch-initiative/dismech/enum/ImagingModalityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| MRI | NCIT:C16809 | Magnetic resonance imaging, including structural and contrast-enhanced MRI | Title: Magnetic Resonance Imaging<br>|
| FUNCTIONAL_MRI | NCIT:C17958 | Blood-oxygen-level-dependent functional MRI | Title: Functional Magnetic Resonance Imaging<br>|
| CT | NCIT:C17204 | X-ray computed tomography | Title: Computed Tomography<br>|
| PET | NCIT:C17007 | Positron emission tomography (e | Title: Positron Emission Tomography<br>|
| SPECT | NCIT:C17203 | Single-photon emission computed tomography | Title: Single Photon Emission Computed Tomography<br>|
| ULTRASOUND | NCIT:C17230 | Diagnostic ultrasonography, including Doppler and echocardiography | Title: Ultrasound Imaging<br>|
| XRAY | NCIT:C38101 | Projectional radiography (plain film) | Title: X-Ray Imaging<br>|
| MAMMOGRAPHY | NCIT:C16818 | X-ray imaging of the breast | Title: Mammography<br>|
| ANGIOGRAPHY | NCIT:C190556 | Imaging of blood vessels (CT, MR, or catheter angiography) | Title: Angiography<br>|
| OCT | NCIT:C20828 | Optical coherence tomography (e | Title: Optical Coherence Tomography<br>|
| OTHER | None | An imaging modality not otherwise enumerated | Title: Other imaging modality<br>|




## Slots

| Name | Description |
| ---  | --- |
| [modality](../slots/modality.md) | The in-vivo imaging modality by which a finding is detected |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ImagingModalityEnum
description: In-vivo medical imaging modality by which an ImagingFinding is detected.
  Meanings bind to the NCI Thesaurus Diagnostic Imaging branch.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  MRI:
    text: MRI
    description: Magnetic resonance imaging, including structural and contrast-enhanced
      MRI
    meaning: NCIT:C16809
    title: Magnetic Resonance Imaging
  FUNCTIONAL_MRI:
    text: FUNCTIONAL_MRI
    description: Blood-oxygen-level-dependent functional MRI
    meaning: NCIT:C17958
    title: Functional Magnetic Resonance Imaging
  CT:
    text: CT
    description: X-ray computed tomography
    meaning: NCIT:C17204
    title: Computed Tomography
  PET:
    text: PET
    description: Positron emission tomography (e.g., FDG-PET, amyloid-PET)
    meaning: NCIT:C17007
    title: Positron Emission Tomography
  SPECT:
    text: SPECT
    description: Single-photon emission computed tomography
    meaning: NCIT:C17203
    title: Single Photon Emission Computed Tomography
  ULTRASOUND:
    text: ULTRASOUND
    description: Diagnostic ultrasonography, including Doppler and echocardiography
    meaning: NCIT:C17230
    title: Ultrasound Imaging
  XRAY:
    text: XRAY
    description: Projectional radiography (plain film)
    meaning: NCIT:C38101
    title: X-Ray Imaging
  MAMMOGRAPHY:
    text: MAMMOGRAPHY
    description: X-ray imaging of the breast
    meaning: NCIT:C16818
    title: Mammography
  ANGIOGRAPHY:
    text: ANGIOGRAPHY
    description: Imaging of blood vessels (CT, MR, or catheter angiography)
    meaning: NCIT:C190556
    title: Angiography
  OCT:
    text: OCT
    description: Optical coherence tomography (e.g., retinal OCT)
    meaning: NCIT:C20828
    title: Optical Coherence Tomography
  OTHER:
    text: OTHER
    description: An imaging modality not otherwise enumerated
    title: Other imaging modality

```
</details>