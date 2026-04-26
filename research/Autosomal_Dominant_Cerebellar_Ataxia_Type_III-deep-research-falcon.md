---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T15:36:06.589786'
end_time: '2026-04-26T15:51:34.947762'
duration_seconds: 928.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Cerebellar Ataxia Type III
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Cerebellar Ataxia Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Cerebellar Ataxia Type III** covering all of the
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
- **Disease Name:** Autosomal Dominant Cerebellar Ataxia Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Cerebellar Ataxia Type III** covering all of the
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


# Autosomal Dominant Cerebellar Ataxia Type III (ADCA III) — Disease Characteristics Research Report

## Target Disease
- **Disease name (legacy clinical label):** Autosomal Dominant Cerebellar Ataxia Type III (ADCA type III) (fujioka2013autosomaldominantcerebellar pages 1-2)
- **Category:** Mendelian (autosomal dominant)
- **Modern framing:** A historical (pre-molecular) *clinicophenotypic* grouping within the autosomal-dominant spinocerebellar ataxias (SCAs), enriched for “pure cerebellar” syndromes, now typically discussed as gene-defined SCA subtypes (fujioka2013autosomaldominantcerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 3-4)
- **MONDO / OMIM / Orphanet / MeSH / ICD identifiers:** Not retrievable from the currently available tool-retrieved sources; below, the gene-defined SCA entities are specified instead, and one OMIM example (SCA1) appears in a review but not for ADCA III itself (pilotto2024hereditaryataxiasfrom pages 3-4, warrenburg2005autosomaldominantcerebellar pages 149-152).

---

## 1. Disease Information

### 1.1 What is the disease? (concise overview)
ADCA type III is a subtype of autosomal dominant cerebellar ataxia characterized predominantly by a **pure cerebellar syndrome** (gait/stance/limb ataxia and dysarthria), with **cerebellar oculomotor dysfunction** (e.g., nystagmus, impaired smooth pursuit) and occasional additional neurologic signs (e.g., pyramidal signs, tremor, ophthalmoplegia) (fujioka2013autosomaldominantcerebellar pages 1-2).

**Direct abstract quote (definition):**
- “Autosomal Dominant Cerebellar Ataxia (ADCA) Type III is a type of spinocerebellar ataxia (SCA) classically characterized by pure cerebellar ataxia and occasionally by non-cerebellar signs such as pyramidal signs, ophthalmoplegia, and tremor.” (Fujioka et al., *Orphanet J Rare Dis*, **2013-01**, DOI: https://doi.org/10.1186/1750-1172-8-14) (fujioka2013autosomaldominantcerebellar pages 1-2)

### 1.2 Key identifiers and synonyms
- **Synonyms/related terms:** “autosomal dominant cerebellar ataxias,” “spinocerebellar ataxias (SCAs)” (fujioka2013autosomaldominantcerebellar pages 1-2)
- **Subtypes commonly included in ADCA type III:** **SCA5, SCA6, SCA11, SCA26, SCA30, SCA31** (fujioka2013autosomaldominantcerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 3-4)
  - (Some older sources also list additional entities; e.g., a 2011 ADCA type I review lists SCA29 among “pure cerebellar” syndromes, reflecting historical fluidity) (whaley2011autosomaldominantcerebellar pages 1-2).

### 1.3 Evidence source type
The ADCA type III grouping derives from **aggregated disease-level resources and reviews** synthesizing multiple families and case series (e.g., Fujioka 2013), while gene-specific entities (SCA31, SCA11) have both patient-level and mechanistic/model evidence (fujioka2013autosomaldominantcerebellar pages 1-2, ishikawa2023spinocerebellarataxiatype pages 1-2, felicio2024spinocerebellarataxiatype pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
ADCA type III is genetically heterogeneous and (in current understanding) is best described as a set of **gene-defined SCAs** with predominant cerebellar involvement.

- **SCA5:** pathogenic variants in **SPTBN2** (β-III spectrin) (fujioka2013autosomaldominantcerebellar pages 2-3, fujioka2013autosomaldominantcerebellar pages 5-6)
- **SCA6:** **CAG repeat expansion** in **CACNA1A** (P/Q-type calcium channel α1A subunit) (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 5-6)
- **SCA11:** truncating variants in **TTBK2** (tau tubulin kinase 2) (felicio2024spinocerebellarataxiatype pages 1-2, felicio2024spinocerebellarataxiatype pages 2-4)
- **SCA31:** complex **pentanucleotide repeat insertion/expansion** including pathogenic **(TGGAA)n** in the **BEAN1/TK2 shared intronic region**, producing toxic repeat RNAs (ishikawa2023spinocerebellarataxiatype pages 1-2)
- **SCA26 & SCA30:** mapped loci exist but **causal genes not established** in the classic ADCA III review (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7)

### 2.2 Risk factors
- **Primary risk factor:** autosomal dominant inheritance / family history consistent with ADCA/SCAs (fujioka2013autosomaldominantcerebellar pages 1-2).
- **Geographic ancestry/founder effects:** strong founder effect described for SCA31 in Japan (ishikawa2023spinocerebellarataxiatype pages 1-2).

### 2.3 Protective factors / gene–environment interactions
No ADCA III–specific protective factors or gene–environment interaction data were identified in the retrieved sources. This is a knowledge gap in the provided evidence corpus.

---

## 3. Phenotypes

### 3.1 Core phenotypes (with suggested HPO terms)
Across ADCA type III, the “pure cerebellar” phenotype typically includes:

1. **Gait and limb ataxia** (symptom/sign)
   - **Evidence:** group clinical description (fujioka2013autosomaldominantcerebellar pages 1-2)
   - **HPO:** *Gait ataxia* (HP:0002066), *Limb ataxia* (HP:0002073), *Truncal ataxia* (HP:0002078)

2. **Dysarthria**
   - **Evidence:** typical clinical description for ADCA III and SCA11 (fujioka2013autosomaldominantcerebellar pages 1-2, felicio2024spinocerebellarataxiatype pages 1-2)
   - **HPO:** *Dysarthria* (HP:0001260)

3. **Cerebellar oculomotor dysfunction** (nystagmus, impaired pursuit)
   - **Evidence:** group description; SCA6 vestibulo-ocular reflex/nystagmus patterns reported (fujioka2013autosomaldominantcerebellar pages 1-2, kim2023clinicalvalueof pages 1-2)
   - **HPO:** *Nystagmus* (HP:0000639), *Abnormal smooth pursuit* (HP:0000641), *Downbeat nystagmus* (HP:0007665), *Gaze-evoked nystagmus* (HP:0000668)

4. **Cerebellar atrophy on MRI** (imaging phenotype)
   - **Evidence:** diagnostic relevance of cerebellar atrophy on MRI emphasized (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 2-3)
   - **HPO:** *Cerebellar atrophy* (HP:0001272)

### 3.2 Subtype-specific phenotypic notes
- **SCA6:** late-onset; common eye movement abnormalities; occasional extracerebellar features such as pyramidal signs and peripheral neuropathy; depression and fatigue reported (fujioka2013autosomaldominantcerebellar pages 5-6).
- **SCA5:** eye movement abnormalities; occasional tremor, hyperreflexia, impaired vibration sense; global cerebellar atrophy without brainstem involvement (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6).
- **SCA11:** dysarthria and ocular signs common; pyramidal signs (hyperreflexia) sometimes; MRI shows cerebellar atrophy (felicio2024spinocerebellarataxiatype pages 1-2).
- **SCA31:** late-onset slowly progressive ataxia; classic Japanese description emphasizes lack of extra-cerebellar signs and cerebellar atrophy without brainstem involvement (ishikawa2023spinocerebellarataxiatype pages 1-2).

### 3.3 Age of onset, severity, progression
- **ADCA type III overall:** onset typically in adulthood; minority in adolescence; generally slowly progressive with relatively benign course vs ADCA type I (fujioka2013autosomaldominantcerebellar pages 1-2).
- **SCA6:** mean onset ~45 years (range 16–72), ~60% after age 50; slow progression (SARA increase 0.35±0.3 over 1 year reported in a cited natural history context within the review) (fujioka2013autosomaldominantcerebellar pages 5-6).
- **SCA5:** onset 10–68 (mean 33), slowly progressive, duration may exceed 30 years (fujioka2013autosomaldominantcerebellar pages 3-5).
- **SCA31:** mean onset ~58–60; slow progression (fujioka2013autosomaldominantcerebellar pages 6-7, ishikawa2023spinocerebellarataxiatype pages 1-2).

### 3.4 Quality of life impact
Falls and dysphagia can reduce quality of life and may shorten lifespan, despite the disorder typically being “not fatal” (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 3-5).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (HGNC symbols as used in literature)
- **SPTBN2** (SCA5) (fujioka2013autosomaldominantcerebellar pages 5-6)
- **CACNA1A** (SCA6) (fujioka2013autosomaldominantcerebellar pages 6-7)
- **TTBK2** (SCA11) (felicio2024spinocerebellarataxiatype pages 1-2)
- **BEAN1 / TK2 shared intronic locus** (SCA31 repeat insertion; BEAN1 brain-restricted transcription highlighted) (ishikawa2023spinocerebellarataxiatype pages 1-2)

### 4.2 Pathogenic variant classes
- **SCA6 (CACNA1A):** CAG repeat expansion; expanded alleles usually **20–29 repeats** vs normal **4–18** (fujioka2013autosomaldominantcerebellar pages 6-7).
- **SCA11 (TTBK2):** mainly small indels causing frameshifts and truncated proteins; examples include c.1329insA and multiple frameshift variants summarized in 2024 review (felicio2024spinocerebellarataxiatype pages 2-4, felicio2024spinocerebellarataxiatype pages 1-2).
- **SCA31 (BEAN1/TK2 locus):** complex 2.5–3.8 kb insertion containing multiple pentanucleotide motifs; **(TGGAA)n** isolated as pathogenic component; bidirectionally transcribed repeat RNAs (ishikawa2023spinocerebellarataxiatype pages 1-2).

### 4.3 Penetrance / anticipation
- **SCA6:** penetrance “almost 100%” and “anticipation has not been observed” (fujioka2013autosomaldominantcerebellar pages 5-6).
- **SCA31:** described as likely incomplete penetrance in older review; anticipation absent or mild (fujioka2013autosomaldominantcerebellar pages 6-7).

### 4.4 Modifier genes / epigenetics
No validated modifier gene or epigenetic associations specific to ADCA III were identified in the retrieved corpus. Natural history/genetic modifier studies exist at the trial-registry level (NCT01060371) but do not specify modifiers in the extracted record (NCT01060371 chunk 1).

---

## 5. Environmental Information
No specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence for ADCA type III; the condition is primarily genetic in current descriptions.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core mechanistic concepts (current understanding)
Recent expert reviews emphasize that hereditary ataxias involve diverse molecular pathways (excitability/calcium homeostasis, proteostasis, mitochondrial dysfunction, inflammation), while ADCA type III subtypes often converge on **Purkinje cell dysfunction/degeneration** and cerebellar network impairment (pilotto2024hereditaryataxiasfrom pages 3-4, felicio2024spinocerebellarataxiatype pages 1-2).

### 6.2 Subtype-specific mechanistic chains

#### SCA6 (CACNA1A polyQ)
**Trigger:** CAG expansion in CACNA1A → expanded polyglutamine tract in CaV2.1 channel.
**Proposed chain:** altered Ca2+ channel function → reduced Ca2+ influx → eventual neuronal cell death (hypothesis stated in older review) (fujioka2013autosomaldominantcerebellar pages 6-7).

- **Suggested GO biological process terms:** *calcium ion transmembrane transport*; *synaptic transmission*.
- **Suggested CL cell types:** *Purkinje cell* (CL:0000121), *cerebellar granule cell*.

#### SCA5 (SPTBN2 / β-III spectrin)
**Trigger:** SPTBN2 coding variants → β-III spectrin dysfunction.
**Proposed chain:** impaired stabilization/trafficking of glutamate transporter EAAT4, impaired axonal transport, reduced Purkinje spontaneous firing and dysregulated glutamatergic neurotransmission → cerebellar motor dysfunction (fujioka2013autosomaldominantcerebellar pages 5-6).

- **Suggested GO terms:** *axon transport*, *glutamate uptake*, *regulation of membrane potential*.

#### SCA11 (TTBK2)
**Trigger:** truncating variants in TTBK2.
**Unresolved upstream mechanism:** haploinsufficiency vs dominant-negative effects; reports of loss of kinase activity and mislocalization; and links to disrupted ciliogenesis (felicio2024spinocerebellarataxiatype pages 1-2).
**Downstream hypotheses:** impaired phosphorylation of neuronal substrates such as **tau** and **TDP-43** and potentially neurotransmitter receptors/transporters → cerebellar neurodegeneration (felicio2024spinocerebellarataxiatype pages 1-2).

- **Suggested GO terms:** *protein phosphorylation*, *microtubule cytoskeleton organization*, *cilium assembly*.

#### SCA31 (BEAN1/TK2 locus repeat RNA toxicity)
**Trigger:** insertion/expansion containing (TGGAA)n → brain-restricted bidirectional transcription produces repeat RNAs.
**Causal chain evidence:** (UGGAA)n repeat RNA forms **nuclear RNA foci in Purkinje cell nuclei**; Drosophila models show length- and expression-dependent RNA toxicity; RNA-binding proteins **TDP-43, FUS, hnRNP A2/B1** mitigate toxicity, suggesting an RNA-chaperone/antitoxic mechanism (ishikawa2023spinocerebellarataxiatype pages 1-2, ishikawa2023spinocerebellarataxiatype pages 2-3).

- **Suggested GO terms:** *RNA binding*, *RNA processing*, *nuclear body organization*.

### 6.3 Molecular profiling / omics
No ADCA III subtype-specific transcriptomic/proteomic/metabolomic profiling evidence was retrieved in the current corpus.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Primary system:** central nervous system (motor coordination networks) (fujioka2013autosomaldominantcerebellar pages 1-2)
- **Primary organ/structure:** **cerebellum**; in some subtypes additional involvement of brainstem/pons may be present (e.g., SCA6 MRI atrophy includes pons/red nucleus) (fujioka2013autosomaldominantcerebellar pages 6-7).

### 7.2 Tissue/cell level
- Dominant involvement of **cerebellar Purkinje neurons** is repeatedly emphasized across reviews and in subtype mechanisms (pilotto2024hereditaryataxiasfrom pages 3-4, ishikawa2023spinocerebellarataxiatype pages 1-2).

**Suggested UBERON terms:** *cerebellum*; *cerebellar cortex*; *pons* (for subtypes with brainstem involvement).

---

## 8. Temporal Development

### 8.1 Onset
- Typical: adult onset, often 4th–6th decade depending on subtype (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 5-6, ishikawa2023spinocerebellarataxiatype pages 1-2).

### 8.2 Progression
- Generally slowly progressive; SCA6 noted as slowest progression among compared SCAs in cited European natural history context (fujioka2013autosomaldominantcerebellar pages 5-6).

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** inheritance (definition of ADCA/SCAs) (kim2023clinicalvalueof pages 1-2).

### 9.2 Epidemiology (recent 2023–2024 priority)
- **ADCA prevalence:** ~**1–5 per 100,000**; European incidence reported as **~3 per 100,000** in one 2024 review (Pilotto et al., *Cells*, **2024-02**, DOI https://doi.org/10.3390/cells13040319) (pilotto2024hereditaryataxiasfrom pages 3-4).
- **European SCA prevalence range:** narrative review reports global SCA prevalence **0–5.6/100,000** and highlights Harding’s historical ADCA classification, defining type III as “relatively isolated cerebellar ataxia” (Mattei et al., *Cerebellum*, **2024-09**, DOI https://doi.org/10.1007/s12311-023-01600-x) (mattei2024epidemiologyofspinocerebellar pages 1-2).
- **SCA6 frequency:** EUROSCA European relative frequency ~**13%** (mattei2024epidemiologyofspinocerebellar pages 4-5, mattei2024epidemiologyofspinocerebellar pages 5-6), consistent with older ADCA III review reporting ~13% of all ADCA cases and prevalence <1/100,000 with substantial geographic variation (fujioka2013autosomaldominantcerebellar pages 2-3).
- **SCA31:** strong founder effect; essentially absent in other ethnicities; disease frequency assumed ~0.003% in Japanese population calculations in 2023 review (ishikawa2023spinocerebellarataxiatype pages 1-2, ishikawa2023spinocerebellarataxiatype pages 2-3).

---

## 10. Diagnostics

### 10.1 Clinical evaluation
- No fully validated diagnostic criteria exist for ADCA type III; diagnosis relies on **clinical/family history, neurologic exam, MRI**, exclusion of acquired causes, and **definitive genetic testing** (fujioka2013autosomaldominantcerebellar pages 1-2).

### 10.2 Imaging
- MRI cerebellar atrophy is an important argument for neurodegenerative cerebellar ataxia vs secondary causes (fujioka2013autosomaldominantcerebellar pages 2-3).

### 10.3 Genetic testing approach
A practical stepwise approach is described in Fujioka et al. (2013), including geographically informed prioritization of testing.

- **Figure/Table evidence:** diagnostic algorithm and ADCA III gene/subtype table extracted from the review (fujioka2013autosomaldominantcerebellar media 92211852, fujioka2013autosomaldominantcerebellar media 9844df72, fujioka2013autosomaldominantcerebellar media 27541419).

### 10.4 Differential diagnosis
After confirming a “pure cerebellar” syndrome, secondary causes to exclude include drug effects/toxicity, nutritional deficiencies, infections, and structural abnormalities (fujioka2013autosomaldominantcerebellar pages 1-2).

### 10.5 Emerging diagnostics / biomarkers
- **Physiologic biomarkers:** A 2023 study found distinct **vestibulo-ocular reflex** patterns across SCA subtypes, suggesting video head impulse test measures may aid genotype differentiation (Kim et al., *Sci Rep*, **2023-09**, DOI https://doi.org/10.1038/s41598-023-41924-6) (kim2023clinicalvalueof pages 1-2).

---

## 11. Outcome / Prognosis

- ADCA type III is generally slowly progressive and “not life-threatening,” but dysphagia and falls can shorten lifespan and reduce quality of life (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 1-2).
- In SCA11, lifespan is “thought to be normal,” though many require walking aids later in life (felicio2024spinocerebellarataxiatype pages 1-2).

---

## 12. Treatment

### 12.1 Current standard of care (supportive)
Supportive therapies remain foundational:
- Physical therapy, occupational therapy, speech therapy (dysarthria/swallowing) are recommended in modern inherited ataxia management reviews (coarelli2023theinheritedcerebellar pages 12-13, fujioka2013autosomaldominantcerebellar pages 1-2).

### 12.2 Symptomatic pharmacotherapy (evidence mainly older but still informative)
For SCA6, Fujioka et al. summarize trials suggesting symptomatic benefit:
- acetazolamide 250–500 mg/day (temporal but significant improvement)
- gabapentin 1200 mg/day (pilot symptom alleviation)
- tandospirone 15 mg/day (open-label improvement in ataxia rating and stabilometer measures)
(fujioka2013autosomaldominantcerebellar pages 3-5).

### 12.3 Clinical trials / real-world implementations (ClinicalTrials.gov)

- **Dalfampridine (Ampyra) for gait** (interventional; crossover RCT):
  - **NCT01811706**; University of Florida; started **2013-02**, completed **2013-12**; enrolled **20** adults with SCA1/2/3/6.
  - Primary outcome: change in **Timed 25-Foot Walk (T25FW)** after 4 weeks of dalfampridine 10 mg q12h vs placebo.
  - Secondary outcomes included **SARA** and gait biomechanics (stride length).
  - URL: https://clinicaltrials.gov/study/NCT01811706 (NCT01811706 chunk 1).

- **Natural history and genetic modifiers**:
  - **NCT01060371 (CRC-SCA)**; observational cohort; planned enrollment **800**; includes **SCA6** and other dominant SCAs; collects blood for DNA/genetic modifier analysis; primary outcomes include longitudinal progression and modifier associations.
  - Estimated primary completion **2024-05-19** in the extracted record.
  - URL: https://clinicaltrials.gov/study/NCT01060371 (NCT01060371 chunk 1).

### 12.4 Emerging disease-modifying directions (2023–2024 expert synthesis)
- 2023–2024 reviews highlight **antisense oligonucleotides (ASOs)** and gene therapy as key emerging modalities across inherited ataxias (with clinical trial activity in some polyQ SCAs), and emphasize ongoing challenges (delivery, biomarkers, economics) (coarelli2023theinheritedcerebellar pages 12-13).
- A 2024 review frames therapeutic strategies around regulating excitability/calcium homeostasis and targeting proteostasis/mitochondrial dysfunction/inflammation, and references emerging modalities (ASOs, gene therapy) as part of the broader hereditary ataxia pipeline (pilotto2024hereditaryataxiasfrom pages 3-4).

### 12.5 MAXO suggestions (treatments/actions)
- **Physical therapy / physiotherapy** (MAXO: physical therapy)
- **Occupational therapy**
- **Speech therapy**
- **Genetic counseling**
(These are ontology suggestions; MAXO IDs not available from retrieved sources.)

---

## 13. Prevention

Primary prevention of inheritance is not available, but genetic and reproductive options are key.

- **Genetic counseling:** transmission risk counseling; presymptomatic testing in dominant diseases; prenatal/preimplantation diagnosis are discussed as options in inherited ataxias (coarelli2023theinheritedcerebellar pages 12-13).

---

## 14. Other Species / Natural Disease
No naturally occurring non-human disease analogs were identified in the retrieved corpus.

---

## 15. Model Organisms
- **SCA31 Drosophila models:** overexpression of (UGGAA)n repeat RNA causes toxicity and degeneration; co-expression of RNA-binding proteins (e.g., TDP-43) mitigates toxicity, supporting RNA-chaperone concepts (ishikawa2023spinocerebellarataxiatype pages 2-3).
- **SCA5 mechanistic model evidence:** Drosophila/animal model findings summarized in review include impaired axonal transport and altered Purkinje firing with β-III spectrin loss/mutation (fujioka2013autosomaldominantcerebellar pages 5-6).

---

## Summary Table (subtypes, genes, phenotypes, epidemiology)

| Entity | Key synonyms/notes | Causal gene or locus | Variant/mutation class | Typical age at onset (with ranges if available) | Key clinical features (pure cerebellar + notable extras) | Neuroimaging features | Epidemiology notes/statistics |
|---|---|---|---|---|---|---|---|
| ADCA type III | Harding clinical category; “pure cerebellar” / mostly pure cerebellar syndromes; currently includes SCA5, SCA6, SCA11, SCA26, SCA30, SCA31 (fujioka2013autosomaldominantcerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 3-4) | Four established genes plus two mapped loci: **SPTBN2** (SCA5), **CACNA1A** (SCA6), **TTBK2** (SCA11), **BEAN-TK2/BEAN1-linked repeat insertion** (SCA31), and loci for SCA26/SCA30 (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 2-3) | Mixed mechanisms: missense/in-frame deletion/frameshift variants (SCA5/SCA11), coding **CAG repeat** expansion (SCA6), non-coding **TGGAA-containing repeat** expansion (SCA31), unknown for SCA26/SCA30 (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 2-3) | Usually adulthood; minority in adolescence; symptoms often arise in 4th decade overall for ADCAs (fujioka2013autosomaldominantcerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 3-4) | Gait, stance, limb ataxia and dysarthria with cerebellar oculomotor dysfunction; occasional non-cerebellar signs include pyramidal signs, peripheral neuropathy, involuntary movements, ophthalmoplegia, tremor (fujioka2013autosomaldominantcerebellar pages 1-2) | Cerebellar atrophy on MRI supports neurodegenerative diagnosis; subtype-specific patterns vary (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 2-3) | Incidence/prevalence of ADCA III itself unknown; ADCA prevalence estimated ~3/100,000 in Netherlands and 4.2/100,000 in Norway; ADCA/SCAs overall ~1–5/100,000, ~3/100,000 in Europe (fujioka2013autosomaldominantcerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 3-4) |
| SCA5 | ADCA III subtype; autosomal dominant pure cerebellar ataxia due to β-III spectrin dysfunction (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 5-6) | **SPTBN2** / 11q13.2 (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 2-3, fujioka2013autosomaldominantcerebellar pages 5-6) | Pathogenic **in-frame deletions** and **missense** variants; conventional coding mutations (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6) | Mean ~33 years; range **10–68** years; age-related penetrance; no anticipation reported (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6) | Slowly progressive cerebellar ataxia with dysarthria and eye movement abnormalities; notable extras reported include downbeat/gaze-evoked nystagmus, facial myokymia, horizontal gaze palsy, intention/rest tremor, brisk reflexes, impaired vibration sense (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6) | Global/pancerebellar atrophy without brainstem involvement (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6) | Rare; reported in American, German, French families (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 5-6) |
| SCA6 | Most common ADCA III subtype; polyglutamine/CACNA1A-related pure cerebellar ataxia (fujioka2013autosomaldominantcerebellar pages 1-2) | **CACNA1A** / 19q13.2 (gene table); chromosome 19p13 noted in older text; encodes P/Q-type calcium channel α1A subunit (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 2-3) | **CAG repeat expansion** in coding region; expanded alleles usually **20–29** repeats vs normal **4–18** (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7) | Mean ~45 years; range **16–72** years; ~60% onset after age 50; almost complete penetrance; no anticipation observed (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 5-6) | Predominantly gait ataxia, dysarthria, gaze-evoked/downbeat nystagmus, impaired smooth pursuit and vestibulo-ocular reflex; occasional pyramidal signs, neuropathy, cognitive impairment, parkinsonism, myoclonus, dystonia, tremor, depression, fatigue (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 5-6, kim2023clinicalvalueof pages 1-2) | Severe cerebellar atrophy with mild atrophy of middle cerebellar peduncle/pons/red nucleus; MRI may show mild pons atrophy; VOR testing shows reduced posterior canal gains and catch-up saccades in 2023 study (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 2-3, kim2023clinicalvalueof pages 1-2) | Accounts for ~**13%** of all ADCA cases; prevalence estimated **<1/100,000**; common in Japan (**6–32%**), Korea (**15–23%**), Netherlands (**11–23%**), Germany (**10–22%**); EUROSCA European relative frequency ~**13%** (fujioka2013autosomaldominantcerebellar pages 2-3, mattei2024epidemiologyofspinocerebellar pages 1-2, mattei2024epidemiologyofspinocerebellar pages 5-6) |
| SCA11 | Rare ADCA III subtype; TTBK2-related dominant cerebellar ataxia (fujioka2013autosomaldominantcerebellar pages 1-2, felicio2024spinocerebellarataxiatype pages 1-2) | **TTBK2** / 15q15.2; initially mapped to 15q14-21 (fujioka2013autosomaldominantcerebellar pages 3-5, fujioka2013autosomaldominantcerebellar pages 6-7, felicio2024spinocerebellarataxiatype pages 1-2) | Mainly **small insertions/deletions causing frameshifts and truncation**; review notes missense variants are benign or unvalidated (fujioka2013autosomaldominantcerebellar pages 1-2, felicio2024spinocerebellarataxiatype pages 1-2) | Mean ~25–30 years; range **11–70** years in older review and **4–64** years in 2024 review (fujioka2013autosomaldominantcerebellar pages 5-6, felicio2024spinocerebellarataxiatype pages 1-2) | Slowly progressive cerebellar ataxia with limb/gait imbalance, dysarthria, jerky pursuit/ophthalmoplegia/horizontal-vertical nystagmus; occasional hyperreflexia, peripheral neuropathy, dystonia (fujioka2013autosomaldominantcerebellar pages 5-6, felicio2024spinocerebellarataxiatype pages 1-2) | Isolated marked cerebellar atrophy of hemispheres and vermis; one PET case showed reduced cerebellar and pontine metabolism (fujioka2013autosomaldominantcerebellar pages 5-6, felicio2024spinocerebellarataxiatype pages 1-2) | Very rare; likely **<1% of SCAs in Europe**; only a few families reported (British, Pakistani ancestry, German, French; later additional Chinese pedigree) (fujioka2013autosomaldominantcerebellar pages 5-6, felicio2024spinocerebellarataxiatype pages 1-2) |
| SCA26 | Very rare ADCA III subtype (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7) | Locus on **19p13.3 / 19p.33.3**; causative gene unknown (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 2-3) | Unknown / unmapped gene-level variant not identified (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7) | Mean ~42 years; range **26–60** years; no anticipation reported (fujioka2013autosomaldominantcerebellar pages 6-7) | Relatively late-onset, slowly progressive cerebellar symptoms with eye movement abnormalities (impaired pursuit, nystagmus); one patient with left hyperreflexia and Babinski sign (fujioka2013autosomaldominantcerebellar pages 6-7) | Isolated cerebellar atrophy (fujioka2013autosomaldominantcerebellar pages 6-7) | Extremely rare; only one American family of Norwegian descent reported (23 affected, 14 at-risk members) (fujioka2013autosomaldominantcerebellar pages 6-7) |
| SCA30 | Very rare ADCA III subtype (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7) | Locus on **4q34.3-q35.1**; causative mutation unknown (fujioka2013autosomaldominantcerebellar pages 6-7, fujioka2013autosomaldominantcerebellar pages 2-3) | Unknown / locus only (fujioka2013autosomaldominantcerebellar pages 1-2, fujioka2013autosomaldominantcerebellar pages 6-7) | Mean ~52 years; range **45–76** years (fujioka2013autosomaldominantcerebellar pages 6-7) | Relatively pure, slowly progressive cerebellar ataxia; some mild lower-limb hyperreflexia, gaze-evoked nystagmus, dystonia; family history suggested possible parkinsonism in deceased relatives (fujioka2013autosomaldominantcerebellar pages 6-7) | Isolated cerebellar atrophy, predominantly superior/dorsal vermis (fujioka2013autosomaldominantcerebellar pages 6-7) | Extremely rare; only one Australian family with six affected subjects reported (fujioka2013autosomaldominantcerebellar pages 6-7) |
| SCA31 | ADCA III subtype; common pure cerebellar ataxia in Japan with strong founder effect; sometimes called BEAN/TK2-linked repeat ataxia (ishikawa2023spinocerebellarataxiatype pages 1-2) | **BEAN1/TK2 shared intronic region** at **16q22.1/16q21** with pathogenic insertion containing **(TGGAA)n** (fujioka2013autosomaldominantcerebellar pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2) | **Non-coding complex pentanucleotide repeat insertion/expansion** containing (TGGAA)n, (TAGAA)n, (TAAAA)n, (TAAAATAGAA)n; pathogenic repeat is (TGGAA)n (ishikawa2023spinocerebellarataxiatype pages 1-2) | Mean ~58–60 years; range **8–83** years; late-onset progressive ataxia; anticipation absent or mild; incomplete penetrance suggested (fujioka2013autosomaldominantcerebellar pages 6-7, ishikawa2023spinocerebellarataxiatype pages 1-2) | Cerebellar ataxia with eye movement abnormalities (horizontal gaze nystagmus, impaired pursuit); occasional pyramidal signs, hearing difficulty, decreased vibration sense, tremor; extra-cerebellar features often absent in classic Japanese description (fujioka2013autosomaldominantcerebellar pages 6-7, ishikawa2023spinocerebellarataxiatype pages 1-2) | Cerebellar/global cerebellar atrophy without brainstem involvement; sagittal MRI shows prominent cerebellar atrophy (fujioka2013autosomaldominantcerebellar pages 6-7, ishikawa2023spinocerebellarataxiatype pages 1-2) | One of the most common autosomal dominant cerebellar ataxias in Japan; second most common ADCA III in older review, fourth most common ADCA in Japan in another source; Japan frequency around **9%** among ADCA in older review; disease assumed around **0.003%** in general Japanese population in 2023 review; basically absent in other ethnicities (fujioka2013autosomaldominantcerebellar pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2) |


*Table: This table summarizes Harding ADCA type III and its component SCA subtypes using only the retrieved evidence. It compares genes/loci, mutation classes, onset, phenotypes, imaging, and epidemiology to support disease knowledge-base curation.*

---

## Visual Evidence

- Diagnostic algorithm for ADCA type III and ADCA III gene/subtype table (Fujioka et al. 2013) (fujioka2013autosomaldominantcerebellar media 92211852, fujioka2013autosomaldominantcerebellar media 9844df72, fujioka2013autosomaldominantcerebellar media 27541419).

---

## Key Gaps / Limitations in Retrieved Evidence
1. **Ontology identifiers** (MONDO/OMIM/Orphanet/MeSH/ICD) for ADCA type III and each SCA subtype were not present in the retrieved full texts; thus they cannot be reported with citations from this tool-run (fujioka2013autosomaldominantcerebellar pages 1-2, warrenburg2005autosomaldominantcerebellar pages 149-152, pilotto2024hereditaryataxiasfrom pages 3-4).
2. **SCA26/SCA30 modern gene discovery updates** (if any) and **2023–2024 subtype-specific clinical trials** for SCA5/SCA6/SCA31 were not captured in the accessible retrieved sources; the trial evidence here is primarily from ClinicalTrials.gov records and earlier subtype literature (NCT01811706 chunk 1, NCT01060371 chunk 1).
3. **Biomarkers/omics and quantitative natural-history metrics** for ADCA III as a group remain sparse in the retrieved evidence beyond subtype-focused imaging/physiology examples (kim2023clinicalvalueof pages 1-2).


References

1. (fujioka2013autosomaldominantcerebellar pages 1-2): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

2. (pilotto2024hereditaryataxiasfrom pages 3-4): Federica Pilotto, Andrea Del Bondio, and Hélène Puccio. Hereditary ataxias: from bench to clinic, where do we stand? Cells, 13:319, Feb 2024. URL: https://doi.org/10.3390/cells13040319, doi:10.3390/cells13040319. This article has 23 citations.

3. (warrenburg2005autosomaldominantcerebellar pages 149-152): BPC van de Warrenburg. Autosomal dominant cerebellar ataxias. clinical and genetic studies in dutch patients. Unknown journal, 2005.

4. (whaley2011autosomaldominantcerebellar pages 1-2): Nathaniel Robb Whaley, Shinsuke Fujioka, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type i: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6:33-33, May 2011. URL: https://doi.org/10.1186/1750-1172-6-33, doi:10.1186/1750-1172-6-33. This article has 120 citations and is from a peer-reviewed journal.

5. (ishikawa2023spinocerebellarataxiatype pages 1-2): Kinya Ishikawa. Spinocerebellar ataxia type 31 (sca31). Journal of Human Genetics, 68:153-156, Nov 2023. URL: https://doi.org/10.1038/s10038-022-01091-4, doi:10.1038/s10038-022-01091-4. This article has 12 citations and is from a peer-reviewed journal.

6. (felicio2024spinocerebellarataxiatype pages 1-2): Daniela Felício and Mariana Santos. Spinocerebellar ataxia type 11 (sca11): ttbk2 variants, functions and associated disease mechanisms. Cerebellum (London, England), 23:678-687, Mar 2024. URL: https://doi.org/10.1007/s12311-023-01540-6, doi:10.1007/s12311-023-01540-6. This article has 4 citations.

7. (fujioka2013autosomaldominantcerebellar pages 2-3): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

8. (fujioka2013autosomaldominantcerebellar pages 5-6): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

9. (fujioka2013autosomaldominantcerebellar pages 6-7): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

10. (felicio2024spinocerebellarataxiatype pages 2-4): Daniela Felício and Mariana Santos. Spinocerebellar ataxia type 11 (sca11): ttbk2 variants, functions and associated disease mechanisms. Cerebellum (London, England), 23:678-687, Mar 2024. URL: https://doi.org/10.1007/s12311-023-01540-6, doi:10.1007/s12311-023-01540-6. This article has 4 citations.

11. (kim2023clinicalvalueof pages 1-2): Jae-Myung Kim, Tai-Seung Nam, Seong-Min Choi, Byeong C. Kim, and Seung-Han Lee. Clinical value of vestibulo-ocular reflex in the differentiation of spinocerebellar ataxias. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-41924-6, doi:10.1038/s41598-023-41924-6. This article has 15 citations and is from a peer-reviewed journal.

12. (fujioka2013autosomaldominantcerebellar pages 3-5): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

13. (NCT01060371 chunk 1):  Natural History Study of and Genetic Modifiers in Spinocerebellar Ataxias. University of Florida. 2010. ClinicalTrials.gov Identifier: NCT01060371

14. (ishikawa2023spinocerebellarataxiatype pages 2-3): Kinya Ishikawa. Spinocerebellar ataxia type 31 (sca31). Journal of Human Genetics, 68:153-156, Nov 2023. URL: https://doi.org/10.1038/s10038-022-01091-4, doi:10.1038/s10038-022-01091-4. This article has 12 citations and is from a peer-reviewed journal.

15. (mattei2024epidemiologyofspinocerebellar pages 1-2): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

16. (mattei2024epidemiologyofspinocerebellar pages 4-5): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

17. (mattei2024epidemiologyofspinocerebellar pages 5-6): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

18. (fujioka2013autosomaldominantcerebellar media 92211852): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

19. (fujioka2013autosomaldominantcerebellar media 9844df72): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

20. (fujioka2013autosomaldominantcerebellar media 27541419): Shinsuke Fujioka, Christina Sundal, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type iii: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 8:14-14, Jan 2013. URL: https://doi.org/10.1186/1750-1172-8-14, doi:10.1186/1750-1172-8-14. This article has 50 citations and is from a peer-reviewed journal.

21. (coarelli2023theinheritedcerebellar pages 12-13): Giulia Coarelli, Thomas Wirth, Christine Tranchant, Michel Koenig, Alexandra Durr, and Mathieu Anheim. The inherited cerebellar ataxias: an update. Journal of Neurology, 270:208-222, Sep 2023. URL: https://doi.org/10.1007/s00415-022-11383-6, doi:10.1007/s00415-022-11383-6. This article has 84 citations and is from a domain leading peer-reviewed journal.

22. (NCT01811706 chunk 1):  Dalfampridine and Gait in Spinocerebellar Ataxias. University of Florida. 2013. ClinicalTrials.gov Identifier: NCT01811706