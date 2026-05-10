---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T12:11:08.013636'
end_time: '2026-05-09T12:25:39.391184'
duration_seconds: 871.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis** covering all of the
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
- **Disease Name:** Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis** covering all of the
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


# Comprehensive Disease Characteristics Report: Mesial Temporal Lobe Epilepsy with Hippocampal Sclerosis (MTLE‑HS)

## Executive summary
Mesial temporal lobe epilepsy with hippocampal sclerosis (MTLE‑HS) is an International League Against Epilepsy (ILAE)–recognized epilepsy syndrome defined by focal seizures arising from mesial temporal (limbic) structures together with hippocampal sclerosis (HS), typically unilateral/asymmetric. HS is the most frequent histopathology in drug‑resistant temporal lobe epilepsy (TLE) and is strongly linked to favorable seizure outcomes after appropriately selected epilepsy surgery, while also being associated with substantial cognitive/psychiatric comorbidity and emerging molecular heterogeneity (immune activation; possible low‑level somatic mosaicism in rare cases). (ilae2020mesialtemporallobe pages 1-1, blumcke2013internationalconsensusclassification pages 1-2, blumcke2013internationalconsensusclassification pages 2-4)

| Topic | Key finding/statistics | Population/model | Publication (authors, journal) | Year/month | PMID | URL | Evidence context id |
|---|---|---|---|---|---|---|---|
| ILAE histopathologic HS classification | HS is the most common histopathology in drug-resistant TLE; in large surgical series HS identified in 33.6% of cases, with 5.1% dual pathology. ILAE Type 1 = severe CA1+CA4 neuronal loss/gliosis; Type 2 = CA1-predominant; Type 3 = CA4-predominant; Type 1 is most common (~60-80%) and linked to earlier precipitating injury and better postsurgical seizure control. Surgical seizure freedom after resection for drug-resistant TLE is ~60-80% at 2 years. | Human surgical pathology / clinicopathologic consensus | Blümcke et al., *Epilepsia* | 2013/Jul | not in text | https://doi.org/10.1111/epi.12220 | (blumcke2013internationalconsensusclassification pages 1-2, blumcke2013internationalconsensusclassification pages 2-4) |
| MTLE-HS syndrome definition | MTLE-HS described as a rare epilepsy syndrome with seizures arising from mesial temporal limbic structures (hippocampus, amygdala, parahippocampal gyrus) together with hippocampal sclerosis, commonly unilateral or asymmetric. Often associated with early-life precipitating events in first 5 years, latent seizure-free interval, typical auras/automatisms, later drug-refractoriness, and progressive memory/behavioral deficits. | Human expert consensus / syndrome definition | ILAE Commission on Neurosurgery of Epilepsy, *Definitions* | 2020/Feb | not in text | https://doi.org/10.32388/zvebpt | (ilae2020mesialtemporallobe pages 1-1) |
| MRI/radiologic HS classification aligned to ILAE subtypes | Conventional MRI signs: whole-hippocampal atrophy, increased T2 signal, loss of internal architecture. Proposed radiologic classification: Type 1 = severe subfield volume loss across all subfields or severe CA1+hilum loss; Type 2 = isolated/disproportionate CA1 loss; Type 3 = isolated/disproportionate hilar (CA4/dentate) loss; No HS = no subfield volume loss. Type 1 represents ~60-80% of surgical TLE, Type 2 ~5-10%, Type 3 ~4-7%. High-resolution coronal T2 TSE orthogonal to hippocampal axis is emphasized; T2-FLAIR not recommended as primary screening tool. | Human radiology-pathology review | Middlebrooks et al., *American Journal of Neuroradiology* | 2024/Feb | not in text | https://doi.org/10.3174/ajnr.a8214 | (middlebrooks2024radiologicclassificationof pages 1-3, middlebrooks2024radiologicclassificationof pages 5-7, middlebrooks2024radiologicclassificationof pages 7-9, middlebrooks2024radiologicclassificationof pages 9-10) |
| Febrile status epilepticus leading to HS/MTLE (FEBSTAT) | In a prospective cohort of 222 children after febrile status epilepticus, acute hippocampal T2 hyperintensity strongly predicted later HS and increased MTLE risk. Of 22 with acute T2 hyperintensity, 14 had follow-up and 10 developed definite HS persisting through 10 years. Overall, 44 developed epilepsy; 6 developed MTLE, of whom 2 had definite HS, 2 equivocal HS, and 2 no HS. Earlier FEBSTAT reporting noted ~10% incidence of hippocampal T2 hyperintensity after FSE progressing to radiologic HS at 1 year. | Human prospective pediatric cohort | Lewis et al., *Epilepsia* | 2024/Apr | not in text | https://doi.org/10.1111/epi.17979 | (lewis2024hippocampalsclerosisand pages 1-3, lewis2024hippocampalsclerosisand pages 3-5) |
| Immune pathways in TLE-HS | RNA-seq comparison of TLE-HS vs TLE-nonHS identified altered immune pathways and differential immune-related genes including **HSP90AA1** and **SOD1**; proposed SOX2-OT/miR-671-5p/SPP1 axis as a potential therapeutic target. Notes HS as primary pathology in 36.4% of surgical TLE cases; cites glial activation and inflammatory cytokine production in TLE-HS. | Human hippocampal transcriptomics (3 TLE-HS vs 3 TLE-nonHS) | Che et al., *Scientific Reports* | 2024/Jun | not in text | https://doi.org/10.1038/s41598-024-63541-7 | (che2024alteredimmunepathways pages 1-2) |
| Single-cell and spatial transcriptomics mechanisms | KA-induced mouse TLE model showed inflammatory/stress pathway activation and suppression of axonal-development/neural-support pathways in hippocampus. Profiled 31,390 glial cells and 48,221 neuronal nuclei; Xenium panel mapped 247 genes. Key glial upregulated genes: **Spp1, Trem2, Cd68**; neuronal upregulated genes: **Penk, Sorcs3, Plekha2**. Supports activated glia as drivers of post-epileptogenic hippocampal remodeling. | Mouse kainic-acid TLE model; scRNA-seq/snRNA-seq/spatial transcriptomics | Liu et al., *Biomarker Research* | 2024/Sep | not in text | https://doi.org/10.1186/s40364-024-00636-3 | (liu2024singlecellsinglenucleusand pages 1-2) |
| Genetic susceptibility linking febrile seizures and MTLE-HS | GWAS/meta-analysis found genome-wide significant association for MTLE-HS with febrile seizures at the sodium channel gene cluster on 2q24.3: **rs7587026** in **SCN1A**, **P = 3.36 × 10^-9**, **OR 1.42** (95% CI 1.26-1.59). No association in a cohort with febrile seizures that did not later develop epilepsy, supporting syndrome-specific susceptibility. | Human GWAS/meta-analysis; 1018 cases + 7552 controls, replication 959 cases + 3591 controls | Kasperavičiūtė et al., *Brain* | 2013/Sep | not in text | https://doi.org/10.1093/brain/awt233 | (deleu2026theinteractingetiologies pages 6-7) |
| LITT real-world implementation (LAANTERN registry) | Prospective multicenter registry of 145 MTLE patients from 15 US level-IV centers: mean age 39.2 years; 50.3% female; median hospital stay 1 day; 96.6% discharged home. At 2 years, **58.4% (45/77) Engel I** and **57.2% (44/77) ILAE 1/2**. Adverse events in **16.5%**, mostly mild/transient. One-third reduced or stopped ASMs; QOL improved at nearly all time points. | Human prospective multicenter registry | Landazuri et al., *JAMA Neurology* | 2025/Jul | not in text | https://doi.org/10.1001/jamaneurol.2025.1897 | (landazuri2025interstitialthermaltherapy pages 1-2) |
| Somatic/lesional molecular finding in MTLE-HS | Case report of 31-year-old man with MTLE and ILAE Type 1 HS containing rare **BRAFV600E**-immunopositive neurons (<1% of total cells) in Cornu Ammonis; sparse CD34+ cells; patient seizure-free for 2 years after surgery. Authors discuss possible somatic mosaicism/diagnostic challenge and suggest routine BRAFV600E testing in MTLE-HS research settings. | Human single case report / neuropathology | Alsalek et al., *Free Neuropathology* | 2024/Jan | not in text | https://doi.org/10.17879/freeneuropathology-2024-5269 | (alsalek2024mesialtemporallobe pages 1-3) |


*Table: This table summarizes major authoritative and recent sources relevant to mesial temporal lobe epilepsy with hippocampal sclerosis, including consensus definitions, imaging/pathology classifications, mechanistic studies, and treatment outcomes. It highlights the main statistics and context IDs needed to support a disease knowledge base entry.*

---

## 1. Disease information
### 1.1 What is the disease?
The ILAE Commission on Neurosurgery of Epilepsy describes MTLE‑HS as an epilepsy syndrome characterized by seizures arising from limbic structures of the mesial temporal lobe (hippocampus, amygdala, parahippocampal gyrus) together with hippocampal sclerosis, commonly unilateral or asymmetric; a frequent historical pattern includes an early-life precipitating event, a latent seizure‑free period, typical autonomic/experiential auras and automatisms, later drug refractoriness, and progressive memory/behavioral deficits. (ilae2020mesialtemporallobe pages 1-1)

### 1.2 Common synonyms and alternative names
* **MTLE‑HS** (mesial temporal lobe epilepsy with hippocampal sclerosis). (ilae2020mesialtemporallobe pages 1-1)
* **TLE‑HS** (temporal lobe epilepsy with hippocampal sclerosis), often used when mesial localization is implied. (che2024alteredimmunepathways pages 1-2)
* **Mesial temporal sclerosis (MTS)**: in the ILAE HS consensus, “MTS” is described as HS plus involvement of other mesial temporal structures (e.g., amygdala, entorhinal cortex). (blumcke2013internationalconsensusclassification pages 12-13)
* **Ammon’s horn sclerosis** is referenced as a historical label for HS pathology in MTLE‑HS literature. (deleu2026theinteractingetiologies pages 1-2)

### 1.3 Key identifiers (OMIM, Orphanet, ICD‑10/ICD‑11, MeSH, MONDO)
The retrieved evidence set contains authoritative syndrome definitions and classification systems but does **not** include an explicit mapping to OMIM/Orphanet/ICD/MeSH/MONDO identifiers. Therefore, these identifiers cannot be reliably provided from the present corpus without adding dedicated ontology sources. (ilae2020mesialtemporallobe pages 1-1, blumcke2013internationalconsensusclassification pages 1-2)

### 1.4 Evidence source type
Most disease-level definition/classification statements in this report come from **ILAE consensus documents** and radiology/pathology consensus reviews, while mechanistic statements come from a mix of **human surgical tissue transcriptomics** and **animal-model single-cell/spatial transcriptomics**. (ilae2020mesialtemporallobe pages 1-1, che2024alteredimmunepathways pages 1-2, liu2024singlecellsinglenucleusand pages 1-2)

---

## 2. Etiology
### 2.1 Primary causes / causal factors (current understanding)
MTLE‑HS is best supported as a **multifactorial syndrome** in which heterogeneous early insults and host susceptibility converge on hippocampal injury, network reorganization, and chronic seizure propensity. The ILAE HS pathology consensus highlights associations of HS severity with time-related factors and early insults, particularly prolonged febrile seizures. (blumcke2013internationalconsensusclassification pages 2-4, blumcke2013internationalconsensusclassification pages 1-2)

### 2.2 Risk factors
#### (A) Febrile seizures / febrile status epilepticus (FSE): 2024 update
The FEBSTAT study provides high-quality prospective evidence linking FSE to later HS/MTLE via imaging biomarkers: acute hippocampal **T2 hyperintensity** shortly after FSE predicted later HS and increased MTLE risk. Among 22 with acute hippocampal T2 hyperintensity, 14 had follow-up and **10 developed definite HS** persisting through 10-year follow-up; overall **44** developed epilepsy and **6** developed MTLE (with mixed HS status among those six). (Epilepsia; Apr 2024; https://doi.org/10.1111/epi.17979) (lewis2024hippocampalsclerosisand pages 1-3)

#### (B) Genetic susceptibility (common variation)
A key human GWAS result referenced in the evidence indicates common variation around **SCN1A** can increase susceptibility to MTLE‑HS in the setting of febrile seizures (reported odds ratio ~1.42). (deleu2026theinteractingetiologies pages 6-7)

#### (C) Somatic mosaicism / lesional genetics (emerging; 2024)
A 2024 neuropathology case report describes a patient with MTLE and ILAE type 1 HS with a rare population of **BRAFV600E‑immunopositive neurons** (<1% of cells) and seizure freedom at 2 years post-surgery, emphasizing diagnostic complexity and raising the possibility of low-level somatic mosaicism in some MTLE‑HS cases. (Free Neuropathology; Jan 2024; https://doi.org/10.17879/freeneuropathology-2024-5269) (alsalek2024mesialtemporallobe pages 1-3)

#### (D) Immune/inflammatory processes (human molecular evidence; 2024)
Human hippocampal RNA-seq in a small cohort (3 TLE‑HS vs 3 TLE‑nonHS) reported altered immune-pathway signatures and identified immune-related genes (e.g., **HSP90AA1**, **SOD1**) and a proposed ceRNA axis (**SOX2‑OT/miR‑671‑5p/SPP1**) as potential therapeutic targets, supporting immune involvement in TLE‑HS. (Scientific Reports; Jun 2024; https://doi.org/10.1038/s41598-024-63541-7) (che2024alteredimmunepathways pages 1-2)

### 2.3 Protective factors
No protective genetic variants or environmental protective exposures were explicitly identified in the retrieved evidence corpus.

### 2.4 Gene–environment interaction (G×E)
The convergent picture supported by the retrieved evidence is that early-life insults (e.g., FSE with acute hippocampal injury) can interact with host susceptibility (e.g., common SCN1A-region variation; rare somatic variants in selected reports) to influence whether HS develops and how MTLE manifests. (lewis2024hippocampalsclerosisand pages 1-3, deleu2026theinteractingetiologies pages 6-7, alsalek2024mesialtemporallobe pages 1-3)

---

## 3. Phenotypes
### 3.1 Core seizure semiology and associated clinical features
The ILAE syndrome definition describes typical MTLE‑HS seizures as limbic-onset seizures with features such as rising epigastric aura; emotional disturbances and illusions; autonomic signs (e.g., palpitations); progressive impairment of awareness; oroalimentary automatisms (lip smacking/chewing/licking); behavioral arrest; head deviation; dystonic postures; and manual/verbal automatisms, followed by postictal dysfunction. (ilae2020mesialtemporallobe pages 1-1)

### 3.2 Course and comorbidities
The ILAE definition notes a common course with early medication responsiveness followed by later drug refractoriness and progressive memory/behavioral deficits. (ilae2020mesialtemporallobe pages 1-1)

### 3.3 Imaging-associated phenotypes
In outpatient TLE series, MRI evidence of hippocampal atrophy was reported in ~25% of TLE patients, rising to ~70% in tertiary presurgical cohorts, illustrating ascertainment differences between general and surgical populations. (blumcke2013internationalconsensusclassification pages 1-2)

### 3.4 HPO term suggestions (non-exhaustive; based on described features)
Because HPO identifiers are not embedded in the retrieved texts, the following are **suggested mappings** consistent with the described clinical features:
* Focal seizures with impaired awareness; focal autonomic seizures; epigastric aura; automatisms; dystonia; postictal confusion. (ilae2020mesialtemporallobe pages 1-1)
* Memory impairment / declarative memory impairment (especially linked to HS subtype discussions). (middlebrooks2024radiologicclassificationof pages 10-11)

(These are suggestions; exact HPO IDs should be validated against the HPO database.)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and variants
MTLE‑HS is not presented in the retrieved corpus as a single-gene Mendelian disorder; rather, it is supported as a syndrome with **polygenic susceptibility** and heterogeneous upstream causes. (ilae2020mesialtemporallobe pages 1-1, deleu2026theinteractingetiologies pages 6-7)

### 4.2 Susceptibility loci (common variation)
Common variation around **SCN1A** is reported (in the retrieved evidence) as increasing susceptibility to MTLE‑HS when febrile seizures are part of the clinical history, consistent with an excitability–insult interaction model. (deleu2026theinteractingetiologies pages 6-7)

### 4.3 Somatic variants (emerging evidence)
A 2024 case report provides direct evidence of BRAFV600E‑positive neurons within a hippocampus showing ILAE type 1 HS, consistent with a hypothesis that rare somatic mosaicism may contribute in selected cases. (alsalek2024mesialtemporallobe pages 1-3)

### 4.4 Immune-related molecular candidates
Human RNA-seq study reported immune-related differential genes (e.g., HSP90AA1, SOD1) and a candidate regulatory axis SOX2‑OT/miR‑671‑5p/SPP1. (che2024alteredimmunepathways pages 1-2)

### 4.5 Epigenetic information, chromosomal abnormalities, and allele frequencies
Not explicitly reported in the retrieved evidence corpus.

---

## 5. Environmental information
The ILAE syndrome definition and HS classification literature emphasizes early-life precipitating events (including febrile seizures, hypoxia, intracranial infection, and head trauma) as commonly reported antecedents; however, the retrieved corpus does not quantify environmental exposures beyond the febrile status epilepticus imaging-risk relationship described in FEBSTAT. (ilae2020mesialtemporallobe pages 1-1, lewis2024hippocampalsclerosisand pages 1-3)

---

## 6. Mechanism / pathophysiology
### 6.1 Core pathology: hippocampal sclerosis and ILAE HS subtypes
The ILAE 2013 consensus defines HS as segmental pyramidal cell loss of Ammon’s horn with reactive astrogliosis, and standardizes three HS types (ILAE types 1–3) based on subfield neuronal loss and gliosis patterns. Type 1 (severe CA1+CA4) is most common and is associated with early precipitating injuries and favorable postsurgical seizure control. (Epilepsia; Jul 2013; https://doi.org/10.1111/epi.12220) (blumcke2013internationalconsensusclassification pages 2-4, blumcke2013internationalconsensusclassification pages 1-2)

**Visual evidence:** the ILAE HS subtype patterns and semiquantitative scoring are shown in the extracted Table/Figure images. (blumcke2013internationalconsensusclassification media 00cbc9f7, blumcke2013internationalconsensusclassification media 925dc1e6)

### 6.2 Inflammation and glial activation
Human transcriptomic findings support immune activation in TLE‑HS, including signals consistent with glial activation and immune-pathway enrichment, and propose immune regulatory axes as candidate therapeutic targets. (che2024alteredimmunepathways pages 1-2)

In an established animal model, single-cell/single-nucleus and spatial transcriptomics after intrahippocampal kainic acid identified broad inflammatory/stress pathway activation across hippocampal cell types, with upregulation of glial markers such as **Spp1, Trem2, Cd68**, supporting a mechanistic chain where seizures/injury provoke glial activation that may contribute to hippocampal remodeling and epileptogenesis. (Biomarker Research; Sep 2024; https://doi.org/10.1186/s40364-024-00636-3) (liu2024singlecellsinglenucleusand pages 1-2)

### 6.3 Example causal chain (high-level)
One evidence-supported causal chain is: **febrile status epilepticus → acute hippocampal injury (T2 hyperintensity) → later hippocampal sclerosis → increased long-term risk of epilepsy/MTLE**. This is directly supported by FEBSTAT’s prospective imaging-to-outcome association. (lewis2024hippocampalsclerosisand pages 1-3, lewis2024hippocampalsclerosisand pages 3-5)

### 6.4 Suggested ontology terms (to be validated)
* **UBERON (anatomy):** hippocampus; cornu ammonis (CA1–CA4); dentate gyrus; amygdala; parahippocampal gyrus. (ilae2020mesialtemporallobe pages 1-1, middlebrooks2024radiologicclassificationof pages 5-7)
* **CL (cell types):** astrocyte; microglial cell; neuron (hippocampal pyramidal neuron; granule cell). (che2024alteredimmunepathways pages 1-2, liu2024singlecellsinglenucleusand pages 1-2)
* **GO biological process (mechanism-level suggestions):** gliogenesis/astrocyte activation; microglial activation; inflammatory response; synaptic remodeling; regulation of neuronal excitability (suggested; mechanistic support via immune-pathway enrichment and glial activation evidence). (che2024alteredimmunepathways pages 1-2, liu2024singlecellsinglenucleusand pages 1-2)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary system: **central nervous system**, specifically the **mesial temporal lobe limbic network** including hippocampus, amygdala, and parahippocampal gyrus. (ilae2020mesialtemporallobe pages 1-1)

### 7.2 Tissue/cell level
HS is characterized by selective neuronal loss in hippocampal subfields with reactive astrogliosis; subtype patterns emphasize CA1 vs CA4/dentate involvement. (blumcke2013internationalconsensusclassification pages 2-4, middlebrooks2024radiologicclassificationof pages 5-7)

### 7.3 Lateralization
MTLE‑HS is commonly unilateral or asymmetric. (ilae2020mesialtemporallobe pages 1-1)

---

## 8. Temporal development
### 8.1 Onset
The ILAE definition notes frequent association with an early-life precipitating event (often within the first five years) followed by a latent seizure-free period prior to chronic epilepsy. (ilae2020mesialtemporallobe pages 1-1)

### 8.2 Progression
The ILAE definition describes a tendency toward later drug refractoriness and progressive behavioral/memory deficits. (ilae2020mesialtemporallobe pages 1-1)

---

## 9. Inheritance and population
### 9.1 Epidemiology
The retrieved evidence corpus does not provide population prevalence/incidence for MTLE‑HS. However, it provides surgical-series frequency and cohort-selection markers: HS was identified in **33.6%** of cases in large epilepsy surgery series, and MRI evidence of hippocampal atrophy is reported in ~25% of outpatient TLE series vs ~70% of tertiary presurgical cohorts. (blumcke2013internationalconsensusclassification pages 1-2)

### 9.2 Inheritance pattern
The evidence supports MTLE‑HS as typically **multifactorial / complex**, with common-variant susceptibility (e.g., SCN1A-region association in the context of febrile seizures) and rare somatic mosaic findings in selected reports rather than a single Mendelian inheritance pattern. (deleu2026theinteractingetiologies pages 6-7, alsalek2024mesialtemporallobe pages 1-3)

---

## 10. Diagnostics
### 10.1 Clinical diagnostic approach (syndrome-level)
Diagnosis relies on establishing limbic/mesial temporal seizure onset and evidence of HS, integrating clinical semiology with neurophysiology and neuroimaging, per ILAE syndrome definition. (ilae2020mesialtemporallobe pages 1-1)

### 10.2 MRI: 2024 radiology advances (high priority)
A 2024 AJNR review emphasizes that “binary” MRI assessment (HS yes/no) misses subfield-predominant HS (types 2/3), and proposes an MRI radiologic classification aligned with the ILAE pathology types. Conventional MRI hallmarks include **hippocampal atrophy**, **increased T2 signal**, and **loss of internal architecture**. (AJNR; Feb 2024; https://doi.org/10.3174/ajnr.a8214) (middlebrooks2024radiologicclassificationof pages 1-3)

Key 2024 implementation detail: high-resolution **oblique coronal T2 turbo spin echo** orthogonal to the hippocampal long axis is emphasized; the paper states T2‑FLAIR is not recommended as the primary screening sequence. (middlebrooks2024radiologicclassificationof pages 7-9)

Radiologic subtype mapping (MRI vs ILAE pathology):
* **Type 1 (classic):** severe volume loss across all subfields (or severe CA1 + hilum loss with CA2/CA3 sparing). (middlebrooks2024radiologicclassificationof pages 7-9)
* **Type 2:** CA1‑predominant disproportionate loss with loss of normal CA1 tapering. (middlebrooks2024radiologicclassificationof pages 5-7, middlebrooks2024radiologicclassificationof pages 9-10)
* **Type 3:** hilar (CA4/dentate gyrus)‑predominant disproportionate loss with CA1–CA3 preserved. (middlebrooks2024radiologicclassificationof pages 5-7)
* **No HS:** no subfield volume loss. (middlebrooks2024radiologicclassificationof pages 7-9)

### 10.3 Histopathology (surgical tissue)
The ILAE HS classification provides a semiquantitative scoring approach using neuronal and gliosis markers (e.g., NeuN, GFAP) and standardized CA subfield assessment to assign HS type 1–3 or no-HS category. (blumcke2013internationalconsensusclassification pages 2-4, blumcke2013internationalconsensusclassification pages 1-2)

### 10.4 Differential diagnosis
Not systematically addressed in the retrieved evidence corpus; however, the ILAE HS consensus notes that HS-like changes may occur in elderly non-epileptic brains after anoxic/ischemic injury, underscoring the need for clinicopathologic correlation. (blumcke2013internationalconsensusclassification pages 2-4)

---

## 11. Outcome / prognosis
### 11.1 Surgical prognosis (general)
The ILAE HS pathology consensus reports that surgical resection for drug-resistant TLE is associated with postoperative seizure freedom in ~**60–80%** at 2 years (in appropriately selected patients), with variation by HS subtype (type 1 generally more favorable). (blumcke2013internationalconsensusclassification pages 2-4, blumcke2013internationalconsensusclassification pages 1-2)

### 11.2 Minimally invasive ablation outcomes: real-world registry data
A prospective US multicenter registry (LAANTERN) reported 2‑year seizure outcomes after LITT for drug-resistant MTLE: **58.4% Engel class I** (45/77) and **57.2% ILAE class 1/2** (44/77) at 2 years among those with 2‑year follow-up; adverse events occurred in **16.5%** (mostly mild/transient), and QOL scores improved at almost all time points. (JAMA Neurology; Jul 2025; https://doi.org/10.1001/jamaneurol.2025.1897) (landazuri2025interstitialthermaltherapy pages 1-2)

---

## 12. Treatment
### 12.1 Pharmacotherapy
The retrieved corpus provides syndrome-level statements that MTLE‑HS often becomes drug‑refractory over time, but does not specify comparative antiseizure medication regimens. (ilae2020mesialtemporallobe pages 1-1)

### 12.2 Surgery and ablation (current real-world implementation)
**Resective surgery (e.g., anterior temporal lobectomy / mesial temporal resection)** is established as a key treatment for drug-resistant MTLE‑HS, with reported seizure-freedom rates in the 60–80% range at ~2 years in consensus sources. (blumcke2013internationalconsensusclassification pages 2-4)

**Laser interstitial thermal therapy (LITT)** is increasingly implemented in specialized epilepsy centers; prospective registry outcomes indicate clinically meaningful seizure control with short hospital stays (median 1 day) and generally mild/transient adverse events. (landazuri2025interstitialthermaltherapy pages 1-2)

### 12.3 Neuromodulation and experimental interventional trials (ClinicalTrials.gov)
The retrieved trial records indicate several ongoing or completed interventional studies targeting MTLE (including MTLE‑HS).

* **SEEG-guided RF thermocoagulation vs anterior temporal lobectomy (ATL) in mTLE with HS** – NCT03941613 (Xuanwu Hospital, Beijing). Randomized, parallel, double-masked trial; primary outcome cognitive function at 1 year; secondary outcomes include Engel seizure outcome at 1 year, QOL, complications; enrollment 40; completed 2023‑01‑05. (ClinicalTrials.gov) (NCT03941613 chunk 1)

* **AMT‑260 gene therapy** – NCT06063850 (UniQure; Phase 1/2a; recruiting). One-time intracerebral AAV9 gene therapy (AAV9‑hSyn1‑miGRIK2) via MRI‑guided convection-enhanced delivery; targets **GRIK2** (GluK2 kainate receptor) via miRNA silencing; primary outcome adverse events over 1 year; enrollment 12; adults 18–75 with unilateral refractory MTLE and unilateral hippocampal pathology. (ClinicalTrials.gov) (NCT06063850 chunk 1)

* **NRTX‑1001 cell therapy** – NCT05135091 (Neurona Therapeutics; recruiting). Intracerebral administration of allogeneic human embryonic stem cell–derived GABAergic inhibitory interneurons; Phase 1/2 with subsequent Phase 3 sham-controlled randomized component; safety endpoints include serious/severe adverse events over 1 year and seizure-frequency change endpoints. (ClinicalTrials.gov) (NCT05135091 chunk 1)

### 12.4 MAXO term suggestions (to be validated)
* Epilepsy surgery; anterior temporal lobectomy; laser interstitial thermal therapy; stereotactic EEG–guided radiofrequency thermocoagulation; intracerebral gene therapy; neural cell transplantation; transcranial magnetic stimulation (for network modulation studies). (NCT03941613 chunk 1, NCT06063850 chunk 1, NCT05135091 chunk 1, NCT06521437 chunk 1)

---

## 13. Prevention
Evidence in the retrieved corpus supports **secondary prevention / risk stratification** concepts after febrile status epilepticus via early MRI biomarkers: FEBSTAT indicates that acute hippocampal T2 hyperintensity identifies a subgroup at higher risk for later HS and MTLE, suggesting a practical framework for closer monitoring and potential future preventive trials. (lewis2024hippocampalsclerosisand pages 1-3)

No established primary prevention interventions were identified in the retrieved evidence corpus.

---

## 14. Other species / natural disease
No naturally occurring MTLE‑HS analogs in other species were explicitly documented in the retrieved evidence corpus.

---

## 15. Model organisms
A 2024 mechanistic study used a **mouse intrahippocampal kainic-acid** model to induce TLE and performed scRNA‑seq, snRNA‑seq, and spatial transcriptomics, generating a hippocampal atlas of glial and neuronal transcriptomic changes supporting inflammatory activation and altered cell interactions as candidate mechanisms relevant to HS development and epileptogenesis. (liu2024singlecellsinglenucleusand pages 1-2)

Suggested model categories for MTLE‑HS (supported by retrieved evidence):
* **Chemoconvulsant/lesion-based models:** kainic acid intrahippocampal model. (liu2024singlecellsinglenucleusand pages 1-2)

---

# Notes on citation requirements and limitations
* **PMIDs:** The retrieved full-text snippets and trial records do not include PMIDs; therefore PMIDs cannot be supplied from this evidence set.
* **Ontology IDs (MONDO/MeSH/ICD/Orphanet/OMIM):** Not present in the retrieved sources; therefore not reported here.
* **2023–2024 prioritization:** Key 2024 sources used include FEBSTAT (Epilepsia 2024), AJNR radiologic classification (2024), immune-pathway RNA‑seq (Scientific Reports 2024), and mouse single-cell/spatial atlas (Biomarker Research 2024). (lewis2024hippocampalsclerosisand pages 1-3, middlebrooks2024radiologicclassificationof pages 7-9, che2024alteredimmunepathways pages 1-2, liu2024singlecellsinglenucleusand pages 1-2)


References

1. (ilae2020mesialtemporallobe pages 1-1): … the ILAE Commission on Neurosurgery of Epilepsy. Mesial temporal lobe epilepsy with hippocampal sclerosis. Definitions, Feb 2020. URL: https://doi.org/10.32388/zvebpt, doi:10.32388/zvebpt. This article has 604 citations.

2. (blumcke2013internationalconsensusclassification pages 1-2): Ingmar Blümcke, Maria Thom, Eleonora Aronica, Dawna D. Armstrong, Fabrice Bartolomei, Andrea Bernasconi, Neda Bernasconi, Christian G. Bien, Fernando Cendes, Roland Coras, J. Helen Cross, Thomas S. Jacques, Philippe Kahane, Gary W. Mathern, Haijme Miyata, Solomon L. Moshé, Buge Oz, Çiğdem Özkara, Emilio Perucca, Sanjay Sisodiya, Samuel Wiebe, and Roberto Spreafico. International consensus classification of hippocampal sclerosis in temporal lobe epilepsy: a task force report from the ilae commission on diagnostic methods. Epilepsia, 54:1315-1329, Jul 2013. URL: https://doi.org/10.1111/epi.12220, doi:10.1111/epi.12220. This article has 1269 citations and is from a domain leading peer-reviewed journal.

3. (blumcke2013internationalconsensusclassification pages 2-4): Ingmar Blümcke, Maria Thom, Eleonora Aronica, Dawna D. Armstrong, Fabrice Bartolomei, Andrea Bernasconi, Neda Bernasconi, Christian G. Bien, Fernando Cendes, Roland Coras, J. Helen Cross, Thomas S. Jacques, Philippe Kahane, Gary W. Mathern, Haijme Miyata, Solomon L. Moshé, Buge Oz, Çiğdem Özkara, Emilio Perucca, Sanjay Sisodiya, Samuel Wiebe, and Roberto Spreafico. International consensus classification of hippocampal sclerosis in temporal lobe epilepsy: a task force report from the ilae commission on diagnostic methods. Epilepsia, 54:1315-1329, Jul 2013. URL: https://doi.org/10.1111/epi.12220, doi:10.1111/epi.12220. This article has 1269 citations and is from a domain leading peer-reviewed journal.

4. (middlebrooks2024radiologicclassificationof pages 1-3): Erik H. Middlebrooks, Vivek Gupta, Amit K. Agarwal, Brin E. Freund, Steven A. Messina, William O. Tatum, David S. Sabsevitz, Anteneh M. Feyissa, Seyed M. Mirsattari, Fernando N. Galan, Alfredo Quinones-Hinojosa, Sanjeet S. Grewal, and John V. Murray. Radiologic classification of hippocampal sclerosis in epilepsy. American Journal of Neuroradiology, 45:1185-1193, Feb 2024. URL: https://doi.org/10.3174/ajnr.a8214, doi:10.3174/ajnr.a8214. This article has 21 citations and is from a peer-reviewed journal.

5. (middlebrooks2024radiologicclassificationof pages 5-7): Erik H. Middlebrooks, Vivek Gupta, Amit K. Agarwal, Brin E. Freund, Steven A. Messina, William O. Tatum, David S. Sabsevitz, Anteneh M. Feyissa, Seyed M. Mirsattari, Fernando N. Galan, Alfredo Quinones-Hinojosa, Sanjeet S. Grewal, and John V. Murray. Radiologic classification of hippocampal sclerosis in epilepsy. American Journal of Neuroradiology, 45:1185-1193, Feb 2024. URL: https://doi.org/10.3174/ajnr.a8214, doi:10.3174/ajnr.a8214. This article has 21 citations and is from a peer-reviewed journal.

6. (middlebrooks2024radiologicclassificationof pages 7-9): Erik H. Middlebrooks, Vivek Gupta, Amit K. Agarwal, Brin E. Freund, Steven A. Messina, William O. Tatum, David S. Sabsevitz, Anteneh M. Feyissa, Seyed M. Mirsattari, Fernando N. Galan, Alfredo Quinones-Hinojosa, Sanjeet S. Grewal, and John V. Murray. Radiologic classification of hippocampal sclerosis in epilepsy. American Journal of Neuroradiology, 45:1185-1193, Feb 2024. URL: https://doi.org/10.3174/ajnr.a8214, doi:10.3174/ajnr.a8214. This article has 21 citations and is from a peer-reviewed journal.

7. (middlebrooks2024radiologicclassificationof pages 9-10): Erik H. Middlebrooks, Vivek Gupta, Amit K. Agarwal, Brin E. Freund, Steven A. Messina, William O. Tatum, David S. Sabsevitz, Anteneh M. Feyissa, Seyed M. Mirsattari, Fernando N. Galan, Alfredo Quinones-Hinojosa, Sanjeet S. Grewal, and John V. Murray. Radiologic classification of hippocampal sclerosis in epilepsy. American Journal of Neuroradiology, 45:1185-1193, Feb 2024. URL: https://doi.org/10.3174/ajnr.a8214, doi:10.3174/ajnr.a8214. This article has 21 citations and is from a peer-reviewed journal.

8. (lewis2024hippocampalsclerosisand pages 1-3): Darrell V. Lewis, James Voyvodic, Shlomo Shinnar, Stephen Chan, Jacqueline A. Bello, Solomon L. Moshé, Douglas R. Nordli, L. Matthew Frank, John M. Pellock, Dale C. Hesdorffer, Yuan Xu, Ruth C. Shinnar, Syndi Seinfeld, Leon G. Epstein, David Masur, William Gallentine, Erica Weiss, Xiaoyan Deng, and Shumei Sun. Hippocampal sclerosis and temporal lobe epilepsy following febrile status epilepticus: the febstat study. Epilepsia, 65:1568-1580, Apr 2024. URL: https://doi.org/10.1111/epi.17979, doi:10.1111/epi.17979. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (lewis2024hippocampalsclerosisand pages 3-5): Darrell V. Lewis, James Voyvodic, Shlomo Shinnar, Stephen Chan, Jacqueline A. Bello, Solomon L. Moshé, Douglas R. Nordli, L. Matthew Frank, John M. Pellock, Dale C. Hesdorffer, Yuan Xu, Ruth C. Shinnar, Syndi Seinfeld, Leon G. Epstein, David Masur, William Gallentine, Erica Weiss, Xiaoyan Deng, and Shumei Sun. Hippocampal sclerosis and temporal lobe epilepsy following febrile status epilepticus: the febstat study. Epilepsia, 65:1568-1580, Apr 2024. URL: https://doi.org/10.1111/epi.17979, doi:10.1111/epi.17979. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (che2024alteredimmunepathways pages 1-2): Xiang-Qian Che, Shi-Kun Zhan, Jiao-Jiao Song, Yu-Lei Deng, Wei-Liu, Peng-Huang, Jing-Zhang, Zhan-Fang Sun, Zai-Qian Che, and Jun Liu. Altered immune pathways in patients of temporal lobe epilepsy with and without hippocampal sclerosis. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63541-7, doi:10.1038/s41598-024-63541-7. This article has 11 citations and is from a peer-reviewed journal.

11. (liu2024singlecellsinglenucleusand pages 1-2): Quanlei Liu, Chunhao Shen, Yang Dai, Ting Tang, Changkai Hou, Hongyi Yang, Yihe Wang, Jinkun Xu, Yongchang Lu, Yunming Wang, Yongzhi Shan, Penghu Wei, and Guoguang Zhao. Single-cell, single-nucleus and xenium-based spatial transcriptomics analyses reveal inflammatory activation and altered cell interactions in the hippocampus in mice with temporal lobe epilepsy. Biomarker Research, Sep 2024. URL: https://doi.org/10.1186/s40364-024-00636-3, doi:10.1186/s40364-024-00636-3. This article has 33 citations and is from a peer-reviewed journal.

12. (deleu2026theinteractingetiologies pages 6-7): Boris Deleu, Jules Jeuris, and Wim Van Paesschen. The interacting etiologies of hippocampal sclerosis in epilepsy: a scoping review. Epilepsia, 67:527-541, Oct 2026. URL: https://doi.org/10.1111/epi.18676, doi:10.1111/epi.18676. This article has 2 citations and is from a domain leading peer-reviewed journal.

13. (landazuri2025interstitialthermaltherapy pages 1-2): Patrick Landazuri, Jennifer J. Cheng, Eric Leuthardt, Albert H. Kim, Derek G. Southwell, Peter E. Fecci, Joseph Neimat, David Sun, Bradley Lega, Fedor Panov, Veronica Chiang, Taylor Abel, Sharona Ben-Haim, David E. Piccioni, Jerry J. Shih, Viktoras Palys, Analiz Rodriguez, S. Kathleen Bandt, Joseph Petronio, Michel Lacroix, and James Baumgartner. Interstitial thermal therapy in mesial temporal lobe epilepsy. JAMA neurology, Jul 2025. URL: https://doi.org/10.1001/jamaneurol.2025.1897, doi:10.1001/jamaneurol.2025.1897. This article has 9 citations and is from a highest quality peer-reviewed journal.

14. (alsalek2024mesialtemporallobe pages 1-3): Samir Alsalek, Alexander S. Himstead, Scott Self, Gianna M. Fote, Sumeet Vadera, Edwin S. Monuki, Mari Perez-Rosendahl, and William H. Yong. Mesial temporal lobe epilepsy and hippocampal sclerosis associated with brafv600e mutant neurons in the cornu ammonis: an uncertain pathogenesis and a diagnostic challenge. Free neuropathology, Jan 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5269, doi:10.17879/freeneuropathology-2024-5269. This article has 1 citations and is from a peer-reviewed journal.

15. (blumcke2013internationalconsensusclassification pages 12-13): Ingmar Blümcke, Maria Thom, Eleonora Aronica, Dawna D. Armstrong, Fabrice Bartolomei, Andrea Bernasconi, Neda Bernasconi, Christian G. Bien, Fernando Cendes, Roland Coras, J. Helen Cross, Thomas S. Jacques, Philippe Kahane, Gary W. Mathern, Haijme Miyata, Solomon L. Moshé, Buge Oz, Çiğdem Özkara, Emilio Perucca, Sanjay Sisodiya, Samuel Wiebe, and Roberto Spreafico. International consensus classification of hippocampal sclerosis in temporal lobe epilepsy: a task force report from the ilae commission on diagnostic methods. Epilepsia, 54:1315-1329, Jul 2013. URL: https://doi.org/10.1111/epi.12220, doi:10.1111/epi.12220. This article has 1269 citations and is from a domain leading peer-reviewed journal.

16. (deleu2026theinteractingetiologies pages 1-2): Boris Deleu, Jules Jeuris, and Wim Van Paesschen. The interacting etiologies of hippocampal sclerosis in epilepsy: a scoping review. Epilepsia, 67:527-541, Oct 2026. URL: https://doi.org/10.1111/epi.18676, doi:10.1111/epi.18676. This article has 2 citations and is from a domain leading peer-reviewed journal.

17. (middlebrooks2024radiologicclassificationof pages 10-11): Erik H. Middlebrooks, Vivek Gupta, Amit K. Agarwal, Brin E. Freund, Steven A. Messina, William O. Tatum, David S. Sabsevitz, Anteneh M. Feyissa, Seyed M. Mirsattari, Fernando N. Galan, Alfredo Quinones-Hinojosa, Sanjeet S. Grewal, and John V. Murray. Radiologic classification of hippocampal sclerosis in epilepsy. American Journal of Neuroradiology, 45:1185-1193, Feb 2024. URL: https://doi.org/10.3174/ajnr.a8214, doi:10.3174/ajnr.a8214. This article has 21 citations and is from a peer-reviewed journal.

18. (blumcke2013internationalconsensusclassification media 00cbc9f7): Ingmar Blümcke, Maria Thom, Eleonora Aronica, Dawna D. Armstrong, Fabrice Bartolomei, Andrea Bernasconi, Neda Bernasconi, Christian G. Bien, Fernando Cendes, Roland Coras, J. Helen Cross, Thomas S. Jacques, Philippe Kahane, Gary W. Mathern, Haijme Miyata, Solomon L. Moshé, Buge Oz, Çiğdem Özkara, Emilio Perucca, Sanjay Sisodiya, Samuel Wiebe, and Roberto Spreafico. International consensus classification of hippocampal sclerosis in temporal lobe epilepsy: a task force report from the ilae commission on diagnostic methods. Epilepsia, 54:1315-1329, Jul 2013. URL: https://doi.org/10.1111/epi.12220, doi:10.1111/epi.12220. This article has 1269 citations and is from a domain leading peer-reviewed journal.

19. (blumcke2013internationalconsensusclassification media 925dc1e6): Ingmar Blümcke, Maria Thom, Eleonora Aronica, Dawna D. Armstrong, Fabrice Bartolomei, Andrea Bernasconi, Neda Bernasconi, Christian G. Bien, Fernando Cendes, Roland Coras, J. Helen Cross, Thomas S. Jacques, Philippe Kahane, Gary W. Mathern, Haijme Miyata, Solomon L. Moshé, Buge Oz, Çiğdem Özkara, Emilio Perucca, Sanjay Sisodiya, Samuel Wiebe, and Roberto Spreafico. International consensus classification of hippocampal sclerosis in temporal lobe epilepsy: a task force report from the ilae commission on diagnostic methods. Epilepsia, 54:1315-1329, Jul 2013. URL: https://doi.org/10.1111/epi.12220, doi:10.1111/epi.12220. This article has 1269 citations and is from a domain leading peer-reviewed journal.

20. (NCT03941613 chunk 1):  SEEG Guided RF-TC v.s. ATL for mTLE With HS. Xuanwu Hospital, Beijing. 2019. ClinicalTrials.gov Identifier: NCT03941613

21. (NCT06063850 chunk 1):  AMT-260 Gene Therapy Study in Adults With Unilateral Refractory Mesial Temporal Lobe Epilepsy. UniQure Biopharma B.V.. 2024. ClinicalTrials.gov Identifier: NCT06063850

22. (NCT05135091 chunk 1):  Study of NRTX-1001 Neural Cell Therapy in Drug-Resistant Unilateral Mesial Temporal Lobe Epilepsy (EPIC (EPIlepsy Cell Therapy)). Neurona Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05135091

23. (NCT06521437 chunk 1):  Hippocampal Network Function in Epilepsy. University of Chicago. 2024. ClinicalTrials.gov Identifier: NCT06521437
