---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T18:32:32.717735'
end_time: '2026-04-25T18:52:27.534054'
duration_seconds: 1194.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Li-Fraumeni Syndrome
  mondo_id: MONDO:0018875
  category: Hereditary Cancer Syndrome
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Li-Fraumeni Syndrome
- **MONDO ID:** MONDO:0018875 (if available)
- **Category:** Hereditary Cancer Syndrome

## Research Objectives

Please provide a comprehensive research report on **Li-Fraumeni Syndrome** covering all of the
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
- **Disease Name:** Li-Fraumeni Syndrome
- **MONDO ID:** MONDO:0018875 (if available)
- **Category:** Hereditary Cancer Syndrome

## Research Objectives

Please provide a comprehensive research report on **Li-Fraumeni Syndrome** covering all of the
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


# Li‑Fraumeni Syndrome (LFS; Heritable TP53‑related cancer syndrome) — Comprehensive Disease Characteristics Research Report

## 1. Disease Information

### Overview / definition
Li‑Fraumeni syndrome (LFS) is a classical, highly penetrant hereditary cancer predisposition syndrome characterized by early onset cancers and an unusually broad tumor spectrum, most commonly driven by germline pathogenic variants in **TP53**. (giovino2024newparadigmsin pages 2-4, sanchezheras2023seomclinicalguideline pages 1-2)

Because many TP53‑associated cancer presentations do not meet “classic” LFS family-history patterns, European and national guidelines describe a broader umbrella entity, **heritable TP53‑related cancer syndrome (hTP53rc)**. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

### Key identifiers (available from retrieved sources)
- **MONDO:** The user-specified MONDO:0018875 corresponds to “Li‑Fraumeni syndrome”; the identifier appears as MONDO_0018875 in OpenTargets-derived association output. (frebourg2020guidelinesforthe pages 1-2)
- **Other identifiers (OMIM, Orphanet, ICD‑10/ICD‑11, MeSH):** Not retrieved in the accessible full texts during this run; should be added from OMIM/Orphanet/MeSH as a curation step outside the included sources.

### Synonyms / alternative names
- **SBLA syndrome** (“Sarcoma, Breast, Leukemia, and Adrenal Gland syndrome”) is cited as an alternative name for LFS in a recent review. (hosseini2024currentinsightsand pages 1-4)
- **Heritable TP53‑related cancer syndrome (hTP53rc)** is used in guidelines to encompass “attenuated” and non-classical presentations. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

### Evidence type notes
This report synthesizes **aggregated disease-level resources** (international/national guidelines, systematic reviews, cohort penetrance analyses, genome-first biobank studies) and **human clinical research** (cfDNA surveillance proof-of-principle; MRI surveillance studies) rather than EHR-only single-institution datasets. (fortuno2024cancerrisksassociated pages 1-2, temperley2024wholebodymriscreening pages 11-13, wong2024earlycancerdetection pages 1-3, andrade2024genomefirstapproachof pages 2-3)

## 2. Etiology

### Disease causal factors
**Genetic etiology (primary):** heterozygous germline pathogenic/likely pathogenic variants in **TP53** cause LFS/hTP53rc. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

**De novo variants:** de novo TP53 variants are estimated at **~7–20%** of cases in ERN GENTURIS guidance, supporting testing even without strong family history. (frebourg2020guidelinesforthe pages 1-2)

### Risk factors
- **Family history and early onset cancers** are key clinical flags for testing and diagnosis, but reliance on family history alone misses de novo and “attenuated” presentations. (giovino2024newparadigmsin pages 2-4, frebourg2020guidelinesforthe pages 1-2)
- **Iatrogenic/exposure-related risk amplification:** Radiotherapy and conventional genotoxic chemotherapies contribute to subsequent primary tumors in TP53 carriers; guidance emphasizes TP53 testing before treatment to minimize these exposures where possible. (frebourg2020guidelinesforthe pages 1-2)

### Protective factors
No proven licensed chemopreventive agents exist for LFS/hTP53rc in current standard care; chemoprevention is an active research area. (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2)

### Gene–environment interactions
- **Treatment-related mutational processes:** Whole-genome tumor studies in germline TP53 carriers report mutational signatures associated with prior chemotherapy and other genotoxin exposures (e.g., cisplatin and bacterial genotoxin signatures), consistent with environmental/treatment modifiers of tumor evolution. (light2023germlinetp53mutations pages 6-7)
- **Modifier biology:** Multiple genetic polymorphisms and epigenetic regulators are proposed to modify age at onset and phenotype, implying a complex GxE landscape. (gargallo2020li–fraumenisyndromeheterogeneity pages 2-4, gargallo2020li–fraumenisyndromeheterogeneity pages 7-8)

## 3. Phenotypes

### Core tumor spectrum (clinical phenotypes)
Guidelines and reviews consistently describe a “core” LFS tumor spectrum that includes:
- Premenopausal/early-onset **breast cancer**
- **Soft tissue sarcoma**
- **Osteosarcoma**
- **Central nervous system (CNS) tumors**
- **Adrenocortical carcinoma (ACC)** (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

Rare/highly suggestive tumors for TP53 testing include **choroid plexus carcinoma**, **hypodiploid ALL**, **anaplastic embryonal rhabdomyosarcoma**, **SHH medulloblastoma**, and **jaw osteosarcoma**. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 4-5)

### Age of onset / natural history
- LFS is marked by **early-onset** cancers across childhood and adulthood, with diagnostic criteria explicitly using early ages (e.g., core cancers <46 years in modified Chompret). (sanchezheras2023seomclinicalguideline pages 2-4)
- Penetrance is high and age-dependent, with sex differences driven largely by early breast cancer risk in females. (fortuno2024cancerrisksassociated pages 1-2)

### Frequencies / quantitative phenotype risks (recent)
- In a large maximum-likelihood pedigree analysis (146 TP53-positive families; 4,028 individuals), the **cumulative risk of any cancer by age 50** was **92.4% in females** and **59.7% in males**; female **breast cancer risk by age 50** was **63.3%**. (fortuno2024cancerrisksassociated pages 1-2)

### Quality of life impact
Quality-of-life impact is primarily mediated by repeated screening, follow-up of incidental findings, anxiety, and (in pediatrics) sedation requirements for MRI-based surveillance. (temperley2024wholebodymriscreening pages 11-13, kumamoto2021medicalguidelinesfor pages 1-2)

### Suggested HPO terms (examples; not exhaustive)
Tumor phenotypes (HPO broadly):
- Breast carcinoma — **HP:0003002**
- Soft tissue sarcoma — **HP:0100242**
- Osteosarcoma — **HP:0006731**
- Brain neoplasm — **HP:0004375**
- Adrenocortical carcinoma — **HP:0006746**
Additional TP53-associated rare tumors:
- Choroid plexus carcinoma — **HP:0030858**
- Acute lymphoblastic leukemia — **HP:0006728**

## 4. Genetic / Molecular Information

### Causal gene(s)
- **TP53** is the principal causal gene for LFS/hTP53rc. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

### Pathogenic variant features and classification considerations
- TP53 variants include missense, nonsense, splice-site, frameshift, and others; missense variants in the DNA-binding domain are common and may exert **dominant-negative** effects (mutant monomers inactivate wild-type monomers) and/or **gain-of-function** activities. (hosseini2024currentinsightsand pages 1-4, gargallo2020li–fraumenisyndromeheterogeneity pages 2-4)
- **Variant interpretation in blood** must consider clonal hematopoiesis (CHIP) and mosaicism; the SEOM guideline notes that **VAF ~40–50%** supports germline origin, while **VAF 10–40%** suggests mosaicism and requires confirmation in non-lymphoid tissues to exclude CHIP/ctDNA. (sanchezheras2023seomclinicalguideline pages 2-4)

### Population prevalence (genome-first)
A large genome-first analysis across EHR-linked cohorts (414,824 individuals) found prevalence estimates that depend on cohort selection and potential CH confounding:
- UK Biobank (after excluding hematologic cancers): **~1:10,438**
- Geisinger (after excluding hematologic cancers): **~1:3,790**
- PMBB (after excluding hematologic cancers): **~1:2,983** (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 3-4)

### Modifier genes / variants (evidence and examples)
A heterogeneity-focused review summarizes evidence that age of onset can be modified by polymorphisms including:
- **MDM2 SNP309** (G allele associated with earlier tumor onset)
- **TP53 PIN3** polymorphism (heterozygotes associated with earlier onset)
- **TP53 p.Pro72Arg** polymorphism (Arg allele associated with earlier onset) (gargallo2020li–fraumenisyndromeheterogeneity pages 2-4)

Epigenetic/noncoding regulators (candidate modifiers) include multiple miRNAs (e.g., miR‑34 family) and lncRNAs (e.g., Wrap53), as well as telomere shortening and other factors. (gargallo2020li–fraumenisyndromeheterogeneity pages 7-8)

### Epigenetic information
Mechanistic reviews propose that altered regulation of TP53 expression via miRNAs/lncRNAs and DNA methylation pathways may contribute to intrafamilial variability. (gargallo2020li–fraumenisyndromeheterogeneity pages 7-8)

## 5. Environmental Information

### Environmental and lifestyle factors
Direct, quantitative environmental risk factors for cancer incidence in TP53 carriers were not established in the retrieved primary sources. However, guideline and mechanistic literature emphasize **minimizing iatrogenic radiation exposure** (diagnostic CT/mammography where alternatives exist, and radiotherapy where feasible) due to subsequent primary tumor risk. (frebourg2020guidelinesforthe pages 1-2, sanchezheras2023seomclinicalguideline pages 4-6)

### Infectious agents
No infectious causal agent is implicated for LFS; it is a genetic predisposition syndrome.

## 6. Mechanism / Pathophysiology

### Causal chain (high-level)
1. **Germline TP53 pathogenic variant** reduces normal p53 tumor suppressor function (via LOF and/or dominant-negative effects; some variants may have GOF properties). (gargallo2020li–fraumenisyndromeheterogeneity pages 2-4)
2. Cells experience impaired **DNA damage response**, **cell-cycle checkpoint control**, and **apoptosis/ferroptosis-related tumor suppression** programs, enabling malignant transformation. (gargallo2020li–fraumenisyndromeheterogeneity pages 2-4, vanikova2024functionalanalysisof pages 67-70)
3. A frequent early tumorigenic step is a **“second hit”** at TP53: tumor and fibroblast data show early **TP53 loss-of-heterozygosity (LOH)** and **copy-number gain of the mutant allele**, occurring years before diagnosis and earlier than in sporadic cancers with somatic TP53 alterations. (light2023germlinetp53mutations pages 1-2, light2023germlinetp53mutations pages 6-7)
4. Additional recurrent somatic alterations accumulate in pathways such as **Wnt**, **PI3K/AKT**, **epigenetic modifiers**, and **homologous recombination genes**, shaping tumor type and evolution. (light2023germlinetp53mutations pages 1-2)

### Recent molecular profiling developments (2023–2024)
- Whole-genome analyses indicate **near-ubiquitous early TP53 LOH with gain of the mutant allele** as a characteristic process in LFS tumorigenesis. (light2023germlinetp53mutations pages 1-2, light2023germlinetp53mutations pages 6-7)
- Liquid biopsy (multiomic cfDNA) has emerged as a candidate adjunct surveillance strategy (see §10). (wong2024earlycancerdetection pages 1-3)

### Suggested ontology terms
**GO Biological Process (examples):**
- DNA damage response, signal transduction by p53 class mediator — GO:0030330
- Regulation of apoptotic process — GO:0042981
- Cell cycle arrest — GO:0007050
- Regulation of transcription by RNA polymerase II — GO:0006357

**CL cell types (examples relevant to cancers in spectrum):**
- Hematopoietic stem cell — CL:0000037
- Epithelial cell (breast) — CL:0000066
- Osteoblast — CL:0000062
- Glial cell — CL:0000121

**UBERON anatomical structures (examples):**
- Breast — UBERON:0000310
- Brain — UBERON:0000955
- Adrenal gland cortex — UBERON:0002367
- Bone — UBERON:0002481

## 7. Anatomical Structures Affected
LFS/hTP53rc is a systemic predisposition affecting multiple organ systems due to ubiquitous TP53 function; clinically, tumors commonly arise in breast, bone/soft tissues, CNS, and adrenal cortex. (sanchezheras2023seomclinicalguideline pages 1-2, frebourg2020guidelinesforthe pages 1-2)

## 8. Temporal Development
- **Onset:** often pediatric to young-adult onset, with surveillance recommended from birth in high-risk contexts. (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5)
- **Course:** lifelong predisposition with frequent multiple primaries; one guideline estimates ~half of cases develop synchronous/metachronous multiple cancers. (kumamoto2021medicalguidelinesfor pages 1-2)

## 9. Inheritance and Population

### Inheritance
LFS is typically **autosomal dominant**. (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2, kumamoto2021medicalguidelinesfor pages 1-2)

### Epidemiology (recent quantitative data)
- Genome-first cohorts suggest prevalence on the order of **~1:10,000** in a population cohort (UK Biobank) and **~1:3,000** in health-system cohorts after attempts to reduce clonal hematopoiesis confounding. (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 3-4)

### Penetrance / expressivity
- Penetrance is high and sex-dependent; in the Fortuno et al. pedigree analysis, cumulative any-cancer risk by age 50 reached **92.4% (females)** and **59.7% (males)**. (fortuno2024cancerrisksassociated pages 1-2)
- Variable penetrance and expressivity are influenced by variant class (e.g., dominant-negative effects) and modifying factors. (frebourg2020guidelinesforthe pages 1-2, gargallo2020li–fraumenisyndromeheterogeneity pages 2-4)

## 10. Diagnostics

### Clinical criteria (testing indications)
The SEOM guideline specifies **modified Chompret** testing indications, including early-onset core cancers, multiple primaries, and specific rare pediatric tumors; it also recommends testing after a second primary tumor arising in a prior radiotherapy field following an early core tumor. (sanchezheras2023seomclinicalguideline pages 2-4)

### Genetic testing approach
- Germline TP53 testing is recommended promptly when LFS/hTP53rc is suspected; testing should ideally occur before initiating radiotherapy/genotoxic chemotherapy. (kumamoto2021medicalguidelinesfor pages 1-2, frebourg2020guidelinesforthe pages 1-2)
- Low VAF TP53 findings in blood should prompt confirmation in non-lymphoid tissue to address mosaicism/CHIP. (sanchezheras2023seomclinicalguideline pages 2-4, andrade2024genomefirstapproachof pages 6-7)

### Screening / surveillance (real-world implementation)
Guidelines emphasize MRI/ultrasound-based surveillance. A SEOM guideline-derived schedule is summarized in the artifact below (children vs adults, imaging intervals). (sanchezheras2023seomclinicalguideline pages 4-6)

**Whole-body MRI evidence (2024 update):** A 2024 systematic review/meta-analysis pooling eight studies (506 carriers) found a **pooled WB‑MRI cancer detection rate of 7% (95% CI 5–10%)** and 36/506 (7.1%) new cancers diagnosed. (temperley2024wholebodymriscreening pages 11-13, temperley2024wholebodymriscreening pages 9-11)

**Harms/limitations:** WB‑MRI can yield incidental lesions and anxiety, lacks universal protocol standardization, and lacks cost-effectiveness evaluation in included studies. (temperley2024wholebodymriscreening pages 11-13)

### Emerging diagnostics: multiomic cfDNA “liquid biopsy”
A 2024 Cancer Discovery report describes multimodal cfDNA (targeted sequencing, shallow WGS, methylation) in TP53 carriers under Toronto Protocol surveillance. It reports multimodal performance metrics (PPV/NPV) and examples of detection months-to-years before clinical diagnosis (e.g., methylation signal ~20 months before osteosarcoma), supporting liquid biopsy as a potential adjunct to annual imaging. (wong2024earlycancerdetection pages 1-3, wong2024earlycancerdetection pages 9-11, wong2024earlycancerdetection pages 8-9)

### Clinical trials / ongoing studies (selected)
- **SIGNIFY** (NCT01737255; completed): observational case-control of whole-body and brain MRI in adult TP53 carriers vs controls; included psychological outcomes. (NCT01737255 chunk 1)
- **WB‑MRI screening in LFS and other syndromes** (NCT02950987; active not recruiting): single-group interventional study assessing annual return/retention over four annual scans and cancer detection tabulation. (NCT02950987 chunk 1)
- **Pediatric imaging trait study** (NCT03176836; enrolling by invitation): evaluates imaging traits (STIR/DWI, PET‑MRI conditional) to support imaging–phenotype analyses in children. (NCT03176836 chunk 1)
- **TP53/LFS biobank with ctDNA aims** (NCT04367246; recruiting): prospective biospecimen and clinical data collection with ctDNA utility endpoints. (NCT04367246 chunk 1)

## 11. Outcome / Prognosis

### Surveillance-associated outcomes
The SEOM guideline reports that Toronto Protocol surveillance improved 5‑year survival (**88% vs 59.6%**). (sanchezheras2023seomclinicalguideline pages 2-4)

### Multi-cancer risk and subsequent malignancies
Guidelines emphasize risk of multiple primaries and treatment-related subsequent primaries, motivating radiation-sparing management and lifelong surveillance. (frebourg2020guidelinesforthe pages 1-2, kumamoto2021medicalguidelinesfor pages 1-2)

## 12. Treatment

### Core management principle
LFS is a cancer predisposition syndrome rather than a single tumor entity; treatment is cancer-type specific, but management is strongly influenced by TP53 carrier status.

### Special considerations (authoritative guidance)
- **Avoid or minimize radiotherapy and conventional genotoxic chemotherapy** when feasible because of risk of subsequent primary tumors; perform TP53 testing before treatment initiation when possible. (frebourg2020guidelinesforthe pages 1-2)

### Preventive / risk-reducing interventions
- **Risk-reducing bilateral mastectomy** is discussed as an option for women (decision individualized). (sanchezheras2023seomclinicalguideline pages 4-6, kumamoto2021medicalguidelinesfor pages 1-2)

**Suggested MAXO terms (examples):**
- Cancer surveillance — **MAXO:0000535**
- Whole-body magnetic resonance imaging — **MAXO:0001064** (imaging procedure)
- Prophylactic mastectomy — **MAXO:0001103**
- Genetic counseling — **MAXO:0000079**

### Experimental / emerging interventions (2023–2024)
- **Metformin chemoprevention trial (MILI):** A randomized, open-label phase II trial protocol randomizes 224 adults with LFS to oral metformin plus annual MRI surveillance vs surveillance alone; primary endpoint is 5-year cumulative cancer-free survival. (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2)
  - **CHEBI:** metformin — **CHEBI:6801**

## 13. Prevention

### Primary/secondary prevention
- **Secondary prevention is central:** guideline-based surveillance beginning as soon as carrier status is known and continuing lifelong, using WB‑MRI, brain MRI, and (women) breast MRI; in children, frequent physical exams and abdominal/pelvic ultrasound for ACC surveillance. (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5)

### Radiation avoidance
- Mammography and CT should be minimized when MRI/ultrasound alternatives exist; radiotherapy avoidance is recommended where feasible. (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 1-2)

## 14. Other Species / Natural Disease
No naturally occurring “Li‑Fraumeni syndrome” diagnosis in non-human species was retrieved from the accessed texts. Mechanistic conservation of TP53 biology is strong across vertebrates, and TP53-driven tumor predisposition is widely modeled experimentally (see §15).

## 15. Model Organisms

### Model systems (evidence retrieved)
- **Human carrier-derived cell models:** Primary fibroblasts from TP53 germline variant carriers can undergo spontaneous TP53 LOH and mutant allele copy gain in culture, with high mutant p53 accumulation after LOH. (light2023germlinetp53mutations pages 6-7)
- **Mouse models:** Reviews describe Tp53 mutant knock-in hotspot alleles (e.g., R172H) as models for mutant-p53 biology including ferroptosis pathway interactions, and transposon-based mouse systems show altered tumor latency in the setting of germline Tp53. (vanikova2024functionalanalysisof pages 67-70, levine2021spontaneousandinherited pages 1-2)

### Applications and limitations
- These models are used to study (i) timing and selection of the second TP53 hit, (ii) pathway co-drivers, and (iii) surveillance biomarkers (e.g., cfDNA signals). Tumor spectrum and penetrance in specific engineered mouse alleles are not fully detailed in the retrieved full texts and should be supplemented from dedicated model-organism resources (MGI/IMSR) for knowledge base completeness.

## Recent developments (2023–2024) — focused highlights

1. **Refined penetrance estimates addressing ascertainment bias (2024):** Maximum-likelihood pedigree modeling across 146 TP53 families provides updated, age- and sex-specific risk estimates and extends elevated risks to additional cancers (e.g., colorectal, gastric, lung, pancreatic, ovarian). (fortuno2024cancerrisksassociated pages 1-2)
2. **Genome-first prevalence differences and clonal hematopoiesis confounding (2024):** Large biobank analyses show cohort-dependent prevalence estimates (~1:3,000 in health-system cohorts vs ~1:10,000 in UK Biobank after excluding hematologic cancers) and recommend careful VAF/tissue confirmation. (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 6-7)
3. **Whole-body MRI evidence synthesis (2024):** Meta-analysis confirms ~7% pooled cancer detection on WB‑MRI but highlights incidental findings, protocol non-standardization, and missing cost-effectiveness evidence. (temperley2024wholebodymriscreening pages 11-13)
4. **Multiomic cfDNA for early detection (2024):** Multimodal liquid biopsy in TP53 carriers provides PPV/NPV estimates and case examples with ctDNA/methylation/fragmentation signals preceding conventional detection, supporting development of adjunct screening strategies. (wong2024earlycancerdetection pages 1-3, wong2024earlycancerdetection pages 9-11)
5. **Chemoprevention trial initiation (2024):** MILI evaluates metformin as a prevention agent alongside annual MRI surveillance in adults with LFS. (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2)

## Evidence tables (for knowledge base population)

| Metric | Value | Population/Context | Source (short) | URL | Publication date |
|---|---:|---|---|---|---|
| Lifetime cancer risk, males | ~70% | Classical Li-Fraumeni syndrome / germline TP53 pathogenic variant carriers | Dixon-Zegeye et al. 2024 (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2) | https://doi.org/10.1186/s13063-024-07929-w | 2024-02 |
| Lifetime cancer risk, females | ~100% | Classical Li-Fraumeni syndrome / germline TP53 pathogenic variant carriers | Dixon-Zegeye et al. 2024 (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2) | https://doi.org/10.1186/s13063-024-07929-w | 2024-02 |
| Lifetime cancer risk, males | ~75% | TP53 pathogenic variant carriers; guideline estimate | Kumamoto et al. 2021 (kumamoto2021medicalguidelinesfor pages 1-2) | https://doi.org/10.1007/s10147-021-02011-w | 2021-10 |
| Lifetime cancer risk, females | >90% to nearly 100% | TP53 pathogenic variant carriers; review/guideline estimates | Giovino et al. 2024; Kumamoto et al. 2021 (giovino2024newparadigmsin pages 2-4, kumamoto2021medicalguidelinesfor pages 1-2) | https://doi.org/10.1101/cshperspect.a041584 ; https://doi.org/10.1007/s10147-021-02011-w | 2024-05; 2021-10 |
| Cumulative risk of any cancer by age 50, females | 92.4% (95% CI 82.2–98.3) | TP53-positive families; maximum-likelihood pedigree analysis | Fortuno et al. 2024 (fortuno2024cancerrisksassociated pages 1-2) | https://doi.org/10.1200/PO.23.00453 | 2024-02 |
| Cumulative risk of any cancer by age 50, males | 59.7% (95% CI 39.9–81.3) | TP53-positive families; maximum-likelihood pedigree analysis | Fortuno et al. 2024 (fortuno2024cancerrisksassociated pages 1-2) | https://doi.org/10.1200/PO.23.00453 | 2024-02 |
| Cumulative breast cancer risk by age 50, females | 63.3% (95% CI 35.6–90.1) | Female TP53 carriers | Fortuno et al. 2024 (fortuno2024cancerrisksassociated pages 1-2) | https://doi.org/10.1200/PO.23.00453 | 2024-02 |
| Prevalence of P/LP germline TP53 variants, UK Biobank | 1:10,438 | Genome-first cohort after excluding hematologic-cancer/confounded cases | de Andrade et al. 2024 (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 3-4) | https://doi.org/10.1016/j.xhgg.2023.100242 | 2024-01 |
| Prevalence of P/LP germline TP53 variants, Geisinger | 1:3,790 | Genome-first cohort after excluding hematologic-cancer/confounded cases | de Andrade et al. 2024 (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 3-4) | https://doi.org/10.1016/j.xhgg.2023.100242 | 2024-01 |
| Prevalence of P/LP germline TP53 variants, PMBB | 1:2,983 | Genome-first cohort after excluding hematologic-cancer/confounded cases | de Andrade et al. 2024 (andrade2024genomefirstapproachof pages 2-3, andrade2024genomefirstapproachof pages 3-4) | https://doi.org/10.1016/j.xhgg.2023.100242 | 2024-01 |
| Whole-body MRI pooled cancer detection rate | 7% (95% CI 5–10) | 8 studies; 506 germline TP53 carriers | Temperley et al. 2024 (temperley2024wholebodymriscreening pages 11-13, temperley2024wholebodymriscreening pages 9-11) | https://doi.org/10.3390/jcm13051223 | 2024-02 |
| New cancers diagnosed on WB-MRI | 36/506 (7.1%) | Systematic review of germline TP53 carriers | Temperley et al. 2024 (temperley2024wholebodymriscreening pages 11-13) | https://doi.org/10.3390/jcm13051223 | 2024-02 |
| WB-MRI false-positive rate | 42.5% | Baseline WB-MRI screening performance in guideline summary | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 4-6) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| Brain MRI sensitivity | ~60% | Baseline brain MRI screening performance in TP53 carriers | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 4-6) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| Brain MRI specificity | ~80% | Baseline brain MRI screening performance in TP53 carriers | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 4-6) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| Brain MRI baseline detection range | 1.7%–8.6% | Baseline brain MRI screening yield | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 4-6) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| Brain MRI cumulative detection | 13.6% | Cumulative detection during surveillance | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 4-6) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| Toronto Protocol 5-year survival | 88% vs 59.6% | Surveillance cohort vs non-surveillance comparator | SEOM guideline 2023 (sanchezheras2023seomclinicalguideline pages 2-4) | https://doi.org/10.1007/s12094-023-03202-9 | 2023-05 |
| cfDNA multimodal PPV | 67.6% | Longitudinal multimodal cfDNA analysis in LFS | Wong et al. 2024 (wong2024earlycancerdetection pages 1-3) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |
| cfDNA multimodal NPV | 96.5% | Longitudinal multimodal cfDNA analysis in LFS | Wong et al. 2024 (wong2024earlycancerdetection pages 1-3) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |
| cfDNA PPV in clinically cancer-free TP53 carriers | 54.2% (26/48) | Cancer-free samples/individuals with cancer-associated cfDNA signal | Wong et al. 2024 (wong2024earlycancerdetection pages 8-9, wong2024earlycancerdetection pages 11-12) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |
| cfDNA NPV in clinically cancer-free TP53 carriers | 95.4% (41/43) | Cancer-free samples/individuals without cancer-associated cfDNA signal | Wong et al. 2024 (wong2024earlycancerdetection pages 8-9, wong2024earlycancerdetection pages 11-12) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |
| cfDNA false-positive rate, sample level | 18.3% (24/131) | Cancer-free plasma samples from TP53 carriers | Wong et al. 2024 (wong2024earlycancerdetection pages 8-9) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |
| cfDNA false-positive rate, individual level | 30.1% (22/73) | Cancer-free TP53 carriers | Wong et al. 2024 (wong2024earlycancerdetection pages 8-9, wong2024earlycancerdetection pages 11-12) | https://doi.org/10.1158/2159-8290.CD-23-0456 | 2024-10 |


*Table: This table compiles the main recent quantitative findings for Li-Fraumeni syndrome / heritable TP53-related cancer syndrome, including penetrance, prevalence, surveillance performance, and emerging liquid-biopsy metrics. It is useful as a quick reference for comparing risk estimates and screening yield across recent guidelines and studies.*

| Domain | Recommendation item | Age group | Modality/interval | Notes | Source with URL and publication date |
|---|---|---|---|---|---|
| Testing | Modified Chompret criterion: proband with an LFS core tumor before age 46 years **and** at least one first- or second-degree relative with an LFS core tumor before age 56 years or with multiple tumors | Any | Germline **TP53** testing indicated | Core tumors include breast cancer, soft-tissue sarcoma, osteosarcoma, CNS tumor, adrenocortical carcinoma; family history alone may miss de novo cases (sanchezheras2023seomclinicalguideline pages 2-4, frebourg2020guidelinesforthe pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Testing | Modified Chompret criterion: multiple primary tumors, two of which belong to the LFS core spectrum, with the first before age 46 years | Any | Germline **TP53** testing indicated | Applies even without strong family history; supports broadened hTP53rc concept (sanchezheras2023seomclinicalguideline pages 2-4, sanchezheras2023seomclinicalguideline pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Testing | Modified Chompret criterion: rare tumors strongly associated with TP53 (e.g., adrenocortical carcinoma, choroid plexus carcinoma, anaplastic embryonal rhabdomyosarcoma) regardless of family history | Pediatric/any | Germline **TP53** testing indicated | SEOM and ERN recommend testing for specific childhood tumors; ERN also highlights hypodiploid ALL, SHH medulloblastoma, jaw osteosarcoma (sanchezheras2023seomclinicalguideline pages 2-4, frebourg2020guidelinesforthe pages 4-5) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Testing | Modified Chompret criterion: very early-onset breast cancer | Adults (women) | Germline **TP53** testing for breast cancer diagnosed before age 31 years | Especially important because TP53 carriers may benefit from radiation-sparing management (sanchezheras2023seomclinicalguideline pages 2-4, frebourg2020guidelinesforthe pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Testing | Second primary malignancy arising in a prior radiotherapy field after a first core TP53 tumor before age 46 years | Any | Germline **TP53** testing should be considered | Reflects concern that radiotherapy contributes to subsequent primary tumors in TP53 carriers (sanchezheras2023seomclinicalguideline pages 2-4, frebourg2020guidelinesforthe pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Testing | Presymptomatic/cascade testing for relatives of a known carrier | Adults first-degree relatives; selected children | Offer predictive testing; in children, test from birth when variant is associated with childhood cancer risk | Childhood testing is not systematic for clearly low-childhood-risk variants; decisions may be case-by-case (sanchezheras2023seomclinicalguideline pages 2-4, frebourg2020guidelinesforthe pages 4-5) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Testing | Variant allele fraction (VAF) interpretation in blood | Any | If VAF ~40–50%, constitutional/germline more likely; if VAF 10–40%, confirm in non-lymphoid tissue | Helps distinguish germline/constitutional mosaicism from clonal hematopoiesis or circulating tumor DNA (sanchezheras2023seomclinicalguideline pages 2-4) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Testing | Timing of TP53 testing relative to cancer therapy | Any newly diagnosed cancer patient with suggestive phenotype | Test **before** treatment initiation when possible | Goal is to avoid radiotherapy and conventional genotoxic chemotherapy when feasible (frebourg2020guidelinesforthe pages 1-2, frebourg2020guidelinesforthe pages 3-4) | ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Start surveillance once carrier status is known and continue lifelong | Any confirmed carrier | Begin promptly; lifelong program | Applies to germline and constitutional mosaic TP53 pathogenic/likely pathogenic variants; some classic LFS families without identified TP53 variant may also undergo surveillance (sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Comprehensive physical examination | Children (birth–18 y) | Every 4–6 months | Typically coordinated by pediatric oncology/genetics team (sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Abdominal/pelvic ultrasound for ACC surveillance | Children (birth–18 y) | Every 3–6 months | ERN also recommends abdominal ultrasound every 6 months or 3–4 months depending on protocol; radiation-free modality preferred (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5, frebourg2020guidelinesforthe pages 3-4) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Endocrine/ACC laboratory surveillance | Children | Steroid hormone tests every 3–6 months when indicated; urine steroid monitoring probably every 6 months in ERN | Used because childhood ACC risk is clinically important; exact local protocol may vary (sanchezheras2023seomclinicalguideline pages 2-4, sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Brain MRI | Children | Annually from first year of life | First MRI with gadolinium; subsequent annual MRIs preferably without contrast; ERN suggests alternating with WBMRI so brain is imaged every 6 months in children (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5, frebourg2020guidelinesforthe pages 3-4) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Whole-body MRI (WBMRI) | Children | Annually | No ionizing radiation; usually performed without gadolinium in SEOM protocol; sedation may be needed in young children (sanchezheras2023seomclinicalguideline pages 4-6, kumamoto2021medicalguidelinesfor pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; LFS medical guideline 2021, https://doi.org/10.1007/s10147-021-02011-w, published 2021-10 |
| Surveillance | Complete blood count (CBC) | Children | Annually | Especially considered after leukemogenic therapy; no proven presymptomatic hematologic malignancy screening beyond this (sanchezheras2023seomclinicalguideline pages 2-4, sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Comprehensive physical examination | Adults | Every 6 months | Ideally coordinated by clinicians experienced in cancer genetics (sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Brain MRI | Adults | Annually until age 50 years | First MRI with gadolinium, then annual non-contrast MRI when possible (frebourg2020guidelinesforthe pages 1-2, sanchezheras2023seomclinicalguideline pages 4-6) | ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05; SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Whole-body MRI (WBMRI) | Adults | Annually | Central element of surveillance; avoids ionizing radiation; baseline detection about 7% in guideline summaries (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 3-4) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Clinical breast exam | Adult women | Every 6 months from age 20 years | Breast screening should minimize radiation exposure (sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Breast MRI | Adult women | Annually from age 20 to 75 years (SEOM); ERN 20–65 years | SEOM recommends alternating annual breast MRI with WBMRI at 6-month intervals; mammography generally avoided because of radiation sensitivity concerns (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Risk-reducing bilateral mastectomy discussion | Adult women | Individualized counseling | Mentioned as an option to reduce breast cancer risk and future need for radiotherapy (sanchezheras2023seomclinicalguideline pages 4-6, kumamoto2021medicalguidelinesfor pages 1-2) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; LFS medical guideline 2021, https://doi.org/10.1007/s10147-021-02011-w, published 2021-10 |
| Surveillance | Colonoscopy | Adults | Every 5 years from age 18 **if indicated** | Usually reserved for those with prior abdominal radiotherapy or relevant family history (sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 4-5) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05; ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05 |
| Surveillance | Complete blood count (CBC) | Adults | Annually | Especially after leukemogenic treatment exposure; evidence for routine hematologic cancer screening remains limited (sanchezheras2023seomclinicalguideline pages 2-4, sanchezheras2023seomclinicalguideline pages 4-6) | SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |
| Surveillance | Radiation avoidance principle | All carriers | Prefer MRI/ultrasound-based surveillance; minimize mammography, CT, and radiotherapy when alternatives exist | Important because TP53 carriers are at increased risk of treatment-related subsequent primary tumors (frebourg2020guidelinesforthe pages 1-2, sanchezheras2023seomclinicalguideline pages 4-6, frebourg2020guidelinesforthe pages 3-4) | ERN GENTURIS guideline 2020, https://doi.org/10.1038/s41431-020-0638-4, published 2020-05; SEOM guideline 2023, https://doi.org/10.1007/s12094-023-03202-9, published 2023-05 |


*Table: This table summarizes when to test for TP53 under modified Chompret and related criteria, and the main surveillance schedule for children and adults with heritable TP53-related cancer syndrome. It is useful as a guideline-oriented reference for diagnosis, cascade testing, and radiation-sparing surveillance planning.*

## Visual evidence (WB‑MRI study summary)
A per-study summary table of whole-body MRI studies and detection rates from the 2024 systematic review/meta-analysis is available for visual corroboration. (temperley2024wholebodymriscreening media bbec6272)

## Notes on gaps vs template requirements
- OMIM/Orphanet/ICD/MeSH identifiers, detailed tumor-type–specific incidence beyond the retrieved penetrance/surveillance metrics, and extensive real-world treatment outcome statistics were not present in the retrieved full texts and would require targeted database lookups and additional primary literature retrieval.
- Animal model details (specific allele tumor spectra, strain backgrounds, penetrance curves) are only partially supported by the retrieved sources and should be complemented with MGI/IMPC resources for full knowledge base completeness.


References

1. (giovino2024newparadigmsin pages 2-4): Camilla Giovino, Vallijah Subasri, Frank Telfer, and David Malkin. New paradigms in the clinical management of li-fraumeni syndrome. Cold Spring Harbor perspectives in medicine, 14:a041584, May 2024. URL: https://doi.org/10.1101/cshperspect.a041584, doi:10.1101/cshperspect.a041584. This article has 11 citations and is from a peer-reviewed journal.

2. (sanchezheras2023seomclinicalguideline pages 1-2): Ana Beatriz Sánchez-Heras, Teresa Ramon y Cajal, Marta Pineda, Elena Aguirre, Begoña Graña, Isabel Chirivella, Judit Balmaña, and Joan Brunet. Seom clinical guideline on heritable tp53-related cancer syndrome (2022). Clinical & Translational Oncology, 25:2627-2633, May 2023. URL: https://doi.org/10.1007/s12094-023-03202-9, doi:10.1007/s12094-023-03202-9. This article has 13 citations and is from a peer-reviewed journal.

3. (frebourg2020guidelinesforthe pages 1-2): T. Frébourg, Svetlana Bajalica Lagercrantz, Carla Oliveira, R. Mágenheim, D. Evans, Nicoline Marjolijn Marleen Rianne Rolf Gareth Emma Marc Eam Hoogerbrugge Ligtenberg Kets Oostenbrink Sijmons E, N. Hoogerbrugge, M. Ligtenberg, M. Kets, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, M. Tischkowitz, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frébourg, C. Houdayer, C. Colas, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, R. de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, H. S. Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Guidelines for the li–fraumeni and heritable tp53-related cancer syndromes. European Journal of Human Genetics, 28:1379-1386, May 2020. URL: https://doi.org/10.1038/s41431-020-0638-4, doi:10.1038/s41431-020-0638-4. This article has 372 citations and is from a domain leading peer-reviewed journal.

4. (hosseini2024currentinsightsand pages 1-4): Mohammad-Salar Hosseini. Current insights and future directions of li-fraumeni syndrome. Discover Oncology, Oct 2024. URL: https://doi.org/10.1007/s12672-024-01435-w, doi:10.1007/s12672-024-01435-w. This article has 21 citations.

5. (fortuno2024cancerrisksassociated pages 1-2): Cristina Fortuno, Bing-Jian Feng, Courtney Carroll, Giovanni Innella, Wendy Kohlmann, Conxi Lázaro, Joan Brunet, Lidia Feliubadaló, Silvia Iglesias, Mireia Menéndez, Alex Teulé, Mandy L. Ballinger, David M. Thomas, Ainsley Campbell, Mike Field, Marion Harris, Judy Kirk, Nicholas Pachter, Nicola Poplawski, Rachel Susman, Kathy Tucker, Mathew Wallis, Rachel Williams, Elisa Cops, David Goldgar, Paul A. James, Amanda B. Spurdle, David Amor, Lesley Andrews, Yoland Antill, Rosemary Balleine, Jonathan Beesley, Ian Bennett, Michael Bogwitz, Simon Bodek, Leon Botes, Meagan Brennan, Melissa Brown, Michael Buckley, Jo Burke, Phyllis Butow, Liz Caldon, Ian Campbell, Michelle Cao, Anannya Chakrabarti, Deepa Chauhan, Manisha Chauhan, Georgia Chenevix-Trench, Alice Christian, Paul Cohen, Alison Colley, Ashley Crook, James Cui, Eliza Courtney, Margaret Cummings, Sarah-Jane Dawson, Anna deFazio, Martin Delatycki, Rebecca Dickson, Joanne Dixon, Ted Edkins, Stacey Edwards, Gelareh Farshid, Andrew Fellows, Georgina Fenton, Michael Field, James Flanagan, Peter Fong, Laura Forrest, Stephen Fox, Juliet French, Michael Friedlander, Clara Gaff, Mike Gattas, Peter George, Sian Greening, Marion Harris, Stewart Hart, Nick Hayward, John Hopper, Cass Hoskins, Clare Hunt, Paul James, Mark Jenkins, Alexa Kidd, Judy Kirk, Jessica Koehler, James Kollias, Sunil Lakhani, Mitchell Lawrence, Jason Lee, Shuai Li, Geoff Lindeman, Jocelyn Lippey, Lara Lipton, Liz Lobb, Sherene Loi, Graham Mann, Deborah Marsh, Sue Anne McLachlan, Bettina Meiser, Roger Milne, Sophie Nightingale, Shona O'Connell, Sarah O'Sullivan, David Gallego Ortega, Nick Pachter, Jia-Min Pang, Gargi Pathak, Briony Patterson, Amy Pearn, Kelly Phillips, Ellen Pieper, Susan Ramus, Edwina Rickard, Bridget Robinson, Mona Saleh, Anita Skandarajah, Elizabeth Salisbury, Christobel Saunders, Jodi Saunus, Peter Savas, Rodney Scott, Clare Scott, Adrienne Sexton, Joanne Shaw, Andrew Shelling, Shweta Srinivasa, Peter Simpson, Melissa Southey, Amanda Spurdle, Jessica Taylor, Renea Taylor, Heather Thorne, Alison Trainer, Kathy Tucker, Jane Visvader, Logan Walker, Rachael Williams, Ingrid Winship, Mary Ann Young, and Milita Zaheed. Cancer risks associated with tp53 pathogenic variants: maximum likelihood analysis of extended pedigrees for diagnosis of first cancers beyond the li-fraumeni syndrome spectrum. JCO Precision Oncology, Feb 2024. URL: https://doi.org/10.1200/po.23.00453, doi:10.1200/po.23.00453. This article has 30 citations and is from a peer-reviewed journal.

6. (temperley2024wholebodymriscreening pages 11-13): Hugo C. Temperley, Niall J. O’Sullivan, Benjamin M. Mac Curtain, Wanyang Qian, Tatiana S. Temperley, Alannah Murray, Alison Corr, Ian Brennan, David Gallagher, James F. Meaney, and Michael E. Kelly. Whole-body mri screening for carriers of germline tp53 mutations—a systematic review and meta-analysis. Journal of Clinical Medicine, 13:1223, Feb 2024. URL: https://doi.org/10.3390/jcm13051223, doi:10.3390/jcm13051223. This article has 5 citations.

7. (wong2024earlycancerdetection pages 1-3): Derek Wong, Ping Luo, Leslie E. Oldfield, Haifan Gong, Ledia Brunga, Ron Rabinowicz, Vallijah Subasri, Clarissa Chan, Tiana Downs, Kirsten M. Farncombe, Beatrice Luu, Maia Norman, Julia A. Sobotka, Precious Uju, Jenna Eagles, Stephanie Pedersen, Johanna Wellum, Arnavaz Danesh, Stephenie D. Prokopec, Eric Y. Stutheit-Zhao, Nadia Znassi, Lawrence E. Heisler, Richard Jovelin, Bernard Lam, Beatriz E. Lujan Toro, Kayla Marsh, Yogi Sundaravadanam, Dax Torti, Carina Man, Anna Goldenberg, Wei Xu, Patrick Veit-Haibach, Andrea S. Doria, David Malkin, Raymond H. Kim, and Trevor J. Pugh. Early cancer detection in li–fraumeni syndrome with cell-free dna. Cancer Discovery, 14:104-119, Oct 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0456, doi:10.1158/2159-8290.cd-23-0456. This article has 57 citations and is from a highest quality peer-reviewed journal.

8. (andrade2024genomefirstapproachof pages 2-3): Kelvin C. de Andrade, Natasha T. Strande, Jung Kim, Jeremy S. Haley, Jessica N. Hatton, Megan N. Frone, Payal P. Khincha, Gretchen M. Thone, Uyenlinh L. Mirshahi, Cynthia Schneider, Heena Desai, James T. Dove, Diane T. Smelser, Arnold J. Levine, Kara N. Maxwell, Douglas R. Stewart, David J. Carey, and Sharon A. Savage. Genome-first approach of the prevalence and cancer phenotypes of pathogenic or likely pathogenic germline tp53 variants. Human Genetics and Genomics Advances, 5:100242, Jan 2024. URL: https://doi.org/10.1016/j.xhgg.2023.100242, doi:10.1016/j.xhgg.2023.100242. This article has 28 citations and is from a peer-reviewed journal.

9. (dixonzegeye2024cancerprecisionpreventiontrial pages 1-2): Miriam Dixon-Zegeye, Rachel Shaw, Linda Collins, Kendra Perez-Smith, Alexander Ooms, Maggie Qiao, Pan Pantziarka, Louise Izatt, Marc Tischkowitz, Rachel E. Harrison, Angela George, Emma R. Woodward, Simon Lord, Lara Hawkes, D. Gareth Evans, James Franklin, Helen Hanson, and Sarah P. Blagden. Cancer precision-prevention trial of metformin in adults with li fraumeni syndrome (mili) undergoing yearly mri surveillance: a randomised controlled trial protocol. Trials, Feb 2024. URL: https://doi.org/10.1186/s13063-024-07929-w, doi:10.1186/s13063-024-07929-w. This article has 19 citations and is from a peer-reviewed journal.

10. (light2023germlinetp53mutations pages 6-7): Nicholas Light, Mehdi Layeghifard, Ayush Attery, Vallijah Subasri, Matthew Zatzman, Nathaniel D Anderson, Rupal Hatkar, Sasha Blay, David Chen, Ana Novokmet, Fabio Fuligni, James Tran, Richard De Borja, Himanshi Agarwal, Larissa Waldman, Lisa M Abegglen, Daniel Albertson, Jonathan L Finlay, Jordan R Hansford, Sam Behjati, Anita Villani, Moritz Gerstung, Ludmil B Alexandrov, Gino R Somers, Joshua D Schiffman, Varda Rotter, David Malkin, and Adam Shlien. Germline tp53 mutations undergo copy number gain years prior to tumor diagnosis. JournalArticle, Feb 2023. URL: https://doi.org/10.17863/cam.93707, doi:10.17863/cam.93707. This article has 42 citations.

11. (gargallo2020li–fraumenisyndromeheterogeneity pages 2-4): P. Gargallo, Y. Yáñez, V. Segura, A. Juan, B. Torres, J. Balaguer, S. Oltra, V. Castel, and A. Cañete. Li–fraumeni syndrome heterogeneity. Clinical and Translational Oncology, 22:978-988, Nov 2020. URL: https://doi.org/10.1007/s12094-019-02236-2, doi:10.1007/s12094-019-02236-2. This article has 51 citations and is from a peer-reviewed journal.

12. (gargallo2020li–fraumenisyndromeheterogeneity pages 7-8): P. Gargallo, Y. Yáñez, V. Segura, A. Juan, B. Torres, J. Balaguer, S. Oltra, V. Castel, and A. Cañete. Li–fraumeni syndrome heterogeneity. Clinical and Translational Oncology, 22:978-988, Nov 2020. URL: https://doi.org/10.1007/s12094-019-02236-2, doi:10.1007/s12094-019-02236-2. This article has 51 citations and is from a peer-reviewed journal.

13. (frebourg2020guidelinesforthe pages 4-5): T. Frébourg, Svetlana Bajalica Lagercrantz, Carla Oliveira, R. Mágenheim, D. Evans, Nicoline Marjolijn Marleen Rianne Rolf Gareth Emma Marc Eam Hoogerbrugge Ligtenberg Kets Oostenbrink Sijmons E, N. Hoogerbrugge, M. Ligtenberg, M. Kets, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, M. Tischkowitz, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frébourg, C. Houdayer, C. Colas, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, R. de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, H. S. Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Guidelines for the li–fraumeni and heritable tp53-related cancer syndromes. European Journal of Human Genetics, 28:1379-1386, May 2020. URL: https://doi.org/10.1038/s41431-020-0638-4, doi:10.1038/s41431-020-0638-4. This article has 372 citations and is from a domain leading peer-reviewed journal.

14. (sanchezheras2023seomclinicalguideline pages 2-4): Ana Beatriz Sánchez-Heras, Teresa Ramon y Cajal, Marta Pineda, Elena Aguirre, Begoña Graña, Isabel Chirivella, Judit Balmaña, and Joan Brunet. Seom clinical guideline on heritable tp53-related cancer syndrome (2022). Clinical & Translational Oncology, 25:2627-2633, May 2023. URL: https://doi.org/10.1007/s12094-023-03202-9, doi:10.1007/s12094-023-03202-9. This article has 13 citations and is from a peer-reviewed journal.

15. (kumamoto2021medicalguidelinesfor pages 1-2): Tadashi Kumamoto, Fumito Yamazaki, Yoshiko Nakano, Chieko Tamura, Shimon Tashiro, Hiroyoshi Hattori, Akira Nakagawara, and Yukiko Tsunematsu. Medical guidelines for li–fraumeni syndrome 2019, version 1.1. International Journal of Clinical Oncology, 26:2161-2178, Oct 2021. URL: https://doi.org/10.1007/s10147-021-02011-w, doi:10.1007/s10147-021-02011-w. This article has 87 citations and is from a peer-reviewed journal.

16. (andrade2024genomefirstapproachof pages 3-4): Kelvin C. de Andrade, Natasha T. Strande, Jung Kim, Jeremy S. Haley, Jessica N. Hatton, Megan N. Frone, Payal P. Khincha, Gretchen M. Thone, Uyenlinh L. Mirshahi, Cynthia Schneider, Heena Desai, James T. Dove, Diane T. Smelser, Arnold J. Levine, Kara N. Maxwell, Douglas R. Stewart, David J. Carey, and Sharon A. Savage. Genome-first approach of the prevalence and cancer phenotypes of pathogenic or likely pathogenic germline tp53 variants. Human Genetics and Genomics Advances, 5:100242, Jan 2024. URL: https://doi.org/10.1016/j.xhgg.2023.100242, doi:10.1016/j.xhgg.2023.100242. This article has 28 citations and is from a peer-reviewed journal.

17. (sanchezheras2023seomclinicalguideline pages 4-6): Ana Beatriz Sánchez-Heras, Teresa Ramon y Cajal, Marta Pineda, Elena Aguirre, Begoña Graña, Isabel Chirivella, Judit Balmaña, and Joan Brunet. Seom clinical guideline on heritable tp53-related cancer syndrome (2022). Clinical & Translational Oncology, 25:2627-2633, May 2023. URL: https://doi.org/10.1007/s12094-023-03202-9, doi:10.1007/s12094-023-03202-9. This article has 13 citations and is from a peer-reviewed journal.

18. (vanikova2024functionalanalysisof pages 67-70): L Vaníková. Functional analysis of selected variants of uncertain significance in cancer predisposing genes. Unknown journal, 2024.

19. (light2023germlinetp53mutations pages 1-2): Nicholas Light, Mehdi Layeghifard, Ayush Attery, Vallijah Subasri, Matthew Zatzman, Nathaniel D Anderson, Rupal Hatkar, Sasha Blay, David Chen, Ana Novokmet, Fabio Fuligni, James Tran, Richard De Borja, Himanshi Agarwal, Larissa Waldman, Lisa M Abegglen, Daniel Albertson, Jonathan L Finlay, Jordan R Hansford, Sam Behjati, Anita Villani, Moritz Gerstung, Ludmil B Alexandrov, Gino R Somers, Joshua D Schiffman, Varda Rotter, David Malkin, and Adam Shlien. Germline tp53 mutations undergo copy number gain years prior to tumor diagnosis. JournalArticle, Feb 2023. URL: https://doi.org/10.17863/cam.93707, doi:10.17863/cam.93707. This article has 42 citations.

20. (andrade2024genomefirstapproachof pages 6-7): Kelvin C. de Andrade, Natasha T. Strande, Jung Kim, Jeremy S. Haley, Jessica N. Hatton, Megan N. Frone, Payal P. Khincha, Gretchen M. Thone, Uyenlinh L. Mirshahi, Cynthia Schneider, Heena Desai, James T. Dove, Diane T. Smelser, Arnold J. Levine, Kara N. Maxwell, Douglas R. Stewart, David J. Carey, and Sharon A. Savage. Genome-first approach of the prevalence and cancer phenotypes of pathogenic or likely pathogenic germline tp53 variants. Human Genetics and Genomics Advances, 5:100242, Jan 2024. URL: https://doi.org/10.1016/j.xhgg.2023.100242, doi:10.1016/j.xhgg.2023.100242. This article has 28 citations and is from a peer-reviewed journal.

21. (temperley2024wholebodymriscreening pages 9-11): Hugo C. Temperley, Niall J. O’Sullivan, Benjamin M. Mac Curtain, Wanyang Qian, Tatiana S. Temperley, Alannah Murray, Alison Corr, Ian Brennan, David Gallagher, James F. Meaney, and Michael E. Kelly. Whole-body mri screening for carriers of germline tp53 mutations—a systematic review and meta-analysis. Journal of Clinical Medicine, 13:1223, Feb 2024. URL: https://doi.org/10.3390/jcm13051223, doi:10.3390/jcm13051223. This article has 5 citations.

22. (wong2024earlycancerdetection pages 9-11): Derek Wong, Ping Luo, Leslie E. Oldfield, Haifan Gong, Ledia Brunga, Ron Rabinowicz, Vallijah Subasri, Clarissa Chan, Tiana Downs, Kirsten M. Farncombe, Beatrice Luu, Maia Norman, Julia A. Sobotka, Precious Uju, Jenna Eagles, Stephanie Pedersen, Johanna Wellum, Arnavaz Danesh, Stephenie D. Prokopec, Eric Y. Stutheit-Zhao, Nadia Znassi, Lawrence E. Heisler, Richard Jovelin, Bernard Lam, Beatriz E. Lujan Toro, Kayla Marsh, Yogi Sundaravadanam, Dax Torti, Carina Man, Anna Goldenberg, Wei Xu, Patrick Veit-Haibach, Andrea S. Doria, David Malkin, Raymond H. Kim, and Trevor J. Pugh. Early cancer detection in li–fraumeni syndrome with cell-free dna. Cancer Discovery, 14:104-119, Oct 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0456, doi:10.1158/2159-8290.cd-23-0456. This article has 57 citations and is from a highest quality peer-reviewed journal.

23. (wong2024earlycancerdetection pages 8-9): Derek Wong, Ping Luo, Leslie E. Oldfield, Haifan Gong, Ledia Brunga, Ron Rabinowicz, Vallijah Subasri, Clarissa Chan, Tiana Downs, Kirsten M. Farncombe, Beatrice Luu, Maia Norman, Julia A. Sobotka, Precious Uju, Jenna Eagles, Stephanie Pedersen, Johanna Wellum, Arnavaz Danesh, Stephenie D. Prokopec, Eric Y. Stutheit-Zhao, Nadia Znassi, Lawrence E. Heisler, Richard Jovelin, Bernard Lam, Beatriz E. Lujan Toro, Kayla Marsh, Yogi Sundaravadanam, Dax Torti, Carina Man, Anna Goldenberg, Wei Xu, Patrick Veit-Haibach, Andrea S. Doria, David Malkin, Raymond H. Kim, and Trevor J. Pugh. Early cancer detection in li–fraumeni syndrome with cell-free dna. Cancer Discovery, 14:104-119, Oct 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0456, doi:10.1158/2159-8290.cd-23-0456. This article has 57 citations and is from a highest quality peer-reviewed journal.

24. (NCT01737255 chunk 1):  Magnetic Resonance Imaging Screening in Li Fraumeni Syndrome. Institute of Cancer Research, United Kingdom. 2012. ClinicalTrials.gov Identifier: NCT01737255

25. (NCT02950987 chunk 1): Allison O'Neill, MD. Screening With Whole Body MRI For Detection Of Primary Tumors In Children And Adults With Li-Fraumeni Syndrome (LFS) And Other Cancer Predisposition Syndromes. Dana-Farber Cancer Institute. 2012. ClinicalTrials.gov Identifier: NCT02950987

26. (NCT03176836 chunk 1): Andrea Doria. Li-Fraumeni Syndrome Imaging Study. The Hospital for Sick Children. 2016. ClinicalTrials.gov Identifier: NCT03176836

27. (NCT04367246 chunk 1): Kara Maxwell. Li-Fraumeni Syndrome/TP53 Biobank. Abramson Cancer Center at Penn Medicine. 2019. ClinicalTrials.gov Identifier: NCT04367246

28. (levine2021spontaneousandinherited pages 1-2): Arnold J. Levine. Spontaneous and inherited tp53 genetic alterations. Oncogene, 40:5975-5983, Aug 2021. URL: https://doi.org/10.1038/s41388-021-01991-3, doi:10.1038/s41388-021-01991-3. This article has 69 citations and is from a domain leading peer-reviewed journal.

29. (wong2024earlycancerdetection pages 11-12): Derek Wong, Ping Luo, Leslie E. Oldfield, Haifan Gong, Ledia Brunga, Ron Rabinowicz, Vallijah Subasri, Clarissa Chan, Tiana Downs, Kirsten M. Farncombe, Beatrice Luu, Maia Norman, Julia A. Sobotka, Precious Uju, Jenna Eagles, Stephanie Pedersen, Johanna Wellum, Arnavaz Danesh, Stephenie D. Prokopec, Eric Y. Stutheit-Zhao, Nadia Znassi, Lawrence E. Heisler, Richard Jovelin, Bernard Lam, Beatriz E. Lujan Toro, Kayla Marsh, Yogi Sundaravadanam, Dax Torti, Carina Man, Anna Goldenberg, Wei Xu, Patrick Veit-Haibach, Andrea S. Doria, David Malkin, Raymond H. Kim, and Trevor J. Pugh. Early cancer detection in li–fraumeni syndrome with cell-free dna. Cancer Discovery, 14:104-119, Oct 2024. URL: https://doi.org/10.1158/2159-8290.cd-23-0456, doi:10.1158/2159-8290.cd-23-0456. This article has 57 citations and is from a highest quality peer-reviewed journal.

30. (frebourg2020guidelinesforthe pages 3-4): T. Frébourg, Svetlana Bajalica Lagercrantz, Carla Oliveira, R. Mágenheim, D. Evans, Nicoline Marjolijn Marleen Rianne Rolf Gareth Emma Marc Eam Hoogerbrugge Ligtenberg Kets Oostenbrink Sijmons E, N. Hoogerbrugge, M. Ligtenberg, M. Kets, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, M. Tischkowitz, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frébourg, C. Houdayer, C. Colas, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, R. de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, H. S. Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Guidelines for the li–fraumeni and heritable tp53-related cancer syndromes. European Journal of Human Genetics, 28:1379-1386, May 2020. URL: https://doi.org/10.1038/s41431-020-0638-4, doi:10.1038/s41431-020-0638-4. This article has 372 citations and is from a domain leading peer-reviewed journal.

31. (temperley2024wholebodymriscreening media bbec6272): Hugo C. Temperley, Niall J. O’Sullivan, Benjamin M. Mac Curtain, Wanyang Qian, Tatiana S. Temperley, Alannah Murray, Alison Corr, Ian Brennan, David Gallagher, James F. Meaney, and Michael E. Kelly. Whole-body mri screening for carriers of germline tp53 mutations—a systematic review and meta-analysis. Journal of Clinical Medicine, 13:1223, Feb 2024. URL: https://doi.org/10.3390/jcm13051223, doi:10.3390/jcm13051223. This article has 5 citations.