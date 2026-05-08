---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T13:24:15.827404'
end_time: '2026-05-08T13:43:36.197959'
duration_seconds: 1160.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dystrophic Epidermolysis Bullosa
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 88
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dystrophic Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dystrophic Epidermolysis Bullosa** covering all of the
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
- **Disease Name:** Dystrophic Epidermolysis Bullosa
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dystrophic Epidermolysis Bullosa** covering all of the
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


# Dystrophic Epidermolysis Bullosa (DEB) — Disease Characteristics Research Report (2026-05-08)

## Target disease
**Disease:** Dystrophic epidermolysis bullosa (DEB) (Mendelian mechanobullous genodermatosis).

**Note on identifiers (OMIM/Orphanet/ICD/MeSH/MONDO):** In this tool run, curated database identifier pages were not retrieved directly. The report therefore focuses on evidence-backed clinical/genetic characterization from the peer‑reviewed literature and ClinicalTrials.gov records; identifier fields are flagged as **not captured in retrieved evidence**.

---

## 1. Disease information
### Overview and definition
DEB is a major subtype of epidermolysis bullosa (EB), a group of inherited disorders with **skin and mucosal membrane blistering induced by mechanical trauma**. In DEB, pathogenic variants in **COL7A1** impair **type VII collagen (C7)** and thereby anchoring fibrils at the dermal–epidermal junction, causing separation **below the lamina densa (upper dermis/sub‑lamina densa)** (hou2023innovationsinthe pages 1-2, bischof2024emerginggenetherapeutics pages 1-2, zorina2024currentstatusof pages 1-2).

Recent review language defining the core concept: DEB is “caused by inherited pathogenic variants in the **COL7A1** gene, which encodes type VII collagen, the major component of **anchoring fibrils** which maintain adhesion between the outer epidermis and underlying dermis.” (Hou et al., 2023-06; URL: https://doi.org/10.2147/TCRM.S386923) (hou2023innovationsinthe pages 1-2).

### Subtypes / classification
DEB is subclassified by inheritance into:
- **Dominant DEB (DDEB)** (often milder).
- **Recessive DEB (RDEB)** (often severe with extensive blistering, chronic wounds, fibrosis/scarring and high cancer risk). (hou2023innovationsinthe pages 1-2)

### Synonyms / alternative names (from literature usage)
- Dystrophic epidermolysis bullosa (DEB)
- Dominant dystrophic epidermolysis bullosa (DDEB)
- Recessive dystrophic epidermolysis bullosa (RDEB)
- RDEB generalized severe / generalized intermediate (terminology used in registry cohorts) (kim2018epidemiologyandoutcome pages 3-4, kim2018epidemiologyandoutcome pages 1-2)

### Evidence source type
The information above is derived primarily from **aggregated disease-level resources in peer‑reviewed reviews**, and **registry/cohort studies** for outcomes (hou2023innovationsinthe pages 1-2, bischof2024emerginggenetherapeutics pages 1-2, robertson2021cutaneoussquamouscell pages 3-3, kim2018epidemiologyandoutcome pages 1-2).

---

## 2. Etiology
### Disease causal factors
**Primary cause:** germline pathogenic variants in **COL7A1** causing reduced/absent functional type VII collagen (C7), leading to loss/dysfunction of anchoring fibrils and mechanical fragility with sub‑lamina densa blistering (hou2023innovationsinthe pages 1-2, zorina2024currentstatusof pages 1-2).

**Dominant vs recessive molecular patterns (current understanding):** Reviews emphasize that DDEB commonly involves **glycine substitutions in the C7 triple helix**, while RDEB is frequently driven by **loss-of-function** variants (nonsense/frameshift/splice) that reduce/abolish C7 (hou2023innovationsinthe pages 2-5, zorina2024currentstatusof pages 1-2).

### Risk factors
Because DEB is monogenic, “risk factors” are predominantly genetic:
- **Family history / carrier status** (autosomal dominant or autosomal recessive inheritance, depending on subtype). (hou2023innovationsinthe pages 1-2, shehata2024geneticimplicationsand pages 7-8)
- **Consanguinity** can increase the frequency of autosomal recessive EB/DEB in some populations (reported in a Saudi cohort). (Shehata et al., 2024-08; https://doi.org/10.7759/cureus.66678) (shehata2024geneticimplicationsand pages 7-7)

### Protective factors
No validated protective genetic variants or environmental protective factors were identified in the retrieved evidence.

### Gene–environment interactions
DEB blistering is mechanically provoked; environmental friction/trauma triggers lesions on a genetically fragile dermal–epidermal junction, but formal GxE interaction studies were not identified in this run.

---

## 3. Phenotypes
### Core clinical phenotype spectrum
Across reviews and cohorts, DEB/RDEB is characterized by:
- **Trauma-induced blistering and erosions** of skin and mucosae (hou2023innovationsinthe pages 1-2, azevedo2023fibrosisasa pages 1-2)
- **Chronic nonhealing wounds** with recurrent breakdown (hou2023innovationsinthe pages 1-2, tartaglia2021impairedwoundhealing pages 1-2)
- **Scarring and fibrosis** (including progressive deformity such as “mitten” deformities in severe RDEB due to scarring) (zorina2024currentstatusof pages 1-2)
- **Systemic complications** (commonly cited in reviews): anemia, malnutrition, osteoporosis, failure to thrive, strictures (danescu2024treatmentofepidermolysis pages 1-4, hou2023innovationsinthe pages 1-2)
- **Pain and pruritus** are prominent symptoms; supportive management remains central (stone2024creationandcharacterization pages 1-2)
- **Cutaneous squamous cell carcinoma (cSCC)**: high-risk complication particularly in severe generalized RDEB (hou2023innovationsinthe pages 1-2, robertson2021cutaneoussquamouscell pages 3-3)

A mechanistic systematic review frames the wound-to-fibrosis-to-cancer phenotype chain: “The alteration in col VII expression leads to the formation of recurrent bullae… subsequent events are deficient healing associated with an intense inflammatory process resulting in the development of chronic wounds… creating a vicious cycle… [that] contribute[s] to a microenvironment favorable to epithelial carcinogenesis.” (de Azevedo et al., 2023-02; https://doi.org/10.1055/s-0043-1763257) (azevedo2023fibrosisasa pages 4-5).

### Age of onset and progression (typical)
DEB is generally **congenital/early onset**, with lifelong mechanobullous disease. Disease course is typically **chronic and progressive** in severe RDEB with cumulative scarring/fibrosis and increasing risk of cSCC in early adulthood (hou2023innovationsinthe pages 1-2, robertson2021cutaneoussquamouscell pages 3-3).

### Quality-of-life impact
Retrieved evidence emphasizes substantial daily burden and “extremely poor quality of life” in RDEB (e.g., systemic involvement and early death described in preclinical therapeutic work), but this run did not retrieve quantitative QOLEB/EBDASI/QoL instrument summary statistics (hou2023innovationsinthe pages 1-2, paboncarrasco2024managementofskin pages 6-7). This is a gap for knowledge-base fields requiring numeric QoL values.

### Suggested HPO terms (examples; non-exhaustive)
- Skin blistering: **HP:0032123** (Blistering of the skin)
- Skin erosions: **HP:0001058** (Skin erosion)
- Skin fragility: **HP:0001035** (Fragile skin)
- Abnormal scarring: **HP:0100699** (Abnormal scar)
- Cutaneous squamous cell carcinoma: **HP:0006732** (Squamous cell carcinoma)
- Nail dystrophy: **HP:0008404** (Nail dystrophy)
- Pruritus: **HP:0000989** (Pruritus)
- Pain: **HP:0012531** (Pain)
- Anemia: **HP:0001903** (Anemia)
- Failure to thrive: **HP:0001508** (Failure to thrive)
- Esophageal stricture: **HP:0002043** (Esophageal stricture)

---

## 4. Genetic / molecular information
### Causal gene(s)
- **COL7A1** (type VII collagen α1 chain) is the causal gene for DEB, encoding C7 that forms anchoring fibrils at the dermal–epidermal junction/basement membrane zone (hou2023innovationsinthe pages 1-2, zorina2024currentstatusof pages 1-2).

### Pathogenic variant classes and consequences
- **Loss-of-function (RDEB):** reduced/absent C7 leading to absent/insufficient anchoring fibrils; sub‑lamina densa cleavage and severe blistering and chronic wounds (zorina2024currentstatusof pages 1-2, azevedo2023fibrosisasa pages 1-2).
- **Dominant-negative / structural (DDEB):** glycine substitutions in the triple helix domain are highlighted as common dominant patterns in reviews (hou2023innovationsinthe pages 2-5).
- **Splice variants and deep intronic variants:** 2024 work demonstrates deep intronic loss‑of‑function variants causing aberrant splicing can be corrected in patient keratinocytes/fibroblasts via antisense oligonucleotides (ASOs), restoring normal splicing to >94% and C7 protein up to ~56% of normal (Pironon et al., 2024-08; https://doi.org/10.1073/pnas.2401781121) (pironon2024splicemodulationstrategy pages 1-2, pironon2024splicemodulationstrategy pages 4-6).

### Recent developments (2023–2024) in variant-targeted correction
- **Splice modulation / ASO splicing enhancement:** Hainzl et al. (2024-01; https://doi.org/10.3390/ijms25020761) screened 2′‑MOE ASOs in RDEB cells with c.425A>G and identified candidates increasing correctly spliced COL7A1 transcripts (ddPCR ~3.8–4.2-fold for leading ASOs), with increased full‑length C7 in RDEB skin equivalents (hainzl2024splicingmodulationvia pages 7-10, hainzl2024splicingmodulationvia pages 1-2).
- **Exon skipping:** A DEB treatment review describes exon-skipping logic (“Of the 118 exons in COL7A1, 80 of these could be skipped in frame”) and notes topical exon‑73 ASO trial NCT03605069 had low uptake/limited efficacy; follow-on PTW‑002 is in clinical testing (NCT05529134) (hou2023innovationsinthe pages 6-8).

### Modifier genes / epigenetics / chromosomal abnormalities
Evidence for specific modifier genes and epigenetic signatures was not directly retrieved in this run (although some cohort papers mention modifiers in passing). This should be filled from curated genetics resources or dedicated modifier studies.

---

## 5. Environmental information
DEB is primarily genetic. Environmental contributors are mainly **mechanical trauma/friction** triggering blistering. No toxin/pollution/infectious etiology was identified in retrieved evidence.

---

## 6. Mechanism / pathophysiology
### Causal chain (from trigger to clinical manifestations)
1. **Germline COL7A1 variants → reduced/abnormal C7** (hou2023innovationsinthe pages 1-2, zorina2024currentstatusof pages 1-2).
2. **C7 deficiency → impaired anchoring fibrils → skin cleavage below lamina densa** causing mechanical fragility and blistering (azevedo2023fibrosisasa pages 1-2, condorelli2019epidermolysisbullosaassociatedsquamous pages 8-10).
3. **Recurrent wounding** with chronic nonhealing ulcers, often with bacterial colonization that perpetuates inflammation (condorelli2019epidermolysisbullosaassociatedsquamous pages 8-10, azevedo2023fibrosisasa pages 4-5).
4. **Fibrosis amplification loop:** inflammatory infiltrates and myofibroblasts produce TGF‑β1, sustaining a self‑renewing fibrotic process and ECM stiffening; fibroblasts can acquire CAF‑like transcriptional features (condorelli2019epidermolysisbullosaassociatedsquamous pages 8-10, condorelli2019epidermolysisbullosaassociatedsquamous pages 6-8).
5. **Carcinogenesis:** chronic wounds + inflammation + fibrosis create a permissive tumor microenvironment; RDEB cSCC often arises in chronic wound/scar sites rather than UV-driven pathways (azevedo2023fibrosisasa pages 4-5, robertson2021cutaneoussquamouscell pages 1-2).

Mechanistic quote emphasizing signaling beyond structural failure: “absent expression of wild-type C7 in RDEB dermal fibroblasts… leads to increased TGFβ signaling and a disruption to ECM protein organization and composition that is tumor-promoting.” (Tartaglia et al., 2021-05; https://doi.org/10.3390/ijms22105104) (tartaglia2021impairedwoundhealing pages 2-4).

### Upstream vs downstream
- **Upstream:** COL7A1 loss/dysfunction; anchoring fibril failure (hou2023innovationsinthe pages 1-2, zorina2024currentstatusof pages 1-2)
- **Downstream:** chronic inflammation, TGF‑β signaling, myofibroblast differentiation, ECM remodeling and stiffness, impaired re‑epithelialization, tumor microenvironment and cSCC (condorelli2019epidermolysisbullosaassociatedsquamous pages 6-8, tartaglia2021impairedwoundhealing pages 2-4).

### Cell types involved (suggested CL terms)
- Basal keratinocyte (**CL:0000312**; keratinocyte)
- Dermal fibroblast (**CL:0000057**; fibroblast)
- Myofibroblast (**CL:0000186**; myofibroblast)
- Macrophage (**CL:0000235**) and neutrophil/granulocyte (**CL:0000775**) in chronic wound inflammation (tartaglia2021impairedwoundhealing pages 2-4)

### Molecular pathways / GO term suggestions
- TGF‑β signaling pathway (**GO:0007179**)
- Extracellular matrix organization (**GO:0030198**)
- Wound healing (**GO:0042060**)
- Inflammatory response (**GO:0006954**)
- Epithelial to mesenchymal transition (**GO:0001837**) (discussed in RDEB-SCC context) (condorelli2019epidermolysisbullosaassociatedsquamous pages 8-10)

---

## 7. Anatomical structures affected
### Organ/tissue level
- **Skin** (primary) and **mucous membranes** (hou2023innovationsinthe pages 1-2, azevedo2023fibrosisasa pages 1-2)
- **Basement membrane zone / dermal–epidermal junction** (structural locus of failure) (zorina2024currentstatusof pages 1-2)

Suggested UBERON terms
- Skin: **UBERON:0002097**
- Epidermis: **UBERON:0001003**
- Dermis: **UBERON:0002067**
- Basement membrane: **UBERON:0003725**

Subcellular / molecular localization (suggested GO CC)
- Extracellular matrix: **GO:0031012**
- Basement membrane: **GO:0005604**

---

## 8. Temporal development
- **Onset:** typically congenital/early life, given monogenic structural defect (hou2023innovationsinthe pages 1-2, zorina2024currentstatusof pages 1-2).
- **Course:** chronic lifelong; severe RDEB is progressive with cumulative scarring/fibrosis and increasing cSCC risk in early adulthood (hou2023innovationsinthe pages 1-2, robertson2021cutaneoussquamouscell pages 3-3).
- **Critical period:** adolescence/early adulthood for rising cSCC risk, motivating early surveillance (kim2018epidemiologyandoutcome pages 5-6, bonamonte2022squamouscellcarcinoma pages 6-8).

---

## 9. Inheritance and population
### Inheritance patterns
- **Autosomal dominant** (DDEB) and **autosomal recessive** (RDEB) (hou2023innovationsinthe pages 1-2, nikolova2024autosomalrecessivetype pages 2-4).

### Epidemiology (recent summarized estimates)
- EB incidence ~40–60 per 1,000,000 live births; prevalence ~20–30 per 1,000,000 in some countries (England/Wales, Netherlands) (Bischof et al., 2024-02; https://doi.org/10.3390/ijms25042243) (bischof2024emerginggenetherapeutics pages 1-2).
- DEB may represent ~30% of EB cases (Hou et al., 2023-06; https://doi.org/10.2147/TCRM.S386923) (hou2023innovationsinthe pages 1-2).

### High-impact complication epidemiology: RDEB-associated cSCC
RDEB carries extremely high age-dependent cSCC risk and poor survival:
- In the US National EB Registry estimates summarized in a London cohort paper: cumulative risk of ≥1 SCC in severe RDEB ~7.5% by age 20, 67.8% by 35, 90.1% by 55, with SCC-related death risk ~38.7% by 35 and ~70% by 45 (robertson2021cutaneoussquamouscell pages 3-3).
- Australasian registry: cumulative risk of SCC by age 35 was 76.1% in RDEB generalized severe vs 10% in generalized intermediate; median survival after first SCC 4 years (severe) and 5 years (intermediate) (Kim et al., 2018-01; https://doi.org/10.2340/00015555-2781) (kim2018epidemiologyandoutcome pages 3-4, kim2018epidemiologyandoutcome pages 1-2).

---

## 10. Diagnostics
### Recommended diagnostic approach (evidence-backed components)
EB/DEB classification is anchored to the **level of skin cleavage** and confirmation by a combination of:
- **Immunofluorescence antigen mapping (IFM)** on skin biopsy
- **Transmission electron microscopy (TEM/EM)** to localize cleavage plane and anchoring fibril defects
- **Molecular testing** (NGS gene panels/WES) for COL7A1 variants interpreted under ACMG criteria (montaudie2016inheritedepidermolysisbullosa pages 1-2, nikolova2024autosomalrecessivetype pages 1-2, nikolova2024autosomalrecessivetype pages 2-4).

A case-based diagnostic statement: the “most effective diagnostic approach… combines TEM and immunofluorescence antigen mapping… together with DNA mutational analysis,” and NGS is described as preferable for cost-effective multi-variant screening (Nikolova et al., 2024-09; https://doi.org/10.3892/br.2024.1855) (nikolova2024autosomalrecessivetype pages 1-2).

Real-world implementation example (referral center workflow): In a Romanian ERN-Skin affiliated center, patients received clinical assessment with IFM/TEM and molecular testing when available (molecular testing performed in 29/56; IFM in 5; TEM in 10), illustrating staged diagnosis constrained by access/logistics (Suru et al., 2024-05; https://doi.org/10.7759/cureus.61160) (suru2024descriptivestudyof pages 2-4).

### Genetic testing approaches
- **NGS panels** (multi-gene EB panels) (shehata2024geneticimplicationsand pages 7-7, nikolova2024autosomalrecessivetype pages 1-2)
- **WES** (noted in pediatric case literature) (ali2024epidermolysisbullosatwo pages 12-13)

### Differential diagnosis
Not comprehensively captured in the retrieved evidence; would typically include other EB subtypes (EBS, JEB, Kindler EB) and other blistering disorders, but specific evidence-backed differential criteria were not retrieved here.

---

## 11. Outcomes / prognosis
### Prognosis dominated by severe RDEB complications, especially cSCC
A 28-year London retrospective study reported for severe RDEB: metastatic disease in 16/31 (52%), SCC-associated mortality 64.5%, and **median survival after first SCC 2.4 years** (Robertson et al., 2021-07; https://doi.org/10.2340/00015555-3875) (robertson2021cutaneoussquamouscell pages 1-2, robertson2021cutaneoussquamouscell pages 3-3).

Systematic review synthesis (2024): in 157 RDEB-cSCC cases, median age at diagnosis was 30 years (range 6–68.4), and among cases with survival data, median survival after first cSCC varied with treatments (e.g., surgery only ~2 years; immunotherapy ~4.6 years; anti‑EGFR therapy ~4.0 years), noting small sample sizes (Hwang et al., 2024-05; https://doi.org/10.1186/s13023-024-03190-1) (hwang2024therapiesforcutaneous pages 1-3).

---

## 12. Treatment
### Current applications / real-world implementations (supportive and multidisciplinary)
Current best practice remains **multidisciplinary supportive care**, prioritizing wound care, infection prevention/management, pain and itch control, nutrition, and treatment of complications (danescu2024treatmentofepidermolysis pages 1-4, shehata2024geneticimplicationsand pages 7-8).

### FDA-approved causal/molecular therapy (major 2023 milestone)
**Beremagene geperpavec (B‑VEC; VYJUVEK)** is an in vivo topical gene therapy using a non‑replicating HSV‑1 vector delivering COL7A1 to promote C7 expression and anchoring fibril assembly.

Evidence from the phase 1/2 trial report emphasizes safety and molecular correction: in a randomized, placebo-controlled phase 1/2 trial (NCT03536143), “No grade 2 or above B‑VEC-related adverse events or vector shedding… were noted,” and primary/secondary objectives including “C7 expression” and “anchoring fibril assembly” and wound-closure outcomes were met (Gurevich et al., 2022-03; https://doi.org/10.1038/s41591-022-01737-y) (gurevich2022invivotopical pages 1-2).

Quantitative efficacy (from 2024 therapy review summarizing trials):
- Phase 1/2 (NCT03536143): 10/12 (83%) B‑VEC wounds closed vs 1/7 (14%) placebo at 12 weeks (koutsoukos2024highlightsofgene pages 5-7).
- Phase 3: complete wound healing reported as 67% B‑VEC vs 22% placebo, and 71% vs 20% at 3 months in summary sources (koutsoukos2024highlightsofgene pages 5-7, paboncarrasco2024managementofskin pages 6-7).

**Mechanistic tissue restoration evidence from figures/tables:** Gurevich et al. include tabulated wound closure endpoints and images showing restored C7 at the dermal–epidermal junction and mature anchoring fibrils after therapy (gurevich2022invivotopical media 3ae5ad4d, gurevich2022invivotopical media 80fb8fb9).

### Other advanced therapeutics (2023–2024 research emphasis)
- **Ex vivo gene-corrected epidermal grafts (EB‑101):** Review synthesis reports durable wound closure at multi-year follow-up for gene-corrected autologous keratinocyte grafts (hou2023innovationsinthe pages 2-5).
- **Splice modulation / exon skipping (ASOs):** active 2024 preclinical work (Hainzl 2024; Pironon 2024) demonstrating restoration of correct COL7A1 splicing and partial C7 rescue, including deep intronic variant targeting (pironon2024splicemodulationstrategy pages 1-2, hainzl2024splicingmodulationvia pages 1-2).
- **Readthrough therapy:** IV gentamicin open-label pilot in nonsense-variant RDEB increased C7 at the DEJ and reported >85% closure of monitored wounds at 1 and 3 months in three participants (Woodley et al., 2024-02; https://doi.org/10.1093/bjd/ljae063) (danescu2024treatmentofepidermolysis pages 1-4).

### Clinical trials (examples; not exhaustive)
- B‑VEC phase 1/2: **NCT03536143** (NCT03536143 chunk 1)
- Exon 73 ASO programs: **NCT03605069** (terminated) and **NCT05529134** (PTW‑002) (pironon2024splicemodulationstrategy pages 6-7, hou2023innovationsinthe pages 6-8)
- EB‑101 phase 3 (ex vivo gene therapy): **NCT04227106** (retrieved in trials list)

### MAXO suggestions (selected)
- Topical gene therapy: **MAXO:0000123** (Gene therapy; general)
- Skin wound care: **MAXO:0000756** (Wound care)
- Pain management: **MAXO:0000747** (Pain management)
- Genetic counseling: **MAXO:0000079** (Genetic counseling)

---

## 13. Prevention
### Primary prevention (disease occurrence)
Because DEB is genetic, primary prevention is via **reproductive risk management**:
- After identifying a causal variant in an affected individual, “biological parents and siblings should undergo carrier status testing… following genetic counseling guidelines.” (Shehata et al., 2024-08; https://doi.org/10.7759/cureus.66678) (shehata2024geneticimplicationsand pages 7-8).

### Secondary prevention (early detection)
**cSCC surveillance** is a critical prevention strategy in severe RDEB.
- Review guidance: full skin exam every **3–6 months from age 10** for the highest-risk RDEB patients, with shorter intervals for those with prior cSCC (Bonamonte et al., 2022-04; https://doi.org/10.3390/cells11081365) (bonamonte2022squamouscellcarcinoma pages 6-8).
- Registry guidance: “Regular skin checks at least every **3 months** are… vital,” with biopsy triggers for persistent ulcers/hyperkeratosis and a goal of rapid excision of biopsy-proven SCC (Kim et al., 2018-01; https://doi.org/10.2340/00015555-2781) (kim2018epidemiologyandoutcome pages 5-6).

### Tertiary prevention (complication prevention)
- Multidisciplinary specialized EB centers integrating dermatology, genetics, pain management, nutrition, and wound care are advocated to reduce complication burden (shehata2024geneticimplicationsand pages 7-8).

---

## 14. Other species / natural disease
Naturally occurring DEB/RDEB-like disease has been reported in multiple species including **dogs, cats, cattle, sheep, goats, and ostriches**, with limited utility of some animal cases for therapy testing (Stone et al., 2024-05; https://doi.org/10.1371/journal.pone.0302991) (stone2024creationandcharacterization pages 1-2).

---

## 15. Model organisms
### In vivo genetic models
- **Mouse models:** Col7a1 knockout mice show severe blistering and early death; hypomorphic mice (~10% Col7a1 expression) recapitulate blistering, nail dystrophy, mitten deformities but do not capture patient-specific compound heterozygosity well (takaki2022generationofa pages 1-2).
- **Patient-mutation compound heterozygous mouse models:** CRISPR/i‑GONAD enabled creation of a mouse model carrying patient-derived compound heterozygous mutations, supporting genotype-relevant studies and including single-cell transcriptomics readouts (Takaki et al., 2022-06; https://doi.org/10.1038/s41374-022-00735-5) (takaki2022generationofa pages 1-2).
- **New rat model (2024):** a Lewis rat Col7a1del8/del8 model (8-bp deletion causing a premature stop) shows severe postnatal blistering with absent anchoring fibrils, offering larger surface area for topical/transfusion therapy testing but limited survival (median ~3 days) (stone2024creationandcharacterization pages 7-9, stone2024creationandcharacterization pages 9-10).

### Human cell and xenograft models
- **iPSC-derived skin equivalents / xenografts:** gene-corrected iPS-derived skin constructs grafted onto immunodeficient mice restored collagen VII expression and anchoring fibrils (koutsoukos2024highlightsofgene pages 5-7).

---

## Recent quantitative statistics (quick reference)
The following table consolidates key epidemiology, cSCC outcomes, and B‑VEC efficacy endpoints with URLs and publication dates.

| Finding/Metric | Population/Subtype | Value | Study type | Source (authors/year) | Publication date/month | URL/DOI | Evidence citation id |
|---|---|---:|---|---|---|---|---|
| EB incidence | EB overall | ~19.6 per 1,000,000 live-born infants | Review | Shehata et al. 2024 | 2024-08 | https://doi.org/10.7759/cureus.66678 | (shehata2024geneticimplicationsand pages 1-4) |
| EB incidence | EB overall | ~40–60 per 1,000,000 live births | Review | Bischof et al. 2024 | 2024-02 | https://doi.org/10.3390/ijms25042243 | (bischof2024emerginggenetherapeutics pages 1-2) |
| EB prevalence | EB overall | ~20–30 per 1,000,000 people (England/Wales, Netherlands) | Review | Bischof et al. 2024 | 2024-02 | https://doi.org/10.3390/ijms25042243 | (bischof2024emerginggenetherapeutics pages 1-2) |
| EB prevalence | EB overall (USA) | 8.22 per 1,000,000 | Review | Bonamonte et al. 2022 | 2022-04 | https://doi.org/10.3390/cells11081365 | (bonamonte2022squamouscellcarcinoma pages 1-2) |
| DEB prevalence | DEB overall | ~6 per 1,000,000 in USA/Spain; up to 20 per 1,000,000 in Scotland | Review | Bonamonte et al. 2022 | 2022-04 | https://doi.org/10.3390/cells11081365 | (bonamonte2022squamouscellcarcinoma pages 1-2) |
| DEB proportion among EB | DEB among all EB cases | ~30% | Review | Hou et al. 2023 | 2023-06 | https://doi.org/10.2147/TCRM.S386923 | (hou2023innovationsinthe pages 1-2) |
| DEB proportion among EB | Saudi cohort of EB patients | 42.9% (12/28) | Retrospective cohort | Shehata et al. 2024 | 2024-08 | https://doi.org/10.7759/cureus.66678 | (shehata2024geneticimplicationsand pages 7-7) |
| DEB proportion among EB | Romanian referral-center cohort | 55.4% (31/56) | Retrospective cohort | Suru et al. 2024 | 2024-05 | https://doi.org/10.7759/cureus.61160 | (suru2024descriptivestudyof pages 2-4) |
| cSCC cumulative risk by age | RDEB-severe / RDEB-HS | 7.5% by age 20; 67.8% by 35; 80.2% by 45; 90.1% by 55 | Registry/cohort data summarized in retrospective study | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| cSCC cumulative risk by age | RDEB-severe / RDEB-HS | 7.5% by age 20; 52% by 30; 80% by 45 | Systematic review citing cohort/registry estimates | Hwang et al. 2024 | 2024-05 | https://doi.org/10.1186/s13023-024-03190-1 | (hwang2024therapiesforcutaneous pages 1-3) |
| cSCC cumulative risk by age | RDEB-generalized severe | 26.3% by age 20; 76.1% by 35 | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 3-4, kim2018epidemiologyandoutcome pages 1-2) |
| cSCC cumulative risk by age | RDEB-generalized intermediate | 10% by age 35; 66.7% by 65 | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 3-4) |
| cSCC-related death cumulative risk by age | RDEB-severe / RDEB-HS | 38.7% by age 35; 70.0% by 45; 78.7% by 55 | Registry/cohort data summarized in retrospective study | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| cSCC-related death cumulative risk by age | RDEB-generalized severe | 30% by age 25; 84.4% by age 34 | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 3-4) |
| Median age at first cSCC | EB overall in London cohort | 32.8 years | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| Median age at first cSCC | RDEB-severe | 29.5 years (range 13–52) | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3, robertson2021cutaneoussquamouscell pages 1-2) |
| Median age at cSCC diagnosis | RDEB cSCC cases | 30 years (range 6–68.4) | Systematic review | Hwang et al. 2024 | 2024-05 | https://doi.org/10.1186/s13023-024-03190-1 | (hwang2024therapiesforcutaneous pages 1-3) |
| Median age at first cSCC | Australasian RDEB cohort | 30 years (earliest 16, latest 62) | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 1-2) |
| Metastatic rate | EB patients with cSCC overall (London cohort) | 17/44 (39%) | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| Metastatic rate | RDEB-severe with cSCC (London cohort) | 16/31 (52%) | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| Metastatic rate | EB-cSCC patients (Dutch registry) | 11/22 (50%) developed metastases; all 11 died | Registry cohort | Harrs et al. 2022 | 2022-11 | https://doi.org/10.1111/bjd.21769 | (harrs2022theaggressivebehaviour pages 1-1) |
| SCC-associated mortality | EB patients with cSCC overall (London cohort) | 25/44 (57%) died | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| SCC-associated mortality | RDEB-severe with cSCC (London cohort) | 21/31 (68%) died; 20/21 deaths SCC-related | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| Median survival after first cSCC | EB overall (London cohort) | 2.1 years | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 3-3) |
| Median survival after first cSCC | RDEB-severe (London cohort) | 2.4 years (range 0.5–12.6) | Retrospective cohort | Robertson et al. 2021 | 2021-07 | https://doi.org/10.2340/00015555-3875 | (robertson2021cutaneoussquamouscell pages 1-2) |
| Median survival after first cSCC | RDEB-generalized severe | 4 years | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 3-4, kim2018epidemiologyandoutcome pages 1-2) |
| Median survival after first cSCC | RDEB-generalized intermediate | 5 years | Registry cohort | Kim et al. 2018 | 2018-01 | https://doi.org/10.2340/00015555-2781 | (kim2018epidemiologyandoutcome pages 3-4) |
| Median survival after first cSCC | RDEB-severe (Dutch registry) | 41 months | Registry cohort | Harrs et al. 2022 | 2022-11 | https://doi.org/10.1111/bjd.21769 | (harrs2022theaggressivebehaviour pages 1-1) |
| B-VEC phase 1/2 wound closure at 12 weeks | RDEB wounds treated in NCT03536143 | 10/12 (83%) wounds closed with B-VEC vs 1/7 (14%) placebo | Randomized placebo-controlled phase 1/2 trial | Gurevich et al. 2022 / summarized by Koutsoukos et al. 2024 | 2022-03 / 2024-08 | https://doi.org/10.1038/s41591-022-01737-y ; https://doi.org/10.1007/s13555-024-01239-4 | (koutsoukos2024highlightsofgene pages 5-7, gurevich2022invivotopical pages 1-2, gurevich2022invivotopical media 3ae5ad4d) |
| B-VEC phase 1/2 median time to closure | RDEB wounds treated in NCT03536143 | 13.5 days vs 22.5 days placebo | Randomized placebo-controlled phase 1/2 trial | Koutsoukos et al. 2024 | 2024-08 | https://doi.org/10.1007/s13555-024-01239-4 | (koutsoukos2024highlightsofgene pages 5-7) |
| B-VEC phase 1/2 median duration of closure | RDEB wounds treated in NCT03536143 | 103.0 days vs 16.5 days placebo | Randomized placebo-controlled phase 1/2 trial | Koutsoukos et al. 2024 | 2024-08 | https://doi.org/10.1007/s13555-024-01239-4 | (koutsoukos2024highlightsofgene pages 5-7) |
| B-VEC phase 1/2 responder analysis | RDEB wounds treated in NCT03536143 | 79% B-VEC responders vs 0% placebo; P=0.0026 | Randomized placebo-controlled phase 1/2 trial | Gurevich et al. 2022 | 2022-03 | https://doi.org/10.1038/s41591-022-01737-y | (gurevich2022invivotopical media 3ae5ad4d) |
| B-VEC phase 3 complete wound healing | DEB patients aged ≥6 months | 67% of B-VEC-treated wounds healed vs 22% placebo | Phase 3 double-blind intrapatient randomized placebo-controlled trial | Koutsoukos et al. 2024 | 2024-08 | https://doi.org/10.1007/s13555-024-01239-4 | (koutsoukos2024highlightsofgene pages 5-7) |
| B-VEC phase 3 complete wound healing at 3 months | DEB patients aged ≥6 months | 71% with B-VEC vs 20% placebo | Phase 3 double-blind intrapatient randomized placebo-controlled trial | Koutsoukos et al. 2024 / Pabón-Carrasco et al. 2024 | 2024-08 / 2024-01 | https://doi.org/10.1007/s13555-024-01239-4 ; https://doi.org/10.3390/healthcare12020261 | (koutsoukos2024highlightsofgene pages 5-7, paboncarrasco2024managementofskin pages 6-7) |
| B-VEC phase 3 pain during dressing changes | DEB patients in phase 3 trial | Mean change to week 22: −0.88 with B-VEC vs −0.71 placebo | Phase 3 double-blind intrapatient randomized placebo-controlled trial | Pabón-Carrasco et al. 2024 | 2024-01 | https://doi.org/10.3390/healthcare12020261 | (paboncarrasco2024managementofskin pages 6-7) |
| B-VEC regulatory milestone | DDEB and RDEB / DEB wounds | FDA approval May 2023; first topical gene therapy approved for DEB wounds | Regulatory summary/review | Koutsoukos et al. 2024; Raymakers et al. 2024 | 2024-08 / 2024-03 | https://doi.org/10.1007/s13555-024-01239-4 ; https://doi.org/10.1001/jamadermatol.2023.5857 | (koutsoukos2024highlightsofgene pages 5-7) |


*Table: This table compiles key quantitative epidemiology, cSCC outcome data, and B-VEC trial efficacy metrics for dystrophic epidermolysis bullosa from recent reviews, cohort studies, and trials. It is useful as a quick-reference evidence summary for disease burden, prognosis, and emerging therapy performance.*

---

## Key figures/tables supporting B‑VEC molecular correction (visual evidence)
- Wound closure endpoint table and longitudinal wound area reduction plots: (gurevich2022invivotopical media 3ae5ad4d)
- Restored collagen VII immunofluorescence at the dermal–epidermal junction: (gurevich2022invivotopical media 80fb8fb9)
- Anchoring fibril assembly by immunoelectron microscopy: (gurevich2022invivotopical media 2ab3990c)

---

## Limitations of this report (evidence not retrieved in this run)
- Curated identifier mappings (OMIM, Orphanet, ICD‑10/ICD‑11, MeSH, MONDO) were not retrieved via the available tools in this session.
- Quantitative, instrument-based quality-of-life statistics (QOLEB, SF‑36, EQ‑5D) were not retrieved.
- Differential diagnosis criteria were not comprehensively retrieved.

These gaps should be filled by targeted retrieval from GeneReviews/OMIM/Orphanet/HPO/MeSH and EB consensus guideline documents.

References

1. (hou2023innovationsinthe pages 1-2): Ping-Chen Hou, Nathalie del Agua, Su M Lwin, Chao-Kai Hsu, and John A McGrath. Innovations in the treatment of dystrophic epidermolysis bullosa (deb): current landscape and prospects. Therapeutics and Clinical Risk Management, 19:455-473, Jun 2023. URL: https://doi.org/10.2147/tcrm.s386923, doi:10.2147/tcrm.s386923. This article has 58 citations and is from a peer-reviewed journal.

2. (bischof2024emerginggenetherapeutics pages 1-2): Johannes Bischof, Markus Hierl, and Ulrich Koller. Emerging gene therapeutics for epidermolysis bullosa under development. International Journal of Molecular Sciences, 25:2243, Feb 2024. URL: https://doi.org/10.3390/ijms25042243, doi:10.3390/ijms25042243. This article has 37 citations.

3. (zorina2024currentstatusof pages 1-2): Alla Zorina, Vadim Zorin, Artur Isaev, Dmitry Kudlay, Natalia Manturova, Andrei Ustugov, and Pavel Kopnin. Current status of biomedical products for gene and cell therapy of recessive dystrophic epidermolysis bullosa. International Journal of Molecular Sciences, 25:10270, Sep 2024. URL: https://doi.org/10.3390/ijms251910270, doi:10.3390/ijms251910270. This article has 5 citations.

4. (kim2018epidemiologyandoutcome pages 3-4): Minhee Kim, Minmin Li, Lizbeth R. A. INTONG-WHEELER, K. Tran, D. Marucci, and D. Murrell. Epidemiology and outcome of squamous cell carcinoma in epidermolysis bullosa in australia and new zealand. Acta dermato-venereologica, 98 1:70-76, Jan 2018. URL: https://doi.org/10.2340/00015555-2781, doi:10.2340/00015555-2781. This article has 64 citations and is from a domain leading peer-reviewed journal.

5. (kim2018epidemiologyandoutcome pages 1-2): Minhee Kim, Minmin Li, Lizbeth R. A. INTONG-WHEELER, K. Tran, D. Marucci, and D. Murrell. Epidemiology and outcome of squamous cell carcinoma in epidermolysis bullosa in australia and new zealand. Acta dermato-venereologica, 98 1:70-76, Jan 2018. URL: https://doi.org/10.2340/00015555-2781, doi:10.2340/00015555-2781. This article has 64 citations and is from a domain leading peer-reviewed journal.

6. (robertson2021cutaneoussquamouscell pages 3-3): S. Robertson, E. Orrin, M. Lakhan, G. O’Sullivan, J. Felton, A. Robson, D. Greenblatt, C. Bernardis, J. McGrath, Anna E. Martinez, and J. Mellerio. Cutaneous squamous cell carcinoma in epidermolysis bullosa: a 28-year retrospective study. Acta Dermato-Venereologica, 101:adv00523, Jul 2021. URL: https://doi.org/10.2340/00015555-3875, doi:10.2340/00015555-3875. This article has 55 citations and is from a domain leading peer-reviewed journal.

7. (hou2023innovationsinthe pages 2-5): Ping-Chen Hou, Nathalie del Agua, Su M Lwin, Chao-Kai Hsu, and John A McGrath. Innovations in the treatment of dystrophic epidermolysis bullosa (deb): current landscape and prospects. Therapeutics and Clinical Risk Management, 19:455-473, Jun 2023. URL: https://doi.org/10.2147/tcrm.s386923, doi:10.2147/tcrm.s386923. This article has 58 citations and is from a peer-reviewed journal.

8. (shehata2024geneticimplicationsand pages 7-8): Nancy A Shehata, Noor A Shaik, and Husna Irfan Thalib. Genetic implications and management of epidermolysis bullosa in the saudi arabian population. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66678, doi:10.7759/cureus.66678. This article has 4 citations.

9. (shehata2024geneticimplicationsand pages 7-7): Nancy A Shehata, Noor A Shaik, and Husna Irfan Thalib. Genetic implications and management of epidermolysis bullosa in the saudi arabian population. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66678, doi:10.7759/cureus.66678. This article has 4 citations.

10. (azevedo2023fibrosisasa pages 1-2): Brenda Lamônica Rodrigues de Azevedo, Gabriel Marim Roni, Rosalie Matuk Fuentes Torrelio, and Letícia Nogueira da Gama-de-Souza. Fibrosis as a risk factor for cutaneous squamous cell carcinoma in recessive dystrophic epidermolysis bullosa: a systematic review. Journal of Pediatric Genetics, 12:097-104, Feb 2023. URL: https://doi.org/10.1055/s-0043-1763257, doi:10.1055/s-0043-1763257. This article has 5 citations and is from a peer-reviewed journal.

11. (tartaglia2021impairedwoundhealing pages 1-2): Grace Tartaglia, Qingqing Cao, Zachary M. Padron, and Andrew P. South. Impaired wound healing, fibrosis, and cancer: the paradigm of recessive dystrophic epidermolysis bullosa. International Journal of Molecular Sciences, 22:5104, May 2021. URL: https://doi.org/10.3390/ijms22105104, doi:10.3390/ijms22105104. This article has 53 citations.

12. (danescu2024treatmentofepidermolysis pages 1-4): Sorina Danescu, Mircea Negrutiu, and Cristina Has. Treatment of epidermolysis bullosa and future directions: a review. Dermatology and Therapy, 14:2059-2075, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01227-8, doi:10.1007/s13555-024-01227-8. This article has 14 citations.

13. (stone2024creationandcharacterization pages 1-2): William Stone, Chloe Strege, William Miller, Aron M. Geurts, Michael Grzybowski, Megan Riddle, Christopher Lees, Cindy Eide, Douglas R. Keene, Sara F. Tufa, Davis Seelig, John McGrath, and Jakub Tolar. Creation and characterization of novel rat model for recessive dystrophic epidermolysis bullosa: frameshift mutation of the col7a1 gene leads to severe blistered phenotype. PLOS ONE, 19:e0302991, May 2024. URL: https://doi.org/10.1371/journal.pone.0302991, doi:10.1371/journal.pone.0302991. This article has 2 citations and is from a peer-reviewed journal.

14. (azevedo2023fibrosisasa pages 4-5): Brenda Lamônica Rodrigues de Azevedo, Gabriel Marim Roni, Rosalie Matuk Fuentes Torrelio, and Letícia Nogueira da Gama-de-Souza. Fibrosis as a risk factor for cutaneous squamous cell carcinoma in recessive dystrophic epidermolysis bullosa: a systematic review. Journal of Pediatric Genetics, 12:097-104, Feb 2023. URL: https://doi.org/10.1055/s-0043-1763257, doi:10.1055/s-0043-1763257. This article has 5 citations and is from a peer-reviewed journal.

15. (paboncarrasco2024managementofskin pages 6-7): Manuel Pabón-Carrasco, Rocio Caceres-Matos, Marta Roche-Campos, Maria Antonia Hurtado-Guapo, Mercedes Ortiz-Romero, Luis M. Gordillo-Fernández, Daniel Pabón-Carrasco, and Aurora Castro-Méndez. Management of skin lesions in patients with epidermolysis bullosa by topical treatment: systematic review and meta-analysis. Healthcare, 12:261, Jan 2024. URL: https://doi.org/10.3390/healthcare12020261, doi:10.3390/healthcare12020261. This article has 10 citations.

16. (pironon2024splicemodulationstrategy pages 1-2): Nathalie Pironon, Emmanuelle Bourrat, Catherine Prost, Mei Chen, David T. Woodley, Matthias Titeux, and Alain Hovnanian. Splice modulation strategy applied to deep intronic variants in col7a1 causing recessive dystrophic epidermolysis bullosa. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2401781121, doi:10.1073/pnas.2401781121. This article has 7 citations and is from a highest quality peer-reviewed journal.

17. (pironon2024splicemodulationstrategy pages 4-6): Nathalie Pironon, Emmanuelle Bourrat, Catherine Prost, Mei Chen, David T. Woodley, Matthias Titeux, and Alain Hovnanian. Splice modulation strategy applied to deep intronic variants in col7a1 causing recessive dystrophic epidermolysis bullosa. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2401781121, doi:10.1073/pnas.2401781121. This article has 7 citations and is from a highest quality peer-reviewed journal.

18. (hainzl2024splicingmodulationvia pages 7-10): Stefan Hainzl, Lisa Trattner, Bernadette Liemberger, Johannes Bischof, Thomas Kocher, Michael Ablinger, Alexander Nyström, Astrid Obermayer, Alfred Klausegger, Christina Guttmann-Gruber, Verena Wally, Johann W. Bauer, Josefina Piñón Hofbauer, and Ulrich Koller. Splicing modulation via antisense oligonucleotides in recessive dystrophic epidermolysis bullosa. International Journal of Molecular Sciences, 25:761, Jan 2024. URL: https://doi.org/10.3390/ijms25020761, doi:10.3390/ijms25020761. This article has 7 citations.

19. (hainzl2024splicingmodulationvia pages 1-2): Stefan Hainzl, Lisa Trattner, Bernadette Liemberger, Johannes Bischof, Thomas Kocher, Michael Ablinger, Alexander Nyström, Astrid Obermayer, Alfred Klausegger, Christina Guttmann-Gruber, Verena Wally, Johann W. Bauer, Josefina Piñón Hofbauer, and Ulrich Koller. Splicing modulation via antisense oligonucleotides in recessive dystrophic epidermolysis bullosa. International Journal of Molecular Sciences, 25:761, Jan 2024. URL: https://doi.org/10.3390/ijms25020761, doi:10.3390/ijms25020761. This article has 7 citations.

20. (hou2023innovationsinthe pages 6-8): Ping-Chen Hou, Nathalie del Agua, Su M Lwin, Chao-Kai Hsu, and John A McGrath. Innovations in the treatment of dystrophic epidermolysis bullosa (deb): current landscape and prospects. Therapeutics and Clinical Risk Management, 19:455-473, Jun 2023. URL: https://doi.org/10.2147/tcrm.s386923, doi:10.2147/tcrm.s386923. This article has 58 citations and is from a peer-reviewed journal.

21. (condorelli2019epidermolysisbullosaassociatedsquamous pages 8-10): Angelo Giuseppe Condorelli, Elena Dellambra, Elena Logli, Giovanna Zambruno, and Daniele Castiglia. Epidermolysis bullosa-associated squamous cell carcinoma: from pathogenesis to therapeutic perspectives. International Journal of Molecular Sciences, 20:5707, Nov 2019. URL: https://doi.org/10.3390/ijms20225707, doi:10.3390/ijms20225707. This article has 147 citations.

22. (condorelli2019epidermolysisbullosaassociatedsquamous pages 6-8): Angelo Giuseppe Condorelli, Elena Dellambra, Elena Logli, Giovanna Zambruno, and Daniele Castiglia. Epidermolysis bullosa-associated squamous cell carcinoma: from pathogenesis to therapeutic perspectives. International Journal of Molecular Sciences, 20:5707, Nov 2019. URL: https://doi.org/10.3390/ijms20225707, doi:10.3390/ijms20225707. This article has 147 citations.

23. (robertson2021cutaneoussquamouscell pages 1-2): S. Robertson, E. Orrin, M. Lakhan, G. O’Sullivan, J. Felton, A. Robson, D. Greenblatt, C. Bernardis, J. McGrath, Anna E. Martinez, and J. Mellerio. Cutaneous squamous cell carcinoma in epidermolysis bullosa: a 28-year retrospective study. Acta Dermato-Venereologica, 101:adv00523, Jul 2021. URL: https://doi.org/10.2340/00015555-3875, doi:10.2340/00015555-3875. This article has 55 citations and is from a domain leading peer-reviewed journal.

24. (tartaglia2021impairedwoundhealing pages 2-4): Grace Tartaglia, Qingqing Cao, Zachary M. Padron, and Andrew P. South. Impaired wound healing, fibrosis, and cancer: the paradigm of recessive dystrophic epidermolysis bullosa. International Journal of Molecular Sciences, 22:5104, May 2021. URL: https://doi.org/10.3390/ijms22105104, doi:10.3390/ijms22105104. This article has 53 citations.

25. (kim2018epidemiologyandoutcome pages 5-6): Minhee Kim, Minmin Li, Lizbeth R. A. INTONG-WHEELER, K. Tran, D. Marucci, and D. Murrell. Epidemiology and outcome of squamous cell carcinoma in epidermolysis bullosa in australia and new zealand. Acta dermato-venereologica, 98 1:70-76, Jan 2018. URL: https://doi.org/10.2340/00015555-2781, doi:10.2340/00015555-2781. This article has 64 citations and is from a domain leading peer-reviewed journal.

26. (bonamonte2022squamouscellcarcinoma pages 6-8): Domenico Bonamonte, Angela Filoni, Aurora De Marco, Lucia Lospalluti, Eleonora Nacchiero, Valentina Ronghi, Anna Colagrande, Giuseppe Giudice, and Gerardo Cazzato. Squamous cell carcinoma in patients with inherited epidermolysis bullosa: review of current literature. Cells, 11:1365, Apr 2022. URL: https://doi.org/10.3390/cells11081365, doi:10.3390/cells11081365. This article has 49 citations.

27. (nikolova2024autosomalrecessivetype pages 2-4): Slavena Nikolova, Zornitsa Kamburova, Preslav Vasilev, Katya Kovacheva, and Ivelina Yordanova. Autosomal recessive type of dystrophic epidermolysis bullosa with a novel variant in the col7a1 gene. Biomedical Reports, Sep 2024. URL: https://doi.org/10.3892/br.2024.1855, doi:10.3892/br.2024.1855. This article has 1 citations and is from a peer-reviewed journal.

28. (montaudie2016inheritedepidermolysisbullosa pages 1-2): H. Montaudié, C. Chiaverini, Emilie Sbidian, A. Charlesworth, and Jean-Philippe Lacour. Inherited epidermolysis bullosa and squamous cell carcinoma: a systematic review of 117 cases. Orphanet Journal of Rare Diseases, Aug 2016. URL: https://doi.org/10.1186/s13023-016-0489-9, doi:10.1186/s13023-016-0489-9. This article has 135 citations and is from a peer-reviewed journal.

29. (nikolova2024autosomalrecessivetype pages 1-2): Slavena Nikolova, Zornitsa Kamburova, Preslav Vasilev, Katya Kovacheva, and Ivelina Yordanova. Autosomal recessive type of dystrophic epidermolysis bullosa with a novel variant in the col7a1 gene. Biomedical Reports, Sep 2024. URL: https://doi.org/10.3892/br.2024.1855, doi:10.3892/br.2024.1855. This article has 1 citations and is from a peer-reviewed journal.

30. (suru2024descriptivestudyof pages 2-4): Alina Suru, Alexandru Cătălin Pâslaru, George Sorin Țiplica, and Carmen Maria Sălăvăstru. Descriptive study of the clinical and molecular features of epidermolysis bullosa patients in a romanian european reference network-skin affiliated reference center. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.61160, doi:10.7759/cureus.61160. This article has 1 citations.

31. (ali2024epidermolysisbullosatwo pages 12-13): Fatma Mabrouk Ali, Jieyu Zhou, Mingyan Wang, Qiuxia Wang, Lulu Sun, Mansour Maulid Mshenga, and Hongyan Lu. Epidermolysis bullosa: two rare case reports of col7a1 and ebs-gen sev krt14 variants with review of literature. BMC Pediatrics, Apr 2024. URL: https://doi.org/10.1186/s12887-024-04715-0, doi:10.1186/s12887-024-04715-0. This article has 3 citations and is from a peer-reviewed journal.

32. (hwang2024therapiesforcutaneous pages 1-3): Austin Hwang, Andie Kwon, Corinne H. Miller, Antonia Reimer-Taschenbrecker, and Amy S. Paller. Therapies for cutaneous squamous cell carcinoma in recessive dystrophic epidermolysis bullosa: a systematic review of 157 cases. Orphanet Journal of Rare Diseases, May 2024. URL: https://doi.org/10.1186/s13023-024-03190-1, doi:10.1186/s13023-024-03190-1. This article has 13 citations and is from a peer-reviewed journal.

33. (gurevich2022invivotopical pages 1-2): Irina Gurevich, Pooja Agarwal, PeiPei Zhang, John A. Dolorito, Stacie Oliver, Henry Liu, Nicholas Reitze, Nikhil Sarma, Isin Sinem Bagci, Kunju Sridhar, Visesha Kakarla, Vamsi K. Yenamandra, Mark O’Malley, Marco Prisco, Sara F. Tufa, Douglas R. Keene, Andrew P. South, Suma M. Krishnan, and M. Peter Marinkovich. In vivo topical gene therapy for recessive dystrophic epidermolysis bullosa: a phase 1 and 2 trial. Nature Medicine, 28:780-788, Mar 2022. URL: https://doi.org/10.1038/s41591-022-01737-y, doi:10.1038/s41591-022-01737-y. This article has 181 citations and is from a highest quality peer-reviewed journal.

34. (koutsoukos2024highlightsofgene pages 5-7): Stefanos A. Koutsoukos and Ganna Bilousova. Highlights of gene and cell therapy for epidermolysis bullosa and ichthyosis. Dermatology and Therapy, 14:2379-2392, Aug 2024. URL: https://doi.org/10.1007/s13555-024-01239-4, doi:10.1007/s13555-024-01239-4. This article has 5 citations.

35. (gurevich2022invivotopical media 3ae5ad4d): Irina Gurevich, Pooja Agarwal, PeiPei Zhang, John A. Dolorito, Stacie Oliver, Henry Liu, Nicholas Reitze, Nikhil Sarma, Isin Sinem Bagci, Kunju Sridhar, Visesha Kakarla, Vamsi K. Yenamandra, Mark O’Malley, Marco Prisco, Sara F. Tufa, Douglas R. Keene, Andrew P. South, Suma M. Krishnan, and M. Peter Marinkovich. In vivo topical gene therapy for recessive dystrophic epidermolysis bullosa: a phase 1 and 2 trial. Nature Medicine, 28:780-788, Mar 2022. URL: https://doi.org/10.1038/s41591-022-01737-y, doi:10.1038/s41591-022-01737-y. This article has 181 citations and is from a highest quality peer-reviewed journal.

36. (gurevich2022invivotopical media 80fb8fb9): Irina Gurevich, Pooja Agarwal, PeiPei Zhang, John A. Dolorito, Stacie Oliver, Henry Liu, Nicholas Reitze, Nikhil Sarma, Isin Sinem Bagci, Kunju Sridhar, Visesha Kakarla, Vamsi K. Yenamandra, Mark O’Malley, Marco Prisco, Sara F. Tufa, Douglas R. Keene, Andrew P. South, Suma M. Krishnan, and M. Peter Marinkovich. In vivo topical gene therapy for recessive dystrophic epidermolysis bullosa: a phase 1 and 2 trial. Nature Medicine, 28:780-788, Mar 2022. URL: https://doi.org/10.1038/s41591-022-01737-y, doi:10.1038/s41591-022-01737-y. This article has 181 citations and is from a highest quality peer-reviewed journal.

37. (NCT03536143 chunk 1):  A Phase I/II Study of KB103, a Topical HSV1-COL7, on DEB Patients. Krystal Biotech, Inc.. 2018. ClinicalTrials.gov Identifier: NCT03536143

38. (pironon2024splicemodulationstrategy pages 6-7): Nathalie Pironon, Emmanuelle Bourrat, Catherine Prost, Mei Chen, David T. Woodley, Matthias Titeux, and Alain Hovnanian. Splice modulation strategy applied to deep intronic variants in col7a1 causing recessive dystrophic epidermolysis bullosa. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2401781121, doi:10.1073/pnas.2401781121. This article has 7 citations and is from a highest quality peer-reviewed journal.

39. (takaki2022generationofa pages 1-2): Satoshi Takaki, Takashi Shimbo, Kentaro Ikegami, Tomomi Kitayama, Yukari Yamamoto, Sho Yamazaki, Shiho Mori, and Katsuto Tamai. Generation of a recessive dystrophic epidermolysis bullosa mouse model with patient-derived compound heterozygous mutations. Laboratory Investigation, 102:574-580, Jun 2022. URL: https://doi.org/10.1038/s41374-022-00735-5, doi:10.1038/s41374-022-00735-5. This article has 10 citations and is from a peer-reviewed journal.

40. (stone2024creationandcharacterization pages 7-9): William Stone, Chloe Strege, William Miller, Aron M. Geurts, Michael Grzybowski, Megan Riddle, Christopher Lees, Cindy Eide, Douglas R. Keene, Sara F. Tufa, Davis Seelig, John McGrath, and Jakub Tolar. Creation and characterization of novel rat model for recessive dystrophic epidermolysis bullosa: frameshift mutation of the col7a1 gene leads to severe blistered phenotype. PLOS ONE, 19:e0302991, May 2024. URL: https://doi.org/10.1371/journal.pone.0302991, doi:10.1371/journal.pone.0302991. This article has 2 citations and is from a peer-reviewed journal.

41. (stone2024creationandcharacterization pages 9-10): William Stone, Chloe Strege, William Miller, Aron M. Geurts, Michael Grzybowski, Megan Riddle, Christopher Lees, Cindy Eide, Douglas R. Keene, Sara F. Tufa, Davis Seelig, John McGrath, and Jakub Tolar. Creation and characterization of novel rat model for recessive dystrophic epidermolysis bullosa: frameshift mutation of the col7a1 gene leads to severe blistered phenotype. PLOS ONE, 19:e0302991, May 2024. URL: https://doi.org/10.1371/journal.pone.0302991, doi:10.1371/journal.pone.0302991. This article has 2 citations and is from a peer-reviewed journal.

42. (shehata2024geneticimplicationsand pages 1-4): Nancy A Shehata, Noor A Shaik, and Husna Irfan Thalib. Genetic implications and management of epidermolysis bullosa in the saudi arabian population. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.66678, doi:10.7759/cureus.66678. This article has 4 citations.

43. (bonamonte2022squamouscellcarcinoma pages 1-2): Domenico Bonamonte, Angela Filoni, Aurora De Marco, Lucia Lospalluti, Eleonora Nacchiero, Valentina Ronghi, Anna Colagrande, Giuseppe Giudice, and Gerardo Cazzato. Squamous cell carcinoma in patients with inherited epidermolysis bullosa: review of current literature. Cells, 11:1365, Apr 2022. URL: https://doi.org/10.3390/cells11081365, doi:10.3390/cells11081365. This article has 49 citations.

44. (harrs2022theaggressivebehaviour pages 1-1): Clara Harrs, Peter C. van den Akker, Rosalie Baardman, José C. Duipmans, Barbara Horváth, Marloes S. van Kester, Henny H. Lemmink, Emoke Rácz, Marieke C. Bolling, and Gilles F.H. Diercks. The aggressive behaviour of squamous cell carcinoma in epidermolysis bullosa: analysis of clinical outcomes and tumour characteristics in the dutch eb registry. British Journal of Dermatology, 187:824-826, Nov 2022. URL: https://doi.org/10.1111/bjd.21769, doi:10.1111/bjd.21769. This article has 13 citations and is from a highest quality peer-reviewed journal.

45. (gurevich2022invivotopical media 2ab3990c): Irina Gurevich, Pooja Agarwal, PeiPei Zhang, John A. Dolorito, Stacie Oliver, Henry Liu, Nicholas Reitze, Nikhil Sarma, Isin Sinem Bagci, Kunju Sridhar, Visesha Kakarla, Vamsi K. Yenamandra, Mark O’Malley, Marco Prisco, Sara F. Tufa, Douglas R. Keene, Andrew P. South, Suma M. Krishnan, and M. Peter Marinkovich. In vivo topical gene therapy for recessive dystrophic epidermolysis bullosa: a phase 1 and 2 trial. Nature Medicine, 28:780-788, Mar 2022. URL: https://doi.org/10.1038/s41591-022-01737-y, doi:10.1038/s41591-022-01737-y. This article has 181 citations and is from a highest quality peer-reviewed journal.
