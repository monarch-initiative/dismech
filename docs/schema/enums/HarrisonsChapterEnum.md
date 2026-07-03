# Enum: HarrisonsChapterEnum 




_Harrison's Principles of Internal Medicine classification by Part. Values correspond to the high-level Parts (organ-system or topical groupings) of Harrison's 21st edition (2022). The slot is named `harrisons_chapter` for historical reasons, but the controlled vocabulary lives at the Part level since this is the granularity that matches how curators classify disorders. A single disease may be assigned to multiple Parts (e.g., a hereditary skin disorder could be tagged DERMATOLOGY and GENETICS_ENVIRONMENT_DISEASE). Free-text values used in earlier curation are preserved as `aliases` on the closest-fit Part so that legacy entries continue to validate._



URI: [dismech:enum/HarrisonsChapterEnum](https://w3id.org/monarch-initiative/dismech/enum/HarrisonsChapterEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| GENERAL_CONSIDERATIONS | None | Approach to the patient, clinical decision-making, ethics, evidence-based med... | Title: General Considerations in Clinical Medicine<br>|
| CARDINAL_MANIFESTATIONS | None | Cardinal symptom and sign presentations (pain, fever, fatigue, weight change,... | Title: Cardinal Manifestations and Presentation of Diseases<br>|
| PHARMACOLOGY | None | Principles of clinical pharmacology, drug therapeutics, and adverse drug reac... | Title: Pharmacology<br>|
| ONCOLOGY_HEMATOLOGY | None | Cancers (solid tumors and hematologic malignancies) and non-malignant hematol... | Title: Oncology and Hematology<br>|
| INFECTIOUS_DISEASES | None | Bacterial, viral, fungal, parasitic, and other microbial infections; antimicr... | Title: Infectious Diseases<br>|
| CARDIOVASCULAR | None | Cardiac and vascular diseases including ischemic heart disease, heart failure... | Title: Disorders of the Cardiovascular System<br>|
| RESPIRATORY | None | Pulmonary diseases including obstructive lung disease (asthma, COPD), interst... | Title: Disorders of the Respiratory System<br>|
| CRITICAL_CARE | None | Approach to the critically ill patient, including sepsis and septic shock, AR... | Title: Critical Care Medicine<br>|
| KIDNEY_URINARY_TRACT | None | Renal and urinary tract diseases including glomerular and tubulointerstitial ... | Title: Disorders of the Kidney and Urinary Tract<br>|
| GASTROINTESTINAL | None | Digestive-system disorders including esophageal, gastric, small-bowel, coloni... | Title: Disorders of the Gastrointestinal System<br>|
| IMMUNE_RHEUMATOLOGIC | None | Autoimmune and immune-mediated conditions, connective-tissue diseases, vascul... | Title: Immune-Mediated, Inflammatory, and Rheumatologic Disorders<br>|
| ENDOCRINOLOGY_METABOLISM | None | Endocrine and metabolic diseases including diabetes mellitus, thyroid, adrena... | Title: Endocrinology and Metabolism<br>|
| NEUROLOGIC | None | Diseases of the central and peripheral nervous system, including stroke, epil... | Title: Neurologic Disorders<br>|
| DERMATOLOGY | None | Skin and cutaneous disorders | Title: Disorders of the Skin<br>|
| POISONING_ENVENOMATION | None | Toxicology, poisoning syndromes, drug overdose, and bites or other venom expo... | Title: Poisoning, Drug Overdose, and Envenomation<br>|
| ENVIRONMENTAL_EXPOSURES | None | Disorders attributable to environmental exposures such as altitude, hypotherm... | Title: Disorders Associated with Environmental Exposures<br>|
| GENETICS_ENVIRONMENT_DISEASE | None | Genetic and genomic medicine, chromosomal and Mendelian disorders not better ... | Title: Genes, the Environment, and Disease<br>|
| DISORDER_OF_EAR | None | Disorders of hearing and the vestibular system | Title: Disorders of the Ear<br>|
| GLOBAL_MEDICINE | None | Diseases and health issues that are predominantly addressed in a global healt... | Title: Global Medicine<br>|
| AGING | None | Disorders, syndromes, and physiologic considerations specific to older adults | Title: Aging<br>|
| CONSULTATIVE_MEDICINE | None | Approach to the patient when consulting across specialties (medical consultat... | Title: Consultative Medicine<br>|
| OTHER | None | The disorder does not fit cleanly into any of the above Parts | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [classification_value](../slots/classification_value.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: HarrisonsChapterEnum
description: Harrison's Principles of Internal Medicine classification by Part. Values
  correspond to the high-level Parts (organ-system or topical groupings) of Harrison's
  21st edition (2022). The slot is named `harrisons_chapter` for historical reasons,
  but the controlled vocabulary lives at the Part level since this is the granularity
  that matches how curators classify disorders. A single disease may be assigned to
  multiple Parts (e.g., a hereditary skin disorder could be tagged DERMATOLOGY and
  GENETICS_ENVIRONMENT_DISEASE). Free-text values used in earlier curation are preserved
  as `aliases` on the closest-fit Part so that legacy entries continue to validate.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  GENERAL_CONSIDERATIONS:
    text: GENERAL_CONSIDERATIONS
    description: Approach to the patient, clinical decision-making, ethics, evidence-based
      medicine, screening, and global aspects of medicine. Use sparingly for diseases
      - most diseases fit a more specific organ-system Part.
    title: General Considerations in Clinical Medicine
  CARDINAL_MANIFESTATIONS:
    text: CARDINAL_MANIFESTATIONS
    description: Cardinal symptom and sign presentations (pain, fever, fatigue, weight
      change, cough, dyspnea, etc.) and chapters on alterations of the skin, ear,
      nose, and throat. Use for symptom-defined entries that cut across organ systems.
    title: Cardinal Manifestations and Presentation of Diseases
  PHARMACOLOGY:
    text: PHARMACOLOGY
    description: Principles of clinical pharmacology, drug therapeutics, and adverse
      drug reactions. Rarely used for disorder entries.
    title: Pharmacology
  ONCOLOGY_HEMATOLOGY:
    text: ONCOLOGY_HEMATOLOGY
    description: Cancers (solid tumors and hematologic malignancies) and non-malignant
      hematologic disorders including anemias, coagulation disorders, transfusion
      medicine, and bone marrow failure syndromes.
    title: Oncology and Hematology
    aliases:
    - cancer
    - solid tumor
    - hematologic malignancy
    - hematologic disorder
    - anemia
    - coagulation disorder
    - Adenocarcinoma
    - Carcinoma
    - Embryonal Neoplasm
    - Glioma
    - Leukemia
    - Lymphoma
    - Melanoma
    - Sarcoma
    - Squamous Cell Carcinoma
  INFECTIOUS_DISEASES:
    text: INFECTIOUS_DISEASES
    description: Bacterial, viral, fungal, parasitic, and other microbial infections;
      antimicrobial therapy; infections in immunocompromised hosts; and infections
      by organ system when presented from an infectious-disease perspective.
    title: Infectious Diseases
    aliases:
    - infectious disease
    - bacterial infectious disease
    - viral infectious disease
    - fungal infectious disease
    - parasitic infectious disease
  CARDIOVASCULAR:
    text: CARDIOVASCULAR
    description: Cardiac and vascular diseases including ischemic heart disease, heart
      failure, arrhythmias, cardiomyopathies, valvular and pericardial disease, congenital
      heart disease, and disorders of the aorta and peripheral vasculature.
    title: Disorders of the Cardiovascular System
    aliases:
    - cardiovascular disorder
    - cardiomyopathy
    - coronary artery disorder
    - vascular disease
    - cardiac channelopathy
  RESPIRATORY:
    text: RESPIRATORY
    description: Pulmonary diseases including obstructive lung disease (asthma, COPD),
      interstitial and restrictive lung disease, pulmonary vascular disease, and respiratory
      failure.
    title: Disorders of the Respiratory System
    aliases:
    - respiratory system disorder
    - obstructive lung disease
    - allergic disease
  CRITICAL_CARE:
    text: CRITICAL_CARE
    description: Approach to the critically ill patient, including sepsis and septic
      shock, ARDS, multi-organ failure, and neurologic critical illness.
    title: Critical Care Medicine
  KIDNEY_URINARY_TRACT:
    text: KIDNEY_URINARY_TRACT
    description: Renal and urinary tract diseases including glomerular and tubulointerstitial
      disorders, acute kidney injury, chronic kidney disease, electrolyte and acid-base
      disturbances, and urolithiasis.
    title: Disorders of the Kidney and Urinary Tract
    aliases:
    - kidney disorder
    - glomerular disease
    - epithelial channelopathy
  GASTROINTESTINAL:
    text: GASTROINTESTINAL
    description: Digestive-system disorders including esophageal, gastric, small-bowel,
      colonic, hepatic, biliary, and pancreatic disease.
    title: Disorders of the Gastrointestinal System
    aliases:
    - digestive system disorder
    - liver disorder
    - inflammatory bowel disease
    - peptic disorder
  IMMUNE_RHEUMATOLOGIC:
    text: IMMUNE_RHEUMATOLOGIC
    description: Autoimmune and immune-mediated conditions, connective-tissue diseases,
      vasculitides, and rheumatologic disorders. Musculoskeletal disorders are also
      covered here in Harrison's.
    title: Immune-Mediated, Inflammatory, and Rheumatologic Disorders
    aliases:
    - autoimmune disease
    - immune system disorder
    - connective tissue disease
    - inflammatory arthritis
    - collagenopathy
    - musculoskeletal system disorder
  ENDOCRINOLOGY_METABOLISM:
    text: ENDOCRINOLOGY_METABOLISM
    description: Endocrine and metabolic diseases including diabetes mellitus, thyroid,
      adrenal, pituitary, gonadal, calcium and bone metabolism, lipid disorders, and
      inborn errors of metabolism.
    title: Endocrinology and Metabolism
    aliases:
    - endocrine system disorder
    - diabetes mellitus
    - thyroid disorder
    - adrenal disorder
    - disorder of glycogen metabolism
    - glycoproteinosis
  NEUROLOGIC:
    text: NEUROLOGIC
    description: Diseases of the central and peripheral nervous system, including
      stroke, epilepsy, neurodegenerative disease, movement disorders, demyelinating
      disease, neuromuscular disease, headache, and psychiatric disorders.
    title: Neurologic Disorders
    aliases:
    - nervous system disorder
    - neurodegenerative disease
    - movement disorder
    - epilepsy
    - demyelinating disease
    - neuromuscular disease
    - psychiatric disorder
    - synucleinopathy
    - tauopathy
    - neurological channelopathy
    - skeletal muscle channelopathy
  DERMATOLOGY:
    text: DERMATOLOGY
    description: Skin and cutaneous disorders. In Harrison's 21st edition, dermatology
      is organized as a section within the cardinal manifestations Part; this enum
      value is provided separately so that disorders that are primarily dermatologic
      can be classified directly.
    title: Disorders of the Skin
    aliases:
    - skin disorder
  POISONING_ENVENOMATION:
    text: POISONING_ENVENOMATION
    description: Toxicology, poisoning syndromes, drug overdose, and bites or other
      venom exposures.
    title: Poisoning, Drug Overdose, and Envenomation
  ENVIRONMENTAL_EXPOSURES:
    text: ENVIRONMENTAL_EXPOSURES
    description: Disorders attributable to environmental exposures such as altitude,
      hypothermia/hyperthermia, drowning, and radiation injury.
    title: Disorders Associated with Environmental Exposures
  GENETICS_ENVIRONMENT_DISEASE:
    text: GENETICS_ENVIRONMENT_DISEASE
    description: Genetic and genomic medicine, chromosomal and Mendelian disorders
      not better classified by organ system, and the interplay of genes and environment
      in disease. Use for mechanism-defined entries (RASopathies, ciliopathies, mitochondrial
      disease, etc.) that span multiple organ systems.
    title: Genes, the Environment, and Disease
    aliases:
    - hereditary disease
    - RASopathy
    - ciliopathy
    - mitochondrial disease
    - intermediate filament disease
    - proteotoxic disease
  DISORDER_OF_EAR:
    text: DISORDER_OF_EAR
    description: Disorders of hearing and the vestibular system. Covered in Harrison's
      under cardinal-manifestation chapters on the ear.
    title: Disorders of the Ear
    aliases:
    - disorder of ear
  GLOBAL_MEDICINE:
    text: GLOBAL_MEDICINE
    description: Diseases and health issues that are predominantly addressed in a
      global health context.
    title: Global Medicine
  AGING:
    text: AGING
    description: Disorders, syndromes, and physiologic considerations specific to
      older adults.
    title: Aging
  CONSULTATIVE_MEDICINE:
    text: CONSULTATIVE_MEDICINE
    description: Approach to the patient when consulting across specialties (medical
      consultation in surgical patients, perioperative evaluation, etc.).
    title: Consultative Medicine
  OTHER:
    text: OTHER
    description: The disorder does not fit cleanly into any of the above Parts. Use
      sparingly and prefer the most relevant Part where possible.
    title: Other

```
</details>