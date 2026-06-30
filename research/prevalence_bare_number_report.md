# Bare-number prevalence resolution

Mode: APPLIED  
Files changed: 58  
- CONFIRMED: 91
- CONFIRMED_HIGH: 51
- NO_EVIDENCE: 12
- DISAGREE: 10
- MISPLACED_STAT: 35
- SKIP_GT100: 0

## MISPLACED_STAT — needs manual review (35)

| File | percentage | percent-reading /100k | evidence /100k |
|------|-----------|----------------------|----------------|
| Beta_Thalassemia.yaml | `1.5` | (None, None) | [] |
| Classic_Hodgkin_Lymphoma.yaml | `15-25` | (None, None) | [] |
| Clostridioides_difficile_Infection.yaml | `25` | (None, None) | [] |
| Congenital_Pulmonary_Airway_Malformation.yaml | `0.04` | (None, None) | [] |
| Delayed_Sleep_Phase_Syndrome.yaml | `0.2-10` | (None, None) | [] |
| Diabetes_Mellitus.yaml | `2` | (None, None) | [] |
| Diabetes_Mellitus.yaml | `90` | (None, None) | [] |
| FICUS_syndrome.yaml | `33` | (None, None) | [] |
| Hairy_Cell_Leukemia.yaml | `2` | (None, None) | [] |
| Mantle_Cell_Lymphoma.yaml | `6` | (None, None) | [] |
| Meckel_Diverticulum.yaml | `2` | (None, None) | [] |
| Meningioma.yaml | `40` | (None, None) | [] |
| Metastatic_Breast_Carcinoma.yaml | `30` | (None, None) | [] |
| Metastatic_Breast_Carcinoma.yaml | `46` | (None, None) | [] |
| Metastatic_Colorectal_Cancer.yaml | `20` | (None, None) | [] |
| Metastatic_Colorectal_Cancer.yaml | `20` | (None, None) | [] |
| Metastatic_Gastric_Cancer.yaml | `4` | (None, None) | [] |
| Metastatic_HCC.yaml | `13` | (None, None) | [] |
| Metastatic_Melanoma.yaml | `34.2` | (None, None) | [] |
| Metastatic_Melanoma.yaml | `60` | (None, None) | [] |
| Metastatic_NSCLC.yaml | `15.6` | (None, None) | [] |
| Metastatic_Ovarian_Cancer.yaml | `40` | (None, None) | [] |
| Metastatic_Ovarian_Cancer.yaml | `80` | (None, None) | [] |
| Metastatic_Prostate_Cancer.yaml | `10` | (None, None) | [] |
| Metastatic_Prostate_Cancer.yaml | `37` | (None, None) | [] |
| Metastatic_Renal_Cell_Carcinoma.yaml | `8.2` | (None, None) | [] |
| Mycosis_Fungoides.yaml | `60` | (None, None) | [] |
| Omphalocele.yaml | `0.0098` | (None, None) | [] |
| Peripheral_T_Cell_Lymphoma.yaml | `10` | (None, None) | [] |
| Pleuropulmonary_Blastoma.yaml | `0.3` | (None, None) | [] |
| Prostate_Adenocarcinoma.yaml | `75` | (None, None) | [] |
| Prostate_Adenocarcinoma.yaml | `99` | (None, None) | [] |
| Refeeding_Syndrome.yaml | `38.8` | (None, None) | [] |
| Treacher_Collins_Syndrome.yaml | `0.002` | (None, None) | [] |
| Type_I_Diabetes.yaml | `0.1-0.2` | (None, None) | [] |

## CONFIRMED_HIGH — needs manual review (51)

| File | percentage | percent-reading /100k | evidence /100k |
|------|-----------|----------------------|----------------|
| Achoo_Syndrome.yaml | `25.6` | 25600.0 | [30100.0, 21100.0, 25600.0] |
| Achoo_Syndrome.yaml | `3.1` | 3100.0 | [3100.0] |
| Acne_Vulgaris.yaml | `20` | 20000.0 | [20000.0] |
| Acne_Vulgaris.yaml | `57.8` | 57800.0 | [57800.0, 95000.0, 56900.0] |
| Acne_Vulgaris.yaml | `9.79` | 9790.0 | [95000.0, 95000.0, 95000.0] |
| Acute_Hypotension.yaml | `88` | 88000.0 | [88000.0, 83200.0, 91600.0] |
| Anorexia_Nervosa.yaml | `2.58` | 2580.0 | [2200.0, 8400.0] |
| Autism_Spectrum_Disorder.yaml | `2.78` | 2780.0 | [2780.0, 2777.8] |
| Campylobacteriosis.yaml | `39` | 39000.0 | [39000.0] |
| Cholesteatoma.yaml | `24.5` | 24500.0 | [24500.0] |
| Chronic_Obstructive_Pulmonary_Disease.yaml | `11.7` | 11700.0 | [11100.0, 95000.0, 14800.0] |
| Conduct_Disorder.yaml | `3` | 3000.0 | [3000.0, 3000.0, 4000.0] |
| Contact_Dermatitis.yaml | `15.0` | 15000.0 | [15100.0, 3000.0, 2000.0] |
| Contact_Dermatitis.yaml | `15.0` | 15000.0 | [15000.0] |
| Coronary_Vasospasm.yaml | `43` | 43000.0 | [43000.0, 73000.0, 52000.0] |
| Delayed_Sleep_Phase_Syndrome.yaml | `3` | 3000.0 | [3000.0] |
| Dental_Fluorosis.yaml | `18.3` | 18300.0 | [15600.0, 95000.0, 13200.0] |
| Dental_Fluorosis.yaml | `23` | 23000.0 | [23000.0, 66500.0] |
| Dientamoebiasis.yaml | `0.3-82.9` | (300.0, 82900.0) | [300.0, 82900.0, 300.0] |
| Dientamoebiasis.yaml | `32.5` | 32500.0 | [32500.0, 32500.0, 7900.0] |
| FICUS_syndrome.yaml | `45.8` | 45800.0 | [45800.0, 25000.0, 11100.0] |
| Gilberts_Syndrome.yaml | `2-19` | (2000.0, 19000.0) | [19000.0] |
| Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml | `10` | 10000.0 | [9700.0, 9728.2] |
| Hepatitis_B.yaml | `3.5` | 3500.0 | [3610.0, 95000.0] |
| Kummell_Disease.yaml | `6.3` | 6300.0 | [6300.0, 29900.0] |
| Lathyrism.yaml | `2.4` | 2400.0 | [9200.0, 2400.0, 9200.0] |
| Lathyrism.yaml | `6.6` | 6600.0 | [11900.0, 6600.0, 11900.0] |
| Lead_Poisoning.yaml | `2.2` | 2200.0 | [2200.0] |
| Lead_Poisoning.yaml | `87` | 87000.0 | [87000.0] |
| Leri-Weill_Dyschondrosteosis.yaml | `4.2` | 4200.0 | [4200.0, 4200.0] |
| MYO6_Hearing_Loss.yaml | `2.4` | 2400.0 | [2400.0, 2400.0] |
| Malignant_Non_Dysgerminomatous_Germ_Cell_Tumor_Of_Ovary.yaml | `2-5` | (2000.0, 5000.0) | [5000.0] |
| Mantle_Cell_Lymphoma.yaml | `3-10` | (3000.0, 10000.0) | [3000.0, 10000.0] |
| Migraine_with_Aura.yaml | `5` | 5000.0 | [5000.0, 5000.0, 50000.0] |
| Morgagni-Stewart-Morel_Syndrome.yaml | `2.5` | 2500.0 | [2500.0, 22000.0, 2200.0] |
| Obsessive-Compulsive_Disorder.yaml | `3.0` | 3000.0 | [4100.0, 3000.0] |
| Obsessive-Compulsive_Disorder.yaml | `4.1` | 4100.0 | [3000.0, 4100.0, 3000.0] |
| Oppositional_Defiant_Disorder.yaml | `21.9` | 21900.0 | [21900.0] |
| Osteoarthritis.yaml | `7.6` | 7600.0 | [95000.0, 6000.0, 95000.0] |
| Post-Traumatic_Stress_Disorder.yaml | `23.7` | 23700.0 | [23700.0, 95000.0, 19500.0] |
| Post-Traumatic_Stress_Disorder.yaml | `23.95` | 23950.0 | [23950.0, 95000.0, 95000.0] |
| Posterior_Myocardial_Infarction.yaml | `3-7` | (3000.0, 7000.0) | [7000.0] |
| Premenstrual_Dysphoric_Disorder.yaml | `3.2` | 3200.0 | [3200.0, 95000.0, 1700.0] |
| Premenstrual_Dysphoric_Disorder.yaml | `7.7` | 7700.0 | [3200.0, 95000.0, 1700.0] |
| Raynaud_Disease.yaml | `3.0` | 3000.0 | [5000.0, 3000.0, 5000.0] |
| Refeeding_Syndrome.yaml | `33.3` | 33300.0 | [33300.0] |
| Refeeding_Syndrome.yaml | `8.7-34.8` | (8700.0, 34800.0) | [8700.0, 34800.0] |
| Taurodontism.yaml | `11.8` | 11800.0 | [11800.0] |
| Taurodontism.yaml | `29.14` | 29140.0 | [29140.0, 27240.0, 30650.0] |
| Taurodontism.yaml | `8` | 8000.0 | [8000.0, 3900.0] |
| Twin_to_Twin_Transfusion_Syndrome.yaml | `10-15` | (10000.0, 15000.0) | [15000.0, 15000.0, 50.0] |

## DISAGREE — needs manual review (10)

| File | percentage | percent-reading /100k | evidence /100k |
|------|-----------|----------------------|----------------|
| Axenfeld-Rieger_syndrome.yaml | `0.001-0.002` | (1.0, 2.0) | [260.0, 390.0] |
| Cockayne_Syndrome.yaml | `4e-06` | 0.004 | [0.4, 0.3] |
| Crohn_Disease.yaml | `0.2-0.3` | (200.0, 300.0) | [47000.0] |
| Ehlers-Danlos_Syndrome_COL5A1-related.yaml | `0.002-0.01` | (2.0, 10.0) | [50000.0] |
| Epidermolysis_Bullosa.yaml | `0.0008` | 0.8 | [822000.0] |
| Familial_Mediterranean_Fever.yaml | `0.1-0.2` | (100.0, 200.0) | [41800.0, 15800.0, 6500.0] |
| Hirschsprung_Disease.yaml | `0.0001-0.001` | (0.1, 1.0) | [95000.0] |
| Nephronophthisis.yaml | `0.1-1.0` | (100.0, 1000.0) | [10000.0, 20000.0, 6000.0] |
| Neuromyelitis_Optica.yaml | `0.00154` | 1.54 | [54.0, 16.0, 99553.3] |
| Tuberculosis.yaml | `0.1` | 100.0 | [30660.0, 23670.0, 900.0] |

## NO_EVIDENCE — needs manual review (12)

| File | percentage | percent-reading /100k | evidence /100k |
|------|-----------|----------------------|----------------|
| Acquired_Immunodeficiency_Syndrome.yaml | `0.7` | 700.0 | [] |
| Arsenic_Poisoning.yaml | `12.6` | 12600.0 | [] |
| CHIME_syndrome.yaml | `1e-06` | 0.001 | [] |
| Diamond-Blackfan_Anemia.yaml | `0.0007` | 0.7 | [] |
| Down_syndrome.yaml | `0.1` | 100.0 | [] |
| Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml | `4.9` | 4900.0 | [] |
| Grange_syndrome.yaml | `1e-05` | 0.01 | [] |
| Hypertensive_Heart_Disease.yaml | `10-20` | (10000.0, 20000.0) | [] |
| Jeavons_Syndrome.yaml | `0.0001` | 0.1 | [] |
| Pick_Disease.yaml | `0.002-0.004` | (2.0, 4.0) | [] |
| Plague.yaml | `3e-05` | 0.03 | [] |
| Schizophrenia.yaml | `0.3-0.7` | (300.0, 700.0) | [] |
