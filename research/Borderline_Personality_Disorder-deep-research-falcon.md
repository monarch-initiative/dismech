---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T09:45:48.213756'
end_time: '2026-04-28T09:57:01.038658'
duration_seconds: 672.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Borderline Personality Disorder
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
- **Disease Name:** Borderline Personality Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Borderline Personality Disorder** covering all of the
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
- **Disease Name:** Borderline Personality Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Borderline Personality Disorder** covering all of the
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


# Borderline Personality Disorder (BPD): Disease Characteristics Research Report (Psychiatric)

## 1. Disease information

### Overview (current understanding)
Borderline personality disorder (BPD) is a severe psychiatric condition characterized by pervasive instability in emotion regulation, self-image/identity, interpersonal relationships, and behavior, commonly accompanied by impulsivity and recurrent self-harm/suicidality. A recent review summarizes core features consistent with DSM descriptions (e.g., frantic efforts to avoid abandonment; unstable relationships with idealization/devaluation; identity disturbance; impulsivity; recurrent self-harm/suicidality; chronic emptiness; intense anger; and transient stress-related paranoia/dissociation). (azzam2024borderlinepersonalitydisorder pages 2-3)

### Key identifiers and ontology mappings
* **ICD-11 model (WHO)**: ICD-11 no longer uses multiple categorical personality disorder subtypes. Instead, clinicians diagnose **Personality Disorder** and specify **severity** (mild/moderate/severe) plus **trait domain qualifiers**, and may add a **“borderline pattern” qualifier**. ICD-11 was explicitly designed “to abolish all categories of personality disorder except for the general description of a personality disorder” and then specify “mild,” “moderate,” or “severe.” (mulder2021icd11personalitydisorders pages 2-3)
* **ICD-11 trait domains**: Negative affectivity, detachment, dissociality, disinhibition, and anankastia. (mulder2021icd11personalitydisorders pages 2-3, mulder2020theborderlinepattern pages 1-2, pan2024practicalimplicationsof pages 1-2)
* **ICD-11 borderline pattern qualifier**: retained as a pragmatic compromise; it “essentially lists the symptoms of” DSM-5 BPD and ICD-10 emotionally unstable personality disorder (borderline type). (mulder2020theborderlinepattern pages 1-2)
* **ICD-10 (historical)**: Swedish register studies operationalized “emotionally unstable personality disorder” using **ICD-10 F60.3**. (skoglund2021familialriskand pages 1-2)

**MeSH / MONDO / OMIM / Orphanet**: Not retrieved in the available evidence set. For knowledge-base population, these should be cross-walked from MeSH and MONDO in a follow-up curation step; BPD is not typically an OMIM/Orphanet monogenic disorder.

### Synonyms / alternative names
* **Emotionally unstable personality disorder** (ICD-10 terminology; borderline type) (mulder2020theborderlinepattern pages 1-2, skoglund2021familialriskand pages 1-2)
* **Borderline pattern** (ICD-11 qualifier) (mulder2021icd11personalitydisorders pages 2-3, mulder2020theborderlinepattern pages 1-2)

### Evidence source type
This report integrates **aggregated disease-level resources** (ICD-11 model papers and reviews) and **population-scale individual-level data** from Swedish national registers (familial risk, comorbidity, adverse outcomes). (mulder2021icd11personalitydisorders pages 2-3, skoglund2021familialriskand pages 1-2, tate2022borderlinepersonalitydisorder pages 1-2)


## 2. Etiology

### Disease causal factors (multifactorial)
BPD is widely conceptualized as multifactorial, arising from interacting genetic vulnerability and environmental exposures. A 2024 review emphasizes that **genetic predispositions** (e.g., emotional instability/impulsivity) interact with **environmental risks**, particularly childhood adversity and attachment disruption. (azzam2024borderlinepersonalitydisorder pages 6-7)

### Risk factors

#### Environmental / developmental risk factors
* **Childhood adversities/trauma** (physical, emotional, sexual abuse; neglect; inconsistent caregiving) are frequently reported in BPD and are implicated in disrupted attachment and emotion regulation development. (azzam2024borderlinepersonalitydisorder pages 6-7)
* Swedish register-based and review evidence notes that a very large proportion of clinically diagnosed BPD have psychiatric comorbidity and adverse outcomes, consistent with high cumulative burden and likely shared risk pathways. (skoglund2021familialriskand pages 2-4, tate2022borderlinepersonalitydisorder pages 1-2)

#### Genetic risk factors (polygenic)
Family and twin designs support substantial heritability. A Swedish population register study reported heritability **46% (95% CI 39–53)**, with remaining variance largely due to individually unique environmental factors. (skoglund2021familialriskand pages 1-2)

**Direct abstract quote (primary evidence):** “Heritability was estimated at **46% (95% CI = 39–53)**, and the remaining variance was explained by individually unique environmental factors.” (skoglund2021familialriskand pages 2-4)

Familial aggregation shows a gradient with genetic relatedness (hazard ratios in relatives): monozygotic twins **HR 11.5**, dizygotic twins **HR 7.4**, full siblings **HR 4.7**, maternal half-siblings **HR 2.1**, paternal half-siblings **HR 1.3**. (skoglund2021familialriskand pages 1-2)

### Protective factors
No BPD-specific protective genetic variants or robust protective environmental exposures were identified in the retrieved evidence set. However, long-term work on resilience-related cognitive profiles in relatives suggests potential protective mechanisms at the neurocognitive level (e.g., stronger response inhibition in psychiatrically unaffected relatives), but this is indirect and not a validated protective factor for BPD incidence. (gearin2022spotlightonborderline pages 2-2)

### Gene–environment interactions
Direct BPD-specific GxE effect-size estimates were not retrieved in the evidence set. Nonetheless, multiple sources emphasize that trauma/adversity and genetic liability co-occur and likely interact in shaping risk; Swedish data indicate strong familial aggregation and substantial non-shared environment contributions, consistent with a model where individual exposures (including trauma) may interact with inherited liability. (azzam2024borderlinepersonalitydisorder pages 6-7, skoglund2021familialriskand pages 1-2)


## 3. Phenotypes

### Core phenotype spectrum (symptoms and behavioral changes)
Key symptom domains include:
* **Affective instability / emotion dysregulation** (e.g., rapid mood shifts, intense negative affect). (azzam2024borderlinepersonalitydisorder pages 2-3)
* **Interpersonal instability** (e.g., intense/unstable relationships; fear of abandonment). (azzam2024borderlinepersonalitydisorder pages 2-3)
* **Identity disturbance** (unstable self-image, chronic emptiness). (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2)
* **Impulsivity / behavioral dysregulation** (potentially including substance use, risky behaviors). (azzam2024borderlinepersonalitydisorder pages 2-3)
* **Self-harm, suicidal ideation/attempts**: a major clinical feature; one review notes ~10% may die by suicide. (azzam2024borderlinepersonalitydisorder pages 2-3)

### Age of onset and course
Symptoms typically begin in **late adolescence/early adulthood** (azzam2024borderlinepersonalitydisorder pages 2-3), with a narrative psychotherapy review also noting emergence in adolescence (often after age 12). (neri2024borderlinepersonalitydisorder pages 1-2)

Course heterogeneity is emphasized: impulsivity-related symptoms (self-harm, suicidality) may remit earlier, whereas chronic affective/interpersonal problems may persist and functional impairment can remain even when diagnostic criteria remit. (neri2024borderlinepersonalitydisorder pages 1-2)

### Comorbidity and adverse outcomes (quantitative)
A large Swedish nationwide register study (n ≈ 2 million; 12,175 diagnosed BPD) found markedly elevated risks across psychiatric disorders, somatic illnesses, trauma, and adverse behaviors. Examples:
* Anxiety disorders cumulative incidence **33.13% (95% CI 31.48–34.73)**. (tate2022borderlinepersonalitydisorder pages 1-2)
* Psychotic disorders **HR 24.48 (95% CI 23.14–25.90)**. (tate2022borderlinepersonalitydisorder pages 1-2)
* Self-harm **HR 17.72 (95% CI 17.27–18.19)**. (tate2022borderlinepersonalitydisorder pages 1-2)
* Violent crime victimization **HR 7.65 (95% CI 7.25–8.06)**. (tate2022borderlinepersonalitydisorder pages 1-2)
* Epilepsy **HR 3.38 (95% CI 3.08–3.70)**. (tate2022borderlinepersonalitydisorder pages 1-2)

### Suggested HPO terms (examples for knowledge-base mapping)
HPO codes were not retrieved from HPO directly in the evidence set; below are **suggested** mappings for curation:
* Affective lability / mood swings (e.g., **HP:0000728** Mood swings — verify in HPO)
* Impulsivity (**HP:0000733** Impulsivity — verify)
* Self-injurious behavior (**HP:0100716** Self-injurious behavior — verify)
* Suicidal ideation (**HP:0031586** Suicidal ideation — verify)
* Abnormal social relationships / interpersonal dysfunction (verify HPO term)
* Chronic feelings of emptiness (may require phenotypic proxy term)


## 4. Genetic / molecular information

### Genetic architecture
BPD is **polygenic** rather than a monogenic Mendelian disorder in the retrieved evidence. The strongest quantitative evidence is familial aggregation and heritability in Swedish registries (heritability ~46%). (skoglund2021familialriskand pages 1-2)

### Notable genetic correlations / shared liability
A Swedish nationwide study showed extremely strong co-occurrence and familial co-aggregation between ADHD and BPD:
* Individuals with ADHD had **adjusted OR 19.4 (95% CI 18.6–20.4)** for also having BPD. (kujahalkola2021doborderlinepersonality pages 1-2)
* Familial co-aggregation: e.g., full siblings of ADHD cases had **aOR 2.8 (95% CI 2.6–3.1)** for BPD. (kujahalkola2021doborderlinepersonality pages 1-2)

### Epigenetics / non-coding RNA (recent developments)
A 2023 study connects a microRNA signal to brain morphology and suicidal ideation recovery in BPD. **Direct abstract quote:** “MicroRNA-124-3p (miR-124-3p) was recently identified in a Genome-Wide Association Study as likely associated with BPD.” ()

In that inpatient sample, genes targeted by miR-124-3p were co-expressed in the left globus pallidus, which was smaller in BPD than psychiatric controls, and smaller volume correlated with poorer recovery from suicidal ideation. ()

### Suggested GO / CL / UBERON terms (mechanism-linked suggestions)
Not explicitly enumerated in the evidence set; suggested for curation based on described systems:
* **UBERON**: amygdala; prefrontal cortex; anterior cingulate cortex; globus pallidus (NCT07197502 chunk 1, NCT06626789 chunk 2)
* **CL**: cortical pyramidal neuron; GABAergic interneuron; microglia (neuroinflammation context) (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)
* **GO Biological Process (examples)**: regulation of emotional behavior; response to stress; synaptic signaling; neuroinflammatory response; hypothalamic–pituitary–adrenal axis process (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)


## 5. Environmental information

### Environmental factors and lifestyle factors
Evidence in the retrieved set emphasizes **chronic stress/trauma** as major environmental inputs into BPD symptom development and maintenance. (azzam2024borderlinepersonalitydisorder pages 6-7)

A 2024 review highlights that BPD is associated with metabolic dysfunction and cardiovascular risk, with contributing factors including **obesity** and **childhood trauma**, and with inflammatory marker elevations such as CRP/hs-CRP described in the literature. (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)

### Infectious agents
No BPD-specific infectious etiology was identified in the retrieved evidence.


## 6. Mechanism / pathophysiology

### Working model causal chain (integrative)
**Upstream**: inherited liability (polygenic; ~46% heritability) + individual-specific environmental exposures (including childhood adversity) → (skoglund2021familialriskand pages 1-2, azzam2024borderlinepersonalitydisorder pages 6-7)

**Intermediate mechanisms** (proposed and partially evidenced):
* Disrupted attachment/mentalizing and emotion regulation capacities (azzam2024borderlinepersonalitydisorder pages 6-7)
* Autonomic nervous system dysregulation and stress physiology changes, including HPA-axis alterations described in a 2024 review (qualitative) (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)
* Neurobiological circuit targets for treatment trials: amygdala–ventrolateral prefrontal circuits (rTMS and neurofeedback trials) (NCT07197502 chunk 1, NCT06626789 chunk 2)
* Epigenetic/noncoding regulation and basal ganglia involvement: miR-124-3p target-gene co-expression implicating globus pallidus morphology associated with suicidal ideation recovery. ()

**Downstream**: clinical manifestations (affective instability, impulsivity, unstable relationships, self-harm/suicidality) and high comorbidity/adverse outcomes. (azzam2024borderlinepersonalitydisorder pages 2-3, tate2022borderlinepersonalitydisorder pages 1-2)

### Immune/inflammatory and physiological findings (recent)
A 2024 narrative review synthesizes evidence that BPD can be associated with increased cardiometabolic risk and inflammatory biomarkers (e.g., CRP/hs-CRP) and autonomic dysregulation (e.g., HRV alterations), though effect sizes were not extractable from the provided excerpt. (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)


## 7. Anatomical structures affected
BPD is a psychiatric disorder without primary peripheral organ pathology, but implicated neuroanatomy/circuits in the retrieved evidence includes:
* **Amygdala–ventrolateral prefrontal cortex (vlPFC)** circuitry (targeted by rTMS and neurofeedback trials). (NCT07197502 chunk 1, NCT06626789 chunk 2)
* **Globus pallidus** (reduced volume in inpatients with BPD vs psychiatric controls, in miR-124-3p target-gene analysis context). ()

Suggested UBERON terms for curation: amygdala, ventrolateral prefrontal cortex, globus pallidus.


## 8. Temporal development

### Onset
Most commonly late adolescence/early adulthood. (azzam2024borderlinepersonalitydisorder pages 2-3)

### Progression / remission
BPD can show symptom remission over years (especially impulsive/self-harm symptoms), but functional impairment may persist; course is heterogeneous. (neri2024borderlinepersonalitydisorder pages 1-2)


## 9. Inheritance and population

### Epidemiology (quantitative)
* General population prevalence estimates in recent reviews are ~**1–2%** (azzam2024borderlinepersonalitydisorder pages 2-3) and ~**1.6%** (neri2024borderlinepersonalitydisorder pages 1-2).
* Clinical settings prevalence estimates in reviews: **15–20%** in psychiatric settings (azzam2024borderlinepersonalitydisorder pages 2-3), ~**20%** clinical populations, ~**10%** ambulatory, ~**25%** hospitalized. (neri2024borderlinepersonalitydisorder pages 1-2)

### Sex ratio
A review reports approximately **3:1 female-to-male** ratio. (azzam2024borderlinepersonalitydisorder pages 2-3)
Swedish registers similarly show strong female predominance among clinically diagnosed cases (~85%). (tate2022borderlinepersonalitydisorder pages 1-2, skoglund2021familialriskand pages 2-4)

### Genetic etiology / inheritance model
Evidence supports **multifactorial/polygenic inheritance** with substantial heritability.
* Heritability: **46% (95% CI 39–53)**. (skoglund2021familialriskand pages 1-2)


## 10. Diagnostics

### Clinical criteria and structured assessment
* DSM-style diagnostic symptom domains are summarized in recent reviews (abandonment fears, relationship instability, identity disturbance, impulsivity, self-harm/suicidality, emptiness, anger, transient paranoia/dissociation). (azzam2024borderlinepersonalitydisorder pages 2-3)
* ICD-11 approach: diagnose personality disorder and rate severity and traits; optionally add the borderline pattern qualifier, which is close to the DSM borderline definition. (mulder2021icd11personalitydisorders pages 2-3, mulder2020theborderlinepattern pages 1-2)

### Biomarkers and tests
No validated laboratory biomarker is established for diagnosis in the retrieved evidence. A 2024 review discusses candidate physiological markers (e.g., CRP/hs-CRP, autonomic measures/HRV, echocardiographic strain measures) as part of cardiometabolic risk profiling rather than diagnostic biomarkers. (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)

### Differential diagnosis considerations (high-level)
Diagnostic issues include overlap with trauma-related syndromes and other mood disorders; a 2024 review highlights overlap with complex PTSD and emphasizes that trauma is common but not universal and not the sole cause. (azzam2024borderlinepersonalitydisorder pages 6-7)


## 11. Outcome / prognosis

### Mortality and suicide
BPD carries substantial suicide mortality. A 2024 review reports that roughly **10% may die by suicide** and emphasizes common recurrent self-harm/suicidality. (azzam2024borderlinepersonalitydisorder pages 2-3)

### Morbidity and functional outcomes
Register data demonstrate BPD diagnosis as a marker of vulnerability for multiple negative outcomes (psychiatric, somatic, trauma, adverse behaviors), including very high self-harm risk (HR ~17.7) and high psychiatric comorbidity burden. (tate2022borderlinepersonalitydisorder pages 1-2)


## 12. Treatment

### Evidence-based psychotherapies (core of care)
Multiple evidence-based psychotherapies are emphasized as key treatments, including **Dialectical Behavior Therapy (DBT)**, **Mentalization-Based Treatment (MBT)**, **Schema Therapy**, and **Transference-Focused Psychotherapy (TFP)**. (azzam2024borderlinepersonalitydisorder pages 2-3, azzam2024borderlinepersonalitydisorder pages 9-10, neri2024borderlinepersonalitydisorder pages 1-2)

A narrative review concludes that psychotherapy is the main treatment and “there is no single form of psychotherapy that can fully treat BPD,” but highlights DBT and schema therapy as especially effective for impulsive/self-injurious symptoms and comorbidity management. (neri2024borderlinepersonalitydisorder pages 1-2)

**DBT evidence base (recent synthesis):** a 2024 systematic review of RCTs identified **18 RCTs** (total **1,755 participants**) and reported that trials often target self-injury, suicidal ideation, emergency visits, and hospitalizations; short-term and standard DBT improved suicidality with small-to-moderate effect sizes lasting up to 24 months post-treatment in many studies. ()

**MBT evidence (real-world implementation):** a 2024 naturalistic MBT study (n=46, BPD n=25) found MBT enrollment associated with decreased psychiatric symptoms and improved functioning (all p’s ≤ .01); mentalizing capacity improved (e.g., d=0.68 on TAS; d=1.46 on SCORS), but causal inference is limited due to non-experimental design. (rizzi2024mentalizationbasedtreatment pages 1-2)

### Pharmacotherapy (adjunctive)
Recent reviews emphasize pharmacotherapy as **adjunctive** (symptom-targeted, comorbidity-focused), not a primary treatment for core BPD pathology. Agents commonly used include SSRIs, mood stabilizers, and atypical antipsychotics. (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2)

### Current applications and real-world implementations
* Specialized, manualized psychotherapies require trained clinicians and resources; barriers to access are noted, supporting stepped-care and service design work. (neri2024borderlinepersonalitydisorder pages 1-2, azzam2024borderlinepersonalitydisorder pages 9-10)
* ICD-11 dimensional PD diagnosis is being positioned for broader clinical usability, including adolescence, with the borderline pattern qualifier retained in part to support continuity and identify people likely to benefit from psychotherapy. (pan2024practicalimplicationsof pages 1-2)

### Ongoing and recent clinical trials (ClinicalTrials.gov)
Recent real-world implementations and experimental therapeutics include neuromodulation, neurofeedback, trauma-focused interventions, and pharmacologic proof-of-concept:

* **rTMS (circuit-based, vlPFC–amygdala targeting)**
  * **NCT07197502** (UCLA; recruiting; start 2025-03-01; n=30; randomized single-masked crossover; primary outcomes BSL-23, CGI-BPD, DERS). URL: https://clinicaltrials.gov/study/NCT07197502 (NCT07197502 chunk 1)
  * **NCT07223619** (UCLA; active not recruiting; start 2024; n=20; single-group; individualized vlPFC targeting via resting-state fMRI; tasks include delay discounting and cognitive reappraisal of social exclusion pain). URL: https://clinicaltrials.gov/study/NCT07223619 (NCT07223619 chunk 1)

* **Real-time fMRI neurofeedback (amygdala down-regulation)**
  * **NCT06626789** (BrainSTEADy; planned total n=164; RCT vs sham; includes health-economic outcomes such as QALYs/AQoL-6D). URL: https://clinicaltrials.gov/study/NCT06626789 (NCT06626789 chunk 2)

* **Trauma-focused psychotherapy**
  * **NCT06493708** (EMDR; recruiting; start 2024-10-01; n=56; randomized factorial; primary outcome ZAN-BPD; multiple symptom/regulation measures across 18 weeks). URL: https://clinicaltrials.gov/study/NCT06493708 (NCT06493708 chunk 1)

* **DBT mechanisms / biomarker-rich designs**
  * **NCT06882330** (NeuroDBT; completed; n=106; longitudinal controlled DBT study with clinical outcomes and fMRI/EEG/HRV measures). URL: https://clinicaltrials.gov/study/NCT06882330 (NCT06882330 chunk 1, NCT06882330 chunk 2)

* **Pharmacologic proof-of-concept**
  * **NCT06759298** (methylphenidate/Concerta vs placebo; not yet recruiting; start 2025-01-15; n=60; primary outcomes impulsivity and stress). URL: https://clinicaltrials.gov/study/NCT06759298 (NCT06759298 chunk 1)

* **Adjunctive/feasibility interventions**
  * **NCT07476300** (auricular acupuncture feasibility pilot; not yet recruiting; start 2026-04-15; n=15; NADA protocol). URL: https://clinicaltrials.gov/study/NCT07476300 (NCT07476300 chunk 1)

### Suggested MAXO terms (examples)
MAXO IDs not retrieved directly; suggested actions for curation:
* Dialectical behavior therapy (DBT)
* Mentalization-based therapy (MBT)
* Schema therapy
* Psychodynamic psychotherapy / transference-focused psychotherapy
* Repetitive transcranial magnetic stimulation (rTMS)
* Real-time fMRI neurofeedback
* Eye movement desensitization and reprocessing (EMDR)


## 13. Prevention
Primary prevention is not well-established for BPD in the retrieved evidence. However, ICD-11 and early-intervention literature emphasize earlier identification (including in adolescence) and timely access to evidence-based psychotherapy as a pragmatic prevention strategy for downstream harms (self-harm, hospitalization, chronic disability). (pan2024practicalimplicationsof pages 1-2)


## 14. Other species / natural disease
No naturally occurring “BPD” diagnosis exists in non-human species in the retrieved evidence set; translational relevance is typically via endophenotypes (impulsivity, stress reactivity, social behavior) rather than direct disease homology.


## 15. Model organisms
The retrieved evidence set did not include validated animal models of BPD. Related translational approaches focus on circuits/behaviors (e.g., stress vulnerability, impulsivity) and neuromodulation targets; these are better represented as dimensional constructs rather than a single disease model.


## Summary artifact
The following table compiles high-yield quantitative facts and classification identifiers extracted from the retrieved evidence.

| Topic | Key finding (with numbers) | Source (first author, year) | URL | Evidence type | Citation ID placeholder |
|---|---|---|---|---|---|
| Definition / core features | BPD is characterized by pervasive instability in emotional regulation, self-image, interpersonal relationships, and behavior; core DSM-style features include abandonment fears, unstable idealization/devaluation, identity disturbance, impulsivity, recurrent self-harm/suicidality, chronic emptiness, anger dyscontrol, and transient paranoia/dissociation | Azzam, 2024 | https://doi.org/10.7759/cureus.75893 | Narrative review | (azzam2024borderlinepersonalitydisorder pages 2-3) |
| Prevalence in general population | Reported prevalence is about **1–2%** of the general population; another recent review reports **~1.6%** | Azzam, 2024; Neri, 2024 | https://doi.org/10.7759/cureus.75893 ; https://doi.org/10.22543/2392-7674.1500 | Review | (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2) |
| Prevalence in clinical settings | Reported prevalence rises to **15–20%** in psychiatric settings; review also notes **~20%** in clinical populations, **~10%** of ambulatory patients, and **~25%** of hospitalized patients | Azzam, 2024; Neri, 2024 | https://doi.org/10.7759/cureus.75893 ; https://doi.org/10.22543/2392-7674.1500 | Review | (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2) |
| Sex ratio | Female-to-male ratio reported as approximately **3:1** in clinical samples; a large Swedish cohort found **85.3% female** among diagnosed cases | Azzam, 2024; Tate, 2022 | https://doi.org/10.7759/cureus.75893 ; https://doi.org/10.1038/s41380-022-01503-z | Review; register study | (azzam2024borderlinepersonalitydisorder pages 2-3) |
| Typical onset | Symptoms typically begin in **late adolescence / early adulthood**; one review notes emergence in adolescence, often **after age 12** | Azzam, 2024; Neri, 2024 | https://doi.org/10.7759/cureus.75893 ; https://doi.org/10.22543/2392-7674.1500 | Review | (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2) |
| Suicide mortality | Approximately **10%** of people with BPD may die by suicide; chronic self-harm and suicide attempts are common | Azzam, 2024 | https://doi.org/10.7759/cureus.75893 | Review | (azzam2024borderlinepersonalitydisorder pages 2-3) |
| ICD-11 diagnostic model | ICD-11 replaces categorical PD subtypes with a dimensional model: diagnosis of personality disorder is specified by severity (**mild, moderate, severe**) plus trait domains; clinicians may add a **borderline pattern qualifier** | Mulder, 2021 | https://doi.org/10.3389/fpsyt.2021.655548 | Review / classification commentary | (zheleva2024experiencesofpatients pages 10-15) |
| ICD-11 borderline pattern note | Borderline pattern in ICD-11 is treated as an additional qualifier rather than a standalone disorder category; it maps mainly onto **negative affective, dissocial, and disinhibited** domains | Mulder, 2020 | https://doi.org/10.1177/0004867420951608 | Classification analysis | (zheleva2024experiencesofpatients pages 10-15) |
| Key genetic statistic | In a Swedish population register study of **1,851,755** individuals, **11,665** received a BPD diagnosis; heritability was estimated at **46% (95% CI 39–53)**, with remaining variance explained by individually unique environmental factors | Skoglund, 2021 | https://doi.org/10.1038/s41380-019-0442-0 | Population register study | (zheleva2024experiencesofpatients pages 10-15) |


*Table: This table compiles high-yield identifiers and quantitative disease characteristics for borderline personality disorder, including prevalence, onset, suicide risk, ICD-11 classification notes, and heritability. It is useful as a quick reference for populating structured knowledge-base fields.*


# Key expert/authoritative perspectives (2023–2024 emphasis)
* ICD-11 experts describe the PD model as a major shift: from categorical types to severity+traits, with a retained borderline pattern qualifier largely for continuity with established clinical practice and psychotherapy evidence bases. (mulder2021icd11personalitydisorders pages 2-3, pan2024practicalimplicationsof pages 1-2, mulder2020theborderlinepattern pages 1-2)
* Contemporary clinical reviews consistently position **psychotherapy as first-line** and pharmacotherapy as adjunctive for symptom clusters and comorbidities. (azzam2024borderlinepersonalitydisorder pages 2-3, neri2024borderlinepersonalitydisorder pages 1-2)


# Limitations of this report
* DSM-5 text, ICD-11 official code strings, MeSH/MONDO identifiers, and many HPO/GO/CL/UBERON numeric IDs were not directly retrievable from the current evidence set; ontology term suggestions above are therefore non-cited placeholders for expert curation.
* Biomarker findings (inflammation/HRV/HPA axis) in the retrieved evidence were largely narrative/qualitative without extractable pooled effect sizes. (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9)


References

1. (azzam2024borderlinepersonalitydisorder pages 2-3): Saif Azzam, Rahma Almari, Karees Khattab, Ammar Badr, Arwa R Balawi, Rana Haddad, Rawan Almasri, and Giustino Varrassi. Borderline personality disorder: a comprehensive review of current diagnostic practices, treatment modalities, and key controversies. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75893, doi:10.7759/cureus.75893. This article has 11 citations.

2. (mulder2021icd11personalitydisorders pages 2-3): Roger T. Mulder. Icd-11 personality disorders: utility and implications of the new model. Frontiers in Psychiatry, May 2021. URL: https://doi.org/10.3389/fpsyt.2021.655548, doi:10.3389/fpsyt.2021.655548. This article has 131 citations.

3. (mulder2020theborderlinepattern pages 1-2): Roger T Mulder, L John Horwood, and Peter Tyrer. The borderline pattern descriptor in the international classification of diseases, 11th revision: a redundant addition to classification. Australian & New Zealand Journal of Psychiatry, 54:1095-1100, Sep 2020. URL: https://doi.org/10.1177/0004867420951608, doi:10.1177/0004867420951608. This article has 39 citations and is from a peer-reviewed journal.

4. (pan2024practicalimplicationsof pages 1-2): Bing Pan and Wei Wang. Practical implications of icd-11 personality disorder classifications. BMC Psychiatry, Mar 2024. URL: https://doi.org/10.1186/s12888-024-05640-3, doi:10.1186/s12888-024-05640-3. This article has 27 citations and is from a domain leading peer-reviewed journal.

5. (skoglund2021familialriskand pages 1-2): Charlotte Skoglund, Annika Tiger, Christian Rück, Predrag Petrovic, Philip Asherson, Clara Hellner, David Mataix-Cols, and Ralf Kuja-Halkola. Familial risk and heritability of diagnosed borderline personality disorder: a register study of the swedish population. Molecular Psychiatry, 26:999-1008, Jun 2021. URL: https://doi.org/10.1038/s41380-019-0442-0, doi:10.1038/s41380-019-0442-0. This article has 139 citations and is from a highest quality peer-reviewed journal.

6. (tate2022borderlinepersonalitydisorder pages 1-2): Ashley E. Tate, Hanna Sahlin, Shengxin Liu, Yi Lu, Sebastian Lundström, Henrik Larsson, Paul Lichtenstein, and Ralf Kuja-Halkola. Borderline personality disorder: associations with psychiatric disorders, somatic illnesses, trauma, and adverse behaviors. Molecular Psychiatry, 27:2514-2521, Mar 2022. URL: https://doi.org/10.1038/s41380-022-01503-z, doi:10.1038/s41380-022-01503-z. This article has 77 citations and is from a highest quality peer-reviewed journal.

7. (azzam2024borderlinepersonalitydisorder pages 6-7): Saif Azzam, Rahma Almari, Karees Khattab, Ammar Badr, Arwa R Balawi, Rana Haddad, Rawan Almasri, and Giustino Varrassi. Borderline personality disorder: a comprehensive review of current diagnostic practices, treatment modalities, and key controversies. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75893, doi:10.7759/cureus.75893. This article has 11 citations.

8. (skoglund2021familialriskand pages 2-4): Charlotte Skoglund, Annika Tiger, Christian Rück, Predrag Petrovic, Philip Asherson, Clara Hellner, David Mataix-Cols, and Ralf Kuja-Halkola. Familial risk and heritability of diagnosed borderline personality disorder: a register study of the swedish population. Molecular Psychiatry, 26:999-1008, Jun 2021. URL: https://doi.org/10.1038/s41380-019-0442-0, doi:10.1038/s41380-019-0442-0. This article has 139 citations and is from a highest quality peer-reviewed journal.

9. (gearin2022spotlightonborderline pages 2-2): Priya F. Gearin. Spotlight on borderline personality disorder: history, genetics, and neurobiology. The Brown University Child and Adolescent Behavior Letter, 38:1-4, Aug 2022. URL: https://doi.org/10.1002/cbl.30652, doi:10.1002/cbl.30652. This article has 0 citations.

10. (neri2024borderlinepersonalitydisorder pages 1-2): Marina Neri, Antonino Reitano, Lavinia Rinnone, Antonio Bruno, Fabrizio Turiaco, Felicia Matilde Ferreri, Carmela Mento, Maria Rosaria Anna Muscatello, and Fiammetta Iannuzzo. Borderline personality disorder: a narrative review on effective psychotherapies. Journal of Mind and Medical Sciences, 11:267-276, Oct 2024. URL: https://doi.org/10.22543/2392-7674.1500, doi:10.22543/2392-7674.1500. This article has 1 citations.

11. (kujahalkola2021doborderlinepersonality pages 1-2): Ralf Kuja-Halkola, Kristina Lind Juto, Charlotte Skoglund, Christian Rück, David Mataix-Cols, Ana Pérez-Vigil, Johan Larsson, Clara Hellner, Niklas Långström, Predrag Petrovic, Paul Lichtenstein, and Henrik Larsson. Do borderline personality disorder and attention-deficit/hyperactivity disorder co-aggregate in families? a population-based study of 2 million swedes. Molecular Psychiatry, 26:341-349, Oct 2021. URL: https://doi.org/10.1038/s41380-018-0248-5, doi:10.1038/s41380-018-0248-5. This article has 55 citations and is from a highest quality peer-reviewed journal.

12. (NCT07197502 chunk 1): Andrew F. Leuchter. Treatment of Borderline Personality Disorder With rTMS. University of California, Los Angeles. 2025. ClinicalTrials.gov Identifier: NCT07197502

13. (NCT06626789 chunk 2):  Brain Signal Training to Enhance Affect Down-regulation. Central Institute of Mental Health, Mannheim. 2025. ClinicalTrials.gov Identifier: NCT06626789

14. (bozzatello2024metabolicdysfunctionsdysregulation pages 8-9): Paola Bozzatello, Giacomo Marin, Giulio Gabriele, Claudio Brasso, Paola Rocca, and Silvio Bellino. Metabolic dysfunctions, dysregulation of the autonomic nervous system, and echocardiographic parameters in borderline personality disorder: a narrative review. International Journal of Molecular Sciences, 25:12286, Nov 2024. URL: https://doi.org/10.3390/ijms252212286, doi:10.3390/ijms252212286. This article has 10 citations.

15. (azzam2024borderlinepersonalitydisorder pages 9-10): Saif Azzam, Rahma Almari, Karees Khattab, Ammar Badr, Arwa R Balawi, Rana Haddad, Rawan Almasri, and Giustino Varrassi. Borderline personality disorder: a comprehensive review of current diagnostic practices, treatment modalities, and key controversies. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75893, doi:10.7759/cureus.75893. This article has 11 citations.

16. (rizzi2024mentalizationbasedtreatment pages 1-2): Endang Rizzi, Jonas Gijs Weijers, Coriene ten Kate, and Jean-Paul Selten. Mentalization based treatment for a broad range of personality disorders: a naturalistic study. BMC Psychiatry, Jun 2024. URL: https://doi.org/10.1186/s12888-024-05865-2, doi:10.1186/s12888-024-05865-2. This article has 10 citations and is from a domain leading peer-reviewed journal.

17. (NCT07223619 chunk 1): Andrew F. Leuchter. PILOT Phase: BPD Study. University of California, Los Angeles. 2024. ClinicalTrials.gov Identifier: NCT07223619

18. (NCT06493708 chunk 1): Antonio Vita. Effectiveness of EMDR in Borderline Personality Disorder. Azienda Socio Sanitaria Territoriale degli Spedali Civili di Brescia. 2024. ClinicalTrials.gov Identifier: NCT06493708

19. (NCT06882330 chunk 1):  Neural Mechanisms of Dialectical Behavioral Therapy in Patients with Borderline Personality Disorder. Masarykova Univerzita. 2020. ClinicalTrials.gov Identifier: NCT06882330

20. (NCT06882330 chunk 2):  Neural Mechanisms of Dialectical Behavioral Therapy in Patients with Borderline Personality Disorder. Masarykova Univerzita. 2020. ClinicalTrials.gov Identifier: NCT06882330

21. (NCT06759298 chunk 1): Osama Ibrahim Younes. The Effects of Methylphenidate on Symptomatology in Individuals With Borderline Personality Disorder. Tanta University. 2025. ClinicalTrials.gov Identifier: NCT06759298

22. (NCT07476300 chunk 1): Jenny Gentizon. Pilot Study on Auricular Acupuncture in Hospitalized Adults With Borderline Personality Disorder. Jenny Gentizon. 2026. ClinicalTrials.gov Identifier: NCT07476300

23. (zheleva2024experiencesofpatients pages 10-15): N Zheleva. Experiences of patients with borderline personality disorder in mentalization based psychoeducation groups: a qualitative study. Unknown journal, 2024.