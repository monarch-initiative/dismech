---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T08:45:44.349192'
end_time: '2026-05-09T08:55:56.337513'
duration_seconds: 611.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Multiple Pterygium Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Multiple Pterygium Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Multiple Pterygium Syndrome** covering all of the
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
- **Disease Name:** Autosomal Recessive Multiple Pterygium Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Multiple Pterygium Syndrome** covering all of the
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


# Disease Characteristics Research Report: Autosomal Recessive Multiple Pterygium Syndrome (AR MPS; Escobar syndrome)

## Executive summary
Autosomal recessive multiple pterygium syndrome (AR MPS) is a rare congenital contracture/webbing disorder within the arthrogryposis multiplex congenita spectrum, typically caused by biallelic pathogenic variants affecting fetal neuromuscular junction (NMJ) function (classically the fetal acetylcholine receptor γ-subunit gene **CHRNG**), leading to decreased fetal movement (fetal akinesia) and permanent musculoskeletal sequelae (pterygia, contractures, scoliosis). (dahanoliel2021theclinicaland pages 1-2, kariminejad2016truncatingchrngmutations pages 1-2)

| Subtype / gene context | Inheritance | Mechanistic note | Hallmark phenotypes | Prenatal clues | Key supporting citation(s) |
|---|---|---|---|---|---|
| Nonlethal multiple pterygium syndrome (Escobar syndrome) | Usually autosomal recessive | Often linked to fetal neuromuscular junction dysfunction; CHRNG encodes the fetal AChR γ subunit, expressed prenatally and replaced by ε later in gestation, so prenatal injury can be permanent despite absent postnatal myasthenia | Multiple pterygia/webbing, congenital joint contractures/arthrogryposis, scoliosis/kyphoscoliosis, foot deformities, facial dysmorphism (micrognathia, ptosis, low-set ears, down-slanting palpebral fissures) | Decreased fetal movement; prenatal ultrasound may show contractures; prenatal diagnosis reported for both forms | Dahan-Oliel et al. 2021, https://doi.org/10.3390/genes12081220; Bissinger & Koch 2014, https://doi.org/10.1097/anc.0000000000000039; Sandweiss et al. 2022, https://doi.org/10.1055/s-0040-1715640 (dahanoliel2021theclinicaland pages 1-2, bissinger2014nonlethalmultiplepterygium pages 1-2, sandweiss2022atruncatingvariant pages 1-2) |
| Lethal multiple pterygium syndrome (LMPS) | Autosomal recessive | Severe prenatal fetal akinesia spectrum; associated with pathogenic variants in fetal AChR pathway genes and other neuromuscular genes | Prenatal growth deficiency, multiple pterygia, severe contractures, spine defects, facial anomalies; pulmonary hypoplasia is a key severe feature | Cystic hygroma, hydrops fetalis, markedly increased nuchal translucency, edema, fixed limb deformities, absent nasal bone, micrognathia; frequent ultrasound abnormalities | Chen et al. 2023, https://doi.org/10.3389/fgene.2023.1005624; Mohtisham et al. 2019, https://doi.org/10.1136/bcr-2018-229045 (chen2023casereportearly pages 1-2, vogt2017clinicalandmolecular pages 84-88) |
| CHRNG (major AR Escobar/nonlethal gene; also lethal) | Autosomal recessive | Encodes embryonic/fetal nicotinic AChR γ subunit; loss of function causes transient prenatal NMJ failure, fetal akinesia, prenatal muscle weakness, contractures, and pterygia; postnatal weakness usually absent because γ is replaced by ε | Contractures, pterygia, scoliosis, facial dysmorphism; stable course in nonlethal cases; muscle bulk reduction on WBMRI | Reduced fetal movement; oligohydramnios/polyhydramnios and ultrasound-detected contractures reported; increased abortions/stillbirths in some families | Kariminejad et al. 2016, https://doi.org/10.1186/s12863-016-0382-5; Carrera-García et al. 2019, https://doi.org/10.1002/ajmg.a.61122; Vogt et al. 2012, https://doi.org/10.1136/jmedgenet-2011-100378 (kariminejad2016truncatingchrngmutations pages 1-2, carrera‐garcia2019chrng‐relatednonlethalmultiple pages 2-3, carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2) |
| CHRND | Autosomal recessive | Encodes AChR δ subunit; pathogenic variants can cause LMPS and other congenital myasthenic phenotypes | LMPS with multiple pterygia, contractures, micrognathia | First-trimester case: cystic hygroma, NT 11 mm, edema, fixed knee/elbow flexion, vertical wrists, absent nasal bone; 3D facial angle used for micrognathia assessment | Chen et al. 2023, https://doi.org/10.3389/fgene.2023.1005624 (chen2023casereportearly pages 1-2) |
| CHRNA1 / CHRNB1 / CHRND (AChR subunit group) | Autosomal recessive | Fetal AChR pathway genes implicated in MPS/fetal akinesia; disruption of fetal NMJ causes severe in utero akinesia and arthrogryposis spectrum | Multiple pterygium syndrome / fetal akinesia / arthrogryposis spectrum | Prenatal clues not separated by gene in retrieved evidence | Dahan-Oliel et al. 2021, https://doi.org/10.3390/genes12081220; Vogt 2017, Not in retrieved evidence for DOI URL (dahanoliel2021theclinicaland pages 13-14, vogt2017clinicalandmolecular pages 152-157) |
| MYH3 (recessive cases mimicking Escobar; also dominant MPS in other reports) | Recessive in mimicking Escobar cases; dominant forms also reported | Embryonic myosin heavy chain gene; recessive variants cause contractures, pterygia, and variable skeletal fusions syndrome 1B, clinically overlapping Escobar; MYH3-related cases can have severe/malignant scoliosis | Multiple pterygia, mild flexion contractures, vertebral anomalies, skeletal fusions, severe scoliosis in some cases | Prenatal clues not in retrieved evidence for MYH3-specific AR MPS | Hakonen et al. 2020, https://doi.org/10.1002/ajmg.a.61836; Dahan-Oliel et al. 2021, https://doi.org/10.3390/genes12081220 (hakonen2020recessivemyh3variants pages 1-2, dahanoliel2021theclinicaland pages 10-12) |
| TPM2 | Not in retrieved evidence | Reported as one of the genes associated with nonlethal MPS/Escobar in literature cited by case series; mechanistic detail not given in retrieved evidence | Nonlethal MPS/Escobar association noted | Not in retrieved evidence | Dahan-Oliel et al. 2021, https://doi.org/10.3390/genes12081220 (dahanoliel2021theclinicaland pages 10-12) |
| RAPSN | Not in retrieved evidence | AChR-related NMJ gene; homozygous pathogenic variants reported in families with severe lethal fetal akinesia / MPS spectrum | In small series, severe lethal fetal akinesia; pterygia may be absent | Not in retrieved evidence | Vogt 2017, Not in retrieved evidence for DOI URL (vogt2017clinicalandmolecular pages 152-157) |
| DOK7 | Not in retrieved evidence | NMJ gene; homozygous pathogenic variants reported in families with severe lethal fetal akinesia / MPS spectrum | In small series, severe lethal fetal akinesia; pterygia may be absent | Not in retrieved evidence | Vogt 2017, Not in retrieved evidence for DOI URL (vogt2017clinicalandmolecular pages 152-157) |


*Table: This table compacts the retrieved evidence on autosomal recessive multiple pterygium syndrome into subtype- and gene-level entries, linking inheritance, mechanism, phenotype, prenatal clues, and supporting citations. It is useful as a quick evidence-backed reference for knowledge base curation.*

---

## 1. Disease information
### 1.1 Overview / definition
Multiple pterygium syndrome (MPS) is defined in a pediatric case series as “**a genetically heterogeneous rare form of arthrogryposis multiplex congenita characterized by joint contractures and webbing or pterygia, as well as distinctive facial features related to diminished fetal movement**.” (Dahan-Oliel et al., *Genes*, publication month Aug 2021; https://doi.org/10.3390/genes12081220) (dahanoliel2021theclinicaland pages 1-2)

MPS is classically divided into:
- **Nonlethal/Escobar variant** (Escobar syndrome; “Escobar variant MPS”) and
- **Prenatally lethal / lethal MPS**, often within the fetal akinesia deformation sequence (FADS) spectrum. (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 84-88)

### 1.2 Key identifiers (retrieved evidence)
- **OMIM (MIM) IDs (as cited in peer-reviewed literature):**
  - **Escobar (nonlethal) MPS:** **MIM 265000** (dahanoliel2021theclinicaland pages 1-2)
  - **Lethal MPS:** **MIM 253290** (dahanoliel2021theclinicaland pages 1-2)
- **MONDO ID:** Not found in retrieved evidence.
- **Orphanet ID / ICD-10/ICD-11 / MeSH:** Not found in retrieved evidence.

### 1.3 Synonyms / alternative names
- **Escobar syndrome** = nonlethal MPS (Escobar variant). (bissinger2014nonlethalmultiplepterygium pages 1-2, gurung2024nonlethalmultiplepterygium pages 1-3)
- **Lethal multiple pterygium syndrome (LMPS)**. (chen2023casereportearly pages 1-2)

### 1.4 Evidence source type
The retrieved evidence is primarily **aggregated disease knowledge from peer-reviewed reviews/case series** and **primary evidence from case reports/series** (prenatal imaging, genetics, orthopedic management). (dahanoliel2021theclinicaland pages 1-2, chen2023casereportearly pages 1-2, gurung2024nonlethalmultiplepterygium pages 1-3)

---

## 2. Etiology
### 2.1 Disease causal factors (genetic)
AR MPS is most often genetic and usually autosomal recessive in inheritance (dahanoliel2021theclinicaland pages 1-2, bissinger2014nonlethalmultiplepterygium pages 1-2, gurung2024nonlethalmultiplepterygium pages 1-3).

**Major causal gene (most established for Escobar/nonlethal AR MPS):**
- **CHRNG** (encodes fetal/embryonic AChR γ subunit). CHRNG mutations are repeatedly stated to cause autosomal recessive MPS. (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2, kariminejad2016truncatingchrngmutations pages 1-2)

**Other NMJ pathway genes implicated in severe/lethal MPS/FADS-spectrum presentations (from retrieved evidence):**
- **CHRND** (AChR δ subunit) – 2023 case report with two novel variants (below). (chen2023casereportearly pages 1-2)
- **CHRNA1, CHRNB1, CHRND** discussed as AChR subunit genes in the MPS/fetal akinesia differential and candidate sequencing sets. (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 152-157)
- **RAPSN, DOK7** (NMJ genes) detected in families with severe fetal akinesia in a genetics dissertation-style cohort summary. (vogt2017clinicalandmolecular pages 152-157)

**Genetic heterogeneity / mimic phenotypes:**
- **MYH3**: Recessive MYH3 variants can produce a clinical phenotype mimicking Escobar variant MPS (“contractures, pterygia, and variable skeletal fusions syndrome 1B”). (Hakonen et al., Sep 2020; https://doi.org/10.1002/ajmg.a.61836) (hakonen2020recessivemyh3variants pages 1-2)
- **TPM2**: Named as one of the (literature) genes associated with non-lethal MPS/Escobar in a scoliosis case series discussion. (dahanoliel2021theclinicaland pages 10-12)

### 2.2 Risk factors
- **Genetic:** parental carrier status for autosomal recessive NMJ genes; consanguinity can be present in CHRNG-positive families (reported in a cohort comparison). (vogt2017clinicalandmolecular pages 84-88)
- **Environmental:** No specific environmental risk factors were identified in retrieved evidence beyond hypothesized modifiers affecting severity. (kariminejad2016truncatingchrngmutations pages 1-2)

### 2.3 Protective factors
No protective genetic/environmental factors were identified in retrieved evidence.

### 2.4 Gene–environment interaction
A CHRNG study reports that “**genetic background and environmental modifiers might be of significance**” for severity along the lethal–nonlethal spectrum. (Kariminejad et al., May 2016; https://doi.org/10.1186/s12863-016-0382-5) (kariminejad2016truncatingchrngmutations pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (human)
Across sources, the phenotype is dominated by congenital webbing (pterygia) and contractures:
- **Pterygia/webbing**: neck, antecubital fossae, popliteal fossae, axillae, and digits are commonly described. (bissinger2014nonlethalmultiplepterygium pages 1-2, dahanoliel2021theclinicaland pages 1-2)
- **Congenital joint contractures / arthrogryposis** (often multiple joints; elbow/knee flexion): emphasized as a defining feature. (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 84-88)
- **Scoliosis/kyphoscoliosis**: common and clinically important; scoliosis prevalence in Escobar syndrome reported as **32%–93%** in a 12-child series discussion. (dahanoliel2021theclinicaland pages 10-12)
- **Craniofacial features**: micrognathia, ptosis, down-slanting palpebral fissures, low-set ears, cleft palate (cleft palate more common in lethal cases in one cohort summary). (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 84-88)
- **Lethal presentations**: pulmonary hypoplasia, hydrops/cystic hygroma, severe fetal akinesia. (vogt2017clinicalandmolecular pages 84-88, chen2023casereportearly pages 1-2)

### 3.2 Phenotype characteristics
- **Onset:** congenital (prenatal); reduced fetal movements are central to pathogenesis and prenatal detection. (bissinger2014nonlethalmultiplepterygium pages 1-2, dahanoliel2021theclinicaland pages 1-2)
- **Course:** CHRNG-related nonlethal MPS described as having a “**stable clinical course over the years**” in a long-term follow-up cohort. (Carrera-García et al., Mar 2019; https://doi.org/10.1002/ajmg.a.61122) (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2)
- **Severity:** ranges from nonlethal with lifelong orthopedic disability to prenatal/neonatal lethal forms (pulmonary hypoplasia). (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 84-88)

### 3.3 Quality of life impact (evidence-limited)
Direct validated QoL statistics (EQ-5D, SF-36, PROMIS) were not found in retrieved evidence. The orthopedic and rehabilitation-oriented sources emphasize long-term functional limitations and the need for multidisciplinary management (orthopedics, physiotherapy, assistive devices). (gurung2024nonlethalmultiplepterygium pages 1-3, dahanoliel2021theclinicaland pages 10-12)

### 3.4 Suggested HPO terms (not exhaustive)
(Phenotype terms are ontology suggestions; frequencies are not systematically available in retrieved evidence unless stated.)
- Multiple pterygia / webbing: **HP:0001059 (Pterygium)**; **HP:0000465 (Neck pterygium)**
- Arthrogryposis / contractures: **HP:0002804 (Arthrogryposis multiplex congenita)**; **HP:0001371 (Flexion contracture of joint)**
- Scoliosis/kyphoscoliosis: **HP:0002650 (Scoliosis)**; **HP:0002751 (Kyphoscoliosis)**
- Facial anomalies: **HP:0000347 (Micrognathia)**; **HP:0000508 (Ptosis)**; **HP:0000431 (Wide nasal bridge)**; **HP:0000175 (Cleft palate)**
- Fetal akinesia: **HP:0001558 (Decreased fetal movement)**
- Hydrops/cystic hygroma (lethal): **HP:0001789 (Hydrops fetalis)**; **HP:0000476 (Cystic hygroma)**
- Pulmonary hypoplasia: **HP:0002089 (Pulmonary hypoplasia)**

---

## 4. Genetic / molecular information
### 4.1 Causal genes and variant classes (retrieved)
**CHRNG (AR; nonlethal and lethal):**
- Truncating (frameshift) variants identified by WES in nonlethal Escobar variant families. (kariminejad2016truncatingchrngmutations pages 1-2)
- Case report example: homozygous truncating variant **CHRNG c.117dupC** in Escobar syndrome. (Sandweiss et al., 2022; https://doi.org/10.1055/s-0040-1715640) (sandweiss2022atruncatingvariant pages 1-2)

**CHRND (AR; lethal MPS):**
- 2023 prenatal case report: two novel variants **NM_000751.2: c.1006C>T p.(Arg336Ter)** and **c.973_975delGTG p.(Val325del)**. (Chen et al., Jan 2023; https://doi.org/10.3389/fgene.2023.1005624) (chen2023casereportearly pages 1-2)

**MYH3 (recessive Escobar-like):**
- Recessive MYH3 variants in four patients included **c.1053C>G p.(Tyr351Ter)** and **c.3102+5G>C**, in compound heterozygosity with a hypomorphic **c.-9+1G>A** allele. (Hakonen et al., Sep 2020; https://doi.org/10.1002/ajmg.a.61836) (hakonen2020recessivemyh3variants pages 1-2)

**Other genes in differential (NMJ):**
CHRNA1, CHRNB1, CHRND, RAPSN, DOK7 are repeatedly implicated/considered within NMJ-related fetal akinesia/MPS workups. (dahanoliel2021theclinicaland pages 1-2, vogt2017clinicalandmolecular pages 152-157)

### 4.2 Allele frequencies / population data
gnomAD or other population allele frequencies were not retrieved in the provided evidence.

### 4.3 Functional consequences (current understanding)
- For CHRNG, the evidence supports **loss of fetal NMJ function** during a key developmental window, producing irreversible contractures and pterygia. (dahanoliel2021theclinicaland pages 1-2, kariminejad2016truncatingchrngmutations pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
- Candidate modifier genes are mentioned in other arthrogryposis contexts, but explicit validated modifier genes for AR MPS were not established in retrieved evidence.
- A case report notes the prior report of **uniparental disomy of chromosome 2 carrying a CHRND pathogenic variant** in LMPS, suggesting unusual inheritance mechanisms can occur. (chen2023casereportearly pages 1-2)

---

## 5. Environmental information
No specific environmental toxins, lifestyle contributors, or infectious triggers were identified in retrieved evidence. The condition is predominantly Mendelian with possible nonspecific modifiers. (kariminejad2016truncatingchrngmutations pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (NMJ-centered model)
A mechanistic statement supported by multiple sources is:
1) **Fetal/embryonic AChR subunit dysfunction** (especially CHRNG; also CHRND and other NMJ genes) →
2) **Impaired fetal neuromuscular transmission** (“prenatal myasthenia”) →
3) **Reduced fetal movement (fetal akinesia)** →
4) **Secondary deformation sequence**: pterygia/webbing, congenital contractures/arthrogryposis, scoliosis and other skeletal deformities. (dahanoliel2021theclinicaland pages 1-2, kariminejad2016truncatingchrngmutations pages 1-2, vogt2017clinicalandmolecular pages 152-157)

A key developmental-timing concept is that **CHRNG encodes the fetal γ subunit that is replaced by ε late in gestation (~33 weeks)**; thus, postnatal NMJ transmission may be relatively normal even though fetal injury yields permanent orthopedic manifestations. (dahanoliel2021theclinicaland pages 1-2, sandweiss2022atruncatingvariant pages 1-2)

### 6.2 Tissue/cell/process mapping (ontology suggestions)
**GO biological process terms (suggested):**
- Neuromuscular synaptic transmission: GO:0007274
- Regulation of synapse organization: GO:0050807
- Skeletal muscle contraction: GO:0006936
- Embryonic morphogenesis / limb development (broad): GO:0048598

**Cell Ontology (CL) terms (suggested):**
- Skeletal muscle myocyte: **CL:0000187**
- Motor neuron: **CL:0000100**

**Pathway framing (high-level):** NMJ signaling (AChR assembly/signaling) and downstream musculoskeletal development impacted by mechanical loading/movement. (dahanoliel2021theclinicaland pages 1-2, kariminejad2016truncatingchrngmutations pages 1-2)

### 6.3 Molecular profiling / omics
No disease-specific transcriptomic/proteomic/metabolomic signatures were identified in retrieved evidence.

---

## 7. Anatomical structures affected
Based on described manifestations, primary anatomical systems include:
- **Musculoskeletal system:** joints (contractures), skin/soft tissues (webbing/pterygia), spine (scoliosis), feet (clubfoot/vertical talus), hands (camptodactyly/syndactyly; radial club hand in a rare association). (dahanoliel2021theclinicaland pages 1-2, bissinger2014nonlethalmultiplepterygium pages 1-2, gurung2024nonlethalmultiplepterygium pages 1-3)
- **Respiratory system:** pulmonary hypoplasia in lethal forms; restrictive disease noted in some long-term reports (evidence in retrieved snippets stronger for lethal prenatal pulmonary hypoplasia). (vogt2017clinicalandmolecular pages 84-88, bissinger2014nonlethalmultiplepterygium pages 1-2)

**UBERON suggestions:**
- Elbow region: UBERON:0001460; knee region: UBERON:0001463; vertebral column: UBERON:0001137; skeletal muscle tissue: UBERON:0001134; lung: UBERON:0002048.

---

## 8. Temporal development
- **Onset:** prenatal/congenital; reduced fetal movement is central. (bissinger2014nonlethalmultiplepterygium pages 1-2, dahanoliel2021theclinicaland pages 1-2)
- **Progression:** orthopedic issues can progress (notably scoliosis), and require monitoring and management over childhood. (dahanoliel2021theclinicaland pages 10-12)

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
Most cases are **autosomal recessive**. (dahanoliel2021theclinicaland pages 1-2, bissinger2014nonlethalmultiplepterygium pages 1-2, gurung2024nonlethalmultiplepterygium pages 1-3)

### 9.2 Epidemiology
Robust prevalence data were not found in retrieved evidence. A recent primary source provides one quantitative statement for lethal MPS: “**incidence <1/100000**” in the 2023 CHRND case report. (Chen et al., Jan 2023; https://doi.org/10.3389/fgene.2023.1005624) (chen2023casereportearly pages 1-2)

### 9.3 Population/variant distribution, sex ratio
Not available in retrieved evidence.

---

## 10. Diagnostics
### 10.1 Clinical and prenatal imaging
A 2023 first-trimester lethal MPS case report provides specific prenatal ultrasound features (12+ weeks) including:
- cystic hygroma, markedly increased nuchal translucency (NT 11 mm), absent nasal bone,
- edema,
- fixed limb contractures (knees/elbows), vertical wrists,
- and 3D facial angle measurement for micrognathia assessment. (chen2023casereportearly pages 1-2)

### 10.2 Genetic testing approach (current practice evidence)
Given genetic heterogeneity, **broad sequencing (panel/WES/WGS) and trio analysis** are aligned with current prenatal diagnostics implementation:
- In a 2023 prenatal WES implementation study, “**Twenty-eight fetus-parent trios were analyzed, of which seven (25%) showed a pathogenic or likely pathogenic variant that explained the fetal phenotype**,” and “**With a diagnostic yield in selected cases of 25% and a turn-around time under 4 weeks, rapid WES shows promise for becoming part of pregnancy care** …” (Janicki et al., published 23 Feb 2023; https://doi.org/10.3390/diagnostics13050860). (janicki2023implementationofexome pages 1-2)

**Differential diagnosis considerations (evidence-based):**
- Overlap with broader fetal akinesia deformation sequence/arthrogryposis disorders necessitates including NMJ genes (CHRNG/CHRND/CHRNA1/CHRNB1/RAPSN/DOK7) and contracture/myopathy genes (MYH3/TPM2) in diagnostic evaluation. (vogt2017clinicalandmolecular pages 152-157, hakonen2020recessivemyh3variants pages 1-2, dahanoliel2021theclinicaland pages 10-12)

### 10.3 Biomarkers / lab testing
No specific biochemical biomarkers were identified in retrieved evidence.

---

## 11. Outcome / prognosis
- **Nonlethal (Escobar/CHRNG-related) course:** described as stable over years, but with significant orthopedic morbidity (contractures, scoliosis). (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2, dahanoliel2021theclinicaland pages 10-12)
- **Lethal forms:** high frequency of severe prenatal complications including cystic hygroma, hydrops, pulmonary hypoplasia, fetal growth restriction, and reduced fetal movements in a cohort summary; these are associated with fetal/neonatal death. (vogt2017clinicalandmolecular pages 84-88)

Quantitative long-term survival rates and life expectancy estimates were not retrieved.

---

## 12. Treatment / management (current applications)
No disease-modifying pharmacotherapy is established in retrieved evidence; management is primarily **orthopedic + rehabilitative + supportive**, individualized.

### 12.1 Orthopedic and rehabilitative management
- In a 12-child series, scoliosis management included conservative approaches “**Bracing and serial spine casting appear to be beneficial for a few years**,” and more severe curves may require “**non-fusion spinal instrumentation**”; the authors conclude that “**Molecular diagnosis and careful monitoring of the spine is needed** …” (Dahan-Oliel et al., Aug 2021; https://doi.org/10.3390/genes12081220). (dahanoliel2021theclinicaland pages 1-2)
- A 2024 orthopedic case report describes functional management of contractures: knee flexion contractures due to pterygia corrected with **skeletal traction**, then **long-leg stretch casting** and **orthoses**; surgical correction for bilateral radial club hands was deferred due to reasonable function. (Gurung et al., Jul 2024; https://doi.org/10.59173/noaj.20241001i). (gurung2024nonlethalmultiplepterygium pages 1-3)

### 12.2 Perioperative/anesthesia considerations
Anesthetic/difficult airway concerns are mentioned as recurring themes in the broader Escobar literature (not detailed quantitatively in retrieved primary excerpts). (cichelli2025multiplepterygiumin pages 9-9)

### 12.3 MAXO (treatment action ontology) suggestions
- Physical therapy / physiotherapy: MAXO:0000010 (rehabilitation therapy; broad)
- Orthopedic casting: MAXO term not retrieved; conceptually “casting/immobilization”
- Orthotic device use: MAXO:0000899 (orthosis; broad)
- Spinal bracing: orthosis subclass
- Surgical correction of scoliosis / instrumentation: surgical procedure (broad MAXO)

### 12.4 Clinical trials
A ClinicalTrials.gov search on “multiple pterygium syndrome OR Escobar” did not yield disease-specific interventional trials in retrieved results. (dahanoliel2021theclinicaland pages 1-2)

---

## 13. Prevention
Primary prevention is not applicable for a Mendelian disorder; prevention focuses on **reproductive and family-risk management**:
- **Genetic counseling** for autosomal recessive inheritance and recurrence risk.
- **Prenatal diagnosis** (ultrasound + rapid WES/panel testing) enabling timely decision-making and planning; rapid trio-WES can return results in <4 weeks in a prenatal program. (janicki2023implementationofexome pages 1-2, chen2023casereportearly pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary MPS analogs or OMIA entries were identified in retrieved evidence.

---

## 15. Model organisms
Direct CHRNG-specific animal models were not retrieved in the provided evidence.

For MYH3-related congenital syndromes (which can overlap clinically with Escobar-like presentations), a mouse knockout study demonstrates that **Myh3 knockout mice display scoliosis and vertebral fusion** and implicates **YAP signaling** as a mediator, with pharmacologic inhibition improving multiple phenotypes (mouse model relevance to congenital contracture/skeletal fusion biology). (publication details in retrieved evidence list, but mechanistic excerpt not extracted for citation here; therefore not asserted further)

---

## Key limitations of this report (evidence gaps)
1. **Orphanet/ICD/MeSH/MONDO identifiers** were not present in the retrieved evidence snippets; only OMIM IDs and subtype labels were captured from peer-reviewed articles. (dahanoliel2021theclinicaland pages 1-2)
2. **Population prevalence, carrier frequency, and variant geographic distribution** were not available from the retrieved texts.
3. **Validated QoL instruments and longitudinal survival statistics** were not retrieved.
4. An attempt to retrieve **figure/table images (e.g., WBMRI patterns)** from CHRNG-related MPS publications was unsuccessful with available tooling; thus imaging information is reported from text descriptions only. (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2)


References

1. (dahanoliel2021theclinicaland pages 1-2): Noémi Dahan-Oliel, Klaus Dieterich, Frank Rauch, Ghalib Bardai, Taylor N. Blondell, Anxhela Gjyshi Gustafson, Reggie Hamdy, Xenia Latypova, Kamran Shazand, Philip F. Giampietro, and Harold van Bosse. The clinical and genotypic spectrum of scoliosis in multiple pterygium syndrome: a case series on 12 children. Genes, 12:1220, Aug 2021. URL: https://doi.org/10.3390/genes12081220, doi:10.3390/genes12081220. This article has 12 citations.

2. (kariminejad2016truncatingchrngmutations pages 1-2): Ariana Kariminejad, Navid Almadani, Atefeh Khoshaeen, Bjorn Olsson, Ali-Reza Moslemi, and Homa Tajsharghi. Truncating chrng mutations associated with interfamilial variability of the severity of the escobar variant of multiple pterygium syndrome. BMC Genetics, May 2016. URL: https://doi.org/10.1186/s12863-016-0382-5, doi:10.1186/s12863-016-0382-5. This article has 22 citations.

3. (bissinger2014nonlethalmultiplepterygium pages 1-2): Robin L. Bissinger and Frances R. Koch. Nonlethal multiple pterygium syndrome: escobar syndrome. Advances in Neonatal Care, 14:24–29, Feb 2014. URL: https://doi.org/10.1097/anc.0000000000000039, doi:10.1097/anc.0000000000000039. This article has 19 citations and is from a peer-reviewed journal.

4. (sandweiss2022atruncatingvariant pages 1-2): Alexander J. Sandweiss, Shalinkumar Patel, Mohammad Y. Bader, and Ranjit I. Kylat. A truncating variant of chrng as a cause of escobar syndrome: a multiple pterygium syndrome subtype. Journal of Pediatric Genetics, 11:144-146, Aug 2022. URL: https://doi.org/10.1055/s-0040-1715640, doi:10.1055/s-0040-1715640. This article has 5 citations and is from a peer-reviewed journal.

5. (chen2023casereportearly pages 1-2): Caiyuan Chen, Jin Han, Jiaxin Xue, Ru Li, Guilan Chen, Xin Yang, Jiajie Tang, Fucheng Li, and Dongzhi Li. Case report: early diagnosis of lethal multiple pterygium syndrome with micrognathia: two novel mutations in the chrnd gene. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2023.1005624, doi:10.3389/fgene.2023.1005624. This article has 2 citations and is from a peer-reviewed journal.

6. (vogt2017clinicalandmolecular pages 84-88): J Vogt. Clinical and molecular genetics of the multiple pterygium syndromes. Unknown journal, 2017.

7. (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 2-3): Laura Carrera‐García, Daniel Natera‐de Benito, Klaus Dieterich, Marta G. G. de la Banda, Adrien Felter, Emili Inarejos, Anna Codina, Cristina Jou, Monica Roldan, Francesc Palau, Janet Hoenicka, Jordi Pijuan, Carlos Ortez, Jessica Expósito‐Escudero, Chantal Durand, Frédérique Nugues, Cecilia Jimenez‐Mallebrera, Jaume Colomer, Robert Y. Carlier, Hanns Lochmüller, Susana Quijano‐Roy, and Andres Nascimento. Chrng‐related nonlethal multiple pterygium syndrome: muscle imaging pattern and clinical, histopathological, and molecular genetic findings. American Journal of Medical Genetics Part A, 179:915-926, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61122, doi:10.1002/ajmg.a.61122. This article has 18 citations.

8. (carrera‐garcia2019chrng‐relatednonlethalmultiple pages 1-2): Laura Carrera‐García, Daniel Natera‐de Benito, Klaus Dieterich, Marta G. G. de la Banda, Adrien Felter, Emili Inarejos, Anna Codina, Cristina Jou, Monica Roldan, Francesc Palau, Janet Hoenicka, Jordi Pijuan, Carlos Ortez, Jessica Expósito‐Escudero, Chantal Durand, Frédérique Nugues, Cecilia Jimenez‐Mallebrera, Jaume Colomer, Robert Y. Carlier, Hanns Lochmüller, Susana Quijano‐Roy, and Andres Nascimento. Chrng‐related nonlethal multiple pterygium syndrome: muscle imaging pattern and clinical, histopathological, and molecular genetic findings. American Journal of Medical Genetics Part A, 179:915-926, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61122, doi:10.1002/ajmg.a.61122. This article has 18 citations.

9. (dahanoliel2021theclinicaland pages 13-14): Noémi Dahan-Oliel, Klaus Dieterich, Frank Rauch, Ghalib Bardai, Taylor N. Blondell, Anxhela Gjyshi Gustafson, Reggie Hamdy, Xenia Latypova, Kamran Shazand, Philip F. Giampietro, and Harold van Bosse. The clinical and genotypic spectrum of scoliosis in multiple pterygium syndrome: a case series on 12 children. Genes, 12:1220, Aug 2021. URL: https://doi.org/10.3390/genes12081220, doi:10.3390/genes12081220. This article has 12 citations.

10. (vogt2017clinicalandmolecular pages 152-157): J Vogt. Clinical and molecular genetics of the multiple pterygium syndromes. Unknown journal, 2017.

11. (hakonen2020recessivemyh3variants pages 1-2): Anna H. Hakonen, Johanna Lehtonen, Sirpa Kivirikko, Riikka Keski‐Filppula, Jukka Moilanen, Reetta Kivisaari, Henrikki Almusa, Eveliina Jakkula, Janna Saarela, Kristiina Avela, and Kristiina Aittomäki. Recessive myh3 variants cause “contractures, pterygia, and variable skeletal fusions syndrome 1b” mimicking escobar variant multiple pterygium syndrome. American Journal of Medical Genetics Part A, 182:2605-2610, Sep 2020. URL: https://doi.org/10.1002/ajmg.a.61836, doi:10.1002/ajmg.a.61836. This article has 14 citations.

12. (dahanoliel2021theclinicaland pages 10-12): Noémi Dahan-Oliel, Klaus Dieterich, Frank Rauch, Ghalib Bardai, Taylor N. Blondell, Anxhela Gjyshi Gustafson, Reggie Hamdy, Xenia Latypova, Kamran Shazand, Philip F. Giampietro, and Harold van Bosse. The clinical and genotypic spectrum of scoliosis in multiple pterygium syndrome: a case series on 12 children. Genes, 12:1220, Aug 2021. URL: https://doi.org/10.3390/genes12081220, doi:10.3390/genes12081220. This article has 12 citations.

13. (gurung2024nonlethalmultiplepterygium pages 1-3): YP Gurung, S Sharma, B Banskota, and T Rajbhandari. Non-lethal multiple pterygium syndrome (escobar syndrome) with bilateral radial club hands: a case report. Nepal Orthopaedic Association Journal, pages 30-32, Jul 2024. URL: https://doi.org/10.59173/noaj.20241001i, doi:10.59173/noaj.20241001i. This article has 0 citations.

14. (janicki2023implementationofexome pages 1-2): Ewa Janicki, Marjan De Rademaeker, Colombine Meunier, Nele Boeckx, Bettina Blaumeiser, and Katrien Janssens. Implementation of exome sequencing in prenatal diagnostics: chances and challenges. Diagnostics, 13:860, Feb 2023. URL: https://doi.org/10.3390/diagnostics13050860, doi:10.3390/diagnostics13050860. This article has 16 citations.

15. (cichelli2025multiplepterygiumin pages 9-9): Alice Cichelli, Simona Federica Montemitro, Donato Carlo Zotta, Daniele Intraina, Raffaele Nigro, Paolo Barbone, Stefano Delli Pizzi, and Teresa Paolucci. Multiple pterygium in escobar syndrome: a scoping review for a personalized rehabilitative plan. Egyptian Journal of Medical Human Genetics, Dec 2025. URL: https://doi.org/10.1186/s43042-025-00817-1, doi:10.1186/s43042-025-00817-1. This article has 0 citations and is from a peer-reviewed journal.