---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-01T07:16:22.727426'
end_time: '2026-05-01T07:30:40.544999'
duration_seconds: 857.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Takayasu Arteritis
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Takayasu Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Takayasu Arteritis** covering all of the
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
- **Disease Name:** Takayasu Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Takayasu Arteritis** covering all of the
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


## Comprehensive Research Report: Takayasu Arteritis (Autoimmune Large-Vessel Vasculitis)

### Scope and evidence base
This report synthesizes recent guidelines and reviews (prioritizing 2023–2024) plus key trials and cohort studies that quantify outcomes in Takayasu arteritis (TAK). Evidence includes aggregated resources (guidelines, systematic reviews/meta-analyses) and patient-level cohorts/clinical trials; both are explicitly distinguished where possible.

---

## 1. Disease Information

### 1.1 What is the disease? (concise overview)
Takayasu arteritis is a chronic granulomatous inflammatory large-vessel vasculitis that predominantly involves the aorta and its primary branches, leading to vessel-wall thickening and remodeling with stenosis/occlusion and/or aneurysm formation; clinical consequences arise from organ ischemia and vascular complications. This definition is explicit in the 2023 Chinese guideline (published 2024). (tian2024chineseguidelinefor pages 1-2)

The 2023 International Heart Journal review similarly defines TAK as “a chronic large vessel vasculitis with predilection to affect the aorta and its branches,” highlighting vessel-wall thickening/fibrosis and ischemic complications. (as2023currentdiagnosisand pages 1-2)

### 1.2 Key identifiers (available from retrieved sources)
* **ICD-10:** **M31.4** (Takayasu’s arteritis), explicitly used for case ascertainment in a Korean population-based survival study. (jang2021survivalandcauses pages 1-2)
* **MeSH:** **D013625** (“Takayasu Arteritis”), explicitly listed in multiple ClinicalTrials.gov condition browse modules. (NCT07491913 chunk 2, NCT02101333 chunk 2, NCT04882072 chunk 4, NCT02101333 chunk 3)
* **MONDO / Orphanet / OMIM / ICD-11:** Not explicitly present in the retrieved full texts or clinical trial record chunks available in this tool run; therefore, these identifiers cannot be asserted here without external ontology lookup. (NCT02101333 chunk 2, jang2021survivalandcauses pages 1-2)

### 1.3 Common synonyms and alternative names
Authoritative sources and trial records show the following synonyms/alternative names:
* **Aortic arch syndrome**, **non-specific aortoarteritis**, **pulseless disease** (explicitly listed as alternative names in the Korean population-based study). (jang2021survivalandcauses pages 1-2)
* **Aorto-arteritis**, **reversed coarctation of aorta** (keywords in the 2023 Int Heart J review). (as2023currentdiagnosisand pages 1-2)
* Abbreviations: **TA**, **TAK**. (as2023currentdiagnosisand pages 1-2)

### 1.4 Data provenance note (individual vs aggregated)
* **Aggregated resources:** evidence-based clinical guideline (China 2023 guideline published 2024), systematic review/meta-analyses (tuberculosis prevalence; tocilizumab outcomes; imaging SLR). (tian2024chineseguidelinefor pages 1-2, li2023prevalenceoftuberculosis pages 1-2, kang2023systematicreviewand pages 1-2, bosch2023imagingindiagnosis pages 1-2)
* **Individual/patient-level cohorts and trials:** multicenter French cohort (n=318), pediatric cohort (n=101), randomized trial extension (TAKT). (comarmond2017longtermoutcomesand pages 1-4, fan2019clinicalcourseand pages 1-2, nakaoka2020longtermefficacyand pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
The precise etiology remains incompletely defined, but TAK is strongly supported as an immune-mediated disease with both cellular and humoral immune components, featuring granulomatous arterial-wall inflammation that evolves into vascular remodeling. (bhandari2023pathophysiologydiagnosisand pages 3-4, as2023currentdiagnosisand pages 1-2)

### 2.2 Risk factors

#### 2.2.1 Demographic risk signals
TAK preferentially affects **young women** and is more common in Asian populations in multiple reviews/guidelines. (tian2024chineseguidelinefor pages 1-2, as2023currentdiagnosisand pages 1-2)

#### 2.2.2 Infectious association: tuberculosis (TB)
A 2023 meta-analysis of observational studies (30 studies; **n=5,548**) quantified TB burden among TAK patients:
* **Any TB infection prevalence:** **31.27%** (95% CI 20.48–43.11%)
* **Latent TB infection:** **50.01%** (95% CI 31.25–68.77%)
* **Active TB:** **14.40%** (95% CI 9.03–20.68%)
* Strong regional variation (e.g., **Western Pacific 16.93%** vs **African region 63.58%**). (li2023prevalenceoftuberculosis pages 1-2)

These data support the expert conclusion to consider “rigorous TB screening measures and preventive interventions specifically tailored for the TAK population.” (li2023prevalenceoftuberculosis pages 1-2)

#### 2.2.3 Genetic susceptibility (not monogenic)
A 2023 review describes TAK genetic susceptibility loci (e.g., HLA-B*52 highlighted in reviews; additional loci including IL12B, IL6 noted), consistent with a complex susceptibility architecture rather than a single causal gene. (bhandari2023pathophysiologydiagnosisand pages 8-9, as2023currentdiagnosisand pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were explicitly identified in the retrieved evidence; therefore, no protection claims are made here. (bhandari2023pathophysiologydiagnosisand pages 3-4)

### 2.4 Gene–environment interactions
The retrieved evidence supports an epidemiologic and mechanistic plausibility for infection-triggering hypotheses (e.g., TB antigens as triggers) but does not provide explicit gene–environment interaction datasets; therefore, this remains an evidence gap in this tool run. (as2023currentdiagnosisand pages 1-2, li2023prevalenceoftuberculosis pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with frequencies where available)
Pediatric data provide concrete phenotype frequencies. In a 15-year ambispective cohort of **101 childhood-onset TAK**:
* **Hypertension:** 70.3%
* **Blood pressure discrepancy:** 55.4%
* **Bruits:** 51.5%
* **Pulse deficits:** 37.6%
* Common arterial involvement: **renal artery 62.4%**, **subclavian artery 43.6%**, **abdominal aorta 42.6%**, **carotid artery 42.6%**. (fan2019clinicalcourseand pages 1-2)

Adult phenotypes are more variably described across cohorts, but ischemia-related manifestations (claudication, pulse inequality/loss, bruits) are consistently emphasized in reviews and guidelines. (tian2024chineseguidelinefor pages 1-2, as2023currentdiagnosisand pages 1-2)

### 3.2 Phenotype characteristics
* **Age of onset:** Often young (many <30) in the Chinese guideline narrative. (tian2024chineseguidelinefor pages 1-2)
* **Progression:** Reviews describe a staged progression from early inflammatory symptoms to vascular stenosis/occlusion (“pulseless disease”) and later fibrotic changes; delayed diagnosis is common because of non-specific early features. (bhandari2023pathophysiologydiagnosisand pages 3-4, as2023currentdiagnosisand pages 1-2)

### 3.3 Quality-of-life impact
The TAKT long-term extension study evaluated patient-reported outcomes via the SF-36 and reported clinically improved physical and mental component summary scores maintained over 96 weeks of tocilizumab treatment. (nakaoka2020longtermefficacyand pages 1-2)

### 3.4 Suggested HPO terms (examples)
* Constitutional: **Fever (HP:0001945)**, **Weight loss (HP:0001824)**
* Vascular/ischemic: **Claudication (HP:0004417)**, **Stroke (HP:0001297)**
* Vitals/exam: **Hypertension (HP:0000822)**, **Bruit (HP:0030407)**, **Absent pulses / pulse deficit (HP:0004403)**
* Cardiovascular sequelae (where present): **Aortic regurgitation (HP:0001659)**

(Phenotype frequencies are best supported by pediatric cohort data above; adult frequencies were not quantified in the retrieved evidence.) (fan2019clinicalcourseand pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
TAK is not supported as a single-gene (Mendelian) disorder in the retrieved evidence. Instead, susceptibility loci and immune pathway genes (e.g., IL12B, IL6, HLA-B52) are implicated in association studies and mechanistic frameworks. (bhandari2023pathophysiologydiagnosisand pages 8-9, as2023currentdiagnosisand pages 1-2)

### 4.2 Pathogenic variants / modifier genes / chromosomal abnormalities
No ClinVar/ACMG-style variant assertions, population allele frequencies (gnomAD), or chromosomal abnormalities were present in the retrieved sources. Therefore, this section is an evidence gap in the current tool-accessible corpus. (bhandari2023pathophysiologydiagnosisand pages 8-9)

### 4.3 Epigenetics
No TAK-specific methylation/histone evidence was present in retrieved sources. (misra2023arterialwallfibrosis pages 1-2)

---

## 5. Environmental Information

### 5.1 Infectious agents
**Mycobacterium tuberculosis** is the main infectious agent highlighted across recent review and meta-analysis literature as a potential trigger/association; the 2023 meta-analysis quantified TB prevalence in TAK (see Etiology). (li2023prevalenceoftuberculosis pages 1-2, as2023currentdiagnosisand pages 1-2)

### 5.2 Lifestyle/environmental factors
No specific toxins/lifestyle exposures were quantified as risk modifiers in the retrieved evidence; one review mentions non-pharmacologic measures (e.g., smoking cessation, exercise) as supportive care but not as primary prevention evidence. (bhandari2023pathophysiologydiagnosisand pages 7-8)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (immune-to-vascular damage causal chain)
A consistent causal chain from recent mechanistic reviews can be summarized as:
1) **Initiation at vasa vasorum / medio-adventitial junction** with immune activation → **panarteritis** and wall thickening. (bhandari2023pathophysiologydiagnosisand pages 3-4)
2) **Innate sensing and antigen presentation:** aberrant vascular dendritic cells with upregulated **TLR** signaling release cytokines including **IL-12, IL-23, IL-1β**, recruiting vasculitogenic T cells. (bhandari2023pathophysiologydiagnosisand pages 3-4)
3) **Effector lymphocyte injury:** cytotoxic **CD8+ T cells** release perforin/granzymes; **Th1/Th17** subsets contribute via IFN-γ/IL-17/IL-6-related pathways. (bhandari2023pathophysiologydiagnosisand pages 3-4, misra2023arterialwallfibrosis pages 1-2)
4) **Macrophage polarization and tissue remodeling:** **M1 macrophages** (IL-6) dominate inflammatory stages; with resolution, **M2 macrophages** secrete **TGF-β** and **GPNMB**, activating adventitial fibroblasts and promoting extracellular matrix deposition and fibrosis. (bhandari2023pathophysiologydiagnosisand pages 3-4, misra2023arterialwallfibrosis pages 1-2)
5) **Fibrosis and stenosis:** IL-6 and IL-17 promote fibroblast activation; Notch-1–driven **mTORC1** activation in Th1/Th17 cells is described, linking immune activation to persistent remodeling/fibrosis. (misra2023arterialwallfibrosis pages 1-2, bhandari2023pathophysiologydiagnosisand pages 3-4)

This chain provides a mechanistic rationale for targeting cytokines (IL-6; TNF), T-cell pathways, and JAK/STAT signaling and (in future) anti-fibrotic strategies. (misra2023arterialwallfibrosis pages 1-2, bhandari2023pathophysiologydiagnosisand pages 5-7)

### 6.2 Suggested GO biological process terms (examples)
* **Inflammatory response (GO:0006954)**
* **Cytokine-mediated signaling pathway (GO:0019221)**
* **Leukocyte migration (GO:0050900)**
* **Extracellular matrix organization (GO:0030198)**
* **Collagen fibril organization (GO:0030199)**

### 6.3 Suggested Cell Ontology (CL) terms (examples)
* **CD8-positive, alpha-beta T cell (CL:0000625)**
* **T helper 17 cell (CL:0000899)**
* **Macrophage (CL:0000235)**
* **Dendritic cell (CL:0000451)**
* **Mast cell (CL:0000097)**
* **Fibroblast (CL:0000057)** (including adventitial fibroblast concept) (misra2023arterialwallfibrosis pages 1-2)

### 6.4 Molecular profiling and advanced technologies
The retrieved evidence discusses molecular profiling and biomarkers as future directions but does not provide a specific single-cell/spatial multi-omics dataset in the accessible excerpts; thus, detailed omics signatures are not asserted here. (bhandari2023pathophysiologydiagnosisand pages 8-9, bhandari2023pathophysiologydiagnosisand pages 5-7)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary: **aorta and major branches** (large vessel vasculitis). (tian2024chineseguidelinefor pages 1-2, as2023currentdiagnosisand pages 1-2)

Common branch vessels (pediatric cohort frequencies): **renal artery**, **subclavian artery**, **carotid artery**, **abdominal aorta** involvement. (fan2019clinicalcourseand pages 1-2)

### 7.2 Suggested UBERON terms (examples)
* **Aorta (UBERON:0000947)**
* **Renal artery (UBERON:0001637)**
* **Subclavian artery (UBERON:0001516)**
* **Common carotid artery (UBERON:0001502)**

---

## 8. Temporal Development

### 8.1 Onset
TAK often begins insidiously with non-specific constitutional symptoms; one review reports a mean delay from symptom onset to diagnosis of ~1.3 years (SD ±0.6). (as2023currentdiagnosisand pages 1-2)

### 8.2 Progression/course
A staged concept (active/chronic/healing; or inflammatory to fibrotic progression) is described in reviews, aligning clinical phases with inflammatory activity and subsequent fibrosis. (bhandari2023pathophysiologydiagnosisand pages 3-4, bhandari2023pathophysiologydiagnosisand pages 5-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent numeric estimates from retrieved sources)
* Chinese guideline: annual incidence **~2.6 cases per million people worldwide**; “90% of patients are younger than 30 at disease onset” (as stated in the guideline introduction). (tian2024chineseguidelinefor pages 1-2)
* Review: incidence broadly reported **~1.11 per million person-years**. (as2023currentdiagnosisand pages 1-2)
* Global frequency range (review): **3.2–40.0 cases per million**. (bhandari2023pathophysiologydiagnosisand pages 3-4)

### 9.2 Sex ratio
Female predominance is consistent:
* French multicenter cohort: **86.8% women** (276/318). (comarmond2017longtermoutcomesand pages 1-4)
* Pediatric cohort: **76.2% female**. (fan2019clinicalcourseand pages 1-2)

### 9.3 Inheritance pattern
The retrieved evidence supports complex susceptibility (e.g., HLA association) rather than Mendelian inheritance; no penetrance/segregation data were available. (as2023currentdiagnosisand pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria / classification
The 2022 ACR/EULAR classification criteria incorporate **imaging characteristics as an absolute requirement** (key recent change). (as2023currentdiagnosisand pages 1-2)

Disease activity assessment approaches in the Chinese guideline include Kerr criteria and ITAS2010/ITAS-A thresholds (e.g., ITAS2010 ≥2; ITAS-A ≥5 for active disease). (tian2024chineseguidelinefor pages 6-7)

### 10.2 Laboratory biomarkers
ESR and CRP are widely used but have limited accuracy for disease activity; pentraxin-3 (PTX3) is described as “relatively superior” and correlating with ITAS2010 in several studies (per review). (as2023currentdiagnosisand pages 1-2)

Other candidate biomarkers mentioned as promising but requiring validation include anti-endothelial cell antibodies, VEGF, IL-6, IL-8, and PTX3. (bhandari2023pathophysiologydiagnosisand pages 5-7)

### 10.3 Imaging
Current imaging principles in retrieved sources include:
* **CTA** often recommended as an initial diagnostic imaging modality for availability and resolution (review). (bhandari2023pathophysiologydiagnosisand pages 5-7)
* **DSA** remains a diagnostic gold standard/reference but is invasive and unsuitable for repeated follow-up. (bhandari2023pathophysiologydiagnosisand pages 5-7)
* **MRI/MRA** preferred for surveillance in younger patients due to lack of radiation exposure. (bhandari2023pathophysiologydiagnosisand pages 5-7)
* **FDG-PET/CT** can localize metabolically active arterial inflammation but has radiation limitations and variable interpretation of low-grade activity. (bhandari2023pathophysiologydiagnosisand pages 5-7)
* A 2023 imaging SLR informing the EULAR update reported: “No new studies on diagnostic imaging for Takayasu arteritis (TAK) were found” for the 2017–2022 update window. (bosch2023imagingindiagnosis pages 1-2)

The Chinese guideline provides an algorithmic diagnostic/treatment pathway (Figure 1). (tian2024chineseguidelinefor media 1be88471)

### 10.4 Suggested LOINC-style lab signals (examples)
Not formally mapped in retrieved texts; typical monitoring includes ESR and CRP. (bhandari2023pathophysiologydiagnosisand pages 7-8, as2023currentdiagnosisand pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Adult outcomes (multicenter cohort)
In a French nationwide multicenter study (n=318; median follow-up 6.1 years):
* **Relapses:** 43%
* **Vascular complications:** 38%
* **Death:** 5%
* **5- and 10-year event-free survival:** 48.2% and 36.4%
* **5- and 10-year relapse-free survival:** 58.6% and 47.7%
* **5- and 10-year complication-free survival:** 69.9% and 53.7% (comarmond2017longtermoutcomesand pages 1-4)

Risk factors highlighted included progressive disease course and carotidodynia for worse EFS; male sex, elevated CRP, carotidodynia for relapse; thoracic aorta involvement and retinopathy for vascular complications. (comarmond2017longtermoutcomesand pages 1-4)

### 11.2 Pediatric outcomes
In childhood-onset TAK (n=101; median follow-up 2.4 years): events 44.6%, vascular complications 44.6%, flares 26.7%, death 3%; 5-year event-free survival 42.8%. (fan2019clinicalcourseand pages 1-2)

---

## 12. Treatment

### 12.1 Standard-of-care concepts
Across reviews and guidelines, **glucocorticoids plus steroid-sparing immunosuppressants** are emphasized, with biologics for refractory disease and revascularization procedures for critical lesions once inflammation is controlled. (bhandari2023pathophysiologydiagnosisand pages 7-8, tian2024chineseguidelinefor pages 1-2, bhandari2023pathophysiologydiagnosisand pages 5-7)

### 12.2 csDMARDs / immunosuppressants (examples)
Commonly referenced agents include methotrexate, azathioprine, mycophenolate mofetil, leflunomide, cyclophosphamide. (bhandari2023pathophysiologydiagnosisand pages 5-7, bhandari2023pathophysiologydiagnosisand pages 7-8)

### 12.3 Biologics and targeted therapy (key recent evidence)

#### Tocilizumab (IL-6R blockade)
A 2023 meta-analysis (19 studies, 466 refractory TAK patients) reported:
* **Remission rate:** 79% (95% CI 69–86%)
* **Relapse rate:** 17% (95% CI 5–45%)
* **Imaging progression:** 16% (95% CI 9–27%)
* **Retention rate:** 68% (95% CI 50–82%)
* **Adverse events:** 16% (infection 12%)
* ~76% achieved glucocorticoid dose reduction (kang2023systematicreviewand pages 1-2)

The TAKT randomized trial long-term extension (up to 96 weeks) showed steroid-sparing with median glucocorticoid dose decreasing from 0.223 mg/kg/day (pre-entry relapse) to 0.131 at 48 weeks and 0.105 at 96 weeks; 46.4% reduced to <0.1 mg/kg/day; imaging mostly stable/improved (improved 17.9%, stable 67.9%). (nakaoka2020longtermefficacyand pages 1-2)

#### TNF inhibitors
TNF inhibitors (e.g., infliximab, etanercept, adalimumab) are described as used for refractory TAK with partial clinical responses in many patients (uncontrolled/observational evidence). (bhandari2023pathophysiologydiagnosisand pages 5-7)

#### JAK inhibitors (emerging)
Recent guideline/review material notes JAK inhibitors as potentially effective and increasingly used/considered for refractory disease, but acknowledges limited controlled evidence and the need for careful safety consideration. (arita2024currentimmunosuppressivetreatment pages 5-5)

### 12.4 Interventional/surgical management
Revascularization (endovascular or open surgery) is used for critical symptomatic stenoses; guidance emphasizes delaying interventions until disease activity is controlled and performing procedures in specialized centers. (bhandari2023pathophysiologydiagnosisand pages 7-8)

### 12.5 Experimental/ongoing clinical trials (selected)
ClinicalTrials.gov records retrieved in this run include:
* **Tocilizumab in TAK:** **NCT02101333** (completed) (NCT02101333 chunk 2)
* **Baricitinib for refractory TAK:** **NCT06662721** (completed; phase 2) (clinical trial listing retrieved in tool run; see overall trial set) (NCT04300686 chunk 3)
* **Ustekinumab:** **NCT04882072** (terminated; phase 3) (NCT04882072 chunk 4)
* **Biologic withdrawal in sustained remission:** **NCT07491913** (recruiting) (NCT07491913 chunk 2)

### 12.6 Suggested MAXO terms (examples)
* **Glucocorticoid therapy** (e.g., prednisone) (bhandari2023pathophysiologydiagnosisand pages 7-8)
* **Interleukin-6 receptor inhibitor therapy** (tocilizumab) (kang2023systematicreviewand pages 1-2, nakaoka2020longtermefficacyand pages 1-2)
* **TNF inhibitor therapy** (infliximab/adalimumab) (bhandari2023pathophysiologydiagnosisand pages 5-7)
* **Endovascular angioplasty / vascular revascularization procedure** (bhandari2023pathophysiologydiagnosisand pages 7-8)

---

## 13. Prevention

### 13.1 Primary prevention
No established primary prevention strategy exists in the retrieved evidence.

### 13.2 Secondary/tertiary prevention
Given high TB prevalence in TAK populations and the immunosuppressive treatment context, TB screening and preventive strategies are strongly supported by the 2023 meta-analysis conclusion. (li2023prevalenceoftuberculosis pages 1-2)

Tertiary prevention includes aggressive control of inflammation to prevent stenosis/aneurysm complications and procedure timing during inactive disease. (bhandari2023pathophysiologydiagnosisand pages 7-8)

---

## 14. Other Species / Natural Disease
No naturally occurring TAK analog in non-human species was identified in the retrieved sources. This section is an evidence gap for this tool run. (misra2023arterialwallfibrosis pages 1-2)

---

## 15. Model Organisms
The retrieved sources reference experimental/“in vitro” mechanistic findings relevant to fibrosis modulation but do not provide a specific, well-validated animal model description in the accessible excerpts; therefore, model organism details are not asserted here. (misra2023arterialwallfibrosis pages 1-2)

---

## Key recent (2023–2024) developments (high-level synthesis)
1) **Classification/diagnostics shifting toward imaging**: 2022 ACR/EULAR criteria require imaging; imaging-centric pathways are emphasized in guidelines and reviews. (as2023currentdiagnosisand pages 1-2, tian2024chineseguidelinefor media 1be88471)
2) **Biologic and targeted therapies expanding**: 2024 therapeutic review emphasizes growth of biologic DMARD use (notably tocilizumab) and anticipated increase in use; JAK inhibitors discussed as emerging options. (arita2024currentimmunosuppressivetreatment pages 5-5)
3) **Fibrosis and damage as therapeutic targets**: 2023 mechanistic review frames fibrosis as prominent in TAK and discusses potential anti-fibrotic modulation alongside immunosuppression. (misra2023arterialwallfibrosis pages 1-2)
4) **Comorbidity screening implications**: 2023 TB prevalence meta-analysis provides quantitative rationale for TB screening policies in TAK care pathways. (li2023prevalenceoftuberculosis pages 1-2)

---

## Summary table (artifact)
The following table consolidates key quantitative facts and sources extracted in this run.

| Domain | Key points (with numbers) | Key sources (PMID/DOI/URL when available) |
|---|---|---|
| Core definition / overview | Chronic granulomatous large-vessel vasculitis involving the aorta and major branches; causes wall thickening, stenosis/occlusion, aneurysm formation, and ischemic complications; often affects young women, especially in Asia (tian2024chineseguidelinefor pages 1-2, as2023currentdiagnosisand pages 1-2) | Chinese guideline 2024, doi:10.1515/rir-2024-0002, https://doi.org/10.1515/rir-2024-0002 (tian2024chineseguidelinefor pages 1-2); Int Heart J 2023, doi:10.1536/ihj.23-195, https://doi.org/10.1536/ihj.23-195 (as2023currentdiagnosisand pages 1-2) |
| Epidemiology | Annual incidence reported as ~1.11 per million person-years in one review; worldwide annual incidence ~2.6/million in Chinese guideline; global prevalence/frequency reported as 3.2–40.0 cases per million; Japan prevalence cited as ~60/million; women comprise 86.8% in a 318-patient multicenter cohort; childhood cohort 76.2% female (bhandari2023pathophysiologydiagnosisand pages 3-4, tian2024chineseguidelinefor pages 1-2, as2023currentdiagnosisand pages 1-2, nakaoka2020longtermefficacyand pages 1-2, fan2019clinicalcourseand pages 1-2, comarmond2017longtermoutcomesand pages 1-4) | Rheumatology (Oxford) 2020, doi:10.1093/rheumatology/kez630, https://doi.org/10.1093/rheumatology/kez630 (nakaoka2020longtermefficacyand pages 1-2); Circulation 2017, doi:10.1161/CIRCULATIONAHA.116.027094, https://doi.org/10.1161/CIRCULATIONAHA.116.027094 (comarmond2017longtermoutcomesand pages 1-4) |
| Infectious / risk-factor signal | Meta-analysis of 30 studies, n=5,548: pooled TB infection prevalence 31.27% (95% CI 20.48–43.11%); latent TB 50.01% (31.25–68.77%); active TB 14.40% (9.03–20.68%); African Region 63.58% vs Western Pacific 16.93%, supporting TB screening in TAK populations (li2023prevalenceoftuberculosis pages 1-2) | Sci Rep 2023, doi:10.1038/s41598-023-49998-y, https://doi.org/10.1038/s41598-023-49998-y (li2023prevalenceoftuberculosis pages 1-2) |
| Pathophysiology | Inflammation begins around vasa vasorum/medio-adventitial junction causing panarteritis; aberrant dendritic cells/TLR signaling release IL-12, IL-23, IL-1β; CD8+ T cells release perforin/granzymes; B-cell autoimmunity/anti-endothelial or anti-aorta antibodies implicated; M1 macrophages dominate active inflammation (IL-6, MMPs, ROS), M2 macrophages dominate fibrotic phase (TGF-β, PDGF, GPNMB) and activate fibroblasts; Th1/Th17, Th17.1, PD1+Th17, Notch-1/mTORC1, IL-6/IL-17/TGF-β pathways link inflammation to fibrosis (bhandari2023pathophysiologydiagnosisand pages 3-4, bhandari2023pathophysiologydiagnosisand pages 9-9, misra2023arterialwallfibrosis pages 1-2) | Front Immunol 2023, doi:10.3389/fimmu.2023.1174249, https://doi.org/10.3389/fimmu.2023.1174249 (misra2023arterialwallfibrosis pages 1-2); Cureus 2023, doi:10.7759/cureus.42667, https://doi.org/10.7759/cureus.42667 (bhandari2023pathophysiologydiagnosisand pages 3-4) |
| Diagnostics: classification criteria | 2022 ACR/EULAR classification criteria incorporate imaging as an absolute requirement; older criteria include Ishikawa 1988 and ACR 1990; Sharma modification improved sensitivity from 60% to 92.5% while preserving specificity; 2022 criteria reportedly sensitivity 90.5% and specificity 98.3% in DCVAS-related comparison vs ACR 1990 sensitivity 73.6% and specificity 97.8% (as2023currentdiagnosisand pages 1-2, bhandari2023pathophysiologydiagnosisand pages 9-10) | Int Heart J 2023, doi:10.1536/ihj.23-195, https://doi.org/10.1536/ihj.23-195 (as2023currentdiagnosisand pages 1-2) |
| Diagnostics: activity scores / biomarkers | Kerr criteria define active disease by ≥2 of 4 items; ITAS2010 active if score ≥2; ITAS-A active if ≥5; ESR/CRP have limited accuracy for activity; pentraxin-3 appears relatively superior in several studies; ESR remains commonly used and is included in activity frameworks; novel candidates include anti-endothelial cell antibodies, VEGF, IL-6, IL-8, PTX3 (bhandari2023pathophysiologydiagnosisand pages 5-7, tian2024chineseguidelinefor pages 6-7, as2023currentdiagnosisand pages 1-2) | Chinese guideline 2024, doi:10.1515/rir-2024-0002, https://doi.org/10.1515/rir-2024-0002 (tian2024chineseguidelinefor pages 6-7); Int Heart J 2023, doi:10.1536/ihj.23-195, https://doi.org/10.1536/ihj.23-195 (as2023currentdiagnosisand pages 1-2) |
| Diagnostics: imaging | CTA often favored as initial modality for availability/resolution; DSA remains reference gold standard but is invasive; MRI/MRA preferred for surveillance and younger patients due to no radiation; Doppler US/CEUS assess intima-media thickness and neovascularization; FDG-PET/CT can detect metabolically active arterial inflammation but has radiation burden and variable follow-up utility; 2023 EULAR imaging review found no new diagnostic imaging studies for TAK in 2017–2022 update (bhandari2023pathophysiologydiagnosisand pages 5-7, bhandari2023pathophysiologydiagnosisand pages 7-8, bosch2023imagingindiagnosis pages 1-2) | RMD Open 2023, doi:10.1136/rmdopen-2023-003379, https://doi.org/10.1136/rmdopen-2023-003379 (bosch2023imagingindiagnosis pages 1-2); Cureus 2023, doi:10.7759/cureus.42667, https://doi.org/10.7759/cureus.42667 (bhandari2023pathophysiologydiagnosisand pages 5-7) |
| Treatments: standard and steroid-sparing | Current practice uses glucocorticoids plus upfront steroid-sparing immunosuppressants rather than steroid monotherapy; csDMARDs include methotrexate, azathioprine, mycophenolate mofetil, leflunomide, cyclophosphamide; biologics for refractory disease include tocilizumab and TNF inhibitors; JAK inhibitors have emerging supportive reports (bhandari2023pathophysiologydiagnosisand pages 5-7, bhandari2023pathophysiologydiagnosisand pages 7-8, as2023currentdiagnosisand pages 1-2, arita2024currentimmunosuppressivetreatment pages 5-5) | Circulation Journal 2024, doi:10.1253/circj.cj-23-0780, https://doi.org/10.1253/circj.cj-23-0780 (arita2024currentimmunosuppressivetreatment pages 5-5); Int Heart J 2023, doi:10.1536/ihj.23-195, https://doi.org/10.1536/ihj.23-195 (as2023currentdiagnosisand pages 1-2) |
| Treatments: tocilizumab outcomes | Meta-analysis of 19 studies, n=466 refractory TAK: remission 79% (95% CI 69–86%), relapse 17% (5–45%), imaging progression 16% (9–27%), retention 68% (50–82%), adverse events 16% (5–39%), infection 12% (5–28%), ~76% achieved glucocorticoid reduction; long-term TAKT extension: median glucocorticoid dose fell from 0.223 mg/kg/day pre-entry relapse to 0.131 at 48 weeks and 0.105 at 96 weeks; 46.4% reduced to <0.1 mg/kg/day; imaging improved in 17.9% and stable in 67.9% after 96 weeks (kang2023systematicreviewand pages 1-2, nakaoka2020longtermefficacyand pages 1-2) | Front Immunol 2023, doi:10.3389/fimmu.2023.1084558, https://doi.org/10.3389/fimmu.2023.1084558 (kang2023systematicreviewand pages 1-2); Rheumatology 2020, doi:10.1093/rheumatology/kez630, https://doi.org/10.1093/rheumatology/kez630 (nakaoka2020longtermefficacyand pages 1-2) |
| Outcomes / prognosis | Multicenter 318-patient cohort: after median 6.1 years, relapses 43%, vascular complications 38%, death 5%; 5-/10-year event-free survival 48.2%/36.4%, relapse-free survival 58.6%/47.7%, complication-free survival 69.9%/53.7%; childhood cohort (n=101): events 44.6%, rehospitalization 37.6%, vascular complications 44.6%, flares 26.7%, death 3% at median 2.4 years; 5-year event-free survival 42.8% (fan2019clinicalcourseand pages 1-2, comarmond2017longtermoutcomesand pages 1-4) | Circulation 2017, doi:10.1161/CIRCULATIONAHA.116.027094, https://doi.org/10.1161/CIRCULATIONAHA.116.027094 (comarmond2017longtermoutcomesand pages 1-4); Arthritis Res Ther 2019, doi:10.1186/s13075-018-1790-x, https://doi.org/10.1186/s13075-018-1790-x (fan2019clinicalcourseand pages 1-2) |


*Table: This table condenses the main evidence already retrieved in the chat on Takayasu arteritis, including definition, epidemiology, mechanisms, diagnosis, treatment, and prognosis. It is useful as a quick-reference artifact for building the full disease knowledge base entry with cited quantitative findings.*

---

## Visual evidence (guideline pathway)
The Chinese guideline includes a diagnosis-and-treatment algorithm figure.

(tian2024chineseguidelinefor media 1be88471)

---

## Limitations of this report (due to tool-accessible corpus)
* **MONDO / Orphanet / OMIM / ICD-11 identifiers** were not explicitly present in the retrieved texts and trial record chunks; they are therefore not asserted.
* **Variant-level genetics (ClinVar/ACMG), epigenetics, and detailed omics signatures** were not available in retrieved excerpts.
* Some requested items (e.g., model organisms, other species) were not covered by accessible sources in this run.



References

1. (tian2024chineseguidelinefor pages 1-2): Xinping Tian and Xiaofeng Zeng. Chinese guideline for the diagnosis and treatment of takayasu’s arteritis (2023). Rheumatology and Immunology Research, 5:5-26, Mar 2024. URL: https://doi.org/10.1515/rir-2024-0002, doi:10.1515/rir-2024-0002. This article has 14 citations.

2. (as2023currentdiagnosisand pages 1-2): Chandhu AS and Debashish Danda. Current diagnosis and management of takayasu arteritis. International heart journal, 64 4:519-534, Jul 2023. URL: https://doi.org/10.1536/ihj.23-195, doi:10.1536/ihj.23-195. This article has 14 citations and is from a peer-reviewed journal.

3. (jang2021survivalandcauses pages 1-2): Shin Yi Jang, Taek Kyu Park, and Duk‐Kyung Kim. Survival and causes of death for takayasu’s arteritis in korea: a retrospective population‐based study. International Journal of Rheumatic Diseases, 24:69-73, Oct 2021. URL: https://doi.org/10.1111/1756-185x.14005, doi:10.1111/1756-185x.14005. This article has 24 citations and is from a peer-reviewed journal.

4. (NCT07491913 chunk 2): Fatma Alibaz Oner. Biologic Treatment Withdrawal in Takayasu Arteritis Patients in Sustained Remission. Marmara University. 2025. ClinicalTrials.gov Identifier: NCT07491913

5. (NCT02101333 chunk 2):  Efficacy and Tolerance of Tocilizumab In Takayasu Arteritis. Assistance Publique - Hôpitaux de Paris. 2014. ClinicalTrials.gov Identifier: NCT02101333

6. (NCT04882072 chunk 4):  A Study of Ustekinumab in Participants With Takayasu Arteritis (TAK). Janssen Pharmaceutical K.K.. 2021. ClinicalTrials.gov Identifier: NCT04882072

7. (NCT02101333 chunk 3):  Efficacy and Tolerance of Tocilizumab In Takayasu Arteritis. Assistance Publique - Hôpitaux de Paris. 2014. ClinicalTrials.gov Identifier: NCT02101333

8. (li2023prevalenceoftuberculosis pages 1-2): Liping Li, Fang Zhou, Fen Li, Jinwei Chen, and Xi Xie. Prevalence of tuberculosis infection among patients with takayasu arteritis: a meta-analysis of observational studies. Scientific Reports, Dec 2023. URL: https://doi.org/10.1038/s41598-023-49998-y, doi:10.1038/s41598-023-49998-y. This article has 10 citations and is from a peer-reviewed journal.

9. (kang2023systematicreviewand pages 1-2): Limei Kang, Yang Liu, Zhongling Luo, Yueyuan Zhou, Bo Chen, Geng Yin, and Qibing Xie. Systematic review and meta-analysis of the current literature on tocilizumab in patients with refractory takayasu arteritis. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1084558, doi:10.3389/fimmu.2023.1084558. This article has 15 citations and is from a peer-reviewed journal.

10. (bosch2023imagingindiagnosis pages 1-2): Philipp Bosch, Milena Bond, Christian Dejaco, Cristina Ponte, Sarah Louise Mackie, Louise Falzon, Wolfgang A Schmidt, and Sofia Ramiro. Imaging in diagnosis, monitoring and outcome prediction of large vessel vasculitis: a systematic literature review and meta-analysis informing the 2023 update of the eular recommendations. RMD Open, 9:e003379, Aug 2023. URL: https://doi.org/10.1136/rmdopen-2023-003379, doi:10.1136/rmdopen-2023-003379. This article has 108 citations and is from a peer-reviewed journal.

11. (comarmond2017longtermoutcomesand pages 1-4): Cloé Comarmond, Lucie Biard, Marc Lambert, Arsène Mekinian, Yasmina Ferfar, Jean-Emmanuel Kahn, Ygal Benhamou, Laurent Chiche, Fabien Koskas, Philippe Cluzel, Eric Hachulla, Emmanuel Messas, Matthieu Resche-Rigon, Patrice Cacoub, Tristan Mirault, and David Saadoun. Long-term outcomes and prognostic factors of complications in takayasu arteritis: a multicenter study of 318 patients. Circulation, 136:1114–1122, Sep 2017. URL: https://doi.org/10.1161/circulationaha.116.027094, doi:10.1161/circulationaha.116.027094. This article has 278 citations and is from a highest quality peer-reviewed journal.

12. (fan2019clinicalcourseand pages 1-2): Luyun Fan, Huimin Zhang, Jun Cai, Lirui Yang, Bin Liu, Dongmei Wei, Jiachen Yu, Jiali Fan, Lei Song, Wenjun Ma, Xianliang Zhou, Haiying Wu, and Ying Lou. Clinical course and prognostic factors of childhood takayasu’s arteritis: over 15-year comprehensive analysis of 101 patients. Arthritis Research & Therapy, Jan 2019. URL: https://doi.org/10.1186/s13075-018-1790-x, doi:10.1186/s13075-018-1790-x. This article has 70 citations and is from a domain leading peer-reviewed journal.

13. (nakaoka2020longtermefficacyand pages 1-2): Yoshikazu Nakaoka, Mitsuaki Isobe, Yoshiya Tanaka, Tomonori Ishii, Seido Ooka, Hiroaki Niiro, Naoto Tamura, Shogo Banno, Hajime Yoshifuji, Yasushi Sakata, Atsushi Kawakami, Tatsuya Atsumi, Shunsuke Furuta, Hitoshi Kohsaka, Katsuya Suzuki, Ryoki Hara, Yasuhiro Maejima, Hiroshi Tsukamoto, Yoshinari Takasaki, Katsuhisa Yamashita, Norihiro Okada, Shinji Yamakido, Syuji Takei, Shumpei Yokota, and Norihiro Nishimoto. Long-term efficacy and safety of tocilizumab in refractory takayasu arteritis: final results of the randomized controlled phase 3 takt study. Rheumatology (Oxford, England), 59:2427-2434, Jan 2020. URL: https://doi.org/10.1093/rheumatology/kez630, doi:10.1093/rheumatology/kez630. This article has 128 citations.

14. (bhandari2023pathophysiologydiagnosisand pages 3-4): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.

15. (bhandari2023pathophysiologydiagnosisand pages 8-9): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.

16. (misra2023arterialwallfibrosis pages 1-2): Durga Prasanna Misra, Kritika Singh, Aman Sharma, and Vikas Agarwal. Arterial wall fibrosis in takayasu arteritis and its potential for therapeutic modulation. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1174249, doi:10.3389/fimmu.2023.1174249. This article has 31 citations and is from a peer-reviewed journal.

17. (bhandari2023pathophysiologydiagnosisand pages 7-8): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.

18. (bhandari2023pathophysiologydiagnosisand pages 5-7): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.

19. (tian2024chineseguidelinefor pages 6-7): Xinping Tian and Xiaofeng Zeng. Chinese guideline for the diagnosis and treatment of takayasu’s arteritis (2023). Rheumatology and Immunology Research, 5:5-26, Mar 2024. URL: https://doi.org/10.1515/rir-2024-0002, doi:10.1515/rir-2024-0002. This article has 14 citations.

20. (tian2024chineseguidelinefor media 1be88471): Xinping Tian and Xiaofeng Zeng. Chinese guideline for the diagnosis and treatment of takayasu’s arteritis (2023). Rheumatology and Immunology Research, 5:5-26, Mar 2024. URL: https://doi.org/10.1515/rir-2024-0002, doi:10.1515/rir-2024-0002. This article has 14 citations.

21. (arita2024currentimmunosuppressivetreatment pages 5-5): Yoh Arita, Tomohiko Ishibashi, and Yoshikazu Nakaoka. Current immunosuppressive treatment for takayasu arteritis. Circulation Journal, 88:1605-1609, Sep 2024. URL: https://doi.org/10.1253/circj.cj-23-0780, doi:10.1253/circj.cj-23-0780. This article has 11 citations and is from a peer-reviewed journal.

22. (NCT04300686 chunk 3):  A Pilot Study in Severe Patients With Takayasu Arteritis.. Shanghai Zhongshan Hospital. 2020. ClinicalTrials.gov Identifier: NCT04300686

23. (bhandari2023pathophysiologydiagnosisand pages 9-9): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.

24. (bhandari2023pathophysiologydiagnosisand pages 9-10): Sagar Bhandari, Samia Rauf R Butt, Anzal Ishfaq, Mohamed H Attaallah, Chukwuyem Ekhator, Raghu Halappa Nagaraj, Asmita Mulmi, Muhammad Kamran, Amanda Karski, Karla I Vargas, Slobodan Lazarevic, Mohammad Uzair Zaman, Gautham Lakshmipriya Vetrivendan, S M Iram Shahzed, Archana Das, Vikas Yadav, Sophia B Bellegarde, and Ashraf Ullah. Pathophysiology, diagnosis, and management of takayasu arteritis: a review of current advances. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.42667, doi:10.7759/cureus.42667. This article has 57 citations.