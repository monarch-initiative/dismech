---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:27:31.680613'
end_time: '2026-04-05T20:42:05.790540'
duration_seconds: 874.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Myeloid Leukemia, NPM1-Mutated
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Myeloid Leukemia, NPM1-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, NPM1-Mutated** covering all of the
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
- **Disease Name:** Acute Myeloid Leukemia, NPM1-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, NPM1-Mutated** covering all of the
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


## Acute Myeloid Leukemia (AML), *NPM1*-Mutated — Disease Characteristics Research Report

### Target disease
- **Disease name:** Acute myeloid leukemia with mutated *NPM1* (NPM1-mutated AML)
- **MONDO ID:** Not retrieved from the available evidence in this run (MONDO mapping should be added from Mondo/OLS in a follow-up curation step).
- **Category:** Hematologic malignancy (acute leukemia)

This report synthesizes **aggregated disease-level evidence** from peer‑reviewed reviews, prospective trials, and real‑world cohorts; plus **trial registry records** from ClinicalTrials.gov.

---

## 1. Disease Information

### 1.1 Concise overview
*NPM1*-mutated AML is a genetically defined AML subtype characterized by somatic mutations in *NPM1* that produce an aberrantly **cytoplasmic** nucleophosmin protein (“NPM1c”), and it is the **largest molecular subgroup of adult AML**. (falini2024criteriafordiagnosis pages 1-2)

**Current classification concept:** recent WHO/ICC schemes treat *NPM1* mutation as **AML‑defining**, with differences in blast thresholds (see below). (patel2024npm1mutatedacutemyeloid pages 1-2, falini2024criteriafordiagnosis pages 5-6, shimony2023acutemyeloidleukemia pages 5-6)

### 1.2 Common synonyms / alternative names
- “AML with mutated *NPM1*”
- “NPM1-mutated AML”, “NPM1mut AML”, “NPM1+ AML” (falini2024criteriafordiagnosis pages 1-2)

### 1.3 Key identifiers (available from retrieved sources)
- **WHO/ICC entity:** AML with mutated *NPM1* (AML defined by genetic abnormality) (falini2024criteriafordiagnosis pages 5-6, shimony2023acutemyeloidleukemia pages 5-6)
- **Risk stratification:** ELN 2022 incorporates *NPM1* and *FLT3* testing as mandatory for genetic risk stratification. (falini2024criteriafordiagnosis pages 1-2)

**Not retrieved in this run:** OMIM, Orphanet, MeSH, ICD-10/ICD-11, and a disease-specific MONDO identifier for “NPM1-mutated AML”.

### 1.4 Classification details (WHO 2022 vs ICC 2022; ELN 2022)
- **Blast threshold (WHO 5th edition / WHO 2022):** WHO permits diagnosing NPM1‑mutated AML **irrespective of blast percentage** (WHO “AML defined by genetic abnormalities” does not specify a blast cut-off). (falini2024criteriafordiagnosis pages 5-6, shimony2023acutemyeloidleukemia pages 5-6)
- **Blast threshold (ICC 2022):** ICC requires **≥10% blasts** for AML with recurrent genetic abnormalities, including *NPM1*-mutated AML. (falini2024criteriafordiagnosis pages 5-6, shimony2023acutemyeloidleukemia pages 5-6)
- **ELN 2022 genetic risk rules relevant to *NPM1*:**
  - *NPM1* mutation **without *FLT3*-ITD** → **favorable risk**. (falini2024criteriafordiagnosis pages 5-6)
  - *NPM1* mutation **with *FLT3*-ITD** → **intermediate risk regardless of *FLT3*-ITD allelic ratio**. (falini2024criteriafordiagnosis pages 5-6, sargas2023comparisonofthe pages 1-2, lachowiez2023comparisonandvalidation pages 1-2)
  - Adverse cytogenetics can override; “*NPM1* mutated AML with adverse cytogenetic abnormalities will be classified as adverse risk.” (shimony2023acutemyeloidleukemia pages 5-6)

| Key point | Value | Source (first author, year) | URL/DOI | Publication date |
|---|---|---|---|---|
| Disease name | Acute myeloid leukemia with mutated NPM1; also written as NPM1-mutated AML | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| Common synonyms | AML with mutated NPM1; NPM1-mutated AML; NPM1mut AML; NPM1+ AML | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| Classification source | WHO 5th edition (2022) recognizes AML with mutated NPM1 as an AML-defining genetic abnormality/distinct entity | Patel, 2024 (patel2024npm1mutatedacutemyeloid pages 1-2, patel2024npm1mutatedacutemyeloid pages 4-4) | https://doi.org/10.1159/000530253 | 2024-03 |
| Classification source | ICC 2022 recognizes NPM1-mutated AML as a distinct recurrent-genetic-abnormality category | Sharma, 2023 (sharma2023npm1mutations pages 1-2); Shimony, 2023 (shimony2023acutemyeloidleukemia pages 5-6) | https://doi.org/10.3390/cancers15041177; https://doi.org/10.1002/ajh.26822 | 2023-02; 2023-01 |
| Classification source | ELN 2022 requires NPM1 and FLT3 status for genetic risk stratification | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2, falini2024criteriafordiagnosis pages 5-6) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| Blast-count threshold (WHO 5th ed.) | WHO 5th edition permits diagnosis of NPM1-mutated AML irrespective of blast percentage / no blast threshold for AML defined by genetic abnormalities | Falini, 2024 (falini2024criteriafordiagnosis pages 5-6); Shimony, 2023 (shimony2023acutemyeloidleukemia pages 5-6) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1002/ajh.26822 | 2024-12; 2023-01 |
| Blast-count threshold (ICC 2022) | ICC 2022 requires ≥10% blasts for AML with mutated NPM1 | Falini, 2024 (falini2024criteriafordiagnosis pages 5-6); Patel, 2024 (patel2024npm1mutatedacutemyeloid pages 4-4) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1159/000530253 | 2024-12; 2024-03 |
| ELN 2022 risk group: NPM1-mutated, FLT3-ITD negative | Favorable risk | Falini, 2024 (falini2024criteriafordiagnosis pages 5-6) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| ELN 2022 risk group: NPM1-mutated with FLT3-ITD | Intermediate risk regardless of FLT3-ITD allelic ratio | Falini, 2024 (falini2024criteriafordiagnosis pages 5-6); Sargas, 2023 (sargas2023comparisonofthe pages 1-2); Lachowiez, 2023 (lachowiez2023comparisonandvalidation pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1038/s41408-023-00835-5; https://doi.org/10.1182/bloodadvances.2022009010 | 2024-12; 2023-05; 2023-05 |
| ELN 2022 adverse override | NPM1-mutated AML with adverse cytogenetic abnormalities is classified as adverse risk | Shimony, 2023 (shimony2023acutemyeloidleukemia pages 5-6); Mrózek, 2023 (mrozek2023outcomepredictionby pages 1-2) | https://doi.org/10.1002/ajh.26822; https://doi.org/10.1038/s41375-023-01846-8 | 2023-01; 2023-02 |
| ELN/MDS-related mutation note | WHO/ICC prioritize NPM1 mutation over myelodysplasia-related mutations when co-occurring; ELN discussion suggests MR mutations should not automatically overrule favorable NPM1 biology | Falini, 2024 (falini2024criteriafordiagnosis pages 5-6) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| Epidemiology: adult AML frequency | NPM1 mutations occur in ~30–35% of adult AML / about one-third of adult AML | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2); Patel, 2024 (patel2024npm1mutatedacutemyeloid pages 1-2); Sharma, 2023 (sharma2023npm1mutations pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1159/000530253; https://doi.org/10.3390/cancers15041177 | 2024-12; 2024-03; 2023-02 |
| Epidemiology: normal-karyotype AML | NPM1 mutations are present in ~50–60% of normal-karyotype AML; Patel also notes ~60% of normal-karyotype AML | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2); Patel, 2024 (patel2024npm1mutatedacutemyeloid pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1159/000530253 | 2024-12; 2024-03 |
| Epidemiology: pediatric AML | Less frequent in children, about 2–8% | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144 | 2024-12 |
| Typical associated clinicopathologic features | Often normal karyotype, myelomonocytic/monocytic differentiation, low/absent CD34, frequent extramedullary involvement | Falini, 2024 (falini2024criteriafordiagnosis pages 1-2); Patel, 2024 (patel2024npm1mutatedacutemyeloid pages 1-2) | https://doi.org/10.1158/2643-3230.bcd-23-0144; https://doi.org/10.1159/000530253 | 2024-12; 2024-03 |


*Table: This table summarizes the current naming, classification framework, blast-threshold differences, and headline epidemiology figures for acute myeloid leukemia with mutated NPM1. It is useful for quickly aligning WHO 2022, ICC 2022, and ELN 2022 terminology and risk-stratification rules.*

---

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
- The defining lesion is a **somatic** *NPM1* mutation, usually an exon 12 frameshift insertion affecting the C‑terminus; this creates **aberrant cytoplasmic localization** of mutant nucleophosmin (NPM1c). (patel2024npm1mutatedacutemyeloid pages 1-2, chin2023targetingandmonitoring pages 1-2)
- Mechanistically, *NPM1*-mutated AML depends on a characteristic transcriptional program with **HOX/MEIS1 overexpression** linked to NPM1c biology. (patel2024npm1mutatedacutemyeloid pages 1-2, falini2024criteriafordiagnosis pages 1-2)

### 2.2 Risk factors
**Genetic (somatic co-mutations / disease biology modifiers)**
- Co-mutations are common and clinically important; across cohorts, recurrent co-mutations include *FLT3* (especially *FLT3*-ITD), *DNMT3A*, *WT1*, and others, with prognostic impact (see Prognosis). (othman2024molecularclinicaland pages 1-5)

**Environmental / iatrogenic**
- Therapy-related AML (t‑AML) can carry *NPM1* mutations. A diagnostic-focused review notes that therapy-related NPM1‑mutated AML comprises **≈15% of therapy-related AMLs** and, if *FLT3*-ITD negative, is considered ELN favorable with post‑remission decisions guided by MRD. (falini2024criteriafordiagnosis pages 5-6)

### 2.3 Protective factors
No specific protective (genetic or environmental) factors were retrieved in the cited evidence for the *NPM1*-mutated AML subtype.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to *NPM1*-mutated AML was retrieved in this run.

---

## 3. Phenotypes

### 3.1 Core clinical and pathologic phenotype (with selected frequencies)
Common presentation overlaps with AML generally (cytopenias, infections, bleeding), but *NPM1*-mutated AML has recurrent clinicopathologic patterns:
- **Bone marrow:** typically **markedly hypercellular**. (falini2024criteriafordiagnosis pages 1-2)
- **Differentiation:** often **myelomonocytic/monocytic** (FAB M4/M5 predominance; other FAB categories can occur). (falini2024criteriafordiagnosis pages 1-2)
- **Immunophenotype:** typically **no/low CD34 expression**; a 2024 cohort paper states “the vast majority of NPM1m AML cases are therefore CD34‑negative”. (falini2024criteriafordiagnosis pages 1-2, papadopoulou2024characteristicsandprognosis pages 1-2)
- **Extramedullary disease:** commonly reported, particularly **skin involvement**, and IHC can help detect such involvement. (falini2024criteriafordiagnosis pages 1-2)
- **Demographics:** “female predominance” is noted in diagnostic reviews. (falini2024criteriafordiagnosis pages 1-2)

### 3.2 “APL-like” phenotype subset
A subset of NPM1‑mutated AML may show a “double negative” **CD34−/HLA‑DR−** immunophenotype that can mimic acute promyelocytic leukemia (APL) at presentation, necessitating rapid exclusion of PML::RARA rearrangement. (papadopoulou2024characteristicsandprognosis pages 1-2)

### 3.3 Suggested HPO terms (non-exhaustive; for knowledge-base tagging)
These are ontology suggestions (not direct extractions from a single cited ontology resource in this run):
- **Anemia** (HP:0001903)
- **Thrombocytopenia** (HP:0001873)
- **Leukocytosis** (HP:0001974)
- **Neutropenia** (HP:0001875)
- **Recurrent infections** (HP:0002719)
- **Abnormal bleeding** (HP:0001892)
- **Bone marrow hypercellularity** (commonly mapped to marrow hypercellularity concepts; exact HPO mapping requires ontology lookup)
- **Extramedullary hematopoiesis / myeloid sarcoma** (ontology mapping requires curation)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Primary causal/defining gene:** *NPM1* (nucleophosmin 1). (falini2024criteriafordiagnosis pages 1-2)

### 4.2 Pathogenic variant spectrum (high-level)
- Variants are typically small insertions causing a C‑terminal frameshift and acquisition of a nuclear export signal, producing NPM1c. (chin2023targetingandmonitoring pages 1-2)
- Common mutation “types” (A/B/D) are described as exon‑12 insertion variants; one review provides approximate distribution: Type A ~72%, Type B ~12%, Type D ~4%. (chin2023targetingandmonitoring pages 1-2)

**Somatic vs germline:** the defining *NPM1* lesion is described as **somatic** in AML series/reviews. (patel2024npm1mutatedacutemyeloid pages 1-2)

**Population allele frequencies:** not retrieved (these are somatic leukemia variants and are generally absent from germline population databases).

### 4.3 Co-mutations as molecular modifiers (selected)
In a large prospective trial cohort (NCRI AML17/AML19; n=1357), independent adverse baseline associations for overall survival included: *FLT3*-ITD (HR 1.28), *DNMT3A* (HR 1.65), *WT1* (HR 1.74), and non‑ABD *NPM1* mutations (HR 1.64). (othman2024molecularclinicaland pages 1-5)

### 4.4 Chromosomal abnormalities
*NPM1*-mutated AML is enriched in **normal karyotype AML** (a large fraction of NK-AML cases). (patel2024npm1mutatedacutemyeloid pages 1-2, falini2024criteriafordiagnosis pages 1-2)

### 4.5 Epigenetic / chromatin-level regulation (2023–2024 primary data)
Recent mechanistic work supports *NPM1* mutation as a **chromatin-associated neomorphic driver** of the HOX program, including cooperation with KMT2A/MLL1 and maintenance of active chromatin at HOX loci. (patel2024npm1mutatedacutemyeloid pages 3-4)

A 2023 primary study additionally links *NPM1C+* to **3D genome architecture** changes (CTCF/TAD remodeling) that strengthen TADs at HOXA/B and PBX3 loci and weaken TADs at cell-cycle inhibitor loci (e.g., *Cdkn1a/p21*), supporting proliferation and differentiation block. (lai2023npm1mutationreprograms pages 1-3)

---

## 5. Mechanism / Pathophysiology

### 5.1 Causal chain (conceptual)
1. **Somatic *NPM1* frameshift mutation** creates a C‑terminal neo‑sequence with nuclear export features →
2. **Mutant NPM1 (NPM1c) mislocalizes to cytoplasm** in an **XPO1/exportin-1 dependent** manner →
3. NPM1c engages nuclear/chromatin programs (and may mislocalize other factors), maintaining an abnormal transcriptional state →
4. **HOX/MEIS1 transcriptional program is enforced**, supporting self-renewal / differentiation arrest →
5. **Myeloid differentiation block and clonal expansion** manifest clinically as AML with characteristic monocytic/myelomonocytic phenotypes. (patel2024npm1mutatedacutemyeloid pages 1-2, falini2024criteriafordiagnosis pages 1-2, lai2023npm1mutationreprograms pages 1-3)

### 5.2 Pathways and cellular processes (selected)
- **HOX/MEIS1 axis / menin–KMT2A dependency:** NPM1-mutated cells rely on overexpression of HOX/MEIS1, which provides rationale for menin inhibitors. (patel2024npm1mutatedacutemyeloid pages 1-2, falini2024criteriafordiagnosis pages 1-2)
- **Nuclear export (XPO1/CRM1):** NPM1c localization depends on XPO1; inhibition can relocalize NPM1c and promote differentiation. (patel2024npm1mutatedacutemyeloid pages 8-9)
- **3D genome organization (CTCF/TADs):** NPM1C+ can reshape CTCF-defined TAD topology, linking mutation to chromatin architecture and HOX activation. (lai2023npm1mutationreprograms pages 1-3)

### 5.3 Suggested GO and CL terms (for annotation; requires ontology validation)
- **GO Biological Process (suggestions):**
  - hematopoietic cell differentiation
  - myeloid cell differentiation
  - regulation of transcription by RNA polymerase II
  - chromatin organization / regulation of chromatin architecture
  - nuclear export
- **Cell Ontology (CL) (suggestions):**
  - hematopoietic stem cell
  - myeloid progenitor cell
  - monocyte
  - myeloblast

---

## 6. Anatomical Structures Affected

**Primary site:** bone marrow hematopoietic tissue. (falini2024criteriafordiagnosis pages 1-2)

**Peripheral blood involvement:** circulating blasts/leukocytosis can occur, especially with RAS/*FLT3* co-mutations. (falini2024criteriafordiagnosis pages 1-2)

**Extramedullary involvement:** skin and other sites (myeloid sarcoma) may be involved; mutant NPM1 IHC can support identification. (falini2024criteriafordiagnosis pages 1-2, patel2024npm1mutatedacutemyeloid pages 2-3)

**Suggested UBERON terms (requires ontology lookup):** bone marrow; blood; skin.

---

## 7. Temporal Development

- **Typical onset:** adult-onset AML; NPM1 mutations are common in adults and less common in children (2–8%). (falini2024criteriafordiagnosis pages 1-2)
- **Course:** acute presentation; relapse risk remains substantial even in this generally favorable subtype, motivating MRD monitoring and risk-adapted post-remission therapy. (othman2024molecularclinicaland pages 1-5, othman2024molecularmrdis pages 1-2)

---

## 8. Inheritance and Population

### 8.1 Epidemiology (mutation frequency within AML)
- *NPM1* mutations occur in **~30–35% of adult AML** and **50–60% of normal-karyotype AML**; they are **less frequent in children (2–8%)**. (falini2024criteriafordiagnosis pages 1-2)

### 8.2 Inheritance
- The defining lesion is somatic; a Mendelian inheritance pattern is not applicable to the AML entity itself in most cases. (patel2024npm1mutatedacutemyeloid pages 1-2)

---

## 9. Diagnostics

### 9.1 Recommended core molecular testing
- Determination of *NPM1* and *FLT3* mutational status is “a mandatory step” for ELN 2022 genetic risk stratification. (falini2024criteriafordiagnosis pages 1-2)

### 9.2 Diagnostic modalities
- **Molecular techniques** (e.g., sequencing-based detection) and **immunohistochemistry** for cytoplasmic NPM1c can be combined to solve difficult diagnostic problems (including certain atypical mutations). (falini2024criteriafordiagnosis pages 1-2)
- **Flow cytometry:** useful for immunophenotyping, but multiparameter flow MRD may be challenging to interpret in this subtype. (patel2024npm1mutatedacutemyeloid pages 1-2)

### 9.3 MRD monitoring (NPM1 as an MRD marker)
NPM1 mutant transcript burden closely tracks disease status and is suited to high-sensitivity MRD monitoring. (patel2024npm1mutatedacutemyeloid pages 1-2)

A key 2024 real-world analysis (venetoclax-based, nonintensive therapy) reported:
- **BM MRD negativity** 25% by cycle 2; 47% by cycle 4; 50% by cycle 6. (othman2024molecularmrdis pages 1-2)
- **2-year OS** 84% if MRD-negative by cycle 4 vs 46% if MRD-positive. (othman2024molecularmrdis pages 1-2)

**Direct abstract quote (MRD utility):** “A total of 44 patients (58%) achieved bone marrow (BM) MRD negativity…” and “Patients achieving BM MRD negativity by the end of cycle 4 had 2-year overall of 84% compared with 46% if MRD was positive.” (othman2024molecularmrdis pages 1-2)

### 9.4 Visual evidence: MRD-based monitoring/decision algorithm
An MRD monitoring algorithm for intensive chemotherapy (including management of “MRD relapse”) is provided in Figure 4 of Falini & Dillon 2024. (falini2024criteriafordiagnosis media 3d972561)

---

## 10. Outcome / Prognosis

### 10.1 Baseline prognostic factors (intensively treated cohorts)
In a large prospective analysis of *NPM1*-mutated AML (NCRI AML17/AML19; n=1357), independent adverse factors for overall survival included *FLT3*-ITD, *DNMT3A*, *WT1*, and non‑ABD *NPM1* mutation classes, and these were strongly associated with MRD positivity. (othman2024molecularclinicaland pages 1-5)

### 10.2 Response depth (MRD) as a major determinant
- Post-induction MRD negativity is emphasized as a major outcome determinant in *NPM1*-mutated AML, and MRD integration can guide post-remission therapy decisions including transplant. (falini2024criteriafordiagnosis pages 1-2, othman2024molecularclinicaland pages 1-5)
- In venetoclax-based nonintensive therapy, RT‑qPCR MRD negativity was the strongest prognostic factor in multivariable analysis and identified a subgroup with very favorable 2‑year OS (84%). (othman2024molecularmrdis pages 1-2)

---

## 11. Treatment

### 11.1 Standard-of-care frameworks (context)
- Standard AML backbones (intensive induction, consolidation, and/or allogeneic HSCT depending on risk/MRD) remain foundational; venetoclax + hypomethylating agent (HMA) or low-dose cytarabine (LDAC) are widely used in older/unfit patients and show high efficacy in *NPM1*-mutated disease. (shukla2024molecularfeaturesand pages 5-6, othman2024molecularmrdis pages 1-2)

### 11.2 MRD-directed and relapse-preemptive strategies (2024)
The prospective VALDAC phase II study demonstrates a real-world implementation of treating **molecular MRD relapse** or **oligoblastic relapse** with venetoclax+LDAC, with mutant *NPM1* comprising 77% of MRD markers and MRD-negative remission achieved in 46% by cycle 2 in the MRD cohort. (tiong2024targetingmolecularmeasurable pages 1-2)

**Direct abstract quote (VALDAC):** “By cycle 2 in the MRD relapse cohort, a log10 reduction in MRD was observed in 69%; 46% achieved MRD negative remission.” (tiong2024targetingmolecularmeasurable pages 1-2)

### 11.3 Targeted therapy: Menin inhibitors (revumenib; emerging class)
A seminal first-in-human trial established menin inhibition as an actionable strategy in susceptible leukemias (including NPM1-mutant):

**Direct abstract quote (Nature 2023):** “therapy with revumenib was associated with a low frequency of grade 3 or higher treatment-related adverse events and a 30% rate of complete remission or complete remission with partial haematologic recovery (CR/CRh)… Asymptomatic prolongation of the QT interval… was identified as the only dose-limiting toxicity.” (issa2023themenininhibitor pages 1-2)

Quantitatively, in 60 evaluable patients with KMT2A-rearranged or NPM1-mutant disease, ORR was 53%, CR/CRh 30%, and MRD negativity among CR/CRh was 78%. (issa2023themenininhibitor pages 4-4)

### 11.4 Current applications / late-stage clinical development (Phase 3)
Multiple Phase 3 programs are actively evaluating adding menin inhibitors to standard regimens in newly diagnosed genetically selected AML:
- **Revumenib + intensive chemotherapy vs placebo** (newly diagnosed NPM1-mutated AML): NCT07211958; Phase 3; estimated n=468; primary endpoints include event-free survival and MRD CR rate. (NCT07211958 chunk 1)
- **Revumenib + azacitidine + venetoclax vs placebo** (newly diagnosed NPM1-mutated or KMT2A-rearranged AML, intensive-ineligible): NCT06652438; Phase 3; estimated n≈415. (NCT06652438 chunk 1)
- **Ziftomenib + (venetoclax+azacitidine) or + (7+3) vs placebo** in untreated NPM1-mutated/KMT2A-rearranged AML: NCT07007312; Phase 3; estimated n=1300. (NCT07007312 chunk 1)

| Intervention/setting | Key outcomes/statistics | Safety notes | Evidence type | Source (first author, journal, year) | Publication date | URL/DOI or ClinicalTrials.gov URL | Notes |
|---|---|---|---|---|---|---|---|
| Venetoclax + HMA or LDAC in previously untreated NPM1-mutated AML achieving CR/CRi; molecular MRD by RT-qPCR | Bone marrow MRD negativity: 25% by end of cycle 2, 47% by end of cycle 4, 50% by end of cycle 6; best MRD-negative response 58%; additional 18% achieved >=4 log10 reduction; 2-year OS 84% if BM MRD-negative by cycle 4 vs 46% if MRD-positive; 22 patients who stopped therapy in BM MRD-negative remission after median 8 cycles had 2-year treatment-free remission 88% (othman2024molecularmrdis pages 1-2, othman2024molecularmrdis pages 7-8, othman2024molecularmrdis pages 5-6) | MRD status, not a drug-specific new toxicity signal, was the dominant prognostic discriminator in this real-world cohort; PB MRD less sensitive than BM MRD (othman2024molecularmrdis pages 7-8) | Human clinical; international real-world cohort | Othman, *Blood*, 2024 | 2024-01 | https://doi.org/10.1182/blood.2023021579 | Strong contemporary evidence for MRD-guided management in venetoclax-based nonintensive therapy for NPM1-mutated AML (othman2024molecularmrdis pages 1-2, othman2024molecularmrdis pages 5-6) |
| VALDAC: venetoclax + low-dose cytarabine for first molecular MRD relapse or oligoblastic relapse in AML; mutant NPM1 represented 77% of MRD markers | In MRD-relapse cohort, by cycle 2: >=1 log10 MRD reduction in 69%, MRD-negative remission in 46%; in oligoblastic relapse cohort, CR/CRh/CRi 73%; estimated 2-year OS 67% in MRD cohort and 53% in oligoblastic cohort; 44% proceeded to HCT (tiong2024targetingmolecularmeasurable pages 1-2) | Oligoblastic relapse cohort had more grade >=3 anemia (32% vs 4%) and infections (36% vs 8%); grade 4 neutropenia 32% and thrombocytopenia 27% in oligoblastic cohort (tiong2024targetingmolecularmeasurable pages 1-2) | Human clinical; prospective phase II | Tiong, *J Clin Oncol*, 2024 | 2024-06 | https://doi.org/10.1200/JCO.23.01599 | Demonstrates a real-world actionable use of molecular relapse detection, often driven by NPM1 RT-qPCR monitoring (tiong2024targetingmolecularmeasurable pages 1-2) |
| Revumenib (SNDX-5613), AUGMENT-101, relapsed/refractory KMT2A-rearranged or NPM1-mutant acute leukemia | In 60 evaluable patients: ORR 53% (32/60); CR/CRh 30% (18/60), including CR 20% and CRh 10%; MRD-negative rate among CR/CRh 78% (14/18); median time to CR/CRh about 1.9 months; median duration of response 9.1 months; median OS 7 months (issa2023themenininhibitor pages 1-2, issa2023themenininhibitor pages 4-4) | Dose-limiting toxicity: asymptomatic QT prolongation; any-grade TEAEs 98.5%, TRAEs 77.9%; differentiation syndrome in 11 patients (16.2%); common AEs included nausea and vomiting (issa2023themenininhibitor pages 1-2) | Human clinical; first-in-human phase I/II | Issa, *Nature*, 2023 | 2023-03 | https://doi.org/10.1038/s41586-023-05812-3 | Foundational proof-of-concept for menin inhibition in NPM1-mutant leukemia; included 14 NPM1-mutant patients in the enrolled population (issa2023themenininhibitor pages 1-2, issa2023themenininhibitor pages 4-4) |
| Revumenib + intensive chemotherapy in newly diagnosed NPM1-mutated AML | Phase 3, randomized, double-blind, placebo-controlled; estimated enrollment 468; compares revumenib + cytarabine/daunorubicin intensive chemotherapy vs placebo + intensive chemotherapy; primary endpoints include event-free survival and MRD complete remission rate (NCT07211958 chunk 1) | Key exclusions include significant QTc prolongation, active CNS disease, GI absorption issues, pregnancy/nursing, active viral infections with detectable viral load (NCT07211958 chunk 1) | Interventional trial; ongoing Phase 3 | ClinicalTrials.gov NCT07211958 | 2025 record | https://clinicaltrials.gov/study/NCT07211958 | Newly diagnosed, previously untreated AML with NPM1 mutation; minimum age 12 years; candidates for intensive chemotherapy (NCT07211958 chunk 1) |
| Revumenib + azacitidine + venetoclax in newly diagnosed NPM1-mutated or KMT2A-rearranged AML ineligible for intensive chemotherapy | Phase 3, randomized, double-blind, placebo-controlled; estimated enrollment ~415; revumenib or placebo added day 1-28 each cycle on top of azacitidine + venetoclax (NCT06652438 chunk 1) | Requires WBC <25 x 10^9/L before enrollment (hydroxyurea allowed); trial population defined by intensive-therapy ineligibility rather than published safety outcomes yet (NCT06652438 chunk 1) | Interventional trial; ongoing Phase 3 | ClinicalTrials.gov NCT06652438 | 2025 record | https://clinicaltrials.gov/study/NCT06652438 | Adults >=18 years; central confirmation of NPM1 mutation or KMT2A rearrangement; newly diagnosed disease, including >=10% blasts for NPM1c entry criterion (NCT06652438 chunk 1) |
| Ziftomenib program in untreated NPM1-mutated or KMT2A-rearranged AML: nonintensive venetoclax/azacitidine +/- ziftomenib and intensive 7+3 +/- ziftomenib | Phase 3, randomized, double-blind, placebo-controlled; estimated enrollment 1,300; nonintensive study primary endpoint OS; intensive study primary endpoint EFS, with CR/MRD-related endpoints also specified (NCT07007312 chunk 1) | No mature efficacy/safety results yet in this registration excerpt; standard backbone toxicities expected from venetoclax/azacitidine or 7+3, with ziftomenib under blinded evaluation (NCT07007312 chunk 1) | Interventional trial; ongoing Phase 3 | ClinicalTrials.gov NCT07007312 | 2025 record | https://clinicaltrials.gov/study/NCT07007312 | Nonintensive arm targets untreated adults with NPM1-mut AML; intensive arm includes untreated adults with NPM1-mut or KMT2A-rearranged AML (NCT07007312 chunk 1) |


*Table: This table summarizes high-value recent clinical evidence and current Phase 3 implementation studies for NPM1-mutated AML, spanning MRD-guided venetoclax use, preemptive relapse treatment, menin inhibition with revumenib, and active registrational trials. It is useful for comparing outcomes, safety signals, and real-world translational applications across the rapidly evolving 2023-2025 landscape.*

### 11.5 Suggested MAXO terms (treatment action ontology; suggestions)
- induction chemotherapy
- consolidation chemotherapy
- allogeneic hematopoietic stem cell transplantation
- measurable residual disease monitoring
- BCL2 inhibitor therapy (venetoclax)
- hypomethylating agent therapy (azacitidine/decitabine)
- menin inhibitor therapy (revumenib/ziftomenib)

---

## 12. Prevention

Primary prevention of de novo *NPM1*-mutated AML is not established. Practical prevention in AML largely focuses on **reducing therapy-related AML risk** (when feasible) and optimizing supportive care to reduce infectious/hemorrhagic mortality; no *NPM1*-specific preventive interventions were retrieved in the evidence set for this run.

---

## 13. Other Species / Natural Disease

No naturally occurring *NPM1*-mutated AML analogs in non-human species were retrieved in this run.

---

## 14. Model Organisms / Experimental Models

### 14.1 Genetic mouse models
A 2023 primary study used a hematopoietic-specific **conditional knock-in NPM1C+ mouse model** and showed that NPM1C+ alters TAD topology and induces an MPN/MDS-like condition (long latency, splenomegaly, leukocytosis, thrombocytopenia), supporting its use as a mechanistic model for leukemogenesis and differentiation block. (lai2023npm1mutationreprograms pages 1-3)

### 14.2 Cell lines and PDX models
- OCI-AML3 (human NPM1-mutant AML) is used in mechanistic intervention experiments including XPO1 inhibition (selinexor) to restore nuclear NPM1 and reduce HOX/MEIS1 programs. (lai2023npm1mutationreprograms pages 1-3)
- Patient-derived xenograft (PDX) models and AML cell lines are used to test menin–MLL inhibitors (e.g., DS‑1594a preclinical work; multiple models including PDX). (numata2023anovelmeninmll1 pages 1-2)

---

## Appendix: Key “expert opinion” / interpretive synthesis (grounded in authoritative sources)

1. **Classification is converging on “AML-defining” genetics, but thresholds differ.** WHO 2022’s no-blast-threshold stance for AML-defining genetics contrasts with ICC’s ≥10% cutoff, creating a gray zone for low-blast NPM1-mutated myeloid neoplasms. (falini2024criteriafordiagnosis pages 5-6, patel2024npm1mutatedacutemyeloid pages 4-4)
2. **MRD is central for NPM1-mutated AML management across treatment intensities.** MRD is presented as a key decision tool in diagnostic guidance and is strongly prognostic in contemporary venetoclax-treated cohorts; it also enables relapse-preemptive strategies. (falini2024criteriafordiagnosis pages 1-2, othman2024molecularmrdis pages 1-2, tiong2024targetingmolecularmeasurable pages 1-2)
3. **Therapy is shifting from cytotoxic-only toward genotype-driven targeted combinations.** Menin inhibition has first-in-human efficacy and is now being tested in large Phase 3 trials in both intensive and nonintensive backbones in NPM1-mutated AML. (issa2023themenininhibitor pages 1-2, NCT07211958 chunk 1, NCT07007312 chunk 1, NCT06652438 chunk 1)

---

### Notes on evidence limitations
- This run did not retrieve ICD, MeSH, OMIM, Orphanet, or a disease-specific MONDO identifier for *NPM1*-mutated AML, and therefore these identifiers are not asserted here.
- Supportive care details (antibacterial/antifungal prophylaxis specifics) were not extracted into citable evidence within this run and are therefore not included as major claims.


References

1. (falini2024criteriafordiagnosis pages 1-2): Brunangelo Falini and Richard Dillon. Criteria for diagnosis and molecular monitoring of <i>npm1</i>-mutated aml. Blood Cancer Discovery, 5:8-20, Dec 2024. URL: https://doi.org/10.1158/2643-3230.bcd-23-0144, doi:10.1158/2643-3230.bcd-23-0144. This article has 40 citations and is from a peer-reviewed journal.

2. (patel2024npm1mutatedacutemyeloid pages 1-2): Sanjay S. Patel. Npm1-mutated acute myeloid leukemia: recent developments and open questions. Pathobiology, 91:18-29, Mar 2024. URL: https://doi.org/10.1159/000530253, doi:10.1159/000530253. This article has 23 citations and is from a peer-reviewed journal.

3. (falini2024criteriafordiagnosis pages 5-6): Brunangelo Falini and Richard Dillon. Criteria for diagnosis and molecular monitoring of <i>npm1</i>-mutated aml. Blood Cancer Discovery, 5:8-20, Dec 2024. URL: https://doi.org/10.1158/2643-3230.bcd-23-0144, doi:10.1158/2643-3230.bcd-23-0144. This article has 40 citations and is from a peer-reviewed journal.

4. (shimony2023acutemyeloidleukemia pages 5-6): Shai Shimony, Maximilian Stahl, and Richard M. Stone. Acute myeloid leukemia: 2023 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:502-526, Jan 2023. URL: https://doi.org/10.1002/ajh.26822, doi:10.1002/ajh.26822. This article has 524 citations and is from a domain leading peer-reviewed journal.

5. (sargas2023comparisonofthe pages 1-2): Claudia Sargas, Rosa Ayala, María J. Larráyoz, María C. Chillón, Eduardo Rodriguez-Arboli, Cristina Bilbao, Esther Prados de la Torre, David Martínez-Cuadrón, Rebeca Rodríguez-Veiga, Blanca Boluda, Cristina Gil, Teresa Bernal, Juan Bergua, Lorenzo Algarra, Mar Tormo, Pilar Martínez-Sánchez, Elena Soria, Josefina Serrano, Juan M. Alonso-Dominguez, Raimundo García, María Luz Amigo, Pilar Herrera-Puente, María J. Sayas, Esperanza Lavilla-Rubira, Joaquín Martínez-López, María J. Calasanz, Ramón García-Sanz, José A. Pérez-Simón, María T. Gómez Casares, Joaquín Sánchez-García, Eva Barragán, Pau Montesinos, and Esther Prados de la Torre. Comparison of the 2022 and 2017 european leukemianet risk classifications in a real-life cohort of the pethema group. Blood Cancer Journal, May 2023. URL: https://doi.org/10.1038/s41408-023-00835-5, doi:10.1038/s41408-023-00835-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

6. (lachowiez2023comparisonandvalidation pages 1-2): Curtis A. Lachowiez, Nicola Long, Jennifer Saultz, Arpita Gandhi, Laura F. Newell, Brandon Hayes-Lattin, Richard T. Maziarz, Jessica Leonard, Daniel Bottomly, Shannon McWeeney, Jennifer Dunlap, Richard Press, Gabrielle Meyers, Ronan Swords, Rachel J. Cook, Jeffrey W. Tyner, Brian J. Druker, and Elie Traer. Comparison and validation of the 2022 european leukemianet guidelines in acute myeloid leukemia. Blood Advances, 7:1899-1909, May 2023. URL: https://doi.org/10.1182/bloodadvances.2022009010, doi:10.1182/bloodadvances.2022009010. This article has 112 citations and is from a peer-reviewed journal.

7. (patel2024npm1mutatedacutemyeloid pages 4-4): Sanjay S. Patel. Npm1-mutated acute myeloid leukemia: recent developments and open questions. Pathobiology, 91:18-29, Mar 2024. URL: https://doi.org/10.1159/000530253, doi:10.1159/000530253. This article has 23 citations and is from a peer-reviewed journal.

8. (sharma2023npm1mutations pages 1-2): Naman Sharma and Jane L. Liesveld. Npm 1 mutations in aml—the landscape in 2023. Cancers, 15:1177, Feb 2023. URL: https://doi.org/10.3390/cancers15041177, doi:10.3390/cancers15041177. This article has 60 citations.

9. (mrozek2023outcomepredictionby pages 1-2): Krzysztof Mrózek, Jessica Kohlschmidt, James S. Blachly, Deedra Nicolet, Andrew J. Carroll, Kellie J. Archer, Alice S. Mims, Karilyn T. Larkin, Shelley Orwick, Christopher C. Oakes, Jonathan E. Kolitz, Bayard L. Powell, William G. Blum, Guido Marcucci, Maria R. Baer, Geoffrey L. Uy, Wendy Stock, John C. Byrd, and Ann-Kathrin Eisfeld. Outcome prediction by the 2022 european leukemianet genetic-risk classification for adults with acute myeloid leukemia: an alliance study. Leukemia, 37:788-798, Feb 2023. URL: https://doi.org/10.1038/s41375-023-01846-8, doi:10.1038/s41375-023-01846-8. This article has 82 citations and is from a highest quality peer-reviewed journal.

10. (chin2023targetingandmonitoring pages 1-2): Lynn Chin, Chantelle Ye Gwen Wong, and Harinder Gill. Targeting and monitoring acute myeloid leukaemia with nucleophosmin-1 (npm1) mutation. International Journal of Molecular Sciences, 24:3161, Feb 2023. URL: https://doi.org/10.3390/ijms24043161, doi:10.3390/ijms24043161. This article has 20 citations.

11. (othman2024molecularclinicaland pages 1-5): Jad Othman, Nicola Potter, Adam Ivey, Yanis Tazi, Elli Papaemmanuil, Jelena Jovanovic, Sylvie D. Freeman, Amanda Gilkes, Rosemary Gale, Tanya Rapoz-D’Silva, Manohursingh Runglall, Michelle Kleeman, Pawan Dhami, Ian Thomas, Sean Johnson, Joanna Canham, Jamie Cavenagh, Panagiotis Kottaridis, Claire Arnold, Hans Beier Ommen, Ulrik Malthe Overgaard, Mike Dennis, Alan Burnett, Charlotte Wilhelm-Benartzi, Brian Huntly, Nigel H. Russell, and Richard Dillon. Molecular, clinical, and therapeutic determinants of outcome in <i>npm1</i>-mutated aml. Blood, 144:714-728, Aug 2024. URL: https://doi.org/10.1182/blood.2024024310, doi:10.1182/blood.2024024310. This article has 86 citations and is from a highest quality peer-reviewed journal.

12. (papadopoulou2024characteristicsandprognosis pages 1-2): Vasiliki Papadopoulou, Giulia Schiavini, Gregoire Stalder, Valentin Basset, Jacqueline Schoumans, Mitja Nabergoj, and Muriel Schaller. Characteristics and prognosis of “acute promyelocytic leukemia-like” nucleophosmin-1-mutated acute myeloid leukemia in a retrospective patient cohort. Biomedicines, 12:2282, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102282, doi:10.3390/biomedicines12102282. This article has 2 citations.

13. (patel2024npm1mutatedacutemyeloid pages 3-4): Sanjay S. Patel. Npm1-mutated acute myeloid leukemia: recent developments and open questions. Pathobiology, 91:18-29, Mar 2024. URL: https://doi.org/10.1159/000530253, doi:10.1159/000530253. This article has 23 citations and is from a peer-reviewed journal.

14. (lai2023npm1mutationreprograms pages 1-3): Qian Lai, Karina Hamamoto, Huacheng Luo, Zachary J Zaroogian, Caixian Zhou, Julia Lesperance, Jie Zha, Y. Qiu, O. Guryanova, Suming Huang, and Bing Xu. Npm1 mutation reprograms leukemic transcription network via reshaping tad topology. Leukemia, 37:1732-1736, Jun 2023. URL: https://doi.org/10.1038/s41375-023-01942-9, doi:10.1038/s41375-023-01942-9. This article has 11 citations and is from a highest quality peer-reviewed journal.

15. (patel2024npm1mutatedacutemyeloid pages 8-9): Sanjay S. Patel. Npm1-mutated acute myeloid leukemia: recent developments and open questions. Pathobiology, 91:18-29, Mar 2024. URL: https://doi.org/10.1159/000530253, doi:10.1159/000530253. This article has 23 citations and is from a peer-reviewed journal.

16. (patel2024npm1mutatedacutemyeloid pages 2-3): Sanjay S. Patel. Npm1-mutated acute myeloid leukemia: recent developments and open questions. Pathobiology, 91:18-29, Mar 2024. URL: https://doi.org/10.1159/000530253, doi:10.1159/000530253. This article has 23 citations and is from a peer-reviewed journal.

17. (othman2024molecularmrdis pages 1-2): Jad Othman, Ing S. Tiong, Jenny O'Nions, Mike Dennis, Katya Mokretar, Adam Ivey, Michael Austin, Anne-Louise Latif, Mariam Amer, Wei Yee Chan, Charles Crawley, Francesca Crolla, Joe Cross, Ray Dang, Johnathon Elliot, Chun Y. Fong, Sofia Galli, Paolo Gallipoli, Francesca Hogan, Pallavi Kalkur, Anjum Khan, Pramila Krishnamurthy, John Laurie, Sun Loo, Scott Marshall, Priyanka Mehta, Vidhya Murthy, Sateesh Nagumantry, Srinivas Pillai, Nicola Potter, Rob Sellar, Tom Taylor, Rui Zhao, Nigel H. Russell, Andrew H. Wei, and Richard Dillon. Molecular mrd is strongly prognostic in patients with <i>npm1</i>-mutated aml receiving venetoclax-based nonintensive therapy. Blood, 143:336-341, Jan 2024. URL: https://doi.org/10.1182/blood.2023021579, doi:10.1182/blood.2023021579. This article has 79 citations and is from a highest quality peer-reviewed journal.

18. (falini2024criteriafordiagnosis media 3d972561): Brunangelo Falini and Richard Dillon. Criteria for diagnosis and molecular monitoring of <i>npm1</i>-mutated aml. Blood Cancer Discovery, 5:8-20, Dec 2024. URL: https://doi.org/10.1158/2643-3230.bcd-23-0144, doi:10.1158/2643-3230.bcd-23-0144. This article has 40 citations and is from a peer-reviewed journal.

19. (shukla2024molecularfeaturesand pages 5-6): Mihir Shukla, Maher Abdul-Hay, and Jun H. Choi. Molecular features and treatment paradigms of acute myeloid leukemia. Biomedicines, 12:1768, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081768, doi:10.3390/biomedicines12081768. This article has 6 citations.

20. (tiong2024targetingmolecularmeasurable pages 1-2): Ing Soo Tiong, Devendra K. Hiwase, Emad Abro, Ashish Bajel, Emma Palfreyman, Ashanka Beligaswatte, John Reynolds, Natasha Anstee, Tamia Nguyen, Sun Loo, Chong Chyn Chua, Michael Ashby, Kaitlyn M. Wiltshire, Shaun Fleming, Chun Y. Fong, Tse-Chieh Teh, Piers Blombery, Richard Dillon, Adam Ivey, and Andrew H. Wei. Targeting molecular measurable residual disease and low-blast relapse in aml with venetoclax and low-dose cytarabine: a prospective phase ii study (valdac). Journal of Clinical Oncology, 42:2161-2173, Jun 2024. URL: https://doi.org/10.1200/jco.23.01599, doi:10.1200/jco.23.01599. This article has 32 citations and is from a highest quality peer-reviewed journal.

21. (issa2023themenininhibitor pages 1-2): Ghayas C. Issa, Ibrahim Aldoss, John DiPersio, Branko Cuglievan, Richard Stone, Martha Arellano, Michael J. Thirman, Manish R. Patel, David S. Dickens, Shalini Shenoy, Neerav Shukla, Hagop Kantarjian, Scott A. Armstrong, Florian Perner, Jennifer A. Perry, Galit Rosen, Rebecca G. Bagley, Michael L. Meyers, Peter Ordentlich, Yu Gu, Vinit Kumar, Steven Smith, Gerard M. McGeehan, and Eytan M. Stein. The menin inhibitor revumenib in kmt2a-rearranged or npm1-mutant leukaemia. Nature, 615:920-924, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05812-3, doi:10.1038/s41586-023-05812-3. This article has 522 citations and is from a highest quality peer-reviewed journal.

22. (issa2023themenininhibitor pages 4-4): Ghayas C. Issa, Ibrahim Aldoss, John DiPersio, Branko Cuglievan, Richard Stone, Martha Arellano, Michael J. Thirman, Manish R. Patel, David S. Dickens, Shalini Shenoy, Neerav Shukla, Hagop Kantarjian, Scott A. Armstrong, Florian Perner, Jennifer A. Perry, Galit Rosen, Rebecca G. Bagley, Michael L. Meyers, Peter Ordentlich, Yu Gu, Vinit Kumar, Steven Smith, Gerard M. McGeehan, and Eytan M. Stein. The menin inhibitor revumenib in kmt2a-rearranged or npm1-mutant leukaemia. Nature, 615:920-924, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05812-3, doi:10.1038/s41586-023-05812-3. This article has 522 citations and is from a highest quality peer-reviewed journal.

23. (NCT07211958 chunk 1):  Study of Revumenib in Combination With Intensive Chemotherapy in Newly Diagnosed Acute Myeloid Leukemia (AML) With a NPM1 Mutation. Syndax Pharmaceuticals. 2025. ClinicalTrials.gov Identifier: NCT07211958

24. (NCT06652438 chunk 1):  Revumenib in Combination With Azacitidine + Venetoclax in Patients NPM1-mutated or KMT2A-rearranged AML. Stichting Hemato-Oncologie voor Volwassenen Nederland. 2025. ClinicalTrials.gov Identifier: NCT06652438

25. (NCT07007312 chunk 1):  Studies to Assess Ziftomenib in Combination With Ven+Aza or 7+3 in Patients With Untreated NPM1-m or KMT2A-r AML. Kura Oncology, Inc.. 2025. ClinicalTrials.gov Identifier: NCT07007312

26. (othman2024molecularmrdis pages 7-8): Jad Othman, Ing S. Tiong, Jenny O'Nions, Mike Dennis, Katya Mokretar, Adam Ivey, Michael Austin, Anne-Louise Latif, Mariam Amer, Wei Yee Chan, Charles Crawley, Francesca Crolla, Joe Cross, Ray Dang, Johnathon Elliot, Chun Y. Fong, Sofia Galli, Paolo Gallipoli, Francesca Hogan, Pallavi Kalkur, Anjum Khan, Pramila Krishnamurthy, John Laurie, Sun Loo, Scott Marshall, Priyanka Mehta, Vidhya Murthy, Sateesh Nagumantry, Srinivas Pillai, Nicola Potter, Rob Sellar, Tom Taylor, Rui Zhao, Nigel H. Russell, Andrew H. Wei, and Richard Dillon. Molecular mrd is strongly prognostic in patients with <i>npm1</i>-mutated aml receiving venetoclax-based nonintensive therapy. Blood, 143:336-341, Jan 2024. URL: https://doi.org/10.1182/blood.2023021579, doi:10.1182/blood.2023021579. This article has 79 citations and is from a highest quality peer-reviewed journal.

27. (othman2024molecularmrdis pages 5-6): Jad Othman, Ing S. Tiong, Jenny O'Nions, Mike Dennis, Katya Mokretar, Adam Ivey, Michael Austin, Anne-Louise Latif, Mariam Amer, Wei Yee Chan, Charles Crawley, Francesca Crolla, Joe Cross, Ray Dang, Johnathon Elliot, Chun Y. Fong, Sofia Galli, Paolo Gallipoli, Francesca Hogan, Pallavi Kalkur, Anjum Khan, Pramila Krishnamurthy, John Laurie, Sun Loo, Scott Marshall, Priyanka Mehta, Vidhya Murthy, Sateesh Nagumantry, Srinivas Pillai, Nicola Potter, Rob Sellar, Tom Taylor, Rui Zhao, Nigel H. Russell, Andrew H. Wei, and Richard Dillon. Molecular mrd is strongly prognostic in patients with <i>npm1</i>-mutated aml receiving venetoclax-based nonintensive therapy. Blood, 143:336-341, Jan 2024. URL: https://doi.org/10.1182/blood.2023021579, doi:10.1182/blood.2023021579. This article has 79 citations and is from a highest quality peer-reviewed journal.

28. (numata2023anovelmeninmll1 pages 1-2): Masashi Numata, Noriyasu Haginoya, Machiko Shiroishi, Tsuyoshi Hirata, Aiko Sato-Otsubo, Kenji Yoshikawa, Yoshimi Takata, Reina Nagase, Yoshinori Kashimoto, Makoto Suzuki, Nina Schulte, Gernot Polier, Akiko Kurimoto, Yumiko Tomoe, Akiko Toyota, Tomoko Yoneyama, Emi Imai, Kenji Watanabe, Tomoaki Hamada, Ryutaro Kanada, Jun Watanabe, Yoshiko Kagoshima, Eri Tokumaru, Kenji Murata, Takayuki Baba, Taeko Shinozaki, Masami Ohtsuka, Koichi Goto, Tsuyoshi Karibe, Takao Deguchi, Yoshihiro Gocho, Masanori Yoshida, Daisuke Tomizawa, Motohiro Kato, Shinji Tsutsumi, Mayumi Kitagawa, and Yuki Abe. A novel menin-mll1 inhibitor, ds-1594a, prevents the progression of acute leukemia with rearranged mll1 or mutated npm1. Cancer Cell International, Feb 2023. URL: https://doi.org/10.1186/s12935-023-02877-y, doi:10.1186/s12935-023-02877-y. This article has 34 citations and is from a peer-reviewed journal.
