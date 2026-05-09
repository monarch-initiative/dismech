---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:20:45.526667'
end_time: '2026-05-09T09:36:38.889176'
duration_seconds: 953.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IgG4-Related Disease
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IgG4-Related Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgG4-Related Disease** covering all of the
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
- **Disease Name:** IgG4-Related Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **IgG4-Related Disease** covering all of the
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


## Comprehensive Disease Characteristics Report: IgG4-Related Disease (IgG4-RD)

### Target disease
- **Disease name:** IgG4-Related Disease (IgG4-RD)
- **Category:** Immune-mediated fibroinflammatory / autoimmune-associated
- **Orphanet ID:** **ORPHA284264** (pieringer2014igg4relateddisease pages 1-2)
- **MONDO / MeSH / ICD-10/ICD-11:** Not retrieved from the available tool-accessible corpus in this run; therefore not reported.

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
IgG4-related disease is a **systemic, immune-mediated fibroinflammatory disorder** that can produce **tumefactive (mass-like) lesions** in one or multiple organs and is unified by characteristic histopathology and clinicopathologic correlation (wallace2024currentandfuture pages 2-4, chen2024igg4relateddiseasefor pages 1-2). A core reason IgG4-RD is diagnostically challenging is that **no single serologic test is both sensitive and specific**, so biopsy and integrative assessment are central (wallace2024currentandfuture pages 2-4, bartoszek2024igg4relateddiseasecomprehensive pages 4-7).

**Key diagnostic concept:** tissue lesions typically show **(i) dense lymphoplasmacytic infiltrate enriched for IgG4+ plasma cells, (ii) storiform fibrosis, and (iii) obliterative phlebitis**, often with **eosinophilia** (chen2024igg4relateddiseasefor pages 1-2, wallace2024currentandfuture pages 2-4).

**Direct abstract quote (identifier resource):** Pieringer et al. state: “Immunoglobulin G4- related disease (IgG4-RD) is a rare systemic fibro-inflammatory disorder (ORPHA284264).” (pieringer2014igg4relateddisease pages 1-2)

### 1.2 Synonyms / alternative names
Commonly used alternative phrasings include “IgG4-related disease,” “IgG4-RD,” and organ-specific manifestations (e.g., type 1 autoimmune pancreatitis; IgG4-related sclerosing cholangitis; retroperitoneal fibrosis as a phenotype) (chen2024igg4relateddiseasefor pages 1-2, pieringer2014igg4relateddisease pages 2-4, wallace2024currentandfuture pages 2-4).

### 1.3 Evidence source type
The information below is derived primarily from **aggregated disease-level resources** (peer-reviewed reviews and guidelines) and from **human cohort studies/registries** and **clinical trial registry records** (wallace2024currentandfuture pages 2-4, wallace2020the2019american pages 1-1, wallace2024currentandfuture pages 1-2, NCT07148791 chunk 2).

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
The aetiology remains incompletely resolved, but convergent evidence indicates a **B cell–T cell–driven immune disorder** with downstream fibroinflammation (wallace2024currentandfuture pages 2-4, hao2023thespectrumof pages 2-4).

### 2.2 Risk factors

#### Genetic risk factors (susceptibility)
- **HLA associations have been reported** in IgG4-RD and related phenotypes. Examples in the retrieved corpus include:
  - **HLA-DRB1*03** association reported for **retroperitoneal fibrosis (RPF)** subtype (bartoszek2024igg4relateddiseasecomprehensive pages 4-7).
  - **HLA-DR4** proposed susceptibility in autoimmune pancreatitis (AIP; an IgG4-RD manifestation) (wallace2019immunoglobuling4relateddisease. pages 1-2).
  - **HLA-DRB1*16** and **HLA-DQB1*05** described as “strongly associated” with autoimmune pancreatitis in one cohort (motta2024igg4autoantibodiesand pages 15-15).

#### Environmental / occupational risk factors
- A Dutch study associated occupational exposure to **solvents, oils, and industrial/metal dusts** with IgG4-related cholangitis/pancreatitis (bartoszek2024igg4relateddiseasecomprehensive pages 4-7).
- **Smoking** and **asbestos** exposure have been linked to **retroperitoneal fibrosis** risk (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, wallace2019immunoglobuling4relateddisease. pages 1-2).

#### Infectious triggers
No unifying infectious trigger is established in the retrieved evidence; reviews emphasize the absence of a consistent infectious cause (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, wallace2019immunoglobuling4relateddisease. pages 1-2).

### 2.3 Protective factors
No specific protective genetic or environmental factors were identified in the retrieved corpus.

### 2.4 Gene–environment interactions
Not clearly established in the retrieved corpus; current data support multifactorial susceptibility with organ-specific exposures and HLA background (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, wallace2019immunoglobuling4relateddisease. pages 1-2).

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Common organ involvement and clinical phenotypes
Contemporary clinical practice recognizes reproducible **organ-pattern phenotypes**, including:
- **Pancreato-hepatobiliary** (type 1 autoimmune pancreatitis; sclerosing cholangitis) (wallace2024currentandfuture pages 2-4, chen2024igg4relateddiseasefor pages 1-2)
- **Retroperitoneum/aorta** (retroperitoneal fibrosis; aortitis/large-vessel disease) (wallace2024currentandfuture pages 2-4, chen2024igg4relateddiseasefor pages 1-2)
- **Head-and-neck limited** (salivary/lacrimal gland enlargement; orbital adnexal disease) (wallace2024currentandfuture pages 2-4)
- **Mikulicz/systemic** (symmetric lacrimal/salivary enlargement plus systemic involvement; typically very high serum IgG4) (wallace2024currentandfuture pages 2-4)

Multi-organ involvement is common (reported as 60–90% in one review) (bartoszek2024igg4relateddiseasecomprehensive pages 4-7).

### 3.2 Frequencies and statistics from recent cohorts/surveys
- In a large international cohort analysis, mean organ involvement was **2.9 organs (SD 1.8)**, serum IgG4 was elevated in **78.7%**, and classic storiform fibrosis was reported in **39.6%** (illustrating that classic histology is not always captured in routine reporting) (wallace2019clinicalphenotypesof pages 2-3).
- In a Japanese nationwide survey focused on IgG4-RD with malignancy, organ frequencies included: **autoimmune pancreatitis 44.7%**, **sialadenitis 20.8%**, **eye disease 14.0%**, **kidney disease 5.16%**, **retroperitoneal fibrosis 5.12%** (sumimoto2022nationwideepidemiologicalsurvey pages 1-1).

### 3.3 Thoracic (lung/mediastinal) phenotype
Thoracic disease is clinically important and often incidental:
- Up to **30%** of systemic IgG4-RD patients may have thoracic involvement; thoracic disease is the sole manifestation in ~**10%** (muller2023thoracicmanifestationsof pages 1-2).
- Reported estimates across cohorts are ~**15–35%** thoracic involvement (muller2023thoracicmanifestationsof pages 2-3).

### 3.4 Suggested HPO terms (examples; not exhaustive)
(These are ontology suggestions for knowledge-base encoding; mapping not directly cited in the retrieved literature.)
- Tumefactive lesion / mass effect: **HP:0002664 (Neoplasm)** (used as proxy for mass-like lesion), **HP:0033694 (Organomegaly)** depending on organ.
- Salivary/lacrimal enlargement: **HP:0000217 (Xerostomia)**, **HP:0001097 (Dry eyes)**, **HP:0000175 (Parotid enlargement)**.
- Obstructive jaundice (pancreatobiliary): **HP:0000952 (Jaundice)**.
- Retroperitoneal fibrosis-related obstruction: **HP:0000795 (Ureteral obstruction)**.
- Eosinophilia: **HP:0001880 (Eosinophilia)**.
- Hypergammaglobulinemia: **HP:0012204 (Hypergammaglobulinemia)**.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
IgG4-RD is not established as a monogenic disorder in the retrieved evidence. Genetic findings are primarily **susceptibility associations** (HLA and selected non-HLA loci) rather than causal variants (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, motta2024igg4autoantibodiesand pages 15-15).

### 4.2 Pathogenic variants
No recurrent pathogenic germline variants defining IgG4-RD were identified in the retrieved corpus.

### 4.3 Autoantigens / autoantibodies (molecular targets)
Multiple candidate autoantigens have been reported in IgG4-RD. Examples include **galectin-3** (reported in 28% of a cohort) and **laminin-511** (detected in 50% of subjects with IgG4-related pancreatitis), supporting antigen-driven immunity in at least some patients (wallace2019immunoglobuling4relateddisease. pages 1-2).

---

## 5. Environmental Information

Environmental associations appear phenotype-specific:
- Occupational exposure to **solvents/oils/industrial & metal dusts** has been associated with IgG4-related cholangitis/pancreatitis (bartoszek2024igg4relateddiseasecomprehensive pages 4-7).
- **Smoking** and **asbestos exposure** have been linked to retroperitoneal fibrosis risk (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, wallace2019immunoglobuling4relateddisease. pages 1-2).

No consistent infectious agent trigger is supported in the retrieved evidence (bartoszek2024igg4relateddiseasecomprehensive pages 4-7, wallace2019immunoglobuling4relateddisease. pages 1-2).

---

## 6. Mechanism / Pathophysiology (current model)

### 6.1 Core cellular players (with CL term suggestions)
Evidence converges on immune dysregulation involving:
- **B-lineage cells**, especially **plasmablasts** (suggest CL:0000946 plasma cell; plasmablasts are a transitional phenotype).
- **T follicular helper (Tfh) cells** (suggest CL:0000907 T follicular helper cell).
- **CD4+ cytotoxic T lymphocytes (CD4+ CTLs)** (suggest CL:0000899 CD4-positive, alpha-beta T cell; “cytotoxic CD4” is a functional state).

### 6.2 B-cell/plasmablast axis and fibrosis linkage
Circulating plasmablasts are an important mechanistic and biomarker node: plasmablast levels correlate with serum IgG4, inflammatory markers, number of involved organs, and disease activity, and they fall with effective therapy and rise with relapse (hao2023thespectrumof pages 2-4, hao2023thespectrumof pages 4-6). A mechanistic link to fibrosis is proposed through plasmablast profibrotic programs (e.g., LOXL2 expression and PDGF-B secretion) (hao2023thespectrumof pages 2-4).

### 6.3 Tfh-driven class switching and plasmablast generation
Tfh cells provide B-cell help and promote IgG4 class-switching via IL-4/IL-21 and co-stimulatory interactions. Circulating PD-1+ Tfh measures correlate with serum IgG/IgG4 metrics and the number of organs involved (xu2024pathogenicrolesof pages 2-4). A 2024 review explicitly notes that “the expansion of circulating Tfh2 cells and plasmablasts may also serve as novel biomarkers for disease diagnosis and activity monitoring” (xu2024pathogenicrolesof pages 1-2).

### 6.4 CD4+ CTLs and profibrotic mediators
CD4+ CTLs infiltrate lesions and can produce profibrotic mediators such as TGF-β, providing a plausible bridge between immune activation and storiform fibrosis (hao2023thespectrumof pages 2-4).

### 6.5 Suggested GO biological process terms (examples)
(These are ontology suggestions; not directly asserted as GO annotations in the retrieved papers.)
- **GO:0006954 inflammatory response**
- **GO:0042113 B cell activation**
- **GO:0002460 adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains**
- **GO:0001525 angiogenesis** / vascular remodeling (for obliterative phlebitis context)
- **GO:0042060 wound healing** and **GO:0006959 humoral immune response**
- **GO:0045429 positive regulation of nitric oxide biosynthetic process** (macrophage-related; hypothesis-level)

### 6.6 Suggested causal chain (integrated)
A plausible chain supported by current evidence is: antigen-driven or dysregulated immune activation → expansion of Tfh (especially Tfh2-like) and plasmablasts → IgG4 class switching and oligoclonal plasmablast expansion → recruitment/activation of profibrotic T-cell and myeloid programs (including CD4+ CTLs) → storiform fibrosis and organ dysfunction (hao2023thespectrumof pages 2-4, xu2024pathogenicrolesof pages 2-4, wallace2024currentandfuture pages 2-4).

---

## 7. Anatomical Structures Affected

### 7.1 Organs and systems (examples)
IgG4-RD can affect virtually any organ; commonly involved sites include pancreas and hepatobiliary system, salivary/lacrimal glands and orbit, retroperitoneum/aorta, kidney, lung/mediastinum, and lymph nodes (chen2024igg4relateddiseasefor pages 1-2, pieringer2014igg4relateddisease pages 2-4, wallace2024currentandfuture pages 2-4).

### 7.2 UBERON suggestions (examples)
- Pancreas: **UBERON:0001264**
- Lacrimal gland: **UBERON:0001813**
- Major salivary gland: **UBERON:0001044**
- Lung: **UBERON:0002048**
- Kidney: **UBERON:0002113**
- Retroperitoneum: **UBERON:0003698**

---

## 8. Temporal Development

### 8.1 Onset
IgG4-RD typically affects **middle-aged to older adults** (median around late 50s–60 in major cohorts) (chen2024igg4relateddiseasefor pages 1-2, muller2023thoracicmanifestationsof pages 2-3).

### 8.2 Course and progression
The disease often follows a **relapsing–remitting** course; if under-treated, it can cause **irreversible fibrotic organ damage** (wallace2024currentandfuture pages 2-4, chen2024igg4relateddiseasefor pages 1-2). Proliferative manifestations tend to respond better than chronic fibrotic disease, which may be less reversible (chen2024igg4relateddiseasefor pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent estimates prioritized)
A 2024 practice review summarized a US claims-based analysis reporting:
- **Incidence:** **0.78–1.39 per 100,000 person-years** (2015–2019)
- **Point prevalence:** **5.3 per 100,000 persons** (as of 1 Jan 2019) (wallace2024currentandfuture pages 1-2)

A thoracic-manifestations review summarizes additional estimates, e.g., Japan incidence approximated at ~1 per 100,000 and prevalence ~0.8 per 100,000 (muller2023thoracicmanifestationsof pages 2-3), while also emphasizing heterogeneity.

### 9.2 Demographics
- Male predominance is frequently reported overall, but varies by phenotype; head-and-neck–limited disease shows less male predominance (wallace2024currentandfuture pages 2-4, wallace2019clinicalphenotypesof pages 2-3).
- In an international cohort, Asians had higher median serum IgG4 (median 666 vs 240.5 mg/dL in non-Asians), and males were older at onset/diagnosis than females (wallace2019clinicalphenotypesof pages 2-3).

---

## 10. Diagnostics

### 10.1 Histopathology and core features
Hallmark tissue features include dense lymphoplasmacytic infiltrate rich in IgG4+ plasma cells, storiform fibrosis, obliterative phlebitis, and eosinophilia. A common supportive threshold is an **IgG4/IgG ratio >40%** in tissue (chen2024igg4relateddiseasefor pages 1-2).

### 10.2 Classification criteria (2019 ACR/EULAR)
The 2019 ACR/EULAR criteria provide a validated, points-based framework requiring: entry organ involvement, exclusion criteria application, and weighted inclusion domains across clinical/serologic/radiologic/pathologic data, with classification at **≥20 points** (wallace2020the2019american pages 1-1). Performance:
- Derived/validated in **1,879 subjects** (1,086 cases; 793 mimickers) (wallace2020the2019american pages 1-1)
- Validation cohort 1: **specificity 99.2%**, **sensitivity 85.5%** at threshold 20 (wallace2020the2019american pages 1-1)
- Validation cohort 2: **specificity 97.8%**, **sensitivity 82.0%** at threshold 20 (wallace2020the2019american pages 1-1)

### 10.3 Biomarkers
- Serum IgG4 is often elevated and correlates with extent of organ involvement and relapse risk, but is not specific (wallace2024currentandfuture pages 2-4).
- Circulating plasmablasts and Tfh-derived measures (e.g., PD-1+ cTfh metrics) are proposed activity biomarkers (hao2023thespectrumof pages 2-4, xu2024pathogenicrolesof pages 2-4).

### 10.4 Imaging and diagnostic pitfalls
Thoracic IgG4-RD has heterogeneous CT patterns and can mimic malignancy or vasculitis; cautious diagnosis includes searching for extra-thoracic disease and integrating serum IgG4/plasmablast measures plus pathology (muller2023thoracicmanifestationsof pages 1-2).

---

## 11. Outcome / Prognosis

### 11.1 Organ damage and reversibility
Clinical outcomes vary by phenotype: proliferative manifestations generally respond well to immunosuppression, whereas established fibrotic disease may be less reversible (chen2024igg4relateddiseasefor pages 1-2).

### 11.2 Malignancy association (statistics)
A Japanese nationwide survey reported an estimated overall prevalence of malignancy among IgG4-RD cases of **~10.9%** (10,900 per 100,000 cases), and malignant lymphoma **~2.0%** (1,985 per 100,000). IgG4-related kidney disease had the highest associated malignancy frequency (17.1%) (sumimoto2022nationwideepidemiologicalsurvey pages 1-1). These data are context-specific (survey methodology) and should be interpreted accordingly.

---

## 12. Treatment

### 12.1 Standard of care: glucocorticoids (real-world implementation)
European evidence-based guidance for IgG4-related digestive disease recommends:
- **Induction:** oral glucocorticoids **0.6–0.8 mg/kg/day for 1 month** (typical **30–40 mg/day prednisone equivalent**) (lohr2020europeanguidelineon pages 17-19, lohr2020europeanguidelineon pages 1-2)
- **Response assessment:** at **week 2–4** using clinical/biochemical/morphological markers (lohr2020europeanguidelineon pages 17-19, lohr2020europeanguidelineon pages 1-2)
- **Taper:** e.g., **5 mg every 2 weeks**, over **3–6 months** (lohr2020europeanguidelineon pages 17-19)
- **Relapse:** common; guideline notes relapse rates **26–70%** and high re-induction success with glucocorticoids (>95%) (lohr2020europeanguidelineon pages 19-20)

### 12.2 B-cell depletion and steroid-sparing therapy
- B-cell depletion (rituximab) is widely used in relapsing/refractory disease and is supported by the central role of B cells/plasmablasts (hao2023thespectrumof pages 2-4, wallace2024currentandfuture pages 2-4).
- A phase 1–2 registry trial entry exists for rituximab (**NCT01584388**) and cites a prospective open-label study publication (**PMID: 25667206**) (NCT01584388 chunk 2).

### 12.3 Emerging and investigational immunomodulators (clinical trials)
- **Belimumab** (BAFF inhibition) RCT: NCT04660565 is described as an RCT of **belimumab + glucocorticoids vs glucocorticoids alone**, primary outcome relapse rate, 12-month follow-up (wallace2024currentandfuture pages 7-8). Registry: https://clinicaltrials.gov/study/NCT04660565 (post date and version dates vary by record).
- **Abatacept** (CTLA4-Ig; co-stimulation blockade): NCT03669861 (Massachusetts General Hospital) (NCT03669861 chunk 2). Registry: https://clinicaltrials.gov/study/NCT03669861.
- **Anti-CD19/BCMA-CD19 CAR-T** exploratory trial for relapsed/refractory IgG4-RD: NCT07148791, with key efficacy endpoint change in IgG4-RD Responder Index at baseline, week 12, week 26, and intensive safety monitoring for CRS/ICANS (NCT07148791 chunk 2). Registry: https://clinicaltrials.gov/study/NCT07148791.

*Note:* A placebo-controlled inebilizumab study is referenced in a 2024 table, but the excerpt available here is truncated and does not provide full registry detail (wallace2024currentandfuture pages 7-8).

### 12.4 MAXO term suggestions (examples)
- Glucocorticoid therapy: **MAXO:0000155 (glucocorticoid therapy)**
- B-cell depletion therapy (rituximab): **MAXO:0001181 (B cell depletion therapy)** (term may vary)
- Abatacept therapy: **MAXO: immunomodulatory therapy**
- Belimumab therapy: **MAXO: monoclonal antibody therapy**
- CAR-T cell therapy: **MAXO:0001503 (CAR T cell therapy)**

---

## 13. Prevention

### Primary prevention
No established primary prevention strategies are supported by the retrieved evidence.

### Secondary/tertiary prevention (practical)
- Early recognition and clinicopathologic confirmation (biopsy) are emphasized to avoid diagnostic delay and prevent irreversible fibrosis (wallace2024currentandfuture pages 2-4, bartoszek2024igg4relateddiseasecomprehensive pages 4-7).
- Relapse prevention/monitoring: maintenance glucocorticoids may be considered in multi-organ disease or prior relapse; response monitoring at week 2–4; add immunosuppressives when relapse occurs early during taper or when disease is not controlled (lohr2020europeanguidelineon pages 1-2, lohr2020europeanguidelineon pages 19-20).

---

## 14. Other Species / Natural Disease
No evidence for naturally occurring IgG4-RD in non-human species was retrieved in this run.

---

## 15. Model Organisms
No standardized animal model systems were retrieved in the accessible corpus. A mouse immunization experiment linked to laminin-511 is mentioned as supporting an antigen-driven mechanism but details were not available in the retrieved text segments (wallace2019immunoglobuling4relateddisease. pages 1-2).

---

## Key curated summary table

| Category | Item | Summary | Publication | URL | Citation |
|---|---|---|---|---|---|
| Identifier | Orphanet ID | IgG4-related disease is identified as a rare systemic fibro-inflammatory disorder with Orphanet identifier **ORPHA284264**. | Pieringer et al., 2014 | https://doi.org/10.1186/s13023-014-0110-z | (pieringer2014igg4relateddisease pages 1-2) |
| Defining histopathology | Lymphoplasmacytic infiltrate rich in IgG4+ plasma cells | Hallmark lesion includes a **dense lymphoplasmacytic infiltrate** enriched in **IgG4-positive plasma cells**; tissue diagnosis is essential. | Chen, 2024 | https://doi.org/10.1182/hematology.2024000584 | (chen2024igg4relateddiseasefor pages 1-2) |
| Defining histopathology | Storiform fibrosis | **Storiform fibrosis** is a core histopathologic feature and part of the classic triad used in diagnosis/classification. | Chen, 2024 | https://doi.org/10.1182/hematology.2024000584 | (chen2024igg4relateddiseasefor pages 1-2) |
| Defining histopathology | Obliterative phlebitis | **Obliterative phlebitis** is a characteristic histologic feature supporting IgG4-RD diagnosis. | Chen, 2024 | https://doi.org/10.1182/hematology.2024000584 | (chen2024igg4relateddiseasefor pages 1-2) |
| Supportive finding | Tissue eosinophilia | **Tissue eosinophilia** is a common supportive feature accompanying the histopathologic triad. | Chen, 2024 | https://doi.org/10.1182/hematology.2024000584 | (chen2024igg4relateddiseasefor pages 1-2) |
| Supportive finding | Serum IgG4 elevation | Many patients have **elevated serum IgG4**; this correlates with extent of organ involvement and relapse risk, but is not specific enough to diagnose disease alone. | Wallace et al., 2024 | https://doi.org/10.1093/rap/rkae020 | (wallace2024currentandfuture pages 2-4) |
| Supportive finding | Tissue IgG4/IgG ratio | A commonly used supportive tissue threshold is an **IgG4:IgG plasma-cell ratio >40%**. | Chen, 2024 | https://doi.org/10.1182/hematology.2024000584 | (chen2024igg4relateddiseasefor pages 1-2) |
| Classification criteria | 2019 ACR/EULAR entry and threshold | Classification uses a 3-step process (typical organ involvement, exclusion criteria, weighted inclusion criteria) with a threshold of **≥20 points**. | Wallace et al., 2020 | https://doi.org/10.1136/annrheumdis-2019-216561 | (wallace2020the2019american pages 1-1) |
| Classification performance | Cohort size used in development/validation | Criteria were developed/validated using **1,879 subjects** total (**1,086 cases** and **793 mimickers**). | Wallace et al., 2020 | https://doi.org/10.1136/annrheumdis-2019-216561 | (wallace2020the2019american pages 1-1) |
| Classification performance | Validation cohort 1 | At **≥20 points**, specificity was **99.2%** (95% CI 97.2–99.8) and sensitivity was **85.5%** (95% CI 81.9–88.5). | Wallace et al., 2020 | https://doi.org/10.1136/annrheumdis-2019-216561 | (wallace2020the2019american pages 1-1) |
| Classification performance | Validation cohort 2 | At **≥20 points**, specificity was **97.8%** (95% CI 93.7–99.2) and sensitivity was **82.0%** (95% CI 77.0–86.1). | Wallace et al., 2020 | https://doi.org/10.1136/annrheumdis-2019-216561 | (wallace2020the2019american pages 1-1) |


*Table: This table summarizes the core disease identifier, defining pathology, supportive findings, and validated 2019 ACR/EULAR classification performance for IgG4-related disease. It is useful as a compact reference for knowledge-base curation and diagnostic context.*

---

## Notes on evidence gaps and limitations
1. **Ontology identifiers (MONDO, MeSH, ICD)** were not retrievable from the current tool-accessible literature corpus; the report therefore does not assert them.
2. Several important 2023–2025 primary studies (e.g., single-cell transcriptomics; some therapeutics RCT publications) were listed as unobtainable in tool retrieval; mechanistic and treatment sections thus emphasize accessible, high-quality reviews/cohorts and clinical trial registry records.
3. HPO/GO/UBERON/MAXO terms are provided as **suggestions for encoding** and were not directly mapped in the cited papers.


References

1. (pieringer2014igg4relateddisease pages 1-2): Herwig Pieringer, Ilse Parzer, Adelheid Wöhrer, Petra Reis, Bastian Oppl, and Jochen Zwerina. Igg4- related disease: an orphan disease with many faces. Orphanet Journal of Rare Diseases, 9:110-110, Jul 2014. URL: https://doi.org/10.1186/s13023-014-0110-z, doi:10.1186/s13023-014-0110-z. This article has 142 citations and is from a peer-reviewed journal.

2. (wallace2024currentandfuture pages 2-4): Zachary S Wallace, Guy Katz, Yasmin G Hernandez-Barco, and Matthew C Baker. Current and future advances in practice: igg4-related disease. Rheumatology Advances in Practice, Apr 2024. URL: https://doi.org/10.1093/rap/rkae020, doi:10.1093/rap/rkae020. This article has 71 citations and is from a peer-reviewed journal.

3. (chen2024igg4relateddiseasefor pages 1-2): Luke Y. C. Chen. Igg4-related disease for the hematologist. Hematology, 2024:594-603, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000584, doi:10.1182/hematology.2024000584. This article has 15 citations and is from a peer-reviewed journal.

4. (bartoszek2024igg4relateddiseasecomprehensive pages 4-7): Lidia Bartoszek, Dominika Orłowska, Joanna Olszak, Karolina Zalewa, Wojciech Kapłan, Jakub Starownik, and Bartłomiej Gastoł. Igg4-related disease: comprehensive overview of pathogenesis, clinical manifestations, and diagnostic challenges. Quality in Sport, 22:54293, Sep 2024. URL: https://doi.org/10.12775/qs.2024.22.54293, doi:10.12775/qs.2024.22.54293. This article has 0 citations.

5. (pieringer2014igg4relateddisease pages 2-4): Herwig Pieringer, Ilse Parzer, Adelheid Wöhrer, Petra Reis, Bastian Oppl, and Jochen Zwerina. Igg4- related disease: an orphan disease with many faces. Orphanet Journal of Rare Diseases, 9:110-110, Jul 2014. URL: https://doi.org/10.1186/s13023-014-0110-z, doi:10.1186/s13023-014-0110-z. This article has 142 citations and is from a peer-reviewed journal.

6. (wallace2020the2019american pages 1-1): Zachary S Wallace, Ray P Naden, Suresh Chari, Hyon K Choi, Emanuel Della-Torre, Jean-Francois Dicaire, Phillip A Hart, Dai Inoue, Mitsuhiro Kawano, Arezou Khosroshahi, Marco Lanzillotta, Kazuichi Okazaki, Cory A Perugino, Amita Sharma, Takako Saeki, Nicolas Schleinitz, Naoki Takahashi, Hisanori Umehara, Yoh Zen, and John H Stone. The 2019 american college of rheumatology/european league against rheumatism classification criteria for igg4-related disease. Annals of the Rheumatic Diseases, 79:77-87, Jan 2020. URL: https://doi.org/10.1136/annrheumdis-2019-216561, doi:10.1136/annrheumdis-2019-216561. This article has 1362 citations and is from a highest quality peer-reviewed journal.

7. (wallace2024currentandfuture pages 1-2): Zachary S Wallace, Guy Katz, Yasmin G Hernandez-Barco, and Matthew C Baker. Current and future advances in practice: igg4-related disease. Rheumatology Advances in Practice, Apr 2024. URL: https://doi.org/10.1093/rap/rkae020, doi:10.1093/rap/rkae020. This article has 71 citations and is from a peer-reviewed journal.

8. (NCT07148791 chunk 2): Jian Zhu. Exploratory Study of Anti-BCMA-CD19 CAR-T Cell Therapy in Relapsed or Refractory IgG4-Related Disease. Chinese PLA General Hospital. 2025. ClinicalTrials.gov Identifier: NCT07148791

9. (hao2023thespectrumof pages 2-4): Qiyuan Hao, Meng Sun, and Yanying Liu. The spectrum of b cells in the pathogenesis, diagnosis and therapeutic applications of immunoglobulin g4‐related disease. Clinical & Translational Immunology, Jan 2023. URL: https://doi.org/10.1002/cti2.1477, doi:10.1002/cti2.1477. This article has 7 citations and is from a peer-reviewed journal.

10. (wallace2019immunoglobuling4relateddisease. pages 1-2): Zachary S. Wallace, Cory Perugino, Mark Matza, Vikram Deshpande, Amita Sharma, and John H. Stone. Immunoglobulin g4-related disease. Clinics in chest medicine, 40 3:583-597, Sep 2019. URL: https://doi.org/10.1016/j.ccm.2019.05.005, doi:10.1016/j.ccm.2019.05.005. This article has 70 citations and is from a peer-reviewed journal.

11. (motta2024igg4autoantibodiesand pages 15-15): Rodrigo V. Motta and Emma L. Culver. Igg4 autoantibodies and autoantigens in the context of igg4-autoimmune disease and igg4-related disease. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1272084, doi:10.3389/fimmu.2024.1272084. This article has 30 citations and is from a peer-reviewed journal.

12. (wallace2019clinicalphenotypesof pages 2-3): Zachary S Wallace, Yuqing Zhang, Cory A Perugino, Ray Naden, Hyon K Choi, and John H Stone. Clinical phenotypes of igg4-related disease: an analysis of two international cross-sectional cohorts. Annals of the Rheumatic Diseases, 78:406-412, Mar 2019. URL: https://doi.org/10.1136/annrheumdis-2018-214603, doi:10.1136/annrheumdis-2018-214603. This article has 422 citations and is from a highest quality peer-reviewed journal.

13. (sumimoto2022nationwideepidemiologicalsurvey pages 1-1): Kimi Sumimoto, Kazushige Uchida, Tsukasa Ikeura, Kenji Hirano, Motohisa Yamamoto, Hiroki Takahashi, Takayoshi Nishino, Ichiro Mizushima, Mitsuhiro Kawano, Terumi Kamisawa, Takako Saeki, Hiroyuki Maguchi, Tomoyuki Ushijima, Masahiro Shiokawa, Hiroshi Seno, Hiroshi Goto, Seiji Nakamura, and Kazuichi Okazaki. Nationwide epidemiological survey of immunoglobulin g4‐related disease with malignancy in japan. Journal of Gastroenterology and Hepatology, 37:1022-1033, Mar 2022. URL: https://doi.org/10.1111/jgh.15809, doi:10.1111/jgh.15809. This article has 26 citations and is from a peer-reviewed journal.

14. (muller2023thoracicmanifestationsof pages 1-2): Romain Muller, Mikael Ebbo, Paul Habert, Laurent Daniel, Antoine Briantais, Pascal Chanez, Jean Yves Gaubert, and Nicolas Schleinitz. Thoracic manifestations of igg4‐related disease. Respirology (Carlton, Vic.), 28:120-131, Nov 2023. URL: https://doi.org/10.1111/resp.14422, doi:10.1111/resp.14422. This article has 58 citations.

15. (muller2023thoracicmanifestationsof pages 2-3): Romain Muller, Mikael Ebbo, Paul Habert, Laurent Daniel, Antoine Briantais, Pascal Chanez, Jean Yves Gaubert, and Nicolas Schleinitz. Thoracic manifestations of igg4‐related disease. Respirology (Carlton, Vic.), 28:120-131, Nov 2023. URL: https://doi.org/10.1111/resp.14422, doi:10.1111/resp.14422. This article has 58 citations.

16. (hao2023thespectrumof pages 4-6): Qiyuan Hao, Meng Sun, and Yanying Liu. The spectrum of b cells in the pathogenesis, diagnosis and therapeutic applications of immunoglobulin g4‐related disease. Clinical & Translational Immunology, Jan 2023. URL: https://doi.org/10.1002/cti2.1477, doi:10.1002/cti2.1477. This article has 7 citations and is from a peer-reviewed journal.

17. (xu2024pathogenicrolesof pages 2-4): Jingyi Xu, Jiayu Zhai, and Jinxia Zhao. Pathogenic roles of follicular helper t cells in igg4-related disease and implications for potential therapy. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1413860, doi:10.3389/fimmu.2024.1413860. This article has 18 citations and is from a peer-reviewed journal.

18. (xu2024pathogenicrolesof pages 1-2): Jingyi Xu, Jiayu Zhai, and Jinxia Zhao. Pathogenic roles of follicular helper t cells in igg4-related disease and implications for potential therapy. Frontiers in Immunology, Jun 2024. URL: https://doi.org/10.3389/fimmu.2024.1413860, doi:10.3389/fimmu.2024.1413860. This article has 18 citations and is from a peer-reviewed journal.

19. (lohr2020europeanguidelineon pages 17-19): J‐Matthias Löhr, Ulrich Beuers, Miroslav Vujasinovic, Domenico Alvaro, Jens Brøndum Frøkjær, Frank Buttgereit, Gabriele Capurso, Emma L Culver, Enrique de‐Madaria, Emanuel Della‐Torre, Sönke Detlefsen, Enrique Dominguez‐Muñoz, Piotr Czubkowski, Nils Ewald, Luca Frulloni, Natalya Gubergrits, Deniz Guney Duman, Thilo Hackert, Julio Iglesias‐Garcia, Nikolaos Kartalis, Andrea Laghi, Frank Lammert, Fredrik Lindgren, Alexey Okhlobystin, Grzegorz Oracz, Andrea Parniczky, Raffaella Maria Pozzi Mucelli, Vinciane Rebours, Jonas Rosendahl, Nicolas Schleinitz, Alexander Schneider, Eric FH van Bommel, Caroline Sophie Verbeke, Marie Pierre Vullierme, and Heiko Witt. European guideline on igg4‐related digestive disease – ueg and sgf evidence‐based recommendations. United European Gastroenterology Journal, 8:637-666, Jul 2020. URL: https://doi.org/10.1177/2050640620934911, doi:10.1177/2050640620934911. This article has 272 citations and is from a peer-reviewed journal.

20. (lohr2020europeanguidelineon pages 1-2): J‐Matthias Löhr, Ulrich Beuers, Miroslav Vujasinovic, Domenico Alvaro, Jens Brøndum Frøkjær, Frank Buttgereit, Gabriele Capurso, Emma L Culver, Enrique de‐Madaria, Emanuel Della‐Torre, Sönke Detlefsen, Enrique Dominguez‐Muñoz, Piotr Czubkowski, Nils Ewald, Luca Frulloni, Natalya Gubergrits, Deniz Guney Duman, Thilo Hackert, Julio Iglesias‐Garcia, Nikolaos Kartalis, Andrea Laghi, Frank Lammert, Fredrik Lindgren, Alexey Okhlobystin, Grzegorz Oracz, Andrea Parniczky, Raffaella Maria Pozzi Mucelli, Vinciane Rebours, Jonas Rosendahl, Nicolas Schleinitz, Alexander Schneider, Eric FH van Bommel, Caroline Sophie Verbeke, Marie Pierre Vullierme, and Heiko Witt. European guideline on igg4‐related digestive disease – ueg and sgf evidence‐based recommendations. United European Gastroenterology Journal, 8:637-666, Jul 2020. URL: https://doi.org/10.1177/2050640620934911, doi:10.1177/2050640620934911. This article has 272 citations and is from a peer-reviewed journal.

21. (lohr2020europeanguidelineon pages 19-20): J‐Matthias Löhr, Ulrich Beuers, Miroslav Vujasinovic, Domenico Alvaro, Jens Brøndum Frøkjær, Frank Buttgereit, Gabriele Capurso, Emma L Culver, Enrique de‐Madaria, Emanuel Della‐Torre, Sönke Detlefsen, Enrique Dominguez‐Muñoz, Piotr Czubkowski, Nils Ewald, Luca Frulloni, Natalya Gubergrits, Deniz Guney Duman, Thilo Hackert, Julio Iglesias‐Garcia, Nikolaos Kartalis, Andrea Laghi, Frank Lammert, Fredrik Lindgren, Alexey Okhlobystin, Grzegorz Oracz, Andrea Parniczky, Raffaella Maria Pozzi Mucelli, Vinciane Rebours, Jonas Rosendahl, Nicolas Schleinitz, Alexander Schneider, Eric FH van Bommel, Caroline Sophie Verbeke, Marie Pierre Vullierme, and Heiko Witt. European guideline on igg4‐related digestive disease – ueg and sgf evidence‐based recommendations. United European Gastroenterology Journal, 8:637-666, Jul 2020. URL: https://doi.org/10.1177/2050640620934911, doi:10.1177/2050640620934911. This article has 272 citations and is from a peer-reviewed journal.

22. (NCT01584388 chunk 2): John H. Stone, MD. Rituximab in IgG4-RD: A Phase 1-2 Trial. Massachusetts General Hospital. 2012. ClinicalTrials.gov Identifier: NCT01584388

23. (wallace2024currentandfuture pages 7-8): Zachary S Wallace, Guy Katz, Yasmin G Hernandez-Barco, and Matthew C Baker. Current and future advances in practice: igg4-related disease. Rheumatology Advances in Practice, Apr 2024. URL: https://doi.org/10.1093/rap/rkae020, doi:10.1093/rap/rkae020. This article has 71 citations and is from a peer-reviewed journal.

24. (NCT03669861 chunk 2): Stone, John H, M.D., M.P.H. Safety and Efficacy of Abatacept in IgG4-Related Disease. Massachusetts General Hospital. 2018. ClinicalTrials.gov Identifier: NCT03669861
