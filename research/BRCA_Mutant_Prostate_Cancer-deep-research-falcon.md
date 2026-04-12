---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T13:31:30.285282'
end_time: '2026-04-05T13:46:28.132059'
duration_seconds: 897.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRCA-Mutant Prostate Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRCA-Mutant Prostate Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRCA-Mutant Prostate Cancer** covering all of the
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
- **Disease Name:** BRCA-Mutant Prostate Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRCA-Mutant Prostate Cancer** covering all of the
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


# BRCA‑Mutant Prostate Cancer — Disease Characteristics Research Report (2023–2024 emphasis)

## Target disease
- **Disease name:** BRCA‑mutant prostate cancer (BRCA1/BRCA2-altered prostate cancer; typically discussed within advanced/metastatic prostate cancer and mCRPC)
- **Category:** Molecularly defined subtype of prostate cancer characterized by homologous recombination repair deficiency (HRD)
- **Ontology identifiers (available in retrieved sources):**
  - **MONDO:** Prostate cancer **MONDO:0008315** (used as parent disease entity; a distinct MONDO subtype term for “BRCA‑mutant prostate cancer” was not evidenced in the retrieved context) (heiss2024usfoodand pages 2-4)
  - **EFO:** Prostate carcinoma **EFO_0001663** (as a parent disease entity used in target–disease resources) (heiss2024usfoodand pages 2-4)

## 1. Disease information

### 1.1 Overview (current understanding)
BRCA‑mutant prostate cancer refers to prostate cancer with pathogenic alterations in **BRCA1 and/or BRCA2**, which encode key homologous recombination repair proteins. These alterations are clinically important because they (i) are associated with an aggressive phenotype and poorer prognosis in metastatic settings and (ii) predict benefit from **PARP inhibitor** therapy, including PARP inhibitor combinations with androgen receptor pathway inhibitors in selected biomarker-defined populations (mateo2024olaparibforthe pages 1-2, fettke2023brcadeficientmetastaticprostate pages 1-2).

### 1.2 Synonyms / alternative names
Commonly used terms in the literature include:
- BRCA1/2‑altered prostate cancer
- BRCA‑altered metastatic castration‑resistant prostate cancer (BRCA‑altered mCRPC)
- HRR‑mutated or HRR‑deficient prostate cancer (often includes BRCA but is broader) (fizazi2024firstlinetalazoparibwith pages 1-2, chi2023niraparibandabiraterone pages 1-2).

### 1.3 Source type (patient-level vs aggregated)
The information in this report is derived from:
- **Aggregated evidence:** systematic review/meta-analysis of BRCA mutation frequencies across stages (Valsecchi 2023) (valsecchi2023frequencyofgermline pages 1-2)
- **Randomized clinical trials / subgroup analyses:** PROfound (olaparib) subgroup analysis; MAGNITUDE (niraparib + abiraterone) (mateo2024olaparibforthe pages 1-2, chi2023niraparibandabiraterone pages 1-2)
- **Real‑world cohorts:** cfDNA/ctDNA studies in advanced disease (e.g., Fettke 2023; PROfound screening concordance studies) (fettke2023brcadeficientmetastaticprostate pages 1-2, chi2023detectionofbrca1 pages 1-2).

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor (genetic):**
- Pathogenic alterations (germline or somatic) in **BRCA2** (more common) and **BRCA1** lead to homologous recombination repair deficiency (HRD), genomic instability, and therapeutic vulnerabilities (synthetic lethality with PARP inhibition) (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2).

### 2.2 Risk factors
#### Genetic risk factors
- **Male BRCA2 pathogenic variant (PV) carriers** have substantially increased lifetime prostate cancer risk; estimates vary by cohort/meta-analytic approach. Cheng et al. summarize that lifetime risk estimates range from ~27% (95% CI 21–35%) to ~60% (95% CI 43–78%), with relative risk estimates around 4.7–8.6-fold depending on study (cheng2024brca1brca2and pages 5-6, cheng2024brca1brca2and pages 16-19).
- **BRCA1 PV** also increases risk, but estimates are lower than BRCA2; Cheng et al. summarize “up to 3.8-fold” with lifetime risk 15–45% (cheng2024brca1brca2and pages 5-6).

#### Non-genetic risk factors
The retrieved evidence base emphasized genetic risk and did not provide high-quality quantified environmental/lifestyle risk modifiers specific to BRCA‑mutant prostate cancer.

### 2.3 Protective factors
No disease-specific protective genetic variants or protective environmental factors for BRCA‑mutant prostate cancer were identified in the retrieved evidence.

### 2.4 Epidemiology of BRCA alterations in prostate cancer (2023 pooled estimates)
A 2023 systematic review/meta-analysis (literature search through Nov 2022) provides pooled frequencies by disease setting (random-effects estimates):
- **Any-stage PC:**
  - BRCA1 germline 0.73%; BRCA1 somatic 1.20%
  - BRCA2 germline 3.25%; BRCA2 somatic 6.29%
  - Combined BRCA1/2 germline 4.47%; somatic 7.18% (valsecchi2023frequencyofgermline pages 1-2, valsecchi2023frequencyofgermline pages 2-5)
- **Metastatic PC:**
  - BRCA1 germline 0.94%; somatic 1.10%
  - BRCA2 germline 4.51%; somatic 10.26%
  - Combined BRCA1/2 germline 5.84%; somatic 10.94% (valsecchi2023frequencyofgermline pages 1-2)
- **mCRPC:**
  - BRCA1 germline 1.21%; somatic 1.10%
  - BRCA2 germline 3.90%; somatic 10.52%
  - Combined BRCA1/2 germline 5.26%; somatic 11.26% (valsecchi2023frequencyofgermline pages 1-2, valsecchi2023frequencyofgermline pages 25-27)

**Interpretation:** Somatic BRCA alterations are more common than germline across settings, and BRCA2 predominates, with higher frequencies in metastatic disease (valsecchi2023frequencyofgermline pages 1-2).

A compact synthesis of these stage-specific frequencies is provided in:

| Setting | Germline BRCA1 % | Somatic BRCA1 % | Germline BRCA2 % | Somatic BRCA2 % | Notes | Source |
|---|---:|---:|---:|---:|---|---|
| Any-stage prostate cancer | 0.73% | 1.20% | 3.25% | 6.29% | Meta-analysis: somatic mutations more common than germline; BRCA2 more common than BRCA1. Combined BRCA1/2 frequency: 4.47% germline, 7.18% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic prostate cancer | 0.94% | 1.10% | 4.51% | 10.26% | Frequency rises in metastatic disease; BRCA2 predominates; combined BRCA1/2 frequency: 5.84% germline, 10.94% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic castration-resistant prostate cancer (mCRPC) | 1.21% | 1.10% | 3.90% | 10.52% | In mCRPC, somatic BRCA2 is especially enriched; combined BRCA1/2 frequency: 5.26% germline, 11.26% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic prostate cancer, germline DDR pathogenic variants | — | — | ~6% (BRCA1/2 combined) | — | Review states ~12% of metastatic prostate cancer patients harbor germline DDR pathogenic variants, with BRCA1/2 the most frequent DDR genes (~6% combined). Also notes germline and somatic BRCA1/2 frequencies are reported as similar enough that both should be evaluated. (inoue2023rolesofthe pages 2-4) | Inoue et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092662 |
| BRCA2-altered mCRPC PARPi-treated cohort (clinical provenance split) | — | — | 50% of BRCA2-altered cases were germline overall; 58% among responders | 50% of BRCA2-altered cases were somatic overall; 39% among responders | Clinical cohort provenance rather than population prevalence: in BRCA2-altered mCRPC treated with PARP inhibitors, mutation origin was roughly evenly split overall (56/110 germline, 54/110 somatic), with germline enrichment among responders. (taza2021differentialactivityof pages 20-21) | Taza et al., 2021, *JCO Precision Oncology*; https://doi.org/10.1200/PO.21.00070 |
| Real-world ctDNA metastatic prostate cancer cohort | not separately reported | not separately reported | not separately reported | not separately reported | ctDNA cohort found BRCA1/2 alterations (germline or somatic) in 21% of patients with metastatic prostate cancer; this row reflects assay-detected prevalence in a progression-enriched real-world blood cohort, not stage-specific tissue prevalence. (valsecchi2023frequencyofgermline pages 8-10) | Bang et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15153998 |


*Table: This table summarizes reported BRCA1/2 mutation frequencies and mutation provenance in prostate cancer across disease settings. It combines meta-analytic prevalence estimates with review and cohort data to distinguish population frequency from clinical provenance in advanced disease.*

## 3. Phenotypes

### 3.1 Core clinical phenotype (advanced disease)
Across advanced prostate cancer cohorts, BRCA alterations—particularly BRCA2—are associated with aggressive disease features and poorer outcomes.
- In a multicenter retrospective cohort of BRCA-altered mCRPC treated with PARP inhibitors, **72%** had **Gleason 8–10** at diagnosis, and BRCA1 cases more often presented with metastatic disease (69% vs 37%) (taza2021differentialactivityof pages 1-2).
- In a real-world cfDNA cohort (375 men with mCRPC), BRCA alterations were associated with **lower PSA response rates to AR pathway inhibitors** (32% vs 60%) (fettke2023brcadeficientmetastaticprostate pages 1-2).

### 3.2 Differential phenotype: BRCA1 vs BRCA2 in PARP inhibitor–treated mCRPC
In a retrospective multicenter analysis of PARP inhibitor–treated BRCA-altered mCRPC (n=123):
- PSA50 responses were **23%** in BRCA1‑altered vs **63%** in BRCA2‑altered disease (P=.01) (taza2021differentialactivityof pages 1-2).
- BRCA1 cases more often had metastatic presentation and more monoallelic alterations and TP53 co-alterations, potentially contributing to reduced PARP inhibitor sensitivity (taza2021differentialactivityof pages 1-2).

### 3.3 Quality of life impact
The retrieved primary evidence set emphasizes survival and progression endpoints; systematic, quantitative health-related QoL outcomes specific to BRCA-mutant subsets were not captured in the available excerpts.

### 3.4 Suggested HPO phenotype mappings (examples)
A structured mapping (including treatment-related phenotypes such as anemia/fatigue) is proposed in:

| Section | Suggested term(s) | Evidence/rationale |
|---|---|---|
| Disease concept | prostate cancer — MONDO:0008315; BRCA-mutant prostate cancer — MONDO: not clearly established in available context; prostate carcinoma — EFO:0001663 | Open Targets evidence links BRCA1/2 to prostate cancer/prostate carcinoma; BRCA-mutant prostate cancer is best modeled as a molecularly defined subtype of prostate cancer rather than a clearly separate MONDO disease in the provided context (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Key genes | BRCA2 (HGNC:1101); BRCA1 (HGNC:1100); ATM (HGNC:795) | BRCA2 is the dominant altered gene in prostate cancer and is more common than BRCA1; ATM is a major comparator/HRR gene in trials and testing panels (inoue2023rolesofthe pages 2-4, alakhras2024parpinhibitorsin pages 10-11, heiss2024usfoodand pages 2-4) |
| Key genes | TP53 (HGNC:11998); AR (HGNC:644); CDK12 (HGNC:24243) | BRCA1-altered disease shows more concurrent TP53 alterations and worse PARPi outcomes; AR biology underlies PARP/AR combination rationale; CDK12 is a frequent HRR-panel gene in advanced disease studies (taza2021differentialactivityof pages 1-2, alakhras2024parpinhibitorsin pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Phenotypes (HPO) | Aggressive prostate carcinoma phenotype — HPO likely prefix HP:; High Gleason score — HPO likely prefix HP:; Early adult onset/neoplasm onset younger than typical — HPO likely prefix HP:0003581/HP: | BRCA2 carriers show more clinically significant disease, younger onset, and high-grade tumors; BRCA-deficient metastatic disease has adverse prognosis (inoue2023rolesofthe pages 2-4, taza2021differentialactivityof pages 1-2) |
| Phenotypes (HPO) | Metastatic prostate adenocarcinoma — HPO likely prefix HP:0004409/HP:; Bone metastasis — HPO likely prefix HP:0002664; Castration-resistant disease — HPO likely prefix HP: | BRCA1 patients more often present metastatic at diagnosis; BRCA2 cohorts show frequent M1 disease and bone metastases; advanced trials focus on mCRPC (taza2021differentialactivityof pages 1-2, taza2021differentialactivityof pages 20-21, mateo2024olaparibforthe pages 1-2) |
| Phenotypes (HPO) | Anemia — HP:0001903; Fatigue — HP:0012378; Neutropenia — HP:0001875 | Common toxicities of PARP inhibitors/combination therapy include anemia, fatigue, and neutropenia; anemia is the most frequent grade ≥3 hematologic adverse event (tisseverasinghe2023advancesinparp pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Anatomical entities (UBERON) | prostate gland — UBERON:0002367; prostate epithelium — UBERON likely prefix UBERON:; prostate stromal tissue — UBERON likely prefix UBERON: | Primary organ and tissue compartments involved in prostate carcinoma biology (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Anatomical entities (UBERON) | bone of skeletal system — UBERON:0001474; lymph node — UBERON:0000029; blood/plasma — UBERON:0000178 / body fluid term likely needed | Bone metastases are common; lymph nodes are common metastatic sites; plasma is important for ctDNA diagnostics (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Biological processes (GO) | homologous recombination — GO:0000724; DNA repair — GO:0006281; double-strand break repair — GO:0006302 | Core BRCA biology in prostate cancer is homologous recombination repair deficiency and impaired DSB repair (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | response to DNA damage stimulus — GO:0006974; DNA replication fork processing — GO likely prefix GO:; cell cycle process — GO:0022402 | PARP inhibition exploits replication-fork collapse and DNA damage accumulation; BRCA2-mutant tumors are enriched for cell-cycle programs (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | androgen receptor signaling pathway — GO likely prefix GO:; regulation of transcription by RNA polymerase II — GO:0006357; synthetic lethal interaction context — no direct GO term, represent via DNA repair dependency | TALAPRO-2 and FDA summary emphasize AR–PARP interplay: AR inhibition downregulates HRR genes and PARP inhibition suppresses AR transcriptional activity (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Cell types (CL) | prostate gland epithelial cell — CL likely prefix CL:; luminal epithelial cell of prostate — CL likely prefix CL:; basal cell of prostate epithelium — CL likely prefix CL: | Prostate cancer arises from epithelial compartments; organoid/PDX models preserve epithelial tumor features (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) |
| Cell types (CL) | metastatic prostate cancer cell — CL likely prefix CL: cancer cell term; osteoblast — CL:0000062; osteoclast — CL:0000097 | Bone metastasis is a hallmark clinical site and relevant microenvironmental context (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Treatments (MAXO) | PARP inhibitor therapy — MAXO likely prefix MAXO:; olaparib treatment — MAXO likely prefix MAXO:; talazoparib treatment — MAXO likely prefix MAXO: | Olaparib improves rPFS/OS/ORR in BRCA-altered mCRPC; talazoparib + enzalutamide improves rPFS in HRR-mutated disease, especially BRCA-mutant subgroup (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, heiss2024usfoodand pages 2-4) |
| Treatments (MAXO) | niraparib plus abiraterone therapy — MAXO likely prefix MAXO:; enzalutamide therapy — MAXO likely prefix MAXO:; androgen receptor pathway inhibitor therapy — MAXO likely prefix MAXO: | MAGNITUDE supports niraparib + abiraterone in BRCA1/2-mutated mCRPC; ARPI backbone is central to current implementation (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) |
| Treatments (MAXO) | circulating tumor DNA testing-guided targeted therapy — MAXO likely prefix MAXO:; germline genetic testing — MAXO likely prefix MAXO:; supportive treatment for anemia — MAXO likely prefix MAXO: | Tissue and ctDNA testing are used to identify eligible patients; anemia management is a key supportive action during PARPi therapy (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 2-4, tisseverasinghe2023advancesinparp pages 10-11) |


*Table: This table proposes practical ontology mappings for a BRCA-mutant prostate cancer knowledge-base entry, spanning disease concept, genes, phenotypes, anatomy, processes, cell types, and treatments. It is grounded in the provided evidence on aggressive disease biology, metastatic behavior, PARP inhibitor response, and treatment toxicity.*

## 4. Genetic / molecular information

### 4.1 Causal genes
- **BRCA2** (dominant in prostate cancer)
- **BRCA1** (less frequent)
These genes function in homologous recombination repair; their inactivation results in HRD (valsecchi2023frequencyofgermline pages 1-2, fizazi2024firstlinetalazoparibwith pages 1-2).

### 4.2 Variant origin (germline vs somatic)
- Germline and somatic BRCA alterations both predict benefit from PARP inhibition in mCRPC; in PROfound BRCA subgroup, progression-risk reduction was similar for germline and somatic BRCA alterations (mateo2024olaparibforthe pages 1-2).

### 4.3 Co-alterations / molecular phenotype
BRCA-deficient metastatic prostate cancer shows enrichment of additional potentially actionable alterations:
- In a 2023 cfDNA cohort, BRCA-deficient tumors were enriched for **AR** and **PI3K pathway** alterations (fettke2023brcadeficientmetastaticprostate pages 1-2).
- Additional genomic enrichments reported include PI3K pathway alterations (PIK3CA/PTEN), FGFR1 copy gain, CDK6 alterations, and enrichment for aggressive disease-associated drivers (e.g., TP53/RB1/MYC) (fettke2023brcadeficientmetastaticprostate pages 7-8).

### 4.4 Epigenetic information
BRCA promoter methylation and broader epigenetic HRD (“BRCAness”) are conceptually relevant but were not supported by prostate-cancer-specific quantitative data in the retrieved excerpts.

## 5. Environmental information
No BRCA‑subtype–specific environmental exposures were identified in the retrieved evidence. Established prostate cancer environmental/lifestyle associations are outside the scope of the current evidence set.

## 6. Mechanism / pathophysiology

### 6.1 DNA repair defect → HRD → therapeutic vulnerability
- PARP enzymes (notably PARP‑1/2) participate in single‑strand break (SSB) repair; PARP inhibitors block PARP catalytic activity and trap PARP on DNA. In BRCA1/2‑deficient cells, unrepaired SSBs convert to double‑strand breaks during replication, replication forks collapse, and the cell cannot repair the damage (synthetic lethality) (inoue2023rolesofthe pages 2-4).

### 6.2 AR–PARP interplay (rationale for combinations)
TALAPRO‑2 explicitly describes preclinical rationale for co-inhibition:
- “Androgen receptor inhibition is associated with upregulated PARP activity and downregulated HRR gene expression… while PARP inhibition suppresses androgen receptor transcriptional activity” (fizazi2024firstlinetalazoparibwith pages 1-2).

### 6.3 Suggested GO/CL terms
Candidate GO biological processes and CL cell types are included in:

| Section | Suggested term(s) | Evidence/rationale |
|---|---|---|
| Disease concept | prostate cancer — MONDO:0008315; BRCA-mutant prostate cancer — MONDO: not clearly established in available context; prostate carcinoma — EFO:0001663 | Open Targets evidence links BRCA1/2 to prostate cancer/prostate carcinoma; BRCA-mutant prostate cancer is best modeled as a molecularly defined subtype of prostate cancer rather than a clearly separate MONDO disease in the provided context (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Key genes | BRCA2 (HGNC:1101); BRCA1 (HGNC:1100); ATM (HGNC:795) | BRCA2 is the dominant altered gene in prostate cancer and is more common than BRCA1; ATM is a major comparator/HRR gene in trials and testing panels (inoue2023rolesofthe pages 2-4, alakhras2024parpinhibitorsin pages 10-11, heiss2024usfoodand pages 2-4) |
| Key genes | TP53 (HGNC:11998); AR (HGNC:644); CDK12 (HGNC:24243) | BRCA1-altered disease shows more concurrent TP53 alterations and worse PARPi outcomes; AR biology underlies PARP/AR combination rationale; CDK12 is a frequent HRR-panel gene in advanced disease studies (taza2021differentialactivityof pages 1-2, alakhras2024parpinhibitorsin pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Phenotypes (HPO) | Aggressive prostate carcinoma phenotype — HPO likely prefix HP:; High Gleason score — HPO likely prefix HP:; Early adult onset/neoplasm onset younger than typical — HPO likely prefix HP:0003581/HP: | BRCA2 carriers show more clinically significant disease, younger onset, and high-grade tumors; BRCA-deficient metastatic disease has adverse prognosis (inoue2023rolesofthe pages 2-4, taza2021differentialactivityof pages 1-2) |
| Phenotypes (HPO) | Metastatic prostate adenocarcinoma — HPO likely prefix HP:0004409/HP:; Bone metastasis — HPO likely prefix HP:0002664; Castration-resistant disease — HPO likely prefix HP: | BRCA1 patients more often present metastatic at diagnosis; BRCA2 cohorts show frequent M1 disease and bone metastases; advanced trials focus on mCRPC (taza2021differentialactivityof pages 1-2, taza2021differentialactivityof pages 20-21, mateo2024olaparibforthe pages 1-2) |
| Phenotypes (HPO) | Anemia — HP:0001903; Fatigue — HP:0012378; Neutropenia — HP:0001875 | Common toxicities of PARP inhibitors/combination therapy include anemia, fatigue, and neutropenia; anemia is the most frequent grade ≥3 hematologic adverse event (tisseverasinghe2023advancesinparp pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Anatomical entities (UBERON) | prostate gland — UBERON:0002367; prostate epithelium — UBERON likely prefix UBERON:; prostate stromal tissue — UBERON likely prefix UBERON: | Primary organ and tissue compartments involved in prostate carcinoma biology (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Anatomical entities (UBERON) | bone of skeletal system — UBERON:0001474; lymph node — UBERON:0000029; blood/plasma — UBERON:0000178 / body fluid term likely needed | Bone metastases are common; lymph nodes are common metastatic sites; plasma is important for ctDNA diagnostics (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Biological processes (GO) | homologous recombination — GO:0000724; DNA repair — GO:0006281; double-strand break repair — GO:0006302 | Core BRCA biology in prostate cancer is homologous recombination repair deficiency and impaired DSB repair (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | response to DNA damage stimulus — GO:0006974; DNA replication fork processing — GO likely prefix GO:; cell cycle process — GO:0022402 | PARP inhibition exploits replication-fork collapse and DNA damage accumulation; BRCA2-mutant tumors are enriched for cell-cycle programs (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | androgen receptor signaling pathway — GO likely prefix GO:; regulation of transcription by RNA polymerase II — GO:0006357; synthetic lethal interaction context — no direct GO term, represent via DNA repair dependency | TALAPRO-2 and FDA summary emphasize AR–PARP interplay: AR inhibition downregulates HRR genes and PARP inhibition suppresses AR transcriptional activity (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Cell types (CL) | prostate gland epithelial cell — CL likely prefix CL:; luminal epithelial cell of prostate — CL likely prefix CL:; basal cell of prostate epithelium — CL likely prefix CL: | Prostate cancer arises from epithelial compartments; organoid/PDX models preserve epithelial tumor features (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) |
| Cell types (CL) | metastatic prostate cancer cell — CL likely prefix CL: cancer cell term; osteoblast — CL:0000062; osteoclast — CL:0000097 | Bone metastasis is a hallmark clinical site and relevant microenvironmental context (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Treatments (MAXO) | PARP inhibitor therapy — MAXO likely prefix MAXO:; olaparib treatment — MAXO likely prefix MAXO:; talazoparib treatment — MAXO likely prefix MAXO: | Olaparib improves rPFS/OS/ORR in BRCA-altered mCRPC; talazoparib + enzalutamide improves rPFS in HRR-mutated disease, especially BRCA-mutant subgroup (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, heiss2024usfoodand pages 2-4) |
| Treatments (MAXO) | niraparib plus abiraterone therapy — MAXO likely prefix MAXO:; enzalutamide therapy — MAXO likely prefix MAXO:; androgen receptor pathway inhibitor therapy — MAXO likely prefix MAXO: | MAGNITUDE supports niraparib + abiraterone in BRCA1/2-mutated mCRPC; ARPI backbone is central to current implementation (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) |
| Treatments (MAXO) | circulating tumor DNA testing-guided targeted therapy — MAXO likely prefix MAXO:; germline genetic testing — MAXO likely prefix MAXO:; supportive treatment for anemia — MAXO likely prefix MAXO: | Tissue and ctDNA testing are used to identify eligible patients; anemia management is a key supportive action during PARPi therapy (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 2-4, tisseverasinghe2023advancesinparp pages 10-11) |


*Table: This table proposes practical ontology mappings for a BRCA-mutant prostate cancer knowledge-base entry, spanning disease concept, genes, phenotypes, anatomy, processes, cell types, and treatments. It is grounded in the provided evidence on aggressive disease biology, metastatic behavior, PARP inhibitor response, and treatment toxicity.*

## 7. Anatomical structures affected

### 7.1 Primary and secondary sites
- **Primary organ:** prostate gland
- **Common metastatic sites in advanced disease:** bone and lymph nodes (common in mCRPC cohorts and trial baseline characteristics) (taza2021differentialactivityof pages 1-2, fizazi2024firstlinetalazoparibwith pages 1-2).

### 7.2 Suggested UBERON terms
See ontology mapping table (artifact-03).

## 8. Temporal development
- Typical clinical trajectory relevant to BRCA‑mutant disease is progression from localized prostate cancer to metastatic disease and eventually mCRPC, where HRR alterations are enriched (valsecchi2023frequencyofgermline pages 1-2).
- In advanced cohorts, BRCA2 alterations can be observed early, including in hormone-sensitive metastatic disease in real-world ctDNA profiling (fettke2023brcadeficientmetastaticprostate pages 8-10).

## 9. Inheritance and population

### 9.1 Inheritance pattern
- Germline BRCA1/2 pathogenic variants are inherited in an **autosomal dominant** pattern with variable penetrance (general hereditary cancer syndrome context; prostate cancer risk in male carriers is emphasized) (cheng2024brca1brca2and pages 5-6).

### 9.2 Population statistics (selected)
- Male carriers are under-tested: Cheng et al. summarize that males undergo cancer-specific genetic testing at ~one-tenth the frequency of females (RR 0.10; 95% CI 0.05–0.23) (cheng2024brca1brca2and pages 1-3).

## 10. Diagnostics

### 10.1 Genomic testing (tumor tissue and plasma)
A key implementation challenge is insufficient or failed tissue testing in advanced disease:
- In PROfound screening, **31%** of tumor tissue samples failed molecular screening (insufficient/inadequate tissue or tumor content, DNA quality/quantity, or downstream assay failures) (chi2023detectionofbrca1 pages 1-2).

**ctDNA as a complement to tissue testing:**
- PROfound matched analysis: **81% (503/619)** of ctDNA samples yielded an NGS result; comparing tissue to ctDNA showed **81% positive percentage agreement** and **92% negative percentage agreement**; concordance was high for nonsense (93%), splice (87%), frameshift (86%) but lower for large rearrangements (63%) and homozygous deletions (27%); low ctDNA fraction was limiting (chi2023detectionofbrca1 pages 1-2).

A detailed diagnostic synthesis (including structural-variant limitations) is provided in:

| Specimen/test | Yield | Agreement metrics | Strengths | Limitations | Source |
|---|---:|---|---|---|---|
| Tumor tissue NGS (FoundationOne CDx–based screening in PROfound) | Tissue molecular screening failure rate ~31% | Used as reference standard for matched analyses; when compared with ctDNA, corresponding ctDNA PPA/sensitivity 81% and NPA/specificity 92% | Current gold-standard approach for HRR testing; better detection of structural events such as homozygous deletions and large rearrangements; avoids some plasma false negatives (chi2023detectionofbrca1 pages 2-2, chi2023detectionofbrca1 pages 6-8) | Invasive biopsy; frequent insufficiency/quality failures, especially with small samples and bone-predominant disease; decalcification and low DNA quantity/quality can impair testing | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 2-4, chi2023detectionofbrca1 pages 2-2) |
| Plasma ctDNA NGS (FoundationOne Liquid CDx in matched PROfound cohort) | 81% (503/619) yielded an NGS result; ~90% yield after excluding technical batch failures; plasma volume ≥7 mL improved yield (82% vs 69%) | Overall BRCA/ATM status vs tissue: PPA 81%, NPA 92%, PPV 0.68, NPV 0.96; variant-level sensitivity 74% and overall variant concordance 71% (146/207 shared variants) | Minimally invasive; complements tissue when tissue is unavailable/insufficient; identified additional patients potentially eligible for PARP inhibitor treatment; high specificity even at lower ctDNA fractions | False negatives occur, especially with low ctDNA fraction/non-shedders; ~20% of qualifying mutations identified by tissue only; ctDNA fraction not evaluable in 13% | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 2-4, chi2023detectionofbrca1 pages 6-8) |
| Plasma ctDNA NGS performance by ctDNA fraction | 428/491 (87%) had evaluable ctDNA fraction | At ctDNA fraction ≥10%: sensitivity 87%, specificity 90%; at 1% to <10%: sensitivity 92%, specificity 95%; at <1%/not evaluable: sensitivity fell to 68%/56% while specificity remained high (92%/100%) | Best performance when tumor shedding is adequate; useful for dynamic testing in metastatic disease | Low-shedding tumors markedly reduce sensitivity; negative plasma test does not exclude actionable BRCA/ATM alteration | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 6-8) |
| Variant subtype concordance: nonsense / splice / frameshift | Not applicable | High concordance versus tissue: nonsense 93%, splice 87%, frameshift 86% | ctDNA performs well for many short variants/indels relevant to BRCA/ATM | Some splice and missense variants show lower overlap when assessed from ctDNA perspective | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 5-6) |
| Variant subtype concordance: large rearrangements / homozygous deletions | Not applicable | Large rearrangements 63% concordance from tissue reference; homozygous deletions only 27% concordance from tissue reference | Tissue testing better captures these lesion classes | Major plasma blind spot, especially at low ctDNA fraction; important because BRCA2 homozygous deletions can predict strong PARP inhibitor sensitivity | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 5-6) |
| Clinical interpretation of negative plasma test | Not applicable | Approx. 80% concordance overall with tissue in PROfound-era analyses | ctDNA is clinically useful to complement tissue and can support identification of BRCA/ATM-altered mCRPC for olaparib | FoundationOne Liquid CDx not validated for some homozygous BRCA deletions/large rearrangements; low tumor content and CHIP can confound results; FDA label cautions that a negative liquid test does not rule out actionable alterations and tissue testing should be pursued if feasible | Matsubara et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-21-3577 (matsubara2023olaparibefficacyin pages 5-6); Chi et al., 2023 (chi2023detectionofbrca1 pages 6-8) |


*Table: This table compares tumor tissue NGS and plasma ctDNA testing for BRCA/ATM alterations in mCRPC, emphasizing test yield, concordance, and important structural-variant limitations. It is useful for selecting testing strategies and interpreting negative liquid-biopsy results.*

**Visual evidence (PROfound tissue vs ctDNA concordance):** key tables/figures were retrieved from the PROfound screening paper (chi2023detectionofbrca1 media 1d7942c2, chi2023detectionofbrca1 media 19a57459, chi2023detectionofbrca1 media c50e82d1, chi2023detectionofbrca1 media 89bfe680).

### 10.2 Imaging and early detection pathways
A 2024 JAMA Oncology systematic review/meta-analysis of MRI in screening pathways (12 studies; ~80k men) found that, compared with PSA-only pathways, MRI-based screening:
- Reduced biopsies (OR **0.28**, 95% CI 0.22–0.36)
- Reduced detection of insignificant cancers (OR **0.34**, 95% CI 0.23–0.49)
- Maintained overall clinically significant cancer detection (OR **1.02**, 95% CI 0.75–1.37)
- Increased PPV for clinically significant cancer among positives (OR **4.15**, 95% CI 2.93–5.88) (fazekas2024magneticresonanceimaging pages 1-6, fazekas2024magneticresonanceimaging pages 21-25).

### 10.3 Differential diagnosis
BRCA-mutant prostate cancer is not a separate histologic diagnosis; differential diagnosis is primarily across prostate cancer clinical/molecular subtypes (e.g., AR-driven adenocarcinoma vs AR-negative/neuroendocrine/double-negative phenotypes). A relevant model of AR-negative DNPC with BRCA2 variant is described under model systems (turnham2024developmentandcharacterisation pages 1-2).

## 11. Outcome / prognosis

### 11.1 Prognostic impact of BRCA alterations (real-world cfDNA cohort)
In a 2023 cfDNA cohort of men with mCRPC:
- BRCA alterations were associated with significantly worse **PFS** (HR **3.3**, 95% CI 1.9–6.0; p<0.001) and worse **OS** (HR **2.2**, 95% CI 1.1–4.5; p=0.02) (fettke2023brcadeficientmetastaticprostate pages 1-2).
- PSA response rates to AR pathway inhibitors were lower in BRCA-altered patients (32% vs 60%) (fettke2023brcadeficientmetastaticprostate pages 1-2).

More granular hazard ratios by BRCA2 alteration type/zygosity were also reported (e.g., BRCA2 homozygous deletion HR 7.0 for OS in one analysis; and elevated hazards across point mutations, heterozygous/homozygous deletions, and mono/biallelic loss) (fettke2023brcadeficientmetastaticprostate pages 8-10, fettke2023brcadeficientmetastaticprostate pages 7-8).

### 11.2 Predictive impact for PARP inhibitor benefit
In PROfound BRCA subgroup analysis, olaparib improved rPFS and OS versus control, supporting BRCA alterations as predictive biomarkers of PARP inhibitor benefit (mateo2024olaparibforthe pages 1-2).

## 12. Treatment

### 12.1 Targeted therapy: PARP inhibitor monotherapy (mCRPC)
**PROfound BRCA subgroup (2024):**
- Olaparib improved rPFS (HR **0.22**, 95% CI 0.15–0.32) and OS (HR **0.63**, 95% CI 0.42–0.95) vs abiraterone or enzalutamide in BRCA-altered mCRPC after prior NHA (mateo2024olaparibforthe pages 1-2).
- Confirmed ORR was **43.9% (25/57)** vs 0% (0/33) (mateo2024olaparibforthe pages 4-5).
- Benefit was strong in biallelic alterations (rPFS HR **0.08**) and also present in heterozygous/unknown zygosity (HR **0.30**) (mateo2024olaparibforthe pages 1-2).

### 12.2 PARP inhibitor + AR pathway inhibitor combinations (first-line mCRPC in biomarker-defined groups)
**MAGNITUDE (JCO 2023): niraparib + abiraterone**
- In BRCA1/2 subgroup: median rPFS **16.6 vs 10.9 months**, HR **0.53** (95% CI 0.36–0.79), **P=.001** (chi2023niraparibandabiraterone pages 1-2).
- “Treatment … was tolerable, with anemia and hypertension as the most reported grade ≥3 adverse events” (exact frequencies not present in provided excerpt) (chi2023niraparibandabiraterone pages 1-2).

**TALAPRO‑2 (Nature Medicine 2024): talazoparib + enzalutamide**
- In HRR-deficient population: median rPFS **not reached vs 13.8 months**, HR **0.45** (95% CI 0.33–0.61), **P<0.0001**; OS immature but favored talazoparib (HR 0.69; P=0.07) (fizazi2024firstlinetalazoparibwith pages 1-2).

**FDA approval summary (JCO 2024): talazoparib + enzalutamide**
- FDA limited approval to HRR gene–mutated mCRPC based on clinically meaningful rPFS in HRRm population (HR **0.45**, 95% CI 0.33–0.61). In exploratory BRCA-mutated subgroup (n=155), rPFS HR **0.20** (95% CI 0.11–0.36) (heiss2024usfoodand pages 1-2).

A compact synthesis of major therapy evidence is provided in:

| Study (name; phase; publication) | Population/biomarker | Intervention vs control | Key efficacy results | Key safety notes | URL/DOI |
|---|---|---|---|---|---|
| **PROfound BRCA subgroup**; phase III post hoc subgroup analysis; **Mateo et al., J Clin Oncol 2024** | mCRPC with **BRCA1/2 alterations** after prior NHA; 160 patients with BRCA alterations; subgroup analyses by germline vs somatic and zygosity (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, mateo2024olaparibforthe pages 4-5) | **Olaparib** vs physician’s choice **abiraterone or enzalutamide** (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 4-5) | rPFS HR **0.22** (95% CI 0.15–0.32); OS HR **0.63** (95% CI 0.42–0.95). Confirmed ORR **43.9% (25/57)** vs **0% (0/33)**. Biallelic subgroup rPFS HR **0.08**; heterozygous/unknown HR **0.30**. BRCA2 homozygous deletion subset median rPFS **16.6 mo** (95% CI 9.3–NR). Germline BRCA: median rPFS **10.4 vs 1.9 mo**, HR **0.08**; somatic BRCA: **11.1 vs 2.3 mo**, HR **0.16** (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, mateo2024olaparibforthe pages 6-8, mateo2024olaparibforthe pages 4-5) | Safety details not quantified in provided context for this subgroup analysis; efficacy benefit observed across germline and somatic subgroups (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9) | https://doi.org/10.1200/JCO.23.00339 |
| **MAGNITUDE**; phase III; **Chi et al., J Clin Oncol 2023** | First-line mCRPC with prospectively defined **HRR+**, including prespecified **BRCA1/2** subgroup; HRR testing by **tissue and/or plasma** assays (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6, chi2023niraparibandabiraterone pages 3-4) | **Niraparib + abiraterone acetate + prednisone (AAP)** vs **placebo + AAP** (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) | In **BRCA1/2** subgroup: median rPFS **16.6 vs 10.9 mo**, HR **0.53** (95% CI 0.36–0.79), **P=.001**; investigator-assessed rPFS **19.3 vs 12.4 mo**, HR **0.50** (95% CI 0.33–0.75). In overall HRR+ cohort: median rPFS **16.5 vs 13.7 mo**, HR **0.73**, P=.022 (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) | Combination described as tolerable; most frequently reported grade ≥3 AEs were **anemia** and **hypertension**. Exact subgroup frequencies not available in provided context (chi2023niraparibandabiraterone pages 1-2) | https://doi.org/10.1200/JCO.22.01649 |
| **TALAPRO-2**; phase III; **Fizazi et al., Nature Medicine 2024** | First-line mCRPC with **HRR-deficient** tumors; combined HRR-deficient population **N=399**; prospective tumor testing, with later protocol allowance for **ctDNA** testing; common alterations included **BRCA2, ATM, CDK12** (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) | **Talazoparib + enzalutamide** vs **placebo + enzalutamide** (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) | HRR-deficient population: median rPFS **not reached vs 13.8 mo**, HR **0.45** (95% CI 0.33–0.61), **P<0.0001**. Time to PSA progression HR **0.41**; time to cytotoxic chemotherapy HR **0.46**. OS immature but favored talazoparib, HR **0.69** (95% CI 0.46–1.03), P=.07 (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 5-5) | Common AEs: **anemia, fatigue, neutropenia**; detailed rates not provided in the sampled publication excerpt (fizazi2024firstlinetalazoparibwith pages 1-2) | https://doi.org/10.1038/s41591-023-02704-x |
| **TALAPRO-2 FDA approval summary**; regulatory review of phase III data; **Heiss et al., J Clin Oncol 2024** | HRR gene-mutated mCRPC; exploratory **BRCA-mutated** subgroup within combined HRRm population; NGS-based 12-gene panel with tumor tissue initially and **blood ctDNA** allowed by amendment (heiss2024usfoodand pages 2-4) | **Talazoparib + enzalutamide** vs **placebo + enzalutamide** (heiss2024usfoodand pages 2-4) | Combined HRRm population rPFS HR **0.45** (95% CI 0.33–0.61), **P<.0001**. Exploratory **BRCA-mutated** subgroup rPFS HR **0.20** (95% CI 0.11–0.36); OS HR **0.61** (95% CI 0.31–1.23). FDA judged benefit clinically meaningful in HRRm disease, not broad all-comers population (heiss2024usfoodand pages 2-4) | Primary safety population noted, but specific event rates not provided in context excerpt (heiss2024usfoodand pages 2-4) | https://doi.org/10.1200/JCO.23.02182 |
| **Multicenter retrospective PARPi analysis**; retrospective; **Taza et al., JCO Precis Oncol 2021** | **BRCA1- vs BRCA2-altered mCRPC** treated with PARP inhibitors; **n=123** total (**13 BRCA1**, **110 BRCA2**) (taza2021differentialactivityof pages 1-2) | PARPi cohort only: olaparib (most), rucaparib, talazoparib, veliparib; no randomized control arm (taza2021differentialactivityof pages 1-2) | **PSA50 response:** **23% BRCA1** vs **63% BRCA2** (**P=.01**). BRCA2 patients had longer PSA-PFS (HR **1.94**), PFS (HR **2.08**), and OS (HR **3.01**, 95% CI 1.32–6.83, **P=.008**) relative to BRCA1 group. Predictors of PARPi sensitivity: **biallelic** status, **truncating** mutations, absence of **TP53** co-alteration (taza2021differentialactivityof pages 1-2) | Safety not the main focus in provided excerpt; study supports diminished PARPi activity in BRCA1 vs BRCA2 disease (taza2021differentialactivityof pages 1-2) | https://doi.org/10.1200/PO.21.00070 |


*Table: This table summarizes major clinical evidence for BRCA/HRR-mutant prostate cancer focused on PARP inhibitor monotherapy and PARP inhibitor combinations, including efficacy, biomarker context, and available safety findings from the cited studies.*

### 12.3 Safety considerations (class effects)
Hematologic toxicity is a major class consideration. In the retrieved evidence:
- PARP inhibitor combinations frequently report **anemia** as a prominent toxicity signal (chi2023niraparibandabiraterone pages 1-2, fizazi2024firstlinetalazoparibwith pages 1-2).
- TALAPRO-1 safety analyses show anemia as the most common AE class and emphasize supportive care and dose modifications (fizazi2024firstlinetalazoparibwith pages 2-3).

### 12.4 MAXO treatment term suggestions
See ontology mapping table (artifact-03).

## 13. Prevention

### 13.1 Genetic testing, cascade testing, and early detection
The major preventive lever is **identifying germline BRCA1/2 carriers** for:
- cascade testing of relatives
- risk-adapted screening
Cheng et al. emphasize under-recognition and under-testing of male carriers, despite growing clinical actionability (cheng2024brca1brca2and pages 1-3).

### 13.2 Screening: IMPACT trial–informed PSA screening for BRCA2 carriers
Cheng et al. summarize the IMPACT trial approach and downstream implications:
- Annual PSA screening; biopsy threshold PSA >3.0 ng/mL
- After four rounds: biopsy PPV higher in BRCA2 carriers (39% vs 28) and intermediate/high-risk disease more frequent (77% vs 40%) (cheng2024brca1brca2and pages 5-6).
- Guidelines recommend PSA screening start age **40–45** years for male BRCA2 PV carriers (cheng2024brca1brca2and pages 5-6).

### 13.3 MRI-based screening pathways
MRI-based screening pathways reduce biopsies and overdiagnosis while maintaining clinically significant cancer detection in general screening populations, and are noted as effective in genetically predisposed groups, but BRCA2-specific pooled estimates are limited in the meta-analysis (fazekas2024magneticresonanceimaging pages 10-13).

## 14. Other species / natural disease
Not assessed in the retrieved evidence.

## 15. Model organisms / model systems

### 15.1 Patient-derived xenografts (PDX) and explants
- A 2024 report describes a new AR-negative DNPC mCRPC PDX model (CU‑PC01) with TP53 and **BRCA2** variants; it is resistant to enzalutamide and docetaxel but shows initial sensitivity to **olaparib** in short-term explant cultures (turnham2024developmentandcharacterisation pages 1-2).

### 15.2 Organoids and engineered in vitro models
- Prostate cancer organoids derived from PDX models (**LuCaP 96** and **LuCaP 86.2**) and engineered HRD models (PC3M with BRCA2 or ATM knockdown) have been used to study HRD vulnerabilities; these models show strong HRD-associated sensitivity patterns to DNA-damaging agents, and were used for comparative potency analyses against olaparib (kulkarni2024lp184anovel pages 8-9).

## Expert interpretation and implementation notes (authoritative sources)
- **Testing strategy:** High tissue failure rates and ctDNA blind spots for structural variants support combined or sequential testing strategies; a negative ctDNA test does not exclude actionable BRCA alterations, especially homozygous deletions/large rearrangements (chi2023detectionofbrca1 pages 1-2).
- **Treatment selection:** Across multiple phase III programs, benefit is largest in **BRCA-mutated** populations compared with broader HRR or unselected groups, consistent with FDA labeling decisions for HRRm indications (heiss2024usfoodand pages 1-2).
- **Public health/health systems:** Under-testing of males for BRCA1/2 has implications for prevention, cascade testing, and treatment access (cheng2024brca1brca2and pages 1-3).

## Key statistics (quick reference)
- **BRCA1/2 prevalence (pooled, 2023 meta-analysis):** mCRPC somatic BRCA1/2 **11.26%**, germline **5.26%** (valsecchi2023frequencyofgermline pages 1-2).
- **PROfound BRCA subgroup (2024):** olaparib rPFS HR **0.22**; OS HR **0.63**; ORR **43.9%** vs 0% (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 4-5).
- **MAGNITUDE BRCA subgroup (2023):** niraparib+abiraterone median rPFS **16.6 vs 10.9 months**, HR **0.53** (chi2023niraparibandabiraterone pages 1-2).
- **TALAPRO‑2 HRR-deficient (2024):** talazoparib+enzalutamide rPFS HR **0.45** (fizazi2024firstlinetalazoparibwith pages 1-2).
- **PROfound tissue vs ctDNA testing (2023):** ctDNA yield **81%**; PPA **81%**, NPA **92%**; homozygous deletion concordance **27%** (chi2023detectionofbrca1 pages 1-2).

---

## Embedded synthesis tables

| Study (name; phase; publication) | Population/biomarker | Intervention vs control | Key efficacy results | Key safety notes | URL/DOI |
|---|---|---|---|---|---|
| **PROfound BRCA subgroup**; phase III post hoc subgroup analysis; **Mateo et al., J Clin Oncol 2024** | mCRPC with **BRCA1/2 alterations** after prior NHA; 160 patients with BRCA alterations; subgroup analyses by germline vs somatic and zygosity (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, mateo2024olaparibforthe pages 4-5) | **Olaparib** vs physician’s choice **abiraterone or enzalutamide** (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 4-5) | rPFS HR **0.22** (95% CI 0.15–0.32); OS HR **0.63** (95% CI 0.42–0.95). Confirmed ORR **43.9% (25/57)** vs **0% (0/33)**. Biallelic subgroup rPFS HR **0.08**; heterozygous/unknown HR **0.30**. BRCA2 homozygous deletion subset median rPFS **16.6 mo** (95% CI 9.3–NR). Germline BRCA: median rPFS **10.4 vs 1.9 mo**, HR **0.08**; somatic BRCA: **11.1 vs 2.3 mo**, HR **0.16** (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, mateo2024olaparibforthe pages 6-8, mateo2024olaparibforthe pages 4-5) | Safety details not quantified in provided context for this subgroup analysis; efficacy benefit observed across germline and somatic subgroups (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9) | https://doi.org/10.1200/JCO.23.00339 |
| **MAGNITUDE**; phase III; **Chi et al., J Clin Oncol 2023** | First-line mCRPC with prospectively defined **HRR+**, including prespecified **BRCA1/2** subgroup; HRR testing by **tissue and/or plasma** assays (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6, chi2023niraparibandabiraterone pages 3-4) | **Niraparib + abiraterone acetate + prednisone (AAP)** vs **placebo + AAP** (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) | In **BRCA1/2** subgroup: median rPFS **16.6 vs 10.9 mo**, HR **0.53** (95% CI 0.36–0.79), **P=.001**; investigator-assessed rPFS **19.3 vs 12.4 mo**, HR **0.50** (95% CI 0.33–0.75). In overall HRR+ cohort: median rPFS **16.5 vs 13.7 mo**, HR **0.73**, P=.022 (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) | Combination described as tolerable; most frequently reported grade ≥3 AEs were **anemia** and **hypertension**. Exact subgroup frequencies not available in provided context (chi2023niraparibandabiraterone pages 1-2) | https://doi.org/10.1200/JCO.22.01649 |
| **TALAPRO-2**; phase III; **Fizazi et al., Nature Medicine 2024** | First-line mCRPC with **HRR-deficient** tumors; combined HRR-deficient population **N=399**; prospective tumor testing, with later protocol allowance for **ctDNA** testing; common alterations included **BRCA2, ATM, CDK12** (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) | **Talazoparib + enzalutamide** vs **placebo + enzalutamide** (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) | HRR-deficient population: median rPFS **not reached vs 13.8 mo**, HR **0.45** (95% CI 0.33–0.61), **P<0.0001**. Time to PSA progression HR **0.41**; time to cytotoxic chemotherapy HR **0.46**. OS immature but favored talazoparib, HR **0.69** (95% CI 0.46–1.03), P=.07 (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 5-5) | Common AEs: **anemia, fatigue, neutropenia**; detailed rates not provided in the sampled publication excerpt (fizazi2024firstlinetalazoparibwith pages 1-2) | https://doi.org/10.1038/s41591-023-02704-x |
| **TALAPRO-2 FDA approval summary**; regulatory review of phase III data; **Heiss et al., J Clin Oncol 2024** | HRR gene-mutated mCRPC; exploratory **BRCA-mutated** subgroup within combined HRRm population; NGS-based 12-gene panel with tumor tissue initially and **blood ctDNA** allowed by amendment (heiss2024usfoodand pages 2-4) | **Talazoparib + enzalutamide** vs **placebo + enzalutamide** (heiss2024usfoodand pages 2-4) | Combined HRRm population rPFS HR **0.45** (95% CI 0.33–0.61), **P<.0001**. Exploratory **BRCA-mutated** subgroup rPFS HR **0.20** (95% CI 0.11–0.36); OS HR **0.61** (95% CI 0.31–1.23). FDA judged benefit clinically meaningful in HRRm disease, not broad all-comers population (heiss2024usfoodand pages 2-4) | Primary safety population noted, but specific event rates not provided in context excerpt (heiss2024usfoodand pages 2-4) | https://doi.org/10.1200/JCO.23.02182 |
| **Multicenter retrospective PARPi analysis**; retrospective; **Taza et al., JCO Precis Oncol 2021** | **BRCA1- vs BRCA2-altered mCRPC** treated with PARP inhibitors; **n=123** total (**13 BRCA1**, **110 BRCA2**) (taza2021differentialactivityof pages 1-2) | PARPi cohort only: olaparib (most), rucaparib, talazoparib, veliparib; no randomized control arm (taza2021differentialactivityof pages 1-2) | **PSA50 response:** **23% BRCA1** vs **63% BRCA2** (**P=.01**). BRCA2 patients had longer PSA-PFS (HR **1.94**), PFS (HR **2.08**), and OS (HR **3.01**, 95% CI 1.32–6.83, **P=.008**) relative to BRCA1 group. Predictors of PARPi sensitivity: **biallelic** status, **truncating** mutations, absence of **TP53** co-alteration (taza2021differentialactivityof pages 1-2) | Safety not the main focus in provided excerpt; study supports diminished PARPi activity in BRCA1 vs BRCA2 disease (taza2021differentialactivityof pages 1-2) | https://doi.org/10.1200/PO.21.00070 |


*Table: This table summarizes major clinical evidence for BRCA/HRR-mutant prostate cancer focused on PARP inhibitor monotherapy and PARP inhibitor combinations, including efficacy, biomarker context, and available safety findings from the cited studies.*

| Specimen/test | Yield | Agreement metrics | Strengths | Limitations | Source |
|---|---:|---|---|---|---|
| Tumor tissue NGS (FoundationOne CDx–based screening in PROfound) | Tissue molecular screening failure rate ~31% | Used as reference standard for matched analyses; when compared with ctDNA, corresponding ctDNA PPA/sensitivity 81% and NPA/specificity 92% | Current gold-standard approach for HRR testing; better detection of structural events such as homozygous deletions and large rearrangements; avoids some plasma false negatives (chi2023detectionofbrca1 pages 2-2, chi2023detectionofbrca1 pages 6-8) | Invasive biopsy; frequent insufficiency/quality failures, especially with small samples and bone-predominant disease; decalcification and low DNA quantity/quality can impair testing | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 2-4, chi2023detectionofbrca1 pages 2-2) |
| Plasma ctDNA NGS (FoundationOne Liquid CDx in matched PROfound cohort) | 81% (503/619) yielded an NGS result; ~90% yield after excluding technical batch failures; plasma volume ≥7 mL improved yield (82% vs 69%) | Overall BRCA/ATM status vs tissue: PPA 81%, NPA 92%, PPV 0.68, NPV 0.96; variant-level sensitivity 74% and overall variant concordance 71% (146/207 shared variants) | Minimally invasive; complements tissue when tissue is unavailable/insufficient; identified additional patients potentially eligible for PARP inhibitor treatment; high specificity even at lower ctDNA fractions | False negatives occur, especially with low ctDNA fraction/non-shedders; ~20% of qualifying mutations identified by tissue only; ctDNA fraction not evaluable in 13% | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 2-4, chi2023detectionofbrca1 pages 6-8) |
| Plasma ctDNA NGS performance by ctDNA fraction | 428/491 (87%) had evaluable ctDNA fraction | At ctDNA fraction ≥10%: sensitivity 87%, specificity 90%; at 1% to <10%: sensitivity 92%, specificity 95%; at <1%/not evaluable: sensitivity fell to 68%/56% while specificity remained high (92%/100%) | Best performance when tumor shedding is adequate; useful for dynamic testing in metastatic disease | Low-shedding tumors markedly reduce sensitivity; negative plasma test does not exclude actionable BRCA/ATM alteration | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 6-8) |
| Variant subtype concordance: nonsense / splice / frameshift | Not applicable | High concordance versus tissue: nonsense 93%, splice 87%, frameshift 86% | ctDNA performs well for many short variants/indels relevant to BRCA/ATM | Some splice and missense variants show lower overlap when assessed from ctDNA perspective | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 5-6) |
| Variant subtype concordance: large rearrangements / homozygous deletions | Not applicable | Large rearrangements 63% concordance from tissue reference; homozygous deletions only 27% concordance from tissue reference | Tissue testing better captures these lesion classes | Major plasma blind spot, especially at low ctDNA fraction; important because BRCA2 homozygous deletions can predict strong PARP inhibitor sensitivity | Chi et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-22-0931 (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 4-5, chi2023detectionofbrca1 pages 5-6) |
| Clinical interpretation of negative plasma test | Not applicable | Approx. 80% concordance overall with tissue in PROfound-era analyses | ctDNA is clinically useful to complement tissue and can support identification of BRCA/ATM-altered mCRPC for olaparib | FoundationOne Liquid CDx not validated for some homozygous BRCA deletions/large rearrangements; low tumor content and CHIP can confound results; FDA label cautions that a negative liquid test does not rule out actionable alterations and tissue testing should be pursued if feasible | Matsubara et al., 2023, Clin Cancer Res, doi:10.1158/1078-0432.CCR-21-3577 (matsubara2023olaparibefficacyin pages 5-6); Chi et al., 2023 (chi2023detectionofbrca1 pages 6-8) |


*Table: This table compares tumor tissue NGS and plasma ctDNA testing for BRCA/ATM alterations in mCRPC, emphasizing test yield, concordance, and important structural-variant limitations. It is useful for selecting testing strategies and interpreting negative liquid-biopsy results.*

| Setting | Germline BRCA1 % | Somatic BRCA1 % | Germline BRCA2 % | Somatic BRCA2 % | Notes | Source |
|---|---:|---:|---:|---:|---|---|
| Any-stage prostate cancer | 0.73% | 1.20% | 3.25% | 6.29% | Meta-analysis: somatic mutations more common than germline; BRCA2 more common than BRCA1. Combined BRCA1/2 frequency: 4.47% germline, 7.18% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic prostate cancer | 0.94% | 1.10% | 4.51% | 10.26% | Frequency rises in metastatic disease; BRCA2 predominates; combined BRCA1/2 frequency: 5.84% germline, 10.94% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic castration-resistant prostate cancer (mCRPC) | 1.21% | 1.10% | 3.90% | 10.52% | In mCRPC, somatic BRCA2 is especially enriched; combined BRCA1/2 frequency: 5.26% germline, 11.26% somatic. (valsecchi2023frequencyofgermline pages 8-10) | Valsecchi et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092435 |
| Metastatic prostate cancer, germline DDR pathogenic variants | — | — | ~6% (BRCA1/2 combined) | — | Review states ~12% of metastatic prostate cancer patients harbor germline DDR pathogenic variants, with BRCA1/2 the most frequent DDR genes (~6% combined). Also notes germline and somatic BRCA1/2 frequencies are reported as similar enough that both should be evaluated. (inoue2023rolesofthe pages 2-4) | Inoue et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15092662 |
| BRCA2-altered mCRPC PARPi-treated cohort (clinical provenance split) | — | — | 50% of BRCA2-altered cases were germline overall; 58% among responders | 50% of BRCA2-altered cases were somatic overall; 39% among responders | Clinical cohort provenance rather than population prevalence: in BRCA2-altered mCRPC treated with PARP inhibitors, mutation origin was roughly evenly split overall (56/110 germline, 54/110 somatic), with germline enrichment among responders. (taza2021differentialactivityof pages 20-21) | Taza et al., 2021, *JCO Precision Oncology*; https://doi.org/10.1200/PO.21.00070 |
| Real-world ctDNA metastatic prostate cancer cohort | not separately reported | not separately reported | not separately reported | not separately reported | ctDNA cohort found BRCA1/2 alterations (germline or somatic) in 21% of patients with metastatic prostate cancer; this row reflects assay-detected prevalence in a progression-enriched real-world blood cohort, not stage-specific tissue prevalence. (valsecchi2023frequencyofgermline pages 8-10) | Bang et al., 2023, *Cancers*; https://doi.org/10.3390/cancers15153998 |


*Table: This table summarizes reported BRCA1/2 mutation frequencies and mutation provenance in prostate cancer across disease settings. It combines meta-analytic prevalence estimates with review and cohort data to distinguish population frequency from clinical provenance in advanced disease.*

| Section | Suggested term(s) | Evidence/rationale |
|---|---|---|
| Disease concept | prostate cancer — MONDO:0008315; BRCA-mutant prostate cancer — MONDO: not clearly established in available context; prostate carcinoma — EFO:0001663 | Open Targets evidence links BRCA1/2 to prostate cancer/prostate carcinoma; BRCA-mutant prostate cancer is best modeled as a molecularly defined subtype of prostate cancer rather than a clearly separate MONDO disease in the provided context (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Key genes | BRCA2 (HGNC:1101); BRCA1 (HGNC:1100); ATM (HGNC:795) | BRCA2 is the dominant altered gene in prostate cancer and is more common than BRCA1; ATM is a major comparator/HRR gene in trials and testing panels (inoue2023rolesofthe pages 2-4, alakhras2024parpinhibitorsin pages 10-11, heiss2024usfoodand pages 2-4) |
| Key genes | TP53 (HGNC:11998); AR (HGNC:644); CDK12 (HGNC:24243) | BRCA1-altered disease shows more concurrent TP53 alterations and worse PARPi outcomes; AR biology underlies PARP/AR combination rationale; CDK12 is a frequent HRR-panel gene in advanced disease studies (taza2021differentialactivityof pages 1-2, alakhras2024parpinhibitorsin pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Phenotypes (HPO) | Aggressive prostate carcinoma phenotype — HPO likely prefix HP:; High Gleason score — HPO likely prefix HP:; Early adult onset/neoplasm onset younger than typical — HPO likely prefix HP:0003581/HP: | BRCA2 carriers show more clinically significant disease, younger onset, and high-grade tumors; BRCA-deficient metastatic disease has adverse prognosis (inoue2023rolesofthe pages 2-4, taza2021differentialactivityof pages 1-2) |
| Phenotypes (HPO) | Metastatic prostate adenocarcinoma — HPO likely prefix HP:0004409/HP:; Bone metastasis — HPO likely prefix HP:0002664; Castration-resistant disease — HPO likely prefix HP: | BRCA1 patients more often present metastatic at diagnosis; BRCA2 cohorts show frequent M1 disease and bone metastases; advanced trials focus on mCRPC (taza2021differentialactivityof pages 1-2, taza2021differentialactivityof pages 20-21, mateo2024olaparibforthe pages 1-2) |
| Phenotypes (HPO) | Anemia — HP:0001903; Fatigue — HP:0012378; Neutropenia — HP:0001875 | Common toxicities of PARP inhibitors/combination therapy include anemia, fatigue, and neutropenia; anemia is the most frequent grade ≥3 hematologic adverse event (tisseverasinghe2023advancesinparp pages 10-11, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Anatomical entities (UBERON) | prostate gland — UBERON:0002367; prostate epithelium — UBERON likely prefix UBERON:; prostate stromal tissue — UBERON likely prefix UBERON: | Primary organ and tissue compartments involved in prostate carcinoma biology (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Anatomical entities (UBERON) | bone of skeletal system — UBERON:0001474; lymph node — UBERON:0000029; blood/plasma — UBERON:0000178 / body fluid term likely needed | Bone metastases are common; lymph nodes are common metastatic sites; plasma is important for ctDNA diagnostics (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Biological processes (GO) | homologous recombination — GO:0000724; DNA repair — GO:0006281; double-strand break repair — GO:0006302 | Core BRCA biology in prostate cancer is homologous recombination repair deficiency and impaired DSB repair (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | response to DNA damage stimulus — GO:0006974; DNA replication fork processing — GO likely prefix GO:; cell cycle process — GO:0022402 | PARP inhibition exploits replication-fork collapse and DNA damage accumulation; BRCA2-mutant tumors are enriched for cell-cycle programs (inoue2023rolesofthe pages 2-4, fizazi2024firstlinetalazoparibwith pages 1-2) |
| Biological processes (GO) | androgen receptor signaling pathway — GO likely prefix GO:; regulation of transcription by RNA polymerase II — GO:0006357; synthetic lethal interaction context — no direct GO term, represent via DNA repair dependency | TALAPRO-2 and FDA summary emphasize AR–PARP interplay: AR inhibition downregulates HRR genes and PARP inhibition suppresses AR transcriptional activity (fizazi2024firstlinetalazoparibwith pages 1-2, heiss2024usfoodand pages 2-4) |
| Cell types (CL) | prostate gland epithelial cell — CL likely prefix CL:; luminal epithelial cell of prostate — CL likely prefix CL:; basal cell of prostate epithelium — CL likely prefix CL: | Prostate cancer arises from epithelial compartments; organoid/PDX models preserve epithelial tumor features (fizazi2024firstlinetalazoparibwith pages 1-2, fizazi2024firstlinetalazoparibwith pages 2-3) |
| Cell types (CL) | metastatic prostate cancer cell — CL likely prefix CL: cancer cell term; osteoblast — CL:0000062; osteoclast — CL:0000097 | Bone metastasis is a hallmark clinical site and relevant microenvironmental context (taza2021differentialactivityof pages 20-21, chi2023detectionofbrca1 pages 1-2) |
| Treatments (MAXO) | PARP inhibitor therapy — MAXO likely prefix MAXO:; olaparib treatment — MAXO likely prefix MAXO:; talazoparib treatment — MAXO likely prefix MAXO: | Olaparib improves rPFS/OS/ORR in BRCA-altered mCRPC; talazoparib + enzalutamide improves rPFS in HRR-mutated disease, especially BRCA-mutant subgroup (mateo2024olaparibforthe pages 1-2, mateo2024olaparibforthe pages 8-9, heiss2024usfoodand pages 2-4) |
| Treatments (MAXO) | niraparib plus abiraterone therapy — MAXO likely prefix MAXO:; enzalutamide therapy — MAXO likely prefix MAXO:; androgen receptor pathway inhibitor therapy — MAXO likely prefix MAXO: | MAGNITUDE supports niraparib + abiraterone in BRCA1/2-mutated mCRPC; ARPI backbone is central to current implementation (chi2023niraparibandabiraterone pages 1-2, chi2023niraparibandabiraterone pages 5-6) |
| Treatments (MAXO) | circulating tumor DNA testing-guided targeted therapy — MAXO likely prefix MAXO:; germline genetic testing — MAXO likely prefix MAXO:; supportive treatment for anemia — MAXO likely prefix MAXO: | Tissue and ctDNA testing are used to identify eligible patients; anemia management is a key supportive action during PARPi therapy (chi2023detectionofbrca1 pages 1-2, chi2023detectionofbrca1 pages 2-4, tisseverasinghe2023advancesinparp pages 10-11) |


*Table: This table proposes practical ontology mappings for a BRCA-mutant prostate cancer knowledge-base entry, spanning disease concept, genes, phenotypes, anatomy, processes, cell types, and treatments. It is grounded in the provided evidence on aggressive disease biology, metastatic behavior, PARP inhibitor response, and treatment toxicity.*


References

1. (heiss2024usfoodand pages 2-4): Brian L. Heiss, Elaine Chang, Xin Gao, Tien Truong, Michael H. Brave, Erik Bloomquist, Ankit Shah, Salaheldin Hamed, Jeffrey Kraft, Haw-Jyh Chiu, Tiffany K. Ricks, Amy Tilley, William F. Pierce, Liuya Tang, Abdelrahmman Abukhdeir, Shyam Kalavar, Reena Philip, Shenghui Tang, Richard Pazdur, Laleh Amiri-Kordestani, Paul G. Kluetz, and Daniel L. Suzman. Us food and drug administration approval summary: talazoparib in combination with enzalutamide for treatment of patients with homologous recombination repair gene-mutated metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 42:1851-1860, May 2024. URL: https://doi.org/10.1200/jco.23.02182, doi:10.1200/jco.23.02182. This article has 29 citations and is from a highest quality peer-reviewed journal.

2. (mateo2024olaparibforthe pages 1-2): Joaquin Mateo, Johann S. de Bono, Karim Fizazi, Fred Saad, Neal Shore, Shahneen Sandhu, Kim N. Chi, Neeraj Agarwal, David Olmos, Antoine Thiery-Vuillemin, Mustafa Özgüroğlu, Niven Mehra, Nobuaki Matsubara, Jae Young Joung, Charles Padua, Ernesto Korbenfeld, Jinyu Kang, Helen Marshall, Zhongwu Lai, Alan Barnicle, Christian Poehlein, Natalia Lukashchuk, and Maha Hussain. Olaparib for the treatment of patients with metastatic castration-resistant prostate cancer and alterations in <i>brca1</i> and/or <i>brca2</i> in the profound trial. Journal of Clinical Oncology, 42:571-583, Feb 2024. URL: https://doi.org/10.1200/jco.23.00339, doi:10.1200/jco.23.00339. This article has 91 citations and is from a highest quality peer-reviewed journal.

3. (fettke2023brcadeficientmetastaticprostate pages 1-2): Heidi Fettke, Chao Dai, Edmond M. Kwan, Tiantian Zheng, Pan Du, Nicole Ng, Patricia Bukczynska, Maria Docanto, Louise Kostos, Siavash Foroughi, Stephen Brown, Lisa-Jane K. Graham, Kate Mahon, Lisa G. Horvath, Shidong Jia, Manish Kohli, and Arun A. Azad. Brca-deficient metastatic prostate cancer has an adverse prognosis and distinct genomic phenotype. eBioMedicine, 95:104738, Sep 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104738, doi:10.1016/j.ebiom.2023.104738. This article has 41 citations and is from a peer-reviewed journal.

4. (fizazi2024firstlinetalazoparibwith pages 1-2): Karim Fizazi, Arun A. Azad, Nobuaki Matsubara, Joan Carles, Andre P. Fay, Ugo De Giorgi, Jae Young Joung, Peter C. C. Fong, Eric Voog, Robert J. Jones, Neal D. Shore, Curtis Dunshee, Stefanie Zschäbitz, Jan Oldenburg, Dingwei Ye, Xun Lin, Cynthia G. Healy, Nicola Di Santo, A. Douglas Laird, Fabian Zohren, and Neeraj Agarwal. First-line talazoparib with enzalutamide in hrr-deficient metastatic castration-resistant prostate cancer: the phase 3 talapro-2 trial. Nature Medicine, 30:257-264, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02704-x, doi:10.1038/s41591-023-02704-x. This article has 152 citations and is from a highest quality peer-reviewed journal.

5. (chi2023niraparibandabiraterone pages 1-2): Kim N. Chi, Dana Rathkopf, Matthew R. Smith, Eleni Efstathiou, Gerhardt Attard, David Olmos, Ji Youl Lee, Eric J. Small, Andrea J. Pereira de Santana Gomes, Guilhem Roubaud, Marniza Saad, Bogdan Zurawski, Valerii Sakalo, Gary E. Mason, Peter Francis, George Wang, Daphne Wu, Brooke Diorio, Angela Lopez-Gitlitz, Shahneen Sandhu, Maria Alvarez, Gabriela Gatica, Martin Greco, Ernesto Korbenfeld, Esteban Metrebian, Jorge Salinas, Alejandro Salvatierra, Marcelo Tatangelo, Tom Ferguson, Howard Gurney, Elizabeth Hovey, Anthony Joshua, Matos Marco, Gavin Marx, Michelle Morris, Siobhan Ng, David Pook, Shahneen Sandhu, Ali Tafreshi, Thean Hsiang Tan, Tsvetanka Tosheva, Livia Andrade, Felipe Cruz, Luiza Faria, Jose Figueiredo, Fabio Franke, Andrea Juliana Gomes, Ariel Kann, Celio Kussumoto, Suelen Martins, Andre Murad, Helio Pinczowski, Giovani Pioner, Luis Pires, Daniel Preto, Gisele Santos, Eduardo Silva, Jamile Silva, Luciano Viana, Karina Vianna, Adriano Paula, Zhiwen Chen, Kim Chi, Urban Emmenegger, Neil Fleshner, Sunil Parimi, Fred Saad, Francisco Vera-Badillo, Hongqian Guo, Hong Luo, Lulin Ma, Mingxing Qui, Wei Xue, Guo Yonglian, Lei Li, Jinxian Pu, Song Zheng, Qing Zou, Milos Brodak, Milan Hora, Vladimir Samal, Vladimir Student, Jaroslav Vanasek, Emmanuelle Bompas, Philippe Barthelemy, Delphine Borchiellini, Aude Flechon, Hakim Mahammedi, Guilhem Roubaud, Antoine Thiery-Vuillemin, Diego Tosi, Spaeth Dominique, Carole Helissey, Martin Boegemann, Susan Feyerabend, Eva Hellmis, Martin Schostak, Gerhardt Attard, Anna Lydon, Ian Sayers, Omi Parikh, Duncan Wheatley, Peter Arkosy, Jozsef Erfan, Lajos Geczi, Peter Nyirady, Judit Olah, Istvan Papos, Bela Piko, Raanan Berger, Avivit Peer, Umberto Basso, Sergio Bracarda, Orazio Caffo, Francesco Carrozza, Gianluca Del Conte, Luca Galli, Donatello Gasparro, Sandro Pignata, Riccardo Ricotta, Daniele Santini, Giampaolo Tortora, Seoksoo Byun, SeolHo Choo, ByungHa Chung, Jaeyoung Joung, Wonho Jung, Taek Won Kang, Cheol Kwak, TaeGyun Kwon, Hyo Jin Lee, Ji Youl Lee, SeongIl Seo, YoungDeuk Choi, HongKoo Ha, ChoungSoo Kim, Flora Li Tze Chong, Chun Sen Lim, Vijayan Manogran, Hwoei Fen Soo Hoo, Guan Chou Teh, Marniza Saad, David Calvo Dominguez, Abraham Cardenas, Julia Saenz, Andre Bergman, Helgi Helgason, C.B. Hunting, Rik Somford, Tomasz Byrski, Tomasz Drewa, Dorota Filarska, Jolanta LuniewskaBury, Adam Marcheluk, Konrad Talasiewicz, Krzysztof Tupikowski, Renata Zaucha, Bogdan Zurawski, Pedro Madeira, Andre Mansinho, Nuno Vau, Anna Alyasova, Victoria Chistyakova, Denis Khvorostenko, Dmitry Kirtbaya, Gennady Kolesnikov, Evgeny Kopyltsov, Igor Lifirenko, Alexander Lykov, Konstantin Penkov, Andrey Semenov, Mikhail Shkolnik, Pavel Skopin, Roman Smirnov, Evgeny Usynin, Sergey Varlamov, Vladimir Vladimirov, Teresa Alonso, Sara Breijo, Elena Castro, Enrique Gallardo, Jose Gutierrez Banos, Alvaro Juarez, Rebeca Lozano, Pablo Maroto, Javier Puente, Alejo Rodriguez-Vida, Regina Girones, Begona Mellado, Enrique Castellanos, Chunde Li, Chao-Hsiang Chang, Hsiao-Jen Chung, Kuan-Hua Huang, Yen-Chuan Ou, Yu-Chieh Tsai, Shian-Shiang Wang, Wen-Jeng Wu, See Tong Pang, Cagatay Arslan, Devrim Cabuk, Hasan Coskun, Mahmut Gumus, Mustafa Ozguroglu, Berna Oksuzoglu, Berksoy Sahin, Deniz Tural, Bulent Yalcin, Irfan Cicin, Igor Bondarenko, Yaroslav Gotsuliak, Yevhen Hotko, Gennadii Khareba, Oleksandr Lychkovskyy, Iryna Lytvyn, Taron Nalbandyan, Viktor Paramonov, Valerii Sakalo, Eduard Stakhovsky, Viktor Stus, Sunil Babu, Alan Bryce, David Cahn, Herta Chao, Franklin Chu, Curtis Dunshee, Oscar Goodman, Michael Grable, Jason Hafron, Joelle Hamilton, Ralph Hauke, Joseph Maly, David Morris, Gregg Newman, Patrick Pilie, Neal Shore, Paul Sieber, Matthew Smith, Andrew Trainer, and Ronald Tutrone. Niraparib and abiraterone acetate for metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 41:3339-3351, Jun 2023. URL: https://doi.org/10.1200/jco.22.01649, doi:10.1200/jco.22.01649. This article has 380 citations and is from a highest quality peer-reviewed journal.

6. (valsecchi2023frequencyofgermline pages 1-2): Anna Amela Valsecchi, Rossana Dionisio, Olimpia Panepinto, Jessica Paparo, Andrea Palicelli, Francesca Vignani, and Massimo Di Maio. Frequency of germline and somatic brca1 and brca2 mutations in prostate cancer: an updated systematic review and meta-analysis. Cancers, 15:2435, Apr 2023. URL: https://doi.org/10.3390/cancers15092435, doi:10.3390/cancers15092435. This article has 38 citations.

7. (chi2023detectionofbrca1 pages 1-2): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

8. (inoue2023rolesofthe pages 2-4): Takahiro Inoue, Sho Sekito, Takumi Kageyama, Yusuke Sugino, and Takeshi Sasaki. Roles of the parp inhibitor in brca1 and brca2 pathogenic mutated metastatic prostate cancer: direct functions and modification of the tumor microenvironment. Cancers, 15:2662, May 2023. URL: https://doi.org/10.3390/cancers15092662, doi:10.3390/cancers15092662. This article has 18 citations.

9. (cheng2024brca1brca2and pages 5-6): Heather H. Cheng, Jeffrey W. Shevach, Elena Castro, Fergus J. Couch, Susan M. Domchek, Rosalind A. Eeles, Veda N. Giri, Michael J. Hall, Mary-Claire King, Daniel W. Lin, Stacy Loeb, Todd M. Morgan, Kenneth Offit, Colin C. Pritchard, Edward M. Schaeffer, Brittany M. Szymaniak, Jason L. Vassy, Bryson W. Katona, and Kara N. Maxwell. <i>brca1, brca2</i>, and associated cancer risks and management for male patients. JAMA Oncology, 10:1272, Sep 2024. URL: https://doi.org/10.1001/jamaoncol.2024.2185, doi:10.1001/jamaoncol.2024.2185. This article has 40 citations and is from a highest quality peer-reviewed journal.

10. (cheng2024brca1brca2and pages 16-19): Heather H. Cheng, Jeffrey W. Shevach, Elena Castro, Fergus J. Couch, Susan M. Domchek, Rosalind A. Eeles, Veda N. Giri, Michael J. Hall, Mary-Claire King, Daniel W. Lin, Stacy Loeb, Todd M. Morgan, Kenneth Offit, Colin C. Pritchard, Edward M. Schaeffer, Brittany M. Szymaniak, Jason L. Vassy, Bryson W. Katona, and Kara N. Maxwell. <i>brca1, brca2</i>, and associated cancer risks and management for male patients. JAMA Oncology, 10:1272, Sep 2024. URL: https://doi.org/10.1001/jamaoncol.2024.2185, doi:10.1001/jamaoncol.2024.2185. This article has 40 citations and is from a highest quality peer-reviewed journal.

11. (valsecchi2023frequencyofgermline pages 2-5): Anna Amela Valsecchi, Rossana Dionisio, Olimpia Panepinto, Jessica Paparo, Andrea Palicelli, Francesca Vignani, and Massimo Di Maio. Frequency of germline and somatic brca1 and brca2 mutations in prostate cancer: an updated systematic review and meta-analysis. Cancers, 15:2435, Apr 2023. URL: https://doi.org/10.3390/cancers15092435, doi:10.3390/cancers15092435. This article has 38 citations.

12. (valsecchi2023frequencyofgermline pages 25-27): Anna Amela Valsecchi, Rossana Dionisio, Olimpia Panepinto, Jessica Paparo, Andrea Palicelli, Francesca Vignani, and Massimo Di Maio. Frequency of germline and somatic brca1 and brca2 mutations in prostate cancer: an updated systematic review and meta-analysis. Cancers, 15:2435, Apr 2023. URL: https://doi.org/10.3390/cancers15092435, doi:10.3390/cancers15092435. This article has 38 citations.

13. (valsecchi2023frequencyofgermline pages 8-10): Anna Amela Valsecchi, Rossana Dionisio, Olimpia Panepinto, Jessica Paparo, Andrea Palicelli, Francesca Vignani, and Massimo Di Maio. Frequency of germline and somatic brca1 and brca2 mutations in prostate cancer: an updated systematic review and meta-analysis. Cancers, 15:2435, Apr 2023. URL: https://doi.org/10.3390/cancers15092435, doi:10.3390/cancers15092435. This article has 38 citations.

14. (taza2021differentialactivityof pages 20-21): Fadi Taza, Albert E. Holler, Wei Fu, Hao Wang, Nabil Adra, Costantine Albany, Ryan Ashkar, Heather H. Cheng, Alexandra O. Sokolova, Neeraj Agarwal, Adam Kessel, Alan Bryce, Nellie Nafissi, Pedro Barata, A. Oliver Sartor, Diogo Bastos, Oren Smaletz, Jacob E. Berchuck, Mary-Ellen Taplin, Rahul Aggarwal, Cora N. Sternberg, Panagiotis J. Vlachostergios, Ajjai S. Alva, Christopher Su, Catherine H. Marshall, and Emmanuel S. Antonarakis. Differential activity of parp inhibitors in<i>brca1</i>- versus<i>brca2</i>-altered metastatic castration-resistant prostate cancer. JCO Precision Oncology, pages 1200-1220, Nov 2021. URL: https://doi.org/10.1200/po.21.00070, doi:10.1200/po.21.00070. This article has 68 citations and is from a peer-reviewed journal.

15. (taza2021differentialactivityof pages 1-2): Fadi Taza, Albert E. Holler, Wei Fu, Hao Wang, Nabil Adra, Costantine Albany, Ryan Ashkar, Heather H. Cheng, Alexandra O. Sokolova, Neeraj Agarwal, Adam Kessel, Alan Bryce, Nellie Nafissi, Pedro Barata, A. Oliver Sartor, Diogo Bastos, Oren Smaletz, Jacob E. Berchuck, Mary-Ellen Taplin, Rahul Aggarwal, Cora N. Sternberg, Panagiotis J. Vlachostergios, Ajjai S. Alva, Christopher Su, Catherine H. Marshall, and Emmanuel S. Antonarakis. Differential activity of parp inhibitors in<i>brca1</i>- versus<i>brca2</i>-altered metastatic castration-resistant prostate cancer. JCO Precision Oncology, pages 1200-1220, Nov 2021. URL: https://doi.org/10.1200/po.21.00070, doi:10.1200/po.21.00070. This article has 68 citations and is from a peer-reviewed journal.

16. (alakhras2024parpinhibitorsin pages 10-11): Ashaar Al-Akhras, Chadi Hage Chehade, Arshit Narang, and Umang Swami. Parp inhibitors in metastatic castration-resistant prostate cancer: unraveling the therapeutic landscape. Life, 14:198, Jan 2024. URL: https://doi.org/10.3390/life14020198, doi:10.3390/life14020198. This article has 22 citations.

17. (tisseverasinghe2023advancesinparp pages 10-11): Steven Tisseverasinghe, Boris Bahoric, Maurice Anidjar, Stephan Probst, and Tamim Niazi. Advances in parp inhibitors for prostate cancer. Cancers, 15:1849, Mar 2023. URL: https://doi.org/10.3390/cancers15061849, doi:10.3390/cancers15061849. This article has 27 citations.

18. (fizazi2024firstlinetalazoparibwith pages 2-3): Karim Fizazi, Arun A. Azad, Nobuaki Matsubara, Joan Carles, Andre P. Fay, Ugo De Giorgi, Jae Young Joung, Peter C. C. Fong, Eric Voog, Robert J. Jones, Neal D. Shore, Curtis Dunshee, Stefanie Zschäbitz, Jan Oldenburg, Dingwei Ye, Xun Lin, Cynthia G. Healy, Nicola Di Santo, A. Douglas Laird, Fabian Zohren, and Neeraj Agarwal. First-line talazoparib with enzalutamide in hrr-deficient metastatic castration-resistant prostate cancer: the phase 3 talapro-2 trial. Nature Medicine, 30:257-264, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02704-x, doi:10.1038/s41591-023-02704-x. This article has 152 citations and is from a highest quality peer-reviewed journal.

19. (mateo2024olaparibforthe pages 8-9): Joaquin Mateo, Johann S. de Bono, Karim Fizazi, Fred Saad, Neal Shore, Shahneen Sandhu, Kim N. Chi, Neeraj Agarwal, David Olmos, Antoine Thiery-Vuillemin, Mustafa Özgüroğlu, Niven Mehra, Nobuaki Matsubara, Jae Young Joung, Charles Padua, Ernesto Korbenfeld, Jinyu Kang, Helen Marshall, Zhongwu Lai, Alan Barnicle, Christian Poehlein, Natalia Lukashchuk, and Maha Hussain. Olaparib for the treatment of patients with metastatic castration-resistant prostate cancer and alterations in <i>brca1</i> and/or <i>brca2</i> in the profound trial. Journal of Clinical Oncology, 42:571-583, Feb 2024. URL: https://doi.org/10.1200/jco.23.00339, doi:10.1200/jco.23.00339. This article has 91 citations and is from a highest quality peer-reviewed journal.

20. (chi2023niraparibandabiraterone pages 5-6): Kim N. Chi, Dana Rathkopf, Matthew R. Smith, Eleni Efstathiou, Gerhardt Attard, David Olmos, Ji Youl Lee, Eric J. Small, Andrea J. Pereira de Santana Gomes, Guilhem Roubaud, Marniza Saad, Bogdan Zurawski, Valerii Sakalo, Gary E. Mason, Peter Francis, George Wang, Daphne Wu, Brooke Diorio, Angela Lopez-Gitlitz, Shahneen Sandhu, Maria Alvarez, Gabriela Gatica, Martin Greco, Ernesto Korbenfeld, Esteban Metrebian, Jorge Salinas, Alejandro Salvatierra, Marcelo Tatangelo, Tom Ferguson, Howard Gurney, Elizabeth Hovey, Anthony Joshua, Matos Marco, Gavin Marx, Michelle Morris, Siobhan Ng, David Pook, Shahneen Sandhu, Ali Tafreshi, Thean Hsiang Tan, Tsvetanka Tosheva, Livia Andrade, Felipe Cruz, Luiza Faria, Jose Figueiredo, Fabio Franke, Andrea Juliana Gomes, Ariel Kann, Celio Kussumoto, Suelen Martins, Andre Murad, Helio Pinczowski, Giovani Pioner, Luis Pires, Daniel Preto, Gisele Santos, Eduardo Silva, Jamile Silva, Luciano Viana, Karina Vianna, Adriano Paula, Zhiwen Chen, Kim Chi, Urban Emmenegger, Neil Fleshner, Sunil Parimi, Fred Saad, Francisco Vera-Badillo, Hongqian Guo, Hong Luo, Lulin Ma, Mingxing Qui, Wei Xue, Guo Yonglian, Lei Li, Jinxian Pu, Song Zheng, Qing Zou, Milos Brodak, Milan Hora, Vladimir Samal, Vladimir Student, Jaroslav Vanasek, Emmanuelle Bompas, Philippe Barthelemy, Delphine Borchiellini, Aude Flechon, Hakim Mahammedi, Guilhem Roubaud, Antoine Thiery-Vuillemin, Diego Tosi, Spaeth Dominique, Carole Helissey, Martin Boegemann, Susan Feyerabend, Eva Hellmis, Martin Schostak, Gerhardt Attard, Anna Lydon, Ian Sayers, Omi Parikh, Duncan Wheatley, Peter Arkosy, Jozsef Erfan, Lajos Geczi, Peter Nyirady, Judit Olah, Istvan Papos, Bela Piko, Raanan Berger, Avivit Peer, Umberto Basso, Sergio Bracarda, Orazio Caffo, Francesco Carrozza, Gianluca Del Conte, Luca Galli, Donatello Gasparro, Sandro Pignata, Riccardo Ricotta, Daniele Santini, Giampaolo Tortora, Seoksoo Byun, SeolHo Choo, ByungHa Chung, Jaeyoung Joung, Wonho Jung, Taek Won Kang, Cheol Kwak, TaeGyun Kwon, Hyo Jin Lee, Ji Youl Lee, SeongIl Seo, YoungDeuk Choi, HongKoo Ha, ChoungSoo Kim, Flora Li Tze Chong, Chun Sen Lim, Vijayan Manogran, Hwoei Fen Soo Hoo, Guan Chou Teh, Marniza Saad, David Calvo Dominguez, Abraham Cardenas, Julia Saenz, Andre Bergman, Helgi Helgason, C.B. Hunting, Rik Somford, Tomasz Byrski, Tomasz Drewa, Dorota Filarska, Jolanta LuniewskaBury, Adam Marcheluk, Konrad Talasiewicz, Krzysztof Tupikowski, Renata Zaucha, Bogdan Zurawski, Pedro Madeira, Andre Mansinho, Nuno Vau, Anna Alyasova, Victoria Chistyakova, Denis Khvorostenko, Dmitry Kirtbaya, Gennady Kolesnikov, Evgeny Kopyltsov, Igor Lifirenko, Alexander Lykov, Konstantin Penkov, Andrey Semenov, Mikhail Shkolnik, Pavel Skopin, Roman Smirnov, Evgeny Usynin, Sergey Varlamov, Vladimir Vladimirov, Teresa Alonso, Sara Breijo, Elena Castro, Enrique Gallardo, Jose Gutierrez Banos, Alvaro Juarez, Rebeca Lozano, Pablo Maroto, Javier Puente, Alejo Rodriguez-Vida, Regina Girones, Begona Mellado, Enrique Castellanos, Chunde Li, Chao-Hsiang Chang, Hsiao-Jen Chung, Kuan-Hua Huang, Yen-Chuan Ou, Yu-Chieh Tsai, Shian-Shiang Wang, Wen-Jeng Wu, See Tong Pang, Cagatay Arslan, Devrim Cabuk, Hasan Coskun, Mahmut Gumus, Mustafa Ozguroglu, Berna Oksuzoglu, Berksoy Sahin, Deniz Tural, Bulent Yalcin, Irfan Cicin, Igor Bondarenko, Yaroslav Gotsuliak, Yevhen Hotko, Gennadii Khareba, Oleksandr Lychkovskyy, Iryna Lytvyn, Taron Nalbandyan, Viktor Paramonov, Valerii Sakalo, Eduard Stakhovsky, Viktor Stus, Sunil Babu, Alan Bryce, David Cahn, Herta Chao, Franklin Chu, Curtis Dunshee, Oscar Goodman, Michael Grable, Jason Hafron, Joelle Hamilton, Ralph Hauke, Joseph Maly, David Morris, Gregg Newman, Patrick Pilie, Neal Shore, Paul Sieber, Matthew Smith, Andrew Trainer, and Ronald Tutrone. Niraparib and abiraterone acetate for metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 41:3339-3351, Jun 2023. URL: https://doi.org/10.1200/jco.22.01649, doi:10.1200/jco.22.01649. This article has 380 citations and is from a highest quality peer-reviewed journal.

21. (chi2023detectionofbrca1 pages 2-4): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

22. (fettke2023brcadeficientmetastaticprostate pages 7-8): Heidi Fettke, Chao Dai, Edmond M. Kwan, Tiantian Zheng, Pan Du, Nicole Ng, Patricia Bukczynska, Maria Docanto, Louise Kostos, Siavash Foroughi, Stephen Brown, Lisa-Jane K. Graham, Kate Mahon, Lisa G. Horvath, Shidong Jia, Manish Kohli, and Arun A. Azad. Brca-deficient metastatic prostate cancer has an adverse prognosis and distinct genomic phenotype. eBioMedicine, 95:104738, Sep 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104738, doi:10.1016/j.ebiom.2023.104738. This article has 41 citations and is from a peer-reviewed journal.

23. (fettke2023brcadeficientmetastaticprostate pages 8-10): Heidi Fettke, Chao Dai, Edmond M. Kwan, Tiantian Zheng, Pan Du, Nicole Ng, Patricia Bukczynska, Maria Docanto, Louise Kostos, Siavash Foroughi, Stephen Brown, Lisa-Jane K. Graham, Kate Mahon, Lisa G. Horvath, Shidong Jia, Manish Kohli, and Arun A. Azad. Brca-deficient metastatic prostate cancer has an adverse prognosis and distinct genomic phenotype. eBioMedicine, 95:104738, Sep 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104738, doi:10.1016/j.ebiom.2023.104738. This article has 41 citations and is from a peer-reviewed journal.

24. (cheng2024brca1brca2and pages 1-3): Heather H. Cheng, Jeffrey W. Shevach, Elena Castro, Fergus J. Couch, Susan M. Domchek, Rosalind A. Eeles, Veda N. Giri, Michael J. Hall, Mary-Claire King, Daniel W. Lin, Stacy Loeb, Todd M. Morgan, Kenneth Offit, Colin C. Pritchard, Edward M. Schaeffer, Brittany M. Szymaniak, Jason L. Vassy, Bryson W. Katona, and Kara N. Maxwell. <i>brca1, brca2</i>, and associated cancer risks and management for male patients. JAMA Oncology, 10:1272, Sep 2024. URL: https://doi.org/10.1001/jamaoncol.2024.2185, doi:10.1001/jamaoncol.2024.2185. This article has 40 citations and is from a highest quality peer-reviewed journal.

25. (chi2023detectionofbrca1 pages 2-2): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

26. (chi2023detectionofbrca1 pages 6-8): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

27. (chi2023detectionofbrca1 pages 4-5): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

28. (chi2023detectionofbrca1 pages 5-6): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

29. (matsubara2023olaparibefficacyin pages 5-6): N. Matsubara, J. D. de Bono, D. Olmos, G. Procopio, S. Kawakami, Y. Ürün, R. van Alphen, A. Fléchon, M. Carducci, Y. Choi, S. Hotte, Ernesto Korbenfeld, G. Kramer, N. Agarwal, K. Chi, S. Dearden, C. Gresty, Jinyu Kang, C. Poehlein, E. Harrington, and M. Hussain. Olaparib efficacy in patients with metastatic castration-resistant prostate cancer and brca1, brca2, or atm alterations identified by testing circulating tumor dna. Clinical Cancer Research, 29:92-99, Nov 2023. URL: https://doi.org/10.1158/1078-0432.ccr-21-3577, doi:10.1158/1078-0432.ccr-21-3577. This article has 48 citations and is from a highest quality peer-reviewed journal.

30. (chi2023detectionofbrca1 media 1d7942c2): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

31. (chi2023detectionofbrca1 media 19a57459): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

32. (chi2023detectionofbrca1 media c50e82d1): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

33. (chi2023detectionofbrca1 media 89bfe680): Kim N. Chi, Alan Barnicle, Caroline Sibilla, Zhongwu Lai, Claire Corcoran, J. Carl Barrett, Carrie A. Adelman, Ping Qiu, Ashley Easter, Simon Dearden, Geoffrey R. Oxnard, Neeraj Agarwal, Arun Azad, Johann de Bono, Joaquin Mateo, David Olmos, Antoine Thiery-Vuillemin, and Elizabeth A. Harrington. Detection of brca1, brca2, and atm alterations in matched tumor tissue and circulating tumor dna in patients with prostate cancer screened in profound. Clinical Cancer Research, 29:81-91, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-0931, doi:10.1158/1078-0432.ccr-22-0931. This article has 79 citations and is from a highest quality peer-reviewed journal.

34. (fazekas2024magneticresonanceimaging pages 1-6): Tamás Fazekas, Sung Ryul Shim, Giuseppe Basile, Michael Baboudjian, Tamás Kói, Mikolaj Przydacz, Mohammad Abufaraj, Guillaume Ploussard, Veeru Kasivisvanathan, Juan Gómez Rivas, Giorgio Gandaglia, Tibor Szarvas, Ivo G. Schoots, Roderick C. N. van den Bergh, Michael S. Leapman, Péter Nyirády, Shahrokh F. Shariat, and Pawel Rajwa. Magnetic resonance imaging in prostate cancer screening. JAMA Oncology, 10:745, Jun 2024. URL: https://doi.org/10.1001/jamaoncol.2024.0734, doi:10.1001/jamaoncol.2024.0734. This article has 95 citations and is from a highest quality peer-reviewed journal.

35. (fazekas2024magneticresonanceimaging pages 21-25): Tamás Fazekas, Sung Ryul Shim, Giuseppe Basile, Michael Baboudjian, Tamás Kói, Mikolaj Przydacz, Mohammad Abufaraj, Guillaume Ploussard, Veeru Kasivisvanathan, Juan Gómez Rivas, Giorgio Gandaglia, Tibor Szarvas, Ivo G. Schoots, Roderick C. N. van den Bergh, Michael S. Leapman, Péter Nyirády, Shahrokh F. Shariat, and Pawel Rajwa. Magnetic resonance imaging in prostate cancer screening. JAMA Oncology, 10:745, Jun 2024. URL: https://doi.org/10.1001/jamaoncol.2024.0734, doi:10.1001/jamaoncol.2024.0734. This article has 95 citations and is from a highest quality peer-reviewed journal.

36. (turnham2024developmentandcharacterisation pages 1-2): Daniel J. Turnham, Manisha S. Mullen, Nicholas P. Bullock, Kathryn L. Gilroy, Anna E. Richards, Radhika Patel, Marcos Quintela, Valerie S. Meniel, Gillian Seaton, Howard Kynaston, Richard W. E. Clarkson, Toby J. Phesse, Peter S. Nelson, Michael C. Haffner, John N. Staffurth, and Helen B. Pearson. Development and characterisation of a new patient-derived xenograft model of ar-negative metastatic castration-resistant prostate cancer. Cells, 13:673, Apr 2024. URL: https://doi.org/10.3390/cells13080673, doi:10.3390/cells13080673. This article has 2 citations.

37. (mateo2024olaparibforthe pages 4-5): Joaquin Mateo, Johann S. de Bono, Karim Fizazi, Fred Saad, Neal Shore, Shahneen Sandhu, Kim N. Chi, Neeraj Agarwal, David Olmos, Antoine Thiery-Vuillemin, Mustafa Özgüroğlu, Niven Mehra, Nobuaki Matsubara, Jae Young Joung, Charles Padua, Ernesto Korbenfeld, Jinyu Kang, Helen Marshall, Zhongwu Lai, Alan Barnicle, Christian Poehlein, Natalia Lukashchuk, and Maha Hussain. Olaparib for the treatment of patients with metastatic castration-resistant prostate cancer and alterations in <i>brca1</i> and/or <i>brca2</i> in the profound trial. Journal of Clinical Oncology, 42:571-583, Feb 2024. URL: https://doi.org/10.1200/jco.23.00339, doi:10.1200/jco.23.00339. This article has 91 citations and is from a highest quality peer-reviewed journal.

38. (heiss2024usfoodand pages 1-2): Brian L. Heiss, Elaine Chang, Xin Gao, Tien Truong, Michael H. Brave, Erik Bloomquist, Ankit Shah, Salaheldin Hamed, Jeffrey Kraft, Haw-Jyh Chiu, Tiffany K. Ricks, Amy Tilley, William F. Pierce, Liuya Tang, Abdelrahmman Abukhdeir, Shyam Kalavar, Reena Philip, Shenghui Tang, Richard Pazdur, Laleh Amiri-Kordestani, Paul G. Kluetz, and Daniel L. Suzman. Us food and drug administration approval summary: talazoparib in combination with enzalutamide for treatment of patients with homologous recombination repair gene-mutated metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 42:1851-1860, May 2024. URL: https://doi.org/10.1200/jco.23.02182, doi:10.1200/jco.23.02182. This article has 29 citations and is from a highest quality peer-reviewed journal.

39. (mateo2024olaparibforthe pages 6-8): Joaquin Mateo, Johann S. de Bono, Karim Fizazi, Fred Saad, Neal Shore, Shahneen Sandhu, Kim N. Chi, Neeraj Agarwal, David Olmos, Antoine Thiery-Vuillemin, Mustafa Özgüroğlu, Niven Mehra, Nobuaki Matsubara, Jae Young Joung, Charles Padua, Ernesto Korbenfeld, Jinyu Kang, Helen Marshall, Zhongwu Lai, Alan Barnicle, Christian Poehlein, Natalia Lukashchuk, and Maha Hussain. Olaparib for the treatment of patients with metastatic castration-resistant prostate cancer and alterations in <i>brca1</i> and/or <i>brca2</i> in the profound trial. Journal of Clinical Oncology, 42:571-583, Feb 2024. URL: https://doi.org/10.1200/jco.23.00339, doi:10.1200/jco.23.00339. This article has 91 citations and is from a highest quality peer-reviewed journal.

40. (chi2023niraparibandabiraterone pages 3-4): Kim N. Chi, Dana Rathkopf, Matthew R. Smith, Eleni Efstathiou, Gerhardt Attard, David Olmos, Ji Youl Lee, Eric J. Small, Andrea J. Pereira de Santana Gomes, Guilhem Roubaud, Marniza Saad, Bogdan Zurawski, Valerii Sakalo, Gary E. Mason, Peter Francis, George Wang, Daphne Wu, Brooke Diorio, Angela Lopez-Gitlitz, Shahneen Sandhu, Maria Alvarez, Gabriela Gatica, Martin Greco, Ernesto Korbenfeld, Esteban Metrebian, Jorge Salinas, Alejandro Salvatierra, Marcelo Tatangelo, Tom Ferguson, Howard Gurney, Elizabeth Hovey, Anthony Joshua, Matos Marco, Gavin Marx, Michelle Morris, Siobhan Ng, David Pook, Shahneen Sandhu, Ali Tafreshi, Thean Hsiang Tan, Tsvetanka Tosheva, Livia Andrade, Felipe Cruz, Luiza Faria, Jose Figueiredo, Fabio Franke, Andrea Juliana Gomes, Ariel Kann, Celio Kussumoto, Suelen Martins, Andre Murad, Helio Pinczowski, Giovani Pioner, Luis Pires, Daniel Preto, Gisele Santos, Eduardo Silva, Jamile Silva, Luciano Viana, Karina Vianna, Adriano Paula, Zhiwen Chen, Kim Chi, Urban Emmenegger, Neil Fleshner, Sunil Parimi, Fred Saad, Francisco Vera-Badillo, Hongqian Guo, Hong Luo, Lulin Ma, Mingxing Qui, Wei Xue, Guo Yonglian, Lei Li, Jinxian Pu, Song Zheng, Qing Zou, Milos Brodak, Milan Hora, Vladimir Samal, Vladimir Student, Jaroslav Vanasek, Emmanuelle Bompas, Philippe Barthelemy, Delphine Borchiellini, Aude Flechon, Hakim Mahammedi, Guilhem Roubaud, Antoine Thiery-Vuillemin, Diego Tosi, Spaeth Dominique, Carole Helissey, Martin Boegemann, Susan Feyerabend, Eva Hellmis, Martin Schostak, Gerhardt Attard, Anna Lydon, Ian Sayers, Omi Parikh, Duncan Wheatley, Peter Arkosy, Jozsef Erfan, Lajos Geczi, Peter Nyirady, Judit Olah, Istvan Papos, Bela Piko, Raanan Berger, Avivit Peer, Umberto Basso, Sergio Bracarda, Orazio Caffo, Francesco Carrozza, Gianluca Del Conte, Luca Galli, Donatello Gasparro, Sandro Pignata, Riccardo Ricotta, Daniele Santini, Giampaolo Tortora, Seoksoo Byun, SeolHo Choo, ByungHa Chung, Jaeyoung Joung, Wonho Jung, Taek Won Kang, Cheol Kwak, TaeGyun Kwon, Hyo Jin Lee, Ji Youl Lee, SeongIl Seo, YoungDeuk Choi, HongKoo Ha, ChoungSoo Kim, Flora Li Tze Chong, Chun Sen Lim, Vijayan Manogran, Hwoei Fen Soo Hoo, Guan Chou Teh, Marniza Saad, David Calvo Dominguez, Abraham Cardenas, Julia Saenz, Andre Bergman, Helgi Helgason, C.B. Hunting, Rik Somford, Tomasz Byrski, Tomasz Drewa, Dorota Filarska, Jolanta LuniewskaBury, Adam Marcheluk, Konrad Talasiewicz, Krzysztof Tupikowski, Renata Zaucha, Bogdan Zurawski, Pedro Madeira, Andre Mansinho, Nuno Vau, Anna Alyasova, Victoria Chistyakova, Denis Khvorostenko, Dmitry Kirtbaya, Gennady Kolesnikov, Evgeny Kopyltsov, Igor Lifirenko, Alexander Lykov, Konstantin Penkov, Andrey Semenov, Mikhail Shkolnik, Pavel Skopin, Roman Smirnov, Evgeny Usynin, Sergey Varlamov, Vladimir Vladimirov, Teresa Alonso, Sara Breijo, Elena Castro, Enrique Gallardo, Jose Gutierrez Banos, Alvaro Juarez, Rebeca Lozano, Pablo Maroto, Javier Puente, Alejo Rodriguez-Vida, Regina Girones, Begona Mellado, Enrique Castellanos, Chunde Li, Chao-Hsiang Chang, Hsiao-Jen Chung, Kuan-Hua Huang, Yen-Chuan Ou, Yu-Chieh Tsai, Shian-Shiang Wang, Wen-Jeng Wu, See Tong Pang, Cagatay Arslan, Devrim Cabuk, Hasan Coskun, Mahmut Gumus, Mustafa Ozguroglu, Berna Oksuzoglu, Berksoy Sahin, Deniz Tural, Bulent Yalcin, Irfan Cicin, Igor Bondarenko, Yaroslav Gotsuliak, Yevhen Hotko, Gennadii Khareba, Oleksandr Lychkovskyy, Iryna Lytvyn, Taron Nalbandyan, Viktor Paramonov, Valerii Sakalo, Eduard Stakhovsky, Viktor Stus, Sunil Babu, Alan Bryce, David Cahn, Herta Chao, Franklin Chu, Curtis Dunshee, Oscar Goodman, Michael Grable, Jason Hafron, Joelle Hamilton, Ralph Hauke, Joseph Maly, David Morris, Gregg Newman, Patrick Pilie, Neal Shore, Paul Sieber, Matthew Smith, Andrew Trainer, and Ronald Tutrone. Niraparib and abiraterone acetate for metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 41:3339-3351, Jun 2023. URL: https://doi.org/10.1200/jco.22.01649, doi:10.1200/jco.22.01649. This article has 380 citations and is from a highest quality peer-reviewed journal.

41. (fizazi2024firstlinetalazoparibwith pages 5-5): Karim Fizazi, Arun A. Azad, Nobuaki Matsubara, Joan Carles, Andre P. Fay, Ugo De Giorgi, Jae Young Joung, Peter C. C. Fong, Eric Voog, Robert J. Jones, Neal D. Shore, Curtis Dunshee, Stefanie Zschäbitz, Jan Oldenburg, Dingwei Ye, Xun Lin, Cynthia G. Healy, Nicola Di Santo, A. Douglas Laird, Fabian Zohren, and Neeraj Agarwal. First-line talazoparib with enzalutamide in hrr-deficient metastatic castration-resistant prostate cancer: the phase 3 talapro-2 trial. Nature Medicine, 30:257-264, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02704-x, doi:10.1038/s41591-023-02704-x. This article has 152 citations and is from a highest quality peer-reviewed journal.

42. (fazekas2024magneticresonanceimaging pages 10-13): Tamás Fazekas, Sung Ryul Shim, Giuseppe Basile, Michael Baboudjian, Tamás Kói, Mikolaj Przydacz, Mohammad Abufaraj, Guillaume Ploussard, Veeru Kasivisvanathan, Juan Gómez Rivas, Giorgio Gandaglia, Tibor Szarvas, Ivo G. Schoots, Roderick C. N. van den Bergh, Michael S. Leapman, Péter Nyirády, Shahrokh F. Shariat, and Pawel Rajwa. Magnetic resonance imaging in prostate cancer screening. JAMA Oncology, 10:745, Jun 2024. URL: https://doi.org/10.1001/jamaoncol.2024.0734, doi:10.1001/jamaoncol.2024.0734. This article has 95 citations and is from a highest quality peer-reviewed journal.

43. (kulkarni2024lp184anovel pages 8-9): Aditya Kulkarni, Jianli Zhou, Neha Biyani, Umesh Kathad, Partha P. Banerjee, Shiv Srivastava, Zsombor Prucsi, Kamil Solarczyk, Kishor Bhatia, Reginald B. Ewesuedo, and Panna Sharma. Lp-184, a novel acylfulvene molecule, exhibits anticancer activity against diverse solid tumors with homologous recombination deficiency. Cancer Research Communications, 4:1199-1210, May 2024. URL: https://doi.org/10.1158/2767-9764.crc-23-0554, doi:10.1158/2767-9764.crc-23-0554. This article has 5 citations and is from a peer-reviewed journal.
