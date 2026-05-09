---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T21:37:00.787549'
end_time: '2026-05-04T21:47:57.572108'
duration_seconds: 656.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Allergic Cutaneous Vasculitis
  mondo_id: ''
  category: Immune-Mediated
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Allergic Cutaneous Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Immune-Mediated

## Research Objectives

Please provide a comprehensive research report on **Allergic Cutaneous Vasculitis** covering all of the
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
- **Disease Name:** Allergic Cutaneous Vasculitis
- **MONDO ID:**  (if available)
- **Category:** Immune-Mediated

## Research Objectives

Please provide a comprehensive research report on **Allergic Cutaneous Vasculitis** covering all of the
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


# Comprehensive Research Report: Allergic Cutaneous Vasculitis (ACV)

**Scope note (terminology):** “Allergic cutaneous vasculitis” is commonly used clinically to refer to an acquired, usually immune-complex–mediated **cutaneous small-vessel vasculitis (CSVV)**, which is frequently synonymous with **cutaneous leukocytoclastic vasculitis (LCV)** and historically overlaps with the term **hypersensitivity vasculitis**. Contemporary nomenclature (Chapel Hill + dermatologic addendum) prefers “CSVV” and reserves “single-organ cutaneous vasculitis” for skin-limited forms after exclusion of systemic disease. (micheletti2023cutaneoussmallvessel pages 1-2)

**Key recent sources prioritized:**
- Micheletti RG. *Cutaneous Small Vessel Vasculitis: A Practical Guide to Diagnosis and Management.* **Am J Clin Dermatol** (published online 2022; issue date **Oct 2023**). https://doi.org/10.1007/s40257-022-00736-6 (micheletti2023cutaneoussmallvessel pages 1-2, micheletti2023cutaneoussmallvessel pages 5-6)
- Cassisa A, Cima L. *Cutaneous vasculitis: insights into pathogenesis and histopathological features.* **Pathologica** (**Apr 2024**). https://doi.org/10.32074/1591-951x-985 (cassisa2024cutaneousvasculitisinsights pages 1-2)
- Sunderkötter C, et al. *Pathophysiology and clinical manifestations of immune complex vasculitides.* **Frontiers in Medicine** (**Mar 2023**). https://doi.org/10.3389/fmed.2023.1103065 (sunderkotter2023pathophysiologyandclinical pages 1-2)

---

## 1. Disease Information

### 1.1 What is the disease? (concise overview)
ACV/CSVV/LCV is a **small-vessel vasculitis of the skin** in which inflammation primarily targets superficial dermal post-capillary venules, producing **palpable purpura** and related purpuric/urticarial lesions, most often on dependent areas (lower legs). It is typically **immune-complex–mediated with complement activation**, and may be idiopathic or triggered by drugs/infections; it can also reflect systemic vasculitis or systemic disease and thus requires evaluation for extracutaneous involvement. (micheletti2023cutaneoussmallvessel pages 1-2, micheletti2023cutaneoussmallvessel pages 2-5)

### 1.2 Key identifiers (ontology / coding)
- **MeSH:** *Vasculitis, Leukocytoclastic, Cutaneous* — **D018366** (NCT02550080 chunk 2)
- **ICD-10(-CM) codes used in large EHR research for LCV/cutaneous LCV:** **D69.0** and **L95.8** (takatu2017clinicopathologiccorrelationof pages 1-2)
- **MONDO / Orphanet / OMIM:** Not found in the retrieved sources; ACV/CSVV is generally treated as an *acquired clinical-pathologic syndrome* rather than a single-gene disorder in the dermatology/rheumatology literature summarized here. (micheletti2023cutaneoussmallvessel pages 1-2)

### 1.3 Common synonyms / alternative names
- Cutaneous small-vessel vasculitis (CSVV)
- Cutaneous leukocytoclastic vasculitis (LCV)
- Leukocytoclastic vasculitis
- Hypersensitivity vasculitis
- Cutaneous leukocytoclastic angiitis (micheletti2023cutaneoussmallvessel pages 1-2)

### 1.4 Evidence sources
The information summarized here is derived from **aggregated disease-level resources** (reviews/guides) plus **clinical cohorts/case series**, not from a single EHR system except where explicitly noted (e.g., DIF cohort; population estimates; EHR database cohort). (micheletti2023cutaneoussmallvessel pages 5-6, fraticelli2021diagnosisandmanagement pages 1-2, takatu2017clinicopathologiccorrelationof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
The prevailing model is **immune complex deposition in small cutaneous vessels** with **complement activation** and **neutrophil recruitment/activation**, leading to vessel wall injury (fibrinoid necrosis), leukocytoclasia, and red blood cell extravasation (purpura). (micheletti2023cutaneoussmallvessel pages 1-2, fadel2025healthliteracyand pages 3-5)

### 2.2 Risk factors (clinical triggers and associated conditions)
**Frequently reported triggers/associations include:**
- **Medications** (antibiotics, including **beta-lactams**, among common triggers) (micheletti2023cutaneoussmallvessel pages 2-5)
- **Infections** (e.g., **upper respiratory infections**, **Group A Streptococcus**, **hepatitis C**) (micheletti2023cutaneoussmallvessel pages 2-5)
- **Systemic inflammatory/autoimmune disease** (connective tissue diseases; ANCA-associated vasculitis; cryoglobulinemia; IgA vasculitis; urticarial vasculitis) (fraticelli2021diagnosisandmanagement pages 1-2)
- **Malignancy (less common)**: LCV may rarely be a paraneoplastic clue; reviews emphasize malignancy as a possible association that should be considered based on clinical context. (micheletti2023cutaneoussmallvessel pages 2-5, fraticelli2021diagnosisandmanagement pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
Not well defined for ACV/CSVV specifically in the retrieved sources. Mechanistically, type III immune complex reactions are driven by **antigen exposure** (infection/drug antigen) leading to immune-complex formation and complement activation. (fadel2025healthliteracyand pages 3-5, sunderkotter2023pathophysiologyandclinical pages 2-3)

---

## 3. Phenotypes

### 3.1 Core cutaneous phenotypes (with HPO suggestions)
**Common skin manifestations** (adult and pediatric literature overlap, but this report emphasizes adult CSVV/LCV):
- **Palpable purpura** (dependent distribution, often lower legs) — suggested HPO: **Purpura (HP:0000979)** (micheletti2023cutaneoussmallvessel pages 1-2)
- **Petechiae / non-blanching purpura** — suggested HPO: **Petechiae (HP:0000967)** (micheletti2023cutaneoussmallvessel pages 2-5)
- **Urticarial papules / wheals** (esp. in urticarial vasculitis overlap) — suggested HPO: **Urticaria (HP:0001025)** (rothermel2024managingurticarialvasculitis pages 1-2)
- **Hemorrhagic vesicles/pustules** (subset) — suggested HPO: **Vesicle (HP:0001598)** / **Pustule (HP:0000966)** (micheletti2023cutaneoussmallvessel pages 1-2)
- **Ulceration/necrosis/retiform purpura** may indicate more severe disease or larger-vessel involvement and triggers expanded systemic evaluation — suggested HPO: **Skin ulcer (HP:0001059)** / **Skin necrosis (HP:0025478)** (micheletti2023cutaneoussmallvessel pages 2-5)

**Extracutaneous symptoms (when present):**
- **Arthralgia** is commonly reported among extracutaneous symptoms — suggested HPO: **Arthralgia (HP:0002829)** (escamilla2024vasculitisleucocitoclásticaasociada pages 10-15)

### 3.2 Phenotype characteristics
- **Onset pattern:** commonly **acute** episodes; many are self-limited over weeks (micheletti2023cutaneoussmallvessel pages 2-5)
- **Frequency/severity example (clinical cohort):** in a 75-patient series, lesions affected only lower limbs in **80%** and presented as palpable purpura in **64%**. (micheletti2023cutaneoussmallvessel pages 2-5)

### 3.3 Quality of life impact
Recent guidance emphasizes that cutaneous vasculitis can significantly impact patients and that management can be challenging despite skin-limited disease. (micheletti2023cutaneoussmallvessel pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / pathogenic variants
**Not established for typical ACV/CSVV**: the retrieved clinical guidance treats CSVV/LCV largely as an **acquired immune-mediated** syndrome rather than a monogenic disorder. (micheletti2023cutaneoussmallvessel pages 1-2, fraticelli2021diagnosisandmanagement pages 1-2)

### 4.2 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in the retrieved sources for ACV/CSVV.

**Important “genetic mimic” note (clinical differential):** monogenic autoinflammatory diseases can present with cutaneous vasculitis phenotypes in other contexts, but specific gene-level evidence for ACV/CSVV was not extracted from the retrieved texts in this run. (fraticelli2021diagnosisandmanagement pages 1-2)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
No specific pollutant/toxin/lifestyle risks were identified in the retrieved sources, beyond **exposure to triggering antigens** such as medications and infections. (micheletti2023cutaneoussmallvessel pages 2-5)

### 5.2 Infectious agents
Upper respiratory infections, Group A Streptococcus, and hepatitis C are highlighted as common or notable triggers/associations in CSVV/LCV reviews. (micheletti2023cutaneoussmallvessel pages 2-5)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → lesion)
A widely used mechanistic chain for immune-complex (type III) cutaneous vasculitis is:
1) **Antigen exposure** → 2) **IgG formation and immune complex formation** → 3) **Immune complex deposition** → 4) **Classical complement cascade activation** (C3a/C5a generation) → 5) **mast cell degranulation and histamine release** → 6) **neutrophil recruitment and degranulation** → 7) **fibrinoid necrosis of vessel walls** and leukocytoclasia → 8) **RBC extravasation** causing non-blanching purpura. (fadel2025healthliteracyand pages 3-5)

### 6.2 Immune-complex vasculitis and NETosis (recent developments)
A 2023 synthesis of immune-complex vasculitides highlights polymorphonuclear neutrophil activation via Fc receptors and notes that in IgA vasculitis, **intravascular priming of neutrophils** can lead to **vessel-destructive NETosis** upon encountering deposited IgA at vessel walls, linking Fcα receptor biology to NET formation and vascular injury. (sunderkotter2023pathophysiologyandclinical pages 1-2)

A 2024 pathology-focused review emphasizes that newer insights (including **NETosis**) are increasingly integrated into understanding of vasculitis initiation and progression. (cassisa2024cutaneousvasculitisinsights pages 1-2)

### 6.3 Key cellular players (CL term suggestions)
- **Neutrophil** — suggested CL: **neutrophil (CL:0000775)** (sunderkotter2023pathophysiologyandclinical pages 1-2)
- **Endothelial cell** — suggested CL: **endothelial cell (CL:0000115)** (cassisa2024cutaneousvasculitisinsights pages 1-2)
- **Mast cell** — suggested CL: **mast cell (CL:0000097)** (fadel2025healthliteracyand pages 3-5)

### 6.4 Key pathways and processes (GO term suggestions)
- **Immune complex clearance / immune complex deposition** — suggested GO: **immune complex clearance (GO:0006956)** (sunderkotter2023pathophysiologyandclinical pages 2-3)
- **Complement activation (classical pathway)** — suggested GO: **classical complement activation (GO:0006958)** (fadel2025healthliteracyand pages 3-5)
- **Neutrophil chemotaxis and activation** — suggested GO: **neutrophil chemotaxis (GO:0030593)** (fadel2025healthliteracyand pages 3-5)
- **NET formation** — suggested GO: **neutrophil extracellular trap formation (GO:0036416)** (sunderkotter2023pathophysiologyandclinical pages 1-2)

### 6.5 Tissue damage mechanism
Histopathologic injury includes **fibrinoid necrosis** of small vessels with neutrophilic infiltration and nuclear debris (leukocytoclasia), which can be visualized on H&E sections. (escamilla2024vasculitisleucocitoclásticaasociada pages 10-15, cassisa2024cutaneousvasculitisinsights media af7d9316)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Primary: **skin** (dermis), especially **post-capillary venules** in superficial dermis (escamilla2024vasculitisleucocitoclásticaasociada pages 10-15, sunderkotter2023pathophysiologyandclinical pages 2-3)
- Secondary involvement to screen for: **kidney** (occult glomerulonephritis), joints, peripheral nerves depending on systemic features and subtype (fraticelli2021diagnosisandmanagement pages 1-2, micheletti2023cutaneoussmallvessel pages 2-5)

**UBERON suggestions:**
- Skin — **UBERON:0002097**
- Dermis — **UBERON:0002067**

---

## 8. Temporal Development

### 8.1 Onset and course
- Often **acute** with episodes that may be self-limited. Many cases resolve within **~3–4 weeks**. (micheletti2023cutaneoussmallvessel pages 2-5)
- Chronicity: a subset becomes **chronic or recurrent**; one guide cites ~**10%** chronic/relapsing disease. (micheletti2023cutaneoussmallvessel pages 6-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recently summarized statistics)
A highly cited clinical review reports wide variability in reported epidemiology for biopsy-proven cutaneous LCV:
- **Incidence:** **15–38 per million/year**
- **Prevalence:** **2.7–29.7 per million**
- A U.S. population study estimate for biopsy-proven LCV: **4.5 per 100,000 person-years** (95% CI 3.5–5.4) (fraticelli2021diagnosisandmanagement pages 1-2)

### 9.2 Demographics
Cutaneous LCV affects both sexes and all ages; some studies report a slight male/older-age predilection. (fraticelli2021diagnosisandmanagement pages 2-3)

### 9.3 Inheritance
No Mendelian inheritance pattern is established for typical ACV/CSVV in the retrieved sources (acquired immune-mediated condition). (micheletti2023cutaneoussmallvessel pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical approach (real-world implementation)
A recent practical guide emphasizes **history, exam, and review of systems** to identify triggers and to distinguish skin-limited disease from systemic vasculitis. A **targeted stepwise workup** is favored, with broad testing reserved for systemic features. (micheletti2023cutaneoussmallvessel pages 2-5, micheletti2023cutaneoussmallvessel pages 5-6)

### 10.2 Laboratory tests (core and extended)
**Minimal baseline tests for straightforward, skin-limited presentations (per dermatology guidance):**
- CBC
- Basic metabolic panel / renal function
- Urinalysis with microscopic review (screen for occult glomerulonephritis) (micheletti2023cutaneoussmallvessel pages 2-5)

**Commonly used broader evaluation (particularly if systemic involvement is suspected):**
- Platelet count
- Hepatitis B and C serologies
- ANA and ANCA
- Complement fractions
- IgA staining in biopsy specimens (fraticelli2021diagnosisandmanagement pages 1-2)

### 10.3 Biopsy and immunopathology
- **Timing:** biopsy ideally from a lesion **~24–48 hours** old / **1–2 days** old to optimize diagnostic yield (micheletti2023cutaneoussmallvessel pages 1-2)
- **Histology:** neutrophilic inflammation, **leukocytoclasia**, **fibrinoid necrosis**, and RBC extravasation (escamilla2024vasculitisleucocitoclásticaasociada pages 10-15, fraticelli2021diagnosisandmanagement pages 1-2)
- **Direct immunofluorescence (DIF):** recommended; in a large cohort, DIF was positive in **70.21%** and systemic involvement occurred in **12.5%** (takatu2017clinicopathologiccorrelationof pages 1-2). DIF is reported to be ~**80% sensitive/specific** for IgA vasculitis in a dermatology guide. (micheletti2023cutaneoussmallvessel pages 1-2)

### 10.4 Differential diagnosis
Key systemic associations to consider include ANCA-associated vasculitis, connective tissue diseases (e.g., SLE), cryoglobulinemic vasculitis, IgA vasculitis, and hypocomplementemic urticarial vasculitis. (fraticelli2021diagnosisandmanagement pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Overall prognosis
A practical dermatology guide reports a generally favorable course:
- ~**90%** resolve spontaneously within weeks to months
- ~**10%** develop a chronic/relapsing course that may last months to years (micheletti2023cutaneoussmallvessel pages 6-7)

### 11.2 Prognostic factors (clinical)
Prognosis depends strongly on whether disease is **skin-limited** versus reflecting a **systemic vasculitis/systemic disease**, emphasizing the importance of accurate classification and systemic screening. (micheletti2023cutaneoussmallvessel pages 6-7)

---

## 12. Treatment

### 12.1 Treatment principles (current practice)
- **First-line for most acute skin-limited episodes:** supportive measures (rest, elevation, compression), topical steroids/NSAIDs if appropriate, plus **removal of the trigger** (stop offending drug; treat infection). (micheletti2023cutaneoussmallvessel pages 2-5, escamilla2024vasculitisleucocitoclásticaasociada pages 10-15)
- **Avoid aggressive long-term immunosuppression** for purely skin-limited disease; reserve systemic therapy for severe, intractable, or recurrent cases. (micheletti2023cutaneoussmallvessel pages 2-5, micheletti2023cutaneoussmallvessel pages 5-6)

### 12.2 Common systemic therapies and dosing (real-world implementation)
From a 2023 practical guide:
- **Colchicine:** **0.6 mg twice daily**
- **Dapsone:** **100–150 mg/day** (screen for **G6PD deficiency**)
- **Azathioprine:** target **2 mg/kg/day** (screen **TPMT**) (micheletti2023cutaneoussmallvessel pages 5-6)

**Oral glucocorticoids** may be used for severe symptomatic disease (example regimens):
- **Prednisone ~0.5–1 mg/kg/day** or **40–60 mg/day**, tapered over **3–4 weeks**; not appropriate as a long-term plan due to toxicity. (micheletti2023cutaneoussmallvessel pages 5-6, micheletti2023cutaneoussmallvessel pages 6-7)

**Escalation options** for refractory disease include mycophenolate mofetil, methotrexate, hydroxychloroquine, pentoxifylline, and (for severe refractory cases) rituximab, infliximab, IVIG, cyclosporine, cyclophosphamide. (micheletti2023cutaneoussmallvessel pages 5-6, micheletti2023cutaneoussmallvessel pages 6-7)

### 12.3 Trials / experimental evidence
- **ARAMIS trial (ongoing at the time of the guide):** international randomized trial for colchicine in CSVV/LCV (ClinicalTrials.gov identifier **NCT02939573**) was cited as ongoing in the 2023 guide. (micheletti2023cutaneoussmallvessel pages 5-6)
- Additional vasculitis-related observational/interventional trials relevant to immune-complex vasculitis phenotyping and relapse prevention include studies comparing **IgA-positive vs IgA-negative immune complex vasculitis (NCT01815190)** and adult IgA vasculitis relapse prevention with colchicine (**NCT04008316**). (NCT01815190 chunk 1, NCT04008316 chunk 2)

**MAXO suggestions (treatment actions):**
- Systemic glucocorticoid therapy — **MAXO:0000058**
- Colchicine therapy — **MAXO:0000745** (drug-based action; placeholder mapping)
- Dapsone therapy — **MAXO:0000746** (placeholder mapping)
- Skin biopsy — **MAXO:0000476** (diagnostic action; placeholder mapping)

*Note:* MAXO IDs above are suggested conceptually; confirm exact MAXO mappings in ontology tooling.

---

## 13. Prevention

### 13.1 Primary prevention
Primary prevention is not well defined for idiopathic CSVV. Practical prevention focuses on **avoiding re-exposure to known culprit drugs** and **managing infections** that have triggered prior episodes. (micheletti2023cutaneoussmallvessel pages 2-5, fraticelli2021diagnosisandmanagement pages 1-2)

### 13.2 Secondary/tertiary prevention
- Early recognition of systemic involvement via urinalysis/renal screening and review of systems (micheletti2023cutaneoussmallvessel pages 2-5)
- Relapse prevention strategies are under study (e.g., colchicine trials). (micheletti2023cutaneoussmallvessel pages 5-6)

---

## 14. Other Species / Natural Disease
No veterinary/natural disease evidence was identified in the retrieved sources.

---

## 15. Model Organisms
No model organism systems specific to ACV/CSVV were identified in the retrieved sources.

---

## Key figure (histopathology)
Representative histopathologic appearances of leukocytoclastic vasculitis (neutrophils infiltrating vessel wall with fibrin rim and leukocytoclasia/nuclear dust) are shown in a recent pathology review. (cassisa2024cutaneousvasculitisinsights media af7d9316)

---

## Condensed knowledge-base table
| Preferred term + synonyms | Key identifiers / codes | Core clinical phenotype | Recommended initial labs | Biopsy / DIF key points | Common triggers / associations | Epidemiology / prognosis | Treatment (first-line → escalation; typical doses) |
|---|---|---|---|---|---|---|---|
| **Preferred term:** cutaneous small-vessel vasculitis (CSVV), often used interchangeably with **cutaneous leukocytoclastic vasculitis / leukocytoclastic vasculitis**; older names include **hypersensitivity vasculitis** and **cutaneous leukocytoclastic angiitis**. "Allergic cutaneous vasculitis" is best mapped to this acquired, usually immune-complex-mediated skin-limited vasculitis category. (micheletti2023cutaneoussmallvessel pages 1-2, micheletti2023cutaneoussmallvessel pages 6-7) | **MeSH:** *Vasculitis, Leukocytoclastic, Cutaneous* **D018366**. **ICD-10-CM codes used in recent database work:** **D69.0** and **L95.8** for LCV/cutaneous LCV. Formal OMIM/Orphanet/MONDO identifiers were not identified in the retrieved sources. (NCT02550080 chunk 2, NCT01815190 chunk 1) | Typical lesions are **palpable purpura**, petechiae, urticarial papules, hemorrhagic vesicles/pustules, favoring **dependent areas/lower legs**; non-blanching purpura reflects RBC extravasation, and arthralgia is a common extracutaneous symptom. Lower-limb-only involvement was 80% in one 75-patient series; palpable purpura occurred in 64%. (micheletti2023cutaneoussmallvessel pages 1-2, micheletti2023cutaneoussmallvessel pages 2-5) | For straightforward skin-limited disease with negative review of systems, suggested baseline tests are **CBC**, **basic metabolic panel/renal function**, and **urinalysis with microscopy** to screen for occult glomerulonephritis; broader workup may include **ANA, ANCA, hepatitis B/C serologies, complement fractions, platelet count**, and **IgA staining** when indicated. (micheletti2023cutaneoussmallvessel pages 2-5, fraticelli2021diagnosisandmanagement pages 1-2, fadel2025healthliteracyand pages 3-5) | Skin biopsy is central: best from a **new lesion (ideally 24–48 h old; ~1–2 days old)**. Histology shows **neutrophilic small-vessel inflammation, leukocytoclasia, fibrinoid necrosis, and erythrocyte extravasation**. **DIF** is recommended; one cohort found positivity in **70.21%**, and Micheletti notes DIF is ~**80% sensitive/specific for IgA vasculitis**. (micheletti2023cutaneoussmallvessel pages 1-2, takatu2017clinicopathologiccorrelationof pages 1-2, escamilla2024vasculitisleucocitoclásticaasociada pages 10-15) | Often idiopathic, but common triggers include **medications** (especially **beta-lactams/other antibiotics**), **infections** (notably **upper respiratory infections**, **Group A Streptococcus**, **hepatitis C**), and less often **connective tissue disease**, **cryoglobulinemia**, or **malignancy**. In one retrospective series, the most common secondary causes were **infections and drugs**. (micheletti2023cutaneoussmallvessel pages 2-5, fraticelli2021diagnosisandmanagement pages 1-2, fraticelli2021diagnosisandmanagement pages 2-3) | Reported incidence ranges **15–38 cases per million/year** with prevalence **2.7–29.7 per million**; a U.S. population study estimated **4.5 per 100,000 person-years** for biopsy-proven LCV. Most episodes are self-limited: **3–4 weeks** for many cases; about **90%** resolve spontaneously within weeks to months, while about **10%** become chronic/relapsing. (fraticelli2021diagnosisandmanagement pages 2-3, fraticelli2021diagnosisandmanagement pages 1-2, micheletti2023cutaneoussmallvessel pages 6-7, micheletti2023cutaneoussmallvessel pages 5-6) | **Supportive/trigger removal first:** rest, leg elevation, compression, topical steroids/NSAIDs where appropriate; stop culprit drug/treat infection. For symptomatic or recurrent disease: **colchicine 0.6 mg BID**, **dapsone 100–150 mg/day** (check **G6PD**), **azathioprine target 2 mg/kg/day** (check **TPMT**), **prednisone ~0.5–1 mg/kg/day** or **40–60 mg/day** tapered over **3–4 weeks**. Escalation for refractory/severe disease: **mycophenolate 2–3 g/day, methotrexate 15–25 mg/week, hydroxychloroquine 200–400 mg/day, pentoxifylline 400 mg TID**, and in severe refractory cases **rituximab, infliximab, IVIG, cyclosporine, cyclophosphamide**. (micheletti2023cutaneoussmallvessel pages 5-6, micheletti2023cutaneoussmallvessel pages 6-7, escamilla2024vasculitisleucocitoclásticaasociada pages 10-15, micheletti2023cutaneoussmallvessel pages 2-5) |


*Table: This table condenses the most useful disease-knowledge-base facts for allergic cutaneous vasculitis treated as cutaneous small-vessel/leukocytoclastic vasculitis. It captures nomenclature, identifiers, diagnostic workup, pathology, epidemiology, and practical treatment dosing in one place.*

---

## Direct abstract quotes (for key KB statements)
1) **Definition / histology:** “*Leukocytoclastic vasculitis (LCV) is a histopathologic description of a common form of small vessel vasculitis (SVV)… the inflammatory infiltrate is composed of neutrophils with fibrinoid necrosis and disintegration of nuclei into fragments (“leukocytoclasia”)*.” (Fraticelli 2021; abstract excerpt) (fraticelli2021diagnosisandmanagement pages 1-2)
2) **Mechanism / associations / workup:** “*Several medications can cause LCV, as well as infections, or malignancy… platelet count, renal function and urinalysis… hepatitis B and C… autoantibodies (anti-nuclear… anti-neutrophil cytoplasmic antibodies), complement fractions and IgA staining in biopsy specimens are part of the usual workout of LCV.*” (Fraticelli 2021; abstract excerpt) (fraticelli2021diagnosisandmanagement pages 1-2)
3) **Type III hypersensitivity:** “*Serum sickness and CV fulfill the criteria of a type III hypersensitivity immune reaction…*” (Sunderkötter 2023; abstract excerpt) (sunderkotter2023pathophysiologyandclinical pages 1-2)

---

# Evidence gaps / limitations
- **MONDO/Orphanet/OMIM identifiers** were not present in the retrieved document set and thus are not reported here.
- **High-quality randomized trial evidence** for CSVV/LCV treatments remains limited; recent guides emphasize reliance on case series and expert opinion with ongoing trial efforts (e.g., colchicine). (micheletti2023cutaneoussmallvessel pages 5-6)


References

1. (micheletti2023cutaneoussmallvessel pages 1-2): Robert G. Micheletti. Cutaneous small vessel vasculitis: a practical guide to diagnosis and management. American Journal of Clinical Dermatology, 24:89-95, Oct 2023. URL: https://doi.org/10.1007/s40257-022-00736-6, doi:10.1007/s40257-022-00736-6. This article has 15 citations and is from a peer-reviewed journal.

2. (micheletti2023cutaneoussmallvessel pages 5-6): Robert G. Micheletti. Cutaneous small vessel vasculitis: a practical guide to diagnosis and management. American Journal of Clinical Dermatology, 24:89-95, Oct 2023. URL: https://doi.org/10.1007/s40257-022-00736-6, doi:10.1007/s40257-022-00736-6. This article has 15 citations and is from a peer-reviewed journal.

3. (cassisa2024cutaneousvasculitisinsights pages 1-2): Angelo Cassisa and Luca Cima. Cutaneous vasculitis: insights into pathogenesis and histopathological features. Pathologica, 116:119-133, Apr 2024. URL: https://doi.org/10.32074/1591-951x-985, doi:10.32074/1591-951x-985. This article has 11 citations.

4. (sunderkotter2023pathophysiologyandclinical pages 1-2): Cord Sunderkötter, Linda Golle, Evangéline Pillebout, and Christiane Michl. Pathophysiology and clinical manifestations of immune complex vasculitides. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1103065, doi:10.3389/fmed.2023.1103065. This article has 27 citations.

5. (micheletti2023cutaneoussmallvessel pages 2-5): Robert G. Micheletti. Cutaneous small vessel vasculitis: a practical guide to diagnosis and management. American Journal of Clinical Dermatology, 24:89-95, Oct 2023. URL: https://doi.org/10.1007/s40257-022-00736-6, doi:10.1007/s40257-022-00736-6. This article has 15 citations and is from a peer-reviewed journal.

6. (NCT02550080 chunk 2):  Clinical Utility Of Genetic Screening For HLA-B*1301, On Susceptibility To Dapsone Hypersensitivity Syndrome. Shandong Provincial Institute of Dermatology and Venereology. 2015. ClinicalTrials.gov Identifier: NCT02550080

7. (takatu2017clinicopathologiccorrelationof pages 1-2): Caroline Maris Takatu, Antonio Pedro Ribeiro Heringer, Valéria Aoki, Neusa Yuriko Sakai Valente, Paula Cristina de Faria Sanchez, Jozélio Freire de Carvalho, and Paulo Ricardo Criado. Clinicopathologic correlation of 282 leukocytoclastic vasculitis cases in a tertiary hospital: a focus on direct immunofluorescence findings at the blood vessel wall. Immunologic Research, 65:395-401, Feb 2017. URL: https://doi.org/10.1007/s12026-016-8850-6, doi:10.1007/s12026-016-8850-6. This article has 33 citations and is from a peer-reviewed journal.

8. (fraticelli2021diagnosisandmanagement pages 1-2): Paolo Fraticelli, Devis Benfaremo, and Armando Gabrielli. Diagnosis and management of leukocytoclastic vasculitis. Internal and Emergency Medicine, 16:831-841, Mar 2021. URL: https://doi.org/10.1007/s11739-021-02688-x, doi:10.1007/s11739-021-02688-x. This article has 215 citations and is from a peer-reviewed journal.

9. (fadel2025healthliteracyand pages 3-5): Lynn Fadel, Sara Shah, Jehad Feras AlSamhori, Justin Ma, Ahmed Nadeem-Tariq, Janae Rasmussen, Kiratpreet Sraa, and Kelly Frasier. Health literacy and treatment adherence in patients with cutaneous-limited vasculitis and musculoskeletal pain. ARC Journal of Dermatology, 8:21-37, Jan 2025. URL: https://doi.org/10.20431/2456-0022.0807003, doi:10.20431/2456-0022.0807003. This article has 0 citations.

10. (sunderkotter2023pathophysiologyandclinical pages 2-3): Cord Sunderkötter, Linda Golle, Evangéline Pillebout, and Christiane Michl. Pathophysiology and clinical manifestations of immune complex vasculitides. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1103065, doi:10.3389/fmed.2023.1103065. This article has 27 citations.

11. (rothermel2024managingurticarialvasculitis pages 1-2): Nikolai Dario Rothermel, Carolina Vera Ayala, Margarida Gonçalo, Jie Shen Fok, Leonie Shirin Herzog, Emek Kocatürk, Sophia Neisinger, Manuel P. Pereira, Indrashis Podder, Polina Pyatilova, Aiste Ramanauskaite, Melba Munoz, Karoline Krause, Marcus Maurer, Hanna Bonnekoh, and Pavel Kolkhir. Managing urticarial vasculitis: a clinical decision-making algorithm based on expert consensus. American Journal of Clinical Dermatology, 26:61-75, Nov 2024. URL: https://doi.org/10.1007/s40257-024-00902-y, doi:10.1007/s40257-024-00902-y. This article has 14 citations and is from a peer-reviewed journal.

12. (escamilla2024vasculitisleucocitoclásticaasociada pages 10-15): Diana Verónica Romero Escamilla, Mariam Hussein Jumaan Torres, and Julieta Peralta y Serna. Vasculitis leucocitoclástica asociada a infección: a proposito de un caso y revisión de literatura. Revista Científica de Salud y Desarrollo Humano, 5:177-190, Oct 2024. URL: https://doi.org/10.61368/r.s.d.h.v5i4.345, doi:10.61368/r.s.d.h.v5i4.345. This article has 2 citations.

13. (cassisa2024cutaneousvasculitisinsights media af7d9316): Angelo Cassisa and Luca Cima. Cutaneous vasculitis: insights into pathogenesis and histopathological features. Pathologica, 116:119-133, Apr 2024. URL: https://doi.org/10.32074/1591-951x-985, doi:10.32074/1591-951x-985. This article has 11 citations.

14. (micheletti2023cutaneoussmallvessel pages 6-7): Robert G. Micheletti. Cutaneous small vessel vasculitis: a practical guide to diagnosis and management. American Journal of Clinical Dermatology, 24:89-95, Oct 2023. URL: https://doi.org/10.1007/s40257-022-00736-6, doi:10.1007/s40257-022-00736-6. This article has 15 citations and is from a peer-reviewed journal.

15. (fraticelli2021diagnosisandmanagement pages 2-3): Paolo Fraticelli, Devis Benfaremo, and Armando Gabrielli. Diagnosis and management of leukocytoclastic vasculitis. Internal and Emergency Medicine, 16:831-841, Mar 2021. URL: https://doi.org/10.1007/s11739-021-02688-x, doi:10.1007/s11739-021-02688-x. This article has 215 citations and is from a peer-reviewed journal.

16. (NCT01815190 chunk 1): Cord Sunderkötter. IgA-positive Versus IgA-negative Immune Complex Vasculitis. University Hospital Muenster. 2011. ClinicalTrials.gov Identifier: NCT01815190

17. (NCT04008316 chunk 2):  Efficacy of Colchicine to Prevent Skin Relapses in Adult's IgA Vasculitis. Assistance Publique - Hôpitaux de Paris. 2019. ClinicalTrials.gov Identifier: NCT04008316
