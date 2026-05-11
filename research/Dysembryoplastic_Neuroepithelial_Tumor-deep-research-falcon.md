---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T11:03:50.588427'
end_time: '2026-05-11T11:29:46.550060'
duration_seconds: 1555.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dysembryoplastic Neuroepithelial Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dysembryoplastic Neuroepithelial Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Dysembryoplastic Neuroepithelial Tumor** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dysembryoplastic Neuroepithelial Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Dysembryoplastic Neuroepithelial Tumor** covering all of the
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


# Dysembryoplastic Neuroepithelial Tumor (DNET/DNT): Disease Characteristics Research Report

**Target disease:** Dysembryoplastic neuroepithelial tumor (also written dysembryoplastic neuroepithelial tumour; abbreviation **DNET** or **DNT**). (rahim2023clinicopathologicalfeaturesof pages 1-2, khalilov2024atypicalpresentationof pages 1-2)

**Category (high level):** WHO-defined circumscribed **glioneuronal tumor**; a prototypic **low-grade epilepsy-associated neuroepithelial tumor (LEAT)** entity. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

**MONDO ID:** Not found in the retrieved primary literature corpus used here (evidence gap noted). (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

## Executive snapshot (knowledge-base compact)

| Domain | Key characteristics |
|---|---|
| Definition/classification | • Rare benign glioneuronal tumor; classic representative of low-grade epilepsy-associated tumors (LEATs) • WHO CNS 2021/5th-ed context: WHO grade 1 • Often termed DNET/DNT in literature • Characteristic alteration in LEAT classification tables: FGFR1 (xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3, xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial media 10d99c66) |
| Epidemiology | • Rare: estimated incidence ~0.03/100,000/year in the US • Reported prevalence among CNS tumors: ~1.2% in patients <20 years and ~0.2% in >20 years • DNT/DNET is among the commonest LEATs, with ganglioglioma together accounting for >75% of pediatric LEATs and >80% of LEATs in some epilepsy-surgery series (zhang2022longtermseizureoutcomes pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2, pelissier2026pediatriclowgradeepilepsyassociated pages 1-3, iijima2024genotyperelevantneuroimagingfeatures pages 1-2) |
| Typical presentation | • Usually children/adolescents or young adults; LEAT seizure onset often ~12–15 years • Main presentation is chronic focal/drug-resistant epilepsy; seizures may be the only symptom • Rare non-epileptic presentations occur (e.g., headache without epileptiform activity) (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, khalilov2024atypicalpresentationof pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2) |
| Anatomy/location | • Supratentorial, cortical or cortico-subcortical tumor • Strong temporal lobe predilection: ~65–80% of LEATs temporal; >67% temporal in DNT series • Frontal lobe is the second most common site • Frequent association with adjacent focal cortical dysplasia/peritumoral cortical dysplasia (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2, bonney2016reviewofseizure pages 4-5) |
| Imaging/pathology hallmarks | • MRI often shows cortical-based lesion spanning cortical thickness, usually without major mass effect/edema • MRI patterns reported as cystic-like, nodular-like, and dysplastic-like types • Histology: multinodular architecture, specific glioneuronal element, oligodendrocyte-like cells in mucinous matrix, and “floating neurons” • Very low proliferative index; Ki-67 typically <1% (rahim2023clinicopathologicalfeaturesof pages 1-2, zhang2022longtermseizureoutcomes pages 2-5) |
| Molecular genetics | • FGFR1 is the dominant driver: hotspot mutations (p.N546, p.K656), tyrosine kinase domain/internal tandem duplication, and rare fusions • Frequency of FGFR1 alterations reported at ~58.1% in neuropathology-confirmed DNT (25/43) and ~68% in a 58-case specific DNT cohort • MAPK pathway activation is central; some tumors also implicate PI3K/mTOR signaling • BRAF V600E can be reported in the broader DNT spectrum, but was absent in some well-curated specific DNT cohorts; rare alternative fusions include LHFPL3::NTRK2 (rivera2016germlineandsomatic pages 1-2, lucas2020comprehensiveanalysisof pages 1-2, jesus‐ribeiro2022thelandscapeof pages 6-7, pages2022thegenomiclandscape pages 10-10, chen2022casereporta pages 1-2) |
| Diagnostics/molecular testing | • Diagnosis remains integrated: clinical epilepsy history + MRI + neuropathology • Pre-op workup often includes long-term video-EEG; MEG/PET/SEEG used when epileptogenic zone is unclear • Molecular testing increasingly useful for difficult cases: targeted sequencing for FGFR1/BRAF/NTRK alterations and DNA methylation profiling for classification support • sEEG-electrode-derived micro-tissue has been shown feasible for NGS and methylation analysis in a 2024 DNET case (zhang2022longtermseizureoutcomes pages 2-5, gatesman2024characterizationoflow‐grade pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial media f56d460d) |
| Treatment/management | • Mainstay is maximal safe surgical resection/lesionectomy, ideally including epileptogenic zone when indicated • Gross-total resection is generally favored for seizure control; lesionectomy alone may suffice in temporal LEATs with normal hippocampus • Anti-seizure medications are used for tumor-related epilepsy, but DNET-associated epilepsy is often pharmacoresistant • Chemo/radiotherapy usually not required for typical indolent DNET; targeted therapy remains investigational/exceptional (takayama2022ishippocampalresection pages 1-2, zhang2022longtermseizureoutcomes pages 1-2, gatesman2024characterizationoflow‐grade pages 1-2) |
| Outcomes/prognosis | • Overall prognosis is favorable; biologically stable tumor with rare malignant transformation • In a 63-patient DNT cohort, 49/63 (77.8%) were seizure-free after surgery; seizure-recurrence-free rates were 82.5% at 2 years, 79.0% at 5 years, and 76.5% at 10 years • Across prior studies, seizure freedom after gross-total resection is often >80%; systematic review median seizure-free range IQR 77–93% • Better outcomes linked to gross-total resection and shorter epilepsy duration; MRI type 3/dysplastic-like pattern and bilateral interictal discharges predict worse seizure outcome (zhang2022longtermseizureoutcomes pages 1-2, zhang2022longtermseizureoutcomes pages 2-5, bonney2016reviewofseizure pages 4-5) |
| Recent developments 2023-2024 | • 2023 LEAT reviews reinforced DNET as a WHO grade 1, FGFR1-linked LEAT entity • 2024 neuroimaging-genotype work showed FGFR1-associated LEAT imaging pattern with 100% sensitivity/specificity in that cohort and poorer seizure-free rates than BRAF-pattern tumors • 2024 S/EEG-based molecular diagnosis showed practical minimally invasive tumor profiling • 2023–2024 literature increasingly emphasizes integrated histology + molecular genetics + methylation classification for diagnostically ambiguous low-grade epilepsy-associated tumors (iijima2024genotyperelevantneuroimagingfeatures pages 1-2, gatesman2024characterizationoflow‐grade pages 1-2, rosemberg2023longtermepilepsyassociatedtumors pages 1-2, rahim2023clinicopathologicalfeaturesof pages 6-7) |


*Table: This compact table summarizes core disease-characteristic facts for dysembryoplastic neuroepithelial tumor (DNET/DNT), including classification, phenotype, molecular genetics, diagnosis, treatment, and prognosis. It is designed as a concise knowledge-base-ready snapshot with quantitative details and context-ID citations.*

## 1. Disease Information

### 1.1 What is the disease?
Dysembryoplastic neuroepithelial tumor is a **rare, benign/indolent, supratentorial, epilepsy-associated glioneuronal tumor** that most commonly affects **children and young adults** and typically presents with **long-standing focal seizures**, often drug-resistant. (rahim2023clinicopathologicalfeaturesof pages 1-2, khalilov2024atypicalpresentationof pages 1-2)

Within the LEAT concept (long-term/low-grade epilepsy-associated tumors), DNET is recognized as one of the **typical representatives** alongside ganglioglioma, with a predilection for **neocortical temporal lobe** involvement and generally benign growth behavior. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

### 1.2 WHO grade and classification context
Multiple WHO-2021 (5th edition) aligned sources list DNET/DNT as **WHO grade 1** within LEAT/glioneuronal tumor groupings. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3, xie2023lowgradeepilepsyassociatedneuroepithelial media 10d99c66)

### 1.3 Synonyms and alternative names
* Dysembryoplastic neuroepithelial **tumor** (US spelling) / **tumour** (UK spelling). (pages2022thegenomiclandscape pages 10-10)
* Dysembryoplastic neuroepithelial tumor (**DNET**) / dysembryoplastic neuroepithelial tumour (**DNT**). (rahim2023clinicopathologicalfeaturesof pages 1-2)
* Informal clinical term: “**epileptoma**” (used for highly epileptogenic low-grade tumors such as DNET and ganglioglioma). (khalilov2024atypicalpresentationof pages 1-2)

### 1.4 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
No explicit OMIM/Orphanet/ICD/MeSH/MONDO identifiers were present in the retrieved full-text evidence set. This report therefore **does not assert codes** without direct supporting evidence. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

### 1.5 Evidence source type
Most disease-level information here is derived from **aggregated literature sources** (reviews, cohorts) plus a few case reports/case series and a clinical registry trial record, rather than EHR-only data. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2, NCT03970785 chunk 1)

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factors are somatic oncogenic alterations**, most commonly involving **FGFR1** and the downstream **MAPK/ERK pathway**, consistent with a developmental/circumscribed tumor biology typical for LEATs. (rivera2016germlineandsomatic pages 1-2, rivera2016germlineandsomatic pages 12-15)

Rivera et al. explicitly conclude that “**constitutional and somatic FGFR1 alterations and MAP kinase pathway activation are key events in the pathogenesis of DNET**,” supporting a molecularly driven etiology. (rivera2016germlineandsomatic pages 1-2)

### 2.2 Risk factors
**Clinical/demographic risk:** DNET is predominantly encountered in **children/adolescents/young adults** (e.g., LEAT seizure onset often around early teens) and occurs supratentorially with temporal predilection, but established population-level environmental risk factors were not identified in the retrieved corpus. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2)

**Genetic risk:** Most evidence supports **somatic** drivers rather than inherited predisposition; however, a familial scenario with a **germline FGFR1 mutation** (p.R661P) plus somatic “second hits” was reported, demonstrating a possible (rare) inherited predisposition mechanism in select families. (rivera2016germlineandsomatic pages 1-2)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved corpus. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved corpus. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

## 3. Phenotypes (clinical features)

### 3.1 Core phenotypes (with suggested HPO terms)
DNET is strongly linked to epilepsy; seizures are typically focal and may be drug-resistant. (rahim2023clinicopathologicalfeaturesof pages 1-2, khalilov2024atypicalpresentationof pages 1-2)

Key phenotypes:
* **Focal seizures / epilepsy (often drug-resistant)** — suggested HPO: **HP:0001250 (Seizures)**; **HP:0002197 (Generalized seizures)** when present; **HP:0007359 (Focal seizures)** (term name may vary by HPO release). (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2)
* **Headache** can occur, including rare presentations without epilepsy — suggested HPO: **HP:0002315 (Headache)**. (khalilov2024atypicalpresentationof pages 1-2)

### 3.2 Phenotype characteristics (age of onset, severity, progression)
* **Age of onset:** LEATs typically have seizure onsets at a young age (commonly cited ~12–15 years) and DNETs are described as occurring in children/adolescents and young adults. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2)
* **Progression:** biologically stable/benign course is typical, with rare malignant transformation. (khalilov2024atypicalpresentationof pages 1-2, zhang2022longtermseizureoutcomes pages 1-2)

Quantitative examples from a 2023 case series (Pakistan; n=14): age range **9–45 years** (mean **19**), seizure duration pre-resection **2 months to 9 years** (mean **3.2 years**), with temporal and frontal lobes most common sites. (rahim2023clinicopathologicalfeaturesof pages 1-2)

### 3.3 Quality of life impact
Seizures are commonly chronic and may be refractory, motivating epilepsy surgery; thus, DNET can substantially impact function through seizure burden (school/work limitations and medication adverse effects), although disease-specific validated QOL metrics were not extracted from the retrieved corpus. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2, avila2024braintumorrelatedepilepsy pages 10-11)

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathways
The dominant molecular theme is **RTK → RAS/MAPK/ERK activation**, with **FGFR1** as a key oncogenic driver in many DNETs; subsets also show alterations converging on **PI3K/mTOR**. (rivera2016germlineandsomatic pages 1-2, surrey2019genomicanalysisof pages 1-1)

### 4.2 Pathogenic variants and alteration types (somatic vs germline)
**FGFR1** alterations in DNET include:
* **Hotspot missense mutations** (e.g., p.N546K, p.K656E) (rivera2016germlineandsomatic pages 1-2, lucas2020comprehensiveanalysisof pages 1-2)
* **Tyrosine kinase domain duplication / internal tandem duplication (ITD)** (rivera2016germlineandsomatic pages 1-2, pages2022thegenomiclandscape pages 10-10)
* **Rare fusions/breakpoints** involving FGFR1 (rivera2016germlineandsomatic pages 12-15, pages2022thegenomiclandscape pages 10-10)

Somatic vs germline: Rivera et al. provide explicit evidence of both, reporting a **germline** FGFR1 p.R661P with **somatic** activating FGFR1 hotspot mutations (p.N546K or p.K656E) in tumor, including a case where p.K656E occurred in cis with the germline variant. (rivera2016germlineandsomatic pages 1-2)

### 4.3 Frequencies/statistics for molecular alterations
Well-curated DNET cohorts show high enrichment of FGFR1 alterations:
* In a neuropathology-confirmed cohort (43 cases), FGFR1 alterations were frequent and “**mainly comprised intragenic tyrosine kinase FGFR1 duplication and multiple mutants in cis (25/43; 58.1%) while BRAF p.V600E alterations were absent (0/43)**.” (rivera2016germlineandsomatic pages 1-2)
* In a cohort of 58 “specific” DNTs, Pagès et al. report FGFR1 disruption (mutation, ITD, fusion) and state “**In our cohort of 58 specific DNTs, we found a similar frequency (68%)**” (of FGFR1-related events). (pages2022thegenomiclandscape pages 10-10)

Broader DNT/MNGT spectrum sequencing shows that alterations frequently converge on MAPK/PI3K signaling; in one series, “more than half” (19/33) of analyzed tumors had alterations predicted to dysregulate MAPK and/or PI3K pathways. (surrey2019genomicanalysisof pages 1-1)

### 4.4 Other drivers and rare events
* **NTRK2 fusion**: A DNET case reported a novel **LHFPL3::NTRK2** fusion retaining the NTRK2 tyrosine kinase domain; authors describe likely pathogenicity through constitutive RTK signaling. (chen2022casereporta pages 1-2)
* **BRAF V600E**: Literature reports exist, but BRAF V600E may be absent in some well-curated “specific DNT” cohorts (e.g., none detected in two cohorts summarized above). (rivera2016germlineandsomatic pages 1-2, pages2022thegenomiclandscape pages 10-10)

### 4.5 Epigenetic information
DNA methylation profiling is increasingly used for difficult-to-classify low-grade neuroepithelial tumors and can support/refine diagnosis beyond morphology alone; however, DNET-specific methylation subclass statistics were not available from the retrieved evidence set. (gatesman2024characterizationoflow‐grade pages 1-2)

## 5. Environmental Information
No validated environmental/lifestyle/infectious causal factors were identified for DNET in the retrieved corpus. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (molecular → cellular → clinical)
A commonly supported mechanistic chain is:
1) **FGFR1 activation** (hotspot mutation, ITD/kinase duplication, or fusion) → 2) **increased MAPK/ERK signaling** (phospho-ERK upregulation) → 3) **tumor formation/maintenance** in cortex (glioneuronal tumor microenvironment) → 4) **cortical network hyperexcitability and epileptogenesis**, clinically manifesting as focal seizures and drug-resistant epilepsy; seizure burden is also influenced by the epileptogenic zone extending into peritumoral cortex and co-existing focal cortical dysplasia (“dual pathology”). (rivera2016germlineandsomatic pages 12-15, xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, bonney2016reviewofseizure pages 4-5)

Rivera et al. provide functional support for MAPK activation: phospho-ERK was upregulated in FGFR1-mutated cases and they report immunohistochemical confirmation of phospho-ERK upregulation in “**24/35 (69%)**” of FGFR1-mutated cases. (rivera2016germlineandsomatic pages 12-15)

### 6.2 Upstream vs downstream mechanisms
* **Upstream**: receptor tyrosine kinase (FGFR1) activating events; rare RTK fusions (e.g., NTRK2) (rivera2016germlineandsomatic pages 1-2, chen2022casereporta pages 1-2)
* **Downstream**: MAPK/ERK and sometimes PI3K/mTOR pathway dysregulation (surrey2019genomicanalysisof pages 1-1, rivera2016germlineandsomatic pages 12-15)

### 6.3 Cell types (suggested CL terms) and biological processes (suggested GO terms)
The tumor is glioneuronal, implicating glial-lineage and neuronal components and peritumoral neuronal circuitry.

Suggested Cell Ontology (CL) terms (examples):
* **CL:0000540 (Neuron)** for epileptogenic network effects and “floating neurons” concept (pathology context). (rahim2023clinicopathologicalfeaturesof pages 1-2)
* **CL:0000127 (Astrocyte)** and **CL:0000128 (Oligodendrocyte)** as relevant to glial components/oligodendrocyte-like cells described histologically. (rahim2023clinicopathologicalfeaturesof pages 1-2)

Suggested GO Biological Process terms (examples):
* **MAPK cascade** (e.g., GO:0000165) and **ERK1/2 cascade** (relevant to phospho-ERK evidence). (rivera2016germlineandsomatic pages 12-15)
* **Regulation of synaptic transmission / neuronal excitability** (epileptogenesis context; general). (avila2024braintumorrelatedepilepsy pages 10-11)

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary system affected is the **central nervous system** (brain), with seizures as the dominant symptom. (rahim2023clinicopathologicalfeaturesof pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)

### 7.2 Localization (suggested UBERON terms)
DNET is typically **supratentorial and cortical** with strong **temporal lobe** predominance and frequent frontal involvement. (rahim2023clinicopathologicalfeaturesof pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)

Suggested UBERON terms (examples):
* **UBERON:0000955 (brain)**
* **UBERON:0001870 (cerebral cortex)**
* **UBERON:0002285 (temporal lobe)**
* **UBERON:0001871 (frontal lobe)**

### 7.3 Tissue/cell level and subcellular components
A frequent associated lesion is **focal cortical dysplasia** adjacent to tumor (dual pathology), implicating both tumor and surrounding cortex. (khalilov2024atypicalpresentationof pages 1-2)

## 8. Temporal Development

### 8.1 Onset
DNETs are described as occurring most often in childhood/adolescence; LEAT seizures commonly begin in early teens and frequently precede surgery by years. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, rahim2023clinicopathologicalfeaturesof pages 1-2)

### 8.2 Progression/course
Tumors are usually slow-growing/indolent with long seizure histories; malignant transformation is rare. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2, zhang2022longtermseizureoutcomes pages 1-2)

## 9. Inheritance and Population

### 9.1 Epidemiology
Quantitative epidemiology is limited but a large surgical cohort review reports DNET incidence around **0.03/100,000/year** (US estimate) and highlights that DNET constitutes a substantial fraction of LEAT diagnoses in epilepsy surgery series. (zhang2022longtermseizureoutcomes pages 1-2, iijima2024genotyperelevantneuroimagingfeatures pages 1-2)

### 9.2 Inheritance
DNET is primarily driven by **somatic** alterations, but rare familial predisposition via **germline FGFR1** alteration has been reported. (rivera2016germlineandsomatic pages 1-2)

## 10. Diagnostics

### 10.1 Clinical workup
Diagnosis is typically based on seizure history plus MRI and confirmatory histopathology; preoperative epilepsy workup commonly includes long-term video-EEG, with additional modalities (MEG, PET, invasive monitoring) when needed to define the epileptogenic zone. (zhang2022longtermseizureoutcomes pages 2-5, takayama2022ishippocampalresection pages 1-2)

### 10.2 Imaging
MRI is emphasized as the key modality; lesions are often cortical-based and may be classified into morphologic patterns (e.g., cystic-like, nodular-like, dysplastic-like). (zhang2022longtermseizureoutcomes pages 2-5, rahim2023clinicopathologicalfeaturesof pages 1-2)

A 2024 radiogenomic study in LEATs showed that certain imaging patterns can predict genotype with high accuracy, reporting imaging groups with “**93.8% sensitivity and 100% specificity to BRAF V600E**” (Group 1) and “**100% sensitivity and specificity for FGFR1 mutations**” (Group 2). (iijima2024genotyperelevantneuroimagingfeatures pages 1-2)

### 10.3 Histopathology
Characteristic pathology includes a multinodular architecture and “floating neurons” within a specific glioneuronal element; Ki-67 is typically very low. (rahim2023clinicopathologicalfeaturesof pages 1-2)

### 10.4 Molecular diagnostics (NGS, methylation)
Molecular profiling supports diagnosis and may clarify difficult cases, particularly in the DNT/MNGT/PLNTY spectrum where morphology overlaps; testing may include targeted DNA/RNA sequencing for FGFR1/BRAF/NTRK alterations and methylation arrays. (surrey2019genomicanalysisof pages 1-1, gatesman2024characterizationoflow‐grade pages 1-2)

A 2024 proof-of-concept study demonstrated feasibility of extracting tumor DNA from tissue adherent to **stereoelectroencephalography (sEEG) electrodes** and performing targeted sequencing and DNA methylation array analysis to aid classification. (gatesman2024characterizationoflow‐grade pages 1-2)

## 11. Outcome/Prognosis

### 11.1 Seizure outcomes after surgery (key quantitative data)
In a 63-patient DNET cohort (2008–2021), **49/63 (77.8%)** were seizure-free after surgery, with cumulative seizure recurrence-free rates **82.5% (2 years), 79.0% (5 years), 76.5% (10 years)**. (zhang2022longtermseizureoutcomes pages 1-2)

A systematic review of surgical series reported a median seizure-freedom rate of **86%** (IQR **77–93%**) and highlighted that gross-total resection is repeatedly associated with seizure freedom. (bonney2016reviewofseizure pages 4-5)

### 11.2 Prognostic factors
Predictors of better seizure outcomes include gross total resection and shorter epilepsy duration, while certain imaging patterns (e.g., dysplastic-like) and bilateral interictal epileptiform discharges may predict poorer seizure outcomes. (zhang2022longtermseizureoutcomes pages 1-2)

## 12. Treatment

### 12.1 Surgical and interventional (standard of care)
Maximal safe **surgical resection/lesionectomy** is widely considered the optimal approach to achieve seizure control and durable tumor control in LEATs, including DNET. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)

A hippocampus-sparing strategy may be appropriate in selected temporal-lobe LEATs with normal hippocampus: in a cohort of 32 temporal LEAT cases, **28/32 (87.5%)** achieved seizure freedom irrespective of hippocampal resection, and additional hippocampal resection negatively impacted verbal outcomes. (takayama2022ishippocampalresection pages 1-2)

**Real-world implementation example:** an observational clinical registry study evaluated intraoperative **fluorescein**-guided resection feasibility for ganglioglioma and DNET (NCT03970785), using surgical video review and postoperative MRI to assess fluorescence and extent of resection, with Engel-classification seizure outcomes. (NCT03970785 chunk 1)

### 12.2 Pharmacotherapy: antiseizure medications (ASMs)
DNET-associated epilepsy is frequently treated with ASMs but may be drug-resistant; consensus neuro-oncology practice avoids routine prophylactic ASM use in seizure-naïve patients. (rahim2023clinicopathologicalfeaturesof pages 1-2, avila2024braintumorrelatedepilepsy pages 10-11)

A 2024 Society for Neuro-Oncology consensus review states prophylactic ASM in seizure-naïve brain tumor patients lacks high-quality evidence, yet ~70% of neurosurgeons give a short postoperative course (commonly **levetiracetam for 7 days** after supratentorial craniotomy); meta-analysis showed reduced **early** postoperative seizures (RR **0.35**, 95% CI **0.13–0.95**) but not late seizures. (avila2024braintumorrelatedepilepsy pages 10-11)

Newton & Wojkowski (2024) summarize that seizures affect **>50%** of brain tumor patients overall and provide tumor-specific estimates (DNET ~**100%**), and similarly advise that **prophylactic AEDs are not recommended**; after a first verified seizure, consensus is to start ASM monotherapy, most often **levetiracetam** (with alternatives/add-ons including lacosamide, valproate, brivaracetam, lamotrigine, and perampanel). (newton2024antiepilepticstrategiesfor pages 1-3)

### 12.3 Targeted/experimental therapy
Because DNET biology is frequently MAPK-driven (FGFR1 alterations, RTK fusions), MEK-pathway targeting is being evaluated within broader pediatric/AYA low-grade glioma frameworks.

**Clinical trial example (MAPK-pathway therapy):** SJ901 (NCT04923126) evaluates **mirdametinib** (MEK1/2 inhibitor) in pediatric/AYA low-grade glioma and explicitly includes LEAT histologies such as **dysembryoplastic neuroepithelial tumor (DNET)** among eligible conditions; a separate protocol chunk specifies requirement for centrally reviewed **MAPK-pathway activation** evidence (including FGFR1/2/3 aberrations and other RAS/MAPK genes). (NCT04923126 chunk 2, NCT04923126 chunk 4)

### 12.4 Suggested MAXO (Medical Action Ontology) terms
Because MAXO codes were not present in the evidence corpus, the following are suggested as likely appropriate mappings (to be verified against MAXO):
* **Neurosurgical resection of brain tumor** (lesionectomy/gross total resection). (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)
* **Antiseizure medication therapy** (levetiracetam monotherapy; add-on therapy). (avila2024braintumorrelatedepilepsy pages 10-11)
* **Stereoelectroencephalography (SEEG) monitoring** / intracranial EEG evaluation. (gatesman2024characterizationoflow‐grade pages 1-2)
* **Intraoperative fluorescence-guided surgery**. (NCT03970785 chunk 1)
* **MEK inhibitor therapy** (mirdametinib clinical trial context). (NCT04923126 chunk 2)

## 13. Prevention
No primary-prevention interventions are established for DNET based on available evidence; secondary prevention in practice is largely **early recognition** of epileptogenic lesions and timely referral for epilepsy surgery evaluation when seizures are drug-resistant. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)

## 14. Other Species / Natural Disease
No naturally occurring DNET analogue in non-human species was identified in the retrieved corpus. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)

## 15. Model Organisms
A 2024 review on epilepsy-associated tumors notes improving animal modeling capacity for low-grade neuroepithelial tumors (LGNTs) with tools such as in utero electroporation to generate tumors with relevant genetic features; however, DNET-specific validated model organism details were not extracted from the retrieved evidence set. (rahim2023clinicopathologicalfeaturesof pages 6-7)

# Recent developments and expert analysis (2023–2024 emphasis)

## 2023–2024: classification and diagnostic modernization
Recent LEAT-focused reviews emphasize that DNET is a core LEAT entity and that the WHO CNS 2021 classification recognized additional epilepsy-associated tumor entities, increasing the importance of integrated diagnosis using histology plus molecular tools. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2, xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2)

A WHO-2021-based LEAT table explicitly lists DNET as **WHO grade 1** with characteristic genetic alteration **FGFR1**, supporting a molecularly anchored diagnostic approach rather than morphology alone. (xie2023lowgradeepilepsyassociatedneuroepithelial media 10d99c66)

## 2024: radiogenomics and minimally invasive molecular profiling
The 2024 radiogenomic study provides a practical framework suggesting that **preoperative neuroimaging patterns can predict genotype**, potentially enabling earlier precision planning (e.g., anticipating FGFR1 vs BRAF-driven lesions), and also indicates seizure outcomes may differ by genotype-associated imaging group. (iijima2024genotyperelevantneuroimagingfeatures pages 1-2)

A 2024 proof-of-concept sEEG-electrode approach suggests that neurosurgical epilepsy workflows can also become **molecular diagnostic workflows**, enabling targeted sequencing and methylation analysis from microscopic tissue without requiring a separate biopsy procedure. (gatesman2024characterizationoflow‐grade pages 1-2)

## 2024: consensus TRE management
The 2024 SNO consensus emphasizes evidence-based antiseizure management principles that generalize to DNET patients (especially perioperative decisions): no strong support for routine prophylaxis in seizure-naïve cases, frequent use of short postoperative levetiracetam courses, preference for monotherapy and non–enzyme-inducing ASMs, and escalation toward local therapies (surgery/irradiation) for drug-resistant seizures. (avila2024braintumorrelatedepilepsy pages 10-11)

# URLs and publication dates (selected key sources)
* Rahim et al. “Clinicopathological features of dysembryoplastic neuroepithelial tumor: a case series” (2023-08). https://doi.org/10.1186/s13256-023-04062-1 (rahim2023clinicopathologicalfeaturesof pages 1-2)
* Khalilov et al. “Atypical presentation of dysembryoplastic neuroepithelial tumor” (2024-10). https://doi.org/10.17816/acen.1126 (khalilov2024atypicalpresentationof pages 1-2)
* Iijima et al. “Genotype-relevant neuroimaging features in low-grade epilepsy-associated tumors” (2024-07). https://doi.org/10.3389/fneur.2024.1419104 (iijima2024genotyperelevantneuroimagingfeatures pages 1-2)
* Avila et al. SNO consensus “Brain tumor-related epilepsy management…” (2024-09). https://doi.org/10.1093/neuonc/noad154 (avila2024braintumorrelatedepilepsy pages 10-11)
* Newton & Wojkowski “Antiepileptic strategies…” (2024-02). https://doi.org/10.1007/s11864-024-01182-8 (newton2024antiepilepticstrategiesfor pages 1-3)
* ClinicalTrials.gov NCT03970785 (first posted 2019-06-03; study 2015–2018 cases): https://clinicaltrials.gov/study/NCT03970785 (NCT03970785 chunk 1)
* ClinicalTrials.gov NCT04923126 (first posted 2021-06-18): https://clinicaltrials.gov/study/NCT04923126 (NCT04923126 chunk 2)

# Evidence gaps and limitations (for knowledge-base curation)
* Formal external identifiers (MeSH, ICD-10/11, Orphanet, MONDO, OMIM) were not retrievable from the current evidence set; they should be added from dedicated ontology resources (not inferred). (rosemberg2023longtermepilepsyassociatedtumors pages 1-2)
* DNET-specific methylation subclass definitions and epigenetic prognostic biomarkers were not extractable from the retrieved texts; further targeted retrieval of DKFZ classifier class descriptions and DNET methylation studies would be needed. (gatesman2024characterizationoflow‐grade pages 1-2)
* Non-human natural disease and validated DNET-specific model organism details were not identified in the retrieved corpus. (rahim2023clinicopathologicalfeaturesof pages 6-7)

References

1. (rahim2023clinicopathologicalfeaturesof pages 1-2): Shabina Rahim, Nasir Ud Din, Jamshid Abdul-Ghafar, Qurratulain Chundriger, Poonum Khan, and Zubair Ahmad. Clinicopathological features of dysembryoplastic neuroepithelial tumor: a case series. Journal of Medical Case Reports, Aug 2023. URL: https://doi.org/10.1186/s13256-023-04062-1, doi:10.1186/s13256-023-04062-1. This article has 6 citations and is from a peer-reviewed journal.

2. (khalilov2024atypicalpresentationof pages 1-2): Varis S. Khalilov, Aleksey N. Kislyakov, Natalia A. Medvedeva, and Natalia S. Serova. Atypical presentation of dysembryoplastic neuroepithelial tumor. Annals of Clinical and Experimental Neurology, 18:109-115, Oct 2024. URL: https://doi.org/10.17816/acen.1126, doi:10.17816/acen.1126. This article has 0 citations.

3. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 1-2): Mingguo Xie, Xiongfei Wang, Zejun Duan, and Guoming Luan. Low-grade epilepsy-associated neuroepithelial tumors: tumor spectrum and diagnosis based on genetic alterations. Frontiers in Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnins.2022.1071314, doi:10.3389/fnins.2022.1071314. This article has 27 citations and is from a peer-reviewed journal.

4. (rosemberg2023longtermepilepsyassociatedtumors pages 1-2): Sergio Rosemberg. Long-term epilepsy associated-tumors (leats): what is new? Arquivos de Neuro-Psiquiatria, 81:1146-1151, Dec 2023. URL: https://doi.org/10.1055/s-0043-1777730, doi:10.1055/s-0043-1777730. This article has 10 citations and is from a peer-reviewed journal.

5. (xie2023lowgradeepilepsyassociatedneuroepithelial pages 2-3): Mingguo Xie, Xiongfei Wang, Zejun Duan, and Guoming Luan. Low-grade epilepsy-associated neuroepithelial tumors: tumor spectrum and diagnosis based on genetic alterations. Frontiers in Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnins.2022.1071314, doi:10.3389/fnins.2022.1071314. This article has 27 citations and is from a peer-reviewed journal.

6. (xie2023lowgradeepilepsyassociatedneuroepithelial media 10d99c66): Mingguo Xie, Xiongfei Wang, Zejun Duan, and Guoming Luan. Low-grade epilepsy-associated neuroepithelial tumors: tumor spectrum and diagnosis based on genetic alterations. Frontiers in Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnins.2022.1071314, doi:10.3389/fnins.2022.1071314. This article has 27 citations and is from a peer-reviewed journal.

7. (zhang2022longtermseizureoutcomes pages 1-2): Huawei Zhang, Yue Hu, Adilijiang Aihemaitiniyazi, Tiemin Li, Jian Zhou, Yuguang Guan, Xueling Qi, Xufei Zhang, Mengyang Wang, Changqing Liu, and Guoming Luan. Long-term seizure outcomes and predictors in patients with dysembryoplastic neuroepithelial tumors associated with epilepsy. Brain Sciences, 13:24, Dec 2022. URL: https://doi.org/10.3390/brainsci13010024, doi:10.3390/brainsci13010024. This article has 2 citations.

8. (pelissier2026pediatriclowgradeepilepsyassociated pages 1-3): Lindsey Pelissier, Asha Sarma, Joanne Rispoli, Stephen Little, Sumit Pruthi, and Alexandra Foust. Pediatric low-grade epilepsy-associated tumors (leats): neuroimaging review and genetics update. Pediatric Radiology, Jan 2026. URL: https://doi.org/10.1007/s00247-026-06519-z, doi:10.1007/s00247-026-06519-z. This article has 0 citations and is from a peer-reviewed journal.

9. (iijima2024genotyperelevantneuroimagingfeatures pages 1-2): Keiya Iijima, Hiroyuki Fujii, Fumio Suzuki, Kumiko Murayama, Yu-ichi Goto, Yuko Saito, Terunori Sano, Hiroyoshi Suzuki, Hajime Miyata, Yukio Kimura, Takuma Nakashima, Hiromichi Suzuki, Masaki Iwasaki, and Noriko Sato. Genotype-relevant neuroimaging features in low-grade epilepsy-associated tumors. Frontiers in Neurology, Jul 2024. URL: https://doi.org/10.3389/fneur.2024.1419104, doi:10.3389/fneur.2024.1419104. This article has 2 citations and is from a peer-reviewed journal.

10. (bonney2016reviewofseizure pages 4-5): Phillip A. Bonney, Lillian B. Boettcher, Andrew K. Conner, Chad A. Glenn, Robert G. Briggs, Joshua A. Santucci, Michael R. Bellew, James D. Battiste, and Michael E. Sughrue. Review of seizure outcomes after surgical resection of dysembryoplastic neuroepithelial tumors. Journal of Neuro-Oncology, 126:1-10, Oct 2016. URL: https://doi.org/10.1007/s11060-015-1961-4, doi:10.1007/s11060-015-1961-4. This article has 60 citations and is from a peer-reviewed journal.

11. (zhang2022longtermseizureoutcomes pages 2-5): Huawei Zhang, Yue Hu, Adilijiang Aihemaitiniyazi, Tiemin Li, Jian Zhou, Yuguang Guan, Xueling Qi, Xufei Zhang, Mengyang Wang, Changqing Liu, and Guoming Luan. Long-term seizure outcomes and predictors in patients with dysembryoplastic neuroepithelial tumors associated with epilepsy. Brain Sciences, 13:24, Dec 2022. URL: https://doi.org/10.3390/brainsci13010024, doi:10.3390/brainsci13010024. This article has 2 citations.

12. (rivera2016germlineandsomatic pages 1-2): Barbara Rivera, Tenzin Gayden, Jian Carrot-Zhang, Javad Nadaf, Talia Boshari, Damien Faury, Michele Zeinieh, Romeo Blanc, David L. Burk, Somayyeh Fahiminiya, Eric Bareke, Ulrich Schüller, Camelia M. Monoranu, Ronald Sträter, Kornelius Kerl, Thomas Niederstadt, Gerhard Kurlemann, Benjamin Ellezam, Zuzanna Michalak, Maria Thom, Paul J. Lockhart, Richard J. Leventer, Milou Ohm, Duncan MacGregor, David Jones, Jason Karamchandani, Celia M. T. Greenwood, Albert M. Berghuis, Susanne Bens, Reiner Siebert, Magdalena Zakrzewska, Pawel P. Liberski, Krzysztof Zakrzewski, Sanjay M. Sisodiya, Werner Paulus, Steffen Albrecht, Martin Hasselblatt, Nada Jabado, William D. Foulkes, and Jacek Majewski. Germline and somatic fgfr1 abnormalities in dysembryoplastic neuroepithelial tumors. Acta Neuropathologica, 131:847-863, Feb 2016. URL: https://doi.org/10.1007/s00401-016-1549-x, doi:10.1007/s00401-016-1549-x. This article has 214 citations and is from a highest quality peer-reviewed journal.

13. (lucas2020comprehensiveanalysisof pages 1-2): Calixto-Hope G. Lucas, Rohit Gupta, Pamela Doo, Julieann C. Lee, Cathryn R. Cadwell, Biswarathan Ramani, Jeffrey W. Hofmann, Emily A. Sloan, Bette K. Kleinschmidt-DeMasters, Han S. Lee, Matthew D. Wood, Marjorie Grafe, Donald Born, Hannes Vogel, Shahriar Salamat, Diane Puccetti, David Scharnhorst, David Samuel, Tabitha Cooney, Elaine Cham, Lee-way Jin, Ziad Khatib, Ossama Maher, Gabriel Chamyan, Carole Brathwaite, Serguei Bannykh, Sabine Mueller, Cassie N. Kline, Anu Banerjee, Alyssa Reddy, Jennie W. Taylor, Jennifer L. Clarke, Nancy Ann Oberheim Bush, Nicholas Butowski, Nalin Gupta, Kurtis I. Auguste, Peter P. Sun, Jarod L. Roland, Corey Raffel, Manish K. Aghi, Philip Theodosopoulos, Edward Chang, Shawn Hervey-Jumper, Joanna J. Phillips, Melike Pekmezci, Andrew W. Bollen, Tarik Tihan, Susan Chang, Mitchel S. Berger, Arie Perry, and David A. Solomon. Comprehensive analysis of diverse low-grade neuroepithelial tumors with fgfr1 alterations reveals a distinct molecular signature of rosette-forming glioneuronal tumor. Acta Neuropathologica Communications, Aug 2020. URL: https://doi.org/10.1186/s40478-020-01027-z, doi:10.1186/s40478-020-01027-z. This article has 71 citations and is from a peer-reviewed journal.

14. (jesus‐ribeiro2022thelandscapeof pages 6-7): Joana Jesus‐Ribeiro, Olinda Rebelo, Ilda Patrícia Ribeiro, Luís Miguel Pires, João Daniel Melo, Francisco Sales, Isabel Santana, António Freire, and Joana Barbosa Melo. The landscape of common genetic drivers and dna methylation in low‐grade (epilepsy‐associated) neuroepithelial tumors: a review. Neuropathology, 42:467-482, Jul 2022. URL: https://doi.org/10.1111/neup.12846, doi:10.1111/neup.12846. This article has 4 citations and is from a peer-reviewed journal.

15. (pages2022thegenomiclandscape pages 10-10): Mélanie Pagès, Marie‐Anne Debily, Frédéric Fina, David T. W. Jones, Raphael Saffroy, David Castel, Thomas Blauwblomme, Alice Métais, Marie Bourgeois, Emmanuèle Lechapt‐Zalcman, Arnault Tauziède‐Espariat, Felipe Andreiuolo, Fabrice Chrétien, Jacques Grill, Nathalie Boddaert, Dominique Figarella‐Branger, Rameen Beroukhim, and Pascale Varlet. The genomic landscape of dysembryoplastic neuroepithelial tumours and a comprehensive analysis of recurrent cases. Neuropathology and Applied Neurobiology, Aug 2022. URL: https://doi.org/10.1111/nan.12834, doi:10.1111/nan.12834. This article has 13 citations and is from a peer-reviewed journal.

16. (chen2022casereporta pages 1-2): Yanming Chen, Qing Zhu, Ye Wang, Xiaoxiao Dai, Ping Chen, Ailin Chen, Sujuan Zhou, Chungang Dai, Shengbin Zhao, Sheng Xiao, and Qing Lan. Case report: a novel lhfpl3::ntrk2 fusion in dysembryoplastic neuroepithelial tumor. Frontiers in Oncology, Dec 2022. URL: https://doi.org/10.3389/fonc.2022.1064817, doi:10.3389/fonc.2022.1064817. This article has 2 citations.

17. (gatesman2024characterizationoflow‐grade pages 1-2): Taylor A. Gatesman, Jasmine L. Hect, H. Westley Phillips, Brenden J. Johnson, Abigail I. Wald, Colleen McClung, Marina N. Nikiforova, John M. Skaugen, Ian F. Pollack, Taylor J. Abel, and Sameer Agnihotri. Characterization of low‐grade epilepsy‐associated tumor from implanted stereoelectroencephalography electrodes. Epilepsia Open, 9:409-416, Nov 2024. URL: https://doi.org/10.1002/epi4.12840, doi:10.1002/epi4.12840. This article has 11 citations and is from a peer-reviewed journal.

18. (xie2023lowgradeepilepsyassociatedneuroepithelial media f56d460d): Mingguo Xie, Xiongfei Wang, Zejun Duan, and Guoming Luan. Low-grade epilepsy-associated neuroepithelial tumors: tumor spectrum and diagnosis based on genetic alterations. Frontiers in Neuroscience, Jan 2023. URL: https://doi.org/10.3389/fnins.2022.1071314, doi:10.3389/fnins.2022.1071314. This article has 27 citations and is from a peer-reviewed journal.

19. (takayama2022ishippocampalresection pages 1-2): Yutaro Takayama, Naoki Ikegaya, Keiya Iijima, Yuiko Kimura, Kenzo Kosugi, Suguru Yokosako, Yuu Kaneko, Tetsuya Yamamoto, and Masaki Iwasaki. Is hippocampal resection necessary for low-grade epilepsy-associated tumors in the temporal lobe? Brain Sciences, 12:1381, Oct 2022. URL: https://doi.org/10.3390/brainsci12101381, doi:10.3390/brainsci12101381. This article has 6 citations.

20. (rahim2023clinicopathologicalfeaturesof pages 6-7): Shabina Rahim, Nasir Ud Din, Jamshid Abdul-Ghafar, Qurratulain Chundriger, Poonum Khan, and Zubair Ahmad. Clinicopathological features of dysembryoplastic neuroepithelial tumor: a case series. Journal of Medical Case Reports, Aug 2023. URL: https://doi.org/10.1186/s13256-023-04062-1, doi:10.1186/s13256-023-04062-1. This article has 6 citations and is from a peer-reviewed journal.

21. (NCT03970785 chunk 1):  Intraoperative Fluorescence of Ganglogliomas and Neuroepithelial Dysembryoplastic Tumors. Rennes University Hospital. 2018. ClinicalTrials.gov Identifier: NCT03970785

22. (rivera2016germlineandsomatic pages 12-15): Barbara Rivera, Tenzin Gayden, Jian Carrot-Zhang, Javad Nadaf, Talia Boshari, Damien Faury, Michele Zeinieh, Romeo Blanc, David L. Burk, Somayyeh Fahiminiya, Eric Bareke, Ulrich Schüller, Camelia M. Monoranu, Ronald Sträter, Kornelius Kerl, Thomas Niederstadt, Gerhard Kurlemann, Benjamin Ellezam, Zuzanna Michalak, Maria Thom, Paul J. Lockhart, Richard J. Leventer, Milou Ohm, Duncan MacGregor, David Jones, Jason Karamchandani, Celia M. T. Greenwood, Albert M. Berghuis, Susanne Bens, Reiner Siebert, Magdalena Zakrzewska, Pawel P. Liberski, Krzysztof Zakrzewski, Sanjay M. Sisodiya, Werner Paulus, Steffen Albrecht, Martin Hasselblatt, Nada Jabado, William D. Foulkes, and Jacek Majewski. Germline and somatic fgfr1 abnormalities in dysembryoplastic neuroepithelial tumors. Acta Neuropathologica, 131:847-863, Feb 2016. URL: https://doi.org/10.1007/s00401-016-1549-x, doi:10.1007/s00401-016-1549-x. This article has 214 citations and is from a highest quality peer-reviewed journal.

23. (avila2024braintumorrelatedepilepsy pages 10-11): Edward K Avila, Steven Tobochnik, Sara K Inati, Johan A F Koekkoek, Guy M McKhann, James J Riviello, Roberta Rudà, David Schiff, William O Tatum, Jessica W Templer, Michael Weller, and Patrick Y Wen. Brain tumor-related epilepsy management: a society for neuro-oncology (sno) consensus review on current management. Neuro-oncology, 26:7-24, Sep 2024. URL: https://doi.org/10.1093/neuonc/noad154, doi:10.1093/neuonc/noad154. This article has 106 citations and is from a domain leading peer-reviewed journal.

24. (surrey2019genomicanalysisof pages 1-1): Lea F Surrey, Payal Jain, Bo Zhang, Joshua Straka, Xiaonan Zhao, Brian N Harding, Adam C Resnick, Phillip B Storm, Anna Maria Buccoliero, Lorenzo Genitori, Marilyn M Li, Angela J Waanders, and Mariarita Santi. Genomic analysis of dysembryoplastic neuroepithelial tumor spectrum reveals a diversity of molecular alterations dysregulating the mapk and pi3k/mtor pathways. Journal of neuropathology and experimental neurology, 78:1100-1111, Dec 2019. URL: https://doi.org/10.1093/jnen/nlz101, doi:10.1093/jnen/nlz101. This article has 66 citations and is from a peer-reviewed journal.

25. (newton2024antiepilepticstrategiesfor pages 1-3): Herbert B. Newton and Jenna Wojkowski. Antiepileptic strategies for patients with primary and metastatic brain tumors. Current Treatment Options in Oncology, 25:389-403, Feb 2024. URL: https://doi.org/10.1007/s11864-024-01182-8, doi:10.1007/s11864-024-01182-8. This article has 20 citations and is from a peer-reviewed journal.

26. (NCT04923126 chunk 2):  SJ901: Evaluation of Mirdametinib in Children, Adolescents, and Young Adults With Low-Grade Glioma. St. Jude Children's Research Hospital. 2021. ClinicalTrials.gov Identifier: NCT04923126

27. (NCT04923126 chunk 4):  SJ901: Evaluation of Mirdametinib in Children, Adolescents, and Young Adults With Low-Grade Glioma. St. Jude Children's Research Hospital. 2021. ClinicalTrials.gov Identifier: NCT04923126