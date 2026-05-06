---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:12:20.783273'
end_time: '2026-05-05T23:25:09.211664'
duration_seconds: 768.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ischemic Stroke
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ischemic Stroke
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ischemic Stroke** covering all of the
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
- **Disease Name:** Ischemic Stroke
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ischemic Stroke** covering all of the
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


# Ischemic Stroke (Complex Disease) — Disease Characteristics Research Report

## Executive summary
Ischemic stroke (IS) is brain tissue infarction due to occlusion of cerebral blood flow (thrombosis/embolism), producing acute focal neurologic deficits and major global disability and mortality burden. Contemporary evidence highlights (i) persistently high absolute global burden despite improvements in age-standardized rates, (ii) hypertension and dyslipidemia (especially high systolic blood pressure and high LDL-cholesterol) as leading modifiable contributors to disability-adjusted life-years (DALYs), and (iii) large, real-world improvements in evidence-based acute care and secondary prevention processes in organized stroke systems (e.g., Get With The Guidelines–Stroke in the US). (zhu2025globalandregional pages 1-5, liu2025globalregionaland pages 1-2, bushnell20242024guidelinefor pages 2-3, li2024globalregionaland pages 1-2, xian2024twentyyearsof pages 3-4)

| Domain | Metric | Value | Population/setting | Year(s) | Source (include DOI URL) | Notes |
|---|---|---:|---|---|---|---|
| Burden | Prevalent ischemic stroke cases | 69,944,884.8 cases | Global; GBD 2021 ischemic stroke estimates | 2021 | Li et al., *eClinicalMedicine* (2024), https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2) | Absolute prevalent case count |
| Burden | Age-standardized prevalence rate (ASPR) | 819.5 per 100,000 | Global; GBD 2021 | 2021 | Li et al., *eClinicalMedicine* (2024), https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2) | 95% UI 760.3–878.7 |
| Burden | Age-standardized incidence rate (ASIR) | 92.4 per 100,000 | Global; GBD 2021 | 2021 | Li et al., *eClinicalMedicine* (2024), https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2) | 95% UI 79.8–105.8 |
| Burden | Age-standardized death rate (ASDR) | 44.2 per 100,000 | Global; GBD 2021 | 2021 | Li et al., *eClinicalMedicine* (2024), https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2) | Mortality rate |
| Burden | Age-standardized DALY rate | 837.4 per 100,000 | Global; GBD 2021 | 2021 | Li et al., *eClinicalMedicine* (2024), https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2) | 95% UI 763.7–905 |
| Prevention | Antihypertensive therapy intensity needed for BP control | ~30% controlled with a single antihypertensive; most required 2–3 medications | Randomized trial evidence summarized in AHA/ASA primary prevention guideline | Evidence summarized through 2024 | Bushnell et al., *Stroke* (2024), https://doi.org/10.1161/STR.0000000000000475 (bushnell20242024guidelinefor pages 2-3) | Supports guideline emphasis on aggressive BP control as a primary stroke-prevention strategy |
| Care quality | Anticoagulation for atrial fibrillation/flutter at discharge | 55.7% → 97.2% | U.S. GWTG-Stroke registry; eligible acute ischemic stroke patients | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 1-2, xian2024twentyyearsof pages 3-4) | Major improvement in secondary prevention quality metric |
| Care quality | Door-to-needle time ≤60 min | 19.0% → 75.3% | U.S. GWTG-Stroke registry; thrombolysis-treated acute ischemic stroke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 1-2, xian2024twentyyearsof pages 3-4) | Time-to-treatment benchmark improved ~4-fold |
| Care quality | Arrive-by-3.5 h / treat-by-4.5 h | 15.2% → 92.9% | U.S. GWTG-Stroke registry; eligible early-arriving acute ischemic stroke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 1-2, xian2024twentyyearsof pages 3-4) | Reflects expansion and uptake of timely IV thrombolysis workflows |
| Care quality | Smoking cessation counseling | 44.7% → 97.8% | U.S. GWTG-Stroke registry; eligible stroke/TIA patients who smoke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 1-2, xian2024twentyyearsof pages 3-4) | Prevention-focused discharge quality measure |
| Care quality | Dysphagia screening | 53.8% → 83.5% | U.S. GWTG-Stroke registry; eligible acute ischemic stroke patients | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 1-2, xian2024twentyyearsof pages 3-4) | Important complication-prevention and safety process measure |
| Care quality | In-hospital mortality for ischemic stroke | 5.8% → 4.2% | U.S. GWTG-Stroke registry; hospitalized ischemic stroke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 4-5) | Risk-adjusted outcomes improved over time |
| Care quality | Discharge to home after ischemic stroke | 44.1% → 50.6% | U.S. GWTG-Stroke registry; hospitalized ischemic stroke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 5-8) | Suggests improved short-term functional/disposition outcomes |
| Care quality | Discharge to skilled nursing facility after ischemic stroke | 20.9% → 13.6% | U.S. GWTG-Stroke registry; hospitalized ischemic stroke | 2003 → 2022 | Xian et al., *Stroke* (2024), https://doi.org/10.1161/STROKEAHA.124.048174 (xian2024twentyyearsof pages 5-8) | Decline consistent with better acute care and discharge outcomes |


*Table: This table compiles recent quantitative ischemic stroke burden estimates and selected prevention/care-quality metrics from major 2024 sources. It is useful for quickly comparing global burden with real-world U.S. improvements in evidence-based stroke care delivery.*

## 1. Disease Information
### 1.1 Definition / overview (current understanding)
Ischemic stroke (also termed *cerebral infarction*) is caused primarily by thrombotic obstruction or embolic occlusion of cerebral vessels, leading to brain ischemia and tissue necrosis/infarction. (zhu2025globalandregional pages 1-5)

A widely used clinical/epidemiologic definition (as used in Global Burden of Disease [GBD] analyses aligned to WHO criteria) describes ischemic stroke as rapidly developing clinical signs of cerebral dysfunction due to occlusion of cerebral blood flow by thrombus/embolus, typically lasting >24 hours or leading to death; GBD also references the tissue-based concept of infarction-driven neurological dysfunction. (liu2025globalregionaland pages 1-2, liu2025epidemiologyandfuture pages 11-12)

### 1.2 Key identifiers (available from retrieved sources)
*This run did not retrieve OMIM/Orphanet/MeSH/ICD records directly; therefore, formal code mappings are not provided here and should be added from ontology resources (e.g., MeSH D-codes; ICD-10 I63.*).*

Identifiers and abbreviations commonly used in the epidemiology literature include: IS (ischemic stroke), DALYs, ASIR (age-standardized incidence rate), ASMR (age-standardized mortality rate), ASDR (age-standardized DALY rate). (zhu2025globalandregional pages 16-19)

### 1.3 Common synonyms / alternative names
- Ischemic stroke (IS) (liu2025globalregionaland pages 1-2)
- Cerebral infarction (zhu2025globalandregional pages 1-5)

### 1.4 Source of information
The evidence synthesized here is primarily from:
- Aggregated, disease-level epidemiologic resources (GBD 2021–based analyses). (li2024globalregionaland pages 1-2, liu2025globalregionaland pages 1-2)
- Aggregated clinical quality-improvement registry data (Get With The Guidelines–Stroke). (xian2024twentyyearsof pages 3-4)
- Evidence-synthesizing clinical guideline documents (AHA/ASA 2024 primary prevention guideline). (bushnell20242024guidelinefor pages 2-3)

## 2. Etiology
### 2.1 Disease causal factors (mechanistic framing)
The proximal cause of ischemic stroke is cerebral blood flow interruption due to intravascular occlusion (thrombus/embolus), leading to ischemia and infarction/necrosis of downstream brain tissue. (zhu2025globalandregional pages 1-5, liu2025globalregionaland pages 1-2)

### 2.2 Risk factors (recent quantitative summaries)
GBD 2021–based analyses consistently identify metabolic/vascular risks as dominant contributors to ischemic stroke burden.
- High systolic blood pressure and high LDL-cholesterol were the leading modifiable contributors to DALYs over 1990–2021 in a GBD 2021 systematic analysis. (liu2025globalregionaland pages 1-2)
- A GBD 2019–based analysis (Neurology, 2023) identified seven major attributable risk factors: smoking and high-sodium diet (behavioral), plus high systolic blood pressure, high LDL cholesterol, kidney dysfunction, high fasting plasma glucose, and high BMI (metabolic). (fan2023globalburdenrisk pages 1-2)

Environmental and behavioral factors are also highlighted in GBD-based syntheses, including air pollution and smoking. (liu2025epidemiologyandfuture pages 11-12, zhu2025globalandregional pages 16-19)

### 2.3 Protective factors
AHA/ASA’s 2024 primary prevention guideline endorses Mediterranean dietary patterns (with nuts and olive oil highlighted in the evidence synthesis) for stroke risk reduction. (bushnell20242024guidelinefor pages 2-3)

### 2.4 Gene–environment interactions
*Not established from the retrieved evidence in this run.* GBD and guideline sources emphasize risk-factor synergy (e.g., metabolic + behavioral risks) but do not provide specific validated gene–environment interaction effect estimates in the extracted passages. (fan2023globalburdenrisk pages 1-2, bushnell20242024guidelinefor pages 2-3)

## 3. Phenotypes
*The present run did not retrieve dedicated phenotype frequency studies or HPO-mapped clinical series; thus, phenotype frequencies and detailed HPO mapping are incomplete.*

### 3.1 Core phenotype concept (high-level)
The defining clinical phenotype is an acute episode of neurological dysfunction due to focal infarction (classically focal deficits corresponding to vascular territory). (liu2025epidemiologyandfuture pages 11-12)

### 3.2 Quality-of-life impact (system-level proxy)
Large registry data show temporal improvements in discharge disposition after ischemic stroke (a proxy for early functional outcome): discharge to home increased from 44.1% (2003) to 50.6% (2022) and discharge to skilled nursing facilities decreased from 20.9% to 13.6% in GWTG-Stroke hospitals. (xian2024twentyyearsof pages 5-8)

### 3.3 Suggested HPO terms (placeholders; not evidence-mapped in this run)
- Hemiparesis (HP:0001269)
- Aphasia (HP:0002381)
- Dysarthria (HP:0001260)
- Dysphagia (HP:0002015)
- Visual field defect (HP:0001123)

*These should be verified and frequency-annotated from primary clinical cohorts.*

## 4. Genetic / Molecular Information
*This run did not retrieve OMIM/ClinVar/HGMD/ClinGen evidence for monogenic stroke syndromes; therefore, causal genes/variants and ACMG classifications are not provided.*

### 4.1 Current understanding (complex genetics)
Ischemic stroke is described as a complex, multifactorial disorder with both environmental and heritable components; epidemiology sources emphasize that GBD-based analyses do not capture all genetic contributors. (fan2023globalburdenrisk pages 1-2, zhu2025globalandregional pages 16-19)

## 5. Environmental Information
### 5.1 Environmental factors
Environmental pollution is repeatedly identified as a major contributor alongside hypertension and LDL-cholesterol in GBD-based ischemic stroke risk-attribution summaries. (zhu2025globalandregional pages 1-5, zhu2025globalandregional pages 12-16)

### 5.2 Lifestyle factors
Lifestyle and metabolic risks highlighted include smoking, high BMI, and high-sodium diet. (fan2023globalburdenrisk pages 1-2)

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (macro-to-micro)
A canonical upstream-to-downstream chain supported by the retrieved evidence is:
1) Thrombotic/embolic occlusion of cerebral blood flow → 2) focal cerebral ischemia → 3) tissue infarction/necrosis → 4) acute neurological dysfunction and disability. (zhu2025globalandregional pages 1-5, liu2025globalregionaland pages 1-2)

### 6.2 Biological processes and cell types (ontology suggestions; limited direct evidence in this run)
Because this run emphasized epidemiology/guidelines, mechanistic molecular pathways (e.g., excitotoxicity, oxidative stress, BBB disruption) were not extracted from primary mechanistic papers here.

Suggested GO biological process terms (to be evidence-validated):
- GO:0006954 inflammatory response
- GO:0008219 cell death
- GO:0006281 DNA repair (secondary injury context)

Suggested CL cell types (to be evidence-validated):
- Microglial cell (CL:0000129)
- Astrocyte (CL:0000127)
- Brain microvascular endothelial cell (CL:2000064)

## 7. Diagnostics
*This run did not retrieve primary imaging guideline text or biomarker performance statistics; diagnostic details should be supplemented from acute stroke guideline documents and radiology literature.*

## 8. Treatment
### 8.1 Real-world implementation and systems of care
The US Get With The Guidelines–Stroke (GWTG-Stroke) registry demonstrates large real-world improvements in evidence-based acute ischemic stroke workflows and secondary prevention processes from 2003–2022, including:
- Anticoagulation for atrial fibrillation/flutter: 55.7% → 97.2%.
- Smoking cessation counseling: 44.7% → 97.8%.
- Dysphagia screening: 53.8% → 83.5%.
- Arrive-by-3.5h/treat-by-4.5h thrombolysis measure: 15.2% → 92.9%.
- Door-to-needle ≤60 min: 19.0% → 75.3%.
These changes occurred across 7,837,849 stroke/TIA admissions from 2,865 hospitals and are presented as sustained improvements across performance measures. (xian2024twentyyearsof pages 3-4, xian2024twentyyearsof pages 1-2)

A figure depicting these temporal trends in key acute ischemic stroke care performance measures is provided in the source paper. (xian2024twentyyearsof media e6f60d86)

### 8.2 MAXO terms (suggested; not formally mapped in this run)
- Thrombolysis (MAXO:0001294)
- Mechanical thrombectomy / endovascular thrombectomy (MAXO term to be confirmed)
- Anticoagulant therapy (MAXO:0000436)
- Antiplatelet therapy (MAXO:0000435)
- Dysphagia screening/intervention (MAXO term to be confirmed)

## 9. Prevention
### 9.1 Primary prevention (AHA/ASA 2024 guideline highlights)
The AHA/ASA 2024 primary prevention guideline organizes prevention around the American Heart Association’s “Life’s Essential 8” domains: diet, physical activity, weight, sleep, blood sugar, blood pressure, lipids, and tobacco. (bushnell20242024guidelinefor pages 2-3)

Selected evidence-based prevention statements extracted from the guideline include:
- Mediterranean diet is endorsed for stroke risk reduction (with nuts and olive oil emphasized in the evidence synthesis), while low-fat diets have shown little impact on stroke risk. (bushnell20242024guidelinefor pages 2-3)
- Sedentary behavior: a new recommendation is to screen for sedentary behavior and counsel patients to avoid prolonged sedentary time. (bushnell20242024guidelinefor pages 2-3)
- Blood pressure: randomized trial evidence summarized indicates single-drug BP control occurred in only ~30% of participants and most required 2–3 medications; accordingly, ≥2 antihypertensive medications are recommended when needed to achieve targets. (bushnell20242024guidelinefor pages 2-3)

### 9.2 Population-health rationale from burden data
Despite declining age-standardized mortality and DALY rates in many regions, absolute ischemic stroke case counts have increased substantially over 1990–2021 due to population growth and aging. (liu2025globalregionaland pages 1-2, zhu2025globalandregional pages 12-16)

## 10. Other Species / Natural Disease
*Not established from retrieved evidence.*

## 11. Model organisms
*This run retrieved some model-system papers but did not extract detailed evidence passages on model recapitulation/limitations.*

## 12. Outcomes / Prognosis
### 12.1 Registry-based short-term outcome trends (US)
In-hospital mortality for ischemic stroke in GWTG-Stroke hospitals declined from 5.8% to 4.2% across 2003–2022, alongside shifting discharge patterns (more direct home discharge, fewer SNF discharges). (xian2024twentyyearsof pages 4-5, xian2024twentyyearsof pages 5-8)

## 13–15. Remaining template elements
Several requested knowledge-base fields (MONDO ID, ICD/MeSH codes, detailed phenotype frequencies with HPO mapping, causal genes/variants with ClinVar/gnomAD allele frequencies, and comprehensive diagnostics/treatment trial effect sizes) were not retrievable from the specific documents accessed in this run. The report should be extended by targeted retrieval from ontology databases (MONDO/MeSH/ICD), clinical guidelines for acute management, and primary genetics/biomarker studies.

## Direct quotes from abstracts (for key statements)
- AHA/ASA 2024 prevention guideline aim: “Ischemic and hemorrhagic strokes lead to significant disability but, most important, are preventable.” (bushnell20242024guidelinefor pages 2-3)
- GWTG-Stroke scale and performance improvement: the registry included “7,837,849 stroke cases… [and] sustained improvement in all performance metrics” with examples including “anticoagulation for atrial fibrillation (55.7% in 2003 to 97.2% in 2022)” and “door-to-needle time within 60 minutes (19.0%–75.3%).” (xian2024twentyyearsof pages 3-4)

## Key URLs and publication dates (from retrieved sources)
- Li et al. “Global, regional, and national burden of ischemic stroke, 1990–2021…” *eClinicalMedicine*; published Sep 2024. https://doi.org/10.1016/j.eclinm.2024.102758 (li2024globalregionaland pages 1-2)
- Bushnell et al. “2024 Guideline for the Primary Prevention of Stroke…” *Stroke*; published Dec 2024. https://doi.org/10.1161/str.0000000000000475 (bushnell20242024guidelinefor pages 2-3)
- Xian et al. “Twenty Years of Sustained Improvement…” *Stroke*; published Nov 2024. https://doi.org/10.1161/strokeaha.124.048174 (xian2024twentyyearsof pages 3-4)



References

1. (zhu2025globalandregional pages 1-5): Weimin Zhu, Xiaxia He, Daochao Huang, Yiqing Jiang, Weijun Hong, Shaofa Ke, En Wang, Feng Wang, Xianwei Wang, Renfei Shan, Suzhi Liu, Yinghe Xu, and Yongpo Jiang. Global and regional burden of ischemic stroke disease from 1990 to 2021: an age-period-cohort analysis. Translational stroke research, Dec 2025. URL: https://doi.org/10.1007/s12975-024-01319-9, doi:10.1007/s12975-024-01319-9. This article has 32 citations and is from a peer-reviewed journal.

2. (liu2025globalregionaland pages 1-2): Sibo Liu, Yanzhao Li, Xiaoyan Lan, Long Wang, Hang Li, Dean Gu, Mengxing Wang, and Jinjie Liu. Global, regional, and national trends in ischaemic stroke burden and risk factors among adults aged 20 + years (1990–2021): a systematic analysis of data from the global burden of disease study 2021 with projections into 2050. Frontiers in Public Health, Apr 2025. URL: https://doi.org/10.3389/fpubh.2025.1567275, doi:10.3389/fpubh.2025.1567275. This article has 23 citations.

3. (bushnell20242024guidelinefor pages 2-3): Cheryl Bushnell, Walter N. Kernan, Anjail Z. Sharrief, Seemant Chaturvedi, John W. Cole, William K. Cornwell, Christine Cosby-Gaither, Sarah Doyle, Larry B. Goldstein, Olive Lennon, Deborah A. Levine, Mary Love, Eliza Miller, Mai Nguyen-Huynh, Jennifer Rasmussen-Winkler, Kathryn M. Rexrode, Nicole Rosendale, Satyam Sarma, Daichi Shimbo, Alexis N. Simpkins, Erica S. Spatz, Lisa R. Sun, Vin Tangpricha, Dawn Turnage, Gabriela Velazquez, and Paul K. Whelton. 2024 guideline for the primary prevention of stroke: a guideline from the american heart association/american stroke association. Stroke, Dec 2024. URL: https://doi.org/10.1161/str.0000000000000475, doi:10.1161/str.0000000000000475. This article has 332 citations and is from a highest quality peer-reviewed journal.

4. (li2024globalregionaland pages 1-2): Xin-yu Li, Xiang-meng Kong, Cheng-hao Yang, Zhi-feng Cheng, Jia-jie Lv, Hong Guo, and Xiao-hong Liu. Global, regional, and national burden of ischemic stroke, 1990–2021: an analysis of data from the global burden of disease study 2021. eClinicalMedicine, 75:102758, Sep 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102758, doi:10.1016/j.eclinm.2024.102758. This article has 309 citations and is from a peer-reviewed journal.

5. (xian2024twentyyearsof pages 3-4): Ying Xian, Shen Li, Tian Jiang, Chandler D. Beon, Remy Poudel, Kathie Thomas, Mathew J. Reeves, Eric E. Smith, Jeffrey L. Saver, Kevin N. Sheth, Steven R. Messé, Lee H. Schwamm, and Gregg C. Fonarow. Twenty years of sustained improvement in quality of care and outcomes for patients hospitalized with stroke or transient ischemic attack: data from the get with the guidelines-stroke program. Stroke, 55:2599-2610, Nov 2024. URL: https://doi.org/10.1161/strokeaha.124.048174, doi:10.1161/strokeaha.124.048174. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (xian2024twentyyearsof pages 1-2): Ying Xian, Shen Li, Tian Jiang, Chandler D. Beon, Remy Poudel, Kathie Thomas, Mathew J. Reeves, Eric E. Smith, Jeffrey L. Saver, Kevin N. Sheth, Steven R. Messé, Lee H. Schwamm, and Gregg C. Fonarow. Twenty years of sustained improvement in quality of care and outcomes for patients hospitalized with stroke or transient ischemic attack: data from the get with the guidelines-stroke program. Stroke, 55:2599-2610, Nov 2024. URL: https://doi.org/10.1161/strokeaha.124.048174, doi:10.1161/strokeaha.124.048174. This article has 23 citations and is from a highest quality peer-reviewed journal.

7. (xian2024twentyyearsof pages 4-5): Ying Xian, Shen Li, Tian Jiang, Chandler D. Beon, Remy Poudel, Kathie Thomas, Mathew J. Reeves, Eric E. Smith, Jeffrey L. Saver, Kevin N. Sheth, Steven R. Messé, Lee H. Schwamm, and Gregg C. Fonarow. Twenty years of sustained improvement in quality of care and outcomes for patients hospitalized with stroke or transient ischemic attack: data from the get with the guidelines-stroke program. Stroke, 55:2599-2610, Nov 2024. URL: https://doi.org/10.1161/strokeaha.124.048174, doi:10.1161/strokeaha.124.048174. This article has 23 citations and is from a highest quality peer-reviewed journal.

8. (xian2024twentyyearsof pages 5-8): Ying Xian, Shen Li, Tian Jiang, Chandler D. Beon, Remy Poudel, Kathie Thomas, Mathew J. Reeves, Eric E. Smith, Jeffrey L. Saver, Kevin N. Sheth, Steven R. Messé, Lee H. Schwamm, and Gregg C. Fonarow. Twenty years of sustained improvement in quality of care and outcomes for patients hospitalized with stroke or transient ischemic attack: data from the get with the guidelines-stroke program. Stroke, 55:2599-2610, Nov 2024. URL: https://doi.org/10.1161/strokeaha.124.048174, doi:10.1161/strokeaha.124.048174. This article has 23 citations and is from a highest quality peer-reviewed journal.

9. (liu2025epidemiologyandfuture pages 11-12): Jiayu Liu, Aoxi Xu, Zhifeng Zhao, Bin Ren, Zhao Gao, Dandong Fang, Bo Hei, Junzhao Sun, Xiangyang Bao, Lin Ma, Xiaoque Zheng, Yuxin Wang, Hecheng Ren, Guan Wang, Li Zhu, and Jianning Zhang. Epidemiology and future trend predictions of ischemic stroke based on the global burden of disease study 1990–2021. Communications Medicine, Jul 2025. URL: https://doi.org/10.1038/s43856-025-00939-y, doi:10.1038/s43856-025-00939-y. This article has 35 citations and is from a peer-reviewed journal.

10. (zhu2025globalandregional pages 16-19): Weimin Zhu, Xiaxia He, Daochao Huang, Yiqing Jiang, Weijun Hong, Shaofa Ke, En Wang, Feng Wang, Xianwei Wang, Renfei Shan, Suzhi Liu, Yinghe Xu, and Yongpo Jiang. Global and regional burden of ischemic stroke disease from 1990 to 2021: an age-period-cohort analysis. Translational stroke research, Dec 2025. URL: https://doi.org/10.1007/s12975-024-01319-9, doi:10.1007/s12975-024-01319-9. This article has 32 citations and is from a peer-reviewed journal.

11. (fan2023globalburdenrisk pages 1-2): Jiahui Fan, Xiaoguang Li, Xueying Yu, Zhenqiu Liu, Yanfeng Jiang, Yibin Fang, Ming Zong, Chen Suo, Qiuhong Man, and Lize Xiong. Global burden, risk factor analysis, and prediction study of ischemic stroke, 1990–2030. Neurology, Jul 2023. URL: https://doi.org/10.1212/wnl.0000000000207387, doi:10.1212/wnl.0000000000207387. This article has 433 citations and is from a highest quality peer-reviewed journal.

12. (zhu2025globalandregional pages 12-16): Weimin Zhu, Xiaxia He, Daochao Huang, Yiqing Jiang, Weijun Hong, Shaofa Ke, En Wang, Feng Wang, Xianwei Wang, Renfei Shan, Suzhi Liu, Yinghe Xu, and Yongpo Jiang. Global and regional burden of ischemic stroke disease from 1990 to 2021: an age-period-cohort analysis. Translational stroke research, Dec 2025. URL: https://doi.org/10.1007/s12975-024-01319-9, doi:10.1007/s12975-024-01319-9. This article has 32 citations and is from a peer-reviewed journal.

13. (xian2024twentyyearsof media e6f60d86): Ying Xian, Shen Li, Tian Jiang, Chandler D. Beon, Remy Poudel, Kathie Thomas, Mathew J. Reeves, Eric E. Smith, Jeffrey L. Saver, Kevin N. Sheth, Steven R. Messé, Lee H. Schwamm, and Gregg C. Fonarow. Twenty years of sustained improvement in quality of care and outcomes for patients hospitalized with stroke or transient ischemic attack: data from the get with the guidelines-stroke program. Stroke, 55:2599-2610, Nov 2024. URL: https://doi.org/10.1161/strokeaha.124.048174, doi:10.1161/strokeaha.124.048174. This article has 23 citations and is from a highest quality peer-reviewed journal.