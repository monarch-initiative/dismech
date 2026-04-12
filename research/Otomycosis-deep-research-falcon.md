---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:46:58.847643'
end_time: '2026-04-04T15:57:11.236429'
duration_seconds: 612.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Otomycosis
  mondo_id: ''
  category: Infectious
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
- **Disease Name:** Otomycosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Otomycosis** covering all of the
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
- **Disease Name:** Otomycosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Otomycosis** covering all of the
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


# Otomycosis (Fungal Otitis Externa): Disease Characteristics Research Report

**Target disease:** Otomycosis (infectious; fungal infection of the external ear canal).

## Executive summary (current understanding)
Otomycosis is a **superficial fungal infection of the external auditory canal (EAC)**, often presenting with pruritus, otorrhea, otalgia, aural fullness/blockage, and sometimes hearing loss and tinnitus, and it may be acute, subacute, or chronic. (bojanovic2023etiologypredisposingfactors pages 1-2, alam2023astudyof pages 1-2, j.f.2025pooledanalysisof pages 1-3)

Across recent multicenter and regional datasets, **Aspergillus spp. (especially the A. niger complex/section Nigri) and Candida spp.** dominate the etiology, but geographic heterogeneity is substantial and mixed bacterial–fungal infection is common. (bojanovic2023etiologypredisposingfactors pages 1-2, roohi2023otomycosistheforemost pages 3-3, sn2024mycologicepidemiologyand pages 1-2)

Clinically, the evidence base continues to emphasize **mechanical aural toilet/debridement plus topical antifungals**, with emerging higher-quality RCT evidence supporting **clotrimazole 1% otic solution** versus placebo. (j.f.2025pooledanalysisof pages 1-3, sangare2021otomycosisinafrica pages 4-5)

## 1. Disease information
### 1.1 What is the disease?
**Definition/overview:**
- “Otomycosis (OM) is a superficial fungal infection of the external auditory canal (EAC)” (review-level definition). (bojanovic2023etiologypredisposingfactors pages 1-2)
- “Otomycosis is a superficial fungal infection of the external auditory canal.” (prospective cohort definition). (alam2023astudyof pages 1-2)
- Otomycosis is “a superficial infection involving the external auditory canal caused by yeasts and filamentous fungi.” (trial definition). (j.f.2025pooledanalysisof pages 1-3)

**Synonyms/alternative names (clinical):** otomycosis; fungal otitis externa; fungal infection of the external auditory canal; “ear fungus” (common usage in recent clinical literature). (bojanovic2023etiologypredisposingfactors pages 1-2, j.f.2025pooledanalysisof pages 1-3)

### 1.2 Key identifiers (ontology/terminology)
- **MONDO ID:** Not identified from the retrieved evidence corpus.
- **ICD-10/ICD-11, MeSH:** Not extractable from the retrieved evidence corpus.

### 1.3 Evidence source type
Most information here is derived from **aggregated disease-level resources** (systematic/literature reviews), complemented by **human clinical cohort studies**, **cross-sectional microbiology studies**, **a multicenter randomized clinical trial program**, and **clinicaltrials.gov registry records**. (bojanovic2023etiologypredisposingfactors pages 1-2, pereira2024topicalantibioticinducedotomycosis pages 1-2, j.f.2025pooledanalysisof pages 1-3, NCT01547221 chunk 1)

## 2. Etiology
### 2.1 Disease causal factors
Otomycosis is an **infectious disease** caused by fungal colonization/overgrowth of the EAC under permissive conditions (humidity, barrier disruption, dysbiosis), with the most common agents being **Aspergillus spp. and Candida spp.** (bojanovic2023etiologypredisposingfactors pages 1-2, pereira2024topicalantibioticinducedotomycosis pages 1-2)

**Key etiologic fungi (recent datasets):**
- **Iran (2023; molecular identification):** Aspergillus spp. dominated (88% of mold isolates), including Aspergillus section Nigri 57.4%, Flavi 18.8%, Fumigati 11.8%; yeasts included *Candida parapsilosis* (13.8%), *C. orthopsilosis* (5.9%), and *C. albicans* (4.9%). (roohi2023otomycosistheforemost pages 3-3)
- **Libya (2024; culture-based):** Aspergillus spp. 82.67% of isolates; *A. niger* 41.16%, *A. flavus* 38.63%. (elarabi2024prevalenceandetiology pages 2-3, elarabi2024prevalenceandetiology pages 3-4)
- **Cameroon (2024; culture-positive cases):** *Candida albicans* 38%, *Aspergillus niger* 26%, Candida spp. 22%, *A. fumigatus* 14%. (sn2024mycologicepidemiologyand pages 1-2)
- **India (2023; prospective):** Among culture-positive cases, *Aspergillus* 91.1%, *Candida* 8.9%. (alam2023astudyof pages 1-2)

### 2.2 Risk factors (prioritize 2023–2024)
**Pooled/quantitative risk factors (systematic review of topical antibiotic-induced otomycosis; published July 2024):**
- Ototopical antibiotics ± steroids: **47%** (95% CI 0.38–0.56). (pereira2024topicalantibioticinducedotomycosis pages 1-2)
- Oils/wax solvents: **38%** (95% CI 0.26–0.51). (pereira2024topicalantibioticinducedotomycosis pages 1-2)
- Trauma from cleaning/instrumentation: **37%** (95% CI 0.21–0.54). (pereira2024topicalantibioticinducedotomycosis pages 1-2)

**Study-level risk factors (Iran, 2023):** cotton swab/manipulation 40.6%; topical antibiotics 42.6%; topical steroids 33.7%; prior bacterial otitis 31.7%; swimming 8.6%. (roohi2023otomycosistheforemost pages 3-3)

**Environmental/host factors (review synthesis):** tropical/subtropical climates, EAC hygiene practices/trauma, diabetes, and immunodeficiency are repeatedly highlighted across the literature. (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 2-3)

### 2.3 Protective factors
Direct protective factors are not quantified in the retrieved clinical studies. Mechanistically, **intact cerumen/skin barrier and preserved ear-canal microenvironment** are discussed as protective in review-level synthesis. (bojanovic2023etiologypredisposingfactors pages 2-3)

### 2.4 Gene–environment interactions
No host gene–environment interaction (GxE) evidence was identified in the retrieved corpus; otomycosis is treated as an acquired infection with risk driven by local environment, behavior, comorbidity, and iatrogenic factors (e.g., topical antibiotics). (pereira2024topicalantibioticinducedotomycosis pages 1-2)

## 3. Phenotypes
### 3.1 Clinical phenotype spectrum
Commonly reported symptoms/signs include:
- Pruritus/itching (often the dominant symptom) (alam2023astudyof pages 1-2)
- Otorrhea/discharge (bojanovic2023etiologypredisposingfactors pages 3-5)
- Otalgia/ear pain (bojanovic2023etiologypredisposingfactors pages 3-5)
- Aural fullness/blocked sensation (bojanovic2023etiologypredisposingfactors pages 3-5)
- Hearing loss/hypoacusis (roohi2023otomycosistheforemost pages 3-3)
- Tinnitus (roohi2023otomycosistheforemost pages 3-3)
- Scaling/desquamation (roohi2023otomycosistheforemost pages 3-3)
- EAC edema/erythema (bojanovic2023etiologypredisposingfactors pages 3-5)

**Frequencies from recent primary studies:**
- India (2023): ear itching **70.9%**. (alam2023astudyof pages 1-2)
- Iran (2023): tinnitus **26.7%**, hearing loss **19.8%**, scaling **11.8%**. (roohi2023otomycosistheforemost pages 3-3)

### 3.2 Age of onset, severity, and course
Otomycosis can be **acute, subacute, or chronic**, typically **unilateral**, with **bilateral disease more frequent in immunocompromised patients**. (bojanovic2023etiologypredisposingfactors pages 1-2)

### 3.3 Quality of life impact
Formal QoL instruments (e.g., SF-36, EQ-5D) were not reported in the retrieved corpus. The symptom complex (itching, pain, discharge, fullness, hearing symptoms) implies functional burden, but direct quantitative QoL data are currently a gap in this evidence set. (alam2023astudyof pages 1-2, roohi2023otomycosistheforemost pages 3-3)

### 3.4 Suggested HPO terms (examples)
- Pruritus: **HP:0000989**
- Otalgia: **HP:0000366**
- Otorrhea: **HP:0001754**
- Hearing impairment: **HP:0000365**
- Tinnitus: **HP:0000360**
- Ear fullness (aural fullness; no single canonical HPO term universally used; can map to related concepts such as abnormal sensation in ear)
- Scaling/desquamation: **HP:0001056** (abnormality of skin exfoliation), context EAC

(These are ontology suggestions; not directly asserted by the cited articles.)

## 4. Genetic / molecular information
### 4.1 Causal genes / pathogenic variants
No human causal genes/variants are implicated in the retrieved otomycosis evidence; the condition is not presented as an inherited monogenic disorder in these sources. (bojanovic2023etiologypredisposingfactors pages 1-2)

### 4.2 Molecular information relevant to otomycosis
**Molecular methods are used primarily to identify fungal pathogens** (e.g., Aspergillus section/species determination), not host genetics. (roohi2023otomycosistheforemost pages 5-6)

Examples:
- Roohi et al. (2023) describe PCR-based identification (PCR-RFLP and species/section-level identification). (roohi2023otomycosistheforemost pages 4-5, roohi2023otomycosistheforemost pages 5-6)

## 5. Environmental information
### 5.1 Environmental and lifestyle contributors
- Humid/warm climates and moisture exposure (e.g., swimming) are repeatedly implicated. (bojanovic2023etiologypredisposingfactors pages 1-2, roohi2023otomycosistheforemost pages 3-3)
- Canal trauma from cleaning/instrumentation (cotton swabs and other objects) is a major behavioral risk factor. (roohi2023otomycosistheforemost pages 3-3, pereira2024topicalantibioticinducedotomycosis pages 1-2)
- Ototopical antibiotic ± steroid exposure is a major iatrogenic risk factor, with pooled estimates in 2024 systematic review. (pereira2024topicalantibioticinducedotomycosis pages 1-2)

### 5.2 Infectious agents (pathogens)
Predominant genera/species in recent datasets include *Aspergillus* (section Nigri/*A. niger* complex; *A. flavus* complex; *A. fumigatus*) and *Candida* (*C. albicans*, *C. parapsilosis*, non-albicans Candida). (roohi2023otomycosistheforemost pages 3-3, sn2024mycologicepidemiologyand pages 1-2)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (trigger → clinical manifestation)
A synthesis supported by 2023–2024 evidence:
1. **Predisposing exposures** (humidity, swimming, EAC trauma, topical antibiotic/steroid use, diabetes/immunodeficiency) alter local defenses. (roohi2023otomycosistheforemost pages 3-3, pereira2024topicalantibioticinducedotomycosis pages 1-2)
2. **Disruption of normal ear-canal environment** (including microbiome/pH and barrier integrity) facilitates fungal overgrowth; the 2024 systematic review emphasizes prolonged topical antibiotics as a driver of disruption that promotes fungal growth. (pereira2024topicalantibioticinducedotomycosis pages 1-2)
3. **Fungal proliferation on EAC epithelium** leads to inflammation, debris, scaling, discharge, and symptoms (itching, fullness, otalgia, hearing symptoms). (bojanovic2023etiologypredisposingfactors pages 3-5)
4. **Persistence/relapse** can be supported by pathogen traits such as **biofilm formation** (see below). (bojanovic2022clinicalpresentationscluster pages 4-6)

### 6.2 Biofilms and relapse (recent evidence)
In a 30-patient single-center experience of laboratory-confirmed Aspergillus otomycosis, **six patients had relapse at 60 days** with the same Aspergillus species re-isolated, and **“all six species isolated in the relapse episode had the ability to produce biofilm.”** (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6)

### 6.3 Suggested ontology terms
**GO biological process (examples):**
- GO:0006954 inflammatory response
- GO:0009405 pathogenesis
- GO:0009615 response to virus (not applicable); instead use general immune response GO:0006955
- GO:0044419 interspecies interaction between organisms (host–pathogen interaction)

**Cell Ontology (CL) (examples):**
- CL:0000084 T cell (in immune response; not directly measured here)
- CL:0000236 B cell (not directly measured)
- CL:0000583 neutrophil (not directly measured)
- CL:0000066 epithelial cell (EAC epithelium as the affected tissue context)

**Note:** These ontology mappings are mechanistic suggestions; the cited sources do not provide direct single-cell or immunophenotyping data.

## 7. Anatomical structures affected
### 7.1 Organ/tissue localization
Primary site is the **external auditory canal (EAC)**; review-level evidence notes possible extension to the tympanic membrane and auricle, and bilateral disease is more common in immunocompromised hosts. (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 3-5)

**Suggested UBERON terms (examples):**
- External auditory canal: UBERON:0001691 (suggested)
- Tympanic membrane: UBERON:0004499 (suggested)

## 8. Temporal development
### 8.1 Onset and progression
Otomycosis can be **acute, subacute, or chronic**. (bojanovic2023etiologypredisposingfactors pages 1-2)

### 8.2 Recurrence/relapse
Recurrence is a prominent clinical feature discussed across reviews, and in Aspergillus otomycosis a measurable relapse signal (6/30 at 60 days) is reported, with biofilm implicated. (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6)

## 9. Inheritance and population
### 9.1 Epidemiology (statistics from recent studies)
Prevalence estimates vary by context and ascertainment:
- 2023 literature review summarizes a worldwide prevalence “ranging from 9% to 30%.” (bojanovic2023etiologypredisposingfactors pages 1-2)
- 2024 systematic review notes otomycosis accounts for **~5–20% of external ear infections worldwide** (in the context of topical antibiotic-induced otomycosis). (pereira2024topicalantibioticinducedotomycosis pages 1-2)
- Cameroon (2024): 50/100 participants had positive fungal cultures (study sample, not population prevalence). (sn2024mycologicepidemiologyand pages 2-3)
- Libya (2024): fungal growth detected in **86.34% (177/205)** of sampled ear swabs (study sample). (elarabi2024prevalenceandetiology pages 2-3)

### 9.2 Demographics and geographic distribution
- Libya (2024 isolates): female 62.82% (174/277 isolates); age 1–20 years 39.35% (109/277). (elarabi2024prevalenceandetiology pages 3-4)
- Cameroon (2024 positives): female 58% (29/50). (sn2024mycologicepidemiologyand pages 2-3)

## 10. Diagnostics
### 10.1 Clinical examination
Otoscopy/otoendoscopy is central; at least one prospective study states that clinical presentation plus otoscopic findings is often sufficient for presumptive diagnosis, but laboratory confirmation improves etiologic specificity and treatment selection. (alam2023astudyof pages 1-2, bojanovic2023etiologypredisposingfactors pages 3-5)

### 10.2 Laboratory diagnostics
Common diagnostic components (review and primary studies):
- **Direct microscopy / KOH wet mount:** rapid screening approach. (alam2023astudyof pages 1-2, bojanovic2023etiologypredisposingfactors pages 3-5)
- **Fungal culture (SDA and related media):** described as the “gold standard” in review synthesis; proper incubation conditions are important for molds. (bojanovic2023etiologypredisposingfactors pages 3-5, bojanovic2022clinicalpresentationscluster pages 4-6)
- **Serial cultures:** up to three may be needed to distinguish colonization/saprophytes from pathogens (review recommendation). (bojanovic2023etiologypredisposingfactors pages 3-5, bojanovic2023etiologypredisposingfactors pages 12-13)
- **Molecular identification (PCR-based):** used in some settings for species/section-level identification, particularly for Aspergillus. (roohi2023otomycosistheforemost pages 5-6)

**Diagnostic performance note:** In Aspergillus otomycosis, microscopy sensitivity was reported as **90.0%** in a single-center series. (bojanovic2022clinicalpresentationscluster pages 4-6)

### 10.3 Differential diagnosis
The retrieved evidence emphasizes that otomycosis can be difficult to distinguish from other etiologies of otitis externa and that mixed bacterial–fungal infections can complicate evaluation, supporting laboratory confirmation where feasible. (bojanovic2023etiologypredisposingfactors pages 3-5)

## 11. Outcome / prognosis
Otomycosis is typically non-lethal and localized, but it can be recurrent and burdensome. Severe complications are uncommon but include invasive disease (e.g., skull base involvement) particularly in immunocompromised hosts, as highlighted in the 2024 systematic review. (pereira2024topicalantibioticinducedotomycosis pages 1-2)

Relapse risk is supported by the 60-day relapse signal in Aspergillus otomycosis and by review-level statements about recurrence and the need for monitoring. (bojanovic2022clinicalpresentationscluster pages 4-6, bojanovic2023etiologypredisposingfactors pages 5-6)

## 12. Treatment
### 12.1 Key concepts (current standard of care)
Core treatment in recent reviews emphasizes:
1. **Aural toilet / debridement** (microsuction/cleaning of debris). (sangare2021otomycosisinafrica pages 4-5, aloebady2024otomycosisreview pages 3-4)
2. **Topical antifungal therapy** (imidazoles such as clotrimazole; polyenes such as nystatin; others depending on agent and setting). (sangare2021otomycosisinafrica pages 5-6, bojanovic2023etiologypredisposingfactors pages 5-6)
3. **Dry ear precautions and hygiene**, and avoidance of ongoing risk factors (e.g., discontinuing topical antibiotics where feasible). (sangare2021otomycosisinafrica pages 3-4, sangare2021otomycosisinafrica pages 4-5)

### 12.2 Evidence for clotrimazole (recent higher-quality RCT evidence)
A pooled analysis of two international multicenter randomized, double-blind, placebo-controlled trials (Feb 2020–Oct 2021) reported:
- Therapeutic cure: **68.2% (107/157) clotrimazole vs 25.4% (18/71) placebo** (MITT; P<.0001). (j.f.2025pooledanalysisof pages 5-7)
- Related adverse events: **2.7% vs 1.5%** (clotrimazole vs placebo). (j.f.2025pooledanalysisof pages 1-3)

**Notable quote from abstract:** “There is no antifungal otic drug for the treatment of otomycosis approved in the United States.” (j.f.2025pooledanalysisof pages 1-3)

### 12.3 Susceptibility/resistance signals
- In a 2023 primary study, the authors note an “increasing trend of antifungal resistance” (including for commonly used agents such as fluconazole and clotrimazole) and emphasize variability by region. (alam2023astudyof pages 1-2)
- A 2023 molecular study performed susceptibility testing and raised concerns about MIC distributions for triazoles relative to ECVs over time. (roohi2023otomycosistheforemost pages 1-2)

### 12.4 Real-world implementations (durations, monitoring, ototoxicity considerations)
- In an Africa-focused review, recommended management includes **“suction clearance of fungal mass,” discontinuation of topical antibiotics, and “treatment with antifungal eardrops for three weeks,”** with instruction that the **“Ear should be kept dry and hygiene for three weeks”** and follow-up mycological testing. (sangare2021otomycosisinafrica pages 4-5)
- Ototoxicity considerations: imidazoles are discussed as usable even with perforation (with technique cautions), clotrimazole is described as “considered free of ototoxic effects,” and the review emphasizes considering ototoxicity when the tympanic membrane is perforated. (sangare2021otomycosisinafrica pages 5-6, sangare2021otomycosisinafrica pages 4-5)

### 12.5 Experimental / clinical trial landscape (registry evidence)
Recent/ongoing trials include:
- **Boric acid vs clotrimazole:** NCT04824261 (Assiut University; 1% clotrimazole vs 4% boric acid; enrollment 100; open-label randomized; status uncertain/not yet recruiting per extract). (NCT04824261 chunk 1)
- **Boric acid in alcohol vs clotrimazole:** NCT01547221 (Khon Kaen Hospital; randomized double-masked; n=120; cure at 1 week; completed). (NCT01547221 chunk 1)
- **Terbinafine:** NCT07152327 (single-arm; topical terbinafine cream on ear pack; n=50; not yet recruiting). (NCT07152327 chunk 1)
- **Investigational topical vs clotrimazole:** NCT01993823 (G238 vs clotrimazole; Phase III; completed; results posted). (NCT01993823 chunk 1)

### 12.6 Suggested MAXO and CHEBI mappings (examples)
**MAXO (actions; suggested):**
- Ear canal debridement / aural toilet (procedure)
- Topical antifungal therapy
- Antifungal susceptibility testing
- Dry ear precautions / patient education

**CHEBI (chemicals; suggested):**
- Clotrimazole
- Miconazole
- Nystatin
- Terbinafine
- Boric acid
- Acetic acid

## 13. Prevention
Prevention is largely risk-factor reduction and is supported by both review synthesis and pooled risk-factor evidence:
- Avoid EAC trauma from cleaning/instrumentation and reduce unnecessary ototopical antibiotic/steroid use (key pooled factors). (pereira2024topicalantibioticinducedotomycosis pages 1-2)
- Keep ears dry, particularly after swimming, and avoid sustained moisture exposure. (roohi2023otomycosistheforemost pages 3-3, sangare2021otomycosisinafrica pages 4-5)
- Address underlying comorbidity (e.g., diabetes, immunodeficiency) and avoid practices that damage the EAC barrier or cerumen. (bojanovic2023etiologypredisposingfactors pages 12-13)

## 14. Other species / natural disease
No veterinary/natural disease cross-species evidence was identified in the retrieved corpus.

## 15. Model organisms
No model organism systems specific to otomycosis pathogenesis were identified in the retrieved corpus.

## Recent developments (2023–2024 emphasis)
Key 2023–2024 developments from the retrieved evidence include:
1. **Quantified iatrogenic risk (2024 systematic review):** pooled estimates implicate ototopical antibiotic exposure, oils/wax solvents, and canal trauma as major drivers. (pereira2024topicalantibioticinducedotomycosis pages 1-2)
2. **More granular pathogen profiling:** region-specific molecular identification and section/species-level distributions (e.g., Aspergillus section Nigri predominance) support targeted management and surveillance. (roohi2023otomycosistheforemost pages 3-3, roohi2023otomycosistheforemost pages 5-6)
3. **Treatment evidence consolidation:** continued recognition of heterogeneity and limited head-to-head evidence between topical antifungals and acidifying agents. (yassin2023comparisonofacidifying pages 2-3)

## Expert opinions / consensus themes (authoritative sources)
- **Lack of standardized guidance:** the 2023 Journal of Fungi review highlights “the lack of official and recommended treatments or diagnostic procedures.” (bojanovic2023etiologypredisposingfactors pages 2-3)
- Emphasis on **etiologic identification and monitoring** (serial cultures, susceptibility where feasible), especially with recurrent disease and in special populations (immunodeficiency/diabetes). (bojanovic2023etiologypredisposingfactors pages 12-13)

## Visual evidence (table)
A multi-country summary table of fungi, symptoms, and predisposing factors is compiled in the 2023 Journal of Fungi review (Table 1). (bojanovic2023etiologypredisposingfactors media ef15a2c0, bojanovic2023etiologypredisposingfactors media 195ea1dc, bojanovic2023etiologypredisposingfactors media a1c2fe71, bojanovic2023etiologypredisposingfactors media 7e0923a9)

## Structured evidence synthesis table
| Study | Setting/population (incl. n) | Key pathogen distribution | Key risk factors (with % if available) | Key symptoms/clinical findings (with % if available) | Diagnostics used | Treatment/outcomes (cure/response/relapse) | URL/DOI |
|---|---|---|---|---|---|---|---|
| Bojanović 2023, *Journal of Fungi* | Literature review of global otomycosis evidence; disease-level synthesis, no single cohort n (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 2-3, bojanovic2023etiologypredisposingfactors pages 3-5) | Predominantly *Aspergillus* and *Candida*; review notes *A. niger* complex and *Candida* spp. as major agents; broader range includes *Penicillium*, *Fusarium*, *Mucorales*, others (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 2-3) | Tropical/subtropical climate; clothing habits; EAC hygiene practices; prolonged antibiotic therapy; diabetes; immunodeficiency; local trauma; occlusive hearing-aid molds (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 2-3) | Common features include itching, otorrhea, ear canal blockage sensation, pain, headache, tinnitus, edema/redness, desquamation, impaired hearing; bilateral disease more common in immunocompromised patients (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 3-5) | History + otoscopy + lab confirmation; KOH/wet mount for screening; culture described as gold standard; serial mycological exams may be needed; molecular identification useful for *Aspergillus* speciation (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 3-5) | States there are no official therapeutic guidelines; topical polyenes/imidazoles/allylamines used; systemic triazoles reserved for severe forms (bojanovic2023etiologypredisposingfactors pages 1-2, bojanovic2023etiologypredisposingfactors pages 2-3) | https://doi.org/10.3390/jof9060662 |
| Alam 2023, *Asian Journal of Medical Sciences* | Prospective study of primary otomycosis; 230 clinically diagnosed patients (alam2023astudyof pages 1-2) | Positive fungal growth in 203/230 (88.3%); *Aspergillus* 185/203 (91.1%), *Candida* 18/203 (8.9%) (alam2023astudyof pages 1-2) | Most frequent observed risk factor: oil instillation in ear 20%; background risk factors listed: humid climate, ear instrumentation, immunocompromised status, frequent topical antibiotic/steroid use (alam2023astudyof pages 1-2) | Ear itching most common symptom 70.9%; presenting complaints included pain, discharge, hearing difficulty, ringing, heaviness (alam2023astudyof pages 1-2) | Clinical presentation + otoscopic findings; KOH wet mount; culture on Sabouraud dextrose agar; Candida germ tube test; disk diffusion susceptibility testing (alam2023astudyof pages 1-2) | All patients received aural cleaning + topical clotrimazole; 167/203 (83.3%) responded to primary treatment, 36/203 (16.7%) non-responders received topical itraconazole; voriconazole showed highest susceptibility (alam2023astudyof pages 1-2) | https://doi.org/10.3126/ajms.v14i8.54270 |
| Roohi 2023, *Mycoses* | Molecular/mycological study in north-western Iran; prevalence analysis compared with prior 2013 data; symptom/risk-factor frequencies reported from study cohort (roohi2023otomycosistheforemost pages 3-3, roohi2023otomycosistheforemost pages 4-5, roohi2023otomycosistheforemost pages 5-6) | *Aspergillus* spp. 89 isolates (88%): section Nigri 58 (57.4%), Flavi 19 (18.8%), Fumigati 12 (11.8%); yeasts 25 isolates incl. *Candida parapsilosis* 14 (13.8%), *C. orthopsilosis* 6 (5.9%), *C. albicans* 5 (4.9%) (roohi2023otomycosistheforemost pages 3-3) | Cotton swab/manipulation 40.6%; topical antibiotics 42.6%; topical steroids 33.7%; prior bacterial otitis 31.7%; swimming 8.6% (roohi2023otomycosistheforemost pages 3-3) | Tinnitus 26.7%; hearing loss 19.8%; scaling 11.8%; previous fungal otitis 27.7%; tympanic membrane perforation 5.9% (roohi2023otomycosistheforemost pages 3-3) | Direct examination, culture, PCR-RFLP / PCR-based molecular identification to species or section level; study notes prevalence rose from 43% (2013) to 50.5% (2021) (roohi2023otomycosistheforemost pages 4-5, roohi2023otomycosistheforemost pages 5-6) | Antifungal susceptibility performed; excerpts note limited in vitro sensitivity to tioconazole and nystatin for some isolates; no direct clinical cure-rate comparison reported in extracted evidence (roohi2023otomycosistheforemost pages 1-2) | https://doi.org/10.1111/myc.13532 |
| Pereira 2024, *Indian Journal of Otolaryngology and Head & Neck Surgery* | Systematic review of topical antibiotic-induced otomycosis; pooled risk-factor analysis across studies (pereira2024topicalantibioticinducedotomycosis pages 1-2) | *Aspergillus* most commonly isolated organism (pereira2024topicalantibioticinducedotomycosis pages 1-2) | Ototopical antibiotics ± steroids 47% (95% CI 0.38-0.56); oils/wax solvents 38% (95% CI 0.26-0.51); trauma from cleaning/instrumentation 37% (95% CI 0.21-0.54) (pereira2024topicalantibioticinducedotomycosis pages 1-2) | Symptoms range from pruritus and aural fullness to rare invasive skull-base/cranial nerve involvement (pereira2024topicalantibioticinducedotomycosis pages 1-2) | Review-level synthesis; emphasizes altered ear-canal flora/pH from prolonged topical antibiotics as mechanistic predisposing factor (pereira2024topicalantibioticinducedotomycosis pages 1-2) | Recommends caution with ototopical drops; suggests considering 2% acetic acid in mild cases; no pooled cure-rate estimate extracted (pereira2024topicalantibioticinducedotomycosis pages 1-2) | https://doi.org/10.1007/s12070-024-04852-z |
| Elarabi 2024, *Journal of Pure & Applied Sciences* | Cross-sectional study in West Libya; 205 clinical samples, 277 fungal isolates recovered (elarabi2024prevalenceandetiology pages 1-2, elarabi2024prevalenceandetiology pages 2-3, elarabi2024prevalenceandetiology pages 3-4) | Fungal growth in 177/205 (86.34%); genus distribution: *Aspergillus* 229/277 (82.67%), *Alternaria* 33/277 (11.91%), *Candida* 9/277 (3.25%), *Penicillium* 6/277 (2.17%); *A. niger* 114/277 (41.16%), *A. flavus* 107/277 (38.63%) (elarabi2024prevalenceandetiology pages 2-3, elarabi2024prevalenceandetiology pages 3-4) | Female sex 62.82%; age 1-20 years 39.35%; reported contributors: diabetes, eczema, immune deficiency, ear cleaning sticks/earphones/oils, water sports, humid/tropical climate (elarabi2024prevalenceandetiology pages 1-2, elarabi2024prevalenceandetiology pages 2-3, elarabi2024prevalenceandetiology pages 3-4) | Hearing loss/weakness, ear blockage, colored secretions, redness/inflammation; itching, ear pain, tinnitus, fullness, swelling also reported (elarabi2024prevalenceandetiology pages 1-2, elarabi2024prevalenceandetiology pages 3-4) | Ear swab culture on Sabouraud dextrose agar and Czapek-Dox agar at 30°C for one week (elarabi2024prevalenceandetiology pages 1-2) | No treatment outcomes reported in extracted evidence (elarabi2024prevalenceandetiology pages 1-2, elarabi2024prevalenceandetiology pages 2-3) | https://doi.org/10.51984/jopas.v23i2.3122 |
| Awungafac 2024, *Fortune Journal of Health Sciences* | Cross-sectional study in Yaoundé, Cameroon; 100 participants, 50 culture-positive cases (sn2024mycologicepidemiologyand pages 1-2, sn2024mycologicepidemiologyand pages 2-3) | Among cases: *Candida albicans* 38%, *Aspergillus niger* 26%, *Candida* spp. 22%, *A. fumigatus* 14% (sn2024mycologicepidemiologyand pages 1-2) | Swimming and excessive ear cleaning identified; text also notes humid climate and antibiotic/steroid abuse as contributing factors (sn2024mycologicepidemiologyand pages 1-2, sn2024mycologicepidemiologyand pages 2-3) | Complications/findings noted include hearing loss, tympanic membrane perforation, invasive temporal bone infection; female cases 58% (29/50) (sn2024mycologicepidemiologyand pages 1-2, sn2024mycologicepidemiologyand pages 2-3) | Culture on Sabouraud-chloramphenicol agar; microscopy; germ tube test for yeast/C. albicans; disk and macrodilution susceptibility testing (sn2024mycologicepidemiologyand pages 1-2, sn2024mycologicepidemiologyand pages 2-3) | Nystatin showed highest sensitivity, 86% of isolates susceptible; no clinical cure-rate reported in extracted evidence (sn2024mycologicepidemiologyand pages 1-2) | https://doi.org/10.26502/fjhs.162 |
| Bojanović 2022, *Journal of Fungi* | Single-center retrospective/pilot study of laboratory-confirmed *Aspergillus* otomycosis; 30 patients with follow-up at 30 and 60 days (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6, bojanovic2022clinicalpresentationscluster pages 2-4) | *A. niger* complex 66.7%, *A. flavus* complex 33.3% (bojanovic2022clinicalpresentationscluster pages 2-4) | Not a risk-factor prevalence study; focused on relapse and biofilm in *Aspergillus* otomycosis (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6) | At 30 days all mycology negative, but 33.3% still had low-to-moderate symptoms; relapse at 60 days in 6/30 (~20%) with same species re-isolated (bojanovic2022clinicalpresentationscluster pages 4-6) | Microscopy sensitivity 90%; wet mount rapid/cost-effective; culture at both routine and mold-favoring temperatures; 16.7% of isolates required 27-28°C for growth (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6) | Relapse in 6/30 by day 60; all relapse isolates produced biofilm, supporting a role in persistence/recurrence (bojanovic2022clinicalpresentationscluster pages 1-2, bojanovic2022clinicalpresentationscluster pages 4-6) | https://doi.org/10.3390/jof8030315 |
| Ansley 2025, *Journal of Otolaryngology - Head & Neck Surgery* | Pooled analysis of 2 international multicenter randomized double-blind placebo-controlled trials (CLEAR-1/CLEAR-2); 393 treated, 228 MITT (157 clotrimazole, 71 placebo) (j.f.2025pooledanalysisof pages 1-3, j.f.2025pooledanalysisof pages 3-4) | Common pathogens *Aspergillus* and *Candida*; efficacy analysis restricted to baseline culture-positive patients (j.f.2025pooledanalysisof pages 1-3, j.f.2025pooledanalysisof pages 3-4) | Trial excluded diabetes/immunosuppression, tympanic perforation, recent antifungals/corticosteroids, bacterial/malignant otitis externa (j.f.2025pooledanalysisof pages 3-4) | Symptoms assessed: pruritus, otalgia, otorrhea, ear fullness, scored 0-3 (j.f.2025pooledanalysisof pages 1-3, j.f.2025pooledanalysisof pages 3-4) | Ear exudate for mycological/microbiological evaluation; primary endpoint = therapeutic cure (mycological + clinical) at day 24-26 (j.f.2025pooledanalysisof pages 1-3, j.f.2025pooledanalysisof pages 3-4) | Clotrimazole 1% otic solution superior to placebo: therapeutic cure 68.2% vs 25.4%; mycological cure 73.9% vs 28.2%; related AEs 2.7% vs 1.5%; treatment safe/well tolerated (j.f.2025pooledanalysisof pages 5-7, j.f.2025pooledanalysisof pages 1-3) | https://doi.org/10.1177/19160216251330629 |
| Yassin 2023, *Current Medical Mycology* | Mini-review comparing acidifying agents and clotrimazole; 11 studies included from 53 records screened (yassin2023comparisonofacidifying pages 2-3, yassin2023comparisonofacidifying pages 1-2) | Review-level summary of otomycosis pathogens rather than new microbiology; evaluates therapy classes incl. clotrimazole, nystatin, miconazole, acidifying agents (yassin2023comparisonofacidifying pages 1-2) | Not a primary epidemiologic study; notes recurrent disease common and sparse direct head-to-head evidence (yassin2023comparisonofacidifying pages 2-3) | Focuses on symptom improvement (pain, itching, swelling, hearing loss) rather than symptom prevalence (yassin2023comparisonofacidifying pages 1-2) | Review synthesis of prior studies; no new diagnostic cohort (yassin2023comparisonofacidifying pages 2-3, yassin2023comparisonofacidifying pages 1-2) | Eight studies favored clotrimazole for symptom relief; evidence heterogeneous, low quality, and adverse events poorly reported; authors conclude evidence is insufficient to definitively choose clotrimazole vs acidifying agents (yassin2023comparisonofacidifying pages 2-3, yassin2023comparisonofacidifying pages 1-2) | https://doi.org/10.18502/cmm.2023.345035.1402 |
| Nazari 2025, *BMC Infectious Diseases* | Systematic review/meta-analysis of molecularly identified otomycosis isolates; 20 studies, 1392 fungal isolates (abstract-level evidence from search results) (bojanovic2023etiologypredisposingfactors pages 1-2) | Prevalence among clinically suspected patients 58.3% (95% CI 41.4-73.5%); *Aspergillus* 75.8% (95% CI 70.3-80.6%), *Candida* 15.3% (95% CI 8.7-25.6%); frequent species *A. niger* 30.9%, *A. tubingensis* 23.7%, *C. parapsilosis* 39.7% of Candida isolates, *C. albicans* 30.8% (bojanovic2023etiologypredisposingfactors pages 1-2) | Not a primary risk-factor study; focused on molecular distribution of causative agents (bojanovic2023etiologypredisposingfactors pages 1-2) | Not reported in extracted evidence (bojanovic2023etiologypredisposingfactors pages 1-2) | Inclusion required molecular identification methods; addresses limits of conventional morphology (bojanovic2023etiologypredisposingfactors pages 1-2) | No treatment outcomes; authors state evidence quality poor across included studies (bojanovic2023etiologypredisposingfactors pages 1-2) | https://doi.org/10.1186/s12879-025-10954-y |
| NCT04824261, Assiut University | Randomized open-label parallel trial planned; 100 patients, 50/arm; status listed as UNKNOWN / not yet recruiting in registry extract (NCT04824261 chunk 1) | Trial rationale cites common pathogens *Candida* and *Aspergillus* (NCT04824261 chunk 1) | High recurrence noted as rationale; no baseline risk-factor estimates (NCT04824261 chunk 1) | Symptomatic otomycosis with microscopic and/or culture confirmation required (NCT04824261 chunk 1) | Microscopy and/or culture confirmation; follow-up at 1 week, 2 weeks, 1 month (NCT04824261 chunk 1) | Compares 1% clotrimazole solution vs 4% boric acid in distilled water; primary outcome curative rate at 1 month (results not yet available in extract) (NCT04824261 chunk 1) | https://clinicaltrials.gov/study/NCT04824261 |
| NCT01547221, Khon Kaen Hospital | Randomized double-masked parallel completed trial; n=120 (NCT01547221 chunk 1) | Not a pathogen-distribution study; eligibility required KOH-positive otomycosis (NCT01547221 chunk 1) | No baseline risk-factor estimates in registry extract (NCT01547221 chunk 1) | Symptomatic otomycosis; age >7 years (NCT01547221 chunk 1) | Otolaryngologist microscopic findings at 1 week; KOH smear positive at baseline (NCT01547221 chunk 1) | Compared single application 1% clotrimazole ear drop vs 3% boric acid in 70% alcohol; primary outcome cure rate at 1 week; adverse effects recorded 5 minutes after application (results not included in extract) (NCT01547221 chunk 1) | https://clinicaltrials.gov/study/NCT01547221 |
| NCT07152327, Assiut University | Single-arm open-label interventional study; planned n=50 adults; not yet recruiting (NCT07152327 chunk 1) | Study rationale cites in vitro activity of terbinafine against *Aspergillus* and *Candida* (NCT07152327 chunk 1) | Excludes mixed infections, immunocompromise, perforation, recent antifungals, pregnancy/breastfeeding (NCT07152327 chunk 1) | Clinical otoscopic exam plus baseline and post-treatment ear swabs planned (NCT07152327 chunk 1) | Baseline/post-treatment KOH and culture; otoscopy (NCT07152327 chunk 1) | Tests terbinafine 1% cream on ear pack changed every 2 days for 14 days; primary outcome combined clinical + mycological cure at 14 days (results pending) (NCT07152327 chunk 1) | https://clinicaltrials.gov/study/NCT07152327 |


*Table: This table compiles key 2023-2025 otomycosis evidence, including major pathogens, risk factors, clinical features, diagnostics, and treatment outcomes from reviews, cohort studies, randomized trials, and registry entries. It is useful for quickly comparing real-world epidemiology and management evidence across studies.*

## Source notes and limitations
- **Ontology identifiers (MONDO/ICD/MeSH):** not extractable from the available retrieved evidence; should be added via direct ontology database lookup.
- Many epidemiology estimates are **clinic-ascertained** and not directly generalizable to population incidence/prevalence.
- Comparative effectiveness across topical agents remains limited by **heterogeneity and sparse high-quality head-to-head trials**, as emphasized by treatment reviews. (yassin2023comparisonofacidifying pages 2-3)


References

1. (bojanovic2023etiologypredisposingfactors pages 1-2): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

2. (alam2023astudyof pages 1-2): Imran Alam, Rajeev Krishna Gupta, Anuja Bhargava, S M Faiz, Saurabh Srivastava, Fareya Haider, Abhijeet Singh, and Himanshu Sharma. A study of clinico-mycological profile and treatment of primary otomycosis. Asian Journal of Medical Sciences, 14:133-138, Aug 2023. URL: https://doi.org/10.3126/ajms.v14i8.54270, doi:10.3126/ajms.v14i8.54270. This article has 2 citations.

3. (j.f.2025pooledanalysisof pages 1-3): Ansley J.F., Bernal-Sprekelsen M., Butehorn H.F., Todorov S., Tzvetkov V., Douglis F., Georgiev K., and Moreira da Silva F. Pooled analysis of 2 randomized clinical trials to evaluate the efficacy and safety of clotrimazole 1% otic solution for the treatment of otomycosis in adults. Journal of Otolaryngology - Head & Neck Surgery, Apr 2025. URL: https://doi.org/10.1177/19160216251330629, doi:10.1177/19160216251330629. This article has 2 citations.

4. (roohi2023otomycosistheforemost pages 3-3): Behrad Roohi, Shadman Nemati, Abbas Alipour, Leila Faeli, Sabah Mayahi, Iman Haghani, Makan Shalchizadeh, Ali Darini, Abdullah M. S. Al‐Hatmi, Mahdi Abastabar, and Tahereh Shokohi. Otomycosis: the foremost aetiological agent causing otitis externa and the antifungal susceptibility pattern in north‐western iran. Mycoses, 66:87-97, Sep 2023. URL: https://doi.org/10.1111/myc.13532, doi:10.1111/myc.13532. This article has 26 citations and is from a peer-reviewed journal.

5. (sn2024mycologicepidemiologyand pages 1-2): Awungafac Sn, Ngando Ml, Akem Et, Tolefac Pn, and Ndjolo A. Mycologic epidemiology and antifungal susceptibility patterns of otomycosis in yaounde, cameroon: a cross sectional study revealing candida albicans dorminance and nystatin sensitivity. Fortune Journal of Health Sciences, Jan 2024. URL: https://doi.org/10.26502/fjhs.162, doi:10.26502/fjhs.162. This article has 1 citations.

6. (sangare2021otomycosisinafrica pages 4-5): Ibrahim Sangaré, Fructueux Modeste Amona, Richard Wend-Lasida Ouedraogo, Adama Zida, and Macaire Sampawende Ouedraogo. Otomycosis in africa: epidemiology, diagnosis and treatment. Journal of Medical Mycology, 31:101115, Jun 2021. URL: https://doi.org/10.1016/j.mycmed.2021.101115, doi:10.1016/j.mycmed.2021.101115. This article has 34 citations and is from a peer-reviewed journal.

7. (pereira2024topicalantibioticinducedotomycosis pages 1-2): Maria Pereira, Karthik Rao, Florida Sharin, Faiz Tanweer, Manish Mair, and Peter Rea. Topical antibiotic-induced otomycosis - a systematic review of aetiology and risk factors. Indian journal of otolaryngology and head and neck surgery : official publication of the Association of Otolaryngologists of India, 76 5:3766-3776, Jul 2024. URL: https://doi.org/10.1007/s12070-024-04852-z, doi:10.1007/s12070-024-04852-z. This article has 4 citations.

8. (NCT01547221 chunk 1): Ms. Sarisa Romsaithong. Effectiveness of 3% Boric Acid in 70% Alcohol Versus 1% Clotrimazole Solution in Otomycosis Patients. Khon Kaen Hospital. 2012. ClinicalTrials.gov Identifier: NCT01547221

9. (elarabi2024prevalenceandetiology pages 2-3): Ali Elarabi, Adel Jama, Monira AL-Gorag, Laila Gewili, and Maha Farid. Prevalence and etiology of otomycosis in west libya. Journal of Pure &amp; Applied Sciences, 23:144-148, Nov 2024. URL: https://doi.org/10.51984/jopas.v23i2.3122, doi:10.51984/jopas.v23i2.3122. This article has 2 citations.

10. (elarabi2024prevalenceandetiology pages 3-4): Ali Elarabi, Adel Jama, Monira AL-Gorag, Laila Gewili, and Maha Farid. Prevalence and etiology of otomycosis in west libya. Journal of Pure &amp; Applied Sciences, 23:144-148, Nov 2024. URL: https://doi.org/10.51984/jopas.v23i2.3122, doi:10.51984/jopas.v23i2.3122. This article has 2 citations.

11. (bojanovic2023etiologypredisposingfactors pages 2-3): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

12. (bojanovic2023etiologypredisposingfactors pages 3-5): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

13. (roohi2023otomycosistheforemost pages 5-6): Behrad Roohi, Shadman Nemati, Abbas Alipour, Leila Faeli, Sabah Mayahi, Iman Haghani, Makan Shalchizadeh, Ali Darini, Abdullah M. S. Al‐Hatmi, Mahdi Abastabar, and Tahereh Shokohi. Otomycosis: the foremost aetiological agent causing otitis externa and the antifungal susceptibility pattern in north‐western iran. Mycoses, 66:87-97, Sep 2023. URL: https://doi.org/10.1111/myc.13532, doi:10.1111/myc.13532. This article has 26 citations and is from a peer-reviewed journal.

14. (roohi2023otomycosistheforemost pages 4-5): Behrad Roohi, Shadman Nemati, Abbas Alipour, Leila Faeli, Sabah Mayahi, Iman Haghani, Makan Shalchizadeh, Ali Darini, Abdullah M. S. Al‐Hatmi, Mahdi Abastabar, and Tahereh Shokohi. Otomycosis: the foremost aetiological agent causing otitis externa and the antifungal susceptibility pattern in north‐western iran. Mycoses, 66:87-97, Sep 2023. URL: https://doi.org/10.1111/myc.13532, doi:10.1111/myc.13532. This article has 26 citations and is from a peer-reviewed journal.

15. (bojanovic2022clinicalpresentationscluster pages 4-6): Mila Bojanović, Aleksandra Ignjatović, Marko Stalević, Valentina Arsić-Arsenijević, Marina Ranđelović, Vladimir Gerginić, Zorica Stojanović-Radić, Ognjen Stojković, Emilija Živković-Marinkov, and Suzana Otašević. Clinical presentations, cluster analysis and laboratory-based investigation of aspergillus otomycosis—a single center experience. Journal of Fungi, 8:315, Mar 2022. URL: https://doi.org/10.3390/jof8030315, doi:10.3390/jof8030315. This article has 21 citations.

16. (bojanovic2022clinicalpresentationscluster pages 1-2): Mila Bojanović, Aleksandra Ignjatović, Marko Stalević, Valentina Arsić-Arsenijević, Marina Ranđelović, Vladimir Gerginić, Zorica Stojanović-Radić, Ognjen Stojković, Emilija Živković-Marinkov, and Suzana Otašević. Clinical presentations, cluster analysis and laboratory-based investigation of aspergillus otomycosis—a single center experience. Journal of Fungi, 8:315, Mar 2022. URL: https://doi.org/10.3390/jof8030315, doi:10.3390/jof8030315. This article has 21 citations.

17. (sn2024mycologicepidemiologyand pages 2-3): Awungafac Sn, Ngando Ml, Akem Et, Tolefac Pn, and Ndjolo A. Mycologic epidemiology and antifungal susceptibility patterns of otomycosis in yaounde, cameroon: a cross sectional study revealing candida albicans dorminance and nystatin sensitivity. Fortune Journal of Health Sciences, Jan 2024. URL: https://doi.org/10.26502/fjhs.162, doi:10.26502/fjhs.162. This article has 1 citations.

18. (bojanovic2023etiologypredisposingfactors pages 12-13): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

19. (bojanovic2023etiologypredisposingfactors pages 5-6): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

20. (aloebady2024otomycosisreview pages 3-4): Mouna Akeel Hamed Al-Oebady, Hawraa F. Wali, and Nuha Mohammed Mousa. Otomycosis, review. Scholars Academic Journal of Biosciences, 12:236-242, Sep 2024. URL: https://doi.org/10.36347/sajb.2024.v12i08.001, doi:10.36347/sajb.2024.v12i08.001. This article has 2 citations.

21. (sangare2021otomycosisinafrica pages 5-6): Ibrahim Sangaré, Fructueux Modeste Amona, Richard Wend-Lasida Ouedraogo, Adama Zida, and Macaire Sampawende Ouedraogo. Otomycosis in africa: epidemiology, diagnosis and treatment. Journal of Medical Mycology, 31:101115, Jun 2021. URL: https://doi.org/10.1016/j.mycmed.2021.101115, doi:10.1016/j.mycmed.2021.101115. This article has 34 citations and is from a peer-reviewed journal.

22. (sangare2021otomycosisinafrica pages 3-4): Ibrahim Sangaré, Fructueux Modeste Amona, Richard Wend-Lasida Ouedraogo, Adama Zida, and Macaire Sampawende Ouedraogo. Otomycosis in africa: epidemiology, diagnosis and treatment. Journal of Medical Mycology, 31:101115, Jun 2021. URL: https://doi.org/10.1016/j.mycmed.2021.101115, doi:10.1016/j.mycmed.2021.101115. This article has 34 citations and is from a peer-reviewed journal.

23. (j.f.2025pooledanalysisof pages 5-7): Ansley J.F., Bernal-Sprekelsen M., Butehorn H.F., Todorov S., Tzvetkov V., Douglis F., Georgiev K., and Moreira da Silva F. Pooled analysis of 2 randomized clinical trials to evaluate the efficacy and safety of clotrimazole 1% otic solution for the treatment of otomycosis in adults. Journal of Otolaryngology - Head & Neck Surgery, Apr 2025. URL: https://doi.org/10.1177/19160216251330629, doi:10.1177/19160216251330629. This article has 2 citations.

24. (roohi2023otomycosistheforemost pages 1-2): Behrad Roohi, Shadman Nemati, Abbas Alipour, Leila Faeli, Sabah Mayahi, Iman Haghani, Makan Shalchizadeh, Ali Darini, Abdullah M. S. Al‐Hatmi, Mahdi Abastabar, and Tahereh Shokohi. Otomycosis: the foremost aetiological agent causing otitis externa and the antifungal susceptibility pattern in north‐western iran. Mycoses, 66:87-97, Sep 2023. URL: https://doi.org/10.1111/myc.13532, doi:10.1111/myc.13532. This article has 26 citations and is from a peer-reviewed journal.

25. (NCT04824261 chunk 1): Maria Hosny Kamal Gendi. Effectiveness of 4% Boric Acid in Distilled Water Versus Clotrimazole Solution in Otomycosis Patients.. Assiut University. 2021. ClinicalTrials.gov Identifier: NCT04824261

26. (NCT07152327 chunk 1): Doaa Mohamed Samy Mohamed Abd Ellatief. Terbinafine Hydrochloride for the Treatment of Otomycosis. Assiut University. 2025. ClinicalTrials.gov Identifier: NCT07152327

27. (NCT01993823 chunk 1):  Clinical Study to Assess the Efficacy and Safety of G238 Compared to Clotrimazole Otic Solution in the Treatment of Otomycosis. Salvat. 2013. ClinicalTrials.gov Identifier: NCT01993823

28. (yassin2023comparisonofacidifying pages 2-3): Zeynab Yassin, Behrooz Amirzargar, R. Ghasemi, Farnaz Valizadeh, and M. Fattahi. Comparison of acidifying agents and clotrimazole for treatment of otomycosis: a comprehensive one-way mini-review. Current Medical Mycology, 9:45-51, Jun 2023. URL: https://doi.org/10.18502/cmm.2023.345035.1402, doi:10.18502/cmm.2023.345035.1402. This article has 6 citations.

29. (bojanovic2023etiologypredisposingfactors media ef15a2c0): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

30. (bojanovic2023etiologypredisposingfactors media 195ea1dc): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

31. (bojanovic2023etiologypredisposingfactors media a1c2fe71): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

32. (bojanovic2023etiologypredisposingfactors media 7e0923a9): Mila Bojanović, Marko Stalević, Valentina Arsić-Arsenijević, Aleksandra Ignjatović, Marina Ranđelović, Milan Golubović, Emilija Živković-Marinkov, Goran Koraćević, Bojana Stamenković, and Suzana Otašević. Etiology, predisposing factors, clinical features and diagnostic procedure of otomycosis: a literature review. Journal of Fungi, 9:662, Jun 2023. URL: https://doi.org/10.3390/jof9060662, doi:10.3390/jof9060662. This article has 42 citations.

33. (elarabi2024prevalenceandetiology pages 1-2): Ali Elarabi, Adel Jama, Monira AL-Gorag, Laila Gewili, and Maha Farid. Prevalence and etiology of otomycosis in west libya. Journal of Pure &amp; Applied Sciences, 23:144-148, Nov 2024. URL: https://doi.org/10.51984/jopas.v23i2.3122, doi:10.51984/jopas.v23i2.3122. This article has 2 citations.

34. (bojanovic2022clinicalpresentationscluster pages 2-4): Mila Bojanović, Aleksandra Ignjatović, Marko Stalević, Valentina Arsić-Arsenijević, Marina Ranđelović, Vladimir Gerginić, Zorica Stojanović-Radić, Ognjen Stojković, Emilija Živković-Marinkov, and Suzana Otašević. Clinical presentations, cluster analysis and laboratory-based investigation of aspergillus otomycosis—a single center experience. Journal of Fungi, 8:315, Mar 2022. URL: https://doi.org/10.3390/jof8030315, doi:10.3390/jof8030315. This article has 21 citations.

35. (j.f.2025pooledanalysisof pages 3-4): Ansley J.F., Bernal-Sprekelsen M., Butehorn H.F., Todorov S., Tzvetkov V., Douglis F., Georgiev K., and Moreira da Silva F. Pooled analysis of 2 randomized clinical trials to evaluate the efficacy and safety of clotrimazole 1% otic solution for the treatment of otomycosis in adults. Journal of Otolaryngology - Head & Neck Surgery, Apr 2025. URL: https://doi.org/10.1177/19160216251330629, doi:10.1177/19160216251330629. This article has 2 citations.

36. (yassin2023comparisonofacidifying pages 1-2): Zeynab Yassin, Behrooz Amirzargar, R. Ghasemi, Farnaz Valizadeh, and M. Fattahi. Comparison of acidifying agents and clotrimazole for treatment of otomycosis: a comprehensive one-way mini-review. Current Medical Mycology, 9:45-51, Jun 2023. URL: https://doi.org/10.18502/cmm.2023.345035.1402, doi:10.18502/cmm.2023.345035.1402. This article has 6 citations.
