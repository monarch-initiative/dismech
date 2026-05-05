---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T16:49:03.378039'
end_time: '2026-05-05T17:02:36.752791'
duration_seconds: 813.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multisystemic smooth muscle dysfunction syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multisystemic smooth muscle dysfunction syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Multisystemic smooth muscle dysfunction syndrome** covering all of the
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
- **Disease Name:** Multisystemic smooth muscle dysfunction syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Multisystemic smooth muscle dysfunction syndrome** covering all of the
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


# Comprehensive Disease Characteristics Report: Multisystemic Smooth Muscle Dysfunction Syndrome (MSMDS)

## Executive summary
Multisystemic smooth muscle dysfunction syndrome (MSMDS; also called smooth muscle dysfunction syndrome, SMDS) is an ultrarare, typically de novo, autosomal-dominant smooth muscle disorder classically caused by heterozygous missense substitution of ACTA2 arginine 179 (ACTA2 p.Arg179*) and characterized by congenital mydriasis plus early congenital heart disease (patent ductus arteriosus/aortopulmonary window), early-onset aortic disease, and a distinctive cerebral arteriopathy with small-vessel white-matter injury and large-artery stenosis/occlusion. Quantitative natural-history data from a 33-patient cohort demonstrate very high burdens of brain MRI abnormalities (e.g., 95% white-matter lesions) and early aortic events (36% by a median age of 14; 100% penetrance of aortic disease by age 25), underpinning recommendations for aggressive, multidisciplinary surveillance. (regalado2018clinicalhistoryand pages 1-2)

A major recent development is that an MSMDS phenotype can also be produced by a de novo noncoding MIR145 (miR-145-5p seed) variant, functionally converging on loss of smooth muscle contractile/cytoskeletal programs. (cardenas2023aseedsequence pages 1-3)

---

## 1. Disease information
### 1.1 Definition and overview
MSMDS is a multisystem disorder of smooth muscle-dependent organs, classically due to heterozygous ACTA2 Arg179 substitutions. It features ocular (congenital mydriasis), cardiovascular (PDA/AP window, thoracic aortic aneurysm/dissection), cerebrovascular disease (moyamoya-like/steno-occlusive arteriopathy plus small-vessel white matter lesions), pulmonary arterial hypertension, and additional smooth muscle organ dysfunction (e.g., bladder hypotonia, gut hypoperistalsis). (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2)

### 1.2 Key identifiers
- **OMIM (MIM) disease number:** **613834** (referred to as “MSMDS/SMDS/MSMD syndrome” depending on source) (kaw2022expandingacta2genotypes pages 1-2, cardenas2023aseedsequence pages 1-3, laar2019europeanreferencenetwork pages 2-4)
- **MONDO ID:** not retrieved from the tool-accessible full text in this run (flagged as unavailable).
- **Orphanet ID:** not retrieved from tool-accessible full text in this run (flagged as unavailable).
- **ICD-10/ICD-11 / MeSH:** not retrieved from tool-accessible full text in this run (flagged as unavailable).

### 1.3 Synonyms and alternative names (observed in sources)
- Multisystemic smooth muscle dysfunction syndrome (MSMDS) (li2025casereportmultisystemic pages 2-4, cardenas2023aseedsequence pages 1-3)
- Multisystem smooth muscle dysfunction syndrome (cardenas2023aseedsequence pages 1-3)
- Smooth muscle dysfunction syndrome (SMDS/SMDS) (regalado2018clinicalhistoryand pages 1-2)
- “MSMD syndrome” (multisystem smooth muscle dysfunction) used in ACTA2 consensus context (laar2019europeanreferencenetwork pages 1-2)

### 1.4 Evidence source types
Evidence in this report is derived from:
- Aggregated cohort natural history and management recommendations (human clinical; multicenter series). (regalado2018clinicalhistoryand pages 1-2, regalado2018clinicalhistoryand pages 8-9)
- Case reports/literature reviews (human clinical). (yang2021acta2mutationis pages 5-6, li2025casereportmultisystemic pages 2-4, logeswaran2017twopatientswith pages 3-4)
- Consensus management guidance for ACTA2 vasculopathy (expert consensus). (laar2019europeanreferencenetwork pages 2-4, laar2019europeanreferencenetwork pages 4-6, laar2019europeanreferencenetwork pages 6-7)
- Mechanistic cellular/genomic studies (iPSC/SMC models; human tissue single-cell; mouse models). (kwartler2023nuclearsmoothmuscle pages 7-11, kwartler2023nuclearsmoothmuscle pages 42-46, milewicz2023augmentingmitochondrialrespiration pages 6-9)
- ClinicalTrials.gov trial registry entries (real-world implementation and translational research). (NCT06280482 chunk 1)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary genetic cause (classic MSMDS/SMDS):** heterozygous missense variants in **ACTA2** that alter **arginine 179** (e.g., p.Arg179His) affecting smooth muscle α-actin. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)

**Expanded genetic cause (2023):** a **de novo MIR145** seed-sequence variant (miR-145-5p) was reported to cause an MSMDS phenotype, expanding the locus beyond ACTA2 while converging on smooth muscle contractile/cytoskeletal regulation. (cardenas2023aseedsequence pages 1-3)

### 2.2 Risk factors
- **Genetic:** presence of pathogenic ACTA2 Arg179 substitutions (often de novo in the classic syndrome). (regalado2018clinicalhistoryand pages 1-2)
- **Sex (case-ascertained):** a 2024 compilation reported 66.7% of published cases were female, but this is not population-based and may reflect ascertainment/reporting bias. (li2025casereportmultisystemic pages 2-4)

**Environmental risk factors:** none established in the retrieved sources; MSMDS is largely monogenic in classic cases. (regalado2018clinicalhistoryand pages 1-2, cardenas2023aseedsequence pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
Not established in the retrieved sources.

---

## 3. Phenotypes (with suggested HPO terms)
### 3.1 Core phenotype spectrum and frequency/quantitative data
A high-quality 33-patient natural-history study provides cohort-level frequencies for major findings and outcomes. (regalado2018clinicalhistoryand pages 1-2)

Key quantitative features are summarized in the artifact table below.

| Category | Finding | Quantitative detail | Notes | Citation |
|---|---|---:|---|---|
| Disease concept | Multisystemic/smooth muscle dysfunction syndrome (MSMDS/SMDS) due to ACTA2 Arg179 alterations | Cohort n=33; median age 12 years in major natural-history series | Severe childhood-onset multisystem smooth-muscle disorder | (regalado2018clinicalhistoryand pages 1-2) |
| Inheritance | Usually autosomal dominant, but most classic Arg179 cases are de novo heterozygous | “Most”/nearly all reported classic cases de novo | Family transmission and somatic mosaicism have also been reported for non-Arg179 overlap phenotypes | (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2) |
| Typical causal variants | ACTA2 Arg179 substitutions | Commonly p.Arg179His; also p.Arg179Cys, p.Arg179Leu, p.Arg179Ser, p.Arg179Gly | Arg179 substitutions define the classic severe syndrome; other ACTA2 missense variants can overlap with MSMDS | (kaw2022expandingacta2genotypes pages 1-2, yang2021acta2mutationis pages 5-6, regalado2018clinicalhistoryand pages 1-2) |
| Core ocular feature | Congenital mydriasis / fixed dilated pupils | 100% in 33-patient series; 37/37 in literature review | Often present at birth; strong diagnostic clue | (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6) |
| Congenital heart disease | Patent ductus arteriosus (PDA) or aortopulmonary window | PDA in 35/37 (94.6%) in review; infancy presentation typical in cohort | Hemodynamically important PDA/AP window is a hallmark neonatal feature | (yang2021acta2mutationis pages 5-6, regalado2018clinicalhistoryand pages 1-2) |
| Cerebral small-vessel disease | Periventricular white-matter lesions | 95% | MRI hallmark of ACTA2 Arg179 syndrome | (regalado2018clinicalhistoryand pages 1-2) |
| Cerebrovascular large-artery disease | Intracranial artery stenosis | 77% | Moyamoya-like arteriopathy/arterial straightening-stenosis pattern | (regalado2018clinicalhistoryand pages 1-2) |
| Ischemic complications | Ischemic stroke | 27% in 33-patient cohort; seizures in 4/37 (10.8%) in literature review | Neurologic morbidity begins in childhood in many patients | (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6) |
| Seizures | Epileptic seizures | 18% in 33-patient cohort | Likely secondary to cerebrovascular and white-matter injury | (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6) |
| Aortic disease | Thoracic aortic aneurysm repair or dissection (“aortic event”) | 12/33 (36%) at median age 14 years | Aortic disease reached full penetrance by age 25 years in the cohort | (regalado2018clinicalhistoryand pages 1-2) |
| Peripheral vasculopathy | Axillary artery aneurysm with thromboembolism | 3/33 (9%) | Illustrates systemic arterial involvement beyond the aorta/cerebral circulation | (regalado2018clinicalhistoryand pages 1-2) |
| Mortality | Deaths from aortic, pulmonary, stroke, or unknown causes | 9/33; age at death 0.5–32 years | Confirms high early-life morbidity and mortality | (regalado2018clinicalhistoryand pages 1-2) |
| Other smooth-muscle organ involvement | Pulmonary hypertension, hypotonic bladder, gut hypoperistalsis/megacystis/hydronephrosis | Common but variably reported | Multisystem involvement reflects generalized smooth-muscle dysfunction | (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2) |
| Epidemiology | Reported global cases | ~90 cases reported by Apr 2024; 85 with genotype described | Ultra-rare disorder; published cases concentrated in Europe/USA | (li2025casereportmultisystemic pages 2-4) |
| Sex distribution | Female share among reported cases | 66.7% | Based on compiled case reports, not population-based registry data | (li2025casereportmultisystemic pages 2-4) |

| 2023–2024 development | Key finding | Quantitative / study detail | Why it matters | Citation |
|---|---|---:|---|---|
| 2023: MIR145 noncoding cause | De novo MIR145 seed-sequence variant (NR_029686.1:n.18C>A) caused an MSMDS phenotype | Variant absent from gnomAD; CADD 20.9 | First reported monogenic vascular disease causing MSMDS from a noncoding-gene mutation; links miR-145 to actin-cytoskeleton/SMC contractile program | (cardenas2023aseedsequence pages 1-3) |
| 2023: mechanistic insight | Mutant/knockdown miR-145 reduced transgelin, calponin, and α-SMA and disrupted stress-fiber induction | RNA-seq enriched for actin-cytoskeleton regulation | Supports a shared downstream contractile-cytoskeletal mechanism with ACTA2-related disease | (cardenas2023aseedsequence pages 1-3) |
| 2024: WES in moyamoya syndrome | WES identified MSMDS among genetic causes of moyamoya syndrome and highlighted modifier architecture | 13 patients with diverse genetic disorders; 2 had MSMDS | Reinforces value of exome sequencing in unexplained moyamoya-like disease and suggests modifier genes may shape cerebrovascular severity | (laar2019europeanreferencenetwork pages 1-2) |
| 2024–ongoing clinical translation | Nicotinamide riboside (NR) trial for moyamoya-like cerebrovascular disease in SMDS | NCT06280482; Phase 1; recruiting; target enrollment 15 | First interventional trial directly targeting a mechanistic pathway emerging from ACTA2 smooth-muscle metabolism studies | (laar2019europeanreferencenetwork pages 1-2) |


*Table: This table compiles the main quantitative clinical features of ACTA2 Arg179-related MSMDS/SMDS and highlights notable 2023–2024 developments, including the MIR145 discovery, WES evidence in moyamoya syndrome, and the ongoing nicotinamide riboside trial.*

### 3.2 Phenotype details and suggested HPO terms
Below are commonly reported phenotypes with suggested HPO terms and typical temporal patterns:

**Ocular**
- Congenital mydriasis / fixed dilated pupils (present at birth; highly penetrant). HPO: **HP:0007726 (Mydriasis)**; also consider iris anomalies. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)

**Cardiovascular / great vessels**
- Patent ductus arteriosus (often infancy). HPO: **HP:0001643 (Patent ductus arteriosus)**. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)
- Aortopulmonary window (reported in cohort abstract; infancy presentation). HPO: **HP:0004940 (Aortopulmonary window)**. (regalado2018clinicalhistoryand pages 1-2)
- Thoracic aortic aneurysm and/or dissection; early aortic events. HPO: **HP:0002647 (Aortic aneurysm)**; **HP:0002648 (Aortic dissection)**. (regalado2018clinicalhistoryand pages 1-2, regalado2018clinicalhistoryand pages 8-9)

**Cerebrovascular / neurologic**
- White matter lesions/leukoencephalopathy on MRI (very common in Arg179 cohort). HPO: **HP:0006975 (White matter abnormalities)**. (regalado2018clinicalhistoryand pages 1-2)
- Intracranial artery stenosis / moyamoya-like arteriopathy; distinctive “straight” arteries and absent basal collaterals. HPO: **HP:0002638 (Cerebral artery stenosis)**; **HP:0002138 (Moyamoya disease)** (note: phenotype overlaps but is distinguishable). (munot2012anoveldistinctive pages 1-2, munot2012anoveldistinctive pages 4-4)
- Ischemic stroke. HPO: **HP:0001297 (Stroke)**. (regalado2018clinicalhistoryand pages 1-2)
- Seizures. HPO: **HP:0001250 (Seizures)**. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)

**Pulmonary**
- Pulmonary arterial hypertension. HPO: **HP:0002092 (Pulmonary hypertension)**. (kaw2022expandingacta2genotypes pages 1-2, yang2021acta2mutationis pages 5-6)
- Interstitial lung disease (rare; ~13.3% in a 2024 compilation) with infantile presentation described. HPO: **HP:0006530 (Interstitial lung disease)**. (li2025casereportmultisystemic pages 2-4)

**Gastrointestinal / genitourinary smooth muscle dysfunction**
- Hypotonic bladder / megacystis / hydronephrosis. HPO: **HP:0000017 (Hydronephrosis)**; **HP:0000028 (Cryptorchidism)** may be relevant for male reproductive issues noted in counseling. (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 8-9)
- Gut hypoperistalsis/dysmotility. HPO: **HP:0002579 (Intestinal pseudo-obstruction)** and/or **HP:0002028 (Abdominal pain)** depending on clinical manifestation. (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2)

### 3.3 Quality-of-life impact
Direct standardized QoL metrics (e.g., EQ-5D, SF-36) were not present in retrieved sources. However, the multisystem nature and early cerebrovascular/aortic morbidity (strokes, seizures, aneurysm repair) imply substantial functional impact and need for multidisciplinary support. (regalado2018clinicalhistoryand pages 1-2, regalado2018clinicalhistoryand pages 8-9)

---

## 4. Genetic / molecular information
### 4.1 Causal genes
- **ACTA2** (smooth muscle α-actin; smooth muscle contractile apparatus component). (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2)
- **MIR145** (miR-145-5p; smooth muscle-enriched regulatory microRNA; 2023 single case). (cardenas2023aseedsequence pages 1-3)

### 4.2 Pathogenic variants (examples from retrieved sources)
**ACTA2**
- **c.536G>A (p.Arg179His; “R179H”)**: recurrent; common in literature review; associated with broad MSMDS phenotype including seizures. (yang2021acta2mutationis pages 5-6)
- Other Arg179 substitutions (e.g., Arg179Cys/Leu/Ser/Gly) are described as causal for the severe syndrome or classic features. (yang2021acta2mutationis pages 5-6, kaw2022expandingacta2genotypes pages 1-2)

**MIR145**
- **NR_029686.1:n.18C>A** (seed sequence nucleotide 3; de novo; absent from gnomAD; CADD 20.9). (cardenas2023aseedsequence pages 1-3)

Variant classification (ACMG/ClinVar), allele frequencies (beyond “absent from gnomAD” for MIR145), and HGNC IDs were not fully extractable from the retrieved texts and are therefore flagged as not retrieved.

### 4.3 Inheritance
Classic ACTA2 Arg179 MSMDS/SMDS is **autosomal dominant** with **a high proportion of de novo events** in reported cohorts. (regalado2018clinicalhistoryand pages 1-2)

### 4.4 Modifier genes / genetic modifiers
A 2024 exome-sequencing study of moyamoya syndrome (secondary moyamoya) identified multiple primary diagnoses including MSMDS and discussed modifier architecture (e.g., RNF213/MRVI1 in other syndromes; potential enrichment of rare variants in other vascular genes), supporting a broader concept that cerebrovascular severity can be modified by additional rare variants. (laar2019europeanreferencenetwork pages 1-2)

### 4.5 Epigenetic information
ACTA2 Arg179 variants are associated with altered chromatin states in smooth muscle cells, including altered chromatin accessibility and increased H3K27me3 at smooth muscle loci in ACTA2 R179C SMCs. (kwartler2023nuclearsmoothmuscle pages 24-28)

---

## 5. Environmental information
No specific environmental, lifestyle, or infectious triggers have been established for MSMDS in the retrieved sources. Disease manifestations appear primarily driven by the causal genetic alteration and downstream smooth muscle dysfunction. (regalado2018clinicalhistoryand pages 1-2, cardenas2023aseedsequence pages 1-3)

---

## 6. Mechanism / pathophysiology
### 6.1 Current understanding (causal chain)
**Upstream trigger:** ACTA2 Arg179 (or MIR145 seed) pathogenic variation → impaired smooth muscle cell (SMC) differentiation/contractile program and increased SMC plasticity. (kwartler2023nuclearsmoothmuscle pages 7-11, cardenas2023aseedsequence pages 1-3)

**Intermediate cellular consequences:** SMCs exhibit reduced expression of contractile proteins and increased proliferative/migratory behavior (“synthetic”/immature phenotype), leading to:
- **Occlusive lesions** and steno-occlusive arteriopathy in cerebral vessels (moyamoya-like pattern). (munot2012anoveldistinctive pages 1-2, munot2012anoveldistinctive pages 7-8)
- **Aneurysm/dissection predisposition** in elastic arteries including thoracic aorta (early aortic events). (regalado2018clinicalhistoryand pages 1-2)
- **Multiorgan smooth muscle dysfunction** affecting iris sphincter, ductus arteriosus closure, pulmonary vascular tone, gut motility, and bladder function. (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2)

**Clinical manifestations:** congenital mydriasis and PDA in infancy; progressive vasculopathy (aortic aneurysm/dissection; cerebral stenosis and strokes), pulmonary hypertension, and visceral dysmotility. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)

### 6.2 Recent mechanistic advances (prioritize 2023–2024)
**(A) Nuclear ACTA2 function and chromatin remodeling (2023)**
A 2023 Nature Cardiovascular Research study provides a mechanism connecting ACTA2 Arg179 variants to impaired SMC differentiation via loss of nuclear αSMA interactions with chromatin remodelers and promoters of SMC contractile genes. Key statements in the text include: **“the absence of nuclear αSMA in patients with ACTA2 R179 mutations leads to global defects in SMC differentiation”** and evidence that nuclear αSMA co-occupies promoters (e.g., Cnn1, Myh11, Tagln) with INO80/BAF remodeling complexes. (kwartler2023nuclearsmoothmuscle pages 7-11)

**(B) MIR145 seed-sequence variant as a convergent upstream regulator (2023)**
The 2023 JCI report shows a de novo MIR145 seed variant producing an MSMDS phenotype and functionally reducing cytoskeletal/contractile proteins (including α-SMA), with RNA-seq enrichment for “regulation of actin cytoskeleton,” strengthening the hypothesis that dysregulation of the actin cytoskeleton and SMC contractile differentiation is central and potentially targetable. (cardenas2023aseedsequence pages 1-3)

**(C) Metabolic modulation (OXPHOS) and nicotinamide riboside (NR) translational path (2023–2024)**
A 2023 preclinical study reports that Acta2R179C/+ SMCs exhibit immature features and that **NR** (a NAD+ precursor) increases oxygen consumption and reduces glycolytic flux, increases differentiation markers, decreases migration, and attenuates strokes and moyamoya-like occlusive lesions after carotid injury in mutant mice. (milewicz2023augmentingmitochondrialrespiration pages 6-9)

This preclinical work has translated into a 2024 Phase 1 trial (NCT06280482) in patients with ACTA2 arginine-179 SMDS to evaluate safety/tolerability and multiple physiologic endpoints (e.g., cerebral oxygenation/perfusion, cognition, autonomic symptoms) during 60 days of oral NR. (NCT06280482 chunk 1)

### 6.3 Pathways, processes, cell types (ontology suggestions)
**GO biological process (examples):**
- **Smooth muscle cell differentiation**; **regulation of actin cytoskeleton organization**; **cell migration**; **chromatin remodeling**; **vascular remodeling**. (kwartler2023nuclearsmoothmuscle pages 7-11, cardenas2023aseedsequence pages 1-3, milewicz2023augmentingmitochondrialrespiration pages 6-9)

**Cell types (CL suggestions):**
- **Vascular smooth muscle cell** (primary). (kwartler2023nuclearsmoothmuscle pages 7-11)

**Anatomical systems (UBERON suggestions):**
- **Aorta**, **cerebral arteries**, **iris sphincter muscle**, **ductus arteriosus**, **pulmonary artery**, **urinary bladder**, **intestine**. (regalado2018clinicalhistoryand pages 1-2, munot2012anoveldistinctive pages 1-2)

---

## 7. Anatomical structures affected
### 7.1 Organ-level involvement
Primary affected structures include:
- **Cardiovascular:** ductus arteriosus, thoracic aorta, systemic arteries (including peripheral aneurysms). (regalado2018clinicalhistoryand pages 1-2)
- **CNS vasculature and brain:** terminal internal carotids and intracranial arteries with distinctive straight course and stenosis/occlusion; white matter injury and infarcts. (munot2012anoveldistinctive pages 1-2, munot2012anoveldistinctive pages 4-4)
- **Eye:** iris sphincter/pupil control. (regalado2018clinicalhistoryand pages 1-2)
- **Pulmonary vasculature/lung:** pulmonary hypertension; rare ILD. (yang2021acta2mutationis pages 5-6, li2025casereportmultisystemic pages 2-4)
- **Visceral smooth muscle:** bladder and gastrointestinal tract. (kaw2022expandingacta2genotypes pages 1-2, regalado2018clinicalhistoryand pages 1-2)

### 7.2 Tissue/cellular and subcellular
- Predominant implicated cell type: **vascular SMC** and other smooth muscle lineages. (regalado2018clinicalhistoryand pages 1-2)
- Subcellular emphasis (2023): **nuclear pool of αSMA** and its interaction with chromatin remodelers (INO80/BAF) and chromatin accessibility changes. (kwartler2023nuclearsmoothmuscle pages 7-11, kwartler2023nuclearsmoothmuscle pages 24-28)

---

## 8. Temporal development
### 8.1 Onset
- Often **congenital/infancy**, with congenital mydriasis present at birth and early presentation with PDA or aortopulmonary window. (regalado2018clinicalhistoryand pages 1-2)
- Literature review noted age at presentation spanning from days to adulthood (3 days to 41 years), reflecting variable detection timing and phenotype. (yang2021acta2mutationis pages 5-6)

### 8.2 Progression
- Cerebrovascular and white-matter abnormalities show progression/accumulation with age in many cases; in a 13-patient imaging cohort, the youngest patient (3 months) lacked white-matter changes observed in older patients, consistent with progression. (munot2012anoveldistinctive pages 4-4)
- Aortic disease shows early high penetrance: cumulative aortic-event risk reached 100% by age 25 in a 33-patient Arg179 cohort. (regalado2018clinicalhistoryand pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology
MSMDS is **ultrarare** and largely described through case reports/series and a small number of cohorts.
- A 2024 compilation (as summarized in a 2025 case report) reported **~90 cases globally by April 2024**, with ~80% of reports from Europe/USA and relatively few cases reported in East Asia. (li2025casereportmultisystemic pages 2-4)

### 9.2 Inheritance pattern
- **Autosomal dominant**; classic Arg179 cases are frequently **de novo heterozygous**. (regalado2018clinicalhistoryand pages 1-2)

Penetrance/expressivity are incompletely quantified across the broader literature; however, in the Arg179 natural-history cohort, congenital mydriasis was universal and aortic disease was fully penetrant by age 25. (regalado2018clinicalhistoryand pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical recognition
Key diagnostic clues include the combination of congenital fixed dilated pupils (congenital mydriasis) and PDA/AP window with early neurovascular findings. (regalado2018clinicalhistoryand pages 1-2, munot2012anoveldistinctive pages 1-2)

### 10.2 Imaging
- **Brain MRI** for white-matter injury; **head/neck MRA** for arterial stenosis/arteriopathy is recommended in Arg179 management guidance. (regalado2018clinicalhistoryand pages 8-9)
- The cerebral arteriopathy has distinguishable neuroimaging features compared with classic moyamoya (proximal ectasia + distal stenosis, straight arterial course, absent basal collaterals). (munot2012anoveldistinctive pages 1-2, munot2012anoveldistinctive pages 6-7)

### 10.3 Genetic testing
- **Whole-exome sequencing** and targeted sequencing/panels for thoracic aortic aneurysm/dissection genes can identify ACTA2 variants and confirm diagnosis; this is emphasized in cohort and case-based literature. (li2025casereportmultisystemic pages 2-4, kaw2022expandingacta2genotypes pages 1-2)

---

## 11. Outcome / prognosis
### 11.1 Survival and mortality
In a 33-patient Arg179 cohort, **9 deaths** occurred between ages **0.5 and 32 years**, attributed to aortic, pulmonary, stroke complications, or unknown causes—indicating meaningful early mortality risk. (regalado2018clinicalhistoryand pages 1-2)

### 11.2 Morbidity and complications
- High burden of cerebrovascular injury (strokes, seizures, progressive arteriopathy) and early aortic events requiring repair. (regalado2018clinicalhistoryand pages 1-2)
- Neurologic and vascular disease can have perioperative risk; a 13-patient imaging cohort noted increased risk of postoperative ischemic stroke after revascularization in these patients. (munot2012anoveldistinctive pages 4-4)

---

## 12. Treatment
### 12.1 Current treatment paradigm (organ-directed; largely supportive)
There is no established disease-modifying therapy in current clinical practice for MSMDS. Management is multidisciplinary and focused on prevention/mitigation of life-threatening vascular complications plus symptomatic care for organ-specific dysfunction. (regalado2018clinicalhistoryand pages 1-2, yang2021acta2mutationis pages 5-6)

### 12.2 Surveillance and vascular management (real-world implementations)
**ACTA2 vasculopathy consensus (VASCERN, 2019)** provides structured imaging/monitoring recommendations for ACTA2-related vasculopathy (not MSMDS-specific) including:
- At diagnosis: **2D transthoracic echo** plus **complete vascular imaging (neck to pelvis) by CTA/MRA from age 18**; yearly 2D-TTE in children from diagnosis; adults complete vascular imaging every **2–5 years**. (laar2019europeanreferencenetwork pages 2-4)
- Blood pressure control (≤130/80 mmHg per ESC guidance). (laar2019europeanreferencenetwork pages 4-6)
- β-blockers are commonly used; VASCERN notes limited direct pediatric evidence but advises offering therapy from age 4 years and emphasizes individualized monitoring programs. (laar2019europeanreferencenetwork pages 6-7)
- Pregnancy counseling: preconception imaging of the entire aorta; maternal 2D-TTE monitoring every 4–12 weeks during pregnancy and at 6 months postpartum; avoid ARBs in pregnancy; consider prophylactic surgery for women with aortic root ≥45 mm and advise against pregnancy after prior dissection. (laar2019europeanreferencenetwork pages 4-6)

**MSMDS/Arg179 SMDS-specific management recommendations (2018 cohort)** include:
- Consider elective aortic root repair around **45 mm**, prefer valve-sparing when feasible; close monitoring of descending/thoracoabdominal segments due to potentially rapid enlargement. (regalado2018clinicalhistoryand pages 8-9)
- Baseline brain MRI and head/neck MRA (avoid CT when possible) and ongoing monitoring; consider aspirin in asymptomatic cerebral vasculopathy with pediatric precautions; standard seizure management. (regalado2018clinicalhistoryand pages 8-9)

**MAXO suggestions (examples):**
- Aortic imaging surveillance; echocardiography; magnetic resonance angiography; prophylactic aortic surgery; antihypertensive therapy; antiplatelet therapy (selected patients); genetic counseling; cascade testing; multidisciplinary care coordination.

### 12.3 Recent/experimental therapies and clinical trials
**Nicotinamide riboside (NR) metabolic therapy (translational):**
- **Trial:** *Nicotinamide Riboside (NR) to Treat Moyamoya-like Cerebrovascular Disease in Smooth Muscle Dysfunction Syndrome (SMDS)*, **ClinicalTrials.gov NCT06280482**, first posted **2024-02-28**, actual start **2024-03-06**; Phase 1; oral weight-based NR daily for 60 days; multiple endpoints including cerebral oxygenation/perfusion and aortic diameter. (NCT06280482 chunk 1)
- **URL:** https://clinicaltrials.gov/study/NCT06280482 (registry URL based on NCT identifier; core protocol details extracted from trial record). (NCT06280482 chunk 1)

---

## 13. Prevention
There is no primary prevention for de novo cases; prevention focuses on **secondary/tertiary prevention** of catastrophic events via early recognition, genetic confirmation, surveillance, and prophylactic/early intervention.
- VASCERN emphasizes cascade testing and “**proper genetic counselling involving psychosocial support**.” (laar2019europeanreferencenetwork pages 6-7)
- Pregnancy-related prevention includes preconception imaging, multidisciplinary counseling, and avoidance of teratogenic antihypertensives; postpartum surveillance is recommended. (laar2019europeanreferencenetwork pages 4-6)

---

## 14. Other species / natural disease
Naturally occurring MSMDS in nonhuman species was not identified in the retrieved sources.

---

## 15. Model organisms
Mechanistic and translational work relies heavily on engineered cellular and mouse models:
- **Acta2R179C/+ mouse SMC models (preclinical):** NR increased mitochondrial respiration and reduced glycolysis in mutant SMCs and attenuated moyamoya-like occlusive lesions and strokes after carotid injury. (milewicz2023augmentingmitochondrialrespiration pages 6-9)
- **iPSC-derived SMC differentiation models and human aortic scRNA-seq (2023):** Arg179 mutations reduce nuclear αSMA interactions with chromatin remodeling machinery, causing global defects in differentiation and increased plasticity/proliferation/migration. (kwartler2023nuclearsmoothmuscle pages 7-11, kwartler2023nuclearsmoothmuscle pages 42-46)

---

## Visual evidence
The following table image (cropped from the primary 33-patient cohort publication) provides patient-by-patient clinical characteristics and ages at major events and can be used as primary visual evidence for natural-history data extraction. (regalado2018clinicalhistoryand media 32dd1498)

---

## Notes on gaps and limitations
- Several requested identifiers (MONDO, Orphanet, ICD, MeSH) were not retrievable from the full-text sources available in this tool run; they should be added from dedicated ontology cross-reference resources.
- Many claims in the MSMDS space are based on small cohorts and case reports; statistics outside the 33-patient Arg179 cohort and compiled case tallies may be subject to ascertainment bias. (regalado2018clinicalhistoryand pages 1-2, li2025casereportmultisystemic pages 2-4)


References

1. (regalado2018clinicalhistoryand pages 1-2): Ellen S. Regalado, Lauren Mellor-Crummey, Julie De Backer, Alan C. Braverman, Lesley Ades, Susan Benedict, Timothy J. Bradley, M.Elizabeth Brickner, Kathryn C. Chatfield, Anne Child, Cori Feist, Kathryn W. Holmes, Glen Iannucci, Birgit Lorenz, Paul Mark, Takayuki Morisaki, Hiroko Morisaki, Shaine A. Morris, Anna L. Mitchell, John R. Ostergaard, Julie Richer, Denver Sallee, Sherene Shalhub, Mustafa Tekin, Anthony Estrera, Patricia Musolino, Anji Yetman, Reed Pyeritz, and Dianna M. Milewicz. Clinical history and management recommendations of the smooth muscle dysfunction syndrome due to acta2 arginine 179 alterations. Genetics in Medicine, 20:1206-1215, Oct 2018. URL: https://doi.org/10.1038/gim.2017.245, doi:10.1038/gim.2017.245. This article has 88 citations and is from a highest quality peer-reviewed journal.

2. (cardenas2023aseedsequence pages 1-3): Christian Lacks Lino Cardenas, Lauren C. Briere, David A. Sweetser, Mark E. Lindsay, and Patricia L. Musolino. A seed sequence variant in mir-145-5p causes multisystem smooth muscle dysfunction syndrome. Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci166497, doi:10.1172/jci166497. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (kaw2022expandingacta2genotypes pages 1-2): Anita Kaw, Kaveeta Kaw, Ellen M. Hostetler, Ana Beleza‐Meireles, Adam Smith‐Collins, Catherine Armstrong, Ingrid Scurr, Timothy Cotts, Rajani Aatre, Michael J. Bamshad, Dawn Earl, Abraham Groner, Katherine Agre, Yehuda Raveh, Callie S. Kwartler, and Dianna M. Milewicz. Expanding acta2 genotypes with corresponding phenotypes overlapping with smooth muscle dysfunction syndrome. American Journal of Medical Genetics Part A, 188:2389-2396, May 2022. URL: https://doi.org/10.1002/ajmg.a.62775, doi:10.1002/ajmg.a.62775. This article has 22 citations.

4. (laar2019europeanreferencenetwork pages 2-4): Ingrid M. B. H. van de Laar, Eloisa Arbustini, Bart Loeys, Erik Björck, Lise Murphy, Maarten Groenink, Marlies Kempers, Janneke Timmermans, Jolien Roos-Hesselink, Kalman Benke, Guglielmina Pepe, Barbara Mulder, Zoltan Szabolcs, Gisela Teixidó-Turà, Leema Robert, Yaso Emmanuel, Arturo Evangelista, Alessandro Pini, Yskert von Kodolitsch, Guillaume Jondeau, and Julie De Backer. European reference network for rare vascular diseases (vascern) consensus statement for the screening and management of patients with pathogenic acta2 variants. Orphanet Journal of Rare Diseases, Nov 2019. URL: https://doi.org/10.1186/s13023-019-1186-2, doi:10.1186/s13023-019-1186-2. This article has 48 citations and is from a peer-reviewed journal.

5. (li2025casereportmultisystemic pages 2-4): Qianying Li, Lidan Cui, Jun Su, and Yuelin Shen. Case report: multisystemic smooth muscle dysfunction syndrome: a rare genetic cause of infantile interstitial lung disease. Frontiers in Pharmacology, Jan 2025. URL: https://doi.org/10.3389/fphar.2024.1510969, doi:10.3389/fphar.2024.1510969. This article has 1 citations.

6. (laar2019europeanreferencenetwork pages 1-2): Ingrid M. B. H. van de Laar, Eloisa Arbustini, Bart Loeys, Erik Björck, Lise Murphy, Maarten Groenink, Marlies Kempers, Janneke Timmermans, Jolien Roos-Hesselink, Kalman Benke, Guglielmina Pepe, Barbara Mulder, Zoltan Szabolcs, Gisela Teixidó-Turà, Leema Robert, Yaso Emmanuel, Arturo Evangelista, Alessandro Pini, Yskert von Kodolitsch, Guillaume Jondeau, and Julie De Backer. European reference network for rare vascular diseases (vascern) consensus statement for the screening and management of patients with pathogenic acta2 variants. Orphanet Journal of Rare Diseases, Nov 2019. URL: https://doi.org/10.1186/s13023-019-1186-2, doi:10.1186/s13023-019-1186-2. This article has 48 citations and is from a peer-reviewed journal.

7. (regalado2018clinicalhistoryand pages 8-9): Ellen S. Regalado, Lauren Mellor-Crummey, Julie De Backer, Alan C. Braverman, Lesley Ades, Susan Benedict, Timothy J. Bradley, M.Elizabeth Brickner, Kathryn C. Chatfield, Anne Child, Cori Feist, Kathryn W. Holmes, Glen Iannucci, Birgit Lorenz, Paul Mark, Takayuki Morisaki, Hiroko Morisaki, Shaine A. Morris, Anna L. Mitchell, John R. Ostergaard, Julie Richer, Denver Sallee, Sherene Shalhub, Mustafa Tekin, Anthony Estrera, Patricia Musolino, Anji Yetman, Reed Pyeritz, and Dianna M. Milewicz. Clinical history and management recommendations of the smooth muscle dysfunction syndrome due to acta2 arginine 179 alterations. Genetics in Medicine, 20:1206-1215, Oct 2018. URL: https://doi.org/10.1038/gim.2017.245, doi:10.1038/gim.2017.245. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (yang2021acta2mutationis pages 5-6): Wen-Xian Yang, Hang-Hu Zhang, Jia-Ni Hu, Li Zhao, Yan-Yun Li, and Xiao-Li Shao. Acta2 mutation is responsible for multisystemic smooth muscle dysfunction syndrome with seizures: a case report and review of literature. World Journal of Clinical Cases, 9:8789-8796, Oct 2021. URL: https://doi.org/10.12998/wjcc.v9.i29.8789, doi:10.12998/wjcc.v9.i29.8789. This article has 10 citations.

9. (logeswaran2017twopatientswith pages 3-4): Thushiha Logeswaran, Christoph Friedburg, Karoline Hofmann, Hakan Akintuerk, Saskia Biskup, Michael Graef, Ali Rad, Axel Weber, Bernd A. Neubauer, Dietmar Schranz, Patrice Bouvagnet, Birgit Lorenz, and Andreas Hahn. Two patients with the heterozygous r189h mutation in acta2 and complex congenital heart defects expands the cardiac phenotype of multisystemic smooth muscle dysfunction syndrome. American Journal of Medical Genetics Part A, 173:959-965, Apr 2017. URL: https://doi.org/10.1002/ajmg.a.38102, doi:10.1002/ajmg.a.38102. This article has 18 citations.

10. (laar2019europeanreferencenetwork pages 4-6): Ingrid M. B. H. van de Laar, Eloisa Arbustini, Bart Loeys, Erik Björck, Lise Murphy, Maarten Groenink, Marlies Kempers, Janneke Timmermans, Jolien Roos-Hesselink, Kalman Benke, Guglielmina Pepe, Barbara Mulder, Zoltan Szabolcs, Gisela Teixidó-Turà, Leema Robert, Yaso Emmanuel, Arturo Evangelista, Alessandro Pini, Yskert von Kodolitsch, Guillaume Jondeau, and Julie De Backer. European reference network for rare vascular diseases (vascern) consensus statement for the screening and management of patients with pathogenic acta2 variants. Orphanet Journal of Rare Diseases, Nov 2019. URL: https://doi.org/10.1186/s13023-019-1186-2, doi:10.1186/s13023-019-1186-2. This article has 48 citations and is from a peer-reviewed journal.

11. (laar2019europeanreferencenetwork pages 6-7): Ingrid M. B. H. van de Laar, Eloisa Arbustini, Bart Loeys, Erik Björck, Lise Murphy, Maarten Groenink, Marlies Kempers, Janneke Timmermans, Jolien Roos-Hesselink, Kalman Benke, Guglielmina Pepe, Barbara Mulder, Zoltan Szabolcs, Gisela Teixidó-Turà, Leema Robert, Yaso Emmanuel, Arturo Evangelista, Alessandro Pini, Yskert von Kodolitsch, Guillaume Jondeau, and Julie De Backer. European reference network for rare vascular diseases (vascern) consensus statement for the screening and management of patients with pathogenic acta2 variants. Orphanet Journal of Rare Diseases, Nov 2019. URL: https://doi.org/10.1186/s13023-019-1186-2, doi:10.1186/s13023-019-1186-2. This article has 48 citations and is from a peer-reviewed journal.

12. (kwartler2023nuclearsmoothmuscle pages 7-11): Callie S. Kwartler, Albert J. Pedroza, Anita Kaw, Pujun Guan, Shuangtao Ma, Xue-yan Duan, Caroline Kernell, Charis Wang, Jose Emiliano Esparza Pinelo, Mikayla S. Borthwick Bowen, Jiyuan Chen, Yuan Zhong, Sanjay Sinha, Xuetong Shen, Michael P. Fischbein, and Dianna M. Milewicz. Nuclear smooth muscle α-actin participates in vascular smooth muscle cell differentiation. Nature Cardiovascular Research, 2:937-955, Sep 2023. URL: https://doi.org/10.1038/s44161-023-00337-4, doi:10.1038/s44161-023-00337-4. This article has 25 citations and is from a peer-reviewed journal.

13. (kwartler2023nuclearsmoothmuscle pages 42-46): Callie S. Kwartler, Albert J. Pedroza, Anita Kaw, Pujun Guan, Shuangtao Ma, Xue-yan Duan, Caroline Kernell, Charis Wang, Jose Emiliano Esparza Pinelo, Mikayla S. Borthwick Bowen, Jiyuan Chen, Yuan Zhong, Sanjay Sinha, Xuetong Shen, Michael P. Fischbein, and Dianna M. Milewicz. Nuclear smooth muscle α-actin participates in vascular smooth muscle cell differentiation. Nature Cardiovascular Research, 2:937-955, Sep 2023. URL: https://doi.org/10.1038/s44161-023-00337-4, doi:10.1038/s44161-023-00337-4. This article has 25 citations and is from a peer-reviewed journal.

14. (milewicz2023augmentingmitochondrialrespiration pages 6-9): D. Milewicz, Anita Kaw, Ting Wu, Zbigniew Starosolski, Zhen Zhou, Albert J. Pedroza, Suravi Majumder, Xue-yan Duan, Kaveeta Kaw, Jose Emiliano Esparza Pinelo, Michael P. Fischbein, Philip L. Lorenzi, Lin Tan, Sara Martinez, Iqbal Mahmud, L. Devkota, Heinrich Taegtmeyer, K. Ghaghada, Sean P Marrelli, and Callie S. Kwartler. Augmenting mitochondrial respiration in immature smooth muscle cells with an acta2 pathogenic variant mitigates moyamoya-like cerebrovascular disease. Research Square, Oct 2023. URL: https://doi.org/10.21203/rs.3.rs-3304679/v1, doi:10.21203/rs.3.rs-3304679/v1. This article has 2 citations.

15. (NCT06280482 chunk 1): Dianna M Milewicz. Nicotinamide Riboside (NR) to Treat Moyamoya-like Cerebrovascular Disease in Smooth Muscle Dysfunction Syndrome (SMDS). The University of Texas Health Science Center, Houston. 2024. ClinicalTrials.gov Identifier: NCT06280482

16. (munot2012anoveldistinctive pages 1-2): P. Munot, D. E. Saunders, D. M. Milewicz, E. S. Regalado, J. R. Ostergaard, K. P. Braun, T. Kerr, K. D. Lichtenbelt, S. Philip, C. Rittey, T. S. Jacques, T. C. Cox, and V. Ganesan. A novel distinctive cerebrovascular phenotype is associated with heterozygous arg179 acta2 mutations. Brain, 135:2506-2514, Jul 2012. URL: https://doi.org/10.1093/brain/aws172, doi:10.1093/brain/aws172. This article has 149 citations and is from a highest quality peer-reviewed journal.

17. (munot2012anoveldistinctive pages 4-4): P. Munot, D. E. Saunders, D. M. Milewicz, E. S. Regalado, J. R. Ostergaard, K. P. Braun, T. Kerr, K. D. Lichtenbelt, S. Philip, C. Rittey, T. S. Jacques, T. C. Cox, and V. Ganesan. A novel distinctive cerebrovascular phenotype is associated with heterozygous arg179 acta2 mutations. Brain, 135:2506-2514, Jul 2012. URL: https://doi.org/10.1093/brain/aws172, doi:10.1093/brain/aws172. This article has 149 citations and is from a highest quality peer-reviewed journal.

18. (kwartler2023nuclearsmoothmuscle pages 24-28): Callie S. Kwartler, Albert J. Pedroza, Anita Kaw, Pujun Guan, Shuangtao Ma, Xue-yan Duan, Caroline Kernell, Charis Wang, Jose Emiliano Esparza Pinelo, Mikayla S. Borthwick Bowen, Jiyuan Chen, Yuan Zhong, Sanjay Sinha, Xuetong Shen, Michael P. Fischbein, and Dianna M. Milewicz. Nuclear smooth muscle α-actin participates in vascular smooth muscle cell differentiation. Nature Cardiovascular Research, 2:937-955, Sep 2023. URL: https://doi.org/10.1038/s44161-023-00337-4, doi:10.1038/s44161-023-00337-4. This article has 25 citations and is from a peer-reviewed journal.

19. (munot2012anoveldistinctive pages 7-8): P. Munot, D. E. Saunders, D. M. Milewicz, E. S. Regalado, J. R. Ostergaard, K. P. Braun, T. Kerr, K. D. Lichtenbelt, S. Philip, C. Rittey, T. S. Jacques, T. C. Cox, and V. Ganesan. A novel distinctive cerebrovascular phenotype is associated with heterozygous arg179 acta2 mutations. Brain, 135:2506-2514, Jul 2012. URL: https://doi.org/10.1093/brain/aws172, doi:10.1093/brain/aws172. This article has 149 citations and is from a highest quality peer-reviewed journal.

20. (munot2012anoveldistinctive pages 6-7): P. Munot, D. E. Saunders, D. M. Milewicz, E. S. Regalado, J. R. Ostergaard, K. P. Braun, T. Kerr, K. D. Lichtenbelt, S. Philip, C. Rittey, T. S. Jacques, T. C. Cox, and V. Ganesan. A novel distinctive cerebrovascular phenotype is associated with heterozygous arg179 acta2 mutations. Brain, 135:2506-2514, Jul 2012. URL: https://doi.org/10.1093/brain/aws172, doi:10.1093/brain/aws172. This article has 149 citations and is from a highest quality peer-reviewed journal.

21. (regalado2018clinicalhistoryand media 32dd1498): Ellen S. Regalado, Lauren Mellor-Crummey, Julie De Backer, Alan C. Braverman, Lesley Ades, Susan Benedict, Timothy J. Bradley, M.Elizabeth Brickner, Kathryn C. Chatfield, Anne Child, Cori Feist, Kathryn W. Holmes, Glen Iannucci, Birgit Lorenz, Paul Mark, Takayuki Morisaki, Hiroko Morisaki, Shaine A. Morris, Anna L. Mitchell, John R. Ostergaard, Julie Richer, Denver Sallee, Sherene Shalhub, Mustafa Tekin, Anthony Estrera, Patricia Musolino, Anji Yetman, Reed Pyeritz, and Dianna M. Milewicz. Clinical history and management recommendations of the smooth muscle dysfunction syndrome due to acta2 arginine 179 alterations. Genetics in Medicine, 20:1206-1215, Oct 2018. URL: https://doi.org/10.1038/gim.2017.245, doi:10.1038/gim.2017.245. This article has 88 citations and is from a highest quality peer-reviewed journal.