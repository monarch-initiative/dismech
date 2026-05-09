---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T07:58:45.985580'
end_time: '2026-05-06T08:07:56.312063'
duration_seconds: 550.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile Temporal Arteritis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Temporal Arteritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Juvenile Temporal Arteritis** covering all of the
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
- **Disease Name:** Juvenile Temporal Arteritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Juvenile Temporal Arteritis** covering all of the
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


# Juvenile Temporal Arteritis (JTA): Disease Characteristics Research Report (2024 update)

## 1. Disease information

### 1.1 Overview (current understanding)
Juvenile temporal arteritis (JTA) is a rare, localized vasculitis/arteritis confined to the superficial temporal artery (STA) and its branches, characterized most often by non-granulomatous, eosinophil-rich panarteritis and intimal hyperplasia that presents clinically as temporal nodules or a temporal “lump,” usually without systemic symptoms. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

Direct abstract support (2024 systematic review): “Juvenile Temporal Arteritis (JTA) is a rare non-granulomatous vasculitis affecting the superficial temporal arteries, mostly in individuals under 45 years old.” (Published online 2024-08-24; DOI: https://doi.org/10.1007/s00296-024-05624-2) (marquessoares2024bilateraljuveniletemporal pages 1-2)

Direct abstract support (2019 multicenter series): “Juvenile temporal arteritis (JTA) is a recently-described and little-known inflammatory disease and its etiology is undetermined. Less than forty cases have been published.” (Available online 2019-03-04; DOI: https://doi.org/10.1016/j.autrev.2019.03.007) (journeau2019juveniletemporalarteritis pages 1-2)

### 1.2 Key identifiers and terminology
- **Preferred name:** Juvenile temporal arteritis (JTA). (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)
- **Common synonym(s):** juvenile temporal vasculitis (used in case literature). (durant2011juveniletemporalvasculitis pages 1-2)
- **Orphanet:** Juvenile temporal arteritis **Orphanet:26137** (as cited by Marques-Soares et al., 2024; accessed 2024-04-26). URL: https://www.orpha.net/en/disease/detail/26137 (marquessoares2024bilateraljuveniletemporal pages 8-9)
- **GARD (NIH):** juvenile temporal arteritis (cited as a reference/resource by Marques-Soares et al., 2024; accessed 2024-04-26). URL: https://rarediseases.info.nih.gov/diseases/3068/index (marquessoares2024bilateraljuveniletemporal pages 8-9)
- **MONDO / MeSH / ICD-10/ICD-11 / OMIM:** Not identified in the retrieved full-text evidence. The 2024 review explicitly notes that comprehensive hereditary data are lacking, consistent with JTA being primarily defined clinicopathologically rather than genetically. (marquessoares2024bilateraljuveniletemporal pages 1-2)

### 1.3 Evidence type note
Most knowledge about JTA comes from **aggregated disease-level synthesis of case reports/series** (e.g., systematic reviews, multicenter clinicopathologic series), rather than population cohorts or EHR-scale studies. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors
The etiology of JTA remains **undetermined/unknown** in major reviews/series. (journeau2019juveniletemporalarteritis pages 1-2)

### 2.2 Risk factors
Evidence supports demographic and laboratory correlates more than causal risk factors:
- **Age:** typically young adults/“under 45–50.” (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)
- **Sex:** male predominance reported across aggregated case data (e.g., 77.3% male in a 44-patient combined cohort+literature dataset). (journeau2019juveniletemporalarteritis pages 1-2)
- **Eosinophilia / IgE:** peripheral blood eosinophilia is common in subsets and may point toward overlap with eosinophil-associated conditions (see §6). (journeau2019juveniletemporalarteritis pages 1-2, marquessoares2024bilateraljuveniletemporal pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interactions were identified in the retrieved evidence.

## 3. Phenotypes (with ontology suggestions)

### 3.1 Core clinical phenotype (from largest clinicopathologic aggregation)
In the 44-patient synthesis (12 French cases + 32 literature), all patients presented “either a lump in the temporal region or prominent temporal arteries,” and **47.7%** had headache; **11.4%** had general symptoms. (journeau2019juveniletemporalarteritis pages 1-2)

### 3.2 Phenotype list with suggested HPO terms
Below are phenotype items supported by retrieved evidence:
- **Temporal lump / temporal nodules (often unilateral; sometimes bilateral)**
  - Evidence: temporal lump 72.7% in 44-patient dataset; bilateral involvement 25.0% at presentation in that dataset; the 2024 bilateral-focused review emphasizes frequent bilateral disease in that selected subset. (journeau2019juveniletemporalarteritis pages 1-2, marquessoares2024bilateraljuveniletemporal pages 7-8)
  - HPO suggestions: **HP:0002056** (Subcutaneous nodule), **HP:0025464** (Mass), **HP:0100259** (Localized swelling).
- **Headache / temporal headache**
  - Evidence: 47.7% headache in the 44-patient dataset; ~28.6% in the bilateral-case subset analyzed by Marques-Soares et al. (journeau2019juveniletemporalarteritis pages 1-2, marquessoares2024bilateraljuveniletemporal pages 6-7)
  - HPO suggestions: **HP:0002315** (Headache).
- **Temporal artery tenderness / pain in temple region**
  - Evidence: painful nodules reported; “not particularly painful” is typical in the image-gallery case description but painful cases exist. (espitia2018imagegallerybilateral pages 1-1, marquessoares2024bilateraljuveniletemporal pages 7-8)
  - HPO suggestions: **HP:0030834** (Scalp tenderness), **HP:0012531** (Pain).
- **Pruritus (temporal itching)**
  - Evidence: temporal itching in 11.4% (4/35) in the 2019 compilation. (journeau2019juveniletemporalarteritis pages 1-2)
  - HPO suggestions: **HP:0000989** (Pruritus).
- **Visual symptoms (rare): visual blurring/phosphenes**
  - Evidence: 9.8% in 2019 compilation. (journeau2019juveniletemporalarteritis pages 1-2)
  - HPO suggestions: **HP:0000648** (Blurred vision), **HP:0001109** (Photopsia).
- **Attenuated temporal pulse / local ischemic signs**
  - Evidence: attenuated temporal pulse in the 2024 case report. (marquessoares2024bilateraljuveniletemporal pages 2-4)
  - HPO suggestions: **HP:0005305** (Decreased peripheral pulses).
- **Occasional systemic symptoms (malaise/fatigue/fever)**
  - Evidence: general symptoms 11.4% in 2019 compilation; bilateral-case subset described systemic involvement 22.2% in that selected set. (journeau2019juveniletemporalarteritis pages 1-2, marquessoares2024bilateraljuveniletemporal pages 7-8)
  - HPO suggestions: **HP:0012378** (Fatigue), **HP:0001945** (Fever).

### 3.3 Quality of life impact
Formal QoL instruments (e.g., SF-36/EQ-5D) were not reported in the retrieved evidence. Clinically, the primary burden appears to be local pain, cosmetic/structural temporal nodules, and diagnostic uncertainty (misdiagnosis leading to unnecessary testing/overtreatment). (marquessoares2024bilateraljuveniletemporal pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
No causal genes, pathogenic variants, or inherited patterns were identified in the retrieved primary literature. The 2024 review states that, given rarity, “comprehensive data on the hereditary patterns of JTA is lacking.” (marquessoares2024bilateraljuveniletemporal pages 1-2)

### 4.2 Modifier genes / epigenetics / chromosomal abnormalities
Not reported in retrieved evidence.

## 5. Environmental information

No specific environmental exposures, lifestyle factors, or infectious triggers were identified as established contributors in the retrieved evidence. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

## 6. Mechanism / pathophysiology

### 6.1 Clinicopathologic concept
JTA is generally modeled as a **localized eosinophil-rich panarteritis** of the STA with **intimal hyperplasia/proliferation**, **disruption of the internal elastic lamina (IEL)**, and variable thrombosis/microaneurysmal changes; it differs from classic giant cell arteritis (GCA) by typical absence/minimal systemic inflammation and rare/absent giant cells and granulomas. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2, nesher2009vasculitisofthe pages 2-4)

### 6.2 Immune cell involvement (human pathology)
- In the 2019 combined dataset, arterial-wall inflammatory infiltrate occurred in **97.6%**; perivascular extension in **82.6%**; lymphoid follicles/germinal centers in **60%**; “sparse giant cells” in **25%** and granuloma in **22.9%** (indicating giant cells can occur but are not defining). (journeau2019juveniletemporalarteritis pages 1-2)
- The 2024 review emphasizes a “lymphoeosinophilic” infiltrate and notes that giant cells/granulomas are absent or nominal in many JTA cases and help distinguish JTA from GCA. (marquessoares2024bilateraljuveniletemporal pages 2-4)

### 6.3 Proposed nosologic overlap (expert interpretation)
Marques-Soares et al. (2024) highlight overlap features with **Kimura disease (KD)** and **angiolymphoid hyperplasia with eosinophilia (ALHE)**, especially because both can show eosinophilia/IgE elevation and perivascular eosinophilic infiltrates. The paper notes the hypothesis that JTA may start as a vascular inflammatory process that can extend to neighboring tissues and lead to lymphoid follicles. (marquessoares2024bilateraljuveniletemporal pages 2-4)

### 6.4 Differential-pathology “red flags”
The 2024 review notes that **fibrinoid necrosis** should prompt alternative diagnoses, including **ANCA-associated vasculitis** and **polyarteritis nodosa**, rather than JTA. (marquessoares2024bilateraljuveniletemporal pages 1-2)

### 6.5 Suggested ontology terms (mechanisms)
- **GO Biological Process (suggestions):** arteritis; inflammatory response; eosinophil chemotaxis/activation; intimal hyperplasia; thrombus formation; extracellular matrix organization.
- **Cell Ontology (CL) (suggestions):** eosinophil; CD4-positive T cell; B cell; plasma cell; macrophage/monocyte.

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
- Primary site: **superficial temporal arteries** and branches of the **external carotid artery** system. (marquessoares2024bilateraljuveniletemporal pages 1-2)

### 7.2 Suggested UBERON terms
- **Superficial temporal artery** (UBERON term exists; exact identifier not available from retrieved evidence; recommended to map in ontology pipeline).
- **Temporal region of head**; **scalp**.

### 7.3 Subcellular level
Not characterized in retrieved evidence.

## 8. Temporal development (natural history)

### 8.1 Onset
Typically presents in late childhood through early adulthood; commonly operationalized as <45 years or <50 years in series and reviews. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

### 8.2 Course/progression
JTA is often described as **benign** and localized. In the 44-patient dataset, **83.7%** had a single episode and local relapse occurred in **~16%**. (journeau2019juveniletemporalarteritis pages 1-2)

The 2024 case report highlights potential **spontaneous regression** without further treatment following biopsy and emphasizes variability in disease course. (marquessoares2024bilateraljuveniletemporal pages 2-4)

## 9. Inheritance and population

### 9.1 Epidemiology
Robust incidence/prevalence estimates are not available due to rarity. The 2024 review cites “prevalence estimates under 1 per 1,000,000 individuals.” (marquessoares2024bilateraljuveniletemporal pages 1-2)

Case-count statistics (proxy epidemiology):
- 2019 multicenter series states “Less than forty cases have been published” (at that time), and analyzed 44 total cases by combining new cases and literature. (journeau2019juveniletemporalarteritis pages 1-2)
- 2009 review similarly emphasizes extreme rarity and notes <40 young temporal-artery vasculitis cases, including 15 JTA patients described in that review’s framing. (nesher2009vasculitisofthe pages 1-2)

### 9.2 Demographics
- Sex ratio: male predominance. Example: 34/44 (77.3%) male in 2019 compilation. (journeau2019juveniletemporalarteritis pages 1-2)
- Age distribution: median age 30 (range 7–44) in 2019 compilation; median 34.5 (range 21–49) in 2024 bilateral-case subset synthesis. (journeau2019juveniletemporalarteritis pages 1-2, marquessoares2024bilateraljuveniletemporal pages 6-7)

### 9.3 Inheritance
No established inheritance pattern; hereditary data are lacking. (marquessoares2024bilateraljuveniletemporal pages 1-2)

## 10. Diagnostics

### 10.1 Clinical suspicion
Key clinical pattern is a localized temporal nodule/lump in a young patient, typically without systemic inflammatory syndrome. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

### 10.2 Laboratory tests
A distinguishing feature from GCA is often normal acute-phase reactants (ESR/CRP) in many cases. (marquessoares2024bilateraljuveniletemporal pages 1-2, nesher2009vasculitisofthe pages 2-4)

However, eosinophilia can be present:
- 2019 compilation: eosinophilia >500/mm³ in 34.1% (14/41). (journeau2019juveniletemporalarteritis pages 1-2)
- 2024 bilateral-case subset: peripheral blood eosinophilia 69.2% (9/13) and elevated IgE 66.7% (4/6) where measured. (marquessoares2024bilateraljuveniletemporal pages 7-8)

### 10.3 Imaging
- **Doppler/duplex ultrasound:** can show the “halo sign” (which also occurs in GCA) and can show segmental thickening and microaneurysms. (marquessoares2024bilateraljuveniletemporal pages 1-2, espitia2018imagegallerybilateral pages 1-1)
- **PET-CT/CT:** the 2024 review states PET-CT/CT “reveal no indications of vasculitis in other arterial regions” in contrast to GCA. (marquessoares2024bilateraljuveniletemporal pages 1-2)

### 10.4 Biopsy / histopathology (diagnostic cornerstone)
Histopathology is repeatedly emphasized as crucial for diagnosis and for distinguishing from mimics (GCA, KD, ALHE, systemic vasculitides). (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2)

Canonical features include:
- Lymphoeosinophilic arteritis/panarteritis. (marquessoares2024bilateraljuveniletemporal pages 1-2)
- Intimal hyperplasia/proliferation with luminal occlusion. (marquessoares2024bilateraljuveniletemporal pages 2-4)
- IEL disruption/disorganization. (marquessoares2024bilateraljuveniletemporal pages 2-4)
- Thrombosis and/or microaneurysmal lesions in some cases. (marquessoares2024bilateraljuveniletemporal pages 1-2, espitia2018imagegallerybilateral pages 1-1)

**Histopathology figure evidence:** Figure 2 from Marques-Soares et al. (2024) shows STA cross-sections with luminal obliteration/intimal hyperplasia, transmural inflammatory infiltrate with abundant eosinophils, and elastic fiber disorganization on Verhoeff-Van Gieson stain. (marquessoares2024bilateraljuveniletemporal media 84a68dfb)

### 10.5 Differential diagnosis (expert consensus)
- **Giant cell arteritis (GCA):** typically >50 years, systemic symptoms and elevated ESR/CRP more common; treated urgently with corticosteroids to prevent ischemic complications. JTA is younger, usually localized/benign, and excision often curative; giant cells/granulomas are often absent in JTA but may occur sparsely. (marquessoares2024bilateraljuveniletemporal pages 1-2, journeau2019juveniletemporalarteritis pages 1-2, espitia2018imagegallerybilateral pages 1-1)
- **Kimura disease / ALHE:** may mimic clinically and share eosinophilia/IgE and perivascular inflammation; histology and anatomic distribution aid distinction. (marquessoares2024bilateraljuveniletemporal pages 1-2, marquessoares2024bilateraljuveniletemporal pages 2-4)
- **Systemic vasculitides involving temporal arteries:** PAN, ANCA-associated vasculitis; fibrinoid necrosis should raise suspicion for these rather than JTA. (marquessoares2024bilateraljuveniletemporal pages 1-2, nesher2009vasculitisofthe pages 1-2)
- **Non-vascular mimics:** lipoma, sebaceous/dermoid cysts, aneurysm/AVM. (marquessoares2024bilateraljuveniletemporal pages 1-2)

## 11. Outcome / prognosis

### 11.1 Prognosis
JTA is generally favorable/benign:
- 2019 conclusion: “JTA is a rare, localized and benign disease… cured by local surgery.” (journeau2019juveniletemporalarteritis pages 1-2)
- 2018 image-case: “The course is favourable; relapses are rare. Unlike giant-cell arteritis, excision is curative in JTA.” (espitia2018imagegallerybilateral pages 1-1)

### 11.2 Relapse
Local relapses were ~16% in the 2019 aggregated dataset. (journeau2019juveniletemporalarteritis pages 1-2)

## 12. Treatment

### 12.1 Real-world management patterns
**Surgical biopsy/excision** is the most common approach and often curative.
- In 2019 compilation: “complete excision without further treatment was documented for 72.7%.” (journeau2019juveniletemporalarteritis pages 1-2)
- In 2018 image-case: excision followed by favorable course without treatment and no relapse in 3 years. (espitia2018imagegallerybilateral pages 1-1)

**Corticosteroids** are used in a minority of cases (often when symptoms persist, bilateral disease complicates excision, or when diagnosis is uncertain):
- 2019: corticosteroids used in 18.6% (8/43). (journeau2019juveniletemporalarteritis pages 1-2)
- 2024 bilateral-case subset: corticosteroid therapy used in 33.3% (6/18) with resolution in 66.7% (4/6) of treated cases. (marquessoares2024bilateraljuveniletemporal pages 7-8)

Other sporadically used therapies in the 2024 synthesis include **colchicine, methotrexate, aspirin, suplatast tosilate, tocopherol nicotinamide**, typically in anecdotal contexts. (marquessoares2024bilateraljuveniletemporal pages 7-8)

### 12.2 MAXO (Medical Action Ontology) suggestions
- Surgical excision of affected artery / excisional biopsy (MAXO: procedure terms to be mapped in ontology pipeline). (journeau2019juveniletemporalarteritis pages 1-2)
- Systemic corticosteroid therapy (MAXO mapping recommended). (journeau2019juveniletemporalarteritis pages 1-2)

### 12.3 Clinical trials
A ClinicalTrials.gov search did not identify trials specifically targeting JTA; retrieved trials related to GCA/vasculitis broadly or imaging methods, consistent with JTA’s rarity and lack of dedicated interventional research. (clinical trials tool output; no JTA-relevant trial chunks met relevance criteria)

## 13. Prevention

No JTA-specific primary/secondary prevention strategies are established in the retrieved literature; prevention is not emphasized, consistent with unclear etiology and rarity.

## 14. Other species / natural disease

No naturally occurring JTA analog in other species was identified in retrieved evidence.

## 15. Model organisms

No established model organisms for JTA were identified in retrieved evidence.

## Recent developments (2023–2024 priority)

The most substantive recent development in the retrieved corpus is the **2024 Rheumatology International case-based systematic review** that focuses on bilateral JTA and provides updated quantitative synthesis, emphasizing: (i) rarity with cited prevalence <1/1,000,000, (ii) importance of histopathology, (iii) frequency of eosinophilia/IgE elevation in bilateral-case reports, and (iv) possibility of spontaneous regression and need to avoid overtreatment. (Published online 2024-08-24; DOI: https://doi.org/10.1007/s00296-024-05624-2) (marquessoares2024bilateraljuveniletemporal pages 1-2, marquessoares2024bilateraljuveniletemporal pages 7-8)

## Key data/statistics (most directly supported)
- 44-patient clinicopathologic synthesis (2019): male 77.3%; headache 47.7%; general symptoms 11.4%; eosinophilia 34.1%; excision alone 72.7%; relapse ~16%. (journeau2019juveniletemporalarteritis pages 1-2)
- Bilateral-case subset synthesis (2024): median age 34.5 (21–49); painful nodules 44.4%; headache 28.6%; elevated ESR 11.1%; peripheral eosinophilia ~69%; elevated IgE 66.7% (measured subset); recurrence after biopsy 16.7%. (marquessoares2024bilateraljuveniletemporal pages 6-7, marquessoares2024bilateraljuveniletemporal pages 7-8)

## Evidence summary table (key sources)
| Citation | PMID | Publication type | Population / case count | Key clinical features | Labs (ESR/CRP/eosinophilia/IgE) | Histopathology highlights | Management / outcome | URL / DOI |
|---|---|---|---|---|---|---|---|---|
| Nesher 2009 |  | Review + case report | Review of temporal-artery vasculitis in patients <50; states 15 JTA patients described and <40 young temporal-artery vasculitis cases overall | Typical JTA presents as palpable temporal nodule/swelling, painless or tender; usually no ophthalmic or cranial ischemic symptoms; review case had pulsatile tender swelling | Case: ESR 3 mm/h, CRP 0.1 mg/dL, no peripheral eosinophilia; review notes eosinophilia may be present and normal ESR is common | Nongranulomatous panarteritis with mononuclear infiltrate and numerous eosinophils; intimal thickening/hyperplasia, severe internal elastic lamina disruption, luminal thrombosis; no multinucleated giant cells in the case | Excision considered curative in the case; no systemic therapy beyond mild analgesics; review emphasizes clinicopathologic correlation and distinction from systemic vasculitides | https://doi.org/10.1016/j.semarthrit.2008.03.001 (nesher2009vasculitisofthe pages 1-2, nesher2009vasculitisofthe pages 2-4, nesher2009vasculitisofthe pages 4-5) |
| Journeau 2019 |  | Multicenter series + literature review | 12 new French cases + 32 literature cases = 44 total patients (34 men, 10 women), median age 30 years | Temporal lump/prominent temporal arteries in all patients; headache in 47.7%; general symptoms uncommon (11.4%); initial bilateral involvement 25.0% | Biological inflammatory syndrome 6.8%; eosinophilia >500/mm3 in 34.1% | Inflammatory infiltrate in arterial wall 97.6%; perivascular extension 82.6%; lymphoid follicles/germinal centres 60%; sparse giant cells 25%; granuloma 22.9% | Complete excision without further treatment in 72.7%; corticosteroids in 18.6%; majority had a single episode; local relapses 16.3%; authors conclude JTA is rare, localized, benign, and usually cured by local surgery | https://doi.org/10.1016/j.autrev.2019.03.007 (journeau2019juveniletemporalarteritis pages 1-2) |
| Espitia 2018 |  | Image-based case report | 1 case, 23-year-old man with bilateral disease | Bilateral temporal nodules with “horn growth” appearance; often unilateral in JTA generally; lacked systemic symptoms | Hypereosinophilia noted; inflammatory syndrome absent | Segmental thickening and microaneurysms on duplex US; histology showed intimal hyperplasia with panarteritis and eosinophilic/lymphocytic infiltrate extending to perivascular tissue | Temporal artery excision; favorable course without treatment; no relapse within 3 years; note states excision is treatment of choice over steroids | https://doi.org/10.1111/bjd.17008 (espitia2018imagegallerybilateral pages 1-1) |
| Durant 2011 |  | Case report | 1 middle-aged woman; article notes JTV/JTA median age 23 years, range 7–39, and <40 cases reported | Localized temporal nodules/swelling rather than full GCA syndrome | Example case: CRP 12 mg/L, ESR 15 mm/h, no hypereosinophilia | Nongranulomatous panarteritis with mononuclear cells and eosinophils; intimal hyperplasia; partial loss of internal elastic lamina; no giant cells | Excision of involved artery often curative; steroids not required | https://doi.org/10.1016/j.avsg.2010.10.006 (durant2011juveniletemporalvasculitis pages 1-2) |
| Marques-Soares 2024 |  | Case report + systematic review | 43 case reports reviewed, including 17 with bilateral involvement; presented case was a 40-year-old woman | JTA defined as rare localized non-granulomatous eosinophilic arteritis of superficial temporal arteries, usually <45 years; presents as painful or painless temporal nodules; bilateral cases emphasized; prevalence estimate <1 per 1,000,000 | Acute-phase reactants typically normal; hypereosinophilia and elevated IgE described as common; in bilateral-case synthesis: elevated ESR 11.1%, peripheral blood eosinophilia 69.2%, elevated IgE 66.7% where measured; index case had normal eosinophils and normal ESR/CRP | Lymphoeosinophilic arteritis/panarteritis, intraluminal thrombosis, possible parietal microaneurysms, disruption of internal elastic lamina, intimal proliferation/hyperplasia; giant cells/granulomas absent or rare; fibrinoid necrosis should prompt alternate diagnosis | Biopsy often diagnostic and therapeutic; bilateral-case review: corticosteroids used in 33.3% with resolution in 66.7% of treated cases; recurrence after biopsy 16.7%; some cases, including index case, had spontaneous regression without treatment | https://doi.org/10.1007/s00296-024-05624-2 (marquessoares2024bilateraljuveniletemporal pages 1-2, marquessoares2024bilateraljuveniletemporal pages 4-6, marquessoares2024bilateraljuveniletemporal pages 2-4, marquessoares2024bilateraljuveniletemporal pages 6-7, marquessoares2024bilateraljuveniletemporal pages 7-8, marquessoares2024bilateraljuveniletemporal pages 8-9) |


*Table: This table summarizes major published sources on juvenile temporal arteritis, emphasizing clinical presentation, laboratory patterns, histopathology, and management/outcomes. It is useful for quickly comparing how case reports, reviews, and multicenter data define and distinguish JTA from other temporal vasculitides.*

## Limitations of current evidence base
The evidence base is dominated by case reports/series and retrospective synthesis, with limited longitudinal follow-up standardization, scarce population-level epidemiology, and minimal molecular/genetic investigation; these limitations are explicitly noted as motivations for future research in the 2024 review. (marquessoares2024bilateraljuveniletemporal pages 7-8)


References

1. (marquessoares2024bilateraljuveniletemporal pages 1-2): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

2. (journeau2019juveniletemporalarteritis pages 1-2): Louis Journeau, Marc-Antoine Pistorius, Ulrique Michon-Pasturel, Marc Lambert, Francois-Xavier Lapébie, Alessandra Bura-Riviere, Philippe de Faucal, Patrick Jego, Quentin Didier, Cécile Durant, Geoffrey Urbanski, Baptiste Hervier, Claire Toquet, Christian Agard, and Olivier Espitia. Juvenile temporal arteritis: a clinicopathological multicentric experience. Autoimmunity reviews, 18 5:476-483, May 2019. URL: https://doi.org/10.1016/j.autrev.2019.03.007, doi:10.1016/j.autrev.2019.03.007. This article has 23 citations and is from a peer-reviewed journal.

3. (durant2011juveniletemporalvasculitis pages 1-2): Cecile Durant, Jérome Connault, Julie Graveleau, Claire Toquet, Jean M. Brisseau, and Mohamed Hamidou. Juvenile temporal vasculitis: a rare case in a middle-aged woman. Annals of vascular surgery, 25 3:384.e5-7, Apr 2011. URL: https://doi.org/10.1016/j.avsg.2010.10.006, doi:10.1016/j.avsg.2010.10.006. This article has 16 citations and is from a peer-reviewed journal.

4. (marquessoares2024bilateraljuveniletemporal pages 8-9): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

5. (marquessoares2024bilateraljuveniletemporal pages 7-8): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

6. (marquessoares2024bilateraljuveniletemporal pages 6-7): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

7. (espitia2018imagegallerybilateral pages 1-1): O. Espitia, C. Agard, and Marc-Antoine Pistorius. Image gallery: bilateral juvenile temporal arteritis. British Journal of Dermatology, 179:e168-e168, Oct 2018. URL: https://doi.org/10.1111/bjd.17008, doi:10.1111/bjd.17008. This article has 3 citations and is from a highest quality peer-reviewed journal.

8. (marquessoares2024bilateraljuveniletemporal pages 2-4): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

9. (nesher2009vasculitisofthe pages 2-4): Gideon Nesher, Shirly Oren, Graciela Lijovetzky, and Ronit Nesher. Vasculitis of the temporal arteries in the young. Seminars in arthritis and rheumatism, 39 2:96-107, Oct 2009. URL: https://doi.org/10.1016/j.semarthrit.2008.03.001, doi:10.1016/j.semarthrit.2008.03.001. This article has 52 citations and is from a peer-reviewed journal.

10. (nesher2009vasculitisofthe pages 1-2): Gideon Nesher, Shirly Oren, Graciela Lijovetzky, and Ronit Nesher. Vasculitis of the temporal arteries in the young. Seminars in arthritis and rheumatism, 39 2:96-107, Oct 2009. URL: https://doi.org/10.1016/j.semarthrit.2008.03.001, doi:10.1016/j.semarthrit.2008.03.001. This article has 52 citations and is from a peer-reviewed journal.

11. (marquessoares2024bilateraljuveniletemporal media 84a68dfb): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.

12. (nesher2009vasculitisofthe pages 4-5): Gideon Nesher, Shirly Oren, Graciela Lijovetzky, and Ronit Nesher. Vasculitis of the temporal arteries in the young. Seminars in arthritis and rheumatism, 39 2:96-107, Oct 2009. URL: https://doi.org/10.1016/j.semarthrit.2008.03.001, doi:10.1016/j.semarthrit.2008.03.001. This article has 52 citations and is from a peer-reviewed journal.

13. (marquessoares2024bilateraljuveniletemporal pages 4-6): Joana Marques-Soares, Mª Isabel Garcia-Domingo, Cinthya Báez Leal, and Jaume Alijotas-Reig. Bilateral juvenile temporal arteritis: a case-based review. Rheumatology International, 44:2253-2261, Aug 2024. URL: https://doi.org/10.1007/s00296-024-05624-2, doi:10.1007/s00296-024-05624-2. This article has 0 citations and is from a peer-reviewed journal.