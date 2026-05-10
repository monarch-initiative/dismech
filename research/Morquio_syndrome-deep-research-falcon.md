---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-05-10T05:44:04.816766'
end_time: '2026-05-10T05:44:04.819341'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Morquio syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Morquio syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Morquio syndrome** covering all of the
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
- **Disease Name:** Morquio syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Morquio syndrome** covering all of the
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


## Comprehensive Research Report: Morquio syndrome (Mucopolysaccharidosis type IV)

### Scope and evidence note
This report synthesizes evidence retrieved via the toolchain (peer‑reviewed articles and ClinicalTrials.gov records). Direct access to OMIM/Orphanet/MeSH/MONDO pages was not available in the retrieved full texts; therefore, several standard identifiers (OMIM disease numbers, Orphanet IDs, MeSH terms, ICD‑10/ICD‑11 codes, MONDO IDs) could not be verified from primary source pages within this run and are explicitly marked as **not available in retrieved evidence**.

A structured summary table suitable for knowledge‑base ingestion is provided below.

| Topic | MPS IVA (Morquio A) | MPS IVB (Morquio B) | Key citations |
|---|---|---|---|
| Subtype / definition | Major Morquio syndrome subtype; lysosomal storage disease with predominant skeletal dysplasia and generally normal intellect | Rarer Morquio subtype; GLB1-related skeletal dysplasia phenotype distinct from GM1 gangliosidosis, usually milder/later-presenting and generally normal intellect | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |
| Causal gene | **GALNS** | **GLB1** | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |
| Deficient enzyme | N-acetylgalactosamine-6-sulfatase (GALNS; EC 3.1.6.4) | β-galactosidase (β-GAL) | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |
| Stored substrates | Keratan sulfate (KS) and chondroitin-6-sulfate (C6S) accumulate, especially in bone/cartilage/ECM | Keratan sulfate accumulates, especially in cartilage and retina | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |
| Inheritance | Autosomal recessive | Autosomal recessive | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, gholamian2024morquiobdisease pages 1-2) |
| Key clinical features | Disproportionate short stature, skeletal dysplasia, platyspondyly, kyphoscoliosis, genu valgum, joint laxity, pectus carinatum, odontoid/cervical instability, tracheal obstruction, corneal clouding, hearing loss; adults often have pain, mobility loss, self-care dependence | Dysostosis multiplex/Morquio dysostosis, disproportionate short stature, atlantoaxial instability, odontoid hypoplasia, platyspondyly, kyphoscoliosis, coxa valga/genu valgum, joint laxity, corneal clouding, hearing loss, dental/cardiopulmonary issues | (quijadafraile2021clinicalfeaturesand pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |
| Key biomarkers / diagnostics | Low GALNS activity in leukocytes/fibroblasts or DBS; molecular confirmation; urinary KS/uGAGs useful but age-dependent; radiographs and multisystem assessment essential; LC-MS/MS supports multiplex/newborn screening workflows | Low leukocyte β-galactosidase activity; GLB1 sequencing; urinary mucopolysaccharides/oligosaccharide abnormalities may support diagnosis; characteristic radiography | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, alsayed2024consensusbasedexpertrecommendations pages 5-6, sawamoto2020mucopolysaccharidosisivadiagnosis pages 20-22, gholamian2024morquiobdisease pages 1-2) |
| Approved disease-modifying therapy | **Elosulfase alfa** IV ERT (2 mg/kg weekly) is approved/standard disease-specific therapy; improves or stabilizes endurance, respiratory outcomes, uKS, and some PROs, but limited effect on bone, eyes, and some airway/cardiac disease | No approved disease-modifying therapy identified in retrieved evidence | (cleary2021impactoflongterm pages 1-2, NCT00884949 chunk 1, magner2022consensusstatementon pages 1-2, crippa2024aglb1transgene pages 1-2) |
| HSCT status | Available in some centers historically, but evidence/guidelines indicate limited skeletal benefit and 2024 Saudi consensus states HSCT is ineffective for MPS IVA | No established role identified in retrieved evidence | (sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, alsayed2024consensusbasedexpertrecommendations pages 6-8) |
| Notable recent (2024) developments | 2024 Saudi consensus: early diagnosis, immediate treatment after counseling, multidisciplinary centers, DBS/LC-MS/MS, pilot newborn screening, home-infusion programs; 2024 AAV9/AAV8 combination gene therapy study in MPS IVA mice delivering GALNS plus CNP for skeletal benefit; 2024 UK case series showed transcervical tracheal resection with partial manubriectomy improved spirometry/QoL in severe airway disease | 2024 preclinical ex vivo HSPC gene therapy work developed an enhanced **GLB1** lentiviral construct with improved enzyme release/cross-correction; 2024 case report detailed orthopedic progression/management in adolescent MPS IVB | (alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 6-8, kenth2024novelapproachfor pages 9-12, kenth2024novelapproachfor pages 1-2, kenth2024novelapproachfor pages 12-13, rintz2024adenoassociatedvirusbasedgene pages 1-2, crippa2024aglb1transgene pages 1-2, crippa2024aglb1transgene pages 14-16, gholamian2024morquiobdisease pages 1-2) |
| Key real-world implementations | England Managed Access Agreement: 55 patients, conditional access with annual review; mean 6MWT rose from 217 m to 244 m after ~4.9 years, FVC/FEV1 from 0.87/0.78 L to 1.05/0.88 L after ~5.5 years; UK specialist airway surgery pathway with AAA 3D planning and MDT selection; regional consensus statements in Europe/Saudi Arabia emphasize multidisciplinary centers and reimbursement/access frameworks | No approved therapy implementation pathway identified; current real-world care is largely symptomatic/orthopedic and multidisciplinary | (cleary2021impactoflongterm pages 1-2, magner2022consensusstatementon pages 1-2, kenth2024novelapproachfor pages 9-12, kenth2024novelapproachfor pages 1-2, kenth2024novelapproachfor pages 4-6, alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 6-8) |
| Epidemiology / prevalence notes | Birth prevalence reported variably by country, e.g., Denmark 1/323,000; UK 1/599,000; Australia 1/926,000; Malaysia 1/1,872,000; broader review range ~1:76,000 to 1:640,000 births | Reported prevalence about 1 in 250,000; incidence estimates ~1/250,000–1,000,000 births | (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2) |


*Table: This table condenses the most actionable structured facts about Morquio syndrome (MPS IV) for knowledge-base ingestion, separating MPS IVA and MPS IVB while highlighting diagnostics, therapy, epidemiology, and 2024 developments. It is designed to support rapid curation with direct context-ID citations.*

---

## 1. Disease information

### 1.1 What is Morquio syndrome?
Morquio syndrome is a lysosomal storage disorder within the mucopolysaccharidoses (MPS) characterized by defective degradation of glycosaminoglycans (GAGs) and prominent skeletal dysplasia. The term commonly encompasses **MPS IVA (Morquio A)** and **MPS IVB (Morquio B)**, which are genetically distinct entities with overlapping skeletal phenotypes. Morquio A is caused by deficiency of **N‑acetylgalactosamine‑6‑sulfatase (GALNS)** leading to keratan sulfate (KS) and chondroitin‑6‑sulfate (C6S) storage, while Morquio B is caused by **β‑galactosidase deficiency due to GLB1 variants**, leading to KS storage (particularly in cartilage and retina). (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2)

### 1.2 Key identifiers (availability in retrieved evidence)
- **OMIM (disease/gene IDs):** Not available in the retrieved evidence for MPS IVA/IVB; one 2024 genetics paper included OMIM IDs for other MPS types but not MPS IV. (zabihi2024identificationofnew pages 1-2)
- **Orphanet ID:** Not available in retrieved evidence.
- **ICD‑10/ICD‑11:** Not available in retrieved evidence.
- **MeSH:** ClinicalTrials.gov records include MeSH condition term “Mucopolysaccharidosis IV” for elosulfase alfa trials/long‑term studies. (NCT01242111 chunk 2)
- **MONDO:** Not available in retrieved evidence.

### 1.3 Synonyms and alternative names
- Morquio syndrome
- Morquio A syndrome; MPS IVA; “Morquio–Brailsford” (Morquio A) (lee2022clinicalutilityof pages 1-2)
- Morquio B disease; MPS IVB (gholamian2024morquiobdisease pages 1-2)

### 1.4 Evidence source type
The information is derived primarily from **aggregated disease‑level resources** (consensus guidelines/reviews and cohorts) and **clinical trial/real‑world datasets**, with additional evidence from **case reports** and **preclinical model studies**. (cleary2021impactoflongterm pages 1-2, alsayed2024consensusbasedexpertrecommendations pages 5-6, kenth2024novelapproachfor pages 9-12, gholamian2024morquiobdisease pages 1-2, rintz2024adenoassociatedvirusbasedgene pages 1-2, crippa2024aglb1transgene pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic/biochemical cause (Mendelian):**
- **MPS IVA (Morquio A):** autosomal recessive lysosomal enzyme deficiency of **GALNS** causing impaired degradation of **KS and C6S**. (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)
- **MPS IVB (Morquio B):** autosomal recessive **GLB1** mutations causing **β‑galactosidase** deficiency and **KS** accumulation; GLB1 deficiency can also cause GM1 gangliosidosis, while Morquio B represents a primarily skeletal/retinal phenotype. (gholamian2024morquiobdisease pages 1-2, crippa2024aglb1transgene pages 1-2)

### 2.2 Risk factors
- **Carrier status and family history** in an autosomal recessive disorder; no environmental triggers are required.
- **Consanguinity** is highlighted by Saudi experts as a driver of higher local prevalence for MPS IVa and VI in Saudi Arabia. (alsayed2024consensusbasedexpertrecommendations pages 2-4)

### 2.3 Protective factors
No validated genetic “protective variants” or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No specific gene–environment interaction evidence was identified in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (MPS IVA emphasized)
Morquio A exhibits a phenotypic continuum (classical to non‑classical). In an adult Spanish cohort (n=33), phenotypes were **54.5% classical**, **33.3% intermediate**, and **12.1% non‑classical**. (quijadafraile2021clinicalfeaturesand pages 1-2)

Key manifestations in this adult cohort (frequencies):
- **Hearing loss:** 75.7% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Ligamentous laxity:** 72.7% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Odontoid dysplasia:** 69.7% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Limb deformities requiring orthopaedic aids (e.g., hip dysplasia, genu valgum):** 63.6% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Corneal clouding:** 60.6% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Obstructive sleep apnea/hypopnea syndrome (OSAHS):** 36.0% (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Need for non‑invasive ventilation:** 33.3% (quijadafraile2021clinicalfeaturesand pages 1-2)

Functional/quality‑of‑life impact in adults:
- ~80% had mobility problems; 36.4% used a wheelchair at all times; 87.9% needed help with self‑care; 33.3% were fully dependent; 78.8% had pain. (quijadafraile2021clinicalfeaturesand pages 1-2)

Morquio A skeletal phenotype and clinical suspicion often arise from radiographic skeletal dysplasia in the preschool years, with progressive multisystem involvement. (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)

### 3.2 Morquio B (MPS IVB) phenotypes
Morquio B is typically milder and later‑presenting than GM1 gangliosidosis, with generally normal cognition. In a 2024 case report, classic “Morquio dysostosis multiplex” radiographic findings were present, with progressive deterioration of walking in adolescence due to joint instability and pain; biochemical testing showed reduced leukocyte β‑galactosidase activity (12.3 nmol/h/mg protein) and elevated urinary mucopolysaccharides (18 mg/mmol). (gholamian2024morquiobdisease pages 1-2)

### 3.3 Suggested HPO terms (non‑exhaustive; mapped to phenotypes in retrieved evidence)
- Short stature, disproportionate (HP:0003510)
- Kyphoscoliosis (HP:0008453)
- Genu valgum (HP:0002857)
- Hip dysplasia (HP:0001385)
- Joint laxity (HP:0001382)
- Odontoid hypoplasia/dysplasia (HP:0011817)
- Cervical spinal stenosis / spinal cord compression (HP:0003416)
- Pectus carinatum (HP:0000768)
- Corneal clouding (HP:0007957)
- Hearing impairment (HP:0000365)
- Obstructive sleep apnea (HP:0010535)
- Pain (HP:0012531)

### 3.4 Anatomy affected (high‑level)
Primary involvement: skeletal system (spine, hips, long bones, growth plates), airway (trachea), and connective tissues; secondary involvement includes cardiopulmonary and ENT systems. (quijadafraile2021clinicalfeaturesand pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3, kenth2024novelapproachfor pages 1-2)

Suggested UBERON examples: growth plate cartilage (UBERON:0001988), trachea (UBERON:0003126), vertebral column (UBERON:0001130), cornea (UBERON:0000964).

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **GALNS** → MPS IVA (Morquio A) (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)
- **GLB1** → MPS IVB (Morquio B) (crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2)

### 4.2 Pathogenic variants and variant classes
**MPS IVA (GALNS):** broad allelic heterogeneity; one 2022 review reports ClinVar counts (as of Aug 2021) and notes numerous pathogenic/likely pathogenic variants. (lee2022clinicalutilityof pages 1-2)

**MPS IVB (GLB1):** recurrent variants associated with Morquio B skeletal phenotypes include **p.Tyr83His, p.Thr500Ala, p.Trp273Leu**, and a case report described a compound genotype **W273L/N484K**. (crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2)

### 4.3 Functional consequences
Both subtypes are consistent with **loss‑of‑function enzyme deficiency**, leading to lysosomal accumulation of incompletely degraded substrates (KS ± C6S). (lee2022clinicalutilityof pages 1-2, crippa2024aglb1transgene pages 1-2)

### 4.4 Modifier/protective genes and epigenetics
No validated modifier genes, protective alleles, or epigenetic signatures specific to Morquio syndrome were identified in the retrieved evidence.

---

## 5. Environmental information
Morquio syndrome is a genetic lysosomal storage disorder; no environmental causes were identified. Population‑level factors such as **consanguinity** influence observed prevalence in some regions. (alsayed2024consensusbasedexpertrecommendations pages 2-4)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current understanding)
A 2024 mechanistic synthesis of mucopolysaccharidoses describes a general cascade:
1) **Primary storage:** lysosomal enzyme deficiency → progressive GAG accumulation.
2) **Organelle dysfunction:** disruption of lysosomal function, impaired autophagy, and mitochondrial dysfunction.
3) **Downstream stress and inflammation:** increased oxidative stress and activation of innate immunity/inflammation.
4) **Tissue damage:** progressive organ damage and cell death manifesting as skeletal dysplasia and (in many MPS types) CNS impairment.
(ago2024molecularmechanismsin pages 1-2)

For Morquio (MPS IV), the stored substrates (KS/C6S) preferentially affect cartilage and growth plates, contributing to a distinct skeletal dysplasia pattern (e.g., platyspondyly and anterior beaking). (ago2024molecularmechanismsin pages 7-9)

### 6.2 Key pathways and processes (suggested GO terms)
Based on 2024 synthesis, relevant processes include:
- Lysosome organization/function (GO:0007040)
- Autophagy / mitophagy (GO:0006914; GO:0000422)
- Oxidative stress response (GO:0006979)
- Innate immune response / NF‑κB signaling (GO:0045087; GO:0043122)
- Inflammasome complex activation (GO:1902552)
(ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 11-14, ago2024molecularmechanismsin pages 7-9)

### 6.3 Cell types (suggested CL terms)
- Chondrocyte (CL:0000138)
- Osteoblast (CL:0000062)
- Osteoclast (CL:0000092)
- Macrophage / microglia (CL:0000235; CL:0000129)
(ago2024molecularmechanismsin pages 2-3, crippa2024aglb1transgene pages 14-16)

### 6.4 Implications for therapeutic delivery
The 2024 review emphasizes that conventional IV ERT has limited impact on **bone/cartilage** and does not address **BBB‑restricted compartments**, motivating approaches such as receptor‑mediated transcytosis (“molecular Trojan horses”) for CNS delivery and bone‑targeting strategies. (ago2024molecularmechanismsin pages 11-14, ago2024molecularmechanismsin pages 2-3)

---

## 7. Anatomical structures affected
- **Skeletal system:** vertebrae, growth plates, hips, long bones; cervical spine/odontoid region. (quijadafraile2021clinicalfeaturesand pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)
- **Respiratory/airway:** trachea with multilevel pathology (tracheomalacia, stenosis, tortuosity/buckling). (kenth2024novelapproachfor pages 1-2)
- **Eye:** corneal clouding. (quijadafraile2021clinicalfeaturesand pages 1-2)
- **Ear/ENT:** hearing loss. (quijadafraile2021clinicalfeaturesand pages 1-2)

Subcellular: lysosome (GO:0005764) as primary site of storage pathology (ago2024molecularmechanismsin pages 1-2).

---

## 8. Temporal development

### 8.1 Onset
Neonates may appear normal; disease is often suspected in early childhood when skeletal abnormalities and radiographic dysplasia become apparent. Attenuated forms can present later and survive into adulthood. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)

### 8.2 Progression
Progressive course with worsening skeletal deformity, mobility limitation, pain, and cardiopulmonary/airway complications. End‑stage airway obstruction can become life‑threatening in severe Morquio A. (quijadafraile2021clinicalfeaturesand pages 1-2, kenth2024novelapproachfor pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
Autosomal recessive for both MPS IVA and MPS IVB. (lee2022clinicalutilityof pages 1-2, gholamian2024morquiobdisease pages 1-2)

### 9.2 Epidemiology
Reported birth prevalence for MPS IVA varies widely by country. A 2022 review provides examples: Denmark **1/323,000**, UK **1/599,000**, Australia **1/926,000**, Malaysia **1/1,872,000**. A 2020 review gives a broader prevalence range of ~**1:76,000 to 1:640,000** births. (lee2022clinicalutilityof pages 1-2, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)

For MPS IVB, a 2024 gene‑therapy development paper cites prevalence ~**1 in 250,000** and carrier frequency ~**1 in 250**, while a 2024 case report cites incidence estimates **~1/250,000–1,000,000** births. (crippa2024aglb1transgene pages 1-2, gholamian2024morquiobdisease pages 1-2)

### 9.3 Population considerations
Saudi experts highlight higher‑than‑average prevalence in Saudi Arabia attributed to high consanguinity rates, motivating registry and screening initiatives. (alsayed2024consensusbasedexpertrecommendations pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical and biochemical testing
**MPS IVA:** diagnosis generally requires demonstration of low **GALNS activity** (leukocytes/fibroblasts; DBS can be used as an initial/remote sample) plus molecular confirmation; urinary KS is a biomarker but declines with age so requires age‑appropriate interpretation. (lee2022clinicalutilityof pages 1-2, akyol2019recommendationsforthe pages 1-2)

**MPS IVB:** reduced leukocyte **β‑galactosidase activity** and GLB1 sequencing; supportive urinary testing may include elevated mucopolysaccharides and abnormal oligosaccharide electrophoresis. (gholamian2024morquiobdisease pages 1-2)

### 10.2 Biomarkers and advanced assays / screening
A 2024 Saudi consensus notes dried blood spot (DBS) assays and **LC‑MS/MS** as precise methods suitable for multiplex newborn screening; the panel recommends piloting newborn screening initiatives and improving access to molecular testing. (alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 2-4)

A 2020 MPS IVA review describes LC‑MS/MS and other quantitative assays for KS and related biomarkers (including di‑sulfated KS and C6S) and discusses pilot newborn screening approaches. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 20-22)

### 10.3 Imaging and functional testing
Radiographic skeletal dysplasia drives suspicion, and severe airway disease requires dedicated assessment. A 2024 UK surgical series used advanced CT‑based “Advanced Airway Analytics” with 3D reconstruction/virtual endoscopy to quantify narrowing and plan interventions. (kenth2024novelapproachfor pages 8-9)

### 10.4 Differential diagnosis
Not exhaustively retrievable within this run; in practice includes other skeletal dysplasias and other MPS subtypes with overlapping dysostosis multiplex.

---

## 11. Outcome / prognosis

### 11.1 Morbidity and function
Adult cohort data show substantial disability and pain burden (mobility impairment, wheelchair dependence, self‑care dependence) and reduced HRQoL, requiring multidisciplinary care. (quijadafraile2021clinicalfeaturesand pages 1-2)

### 11.2 Survival and mortality
Specific survival curves or life expectancy estimates were not retrieved in the available evidence set.

### 11.3 Real‑world outcomes with therapy (disease‑modifying and interventional)

**Elosulfase alfa (ERT) in England managed access agreement (real‑world):**
- 55 patients; mean 6‑minute walk test increased from **217 m to 244 m** after mean follow‑up **4.9 years**.
- Mean FVC/FEV1 improved from **0.87/0.78 L** to **1.05/0.88 L** after mean follow‑up **5.5 years**.
- Patient‑reported outcomes showed improvements in mobility/self‑care domains and relatively stable QoL. (cleary2021impactoflongterm pages 1-2)

**Severe airway obstruction surgery (2024 UK case series):**
Seven adolescents underwent transcervical tracheal resection with partial manubriectomy, reporting spirometric improvement and QoL gains. Pre‑ and post‑operative spirometry values for each subject are summarized in Table 3 (image evidence). (kenth2024novelapproachfor pages 1-2, kenth2024novelapproachfor pages 12-13, kenth2024novelapproachfor media 9eafb273)

---

## 12. Treatment

### 12.1 Pharmacotherapy: enzyme replacement therapy (ERT)
**Elosulfase alfa** (recombinant GALNS) is the principal approved disease‑specific therapy for **MPS IVA**, administered IV (commonly 2 mg/kg weekly). Clinical reviews note improvements in endurance and respiratory outcomes versus placebo and reduction in urinary GAGs/KS. (lee2022clinicalutilityof pages 1-2, NCT00884949 chunk 1)

**Limitations:** 2024 Saudi experts emphasize ERT requires weekly costly infusions and has limited efficacy for ocular, skeletal, and some cardiac manifestations, supporting early initiation and improved care models. (alsayed2024consensusbasedexpertrecommendations pages 2-4)

Real‑world long‑term stabilization/improvement is supported by the England managed access dataset. (cleary2021impactoflongterm pages 1-2)

### 12.2 Surgical/interventional and supportive care
Airway disease can progress to life‑threatening obstruction. In 2024, a UK MDT implemented a transcervical tracheal resection approach avoiding cardiopulmonary bypass, demonstrating meaningful spirometric improvement and improved patient‑reported QoL (PedsQL domains). (kenth2024novelapproachfor pages 1-2, kenth2024novelapproachfor pages 12-13, kenth2024novelapproachfor media 9eafb273)

### 12.3 HSCT
A 2024 Saudi consensus states **HSCT is ineffective for MPS IVa**. Earlier reviews note HSCT availability but limited skeletal impact and significant risks. (alsayed2024consensusbasedexpertrecommendations pages 6-8, sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3)

### 12.4 Emerging / experimental therapies (prioritize 2023–2024)

**MPS IVA—AAV gene therapy (preclinical; 2024):**
A 2024 Molecular Therapy – Nucleic Acids study tested systemic AAV delivery of **GALNS** together with a growth‑associated gene **NPPC/CNP** in MPS IVA mice. The rationale is that enzyme delivery alone may not sufficiently correct avascular growth‑plate cartilage; combining enzyme restoration with growth‑plate signaling may improve skeletal outcomes. The study reports increased GALNS activity in multiple tissues (including bone) and bone growth effects, but also highlights dose‑related adverse effects with high‑dose CNP. (rintz2024adenoassociatedvirusbasedgene pages 1-2)

**MPS IVB—ex vivo HSPC gene therapy (preclinical; 2024):**
A 2024 Methods & Clinical Development paper developed an enhanced GLB1/β‑galactosidase approach for ex vivo lentiviral HSPC gene therapy, addressing instability/poor extracellular release of human β‑GAL. Supernatants from LV‑enhGLB1‑transduced myeloid cells/osteoclasts corrected patient fibroblasts, supporting further development. (crippa2024aglb1transgene pages 14-16)

**Innovative delivery platforms (broader MPS; 2024 synthesis):**
A 2024 mechanistic review highlights receptor‑mediated BBB transport (“molecular Trojan horses”) and bone‑targeting enzyme strategies as key directions for MPS therapies, relevant to Morquio’s bone‑dominant pathology. (ago2024molecularmechanismsin pages 11-14, ago2024molecularmechanismsin pages 2-3)

### 12.5 Clinical trials (selected; ClinicalTrials.gov)
Key elosulfase alfa trials include:
- Phase 1/2 study of BMN‑110 (elosulfase alfa): **NCT00884949** (NCT00884949 chunk 1)
- Long‑term efficacy/safety study: **NCT01242111** (NCT01242111 chunk 2)

---

## 13. Prevention
Because Morquio syndrome is autosomal recessive, prevention focuses on genetic services and early detection rather than exposure modification.

**Secondary prevention (early detection):** Saudi experts recommend piloting **newborn screening** initiatives and improving DBS/LC‑MS/MS workflows, paired with confirmatory enzyme/molecular testing. (alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 2-4)

**Primary prevention (genetic counseling):** The 2024 Saudi consensus recommends **premarital screening** and enhanced genetic counseling for families with known MPS history, reflecting population risk from consanguinity. (alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 6-8)

---

## 14. Other species / natural disease
No evidence of naturally occurring Morquio syndrome in non‑human species (companion animals/wildlife) was retrieved in this run.

---

## 15. Model organisms

### 15.1 MPS IVA models
- **Mouse models:** used for substrate‑degradation enzyme therapy and AAV gene transfer; reduction in circulating KS and improved bone pathology have been demonstrated in preclinical interventions. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 11-13)
- **Cellular models:** human MPS IVA fibroblasts and murine MPS IVA chondrocytes have been used to test AAV vectors and assess GALNS activity and chondrocyte pathology. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 11-13)
- **AAV gene therapy in mice (2024):** combination AAV‑GALNS and AAV‑NPPC/CNP to address skeletal growth plate pathology. (rintz2024adenoassociatedvirusbasedgene pages 1-2)

### 15.2 MPS IVB models
- Ex vivo HSPC models, differentiated myeloid cells/osteoclasts/osteoblasts, and patient fibroblast cross‑correction assays; preliminary use of **Glb1−/− mouse BM HSPCs** for testing enhanced enzyme constructs. (crippa2024aglb1transgene pages 14-16)

---

## Expert opinions and implementation analysis (2024)
A 2024 Saudi Delphi‑based consensus emphasizes implementation gaps and recommends: multidisciplinary centers of excellence, periodic training, national registries, improved access to enzyme and molecular testing, piloting newborn screening using LC‑MS/MS, and developing **home‑infusion programs** for ERT to improve adherence and reduce logistical barriers. (alsayed2024consensusbasedexpertrecommendations pages 5-6, alsayed2024consensusbasedexpertrecommendations pages 6-8, alsayed2024consensusbasedexpertrecommendations pages 2-4)

---

## Required abstract quotes (direct excerpts)
- 2024 mechanistic synthesis (MPS pathophysiology cascade): “At the initial stage of GAG accumulation, affected tissues/cells are reversibly affected but progress irreversibly to: (1) disruption of substrate degradation with pathogenic changes in lysosomal function, (2) cellular dysfunction, secondary/tertiary accumulation … and inflammatory process, and (3) progressive tissue/organ damage and cell death (e.g., skeletal dysplasia, CNS impairment, etc.).” (ago2024molecularmechanismsin pages 1-2)
- 2024 Morquio B case report: “Mucopolysaccharidosis IV type B, or Morquio B disease (MBD), is an autosomal recessive disorder caused by a genetic mutation in GLB1 gene encoding for β-galactosidase…” (gholamian2024morquiobdisease pages 1-2)

---

## URLs and publication dates (examples of key 2024 sources)
- AlSayed et al. “Consensus-based expert recommendations on the management of MPS IVa and VI in Saudi Arabia.” Orphanet J Rare Dis. **July 2024**. https://doi.org/10.1186/s13023-024-03237-3 (alsayed2024consensusbasedexpertrecommendations pages 2-4)
- Kenth et al. “Novel approach for tracheal resection in Morquio a syndrome…” Orphanet J Rare Dis. **July 2024**. https://doi.org/10.1186/s13023-024-03253-3 (kenth2024novelapproachfor pages 1-2)
- Rintz et al. “Adeno-associated virus-based gene therapy…” Mol Ther Nucleic Acids. **June 2024**. https://doi.org/10.1016/j.omtn.2024.102211 (rintz2024adenoassociatedvirusbasedgene pages 1-2)
- Crippa et al. “A GLB1 transgene with enhanced therapeutic potential…” Mol Ther Methods Clin Dev. **September 2024**. https://doi.org/10.1016/j.omtm.2024.101313 (crippa2024aglb1transgene pages 1-2)
- Ago et al. “Molecular Mechanisms in Pathophysiology of Mucopolysaccharidosis…” IJMS. **January 2024**. https://doi.org/10.3390/ijms25021113 (ago2024molecularmechanismsin pages 1-2)

---

## Evidence gaps (for knowledge base curation)
- Standard identifiers (OMIM/Orphanet/ICD/MONDO) were not retrievable directly; they should be added from authoritative databases.
- Survival/life expectancy statistics were not captured in the retrieved set.
- Detailed newborn screening performance metrics (sensitivity/PPV) and long-term outcomes from NBS implementation were not available in retrieved evidence.
- Naturally occurring animal disease evidence was not retrieved.


References

1. (lee2022clinicalutilityof pages 1-2): Chung-Lin Lee, C. Chuang, Huei-Ching Chiu, Ru-Yi Tu, Yun-Ting Lo, Ya-Hui Chang, Shuan-Pei Lin, and Hsiang-Yu Lin. Clinical utility of elosulfase alfa in the treatment of morquio a syndrome. Drug Design, Development and Therapy, 16:143-154, Jan 2022. URL: https://doi.org/10.2147/dddt.s219433, doi:10.2147/dddt.s219433. This article has 16 citations.

2. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 1-3): Kazuki Sawamoto, José Álvarez González, Matthew Piechnik, Francisco Otero, Maria Couce, Yasuyuki Suzuki, and Shunji Tomatsu. Mucopolysaccharidosis iva: diagnosis, treatment, and management. International Journal of Molecular Sciences, 21:1517, Feb 2020. URL: https://doi.org/10.3390/ijms21041517, doi:10.3390/ijms21041517. This article has 160 citations.

3. (crippa2024aglb1transgene pages 1-2): Stefania Crippa, Gaia Alberti, Laura Passerini, Evelyn Oliva Savoia, Marilena Mancino, Giada De Ponti, Ludovica Santi, Margherita Berti, Marialuisa Testa, Raisa Jofra Hernandez, Pamela Quaranta, Selene Ceriotti, Ilaria Visigalli, Amelia Morrone, Antonella Paoli, Claudia Forni, Serena Scala, Massimo Degano, Leopoldo Staiano, Silvia Gregori, Alessandro Aiuti, and Maria Ester Bernardo. A glb1 transgene with enhanced therapeutic potential for the preclinical development of ex-vivo gene therapy to treat mucopolysaccharidosis type ivb. Molecular Therapy - Methods &amp; Clinical Development, 32:101313, Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101313, doi:10.1016/j.omtm.2024.101313. This article has 4 citations.

4. (gholamian2024morquiobdisease pages 1-2): Tara Gholamian, Harpreet Chhina, Sylvia Stockler, and Anthony Cooper. Morquio b disease: a case report. Frontiers in Pediatrics, Mar 2024. URL: https://doi.org/10.3389/fped.2024.1285414, doi:10.3389/fped.2024.1285414. This article has 3 citations.

5. (quijadafraile2021clinicalfeaturesand pages 1-2): Pilar Quijada-Fraile, Elena Arranz Canales, Elena Martín-Hernández, María Juliana Ballesta-Martínez, Encarna Guillén-Navarro, Guillem Pintos-Morell, Marc Moltó-Abad, David Moreno-Martínez, Salvador García Morillo, Javier Blasco-Alonso, María Luz Couce, Ricardo Gil Sánchez, Elisenda Cortès-Saladelafont, Mónica A. López Rodríguez, María Teresa García-Silva, and Montserrat Morales Conejo. Clinical features and health-related quality of life in adult patients with mucopolysaccharidosis iva: the spanish experience. Orphanet Journal of Rare Diseases, Nov 2021. URL: https://doi.org/10.1186/s13023-021-02074-y, doi:10.1186/s13023-021-02074-y. This article has 16 citations and is from a peer-reviewed journal.

6. (alsayed2024consensusbasedexpertrecommendations pages 5-6): Moeenaldeen AlSayed, Dia Arafa, Huda Al-Khawajha, Manal Afqi, Nouriya Al-Sanna’a, Rawda Sunbul, and Maha Faden. Consensus-based expert recommendations on the management of mps iva and vi in saudi arabia. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03237-3, doi:10.1186/s13023-024-03237-3. This article has 3 citations and is from a peer-reviewed journal.

7. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 20-22): Kazuki Sawamoto, José Álvarez González, Matthew Piechnik, Francisco Otero, Maria Couce, Yasuyuki Suzuki, and Shunji Tomatsu. Mucopolysaccharidosis iva: diagnosis, treatment, and management. International Journal of Molecular Sciences, 21:1517, Feb 2020. URL: https://doi.org/10.3390/ijms21041517, doi:10.3390/ijms21041517. This article has 160 citations.

8. (cleary2021impactoflongterm pages 1-2): Maureen Cleary, James Davison, Rachel Gould, Tarekegn Geberhiwot, Derralynn Hughes, Jean Mercer, Alexandra Morrison, Elaine Murphy, Saikat Santra, James Jarrett, Swati Mukherjee, and Karolina M. Stepien. Impact of long-term elosulfase alfa treatment on clinical and patient-reported outcomes in patients with mucopolysaccharidosis type iva: results from a managed access agreement in england. Orphanet Journal of Rare Diseases, Jan 2021. URL: https://doi.org/10.1186/s13023-021-01675-x, doi:10.1186/s13023-021-01675-x. This article has 27 citations and is from a peer-reviewed journal.

9. (NCT00884949 chunk 1):  A Study to Evaluate the Safety, Tolerability and Efficacy of BMN 110 in Subjects With Mucopolysaccharidosis IVA. BioMarin Pharmaceutical. 2009. ClinicalTrials.gov Identifier: NCT00884949

10. (magner2022consensusstatementon pages 1-2): Martin Magner, Zsuzsanna Almássy, Zoran Gucev, Beata Kieć-Wilk, Vasilica Plaiasu, Anna Tylki-Szymańska, Dimitrios Zafeiriou, Ioannis Zaganas, and Christina Lampe. Consensus statement on enzyme replacement therapy for mucopolysaccharidosis iva in central and south-eastern european countries. Orphanet Journal of Rare Diseases, May 2022. URL: https://doi.org/10.1186/s13023-022-02332-7, doi:10.1186/s13023-022-02332-7. This article has 11 citations and is from a peer-reviewed journal.

11. (alsayed2024consensusbasedexpertrecommendations pages 6-8): Moeenaldeen AlSayed, Dia Arafa, Huda Al-Khawajha, Manal Afqi, Nouriya Al-Sanna’a, Rawda Sunbul, and Maha Faden. Consensus-based expert recommendations on the management of mps iva and vi in saudi arabia. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03237-3, doi:10.1186/s13023-024-03237-3. This article has 3 citations and is from a peer-reviewed journal.

12. (kenth2024novelapproachfor pages 9-12): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

13. (kenth2024novelapproachfor pages 1-2): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

14. (kenth2024novelapproachfor pages 12-13): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

15. (rintz2024adenoassociatedvirusbasedgene pages 1-2): Estera Rintz, Betul Celik, Nidhi Fnu, Angélica María Herreño-Pachón, Shaukat Khan, Eliana Benincore-Flórez, and Shunji Tomatsu. Adeno-associated virus-based gene therapy delivering combinations of two growth-associated genes to mps iva mice. Molecular Therapy - Nucleic Acids, 35:102211, Jun 2024. URL: https://doi.org/10.1016/j.omtn.2024.102211, doi:10.1016/j.omtn.2024.102211. This article has 2 citations.

16. (crippa2024aglb1transgene pages 14-16): Stefania Crippa, Gaia Alberti, Laura Passerini, Evelyn Oliva Savoia, Marilena Mancino, Giada De Ponti, Ludovica Santi, Margherita Berti, Marialuisa Testa, Raisa Jofra Hernandez, Pamela Quaranta, Selene Ceriotti, Ilaria Visigalli, Amelia Morrone, Antonella Paoli, Claudia Forni, Serena Scala, Massimo Degano, Leopoldo Staiano, Silvia Gregori, Alessandro Aiuti, and Maria Ester Bernardo. A glb1 transgene with enhanced therapeutic potential for the preclinical development of ex-vivo gene therapy to treat mucopolysaccharidosis type ivb. Molecular Therapy - Methods &amp; Clinical Development, 32:101313, Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101313, doi:10.1016/j.omtm.2024.101313. This article has 4 citations.

17. (kenth2024novelapproachfor pages 4-6): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

18. (zabihi2024identificationofnew pages 1-2): Rezvan Zabihi, Mina Zamani, Majid Aminzadeh, Niloofar Chamanrou, Fatemeh Zahra Kiani, Tahere Seifi, Jawaher Zeighami, Tahere Yadegari, Alireza Sedaghat, Alihossein Saberi, Mohammad Hamid, Gholamreza Shariati, and Hamid Galehdari. Identification of new variants in patients with mucopolysaccharidosis in consanguineous iranian families. Frontiers in Genetics, Feb 2024. URL: https://doi.org/10.3389/fgene.2024.1343094, doi:10.3389/fgene.2024.1343094. This article has 2 citations and is from a peer-reviewed journal.

19. (NCT01242111 chunk 2):  A Study to Evaluate the Long-Term Efficacy and Safety of BMN 110 in Patients With Mucopolysaccharidosis IVA (Morquio A Syndrome). BioMarin Pharmaceutical. 2010. ClinicalTrials.gov Identifier: NCT01242111

20. (alsayed2024consensusbasedexpertrecommendations pages 2-4): Moeenaldeen AlSayed, Dia Arafa, Huda Al-Khawajha, Manal Afqi, Nouriya Al-Sanna’a, Rawda Sunbul, and Maha Faden. Consensus-based expert recommendations on the management of mps iva and vi in saudi arabia. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03237-3, doi:10.1186/s13023-024-03237-3. This article has 3 citations and is from a peer-reviewed journal.

21. (ago2024molecularmechanismsin pages 1-2): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 33 citations.

22. (ago2024molecularmechanismsin pages 7-9): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 33 citations.

23. (ago2024molecularmechanismsin pages 11-14): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 33 citations.

24. (ago2024molecularmechanismsin pages 2-3): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 33 citations.

25. (akyol2019recommendationsforthe pages 1-2): Mehmet Umut Akyol, Tord D. Alden, Hernan Amartino, Jane Ashworth, Kumar Belani, Kenneth I. Berger, Andrea Borgo, Elizabeth Braunlin, Yoshikatsu Eto, Jeffrey I. Gold, Andrea Jester, Simon A. Jones, Cengiz Karsli, William Mackenzie, Diane Ruschel Marinho, Andrew McFadyen, Jim McGill, John J. Mitchell, Joseph Muenzer, Torayuki Okuyama, Paul J. Orchard, Bob Stevens, Sophie Thomas, Robert Walker, Robert Wynn, Roberto Giugliani, Paul Harmatz, Christian Hendriksz, and Maurizio Scarpa. Recommendations for the management of mps iva: systematic evidence- and consensus-based guidance. Orphanet Journal of Rare Diseases, Jun 2019. URL: https://doi.org/10.1186/s13023-019-1074-9, doi:10.1186/s13023-019-1074-9. This article has 162 citations and is from a peer-reviewed journal.

26. (kenth2024novelapproachfor pages 8-9): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

27. (kenth2024novelapproachfor media 9eafb273): Johnny Kenth, Elizabeth Maughan, Colin R Butler, Jasleen Gabrie, Maral Rouhani, Benjamin Silver, Olumide K Ogunbiyi, Stuart Wilkinson, Reema Nandi, Robert Walker, Nagarajan Muthialu, Simon Jones, Richard Hewitt, and Iain A Bruce. Novel approach for tracheal resection in morquio a syndrome with end-stage critical airway obstruction: a uk case series. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03253-3, doi:10.1186/s13023-024-03253-3. This article has 3 citations and is from a peer-reviewed journal.

28. (sawamoto2020mucopolysaccharidosisivadiagnosis pages 11-13): Kazuki Sawamoto, José Álvarez González, Matthew Piechnik, Francisco Otero, Maria Couce, Yasuyuki Suzuki, and Shunji Tomatsu. Mucopolysaccharidosis iva: diagnosis, treatment, and management. International Journal of Molecular Sciences, 21:1517, Feb 2020. URL: https://doi.org/10.3390/ijms21041517, doi:10.3390/ijms21041517. This article has 160 citations.
