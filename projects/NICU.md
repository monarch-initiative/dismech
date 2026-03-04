# NICU Curation Project

## Overview

This project focuses on disorders commonly managed in neonatal intensive care units (NICUs), spanning prematurity complications, neonatal critical care, and high-impact genetic diseases that present in the newborn period.

## Goals

- Curate NICU-relevant diseases with evidence-backed pathophysiology
- Map neonatal phenotypes to HPO terms
- Annotate treatments with MAXO terms
- Provide PMID-supported evidence for all claims

## Target Conditions (NICU Core)

### Prematurity / Respiratory
- [ ] Respiratory Distress Syndrome of the Newborn (surfactant deficiency)
- [ ] Bronchopulmonary Dysplasia (chronic lung disease of prematurity)
- [ ] Apnea of Prematurity
- [ ] Transient Tachypnea of the Newborn
- [ ] Meconium Aspiration Syndrome
- [ ] Persistent Pulmonary Hypertension of the Newborn (PPHN)

### Neurologic / Brain Injury
- [ ] Hypoxic-Ischemic Encephalopathy (HIE)
- [ ] Intraventricular Hemorrhage (IVH)
- [ ] Periventricular Leukomalacia (PVL)
- [ ] Neonatal Seizures

### GI / Nutrition
- [ ] Necrotizing Enterocolitis (NEC)
- [ ] Spontaneous Intestinal Perforation
- [ ] Short Bowel Syndrome (post-NEC or surgical)
- [ ] Feeding Intolerance / Dysmotility (syndrome-level entry if needed)

### Infectious
- [ ] Early-Onset Neonatal Sepsis (e.g., GBS, E. coli)
- [ ] Late-Onset Neonatal Sepsis
- [ ] Neonatal Meningitis

### Heme / Metabolic / Endocrine
- [ ] Neonatal Hyperbilirubinemia
- [ ] Kernicterus
- [ ] Neonatal Hypoglycemia
- [ ] Anemia of Prematurity
- [ ] Neonatal Polycythemia
- [ ] Congenital Adrenal Hyperplasia
- [ ] Congenital Hypothyroidism

### Congenital / Surgical / Cardiac
- [ ] Patent Ductus Arteriosus (PDA)
- [ ] Congenital Diaphragmatic Hernia (CDH)
- [ ] Gastroschisis
- [ ] Omphalocele
- [ ] Esophageal Atresia / Tracheoesophageal Fistula
- [ ] Ductal-Dependent Congenital Heart Disease (TGA, HLHS, etc.)

## Target Genetic Diseases (NICU-Relevant)

### Chromosomal / Syndromic
- [x] Down syndrome - `Down_syndrome.yaml`
- [ ] Trisomy 18 (Edwards syndrome)
- [ ] Trisomy 13 (Patau syndrome)
- [x] Wolf-Hirschhorn syndrome - `Wolf-Hirschhorn_Syndrome.yaml`
- [x] 22q11.2 deletion (DiGeorge syndrome) - `22q11.2_Deletion_Syndrome.yaml` - Created 2026-02-03, 85% compliance
- [x] Noonan syndrome - `Noonan_Syndrome.yaml`

### Inborn Errors of Metabolism
- [x] Phenylketonuria (PKU) - `Phenylketonuria.yaml`
- [x] Maple Syrup Urine Disease - `Maple_Syrup_Urine_Disease.yaml`
- [ ] Urea cycle disorders (e.g., OTC deficiency)
- [ ] Propionic acidemia
- [ ] Methylmalonic acidemia
- [ ] Isovaleric acidemia
- [ ] Galactosemia
- [x] MCAD deficiency - `MCAD_Deficiency.yaml` - Created 2026-02-03, 45% compliance (needs evidence)
- [ ] VLCAD deficiency
- [x] Peroxisome biogenesis disorder - `Peroxisome_Biogenesis_Disorder.yaml`

### Neuromuscular / Neurogenetic
- [x] Spinal Muscular Atrophy - `Spinal_Muscular_Atrophy.yaml`
- [ ] Congenital myotonic dystrophy
- [ ] Congenital myasthenic syndromes

### Skeletal Dysplasias
- [x] Thanatophoric dysplasia type 1 - `Thanatophoric_Dysplasia_Type_1.yaml`
- [x] Thanatophoric dysplasia type 2 - `Thanatophoric_Dysplasia_Type_2.yaml`
- [x] Achondroplasia - `Achondroplasia.yaml`
- [x] Hypochondroplasia - `Hypochondroplasia.yaml`
- [x] SADDAN - `SADDAN.yaml`

### Hematologic / Other Genetic
- [x] G6PD deficiency - `Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml`
- [x] Gaucher disease - `Gaucher_Disease.yaml`
- [x] Fabry disease - `Fabry_Disease.yaml`
- [x] Fanconi anemia - `Fanconi_Anemia.yaml`
- [x] TARP syndrome - `TARP_syndrome.yaml`
- [x] Sengers syndrome - `Sengers_syndrome.yaml`
- [x] CHIME syndrome - `CHIME_syndrome.yaml`
- [x] HIDEA syndrome - `HIDEA_Syndrome.yaml`

## Curation Workflow

1. Create YAML file in `kb/disorders/`
2. Validate with `just validate` and `just validate-references`
3. Validate terms with `just validate-terms-file`
4. Run `just qc` before committing
