---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:53.173305'
end_time: '2026-04-04T12:56:43.634077'
duration_seconds: 830.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3** covering all of the
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
- **Disease Name:** ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3** covering all of the
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


# Comprehensive Research Report: ALDH18A1-Related Autosomal Dominant Cutis Laxa Type 3 (ADCL3)

## Executive summary
ALDH18A1-related autosomal dominant cutis laxa type 3 (ADCL3) is a very rare, typically **de novo** Mendelian neurocutaneous/connective-tissue disorder characterized by congenital/early-onset **cutis laxa with progeroid facial appearance**, **growth restriction**, **neurodevelopmental impairment**, **ocular disease (cataract/corneal clouding)**, and distinctive **intracranial arterial tortuosity** in a subset. The disorder is caused by heterozygous pathogenic variants in **ALDH18A1**, encoding mitochondrial **Δ1-pyrroline-5-carboxylate synthase (P5CS)**, a bifunctional enzyme in de novo **proline and ornithine** biosynthesis. Pathogenesis is supported by evidence for **dominant-negative effects** of Arg138 substitutions and by downstream metabolic effects implicating **proline/ornithine/polyamine** and **glutathione (redox)** pathways, which plausibly link mitochondrial metabolism to extracellular matrix (ECM) homeostasis. (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6, bhola2017autosomaldominantcutis pages 2-3, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

---

## 1. Disease information

### 1.1 What is the disease?
ADCL3 is a progeroid form of autosomal-dominant cutis laxa caused by heterozygous ALDH18A1 variants, initially delineated as recurrent de novo substitutions at **P5CS residue Arg138** in eight unrelated individuals with a shared neurocutaneous phenotype. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media cda3d61e)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
* **MONDO (parent term):** cutis laxa = **MONDO_0016175** (disease-level parent concept; subtype-specific MONDO code not retrieved in the accessed corpus). (fischerzirnsak2015recurrentdenovo pages 1-2)
* **OMIM/Orphanet/ICD-10/ICD-11/MeSH:** Not directly retrievable from the accessed full-text sources in this run; this report therefore cites primary literature and expert reviews as evidence sources.

### 1.3 Synonyms and alternative names
Commonly used names in the literature include:
* “**Progeroid form of autosomal-dominant cutis laxa**”
* “**Autosomal dominant cutis laxa with progeroid features**”
* “**ALDH18A1-ADCL**”
* “Dominant form of **De Barsy / de Barsy-like** cutis laxa (reflecting phenotypic overlap)” (bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6)

| Concept | Details | Key citations |
|---|---|---|
| Disease name | **ALDH18A1-related autosomal dominant cutis laxa type 3**; a progeroid form of autosomal-dominant cutis laxa linked to heterozygous pathogenic variants in **ALDH18A1** encoding pyrroline-5-carboxylate synthase (**P5CS**) (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6) | Fischer-Zirnsak et al., *Am J Hum Genet* 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; Bhola et al., *J Hum Genet* 2017, DOI: https://doi.org/10.1038/jhg.2017.18; Beyens et al., *Clin Genet* 2021, DOI: https://doi.org/10.1111/cge.13865 |
| Synonyms | Reported/used names include **autosomal-dominant cutis laxa with progeroid features**, **ALDH18A1-ADCL**, **progeroid form of autosomal-dominant cutis laxa**, and a **dominant form of De Barsy syndrome / de Barsy-like syndrome** because of overlap with recessive PYCR1/ALDH18A1 disorders (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18; DOI: https://doi.org/10.1111/cge.13865 |
| Inheritance | **Autosomal dominant**, with most published cases due to **heterozygous de novo** variants; de novo origin was confirmed in six probands in the 2015 series, and the 2017 case was also de novo. Genetic counseling note: sibling recurrence risk is generally low but **gonadal mosaicism** cannot be excluded (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 2-3) | Fischer-Zirnsak et al. 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; Bhola et al. 2017, DOI: https://doi.org/10.1038/jhg.2017.18 |
| Causal gene | **ALDH18A1** (aldehyde dehydrogenase 18 family member A1), encoding mitochondrial **Δ1-pyrroline-5-carboxylate synthase / P5CS**, a bifunctional enzyme in **de novo proline and ornithine biosynthesis**. Dominant disease is associated with monoallelic pathogenic variants that can exert a dominant-negative effect on P5CS function (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, bhola2017autosomaldominantcutis pages 2-3) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18 |
| Distinguishing clinical features | Core recognizable phenotype includes **congenital/early-onset cutis laxa**, **progeroid triangular facies**, **broad/prominent forehead**, **thin translucent wrinkled skin with visible veins**, **prenatal and postnatal growth restriction**, **developmental delay**, **joint hyperlaxity**, **ocular abnormalities** (cataracts, corneal clouding/opacities, nystagmus), **adducted thumbs**, and **skeletal anomalies** such as hip dislocation. This phenotype overlaps with recessive De Barsy/wrinkly skin syndromes but is generally described as milder than recessive ALDH18A1/PYCR1 disease (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6, fischerzirnsak2015recurrentdenovo media cda3d61e) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18; DOI: https://doi.org/10.1111/cge.13865 |
| Neuroimaging / vascular features | Important distinguishing findings include **intracranial/cranial arterial tortuosity** and MRI abnormalities such as **prominent ventricles**, **thin corpus callosum**, and enlarged perivascular spaces in later summaries. Cranial vessel tortuosity was reported in multiple affected individuals and is a notable clue in molecular diagnosis (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, beyens2021cutislaxaa pages 4-6) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18; DOI: https://doi.org/10.1111/cge.13865 |
| Variant spectrum | Landmark dominant variants cluster at **Arg138** of P5CS: recurrent de novo substitutions **p.Arg138Trp**, **p.Arg138Leu**, and **p.Arg138Gln** were identified in eight unrelated individuals. Bhola et al. added the first dominant case outside Arg138: **c.377G>A (p.Arg126His)** (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, bhola2017autosomaldominantcutis pages 2-3, fischerzirnsak2015recurrentdenovo media cda3d61e) | Fischer-Zirnsak et al. 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; Bhola et al. 2017, DOI: https://doi.org/10.1038/jhg.2017.18 |
| Mechanistic distinction | Functional work showed Arg138 mutant P5CS is **stable** and can interact with wild-type protein, but has **altered sub-mitochondrial distribution**, **altered native-complex size**, **reduced enzymatic activity**, and **delayed proline accumulation**, supporting a **dominant-negative** mechanism rather than simple haploinsufficiency (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 2-3) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18 |
| Reported case counts | Initial defining series: **8 unrelated individuals** with Arg138 substitutions (2015). The 2017 report added **1 additional de novo case** with p.Arg126His. A later GeneReview-style summary states **13 individuals** with heterozygous de novo pathogenic ALDH18A1 variants causing ADCL had been reported (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18 |
| Differential diagnosis | Key differentials include **PYCR1-related autosomal recessive cutis laxa**, **ALDH18A1-related autosomal recessive cutis laxa / De Barsy syndrome**, wrinkly skin syndrome, and other cutis laxa syndromes. Intracranial arterial tortuosity, adducted thumbs, ocular disease, and de novo ALDH18A1 variants are especially helpful discriminators (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6, wolthuis2014cutislaxafat pages 1-2) | DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; DOI: https://doi.org/10.1038/jhg.2017.18; DOI: https://doi.org/10.1111/cge.13865 |
| Key publications | **Fischer-Zirnsak et al. 2015 (AJHG)**: defining series of recurrent de novo Arg138 variants; **Bhola et al. 2017 (J Hum Genet)**: first non-Arg138 dominant variant p.Arg126His; **Beyens et al. 2021 (Clin Genet)**: broad cutis laxa review summarizing ALDH18A1-related AD disease; **Fischer-Zirnsak & Callewaert 2026 GeneReview chapter**: updated synthesis noting 13 reported dominant individuals and expanded imaging/phenotypic spectrum (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | 2015 AJHG DOI: https://doi.org/10.1016/j.ajhg.2015.08.001; 2017 J Hum Genet DOI: https://doi.org/10.1038/jhg.2017.18; 2021 Clin Genet DOI: https://doi.org/10.1111/cge.13865; 2026 chapter summary (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |


*Table: This table summarizes the core identity, inheritance, gene, distinguishing phenotype, and foundational literature for ALDH18A1-related autosomal dominant cutis laxa type 3. It is useful as a compact reference for nomenclature, diagnosis, and key evidence sources.*

### 1.4 Evidence source type
The disorder definition and phenotype spectrum are derived largely from **individual patients** in published case reports/series (human clinical genetics) and consolidated in disease-level reviews (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 4-6) and an expert GeneReview-style synthesis (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline heterozygous pathogenic variants in **ALDH18A1** encoding **P5CS**, typically arising **de novo**. (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 2-3, fischerzirnsak2026neurocutaneousdisordersdue pages 15-18)

### 2.2 Risk factors
* **Genetic:** de novo occurrence is typical; familial recurrence risk is low but non-zero because parental gonadal mosaicism is possible (estimated ~1% when parental leukocyte testing is negative). (bhola2017autosomaldominantcutis pages 2-3, fischerzirnsak2026neurocutaneousdisordersdue pages 15-18)
* **Environmental:** No specific environmental risk factors have been established for ADCL3 in the accessed literature.

### 2.3 Protective factors
No genetic or environmental protective factors have been reported for ADCL3 in the accessed literature.

### 2.4 Gene–environment interactions
No established GxE interactions were identified in the accessed sources.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (human)
The original AJHG series reports **8 unrelated individuals** with recurrent de novo variants at **Arg138**, with a shared phenotype including:
* **Prenatal growth restriction** (reported as present in all), and postnatal growth restriction in most (fischerzirnsak2015recurrentdenovo pages 1-2)
* **Lax thin skin** with visible veins, **joint hyperlaxity** (fischerzirnsak2015recurrentdenovo pages 1-2)
* **Psychomotor delay** in all (fischerzirnsak2015recurrentdenovo pages 1-2)
* **Ocular disease**: “cataracts or corneal clouding” (fischerzirnsak2015recurrentdenovo pages 1-2)
* **Adducted thumbs** (reported in 5/8) (fischerzirnsak2015recurrentdenovo pages 1-2)
* **Cranial vessel tortuosity** in a subset (reported in 4/8) (fischerzirnsak2015recurrentdenovo pages 1-2)

A later de novo case with a non-Arg138 variant (p.Arg126His) also showed intracranial arterial tortuosity on brain MRI and severe growth and neurodevelopmental involvement. (bhola2017autosomaldominantcutis pages 1-2)

**Table evidence:** The clinical and molecular summary across the 8 individuals (including variant class p.Arg138Trp/Leu/Gln) is summarized in Table 1 of Fischer-Zirnsak et al. 2015. (fischerzirnsak2015recurrentdenovo media cda3d61e)

### 3.2 Phenotype ontology mapping (HPO suggestions)
| Clinical feature | Suggested HPO term(s) with IDs | Notes | Key citations |
|---|---|---|---|
| Cutis laxa / wrinkled redundant skin | Cutis laxa (HP:0000973); Wrinkled skin (HP:0002487) | Hallmark feature; congenital or early-infantile onset in reported dominant cases; skin wrinkling may become less prominent with age in later summaries (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Thin translucent skin | Thin skin (HP:0000958); Translucent skin (HP:0008067) | Frequently reported in progeroid ADCL/ADCL3; later synthesis suggests thin/translucent skin in ~90% of affected individuals with heterozygous de novo ALDH18A1 variants (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Visible/prominent veins | Prominent superficial blood vessels (HP:0007408) | Often described together with translucent skin and paucity of subcutaneous fat; clinically useful clue in infancy/childhood (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) | (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) |
| Intrauterine growth restriction | Intrauterine growth retardation (HP:0001511) | Present in all individuals in the original 2015 series; later summary gives ~96% across reported AD cases (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Postnatal growth retardation / short stature / poor growth | Postnatal growth retardation (HP:0008897); Short stature (HP:0004322); Failure to thrive (HP:0001508) | Postnatal growth restriction in 7/8 original cases; marked growth deficit also described in the 2017 case report (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 25-26) | (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, beyens2021cutislaxaa pages 25-26) |
| Developmental delay / intellectual disability | Global developmental delay (HP:0001263); Delayed psychomotor development (HP:0001263); Intellectual disability (HP:0001249) | Psychomotor delay in all individuals in the defining series; later review describes mild-to-moderate intellectual disability as typical (fischerzirnsak2015recurrentdenovo pages 1-2, beyens2021cutislaxaa pages 4-6, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (fischerzirnsak2015recurrentdenovo pages 1-2, beyens2021cutislaxaa pages 4-6, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Hypotonia | Hypotonia (HP:0001252); Truncal hypotonia (HP:0002078) | Reported especially in early life/childhood, including in the 2017 non-Arg138 case (bhola2017autosomaldominantcutis pages 1-2) | (bhola2017autosomaldominantcutis pages 1-2) |
| Hypertonia / spasticity | Hypertonia (HP:0001276); Spasticity (HP:0001257); Spastic diplegia (HP:0001264) | Dominant ALDH18A1 cases are considered at higher risk of hypertonia/spasticity than recessive cutis laxa phenotypes; spastic diplegia reported in a minority (~10%) in later summary (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) | (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) |
| Joint hyperlaxity | Joint hypermobility (HP:0001382) | Common connective-tissue manifestation in the original dominant series (fischerzirnsak2015recurrentdenovo pages 1-2) | (fischerzirnsak2015recurrentdenovo pages 1-2) |
| Adducted thumbs / distal arthrogryposis | Adducted thumb (HP:0001182); Distal arthrogryposis (HP:0005684); Camptodactyly (HP:0004209) | Adducted thumbs reported in 5/8 individuals in the original series and highlighted as particularly characteristic/pathognomonic in later summaries (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) | (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) |
| Hip dislocation / dysplasia | Congenital hip dislocation (HP:0002827); Hip dysplasia (HP:0001385) | Congenital hip dislocation described in dominant cases and in the 2017 report (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) | (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) |
| Scoliosis | Scoliosis (HP:0002650) | Reported in later disease summaries as part of skeletal involvement (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13) | (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13) |
| Osteopenia | Osteopenia (HP:0000938) | Included in later synthesized phenotype descriptions for ALDH18A1-related ADCL (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) | (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7) |
| Cataract | Cataract (HP:0000518); Congenital cataract (HP:0000519) | Very frequent ocular feature; cataracts reported in original dominant series and 2017 case; early cataracts emphasized in later summary (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) | (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) |
| Corneal clouding / corneal opacity | Corneal opacity (HP:0007957); Cloudy cornea (HP:0001115) | Recurrent and clinically important ocular finding; helpful in differential diagnosis with De Barsy-like conditions (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) | (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) |
| Nystagmus / strabismus | Nystagmus (HP:0000639); Strabismus (HP:0000486) | Nystagmus reported in the 2017 case; strabismus listed in later synthesis (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) | (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) |
| Intracranial / cranial arterial tortuosity | Tortuosity of intracranial arteries (HP:0034397); Arterial tortuosity (HP:0005117) | Highly informative vascular phenotype; present in 4/8 individuals in the original series and strongly associated with ADCL3 in later reviews (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) | (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) |
| Ventriculomegaly / prominent ventricles | Ventriculomegaly (HP:0002119) | Brain MRI may show enlarged/prominent ventricles; reported in the 2017 case and later summaries (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Thin corpus callosum | Thin corpus callosum (HP:0002079) | Recurrent neuroimaging finding in later summaries of ALDH18A1-related ADCL/mitochondrial proline synthesis disorders (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) | (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |


*Table: This table maps the core reported phenotype spectrum of ALDH18A1-related autosomal dominant cutis laxa type 3 to suggested HPO terms for knowledge-base annotation. It emphasizes features repeatedly described in primary case reports and later expert summaries, including skin, growth, neurologic, skeletal, ocular, and vascular/neuroimaging findings.*

### 3.3 Quality of life impact
No disease-specific validated quality-of-life instruments (e.g., SF-36, EQ-5D) were identified in the accessed sources. Functional impact is inferred from developmental delay, movement disorder/spasticity risk, orthopedic issues (hip dislocation, scoliosis), and visual impairment from cataract/corneal clouding. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, beyens2021cutislaxaa pages 25-26)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
* **Gene:** ALDH18A1 (P5CS), a bifunctional mitochondrial enzyme in **de novo proline and ornithine** biosynthesis. (colonna2023functionalassessmentof pages 1-2)

### 4.2 Pathogenic variant spectrum in ADCL3
The dominant ADCL3 spectrum is centered on recurrent de novo substitutions affecting **Arg138** (p.Arg138Trp/Leu/Gln) and includes at least one dominant case outside Arg138 (p.Arg126His). (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2, bhola2017autosomaldominantcutis pages 2-3, fischerzirnsak2015recurrentdenovo media cda3d61e)

| Variant (HGVS protein) | Nucleotide (if stated) | Evidence type | Key phenotypic notes | Mechanistic notes | Key citation |
|---|---|---|---|---|---|
| p.Arg138Trp | Not stated in retrieved context | De novo case-series variant in 2015 defining cohort; supported by functional assay | Part of the recurrent Arg138 dominant ADCL3 spectrum with progeroid triangular facies, prenatal/postnatal growth restriction, lax thin translucent skin with visible veins, developmental delay, ocular abnormalities, joint hyperlaxity, adducted thumbs, and intracranial vessel tortuosity in a subset (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media cda3d61e) | Arg138 substitutions were reported as stable mutant proteins that interact with wild-type P5CS but show altered sub-mitochondrial distribution, altered native-complex size, reduced enzymatic activity, delayed proline accumulation, supporting a dominant-negative mechanism (fischerzirnsak2015recurrentdenovo pages 1-2) | Fischer-Zirnsak et al., *Am J Hum Genet* 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001 (fischerzirnsak2015recurrentdenovo pages 1-2) |
| p.Arg138Leu | Not stated in retrieved context | De novo case-series variant in 2015 defining cohort; supported by functional assay | Same recurrent Arg138-associated ADCL3 phenotype spectrum in the original 8 unrelated individuals with progeroid cutis laxa, growth restriction, neurodevelopmental delay, ocular disease, skeletal/connective tissue findings, and vascular tortuosity clues (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media cda3d61e) | Included among the heterozygous Arg138 substitutions causing amino acid change at the same highly conserved residue; functional data support dominant-negative pathogenicity via abnormal complex behavior/localization and reduced P5CS function (fischerzirnsak2015recurrentdenovo pages 1-2) | Fischer-Zirnsak et al., *Am J Hum Genet* 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001 (fischerzirnsak2015recurrentdenovo pages 1-2) |
| p.Arg138Gln | Not stated in retrieved context | De novo case-series variant in 2015 defining cohort; supported by functional assay | Same defining ADCL3/progeroid cutis laxa syndrome with congenital/early cutis laxa, characteristic facies, developmental delay, cataract/corneal clouding, joint laxity, adducted thumbs, and intracranial arterial tortuosity in some evaluated individuals (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media cda3d61e) | Later mechanistic discussion specifically notes P5CS R138Q as functioning in a dominant-negative manner; the 2015 study showed Arg138 mutant proteins alter localization/complex properties and reduce enzymatic activity (fischerzirnsak2015recurrentdenovo pages 1-2) | Fischer-Zirnsak et al., *Am J Hum Genet* 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.08.001 (fischerzirnsak2015recurrentdenovo pages 1-2) |
| p.Arg126His | c.377G>A | De novo case report in 2017; interpreted using prior Arg138 functional/mechanistic framework | Reported in a male with autosomal dominant cutis laxa with progeroid features including cutis laxa, poor growth/small stature, microcephaly, truncal hypotonia, global developmental delay, congenital cataracts/nystagmus/corneal opacities, inguinal hernias, hip dislocations, adducted thumbs, and marked tortuosity of intracranial vertebral and carotid arteries (bhola2017autosomaldominantcutis pages 1-2, bhola2017autosomaldominantcutis pages 2-3) | First dominant ADCL3 variant reported outside Arg138; absent from population databases and near Arg138. Prior studies of Arg138-mutant cell lines showed altered mitochondrial localization and decreased proline levels, and the authors considered a dominant-negative effect plausible for p.Arg126His as well (bhola2017autosomaldominantcutis pages 2-3) | Bhola et al., *J Hum Genet* 2017, DOI: https://doi.org/10.1038/jhg.2017.18 (bhola2017autosomaldominantcutis pages 1-2, bhola2017autosomaldominantcutis pages 2-3) |


*Table: This table summarizes the currently reported pathogenic ALDH18A1 variants specifically linked to autosomal dominant cutis laxa type 3, including their evidence base, phenotype associations, and mechanistic interpretation. It is useful for variant curation and genotype-phenotype annotation.*

### 4.3 Variant mechanism (dominant negative)
Functional evidence in the defining ADCL3 report indicates the Arg138 mutant protein is stable and can interact with wild-type P5CS but shows altered mitochondrial subcompartment behavior/complex properties and reduced activity with delayed proline accumulation—supporting a **dominant-negative** mechanism rather than haploinsufficiency. (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 2-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities specific to ADCL3 were identified in the accessed sources.

---

## 5. Environmental information
No specific toxins, lifestyle factors, or infectious triggers have been linked to ADCL3 in the accessed sources.

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding
**Biochemical context:** P5CS converts **glutamate → pyrroline-5-carboxylate (P5C)**, which can be directed to **proline** (via PYCR1) or **ornithine** (via OAT), linking ALDH18A1 function to the **urea cycle** and **TCA/Krebs cycle**-connected metabolism. (colonna2023functionalassessmentof pages 1-2)

**ECM link:** Impaired proline biosynthesis is proposed to limit collagen and elastin production because proline is abundant in these proteins, providing a plausible connection from mitochondrial metabolism to cutis laxa/ECM weakness. (beyens2021cutislaxaa pages 12-14, colonna2023functionalassessmentof pages 1-2)

**Redox/antioxidant link:** Downstream products and substrate pools connect P5CS to redox balance through **glutathione** and **polyamine** pathways. Multi-omic and metabolomic work in ALDH18A1/P5CS-deficient patient fibroblasts shows reduced proline and glutathione with altered polyamines (e.g., putrescine), consistent with oxidative-stress–relevant mechanisms and ECM remodeling signals (e.g., MMP3/COMP). (colonna2023functionalassessmentof pages 8-9, colonna2023functionalassessmentof pages 6-7)

### 6.2 2023–2024 research developments (prioritized)
Although not focused exclusively on ADCL3, recent high-resolution cellular multi-omics provides mechanistic insights relevant to the ALDH18A1 disease spectrum:

* **Human molecular genetics 2023 (Colonna et al.; publication month Sep 2023; URL https://doi.org/10.1093/hmg/ddac226):**
  * Abstract statement (direct quote): “**ALDH18A1 encodes the bifunctional enzyme pyrroline-5-carboxylate synthetase (P5CS) that plays a role in the de novo biosynthesis of proline and ornithine.**” (colonna2023functionalassessmentof pages 1-2)
  * Abstract statement (direct quote): “**Using an unlabeled NMR-based metabolomics approach … we identified reduced abundance of glutamate and several metabolites derived from glutamate, including proline and glutathione.**” (colonna2023functionalassessmentof pages 1-1)
  * Key statistics: RNA-seq differential expression included “**2391 upregulated and 456 downregulated**” genes in patient fibroblasts versus controls; metabolomics implicated glutathione and polyamine pathways; ECM-related genes/proteins were altered (e.g., MMP3/COMP). (colonna2023functionalassessmentof pages 8-9, colonna2023functionalassessmentof pages 6-7)
  * Interpretation: these data nominate metabolic and redox biomarkers (proline, glutathione, putrescine; glutamate) and ECM markers (e.g., MMP3, COMP) as measurable downstream effects of P5CS deficiency that could be investigated in ADCL3. (colonna2023functionalassessmentof pages 8-9)

* **In silico population/cohort context (2024; Egyptian J Med Hum Genet; URL https://doi.org/10.1186/s43042-024-00479-5):** While not ADCL3-specific, a 2024 Iranian cohort analysis emphasizes that overlapping connective tissue phenotypes (EDS/OI/CL) often require WES for accurate molecular diagnosis; it reports ≥59% of cases in that cohort involved consanguinity (more relevant to recessive conditions). (colonna2023functionalassessmentof pages 7-8)

### 6.3 Causal chain (proposed, evidence-based)
1. **Heterozygous de novo ALDH18A1 variants (Arg138 cluster)** → dominant-negative P5CS dysfunction with reduced enzymatic function and altered mitochondrial localization/complex properties. (fischerzirnsak2015recurrentdenovo pages 1-2)
2. **Altered proline/ornithine (and related glutamate pool) availability** → impaired collagen/elastin synthesis and/or broader ECM remodeling; may contribute to lax skin and connective tissue signs. (beyens2021cutislaxaa pages 12-14, colonna2023functionalassessmentof pages 1-2)
3. **Perturbed antioxidant metabolism** (e.g., glutathione depletion/overutilization) and altered polyamines → oxidative stress and cellular dysfunction that may exacerbate connective tissue and neurodevelopmental outcomes. (colonna2023functionalassessmentof pages 8-9)
4. **Vascular phenotype (intracranial arterial tortuosity):** consistently observed in multiple ADCL3 individuals and emphasized in expert summaries; however, direct mechanistic links from P5CS dysfunction to tortuosity remain incompletely established in the accessed sources and should be treated as a high-confidence phenotype with a hypothesis-level mechanism. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9)

### 6.4 Suggested ontology terms
* **GO Biological Process (suggested):** proline biosynthetic process; ornithine biosynthetic process; amino acid metabolic process; mitochondrial organization; extracellular matrix organization; response to oxidative stress; glutathione metabolic process.
* **CL cell types (suggested):** dermal fibroblast; vascular smooth muscle cell; endothelial cell; neuronal cell types (corticospinal neurons) (phenotype-driven; direct cell-type evidence limited in accessed sources).
* **CHEBI (suggested metabolites):** L-proline; L-ornithine; L-arginine; L-glutamate; glutathione; putrescine.

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
* **Skin / connective tissue:** cutis laxa, translucent skin, visible veins. (fischerzirnsak2015recurrentdenovo pages 1-2, beyens2021cutislaxaa pages 25-26)
* **Eye:** cataracts, corneal clouding/opacities; strabismus/nystagmus. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9)
* **Central nervous system:** developmental delay; brain MRI findings including ventriculomegaly and thin corpus callosum (reported across syntheses and case report). (bhola2017autosomaldominantcutis pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5)
* **Vasculature (intracranial):** intracranial arterial tortuosity. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9)
* **Musculoskeletal:** joint hypermobility, adducted thumbs/distal arthrogryposis, hip dislocation, scoliosis/osteopenia in some summaries. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 5-7)

### 7.2 UBERON (suggested)
* Skin of body (UBERON:0002097)
* Eye (UBERON:0000970)
* Brain (UBERON:0000955)
* Intracranial artery (UBERON:0001637; subtype terms as needed)
* Hip joint (UBERON:0001463)

---

## 8. Temporal development

### 8.1 Onset
Phenotype is typically **congenital or early-infantile**, with prenatal growth restriction and early appearance of skin/ocular/neurodevelopmental features. (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 1-2)

### 8.2 Progression
An expert synthesis notes skin wrinkling may become less prominent with age while translucent skin and paucity of subcutaneous fat become more evident; systematic longitudinal natural history data remain limited. (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7)

---

## 9. Inheritance and population

### 9.1 Inheritance
* **Autosomal dominant**, predominantly **de novo**. (fischerzirnsak2015recurrentdenovo pages 1-2, bhola2017autosomaldominantcutis pages 2-3)

### 9.2 Epidemiology
No population prevalence/incidence estimates were identified in the accessed sources.

### 9.3 Reported case counts (recent synthesis)
* Defining dominant Arg138 series: **8 unrelated individuals** (2015). (fischerzirnsak2015recurrentdenovo pages 1-2)
* Additional de novo case with p.Arg126His (2017). (bhola2017autosomaldominantcutis pages 1-2)
* Later expert summary: **13 individuals** with heterozygous de novo pathogenic variants causing ALDH18A1-related ADCL. (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5)

---

## 10. Diagnostics

### 10.1 Clinical pattern recognition (high-yield features)
A practical diagnostic clue-set includes: congenital/early cutis laxa with translucent skin/visible veins, prenatal/postnatal growth restriction, ocular disease (cataract/corneal clouding), adducted thumbs, neurodevelopmental delay, and intracranial arterial tortuosity on neuroimaging. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26)

### 10.2 Genetic testing
Gene panel testing and/or WES/WGS are recommended approaches for molecular confirmation, with parental testing to establish de novo status and refine recurrence counseling. (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5, fischerzirnsak2026neurocutaneousdisordersdue pages 15-18)

### 10.3 Biochemical tests and biomarkers
Serum/urine amino-acid screening is suggested (ornithine, citrulline, arginine, proline), but routine metabolic workups can be normal in ALDH18A1-related cutis laxa, so normal amino acids do not exclude diagnosis. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, wolthuis2014cutislaxafat pages 1-2)

### 10.4 Imaging and system assessments
Baseline echocardiography and broad vascular evaluation are recommended for cutis laxa syndromes, with **MRI head-to-pelvis at diagnosis** specifically recommended in a practical review for progeroid ADCL because of aneurysm/cardiovascular risk concerns across these syndromes. (beyens2021cutislaxaa pages 12-14)

| Domain | Suggested evaluations/tests | Purpose | Notes/implementation details | Key citations (pqac ids) |
|---|---|---|---|---|
| Molecular genetics | Cutis laxa / connective tissue / intellectual disability multigene panel; WES or WGS if panel is non-diagnostic; confirm variant in proband | Establish diagnosis of ALDH18A1-related ADCL3 | Diagnosis is established by a heterozygous ALDH18A1 pathogenic variant known to cause ADCL; exome/genome sequencing is appropriate because coding-region variants predominate in reported cases | (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5, beyens2021cutislaxaa pages 12-14) |
| Parental testing and counseling | Targeted parental molecular testing for the proband’s ALDH18A1 variant | Clarify de novo status and recurrence risk | Reported ADCL cases are typically de novo; if absent in parental leukocyte DNA, recurrence risk is still not zero because gonadal/somatic mosaicism is possible; sibling recurrence risk is estimated at ~1%; prenatal and preimplantation testing are possible once the familial variant is known | (fischerzirnsak2026neurocutaneousdisordersdue pages 15-18, fischerzirnsak2026neurocutaneousdisordersduef pages 15-18, fischerzirnsak2026neurocutaneousdisordersdueb pages 15-18) |
| Biochemical screening | Serum and urine amino acid analysis including ornithine, citrulline, arginine, and proline | Look for mitochondrial proline-synthesis abnormalities and support broader differential diagnosis | Low ornithine/citrulline/arginine/proline may be seen in the disease group, but routine metabolic testing can be normal in ALDH18A1-related cutis laxa; normal amino acids do not exclude diagnosis | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, wolthuis2014cutislaxafat pages 1-2) |
| Neuroimaging | Brain MRI with attention to ventriculomegaly, thin corpus callosum, gyral abnormalities, perivascular spaces, and intracranial arterial tortuosity | Detect characteristic CNS and vascular findings that support diagnosis and guide surveillance | MRI is recommended to assess for structural brain abnormalities and intracranial arterial tortuosity; MRI head-to-pelvis at diagnosis is specifically recommended in the Beyens review for progeroid ADCL because of cardiovascular/aneurysm risk | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, beyens2021cutislaxaa pages 12-14, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) |
| Cardiovascular evaluation | Baseline echocardiography; cardiovascular imaging, including MRI head-to-pelvis at diagnosis | Screen for cardiovascular involvement and aneurysm/vascular risk | Beyens et al. recommend baseline echocardiography for all cutis laxa subtypes and MRI head-to-pelvis at diagnosis for progeroid ADCL; intracranial arterial tortuosity is a notable clue in ALDH18A1-related ADCL3 | (beyens2021cutislaxaa pages 12-14, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) |
| Ophthalmology | Complete ophthalmologic exam with anterior chamber/slit-lamp assessment | Detect cataracts, lens opacities, corneal clouding, and other ocular complications | Ocular disease is common in ALDH18A1-related ADCL3; GeneReview excerpt specifically recommends anterior chamber evaluation for corneal clouding and lens opacities | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9, beyens2021cutislaxaa pages 25-26) |
| Orthopedic / musculoskeletal | Hip radiographs or ultrasound; cervical spine radiographs in flexion/extension; assessment for scoliosis, joint laxity, contractures | Identify hip dislocation, atlantoaxial instability, scoliosis, and connective-tissue skeletal complications | Cervical spine imaging is recommended to evaluate atlantoaxial instability; orthopedic interventions may be required in selected patients | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13) |
| Development / neurology | Full neurologic exam; developmental assessment; referral for early intervention, special education, PT/OT as indicated; EEG if seizures are suspected | Define neurodevelopmental burden and initiate supportive therapies early | Developmental delay is common; GeneReview excerpt recommends developmental assessment and EEG when clinically indicated; supportive multidisciplinary care is standard because no disease-specific guideline exists | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, fischerzirnsak2026neurocutaneousdisordersdue pages 3-5) |
| Blood pressure / vascular risk reduction | Routine blood pressure monitoring and treatment of hypertension | Minimize vascular risk in patients with arterial tortuosity or other vascular involvement | GeneReview excerpt explicitly advises blood pressure control to minimize vascular risks; practical relevance is heightened by frequent intracranial arterial tortuosity in ADCL3 | (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13, fischerzirnsak2026neurocutaneousdisordersdue pages 7-9) |
| Pulmonary / general surveillance | Consider lung function testing when age-appropriate; broader multisystem follow-up | Monitor for systemic involvement over time | Beyens et al. advise regular pulmonary, cardiovascular, and urinary assessment across cutis laxa syndromes; lung function testing is feasible from about age 8 years | (beyens2021cutislaxaa pages 12-14) |


*Table: This table summarizes the main diagnostic work-up and follow-up measures supported by the accessed review and GeneReview-style sources for ALDH18A1-related autosomal dominant cutis laxa type 3. It is useful as a practical checklist for molecular confirmation, multisystem evaluation, and ongoing surveillance.*

### 10.5 Differential diagnosis (selected)
* **PYCR1-related** recessive cutis laxa / De Barsy-like phenotypes (overlap). (fischerzirnsak2015recurrentdenovo pages 1-2, beyens2021cutislaxaa pages 4-6)
* **ALDH18A1-related autosomal recessive cutis laxa** (more severe neurodevelopmental phenotype in many reports). (beyens2021cutislaxaa pages 4-6)
* **V-ATPase / glycosylation-related cutis laxa** (may be distinguished by abnormal transferrin glycosylation in serum per expert summary). (fischerzirnsak2026neurocutaneousdisordersdue pages 7-9)

---

## 11. Outcome / prognosis
Natural history and life expectancy are not systematically quantified in the accessed ADCL3-focused primary literature. The disorder is often described as milder than recessive ALDH18A1-related ARCL3 in overall severity but includes potentially consequential vascular, neurodevelopmental, ocular, and orthopedic morbidity requiring surveillance. (beyens2021cutislaxaa pages 4-6, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

---

## 12. Treatment

### 12.1 Current standard of care (supportive)
No disease-modifying therapy or formal clinical practice guideline exists; management is supportive and multidisciplinary. (beyens2021cutislaxaa pages 12-14, fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

Key real-world implementations include:
* **Rehabilitation:** PT/OT, early developmental interventions, mobility aids as needed. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)
* **Neurology:** standard seizure management; EEG if indicated. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)
* **Orthopedics:** management of hip dislocation/scoliosis/contractures; cervical spine fusion if atlantoaxial instability is present. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)
* **Ophthalmology:** surgery for vision-impairing corneal clouding/lens opacities. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)
* **Vascular risk management:** blood pressure control to minimize vascular risks. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

### 12.2 Metabolic supplementation (experimental/low-evidence)
Citrulline and proline replacement and/or arginine supplementation have been used in some individuals in the broader mitochondrial proline synthesis defect group, but evidence is limited to case reports and clinical benefit is unconfirmed. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

### 12.3 Clinical trials
ClinicalTrials.gov searches for “cutis laxa” retrieve trials largely related to **cosmetic skin laxity** interventions and not to Mendelian ALDH18A1-related ADCL3; no ADCL3-targeted interventional trials were identified in the accessed trial corpus. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

### 12.4 MAXO terms (suggested)
* Physical therapy (MAXO:0000011)
* Occupational therapy (MAXO:0000012)
* Genetic counseling (MAXO:0000131)
* Ophthalmologic surgery (MAXO:0000799; or more specific ocular surgery terms as appropriate)
* Orthopedic surgical procedure (MAXO:0000747)
* Nutritional supplementation / amino acid supplementation (MAXO:0000095)

---

## 13. Prevention
Primary prevention is not currently available for de novo cases. **Secondary/tertiary prevention** focuses on:
* Genetic counseling and recurrence risk assessment via parental testing (recurrence risk ~1% if parents test negative due to possible gonadal mosaicism). (fischerzirnsak2026neurocutaneousdisordersdue pages 15-18)
* **Prenatal testing / preimplantation genetic testing** when a familial pathogenic variant is known. (fischerzirnsak2026neurocutaneousdisordersduef pages 15-18)
* Complication prevention through surveillance and supportive management (e.g., blood pressure control for vascular risk, early ophthalmologic care). (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13)

---

## 14. Other species / natural disease
No naturally occurring veterinary cutis laxa syndrome specifically attributed to Aldh18a1 orthologs was identified in the accessed sources.

---

## 15. Model organisms and experimental systems
Multiple experimental systems support ALDH18A1/P5CS functions relevant to human disease:

* **Drosophila + mammalian cell models (Cell Death & Differentiation; Aug 2021; URL https://doi.org/10.1038/s41418-020-0601-5):** P5CS forms mitochondrial puncta and redistributes under starvation/oxidative stress; P5CS loss affects mitochondrial respiration and causes lipid droplet phenotypes in Drosophila eyes. (yang2021pyrroline5carboxylatesynthasesenses pages 1-2)

* **Structural biology (eLife; Dec 2022; URL https://doi.org/10.7554/eLife.76107):** Cryo-EM structures of Drosophila P5CS filaments (3.1–4.3 Å) show filamentation is important for activity coordination; interface-disrupting point mutations impair filamentation and reduce enzymatic activity, relevant to human disease-associated mutations that may disrupt higher-order assembly. (zhong2022structuralbasisof pages 1-2)

* **Rodent/cell metabolic homeostasis (Scientific Reports; Jan 2021; URL https://doi.org/10.1038/s41598-020-80917-7):** P5CS can buffer glutamate by routing it into proline biosynthesis; P5CS depletion increases glutamate under stress in neuronal models, and P5CS expression increases in mouse cortex after methamphetamine exposure. (jones2021activationofproline pages 1-2)

These models support the plausibility that ALDH18A1 mutations can perturb mitochondrial organization/respiration and central amino-acid/redox metabolism, complementing patient-derived fibroblast observations in ALDH18A1-related disorders. (yang2021pyrroline5carboxylatesynthasesenses pages 1-2, zhong2022structuralbasisof pages 1-2, jones2021activationofproline pages 1-2)

---

## Evidence limitations and gaps
* Subtype-specific database identifiers (OMIM/Orphanet/ICD/MeSH) and population epidemiology were not available from the accessed corpus and should be added by direct database lookup.
* Natural history, survival, and standardized QoL metrics for ADCL3 remain sparsely documented in the accessed primary literature.
* Mechanistic links between P5CS dysfunction and intracranial arterial tortuosity are supported phenotypically but remain incompletely resolved mechanistically in the accessed sources.

---

## Key primary literature (with dates and URLs)
* **2015-09** Fischer-Zirnsak et al. *Am J Hum Genet*: “Recurrent De Novo Mutations Affecting Residue Arg138 … Cause a Progeroid Form of Autosomal-Dominant Cutis Laxa.” https://doi.org/10.1016/j.ajhg.2015.08.001 (fischerzirnsak2015recurrentdenovo pages 1-2)
* **2017-02** Bhola et al. *J Hum Genet*: “Autosomal dominant cutis laxa with progeroid features … ALDH18A1.” https://doi.org/10.1038/jhg.2017.18 (bhola2017autosomaldominantcutis pages 1-2)
* **2021-10** Beyens et al. *Clin Genet* review: “Cutis laxa: A comprehensive overview …” https://doi.org/10.1111/cge.13865 (beyens2021cutislaxaa pages 12-14)
* **2023-09** Colonna et al. *Hum Mol Genet*: “Functional Assessment … ALDH18A1 Variants …” https://doi.org/10.1093/hmg/ddac226 (colonna2023functionalassessmentof pages 1-1)

---

## Embedded clinical evidence figure/table
The defining ADCL3 cohort’s clinical and molecular summary (Table 1) is available from the 2015 AJHG paper. (fischerzirnsak2015recurrentdenovo media cda3d61e)


References

1. (fischerzirnsak2015recurrentdenovo pages 1-2): Björn Fischer-Zirnsak, Nathalie Escande-Beillard, Jaya Ganesh, Yu Xuan Tan, Mohammed Al Bughaili, Angela E. Lin, Inderneel Sahai, Paulina Bahena, Sara L. Reichert, Abigail Loh, Graham D. Wright, Jaron Liu, Elisa Rahikkala, Eniko K. Pivnick, Asim F. Choudhri, Ulrike Krüger, Tomasz Zemojtel, Conny van Ravenswaaij-Arts, Roya Mostafavi, Irene Stolte-Dijkstra, Sofie Symoens, Leila Pajunen, Lihadh Al-Gazali, David Meierhofer, Peter N. Robinson, Stefan Mundlos, Camilo E. Villarroel, Peter Byers, Amira Masri, Stephen P. Robertson, Ulrike Schwarze, Bert Callewaert, Bruno Reversade, and Uwe Kornak. Recurrent de novo mutations affecting residue arg138 of pyrroline-5-carboxylate synthase cause a progeroid form of autosomal-dominant cutis laxa. American journal of human genetics, 97 3:483-92, Sep 2015. URL: https://doi.org/10.1016/j.ajhg.2015.08.001, doi:10.1016/j.ajhg.2015.08.001. This article has 92 citations and is from a highest quality peer-reviewed journal.

2. (bhola2017autosomaldominantcutis pages 1-2): Priya T Bhola, Taila Hartley, Eric Bareke, K M Boycott, A E MacKenzie, J Majewski, M Brudno, D E Bulman, D A Dyment, Kym M Boycott, Sarah M Nikkel, and David A Dyment. Autosomal dominant cutis laxa with progeroid features due to a novel, de novo mutation in aldh18a1. Journal of Human Genetics, 62:661-663, Feb 2017. URL: https://doi.org/10.1038/jhg.2017.18, doi:10.1038/jhg.2017.18. This article has 16 citations and is from a peer-reviewed journal.

3. (beyens2021cutislaxaa pages 4-6): Aude Beyens, Annekatrien Boel, Sofie Symoens, and Bert Callewaert. Cutis laxa: a comprehensive overview of clinical characteristics and pathophysiology. Clinical Genetics, 99:53-66, Oct 2021. URL: https://doi.org/10.1111/cge.13865, doi:10.1111/cge.13865. This article has 55 citations and is from a peer-reviewed journal.

4. (bhola2017autosomaldominantcutis pages 2-3): Priya T Bhola, Taila Hartley, Eric Bareke, K M Boycott, A E MacKenzie, J Majewski, M Brudno, D E Bulman, D A Dyment, Kym M Boycott, Sarah M Nikkel, and David A Dyment. Autosomal dominant cutis laxa with progeroid features due to a novel, de novo mutation in aldh18a1. Journal of Human Genetics, 62:661-663, Feb 2017. URL: https://doi.org/10.1038/jhg.2017.18, doi:10.1038/jhg.2017.18. This article has 16 citations and is from a peer-reviewed journal.

5. (fischerzirnsak2026neurocutaneousdisordersdue pages 11-13): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

6. (fischerzirnsak2015recurrentdenovo media cda3d61e): Björn Fischer-Zirnsak, Nathalie Escande-Beillard, Jaya Ganesh, Yu Xuan Tan, Mohammed Al Bughaili, Angela E. Lin, Inderneel Sahai, Paulina Bahena, Sara L. Reichert, Abigail Loh, Graham D. Wright, Jaron Liu, Elisa Rahikkala, Eniko K. Pivnick, Asim F. Choudhri, Ulrike Krüger, Tomasz Zemojtel, Conny van Ravenswaaij-Arts, Roya Mostafavi, Irene Stolte-Dijkstra, Sofie Symoens, Leila Pajunen, Lihadh Al-Gazali, David Meierhofer, Peter N. Robinson, Stefan Mundlos, Camilo E. Villarroel, Peter Byers, Amira Masri, Stephen P. Robertson, Ulrike Schwarze, Bert Callewaert, Bruno Reversade, and Uwe Kornak. Recurrent de novo mutations affecting residue arg138 of pyrroline-5-carboxylate synthase cause a progeroid form of autosomal-dominant cutis laxa. American journal of human genetics, 97 3:483-92, Sep 2015. URL: https://doi.org/10.1016/j.ajhg.2015.08.001, doi:10.1016/j.ajhg.2015.08.001. This article has 92 citations and is from a highest quality peer-reviewed journal.

7. (fischerzirnsak2026neurocutaneousdisordersdue pages 5-7): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

8. (fischerzirnsak2026neurocutaneousdisordersdue pages 3-5): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

9. (wolthuis2014cutislaxafat pages 1-2): David F.G.J. Wolthuis, Ellyze van Asbeck, Miski Mohamed, Thatjana Gardeitchik, Elizabeth R. Lim-Melia, Ron A. Wevers, and Eva Morava. Cutis laxa, fat pads and retinopathy due to aldh18a1 mutation and review of the literature. European journal of paediatric neurology : EJPN : official journal of the European Paediatric Neurology Society, 18 4:511-5, Jul 2014. URL: https://doi.org/10.1016/j.ejpn.2014.01.003, doi:10.1016/j.ejpn.2014.01.003. This article has 59 citations.

10. (fischerzirnsak2026neurocutaneousdisordersdue pages 15-18): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

11. (beyens2021cutislaxaa pages 25-26): Aude Beyens, Annekatrien Boel, Sofie Symoens, and Bert Callewaert. Cutis laxa: a comprehensive overview of clinical characteristics and pathophysiology. Clinical Genetics, 99:53-66, Oct 2021. URL: https://doi.org/10.1111/cge.13865, doi:10.1111/cge.13865. This article has 55 citations and is from a peer-reviewed journal.

12. (fischerzirnsak2026neurocutaneousdisordersdue pages 7-9): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

13. (colonna2023functionalassessmentof pages 1-2): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 19 citations and is from a domain leading peer-reviewed journal.

14. (beyens2021cutislaxaa pages 12-14): Aude Beyens, Annekatrien Boel, Sofie Symoens, and Bert Callewaert. Cutis laxa: a comprehensive overview of clinical characteristics and pathophysiology. Clinical Genetics, 99:53-66, Oct 2021. URL: https://doi.org/10.1111/cge.13865, doi:10.1111/cge.13865. This article has 55 citations and is from a peer-reviewed journal.

15. (colonna2023functionalassessmentof pages 8-9): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 19 citations and is from a domain leading peer-reviewed journal.

16. (colonna2023functionalassessmentof pages 6-7): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 19 citations and is from a domain leading peer-reviewed journal.

17. (colonna2023functionalassessmentof pages 1-1): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 19 citations and is from a domain leading peer-reviewed journal.

18. (colonna2023functionalassessmentof pages 7-8): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 19 citations and is from a domain leading peer-reviewed journal.

19. (fischerzirnsak2026neurocutaneousdisordersduef pages 15-18): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

20. (fischerzirnsak2026neurocutaneousdisordersdueb pages 15-18): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

21. (yang2021pyrroline5carboxylatesynthasesenses pages 1-2): Zhaoying Yang, Xiaocui Zhao, Weina Shang, Yang Liu, Jun-Feng Ji, Jun-Ping Liu, and Chao Tong. Pyrroline-5-carboxylate synthase senses cellular stress and modulates metabolism by regulating mitochondrial respiration. Cell Death & Differentiation, 28:303-319, Aug 2021. URL: https://doi.org/10.1038/s41418-020-0601-5, doi:10.1038/s41418-020-0601-5. This article has 42 citations and is from a domain leading peer-reviewed journal.

22. (zhong2022structuralbasisof pages 1-2): Jiale Zhong, Chen-Jun Guo, Xian Zhou, Chia-Chun Chang, Boqi Yin, Tianyi Zhang, Huan-Huan Hu, Guang-Ming Lu, and Ji-Long Liu. Structural basis of dynamic p5cs filaments. eLife, Dec 2022. URL: https://doi.org/10.7554/elife.76107, doi:10.7554/elife.76107. This article has 31 citations and is from a domain leading peer-reviewed journal.

23. (jones2021activationofproline pages 1-2): Bobby Jones, Muthukumar Balasubramaniam, Joseph J. Lebowitz, Anne Taylor, Fernando Villalta, Habibeh Khoshbouei, Carrie Grueter, Brad Grueter, Chandravanu Dash, and Jui Pandhare. Activation of proline biosynthesis is critical to maintain glutamate homeostasis during acute methamphetamine exposure. Scientific Reports, Jan 2021. URL: https://doi.org/10.1038/s41598-020-80917-7, doi:10.1038/s41598-020-80917-7. This article has 26 citations and is from a peer-reviewed journal.