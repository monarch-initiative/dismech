---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:54.166946'
end_time: '2026-04-04T12:39:37.122784'
duration_seconds: 882.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Periventricular Nodular Heterotopia
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Periventricular Nodular Heterotopia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Periventricular Nodular Heterotopia** covering all of the
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
- **Disease Name:** Periventricular Nodular Heterotopia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Periventricular Nodular Heterotopia** covering all of the
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


# Comprehensive Disease Characteristics Report: Periventricular Nodular Heterotopia (PVNH)

## Executive summary
Periventricular nodular heterotopia (PVNH; also PNH) is a malformation of cortical development caused by abnormal neuronal migration, with heterotopic gray-matter nodules lining the lateral ventricular walls and a strong association with epilepsy and variable neurodevelopmental outcomes. Classical PVNH is most often due to X-linked loss-of-function (LoF) variants in **FLNA**, but PVNH is genetically heterogeneous, with multiple additional Mendelian genes and copy-number variants (CNVs) implicated. Recent 2023–2024 work expanded causal gene/phenotype space (e.g., **ARF1**, **TAOK1**) and provided experimentally testable pathway hypotheses (e.g., **autophagy/AMPK** modulation in **DCHS1/FAT4**-related periventricular heterotopia) with a potential repurposing angle for **metformin** in model systems. (agathe2023arf1relateddisorderphenotypic pages 1-2, cavalli2024heterozygoustruncatingvariant pages 1-3, bressan2023metforminrescuesmigratory pages 1-2)

---

## 1. Disease information
### 1.1 Disease overview (definition and current understanding)
PVNH/PNH is a neuronal migration disorder in which subsets of neurons fail to migrate into the developing cerebral cortex and instead “remain as nodules lining the ventricular surface,” producing periventricular nodules (typically adjacent to the lateral ventricles). (parrini2004mosaicmutationsof pages 1-2)

A practical MRI definition used clinically is the presence of subependymal/periventricular nodules with signal similar to gray matter along the lateral ventricle lining, frequently bilateral and often anterior predominant in FLNA-associated disease. (fernandes2024periventricularnodularheterotopias pages 1-2, lu2022theclinicaland pages 1-8)

### 1.2 Key identifiers
- **OMIM (disease):** Periventricular nodular heterotopia / PNH **300049** (parrini2004mosaicmutationsof pages 1-2, gerlevik2022computationalanalysisof pages 1-2)
- **OMIM (gene):** **FLNA/FLN1** **\*300017** (parrini2004mosaicmutationsof pages 1-2)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** Not available in the retrieved evidence corpus for this run; should be added via direct lookup in MONDO/Orphanet/ICD/MeSH resources outside the current tool context. (parrini2004mosaicmutationsof pages 1-2)

### 1.3 Synonyms and alternative names
Commonly used synonyms include:
- **Periventricular heterotopia** / **periventricular nodular heterotopia** (PVNH/PNH) (parrini2004mosaicmutationsof pages 1-2, paliotti2022epilepsyinindividualsa pages 8-13)
- **Subependymal heterotopia(s)** (fernandes2024periventricularnodularheterotopias pages 1-2)

### 1.4 Evidence source type
This report synthesizes evidence from:
- Aggregated disease-level cohorts and cross-sectional/retrospective cohorts (e.g., 24-person FLNA LoF cohort; 47-person FLNA-PVNH cohort; 100-person PVNH epilepsy cohort) (rijckmans2024counselingindividualswith pages 1-3, lange201547patientswith pages 1-2, paliotti2022epilepsyinindividualsa pages 26-31)
- Primary experimental studies using patient-derived cells/organoids and xenografts (e.g., DCHS1/FAT4 models) (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 9-10)
- ClinicalTrials.gov registry entries for research implementations involving PVNH (NCT00552045 chunk 1, NCT05696912 chunk 1)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary causes are genetic**, centered on disruption of neuronal migration and related developmental programs.

- **Classical/X-linked PVNH:** X-linked dominant LoF variants in **FLNA** are a major cause and show strong female predominance; hemizygous male viability is reduced with high prenatal/perinatal lethality, though surviving males occur (often via mosaicism or hypomorphic alleles). (lange201547patientswith pages 1-2, cannaerts2018flnamutationsin pages 1-3, lange201547patientswith pages 4-6)
- **Autosomal dominant PVNH syndromes:** De novo **ARF1** variants were identified in a 17-individual cohort with a phenotype including PVNH, seizures, microcephaly, and intellectual disability. (agathe2023arf1relateddisorderphenotypic pages 1-1)
- **Other Mendelian causes:** PVNH genetic heterogeneity includes genes implicated in vesicle trafficking (e.g., **ARFGEF2**) and multiple other loci; CNVs are also reported contributors. (paliotti2022epilepsyinindividuals pages 17-22, lange201547patientswith pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors (examples supported by retrieved evidence)
- **FLNA LoF**: most frequent cause of bilateral/anterior-predominant PVNH. (lange201547patientswith pages 1-2, lu2022theclinicaland pages 1-8)
- **ARF1 (de novo)**: autosomal dominant NDD including PVNH. (agathe2023arf1relateddisorderphenotypic pages 1-1)
- **TAOK1 (heterozygous truncating)**: reported association with PVNH in a child with TAOK1-related NDD. (cavalli2024heterozygoustruncatingvariant pages 1-3)
- **DCHS1/FAT4**: periventricular heterotopia/gray matter heterotopia with demonstrated migration defects in patient-derived models. (bressan2023metforminrescuesmigratory pages 1-2)

#### Environmental risk factors
Not established in the retrieved evidence corpus; PVNH is predominantly treated as a genetic neurodevelopmental disorder in the included sources. (parrini2004mosaicmutationsof pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-2)

### 2.3 Protective factors
No validated protective variants or environmental protective factors were identified in the retrieved evidence corpus. (parrini2004mosaicmutationsof pages 1-2)

### 2.4 Gene–environment interactions
Not addressed in the retrieved evidence corpus. (parrini2004mosaicmutationsof pages 1-2)

---

## 3. Phenotypes (clinical spectrum)
The phenotype is variable and depends on genetic etiology and imaging pattern (isolated PVNH vs PVNH-plus with additional malformations). (paliotti2022epilepsyinindividualsa pages 26-31)

### 3.1 Core neurologic phenotypes
- **Epilepsy/seizures (HP:0001250):** In a 100-person PVNH cohort, **70/100 (70%)** had epilepsy. (paliotti2022epilepsyinindividualsa pages 17-22, paliotti2022epilepsyinindividuals pages 17-22)
- **Seizure onset:** Mean **7.9 years** (range day 1–41 years) in the 100-person cohort. (paliotti2022epilepsyinindividualsa pages 26-31)
- **EEG abnormalities:** **95% (92/99)** abnormal EEG in the 100-person cohort, including focal, multifocal, and generalized interictal epileptiform discharges. (paliotti2022epilepsyinindividualsa pages 26-31)

### 3.2 Neurodevelopmental and behavioral phenotypes
In the 100-person cohort:
- **Delayed milestones (HP:0001263):** **43%** (paliotti2022epilepsyinindividualsa pages 26-31)
- **Learning/communication difficulties (HP:0001328 / HP:0000750):** **62%** (paliotti2022epilepsyinindividualsa pages 26-31)
- **Autism diagnosis / autistic behavior (HP:0000729):** **15%** (paliotti2022epilepsyinindividualsa pages 26-31)

### 3.3 Systemic phenotypes in FLNA LoF (“FLNA deficiency”)
In a 24-individual FLNA LoF cohort:
- **Epilepsy:** **84%** with median onset **17 years**; drug resistance **42%** among those with seizure data. (rijckmans2024counselingindividualswith pages 5-6)
- **Cardiovascular involvement (HP:0001626):** **56%** (9/16 with comprehensive cardiology evaluation). (rijckmans2024counselingindividualswith pages 5-6)
- **Constipation/GI dysmotility (HP:0002019):** constipation noted at cohort level (~25% in extracted cohort discussion) and severe cases including chronic intestinal pseudo-obstruction (CIPO). (rijckmans2024counselingindividualswith pages 6-8, rijckmans2024counselingindividualswith pages 5-6)
- **Thrombocytopenia (HP:0001873):** reported in two cohort members. (rijckmans2024counselingindividualswith pages 5-6)

### 3.4 Phenotype frequencies and suggested HPO terms (curation-ready)
A structured phenotype table with HPO mappings and cohort frequencies is provided below.

| Feature | Suggested HPO term(s) | Frequency/statistic | Cohort/source details (n, population) | Notes | Citation IDs |
|---|---|---|---|---|---|
| Periventricular nodular heterotopia on MRI | HP:0002138 Periventricular heterotopia | 23/24 (95.8%) | FLNA loss-of-function cohort, 24 index patients | Core neuroimaging feature in FLNA deficiency cohort | (rijckmans2024counselingindividualswith pages 1-3, rijckmans2025"phenotypicandgenotypic pages 1-6) |
| Epilepsy | HP:0001250 Seizure, HP:0002123 Generalized myoclonic seizure, HP:0007359 Focal-onset seizure | 16/19 (84%) | FLNA loss-of-function cohort, seizure data available for 19/24 | Median seizure onset 17 years in this cohort | (rijckmans2025"phenotypicandgenotypic pages 6-10, rijckmans2024counselingindividualswith pages 5-6) |
| Cardiovascular involvement | HP:0001626 Abnormality of the cardiovascular system, HP:0001659 Congenital heart defect, HP:0001644 Dilatation of the aorta | 9/16 (56%) | FLNA loss-of-function cohort, 16/24 had comprehensive cardiology evaluation | Valve insufficiency most common; aortic root involvement reported | (rijckmans2025"phenotypicandgenotypic pages 6-10, rijckmans2024counselingindividualswith pages 5-6, rijckmans2024counselingindividualswith pages 6-8) |
| Constipation / GI dysmotility | HP:0002019 Constipation, HP:0012602 Intestinal pseudo-obstruction | 25% constipation; 1 case CIPO requiring colectomy | FLNA loss-of-function cohort, 24 index patients | Constipation likely underreported in earlier literature | (rijckmans2024counselingindividualswith pages 6-8, rijckmans2025"phenotypicandgenotypic pages 10-14) |
| Thrombocytopenia | HP:0001873 Thrombocytopenia | 2 cases | FLNA loss-of-function cohort, 24 index patients | Hematologic involvement recognized but incompletely quantified | (rijckmans2024counselingindividualswith pages 5-6, rijckmans2024counselingindividualswith pages 6-8) |
| Posterior fossa anomaly / mega cisterna magna on MRI | HP:0002280 Enlarged cisterna magna, HP:0000936 Posterior fossa abnormality | 33% | FLNA loss-of-function cohort, 24 index patients | MRI-associated anomaly in addition to PVNH | (rijckmans2024counselingindividualswith pages 5-6) |
| Corpus callosum abnormality | HP:0001273 Abnormality of the corpus callosum | 18% | FLNA loss-of-function cohort, 24 index patients | Structural MRI-associated anomaly | (rijckmans2024counselingindividualswith pages 5-6) |
| Seizure-free carriers | HP:0001250 Seizure | 10 carriers seizure-free; median age 19.7 years | FLNA-associated PVNH cohort, 47 patients | Shows incomplete penetrance for epilepsy | (lange201547patientswith pages 1-2) |
| Mainstream schooling / preserved educational attainment | HP:0000729 Autistic behavior, HP:0001249 Intellectual disability | 22/24 attended regular school | FLNA-associated PVNH cohort, educational data available for 24 patients | Supports generally preserved cognition in many FLNA-PVNH patients | (lange201547patientswith pages 1-2) |
| Diagnostic latency | HP:0010524 Delayed diagnosis | Median 17-20 years | FLNA-associated PVNH cohort, 47 patients | Long delay may postpone surveillance for cardiovascular complications | (lange201547patientswith pages 1-2) |
| Delayed developmental milestones | HP:0001263 Global developmental delay, HP:0011344 Severe global developmental delay | 43% | PVNH cohort, n=100 | Mixed-genetic/clinical PVNH cohort | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Learning or communication difficulties | HP:0001328 Learning disability, HP:0000750 Delayed speech and language development | 62% | PVNH cohort, n=100 | Reflects common neurodevelopmental burden beyond seizures | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Autism spectrum disorder | HP:0000729 Autistic behavior | 15/100 (15%) | PVNH cohort, n=100 | Behavioral/neurodevelopmental comorbidity | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Epilepsy overall | HP:0001250 Seizure | 70/100 (70%) | PVNH cohort, n=100 | Broad PVNH cohort; epilepsy common but not universal | (paliotti2022epilepsyinindividualsa pages 17-22, paliotti2022epilepsyinindividuals pages 17-22) |
| Self-limited epilepsy course | HP:0001250 Seizure | 10% | PVNH cohort, n=100 | Indicates a minority have relatively benign seizure trajectory | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Pharmacoresponsive epilepsy | HP:0001250 Seizure | 35% | PVNH cohort, n=100 | Seizure-free mean 4.5 years in responders | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Uncontrolled seizures | HP:0001250 Seizure | 55% | PVNH cohort, n=100 | Highlights substantial refractory burden | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Drug-resistant epilepsy | HP:0001250 Seizure, HP:0032794 Drug-resistant epilepsy | 23% | PVNH cohort, n=100 | Multiple bilateral PVNH had highest drug-resistance in this cohort | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Corpus callosum agenesis/dysgenesis | HP:0001274 Agenesis of corpus callosum, HP:0001273 Abnormality of the corpus callosum | 28% | PVNH-Plus subgroup within PVNH cohort, n=100 overall | One of the most frequent associated brain malformations | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Ventricular abnormalities | HP:0002119 Ventriculomegaly | 20% | PVNH-Plus subgroup within PVNH cohort, n=100 overall | Associated imaging abnormality | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Polymicrogyria | HP:0002126 Polymicrogyria | 18% | PVNH-Plus subgroup within PVNH cohort, n=100 overall | Co-occurring malformation of cortical development | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Brain cysts | HP:0000932 Cerebral cyst | 16% | PVNH-Plus subgroup within PVNH cohort, n=100 overall | Associated structural brain finding | (paliotti2022epilepsyinindividualsa pages 26-31) |
| Hippocampal abnormality | HP:0012083 Abnormality of the hippocampus | 13% | PVNH-Plus subgroup within PVNH cohort, n=100 overall | Relevant to epileptogenic network considerations | (paliotti2022epilepsyinindividualsa pages 26-31) |


*Table: This table summarizes key clinical and imaging features of periventricular nodular heterotopia with frequencies drawn from major cohorts, emphasizing FLNA-related multisystem disease and epilepsy outcomes in broader PVNH populations. It is useful for structured phenotype curation and knowledge base entry building.*

### 3.5 Quality-of-life impact
Validated QoL instruments (e.g., SF-36, EQ-5D, PROMIS) were not reported in the retrieved evidence corpus. Functional impact is nevertheless strongly suggested by the high proportion of individuals with uncontrolled or drug-resistant seizures (55% uncontrolled; 23% drug-resistant in one 100-person cohort) and by multisystem FLNA-related complications (e.g., cardiovascular disease requiring surveillance). (paliotti2022epilepsyinindividualsa pages 26-31, rijckmans2024counselingindividualswith pages 6-8)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (representative, evidence-backed)
- **FLNA (X-linked dominant):** most frequent cause of classical bilateral/anterior-predominant PVNH. (lange201547patientswith pages 1-2, lu2022theclinicaland pages 1-8)
- **ARF1 (autosomal dominant, de novo):** neurodevelopmental disorder with PVNH, microcephaly, seizures, and intellectual disability (international cohort, n=17). (agathe2023arf1relateddisorderphenotypic pages 1-1)
- **TAOK1 (autosomal dominant, typically de novo):** truncating variant associated with PVNH in a reported case; supports a role in neuronal migration disorders. (cavalli2024heterozygoustruncatingvariant pages 1-3)
- **DCHS1 / FAT4:** periventricular heterotopia/gray matter heterotopia with experimentally demonstrated migration/autophagy phenotypes. (bressan2023metforminrescuesmigratory pages 1-2)
- **ARFGEF2:** mentioned as PVNH-associated, mechanistically tied to vesicle trafficking and in some contexts associated with microcephaly plus PVNH. (gerlevik2022computationalanalysisof pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences
- **FLNA:** Variants are frequently truncating LoF; in one 47-patient FLNA-PVNH cohort, mutations were “mainly truncating (37/39).” (lange201547patientswith pages 1-2)
- **Mosaicism and male survival:** Surviving males in one FLNA cohort carried truncating variants in mosaic state in blood (~40–60% mutant alleles). (lange201547patientswith pages 4-6)
- **Germline mosaicism:** A family report concluded “evidence for germline mosaicism in filamin A-associated periventricular nodular heterotopia,” relevant when parental blood testing is negative. (lapointe2014germlinemosaicismin pages 1-3)

### 4.3 Modifier genes / epigenetics
Not established in the retrieved evidence corpus.

### 4.4 Chromosomal abnormalities / CNVs
CNVs are part of the genetic heterogeneity and are detected in clinical cohorts using chromosomal microarray (CMA) and MLPA (for FLNA). In a 100-person cohort, CMA was used in 20 individuals and CNVs were found in five (three pathogenic). (paliotti2022epilepsyinindividualsa pages 26-31)

### 4.5 Curation table: identifiers and major genetic causes
| Entity (disease/gene) | Identifier type | Identifier | Notes (inheritance/phenotype) | Key citation IDs |
|---|---|---|---|---|
| Periventricular nodular heterotopia (PVNH) / periventricular heterotopia / PNH / subependymal heterotopia | Disease OMIM | 300049 | Neuronal migration disorder with gray-matter nodules lining the lateral ventricles; terms PVNH and PNH are used interchangeably in the literature. Classical form is often bilateral/symmetric and strongly associated with epilepsy. | (parrini2004mosaicmutationsof pages 1-2, fernandes2024periventricularnodularheterotopias pages 1-2, lange201547patientswith pages 1-2, paliotti2022epilepsyinindividualsa pages 8-13) |
| FLNA (historically FLN1) | Gene OMIM | *300017 | Most common cause of classical bilateral/symmetric PVNH; X-linked dominant; female predominance with high prenatal/perinatal lethality in hemizygous males; extracerebral features can include cardiovascular, pulmonary, gastrointestinal, connective-tissue, and hematologic abnormalities. | (parrini2004mosaicmutationsof pages 1-2, lange201547patientswith pages 1-2, lapointe2014germlinemosaicismin pages 1-3, cannaerts2018flnamutationsin pages 1-3) |
| ARF1 | Gene identifier | not available in gathered evidence | De novo variants identified in 17 unrelated individuals; autosomal-dominant ARF1-related neurodevelopmental disorder with severe ID, microcephaly, seizures, and PVNH due to impaired neuronal migration. | (agathe2023arf1relateddisorderphenotypic pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-1) |
| TAOK1 | Gene identifier | not available in gathered evidence | Heterozygous truncating TAOK1 variant reported in a boy with PVNH; described as the first reported neuronal migration disorder in TAOK1-related neurodevelopmental disease. Usually de novo in published cases, with variable developmental delay/NDD phenotype. | (cavalli2024heterozygoustruncatingvariant pages 1-3) |
| DCHS1 | Gene identifier | not available in gathered evidence | Reported genetic cause of periventricular heterotopia/gray matter heterotopia; patient-derived hNPCs show migration defects linked to altered autophagy and paxillin accumulation; wild-type DCHS1 can rescue morphology in model systems. | (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 6-7, bressan2023metforminrescuesmigratory pages 9-10) |
| FAT4 | Gene identifier | not available in gathered evidence | Reported genetic cause of periventricular heterotopia/gray matter heterotopia; DCHS1/FAT4-mutant hNPCs show impaired migration and altered autophagy; metformin promoted migration rescue experimentally. | (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 6-7, bressan2023metforminrescuesmigratory pages 9-10) |
| ARFGEF2 | Gene identifier | OMIM 608097 | Mentioned as a non-FLNA PVNH gene; associated in evidence with autosomal-recessive forms and with microcephaly plus PVNH/neuronal migration disorder; mechanistically linked to vesicle trafficking. | (gerlevik2022computationalanalysisof pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-2, lange201547patientswith pages 1-2) |
| NEDD4L | Gene identifier | not available in gathered evidence | Mentioned among PVNH genes; evidence links NEDD4L-related disease to AKT-mTOR deregulation and migration-related pathology in broader PVNH literature summarized in cohort/thesis evidence. | (paliotti2022epilepsyinindividuals pages 44-47, paliotti2022epilepsyinindividualsa pages 17-22) |
| MAP1B | Gene identifier | not available in gathered evidence | Mentioned among implicated PVNH genes; private de novo/inherited variants reported in PVNH and included in disease heterogeneity summaries. | (paliotti2022epilepsyinindividualsa pages 17-22) |
| TMTC3 | Gene identifier | not available in gathered evidence | Recessive association with PVNH, intellectual disability, and epilepsy; three of four affected siblings had PVNH in the cited study. | (gerlevik2022computationalanalysisof pages 1-2) |


*Table: This table summarizes core disease terminology and the main genes implicated in periventricular nodular heterotopia/periventricular heterotopia based on the gathered evidence. It highlights which identifiers were directly supported in-context and which entries currently lack explicit identifier data in the available evidence.*

---

## 5. Environmental information
No specific toxin, lifestyle, or infectious contributors were identified in the retrieved evidence corpus; PVNH is treated primarily as a genetic neurodevelopmental condition. (parrini2004mosaicmutationsof pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Unifying biological concept
The core mechanistic concept is **disruption of neuronal migration during corticogenesis**, producing ectopic gray-matter nodules adjacent to the ventricles. (parrini2004mosaicmutationsof pages 1-2, paliotti2022epilepsyinindividualsa pages 8-13)

### 6.2 Mechanistic axes with causal chains (examples)
1. **FLNA LoF → cytoskeletal dysregulation → impaired migration → PVNH nodules → epilepsy and multisystem disease**
   - FLNA is an actin-binding/cytoskeletal protein implicated in cell migration; LoF variants cause failure of neurons to migrate, leaving nodules at the ventricular surface. (rijckmans2024counselingindividualswith pages 1-3, parrini2004mosaicmutationsof pages 1-2)

2. **ARF1 de novo variants → altered small-GTPase/vesicle trafficking (trans-Golgi) → impaired neuronal migration → PVNH within a syndromic NDD**
   - ARF1 “acts as a molecular switch” and ARF1-GTP “promotes trans-Golgi and the fission step of the vesicle formation,” linking vesicle trafficking to migration disorders. (agathe2023arf1relateddisorderphenotypic pages 1-2)

3. **DCHS1/FAT4 mutations → impaired autophagic flux and focal adhesion recycling → hNPC migration deficits → heterotopia phenotypes**
   - The migration defect is linked to altered autophagy with paxillin accumulation; “Metformin, an FDA-approved drug, was used to trigger autophagy… and restored the migration of hNPCs derived from PH patients.” (bressan2023metforminrescuesmigratory pages 11-12, bressan2023metforminrescuesmigratory pages 1-2)

### 6.3 Suggested GO biological process and CL cell type terms
A curation-ready mapping of implicated processes and cell types is provided below.

| Gene/axis | Mechanistic theme | Upstream defect | Downstream cellular phenotype | Evidence system (human/organoid/hNPC xenograft) | Therapeutic implication | Suggested GO biological process terms | Suggested CL cell types |
|---|---|---|---|---|---|---|---|
| FLNA | Actin cytoskeleton organization and neuronal migration | Loss-of-function variants in X-linked **FLNA** disrupt filamin A, an actin-binding cytoskeletal scaffold required for cell motility/migration during corticogenesis | Failure of subsets of neurons to migrate from the ventricular zone to cortex, producing bilateral/symmetric periventricular nodules; epilepsy and multisystem manifestations in many affected individuals (parrini2004mosaicmutationsof pages 1-2, lange201547patientswith pages 1-2, paliotti2022epilepsyinindividualsa pages 17-22) | Human clinical/genetic cohorts and case series (parrini2004mosaicmutationsof pages 1-2, lange201547patientswith pages 1-2, paliotti2022epilepsyinindividualsa pages 17-22) | No established pathway-targeted therapy; strong rationale for genetic diagnosis plus surveillance/management rather than mechanism-based drug treatment at present (rijckmans2024counselingindividualswith pages 1-3, lange201547patientswith pages 1-2) | GO:0007010 cytoskeleton organization; GO:0007411 axon guidance; GO:0001764 neuron migration; GO:0030036 actin cytoskeleton organization | CL:0000540 neuron; CL:0011115 neural progenitor cell; CL:0011116 radial glial cell |
| ARF1 / ARFGEF2 | Vesicle trafficking and trans-Golgi network regulation in neuronal migration | De novo **ARF1** variants alter a small GTPase molecular switch; **ARFGEF2** dysfunction perturbs guanine-exchange control of ARF signaling and vesicle formation/trafficking from the trans-Golgi (agathe2023arf1relateddisorderphenotypic pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-1, gerlevik2022computationalanalysisof pages 1-2) | Impaired neuronal migration with PVNH, microcephaly, seizures, and neurodevelopmental disorder; broader migration disorder pattern on MRI (agathe2023arf1relateddisorderphenotypic pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-1) | Human cohort/genetic study with functional validation for ARF1; human genetic association summaries for ARFGEF2 (agathe2023arf1relateddisorderphenotypic pages 1-2, agathe2023arf1relateddisorderphenotypic pages 1-1, gerlevik2022computationalanalysisof pages 1-2) | Primarily diagnostic/genetic-counseling relevance currently; no validated targeted therapy identified in available evidence | GO:0016192 vesicle-mediated transport; GO:0006891 intra-Golgi vesicle-mediated transport; GO:0006886 intracellular protein transport; GO:0001764 neuron migration | CL:0011115 neural progenitor cell; CL:0000540 neuron |
| DCHS1 / FAT4 | Autophagy-dependent migration control; AMPK-autophagy-paxillin/focal adhesion axis | **DCHS1** or **FAT4** mutations impair autophagic flux, including defective autophagosome-lysosome fusion and accumulation of paxillin/focal adhesion components; pathway intersects with AMPK and cellular energy sensing (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 6-7, bressan2023metforminrescuesmigratory pages 9-10, bressan2023metforminrescuesmigratory pages 7-9) | Altered migratory dynamics of human neural progenitor cells, shorter migratory phases, abnormal actin/Golgi organization, exaggerated neuronal/network hyperactivity in derived models, and heterotopia-like phenotypes (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 11-12, bressan2023metforminrescuesmigratory pages 9-10) | Human patient-derived hNPCs, cortical organoids, xenografts into mouse brain, and organoid electrophysiology/proteogenomic analyses (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 6-7, bressan2023metforminrescuesmigratory pages 9-10) | **Metformin** enhanced AMPK-dependent autophagy and rescued migration defects experimentally; autophagy/mTOR modulation is a candidate translational strategy in selected PH forms (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 10-11, bressan2023metforminrescuesmigratory pages 11-12) | GO:0006914 autophagy; GO:1905037 autophagosome organization; GO:0030335 positive regulation of cell migration; GO:0001764 neuron migration; GO:0005925 focal adhesion | CL:0011115 neural progenitor cell; CL:0000540 neuron |
| TAOK1 | Microtubule/cytoskeleton regulation and stress-activated MAPK signaling during cortical maturation | Heterozygous truncating **TAOK1** variants disrupt a MAP3K family kinase important for neuronal maturation, cortical differentiation, microtubule stability, cytoskeletal dynamics, and stress-activated MAPK pathway signaling (cavalli2024heterozygoustruncatingvariant pages 1-3) | Neurodevelopmental disorder with PVNH in the reported case, supporting a neuronal migration defect linked to impaired cortical development/cytoskeletal regulation (cavalli2024heterozygoustruncatingvariant pages 1-3) | Human case report plus literature review; mechanistic support largely inferred from prior experimental biology summarized in the report (cavalli2024heterozygoustruncatingvariant pages 1-3) | No validated targeted therapy in available evidence; principal value is expanding diagnostic panels and mechanistic stratification | GO:0000226 microtubule cytoskeleton organization; GO:0001764 neuron migration; GO:0007254 JNK cascade; GO:0030154 cell differentiation | CL:0011115 neural progenitor cell; CL:0000540 neuron |
| NEDD4L / AKT-mTOR axis | Ubiquitin signaling with AKT-mTOR deregulation affecting cortical development and migration | Pathogenic **NEDD4L** variants are summarized as causing AKT-mTOR deregulation in PVNH-related disease references (paliotti2022epilepsyinindividuals pages 44-47, bressan2023metforminrescuesmigratory pages 10-11) | Abnormal neuronal migration/cortical development contributing to PVNH phenotypes; specific downstream cellular details are less developed in the available evidence than for DCHS1/FAT4 (paliotti2022epilepsyinindividuals pages 44-47, bressan2023metforminrescuesmigratory pages 10-11) | Human genetic/clinical literature summaries; mechanistic mention in review/thesis evidence rather than a dedicated primary mechanistic paper in available context (paliotti2022epilepsyinindividuals pages 44-47, bressan2023metforminrescuesmigratory pages 10-11) | Rapamycin-like/autophagy-activating approaches are noted as partially rescuing migration in related cited contexts, supporting mTOR-pathway modulation as a hypothesis-generating avenue (bressan2023metforminrescuesmigratory pages 10-11) | GO:0010506 regulation of autophagy; GO:0032008 positive regulation of TOR signaling; GO:0001764 neuron migration; GO:0046777 protein autoubiquitination | CL:0011115 neural progenitor cell; CL:0000540 neuron |


*Table: This table summarizes the main mechanistic axes currently implicated in periventricular nodular heterotopia/periventricular heterotopia, linking genes to cellular defects, evidence systems, and translational implications. It is useful for mapping disease biology into structured pathway, cell type, and therapeutic hypothesis annotations.*

---

## 7. Anatomical structures affected
### 7.1 Primary organs/systems
- **Central nervous system (brain)** is primary, especially periventricular region surrounding the lateral ventricles. (paliotti2022epilepsyinindividualsa pages 8-13)

### 7.2 Specific anatomical localization (example UBERON suggestions)
- **Lateral ventricle / ventricular zone region** (UBERON suggestion: lateral ventricle of brain)
- **Periventricular region / subependymal zone**

(UBERON IDs are not present in the retrieved evidence corpus; terms above are suggested for ontology mapping based on described anatomy.) (paliotti2022epilepsyinindividualsa pages 8-13)

### 7.3 Extra-CNS involvement (FLNA deficiency)
- Cardiovascular system involvement (valvular disease, aortic root involvement, congenital lesions) is common in FLNA LoF cohorts, motivating surveillance. (rijckmans2024counselingindividualswith pages 6-8, rijckmans2024counselingindividualswith pages 5-6)

---

## 8. Temporal development
- **Onset:** PVNH is congenital (developmental), but clinical presentation often occurs later with seizure onset in childhood/adolescence; mean seizure onset 7.9 years in one cohort and median 17 years in a FLNA LoF cohort. (paliotti2022epilepsyinindividualsa pages 26-31, rijckmans2024counselingindividualswith pages 5-6)
- **Course:** Variable—ranging from self-limited epilepsy (10% in one cohort) to drug-resistant epilepsy (23% overall; enriched in multiple bilateral PVNH). (paliotti2022epilepsyinindividualsa pages 26-31)

---

## 9. Inheritance and population
### 9.1 Inheritance patterns
- **X-linked dominant:** FLNA-associated PVNH/FLNA deficiency, with reduced male viability and frequent female predominance. (lange201547patientswith pages 1-2, cannaerts2018flnamutationsin pages 1-3)
- **Autosomal dominant (de novo):** ARF1-related disorder (17 unrelated individuals with de novo variants). (agathe2023arf1relateddisorderphenotypic pages 1-1)

### 9.2 Penetrance/expressivity and mosaicism
- Incomplete penetrance for seizures is supported by seizure-free FLNA variant carriers (e.g., 10 carriers seizure-free at median age 19.7 years in a 47-person cohort). (lange201547patientswith pages 1-2)
- Mosaicism and germline mosaicism are documented and relevant for recurrence risk and male survival. (lapointe2014germlinemosaicismin pages 1-3, lange201547patientswith pages 4-6)

### 9.3 Epidemiology and prevalence/incidence
No population-level prevalence or incidence rates were available in the retrieved evidence corpus. (rijckmans2024counselingindividualswith pages 3-5)

---

## 10. Diagnostics
### 10.1 Imaging
MRI is the central diagnostic tool. In a 2024 case report, the authors state: “Head magnetic resonance imaging (MRI) is the most sensitive neuroimaging method,” and describe “bilateral subependymal nodular irregularities lining the lateral ventricles, with similar signal evolution to grey matter.” (fernandes2024periventricularnodularheterotopias pages 1-2)

MRI pattern stratification is clinically useful. One cohort classified PVNH into four patterns (anterior predominant bilateral symmetric; inferior; bilateral asymmetric; unilateral focal) and reported FLNA-positive cases were predominantly anterior bilateral symmetric (8/9). (lu2022theclinicaland pages 1-8)

An MRI figure demonstrating bilateral periventricular nodules (arrows) is available from the retrieved case report. (fernandes2024periventricularnodularheterotopias media ff0bd3e1)

### 10.2 EEG
EEG abnormalities are frequent: in a 100-person cohort, EEG was abnormal in 95% (92/99), with focal, multifocal, and generalized patterns. (paliotti2022epilepsyinindividualsa pages 26-31)

### 10.3 Genetic testing approaches
Real-world diagnostic testing in PVNH includes sequencing plus CNV detection:
- In a 100-person cohort: single-gene sequencing (n=17), clinical panels (n=19), WES (n=6), and CMA (n=20) were used; eight pathogenic/likely pathogenic single-gene variants and CNVs (including pathogenic CNVs) were identified. (paliotti2022epilepsyinindividualsa pages 26-31)
- In FLNA-focused cohorts: FLNA testing included Sanger sequencing and MLPA, and/or NGS panels. (lange201547patientswith pages 1-2, rijckmans2025"phenotypicandgenotypic pages 6-10)

### 10.4 Differential diagnosis
The retrieved evidence supports a radiologic distinction between **PVNH-only** vs **PVNH-plus** (PVNH with additional malformations such as corpus callosum abnormalities, polymicrogyria, ventriculomegaly, hippocampal abnormalities). (paliotti2022epilepsyinindividualsa pages 26-31)

A comprehensive differential diagnosis list (e.g., tubulinopathies, other MCDs) was not extractable from the retrieved corpus in this run.

---

## 11. Outcome / prognosis
- **Epilepsy outcomes:** In the 100-person cohort: 10% self-limited, 35% pharmacoresponsive (mean seizure-free 4.5 years), 55% uncontrolled at interview; 23% drug-resistant. (paliotti2022epilepsyinindividualsa pages 26-31)
- **Prognostic imaging correlates:** Drug resistance enriched in multiple bilateral PVNH (39% of that subgroup). (paliotti2022epilepsyinindividualsa pages 26-31)
- **Neurodevelopment:** Many FLNA-PVNH individuals have normal cognition or mild impairment; one FLNA cohort emphasized generally reassuring educational outcomes (22/24 attending regular school). (lange201547patientswith pages 1-2)
- **Potential mortality risks in FLNA deficiency:** Cardiovascular disease can be progressive; fatal aortic rupture has been reported at smaller-than-expected diameters, supporting routine cardiological follow-up. (rijckmans2024counselingindividualswith pages 6-8, rijckmans2025"phenotypicandgenotypic pages 10-14)

---

## 12. Treatment
### 12.1 Pharmacotherapy (symptomatic)
In a 100-person PVNH cohort:
- **Clobazam** was reported with high efficacy (PVNH-only 76% [13/17]; PVNH-plus 64% [16/25]). (paliotti2022epilepsyinindividualsa pages 26-31)
- **Levetiracetam** “provided seizure freedom in 14 cases,” often as monotherapy in responders. (paliotti2022epilepsyinindividualsa pages 26-31)

**MAXO suggestions:** antiseizure medication therapy (MAXO term suggestion: anticonvulsant therapy), epilepsy management.

### 12.2 Device/dietary therapies
VNS and ketogenic diet were tried in 14 individuals; 71% reported no benefit and none achieved seizure freedom. (paliotti2022epilepsyinindividualsa pages 26-31)

**MAXO suggestions:** vagus nerve stimulation (device-based neuromodulation), ketogenic diet therapy.

### 12.3 Surgical and interventional epilepsy treatment
- In a 100-person cohort, 12 underwent epilepsy surgery; outcomes were mixed: 2 seizure-free (on ASMs), 7 improved, 3 no clear benefit; radiofrequency thermocoagulation of nodules was performed in 4. (paliotti2022epilepsyinindividuals pages 26-31)
- SEEG-guided thermocoagulation is a key real-world implementation; one report cites an overall efficacy of ~65% for SEEG-guided THC in PVNH, and in FLNA-positive PVNH cases outcomes varied (Engel I–II in 2/4, Engel III in 1/4, Engel IV in 1/4). (clerck2025stereoelectroencephalographicthermocoagulationin pages 1-2)

**MAXO suggestions:** stereoelectroencephalography, radiofrequency ablation/thermocoagulation, epilepsy surgery.

### 12.4 Experimental / mechanism-based approaches (preclinical)
A major 2023 mechanistic study in DCHS1/FAT4-related periventricular heterotopia demonstrated autophagy-linked migration defects in patient-derived hNPCs and showed that metformin promoted migration rescue, supporting an AMPK–autophagy therapeutic hypothesis in select genetic subtypes (preclinical). (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 11-12)

---

## 13. Prevention
No established primary prevention exists for genetically determined PVNH in the retrieved evidence. Preventive approaches are primarily **genetic counseling** and **surveillance for complications** (e.g., cardiology in FLNA deficiency). (rijckmans2024counselingindividualswith pages 6-8, lapointe2014germlinemosaicismin pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring veterinary PVNH analogs were identified in the retrieved evidence.

---

## 15. Model organisms and experimental systems
PVNH/heterotopia modeling spans invertebrate, rodent, and human stem-cell systems:
- **Drosophila (TMTC3 ortholog):** neuron-specific knockdown increased susceptibility to induced seizures; rescue by neuron-specific human TMTC3 expression supports conserved seizure biology. (farhan2017identificationofa pages 1-2)
- **Human iPSC/hNPC and cortical organoids:** patient-derived hNPCs and organoids for DCHS1/FAT4 periventricular heterotopia; xenografting hNPCs into mouse brain enabled in vivo migration assays and metformin rescue experiments. (bressan2023metforminrescuesmigratory pages 1-2)
- **Rodent FLNA models:** mouse FLNA loss-of-function models do not consistently reproduce the human neuronal migration defect/PVNH phenotype, indicating interspecies limitations; rat approaches may be more comparable but resource-intensive. (donada2018physiopathologicalmechanismsof pages 166-168, benadero2019geneticalterationsin pages 105-109)

---

## Recent developments (2023–2024 highlights)
1. **ARF1-related disorder (2023, Journal of Medical Genetics):** expanded from a handful of cases to a 17-individual cohort with de novo ARF1 variants and recurrent PVNH, seizures, microcephaly, and ID, with mechanistic linkage to vesicle formation at the trans-Golgi. URL: https://doi.org/10.1136/jmg-2022-108803 (Apr 2023). (agathe2023arf1relateddisorderphenotypic pages 1-1, agathe2023arf1relateddisorderphenotypic pages 1-2)
2. **Metformin/autophagy rescue in DCHS1/FAT4 periventricular heterotopia (2023, EMBO Molecular Medicine):** patient-derived hNPC migration deficits linked to altered autophagy and paxillin accumulation; metformin increased autophagic flux and restored migration in preclinical models. URL: https://doi.org/10.15252/emmm.202216908 (Aug 2023). (bressan2023metforminrescuesmigratory pages 1-2, bressan2023metforminrescuesmigratory pages 11-12)
3. **TAOK1 association with PVNH (2024, BMC Medical Genomics):** first report of a TAOK1-related NDD case with PVNH, supporting TAOK1’s role in neuronal migration/cytoskeleton biology. URL: https://doi.org/10.1186/s12920-024-01840-8 (Mar 2024). (cavalli2024heterozygoustruncatingvariant pages 1-3)
4. **FLNA LoF surveillance emphasis (2024 preprint):** cohort data underscore frequent epilepsy and cardiovascular involvement and highlight that “guidelines are lacking,” motivating multidisciplinary follow-up and cardiologic screening. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1 (Oct 2024). (rijckmans2024counselingindividualswith pages 1-3, rijckmans2024counselingindividualswith pages 6-8)

---

## Real-world implementations / research infrastructure
- **EPGP (NCT00552045):** A completed, large observational epilepsy genetics project (enrollment 4,150) that explicitly includes “Periventricular Heterotopias” among conditions studied; collected whole-blood DNA and required parent participation for MCD cases. https://clinicaltrials.gov/study/NCT00552045 (first posted 2007). (NCT00552045 chunk 1)
- **RID functional testing for VUS (NCT05696912):** Diagnostic-focused study to reclassify VUS via RNA-seq/minigene/luciferase functional assays; includes PVNH among conditions. https://clinicaltrials.gov/study/NCT05696912 (first posted 2023). (NCT05696912 chunk 1)

---

## Notes on citation requirements (PMIDs)
Where possible, this report cites primary literature and includes DOIs/URLs with publication months/years. However, **PMID values were not present in the retrieved text extracts for this run**, so PMIDs cannot be reliably provided without external database lookup. All major claims are nevertheless tied to the provided evidence excerpts via the in-run citation IDs.


References

1. (agathe2023arf1relateddisorderphenotypic pages 1-2): Jean-Madeleine de Sainte Agathe, Ben Pode-Shakked, Sophie Naudion, Vincent Michaud, Benoit Arveiler, Patricia Fergelot, Jean Delmas, Boris Keren, Céline Poirsier, Fowzan S Alkuraya, Brahim Tabarki, Eric Bend, Kellie Davis, Martina Bebin, Michelle L Thompson, Emily M Bryant, Matias Wagner, Iris Hannibal, Jerica Lenberg, Martin Krenn, Kristen M Wigby, Jennifer R Friedman, Maria Iascone, Anna Cereda, Térence Miao, Eric LeGuern, Emanuela Argilli, Elliott Sherr, Oana Caluseriu, Timothy Tidwell, Pinar Bayrak-Toydemir, Caroline Hagedorn, Melanie Brugger, Katharina Vill, Francois-Dominique Morneau-Jacob, Wendy Chung, Kathryn N Weaver, Joshua W Owens, Ammar Husami, Bimal P Chaudhari, Brandon S Stone, Katie Burns, Rachel Li, Iris M de Lange, Margaux Biehler, Emmanuelle Ginglinger, Bénédicte Gérard, Rolf W Stottmann, and Aurélien Trimouille. Arf1-related disorder: phenotypic and molecular spectrum. Journal of Medical Genetics, 60:999-1005, Apr 2023. URL: https://doi.org/10.1136/jmg-2022-108803, doi:10.1136/jmg-2022-108803. This article has 13 citations and is from a domain leading peer-reviewed journal.

2. (cavalli2024heterozygoustruncatingvariant pages 1-3): Anna Cavalli, Stefano Giuseppe Caraffi, Susanna Rizzi, Gabriele Trimarchi, Manuela Napoli, Daniele Frattini, Carlotta Spagnoli, Livia Garavelli, and Carlo Fusco. Heterozygous truncating variant of taok1 in a boy with periventricular nodular heterotopia: a case report and literature review of taok1-related neurodevelopmental disorders. BMC Medical Genomics, Mar 2024. URL: https://doi.org/10.1186/s12920-024-01840-8, doi:10.1186/s12920-024-01840-8. This article has 4 citations and is from a peer-reviewed journal.

3. (bressan2023metforminrescuesmigratory pages 1-2): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

4. (parrini2004mosaicmutationsof pages 1-2): Elena Parrini, Davide Mei, Micheal Wright, Thomas Dorn, and Renzo Guerrini. Mosaic mutations of the fln1 gene cause a mild phenotype in patients with periventricular heterotopia. Neurogenetics, 5:191-196, Jul 2004. URL: https://doi.org/10.1007/s10048-004-0187-y, doi:10.1007/s10048-004-0187-y. This article has 52 citations and is from a peer-reviewed journal.

5. (fernandes2024periventricularnodularheterotopias pages 1-2): Andreia Fernandes, Mafalda J Pereira, Íris Oliveira, André M Travessa, José Drago, and Carla Mendonça. Periventricular nodular heterotopias induced-seizures in an adolescent. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75272, doi:10.7759/cureus.75272. This article has 0 citations.

6. (lu2022theclinicaland pages 1-8): Yan-Ting Lu, Chung-Yao Hsu, Yo-Tsen Liu, Chung-Kin Chan, Yao-Chung Chuang, Chih-Hsiang Lin, Kai-Ping Chang, Chen-Jui Ho, Ching-Ching Ng, Kheng-Seang Lim, and Meng-Han Tsai. The clinical and imaging features of flna positive and negative periventricular nodular heterotopia. Biomedical Journal, 45:542-548, Jun 2022. URL: https://doi.org/10.1016/j.bj.2021.05.003, doi:10.1016/j.bj.2021.05.003. This article has 11 citations.

7. (gerlevik2022computationalanalysisof pages 1-2): Umut Gerlevik, Ceren Saygı, Hakan Cangül, Aslı Kutlu, Erdal Fırat Çaralan, Yasemin Topçu, Nesrin Özören, and Osman Uğur Sezerman. Computational analysis of missense filamin-a variants, including the novel p.arg484gln variant of two brothers with periventricular nodular heterotopia. PLOS ONE, 17:e0265400, May 2022. URL: https://doi.org/10.1371/journal.pone.0265400, doi:10.1371/journal.pone.0265400. This article has 2 citations and is from a peer-reviewed journal.

8. (paliotti2022epilepsyinindividualsa pages 8-13): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

9. (rijckmans2024counselingindividualswith pages 1-3): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

10. (lange201547patientswith pages 1-2): Max Lange, Burkhard Kasper, Axel Bohring, Frank Rutsch, Gerhard Kluger, Sabine Hoffjan, Stephanie Spranger, Anne Behnecke, Andreas Ferbert, Andreas Hahn, Barbara Oehl-Jaschkowitz, Luitgard Graul-Neumann, Katharina Diepold, Isolde Schreyer, Matthias K. Bernhard, Franziska Mueller, Ulrike Siebers-Renelt, Ana Beleza-Meireles, Goekhan Uyanik, Sandra Janssens, Eugen Boltshauser, Juergen Winkler, Gerhard Schuierer, and Ute Hehr. 47 patients with flna associated periventricular nodular heterotopia. Orphanet Journal of Rare Diseases, Oct 2015. URL: https://doi.org/10.1186/s13023-015-0331-9, doi:10.1186/s13023-015-0331-9. This article has 116 citations and is from a peer-reviewed journal.

11. (paliotti2022epilepsyinindividualsa pages 26-31): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

12. (bressan2023metforminrescuesmigratory pages 9-10): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

13. (NCT00552045 chunk 1):  Epilepsy Phenome/Genome Project. University of California, San Francisco. 2007. ClinicalTrials.gov Identifier: NCT00552045

14. (NCT05696912 chunk 1):  Functional Tests to Resolve Unsolved Rare Diseases. Rares.. University Hospital, Bordeaux. 2023. ClinicalTrials.gov Identifier: NCT05696912

15. (cannaerts2018flnamutationsin pages 1-3): Elyssa Cannaerts, Anju Shukla, Mensuda Hasanhodzic, Maaike Alaerts, Dorien Schepers, Lut Van Laer, Katta M. Girisha, Iva Hojsak, Bart Loeys, and Aline Verstraeten. Flna mutations in surviving males presenting with connective tissue findings: two new case reports and review of the literature. BMC Medical Genetics, Sep 2018. URL: https://doi.org/10.1186/s12881-018-0655-0, doi:10.1186/s12881-018-0655-0. This article has 38 citations and is from a peer-reviewed journal.

16. (lange201547patientswith pages 4-6): Max Lange, Burkhard Kasper, Axel Bohring, Frank Rutsch, Gerhard Kluger, Sabine Hoffjan, Stephanie Spranger, Anne Behnecke, Andreas Ferbert, Andreas Hahn, Barbara Oehl-Jaschkowitz, Luitgard Graul-Neumann, Katharina Diepold, Isolde Schreyer, Matthias K. Bernhard, Franziska Mueller, Ulrike Siebers-Renelt, Ana Beleza-Meireles, Goekhan Uyanik, Sandra Janssens, Eugen Boltshauser, Juergen Winkler, Gerhard Schuierer, and Ute Hehr. 47 patients with flna associated periventricular nodular heterotopia. Orphanet Journal of Rare Diseases, Oct 2015. URL: https://doi.org/10.1186/s13023-015-0331-9, doi:10.1186/s13023-015-0331-9. This article has 116 citations and is from a peer-reviewed journal.

17. (agathe2023arf1relateddisorderphenotypic pages 1-1): Jean-Madeleine de Sainte Agathe, Ben Pode-Shakked, Sophie Naudion, Vincent Michaud, Benoit Arveiler, Patricia Fergelot, Jean Delmas, Boris Keren, Céline Poirsier, Fowzan S Alkuraya, Brahim Tabarki, Eric Bend, Kellie Davis, Martina Bebin, Michelle L Thompson, Emily M Bryant, Matias Wagner, Iris Hannibal, Jerica Lenberg, Martin Krenn, Kristen M Wigby, Jennifer R Friedman, Maria Iascone, Anna Cereda, Térence Miao, Eric LeGuern, Emanuela Argilli, Elliott Sherr, Oana Caluseriu, Timothy Tidwell, Pinar Bayrak-Toydemir, Caroline Hagedorn, Melanie Brugger, Katharina Vill, Francois-Dominique Morneau-Jacob, Wendy Chung, Kathryn N Weaver, Joshua W Owens, Ammar Husami, Bimal P Chaudhari, Brandon S Stone, Katie Burns, Rachel Li, Iris M de Lange, Margaux Biehler, Emmanuelle Ginglinger, Bénédicte Gérard, Rolf W Stottmann, and Aurélien Trimouille. Arf1-related disorder: phenotypic and molecular spectrum. Journal of Medical Genetics, 60:999-1005, Apr 2023. URL: https://doi.org/10.1136/jmg-2022-108803, doi:10.1136/jmg-2022-108803. This article has 13 citations and is from a domain leading peer-reviewed journal.

18. (paliotti2022epilepsyinindividuals pages 17-22): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

19. (paliotti2022epilepsyinindividualsa pages 17-22): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

20. (rijckmans2024counselingindividualswith pages 5-6): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

21. (rijckmans2024counselingindividualswith pages 6-8): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

22. (rijckmans2025"phenotypicandgenotypic pages 1-6): Ellen Rijckmans, Lars De Strooper, K. Keymolen, Jessica Rosenblum, B. Loeys, M. Meuwissen, Anna C. Jansen, and K. Stouffs. "phenotypic and genotypic insights, counseling strategies, and follow-up in 24 individuals with filamin a deficiency: findings from a retrospective cohort study". Acta neurologica Belgica, Aug 2025. URL: https://doi.org/10.1007/s13760-025-02858-0, doi:10.1007/s13760-025-02858-0. This article has 0 citations and is from a peer-reviewed journal.

23. (rijckmans2025"phenotypicandgenotypic pages 6-10): Ellen Rijckmans, Lars De Strooper, K. Keymolen, Jessica Rosenblum, B. Loeys, M. Meuwissen, Anna C. Jansen, and K. Stouffs. "phenotypic and genotypic insights, counseling strategies, and follow-up in 24 individuals with filamin a deficiency: findings from a retrospective cohort study". Acta neurologica Belgica, Aug 2025. URL: https://doi.org/10.1007/s13760-025-02858-0, doi:10.1007/s13760-025-02858-0. This article has 0 citations and is from a peer-reviewed journal.

24. (rijckmans2025"phenotypicandgenotypic pages 10-14): Ellen Rijckmans, Lars De Strooper, K. Keymolen, Jessica Rosenblum, B. Loeys, M. Meuwissen, Anna C. Jansen, and K. Stouffs. "phenotypic and genotypic insights, counseling strategies, and follow-up in 24 individuals with filamin a deficiency: findings from a retrospective cohort study". Acta neurologica Belgica, Aug 2025. URL: https://doi.org/10.1007/s13760-025-02858-0, doi:10.1007/s13760-025-02858-0. This article has 0 citations and is from a peer-reviewed journal.

25. (lapointe2014germlinemosaicismin pages 1-3): Monique M LaPointe, Elizabeth L Spriggs, and Aizeddin A Mhanni. Germline mosaicism in x-linked periventricular nodular heterotopia. BMC Neurology, 14:125-125, Jun 2014. URL: https://doi.org/10.1186/1471-2377-14-125, doi:10.1186/1471-2377-14-125. This article has 11 citations and is from a peer-reviewed journal.

26. (bressan2023metforminrescuesmigratory pages 6-7): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

27. (paliotti2022epilepsyinindividuals pages 44-47): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

28. (bressan2023metforminrescuesmigratory pages 11-12): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

29. (bressan2023metforminrescuesmigratory pages 7-9): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

30. (bressan2023metforminrescuesmigratory pages 10-11): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

31. (rijckmans2024counselingindividualswith pages 3-5): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

32. (fernandes2024periventricularnodularheterotopias media ff0bd3e1): Andreia Fernandes, Mafalda J Pereira, Íris Oliveira, André M Travessa, José Drago, and Carla Mendonça. Periventricular nodular heterotopias induced-seizures in an adolescent. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.75272, doi:10.7759/cureus.75272. This article has 0 citations.

33. (paliotti2022epilepsyinindividuals pages 26-31): K Paliotti. Epilepsy in individuals with periventricular nodular heterotopia: defining the clinical phenotypic spectrum and underlying molecular causes. Unknown journal, 2022.

34. (clerck2025stereoelectroencephalographicthermocoagulationin pages 1-2): Lucie De Clerck, Veronica Pelliccia, Romain Carron, Agnès Trébuchon, Laura Tassi, Fabrice Bartolomei, and Francesca Pizzo. Stereoelectroencephalographic thermocoagulation in flna ‐positive heterotopia: is it an effective treatment? Epilepsia, 66:e29-e34, Dec 2025. URL: https://doi.org/10.1111/epi.18231, doi:10.1111/epi.18231. This article has 1 citations and is from a domain leading peer-reviewed journal.

35. (farhan2017identificationofa pages 1-2): Sali M. K. Farhan, K. Nixon, Michelle Everest, Michelle Everest, T. Edwards, Shirley Q. Long, Dmitri Segal, Maria J Knip, H. Arts, H. Arts, R. Chakrabarti, Jian Wang, John F. Robinson, Donald Lee, S. Mirsattari, C. Rupar, V. Siu, Michael O. Poulter, Michael O. Poulter, R. Hegele, and Jamie M. Kramer. Identification of a novel synaptic protein, tmtc3, involved in periventricular nodular heterotopia with intellectual disability and epilepsy. Human Molecular Genetics, 26:4278-4289, Aug 2017. URL: https://doi.org/10.1093/hmg/ddx316, doi:10.1093/hmg/ddx316. This article has 48 citations and is from a domain leading peer-reviewed journal.

36. (donada2018physiopathologicalmechanismsof pages 166-168): A Donada. Physiopathological mechanisms of two congenical platelet disorders: filaminopathy-a and ankrd26-related-thrombocytopenia 5thc2. Unknown journal, 2018.

37. (benadero2019geneticalterationsin pages 105-109): C Llinares Benadero. Genetic alterations in cortical development as a cause of epileptogenic disorders. Unknown journal, 2019.