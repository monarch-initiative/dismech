---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T19:31:41.154981'
end_time: '2026-05-07T19:44:16.352170'
duration_seconds: 755.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myxedema
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myxedema
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myxedema** covering all of the
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
- **Disease Name:** Myxedema
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myxedema** covering all of the
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


# Comprehensive Disease Characteristics Report: Myxedema (incl. Myxedema Coma)

## Target disease
**Disease name:** Myxedema (clinical syndrome of severe hypothyroidism with characteristic non‑pitting edema) and **myxedema coma** (decompensated, life‑threatening severe hypothyroidism). (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

**Note on scope and terminology:** Contemporary reviews emphasize that “myxedema coma” is a misnomer because mental status can range from lethargy to coma; some authors prefer “myxedema crisis.” (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

**Key identifiers (ICD/MeSH/MONDO/OMIM/Orphanet):** Not reliably extractable from the currently retrieved sources in this run; therefore not reported here (no evidence to cite).

**Common synonyms/related terms (usage varies by context):**
- *Generalized myxedema* (diffuse, non‑pitting edema/skin thickening in severe hypothyroidism) (bonino2023pediatricmyxedemadue pages 1-2, cohen2023dermatologicmanifestationsof pages 2-3)
- *Myxedema coma / hypothyroid coma / myxedema crisis* (severe decompensation) (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- *Pretibial myxedema* / *thyroid dermopathy* (localized mucin deposition classically associated with Graves disease; distinct from generalized myxedema) (cohen2023dermatologicmanifestationsof pages 2-3, demirkesen2015skinmanifestationsof pages 4-6)

**Data provenance:** This report uses aggregated evidence from peer‑reviewed reviews, cohorts, case series, and a national administrative database study; it is not derived from a single-patient EHR. (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2, sokołowski2024increasedincidenceof pages 2-4, hashmi2023weekendhospitaladmissions pages 4-9)

---

## 1. Disease information (overview)
**Myxedema (generalized)** is a manifestation of severe hypothyroidism characterized by non‑focal thickening/induration of skin and subcutaneous tissues due to increased deposition of connective tissue constituents (glycosaminoglycans/mucin) with water retention. (bonino2023pediatricmyxedemadue pages 1-2, cohen2023dermatologicmanifestationsof pages 2-3)

**Myxedema coma** is the extreme decompensated state of profound hypothyroidism with altered mentation and multisystem organ dysfunction, requiring ICU‑level care. (ylli2019thyroidemergencies pages 3-4, hwang2014treatmentofendocrine pages 6-9)

---

## 2. Etiology
### 2.1 Primary causal factors
**Underlying cause:** myxedema/myxedema coma generally arises from longstanding severe hypothyroidism (usually primary; less commonly central) with failure of compensatory mechanisms. (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2, sokołowski2024increasedincidenceof pages 2-4)

**Evidence (recent case series):** In a 2015–2023 Polish center cohort (n=11), 9 patients had primary hypothyroidism and 2 had central hypothyroidism; most cases were due to severe hypothyroidism from therapy non‑compliance, with 2 (18%) de novo diagnoses. (sokołowski2024increasedincidenceof pages 2-4)

### 2.2 Risk factors and triggers (myxedema coma)
Frequently reported precipitants include:
- **Infection** (pneumonia, sepsis) (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- **Cold exposure** and **winter seasonality** (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- **Stroke/CVA**, **heart failure**, **trauma**, **GI bleeding**, and **sedatives/other medications** (chaudhary2023utilityofmyxedema pages 1-2, garg2020handbookofinpatient pages 57-62)

**Medication-related risk:** Reviews highlight medications that may contribute to thyroid dysfunction/critical illness interpretation, including **amiodarone** (iodine-rich) and iodinated contrast, among others; amiodarone is noted in the hypothyroidism/ICU setting. (garg2020handbookofinpatient pages 57-62)

### 2.3 Protective factors
No directly evidenced genetic or environmental protective factors were identified in the retrieved sources. Prevention is implied through consistent hypothyroidism treatment adherence and healthcare access (see Section 13). (sokołowski2024increasedincidenceof pages 2-4)

### 2.4 Gene–environment interactions
Not specifically addressed in the retrieved evidence.

---

## 3. Phenotypes (clinical & laboratory) with ontology suggestions
### 3.1 Generalized myxedema (severe hypothyroidism)
**Core phenotype:** diffuse/non‑focal, **non‑pitting edema** and skin thickening/induration. (bonino2023pediatricmyxedemadue pages 1-2, cohen2023dermatologicmanifestationsof pages 2-3)

**HPO suggestions (examples):**
- Nonpitting edema (HP:0100651)
- Facial edema (HP:0000282)
- Periorbital edema (HP:0000284)
- Xerosis (dry skin) (HP:0000958)
- Hypothermia (HP:0002045) (in severe decompensation) (bonino2023pediatricmyxedemadue pages 1-2)

**Systemic involvement examples:** pericardial effusion reported in pediatric severe hypothyroidism with myxedema (up to 12 mm in a case). (bonino2023pediatricmyxedemadue pages 1-2)

### 3.2 Myxedema coma (decompensated severe hypothyroidism)
**Typical clinical features:**
- Altered mental status (lethargy → coma) (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- Hypothermia (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- Bradycardia and low cardiac output/hypotension (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)
- Hypoventilation with hypoxemia/hypercarbia; possible airway obstruction from macroglossia/peri‑laryngeal edema (ylli2019thyroidemergencies pages 3-4)
- Serous effusions (pleural/pericardial), ascites (ylli2019thyroidemergencies pages 3-4)

**Laboratory abnormalities (commonly reported):**
- Very low free T4 (often near undetectable) with variable TSH (including patterns consistent with central hypothyroidism) (ylli2019thyroidemergencies pages 3-4, sokołowski2024increasedincidenceof pages 2-4)
- Hyponatremia, hypoglycemia, and renal dysfunction (elevated BUN/creatinine) may occur (ylli2019thyroidemergencies pages 3-4)

**Quantitative thresholds used in a large cohort (operational definitions):**
- Hypothermia ≤35°C; hypotension <90/60 mmHg; bradycardia <60 bpm; hyponatremia <135 mEq/L; hypoglycemia ≤60 mg/dL; hypoxemia SatO2 <88% or PaO2 <55 mmHg. (chaudhary2023utilityofmyxedema pages 1-2)

**HPO suggestions (examples):**
- Abnormality of consciousness (HP:0001251)
- Hypothermia (HP:0002045)
- Bradycardia (HP:0001662)
- Hypotension (HP:0002615)
- Hyponatremia (HP:0002902)
- Hypoglycemia (HP:0001943)
- Hypoventilation (HP:0002791)
- Hypercapnia (HP:0012418)
- Hypoxemia (HP:0012418/HP:0002093 context-dependent)

**Course:** Cases cluster in winter and are commonly precipitated by acute stressors; delayed recognition is common due to nonspecific presentation. (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

**Quality-of-life impact:** Not quantified in retrieved sources; however, severe hypothyroid manifestations can impair daily function and, in coma, lead to critical illness requiring organ support. (ylli2019thyroidemergencies pages 3-4, hwang2014treatmentofendocrine pages 6-9)

---

## 4. Genetic / molecular information
**Causal genes/variants:** Myxedema is typically *not* a monogenic disorder; it is a clinical syndrome resulting from thyroid hormone deficiency. No causal gene/variant evidence was retrieved for this run.

**Autoimmune context:** For localized pretibial myxedema (thyroid dermopathy), thyrotropin receptor antibodies are implicated in some literature; older evidence suggests TRAb elevated in ~50% of pretibial myxedema cases (not specific to generalized myxedema). (anuradha2015pretibialmyxedemain pages 3-4)

---

## 5. Environmental information
**Cold exposure** and **winter seasonality** are repeatedly cited as triggers for decompensation (myxedema coma), consistent with environmental stress interacting with reduced thermogenesis in severe hypothyroidism. (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

**Medication exposures:** ICU/geriatric review highlights exposures relevant to thyroid dysfunction (e.g., amiodarone; iodinated contrast) in critically ill older adults. (garg2020handbookofinpatient pages 57-62)

---

## 6. Mechanism / pathophysiology
### 6.1 Generalized myxedema (severe hypothyroidism)
**Current understanding (skin/interstitium):**
- Major accumulating GAG in myxedema is **hyaluronic acid**. (cohen2023dermatologicmanifestationsof pages 1-2)
- Generalized myxedema is attributed to altered dermal mucopolysaccharides (GAGs) and increased dermal water content, producing cool, pale skin. (cohen2023dermatologicmanifestationsof pages 2-3)
- Mechanisms proposed include increased protein extravasation and relatively slow lymphatic drainage, contributing to interstitial swelling. (cohen2023dermatologicmanifestationsof pages 18-18)

**Cell types:** Dermal fibroblasts and epidermal keratinocytes are thyroid-hormone responsive; thyroid hormones stimulate keratinocyte and fibroblast growth and influence hyaluronate synthesis/barrier formation. (cohen2023dermatologicmanifestationsof pages 1-2)

**Histopathologic correlates (esp. thyroid dermopathy/pretibial form):** mucin/GAG deposition separating dermal collagen bundles; Alcian blue pH 2.5 and colloidal iron staining highlight mucin. (cohen2023dermatologicmanifestationsof pages 3-4, demirkesen2015skinmanifestationsof pages 4-6)

**GO biological process suggestions (examples):**
- Glycosaminoglycan metabolic process (GO:0006022)
- Extracellular matrix organization (GO:0030198)
- Hyaluronan metabolic process (GO:0030212)
- Regulation of fibroblast proliferation (GO:0048146)

**Cell Ontology suggestions:**
- Dermal fibroblast (CL:0002553, broadly “fibroblast” CL:0000057)
- Keratinocyte (CL:0000312) (cohen2023dermatologicmanifestationsof pages 1-2)

**UBERON suggestions:**
- Skin (UBERON:0002097)
- Dermis (UBERON:0002067)
- Epidermis (UBERON:0001003)

### 6.2 Myxedema coma (systemic decompensation)
Myxedema coma represents multisystem failure from profound thyroid hormone deficiency. Key downstream physiological effects described include hypoventilation with hypoxemia/hypercarbia, cardiovascular depression (bradycardia/low output), and serous effusions. (ylli2019thyroidemergencies pages 3-4)

A major clinical pathophysiology consideration is possible coexisting adrenal insufficiency; thyroid hormone replacement can increase cortisol metabolism and precipitate adrenal crisis, motivating empiric stress-dose glucocorticoids. (hwang2014treatmentofendocrine pages 6-9)

---

## 7. Anatomical structures affected
**Primary systems:** endocrine (thyroid axis), skin/subcutis, cardiovascular and respiratory systems, CNS. (ylli2019thyroidemergencies pages 3-4, cohen2023dermatologicmanifestationsof pages 1-2)

**Organ/tissue involvement (examples):**
- Skin/dermis (GAG/mucin deposition and edema) (cohen2023dermatologicmanifestationsof pages 1-2, cohen2023dermatologicmanifestationsof pages 2-3)
- Heart/pericardium (pericardial effusion; low output) (ylli2019thyroidemergencies pages 3-4, bonino2023pediatricmyxedemadue pages 1-2)
- Lungs/pleura (hypoventilation; pleural effusions) (ylli2019thyroidemergencies pages 3-4)

---

## 8. Temporal development
**Onset:** generalized myxedema typically develops insidiously with progressive hypothyroidism; myxedema coma often emerges acutely/subacutely in the setting of a precipitating factor (infection, cold exposure, etc.). (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

**Course:** Myxedema coma is rare but high risk and requires urgent intervention; delayed diagnosis is common because symptoms can resemble sepsis/metabolic encephalopathy. (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

---

## 9. Inheritance and population
**Inheritance pattern:** Not applicable as a primary inherited disease entity (clinical syndrome secondary to thyroid hormone deficiency).

**Epidemiology (myxedema coma):**
- A recent U.S. National Inpatient Sample (NIS) analysis (2016–2020) identified **5,095** myxedema coma hospitalizations with **overall inpatient mortality 11.60%**. (hashmi2023weekendhospitaladmissions pages 4-9, hashmi2023weekendhospitaladmissions pages 1-4)
- In that NIS study, mortality increased from **6.76% (2016) to 13.36% (2020)**, and weekend admissions had higher mortality: **13.11% weekend vs 8.38% weekday**, adjusted OR **1.91**. (hashmi2023weekendhospitaladmissions pages 4-9, hashmi2023weekendhospitaladmissions pages 1-4)
- A 2015–2023 single-center Polish series (n=11) reported mortality **27.2%** and suggested a marked rise in cases during/post‑COVID era (1 case in 2015–2019 vs 10 cases after pandemic onset). (sokołowski2024increasedincidenceof pages 2-4)

**Sex/age:** Reviews describe predominance in older adults and women (e.g., mean age 77 in one cited series; ~two-thirds women in review discussion). (ylli2019thyroidemergencies pages 3-4)

---

## 10. Diagnostics
### 10.1 Clinical diagnosis and scoring
Because presentation is nonspecific, scoring systems support structured diagnosis.

**Popoveniuc (myxedema coma) score thresholds:** cumulative score **≥60** correlates with myxedema coma; **45–59** indicates overt hypothyroidism with increased risk; ≤25 unlikely in some summaries. (ylli2019thyroidemergencies pages 3-4, aguirre2026fromthepopoveniuc pages 5-6)

A 2024 case series used a point-based score including neurologic status (e.g., coma/seizures), cardiovascular, respiratory, GI, and metabolic parameters; the paper restated that **60+ is highly suggestive/diagnostic; 25–59 suggests risk.** (sokołowski2024increasedincidenceof pages 2-4)

### 10.2 Laboratory tests
Recommended initial tests include thyroid function tests (TSH, free T4 ± T3) and metabolic panels, plus **baseline/random cortisol** prior to thyroid replacement where feasible (do not delay treatment). (garg2020handbookofinpatient pages 62-66)

### 10.3 Differential diagnosis
Nonspecific features overlap with sepsis, metabolic encephalopathy, and other causes of coma/shock; the diagnostic scoring approach and thyroid labs are used to support recognition in ambiguous cases. (ylli2019thyroidemergencies pages 3-4, hwang2014treatmentofendocrine pages 6-9)

---

## 11. Outcome / prognosis
### 11.1 Mortality
- Cohort mortality remains high; in one large single-center cohort spanning 1999–2020, mortality was **60.9%**. (chaudhary2023utilityofmyxedema pages 1-2)
- National inpatient mortality in the U.S. NIS analysis (2016–2020) was **11.6%** overall, with worsening trend through 2020. (hashmi2023weekendhospitaladmissions pages 4-9, hashmi2023weekendhospitaladmissions pages 1-4)

### 11.2 Prognostic factors
A 1999–2020 cohort analysis found higher mortality associated with:
- Higher myxedema score (see below)
- Need for mechanical ventilation
- In-hospital hypotension
- Higher qSOFA score
- Female sex (in that cohort). (chaudhary2023utilityofmyxedema pages 1-2)

**Myxedema score and mortality:** myxedema score **>90** associated with significantly higher mortality; **>110** associated with **100% mortality** in that cohort. (chaudhary2023utilityofmyxedema pages 1-2)

---

## 12. Treatment
### 12.1 Core treatment principles (ICU emergency)
Myxedema coma management consists of **rapid thyroid hormone replacement, empiric stress-dose glucocorticoids, and aggressive supportive care** (airway/ventilation, hemodynamic support, cautious rewarming, correction of metabolic derangements, and treatment of precipitating factors including infection). (ylli2019thyroidemergencies pages 3-4, garg2020handbookofinpatient pages 62-66)

### 12.2 Thyroid hormone replacement (dosing patterns in retrieved sources)
**IV levothyroxine (LT4) regimen (summarized guidance):**
- Loading **200–400 mcg IV**, followed by **50–100 mcg IV daily**. (lundholm2025myxedemacomadiagnostic pages 1-2, garg2020handbookofinpatient pages 62-66)

**Liothyronine (LT3) adjunct (selected cases / controversial):**
- **5–20 mcg IV once**, then **2.5–10 mcg IV q8h**, with lower doses for older adults or cardiac disease. (lundholm2025myxedemacomadiagnostic pages 1-2, garg2020handbookofinpatient pages 62-66)

### 12.3 Glucocorticoids
**Stress-dose hydrocortisone** recommended prior to/during thyroid hormone replacement, due to adrenal insufficiency risk:
- Hydrocortisone **50–100 mg IV every 6–8 hours** (and similar stress regimens). (garg2020handbookofinpatient pages 62-66)

### 12.4 Real-world implementation when IV LT4 is unavailable (oral/liquid LT4)
**Oral LT4 single-center experience:** 14 patients treated with an oral LT4 regimen including **300–500 mcg loading** followed by taper over several days; **13/14 survived**. (rajendran2021orallevothyroxineis pages 2-3)

**Protocol figure (oral LT4):** A published algorithm stratifies loading dose by coronary disease and LVEF and integrates baseline cortisol‑guided hydrocortisone. (rajendran2021orallevothyroxineis media 1ba7db35)

### 12.5 MAXO (Medical Action Ontology) suggestions
- Thyroid hormone replacement therapy (MAXO term suggestion: levothyroxine therapy / thyroid hormone replacement)
- Glucocorticoid therapy (stress-dose hydrocortisone)
- Mechanical ventilation
- Vasopressor therapy
- Passive rewarming
- Antibiotic therapy (when infection suspected)
- Electrolyte correction (e.g., hyponatremia management). (ylli2019thyroidemergencies pages 3-4, garg2020handbookofinpatient pages 62-66)

---

## 13. Prevention
Evidence in the retrieved sources supports prevention strategies focused on preventing progression of hypothyroidism to decompensation:
- **Medication adherence** and long-term follow-up: A 2024 case series attributed most cases to **therapy non-compliance** and emphasized maintaining healthcare access/communication, particularly during resource-limited periods (e.g., COVID-19 era). (sokołowski2024increasedincidenceof pages 2-4)
- **Risk reduction for triggers:** vigilance for infection/cold exposure in high-risk patients (older adults with severe hypothyroidism). (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2)

---

## 14. Other species / natural disease
No cross-species naturally occurring myxedema or zoonotic information was retrieved in this run.

---

## 15. Model organisms
No model organism evidence specific to myxedema/myxedema coma was retrieved in this run.

---

## Recent developments and latest research highlights (prioritizing 2023–2024)
1. **Myxedema score as a mortality predictor (2023):** A Journal of Endocrinological Investigation cohort study evaluated the Popoveniuc-derived myxedema score as a predictor of mortality and identified high-risk cutpoints (MS>90; MS>110). (chaudhary2023utilityofmyxedema pages 1-2)
2. **COVID-era access/implementation effects (2024):** A single-center case series reported increased myxedema coma incidence during/post-pandemic and documented use of oral (often liquid) LT4 due to lack of parenteral LT4. (sokołowski2024increasedincidenceof pages 2-4)
3. **Dermatologic mechanistic synthesis (2023):** A Frontiers in Endocrinology review summarized modern mechanistic understanding of thyroid-related skin disease, emphasizing hyaluronic-acid/GAG accumulation and the roles of fibroblasts/keratinocytes and lymphatic/vascular factors in myxedema. (cohen2023dermatologicmanifestationsof pages 1-2, cohen2023dermatologicmanifestationsof pages 3-4)

---

## Evidence table (selected quantitative and protocol data)
| Topic | Key data | Population/setting | Source (first author year, journal) | URL | Citation ID (pqac-...) |
|---|---|---|---|---|---|
| Epidemiology/incidence | Myxedema coma incidence reported as “as low as 1.08 per million people per year.” | Emergency medicine educational review summarizing epidemiology | Namespetra 2025, JETem | https://doi.org/10.21980/j8vm0j | (mansoor2025myxedemacomaas pages 4-5) |
| Mortality | Historical mortality described as 25–60%; in one 1999–2020 cohort, mortality was 60.9%. | Single-center cohort of myxedema crisis/coma patients | Chaudhary 2023, Journal of Endocrinological Investigation | https://doi.org/10.1007/s40618-022-01884-6 | (chaudhary2023utilityofmyxedema pages 1-2) |
| Mortality | Cohort mortality was 27.2%. | Single-center Krakow case series, 11 patients treated 2015–2023 | Sokołowski 2024, Internal and Emergency Medicine | https://doi.org/10.1007/s11739-024-03690-9 | (sokołowski2024increasedincidenceof pages 2-4) |
| Mortality trend / weekend effect | NIS study identified 5,095 myxedema coma hospitalizations (2016–2020); overall mortality 11.60%; weekend mortality 13.11% vs weekday 8.38%; adjusted OR for weekend admission 1.91 (95% CI 1.18–3.10), p=0.009. | U.S. National Inpatient Sample | Hashmi 2023, Research Square preprint | https://doi.org/10.21203/rs.3.rs-3085786/v1 | (hashmi2023weekendhospitaladmissions pages 4-9, hashmi2023weekendhospitaladmissions pages 1-4) |
| Mortality trend over time | Overall mortality increased from 6.76% in 2016 to 13.36% in 2020 (p=0.014). | U.S. National Inpatient Sample, 2016–2020 | Hashmi 2023, Research Square preprint | https://doi.org/10.21203/rs.3.rs-3085786/v1 | (hashmi2023weekendhospitaladmissions pages 4-9, hashmi2023weekendhospitaladmissions pages 1-4) |
| Diagnostic scoring cutoffs | Popoveniuc-style score: ≥60 highly suggestive/diagnostic; 25–59 suggests risk for myxedema coma. | Review/guideline summaries and case series using diagnostic score | Ylli 2021, Polish Archives of Internal Medicine; Sokołowski 2024, Internal and Emergency Medicine | https://doi.org/10.20452/pamw.14876 ; https://doi.org/10.1007/s11739-024-03690-9 | (ylli2019thyroidemergencies pages 3-4, sokołowski2024increasedincidenceof pages 2-4) |
| Mortality predictors by score | Myxedema score >90 associated with significantly higher mortality; score >110 associated with 100% mortality. | Single-center cohort, 1999–2020 | Chaudhary 2023, Journal of Endocrinological Investigation | https://doi.org/10.1007/s40618-022-01884-6 | (chaudhary2023utilityofmyxedema pages 1-2) |
| Other prognostic factors | Female sex, need for mechanical ventilation, in-hospital hypotension, and high qSOFA predicted mortality. | Single-center cohort, 1999–2020 | Chaudhary 2023, Journal of Endocrinological Investigation | https://doi.org/10.1007/s40618-022-01884-6 | (chaudhary2023utilityofmyxedema pages 1-2) |
| Key precipitants | Common precipitants include infection (especially pneumonia/sepsis), cold exposure, CVA/stroke, CHF, GI bleeding, trauma, sedatives; winter predominance noted. | Reviews and cohort studies of myxedema coma | Ylli 2021, Polish Archives of Internal Medicine; Chaudhary 2023, Journal of Endocrinological Investigation | https://doi.org/10.20452/pamw.14876 ; https://doi.org/10.1007/s40618-022-01884-6 | (ylli2019thyroidemergencies pages 3-4, chaudhary2023utilityofmyxedema pages 1-2) |
| COVID-era incidence change | At one center, 1 case occurred in 2015–2019 versus 10 cases after the start of the COVID-19 pandemic through 2023. | Single-center Krakow case series | Sokołowski 2024, Internal and Emergency Medicine | https://doi.org/10.1007/s11739-024-03690-9 | (sokołowski2024increasedincidenceof pages 2-4) |
| Etiology in recent case series | 2/11 (18%) had de novo hypothyroidism; 9/11 had severe hypothyroidism due to therapy non-compliance; 9 primary and 2 central hypothyroidism. | Single-center Krakow case series | Sokołowski 2024, Internal and Emergency Medicine | https://doi.org/10.1007/s11739-024-03690-9 | (sokołowski2024increasedincidenceof pages 2-4) |
| Key labs | Very low FT4 (often almost undetectable) with variable TSH; possible hypoglycemia, hyponatremia, low chloride, hypercalcemia, mild renal failure (elevated BUN/creatinine). | Review of thyroid emergencies | Ylli 2021, Polish Archives of Internal Medicine | https://doi.org/10.20452/pamw.14876 | (ylli2019thyroidemergencies pages 3-4) |
| Key labs / cohort thresholds | Defined thresholds used in cohort: hypothermia ≤35°C, hypotension <90/60 mmHg, bradycardia <60 bpm, hyponatremia <135 mEq/L, hypoglycemia ≤60 mg/dL, hypoxemia SatO2 <88% or PaO2 <55 mmHg. | Single-center cohort, 1999–2020 | Chaudhary 2023, Journal of Endocrinological Investigation | https://doi.org/10.1007/s40618-022-01884-6 | (chaudhary2023utilityofmyxedema pages 1-2) |
| Treatment doses | Recommended IV levothyroxine loading 200–400 mcg, then 50–100 mcg IV daily; consider IV liothyronine 5–20 mcg once then 2.5–10 mcg q8h; hydrocortisone 100 mg q8h or 50–100 mg every 6–8 h before/during thyroid replacement. | Guideline/review summaries | Lundholm 2025, Evidence to Action: Official Journal of MDCalc; Garg 2020, Handbook of Inpatient Endocrinology | https://doi.org/10.65357/001c.153938 ; https://doi.org/10.1007/978-3-030-38976-5 | (lundholm2025myxedemacomadiagnostic pages 1-2, garg2020handbookofinpatient pages 62-66) |
| Supportive care protocol | ICU admission; do not wait for labs; broad-spectrum antibiotics if infection suspected; assisted ventilation/intubation as needed; passive rewarming; fluids/vasopressors for hypotension; correction of hyponatremia/hypoglycemia. | Review/guideline summaries | Ylli 2021, Polish Archives of Internal Medicine; Garg 2020, Handbook of Inpatient Endocrinology | https://doi.org/10.20452/pamw.14876 ; https://doi.org/10.1007/978-3-030-38976-5 | (ylli2019thyroidemergencies pages 3-4, garg2020handbookofinpatient pages 62-66) |
| Oral LT4 protocol alternative | Oral LT4 regimen in 14 patients: loading dose 300–500 mcg followed by taper over 3–5 days; 13/14 survived. | Single-center retrospective observational study where IV LT4 unavailable | Rajendran 2021, European Thyroid Journal | https://doi.org/10.1159/000507855 | (rajendran2021orallevothyroxineis pages 2-3) |
| Oral LT4 protocol details | Algorithm stratified by cardiac status: no CAD, LD 500 mcg; CAD with normal LVEF, LD 300–400 mcg; CAD with LVEF <60%, LD 250–300 mcg; check FT4 every alternate day; if cortisol <15 mcg/dL give hydrocortisone 50–100 mg IV stat then q8h. | Figure 1 protocol for oral LT4 in myxedema coma | Rajendran 2021, European Thyroid Journal | https://doi.org/10.1159/000507855 | (rajendran2021orallevothyroxineis pages 2-3, rajendran2021orallevothyroxineis media 1ba7db35) |
| Alternative non-IV implementation | Due to lack of parenteral levothyroxine, recent Polish series used oral, mostly liquid, levothyroxine. | Single-center Krakow case series | Sokołowski 2024, Internal and Emergency Medicine | https://doi.org/10.1007/s11739-024-03690-9 | (sokołowski2024increasedincidenceof pages 2-4) |


*Table: This table compiles evidence-backed quantitative findings and practical treatment protocol details for myxedema coma from the gathered literature. It highlights incidence, mortality, diagnostic score cutoffs, prognostic markers, common precipitants, laboratory abnormalities, and both IV and oral levothyroxine treatment approaches.*

## Visual evidence: oral levothyroxine protocol
The following cited figure provides a practical, published algorithm for oral levothyroxine dosing and cortisol-guided hydrocortisone use in myxedema coma when IV LT4 is unavailable. (rajendran2021orallevothyroxineis media 1ba7db35)

---

## Notes on evidence gaps and PMIDs
- Several key retrieved items are peer‑reviewed but the tool-extracted metadata did not include PMIDs; thus, this report cannot provide PMID‑keyed citations without risking fabrication. URLs and DOIs are provided where available in the sources above. 
- Dedicated interventional clinical trials for myxedema coma were not identified in the retrieved ClinicalTrials.gov search results; available trials largely address hypothyroidism broadly rather than myxedema coma specifically. (clinical trials retrieved; no relevant myxedema-coma interventional trials identified in evidence)


References

1. (ylli2019thyroidemergencies pages 3-4): D. Ylli, J. Klubo-Gwiezdzinska, and L. Wartofsky. Thyroid emergencies. Polish archives of internal medicine, 129:526-534, Jun 2021. URL: https://doi.org/10.20452/pamw.14876, doi:10.20452/pamw.14876. This article has 21 citations.

2. (chaudhary2023utilityofmyxedema pages 1-2): S. Chaudhary, L. Das, Nikhil Sharma, N. Sachdeva, A. Bhansali, and P. Dutta. Utility of myxedema score as a predictor of mortality in myxedema coma. Journal of Endocrinological Investigation, 46:59-65, Aug 2023. URL: https://doi.org/10.1007/s40618-022-01884-6, doi:10.1007/s40618-022-01884-6. This article has 19 citations and is from a peer-reviewed journal.

3. (bonino2023pediatricmyxedemadue pages 1-2): Elisa Bonino, Patrizia Matarazzo, Raffaele Buganza, Gerdi Tuli, Jessica Munarin, Claudia Bondone, and Luisa de Sanctis. Pediatric myxedema due to autoimmune hypothyroidism: a rare complication of a common disorder. Children, 10:614, Mar 2023. URL: https://doi.org/10.3390/children10040614, doi:10.3390/children10040614. This article has 3 citations.

4. (cohen2023dermatologicmanifestationsof pages 2-3): Benjamin Cohen, Adam Cadesky, and Shuchie Jaggi. Dermatologic manifestations of thyroid disease: a literature review. Frontiers in Endocrinology, May 2023. URL: https://doi.org/10.3389/fendo.2023.1167890, doi:10.3389/fendo.2023.1167890. This article has 63 citations.

5. (demirkesen2015skinmanifestationsof pages 4-6): Cuyan Demirkesen. Skin manifestations of endocrine diseases. Turk patoloji dergisi, 31 Suppl 1:145-54, Jan 2015. URL: https://doi.org/10.5146/tjpath.2015.01321, doi:10.5146/tjpath.2015.01321. This article has 24 citations.

6. (sokołowski2024increasedincidenceof pages 2-4): Grzegorz Sokołowski, Katica Bajuk Studen, Marta Opalinska, Karolina Wegrzyn, Marcin Motyka, Aleksandra Gilis-Januszewska, and Alicja Hubalewska-Dydejczyk. Increased incidence of myxedema coma during the covid-19 pandemic and in the post pandemic era: a single-center case series. Internal and Emergency Medicine, 19:1921-1928, Jul 2024. URL: https://doi.org/10.1007/s11739-024-03690-9, doi:10.1007/s11739-024-03690-9. This article has 2 citations and is from a peer-reviewed journal.

7. (hashmi2023weekendhospitaladmissions pages 4-9): Mariam Hashmi, Zubair Hassan Bodla, Fatima Niaz, Umer Farooq, Christopher L. Bray, and Peters Okonoboh. Weekend hospital admissions for myxedema coma linked to higher mortality rates: an insight from national inpatient sample from 2016 to 2020. Jun 2023. URL: https://doi.org/10.21203/rs.3.rs-3085786/v1, doi:10.21203/rs.3.rs-3085786/v1.

8. (hwang2014treatmentofendocrine pages 6-9): Janice J. Hwang and David Y. Hwang. Treatment of endocrine disorders in the neuroscience intensive care unit. Current Treatment Options in Neurology, 16:1-15, Jan 2014. URL: https://doi.org/10.1007/s11940-013-0271-4, doi:10.1007/s11940-013-0271-4. This article has 24 citations and is from a peer-reviewed journal.

9. (garg2020handbookofinpatient pages 57-62): RK Garg. Handbook of Inpatient Endocrinology. Springer International Publishing, Jan 2020. URL: https://doi.org/10.1007/978-3-030-38976-5, doi:10.1007/978-3-030-38976-5.

10. (anuradha2015pretibialmyxedemain pages 3-4): KB Anuradha and K Prasad. Pretibial myxedema in hypothyroidism-a clinical paradox. Unknown journal, 2015.

11. (cohen2023dermatologicmanifestationsof pages 1-2): Benjamin Cohen, Adam Cadesky, and Shuchie Jaggi. Dermatologic manifestations of thyroid disease: a literature review. Frontiers in Endocrinology, May 2023. URL: https://doi.org/10.3389/fendo.2023.1167890, doi:10.3389/fendo.2023.1167890. This article has 63 citations.

12. (cohen2023dermatologicmanifestationsof pages 18-18): Benjamin Cohen, Adam Cadesky, and Shuchie Jaggi. Dermatologic manifestations of thyroid disease: a literature review. Frontiers in Endocrinology, May 2023. URL: https://doi.org/10.3389/fendo.2023.1167890, doi:10.3389/fendo.2023.1167890. This article has 63 citations.

13. (cohen2023dermatologicmanifestationsof pages 3-4): Benjamin Cohen, Adam Cadesky, and Shuchie Jaggi. Dermatologic manifestations of thyroid disease: a literature review. Frontiers in Endocrinology, May 2023. URL: https://doi.org/10.3389/fendo.2023.1167890, doi:10.3389/fendo.2023.1167890. This article has 63 citations.

14. (hashmi2023weekendhospitaladmissions pages 1-4): Mariam Hashmi, Zubair Hassan Bodla, Fatima Niaz, Umer Farooq, Christopher L. Bray, and Peters Okonoboh. Weekend hospital admissions for myxedema coma linked to higher mortality rates: an insight from national inpatient sample from 2016 to 2020. Jun 2023. URL: https://doi.org/10.21203/rs.3.rs-3085786/v1, doi:10.21203/rs.3.rs-3085786/v1.

15. (aguirre2026fromthepopoveniuc pages 5-6): Rodolfo A Valerio Aguirre, Karla C Ocaña Martinez, Erick U Martinez Rodriguez, Taide I Cabrera López, and Jonathan G Gonzalez Mena. From the popoveniuc score to therapeutic protocols: a comprehensive review of myxedema coma. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.101023, doi:10.7759/cureus.101023. This article has 0 citations.

16. (garg2020handbookofinpatient pages 62-66): RK Garg. Handbook of Inpatient Endocrinology. Springer International Publishing, Jan 2020. URL: https://doi.org/10.1007/978-3-030-38976-5, doi:10.1007/978-3-030-38976-5.

17. (lundholm2025myxedemacomadiagnostic pages 1-2): Michelle D. Lundholm. Myxedema coma diagnostic score. Evidence to Action: Official Journal of MDCalc, Dec 2025. URL: https://doi.org/10.65357/001c.153938, doi:10.65357/001c.153938. This article has 0 citations.

18. (rajendran2021orallevothyroxineis pages 2-3): Arjun Rajendran, Nisha Bhavani, Vasantha Nair, Praveen V. Pavithran, V. Usha Menon, and Harish Kumar. Oral levothyroxine is an effective option for myxedema coma: a single-centre experience. European Thyroid Journal, 10:52-58, Jun 2021. URL: https://doi.org/10.1159/000507855, doi:10.1159/000507855. This article has 38 citations and is from a peer-reviewed journal.

19. (rajendran2021orallevothyroxineis media 1ba7db35): Arjun Rajendran, Nisha Bhavani, Vasantha Nair, Praveen V. Pavithran, V. Usha Menon, and Harish Kumar. Oral levothyroxine is an effective option for myxedema coma: a single-centre experience. European Thyroid Journal, 10:52-58, Jun 2021. URL: https://doi.org/10.1159/000507855, doi:10.1159/000507855. This article has 38 citations and is from a peer-reviewed journal.

20. (mansoor2025myxedemacomaas pages 4-5): Rabia Mansoor, Maheen Iqbal, Tushaar Kakkar, Aymen Bader, and Taha Elsahy. Myxedema coma as the initial presentation of undiagnosed hypothyroidism: a rare but reversible emergency. Cureus, Dec 2025. URL: https://doi.org/10.7759/cureus.98621, doi:10.7759/cureus.98621. This article has 0 citations.