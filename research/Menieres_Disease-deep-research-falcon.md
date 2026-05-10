---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:56:16.854869'
end_time: '2026-05-09T12:24:46.046377'
duration_seconds: 1709.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Meniere's Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 62
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meniere's Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Meniere's Disease** covering all of the
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
- **Disease Name:** Meniere's Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Meniere's Disease** covering all of the
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


# Ménière’s Disease (MD) — Disease Characteristics Research Report (Complex)

## Executive summary
Ménière’s disease (MD) is a clinical inner-ear disorder characterized by recurrent spontaneous vertigo attacks together with fluctuating auditory symptoms (hearing loss, tinnitus, and/or aural fullness) and documented low- to mid-frequency sensorineural hearing loss (SNHL) in the affected ear for “definite” disease under contemporary international criteria. (basura2020clinicalpracticeguidelinea pages 9-10, lopezescamez2015diagnosticcriteriafor pages 2-4, basura2020clinicalpracticeguideline pages 1-2)

Major 2023–2024 advances include (i) maturation of delayed post-gadolinium “hydrops MRI” with meta-analytic performance estimates and identification of high-yield imaging descriptors (notably saccular abnormality and perilymphatic enhancement), and (ii) expanding genetic evidence supporting heterogeneous inheritance in ~5–20% familial disease with enrichment of rare variants in genes involved in stereocilia and extracellular membranes. (connor2024assessingtheoptimal pages 1-3, connor2023delayedpostgadolinium pages 1-2, parraperez2023typesofinheritance pages 1-2)

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
MD is an episodic vestibulo-cochlear syndrome defined clinically by (a) spontaneous vertigo attacks (20 minutes to 12 hours for definite MD), (b) low- to mid-frequency SNHL documented in the affected ear, and (c) fluctuating aural symptoms (hearing loss, tinnitus, and/or aural fullness), with exclusion of alternative vestibular diagnoses. (lopezescamez2015diagnosticcriteriafor pages 2-4, basura2020clinicalpracticeguideline pages 1-2)

### 1.2 Key identifiers (what could be retrieved with tools)
* **ICD-10**: **H81.0 / H810** (“Meniere’s disease”) is explicitly used for case ascertainment in a Korean nationwide cohort study. (kwon2024epidemiologicalevidencefor pages 2-3)
* **ClinicalTrials.gov** uses the condition label **“Meniere Disease”** in registered interventional studies, and shows associated MeSH/ontology ancestors for related concepts (e.g., Endolymphatic Hydrops). (NCT00802529 chunk 2)

**Not retrieved from the current tool context:** MONDO ID, Orphanet ID, OMIM ID, and the direct MeSH descriptor ID for “Ménière Disease” were not present in the retrieved full texts/snippets and could not be confirmed here without additional ontology/database calls beyond the provided tool outputs.

### 1.3 Synonyms / alternative names (from clinical usage and literature)
Commonly used variants include:
* Ménière’s disease / Meniere disease / Morbus Ménière
* Endolymphatic hydrops (often used as a pathologic correlate rather than a strict synonym)
* Hydropic ear disease (broader category used in some classifications)
These labels are referenced in the guideline/review framing (e.g., association with “inner ear fluid (endolymph) volume increases” and the term endolymphatic hydrops). (basura2020clinicalpracticeguidelinea pages 1-2, lopezescamez2015diagnosticcriteriafor pages 1-2)

### 1.4 Evidence source type
This entry is synthesized from **aggregated disease-level resources** (international diagnostic consensus and a clinical practice guideline) plus **clinical observational cohorts**, **systematic reviews/meta-analyses**, **genetic reviews**, and **clinical trial registry records**. (basura2020clinicalpracticeguideline pages 1-2, connor2023delayedpostgadolinium pages 1-2, parraperez2023typesofinheritance pages 1-2, NCT05851508 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (current consensus)
MD remains etiologically heterogeneous and incompletely explained by a single mechanism. Consensus descriptions emphasize association with “inner ear fluid (endolymph) volume increases,” i.e., endolymphatic hydrops (EH), but note that etiology is “not completely clear.” (basura2020clinicalpracticeguidelinea pages 1-2)

### 2.2 Risk factors (recent human evidence prioritized)

#### Infectious / inflammatory triggers
* **Upper respiratory infection (URI) as a risk factor (2024):** In a Korean National Health Insurance matched cohort (2002–2019; 19,721 MD cases; 78,884 controls), a URI within one year was associated with **2.01-fold higher likelihood** of MD (95% CI 1.91–2.11), and URI within two years with **1.54-fold higher likelihood** (95% CI 1.50–1.59). (kwon2024epidemiologicalevidencefor pages 1-2)

#### Trauma / exposure-related associations (phenotype modifiers)
* **Head injury / neck injury / acoustic trauma (2024):** In a Finnish registry study (n=912), **19.2%** reported prior traumatic brain injury, **10.8%** neck trauma, and **25.4%** occupational noise exposure; these exposures were associated with altered complaint profiles (e.g., more vestibular drop attacks or greater tinnitus/hyperacusis impact), though not with differences in vertigo frequency/duration/severity. (pyykko2024associationofhead pages 1-2)

#### Other comorbidity signals
* MD epidemiology appears variable by region and population; the 2024 cohort paper notes wide ranges in reported incidence/prevalence (3–513 per 100,000 annually, depending on study/region/criteria) and demographic patterns (increasing incidence with age; higher in white females in 40s–50s in some reports). (kwon2024epidemiologicalevidencefor pages 1-2)

### 2.3 Genetic risk (familial MD and susceptibility)
Familial aggregation supports heritability, with **familial MD estimated ~5–20% in European-descended cohorts and ~10% overall** in the 2023 genetics review. (parraperez2023typesofinheritance pages 1-2)

Key implicated genes in familial MD include **OTOG, MYO7A, TECTA** (frequently reported) and additional autosomal dominant family genes such as **FAM136A, DTNA, PRKCB, COCH, DPT, SEMA3D, GUSB, SLC6A7**. (parraperez2023typesofinheritance pages 2-4, parraperez2023typesofinheritance pages 4-5)

### 2.4 Protective factors
Protective genetic or environmental factors were not clearly established in the retrieved primary/secondary sources. One genetics review notes that some loci may be “protective or population-specific” in candidate-gene literature, but no clinically actionable protective factor was supported strongly enough in the available evidence to enumerate here. (dai2023geneticadvancesin pages 5-6)

### 2.5 Gene–environment interaction (current evidence status)
The 2023 familial genetics review explicitly frames MD as a disorder where diverse genetic architectures (AD/AR/multiallelic) and variable expressivity suggest interaction with modifiers, but direct gene–environment interaction effects were not quantified in the retrieved excerpts. (parraperez2023typesofinheritance pages 2-4)

---

## 3. Phenotypes (clinical features)

### 3.1 Core phenotype (diagnostic)
**Definite MD** (Bárány Society 2015 / AAO-HNSF adoption) requires:
1) ≥2 spontaneous vertigo attacks, **20 min to 12 h**;
2) documented low- to mid-frequency SNHL in the affected ear;
3) fluctuating aural symptoms in the affected ear;
4) not better accounted for by another vestibular diagnosis. (lopezescamez2015diagnosticcriteriafor pages 2-4, basura2020clinicalpracticeguideline pages 1-2)

**Probable MD** broadens to vertigo/dizziness episodes **20 min to 24 h** with fluctuating aural symptoms, excluding other causes. (goebel20162015equilibriumcommittee pages 2-2, basura2020clinicalpracticeguideline pages 1-2)

A guideline-captured diagnostic criteria table is available as an extracted figure for reference. (basura2020clinicalpracticeguideline media b1eac1f2)

### 3.2 Symptom spectrum, frequency, and longitudinal features (2024 data)
A large Finnish patient-organization cohort (definite MD; n=365) reported:
* Simultaneous onset of hearing loss + vertigo + tinnitus in **38%**. (pyykko2024changesinsymptom pages 1-2)
* **Spontaneous remission** from episodic vertigo in **34%** over the course of disease. (pyykko2024changesinsymptom pages 1-2)
* **Balance issues** in **65.5%**. (pyykko2024changesinsymptom pages 1-2)
* **Vestibular drop attacks** in **34%**; **severe falls** in **10%**. (pyykko2024changesinsymptom pages 1-2)
* **Bilateral hearing loss** developed long-term in **34.5%**, with higher risk associated with younger onset, migraine, and family history. (pyykko2024changesinsymptom pages 1-2)

### 3.3 Quality-of-life impact
* The 2024 cohort above reports that quality of life was “significantly lower among participants with constant dizziness,” and identifies fatigue, depression, vestibular drop attacks, and hearing loss as contributors. (pyykko2024changesinsymptom pages 1-2)
* In a clinical MRI correlation study (n=70), anxiety and depression scales (SAS/SDS) correlated with dizziness handicap (DHI emotional and total scores), linking symptom burden and mental health in MD. (hu2023endolymphatichydropsimaging pages 1-2)

### 3.4 Suggested HPO terms (phenotype ontology mapping; for knowledge base)
Below are commonly appropriate HPO mappings for the core MD phenotype (term names shown; exact IDs should be validated against the current HPO release):
* Vertigo; Episodic vertigo
* Sensorineural hearing impairment (often low-frequency/fluctuating)
* Tinnitus
* Aural fullness / Ear fullness
* Drop attacks (Tumarkin attacks)
* Imbalance
* Nausea (during attacks)

(These mappings are ontology suggestions; they are consistent with the clinical criteria and cohort descriptions above.) (lopezescamez2015diagnosticcriteriafor pages 2-4, basura2020clinicalpracticeguideline pages 1-2, pyykko2024changesinsymptom pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes vs susceptibility genes
MD is not generally monogenic in sporadic presentations; however, **familial MD** can show Mendelian or oligogenic patterns in some pedigrees, with multiple genes reported in association studies and sequencing reports aggregated in 2023–2024 reviews. (parraperez2023typesofinheritance pages 2-4, dai2023geneticadvancesin pages 1-2)

### 4.2 Inheritance patterns (familial MD)
Familial MD shows heterogeneous inheritance models, including:
* **Autosomal dominant** families (e.g., reported with variants in FAM136A, DTNA, PRKCB, and others)
* **Autosomal recessive / compound recessive** models (including multiallelic inheritance for OTOG in multiple families)
* **Digenic/multiallelic** models and incomplete penetrance/variable expressivity
These patterns are explicitly summarized in the 2023 JARO review. (parraperez2023typesofinheritance pages 2-4)

### 4.3 Key genes implicated (familial MD; 2023 synthesis)
Frequently implicated genes include:
* **OTOG, MYO7A, TECTA** (most frequently found in familial MD per 2023 review) (parraperez2023typesofinheritance pages 1-2)
* Additional reported AD-family genes: **FAM136A, DTNA, PRKCB, COCH, DPT, SEMA3D, GUSB, SLC6A7** (parraperez2023typesofinheritance pages 2-4)

### 4.4 Pathogenic variant types (examples from 2023 review)
The familial genetics review reports examples including **frameshift deletions** in TECTA producing truncated α-tectorin (classified as likely pathogenic in those reports) and multiple family-private variants with incomplete penetrance. (parraperez2023typesofinheritance pages 4-5)

### 4.5 Mechanistic hypothesis linking genes to phenotype (expert synthesis from authoritative review)
A prominent 2023 hypothesis emphasizes proteins of the **tectorial membrane/otolithic membrane and stereocilia links**, proposing that focal detachment and altered ionic homeostasis at the apical surface of sensory epithelia may trigger tinnitus fluctuations and early vertigo attacks, with progression leading to otolithic membrane herniation and vestibular test dissociations. (parraperez2023typesofinheritance pages 1-2)

### 4.6 Epigenetics
The familial genetics review notes epigenetic findings (e.g., WGBS) suggesting altered DNA methylation in hearing-loss genes as potential modifiers, but specific methylation biomarkers were not extractable as validated clinical markers from the available excerpts. (parraperez2023typesofinheritance pages 2-4)

---

## 5. Environmental information

### 5.1 Environmental/lifestyle exposures associated with MD phenotype
* **Occupational noise exposure** (25.4% prevalence in a Finnish registry cohort) was associated with greater tinnitus/hyperacusis/hearing-loss impact. (pyykko2024associationofhead pages 1-2)
* **Head and neck trauma** were common and associated with specific complaint clusters (e.g., vestibular drop attacks; strain-induced vertigo; hyperacusis), though causality is not established by the retrospective design. (pyykko2024associationofhead pages 1-2)

### 5.2 Infectious agents
URI history is epidemiologically linked to MD incidence in a large national cohort; the study frames viral infection as a plausible contributor among multifactorial causes, but it does not identify a single pathogen as causal. (kwon2024epidemiologicalevidencefor pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Core pathological correlate: endolymphatic hydrops
Consensus and reviews link MD to **endolymphatic hydrops** (dilation/expansion of the endolymphatic space), while acknowledging that EH alone may not fully explain symptom variability and chronic progression. (lopezescamez2015diagnosticcriteriafor pages 1-2, basura2020clinicalpracticeguidelinea pages 1-2)

### 6.2 Imaging-based mechanistic insights (2023–2024)
Hydrops MRI is increasingly used as an in vivo biomarker of EH and related blood–labyrinth barrier changes:
* 2023 meta-analysis: combined **increased perilymphatic enhancement (PLE) + EH** was the best-performing descriptor combination with pooled sensitivity ~87% and specificity ~91% (subset). (connor2023delayedpostgadolinium pages 1-2)
* 2024 diagnostic optimization study: **saccular abnormality** was the best individual predictor (DOR 292.6), and a multi-descriptor model (saccule + asymmetric cochlear PLE + incomplete vestibular aqueduct visualization) achieved sensitivity 84.4%, specificity 97.4%, AUC 0.938. (connor2024assessingtheoptimal pages 1-3)
* A 2024 systematic review summarizes between-center variability and explicitly states: “**sensitivity (69%-92%) and specificity (78%-96%)**” vary by lab, reflecting selection and grading differences. (young2024potentialapplicationof pages 1-3)

### 6.3 Molecular pathways/cellular processes (evidence-supported themes)
Evidence-backed themes from genetics reviews and experimental model reviews include:
* **Ionic/fluid homeostasis** in endolymph and extracellular membranes (e.g., implied by tectorial/otolithic membrane ionic homeostasis hypothesis). (parraperez2023typesofinheritance pages 1-2)
* **Immune/inflammatory involvement** as a candidate contributor (reviews highlight immune loci and inflammatory signaling themes). (dai2023geneticadvancesin pages 6-7, dai2023geneticadvancesin pages 1-2)

### 6.4 Suggested ontology terms (mechanisms)
* **GO Biological Process (suggestions):** inner ear development/homeostasis; regulation of ion transport; mechanosensory behavior; inflammatory response.
* **Cell Ontology (CL) (suggestions):** auditory hair cell; vestibular hair cell; supporting cells; endolymphatic sac epithelial cell.

(These are ontology suggestions aligned to the mechanistic themes above; specific GO/CL IDs should be validated in the target ontology version.) (parraperez2023typesofinheritance pages 1-2, seo2020experimentalanimalmodels pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Primary structures
MD affects the **inner ear** (labyrinth), involving both cochlear and vestibular organs, consistent with the core symptom triad and imaging/histopathologic correlate of EH. (basura2020clinicalpracticeguidelinea pages 1-2, connor2023delayedpostgadolinium pages 1-2)

### 7.2 Substructures highlighted by modern imaging
Hydrops MRI work emphasizes compartment-specific findings (cochlear vs vestibular EH), and descriptors such as **saccular abnormality** (inferior vestibule) and cochlear perilymphatic enhancement. (connor2024assessingtheoptimal pages 1-3, lineraalperi2024isendolymphatichydrops pages 1-2)

### 7.3 UBERON / GO CC suggestions
* **UBERON (suggestions):** inner ear; cochlea; vestibule; saccule; utricle; semicircular canal; endolymphatic sac/duct.
* **GO Cellular Component (suggestions):** stereocilium; mechanosensory hair bundle; tectorial membrane; otolithic membrane.

(These are ontology suggestions consistent with genetic and imaging emphases.) (connor2024assessingtheoptimal pages 1-3, parraperez2023typesofinheritance pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
A clinical practice guideline states onset is most common between **40 and 60 years**. (basura2020clinicalpracticeguidelinea pages 1-2)

### 8.2 Course and staging concepts
MD is episodic with remissions; the guideline describes attack frequency often around **6–11 episodes/year** with remissions that may last months to years, and that diagnosis can require longitudinal observation because manifestations evolve over time. (basura2020clinicalpracticeguidelinea pages 1-2)

### 8.3 Recent natural-history evidence (2024)
* In a cohort of “intractable” unilateral definite MD (n=35), **64%** (21/33 with complete data) were free of vertigo attacks at follow-up after median disease duration 5.3 years, supporting attack resolution over time in many patients. (gerritsen2024theevolutionof pages 9-10)
* In a larger patient-organization cohort (n=365), **34%** reported spontaneous remission of episodic vertigo; however, balance problems and drop attacks could persist/worsen, supporting the need for comprehensive management beyond vertigo control alone. (pyykko2024changesinsymptom pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (ranges and variability)
* Guideline-cited prevalence: **~50–200 per 100,000 adults**. (basura2020clinicalpracticeguidelinea pages 1-2)
* A 2024 cohort paper summarizes wide reported incidence/prevalence variation across studies/regions and notes a South Korea increase from **30.02 to 118.48 per 100,000 (2013–2017)** (interpretation limited by coding/ascertainment). (kwon2024epidemiologicalevidencefor pages 1-2)

### 9.2 Bilateral involvement
Bilateral involvement frequency varies by definition and follow-up; an earlier large clinical review of bilateral MD notes reported ranges from **5–50%** depending on disease duration and other factors. (frejo2016clinicalsubgroupsin pages 1-2)

### 9.3 Familial proportion and inheritance
Familial MD accounts for **~5–20%** of cases in some cohorts (~10% overall) and can show AD/AR/multiallelic inheritance with incomplete penetrance. (parraperez2023typesofinheritance pages 1-2, parraperez2023typesofinheritance pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria (standard)
International diagnostic criteria define “definite” and “probable” MD using attack-duration thresholds, audiometric SNHL, fluctuating aural symptoms, and exclusion of alternative diagnoses. (lopezescamez2015diagnosticcriteriafor pages 2-4, basura2020clinicalpracticeguideline pages 1-2)

A guideline-derived criteria table image is available. (basura2020clinicalpracticeguideline media b1eac1f2)

### 10.2 Audiology and vestibular testing
The diagnostic criteria require **audiometric documentation** of low- to mid-frequency SNHL in the affected ear for definite MD. (lopezescamez2015diagnosticcriteriafor pages 2-4)

### 10.3 Hydrops MRI (2023–2024) — “latest research” and implementation
Hydrops MRI has transitioned from research use toward practical clinical adjunctive diagnosis:
* 2023 meta-analysis (66 studies; 3073 MD ears) identifies PLE + EH as best-performing pooled descriptor combination. (connor2023delayedpostgadolinium pages 1-2)
* 2024 European Radiology study identifies a small set of high-yield descriptors (saccular abnormality, asymmetric cochlear PLE, vestibular aqueduct visualization) achieving high specificity (~97%). (connor2024assessingtheoptimal pages 1-3)
* 2024 systematic review describes delayed IV gadolinium imaging and notes variability: “**sensitivity (69%-92%) and specificity (78%-96%)**.” (young2024potentialapplicationof pages 1-3)

**Direct abstract quote (hydrops MRI performance variability):** “The sensitivity (69%-92%) and specificity (78%-96%) values varied from each laboratory…” (young2024potentialapplicationof pages 1-3)

### 10.4 Differential diagnosis (high-level)
The Bárány criteria paper explicitly notes diagnostic complexity due to overlapping disorders and includes differentials such as autoimmune inner ear disease and genetic hearing loss conditions. (lopezescamez2015diagnosticcriteriafor pages 2-4)

---

## 11. Outcome / prognosis

### 11.1 Symptom evolution
Recent evidence supports that vertigo attacks often diminish over time, including in refractory cohorts. (gerritsen2024theevolutionof pages 9-10, pyykko2024changesinsymptom pages 1-2)

### 11.2 Functional morbidity
Balance problems, drop attacks, hearing loss, and mental health symptoms can persist even when episodic vertigo remits and are key drivers of reduced quality of life. (pyykko2024changesinsymptom pages 1-2)

---

## 12. Treatment

### 12.1 Treatment goals
Guidelines emphasize preventing/reducing vertigo, mitigating hearing loss/tinnitus/aural fullness, and improving quality of life. (basura2020clinicalpracticeguidelinea pages 1-2)

### 12.2 Intratympanic therapies (evidence prioritized)
**Gentamicin vs corticosteroids (2024 meta-analysis):** Across 12 studies (n=694), intratympanic gentamicin achieved higher vertigo control (RR 1.36, 95% CI 1.13–1.65) while corticosteroids better preserved hearing (pure tone average WMD 4.41 favoring steroids). (wu2024comparativeefficacyof pages 1-2)

### 12.3 Surgical/interventional therapies
**Selective vestibular neurectomy (2024 series):** In 23 refractory patients after failed endolymphatic sac surgery, micro-endoscopic selective vestibular neurectomy achieved ~90% vertigo control at up to 2 years and significant DHI improvement, with one CSF fistula reoperation and no definitive hearing loss/facial palsy reported in the series. (salvinelli2024selectivevestibularneurectomy pages 1-2)

### 12.4 Auditory rehabilitation
Cochlear implantation can improve multiple patient-reported outcomes (hearing, vertigo, tinnitus, QoL) in implanted MD patients in small retrospective cohorts (details available in retrieved abstract but not expanded in the current evidence snippets). (basura2020clinicalpracticeguidelinea pages 9-10)

### 12.5 Ongoing/registered clinical trials (real-world implementation)
* **PREDMEN (NCT05851508)**: Phase 3, multicenter, randomized, double-blind placebo-controlled trial (start 2023-10-01; planned n=148) of intratympanic methylprednisolone (62.5 mg/mL) vs saline; vertigo tracked daily via DizzyQuest app; outcomes include hearing measures, tinnitus instruments, EQ-5D, adverse events, and cost-effectiveness. (NCT05851508 chunk 1, NCT05851508 chunk 2)
* **NCT00802529**: Completed randomized quadruple-masked Phase 2/3 trial (n=60) comparing transtympanic methylprednisolone vs gentamicin with 18–24 month vertigo endpoints and serial hearing measures. (NCT00802529 chunk 1)

### 12.6 MAXO term suggestions (treatment ontology)
* Intratympanic drug administration (gentamicin; corticosteroid)
* Vestibular nerve section / vestibular neurectomy
* Cochlear implantation
* Lifestyle and dietary modification

(These are ontology suggestions aligned to guideline and trial interventions.) (salvinelli2024selectivevestibularneurectomy pages 1-2, NCT05851508 chunk 1, wu2024comparativeefficacyof pages 1-2)

---

## 13. Prevention
No definitive primary prevention is established; however, modifiable exposure and comorbidity management may be relevant given associations with URIs and exposure-related phenotype modifiers.
* URI–MD association suggests monitoring patients with recurrent URIs could be relevant for early recognition, though causal prevention is unproven. (kwon2024epidemiologicalevidencefor pages 1-2)
* Avoidance/mitigation of occupational noise exposure and management after head/neck trauma may reduce symptom burden in susceptible individuals, but evidence is observational. (pyykko2024associationofhead pages 1-2)

---

## 14. Other species / natural disease
The retrieved evidence did not identify a naturally occurring, clinically defined “Ménière’s disease” entity in non-human species; instead, animal work models the **endolymphatic hydrops** phenotype as an experimental analog. (seo2020experimentalanimalmodels pages 1-2)

---

## 15. Model organisms
Animal models are primarily designed to induce or measure endolymphatic hydrops (ELH/EH) and related cochlear/vestibular dysfunction.

### 15.1 Model types and species
* **Guinea pig**: historically central for surgical endolymphatic sac ablation models and other hydrops induction methods. (seo2020experimentalanimalmodels pages 1-2)
* **Mouse/rat**: used for systemic/hormonal induction (e.g., vasopressin-based models) and for molecular analyses, with interest in shifting from large-animal surgical models to smaller animals for omics-compatible workflows. (seo2020experimentalanimalmodels pages 1-2)

### 15.2 Induced models (examples)
A mini-review categorizes models into acute vs chronic ELH models and lists chronic induction via:
* Surgical **endolymphatic sac (ES) ablation**
* Systemic agents (e.g., **vasopressin**, aldosterone; inflammatory stimuli such as LPS)
These models are explicitly described as representing the ELH pathophysiological process. (seo2020experimentalanimalmodels pages 1-2)

### 15.3 Model limitations
The mini-review notes that available animal models do not fully replicate the fluctuating/episodic clinical course of human MD, motivating ongoing model development. (seo2020experimentalanimalmodels pages 1-2)

---

## Synthesis of recent (2023–2024) key evidence
The table below aggregates high-yield 2023–2024 evidence on diagnostics, genetics, epidemiology/risk, natural history, and treatment.

| Topic | Citation (first author year) | Publication date | Study type | N (if available) | Key quantitative findings | URL/DOI |
|---|---|---|---|---:|---|---|
| Diagnostics MRI | Connor 2023 (connor2023delayedpostgadolinium pages 1-2, connor2023delayedpostgadolinium pages 8-9) | May 2023 | Systematic review and meta-analysis | 66 studies; 3,073 ears with MD | Delayed post-gadolinium MRI descriptors were pooled; the combination of increased perilymphatic enhancement (PLE) + endolymphatic hydrops (EH) showed sensitivity ~87% and specificity ~91% for MD diagnosis. Several descriptors had pooled specificities >90%, including fused utricle/saccule (96%) and increased ipsilateral PLE (98%). | https://doi.org/10.1007/s00330-023-09651-8 |
| Diagnostics MRI | Connor 2024 (connor2024assessingtheoptimal pages 1-3) | Feb 2024 | Retrospective single-center case-control MRI study | 227 patients; 96 definite MD ears vs 78 control ears | Best individual MRI predictor was saccular abnormality with DOR 292.6. Combining saccular abnormality + asymmetric cochlear PLE + incomplete vestibular aqueduct visualization correctly classified 90.2% of cases; sensitivity 84.4%, specificity 97.4%, AUC 0.938. | https://doi.org/10.1007/s00330-024-10587-w |
| Diagnostics MRI | Young 2024 (young2024potentialapplicationof pages 1-3, young2024potentialapplicationof pages 9-9) | Jan 2024 | Systematic review | 80 relevant articles selected from 470 screened | Across centers, hydrops MRI performance varied with sensitivity 69%–92% and specificity 78%–96%. Main current uses: differentiate EH from sudden SNHL, determine affected side, and confirm EH with concomitant disorders. | https://doi.org/10.1177/19160216241250350 |
| Diagnostics MRI | Linera-Alperi 2024 (lineraalperi2024isendolymphatichydrops pages 1-2) | Dec 2024 | Retrospective longitudinal tertiary-center study | 137 unilateral MD patients | 40.15% classified as cochleocentric and 59.85% non-cochleocentric; vestibular EH was more severe in the non-cochleocentric group, supporting heterogeneity in hydropic patterns rather than a uniform cochleocentric progression model. | https://doi.org/10.3389/fneur.2024.1477282 |
| Diagnostics MRI / Phenotype correlation | Hu 2023 (hu2023endolymphatichydropsimaging pages 1-2) | Feb 2023 | Clinical imaging correlation study | 70 unilateral MD patients | Vestibular EH correlated positively with cochlear EH, hearing loss, VEMP, caloric test abnormalities, disease course, and vertigo duration; MRI also correlated with emotional burden measures (SAS/SDS via DHI emotional/total scores). | https://doi.org/10.1007/s00405-023-07899-w |
| Genetics | Parra-Perez 2023 (parraperez2023typesofinheritance pages 1-2, parraperez2023typesofinheritance pages 2-4, parraperez2023typesofinheritance pages 4-5) | Apr 2023 | Narrative review of familial MD genetics | Not applicable | Familial MD accounts for ~5%–20% of cases in European-descended cohorts and ~10% overall; key implicated genes include OTOG, MYO7A, TECTA, FAM136A, DTNA, PRKCB, COCH, DPT, and SEMA3D. Proposed inheritance includes AD, AR/compound recessive, digenic/multiallelic models, with incomplete penetrance and variable expressivity. | https://doi.org/10.1007/s10162-023-00896-0 |
| Genetics | Dai 2023 (dai2023geneticadvancesin pages 6-7, dai2023geneticadvancesin pages 1-2, dai2023geneticadvancesin pages 5-6) | Dec 2023 | Review | Not applicable | Review highlights rare variants in OTOG reported in 33% of familial MD in one series; also summarizes immune-associated loci, 6p21.33 signal rs4947296, and candidate genes linked to ion/fluid homeostasis, inflammation, and stereocilia integrity. | https://doi.org/10.1007/s11033-022-08149-8 |
| Epidemiology-Risk | Kwon 2024 (kwon2024epidemiologicalevidencefor pages 1-2) | Oct 2024 | Nationwide matched cohort study | 19,721 MD cases; 78,884 matched controls | A URI within 1 year before index date was associated with a 2.01-fold greater likelihood of MD (95% CI 1.91–2.11); URI within 2 years remained associated (1.54-fold; 95% CI 1.50–1.59). Review text also notes wide regional epidemiologic variability (3–513 per 100,000 annually). | https://doi.org/10.3390/microorganisms12102047 |
| Epidemiology-Risk | Basura 2020 guideline (basura2020clinicalpracticeguidelinea pages 1-2) | Apr 2020 | Clinical practice guideline | Not applicable | Commonly cited prevalence range is ~50–200 per 100,000 adults; onset is most common between ages 40 and 60 years; attack frequency is often ~6–11 episodes/year, with remissions that may last months to years. | https://doi.org/10.1177/0194599820909438 |
| Natural history | Gerritsen 2024 (gerritsen2024theevolutionof pages 9-10) | Oct 2024 | Retrospective cohort | 35 intractable unilateral definite MD patients | Of 33 patients with complete attack data, 21 (64%) were free of vertigo attacks at follow-up after a median disease duration of 5.3 years, supporting spontaneous reduction of attacks over time even in refractory cohorts. | https://doi.org/10.3389/fneur.2024.1469276 |
| Natural history / QoL | Pyykkö 2024 (basura2020clinicalpracticeguidelinea pages 1-2) | Nov 2024 | Cross-sectional registry/questionnaire study | 365/560 surveyed definite MD patients | Spontaneous remission from episodic vertigo occurred in 34%; bilateral hearing loss developed in 34.5% long term; 65.5% reported balance issues, 34% mild vestibular drop attacks, and 10% severe falls; QoL was worst with constant dizziness. | https://doi.org/10.3389/fneur.2024.1496384 |
| Treatment | Wu 2024 (wu2024comparativeefficacyof pages 1-2) | Sep 2024 | Systematic review and meta-analysis | 12 studies; 694 patients | Intratympanic gentamicin showed superior vertigo control versus corticosteroids overall (RR 1.36, 95% CI 1.13–1.65) and at 6 months (RR 1.69, 95% CI 1.28–2.24), while corticosteroids better preserved hearing/pure-tone average (WMD 4.41, 95% CI 3.31–5.52). | https://doi.org/10.3389/fneur.2024.1471010 |
| Treatment | Salvinelli 2024 (salvinelli2024selectivevestibularneurectomy pages 1-2) | Apr 2024 | Retrospective surgical series | 23 patients | Selective vestibular neurectomy after failed sac surgery achieved ~90% vertigo control at up to 2 years, with significant DHI improvement (p=0.001), no definitive facial palsy or hearing loss reported, and one CSF fistula requiring reoperation. | https://doi.org/10.3390/brainsci14040369 |
| Treatment / Trial | NCT05851508 PREDMEN (NCT05851508 chunk 1, NCT05851508 chunk 2) | Trial start Oct 2023; estimated primary completion May 2026 | Multicenter randomized double-blind placebo-controlled phase 3 trial | Planned 148 participants | Two intratympanic methylprednisolone injections (62.5 mg/mL) vs saline placebo; primary outcome is control of vertigo spells tracked daily with the DizzyQuest app. Secondary outcomes include PTA, speech discrimination, THI/TFI, EQ-5D/EQ-VAS, adverse events, co-interventions, and cost-effectiveness. | https://clinicaltrials.gov/study/NCT05851508 |
| Treatment / Trial | NCT00802529 (NCT00802529 chunk 1, NCT00802529 chunk 2) | Completed; primary completion May 2015 | Randomized quadruple-masked phase 2/3 trial | 60 participants | Head-to-head transtympanic methylprednisolone vs gentamicin in refractory unilateral MD; primary endpoint was vertigo attacks at 18–24 months relative to 6-month baseline, with serial hearing and speech discrimination follow-up. | https://clinicaltrials.gov/study/NCT00802529 |


*Table: This table summarizes high-yield recent clinical and research evidence on Ménière’s disease across diagnostics, genetics, epidemiology, natural history, and treatment. It prioritizes the most relevant 2023–2024 sources and key trial records for rapid knowledge-base curation.*

---

## Notes on citation requirements (PMID)
PMIDs were not consistently available in the retrieved text snippets and tool outputs; therefore, this report cites by internal evidence context IDs linked to peer-reviewed articles and trial registry records, each containing DOI/URL and publication month/year in the retrieved metadata.

## URLs and publication dates (examples)
* Basura et al., **Apr 2020**, Clinical Practice Guideline: Ménière’s Disease. https://doi.org/10.1177/0194599820909438 (basura2020clinicalpracticeguidelinea pages 9-10)
* Lopez-Escamez et al., **Mar 2015**, Bárány diagnostic criteria. https://doi.org/10.3233/ves-150549 (lopezescamez2015diagnosticcriteriafor pages 2-4)
* Connor et al., **May 2023**, delayed post-gadolinium MRI meta-analysis. https://doi.org/10.1007/s00330-023-09651-8 (connor2023delayedpostgadolinium pages 1-2)
* Connor et al., **Feb 2024**, optimal MRI descriptors (saccular abnormality). https://doi.org/10.1007/s00330-024-10587-w (connor2024assessingtheoptimal pages 1-3)
* Parra-Perez & Lopez-Escamez, **Apr 2023**, familial MD genetics. https://doi.org/10.1007/s10162-023-00896-0 (parraperez2023typesofinheritance pages 1-2)
* Kwon et al., **Oct 2024**, URI risk cohort. https://doi.org/10.3390/microorganisms12102047 (kwon2024epidemiologicalevidencefor pages 1-2)
* Wu et al., **Sep 2024**, intratympanic gentamicin vs steroids meta-analysis. https://doi.org/10.3389/fneur.2024.1471010 (wu2024comparativeefficacyof pages 1-2)
* PREDMEN trial, **start Oct 2023**, NCT05851508. https://clinicaltrials.gov/study/NCT05851508 (NCT05851508 chunk 1)


References

1. (basura2020clinicalpracticeguidelinea pages 9-10): Gregory J. Basura, Meredith E. Adams, Ashkan Monfared, Seth R. Schwartz, Patrick J. Antonelli, Robert Burkard, Matthew L. Bush, Julie Bykowski, Maria Colandrea, Jennifer Derebery, Elizabeth A. Kelly, Kevin A. Kerber, Charles F. Koopman, Amy Angie Kuch, Evie Marcolini, Brian J. McKinnon, Michael J. Ruckenstein, Carla V. Valenzuela, Alexis Vosooney, Sandra A. Walsh, Lorraine C. Nnacheta, Nui Dhepyasuwan, and Erin M. Buchanan. Clinical practice guideline: ménière’s disease. Otolaryngology–Head and Neck Surgery, 162:S1-S55, Apr 2020. URL: https://doi.org/10.1177/0194599820909438, doi:10.1177/0194599820909438. This article has 555 citations.

2. (lopezescamez2015diagnosticcriteriafor pages 2-4): Jose A. Lopez-Escamez, John Carey, Won-Ho Chung, Joel A. Goebel, Måns Magnusson, Marco Mandalà, David E. Newman-Toker, Michael Strupp, Mamoru Suzuki, Franco Trabalzini, and Alexandre Bisdorff. Diagnostic criteria for menière's disease. Journal of Vestibular Research, 25:1-7, Mar 2015. URL: https://doi.org/10.3233/ves-150549, doi:10.3233/ves-150549. This article has 1866 citations.

3. (basura2020clinicalpracticeguideline pages 1-2): Gregory J. Basura, Meredith E. Adams, Ashkan Monfared, Seth R. Schwartz, Patrick J. Antonelli, Robert Burkard, Matthew L. Bush, Julie Bykowski, Maria Colandrea, Jennifer Derebery, Elizabeth A. Kelly, Kevin A. Kerber, Charles F. Koopman, Amy Angie Kuch, Evie Marcolini, Brian J. McKinnon, Michael J. Ruckenstein, Carla V. Valenzuela, Alexis Vosooney, Sandra A. Walsh, Lorraine C. Nnacheta, Nui Dhepyasuwan, and Erin M. Buchanan. Clinical practice guideline: ménière’s disease executive summary. Otolaryngology–Head and Neck Surgery, 162:415-434, Apr 2020. URL: https://doi.org/10.1177/0194599820909439, doi:10.1177/0194599820909439. This article has 126 citations.

4. (connor2024assessingtheoptimal pages 1-3): Steve Connor, Irumee Pai, Philip Touska, Sarah McElroy, Sebastien Ourselin, and Joseph V. Hajnal. Assessing the optimal mri descriptors to diagnose ménière’s disease and the added value of analysing the vestibular aqueduct. European Radiology, 34:6060-6071, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10587-w, doi:10.1007/s00330-024-10587-w. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (connor2023delayedpostgadolinium pages 1-2): Steve Connor, Mariusz T. Grzeda, Babak Jamshidi, Sebastien Ourselin, Joseph V. Hajnal, and Irumee Pai. Delayed post gadolinium mri descriptors for meniere’s disease: a systematic review and meta-analysis. European Radiology, 33:7113-7135, May 2023. URL: https://doi.org/10.1007/s00330-023-09651-8, doi:10.1007/s00330-023-09651-8. This article has 33 citations and is from a domain leading peer-reviewed journal.

6. (parraperez2023typesofinheritance pages 1-2): Alberto M. Parra-Perez and Jose A. Lopez-Escamez. Types of inheritance and genes associated with familial meniere disease. JARO: Journal of the Association for Research in Otolaryngology, 24:269-279, Apr 2023. URL: https://doi.org/10.1007/s10162-023-00896-0, doi:10.1007/s10162-023-00896-0. This article has 48 citations and is from a domain leading peer-reviewed journal.

7. (kwon2024epidemiologicalevidencefor pages 2-3): Mi Jung Kwon, Ho Suk Kang, Joo-Hee Kim, Ji Hee Kim, Woo Jin Bang, Dae Myoung Yoo, Na-Eun Lee, Kyeong Min Han, Nan Young Kim, Hyo Geun Choi, Min-Jeong Kim, and Eun Soo Kim. Epidemiological evidence for upper respiratory infections as a potential risk factor for meniere’s disease: a korean national health sample cohort study. Microorganisms, 12:2047, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102047, doi:10.3390/microorganisms12102047. This article has 2 citations.

8. (NCT00802529 chunk 2):  Transtympanic Gentamicin vs. Steroids in Refractory Meniere's Disease. Imperial College London. 2009. ClinicalTrials.gov Identifier: NCT00802529

9. (basura2020clinicalpracticeguidelinea pages 1-2): Gregory J. Basura, Meredith E. Adams, Ashkan Monfared, Seth R. Schwartz, Patrick J. Antonelli, Robert Burkard, Matthew L. Bush, Julie Bykowski, Maria Colandrea, Jennifer Derebery, Elizabeth A. Kelly, Kevin A. Kerber, Charles F. Koopman, Amy Angie Kuch, Evie Marcolini, Brian J. McKinnon, Michael J. Ruckenstein, Carla V. Valenzuela, Alexis Vosooney, Sandra A. Walsh, Lorraine C. Nnacheta, Nui Dhepyasuwan, and Erin M. Buchanan. Clinical practice guideline: ménière’s disease. Otolaryngology–Head and Neck Surgery, 162:S1-S55, Apr 2020. URL: https://doi.org/10.1177/0194599820909438, doi:10.1177/0194599820909438. This article has 555 citations.

10. (lopezescamez2015diagnosticcriteriafor pages 1-2): Jose A. Lopez-Escamez, John Carey, Won-Ho Chung, Joel A. Goebel, Måns Magnusson, Marco Mandalà, David E. Newman-Toker, Michael Strupp, Mamoru Suzuki, Franco Trabalzini, and Alexandre Bisdorff. Diagnostic criteria for menière's disease. Journal of Vestibular Research, 25:1-7, Mar 2015. URL: https://doi.org/10.3233/ves-150549, doi:10.3233/ves-150549. This article has 1866 citations.

11. (NCT05851508 chunk 1): Babette F van Esch, MD, PhD. The Effecttiveness of Intratympanic Methylprednisolon Injections Compared to Placebo in the Treatment of Vertigo Attacks in Meniere's Disease. Leiden University Medical Center. 2023. ClinicalTrials.gov Identifier: NCT05851508

12. (kwon2024epidemiologicalevidencefor pages 1-2): Mi Jung Kwon, Ho Suk Kang, Joo-Hee Kim, Ji Hee Kim, Woo Jin Bang, Dae Myoung Yoo, Na-Eun Lee, Kyeong Min Han, Nan Young Kim, Hyo Geun Choi, Min-Jeong Kim, and Eun Soo Kim. Epidemiological evidence for upper respiratory infections as a potential risk factor for meniere’s disease: a korean national health sample cohort study. Microorganisms, 12:2047, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102047, doi:10.3390/microorganisms12102047. This article has 2 citations.

13. (pyykko2024associationofhead pages 1-2): Ilmari Pyykkö, Vinay Vinay, Artur Vetkas, Jing Zou, and Vinaya Manchaiah. Association of head injury, neck injury or acoustic trauma on phenotype of ménière’s disease. Audiology Research, 14:204-216, Feb 2024. URL: https://doi.org/10.3390/audiolres14010019, doi:10.3390/audiolres14010019. This article has 2 citations.

14. (parraperez2023typesofinheritance pages 2-4): Alberto M. Parra-Perez and Jose A. Lopez-Escamez. Types of inheritance and genes associated with familial meniere disease. JARO: Journal of the Association for Research in Otolaryngology, 24:269-279, Apr 2023. URL: https://doi.org/10.1007/s10162-023-00896-0, doi:10.1007/s10162-023-00896-0. This article has 48 citations and is from a domain leading peer-reviewed journal.

15. (parraperez2023typesofinheritance pages 4-5): Alberto M. Parra-Perez and Jose A. Lopez-Escamez. Types of inheritance and genes associated with familial meniere disease. JARO: Journal of the Association for Research in Otolaryngology, 24:269-279, Apr 2023. URL: https://doi.org/10.1007/s10162-023-00896-0, doi:10.1007/s10162-023-00896-0. This article has 48 citations and is from a domain leading peer-reviewed journal.

16. (dai2023geneticadvancesin pages 5-6): Qingqing Dai, Lili Long, Hui Zhao, Ruikai Wang, Hong Zheng, and Maoli Duan. Genetic advances in meniere disease. Molecular Biology Reports, 50:2901-2908, Dec 2023. URL: https://doi.org/10.1007/s11033-022-08149-8, doi:10.1007/s11033-022-08149-8. This article has 25 citations and is from a peer-reviewed journal.

17. (goebel20162015equilibriumcommittee pages 2-2): Joel A Goebel. 2015 equilibrium committee amendment to the 1995 aao-hns guidelines for the definition of ménière’s disease. Otolaryngology–Head and Neck Surgery, 154:403-404, Feb 2016. URL: https://doi.org/10.1177/0194599816628524, doi:10.1177/0194599816628524. This article has 205 citations.

18. (basura2020clinicalpracticeguideline media b1eac1f2): Gregory J. Basura, Meredith E. Adams, Ashkan Monfared, Seth R. Schwartz, Patrick J. Antonelli, Robert Burkard, Matthew L. Bush, Julie Bykowski, Maria Colandrea, Jennifer Derebery, Elizabeth A. Kelly, Kevin A. Kerber, Charles F. Koopman, Amy Angie Kuch, Evie Marcolini, Brian J. McKinnon, Michael J. Ruckenstein, Carla V. Valenzuela, Alexis Vosooney, Sandra A. Walsh, Lorraine C. Nnacheta, Nui Dhepyasuwan, and Erin M. Buchanan. Clinical practice guideline: ménière’s disease. Otolaryngology–Head and Neck Surgery, 162:S1-S55, Apr 2020. URL: https://doi.org/10.1177/0194599820909438, doi:10.1177/0194599820909438. This article has 555 citations.

19. (pyykko2024changesinsymptom pages 1-2): Ilmari Pyykkö, Jing Zou, and Nora Vetkas. Changes in symptom pattern in meniere's disease by duration: the need for comprehensive management. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1496384, doi:10.3389/fneur.2024.1496384. This article has 12 citations and is from a peer-reviewed journal.

20. (hu2023endolymphatichydropsimaging pages 1-2): Ying Hu, Yue Zhang, Xu Zhao, and Juan Li. Endolymphatic hydrops imaging and correlation with clinical characteristics, audiovestibular function and mental impairment in patients with meniere’s disease. European Archives of Oto-Rhino-Laryngology, 280:4027-4036, Feb 2023. URL: https://doi.org/10.1007/s00405-023-07899-w, doi:10.1007/s00405-023-07899-w. This article has 19 citations and is from a peer-reviewed journal.

21. (dai2023geneticadvancesin pages 1-2): Qingqing Dai, Lili Long, Hui Zhao, Ruikai Wang, Hong Zheng, and Maoli Duan. Genetic advances in meniere disease. Molecular Biology Reports, 50:2901-2908, Dec 2023. URL: https://doi.org/10.1007/s11033-022-08149-8, doi:10.1007/s11033-022-08149-8. This article has 25 citations and is from a peer-reviewed journal.

22. (young2024potentialapplicationof pages 1-3): Yi-Ho Young and Kao-Tsung Lin. Potential application of hydrops mr imaging: a systematic review. Journal of Otolaryngology - Head & Neck Surgery, Jan 2024. URL: https://doi.org/10.1177/19160216241250350, doi:10.1177/19160216241250350. This article has 12 citations.

23. (dai2023geneticadvancesin pages 6-7): Qingqing Dai, Lili Long, Hui Zhao, Ruikai Wang, Hong Zheng, and Maoli Duan. Genetic advances in meniere disease. Molecular Biology Reports, 50:2901-2908, Dec 2023. URL: https://doi.org/10.1007/s11033-022-08149-8, doi:10.1007/s11033-022-08149-8. This article has 25 citations and is from a peer-reviewed journal.

24. (seo2020experimentalanimalmodels pages 1-2): Young Joon Seo and Daniel Brown. Experimental animal models for meniere’s disease: a mini-review. Journal of Audiology and Otology, 24:53-60, Apr 2020. URL: https://doi.org/10.7874/jao.2020.00115, doi:10.7874/jao.2020.00115. This article has 28 citations.

25. (lineraalperi2024isendolymphatichydrops pages 1-2): Marta Álvarez De Linera-Alperi, Pablo Dominguez, Melissa Blanco-Pareja, Pablo Menéndez Fernández-Miranda, Raquel Manrique-Huarte, Gloria Liaño, Nicolas Pérez-Fernández, and Víctor Suárez-Vega. Is endolymphatic hydrops, as detected in mri, a truly cochleocentric finding? Frontiers in Neurology, Dec 2024. URL: https://doi.org/10.3389/fneur.2024.1477282, doi:10.3389/fneur.2024.1477282. This article has 5 citations and is from a peer-reviewed journal.

26. (gerritsen2024theevolutionof pages 9-10): F. R. Gerritsen, A. A. Schenck, H. Locher, R. van de Berg, P. P. van Benthem, and H. M. Blom. The evolution of intractable ménière’s disease: attacks resolve over time. Frontiers in Neurology, Oct 2024. URL: https://doi.org/10.3389/fneur.2024.1469276, doi:10.3389/fneur.2024.1469276. This article has 4 citations and is from a peer-reviewed journal.

27. (frejo2016clinicalsubgroupsin pages 1-2): Lidia Frejo, Andres Soto-Varela, Sofía Santos-Perez, Ismael Aran, Angel Batuecas-Caletrio, Vanesa Perez-Guillen, Herminio Perez-Garrigues, Jesus Fraile, Eduardo Martin-Sanz, Maria C. Tapia, Gabriel Trinidad, Ana María García-Arumi, Rocío González-Aguado, Juan M. Espinosa-Sanchez, Pedro Marques, Paz Perez, Jesus Benitez, and Jose A. Lopez-Escamez. Clinical subgroups in bilateral meniere disease. Frontiers in Neurology, Oct 2016. URL: https://doi.org/10.3389/fneur.2016.00182, doi:10.3389/fneur.2016.00182. This article has 175 citations and is from a peer-reviewed journal.

28. (wu2024comparativeefficacyof pages 1-2): Xuanmei Wu, Jiacheng Shui, Chengyuan Liu, Xinyue Wu, Ying Yu, Hanyu Wang, and Cong Yan. Comparative efficacy of intratympanic gentamicin and intratympanic corticosteroid in the treatment of meniere’s disease: a systematic review and meta-analysis. Frontiers in Neurology, Sep 2024. URL: https://doi.org/10.3389/fneur.2024.1471010, doi:10.3389/fneur.2024.1471010. This article has 6 citations and is from a peer-reviewed journal.

29. (salvinelli2024selectivevestibularneurectomy pages 1-2): Fabrizio Salvinelli, Francesca Bonifacio, Mara Capece, Denis Aiudi, Alessio Iacoangeli, Fabio Greco, Maurizio Gladi, and Maurizio Iacoangeli. Selective vestibular neurectomy through the presigmoid retrolabyrinthine approach in the treatment of meniere’s disease. Brain Sciences, 14:369, Apr 2024. URL: https://doi.org/10.3390/brainsci14040369, doi:10.3390/brainsci14040369. This article has 3 citations.

30. (NCT05851508 chunk 2): Babette F van Esch, MD, PhD. The Effecttiveness of Intratympanic Methylprednisolon Injections Compared to Placebo in the Treatment of Vertigo Attacks in Meniere's Disease. Leiden University Medical Center. 2023. ClinicalTrials.gov Identifier: NCT05851508

31. (NCT00802529 chunk 1):  Transtympanic Gentamicin vs. Steroids in Refractory Meniere's Disease. Imperial College London. 2009. ClinicalTrials.gov Identifier: NCT00802529

32. (connor2023delayedpostgadolinium pages 8-9): Steve Connor, Mariusz T. Grzeda, Babak Jamshidi, Sebastien Ourselin, Joseph V. Hajnal, and Irumee Pai. Delayed post gadolinium mri descriptors for meniere’s disease: a systematic review and meta-analysis. European Radiology, 33:7113-7135, May 2023. URL: https://doi.org/10.1007/s00330-023-09651-8, doi:10.1007/s00330-023-09651-8. This article has 33 citations and is from a domain leading peer-reviewed journal.

33. (young2024potentialapplicationof pages 9-9): Yi-Ho Young and Kao-Tsung Lin. Potential application of hydrops mr imaging: a systematic review. Journal of Otolaryngology - Head & Neck Surgery, Jan 2024. URL: https://doi.org/10.1177/19160216241250350, doi:10.1177/19160216241250350. This article has 12 citations.
