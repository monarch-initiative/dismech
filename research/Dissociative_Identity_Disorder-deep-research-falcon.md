---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T09:45:49.725343'
end_time: '2026-04-28T10:00:54.719707'
duration_seconds: 904.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dissociative Identity Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 5000
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dissociative Identity Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Dissociative Identity Disorder** covering all of the
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
- **Disease Name:** Dissociative Identity Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Dissociative Identity Disorder** covering all of the
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


# Dissociative Identity Disorder (DID): Disease Characteristics Research Report (Psychiatric)

## Executive summary
Dissociative identity disorder (DID) is a dissociative disorder characterized by disruption of identity (≥2 distinct personality states/self-states) with discontinuity in sense of self/agency and associated alterations in affect, behavior, consciousness, memory, perception, cognition and/or sensorimotor functioning, commonly accompanied by amnesia and clinically significant distress/impairment. DID is widely conceptualized as a trauma-related, developmental condition with frequent comorbidity and underrecognition in routine care; structured diagnostic interviews substantially increase detection. Recent (2023–2024) work continues to refine neurobiological correlates (e.g., hippocampal subfields linked to dissociative amnesia) and emphasizes staged/phase-oriented psychotherapy with careful dissociation screening prior to trauma processing. (brand2016separatingfactfrom pages 1-2, purcell2024treatmentofdissociative pages 4-6, dimitrova2023aneurostructuralbiomarker pages 1-2, foote2006prevalenceofdissociative pages 1-2, purcell2024treatmentofdissociative pages 21-22)

## 1. Disease information

### 1.1 What is the disease?
DID is defined in DSM-5 terms as an identity disruption involving two or more distinct personality states with marked discontinuity in self/agency and associated changes in multiple mental functions (affect, behavior, consciousness, memory, perception, cognition, sensorimotor function). DID is commonly framed as a complex posttraumatic developmental disorder linked to childhood trauma, though dissociative symptoms are often obscured by comorbid presentations and patient shame/avoidance. (brand2016separatingfactfrom pages 1-2)

### 1.2 Key identifiers and codes
| Identifier system | Code/ID | Label | Notes | Key citation IDs |
|---|---|---|---|---|
| DSM-5 / DSM-5-TR concept | N/A | Dissociative Identity Disorder | Core definition phrase: identity disruption with **two or more distinct personality states**, with marked discontinuity in sense of self/agency and related alterations in affect, behavior, consciousness, memory, perception, cognition, and/or sensory-motor functioning; commonly associated with amnesia and trauma-related presentation. | (brand2016separatingfactfrom pages 1-2, purcell2024treatmentofdissociative pages 4-6) |
| ICD-11 | 6B64 | Dissociative identity disorder | Explicitly listed in ICD-11 dissociative disorders grouping. | (mateofernandez2024dissociationasa pages 2-3, krawczyk2020icd11vs.icd10 pages 7-10) |
| ICD-11 | 6B65 | Partial dissociative identity disorder | Explicit ICD-11 category related to DID spectrum; noted as a separate diagnostic entity from full DID. | (mateofernandez2024dissociationasa pages 2-3, krawczyk2020icd11vs.icd10 pages 7-10) |
| ICD-10 (codes reported in evidence) | F44.81 | Multiple personality disorder / DID equivalent | Older ICD-10 terminology reported in the evidence as the ICD-10 counterpart to DID; terminology often differs from DSM-5 wording. | (mateofernandez2024dissociationasa pages 2-3) |
| ICD-10 (codes reported in evidence) | F44.8 | Dissociative identity disorder / other dissociative disorder code used in case report | A 2024 case report stated diagnosis was coded as **F44.8** under ICD-10; this appears in the retrieved evidence and reflects coding variation across sources/settings. | (NCT02459340 chunk 1) |
| Synonym / legacy term | N/A | Multiple personality disorder | Historical name still used in older ICD-10-era literature and case reports; replaced by DID terminology in modern DSM/ICD-11 usage. | (mateofernandez2024dissociationasa pages 2-3, krawczyk2020icd11vs.icd10 pages 7-10) |
| Synonym / shorthand | DID | Dissociative Identity Disorder | Standard abbreviation used across contemporary research, diagnostic interviews, and clinical trials. | (fidyk2025dissociativeidentitydisorder pages 1-4, NCT06330467 chunk 1) |


*Table: This table summarizes the main identifier systems and diagnostic codes for dissociative identity disorder, including ICD-11 and ICD-10 labels reported in the evidence. It also captures common synonyms and a concise DSM-5-style definition phrase to support disease knowledge-base normalization.*

**ICD-11:** Dissociative identity disorder is coded as **6B64**, and **partial dissociative identity disorder** as **6B65**. (mateofernandez2024dissociationasa pages 2-3, krawczyk2020icd11vs.icd10 pages 7-10)

**ICD-10 (as reported in retrieved sources):** “Multiple personality disorder” **F44.81** is cited as the ICD-10 counterpart in an ICD-11/ICD-10 comparison table; a case report also documents use of **F44.8** for DID coding in a clinical setting, reflecting variability in practice and mapping. (mateofernandez2024dissociationasa pages 2-3, NCT02459340 chunk 1)

**MeSH / MONDO:** A definitive MeSH descriptor ID and MONDO ID were not retrievable from the current tool evidence set; this section is therefore incomplete and should be populated directly from NLM MeSH Browser and the MONDO ontology release. (No tool-retrieved evidence)

### 1.3 Common synonyms and alternative names
Common synonyms include **multiple personality disorder** (legacy term) and the abbreviation **DID**. (mateofernandez2024dissociationasa pages 2-3, fidyk2025dissociativeidentitydisorder pages 1-4)

### 1.4 Evidence sources (individual vs aggregated)
The evidence synthesized here includes (i) aggregated disease-level resources (ICD-11 update reviews; meta-analyses and reviews), (ii) clinical epidemiology studies with structured diagnostic interviews in outpatient/inpatient cohorts, (iii) neuroimaging case–control studies, and (iv) ClinicalTrials.gov registry entries describing real-world research implementations. (krawczyk2020icd11vs.icd10 pages 7-10, mychailyszyn2021differentiatingdissociativefrom pages 7-9, foote2006prevalenceofdissociative pages 1-2, dimitrova2023aneurostructuralbiomarker pages 1-2, NCT06330467 chunk 1)

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
A contemporary diathesis–stress framing described in a 2024 expert review posits (a) a diathesis of high innate capacity for dissociation/hypnosis (including autohypnotic trance states) and (b) a stressor of intolerable, physically inescapable early childhood maltreatment (neglect/abuse). The hypothesized causal chain is that autohypnosis-based compartmentalization of overwhelming experiences leads to dissociative self-states and memory discontinuities. (purcell2024treatmentofdissociative pages 4-6)

### 2.2 Risk factors (human clinical evidence)
**Childhood physical and sexual abuse**: In an inner-city outpatient study using structured interviews, childhood physical abuse (OR 5.86, 95% CI 2.06–16.6) and childhood sexual abuse (OR 7.88, 95% CI 2.65–23.39) were associated with having any dissociative disorder diagnosis. (foote2006prevalenceofdissociative pages 4-5)

**Childhood emotional neglect**: In a 2023 hippocampal MRI study of women with DID, emotional neglect correlated negatively with global hippocampal volume and multiple subfields, supporting links between neglect and brain structural correlates of dissociation. (dimitrova2023aneurostructuralbiomarker pages 1-2)

### 2.3 Protective factors
Robust, DID-specific protective-factor evidence (e.g., resilience, social support, early intervention preventing DID onset) was not identified in the retrieved primary evidence set.

### 2.4 Gene–environment interactions
The 2024 expert review describes the dissociation/hypnosis diathesis as “likely with genetic mediation,” interacting with early maltreatment; however, specific susceptibility loci or replicated gene–environment interaction studies were not extractable from the provided evidence excerpts. (purcell2024treatmentofdissociative pages 4-6)

## 3. Phenotypes

### 3.1 Core phenotype domains (DSM-5 framing)
Key clinical manifestations include:
- **Identity disruption / identity alteration** (distinct personality states/self-states; discontinuity in self/agency). (brand2016separatingfactfrom pages 1-2)
- **Dissociative amnesia** (gaps in recall; variable inter-state amnesia), often central to diagnosis. (purcell2024treatmentofdissociative pages 4-6)
- **Depersonalization/derealization** and broader psychoform dissociation features. (purcell2024treatmentofdissociative pages 4-6)

### 3.2 Course features and onset
DID is commonly conceptualized as a developmental/trauma-related condition with early-life etiologic exposures; epidemiologic/clinical cohorts emphasize long diagnostic delays and under-recognition. A 2006 outpatient study found that only 5% of those meeting dissociative disorder criteria via structured interview had a dissociative diagnosis documented in charts. (foote2006prevalenceofdissociative pages 1-2)

### 3.3 Phenotype frequencies (examples)
In a structured-interview outpatient sample (N=82 interviewed), diagnoses were: dissociative amnesia 10%, depersonalization disorder 5%, dissociative disorder NOS 9%, and DID 6%. (foote2006prevalenceofdissociative pages 2-3)

### 3.4 Quality-of-life impact
Direct QoL metrics specific to DID vary by study and were not consistently available in the retrieved excerpts; however, ClinicalTrials.gov records for trauma/dissociation interventions use generic QoL instruments such as SF-36, implying meaningful functional and health-related QoL impairment targeted by interventions. (NCT02450617 chunk 2)

### 3.5 Suggested HPO terms (candidate mappings)
Because HPO is not tailored to psychiatric nosology, the following are *candidate* mappings for KB use (validate against HPO):
- Dissociative amnesia (candidate: **HP:0002354 Memory impairment**; **HP:0000723 Dementia** is not appropriate; consider “amnesia” term if available)
- Depersonalization/derealization (candidate: **HP:0031985 Depersonalization** / derealization if present)
- Identity disturbance (candidate: psychiatric phenotype term may not exist; consider mapping to clinical vocabulary outside HPO)

(These ontology suggestions are provided without tool-retrieved ontology evidence.)

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
No causal monogenic basis for DID is established in the retrieved evidence; DID is generally treated as a complex, trauma-associated psychiatric condition. (purcell2024treatmentofdissociative pages 4-6)

### 4.2 Modifier genes, epigenetics, and biomarkers
The retrieved evidence emphasizes neurobiological correlates (structural/functional neuroimaging) rather than validated molecular biomarkers for routine clinical use. (purcell2024treatmentofdissociative pages 27-30, dimitrova2023aneurostructuralbiomarker pages 1-2)

## 5. Environmental information

### 5.1 Environmental and psychosocial contributors
The most consistently described environmental contributors are severe and/or chronic **childhood maltreatment**, including neglect and abuse, which are associated with both diagnosis and neurobiological correlates (e.g., hippocampal volume). (purcell2024treatmentofdissociative pages 4-6, foote2006prevalenceofdissociative pages 4-5, dimitrova2023aneurostructuralbiomarker pages 1-2)

### 5.2 Infectious agents
Not applicable based on current evidence.

## 6. Mechanism / pathophysiology

### 6.1 Neuroanatomy and neuroimaging (key findings)
**Hippocampus and dissociative amnesia (2023)**: In a structural MRI case–control study (75 women; 32 DID, 43 controls), DID was associated with smaller bilateral global hippocampal volume and subfields including bilateral CA1. Dissociative amnesia uniquely correlated with reduced bilateral CA1 volumes. The authors conclude: “We propose decreased CA1 volume as a biomarker for dissociative amnesia,” and link traumatisation (emotional neglect) to hippocampal volume reduction. (dimitrova2023aneurostructuralbiomarker pages 1-2)

**Cortical morphology and early trauma (2018)**: A multicenter MRI study reported decreased cortical thickness in insula/anterior cingulate/parietal regions and reduced surface area in temporal/orbitofrontal cortices in DID; correlations between abnormal morphology, dissociative symptoms, and very early trauma exposure (0–3 years) were observed but did not survive multiple-comparison correction. (reinders2018neurodevelopmentaloriginsof pages 11-12)

### 6.2 Causal chain (integrated model)
A synthesis consistent with the 2024 expert review and imaging findings is:
1) Early inescapable maltreatment/neglect → 2) dissociation/autohypnosis-based compartmentalization → 3) enduring dissociative self-states with discontinuities in memory and self-experience → 4) downstream alterations in memory/emotion-regulation circuitry (e.g., hippocampal CA1 reductions associated with dissociative amnesia; cortical alterations in insula/ACC networks) contributing to clinical manifestations. (purcell2024treatmentofdissociative pages 4-6, dimitrova2023aneurostructuralbiomarker pages 1-2, reinders2018neurodevelopmentaloriginsof pages 11-12)

### 6.3 Suggested GO (biological process) and CL (cell type) terms (candidates)
Not directly supported by tool-retrieved mechanistic genomics evidence for DID. Candidate high-level mappings for KB interoperability include:
- GO: learning or memory; regulation of fear response; stress response; emotion regulation (candidate concepts)
- CL: hippocampal pyramidal neuron; cortical glutamatergic neuron; astrocyte/microglia (candidate concepts)

(These are conceptual mappings; validate with mechanistic molecular studies if required for the KB.)

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary system: **central nervous system** (psychiatric disorder with brain network correlates). (dimitrova2023aneurostructuralbiomarker pages 1-2, reinders2018neurodevelopmentaloriginsof pages 11-12)

### 7.2 Tissue/circuit level
Frequently implicated structures/circuits in retrieved evidence include:
- **Hippocampus (including CA1 subfield)** (dimitrova2023aneurostructuralbiomarker pages 1-2)
- **Insula and anterior cingulate cortex** as regions showing altered cortical thickness (reinders2018neurodevelopmentaloriginsof pages 11-12)

### 7.3 UBERON suggestions (candidates)
- UBERON:0001954 (brain)
- UBERON:0002421 (hippocampus)
- UBERON:0001873 (cerebral cortex)

## 8. Temporal development

### 8.1 Onset and diagnostic delay
Clinical cohorts highlight underdiagnosis and delayed detection in routine services; in one outpatient study, structured interviews detected dissociative disorders in 29% of interviewed patients while charts documented dissociative diagnoses in only 5%. (foote2006prevalenceofdissociative pages 1-2)

### 8.2 Course pattern
DID is often chronic without targeted treatment; controversies and lack of clinician training contribute to delays and suboptimal trajectories. (purcell2024treatmentofdissociative pages 4-6, brand2016separatingfactfrom pages 1-2)

## 9. Inheritance and population

### 9.1 Epidemiology (key statistics)
**General population prevalence:** Reviews cite general-population prevalence around ~1.1–1.5% based on SCID-D/DDIS studies; DID is therefore not “rare” when systematically assessed. (brand2016separatingfactfrom pages 3-4)

**Psychiatric outpatient prevalence (structured interview):**
- U.S. inner-city outpatient clinic: 24/82 (29%) had any dissociative disorder and 5/82 (6%) had DID; only 5% had prior dissociative diagnosis in charts. (Foote et al., Am J Psychiatry, 2006; DOI: 10.1176/ajp.2006.163.4.623) (foote2006prevalenceofdissociative pages 1-2)
- Egypt outpatient cohort (data collection 2018–2023): DID prevalence 4.8% by SCID-D vs 6.8% by DDIS. (abdellah2025prevalenceofdissociative pages 1-2)

**Psychiatric inpatient prevalence (structured interview):**
- Dutch inpatients: 10/122 (8%) had a dissociative disorder and ~2/122 (~1.6–2%) had DID, using DES screening plus SCID-D. (friedl2000dissociativedisordersin pages 1-2)
- Chinese inpatient training study: yield 0.4% DID in 569 inpatients (with stratified sampling and DDIS/clinical interviews) and kappa 0.75 interrater agreement. (fan2011teachingchinesepsychiatrists pages 3-6)

### 9.2 Sex ratio, demographics, geography
The retrieved evidence base includes multiple countries and emphasizes cross-cultural presence; DID prevalence and detection vary by sampling, instruments, and clinical setting. Specific pooled sex ratio estimates were not extractable from the provided evidence snippets. (brand2016separatingfactfrom pages 3-4, fan2011teachingchinesepsychiatrists pages 3-6)

## 10. Diagnostics

### 10.1 Clinical criteria (DSM-5/DSM-5-TR framing)
Core criterion domains include identity disruption with distinct personality states and associated discontinuity in self/agency, with alterations across psychological functions and frequent amnesia; DID is placed adjacent to trauma/stressor-related disorders in DSM-5 and strongly associated with childhood trauma histories. (brand2016separatingfactfrom pages 1-2)

### 10.2 Diagnostic interviews and screening instruments (implementation + validity)

**SCID-D (Structured Clinical Interview for DSM Dissociative Disorders)**
- **Meta-analysis (2021):** Across 15 studies (N=1194), the SCID-D total score strongly differentiated dissociative disorders from non-dissociative populations (Hedges g = 3.12, 95% CI 2.30–3.94). Subscales were also large: amnesia g = 2.16 and identity alteration g = 2.87 (among other domains). Authors concluded the interview shows good validity for identifying dissociative disorders and differentiating from other psychiatric disorders and feigned presentations. (Mychailyszyn et al., J Trauma Dissociation, 2021; DOI: 10.1080/15299732.2020.1760169) (mychailyszyn2021differentiatingdissociativefrom pages 7-9)
- **French validation (2022):** A French SCID-D-5 translation describes >300 questions with ratings across five domains and reports high interrater/construct validity correlations with dissociation questionnaires (e.g., Pearson correlations with SDQ-20 and DIS-Q of 0.75 and 0.81). (piedfortmarin2022reliabilityandvalidity pages 2-3)

**DES-II (Dissociative Experiences Scale-II) and follow-up**
- DES-II is widely used as a brief screener, but a 2023 EMDR-practice paper emphasizes that DES-II alone risks false negatives and lacks diagnostic/validity subscales; it recommends follow-up interviews when screening suggests dissociation. A DES score >30 is highlighted as indicating need for a structured diagnostic interview; alternative suggested brief-screen thresholds include mean cutoffs 12–20 to flag need for in-depth assessment and follow-up, and any DES item ≥20 (especially amnesia items) prompting interview. (Leeds et al., J EMDR Pract Res, 2023; DOI: 10.1891/emdr-d-21-00019) (leeds2023beyondthedesii pages 1-2, leeds2023beyondthedesii pages 11-12)

**MID / MID-60 (Multidimensional Inventory of Dissociation)**
- The 2023 EMDR-practice paper describes the MID (218 items; 74 scales) and reports a diagnostic impression predictive power of 0.89 for distinguishing DID/OSDD from other presentations; it stresses clinician-directed follow-up interview for valid use. MID resources are provided at **https://www.mid-assessment.com**. (leeds2023beyondthedesii pages 8-10)

**DDIS (Dissociative Disorders Interview Schedule)**
- The 2023 EMDR-practice paper reports DDIS sensitivity for DID of 95.4% across 196 clinically diagnosed patients and a 1% false-positive confirmation rate across 500 administrations (as cited by Ross 2021), and notes DDIS includes modules addressing confounds such as substance use. (leeds2023beyondthedesii pages 7-8)
- In the 2006 outpatient prevalence study, DDIS was the structured interview used and interviewers were trained/blinded with high interrater reliability (kappa 0.95). (foote2006prevalenceofdissociative pages 2-3)

### 10.3 Differential diagnosis (high-level)
DID is frequently misdiagnosed as other psychiatric disorders (e.g., psychotic disorders, personality disorders) because dissociative phenomena may be mistaken for hallucinations/delusions and because patients present with polysymptomatic comorbidity. (brand2016separatingfactfrom pages 1-2)

## 11. Outcome / prognosis

### 11.1 Morbidity and functioning
Routine-care underdiagnosis is substantial, implying prolonged morbidity and misdirected treatment. In the 2006 outpatient study, only 5% of structured-interview-identified dissociative diagnoses were present in chart records. (foote2006prevalenceofdissociative pages 1-2)

### 11.2 Suicidality and self-harm
The retrieved evidence set did not yield a DID-specific meta-analytic suicide rate. However, DID and dissociative disorders are repeatedly described as high-risk/high-utilization conditions with self-harm and suicidality concerns, and clinical trial protocols frequently exclude acute suicidality, reflecting clinical risk management practices. (mychailyszyn2021differentiatingdissociativefrom pages 11-13, NCT02450617 chunk 2)

## 12. Treatment

### 12.1 Current standard approaches (clinical practice)
A 2024 expert review emphasizes DID is treatable and describes **phase-oriented psychotherapy** as a mainstay (stabilization/safety and symptom management; trauma processing when appropriate; integration/rehabilitation), with adjunct psychotropics aimed primarily at comorbid symptoms rather than core identity disruption. (Purcell et al., Expert Rev Neurother, 2024; DOI: 10.1080/14737175.2024.2316153) (purcell2024treatmentofdissociative pages 4-6, purcell2024treatmentofdissociative pages 21-22)

### 12.2 Pharmacotherapy
A 2024 expert review points to limited pharmacotherapy evidence for dissociative disorders and cites a 2019 systematic review of pharmacotherapy in dissociative disorders (PubMed: 31470213). Pharmacotherapy is generally positioned as adjunctive (e.g., targeting mood/anxiety/sleep) rather than curative for core DID features in the retrieved evidence excerpts. (purcell2024treatmentofdissociative pages 21-22)

### 12.3 EMDR and real-world implementation cautions
A 2023 EMDR-practice paper emphasizes that **screening for dissociative disorders prior to EMDR trauma processing** is essential; early use of standard EMDR in unrecognized DID has been associated with destabilization (e.g., flooding, emergence of alternate identities, breaches of dissociative barriers). The paper recommends more comprehensive screening (DES-II plus follow-up interview; MID/MID-60; SCID-D or DDIS) before initiating trauma reprocessing. (leeds2023beyondthedesii pages 1-2, leeds2023beyondthedesii pages 6-7)

### 12.4 Clinical trials and real-world programs (examples)
- **NCT02450617 (Modum Bad; started 2014):** RCT of stabilizing group treatment for complex trauma with a dissociative-disorders arm requiring DID or DDNOS; outcomes include SF-36 QoL change and health-service use. (NCT02450617 chunk 2)
- **NCT07432646 (Modum Bad; 2023):** “Finding Solid Ground” inpatient stabilization plus outpatient continuation with 1-year follow-up, assessing dissociation (DES-II) and emotion regulation among other outcomes. (NCT07432646 chunk 1, NCT07432646 chunk 2)
- **NCT06330467 (Centre Psychothérapique de Nancy; recruiting since 2024-06-04):** Diagnostic prevalence study using SCID-D plus multiple trauma/dissociation instruments in at-risk outpatient groups (BPD, functional dissociative crises, early psychosis), specifying thresholds (e.g., DES 15; PCL-5 33; SDQ-20 28; DIS-Q 2.5). (NCT06330467 chunk 1)

### 12.5 Suggested MAXO terms (candidates)
- Psychotherapy (phase-oriented psychotherapy; trauma-informed psychotherapy)
- Psychoeducation
- Group psychotherapy
- Diagnostic interview / psychological assessment

## 13. Prevention
Primary prevention is not well established for DID in the retrieved evidence set; plausible prevention targets include preventing childhood maltreatment/neglect and early identification/treatment of dissociative symptoms following trauma exposure. Evidence in the retrieved set supports the importance of systematic screening to reduce diagnostic delay (a form of secondary prevention). (foote2006prevalenceofdissociative pages 1-2, leeds2023beyondthedesii pages 1-2)

## 14. Other species / natural disease
No naturally occurring DID analogue in non-human species is established in the retrieved evidence.

## 15. Model organisms
Given the disorder’s clinical phenomenology and reliance on self-report/identity experience, DID is not readily modeled in non-human organisms; research models focus instead on trauma-related neurobiology and dissociation-relevant circuitry in humans (e.g., MRI studies). (dimitrova2023aneurostructuralbiomarker pages 1-2, reinders2018neurodevelopmentaloriginsof pages 11-12)

## Recent developments and expert analysis (2023–2024 prioritized)

1) **Hippocampal subfields as candidate biomarkers (2023):** The Psychological Medicine study proposes CA1 volume reduction as a biomarker of dissociative amnesia in DID and links emotional neglect with hippocampal reductions. (Published 2023-06; DOI: 10.1017/S0033291721002154) (dimitrova2023aneurostructuralbiomarker pages 1-2)

2) **Treatment innovation guided by neurobiology (2024):** The Expert Review of Neurotherapeutics article argues for moving beyond historical controversy and leveraging neurobiological findings to reduce shame, guide assessment, and identify novel intervention targets, emphasizing that DID is treatable with psychotherapy and that research should include lived experience. (Published 2024-02; DOI: 10.1080/14737175.2024.2316153) (purcell2024treatmentofdissociative pages 21-22, purcell2024treatmentofdissociative pages 27-30)

3) **Improved screening prior to trauma processing (2023):** The EMDR Practice and Research paper details implementation-oriented screening pathways (DES-II, MID/MID-60, DDIS, SCID-D) to reduce harms from premature trauma reprocessing in undiagnosed DID/complex dissociation. (Published 2023-02; DOI: 10.1891/emdr-d-21-00019) (leeds2023beyondthedesii pages 1-2, leeds2023beyondthedesii pages 8-10)

## Limitations of this report
- MONDO and MeSH identifiers were not retrievable via the current tool evidence; these should be added from the MONDO ontology and NLM MeSH Browser.
- DID-specific pooled statistics for suicidality, mortality, and standardized QoL outcomes were not available from the retrieved excerpts; dedicated epidemiologic meta-analyses and longitudinal cohorts would be needed.



References

1. (brand2016separatingfactfrom pages 1-2): Bethany L. Brand, Vedat Sar, Pam Stavropoulos, Christa Krüger, Marilyn Korzekwa, Alfonso Martínez-Taboas, and Warwick Middleton. Separating fact from fiction: an empirical examination of six myths about dissociative identity disorder. Harvard Review of Psychiatry, 24:257-270, Jul 2016. URL: https://doi.org/10.1097/hrp.0000000000000100, doi:10.1097/hrp.0000000000000100. This article has 262 citations and is from a peer-reviewed journal.

2. (purcell2024treatmentofdissociative pages 4-6): Juliann B. Purcell, Bethany Brand, Heidi A. Browne, Richard A. Chefetz, Meghan Shanahan, Zoe A. Bair, Kim A. Baranowski, Vona Davis, Patricia Mangones, Rebecca L. Modell, Cori A. Palermo, Emma C. Robertson, Matthew A. Robinson, Laura Ward, Sherry Winternitz, Milissa L. Kaufman, and Lauren A. M. Lebois. Treatment of dissociative identity disorder: leveraging neurobiology to optimize success. Expert Review of Neurotherapeutics, 24:273-289, Feb 2024. URL: https://doi.org/10.1080/14737175.2024.2316153, doi:10.1080/14737175.2024.2316153. This article has 18 citations and is from a peer-reviewed journal.

3. (dimitrova2023aneurostructuralbiomarker pages 1-2): Lora I. Dimitrova, Sophie L. Dean, Yolanda R. Schlumpf, Eline M. Vissia, Ellert R. S. Nijenhuis, Vasiliki Chatzi, Lutz Jäncke, Dick J. Veltman, Sima Chalavi, and Antje A. T. S. Reinders. A neurostructural biomarker of dissociative amnesia: a hippocampal study in dissociative identity disorder. Psychological Medicine, 53:805-813, Jun 2023. URL: https://doi.org/10.1017/s0033291721002154, doi:10.1017/s0033291721002154. This article has 59 citations and is from a highest quality peer-reviewed journal.

4. (foote2006prevalenceofdissociative pages 1-2): Brad Foote, Yvette Smolin, Margaret Kaplan, Michael E. Legatt, and Deborah Lipschitz. Prevalence of dissociative disorders in psychiatric outpatients. American Journal of Psychiatry, 163:623-629, Apr 2006. URL: https://doi.org/10.1176/ajp.2006.163.4.623, doi:10.1176/ajp.2006.163.4.623. This article has 417 citations and is from a highest quality peer-reviewed journal.

5. (purcell2024treatmentofdissociative pages 21-22): Juliann B. Purcell, Bethany Brand, Heidi A. Browne, Richard A. Chefetz, Meghan Shanahan, Zoe A. Bair, Kim A. Baranowski, Vona Davis, Patricia Mangones, Rebecca L. Modell, Cori A. Palermo, Emma C. Robertson, Matthew A. Robinson, Laura Ward, Sherry Winternitz, Milissa L. Kaufman, and Lauren A. M. Lebois. Treatment of dissociative identity disorder: leveraging neurobiology to optimize success. Expert Review of Neurotherapeutics, 24:273-289, Feb 2024. URL: https://doi.org/10.1080/14737175.2024.2316153, doi:10.1080/14737175.2024.2316153. This article has 18 citations and is from a peer-reviewed journal.

6. (mateofernandez2024dissociationasa pages 2-3): Pedro V. Mateo-Fernández, Iria de la Osa Subtil, and María Ángeles de la Cruz-Fortún. Dissociation as a modifying variable of imputability in criminal cases. Journal of Psychology &amp; Clinical Psychiatry, 15:193-196, Jun 2024. URL: https://doi.org/10.15406/jpcpy.2024.15.00780, doi:10.15406/jpcpy.2024.15.00780. This article has 3 citations.

7. (krawczyk2020icd11vs.icd10 pages 7-10): Piotr Krawczyk and Łukasz Święcicki. Icd-11 vs. icd-10 – a review of updates and novelties introduced in the latest version of the who international classification of diseases. Psychiatria Polska, 54:7-20, Feb 2020. URL: https://doi.org/10.12740/pp/103876, doi:10.12740/pp/103876. This article has 93 citations.

8. (NCT02459340 chunk 1): Yolanda Schlumpf, PhD. Emotional and Cognitive Self-regulation, an EEG Study. Yolanda Schlumpf, PhD. 2015. ClinicalTrials.gov Identifier: NCT02459340

9. (fidyk2025dissociativeidentitydisorder pages 1-4): Monika Fidyk, Michał Bolek, Bartosz Jagieła, Aleksandra Kędzia, Dominika Musialska, and Magda Minkiewicz. Dissociative identity disorder: a comprehensive review of etiology, diagnosis, neurobiology, and treatment. Quality in Sport, 41:60277, May 2025. URL: https://doi.org/10.12775/qs.2025.41.60277, doi:10.12775/qs.2025.41.60277. This article has 1 citations.

10. (NCT06330467 chunk 1):  Prevalence of Dissociative Identity Disorder in At-risk Outpatient Groups Reporting Childhood Trauma.. Centre Psychothérapique de Nancy. 2024. ClinicalTrials.gov Identifier: NCT06330467

11. (mychailyszyn2021differentiatingdissociativefrom pages 7-9): Matthew P. Mychailyszyn, Bethany L. Brand, Aliya R. Webermann, Vedat Şar, and Nel Draijer. Differentiating dissociative from non-dissociative disorders: a meta-analysis of the structured clinical interview for dsm dissociative disorders (scid-d). Journal of Trauma & Dissociation, 22:19-34, May 2021. URL: https://doi.org/10.1080/15299732.2020.1760169, doi:10.1080/15299732.2020.1760169. This article has 61 citations and is from a peer-reviewed journal.

12. (foote2006prevalenceofdissociative pages 4-5): Brad Foote, Yvette Smolin, Margaret Kaplan, Michael E. Legatt, and Deborah Lipschitz. Prevalence of dissociative disorders in psychiatric outpatients. American Journal of Psychiatry, 163:623-629, Apr 2006. URL: https://doi.org/10.1176/ajp.2006.163.4.623, doi:10.1176/ajp.2006.163.4.623. This article has 417 citations and is from a highest quality peer-reviewed journal.

13. (foote2006prevalenceofdissociative pages 2-3): Brad Foote, Yvette Smolin, Margaret Kaplan, Michael E. Legatt, and Deborah Lipschitz. Prevalence of dissociative disorders in psychiatric outpatients. American Journal of Psychiatry, 163:623-629, Apr 2006. URL: https://doi.org/10.1176/ajp.2006.163.4.623, doi:10.1176/ajp.2006.163.4.623. This article has 417 citations and is from a highest quality peer-reviewed journal.

14. (NCT02450617 chunk 2):  Stabilizing Group Treatment of Complex Trauma: A Randomized Controlled Trial. Modum Bad. 2014. ClinicalTrials.gov Identifier: NCT02450617

15. (purcell2024treatmentofdissociative pages 27-30): Juliann B. Purcell, Bethany Brand, Heidi A. Browne, Richard A. Chefetz, Meghan Shanahan, Zoe A. Bair, Kim A. Baranowski, Vona Davis, Patricia Mangones, Rebecca L. Modell, Cori A. Palermo, Emma C. Robertson, Matthew A. Robinson, Laura Ward, Sherry Winternitz, Milissa L. Kaufman, and Lauren A. M. Lebois. Treatment of dissociative identity disorder: leveraging neurobiology to optimize success. Expert Review of Neurotherapeutics, 24:273-289, Feb 2024. URL: https://doi.org/10.1080/14737175.2024.2316153, doi:10.1080/14737175.2024.2316153. This article has 18 citations and is from a peer-reviewed journal.

16. (reinders2018neurodevelopmentaloriginsof pages 11-12): Antje A.T.S. Reinders, Antje A.T.S. Reinders, S. Chalavi, S. Chalavi, Yolanda R. Schlumpf, E. Vissia, E. Nijenhuis, Lutz Jäncke, D. Veltman, C. Ecker, and C. Ecker. Neurodevelopmental origins of abnormal cortical morphology in dissociative identity disorder. Acta Psychiatrica Scandinavica, Feb 2018. URL: https://doi.org/10.1111/acps.12839, doi:10.1111/acps.12839. This article has 48 citations and is from a domain leading peer-reviewed journal.

17. (brand2016separatingfactfrom pages 3-4): Bethany L. Brand, Vedat Sar, Pam Stavropoulos, Christa Krüger, Marilyn Korzekwa, Alfonso Martínez-Taboas, and Warwick Middleton. Separating fact from fiction: an empirical examination of six myths about dissociative identity disorder. Harvard Review of Psychiatry, 24:257-270, Jul 2016. URL: https://doi.org/10.1097/hrp.0000000000000100, doi:10.1097/hrp.0000000000000100. This article has 262 citations and is from a peer-reviewed journal.

18. (abdellah2025prevalenceofdissociative pages 1-2): May Mahmoud Abdellah, Khadiga Mohamed Ragheb, Taghreed Mohamed Elshafie, and Rania Ahmed Hamed. Prevalence of dissociative identity disorder among psychiatric outpatients in different cultural groups. Middle East Current Psychiatry, Jul 2025. URL: https://doi.org/10.1186/s43045-025-00546-6, doi:10.1186/s43045-025-00546-6. This article has 1 citations.

19. (friedl2000dissociativedisordersin pages 1-2): Monica C. Friedl and Nel Draijer. Dissociative disorders in dutch psychiatric inpatients. The American journal of psychiatry, 157 6:1012-3, Jun 2000. URL: https://doi.org/10.1176/appi.ajp.157.6.1012, doi:10.1176/appi.ajp.157.6.1012. This article has 187 citations.

20. (fan2011teachingchinesepsychiatrists pages 3-6): Qing Fan, Junhan Yu, Colin A. Ross, Benjamin B. Keyes, Yunfei Dai, Tianhong Zhang, Lanlan Wang, and Zeping Xiao. Teaching chinese psychiatrists to make reliable dissociative disorder diagnoses. Transcultural Psychiatry, 48:473-483, Sep 2011. URL: https://doi.org/10.1177/1363461511409484, doi:10.1177/1363461511409484. This article has 14 citations and is from a peer-reviewed journal.

21. (piedfortmarin2022reliabilityandvalidity pages 2-3): Olivier Piedfort-Marin, Cyril Tarquinio, Marlene Steinberg, Sabine Azarmsa, Thérèse Cuttelod, Marie-Eve Piot, Déborah Wisler, Eva Zimmermann, and Jessie Nater. Reliability and validity study of the french-language version of the scid-d semi-structured clinical interview for diagnosing dsm-5 and icd-11 dissociative disorders. Annales Médico-psychologiques, revue psychiatrique, 180:S1-S9, Jun 2022. URL: https://doi.org/10.1016/j.amp.2020.12.012, doi:10.1016/j.amp.2020.12.012. This article has 13 citations.

22. (leeds2023beyondthedesii pages 1-2): Andrew M. Leeds, Jennifer A. Madere, and D. Michael Coy. Beyond the des-ii: screening for dissociative disorders in emdr therapy. Journal of EMDR Practice and Research, 16:25-38, Feb 2023. URL: https://doi.org/10.1891/emdr-d-21-00019, doi:10.1891/emdr-d-21-00019. This article has 19 citations.

23. (leeds2023beyondthedesii pages 11-12): Andrew M. Leeds, Jennifer A. Madere, and D. Michael Coy. Beyond the des-ii: screening for dissociative disorders in emdr therapy. Journal of EMDR Practice and Research, 16:25-38, Feb 2023. URL: https://doi.org/10.1891/emdr-d-21-00019, doi:10.1891/emdr-d-21-00019. This article has 19 citations.

24. (leeds2023beyondthedesii pages 8-10): Andrew M. Leeds, Jennifer A. Madere, and D. Michael Coy. Beyond the des-ii: screening for dissociative disorders in emdr therapy. Journal of EMDR Practice and Research, 16:25-38, Feb 2023. URL: https://doi.org/10.1891/emdr-d-21-00019, doi:10.1891/emdr-d-21-00019. This article has 19 citations.

25. (leeds2023beyondthedesii pages 7-8): Andrew M. Leeds, Jennifer A. Madere, and D. Michael Coy. Beyond the des-ii: screening for dissociative disorders in emdr therapy. Journal of EMDR Practice and Research, 16:25-38, Feb 2023. URL: https://doi.org/10.1891/emdr-d-21-00019, doi:10.1891/emdr-d-21-00019. This article has 19 citations.

26. (mychailyszyn2021differentiatingdissociativefrom pages 11-13): Matthew P. Mychailyszyn, Bethany L. Brand, Aliya R. Webermann, Vedat Şar, and Nel Draijer. Differentiating dissociative from non-dissociative disorders: a meta-analysis of the structured clinical interview for dsm dissociative disorders (scid-d). Journal of Trauma & Dissociation, 22:19-34, May 2021. URL: https://doi.org/10.1080/15299732.2020.1760169, doi:10.1080/15299732.2020.1760169. This article has 61 citations and is from a peer-reviewed journal.

27. (leeds2023beyondthedesii pages 6-7): Andrew M. Leeds, Jennifer A. Madere, and D. Michael Coy. Beyond the des-ii: screening for dissociative disorders in emdr therapy. Journal of EMDR Practice and Research, 16:25-38, Feb 2023. URL: https://doi.org/10.1891/emdr-d-21-00019, doi:10.1891/emdr-d-21-00019. This article has 19 citations.

28. (NCT07432646 chunk 1):  "Finding Solid Ground" in Inpatient Treatment for Dissociative Disorder Patients Followed by Transition to Outpatient Treatment Settings: A 1-year Follow-up Pilot Study. Modum Bad. 2023. ClinicalTrials.gov Identifier: NCT07432646

29. (NCT07432646 chunk 2):  "Finding Solid Ground" in Inpatient Treatment for Dissociative Disorder Patients Followed by Transition to Outpatient Treatment Settings: A 1-year Follow-up Pilot Study. Modum Bad. 2023. ClinicalTrials.gov Identifier: NCT07432646