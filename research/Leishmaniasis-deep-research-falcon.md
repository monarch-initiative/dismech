---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T14:44:35.911489'
end_time: '2026-04-04T14:53:57.342801'
duration_seconds: 561.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leishmaniasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leishmaniasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Leishmaniasis** covering all of the
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
- **Disease Name:** Leishmaniasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Leishmaniasis** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Leishmaniasis (Infectious Disease)

### Scope and evidence limitations
This report synthesizes the currently retrieved literature and trial registry entries. Several required curated identifiers (MONDO, MeSH, ICD-10/11, Orphanet) could not be evidenced within the retrieved document corpus and are therefore marked as *not available in the current evidence set* to avoid uncited guessing. (cosma2024leishmaniasisinhumans pages 2-4, balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4)

| Clinical form | Key features | Main causative species (examples) | Recent burden statistics (with year) | Geographic notes |
|---|---|---|---|---|
| Cutaneous leishmaniasis (CL) | Most prevalent form; skin lesions/ulcers on exposed sites; lesions may persist for months to years and often leave atrophic scars; substantial psychosocial impact (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, cosma2024leishmaniasisinhumans pages 2-4, balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4) | *L. major*, *L. tropica*, *L. aethiopica*, *L. mexicana*, *L. amazonensis*, *L. braziliensis* complex (examples) (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, mota2024classicalandinnovative pages 1-3) | WHO reported 253,435 new CL cases in 2018; estimated 500,000–1,000,000 new CL cases annually; another review cites ~1.5–2 million newly diagnosed leishmaniasis cases/year overall with ~350 million people at risk (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4) | Endemic in 87 countries; concentrated in the Eastern Mediterranean and the Americas, with major burdens in Afghanistan, Algeria, Brazil, Iran, Iraq, Pakistan, and Syria (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6) |
| Mucocutaneous leishmaniasis (MCL/ML) | Granulomatous, destructive mucosal disease affecting nose, mouth, pharynx; can follow untreated/inadequately treated CL; may impair eating, breathing, swallowing, and speech (fischer2024treatmentofmucocutaneous pages 2-2) | *L. braziliensis*, *L. guyanensis*, *L. amazonensis*, *L. panamensis*; Old World cases mainly *L. infantum*, *L. tropica*, *L. major* (fischer2024treatmentofmucocutaneous pages 2-2) | Approximately 1,700 new MCL cases/year in the New World (fischer2024treatmentofmucocutaneous pages 2-2) | Highest risk in a South American “mucosal belt” from Peru through Bolivia and Brazil to Paraguay; >90% of cases reported in Bolivia, Brazil, Ethiopia, and Peru (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, fischer2024treatmentofmucocutaneous pages 2-2) |
| Visceral leishmaniasis (VL, kala-azar) | Most severe/systemic form; fever, weight loss, splenomegaly/hepatomegaly, pancytopenia/anemia; potentially fatal if untreated (sousa2024visceralleishmaniasistherapeutic pages 4-6, balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, cosma2024leishmaniasisinhumans pages 2-4) | *L. donovani*, *L. infantum* (cosma2024leishmaniasisinhumans pages 2-4, mota2024classicalandinnovative pages 1-3) | Estimated 50,000–90,000 new cases/year globally, with only ~25–45% officially reported; untreated mortality exceeds 95%; >95% of new VL cases in 2018 occurred in 10 countries; VL contributes up to 1.6 million DALYs (sousa2024visceralleishmaniasistherapeutic pages 4-6, balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, cosma2024leishmaniasisinhumans pages 2-4) | Concentrated in India, Sudan, Brazil, and Kenya (68% of cases); also major burden across Brazil, China, Ethiopia, India, Iraq, Kenya, Nepal, Somalia, South Sudan, and Sudan; in the Americas, 69,665 cases were reported from 2001–2021 and Brazil accounted for ~90% of Latin American reports (sousa2024visceralleishmaniasistherapeutic pages 4-6, balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6) |
| Post-kala-azar dermal leishmaniasis (PKDL) | Post-VL dermal complication recognized as part of the clinical spectrum (cosma2024leishmaniasisinhumans pages 2-4) | Usually follows viscerotropic infection by *L. donovani*/*L. infantum* context (cosma2024leishmaniasisinhumans pages 2-4) | No specific burden figure provided in the cited evidence (cosma2024leishmaniasisinhumans pages 2-4) | Geographic distribution not quantified in the cited evidence; discussed as a post-VL manifestation in endemic settings (cosma2024leishmaniasisinhumans pages 2-4) |


*Table: This table summarizes the main clinical forms of leishmaniasis, their defining features, example causative species, recent burden estimates, and major endemic regions. It condenses key disease-level epidemiology from the provided 2023–2024 evidence sources for rapid knowledge-base use.*

## 1. Disease Information

### 1.1 Disease definition and overview
Leishmaniasis is a neglected tropical disease caused by protozoan parasites of the genus *Leishmania* transmitted to humans (and other mammals) by infected female phlebotomine sandflies. Clinical expression spans cutaneous, mucocutaneous, and visceral disease forms, with post-kala-azar dermal leishmaniasis (PKDL) recognized as part of the visceral spectrum. (cosma2024leishmaniasisinhumans pages 2-4, mota2024classicalandinnovative pages 1-3)

**Direct abstract support (definition quote):**
- “Leishmaniasis is classified as a neglected tropical disease (NTD), caused by protozoan parasites of the genus *Leishmania*, which are transmitted to humans and other animals through the bite of infected female phlebotomine sandflies.” (Cosma et al., 2024-10-??, DOI: 10.3390/tropicalmed9110258) (cosma2024leishmaniasisinhumans pages 2-4)

### 1.2 Key identifiers (ontology and clinical coding)
- **MONDO ID:** not available in retrieved evidence.
- **MeSH:** not available in retrieved evidence.
- **ICD-10 / ICD-11:** not available in retrieved evidence.
- **Orphanet:** not available in retrieved evidence.

### 1.3 Common synonyms / alternative names
- **Visceral leishmaniasis:** “kala-azar”. (sousa2024visceralleishmaniasistherapeutic pages 4-6, cosma2024leishmaniasisinhumans pages 2-4)
- **Tegumentary leishmaniasis:** used as an umbrella term for cutaneous and mucosal involvement in some clinical contexts. (chivinski2023intravenousliposomalamphotericin pages 6-7)

### 1.4 Evidence sources and aggregation level
The evidence used here includes: peer-reviewed reviews and systematic reviews/meta-analyses, observational clinical cohorts, and controlled human infection model (CHIM) data. These are aggregated disease-level resources with embedded patient-level study data; some sections also draw on retrospective chart review and case series evidence. (cosma2024leishmaniasisinhumans pages 2-4, lindner2024americancutaneousleishmaniasis pages 2-4, parkash2024safetyandreactogenicity pages 2-3, chivinski2023intravenousliposomalamphotericin pages 6-7)

## 2. Etiology

### 2.1 Disease causal factors
- **Infectious agent:** intracellular protozoa (*Leishmania* spp.). (cosma2024leishmaniasisinhumans pages 2-4, balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4)
- **Transmission:** via bites of infected female sandflies. (cosma2024leishmaniasisinhumans pages 2-4, sousa2024visceralleishmaniasistherapeutic pages 4-6)
- **Clinical heterogeneity:** depends strongly on parasite species and host immunity. (cosma2024leishmaniasisinhumans pages 2-4, dey2024il32producingcd8+ pages 1-7)

### 2.2 Risk factors
**Host factors**
- **Immunocompromise** (e.g., HIV, inborn errors of immunity) is associated with more severe disease and relapse risk in visceral infection. (lodi2024immuneresponseto pages 10-11)

**Behavioral/environmental factors (mucosal disease)**
- Risk factors for mucocutaneous leishmaniasis include **smoking**, **alcohol abuse**, and **large or multiple untreated skin lesions**, especially on head/neck. (fischer2024treatmentofmucocutaneous pages 2-2)

**Macro-environmental determinants (One Health)**
Climate change, deforestation, urbanization, globalization/migration can shift sandfly and reservoir distributions, increasing human exposure and expanding leishmaniasis into new latitudes/altitudes. (cosma2024leishmaniasisinhumans pages 2-4)

### 2.3 Protective factors
Not directly identified in the retrieved evidence corpus (no specific host genetic protective alleles or environmental protective exposures were evidenced).

### 2.4 Gene–environment interactions
Explicit gene–environment interaction evidence was not present in the retrieved corpus. The best-supported interaction framework here is “parasite species × host immune state × environment/vector ecology” determining clinical form and outcomes. (cosma2024leishmaniasisinhumans pages 2-4, fischer2024treatmentofmucocutaneous pages 2-2)

## 3. Phenotypes

### 3.1 Core clinical phenotypes by form (with suggested HPO terms)

**Cutaneous leishmaniasis (CL)**
- **Skin ulcer(s)** / **papules/plaques**; lesions may persist months–years; atrophic scarring common. (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4)
  - Suggested HPO: **Skin ulcer (HP:0031432)**; **Scar (HP:0100716)**; **Skin papule (HP:0200037)**.
- Typical incubation reported as **1–4 months** and spontaneous healing over **2–10 months** in some cases. (balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4)

**Mucocutaneous leishmaniasis (MCL/ML)**
- Destructive granulomatous lesions of oral/nasal/pharyngeal mucosa; complications include impaired swallowing/speech, aspiration pneumonia, bacterial superinfection/sepsis, and need for reconstructive surgery. (fischer2024treatmentofmucocutaneous pages 2-2)
  - Suggested HPO: **Nasal septum perforation (HP:0011833)**; **Dysphagia (HP:0002015)**; **Dysarthria (HP:0001260)**.

**Visceral leishmaniasis (VL; kala-azar)**
- Systemic syndrome including fever, weight loss, hepatosplenomegaly, and cytopenias (pancytopenia/anemia). (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, cosma2024leishmaniasisinhumans pages 2-4)
  - Suggested HPO: **Fever (HP:0001945)**; **Weight loss (HP:0001824)**; **Splenomegaly (HP:0001744)**; **Hepatomegaly (HP:0002240)**; **Anemia (HP:0001903)**; **Pancytopenia (HP:0001876)**.

**Post-kala-azar dermal leishmaniasis (PKDL)**
- Recognized as post-VL dermal manifestation; detailed phenotype frequencies not evidenced in the retrieved set. (cosma2024leishmaniasisinhumans pages 2-4)

### 3.2 Quality of life impact
CL and MCL can cause scarring/disfigurement with substantial psychosocial morbidity. (cosma2024leishmaniasisinhumans pages 2-4, balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6)

## 4. Genetic / Molecular Information

### 4.1 Human causal genes / Mendelian causes
Leishmaniasis is not a monogenic inherited disease; causal pathogen is *Leishmania* spp. Host genetics can modulate susceptibility and course, but specific loci were not evidenced in the retrieved corpus.

### 4.2 Molecular mechanisms (host–pathogen) and ontology suggestions

#### 4.2.1 Cellular tropism and immune evasion (VL and CL)
- Parasite survival involves immune evasion mechanisms that favor anti-inflammatory environments, including immune checkpoint activity and cytokine skewing. (lodi2024immuneresponseto pages 10-11, dey2024il32producingcd8+ pages 1-7)

**Phagosome manipulation (VL)**
- *L. donovani* lipophosphoglycan (LPG) can exclude vesicular proton-ATPase (V-ATPase) from phagosomes by impairing Synaptotagmin V recruitment, limiting acidification. (lodi2024immuneresponseto pages 10-11)

**TLR pathway suppression**
- Parasites can exploit host deubiquitinating enzyme **A20**, a negative regulator of TLR signaling, to subvert innate responses. (lodi2024immuneresponseto pages 10-11)

Suggested ontologies:
- **GO biological process:** *response to protozoan (GO:0009617)*; *phagosome maturation (GO:0090382)*; *regulation of Toll-like receptor signaling pathway (GO:0034121)*.
- **CL cell types:** **macrophage (CL:0000235)**; **neutrophil (CL:0000775)**; **dendritic cell (CL:0000451)**; **CD8-positive, alpha-beta T cell (CL:0000625)**; **regulatory T cell (CL:0000815)**.

#### 4.2.2 Immune checkpoints and localized immunosuppressive niches (human CL; 2024)
Spatial and single-cell profiling of human CL lesions identified myeloid-centered niches co-expressing **PD-L1 (CD274)** and **IDO1**, with neighboring **IL-32–producing CD8+ memory T cells and Tregs**. Mechanistically, IDO1-mediated tryptophan catabolism can suppress T-cell proliferation and promote regulatory phenotypes, and PD-L1 can suppress T-cell activation via PD-1 engagement. (dey2024il32producingcd8+ pages 7-11, dey2024il32producingcd8+ pages 11-15)

**Quantitative prognostic finding (treatment response):**
Higher IL-32+ CD8+ T cell abundance was associated with slower cure; IL-32-low patients cured earlier with hazard ratios reported in the preprint. (dey2024il32producingcd8+ pages 11-15)

Suggested ontologies:
- **GO:** *tryptophan catabolic process (GO:0006569)*; *negative regulation of T cell activation (GO:0050868)*.

#### 4.2.3 Hypoxia–neutrophil–CD8 cytotoxic pathology in CL (2024)
A 2024 mechanistic study supports a causal chain in CL lesions: neutrophil recruitment increases oxygen consumption and reactive oxygen species (ROS) generation, amplifying local hypoxia; hypoxia drives **Blimp-1/PRDM1** and induces cytolytic differentiation and **granzyme B** expression in lesion CD8+ T cells. Downstream, cytolysis activates NLRP3 inflammasome/IL-1β and perpetuates neutrophilic inflammation and tissue damage. Human CL lesions exhibit hypoxia transcriptional signatures correlated with neutrophils. (fowler2024neutrophilmediatedhypoxiadrives pages 1-2)

Suggested ontologies:
- **GO:** *response to hypoxia (GO:0001666)*; *neutrophil degranulation (GO:0043312)*; *T cell mediated cytotoxicity (GO:0001913)*; *NLRP3 inflammasome complex assembly (GO:0072557)*.

#### 4.2.4 Epigenetic regulation and IL-10/IL-12 reciprocity (macrophage; 2024)
Single-cell ATAC-seq analysis in a macrophage infection model identified a transient “sleepy macrophage” state and a reciprocal IL-10/IL-12 axis; the work emphasizes transcription-factor-driven chromatin remodeling and epigenetic control of inflammatory cytokine programs in infected macrophages. (khandibharad2024singlecellatacsequencing pages 1-2)

Suggested ontologies:
- **GO:** *chromatin remodeling (GO:0006338)*; *regulation of interleukin-10 production (GO:0032666)*; *regulation of interleukin-12 production (GO:0032655)*.

#### 4.2.5 Single-cell atlas of parasite development in the vector (2024)
Single-cell analysis of *Leishmania* development in sandflies identified heterogeneity in transmitted parasite forms beyond classical nondividing metacyclic promastigotes, including “replicating early metacyclics” and haptomonad stages, with in vivo mouse infection indicating pathology is not restricted to a single transmitted stage. (parkash2024safetyandreactogenicity pages 2-3)

## 5. Environmental Information

### 5.1 Environmental and ecological drivers (One Health)
Environmental disruptions (climate change, deforestation, urbanization) and human/animal movement can expand sandfly range and human-vector contact, contributing to emergence in previously non-endemic areas. (cosma2024leishmaniasisinhumans pages 2-4)

### 5.2 Reservoirs and zoonotic ecology
Domestic dogs are highlighted as primary reservoirs for zoonotic visceral leishmaniasis in some settings, with additional roles for wild reservoirs. (sousa2024visceralleishmaniasistherapeutic pages 4-6)

## 6. Anatomical Structures Affected

### 6.1 Primary organs/tissues
- **Skin** (cutaneous lesions; scarring). (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6)
  - Suggested UBERON: **skin of body (UBERON:0002097)**
- **Mucosa of upper aerodigestive tract** (nasal/oral/pharyngeal). (fischer2024treatmentofmucocutaneous pages 2-2)
  - Suggested UBERON: **nasal mucosa (UBERON:0001707)**; **oral mucosa (UBERON:0000344)**
- **Spleen, liver, bone marrow** (visceral leishmaniasis systemic involvement and diagnostic sampling sites). (cosma2024leishmaniasisinhumans pages 2-4, gritti2024epidemiologicalclinicaland pages 30-35)
  - Suggested UBERON: **spleen (UBERON:0002106)**; **liver (UBERON:0002107)**; **bone marrow (UBERON:0002371)**

### 6.2 Subcellular compartments
Not explicitly evidenced in the retrieved corpus; infection is intracellular (amastigotes in host cells). (mota2024classicalandinnovative pages 1-3)

## 7. Temporal Development

- **CL incubation:** reported 1–4 months in a 2023 review; typical spontaneous healing 2–10 months (variable). (balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4)
- **MCL evolution:** may occur after untreated/inadequately treated CL, potentially years later. (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6, fischer2024treatmentofmucocutaneous pages 2-2)
- **VL progression:** can be fatal if untreated; Sousa 2024 reports untreated mortality exceeding 95%. (sousa2024visceralleishmaniasistherapeutic pages 4-6)

## 8. Inheritance and Population

### 8.1 Epidemiology (recent statistics)
- Global annual incidence often cited as **700,000–1,000,000 new cases/year**. (cosma2024leishmaniasisinhumans pages 2-4)
- For CL, WHO reported **253,435 new cases in 2018**; a review cites **500,000–1,000,000 new cases annually**. (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6)
- For VL, a 2024 review estimates **50,000–90,000 new cases/year**, with **only 25–45% officially reported**, and **untreated mortality >95%**. (sousa2024visceralleishmaniasistherapeutic pages 4-6)
- VL is concentrated in India, Sudan, Brazil, and Kenya (reported as 68% of cases). (sousa2024visceralleishmaniasistherapeutic pages 4-6)

### 8.2 Geographic distribution and expansion
Leishmaniasis is endemic across Africa, Asia, Southern Europe, the Middle East, and Central/South America, with recent reports of autochthonous transmission in previously non-endemic Western Europe and North America attributed to climate and migration drivers. (cosma2024leishmaniasisinhumans pages 2-4)

## 9. Diagnostics

### 9.1 Parasitological diagnosis (microscopy, histology, culture)
- VL: microscopy sensitivity differs by sampling site: splenic aspirate/biopsy microscopy reported **>90% sensitivity**, bone marrow aspirate **50–80%**, with a quoted **0.1% fatality risk** for splenic sampling. (gritti2024epidemiologicalclinicaland pages 30-35)
- CL: microscopy of skin biopsy for amastigotes is used; one cited study reports direct exam sensitivity ~**89.3%**, decreasing with older lesions. (balahbib2023cutaneousleishmaniasisphysiopathology pages 9-12, balahbib2023cutaneousleishmaniasisphysiopathology pages 12-15)
- Culture: reported as uncommon in some settings due to long growth time; sensitivity cited as **60–85%**. (gritti2024epidemiologicalclinicaland pages 35-39)

### 9.2 Serology
- rK39 antigen is cited as useful for VL; performance may vary by geography (high performance in Indian subcontinent, lower sensitivity in Eastern Africa and southern Europe). (balahbib2023cutaneousleishmaniasisphysiopathology pages 12-15, gritti2024epidemiologicalclinicaland pages 35-39)

### 9.3 Molecular diagnostics and species typing
- PCR can detect as few as **10 parasites/mL**, with sensitivity **86–95% in acute lesions** but lower in chronic disease (~45.5% in one report). (balahbib2023cutaneousleishmaniasisphysiopathology pages 12-15)
- For imported ACL cases in Germany, diagnosis was clinical + **PCR confirmation**, with typing via ITS1/SSU rRNA PCR-RFLP and later HSP70 PCR-RFLP. (lindner2024americancutaneousleishmaniasis pages 2-4)
- Molecular typing: MLEE is described as historical gold standard but laborious and requires culture; high-copy targets used for molecular typing include kDNA minicircles, miniexon, and hsp70 (widely validated for species typing). (gritti2024epidemiologicalclinicaland pages 39-44, gritti2024epidemiologicalclinicaland pages 35-39)

### 9.4 Diagnostics used in recent spatial-omics CL studies
Studies of human CL lesions used slit-skin smears (Giemsa), PCR/qPCR confirmation, and RNA-FISH probes (e.g., amastin) for parasite detection in tissue sections. (dey2024il32producingcd8+ pages 19-22)

## 10. Outcome / Prognosis

- VL is described as potentially fatal if untreated; one 2024 review states untreated mortality **exceeds 95%**. (sousa2024visceralleishmaniasistherapeutic pages 4-6)
- In Brazil, a 2024 narrative review reports **50,478 cases and 3,945 deaths** through Aug 2024 with mortality **7.02%** (as reported in that secondary source). (sousa2024visceralleishmaniasistherapeutic pages 4-6)
- CL and MCL often lead to chronic morbidity via scarring/disfigurement and mucosal destruction. (fischer2024treatmentofmucocutaneous pages 2-2, cosma2024leishmaniasisinhumans pages 2-4)

## 11. Treatment

### 11.1 Standard pharmacotherapy and real-world use
Common antileishmanial agents across syndromes include pentavalent antimonials, amphotericin B (including liposomal), miltefosine, paromomycin, and pentamidine; choice often depends on setting/availability and host factors. (sousa2024visceralleishmaniasistherapeutic pages 4-6, fischer2024treatmentofmucocutaneous pages 2-2)

### 11.2 Quantitative treatment outcomes from recent evidence

#### Liposomal amphotericin B for cutaneous/mucosal disease (systematic review/meta-analysis; 2023)
- **Pooled cure rate (case series):** **87.0%** (95% CI 79–92%) across 38 case series. (Chivinski et al., 2023-07, DOI: 10.1093/ofid/ofad348) (chivinski2023intravenousliposomalamphotericin pages 1-2)
- **Case reports cure:** 65/92 (82.3%). (chivinski2023intravenousliposomalamphotericin pages 1-2)
- **Adverse reactions:** in pooled data, adverse reactions reported in **40.7%** of cases; most commonly renal toxicity and infusion reactions. (chivinski2023intravenousliposomalamphotericin pages 7-9)

#### Mucocutaneous leishmaniasis therapies (systematic review; 2024)
- Species-stratified outcomes show high reported success for L-AmB in multiple small series (e.g., *L. braziliensis* 57/64 (89%)). (fischer2024treatmentofmucocutaneous pages 4-4)
- Combination therapy NMA + pentoxifylline had 9/10 cured in one report and an overall cure rate reported as 95% for the combination. (fischer2024treatmentofmucocutaneous pages 6-7)

#### Post-kala-azar dermal leishmaniasis (PKDL) randomized trial (2021)
- Per-protocol final cure: **74.5%** (liposomal amphotericin B) vs **86.9%** (miltefosine). (pandey2021arandomizedopenlabel pages 3-4)
- Adverse events: 82% vs 56% (mostly grade I–II). (pandey2021arandomizedopenlabel pages 3-4)

### 11.3 Treatment guidelines (evidence limitation)
Formal WHO/IDSA guideline text was not retrieved in this corpus; treatment regimen details referenced in the meta-analysis include mention of guideline cumulative dosing (e.g., IDSA cumulative 18–21 mg/kg for L-AmB) but without full guideline retrieval. (chivinski2023intravenousliposomalamphotericin pages 7-9)

### 11.4 MAXO term suggestions (treatments)
- Liposomal amphotericin B therapy: **MAXO:0000743 (antifungal/antiparasitic drug therapy)** (placeholder—MAXO IDs not evidenced in corpus).
- Cryotherapy for localized CL lesions (used in CHIM recurrences): **MAXO:0000549 (cryotherapy)** (placeholder—MAXO IDs not evidenced in corpus). (parkash2024safetyandreactogenicity pages 1-2)

## 12. Prevention

### 12.1 Vector/reservoir control and One Health prevention
Integrated surveillance and prevention strategies targeting vectors, animal reservoirs (notably dogs), and human exposure are emphasized in the One Health literature; drivers such as climate change and land-use change motivate adaptive surveillance. (cosma2024leishmaniasisinhumans pages 2-4, sousa2024visceralleishmaniasistherapeutic pages 4-6)

### 12.2 Vaccines and CHIM as a vaccine-enabling technology (2024)
A major 2024 development is the establishment of a controlled human infection model (CHIM) for sand fly–transmitted *L. major* CL to accelerate vaccine development. (parkash2024safetyandreactogenicity pages 2-3, parkash2024safetyandreactogenicity pages 1-2)

**Direct abstract support (CHIM quote):**
- “The leishmaniases are globally important parasitic diseases for which no human vaccines are currently available.” (Parkash et al., Nature Medicine, 2024-08, DOI: 10.1038/s41591-024-03146-9) (parkash2024safetyandreactogenicity pages 1-2)

## 13. Other Species / Natural Disease (One Health)

- Dogs are highlighted as primary domestic reservoirs for visceral leishmaniasis in the Americas, with implications for zoonotic transmission and control. (sousa2024visceralleishmaniasistherapeutic pages 4-6)
- Leishmaniasis is framed as a human–animal–environment system, influenced by pet trade, breeding, and migration affecting reservoir movement. (cosma2024leishmaniasisinhumans pages 2-4)

## 14. Model Organisms and Experimental Systems

### 14.1 Human CHIM (real-world implementation for translational research)
- **Model:** sand fly–transmitted CL CHIM (*L. major* via *Phlebotomus duboscqi*). (parkash2024safetyandreactogenicity pages 2-3)
- **Take rate:** 64% overall (9/14), 82% among confirmed bites (9/11). (parkash2024safetyandreactogenicity pages 2-3)
- **Trial registration:** **NCT04512742**. (parkash2024safetyandreactogenicity pages 1-2)
- **Safety:** no severe/serious adverse events; recurrences treated successfully with cryotherapy; scarring observed. (parkash2024safetyandreactogenicity pages 1-2)

### 14.2 Mouse models
Mechanistic work in mice supports roles for neutrophils/hypoxia and CD8 cytotoxicity in CL pathology. (fowler2024neutrophilmediatedhypoxiadrives pages 1-2)

### 14.3 Macaque model (visceral persistence; single-cell)
A rhesus macaque VL model with post-treatment tissue reservoirs and single-cell transcriptomic profiling is described (preprint), highlighting parasite persistence in spleen, bone marrow, and lymph nodes after miltefosine. (parkash2024safetyandreactogenicity pages 2-3)

## 15. Clinical Trials and Development Pipeline (selected)
ClinicalTrials.gov trials retrieved include:
- **NCT04512742:** sand fly-transmitted CL CHIM (vaccine-enabling model). (parkash2024safetyandreactogenicity pages 1-2)
- VL combination therapy trials (completed): **NCT01122771**, **NCT00696969**, **NCT00523965**, **NCT00371995**. (clinical-trials tool output; not chunk-cited in current evidence set)
- Cutaneous/mucosal treatment trials: **NCT01377974** (miltefosine for mucosal leishmaniasis), **NCT03829917** (oral miltefosine + topical paromomycin in ACL). (clinical-trials tool output; not chunk-cited in current evidence set)

## Expert interpretation and analysis (2023–2024 emphasis)

1. **Diagnostics are moving toward molecular confirmation and species typing**, driven by heterogeneous treatment response across *Leishmania* species and the need to guide therapy; PCR-RFLP and HSP70 typing are used in real-world clinical practice for imported cases. (lindner2024americancutaneousleishmaniasis pages 2-4, gritti2024epidemiologicalclinicaland pages 39-44)
2. **Pathophysiology is increasingly understood as spatially compartmentalized immunopathology**, where distinct immune niches and checkpoints exist within lesions; spatial transcriptomics and single-cell methods identify actionable pathways (PD-L1/IDO1; hypoxia-driven cytotoxicity). (dey2024il32producingcd8+ pages 7-11, fowler2024neutrophilmediatedhypoxiadrives pages 1-2)
3. **A major translational development is the CL CHIM** that directly supports vaccine development by enabling controlled assessment of protective immunity and lesion biology in humans, including spatial immune mapping. (parkash2024safetyandreactogenicity pages 1-2, parkash2024safetyeffectivenessand pages 13-17)
4. **One Health framing is essential**: climate change and land-use shifts are not only upstream risk drivers but also determinants of future geographic spread, requiring surveillance strategies integrating humans, vectors, and reservoir animals (notably dogs). (cosma2024leishmaniasisinhumans pages 2-4, sousa2024visceralleishmaniasistherapeutic pages 4-6)

## Key URLs (publication pages)
- Cosma et al. 2024 (One Health perspective): https://doi.org/10.3390/tropicalmed9110258 (published 2024-10) (cosma2024leishmaniasisinhumans pages 2-4)
- Parkash et al. 2024 (Nature Medicine CHIM): https://doi.org/10.1038/s41591-024-03146-9 (published 2024-08) (parkash2024safetyandreactogenicity pages 1-2)
- Chivinski et al. 2023 (L-AmB meta-analysis): https://doi.org/10.1093/ofid/ofad348 (published 2023-07) (chivinski2023intravenousliposomalamphotericin pages 1-2)
- Fischer et al. 2024 (MCL treatment systematic review): https://doi.org/10.1111/ddg.15424 (published 2024-05) (fischer2024treatmentofmucocutaneous pages 2-2)
- Fowler et al. 2024 (hypoxia/CD8 pathology): https://doi.org/10.1172/jci177992 (published 2024-06) (fowler2024neutrophilmediatedhypoxiadrives pages 1-2)
- Khandibharad & Singh 2024 (scATAC “sleepy macrophages”): https://doi.org/10.1128/spectrum.03478-23 (published 2024-03) (khandibharad2024singlecellatacsequencing pages 1-2)

## Not-yet-fulfilled template elements (data not present in retrieved evidence)
- Curated IDs (MONDO, MeSH, ICD-10/11, Orphanet) and validated ontology mappings (MAXO IDs, specific UBERON/HPO/GO IDs) were not available in the evidence corpus and therefore remain incomplete.
- Specific host genetic susceptibility loci/variants and protective factors were not retrieved.



References

1. (cosma2024leishmaniasisinhumans pages 2-4): Claudia Cosma, Carla Maia, Nushrat Khan, Maria Infantino, and Marco Del Riccio. Leishmaniasis in humans and animals: a one health approach for surveillance, prevention and control in a changing world. Tropical Medicine and Infectious Disease, 9:258, Oct 2024. URL: https://doi.org/10.3390/tropicalmed9110258, doi:10.3390/tropicalmed9110258. This article has 76 citations.

2. (balahbib2023cutaneousleishmaniasisphysiopathology pages 1-4): Abdelaali Balahbib, Asma Hmamouch, Aicha El Allam, Hikmat Douhri, Naoufal Dahaieh, Nasreddine El Omari, Jactty Chew, Long Chiau Ming, and Abdelhakim Bouyahya. Cutaneous leishmaniasis: physiopathology, molecular diagnostic, and therapeutic approaches. Progress In Microbes &amp; Molecular Biology, Dec 2023. URL: https://doi.org/10.36877/pmmb.a0000395, doi:10.36877/pmmb.a0000395. This article has 5 citations.

3. (balahbib2023cutaneousleishmaniasisphysiopathology pages 4-6): Abdelaali Balahbib, Asma Hmamouch, Aicha El Allam, Hikmat Douhri, Naoufal Dahaieh, Nasreddine El Omari, Jactty Chew, Long Chiau Ming, and Abdelhakim Bouyahya. Cutaneous leishmaniasis: physiopathology, molecular diagnostic, and therapeutic approaches. Progress In Microbes &amp; Molecular Biology, Dec 2023. URL: https://doi.org/10.36877/pmmb.a0000395, doi:10.36877/pmmb.a0000395. This article has 5 citations.

4. (mota2024classicalandinnovative pages 1-3): Wanessa J. S. Mota, Beatriz N. Guedes, Sona Jain, Juliana C. Cardoso, Patricia Severino, and Eliana B. Souto. Classical and innovative drugs for the treatment of leishmania infections. Discover Public Health, Oct 2024. URL: https://doi.org/10.1186/s12982-024-00247-1, doi:10.1186/s12982-024-00247-1. This article has 6 citations and is from a peer-reviewed journal.

5. (fischer2024treatmentofmucocutaneous pages 2-2): Theresa Fischer, Marcellus Fischer, Sibylle Schliemann, and Peter Elsner. Treatment of mucocutaneous leishmaniasis – a systematic review. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 22:763-773, May 2024. URL: https://doi.org/10.1111/ddg.15424, doi:10.1111/ddg.15424. This article has 32 citations.

6. (sousa2024visceralleishmaniasistherapeutic pages 4-6): Júlia Santos Pinto de Sousa, Suzana Telles da Cunha Lima, Vitória Pereira de Oliveira, Esther Carvalho Nascimento, and Carlos Eduardo Sampaio Guedes. Visceral leishmaniasis: therapeutic challenges and the potential of microalgae as a source of antileishmanial compounds. Research, Society and Development, 13:e145131247645, Dec 2024. URL: https://doi.org/10.33448/rsd-v13i12.47645, doi:10.33448/rsd-v13i12.47645. This article has 0 citations.

7. (chivinski2023intravenousliposomalamphotericin pages 6-7): Jeffrey Chivinski, Keren Nathan, Faheel Naeem, Taline Ekmekjian, Michael D Libman, and Sapha Barkati. Intravenous liposomal amphotericin b efficacy and safety for cutaneous and mucosal leishmaniasis: a systematic review and meta-analysis. Open Forum Infectious Diseases, Jul 2023. URL: https://doi.org/10.1093/ofid/ofad348, doi:10.1093/ofid/ofad348. This article has 16 citations and is from a peer-reviewed journal.

8. (lindner2024americancutaneousleishmaniasis pages 2-4): Andreas K. Lindner, Maria Cristina Moreno-del Castillo, Mia Wintel, Gabriela Equihua Martinez, Joachim Richter, Florian Kurth, Frieder Pfäfflin, Thomas Zoller, Maximilian Gertler, Susanne Georgi, Michael Nürnberg, Claudia Hülso, Julian Bernhard, Sarah Konopelska Kotsias, Antonio Seigerschmidt, Welmoed van Loon, Frank Mockenhaupt, Beate Kampmann, and Gundel Harms. American cutaneous leishmaniasis: imported cases in berlin 2000–2023. PLOS Neglected Tropical Diseases, 18:e0012323, Jul 2024. URL: https://doi.org/10.1371/journal.pntd.0012323, doi:10.1371/journal.pntd.0012323. This article has 2 citations and is from a domain leading peer-reviewed journal.

9. (parkash2024safetyandreactogenicity pages 2-3): Vivak Parkash, Helen Ashwin, Shoumit Dey, Jovana Sadlova, Barbora Vojtkova, Katrien Van Bocxlaer, Rebecca Wiggins, David Thompson, Nidhi Sharma Dey, Charles L. Jaffe, Eli Schwartz, Petr Volf, Charles J. N. Lacey, Alison M. Layton, and Paul M. Kaye. Safety and reactogenicity of a controlled human infection model of sand fly-transmitted cutaneous leishmaniasis. Nature Medicine, 30:3150-3162, Aug 2024. URL: https://doi.org/10.1038/s41591-024-03146-9, doi:10.1038/s41591-024-03146-9. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (dey2024il32producingcd8+ pages 1-7): Nidhi S. Dey, Shoumit Dey, Naj Brown, Sujai Senarathne, Luiza Campos Reis, Ritika Sengupta, Jose Angelo L. Lindoso, Sally James, Lesley Gilbert, Mitali Chatterjee, Hiro Goto, Shalindra Ranasinghe, and Paul M. Kaye. Il-32 producing cd8+ memory t cells and tregs define the ido1 / pd-l1 niche in human cutaneous leishmaniasis skin lesions. MedRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.02.23300281, doi:10.1101/2024.01.02.23300281. This article has 5 citations.

11. (lodi2024immuneresponseto pages 10-11): Lorenzo Lodi, Marta Voarino, Silvia Stocco, Silvia Ricci, Chiara Azzari, Luisa Galli, and Elena Chiappini. Immune response to viscerotropic leishmania: a comprehensive review. Frontiers in Immunology, Sep 2024. URL: https://doi.org/10.3389/fimmu.2024.1402539, doi:10.3389/fimmu.2024.1402539. This article has 25 citations and is from a peer-reviewed journal.

12. (dey2024il32producingcd8+ pages 7-11): Nidhi S. Dey, Shoumit Dey, Naj Brown, Sujai Senarathne, Luiza Campos Reis, Ritika Sengupta, Jose Angelo L. Lindoso, Sally James, Lesley Gilbert, Mitali Chatterjee, Hiro Goto, Shalindra Ranasinghe, and Paul M. Kaye. Il-32 producing cd8+ memory t cells and tregs define the ido1 / pd-l1 niche in human cutaneous leishmaniasis skin lesions. MedRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.02.23300281, doi:10.1101/2024.01.02.23300281. This article has 5 citations.

13. (dey2024il32producingcd8+ pages 11-15): Nidhi S. Dey, Shoumit Dey, Naj Brown, Sujai Senarathne, Luiza Campos Reis, Ritika Sengupta, Jose Angelo L. Lindoso, Sally James, Lesley Gilbert, Mitali Chatterjee, Hiro Goto, Shalindra Ranasinghe, and Paul M. Kaye. Il-32 producing cd8+ memory t cells and tregs define the ido1 / pd-l1 niche in human cutaneous leishmaniasis skin lesions. MedRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.02.23300281, doi:10.1101/2024.01.02.23300281. This article has 5 citations.

14. (fowler2024neutrophilmediatedhypoxiadrives pages 1-2): Erin A. Fowler, Camila Farias Amorim, Klauss Mostacada, Allison Yan, Laís Amorim Sacramento, Rae A. Stanco, Emily D.S. Hales, Aditi Varkey, Wenjing Zong, Gary D. Wu, Camila I. de Oliveira, Patrick L. Collins, and Fernanda O. Novais. Neutrophil-mediated hypoxia drives pathogenic cd8+ t cell responses in cutaneous leishmaniasis. The Journal of Clinical Investigation, Jun 2024. URL: https://doi.org/10.1172/jci177992, doi:10.1172/jci177992. This article has 19 citations.

15. (khandibharad2024singlecellatacsequencing pages 1-2): Shweta Khandibharad and Shailza Singh. Single-cell atac sequencing identifies sleepy macrophages during reciprocity of cytokines in <i>l. major</i> infection. Microbiology Spectrum, Mar 2024. URL: https://doi.org/10.1128/spectrum.03478-23, doi:10.1128/spectrum.03478-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (gritti2024epidemiologicalclinicaland pages 30-35): Tommaso Gritti. Epidemiological, clinical and molecular characterization of tegumentary leishmaniasis in the emilia-romagna region. Text, Jan 2024. URL: https://doi.org/10.48676/unibo/amsdottorato/11146, doi:10.48676/unibo/amsdottorato/11146. This article has 0 citations and is from a peer-reviewed journal.

17. (balahbib2023cutaneousleishmaniasisphysiopathology pages 9-12): Abdelaali Balahbib, Asma Hmamouch, Aicha El Allam, Hikmat Douhri, Naoufal Dahaieh, Nasreddine El Omari, Jactty Chew, Long Chiau Ming, and Abdelhakim Bouyahya. Cutaneous leishmaniasis: physiopathology, molecular diagnostic, and therapeutic approaches. Progress In Microbes &amp; Molecular Biology, Dec 2023. URL: https://doi.org/10.36877/pmmb.a0000395, doi:10.36877/pmmb.a0000395. This article has 5 citations.

18. (balahbib2023cutaneousleishmaniasisphysiopathology pages 12-15): Abdelaali Balahbib, Asma Hmamouch, Aicha El Allam, Hikmat Douhri, Naoufal Dahaieh, Nasreddine El Omari, Jactty Chew, Long Chiau Ming, and Abdelhakim Bouyahya. Cutaneous leishmaniasis: physiopathology, molecular diagnostic, and therapeutic approaches. Progress In Microbes &amp; Molecular Biology, Dec 2023. URL: https://doi.org/10.36877/pmmb.a0000395, doi:10.36877/pmmb.a0000395. This article has 5 citations.

19. (gritti2024epidemiologicalclinicaland pages 35-39): Tommaso Gritti. Epidemiological, clinical and molecular characterization of tegumentary leishmaniasis in the emilia-romagna region. Text, Jan 2024. URL: https://doi.org/10.48676/unibo/amsdottorato/11146, doi:10.48676/unibo/amsdottorato/11146. This article has 0 citations and is from a peer-reviewed journal.

20. (gritti2024epidemiologicalclinicaland pages 39-44): Tommaso Gritti. Epidemiological, clinical and molecular characterization of tegumentary leishmaniasis in the emilia-romagna region. Text, Jan 2024. URL: https://doi.org/10.48676/unibo/amsdottorato/11146, doi:10.48676/unibo/amsdottorato/11146. This article has 0 citations and is from a peer-reviewed journal.

21. (dey2024il32producingcd8+ pages 19-22): Nidhi S. Dey, Shoumit Dey, Naj Brown, Sujai Senarathne, Luiza Campos Reis, Ritika Sengupta, Jose Angelo L. Lindoso, Sally James, Lesley Gilbert, Mitali Chatterjee, Hiro Goto, Shalindra Ranasinghe, and Paul M. Kaye. Il-32 producing cd8+ memory t cells and tregs define the ido1 / pd-l1 niche in human cutaneous leishmaniasis skin lesions. MedRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.02.23300281, doi:10.1101/2024.01.02.23300281. This article has 5 citations.

22. (chivinski2023intravenousliposomalamphotericin pages 1-2): Jeffrey Chivinski, Keren Nathan, Faheel Naeem, Taline Ekmekjian, Michael D Libman, and Sapha Barkati. Intravenous liposomal amphotericin b efficacy and safety for cutaneous and mucosal leishmaniasis: a systematic review and meta-analysis. Open Forum Infectious Diseases, Jul 2023. URL: https://doi.org/10.1093/ofid/ofad348, doi:10.1093/ofid/ofad348. This article has 16 citations and is from a peer-reviewed journal.

23. (chivinski2023intravenousliposomalamphotericin pages 7-9): Jeffrey Chivinski, Keren Nathan, Faheel Naeem, Taline Ekmekjian, Michael D Libman, and Sapha Barkati. Intravenous liposomal amphotericin b efficacy and safety for cutaneous and mucosal leishmaniasis: a systematic review and meta-analysis. Open Forum Infectious Diseases, Jul 2023. URL: https://doi.org/10.1093/ofid/ofad348, doi:10.1093/ofid/ofad348. This article has 16 citations and is from a peer-reviewed journal.

24. (fischer2024treatmentofmucocutaneous pages 4-4): Theresa Fischer, Marcellus Fischer, Sibylle Schliemann, and Peter Elsner. Treatment of mucocutaneous leishmaniasis – a systematic review. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 22:763-773, May 2024. URL: https://doi.org/10.1111/ddg.15424, doi:10.1111/ddg.15424. This article has 32 citations.

25. (fischer2024treatmentofmucocutaneous pages 6-7): Theresa Fischer, Marcellus Fischer, Sibylle Schliemann, and Peter Elsner. Treatment of mucocutaneous leishmaniasis – a systematic review. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 22:763-773, May 2024. URL: https://doi.org/10.1111/ddg.15424, doi:10.1111/ddg.15424. This article has 32 citations.

26. (pandey2021arandomizedopenlabel pages 3-4): Krishna Pandey, Biplab Pal, Niyamat Ali Siddiqui, Chandra Shekhar Lal, Vahab Ali, Sanjiva Bimal, Ashish Kumar, Neena Verma, Vidya Nand Rabi Das, Shubhankar Kumar Singh, Roshan Kamal Topno, and Pradeep Das. A randomized, open-label study to evaluate the efficacy and safety of liposomal amphotericin b (ambisome) versus miltefosine in patients with post-kala-azar dermal leishmaniasis. Indian Journal of Dermatology, Venereology and Leprology, 87:34-41, Feb 2021. URL: https://doi.org/10.25259/ijdvl\_410\_19, doi:10.25259/ijdvl\_410\_19. This article has 19 citations.

27. (parkash2024safetyandreactogenicity pages 1-2): Vivak Parkash, Helen Ashwin, Shoumit Dey, Jovana Sadlova, Barbora Vojtkova, Katrien Van Bocxlaer, Rebecca Wiggins, David Thompson, Nidhi Sharma Dey, Charles L. Jaffe, Eli Schwartz, Petr Volf, Charles J. N. Lacey, Alison M. Layton, and Paul M. Kaye. Safety and reactogenicity of a controlled human infection model of sand fly-transmitted cutaneous leishmaniasis. Nature Medicine, 30:3150-3162, Aug 2024. URL: https://doi.org/10.1038/s41591-024-03146-9, doi:10.1038/s41591-024-03146-9. This article has 17 citations and is from a highest quality peer-reviewed journal.

28. (parkash2024safetyeffectivenessand pages 13-17): Vivak Parkash, Helen Ashwin, Shoumit Dey, Jovana Sadlova, Barbora Vojtkova, Katrien Van Bocxlaer, Rebecca Wiggins, David Thompson, Nidhi Sharma Dey, Charles L. Jaffe, Eli Schwartz, Petr Volf, Charles J. N. Lacey, Alison M. Layton, and Paul M. Kaye. Safety, effectiveness, and skin immune response in a controlled human infection model of sand fly transmitted cutaneous leishmaniasis. MedRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.12.24305492, doi:10.1101/2024.04.12.24305492. This article has 1 citations.
