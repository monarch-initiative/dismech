---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T16:36:49.881276'
end_time: '2026-04-25T16:47:50.370870'
duration_seconds: 660.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Angelman Syndrome
  mondo_id: MONDO:0007113
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Angelman Syndrome
- **MONDO ID:** MONDO:0007113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Angelman Syndrome** covering all of the
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
- **Disease Name:** Angelman Syndrome
- **MONDO ID:** MONDO:0007113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Angelman Syndrome** covering all of the
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


# Angelman Syndrome (MONDO:0007113) — Disease Characteristics Research Report

## Executive summary
Angelman syndrome (AS) is a rare, severe neurodevelopmental disorder caused by loss of functional **maternal** UBE3A expression in neurons, while the paternal allele is normally silenced by a neuronally expressed antisense transcript (UBE3A-ATS). The disorder is characterized by profound developmental delay/intellectual disability, minimal-to-absent speech, ataxia/gait disturbance, seizures, sleep disturbance, and a distinctive behavioral phenotype (frequent laughter/happy demeanor). Recent (2023–2024) research has accelerated disease-modifying strategies that *restore UBE3A function*, especially by **unsilencing paternal UBE3A** using antisense oligonucleotides (ASOs), RNA-targeting CRISPR/Cas13, and small-molecule “unsilencers.” Key translational biomarkers include **quantitative EEG delta-band power**, coherence, and sleep spindle metrics.

---

## 1. Disease information

### 1.1 Definition and overview
Angelman syndrome is a rare neurodevelopmental disorder due to maternal UBE3A deficiency in neurons; because paternal UBE3A is epigenetically silenced in neurons by UBE3A-ATS, loss of the maternal allele produces near-absence of UBE3A protein in the brain and the clinical phenotype. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)

*Abstract-supported quote (overview of core mechanism):* “Angelman syndrome … is caused by maternal UBE3A deficiency. A promising therapeutic approach … is to reactivate the intact paternal UBE3A by suppressing UBE3A-ATS.” (lee2023antisenseoligonucleotidetherapy pages 1-4)

### 1.2 Key identifiers
- **MONDO:** MONDO:0007113 (Angelman syndrome; Open Targets disease entry) (roberts2024epigeneticsinrare pages 12-14)
- **OMIM:** 105830 (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)
- **Other identifiers (Orphanet, ICD-10/ICD-11, MeSH):** Not retrieved in the current evidence set; should be filled from OMIM/Orphanet/MeSH directly in a follow-up extraction step.

### 1.3 Synonyms / alternative names
Commonly used synonyms in the literature include **“Angelman syndrome,” “AS,”** and descriptions historically referring to the characteristic behavior (e.g., “happy disposition”). (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
The report’s disease characterization draws from:
- **Aggregated resources/reviews** (mechanism, genotype proportions, diagnostic algorithms, therapy landscape) (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2, ma2023praderwilliandangelman pages 2-5)
- **Human cohort/natural history datasets** (genotype-stratified epilepsy and EEG phenotypes) (cassater2021clinicalcharacterizationof pages 1-3, frohlich2019electrophysiologicalphenotypein pages 1-3)
- **Preclinical model systems** (mouse, rat, nonhuman primate, stem-cell/iPSC models) supporting mechanism and intervention timing (born2021earlydevelopmentaleeg pages 1-2, ramirez2024regionalandcellular pages 1-2, santos2023stemcellmodels pages 10-11)

---

## 2. Etiology

### 2.1 Primary causal factors
AS is a **Mendelian imprinting disorder** due to **loss of maternal UBE3A function in neurons**, with paternal UBE3A silenced by **UBE3A-ATS**. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2, lee2023antisenseoligonucleotidetherapy pages 1-4)

Mechanistic detail relevant to etiology: UBE3A-ATS represses paternal UBE3A “in cis through a transcriptional collision mechanism,” explaining why reactivating the paternal allele is a rational therapy. (lee2023antisenseoligonucleotidetherapy pages 1-4)

### 2.2 Genetic risk factors (causal variants / molecular subtypes)
Major molecular etiologies and approximate frequencies reported across reviews/cohorts include:
- **Maternal 15q11–q13 deletion:** ~70% (yang2021genotype–phenotypecorrelationsin pages 1-2) (some reviews report higher/variable values) (markati2021therapiesinpreclinical pages 1-3)
- **Paternal uniparental disomy (UPD) 15:** ~2–7% (yang2021genotype–phenotypecorrelationsin pages 1-2)
- **Imprinting defects (IC defects):** ~3–5% (yang2021genotype–phenotypecorrelationsin pages 1-2)
- **Pathogenic UBE3A variants (coding mutations):** ~10% (yang2021genotype–phenotypecorrelationsin pages 1-2) 

A 2024 epigenetics-focused review also summarizes subtype ranges and highlights a “large (5–7 Mb) maternal deletion,” with UPD (3–7%), imprinting defects (2–4%), and UBE3A coding mutations (~10%). (roberts2024epigeneticsinrare pages 12-14)

### 2.3 Environmental risk factors and protective factors
AS is primarily genetic; no environmental risk factors or protective factors were identified in the retrieved evidence corpus.

### 2.4 Gene–environment interactions
No specific gene–environment interaction evidence was identified in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Core phenotype domains (with suggested HPO terms)
Below are key phenotypes, typical timing, and representative **HPO term suggestions**.

1) **Global developmental delay / severe intellectual disability**
- Typical onset: infancy/early childhood; often apparent in the first year of life. (yang2021genotype–phenotypecorrelationsin pages 1-2, alias2023angelmansyndromea pages 1-2)
- Suggested HPO: **HP:0001263** (Global developmental delay), **HP:0001249** (Intellectual disability)

2) **Severe expressive speech impairment / absent speech**
- Minimal-to-absent expressive language is a hallmark. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)
- Suggested HPO: **HP:0001344** (Absent speech), **HP:0002465** (Poor speech)

3) **Movement disorder: ataxia / gait disturbance / tremor**
- Characteristic unsteady gait and balance problems; jerky movements. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)
- Suggested HPO: **HP:0001251** (Ataxia), **HP:0002066** (Gait ataxia), **HP:0001337** (Tremor)

4) **Epilepsy and seizure types**
- Many individuals develop seizures early; one review states seizures begin in “>80% before age three.” (roberts2024epigeneticsinrare pages 12-14)
- Natural history cohort data show strong genotype effects: in 265 children, epilepsy was more common in deletion vs non-deletion genotypes (171/187 [91%] vs 48/78 [61%]) and with earlier median onset (24 vs 57 months). (cassater2021clinicalcharacterizationof pages 1-3)
- Suggested HPO: **HP:0001250** (Seizures), **HP:0002184** (Focal seizures) / **HP:0002197** (Generalized seizures) as appropriate

5) **Sleep disturbance**
- Sleep problems are prominent; preclinical and clinical EEG work supports sleep-architecture disruptions. (lee2023antisenseoligonucleotidetherapy pages 1-4, bakker2018abnormalcoherenceand pages 1-2)
- Suggested HPO: **HP:0002360** (Sleep disturbance)

6) **Behavioral phenotype (happy demeanor / frequent laughter)**
- Distinctive behavioral profile includes frequent inappropriate laughter/happy disposition. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)
- Suggested HPO: **HP:0000749** (Inappropriate laughter)

### 3.2 EEG phenotypes and quantitative biomarkers (key statistics)
EEG abnormalities are a defining clinical biomarker domain in AS.

- **Elevated broadband power peaking in delta range**: In a genotype-stratified study (deletion n=37, non-deletion n=21, controls n=48), both genotypes showed “excess broadband power from 1–32 Hz peaking in the delta range (peak 2.8 Hz).” (frohlich2019electrophysiologicalphenotypein pages 1-3)
- **Genotype-specific spectral differences**: deletion AS showed elevated theta (peak 5.3 Hz) and diminished beta (peak 23 Hz) relative to non-deletion AS, implicating hemizygosity of the **GABRB3–GABRA5–GABRG3** cluster within typical deletions. (frohlich2019electrophysiologicalphenotypein pages 1-3)
- **Sleep EEG architecture and connectivity**: In a retrospective EEG study (28 AS vs 72 neurotypical controls; ages 4–11), AS showed increased long-range coherence (wake across frequencies; sleep gamma coherence) and **fewer/shorter sleep spindles**. (bakker2018abnormalcoherenceand pages 1-2)
- **Longitudinal EEG delta modeling for trials**: A natural history modeling study used **204 EEG recordings from 56 subjects** (ages 1.3–21) to predict delta (2–4 Hz) trajectories and showed, in mice, ASO treatment effects detectable through at least 8 weeks (P < 1e-15) with correlation to Ube3a expression (P < 0.001). (spencer2022longitudinaleegmodel pages 1-3)

### 3.3 Quality of life (QoL) impact
QoL limitations arise from severe developmental disability, communication impairment, seizures/sleep disruption, and motor dysfunction, driving a need for multidisciplinary supports and accessible outcome measures. (ma2023praderwilliandangelman pages 2-5, bakker2018abnormalcoherenceand pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **UBE3A** (ubiquitin protein ligase E3A): primary causal gene underlying AS when maternal neuronal expression is lost. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)

### 4.2 Pathogenic variant classes and structural mechanisms
Major causal mechanisms include:
- **Maternal 15q11–q13 deletions** (often ~5–7 Mb): remove maternal UBE3A and can remove additional genes contributing to phenotype severity (notably GABA-A receptor subunit genes). (roberts2024epigeneticsinrare pages 12-14, cassater2021clinicalcharacterizationof pages 1-3)
- **Paternal UPD 15** and **imprinting center defects**: disrupt parent-of-origin expression (methylation) leading to lack of maternal UBE3A expression in neurons. (roberts2024epigeneticsinrare pages 12-14, ma2023praderwilliandangelman pages 2-5)
- **Intragenic UBE3A variants**: missense, nonsense, splice, small indels; sequencing is required when methylation is normal. (ma2023praderwilliandangelman pages 2-5, yang2021genotype–phenotypecorrelationsin pages 2-4)

### 4.3 Functional consequence
The unifying functional consequence is **loss-of-function of maternal UBE3A activity** in neurons due to imprinting, with paternal allele silenced by UBE3A-ATS. (lee2023antisenseoligonucleotidetherapy pages 1-4, roberts2024epigeneticsinrare pages 12-14)

### 4.4 Epigenetic information (imprinting)
Imprinting is central: in neurons the paternal UBE3A allele is silenced by UBE3A-ATS; restoring expression is a main disease-modifying strategy. (lee2023antisenseoligonucleotidetherapy pages 1-4, roberts2024epigeneticsinrare pages 12-14)

**Mechanism schematic evidence (figure):** A schematic of UBE3A imprinting and UBE3A-ATS-mediated silencing in mature neurons is shown in Vihma et al. 2024. (vihma2024ube3aunsilencerfor media f576f803)

### 4.5 Modifier genes / locus context
Deletion genotypes can include hemizygosity of **GABRB3, GABRA5, and GABRG3**, proposed contributors to more severe epilepsy/EEG features relative to non-deletion genotypes. (cassater2021clinicalcharacterizationof pages 1-3, frohlich2019electrophysiologicalphenotypein pages 1-3)

---

## 5. Environmental information
AS is primarily genetic; environmental/lifestyle and infectious triggers were not identified as causal contributors in this evidence set.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (from genotype to phenotype)
1) **Initial trigger:** maternal UBE3A deletion/mutation, paternal UPD, or imprinting defect reduces/abolishes maternal UBE3A expression in neurons. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)
2) **Upstream epigenetic constraint:** paternal UBE3A is silenced in neurons by UBE3A-ATS; thus neurons have insufficient UBE3A protein. (lee2023antisenseoligonucleotidetherapy pages 1-4, roberts2024epigeneticsinrare pages 12-14)
3) **Downstream circuit dysfunction:** abnormal neuronal synchrony and network activity manifests as characteristic EEG signatures (elevated delta power, altered coherence, reduced spindles), contributing to epilepsy, sleep disruption, and cognitive impairment. (frohlich2019electrophysiologicalphenotypein pages 1-3, bakker2018abnormalcoherenceand pages 1-2, spencer2022longitudinaleegmodel pages 1-3)
4) **Clinical manifestations:** severe developmental delay/ID, minimal speech, ataxia, seizures, sleep disturbance, and behavioral features. (roberts2024epigeneticsinrare pages 12-14, yang2021genotype–phenotypecorrelationsin pages 1-2)

### 6.2 Molecular pathways and cellular processes (selected, model-supported)
A 2023 stem-cell model review summarizes downstream abnormalities identified largely in animal models, including dysregulated mTOR signaling, synaptic plasticity deficits, mitochondrial dysfunction, and oxidative stress/ROS, as well as epilepsy linked to GABAergic circuitry dysfunction. (santos2023stemcellmodels pages 8-9)

**Suggested GO biological process terms (representative):**
- Synaptic plasticity: **GO:0048167**
- Regulation of synaptic transmission: **GO:0050804**
- Ubiquitin-dependent protein catabolic process: **GO:0006511**
- mTOR signaling: **GO:0031929** (regulation of mTOR signaling)

**Suggested CL cell types (representative):**
- Neuron: **CL:0000540**
- GABAergic interneuron: **CL:0000617** (as relevant to GABAergic circuitry discussions)
- Glial cells (for imprinting contrast): astrocyte **CL:0000127**, oligodendrocyte **CL:0000128**

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary involvement is the **central nervous system**, reflected in neurodevelopmental disability, epilepsy, sleep dysregulation, and motor dysfunction. (roberts2024epigeneticsinrare pages 12-14, frohlich2019electrophysiologicalphenotypein pages 1-3)

**Suggested UBERON terms:**
- Brain: **UBERON:0000955**
- Cerebral cortex: **UBERON:0000956**
- Hippocampus: **UBERON:0001954**

### 7.2 Tissue and cellular level
Evidence indicates paternal UBE3A silencing occurs in **neurons but not glial cells**, at least in rhesus macaque developmental mapping, supporting neuron-targeted interventions. (ramirez2024regionalandcellular pages 1-2)

### 7.3 Subcellular
UBE3A is an E3 ubiquitin ligase; dysfunction impacts ubiquitin-mediated processes and downstream nuclear/cytoplasmic neuronal function (broadly summarized in the therapeutics literature). (markati2021therapiesinpreclinical pages 1-3)

**Suggested GO cellular component terms (representative):**
- Nucleus: **GO:0005634**
- Synapse: **GO:0045202**

---

## 8. Temporal development

### 8.1 Onset
Clinical features typically emerge in infancy/early childhood; seizures often begin early (one review: >80% before age 3). (roberts2024epigeneticsinrare pages 12-14)

Cohort data show genotype-dependent timing: median seizure onset 24 months (deletion) vs 57 months (non-deletion). (cassater2021clinicalcharacterizationof pages 1-3)

### 8.2 Progression/course
AS is typically lifelong; symptom domains evolve with development. EEG delta power varies with age, motivating longitudinal models for clinical trials. (spencer2022longitudinaleegmodel pages 1-3)

### 8.3 Critical windows for intervention
While early-life treatment is widely viewed as optimal, preclinical data suggest at least some phenotypes (EEG rhythms and sleep disturbance) may be improved even with juvenile/adult ASO intervention.

*Abstract-supported quote:* “reducing Ube3a-ATS by antisense oligonucleotides in juvenile or adult … mice rescues the abnormal electroencephalogram rhythms and sleep disturbance” (lee2023antisenseoligonucleotidetherapy pages 1-4).

Nonhuman primate mapping indicates paternal UBE3A silencing onset between gestational day 48 and 100 in macaque neurons, supporting early (potentially prenatal) intervention concepts. (ramirez2024regionalandcellular pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Reported frequency is consistently rare but variable across sources:
- Prevalence estimates in reviews span roughly **1 in 10,000–24,000 births**. (yang2021genotype–phenotypecorrelationsin pages 1-2)
- Other sources commonly cite **~1 in 12,000–20,000**. (roberts2024epigeneticsinrare pages 12-14, alias2023angelmansyndromea pages 1-2)

### 9.2 Inheritance pattern
Although AS is genetic, most common mechanisms (large maternal deletions, UPD) are typically **de novo**; recurrence risk depends strongly on molecular subtype (e.g., imprinting center defects and inherited UBE3A variants can elevate recurrence risk). Molecular subtyping is therefore essential in genetic counseling. (ma2023praderwilliandangelman pages 2-5, roberts2024epigeneticsinrare pages 12-14)

### 9.3 Sex ratio, geography, variant geography
Not available in the retrieved evidence corpus.

---

## 10. Diagnostics

### 10.1 Molecular diagnostic workflow (real-world implementation)
A consistent algorithm across reviews emphasizes **methylation/copy-number first**:
- **First-line:** methylation analysis of 15q11–q13 (e.g., SNRPN locus) and/or **MS-MLPA**, which can assess methylation + copy number and detect microdeletions and mosaicism. (ma2023praderwilliandangelman pages 2-5)
- **If methylation abnormal + deletion present:** AS due to **15q11–q13 deletion**. (yang2021genotype–phenotypecorrelationsin pages 2-4)
- **If methylation abnormal without deletion:** use **microsatellite linkage analysis** to distinguish **UPD** from **imprinting defect**. (yang2021genotype–phenotypecorrelationsin pages 2-4)
- **If methylation normal:** proceed to **UBE3A sequencing** for intragenic pathogenic variants; if negative, consider alternative diagnoses. (yang2021genotype–phenotypecorrelationsin pages 2-4)

### 10.2 EEG as supportive diagnostic/biomarker tool
Characteristic EEG patterns include high-amplitude rhythmic delta activity and genotype-associated spectral differences; quantitative EEG (qEEG) provides objective measures for both diagnosis support and therapeutic monitoring. (frohlich2019electrophysiologicalphenotypein pages 1-3, martinez2023quantitativeeeganalysis pages 1-2)

### 10.3 Differential diagnosis
Chromosomal microarray can identify other microdeletion syndromes that can mimic AS when methylation and UBE3A testing are negative. (yang2021genotype–phenotypecorrelationsin pages 2-4)

---

## 11. Outcomes / prognosis

### 11.1 Mortality and survival
The retrieved evidence notes seizure complications as a potential cause of death but does not provide robust life expectancy or mortality-rate estimates. (roberts2024epigeneticsinrare pages 12-14)

### 11.2 Morbidity
Major morbidity drivers include severe intellectual disability, communication impairment, epilepsy, motor impairment, and sleep problems. (roberts2024epigeneticsinrare pages 12-14, cassater2021clinicalcharacterizationof pages 1-3)

---

## 12. Treatment

### 12.1 Current clinical management (standard of care)
Current care is primarily **supportive and symptomatic**, including seizure management and multidisciplinary developmental/rehabilitative services. (ma2023praderwilliandangelman pages 2-5)

### 12.2 Disease-modifying and advanced therapeutics (2023–2024 emphasis)

#### A) ASO-mediated paternal UBE3A unsilencing (targeting UBE3A-ATS)
**Mechanism:** suppress UBE3A-ATS to unsilence paternal UBE3A. (lee2023antisenseoligonucleotidetherapy pages 1-4, markati2021therapiesinpreclinical pages 5-6)

- **Clinical safety/early efficacy signal (GTX-102 / apazunersen):** A gene-therapy overview paper summarizes an open-label intrathecal Phase 1/2 experience where five participants received cumulative 20–105.3 mg; “acute inflammatory polyradiculopathy causing leg weakness” occurred in two patients (clinical hold; recovery after discontinuation), while mean CGI-AS improvement was +2.4 at 4.5 months with improvements in behavioral/motor measures. (davidson2022genebasedtherapeuticsfor pages 4-5)

#### B) Small-molecule unsilencing of paternal UBE3A (2024)
A 2024 Nature Communications study identified (S)-PHA533533 as a small-molecule unsilencer.

*Abstract-supported quotes:*
- “(S)-PHA533533 … significantly increase[s] paternal Ube3a mRNA and UBE3A protein levels while downregulating Ube3a-ATS” (vihma2024ube3aunsilencerfor pages 1-2)
- “peripheral delivery of (S)-PHA533533 in AS model mice induces widespread neuronal UBE3A expression” (vihma2024ube3aunsilencerfor pages 1-2)

**Visual evidence:** immunofluorescent images and schematics of UBE3A imprinting/unsilencing are shown in the extracted figures. (vihma2024ube3aunsilencerfor media e5b0fdd9, vihma2024ube3aunsilencerfor media f576f803)

#### C) RNA-targeting CRISPR/Cas (Cas13) unsilencing (2023)
A 2023 Molecular Therapy paper reports that an AAV-delivered high-fidelity Cas13 system targeting Ube3a-ATS can restore paternal Ube3a in cortex/hippocampus for up to four months and improve motor function in AS mice. (li2023ahighfidelityrnatargeting pages 1-3)

#### D) Outcome measures / biomarkers for trials and real-world use
Quantitative EEG delta power is a leading noninvasive biomarker and can be modeled longitudinally to detect target engagement and treatment effects. (spencer2022longitudinaleegmodel pages 1-3)

### 12.3 Clinical trials (real-world implementation; key records)
Below are high-salience interventional programs with ClinicalTrials.gov records retrieved in this run (URLs embedded in NCT identifiers):

1) **ION582 (Olezarsen-class ASO; Ionis) — HALOS**
- **NCT05127226 (Phase 1–2a; Recruiting; planned n≈70)**; intrathecal bolus; primary outcome safety/tolerability; includes PK endpoints (Cmax, Tmax, t1/2, CSF concentration). (NCT05127226 chunk 1)
- URL: https://clinicaltrials.gov/study/NCT05127226 (ClinicalTrials.gov; first posted year in record: 2021) (NCT05127226 chunk 1)

2) **ION582 — REVEAL (Phase 3)**
- NCT number was retrieved by search but not fully extracted in text chunks in this evidence set; should be pulled directly from ClinicalTrials.gov (listed as Phase 3 recruiting in the tool output but not included as an evidence chunk here).

3) **GTX-102 / apazunersen (Ultragenyx)**
- **NCT04259281 (Phase 1/2; Completed; actual enrollment 74)**; multiple-dose escalation; intrathecal injection; primary outcomes are AE/SAE counts and severity up to Day 337; includes PK (Cmax). (NCT04259281 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT04259281 (record year: 2020) (NCT04259281 chunk 1)
- **NCT06617429 (Phase 3; Active not recruiting; actual enrollment 129)**; randomized, double-blind, sham-controlled; primary endpoint Bayley-4 cognitive raw score change at Day 338. (NCT06617429 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT06617429 (record year: 2024) (NCT06617429 chunk 1)
- **NCT06415344 (Phase 3 LTE; Enrolling by invitation; enrollment 255)**; open-label intrathecal flexible dosing; primary outcome AE/SAE frequency over 5 years. (NCT06415344 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT06415344 (record year: 2024) (NCT06415344 chunk 1)
- **NCT07157254 (Phase 2; Recruiting; enrollment 60)**; open-label basket study by genotype/age; includes Bayley-4 cognitive and a multidomain responder index (MDRI) endpoints. (NCT07157254 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT07157254 (record year: 2025) (NCT07157254 chunk 1)

**Note:** None of the retrieved ClinicalTrials.gov chunks included posted results modules; thus, efficacy should be treated as investigational pending peer-reviewed trial publications. (NCT05127226 chunk 1, NCT04259281 chunk 1, NCT06617429 chunk 1)

### 12.4 Suggested MAXO terms (examples)
- Intrathecal drug administration: **MAXO:0000934** (conceptual; verify exact MAXO ID in ontology browser)
- Antisense oligonucleotide therapy: **MAXO:000XXXX** (needs MAXO lookup; not present in retrieved evidence)
- Physical therapy / occupational therapy / speech therapy: MAXO terms not retrieved here; should be mapped from clinical guidelines.

---

## 13. Prevention
Primary prevention of de novo genetic events is not generally feasible; prevention focuses on:
- **Genetic counseling** and molecular subtype determination to inform recurrence risk. (ma2023praderwilliandangelman pages 2-5)
- **Prenatal or preimplantation genetic testing** may be applicable for families with known pathogenic UBE3A variants or imprinting center defects, but detailed guideline sources were not in the retrieved corpus.

---

## 14. Other species / natural disease
No naturally occurring veterinary AS analogs were identified in the retrieved evidence.

---

## 15. Model organisms

### 15.1 Mouse models
- Maternal Ube3a knockout mice are widely used; specialized lines enable temporal reinstatement and drug screening using paternal-allele reporter systems. (santos2023stemcellmodels pages 2-4)

### 15.2 Rat models
- A CRISPR-engineered rat with complete maternal Ube3a deletion shows age-dependent EEG delta power increases, epileptiform activity, and seizure phenotypes, supporting translational biomarker development. (born2021earlydevelopmentaleeg pages 1-2)

### 15.3 Nonhuman primate (rhesus macaque)
- Developmental mapping shows neuron-specific paternal UBE3A silencing onset between gestational days 48–100, supporting early-intervention hypotheses. (ramirez2024regionalandcellular pages 1-2)

### 15.4 Human stem cell models (iPSC/ESC and organoids)
- PSC-derived neurons and organoids recapitulate imprinting dynamics: UBE3A decreases while UBE3A-ATS increases during neuronal differentiation; models show electrophysiological immaturity and altered calcium transients/synaptic plasticity, supporting mechanism studies and drug screening. (santos2023stemcellmodels pages 10-11, santos2023stemcellmodels pages 9-10)

---

## Data gaps and recommended next-step sources (for knowledge base completion)
Several requested fields (ICD-10/ICD-11 codes, MeSH ID, Orphanet ID, penetrance/life expectancy distributions, and MAXO IDs for specific interventions) were not present in the retrieved full-text evidence. For knowledge base completion, extract these from: OMIM (105830), Orphanet disease pages, MeSH browser, and ICD coding systems, and map ontologies via MONDO cross-references.

---

## Key visual evidence (recent mechanism and unsilencing)
- UBE3A imprinting schematic and paternal allele silencing by UBE3A-ATS in mature neurons (Vihma et al., 2024 figure crop). (vihma2024ube3aunsilencerfor media f576f803)
- Immunofluorescent evidence of increased paternal UBE3A signal after (S)-PHA533533 treatment (Vihma et al., 2024 figure crop). (vihma2024ube3aunsilencerfor media e5b0fdd9)



References

1. (roberts2024epigeneticsinrare pages 12-14): Chris-Tiann Roberts, Khatereh Saei Arezoumand, Ashraf Kadar Shahib, James R. Davie, and Mojgan Rastegar. Epigenetics in rare neurological diseases. Frontiers in Cell and Developmental Biology, Jul 2024. URL: https://doi.org/10.3389/fcell.2024.1413248, doi:10.3389/fcell.2024.1413248. This article has 7 citations.

2. (yang2021genotype–phenotypecorrelationsin pages 1-2): Lili Yang, Xiaoli Shu, Shujiong Mao, Yi Wang, Xiaonan Du, and Chaochun Zou. Genotype–phenotype correlations in angelman syndrome. Genes, 12:987, Jun 2021. URL: https://doi.org/10.3390/genes12070987, doi:10.3390/genes12070987. This article has 66 citations.

3. (lee2023antisenseoligonucleotidetherapy pages 1-4): Dongwon Lee, Wu Chen, Heet Naresh Kaku, Xinming Zhuo, Eugene S. Chao, Armand Soriano, Allen Kuncheria, Stephanie Flores, Joo Hyun Kim, Frank Rigo, Paymaan Jafar-nejad, Arthur L. Beaudet, Matthew S. Caudill, and Mingshan Xue. Antisense oligonucleotide therapy rescues disturbed brain rhythms and sleep in juvenile and adult mouse models of angelman syndrome. eLife, Jun 2023. URL: https://doi.org/10.1101/2022.06.18.496687, doi:10.1101/2022.06.18.496687. This article has 30 citations and is from a domain leading peer-reviewed journal.

4. (ma2023praderwilliandangelman pages 2-5): V. K. Ma, R. Mao, Jessica N Toth, Makenzie L. Fulmer, Alena Egense, and Suma P Shankar. Prader-willi and angelman syndromes: mechanisms and management. The Application of Clinical Genetics, 16:41-52, Apr 2023. URL: https://doi.org/10.2147/tacg.s372708, doi:10.2147/tacg.s372708. This article has 39 citations.

5. (cassater2021clinicalcharacterizationof pages 1-3): Daiana Cassater, Mariana Bustamante, Lisa Sach-Peltason, Alexander Rotenberg, Mark Nespeca, Wen-Hann Tan, Lynne M. Bird, and Joerg F. Hipp. Clinical characterization of epilepsy in children with angelman syndrome. Pediatric Neurology, 124:42-50, Nov 2021. URL: https://doi.org/10.1016/j.pediatrneurol.2021.08.007, doi:10.1016/j.pediatrneurol.2021.08.007. This article has 26 citations and is from a peer-reviewed journal.

6. (frohlich2019electrophysiologicalphenotypein pages 1-3): Joel Frohlich, Meghan T. Miller, Lynne M. Bird, Pilar Garces, Hannah Purtell, Marius C. Hoener, Benjamin D. Philpot, Michael S. Sidorov, Wen-Hann Tan, Maria-Clemencia Hernandez, Alexander Rotenberg, Shafali S. Jeste, Michelle Krishnan, Omar Khwaja, and Joerg F. Hipp. Electrophysiological phenotype in angelman syndrome differs between genotypes. Biological Psychiatry, 85:752-759, May 2019. URL: https://doi.org/10.1016/j.biopsych.2019.01.008, doi:10.1016/j.biopsych.2019.01.008. This article has 106 citations and is from a highest quality peer-reviewed journal.

7. (born2021earlydevelopmentaleeg pages 1-2): Heather A. Born, Luis A. Martinez, Amber T. Levine, Sarah E. Harris, Shubhangi Mehra, Wai Ling Lee, Scott V. Dindot, Kevin R. Nash, Jill L. Silverman, David J. Segal, Edwin J. Weeber, and Anne E. Anderson. Early developmental eeg and seizure phenotypes in a full gene deletion of ubiquitin protein ligase e3a rat model of angelman syndrome. eNeuro, 8:ENEURO.0345-20.2020, Feb 2021. URL: https://doi.org/10.1523/eneuro.0345-20.2020, doi:10.1523/eneuro.0345-20.2020. This article has 24 citations and is from a peer-reviewed journal.

8. (ramirez2024regionalandcellular pages 1-2): Chavely Gonzalez Ramirez, Sarah G. Salvador, Ridthi Kartik Rekha Patel, Sarah Clark, Noah W. Miller, Lucas M. James, Nicholas W. Ringelberg, Jeremy M. Simon, Jeffrey Bennett, David G. Amaral, Alain C. Burette, and Benjamin D. Philpot. Regional and cellular organization of the autism-associated protein ube3a/e6ap and its antisense transcript in the brain of the developing rhesus monkey. Frontiers in Neuroanatomy, May 2024. URL: https://doi.org/10.3389/fnana.2024.1410791, doi:10.3389/fnana.2024.1410791. This article has 12 citations.

9. (santos2023stemcellmodels pages 10-11): João Camões dos Santos, Carolina Appleton, Francisca Cazaux Mateus, Rita Covas, Evguenia Pavlovna Bekman, and Simão Teixeira da Rocha. Stem cell models of angelman syndrome. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1274040, doi:10.3389/fcell.2023.1274040. This article has 10 citations.

10. (markati2021therapiesinpreclinical pages 1-3): Theodora Markati, Jessica Duis, and Laurent Servais. Therapies in preclinical and clinical development for angelman syndrome. Expert Opinion on Investigational Drugs, 30:709-720, Jun 2021. URL: https://doi.org/10.1080/13543784.2021.1939674, doi:10.1080/13543784.2021.1939674. This article has 51 citations and is from a peer-reviewed journal.

11. (alias2023angelmansyndromea pages 1-2): Bassy Kuruppan Alias and Lini K. Simon. Angelman syndrome: a genetic challenge for physical and learning disabilities. American Journal of Biopharmacy and Pharmaceutical Sciences, 3:9, Dec 2023. URL: https://doi.org/10.25259/ajbps\_6\_2023, doi:10.25259/ajbps\_6\_2023. This article has 0 citations.

12. (bakker2018abnormalcoherenceand pages 1-2): Hanna den Bakker, Michael S. Sidorov, Zheng Fan, David J. Lee, Lynne M. Bird, Catherine J. Chu, and Benjamin D. Philpot. Abnormal coherence and sleep composition in children with angelman syndrome: a retrospective eeg study. Molecular Autism, Apr 2018. URL: https://doi.org/10.1186/s13229-018-0214-8, doi:10.1186/s13229-018-0214-8. This article has 71 citations and is from a peer-reviewed journal.

13. (spencer2022longitudinaleegmodel pages 1-3): Elizabeth R. Spencer, Wen Shi, Robert W. Komorowski, James P. Gilbert, Lauren M. Ostrowski, Lynne M. Bird, Ronald Thibert, Channa Bao, Fiona Molloy, Michael Calhoun, Samir Koirala, Paymaan Jafar-nejad, Frank Rigo, Mark A. Kramer, and Catherine J. Chu. Longitudinal eeg model detects antisense oligonucleotide treatment effect and increased ube3a in angelman syndrome. Brain Communications, Apr 2022. URL: https://doi.org/10.1093/braincomms/fcac106, doi:10.1093/braincomms/fcac106. This article has 19 citations and is from a peer-reviewed journal.

14. (yang2021genotype–phenotypecorrelationsin pages 2-4): Lili Yang, Xiaoli Shu, Shujiong Mao, Yi Wang, Xiaonan Du, and Chaochun Zou. Genotype–phenotype correlations in angelman syndrome. Genes, 12:987, Jun 2021. URL: https://doi.org/10.3390/genes12070987, doi:10.3390/genes12070987. This article has 66 citations.

15. (vihma2024ube3aunsilencerfor media f576f803): Hanna Vihma, Kelin Li, Anna Welton-Arndt, Audrey L. Smith, Kiran R. Bettadapur, Rachel B. Gilmore, Eric Gao, Justin L. Cotney, Hsueh-Cheng Huang, Jon L. Collins, Stormy J. Chamberlain, Hyeong-Min Lee, Jeffrey Aubé, and Benjamin D. Philpot. Ube3a unsilencer for the potential treatment of angelman syndrome. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49788-8, doi:10.1038/s41467-024-49788-8. This article has 24 citations and is from a highest quality peer-reviewed journal.

16. (santos2023stemcellmodels pages 8-9): João Camões dos Santos, Carolina Appleton, Francisca Cazaux Mateus, Rita Covas, Evguenia Pavlovna Bekman, and Simão Teixeira da Rocha. Stem cell models of angelman syndrome. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1274040, doi:10.3389/fcell.2023.1274040. This article has 10 citations.

17. (martinez2023quantitativeeeganalysis pages 1-2): Luis A. Martinez, Heather A. Born, Sarah Harris, Angelique Regnier-Golanov, Joseph C. Grieco, Edwin J. Weeber, and Anne E. Anderson. Quantitative eeg analysis in angelman syndrome: candidate method for assessing therapeutics. Clinical EEG and Neuroscience, 54:203-212, Nov 2023. URL: https://doi.org/10.1177/1550059420973095, doi:10.1177/1550059420973095. This article has 27 citations and is from a peer-reviewed journal.

18. (markati2021therapiesinpreclinical pages 5-6): Theodora Markati, Jessica Duis, and Laurent Servais. Therapies in preclinical and clinical development for angelman syndrome. Expert Opinion on Investigational Drugs, 30:709-720, Jun 2021. URL: https://doi.org/10.1080/13543784.2021.1939674, doi:10.1080/13543784.2021.1939674. This article has 51 citations and is from a peer-reviewed journal.

19. (davidson2022genebasedtherapeuticsfor pages 4-5): Beverly L. Davidson, Guangping Gao, Elizabeth Berry-Kravis, Allison M. Bradbury, Carsten Bönnemann, Joseph D. Buxbaum, Gavin R. Corcoran, Steven J. Gray, Heather Gray-Edwards, Robin J. Kleiman, Adam J. Shaywitz, Dan Wang, Huda Y. Zoghbi, Terence R. Flotte, Sitra Tauscher-Wisniewski, Cynthia J. Tifft, and Mustafa Sahin. Gene-based therapeutics for rare genetic neurodevelopmental psychiatric disorders. Molecular Therapy, 30:2416-2428, Jul 2022. URL: https://doi.org/10.1016/j.ymthe.2022.05.014, doi:10.1016/j.ymthe.2022.05.014. This article has 24 citations and is from a highest quality peer-reviewed journal.

20. (vihma2024ube3aunsilencerfor pages 1-2): Hanna Vihma, Kelin Li, Anna Welton-Arndt, Audrey L. Smith, Kiran R. Bettadapur, Rachel B. Gilmore, Eric Gao, Justin L. Cotney, Hsueh-Cheng Huang, Jon L. Collins, Stormy J. Chamberlain, Hyeong-Min Lee, Jeffrey Aubé, and Benjamin D. Philpot. Ube3a unsilencer for the potential treatment of angelman syndrome. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49788-8, doi:10.1038/s41467-024-49788-8. This article has 24 citations and is from a highest quality peer-reviewed journal.

21. (vihma2024ube3aunsilencerfor media e5b0fdd9): Hanna Vihma, Kelin Li, Anna Welton-Arndt, Audrey L. Smith, Kiran R. Bettadapur, Rachel B. Gilmore, Eric Gao, Justin L. Cotney, Hsueh-Cheng Huang, Jon L. Collins, Stormy J. Chamberlain, Hyeong-Min Lee, Jeffrey Aubé, and Benjamin D. Philpot. Ube3a unsilencer for the potential treatment of angelman syndrome. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49788-8, doi:10.1038/s41467-024-49788-8. This article has 24 citations and is from a highest quality peer-reviewed journal.

22. (li2023ahighfidelityrnatargeting pages 1-3): Jinhui Li, Zhixin Shen, Yajing Liu, Zixiang Yan, Yuanhua Liu, Xiang Lin, Junjie Tang, Ruimin Lv, Guannan Geng, Zhi-Qi Xiong, Changyang Zhou, and Hui Yang. A high-fidelity rna-targeting cas13 restores paternal ube3a expression and improves motor functions in angelman syndrome mice. Molecular Therapy, 31:2286-2295, Jul 2023. URL: https://doi.org/10.1016/j.ymthe.2023.02.015, doi:10.1016/j.ymthe.2023.02.015. This article has 36 citations and is from a highest quality peer-reviewed journal.

23. (NCT05127226 chunk 1):  HALOS: A Safety, Tolerability, Pharmacokinetics and Pharmacodynamics Study of Multiple Ascending Doses of ION582 in Participants With Angelman Syndrome. Ionis Pharmaceuticals, Inc.. 2021. ClinicalTrials.gov Identifier: NCT05127226

24. (NCT04259281 chunk 1):  A Study of the Safety and Tolerability of GTX-102 in Children With Angelman Syndrome. Ultragenyx Pharmaceutical Inc. 2020. ClinicalTrials.gov Identifier: NCT04259281

25. (NCT06617429 chunk 1):  Phase 3 Efficacy and Safety Study of GTX-102 in Pediatric Subjects With Angelman Syndrome (AS). Ultragenyx Pharmaceutical Inc. 2024. ClinicalTrials.gov Identifier: NCT06617429

26. (NCT06415344 chunk 1):  Long-term Extension of GTX-102 in Angelman Syndrome. Ultragenyx Pharmaceutical Inc. 2024. ClinicalTrials.gov Identifier: NCT06415344

27. (NCT07157254 chunk 1):  A Safety and Efficacy Study of GTX-102 in Subjects With Deletion- or Nondeletion-type Angelman Syndrome (AS). Ultragenyx Pharmaceutical Inc. 2025. ClinicalTrials.gov Identifier: NCT07157254

28. (santos2023stemcellmodels pages 2-4): João Camões dos Santos, Carolina Appleton, Francisca Cazaux Mateus, Rita Covas, Evguenia Pavlovna Bekman, and Simão Teixeira da Rocha. Stem cell models of angelman syndrome. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1274040, doi:10.3389/fcell.2023.1274040. This article has 10 citations.

29. (santos2023stemcellmodels pages 9-10): João Camões dos Santos, Carolina Appleton, Francisca Cazaux Mateus, Rita Covas, Evguenia Pavlovna Bekman, and Simão Teixeira da Rocha. Stem cell models of angelman syndrome. Frontiers in Cell and Developmental Biology, Oct 2023. URL: https://doi.org/10.3389/fcell.2023.1274040, doi:10.3389/fcell.2023.1274040. This article has 10 citations.