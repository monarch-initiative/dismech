---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:52.421559'
end_time: '2026-04-04T12:55:23.400926'
duration_seconds: 750.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FOXE3-Related Anterior Segment Dysgenesis
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** FOXE3-Related Anterior Segment Dysgenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FOXE3-Related Anterior Segment Dysgenesis** covering all of the
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
- **Disease Name:** FOXE3-Related Anterior Segment Dysgenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FOXE3-Related Anterior Segment Dysgenesis** covering all of the
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


# FOXE3-Related Anterior Segment Dysgenesis (ASD2; OMIM 610256): Comprehensive Research Report

## Executive summary
FOXE3-related anterior segment dysgenesis is a Mendelian developmental eye disorder caused by pathogenic variants in the lens transcription factor **FOXE3** (gene MIM **601094**) and classically mapped to **Anterior segment dysgenesis 2 (ASD2; OMIM 610256)**. It shows **both autosomal recessive (biallelic) and autosomal dominant** inheritance, with a strong genotype–phenotype relationship: **biallelic loss-of-function/forkhead-domain missense variants** tend to cause **severe congenital malformations** (corneal opacity/sclerocornea, aphakia, microphthalmia), while **dominant C-terminal extension (stop-loss/non-stop) variants** more often cause **cataract with variable, usually milder anterior segment anomalies**. (reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13, iseri2009seeingclearlythe pages 2-3)

Recent (2023–2024) literature emphasizes (i) increasing availability—but high heterogeneity—of **commercial gene panels** for anterior segment phenotypes, (ii) the role of **WES** in resolving phenotypically overlapping congenital ocular disorders, and (iii) improved evidence synthesis on **management and outcomes** for key overlapping clinical entities (notably **Peters anomaly**) that frequently appear in the FOXE3 spectrum. (wowra2024generaltreatmentand pages 1-2, procopio2023comparinggenepanels pages 1-2, zucco2024abird’seye pages 3-4)

---

## 1. Disease information
### 1.1 Definition / overview
**Anterior segment dysgenesis (ASD)** comprises developmental abnormalities of the cornea, iris, lens, and iridocorneal angle. **FOXE3-related ASD** is a genetically defined subset in which abnormal lens development secondarily disrupts anterior segment morphogenesis, producing a spectrum from isolated cataract to severe congenital malformations such as **sclerocornea–microphthalmia–aphakia complex** and/or **Peters anomaly**. FOXE3 expression is lens-restricted, supporting a lens-primary mechanism for many downstream anterior segment findings. (iseri2009seeingclearlythe pages 1-2, iseri2009seeingclearlythe pages 2-3)

### 1.2 Key identifiers
* **Disease OMIM:** **610256** (anterior segment dysgenesis 2 / congenital primary aphakia locus referenced under MIM#610256 in FOXE3 literature). (iseri2009seeingclearlythe pages 2-3, reis2021comprehensivephenotypicand pages 2-2)
* **Causal gene OMIM:** **FOXE3 MIM 601094**. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, iseri2009seeingclearlythe pages 2-3)
* **Genomic locus:** **1p33** for FOXE3. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, iseri2009seeingclearlythe pages 2-3)
* **MONDO / Orphanet / ICD / MeSH:** Not explicitly provided in the retrieved full texts; these should be added via direct lookup in OMIM/Orphanet/MONDO/NCBI MeSH during curation. (iseri2009seeingclearlythe pages 2-3, reis2021comprehensivephenotypicand pages 14-14)

### 1.3 Common synonyms / alternative names
Because FOXE3 variants yield multiple overlapping clinical diagnoses, the phenotype is often reported under:
* **Anterior segment dysgenesis (ASD)**
* **Peters anomaly** (when central corneal opacity with irido-/lenticulo-corneal adhesions is present) (doucette2011anovelnonstop pages 1-2, wowra2024generaltreatmentand pages 1-2)
* **Congenital primary aphakia** (when lens is absent congenitally) (iseri2009seeingclearlythe pages 2-3)
* **Sclerocornea–microphthalmia–aphakia complex** (a severe biallelic FOXE3 phenotype) (plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13)

### 1.4 Evidence source type
Most FOXE3 disease knowledge comes from **aggregated disease-level resources and case series** (families/case reports with sequencing) plus **functional assays** in cell systems, and supporting developmental biology evidence from animal models (e.g., Foxe3/dyl mouse). (semina2001mutationsinthe pages 1-2, reis2021comprehensivephenotypicand pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors
**Genetic (monogenic) etiology:** pathogenic germline variants in **FOXE3**, encoding a forkhead transcription factor critical for lens development. (reis2021comprehensivephenotypicand pages 1-2, iseri2009seeingclearlythe pages 2-3)

### 2.2 Risk factors
* **Family history** of congenital cataract/anterior segment anomalies consistent with **AD** inheritance for C-terminal extension alleles, or **AR** inheritance in consanguineous pedigrees. (doucette2011anovelnonstop pages 1-2, iseri2009seeingclearlythe pages 2-3)
* **Consanguinity** increases risk for **biallelic FOXE3 disease**, illustrated by case-based reports and linkage approaches in consanguineous families. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, iseri2009seeingclearlythe pages 2-3)

### 2.3 Protective factors / gene–environment interactions
No validated protective environmental factors or gene–environment interactions were identified in the retrieved texts for FOXE3-specific disease; most evidence supports a primarily genetic developmental mechanism. (reis2021comprehensivephenotypicand pages 1-2, iseri2009seeingclearlythe pages 2-3)

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum and frequencies (human)
The best quantitative synthesis in the retrieved evidence is from Reis et al. 2021, which explicitly stratifies recessive vs dominant FOXE3 disease:
* **Recessive/biallelic FOXE3:** severe congenital phenotypes with **corneal opacity (90%)**, **sclerocornea (47%)**, **aphakia (83%)**, **microphthalmia (80%)**; when assessed, **aniridia/iris hypoplasia (89%)** and **optic nerve anomalies (60%)** were frequent. (reis2021comprehensivephenotypicand pages 1-2)
* **Dominant FOXE3 (often extension alleles):** usually **normal eye size (96%)**, **cataracts (99%)**, and **variable anterior segment anomalies** with overlap in some individuals (microphthalmia/aphakia/sclerocornea can occur). (reis2021comprehensivephenotypicand pages 1-2)

Figure-based visual evidence for these phenotype distributions is provided in Figure 3 (Reis 2021). (reis2021comprehensivephenotypicand media 2b34c269, reis2021comprehensivephenotypicand media cd18957d)

Additional genotype-phenotype synthesis across the literature:
* Recessive cases predominate in published FOXE3 cohorts (reported **84% recessive vs 16% dominant**), with **severe ocular disease** much more frequent in recessive than dominant cases (**77% vs 5%**), and severity associated with truncating vs missense allele classes. (plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13)

### 3.2 Phenotype characteristics (typical)
**Onset:** Congenital/early childhood (developmental malformation present at birth; cataract may be congenital or progress/manifest later depending on allele class). (reis2021comprehensivephenotypicand pages 1-2, iseri2009seeingclearlythe pages 2-3)

**Progression:** Structural anomalies are generally non-progressive, but vision-threatening sequelae (e.g., amblyopia, glaucoma, corneal graft outcomes) can evolve over time. (wowra2024generaltreatmentand pages 1-2, wowra2024generaltreatmentand pages 4-7)

### 3.3 Suggested HPO terms (examples)
(ontology suggestions; confirm exact mappings during curation)
* Anterior segment dysgenesis — **HP:0000649**
* Peters anomaly — **HP:0000570**
* Corneal opacity — **HP:0007957**
* Sclerocornea — **HP:0000678**
* Microphthalmia — **HP:0000568**
* Aphakia — **HP:0000565**
* Cataract — **HP:0000518**
* Glaucoma — **HP:0000501**
* Iris hypoplasia / aniridia — **HP:0000528 / HP:0000526**
* Optic nerve hypoplasia/anomaly — **HP:0000609**

### 3.4 Quality of life impact
Although FOXE3-specific quality-of-life instrument data were not found in the retrieved texts, the phenotype spectrum includes high-impact outcomes (childhood visual impairment/blindness, multiple surgeries, long-term amblyopia therapy and glaucoma monitoring). For Peters anomaly (a frequent overlapping entity), half of infants/children may achieve “functional vision” after surgical treatment in some series, but severe outcomes including no light perception are also reported. (wowra2024generaltreatmentand pages 7-8, wowra2024generaltreatmentand pages 4-7)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
* **Gene:** **FOXE3** (forkhead box E3), **MIM 601094**, located at **1p33**. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, iseri2009seeingclearlythe pages 2-3)

### 4.2 Pathogenic variant classes and functional consequences
A major current understanding is that **variant class correlates with inheritance mode and severity**:
* **Biallelic recessive disease:** often **truncating (frameshift/nonsense)** or **forkhead-domain missense** variants consistent with reduced FOXE3 function; functional assays show variable impacts on stability/DNA binding/nuclear localization/transcriptional activity depending on substitution/position. (reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13)
* **Dominant disease:** commonly **C-terminal extension/stop-loss (“elongating/non-stop”)** variants; Reis et al. report **dominant-negative characteristics** in functional studies of dominant alleles. (reis2021comprehensivephenotypicand pages 1-2, doucette2011anovelnonstop pages 1-2)

Concrete variant-class examples documented in the literature include missense, truncating frameshift, and stop-loss/extension variants (e.g., FOXE3 p.X320ArgextX72 and related stop-codon disruptions). (iseri2009seeingclearlythe pages 2-3)

### 4.3 Genotype–phenotype correlations (quantitative)
Plaisancié et al. 2018 provides cross-study quantitative synthesis:
* With ≥1 truncating allele: **90% (37/41)** severe ocular phenotype.
* With biallelic missense alleles: **69% (42/61)** severe ocular disease.
* ASD more frequent with two missense alleles (31%; 19/61) than with two truncating alleles (17%; 4/23). (plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No FOXE3-specific modifier-gene or epigenetic disease mechanism evidence was identified in the retrieved texts.

---

## 5. Environmental information
No validated environmental contributors are established for FOXE3-related ASD2 in the retrieved evidence; disease is principally genetic and developmental. (reis2021comprehensivephenotypicand pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
**Upstream:** germline pathogenic variant in **FOXE3**, a lens transcription factor with forkhead DNA-binding domain. (iseri2009seeingclearlythe pages 2-3)

**Intermediate:** disrupted **lens development/maintenance**, leading to abnormal lens epithelium behavior and lens morphogenesis; dominant and recessive alleles differ mechanistically (dominant-negative vs loss-of-function spectrum). (reis2021comprehensivephenotypicand pages 1-2)

**Downstream:** secondary abnormal development of adjacent anterior segment structures (cornea, iris, iridocorneal angle), producing phenotypes such as corneal opacity/sclerocornea, adhesions characteristic of Peters anomaly, and angle abnormalities predisposing to glaucoma. (doucette2011anovelnonstop pages 1-2, wowra2024generaltreatmentand pages 1-2)

### 6.2 Suggested GO biological process terms (examples)
(ontology suggestions; confirm during curation)
* Eye development — **GO:0001654**
* Lens development in camera-type eye — **GO:0002088**
* Anterior/posterior pattern specification (eye) — related developmental GO terms
* Regulation of transcription by RNA polymerase II — **GO:0006357** (FOXE3 as transcription factor)

### 6.3 Suggested cell types (CL) and anatomical sites (UBERON)
(ontology suggestions; confirm during curation)
* **Lens epithelial cell** (CL term; lens anterior epithelium implicated) (iseri2009seeingclearlythe pages 1-2)
* UBERON structures: **lens (UBERON:0000965)**, **cornea (UBERON:0000964)**, **iris (UBERON:0001769)**, **anterior chamber angle / trabecular meshwork / Schlemm canal** (angle structures relevant to glaucoma risk). (wowra2024generaltreatmentand pages 1-2, wowra2024generaltreatmentand pages 2-4)

---

## 7. Anatomical structures affected
**Primary organ:** eye.

**Primary structures:** lens (aphakia/cataract), cornea (opacity/sclerocornea), iris (hypoplasia/aniridia, adhesions), iridocorneal angle (glaucoma risk), optic nerve (anomalies in a subset). (reis2021comprehensivephenotypicand pages 1-2)

**Laterality:** can be bilateral or unilateral depending on allele and phenotype; microphthalmia and Peters anomaly can be unilateral or bilateral in broader ASD cohorts. (reis2021comprehensivephenotypicand pages 2-2, wowra2024generaltreatmentand pages 2-4)

---

## 8. Temporal development
**Onset:** congenital (developmental malformation). (reis2021comprehensivephenotypicand pages 1-2)

**Course:** lifelong structural ocular phenotype; clinical course largely defined by visual axis clarity, amblyopia risk, and management of complications such as glaucoma and corneal graft failure (when present). (wowra2024generaltreatmentand pages 7-8, wowra2024generaltreatmentand pages 4-7)

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
* **Autosomal recessive (biallelic)** FOXE3 disease: typically severe congenital malformations; heterozygous carriers often unaffected. (plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13, reis2021comprehensivephenotypicand pages 2-2)
* **Autosomal dominant** FOXE3 disease: typically cataract with variable ASD features; can show variable expressivity across family members. (doucette2011anovelnonstop pages 1-2, iseri2009seeingclearlythe pages 2-3)

### 9.2 Epidemiology
Direct prevalence/incidence of FOXE3-ASD2 is not provided in the retrieved texts.

However, broader context:
* Developmental eye anomalies collectively have been cited as an important contributor to childhood visual impairment, and anophthalmia/microphthalmia has been reported around 0.6–3.2 per 10,000 in aggregated reviews, with FOXE3 accounting for a small fraction of such cases in some series. (plaisancie2018foxe3mutationsgenotype‐phenotype pages 1-4)

---

## 10. Diagnostics
### 10.1 Clinical evaluation
Common diagnostic components across FOXE3 and related ASD phenotypes include slit-lamp exam, tonometry, gonioscopy, corneal diameter measurement, and ocular biometry/ultrasound; in severe corneal opacity, exam under anesthesia is often needed. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, doucette2011anovelnonstop pages 1-2)

### 10.2 Imaging and ancillary testing
For Peters anomaly (often in the FOXE3 spectrum), 2024 guidance emphasizes:
* **Anterior-segment OCT (AS-OCT)** and **ultrasound biomicroscopy (UBM)**
* **A/B-scan ultrasound** when posterior pathology is suspected
* Gonioscopy and (in some cases) electrophysiology to assess posterior segment function. (wowra2024generaltreatmentand pages 2-4)

### 10.3 Genetic testing (real-world implementation)
#### Gene panels (2023 snapshot)
Commercial panel testing for ASD shows substantial variability:
* Across four ASD panels surveyed, **FOXE3 was included in 100% (4/4)** and **PAX6 in 100% (4/4)**, but other common ASD genes (PITX2/FOXC1/CYP1B1/PITX3) were only present on ~50% of panels; **PXDN** was present on 75%. (procopio2023comparinggenepanels pages 2-4)
* Panel scope varies widely; in a broader non-retinal panel survey, panels ranged from **“1 to 893 genes”** across indications, underscoring the need for careful selection and coverage review. (procopio2023comparinggenepanels pages 4-6)
* Technical sensitivity varies by variant class; some labs report poor reliability for certain structural variants (e.g., CNVs <500 bp, larger indels), and variant interpretation differs among laboratories—supporting genetic counselor involvement. (procopio2023comparinggenepanels pages 6-7)

#### WES-based approaches (2024 cohort evidence)
A 2024 cohort study describing long-term molecular characterization of congenital ocular dysgenesis reports:
* Use of WES in phenotype-overlapping congenital ocular disease and that, after filtering benign variants, **“30.8% patients bore a pathogenic or likely pathogenic aberration in genes known to cause ocular dysgenesis.”** (Journal of Human Genetics; Mar 2024; https://doi.org/10.1038/s10038-024-01237-6) (zucco2024abird’seye pages 3-4)

#### Single-gene testing
Historically, candidate-gene sequencing and positional approaches identified FOXE3 variants in families with congenital aphakia/ASD and informed inclusion of FOXE3 in diagnostic screening. (iseri2009seeingclearlythe pages 2-3)

### 10.4 Differential diagnosis
Genetically heterogeneous ASD disorders include variants in PAX6, PITX2, FOXC1, CYP1B1, PXDN, and others; phenotypic overlap is substantial, supporting broad-panel or exome approaches in many patients. (alkhaldi2023homozygousvariantfoxe3 pages 1-3, procopio2023comparinggenepanels pages 1-2)

---

## 11. Outcome / prognosis
FOXE3-specific long-term prognosis depends on phenotype severity and treatability of complications (glaucoma, corneal opacity, aphakia/cataract, amblyopia).

Because many FOXE3 patients are clinically managed under broader entities (e.g., Peters anomaly), recent outcome statistics for those entities are informative:
* In Peters anomaly, glaucoma is reported in **30–70%** of patients; up to **60%** may have systemic abnormalities/developmental delays, and PA is a common congenital indication for infant corneal transplantation. (wowra2024generaltreatmentand pages 1-2)
* For penetrating keratoplasty in Peters anomaly, published outcomes vary widely (examples reported): graft survival/failure rates including **30% failure at 1 year**, **70% failure at 5 years**, and **77% failure at 10 years** in some series; rejection is a major cause, and congenital/secondary glaucoma predicts graft failure. (wowra2024generaltreatmentand pages 7-8, wowra2024generaltreatmentand pages 4-7)

---

## 12. Treatment
There is no FOXE3 gene-specific therapy in clinical use; management is phenotype-driven and typically multidisciplinary.

### 12.1 Management of key ocular components (current practice)
**Corneal opacity / Peters anomaly-type disease**
* Penetrating keratoplasty (PK) is first-line when corneal opacity prevents visual development; alternatives include optical sector iridectomy, pupil dilation, corneal rotation, and keratoprosthesis in selected cases. (wowra2024generaltreatmentand pages 1-2, wowra2024generaltreatmentand pages 8-10)
* Postoperative priorities: maintain clear visual axis and prevent amblyopia; EUAs used to monitor grafts and IOP; immunosuppression regimens may include topical corticosteroids/cyclosporine A and sometimes systemic agents. (wowra2024generaltreatmentand pages 2-4, wowra2024generaltreatmentand pages 4-7)

**Glaucoma / elevated IOP**
* Medical therapy and surgical options (e.g., cyclophotocoagulation) are used depending on anatomy/severity; an Oman case report of FOXE3-ASD2 documented treatment with anti-glaucoma medications and CPC. (alkhaldi2023homozygousvariantfoxe3 pages 1-3)

**Aphakia / cataract**
* Optical correction (contact lenses/spectacles) and amblyopia therapy are key; in Peters anomaly care pathways, cataract removal and secondary IOL implantation are often deferred until ~2–3 years, with contact lenses for temporary aphakia. (wowra2024generaltreatmentand pages 4-7)

### 12.2 Suggested MAXO terms (examples)
(ontology suggestions; confirm during curation)
* Corneal transplantation / penetrating keratoplasty
* Antiglaucoma pharmacotherapy
* Cyclophotocoagulation
* Lensectomy / cataract extraction
* Amblyopia therapy (occlusion therapy, atropine penalization)
* Contact lens fitting for aphakia

---

## 13. Prevention
Primary prevention is not currently available for a monogenic congenital malformation; however:
* **Genetic counseling** and **cascade testing** are central.
* **Reproductive options** may include prenatal or preimplantation genetic testing once the familial FOXE3 variant(s) are known; panel-testing reviews explicitly note that prenatal/PGT discussion is outside scope but clinically relevant. (procopio2023comparinggenepanels pages 6-7)

---

## 14. Other species / natural disease
The retrieved human-focused evidence did not provide curated naturally occurring FOXE3-related ASD in non-human species; however, vertebrate developmental biology evidence supports conserved Foxe3 function in lens/anterior segment development (see model organisms below). (semina2001mutationsinthe pages 1-2)

---

## 15. Model organisms
The retrieved evidence base includes strong support from mouse developmental genetics:
* The classic dysgenetic lens (**dyl**) mouse mutant has Foxe3 mutations and displays small eyes, corneal opacities, iris adhesions, persistent lens–cornea attachment, and cataracts, aligning with the concept that lens-primary defects drive secondary anterior segment malformations. (semina2001mutationsinthe pages 1-2)

Additional model-organism evidence (e.g., zebrafish foxe3 deficiency) was retrieved in searches but not fully incorporated into the evidence excerpts above; it should be added during extended curation if model details are required. 

---

## Key abstract-supported quotes (for knowledge base evidence items)
* Reis et al. 2021 (Human Molecular Genetics; May 2021; https://doi.org/10.1093/hmg/ddab142): “**Most families with recessive alleles… had severe corneal opacity (90%; sclerocornea in 47%), aphakia (83%) and microphthalmia (80%)…**” (reis2021comprehensivephenotypicand pages 1-2)
* Wowra et al. 2024 (J Clin Med; Jan 2024; https://doi.org/10.3390/jcm13020532): “**Glaucoma is observed in 30–70% of patients**…” and “**Up to 60% of patients have systemic abnormalities or developmental delays**…” (wowra2024generaltreatmentand pages 1-2)
* Zucco et al. 2024 (J Hum Genet; Mar 2024; https://doi.org/10.1038/s10038-024-01237-6): “**After ﬁltering benign and likely benign variants, 30.8% patients bore a pathogenic or likely pathogenic aberration in genes known to cause ocular dysgenesis.**” (zucco2024abird’seye pages 3-4)

---

## Embedded summary artifact
The following table consolidates inheritance patterns, variant classes, phenotype patterns, and key quantitative frequencies.

| Inheritance mode | Typical phenotype pattern | Variant classes / inferred mechanism | Key quantitative phenotype data | Key citations |
|---|---|---|---|---|
| Autosomal recessive / biallelic FOXE3-related disease | Usually more severe congenital ocular malformations: dense corneal opacity, sclerocornea, primary aphakia, microphthalmia; frequent iris hypoplasia/aniridia and optic nerve anomalies; may include Peters-like anterior segment dysgenesis, cataract, and occasional extraocular findings | Typically truncating variants (nonsense, frameshift) throughout the single-exon gene and missense variants in the forkhead DNA-binding domain; overall most consistent with loss of function, though missense alleles show variable functional effects on protein stability, DNA binding, nuclear localization, and transcriptional activity | Reis 2021: corneal opacity 90%, sclerocornea 47%, aphakia 83%, microphthalmia 80%, aniridia/iris hypoplasia 89% (when assessed), optic nerve anomalies 60% (when assessed). Plaisancié 2018: recessive cases 84% of reported FOXE3 families; severe ocular phenotype in 77% of recessive cases; among patients with ≥1 truncating allele, 90% (37/41) had severe ocular disease; among biallelic missense cases, 69% (42/61) had severe ocular disease; ASD reported in 31% (19/61) of biallelic missense vs 17% (4/23) with two truncating variants (reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) | (reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) |
| Autosomal dominant FOXE3-related disease | Typically milder and more variable anterior segment disease with congenital/early-onset cataract, Peters anomaly, iris abnormalities, microcornea, corneal scleralization, and occasional coloboma; most individuals have normal eye size, but overlap with recessive features can occur | Most often C-terminal extension / non-stop / elongating variants affecting or near the stop codon; dominant alleles show severe impairment in multiple functional assays and dominant-negative behavior in Reis 2021, while earlier genotype reviews also discuss possible gain-of-function effects for elongating alleles | Reis 2021: normal eye size 96%, cataract 99% in dominant pedigrees, with variable anterior segment anomalies. Plaisancié 2018: dominant cases 16% of reported FOXE3 families; severe ocular phenotype in 5% of dominant cases. Newfoundland pedigree: 11 affected among 31 examined relatives in a 4-generation family with a non-stop variant and variable ASD including Peters anomaly (reis2021comprehensivephenotypicand pages 1-2, doucette2011anovelnonstop pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) | (reis2021comprehensivephenotypicand pages 1-2, doucette2011anovelnonstop pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) |
| Genotype-phenotype overlap across AD and AR disease | Considerable overlap exists: cataract, anterior segment dysgenesis, Peters anomaly, aphakia, sclerocornea, and microphthalmia can occur in either inheritance class, although severity trends differ | Recessive missense alleles can be milder than recessive truncating alleles; dominant extension alleles usually milder but can occasionally produce features more typical of recessive disease | Reis 2021 identified overlap between dominant and recessive disease and noted that some recessive cases had isolated cataract, while some dominant individuals had microphthalmia, aphakia, or sclerocornea. Plaisancié 2018 concluded that mutation type, inheritance mode, and severity are correlated but not absolute (plaisancie2018foxe3mutationsgenotype‐phenotype pages 1-4, reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) | (plaisancie2018foxe3mutationsgenotype‐phenotype pages 1-4, reis2021comprehensivephenotypicand pages 1-2, plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13) |


*Table: This table summarizes the main genotype-phenotype patterns in FOXE3-related anterior segment dysgenesis, contrasting autosomal recessive/biallelic and autosomal dominant disease. It highlights the typical clinical presentations, variant classes and mechanisms, and the most useful quantitative phenotype frequencies from key studies.*

---

## Limitations and curation notes
* **MONDO/Orphanet/ICD/MeSH identifiers** were not retrievable from the full texts accessed here and should be completed by direct database lookup during knowledge base normalization. (iseri2009seeingclearlythe pages 2-3)
* Many treatment/outcome statistics come from **Peters anomaly management literature** (2024) rather than FOXE3-genotype-stratified cohorts; however, these are clinically relevant because Peters anomaly is a common manifestation within the FOXE3 spectrum. (wowra2024generaltreatmentand pages 1-2, wowra2024generaltreatmentand pages 7-8)
* Variant-level details (HGVS for all known FOXE3 alleles, allele frequencies in gnomAD, ClinVar assertions) require direct ClinVar/gnomAD extraction; Reis et al. note FOXE3 alleles are rare/absent in gnomAD but full frequencies were not present in the excerpted evidence. (reis2021comprehensivephenotypicand pages 1-2)


References

1. (reis2021comprehensivephenotypicand pages 1-2): Linda M Reis, Elena A Sorokina, Lubica Dudakova, Jana Moravikova, Pavlina Skalicka, Frantisek Malinka, Sarah E Seese, Samuel Thompson, Tanya Bardakjian, Jenina Capasso, William Allen, Tom Glaser, Alex V Levin, Adele Schneider, Ayesha Khan, Petra Liskova, and Elena V Semina. Comprehensive phenotypic and functional analysis of dominant and recessive foxe3 alleles in ocular developmental disorders. Human Molecular Genetics, 30:1591-1606, May 2021. URL: https://doi.org/10.1093/hmg/ddab142, doi:10.1093/hmg/ddab142. This article has 22 citations and is from a domain leading peer-reviewed journal.

2. (plaisancie2018foxe3mutationsgenotype‐phenotype pages 8-13): Julie Plaisancié, N. Ragge, H. Dollfus, J. Kaplan, D. Lehalle, C. Francannet, G. Morin, H. Colineaux, P. Calvas, and N. Chassaing. Foxe3 mutations: genotype‐phenotype correlations. Clinical Genetics, 93:837-845, Apr 2018. URL: https://doi.org/10.1111/cge.13177, doi:10.1111/cge.13177. This article has 42 citations and is from a peer-reviewed journal.

3. (iseri2009seeingclearlythe pages 2-3): Sibel Ugur Iseri, Robert J. Osborne, Martin Farrall, Alexander William Wyatt, Ghazala Mirza, Gudrun Nürnberg, Christian Kluck, Helen Herbert, Angela Martin, Muhammad Sajid Hussain, J. Richard O. Collin, Mark Lathrop, Peter Nürnberg, Jiannis Ragoussis, and Nicola K. Ragge. Seeing clearly: the dominant and recessive nature of foxe3 in eye developmental anomalies. Human Mutation, 30:1378-1386, Oct 2009. URL: https://doi.org/10.1002/humu.21079, doi:10.1002/humu.21079. This article has 109 citations and is from a domain leading peer-reviewed journal.

4. (wowra2024generaltreatmentand pages 1-2): Bogumil Wowra, Dariusz Dobrowolski, Mohit Parekh, and Edward Wylęgała. General treatment and ophthalmic management of peters’ anomaly. Journal of Clinical Medicine, 13:532, Jan 2024. URL: https://doi.org/10.3390/jcm13020532, doi:10.3390/jcm13020532. This article has 6 citations.

5. (procopio2023comparinggenepanels pages 1-2): Rebecca Procopio, Jose S. Pulido, Kammi B. Gunton, Zeba A. Syed, Daniel Lee, Mark L. Moster, Robert Sergott, Julie A. Neidich, and Margaret M. Reynolds. Comparing gene panels for non-retinal indications: a systematic review. Genes, 14:738, Mar 2023. URL: https://doi.org/10.3390/genes14030738, doi:10.3390/genes14030738. This article has 0 citations.

6. (zucco2024abird’seye pages 3-4): Jessica Zucco, Federica Baldan, Lorenzo Allegri, Elisa Bregant, Nadia Passon, Alessandra Franzoni, Angela Valentina D’Elia, Flavio Faletra, Giuseppe Damante, and Catia Mio. A bird’s eye view on the use of whole exome sequencing in rare congenital ophthalmic diseases. Journal of Human Genetics, 69:271-282, Mar 2024. URL: https://doi.org/10.1038/s10038-024-01237-6, doi:10.1038/s10038-024-01237-6. This article has 9 citations and is from a peer-reviewed journal.

7. (iseri2009seeingclearlythe pages 1-2): Sibel Ugur Iseri, Robert J. Osborne, Martin Farrall, Alexander William Wyatt, Ghazala Mirza, Gudrun Nürnberg, Christian Kluck, Helen Herbert, Angela Martin, Muhammad Sajid Hussain, J. Richard O. Collin, Mark Lathrop, Peter Nürnberg, Jiannis Ragoussis, and Nicola K. Ragge. Seeing clearly: the dominant and recessive nature of foxe3 in eye developmental anomalies. Human Mutation, 30:1378-1386, Oct 2009. URL: https://doi.org/10.1002/humu.21079, doi:10.1002/humu.21079. This article has 109 citations and is from a domain leading peer-reviewed journal.

8. (reis2021comprehensivephenotypicand pages 2-2): Linda M Reis, Elena A Sorokina, Lubica Dudakova, Jana Moravikova, Pavlina Skalicka, Frantisek Malinka, Sarah E Seese, Samuel Thompson, Tanya Bardakjian, Jenina Capasso, William Allen, Tom Glaser, Alex V Levin, Adele Schneider, Ayesha Khan, Petra Liskova, and Elena V Semina. Comprehensive phenotypic and functional analysis of dominant and recessive foxe3 alleles in ocular developmental disorders. Human Molecular Genetics, 30:1591-1606, May 2021. URL: https://doi.org/10.1093/hmg/ddab142, doi:10.1093/hmg/ddab142. This article has 22 citations and is from a domain leading peer-reviewed journal.

9. (alkhaldi2023homozygousvariantfoxe3 pages 1-3): Zuha Alkhaldi, Moosa Allawati, and Nadia Alhashmi. Homozygous variant foxe3 causes autosomal recessive anterior segment dysgenesis type 2: a case report. Journal of Biochemical and Clinical Genetics, pages 75-79, Jan 2023. URL: https://doi.org/10.24911/jbcgenetics/183-1670866871, doi:10.24911/jbcgenetics/183-1670866871. This article has 0 citations.

10. (reis2021comprehensivephenotypicand pages 14-14): Linda M Reis, Elena A Sorokina, Lubica Dudakova, Jana Moravikova, Pavlina Skalicka, Frantisek Malinka, Sarah E Seese, Samuel Thompson, Tanya Bardakjian, Jenina Capasso, William Allen, Tom Glaser, Alex V Levin, Adele Schneider, Ayesha Khan, Petra Liskova, and Elena V Semina. Comprehensive phenotypic and functional analysis of dominant and recessive foxe3 alleles in ocular developmental disorders. Human Molecular Genetics, 30:1591-1606, May 2021. URL: https://doi.org/10.1093/hmg/ddab142, doi:10.1093/hmg/ddab142. This article has 22 citations and is from a domain leading peer-reviewed journal.

11. (doucette2011anovelnonstop pages 1-2): Lance Doucette, Jane Green, Bridget Fernandez, Gordon J Johnson, Patrick Parfrey, and Terry-Lynn Young. A novel, non-stop mutation in foxe3 causes an autosomal dominant form of variable anterior segment dysgenesis including peters anomaly. European Journal of Human Genetics, 19:293-299, Mar 2011. URL: https://doi.org/10.1038/ejhg.2010.210, doi:10.1038/ejhg.2010.210. This article has 55 citations and is from a domain leading peer-reviewed journal.

12. (semina2001mutationsinthe pages 1-2): E. Semina, Isaac Brownell, H. Mintz‐Hittner, Jeffrey C. Murray, and M. Jamrich. Mutations in the human forkhead transcription factor foxe3 associated with anterior segment ocular dysgenesis and cataracts. Human molecular genetics, 10 3:231-6, Feb 2001. URL: https://doi.org/10.1093/hmg/10.3.231, doi:10.1093/hmg/10.3.231. This article has 239 citations and is from a domain leading peer-reviewed journal.

13. (reis2021comprehensivephenotypicand media 2b34c269): Linda M Reis, Elena A Sorokina, Lubica Dudakova, Jana Moravikova, Pavlina Skalicka, Frantisek Malinka, Sarah E Seese, Samuel Thompson, Tanya Bardakjian, Jenina Capasso, William Allen, Tom Glaser, Alex V Levin, Adele Schneider, Ayesha Khan, Petra Liskova, and Elena V Semina. Comprehensive phenotypic and functional analysis of dominant and recessive foxe3 alleles in ocular developmental disorders. Human Molecular Genetics, 30:1591-1606, May 2021. URL: https://doi.org/10.1093/hmg/ddab142, doi:10.1093/hmg/ddab142. This article has 22 citations and is from a domain leading peer-reviewed journal.

14. (reis2021comprehensivephenotypicand media cd18957d): Linda M Reis, Elena A Sorokina, Lubica Dudakova, Jana Moravikova, Pavlina Skalicka, Frantisek Malinka, Sarah E Seese, Samuel Thompson, Tanya Bardakjian, Jenina Capasso, William Allen, Tom Glaser, Alex V Levin, Adele Schneider, Ayesha Khan, Petra Liskova, and Elena V Semina. Comprehensive phenotypic and functional analysis of dominant and recessive foxe3 alleles in ocular developmental disorders. Human Molecular Genetics, 30:1591-1606, May 2021. URL: https://doi.org/10.1093/hmg/ddab142, doi:10.1093/hmg/ddab142. This article has 22 citations and is from a domain leading peer-reviewed journal.

15. (wowra2024generaltreatmentand pages 4-7): Bogumil Wowra, Dariusz Dobrowolski, Mohit Parekh, and Edward Wylęgała. General treatment and ophthalmic management of peters’ anomaly. Journal of Clinical Medicine, 13:532, Jan 2024. URL: https://doi.org/10.3390/jcm13020532, doi:10.3390/jcm13020532. This article has 6 citations.

16. (wowra2024generaltreatmentand pages 7-8): Bogumil Wowra, Dariusz Dobrowolski, Mohit Parekh, and Edward Wylęgała. General treatment and ophthalmic management of peters’ anomaly. Journal of Clinical Medicine, 13:532, Jan 2024. URL: https://doi.org/10.3390/jcm13020532, doi:10.3390/jcm13020532. This article has 6 citations.

17. (wowra2024generaltreatmentand pages 2-4): Bogumil Wowra, Dariusz Dobrowolski, Mohit Parekh, and Edward Wylęgała. General treatment and ophthalmic management of peters’ anomaly. Journal of Clinical Medicine, 13:532, Jan 2024. URL: https://doi.org/10.3390/jcm13020532, doi:10.3390/jcm13020532. This article has 6 citations.

18. (plaisancie2018foxe3mutationsgenotype‐phenotype pages 1-4): Julie Plaisancié, N. Ragge, H. Dollfus, J. Kaplan, D. Lehalle, C. Francannet, G. Morin, H. Colineaux, P. Calvas, and N. Chassaing. Foxe3 mutations: genotype‐phenotype correlations. Clinical Genetics, 93:837-845, Apr 2018. URL: https://doi.org/10.1111/cge.13177, doi:10.1111/cge.13177. This article has 42 citations and is from a peer-reviewed journal.

19. (procopio2023comparinggenepanels pages 2-4): Rebecca Procopio, Jose S. Pulido, Kammi B. Gunton, Zeba A. Syed, Daniel Lee, Mark L. Moster, Robert Sergott, Julie A. Neidich, and Margaret M. Reynolds. Comparing gene panels for non-retinal indications: a systematic review. Genes, 14:738, Mar 2023. URL: https://doi.org/10.3390/genes14030738, doi:10.3390/genes14030738. This article has 0 citations.

20. (procopio2023comparinggenepanels pages 4-6): Rebecca Procopio, Jose S. Pulido, Kammi B. Gunton, Zeba A. Syed, Daniel Lee, Mark L. Moster, Robert Sergott, Julie A. Neidich, and Margaret M. Reynolds. Comparing gene panels for non-retinal indications: a systematic review. Genes, 14:738, Mar 2023. URL: https://doi.org/10.3390/genes14030738, doi:10.3390/genes14030738. This article has 0 citations.

21. (procopio2023comparinggenepanels pages 6-7): Rebecca Procopio, Jose S. Pulido, Kammi B. Gunton, Zeba A. Syed, Daniel Lee, Mark L. Moster, Robert Sergott, Julie A. Neidich, and Margaret M. Reynolds. Comparing gene panels for non-retinal indications: a systematic review. Genes, 14:738, Mar 2023. URL: https://doi.org/10.3390/genes14030738, doi:10.3390/genes14030738. This article has 0 citations.

22. (wowra2024generaltreatmentand pages 8-10): Bogumil Wowra, Dariusz Dobrowolski, Mohit Parekh, and Edward Wylęgała. General treatment and ophthalmic management of peters’ anomaly. Journal of Clinical Medicine, 13:532, Jan 2024. URL: https://doi.org/10.3390/jcm13020532, doi:10.3390/jcm13020532. This article has 6 citations.