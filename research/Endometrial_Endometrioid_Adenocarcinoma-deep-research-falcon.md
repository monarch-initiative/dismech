---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T09:19:31.372159'
end_time: '2026-05-08T09:35:40.452557'
duration_seconds: 969.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Endometrial Endometrioid Adenocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Endometrial Endometrioid Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Endometrial Endometrioid Adenocarcinoma** covering all of the
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
- **Disease Name:** Endometrial Endometrioid Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Endometrial Endometrioid Adenocarcinoma** covering all of the
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


# Endometrial Endometrioid Adenocarcinoma (EEC): Comprehensive Disease Characteristics Report (2023–2024 emphasis)

## Target Disease
- **Disease name:** Endometrial endometrioid adenocarcinoma (endometrioid endometrial carcinoma; “endometrioid” histotype of endometrial carcinoma) (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3)
- **Ontology/identifier notes (available from retrieved sources):** Open Targets returns the disease as **EFO_1000233 “Endometrial Endometrioid Adenocarcinoma”** (OpenTargets Search: endometrioid endometrial adenocarcinoma,endometrial carcinoma).
- **Key external IDs (ICD-10/ICD-11/MeSH/MONDO/OMIM/Orphanet):** Not retrieved with the current tool evidence; therefore not reported here.
- **Category:** Malignant epithelial tumor of the uterine corpus endometrium; histologic subtype of endometrial carcinoma (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3).

### Common synonyms / alternative names
- Endometrioid endometrial carcinoma (EEC) (nagel2024predictivebiomarkersin pages 1-2)
- Endometrioid adenocarcinoma of the endometrium / endometrioid adenocarcinoma (uterus) (yasuda2024newclinicopathologicalconcept pages 1-3)

### Evidence type note
This report is derived from **aggregated disease-level resources** (peer-reviewed reviews, meta-analyses, clinical trials, registry analyses) and one **real-world institutional screening implementation study** (nagel2024predictivebiomarkersin pages 2-4, ruscelli2023prognosticimpactof pages 1-2, wilson2023systematicreviewand pages 1-2, liu2023differentialtrendsin pages 2-4).

---

## 1. Disease information (definition and current understanding)

### Concise overview
Endometrial endometrioid adenocarcinoma is the most common histologic type of endometrial carcinoma, arising from the endometrial lining and typically showing gland-forming “endometrioid” architecture with FIGO grading based on solid growth (yang2024molecularsubtypesof pages 4-5, yasuda2024newclinicopathologicalconcept pages 1-3). EEC has historically been described as estrogen-associated (“type I”) in contrast to less common non-endometrioid “type II” tumors (nagel2024predictivebiomarkersin pages 1-2).

### Histopathologic definition and grading
Yasuda (2024) describes endometrioid adenocarcinoma as “a malignant tumor with varying proportions of glandular, papillary, and solid architectures” and outlines FIGO grading thresholds (G1 <5% solid; G2 6–50%; G3 >50%), often simplified as low grade (G1–2) vs high grade (G3) (yasuda2024newclinicopathologicalconcept pages 1-3).

### Molecular classification now integrated into routine practice
Multiple 2024 reviews emphasize that the TCGA-derived 4-group molecular taxonomy has been translated into pragmatic classifiers (ProMisE/TransPORTEC) and is being integrated into pathology reporting and staging (WHO 2020; FIGO 2023) (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3).

---

## 2. Etiology

### Primary causal factors (mechanistic framing)
EEC is commonly conceptualized as an estrogen-driven malignancy in which hormonal and metabolic contexts (obesity, hyperestrogenism, insulin resistance) promote endometrial proliferation and progression to carcinoma, with cooperating somatic genomic alterations defining molecular subtypes and therapeutic vulnerabilities (clontz2024effectsofweight pages 1-2, ribeirosantos2024tailoringendometrialcancer pages 2-3).

### Risk factors (quantitative, recent where possible)

#### Metabolic/hormonal risk factors
- **Obesity and metabolic dysfunction:** A 2024 meta-analysis of metabolic obesity phenotypes reported that **metabolically unhealthy overweight/obese** individuals had substantially higher endometrial cancer risk vs metabolically healthy normal weight (**SRR 2.31, 95% CI 2.08–2.57; high certainty**) (Mahamat‑saleh et al., *Br J Cancer*, published 2024-09-??; https://doi.org/10.1038/s41416-024-02857-7) (mahamatsaleh2024associationofmetabolic pages 1-2).
- **Polycystic ovary syndrome (PCOS):** A 2023 meta-analysis concluded: “**Females with PCOS had a significantly increased odds of developing endometrial cancer**” with **OR 4.07 (95% CI 2.13–7.78)**, and when excluding postmenopausal subjects the odds increased to **OR 5.14 (95% CI 3.22–8.21)** (Johnson et al., *Oncology Letters*, 2023-03-??; https://doi.org/10.3892/ol.2023.13754) (johnson2023riskofendometrial pages 1-2).
- **Age/menopause context:** Reviews emphasize endometrioid cancers are often diagnosed in peri-/postmenopausal women and obesity is particularly relevant post-menopause due to adipose aromatase as a major estrogen source (clontz2024effectsofweight pages 1-2, ribeirosantos2024tailoringendometrialcancer pages 2-3).

#### Hereditary predisposition (genetic etiology)
- **Lynch syndrome (LS):** A 2023 review notes LS is estimated to be the hereditary cause in **~3% of endometrial cancer** and that LS-related tumors often demonstrate an MMR-deficient (MMRd) pattern detectable by IHC (Capasso et al., *Cancers*, 2023-02-??; https://doi.org/10.3390/cancers15051400) ().

### Protective factors (quantitative)
- **Bariatric surgery (obesity intervention):** A 2023 systematic review/meta-analysis reported bariatric surgery was associated with reduced future incidence of endometrial cancer (**RR 0.38, 95% CI 0.26–0.55**) (Wilson et al., *Int J Mol Sci*, 2023-03-??; https://doi.org/10.3390/ijms24076192) (wilson2023systematicreviewand pages 1-2).
- **Weight loss effects on mechanistic biomarkers:** A 2024 systematic review/meta-analysis reported bariatric surgery produced an overall **25.8% weight reduction** and weight loss reduced inflammatory biomarkers linked to endometrioid EC risk (e.g., **CRP −33.5%**, **IL-6 −41.9%**) (Clontz et al., *Cancers*, 2024-06-??; https://doi.org/10.3390/cancers16122197) (clontz2024effectsofweight pages 18-19).

### Gene–environment interactions (current state)
The retrieved evidence supports a strong interaction framework in which environmental/metabolic exposures (obesity, insulin resistance, inflammatory milieu) act upstream of signaling pathways frequently altered in endometrioid EC (e.g., PI3K/AKT/mTOR), but specific, validated **variant-by-exposure interaction effect sizes** were not retrieved in the current corpus (clontz2024effectsofweight pages 18-19).

---

## 3. Phenotypes (clinical presentation, pathology; HPO suggestions)

### Common presentation and key clinicopathologic traits
While the most common symptom (abnormal uterine bleeding) is not explicitly captured in the retrieved excerpts, EEC is emphasized as the dominant endometrial cancer histotype and is frequently diagnosed at early stage (often localized) in population-based datasets (liu2023differentialtrendsin pages 2-4). Yasuda (2024) provides histotype distribution in a referenced series with endometrioid adenocarcinoma grades: **G1 54.1%, G2 18.9%, G3 8.7%** (yasuda2024newclinicopathologicalconcept pages 1-3).

### Suggested phenotype (HPO) terms (not exhaustive)
- Abnormal uterine bleeding (**HP:0000132**)
- Postmenopausal bleeding (**HP:0000858**)
- Pelvic pain (**HP:0030834**)
- Anemia (**HP:0001903**) (secondary)
- Endometrial neoplasm / carcinoma (HPO term availability varies; may map via disease ontology)

**Phenotype frequency and QoL impact:** Not systematically retrievable from current excerpts; would require symptom-focused cohort studies.

---

## 4. Genetic / Molecular information

### 4.1 Clinically used molecular subtypes (TCGA / ProMisE)
Contemporary clinical practice increasingly applies the TCGA-derived four molecular classes operationalized by ProMisE/TransPORTEC using POLE sequencing plus MMR and p53 IHC surrogates: **POLEmut**, **MMRd/MSI-H**, **p53abn**, and **NSMP** (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3).

| Molecular subtype | Defining tests / practical surrogates | Typical frequency reported in retrieved sources | General prognosis | Key therapy implications |
|---|---|---|---|---|
| POLEmut / ultramutated | Pathogenic **POLE exonuclease-domain** mutation by sequencing/NGS; in ProMisE workflow, POLE testing is integrated with MMR and p53 IHC, and WHO 2020 prioritizes POLEmut classification when present | ~**7–10%** overall in EC; **7.8%** in Ruscelli 2023 cohort; ~**10%** in Yasuda 2024; **8–10%** overall and **6.4% low-grade endometrioid / 17.4% high-grade endometrioid** in TCGA summary cited by Ribeiro-Santos 2024; **7%** in Yang 2024 (ruscelli2023prognosticimpactof pages 1-2, yasuda2024newclinicopathologicalconcept pages 3-4, ribeirosantos2024tailoringendometrialcancer pages 2-3, yang2024molecularsubtypesof pages 4-5, yasuda2024newclinicopathologicalconcept pages 1-3) | **Excellent / best** prognosis, even when conventional histology appears high risk (nagel2024predictivebiomarkersin pages 2-4, yasuda2024newclinicopathologicalconcept pages 3-4, ruscelli2023prognosticimpactof pages 1-2) | Supports **adjuvant de-escalation/observation** in appropriate early-stage patients; POLE tumors appear to derive little benefit from adjuvant radiotherapy; FIGO 2023 incorporates **IAm_POLEmut** modifier (nagel2024predictivebiomarkersin pages 2-4, yasuda2024newclinicopathologicalconcept pages 1-3, berek2023figostagingof media 9e3676d6) |
| MMRd / MSI-H / hypermutated | Loss of **MLH1, PMS2, MSH2, or MSH6** by IHC; MSI testing by PCR/NGS as adjunct; if MLH1/PMS2 loss, reflex **MLH1 promoter hypermethylation** testing helps distinguish sporadic cases from Lynch syndrome-associated tumors | Commonly ~**24–32%** overall; **31.0%** in Ruscelli 2023; **32.2%** in de Biase 2023; **28%** in Yang 2024; ~**30%** MSI/MMRd noted in Addante 2024; Yasuda 2024 reports MSI in ~**40% of endometrioid adenocarcinomas** (ruscelli2023prognosticimpactof pages 1-2, yang2024molecularsubtypesof pages 4-5, addante2024mismatchrepairdeficiency pages 3-5, yasuda2024newclinicopathologicalconcept pages 3-4) | **Intermediate** prognosis overall, but heterogeneous; MLH1-hypermethylated/sporadic MMRd may behave worse than Lynch-like/germline-associated MMRd subsets (addante2024mismatchrepairdeficiency pages 3-5, yasuda2024newclinicopathologicalconcept pages 3-4) | Strongest current implication is **immune checkpoint inhibitor sensitivity/eligibility**: anti–PD-1/PD-L1 therapies in advanced/recurrent disease; first-line chemo-immunotherapy shows especially large benefit in dMMR populations; also central for **Lynch syndrome universal screening** (nagel2024predictivebiomarkersin pages 2-4, mirza2023dostarlimabforprimary pages 10-11, mirza2023dostarlimabforprimary pages 1-3, eskander2023pembrolizumabpluschemotherapy pages 6-7, eskander2023pembrolizumabpluschemotherapy pages 1-3, addante2024mismatchrepairdeficiency pages 3-5) |
| NSMP / copy-number low / p53wt | No pathogenic POLE mutation, **MMR retained** by IHC, and **wild-type p53** staining pattern; assigned after exclusion of POLEmut, MMRd, and p53abn in practical classifiers | Often the **largest subgroup**: **39.3%** in de Biase 2023; **40.2%** in Ruscelli 2023; **39%** in Yang 2024; ~**60%** of low copy-number tumors are low-grade endometrioid in TCGA summary cited by Ribeiro-Santos 2024 (ruscelli2023prognosticimpactof pages 1-2, yang2024molecularsubtypesof pages 4-5, ribeirosantos2024tailoringendometrialcancer pages 2-3) | **Intermediate** prognosis, but clinically heterogeneous; in NSMP, traditional pathologic features such as grade, stage, necrosis, and substantial LVSI remain important prognostic modifiers (ruscelli2023prognosticimpactof pages 1-2, nagel2024predictivebiomarkersin pages 2-4) | Management remains driven by integrated clinicopathologic risk; **brachytherapy/adjuvant tailoring** may be relevant in selected early-stage cases, but there is no single defining targeted systemic therapy yet; this group is a priority for further biomarker refinement (nagel2024predictivebiomarkersin pages 2-4, ruscelli2023prognosticimpactof pages 1-2) |
| p53abn / copy-number high / serous-like | **Abnormal p53 IHC** pattern (overexpression, null, or cytoplasmic pattern) as surrogate for TP53 alteration; assigned after excluding POLEmut in integrated algorithms | Roughly **20–26%** overall across mixed EC cohorts; **20.9%** in Ruscelli 2023; **26%** in Yang 2024; **6.7%** in the small Guo 2024 cohort; p53-abnormality enriched in high-grade/aggressive tumors and estimated at ~**30% of FIGO grade 3 endometrioid EC** in Casanova 2024 meta-analysis (ruscelli2023prognosticimpactof pages 1-2, yang2024molecularsubtypesof pages 4-5, nagel2024predictivebiomarkersin pages 2-4) | **Poor / worst** prognosis among the four groups, with higher recurrence and mortality (nagel2024predictivebiomarkersin pages 2-4, ruscelli2023prognosticimpactof pages 1-2) | Supports **adjuvant intensification**, including added chemotherapy and external-beam radiotherapy in appropriate settings; FIGO 2023 uses **IICm_p53abn** modifier for early-stage disease with p53 abnormality; p53abn disease is also an important subgroup in ongoing/improving immunotherapy datasets (nagel2024predictivebiomarkersin pages 2-4, berek2023figostagingof media 9e3676d6) |


*Table: This table summarizes the four TCGA/ProMisE molecular subtypes used clinically in endometrial carcinoma, with practical diagnostic surrogates, approximate frequencies from the retrieved literature, prognostic direction, and major treatment implications.*

### 4.2 Subtype proportions (examples from clinical cohorts)
In a 2023 clinical cohort classified per WHO algorithm, subtypes were **7.8% POLE**, **31% MMRd**, **21% p53abn**, **40.2% NSMP** (Ruscelli et al., *J Pers Med*, 2023-04-??; https://doi.org/10.3390/jpm13050723) (ruscelli2023prognosticimpactof pages 1-2). A separate 2023 cohort similarly found molecular analysis success in all cases with subgroup fractions including **7.6% POLE**, **32.2% MMRd**, **20.9% p53abn**, **39.3% NSMP** (de Biase et al., *Front Med*, 2023-03-??; https://doi.org/10.3389/fmed.2023.1146499) (ruscelli2023prognosticimpactof pages 1-2).

### 4.3 Key genes and targets (disease-level resources)
Open Targets lists multiple associated targets for “Endometrial Endometrioid Adenocarcinoma” including **PTEN, ARID1A, CTNNB1, MLH1** among others, supported by literature evidence aggregation (OpenTargets Search: endometrioid endometrial adenocarcinoma,endometrial carcinoma).

### 4.4 Epigenetic features (MLH1 promoter hypermethylation)
MMRd/MSI-H EEC includes a clinically important epigenetic subset driven by **MLH1 promoter hypermethylation**, which is distinguished from suspected-LS tumors in routine workflows; a study in 527 ECs categorized “met-EC” (MLH1-PHM) and found it had a higher fraction of stage III/IV disease (37.2%) and worse OS/PFS than suspected-LS in that cohort (Kaneko et al., *J Gynecol Oncol*, 2021; https://doi.org/10.3802/jgo.2021.32.e79) (addante2024mismatchrepairdeficiency pages 3-5).

---

## 5. Mechanism / pathophysiology (causal chains; GO/CL suggestions)

### 5.1 Estrogen–obesity–inflammation axis (upstream drivers)
A recent meta-analysis frames endometrioid EC risk as strongly influenced by obesity-driven endocrine changes: adipocytes serve as a primary estrogen source post-menopause via aromatase, and obesity is linked to insulin resistance and chronic inflammation (clontz2024effectsofweight pages 1-2). Weight loss interventions reduce inflammatory mediators implicated in carcinogenesis (CRP, IL-6) (clontz2024effectsofweight pages 18-19).

**Suggested GO biological process terms** (examples):
- GO:0008284 positive regulation of cell population proliferation
- GO:0071396 cellular response to lipid
- GO:0006954 inflammatory response
- GO:0001525 angiogenesis

### 5.2 DNA repair deficiency and immune microenvironment (MMRd/MSI-H)
MMRd/MSI-H tumors have high mutation burden and are a key predictive biomarker class for immune checkpoint inhibition; IHC for MMR proteins is an “optimal diagnostic MSI surrogate worldwide” according to a 2024 review (Addante et al., *Int J Mol Sci*, 2024-01-??; https://doi.org/10.3390/ijms25021056) (addante2024mismatchrepairdeficiency pages 3-5).

**Suggested GO terms:**
- GO:0006298 mismatch repair
- GO:0006974 cellular response to DNA damage stimulus
- GO:0006955 immune response

### 5.3 PI3K/AKT/mTOR signaling and metabolic coupling
The weight-loss meta-analysis highlights PI3K/Akt/mTOR pathway activation as part of the obesity-related mechanistic link to endometrioid EC risk (clontz2024effectsofweight pages 18-19).

**Suggested GO terms:**
- GO:0014068 positive regulation of phosphatidylinositol 3-kinase signaling
- GO:0032147 activation of protein kinase B activity

### 5.4 Cell types (Cell Ontology suggestions)
- Endometrial glandular epithelial cell (**CL:0002563**, if available)
- Endometrial stromal cell (appropriate CL mapping)
- Tumor-infiltrating lymphocyte / T cell (**CL:0000084**, T cell)
- Macrophage (**CL:0000235**) (obesity-associated inflammatory milieu)

---

## 6. Environmental information

### Lifestyle/environmental factors with strongest retrieved evidence
- Obesity and metabolic dysfunction as modifiable exposures (mahamatsaleh2024associationofmetabolic pages 1-2, wilson2023systematicreviewand pages 1-2).
- Nutritional patterns and other exposures were not comprehensively retrieved in the current evidence corpus.

**Infectious agents:** No infectious etiology is supported in the retrieved evidence.

---

## 7. Anatomical structures affected (UBERON/CL/GO CC suggestions)

### Primary affected site
- Endometrium of uterine corpus (UBERON:0001295 endometrium; UBERON:0000995 uterus—verify exact IDs in ontology curation).

### Tissue/cell level
- Endometrial epithelium (glandular epithelium) (yasuda2024newclinicopathologicalconcept pages 1-3).

### Subcellular localization (typical for key biomarkers)
- Nucleus (p53 IHC; MMR proteins IHC) (GO:0005634 nucleus)

---

## 8. Temporal development

### Onset
EEC is typically diagnosed in older adult women (mean age in one review context: 62 years) (yang2024molecularsubtypesof pages 4-5).

### Progression and staging
FIGO 2023 updated staging incorporates histology/grade/LVSI and, critically, **molecular alterations**. The FIGO staging paper states that “the presence of pathogenic POLE mutations or of p53 abnormalities now modifies the FIGO stage” (Berek et al., *Int J Gynecol Obstet*, 2023-06-??; https://doi.org/10.1002/ijgo.14923) (berek2023figostagingof media 9e3676d6).

A key implementation detail is reflected in the FIGO 2023 staging tables (image evidence): molecular stage modifiers include **IAm_POLEmut** and **IICm_p53abn**, and an “m” subscript plus subtype can be added when molecular class is known (berek2023figostagingof media 9e3676d6, berek2023figostagingof media f7c3e53d, berek2023figostagingof media 4b64842a).

---

## 9. Inheritance and population

### Population incidence and trends (recent, quantitative)
- A large US registry analysis (1995–2018) found endometrial cancer incidence rising for both early-onset (<50) and late-onset disease, with early-onset increasing faster (AAPC 1.8% vs 0.7% overall), and highlighted disparities by race/ethnicity (e.g., early-onset AAPC 3.5% in Non-Hispanic Black women) (Liu et al., *JNCI Cancer Spectrum*, 2023-01-??; https://doi.org/10.1093/jncics/pkad001) (liu2023differentialtrendsin pages 2-4).
- The same analysis reported **930,176 invasive EC cases** total, with **12.6% early-onset**; early-onset had higher proportion of endometrioid histology (87.0% vs 79.0%) (liu2023differentialtrendsin pages 2-4).

### US case/death estimates (2023)
A SEER-focused elderly-women trends paper cites: “**66,200 new U.S. cases and 13,030 deaths in 2023**” for uterine cancer (corpus) (Priyadarshini et al., *Aging Medicine*, 2024-04-??; https://doi.org/10.1002/agm2.12297) (priyadarshini2024trendsingynecological pages 1-2).

### Inheritance pattern (subset)
- **Lynch syndrome (autosomal dominant cancer predisposition)** is a key inherited etiology for a minority of cases; universal screening is widely recommended (, ).

---

## 10. Diagnostics

### Standard diagnostic approach (current practice emphasis)
- **Histopathology from endometrial biopsy/curettage or hysterectomy specimen** with FIGO grading (yasuda2024newclinicopathologicalconcept pages 1-3).
- **Molecular classification surrogates in pathology** (POLE sequencing + p53 and MMR IHC) are increasingly recommended/endorsed in WHO 2020 and FIGO 2023 frameworks to support prognostication and treatment decisions (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3).

### MMR/MSI testing and Lynch syndrome screening
- A 2024 real-world institutional study states international guidelines recommend universal LS screening in endometrial cancer and reports implementation metrics: among 331 patients, **30.8% were MMR-deficient** and **0.9% diagnosed with Lynch syndrome**, with screening adherence improving to 90.6% over time (Joder et al., *Cancers*, 2024-02-??; https://doi.org/10.3390/cancers16030671) ().

### Practical biomarker implication for systemic therapy
A 2024 pathology review notes MMRd has predictive value for immunotherapy; in the palliative setting, MMRd tumors can receive anti–PD-(L)1 monotherapy, whereas MMR-proficient tumors may receive pembrolizumab + lenvatinib (nagel2024predictivebiomarkersin pages 2-4).

### Differential diagnosis (not exhaustive)
- Non-endometrioid endometrial carcinomas (serous, clear cell, carcinosarcoma) which are molecularly and clinically distinct (yasuda2024newclinicopathologicalconcept pages 1-3).

---

## 11. Outcome / prognosis

### Molecular subtype as a prognostic axis
Across cohorts and reviews, prognostic ordering is generally: **POLEmut best**, **MMRd and NSMP intermediate**, **p53abn worst** (ruscelli2023prognosticimpactof pages 1-2, yasuda2024newclinicopathologicalconcept pages 3-4, nagel2024predictivebiomarkersin pages 1-2).

### Stage and histopathologic modifiers remain important
Within NSMP and MMRd groups, standard pathologic factors (stage, LVSI, lymph node status) retain prognostic importance (ruscelli2023prognosticimpactof pages 1-2).

### Example survival statistics from retrieved sources
- Yang (2024) reports an “overall relative 5-year survival of **81.1%**” in the endometrioid endometrial cancer context (review statement) (yang2024molecularsubtypesof pages 4-5).

---

## 12. Treatment (current applications; 2023–2024 pivotal trials)

### 12.1 Standard local management (high-level)
The retrieved evidence corpus is dominated by systemic therapy advances; detailed surgical/radiation algorithms specific to EEC were not directly retrieved. Molecular-risk integration into adjuvant decisions is emphasized in 2024 reviews and in ESGO/ESTRO/ESP risk classification studies (nagel2024predictivebiomarkersin pages 2-4, ruscelli2023prognosticimpactof pages 1-2).

### 12.2 First-line systemic therapy advances (real-world implementing evidence from phase 3)

#### Dostarlimab + carboplatin/paclitaxel (RUBY, phase 3)
Mirza et al. report that in the dMMR–MSI-H subgroup, “estimated progression-free survival at 24 months was **61.4%** … in the dostarlimab group and **15.7%** … in the placebo group (hazard ratio … **0.28**; … P<0.001)” and in the overall population 24-month PFS was 36.1% vs 18.1% (Mirza et al., *NEJM*, 2023-06-08; https://doi.org/10.1056/NEJMoa2216334) (mirza2023dostarlimabforprimary pages 1-3). Safety signals included higher grade ≥3 events and immune-related events in the dostarlimab arm (mirza2023dostarlimabforprimary pages 10-11).

#### Pembrolizumab + carboplatin/paclitaxel (NRG-GY018, phase 3)
Eskander et al. report (dMMR cohort) 12-month Kaplan–Meier PFS of **74%** with pembrolizumab vs **38%** with placebo (HR **0.30**; 95% CI 0.19–0.48; P<0.001) and (pMMR cohort) median PFS **13.1 months** vs **8.7 months** (HR **0.54**; P<0.001) (Eskander et al., *NEJM*, 2023-06-08; https://doi.org/10.1056/NEJMoa2302312) (eskander2023pembrolizumabpluschemotherapy pages 6-7, eskander2023pembrolizumabpluschemotherapy pages 1-3).

### 12.3 MAXO (Medical Action Ontology) suggestions (examples)
- Hysterectomy (MAXO term for hysterectomy)
- Bilateral salpingo-oophorectomy
- External beam radiation therapy
- Vaginal brachytherapy
- Combination chemotherapy (carboplatin + paclitaxel)
- Immune checkpoint inhibitor therapy (anti-PD-1)

---

## 13. Prevention

### Primary prevention (risk reduction)
Evidence supports prevention via reduction of obesity/metabolic dysfunction. Bariatric surgery is associated with reduced endometrial cancer incidence (RR 0.38) (wilson2023systematicreviewand pages 1-2), and weight-loss interventions reduce inflammatory biomarkers linked to risk (clontz2024effectsofweight pages 18-19).

### Secondary prevention (screening / early detection)
- Universal tumor testing for MMR deficiency to identify Lynch syndrome and inform therapeutic options is increasingly implemented, but adherence varies; reflex/standardized pathways are recommended ().

### Tertiary prevention
- Molecularly guided therapy selection (e.g., dMMR-directed immunotherapy) to reduce recurrence/progression risk in advanced settings (mirza2023dostarlimabforprimary pages 1-3, eskander2023pembrolizumabpluschemotherapy pages 6-7).

---

## 14. Other species / natural disease
Not addressed in retrieved evidence.

---

## 15. Model organisms
Not addressed in retrieved evidence.

---

# Recent developments (2023–2024) and expert synthesis

1. **Histomolecular integration is now central**: authoritative pathology reviews describe molecular classification as endorsed by WHO (2020) and integrated into FIGO 2023 staging updates (nagel2024predictivebiomarkersin pages 1-2, yasuda2024newclinicopathologicalconcept pages 1-3, berek2023figostagingof media 9e3676d6).
2. **First-line chemo-immunotherapy has changed practice**: RUBY and NRG-GY018 demonstrate large PFS gains, especially in dMMR/MSI-H disease, supporting routine MMR testing as both a hereditary screen and a predictive biomarker (mirza2023dostarlimabforprimary pages 1-3, eskander2023pembrolizumabpluschemotherapy pages 6-7, addante2024mismatchrepairdeficiency pages 3-5).
3. **Metabolic prevention is a major real-world lever**: high-certainty meta-analytic evidence links combined obesity + metabolic dysfunction to substantially increased endometrial cancer risk, and bariatric surgery shows a large protective association (mahamatsaleh2024associationofmetabolic pages 1-2, wilson2023systematicreviewand pages 1-2).

# Visual evidence (FIGO 2023)
The FIGO 2023 staging tables illustrating molecular modifiers (e.g., **IAm_POLEmut**, **IICm_p53abn**) are provided in the cited table images from the FIGO staging publication (berek2023figostagingof media 9e3676d6, berek2023figostagingof media f7c3e53d, berek2023figostagingof media 4b64842a).


References

1. (nagel2024predictivebiomarkersin pages 1-2): Janaína Nagel, Rafael Bispo Paschoalini, Patrícia Sodré Dias Barreto, Caroline Haydn Credidio, Eduardo Paulino, and Maria Del Pilar Estevez-Diz. Predictive biomarkers in endometrial carcinomas: a review of their relevance in daily anatomic pathology. Surgical and Experimental Pathology, Nov 2024. URL: https://doi.org/10.1186/s42047-024-00164-2, doi:10.1186/s42047-024-00164-2. This article has 9 citations.

2. (yasuda2024newclinicopathologicalconcept pages 1-3): Masanori Yasuda. New clinicopathological concept of endometrial carcinoma with integration of histological features and molecular profiles. Pathology International, 74:557-573, Aug 2024. URL: https://doi.org/10.1111/pin.13471, doi:10.1111/pin.13471. This article has 10 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: endometrioid endometrial adenocarcinoma,endometrial carcinoma): Open Targets Query (endometrioid endometrial adenocarcinoma,endometrial carcinoma, 40 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (nagel2024predictivebiomarkersin pages 2-4): Janaína Nagel, Rafael Bispo Paschoalini, Patrícia Sodré Dias Barreto, Caroline Haydn Credidio, Eduardo Paulino, and Maria Del Pilar Estevez-Diz. Predictive biomarkers in endometrial carcinomas: a review of their relevance in daily anatomic pathology. Surgical and Experimental Pathology, Nov 2024. URL: https://doi.org/10.1186/s42047-024-00164-2, doi:10.1186/s42047-024-00164-2. This article has 9 citations.

5. (ruscelli2023prognosticimpactof pages 1-2): Martina Ruscelli, Thais Maloberti, Angelo Gianluca Corradini, Francesca Rosini, Giulia Querzoli, Marco Grillini, Annalisa Altimari, Elisa Gruppioni, Viviana Sanza, Alessia Costantino, Riccardo Ciudino, Matteo Errani, Alessia Papapietro, Sara Coluccelli, Daniela Turchetti, Martina Ferioli, Susanna Giunchi, Giulia Dondi, Marco Tesei, Gloria Ravegnini, Francesca Abbati, Daniela Rubino, Claudio Zamagni, Emanuela D’Angelo, Pierandrea De Iaco, Donatella Santini, Claudio Ceccarelli, Anna Myriam Perrone, Giovanni Tallini, Dario de Biase, and Antonio De Leo. Prognostic impact of pathologic features in molecular subgroups of endometrial carcinoma. Journal of Personalized Medicine, 13:723, Apr 2023. URL: https://doi.org/10.3390/jpm13050723, doi:10.3390/jpm13050723. This article has 15 citations.

6. (wilson2023systematicreviewand pages 1-2): Robert B. Wilson, Dhruvi Lathigara, and Devesh Kaushal. Systematic review and meta-analysis of the impact of bariatric surgery on future cancer risk. International Journal of Molecular Sciences, 24:6192, Mar 2023. URL: https://doi.org/10.3390/ijms24076192, doi:10.3390/ijms24076192. This article has 154 citations.

7. (liu2023differentialtrendsin pages 2-4): Lihua Liu, Talar S Habeshian, Juanjuan Zhang, Noah C Peeri, Mengmeng Du, Immaculata De Vivo, and Veronica Wendy Setiawan. Differential trends in rising endometrial cancer incidence by age, race, and ethnicity. JNCI Cancer Spectrum, Jan 2023. URL: https://doi.org/10.1093/jncics/pkad001, doi:10.1093/jncics/pkad001. This article has 103 citations and is from a peer-reviewed journal.

8. (yang2024molecularsubtypesof pages 4-5): Ye Yang, Su Fang Wu, and Wei Bao. Molecular subtypes of endometrial cancer: implications for adjuvant treatment strategies. International Journal of Gynecology & Obstetrics, 164:436-459, Jul 2024. URL: https://doi.org/10.1002/ijgo.14969, doi:10.1002/ijgo.14969. This article has 107 citations and is from a peer-reviewed journal.

9. (clontz2024effectsofweight pages 1-2): Angela D. Clontz, Emma Gan, Stephen D. Hursting, and Victoria L. Bae-Jump. Effects of weight loss on key obesity-related biomarkers linked to the risk of endometrial cancer: a systematic review and meta-analysis. Cancers, 16:2197, Jun 2024. URL: https://doi.org/10.3390/cancers16122197, doi:10.3390/cancers16122197. This article has 21 citations.

10. (ribeirosantos2024tailoringendometrialcancer pages 2-3): Pedro Ribeiro-Santos, Carolina Martins Vieira, Gilson Gabriel Viana Veloso, Giovanna Vieira Giannecchini, Martina Parenza Arenhardt, Larissa Müller Gomes, Pedro Zanuncio, Flávio Silva Brandão, and Angélica Nogueira-Rodrigues. Tailoring endometrial cancer treatment based on molecular pathology: current status and possible impacts on systemic and local treatment. International Journal of Molecular Sciences, 25:7742, Jul 2024. URL: https://doi.org/10.3390/ijms25147742, doi:10.3390/ijms25147742. This article has 22 citations.

11. (mahamatsaleh2024associationofmetabolic pages 1-2): Yahya Mahamat-saleh, Dagfinn Aune, Heinz Freisling, Sheetal Hardikar, Rola Jaafar, Sabina Rinaldi, Marc J. Gunter, and Laure Dossus. Association of metabolic obesity phenotypes with risk of overall and site-specific cancers: a systematic review and meta-analysis of cohort studies. British Journal of Cancer, 131:1480-1495, Sep 2024. URL: https://doi.org/10.1038/s41416-024-02857-7, doi:10.1038/s41416-024-02857-7. This article has 49 citations and is from a domain leading peer-reviewed journal.

12. (johnson2023riskofendometrial pages 1-2): Jean-Ellen Johnson, Diandra Daley, Cristi Tarta, and Paul Stanciu. Risk of endometrial cancer in patients with polycystic ovarian syndrome: a meta‑analysis. Oncology Letters, Mar 2023. URL: https://doi.org/10.3892/ol.2023.13754, doi:10.3892/ol.2023.13754. This article has 80 citations and is from a peer-reviewed journal.

13. (clontz2024effectsofweight pages 18-19): Angela D. Clontz, Emma Gan, Stephen D. Hursting, and Victoria L. Bae-Jump. Effects of weight loss on key obesity-related biomarkers linked to the risk of endometrial cancer: a systematic review and meta-analysis. Cancers, 16:2197, Jun 2024. URL: https://doi.org/10.3390/cancers16122197, doi:10.3390/cancers16122197. This article has 21 citations.

14. (yasuda2024newclinicopathologicalconcept pages 3-4): Masanori Yasuda. New clinicopathological concept of endometrial carcinoma with integration of histological features and molecular profiles. Pathology International, 74:557-573, Aug 2024. URL: https://doi.org/10.1111/pin.13471, doi:10.1111/pin.13471. This article has 10 citations and is from a peer-reviewed journal.

15. (berek2023figostagingof media 9e3676d6): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1291 citations and is from a peer-reviewed journal.

16. (addante2024mismatchrepairdeficiency pages 3-5): Francesca Addante, Antonio d’Amati, Angela Santoro, Giuseppe Angelico, Frediano Inzani, Damiano Arciuolo, Antonio Travaglino, Antonio Raffone, Nicoletta D’Alessandris, Giulia Scaglione, Michele Valente, Giordana Tinnirello, Stefania Sfregola, Belen Padial Urtueta, Alessia Piermattei, Federica Cianfrini, Antonino Mulè, Emma Bragantini, and Gian Franco Zannoni. Mismatch repair deficiency as a predictive and prognostic biomarker in endometrial cancer: a review on immunohistochemistry staining patterns and clinical implications. International Journal of Molecular Sciences, 25:1056, Jan 2024. URL: https://doi.org/10.3390/ijms25021056, doi:10.3390/ijms25021056. This article has 45 citations.

17. (mirza2023dostarlimabforprimary pages 10-11): Mansoor R. Mirza, Dana M. Chase, Brian M. Slomovitz, René dePont Christensen, Zoltán Novák, Destin Black, Lucy Gilbert, Sudarshan Sharma, Giorgio Valabrega, Lisa M. Landrum, Lars C. Hanker, Ashley Stuckey, Ingrid Boere, Michael A. Gold, Annika Auranen, Bhavana Pothuri, David Cibula, Carolyn McCourt, Francesco Raspagliesi, Mark S. Shahin, Sarah E. Gill, Bradley J. Monk, Joseph Buscema, Thomas J. Herzog, Larry J. Copeland, Min Tian, Zangdong He, Shadi Stevens, Eleftherios Zografos, Robert L. Coleman, and Matthew A. Powell. Dostarlimab for primary advanced or recurrent endometrial cancer. New England Journal of Medicine, 388:2145-2158, Jun 2023. URL: https://doi.org/10.1056/nejmoa2216334, doi:10.1056/nejmoa2216334. This article has 874 citations and is from a highest quality peer-reviewed journal.

18. (mirza2023dostarlimabforprimary pages 1-3): Mansoor R. Mirza, Dana M. Chase, Brian M. Slomovitz, René dePont Christensen, Zoltán Novák, Destin Black, Lucy Gilbert, Sudarshan Sharma, Giorgio Valabrega, Lisa M. Landrum, Lars C. Hanker, Ashley Stuckey, Ingrid Boere, Michael A. Gold, Annika Auranen, Bhavana Pothuri, David Cibula, Carolyn McCourt, Francesco Raspagliesi, Mark S. Shahin, Sarah E. Gill, Bradley J. Monk, Joseph Buscema, Thomas J. Herzog, Larry J. Copeland, Min Tian, Zangdong He, Shadi Stevens, Eleftherios Zografos, Robert L. Coleman, and Matthew A. Powell. Dostarlimab for primary advanced or recurrent endometrial cancer. New England Journal of Medicine, 388:2145-2158, Jun 2023. URL: https://doi.org/10.1056/nejmoa2216334, doi:10.1056/nejmoa2216334. This article has 874 citations and is from a highest quality peer-reviewed journal.

19. (eskander2023pembrolizumabpluschemotherapy pages 6-7): Ramez N. Eskander, Michael W. Sill, Lindsey Beffa, Richard G. Moore, Joanie M. Hope, Fernanda B. Musa, Robert Mannel, Mark S. Shahin, Guilherme H. Cantuaria, Eugenia Girda, Cara Mathews, Juraj Kavecansky, Charles A. Leath, Lilian T. Gien, Emily M. Hinchcliff, Shashikant B. Lele, Lisa M. Landrum, Floor Backes, Roisin E. O’Cearbhaill, Tareq Al Baghdadi, Emily K. Hill, Premal H. Thaker, Veena S. John, Stephen Welch, Amanda N. Fader, Matthew A. Powell, and Carol Aghajanian. Pembrolizumab plus chemotherapy in advanced endometrial cancer. New England Journal of Medicine, 388:2159-2170, Jun 2023. URL: https://doi.org/10.1056/nejmoa2302312, doi:10.1056/nejmoa2302312. This article has 780 citations and is from a highest quality peer-reviewed journal.

20. (eskander2023pembrolizumabpluschemotherapy pages 1-3): Ramez N. Eskander, Michael W. Sill, Lindsey Beffa, Richard G. Moore, Joanie M. Hope, Fernanda B. Musa, Robert Mannel, Mark S. Shahin, Guilherme H. Cantuaria, Eugenia Girda, Cara Mathews, Juraj Kavecansky, Charles A. Leath, Lilian T. Gien, Emily M. Hinchcliff, Shashikant B. Lele, Lisa M. Landrum, Floor Backes, Roisin E. O’Cearbhaill, Tareq Al Baghdadi, Emily K. Hill, Premal H. Thaker, Veena S. John, Stephen Welch, Amanda N. Fader, Matthew A. Powell, and Carol Aghajanian. Pembrolizumab plus chemotherapy in advanced endometrial cancer. New England Journal of Medicine, 388:2159-2170, Jun 2023. URL: https://doi.org/10.1056/nejmoa2302312, doi:10.1056/nejmoa2302312. This article has 780 citations and is from a highest quality peer-reviewed journal.

21. (berek2023figostagingof media f7c3e53d): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1291 citations and is from a peer-reviewed journal.

22. (berek2023figostagingof media 4b64842a): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1291 citations and is from a peer-reviewed journal.

23. (priyadarshini2024trendsingynecological pages 1-2): Subhadra Priyadarshini, Prafulla Kumar Swain, Khushi Agarwal, Diptismita Jena, and Sourav Padhee. Trends in gynecological cancer incidence, mortality, and survival among elderly women: a seer study. Aging Medicine, 7:179-188, Apr 2024. URL: https://doi.org/10.1002/agm2.12297, doi:10.1002/agm2.12297. This article has 40 citations and is from a peer-reviewed journal.