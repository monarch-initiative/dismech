---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:10:03.644748'
end_time: '2026-05-09T10:32:00.013707'
duration_seconds: 1316.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alveolar Soft Part Sarcoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alveolar Soft Part Sarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Alveolar Soft Part Sarcoma** covering all of the
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
- **Disease Name:** Alveolar Soft Part Sarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Alveolar Soft Part Sarcoma** covering all of the
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


# Alveolar Soft Part Sarcoma (ASPS): Disease Characteristics Research Report (2026-05-09)

## Executive summary
Alveolar soft part sarcoma (ASPS) is an ultra-rare, translocation-defined soft-tissue sarcoma driven by the ASPSCR1::TFE3 fusion that typically presents as a slow-growing, deeply located soft-tissue mass in adolescents and young adults, but with a high propensity for early or eventual metastasis—most commonly to lung, bone, and brain. Recent practice-changing progress includes durable responses to immune checkpoint blockade, notably atezolizumab, with an objective response rate (ORR) of 37% and median progression-free survival (PFS) of 20.8 months in a 2023 phase 2 study that underpinned regulatory approval. Concurrently, mechanistic 2024 work has clarified fusion-driven transcriptional programs and identified targetable dependencies (Cyclin D1/CDK4) that rationalize combination strategies with anti-angiogenic therapy.

## Evidence summary table
The following table consolidates disease identity, clinicopathology, diagnostics, imaging, molecular biology, and the most recent outcome statistics extracted from the tool-retrieved evidence.

| Domain | Item | Key details / quantitative values | Evidence |
|---|---|---|---|
| Disease identity | Definition | Ultra-rare, translocation-defined soft-tissue sarcoma characterized by der(17)t(X;17)(p11.2;q25) creating the **ASPSCR1::TFE3** fusion; typically indolent but highly metastatic and often vascular. Incidence reported as **~1 per 10 million population/year** and **0.2–0.9% of soft-tissue sarcomas**. | (fujiwara2023advancesintreatment pages 1-2) |
| Disease identity | Preferred name / synonym | **Alveolar soft part sarcoma (ASPS)**; literature also refers to **alveolar soft-part sarcoma**. Fusion historically described as **ASPL-TFE3 / TFE3-ASPL** in older literature. | (fujiwara2023advancesintreatment pages 1-2, fernandes2024realworldoutcomes pages 1-2) |
| Disease identity | Identifiers available from retrieved evidence | Retrieved evidence supports disease name and molecular definition, but **MONDO, Orphanet, ICD-10/ICD-11, MeSH, and OMIM identifiers were not directly retrieved in the gathered evidence set**; these should be added from ontology resources separately. | (fujiwara2023advancesintreatment pages 1-2) |
| Clinicopathology | Age distribution | Peak age **15–35 years**; SEER-based review reports median age **25 years**, **72% <30 years**. Recent cohorts: mean **27.1 ± 10.7 y** (Spinnato 2023, n=12), median **27.5 y** (Zhang 2024, n=26), median **28 y** (Fernandes 2024, n=34). | (fujiwara2023advancesintreatment pages 1-2, spinnato2023imagingfeaturesof pages 1-2, zhang2024alveolarsoftpart pages 1-2, fernandes2024realworldoutcomes pages 1-2) |
| Clinicopathology | Sex distribution | Often slight female predominance: review reports **58% female** and approximate male:female ratio **~1:1.5**; however real-world 2024 Indian cohort showed slight male predominance (**19 M / 15 F**). | (fujiwara2023advancesintreatment pages 1-2, cong2025recentprogressin pages 1-2, fernandes2024realworldoutcomes pages 1-2) |
| Clinicopathology | Primary sites | Most common sites: **extremities 61%**, **trunk 20%**, **head/neck 9%**, **internal organs 8%** in review data. In Fernandes 2024, **73%** arose in extremities. Pediatric series showed **50% head/neck** and **50% trunk/limbs**. | (fujiwara2023advancesintreatment pages 1-2, fernandes2024realworldoutcomes pages 1-2, wang2024ultrasoundcharacteristicsof pages 1-2) |
| Clinicopathology | Typical presentation | Usually a **slow-growing, painless deep soft-tissue mass**; tumors are often highly vascular. Zhang 2024: painless enlarged masses in deep soft tissue; Spinnato 2023: all tumors were **deeply seated** with mean longest diameter **7.6 ± 2.9 cm**. | (zhang2024alveolarsoftpart pages 1-2, spinnato2023imagingfeaturesof pages 1-2) |
| Clinicopathology | Metastasis pattern | Common metastatic sites are **lung**, **bone**, and **brain**. Japanese population study: metastatic cases had lung **99%**, bone **14%**, brain **11%**; localized cases later developed distant metastases in **45%**. Fernandes 2024: lung **82%**, bone **21%**, brain metastasis at baseline **25.9%**. | (fujiwara2022alveolarsoftpart pages 1-2, fernandes2024realworldoutcomes pages 1-2, fernandes2024realworldoutcomes pages 2-6) |
| Clinicopathology | Metastasis at diagnosis | High baseline dissemination: Spinnato 2023 **8/12 (66.7%)** metastatic at baseline; Fujiwara 2022 **72%** metastatic at presentation; Fernandes 2024 **27/34 (79%)** metastatic at presentation. Larger tumors were associated with metastasis in imaging cohorts. | (spinnato2023imagingfeaturesof pages 1-2, fujiwara2022alveolarsoftpart pages 1-2, fernandes2024realworldoutcomes pages 2-6) |
| Diagnostics | Histopathology | Classic morphology: organoid/nested epithelioid cells with **pseudoalveolar** architecture, abundant eosinophilic cytoplasm, sinusoidal vasculature; PAS-positive diastase-resistant crystalline material may be present. | (fujiwara2023advancesintreatment pages 1-2, zhang2024alveolarsoftpart pages 4-7) |
| Diagnostics | PAS crystals / PAS positivity | Review data describe **PAS-positive glycogen and rod-shaped crystals** as characteristic. In Zhang 2024, **20/26** tumors were PAS-positive. | (fujiwara2023advancesintreatment pages 1-2, zhang2024alveolarsoftpart pages 4-7) |
| Diagnostics | TFE3 immunohistochemistry | Nuclear **TFE3** staining is a major diagnostic hallmark. Zhang 2024: **24/26 (92.3%)** TFE3-positive. Review literature describes sensitivity often **>95%**, but specificity is imperfect and false positives can occur. | (zhang2024alveolarsoftpart pages 2-4, zhang2024alveolarsoftpart pages 4-7, cong2025recentprogressin pages 4-5) |
| Diagnostics | Fusion event | Pathognomonic chromosomal abnormality: **der(17)t(X;17)(p11.2;q25)** producing **ASPSCR1::TFE3** fusion. This is the key molecular defining event in ASPS. | (fujiwara2023advancesintreatment pages 1-2, fujiwara2022alveolarsoftpart pages 1-2, sicinska2024aspscr1tfe3drivesalveolar pages 1-3) |
| Diagnostics | Fusion testing methods | Molecular confirmation can be performed by **FISH**, **RT-PCR**, and increasingly **RNA sequencing/NGS**. Zhang 2024: **12/12 tested** showed TFE3 rearrangement by FISH in the tested subset. | (zhang2024alveolarsoftpart pages 2-4, cong2025recentprogressin pages 3-4, cong2025recentprogressin pages 4-5) |
| Imaging | Characteristic imaging hallmarks | MRI: slight/mild **T1 hyperintensity**, **T2 hyperintensity**, frequent **flow voids**, peritumoral edema; US: well-defined **hypoechoic heterogeneous** lesion with abundant Doppler flow; large peritumoral feeding vessels seen on US/MRI/CT. | (spinnato2023imagingfeaturesof pages 1-2, spinnato2023imagingfeaturesof pages 8-10, spinnato2023imagingfeaturesof pages 2-4) |
| Imaging | Imaging risk marker | In Spinnato 2023, tumor size **>5 cm** was associated with metastasis at diagnosis (**p=0.01**), with OR **45.0** (95% CI **1.49–1358.36**, **p=0.0285**). Pediatric US study found moderate correlation between size and metastasis risk (**r=0.64**). | (spinnato2023imagingfeaturesof pages 1-2, wang2024ultrasoundcharacteristicsof pages 1-2) |
| Molecular pathogenesis | Core biology | ASPSCR1::TFE3 is essential for tumor cell viability and drives transcriptional programs in **proliferation, angiogenesis, mitochondrial biology, and differentiation**; it engages enhancer/promoter complexes and epigenetic regulators. | (sicinska2024aspscr1tfe3drivesalveolar pages 1-3, sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 8-9) |
| Molecular pathogenesis | Targetable downstream dependencies | 2024 mechanistic work identified **Cyclin D1/CDK4** dependence and showed **palbociclib** reduced proliferation; **palbociclib + sunitinib** was more effective than either alone in xenografts. | (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 13-14) |
| Treatment (recent) | Atezolizumab phase 2 (NEJM 2023) | Multicenter single-group phase 2; **52 evaluable** patients. **ORR 37% (19/52)** = **1 CR + 18 PR**; median time to response **3.6 mo**; median duration of response **24.7 mo**; median **PFS 20.8 mo**; **no treatment-related grade 4/5 AEs**. | (chen2023atezolizumabforadvanced pages 1-3, chen2023atezolizumabforadvanced pages 5-7, chen2023atezolizumabforadvanced pages 7-8) |
| Treatment (recent) | Atezolizumab regulatory relevance / implementation | Study formed the basis for **FDA approval of atezolizumab** for advanced ASPS in late 2022; ongoing trial platform continues as **NCT03141684** (atezolizumab alone or with bevacizumab). | (chen2023atezolizumabforadvanced pages 1-3, NCT03141684 chunk 2, NCT03141684 chunk 3) |
| Treatment (real-world) | TKI outcomes in Fernandes 2024 | In metastatic ASPS, **90%** received first-line TKI. Median **PFS 12 mo** overall for first-line TKI monotherapy; **sunitinib ORR 36%**, disease-control rate **64%**; median PFS numerically **15 vs 11 mo** for sunitinib vs non-sunitinib TKIs. | (fernandes2024realworldoutcomes pages 2-6, fernandes2024realworldoutcomes pages 6-8) |
| Treatment (real-world) | ICI outcomes in Fernandes 2024 | **7** advanced-disease patients received ICIs (**3 atezolizumab, 4 nivolumab**). Atezolizumab produced prolonged disease control in some patients (progression-free at **20** and **15** months in cohort summary). Nivolumab included one ongoing complete metabolic response with duration **~52 months**. | (fernandes2024realworldoutcomes pages 1-2, fernandes2024realworldoutcomes pages 2-6, fernandes2024realworldoutcomes pages 6-8) |
| Prognosis | Population survival (Fujiwara 2022) | In **120** Japanese patients, **5-year disease-specific survival (DSS) 68% overall**, **86% localized**, **62% metastatic** (**p=0.019**). Metastasis at presentation was the only adverse prognostic factor (**HR 7.65**, **p=0.048**). | (fujiwara2022alveolarsoftpart pages 1-2) |
| Prognosis | Additional cohort outcomes | Fernandes 2024 metastatic cohort: median **OS 36 mo**, **3-year OS 52%**; brain metastasis associated with poor survival (**9.4 vs 56 mo**, **p=0.003**). Zhang 2024: prognosis associated with **sex (P=0.006)**, **tumor size (P=0.031)**, and **metastasis (P=0.043)**. | (fernandes2024realworldoutcomes pages 2-6, zhang2024alveolarsoftpart pages 4-7, zhang2024alveolarsoftpart pages 2-4) |
| Trials / current implementation | Active and landmark trial programs | Key ASPS systemic-therapy trials include **NCT03141684** (atezolizumab ± bevacizumab), **NCT02636725** (axitinib + pembrolizumab), and **NCT01391962** (randomized phase 2 cediranib vs sunitinib; actual enrollment **34**). | (NCT03141684 chunk 2, NCT02636725 chunk 2, NCT01391962 chunk 1) |


*Table: This table condenses the most actionable disease-level evidence for alveolar soft part sarcoma, including identity, clinicopathologic characteristics, diagnostic hallmarks, and the most important recent treatment and survival data. It is designed to support knowledge-base population with quantitative facts and direct evidence links.*

---

## 1. Disease information
### 1.1 Definition and overview
ASPS is an ultra-rare soft-tissue sarcoma characterized by a specific chromosomal translocation der(17)t(X;17)(p11.2;q25) producing the ASPSCR1::TFE3 fusion, with an indolent primary tumor behavior but marked metastatic potential. A recent review describes ASPS as “a rare neoplasm of uncertain histogenesis… characterized by a specific chromosomal translocation… that results in ASPSCR1–TFE3 gene fusion,” and summarizes typical sites (extremities/trunk/head–neck) and metastatic predilection (lung/bone/brain). (fujiwara2023advancesintreatment pages 1-2)

### 1.2 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
Within the tool-retrieved evidence set, formal ontology identifiers (OMIM, Orphanet/ORPHA, ICD-10/ICD-11, MeSH, MONDO) were not captured in full text and therefore cannot be asserted without external ontology lookup. The disease name and its defining fusion lesion were consistently supported in the retrieved primary literature and reviews. (fujiwara2023advancesintreatment pages 1-2)

### 1.3 Synonyms and alternative names
Common written variants include “alveolar soft part sarcoma” and “alveolar soft-part sarcoma.” The canonical fusion has also been described historically as “ASPL-TFE3” or “TFE3-ASPL” in older literature; recent papers use ASPSCR1::TFE3. (fujiwara2023advancesintreatment pages 1-2, fernandes2024realworldoutcomes pages 1-2)

### 1.4 Evidence source types
This report integrates aggregated evidence from population-based registries and retrospective cohorts (human clinical), prospective interventional trials (human clinical), and mechanistic preclinical models (in vitro, xenograft/PDX). (fujiwara2022alveolarsoftpart pages 1-2, fernandes2024realworldoutcomes pages 2-6, chen2023atezolizumabforadvanced pages 1-3, sicinska2024aspscr1tfe3drivesalveolar pages 14-16)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factor (genetic/driver lesion):** The defining lesion is an unbalanced t(X;17)(p11.2;q25) producing ASPSCR1::TFE3, a chimeric transcription factor essential for tumor viability. (fujiwara2023advancesintreatment pages 1-2, fujiwara2022alveolarsoftpart pages 1-2, sicinska2024aspscr1tfe3drivesalveolar pages 1-3)

**Mechanistic nature:** ASPSCR1::TFE3 functions as an oncogenic transcriptional regulator that occupies active chromatin and coordinates programs including proliferation and angiogenesis. (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 8-9)

### 2.2 Risk factors
No specific inherited predisposition, environmental exposure, or infectious agent risk factors were identified in the retrieved evidence. The most consistent “risk” correlates relate to clinical factors associated with metastatic presentation (e.g., tumor size, deep location, and age >25 years in a registry cohort) rather than causal exposures. (fujiwara2022alveolarsoftpart pages 1-2, spinnato2023imagingfeaturesof pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence set.

---

## 3. Phenotypes (clinical presentation)
### 3.1 Common phenotypes and suggested HPO terms
**Deep soft-tissue mass; often painless, slow-growing**
- Evidence: “The clinical symptoms mainly included painless enlarged masses in deep soft tissues.” (Zhang 2024) (zhang2024alveolarsoftpart pages 1-2)
- Suggested HPO: 
  - Soft tissue neoplasm (HP:0002664)
  - Painless mass (HP:0031509) (term availability may vary)

**High vascularity / prominent feeding vessels (imaging phenotype)**
- Evidence: ASPS lesions show abundant intratumoral/peritumoral vascularity with prominent feeding vessels on US/MRI/CT. (spinnato2023imagingfeaturesof pages 1-2, spinnato2023imagingfeaturesof pages 8-10)
- Suggested HPO (proxy imaging/vascular): 
  - Increased vascularity (phenotype representation may be recorded clinically rather than as a specific HPO term)

**Metastatic disease manifestations**
- Lung metastasis (common): registry and cohort data show lung as the dominant metastatic site. (fujiwara2022alveolarsoftpart pages 1-2, fernandes2024realworldoutcomes pages 2-6)
- Brain metastasis (notable in ASPS): baseline brain metastasis 25.9% in one real-world cohort with poor outcomes. (fernandes2024realworldoutcomes pages 2-6)
- Suggested HPO:
  - Neoplasm metastasis (HP:0003002)
  - Pulmonary metastasis (HP:0031411)
  - Brain metastasis (HP:0007297)

### 3.2 Age of onset and progression
ASPS most commonly affects adolescents and young adults (peak ~15–35 years; SEER median age ~25; majority <30), and often follows an indolent course that can delay diagnosis, but with frequent metastasis at baseline or later. (fujiwara2023advancesintreatment pages 1-2, fujiwara2022alveolarsoftpart pages 1-2, spinnato2023imagingfeaturesof pages 1-2)

### 3.3 Frequency and severity
Quantitative frequencies vary by cohort and ascertainment, but baseline metastasis rates are often high:
- 72% metastatic at presentation in a Japanese registry (n=120). (fujiwara2022alveolarsoftpart pages 1-2)
- 66.7% metastatic at baseline in an imaging cohort (n=12). (spinnato2023imagingfeaturesof pages 1-2)
- 79% metastatic at presentation in a tertiary-care real-world cohort (n=34). (fernandes2024realworldoutcomes pages 2-6)

### 3.4 Quality of life impact
QoL instruments (EQ-5D/SF-36) were not reported in the retrieved evidence. QoL impact is inferred from tumor burden and metastatic complications (notably CNS involvement) but cannot be quantified here.

---

## 4. Genetic / molecular information
### 4.1 Causal genes and chromosomal abnormalities
- **ASPSCR1** and **TFE3** are implicated via the defining fusion ASPSCR1::TFE3 produced by der(17)t(X;17)(p11.2;q25). (fujiwara2023advancesintreatment pages 1-2, sicinska2024aspscr1tfe3drivesalveolar pages 1-3)

### 4.2 Pathogenic variants and variant properties
ASPS is primarily driven by a **somatic structural variant (fusion/translocation)** rather than recurrent point mutations in the retrieved sources.
- Variant class: structural rearrangement (fusion)
- Origin: somatic (tumor)
- Detection: FISH/RT-PCR/RNA-seq/NGS (methods discussed in recent pathology sources). (zhang2024alveolarsoftpart pages 2-4, cong2025recentprogressin pages 4-5)

Population allele frequencies (gnomAD/ExAC) are not applicable for a tumor-specific fusion.

### 4.3 Diagnostic biomarker performance (TFE3)
TFE3 nuclear immunohistochemistry (IHC) is a key marker, but practical specificity can vary; a recent clinicopathologic series reported TFE3 positivity in **24/26 (92.3%)** cases. (zhang2024alveolarsoftpart pages 2-4)

### 4.4 Epigenetic / transcriptional regulation (recent mechanistic advance; 2024)
A 2024 Cancer Research study mapped ASPS transcriptional/chromatin landscapes and provides direct mechanistic statements in the abstract:
- Quote: “ASPSCR1::TFE3 directly interacted with key epigenetic regulators at enhancers and promoters to support ASPS-associated transcription.” (sicinska2024aspscr1tfe3drivesalveolar pages 1-3)
- Quote: “cell proliferation was driven by high levels of cyclin D1 expression.” (sicinska2024aspscr1tfe3drivesalveolar pages 1-3)
- Therapeutic implication: “combined inhibition of CDK4/6 and angiogenesis halted tumor growth in xenografts.” (sicinska2024aspscr1tfe3drivesalveolar pages 1-3)

### 4.5 Disease–target associations (knowledge graph)
OpenTargets lists ASPS associations for TFE3 and angiogenesis-related targets (e.g., KDR/VEGFR2, FLT4/VEGFR3, PDGFRB), reflecting both biology and clinical development focus. (OpenTargets Search: Alveolar soft part sarcoma)

---

## 5. Environmental information
No specific environmental, lifestyle, or infectious causal contributors were identified in the retrieved evidence.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (current understanding)
1) **Initiating lesion:** somatic der(17)t(X;17) generates **ASPSCR1::TFE3**. (fujiwara2023advancesintreatment pages 1-2, sicinska2024aspscr1tfe3drivesalveolar pages 1-3)
2) **Fusion-driven transcriptional amplification:** ASPSCR1::TFE3 broadly binds active chromatin and sustains programs in cell cycle/proliferation, angiogenesis, and mitochondrial biology. (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 8-9)
3) **Tumor phenotype:** highly vascular tumor microenvironment and slow-growing primary lesions, with high metastatic propensity (lung/bone/brain). (fujiwara2022alveolarsoftpart pages 1-2, spinnato2023imagingfeaturesof pages 1-2)
4) **Clinical manifestations:** painless deep mass; metastatic symptoms depend on organ involved; brain metastasis is an adverse clinical turning point in real-world cohorts. (fernandes2024realworldoutcomes pages 2-6)

### 6.2 Key molecular programs and targetable dependencies (2024)
Mechanistic evidence supports targetable tumor-intrinsic and tumor-extrinsic vulnerabilities:
- **Cyclin D1/CDK4 dependency:** palbociclib decreased Ki-67 and halted tumor growth in ASPS PDX; CRISPR targeting supports dependency; CDK4/6 + VEGFR inhibition improved xenograft control. (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 13-14)
- **Angiogenesis program:** ASPS super-enhancers and expression profiles include angiogenesis genes (e.g., VEGFA), consistent with clinical activity of anti-angiogenic TKIs. (sicinska2024aspscr1tfe3drivesalveolar pages 8-9, fernandes2024realworldoutcomes pages 2-6)

### 6.3 Suggested ontology terms
**GO biological process (examples):**
- Angiogenesis (GO:0001525)
- Regulation of transcription by RNA polymerase II (GO:0006357)
- Cell cycle G1/S transition (GO:0044843)
- Mitochondrial biogenesis (GO:0007005)

**Cell types (CL, examples):**
- Mesenchymal cell (CL:0000134)
- Endothelial cell (CL:0000115) (relevant to the vascular phenotype)

---

## 7. Anatomical structures affected
### 7.1 Primary anatomical sites
Most commonly deep soft tissues of extremities (often thigh), with additional sites including trunk and head/neck; pediatric cohorts show relatively more head/neck presentations. (fujiwara2023advancesintreatment pages 1-2, wang2024ultrasoundcharacteristicsof pages 1-2)

Suggested UBERON (examples):
- Limb (UBERON:0002101)
- Thigh (UBERON:0000978)
- Head and neck region (UBERON:0000033)

### 7.2 Secondary organs (metastases)
- Lung (dominant), bone, brain; liver also occurs in some series. (fujiwara2022alveolarsoftpart pages 1-2, zhang2024alveolarsoftpart pages 2-4, fernandes2024realworldoutcomes pages 2-6)

Suggested UBERON (examples):
- Lung (UBERON:0002048)
- Bone tissue (UBERON:0002481)
- Brain (UBERON:0000955)

---

## 8. Temporal development
### 8.1 Onset
Typically adolescent/young adult onset (peak 15–35), but cases can occur across a wide age range. (fujiwara2023advancesintreatment pages 1-2, zhang2024alveolarsoftpart pages 2-4)

### 8.2 Progression and course
ASPS often shows slow primary growth but frequent metastasis at diagnosis and ongoing metastatic risk even after localized presentation.
- Example: in a registry cohort of localized ASPS, **45%** developed distant metastases later. (fujiwara2022alveolarsoftpart pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology
- Incidence estimate: **~1 per 10 million population per year** (review-level estimate). (fujiwara2023advancesintreatment pages 1-2)
- Proportion of soft-tissue sarcomas: **~0.2–0.9%** (review-level). (fujiwara2023advancesintreatment pages 1-2)

Prevalence estimates were not provided in the retrieved evidence.

### 9.2 Inheritance
ASPS is not described as a Mendelian inherited disorder in the retrieved sources; it is primarily a sporadic cancer driven by a somatic fusion event.

### 9.3 Demographics
- Sex: often female predominance reported in reviews, but cohort-to-cohort variation exists. (fujiwara2023advancesintreatment pages 1-2, fernandes2024realworldoutcomes pages 2-6)
- Age: concentration in younger patients. (fujiwara2023advancesintreatment pages 1-2)

---

## 10. Diagnostics
### 10.1 Pathology and biomarkers
- **TFE3 IHC**: 24/26 positive in a 2024 series; sensitivity high but specificity can vary. (zhang2024alveolarsoftpart pages 2-4, cong2025recentprogressin pages 4-5)
- **Molecular confirmation**: FISH/RT-PCR/NGS for ASPSCR1::TFE3; Zhang 2024 detected TFE3 rearrangement in 12 tested patients. (zhang2024alveolarsoftpart pages 2-4)
- **PAS-positive crystals**: 20/26 PAS-positive in Zhang 2024. (zhang2024alveolarsoftpart pages 4-7)

### 10.2 Imaging-based diagnosis (2023–2024 evidence)
ASPS is notable for hypervascular imaging patterns that can mimic vascular malformations.
- MRI/US hallmarks (Spinnato 2023): Quote from abstract: “Large peritumoral feeding vessels were systematically found and identified on ultrasonography (7/7), MRI (10/10), and CT (3/3).” (spinnato2023imagingfeaturesof pages 1-2)
- Pediatric ultrasound (Wang 2024) describes rich vascularity and misclassification as vascular lesions in some cases; tumors were 50% head/neck and 50% trunk/limbs, with 8/20 metastatic at diagnosis. (wang2024ultrasoundcharacteristicsof pages 1-2, wang2024ultrasoundcharacteristicsof pages 3-6)

### 10.3 Differential diagnosis
A structured differential diagnosis list was not fully extractable from the retrieved evidence set; however, the need for molecular confirmation (fusion testing) in TFE3-positive or equivocal cases is emphasized due to IHC variability. (cong2025recentprogressin pages 4-5)

---

## 11. Outcome / prognosis
### 11.1 Survival statistics (population-level)
A Japanese population-based study (2006–2017; n=120) reported:
- “The 5-year disease-specific survival (DSS) was **68%** for all patients and **86%** and **62%** for localized and metastatic disease, respectively.” (fujiwara2022alveolarsoftpart pages 1-2)
- Metastasis at presentation was the only adverse prognostic factor (HR 7.65). (fujiwara2022alveolarsoftpart pages 1-2)

### 11.2 Real-world outcomes (2024)
A tertiary-center real-world cohort (2016–2023; n=34) reported:
- Median PFS on first-line TKI monotherapy: **12 months**; median OS in metastatic cohort: **36 months**; 3-year OS: **52%**. (fernandes2024realworldoutcomes pages 2-6)
- Brain metastasis conferred markedly poor outcomes (OS **9.4 vs 56 months**). (fernandes2024realworldoutcomes pages 2-6)

### 11.3 Prognostic factors
In a 2024 clinicopathologic series (n=26), prognosis was significantly correlated with sex, tumor size, and metastasis; multivariable Cox regression identified sex and metastasis as independent prognostic factors. (zhang2024alveolarsoftpart pages 4-7, zhang2024alveolarsoftpart pages 2-4)

---

## 12. Treatment
### 12.1 Standard local therapy
Complete surgical resection is described as the standard approach for localized disease, with radiotherapy considered for inadequate margins or unresectable tumors. (fujiwara2023advancesintreatment pages 1-2)

Suggested MAXO terms (examples):
- Surgical excision (MAXO:0001025)
- Radiotherapy (MAXO:0000647)

### 12.2 Systemic therapy: recent developments (prioritizing 2023–2024)
#### Atezolizumab (PD-L1 inhibitor) — pivotal 2023 evidence
A 2023 investigator-initiated multicenter single-group phase 2 study (NEJM; ClinicalTrials.gov NCT03141684) reported:
- Quote: “An objective response was observed in **19 of 52 patients (37%)**, with **1 complete response** and **18 partial responses**.” (chen2023atezolizumabforadvanced pages 1-3)
- Quote: “the median duration of response was **24.7 months** (range, 4.1 to 55.8), and the median progression-free survival was **20.8 months**.” (chen2023atezolizumabforadvanced pages 1-3)
- Safety: no treatment-related grade 4–5 AEs in the abstract; detailed excerpt indicates grade 3 potentially related AEs in 15% and no discontinuations due to AEs. (chen2023atezolizumabforadvanced pages 1-3, chen2023atezolizumabforadvanced pages 7-8)

**Real-world implementation:** The same NEJM paper notes FDA approval of atezolizumab based on this study, and ongoing trial infrastructure includes atezolizumab alone or with bevacizumab (NCT03141684). (chen2023atezolizumabforadvanced pages 1-3, NCT03141684 chunk 2)

**Visual evidence (trial efficacy figures):** Waterfall plot and Kaplan–Meier PFS are provided from the NEJM report. (chen2023atezolizumabforadvanced media 37f80583, chen2023atezolizumabforadvanced media 591ab6cf)

Suggested MAXO terms:
- Immune checkpoint inhibitor therapy (MAXO:0001481)
- PD-L1 inhibitor therapy (MAXO term may vary by release)

#### Anti-angiogenic TKIs (VEGFR pathway) — real-world and trial infrastructure
A 2024 real-world cohort found most metastatic patients received TKIs first line, with median PFS 12 months and sunitinib ORR 36%. (fernandes2024realworldoutcomes pages 2-6)

A randomized phase 2 crossover trial comparing cediranib vs sunitinib (NCT01391962; enrollment 34) used ORR and 24-week PFS endpoints and required RECIST-defined progression prior to enrollment, reflecting the clinical need to benchmark TKI activity in ASPS. (NCT01391962 chunk 1)

Suggested MAXO terms:
- Tyrosine kinase inhibitor therapy (MAXO:0000943)
- Antiangiogenic therapy (MAXO:0000938)

#### Combination and next-step strategies (mechanism-informed)
A 2024 mechanistic study supports combined targeting of cell-intrinsic CDK4 dependence and cell-extrinsic angiogenesis:
- Quote (preclinical): “the combination of palbociclib and sunitinib was significantly more effective than either therapy alone…” (sicinska2024aspscr1tfe3drivesalveolar pages 14-16)
This motivates clinical exploration of CDK4/6 inhibitors with anti-angiogenic agents (clinical translation remains investigational in ASPS). (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 13-14)

Suggested MAXO:
- CDK4/6 inhibitor therapy (MAXO term may vary)

### 12.3 Active/landmark clinical trials (selected)
- **NCT03141684** (NCI; started 2017): atezolizumab alone or atezolizumab + bevacizumab; ORR by RECIST v1.1 is the primary endpoint; includes biopsy and imaging procedures. (NCT03141684 chunk 2, NCT03141684 chunk 3)
- **NCT02636725** (PI Jonathan Trent; started 2016): axitinib + pembrolizumab phase 2 single-arm; requires measurable disease and RECIST-defined progression; requires serial core biopsies. (NCT02636725 chunk 2)
- **NCT01391962** (NCI; started 2011): randomized phase 2 cediranib vs sunitinib with crossover; primary endpoints include ORR and 24-week PFS. (NCT01391962 chunk 1)

---

## 13. Prevention
No primary prevention strategies are established for ASPS in the retrieved evidence. Secondary/tertiary prevention in practice involves early recognition of hypervascular deep soft-tissue masses, referral to sarcoma centers, and appropriate staging (including chest and, in selected contexts, brain imaging given non-trivial CNS involvement in some cohorts). (spinnato2023imagingfeaturesof pages 1-2, fernandes2024realworldoutcomes pages 2-6)

---

## 14. Other species / natural disease
No naturally occurring ASPS analogs in non-human species were identified in the retrieved evidence.

---

## 15. Model organisms / preclinical models
Mechanistic work uses ASPS cell lines and xenograft/PDX models.
- A 2024 Cancer Research study reports palbociclib effects in ASPS PDX and combination efficacy with sunitinib in xenografts, supporting translational modeling for therapy development. (sicinska2024aspscr1tfe3drivesalveolar pages 14-16, sicinska2024aspscr1tfe3drivesalveolar pages 13-14)

---

## Recent developments (2023–2024) — key takeaways for a knowledge base
1) **Checkpoint blockade is now a central systemic option in advanced ASPS**: atezolizumab achieved ORR 37% with durable responses and median PFS 20.8 months, with favorable high-grade toxicity profile (no treatment-related grade 4–5 AEs), and served as the basis for regulatory approval. (chen2023atezolizumabforadvanced pages 1-3, chen2023atezolizumabforadvanced pages 7-8)
2) **Real-world data confirm continued importance of anti-angiogenic TKIs and highlight CNS metastasis as a major adverse factor**, with median OS 36 months in a heavily metastatic cohort and OS ~9.4 months in those with brain metastases. (fernandes2024realworldoutcomes pages 2-6)
3) **Mechanistic 2024 data identify a targetable cell-cycle dependency (Cyclin D1/CDK4) and support combination strategies with angiogenesis inhibition**, providing a rational next wave of trial design beyond single-agent VEGFR-TKIs and ICIs. (sicinska2024aspscr1tfe3drivesalveolar pages 1-3, sicinska2024aspscr1tfe3drivesalveolar pages 14-16)

---

## Limitations of the retrieved evidence for this template
- Formal disease identifiers (MONDO/Orphanet/OMIM/ICD/MeSH) were not available in the retrieved full-text snippets; they should be added from dedicated ontology resources.
- QoL metrics, prevalence estimates, and comprehensive differential diagnosis lists were not captured in the current evidence set.
- Some citations above are based on tool-provided excerpts; if a downstream curation workflow requires PMIDs for every item, the DOI-anchored references provided here should be mapped to PMIDs via PubMed.


References

1. (fujiwara2023advancesintreatment pages 1-2): Tomohiro Fujiwara, Toshiyuki Kunisada, Eiji Nakata, Kenji Nishida, Hiroyuki Yanai, Tomoki Nakamura, Kazuhiro Tanaka, and Toshifumi Ozaki. Advances in treatment of alveolar soft part sarcoma: an updated review. Japanese Journal of Clinical Oncology, 53:1009-1018, Aug 2023. URL: https://doi.org/10.1093/jjco/hyad102, doi:10.1093/jjco/hyad102. This article has 26 citations and is from a peer-reviewed journal.

2. (fernandes2024realworldoutcomes pages 1-2): Sanal Fernandes, Sameer Rastogi, Kanu Priya Bhatia, Sindhura Chitikela, Shamim A Shamim, Shivanand Gammanagatti, and Adarsh Barwad. Real world outcomes in alveolar soft part sarcomas: experience with an ultra-rare sarcoma from a tertiary care centre in north india. ecancermedicalscience, Dec 2024. URL: https://doi.org/10.3332/ecancer.2024.1813, doi:10.3332/ecancer.2024.1813. This article has 1 citations and is from a peer-reviewed journal.

3. (spinnato2023imagingfeaturesof pages 1-2): Paolo Spinnato, Nicolas Papalexis, Marco Colangeli, Marco Miceli, Amandine Crombé, Anna Parmeggiani, Emanuela Palmerini, Alberto Righi, and Giuseppe Bianchi. Imaging features of alveolar soft part sarcoma: single institution experience and literature review. Clinics and Practice, 13:1369-1382, Nov 2023. URL: https://doi.org/10.3390/clinpract13060123, doi:10.3390/clinpract13060123. This article has 16 citations.

4. (zhang2024alveolarsoftpart pages 1-2): Yi Zhang, Yuchen Huang, Yanzi Qin, Ningning Yang, Panpan Yang, Nan Li, and Zhenzhong Feng. Alveolar soft part sarcoma: a clinicopathological and immunohistochemical analysis of 26 cases emphasizing risk factors and prognosis. Diagnostic Pathology, Jan 2024. URL: https://doi.org/10.1186/s13000-024-01450-z, doi:10.1186/s13000-024-01450-z. This article has 10 citations and is from a peer-reviewed journal.

5. (cong2025recentprogressin pages 1-2): Nan Cong, Qi Shi, Qingyu Xu, and Lin Zhang. Recent progress in the clinicopathological characteristics of alveolar soft part sarcoma. Frontiers in Medicine, Dec 2025. URL: https://doi.org/10.3389/fmed.2025.1702870, doi:10.3389/fmed.2025.1702870. This article has 0 citations.

6. (wang2024ultrasoundcharacteristicsof pages 1-2): Siwei Wang, Yu Wang, Jiatong Xu, Qinghua Ren, Yanxiu Hu, Liqun Jia, and Xiaoman Wang. Ultrasound characteristics of alveolar soft part sarcoma in pediatric patients: a retrospective analysis. BMC Cancer, Dec 2024. URL: https://doi.org/10.1186/s12885-024-13262-x, doi:10.1186/s12885-024-13262-x. This article has 2 citations and is from a peer-reviewed journal.

7. (fujiwara2022alveolarsoftpart pages 1-2): Tomohiro Fujiwara, Eiji Nakata, Toshiyuki Kunisada, Toshifumi Ozaki, and Akira Kawai. Alveolar soft part sarcoma: progress toward improvement in survival? a population-based study. BMC Cancer, Aug 2022. URL: https://doi.org/10.1186/s12885-022-09968-5, doi:10.1186/s12885-022-09968-5. This article has 33 citations and is from a peer-reviewed journal.

8. (fernandes2024realworldoutcomes pages 2-6): Sanal Fernandes, Sameer Rastogi, Kanu Priya Bhatia, Sindhura Chitikela, Shamim A Shamim, Shivanand Gammanagatti, and Adarsh Barwad. Real world outcomes in alveolar soft part sarcomas: experience with an ultra-rare sarcoma from a tertiary care centre in north india. ecancermedicalscience, Dec 2024. URL: https://doi.org/10.3332/ecancer.2024.1813, doi:10.3332/ecancer.2024.1813. This article has 1 citations and is from a peer-reviewed journal.

9. (zhang2024alveolarsoftpart pages 4-7): Yi Zhang, Yuchen Huang, Yanzi Qin, Ningning Yang, Panpan Yang, Nan Li, and Zhenzhong Feng. Alveolar soft part sarcoma: a clinicopathological and immunohistochemical analysis of 26 cases emphasizing risk factors and prognosis. Diagnostic Pathology, Jan 2024. URL: https://doi.org/10.1186/s13000-024-01450-z, doi:10.1186/s13000-024-01450-z. This article has 10 citations and is from a peer-reviewed journal.

10. (zhang2024alveolarsoftpart pages 2-4): Yi Zhang, Yuchen Huang, Yanzi Qin, Ningning Yang, Panpan Yang, Nan Li, and Zhenzhong Feng. Alveolar soft part sarcoma: a clinicopathological and immunohistochemical analysis of 26 cases emphasizing risk factors and prognosis. Diagnostic Pathology, Jan 2024. URL: https://doi.org/10.1186/s13000-024-01450-z, doi:10.1186/s13000-024-01450-z. This article has 10 citations and is from a peer-reviewed journal.

11. (cong2025recentprogressin pages 4-5): Nan Cong, Qi Shi, Qingyu Xu, and Lin Zhang. Recent progress in the clinicopathological characteristics of alveolar soft part sarcoma. Frontiers in Medicine, Dec 2025. URL: https://doi.org/10.3389/fmed.2025.1702870, doi:10.3389/fmed.2025.1702870. This article has 0 citations.

12. (sicinska2024aspscr1tfe3drivesalveolar pages 1-3): Ewa Sicinska, Vijaya S.R. Kola, Joseph A. Kerfoot, Madeleine L. Taddei, Alyaa Al-Ibraheemi, Yi-Hsuan Hsieh, Alanna J. Church, Esther Landesman-Bollag, Yosef Landesman, and Matthew L. Hemming. Aspscr1::tfe3 drives alveolar soft part sarcoma by inducing targetable transcriptional programs. Cancer Research, 84:2247-2264, Apr 2024. URL: https://doi.org/10.1158/0008-5472.can-23-2115, doi:10.1158/0008-5472.can-23-2115. This article has 11 citations and is from a highest quality peer-reviewed journal.

13. (cong2025recentprogressin pages 3-4): Nan Cong, Qi Shi, Qingyu Xu, and Lin Zhang. Recent progress in the clinicopathological characteristics of alveolar soft part sarcoma. Frontiers in Medicine, Dec 2025. URL: https://doi.org/10.3389/fmed.2025.1702870, doi:10.3389/fmed.2025.1702870. This article has 0 citations.

14. (spinnato2023imagingfeaturesof pages 8-10): Paolo Spinnato, Nicolas Papalexis, Marco Colangeli, Marco Miceli, Amandine Crombé, Anna Parmeggiani, Emanuela Palmerini, Alberto Righi, and Giuseppe Bianchi. Imaging features of alveolar soft part sarcoma: single institution experience and literature review. Clinics and Practice, 13:1369-1382, Nov 2023. URL: https://doi.org/10.3390/clinpract13060123, doi:10.3390/clinpract13060123. This article has 16 citations.

15. (spinnato2023imagingfeaturesof pages 2-4): Paolo Spinnato, Nicolas Papalexis, Marco Colangeli, Marco Miceli, Amandine Crombé, Anna Parmeggiani, Emanuela Palmerini, Alberto Righi, and Giuseppe Bianchi. Imaging features of alveolar soft part sarcoma: single institution experience and literature review. Clinics and Practice, 13:1369-1382, Nov 2023. URL: https://doi.org/10.3390/clinpract13060123, doi:10.3390/clinpract13060123. This article has 16 citations.

16. (sicinska2024aspscr1tfe3drivesalveolar pages 14-16): Ewa Sicinska, Vijaya S.R. Kola, Joseph A. Kerfoot, Madeleine L. Taddei, Alyaa Al-Ibraheemi, Yi-Hsuan Hsieh, Alanna J. Church, Esther Landesman-Bollag, Yosef Landesman, and Matthew L. Hemming. Aspscr1::tfe3 drives alveolar soft part sarcoma by inducing targetable transcriptional programs. Cancer Research, 84:2247-2264, Apr 2024. URL: https://doi.org/10.1158/0008-5472.can-23-2115, doi:10.1158/0008-5472.can-23-2115. This article has 11 citations and is from a highest quality peer-reviewed journal.

17. (sicinska2024aspscr1tfe3drivesalveolar pages 8-9): Ewa Sicinska, Vijaya S.R. Kola, Joseph A. Kerfoot, Madeleine L. Taddei, Alyaa Al-Ibraheemi, Yi-Hsuan Hsieh, Alanna J. Church, Esther Landesman-Bollag, Yosef Landesman, and Matthew L. Hemming. Aspscr1::tfe3 drives alveolar soft part sarcoma by inducing targetable transcriptional programs. Cancer Research, 84:2247-2264, Apr 2024. URL: https://doi.org/10.1158/0008-5472.can-23-2115, doi:10.1158/0008-5472.can-23-2115. This article has 11 citations and is from a highest quality peer-reviewed journal.

18. (sicinska2024aspscr1tfe3drivesalveolar pages 13-14): Ewa Sicinska, Vijaya S.R. Kola, Joseph A. Kerfoot, Madeleine L. Taddei, Alyaa Al-Ibraheemi, Yi-Hsuan Hsieh, Alanna J. Church, Esther Landesman-Bollag, Yosef Landesman, and Matthew L. Hemming. Aspscr1::tfe3 drives alveolar soft part sarcoma by inducing targetable transcriptional programs. Cancer Research, 84:2247-2264, Apr 2024. URL: https://doi.org/10.1158/0008-5472.can-23-2115, doi:10.1158/0008-5472.can-23-2115. This article has 11 citations and is from a highest quality peer-reviewed journal.

19. (chen2023atezolizumabforadvanced pages 1-3): Alice P. Chen, Elad Sharon, Geraldine O’Sullivan-Coyne, Nancy Moore, Jared C. Foster, James S. Hu, Brian A. Van Tine, Anthony P. Conley, William L. Read, Richard F. Riedel, Melissa A. Burgess, John Glod, Elizabeth J. Davis, Priscilla Merriam, Abdul R. Naqash, Kristin K. Fino, Brandon L. Miller, Deborah F. Wilsker, Asma Begum, Katherine V. Ferry-Galow, Hari A. Deshpande, Gary K. Schwartz, Brian H. Ladle, Scott H. Okuno, Jill C. Beck, James L. Chen, Naoko Takebe, Laura K. Fogli, Christina L. Rosenberger, Ralph E. Parchment, and James H. Doroshow. Atezolizumab for advanced alveolar soft part sarcoma. The New England journal of medicine, 389 10:911-921, Sep 2023. URL: https://doi.org/10.1056/nejmoa2303383, doi:10.1056/nejmoa2303383. This article has 167 citations and is from a highest quality peer-reviewed journal.

20. (chen2023atezolizumabforadvanced pages 5-7): Alice P. Chen, Elad Sharon, Geraldine O’Sullivan-Coyne, Nancy Moore, Jared C. Foster, James S. Hu, Brian A. Van Tine, Anthony P. Conley, William L. Read, Richard F. Riedel, Melissa A. Burgess, John Glod, Elizabeth J. Davis, Priscilla Merriam, Abdul R. Naqash, Kristin K. Fino, Brandon L. Miller, Deborah F. Wilsker, Asma Begum, Katherine V. Ferry-Galow, Hari A. Deshpande, Gary K. Schwartz, Brian H. Ladle, Scott H. Okuno, Jill C. Beck, James L. Chen, Naoko Takebe, Laura K. Fogli, Christina L. Rosenberger, Ralph E. Parchment, and James H. Doroshow. Atezolizumab for advanced alveolar soft part sarcoma. The New England journal of medicine, 389 10:911-921, Sep 2023. URL: https://doi.org/10.1056/nejmoa2303383, doi:10.1056/nejmoa2303383. This article has 167 citations and is from a highest quality peer-reviewed journal.

21. (chen2023atezolizumabforadvanced pages 7-8): Alice P. Chen, Elad Sharon, Geraldine O’Sullivan-Coyne, Nancy Moore, Jared C. Foster, James S. Hu, Brian A. Van Tine, Anthony P. Conley, William L. Read, Richard F. Riedel, Melissa A. Burgess, John Glod, Elizabeth J. Davis, Priscilla Merriam, Abdul R. Naqash, Kristin K. Fino, Brandon L. Miller, Deborah F. Wilsker, Asma Begum, Katherine V. Ferry-Galow, Hari A. Deshpande, Gary K. Schwartz, Brian H. Ladle, Scott H. Okuno, Jill C. Beck, James L. Chen, Naoko Takebe, Laura K. Fogli, Christina L. Rosenberger, Ralph E. Parchment, and James H. Doroshow. Atezolizumab for advanced alveolar soft part sarcoma. The New England journal of medicine, 389 10:911-921, Sep 2023. URL: https://doi.org/10.1056/nejmoa2303383, doi:10.1056/nejmoa2303383. This article has 167 citations and is from a highest quality peer-reviewed journal.

22. (NCT03141684 chunk 2):  Testing Atezolizumab Alone or Atezolizumab Plus Bevacizumab in People With Advanced Alveolar Soft Part Sarcoma. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03141684

23. (NCT03141684 chunk 3):  Testing Atezolizumab Alone or Atezolizumab Plus Bevacizumab in People With Advanced Alveolar Soft Part Sarcoma. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03141684

24. (fernandes2024realworldoutcomes pages 6-8): Sanal Fernandes, Sameer Rastogi, Kanu Priya Bhatia, Sindhura Chitikela, Shamim A Shamim, Shivanand Gammanagatti, and Adarsh Barwad. Real world outcomes in alveolar soft part sarcomas: experience with an ultra-rare sarcoma from a tertiary care centre in north india. ecancermedicalscience, Dec 2024. URL: https://doi.org/10.3332/ecancer.2024.1813, doi:10.3332/ecancer.2024.1813. This article has 1 citations and is from a peer-reviewed journal.

25. (NCT02636725 chunk 2): Jonathan Trent, MD, PhD. Axitinib and Pembrolizumab in Subjects With Advanced Alveolar Soft Part Sarcoma and Other Soft Tissue Sarcomas. Jonathan Trent, MD, PhD. 2016. ClinicalTrials.gov Identifier: NCT02636725

26. (NCT01391962 chunk 1): Alice Chen, M.D.. Sunitinib or Cediranib for Alveolar Soft Part Sarcoma. National Cancer Institute (NCI). 2011. ClinicalTrials.gov Identifier: NCT01391962

27. (OpenTargets Search: Alveolar soft part sarcoma): Open Targets Query (Alveolar soft part sarcoma, 42 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

28. (wang2024ultrasoundcharacteristicsof pages 3-6): Siwei Wang, Yu Wang, Jiatong Xu, Qinghua Ren, Yanxiu Hu, Liqun Jia, and Xiaoman Wang. Ultrasound characteristics of alveolar soft part sarcoma in pediatric patients: a retrospective analysis. BMC Cancer, Dec 2024. URL: https://doi.org/10.1186/s12885-024-13262-x, doi:10.1186/s12885-024-13262-x. This article has 2 citations and is from a peer-reviewed journal.

29. (chen2023atezolizumabforadvanced media 37f80583): Alice P. Chen, Elad Sharon, Geraldine O’Sullivan-Coyne, Nancy Moore, Jared C. Foster, James S. Hu, Brian A. Van Tine, Anthony P. Conley, William L. Read, Richard F. Riedel, Melissa A. Burgess, John Glod, Elizabeth J. Davis, Priscilla Merriam, Abdul R. Naqash, Kristin K. Fino, Brandon L. Miller, Deborah F. Wilsker, Asma Begum, Katherine V. Ferry-Galow, Hari A. Deshpande, Gary K. Schwartz, Brian H. Ladle, Scott H. Okuno, Jill C. Beck, James L. Chen, Naoko Takebe, Laura K. Fogli, Christina L. Rosenberger, Ralph E. Parchment, and James H. Doroshow. Atezolizumab for advanced alveolar soft part sarcoma. The New England journal of medicine, 389 10:911-921, Sep 2023. URL: https://doi.org/10.1056/nejmoa2303383, doi:10.1056/nejmoa2303383. This article has 167 citations and is from a highest quality peer-reviewed journal.

30. (chen2023atezolizumabforadvanced media 591ab6cf): Alice P. Chen, Elad Sharon, Geraldine O’Sullivan-Coyne, Nancy Moore, Jared C. Foster, James S. Hu, Brian A. Van Tine, Anthony P. Conley, William L. Read, Richard F. Riedel, Melissa A. Burgess, John Glod, Elizabeth J. Davis, Priscilla Merriam, Abdul R. Naqash, Kristin K. Fino, Brandon L. Miller, Deborah F. Wilsker, Asma Begum, Katherine V. Ferry-Galow, Hari A. Deshpande, Gary K. Schwartz, Brian H. Ladle, Scott H. Okuno, Jill C. Beck, James L. Chen, Naoko Takebe, Laura K. Fogli, Christina L. Rosenberger, Ralph E. Parchment, and James H. Doroshow. Atezolizumab for advanced alveolar soft part sarcoma. The New England journal of medicine, 389 10:911-921, Sep 2023. URL: https://doi.org/10.1056/nejmoa2303383, doi:10.1056/nejmoa2303383. This article has 167 citations and is from a highest quality peer-reviewed journal.