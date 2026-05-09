---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T18:34:44.317245'
end_time: '2026-05-08T18:55:34.785410'
duration_seconds: 1250.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Greig Cephalopolysyndactyly Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Greig Cephalopolysyndactyly Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Greig Cephalopolysyndactyly Syndrome** covering all of the
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
- **Disease Name:** Greig Cephalopolysyndactyly Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Greig Cephalopolysyndactyly Syndrome** covering all of the
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


# Greig Cephalopolysyndactyly Syndrome (GCPS) — Disease Characteristics Research Report

## Executive summary
Greig cephalopolysyndactyly syndrome (GCPS) is a rare, pleiotropic multiple congenital anomaly syndrome classically defined by macrocephaly, widely spaced eyes (hypertelorism/increased interpupillary distance), and limb malformations dominated by preaxial polydactyly with variable syndactyly. It is primarily caused by *GLI3* haploinsufficiency with autosomal dominant inheritance, and shows clinically important genotype–phenotype correlations based on variant type/position and variant class (sequence variants vs copy-number/structural rearrangements). Recent genomic diagnostics (2023–2024) highlight that copy-neutral inversions disrupting *GLI3* can end long “diagnostic odysseys,” underscoring the need for whole-genome sequencing (WGS) structural-variant (SV) detection and clinician–analyst review in real-world health systems. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3, pagnamenta2023conclusionofdiagnostic pages 1-1)

| Domain | Summary |
|---|---|
| Core identifiers | Disease: Greig cephalopolysyndactyly syndrome (GCPS); MONDO: MONDO:0008287; OMIM: 175700; Orphanet: ORPHA:380; primary causal gene: GLI3; inheritance: autosomal dominant |
| Common synonyms / related names | Greig syndrome; GLI3-related Greig cephalopolysyndactyly syndrome; GCPS; related/overlapping entities: preaxial polydactyly type IV (PPD-IV), GLI3-related Pallister-Hall syndrome |
| Defining clinical pattern | Classic triad: macrocephaly, widely spaced eyes/increased interpupillary distance, and limb malformations including preaxial polydactyly with or without postaxial polydactyly plus cutaneous syndactyly |
| Key clinical features with reported frequencies | Preaxial polydactyly ~90%; cutaneous syndactyly ~75%; macrocephaly ~50%; widely spaced eyes ~50%; postaxial polydactyly ~50%; broad thumb ~30%; broad hallux ~25%; corpus callosum hypoplasia/agenesis ~20%; developmental delay/intellectual disability/seizures uncommon (<10%) |
| Molecular mechanism / variant spectrum | GLI3 haploinsufficiency; pathogenic variant classes include truncating, missense, splice, exonic deletions/duplications, large deletions, translocations, and inversions; GCPS generally associated with variants 5' of nucleotide 1998 and 3' of 3481, whereas Pallister-Hall syndrome is associated with truncating variants between nucleotides 1998 and 3481 |
| Routine molecular diagnostics | Single-gene GLI3 sequencing with reflex deletion/duplication testing; multigene panels; exome sequencing; genome sequencing; chromosomal microarray (especially if developmental delay or larger deletion suspected); qPCR, long-range PCR, MLPA, targeted microarray, karyotype/FISH in selected structural cases |
| Approximate diagnostic yield by modality class | Sequence analysis identifies ~80% of pathogenic findings; gene-targeted deletion/duplication analysis identifies ~20%; karyotype-detectable rearrangements are rare |
| Notable structural variant findings | Copy-neutral inversions disrupting GLI3 identified by WGS in families with GCPS, including 1.2 Mb inversion chr7:42,051,297-43,254,780 and 14.8 Mb inversion chr7:27,245,456-42,072,394; one distal breakpoint lay ~45 kb from HOXA13; such findings resolved diagnostic odysseys of 9-20 years |
| Epidemiology | Rare disorder; prevalence/incidence generally reported as unknown in recent GeneReviews-based evidence; historical estimate range reported in review literature/definitions: ~1-9 per 1,000,000; approximately 300 affected individuals known to GeneReviews authors |
| Prognosis | Often favorable in typical GLI3-related GCPS, with mild forms, excellent general health, and normal longevity reported in large families; prognosis worsens with large (>300 kb) deletions involving GLI3, which are associated with more severe neurodevelopmental/CNS phenotypes |


*Table: This table compacts the main disease-knowledge-base facts for Greig cephalopolysyndactyly syndrome, including identifiers, phenotype frequencies, diagnostic strategy, structural variant findings, epidemiology, and prognosis. It is useful as a quick-reference scaffold for a fuller narrative report.*

---

## 1. Disease information
### 1.1 Definition / overview (current understanding)
GCPS is a “pleiotropic, multiple congenital anomaly syndrome.” (biesecker2024greigcephalopolysyndactylysyndrome pages 1-1)

A consolidated clinical definition from a GeneReviews-style synthesis describes a classic triad of **macrocephaly**, **widely spaced eyes/increased interpupillary distance**, and **preaxial polydactyly (± postaxial polydactyly) with cutaneous syndactyly**. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3, biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)

A key expert clarification is that the term **“Greig syndrome”** has sometimes been used for the *nonspecific* dyad of macrocephaly + widely spaced eyes, and “should not be used as a synonym” for the full GLI3-related GCPS phenotype. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8)

### 1.2 Key identifiers
* **MONDO**: **MONDO:0008287** (via OpenTargets disease entity) (OpenTargets Search: Greig cephalopolysyndactyly syndrome)
* **Orphanet**: **ORPHA:380** (INSERM/Orphanet source excerpt) (biesecker2024greigcephalopolysyndactylysyndrome pages 1-1)
* **OMIM**: **175700** is referenced as the GCPS entry in contemporary GLI3/GCPS literature (e.g., “GCPS, MIM: #175700”). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

**Not retrieved in the current tool run:** ICD-10/ICD-11 codes and MeSH descriptors were not directly retrieved from authoritative sources using the available evidence/tools.

### 1.3 Synonyms / alternative names
Commonly used names in the retrieved evidence include:
* **Greig cephalopolysyndactyly syndrome (GCPS)** (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)
* **GLI3-related Greig cephalopolysyndactyly syndrome (GLI3-GCPS)** (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)
* **Greig syndrome** (as a historical/colloquial term; not recommended as a synonym) (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8)

Related/overlapping entities for differential purposes include:
* **GLI3-related Pallister–Hall syndrome (GLI3-PHS)** (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8)
* **Preaxial polydactyly type IV (PPD-IV)** as part of the GLI3 phenotypic spectrum (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8)

### 1.4 Evidence-source type
The information synthesized here is derived from:
* **Aggregated disease-level resources/synthesis** (GeneReviews-style clinical genetics synthesis) (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)
* **Primary human genomics/diagnostics studies** (e.g., WGS SV inversions) (pagnamenta2023conclusionofdiagnostic pages 3-4)
* **Prenatal clinical case report (human)** with cytogenetics + array-CGH confirmation (hakcıl2024arareprenatal pages 1-2)
* **Model organism evidence (mouse *Gli3* loss-of-function)** supporting developmental mechanisms (veistinen2012lossoffunctionofgli3 pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** pathogenic variation affecting *GLI3* leading to **haploinsufficiency** (loss of one functional allele) in the typical GCPS mechanism. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

**Inheritance:** autosomal dominant with a 50% recurrence risk to offspring of an affected individual; apparent non-penetrance has been reported. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15)

**Variant classes causing GCPS:** sequence variants (including truncating/frameshift, splice, missense), intragenic deletions/duplications, larger deletions involving 7p14.1, and structural rearrangements including translocations/inversions. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

### 2.2 Risk factors
**Genetic risk factor (causal):** carrying a heterozygous pathogenic/likely pathogenic *GLI3* variant or a heterozygous deletion encompassing 7p14.1/*GLI3*. In the GeneReviews-style synthesis, ~80% of affected individuals have a heterozygous pathogenic *GLI3* variant and ~20% have a heterozygous deletion involving 7p14.1/*GLI3*. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3, biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)

**Structural variant risk (underascertained class):** copy-neutral inversions disrupting *GLI3* can cause GCPS-consistent skeletal phenotypes and are likely underdetected by CNV-biased pipelines. (pagnamenta2023conclusionofdiagnostic pages 1-1, pagnamenta2023conclusionofdiagnostic pages 4-4)

**Environmental risk factors:** none were identified in the retrieved evidence; GCPS is predominantly a Mendelian developmental disorder caused by *GLI3* disruption. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

### 2.3 Protective factors and gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes
### 3.1 Major phenotype spectrum (with frequencies when available)
A GeneReviews-style synthesis provides quantitative frequencies for select features:
* **Preaxial polydactyly** (~90%; more common in feet) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Cutaneous syndactyly** (~75%) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Macrocephaly** (~50%) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Widely spaced eyes / increased interpupillary distance** (~50%) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Postaxial polydactyly** (~50%; more common in hands) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Broad thumb** (~30%) and **broad hallux** (~25%) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Corpus callosum hypoplasia/agenesis** (~20%) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)
* **Developmental delay / intellectual disability / seizures** uncommon (~<10%), but risk increases with large deletions encompassing *GLI3*. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)

**Visual evidence:** The same synthesis includes (i) a mutational-spectrum schematic dividing GCPS vs Pallister–Hall regions and (ii) a feature-frequency table. (biesecker2025gli3relatedgreigcephalopolysyndactyly media 5cc46968, biesecker2025gli3relatedgreigcephalopolysyndactyly media 55afed63)

### 3.2 Example of prenatal phenotype (2024)
A 2024 prenatal GCPS case reported ultrasound findings including **polydactyly**, **polyhydramnios**, **aortic valve stenosis**, and nonvisualization of the **vesica biliaris**, prompting invasive testing and subsequent confirmation of a large 7p deletion encompassing *GLI3*. (hakcıl2024arareprenatal pages 2-4)

### 3.3 HPO term suggestions (non-exhaustive)
(ontology suggestions; not all are explicitly enumerated in the cited sources)
* Macrocephaly — **HP:0000256**
* Hypertelorism — **HP:0000316** / increased interpupillary distance
* Preaxial polydactyly — **HP:0100259** (hand/foot subtypes may be used)
* Postaxial polydactyly — **HP:0100258**
* Cutaneous syndactyly — **HP:0006101**
* Broad thumb — **HP:0011304**
* Broad hallux — **HP:0010055**
* Corpus callosum agenesis — **HP:0001274**
* Developmental delay — **HP:0001263**
* Seizures — **HP:0001250**
* Craniosynostosis (metopic) — **HP:0005464** (metopic ridge/trigonocephaly terms may apply in subsets)

### 3.4 Quality-of-life impact (evidence availability)
The retrieved evidence supports that many individuals have mild disease and “excellent general health and normal longevity,” implying limited systemic morbidity in typical cases, but does not provide validated quality-of-life instrument data (e.g., SF-36/EQ-5D) specific to GCPS. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
**Primary causal gene:** *GLI3* (GLI family zinc finger 3). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

OpenTargets provides a strong disease–target association of GCPS with *GLI3* (association score reported; PubMed IDs listed in evidence). (OpenTargets Search: Greig cephalopolysyndactyly syndrome)

### 4.2 Variant spectrum and functional consequences
**Mechanism:** Haploinsufficiency of *GLI3* in typical GCPS. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8)

**Genotype–phenotype correlation (variant position/type):**
* Frameshift/truncating variants in the **first third** of *GLI3* are reported as causing GCPS; truncations in the **middle third** generally cause Pallister–Hall syndrome (PHS) but can uncommonly produce GCPS; truncations in the **final third** cause GCPS. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8)
* A summarized regional model: “GCPS is primarily caused by *GLI3* pathogenic variants 5′ of nucleotide 1998 and 3′ of 3481, whereas PHS is exclusively caused by truncations between 1998 and 3481.” (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8, biesecker2025gli3relatedgreigcephalopolysyndactyly media 5cc46968)

**Copy-number/structural mechanisms:**
* Large deletions (>300 kb) encompassing *GLI3* are associated with a more severe phenotype (higher rates of intellectual disability, seizures, CNS anomalies). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)
* Copy-neutral inversions disrupting *GLI3* can be diagnostic causes in families with GCPS-consistent skeletal phenotypes; examples include a **1.2 Mb inversion** (chr7:42,051,297–43,254,780) and a **14.8 Mb inversion** (chr7:27,245,456–42,072,394). (pagnamenta2023conclusionofdiagnostic pages 3-4)

### 4.3 Pathway context (molecular mechanism)
*GLI3* is a Hedgehog (Hh) pathway transcription factor whose processing and the balance of activator vs repressor forms are critical in development; in a *Gli3* loss-of-function mouse model, loss of *Gli3* causes ectopic Hedgehog pathway activity in cranial sutural mesenchyme associated with abnormal osteogenic differentiation. (veistinen2012lossoffunctionofgli3 pages 1-2, veistinen2012lossoffunctionofgli3 pages 4-5)

**GO term suggestions (mechanism-oriented):**
* Hedgehog signaling pathway — **GO:0007224**
* Limb development — **GO:0060173** (and related patterning terms)
* Osteoblast differentiation — **GO:0001649**
* Cranial suture morphogenesis / skull development — (multiple GO options depending on curation scope)

### 4.4 Modifier genes / epigenetics
No GCPS-specific modifier genes or epigenetic signatures were identified in the retrieved evidence.

---

## 5. Environmental information
No non-genetic environmental contributors, lifestyle factors, or infectious triggers were identified in the retrieved evidence; GCPS is primarily a Mendelian disorder due to *GLI3* disruption. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (developmental mechanism)
1. **Upstream trigger:** germline loss-of-function variants or structural disruption/deletion of *GLI3* (including inversions) (pagnamenta2023conclusionofdiagnostic pages 3-4).
2. **Molecular effect:** reduced functional GLI3 dosage (haploinsufficiency) and/or altered GLI3 processing balance within Hedgehog signaling developmental programs. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8, veistinen2012lossoffunctionofgli3 pages 1-2)
3. **Cell/tissue effects:** altered patterning and differentiation in limb bud anterior–posterior axis and in craniofacial/skull development programs, with CNS structural anomalies in a subset. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)
4. **Clinical manifestations:** preaxial polydactyly ± syndactyly, craniofacial features (macrocephaly, widely spaced eyes), and sometimes corpus callosum anomalies/neurodevelopmental issues; more severe outcomes can occur with large deletions encompassing *GLI3* and adjacent genes. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

### 6.2 Evidence from a mouse model for cranial mechanism (quantitative)
In *Gli3*Xt-J/Xt-J mice (loss-of-function), ectopic osteogenic markers appear early (e.g., ectopic alkaline phosphatase staining by E13.5), heterotopic ossification is present by E16.5–E18.5, and in severe cases the interfrontal suture fuses prior to birth. (veistinen2012lossoffunctionofgli3 pages 1-2, veistinen2012lossoffunctionofgli3 pages 2-4)

Quantitatively, at E18.5 the mean width at the anterior interfrontal suture was increased in mutants (**WT 2.8 ± 0.1 mm vs *Gli3*Xt-J/Xt-J 3.5 ± 0.2 mm; P < 0.001**). (veistinen2012lossoffunctionofgli3 pages 1-2)

### 6.3 Cell types and ontology suggestions
**Cell Ontology suggestions (typical developmental actors):**
* Osteoblast — **CL:0000062**
* Osteoprogenitor cell — **CL:0000058**
* Chondrocyte — **CL:0000138**
* Cranial neural crest-derived mesenchymal cell (term selection depends on CL availability)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary systems involved include:
* **Limbs/autopod** (polydactyly, syndactyly) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* **Craniofacial/skull** (macrocephaly; cranial suture pathology in a subset; craniofacial dysmorphism) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6, veistinen2012lossoffunctionofgli3 pages 1-2)
* **Central nervous system** (corpus callosum hypoplasia/agenesis ~20%; DD/ID/seizures uncommon but present) (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)

### 7.2 UBERON term suggestions (examples)
* Hand — **UBERON:0002398**; Foot — **UBERON:0002399**
* Skull — **UBERON:0003129**
* Corpus callosum — **UBERON:0001442**

---

## 8. Temporal development
GCPS is **congenital** with manifestations detectable prenatally (e.g., polydactyly on ultrasound in some cases) and present at birth. (hakcıl2024arareprenatal pages 2-4, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15)

Course is typically **non-progressive** with respect to the congenital malformations; outcomes depend on severity, presence of CNS anomalies, and whether large deletions involve adjacent genes. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

---

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal dominant inheritance is supported by the GeneReviews-style synthesis, with **50% transmission risk** to offspring of an affected individual. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15)

### 9.2 Epidemiology
The GeneReviews-style synthesis states that prevalence is unknown and notes that “Approximately 300 affected individuals are known to the authors,” indicating ascertainment limitations and likely underdiagnosis of mild cases. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8, biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8)

**Not retrieved in this tool run:** robust population-based prevalence/incidence estimates from Orphanet/registry epidemiology fields. (The earlier “incidence range 1–9/1,000,000” is not present in the citeable evidence captured here.)

---

## 10. Diagnostics
### 10.1 Clinical diagnosis
No consensus clinical diagnostic criteria are stated to exist in the GeneReviews-style synthesis, but typical GCPS is recognized by the triad of macrocephaly, widely spaced eyes, and preaxial polydactyly with syndactyly. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3)

### 10.2 Genetic testing (real-world implementations)
**Testing modalities and approximate yields (from synthesis):**
* *GLI3* sequence analysis identifies ~80% of pathogenic variants; gene-targeted deletion/duplication testing identifies ~20%. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)
* Comprehensive approaches include multigene panels, exome sequencing (noted as most commonly used), genome sequencing, and chromosomal microarray (CMA). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3)

**Structural rearrangements and “diagnostic odysseys” (2023):**
A 2023 Journal of Medical Genetics study demonstrated that copy-neutral inversions can disrupt *GLI3* and segregate with GCPS-consistent skeletal phenotypes; the authors report two inverted segments (1.2 Mb and 14.8 Mb) disrupting *GLI3* and state these findings “resolved lengthy diagnostic odysseys of 9–20 years.” (pagnamenta2023conclusionofdiagnostic pages 1-1, pagnamenta2023conclusionofdiagnostic pages 3-4)

**Implementation lesson (quoted):** the same study explicitly notes that “copy-neutral rearrangements such as inversions are therefore likely to suffer from underascertainment,” and that a CNV-focused SV pipeline can miss these events. (pagnamenta2023conclusionofdiagnostic pages 1-1, pagnamenta2023conclusionofdiagnostic pages 4-4)

**Prenatal diagnostic workflow (2024 case):** fetal ultrasound abnormalities led to amniocentesis; initial aneuploidy testing was normal, followed by cytogenetics/FISH and array-CGH that identified a **17.4 Mb 7p12.3–14.3 deletion** including *GLI3*, interpreted as de novo after normal parental karyotypes. (hakcıl2024arareprenatal pages 1-2)

### 10.3 Differential diagnosis
Differential diagnoses listed in the GeneReviews-style synthesis include multiple polydactyly/macrocephaly syndromes and *GLI3*-allelic disorders, including GLI3-related Pallister–Hall syndrome and PPD-IV as part of the phenotypic spectrum. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8)

---

## 11. Outcome / prognosis
Typical GLI3-related GCPS can be mild: “several large families” are reported with “excellent general health and normal longevity,” while developmental delay/intellectual disability/seizures are uncommon (~<10%). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

Prognosis worsens for individuals with **large deletions (>300 kb) encompassing *GLI3***, associated with increased rates of intellectual disability, seizures, and CNS anomalies. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6)

---

## 12. Treatment
No disease-specific pharmacotherapy was identified in the retrieved evidence; management is primarily **symptomatic and surgical**.

### 12.1 Surgical and interventional
The GeneReviews-style synthesis states that treatment is symptomatic, with **plastic or orthopedic surgery** indicated for significant limb malformations. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6)

### 12.2 Supportive and rehabilitative
Supportive care is implied for neurodevelopmental issues when present (e.g., developmental assessment and services), but GCPS-specific rehabilitation outcome statistics were not found in the retrieved evidence.

### 12.3 MAXO term suggestions
* Surgical correction of polydactyly — (MAXO term selection depends on the MAXO branch; candidate: “surgical excision” / “orthopedic surgery”)
* Syndactyly release surgery — (MAXO: surgical procedure term)
* Genetic counseling — (MAXO: genetic counseling)
* Prenatal diagnosis — (MAXO: prenatal genetic testing)

---

## 13. Prevention
Primary prevention of de novo variants is not currently available; prevention in GCPS is largely **reproductive risk reduction** and **early detection**.

* **Genetic counseling** and **cascade testing** for relatives when a familial *GLI3* alteration is identified are recommended by the inheritance model and family risk structure. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15)
* **Prenatal diagnosis** and **preimplantation genetic testing** are possible when the familial pathogenic variant is known; prenatal ultrasound may detect limb/CNS features but normal ultrasound does not exclude GCPS. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15)

---

## 14. Other species / natural disease
No naturally occurring veterinary GCPS analogs were identified in the retrieved evidence.

---

## 15. Model organisms
### 15.1 Mouse models (mechanistic relevance)
A *Gli3* loss-of-function mouse allele (*Gli3*Xt-J/Xt-J) is described as a model that largely phenocopies aspects of human GCPS and is used to study craniofacial suture pathology, including premature interfrontal (metopic-equivalent) synostosis with embryonic onset. (veistinen2012lossoffunctionofgli3 pages 1-2, veistinen2012lossoffunctionofgli3 pages 2-4)

### 15.2 Model limitations
A key limitation is that *Gli3*Xt-J/Xt-J mice die at birth, limiting postnatal phenotyping and long-term outcome studies. (veistinen2012lossoffunctionofgli3 pages 4-5)

---

## Recent developments (2023–2024) — highlights
1. **WGS reveals diagnostic inversions disrupting *GLI3***: Two families with GCPS-consistent skeletal phenotypes had large, copy-neutral inversions disrupting *GLI3* (1.2 Mb and 14.8 Mb), resolving “diagnostic odysseys of 9–20 years” and demonstrating the need to improve inversion/SV detection in clinical genomics pipelines. (pagnamenta2023conclusionofdiagnostic pages 1-1, pagnamenta2023conclusionofdiagnostic pages 3-4)
2. **Prenatal GCPS confirmed via cytogenetics + array-CGH (2024)**: A fetal case with polydactyly and other ultrasound findings was confirmed to have a 17.4 Mb 7p deletion including *GLI3*, illustrating real-world prenatal diagnostic workflows beyond single-gene testing. (hakcıl2024arareprenatal pages 1-2, hakcıl2024arareprenatal pages 2-4)

---

## Evidence gaps / limitations of this report
* ICD-10/ICD-11 and MeSH identifiers were not retrieved in the citeable evidence of this tool run.
* Robust population-based prevalence/incidence estimates were not retrieved; the synthesis primarily notes rarity and ascertainment-limited counts (~300 known to authors). (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8)
* No GCPS-specific quality-of-life instrument results or pharmacologic clinical trials were found in the retrieved evidence.

---

## Key source URLs (as available in retrieved evidence)
* OpenTargets disease–target association for GCPS–*GLI3* (MONDO:0008287): https://platform.opentargets.org/ (entity surfaced via tool output) (OpenTargets Search: Greig cephalopolysyndactyly syndrome)
* Pagnamenta et al., *Journal of Medical Genetics* (published 2023; evidence excerpt): https://doi.org/10.1136/jmg-2022-108753 (pagnamenta2023conclusionofdiagnostic pages 3-4)
* Hakçıl et al., *Gazi Medical Journal* (Apr 2024): https://doi.org/10.12996/gmj.2023.4053 (hakcıl2024arareprenatal pages 1-2)
* Veistinen et al., *Frontiers in Physiology* (Feb 2012): https://doi.org/10.3389/fphys.2012.00121 (veistinen2012lossoffunctionofgli3 pages 1-2)



References

1. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 1-3): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

2. (pagnamenta2023conclusionofdiagnostic pages 1-1): Alistair T Pagnamenta, Jing Yu, Julie Evans, Philip Twiss, Amaka C Offiah, Mohamed Wafik, Sarju G Mehta, Mohammed K Javaid, Sarah F Smithson, and Jenny C Taylor. Conclusion of diagnostic odysseys due to inversions disrupting gli3 and fbn1. Journal of Medical Genetics, 60:505-510, Nov 2023. URL: https://doi.org/10.1136/jmg-2022-108753, doi:10.1136/jmg-2022-108753. This article has 15 citations and is from a domain leading peer-reviewed journal.

3. (biesecker2024greigcephalopolysyndactylysyndrome pages 1-1): LG Biesecker and JJ Johnston. Greig cephalopolysyndactyly syndrome. Definitions, Feb 2024. URL: https://doi.org/10.1007/978-1-4614-1037-9\_111, doi:10.1007/978-1-4614-1037-9\_111. This article has 75 citations.

4. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 1-3): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

5. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 6-8): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

6. (OpenTargets Search: Greig cephalopolysyndactyly syndrome): Open Targets Query (Greig cephalopolysyndactyly syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 3-6): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

8. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 6-8): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

9. (pagnamenta2023conclusionofdiagnostic pages 3-4): Alistair T Pagnamenta, Jing Yu, Julie Evans, Philip Twiss, Amaka C Offiah, Mohamed Wafik, Sarju G Mehta, Mohammed K Javaid, Sarah F Smithson, and Jenny C Taylor. Conclusion of diagnostic odysseys due to inversions disrupting gli3 and fbn1. Journal of Medical Genetics, 60:505-510, Nov 2023. URL: https://doi.org/10.1136/jmg-2022-108753, doi:10.1136/jmg-2022-108753. This article has 15 citations and is from a domain leading peer-reviewed journal.

10. (hakcıl2024arareprenatal pages 1-2): Tilbe Hakçıl, Gülsüm Kayhan, Tuncay Nas, Pınar Telli Celtemen, and Meral Yirmibeş Karaoğuz. A rare prenatal case: greig cephalopolysyndactyly syndrome. Gazi Medical Journal, 35:208-211, Apr 2024. URL: https://doi.org/10.12996/gmj.2023.4053, doi:10.12996/gmj.2023.4053. This article has 0 citations.

11. (veistinen2012lossoffunctionofgli3 pages 1-2): Lotta Veistinen, M. Takatalo, Y. Tanimoto, D. Kesper, A. Vortkamp, and D. Rice. Loss-of-function of gli3 in mice causes abnormal frontal bone morphology and premature synostosis of the interfrontal suture. Frontiers in Physiology, Feb 2012. URL: https://doi.org/10.3389/fphys.2012.00121, doi:10.3389/fphys.2012.00121. This article has 46 citations.

12. (biesecker2025gli3relatedgreigcephalopolysyndactylya pages 12-15): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

13. (pagnamenta2023conclusionofdiagnostic pages 4-4): Alistair T Pagnamenta, Jing Yu, Julie Evans, Philip Twiss, Amaka C Offiah, Mohamed Wafik, Sarju G Mehta, Mohammed K Javaid, Sarah F Smithson, and Jenny C Taylor. Conclusion of diagnostic odysseys due to inversions disrupting gli3 and fbn1. Journal of Medical Genetics, 60:505-510, Nov 2023. URL: https://doi.org/10.1136/jmg-2022-108753, doi:10.1136/jmg-2022-108753. This article has 15 citations and is from a domain leading peer-reviewed journal.

14. (biesecker2025gli3relatedgreigcephalopolysyndactyly pages 3-6): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

15. (biesecker2025gli3relatedgreigcephalopolysyndactyly media 5cc46968): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

16. (biesecker2025gli3relatedgreigcephalopolysyndactyly media 55afed63): LG Biesecker and JJ Johnston. Gli3-related greig cephalopolysyndactyly syndrome. Unknown journal, 2025.

17. (hakcıl2024arareprenatal pages 2-4): Tilbe Hakçıl, Gülsüm Kayhan, Tuncay Nas, Pınar Telli Celtemen, and Meral Yirmibeş Karaoğuz. A rare prenatal case: greig cephalopolysyndactyly syndrome. Gazi Medical Journal, 35:208-211, Apr 2024. URL: https://doi.org/10.12996/gmj.2023.4053, doi:10.12996/gmj.2023.4053. This article has 0 citations.

18. (veistinen2012lossoffunctionofgli3 pages 4-5): Lotta Veistinen, M. Takatalo, Y. Tanimoto, D. Kesper, A. Vortkamp, and D. Rice. Loss-of-function of gli3 in mice causes abnormal frontal bone morphology and premature synostosis of the interfrontal suture. Frontiers in Physiology, Feb 2012. URL: https://doi.org/10.3389/fphys.2012.00121, doi:10.3389/fphys.2012.00121. This article has 46 citations.

19. (veistinen2012lossoffunctionofgli3 pages 2-4): Lotta Veistinen, M. Takatalo, Y. Tanimoto, D. Kesper, A. Vortkamp, and D. Rice. Loss-of-function of gli3 in mice causes abnormal frontal bone morphology and premature synostosis of the interfrontal suture. Frontiers in Physiology, Feb 2012. URL: https://doi.org/10.3389/fphys.2012.00121, doi:10.3389/fphys.2012.00121. This article has 46 citations.
