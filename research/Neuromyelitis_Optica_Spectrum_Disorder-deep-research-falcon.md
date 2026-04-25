---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-23T18:35:12.164815'
end_time: '2026-04-23T18:52:34.920735'
duration_seconds: 1042.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuromyelitis Optica Spectrum Disorder
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Neuromyelitis Optica Spectrum Disorder** covering all of the
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
- **Disease Name:** Neuromyelitis Optica Spectrum Disorder
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Neuromyelitis Optica Spectrum Disorder** covering all of the
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


# Neuromyelitis Optica Spectrum Disorder (NMOSD): Comprehensive Disease Characteristics Report (2023–2024 Emphasis)

## Executive summary
Neuromyelitis optica spectrum disorder (NMOSD) is a rare, predominantly relapsing autoimmune inflammatory disorder of the central nervous system (CNS) that classically affects the optic nerves and spinal cord and is frequently associated with pathogenic aquaporin-4 immunoglobulin G (AQP4-IgG) autoantibodies. Consensus diagnostic criteria (IPND 2015) stratify diagnosis by AQP4-IgG serostatus and define six “core clinical characteristics.” Major recent developments include broad implementation of cell-based AQP4-IgG assays, biomarker work (serum GFAP and neurofilament light chain), and multiple targeted relapse-prevention therapies with high-level clinical trial evidence (C5 complement inhibitors, IL-6 receptor blockade) plus real-world post-marketing surveillance data. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, rodin2024solublebiomarkersfor pages 1-2)

| Evidence domain | Source (year) | Journal | URL | Key findings | Citation |
|---|---|---|---|---|---|
| Diagnostic criteria / identifiers | Wingerchuk et al. (2015) | *Neurology* | https://doi.org/10.1212/WNL.0000000000001729 | IPND 2015 unified the term **NMOSD** and stratified diagnosis by **AQP4-IgG status**. **AQP4-IgG-positive:** ≥1 core clinical characteristic + positive AQP4-IgG (best available assay) + exclusion of alternatives. **AQP4-IgG-negative/unknown:** ≥2 core clinical characteristics from ≥1 attacks, with ≥1 being optic neuritis, acute myelitis with LETM, or area postrema syndrome; dissemination in space; additional MRI requirements; exclusion of alternatives. Six core characteristics: optic neuritis, acute myelitis, area postrema syndrome, acute brainstem syndrome, symptomatic narcolepsy/acute diencephalic syndrome with typical MRI lesions, symptomatic cerebral syndrome with typical lesions. | (bennett2016findingnmothe pages 11-12, wingerchuk2015internationalconsensusdiagnostic pages 3-3, wingerchuk2015internationalconsensusdiagnostic pages 2-3) |
| Epidemiology | Briggs & Shaia (2024) | *Multiple Sclerosis Journal* | https://doi.org/10.1177/13524585231224683 | 2022 U.S. EHR-based prevalence: **6.88/100,000** (1,772 NMOSD patients among 25,743,039). By race: **Black 12.99/100,000**, **Asian 9.41/100,000**, **White 5.58/100,000**. By sex: **female 9.48/100,000**, **male 3.52/100,000**; observed female:male ratio **3.5:1**. Estimated **~22,000 Americans** living with NMOSD in 2022; **15,413 females** and **6,233 males**. | (briggs2024prevalenceofneuromyelitis pages 1-3, briggs2024prevalenceofneuromyelitis media c3f20c73) |
| Eculizumab pivotal trial (PREVENT) | Pittock et al. (2019) | *New England Journal of Medicine* | https://doi.org/10.1056/NEJMoa1900866 | In AQP4-IgG-positive NMOSD, adjudicated relapses occurred in **3/96 (3%)** on eculizumab vs **20/47 (43%)** on placebo; hazard ratio **0.06 (95% CI 0.02–0.20; P<0.001)**. Adjudicated annualized relapse rate: **0.02** vs **0.35**. Baseline annualized relapse rate over prior 24 months: **1.99±0.94**. | (pittock2019eculizumabinaquaporin4–positive pages 4-5) |
| Eculizumab real-world implementation | Nakashima et al. (2023) | *Therapeutic Advances in Neurological Disorders* | https://doi.org/10.1177/17562864231181177 | Japan post-marketing surveillance: safety set **71**; effectiveness set **68**; **94.4% female**; mean age at initiation **50.7 years**. Relapse rate decreased from **0.74/patient-year** in the 2 years pre-eculizumab to **0.02/patient-year** after initiation. Adverse events in **19/71 (26.8%)**; adverse drug reactions **10/71 (14.1%)**; serious ADRs **7/71 (9.9%)**; **no meningococcal infections** reported. | (nakashima2023longtermsafetyand pages 1-2) |
| Ravulizumab phase 3 | Pittock et al. (2024) | *Canadian Journal of Neurological Sciences* | https://doi.org/10.1017/cjn.2024.119 | CHAMPION-NMOSD interim analysis: **58** patients; median follow-up **138.4 weeks** (range **11.0–183.1**), **153.9 patient-years**. **No adjudicated on-trial relapses** across primary treatment period and long-term extension. **91.4% (53/58)** had stable/improved Hauser Ambulation Index; **91.4% (53/58)** had no clinically important EDSS worsening. TEAEs **94.8%**; serious AEs **25.9%**; withdrawal due to TEAE in **1** patient. | (pittock2024p.011efficacyand pages 1-1) |
| Ravulizumab PK/PD | Ortiz et al. (2024) | *Frontiers in Neurology* | https://doi.org/10.3389/fneur.2024.1332890 | In **58** treated AQP4+ NMOSD patients, ravulizumab achieved serum concentrations above therapeutic threshold (**≥175 μg/mL**) in all patients after first dose and maintained for **50 weeks**. Immediate and complete terminal complement inhibition achieved by end of first infusion: free C5 **<0.5 μg/mL** throughout treatment. Week-50 mean Cmax **1,887.6 μg/mL**, mean Ctrough **764.4 μg/mL**. | (ortiz2024immediateandsustained pages 1-2) |
| Biomarker trial analysis / inebilizumab | Aktas et al. (2023) | *Journal of Neurology, Neurosurgery & Psychiatry* | https://doi.org/10.1136/jnnp-2022-330412 | In N-MOmentum biomarker analysis, attack-time **sNfL** was the strongest predictor of disability worsening at attack and follow-up; attack-time cut-off **32 pg/mL** predicted post-attack disability worsening with **AUC 0.71 (95% CI 0.51–0.89; P=0.02)**. At randomized-period end, fewer inebilizumab-treated than placebo-treated participants had **sNfL >16 pg/mL**: **22% vs 45%**; OR **0.36 (95% CI 0.17–0.76; P=0.004)**. | (aktas2023serumneurofilamentlight pages 7-8, aktas2023serumneurofilamentlight pages 1-2) |
| Biomarker cutoffs | Aktas et al. (2023) | *Journal of Neurology, Neurosurgery & Psychiatry* | https://doi.org/10.1136/jnnp-2022-330412 | Prespecified elevated serum biomarker thresholds: **sGFAP >170 pg/mL** and **sNfL >16 pg/mL** (>2 SD above healthy donors). Elevated baseline prevalence in AQP4+ participants: **~30%** for sGFAP and **37%** for sNfL. Among **198** AQP4+ participants there were **32** adjudicated attacks; **20** had >2-fold increase in sGFAP, **12** had >2-fold change in sNfL. sNfL remained elevated **>7 days** after attack onset whereas sGFAP returned toward baseline faster. | (aktas2023serumneurofilamentlight pages 2-3, aktas2023serumneurofilamentlight pages 4-5) |
| GFAP effect size | Shaygannejad et al. (2024) | *Medicina* | https://doi.org/10.3390/medicina60071050 | Systematic review/meta-analysis: serum GFAP in NMOSD vs healthy controls showed pooled **SMD 0.90 (95% CI 0.73–1.07; P<0.001; I²=10%)**, supporting GFAP as an astrocytopathy-linked biomarker. | (shaygannejad2024theroleof pages 1-2) |
| Biomarker overview | Rodin & Chitnis (2024) | *Frontiers in Neurology* | https://doi.org/10.3389/fneur.2024.1415535 | Review summary: **sGFAP commonly rises ~4–20× above recent baseline within <1 week of attack** and higher baseline sGFAP predicts shorter time to next attack (reported hazard ratios **~3–11** across studies). **sNfL** declines more slowly and may remain elevated for **months to years**; AQP4-IgG is diagnostically useful but not reliable for monitoring activity or treatment response. | (rodin2024solublebiomarkersfor pages 1-2) |


*Table: This table compiles high-yield NMOSD evidence from retrieved sources, covering diagnostic criteria, epidemiology, major therapies, and biomarker findings with quantitative results, journals, URLs, and citations.*

## 1. Disease information

### 1.1 Overview (what is the disease?)
NMOSD is defined clinically by inflammatory demyelinating attacks involving the optic nerve, spinal cord, and additional CNS regions (e.g., area postrema/dorsal medulla, brainstem, diencephalon, cerebrum). The IPND 2015 consensus emphasizes integrating clinical, serologic, and neuroimaging data, and explicitly states that diagnosis is not based on AQP4-IgG alone. (wingerchuk2015internationalconsensusdiagnostic pages 2-3)

### 1.2 Key identifiers and ontology cross-references
* **Consensus definition / diagnostic anchor:** International Panel for NMO Diagnosis (IPND) 2015 criteria (Neurology, July 2015) (wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* **MONDO / OMIM / Orphanet / ICD-10 / ICD-11 / MeSH:** Not retrievable from the current tool context; therefore not asserted here.

### 1.3 Common synonyms / alternative names
* “Neuromyelitis optica” (NMO) is described as a related/preceding term unified under “NMOSD” in the IPND 2015 nomenclature. (wingerchuk2015internationalconsensusdiagnostic pages 2-3)

### 1.4 Evidence source type
The report integrates:
* **Aggregated disease-level resources:** IPND consensus criteria (wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* **Real-world aggregated EHR data:** U.S. prevalence analysis using TriNetX network (briggs2024prevalenceofneuromyelitis pages 1-3)
* **Randomized controlled trials and trial-derived biomarker analyses:** PREVENT (eculizumab), SAkuraStar (satralizumab), N-MOmentum biomarker analyses, CHAMPION-NMOSD interim (ravulizumab). (pittock2019eculizumabinaquaporin4–positive pages 4-5, traboulsee2020safetyandefficacy pages 1-2, aktas2023serumneurofilamentlight pages 2-3, pittock2024p.011efficacyand pages 1-1)
* **Post-marketing surveillance:** Japan eculizumab all-case surveillance. (nakashima2023longtermsafetyand pages 1-2)

## 2. Etiology

### 2.1 Primary causal factors (current understanding)
AQP4-IgG–positive NMOSD is widely conceptualized as an antibody-mediated autoimmune astrocytopathy in which AQP4-IgG targets AQP4 on astrocytic endfeet, triggering downstream complement activation and cellular cytotoxicity mechanisms leading to tissue injury. (thangaleela2023neuromyelitisopticaspectrum pages 1-2)

### 2.2 Risk factors

#### Demographic risk patterns
A large U.S. EHR-based prevalence analysis (2022 prevalence estimate; publication Jan 2024) reported clear sex and race differences: overall prevalence 6.88/100,000, higher in females (9.48/100,000) than males (3.52/100,000), and highest in Black individuals (12.99/100,000) followed by Asian individuals (9.41/100,000) and White individuals (5.58/100,000). (briggs2024prevalenceofneuromyelitis pages 1-3, briggs2024prevalenceofneuromyelitis media c3f20c73)

#### Infectious / microbiome-associated triggers and gene–environment hypotheses
A 2024 review of gut microbiota in NMOSD reported that **20–30% of recurrent NMOSD cases have preceding infections** and described molecular mimicry evidence involving *Clostridium perfringens*: AQP4-specific T-cell epitopes have ~90% homology to bacterial peptide sequences (ABC-TP), and patient Th17 cells proliferate in response to the corresponding bacterial peptide, supporting cross-reactivity as a plausible trigger/amplifier of AQP4-targeted immunity. (yao2024theroleof pages 5-6, yao2024theroleof pages 6-8)

#### Genetic susceptibility (examples from recent review synthesis)
A 2023 review summarized HLA associations reported across populations (e.g., HLA-DRB1*03; HLA-DRB1*05:01; DRB1*1602) and additional immune-gene polymorphism signals (e.g., IL-17 gene polymorphism; PD-1 receptor polymorphism), noting population specificity. (thangaleela2023neuromyelitisopticaspectrum pages 2-4)

### 2.3 Protective factors
No clearly established protective genetic or environmental factors were retrievable in the current evidence context.

### 2.4 Gene–environment interactions
The microbiome-driven molecular mimicry hypothesis (AQP4 peptide homology with bacterial antigens and Th17 cross-reactivity) is a concrete gene–environment interaction model: genetic susceptibility shaping adaptive immune responses, while environmental microbial exposures provide cross-reactive epitopes and inflammatory milieu. (yao2024theroleof pages 6-8)

## 3. Phenotypes

### 3.1 Core clinical phenotypes and suggested HPO terms
The IPND 2015 diagnostic framework defines six **core clinical characteristics** (phenotype anchors) (bennett2016findingnmothe pages 11-12, wingerchuk2015internationalconsensusdiagnostic pages 3-3):
1. **Optic neuritis** — suggested HPO: *Optic neuritis* (HP:0001088)
2. **Acute myelitis** — suggested HPO: *Myelitis* (HP:0002380); and for LETM: *Longitudinally extensive transverse myelitis* (clinical descriptor; HPO mapping may be represented by spinal cord inflammatory lesion terms)
3. **Area postrema syndrome** (“hiccups; nausea and vomiting”) — suggested HPO: *Intractable hiccups* (HP:0010817), *Nausea* (HP:0002018), *Vomiting* (HP:0002013)
4. **Acute brainstem syndrome** — suggested HPO: *Brainstem dysfunction* (HP:0002363)
5. **Symptomatic narcolepsy or acute diencephalic clinical syndrome with NMOSD-typical diencephalic MRI lesions** — suggested HPO: *Narcolepsy* (HP:0002526)
6. **Symptomatic cerebral syndrome with NMOSD-typical brain lesions** — suggested HPO: *Seizure* (HP:0001250) and broader cerebral dysfunction terms depending on presentation

### 3.2 Phenotype characteristics (onset/course)
NMOSD is typically episodic/relapsing, and relapse prevention is emphasized because single attacks can cause severe and irreversible disability. CHAMPION-NMOSD interim data support disability stability (91.4% without clinically important EDSS worsening), consistent with effective relapse prevention in treated cohorts. (pittock2024p.011efficacyand pages 1-1)

### 3.3 Laboratory and imaging-related phenotypes
For AQP4-IgG seronegative or unknown cases, IPND 2015 requires additional MRI features tailored to the clinical syndrome (e.g., LETM ≥3 contiguous vertebral segments; dorsal medulla/area postrema lesions; periependymal brainstem lesions). (wingerchuk2015internationalconsensusdiagnostic pages 3-4)

### 3.4 Quality-of-life impact
Validated QoL instrument statistics (e.g., EQ-5D, SF-36) were not retrievable in the current evidence context. However, the disease burden is implied by attack-related disability risks and the emphasis on relapse prevention to avoid irreversible impairment. (rodin2024solublebiomarkersfor pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes
NMOSD is not a monogenic disorder in the retrieved evidence. Instead, it is primarily an autoimmune disease defined by pathogenic autoantibodies (AQP4-IgG) and associated immunogenetic susceptibility signals. (thangaleela2023neuromyelitisopticaspectrum pages 2-4)

### 4.2 Key molecular targets and biomarkers
* **AQP4 (aquaporin-4):** main autoantigen in a large fraction of NMOSD, forming the basis for AQP4-IgG serologic stratification. (wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* **Complement C5:** therapeutic target for eculizumab and ravulizumab (terminal complement inhibition). (ortiz2024immediateandsustained pages 1-2, pittock2019eculizumabinaquaporin4–positive pages 4-5)
* **IL-6 receptor:** therapeutic target for satralizumab. (traboulsee2020safetyandefficacy pages 1-2)

### 4.3 Epigenetics / chromosomal abnormalities
Not retrievable from current context.

## 5. Environmental information

### 5.1 Infectious agents and microbiome-related exposures
The microbiome literature implicated *Clostridium perfringens* enrichment and proposed molecular mimicry and toxin-mediated mechanisms (epsilon toxin crossing BBB and damaging CNS cells). (yao2024theroleof pages 6-8)

### 5.2 Lifestyle factors
Not supported with specific quantitative evidence in the retrieved context.

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (AQP4-IgG+ NMOSD)
A mechanistic summary supported by recent reviews:
1. **Peripheral AQP4-IgG** (and AQP4-reactive T/B cell responses) exist systemically.
2. **CNS access** occurs during blood–brain barrier (BBB) dysfunction, enabling AQP4-IgG to reach astrocytic endfeet.
3. **Binding of AQP4-IgG to AQP4** triggers astrocyte injury via **complement-dependent cytotoxicity (CDC)** and **antibody-dependent cellular cytotoxicity (ADCC)**.
4. Complement activation culminates in **membrane attack complex (MAC)** formation and inflammatory recruitment.
5. Downstream consequences include **astrocyte loss (GFAP changes), demyelination, and neuronal injury**, producing clinical attacks. (thangaleela2023neuromyelitisopticaspectrum pages 1-2, xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 1-2)

### 6.2 Key pathways (suggested GO terms)
* **Complement activation, classical pathway** (GO:0006958)
* **Antibody-mediated complement activation** (GO:0002560)
* **Antibody-dependent cellular cytotoxicity** (GO:0001788)
* **Inflammatory response** (GO:0006954)
* **Blood–brain barrier disruption / regulation of BBB permeability** (conceptual; GO terms may include regulation of endothelial barrier function)

### 6.3 Cell types involved (suggested CL terms)
* **Astrocyte** (CL:0000127)
* **Microglial cell** (CL:0000129)
* **Macrophage** (CL:0000235)
* **Neutrophil** (CL:0000775)
* **B cell / plasmablast** (B cell CL:0000236; plasmablast CL:0000980)

### 6.4 Anatomical localization (suggested UBERON)
* **Optic nerve** (UBERON:0001890)
* **Spinal cord** (UBERON:0002240)
* **Area postrema (dorsal medulla)** (UBERON:0001937)
* **Brainstem** (UBERON:0002298)
* **Diencephalon** (UBERON:0001896)

### 6.5 Distinction from MOG antibody-associated disease (MOGAD)
A 2023 pathology review emphasizes that **MOGAD pathology is principally inflammatory demyelination without astrocyte destruction**, contrasting with AQP4-positive NMOSD where complement deposition and astrocyte-targeted injury are central concepts. (pittock2024p.011efficacyand pages 1-1)

## 7. Anatomical structures affected
Primary: optic nerves and spinal cord; additional CNS regions as per IPND core characteristics (area postrema/dorsal medulla, brainstem, diencephalon, cerebrum). (bennett2016findingnmothe pages 11-12)

## 8. Temporal development
NMOSD is commonly relapsing with discrete attacks; IPND criteria require at least one clinical attack and note that asymptomatic AQP4-IgG positivity is insufficient for diagnosis. (wingerchuk2015internationalconsensusdiagnostic pages 3-3)

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
A U.S. 2022 prevalence estimate using a large aggregated EHR network (TriNetX; 55 healthcare organizations; 25.7 million patients) found 6.88/100,000 prevalence overall with marked sex/race differences and an estimated ~22,000 Americans living with NMOSD in 2022. (briggs2024prevalenceofneuromyelitis pages 1-3, briggs2024prevalenceofneuromyelitis media c3f20c73, briggs2024prevalenceofneuromyelitis media be629dae)

### 9.2 Inheritance
No Mendelian inheritance pattern is supported by retrieved evidence; disease is best described as multifactorial autoimmune with immunogenetic susceptibility signals. (thangaleela2023neuromyelitisopticaspectrum pages 2-4)

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria (IPND 2015)
The IPND 2015 criteria define NMOSD and stratify diagnosis by AQP4-IgG status:
* **NMOSD with AQP4-IgG:** (1) ≥1 core clinical characteristic; (2) positive AQP4-IgG using best available method; (3) exclusion of alternative diagnoses. (bennett2016findingnmothe pages 11-12, wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* **NMOSD without AQP4-IgG (or unknown):** ≥2 core clinical characteristics from ≥1 attacks, requiring dissemination in space and additional MRI requirements, with at least one of optic neuritis, acute myelitis with LETM, or area postrema syndrome. (bennett2016findingnmothe pages 11-12, wingerchuk2015internationalconsensusdiagnostic pages 3-3)

### 10.2 Laboratory testing
AQP4-IgG testing is central, and cell-based assays are recommended as best-available detection methods. (wingerchuk2015internationalconsensusdiagnostic pages 3-3, bennett2016findingnmothe pages 3-4)

### 10.3 Differential diagnosis (examples)
NMOSD is differentiated from multiple sclerosis and other inflammatory myelopathies using clinical pattern plus MRI requirements (e.g., LETM, area postrema lesions) and supportive CSF features; oligoclonal bands can be absent in a large fraction of cases, which can be helpful in differentiation. (baranello2015neuromyelitisopticaspectrum pages 5-5, wingerchuk2015internationalconsensusdiagnostic pages 3-4)

## 11. Outcome / prognosis
Relapse prevention strongly influences prognosis. In CHAMPION-NMOSD interim data, no adjudicated on-trial relapses were observed and disability measures were stable for most patients over a median follow-up of 138.4 weeks. (pittock2024p.011efficacyand pages 1-1)

## 12. Treatment

### 12.1 Acute attack management (contextual)
Acute attacks are commonly managed with high-dose corticosteroids and escalation strategies such as apheresis (plasmapheresis) per historical standards; specific quantitative acute-therapy outcomes were not retrieved in this context. (baranello2015neuromyelitisopticaspectrum pages 5-5)

### 12.2 Maintenance relapse-prevention therapies (targeted biologics)

#### Complement C5 inhibitors
* **Eculizumab (PREVENT; NEJM; Aug 2019)**: Adjudicated relapses occurred in **3/96 (3%)** eculizumab vs **20/47 (43%)** placebo; hazard ratio **0.06 (95% CI 0.02–0.20; P<0.001)**; ARR **0.02 vs 0.35**. (pittock2019eculizumabinaquaporin4–positive pages 4-5)
* **Eculizumab real-world (Japan PMS; Jan 2023)**: relapse rate fell from **0.74/patient-year** (pre-treatment) to **0.02/patient-year** after initiation; no meningococcal infections in interim analysis; steroid-sparing observed (prednisolone >10 mg/day dropped to 0% by 100–104 weeks). (nakashima2023longtermsafetyand pages 1-2)
* **Ravulizumab (CHAMPION-NMOSD interim; May 2024 abstract)**: **0 adjudicated on-trial relapses** in **58** patients across primary period + extension; TEAEs 94.8% and serious AEs 25.9%. (pittock2024p.011efficacyand pages 1-1)

#### IL-6 receptor blockade
* **Satralizumab monotherapy (SAkuraStar; Lancet Neurology; May 2020)**: protocol-defined relapses in **19/63 (30%)** satralizumab vs **16/32 (50%)** placebo; hazard ratio **0.45 (95% CI 0.23–0.89; p=0.018)**. (traboulsee2020safetyandefficacy pages 1-2)
* A secondary summary source reports AQP4-IgG+ subgroup hazard ratio **0.26 (0.11–0.63)** (74% risk reduction). (duchow2021satralizumabinthe pages 4-5)

#### B-cell depletion targeting CD19
While the pivotal inebilizumab trial statistics were not directly retrievable here, trial-derived biomarker analyses demonstrate biologic effect on damage markers and suggest potential utility for stratifying relapse severity and recovery:
* Inebilizumab was associated with lower sNfL and sGFAP versus placebo in N-MOmentum biomarker analysis. (aktas2023serumneurofilamentlight pages 1-2)

### 12.3 Biomarkers for monitoring treatment and risk
From a 2023 biomarker analysis (JN Neurol Neurosurg Psychiatry) linked to N-MOmentum:
* Attack-time **sNfL cut-off 32 pg/mL** predicted disability worsening after attacks (AUC 0.71). (aktas2023serumneurofilamentlight pages 1-2)
* Prespecified “elevated” thresholds: **sGFAP >170 pg/mL** and **sNfL >16 pg/mL** (>2 SD above healthy donors). (aktas2023serumneurofilamentlight pages 2-3)

### 12.4 MAXO suggestions (examples)
* **Complement inhibition therapy** (MAXO concept: complement inhibitor administration) — eculizumab/ravulizumab (pittock2019eculizumabinaquaporin4–positive pages 4-5, pittock2024p.011efficacyand pages 1-1)
* **Interleukin-6 receptor antagonist therapy** — satralizumab (traboulsee2020safetyandefficacy pages 1-2)
* **B cell depletion therapy** — inebilizumab (aktas2023serumneurofilamentlight pages 1-2)
* **Plasma exchange therapy** — for acute attack escalation (historical standard; not quantitatively evidenced here) (baranello2015neuromyelitisopticaspectrum pages 5-5)

### 12.5 Current applications / real-world implementation
Post-marketing surveillance in Japan demonstrates real-world deployment of eculizumab, including relapse-rate reduction, monitoring for adverse drug reactions, and steroid-sparing trajectories. (nakashima2023longtermsafetyand pages 1-2)

## 13. Prevention
Primary prevention of NMOSD onset is not established. Practical prevention is predominantly **secondary/tertiary prevention of relapses and disability** via long-term immunotherapy, supported by phase 3 trial evidence and real-world surveillance (e.g., eculizumab PMS). (nakashima2023longtermsafetyand pages 1-2, pittock2019eculizumabinaquaporin4–positive pages 4-5)

Vaccination- and pregnancy-specific prevention guidance was not retrievable in the current context.

## 14. Other species / natural disease
Not established in the retrieved evidence context.

## 15. Model organisms
Experimental systems are largely built on AQP4-IgG pathogenesis:
* **Rodent passive-transfer models**: AQP4-IgG introduction often requires BBB disruption or co-administration of human complement (mice) to recapitulate complement-mediated pathology; rats can develop more NMOSD-like lesions with intact complement. Peripheral administration frequently leads to antibody sequestration in AQP4-expressing peripheral organs rather than CNS deposition unless BBB is breached. (huang2024scientificissueswith pages 1-3)
* **In vitro/ex vivo models**: astrocyte and slice models recapitulate AQP4 loss, astrocytopathy, complement activation, demyelination, and neuronal loss, supporting mechanistic studies and therapeutic screening, but they do not fully capture the human disease process. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 1-2)

## Recent developments and expert analysis (2023–2024)
1. **Epidemiology update (2024):** Large-scale EHR data indicate ~22,000 Americans living with NMOSD in 2022 and highlight substantial race/sex disparities, with the highest prevalence in Black individuals and a strong female predominance. (briggs2024prevalenceofneuromyelitis pages 1-3, briggs2024prevalenceofneuromyelitis media c3f20c73)
2. **Biomarker maturation (2023–2024):** Attack-linked serum biomarkers (GFAP and NfL) show different kinetics and prognostic implications; sNfL at attack predicts post-attack disability worsening and is mitigated by inebilizumab, while sGFAP is tightly linked to astrocytic injury and is elevated in NMOSD vs controls (SMD 0.9). (aktas2023serumneurofilamentlight pages 1-2, shaygannejad2024theroleof pages 1-2)
3. **Expansion of targeted relapse prevention (2024):** Ravulizumab (long-acting C5 inhibitor) shows sustained terminal complement inhibition pharmacodynamically and interim clinical data with no adjudicated on-trial relapses in CHAMPION-NMOSD. (ortiz2024immediateandsustained pages 1-2, pittock2024p.011efficacyand pages 1-1)

## Limitations of this report (evidence gaps)
* Formal ontology identifiers (MONDO, MeSH, Orphanet, ICD-10/ICD-11) were not retrievable via the current tool context.
* QoL instrument outcomes (EQ-5D/SF-36/PROMIS) were not available in retrieved primary evidence.
* Direct inebilizumab pivotal relapse-prevention effect sizes were not retrieved (only biomarker analyses and secondary summaries).

## URLs and publication dates (examples of key sources used)
* Wingerchuk et al., *Neurology* (July 2015): https://doi.org/10.1212/WNL.0000000000001729 (wingerchuk2015internationalconsensusdiagnostic pages 3-3)
* Briggs & Shaia, *Multiple Sclerosis Journal* (Jan 2024): https://doi.org/10.1177/13524585231224683 (briggs2024prevalenceofneuromyelitis pages 1-3)
* Pittock et al., *NEJM* (Aug 2019): https://doi.org/10.1056/NEJMoa1900866 (pittock2019eculizumabinaquaporin4–positive pages 4-5)
* Nakashima et al., *Therapeutic Advances in Neurological Disorders* (Jan 2023): https://doi.org/10.1177/17562864231181177 (nakashima2023longtermsafetyand pages 1-2)
* Ortiz et al., *Frontiers in Neurology* (Jan 2024): https://doi.org/10.3389/fneur.2024.1332890 (ortiz2024immediateandsustained pages 1-2)
* Pittock et al., *Canadian Journal of Neurological Sciences* (May 2024): https://doi.org/10.1017/cjn.2024.119 (pittock2024p.011efficacyand pages 1-1)
* Aktas et al., *JNNP* (May 2023): https://doi.org/10.1136/jnnp-2022-330412 (aktas2023serumneurofilamentlight pages 1-2)
* Rodin & Chitnis, *Frontiers in Neurology* (May 2024): https://doi.org/10.3389/fneur.2024.1415535 (rodin2024solublebiomarkersfor pages 1-2)



References

1. (wingerchuk2015internationalconsensusdiagnostic pages 3-3): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5307 citations and is from a highest quality peer-reviewed journal.

2. (rodin2024solublebiomarkersfor pages 1-2): Rachel E. Rodin and Tanuja Chitnis. Soluble biomarkers for neuromyelitis optica spectrum disorders: a mini review. Frontiers in Neurology, May 2024. URL: https://doi.org/10.3389/fneur.2024.1415535, doi:10.3389/fneur.2024.1415535. This article has 17 citations and is from a peer-reviewed journal.

3. (bennett2016findingnmothe pages 11-12): Jeffrey L. Bennett. Finding nmo: the evolving diagnostic criteria of neuromyelitis optica. Journal of neuro-ophthalmology : the official journal of the North American Neuro-Ophthalmology Society, 36 3:238-45, Sep 2016. URL: https://doi.org/10.1097/wno.0000000000000396, doi:10.1097/wno.0000000000000396. This article has 57 citations.

4. (wingerchuk2015internationalconsensusdiagnostic pages 2-3): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5307 citations and is from a highest quality peer-reviewed journal.

5. (briggs2024prevalenceofneuromyelitis pages 1-3): Farren B S Briggs and Jacqueline Shaia. Prevalence of neuromyelitis optica spectrum disorder in the united states. Multiple Sclerosis Journal, 30:316-324, Jan 2024. URL: https://doi.org/10.1177/13524585231224683, doi:10.1177/13524585231224683. This article has 25 citations.

6. (briggs2024prevalenceofneuromyelitis media c3f20c73): Farren B S Briggs and Jacqueline Shaia. Prevalence of neuromyelitis optica spectrum disorder in the united states. Multiple Sclerosis Journal, 30:316-324, Jan 2024. URL: https://doi.org/10.1177/13524585231224683, doi:10.1177/13524585231224683. This article has 25 citations.

7. (pittock2019eculizumabinaquaporin4–positive pages 4-5): Sean J. Pittock, Achim Berthele, Kazuo Fujihara, Ho Jin Kim, Michael Levy, Jacqueline Palace, Ichiro Nakashima, Murat Terzi, Natalia Totolyan, Shanthi Viswanathan, Kai-Chen Wang, Amy Pace, Kenji P. Fujita, Róisín Armstrong, and Dean M. Wingerchuk. Eculizumab in aquaporin-4–positive neuromyelitis optica spectrum disorder. New England Journal of Medicine, 381:614-625, Aug 2019. URL: https://doi.org/10.1056/nejmoa1900866, doi:10.1056/nejmoa1900866. This article has 948 citations and is from a highest quality peer-reviewed journal.

8. (nakashima2023longtermsafetyand pages 1-2): Ichiro Nakashima, Jin Nakahara, Hiroaki Yokote, Yasuhiro Manabe, Kazumi Okamura, Kou Hasegawa, and Kazuo Fujihara. Long-term safety and effectiveness of eculizumab in patients with aquaporin-4 antibody-positive neuromyelitis optica spectrum disorder: a 2-year interim analysis of post-marketing surveillance in japan. Therapeutic Advances in Neurological Disorders, Jan 2023. URL: https://doi.org/10.1177/17562864231181177, doi:10.1177/17562864231181177. This article has 28 citations and is from a peer-reviewed journal.

9. (pittock2024p.011efficacyand pages 1-1): SJ Pittock, M Barnett, JL Bennett, A Berthele, J de Sèze, M Levy, I Nakashima, C Oreja-Guevara, J Palace, F Paul, C Pozzilli, Y Mashhoon, K Allen, B Parks, H Kim, and G Vorobeychik. P.011 efficacy and safety of ravulizumab in adults with aqp4+ nmosd: interim analysis from the ongoing phase 3 champion-nmosd trial. Canadian Journal of Neurological Sciences / Journal Canadien des Sciences Neurologiques, 51:S17-S17, May 2024. URL: https://doi.org/10.1017/cjn.2024.119, doi:10.1017/cjn.2024.119. This article has 0 citations.

10. (ortiz2024immediateandsustained pages 1-2): Stephan Ortiz, Sean J. Pittock, Achim Berthele, Michael Levy, Ichiro Nakashima, Celia Oreja-Guevara, Kerstin Allen, Yasmin Mashhoon, Becky Parks, and Ho Jin Kim. Immediate and sustained terminal complement inhibition with ravulizumab in patients with anti-aquaporin-4 antibody-positive neuromyelitis optica spectrum disorder. Frontiers in Neurology, Jan 2024. URL: https://doi.org/10.3389/fneur.2024.1332890, doi:10.3389/fneur.2024.1332890. This article has 10 citations and is from a peer-reviewed journal.

11. (aktas2023serumneurofilamentlight pages 7-8): Orhan Aktas, Hans-Peter Hartung, Michael A Smith, William A Rees, Kazuo Fujihara, Friedemann Paul, Romain Marignier, Jeffrey L Bennett, Ho Jin Kim, Brian G Weinshenker, Sean J Pittock, Dean M Wingerchuk, Gary Cutter, Dewei She, Michele Gunsior, Daniel Cimbora, Eliezer Katz, and Bruce A Cree. Serum neurofilament light chain levels at attack predict post-attack disability worsening and are mitigated by inebilizumab: analysis of four potential biomarkers in neuromyelitis optica spectrum disorder. Journal of Neurology, Neurosurgery &amp; Psychiatry, 94:757-768, May 2023. URL: https://doi.org/10.1136/jnnp-2022-330412, doi:10.1136/jnnp-2022-330412. This article has 43 citations.

12. (aktas2023serumneurofilamentlight pages 1-2): Orhan Aktas, Hans-Peter Hartung, Michael A Smith, William A Rees, Kazuo Fujihara, Friedemann Paul, Romain Marignier, Jeffrey L Bennett, Ho Jin Kim, Brian G Weinshenker, Sean J Pittock, Dean M Wingerchuk, Gary Cutter, Dewei She, Michele Gunsior, Daniel Cimbora, Eliezer Katz, and Bruce A Cree. Serum neurofilament light chain levels at attack predict post-attack disability worsening and are mitigated by inebilizumab: analysis of four potential biomarkers in neuromyelitis optica spectrum disorder. Journal of Neurology, Neurosurgery &amp; Psychiatry, 94:757-768, May 2023. URL: https://doi.org/10.1136/jnnp-2022-330412, doi:10.1136/jnnp-2022-330412. This article has 43 citations.

13. (aktas2023serumneurofilamentlight pages 2-3): Orhan Aktas, Hans-Peter Hartung, Michael A Smith, William A Rees, Kazuo Fujihara, Friedemann Paul, Romain Marignier, Jeffrey L Bennett, Ho Jin Kim, Brian G Weinshenker, Sean J Pittock, Dean M Wingerchuk, Gary Cutter, Dewei She, Michele Gunsior, Daniel Cimbora, Eliezer Katz, and Bruce A Cree. Serum neurofilament light chain levels at attack predict post-attack disability worsening and are mitigated by inebilizumab: analysis of four potential biomarkers in neuromyelitis optica spectrum disorder. Journal of Neurology, Neurosurgery &amp; Psychiatry, 94:757-768, May 2023. URL: https://doi.org/10.1136/jnnp-2022-330412, doi:10.1136/jnnp-2022-330412. This article has 43 citations.

14. (aktas2023serumneurofilamentlight pages 4-5): Orhan Aktas, Hans-Peter Hartung, Michael A Smith, William A Rees, Kazuo Fujihara, Friedemann Paul, Romain Marignier, Jeffrey L Bennett, Ho Jin Kim, Brian G Weinshenker, Sean J Pittock, Dean M Wingerchuk, Gary Cutter, Dewei She, Michele Gunsior, Daniel Cimbora, Eliezer Katz, and Bruce A Cree. Serum neurofilament light chain levels at attack predict post-attack disability worsening and are mitigated by inebilizumab: analysis of four potential biomarkers in neuromyelitis optica spectrum disorder. Journal of Neurology, Neurosurgery &amp; Psychiatry, 94:757-768, May 2023. URL: https://doi.org/10.1136/jnnp-2022-330412, doi:10.1136/jnnp-2022-330412. This article has 43 citations.

15. (shaygannejad2024theroleof pages 1-2): Aysa Shaygannejad, Nazanin Rafiei, Saeed Vaheb, Mohammad Yazdan Panah, Vahid Shaygannejad, and Omid Mirmosayyeb. The role of glial fibrillary acidic protein as a biomarker in multiple sclerosis and neuromyelitis optica spectrum disorder: a systematic review and meta-analysis. Medicina, 60:1050, Jun 2024. URL: https://doi.org/10.3390/medicina60071050, doi:10.3390/medicina60071050. This article has 17 citations.

16. (traboulsee2020safetyandefficacy pages 1-2): Anthony Traboulsee, Benjamin M Greenberg, Jeffrey L Bennett, Lech Szczechowski, Edward Fox, Svitlana Shkrobot, Takashi Yamamura, Yusuke Terada, Yuichi Kawata, Padraig Wright, Athos Gianella-Borradori, Hideki Garren, and Brian G Weinshenker. Safety and efficacy of satralizumab monotherapy in neuromyelitis optica spectrum disorder: a randomised, double-blind, multicentre, placebo-controlled phase 3 trial. The Lancet Neurology, 19:402-412, May 2020. URL: https://doi.org/10.1016/s1474-4422(20)30078-8, doi:10.1016/s1474-4422(20)30078-8. This article has 578 citations and is from a highest quality peer-reviewed journal.

17. (thangaleela2023neuromyelitisopticaspectrum pages 1-2): Subramanian Thangaleela, Bhagavathi Sundaram Sivamaruthi, Arumugam Radha, Periyanaina Kesika, and Chaiyavat Chaiyasut. Neuromyelitis optica spectrum disorders: clinical perspectives, molecular mechanisms, and treatments. Applied Sciences, 13:5029, Apr 2023. URL: https://doi.org/10.3390/app13085029, doi:10.3390/app13085029. This article has 10 citations.

18. (yao2024theroleof pages 5-6): Shi-Qi Yao, Xiayin Yang, Ling-Ping Cen, and Shaoying Tan. The role of gut microbiota in neuromyelitis optica spectrum disorder. International Journal of Molecular Sciences, 25:3179, Mar 2024. URL: https://doi.org/10.3390/ijms25063179, doi:10.3390/ijms25063179. This article has 13 citations.

19. (yao2024theroleof pages 6-8): Shi-Qi Yao, Xiayin Yang, Ling-Ping Cen, and Shaoying Tan. The role of gut microbiota in neuromyelitis optica spectrum disorder. International Journal of Molecular Sciences, 25:3179, Mar 2024. URL: https://doi.org/10.3390/ijms25063179, doi:10.3390/ijms25063179. This article has 13 citations.

20. (thangaleela2023neuromyelitisopticaspectrum pages 2-4): Subramanian Thangaleela, Bhagavathi Sundaram Sivamaruthi, Arumugam Radha, Periyanaina Kesika, and Chaiyavat Chaiyasut. Neuromyelitis optica spectrum disorders: clinical perspectives, molecular mechanisms, and treatments. Applied Sciences, 13:5029, Apr 2023. URL: https://doi.org/10.3390/app13085029, doi:10.3390/app13085029. This article has 10 citations.

21. (wingerchuk2015internationalconsensusdiagnostic pages 3-4): Dean M. Wingerchuk, Brenda Banwell, Jeffrey L. Bennett, Philippe Cabre, William Carroll, Tanuja Chitnis, Jérôme de Seze, Kazuo Fujihara, Benjamin Greenberg, Anu Jacob, Sven Jarius, Marco Lana-Peixoto, Michael Levy, Jack H. Simon, Silvia Tenembaum, Anthony L. Traboulsee, Patrick Waters, Kay E. Wellik, and Brian G. Weinshenker. International consensus diagnostic criteria for neuromyelitis optica spectrum disorders. Neurology, 85:177-189, Jul 2015. URL: https://doi.org/10.1212/wnl.0000000000001729, doi:10.1212/wnl.0000000000001729. This article has 5307 citations and is from a highest quality peer-reviewed journal.

22. (xu2025aquaporin4iggseropositiveneuromyelitisoptica pages 1-2): Li Xu, Huiming Xu, and Changyong Tang. Aquaporin-4-igg-seropositive neuromyelitis optica spectrum disorders: progress of experimental models based on disease pathogenesis. Neural Regeneration Research, 20:354-365, Jan 2024. URL: https://doi.org/10.4103/nrr.nrr-d-23-01325, doi:10.4103/nrr.nrr-d-23-01325. This article has 15 citations and is from a peer-reviewed journal.

23. (briggs2024prevalenceofneuromyelitis media be629dae): Farren B S Briggs and Jacqueline Shaia. Prevalence of neuromyelitis optica spectrum disorder in the united states. Multiple Sclerosis Journal, 30:316-324, Jan 2024. URL: https://doi.org/10.1177/13524585231224683, doi:10.1177/13524585231224683. This article has 25 citations.

24. (bennett2016findingnmothe pages 3-4): Jeffrey L. Bennett. Finding nmo: the evolving diagnostic criteria of neuromyelitis optica. Journal of neuro-ophthalmology : the official journal of the North American Neuro-Ophthalmology Society, 36 3:238-45, Sep 2016. URL: https://doi.org/10.1097/wno.0000000000000396, doi:10.1097/wno.0000000000000396. This article has 57 citations.

25. (baranello2015neuromyelitisopticaspectrum pages 5-5): RJ Baranello and JR Avasarala. Neuromyelitis optica spectrum disorders with and without aquaporin 4 antibody: characterization, differential diagnosis, and recent advances. Journal of Neurology and Therapeutics, 1:9-14, Nov 2015. URL: https://doi.org/10.14312/2397-1304.2015-2, doi:10.14312/2397-1304.2015-2. This article has 98 citations.

26. (duchow2021satralizumabinthe pages 4-5): Ankelien Duchow and Judith Bellmann-Strobl. Satralizumab in the treatment of neuromyelitis optica spectrum disorder. Neurodegenerative disease management, 11:49-59, Nov 2021. URL: https://doi.org/10.2217/nmt-2020-0046, doi:10.2217/nmt-2020-0046. This article has 22 citations and is from a peer-reviewed journal.

27. (huang2024scientificissueswith pages 1-3): Yusen Huang, Tian-wei Wang, Fangruyue Wang, Yujing Wu, Jia Ai, Ying Zhang, Meiyan Shao, and Le Fang. Scientific issues with rodent models of neuromyelitis optic spectrum disorders. Frontiers in Immunology, Nov 2024. URL: https://doi.org/10.3389/fimmu.2024.1423107, doi:10.3389/fimmu.2024.1423107. This article has 2 citations and is from a peer-reviewed journal.