---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:17:03.915708'
end_time: '2026-05-09T11:28:06.348030'
duration_seconds: 662.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Panuveitis
  mondo_id: ''
  category: Immune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Panuveitis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Panuveitis** covering all of the
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
- **Disease Name:** Panuveitis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Panuveitis** covering all of the
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


# Comprehensive Research Report: Panuveitis (Immune category)

## Executive summary
Panuveitis is an anatomic classification of uveitis in which intraocular inflammation involves **all uveal regions** (anterior, intermediate, and posterior) and is clinically important because it is disproportionately associated with **sight-threatening complications** and frequently requires **systemic and/or intraocular corticosteroids plus steroid-sparing immunomodulatory therapy**, with biologics (notably adalimumab) supported by high-quality randomized trials in noninfectious intermediate/posterior/panuveitis. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7, jaffe2016adalimumabinpatients pages 1-2)

A structured summary table of identifiers/epidemiology/etiologies/complications and key trial statistics is provided here:

| Domain | Key facts for panuveitis KB entry | Source / year / DOI-URL | Support |
|---|---|---|---|
| Definition / classification | **Panuveitis** is the SUN anatomic class with inflammation involving **all uveal areas** (“all areas”); clinically, symptoms/signs may arise from anterior, intermediate, and posterior segments. | SUN overview: Clinical & Experimental Ophthalmology (2022), DOI: 10.1111/ceo.14175, https://doi.org/10.1111/ceo.14175; JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (jabs2022thestandardisationof pages 1-3, maghsoudlou2025uveitisinadults pages 4-7) |
| Epidemiology | In US/Europe series, **panuveitis accounts for ~7–32% of uveitis**. General uveitis epidemiology: **prevalence ~38–714/100,000** and **incidence ~17–52/100,000/year**; uveitis most often affects adults **20–50 years**. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 14-16) |
| Laterality / course | Panuveitis is **often bilateral (~75%)** and may be more chronic than anterior/posterior forms in some cohorts; disease progression can be variable/relapsing. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358; Life (2025), DOI: 10.3390/life15060882, https://doi.org/10.3390/life15060882 | (maghsoudlou2025uveitisinadults pages 4-7) |
| Common etiologies: infectious | Important infectious causes include **toxoplasmosis, herpes viruses, tuberculosis, syphilis, HIV-related infections**; infectious uveitis comprises **~11–21%** of cases in high-income countries and up to **~50%** in low-/middle-income countries. In one summary, toxoplasmosis contributed **~1–8%** among panuveitis associations. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358; Eye overview (2024), DOI: 10.1038/s41433-024-02966-w, https://doi.org/10.1038/s41433-024-02966-w | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7) |
| Common etiologies: noninfectious / immune | Frequent noninfectious associations include **sarcoidosis, Behçet disease, Vogt–Koyanagi–Harada disease** and other immune-mediated/systemic disorders; **37–49%** of uveitis cases are associated with systemic disease overall. Sarcoidosis was cited in **~5–29%** of panuveitis associations in reviewed series. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7, chauhan2024updateonnoninfectious pages 2-4) |
| Key complications | Panuveitis carries high risk of sight-threatening complications including **macular edema, retinal detachment, cataract, glaucoma, optic nerve damage, and vision loss**. Frequency ranges reported for uveitis complications include **cataract 18–49%**, **glaucoma 7–56%**, and **macular edema 8–10%**. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358; intravitreal therapy review (2016), DOI: 10.2147/OPTH.S89341, https://doi.org/10.2147/OPTH.S89341 | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 11-14) |
| Initial treatment algorithm | **Rule out infection first.** Infectious panuveitis requires organism-directed antimicrobials; noninfectious moderate/severe intermediate/posterior/panuveitis generally needs **systemic and/or intravitreal corticosteroids**, with early **steroid-sparing immunosuppression** when chronic, bilateral, recurrent, or vision-threatening. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358; Frontiers in Ophthalmology (2024), DOI: 10.3389/fopht.2024.1412930, https://doi.org/10.3389/fopht.2024.1412930 | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 14-16, chauhan2024updateonnoninfectious pages 2-4, chauhan2024updateonnoninfectious pages 1-2) |
| Corticosteroids / local therapy | Local steroid options used for posterior/panuveitic disease include **sub-Tenon triamcinolone (1–2 months)**, **intravitreal dexamethasone implant (3–6 months)**, and **fluocinolone implant (~36 months)**. Ocular hypertension is an important toxicity: cumulative incidence at 24 weeks reported as **41%** with dexamethasone implant, **30%** with intravitreal triamcinolone, **20%** with periocular triamcinolone. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 7-9) |
| DMARD evidence | Conventional steroid-sparing agents remain key: **methotrexate** achieved remission/control in about **52.1%** (95% CI 38.6–67.1%) and **mycophenolate mofetil** in about **70.9%** (95% CI 57.1–83.5%) in summarized posterior/nonanterior uveitis data; cyclosporine and azathioprine are additional options in selected etiologies (e.g., Behçet). | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 7-9) |
| Biologic therapy positioning | **Adalimumab** is the best-supported biologic and is approved for **noninfectious intermediate, posterior, and panuveitis**; typically used after inadequate response/intolerance to corticosteroids and/or conventional IMT, or when steroid-sparing control is needed. | Frontiers in Ophthalmology (2024), DOI: 10.3389/fopht.2024.1412930, https://doi.org/10.3389/fopht.2024.1412930; NEJM (2016), DOI: 10.1056/NEJMoa1509852, https://doi.org/10.1056/NEJMoa1509852 | (chauhan2024updateonnoninfectious pages 2-4, jaffe2016adalimumabinpatients pages 1-2) |
| RCT: adalimumab VISUAL I (active disease) | **VISUAL I**: phase 3 RCT in **active noninfectious intermediate/posterior/panuveitis**. Adalimumab **prolonged median time to treatment failure to 24 vs 13 weeks** for placebo; **HR 0.50 (95% CI 0.36–0.70), P<0.001**. | NEJM (2016), DOI: 10.1056/NEJMoa1509852, https://doi.org/10.1056/NEJMoa1509852 | (jaffe2016adalimumabinpatients pages 1-2, jaffe2016adalimumabinpatients pages 2-3) |
| RCT: adalimumab VISUAL II (inactive steroid-dependent disease) | **VISUAL II**: phase 3 RCT in **inactive steroid-dependent intermediate/posterior/panuveitis**. Adalimumab **reduced risk of treatment failure** vs placebo: **HR 0.57 (95% CI 0.39–0.84), P=0.004**; **40th percentile time to failure 10.2 vs 4.8 months**. | VISUAL II report (2016), multicentre double-masked trial; URL/DOI not fully captured in excerpt | (nguyen2016adalimumabforpreventiona pages 1-6, nguyen2016adalimumabforprevention pages 6-10) |
| Long-term biologic data | In **VISUAL III** long-term follow-up/open-label data summarized in review literature, quiescence increased from **34% to 85% over 3 years** among noninfectious intermediate/posterior/panuveitis patients treated with adalimumab. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 11-14) |
| RCT: local steroid comparison | In a **192-patient trial**, intravitreal steroid implants reduced macular thickness at 8 weeks more than periocular triamcinolone: **39%** (triamcinolone implant) and **46%** (dexamethasone implant) vs **23%** (periocular), **p<0.0001**. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 7-9) |
| RCT: suprachoroidal triamcinolone | In a **160-patient RCT**, **suprachoroidal triamcinolone** produced **≥15-letter visual acuity gains in 47% vs 16%** with placebo at 4 weeks (**p<0.001**) in noninfectious uveitic macular edema/posterior segment disease contexts relevant to panuveitis care. | JAMA review (2025), DOI: 10.1001/jama.2025.4358, https://doi.org/10.1001/jama.2025.4358 | (maghsoudlou2025uveitisinadults pages 7-9) |


*Table: This table summarizes core disease-knowledge-base facts for panuveitis, including definition, epidemiology, etiologies, complications, and treatment evidence. It highlights the most actionable quantitative findings, especially major randomized trial results relevant to current management.*

---

## 1. Disease information

### 1.1 What is panuveitis?
**Panuveitis** is a **SUN (Standardization of Uveitis Nomenclature) anatomic class** of uveitis describing inflammation that affects **all uveal areas** (“all areas”). (maghsoudlou2025uveitisinadults pages 4-7)

### 1.2 Key identifiers (ICD/MeSH/MONDO)
* **ICD-10 / ICD-11**: Not fully retrievable from the provided evidence snippets; some literature notes alignment of reimbursement codes with ICD-10 uveitis categories (but does not explicitly provide the panuveitis ICD code in extracted text). (jabs2022thestandardisationof pages 3-4)
* **MeSH**: Not retrievable from the provided evidence snippets.
* **MONDO ID**: Not retrievable from the provided evidence snippets.

Because the tool-retrieved corpus did not include ontology registry pages (e.g., MONDO, MeSH browser), the KB identifiers above should be validated against those databases directly.

### 1.3 Synonyms / alternative names
Panuveitis is often discussed as “**pan-uveitis**” or “uveitis involving all anatomic locations.” (maghsoudlou2025uveitisinadults pages 4-7)

### 1.4 Evidence source type
The information below is derived from **aggregated disease-level resources** (systematic/narrative reviews, consensus/standardization efforts, randomized trials) and selected cohort studies, rather than individual EHR-derived phenotyping. (maghsoudlou2025uveitisinadults pages 1-4, jabs2022thestandardisationof pages 1-3, jaffe2016adalimumabinpatients pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (high-level)
Panuveitis is not a single etiologic disease; it is an **anatomic phenotype** that can arise from **infectious** or **noninfectious (immune-mediated/systemic)** conditions. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 14-16)

### 2.2 Risk factors and associated conditions
#### Infectious causes (examples)
Across settings, major infectious contributors to uveitis include **toxoplasmosis, herpes viruses, tuberculosis, HIV**, and **syphilis**; in high-income countries infectious causes contribute roughly **11–21%** of uveitis, while in low-/middle-income countries they may contribute up to **~50%**. (maghsoudlou2025uveitisinadults pages 1-4)

In reviewed series summarized in a 2025 JAMA uveitis review, panuveitis associations included **toxoplasmosis (reported ~1–8%)**. (maghsoudlou2025uveitisinadults pages 4-7)

#### Noninfectious / immune-mediated associations (examples)
Noninfectious associations discussed in recent synthesis include **sarcoidosis**, **Behçet disease**, and **Vogt–Koyanagi–Harada (VKH)**, among other systemic inflammatory diseases; overall, **37–49%** of uveitis cases are associated with systemic disease in US/Europe series. (maghsoudlou2025uveitisinadults pages 1-4)

In the same synthesis, panuveitis associations included **sarcoidosis (~5–29%)** across reviewed cohorts. (maghsoudlou2025uveitisinadults pages 4-7)

### 2.3 Protective factors
No protective factors specific to panuveitis were identified in the retrieved evidence corpus.

### 2.4 Gene–environment interactions
The retrieved evidence notes that uveitis epidemiology is influenced by genetic factors (e.g., HLA associations) and environmental factors (e.g., air pollution), but gene–environment interaction effects specific to panuveitis were not extractable from the provided excerpts. (maghsoudlou2025uveitisinadults pages 1-4)

---

## 3. Phenotypes (clinical features)

### 3.1 Common symptom/sign phenotypes
Panuveitis produces combined manifestations from the three uveal regions; uveitis generally presents with **eye redness, pain, photophobia, floaters, and blurred vision**. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7)

### 3.2 Sight-threatening features/complications as phenotypes
Panuveitis (grouped with moderate–severe intermediate and posterior uveitis) is highlighted as high risk for **sight-threatening complications**, including **macular edema** and severe posterior segment inflammation. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 7-9)

### 3.3 Quality-of-life impact
Direct quantitative QoL statistics for panuveitis were not present in the retrieved evidence. However, the clinical emphasis that uveitis is a major cause of irreversible vision loss implies substantial functional impact when complications occur. (chauhan2024updateonnoninfectious pages 1-2, maghsoudlou2025uveitisinadults pages 1-4)

### 3.4 Suggested HPO terms (non-exhaustive; ontology suggestions)
* Eye pain: **HP:0030038**
* Photophobia: **HP:0000613**
* Floaters: **HP:0030319**
* Blurred vision: **HP:0000622**
* Cystoid macular edema: **HP:0001103**
* Cataract: **HP:0000518**
* Glaucoma: **HP:0000501**
* Retinal detachment: **HP:0000541**

(These are ontology suggestions; confirmation against HPO is recommended.)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
Panuveitis is an anatomic descriptor rather than a monogenic disorder; causal genes/variants are typically defined at the level of **underlying specific uveitic diseases** (e.g., systemic inflammatory syndromes), not the panuveitis anatomic class. No gene-specific variant claims were retrievable from the evidence corpus provided.

### 4.2 Immune mechanisms and pathways (current understanding)
A recent synthesis describes uveitis as involving loss of ocular immune privilege and inflammatory pathways including **Th1/Th17** and cytokines including **IL-6** and **TNF-α**—a mechanistic rationale consistent with the clinical efficacy of anti-TNF biologics in noninfectious intermediate/posterior/panuveitis. (maghsoudlou2025uveitisinadults pages 14-16, chauhan2024updateonnoninfectious pages 2-4)

### 4.3 Suggested GO / CL ontology terms (mechanism/cell-type suggestions)
* GO: inflammatory response (**GO:0006954**)
* GO: regulation of T cell activation (**GO:0050863**)
* GO: cytokine-mediated signaling pathway (**GO:0019221**)
* Cell types: T helper 17 cell (**CL:0000899**), CD4-positive T cell (**CL:0000624**), macrophage (**CL:0000235**)

(These are ontology suggestions; confirmation against GO/CL is recommended.)

---

## 5. Environmental information
No panuveitis-specific environmental toxin or lifestyle risk-factor statistics were retrievable from the provided evidence. Uveitis incidence/prevalence is described as influenced by environmental factors such as air pollution at a general level. (maghsoudlou2025uveitisinadults pages 1-4)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (conceptual)
1. **Trigger/underlying disease**: infection (e.g., toxoplasmosis, herpes viruses, TB, syphilis) or immune-mediated systemic disease (e.g., sarcoidosis, Behçet, VKH). (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7)
2. **Immune activation in ocular tissues**: breakdown of immune privilege and inflammatory cytokine signaling (e.g., TNF-α, IL-6; Th1/Th17-related responses). (maghsoudlou2025uveitisinadults pages 14-16, chauhan2024updateonnoninfectious pages 2-4)
3. **Tissue injury**: inflammation of iris/ciliary body/choroid with spillover to vitreous/retina and downstream complications such as macular edema, glaucoma/cataract, retinal detachment, optic nerve damage. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 7-9)
4. **Clinical outcomes**: reduced visual acuity and potential irreversible vision loss if uncontrolled. (maghsoudlou2025uveitisinadults pages 1-4)

---

## 7. Anatomical structures affected

### 7.1 Organ level
Primary organ: **eye** (uveal tract and adjacent intraocular structures). (maghsoudlou2025uveitisinadults pages 1-4)

### 7.2 Tissue / intraocular compartments
The anatomic distribution explicitly includes iris/ciliary body/choroid (uvea), and clinical consequences include involvement of retina/macula and optic nerve structures via macular edema, retinal detachment, and optic nerve damage. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 7-9)

### 7.3 Suggested UBERON terms (examples; ontology suggestions)
* Eye: **UBERON:0000970**
* Uvea: **UBERON:0001777**
* Retina: **UBERON:0000966**
* Choroid: **UBERON:0001775**

---

## 8. Temporal development (onset, course)
Uveitis most commonly affects adults aged **~20–50 years**. Panuveitis may be **bilateral (~75%)** and is managed as higher-risk disease often needing systemic therapy, consistent with potential chronic/relapsing courses in noninfectious disease. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recently summarized ranges)
A 2025 clinical synthesis reports broad ranges for **uveitis** epidemiology: **prevalence ~38–714 per 100,000** and **incidence ~17–52 per 100,000/year**; within uveitis cohorts, panuveitis represented **~7–32%** of cases (US/Europe) and could be higher in some regions. (maghsoudlou2025uveitisinadults pages 14-16, maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 4-7)

### 9.2 Population demographics
The same synthesis notes uveitis is most frequent in working-age adults (~20–50) with a slight female predominance (uveitis overall), but panuveitis-specific sex ratios were not extractable from the provided text. (maghsoudlou2025uveitisinadults pages 14-16)

---

## 10. Diagnostics

### 10.1 Workup principles
Because panuveitis spans infectious and immune causes, evaluation emphasizes testing for infection (e.g., syphilis) and systemic disease (e.g., sarcoidosis), with ocular sampling when infection is suspected. (maghsoudlou2025uveitisinadults pages 4-7, maghsoudlou2025uveitisinadults pages 14-16)

### 10.2 Imaging: current applications and real-world implementation (2023–2024 emphasis)
#### Fundus autofluorescence (FAF)
A 2024 review emphasizes **FAF as a prompt, non-invasive modality** helpful in detecting and monitoring retinal/choroidal abnormalities in posterior uveitis and panuveitis; FAF is described as useful for **staging**, **mapping lesion extent beyond clinical exam**, and **monitoring activity/response**, with disease- and stage-dependent patterns (often hyperautofluorescence in active inflammation, hypoautofluorescence in atrophy/inactive disease, with important entity-specific exceptions). (mauschitz2024fundusautofluorescencein pages 2-4, mauschitz2024fundusautofluorescencein pages 15-16, mauschitz2024fundusautofluorescencein pages 13-15)

Practical limitations include that FAF alone cannot reliably subtype uveitis, may be impacted by media opacity, and should be used as part of **multimodal imaging** with OCT/angiography and clinical/laboratory correlation. (mauschitz2024fundusautofluorescencein pages 15-16)

#### Artificial intelligence for diagnosis/classification
A major SUN standardization effort incorporated machine learning to derive classification criteria for 25 common uveitic diseases from a curated retrospective dataset, reporting high validation performance across anatomic classes. In validation, reported accuracy by anatomic class included **panuveitides ~94.0%** and **infectious posterior/panuveitides ~93.3%**; performance on a masked-observer application of final rules was reported as **panuveitides ~98.9%** and **infectious posterior/panuveitides ~98.8%**. (jabs2022thestandardisationof pages 6-7)

Key caveats described for the SUN approach include lack of a diagnostic gold standard, moderate expert agreement historically, and incomplete retrospective data requiring an “evidence for” approach to missingness; additionally, the project used graded image results rather than raw images for machine learning. (jabs2022thestandardisationof pages 3-4, jabs2022thestandardisationof pages 4-6)

### 10.3 Molecular diagnostics for infectious panuveitis (metagenomic sequencing)
A 2025 clinical study using intraocular-fluid metagenomic next-generation sequencing (mNGS) in suspected infectious uveitis reported **mNGS positivity 73.97% vs culture 3.45%**, supporting mNGS as a high-yield tool when infection is in the differential. In this cohort, all patients were described as presenting with **panuveitis**, and **14 cases** were complicated by retinal detachment. (shen2025virusininfectious pages 1-2, shen2025virusininfectious pages 4-5)

---

## 11. Outcome / prognosis
Untreated uveitis can result in vision-threatening structural complications including cataract, glaucoma, macular edema, retinal detachment, and optic nerve damage. (maghsoudlou2025uveitisinadults pages 1-4)

In a recent synthesis, reported frequency ranges for uveitis complications included **cataract 18–49%**, **glaucoma 7–56%**, and **macular edema 8–10%**. (maghsoudlou2025uveitisinadults pages 11-14)

---

## 12. Treatment

### 12.1 Treatment goals
The overarching goal is to induce and maintain remission while minimizing corticosteroid toxicity, with etiologic therapy (antimicrobial) prioritized for infectious disease. (maghsoudlou2025uveitisinadults pages 1-4)

### 12.2 Pharmacotherapy and immunomodulatory therapy (current practice)
Patients with moderate–severe intermediate uveitis, posterior uveitis, and **panuveitis** are emphasized as higher risk for sight-threatening outcomes and generally require **systemic and/or intravitreal corticosteroids** and steroid-sparing immunosuppressive agents. (maghsoudlou2025uveitisinadults pages 1-4, maghsoudlou2025uveitisinadults pages 7-9)

#### Corticosteroids (systemic/local)
Local steroid delivery options and typical durations include **sub-Tenon triamcinolone (1–2 months)**, **intravitreal dexamethasone implant (3–6 months)**, and **fluocinolone implant (~36 months)**; ocular hypertension risk varies by delivery method (e.g., cumulative ocular hypertension at 24 weeks: dexamethasone implant 41%, intravitreal triamcinolone 30%, periocular 20%). (maghsoudlou2025uveitisinadults pages 7-9)

#### Conventional steroid-sparing IMT (DMARDs)
In summarized posterior/nonanterior uveitis data, methotrexate achieved remission/control in **52.1%** (95% CI 38.6–67.1) and mycophenolate mofetil achieved control in **70.9%** (95% CI 57.1–83.5). (maghsoudlou2025uveitisinadults pages 1-4)

#### Biologics (2023–2024 context and evidence base)
A 2024 review emphasizes that biologics are used for corticosteroid-intolerant/resistant disease, highlighting TNF-α inhibitors, and notes that **adalimumab** is approved for **noninfectious intermediate, posterior, and panuveitis**. (chauhan2024updateonnoninfectious pages 2-4)

##### Adalimumab – randomized trial evidence (VISUAL program)
* **VISUAL I (active disease)** (NEJM, Sep 2016; DOI: 10.1056/NEJMoa1509852; URL: https://doi.org/10.1056/NEJMoa1509852): In active noninfectious intermediate/posterior/panuveitis, adalimumab prolonged **median time to treatment failure to 24 weeks vs 13 weeks** with placebo (**HR 0.50**, 95% CI 0.36–0.70; **P<0.001**). (jaffe2016adalimumabinpatients pages 1-2)
  * Abstract quote (from extracted excerpt): “**median time to treatment failure was 24 weeks in the adalimumab group and 13 weeks in the placebo group**.” (jaffe2016adalimumabinpatients pages 1-2)
* **VISUAL II (inactive, steroid-dependent disease)**: In inactive steroid-dependent intermediate/posterior/panuveitis, adalimumab reduced treatment failure risk (**HR 0.57**, 95% CI 0.39–0.84; **P=0.004**) with a reported **40th percentile time to treatment failure 10.2 vs 4.8 months** (adalimumab vs placebo). (nguyen2016adalimumabforpreventiona pages 1-6)

Longer-term follow-up summarized in a 2025 clinical synthesis notes VISUAL III data with quiescence increasing from **34% to 85% over 3 years** on adalimumab in noninfectious intermediate/posterior/panuveitis. (maghsoudlou2025uveitisinadults pages 11-14)

### 12.3 Real-world implementations
Implementation patterns emphasized in recent syntheses include (i) multidisciplinary care when systemic inflammatory disease is present and (ii) escalation from corticosteroids to immunosuppressants and then biologics for refractory disease. (maghsoudlou2025uveitisinadults pages 1-4, chauhan2024updateonnoninfectious pages 2-4)

### 12.4 Treatment outcomes: local steroid trials relevant to posterior-segment inflammation
A 2025 synthesis reports trials supporting local corticosteroid approaches relevant to posterior-segment inflammation seen in panuveitis:
* In a **192-patient trial**, intravitreal steroid implants reduced macular thickness at 8 weeks more than periocular triamcinolone (39% and 46% vs 23%; **p<0.0001**). (maghsoudlou2025uveitisinadults pages 7-9)
* In a **160-patient RCT**, suprachoroidal triamcinolone produced ≥15-letter VA gains in **47% vs 16%** with placebo at 4 weeks (**p<0.001**). (maghsoudlou2025uveitisinadults pages 7-9)

### 12.5 MAXO term suggestions (treatment actions; ontology suggestions)
* Corticosteroid therapy (systemic and local ocular delivery)
* Immunosuppressive therapy (e.g., antimetabolite therapy)
* Anti-TNF therapy (adalimumab)
* Intravitreal drug delivery / ocular implant therapy

---

## 13. Prevention
No panuveitis-specific primary-prevention interventions were identified in the retrieved corpus. Preventive strategy is largely **secondary/tertiary**: early identification of infectious etiologies (to avoid inappropriate immunosuppression) and early initiation of steroid-sparing control to prevent recurrent inflammatory damage. (maghsoudlou2025uveitisinadults pages 14-16, maghsoudlou2025uveitisinadults pages 1-4)

---

## 14. Other species / natural disease
No veterinary/natural panuveitis evidence in other species was retrieved within the provided corpus.

---

## 15. Model organisms
No model-organism evidence was retrieved within the provided corpus. (Note: uveitis research commonly uses experimental autoimmune uveitis models, but this claim cannot be supported from the current evidence set.)

---

## Recent developments (prioritizing 2023–2024)
* **Imaging/monitoring**: 2024 review highlights expanding and entity-specific use of **fundus autofluorescence** (including ultra-widefield and multi-wavelength FAF) for diagnosis, staging, and monitoring posterior uveitis/panuveitis, emphasizing multimodal imaging integration. Publication date: Apr 2024; URL: https://doi.org/10.3390/biom14050515. (mauschitz2024fundusautofluorescencein pages 2-4, mauschitz2024fundusautofluorescencein pages 15-16)
* **Therapeutic landscape**: 2024 review synthesizes “anti-TNF-alpha and beyond” strategies for **noninfectious uveitis**, positioning biologics as key steroid-sparing options when conventional therapy fails; publication date: Aug 2024; URL: https://doi.org/10.3389/fopht.2024.1412930. (chauhan2024updateonnoninfectious pages 2-4)
* **AI/classification infrastructure**: SUN project report (Oct 2022) documents the machine-learning-based development of classification criteria for common uveitides with high reported accuracy in panuveitides and infectious posterior/panuveitides categories, illustrating a pathway toward more standardized research cohorts. Publication date: Oct 2022; URL: https://doi.org/10.1111/ceo.14175. (jabs2022thestandardisationof pages 6-7, jabs2022thestandardisationof pages 4-6)

---

## Limitations of this report (evidence availability)
1. **PMIDs**: Although multiple primary trials were retrieved with DOIs and journal information, **PMIDs were not present in the extracted text snippets**, so PMID-level citation could not be reliably provided without external lookup. (jaffe2016adalimumabinpatients pages 1-2, nguyen2016adalimumabforpreventiona pages 1-6)
2. **Ontology IDs (MONDO/MeSH/ICD)**: MONDO/MeSH/ICD identifiers for panuveitis were not present in the retrieved excerpts; this report therefore flags them as not retrievable from the current tool evidence. (jabs2022thestandardisationof pages 3-4)
3. **Genetics/model organisms**: The current corpus did not contain panuveitis-specific genetic variant evidence or model organism summaries.

---

## Key references with URLs and publication dates
* Maghsoudlou P, et al. **Uveitis in Adults: A Review.** *JAMA.* **May 2025.** https://doi.org/10.1001/jama.2025.4358 (maghsoudlou2025uveitisinadults pages 1-4)
* Jaffe GJ, et al. **Adalimumab in Patients with Active Noninfectious Uveitis (VISUAL I).** *N Engl J Med.* **Sep 2016.** https://doi.org/10.1056/NEJMoa1509852 (jaffe2016adalimumabinpatients pages 1-2)
* Chauhan K, Tyagi M. **Update on non-infectious uveitis treatment: anti-TNF-alpha and beyond.** *Frontiers in Ophthalmology.* **Aug 2024.** https://doi.org/10.3389/fopht.2024.1412930 (chauhan2024updateonnoninfectious pages 2-4)
* Mauschitz MM, et al. **Fundus Autofluorescence in Posterior and Panuveitis—An Under-Estimated Imaging Technique.** *Biomolecules.* **Apr 2024.** https://doi.org/10.3390/biom14050515 (mauschitz2024fundusautofluorescencein pages 2-4)
* Jabs DA, et al. **The standardisation of uveitis nomenclature (SUN) project.** *Clin Exp Ophthalmol.* **Oct 2022.** https://doi.org/10.1111/ceo.14175 (jabs2022thestandardisationof pages 1-3)
* Shen J, et al. **Virus in infectious uveitis: bibliometric analysis and a clinical study (mNGS yield).** *Frontiers in Microbiology.* **Aug 2025.** https://doi.org/10.3389/fmicb.2025.1588195 (shen2025virusininfectious pages 1-2)


References

1. (maghsoudlou2025uveitisinadults pages 1-4): Panayiotis Maghsoudlou, Simon J. Epps, Catherine M. Guly, and Andrew D. Dick. Uveitis in adults: a review. JAMA, May 2025. URL: https://doi.org/10.1001/jama.2025.4358, doi:10.1001/jama.2025.4358. This article has 47 citations.

2. (maghsoudlou2025uveitisinadults pages 4-7): Panayiotis Maghsoudlou, Simon J. Epps, Catherine M. Guly, and Andrew D. Dick. Uveitis in adults: a review. JAMA, May 2025. URL: https://doi.org/10.1001/jama.2025.4358, doi:10.1001/jama.2025.4358. This article has 47 citations.

3. (jaffe2016adalimumabinpatients pages 1-2): Glenn J. Jaffe, Andrew D. Dick, Antoine P. Brézin, Quan Dong Nguyen, Jennifer E. Thorne, Philippe Kestelyn, Talin Barisani-Asenbauer, Pablo Franco, Arnd Heiligenhaus, David Scales, David S. Chu, Anne Camez, Nisha V. Kwatra, Alexandra P. Song, Martina Kron, Samir Tari, and Eric B. Suhler. Adalimumab in patients with active noninfectious uveitis. New England Journal of Medicine, 375:932-943, Sep 2016. URL: https://doi.org/10.1056/nejmoa1509852, doi:10.1056/nejmoa1509852. This article has 746 citations and is from a highest quality peer-reviewed journal.

4. (jabs2022thestandardisationof pages 1-3): Douglas A. Jabs, Peter McCluskey, Alan G. Palestine, Jennifer E. Thorne, and The Standardization of Uveitis Nomenclature (SUN) Working Gr. The standardisation of uveitis nomenclature (<scp>sun</scp>) project. Clinical &amp; Experimental Ophthalmology, 50:991-1000, Oct 2022. URL: https://doi.org/10.1111/ceo.14175, doi:10.1111/ceo.14175. This article has 45 citations and is from a peer-reviewed journal.

5. (maghsoudlou2025uveitisinadults pages 14-16): Panayiotis Maghsoudlou, Simon J. Epps, Catherine M. Guly, and Andrew D. Dick. Uveitis in adults: a review. JAMA, May 2025. URL: https://doi.org/10.1001/jama.2025.4358, doi:10.1001/jama.2025.4358. This article has 47 citations.

6. (chauhan2024updateonnoninfectious pages 2-4): Khushboo Chauhan and Mudit Tyagi. Update on non-infectious uveitis treatment: anti-tnf-alpha and beyond. Frontiers in Ophthalmology, Aug 2024. URL: https://doi.org/10.3389/fopht.2024.1412930, doi:10.3389/fopht.2024.1412930. This article has 15 citations.

7. (maghsoudlou2025uveitisinadults pages 11-14): Panayiotis Maghsoudlou, Simon J. Epps, Catherine M. Guly, and Andrew D. Dick. Uveitis in adults: a review. JAMA, May 2025. URL: https://doi.org/10.1001/jama.2025.4358, doi:10.1001/jama.2025.4358. This article has 47 citations.

8. (chauhan2024updateonnoninfectious pages 1-2): Khushboo Chauhan and Mudit Tyagi. Update on non-infectious uveitis treatment: anti-tnf-alpha and beyond. Frontiers in Ophthalmology, Aug 2024. URL: https://doi.org/10.3389/fopht.2024.1412930, doi:10.3389/fopht.2024.1412930. This article has 15 citations.

9. (maghsoudlou2025uveitisinadults pages 7-9): Panayiotis Maghsoudlou, Simon J. Epps, Catherine M. Guly, and Andrew D. Dick. Uveitis in adults: a review. JAMA, May 2025. URL: https://doi.org/10.1001/jama.2025.4358, doi:10.1001/jama.2025.4358. This article has 47 citations.

10. (jaffe2016adalimumabinpatients pages 2-3): Glenn J. Jaffe, Andrew D. Dick, Antoine P. Brézin, Quan Dong Nguyen, Jennifer E. Thorne, Philippe Kestelyn, Talin Barisani-Asenbauer, Pablo Franco, Arnd Heiligenhaus, David Scales, David S. Chu, Anne Camez, Nisha V. Kwatra, Alexandra P. Song, Martina Kron, Samir Tari, and Eric B. Suhler. Adalimumab in patients with active noninfectious uveitis. New England Journal of Medicine, 375:932-943, Sep 2016. URL: https://doi.org/10.1056/nejmoa1509852, doi:10.1056/nejmoa1509852. This article has 746 citations and is from a highest quality peer-reviewed journal.

11. (nguyen2016adalimumabforpreventiona pages 1-6): QD Nguyen, PT Merrill, GJ Jaffe, AD Dick, and SK Kurup. Adalimumab for prevention of uveitic flare in patients with inactive non-infectious uveitis controlled by corticosteroids (visual ii): a multicentre, double-masked …. Unknown journal, 2016.

12. (nguyen2016adalimumabforprevention pages 6-10): QD Nguyen, PT Merrill, GJ Jaffe, AD Dick, and SK Kurup. Adalimumab for prevention of uveitic flare in patients with inactive non-infectious uveitis controlled by corticosteroids (visual ii): a multicentre, double-masked …. Unknown journal, 2016.

13. (jabs2022thestandardisationof pages 3-4): Douglas A. Jabs, Peter McCluskey, Alan G. Palestine, Jennifer E. Thorne, and The Standardization of Uveitis Nomenclature (SUN) Working Gr. The standardisation of uveitis nomenclature (<scp>sun</scp>) project. Clinical &amp; Experimental Ophthalmology, 50:991-1000, Oct 2022. URL: https://doi.org/10.1111/ceo.14175, doi:10.1111/ceo.14175. This article has 45 citations and is from a peer-reviewed journal.

14. (mauschitz2024fundusautofluorescencein pages 2-4): Matthias M. Mauschitz, Markus Zeller, Pradeep Sagar, Suchitra Biswal, Gabriela Guzman, Jan H. Terheyden, Carsten H. Meyer, Frank G. Holz, Carsten Heinz, Uwe Pleyer, Robert P. Finger, and Maximilian W. M. Wintergerst. Fundus autofluorescence in posterior and panuveitis—an under-estimated imaging technique: a review and case series. Biomolecules, 14:515, Apr 2024. URL: https://doi.org/10.3390/biom14050515, doi:10.3390/biom14050515. This article has 3 citations.

15. (mauschitz2024fundusautofluorescencein pages 15-16): Matthias M. Mauschitz, Markus Zeller, Pradeep Sagar, Suchitra Biswal, Gabriela Guzman, Jan H. Terheyden, Carsten H. Meyer, Frank G. Holz, Carsten Heinz, Uwe Pleyer, Robert P. Finger, and Maximilian W. M. Wintergerst. Fundus autofluorescence in posterior and panuveitis—an under-estimated imaging technique: a review and case series. Biomolecules, 14:515, Apr 2024. URL: https://doi.org/10.3390/biom14050515, doi:10.3390/biom14050515. This article has 3 citations.

16. (mauschitz2024fundusautofluorescencein pages 13-15): Matthias M. Mauschitz, Markus Zeller, Pradeep Sagar, Suchitra Biswal, Gabriela Guzman, Jan H. Terheyden, Carsten H. Meyer, Frank G. Holz, Carsten Heinz, Uwe Pleyer, Robert P. Finger, and Maximilian W. M. Wintergerst. Fundus autofluorescence in posterior and panuveitis—an under-estimated imaging technique: a review and case series. Biomolecules, 14:515, Apr 2024. URL: https://doi.org/10.3390/biom14050515, doi:10.3390/biom14050515. This article has 3 citations.

17. (jabs2022thestandardisationof pages 6-7): Douglas A. Jabs, Peter McCluskey, Alan G. Palestine, Jennifer E. Thorne, and The Standardization of Uveitis Nomenclature (SUN) Working Gr. The standardisation of uveitis nomenclature (<scp>sun</scp>) project. Clinical &amp; Experimental Ophthalmology, 50:991-1000, Oct 2022. URL: https://doi.org/10.1111/ceo.14175, doi:10.1111/ceo.14175. This article has 45 citations and is from a peer-reviewed journal.

18. (jabs2022thestandardisationof pages 4-6): Douglas A. Jabs, Peter McCluskey, Alan G. Palestine, Jennifer E. Thorne, and The Standardization of Uveitis Nomenclature (SUN) Working Gr. The standardisation of uveitis nomenclature (<scp>sun</scp>) project. Clinical &amp; Experimental Ophthalmology, 50:991-1000, Oct 2022. URL: https://doi.org/10.1111/ceo.14175, doi:10.1111/ceo.14175. This article has 45 citations and is from a peer-reviewed journal.

19. (shen2025virusininfectious pages 1-2): Junhui Shen, Jinfeng Kong, Yufeng Xu, Yanyan Hu, and Lei Feng. Virus in infectious uveitis: bibliometric analysis and a clinical study. Frontiers in Microbiology, Aug 2025. URL: https://doi.org/10.3389/fmicb.2025.1588195, doi:10.3389/fmicb.2025.1588195. This article has 0 citations and is from a peer-reviewed journal.

20. (shen2025virusininfectious pages 4-5): Junhui Shen, Jinfeng Kong, Yufeng Xu, Yanyan Hu, and Lei Feng. Virus in infectious uveitis: bibliometric analysis and a clinical study. Frontiers in Microbiology, Aug 2025. URL: https://doi.org/10.3389/fmicb.2025.1588195, doi:10.3389/fmicb.2025.1588195. This article has 0 citations and is from a peer-reviewed journal.