---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:53.678328'
end_time: '2026-04-24T17:20:27.727817'
duration_seconds: 1174.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Post-Traumatic Stress Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 65
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Post-Traumatic Stress Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Post-Traumatic Stress Disorder** covering all of the
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
- **Disease Name:** Post-Traumatic Stress Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Post-Traumatic Stress Disorder** covering all of the
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


## Post-Traumatic Stress Disorder (PTSD): Comprehensive Disease Characteristics Research Report (Psychiatric)

### Executive summary (current understanding; 2023–2024 emphasis)
Post-traumatic stress disorder (PTSD) is a trauma- and stressor-related psychiatric disorder characterized by persistent re-experiencing of a traumatic event, avoidance of reminders, and alterations in threat detection/arousal and mood/cognition that cause functional impairment. Contemporary research and guidelines emphasize (i) heterogeneity across diagnostic frameworks (DSM-5-TR vs ICD-11), (ii) strong evidence for trauma-focused psychotherapies as first-line treatment, (iii) robust epidemiologic burden in conflict and displacement settings, and (iv) emerging but not-yet-clinically-validated biological markers implicating HPA-axis dysregulation and neuroimmune activation. (bisson2024posttraumaticstressdisorder pages 1-2, schincariol2024posttraumaticstressdisorder pages 2-3, lang2024acliniciansguide pages 5-5, lawrence2024posttraumaticstress pages 5-5)

A compact, citation-rich snapshot suitable for knowledge-base ingestion is provided in the embedded table below.

| Category | Key points | Key citations |
|---|---|---|
| Identifiers/Definitions | **Disease:** Post-traumatic stress disorder (PTSD), a trauma- and stressor-related mental disorder that may develop after exposure to exceptionally threatening/horrifying events. **DSM-5-TR vs ICD-11:** DSM-5-TR requires qualifying trauma exposure and 4 symptom clusters—intrusion, avoidance, negative alterations in cognition/mood, and arousal/reactivity—with duration **>1 month** and functional impairment; ICD-11 defines 3 core clusters—re-experiencing, avoidance, and persistent sense of current threat—with symptoms lasting **several weeks** and impairment. ICD-11 additionally distinguishes **PTSD** and **complex PTSD (CPTSD)** as sibling diagnoses. Recent population work found DSM-5 and ICD-11 prevalence can be similar overall but identify only partially overlapping cases (κ=0.62). URLs: https://doi.org/10.1192/bja.2024.27 (Aug 2024); https://doi.org/10.1136/bmj.h6161 (Nov 2024); https://doi.org/10.1017/S2045796025100164 (Aug 2025). | Siddaway 2024, BJPsych Advances, doi:10.1192/bja.2024.27; Bisson et al. 2024, BMJ, doi:10.1136/bmj.h6161; Pettrich et al. 2025, Epidemiol Psychiatr Sci, doi:10.1017/S2045796025100164 (siddaway2024assessmentanddiagnosis pages 1-2, siddaway2024assessmentanddiagnosis pages 3-4, bisson2024posttraumaticstressdisorder pages 1-2, pettrich2025theprevalenceof pages 1-2) |
| Epidemiology | **General burden:** Umbrella review of 59 reviews found pooled PTSD prevalence **23.95%** (95% CI 20.74–27.15), with wide heterogeneity across trauma contexts; lifetime global prevalence cited around **5.6%**. **General adult estimates:** BMJ review reports point prevalence about **3%** and lifetime prevalence **1.9%–8.8%**. **Context-specific:** armed-conflict civilians **23.70%** (95% CI 19.50–28.40%); displaced people in Africa **55.64%** (95% CI 42.76–68.41%); internally displaced persons in Africa **51%** (95% CI 38–64); Ethiopian war-affected communities **48.4%** (95% CI 37.1–59.8%). **German general population:** trauma exposure 47.2%; probable PTSD **4.7%** by both DSM-5 and ICD-11 algorithms. URLs: https://doi.org/10.1017/S0033291724002319 (Sep 2024); https://doi.org/10.1136/gpsych-2023-101438 (Jun 2024); https://doi.org/10.3389/fpsyt.2024.1336665 (Mar 2024); https://doi.org/10.1371/journal.pone.0300894 (Apr 2024); https://doi.org/10.3389/fpsyt.2024.1399013 (May 2024). | Schincariol et al. 2024, Psychol Med, doi:10.1017/S0033291724002319; Ahmed et al. 2024, Gen Psychiatry, doi:10.1136/gpsych-2023-101438; Andualem et al. 2024, Front Psychiatry, doi:10.3389/fpsyt.2024.1336665; Tesfaye et al. 2024, PLoS One, doi:10.1371/journal.pone.0300894; Tinsae et al. 2024, Front Psychiatry, doi:10.3389/fpsyt.2024.1399013; Pettrich et al. 2025, doi:10.1017/S2045796025100164 (schincariol2024posttraumaticstressdisorder pages 1-2, ahmed2024prevalenceofposttraumatic pages 1-2, andualem2024prevalenceofposttraumatic pages 1-2, tesfaye2024posttraumaticstressdisorder pages 1-2, tinsae2024posttraumaticstressdisorder pages 1-2, pettrich2025theprevalenceof pages 1-2) |
| Risk factors | **Sex:** female sex repeatedly increases risk—OR **2.2** (95% CI 1.2–4.3) in Ethiopian war-affected communities; pooled OR **1.99** (95% CI 1.65–2.32) in African IDPs. **Trauma severity/cumulative trauma:** witnessing murder of a loved one OR **3.0**; close family member killed/seriously injured OR **3.1**; moderate/high perceived threat to life OR **3.4**. In IDPs, dose-response for traumatic events: **4–7 events OR 2.09**, **8–11 events OR 3.15**, **12–16 events OR 5.37**. **Social/contextual:** poor social support OR **4.4**; no longer married OR **1.93**; unemployment OR **1.92**; repeated displacement OR **2.13**; illness without medical care OR **1.92**. **Comorbidity:** depression OR **2.97** in IDPs; depression symptoms OR **2.8** and anxiety symptoms OR **3.4** in Ethiopian war-affected communities. Interpersonal trauma is noted to produce more severe/lasting PTSD than many non-intentional events. | Tinsae et al. 2024, Front Psychiatry, doi:10.3389/fpsyt.2024.1399013; Tesfaye et al. 2024, PLoS One, doi:10.1371/journal.pone.0300894; Schincariol et al. 2024, doi:10.1017/S0033291724002319 (tinsae2024posttraumaticstressdisorder pages 1-2, tinsae2024posttraumaticstressdisorder pages 10-11, tesfaye2024posttraumaticstressdisorder pages 15-16, tesfaye2024posttraumaticstressdisorder pages 1-2, schincariol2024posttraumaticstressdisorder pages 2-3) |
| Diagnostics | **Diagnostic approach:** validated clinician-administered interviews should be used to establish diagnosis; screening tools should **not** be used alone to diagnose PTSD. **Structured interviews:** CAPS-5, CAPS-CA-5, PSSI-5. **Self-report measures:** PCL-5, PDS-5. **ICD-11 PTSD/CPTSD tools:** International Trauma Questionnaire (ITQ), ITQ-CA; International Trauma Interview validation also cited. **Assessment caveats:** PCL-5-based prevalence depends strongly on cut-off; one general-population study found cut-off methods aligned more with DSM-5 than ICD-11. PCL-5 lacks depersonalization/derealization items, so DSM-5 dissociative subtype may be missed. Questionnaires are faster but more bias-prone; interviews are more comprehensive but time-consuming. URLs: https://doi.org/10.1002/jts.23013 (Jan 2024); https://doi.org/10.1192/bja.2024.27 (Aug 2024); https://doi.org/10.1002/cpp.3012 (May 2024). | Lang et al. 2024, J Trauma Stress, doi:10.1002/jts.23013; Siddaway 2024, doi:10.1192/bja.2024.27; Sarr et al. 2024, Clin Psychol Psychother, doi:10.1002/cpp.3012; Pettrich et al. 2025, doi:10.1017/S2045796025100164 (lang2024acliniciansguide pages 4-4, siddaway2024assessmentanddiagnosis pages 10-11, sarr2024asystematicreview pages 35-35, pettrich2025theprevalenceof pages 6-7, pettrich2025theprevalenceof pages 1-2) |
| Treatment | **2023 VA/DoD first-line (“strong for”):** trauma-focused psychotherapies **CPT, EMDR, PE**; first-line medications **paroxetine, sertraline, venlafaxine**. Trauma-focused psychotherapy is preferred first-line because meta-analyses show larger and more persistent improvement. **Other options:** Ehlers’ cognitive therapy, present-centered therapy, written exposure therapy (WET), and mindfulness-based stress reduction have weaker/supportive roles; prazosin is suggested **against** for overall PTSD but suggested **for nightmares**. **Strong against:** benzodiazepines and cannabis/cannabis derivatives. Guideline also suggests against invasive interventions such as ECT and vagus nerve stimulation for routine PTSD treatment because of limited efficacy evidence/harms. Some brief treatment formats in implementation/research: trauma-focused treatments often **8–16 sessions**; WET can be **5 sessions**. URLs: https://doi.org/10.1002/jts.23013 (Jan 2024); Figure summary from guideline article page 22. | Lang et al. 2024, J Trauma Stress, doi:10.1002/jts.23013; Koven 2024, Eur J Med Health Res, doi:10.59324/ejmhr.2024.2(5).01; BMJ review 2024, doi:10.1136/bmj.h6161 (lang2024acliniciansguide pages 5-5, koven2024ptsdtreatmentliterature pages 1-2, koven2024ptsdtreatmentliterature pages 2-3, lang2024acliniciansguide media 0f51705c, geter2024posttraumaticstress pages 41-47) |
| Mechanisms | **Core pathophysiology:** dysregulation of stress systems links limbic threat circuitry to endocrine and immune abnormalities. Canonical HPA cascade: amygdala/limbic input → hypothalamic **CRH** → pituitary **ACTH** → adrenal **cortisol**. Reviews report **low cortisol / hypocortisolism**, enhanced glucocorticoid receptor sensitivity, and stronger negative feedback in many PTSD cohorts. **Inflammation/immune:** elevated **IL-6, TNF-α, IL-1β**, chemokine changes, interferon-related gene expression, and reduced anti-inflammatory/regulatory cytokines. **Neuroimmune mechanisms:** microglia, astrocytes, mast cells, NLRP3-related signaling, COX-2/PGE2 pathways, endothelial-brain microvasculature signaling. **Affected circuits/regions:** amygdala, hippocampus, prefrontal cortex, PVN; consequences include impaired fear extinction, altered memory/emotion regulation, and possible neurodegenerative/somatic disease links. **Epigenetics/genetics:** FKBP5 and glucocorticoid signaling are repeatedly implicated; epigenetic reviews also highlight NR3C1, BDNF, and SLC6A4-related alterations. URLs: https://doi.org/10.1016/j.bbih.2024.100849 (Nov 2024); https://doi.org/10.1007/s11481-023-10064-z (Apr 2023); https://doi.org/10.1159/000541822 (Nov 2024). | Lawrence & Scofield 2024, Brain Behav Immun Health, doi:10.1016/j.bbih.2024.100849; Govindula et al. 2023, J Neuroimmune Pharmacol, doi:10.1007/s11481-023-10064-z; Golubeva et al. 2024, Complex Psychiatry, doi:10.1159/000541822 (lawrence2024posttraumaticstress pages 5-5, lawrence2024posttraumaticstress pages 1-2, lawrence2024posttraumaticstress pages 2-4, govindula2023emphasizingthecrosstalk pages 1-2) |
| Trials | **Representative active/recent trials from ClinicalTrials.gov:** **STEPPS** (NCT06947538; recruiting; Boston Medical Center; posted Apr 27 2025) tests a SMART stepped-care model using **webSTAIR**, coaching, **Brief STAIR**, and **WET**; nonresponse defined as **<15-point decrease on PCL-5**. **Intranasal insulin for PTSD** (NCT04044534; phase 2; recruiting; VA Connecticut; posted Aug 5 2019, updated Sep 16 2025) tests 40 IU twice daily with CAPS-5 outcome and amygdala hyperactivation rationale. **tcVNS in Veterans with PTSD** (NCT05517304; recruiting; VA ORD; posted Aug 26 2022, updated Mar 3 2026) evaluates PTSD symptoms, PET-measured insula activation, and **IL-6**. **Group WET** (NCT05729789; recruiting; St. Joseph’s Healthcare Hamilton; posted Feb 15 2023, updated Apr 17 2024) evaluates 6-session online group WET, hypothesizing low dropout (<10%) and symptom reduction. URLs: https://clinicaltrials.gov/study/NCT06947538 ; https://clinicaltrials.gov/study/NCT04044534 ; https://clinicaltrials.gov/study/NCT05517304 ; https://clinicaltrials.gov/study/NCT05729789 | ClinicalTrials.gov records: NCT06947538; NCT04044534; NCT05517304; NCT05729789 (NCT06947538 chunk 1, NCT04044534 chunk 1, NCT05517304 chunk 1, NCT05729789 chunk 1) |


*Table: This table compiles high-yield PTSD facts for a knowledge base entry, including diagnostic frameworks, epidemiology, risk factors, diagnostics, treatment recommendations, mechanisms, and active clinical trials. It is designed to provide a compact but citation-rich snapshot anchored to the gathered evidence.*

---

## 1. Disease information

### 1.1 Concise overview
PTSD is defined in authoritative clinical reviews as “a mental disorder that may develop after exposure to exceptionally threatening or horrifying events.” (BMJ, Nov 2024, DOI: https://doi.org/10.1136/bmj.h6161). (bisson2024posttraumaticstressdisorder pages 1-2)

### 1.2 Key identifiers (available from evidence)
- **MeSH (ClinicalTrials.gov browse term):** *Stress Disorders, Post-Traumatic* (MeSH ID: D013313), visible in ClinicalTrials.gov-derived trial metadata. (NCT04044534 chunk 1)
- **MONDO / ICD-10 / ICD-11 code strings:** Not retrieved in the currently available evidence; should be added from ICD-11 and MONDO resources directly.

### 1.3 Common synonyms / alternative names
- Post-traumatic stress disorder; Posttraumatic stress disorder; PTSD. (bisson2024posttraumaticstressdisorder pages 1-2, schincariol2024posttraumaticstressdisorder pages 2-3)

### 1.4 Provenance of information
This report integrates aggregated disease-level sources: clinical guidelines/summaries, umbrella/systematic reviews and meta-analyses, and clinical trial registry records; it does not derive from individual EHR case reports (though some evidence relates to EHR/biobank approaches in the broader retrieved corpus). (lang2024acliniciansguide pages 5-5, schincariol2024posttraumaticstressdisorder pages 1-2, NCT06947538 chunk 1)

---

## 2. Etiology

### 2.1 Primary causal factors
PTSD requires exposure to a traumatic stressor (Criterion A–type exposure in DSM-5-TR; “extremely threatening or horrific event(s)” in ICD-11). (bisson2024posttraumaticstressdisorder pages 1-2, siddaway2024assessmentanddiagnosis pages 3-4)

### 2.2 Risk factors (quantitative, recent)
**Conflict/displacement settings show particularly high pooled prevalence and strong associations with social/clinical risk factors.**
- **War-affected Ethiopian communities (meta-analysis; May 2024; Frontiers in Psychiatry):** pooled prevalence 48.4% (95% CI 37.1–59.8) with risk factors including female sex (OR 2.2), poor social support (OR 4.4), depression symptoms (OR 2.8), anxiety symptoms (OR 3.4), and threat/severity indicators (e.g., perceived threat to life OR 3.4). (https://doi.org/10.3389/fpsyt.2024.1399013). (tinsae2024posttraumaticstressdisorder pages 1-2)
- **Internally displaced persons (IDPs) in Africa (systematic review/meta-analysis; Apr 2024; PLOS ONE):** pooled PTSD prevalence 51% (95% CI 38–64) and dose–response with number of traumatic events (e.g., 12–16 events OR 5.37). Other pooled risk factors include female sex (OR 1.99), depression (OR 2.97), repeated displacement (OR 2.13), and illness without medical care (OR 1.92). (https://doi.org/10.1371/journal.pone.0300894). (tesfaye2024posttraumaticstressdisorder pages 1-2)
- **Displaced people in Africa (Mar 2024; Frontiers in Psychiatry):** pooled PTSD prevalence 55.64% (95% CI 42.76–68.41%); associated factors included female sex, unemployment, and depression. (https://doi.org/10.3389/fpsyt.2024.1336665). (andualem2024prevalenceofposttraumatic pages 1-2)

### 2.3 Protective factors
Direct quantitative protective-factor synthesis was limited in retrieved evidence. However, poor social support was strongly associated with PTSD in war-affected communities (OR 4.4), implying that **strong social support** is plausibly protective in those contexts. (tinsae2024posttraumaticstressdisorder pages 1-2)

### 2.4 Gene–environment interactions and polygenic risk (2023 evidence)
PTSD risk is partly genetically influenced and interacts with traumatic exposures.
- In a prospective cohort of mild traumatic brain injury (TRACK-TBI; Translational Psychiatry; Jan 2023; DOI: https://doi.org/10.1038/s41398-023-02313-9), probable PTSD at 6 months occurred in 16.3% (116/714; PCL-5 ≥33). A PTSD polygenic risk score (PRS) significantly predicted PTSD: top PRS quintile vs lowest aOR 3.71 (95% CI 1.80–7.65), and adding PRS improved discrimination (AUC 0.687→0.733). Authors interpret PRS as potentially actionable for enhanced follow-up/early intervention, pending prospective validation. (stein2023polygenicriskfor pages 3-5)

---

## 3. Phenotypes

### 3.1 Core symptom domains (DSM-5-TR vs ICD-11)
**DSM-5-TR** groups symptoms into four clusters: intrusion; avoidance; negative alterations in cognitions and mood; and alterations in arousal and reactivity, with persistence >1 month and functional impairment. (schincariol2024posttraumaticstressdisorder pages 2-3, bisson2024posttraumaticstressdisorder pages 1-2)

**ICD-11** defines PTSD with three core clusters: re-experiencing in the present; avoidance; and a persistent perception of heightened current threat, with symptoms lasting several weeks and causing distress/impairment; ICD-11 additionally recognizes complex PTSD (CPTSD) as a sibling diagnosis. (schincariol2024posttraumaticstressdisorder pages 2-3, siddaway2024assessmentanddiagnosis pages 3-4)

### 3.2 Suggested HPO mappings (examples)
(These are ontology suggestions; exact mapping should be verified against HPO.)
- Intrusive memories/flashbacks → *Recurrent intrusive memories*; *Flashback* (HPO suggestion).
- Nightmares → *Nightmares* (HPO suggestion).
- Avoidance → *Avoidant behavior* (HPO suggestion).
- Hypervigilance / exaggerated startle → *Hypervigilance*; *Increased startle response* (HPO suggestion).
- Sleep disturbance/insomnia (not core ICD-11 but common DSM-5-TR symptom content) → *Insomnia* (HPO suggestion). (schincariol2024posttraumaticstressdisorder pages 2-3, bisson2024posttraumaticstressdisorder pages 1-2)

### 3.3 Comorbidities and functional impacts
- PTSD and substance use disorders (SUDs) “co-occur at high rates,” with estimates “up to nearly 60%” comorbidity for alcohol and/or drug use disorder in PTSD populations (Journal of Traumatic Stress; Jun 2024; DOI: https://doi.org/10.1002/jts.23049). (back2024stateofthe pages 3-4)
- PTSD has clinically relevant associations with physical illness (e.g., cardiovascular/metabolic/autoimmune/neurocognitive risk) in HPA-axis focused reviews; these are mechanistically linked to stress physiology and immune alterations. (lawrence2024posttraumaticstress pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
No monogenic causal genes were supported in the retrieved evidence; PTSD is treated as a **polygenic** and multifactorial disorder with environmental necessity (trauma exposure). (barr2025multivariategenomewideassociation pages 1-4, stein2023polygenicriskfor pages 3-5)

### 4.2 Polygenic architecture (quantitative statements available)
A recent multivariate GWAS preprint summarizing background evidence reports twin-based heritability around 30–40% and SNP-based variance explained roughly 5–9% for PTSD (interpret cautiously as preprint/background). (barr2025multivariategenomewideassociation pages 1-4)

### 4.3 Epigenetic information (2024 review)
A 2024 epigenetics review emphasizes that environmental stressors can induce epigenetic changes relevant to PTSD, focusing on DNA methylation/chromatin regulation/noncoding RNA and highlighting gene systems related to HPA-axis regulation, neurotrophins, neurotransmission, and immune function. (Complex Psychiatry; Nov 2024; DOI: https://doi.org/10.1159/000541822). (hu2025thecentralrole pages 3-5)

### 4.4 Key limitation
The retrieved 2023–2024 corpus did not include a primary, large PTSD GWAS locus paper with a complete locus list; thus, locus-level curation is incomplete in this report.

---

## 5. Environmental information

### 5.1 Environmental factors and exposures
- Conflict/war exposure and displacement are associated with markedly elevated PTSD prevalence (e.g., 23.70% among civilians in conflict-affected regions; 51–55% among displaced/IDP populations in Africa). (ahmed2024prevalenceofposttraumatic pages 1-2, tesfaye2024posttraumaticstressdisorder pages 1-2)

### 5.2 Lifestyle factors
Specific lifestyle exposures (diet, exercise) were not directly quantified in retrieved evidence; substance use is addressed under comorbidity and treatment evidence. (back2024stateofthe pages 3-4)

### 5.3 Infectious agents
Not applicable as a primary cause in the evidence retrieved.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → biology → symptoms)
A consistent contemporary mechanistic model is:
1) **Trauma exposure** initiates stress responses and threat-learning processes (diagnostic prerequisite). (bisson2024posttraumaticstressdisorder pages 1-2)
2) **Stress-system dysregulation:** the limbic system (including amygdala) influences hypothalamic CRH release → pituitary ACTH → adrenal cortisol; PTSD is often associated with low cortisol and heightened glucocorticoid receptor sensitivity and enhanced negative feedback. (Brain, Behavior, & Immunity–Health; Nov 2024; DOI: https://doi.org/10.1016/j.bbih.2024.100849). (lawrence2024posttraumaticstress pages 5-5)
3) **Neuroimmune activation:** elevated pro-inflammatory cytokines (e.g., IL-6, TNF-α, IL-1β) and reduced regulatory cytokines occur alongside stress physiology; immune signaling can influence brain function through endothelial/microglial/astrocytic mechanisms. (lawrence2024posttraumaticstress pages 5-5, govindula2023emphasizingthecrosstalk pages 1-2)
4) **Circuit-level manifestations:** altered function in hippocampus/amygdala/prefrontal cortex contributes to dysregulated fear extinction, emotional processing, memory re-experiencing, hypervigilance, and impaired executive control. (lawrence2024posttraumaticstress pages 5-5)

### 6.2 Molecular pathways / suggested GO terms (examples)
(These are ontology suggestions; verify in GO for exact labels.)
- **HPA axis signaling / glucocorticoid response:** “response to glucocorticoid”; “regulation of hormone secretion”. (lawrence2024posttraumaticstress pages 5-5)
- **Inflammatory signaling:** “cytokine-mediated signaling pathway”; “inflammatory response”; “interferon signaling”. (lawrence2024posttraumaticstress pages 5-5, govindula2023emphasizingthecrosstalk pages 1-2)
- **COX-2/PGE2 axis:** “prostaglandin biosynthetic process”; “cyclooxygenase pathway” (suggested). (govindula2023emphasizingthecrosstalk pages 1-2)

### 6.3 Cell types / suggested CL terms (examples)
- Microglia (CL suggestion); Astrocytes (CL suggestion); Mast cells (CL suggestion) are explicitly implicated in neuroinflammatory mechanisms in PTSD-focused HPA/immune reviews. (lawrence2024posttraumaticstress pages 5-5)

---

## 7. Anatomical structures affected (UBERON suggestions)
Primary neuroanatomical structures repeatedly implicated include:
- **Amygdala** (UBERON suggestion) (lawrence2024posttraumaticstress pages 5-5)
- **Hippocampus** (UBERON suggestion) (lawrence2024posttraumaticstress pages 5-5)
- **Prefrontal cortex** (UBERON suggestion) (lawrence2024posttraumaticstress pages 5-5)
- **Hypothalamic paraventricular nucleus (PVN)** (UBERON suggestion) (govindula2023emphasizingthecrosstalk pages 1-2)

An example of ongoing mechanistically motivated neuromodulation research targets **insula activation** via imaging outcomes (see tcVNS trial). (NCT05517304 chunk 1)

---

## 8. Temporal development

### 8.1 Onset and duration thresholds
- DSM-5-TR: symptoms persist >1 month. (schincariol2024posttraumaticstressdisorder pages 2-3)
- ICD-11: symptoms persist “several weeks.” (schincariol2024posttraumaticstressdisorder pages 2-3)

### 8.2 Course, chronicity, and recurrence
A 2024 umbrella review reports that World Mental Health Surveys estimate 25–40% recover within 12 months (many within 6 months), while meta-analyses suggest nearly 50% may develop chronic PTSD if untreated. (schincariol2024posttraumaticstressdisorder pages 2-3)

A 2024 systematic review on PTSD recurrence concludes terminology/definitions are inconsistent and meta-analysis was not possible, indicating uncertainty around recurrence prevalence and predictors. (schincariol2024posttraumaticstressdisorder pages 2-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent quantitative estimates)
- **Umbrella review of PTSD prevalence (Psychological Medicine; Sep 2024; DOI: https://doi.org/10.1017/S0033291724002319):** pooled prevalence 23.95% (95% CI 20.74–27.15) across trauma-exposed contexts/reviews, with substantial heterogeneity. (schincariol2024posttraumaticstressdisorder pages 1-2)
- **Conflict-affected civilians (General Psychiatry; Jun 2024; DOI: https://doi.org/10.1136/gpsych-2023-101438):** pooled prevalence 23.70% (95% CI 19.50–28.40). (ahmed2024prevalenceofposttraumatic pages 1-2)
- **German general population survey (Epidemiology and Psychiatric Sciences; Aug 2025; DOI: https://doi.org/10.1017/S2045796025100164):** 47.2% reported ≥1 lifetime traumatic event; probable PTSD 4.7% under both DSM-5 and ICD-11 screening algorithms. (pettrich2025theprevalenceof pages 1-2)

### 9.2 Sex ratio
Pooled evidence in African displacement/war-affected meta-analyses shows higher risk for women (e.g., OR 1.99 in IDPs; OR 2.2 in Ethiopian war-affected communities). (tesfaye2024posttraumaticstressdisorder pages 1-2, tinsae2024posttraumaticstressdisorder pages 1-2)

### 9.3 Genetic architecture
Polygenic risk contributes to susceptibility (see PRS evidence), but no Mendelian inheritance pattern is supported. (stein2023polygenicriskfor pages 3-5)

---

## 10. Diagnostics

### 10.1 Clinical criteria (DSM-5-TR; ICD-11)
- DSM-5-TR requires qualifying exposure and 4 symptom clusters with >1 month duration and functional impairment. (schincariol2024posttraumaticstressdisorder pages 2-3, bisson2024posttraumaticstressdisorder pages 1-2)
- ICD-11 emphasizes 3 core symptom clusters and includes CPTSD as a related diagnosis. (schincariol2024posttraumaticstressdisorder pages 2-3)

### 10.2 Validated assessments (with implementation caveats)
- The 2023 VA/DoD clinician guide emphasizes that diagnosis should be established with validated clinician-administered interviews such as **CAPS-5** or the **PTSD Symptom Scale–Interview (PSS-I)** and that screening tools should not be used alone to establish a diagnosis (Journal of Traumatic Stress; Jan 2024; DOI: https://doi.org/10.1002/jts.23013). (lang2024acliniciansguide pages 4-4)
- Structured interviews and self-report instruments include CAPS-5/CAPS-CA-5/PSSI-5 and self-report measures such as PDS-5, with ICD-11-aligned measures including **ITQ** and ITQ-CA for PTSD/CPTSD. (siddaway2024assessmentanddiagnosis pages 10-11)
- Population screening work shows cut-off selection on PCL-5 markedly affects prevalence estimates and that DSM-5 vs ICD-11 algorithms can identify partially distinct cases despite similar overall prevalence. (pettrich2025theprevalenceof pages 4-5)

### 10.3 Biomarkers and imaging
No validated, scalable diagnostic biomarkers were established in the evidence. Reviews highlight cortisol-axis markers and inflammatory cytokines (e.g., IL-6, TNF-α) as biologically plausible but heterogeneous across studies and sensitive to sampling and comorbidity. (lawrence2024posttraumaticstress pages 2-4, lawrence2024posttraumaticstress pages 5-5)

---

## 11. Outcome / prognosis
Quantitative prognosis evidence in the retrieved corpus is limited; the umbrella review-derived course estimates suggest substantial early recovery for a subset (25–40% within 12 months) but substantial chronicity risk if untreated (~50%). (schincariol2024posttraumaticstressdisorder pages 2-3)

---

## 12. Treatment

### 12.1 First-line treatments (authoritative guideline synthesis; 2023 VA/DoD)
A clinician’s guide to the **2023 VA/DoD Clinical Practice Guideline** (Journal of Traumatic Stress; Jan 2024; DOI: https://doi.org/10.1002/jts.23013) emphasizes **trauma-focused psychotherapies as first-line** and recommends starting with one of three recommended trauma-focused treatments when feasible, using shared decision-making. (lang2024acliniciansguide pages 5-5)

From the guideline summary figure, “strong for” interventions include:
- **Psychotherapies:** Cognitive Processing Therapy (CPT), Eye Movement Desensitization and Reprocessing (EMDR), Prolonged Exposure (PE). (lang2024acliniciansguide media 0f51705c)
- **Medications:** paroxetine, sertraline, venlafaxine. (lang2024acliniciansguide media 0f51705c)

“Strong against” includes benzodiazepines and cannabis/cannabis derivatives. (lang2024acliniciansguide media 0f51705c, lang2024acliniciansguide pages 5-5)

### 12.2 Other psychotherapies and adjuncts
The guideline also suggests additional psychotherapies (e.g., Written Exposure Therapy; Present-Centered Therapy; Ehlers’ cognitive therapy) and mind–body approaches such as mindfulness-based stress reduction. (lang2024acliniciansguide pages 5-5)

### 12.3 Pharmacotherapy nuances
The guideline suggests against prazosin for overall PTSD treatment but suggests prazosin for PTSD-related nightmares. (lang2024acliniciansguide pages 5-5)

### 12.4 Comorbid PTSD and substance use disorders (SUD)
A 2024 state-of-the-science review reports that rigorously conducted trials support individual, manualized, trauma-focused treatments for PTSD/SUD, and that patients do not need to be abstinent to benefit. It highlights COPE (integrating Prolonged Exposure with CBT for SUD) as the most studied integrated treatment, with evidence for reductions in PTSD symptoms and substance use and improved remission outcomes, delivered in-person and via telehealth. (Journal of Traumatic Stress; Jun 2024; DOI: https://doi.org/10.1002/jts.23049). (back2024stateofthe pages 3-4)

### 12.5 Suggested MAXO terms (examples)
(Verify exact MAXO IDs in downstream curation.)
- Trauma-focused psychotherapy; prolonged exposure therapy; cognitive processing therapy; EMDR; SSRI administration; SNRI administration; prazosin administration for nightmares; shared decision-making in care planning. (lang2024acliniciansguide media 0f51705c, lang2024acliniciansguide pages 5-5)

---

## 13. Prevention

### 13.1 Evidence status
The VA/DoD clinician guide states that no pharmacological interventions had sufficient evidence to recommend for prevention of PTSD or acute stress disorder. (lang2024acliniciansguide pages 5-5)

### 13.2 Emerging early-intervention / stepped-care implementation research
A SMART stepped-care trial (STEPPS; NCT06947538; first posted Apr 27 2025; recruiting) aims to improve PTSD treatment access/engagement via a sequence of a digital intervention (webSTAIR), coaching, and brief clinician-administered treatments (Brief STAIR, WET), reflecting real-world implementation priorities in routine care. (ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06947538). (NCT06947538 chunk 1)

---

## 14. Other species / natural disease
PTSD is a human psychiatric diagnosis; however, mechanistic evidence relies heavily on preclinical stress models.

**Preclinical support for inflammation-linked mechanisms:** A 2024 review cites rodent evidence that PTSD-like symptoms were reduced after chronic inflammation treatment with ibuprofen, supporting a causal role for inflammation in symptom expression (preclinical). (lawrence2024posttraumaticstress pages 5-5)

---

## 15. Model organisms
Detailed model-organism cataloging was not retrieved; available evidence supports that animal stress paradigms are used to interrogate inflammatory mediators (e.g., COX-2/PGE2 signaling and cytokines) and HPA-axis dysregulation in PTSD-like phenotypes. (govindula2023emphasizingthecrosstalk pages 1-2)

---

## Recent developments and real-world applications (2023–2024 emphasis)

1) **Guideline evolution and implementation focus:** The 2023 VA/DoD guideline (described in 2024) centers trauma-focused psychotherapy first-line, shared decision-making, and cautions against benzodiazepines/cannabis; this directly influences real-world care systems (e.g., VA and civilian implementation projects) and informs stepped-care/digital delivery research. (lang2024acliniciansguide pages 5-5, lang2024acliniciansguide media 0f51705c, NCT06947538 chunk 1)

2) **High-burden humanitarian contexts:** 2024 meta-analyses quantify PTSD prevalence in armed conflict and displacement, supporting prioritization of scalable, culturally sensitive services in LMIC and conflict settings. (ahmed2024prevalenceofposttraumatic pages 1-2, tesfaye2024posttraumaticstressdisorder pages 1-2, andualem2024prevalenceofposttraumatic pages 1-2)

3) **Precision mental health directions:** 2023 evidence indicates polygenic risk scores can stratify risk for PTSD after a defined trauma exposure (mTBI), suggesting an emerging path toward targeted follow-up and early intervention trials. (stein2023polygenicriskfor pages 3-5)

---

## Limitations of this evidence synthesis (important for knowledge-base use)
- ICD-10/ICD-11 code strings and MONDO ID were not retrieved in the evidence state and should be added from the official classification/ontology sources.
- Locus-level details from the most recent large PTSD GWAS (2023–2024) were not available in retrieved full texts; genetic findings here therefore emphasize PRS and general heritability rather than comprehensive locus enumeration.
- Differential diagnosis content and some phenotype frequency estimates beyond prevalence (e.g., symptom-level frequencies) were limited in the retrieved evidence.

---

## Key URLs (selected)
- VA/DoD clinician guide summary (Jan 2024): https://doi.org/10.1002/jts.23013 (lang2024acliniciansguide pages 5-5)
- BMJ clinical review (Nov 2024): https://doi.org/10.1136/bmj.h6161 (bisson2024posttraumaticstressdisorder pages 1-2)
- PTSD prevalence umbrella review (Sep 2024): https://doi.org/10.1017/S0033291724002319 (schincariol2024posttraumaticstressdisorder pages 1-2)
- Conflict-affected civilians meta-analysis (Jun 2024): https://doi.org/10.1136/gpsych-2023-101438 (ahmed2024prevalenceofposttraumatic pages 1-2)
- IDPs in Africa meta-analysis (Apr 2024): https://doi.org/10.1371/journal.pone.0300894 (tesfaye2024posttraumaticstressdisorder pages 1-2)
- HPA-axis dysregulation review (Nov 2024): https://doi.org/10.1016/j.bbih.2024.100849 (lawrence2024posttraumaticstress pages 5-5)
- Stepped-care trial STEPPS: https://clinicaltrials.gov/study/NCT06947538 (NCT06947538 chunk 1)



References

1. (bisson2024posttraumaticstressdisorder pages 1-2): Jonathan I Bisson, Sarah Cosgrove, Catrin Lewis, and Neil P Roberts. Post-traumatic stress disorder. BMJ, pages h6161, Nov 2024. URL: https://doi.org/10.1136/bmj.h6161, doi:10.1136/bmj.h6161. This article has 170 citations and is from a domain leading peer-reviewed journal.

2. (schincariol2024posttraumaticstressdisorder pages 2-3): Alexa Schincariol, Graziella Orrù, Henry Otgaar, Giuseppe Sartori, and Cristina Scarpazza. Posttraumatic stress disorder (ptsd) prevalence: an umbrella review. Psychological Medicine, 54:4021-4034, Sep 2024. URL: https://doi.org/10.1017/s0033291724002319, doi:10.1017/s0033291724002319. This article has 58 citations and is from a highest quality peer-reviewed journal.

3. (lang2024acliniciansguide pages 5-5): Ariel J Lang, Jessica L. Hamblen, Paul E. Holtzheimer, Ursula Kelly, Sonya B. Norman, David Riggs, Paula P. Schnurr, and Ilse Wiechers. A clinician's guide to the 2023 va/dod clinical practice guideline for management of posttraumatic stress disorder and acute stress disorder. Journal of traumatic stress, 37:19-34, Jan 2024. URL: https://doi.org/10.1002/jts.23013, doi:10.1002/jts.23013. This article has 43 citations and is from a peer-reviewed journal.

4. (lawrence2024posttraumaticstress pages 5-5): Stephanie Lawrence and R. Hal Scofield. Post traumatic stress disorder associated hypothalamic-pituitary-adrenal axis dysregulation and physical illness. Brain, Behavior, &amp; Immunity - Health, 41:100849, Nov 2024. URL: https://doi.org/10.1016/j.bbih.2024.100849, doi:10.1016/j.bbih.2024.100849. This article has 73 citations.

5. (siddaway2024assessmentanddiagnosis pages 1-2): Andy P. Siddaway. Assessment and diagnosis of post-traumatic stress disorders (ptsds) for medico-legal and other clinical purposes: dsm-5-tr ptsd, icd-11 ptsd and icd-11 complex ptsd. BJPsych Advances, 30:383-397, Aug 2024. URL: https://doi.org/10.1192/bja.2024.27, doi:10.1192/bja.2024.27. This article has 15 citations and is from a peer-reviewed journal.

6. (siddaway2024assessmentanddiagnosis pages 3-4): Andy P. Siddaway. Assessment and diagnosis of post-traumatic stress disorders (ptsds) for medico-legal and other clinical purposes: dsm-5-tr ptsd, icd-11 ptsd and icd-11 complex ptsd. BJPsych Advances, 30:383-397, Aug 2024. URL: https://doi.org/10.1192/bja.2024.27, doi:10.1192/bja.2024.27. This article has 15 citations and is from a peer-reviewed journal.

7. (pettrich2025theprevalenceof pages 1-2): Amelie Pettrich, Yuriy Nesterko, and Heide Glaesmer. The prevalence of traumatic experiences and ptsd according to dsm-5 and icd-11 in the german general population. Epidemiology and Psychiatric Sciences, Aug 2025. URL: https://doi.org/10.1017/s2045796025100164, doi:10.1017/s2045796025100164. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (schincariol2024posttraumaticstressdisorder pages 1-2): Alexa Schincariol, Graziella Orrù, Henry Otgaar, Giuseppe Sartori, and Cristina Scarpazza. Posttraumatic stress disorder (ptsd) prevalence: an umbrella review. Psychological Medicine, 54:4021-4034, Sep 2024. URL: https://doi.org/10.1017/s0033291724002319, doi:10.1017/s0033291724002319. This article has 58 citations and is from a highest quality peer-reviewed journal.

9. (ahmed2024prevalenceofposttraumatic pages 1-2): Syed Hassan Ahmed, Aabia Zakai, Maha Zahid, Muhammad Youshay Jawad, Rui Fu, and Michael Chaiton. Prevalence of post-traumatic stress disorder and depressive symptoms among civilians residing in armed conflict-affected regions: a systematic review and meta-analysis. General Psychiatry, 37:e101438, Jun 2024. URL: https://doi.org/10.1136/gpsych-2023-101438, doi:10.1136/gpsych-2023-101438. This article has 69 citations and is from a peer-reviewed journal.

10. (andualem2024prevalenceofposttraumatic pages 1-2): Fantahun Andualem, Mamaru Melkam, Girmaw Medfu Takelle, Girum Nakie, Techilo Tinsae, Setegn Fentahun, Gidey Rtbey, Tesfaye Derbie Begashaw, Jemal Seid, Lidiya Fasil Tegegn, Getachew Muluye Gedef, Desalegn Anmut Bitew, and Tilahun Nega Godana. Prevalence of posttraumatic stress disorder and associated factors among displaced people in africa: a systematic review and meta-analysis. Frontiers in Psychiatry, Mar 2024. URL: https://doi.org/10.3389/fpsyt.2024.1336665, doi:10.3389/fpsyt.2024.1336665. This article has 13 citations.

11. (tesfaye2024posttraumaticstressdisorder pages 1-2): Amensisa Hailu Tesfaye, Ashenafi Kibret Sendekie, Gebisa Guyasa Kabito, Garedew Tadege Engdaw, Girum Shibeshi Argaw, Belay Desye, Abiy Ayele Angelo, Fantu Mamo Aragaw, and Giziew Abere. Post-traumatic stress disorder and associated factors among internally displaced persons in africa: a systematic review and meta-analysis. PLOS ONE, 19:e0300894, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0300894, doi:10.1371/journal.pone.0300894. This article has 32 citations and is from a peer-reviewed journal.

12. (tinsae2024posttraumaticstressdisorder pages 1-2): Techilo Tinsae, Shegaye Shumet, Gebresilassie Tadesse, Girmaw Medfu Takelle, Gidey Rtbey, Mamaru Melkam, Fantahun Andualem, Girum Nakie, Tesfaye Segon, Selam Koye, Setegn Fentahun, and Wondale Getinet Alemu. Post-traumatic stress disorder in the ethiopian population dwelling in war-affected communities: a systematic review and meta-analysis. Frontiers in Psychiatry, May 2024. URL: https://doi.org/10.3389/fpsyt.2024.1399013, doi:10.3389/fpsyt.2024.1399013. This article has 12 citations.

13. (tinsae2024posttraumaticstressdisorder pages 10-11): Techilo Tinsae, Shegaye Shumet, Gebresilassie Tadesse, Girmaw Medfu Takelle, Gidey Rtbey, Mamaru Melkam, Fantahun Andualem, Girum Nakie, Tesfaye Segon, Selam Koye, Setegn Fentahun, and Wondale Getinet Alemu. Post-traumatic stress disorder in the ethiopian population dwelling in war-affected communities: a systematic review and meta-analysis. Frontiers in Psychiatry, May 2024. URL: https://doi.org/10.3389/fpsyt.2024.1399013, doi:10.3389/fpsyt.2024.1399013. This article has 12 citations.

14. (tesfaye2024posttraumaticstressdisorder pages 15-16): Amensisa Hailu Tesfaye, Ashenafi Kibret Sendekie, Gebisa Guyasa Kabito, Garedew Tadege Engdaw, Girum Shibeshi Argaw, Belay Desye, Abiy Ayele Angelo, Fantu Mamo Aragaw, and Giziew Abere. Post-traumatic stress disorder and associated factors among internally displaced persons in africa: a systematic review and meta-analysis. PLOS ONE, 19:e0300894, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0300894, doi:10.1371/journal.pone.0300894. This article has 32 citations and is from a peer-reviewed journal.

15. (lang2024acliniciansguide pages 4-4): Ariel J Lang, Jessica L. Hamblen, Paul E. Holtzheimer, Ursula Kelly, Sonya B. Norman, David Riggs, Paula P. Schnurr, and Ilse Wiechers. A clinician's guide to the 2023 va/dod clinical practice guideline for management of posttraumatic stress disorder and acute stress disorder. Journal of traumatic stress, 37:19-34, Jan 2024. URL: https://doi.org/10.1002/jts.23013, doi:10.1002/jts.23013. This article has 43 citations and is from a peer-reviewed journal.

16. (siddaway2024assessmentanddiagnosis pages 10-11): Andy P. Siddaway. Assessment and diagnosis of post-traumatic stress disorders (ptsds) for medico-legal and other clinical purposes: dsm-5-tr ptsd, icd-11 ptsd and icd-11 complex ptsd. BJPsych Advances, 30:383-397, Aug 2024. URL: https://doi.org/10.1192/bja.2024.27, doi:10.1192/bja.2024.27. This article has 15 citations and is from a peer-reviewed journal.

17. (sarr2024asystematicreview pages 35-35): Rachel Sarr, Alice M. G. Quinton, Debbie Spain, and Freya Rumball. A systematic review of the assessment of icd-11 complex post-traumatic stress disorder (cptsd) in young people and adults. Clinical psychology & psychotherapy, 31 3:e3012, May 2024. URL: https://doi.org/10.1002/cpp.3012, doi:10.1002/cpp.3012. This article has 15 citations and is from a peer-reviewed journal.

18. (pettrich2025theprevalenceof pages 6-7): Amelie Pettrich, Yuriy Nesterko, and Heide Glaesmer. The prevalence of traumatic experiences and ptsd according to dsm-5 and icd-11 in the german general population. Epidemiology and Psychiatric Sciences, Aug 2025. URL: https://doi.org/10.1017/s2045796025100164, doi:10.1017/s2045796025100164. This article has 1 citations and is from a domain leading peer-reviewed journal.

19. (koven2024ptsdtreatmentliterature pages 1-2): Steven G. Koven. Ptsd treatment literature. European Journal of Medical and Health Research, 2:4-9, Sep 2024. URL: https://doi.org/10.59324/ejmhr.2024.2(5).01, doi:10.59324/ejmhr.2024.2(5).01. This article has 0 citations.

20. (koven2024ptsdtreatmentliterature pages 2-3): Steven G. Koven. Ptsd treatment literature. European Journal of Medical and Health Research, 2:4-9, Sep 2024. URL: https://doi.org/10.59324/ejmhr.2024.2(5).01, doi:10.59324/ejmhr.2024.2(5).01. This article has 0 citations.

21. (lang2024acliniciansguide media 0f51705c): Ariel J Lang, Jessica L. Hamblen, Paul E. Holtzheimer, Ursula Kelly, Sonya B. Norman, David Riggs, Paula P. Schnurr, and Ilse Wiechers. A clinician's guide to the 2023 va/dod clinical practice guideline for management of posttraumatic stress disorder and acute stress disorder. Journal of traumatic stress, 37:19-34, Jan 2024. URL: https://doi.org/10.1002/jts.23013, doi:10.1002/jts.23013. This article has 43 citations and is from a peer-reviewed journal.

22. (geter2024posttraumaticstress pages 41-47): LT Geter. Post traumatic stress disorder (ptsd) screening of military veterans in a civilian primary care setting. Unknown journal, 2024.

23. (lawrence2024posttraumaticstress pages 1-2): Stephanie Lawrence and R. Hal Scofield. Post traumatic stress disorder associated hypothalamic-pituitary-adrenal axis dysregulation and physical illness. Brain, Behavior, &amp; Immunity - Health, 41:100849, Nov 2024. URL: https://doi.org/10.1016/j.bbih.2024.100849, doi:10.1016/j.bbih.2024.100849. This article has 73 citations.

24. (lawrence2024posttraumaticstress pages 2-4): Stephanie Lawrence and R. Hal Scofield. Post traumatic stress disorder associated hypothalamic-pituitary-adrenal axis dysregulation and physical illness. Brain, Behavior, &amp; Immunity - Health, 41:100849, Nov 2024. URL: https://doi.org/10.1016/j.bbih.2024.100849, doi:10.1016/j.bbih.2024.100849. This article has 73 citations.

25. (govindula2023emphasizingthecrosstalk pages 1-2): Anusha Govindula, Niraja Ranadive, Madhavan Nampoothiri, C Mallikarjuna Rao, Devinder Arora, and Jayesh Mudgal. Emphasizing the crosstalk between inflammatory and neural signaling in post-traumatic stress disorder (ptsd). Journal of Neuroimmune Pharmacology, 18:248-266, Apr 2023. URL: https://doi.org/10.1007/s11481-023-10064-z, doi:10.1007/s11481-023-10064-z. This article has 31 citations and is from a peer-reviewed journal.

26. (NCT06947538 chunk 1):  Stepped Care for Posttraumatic Stress Disorder Study. Boston Medical Center. 2026. ClinicalTrials.gov Identifier: NCT06947538

27. (NCT04044534 chunk 1): Gihyun Yoon, MD. Intranasal Insulin for Posttraumatic Stress Disorder. VA Connecticut Healthcare System. 2024. ClinicalTrials.gov Identifier: NCT04044534

28. (NCT05517304 chunk 1):  Transcutaneous Vagal Nerve Stimulation in Veterans With Posttraumatic Stress Disorder. VA Office of Research and Development. 2022. ClinicalTrials.gov Identifier: NCT05517304

29. (NCT05729789 chunk 1): Jenna Boyd. Group Written Exposure Therapy for Posttraumatic Stress Disorder. St. Joseph's Healthcare Hamilton. 2023. ClinicalTrials.gov Identifier: NCT05729789

30. (stein2023polygenicriskfor pages 3-5): Murray B. Stein, Sonia Jain, Livia Parodi, Karmel W. Choi, Adam X. Maihofer, Lindsay D. Nelson, Pratik Mukherjee, Xiaoying Sun, Feng He, David O. Okonkwo, Joseph T. Giacino, Frederick K. Korley, Mary J. Vassar, Claudia S. Robertson, Michael A. McCrea, Nancy Temkin, Amy J. Markowitz, Ramon Diaz-Arrastia, Jonathan Rosand, Geoffrey T. Manley, Neeraj Badjatia, Ann-Christine Duhaime, Adam R. Ferguson, Shankar Gopinath, Ramesh Grandhi, Christopher Madden, Randall Merchant, David Schnyer, Sabrina R. Taylor, John K. Yue, and Ross Zafonte. Polygenic risk for mental disorders as predictors of posttraumatic stress disorder after mild traumatic brain injury. Translational Psychiatry, Jan 2023. URL: https://doi.org/10.1038/s41398-023-02313-9, doi:10.1038/s41398-023-02313-9. This article has 20 citations and is from a peer-reviewed journal.

31. (back2024stateofthe pages 3-4): Sudie E. Back, Amber M. Jarnecke, Sonya B. Norman, Angela J. Zaur, and Denise A. Hien. State of the science: treatment of comorbid posttraumatic stress disorder and substance use disorders. Journal of traumatic stress, 37:803-813, Jun 2024. URL: https://doi.org/10.1002/jts.23049, doi:10.1002/jts.23049. This article has 32 citations and is from a peer-reviewed journal.

32. (barr2025multivariategenomewideassociation pages 1-4): P. Barr, K. Bountress, C. Chatzinakos, J. E. Hart, Z. E. Neale, C. Sheerin, E. Johnson, E. G. Atkinson, C. Nievergelt, A. Maihofer, A. Powers, A. Agrawal, H. Edenberg, J. Gelernter, K. C. Koenen, B. Porjesz, PTSD workgroup of the Psychiatric Genomic Consorti, SUD workgroup of the Psychiatric Genomic Consortiu, A. Amstadter, and J. Meyers. Multivariate genome-wide association study (gwas) of ptsd, alcohol use and alcohol use disorders. MedRxiv, Mar 2025. URL: https://doi.org/10.1101/2025.03.24.25324454, doi:10.1101/2025.03.24.25324454. This article has 1 citations.

33. (hu2025thecentralrole pages 3-5): Xian-Zhang Hu and Lei Zhang. The central role of cytokines in ptsd and major depressive disorder: mechanisms and clinical implications. Immune Discovery, 1:10013-10013, Jan 2025. URL: https://doi.org/10.70322/immune.2025.10013, doi:10.70322/immune.2025.10013. This article has 0 citations.

34. (pettrich2025theprevalenceof pages 4-5): Amelie Pettrich, Yuriy Nesterko, and Heide Glaesmer. The prevalence of traumatic experiences and ptsd according to dsm-5 and icd-11 in the german general population. Epidemiology and Psychiatric Sciences, Aug 2025. URL: https://doi.org/10.1017/s2045796025100164, doi:10.1017/s2045796025100164. This article has 1 citations and is from a domain leading peer-reviewed journal.