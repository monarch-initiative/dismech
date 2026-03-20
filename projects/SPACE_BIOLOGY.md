# Space Biology & Disease Mechanisms

## Overview

Spaceflight biology provides unique insights into disease mechanisms through microgravity environments, radiation exposure, and physiological deconditioning. Many dismech disorders have direct relevance to space health research, and NASA's Open Science Data Repository (OSDR) contains datasets that could enrich our knowledge base.

## Data Sources

- **NASA OSDR (GeneLab)**: https://osdr.nasa.gov/ — spaceflight omics datasets (RNA-seq, proteomics, metabolomics) from ISS experiments
- **OSDR API**: `https://osdr.nasa.gov/osdr/data/osd/files/` — programmatic access, tagged by organism/tissue/assay
- **NBISC**: NASA Biological Institutional Scientific Collection — non-human biospecimens from spaceflight
- **SMCC**: Space Microbes Collection Catalog

## Diseases with Direct Spaceflight Studies

### Bone & Musculoskeletal

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Osteoporosis** | Astronauts lose ~1-2% bone density/month in microgravity. The canonical space health problem. | GeneLab rodent bone datasets; ISS osteocyte studies |
| **Osteoarthritis** | Cartilage tissue engineering in microgravity; joint unloading models | |
| **Muscular dystrophies** | Skeletal muscle wasting in microgravity parallels dystrophic phenotypes | GeneLab rodent skeletal muscle RNA-seq |

### Cardiovascular

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Hypertrophic cardiomyopathy** | Cardiac remodeling from fluid redistribution in microgravity | ISS cardiac tissue models |
| **Pulmonary hypertension** | Pulmonary vascular changes in altered gravity | |
| **Atherosclerosis** | Endothelial dysfunction studies in simulated microgravity | |

### Neurodegeneration & Protein Aggregation

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Alzheimer's disease** | Amyloid-β aggregation/crystallization in microgravity; ISS protein crystal growth experiments | |
| **Parkinson's disease** | α-synuclein aggregation studies on ISS | LRRK2 crystallography experiments |
| **Amyloidosis (ATTR)** | Transthyretin crystallization in microgravity for structural studies | |

### Cancer

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Various solid tumors** | Tumor spheroid/organoid models in microgravity show altered growth, drug response, and gene expression | Breast, lung, thyroid cancer spheroid studies on ISS |
| **Leukemias** | Radiation-induced hematopoietic cancers from galactic cosmic rays (GCR) | GeneLab radiation biology datasets |
| **CNS tumors** | GCR CNS effects; glioma radiation sensitivity studies | |

### Immune & Infectious

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Immunodeficiency disorders** | T-cell dysfunction, NK cell impairment, altered cytokine profiles in astronauts | GeneLab immune panel datasets |
| **Herpesvirus reactivation** | Latent virus reactivation (EBV, VZV, CMV) during spaceflight — model for immunosuppression | Astronaut saliva/blood viral load data |
| **Salmonellosis / Shigellosis** | Increased bacterial virulence in microgravity (Salmonella typhimurium space experiments) | |

### Metabolic & Endocrine

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Diabetes (Type 2)** | Pancreatic beta cell organoids flown on ISS; insulin resistance from deconditioning | |
| **Adrenal disorders** | HPA axis dysregulation during spaceflight | |

### Ophthalmologic

| Disease | Relevance | Key Datasets |
|---------|-----------|--------------|
| **Stargardt disease / macular degeneration** | Spaceflight Associated Neuro-ocular Syndrome (SANS) shares mechanisms (intracranial pressure, optic disc edema) | Astronaut OCT/MRI datasets |

## Diseases Where Microgravity Models Provide Mechanistic Insights

Beyond direct disease relevance, microgravity serves as a unique perturbation for understanding:

- **3D tissue organization** — organoids and spheroids self-organize differently without gravity, revealing cell-autonomous vs. mechanical patterning
- **Protein aggregation kinetics** — removal of convection and sedimentation changes aggregation pathways (relevant to all amyloidopathies, tauopathies, synucleinopathies)
- **Stem cell differentiation** — mechanical unloading alters lineage commitment (relevant to bone marrow failure syndromes)
- **Fluid dynamics in physiology** — cerebrospinal fluid, lymphatic drainage, vascular flow patterns all change (relevant to hydrocephalus, lymphedema, vascular malformations)

## Overlap with Existing dismech Disorders

Disorders currently in dismech that have known spaceflight-relevant datasets or studies:

- Osteoporosis
- Alzheimer's Disease
- Parkinson's Disease
- Hypertrophic Cardiomyopathy
- ATTR Amyloidosis
- Various cancers (breast, lung, leukemias)
- Cystic Fibrosis (infection susceptibility angle)
- Muscular dystrophies
- Stargardt Disease (SANS overlap)

## Action Items

- [ ] Query NASA OSDR API for datasets matching dismech disorders by MONDO/MESH mapping
- [ ] Add spaceflight-relevant datasets to `datasets:` sections of applicable disorder entries
- [ ] Consider adding `SPACEFLIGHT` as a context/environment in relevant evidence items
- [ ] Explore adding SANS (Spaceflight Associated Neuro-ocular Syndrome) as a dismech disorder
- [ ] Cross-reference GeneLab processed data (gene expression signatures) with dismech pathophysiology entries
- [ ] Consider `EnvironmentTerm` additions for microgravity/radiation contexts (ECTO terms)
