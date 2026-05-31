---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T03:37:50.436727'
end_time: '2026-05-05T04:17:15.187183'
duration_seconds: 2364.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Angiosarcoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Angiosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Angiosarcoma** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Disease Characterization Report: Angiosarcoma

---

## Summary

Angiosarcoma is a rare, highly aggressive malignant neoplasm arising from vascular endothelial cells, accounting for less than 1–2% of all soft tissue sarcomas. Despite its rarity, it carries a disproportionately poor prognosis, with an overall 5-year survival rate of approximately 26.7% (95% CI 25.4–28.1%) based on SEER database analysis of 5,135 patients ([PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/)). The disease manifests across diverse anatomical sites — skin (especially head/neck and scalp), breast, liver, heart, spleen, bone, and deep soft tissues — with distinct etiological subtypes defined by their molecular drivers and environmental triggers.

The molecular landscape of angiosarcoma is remarkable for its etiological heterogeneity. Primary/sporadic angiosarcomas harbor recurrent activating mutations in angiogenic signaling genes including *KDR* (VEGFR2), *PIK3CA*, and *PTPRB*, while radiation-associated angiosarcomas are defined by near-universal *MYC* amplification (100% of cases) with frequent *FLT4* (VEGFR3) coamplification. UV-associated head and neck angiosarcomas carry high tumor mutational burden with UV-signature mutations, and chemically-induced hepatic angiosarcomas arise from exposure to vinyl chloride, thorotrast, or arsenic. These distinct molecular subtypes have important therapeutic implications: immune checkpoint inhibitors show particular activity in UV- and radiation-associated subtypes with high TMB, while anti-angiogenic agents and combination regimens are being explored across subtypes.

Canine hemangiosarcoma shares remarkable genomic and biological features with human angiosarcoma — including driver mutations in *PIK3CA* (46%), *TP53* (66%), and *NRAS* (24%) — establishing dogs as a critically important comparative model for advancing therapeutic development in this orphan malignancy.

---

## 1. Disease Information

### Overview

Angiosarcoma is a malignant mesenchymal neoplasm of endothelial cell origin that phenotypically and functionally recapitulates normal endothelium ([PMID: 38391320](https://pubmed.ncbi.nlm.nih.gov/38391320/)). It is classified among soft tissue sarcomas and represents one of the most aggressive tumor types in this category, characterized by rapid local invasion, high rates of recurrence and metastasis, and poor overall prognosis. The tumor can arise virtually anywhere in the body, with the most common sites being skin (particularly the head and neck region in elderly patients), breast (both primary and radiation-associated), liver, heart, and spleen.

### Key Identifiers

| Identifier | Code |
|---|---|
| **MONDO** | MONDO:0005971 |
| **ICD-10** | C49 (malignant neoplasm of other connective and soft tissue); specific histology code 9120/3 |
| **ICD-O-3 Morphology** | 9120/3 (Hemangiosarcoma / Angiosarcoma) |
| **MeSH** | D006394 (Hemangiosarcoma) |
| **Orphanet** | ORPHA:263413 |
| **OMIM** | Not assigned as a distinct Mendelian entry; associated with Li-Fraumeni syndrome (OMIM: 151623) in some familial cases |
| **SNOMED CT** | 39000009 (Angiosarcoma) |

### Synonyms and Alternative Names

- Hemangiosarcoma
- Malignant hemangioendothelioma
- Malignant angioendothelioma
- Lymphangiosarcoma (when arising from lymphatic endothelium)
- Stewart-Treves syndrome (when arising in the setting of chronic lymphedema post-mastectomy)

### Information Sources

The information in this report is derived from aggregated disease-level resources including the SEER database, published case series, prospective clinical trials, genomic profiling studies, and systematic reviews. Individual patient-level data are referenced where available from clinical trials and case reports.

---

## 2. Etiology

### Disease Causal Factors

Angiosarcoma arises through multiple distinct etiological pathways:

**Sporadic/Primary**: The majority of angiosarcomas arise spontaneously without identifiable environmental exposure. These tumors are driven by somatic mutations in angiogenic signaling pathways, particularly *KDR* (VEGFR2) mutations found in 70% of primary mammary angiosarcomas, *PIK3CA/PIK3R1* mutations (70%), and *PTPRB* mutations (30%) ([PMID: 32123305](https://pubmed.ncbi.nlm.nih.gov/32123305/)). The *KDR* p.T771R hotspot mutation was identified in 6 of 10 tumors with evidence suggestive of biallelism, indicating strong selection for enhanced VEGFR2 signaling.

**Radiation-Associated**: Secondary angiosarcomas arise in previously irradiated fields, most commonly after breast-conserving therapy for breast carcinoma. The median latency from index radiotherapy is 9.1 years (range 3.7–46.3 years) ([PMID: 38791996](https://pubmed.ncbi.nlm.nih.gov/38791996/)). These tumors are molecularly defined by near-universal *MYC* amplification (100% of cases) and frequent *FLT4* coamplification (25%) ([PMID: 20949568](https://pubmed.ncbi.nlm.nih.gov/20949568/)). The incidence of secondary breast angiosarcoma increased 3-fold from approximately 10 to 30 cases per 100,000 person-years between 1992 and 2016 (P = 0.0037) ([PMID: 37725702](https://pubmed.ncbi.nlm.nih.gov/37725702/)).

**Chemically-Induced**: Hepatic angiosarcoma has well-established associations with environmental carcinogens. A landmark US survey (1964–1974) identified 168 cases of hepatic angiosarcoma, of which 25% were associated with known etiologic factors including vinyl chloride monomer exposure, thorotrast (thorium dioxide) use in angiography, inorganic arsenic exposure, and androgenic-anabolic steroid treatment ([PMID: 7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/)). Vinyl chloride exposure was first recognized as a cause of hepatic angiosarcoma in the mid-1970s among polymerization workers ([PMID: 945708](https://pubmed.ncbi.nlm.nih.gov/945708/)). More recently, aristolochic acid exposure has been implicated in Asian liver angiosarcoma cohorts, with 80% (8/10) of liver angiosarcoma cases displaying a significant SBS22 mutation signature ([PMID: 41394772](https://pubmed.ncbi.nlm.nih.gov/41394772/)).

**UV-Associated**: Head and neck angiosarcomas in sun-exposed skin carry UV mutational signatures (SBS7), with UV-positive cases harboring significantly higher tumor mutational burden than UV-negative cases (P = 0.0294) ([PMID: 37106027](https://pubmed.ncbi.nlm.nih.gov/37106027/)).

**Chronic Lymphedema-Associated (Stewart-Treves Syndrome)**: Angiosarcoma arising in the setting of chronic lymphedema following mastectomy and axillary lymph node dissection, first described by Stewart and Treves in 1948 ([PMID: 26617830](https://pubmed.ncbi.nlm.nih.gov/26617830/)).

### Risk Factors

#### Genetic Risk Factors

- **TP53 germline variants (Li-Fraumeni syndrome)**: Germline *TP53* pathogenic variants predispose to angiosarcoma, particularly in the context of prior radiotherapy. A novel germline *TP53* variant (c.788del) was identified in a patient who developed radiation-associated angiosarcoma ([PMID: 39734593](https://pubmed.ncbi.nlm.nih.gov/39734593/)). A novel germline risk allele in *CHEK2* (p.P35L) was also identified in a Li-Fraumeni-like family with cardiac angiosarcoma ([PMID: 36387164](https://pubmed.ncbi.nlm.nih.gov/36387164/)).
- **Xeroderma pigmentosum**: Patients with XP have elevated skin cancer risk including angiosarcoma, due to defective nucleotide excision repair ([PMID: 39221877](https://pubmed.ncbi.nlm.nih.gov/39221877/)).

#### Environmental Risk Factors

| Risk Factor | Associated Subtype | Evidence Level |
|---|---|---|
| Ionizing radiation | Breast, chest wall, laryngeal AS | Strong — multiple cohort studies |
| Vinyl chloride monomer | Hepatic AS | Strong — established carcinogen |
| Thorotrast (thorium dioxide) | Hepatic AS | Strong — established carcinogen |
| Inorganic arsenic | Hepatic AS | Strong — established carcinogen |
| Aristolochic acid | Hepatic AS (Asian populations) | Emerging — genomic signature evidence |
| UV radiation | Head/neck cutaneous AS | Moderate — mutational signature evidence |
| Chronic lymphedema | Extremity AS (Stewart-Treves) | Strong — clinical association |

#### Demographic Risk Factors

- **Age**: Median age at diagnosis is 69 years (range 0–102) ([PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/))
- **Sex**: Male predominance overall; male:female ratio approximately 3:1 for hepatic AS
- **Race/Ethnicity**: Predominantly non-Hispanic Caucasian (75.4% in SEER data)

### Protective Factors

No well-established genetic or environmental protective factors have been identified for angiosarcoma. Avoidance of known carcinogens (vinyl chloride, arsenic, excessive UV) reduces risk for specific subtypes. Female sex has been identified as a positive prognostic factor for hepatic angiosarcoma (HR 0.68, 95% CI 0.536–0.875, P < 0.05) ([PMID: 39676119](https://pubmed.ncbi.nlm.nih.gov/39676119/)).

### Gene-Environment Interactions

The interaction between germline *TP53* variants and ionizing radiation represents the best-characterized gene-environment interaction in angiosarcoma. Patients with Li-Fraumeni syndrome who receive radiotherapy have significantly elevated risk of developing secondary angiosarcoma, as radiation-induced DNA damage overwhelms already-compromised DNA damage response pathways. Similarly, xeroderma pigmentosum patients exposed to UV radiation develop cutaneous angiosarcoma at increased rates due to defective nucleotide excision repair.

---

## 3. Phenotypes

### Clinical Presentations by Site

#### Cutaneous Angiosarcoma (Head and Neck)

- **Phenotype type**: Physical manifestation — raised, violaceous or erythematous plaques/nodules on sun-exposed skin
- **HPO terms**: HP:0100242 (Sarcoma), HP:0000951 (Abnormality of the skin)
- **Age of onset**: Typically elderly (median ~70 years)
- **Severity**: Severe — aggressive local invasion with multifocal disease
- **Progression**: Rapidly progressive
- **Frequency**: Most common subtype of cutaneous angiosarcoma
- **QoL impact**: Severe — disfiguring facial lesions cause significant psychological distress

#### Breast Angiosarcoma

- **Phenotype type**: Physical manifestation — mass or skin changes in breast
- **HPO terms**: HP:0100242 (Sarcoma), HP:0100013 (Neoplasm of the breast)
- **Onset**: Primary: median age 31 years; Radiation-associated: median age 68–72 years; latency 4–12 years post-RT ([PMID: 19433291](https://pubmed.ncbi.nlm.nih.gov/19433291/))
- **Severity**: Variable — graded by Rosen's method (low, intermediate, high)
- **Frequency**: 0.1–0.2% of malignant breast neoplasms

#### Cardiac Angiosarcoma

- **Phenotype type**: Clinical signs — pericardial effusion, cardiac tamponade, dyspnea
- **HPO terms**: HP:0001698 (Pericardial effusion), HP:0002094 (Dyspnea)
- **Location**: Predominantly right atrium
- **Severity**: Severe — most aggressive primary cardiac malignancy
- **Clinical features**: Hemorrhagic pericardial effusion, cardiac tamponade ([PMID: 41320327](https://pubmed.ncbi.nlm.nih.gov/41320327/))

#### Hepatic Angiosarcoma

- **Phenotype type**: Clinical signs — abdominal pain, hepatomegaly, hepatic rupture
- **HPO terms**: HP:0001392 (Abnormality of the liver), HP:0002027 (Abdominal pain)
- **Severity**: Extremely poor prognosis — 3-year survival rate 6.7% ([PMID: 39676119](https://pubmed.ncbi.nlm.nih.gov/39676119/))

#### Splenic Angiosarcoma

- **Phenotype type**: Clinical signs — acute abdominal pain, splenic rupture, hemoperitoneum
- **HPO terms**: HP:0001743 (Abnormality of the spleen), HP:0002027 (Abdominal pain)
- **Severity**: Nearly universally fatal — most patients die within 12 months

#### Pulmonary Metastatic Disease

- **Phenotype type**: Symptoms — hemoptysis (73% of patients), dyspnea
- **HPO terms**: HP:0002105 (Hemoptysis), HP:0002094 (Dyspnea)
- **Imaging**: Bilateral, randomly distributed, variably shaped nodules with ground-glass opacities
- **Common misdiagnoses**: Tuberculosis (45%), vasculitis (18%) ([PMID: 28885371](https://pubmed.ncbi.nlm.nih.gov/28885371/))

### Laboratory Abnormalities

- Anemia (from hemorrhage or microangiopathic hemolytic process)
- Thrombocytopenia (consumptive coagulopathy / Kasabach-Merritt phenomenon)
- Elevated LDH

---

## 4. Genetic/Molecular Information

### Somatic Driver Genes and Pathogenic Variants

#### Primary/Sporadic Angiosarcoma

| Gene | Variant Type | Frequency | Functional Consequence | Somatic/Germline |
|---|---|---|---|---|
| **KDR** (VEGFR2) | Missense (T771R hotspot) | 70% (mammary) | Gain of function — constitutive VEGFR2 activation | Somatic |
| **PIK3CA** | Activating mutations (H1047R) | 70% (mammary) | Gain of function — PI3K pathway activation | Somatic |
| **PTPRB** | Inactivating mutations | 30% (mammary) | Loss of function — loss of VE-PTP phosphatase | Somatic |
| **TP53** | Missense, frameshift | 16–44% | Loss of function — impaired tumor suppression | Somatic |
| **PLCG1** | Activating mutations | ~10% | Gain of function — PLCγ1 signaling | Somatic |

**Source**: [PMID: 32123305](https://pubmed.ncbi.nlm.nih.gov/32123305/) — "Recurrent genomic alterations were identified in KDR (70%), PIK3CA/PIK3R1 (70%), and PTPRB (30%), each at higher frequencies than reported in AS across all sites. Six tumors harbored a KDR p.T771R hotspot mutation, and all seven KDR-mutant cases showed evidence suggestive of biallelism."

#### Head and Neck (UV-Associated) Angiosarcoma

| Gene | Frequency | Notes |
|---|---|---|
| **CSMD3** | 18% | CUB and Sushi multiple domains 3 |
| **LRP1B** | 18% | LDL receptor-related protein 1B |
| **MUC16** | 18% | Mucin 16 |
| **POT1** | 16% | Protection of telomeres 1 |
| **TP53** | 16% | Tumor protein p53 |

UV-positive cases had significantly higher TMB than UV-negative cases (P = 0.0294) ([PMID: 37106027](https://pubmed.ncbi.nlm.nih.gov/37106027/)).

#### Radiation-Associated Angiosarcoma

| Gene/Alteration | Frequency | Notes |
|---|---|---|
| **MYC amplification** (8q24) | 100% | Defining molecular feature |
| **FLT4** (VEGFR3) coamplification | 25% | |
| **CDKN2A/CDKN2B loss** | 71% (vs 39% sporadic, P = 6.92e-3) | Cell cycle dysregulation |
| **TP53 mutations** | 44% | |

**Source**: [PMID: 20949568](https://pubmed.ncbi.nlm.nih.gov/20949568/) — "High-level MYC amplification was found in 100% of secondary AS, but in none of the AVL or other radiation-associated sarcomas. Coamplification of FLT4 (encoding VEGFR3) was identified in 25% of secondary AS."

[PMID: 25863565](https://pubmed.ncbi.nlm.nih.gov/25863565/) — "Amplification (5- to 20-fold) of the c-myc oncogene was found in all breast radiation-induced angiosarcomas (32 tumours) but in none of the 15 primary angiosarcomas except one (7%). This study reinforces that there are true pathogenetic differences between the two types of breast angiosarcomas."

#### Hepatic Angiosarcoma

- **K-ras-2** point mutations found in 29% of tumors (7/24), including both sporadic (26%) and Thorotrast-induced (40%) cases. Mutations were characteristic of oxidative damage (G:C > A:T and G:C > T:A) ([PMID: 9010458](https://pubmed.ncbi.nlm.nih.gov/9010458/)).
- **Aristolochic acid signature** (SBS22) identified in 80% of Asian liver angiosarcoma cases ([PMID: 41394772](https://pubmed.ncbi.nlm.nih.gov/41394772/)).

### Epigenetic Information

- Radiation-associated angiosarcomas show a distinct transcriptome signature featuring upregulation of lymphatic endothelial markers (*PDPN*, *PROX-1*, *VEGFR3*, *EDNRA*), suggesting origin from radiation-stimulated lymphatic endothelial cells ([PMID: 22532251](https://pubmed.ncbi.nlm.nih.gov/22532251/)).
- MYC amplification drives upregulation of the miR-17-92 cluster with concomitant downregulation of thrombospondin-1 (*THBS1*), linking MYC to angiogenic promotion ([PMID: 22383169](https://pubmed.ncbi.nlm.nih.gov/22383169/)).
- Alternative lengthening of telomeres (ALT) activation has been identified as a hallmark of liver angiosarcoma ([PMID: 41394772](https://pubmed.ncbi.nlm.nih.gov/41394772/)).

### Chromosomal Abnormalities

- *MYC* amplification at 8q24.21 (5- to 20-fold) — hallmark of radiation-associated AS
- *CDKN2A/CDKN2B* losses at 9p21.3 — more frequent in radiation-associated (71%) than sporadic (39%) sarcomas (P = 6.92e-3) ([PMID: 31243333](https://pubmed.ncbi.nlm.nih.gov/31243333/))
- Gains of 17q24.2-17qter identified in subsets of post-radiation angiosarcomas
- Rare *ALK* rearrangements reported in epithelioid angiosarcoma ([PMID: 41836264](https://pubmed.ncbi.nlm.nih.gov/41836264/))

---

## 5. Environmental Information

### Environmental Factors

| Agent | Mechanism | Tumor Site | Key Evidence |
|---|---|---|---|
| **Vinyl chloride monomer (VCM)** | Chloroethylene oxide metabolite causes DNA adducts; K-ras mutations | Liver | [PMID: 945708](https://pubmed.ncbi.nlm.nih.gov/945708/), [PMID: 7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/) |
| **Thorotrast (thorium dioxide)** | Alpha radiation from retained contrast agent | Liver | [PMID: 7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/), [PMID: 9010458](https://pubmed.ncbi.nlm.nih.gov/9010458/) |
| **Inorganic arsenic** | Oxidative stress, epigenetic changes | Liver | [PMID: 10074736](https://pubmed.ncbi.nlm.nih.gov/10074736/), [PMID: 7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/) |
| **Aristolochic acid** | DNA adduct formation (SBS22 signature) | Liver (Asian) | [PMID: 41394772](https://pubmed.ncbi.nlm.nih.gov/41394772/) |
| **Ionizing radiation (therapeutic)** | DNA DSBs, genomic instability, MYC amplification | Breast, chest wall, larynx | [PMID: 38791996](https://pubmed.ncbi.nlm.nih.gov/38791996/) |
| **UV radiation** | Pyrimidine dimers, UV mutational signature (SBS7) | Head/neck skin | [PMID: 37106027](https://pubmed.ncbi.nlm.nih.gov/37106027/) |

- **CHEBI terms**: Vinyl chloride (CHEBI:28509), Arsenic (CHEBI:22632), Aristolochic acid (CHEBI:22574)

### Lifestyle Factors

No specific lifestyle factors (smoking, diet, exercise, alcohol) have been definitively linked to angiosarcoma risk beyond the occupational and environmental exposures listed above. Androgenic-anabolic steroid use has been associated with hepatic angiosarcoma in rare cases ([PMID: 7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/)).

### Infectious Agents

Viral hepatitis (HBV, HCV) has been investigated but not confirmed as a major risk factor for hepatic angiosarcoma. In a Taiwanese study, 2 of 9 patients had hepatitis C infection and none had hepatitis B, with no evidence supporting a major viral role ([PMID: 22200164](https://pubmed.ncbi.nlm.nih.gov/22200164/)).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

Angiosarcoma pathogenesis involves convergent activation of several key signaling cascades:

**VEGF/VEGFR Signaling (Primary Pathway)**
- *KDR* (VEGFR2) activating mutations drive autocrine/paracrine VEGF signaling
- *FLT4* (VEGFR3) amplification in radiation-associated AS enhances lymphangiogenic signaling
- VEGF stimulates tumor proliferation via VEGFR2 phosphorylation ([PMID: 23522954](https://pubmed.ncbi.nlm.nih.gov/23522954/))

**PI3K-AKT-mTOR Pathway**
- *PIK3CA* activating mutations (H1047R hotspot) found in both human AS and canine HSA
- mTOR/S6K activation demonstrated in vascular tumors including angiosarcoma; rapamycin inhibits growth ([PMID: 23938603](https://pubmed.ncbi.nlm.nih.gov/23938603/))
- Combined MEK + mTOR inhibition shows synergistic anti-tumor effects in AS tumorgrafts ([PMID: 25955301](https://pubmed.ncbi.nlm.nih.gov/25955301/))

**RAS-MAPK Pathway**
- *NRAS* activating mutations (G61R) in 24% of canine HSA
- *K-ras-2* mutations in hepatic AS (29%), characteristic of oxidative damage
- MEK inhibitor sensitivity demonstrated in AS tumorgraft models

**MYC Signaling (Radiation-Associated)**
- MYC amplification → upregulation of miR-17-92 cluster → suppression of THBS1 → enhanced angiogenesis ([PMID: 22383169](https://pubmed.ncbi.nlm.nih.gov/22383169/))
- MYC also drives cell cycle progression and metabolic reprogramming

**Wnt/β-Catenin Pathway**
- SFRP2 overexpression activates calcineurin/NFATc3 pathway and β-catenin signaling
- Anti-SFRP2 monoclonal antibody reduced angiosarcoma tumor volume by 58% (P = 0.004) ([PMID: 23604067](https://pubmed.ncbi.nlm.nih.gov/23604067/))

**Tie2/Angiopoietin Pathway**
- Tie2 universally expressed in human angiosarcomas
- Tie2 antagonism combined with VEGFR inhibition shows synergistic anti-tumor effects ([PMID: 22431921](https://pubmed.ncbi.nlm.nih.gov/22431921/))

### Causal Chain: From Trigger to Clinical Manifestation

```
Environmental trigger (radiation/UV/chemical)
    OR
Sporadic somatic mutations
        │
        ▼
Endothelial cell DNA damage / Oncogenic activation
(MYC amplification | KDR/PIK3CA mutations | K-ras mutations)
        │
        ▼
Constitutive activation of:
  - VEGF/VEGFR signaling → proliferation
  - PI3K/AKT/mTOR → survival, metabolism
  - RAS/MAPK → growth, differentiation
  - MYC → cell cycle, angiogenesis (via miR-17-92/THBS1)
        │
        ▼
Loss of cell cycle control (CDKN2A/p53 loss)
        │
        ▼
Uncontrolled endothelial proliferation
Aberrant vascular channel formation
        │
        ▼
Local invasion, hemorrhage, distant metastasis
```

### Cellular Processes

- **Angiogenesis** (GO:0001525) — central to tumor biology; tumor cells form dysfunctional vascular channels
- **Cell proliferation** (GO:0008283) — driven by VEGFR, PI3K, and MAPK signaling
- **Apoptosis resistance** (GO:0006915) — ROCK knockdown enhances survival through reduced caspase cleavage ([PMID: 22934846](https://pubmed.ncbi.nlm.nih.gov/22934846/))
- **Cell migration** (GO:0016477) — essential for invasion and metastasis
- **Inflammation** — gene expression profiling identifies inflammation as a distinguishing feature ([PMID: 21062482](https://pubmed.ncbi.nlm.nih.gov/21062482/))

### Cell Types Involved

- **Vascular endothelial cells** (CL:0000071) — cell of origin
- **Lymphatic endothelial cells** (CL:0002138) — particularly in radiation-associated AS
- **Tumor-infiltrating T cells** (CL:0000084) — CD3+, CD4+, CD8+ cells correlate with immunotherapy response
- **Tumor-associated macrophages** — contribute to immunosuppressive microenvironment

### Immune System Involvement

The tumor microenvironment of angiosarcoma is characterized by:
- Variable immune infiltration — higher TIL density correlates with better immunotherapy response
- PD-L1 expression in 32% of post-radiation breast AS specimens ([PMID: 41693531](https://pubmed.ncbi.nlm.nih.gov/41693531/))
- Upregulation of immune checkpoints (CTLA4, LAG3, PD-1, CD86) in tumor-infiltrating immune cells ([PMID: 40575034](https://pubmed.ncbi.nlm.nih.gov/40575034/))
- CXCL12-CXCR4 axis as a crucial mediator of the TME ([PMID: 40474296](https://pubmed.ncbi.nlm.nih.gov/40474296/))
- Lower immune infiltrate at tumor periphery associated with more aggressive behavior ([PMID: 31243333](https://pubmed.ncbi.nlm.nih.gov/31243333/))

### Single-Cell and Spatial Transcriptomics Findings

Single-cell RNA sequencing of breast angiosarcoma revealed significant differences in perivascular cells, fibroblasts, T cells, endothelial cells, and myeloid cells compared to invasive breast cancer. Key genes *FAT4*, *KDR*, *FN1*, and *KIT* were highly expressed in angiosarcoma endothelial cells, correlating with poor prognosis ([PMID: 40474296](https://pubmed.ncbi.nlm.nih.gov/40474296/)).

Spatial transcriptomics of head and neck angiosarcoma revealed topological immune landscapes with distinct spatial organization of immune cell populations ([PMID: 37106027](https://pubmed.ncbi.nlm.nih.gov/37106027/)).

Single-cell transcriptomic analysis of pancreatic angiosarcoma liver metastasis demonstrated marked upregulation of NF-κB, HIF-1, and MYC signaling, with an immunosuppressive and angiogenic tumor ecosystem ([PMID: 40575034](https://pubmed.ncbi.nlm.nih.gov/40575034/)).

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Sites:**

| Site | Frequency | UBERON Term |
|---|---|---|
| Skin (head/neck/scalp) | Most common overall | UBERON:0002097 (skin of body) |
| Breast | Common (primary and secondary) | UBERON:0000310 (breast) |
| Liver | 2–5% of cases | UBERON:0002107 (liver) |
| Heart (right atrium) | Rare | UBERON:0002078 (right cardiac atrium) |
| Spleen | Rare | UBERON:0002106 (spleen) |
| Deep soft tissue | ~24% in some series | UBERON:0000479 (tissue) |
| Bone | ~2% | UBERON:0001474 (bone element) |

**Common Metastatic Sites:**
- Lung (most common) — UBERON:0002048
- Liver — UBERON:0002107
- Bone — UBERON:0001474
- Lymph nodes — UBERON:0000029
- Brain — UBERON:0000955

### Tissue and Cell Level

- **Vascular endothelium** (UBERON:0001986) — tissue of origin
- **Lymphatic endothelium** — particularly in radiation-associated subtypes
- Cell populations: Endothelial cells (CL:0000071), pericytes (CL:0000669)

### Subcellular Level

- **Cell membrane** (GO:0005886) — VEGFR2, Tie2 receptor signaling
- **Nucleus** (GO:0005634) — MYC transcription factor activity, TP53 function
- **Cytoplasm** (GO:0005737) — PI3K/AKT/mTOR signaling cascade

---

## 8. Temporal Development

### Onset

- **Primary angiosarcoma**: Typically adult-onset, median age 69 years; primary breast AS median age 31 years
- **Radiation-associated AS**: Median latency 9.1 years (range 3.7–46.3) from index radiation
- **Chemically-induced hepatic AS**: Latency 20–40+ years from exposure onset
- **Onset pattern**: Insidious — often misdiagnosed due to nonspecific presentation

### Progression

**Staging**: The AJCC staging system for soft tissue sarcomas applies. At presentation, tumors are frequently high grade (Grade III 17.2%, Grade IV 19%, unknown 50.6%) but half are considered localized ([PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/)).

**Progression Rate**: Rapidly progressive — median PFS 7 months, median OS 20 months across all subtypes ([PMID: 40500777](https://pubmed.ncbi.nlm.nih.gov/40500777/)).

**Disease Course**: Aggressive, progressive course with high rates of local recurrence and distant metastasis. 12 of 36 patients (33%) developed local recurrence and 12 developed metastasis in one head/neck AS series ([PMID: 38391320](https://pubmed.ncbi.nlm.nih.gov/38391320/)).

### Critical Periods

Early diagnosis and complete surgical resection represent the critical window for optimal outcomes. Once metastatic disease develops, prognosis is uniformly poor. The median OS for patients with pulmonary metastases was only 5.0 months ([PMID: 28885371](https://pubmed.ncbi.nlm.nih.gov/28885371/)).

---

## 9. Inheritance and Population

### Epidemiology

- **Incidence**: Age-adjusted incidence rate approximately 1.4 per million per year ([PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/))
- **Prevalence**: Extremely rare — <1–2% of all soft tissue sarcomas
- **SEER data**: 5,135 patients identified between 1975 and 2016

### Inheritance Patterns

Angiosarcoma is predominantly a sporadic cancer without Mendelian inheritance. However:
- **Li-Fraumeni syndrome** (autosomal dominant *TP53* mutations) — increased risk, especially with radiation exposure
- **Xeroderma pigmentosum** (autosomal recessive) — increased risk of UV-associated AS
- **Familial cases**: Rare; a *CHEK2* p.P35L variant was identified in a family with cardiac angiosarcoma ([PMID: 36387164](https://pubmed.ncbi.nlm.nih.gov/36387164/))

### Population Demographics

- **Sex ratio**: Overall slight male predominance (46% male in SEER); hepatic AS has strong male predominance (~3:1); breast AS almost exclusively female
- **Race/Ethnicity**: Non-Hispanic Caucasian 75.4%; Non-Hispanic Asians/Pacific Islanders overrepresented in hepatic AS (17%) ([PMID: 39676119](https://pubmed.ncbi.nlm.nih.gov/39676119/))
- **Age distribution**: Predominantly elderly; median age 69 years overall; younger for primary breast AS (median 31)
- **Geographic variation**: Higher liver AS incidence in Asia (aristolochic acid exposure); historically elevated in industrial areas with vinyl chloride exposure

---

## 10. Diagnostics

### Histopathology and Immunohistochemistry

Histological diagnosis relies on identification of malignant endothelial cells forming abnormal vascular channels. Morphologic spectrum ranges from well-differentiated vasoformative patterns to poorly differentiated solid sheets of epithelioid or spindle cells.

**Essential IHC Panel:**

| Marker | Sensitivity | Specificity | Notes |
|---|---|---|---|
| **CD31** | ~100% | High | Most sensitive endothelial marker |
| **ERG** | ~95% | High | Nuclear transcription factor |
| **CD34** | 40–80% | Moderate | May be negative in poorly differentiated AS |
| **FLI1** | High | Moderate | Nuclear marker |
| **Factor VIII** | Low-moderate | High | Less sensitive |
| **D2-40** | Variable | — | Positive in lymphatic differentiation |
| **Claudin-5** | 100% in AS | High vs mesothelioma | Distinguishes AS from mesothelioma ([PMID: 32777673](https://pubmed.ncbi.nlm.nih.gov/32777673/)) |

**MYC IHC**: c-MYC immunostain is consistently positive in radiation-associated AS and negative/weakly positive in primary AS — serves as a diagnostic marker for distinguishing these subtypes ([PMID: 34392127](https://pubmed.ncbi.nlm.nih.gov/34392127/), [PMID: 24457083](https://pubmed.ncbi.nlm.nih.gov/24457083/)).

**MYC FISH**: Confirms MYC amplification with 100% concordance with protein expression in mammary AS ([PMID: 24457083](https://pubmed.ncbi.nlm.nih.gov/24457083/)).

### Imaging Studies

- **MRI**: Preferred for soft tissue characterization; hemorrhagic, heterogeneously enhancing masses
- **CT**: Assessment of extent and metastatic disease
- **PET-CT**: Useful for staging and response assessment
- **Cardiac MRI**: Superior to echocardiography for detecting cardiac masses ([PMID: 28885371](https://pubmed.ncbi.nlm.nih.gov/28885371/))

### Molecular/Genetic Testing

- **Targeted NGS panels**: Identify actionable mutations in *KDR*, *PIK3CA*, *TP53*, *NRAS*
- **MYC FISH**: Diagnostic for radiation-associated vs primary AS
- **TMB assessment**: Predictive of immunotherapy response in UV/radiation-associated subtypes
- **Whole-exome sequencing**: For comprehensive genomic profiling and germline testing

### Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| Atypical vascular lesion (AVL) | No MYC amplification; bland cytology |
| Kaposi sarcoma | HHV-8 positive |
| Epithelioid hemangioendothelioma | WWTR1-CAMTA1 fusion; less aggressive |
| Melanoma | S100+, SOX10+, Melan-A+; CD31-negative |
| Poorly differentiated carcinoma | Cytokeratin+, CD31-negative (note: AS can express keratins) |
| Pleural mesothelioma | Calretinin+, claudin-5 negative ([PMID: 32777673](https://pubmed.ncbi.nlm.nih.gov/32777673/)) |

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Metric | Value | Source |
|---|---|---|
| **Overall 5-year survival** | 26.7% (95% CI 25.4–28.1%) | [PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/) |
| **Median PFS** | 7 months | [PMID: 40500777](https://pubmed.ncbi.nlm.nih.gov/40500777/) |
| **Median OS** | 20 months | [PMID: 40500777](https://pubmed.ncbi.nlm.nih.gov/40500777/) |
| **5-year OS, cutaneous AS** | 12% (single cohort) | [PMID: 40712262](https://pubmed.ncbi.nlm.nih.gov/40712262/) |
| **5-year OS, bone AS** | 15% | [PMID: 40914676](https://pubmed.ncbi.nlm.nih.gov/40914676/) |
| **Hepatic AS 3-year survival** | 6.7% | [PMID: 39676119](https://pubmed.ncbi.nlm.nih.gov/39676119/) |
| **Cutaneous vs non-cutaneous median OS** | 36 vs 9 months (P = 0.04) | [PMID: 40712262](https://pubmed.ncbi.nlm.nih.gov/40712262/) |
| **Pulmonary metastatic disease median OS** | 5.0 months | [PMID: 28885371](https://pubmed.ncbi.nlm.nih.gov/28885371/) |

### Prognostic Factors

**Negative prognostic factors (multivariate):**
- Age > 70 years (HR 1.67, P < 0.05)
- No surgical intervention (HR 2.29, P < 0.001)
- Distant stage (HR 2.54, P < 0.001)
- Angiosarcoma histology (HR 2.95 for local relapse in superficial sarcomas, P < 0.001) ([PMID: 40961809](https://pubmed.ncbi.nlm.nih.gov/40961809/))
- Higher tumor grade
- Larger tumor size
- Non-cutaneous location

**Positive prognostic factors:**
- Female sex (HR 0.68 for hepatic AS)
- Localized disease
- Complete surgical resection with R0 margins
- Younger age

### Complications

- Hemorrhage (tumor rupture, especially splenic and hepatic)
- Disseminated intravascular coagulation
- Cardiac tamponade (cardiac AS)
- Treatment-related thrombotic microangiopathy ([PMID: 41177756](https://pubmed.ncbi.nlm.nih.gov/41177756/))

---

## 12. Treatment

### Surgical Treatment

**Wide surgical excision** is the mainstay of treatment for localized angiosarcoma. In SEER data, 66.1% of patients underwent surgery ([PMID: 35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/)). Complete resection with negative margins (R0) is critical — patients without R0 margins had significantly worse outcomes (HR 2.60 for LRFS, P < 0.001; HR 2.02 for OS, P < 0.001) ([PMID: 40961809](https://pubmed.ncbi.nlm.nih.gov/40961809/)).

- **MAXO terms**: MAXO:0000004 (surgical procedure), MAXO:0000015 (mastectomy)

### Chemotherapy

**First-line agents:**
- **Paclitaxel** — anti-angiogenic and cytotoxic; widely used for cutaneous AS
- **Doxorubicin/liposomal doxorubicin** — standard for soft tissue sarcomas
- **Gemcitabine** ± docetaxel — alternative regimen

**Neoadjuvant chemotherapy**: Applied to improve R0 resection rates; response evenly divided between poor (Grades I–II) and good responders (Grades III–IV) ([PMID: 38722225](https://pubmed.ncbi.nlm.nih.gov/38722225/)).

- **MAXO terms**: MAXO:0000058 (chemotherapy)

### Immunotherapy

Immune checkpoint inhibitors represent an emerging treatment paradigm, particularly for UV- and radiation-associated subtypes:

**Cemiplimab (anti-PD-1)**: Phase II CEMangio trial in secondary AS — ORR 27.8% (4 PR, 1 CR), median PFS 3.7 months, median OS 13.1 months. High intratumoral CD3+ (P = 0.019), CD4 (P = 0.046), and CD8+ density associated with response ([PMID: 40632032](https://pubmed.ncbi.nlm.nih.gov/40632032/)).

**Cabozantinib + nivolumab**: Alliance A091902 second-line — ORR 59%, demonstrating significant efficacy in both cutaneous and non-cutaneous AS ([PMID: 40056281](https://pubmed.ncbi.nlm.nih.gov/40056281/)).

**Dual ICI (SWOG S1609)**: ORR 25% — suggests potential benefit but limited activity in cutaneous disease ([PMID: 40056281](https://pubmed.ncbi.nlm.nih.gov/40056281/)).

**Pembrolizumab**: Sustained response reported in PD-L1-expressing angiosarcoma; one patient achieved marked liver disease shrinkage with no new lesions for 8+ months off therapy ([PMID: 28716069](https://pubmed.ncbi.nlm.nih.gov/28716069/)).

- **MAXO terms**: MAXO:0001360 (immune checkpoint inhibitor therapy)

### Targeted Therapy

- **Anti-VEGF/VEGFR agents**: Bevacizumab, pazopanib, sorafenib, sunitinib — variable efficacy; sunitinib showed limited activity against AS in preclinical models ([PMID: 23522954](https://pubmed.ncbi.nlm.nih.gov/23522954/))
- **mTOR inhibitors**: Rapamycin shows synergy with MEK inhibitors in AS ([PMID: 25955301](https://pubmed.ncbi.nlm.nih.gov/25955301/))
- **Anti-SFRP2 antibody**: Reduced AS tumorgraft volume by 58% (P = 0.004) ([PMID: 23604067](https://pubmed.ncbi.nlm.nih.gov/23604067/))
- **CDK4/6 inhibitors**: Suggested by frequent cell cycle dysregulation ([PMID: 41246336](https://pubmed.ncbi.nlm.nih.gov/41246336/))
- **Anlotinib, lenvatinib**: Multi-kinase inhibitors used in refractory disease

### Radiation Therapy

Adjuvant radiation therapy is used for local control, particularly for head/neck cutaneous AS. However, radiation is used cautiously for radiation-associated subtypes.

- **MAXO terms**: MAXO:0000014 (radiation therapy)

### Experimental Treatments

- **Photodynamic therapy (PDT)**: Promising for recurrent superficial cutaneous AS ([PMID: 40364848](https://pubmed.ncbi.nlm.nih.gov/40364848/))
- **IFN-alpha**: Inhibited angiosarcoma growth in murine models by 71–79% through angiogenesis inhibition ([PMID: 16689662](https://pubmed.ncbi.nlm.nih.gov/16689662/))
- **Anti-extracellular vimentin vaccine (iBoost)**: In canine HSA, median OS increased from 136 to 235 days when combined with doxorubicin ([PMID: 41009669](https://pubmed.ncbi.nlm.nih.gov/41009669/))
- **Toripalimab + gemcitabine/nab-paclitaxel**: Achieved 9-month partial response in radiation-associated laryngeal AS ([PMID: 41496010](https://pubmed.ncbi.nlm.nih.gov/41496010/))

---

## 13. Prevention

### Primary Prevention

- **Occupational safety**: Elimination of vinyl chloride exposure through engineering controls and regulatory limits — largely achieved in developed countries
- **Arsenic exposure reduction**: Clean water initiatives in endemic areas
- **UV protection**: Sun-protective measures for head/neck AS prevention
- **Judicious use of radiotherapy**: Appropriate patient selection and field design

### Secondary Prevention

- **Surveillance after breast radiation**: Clinical monitoring for skin changes in irradiated fields, given 3-fold increased incidence of secondary breast AS. Hemangiosarcoma SIR was 27.11 (95% CI 21.6–33.61) on breast/trunk skin after breast radiation ([PMID: 38457179](https://pubmed.ncbi.nlm.nih.gov/38457179/))
- **Monitoring chronic lymphedema patients**: Regular examination for Stewart-Treves syndrome
- **Germline TP53 testing**: In patients with early-onset or radiation-associated AS, to identify Li-Fraumeni syndrome for cancer surveillance in families

### Tertiary Prevention

- Close surveillance for local recurrence and metastatic disease after treatment
- Multidisciplinary follow-up with sarcoma specialists
- Prompt treatment of recurrences

---

## 14. Other Species / Natural Disease

### Canine Hemangiosarcoma

Canine hemangiosarcoma (HSA) is the most important comparative model for human angiosarcoma. It is a common spontaneous malignancy in dogs, particularly in golden retrievers, German shepherds, and Labrador retrievers.

**Taxonomy**: *Canis lupus familiaris* (NCBI Taxon: 9615)

**Genomic Similarities**: Whole-exome sequencing of 47 golden retriever HSAs revealed striking parallels with human angiosarcoma:
- *PIK3CA* mutations: 46% (vs. 70% in human primary mammary AS)
- *TP53* mutations: 66%
- *NRAS* mutations: 24% (G61R hotspot)
- *PLCG1* mutations: 4%
- *PTEN* mutations: 6%

"Overall, we identified potential driver mutations in over 90% of the cases, including well-documented (in human cancers) oncogenic mutations in PIK3CA (46%), PTEN (6%), PLCG1(4%), and TP53 (66%), as well as previously undetected recurrent activating mutations in NRAS (24%)" ([PMID: 32210430](https://pubmed.ncbi.nlm.nih.gov/32210430/)).

"Canine tumors share mutational hotspots with human tumors in oncogenes including PIK3CA, KRAS, NRAS, BRAF, KIT and EGFR. Hotspot mutations with significant association to tumor type include NRAS G61R and PIK3CA H1047R in hemangiosarcoma" ([PMID: 37414794](https://pubmed.ncbi.nlm.nih.gov/37414794/)).

**Clinical Features**: Splenic HSA is the most common form, characterized by rapid growth, splenic rupture, and hemoperitoneum. Median survival after splenectomy alone is 1–3 months; with adjuvant doxorubicin, 5–7 months ([PMID: 41009669](https://pubmed.ncbi.nlm.nih.gov/41009669/)). Stage III disease and hepatic metastases are associated with significantly decreased survival (P < 0.001) ([PMID: 41742582](https://pubmed.ncbi.nlm.nih.gov/41742582/)).

**Gene expression profiling** identified inflammation and angiogenesis as distinguishing features of canine HSA compared to non-malignant endothelial cells ([PMID: 21062482](https://pubmed.ncbi.nlm.nih.gov/21062482/)).

### Other Species

Angiosarcoma/hemangiosarcoma is recognized in multiple mammalian species but is particularly prevalent in dogs. The shared mutational landscape and biological behavior make canine HSA an invaluable One Health model for drug development.

---

## 15. Model Organisms

### In Vivo Models

**Canine Hemangiosarcoma (Spontaneous)**
- **Model type**: Large animal, spontaneous
- **Phenotype recapitulation**: Excellent — shared driver mutations, aggressive behavior, vascular origin, metastatic patterns
- **Applications**: Drug development, immunotherapy testing, biomarker discovery
- **Limitations**: Heterogeneous genetic background; breed-specific predispositions may not fully reflect human disease
- **Key cell isolates**: Used for tumorgraft models and in vitro drug screening

**Murine Models**
- **SVR cell line**: Transformed murine endothelial cells expressing oncogenic H-ras; forms angiosarcomas in nude mice ([PMID: 16689662](https://pubmed.ncbi.nlm.nih.gov/16689662/))
- **MS1-VEGF cell line**: Murine endothelial cells expressing VEGF; low-grade angiosarcoma model
- **HAMON xenograft**: Human angiosarcoma cell line xenograft in immunodeficient mice; expresses CD31, VEGFR2 ([PMID: 23522954](https://pubmed.ncbi.nlm.nih.gov/23522954/))
- **Applications**: Drug testing (MEK/mTOR inhibitors, anti-angiogenic agents, immunotherapy)

### In Vitro Models

- Human angiosarcoma cell lines (limited availability)
- Canine HSA cell isolates — used for drug combination studies
- Patient-derived xenografts (PDX) / tumorgrafts

### Model Limitations

- Murine xenograft models lack intact immune system
- Cell line models may not capture tumor heterogeneity
- Canine HSA, while closely related, is not identical to human AS (e.g., MYC amplification is not a feature of canine HSA)
- Limited availability of human AS cell lines due to disease rarity

---

## Key Findings — Detailed Evidence

### Finding 1: Angiosarcoma is a Rare, Aggressive Vascular Malignancy with Poor Prognosis

Analysis of 5,135 patients in the SEER database (1975–2016) demonstrated an age-adjusted incidence rate of approximately 1.4 per million, with the majority of patients presenting as non-Hispanic Caucasian (75.4%) with a median age of 69 years. Tumor grades were predominantly high at presentation (Grade III 17.2%, Grade IV 19%), and the overall 5-year survival was 26.7% (95% CI 25.4–28.1%). A single-institution cohort of 128 patients confirmed poor outcomes with median PFS of 7 months and median OS of 20 months. Importantly, non-cutaneous angiosarcoma had significantly worse median OS than cutaneous disease (9 vs 36 months, P = 0.04), highlighting the prognostic importance of anatomic site.

### Finding 2: MYC Amplification Defines Radiation-Associated Angiosarcoma

MYC amplification at 8q24 (5- to 20-fold) is present in 100% of radiation-associated breast angiosarcomas but in only 0–7% of primary angiosarcomas, establishing it as both a diagnostic biomarker and a mechanistic driver. FLT4 (VEGFR3) coamplification occurs in 25% of secondary AS. Downstream, MYC amplification drives upregulation of the miR-17-92 cluster and suppression of the anti-angiogenic factor thrombospondin-1, providing a mechanistic link between MYC and the angiogenic phenotype.

### Finding 3: Primary Angiosarcoma Has Distinct Angiogenic Driver Mutations

Primary mammary angiosarcomas harbor recurrent activating mutations in *KDR* (70%), *PIK3CA/PIK3R1* (70%), and *PTPRB* (30%), all at higher frequencies than in angiosarcoma across all sites. The KDR T771R hotspot mutation shows evidence of biallelism, indicating strong selection for constitutive VEGFR2 activation. Head/neck UV-associated angiosarcomas have a distinct mutational profile dominated by CSMD3, LRP1B, MUC16, POT1, and TP53 mutations with high TMB.

### Finding 4: Canine Hemangiosarcoma as a Comparative Model

Canine hemangiosarcoma shares driver mutations in *PIK3CA* (46%), *TP53* (66%), and *NRAS* (24%) with human angiosarcoma, with identical hotspot mutations (PIK3CA H1047R, NRAS G61R). This genomic convergence, combined with similar clinical behavior, validates canine HSA as a One Health model for therapeutic development.

### Finding 5: Immunotherapy Shows Emerging Activity

Immune checkpoint inhibitors demonstrate meaningful activity in angiosarcoma, particularly in UV- and radiation-associated subtypes. The CEMangio phase II trial showed an ORR of 27.8% with cemiplimab in secondary AS, with high intratumoral CD3+ and CD8+ density predicting response. The cabozantinib-nivolumab combination achieved a remarkable 59% ORR in second-line, suggesting synergy between anti-angiogenic and immune checkpoint blockade.

### Finding 6: Environmental Carcinogens Cause Distinct Subtypes

Vinyl chloride, thorotrast, arsenic, ionizing radiation, and UV radiation each cause distinct angiosarcoma subtypes through different mutagenic mechanisms — from oxidative DNA damage (K-ras mutations in hepatic AS) to DNA adduct formation (aristolochic acid SBS22 signature) to direct chromosomal amplification events (MYC in radiation-associated AS).

---

## Mechanistic Model: Integrated Pathogenesis of Angiosarcoma Subtypes

```
┌─────────────────────────────────────────────────────────────────┐
│                    ANGIOSARCOMA SUBTYPES                        │
├─────────────┬──────────────┬────────────┬──────────┬────────────┤
│  Primary/   │  Radiation-  │ UV-Head/   │ Chemical │ Lymphedema │
│  Sporadic   │  Associated  │   Neck     │ Hepatic  │ (Stewart-  │
│             │              │            │          │  Treves)   │
├─────────────┼──────────────┼────────────┼──────────┼────────────┤
│ KDR (70%)   │ MYC amp      │ UV sig     │ K-ras    │ Unknown    │
│ PIK3CA(70%) │ (100%)       │ (SBS7)     │ (29%)    │ drivers    │
│ PTPRB (30%) │ FLT4 (25%)   │ High TMB   │ SBS22    │            │
│             │ CDKN2A loss  │ CSMD3,POT1 │ (AA)     │            │
├─────────────┼──────────────┼────────────┼──────────┼────────────┤
│             │              │            │          │            │
│   VEGFR2 ←──→  MYC/miR ←──→  DNA       │  Oxid.  │ Chronic    │
│   PI3K/AKT  │  17-92      │  repair    │  damage  │ inflam.    │
│   mTOR      │  THBS1↓     │  defects   │          │            │
├─────────────┴──────────────┴────────────┴──────────┴────────────┤
│            CONVERGENT DOWNSTREAM PATHWAYS                       │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ Angiogenesis ↑ │ Cell cycle ↑ │ Apoptosis ↓        │       │
│  │ VEGF/VEGFR    │ CDKN2A loss  │ TP53 loss           │       │
│  │ Tie2/Ang      │ MYC          │ PI3K/AKT            │       │
│  └─────────────────────────────────────────────────────┘       │
│                          ↓                                      │
│           Malignant Endothelial Proliferation                   │
│           Aberrant Vascular Channel Formation                   │
│           Local Invasion → Hemorrhage → Metastasis              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Evidence Base

### Landmark Papers

| Paper | PMID | Key Contribution |
|---|---|---|
| SEER analysis (2022) | [35478727](https://pubmed.ncbi.nlm.nih.gov/35478727/) | Comprehensive epidemiology: 5,135 patients, 26.7% 5-year OS |
| Manner et al. (2010) | [20949568](https://pubmed.ncbi.nlm.nih.gov/20949568/) | MYC amplification in 100% of secondary AS, FLT4 in 25% |
| Italiano et al. (2020) | [32123305](https://pubmed.ncbi.nlm.nih.gov/32123305/) | KDR/PIK3CA/PTPRB mutations in primary mammary AS |
| Wang et al. (2020) | [32210430](https://pubmed.ncbi.nlm.nih.gov/32210430/) | Canine HSA genomic landscape — PIK3CA, TP53, NRAS drivers |
| CEMangio trial (2025) | [40632032](https://pubmed.ncbi.nlm.nih.gov/40632032/) | Cemiplimab ORR 27.8% in secondary AS with biomarker correlates |
| US hepatic AS survey (1979) | [7199426](https://pubmed.ncbi.nlm.nih.gov/7199426/) | Established VCM, thorotrast, arsenic as causes |
| Guo et al. (2012) | [22383169](https://pubmed.ncbi.nlm.nih.gov/22383169/) | MYC → miR-17-92 → THBS1 mechanistic link |
| Angiosarcoma Project (2020) | [32042194](https://pubmed.ncbi.nlm.nih.gov/32042194/) | Patient-partnered genomic and clinical discovery platform |
| Spatial transcriptomics (2023) | [37106027](https://pubmed.ncbi.nlm.nih.gov/37106027/) | UV signature and immune topology in head/neck AS |
| Genomic comparison rad vs sporadic (2019) | [31243333](https://pubmed.ncbi.nlm.nih.gov/31243333/) | CDKN2A/B losses, transcriptomic subtypes |

---

## Limitations and Knowledge Gaps

1. **Rarity precludes large randomized trials**: Most treatment evidence comes from retrospective series, small phase II trials, and case reports. No phase III randomized trials exist for any angiosarcoma treatment.

2. **Molecular heterogeneity**: The marked molecular diversity across subtypes makes unified treatment approaches challenging. Better subtype-specific trial designs are needed.

3. **Limited understanding of primary sporadic AS pathogenesis**: While radiation-associated and chemical subtypes have clear initiating events, the triggers for primary sporadic AS remain largely unknown.

4. **Biomarker validation**: Predictive biomarkers for immunotherapy response (TMB, PD-L1, TIL density) require prospective validation in larger cohorts.

5. **Incomplete genomic landscape**: Whole-genome sequencing has been performed on limited cohorts; non-coding mutations, structural variants, and epigenomic alterations remain underexplored.

6. **Lack of standardized staging**: The AJCC staging system for soft tissue sarcomas may not adequately capture the prognostic nuances of angiosarcoma across different anatomic sites.

7. **Limited cell line resources**: Few authenticated human angiosarcoma cell lines exist, hampering preclinical drug development.

8. **Underrepresentation of non-Western populations**: Most genomic and clinical data derive from Western populations; the role of aristolochic acid in Asian liver AS is only now being characterized.

---

## Proposed Follow-up Experiments/Actions

1. **Prospective biomarker-stratified clinical trials**: Design trials stratifying patients by molecular subtype (MYC-amplified, KDR-mutant, high-TMB) to match targeted therapies to specific driver alterations.

2. **Combinatorial immunotherapy-TKI trials**: Given the 59% ORR with cabozantinib-nivolumab, expand this approach with additional anti-angiogenic/ICI combinations across subtypes.

3. **Comprehensive genomic profiling**: Perform whole-genome sequencing on a large, multi-institutional angiosarcoma cohort to identify non-coding drivers, structural variants, and novel therapeutic targets.

4. **Canine comparative trials**: Leverage canine HSA as a platform for rapid therapeutic testing — particularly for PIK3CA inhibitors, NRAS-targeted approaches, and immunotherapy combinations.

5. **Single-cell multi-omics**: Expand scRNA-seq studies to characterize the tumor microenvironment across subtypes, with focus on identifying determinants of immunotherapy response.

6. **Liquid biopsy development**: Develop ctDNA assays for MYC amplification, KDR mutations, and other actionable alterations to enable non-invasive diagnosis and monitoring.

7. **CDK4/6 inhibitor trials**: Given frequent CDKN2A loss across subtypes, test CDK4/6 inhibitors (palbociclib, ribociclib) as single agents and in combinations.

8. **MEK + mTOR combination trials**: Translate preclinical synergy data into clinical trials for patients with RAS/MAPK pathway-activated angiosarcomas.

9. **Epidemiological surveillance**: Monitor aristolochic acid-associated liver angiosarcoma in Asian populations and implement public health interventions.

10. **Patient-partnered research**: Expand the Angiosarcoma Project (ASCProject) to increase patient enrollment, diversity, and longitudinal follow-up for this rare disease.

---

*Report generated: 2026-05-05*
*Sources: SEER database analyses, genomic profiling studies, clinical trials, systematic reviews, and comparative oncology studies spanning 93 reviewed publications.*
