# Enum: HarrisonsChapterEnum 




_Traditional internal medicine chapter groupings for disease classification. Based on Harrison's Principles of Internal Medicine organization. Sub-chapters use is_a to indicate parent category._



URI: [dismech:HarrisonsChapterEnum](https://w3id.org/monarch-initiative/dismech/HarrisonsChapterEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| cardiovascular disorder | MONDO:0004995 | Heart and vascular diseases, including ischemic, structural, rhythm, and vasc... |
| coronary artery disorder | MONDO:0005010 | Ischemic heart disease due to coronary artery pathology; includes myocardial ... |
| cardiomyopathy | MONDO:0004994 | Primary diseases of the myocardium affecting systolic or diastolic function |
| cardiac rhythm disease | MONDO:0007263 | Electrical conduction or rhythm disorders causing arrhythmias or heart block |
| valvular heart disease | MONDO:0002869 | Structural or functional valve disease (stenosis or regurgitation) affecting ... |
| vascular disease | MONDO:0005385 | Arterial or venous disorders such as aneurysm, peripheral artery disease, or ... |
| respiratory system disorder | MONDO:0005087 | Diseases of airways, lung parenchyma, and pleura that impair ventilation or g... |
| obstructive lung disease | MONDO:0002267 | Airflow limitation from airway narrowing or collapse, including COPD and asth... |
| interstitial lung disease | MONDO:0015925 | Diffuse parenchymal lung disorders with inflammation or fibrosis that reduce ... |
| pulmonary vascular disease | None | Pulmonary arterial or venous vascular disorders, including hypertension and e... |
| digestive system disorder | MONDO:0004335 | Diseases of the gastrointestinal tract and accessory organs affecting digesti... |
| inflammatory bowel disease | MONDO:0005265 | Chronic immune-mediated intestinal inflammation, typically Crohn disease or u... |
| peptic disorder | MONDO:0004247 | Acid-related disorders of the esophagus, stomach, or duodenum such as GERD an... |
| liver disorder | MONDO:0005154 | Hepatobiliary diseases involving liver parenchyma, bile ducts, or gallbladder |
| kidney disorder | MONDO:0005240 | Renal and urinary tract diseases affecting filtration, electrolyte balance, o... |
| glomerular disease | MONDO:0019722 | Diseases of the glomerulus causing hematuria, proteinuria, or nephrotic/nephr... |
| hematologic disorder | MONDO:0005570 | Disorders of blood cells, bone marrow, and hemostasis |
| anemia | MONDO:0002280 | Reduced red cell mass or hemoglobin due to production defects, blood loss, or... |
| coagulation disorder | MONDO:0001531 | Bleeding or thrombotic disorders from clotting factor, platelet, or regulator... |
| cancer | MONDO:0004992 | Neoplastic diseases characterized by uncontrolled cell proliferation and inva... |
| hematologic malignancy | MONDO:0002334 | Cancers of blood, bone marrow, and lymphoid tissues such as leukemia or lymph... |
| solid tumor | None | Non-hematologic neoplasms arising in organs or soft tissues |
| infectious disease | MONDO:0005550 | Illness caused by pathogenic organisms with host invasion and immune response |
| bacterial infectious disease | MONDO:0005113 | Infections caused by bacteria, including community and healthcare-associated ... |
| viral infectious disease | MONDO:0005108 | Infections caused by viruses affecting any organ system |
| fungal infectious disease | MONDO:0002041 | Mycoses ranging from superficial to invasive systemic infections |
| parasitic infectious disease | MONDO:0005135 | Protozoal or helminth infections, often vector-borne or food/water transmitte... |
| mycobacterial infection | MONDO:0020590 | Infections due to Mycobacterium species, including tuberculosis and non-tuber... |
| immune system disorder | MONDO:0005046 | Immune dysregulation disorders including autoimmunity, immunodeficiency, or h... |
| autoimmune disease | MONDO:0007179 | Immune-mediated tissue damage due to loss of self-tolerance |
| allergic disease | MONDO:0005271 | Hypersensitivity disorders including atopy, allergic asthma, and anaphylaxis |
| endocrine system disorder | MONDO:0005151 | Hormonal and metabolic gland disorders affecting systemic homeostasis |
| diabetes mellitus | MONDO:0005015 | Disorders of glucose regulation due to insulin deficiency and/or insulin resi... |
| thyroid disorder | MONDO:0003240 | Thyroid gland dysfunction or structural disease altering metabolic control |
| adrenal disorder | MONDO:0005495 | Adrenal cortex or medulla disorders causing hormone excess or deficiency |
| nervous system disorder | MONDO:0005071 | Central or peripheral nervous system diseases affecting cognition, sensation,... |
| cerebrovascular disorder | MONDO:0011057 | Brain ischemia or hemorrhage due to vascular disease, including stroke and TI... |
| neurodegenerative disease | MONDO:0005559 | Progressive neuronal loss leading to cognitive or motor decline |
| demyelinating disease | MONDO:0002562 | Disorders with loss of myelin in the nervous system, often immune-mediated |
| neuromuscular disease | MONDO:0019056 | Diseases of peripheral nerve, neuromuscular junction, or muscle leading to we... |
| epilepsy | MONDO:0005027 | Recurrent unprovoked seizures from abnormal neuronal activity |
| movement disorder | MONDO:0005395 | Motor control disorders causing tremor, rigidity, dystonia, chorea, or ataxia |
| musculoskeletal system disorder | MONDO:0002081 | Diseases of joints, bones, muscles, or connective tissue |
| inflammatory arthritis | None | Inflammatory joint disorders with synovitis, such as RA or spondyloarthropath... |
| connective tissue disease | MONDO:0003900 | Systemic autoimmune connective tissue disorders affecting skin, joints, vesse... |
| skin disorder | MONDO:0005093 | Diseases of the skin, hair, nails, and related appendages |
| psychiatric disorder | MONDO:0002025 | Mental and behavioral disorders affecting mood, thought, or behavior |
| hereditary disease | MONDO:0003847 | Genetic or congenital disorders due to inherited variants or developmental an... |




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
name: HarrisonsChapterEnum
description: Traditional internal medicine chapter groupings for disease classification.
  Based on Harrison's Principles of Internal Medicine organization. Sub-chapters use
  is_a to indicate parent category.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  cardiovascular disorder:
    text: cardiovascular disorder
    description: Heart and vascular diseases, including ischemic, structural, rhythm,
      and vascular conditions.
    meaning: MONDO:0004995
    title: Diseases of the heart and blood vessels
  coronary artery disorder:
    text: coronary artery disorder
    description: Ischemic heart disease due to coronary artery pathology; includes
      myocardial infarction and angina.
    meaning: MONDO:0005010
    is_a: cardiovascular disorder
    title: Ischemic heart disease, myocardial infarction, angina
  cardiomyopathy:
    text: cardiomyopathy
    description: Primary diseases of the myocardium affecting systolic or diastolic
      function.
    meaning: MONDO:0004994
    is_a: cardiovascular disorder
    title: Diseases of heart muscle (dilated, hypertrophic, restrictive)
  cardiac rhythm disease:
    text: cardiac rhythm disease
    description: Electrical conduction or rhythm disorders causing arrhythmias or
      heart block.
    meaning: MONDO:0007263
    is_a: cardiovascular disorder
    title: Arrhythmias, conduction disorders
  valvular heart disease:
    text: valvular heart disease
    description: Structural or functional valve disease (stenosis or regurgitation)
      affecting cardiac hemodynamics.
    meaning: MONDO:0002869
    is_a: cardiovascular disorder
    title: Diseases of heart valves (stenosis, regurgitation)
  vascular disease:
    text: vascular disease
    description: Arterial or venous disorders such as aneurysm, peripheral artery
      disease, or thrombosis.
    meaning: MONDO:0005385
    is_a: cardiovascular disorder
    title: Diseases of arteries and veins (aneurysm, PAD, DVT)
  respiratory system disorder:
    text: respiratory system disorder
    description: Diseases of airways, lung parenchyma, and pleura that impair ventilation
      or gas exchange.
    meaning: MONDO:0005087
    title: Diseases of the lungs and airways
  obstructive lung disease:
    text: obstructive lung disease
    description: Airflow limitation from airway narrowing or collapse, including COPD
      and asthma.
    meaning: MONDO:0002267
    is_a: respiratory system disorder
    title: COPD, asthma, bronchiectasis
  interstitial lung disease:
    text: interstitial lung disease
    description: Diffuse parenchymal lung disorders with inflammation or fibrosis
      that reduce gas exchange.
    meaning: MONDO:0015925
    is_a: respiratory system disorder
    title: Pulmonary fibrosis, sarcoidosis
  pulmonary vascular disease:
    text: pulmonary vascular disease
    description: Pulmonary arterial or venous vascular disorders, including hypertension
      and embolism.
    is_a: respiratory system disorder
    title: Pulmonary hypertension, pulmonary embolism
  digestive system disorder:
    text: digestive system disorder
    description: Diseases of the gastrointestinal tract and accessory organs affecting
      digestion or absorption.
    meaning: MONDO:0004335
    title: Diseases of the digestive tract and accessory organs
  inflammatory bowel disease:
    text: inflammatory bowel disease
    description: Chronic immune-mediated intestinal inflammation, typically Crohn
      disease or ulcerative colitis.
    meaning: MONDO:0005265
    is_a: digestive system disorder
    title: Crohn's disease, ulcerative colitis
  peptic disorder:
    text: peptic disorder
    description: Acid-related disorders of the esophagus, stomach, or duodenum such
      as GERD and peptic ulcer disease.
    meaning: MONDO:0004247
    is_a: digestive system disorder
    title: Peptic ulcer, GERD, gastritis
  liver disorder:
    text: liver disorder
    description: Hepatobiliary diseases involving liver parenchyma, bile ducts, or
      gallbladder.
    meaning: MONDO:0005154
    title: Diseases of the liver, gallbladder, and biliary system
  kidney disorder:
    text: kidney disorder
    description: Renal and urinary tract diseases affecting filtration, electrolyte
      balance, or urine flow.
    meaning: MONDO:0005240
    title: Diseases of the kidneys and urinary system
  glomerular disease:
    text: glomerular disease
    description: Diseases of the glomerulus causing hematuria, proteinuria, or nephrotic/nephritic
      syndromes.
    meaning: MONDO:0019722
    is_a: kidney disorder
    title: Glomerulonephritis, nephrotic syndrome
  hematologic disorder:
    text: hematologic disorder
    description: Disorders of blood cells, bone marrow, and hemostasis.
    meaning: MONDO:0005570
    title: Diseases of blood and blood-forming organs
  anemia:
    text: anemia
    description: Reduced red cell mass or hemoglobin due to production defects, blood
      loss, or hemolysis.
    meaning: MONDO:0002280
    is_a: hematologic disorder
    title: Red blood cell disorders
  coagulation disorder:
    text: coagulation disorder
    description: Bleeding or thrombotic disorders from clotting factor, platelet,
      or regulatory defects.
    meaning: MONDO:0001531
    is_a: hematologic disorder
    title: Bleeding and thrombotic disorders
  cancer:
    text: cancer
    description: Neoplastic diseases characterized by uncontrolled cell proliferation
      and invasion.
    meaning: MONDO:0004992
    title: Neoplastic diseases and cancer
  hematologic malignancy:
    text: hematologic malignancy
    description: Cancers of blood, bone marrow, and lymphoid tissues such as leukemia
      or lymphoma.
    meaning: MONDO:0002334
    is_a: cancer
    title: Leukemia, lymphoma, myeloma
  solid tumor:
    text: solid tumor
    description: Non-hematologic neoplasms arising in organs or soft tissues.
    is_a: cancer
    title: Carcinomas, sarcomas, other solid neoplasms
  infectious disease:
    text: infectious disease
    description: Illness caused by pathogenic organisms with host invasion and immune
      response.
    meaning: MONDO:0005550
    title: Diseases caused by pathogenic microorganisms
  bacterial infectious disease:
    text: bacterial infectious disease
    description: Infections caused by bacteria, including community and healthcare-associated
      pathogens.
    meaning: MONDO:0005113
    is_a: infectious disease
    title: Infections caused by bacteria
  viral infectious disease:
    text: viral infectious disease
    description: Infections caused by viruses affecting any organ system.
    meaning: MONDO:0005108
    is_a: infectious disease
    title: Infections caused by viruses
  fungal infectious disease:
    text: fungal infectious disease
    description: Mycoses ranging from superficial to invasive systemic infections.
    meaning: MONDO:0002041
    is_a: infectious disease
    title: Infections caused by fungi
  parasitic infectious disease:
    text: parasitic infectious disease
    description: Protozoal or helminth infections, often vector-borne or food/water
      transmitted.
    meaning: MONDO:0005135
    is_a: infectious disease
    title: Infections caused by parasites (protozoa, helminths)
  mycobacterial infection:
    text: mycobacterial infection
    description: Infections due to Mycobacterium species, including tuberculosis and
      non-tuberculous mycobacteria.
    meaning: MONDO:0020590
    is_a: infectious disease
    title: Tuberculosis, NTM, leprosy
  immune system disorder:
    text: immune system disorder
    description: Immune dysregulation disorders including autoimmunity, immunodeficiency,
      or hypersensitivity.
    meaning: MONDO:0005046
    title: Diseases of the immune system including autoimmunity
  autoimmune disease:
    text: autoimmune disease
    description: Immune-mediated tissue damage due to loss of self-tolerance.
    meaning: MONDO:0007179
    is_a: immune system disorder
    title: Diseases caused by immune attack on self
  allergic disease:
    text: allergic disease
    description: Hypersensitivity disorders including atopy, allergic asthma, and
      anaphylaxis.
    meaning: MONDO:0005271
    is_a: immune system disorder
    title: Hypersensitivity disorders, anaphylaxis
  endocrine system disorder:
    text: endocrine system disorder
    description: Hormonal and metabolic gland disorders affecting systemic homeostasis.
    meaning: MONDO:0005151
    title: Diseases of hormonal and metabolic systems
  diabetes mellitus:
    text: diabetes mellitus
    description: Disorders of glucose regulation due to insulin deficiency and/or
      insulin resistance.
    meaning: MONDO:0005015
    is_a: endocrine system disorder
    title: Type 1, type 2, and other forms of diabetes
  thyroid disorder:
    text: thyroid disorder
    description: Thyroid gland dysfunction or structural disease altering metabolic
      control.
    meaning: MONDO:0003240
    is_a: endocrine system disorder
    title: Hyper/hypothyroidism, thyroid nodules, thyroid cancer
  adrenal disorder:
    text: adrenal disorder
    description: Adrenal cortex or medulla disorders causing hormone excess or deficiency.
    meaning: MONDO:0005495
    is_a: endocrine system disorder
    title: Cushing's, Addison's, pheochromocytoma
  nervous system disorder:
    text: nervous system disorder
    description: Central or peripheral nervous system diseases affecting cognition,
      sensation, or movement.
    meaning: MONDO:0005071
    title: Diseases of the central and peripheral nervous system
  cerebrovascular disorder:
    text: cerebrovascular disorder
    description: Brain ischemia or hemorrhage due to vascular disease, including stroke
      and TIA.
    meaning: MONDO:0011057
    is_a: nervous system disorder
    title: Stroke, TIA, vascular dementia
  neurodegenerative disease:
    text: neurodegenerative disease
    description: Progressive neuronal loss leading to cognitive or motor decline.
    meaning: MONDO:0005559
    is_a: nervous system disorder
    title: Alzheimer's, Parkinson's, ALS, Huntington's
  demyelinating disease:
    text: demyelinating disease
    description: Disorders with loss of myelin in the nervous system, often immune-mediated.
    meaning: MONDO:0002562
    is_a: nervous system disorder
    title: Multiple sclerosis, NMO, ADEM
  neuromuscular disease:
    text: neuromuscular disease
    description: Diseases of peripheral nerve, neuromuscular junction, or muscle leading
      to weakness.
    meaning: MONDO:0019056
    is_a: nervous system disorder
    title: Myopathies, neuropathies, NMJ disorders
  epilepsy:
    text: epilepsy
    description: Recurrent unprovoked seizures from abnormal neuronal activity.
    meaning: MONDO:0005027
    is_a: nervous system disorder
    title: Seizure disorders
  movement disorder:
    text: movement disorder
    description: Motor control disorders causing tremor, rigidity, dystonia, chorea,
      or ataxia.
    meaning: MONDO:0005395
    is_a: nervous system disorder
    title: Parkinsonism, dystonia, chorea, ataxia
  musculoskeletal system disorder:
    text: musculoskeletal system disorder
    description: Diseases of joints, bones, muscles, or connective tissue.
    meaning: MONDO:0002081
    title: Diseases of joints, connective tissue, and musculoskeletal system
  inflammatory arthritis:
    text: inflammatory arthritis
    description: Inflammatory joint disorders with synovitis, such as RA or spondyloarthropathies.
    is_a: musculoskeletal system disorder
    title: Rheumatoid arthritis, spondyloarthritis, gout
  connective tissue disease:
    text: connective tissue disease
    description: Systemic autoimmune connective tissue disorders affecting skin, joints,
      vessels, and organs.
    meaning: MONDO:0003900
    is_a: musculoskeletal system disorder
    title: SLE, scleroderma, Sjogren's, vasculitis
  skin disorder:
    text: skin disorder
    description: Diseases of the skin, hair, nails, and related appendages.
    meaning: MONDO:0005093
    title: Diseases of the skin and appendages
  psychiatric disorder:
    text: psychiatric disorder
    description: Mental and behavioral disorders affecting mood, thought, or behavior.
    meaning: MONDO:0002025
    title: Mental and behavioral disorders
  hereditary disease:
    text: hereditary disease
    description: Genetic or congenital disorders due to inherited variants or developmental
      anomalies.
    meaning: MONDO:0003847
    title: Inherited diseases and birth defects

```
</details>