---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T09:01:02.092251'
end_time: '2026-05-11T09:13:04.500406'
duration_seconds: 722.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Feingold Syndrome
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
- **Disease Name:** Feingold Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Feingold Syndrome** covering all of the
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
- **Disease Name:** Feingold Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Feingold Syndrome** covering all of the
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


# Feingold Syndrome (Mendelian) — Comprehensive Disease Characteristics Report

## Target disease
**Disease name:** Feingold syndrome (Feingold syndrome type 1; Feingold syndrome type 2) (OpenTargets Search: Feingold syndrome)

**MONDO IDs (Open Targets):**
- Feingold syndrome: **MONDO_0015267** (OpenTargets Search: Feingold syndrome)
- Feingold syndrome type 1: **MONDO_0008115** (OpenTargets Search: Feingold syndrome)
- Feingold syndrome type 2: **MONDO_0013691** (OpenTargets Search: Feingold syndrome)

**OMIM:** Feingold syndrome type 1 **OMIM #164280** (klaniewska2021occurrenceofesophageal pages 1-2, nishio2024mycninhuman pages 1-2)

**Orphanet:** **ORPHA:391641** (klaniewska2021occurrenceofesophageal pages 1-2)

**Other identifiers (ICD-10/ICD-11, MeSH):** not retrievable from the tool-accessible corpus used here; should be completed from OMIM/Orphanet/MeSH browser in a production curation workflow.

**Common synonyms / alternative names:**
- Feingold syndrome
- Feingold syndrome type 1 (MYCN-related)
- Feingold syndrome type 2 (MIR17HG/miR-17~92-related)
- “oculodigitoesophagoduodenal (Feingold) syndrome” (zeka2022anewvariant pages 5-5)

**Evidence sources:** This report is derived from aggregated disease-level cohort studies and mechanistic animal-model studies (e.g., MYCN genotype–phenotype correlation cohort; MIR17HG deletion cohort; mouse models), supplemented by detailed human case reports and recent narrative reviews (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 2-4, nishio2024mycninhuman pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 1-2, muriello2019growthhormonedeficiency pages 2-4).

---

## 1. Disease information (overview)
Feingold syndrome is a rare, autosomal dominant, congenital malformation syndrome characterized principally by **microcephaly** and **digital skeletal anomalies** (notably brachymesophalangy/short middle phalanges and toe syndactyly), with variable additional findings including **gastrointestinal atresias** (esophageal/duodenal/other) and neurodevelopmental differences (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 1-2, zeka2022anewvariant pages 1-2).

Two main Mendelian subtypes are recognized:
- **Type 1 (FS1):** heterozygous **loss-of-function MYCN** variants (MYCN haploinsufficiency) (marcelis2008genotype–phenotypecorrelationsin pages 1-3, nishio2024mycninhuman pages 1-2)
- **Type 2 (FS2):** heterozygous **MIR17HG** deletions (haploinsufficiency of the **miR-17~92** cluster) (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 2-4)

Recent reviews emphasize MYCN’s broader developmental role beyond oncology and highlight “inverse” phenotypes caused by MYCN gain-of-function (megalencephaly-polydactyly syndrome) versus MYCN loss-of-function (Feingold syndrome) (Frontiers in Oncology; May 2024; https://doi.org/10.3389/fonc.2024.1417607) (nishio2024mycninhuman pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause (genetic):**
- **FS1:** heterozygous MYCN loss-of-function (nonsense/frameshift/PTC variants, certain missense in DNA-binding domain, and larger deletions) with evidence consistent with **haploinsufficiency** (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 2-4).
- **FS2:** heterozygous deletions affecting **MIR17HG** (miR-17~92 polycistron) on chromosome 13q31.3, with variable deletion sizes sometimes including neighboring genes (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 2-4).

**OpenTargets disease–target associations** support MYCN and MIR17HG as the top Feingold syndrome targets and provide literature cross-references (PubMed IDs listed by OpenTargets) (OpenTargets Search: Feingold syndrome).

### 2.2 Risk factors
For this Mendelian syndrome, “risk factors” largely correspond to **carrying a pathogenic variant** or inheriting it from an affected parent; intrafamilial variability is common.
- A three-generation family illustrates marked variable expressivity with a shared MYCN frameshift variant and variable occurrence of esophageal/duodenal atresia and neurodevelopmental findings (Frontiers in Pediatrics; Dec 2021; https://doi.org/10.3389/fped.2021.783553) (klaniewska2021occurrenceofesophageal pages 2-4, klaniewska2021occurrenceofesophageal pages 1-2).

### 2.3 Protective factors / gene–environment interactions
No protective variants or robust gene–environment interactions specific to Feingold syndrome were identified in the tool-accessible literature set. Given congenital onset and high-effect variants, classical G×E evidence is expected to be limited; future work could include modifier-gene discovery and quantitative trait modifier analyses.

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum with frequencies
#### FS1 (MYCN-related) — cohort-level frequencies
A genotype–phenotype study assembling **77 patients** with MYCN-related Feingold syndrome reported:
- **Brachymesophalangy:** **100%**
- **Toe syndactyly:** **97%**
- **Microcephaly/small head circumference:** **89%**
- **Gastrointestinal atresia:** **55%**
with additional “frequent” cardiac and renal anomalies (Human Mutation; Sep 2008; https://doi.org/10.1002/humu.20750) (marcelis2008genotype–phenotypecorrelationsin pages 1-3).

A later frequency summary compiled in a 2022 case report (reflecting prior series) reported: brachymesophalangy **95%**, microcephaly **86%**, toe syndactyly **80%**, short palpebral fissures **57%**, learning disability **41%**, and gastrointestinal atresia **38%** (Clinical Case Reports; May 2022; https://doi.org/10.1002/ccr3.5886) (zeka2022anewvariant pages 2-2).

#### FS2 (MIR17HG/miR-17~92-related) — cohort-level frequencies
A 2019 FS2 report provides a tabulated phenotype frequency summary across published/known cases:
- DD/ID/learning disability: **100% (16/16)**
- Brachymesophalangy: **100% (17/17)**
- 5th finger clinodactyly: **100% (9/9)**
- Microcephaly: **88% (14/16)**
- Short stature: **86% (13/14)**
- Toe syndactyly: **64% (9/14)**
- Thumb hypoplasia: **33% (4/12)**
- Cardiac defects: **40% (4/10)**
(American Journal of Medical Genetics Part A; Mar 2019; https://doi.org/10.1002/ajmg.a.61037) (muriello2019growthhormonedeficiency pages 2-4).

### 3.2 Phenotype characteristics (onset, severity, progression)
- **Onset:** typically **congenital/early life**, as digital anomalies, microcephaly, and GI atresias are present at birth or detected in infancy (klaniewska2021occurrenceofesophageal pages 1-2, muriello2019growthhormonedeficiency pages 2-4).
- **Severity:** variable expressivity is prominent, including intrafamilial variability; some individuals may show limited findings (e.g., microcephaly and mild learning differences) while others have complex GI malformations (klaniewska2021occurrenceofesophageal pages 2-4, klaniewska2021occurrenceofesophageal pages 1-2).
- **Progression:** largely **non-progressive structural** phenotype; growth and neurocognitive trajectories vary. FS2 may include endocrine/cardiovascular issues requiring longitudinal surveillance (muriello2019growthhormonedeficiency pages 5-6, muriello2019growthhormonedeficiency pages 2-4).

### 3.3 Suggested HPO terms (non-exhaustive)
- Microcephaly **HP:0000252**
- Brachymesophalangy **HP:0005930** (commonly 2nd/5th fingers)
- Clinodactyly **HP:0030084**
- Syndactyly of toes **HP:0004691**
- Hypoplastic thumb **HP:0009601**
- Esophageal atresia **HP:0002032** / Tracheoesophageal fistula **HP:0002564**
- Duodenal atresia **HP:0002249**
- Short stature **HP:0004322**
- Intellectual disability / developmental delay **HP:0001249 / HP:0001263**
- Congenital heart defect **HP:0001627**

### 3.4 Quality of life impact
No disease-specific QoL instrument data were identified in the retrieved set. Based on phenotype burden, QoL impact is expected to arise from (i) neonatal/infant surgery for GI atresia, (ii) feeding/growth issues, and (iii) neurodevelopmental and educational needs (klaniewska2021occurrenceofesophageal pages 2-4, muriello2019growthhormonedeficiency pages 2-4).

---

## 4. Genetic / molecular information
### 4.1 Causal genes
- **MYCN** (FS1): MYC-family bHLH transcription factor; heterozygous loss-of-function causes Feingold syndrome type 1 (marcelis2008genotype–phenotypecorrelationsin pages 1-3, nishio2024mycninhuman pages 1-2).
- **MIR17HG** (FS2): host gene encoding the **miR-17~92** microRNA cluster; heterozygous deletions cause Feingold syndrome type 2 (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 2-4).

### 4.2 Pathogenic variant classes and examples
- **MYCN:** frameshift variants segregating in families (e.g., c.266dupG/p.(Ser90GlnfsTer176)) (klaniewska2021occurrenceofesophageal pages 2-4); missense variants reported (e.g., c.1177C>T/p.Arg393Cys in a case report) (zeka2022anewvariant pages 1-2).
- **MIR17HG:** recurrently **CNV deletions** spanning MIR17HG (example deletion coordinates given in FS2 case compilation, e.g., arr[hg19] 91,491,721–99,522,261 for an ~8 Mb deletion) (muriello2019growthhormonedeficiency pages 2-4).

**Somatic vs germline:** Feingold syndrome is driven by **germline** pathogenic variation (marcelis2008genotype–phenotypecorrelationsin pages 1-3, muriello2019growthhormonedeficiency pages 1-2), while MYCN also has prominent **somatic** roles in cancer (reviewed in 2024) (nishio2024mycninhuman pages 1-2).

### 4.3 Modifier genes / contiguous gene effects
Large deletions involving MIR17HG often include additional genes; **GPC5** haploinsufficiency has been suggested as a potential modifier for limb/cardiac findings in some FS2 deletions (muriello2019growthhormonedeficiency pages 5-6, low2015tetralogyoffallot pages 1-2).

### 4.4 Epigenetic information
No Feingold-syndrome–specific methylation signatures were identified here. However, recent ncRNA-focused reviews discuss MIR17HG/miR-17~92 as a key developmental regulatory module relevant to microcephaly phenotypes (Frontiers in Cell and Developmental Biology; Jun 2023; https://doi.org/10.3389/fcell.2023.1168072) (tokunaga2023emergingconceptsinvolving pages 1-2).

---

## 5. Environmental information
No consistent environmental, lifestyle, toxicant, or infectious contributors were identified in this tool-accessible evidence base, consistent with Feingold syndrome’s classification as a Mendelian developmental disorder.

---

## 6. Mechanism / pathophysiology
### 6.1 Unifying developmental concept
Feingold syndrome is a **developmental growth and patterning disorder** affecting craniofacial/brain size and limb skeletogenesis, driven by dosage disruption of a transcription factor (MYCN) or its downstream microRNA effector cluster (miR-17~92). MYCN is expressed in multiple fetal tissues (brain, limbs, heart, kidney, lung), consistent with multisystem involvement (nishio2024mycninhuman pages 1-2).

### 6.2 Distinct downstream mechanisms in FS1 vs FS2 (functional evidence)
A key mechanistic advance is evidence that FS1 and FS2—despite overlapping skeletal phenotypes—can arise via **distinct pathway perturbations** in mesenchymal progenitors:
- **FS2 / Mir17-92 deficiency:** upregulation of **TGF-β signaling**, including derepression/upregulation of **Tgfbr2**, and pharmacologic/genetic TGF-β inhibition can rescue skeletal defects in mouse models (mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7).
- **FS1 / Mycn deficiency:** downregulation of **PI3K/Akt signaling** in limb mesenchymal cells; partial rescue by **Pten** heterozygosity, but not by TGF-β inhibition (mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7).

**Visual evidence (mouse-model figures):** a schematic contrasts these mechanisms and shows rescue experiments with TGF-β receptor inhibition (mirzamohammadi2018distinctmolecularpathways media f81b61fb, mirzamohammadi2018distinctmolecularpathways media 412f5292).

### 6.3 Suggested ontology terms
**GO biological processes (examples):**
- limb development; skeletal system development; regulation of cell proliferation; TGF-β receptor signaling pathway; PI3K signaling; mesenchymal cell proliferation.

**Cell Ontology (CL) terms (examples):**
- mesenchymal progenitor cell / limb bud mesenchyme cells (consistent with the functional mouse-model work) (mirzamohammadi2018distinctmolecularpathways pages 6-7).

---

## 7. Anatomical structures affected
### 7.1 Organ/system level (suggested UBERON mappings)
- Brain / head (microcephaly): **UBERON:0000955 (brain)**; **UBERON:0000033 (head)**
- Hands/feet/digits: **UBERON:0002387 (hand)**; **UBERON:0002389 (foot)**; digits/phalanges
- Gastrointestinal tract (atresias): **UBERON:0001043 (esophagus)**; **UBERON:0002114 (duodenum)**
- Heart (subset of cases): **UBERON:0000948 (heart)**
- Kidney (subset): **UBERON:0002113 (kidney)**

Multi-organ developmental expression of MYCN is emphasized in the 2024 review (nishio2024mycninhuman pages 1-2).

---

## 8. Temporal development
- **Typical onset:** congenital; structural anomalies may prompt neonatal surgery (atresia) and early dysmorphology evaluation (klaniewska2021occurrenceofesophageal pages 2-4, muriello2019growthhormonedeficiency pages 2-4).
- **Course:** chronic/lifelong, non-remitting congenital phenotype; neurodevelopmental and growth outcomes vary; FS2 may require ongoing endocrine and cardiovascular follow-up (muriello2019growthhormonedeficiency pages 5-6, muriello2019growthhormonedeficiency pages 2-4).

---

## 9. Inheritance and population
### 9.1 Inheritance
- Both FS1 and FS2 are consistent with **autosomal dominant inheritance** (heterozygous pathogenic variants/deletions), with **variable expressivity** and intrafamilial variability (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 2-4, muriello2019growthhormonedeficiency pages 1-2).

### 9.2 Epidemiology and available statistics
Robust population prevalence/incidence estimates were not identified in the retrieved evidence set. Available “rarity” indicators include:
- A 2022 case report notes incidence is unknown and that “nearly 200 cases are reported” since 1975 (zeka2022anewvariant pages 1-2).
- A 2021 family report notes “>120 patients reported in the literature” (klaniewska2021occurrenceofesophageal pages 1-2).

For context on one major presenting complication:
- General population prevalence of esophageal atresia (EA) quoted as **2.3–2.4 per 10,000 births** (klaniewska2021occurrenceofesophageal pages 1-2), and recurrence risk in siblings was summarized as **0.5–2%**, increasing up to **~20%** when another sibling is affected (as quoted in the Feingold-family EA report) (klaniewska2021occurrenceofesophageal pages 2-4).

---

## 10. Diagnostics
### 10.1 Clinical recognition
A large MYCN cohort analysis recommends **MYCN testing** when the combination of **brachymesophalangy + toe syndactyly + microcephaly** is present (marcelis2008genotype–phenotypecorrelationsin pages 1-3). Clinical suspicion increases with GI atresia or tracheoesophageal fistula and characteristic digital findings (klaniewska2021occurrenceofesophageal pages 1-2).

### 10.2 Genetic testing approaches (real-world implementation)
- **Single-gene MYCN testing** can be justified by classic digital patterning plus microcephaly (marcelis2008genotype–phenotypecorrelationsin pages 1-3).
- **Chromosomal microarray / CNV analysis** is important when a contiguous deletion is suspected (e.g., 2p24 deletions encompassing MYCN; 13q31 deletions involving MIR17HG) (zeka2022anewvariant pages 3-4, muriello2019growthhormonedeficiency pages 2-4).
- **Whole-exome sequencing (WES):** used to solve familial esophageal atresia and identify MYCN frameshift variants (klaniewska2021occurrenceofesophageal pages 2-4).
- **Genome sequencing (GS):** can identify multiple variant classes simultaneously (SNVs, CNVs, mosaic variants) and may be valuable in complex phenotypes with multiple diagnoses (zeka2022anewvariant pages 5-5).

### 10.3 Differential diagnosis (examples)
Differential considerations for microcephaly + limb anomalies + GI malformations include other syndromic microcephaly disorders and VACTERL-spectrum conditions; Feingold should remain on the differential even when some classic features are absent because variable expressivity is common (klaniewska2021occurrenceofesophageal pages 2-4, klaniewska2021occurrenceofesophageal pages 1-2).

---

## 11. Outcome / prognosis
No population-based survival statistics were identified. Prognosis appears driven by:
- severity and timing of repair of GI atresias (including complications such as postoperative strictures) (klaniewska2021occurrenceofesophageal pages 2-4),
- neurodevelopmental profile and learning support needs (muriello2019growthhormonedeficiency pages 2-4), and
- cardiac/endocrine complications in FS2 (recommendations below) (muriello2019growthhormonedeficiency pages 5-6).

---

## 12. Treatment
Feingold syndrome has no established disease-modifying molecular therapy in humans; management is **supportive**, multidisciplinary, and complication-directed.

### 12.1 Surgical and interventional
- **Surgical repair of esophageal/duodenal atresia / tracheoesophageal fistula** is a key real-world intervention when present; family case reports describe EA with TEF and postoperative complications such as anastomotic stricture (klaniewska2021occurrenceofesophageal pages 2-4).

**Suggested MAXO terms:** surgical repair of congenital gastrointestinal atresia; esophageal atresia repair.

### 12.2 Supportive, rehabilitative, and surveillance
- FS2 management recommendations include **echocardiography at diagnosis** for all patients and consideration of **growth hormone deficiency evaluation** in short stature (muriello2019growthhormonedeficiency pages 1-2).
- A FS2 patient was “treated successfully with growth hormone” (muriello2019growthhormonedeficiency pages 1-2).

**Suggested MAXO terms:** echocardiographic monitoring; endocrine evaluation; growth hormone therapy.

### 12.3 Experimental therapies / clinical trials
A ClinicalTrials.gov search using the disease name retrieved no Feingold-syndrome–specific interventional trials in this tool run (clinical trials tool state indicated 1 trial found but none were returned as relevant records), consistent with the current supportive-care paradigm.

---

## 13. Prevention
### 13.1 Genetic counseling (primary prevention)
Because Feingold syndrome is autosomal dominant, prevention focuses on **genetic counseling** for affected individuals and at-risk families, including discussion of variable expressivity (klaniewska2021occurrenceofesophageal pages 2-4, klaniewska2021occurrenceofesophageal pages 1-2).

**Suggested MAXO terms:** genetic counseling; cascade genetic testing.

### 13.2 Secondary/tertiary prevention
- Early diagnosis enables anticipatory guidance for GI surgery planning (when prenatal anomalies are detected) and early developmental intervention.
- For FS2, early cardiac and endocrine screening may prevent complications (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 5-6).

---

## 14. Other species / natural disease
No naturally occurring veterinary Feingold-syndrome analogs were identified in the retrieved set.

---

## 15. Model organisms
### 15.1 Mouse models (in vivo)
A high-impact mechanistic study used conditional deletions in mouse limb mesenchyme to model FS2 (Mir17-92 deficiency) and FS1 (Mycn deficiency), demonstrating both phenotypic overlap (skeletal defects, microcephaly-like cranial defects) and distinct downstream pathway signatures (TGF-β vs PI3K) (Nature Communications; Apr 2018; https://doi.org/10.1038/s41467-018-03788-7) (mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7). Rescue of FS2-like skeletal defects by TGF-β inhibition supports a causal chain for miR-17~92 haploinsufficiency (mirzamohammadi2018distinctmolecularpathways media f81b61fb, mirzamohammadi2018distinctmolecularpathways media 412f5292).

### 15.2 Model limitations
These models robustly recapitulate limb and cranial skeletal findings, but congenital GI atresias and full neurodevelopmental phenotypes may be incompletely represented depending on tissue specificity and timing of gene deletion.

---

## Recent developments and expert synthesis (prioritizing 2023–2024)
1. **MYCN’s developmental role and “inverse phenotype” paradigm (2024):** A 2024 review synthesizes evidence that MYCN loss-of-function causes FS1, while specific MYCN gain-of-function variants cause an opposite brain-growth phenotype (megalencephaly-polydactyly syndrome), helping refine MYCN dosage/function models in human development (Frontiers in Oncology; May 2024; https://doi.org/10.3389/fonc.2024.1417607) (nishio2024mycninhuman pages 1-2).
2. **ncRNA framing of Feingold microcephaly (2023):** A 2023 review places Feingold syndrome within broader ncRNA biology of microcephaly and highlights MIR17HG/miR-17~92 composition and apoptosis-related mechanisms (e.g., BIM derepression), reinforcing noncoding RNA dosage as a key developmental determinant (Frontiers in Cell and Developmental Biology; Jun 2023; https://doi.org/10.3389/fcell.2023.1168072) (tokunaga2023emergingconceptsinvolving pages 1-2).
3. **Mechanism-to-rescue logic (translational potential):** Although still preclinical, mouse-model rescue of FS2 skeletal defects via TGF-β inhibition provides a concrete pathway-based hypothesis for future therapeutics, while concurrently showing FS1 may require PI3K/Akt-directed strategies rather than TGF-β inhibition (mirzamohammadi2018distinctmolecularpathways pages 6-7, mirzamohammadi2018distinctmolecularpathways media f81b61fb).

---

## Structured summary table (FS1 vs FS2)
| Type | Causal gene/locus | Typical variant class | Inheritance | Core features | Key quantitative phenotype frequencies reported | Mechanistic/pathway notes | Key references with year/DOI/PMID if available |
|---|---|---|---|---|---|---|---|
| Feingold syndrome type 1 | **MYCN** (2p24.3); MONDO also maps Feingold syndrome to MYCN associations (OpenTargets Search: Feingold syndrome, marcelis2008genotype–phenotypecorrelationsin pages 1-3) | Predominantly heterozygous loss-of-function variants: nonsense, frameshift, splice/PTC variants; missense variants in DNA-binding domain; larger 2p24 deletions including **MYCN** also reported (marcelis2008genotype–phenotypecorrelationsin pages 1-3, zeka2022anewvariant pages 3-4, klaniewska2021occurrenceofesophageal pages 1-2, zeka2022anewvariant pages 1-2) | Autosomal dominant with variable expressivity; familial and de novo cases reported (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 2-4, zeka2022anewvariant pages 1-2) | Microcephaly, digital anomalies (especially brachymesophalangy of 2nd/5th fingers, toe syndactyly), short stature, gastrointestinal atresia; additional learning/developmental issues and occasional cardiac/renal/hearing anomalies (marcelis2008genotype–phenotypecorrelationsin pages 1-3, klaniewska2021occurrenceofesophageal pages 1-2, zeka2022anewvariant pages 1-2, zeka2022anewvariant pages 2-2) | **MYCN cohort, n=77 (Marcelis 2008):** brachymesophalangy **100%**, toe syndactyly **97%**, microcephaly/small head circumference **89%**, gastrointestinal atresia **55%**; cardiac and renal anomalies described as frequent (marcelis2008genotype–phenotypecorrelationsin pages 1-3). Another summarized review/case source reports brachymesophalangy **95%**, microcephaly **86%**, toe syndactyly **80%**, short palpebral fissures **57%**, learning disability **41%**, gastrointestinal atresia **38%**, cardiac **14%**, renal **5%**, hearing loss **7%** (zeka2022anewvariant pages 2-2). | Human and mouse data support haploinsufficiency. In limb mesenchyme, **Mycn** deficiency is linked mainly to **downregulated PI3K/Akt signaling**; skeletal phenotype was partially rescued by **Pten** heterozygosity, but not by TGF-β inhibition, indicating a pathway distinct from type 2 (mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7). | Marcelis et al., **2008**, *Human Mutation*, DOI: **10.1002/humu.20750** (marcelis2008genotype–phenotypecorrelationsin pages 1-3); Klaniewska et al., **2021**, DOI: **10.3389/fped.2021.783553** (klaniewska2021occurrenceofesophageal pages 2-4, klaniewska2021occurrenceofesophageal pages 1-2); Zeka et al., **2022**, DOI: **10.1002/ccr3.5886** (zeka2022anewvariant pages 1-2, zeka2022anewvariant pages 2-2); Nishio et al., **2024**, DOI: **10.3389/fonc.2024.1417607** (nishio2024mycninhuman pages 1-2) |
| Feingold syndrome type 2 | **MIR17HG** / miR-17~92 cluster (13q31.3); Open Targets also links Feingold syndrome type 2 to MIR17HG (OpenTargets Search: Feingold syndrome, muriello2019growthhormonedeficiency pages 1-2) | Usually heterozygous germline deletions/CNV losses involving **MIR17HG** (sometimes with neighboring genes such as **GPC5**); pathogenic mechanism is miR-17~92 haploinsufficiency (muriello2019growthhormonedeficiency pages 1-2, low2015tetralogyoffallot pages 1-2, muriello2019growthhormonedeficiency pages 2-4) | Autosomal dominant / dominant transmission of hemizygous loss; familial segregation reported in some families (muriello2019growthhormonedeficiency pages 1-2, low2015tetralogyoffallot pages 1-2) | Microcephaly, short stature, brachymesophalangy/digital anomalies, toe syndactyly, learning or developmental problems; variable cardiac anomalies; reported expansions include growth hormone deficiency, aortic dilation, joint contractures, memory/sleep issues (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 5-6, muriello2019growthhormonedeficiency pages 2-4) | **MIR17HG deletion cohort frequencies (Muriello 2019):** DD/ID/learning disability **100% (16/16)**, brachymesophalangy **100% (17/17)**, 5th finger clinodactyly **100% (9/9)**, microcephaly **88% (14/16)**, short stature **86% (13/14)**, toe syndactyly **64% (9/14)**, thumb hypoplasia **33% (4/12)**, cardiac defects **40% (4/10)** (muriello2019growthhormonedeficiency pages 2-4). Earlier diagnostic series found **MIR17HG deletions in 2/10** tested suspected Feingold cases (low2015tetralogyoffallot pages 1-2). | Mouse and functional data indicate **Mir17-92 deficiency upregulates TGF-β signaling**, including derepression of **Tgfbr2**; genetic or pharmacologic **TGF-β inhibition** rescued skeletal defects. This contrasts with FS1, where the dominant perturbation is PI3K/Akt downregulation (mirzamohammadi2018distinctmolecularpathways pages 2-3, mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7, tokunaga2023emergingconceptsinvolving pages 1-2). | de Pontual et al., **2011**, *Nature Genetics*, DOI: **10.1038/ng.915** (low2015tetralogyoffallot pages 1-2); Muriello et al., **2019**, *Am J Med Genet A*, DOI: **10.1002/ajmg.a.61037** (muriello2019growthhormonedeficiency pages 1-2, muriello2019growthhormonedeficiency pages 2-4); Mirzamohammadi et al., **2018**, *Nature Communications*, DOI: **10.1038/s41467-018-03788-7** (mirzamohammadi2018distinctmolecularpathways pages 2-3, mirzamohammadi2018distinctmolecularpathways pages 1-2, mirzamohammadi2018distinctmolecularpathways pages 6-7) |


*Table: This table compares Feingold syndrome types 1 and 2 across causal loci, variant classes, inheritance, hallmark phenotypes, quantitative frequencies, and mechanistic distinctions. It is useful for quickly contrasting MYCN-associated and MIR17HG-associated disease for diagnostic and knowledge-base curation.*

---

## Evidence limitations and curation gaps
- ICD-10/ICD-11 and MeSH identifiers were not available in the tool-retrieved evidence set and should be added from authoritative terminologies.
- Many statements about penetrance, genotype-specific outcomes, and population prevalence remain incompletely quantified in accessible cohort data; most statistics are cohort-derived rather than population-based.
- For PMID-preferred citations: OpenTargets lists PubMed IDs for key gene–disease associations, but PMIDs were not directly extracted from full-text in this run; future curation should add PMIDs by cross-referencing DOIs to PubMed (OpenTargets Search: Feingold syndrome).

References

1. (OpenTargets Search: Feingold syndrome): Open Targets Query (Feingold syndrome, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (klaniewska2021occurrenceofesophageal pages 1-2): Magdalena Klaniewska, Krystian Toczewski, Anna Rozensztrauch, Michal Bloch, Agata Dzielendziak, Piotr Gasperowicz, Ryszard Slezak, Rafał Ploski, Małgorzata Rydzanicz, Robert Smigiel, and Dariusz Patkowski. Occurrence of esophageal atresia with tracheoesophageal fistula in siblings from three-generation family affected by variable expressivity mycn mutation: a case report. Frontiers in Pediatrics, Dec 2021. URL: https://doi.org/10.3389/fped.2021.783553, doi:10.3389/fped.2021.783553. This article has 6 citations.

3. (nishio2024mycninhuman pages 1-2): Yosuke Nishio, Kohji Kato, Hisashi Oishi, Yoshiyuki Takahashi, and Shinji Saitoh. Mycn in human development and diseases. Frontiers in Oncology, May 2024. URL: https://doi.org/10.3389/fonc.2024.1417607, doi:10.3389/fonc.2024.1417607. This article has 8 citations.

4. (zeka2022anewvariant pages 5-5): Naim Zeka, Ramush Bejiqi, Abdurrahim Gerguri, Leonore Zogaj, and Haki Jashari. A new variant of mycn gene as a cause of feingold syndrome. Clinical Case Reports, May 2022. URL: https://doi.org/10.1002/ccr3.5886, doi:10.1002/ccr3.5886. This article has 4 citations.

5. (marcelis2008genotype–phenotypecorrelationsin pages 1-3): Carlo L.M. Marcelis, Frans A. Hol, Gail E. Graham, Paul N.M.A. Rieu, Richard Kellermayer, Rowdy P.P. Meijer, Dorien Lugtenberg, Hans Scheffer, Hans van Bokhoven, Han G. Brunner, and Arjan P.M. de Brouwer. Genotype–phenotype correlations in mycn‐related feingold syndrome. Human Mutation, 29:1125-1132, Sep 2008. URL: https://doi.org/10.1002/humu.20750, doi:10.1002/humu.20750. This article has 105 citations and is from a domain leading peer-reviewed journal.

6. (klaniewska2021occurrenceofesophageal pages 2-4): Magdalena Klaniewska, Krystian Toczewski, Anna Rozensztrauch, Michal Bloch, Agata Dzielendziak, Piotr Gasperowicz, Ryszard Slezak, Rafał Ploski, Małgorzata Rydzanicz, Robert Smigiel, and Dariusz Patkowski. Occurrence of esophageal atresia with tracheoesophageal fistula in siblings from three-generation family affected by variable expressivity mycn mutation: a case report. Frontiers in Pediatrics, Dec 2021. URL: https://doi.org/10.3389/fped.2021.783553, doi:10.3389/fped.2021.783553. This article has 6 citations.

7. (mirzamohammadi2018distinctmolecularpathways pages 1-2): Fatemeh Mirzamohammadi, Anastasia Kozlova, Garyfallia Papaioannou, Elena Paltrinieri, Ugur M. Ayturk, and Tatsuya Kobayashi. Distinct molecular pathways mediate mycn and myc-regulated mir-17-92 microrna action in feingold syndrome mouse models. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03788-7, doi:10.1038/s41467-018-03788-7. This article has 25 citations and is from a highest quality peer-reviewed journal.

8. (muriello2019growthhormonedeficiency pages 2-4): Michael Muriello, Alexander Y. Kim, Krista Sondergaard Schatz, Natalie Beck, Meral Gunay‐Aygun, and Julie E. Hoover‐Fong. Growth hormone deficiency, aortic dilation, and neurocognitive issues in feingold syndrome 2. American Journal of Medical Genetics Part A, 179:410-416, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61037, doi:10.1002/ajmg.a.61037. This article has 16 citations.

9. (zeka2022anewvariant pages 1-2): Naim Zeka, Ramush Bejiqi, Abdurrahim Gerguri, Leonore Zogaj, and Haki Jashari. A new variant of mycn gene as a cause of feingold syndrome. Clinical Case Reports, May 2022. URL: https://doi.org/10.1002/ccr3.5886, doi:10.1002/ccr3.5886. This article has 4 citations.

10. (muriello2019growthhormonedeficiency pages 1-2): Michael Muriello, Alexander Y. Kim, Krista Sondergaard Schatz, Natalie Beck, Meral Gunay‐Aygun, and Julie E. Hoover‐Fong. Growth hormone deficiency, aortic dilation, and neurocognitive issues in feingold syndrome 2. American Journal of Medical Genetics Part A, 179:410-416, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61037, doi:10.1002/ajmg.a.61037. This article has 16 citations.

11. (zeka2022anewvariant pages 2-2): Naim Zeka, Ramush Bejiqi, Abdurrahim Gerguri, Leonore Zogaj, and Haki Jashari. A new variant of mycn gene as a cause of feingold syndrome. Clinical Case Reports, May 2022. URL: https://doi.org/10.1002/ccr3.5886, doi:10.1002/ccr3.5886. This article has 4 citations.

12. (muriello2019growthhormonedeficiency pages 5-6): Michael Muriello, Alexander Y. Kim, Krista Sondergaard Schatz, Natalie Beck, Meral Gunay‐Aygun, and Julie E. Hoover‐Fong. Growth hormone deficiency, aortic dilation, and neurocognitive issues in feingold syndrome 2. American Journal of Medical Genetics Part A, 179:410-416, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61037, doi:10.1002/ajmg.a.61037. This article has 16 citations.

13. (low2015tetralogyoffallot pages 1-2): Karen J. Low, Chris C. Buxton, and Ruth A. Newbury-Ecob. Tetralogy of fallot, microcephaly, short stature and brachymesophalangy is associated with hemizygous loss of noncoding mir17hg and coding gpc5. Clinical dysmorphology, 24 3:113-4, Jul 2015. URL: https://doi.org/10.1097/mcd.0000000000000069, doi:10.1097/mcd.0000000000000069. This article has 9 citations and is from a peer-reviewed journal.

14. (tokunaga2023emergingconceptsinvolving pages 1-2): Mayuri Tokunaga and Takuya Imamura. Emerging concepts involving inhibitory and activating rna functionalization towards the understanding of microcephaly phenotypes and brain diseases in humans. Frontiers in Cell and Developmental Biology, Jun 2023. URL: https://doi.org/10.3389/fcell.2023.1168072, doi:10.3389/fcell.2023.1168072. This article has 0 citations.

15. (mirzamohammadi2018distinctmolecularpathways pages 6-7): Fatemeh Mirzamohammadi, Anastasia Kozlova, Garyfallia Papaioannou, Elena Paltrinieri, Ugur M. Ayturk, and Tatsuya Kobayashi. Distinct molecular pathways mediate mycn and myc-regulated mir-17-92 microrna action in feingold syndrome mouse models. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03788-7, doi:10.1038/s41467-018-03788-7. This article has 25 citations and is from a highest quality peer-reviewed journal.

16. (mirzamohammadi2018distinctmolecularpathways media f81b61fb): Fatemeh Mirzamohammadi, Anastasia Kozlova, Garyfallia Papaioannou, Elena Paltrinieri, Ugur M. Ayturk, and Tatsuya Kobayashi. Distinct molecular pathways mediate mycn and myc-regulated mir-17-92 microrna action in feingold syndrome mouse models. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03788-7, doi:10.1038/s41467-018-03788-7. This article has 25 citations and is from a highest quality peer-reviewed journal.

17. (mirzamohammadi2018distinctmolecularpathways media 412f5292): Fatemeh Mirzamohammadi, Anastasia Kozlova, Garyfallia Papaioannou, Elena Paltrinieri, Ugur M. Ayturk, and Tatsuya Kobayashi. Distinct molecular pathways mediate mycn and myc-regulated mir-17-92 microrna action in feingold syndrome mouse models. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03788-7, doi:10.1038/s41467-018-03788-7. This article has 25 citations and is from a highest quality peer-reviewed journal.

18. (zeka2022anewvariant pages 3-4): Naim Zeka, Ramush Bejiqi, Abdurrahim Gerguri, Leonore Zogaj, and Haki Jashari. A new variant of mycn gene as a cause of feingold syndrome. Clinical Case Reports, May 2022. URL: https://doi.org/10.1002/ccr3.5886, doi:10.1002/ccr3.5886. This article has 4 citations.

19. (mirzamohammadi2018distinctmolecularpathways pages 2-3): Fatemeh Mirzamohammadi, Anastasia Kozlova, Garyfallia Papaioannou, Elena Paltrinieri, Ugur M. Ayturk, and Tatsuya Kobayashi. Distinct molecular pathways mediate mycn and myc-regulated mir-17-92 microrna action in feingold syndrome mouse models. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03788-7, doi:10.1038/s41467-018-03788-7. This article has 25 citations and is from a highest quality peer-reviewed journal.