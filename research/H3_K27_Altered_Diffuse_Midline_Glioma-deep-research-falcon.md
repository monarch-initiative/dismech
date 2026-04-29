---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T15:39:16.064999'
end_time: '2026-04-05T15:49:04.719582'
duration_seconds: 588.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diffuse Midline Glioma, H3 K27-Altered
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 70
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diffuse Midline Glioma, H3 K27-Altered
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Diffuse Midline Glioma, H3 K27-Altered** covering all of the
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
- **Disease Name:** Diffuse Midline Glioma, H3 K27-Altered
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Diffuse Midline Glioma, H3 K27-Altered** covering all of the
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


## Comprehensive Disease Characteristics Research Report

### Target Disease
- **Disease name:** Diffuse midline glioma, H3 K27-altered (DMG, H3 K27-altered)
- **MONDO ID:** **MONDO:1060171** (vallero2023pediatricdiffusemidline pages 2-3)
- **Category:** Pediatric-type diffuse high-grade glioma (CNS WHO grade 4), can also occur in adults (gianno2022paediatrictypediffusehighgrade pages 1-2, schulte2020clinicalradiologicand pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview
Diffuse midline glioma, H3 K27-altered is an infiltrative midline glioma defined by H3K27-pathway disruption (loss of H3K27 trimethylation) and is assigned **CNS WHO grade 4 regardless of histologic features**. It most commonly arises in midline CNS structures such as the **pons/brainstem (historically “DIPG”), thalamus, and spinal cord** and carries a poor prognosis, especially in children. (park2023the2021who pages 2-2, park2023the2021who pages 6-7, vallero2023pediatricdiffusemidline pages 2-3)

### 1.2 Key identifiers and ontology mapping
- **MONDO:** MONDO:1060171 (vallero2023pediatricdiffusemidline pages 2-3)
- **WHO CNS classification:** WHO CNS5 (2021), pediatric-type diffuse high-grade glioma family; DMG, H3 K27-altered is a tumor type within this family (gianno2022paediatrictypediffusehighgrade pages 1-2)
- **Diagnostic molecular criteria (WHO CNS5-aligned):** midline location plus **H3 K27M mutation OR EZHIP overexpression OR EGFR alteration** → “diffuse midline glioma, H3 K27-altered” (park2023the2021who pages 2-2)

**Not retrieved in this tool session:** ICD-10/ICD-11 codes, MeSH IDs, Orphanet IDs, OMIM disease entry IDs. These may exist but were not present in the provided full-text evidence chunks.

### 1.3 Common synonyms / alternative names
- “Diffuse midline glioma, H3 K27M-mutant” (WHO 2016 name)
- “Diffuse intrinsic pontine glioma (DIPG)” (clinical/radiologic term for pontine cases)
- “H3K27-altered diffuse midline glioma”
(wisniewski2023h3k27maltereddiffuse pages 1-3, vallero2023pediatricdiffusemidline pages 2-3)

### 1.4 Evidence source types
The synthesis below is derived from **aggregated resources**: multicenter and single-center retrospective cohorts, systematic reviews, and contemporary narrative reviews, plus trial registry entries (ClinicalTrials.gov). (hayashi2024neuroradiologicalgeneticand pages 1-2, damodharan2023molecularcharacterizationand pages 1-2, NCT04808245 chunk 1, NCT04196413 chunk 2)

| Preferred name | MONDO ID | WHO CNS grade / WHO 2021 (CNS5) definition criteria | Major synonyms / alternative names | Typical midline anatomical sites | Key references (year; DOI URL; PMID if available) |
|---|---|---|---|---|---|
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | CNS WHO grade 4. WHO CNS5 defines this as an infiltrative/diffuse midline glioma with loss of H3K27me3 and one of the following molecular features: H3 p.K28M (K27M) alteration in histone H3 isoforms, EZHIP overexpression, or EGFR alteration; diagnosis should be restricted to diffuse, midline, astrocytic tumors. (park2023the2021who pages 2-2, gue2024the2021world pages 15-16, broggi2024clinico–pathologicalfeaturesof pages 1-2, wisniewski2023h3k27maltereddiffuse pages 1-3, park2023the2021who pages 6-7) | Diffuse midline glioma, H3 K27M-mutant; DMG, H3 K27-altered; H3K27-altered diffuse midline glioma; diffuse intrinsic pontine glioma (DIPG; historical/clinical term, especially for pontine tumors); pediatric-type diffuse high-grade glioma, H3 K27-altered subset. (vallero2023pediatricdiffusemidline pages 2-3, nonnenbroich2024h3k27altereddiffusemidline pages 1-2, wisniewski2023h3k27maltereddiffuse pages 1-3, park2023the2021who pages 7-7) | Pons/brainstem (classic DIPG location), thalamus, spinal cord; other reported midline sites include cerebellum, third ventricle, mesencephalon, and multifocal midline locations. (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2, schulte2020clinicalradiologicand pages 1-2, hayashi2024neuroradiologicalgeneticand pages 1-2) | Vallero et al. 2023; https://doi.org/10.3389/fonc.2022.1082062; PMID not provided. (vallero2023pediatricdiffusemidline pages 2-3) |
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | WHO CNS5 renamed the 2016 entity “diffuse midline glioma, H3 K27M-mutant” to “diffuse midline glioma, H3 K27-altered” to encompass additional mechanisms causing H3 K27 hypomethylation beyond canonical H3K27M mutation. (gue2024the2021world pages 15-16, wisniewski2023h3k27maltereddiffuse pages 1-3, park2023the2021who pages 6-7) | Former WHO 2016 name: diffuse midline glioma, H3 K27M-mutant; older umbrella clinical usage: DIPG for pontine cases. (wisniewski2023h3k27maltereddiffuse pages 1-3, park2023the2021who pages 7-7) | Midline CNS structures, especially pons, thalamus, spinal cord. (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2, hayashi2024neuroradiologicalgeneticand pages 1-2) | Gianno et al. 2022; https://doi.org/10.32074/1591-951x-830; PMID not provided. (gianno2022paediatrictypediffusehighgrade pages 1-2) |
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | WHO-recognized molecular subtypes/mechanisms include: H3.3 p.K28M (H3F3A), H3.1/H3.2 p.K28M (HIST1H3B/HIST1H3C), H3-wildtype with EZHIP overexpression, and EGFR-altered tumors; all are assigned grade 4 regardless of histology. (gue2024the2021world pages 15-16, gianno2022paediatrictypediffusehighgrade pages 1-2, park2023the2021who pages 6-7) | H3.3 K27M DMG; H3.1/H3.2 K27M DMG; H3-wildtype/EZHIP-overexpressing DMG; EGFR-altered DMG. (gue2024the2021world pages 15-16, gianno2022paediatrictypediffusehighgrade pages 1-2, park2023the2021who pages 6-7) | Brainstem/pons, thalamus, spinal cord; age/site patterns differ by subtype, with pontine predominance in many pediatric H3.1/H3.2 cases and broader midline distribution in H3.3 cases. (vallero2023pediatricdiffusemidline pages 2-3, gianno2022paediatrictypediffusehighgrade pages 1-2) | Park et al. 2023; https://doi.org/10.1002/jmri.28740; PMID not provided. (park2023the2021who pages 2-2, park2023the2021who pages 6-7) |
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | Diagnostic pathology commonly uses immunohistochemistry for H3 K27M, H3 K27me3 loss, and EZHIP; diffuse strong H3 K27M staining with H3K27me3 loss supports diagnosis when integrated with diffuse midline astrocytic morphology. (broggi2024clinico–pathologicalfeaturesof pages 1-2) | H3 K27M-positive diffuse midline glioma; H3K27me3-loss diffuse midline glioma (descriptor, not a formal synonym on its own). (broggi2024clinico–pathologicalfeaturesof pages 1-2, wisniewski2023h3k27maltereddiffuse pages 1-3) | Same midline locations; pathology emphasis does not alter anatomic distribution. (broggi2024clinico–pathologicalfeaturesof pages 1-2) | Broggi et al. 2024; https://doi.org/10.3390/diagnostics14232617; PMID not provided. (broggi2024clinico–pathologicalfeaturesof pages 1-2) |
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | Review sources emphasize that although DMG is classified as a pediatric-type diffuse high-grade glioma, it also occurs in adults; adult series show thalamic predominance more often than pediatric series, which are often pontine. (broggi2024clinico–pathologicalfeaturesof pages 1-2, schulte2020clinicalradiologicand pages 1-2, park2023the2021who pages 6-7) | Adult diffuse midline glioma, H3 K27-altered; pediatric diffuse midline glioma, H3 K27-altered. (broggi2024clinico–pathologicalfeaturesof pages 1-2, schulte2020clinicalradiologicand pages 1-2) | Adults: commonly thalamus; children: often pons/brainstem; spinal cord occurs in both. (broggi2024clinico–pathologicalfeaturesof pages 1-2, schulte2020clinicalradiologicand pages 1-2, hayashi2024neuroradiologicalgeneticand pages 1-2) | Schulte et al. 2020; https://doi.org/10.1093/noajnl/vdaa142; PMID not provided. (schulte2020clinicalradiologicand pages 1-2) |
| Diffuse midline glioma, H3 K27-altered | MONDO:1060171 | Concise WHO-style definition quoted in review literature: “An infiltrative midline glioma with loss of H3 p.K28me3 (K27me3) and either an H3 c.83A>T p.K28M substitution in one of the histone H3 isoforms, aberrant overexpression of EZHIP, or an EGFR mutation.” (wisniewski2023h3k27maltereddiffuse pages 1-3) | DMG H3 K27-altered; previously DMG H3 K27M-mutant. (wisniewski2023h3k27maltereddiffuse pages 1-3) | Midline CNS, especially pons, thalamus, spinal cord. (wisniewski2023h3k27maltereddiffuse pages 1-3) | Wiśniewski et al. 2023; https://doi.org/10.1055/s-0043-1771192; PMID not provided. (wisniewski2023h3k27maltereddiffuse pages 1-3) |


*Table: This table summarizes the core identifiers, nomenclature changes, WHO CNS5 diagnostic criteria, synonyms, and typical anatomical sites for diffuse midline glioma, H3 K27-altered. It is useful as a compact reference for disease ontology and naming normalization in a knowledge base.*

---

## 2. Etiology

### 2.1 Primary causal factors
DMG, H3 K27-altered is primarily driven by **somatic** alterations affecting histone H3 lysine-27 regulation, most commonly a **K27M missense substitution** in histone H3 genes, leading to epigenetic dysregulation. (mandorino2024pediatricdiffusemidline pages 1-2, gue2024the2021world pages 15-16)

### 2.2 Risk factors
- **Genetic risk factors (germline):** No consistent inherited causal variants were identified in the retrieved sources; the defining events are described as tumor somatic alterations. (mandorino2024pediatricdiffusemidline pages 1-2, gue2024the2021world pages 15-16)
- **Environmental risk factors:** No specific environmental exposures were identified in the retrieved evidence.

### 2.3 Protective factors
No validated protective factors (genetic or environmental) were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (especially pontine/brainstem cases)
A common presentation—classically described for DIPG/brainstem DMG—includes **cranial neuropathies, long-tract (pyramidal) signs, and ataxia**. Vallero et al. additionally specify long-tract findings such as **hyperreflexia, clonus, increased tone, and Babinski sign**. (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2)

Mandorino et al. (2024) highlight pediatric presentations including **coordination problems, limb weakness, speech difficulties, and vision impairment**. (mandorino2024pediatricdiffusemidline pages 1-2)

### 3.2 Age of onset and course
- Predominantly a pediatric disease; pediatric DMG/DIPG often affects children in early childhood/school age (e.g., 4–9 years in one review). (mandorino2024pediatricdiffusemidline pages 1-2, vallero2023pediatricdiffusemidline pages 2-3)
- Adults are also affected, with adult cohorts showing frequent thalamic involvement and longer median survival than historical pediatric cohorts. (schulte2020clinicalradiologicand pages 1-2, broggi2024clinico–pathologicalfeaturesof pages 1-2)

### 3.3 Suggested HPO mappings
| Clinical feature | Phenotype type (symptom/sign) | Typical age/setting | Frequency or qualitative note | Suggested HPO term(s) |
|---|---|---|---|---|
| Cranial nerve palsy / multiple cranial neuropathies | Sign | Most typical in pediatric pontine/brainstem DMG (classic DIPG presentation); also described in adult brainstem cases | Part of the classic DIPG triad; commonly reported at presentation in pontine disease (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2) | Cranial nerve palsy [HP:0006999]; Abducens nerve palsy [HP:0001260]; Facial palsy [HP:0010628] |
| Long-tract signs / pyramidal tract dysfunction | Sign | Common in pediatric and adult brainstem DMG/DIPG | Part of the classic DIPG triad; often includes hyperreflexia, clonus, increased tone, and Babinski sign (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Hyperreflexia [HP:0001347]; Clonus [HP:0002169]; Spasticity [HP:0001257]; Extensor plantar response [HP:0003487] |
| Ataxia / cerebellar signs / coordination problems | Symptom/sign | Very common in pediatric pontine DMG; also seen in adults with brainstem involvement | Part of the classic DIPG triad; often manifests as gait instability or incoordination (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2, mandorino2024pediatricdiffusemidline pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Ataxia [HP:0001251]; Gait ataxia [HP:0002066]; Dysmetria [HP:0001310] |
| Limb weakness | Symptom/sign | Pediatric-onset disease, especially brainstem DMG; may occur in adults as well | Common presenting complaint reflecting corticospinal tract involvement (mandorino2024pediatricdiffusemidline pages 1-2) | Muscle weakness [HP:0001324]; Paresis [HP:0004305] |
| Speech difficulties / dysarthria | Symptom/sign | Common in children with brainstem DMG | Frequently accompanies cranial nerve and long-tract involvement (mandorino2024pediatricdiffusemidline pages 1-2) | Dysarthria [HP:0001260]; Speech disorder [HP:0002167] |
| Vision impairment / diplopia / oculomotor disturbance | Symptom/sign | Common in pediatric brainstem DMG; also expected in adult pontine disease with cranial nerve involvement | Often related to cranial neuropathy in pontine tumors (mandorino2024pediatricdiffusemidline pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Abnormality of vision [HP:0000504]; Diplopia [HP:0000651]; Gaze palsy [HP:0000605] |
| Nausea | Symptom | Can occur with thalamic or third-ventricular/midline tumors; reported in adult cases | Less specific than DIPG triad; may accompany raised intracranial pressure or hydrocephalus (broggi2024clinico–pathologicalfeaturesof pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Nausea [HP:0002018] |
| Fatigue | Symptom | Reported in adult thalamic/midline cases | Nonspecific but documented in adult presentation (nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Fatigue [HP:0012378] |
| Walking impairment / gait disturbance | Symptom/sign | Pediatric and adult disease, especially with ataxia or weakness | Reflects cerebellar signs and/or corticospinal dysfunction; common functional consequence (mandorino2024pediatricdiffusemidline pages 1-2) | Gait disturbance [HP:0001288]; Abnormality of gait [HP:0001288] |
| Childhood onset | Clinical course feature | Most commonly ages 5-10 years; DIPG often described in children 4-9 years old | Predominantly pediatric tumor overall (vallero2023pediatricdiffusemidline pages 2-3, mandorino2024pediatricdiffusemidline pages 1-2) | Childhood onset [HP:0011463] |
| Young adult/adult onset | Clinical course feature | Adults can be affected, often with thalamic predominance | Less common than pediatric disease; adult cases may show somewhat less aggressive clinical behavior than pediatric disease (broggi2024clinico–pathologicalfeaturesof pages 1-2, schulte2020clinicalradiologicand pages 1-2) | Adult onset [HP:0003581] |
| Rapidly progressive neurologic decline | Clinical course feature | Characteristic of both pediatric and adult DMG, especially untreated/progressive disease | Qualitatively severe and progressive; prognosis remains poor and disease is highly aggressive (broggi2024clinico–pathologicalfeaturesof pages 1-2, mandorino2024pediatricdiffusemidline pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 1-2) | Progressive neurologic deterioration [HP:0002344] |


*Table: This table summarizes the characteristic clinical presentation of diffuse midline glioma, H3 K27-altered, including the classic DIPG triad and other common symptoms, with suggested HPO mappings. It is useful for phenotype curation and disease knowledge base annotation.*

### 3.4 Quality-of-life impact
Neurologic deficits (ataxia, cranial nerve palsies, long-tract signs/weakness) directly impair gait, speech, vision, and daily function; radiotherapy is used palliatively to reduce symptoms but does not cure disease. (vallero2023pediatricdiffusemidline pages 2-3, mandorino2024pediatricdiffusemidline pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and defining alterations
WHO CNS5 recognizes DMG, H3 K27-altered as defined by **H3 K27M mutation**, or alternative molecular mechanisms including **EZHIP overexpression** or **EGFR alteration**, all producing loss of H3K27 methylation. (park2023the2021who pages 2-2, gue2024the2021world pages 15-16, park2023the2021who pages 6-7)

A review definition consistent with WHO CNS5 is quoted as: **“An infiltrative midline glioma with loss of H3 p.K28me3 (K27me3) and either … p.K28M (K27M) … aberrant overexpression of EZHIP, or an EGFR mutation (CNS WHO grade 4).”** (wisniewski2023h3k27maltereddiffuse pages 1-3)

### 4.2 Frequencies of major alterations (selected cohorts)
- Pediatric/combined cohorts: Dufour et al. report H3F3A K27M ~63.6% and HIST1H3B K27M ~15.9% among interpretable tumors; ~20.5% were histone wild-type in their cohort. (dufour2020identificationofprognostic pages 8-10)
- Kansai multicenter cohort (n=93 DMG): MGMT promoter methylation 9%, FGFR1 mutation 14%, EGFR mutation 3%, TERT promoter mutation 3%, BRAF V600E 1%, HIST1H3B K27M 2%. (hayashi2024neuroradiologicalgeneticand pages 1-2)

### 4.3 Prognostic molecular markers
- TP53 alteration/p53 overexpression is repeatedly associated with worse outcomes (damodharan2023molecularcharacterizationand pages 1-2, wang2021clinicalfeaturesand pages 3-4)
- PDGFRA amplification, 17p loss, and complex chromosomal profiles were associated with worse survival in a pediatric cohort. (dufour2020identificationofprognostic pages 8-10)
- MGMT promoter methylation is uncommon and was not associated with OS in an adult cohort analysis; this supports the concept that temozolomide benefit may be limited in many cases. (gong2023differencesinsurvival pages 7-9, hayashi2024neuroradiologicalgeneticand pages 1-2)

| Alteration (gene/marker) | Alteration type | Typical context (pediatric/adult; location) | Frequency/statistic with cohort details | Prognostic association (direction, OS/PFS) | Evidence type (cohort/systematic review/review) | Key citation (DOI URL and year) |
|---|---|---|---|---|---|---|
| H3 K27M in histone H3 genes (overall) | Somatic missense driver altering histone H3 lysine 27 biology | Predominantly pediatric DMG/DIPG in midline structures; also occurs in adults | ~85% of DIPG/DMG tumors harbor K27M mutations in H3.3/H3.1 genes in review synthesis (mandorino2024pediatricdiffusemidline pages 1-2) | Defining oncogenic event; associated with universally poor prognosis overall, but not itself a within-DMG stratifier in this summary (mandorino2024pediatricdiffusemidline pages 1-2) | Review | https://doi.org/10.3390/cancers16101814 (2024) (mandorino2024pediatricdiffusemidline pages 1-2) |
| H3F3A p.K27M (H3.3) | Somatic missense driver | Pediatric and adult DMG; pediatric pontine/thalamic/spinal, adult predominantly thalamic in one cohort | Dufour 2020: 28/44 interpretable cases (63.6%); Schulte 2020: adult cohort mutations exclusively in H3F3A among sequenced tumors; Damodharan 2023 identifies H3.3 as a prominent alteration across trial IPD (dufour2020identificationofprognostic pages 8-10, schulte2020clinicalradiologicand pages 1-2, damodharan2023molecularcharacterizationand pages 1-2) | Worse OS versus H3.1/HIST1H3B in pediatric disease; Damodharan 2023 found H3.3 associated with worse OS (dufour2020identificationofprognostic pages 8-10, damodharan2023molecularcharacterizationand pages 1-2) | Cohort + adult cohort + systematic review/IPD | https://doi.org/10.1111/bpa.12768 (2020); https://doi.org/10.1093/noajnl/vdaa142 (2020); https://doi.org/10.3390/cancers15133478 (2023) (dufour2020identificationofprognostic pages 8-10, schulte2020clinicalradiologicand pages 1-2, damodharan2023molecularcharacterizationand pages 1-2) |
| HIST1H3B p.K27M (H3.1) | Somatic missense driver | More typical in younger pediatric pontine tumors; uncommon in adults | Dufour 2020: 7 cases (15.9% of interpretable tumors); Hayashi 2024: 2% HIST1H3B p.K27M in multicenter cohort; absent in Schulte adult sequencing subset (dufour2020identificationofprognostic pages 8-10, hayashi2024neuroradiologicalgeneticand pages 1-2, schulte2020clinicalradiologicand pages 1-2) | Pediatric Dufour cohort: longer median OS than H3F3A-mutant tumors (12.1 vs 7.9 months), suggesting relatively better prognosis than H3.3-mutant disease (dufour2020identificationofprognostic pages 8-10) | Cohort + multicenter cohort + adult cohort | https://doi.org/10.1111/bpa.12768 (2020); https://doi.org/10.1186/s40478-024-01808-w (2024); https://doi.org/10.1093/noajnl/vdaa142 (2020) (dufour2020identificationofprognostic pages 8-10, hayashi2024neuroradiologicalgeneticand pages 1-2, schulte2020clinicalradiologicand pages 1-2) |
| TP53 alteration / p53 overexpression | Tumor suppressor mutation / IHC surrogate | Common in pediatric and adult DMG; not location-specific | Dufour 2020: TP53 mutations in 57.1% of H3K27-mutant tumors; Schulte 2020: TP53 frequently co-mutated in adults; Wang 2021 identified p53 overexpression as a negative factor (dufour2020identificationofprognostic pages 8-10, schulte2020clinicalradiologicand pages 1-2, wang2021clinicalfeaturesand pages 3-4) | Worse OS: Damodharan 2023 IPD review found TP53 associated with worse OS; Wang 2021 found p53 overexpression independently adverse for OS (damodharan2023molecularcharacterizationand pages 1-2, wang2021clinicalfeaturesand pages 3-4) | Cohort + adult cohort + systematic review/IPD | https://doi.org/10.1111/bpa.12768 (2020); https://doi.org/10.3390/cancers15133478 (2023); https://doi.org/10.3389/fonc.2020.602553 (2021) (dufour2020identificationofprognostic pages 8-10, damodharan2023molecularcharacterizationand pages 1-2, wang2021clinicalfeaturesand pages 3-4) |
| ACVR1 alteration | Activating kinase mutation | Mainly pediatric pontine/brainstem DMG | Dufour 2020: 11.8% in pediatric cohort; highlighted in reviews of pediatric disease (dufour2020identificationofprognostic pages 8-10, vallero2023pediatricdiffusemidline pages 2-3) | Favorable direction in Damodharan 2023 trial IPD review (“protective effect”) for OS relative to other genotypes (damodharan2023molecularcharacterizationand pages 1-2) | Cohort + systematic review/IPD | https://doi.org/10.1111/bpa.12768 (2020); https://doi.org/10.3390/cancers15133478 (2023) (dufour2020identificationofprognostic pages 8-10, damodharan2023molecularcharacterizationand pages 1-2) |
| PDGFRA amplification | Receptor tyrosine kinase amplification | Pediatric H3K27-mutant DMG; often brainstem-predominant cohorts | Dufour 2020: PDGFRA amplification in 20.6% (dufour2020identificationofprognostic pages 8-10) | Worse survival: significantly associated with shorter OS in Dufour 2020 (dufour2020identificationofprognostic pages 8-10) | Cohort | https://doi.org/10.1111/bpa.12768 (2020) (dufour2020identificationofprognostic pages 8-10) |
| FGFR1 mutation | Activating kinase mutation | More often thalamic/spinal and adult-enriched subsets; also seen in long-term survivor subgroup | Hayashi 2024: 14% FGFR1-mutant in 93-patient DMG cohort; Schulte 2020: FGFR1 frequently co-mutated in adults (hayashi2024neuroradiologicalgeneticand pages 1-2, schulte2020clinicalradiologicand pages 1-2) | Not established as uniformly favorable in all cohorts, but FGFR1/BRAF co-altered DMG has longer median OS >3 years in separate 2024 subtype study; long-term survivor data suggest MAPK pathway enrichment (hayashi2024neuroradiologicalgeneticand pages 1-2) | Multicenter cohort + adult cohort | https://doi.org/10.1186/s40478-024-01808-w (2024); https://doi.org/10.1093/noajnl/vdaa142 (2020) (hayashi2024neuroradiologicalgeneticand pages 1-2, schulte2020clinicalradiologicand pages 1-2) |
| BRAF p.V600E / BRAF co-alteration | Activating kinase mutation | Rare in standard DMG cohorts; enriched in distinct thalamic H3 K27/BRAF-FGFR1 co-altered subtype | Hayashi 2024: BRAF p.V600E in 1% of DMG cohort (hayashi2024neuroradiologicalgeneticand pages 1-2) | Rare alone in standard DMG; prognostic value not clear in Hayashi cohort, but MAPK-pathway co-altered long survivors reported elsewhere (hayashi2024neuroradiologicalgeneticand pages 1-2) | Multicenter cohort | https://doi.org/10.1186/s40478-024-01808-w (2024) (hayashi2024neuroradiologicalgeneticand pages 1-2) |
| EGFR mutation/alteration | Mutation/amplification defining subtype in some tumors | Midline DMG subset; more emphasized in WHO/review classification than common pediatric cohorts | Hayashi 2024: EGFR mutation 3%; WHO/review sources recognize EGFR-altered DMG subtype (hayashi2024neuroradiologicalgeneticand pages 1-2, gianno2022paediatrictypediffusehighgrade pages 1-2) | Prognostic effect not clearly defined in cited cohort excerpt (hayashi2024neuroradiologicalgeneticand pages 1-2) | Multicenter cohort + review/classification | https://doi.org/10.1186/s40478-024-01808-w (2024); https://doi.org/10.32074/1591-951x-830 (2022) (hayashi2024neuroradiologicalgeneticand pages 1-2, gianno2022paediatrictypediffusehighgrade pages 1-2) |
| MGMT promoter methylation | Epigenetic DNA methylation biomarker | Pediatric/adult DMG, often infrequent | Hayashi 2024: MGMT promoter methylation 9%; Gong 2023 noted MGMT methylation status was not associated with adult OS (hayashi2024neuroradiologicalgeneticand pages 1-2, gong2023differencesinsurvival pages 7-9) | No clear OS benefit signal in adult cohort; helps explain limited benefit of temozolomide in many DMGs (gong2023differencesinsurvival pages 7-9) | Multicenter cohort + cohort analysis | https://doi.org/10.1186/s40478-024-01808-w (2024); https://doi.org/10.1111/cns.14307 (2023) (hayashi2024neuroradiologicalgeneticand pages 1-2, gong2023differencesinsurvival pages 7-9) |
| TERT promoter mutation | Promoter hotspot mutation | Adult-enriched/older diffuse glioma biology; uncommon in DMG | Hayashi 2024: 3% TERT promoter mutation (hayashi2024neuroradiologicalgeneticand pages 1-2) | Prognostic significance not established in the cited excerpt (hayashi2024neuroradiologicalgeneticand pages 1-2) | Multicenter cohort | https://doi.org/10.1186/s40478-024-01808-w (2024) (hayashi2024neuroradiologicalgeneticand pages 1-2) |
| ATRX loss/mutation | Chromatin remodeling alteration | Seen in adult DMG and subsets of pediatric DMG | Schulte 2020: ATRX frequently co-mutated in adults; Broggi 2024 review notes ATRX loss in ~15% of adult cases (schulte2020clinicalradiologicand pages 1-2, broggi2024clinico–pathologicalfeaturesof pages 1-2) | Gong 2023: intact ATRX expression associated with longer survival in adults, implying ATRX loss may be unfavorable (gong2023differencesinsurvival pages 7-9) | Adult cohort + adult review + cohort analysis | https://doi.org/10.1093/noajnl/vdaa142 (2020); https://doi.org/10.3390/diagnostics14232617 (2024); https://doi.org/10.1111/cns.14307 (2023) (schulte2020clinicalradiologicand pages 1-2, broggi2024clinico–pathologicalfeaturesof pages 1-2, gong2023differencesinsurvival pages 7-9) |
| Complex chromosomal profile / 17p loss | Copy-number/chromosomal instability markers | Pediatric H3K27-mutant DMG | Dufour 2020: complex chromosomal profiles common (70.6%); 17p loss specifically identified among adverse markers (dufour2020identificationofprognostic pages 8-10) | Both complex chromosomal profile and 17p loss significantly associated with worse survival (dufour2020identificationofprognostic pages 8-10) | Cohort | https://doi.org/10.1111/bpa.12768 (2020) (dufour2020identificationofprognostic pages 8-10) |


*Table: This table summarizes major molecular alterations reported in diffuse midline glioma, H3 K27-altered, with representative frequencies and prognostic associations across key pediatric, adult, and multicenter cohorts. It is useful for comparing defining drivers, recurrent co-alterations, and biomarkers linked to survival.*

---

## 5. Environmental Information

No validated environmental, lifestyle, or infectious causal factors were identified in the retrieved evidence. The disease definition and therapeutic strategies in these sources center on tumor-intrinsic somatic alterations and local CNS anatomy. (mandorino2024pediatricdiffusemidline pages 1-2, gue2024the2021world pages 15-16)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core epigenetic mechanism
H3 K27 alterations (e.g., K27M) and EZHIP overexpression converge on **polycomb repressive complex 2 (PRC2)** interference, producing **global reduction of H3K27me2/H3K27me3** and widespread gene-expression dysregulation that supports aggressive glioma biology. (gue2024the2021world pages 15-16)

### 6.2 Causal chain (simplified)
1. Somatic H3K27-pathway alteration (H3 K27M, EZHIP overexpression, or EGFR-altered subtype) (park2023the2021who pages 2-2, gue2024the2021world pages 15-16)
2. Loss of H3K27me3 and altered chromatin states → abnormal transcriptional programs (gue2024the2021world pages 15-16)
3. Infiltrative glioma growth in critical midline structures (pons/thalamus/spinal cord) (vallero2023pediatricdiffusemidline pages 2-3, schulte2020clinicalradiologicand pages 1-2)
4. Neurologic deficits from local tract/nuclei involvement (cranial nerves, corticospinal tracts, cerebellar pathways) leading to the classic phenotype triad and progressive disability (vallero2023pediatricdiffusemidline pages 2-3, broggi2024clinico–pathologicalfeaturesof pages 1-2)

### 6.3 Pathways and processes (ontology suggestions)
- **GO Biological Process (suggested):** chromatin organization; histone H3-K27 methylation; negative regulation of gene expression (epigenetic); gliogenesis; regulation of cell proliferation.
- **GO Cellular Component (suggested):** Polycomb repressive complex 2 (PRC2); nucleosome; chromatin.
- **Cell types (CL, suggested):** astrocyte (astrocytic lineage tumor); oligodendrocyte precursor cell / glial progenitor-like states are commonly discussed in DMG biology (not quantitatively detailed in retrieved excerpts).

### 6.4 Advanced profiling (single-cell/spatial/multi-omics)
The retrieved evidence set emphasizes molecular profiling via biopsy/NGS and methylation profiling, but does not provide detailed single-cell or spatial transcriptomics results in the accessible excerpts. (nonnenbroich2024h3k27altereddiffusemidline pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue localization
Primary involvement is the **central nervous system**, particularly midline structures:
- Brainstem/pons (classic DIPG)
- Thalamus
- Spinal cord
(vallero2023pediatricdiffusemidline pages 2-3, schulte2020clinicalradiologicand pages 1-2, hayashi2024neuroradiologicalgeneticand pages 1-2)

### 7.2 Suggested UBERON mappings
- Pons (UBERON:0000988)
- Thalamus (UBERON:0001897)
- Spinal cord (UBERON:0002240)

---

## 8. Temporal Development

### 8.1 Onset and progression
Disease is typically **subacute to progressive** with rapid neurologic decline reflecting infiltrative growth in critical midline structures. Pediatric presentations are common; adult presentations occur and may have different site distribution and outcomes. (mandorino2024pediatricdiffusemidline pages 1-2, schulte2020clinicalradiologicand pages 1-2)

### 8.2 Staging
No formal staging system specific to DMG was identified in the retrieved evidence; clinically, course is commonly framed as diagnosis → post-radiotherapy period → progression/recurrence, with consideration of re-irradiation at recurrence. (vallero2023pediatricdiffusemidline pages 2-3, damodharan2023molecularcharacterizationand pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- Vallero et al. summarize pediatric burden as ~20% of pediatric CNS tumors with ~200–300 new cases/year in the United States (as reported in their review context). (vallero2023pediatricdiffusemidline pages 2-3)
- An adult-focused review cites incidence around **2.32 cases per 1 million persons/year** in adults (>20 years). (broggi2024clinico–pathologicalfeaturesof pages 1-2)

### 9.2 Inheritance
This is not typically a Mendelian inherited disorder; it is defined by tumor somatic alterations. No penetrance/carrier frequency/founder-effect data were identified in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Imaging
MRI is widely described as the diagnostic gold standard for pontine/brainstem cases; Vallero et al. note typical DIPG imaging criteria such as a lesion involving >50% of the pons. (vallero2023pediatricdiffusemidline pages 2-3)

### 10.2 Tissue diagnosis and molecular confirmation
- Biopsy in brainstem lesions has historically been debated, but multiple sources describe a trend toward stereotactic biopsy to enable immunohistochemistry and molecular profiling (NGS, methylation profiling). (vallero2023pediatricdiffusemidline pages 2-3, nonnenbroich2024h3k27altereddiffusemidline pages 1-2, damodharan2023molecularcharacterizationand pages 1-2)
- WHO-aligned pathologic workup commonly includes IHC for **H3 K27M** and assessment of **H3K27me3 loss**, with EZHIP evaluation where relevant; strong diffuse H3 K27M immunoreactivity with H3K27me3 loss supports diagnosis. (broggi2024clinico–pathologicalfeaturesof pages 1-2)

### 10.3 Differential diagnosis (high level)
Midline gliomas without H3 K27 alteration and other pediatric high-grade gliomas (e.g., hemispheric H3 G34-mutant tumors) are key considerations in the modern WHO framework. (park2023the2021who pages 2-2)

---

## 11. Outcome / Prognosis

### 11.1 Survival statistics (selected recent/large cohorts)
- **Kansai multicenter cohort (n=93, 24 hospitals):** median **PFS 9.9 months** and median **OS 16.6 months** (hayashi2024neuroradiologicalgeneticand pages 1-2). The Kaplan–Meier figure region containing these medians is shown in the extracted survival-curve images. (hayashi2024neuroradiologicalgeneticand media dec99d06, hayashi2024neuroradiologicalgeneticand media 8f7749a2, hayashi2024neuroradiologicalgeneticand media 14f6a8a7)
- **Adult cohort (n=60):** OS reported as **27.6 months** in Schulte et al. (schulte2020clinicalradiologicand pages 1-2, schulte2020clinicalradiologicand pages 7-8)
- **Mixed-age cohort (n=43):** median OS **12.83 months** with 12- and 24-month OS rates **53.8% and 40.2%**, respectively. (wang2021clinicalfeaturesand pages 3-4)
- Reviews emphasize poor pediatric prognosis with survival often around 12 months and very low long-term survival. (mandorino2024pediatricdiffusemidline pages 1-2)

### 11.2 Prognostic factors (clinical)
- Performance status (KPS) is repeatedly prognostic; KPS ≥80 (Kansai cohort) and KPS ≥70 (Wang cohort) are associated with improved OS. (hayashi2024neuroradiologicalgeneticand pages 1-2, wang2021clinicalfeaturesand pages 3-4)
- Adjuvant radiotherapy and chemoradiotherapy are associated with improved OS in retrospective analyses. (wang2021clinicalfeaturesand pages 3-4, gong2023differencesinsurvival pages 7-9)

---

## 12. Treatment

### 12.1 Standard of care / real-world implementation
**Radiotherapy remains the principal standard palliative treatment**, with typical fractionated dosing in the ~54–60 Gy range (Vallero) and 59 Gy cited in a pediatric review context. (vallero2023pediatricdiffusemidline pages 2-3, mandorino2024pediatricdiffusemidline pages 1-2)

Real-world practice patterns from the Kansai multicenter cohort (n=93) include:
- Resection (when feasible) in 36%
- Adjuvant radiation + chemotherapy in 83%
- Temozolomide use in 76%
- Bevacizumab use in 42%
(hayashi2024neuroradiologicalgeneticand pages 1-2)

Damodharan et al. (2023) systematic review of individual participant trial data highlights that **re-irradiation** was the only statistically significant modality associated with survival benefit in their pooled analysis. (damodharan2023molecularcharacterizationand pages 1-2)

### 12.2 Emerging therapies (2023–2024 prioritized)
- **Imipridones / ONC201-class agents:** Recent reviews summarize multiple clinical datasets with median OS values around ~16–22 months depending on cohort and timing, and emphasize earlier post-radiotherapy administration as potentially beneficial. (nonnenbroich2024h3k27altereddiffusemidline pages 4-6, yang2024newprogressin pages 3-5)
- **Epigenetic therapies (HDAC inhibition):** panobinostat continues to be studied, including approaches to improve delivery such as convection-enhanced delivery (CED). (rechberger2023benchtobedsideinvestigationsof pages 13-15, nonnenbroich2024h3k27altereddiffusemidline pages 9-10)
- **Cellular immunotherapy and vaccines:** Multiple active trials target H3K27M neoantigens (vaccine or engineered effector cells) and GD2 CAR-T approaches. (NCT04808245 chunk 1, NCT04196413 chunk 2, NCT07501156 chunk 1)

**MAXO (suggested) intervention terms** (high-level, for KB annotation): external beam radiotherapy; stereotactic biopsy; chemotherapy; immunotherapy; CAR T-cell therapy; peptide vaccination; re-irradiation; convection-enhanced delivery.

### 12.3 Key clinical trials (ClinicalTrials.gov)
| Modality/therapy | Target/mechanism | NCT ID | Phase | Population (age; mutation requirement; setting) | Delivery/route | Primary outcomes | Status and start date | URL |
|---|---|---|---|---|---|---|---|---|
| GD2 CAR T cells | GD2-directed CAR T-cell immunotherapy after lymphodepleting chemotherapy (fludarabine/cyclophosphamide) for DMG/DIPG; efficacy assessed with RANO 2.0, OS/PFS/PPS endpoints in protocol (yang2024newprogressin pages 3-5, NCT04196413 chunk 2) | NCT04196413 | Phase 1 | Age 2–60 years; H3K27M or H3K27I mutation required; DIPG and spinal DMG; recurrent/progressive setting allowed per eligibility framework (NCT04196413 chunk 2) | Cellular infusion after preparative regimen; CAR T-cell infusion (clinical route not fully specified in excerpt) (NCT04196413 chunk 2) | Safety/toxicity including suspected AEs/SAEs and toxicity resolution; radiographic response rate by RANO 2.0; OS; PFS; post-progression survival (NCT04196413 chunk 2) | Recruiting; start 2020-06 (yang2024newprogressin pages 3-5, NCT04196413 chunk 2) | https://clinicaltrials.gov/study/NCT04196413 |
| H3K27M peptide vaccine + atezolizumab | Long mutant H3K27M peptide vaccine to induce H3K27M-specific T cells, combined with involved-field radiotherapy and anti–PD-L1 checkpoint blockade (atezolizumab); imiquimod used as local adjuvant (NCT04808245 chunk 1) | NCT04808245 | Phase 1 | Adults with newly diagnosed H3.1K27M or H3.3K27M diffuse midline glioma; single-arm multicenter trial; planned n=15 (NCT04808245 chunk 1) | Vaccine administered subcutaneously; atezolizumab IV every 3 weeks; concurrent/serial with radiotherapy (NCT04808245 chunk 1) | Safety (regimen-limiting toxicity) and immunogenicity measured by H3K27M-specific T cells/IFN-γ ELISpot on PBMCs (NCT04808245 chunk 1) | Active, not recruiting; start 2023-02-15 (NCT04808245 chunk 1) | https://clinicaltrials.gov/study/NCT04808245 |
| Split-course hypofractionated radiation with stereotactic biopsy (SPORT-DMG) | Radiation-based management strategy integrating stereotactic biopsy and split-course/hypofractionated radiotherapy for DMG (yang2024newprogressin pages 3-5) | NCT05077735 | Phase 2 | DMG population; trial table identifies diffuse midline glioma with radiation intervention; detailed mutation/age criteria not available in excerpt (yang2024newprogressin pages 3-5) | Radiation: hypofractionated/split-course radiotherapy; stereotactic biopsy component (yang2024newprogressin pages 3-5) | Patient-reported/clinical outcomes include quality-of-life assessment and questionnaire administration; full primary endpoint wording not available in excerpt (yang2024newprogressin pages 3-5) | Recruiting; start 2021-10 (yang2024newprogressin pages 3-5) | https://clinicaltrials.gov/study/NCT05077735 |
| Panobinostat (PBTC-047) | HDAC inhibition (panobinostat/LBH589) targeting epigenetic dysregulation in DIPG/DMG (yang2024newprogressin pages 3-5) | NCT02717455 | Phase 1 | Children with diffuse intrinsic pontine glioma; mutation requirement not specified in excerpt; pediatric pontine DMG-relevant population (yang2024newprogressin pages 3-5) | Drug administration route not specified in excerpt (known panobinostat trial listed as drug intervention) (yang2024newprogressin pages 3-5) | Primary outcomes not specified in excerpt; trial identified as phase I panobinostat study (yang2024newprogressin pages 3-5) | Active, not recruiting; start 2016-06 (yang2024newprogressin pages 3-5) | https://clinicaltrials.gov/study/NCT02717455 |
| H3K27M-specific engineered immune effector cells (EIEs) | Autologous H3K27M-specific immune effectors generated from PBMCs stimulated with H3K27M antigen-primed autologous dendritic cells; product contains CD8+, CD4+, CD56+ populations (NCT07501156 chunk 1) | NCT07501156 | Phase 1/2 | Age 2–70 years; recurrent or refractory DMG/DIPG; confirmed H3K27M-positive disease; KPS ≥60; planned n=30 (NCT07501156 chunk 1) | 1–2 intravenous infusions once weekly at 1×10^5–1×10^7 EIEs/kg after leukapheresis-based manufacturing (NCT07501156 chunk 1) | Safety by CTCAE v4.0 adverse effects; success rate of EIE generation; ELISPOT evidence of target-specific T cells; objective response by RECIST v1.1 (NCT07501156 chunk 1) | Recruiting; start 2026-03-18 (NCT07501156 chunk 1) | https://clinicaltrials.gov/study/NCT07501156 |


*Table: This table summarizes key current and emerging ClinicalTrials.gov studies for diffuse midline glioma, H3 K27-altered, spanning CAR-T, peptide vaccination, radiation strategy, HDAC inhibition, and engineered immune effector cell approaches. It is useful for quickly comparing mechanism, eligibility, route, endpoints, and recruitment status across major active protocols.*

---

## 13. Prevention

No established primary prevention strategies are supported by the retrieved evidence, consistent with a disease primarily driven by sporadic somatic alterations and presenting as a rare CNS tumor. Secondary prevention (screening) is not established; diagnosis is typically symptom- and imaging-driven. (mandorino2024pediatricdiffusemidline pages 1-2, vallero2023pediatricdiffusemidline pages 2-3)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model Organisms

The retrieved evidence set references preclinical models (e.g., murine models used to test epigenetic combinations) but does not provide detailed, model-by-model phenotype recapitulation in the accessible excerpts. (nonnenbroich2024h3k27altereddiffusemidline pages 4-6)

---

## Expert opinions / analysis (authoritative sources)
- Contemporary expert reviews emphasize that despite extensive clinical trial activity, **radiotherapy remains the only proven standard**, and progress likely requires combination therapies, improved delivery across the BBB/BBTB, and molecularly guided strategies. (nonnenbroich2024h3k27altereddiffusemidline pages 1-2, nonnenbroich2024h3k27altereddiffusemidline pages 9-10)
- Drug-delivery concepts such as maximizing “drug–tumor residence time” and focusing on combinational regimens are emphasized as necessary to overcome resistance and clearance limitations. (rechberger2023benchtobedsideinvestigationsof pages 13-15)

---

## Notes on PMID availability
The provided full-text evidence chunks and trial registry records include DOI URLs and publication months/years but **did not include PMIDs** for most articles. Where PMID is required for downstream normalization, the DOI URLs provided here can be used to programmatically map to PubMed records.


References

1. (vallero2023pediatricdiffusemidline pages 2-3): Stefano Gabriele Vallero, Luca Bertero, Giovanni Morana, Paola Sciortino, Daniele Bertin, Anna Mussano, Federica Silvia Ricci, Paola Peretta, and Franca Fagioli. Pediatric diffuse midline glioma h3k27- altered: a complex clinical and biological landscape behind a neatly defined tumor type. Frontiers in Oncology, Jan 2023. URL: https://doi.org/10.3389/fonc.2022.1082062, doi:10.3389/fonc.2022.1082062. This article has 62 citations.

2. (gianno2022paediatrictypediffusehighgrade pages 1-2): Francesca Gianno, Isabella Giovannoni, Barbara Cafferata, Francesca Diomedi-Camassei, Simone Minasi, Sabina Barresi, Francesca Romana Buttarelli, Viola Alesi, Antonello Cardoni, Manila Antonelli, Chiara Puggioni, Giovanna Stefania Colafati, Andrea Carai, Maria Vinci, Angela Mastronuzzi, Evelina Miele, Rita Alaggio, Felice Giangaspero, and Sabrina Rossi. Paediatric-type diffuse high-grade gliomas in the 5th cns who classification. Pathologica, 114:422-435, Dec 2022. URL: https://doi.org/10.32074/1591-951x-830, doi:10.32074/1591-951x-830. This article has 66 citations.

3. (schulte2020clinicalradiologicand pages 1-2): Jessica D Schulte, Robin A Buerki, Sarah Lapointe, Annette M Molinaro, Yalan Zhang, Javier E Villanueva-Meyer, Arie Perry, Joanna J Phillips, Tarik Tihan, Andrew W Bollen, Melike Pekmezci, Nicholas Butowski, Nancy Ann Oberheim Bush, Jennie W Taylor, Susan M Chang, Philip Theodosopoulos, Manish K Aghi, Shawn L Hervey-Jumper, Mitchel S Berger, David A Solomon, and Jennifer L Clarke. Clinical, radiologic, and genetic characteristics of histone h3 k27m-mutant diffuse midline gliomas in adults. Neuro-oncology Advances, Oct 2020. URL: https://doi.org/10.1093/noajnl/vdaa142, doi:10.1093/noajnl/vdaa142. This article has 124 citations and is from a peer-reviewed journal.

4. (park2023the2021who pages 2-2): Yae Won Park, Philipp Vollmuth, Martha Foltyn‐Dumitru, Felix Sahm, Sung Soo Ahn, Jong Hee Chang, and Se Hoon Kim. The 2021 who classification for gliomas and implications on imaging diagnosis: part 2—summary of imaging findings on pediatric‐type diffuse high‐grade gliomas, pediatric‐type diffuse low‐grade gliomas, and circumscribed astrocytic gliomas. Journal of Magnetic Resonance Imaging, 58:690-708, Apr 2023. URL: https://doi.org/10.1002/jmri.28740, doi:10.1002/jmri.28740. This article has 48 citations and is from a domain leading peer-reviewed journal.

5. (park2023the2021who pages 6-7): Yae Won Park, Philipp Vollmuth, Martha Foltyn‐Dumitru, Felix Sahm, Sung Soo Ahn, Jong Hee Chang, and Se Hoon Kim. The 2021 who classification for gliomas and implications on imaging diagnosis: part 2—summary of imaging findings on pediatric‐type diffuse high‐grade gliomas, pediatric‐type diffuse low‐grade gliomas, and circumscribed astrocytic gliomas. Journal of Magnetic Resonance Imaging, 58:690-708, Apr 2023. URL: https://doi.org/10.1002/jmri.28740, doi:10.1002/jmri.28740. This article has 48 citations and is from a domain leading peer-reviewed journal.

6. (wisniewski2023h3k27maltereddiffuse pages 1-3): Karol Wiśniewski, Andrew Ghaly, Kate Drummond, and Andreas Fahlstrӧm. H3 k27m-altered diffuse midline gliomas: a review. Indian Journal of Neurosurgery, 12:104-115, Jul 2023. URL: https://doi.org/10.1055/s-0043-1771192, doi:10.1055/s-0043-1771192. This article has 9 citations.

7. (hayashi2024neuroradiologicalgeneticand pages 1-2): Nobuhide Hayashi, Junya Fukai, Hirokazu Nakatogawa, Hiroshi Kawaji, Ema Yoshioka, Yoshinori Kodama, Kosuke Nakajo, Takehiro Uda, Kentaro Naito, Noriyuki Kijima, Yoshiko Okita, Naoki Kagawa, Yoshinobu Takahashi, Naoya Hashimoto, Hideyuki Arita, Koji Takano, Daisuke Sakamoto, Tomoko Iida, Yoshiki Arakawa, Takeshi Kawauchi, Yukihiko Sonoda, Yuta Mitobe, Kenichi Ishibashi, Masahide Matsuda, Takamune Achiha, Takahiro Tomita, Masahiro Nonaka, Keijiro Hara, Noriyoshi Takebe, Takashi Tsuzuki, Yoshikazu Nakajima, Shiro Ohue, Nobuyuki Nakajima, Akira Watanabe, Akihiro Inoue, Masao Umegaki, Daisuke Kanematsu, Asako Katsuma, Miho Sumida, Tomoko Shofuda, Masayuki Mano, Manabu Kinoshita, Kanji Mori, Naoyuki Nakao, and Yonehiro Kanemura. Neuroradiological, genetic and clinical characteristics of histone h3 k27-mutant diffuse midline gliomas in the kansai molecular diagnosis network for cns tumors (kansai network): multicenter retrospective cohort. Acta Neuropathologica Communications, Jul 2024. URL: https://doi.org/10.1186/s40478-024-01808-w, doi:10.1186/s40478-024-01808-w. This article has 4 citations and is from a peer-reviewed journal.

8. (damodharan2023molecularcharacterizationand pages 1-2): Sudarshawn Damodharan, Alexandra Abbott, Kaitlyn Kellar, Qianqian Zhao, and Mahua Dey. Molecular characterization and treatment approaches for pediatric h3 k27-altered diffuse midline glioma: integrated systematic review of individual clinical trial participant data. Cancers, 15:3478, Jul 2023. URL: https://doi.org/10.3390/cancers15133478, doi:10.3390/cancers15133478. This article has 7 citations.

9. (NCT04808245 chunk 1):  A MultIceNTER Phase I Peptide VaCcine Trial for the Treatment of H3-Mutated Gliomas. German Cancer Research Center. 2023. ClinicalTrials.gov Identifier: NCT04808245

10. (NCT04196413 chunk 2):  GD2 CAR T Cells in Diffuse Intrinsic Pontine Gliomas (DIPG) & Spinal Diffuse Midline Glioma(DMG). Stanford University. 2020. ClinicalTrials.gov Identifier: NCT04196413

11. (gue2024the2021world pages 15-16): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

12. (broggi2024clinico–pathologicalfeaturesof pages 1-2): Giuseppe Broggi, Serena Salzano, Maria Failla, Giuseppe Maria Vincenzo Barbagallo, Francesco Certo, Magda Zanelli, Andrea Palicelli, Maurizio Zizzo, Nektarios Koufopoulos, Gaetano Magro, and Rosario Caltabiano. Clinico–pathological features of diffuse midline glioma, h3 k27-altered in adults: a comprehensive review of the literature with an additional single-institution case series. Diagnostics, 14:2617, Nov 2024. URL: https://doi.org/10.3390/diagnostics14232617, doi:10.3390/diagnostics14232617. This article has 7 citations.

13. (nonnenbroich2024h3k27altereddiffusemidline pages 1-2): Leo F. Nonnenbroich, Samantha M. Bouchal, Elena Millesi, Julian S. Rechberger, Soumen Khatua, and David J. Daniels. H3k27-altered diffuse midline glioma of the brainstem: from molecular mechanisms to targeted interventions. Cells, 13:1122, Jun 2024. URL: https://doi.org/10.3390/cells13131122, doi:10.3390/cells13131122. This article has 14 citations.

14. (park2023the2021who pages 7-7): Yae Won Park, Philipp Vollmuth, Martha Foltyn‐Dumitru, Felix Sahm, Sung Soo Ahn, Jong Hee Chang, and Se Hoon Kim. The 2021 who classification for gliomas and implications on imaging diagnosis: part 2—summary of imaging findings on pediatric‐type diffuse high‐grade gliomas, pediatric‐type diffuse low‐grade gliomas, and circumscribed astrocytic gliomas. Journal of Magnetic Resonance Imaging, 58:690-708, Apr 2023. URL: https://doi.org/10.1002/jmri.28740, doi:10.1002/jmri.28740. This article has 48 citations and is from a domain leading peer-reviewed journal.

15. (mandorino2024pediatricdiffusemidline pages 1-2): Manuela Mandorino, Ahana Maitra, Domenico Armenise, Olga Maria Baldelli, Morena Miciaccia, Savina Ferorelli, Maria Grazia Perrone, and Antonio Scilimati. Pediatric diffuse midline glioma h3k27-altered: from developmental origins to therapeutic challenges. Cancers, 16:1814, May 2024. URL: https://doi.org/10.3390/cancers16101814, doi:10.3390/cancers16101814. This article has 21 citations.

16. (dufour2020identificationofprognostic pages 8-10): Charlotte Dufour, Romain Perbet, Pierre Leblond, Romain Vasseur, Laurence Stechly, Adeline Pierache, Nicolas Reyns, Gustavo Touzet, Emilie Le Rhun, Matthieu Vinchon, Claude‐Alain Maurage, Fabienne Escande, and Florence Renaud. Identification of prognostic markers in diffuse midline gliomas h3k27m‐mutant. Brain Pathology, 30:179-190, Aug 2020. URL: https://doi.org/10.1111/bpa.12768, doi:10.1111/bpa.12768. This article has 40 citations and is from a domain leading peer-reviewed journal.

17. (wang2021clinicalfeaturesand pages 3-4): Yuan Wang, Lan-lan Feng, Pei-gang Ji, Jing-hui Liu, Shao-chun Guo, Yu-long Zhai, Eric W. Sankey, Yue Wang, Yan-rong Xue, Na Wang, Miao Lou, Meng Xu, Min Chao, Guo-Dong Gao, Yan Qu, Li Gong, and Liang Wang. Clinical features and molecular markers on diffuse midline gliomas with h3k27m mutations: a 43 cases retrospective cohort study. Frontiers in Oncology, Feb 2021. URL: https://doi.org/10.3389/fonc.2020.602553, doi:10.3389/fonc.2020.602553. This article has 48 citations.

18. (gong2023differencesinsurvival pages 7-9): Xuan Gong, S. Kuang, Dong-feng Deng, Jun Wu, Longbo Zhang, and Chaoyuan Liu. Differences in survival prognosticators between children and adults with h3k27m‐mutant diffuse midline glioma. CNS Neuroscience & Therapeutics, 29:3863-3875, Jun 2023. URL: https://doi.org/10.1111/cns.14307, doi:10.1111/cns.14307. This article has 17 citations and is from a peer-reviewed journal.

19. (hayashi2024neuroradiologicalgeneticand media dec99d06): Nobuhide Hayashi, Junya Fukai, Hirokazu Nakatogawa, Hiroshi Kawaji, Ema Yoshioka, Yoshinori Kodama, Kosuke Nakajo, Takehiro Uda, Kentaro Naito, Noriyuki Kijima, Yoshiko Okita, Naoki Kagawa, Yoshinobu Takahashi, Naoya Hashimoto, Hideyuki Arita, Koji Takano, Daisuke Sakamoto, Tomoko Iida, Yoshiki Arakawa, Takeshi Kawauchi, Yukihiko Sonoda, Yuta Mitobe, Kenichi Ishibashi, Masahide Matsuda, Takamune Achiha, Takahiro Tomita, Masahiro Nonaka, Keijiro Hara, Noriyoshi Takebe, Takashi Tsuzuki, Yoshikazu Nakajima, Shiro Ohue, Nobuyuki Nakajima, Akira Watanabe, Akihiro Inoue, Masao Umegaki, Daisuke Kanematsu, Asako Katsuma, Miho Sumida, Tomoko Shofuda, Masayuki Mano, Manabu Kinoshita, Kanji Mori, Naoyuki Nakao, and Yonehiro Kanemura. Neuroradiological, genetic and clinical characteristics of histone h3 k27-mutant diffuse midline gliomas in the kansai molecular diagnosis network for cns tumors (kansai network): multicenter retrospective cohort. Acta Neuropathologica Communications, Jul 2024. URL: https://doi.org/10.1186/s40478-024-01808-w, doi:10.1186/s40478-024-01808-w. This article has 4 citations and is from a peer-reviewed journal.

20. (hayashi2024neuroradiologicalgeneticand media 8f7749a2): Nobuhide Hayashi, Junya Fukai, Hirokazu Nakatogawa, Hiroshi Kawaji, Ema Yoshioka, Yoshinori Kodama, Kosuke Nakajo, Takehiro Uda, Kentaro Naito, Noriyuki Kijima, Yoshiko Okita, Naoki Kagawa, Yoshinobu Takahashi, Naoya Hashimoto, Hideyuki Arita, Koji Takano, Daisuke Sakamoto, Tomoko Iida, Yoshiki Arakawa, Takeshi Kawauchi, Yukihiko Sonoda, Yuta Mitobe, Kenichi Ishibashi, Masahide Matsuda, Takamune Achiha, Takahiro Tomita, Masahiro Nonaka, Keijiro Hara, Noriyoshi Takebe, Takashi Tsuzuki, Yoshikazu Nakajima, Shiro Ohue, Nobuyuki Nakajima, Akira Watanabe, Akihiro Inoue, Masao Umegaki, Daisuke Kanematsu, Asako Katsuma, Miho Sumida, Tomoko Shofuda, Masayuki Mano, Manabu Kinoshita, Kanji Mori, Naoyuki Nakao, and Yonehiro Kanemura. Neuroradiological, genetic and clinical characteristics of histone h3 k27-mutant diffuse midline gliomas in the kansai molecular diagnosis network for cns tumors (kansai network): multicenter retrospective cohort. Acta Neuropathologica Communications, Jul 2024. URL: https://doi.org/10.1186/s40478-024-01808-w, doi:10.1186/s40478-024-01808-w. This article has 4 citations and is from a peer-reviewed journal.

21. (hayashi2024neuroradiologicalgeneticand media 14f6a8a7): Nobuhide Hayashi, Junya Fukai, Hirokazu Nakatogawa, Hiroshi Kawaji, Ema Yoshioka, Yoshinori Kodama, Kosuke Nakajo, Takehiro Uda, Kentaro Naito, Noriyuki Kijima, Yoshiko Okita, Naoki Kagawa, Yoshinobu Takahashi, Naoya Hashimoto, Hideyuki Arita, Koji Takano, Daisuke Sakamoto, Tomoko Iida, Yoshiki Arakawa, Takeshi Kawauchi, Yukihiko Sonoda, Yuta Mitobe, Kenichi Ishibashi, Masahide Matsuda, Takamune Achiha, Takahiro Tomita, Masahiro Nonaka, Keijiro Hara, Noriyoshi Takebe, Takashi Tsuzuki, Yoshikazu Nakajima, Shiro Ohue, Nobuyuki Nakajima, Akira Watanabe, Akihiro Inoue, Masao Umegaki, Daisuke Kanematsu, Asako Katsuma, Miho Sumida, Tomoko Shofuda, Masayuki Mano, Manabu Kinoshita, Kanji Mori, Naoyuki Nakao, and Yonehiro Kanemura. Neuroradiological, genetic and clinical characteristics of histone h3 k27-mutant diffuse midline gliomas in the kansai molecular diagnosis network for cns tumors (kansai network): multicenter retrospective cohort. Acta Neuropathologica Communications, Jul 2024. URL: https://doi.org/10.1186/s40478-024-01808-w, doi:10.1186/s40478-024-01808-w. This article has 4 citations and is from a peer-reviewed journal.

22. (schulte2020clinicalradiologicand pages 7-8): Jessica D Schulte, Robin A Buerki, Sarah Lapointe, Annette M Molinaro, Yalan Zhang, Javier E Villanueva-Meyer, Arie Perry, Joanna J Phillips, Tarik Tihan, Andrew W Bollen, Melike Pekmezci, Nicholas Butowski, Nancy Ann Oberheim Bush, Jennie W Taylor, Susan M Chang, Philip Theodosopoulos, Manish K Aghi, Shawn L Hervey-Jumper, Mitchel S Berger, David A Solomon, and Jennifer L Clarke. Clinical, radiologic, and genetic characteristics of histone h3 k27m-mutant diffuse midline gliomas in adults. Neuro-oncology Advances, Oct 2020. URL: https://doi.org/10.1093/noajnl/vdaa142, doi:10.1093/noajnl/vdaa142. This article has 124 citations and is from a peer-reviewed journal.

23. (nonnenbroich2024h3k27altereddiffusemidline pages 4-6): Leo F. Nonnenbroich, Samantha M. Bouchal, Elena Millesi, Julian S. Rechberger, Soumen Khatua, and David J. Daniels. H3k27-altered diffuse midline glioma of the brainstem: from molecular mechanisms to targeted interventions. Cells, 13:1122, Jun 2024. URL: https://doi.org/10.3390/cells13131122, doi:10.3390/cells13131122. This article has 14 citations.

24. (yang2024newprogressin pages 3-5): Zhi Yang, Liang Sun, Haibin Chen, Caixing Sun, and Liang Xia. New progress in the treatment of diffuse midline glioma with h3k27m alteration. Heliyon, 10:e24877, Jan 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e24877, doi:10.1016/j.heliyon.2024.e24877. This article has 11 citations.

25. (rechberger2023benchtobedsideinvestigationsof pages 13-15): Julian S. Rechberger, Samantha M. Bouchal, Erica A. Power, Leo F. Nonnenbroich, Cody L. Nesvick, and David J. Daniels. Bench-to-bedside investigations of h3 k27-altered diffuse midline glioma: drug targets and potential pharmacotherapies. Expert Opinion on Therapeutic Targets, 27:1071-1086, Nov 2023. URL: https://doi.org/10.1080/14728222.2023.2277232, doi:10.1080/14728222.2023.2277232. This article has 5 citations and is from a peer-reviewed journal.

26. (nonnenbroich2024h3k27altereddiffusemidline pages 9-10): Leo F. Nonnenbroich, Samantha M. Bouchal, Elena Millesi, Julian S. Rechberger, Soumen Khatua, and David J. Daniels. H3k27-altered diffuse midline glioma of the brainstem: from molecular mechanisms to targeted interventions. Cells, 13:1122, Jun 2024. URL: https://doi.org/10.3390/cells13131122, doi:10.3390/cells13131122. This article has 14 citations.

27. (NCT07501156 chunk 1):  H3K27M-specific Immune Effector Cells Targeting DMG/DIPG. Shenzhen Geno-Immune Medical Institute. 2026. ClinicalTrials.gov Identifier: NCT07501156
