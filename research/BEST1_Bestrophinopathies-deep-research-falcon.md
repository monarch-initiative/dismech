---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:52.905969'
end_time: '2026-04-04T12:54:36.533958'
duration_seconds: 703.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BEST1 Bestrophinopathies
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BEST1 Bestrophinopathies
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **BEST1 Bestrophinopathies** covering all of the
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
- **Disease Name:** BEST1 Bestrophinopathies
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **BEST1 Bestrophinopathies** covering all of the
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


## Comprehensive Research Report: BEST1 Bestrophinopathies (Genetic)

### Scope and evidence base
This report synthesizes recent peer‑reviewed literature (prioritizing 2023–2024) and ClinicalTrials.gov records on **BEST1 bestrophinopathies**—a spectrum of inherited retinal diseases caused by pathogenic variants in **BEST1** encoding bestrophin‑1. Where the provided evidence does not contain certain identifiers (e.g., MONDO/Orphanet/ICD/MeSH codes), this is stated explicitly.

| Subtype | Core disease label / identifiers | Typical inheritance | Typical onset / epidemiology | Key fundus / OCT / FAF hallmarks | Electrophysiology | Representative variants / findings |
|---|---|---|---|---|---|---|
| BVMD / Best disease | Best vitelliform macular dystrophy; MIM #153700 | Usually autosomal dominant; reduced penetrance reported; rare recessive BVMD-like presentations also described | Median onset about 19 years, range 4–65; reported prevalence estimates vary by region: ~1/10,000 (USA), 2/10,000 (Sweden), 1/20,000 (Minnesota), 1.5/100,000 (Denmark); Israeli estimate 1 in 127,000 overall | Classic central yellow “egg-yolk” vitelliform lesion; Gass stages from previtelliform to atrophic/cicatricial; OCT shows interdigitation zone changes early, then dome-shaped subretinal hyperreflective lesion, later vitelliruptive change and atrophy; FAF usually hyperautofluorescent in vitelliform stage; OCTA shows late macular neovascularization, often non-exudative | EOG typically abnormal with reduced Arden ratio (often ≤1.5), but can be normal in a minority; ffERG usually normal or mildly reduced | BEST1 dominant missense variants enriched in conserved transmembrane / intracellular Ca2+-binding regions; recurrent dominant LOF mutants studied for rescue include A10T, R218H, L234P, A243T, Q293K, D302A; visual prognosis variable, with ~75% of patients <40 years retaining ≥20/40 in at least one eye (bianco2024multimodalimagingin pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, amato2023genetherapyin pages 2-3, owji2024neurotransmitterboundbestrophinchannel pages 5-6) |
| ARB | Autosomal recessive bestrophinopathy; MIM #611809 | Autosomal recessive, usually biallelic BEST1 variants | Mean onset 30.53 years in one 2024 Chinese cohort (range 9–68); earlier onset also reported, including childhood; Chinese WGS cohort mean age at last exam 28.0 ± 13.8 years | Multiple bilateral small round yellow vitelliform deposits across posterior pole/peripapillary region; OCT commonly shows subretinal fluid, intraretinal cystic/schitic spaces, elongated photoreceptor outer segments, retinoschisis, outer-segment loss; FAF often diffuse/punctate hyperautofluorescence; anterior segment may show shallow AC, short axial length, narrow angles, iris bombe | EOG usually severely reduced, but can be normal/slightly reduced in some cases; ffERG may be reduced more often than in BVMD | 2024 Chinese cohort: 15 distinct variants, 82.35% missense; recurrent p.Arg255-256 and p.Ala195Val each 23.68%; 2023 Chinese WGS cohort found founder deep intronic c.867+97G>A (~16% of alleles), plus c.867+97G>T and c.1101-491A>G causing aberrant splicing / PTCs; common coding alleles included p.Arg255Trp (12.8%), p.Tyr44His (5.6%), p.Ala195Val (5.6%); frequent misdiagnoses include angle-closure glaucoma, Best disease, and CSC with CNV (zhao2024clinicalandgenetic pages 1-2, shi2023comprehensivegeneticanalysis pages 5-8, shi2023comprehensivegeneticanalysis pages 1-2) |
| Recessive BVMD-like BEST1 disease | BVMD phenotype secondary to biallelic BEST1 variants | Autosomal recessive | Childhood to young adulthood reported; examples include presentations at 11–12 years and symptoms from age 16; one case stable over 14 years | Imaging can be indistinguishable from classic BVMD: vitelliform / vitelliruptive macular lesions, optically empty subretinal space, hyperreflective subfoveal material, peripheral hyperautofluorescence, central hypoautofluorescence, outer retinal thinning | ERG and PERG can remain normal; EOG is variable, from normal/borderline to absent light rise | Homozygous p.Arg47Cys and p.Asn179del reported in 2024 series; heterozygous carrier parents may be phenotypically normal, underscoring counseling implications (dhoble2024typicalbestvitelliform pages 1-7, dhoble2024typicalbestvitelliform pages 7-11) |
| ADVIRC | Autosomal dominant vitreoretinochoroidopathy; MIM #193220 | Autosomal dominant | Usually developmental / early-life ocular anomaly spectrum with progressive degeneration; exact onset statistics not well defined in gathered recent sources | Peripheral vitreoretinal/chorioretinal degeneration with developmental ocular anomalies; part of BEST1 phenotypic spectrum rather than isolated macular vitelliform disease | EOG often reported as abnormal across BEST1 spectrum, but detailed subtype-specific recent electrophysiology was limited in gathered sources | Included among BEST1-associated phenotypes; recent gathered evidence emphasized spectrum classification more than subtype-specific variant frequencies (bianco2024multimodalimagingin pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, amato2023genetherapyin pages 2-3) |
| AOFVD / AVMD linked to BEST1 | Adult-onset foveomacular / vitelliform macular dystrophy; OMIM #608161 | Often treated as part of dominant BEST1 spectrum when a pathogenic BEST1 variant is identified | Typically presents in 4th–5th decade; some reviews state BEST1-positive AVMD cases are generally reclassified as BVMD | Smaller adult-onset vitelliform macular lesions; can resemble Best disease clinically, so multimodal imaging and genetics are important for distinction | EOG may be normal to subnormal, unlike classic BVMD where marked reduction is commoner | Gathered evidence supports reclassification of BEST1-positive adult-onset vitelliform cases into the BVMD/BEST1 spectrum; no specific recurrent variant dominated the recent evidence retrieved (bianco2024multimodalimagingin pages 1-2, zhao2024clinicalandgenetic pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2, makati2014electrooculographyandoptical pages 3-4) |


*Table: This table organizes the main BEST1-associated bestrophinopathy subtypes by inheritance, onset, hallmark imaging/electrophysiology, and representative variants or cohort findings. It is useful as a compact reference for phenotype-genotype comparison across the BEST1 disease spectrum.*

---

## 1. Disease Information

### 1.1 What is the disease?
**BEST1 bestrophinopathies** are a group of autosomal dominant and autosomal recessive **inherited retinal diseases (IRDs)** caused by pathogenic variants in **BEST1**, most prominently manifesting as **Best vitelliform macular dystrophy (BVMD; “Best disease”)** and **autosomal recessive bestrophinopathy (ARB)**, but also including **ADVIRC**, **adult-onset vitelliform phenotypes**, and BEST1‑associated **retinitis pigmentosa**. These conditions share a central theme of **retinal pigment epithelium (RPE) dysfunction** with characteristic subretinal material (vitelliform deposits and/or fluid) and frequent electro‑oculogram (EOG) abnormalities. (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3)

**Concise overview (current understanding):** BEST1 dysfunction perturbs RPE ion/fluid homeostasis and calcium‑regulated physiology; clinically this produces vitelliform lesions, subretinal/intraretinal fluid, abnormal EOG light rise, and progressive macular/retinal degeneration with variable severity and inheritance. (amato2023genetherapyin pages 1-2, khan2018normalelectrooculographyin pages 9-13)

### 1.2 Key identifiers (as available in evidence)
The retrieved evidence explicitly provides the following **MIM/OMIM identifiers**:
- **BVMD / Best disease:** **MIM #153700** (bianco2024multimodalimagingin pages 1-2)
- **BEST1 gene:** **MIM #607854** (bianco2024multimodalimagingin pages 1-2)
- **Autosomal recessive bestrophinopathy (ARB):** **OMIM 611809** (zhao2024clinicalandgenetic pages 1-2)
- **ADVIRC:** **MIM #193220** (bianco2024multimodalimagingin pages 1-2)
- **BEST1-associated retinitis pigmentosa:** **MIM #613194** (bianco2024multimodalimagingin pages 1-2)
- **Adult-onset vitelliform macular degeneration:** **OMIM 608161** (zhao2024clinicalandgenetic pages 1-2)

**MONDO / Orphanet / ICD‑10/ICD‑11 / MeSH:** Not available in the retrieved text evidence set; therefore, specific IDs cannot be asserted here without adding new database retrieval. (No relevant evidence found in provided corpus)

### 1.3 Synonyms and alternative names
- **BVMD**: “Best disease”, “Best vitelliform macular dystrophy” (beryozkin2024bestdiseaseglobal pages 1-2)
- **AOFVD/AVMD**: “adult‑onset foveomacular vitelliform dystrophy”, “adult vitelliform macular dystrophy/degeneration” (amato2023genetherapyin pages 2-3, zhao2024clinicalandgenetic pages 1-2)
- **ARB**: “autosomal recessive bestrophinopathy” (zhao2024clinicalandgenetic pages 1-2)
- **BEST1** has historical alias **VMD2** in some literature (khan2018normalelectrooculographyin pages 9-13)

### 1.4 Evidence source type
Information summarized here is derived from:
- **Aggregated disease-level resources** in the form of cohort studies and reviews (e.g., imaging review, prevalence analysis) (bianco2024multimodalimagingin pages 1-2, beryozkin2024bestdiseaseglobal pages 1-2)
- **Primary human cohort/case series studies** (e.g., ARB cohorts in China; BVMD/ARB clinical series) (zhao2024clinicalandgenetic pages 1-2, shi2023comprehensivegeneticanalysis pages 5-8)
- **Preclinical animal and in vitro models** (canine models; iPSC‑RPE) (amato2023genetherapyin pages 6-7, khan2018normalelectrooculographyin pages 9-13)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in **BEST1**. The BEST1 gene encodes **bestrophin‑1**, a homopentameric Ca2+-activated anion (chloride) channel expressed in RPE, and BEST1 pathogenic variants cause a phenotypic spectrum collectively termed “bestrophinopathies.” (amato2023genetherapyin pages 1-2, amato2023genetherapyin pages 2-3)

### 2.2 Risk factors
#### Genetic risk factors
- **Causal variants:** Numerous pathogenic variants across BEST1 (missense predominating overall; truncating variants enriched in ARB), including coding variants (e.g., p.Arg255Trp, p.Ala195Val) and noncoding deep intronic variants affecting splicing (e.g., c.867+97G>A). (shi2023comprehensivegeneticanalysis pages 1-2, zhao2024clinicalandgenetic pages 1-2)
- **Founder effects:** In a large Chinese ARB cohort, deep intronic variant **c.867+97G>A** was identified as a founder variant accounting for ~**16%** of alleles/heritability in that cohort. (shi2023comprehensivegeneticanalysis pages 2-2, shi2023comprehensivegeneticanalysis pages 5-8)

#### Environmental/lifestyle risk factors
The retrieved evidence does not provide robust epidemiologic environmental risk factors (e.g., smoking/diet/exposures). The conditions are primarily genetic with variable expressivity; modifiers are suspected but not quantified here. (khan2018normalelectrooculographyin pages 9-13)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence corpus.

### 2.4 Gene–environment interactions
The retrieved evidence supports the concept that phenotype is variable and may involve modifiers, but does not provide a specific, validated gene–environment interaction. (khan2018normalelectrooculographyin pages 9-13)

---

## 3. Phenotypes

### 3.1 Major phenotype domains (with suggested HPO terms)
Below are common clinical phenotypes across the BEST1 spectrum. HPO term suggestions are provided as likely mappings.

1. **Vitelliform subretinal lesions / deposits** (fundus “egg‑yolk” lesion; multifocal yellow deposits)
   - Evidence: classic BVMD “egg‑yolk” lesion; ARB multifocal deposits throughout posterior pole/peripapillary region. (beryozkin2024bestdiseaseglobal pages 1-2, zhao2024clinicalandgenetic pages 1-2)
   - Suggested HPO: **Vitelliform macular dystrophy (HP:0007757)**; **Macular lesion (HP:0001103)**; **Retinal flecks (HP:0001086)**

2. **Subretinal fluid and intraretinal cystic/schitic spaces (especially ARB)**
   - Evidence: ARB OCT findings include subretinal fluid and intraretinal cystic/schitic spaces; changes may fluctuate longitudinally. (shakeel2024phenotypeandgenetic pages 2-3, cideciyan2023photoreceptorfunctionand pages 6-8)
   - Suggested HPO: **Subretinal fluid (HP:0031889)**; **Cystoid macular edema (HP:0000605)**; **Retinoschisis (HP:0000579)**

3. **Abnormal electro‑oculogram (EOG) Arden ratio / reduced light peak**
   - Evidence: EOG abnormality is a hallmark in BVMD/ARB; however normal EOG can occur in a minority (e.g., Arden ratio >1.65 in 8% in one large series). (amato2023genetherapyin pages 2-3)
   - Suggested HPO: **Abnormal electrooculogram (HP:0025206)** (term may vary by HPO release)

4. **Visual acuity impairment / central vision loss**
   - Evidence: BVMD can progress from normal fundus to lesion disruption and atrophy with visual decline; ARB can range broadly in acuity. (beryozkin2024bestdiseaseglobal pages 1-2, zhao2024clinicalandgenetic pages 1-2)
   - Suggested HPO: **Reduced visual acuity (HP:0007663)**; **Central scotoma (HP:0000603)**

5. **Macular neovascularization / choroidal neovascularization (CNV/CNVM)**
   - Evidence: OCTA detects CNVs in many BVMD eyes; nonexudative CNVs are often reported. Real-world anti‑VEGF treatment for CNV is described in cohorts/case series. (amato2023genetherapyin pages 2-3, shakeel2024phenotypeandgenetic pages 2-3)
   - Suggested HPO: **Choroidal neovascularization (HP:0007701)**

6. **Angle-closure glaucoma predisposition (especially ARB with short axial length/narrow angles)**
   - Evidence: ARB cohort shows frequent shallow anterior chamber/narrow angles; misdiagnosis as angle-closure glaucoma common; preventive iridotomy and glaucoma surgeries used. (zhao2024clinicalandgenetic pages 1-2)
   - Suggested HPO: **Angle-closure glaucoma (HP:0001132)**; **Shallow anterior chamber (HP:0000594)**; **Short axial length (HP:0000568)**

### 3.2 Phenotype characteristics (age of onset, severity, progression)
- **BVMD onset and course:** median onset ~**19 years** (range **4–65**), with slow progression and variable expressivity; imaging-based staging shows lesion composition evolves over time. (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3)
- **Vision statistics in BVMD:** one review reports ~**75%** of patients **<40 years** maintain **≥20/40** in at least one eye; ~**75%** of patients **>30 years** have **≤20/100** in at least one eye. (bianco2024multimodalimagingin pages 1-2)
- **ARB onset and course:** in a 2024 Chinese cohort (n=17), average onset **30.53 years** (range **9–68**) with acuity from **light perception to 0.8**; wide phenotypic variability and frequent anterior segment abnormalities. (zhao2024clinicalandgenetic pages 1-2)

### 3.3 Quality of life impact
The retrieved evidence does not provide formal QoL instrument results (e.g., EQ‑5D, VFQ‑25). However, progressive central vision loss and macular atrophy logically impair reading/driving and daily functioning; this should be confirmed with disease-specific QoL studies not present in the current corpus. (No direct QoL evidence in retrieved texts)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Gene:** **BEST1** (bestrophin‑1) (amato2023genetherapyin pages 1-2)
- **Protein:** 585‑aa homopentameric Ca2+-activated anion channel, localized primarily to the **RPE basolateral membrane** (and also discussed in relation to ER localization). (amato2023genetherapyin pages 1-2, amato2023genetherapyin pages 7-8)

### 4.2 Pathogenic variant spectrum and classification
#### Variant types
- In a large Chinese ARB study, 54 distinct pathogenic variants included missense, nonsense, canonical splicing, frameshift, in-frame deletions, synonymous/regulatory changes, and **deep intronic variants** uncovered by WGS. (shi2023comprehensivegeneticanalysis pages 3-5, shi2023comprehensivegeneticanalysis pages 1-2)
- Deep intronic variants **c.1101-491A>G** and **c.867+97G>A/T** caused pseudoexon insertion or intron retention, generating **premature termination codons** consistent with transcript disruption (NMD) and loss-of-function. (shi2023comprehensivegeneticanalysis pages 1-2, shi2023comprehensivegeneticanalysis pages 2-3)

#### Mechanistic classes (current understanding)
BEST1 pathogenic variants are described in mechanistic categories:
- **Loss-of-function (LOF)**
- **Dominant-negative (DN)** (enabled by pentameric co-assembly, “poisoning” WT complexes)
- **Gain-of-function (GOF)** (less common; may require silencing + augmentation)
Gene therapy design implications follow from this classification. (amato2023genetherapyin pages 4-6, amato2023genetherapyin pages 1-2)

### 4.3 Allele frequency / founder variants (examples)
- **Founder variant in Chinese ARB:** **c.867+97G>A** (intron 7) accounted for **16%** (20/125) of alleles in one Chinese cohort; haplotype analysis supported a founder effect. (shi2023comprehensivegeneticanalysis pages 5-8)
- Common coding alleles in that cohort included **p.Arg255Trp (12.8%)**, **p.Tyr44His (5.6%)**, and **p.Ala195Val (5.6%)**. (shi2023comprehensivegeneticanalysis pages 5-8)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic alterations, or chromosomal abnormalities were identified in the retrieved evidence set.

---

## 5. Environmental Information
No clear non-genetic causal environmental exposures were identified in the retrieved evidence. BEST1 bestrophinopathies are primarily genetic. (amato2023genetherapyin pages 2-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Molecular function and causal chain
**Upstream trigger:** pathogenic BEST1 variant → altered bestrophin‑1 channel quantity/function.

**Core molecular role:** bestrophin‑1 is a **Ca2+-activated anion (Cl−) channel** in RPE; its activity contributes to RPE electrophysiology and the **EOG light rise**. (amato2023genetherapyin pages 2-3, khan2018normalelectrooculographyin pages 9-13)

**Proposed downstream steps (integrated from human and iPSC‑RPE evidence):**
1. BEST1 dysfunction perturbs RPE chloride conductance and Ca2+-dependent physiology, including ER calcium handling/store-dependent signaling. (khan2018normalelectrooculographyin pages 9-13, amato2023genetherapyin pages 7-8)
2. Altered Ca2+ homeostasis affects multiple RPE processes (reported/implicated): photoreceptor outer segment (POS) phagocytosis, pigment granule migration, and membrane potential dynamics. (khan2018normalelectrooculographyin pages 9-13)
3. RPE support failure contributes to accumulation of subretinal material, fluid dysregulation (subretinal/intraretinal fluid), and progressive outer retinal disruption leading to photoreceptor dysfunction/degeneration and macular atrophy. (boon2009clinicalandmolecular pages 11-13, pfister2021phenotypicandgenetic pages 1-2)

### 6.2 Structural biology and pharmacologic modulation (2024 development)
Owji et al. (Nature Communications, **Dec 2024**) solved ligand-bound bestrophin structures and identified an **extracellular positive allosteric site** where **PABA (4-aminobenzoic acid)** binds (same site as GABA in Best2). PABA activates Best1 with **EC50 ~192 nM** and can **rescue currents** of multiple patient-derived dominant LOF Best1 mutants (A10T, R218H, L234P, A243T, Q293K, D302A) in co-expression experiments. This provides a mechanistically grounded small-molecule strategy complementary to gene therapy approaches. (owji2024neurotransmitterboundbestrophinchannel pages 5-6, owji2024neurotransmitterboundbestrophinchannel pages 1-2)

### 6.3 Suggested ontology terms
**GO Biological Process (suggested):**
- Chloride transmembrane transport (GO:1902476)
- Calcium ion homeostasis (GO:0055074)
- Phagocytosis (GO:0006909)
- Visual perception (GO:0007601)

**GO Cellular Component (suggested):**
- Basolateral plasma membrane (GO:0016323)
- Endoplasmic reticulum membrane (GO:0005789)

**Cell types (CL terms, suggested):**
- Retinal pigment epithelial cell (CL:0002584)
- Rod photoreceptor cell (CL:0000740)
- Cone photoreceptor cell (CL:0000742)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary system: **Eye / visual system**, with disease centered on:
- **Retina**, especially **macula** (BVMD) and broader posterior pole involvement (ARB). (beryozkin2024bestdiseaseglobal pages 1-2, zhao2024clinicalandgenetic pages 1-2)

### 7.2 Tissue/cell level
- **Retinal pigment epithelium (RPE)** is the key primary affected tissue/cell type (BEST1 expression and electrophysiologic signature). (amato2023genetherapyin pages 1-2)

### 7.3 Subcellular localization
- Basolateral membrane of RPE; ER membrane localization also discussed (relevant to Ca2+ regulation). (amato2023genetherapyin pages 1-2, amato2023genetherapyin pages 7-8)

**Suggested UBERON terms:**
- Retina (UBERON:0000966)
- Macula lutea (UBERON:0001807)
- Retinal pigment epithelium (UBERON:0001994)
- Anterior chamber of eye (UBERON:0001769) (relevant to ARB angle closure predisposition)

---

## 8. Temporal Development

### 8.1 Onset
- **BVMD:** median ~19 years (range 4–65). (bianco2024multimodalimagingin pages 1-2)
- **ARB:** mean onset ~30.5 years (range 9–68) in one 2024 cohort; onset can also occur in childhood in other reports/series. (zhao2024clinicalandgenetic pages 1-2, pfister2021phenotypicandgenetic pages 2-3)

### 8.2 Progression
- Generally **slowly progressive**, with central photoreceptors often viable for decades, supporting a long interventional window. (amato2023genetherapyin pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Inheritance patterns
- **Autosomal dominant:** typical for BVMD; also ADVIRC and other BEST1 phenotypes. (bianco2024multimodalimagingin pages 1-2, amato2023genetherapyin pages 2-3)
- **Autosomal recessive:** ARB (biallelic variants); recessive BVMD-like presentations exist. (zhao2024clinicalandgenetic pages 1-2, dhoble2024typicalbestvitelliform pages 7-11)

### 9.2 Epidemiology (statistics from recent sources)
- BVMD prevalence estimates vary: ~**1/10,000** (USA), **2/10,000** (Sweden), **1/20,000** (Minnesota), **1.5/100,000** (Denmark). (bianco2024multimodalimagingin pages 1-2)
- Israel prevalence estimate for Best disease: **1 in 127,000**, with differences by subgroup (**1 in 76,000** Arab Muslims; **1 in 145,000** Jews). (beryozkin2024bestdiseaseglobal pages 1-2)

---

## 10. Diagnostics

### 10.1 Core clinical tests and typical findings
- **Electro-oculogram (EOG):** hallmark reduced light peak / reduced Arden ratio; however normal EOG can occur in a minority (e.g., 8% in one large series). (amato2023genetherapyin pages 2-3)
- **Full-field ERG:** typically normal or mildly reduced in BVMD; can be reduced in ARB. (bianco2024multimodalimagingin pages 1-2, pfister2021phenotypicandgenetic pages 1-2)
- **OCT:** essential for staging and quantifying subretinal material/fluid; shows characteristic vitelliform lesion morphology and outer retinal layer disruption. (amato2023genetherapyin pages 2-3, bianco2024multimodalimagingin pages 1-2)
- **FAF / quantitative FAF:** helps interpret lipofuscin-related signals and disease evolution; contributes to revised pathogenesis concepts (lipofuscin accumulation may be secondary). (bianco2024multimodalimagingin pages 1-2)
- **OCT-A:** detects macular neovascularization and nonexudative CNV. (amato2023genetherapyin pages 2-3, bianco2024multimodalimagingin pages 1-2)
- **Genetic testing:** emphasized as “gold standard” due to variable clinical presentation. (beryozkin2024bestdiseaseglobal pages 1-2)

### 10.2 Differential diagnosis and diagnostic pitfalls
- BVMD vs **AOFVD/pattern dystrophy**: similar vitelliform lesions; age of onset and EOG/angiographic features can help, and genetics clarifies. (makati2014electrooculographyandoptical pages 3-4, zhao2024clinicalandgenetic pages 1-2)
- ARB may be misdiagnosed as **angle-closure glaucoma**, **Best disease**, or **central serous chorioretinopathy with CNV**. (zhao2024clinicalandgenetic pages 1-2, zhao2024clinicalandgenetic pages 2-4)

---

## 11. Outcome / Prognosis

### 11.1 Vision outcomes
- BVMD prognosis is variable; many younger patients retain good acuity, but later stages with atrophy/fibrosis reduce acuity. Quantitative visual outcomes in one review: 75% <40 years retain ≥20/40 (≥1 eye) while 75% >30 years have ≤20/100 (≥1 eye). (bianco2024multimodalimagingin pages 1-2)

### 11.2 Prognostic factors
Specific prognostic biomarkers are not established in the retrieved evidence; however, multimodal imaging (OCT staging, ellipsoid zone integrity, neovascularization status) is emphasized for monitoring and prognostication. (bianco2024multimodalimagingin pages 1-2)

---

## 12. Treatment

### 12.1 Current real-world management
No approved disease-modifying pharmacotherapy is established in the retrieved evidence; management focuses on monitoring and treating complications.

**Complication-directed care:**
- **Anti-VEGF therapy for CNV/CNVM** (e.g., bevacizumab, conbercept) is used when neovascular complications occur. (shakeel2024phenotypeandgenetic pages 2-3, zhao2024clinicalandgenetic pages 2-4)
- **Angle-closure risk management in ARB**: preventive **laser peripheral iridotomy** and glaucoma surgery (trabeculectomy + iridotomy) were used in a 2024 cohort. (zhao2024clinicalandgenetic pages 1-2, zhao2024clinicalandgenetic pages 2-4)

**Suggested MAXO terms (examples):**
- Anti-VEGF therapy (MAXO:0001298) (term label may vary)
- Laser peripheral iridotomy (MAXO term not confirmed in evidence)
- Trabeculectomy (MAXO term not confirmed in evidence)
- Genetic counseling (MAXO:0000079) (term label may vary)

### 12.2 Advanced therapeutics and latest research (2023–2024 prioritized)
#### Gene therapy / gene augmentation (preclinical → clinical)
Preclinical gene augmentation in canine models shows lesion reversal after subretinal AAV delivery with sustained effects up to **245 weeks** and no inflammatory response in reported experiments, supporting a translational basis for human trials. (amato2023genetherapyin pages 6-7)

#### Small-molecule channel activation (Dec 2024)
PABA and related small molecules activate Best1 and can rescue currents for multiple dominant LOF mutants in vitro, suggesting a potential pharmacologic approach for dominant LOF bestrophinopathies. (owji2024neurotransmitterboundbestrophinchannel pages 5-6)

### 12.3 Clinical trials and real-world implementations
- **NCT05809635 (started 2021-03-30; recruiting)**: Prospective natural history study for BEST1 vitelliform macular dystrophy; endpoints include OCT, FAF, NIR-AF, qAF, EOG, ERG, perimetry, etc., to define sensitive outcome measures for future clinical trials. (NCT05809635 chunk 1)
- **NCT07185256 (Opus Genetics; 2025; recruiting)**: Interventional study of subretinal **OPGx-BEST1** in BVMD or ARB; includes patient-reported outcomes and genetic eligibility criteria. (NCT07185256 chunk 2)
- **NCT02162953 (Mayo Clinic; completed 2022-12-31)**: Observational study collecting samples to generate iPSC models of Best disease and other BEST1-related diseases (disease modeling resource). (NCT02162953 chunk 1)

---

## 13. Prevention
Primary prevention is not generally possible for monogenic inherited retinal diseases, but **genetic counseling**, cascade testing, and reproductive options are key.

- **Secondary prevention:** early detection through family screening and genetics to enable monitoring for CNV and angle-closure risk (especially in ARB). (beryozkin2024bestdiseaseglobal pages 1-2, zhao2024clinicalandgenetic pages 1-2)

---

## 14. Other Species / Natural Disease
- Naturally occurring disease models are described in dogs (canine multifocal retinopathy due to biallelic cBEST1 mutations), which recapitulate many human features and have been used for preclinical AAV gene augmentation studies. (amato2023genetherapyin pages 6-7)

---

## 15. Model Organisms

### 15.1 Canine model
Canine multifocal retinopathy (cmr) caused by biallelic BEST1 mutations reproduces clinical/molecular/histologic features and has enabled long-term AAV augmentation studies. (amato2023genetherapyin pages 6-7)

### 15.2 Mouse models
BEST1 knockout mice reportedly show no retinal phenotype, whereas a knock-in model with **W93C** recapitulates BVMD-like features with dominant inheritance/incomplete penetrance and reduced EOG light peak. (amato2023genetherapyin pages 6-7)

### 15.3 iPSC-RPE models (human)
Patient-derived iPSC‑RPE models demonstrate reduced phagocytosis and stress-dependent autofluorescent material accumulation, plus altered ER-dependent Ca2+ currents; these systems have been used to test rescue strategies including augmentation and silencing+augmentation for GOF/DN contexts. (khan2018normalelectrooculographyin pages 9-13, amato2023genetherapyin pages 7-8)

---

## Expert opinions and analysis (from authoritative sources)
- Reviews emphasize that bestrophinopathies are **slowly progressive** with a **wide therapeutic window**, and that the presence of **quantifiable subretinal material** makes them attractive for clinical-trial endpoints. (amato2023genetherapyin pages 1-2)
- Genetic testing is emphasized as essential/gold standard because phenotypes are variable and can overlap with other maculopathies. (beryozkin2024bestdiseaseglobal pages 1-2)

---

## Direct abstract quotes (where available in retrieved evidence)
- Gene therapy review: bestrophinopathies are collectively named and BEST1 encodes a channel localized to RPE basolateral membrane (from abstract). (amato2023genetherapyin pages 1-2)
- Imaging review abstract: “Quantitative fundus autofluorescence studies informed us that lipofuscin accumulation… is unlikely to be a primary effect of the genetic defect.” (bianco2024multimodalimagingin pages 1-2)
- Owji et al. abstract: “PABA treatment rescues the functional deficiency of patient-derived Best1 mutations.” (owji2024neurotransmitterboundbestrophinchannel pages 1-2)

---

## Gaps / not available in current evidence set
- MONDO, Orphanet, ICD‑10/11, MeSH identifiers were not present in retrieved texts.
- Formal QoL metrics and systematic environmental risk/protective factors were not present.
- Modifier genes and epigenetic signatures were not established in the retrieved evidence corpus.

---

## Key references (URLs and publication dates)
- Bianco et al. *European Journal of Ophthalmology* (Mar 2024): https://doi.org/10.1177/11206721231166434 (bianco2024multimodalimagingin pages 1-2)
- Beryozkin et al. *IOVS* (Feb 2024): https://doi.org/10.1167/iovs.65.2.39 (beryozkin2024bestdiseaseglobal pages 1-2)
- Zhao et al. *BMC Ophthalmology* (Jul 2024): https://doi.org/10.1186/s12886-024-03574-8 (zhao2024clinicalandgenetic pages 1-2)
- Shi et al. *IOVS* (Sep 2023): https://doi.org/10.1167/iovs.64.12.37 (shi2023comprehensivegeneticanalysis pages 1-2)
- Amato et al. *Saudi Journal of Ophthalmology* (Oct 2023): https://doi.org/10.4103/sjopt.sjopt_175_23 (amato2023genetherapyin pages 1-2)
- Owji et al. *Nature Communications* (Dec 2024): https://doi.org/10.1038/s41467-024-54938-z (owji2024neurotransmitterboundbestrophinchannel pages 1-2)
- ClinicalTrials.gov NCT05809635: https://clinicaltrials.gov/study/NCT05809635 (NCT05809635 chunk 1)
- ClinicalTrials.gov NCT07185256: https://clinicaltrials.gov/study/NCT07185256 (NCT07185256 chunk 2)
- ClinicalTrials.gov NCT02162953: https://clinicaltrials.gov/study/NCT02162953 (NCT02162953 chunk 1)


References

1. (bianco2024multimodalimagingin pages 1-2): Lorenzo Bianco, Alessandro Arrigo, Alessio Antropoli, Alessandro Berni, Andrea Saladino, Manuel AP Vilela, Ahmad M Mansour, Francesco Bandello, and Maurizio Battaglia Parodi. Multimodal imaging in best vitelliform macular dystrophy: literature review and novel insights. European Journal of Ophthalmology, 34:39-51, Mar 2024. URL: https://doi.org/10.1177/11206721231166434, doi:10.1177/11206721231166434. This article has 23 citations and is from a peer-reviewed journal.

2. (beryozkin2024bestdiseaseglobal pages 1-2): Avigail Beryozkin, Ifat Sher, Miriam Ehrenberg, Dinah Zur, Hadas Newman, Libe Gradstein, Francis Simaan, Ygal Rotenstreich, Nitza Goldenberg-Cohen, Irit Bahar, Anat Blumenfeld, Antonio Rivera, Boris Rosin, Iris Deitch-Harel, Ido Perlman, Hadas Mechoulam, Itay Chowers, Rina Leibu, Tamar Ben-Yosef, Eran Pras, Eyal Banin, Dror Sharon, and Samer Khateb. Best disease: global mutations review, genotype–phenotype correlation, and prevalence analysis in the israeli population. Investigative Opthalmology &amp; Visual Science, 65:39, Feb 2024. URL: https://doi.org/10.1167/iovs.65.2.39, doi:10.1167/iovs.65.2.39. This article has 6 citations.

3. (amato2023genetherapyin pages 2-3): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 8 citations.

4. (owji2024neurotransmitterboundbestrophinchannel pages 5-6): Aaron P. Owji, Jingyun Dong, Alec Kittredge, Jiali Wang, Yu Zhang, and Tingting Yang. Neurotransmitter-bound bestrophin channel structures reveal small molecule drug targeting sites for disease treatment. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-54938-z, doi:10.1038/s41467-024-54938-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

5. (zhao2024clinicalandgenetic pages 1-2): Dongsheng Zhao, Victoria Y. Gu, Yafu Wang, Jie Peng, Jiao Lyu, Ping Fei, Yu Xu, Xiang Zhang, and Peiquan Zhao. Clinical and genetic features in autosomal recessive bestrophinopathy in chinese cohort. BMC Ophthalmology, Jul 2024. URL: https://doi.org/10.1186/s12886-024-03574-8, doi:10.1186/s12886-024-03574-8. This article has 4 citations and is from a peer-reviewed journal.

6. (shi2023comprehensivegeneticanalysis pages 5-8): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

7. (shi2023comprehensivegeneticanalysis pages 1-2): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

8. (dhoble2024typicalbestvitelliform pages 1-7): Pankaja Dhoble, Anthony G. Robson, Andrew R. Webster, and Michel Michaelides. Typical best vitelliform dystrophy secondary to biallelic variants in best1. Ophthalmic Genetics, 45:38-43, Mar 2024. URL: https://doi.org/10.1080/13816810.2023.2188227, doi:10.1080/13816810.2023.2188227. This article has 2 citations and is from a peer-reviewed journal.

9. (dhoble2024typicalbestvitelliform pages 7-11): Pankaja Dhoble, Anthony G. Robson, Andrew R. Webster, and Michel Michaelides. Typical best vitelliform dystrophy secondary to biallelic variants in best1. Ophthalmic Genetics, 45:38-43, Mar 2024. URL: https://doi.org/10.1080/13816810.2023.2188227, doi:10.1080/13816810.2023.2188227. This article has 2 citations and is from a peer-reviewed journal.

10. (makati2014electrooculographyandoptical pages 3-4): Ravie Makati, Diana Shechtman, Eulogio Besada, and Joseph J. Pizzimenti. Electrooculography and optical coherence tomography reveal late-onset best disease. Optometry and Vision Science, 91:e274–e277, Nov 2014. URL: https://doi.org/10.1097/opx.0000000000000403, doi:10.1097/opx.0000000000000403. This article has 4 citations and is from a peer-reviewed journal.

11. (amato2023genetherapyin pages 1-2): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 8 citations.

12. (khan2018normalelectrooculographyin pages 9-13): Kamron N. Khan, Farrah Islam, Graham E. Holder, Anthony Robson, Andrew R. Webster, Anthony T. Moore, and Michel Michaelides. Normal electrooculography in best disease and autosomal recessive bestrophinopathy. Retina, 38:379–386, Feb 2018. URL: https://doi.org/10.1097/iae.0000000000001523, doi:10.1097/iae.0000000000001523. This article has 23 citations.

13. (amato2023genetherapyin pages 6-7): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 8 citations.

14. (shi2023comprehensivegeneticanalysis pages 2-2): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

15. (shakeel2024phenotypeandgenetic pages 2-3): Areeba Shakeel, Darshan M Bhatt, Lingam Gopal, Rajiv Raman, Chetan Rao, S. Sripriya, and Muna Bhende. Phenotype and genetic spectrum of six indian patients with bestrophinopathy. Taiwan Journal of Ophthalmology, 14:602-608, Oct 2024. URL: https://doi.org/10.4103/tjo.tjo-d-24-00080, doi:10.4103/tjo.tjo-d-24-00080. This article has 2 citations.

16. (cideciyan2023photoreceptorfunctionand pages 6-8): Artur V. Cideciyan, Samuel G. Jacobson, Alexander Sumaroka, Malgorzata Swider, Arun K. Krishnan, Rebecca Sheplock, Alexandra V. Garafalo, Karina E. Guziewicz, Gustavo D. Aguirre, William A. Beltran, Yoshitsugu Matsui, Mineo Kondo, and Elise Heon. Photoreceptor function and structure in retinal degenerations caused by biallelic best1 mutations. Vision Research, 203:108157, Feb 2023. URL: https://doi.org/10.1016/j.visres.2022.108157, doi:10.1016/j.visres.2022.108157. This article has 5 citations and is from a peer-reviewed journal.

17. (amato2023genetherapyin pages 7-8): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 8 citations.

18. (shi2023comprehensivegeneticanalysis pages 3-5): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

19. (shi2023comprehensivegeneticanalysis pages 2-3): Jie-Feng Shi, Lu Tian, Tengyang Sun, Xiao Zhang, K. Xu, Yue Xie, Xiaoyan Peng, Xin Tang, Zidan Jin, and Yang Li. Comprehensive genetic analysis unraveled the missing heritability and a founder variant of <i>best1</i> in a chinese cohort with autosomal recessive bestrophinopathy. Investigative Opthalmology &amp; Visual Science, 64:37, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.37, doi:10.1167/iovs.64.12.37. This article has 8 citations.

20. (amato2023genetherapyin pages 4-6): Alessia Amato, Nida Wongchaisuwat, Andrew Lamborn, Ryan Schmidt, Lesley Everett, Paul Yang, and Mark E. Pennesi. Gene therapy in bestrophinopathies: insights from preclinical studies in preparation for clinical trials. Saudi Journal of Ophthalmology, 37:287-295, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_175\_23, doi:10.4103/sjopt.sjopt\_175\_23. This article has 8 citations.

21. (boon2009clinicalandmolecular pages 11-13): CAMIEL J. F. BOON, THOMAS THEELEN, ELISABETH H. HOEFSLOOT, MARY J. VAN SCHOONEVELD, JAN E. E. KEUNEN, FRANS P. M. CREMERS, B JEROEN KLEVERING, and CAREL B. HOYNG. Clinical and molecular genetic analysis of best vitelliform macular dystrophy. Retina, 29:835-847, Jun 2009. URL: https://doi.org/10.1097/iae.0b013e31819d4fda, doi:10.1097/iae.0b013e31819d4fda. This article has 88 citations.

22. (pfister2021phenotypicandgenetic pages 1-2): Tyler A. Pfister, Wadih M. Zein, Catherine A. Cukras, Hatice N. Sen, Ramiro S. Maldonado, Laryssa A. Huryn, and Robert B. Hufnagel. Phenotypic and genetic spectrum of autosomal recessive bestrophinopathy and best vitelliform macular dystrophy. Investigative Opthalmology &amp; Visual Science, 62:22, May 2021. URL: https://doi.org/10.1167/iovs.62.6.22, doi:10.1167/iovs.62.6.22. This article has 22 citations.

23. (owji2024neurotransmitterboundbestrophinchannel pages 1-2): Aaron P. Owji, Jingyun Dong, Alec Kittredge, Jiali Wang, Yu Zhang, and Tingting Yang. Neurotransmitter-bound bestrophin channel structures reveal small molecule drug targeting sites for disease treatment. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-54938-z, doi:10.1038/s41467-024-54938-z. This article has 6 citations and is from a highest quality peer-reviewed journal.

24. (pfister2021phenotypicandgenetic pages 2-3): Tyler A. Pfister, Wadih M. Zein, Catherine A. Cukras, Hatice N. Sen, Ramiro S. Maldonado, Laryssa A. Huryn, and Robert B. Hufnagel. Phenotypic and genetic spectrum of autosomal recessive bestrophinopathy and best vitelliform macular dystrophy. Investigative Opthalmology &amp; Visual Science, 62:22, May 2021. URL: https://doi.org/10.1167/iovs.62.6.22, doi:10.1167/iovs.62.6.22. This article has 22 citations.

25. (zhao2024clinicalandgenetic pages 2-4): Dongsheng Zhao, Victoria Y. Gu, Yafu Wang, Jie Peng, Jiao Lyu, Ping Fei, Yu Xu, Xiang Zhang, and Peiquan Zhao. Clinical and genetic features in autosomal recessive bestrophinopathy in chinese cohort. BMC Ophthalmology, Jul 2024. URL: https://doi.org/10.1186/s12886-024-03574-8, doi:10.1186/s12886-024-03574-8. This article has 4 citations and is from a peer-reviewed journal.

26. (NCT05809635 chunk 1): Stephen H. Tsang. Study of BEST1 Vitelliform Macular Dystrophy. Columbia University. 2021. ClinicalTrials.gov Identifier: NCT05809635

27. (NCT07185256 chunk 2):  Safety and Tolerability of Subretinally Injected OPGx-BEST1 in Patients With Best Vitelliform Macular Dystrophy (BVMD) or Autosomal-Recessive Bestrophinopathy (ARB). Opus Genetics, Inc. 2025. ClinicalTrials.gov Identifier: NCT07185256

28. (NCT02162953 chunk 1): Alan D. Marmorstein, Ph.D.. Stem Cell Models of Best Disease and Other Retinal Degenerative Diseases.. Mayo Clinic. 2014. ClinicalTrials.gov Identifier: NCT02162953