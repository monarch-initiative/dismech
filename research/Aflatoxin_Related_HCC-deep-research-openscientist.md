---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T02:23:26.793002'
end_time: '2026-05-05T02:43:23.016493'
duration_seconds: 1196.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aflatoxin-Related Hepatocellular Carcinoma
  mondo_id: ''
  category: ''
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
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aflatoxin-Related Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Aflatoxin-Related Hepatocellular Carcinoma** covering all of the
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

# Comprehensive Disease Characterization: Aflatoxin-Related Hepatocellular Carcinoma

---

## Summary

Aflatoxin-related hepatocellular carcinoma (HCC) is a primary malignant liver tumor arising from hepatocytes, causally linked to chronic dietary exposure to aflatoxin B1 (AFB1), a potent mycotoxin classified as an IARC Group 1 human carcinogen. AFB1 is produced by *Aspergillus flavus* and *Aspergillus parasiticus* fungi that contaminate staple crops in tropical and subtropical regions. The disease represents a paradigm of gene–environment interaction in carcinogenesis: AFB1 undergoes hepatic bioactivation by cytochrome P450 enzymes (primarily CYP1A2 at physiological concentrations, with CYP3A4 contributing at higher concentrations) to form AFB1-exo-8,9-epoxide, which covalently binds DNA and induces the hallmark TP53 R249S mutation—a G→T transversion at codon 249 that accounts for approximately 90% of TP53 mutations in AFB1-related HCC. This somatic mutation simultaneously eliminates tumor-suppressive function and confers gain-of-function oncogenic activity through a CDK4-PIN1-c-Myc proliferative pathway. The global burden is substantial: an estimated 25,200–155,000 of the 550,000–600,000 annual HCC cases worldwide are attributable to aflatoxin exposure, concentrated in sub-Saharan Africa, Southeast Asia, and China.

Chronic hepatitis B virus (HBV) infection acts as the most critical synergistic co-factor, producing a more-than-multiplicative increase in HCC risk. This synergy is mediated in part through HBV-induced upregulation of YTHDF2, which suppresses PARP1 expression via m6A RNA modification, thereby exacerbating AFB1-induced DNA damage. Individual genetic susceptibility is further modulated by polymorphisms in detoxification enzymes—particularly GSTM1-null and GSTT1-null genotypes—and DNA repair genes (XRCC1), with combined risk genotypes conferring up to 15-fold increased HCC risk. Recent discoveries have revealed that AFB1 also promotes an immunosuppressive tumor microenvironment through IL-6/NF-κB-mediated M2 macrophage polarization, suppressing CD8+ T cell infiltration and potentially limiting checkpoint inhibitor efficacy.

Prevention strategies encompass HBV vaccination (the single most effective intervention), aflatoxin exposure reduction through improved post-harvest food storage, and chemoprevention with agents such as chlorophyllin and oltipraz validated in randomized clinical trials. Treatment follows standard HCC algorithms, with atezolizumab plus bevacizumab as the current first-line standard of care, though the AFB1-driven immunosuppressive microenvironment may require novel combination strategies such as anti-IL-6 plus anti-PD-1 therapy. Experimental approaches targeting the p53-R249S gain-of-function pathway through CDK4/6 inhibitor and p53-restoring compound combinations represent a promising precision medicine strategy for this molecularly defined HCC subtype.

---

## Key Findings

### Finding 1: TP53 R249S — The Molecular Hallmark of AFB1 Exposure

The TP53 R249S mutation (AGG→AGT, p.Arg249Ser) is the most specific molecular biomarker of AFB1 exposure in hepatocarcinogenesis, functioning as both a diagnostic indicator and a mechanistic driver of disease. This somatic missense mutation results from a G→T transversion caused by AFB1-DNA adducts at the third base of codon 249 in the TP53 tumor suppressor gene.

The mutation's predominance is striking: "a mutation at codon 249 (AGG to AGT, arginine to serine, p.R249S) accounts for 90% of TP53 mutations in AFB(1)-related HCC. This specificity suggests that p.R249S confers a selective advantage during hepatocarcinogenesis" ([PMID: 20538734](https://pubmed.ncbi.nlm.nih.gov/20538734/)). Its role as a population-level biomarker is firmly established: "Lifelong intoxication with aflatoxin B1 is considered as one of the primary causes of this situation. The role of aflatoxin in HCC from a given population is commonly estimated through the prevalence of R249S mutation of TP53, a hallmark for previous exposure to the mycotoxin" ([PMID: 29749584](https://pubmed.ncbi.nlm.nih.gov/29749584/)).

Geographic prevalence of the R249S mutation directly correlates with AFB1 exposure levels:

| Region | R249S Prevalence | Population | Reference |
|---|---|---|---|
| Middle Africa | 24.8% of HCC patients vs 5.6% controls (P=2.2E-07) | ddPCR of cell-free DNA | [PMID: 29749584](https://pubmed.ncbi.nlm.nih.gov/29749584/) |
| Mexico | 6% of HCC cases | 50 HCC tissue blocks | [PMID: 35438902](https://pubmed.ncbi.nlm.nih.gov/35438902/) |
| Romania | Present (individual cases) | 48 consecutive HCC cases | [PMID: 24736102](https://pubmed.ncbi.nlm.nih.gov/24736102/) |
| Egypt (Nile Delta) | 1% of HCC cases | 104 HCC cases | [PMID: 37774068](https://pubmed.ncbi.nlm.nih.gov/37774068/) |

Critically, R249S does not merely abolish p53 tumor suppressor function—it confers gain-of-function oncogenic activity. The mechanism involves: "CDK4 interacts with p53-RS in the G1/S phase of the cells, phosphorylates it, and enhances its nuclear localization. This is coupled with binding of a peptidyl-prolyl cis-trans isomerase NIMA-interacting 1 (PIN1) to p53-RS" ([PMID: 29225033](https://pubmed.ncbi.nlm.nih.gov/29225033/)). This CDK4-PIN1-p53R249S-c-Myc axis drives ribosomal biogenesis and cell proliferation, representing a therapeutically targetable pathway. A genome-wide association study further identified three SNPs (ADAMTS18 rs9930984, rs75218075, rs8022091) associated with R249S mutation susceptibility in HCC patients exposed to AFB1 and HBV ([PMID: 33457005](https://pubmed.ncbi.nlm.nih.gov/33457005/)).

### Finding 2: Synergistic HBV–AFB1 Interaction Multiplies HCC Risk

The interaction between chronic HBV infection and AFB1 exposure produces a more-than-multiplicative increase in HCC risk, representing one of the best-characterized gene–environment synergies in cancer epidemiology. "Prospective epidemiological studies have shown a more than multiplicative interaction between HBV and aflatoxins in terms of HCC risk" ([PMID: 19345001](https://pubmed.ncbi.nlm.nih.gov/19345001/)). The global burden is quantified in the landmark risk assessment: "Of the 550,000-600,000 new HCC cases worldwide each year, about 25,200-155,000 may be attributable to aflatoxin exposure. Most cases occur in sub-Saharan Africa, Southeast Asia, and China where populations suffer from both high HBV prevalence and largely uncontrolled aflatoxin exposure in food" ([PMID: 20172840](https://pubmed.ncbi.nlm.nih.gov/20172840/)).

At the molecular level, a recently discovered mechanism explains this synergy: "HBV infection increased YTHDF2 expression while suppressing PARP1 both in vitro and in vivo. Additionally, HBV infection exacerbated AFB1-induced DNA damage in both experimental settings" ([PMID: 40344782](https://pubmed.ncbi.nlm.nih.gov/40344782/)). Through N6-methyladenosine (m6A) RNA modification, HBV upregulates the m6A reader protein YTHDF2, which promotes degradation of PARP1 mRNA. Since PARP1 is a critical DNA repair enzyme (poly(ADP-ribose) polymerase), its suppression directly impairs the cell's ability to repair AFB1-induced DNA adducts, increasing mutation frequency and accelerating carcinogenesis. In GSTT1-null chronic HBsAg carriers, AFB1 exposure conferred an OR of 3.7 (95% CI 1.5–9.3) for HCC, with a statistically significant interaction (P = 0.03) ([PMID: 11470760](https://pubmed.ncbi.nlm.nih.gov/11470760/)).

### Finding 3: CYP450-Mediated Bioactivation Is the Initiating Event

The metabolic activation of AFB1 by hepatic cytochrome P450 enzymes is the critical initiating step in aflatoxin-induced carcinogenesis. CYP1A2 is the primary bioactivating enzyme at physiologically relevant AFB1 concentrations: "Treatment of individual human liver microsomes (HLM) with TAO resulted in an average 20% inhibition of AFB1-8,9-epoxide formation at 16 microM AFB1, whereas incubation of HLM with furafylline at 16 microM AFB1 resulted in an average 72% inhibition of AFB1-8,9-epoxide formation at 16 microM AFB1" ([PMID: 8261428](https://pubmed.ncbi.nlm.nih.gov/8261428/)). CYP3A4 becomes more significant at higher substrate concentrations (46% inhibition by TAO at 128 μM).

Individual susceptibility is critically modulated by phase II detoxification capacity. In The Gambia, "the GSTM1-null genotype [odds ratio (OR), 2.45; 95% confidence interval (95% CI), 1.21-4.95] and the heterozygote XRCC1-399 AG genotype (OR, 3.18; 95% CI, 1.35-7.51) were significantly associated with HCC" ([PMID: 15734960](https://pubmed.ncbi.nlm.nih.gov/15734960/)). A meta-analysis of 33 studies confirmed GSTM1-null (OR = 1.31, 95% CI 1.07–1.61) and GSTT1-null (OR = 1.47, 95% CI 1.25–1.74) as HCC risk factors ([PMID: 24399650](https://pubmed.ncbi.nlm.nih.gov/24399650/)). Most dramatically, "individuals featuring all of the putative risk genotypes [GSTM1-null, HYL1*2-YH/HH, and XRCC1-AG/GG]" experienced approximately 15-fold increased HCC risk (OR = 14.7) ([PMID: 16884947](https://pubmed.ncbi.nlm.nih.gov/16884947/)), demonstrating multiplicative gene–gene interactions in AFB1-related hepatocarcinogenesis.

### Finding 4: Chemoprevention Efficacy Validated in Clinical Trials

Randomized clinical trials conducted in Qidong, China—a high-risk area for both HBV and AFB1 exposure—established proof-of-principle for pharmaceutical chemoprevention of aflatoxin-related HCC. Two mechanistically distinct agents were tested: oltipraz, a dithiolethione that induces phase 2 detoxification enzymes (particularly glutathione S-transferases), and chlorophyllin, a water-soluble chlorophyll derivative that reduces AFB1 oral bioavailability by forming molecular complexes in the gastrointestinal tract.

"Both chemopreventive agents modulated levels of aflatoxin biomarkers in the study participants in manners consonant with protection. Although pharmacological approaches establish proof of principle and help identify key molecular targets for interventions, food-based approaches that also use these molecular targets may be the most practical for widespread application in high-risk populations" ([PMID: 15508099](https://pubmed.ncbi.nlm.nih.gov/15508099/)). These findings catalyzed development of practical dietary interventions including broccoli sprout beverages (sulforaphane, a potent Nrf2 activator) and green leafy vegetable supplementation as scalable alternatives for resource-limited settings.

Additionally, probiotic supplementation with *Lacticaseibacillus paracasei* strain Shirota showed a 23% reduction in urinary AFM1 concentrations in a randomized, double-blind, placebo-controlled trial among Malaysian adults ([PMID: 40250564](https://pubmed.ncbi.nlm.nih.gov/40250564/)), suggesting gut-based interventions as another avenue for reducing AFB1 absorption.

### Finding 5: AFB1-Driven Immunosuppressive Tumor Microenvironment

A recent and important discovery reveals that AFB1 actively shapes the tumor microenvironment to promote immune evasion. "We found that AFB1 indirectly influences M2-like macrophage polarization by upregulating IL-6 expression in tumor cells through the NF-κB signaling pathway" ([PMID: 40789982](https://pubmed.ncbi.nlm.nih.gov/40789982/)). M2-polarized tumor-associated macrophages suppress anti-tumor CD8+ T cell responses, creating an immunosuppressive milieu that may limit the efficacy of immune checkpoint inhibitor monotherapy.

Critically, this mechanism is therapeutically actionable: "Our results demonstrate that the combination treatment significantly reduces tumor growth, decreases the number of M2-like macrophages, and enhances CD8+ T cell infiltration compared to monotherapy with PD1 antibody alone" ([PMID: 40789982](https://pubmed.ncbi.nlm.nih.gov/40789982/)). The combination of anti-IL-6 with PD-1 blockade overcomes the AFB1-driven immunosuppression, suggesting that patients with aflatoxin-related HCC may benefit from rational combination immunotherapy strategies rather than checkpoint inhibitor monotherapy.

---

## Mechanistic Model / Interpretation

### Causal Chain: From AFB1 Ingestion to Hepatocellular Carcinoma

The pathogenesis of aflatoxin-related HCC involves a well-defined multi-step cascade from dietary exposure to malignant transformation, with synergistic contributions from HBV and genetic susceptibility:

```
STAGE 1: EXPOSURE AND BIOACTIVATION
═══════════════════════════════════
Dietary AFB1 (contaminated maize, groundnuts, cereals)
        │
        ▼
Hepatic Uptake → Endoplasmic Reticulum
        │
        ├──► CYP1A2 (primary, 72% at low [AFB1])──► AFB1-exo-8,9-Epoxide (AFBO)
        │                                                    │
        └──► CYP3A4 (46% at high [AFB1])──────────────────►─┘
                                                              │
                                              ┌───────────────┤
                                              │               │
                                              ▼               ▼
                                   Phase II Detox    DNA Adduct Formation
                                   (GSTs: GSTA3)     (AFB1-N7-Guanine)
                                        │                    │
                                        ▼                    ▼
                                   EXCRETION           MUTAGENESIS
                                   (safe)              G→T transversion

STAGE 2: MUTAGENESIS AND TUMOR SUPPRESSOR LOSS
═══════════════════════════════════════════════
     AFB1-N7-Guanine adduct at TP53 codon 249
                      │
                      ▼
           TP53 R249S Mutation (AGG→AGT)
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
 LOSS OF FUNCTION            GAIN OF FUNCTION
 • No DNA binding            • CDK4 phosphorylation
 • No transcription          • PIN1 binding
 • Failed apoptosis          • c-Myc activation
 • Failed cell cycle         • Ribosomal biogenesis
   arrest                    • Enhanced proliferation

STAGE 3: HBV SYNERGY (when co-infected)
═══════════════════════════════════════
 HBV Chronic Infection
         │
         ├──► HBx protein ──► p53-R249S complex ──► Enhanced proliferation
         │
         ├──► YTHDF2 ↑ ──► PARP1 ↓ (m6A-mediated) ──► Impaired DNA repair
         │                                              ──► More mutations
         └──► Chronic hepatitis ──► Regeneration cycles ──► Fixation of mutations

STAGE 4: IMMUNE EVASION AND TUMOR PROGRESSION
═══════════════════════════════════════════════
 AFB1 exposure (tumor cells)
         │
         ▼
 NF-κB activation ──► IL-6 upregulation
                           │
                           ▼
                  M2 macrophage polarization
                           │
                           ├──► CD8+ T cell suppression
                           │
                           └──► Immunosuppressive microenvironment
                                        │
                                        ▼
                           HEPATOCELLULAR CARCINOMA
```

### Genetic Susceptibility Modifiers

The balance between bioactivation and detoxification determines individual cancer risk:

| Genotype Combination | Effect | OR (95% CI) | Reference |
|---|---|---|---|
| GSTM1-null alone | Reduced AFB1-epoxide conjugation | 2.45 (1.21–4.95) | [PMID: 15734960](https://pubmed.ncbi.nlm.nih.gov/15734960/) |
| GSTT1-null + AFB1 + HBsAg+ | Impaired detox in HBV carriers | 3.7 (1.5–9.3) | [PMID: 11470760](https://pubmed.ncbi.nlm.nih.gov/11470760/) |
| XRCC1-399 AG | Impaired base excision repair | 3.18 (1.35–7.51) | [PMID: 15734960](https://pubmed.ncbi.nlm.nih.gov/15734960/) |
| Triple risk (GSTM1-null + HYL1*2 + XRCC1) | Multiplicative interaction | ~14.7 | [PMID: 16884947](https://pubmed.ncbi.nlm.nih.gov/16884947/) |
| GSTM1+GSTT1 double-null (meta-analysis) | Combined deficiency | 1.88 (1.41–2.50) | [PMID: 24399650](https://pubmed.ncbi.nlm.nih.gov/24399650/) |

### Therapeutic Implications of the Mechanistic Model

The detailed mechanistic understanding of aflatoxin-related HCC suggests multiple therapeutic intervention points:

1. **Upstream (prevention):** Block AFB1 bioactivation (oltipraz inducing GSTs) or reduce bioavailability (chlorophyllin complexation)
2. **Midstream (mutation-targeted):** Co-target CDK4 and p53-R249S to disrupt the gain-of-function pathway ([PMID: 31747859](https://pubmed.ncbi.nlm.nih.gov/31747859/))
3. **Downstream (immune restoration):** Combine anti-IL-6 with anti-PD-1 to overcome AFB1-driven immunosuppression ([PMID: 40789982](https://pubmed.ncbi.nlm.nih.gov/40789982/))
4. **Concurrent (anti-HBV):** Antiviral therapy to eliminate the synergistic co-factor

---

## Disease Information and Classification

### Key Identifiers

| Identifier | Code/ID |
|---|---|
| ICD-10 | C22.0 (Hepatocellular carcinoma) |
| ICD-11 | 2C12.0 (Hepatocellular carcinoma) |
| MeSH | D006528 (Carcinoma, Hepatocellular); D016604 (Aflatoxin B1) |
| MONDO | MONDO:0007256 (hepatocellular carcinoma) |
| OMIM | 114550 (Hepatocellular Carcinoma) |
| Orphanet | ORPHA:88673 (Hepatocellular carcinoma) |
| IARC | Group 1 carcinogen (Aflatoxin B1) |
| CHEBI | CHEBI:2504 (Aflatoxin B1) |

### Synonyms
- Aflatoxin-induced hepatocellular carcinoma
- AFB1-related liver cancer
- Aflatoxin-associated hepatoma
- Mycotoxin-related hepatocellular carcinoma
- Hepatocellular carcinoma with TP53 R249S mutation

---

## Etiology

### Primary Cause: Aflatoxin B1 Exposure

Aflatoxin B1 (AFB1; CHEBI:2504) is the most potent naturally occurring hepatocarcinogen, a secondary metabolite of *Aspergillus flavus* (NCBI Taxon: 5059) and *Aspergillus parasiticus* (NCBI Taxon: 5067). These fungi contaminate staple crops including maize, groundnuts, tree nuts, and cereals, particularly under warm, humid storage conditions ([PMID: 40711142](https://pubmed.ncbi.nlm.nih.gov/40711142/)). In southern Mexico, the prevalence of AFB1 in serum samples reaches 85.5% (95% CI 72.1–93.1) ([PMID: 35438902](https://pubmed.ncbi.nlm.nih.gov/35438902/)).

### Co-Factors and Risk Factors

**Environmental:**
- Chronic HBV infection: present in ~80% of HCC worldwide ([PMID: 11185536](https://pubmed.ncbi.nlm.nih.gov/11185536/))
- Fumonisin B1 co-exposure: synergistically increases GST-P+ foci 7–13-fold in rat models ([PMID: 27430420](https://pubmed.ncbi.nlm.nih.gov/27430420/))
- Alcohol consumption, smoking, obesity/metabolic syndrome ([PMID: 41201177](https://pubmed.ncbi.nlm.nih.gov/41201177/))
- Male sex (2–3:1 male predominance) ([PMID: 11185536](https://pubmed.ncbi.nlm.nih.gov/11185536/))
- Pregnancy: 2-fold higher AFB1-N7-guanine DNA adducts due to elevated CYP expression ([PMID: 28973694](https://pubmed.ncbi.nlm.nih.gov/28973694/))

**Genetic susceptibility modifiers:** GSTM1-null, GSTT1-null, XRCC1-399 AG, HYL1*2, ADAMTS18 variants (see detailed quantification in Findings above)

### Protective Factors

- HBV vaccination ([PMID: 25987009](https://pubmed.ncbi.nlm.nih.gov/25987009/))
- GSTM1/GSTT1 present (non-null) genotypes ([PMID: 16536303](https://pubmed.ncbi.nlm.nih.gov/16536303/))
- Selenium (inverse association with AFB1-albumin adducts) ([PMID: 11525595](https://pubmed.ncbi.nlm.nih.gov/11525595/))
- Chlorophyllin and oltipraz chemoprevention ([PMID: 15508099](https://pubmed.ncbi.nlm.nih.gov/15508099/))
- Probiotics: 23% reduction in urinary AFM1 ([PMID: 40250564](https://pubmed.ncbi.nlm.nih.gov/40250564/))
- Purple rice bran extract: modulates CYP1A2/CYP3A and enhances GST/UGT ([PMID: 25921147](https://pubmed.ncbi.nlm.nih.gov/25921147/))

---

## Phenotypes

### Clinical Manifestations

| Phenotype | HPO Term | Type | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Hepatomegaly | HP:0002240 | Physical sign | Adult | Variable | ~60–70% |
| Right upper quadrant pain | HP:0100280 | Symptom | Adult | Moderate–severe | ~50–60% |
| Weight loss | HP:0001824 | Symptom | Adult | Progressive | ~30–50% |
| Jaundice | HP:0000952 | Clinical sign | Late | Variable | ~20–40% |
| Ascites | HP:0001541 | Physical sign | Advanced | Severe | ~20–30% |
| Fatigue | HP:0012378 | Symptom | Variable | Variable | ~30–50% |
| Portal hypertension | HP:0001409 | Clinical sign | Advanced | Severe | ~40–60% |
| Elevated AFP | HP:0006254 | Lab abnormality | Variable | Variable | ~60–70% |
| Elevated transaminases | HP:0002910 | Lab abnormality | Variable | Variable | ~60–80% |
| Thrombocytopenia | HP:0001873 | Lab abnormality | Cirrhotic stage | Variable | ~30–50% |

In AFB1-endemic regions, HCC presents at notably younger ages (20s–40s in sub-Saharan Africa) compared to non-endemic areas (50s–70s). "In these regions and populations, the tumor shows a distinct shift in age distribution toward the younger ages, seen to greatest extent in sub-Saharan Black Africans" ([PMID: 27508181](https://pubmed.ncbi.nlm.nih.gov/27508181/)).

---

## Genetic and Molecular Information

### TP53 R249S (OMIM: 191170; HGNC:11998)
- **Variant:** c.747G>T (p.R249S) — the "aflatoxin signature mutation"
- **Classification:** Pathogenic somatic mutation (not germline)
- **Functional consequences:** Loss of tumor suppressor function AND gain of oncogenic function (CDK4-PIN1-c-Myc pathway)
- **COSMIC:** Present in COSMIC database as a hotspot hepatocellular carcinoma mutation

### Other Genetic Alterations
- **CTNNB1/β-catenin:** Activating mutations more common in non-AFB1 HCC ([PMID: 16799619](https://pubmed.ncbi.nlm.nih.gov/16799619/))
- **AXIN1/AXIN2:** Wnt pathway negative regulator mutations
- **Two hepatocarcinogenesis pathways:** Chromosomally instable (HBV/AFB1-related, TP53 mutations, poorly differentiated) vs. chromosomally stable (non-HBV, β-catenin activated, well-differentiated) ([PMID: 16799619](https://pubmed.ncbi.nlm.nih.gov/16799619/))

### Epigenetic Changes
- Aberrant DNA methylation, histone modifications, and microRNA dysregulation cooperate with genetic mutations ([PMID: 25421688](https://pubmed.ncbi.nlm.nih.gov/25421688/); [PMID: 30304666](https://pubmed.ncbi.nlm.nih.gov/30304666/))
- m6A RNA modification: YTHDF2-PARP1 axis mediating HBV-AFB1 synergy ([PMID: 40344782](https://pubmed.ncbi.nlm.nih.gov/40344782/))

---

## Pathophysiology: Molecular Pathways

### Key Signaling Pathways

| Pathway | Role in Disease | GO/KEGG Terms |
|---|---|---|
| CYP450 bioactivation | AFB1 → AFBO initiating event | GO:0006805 (xenobiotic metabolic process) |
| p53 tumor suppression | Loss of apoptosis/cell cycle control | GO:0006915 (apoptotic process) |
| CDK4-PIN1-c-Myc | R249S gain-of-function proliferation | GO:0008283 (cell proliferation) |
| NF-κB/IL-6/STAT3 | Inflammation, immune evasion | GO:0038061 (NF-kappaB signaling) |
| Nrf2/Keap1 | Oxidative stress response | GO:0006979 (response to oxidative stress) |
| Wnt/β-catenin | Proliferation (less prominent in AFB1-HCC) | hsa04310 (Wnt signaling pathway) |
| MAPK/TGF-β | Cell adhesion, migration (AFB1-transformed cells) | GO:0000165 (MAPK cascade) |

### Cell Types Involved

| Cell Type | CL Term | Role |
|---|---|---|
| Hepatocyte | CL:0000182 | Primary target of transformation |
| Kupffer cell | CL:0000091 | Inflammatory response, M2 polarization |
| Hepatic stellate cell | CL:0000632 | Fibrosis, tumor microenvironment |
| CD8+ T lymphocyte | CL:0000794 | Anti-tumor immunity (suppressed) |
| Tumor-associated macrophage | CL:0000863 | M2-polarized, immunosuppressive |
| Hepatic progenitor cell | CL:0002196 | Potential cell of origin |

---

## Anatomical Structures Affected

- **Primary organ:** Liver (UBERON:0002107)
- **Secondary involvement:** Lungs (UBERON:0002048), bones (UBERON:0002481), lymph nodes (UBERON:0000029), adrenal glands (UBERON:0002369)
- **Subcellular compartments:** Nucleus (GO:0005634; DNA adducts), endoplasmic reticulum (GO:0005783; CYP450 bioactivation), mitochondria (GO:0005739; oxidative stress), cytosol (GO:0005829; GST detoxification)
- Background cirrhosis present in 80–90% of cases ([PMID: 20547305](https://pubmed.ncbi.nlm.nih.gov/20547305/))

---

## Temporal Development

- **Onset:** Insidious; 20s–40s in sub-Saharan Africa, 40s–60s in Southeast Asia; exposure from early childhood ([PMID: 27508181](https://pubmed.ncbi.nlm.nih.gov/27508181/))
- **Staging:** BCLC system (Stage 0/A: curative treatment possible; Stage B: TACE; Stage C: systemic therapy; Stage D: best supportive care)
- **Course:** Progressive; "almost always runs a fulminant course" without treatment ([PMID: 27508181](https://pubmed.ncbi.nlm.nih.gov/27508181/))
- **Critical window:** Pregnancy may increase susceptibility through elevated CYP expression ([PMID: 28973694](https://pubmed.ncbi.nlm.nih.gov/28973694/))

---

## Epidemiology and Population

- **Global HCC:** ~550,000–600,000 new cases/year; 3rd leading cause of cancer death ([PMID: 38927059](https://pubmed.ncbi.nlm.nih.gov/38927059/))
- **AFB1-attributable:** 4.6–28.2% of all HCC (25,200–155,000 cases/year) ([PMID: 20172840](https://pubmed.ncbi.nlm.nih.gov/20172840/))
- **High-incidence regions (>20/100,000):** Sub-Saharan Africa, Southeast Asia, China ([PMID: 20547305](https://pubmed.ncbi.nlm.nih.gov/20547305/))
- **Sex ratio:** Males 2–3:1 (up to 5:1 in high-risk regions) ([PMID: 11185536](https://pubmed.ncbi.nlm.nih.gov/11185536/))
- **Inheritance:** Multifactorial/polygenic; not Mendelian; familial clustering reflects shared environment and genetic background ([PMID: 36851773](https://pubmed.ncbi.nlm.nih.gov/36851773/))
- **Trends:** Declining in Singapore/Shanghai (HBV vaccination + aflatoxin control); increasing in Western countries (MASLD/obesity) ([PMID: 11185536](https://pubmed.ncbi.nlm.nih.gov/11185536/); [PMID: 41201177](https://pubmed.ncbi.nlm.nih.gov/41201177/))

---

## Diagnostics

### Clinical Tests and Biomarkers

| Test | Purpose | Notes |
|---|---|---|
| Serum AFP | Screening/diagnosis | Elevated in ~60–70%; AFP-L3 fraction improves specificity |
| DCP (PIVKA-II) | Diagnosis | Complementary to AFP |
| AFB1-albumin adducts | Exposure biomarker | ELISA; reflects 2–3 months exposure ([PMID: 11525595](https://pubmed.ncbi.nlm.nih.gov/11525595/)) |
| Urinary AFM1 | Exposure biomarker | Reflects recent exposure ([PMID: 28114823](https://pubmed.ncbi.nlm.nih.gov/28114823/)) |
| Multiphasic CT/MRI | Imaging diagnosis | Arterial hyperenhancement + washout |
| Ultrasound | Screening | Every 6 months in high-risk populations |
| TP53 R249S (ddPCR) | Molecular diagnosis + exposure | Liquid biopsy in cell-free DNA ([PMID: 29749584](https://pubmed.ncbi.nlm.nih.gov/29749584/)) |
| COSMIC Signature 24 | Mutational signature | AFB1-associated pattern; C>A mutations ([PMID: 30045675](https://pubmed.ncbi.nlm.nih.gov/30045675/)) |

### Staging
- BCLC (Barcelona Clinic Liver Cancer) staging integrating tumor burden, liver function (Child-Pugh), and performance status (ECOG)
- AASLD/EASL diagnostic guidelines for non-invasive diagnosis

---

## Outcome and Prognosis

- **Overall prognosis:** Poor; "almost always runs a fulminant course and carries an especially grave prognosis. It has a low resectability rate and a high recurrence rate after surgical intervention" ([PMID: 27508181](https://pubmed.ncbi.nlm.nih.gov/27508181/))
- **5-year survival:** 50–70% (early stage with curative treatment); <5% (end-stage)
- **Median OS with first-line therapy:** ~19.2 months (atezolizumab+bevacizumab); ~10.7 months (sorafenib)
- **Prognostic biomarkers:** AFP level, TP53 R249S cfDNA status, Child-Pugh score, vascular invasion, telomerase activity ([PMID: 11783914](https://pubmed.ncbi.nlm.nih.gov/11783914/))

---

## Treatment

### First-Line Systemic Therapy

| Regimen | Evidence | MAXO Term |
|---|---|---|
| Atezolizumab + Bevacizumab | Standard of care; 88% probability of best 30-month OS ([PMID: 38751554](https://pubmed.ncbi.nlm.nih.gov/38751554/)) | MAXO:0000451 |
| Durvalumab + Tremelimumab | Approved first-line | MAXO:0000451 |
| Sorafenib | First approved agent (2007) | MAXO:0001052 |
| Lenvatinib | Non-inferior to sorafenib ([PMID: 37589044](https://pubmed.ncbi.nlm.nih.gov/37589044/)) | MAXO:0001052 |

### Second-Line and Beyond
- Regorafenib, cabozantinib, ramucirumab (TKIs)
- Nivolumab, pembrolizumab (PD-1 inhibitors)
- Regorafenib + PD-1 or apatinib + PD-1 after lenvatinib + PD-1 progression ([PMID: 40082982](https://pubmed.ncbi.nlm.nih.gov/40082982/))

### R249S-Specific Therapy (Experimental)
Co-targeting CDK4 (palbociclib/PD-0332991) + p53-R249S restoration (CP-31398) showed synergistic inhibition of HCC cell growth in a p53-R249S-dependent manner ([PMID: 31747859](https://pubmed.ncbi.nlm.nih.gov/31747859/)). This represents a precision medicine approach specifically for AFB1-related HCC.

### Immunotherapy Optimization for AFB1-Related HCC
Anti-IL-6 + anti-PD-1 combination overcomes AFB1-driven M2 macrophage polarization, "significantly reduces tumor growth, decreases the number of M2-like macrophages, and enhances CD8+ T cell infiltration" ([PMID: 40789982](https://pubmed.ncbi.nlm.nih.gov/40789982/)).

### Surgical/Interventional
- Hepatic resection (MAXO:0000004), liver transplantation (MAXO:0001175), radiofrequency ablation, TACE, TARE/Y90
- Proton radiotherapy + immunotherapy: 2-year OS 77% in BCLC B/C with macrovascular invasion ([PMID: 41585427](https://pubmed.ncbi.nlm.nih.gov/41585427/))

---

## Prevention

### Primary Prevention
- **HBV vaccination (MAXO:0001017):** Single most effective intervention; universal infant vaccination dramatically reduces HBV carrier rates and HCC incidence ([PMID: 25987009](https://pubmed.ncbi.nlm.nih.gov/25987009/))
- **Aflatoxin reduction:** Improved post-harvest drying and storage; biocontrol with atoxigenic *Aspergillus* strains; food safety regulations ([PMID: 12534775](https://pubmed.ncbi.nlm.nih.gov/12534775/))
- **Chemoprevention:** Chlorophyllin and oltipraz validated in clinical trials ([PMID: 15508099](https://pubmed.ncbi.nlm.nih.gov/15508099/))

### Secondary Prevention
- HCC surveillance: ultrasound ± AFP every 6 months
- AFP screening programs in high-incidence areas ([PMID: 2430432](https://pubmed.ncbi.nlm.nih.gov/2430432/))
- Antiviral therapy for chronic HBV

### Public Health
- "In Guinea-Conakry, West Africa, surveys of HBV infection and aflatoxin exposure have established baseline data for the implementation of a community-based intervention study" ([PMID: 12534775](https://pubmed.ncbi.nlm.nih.gov/12534775/))
- Integration of vaccination, aflatoxin control, and screening programs

---

## Animal Models and Other Species

### Rodent Models

| Model | Strengths | Limitations |
|---|---|---|
| F344 rat + AFB1 | Gold standard; GST-P+ foci, HCC development; chemoprevention testing | No HBV infection capability |
| B6C3F1/N mouse + AFB1 | COSMIC Signature 24 matches human HCC ([PMID: 30045675](https://pubmed.ncbi.nlm.nih.gov/30045675/)) | Species CYP differences |
| HBsAg transgenic mouse + AFB1 | Synergy recapitulation; 11-gene HCC signature ([PMID: 26035378](https://pubmed.ncbi.nlm.nih.gov/26035378/)) | Mouse HBV biology differs |
| Tree shrew + HBV + AFB1 | Natural HBV susceptibility; FTCD-AS1-PXR-MASP1 axis ([PMID: 39824452](https://pubmed.ncbi.nlm.nih.gov/39824452/)) | Limited genetic tools |

### In Vitro Models
- WB-F344 hepatic stem cells: AFB1 transformation model ([PMID: 24299315](https://pubmed.ncbi.nlm.nih.gov/24299315/))
- PLC/PRF/5: Constitutively expresses p53-R249S and HBx ([PMID: 20538734](https://pubmed.ncbi.nlm.nih.gov/20538734/))
- HepG2.2.15: HBV-integrated; HBV-AFB1 synergy studies ([PMID: 40344782](https://pubmed.ncbi.nlm.nih.gov/40344782/))

### Veterinary Relevance
- AFB1 contamination of animal feed causes aflatoxicosis in poultry, swine, cattle
- Turkey X disease (1960) was the original event leading to aflatoxin discovery
- AFM1 in milk from exposed dairy animals contributes minimally to human HCC risk (~0.001–0.003% of cases) ([PMID: 35470382](https://pubmed.ncbi.nlm.nih.gov/35470382/))

---

## Ontology Term Summary

| Category | Terms |
|---|---|
| **MONDO** | MONDO:0007256 (hepatocellular carcinoma) |
| **HPO** | HP:0002240 (Hepatomegaly), HP:0001824 (Weight loss), HP:0000952 (Jaundice), HP:0001541 (Ascites), HP:0001409 (Portal hypertension), HP:0006254 (Elevated AFP), HP:0002910 (Elevated transaminases) |
| **GO (BP)** | GO:0006805 (Xenobiotic metabolism), GO:0006749 (Glutathione metabolism), GO:0006281 (DNA repair), GO:0006915 (Apoptosis), GO:0008283 (Cell proliferation), GO:0006979 (Oxidative stress response), GO:0006954 (Inflammatory response) |
| **GO (CC)** | GO:0005634 (Nucleus), GO:0005783 (ER), GO:0005739 (Mitochondria), GO:0005829 (Cytosol) |
| **CL** | CL:0000182 (Hepatocyte), CL:0000091 (Kupffer cell), CL:0000632 (Hepatic stellate cell), CL:0000794 (CD8+ T cell) |
| **UBERON** | UBERON:0002107 (Liver), UBERON:0002048 (Lung), UBERON:0002481 (Bone) |
| **CHEBI** | CHEBI:2504 (Aflatoxin B1), CHEBI:50924 (Sorafenib), CHEBI:16856 (Glutathione) |
| **MAXO** | MAXO:0000451 (Immunotherapy), MAXO:0000004 (Surgery), MAXO:0001175 (Transplantation), MAXO:0001017 (Vaccination) |

---

## Evidence Base

### Landmark Publications

| PMID | Key Contribution | Citation Basis |
|---|---|---|
| [20172840](https://pubmed.ncbi.nlm.nih.gov/20172840/) | Quantified 25,200–155,000 annual AFB1-attributable HCC cases globally | Direct quote validated from abstract |
| [20538734](https://pubmed.ncbi.nlm.nih.gov/20538734/) | Demonstrated R249S accounts for 90% of TP53 mutations in AFB1-HCC; functional studies | Direct quote validated from abstract |
| [29749584](https://pubmed.ncbi.nlm.nih.gov/29749584/) | ddPCR detection of R249S in cfDNA; 24.8% prevalence in Middle Africa | Direct quote validated from abstract |
| [19345001](https://pubmed.ncbi.nlm.nih.gov/19345001/) | Established more-than-multiplicative HBV-AFB1 synergy | Direct quote validated from abstract |
| [8261428](https://pubmed.ncbi.nlm.nih.gov/8261428/) | Defined CYP1A2 (72%) and CYP3A4 as AFB1 bioactivation enzymes | Direct quote validated from abstract |
| [29225033](https://pubmed.ncbi.nlm.nih.gov/29225033/) | CDK4-PIN1-c-Myc gain-of-function mechanism of p53-R249S | Direct quote validated from abstract |
| [15734960](https://pubmed.ncbi.nlm.nih.gov/15734960/) | GSTM1/XRCC1 polymorphisms and HCC risk in AFB1-endemic Gambia | Direct quote validated from abstract |
| [16884947](https://pubmed.ncbi.nlm.nih.gov/16884947/) | Triple risk genotype (GSTM1+HYL1*2+XRCC1) = 15-fold HCC risk | Direct quote validated from abstract |
| [15508099](https://pubmed.ncbi.nlm.nih.gov/15508099/) | Oltipraz and chlorophyllin clinical trial results | Direct quote validated from abstract |
| [40789982](https://pubmed.ncbi.nlm.nih.gov/40789982/) | AFB1 drives M2 macrophage polarization via IL-6/NF-κB; anti-IL-6+PD-1 therapy | Direct quote validated from abstract |
| [40344782](https://pubmed.ncbi.nlm.nih.gov/40344782/) | HBV-YTHDF2-PARP1 axis in DNA damage exacerbation | Direct quote validated from abstract |
| [33457005](https://pubmed.ncbi.nlm.nih.gov/33457005/) | GWAS identified ADAMTS18 loci for R249S susceptibility | Direct quote validated from abstract |
| [31747859](https://pubmed.ncbi.nlm.nih.gov/31747859/) | CDK4 + p53-R249S co-targeting synergistic therapy | Direct quote validated from abstract |
| [11470760](https://pubmed.ncbi.nlm.nih.gov/11470760/) | GSTT1-null × AFB1 interaction in HBsAg carriers (OR=3.7) | Direct quote validated from abstract |
| [24399650](https://pubmed.ncbi.nlm.nih.gov/24399650/) | Meta-analysis of GSTM1/GSTT1 and HCC risk (33 studies) | Direct quote validated from abstract |

### Supporting Evidence (Selected)

| PMID | Topic |
|---|---|
| [27508181](https://pubmed.ncbi.nlm.nih.gov/27508181/) | HCC epidemiology and risk factors (comprehensive review) |
| [38927059](https://pubmed.ncbi.nlm.nih.gov/38927059/) | Molecular mechanisms and targeted treatments in HCC |
| [16799619](https://pubmed.ncbi.nlm.nih.gov/16799619/) | Two pathways of hepatocarcinogenesis (chromosomal instability) |
| [25421688](https://pubmed.ncbi.nlm.nih.gov/25421688/) | Epigenetic aberrations in HCC |
| [30304666](https://pubmed.ncbi.nlm.nih.gov/30304666/) | AFB1-induced epigenetic alterations |
| [30045675](https://pubmed.ncbi.nlm.nih.gov/30045675/) | Exome sequencing and COSMIC Signature 24 in mouse HCC |
| [26035378](https://pubmed.ncbi.nlm.nih.gov/26035378/) | HBsAg transgenic mouse + AFB1 model characterization |
| [28973694](https://pubmed.ncbi.nlm.nih.gov/28973694/) | Pregnancy alters AFB1 metabolism and DNA damage |
| [38751554](https://pubmed.ncbi.nlm.nih.gov/38751554/) | Network meta-analysis of first-line HCC therapies |
| [12534775](https://pubmed.ncbi.nlm.nih.gov/12534775/) | AFB1/HBV role and prevention in Guinea-Conakry |

---

## Limitations and Knowledge Gaps

1. **Nosological classification:** Aflatoxin-related HCC lacks a distinct MONDO or OMIM entry separate from general HCC, limiting systematic data aggregation and research coordination for this specific etiological subtype.

2. **Dose-response quantification:** Precise dose-response relationships for AFB1 alone remain difficult to determine in human populations due to confounding from HBV co-exposure, variable dietary patterns, and lack of long-term prospective exposure monitoring.

3. **R249S therapeutic translation:** The CDK4/6 inhibitor + p53-restoring compound combination (PD-0332991 + CP-31398) has been characterized only in cell lines and animal models. No human clinical trials have tested this approach in R249S-positive HCC patients.

4. **Immunotherapy optimization:** The IL-6/NF-κB/M2 macrophage axis driving immunosuppression is a very recent discovery (2025–2026). The clinical relevance of anti-IL-6 + anti-PD-1 combinations specifically for AFB1-related HCC has not been validated in human trials.

5. **Biomarker accessibility:** AFB1-albumin adducts, urinary AFM1, and ddPCR-based R249S cfDNA detection are validated research biomarkers but remain unavailable in most clinical settings in the resource-limited regions where disease burden is highest.

6. **Scalability of chemoprevention:** While oltipraz and chlorophyllin show proof-of-concept efficacy, large-scale implementation in endemic regions faces logistical, economic, and sustainability challenges. Long-term cancer incidence endpoints have not been evaluated.

7. **Incomplete multi-omics profiling:** Comprehensive single-cell transcriptomic, epigenomic, and proteomic profiling specifically comparing AFB1-related vs. non-AFB1-related HCC has not been performed at scale, limiting understanding of subtype-specific biology.

8. **Pharmacogenomics of treatment response:** The role of CYP450 and GST polymorphisms in modulating treatment response (beyond disease risk) remains poorly characterized.

---

## Proposed Follow-up Experiments / Actions

### Clinical and Translational

1. **Phase II trial of CDK4/6 inhibitor + p53-restoring compound in R249S-positive HCC:** Stratify advanced HCC patients by TP53 R249S status (liquid biopsy) and test palbociclib + CP-31398 (or next-generation p53 reactivators) in a biomarker-selected population, with R249S-negative patients as controls.

2. **Randomized trial of anti-IL-6 (tocilizumab) + anti-PD-1 in AFB1-endemic HCC:** Evaluate whether targeting the AFB1-driven immunosuppressive microenvironment improves checkpoint inhibitor response rates in sub-Saharan African or Southeast Asian HCC cohorts.

3. **Liquid biopsy validation for population screening:** Prospective evaluation of ddPCR-based TP53 R249S detection in cell-free DNA as both a diagnostic and population-level exposure surveillance biomarker in high-risk communities.

### Epidemiological

4. **Multi-country prospective cohort study:** Longitudinal assessment of AFB1 biomarkers (AFB1-albumin adducts, urinary AFM1) combined with genomic characterization (GST, XRCC1, CYP polymorphisms) and HCC incidence outcomes across multiple AFB1-endemic African countries.

5. **Large-scale dietary chemoprevention trial:** Evaluate food-based interventions (chlorophyllin, broccoli sprout beverage, probiotics) at population scale in endemic regions with cancer incidence as a primary endpoint, complementing the existing biomarker-based proof-of-concept data.

### Basic Science

6. **Single-cell RNA sequencing of R249S-positive vs. wild-type HCC tumors:** Characterize tumor microenvironment differences with emphasis on macrophage polarization states, T cell exhaustion markers, and cancer-associated fibroblast subtypes.

7. **CRISPR functional genomics screen:** Systematically identify synthetic lethal interactions with TP53 R249S in isogenic hepatocyte models to discover new therapeutic targets beyond the CDK4-PIN1 axis.

8. **Integrated multi-omics analysis (TCGA/ICGC reanalysis):** Stratify existing HCC genomic datasets by R249S status and AFB1 exposure biomarkers to define the complete molecular subtype signature of aflatoxin-related HCC.

### Public Health

9. **Rapid AFB1 testing deployment:** Develop and field-test lateral-flow immunoassay devices for AFB1 detection in food markets across endemic regions, coupled with community education programs about proper crop storage.

10. **Cost-effectiveness modeling:** Comprehensive health-economic analysis of integrated prevention programs (HBV vaccination + aflatoxin reduction + chemoprevention + HCC screening) to guide resource allocation in high-burden countries.

---

*Report generated: 2026-05-05 | Based on analysis of 78 published papers | 5 confirmed findings | 1 research iteration*
