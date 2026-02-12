# Phenopacket Store Evaluation Project

> **GitHub Tracking**: TBD (create issue when starting work)

## Overview

Evaluate the dismech knowledge base against the [Phenopacket Store](https://github.com/monarch-initiative/phenopacket-store/) - a curated collection of GA4GH Phenopackets representing individuals with Mendelian diseases. The Phenopacket Store contains phenopackets organized by gene, with detailed phenotype annotations from case reports in medical literature.

**Reference**: Danis et al., HGG Advances 2025

## Goals

1. **Coverage Analysis**: Identify which Phenopacket Store diseases are represented in dismech
2. **Phenotype Comparison**: Compare HPO term usage between phenopackets and dismech entries
3. **Gap Identification**: Prioritize Mendelian diseases for curation based on phenopacket availability
4. **Validation**: Use phenopacket phenotype profiles to validate/enhance dismech pathophysiology

## Phenopacket Store Statistics

- **Current Version**: 0.1.26 (January 2026)
- **Organization**: By causal gene (300+ genes)
- **Content**: Case-level phenopackets with HPO annotations from literature

## Dismech KB Statistics

- **Total Disorders**: 280
- **Mendelian Disorders**: ~40-50 (subset with genetic etiology)

## High-Priority Diseases for Comparison

These diseases exist in BOTH dismech AND the Phenopacket Store, making them ideal for phenotype comparison:

### Tier 1: Direct Matches (Gene-Based)
| Phenopacket Gene | Phenopackets | Dismech Entry | Priority |
|------------------|--------------|---------------|----------|
| FBN1 | 143 | Marfan_Syndrome.yaml | [ ] Compare phenotypes |
| NF1 | 405 | Neurofibromatosis_Type_1.yaml | [ ] Compare phenotypes |
| LMNA | 259 | ATTR_Amyloidosis.yaml (partial) | [ ] Assess overlap |
| COL3A1 | 41 | Ehlers-Danlos_Syndrome.yaml | [ ] Compare phenotypes |
| COL5A1 | 2 | Ehlers-Danlos_Syndrome_COL5A1-related.yaml | [ ] Compare phenotypes |
| CTCF | 46 | CTCF-related_Neurodevelopmental_Disorder.yaml | [ ] Compare phenotypes |
| ACVR1 | 1 | Fibrodysplasia_Ossificans_Progressiva.yaml | [ ] Compare phenotypes |
| BBS1/2/4/5 | 30 | Bardet-Biedl_Syndrome.yaml | [ ] Compare phenotypes |
| GNAS | 103 | Pseudohypoparathyroidism (missing) | [ ] Consider adding |
| DMD | (check) | Duchenne_Muscular_Dystrophy.yaml | [ ] Compare phenotypes |
| CFTR | (check) | Cystic_Fibrosis.yaml | [ ] Compare phenotypes |
| SMN1 | (check) | Spinal_Muscular_Atrophy.yaml | [ ] Compare phenotypes |

### Tier 2: Diseases in Phenopacket Store (Not in Dismech)
High-value diseases to potentially add to dismech based on phenopacket availability:

| Gene | Phenopackets | Disease | Priority |
|------|--------------|---------|----------|
| ANKRD11 | 333 | KBG syndrome | [ ] |
| POGZ | 117 | White-Sutton syndrome | [ ] |
| EHMT1 | 125 | Kleefstra syndrome 1 | [ ] |
| CHD8 | 78 | ID with autism and macrocephaly | [ ] |
| ITPR1 | 170 | Spinocerebellar ataxia 29 | [ ] |
| GLI3 | 81 | Greig/Pallister-Hall syndromes | [ ] |
| KDM6A | 81 | Kabuki syndrome 2 | [ ] |
| KDM6B | 84 | Stolerman syndrome | [ ] |
| KMT2D | 64 | Kabuki syndrome 1 | [ ] |
| IKZF1 | 81 | CVID 13 | [ ] |
| FBXL4 | 95 | Mitochondrial DNA depletion 13 | [ ] |
| IFT140 | 81 | Polycystic kidney disease 9 | [ ] |
| MPV17 | 60 | Mitochondrial DNA depletion 6 | [ ] |
| NIPBL | 60 | Cornelia de Lange syndrome 1 | [ ] |
| PPP2R1A | 60 | Houge-Janssens syndrome 2 | [ ] |
| CYP21A2 | 69 | Congenital adrenal hyperplasia | [ ] |
| FBXO11 | 56 | ID with dysmorphic facies | [ ] |
| AIRE | 58 | Autoimmune polyendocrinopathy I | [ ] |
| AHDC1 | 65 | Xia-Gibbs syndrome | [ ] |
| FGD1 | 48 | Aarskog-Scott syndrome | [ ] |
| CNTNAP2 | 46 | Pitt-Hopkins like syndrome 1 | [ ] |
| ATP13A2 | 45 | Kufor-Rakeb syndrome | [ ] |
| COQ4 | 51 | Coenzyme Q10 deficiency 7 | [ ] |
| CLDN16 | 51 | Hypomagnesemia 3, renal | [ ] |

### Tier 3: Existing Dismech Entries to Enhance
Mendelian diseases already in dismech that could benefit from phenopacket comparison:

| Dismech Entry | Phenopacket Gene(s) | Status |
|---------------|---------------------|--------|
| Gaucher_Disease.yaml | GBA1 | [ ] Check phenopackets |
| Tay-Sachs_Disease.yaml | HEXA | [ ] Check phenopackets |
| Phenylketonuria.yaml | PAH | [ ] Check phenopackets |
| Hemophilia_A.yaml | F8 | [ ] Check phenopackets |
| Huntingtons_Disease.yaml | HTT | [ ] Check phenopackets |
| Rett_Syndrome.yaml | MECP2 | [ ] Check phenopackets |
| Fragile_X_Syndrome.yaml | FMR1 | [ ] Check phenopackets |
| Dravet_syndrome.yaml | SCN1A | [ ] Check phenopackets |
| Sickle_Cell_Disease.yaml | HBB | [ ] Check phenopackets |
| Fabry_Disease.yaml | GLA | [ ] Check phenopackets |
| Wilsons_Disease.yaml | ATP7B | [ ] Check phenopackets |
| Maple_Syrup_Urine_Disease.yaml | BCKDHB | [ ] Check phenopackets |
| Von_Hippel-Lindau_Disease.yaml | VHL | [ ] Check phenopackets |
| Li-Fraumeni_Syndrome.yaml | TP53 | [ ] Check phenopackets |
| Fanconi_Anemia.yaml | FANCC/FANCI | [ ] Check phenopackets |

## Methodology

### Phase 1: Programmatic Overlap Detection
- [ ] Write script to fetch phenopacket store gene list
- [ ] Map genes to MONDO/OMIM disease IDs
- [ ] Cross-reference with dismech MONDO terms
- [ ] Generate overlap report

### Phase 2: Phenotype Comparison Tool
- [ ] For overlapping diseases, extract HPO terms from phenopackets
- [ ] Compare with dismech phenotype annotations
- [ ] Identify phenotypes in phenopackets missing from dismech
- [ ] Identify phenotypes in dismech not seen in phenopackets

### Phase 3: Gap Prioritization
- [ ] Rank diseases by phenopacket count (more = better characterized)
- [ ] Filter to high-impact Mendelian diseases
- [ ] Recommend top 20 for dismech curation

### Phase 4: Validation & Enhancement
- [ ] For each Tier 1 disease, compare phenotype coverage
- [ ] Add missing HPO terms to dismech entries
- [ ] Validate pathophysiology against phenopacket evidence

## Technical Notes

### Phenopacket Store Access
```bash
# Install toolkit
pip install phenopacket-store-toolkit

# Download latest release
wget https://github.com/monarch-initiative/phenopacket-store/releases/download/0.1.26/all_phenopackets.zip
```

### Disease Mapping
- Phenopackets use MONDO/OMIM disease IDs
- Dismech uses MONDO IDs in `disease_id` field
- Gene-disease mapping via HGNC

## Resources

- [Phenopacket Store Docs](https://monarch-initiative.github.io/phenopacket-store)
- [Phenopacket Store GitHub](https://github.com/monarch-initiative/phenopacket-store)
- [pyphetools](https://github.com/monarch-initiative/pyphetools) - Curation toolkit
- [GA4GH Phenopacket Schema](https://phenopacket-schema.readthedocs.io/)

---

# Related Open Repositories for Dismech Evaluation

Comprehensive literature search conducted 2026-01-30 for open repositories containing patient phenotype data, disease mechanisms, and clinical case information that could be used for dismech evaluation and enhancement.

## Tier 1: Patient-Level Phenotype Datasets

### PMC-Patients
**URL**: https://github.com/pmc-patients/pmc-patients | [Hugging Face](https://huggingface.co/datasets/zhengyun21/PMC-Patients)

- **Scale**: 167K patient summaries from PubMed Central case reports
- **Annotations**: 3.1M patient-article relevance, 293K patient-patient similarity
- **Content**: Case summaries extracted from medical literature via NLP
- **Format**: JSON, BEIR benchmark format
- **License**: CC BY-NC-SA 4.0
- **Reference**: Zhao et al., Scientific Data 2023
- **Use case**: Benchmark phenotype-driven retrieval; compare case phenotypes to dismech entries

### DECIPHER
**URL**: https://www.deciphergenomics.org/

- **Scale**: 51,894 patients, 172,000+ phenotype terms, 51,000+ variants
- **Annotations**: HPO phenotypes, genomic variants (CNV, SNV, STR)
- **Content**: Patient records from 250+ academic clinical genetics centers worldwide
- **Format**: Web interface, bulk download for research
- **License**: Open for approved research
- **Use case**: Validate dismech phenotype coverage against clinical cohorts

### OARD (Open Annotations for Rare Diseases)
**URL**: https://rare.cohd.io/

- **Scale**: Annotations for 7,046 HPO phenotype concepts across 10M+ individuals
- **Content**: Real-world EHR-derived rare disease phenotype annotations (CUIMC + CHOP)
- **Format**: RESTful API (MySQL backend)
- **Reference**: AJHG 2022
- **Use case**: Validate phenotype-disease associations with EHR evidence

### PubCaseFinder
**URL**: https://pubcasefinder.dbcls.jp/

- **Scale**: 300,000 case reports, 19,000 open-sharing cases
- **Annotations**: HPO terms extracted via text mining; disease-phenotype associations
- **Content**: Phenotype-driven differential diagnosis from literature
- **Format**: JSON REST API (Matchmaker Exchange compatible)
- **Use case**: Compare dismech phenotype profiles against literature-derived profiles

### MIMIC Phenotype Annotations
**URL**: https://www.physionet.org/content/phenotype-annotations-mimic/1.20.03/

- **Scale**: Discharge summaries annotated with 15 clinical phenotypes
- **Content**: ICU patient notes from Beth Israel Deaconess Medical Center
- **Format**: Tabular (requires MIMIC access approval)
- **Use case**: Validate dismech chronic disease phenotypes against ICU cohort

## Tier 2: Disease-Gene-Phenotype Knowledge Bases

### Monarch Initiative Knowledge Graph
**URL**: https://monarchinitiative.org/ | [GitHub](https://github.com/monarch-initiative)

- **Content**: Integrated gene-phenotype-disease data across species
- **Annotations**: HPO, MONDO, gene-disease associations, model organism phenotypes
- **Format**: KGX (Knowledge Graph Exchange), API, Biolink model
- **Use case**: Cross-reference dismech diseases with Monarch's curated associations

### Orphanet / Orphadata
**URL**: https://www.orphadata.com/ | https://www.orpha.net/

- **Scale**: 6,000+ rare diseases with phenotype annotations
- **Annotations**: HPO phenotypes with frequency qualifiers (HOOM module)
- **Content**: Expert-curated rare disease phenotypes, genes, epidemiology
- **Format**: XML, JSON, RDF (SPARQL endpoint)
- **License**: Open access
- **Use case**: Validate and enhance rare disease phenotype coverage in dismech

### DisGeNET
**URL**: https://disgenet.com/

- **Scale**: 628,685 gene-disease associations, 210,498 variant-disease associations
- **Sources**: CTD, UniProt, ClinVar, Orphanet, GWAS Catalog, RGD, MGD
- **Format**: Tabular download, R package, Cytoscape app, RDF/SPARQL
- **License**: CC BY-NC-SA 4.0
- **Use case**: Validate gene-disease relationships in dismech

### GenCC (Gene Curation Coalition)
**URL**: https://thegencc.org/ | http://search.thegencc.org

- **Scale**: 15,241 gene-disease assertions on 4,569 genes (Dec 2021)
- **Sources**: ClinGen, OMIM, Orphanet, Genomics England PanelApp, diagnostic labs
- **Annotations**: Gene-disease validity classifications (Definitive → No Known Relationship)
- **Format**: Downloadable database
- **Use case**: Validate gene-disease validity levels for dismech Mendelian entries

### Open Targets Platform
**URL**: https://platform.opentargets.org/

- **Content**: Target-disease evidence from genetics, drugs, pathways, literature
- **Annotations**: Disease associations with evidence scores by data type
- **Format**: GraphQL API, FTP bulk download, Google Cloud
- **License**: Open access
- **Use case**: Validate dismech drug targets and mechanism of action

## Tier 3: Ontology & Terminology Resources

### Human Phenotype Ontology (HPO)
**URL**: https://hpo.jax.org/ | [OBO Foundry](https://obofoundry.org/ontology/hp.html)

- **Scale**: 16,000+ phenotype terms; annotations for 7,000+ diseases
- **Format**: OBO, OWL
- **Use case**: Core ontology for dismech phenotype annotation

### MONDO Disease Ontology
**URL**: https://mondo.monarchinitiative.org/ | [GitHub](https://github.com/monarch-initiative/mondo)

- **Scale**: 20,000+ disease classes with cross-references
- **Mappings**: OMIM, Orphanet, NCIT, DOID, MeSH
- **Format**: OBO, OWL, SSSOM mappings
- **Use case**: Disease identity mapping for dismech; already in use

### OMIM
**URL**: https://www.omim.org/

- **Scale**: 15,000+ gene entries, 8,000+ phenotype entries
- **Content**: Authoritative Mendelian disease descriptions, clinical synopses
- **Format**: Bulk download (requires registration)
- **Use case**: Authoritative source for Mendelian disease mechanisms

### MedGen
**URL**: https://www.ncbi.nlm.nih.gov/medgen/

- **Content**: Aggregated clinical genetics information (GTR, ClinVar, OMIM, HPO, Orphanet)
- **Annotations**: Disease concepts with mode of inheritance, clinical features, genes
- **Format**: Web interface, FTP download
- **Use case**: Cross-reference dismech disease concepts

## Tier 4: Pathway & Mechanism Databases

### Reactome
**URL**: https://reactome.org/

- **Scale**: 16,200 reactions, 2,848 pathways, 11,429 genes
- **Content**: Curated biological pathways and reactions
- **Format**: BioPAX, SBML, API, bulk download
- **License**: CC0
- **Use case**: Validate dismech pathophysiology against curated pathways

### KEGG
**URL**: https://www.genome.jp/kegg/

- **Content**: Pathway maps for metabolism, disease, drugs
- **Scale**: 10,664 reactions, 18,107 metabolites
- **Note**: Academic use restrictions apply
- **Use case**: Cross-reference dismech pathophysiology with KEGG disease pathways

### DrugBank
**URL**: https://go.drugbank.com/

- **Scale**: 9,591 drug entries, 4,270 protein targets
- **Content**: Drug mechanisms, targets, pathways, pharmacology
- **Format**: XML, CSV (academic license available)
- **Use case**: Validate dismech treatment mechanisms

### DrugMechDB
**URL**: https://sulab.github.io/DrugMechDB/ | [GitHub](https://github.com/SuLab/DrugMechDB)

- **Content**: Drug-to-disease mechanism of action paths
- **Format**: JSON paths through biomedical knowledge graph
- **License**: Open source
- **Use case**: Validate dismech treatment-disease mechanism relationships

## Tier 5: Genetic Variation & GWAS

### ClinVar
**URL**: https://www.ncbi.nlm.nih.gov/clinvar/

- **Content**: Variant-disease interpretations with evidence
- **Annotations**: Pathogenicity, disease associations, phenotypes
- **Format**: VCF, XML, tabular (FTP download)
- **Use case**: Validate genetic variants underlying dismech diseases

### GWAS Catalog
**URL**: https://www.ebi.ac.uk/gwas/

- **Scale**: Largest GWAS repository; genome-wide summary statistics
- **Content**: Variant-trait associations from published studies
- **Format**: Spreadsheet download, API, summary statistics FTP
- **License**: Open access
- **Use case**: Validate complex disease genetic associations in dismech

### UK Biobank
**URL**: https://www.ukbiobank.ac.uk/

- **Scale**: 500,000 individuals with deep phenotyping + whole-genome sequencing
- **Content**: Genetic data, health outcomes, biomarkers, imaging
- **Format**: Requires approved research application
- **Use case**: Large-scale validation of disease-phenotype-genotype relationships

## Tier 6: Clinical Text & NLP Datasets

### n2c2 / i2b2 Clinical NLP
**URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

- **Content**: Annotated clinical notes for NLP challenges (obesity, medications, temporal relations)
- **Format**: XML (requires DUA)
- **Use case**: Benchmark phenotype extraction methods

### CREEDS
**URL**: http://amp.pharm.mssm.edu/CREEDS/

- **Content**: Crowd-extracted expression signatures (disease, drug, gene perturbation)
- **Scale**: 2,460 gene perturbation, 839 disease, 906 drug signatures from GEO
- **Use case**: Gene expression signatures for dismech diseases

### GEO (Gene Expression Omnibus)
**URL**: https://www.ncbi.nlm.nih.gov/geo/

- **Scale**: 200,000+ studies, 6.5M samples
- **Content**: Gene expression and epigenomics data
- **Format**: SOFT, MINiML, supplementary files
- **Use case**: Expression profiles for dismech disease mechanisms

## Tier 7: Clinical Trials

### ClinicalTrials.gov / AACT
**URL**: https://clinicaltrials.gov/ | https://aact.ctti-clinicaltrials.org/

- **Content**: Clinical trial registry with conditions, interventions, outcomes
- **Format**: XML bulk download, AACT relational database
- **Use case**: Validate dismech treatment annotations against trial data

## Summary: Priority Datasets for Dismech Evaluation

| Dataset | Primary Use | Data Type | Access |
|---------|-------------|-----------|--------|
| Phenopacket Store | Mendelian phenotype validation | Patient phenopackets | Open |
| PMC-Patients | Case report comparison | Patient summaries | Open |
| DECIPHER | Clinical phenotype validation | Patient variants+HPO | Registered |
| Orphadata | Rare disease phenotypes | Disease-HPO | Open |
| DisGeNET | Gene-disease validation | Associations | Open |
| GenCC | Gene validity | Expert curation | Open |
| Open Targets | Drug-target evidence | Multi-source | Open |
| Reactome | Pathway validation | Curated pathways | Open |
| GWAS Catalog | Complex disease genetics | GWAS associations | Open |

---

# STATUS

## Project Setup
- [ ] Create GitHub issue for tracking
- [ ] Install phenopacket-store-toolkit
- [ ] Download latest phenopacket release
- [x] Literature search for related open repositories (completed 2026-01-30)

## Phase 1: Coverage Analysis
- [ ] Generate gene-disease mapping
- [ ] Cross-reference with dismech
- [ ] Produce overlap report

## Phase 2: Tier 1 Comparisons
- [ ] Marfan Syndrome (FBN1)
- [ ] Neurofibromatosis Type 1 (NF1)
- [ ] Ehlers-Danlos Syndrome (COL3A1/COL5A1)
- [ ] CTCF-related NDD (CTCF)
- [ ] Bardet-Biedl Syndrome (BBS genes)
- [ ] Fibrodysplasia Ossificans Progressiva (ACVR1)
- [ ] Duchenne Muscular Dystrophy (DMD)
- [ ] Cystic Fibrosis (CFTR)
- [ ] Spinal Muscular Atrophy (SMN1)

## Phase 3: Gap Analysis
- [ ] Prioritize top 20 missing diseases
- [ ] Begin curation of highest-priority entries

# NOTES

## 2026-01-30
- Project initialized
- Analyzed Phenopacket Store structure: 300+ genes, 5000+ phenopackets
- Identified 12 Tier 1 diseases with direct overlap between dismech and phenopacket store
- Identified 24 high-phenopacket-count diseases not currently in dismech
- Identified 15 existing dismech Mendelian entries that could be enhanced via phenopacket comparison

**Comprehensive literature search for related open repositories:**
- **Patient-level phenotype datasets (Tier 1)**: PMC-Patients (167K cases), DECIPHER (51K patients), OARD (EHR-derived), PubCaseFinder (300K case reports), MIMIC phenotype annotations
- **Disease-gene-phenotype KBs (Tier 2)**: Monarch KG, Orphadata, DisGeNET (628K gene-disease associations), GenCC, Open Targets
- **Ontology resources (Tier 3)**: HPO, MONDO, OMIM, MedGen
- **Pathway databases (Tier 4)**: Reactome, KEGG, DrugBank, DrugMechDB
- **Genetic variation (Tier 5)**: ClinVar, GWAS Catalog, UK Biobank
- **Clinical text/NLP (Tier 6)**: n2c2/i2b2, CREEDS, GEO
- **Clinical trials (Tier 7)**: ClinicalTrials.gov/AACT

Next steps:
1. Install phenopacket-store-toolkit and begin programmatic analysis
2. Prioritize datasets for integration based on overlap with dismech scope
3. Develop comparison scripts for phenotype coverage analysis
