---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T21:45:33.337423'
end_time: '2026-04-05T21:53:06.067235'
duration_seconds: 452.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polycythemia Vera
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Polycythemia Vera
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Polycythemia Vera** covering all of the
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
- **Disease Name:** Polycythemia Vera
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Polycythemia Vera** covering all of the
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


# Polycythemia Vera (PV) — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Polycythemia vera (PV) (tefferi2023polycythemiavera2024 pages 2-2)
- **Category:** BCR::ABL1 (Philadelphia chromosome)–negative myeloproliferative neoplasm (MPN) (silver2023polycythemiaveraaspects pages 1-3, tefferi2023polycythemiavera2024 pages 2-2)
- **MONDO / OMIM / Orphanet / MeSH / ICD identifiers:** Not retrievable from the current evidence set captured with the available tools; therefore not asserted here.

## Executive overview (current understanding)
Polycythemia vera is a chronic, clonal, Philadelphia chromosome–negative MPN characterized by **clonal erythrocytosis**, frequently accompanied by leukocytosis, thrombocytosis, splenomegaly, pruritus, microcirculatory symptoms, and a **markedly increased risk of arterial/venous thrombosis**, with potential progression to post-PV myelofibrosis or acute myeloid leukemia (AML) (silver2023polycythemiaveraaspects pages 1-3, tefferi2023polycythemiavera2024 pages 2-2). Driver genetics are dominated by **JAK2 mutations** (JAK2V617F in ~97%; other JAK2 mutations including exon 12 in ~3%) (tefferi2023polycythemiavera2024 pages 2-2).

---

## 1. Disease Information
### Definition and classification
- PV is described as a **JAK2-mutated myeloproliferative neoplasm characterized by clonal erythrocytosis** (tefferi2023polycythemiavera2024 pages 2-2).
- Expert clinical framing emphasizes that PV is “defined as a Philadelphia chromosome–negative MPN driven almost universally by JAK2 mutations” and that diagnostic confirmation relies on careful interpretation of red cell parameters and bone marrow morphology (silver2023polycythemiaveraaspects pages 1-3).

### Common synonyms / alternative names
The evidence set supports “polycythemia vera” and “PV” as the primary naming; additional synonyms (e.g., “polycythaemia vera”) are not explicitly enumerated in the extracted texts.

### Evidence provenance note (aggregated vs individual-level)
This report is derived primarily from:
- **Aggregated guideline/review sources** (e.g., *American Journal of Hematology* 2024 update; national recommendations) (tefferi2023polycythemiavera2024 pages 2-2, goratybor2024recommendationsofpolish pages 2-3).
- **Randomized trials** (e.g., MAJIC-PV; Low-PV; REVIVE) (harrison2023ruxolitinibversusbest pages 1-2, barbui2023ropeginterferonversusstandard pages 1-2, kremyanskaya2024rusfertideahepcidin pages 1-2).
- **Real-world evidence / claims and EHR analyses** (US claims; PV-NET; PV-AIM) (verstovsek2023realworldtreatmentsand pages 1-2, palandri2023predictorsofresponse pages 2-3).

---

## 2. Etiology
### Primary causal factors
**Somatic clonal hematopoiesis driven by activating JAK2 mutations** is central: JAK2V617F is present in ~97% of cases; ~3% have other JAK2 mutations including exon 12 (tefferi2023polycythemiavera2024 pages 2-2). Constitutive JAK/STAT activation is repeatedly emphasized as core biology underlying PV manifestations and complications (harrison2023ruxolitinibversusbest pages 1-2).

### Genetic risk factors / susceptibility loci (recent)
A 2023 genetic association study explicitly links **iron regulation genetics (HFE)** to PV diagnosis:
- UK Biobank GWAS: **440 PV cases vs 403,351 controls**; SNPs in **HFE** (known hemochromatosis variants) were “highly associated with PV diagnosis,” and FinnGen independently confirmed over-representation of homozygous HFE mutations in PV (bennett2023ironhomeostasisgoverns pages 1-7).

### Environmental and clinical risk modifiers (evidence available)
- Cardiovascular risk factors (e.g., hypertension, dyslipidemia, obesity, smoking) are highlighted as relevant modifiers of overall thrombotic/cardiovascular risk in PV-focused reviews (verstovsek2023realworldtreatmentsand pages 1-2, silver2023polycythemiaveraaspects pages 1-3).
- Direct environmental exposures are not quantified in the captured evidence set.

### Protective factors
- No definitive protective genetic variants are established in the retrieved evidence.
- Secondary prevention strategies (tight hematocrit control, antiplatelet therapy, cardiovascular risk modification) are repeatedly positioned as protective against thrombotic events (verstovsek2023realworldtreatmentsand pages 1-2, barbui2023ropeginterferonversusstandard pages 1-2).

### Gene–environment / gene–physiology interaction (supported example)
PV phenotype appears to interact strongly with systemic iron biology:
- Venesection-induced iron restriction is common, and **hepcidin biology modifies disease severity** in JAK2V617F PV mouse models (hepcidin upregulation alleviates; hepcidin loss worsens), implying that genetic/physiologic regulation of iron handling can modify PV expression (bennett2023ironhomeostasisgoverns pages 1-7).

---

## 3. Phenotypes
### Core clinical phenotype spectrum (with frequencies where available)
From a large 2023 disease update, at/before presentation PV is associated with (examples below):
- **Palpable splenomegaly:** ~36% (tefferi2023polycythemiavera2024 pages 2-2)
- **Prior thrombosis:** ~25% (arterial 15–16%; venous 8–13%) (tefferi2023polycythemiavera2024 pages 2-2)
- **Major hemorrhage:** ~4% (tefferi2023polycythemiavera2024 pages 2-2)
- **Symptoms/microvascular disturbances:** headache, visual disturbances, erythromelalgia, pruritus, splenomegaly discomfort; presentations vary from asymptomatic to thrombotic/bleeding events (tefferi2023polycythemiavera2024 pages 2-2)

A separate expert review notes splenomegaly in a minority in a specific cohort (≈27% any; 6% >5 cm in one series), illustrating variability by cohort/definition (silver2023polycythemiaveraaspects pages 1-3).

### Quality of life (QoL) impact (recent)
A 2024 review focused on low-risk PV reports substantial QoL impact:
- ~**80%** report disease-related QoL impact; fatigue and sleep problems up to **79%**; symptoms can include pruritus, pica, cognitive issues, falls, and poor exercise tolerance (visweshwar2024impactofphlebotomy pages 8-10).
- Phlebotomy itself negatively affects QoL for many low-risk patients; ~**25%** reported negative QoL impact and up to **8%** discontinued phlebotomy in one cited analysis (visweshwar2024impactofphlebotomy pages 8-10).

### Suggested HPO terms (curated suggestions)
(*Ontology mappings are suggested based on reported clinical features; the specific HPO IDs are not present in the evidence set and are therefore proposed as likely matches.*)
- Thrombosis (e.g., venous thrombosis; arterial thrombosis)
- Pruritus
- Splenomegaly
- Headache
- Erythromelalgia / microvascular disturbances
- Leukocytosis, thrombocytosis, erythrocytosis / elevated hematocrit
- Fatigue

---

## 4. Genetic / Molecular Information
### Causal genes and mutation frequencies
- **JAK2**: driver mutation JAK2V617F in ~**97%**; other JAK2 mutations including exon 12 in ~**3%** (tefferi2023polycythemiavera2024 pages 2-2).

### Additional (non-driver) mutations and prognostic genomics
Both a 2023 update and 2024 recommendations summarize frequent co-mutations:
- Common: **TET2 ~18%**, **ASXL1 ~15%**, **LNK ~3%** (tefferi2023polycythemiavera2024 pages 7-8, goratybor2024recommendationsofpolish pages 2-3).
- Adverse mutation sets (examples include **SRSF2, IDH2, RUNX1, U2AF1**) occur in a minority and are used in prognostic modeling (goratybor2024recommendationsofpolish pages 2-3, tefferi2023polycythemiavera2024 pages 7-8).

### Somatic vs germline
- PV driver mutations and most co-mutations are treated as **somatic** clonal hematopoiesis features in the reviewed clinical literature (tefferi2023polycythemiavera2024 pages 2-2, harrison2023ruxolitinibversusbest pages 1-2).
- Germline susceptibility is suggested by the **HFE-associated GWAS** signal (bennett2023ironhomeostasisgoverns pages 1-7).

### Functional consequences (high-level)
- JAK2 mutations lead to **constitutive JAK-STAT activation** with downstream inflammatory signaling and clinical complications (harrison2023ruxolitinibversusbest pages 1-2).

### Epigenetics / chromosomal abnormalities
- Cytogenetic abnormalities are reported in ~**15%** (examples: trisomy 8/9; del13q; del20q), and marrow fibrosis is present in ~**20% at diagnosis** in one recommendation summary (goratybor2024recommendationsofpolish pages 2-3).

---

## 5. Environmental Information
Robust, specific environmental exposures (toxins/radiation) were not captured in the retrieved evidence. Cardiovascular comorbidity burden is consistently emphasized as clinically relevant to outcomes and management (verstovsek2023realworldtreatmentsand pages 1-2, silver2023polycythemiaveraaspects pages 1-3).

---

## 6. Mechanism / Pathophysiology
### Central pathway: JAK–STAT–driven clonal myeloproliferation
- PV is mechanistically tied to JAK2-driven JAK/STAT signaling (tefferi2023polycythemiavera2024 pages 2-2, harrison2023ruxolitinibversusbest pages 1-2).

### Thrombosis and “thrombo-inflammation” (recent mechanistic emphasis)
- Thrombosis is a dominant clinical problem; chronic inflammation and innate immune activation are repeatedly highlighted as contributors to vascular risk in PV/MPNs (verstovsek2023realworldtreatmentsand pages 1-2, barbui2026preservingthrombosisand pages 13-15).

### Iron–hepcidin axis as a disease modifier (2023–2024 developments)
- 2023 GWAS and mouse genetic dissection link PV phenotype to **hepcidin-regulated iron homeostasis**: endogenous hepcidin upregulation alleviates erythroid disease; hepcidin ablation worsens it in JAK2V617F PV mouse models (bennett2023ironhomeostasisgoverns pages 1-7).
- Proposed mechanism includes **inflammatory cytokine signaling via GP130-coupled receptors** influencing hepcidin regulation in PV (bennett2023ironhomeostasisgoverns pages 1-7).

### NETs and inflammatory biomarkers
- In PV, neutrophil activation and NET biology are implicated in thrombosis risk; a 2026 commentary frames NETs as repeatedly linked to thrombosis/atherosclerosis in MPNs and notes associations between leukocytosis/NLR and thrombosis (barbui2026preservingthrombosisand pages 13-15).

### Suggested GO biological process terms (curated suggestions)
(*Suggested based on described mechanisms; GO IDs not present in evidence set.*)
- JAK-STAT cascade
- Cytokine-mediated signaling pathway
- Regulation of iron ion homeostasis / hepcidin-mediated signaling
- Blood coagulation / thrombus formation
- Inflammatory response
- Neutrophil activation and degranulation; NET formation

### Suggested CL cell types (curated suggestions)
(*Suggested based on described mechanisms; CL IDs not present in evidence set.*)
- Hematopoietic stem and progenitor cells
- Erythroid progenitors
- Megakaryocytes/platelets
- Neutrophils
- Endothelial cells

---

## 7. Anatomical Structures Affected
- **Primary site:** bone marrow (clonal myeloproliferation) (silver2023polycythemiaveraaspects pages 1-3).
- **Secondary sites / complications:** spleen (splenomegaly), arterial/venous vasculature (thrombosis, hemorrhage), and systemic involvement via inflammatory cytokines and cardiovascular risk (tefferi2023polycythemiavera2024 pages 2-2, verstovsek2023realworldtreatmentsand pages 1-2).

Suggested UBERON (curated): bone marrow, spleen, blood, vascular endothelium.

---

## 8. Temporal Development
- Typical **median age at diagnosis ~61 years**; ~10% diagnosed <40; sex distribution approximately equal (tefferi2023polycythemiavera2024 pages 2-2).
- PV is chronic with long survival measured in years to decades, but complicated by thrombosis and possible progression to post-PV myelofibrosis or AML (tefferi2023polycythemiavera2024 pages 2-2, verstovsek2023realworldtreatmentsand pages 1-2).

---

## 9. Inheritance and Population
### Epidemiology (recent)
- Sweden (2000–2014): age-standardized PV incidence **1.48 per 100,000 person-years** (tefferi2023polycythemiavera2024 pages 2-2).
- USA prevalence estimate **45–57 per 100,000** (verstovsek2023realworldtreatmentsand pages 1-2).

### Demographics
- Median age ~61; ~10% <40; sex ~1:1 (tefferi2023polycythemiavera2024 pages 2-2).

### Inheritance
PV is primarily a **sporadic somatic clonal disorder** (JAK2-driven), although germline susceptibility loci (e.g., HFE variants influencing iron regulation) may modify risk (tefferi2023polycythemiavera2024 pages 2-2, bennett2023ironhomeostasisgoverns pages 1-7).

---

## 10. Diagnostics
### Standard diagnostic criteria (WHO 2022; ICC nuance)
A 2024 recommendation summarizing WHO 2022 states erythrocytosis thresholds:
- **Hb >16.5 g/dL (men), >16.0 g/dL (women)** or **Hct >49% (men), >48% (women)** (goratybor2024recommendationsofpolish pages 2-3).
- Bone marrow trephine showing panmyelosis is a WHO major criterion (goratybor2024recommendationsofpolish pages 2-3).
- ICC allows omission of bone marrow in selected cases with very high Hb/Hct plus JAK2 mutation and low EPO (goratybor2024recommendationsofpolish pages 2-3).

### Biomarkers and testing strategy (practical summary)
- **JAK2 mutation testing** (V617F; exon 12 if V617F-negative) is central (tefferi2023polycythemiavera2024 pages 2-2).
- **Serum EPO**: “low EPO” is emphasized in WHO/ICC frameworks (goratybor2024recommendationsofpolish pages 2-3).
- Consider expanded **NGS** to detect additional variants for prognosis (not mandatory universally) (tefferi2023polycythemiavera2024 pages 7-8).

### Risk stratification used clinically
- Low-risk vs high-risk is commonly defined by age <60 and no thrombosis vs age ≥60 and/or prior thrombosis (verstovsek2023realworldtreatmentsand pages 1-2).

---

## 11. Outcome / Prognosis
### Survival and major outcome drivers
- Real-world/guideline summaries report **median survival ~12.4–20 years** (range reflects cohorts/methods) (verstovsek2023realworldtreatmentsand pages 1-2).
- Thrombotic complications remain a key contributor to morbidity/mortality (verstovsek2023realworldtreatmentsand pages 1-2, goratybor2024recommendationsofpolish pages 2-3).

### Prognostic modeling (clinical-genetic)
- **MIPSS-PV**: integrates clinical variables and adverse genetics; summarized median OS of **24 years (low)**, **13.1 years (intermediate)**, **3.2 years (high)** (goratybor2024recommendationsofpolish pages 2-3, tefferi2023polycythemiavera2024 pages 7-8).
- In MAJIC-PV, **ASXL1 mutations** predicted adverse event-free survival (HR 3.02) (harrison2023ruxolitinibversusbest pages 1-2).

---

## 12. Treatment
### Treatment goals (core concept)
Prevent thrombosis and manage symptom burden by maintaining **hematocrit <45%** and controlling blood counts and cardiovascular risk factors (verstovsek2023realworldtreatmentsand pages 1-2, barbui2023ropeginterferonversusstandard pages 1-2).

### Standard therapies and real-world implementation
- **Phlebotomy + low-dose aspirin** is common initial therapy, especially in low-risk PV (verstovsek2023realworldtreatmentsand pages 1-2, barbui2023ropeginterferonversusstandard pages 1-2).
- Real-world US claims data show frequent underuse/undertitration in practice: among 28,306 PV patients, many remained on phlebotomy monotherapy and hematocrit control was often suboptimal (verstovsek2023realworldtreatmentsand pages 1-2).

### Cytoreduction
#### Hydroxyurea (HU)
- PV-NET real-world cohort (n=563 on HU ≥12 months): **29.5%** achieved ELN complete response; many patients were underdosed, and splenomegaly/symptoms often drove switching (palandri2023predictorsofresponse pages 2-3).

#### Interferon / ropeginterferon alfa-2b (2023–2024 evidence)
- Low-risk randomized phase 2 **Low-PV** trial: primary endpoint met in **81%** with ropeginterferon vs **51%** standard; maintained response at 24 months **83% vs 59%**; improved symptom/spleen outcomes but discontinuations for adverse events occurred (barbui2023ropeginterferonversusstandard pages 1-2).

#### JAK inhibitor: ruxolitinib
- **MAJIC-PV** randomized phase II (HU-intolerant/resistant high-risk PV; n=180): complete response **43% vs 26%** (ruxolitinib vs BAT), improved CR duration (HR 0.38), improved EFS (HR 0.58), and molecular response associated with improved PFS/EFS/OS; ASXL1 predicted worse EFS (harrison2023ruxolitinibversusbest pages 1-2).
- In previously untreated PV (RuxoBEAT futility analysis; n=28), ruxolitinib reduced hematocrit and phlebotomy needs and improved pruritus scores, with only grade 1–3 adverse events reported in this small cohort (koschmieder2023efficacyandsafety pages 1-2).

### Emerging / novel therapies (2023–2024 priority)
#### Hepcidin mimetic: rusfertide
- **REVIVE (NCT04057040), NEJM 2024**: phlebotomies decreased from **8.7/year to 0.6/year** during part 1; mean maximum hematocrit **44.5% vs 50.0%** pre-treatment; randomized withdrawal response **60% vs 17%** (rusfertide vs placebo; P=0.002); grade 3 adverse events **13%**, no grade 4/5 events (kremyanskaya2024rusfertideahepcidin pages 1-2).
- Review synthesis emphasizes rusfertide as a candidate “chemical phlebotomy” approach and notes high rates of phlebotomy independence in phase 2 reporting; phase 3 is underway (handa2023hepcidinmimeticsin pages 4-6, handa2023hepcidinmimeticsin pages 13-15).

### Suggested MAXO terms (curated suggestions)
(*MAXO IDs not present in evidence set; suggested as likely actions*)
- Therapeutic phlebotomy
- Antiplatelet therapy (aspirin)
- Cytoreductive therapy (hydroxyurea; interferon)
- Janus kinase inhibitor therapy (ruxolitinib)
- Hepcidin mimetic therapy / iron restriction therapy (rusfertide)

---

## 13. Prevention
Primary prevention is not established (somatic clonal disorder), but **secondary/tertiary prevention** is central:
- Maintain hematocrit <45% and manage cardiovascular risk factors to prevent thrombosis (verstovsek2023realworldtreatmentsand pages 1-2, goratybor2024recommendationsofpolish pages 2-3).

---

## 14. Other Species / Natural Disease
No naturally occurring PV analogue in non-human species was captured in the current evidence set.

---

## 15. Model Organisms
### Mouse models (mechanistic utility)
- JAK2V617F PV mouse models are used to dissect phenotype modifiers; notably, **hepcidin upregulation alleviates** and **hepcidin loss worsens** erythroid disease in these models, supporting iron-homeostasis targeting (bennett2023ironhomeostasisgoverns pages 1-7).

---

## Recent developments and real-world applications (2023–2024 highlights)
1. **Hepcidin/iron axis as a therapeutic and etiologic lever:** 2023 GWAS and mouse genetics support iron regulation as a modifier of PV phenotype (bennett2023ironhomeostasisgoverns pages 1-7).
2. **Rusfertide (NEJM 2024)** provides high-quality randomized withdrawal evidence for reducing phlebotomy dependence and maintaining hematocrit control with an acceptable safety profile (kremyanskaya2024rusfertideahepcidin pages 1-2).
3. **Ruxolitinib (JCO 2023, MAJIC-PV)** demonstrates superior complete response and event-free survival vs best available therapy in HU-intolerant/resistant PV; molecular response correlates with improved outcomes and ASXL1 predicts adverse EFS (harrison2023ruxolitinibversusbest pages 1-2).
4. **Ropeginterferon alfa-2b (NEJM Evidence 2023)** shows improved hematocrit-target maintenance and symptom/spleen endpoints in low-risk PV compared to phlebotomy-based standard approaches (barbui2023ropeginterferonversusstandard pages 1-2).
5. **Real-world implementation gaps:** US claims data show many patients initiate and remain on phlebotomy monotherapy and frequently have hematocrit >50%, with 16% experiencing thrombotic events after treatment initiation (verstovsek2023realworldtreatmentsand pages 1-2).

---

## Summary evidence table
The following table consolidates key identifiers, statistics, and major trial outcomes used throughout this report.

| Domain | Key facts/data | Source (PMID if present; otherwise DOI/journal) | Publication date | URL |
|---|---|---|---|---|
| Disease overview / classification | Polycythemia vera (PV) is a JAK2-mutated myeloproliferative neoplasm characterized by clonal erythrocytosis; other features include leukocytosis, thrombocytosis, splenomegaly, pruritus, microcirculatory symptoms, thrombosis risk, and progression to post-PV myelofibrosis or AML (tefferi2023polycythemiavera2024 pages 2-2, silver2023polycythemiaveraaspects pages 1-3) | DOI: 10.1002/ajh.27002; *Am J Hematol* / DOI: 10.1080/17474086.2023.2198698; *Expert Rev Hematol* | 2023-06 / 2023-04 | https://doi.org/10.1002/ajh.27002 ; https://doi.org/10.1080/17474086.2023.2198698 |
| Epidemiology | Sweden population-based age-standardized incidence: **1.48 per 100,000 person-years** for PV (2000–2014) (tefferi2023polycythemiavera2024 pages 2-2) | DOI: 10.1002/ajh.27002; *Am J Hematol* | 2023-06 | https://doi.org/10.1002/ajh.27002 |
| Epidemiology | US prevalence estimate: **45–57 per 100,000** (verstovsek2023realworldtreatmentsand pages 1-2) | DOI: 10.1007/s00277-023-05089-6; *Ann Hematol* | 2023-01 | https://doi.org/10.1007/s00277-023-05089-6 |
| Molecular drivers | **JAK2 V617F ~97%** of PV; **other JAK2 mutations including exon 12 ~3%** (tefferi2023polycythemiavera2024 pages 2-2) | DOI: 10.1002/ajh.27002; *Am J Hematol* | 2023-06 | https://doi.org/10.1002/ajh.27002 |
| Additional molecular lesions | Most frequent additional mutations: **TET2 18%, ASXL1 15%, LNK 3%**; adverse mutations (e.g., **SRSF2, IDH2, RUNX1, U2AF1**) occur in a minority and inform prognosis (goratybor2024recommendationsofpolish pages 2-3, tefferi2023polycythemiavera2024 pages 7-8) | DOI: 10.5603/ahp.102458; *Acta Haematol Pol* / DOI: 10.1002/ajh.27002; *Am J Hematol* | 2024-12 / 2023-06 | https://doi.org/10.5603/ahp.102458 ; https://doi.org/10.1002/ajh.27002 |
| Diagnostic thresholds (WHO 2022) | Major erythrocytosis threshold: **Hb >16.5 g/dL (men), >16.0 g/dL (women)** or **Hct >49% (men), >48% (women)**; bone marrow trephine with panmyelosis is a major criterion; low serum EPO is the minor criterion (goratybor2024recommendationsofpolish pages 2-3) | DOI: 10.5603/ahp.102458; *Acta Haematol Pol* | 2024-12 | https://doi.org/10.5603/ahp.102458 |
| Diagnostic nuance (ICC) | Bone marrow may be omitted in selected ICC cases with markedly elevated values: **men Hb >18.5 g/dL or Hct >55.5%; women Hb >16.5 g/dL or Hct >49.5%**, plus JAK2 mutation and low EPO (goratybor2024recommendationsofpolish pages 2-3) | DOI: 10.5603/ahp.102458; *Acta Haematol Pol* | 2024-12 | https://doi.org/10.5603/ahp.102458 |
| Risk stratification | Conventional thrombosis risk groups: **low risk = age <60 years and no prior thrombosis; high risk = age ≥60 years and/or prior thrombosis** (verstovsek2023realworldtreatmentsand pages 1-2) | DOI: 10.1007/s00277-023-05089-6; *Ann Hematol* | 2023-01 | https://doi.org/10.1007/s00277-023-05089-6 |
| Common complications at presentation | About **25%** have prior thrombosis; **36%** have palpable splenomegaly; major hemorrhage about **4%** (tefferi2023polycythemiavera2024 pages 2-2) | DOI: 10.1002/ajh.27002; *Am J Hematol* | 2023-06 | https://doi.org/10.1002/ajh.27002 |
| Hematocrit target / vascular risk | Maintaining Hct **<45%** is standard; Hct **≥45%** significantly increases vascular event/death risk (**HR 3.91**) (goratybor2024recommendationsofpolish pages 2-3, verstovsek2023realworldtreatmentsand pages 1-2) | DOI: 10.5603/ahp.102458; *Acta Haematol Pol* / DOI: 10.1007/s00277-023-05089-6; *Ann Hematol* | 2024-12 / 2023-01 | https://doi.org/10.5603/ahp.102458 ; https://doi.org/10.1007/s00277-023-05089-6 |
| Prognosis / MIPSS-PV | MIPSS-PV median overall survival: **low risk 24 years**, **intermediate risk 13.1 years**, **high risk 3.2 years**; variables include age, leukocytosis, thrombosis history/abnormal karyotype, and SRSF2 depending on model version summarized (goratybor2024recommendationsofpolish pages 2-3, tefferi2023polycythemiavera2024 pages 7-8) | DOI: 10.5603/ahp.102458; *Acta Haematol Pol* / DOI: 10.1002/ajh.27002; *Am J Hematol* | 2024-12 / 2023-06 | https://doi.org/10.5603/ahp.102458 ; https://doi.org/10.1002/ajh.27002 |
| Real-world outcomes (US claims) | Among **28,306** treated PV patients (Hct subgroup **4,246**), most initiated phlebotomy alone; Hct control was suboptimal, with **54%** of high-risk and **64%** of low-risk patients on phlebotomy monotherapy sometimes/always **>50% Hct**; **16%** had ≥1 thrombotic event after treatment initiation (**20%** high-risk, **8%** low-risk) (verstovsek2023realworldtreatmentsand pages 1-2) | DOI: 10.1007/s00277-023-05089-6; *Ann Hematol* | 2023-01 | https://doi.org/10.1007/s00277-023-05089-6 |
| Low-risk ropeginterferon trial (Low-PV) | Randomized phase 2 Low-PV trial: primary endpoint met in **81%** with ropeginterferon alfa-2b vs **51%** standard therapy; at **24 months**, maintained response **83% vs 59% (P=0.02)**; fewer moderate/severe symptoms (**33% vs 67%**) and less palpable splenomegaly (**14% vs 37%**); 7 ropeg patients discontinued for adverse events (barbui2023ropeginterferonversusstandard pages 1-2) | DOI: 10.1056/EVIDoa2200335; *NEJM Evidence* | 2023-05 | https://doi.org/10.1056/EVIDoa2200335 |
| Ropeginterferon phase 2 (rapid dosing) | Chinese phase 2 ropeginterferon alfa-2b 250–350–500 µg regimen in HU-resistant/intolerant PV: **complete hematologic response 61.2% at week 24**; JAK2 V617F allele burden declined by **17.8% ± 18.0%** by week 24; **14.3%** had reversible grade 3 drug-related AEs; no grade 4/5 AEs; no discontinuations due to AEs (kremyanskaya2024rusfertideahepcidin pages 1-2) | DOI: 10.1186/s40164-023-00415-0; *Exp Hematol Oncol* | 2023-06 | https://doi.org/10.1186/s40164-023-00415-0 |
| REVIVE rusfertide trial | REVIVE (NCT04057040): estimated phlebotomies/year fell from **8.7 ± 2.9** pre-rusfertide to **0.6 ± 1.0** during part 1; mean maximum Hct **44.5% ± 2.2** vs **50.0% ± 5.8** pre-treatment; randomized withdrawal response **60% rusfertide vs 17% placebo (P=0.002)**; grade 3 AEs **13%**, no grade 4/5 events; grade 1–2 injection-site reactions common (kremyanskaya2024rusfertideahepcidin pages 1-2) | DOI: 10.1056/NEJMoa2308809; *N Engl J Med* | 2024-02 | https://doi.org/10.1056/NEJMoa2308809 |
| Rusfertide development context | Review summary of phase 2 studies: **84%** achieved phlebotomy independence by **28 weeks** in REVIVE/PACIFIC-related reporting; phase 3 underway (**NCT05210790**) (handa2023hepcidinmimeticsin pages 4-6, handa2023hepcidinmimeticsin pages 13-15) | DOI: 10.1097/MOH.0000000000000747; *Curr Opin Hematol* | 2023-12 | https://doi.org/10.1097/MOH.0000000000000747 |
| Hydroxyurea real-world response (PV-NET) | In **563** HU-treated PV patients: **29.5%** complete response (**166/563**), **264** partial response, **133** non-response; among PR/NR patients, **71.3% (283/397)** continued HU and **114** switched to ruxolitinib; predictors of CR included no splenomegaly, no pruritus, and HU dose **≥1 g/day** (palandri2023predictorsofresponse pages 2-3) | DOI: 10.3390/cancers15143706; *Cancers* | 2023-07 | https://doi.org/10.3390/cancers15143706 |
| Ruxolitinib clinical activity (RuxoBEAT) | RuxoBEAT futility analysis (NCT02577926) in **28** untreated PV patients: median Hct **46% → 41%** at 6 months; median phlebotomies/year **4.0 → 0**; pruritus score **2 → 1**; night sweats **1.5 → 0** trend; JAK2V617F allele burden significantly decreased; **109** AEs in **24/28** patients, all grade 1–3; no permanent discontinuation due to AEs (koschmieder2023efficacyandsafety pages 1-2) | DOI: 10.1007/s00277-022-05080-7; *Ann Hematol* | 2023-12 | https://doi.org/10.1007/s00277-022-05080-7 |
| Ruxolitinib benchmark after HU failure | In RESPONSE/RESPONSE-2/MAJIC-PV summaries: hematocrit/spleen control **60%/40%** with ruxolitinib vs **20%/0.9%** with BAT; RESPONSE-2 hematocrit superiority **62% vs 19%**; MAJIC-PV CR **43% vs 26%** with BAT (tefferi2023polycythemiavera2024 pages 13-13) | DOI: 10.1002/ajh.27002; *Am J Hematol* | 2023-06 | https://doi.org/10.1002/ajh.27002 |


*Table: This table compiles high-yield quantitative findings and identifiers for polycythemia vera across epidemiology, molecular features, diagnosis, prognosis, and treatment studies. It is useful as a compact evidence map for rapid reference and knowledge-base curation.*

---

## Evidence limitations (important for knowledge-base ingestion)
- **PMID requirement:** The retrieved evidence snippets did not reliably include PMIDs; therefore, citations are provided using the system’s context IDs linked to DOI/journal sources. Where PMIDs are required, the cited DOI URLs can be used to resolve PubMed records.
- **Ontology IDs (MONDO/OMIM/Orphanet/MeSH/ICD):** Not present in the extracted text evidence and therefore not asserted.
- **HPO/GO/CL/MAXO IDs:** Suggested conceptually based on phenotype/mechanism descriptions but not sourced as explicit IDs from retrieved ontology resources.


References

1. (tefferi2023polycythemiavera2024 pages 2-2): Ayalew Tefferi and Tiziano Barbui. Polycythemia vera: 2024 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:1465-1487, Jun 2023. URL: https://doi.org/10.1002/ajh.27002, doi:10.1002/ajh.27002. This article has 254 citations and is from a domain leading peer-reviewed journal.

2. (silver2023polycythemiaveraaspects pages 1-3): Richard T Silver and Ghaith Abu-Zeinah. Polycythemia vera: aspects of its current diagnosis and initial treatment. Expert Review of Hematology, 16:253-266, Apr 2023. URL: https://doi.org/10.1080/17474086.2023.2198698, doi:10.1080/17474086.2023.2198698. This article has 8 citations and is from a peer-reviewed journal.

3. (goratybor2024recommendationsofpolish pages 2-3): Joanna Góra-Tybor, Tomasz Sacha, Maria Bieniaszewska, Marta Sobas, Krzysztof Lewandowski, Patryk Sobieralski, Olga Chyrko, and Aleksandra Gołos. Recommendations of polish adult leukemia group concerning diagnostics and treatment of polycythemia vera. Acta Haematologica Polonica, 55:289-305, Dec 2024. URL: https://doi.org/10.5603/ahp.102458, doi:10.5603/ahp.102458. This article has 5 citations.

4. (harrison2023ruxolitinibversusbest pages 1-2): Claire N. Harrison, Jyoti Nangalia, Rebecca Boucher, Aimee Jackson, Christina Yap, Jennifer O'Sullivan, Sonia Fox, Isaak Ailts, Amylou C. Dueck, Holly L. Geyer, Ruben A. Mesa, William G. Dunn, Eugene Nadezhdin, Natalia Curto-Garcia, Anna Green, Bridget Wilkins, Jason Coppell, John Laurie, Mamta Garg, Joanne Ewing, Steven Knapper, Josephine Crowe, Frederick Chen, Ioannis Koutsavlis, Anna Godfrey, Siamak Arami, Mark Drummond, Jennifer Byrne, Fiona Clark, Carolyn Mead-Harvey, Elizabeth Joanna Baxter, Mary Frances McMullin, and Adam J. Mead. Ruxolitinib versus best available therapy for polycythemia vera intolerant or resistant to hydroxycarbamide in a randomized trial. Journal of Clinical Oncology, 41:3534-3544, Jul 2023. URL: https://doi.org/10.1200/jco.22.01935, doi:10.1200/jco.22.01935. This article has 162 citations and is from a highest quality peer-reviewed journal.

5. (barbui2023ropeginterferonversusstandard pages 1-2): Tiziano Barbui, Alessandro Maria Vannucchi, Valerio De Stefano, Alessandra Carobbio, Arianna Ghirardi, Greta Carioli, Arianna Masciulli, Elena Rossi, Fabio Ciceri, Massimiliano Bonifacio, Alessandra Iurlo, Francesca Palandri, Giulia Benevolo, Fabrizio Pane, Alessandra Ricco, Giuseppe Carli, Marianna Caramella, Davide Rapezzi, Caterina Musolino, Sergio Siragusa, Elisa Rumi, Andrea Patriarca, Nicola Cascavilla, Barbara Mora, Emma Cacciola, Carmela Mannarelli, Giuseppe Gaetano Loscocco, Paola Guglielmelli, Francesca Gesullo, Silvia Betti, Francesca Lunghi, Luigi Scaffidi, Cristina Bucelli, Nicola Vianelli, Marta Bellini, Maria Chiara Finazzi, Gianni Tognoni, and Alessandro Rambaldi. Ropeginterferon versus standard therapy for low-risk patients with polycythemia vera. NEJM Evidence, May 2023. URL: https://doi.org/10.1056/evidoa2200335, doi:10.1056/evidoa2200335. This article has 62 citations and is from a peer-reviewed journal.

6. (kremyanskaya2024rusfertideahepcidin pages 1-2): Marina Kremyanskaya, Andrew T. Kuykendall, Naveen Pemmaraju, Ellen K. Ritchie, Jason Gotlib, Aaron Gerds, Jeanne Palmer, Kristen Pettit, Uttam K. Nath, Abdulraheem Yacoub, Arturo Molina, Samuel R. Saks, Nishit B. Modi, Frank H. Valone, Sarita Khanna, Suneel Gupta, Srdan Verstovsek, Yelena Z. Ginzburg, and Ronald Hoffman. Rusfertide, a hepcidin mimetic, for control of erythrocytosis in polycythemia vera. The New England journal of medicine, 390 8:723-735, Feb 2024. URL: https://doi.org/10.1056/nejmoa2308809, doi:10.1056/nejmoa2308809. This article has 56 citations and is from a highest quality peer-reviewed journal.

7. (verstovsek2023realworldtreatmentsand pages 1-2): Srdan Verstovsek, Naveen Pemmaraju, Nancy L. Reaven, Susan E. Funk, Tracy Woody, Frank Valone, and Suneel Gupta. Real-world treatments and thrombotic events in polycythemia vera patients in the usa. Annals of Hematology, 102:571-581, Jan 2023. URL: https://doi.org/10.1007/s00277-023-05089-6, doi:10.1007/s00277-023-05089-6. This article has 28 citations and is from a peer-reviewed journal.

8. (palandri2023predictorsofresponse pages 2-3): Francesca Palandri, Elena Rossi, Giuseppe Auteri, Massimo Breccia, Simona Paglia, Giulia Benevolo, Elena M. Elli, Francesco Cavazzini, Gianni Binotto, Alessia Tieghi, Mario Tiribelli, Florian H. Heidel, Massimiliano Bonifacio, Novella Pugliese, Giovanni Caocci, Monica Crugnola, Francesco Mendicino, Alessandra D'Addio, Simona Tomassetti, Bruno Martino, Nicola Polverelli, Sara Ceglie, Camilla Mazzoni, Rikard Mullai, Alessia Ripamonti, Bruno Garibaldi, Fabrizio Pane, Antonio Cuneo, Mauro Krampera, Gianpietro Semenzato, Roberto M. Lemoli, Nicola Vianelli, Giuseppe A. Palumbo, Alessandro Andriani, Michele Cavo, Roberto Latagliata, and Valerio De Stefano. Predictors of response to hydroxyurea and switch to ruxolitinib in hu-resistant polycythaemia vera patients: a real-world pv-net study. Cancers, 15:3706, Jul 2023. URL: https://doi.org/10.3390/cancers15143706, doi:10.3390/cancers15143706. This article has 13 citations.

9. (bennett2023ironhomeostasisgoverns pages 1-7): Cavan Bennett, Victoria E Jackson, Anne Pettikiriarachchi, Thomas Hayman, Ute Schaeper, Gemma Moir-Meyer, Katherine Fielding, Ricardo Ataide, Danielle Clucas, Andrew Baldi, Alexandra L Garnham, Connie SN Li-Wai-Suen, Stephen J Loughran, E Joanna Baxter, Anthony R Green, Warren S Alexander, Melanie Bahlo, Kate Burbury, Ashley P Ng, and Sant-Rayn Pasricha. Iron homeostasis governs erythroid phenotype in polycythemia vera. JournalArticle, Mar 2023. URL: https://doi.org/10.17863/cam.95022, doi:10.17863/cam.95022. This article has 17 citations.

10. (visweshwar2024impactofphlebotomy pages 8-10): Nathan Visweshwar, Bradley Fletcher, Michael Jaglal, Damian A. Laber, Ankita Patel, Jennifer Eatrides, Geetha Rajasekharan Rathnakumar, Keshav Visweswaran Iyer, Irmel Ayala, and Arumugam Manoharan. Impact of phlebotomy on quality of life in low-risk polycythemia vera. Journal of Clinical Medicine, 13:4952, Aug 2024. URL: https://doi.org/10.3390/jcm13164952, doi:10.3390/jcm13164952. This article has 5 citations.

11. (tefferi2023polycythemiavera2024 pages 7-8): Ayalew Tefferi and Tiziano Barbui. Polycythemia vera: 2024 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:1465-1487, Jun 2023. URL: https://doi.org/10.1002/ajh.27002, doi:10.1002/ajh.27002. This article has 254 citations and is from a domain leading peer-reviewed journal.

12. (barbui2026preservingthrombosisand pages 13-15): Tiziano Barbui, Arianna Ghirardi, Annalisa Condorelli, and Marta Sobas. Preserving thrombosis and life years in polycythemia vera: start by reading the biology of the disease. Haematologica, Feb 2026. URL: https://doi.org/10.3324/haematol.2025.300028, doi:10.3324/haematol.2025.300028. This article has 0 citations.

13. (koschmieder2023efficacyandsafety pages 1-2): Steffen Koschmieder, Susanne Isfort, Dominik Wolf, Florian H. Heidel, Andreas Hochhaus, Philippe Schafhausen, Martin Griesshammer, Denise Wolleschak, Uwe Platzbecker, Konstanze Döhner, Philipp J. Jost, Stefani Parmentier, Markus Schaich, Nikolas von Bubnoff, Frank Stegelmann, Angela Maurer, Martina Crysandt, Deniz Gezer, Maike Kortmann, Jeremy Franklin, Julia Frank, Martin Hellmich, and Tim H. Brümmendorf. Efficacy and safety of ruxolitinib in patients with newly-diagnosed polycythemia vera: futility analysis of the ruxobeat clinical trial of the gsg-mpn study group. Annals of Hematology, 102:349-358, Dec 2023. URL: https://doi.org/10.1007/s00277-022-05080-7, doi:10.1007/s00277-022-05080-7. This article has 11 citations and is from a peer-reviewed journal.

14. (handa2023hepcidinmimeticsin pages 4-6): Shivani Handa, Yelena Ginzburg, Ronald Hoffman, and Marina Kremyanskaya. Hepcidin mimetics in polycythemia vera: resolving the irony of iron deficiency and erythrocytosis. Current Opinion in Hematology, 30:45-52, Dec 2023. URL: https://doi.org/10.1097/moh.0000000000000747, doi:10.1097/moh.0000000000000747. This article has 29 citations and is from a peer-reviewed journal.

15. (handa2023hepcidinmimeticsin pages 13-15): Shivani Handa, Yelena Ginzburg, Ronald Hoffman, and Marina Kremyanskaya. Hepcidin mimetics in polycythemia vera: resolving the irony of iron deficiency and erythrocytosis. Current Opinion in Hematology, 30:45-52, Dec 2023. URL: https://doi.org/10.1097/moh.0000000000000747, doi:10.1097/moh.0000000000000747. This article has 29 citations and is from a peer-reviewed journal.

16. (tefferi2023polycythemiavera2024 pages 13-13): Ayalew Tefferi and Tiziano Barbui. Polycythemia vera: 2024 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:1465-1487, Jun 2023. URL: https://doi.org/10.1002/ajh.27002, doi:10.1002/ajh.27002. This article has 254 citations and is from a domain leading peer-reviewed journal.
