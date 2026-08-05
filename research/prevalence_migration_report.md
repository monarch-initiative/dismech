# Prevalence migration report

Mode: APPLIED (files written)  
Total prevalence records: **834**  
Files changed: **11**  

## Outcome breakdown

| Flag | Count | Meaning |
|------|------:|---------|
| AMBIGUOUS_BARE_NUMBER | 199 | Bare number/range with no unit — NOT converted, needs manual unit. |
| OK | 194 | Numeric rate parsed; measure type stated. |
| NO_PERCENTAGE | 154 | Record had no percentage value; left untouched. |
| QUALITATIVE | 149 | No number; mapped to a qualitative prevalence_class. |
| OK_MEASURE_INFERRED | 127 | Numeric rate parsed; measure type defaulted to POINT_PREVALENCE (verify). |
| UNPARSED_PROSE | 11 | Free prose / head-count not auto-convertible — needs manual review. |

## Records needing manual review — ambiguous bare numbers (199)

`percentage` is bare (no unit). Hints show cases/100,000 under each reading: **as %** (value x1000) vs **as proportion** (value x100,000). Pick one, then set rate_per_100000/prevalence_class.

| File | population | percentage (raw) | as % -> /100k | as proportion -> /100k |
|------|------------|------------------|---------------|------------------------|
| 2-Methylbutyryl-CoA_Dehydrogenase_Deficiency.yaml | 'Hmong (Wisconsin, USA)' | '1.3' | 1300 | 130000 |
| Achoo_Syndrome.yaml | 'Chinese' | '25.6' | 25600 | 2.56e+06 |
| Achoo_Syndrome.yaml | 'Japanese' | '3.1' | 3100 | 310000 |
| Acne_Vulgaris.yaml | 'Adolescents and young adults (Europe, ages 15-24 years)' | '57.8' | 57800 | 5.78e+06 |
| Acne_Vulgaris.yaml | 'Adolescents and young adults (global, ages 10-24 years, 2021)' | '9.79' | 9790 | 979000 |
| Acne_Vulgaris.yaml | 'Young people (moderate-to-severe acne)' | '20' | 20000 | 2e+06 |
| Acquired_Immunodeficiency_Syndrome.yaml | 'Global' | '0.7' | 700 | 70000 |
| Acute_Hypotension.yaml | 'Moderate-to-high-risk (ASA 3-4) non-cardiac surgical patients' | '88' | 88000 | 8.8e+06 |
| Adult-Onset_Still_Disease.yaml | 'Japan' | '0.0039' | 3.9 | 390 |
| Adult-Onset_Still_Disease.yaml | 'Western Australia' | '0.0024' | 2.4 | 240 |
| Alagille_syndrome.yaml | 'Europe (Orphanet prevalence at birth)' | '0.0001-0.001' | 0.1 | 10 |
| Alagille_syndrome.yaml | 'United States (Orphanet prevalence at birth)' | '0.001-0.01' | 1 | 100 |
| Anorexia_Nervosa.yaml | 'global eating-disorder populations' | '2.58' | 2580 | 258000 |
| Antiphospholipid_Syndrome.yaml | 'Global' | '0.05' | 50 | 5000 |
| Apert_Syndrome.yaml | 'California live births' | '0.00124' | 1.24 | 124 |
| Apert_Syndrome.yaml | 'Pooled multi-registry birth cohorts' | '0.00155' | 1.55 | 155 |
| Apert_Syndrome.yaml | 'Spain live births' | '0.0011' | 1.1 | 110 |
| Arsenic_Poisoning.yaml | 'Bangladesh' | '12.6' | 12600 | 1.26e+06 |
| Autism_Spectrum_Disorder.yaml | 'China' | '0.7' | 700 | 70000 |
| Autism_Spectrum_Disorder.yaml | 'Turkey (Istanbul)' | '0.9' | 900 | 90000 |
| Autism_Spectrum_Disorder.yaml | 'United States' | '2.78' | 2780 | 278000 |
| Axenfeld-Rieger_syndrome.yaml | 'General Population' | '0.001-0.002' | 1 | 100 |
| Beta_Thalassemia.yaml | 'Global carriers' | '1.5' | 1500 | 150000 |
| Binge_Eating_Disorder.yaml | 'U.S. early adolescents aged 10 to 14 years' | '1.0' | 1000 | 100000 |
| Bird_Fanciers_Lung.yaml | 'United Kingdom' | '0.001' | 1 | 100 |
| Body_Dysmorphic_Disorder.yaml | 'Community samples' | '2.0' | 2000 | 200000 |
| Borderline_Personality_Disorder.yaml | 'General population' | '1.8' | 1800 | 180000 |
| CHIME_syndrome.yaml | 'Global' | '1e-06' | 0.001 | 0.1 |
| Campylobacteriosis.yaml | 'Finland domestic cases (pilot case-control study, 2022)' | '39' | 39000 | 3.9e+06 |
| Celiac_Disease.yaml | 'General' | '1.0' | 1000 | 100000 |
| Cholesteatoma.yaml | 'Chronic otitis media patients at a Brazilian referral hospital' | '24.5' | 24500 | 2.45e+06 |
| Chronic_Obstructive_Pulmonary_Disease.yaml | 'Global' | '11.7' | 11700 | 1.17e+06 |
| Classic_Hodgkin_Lymphoma.yaml | 'All lymphomas in the Western world' | '15-25' | 15000 | 1.5e+06 |
| Clostridioides_difficile_Infection.yaml | 'Adults after an initial CDI episode' | '25' | 25000 | 2.5e+06 |
| Cockayne_Syndrome.yaml | 'United States' | '4e-06' | 0.004 | 0.4 |
| Cockayne_Syndrome.yaml | 'Western Europe' | '0.00027' | 0.27 | 27 |
| Conduct_Disorder.yaml | 'community children and adolescents' | '3' | 3000 | 300000 |
| Congenital_Hypothyroidism.yaml | 'Worldwide (central CH)' | '0.006' | 6 | 600 |
| Congenital_Hypothyroidism.yaml | 'Worldwide (primary CH)' | '0.04' | 40 | 4000 |
| Congenital_Pulmonary_Airway_Malformation.yaml | 'Europe' | '0.0106' | 10.6 | 1060 |
| Congenital_Pulmonary_Airway_Malformation.yaml | 'Global (Congenital Lung Malformations)' | '0.04' | 40 | 4000 |
| Contact_Dermatitis.yaml | 'Adults from five European countries' | '15.0' | 15000 | 1.5e+06 |
| Contact_Dermatitis.yaml | 'General population over a lifetime' | '15.0' | 15000 | 1.5e+06 |
| Coronary_Vasospasm.yaml | 'ANOCA patients undergoing spasm provocation testing' | '43' | 43000 | 4.3e+06 |
| Crohn_Disease.yaml | 'Global' | '0.2-0.3' | 200 | 20000 |
| Delayed_Sleep_Phase_Syndrome.yaml | 'Global' | '0.2-10' | 200 | 20000 |
| Delayed_Sleep_Phase_Syndrome.yaml | 'Global' | '3' | 3000 | 300000 |
| Dental_Fluorosis.yaml | 'Brazil meta-analysis' | '18.3' | 18300 | 1.83e+06 |
| Dental_Fluorosis.yaml | 'Primary dentition twin cohort' | '23' | 23000 | 2.3e+06 |
| Diabetes_Mellitus.yaml | 'Global' | '2' | 2000 | 200000 |
| Diabetes_Mellitus.yaml | 'Global' | '90' | 90000 | 9e+06 |
| Diamond-Blackfan_Anemia.yaml | 'Global' | '0.0007' | 0.7 | 70 |
| Dientamoebiasis.yaml | 'Global' | '0.3-82.9' | 300 | 30000 |
| Dientamoebiasis.yaml | 'Israeli pediatric population' | '32.5' | 32500 | 3.25e+06 |
| Down_syndrome.yaml | 'Global' | '0.1' | 100 | 10000 |
| Ehlers-Danlos_Syndrome.yaml | 'Global' | '0.02' | 20 | 2000 |
| Ehlers-Danlos_Syndrome_COL5A1-related.yaml | 'Global' | '0.002-0.01' | 2 | 200 |
| Epidermolysis_Bullosa.yaml | 'Germany' | '0.0054' | 5.4 | 540 |
| Epidermolysis_Bullosa.yaml | 'United States' | '0.0008' | 0.8 | 80 |
| FICUS_syndrome.yaml | 'Family decision-makers of critically ill patients (single-center, United States)' | '45.8' | 45800 | 4.58e+06 |
| FICUS_syndrome.yaml | 'ICU family members of COVID-19 patients (single-center, Japan)' | '33' | 33000 | 3.3e+06 |
| Fabry_Disease.yaml | 'Europe (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Fabry_Disease.yaml | 'Worldwide (Orphanet prevalence at birth)' | '0.0001-0.0009' | 0.1 | 10 |
| Familial_Hypercholesterolemia.yaml | 'Global (heterozygous)' | '0.3-0.4' | 300 | 30000 |
| Familial_Hypercholesterolemia.yaml | 'Global (homozygous)' | '0.0003-0.0006' | 0.3 | 30 |
| Familial_Mediterranean_Fever.yaml | 'Mediterranean Populations' | '0.1-0.2' | 100 | 10000 |
| Friedreich_Ataxia.yaml | 'Global' | '0.003' | 3 | 300 |
| Gilberts_Syndrome.yaml | 'Population studies' | '2-19' | 2000 | 200000 |
| Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml | 'African Americans' | '10' | 10000 | 1e+06 |
| Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml | 'Global' | '4.9' | 4900 | 490000 |
| Grange_syndrome.yaml | 'Global' | '1e-05' | 0.01 | 1 |
| Graves_Disease.yaml | 'Global' | '0.5-1' | 500 | 50000 |
| Hairy_Cell_Leukemia.yaml | 'All leukemia cases' | '2' | 2000 | 200000 |
| Hepatitis_B.yaml | 'Global' | '3.5' | 3500 | 350000 |
| Hereditary_Elliptocytosis.yaml | 'Worldwide' | '0.01-0.05' | 10 | 1000 |
| Hereditary_Hemorrhagic_Telangiectasia.yaml | 'Global' | '0.02' | 20 | 2000 |
| Hereditary_Spherocytosis.yaml | 'Europe (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Hereditary_Spherocytosis.yaml | 'Germany' | '0.01-0.05' | 10 | 1000 |
| Hereditary_Spherocytosis.yaml | 'United States (Orphanet prevalence at birth)' | '0.01-0.05' | 10 | 1000 |
| Hereditary_von_Willebrand_Disease.yaml | 'General population screening cohorts' | '1' | 1000 | 100000 |
| Hidradenitis_Suppurativa.yaml | 'Global' | '1.0' | 1000 | 100000 |
| Hidradenitis_Suppurativa.yaml | 'Spain' | '1.0' | 1000 | 100000 |
| Hirschsprung_Disease.yaml | 'General Population' | '0.0001-0.001' | 0.1 | 10 |
| Hypertensive_Heart_Disease.yaml | 'Adults over 50' | '10-20' | 10000 | 1e+06 |
| Hypertrophic_Cardiomyopathy.yaml | 'General Population' | '0.2' | 200 | 20000 |
| Jeavons_Syndrome.yaml | 'Global' | '0.0001' | 0.1 | 10 |
| Juvenile_Polyposis_Syndrome.yaml | 'Japan nationwide survey' | '0.00015' | 0.15 | 15 |
| Juvenile_Polyposis_Syndrome.yaml | 'Review-derived birth estimate' | '0.001' | 1 | 100 |
| Kabuki_Syndrome.yaml | 'Worldwide' | '0.003' | 3 | 300 |
| Klinefelter_Syndrome.yaml | 'Males' | '0.2' | 200 | 20000 |
| Kummell_Disease.yaml | 'Elderly with osteoporotic vertebral fractures' | '6.3' | 6300 | 630000 |
| Laryngotracheoesophageal_Cleft.yaml | 'Infants undergoing flexible endoscopy at a tertiary care center' | '0.28' | 280 | 28000 |
| Lathyrism.yaml | 'Adults in Delanta district, Amhara region, Ethiopia (community survey, 2023)' | '6.6' | 6600 | 660000 |
| Lathyrism.yaml | 'Grass pea cultivation areas of Dawunt district, north-eastern Ethiopia (2022)' | '2.4' | 2400 | 240000 |
| Lead_Poisoning.yaml | 'Children living in Patna, Bihar, India, 2020' | '87' | 87000 | 8.7e+06 |
| Lead_Poisoning.yaml | 'United States population aged 1 year and older, 1991-1994' | '2.2' | 2200 | 220000 |
| Leri-Weill_Dyschondrosteosis.yaml | 'Children with short stature' | '4.2' | 4200 | 420000 |
| Long_QT_Syndrome.yaml | 'Live births' | '0.04' | 40 | 4000 |
| Lynch_Syndrome.yaml | 'General Population (MMR pathogenic variant carriers)' | '0.3-0.4' | 300 | 30000 |
| MOGAD.yaml | 'Danish adult population, 2023 criteria' | '0.00151' | 1.51 | 151 |
| MOGAD.yaml | 'South Wales population, 2023 criteria' | '0.00385' | 3.85 | 385 |
| MYO6_Hearing_Loss.yaml | 'Japanese ADSNHL families' | '2.4' | 2400 | 240000 |
| Malignant_Non_Dysgerminomatous_Germ_Cell_Tumor_Of_Ovary.yaml | 'Ovarian cancers' | '2-5' | 2000 | 200000 |
| Mantle_Cell_Lymphoma.yaml | 'All lymphoid neoplasms' | '6' | 6000 | 600000 |
| Mantle_Cell_Lymphoma.yaml | 'All lymphoma diagnoses' | '3-10' | 3000 | 300000 |
| Marfan_Syndrome.yaml | 'Global' | '0.01-0.02' | 10 | 1000 |
| Marfan_Syndrome.yaml | 'Worldwide (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Meckel_Diverticulum.yaml | 'Global' | '2' | 2000 | 200000 |
| Meckel_Syndrome.yaml | 'European births (EUROCAT)' | '0.0026' | 2.6 | 260 |
| Meningioma.yaml | 'Individuals with incidental brain MRI findings in a population-based 70-year cohort' | '1.8' | 1800 | 180000 |
| Meningioma.yaml | 'Proportion among central nervous system neoplasms' | '40' | 40000 | 4e+06 |
| Metastatic_Breast_Carcinoma.yaml | 'Advanced breast cancer cohorts with brain metastasis' | '30' | 30000 | 3e+06 |
| Metastatic_Breast_Carcinoma.yaml | 'Swedish metastatic breast cancer cohort' | '46' | 46000 | 4.6e+06 |
| Metastatic_Colorectal_Cancer.yaml | 'Metastatic colorectal cancer' | '20' | 20000 | 2e+06 |
| Metastatic_Colorectal_Cancer.yaml | 'New colorectal cancer diagnoses' | '20' | 20000 | 2e+06 |
| Metastatic_Gastric_Cancer.yaml | 'Clinical metastatic gastric adenocarcinoma cohort' | '4' | 4000 | 400000 |
| Metastatic_HCC.yaml | 'HCC clinical course after treatment' | '13' | 13000 | 1.3e+06 |
| Metastatic_Melanoma.yaml | 'Advanced melanoma treated with nivolumab' | '34.2' | 34200 | 3.42e+06 |
| Metastatic_Melanoma.yaml | 'Advanced melanoma with brain metastasis' | '60' | 60000 | 6e+06 |
| Metastatic_NSCLC.yaml | 'Advanced NSCLC treated with nivolumab' | '15.6' | 15600 | 1.56e+06 |
| Metastatic_Ovarian_Cancer.yaml | 'Advanced-stage ovarian cancer' | '40' | 40000 | 4e+06 |
| Metastatic_Ovarian_Cancer.yaml | 'Ovarian cancer at diagnosis' | '80' | 80000 | 8e+06 |
| Metastatic_Prostate_Cancer.yaml | 'Metastatic prostate cancer' | '37' | 37000 | 3.7e+06 |
| Metastatic_Prostate_Cancer.yaml | 'Newly diagnosed prostate cancer' | '10' | 10000 | 1e+06 |
| Metastatic_Renal_Cell_Carcinoma.yaml | 'Real-world metastatic RCC registry' | '8.2' | 8200 | 820000 |
| Migraine_with_Aura.yaml | 'General population' | '5' | 5000 | 500000 |
| Morgagni-Stewart-Morel_Syndrome.yaml | 'General population (hyperostosis frontalis interna)' | '2.5' | 2500 | 250000 |
| Multiple_Sclerosis.yaml | 'Europe' | '0.115' | 115 | 11500 |
| Multiple_Sclerosis.yaml | 'Global' | '0.036' | 36 | 3600 |
| Myasthenia_Gravis.yaml | 'Europe (Orphanet annual incidence)' | '0.001-0.009' | 1 | 100 |
| Myasthenia_Gravis.yaml | 'Europe (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Myasthenia_Gravis.yaml | 'Worldwide (Orphanet annual incidence)' | '0.0001-0.0009' | 0.1 | 10 |
| Myasthenia_Gravis.yaml | 'Worldwide (Orphanet point prevalence)' | '0.001-0.009' | 1 | 100 |
| Mycosis_Fungoides.yaml | 'All cutaneous T-cell lymphoma diagnoses' | '60' | 60000 | 6e+06 |
| Myotonic_Dystrophy_Type_1.yaml | 'Global' | '0.00927' | 9.27 | 927 |
| Myotonic_Dystrophy_Type_1.yaml | 'Worldwide (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Nephronophthisis.yaml | 'Global' | '0.1-1.0' | 100 | 10000 |
| Neuromyelitis_Optica.yaml | 'Blacks / Afro-Caribbean' | '0.01' | 10 | 1000 |
| Neuromyelitis_Optica.yaml | 'East Asians' | '0.0035' | 3.5 | 350 |
| Neuromyelitis_Optica.yaml | 'Global (pooled)' | '0.00154' | 1.54 | 154 |
| Neuromyelitis_Optica.yaml | 'Whites (European descent)' | '0.001' | 1 | 100 |
| Noonan_Syndrome.yaml | 'United States (Orphanet prevalence at birth)' | '0.06-0.09' | 60 | 6000 |
| Noonan_Syndrome.yaml | 'Worldwide (Orphanet point prevalence)' | '0.01-0.05' | 10 | 1000 |
| Obsessive-Compulsive_Disorder.yaml | 'global (12-month)' | '3.0' | 3000 | 300000 |
| Obsessive-Compulsive_Disorder.yaml | 'global (lifetime)' | '4.1' | 4100 | 410000 |
| Omphalocele.yaml | 'Danish live births (1997-2021)' | '0.0098' | 9.8 | 980 |
| Oppositional_Defiant_Disorder.yaml | 'European children and adolescents (community studies 2015-2020)' | '1.9' | 1900 | 190000 |
| Oppositional_Defiant_Disorder.yaml | 'Spanish general-population children ages 3 to 9' | '21.9' | 21900 | 2.19e+06 |
| Osteoarthritis.yaml | 'Global population (2020)' | '7.6' | 7600 | 760000 |
| Peripheral_T_Cell_Lymphoma.yaml | 'All non-Hodgkin lymphomas in Western countries' | '10' | 10000 | 1e+06 |
| Pick_Disease.yaml | 'General Population' | '0.002-0.004' | 2 | 200 |
| Plague.yaml | 'Global' | '3e-05' | 0.03 | 3 |
| Pleuropulmonary_Blastoma.yaml | 'Pediatric cancers' | '0.3' | 300 | 30000 |
| Post-Traumatic_Stress_Disorder.yaml | 'civilians residing in armed conflict-affected regions' | '23.7' | 23700 | 2.37e+06 |
| Post-Traumatic_Stress_Disorder.yaml | 'trauma-exposed populations across PTSD prevalence reviews' | '23.95' | 23950 | 2.395e+06 |
| Posterior_Myocardial_Infarction.yaml | 'Acute coronary syndrome presentations' | '3-7' | 3000 | 300000 |
| Prader-Willi_Syndrome.yaml | 'Australia' | '0.004' | 4 | 400 |
| Prader-Willi_Syndrome.yaml | 'France' | '0.005' | 5 | 500 |
| Prader-Willi_Syndrome.yaml | 'General population' | '0.003-0.01' | 3 | 300 |
| Prader-Willi_Syndrome.yaml | 'Japan' | '0.007' | 7 | 700 |
| Prader-Willi_Syndrome.yaml | 'United States' | '0.006' | 6 | 600 |
| Premenstrual_Dysphoric_Disorder.yaml | 'Reproductive-age people with menstrual cycles (confirmed, prospectively diagnosed)' | '3.2' | 3200 | 320000 |
| Premenstrual_Dysphoric_Disorder.yaml | 'Reproductive-age people with menstrual cycles (provisional diagnosis)' | '7.7' | 7700 | 770000 |
| Primary_Ciliary_Dyskinesia.yaml | 'Europe' | '0.001-0.01' | 1 | 100 |
| Primary_Ciliary_Dyskinesia.yaml | 'Pakistan (British Asian)' | '0.01-0.05' | 10 | 1000 |
| Prostate_Adenocarcinoma.yaml | 'Newly diagnosed prostate cancer' | '75' | 75000 | 7.5e+06 |
| Prostate_Adenocarcinoma.yaml | 'Prostate cancers' | '99' | 99000 | 9.9e+06 |
| Proteus_syndrome.yaml | 'Live births' | '0.0001' | 0.1 | 10 |
| Pseudoxanthoma_Elasticum.yaml | 'general population' | '0.004' | 4 | 400 |
| Psoriasis.yaml | 'Global' | '2.0' | 2000 | 200000 |
| Psoriasis.yaml | 'Pustular Psoriasis (Europe)' | '0.0002' | 0.2 | 20 |
| Raynaud_Disease.yaml | 'General' | '3.0' | 3000 | 300000 |
| Refeeding_Syndrome.yaml | 'Adult patients receiving parenteral nutrition (Malaysia)' | '33.3' | 33300 | 3.33e+06 |
| Refeeding_Syndrome.yaml | 'Hospitalized adult and elderly patients' | '38.8' | 38800 | 3.88e+06 |
| Refeeding_Syndrome.yaml | 'Severely acutely malnourished children (Sub-Saharan Africa inpatient)' | '8.7-34.8' | 8700 | 870000 |
| Renal_Agenesis.yaml | 'Live and still births (China Birth Defects Monitoring Network, 2007-2020)' | '0.003' | 3 | 300 |
| Renal_Agenesis.yaml | 'Live and still births (China Birth Defects Monitoring Network, 2007-2020)' | '0.0194' | 19.4 | 1940 |
| Rheumatoid_Arthritis.yaml | 'Global' | '0.5-1.0' | 500 | 50000 |
| Schizophrenia.yaml | 'global' | '0.3-0.7' | 300 | 30000 |
| Silent_Sinus_Syndrome.yaml | 'adults undergoing head CT' | '0.56' | 560 | 56000 |
| Silver_Russell_Syndrome.yaml | 'General population' | '0.001-0.0033' | 1 | 100 |
| Stickler_Syndrome_Type_1.yaml | 'Europe (Orphanet point prevalence)' | '0.001-0.009' | 1 | 100 |
| Stickler_Syndrome_Type_1.yaml | 'Worldwide (Orphanet prevalence at birth)' | '0.01-0.05' | 10 | 1000 |
| Takayasu_Arteritis.yaml | 'Europe' | '0.001-0.009' | 1 | 100 |
| Takayasu_Arteritis.yaml | 'Japan' | '0.001-0.009' | 1 | 100 |
| Takayasu_Arteritis.yaml | 'Worldwide' | '0.001-0.009' | 1 | 100 |
| Taurodontism.yaml | 'Adult dental cohort in Northwest China' | '29.14' | 29140 | 2.914e+06 |
| Taurodontism.yaml | 'Recent human populations (meta-analysis)' | '11.8' | 11800 | 1.18e+06 |
| Taurodontism.yaml | 'Saudi CBCT cohort' | '8' | 8000 | 800000 |
| Tourette_Syndrome.yaml | 'children and adolescents' | '1' | 1000 | 100000 |
| Treacher_Collins_Syndrome.yaml | 'Worldwide' | '0.002' | 2 | 200 |
| Tuberculosis.yaml | 'Global' | '0.1' | 100 | 10000 |
| Tuberous_Sclerosis_Complex.yaml | 'Global' | '0.012' | 12 | 1200 |
| Tuberous_Sclerosis_Complex.yaml | 'Japan (Shizuoka Prefecture)' | '0.0102' | 10.2 | 1020 |
| Twin_to_Twin_Transfusion_Syndrome.yaml | 'Monochorionic diamniotic twin pregnancies' | '10-15' | 10000 | 1e+06 |
| Type_I_Diabetes.yaml | 'Global' | '0.1-0.2' | 100 | 10000 |
| Vitiligo.yaml | 'Worldwide' | '0.5-2' | 500 | 50000 |
| Wolf-Hirschhorn_Syndrome.yaml | 'Global' | '0.002-0.005' | 2 | 200 |
| X-linked_Nonsyndromic_Hearing_Loss.yaml | 'Chinese genetically solved hearing-loss cohort' | '1.14' | 1140 | 114000 |

## Records needing manual review — unparsed prose (11)

| File | population | percentage (raw) |
|------|------------|------------------|
| Bacterial_meningitis.yaml | 'Global' | 'Variable, higher in regions with lower vaccination rates' |
| Cholera.yaml | 'Global' | 'Variable, higher in regions with poor sanitation' |
| Ebola_Virus_Disease_EVD.yaml | 'Central and West Africa' | 'Outbreak-dependent' |
| Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml | 'Southwest Germany newborn-screened methylmalonic, remethylation, and CBS disorders' | '27 screened individuals with target inborn metabolic diseases in the study cohort' |
| Jackson-Weiss_Syndrome.yaml | 'Published pedigrees and molecular case reports' | '15 affected individuals in one four-generation pedigree' |
| SADDAN.yaml | 'Published literature worldwide' | '7 genetically confirmed cases' |
| Scarlet_Fever.yaml | 'Children in Chongqing, China' | 'Highest incidence in ages 3-7 during 2005-2023 surveillance' |
| Scarlet_Fever.yaml | 'Shanghai, China' | '25,539 notifiable cases from 2011 to 2024' |
| Sickle_Cell_Disease.yaml | 'Global population, 2021' | '7.74 million people living with sickle cell disease' |
| Spinal_Muscular_Atrophy.yaml | 'United States modeled prevalence and published birth-prevalence literature' | 'approximately 9,429 people living with SMA in the United States' |
| Van_Buchem_Disease.yaml | 'Dutch founder population and published clinical cohorts' | '15 of 18 known Dutch patients in 2013 cohort' |

## Measure type inferred (defaulted to POINT_PREVALENCE) — verify (127)

| File | population | percentage (raw) |
|------|------------|------------------|
| 15q11q13_Microduplication_Syndrome.yaml | 'Pregnant women undergoing genome-wide NIPS' | '0.0069%' |
| 46_XX_Testicular_DSD.yaml | 'General male population' | '~1:20,000' |
| Achromatopsia.yaml | 'General population' | '1 in 30,000-50,000' |
| Acquired_Angioedema.yaml | 'Czech Republic' | '1:760,000' |
| Alpha_1_Antitrypsin_Deficiency.yaml | 'Western Europe and the United States' | '1 in 2,500-5,000' |
| Alstrom_Syndrome.yaml | 'Global' | '1 in 1,000,000' |
| Alternating_Hemiplegia_of_Childhood.yaml | 'Pediatric patients' | 'Approximately 1 in 1,000,000' |
| Aortitis.yaml | 'Single-center major aortic surgery cohort with high histology sampling' | '10.6%' |
| Autoimmune_Polyendocrine_Syndrome_Type_1.yaml | 'General (worldwide)' | '1 in 100,000-200,000' |
| Autosomal_Dominant_Polycystic_Kidney_Disease.yaml | 'United States' | '9.3 per 10,000' |
| Brucellosis.yaml | 'Global literature meta-analysis' | '15.49% pooled prevalence among included study populations' |
| CADASIL_Type_1.yaml | 'General population' | '1.3-4.1 per 100,000 adults' |
| Cardiofaciocutaneous_Syndrome.yaml | 'Japanese nationwide survey' | '1 in 810,000' |
| Carotid_Stenosis.yaml | 'Adults aged 45-80 years in the REACH-derived validation cohort without prior carotid procedures' | '6.3% severe baseline asymptomatic carotid artery stenosis' |
| Central_Core_Myopathy.yaml | 'All-age populations' | '0.37 per 100,000' |
| Coffin_Siris_Syndrome.yaml | 'Published literature cohorts' | 'approximately 1:10,000 to 1:100,000' |
| Cori_Forbes_Disease.yaml | 'Global and founder populations' | '1 in 100,000 globally; 1 in 5,400 in North African Jews; 1 in 3,100-3,600 in the Faroe Islands' |
| Costello_Syndrome.yaml | 'Japanese nationwide survey' | '1 in 1,290,000' |
| Cowden_Syndrome.yaml | 'Global clinically recognized populations' | '1 in 200,000' |
| Crouzon_Syndrome.yaml | 'Birth prevalence' | '16.5 per 1,000,000' |
| Danon_disease.yaml | 'Patients with unexplained LVH and ventricular preexcitation' | '30%' |
| Dentatorubral-Pallidoluysian_Atrophy.yaml | 'Japanese ancestry' | '2-7 per million' |
| Duchenne_Muscular_Dystrophy.yaml | 'Global male population' | '7.1 per 100,000 males' |
| Dystroglycanopathy.yaml | 'Chinese congenital muscular dystrophy cohort' | '21.0% of CMD cases' |
| Dystroglycanopathy.yaml | 'UK genetically confirmed congenital muscular dystrophy cohort' | '26.5% of CMD cases' |
| Epilepsy.yaml | 'Drug-Resistant Epilepsy' | '30% of epilepsy patients' |
| Epilepsy.yaml | 'Global' | '6.38 per 1,000 (active epilepsy)' |
| Epilepsy.yaml | 'Juvenile Myoclonic Epilepsy (Norway)' | '5.6 per 10,000' |
| Fabry_Disease.yaml | 'Global clinically recognized populations' | '1 in 100,000' |
| Facioscapulohumeral_Muscular_Dystrophy.yaml | 'Symptomatic population in the Netherlands' | '12 per 100,000' |
| Fibrodysplasia_Ossificans_Progressiva.yaml | 'France residents' | '1.36 per million inhabitants' |
| Fibrodysplasia_Ossificans_Progressiva.yaml | 'United States residents' | '0.88 per million' |
| Fragile_X_Syndrome.yaml | 'General population' | '1.4 per 10,000 males; 0.9 per 10,000 females' |
| Furunculosis.yaml | 'German village outbreak participants (2002-2004)' | '36%' |
| Furunculosis.yaml | 'Recurrent furunculosis cohorts' | '60%' |
| Gorlin_Syndrome.yaml | 'Global' | '1 in 57,000 to 1 in 256,000' |
| Green_Tobacco_Sickness.yaml | 'Female tobacco farmers in southern Brazil' | '11.9%' |
| Green_Tobacco_Sickness.yaml | 'Global tobacco harvesters' | '8.2-47%' |
| Green_Tobacco_Sickness.yaml | 'Latino farmworkers in North Carolina, USA' | '24.2%' |
| Green_Tobacco_Sickness.yaml | 'Male tobacco farmers in southern Brazil' | '6.6%' |
| Hashimoto_Encephalopathy.yaml | 'General population' | '2.1 / 100,000' |
| Hemochromatosis.yaml | 'Northern European ancestry (C282Y homozygosity prevalence)' | '1 in 200' |
| Hemochromatosis.yaml | 'UK Biobank male C282Y homozygotes' | '56.4% diagnosed by age 80' |
| Hemochromatosis.yaml | 'White primary care patients in Rochester, New York' | '5.4 per 1,000' |
| Hemophilia_A.yaml | 'Males in high-income-country registry meta-analysis' | '17.1 per 100,000 males' |
| Hemophilia_A.yaml | 'United States males' | '12 per 100,000 males' |
| Hemophilia_B.yaml | 'Males' | '3.8 per 100,000' |
| Hereditary_von_Willebrand_Disease.yaml | 'Registry or regional diagnosed cohorts' | '<1 to 450 per million' |
| Heritable_Pulmonary_Arterial_Hypertension.yaml | 'Adults in recent national PAH registries' | '47.6-54.7 per million' |
| Homocystinuria.yaml | 'Global clinically recognized populations' | '0.82 per 100,000' |
| Homocystinuria.yaml | 'United States claims-based cohort (strict case definition)' | '1.04 per 100,000' |
| Hospital-Acquired_Acute_Kidney_Injury.yaml | 'Elderly hospitalized patients' | '15-30%' |
| Hospital-Acquired_Acute_Kidney_Injury.yaml | 'Hospitalized adults (general)' | '10-25%' |
| Hospital-Acquired_Acute_Kidney_Injury.yaml | 'ICU patients' | '16-59%' |
| Huntington_Disease.yaml | 'Western populations (USA, Canada, Europe)' | '8.2-9.0 per 100,000' |
| Hypokalemic_Periodic_Paralysis.yaml | 'General population' | '1 per 100,000' |
| Hypophosphatasia.yaml | 'Less severe adult forms in Europe' | '1 in 3,100 to 1 in 508' |
| IKBKG_Ectodermal_Dysplasia_with_Immunodeficiency.yaml | 'General population' | '0.00237%' |
| Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml | 'United States claims-based classical homocystinuria cohort' | '1.04 per 100,000 under a strict case definition' |
| Inherited_Porphyria.yaml | 'Clinically manifest acute intermittent porphyria' | '5-10 cases per 100,000 persons' |
| Inherited_Retinal_Dystrophy.yaml | 'Global, all inherited retinal dystrophies combined' | '1 in 2,000 to 1 in 4,000' |
| Joubert_syndrome.yaml | 'Reported prevalence' | '1:80,000-1:100,000' |
| Kennedy_Disease.yaml | 'Italy (nationwide estimate)' | '1.5 per 100,000' |
| Kleefstra_Syndrome.yaml | 'Global reported literature and intellectual disability cohorts' | 'Unknown (estimated 1 in 200,000 among cases with intellectual disability)' |
| Koolen_de_Vries_syndrome.yaml | 'Historically estimated general population prevalence' | '~1 in 16,000' |
| Loeys-Dietz_Syndrome.yaml | 'General population' | 'less than 1 in 100,000' |
| Long_COVID.yaml | 'Adults with prior SARS-CoV-2 infection (Victoria, Australia)' | '14.2% clinical long COVID' |
| Long_COVID.yaml | 'COVID-19 survivors (mixed hospitalization status)' | '~45% with at least one unresolved symptom at mean follow-up of 126 days' |
| Lowe_Syndrome.yaml | 'General population' | '1 in 500,000' |
| Lymphangioleiomyomatosis.yaml | 'Adult women' | '~3-8 per million women' |
| Lymphangioleiomyomatosis.yaml | 'Adult women with tuberous sclerosis complex' | '~30-40%' |
| MECP2_Duplication_Syndrome.yaml | 'Global' | '1-9 / 1 000 000' |
| MELAS_Syndrome.yaml | 'Adults in Southwest Finland (2022, m.3243A>G-related disease)' | '4.2/100,000' |
| Machado_Joseph_Disease.yaml | 'Global (most common dominant SCA worldwide)' | '1-9/100,000' |
| Malignant_Hyperthermia_of_Anesthesia.yaml | 'Genetic susceptibility' | 'as great as one in 400 individuals' |
| Methylmalonic_Acidemia.yaml | 'Conventional clinical estimates' | '~1 in 50,000' |
| Minimal_Change_Disease.yaml | 'Adults' | 'approximately 10%-25% of idiopathic nephrotic syndrome cases' |
| Minimal_Change_Disease.yaml | 'Children' | '70-90% of idiopathic nephrotic syndrome cases after age 1 year' |
| Nemaline_Myopathy.yaml | 'muscle-biopsy cohort in India' | '0.53% of all muscle diseases; 22.6% of congenital myopathies' |
| Neurosarcoidosis.yaml | 'Olmsted County sarcoidosis cohort' | '3% of patients with sarcoidosis' |
| Oculocutaneous_Albinism.yaml | 'General population (all OCA forms, worldwide)' | 'Approximately 1 in 17,000' |
| Orofaciodigital_Syndrome_Type_I.yaml | 'Published clinical estimates' | '1 in 50,000 to 1 in 250,000' |
| Osteogenesis_Imperfecta_Type_I.yaml | 'Swedish population-based registry' | '5.16 per 100,000' |
| Osteogenesis_Imperfecta_Type_II.yaml | 'Prenatal-onset OI cases in a single-center fetal diagnostic series' | '50%' |
| Osteogenesis_Imperfecta_Type_III.yaml | 'Swedish pediatric osteogenesis imperfecta population' | '0.89 per 100,000' |
| Osteogenesis_Imperfecta_Type_IV.yaml | 'Swedish pediatric osteogenesis imperfecta population' | '1.35 per 100,000' |
| Osteogenesis_Imperfecta_Type_V.yaml | 'Chinese cohort of 298 osteogenesis imperfecta probands' | '5.03%' |
| Osteogenesis_Imperfecta_Type_VII.yaml | '283-patient severe osteogenesis imperfecta cohort' | '4 of 283 (~1.4%)' |
| PRPH2-Related_Retinopathy.yaml | 'Foundation Fighting Blindness Consortium inherited retinal disease cohort' | '5%' |
| PRPH2-Related_Retinopathy.yaml | 'International inherited macular dystrophy cohort' | '6.7%' |
| PTCH1-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml | 'General nevoid basal cell carcinoma syndrome populations' | '1 in 100,000' |
| Pallister-Hall_Syndrome.yaml | 'GLI3 mutation-positive GCPS/PHS diagnostic cohort' | '27.6%' |
| Paraneoplastic_Neurological_Syndromes.yaml | 'Northeastern Italy population-based cohort, 2009-2017' | '4.37 per 100,000 prevalence; 0.89 per 100,000 person-years incidence' |
| Paraneoplastic_Neurological_Syndromes.yaml | 'Olmsted County, Minnesota population-based cohort, 1987-2018' | '5.4 per 100,000 prevalence; 0.6 per 100,000 person-years incidence' |
| Paratyphoid_Fever.yaml | 'South Delhi suspected enteric fever patients' | '16.74% of typhoidal Salmonella isolates were S. Paratyphi A and B in this cohort' |
| Pelizaeus_Merzbacher_Disease.yaml | 'Global' | '1 in 200,000 to 500,000' |
| Peutz_Jeghers_Syndrome.yaml | 'Review-based estimates' | '1 in 8,300 to 1 in 280,000' |
| Peutz_Jeghers_polyp.yaml | 'Japan, nationwide 2022 Peutz-Jeghers syndrome survey' | '0.6 per 100,000' |
| Peutz_Jeghers_polyp.yaml | 'Review-based global estimates for Peutz-Jeghers syndrome' | '1 in 8,300 to 1 in 280,000' |
| Phenylketonuria.yaml | 'Global neonatal screening cohorts' | '6.002 per 100,000 neonates' |
| Platelet-Type_von_Willebrand_Disease.yaml | 'Global population genetics estimate from gnomAD v4.1' | '136 per million' |
| Polycystic_Kidney_Disease.yaml | 'United States ADPKD populations' | '9.3 per 10,000' |
| Primary_Coenzyme_Q10_Deficiency.yaml | 'General population' | '<0.001%' |
| Pycnodysostosis.yaml | 'Global population' | 'Approximately 1 per million' |
| RHO-Related_Retinopathy.yaml | 'IRD clinical genetics cohort (Foundation Fighting Blindness Consortium, 41 international centers, 33,834 patients)' | '4%' |
| RPGR-Related_Retinopathy.yaml | 'US, Europe, and Australia males' | '3.4-4.4 per 100,000 males' |
| Rett_Syndrome.yaml | 'Females in the general population' | '7.1 per 100,000 females' |
| SUFU-related_Nevoid_Basal_Cell_Carcinoma_Syndrome.yaml | 'Derived from nevoid basal cell carcinoma syndrome cohorts' | 'Approximately 1 in 800,000-3,600,000 individuals' |
| Sarcoidosis.yaml | 'Europe (Germany)' | '44-48 per 100,000' |
| Sclerosteosis.yaml | 'South African Afrikaner founder population' | '1 in 75,000' |
| Smith-Lemli-Opitz_syndrome.yaml | 'Populations of European origin' | '1 in 15,000-60,000' |
| Spasmodic_Dysphonia.yaml | 'Japan' | '3.5-7.0 / 100,000' |
| Spinocerebellar_Ataxia_Type_17.yaml | 'North East England' | '0.16/100,000' |
| Spondyloepiphyseal_Dysplasia_Congenita.yaml | 'General population' | '3.4 per million' |
| Stargardt_Disease.yaml | 'Israeli nationwide inherited retinal disease cohort' | 'approximately 1 in 16,000' |
| Systemic_Lupus_Erythematosus.yaml | 'North America' | '23.2 per 100,000 person-years incidence; 241 per 100,000 prevalence' |
| TBX6-Associated_Congenital_Scoliosis.yaml | 'Sporadic congenital scoliosis (Han Chinese series)' | '~11%' |
| Tetrahydrobiopterin_Deficiency.yaml | 'Hyperphenylalaninemia worldwide' | '1-2% of HPA cases' |
| Usher_Syndrome.yaml | 'General population (worldwide)' | '4-17 per 100,000' |
| VCP-associated_Multisystem_Proteinopathy.yaml | 'General population' | '0.66/100,000' |
| VEXAS_Syndrome.yaml | 'Men older than 50 years (US regional health system, genome-first ascertainment)' | '1 in 4269' |
| VEXAS_Syndrome.yaml | 'Women older than 50 years (US regional health system, genome-first ascertainment)' | '1 in 26238' |
| Wilsons_Disease.yaml | 'Global clinically diagnosed populations' | '1 in 30,000' |
| Wilsons_Disease.yaml | 'Global population sequencing datasets' | '13.9 per 100,000' |
| X-Linked_Hypophosphatemia.yaml | 'Australian and New Zealand pediatric populations' | '1.33-1.60 per 100,000 children' |
| X-Linked_Hypophosphatemia.yaml | 'General populations' | '1 in 20,000' |
| X-linked_Nonsyndromic_Hearing_Loss.yaml | 'Hereditary hearing loss' | 'Up to 2%' |
