# Enum: ElectrophysiologyModalityEnum 




_In-vivo electrophysiologic / neurophysiologic investigation on which an electrophysiologic phenotype was recorded (carried on the ElectrophysiologyContext phenotype sidecar). Meanings bind to the NCI Thesaurus diagnostic-procedure branch._



URI: [dismech:enum/ElectrophysiologyModalityEnum](https://w3id.org/monarch-initiative/dismech/enum/ElectrophysiologyModalityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| EEG | NCIT:C38054 | Scalp electroencephalography (routine, prolonged, or ambulatory) | Title: Electroencephalography<br>|
| VIDEO_EEG | None | Simultaneous video and EEG monitoring for seizure semiology-EEG correlation | Title: Video Electroencephalography<br>|
| ECG | NCIT:C38053 | Electrocardiography, including resting and stress ECG | Title: Electrocardiography<br>|
| EMG | NCIT:C38056 | Needle or surface electromyography | Title: Electromyography<br>|
| NERVE_CONDUCTION_STUDY | NCIT:C88502 | Nerve conduction study (motor/sensory conduction velocity and amplitude) | Title: Nerve Conduction Velocity Test<br>|
| EVOKED_POTENTIAL | None | Evoked-potential testing (visual, brainstem-auditory, or somatosensory) | Title: Evoked Potential<br>|
| POLYSOMNOGRAPHY | NCIT:C114185 | Overnight sleep study combining EEG, EOG, EMG, ECG, and respiratory channels | Title: Polysomnography<br>|
| MEG | NCIT:C16811 | Magnetoencephalography (magnetic-field source localization) | Title: Magnetoencephalography<br>|
| OTHER | None | An electrophysiologic modality not otherwise enumerated | Title: Other electrophysiologic modality<br>|




## Slots

| Name | Description |
| ---  | --- |
| [electrophysiology_modality](../slots/electrophysiology_modality.md) | The in-vivo electrophysiologic modality on which a phenotype was recorded |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ElectrophysiologyModalityEnum
description: In-vivo electrophysiologic / neurophysiologic investigation on which
  an electrophysiologic phenotype was recorded (carried on the ElectrophysiologyContext
  phenotype sidecar). Meanings bind to the NCI Thesaurus diagnostic-procedure branch.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  EEG:
    text: EEG
    description: Scalp electroencephalography (routine, prolonged, or ambulatory)
    meaning: NCIT:C38054
    title: Electroencephalography
  VIDEO_EEG:
    text: VIDEO_EEG
    description: Simultaneous video and EEG monitoring for seizure semiology-EEG correlation.
      No distinct NCIT procedure term; a specialization of EEG.
    title: Video Electroencephalography
  ECG:
    text: ECG
    description: Electrocardiography, including resting and stress ECG
    meaning: NCIT:C38053
    title: Electrocardiography
  EMG:
    text: EMG
    description: Needle or surface electromyography
    meaning: NCIT:C38056
    title: Electromyography
  NERVE_CONDUCTION_STUDY:
    text: NERVE_CONDUCTION_STUDY
    description: Nerve conduction study (motor/sensory conduction velocity and amplitude)
    meaning: NCIT:C88502
    title: Nerve Conduction Velocity Test
  EVOKED_POTENTIAL:
    text: EVOKED_POTENTIAL
    description: Evoked-potential testing (visual, brainstem-auditory, or somatosensory).
      No clean generic NCIT procedure term.
    title: Evoked Potential
  POLYSOMNOGRAPHY:
    text: POLYSOMNOGRAPHY
    description: Overnight sleep study combining EEG, EOG, EMG, ECG, and respiratory
      channels
    meaning: NCIT:C114185
    title: Polysomnography
  MEG:
    text: MEG
    description: Magnetoencephalography (magnetic-field source localization)
    meaning: NCIT:C16811
    title: Magnetoencephalography
  OTHER:
    text: OTHER
    description: An electrophysiologic modality not otherwise enumerated
    title: Other electrophysiologic modality

```
</details>