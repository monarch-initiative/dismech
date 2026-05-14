---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T12:52:12.283959'
end_time: '2026-05-10T13:22:55.140819'
duration_seconds: 1842.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism** covering all of the
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
- **Disease Name:** Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism** covering all of the
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


## Comprehensive research report: Inborn Disorders of the Methionine Cycle and Sulfur Amino Acid Metabolism (Mendelian category)

### Executive summary
“Inborn disorders of the methionine cycle and sulfur amino acid metabolism” is best treated as a *pathway-based Mendelian disease group* rather than a single entity. In contemporary clinical and newborn-screening practice, this group is operationally subdivided into: (i) **transsulfuration defects** (especially classic homocystinuria due to **CBS** deficiency), (ii) **remethylation defects** (isolated remethylation defects such as **MTHFR** deficiency and **cobalamin-related remethylation/combined defects** such as **cblC/MMACHC**), and (iii) **methionine-cycle entry/SAM-synthesis defects** presenting as isolated hypermethioninemia (notably **MAT1A** deficiency). These disorders share characteristic biochemical patterns involving **methionine (Met)**, **total homocysteine (tHcy)**, and sometimes **methylmalonic acid (MMA)**, and are increasingly addressed through multi-tier newborn-screening algorithms and genotype-informed management. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2, kozich2024komrowermemoriallecture pages 1-2, mucha2024vitaminb12metabolism pages 15-15, ma2024hypermethioninemiadueto pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
This knowledge-base entry refers to a **class of inborn errors** affecting the **methionine cycle (one-carbon metabolism)**, **homocysteine remethylation**, and/or **transsulfuration**. Clinically, the group is often encountered through one of three biochemical “entry points”:
- **Hypermethioninemia** (e.g., MAT1A deficiency; sometimes CBS deficiency) (ma2024hypermethioninemiadueto pages 1-2, kozich2024komrowermemoriallecture pages 3-4)
- **Hyperhomocysteinemia/homocystinuria** (CBS deficiency; remethylation defects) (kozich2024komrowermemoriallecture pages 1-2, mucha2024vitaminb12metabolism pages 10-11)
- **Combined MMA + hyperhomocysteinemia with low methionine** (cobalamin trafficking/processing defects such as cblC) (arhip2024lateonsetmethylmalonicacidemia pages 1-2, mucha2024vitaminb12metabolism pages 9-10)

### 1.2 Identifiers and ontologies
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not explicitly provided in the retrieved full texts; therefore, a definitive mapping to a single MONDO term could not be confirmed from the tool-accessible corpus.
- **ICD-10 coding limitation (important for real-world/EHR work):** In a U.S. claims/EHR analysis, ICD-10 **E72.11** was described as **non-specific** for classical homocystinuria, motivating phenotype/lab-based case-finding algorithms. (jain2024estimatingprevalenceof pages 2-3)
- **OMIM-style identifiers present in NBS epidemiology material:** a Portuguese NBS epidemiology text lists cobalamin subtype disorders with OMIM-like numbers (e.g., “Methylmalonic acidaemia type CblC/D … 277400/277410”). (goncalves2024epidemiologyofrare pages 24-27)

### 1.3 Common synonyms / alternative names (as used in the literature)
- **Classic homocystinuria / Homocystinuria due to CBS deficiency / CBS-deficient homocystinuria (HCU)** (kozich2024komrowermemoriallecture pages 1-2, kozich2024komrowermemoriallecture pages 3-3)
- **Cobalamin C disease / cblC defect / Combined methylmalonic acidemia and homocystinuria, cblC type** (arhip2024lateonsetmethylmalonicacidemia pages 1-2, mucha2024vitaminb12metabolism pages 9-10)
- **Late-onset cblC disease** (arhip2024lateonsetmethylmalonicacidemia pages 1-2)
- **MTHFR deficiency (isolated remethylation disorder)** (reischl‐hajiabadi2024outcomesafternewborn pages 1-2)
- **Methionine adenosyltransferase I/III deficiency / MAT I/III deficiency / MAT1A deficiency (hypermethioninemia)** (ma2024hypermethioninemiadueto pages 1-2)

### 1.4 Evidence source type
Most disease information here is derived from **aggregated disease-level resources** (reviews and systematic reviews) and **cohort studies** (newborn-screening programs, multicenter observational cohorts), with some data also derived from **claims/EHR-linked datasets** for prevalence estimation. (kozich2024komrowermemoriallecture pages 1-2, arhip2024lateonsetmethylmalonicacidemia pages 1-2, goncalves2024portugueseneonatalscreening pages 6-7, jain2024estimatingprevalenceof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
Primary causes are **germline pathogenic variants** in genes encoding enzymes or trafficking proteins in:
- **Transsulfuration**: **CBS** deficiency (AR) (kozich2024komrowermemoriallecture pages 3-4)
- **Remethylation**: e.g., **MTHFR** deficiency (reischl‐hajiabadi2024outcomesafternewborn pages 1-2)
- **Intracellular cobalamin processing/trafficking (remethylation + mitochondrial B12 pathways)**: **MMACHC (cblC)**, **MMADHC (cblD)**, **ABCD4/LMBRD1 (cblJ/cblF)**, and upstream uptake components such as **CD320** (mucha2024vitaminb12metabolism pages 9-10, mucha2024vitaminb12metabolism pages 7-9)
- **Methionine-cycle entry/SAM synthesis**: **MAT1A** (MAT I/III deficiency; can be AD or AR) (ma2024hypermethioninemiadueto pages 1-2)

### 2.2 Risk factors and protective factors
- The dominant driver is **genotype**; additional “risk factors” are most relevant as **diagnostic pitfalls** or **secondary causes of abnormal markers** (e.g., methionine elevations from liver disease/parenteral nutrition can cause false positives in NBS for CBS deficiency). (goncalves2024portugueseneonatalscreening pages 4-6)
- A key *phenotypic modifier* in CBS deficiency is **pyridoxine responsiveness**, repeatedly emphasized as a determinant of biochemical and clinical phenotype. (kozich2024komrowermemoriallecture pages 1-2, kozich2024komrowermemoriallecture pages 3-4)

### 2.3 Gene–environment interaction
The evidence retrieved primarily discusses metabolic biochemistry and screening. However, several sources emphasize that **newborn screening performance and clinical outcomes depend on timing and treatment availability** (environment/health-system interaction), and that screening may miss milder cases when relying on methionine alone. (jain2024estimatingprevalenceof pages 1-2, kozich2024komrowermemoriallecture pages 13-13)

---

## 3. Phenotypes

### 3.1 Core phenotype clusters (with suggested HPO terms)
Because this is a pathway-group, phenotypes are best represented per major disorder subtype.

#### A) CBS-deficient homocystinuria (classic HCU)
- **Organ systems predominantly affected:** “vasculature, central nervous system (CNS), and connective tissue” (kozich2024komrowermemoriallecture pages 3-3)
- **Disease variability:** “broad, extending from severe childhood disease to milder (late) adulthood forms” (kozich2024komrowermemoriallecture pages 1-2)
- **Key modifier:** “pyridoxine responsiveness appears to be the key factor determining the clinical course” (kozich2024komrowermemoriallecture pages 1-2)
- Suggested HPO: 
  - Thromboembolism / vascular events (e.g., HP:0001907 Thrombosis)
  - Developmental delay / intellectual disability (HP:0001263, HP:0001249)
  - Lens dislocation (HP:0001083) and osteoporosis (HP:0000939) are mentioned as later onset in pyridoxine-responsive patients (kozich2024komrowermemoriallecture pages 3-4)

#### B) Late-onset cblC disease (MMACHC)
Systematic review (199 patients) provides frequency-rich phenotype data:
- Neuropathy/myelopathy: **94/199** (often ataxic gait, weakness; spinal cord degeneration) (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Encephalopathy/cognitive decline: **80/199** (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Psychiatric symptoms: **57/199** (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Thrombotic microangiopathy (TMA): **38/199** (acute renal failure + hemolytic anemia + thrombocytopenia + hypertension) (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Seizures: **28/199** (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Pulmonary hypertension with heart failure: **20/199** (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
Suggested HPO (examples):
- Peripheral neuropathy (HP:0009830), Myelopathy (HP:0002141), Ataxia (HP:0001251)
- Cognitive decline (HP:0001268)
- Psychosis (HP:0000709) / Depression (HP:0000716)
- Hemolytic uremic syndrome / TMA (HP:0001905)
- Pulmonary hypertension (HP:0002092)

#### C) Late-onset cblC cohort (85 patients; China)
- Neuropsychiatric symptoms overall: **80.0%** (68/85); cognitive decline: **58.8%** (50/85) (ding2023lateonsetcblcdefect pages 2-4)
- Motor involvement (gait instability/ataxia/weakness/spastic paraplegia): **57.6%** (49/85) (ding2023lateonsetcblcdefect pages 2-4)
- Seizures: **28.2%** (24/85) (ding2023lateonsetcblcdefect pages 2-4)
- Renal disease: **23.5%** (20/85); pulmonary arterial hypertension: **5.9%** (5/85) (ding2023lateonsetcblcdefect pages 2-4)
- Diagnostic delay as prognostic factor: time from onset to diagnosis independently associated with poor outcome (OR=1.025, P=0.024) (ding2023lateonsetcblcdefect pages 1-2)

#### D) MAT1A deficiency (MAT I/III; hypermethioninemia)
- Neurological abnormalities in cohort: **10/15 (66.7%)** including language delay, learning difficulties, abnormal imaging; demyelination associated with higher methionine (ma2024hypermethioninemiadueto pages 5-6)
- Demyelination group baseline methionine: **1102 vs 396 µmol/L** (ma2024hypermethioninemiadueto pages 1-2)
- Suggested HPO: Abnormality of white matter (HP:0002500), Language delay (HP:0000750), Learning difficulties (HP:0001328)

---

## 4. Genetic / molecular information

### 4.1 Causal genes emphasized in retrieved evidence
- **CBS** (classic homocystinuria; AR) with enzyme cofactors/regulators: **PLP**, **SAM (AdoMet)** allosteric activator, **heme** (kozich2024komrowermemoriallecture pages 3-4)
- **MMACHC** (cblC): multiple population-specific pathogenic variants and biochemical phenotype of combined MMA + hyperhomocysteinemia with low methionine (mucha2024vitaminb12metabolism pages 9-10)
- **MMADHC** (cblD): can present as isolated MMA, isolated homocystinuria, or combined MMA/HC (mucha2024vitaminb12metabolism pages 9-10, mucha2024vitaminb12metabolism pages 10-11)
- **LMBRD1/LMBD1** and **ABCD4** (cblF/cblJ) affecting lysosomal export of cobalamin (mucha2024vitaminb12metabolism pages 7-9)
- **CD320** (transcobalamin receptor; KO mouse phenotypes include ↑MMA and ↑homocysteine, macrocytic anemia) (mucha2024vitaminb12metabolism pages 7-9)
- **MAT1A**: AR or AD hypermethioninemia (ma2024hypermethioninemiadueto pages 1-2)

### 4.2 Pathogenic variants (examples explicitly in evidence)
- **MMACHC**: c.482G>A (major focus of large Chinese cohort), plus variants including c.609G>A, c.658_660delAAG, c.80A>G (wu2024variablephenotypesand pages 1-2, mucha2024vitaminb12metabolism pages 9-10)
- **MAT1A**: AD variant example c.791G>A (p.Arg264His) discussed in Portuguese NBS experience; many screened infants were heterozygous and asymptomatic, motivating revised thresholds (goncalves2024epidemiologyofrare pages 50-52)

### 4.3 Functional consequences / mechanisms
- **CBS deficiency:** review emphasizes “misfolding of missense mutations” as a common mechanism and highlights therapeutic directions including “correction of misfolding by chaperones” (kozich2024komrowermemoriallecture pages 1-2, kozich2024komrowermemoriallecture pages 16-17)
- **MMACHC:** described as both **chaperone** and **enzymatic processing** protein (reductive decyanation; glutathione-dependent processing) interacting with methionine synthase to regulate intracellular cobalamin metabolism (mucha2024vitaminb12metabolism pages 9-10)

---

## 5. Environmental information
For the Mendelian disorders summarized here, environmental factors mainly influence **screening specificity** and **secondary biochemical changes** rather than primary disease causation.
- Example: methionine elevations in NBS can be caused by **secondary methionine elevations** (e.g., liver disease, parenteral nutrition), which can generate false positives for CBS deficiency screening. (goncalves2024portugueseneonatalscreening pages 4-6)

---

## 6. Mechanism / pathophysiology

### 6.1 Pathway overview and causal chains
- **CBS deficiency (transsulfuration block):** impaired conversion of homocysteine into cystathionine/cysteine causes accumulation of upstream metabolites (tHcy, often Met), driving vascular/CNS/connective-tissue complications; PLP dependence and SAM regulation explain vitamin responsiveness and methylation-state interactions. (kozich2024komrowermemoriallecture pages 3-4, kozich2024komrowermemoriallecture pages 3-3)
- **Remethylation/cobalamin disorders (cblC):** impaired intracellular B12 handling disrupts methylcobalamin-dependent methionine synthase and adenosylcobalamin-dependent mutase pathways, producing **hyperhomocysteinemia + MMA elevation** and **low methionine**; multisystem injury includes neuropsychiatric disease, renal TMA, pulmonary hypertension and thrombosis. (arhip2024lateonsetmethylmalonicacidemia pages 1-2, mucha2024vitaminb12metabolism pages 10-11)
- **MAT1A deficiency:** reduced hepatic SAM synthesis produces persistent hypermethioninemia and (in severe persistent cases) CNS white-matter injury/demyelination; methionine thresholds correlate with risk. (ma2024hypermethioninemiadueto pages 1-2, ma2024hypermethioninemiadueto pages 6-8)

A key supporting visual schematic of the methionine cycle/transsulfuration disruptions in CBS-deficient homocystinuria is provided in Kožich & Majtan (Figure shown). (kozich2024komrowermemoriallecture media e1534ecc)

### 6.2 Suggested GO terms (examples)
- Homocysteine metabolic process (GO:0000096)
- Methionine metabolic process (GO:0006555)
- Transsulfuration (GO:0000097)
- One-carbon metabolic process (GO:0006730)

### 6.3 Suggested CL (cell ontology) and tissue context
Evidence emphasizes **liver** as a key tissue for MAT1A (hepatic expression supports liver-targeted interventions) and systemic vascular/CNS involvement for CBS deficiency; cobalamin disorders have multi-organ involvement including kidney and nervous system. (ma2024hypermethioninemiadueto pages 8-8, kozich2024komrowermemoriallecture pages 3-3, arhip2024lateonsetmethylmalonicacidemia pages 4-5)

---

## 7. Anatomical structures affected

### 7.1 Organ systems (evidence-backed)
- CBS deficiency: “vasculature, CNS, connective tissue” (kozich2024komrowermemoriallecture pages 3-3)
- cblC: frequent involvement of nervous system and kidney (TMA/kidney disease), plus pulmonary vasculature (pulmonary hypertension) (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- MAT1A deficiency: brain white matter/demyelination (ma2024hypermethioninemiadueto pages 1-2)

Suggested UBERON examples:
- Brain (UBERON:0000955)
- Kidney (UBERON:0002113)
- Blood vessel (UBERON:0001981)

---

## 8. Temporal development

- **CBS deficiency:** ranges from severe childhood disease to mild adult/late-onset forms; pyridoxine responsiveness linked to later onset of complications. (kozich2024komrowermemoriallecture pages 1-2, kozich2024komrowermemoriallecture pages 3-4)
- **Late-onset cblC:** onset can be in school-age through adulthood; diagnostic delay can be months to years and predicts outcomes. (ding2023lateonsetcblcdefect pages 1-2, arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- **MTHFR deficiency:** untreated infants develop symptoms at median age ~1–2 months in cited context; early diagnosis is crucial. (reischl‐hajiabadi2024outcomesafternewborn pages 13-13)

---

## 9. Inheritance and population

### 9.1 Inheritance patterns (as evidenced)
- CBS deficiency: autosomal recessive (kozich2024komrowermemoriallecture pages 3-4)
- cblC (MMACHC): autosomal recessive (stated in multiple clinical sources; implied by biallelic cohorts) (arhip2024lateonsetmethylmalonicacidemia pages 4-5, mucha2024vitaminb12metabolism pages 9-10)
- MAT1A deficiency: autosomal recessive and autosomal dominant forms described (ma2024hypermethioninemiadueto pages 1-2)

### 9.2 Epidemiology statistics (recent)
- Portuguese NBS (2004–2022, 1,764,830 neonates): classical homocystinuria detected **4 cases**, birth prevalence **1:441,208**; table also cites estimated worldwide birth prevalence **1:243,902**. (goncalves2024portugueseneonatalscreening pages 6-7)
- U.S. prevalence estimate (claims/EHR-linked Optum dataset; publication Sep 2024): reported worldwide prevalence range **1:200,000–1:335,000** with Qatar incidence **1:1,800**; projected U.S. standardized prevalence **5.29 per 100,000 (broad)** and **1.04 per 100,000 (strict)** for 2016–2020. (jain2024estimatingprevalenceof pages 1-2)
- Hong Kong expanded NBS program (2015–2022): overall IMD prevalence **1 in 2,674**; recall rate decreased from **0.26% to 0.12%** after second-tier testing; **78.7%** of confirmed IMD cases asymptomatic at time of NBS result. (belaramani2024expandednewbornscreening pages 1-2)
- Multicenter NBS with NGS+MS/MS (29,601 newborns): overall IEM incidence **1 in 1,287**; MS/MS PPV **5.29%**, NGS PPV **70.83%**; carrier frequency for **MMACHC 1:52** in that cohort. (tang2024newbornscreeningfor pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical laboratory biomarkers
- **CBS deficiency:** first-tier NBS marker is **methionine**; false positives from secondary methionine elevations; second-tier DBS **tHcy** improves specificity (implemented in Portugal in 2017). (goncalves2024portugueseneonatalscreening pages 4-6)
- **Remethylation/cobalamin disorders:** second-tier biomarkers include **tHcy** and **MMA**; remethylation disorders may show **decreased methionine** (goncalves2024epidemiologyofrare pages 30-33, goncalves2024portugueseneonatalscreening pages 4-6)

### 10.2 Newborn screening practice (real-world implementation)
- Review of global practice notes NBS for HCU using methionine, Met/Phe ratio, and second-tier DBS tHcy by LC–MS/MS to reduce false positives. (kozich2024komrowermemoriallecture pages 13-13)
- German multi-tier algorithm pilot includes CBS deficiency and remethylation disorders (cblC, MTHFR) detected through a multiple-tier approach with meaningful outcome differences by disorder. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2)

### 10.3 Genomic screening and gene panels
- A 2024 multicenter study of NGS+MS/MS as first-tier screening reported higher PPV for NGS than MS/MS (but lower sensitivity), supporting ongoing experimentation with genomic NBS workflows. (tang2024newbornscreeningfor pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Newborn-screened outcomes (recent cohort)
German multicenter observational follow-up after NBS (median follow-up 3.6 years):
- IMD cohort included cblC (N=5), MTHFR (N=2), CBS (N=1). Overall, **17/27 (63%)** had ≥1 decompensation; two thirds experienced decompensation (PA/MMA/cblC). At follow-up, **all cblC** developed “permanent, mostly neurological symptoms,” whereas **MTHFR and CBS** remained asymptomatic. “Survival was favorable” for screened individuals with MMA, cblC, MTHFR, CBS during the study interval. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2, reischl‐hajiabadi2024outcomesafternewborn pages 10-11)

### 11.2 Late-onset cblC outcomes
Systematic review (199 patients): outcomes across literature were **64 recovered**, **78 improved**, **4 did not improve/progressed**, and **12 died**, supporting treatability but highlighting residual morbidity and mortality. (arhip2024lateonsetmethylmalonicacidemia pages 4-5)

### 11.3 Prognostic factors
Diagnostic delay in late-onset cblC is an independent risk factor for poor outcome (OR=1.025, P=0.024). (ding2023lateonsetcblcdefect pages 1-2)

---

## 12. Treatment

### 12.1 Classic homocystinuria (CBS deficiency)
- Review emphasizes pyridoxine responsiveness as key determinant of course, and highlights emerging therapy directions: “gene therapy, correction of misfolding by chaperones, removal of methionine from the gut and enzyme therapies that decrease homocysteine or methionine in the circulation.” (kozich2024komrowermemoriallecture pages 1-2)
- Mechanistic basis includes PLP cofactor dependence and SAM regulation, supporting vitamin- and metabolism-directed therapy concepts. (kozich2024komrowermemoriallecture pages 3-4)

Suggested MAXO (examples):
- Vitamin supplementation therapy (MAXO:0000782)
- Dietary methionine restriction (MAXO term suggestion; not explicitly enumerated in evidence as MAXO-coded)

### 12.2 cblC disease (MMACHC)
- Late-onset systematic review: most patients were treated with **parenteral hydroxocobalamin** (117), with common adjuncts **betaine (134)**, **folic acid (127)**, **L-carnitine (79)**, **vitamin B6 (15)**. (arhip2024lateonsetmethylmalonicacidemia pages 4-5)
- Large MMACHC c.482G>A cohort suggests NBS-detected patients largely remain asymptomatic, and overall mortality is low in that variant-defined group; NBS and pre-symptomatic treatment correlate with favorable neurodevelopment outcomes. (wu2024variablephenotypesand pages 1-2)

Suggested MAXO (examples):
- Hydroxocobalamin administration (MAXO term suggestion)
- Betaine therapy (MAXO term suggestion)

### 12.3 MAT1A deficiency
- Cohort treatments: low-methionine diet often insufficient; SAMe/ademethionine reduced methionine in some; **liver transplantation** normalized methionine in a refractory case and was associated with clinical/imaging improvement. (ma2024hypermethioninemiadueto pages 5-6, ma2024hypermethioninemiadueto pages 6-8)

---

## 13. Prevention

### 13.1 Secondary prevention via newborn screening
Newborn screening (with second-tier testing) is the major proven population-level prevention strategy for morbidity in this pathway group.
- Portuguese program implemented second-tier tHcy for HCU in 2017 to improve specificity. (goncalves2024portugueseneonatalscreening pages 4-6)
- Hong Kong program showed recall rate reduction after second-tier testing. (belaramani2024expandednewbornscreening pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary/OMIA evidence was retrieved in the tool-accessible corpus. However, comparative biology is heavily used in experimental modeling (mouse, zebrafish, invertebrate models) for mechanism and therapy development. (kozich2024komrowermemoriallecture pages 7-8, mathew2024vitaminb12deficiency pages 10-11)

---

## 15. Model organisms

### 15.1 CBS deficiency (homocystinuria)
- Yeast functional assay platform: saturation codon-mutagenesis of human CBS expressed in yeast lacking the ortholog enabled growth-selection functional scoring for variant interpretation. (kozich2024komrowermemoriallecture pages 7-7)
- Mouse models: KO (neonatal lethality), inducible KO, human transgene “Human Only” model, and Tg-I278T used for pathophysiology and therapeutic testing; other taxa include C. elegans, Drosophila, and zebrafish (kozich2024komrowermemoriallecture pages 7-8)

### 15.2 Cobalamin/remethylation models
- Mouse models: CD320 KO mice on B12-deficient diet show ↑MMA and ↑homocysteine and macrocytic anemia; Mmachc conditional and overexpression lines exist (mucha2024vitaminb12metabolism pages 7-9, mathew2024vitaminb12deficiency pages 10-11)
- Zebrafish: mmachc mutants/morphants; rodents: gastrectomy and N2O models; cell models include SH-SY5Y neuronal cells with caveats about media B12 levels (mathew2024vitaminb12deficiency pages 10-11)

---

## Key recent (2023–2024) developments and expert analysis
1. **Phenotype stratification and therapeutics in CBS deficiency:** A 2024 authoritative lecture-review emphasizes decades of progress in CBS biology and argues that pyridoxine responsiveness is the “key factor” for clinical course, while new therapies (gene therapy, chaperones, enzyme therapies, and gut methionine removal) are active areas. (kozich2024komrowermemoriallecture pages 1-2)
2. **Evidence that NBS benefit is disorder-dependent:** In a 2024 German NBS pilot outcome study, outcomes for CBS and MTHFR were favorable, while cblC still showed frequent persistent neurologic symptoms despite early detection—highlighting residual unmet need and the importance of disorder-specific natural history. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2, reischl‐hajiabadi2024outcomesafternewborn pages 10-11)
3. **Large genotype-defined cblC cohort supports NBS and variant-specific prognosis:** The MMACHC c.482G>A cohort (median follow-up ~3.7 years) demonstrates that NBS-detected individuals are often asymptomatic and that this variant associates with milder, later-onset phenotypes and better response to hydroxocobalamin. (wu2024variablephenotypesand pages 1-2)
4. **MAT1A deficiency re-evaluated as not always benign:** A 2024 cohort argues MAT I/III deficiency “is not just a benign disease,” associating severe persistent hypermethioninemia with white-matter brain injury and suggesting transplantation for refractory cases. (ma2024hypermethioninemiadueto pages 1-2, ma2024hypermethioninemiadueto pages 6-8)

---

## Consolidated disorder summary table
| Disorder/group | Key gene(s) | Pathway node | Hallmark biochemical pattern (Met, tHcy, MMA) | Typical presentation/onset | Key treatments | Key recent evidence (study type, year) |
|---|---|---|---|---|---|---|
| Classic homocystinuria (CBS deficiency, HCU) | **CBS** | Transsulfuration | Typically **↑ tHcy**, **↑ Met**, low cystathionine/cysteine in CBS block | Broad spectrum from severe childhood disease to milder late/adult forms; major involvement of **vasculature, CNS, connective tissue**; clinical course strongly modified by pyridoxine responsiveness | **Pyridoxine** in responsive patients, methionine restriction/dietary therapy; emerging approaches include **gene therapy, chaperones, gut methionine removal, enzyme therapies** | 2024 review/lecture: Kožich & Majtan, *J Inherit Metab Dis* 2024, DOI: **10.1002/jimd.12767** (kozich2024komrowermemoriallecture pages 1-2, kozich2024komrowermemoriallecture pages 3-4, kozich2024komrowermemoriallecture pages 3-3) |
| cblC disease (combined methylmalonic acidemia and homocystinuria, cobalamin C type) | **MMACHC** | Cobalamin trafficking / remethylation + mitochondrial cobalamin utilization | **↓ Met**, **↑ tHcy**, **↑ MMA** | Variable pediatric-to-adult spectrum; neurologic, renal, hematologic, ophthalmologic disease; in a 2024 cohort with MMACHC c.482G>A, many NBS-detected cases remained asymptomatic | **Hydroxocobalamin** (often IM), **betaine**, folate/folinic acid, L-carnitine; better outcomes with pre-symptomatic treatment | 2024 cohort: Wu et al., *World J Pediatr* 2024, DOI: **10.1007/s12519-023-00770-2**; 2024 review: Mucha et al., *Int J Mol Sci* 2024, DOI: **10.3390/ijms25158021** (wu2024variablephenotypesand pages 1-2, mucha2024vitaminb12metabolism pages 9-10) |
| Late-onset cblC disease | **MMACHC** | Cobalamin trafficking / remethylation + mitochondrial cobalamin utilization | **↓ Met**, **↑ tHcy**, **↑ MMA** | Onset after infancy/childhood to adulthood; common phenotypes include **neuropathy/myelopathy, encephalopathy/cognitive decline, psychiatric symptoms, TMA/kidney disease, seizures, pulmonary hypertension** | Usually **parenteral hydroxocobalamin** plus **betaine**, folate/folinic acid, L-carnitine; improvement common but sequelae frequent if diagnosis delayed | 2024 systematic review of **199** patients: Arhip et al., *Orphanet J Rare Dis* 2024, DOI: **10.1186/s13023-024-03021-3**; 2023 cohort of **85** late-onset cases: Ding et al., *Orphanet J Rare Dis* 2023, DOI: **10.1186/s13023-023-02890-4** (arhip2024lateonsetmethylmalonicacidemia pages 4-5, arhip2024lateonsetmethylmalonicacidemia pages 1-2, ding2023lateonsetcblcdefect pages 2-4, ding2023lateonsetcblcdefect pages 1-2) |
| MTHFR deficiency (isolated remethylation disorder in NBS cohorts) | **MTHFR** | Remethylation / methionine cycle | Expected remethylation pattern: **↓ Met**, **↑ tHcy**, no MMA elevation emphasized in cited NBS context | Infantile disease can become symptomatic at **1–2 months** if untreated; in NBS cohort, pre-symptomatic children remained well through early follow-up | Early treatment per current guidelines; remethylation-supportive therapy used clinically; NBS plus specialized metabolic care associated with favorable outcomes | 2024 multicenter observational NBS outcome study: Reischl-Hajiabadi et al., *J Inherit Metab Dis* 2024, DOI: **10.1002/jimd.12731** (reischl‐hajiabadi2024outcomesafternewborn pages 1-2, reischl‐hajiabadi2024outcomesafternewborn pages 13-13) |
| MAT I/III deficiency (hypermethioninemia due to MAT1A deficiency) | **MAT1A** | Methionine cycle (AdoMet synthesis; first step) | **Persistent isolated ↑ Met**; **tHcy normal to mildly elevated**; **no homocystinuria/MMA hallmark** | Often detected by NBS; may be asymptomatic, but severe persistent hypermethioninemia is associated with **white-matter injury, language delay, learning difficulties, demyelination** | **Low-methionine diet**, sometimes **SAMe/ademethionine**; **liver transplantation** reported for refractory severe disease | 2024 retrospective cohort of **15** patients: Ma et al., *BMC Pediatr* 2024, DOI: **10.1186/s12887-024-05196-x** (ma2024hypermethioninemiadueto pages 1-2, ma2024hypermethioninemiadueto pages 6-8, ma2024hypermethioninemiadueto pages 5-6, ma2024hypermethioninemiadueto pages 3-5) |
| Neonatal cobalamin deficiency detected by newborn screening | Not a single causal gene in cited cohort; includes neonatal cobalamin deficiency state identified biochemically | Remethylation / cobalamin-related screening category | Abnormal cobalamin-related profile on NBS; confirmatory assessment uses cobalamin-related metabolites (tHcy/MMA in broader screening algorithms) | Identified in the neonatal period; in the cited cohort, diagnosis occurred at median **23.5 days** and short-term developmental outcome was excellent | **Oral cobalamin supplementation** with discontinuation after stabilization in cohort; monitoring through developmental screening | 2024 multicenter observational NBS outcome study: Reischl-Hajiabadi et al., *J Inherit Metab Dis* 2024, DOI: **10.1002/jimd.12731** (reischl‐hajiabadi2024outcomesafternewborn pages 10-11, reischl‐hajiabadi2024outcomesafternewborn pages 7-8) |


*Table: This table summarizes the major methionine cycle and sulfur amino acid metabolism disorders supported by the gathered evidence, including genes, pathway position, biochemical hallmarks, presentations, treatments, and the most relevant recent studies.*

---

## Notes on evidence gaps for this report
- **Ontology identifiers (MONDO/Orphanet/MeSH/ICD-11) and OMIM records** were not directly retrievable via the available tools; therefore, only identifiers embedded in accessed manuscripts (e.g., OMIM-like numbers in an NBS epidemiology text) and ICD coding commentary from claims-based work are included. (goncalves2024epidemiologyofrare pages 24-27, jain2024estimatingprevalenceof pages 2-3)
- **PMIDs** were not provided in the retrieved evidence snippets; citations are therefore given via DOIs/URLs embedded in the tool-retrieved documents. (kozich2024komrowermemoriallecture pages 1-2, arhip2024lateonsetmethylmalonicacidemia pages 4-5, tang2024newbornscreeningfor pages 1-2)


References

1. (reischl‐hajiabadi2024outcomesafternewborn pages 1-2): Anna T. Reischl‐Hajiabadi, Elena Schnabel, Florian Gleich, Katharina Mengler, Martin Lindner, Peter Burgard, Roland Posset, Svenja Lommer‐Steinhoff, Sarah C. Grünert, Eva Thimm, Peter Freisinger, Julia B. Hennermann, Johannes Krämer, Gwendolyn Gramer, Dominic Lenz, Stine Christ, Friederike Hörster, Georg F. Hoffmann, Sven F. Garbade, Stefan Kölker, and Ulrike Mütze. Outcomes after newborn screening for propionic and methylmalonic acidemia and homocystinurias. Journal of Inherited Metabolic Disease, 47:674-689, Apr 2024. URL: https://doi.org/10.1002/jimd.12731, doi:10.1002/jimd.12731. This article has 18 citations and is from a peer-reviewed journal.

2. (kozich2024komrowermemoriallecture pages 1-2): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

3. (mucha2024vitaminb12metabolism pages 15-15): Patryk Mucha, Filip Kus, Dominik Cysewski, Ryszard Tomasz Smolenski, and Marta Tomczyk. Vitamin b12 metabolism: a network of multi-protein mediated processes. International Journal of Molecular Sciences, Jul 2024. URL: https://doi.org/10.3390/ijms25158021, doi:10.3390/ijms25158021. This article has 51 citations.

4. (ma2024hypermethioninemiadueto pages 1-2): Xue Ma, Mei Lu, Zhehui Chen, Huiting Zhang, Jinqing Song, Hui Dong, Ying Jin, Mengqiu Li, Ruxuan He, Lulu Kang, Yi Liu, Yongxing Chen, Zhijun Zhu, Liying Sun, Yao Zhang, and Yanling Yang. Hypermethioninemia due to methionine adenosyltransferase i/iii deficiency and brain damage. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05196-x, doi:10.1186/s12887-024-05196-x. This article has 2 citations and is from a peer-reviewed journal.

5. (kozich2024komrowermemoriallecture pages 3-4): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

6. (mucha2024vitaminb12metabolism pages 10-11): Patryk Mucha, Filip Kus, Dominik Cysewski, Ryszard Tomasz Smolenski, and Marta Tomczyk. Vitamin b12 metabolism: a network of multi-protein mediated processes. International Journal of Molecular Sciences, Jul 2024. URL: https://doi.org/10.3390/ijms25158021, doi:10.3390/ijms25158021. This article has 51 citations.

7. (arhip2024lateonsetmethylmalonicacidemia pages 1-2): Loredana Arhip, Noemi Brox-Torrecilla, Inmaculada Romero, Marta Motilla, Clara Serrano-Moreno, María Miguélez, and Cristina Cuerda. Late-onset methylmalonic acidemia and homocysteinemia (cblc disease): systematic review. Orphanet Journal of Rare Diseases, Jan 2024. URL: https://doi.org/10.1186/s13023-024-03021-3, doi:10.1186/s13023-024-03021-3. This article has 23 citations and is from a peer-reviewed journal.

8. (mucha2024vitaminb12metabolism pages 9-10): Patryk Mucha, Filip Kus, Dominik Cysewski, Ryszard Tomasz Smolenski, and Marta Tomczyk. Vitamin b12 metabolism: a network of multi-protein mediated processes. International Journal of Molecular Sciences, Jul 2024. URL: https://doi.org/10.3390/ijms25158021, doi:10.3390/ijms25158021. This article has 51 citations.

9. (jain2024estimatingprevalenceof pages 2-3): Mahim Jain, Mehul Shah, Kamlesh M. Thakker, Andrew Rava, Agness Pelts Block, Colette Ndiba-Markey, and Lionel Pinto. Estimating prevalence of classical homocystinuria in the united states using optum's de-identified market clarity data. Molecular Genetics and Metabolism Reports, 40:101101, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101101, doi:10.1016/j.ymgmr.2024.101101. This article has 3 citations.

10. (goncalves2024epidemiologyofrare pages 24-27): MMR Gonçalves. Epidemiology of rare diseases detected by newborn screening. Unknown journal, 2024.

11. (kozich2024komrowermemoriallecture pages 3-3): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

12. (goncalves2024portugueseneonatalscreening pages 6-7): Maria Miguel Gonçalves, Ana Marcão, Carmen Sousa, Célia Nogueira, Helena Fonseca, Hugo Rocha, and Laura Vilarinho. Portuguese neonatal screening program: a cohort study of 18 years using ms/ms. International Journal of Neonatal Screening, 10:25, Mar 2024. URL: https://doi.org/10.3390/ijns10010025, doi:10.3390/ijns10010025. This article has 11 citations.

13. (jain2024estimatingprevalenceof pages 1-2): Mahim Jain, Mehul Shah, Kamlesh M. Thakker, Andrew Rava, Agness Pelts Block, Colette Ndiba-Markey, and Lionel Pinto. Estimating prevalence of classical homocystinuria in the united states using optum's de-identified market clarity data. Molecular Genetics and Metabolism Reports, 40:101101, Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101101, doi:10.1016/j.ymgmr.2024.101101. This article has 3 citations.

14. (mucha2024vitaminb12metabolism pages 7-9): Patryk Mucha, Filip Kus, Dominik Cysewski, Ryszard Tomasz Smolenski, and Marta Tomczyk. Vitamin b12 metabolism: a network of multi-protein mediated processes. International Journal of Molecular Sciences, Jul 2024. URL: https://doi.org/10.3390/ijms25158021, doi:10.3390/ijms25158021. This article has 51 citations.

15. (goncalves2024portugueseneonatalscreening pages 4-6): Maria Miguel Gonçalves, Ana Marcão, Carmen Sousa, Célia Nogueira, Helena Fonseca, Hugo Rocha, and Laura Vilarinho. Portuguese neonatal screening program: a cohort study of 18 years using ms/ms. International Journal of Neonatal Screening, 10:25, Mar 2024. URL: https://doi.org/10.3390/ijns10010025, doi:10.3390/ijns10010025. This article has 11 citations.

16. (kozich2024komrowermemoriallecture pages 13-13): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

17. (arhip2024lateonsetmethylmalonicacidemia pages 4-5): Loredana Arhip, Noemi Brox-Torrecilla, Inmaculada Romero, Marta Motilla, Clara Serrano-Moreno, María Miguélez, and Cristina Cuerda. Late-onset methylmalonic acidemia and homocysteinemia (cblc disease): systematic review. Orphanet Journal of Rare Diseases, Jan 2024. URL: https://doi.org/10.1186/s13023-024-03021-3, doi:10.1186/s13023-024-03021-3. This article has 23 citations and is from a peer-reviewed journal.

18. (ding2023lateonsetcblcdefect pages 2-4): Si Ding, Shiying Ling, Lili Liang, Wenjuan Qiu, Huiwen Zhang, Ting Chen, Xia Zhan, Feng Xu, Xuefan Gu, and Lianshu Han. Late-onset cblc defect: clinical, biochemical and molecular analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02890-4, doi:10.1186/s13023-023-02890-4. This article has 10 citations and is from a peer-reviewed journal.

19. (ding2023lateonsetcblcdefect pages 1-2): Si Ding, Shiying Ling, Lili Liang, Wenjuan Qiu, Huiwen Zhang, Ting Chen, Xia Zhan, Feng Xu, Xuefan Gu, and Lianshu Han. Late-onset cblc defect: clinical, biochemical and molecular analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02890-4, doi:10.1186/s13023-023-02890-4. This article has 10 citations and is from a peer-reviewed journal.

20. (ma2024hypermethioninemiadueto pages 5-6): Xue Ma, Mei Lu, Zhehui Chen, Huiting Zhang, Jinqing Song, Hui Dong, Ying Jin, Mengqiu Li, Ruxuan He, Lulu Kang, Yi Liu, Yongxing Chen, Zhijun Zhu, Liying Sun, Yao Zhang, and Yanling Yang. Hypermethioninemia due to methionine adenosyltransferase i/iii deficiency and brain damage. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05196-x, doi:10.1186/s12887-024-05196-x. This article has 2 citations and is from a peer-reviewed journal.

21. (wu2024variablephenotypesand pages 1-2): Sheng-Nan Wu, Hui-Shu E, Yue Yu, Shi-Ying Ling, Li-Li Liang, Wen-Juan Qiu, Hui-Wen Zhang, Rui-Xue Shuai, Hai-Yan Wei, Chi-Ju Yang, Peng Xu, Xi-Gui Chen, Hui Zou, Ji-Zhen Feng, Ting-Ting Niu, Hai-Li Hu, Kai-Chuang Zhang, De-Yun Lu, Zhu-Wen Gong, Xia Zhan, Wen-Jun Ji, Xue-Fan Gu, Yong-Xing Chen, and Lian-Shu Han. Variable phenotypes and outcomes associated with the mmachc c.482g > a mutation: follow-up in a large cblc disease cohort. World Journal of Pediatrics, 20:848-858, Dec 2024. URL: https://doi.org/10.1007/s12519-023-00770-2, doi:10.1007/s12519-023-00770-2. This article has 9 citations and is from a peer-reviewed journal.

22. (goncalves2024epidemiologyofrare pages 50-52): MMR Gonçalves. Epidemiology of rare diseases detected by newborn screening. Unknown journal, 2024.

23. (kozich2024komrowermemoriallecture pages 16-17): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

24. (ma2024hypermethioninemiadueto pages 6-8): Xue Ma, Mei Lu, Zhehui Chen, Huiting Zhang, Jinqing Song, Hui Dong, Ying Jin, Mengqiu Li, Ruxuan He, Lulu Kang, Yi Liu, Yongxing Chen, Zhijun Zhu, Liying Sun, Yao Zhang, and Yanling Yang. Hypermethioninemia due to methionine adenosyltransferase i/iii deficiency and brain damage. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05196-x, doi:10.1186/s12887-024-05196-x. This article has 2 citations and is from a peer-reviewed journal.

25. (kozich2024komrowermemoriallecture media e1534ecc): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

26. (ma2024hypermethioninemiadueto pages 8-8): Xue Ma, Mei Lu, Zhehui Chen, Huiting Zhang, Jinqing Song, Hui Dong, Ying Jin, Mengqiu Li, Ruxuan He, Lulu Kang, Yi Liu, Yongxing Chen, Zhijun Zhu, Liying Sun, Yao Zhang, and Yanling Yang. Hypermethioninemia due to methionine adenosyltransferase i/iii deficiency and brain damage. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05196-x, doi:10.1186/s12887-024-05196-x. This article has 2 citations and is from a peer-reviewed journal.

27. (reischl‐hajiabadi2024outcomesafternewborn pages 13-13): Anna T. Reischl‐Hajiabadi, Elena Schnabel, Florian Gleich, Katharina Mengler, Martin Lindner, Peter Burgard, Roland Posset, Svenja Lommer‐Steinhoff, Sarah C. Grünert, Eva Thimm, Peter Freisinger, Julia B. Hennermann, Johannes Krämer, Gwendolyn Gramer, Dominic Lenz, Stine Christ, Friederike Hörster, Georg F. Hoffmann, Sven F. Garbade, Stefan Kölker, and Ulrike Mütze. Outcomes after newborn screening for propionic and methylmalonic acidemia and homocystinurias. Journal of Inherited Metabolic Disease, 47:674-689, Apr 2024. URL: https://doi.org/10.1002/jimd.12731, doi:10.1002/jimd.12731. This article has 18 citations and is from a peer-reviewed journal.

28. (belaramani2024expandednewbornscreening pages 1-2): Kiran Moti Belaramani, Toby Chun Hei Chan, Edgar Wai Lok Hau, Matthew Chun Wing Yeung, Anne Mei Kwun Kwok, Ivan Fai Man Lo, Terry Hiu Fung Law, Helen Wu, Sheila Suet Na Wong, Shirley Wai Lam, Gladys Ha Yin Ha, Toby Pui Yee Lau, Tsz Ki Wong, Venus Wai Ching Or, Rosanna Ming Sum Wong, Wong Lap Ming, Jasmine Chi Kwan Chow, Eric Kin Cheong Yau, Antony Fu, Josephine Shuk Ching Chong, Ho Chung Yau, Grace Wing Kit Poon, Kwok Leung Ng, Kwong Tat Chan, Yuen Yu Lam, Joannie Hui, Chloe Miu Mak, and Cheuk Wing Fung. Expanded newborn screening for inborn errors of metabolism in hong kong: results and outcome of a 7 year journey. International Journal of Neonatal Screening, 10:23, Mar 2024. URL: https://doi.org/10.3390/ijns10010023, doi:10.3390/ijns10010023. This article has 10 citations.

29. (tang2024newbornscreeningfor pages 1-2): Chengfang Tang, Lixin Li, Ting Chen, Yulin Li, Bo Zhu, Yinhong Zhang, Yifan Yin, Xiulian Liu, Cidan Huang, Jingkun Miao, Baosheng Zhu, Xiaohua Wang, Hui Zou, Lianshu Han, Jizhen Feng, and Yonglan Huang. Newborn screening for inborn errors of metabolism by next-generation sequencing combined with tandem mass spectrometry. International Journal of Neonatal Screening, 10:28, Mar 2024. URL: https://doi.org/10.3390/ijns10020028, doi:10.3390/ijns10020028. This article has 22 citations.

30. (goncalves2024epidemiologyofrare pages 30-33): MMR Gonçalves. Epidemiology of rare diseases detected by newborn screening. Unknown journal, 2024.

31. (reischl‐hajiabadi2024outcomesafternewborn pages 10-11): Anna T. Reischl‐Hajiabadi, Elena Schnabel, Florian Gleich, Katharina Mengler, Martin Lindner, Peter Burgard, Roland Posset, Svenja Lommer‐Steinhoff, Sarah C. Grünert, Eva Thimm, Peter Freisinger, Julia B. Hennermann, Johannes Krämer, Gwendolyn Gramer, Dominic Lenz, Stine Christ, Friederike Hörster, Georg F. Hoffmann, Sven F. Garbade, Stefan Kölker, and Ulrike Mütze. Outcomes after newborn screening for propionic and methylmalonic acidemia and homocystinurias. Journal of Inherited Metabolic Disease, 47:674-689, Apr 2024. URL: https://doi.org/10.1002/jimd.12731, doi:10.1002/jimd.12731. This article has 18 citations and is from a peer-reviewed journal.

32. (kozich2024komrowermemoriallecture pages 7-8): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

33. (mathew2024vitaminb12deficiency pages 10-11): Aimee Rachel Mathew, Giacomo Di Matteo, Piergiorgio La Rosa, Saviana Antonella Barbati, Luisa Mannina, Sandra Moreno, Ada Maria Tata, Virve Cavallucci, and Marco Fidaleo. Vitamin b12 deficiency and the nervous system: beyond metabolic decompensation—comparing biological models and gaining new insights into molecular and cellular mechanisms. International Journal of Molecular Sciences, 25:590, Jan 2024. URL: https://doi.org/10.3390/ijms25010590, doi:10.3390/ijms25010590. This article has 102 citations.

34. (kozich2024komrowermemoriallecture pages 7-7): Viktor Kožich and Tomas Majtan. Komrower memorial lecture 2023. molecular basis of phenotype expression in homocystinuria: where are we 30 years later? Journal of Inherited Metabolic Disease, 47:841-859, Jun 2024. URL: https://doi.org/10.1002/jimd.12767, doi:10.1002/jimd.12767. This article has 6 citations and is from a peer-reviewed journal.

35. (ma2024hypermethioninemiadueto pages 3-5): Xue Ma, Mei Lu, Zhehui Chen, Huiting Zhang, Jinqing Song, Hui Dong, Ying Jin, Mengqiu Li, Ruxuan He, Lulu Kang, Yi Liu, Yongxing Chen, Zhijun Zhu, Liying Sun, Yao Zhang, and Yanling Yang. Hypermethioninemia due to methionine adenosyltransferase i/iii deficiency and brain damage. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05196-x, doi:10.1186/s12887-024-05196-x. This article has 2 citations and is from a peer-reviewed journal.

36. (reischl‐hajiabadi2024outcomesafternewborn pages 7-8): Anna T. Reischl‐Hajiabadi, Elena Schnabel, Florian Gleich, Katharina Mengler, Martin Lindner, Peter Burgard, Roland Posset, Svenja Lommer‐Steinhoff, Sarah C. Grünert, Eva Thimm, Peter Freisinger, Julia B. Hennermann, Johannes Krämer, Gwendolyn Gramer, Dominic Lenz, Stine Christ, Friederike Hörster, Georg F. Hoffmann, Sven F. Garbade, Stefan Kölker, and Ulrike Mütze. Outcomes after newborn screening for propionic and methylmalonic acidemia and homocystinurias. Journal of Inherited Metabolic Disease, 47:674-689, Apr 2024. URL: https://doi.org/10.1002/jimd.12731, doi:10.1002/jimd.12731. This article has 18 citations and is from a peer-reviewed journal.