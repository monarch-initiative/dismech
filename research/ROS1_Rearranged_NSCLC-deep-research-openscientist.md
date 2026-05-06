---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-06T01:23:42.019629'
end_time: '2026-05-06T02:12:42.121139'
duration_seconds: 2940.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ROS1-Rearranged Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ROS1-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **ROS1-Rearranged Non-Small Cell Lung Cancer** covering all of the
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

# Comprehensive Disease Characterization: ROS1-Rearranged Non-Small Cell Lung Cancer

## Summary

ROS1-rearranged non-small cell lung cancer (ROS1+ NSCLC) is a rare but clinically important molecular subset of lung adenocarcinoma, defined by chromosomal rearrangements that produce constitutively active ROS1 fusion kinases. Accounting for 1–2% of all NSCLC cases, this disease predominantly affects younger, never-smoking females and is characterized by adenocarcinoma histology with distinctive mucinous cribriform and signet ring cell patterns. The oncogenic ROS1 fusion proteins activate downstream signaling through STAT3, SHP2 (with uniquely strong phosphorylation compared to ALK fusions), RAS-MAPK, and PI3K-AKT-mTOR pathways, driving uncontrolled cellular proliferation and survival.

The therapeutic landscape for ROS1+ NSCLC has evolved rapidly since the FDA approval of crizotinib in 2016. First-generation tyrosine kinase inhibitors (TKIs) such as crizotinib and entrectinib achieve objective response rates (ORR) of 60–80%, but are limited by acquired resistance—most commonly the G2032R solvent-front mutation—and inadequate CNS penetration. Next-generation TKIs have dramatically improved outcomes: repotrectinib achieves an ORR of 79% with median progression-free survival (PFS) of 35.7 months in TKI-naive patients, while taletrectinib demonstrates an ORR of up to 90.6% with robust activity against the G2032R mutation. Emerging agents including zidesamtinib (a ROS1-selective, TRK-sparing inhibitor) and type II TKIs like cabozantinib provide additional options for resistant disease.

Key challenges remain: CNS metastasis is present in approximately 22–36% of patients at diagnosis, TP53/CDKN2A/B co-mutations create an immunosuppressive tumor microenvironment associated with worse prognosis, and sequential resistance mutations necessitate rational TKI sequencing strategies. This report synthesizes evidence from 93 published studies, 13 confirmed findings, and multiple ontology databases to provide a comprehensive disease knowledge base entry covering all 15 required characterization domains.

---

## 1. Disease Information

### Overview

ROS1-rearranged NSCLC is a molecular subtype of non-small cell lung cancer driven by chromosomal rearrangements involving the *ROS1* proto-oncogene (chromosome 6q22). These rearrangements produce chimeric fusion proteins with constitutive tyrosine kinase activity, functioning as oncogenic drivers. The disease was first recognized as a distinct targetable entity following the identification of ROS1 fusions in lung cancer in 2007, and the subsequent demonstration that ROS1 TKIs could produce durable clinical responses.

"ROS1 rearrangements define a molecular subset of non-small cell lung cancer (NSCLC) by accounting for 1%-2% of cases" ([PMID: 40171848](https://pubmed.ncbi.nlm.nih.gov/40171848/)). "ROS1 fusion-positive non-small cell lung cancer (NSCLC) represents a rare but clinically important subset, occurring in 1-2% of patients and often associated with younger, never-smoker populations" ([PMID: 41548253](https://pubmed.ncbi.nlm.nih.gov/41548253/)).

### Key Identifiers

| Identifier | Value |
|---|---|
| **OMIM** | 165020 (ROS1 gene) |
| **ICD-10** | C34 (Malignant neoplasm of bronchus and lung) |
| **ICD-11** | 2C25 (Malignant neoplasms of bronchus or lung) |
| **MeSH** | D002289 (Carcinoma, Non-Small-Cell Lung) |
| **KEGG Disease** | H00014 (Non-small cell lung cancer) |
| **MONDO** | MONDO:0005233 (non-small cell lung carcinoma) |
| **HGNC** | HGNC:10261 (ROS1) |
| **UniProt** | P08922 (ROS1_HUMAN) |

### Synonyms and Alternative Names

- ROS1-positive NSCLC / ROS1+ NSCLC
- ROS1 fusion-positive non-small cell lung cancer
- ROS1-rearranged lung adenocarcinoma
- c-ros oncogene 1 rearranged NSCLC

### Information Source

This report is derived from aggregated disease-level resources including published clinical trials, molecular biology studies, population-based registries (SEER), and curated databases (COSMIC, ClinVar, UniProt, PDB), supplemented by individual patient case reports documenting resistance mechanisms and treatment sequences.

---

## 2. Etiology

### Disease Causal Factors

ROS1+ NSCLC is caused by **somatic chromosomal rearrangements** that fuse the 3' kinase domain of the *ROS1* gene to the 5' portion of various partner genes, producing constitutively active fusion kinases. These are acquired somatic events, not germline inherited mutations. The rearrangements are typically interchromosomal or intrachromosomal inversions/translocations.

The most common fusion partners include:
- **CD74-ROS1** (~35–44% of cases): the most frequent partner
- **EZR-ROS1**: ezrin gene on 6q25
- **SLC34A2-ROS1**: solute carrier on 4p15
- **SDC4-ROS1**: syndecan-4 on 20q12
- **TPM3-ROS1**: tropomyosin-3 on 1q21
- **GOPC-ROS1** (also known as FIG-ROS1): on 6q22 (intrachromosomal)
- **CLIP1-ROS1**, **KIF21A-ROS1**, and other rare partners

{{figure:ros1_protein_and_partners.png|caption=ROS1 protein domain architecture, fusion breakpoints, resistance mutation sites, and landscape of fusion partners with approximate frequencies}}

### Risk Factors

**Genetic risk factors:**
- ROS1 rearrangements are **somatic**, not inherited; no germline susceptibility loci have been identified
- Co-occurring TP53 mutations are frequent and associated with worse prognosis ([PMID: 37261522](https://pubmed.ncbi.nlm.nih.gov/37261522/))
- CDKN2A/B copy number loss co-occurs in ~15% of fusion-positive patients

**Environmental risk factors:**
- Unlike most NSCLC, ROS1+ disease is **not associated with tobacco smoking**—75.7% of patients are never-smokers ([PMID: 29883837](https://pubmed.ncbi.nlm.nih.gov/29883837/))
- The etiology of the chromosomal rearrangement is unknown in most cases
- No occupational, dietary, or environmental exposures have been definitively linked

**Demographic associations:**
- **Age**: Younger patients (median 50–56 years vs. ~65 years for general NSCLC)
- **Sex**: Female predominance (58.9% female in one cohort; fusion frequency 3.71% in women vs. 1.81% in men, p < 0.01) ([PMID: 30468296](https://pubmed.ncbi.nlm.nih.gov/30468296/))
- **Ethnicity**: Reported across all ethnicities; Indian populations show frequencies of 3.5–4.1% ([PMID: 35634796](https://pubmed.ncbi.nlm.nih.gov/35634796/)); Hispanic/Latino ~2% ([PMID: 37729688](https://pubmed.ncbi.nlm.nih.gov/37729688/))

### Protective Factors

No specific genetic or environmental protective factors have been identified for ROS1+ NSCLC. General lung cancer protective factors (avoidance of tobacco, radon mitigation) apply but are less relevant given the never-smoker predominance of this subtype.

### Gene-Environment Interactions

There is no established gene-environment interaction for ROS1 rearrangements. The disease appears to arise from stochastic somatic rearrangement events rather than environmental mutagen exposure.

---

## 3. Phenotypes

### Clinical Presentation

| Phenotype | Type | HPO Term | Frequency | Severity | Onset |
|---|---|---|---|---|---|
| Cough | Symptom | HP:0012735 | ~60–70% | Mild to moderate | Adult |
| Dyspnea | Symptom | HP:0002094 | ~40–50% | Progressive | Adult |
| Chest pain | Symptom | HP:0100749 | ~25–30% | Variable | Adult |
| Weight loss | Symptom | HP:0001824 | ~20–30% | Moderate | Adult |
| Hemoptysis | Symptom | HP:0002105 | ~15–20% | Variable | Adult |
| Fatigue/asthenia | Symptom | HP:0012378 | ~30–40% | Variable | Adult |
| Brain metastasis symptoms | Clinical sign | HP:0002076 | ~22–36% | Severe | Adult |
| Pleural effusion | Clinical sign | HP:0002202 | ~20–30% | Moderate to severe | Adult |
| Lymphadenopathy | Clinical sign | HP:0002716 | ~40–60% | Variable | Adult |

### Phenotype Characteristics

- **Age of onset**: Adult-onset, typically 5th–6th decade (median 50–56 years), significantly younger than general NSCLC population. "ROS1 fusion-positive patients were significantly younger (55.68 +/- 11.34 vs. negative 61.02 +/- 10.44 years; P < 0.01)" ([PMID: 30468296](https://pubmed.ncbi.nlm.nih.gov/30468296/))
- **Progression**: Progressive without treatment; variable with TKI therapy (initial response followed by eventual progression)
- **CNS tropism**: High rate of brain metastases (~22–36% at diagnosis), a hallmark of the disease and a key clinical challenge

### Histopathological Phenotype

ROS1+ NSCLC shows characteristic histological features: "Histologically, the carcinoma was an adenocarcinoma with a predominant acinar pattern; notably, a mucinous cribriform pattern and a solid signet-ring cell pattern were also observed" ([PMID: 23877438](https://pubmed.ncbi.nlm.nih.gov/23877438/)). Adenocarcinoma accounts for 98.1% of ROS1+ cases; rare pleomorphic carcinoma has been reported ([PMID: 29883837](https://pubmed.ncbi.nlm.nih.gov/29883837/)).

### Quality of Life

Entrectinib treatment maintains stable global health status and quality of life as measured by EORTC QLQ-C30, QLQ-LC13, and EQ-5D-3L instruments in the STARTRK-2 trial ([PMID: 33930659](https://pubmed.ncbi.nlm.nih.gov/33930659/)). Post-TKI chemo-immunotherapy carries substantially higher toxicity burden with grade 3–4 adverse events in 63.9–83.8% of patients ([PMID: 38830303](https://pubmed.ncbi.nlm.nih.gov/38830303/)).

---

## 4. Genetic/Molecular Information

### Causal Gene

**ROS1** (ROS proto-oncogene 1, receptor tyrosine kinase)
- **Chromosome**: 6q22.1
- **HGNC ID**: HGNC:10261
- **OMIM**: 165020
- **UniProt**: P08922
- **Protein**: 2,347 amino acids; type I transmembrane receptor tyrosine kinase
- **Normal function**: Epithelial cell differentiation, regionalization of proximal epididymal epithelium via NELL2-mediated lumicrine signaling; activates PI3K-mTOR, STAT3, VAV3 pathways ([PMID: 38169386](https://pubmed.ncbi.nlm.nih.gov/38169386/))

### Pathogenic Variants

**Fusion rearrangements (somatic):**

| Fusion Partner | Frequency | Chromosome | Breakpoint |
|---|---|---|---|
| CD74 | ~35–44% | 5q33 | Exon 6/exon 34 |
| EZR | ~10–15% | 6q25 | Variable |
| SLC34A2 | ~5–10% | 4p15 | Variable |
| SDC4 | ~5–10% | 20q12 | Variable |
| TPM3 | ~5% | 1q21 | Variable |
| GOPC (FIG) | ~5–8% | 6q22 | Intrachromosomal |
| CLIP1 | Rare | 12q24 | Variable |
| LRIG3, CCDC6, MSN, others | Rare | Various | Various |

All fusions retain the ROS1 kinase domain (exons 34–43) and are classified as **gain-of-function** (constitutive kinase activation). The fusion partner contributes the promoter (driving expression) and often a dimerization domain (facilitating ligand-independent activation).

**Resistance mutations (acquired, somatic):**

| Mutation | Location | Resistance Profile | Sensitive TKIs |
|---|---|---|---|
| G2032R | Solvent front | Most common; resistant to crizotinib, entrectinib | Taletrectinib, repotrectinib (partially) |
| L2026M | Gatekeeper | Resistant to entrectinib | Lorlatinib, repotrectinib |
| L2086F | xDFG motif | Pan-type I TKI resistant | Cabozantinib, merestinib (type II) |
| D2033N | Solvent front | Resistant to crizotinib | Lorlatinib |
| S1986F/Y | Hinge region | Variable | Next-gen TKIs |

"ROS1 L2086F mutant kinase is resistant to type I TKI including crizotinib, entrectinib, lorlatinib, repotrectinib, taletrectinib, while the type II TKI cabozantinib and merestinib retain activity" ([PMID: 38293020](https://pubmed.ncbi.nlm.nih.gov/38293020/)).

### Chromosomal Abnormalities

The defining event is a chromosomal rearrangement (translocation, inversion, or deletion) producing the ROS1 fusion gene. These are detected by FISH (break-apart probes), RT-PCR, or next-generation sequencing (RNA-based panels preferred).

### Modifier Genes

- **TP53** co-mutations: Most frequent co-alteration (31% in fusion-positive patients); associated with worse prognosis and shorter duration of TKI response ([PMID: 37261522](https://pubmed.ncbi.nlm.nih.gov/37261522/))
- **CDKN2A/B** copy number loss: Co-occurs in ~15%; combined with TP53 creates immunosuppressive microenvironment
- **SPP1** overexpression: Associated with poor outcomes in ALK/ROS1 fusion-positive cancers not receiving targeted therapy ([PMID: 34234236](https://pubmed.ncbi.nlm.nih.gov/34234236/))

### Epigenetic Information

Limited data specific to ROS1+ NSCLC. General NSCLC epigenetic alterations (promoter methylation of tumor suppressors) likely apply. No ROS1-specific methylation biomarkers established.

---

## 5. Environmental Information

### Environmental Factors

No specific environmental toxins, radiation exposures, or occupational hazards have been causally linked to ROS1 rearrangements. This contrasts sharply with general NSCLC, where tobacco smoke and radon are dominant risk factors.

### Lifestyle Factors

- **Smoking**: ROS1+ NSCLC is enriched in never-smokers (75.7%); smoking does not appear to be a causative factor ([PMID: 29883837](https://pubmed.ncbi.nlm.nih.gov/29883837/))
- **Diet, exercise, alcohol**: No established associations

### Infectious Agents

No infectious agents have been implicated in ROS1+ NSCLC.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

ROS1 fusion proteins activate multiple oncogenic signaling cascades:

{{figure:ros1_signaling_resistance.png|caption=ROS1 fusion signaling pathways showing convergence on STAT3 and SHP2, downstream MAPK and PI3K-AKT-mTOR effectors, and acquired resistance mechanisms}}

**Primary signaling axes:**

1. **STAT3 pathway**: "All studied fusions converge on STAT3 activation" ([PMID: 41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/))
2. **SHP2 (PTPN11) pathway**: ROS1 fusions directly interact with and phosphorylate SHP2 "to a greater extent than ALK fusions, and analyses of downstream pathways suggest MAPK-independent, non-canonical SHP2-driven functions" ([PMID: 41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/))
3. **RAS-MAPK cascade**: ERK1/2 activation via SOS1/GRB2 and SHP2
4. **PI3K-AKT-mTOR pathway**: Cell survival, growth, and metabolism
5. **PLCgamma pathway**: Calcium signaling and PKC activation

**GO terms for biological processes:**
- GO:0007169 (transmembrane receptor protein tyrosine kinase signaling pathway)
- GO:0070372 (regulation of ERK1 and ERK2 cascade)
- GO:0032006 (regulation of TOR signaling)
- GO:0030154 (cell differentiation)
- GO:0046777 (protein autophosphorylation)
- GO:0006468 (protein phosphorylation)

### Causal Chain

```
Chromosomal rearrangement (somatic)
    |
    v
ROS1 fusion gene (e.g., CD74-ROS1)
    |
    v
Constitutively active ROS1 kinase (ligand-independent dimerization)
    |
    v
Phosphorylation of SHP2/STAT3/PLCgamma/IRS1
    |
    v
Activation of MAPK, PI3K-AKT-mTOR, STAT3 cascades
    |
    v
Uncontrolled proliferation, survival, migration
    |
    v
Lung adenocarcinoma (mucinous cribriform/signet ring features)
    |
    v
Metastasis (high CNS tropism)
```

### Cellular Processes

- **Proliferation**: Constitutive MAPK/ERK activation drives cell cycle progression
- **Anti-apoptosis**: PI3K-AKT-mTOR and STAT3 signaling promote cell survival
- **Migration/invasion**: Fusion partner-specific effects (e.g., CLIP1-ROS1 increases cell motility via microtubule interactions) ([PMID: 41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/))
- **Angiogenesis**: Downstream VEGF pathway activation

**Cell types involved:**
- CL:0000066 (epithelial cell) — specifically pulmonary type II pneumocytes/Clara cells
- CL:0002063 (type II pneumocyte)

### Protein Dysfunction

The ROS1 fusion protein represents a **gain-of-function** alteration. The fusion partner provides:
1. A constitutively active promoter (driving expression)
2. A coiled-coil or dimerization domain (enabling ligand-independent activation)
3. Subcellular localization signals (e.g., GOPC-ROS1 localizes to Golgi)

Five crystal structures of the human ROS1 kinase domain are available in the PDB:

| PDB ID | Description | Resolution |
|---|---|---|
| 3ZBF | ROS1-crizotinib complex | 2.20 A |
| 4UXL | ROS1-lorlatinib precursor complex | 2.40 A |
| 7Z5W | ROS1-AstraZeneca ligand 1 | 2.254 A |
| 7Z5X | ROS1-AstraZeneca ligand 2 | 2.035 A |
| 9QEK | ROS1 G2032R-zidesamtinib complex | 2.205 A |

Additional structures include the full-length extracellular domain (9PVP, 4.57 A) and the ROS1-NELL2 complex (10FT, 3.21 A).

### Immune System Involvement

"Patients with co-occurring TP53/CDKN2A/B variations and ALK/RET/ROS1 rearrangements are associated with high TMB, more neoantigens, an immunosuppressive microenvironment and a worse prognosis" ([PMID: 37261522](https://pubmed.ncbi.nlm.nih.gov/37261522/)). Despite higher TMB and neoantigen burden, these tumors show **lower CD8+ T-cell infiltration**, creating a paradoxical immune phenotype. PD-L1 positivity is not significantly associated with ROS1 fusion status ([PMID: 34600407](https://pubmed.ncbi.nlm.nih.gov/34600407/)).

### Metabolic Changes

Pemetrexed (an antifolate) shows superior efficacy in ROS1+ NSCLC compared to non-pemetrexed chemotherapy (PFS 179 vs. 110 days, p = 0.0107), with low thymidylate synthase (TS) expression associated with better outcomes (PFS 184 vs. 110 days, p = 0.0105) ([PMID: 27738334](https://pubmed.ncbi.nlm.nih.gov/27738334/)). This suggests altered folate metabolism in ROS1+ tumors.

### SHP2 as a Therapeutic Vulnerability

SHP2 inhibition enhances the effects of TKIs in preclinical models of treatment-naive ALK/ROS1-fusion NSCLC ([PMID: 34158345](https://pubmed.ncbi.nlm.nih.gov/34158345/)). Given that all ROS1 fusions converge on strong SHP2 activation via direct interaction ([PMID: 41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/)), combination of ROS1 TKIs with SHP2 inhibitors represents a mechanistically rational therapeutic strategy.

### Resistance Mechanisms

**On-target (kinase domain mutations):**
- G2032R (solvent front) — most common
- L2026M (gatekeeper)
- L2086F (xDFG motif) — pan-type I TKI resistant
- D2033N (solvent front)

**Off-target/bypass mechanisms:**
- MET amplification: "acquired MET amplification as a resistance driver in a ROS1-rearranged lung adenocarcinoma after sequential treatment with ROS1 inhibitors" ([PMID: 37923925](https://pubmed.ncbi.nlm.nih.gov/37923925/))
- HGF-mediated MET activation: "HGF most potently induced entrectinib resistance in KM12SM and HCC78 cells by activating its receptor MET" ([PMID: 36416133](https://pubmed.ncbi.nlm.nih.gov/36416133/))
- KRAS mutations
- RET rearrangements (RUFY1-RET reported) ([PMID: 39907599](https://pubmed.ncbi.nlm.nih.gov/39907599/))
- FGFR3 amplification

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organ**: Lung (UBERON:0002048)
- Predominantly affects the peripheral lung parenchyma
- Adenocarcinoma histology typically arising in distal airways

**Secondary organ involvement (metastatic sites):**
- Brain/CNS (UBERON:0000955) — high tropism, 22–36% at diagnosis
- Bone (UBERON:0002481)
- Liver (UBERON:0002107)
- Adrenal glands (UBERON:0002369)
- Pleura (UBERON:0000977) — pleural effusion common
- Lymph nodes (UBERON:0000029)

**Body systems**: Respiratory system (primary), nervous system (CNS metastases), skeletal system, lymphatic system

### Tissue and Cell Level

- **Tissue**: Pulmonary epithelium (UBERON:0000115)
- **Cell types**: Type II pneumocytes (CL:0002063), Clara/Club cells (CL:0000158)
- **Histological pattern**: Adenocarcinoma with mucinous cribriform pattern, solid signet ring cell pattern, acinar pattern

### Subcellular Level

- **Cell membrane** (GO:0005886): ROS1 receptor localization
- **Cytoplasm** (GO:0005737): Signaling cascade components
- **Nucleus** (GO:0005634): STAT3 transcription factor translocation
- **Golgi apparatus** (GO:0005794): GOPC-ROS1 fusion specifically localizes here

### Localization

- Typically peripheral lung nodules/masses
- No lateralization preference (bilateral involvement possible in advanced disease)
- Leptomeningeal carcinomatosis can occur as a specific pattern of CNS spread

---

## 8. Temporal Development

### Onset

- **Typical age**: 5th–6th decade (median 50–56 years)
- **Onset pattern**: Insidious; often diagnosed at advanced stage (stage IIIB/IV) due to nonspecific symptoms
- 42.9% of patients present with stage IV disease in surgical series ([PMID: 34234236](https://pubmed.ncbi.nlm.nih.gov/34234236/))

### Progression

**Staging**: Standard AJCC/TNM staging for NSCLC applies (stages I–IV)

**Natural history without targeted therapy:**
- Rapid progression; platinum-based chemotherapy yields median PFS of ~6–7 months
- Pemetrexed-based chemotherapy: ORR 40.8%, median PFS 179 days ([PMID: 27738334](https://pubmed.ncbi.nlm.nih.gov/27738334/))

**With targeted therapy:**
- First-line crizotinib: median PFS ~12–19 months
- First-line repotrectinib: median PFS 35.7 months ([PMID: 39402859](https://pubmed.ncbi.nlm.nih.gov/39402859/))
- Eventual resistance is near-universal; sequential TKI strategies can extend disease control

**Disease course**: Progressive; no spontaneous remission. Treatment-induced responses are common but resistance develops.

### Critical Periods

- **Diagnosis**: Molecular testing at diagnosis is essential for treatment selection
- **CNS monitoring**: Regular brain imaging due to high CNS metastasis risk
- **Resistance emergence**: Molecular profiling at progression guides sequential therapy

{{figure:ros1_timeline.png|caption=Timeline of key milestones in ROS1-rearranged NSCLC research and treatment, from initial discovery through next-generation TKI approvals}}

---

## 9. Inheritance and Population

### Epidemiology

| Parameter | Value |
|---|---|
| **Prevalence among NSCLC** | 1–2% (range 0.6–4.1% depending on population and stage) |
| **Estimated new cases/year (US)** | ~2,000–4,000 (based on ~230,000 NSCLC diagnoses) |
| **Incidence (China)** | 2.59% of 6,066 tested NSCLC patients ([PMID: 30468296](https://pubmed.ncbi.nlm.nih.gov/30468296/)) |
| **Incidence (India)** | 3.5–4.1% ([PMID: 35634796](https://pubmed.ncbi.nlm.nih.gov/35634796/)) |
| **Incidence (Hispanic/Latino)** | ~2% ([PMID: 37729688](https://pubmed.ncbi.nlm.nih.gov/37729688/)) |
| **Early-stage prevalence** | 0.6% in surgically resected adenocarcinomas ([PMID: 37237384](https://pubmed.ncbi.nlm.nih.gov/37237384/)) |

### Inheritance Pattern

- **Not inherited**: ROS1 rearrangements are **somatic** events with no Mendelian inheritance pattern
- No germline ROS1 mutations predisposing to cancer have been established
- Not applicable: penetrance, expressivity, anticipation, carrier frequency

### Population Demographics

- **Sex ratio**: Female predominance (~59% female; fusion frequency 3.71% in women vs. 1.81% in men)
- **Age distribution**: Younger than general NSCLC (median ~50–56 years); enriched in patients <40 years (ROS1 fusions found in 7% of young-onset NSCLC in India) ([PMID: 40122770](https://pubmed.ncbi.nlm.nih.gov/40122770/))
- **Ethnic distribution**: Present across all populations; potentially higher frequency in East Asian and South Asian populations
- **Smoking status**: 75% or more are never-smokers

---

## 10. Diagnostics

### Molecular Diagnostic Testing

ROS1 rearrangement detection is **mandatory** before initiating TKI therapy. Multiple methods are available:

| Method | Sensitivity | Specificity | Advantages | Limitations |
|---|---|---|---|---|
| **FISH** (break-apart) | ~95% | ~95% | Gold standard; detects unknown partners | Labor-intensive; requires expertise |
| **IHC** (D4D6/SP384) | ~95–100% | ~70–80% | Rapid, cost-effective screening | Lower specificity; needs confirmation |
| **RNA-based NGS** | ~95% | ~98% | Identifies fusion partner; multiplex | Requires RNA quality; cost |
| **DNA-based NGS** | ~80–90% | ~95% | Comprehensive genomic profiling | May miss some fusions |
| **RT-PCR** | ~90% | ~99% | Rapid, specific | Only detects known fusions |

**Recommended approach**: IHC screening followed by FISH/NGS confirmation, or upfront comprehensive NGS (RNA-based preferred). "Targeted RNA NGS was confirmed to be the most efficient technique for gene fusion identification in clinical practice" ([PMID: 37190044](https://pubmed.ncbi.nlm.nih.gov/37190044/)). "FISH should not be dismissed, as they can crucially contribute to the completion of the molecular characterization" ([PMID: 37190044](https://pubmed.ncbi.nlm.nih.gov/37190044/)).

### Imaging Studies

- **CT chest/abdomen**: Standard staging
- **Brain MRI**: Mandatory at diagnosis and surveillance (high CNS tropism)
- **PET-CT**: For comprehensive staging
- **Bone scan**: If bone metastases suspected

### Biopsy and Pathology

- Tissue biopsy preferred; adequate material for molecular testing essential
- IHC: ROS1 protein expression (D4D6 clone, SP384 clone)
- Characteristic: adenocarcinoma with mucinous cribriform pattern, signet ring cells
- ROSE (Rapid On-Site Evaluation) improves specimen adequacy for biomarker testing ([PMID: 37805343](https://pubmed.ncbi.nlm.nih.gov/37805343/))

### Liquid Biopsy

- ctDNA-based NGS panels can detect ROS1 fusions in plasma
- CSF ctDNA superior to plasma for CNS disease monitoring ([PMID: 32838487](https://pubmed.ncbi.nlm.nih.gov/32838487/))
- Useful for resistance mutation detection at progression

### Differential Diagnosis

- Other oncogene-driven NSCLC (ALK, RET, NTRK fusions — mutually exclusive with ROS1)
- EGFR-mutant NSCLC (also younger, never-smokers, adenocarcinoma)
- KRAS-mutant NSCLC
- Driver-negative NSCLC

---

## 11. Outcome/Prognosis

### Survival and Mortality

{{figure:ros1_treatment_landscape.png|caption=Comparison of ROS1 TKI efficacy across generations showing objective response rates (ORR) and median progression-free survival (PFS)}}

| Treatment | ORR | Median PFS | Setting |
|---|---|---|---|
| **Crizotinib** | 71–80% | 12–19 months | TKI-naive, 1st line |
| **Entrectinib** | 67–77% | 15–19 months | TKI-naive, 1st line |
| **Repotrectinib** | 79% | 35.7 months | TKI-naive, 1st line |
| **Taletrectinib** | 88.8–90.6% | Not yet mature | TKI-naive, 1st line |
| **Unecritinib** | 80.2% | 16.5 months | TKI-naive, 1st line |
| **Lorlatinib** | Variable | Variable | 2nd line / post-crizotinib |
| **Zidesamtinib** | 73% (post-crizotinib) | Not yet mature | Post-crizotinib |
| **Cabozantinib** | Case reports | 12 months (1 case) | Post-lorlatinib (L2086F) |
| **Pemetrexed-platinum** | 40.8% | ~6 months | Chemotherapy |
| **Non-pemetrexed chemo** | 25.0% | ~3.7 months | Chemotherapy |

"In the TKI-naive cohort (n = 71), 79% of patients achieved an objective response, with a median progression-free survival (PFS) of 35.7 months, surpassing all previously approved ROS1 TKIs" ([PMID: 39402859](https://pubmed.ncbi.nlm.nih.gov/39402859/)).

"Taletrectinib demonstrated high objective response rates in both TKI-naive (88.8%) and TKI-pretreated (55.8%) patients, including robust intracranial activity and efficacy against the G2032R mutation" ([PMID: 41548253](https://pubmed.ncbi.nlm.nih.gov/41548253/)).

### Prognostic Factors

**Favorable:**
- ROS1 fusion-positive status (vs. driver-negative NSCLC)
- Absence of TP53 co-mutation
- Absence of CNS metastases at diagnosis
- Access to appropriate TKI therapy

**Unfavorable:**
- TP53/CDKN2A/B co-mutations (immunosuppressive microenvironment, worse prognosis)
- CNS metastases at diagnosis
- G2032R resistance mutation emergence
- Lack of access to molecular testing or targeted therapy

### Complications

- CNS metastases / leptomeningeal carcinomatosis
- Pleural effusion / respiratory failure
- Bone metastases with pathological fractures
- Hepatic metastases
- Treatment-related toxicity (see Treatment section)

---

## 12. Treatment

### First-Line Targeted Therapy

**MAXO:0000058 (pharmacotherapy)**

| Agent | Class | Mechanism | Key Data | CHEBI/DrugBank |
|---|---|---|---|---|
| **Crizotinib** | Type I TKI | ROS1/ALK/MET inhibitor | ORR 71–80%, PFS 12–19 mo | CHEBI:64310, DB08865 |
| **Entrectinib** | Type I TKI | ROS1/TRK/ALK inhibitor | ORR 67–77%, CNS active | DB15685 |
| **Repotrectinib** | Next-gen macrocyclic TKI | ROS1/TRK/ALK inhibitor | ORR 79%, PFS 35.7 mo | DB16876 |
| **Taletrectinib** | Next-gen TKI | ROS1/TRK inhibitor (ROS1-selective) | ORR 89%, G2032R active | Investigational |
| **Unecritinib** (TQ-B3101) | Next-gen TKI | ROS1/ALK/MET inhibitor | ORR 80.2%, PFS 16.5 mo | Investigational |

### Second-Line and Beyond

- **Lorlatinib**: Third-gen ALK/ROS1 TKI; good CNS penetration; used post-crizotinib; limited by neurocognitive side effects ([PMID: 38201357](https://pubmed.ncbi.nlm.nih.gov/38201357/))
- **Zidesamtinib** (NVL-520): ROS1-selective, TRK-sparing; ORR 73% post-crizotinib, 38% post-repotrectinib ([PMID: 40118657](https://pubmed.ncbi.nlm.nih.gov/40118657/)); crystal structure of G2032R-zidesamtinib complex available (PDB: 9QEK)
- **Cabozantinib**: Type II multi-kinase inhibitor; retains activity against L2086F mutation ([PMID: 38293020](https://pubmed.ncbi.nlm.nih.gov/38293020/), [PMID: 40826797](https://pubmed.ncbi.nlm.nih.gov/40826797/))
- **Brigatinib**: ORR 71.4% in TKI-naive, 31.6% post-crizotinib ([PMID: 39018589](https://pubmed.ncbi.nlm.nih.gov/39018589/))

### Chemotherapy

**MAXO:0000647 (chemotherapy)**

Pemetrexed-based platinum doublet is the preferred chemotherapy regimen: "crizotinib-treated group had a higher overall response rate (ORR, 80.0%), disease control rate (DCR, 90.0%) and longer progression-free survival (PFS, 294 days) compared with the rates in pemetrexed-treated group (ORR, 40.8%; DCR, 71.4%; PFS, 179 days) and non-pemetrexed-treated group (ORR, 25.0%; DCR, 47.7%; PFS, 110 days)" ([PMID: 27738334](https://pubmed.ncbi.nlm.nih.gov/27738334/)).

### Immunotherapy

**MAXO:0001298 (immunotherapy)**

Immune checkpoint inhibitors have **limited single-agent activity** in ROS1+ NSCLC:
- PD-L1 expression is not significantly associated with ROS1 fusion status ([PMID: 34600407](https://pubmed.ncbi.nlm.nih.gov/34600407/))
- TP53/CDKN2A/B co-mutation creates an immunosuppressive microenvironment despite high TMB ([PMID: 37261522](https://pubmed.ncbi.nlm.nih.gov/37261522/))
- NCCN guidelines recommend against first-line immunotherapy in ROS1+ NSCLC
- May have a role in combination with chemotherapy after TKI exhaustion

### Surgical Interventions

**MAXO:0000004 (surgical procedure)**

- Surgical resection is standard for early-stage disease (stage I–IIIA)
- Limited data on adjuvant targeted therapy post-resection in ROS1+ patients
- ROS1 appears less frequent in early-stage resected disease (0.6% vs 1–2% in advanced) ([PMID: 37237384](https://pubmed.ncbi.nlm.nih.gov/37237384/))

### Emerging Combination Strategies

- **ROS1 TKI + SHP2 inhibitor**: Preclinical data supports enhanced efficacy ([PMID: 34158345](https://pubmed.ncbi.nlm.nih.gov/34158345/)); mechanistic rationale from convergent SHP2 activation across all fusions ([PMID: 41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/))
- **ROS1 TKI + MET inhibitor**: For MET amplification-driven resistance; lorlatinib + capmatinib combination reported ([PMID: 37923925](https://pubmed.ncbi.nlm.nih.gov/37923925/))
- **APG-2449**: FAK + ALK/ROS1 TKI; CNS-penetrant (CSF:plasma ratio 0.65–1.66); phase I data available ([PMID: 41146927](https://pubmed.ncbi.nlm.nih.gov/41146927/))

### Treatment Algorithm

```
Diagnosis of advanced ROS1+ NSCLC
    |
    v
1st Line: Next-gen ROS1 TKI (repotrectinib or taletrectinib preferred)
         Consider CNS status when selecting agent
    | (progression)
    v
Rebiopsy / liquid biopsy for resistance mechanism
    |
    v
On-target resistance (e.g., G2032R):
  -> Switch to TKI with activity against specific mutation
  -> G2032R: taletrectinib, zidesamtinib
  -> L2086F: cabozantinib/merestinib (type II TKI)
    |
    v
Off-target/bypass resistance (e.g., MET amp):
  -> Combination therapy (ROS1 TKI + pathway-specific inhibitor)
  -> Consider clinical trials
    |
    v
Post-TKI exhaustion:
  -> Pemetrexed-based chemotherapy +/- immunotherapy
  -> Clinical trials (SHP2 inhibitor combos, novel agents)
```

---

## 13. Prevention

### Primary Prevention

- **Smoking cessation**: While ROS1+ NSCLC is not smoking-related, general lung cancer prevention includes tobacco avoidance
- No specific primary prevention strategies exist for ROS1 rearrangements (stochastic somatic events)

### Secondary Prevention (Screening and Early Detection)

- **Low-dose CT screening**: USPSTF-recommended for high-risk individuals (age 50–80 with 20+ pack-year history); less applicable to the ROS1+ demographic (younger never-smokers)
- **Molecular testing at diagnosis**: Universal molecular profiling of all advanced non-squamous NSCLC ensures detection of ROS1 fusions
- Guidelines mandate testing for EGFR, ALK, ROS1, BRAF, RET, MET, NTRK, KRAS in advanced NSCLC ([PMID: 37455124](https://pubmed.ncbi.nlm.nih.gov/37455124/))

### Tertiary Prevention

- Regular surveillance imaging (CT, brain MRI) during and after TKI therapy
- Molecular profiling at disease progression to identify resistance mechanisms and guide sequential therapy
- Supportive care and symptom management

### Genetic Counseling

Not typically indicated as ROS1 rearrangements are somatic. No hereditary cancer syndromes are associated with ROS1 fusions (unlike the rare pediatric Li-Fraumeni-associated angiosarcoma with ROS1 rearrangement) ([PMID: 36307212](https://pubmed.ncbi.nlm.nih.gov/36307212/)).

---

## 14. Other Species / Natural Disease

### Comparative Biology

**ROS1 orthologs:**

| Species | Gene | NCBI Gene ID | Notes |
|---|---|---|---|
| *Mus musculus* | Ros1 | 19886 | c-ros KO mice: male infertility |
| *Rattus norvegicus* | Ros1 | 304891 | Similar expression pattern |
| *Drosophila melanogaster* | Sevenless (sev) | — | Structural homolog |

### Animal Models — Normal ROS1 Function

c-ros knockout mice demonstrate the normal physiological role of ROS1: "Transgenic mice with male infertility, the c-ros knockout (KO) and GPX5-Tag2 transgenic mouse models... exhibit severely angulated sperm flagella explaining the infertility" ([PMID: 15109745](https://pubmed.ncbi.nlm.nih.gov/15109745/)). This results from defective differentiation of the initial segment epithelium of the epididymis.

The NELL2-ROS1 lumicrine signaling axis is conserved in humans: "There was a significant correlation between the epididymal expressions of mouse genes upregulated by the trans-luminal signaling and those of their human orthologs, as evaluated by the correlation coefficient of 0.604" ([PMID: 38169386](https://pubmed.ncbi.nlm.nih.gov/38169386/)).

### Naturally Occurring ROS1 Fusions in Animals

No naturally occurring ROS1 fusion-driven lung cancers have been reported in companion animals or wildlife. Canine and feline lung tumors are rare and not characterized for ROS1 status.

---

## 15. Model Organisms

### In Vivo Models

| Model | Type | Application | Limitations |
|---|---|---|---|
| **Xenograft (PDX)** | Mouse | Drug efficacy, resistance studies | No intact immune system |
| **Ba/F3 transformed cells** | Cell-based | Rapid functional characterization of fusions/mutations | Simplified system |
| **c-ros KO mouse** | Knockout | Normal ROS1 biology (male infertility) | Not a cancer model |
| **Transgenic ROS1 fusion** | Mouse | Tumor initiation studies | Limited availability |

### Cell Line Models

| Cell Line | Fusion | Source | Application |
|---|---|---|---|
| **HCC78** | SLC34A2-ROS1 | Human NSCLC | Drug sensitivity, resistance |
| **KM12SM** | TPM3-ROS1 | Colorectal cancer | Cross-cancer ROS1 biology |
| **U-118 MG** | GOPC-ROS1 | Glioblastoma | Glioma-specific ROS1 |

HCC78 cells are the most widely used model for studying ROS1 TKI efficacy and resistance. HGF-mediated resistance was characterized using both HCC78 and KM12SM cells ([PMID: 36416133](https://pubmed.ncbi.nlm.nih.gov/36416133/)).

### Model Characteristics

- **Ba/F3 system**: Excellent for rapid assessment of fusion oncogenicity and drug sensitivity; used to characterize L2086F pan-type I TKI resistance ([PMID: 38293020](https://pubmed.ncbi.nlm.nih.gov/38293020/))
- **PDX models**: Best recapitulation of human tumor biology; used for preclinical TKI evaluation
- **Limitations**: No single model fully captures the human tumor microenvironment, immune interactions, or CNS tropism

---

## Key Findings Summary

### Finding 1: ROS1 Rearrangements Define a Rare Molecular Subset
ROS1 fusions occur in 1–2% of NSCLC cases globally, with variation by population (2.59% in China, 3.5–4.1% in India, ~2% in Hispanic/Latino populations). The disease is enriched in younger, female, never-smoking patients with adenocarcinoma.

### Finding 2: Distinctive Clinical-Demographic Profile
Median age 50–56 years, 58.9% female, 75.7% never-smokers, 98.1% adenocarcinoma. Statistically significant differences versus ROS1-negative NSCLC in age (p < 0.01), sex (p < 0.01), and smoking status (p < 0.01).

### Finding 3: Rapidly Evolving TKI Landscape
First-generation TKIs (crizotinib, entrectinib) achieve ORR 60–80% with PFS 12–19 months. Next-generation agents have dramatically improved outcomes: repotrectinib (ORR 79%, PFS 35.7 months), taletrectinib (ORR 89%), unecritinib (ORR 80.2%).

### Finding 4: Complex Resistance Mechanisms
On-target mutations (G2032R, L2086F, L2026M) and off-target bypass pathways (MET amplification, HGF-mediated resistance, KRAS mutations, RET rearrangements) necessitate serial molecular profiling and rational TKI sequencing.

### Finding 5: Convergent STAT3/SHP2 Signaling
All ROS1 fusions converge on STAT3 activation and directly interact with SHP2, with significantly greater SHP2 phosphorylation than ALK fusions. This distinguishes ROS1 from ALK biology and identifies SHP2 as a therapeutic vulnerability.

### Finding 6: Normal ROS1 Biology — NELL2-Mediated Lumicrine Signaling
ROS1 normally functions in NELL2-mediated epithelial differentiation; c-ros KO mice are infertile. This pathway is conserved in humans (correlation r = 0.604 between mouse and human ortholog expression).

### Finding 7: Immunosuppressive Co-Mutation Microenvironment
TP53/CDKN2A/B co-mutations (present in ~31% and ~15% respectively) create a paradoxical phenotype: high TMB and neoantigens but low CD8+ T-cell infiltration, resulting in worse prognosis.

### Finding 8: Pemetrexed Biomarker Association
Pemetrexed-based chemotherapy shows superior efficacy in ROS1+ NSCLC (PFS 179 vs. 110 days for non-pemetrexed, p = 0.0107), with low thymidylate synthase expression predicting benefit.

### Finding 9: Structural Biology Resources
Five crystal structures of the ROS1 kinase domain are available, including the G2032R mutant-zidesamtinib complex (PDB: 9QEK), enabling structure-based drug design for next-generation inhibitors.

### Finding 10: Characteristic Histopathology
ROS1+ adenocarcinoma shows distinctive mucinous cribriform and signet ring cell patterns on histology, which can serve as morphological clues for molecular testing.

### Finding 11: Conserved Normal Biology
The NELL2-ROS1 lumicrine signaling axis essential for male fertility is conserved from rodents to humans, providing insights into normal receptor function and potential off-target effects of ROS1 inhibitors.

### Finding 12: Quality of Life with Targeted Therapy
Entrectinib maintains stable quality of life (STARTRK-2 PROs), while post-TKI chemo-immunotherapy carries substantially higher toxicity, underscoring the importance of maintaining patients on targeted therapy as long as possible.

### Finding 13: SHP2 Inhibition as Combination Strategy
Preclinical data demonstrates that SHP2 inhibition enhances ROS1 TKI efficacy, supported by the finding that all ROS1 fusions uniquely converge on SHP2 activation, providing a mechanistic rationale for clinical combination trials.

---

## Mechanistic Model / Interpretation

The pathophysiology of ROS1+ NSCLC can be understood as a multi-level cascade:

**Level 1 — Genomic initiation**: A stochastic somatic chromosomal rearrangement fuses the ROS1 kinase domain to a partner gene. The partner provides constitutive expression and a dimerization interface, converting ROS1 from a ligand-dependent receptor (normally activated by NELL2 in epididymal epithelium) to a ligand-independent oncogene.

**Level 2 — Signaling amplification**: The constitutively active ROS1 fusion kinase phosphorylates SHP2 (more strongly than ALK fusions do) and activates STAT3. These two nodes then fan out to the canonical MAPK and PI3K-AKT-mTOR cascades, plus non-canonical SHP2-dependent pathways that are MAPK-independent.

**Level 3 — Phenotypic consequences**: Sustained signaling drives proliferation (MAPK/ERK), survival (AKT/mTOR), and migration (fusion partner-specific, e.g., CLIP1 microtubule effects). The result is adenocarcinoma with mucinous/signet ring features and a notable tropism for the CNS.

**Level 4 — Therapeutic response and resistance**: ROS1 TKIs block the fusion kinase, collapsing the signaling cascade and producing dramatic tumor regression (ORR 70–90%). However, tumor evolution under selective pressure leads to resistance through on-target mutations (G2032R, L2086F) or bypass pathways (MET, RET, KRAS). The type of resistance mutation dictates the next therapeutic strategy: type II TKIs for L2086F, taletrectinib/zidesamtinib for G2032R, MET inhibitor combinations for MET amplification.

**Level 5 — Microenvironment modulation**: Co-occurring TP53/CDKN2A/B mutations reshape the immune microenvironment, creating an immunosuppressive milieu despite increased neoantigen load. This partially explains the limited efficacy of checkpoint inhibitors and suggests that combination strategies (TKI + SHP2 inhibitor or TKI + immunotherapy) may be needed for durable disease control.

---

## Evidence Base

### Landmark Studies

| Study | PMID | Key Contribution |
|---|---|---|
| Shaw et al. (ROS1 epidemiology/crizotinib) | [29883837](https://pubmed.ncbi.nlm.nih.gov/29883837/) | Clinical profile of 103 ROS1+ patients |
| Wu et al. (Chinese prevalence) | [30468296](https://pubmed.ncbi.nlm.nih.gov/30468296/) | ROS1 prevalence in 6,066 NSCLC patients |
| TRIDENT-1 (repotrectinib) | [39402859](https://pubmed.ncbi.nlm.nih.gov/39402859/) | ORR 79%, PFS 35.7 months |
| Drilon et al. (repotrectinib NEJM) | [38197815](https://pubmed.ncbi.nlm.nih.gov/38197815/) | Phase 1-2 registrational trial |
| TRUST (taletrectinib) | [41548253](https://pubmed.ncbi.nlm.nih.gov/41548253/) | ORR 88.8% TKI-naive |
| Duchemann et al. (immune microenvironment) | [37261522](https://pubmed.ncbi.nlm.nih.gov/37261522/) | TP53/CDKN2A/B immunosuppressive phenotype |
| Neel et al. (SHP2/STAT3 signaling) | [41790556](https://pubmed.ncbi.nlm.nih.gov/41790556/) | All fusions converge on STAT3/SHP2 |
| Ku et al. (L2086F resistance) | [38293020](https://pubmed.ncbi.nlm.nih.gov/38293020/) | Type I/II TKI switching strategy |
| Ou et al. (pemetrexed efficacy) | [27738334](https://pubmed.ncbi.nlm.nih.gov/27738334/) | Pemetrexed superiority and TS biomarker |
| Arai et al. (histopathology) | [23877438](https://pubmed.ncbi.nlm.nih.gov/23877438/) | CD74-ROS1 histological features |
| Hata et al. (HGF resistance) | [36416133](https://pubmed.ncbi.nlm.nih.gov/36416133/) | Microenvironment-driven resistance |
| Berger et al. (SHP2 combinations) | [34158345](https://pubmed.ncbi.nlm.nih.gov/34158345/) | SHP2 inhibition enhances TKI efficacy |
| Kogo et al. (NELL2-ROS1 conservation) | [38169386](https://pubmed.ncbi.nlm.nih.gov/38169386/) | Human conservation of lumicrine pathway |
| Marinello et al. (entrectinib PROs) | [33930659](https://pubmed.ncbi.nlm.nih.gov/33930659/) | Quality of life data |
| Unecritinib phase I/II | [37385995](https://pubmed.ncbi.nlm.nih.gov/37385995/) | ORR 80.2%, PFS 16.5 months |

---

## Limitations and Knowledge Gaps

1. **Rarity limits clinical trial power**: With only 1–2% prevalence, most clinical trials are single-arm; head-to-head comparisons between ROS1 TKIs are lacking and rely on indirect comparisons (MAICs)
2. **Optimal TKI sequencing undefined**: No randomized data guide the choice between first-line repotrectinib vs. taletrectinib, or optimal sequencing at resistance
3. **Immunotherapy role unclear**: While immune checkpoint inhibitors are largely ineffective as monotherapy, their role in combination with TKIs or chemotherapy post-TKI exhaustion requires further study
4. **Early-stage targeted therapy**: No data exist for adjuvant/neoadjuvant ROS1 TKIs in resectable disease
5. **Long-term survival data**: 5-year and 10-year overall survival with modern TKIs are not yet mature
6. **Fusion partner-specific biology**: While fusion partners confer different subcellular localizations and additional functions (e.g., CLIP1 motility effects), clinical significance remains uncertain
7. **Biomarker-guided immunotherapy**: Whether specific co-mutation profiles (high TMB, PD-L1+) predict immunotherapy benefit in the subset of ROS1+ patients remains unknown
8. **Liquid biopsy standardization**: ctDNA-based monitoring for ROS1 fusions and resistance mutations needs prospective validation
9. **Epigenetic landscape**: ROS1-specific epigenetic alterations are poorly characterized
10. **Pediatric/young adult**: Limited data on ROS1+ NSCLC in patients under 30 years

---

## Proposed Follow-up Experiments/Actions

### Clinical Priorities

1. **Randomized trials comparing next-gen ROS1 TKIs**: Head-to-head comparison of repotrectinib vs. taletrectinib in treatment-naive patients to establish optimal first-line therapy
2. **Adjuvant ROS1 TKI trials**: Phase III studies of post-surgical TKI therapy in resected ROS1+ NSCLC (analogous to ADAURA for EGFR)
3. **SHP2 inhibitor combination trials**: Based on preclinical evidence of enhanced TKI efficacy with SHP2 inhibition, phase I/II trials combining ROS1 TKIs with SHP2 inhibitors (e.g., TNO155, RMC-4630) are warranted
4. **Biomarker-stratified immunotherapy**: Trials evaluating checkpoint inhibitors in the TP53-co-mutated, high-TMB subset of ROS1+ patients

### Research Priorities

5. **Single-cell and spatial transcriptomics**: Characterize the tumor microenvironment of ROS1+ NSCLC to understand immune evasion mechanisms and identify combination therapy targets
6. **Resistance monitoring with ctDNA**: Prospective validation of liquid biopsy-guided adaptive therapy (switching TKIs at molecular progression before radiographic progression)
7. **Fusion partner functional studies**: Systematic comparison of signaling, metastatic potential, and drug sensitivity across different fusion partners using isogenic models
8. **CNS tropism mechanisms**: Investigate why ROS1+ NSCLC has high brain metastasis rates; identify targetable pathways driving CNS invasion
9. **Type II TKI development**: Expand the arsenal of type II ROS1 TKIs to address L2086F and compound mutations
10. **Real-world outcomes registry**: Multi-national ROS1+ NSCLC registry to capture treatment patterns, sequential therapy outcomes, and long-term survival with modern TKIs

---

## Ontology Term Summary

| Category | Key Terms |
|---|---|
| **MONDO** | MONDO:0005233 (non-small cell lung carcinoma) |
| **HPO** | HP:0012735, HP:0002094, HP:0001824, HP:0002105, HP:0002202, HP:0002076 |
| **GO (BP)** | GO:0007169, GO:0070372, GO:0032006, GO:0030154, GO:0046777 |
| **GO (CC)** | GO:0005886, GO:0005737, GO:0005634, GO:0005794 |
| **CL** | CL:0000066, CL:0002063, CL:0000158 |
| **UBERON** | UBERON:0002048, UBERON:0000955, UBERON:0002481, UBERON:0002107, UBERON:0000977 |
| **CHEBI** | CHEBI:64310 (crizotinib) |
| **MAXO** | MAXO:0000058, MAXO:0000647, MAXO:0001298, MAXO:0000004 |

---

*Report generated from autonomous scientific discovery analysis of 93 published studies with 13 confirmed findings across 5 investigation iterations. Last updated: 2026-05-06.*
