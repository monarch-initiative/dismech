---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T17:36:28.790847'
end_time: '2026-05-12T17:57:01.336699'
duration_seconds: 1232.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cervical Adenocarcinoma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cervical Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Adenocarcinoma** covering all of the
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
- **Disease Name:** Cervical Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cervical Adenocarcinoma** covering all of the
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


## Comprehensive Research Report: Cervical Adenocarcinoma (Endocervical Adenocarcinoma)

### Target disease overview
Cervical adenocarcinoma (often termed **endocervical adenocarcinoma**) is a malignant epithelial tumor arising from the glandular epithelium of the uterine cervix and is now most usefully conceptualized as two biologically distinct groups: **HPV-associated (HPVA)** and **HPV-independent (HPVI)** adenocarcinomas, as formalized in the **WHO 2020 female genital tumors classification** and aligned with the **International Endocervical Adenocarcinoma Criteria and Classification (IECC)** morphology-based framework. HPVA tumors show characteristic **apical mitoses and apoptotic bodies** and include “usual type” and certain mucinous/villoglandular variants, whereas HPVI tumors lack abundant apoptosis/mitoses and include **gastric-type**, **clear cell**, **mesonephric**, and **endometrioid** subtypes. (carvalho2023prognosisdeterminationof pages 2-2, pulkkinenUnknownyearatypicalendocervicalcells pages 24-29)

**Current understanding (key concept):** HPV-association is not merely etiologic but **prognostically and therapeutically relevant**, because HPV-independent adenocarcinomas tend to present at later stage and have worse outcomes. In one cohort reclassified by WHO 2020 morphology, HPV-independent tumors had lower survival (e.g., 24-month survival 56.7% HPVI vs 76.7% HPVA; 60-month survival 42.5% vs 64.1%). (carvalho2023prognosisdeterminationof pages 3-3)

### Key identifiers, synonyms, and coding
* **Common synonyms/alternative names**: endocervical adenocarcinoma; cervical glandular carcinoma; cervical adenocarcinoma; for a major HPV-independent subtype, **gastric-type adenocarcinoma** historically overlaps with “**minimal deviation adenocarcinoma/adenoma malignum**.” (kerwin2023adenocarcinomaofthe pages 1-3)
* **ICD-O morphology codes (examples; from 2024 guideline tables)**
  * HPV-associated adenocarcinoma: **8140/3**, **8483/3**; adenocarcinoma in situ: **8140/2**, **8483/2** (sznurkowski2024thepolishsociety pages 3-4)
  * HPV-independent gastric-type adenocarcinoma: **8482/3**; gastric-type AIS: **8484/2** (sznurkowski2024thepolishsociety pages 3-4)
  * Clear cell adenocarcinoma: **8310/3**; mesonephric adenocarcinoma: **9110/3** (sznurkowski2024thepolishsociety pages 3-4)

**Unavailable in retrieved sources for this run:** explicit MONDO ID, MeSH unique IDs, ICD-10/ICD-11, and SNOMED CT codes were not present in the retrieved full-text excerpts; therefore they cannot be provided with evidence-grade citations here.

**Evidence provenance:** The report synthesizes **aggregated disease-level evidence** from WHO-aligned pathology literature, SEER population-level analyses, clinical guidelines, and trial registries; it is not derived from individual EHR patient narratives. (carvalho2023prognosisdeterminationof pages 3-3, cohen2023racialandethnic pages 4-5, NCT04221945 chunk 1)

---

## 2. Etiology

### Primary causal factors
**High-risk human papillomavirus (hrHPV)** infection is the principal etiologic factor for most cervical adenocarcinomas, particularly **usual-type HPV-associated adenocarcinoma**, with strong associations reported for **HPV16, HPV18, and HPV45**. (sznurkowski2024thepolishsociety pages 3-4, shao2024researchprogresson pages 4-4)

**Quantitative HPV association:** across studies, hrHPV positivity in endocervical adenocarcinoma is reported in the range of **~62–90% overall**, with the usual subtype showing the strongest association (**~60–95%**). HPV16 and HPV18 are dominant worldwide and together account for **~70–98.3%** of HPV-positive endocervical adenocarcinomas in reported series; multiple-genotype coinfection is described in **~10%** of adenocarcinomas. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33, sznurkowski2024thepolishsociety pages 3-4)

### HPV-negative vs HPV-independent (important distinction)
A minority of cervical cancers are truly HPV-negative; HPV-independent adenocarcinoma subtypes (notably gastric-type) can be hrHPV-negative by sensitive tests and have distinct pathogenesis and clinical behavior. A 2024 review summarizes that “an estimated **3%–8%** of cervical cancers are truly HPV-negative” (recognizing the contribution of testing false negatives and diagnostic misclassification). (shao2024researchprogresson pages 1-2)

### Risk factors and cofactors
Established cofactors that increase cervical cancer risk (including adenocarcinoma) include sexual behavior/HPV exposure dynamics, co-infections/gynecologic infections, immune suppression (including HIV), and smoking; HPV infection alone is typically insufficient for invasion without additional host cellular and immune alterations. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33)

**Special etiologic association (HPV-independent subtype):** clear cell carcinoma of the cervix is reported as associated with prior **diethylstilbestrol (DES)** exposure in a subset of cases. (shao2024researchprogresson pages 4-5)

### Protective factors
Direct quantitative protective-factor estimates for cervical adenocarcinoma specifically were not captured in the retrieved excerpts. However, population-level cervical cancer incidence reductions in vaccinated cohorts (HPV vaccination era) are consistent with prevention of HPV-associated glandular and squamous cancers; for example, US cancer statistics describe a large decline in cervical cancer incidence among the first vaccine-eligible cohort (though not adenocarcinoma-specific in the retrieved excerpt). (shao2024researchprogresson pages 4-4)

### Gene–environment interactions
Mechanistically supported, gene-by-exposure interaction estimates specific to cervical adenocarcinoma were not available in the retrieved excerpts; this remains a gap for this run.

---

## 3. Phenotypes (clinical presentation)

### Common presenting symptoms/signs
Cervical adenocarcinoma may present with abnormal uterine bleeding and/or discharge; a clinically important HPV-independent subtype (gastric-type) is frequently described with **profuse watery vaginal discharge** and abnormal bleeding. (kerwin2023adenocarcinomaofthe pages 1-3)

**Gastric-type clinical phenotype:** the cervix may appear enlarged (“barrel-shaped”), and standard screening tools may under-detect due to HPV-negativity and deep stromal growth. (kerwin2023adenocarcinomaofthe pages 1-3, kerwin2023adenocarcinomaofthe pages 3-4)

### Phenotype characteristics (typical timing)
HPV-independent adenocarcinomas are repeatedly described as presenting at **older age** and **more advanced stage** than HPV-associated tumors. (carvalho2023prognosisdeterminationof pages 3-3, shao2024researchprogresson pages 4-5)

### Suggested HPO terms (examples; to support knowledge-base annotation)
* Abnormal uterine bleeding — **HP:0000132**
* Vaginal discharge (profuse watery discharge phenotype relevant to gastric-type) — **HP:0000155**
* Pelvic pain (if present clinically; not quantified in retrieved excerpts) — **HP:0000233**
* Lymph node metastasis (disease spread phenotype) — **HP:0003003**

**Frequency/penetrance note:** symptom frequency estimates were not provided in the retrieved excerpts and cannot be reliably quantified here.

---

## 4. Genetic / Molecular information

### High-level molecular stratification
The WHO/IECC separation into HPVA vs HPVI aligns with different driver landscapes and treatment responses. In a large prospective tumor-normal sequencing cohort, subtype-associated enrichment patterns were observed, including **STK11 enrichment** in a gastric/clear cell–associated subset and **ERBB2/HER2 enrichment** in uterine endometrioid-like adenocarcinoma patterns. (friedman2023assessingthegenomic pages 11-12)

### Recurrent genes and actionable alterations (recent, clinically integrated data)
A prospective clinical sequencing study (MSK-IMPACT) integrating genomic profiling with clinical outcomes reported:
* Most prevalent alterations included **PIK3CA** and **ERBB2 (HER2)** (statement of prevalence), and quantified frequencies for key genes: **ERBB2 12% (22/177)** and **KRAS 12% (21/177)**. (friedman2023assessingthegenomic pages 2-3, friedman2023assessingthegenomic pages 11-12)
* **STK11 alterations** were enriched in a gastric/clear cell–associated subset: **33% (7/21)** versus lower rates in SCC and uterine endometrioid–like adenocarcinoma. (friedman2023assessingthegenomic pages 11-12)
* **Actionability:** **37%** of tumors had at least one potentially actionable alteration (OncoKB level 3B), and sequencing enabled trial enrollment (17% enrolled; 10% genomics-matched). (friedman2023assessingthegenomic pages 2-3)

### HPV-independent (HPV-negative) adenocarcinoma mutation patterns
A 2024 review compiled subtype-specific data indicating frequent alterations in HPV-independent gastric-type adenocarcinoma such as **TP53 (~41–53%)**, **KRAS (18–36%)**, **CDKN2A (18–27%)**, and **STK11 (10–33%)**, with **PIK3CA less frequent** in gastric type; it also summarized actionable alterations in small HPV-negative endocervical-like adenocarcinoma series (e.g., PIK3CA and PTEN at 50% each, MSI-H 12.5%). (shao2024researchprogresson pages 4-4, shao2024researchprogresson pages 4-5)

### Epigenetic information
While cervical cancer biomarker reviews emphasize epigenetic-regulator loss-of-function and pathway alterations as outcome-associated in some cervical cancers, gene-specific epigenetic mechanisms for cervical adenocarcinoma were not deeply enumerated in the retrieved excerpts. (scholl2023raidsatlasof pages 1-3)

---

## 5. Environmental information

**Infectious agent:** carcinogenic hrHPV genotypes include **16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58, 59**. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33)

**Lifestyle/environmental factors:** smoking and immune suppression are described as cofactors increasing cervical cancer risk. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33)

**Chemical exposure:** DES exposure is linked to cervical clear cell carcinoma (a rare HPV-independent glandular subtype). (shao2024researchprogresson pages 4-5)

---

## 6. Mechanism / Pathophysiology

### Causal chain (HPV-associated adenocarcinoma; conceptual)
1) Persistent infection by hrHPV (often HPV16/18/45) in cervical glandular epithelium → 2) development of glandular precursor lesions (adenocarcinoma in situ is the recognized precursor for HPV-associated adenocarcinoma) → 3) stromal invasion pattern drives metastatic risk (Silva A/B/C) → 4) lymphovascular invasion and nodal spread contribute to recurrence and mortality. (pulkkinenUnknownyearatypicalendocervicalcells pages 24-29, park2020cervicaladenocarcinomaintegration pages 11-13)

### Silva invasion patterns as a mechanism-linked risk stratifier (HPV-associated)
The **Silva pattern classification** is a morphology-based proxy for invasive behavior:
* **Pattern A:** well-demarcated glands; no destructive invasion; no single-cell detachment; no LVI; initial series showed **no nodal metastasis or recurrence**. (park2020cervicaladenocarcinomaintegration pages 11-13)
* **Pattern B:** limited destructive invasion; LVI may be present; rare node-positive cases occur; summarized outcomes include **~5% LNM, ~3% recurrence, ~1% death** in one overview. (stolnicu2021cervicalcancerwhats pages 4-6)
* **Pattern C:** diffuse destructive invasion with desmoplasia/confluence; associated with higher stage and substantially increased spread; one synthesis reports **22.5% nodal metastasis** and **19.7% recurrence**. (park2020cervicaladenocarcinomaintegration pages 11-13)

### HPV-independent gastric-type biology (conceptual)
Gastric-type adenocarcinoma is HPV-independent and often shows a pancreatobiliary/gastric-like driver spectrum (e.g., STK11, TP53, KRAS in multiple series), deep stromal infiltration with deceptively bland cytology, and may be p16-negative, contributing to under-detection in HPV-based screening. (park2020cervicaladenocarcinomaintegration pages 4-6, kerwin2023adenocarcinomaofthe pages 3-4)

### Suggested GO biological process terms (examples)
* Viral process / response to virus — **GO:0016032 / GO:0009615** (HPV-associated carcinogenesis)
* Regulation of cell cycle / apoptotic process — **GO:0051726 / GO:0006915** (consistent with morphologic hallmarks and oncogenic progression)
* Epithelial cell proliferation — **GO:0050673**

### Suggested Cell Ontology (CL) terms (examples)
* Cervical glandular epithelial cell (endocervical epithelium; may require mapping to best available CL term in your ontology stack)
* Tumor-associated macrophage / fibroblast involvement is relevant in invasion biology generally but not adenocarcinoma-specific in the retrieved excerpts.

---

## 7. Anatomical structures affected

* **Primary organ/site:** uterine cervix (endocervix). Suggested UBERON: **uterine cervix (UBERON:0000002)**.
* **Locoregional spread:** parametrial extension and pelvic lymph nodes are clinically important in more aggressive subtypes (e.g., gastric-type) and in higher-risk invasion patterns. (cho2023gastrictypeendocervicaladenocarcinoma pages 2-4, park2020cervicaladenocarcinomaintegration pages 11-13)

---

## 8. Temporal development

* **Onset:** typically adult-onset; HPV-independent tumors skew toward older age at diagnosis relative to HPV-associated tumors. (shao2024researchprogresson pages 4-5)
* **Progression:** progression risk is strongly linked to invasive pattern (Silva A/B/C) in HPV-associated adenocarcinoma, and HPV-independent tumors often present at more advanced stage. (park2020cervicaladenocarcinomaintegration pages 11-13, carvalho2023prognosisdeterminationof pages 3-3)

---

## 9. Inheritance and population

### Epidemiology and disparities (recent, authoritative population-based evidence)
A large SEER-based, hysterectomy-corrected analysis found that **cervical adenocarcinoma incidence** and **stage-specific survival** differ by race/ethnicity; importantly, Black women experienced the **lowest 5-year relative survival** for adenocarcinoma at regional/distant stages.
* **Regional-stage adenocarcinoma 5-year relative survival:** Black 37.6% vs White 61.5% vs Hispanic 65.1%. (cohen2023racialandethnic pages 4-5)
* **Distant-stage adenocarcinoma 5-year relative survival:** Black 9.2% vs White 21.1% vs Hispanic 24.9%. (cohen2023racialandethnic pages 4-5)
* In the same analysis, adenocarcinoma incidence was reported around **0.5 per 100,000** overall in the table excerpt. (cohen2023racialandethnic pages 7-8)

Visual evidence for survival/mortality patterns is shown in the extracted figure/table regions. (cohen2023racialandethnic media b2fbd237, cohen2023racialandethnic media 3662e2f0)

### Genetic inheritance
Most cervical adenocarcinoma is **not inherited in a Mendelian fashion**; it is largely infection-driven and multifactorial. Specific inherited cancer syndromes can be associated with specific subtypes (e.g., Peutz–Jeghers with gastric-type), but detailed germline penetrance statistics were not available in the retrieved excerpts. (kerwin2023adenocarcinomaofthe pages 1-3)

---

## 10. Diagnostics

### Pathology and immunohistochemistry (key clinical implementation)
**HPV-associated adenocarcinoma:** strong/diffuse **p16** is commonly used as a surrogate for HPV association; one guideline states **95%** of HPV-associated carcinomas show diffuse p16 (recognizing occasional exceptions). (sznurkowski2024thepolishsociety pages 3-4)

**HPV-independent gastric-type adenocarcinoma (GEA/GAS):**
* Often **HPV-negative** and **p16 negative or patchy**, contributing to delayed detection. (kerwin2023adenocarcinomaofthe pages 3-4, park2020cervicaladenocarcinomaintegration pages 4-6)
* Helpful immunophenotypic features include **aberrant p53** in ~40–50% and **PAX8 positivity (~68%)** in one synthesis. (park2020cervicaladenocarcinomaintegration pages 4-6)
* Additional gastric-type markers cited as useful include **TFF2, HIK1083 (~70%), Claudin 18 (~65%)**, and HPV RNA ISH is described as a sensitive HPV detection method in difficult cases. (stolnicu2021cervicalcancerwhats pages 3-4)

### Cytology (screening/diagnostic challenges; real-world implementation)
Cytologic distinction between gastric-type and usual-type adenocarcinoma has been characterized:
* Gastric-type shows **flat, honeycomb-like sheets**, **foamy/vacuolated cytoplasm**, **vesicular nuclei**, and **prominent nucleoli** more often than usual type; usual type more often shows **3D clusters**, **peripheral nuclear feathering**, and **hyperchromasia**. (cho2023gastrictypeendocervicaladenocarcinoma pages 1-2, cho2023gastrictypeendocervicaladenocarcinoma pages 2-4)

### Imaging (especially relevant to gastric-type)
Gastric-type adenocarcinoma can present as a **multicystic cervical mass with solid components**; **MRI** is emphasized as the preferred modality to identify solid components and define extent, supporting differentiation from benign multicystic lesions. (kerwin2023adenocarcinomaofthe pages 1-3)

### Differential diagnosis (not exhaustive)
HPV-independent gastric-type carcinoma can be confused with benign glandular lesions (e.g., LEGH) and requires deep sampling plus immunostain correlation; endometrial adenocarcinoma involving cervix is a recognized misclassification issue in HPV-negative cases. (stolnicu2021cervicalcancerwhats pages 3-4, shao2024researchprogresson pages 1-2)

---

## 11. Outcome / prognosis

### HPV-associated vs HPV-independent prognosis
Reclassification by WHO 2020 morphology is prognostically informative; HPV-independent tumors show worse crude survival and present at more advanced stage. In one cohort, mean OS was **73.3 months (HPVA) vs 42.4 months (HPVI)** and the HPVI group had lower 24- and 60-month survival. (carvalho2023prognosisdeterminationof pages 3-3)

### Invasion-pattern (Silva) prognosis (HPV-associated)
Silva pattern C is associated with substantially higher nodal metastasis and recurrence than pattern A; pattern A predicts excellent prognosis and may support conservative management in selected settings. (park2020cervicaladenocarcinomaintegration pages 11-13, stolnicu2023villoglandularpatternin pages 6-8)

### Disparities
SEER data show profound race/ethnicity disparities in regional/distant adenocarcinoma survival as above. (cohen2023racialandethnic pages 4-5)

---

## 12. Treatment

### Standard of care (real-world implementation)
**Locally advanced cervical cancer (including adenocarcinoma histology)**: long-standing cornerstone is **concurrent cisplatin-based chemoradiation followed by brachytherapy**. (ketch2024pharmacotherapyforcervical pages 1-3, sznurkowski2024thepolishsociety pages 1-2)

### Recent developments (priority 2023–2024)
#### Pembrolizumab + chemoradiation (KEYNOTE-A18; practice-changing)
The phase 3, randomized, double-blind KEYNOTE-A18 trial (NCT04221945) evaluated adding **pembrolizumab** to standard chemoradiotherapy with subsequent maintenance pembrolizumab in **high-risk locally advanced** cervical cancer (including squamous, adenocarcinoma, and adenosquamous histologies). (NCT04221945 chunk 2)
* Trial schema and dosing are described in the registry record (pembrolizumab 200 mg Q3W during CRT then 400 mg Q6W maintenance; cisplatin 40 mg/m² weekly + EBRT + brachytherapy). (NCT04221945 chunk 1)
* A linked trial record excerpt reports an **11% absolute 2-year PFS benefit (68% vs 57%)** with ~17.9 months median follow-up. (NCT07368985 chunk 1)

#### Induction chemotherapy before chemoradiation (INTERLACE)
A 2024 expert review summarized INTERLACE: induction weekly dose-dense paclitaxel + carboplatin before chemoradiation improved long-term outcomes (5-year PFS 73% vs 64%; OS 80% vs 72%). Importantly, adenocarcinoma histology was included among eligible histologies. (ang2024evolvingstandardsand pages 1-2)

#### Antibody–drug conjugate: tisotumab vedotin (Tivdak)
* innovaTV 204 (NCT03438396): single-arm phase 2 in previously treated recurrent/metastatic cervical cancer; primary endpoint confirmed objective response by independent review. (NCT03438396 chunk 1)
* innovaTV 301 (NCT04697628): randomized open-label phase 3 comparing tisotumab vedotin vs investigator-choice chemotherapy; primary endpoint overall survival. (NCT04697628 chunk 1)
* A 2024 review reports key efficacy benchmarks: ORR **24%** and DOR **8.3 months** in innovaTV204; and interim innovaTV301 OS **11.5 vs 9.5 months** (HR 0.70) and PFS **4.2 vs 2.9 months** (HR 0.67). (ang2024evolvingstandardsand pages 4-5)

#### Chemo-immunotherapy + anti-VEGF combinations (advanced disease)
A 2024 review reported BEATcc outcomes for adding atezolizumab to bevacizumab + platinum-taxane chemotherapy: median PFS **13.7 vs 10.4 months** (HR 0.62) and OS **32.1 vs 22.8 months** (HR 0.68). (ang2024evolvingstandardsand pages 4-5)

#### Precision oncology (HER2 and others)
Routine tumor genomic profiling can identify targetable alterations; a 2023 prospective sequencing cohort emphasized HER2-directed opportunities and recommended routine HER2 evaluation in advanced/recurrent disease to facilitate targeted trial access. (friedman2023assessingthegenomic pages 17-18)

### Suggested MAXO terms (examples)
* Concurrent chemoradiotherapy — **MAXO:0000045 (radiotherapy)** + **MAXO:0000058 (chemotherapy)** (map to your specific MAXO version)
* Brachytherapy — **MAXO term for brachytherapy/radiotherapy procedure**
* Immune checkpoint inhibitor therapy (anti–PD-1) — **MAXO term for immunotherapy**
* Antibody–drug conjugate therapy — **MAXO term for targeted drug delivery/antibody therapy**

---

## 13. Prevention

**Primary prevention:** HPV vaccination prevents HPV16/18/45-associated cervical cancers; broad vaccination impact is reflected in population statistics showing large declines in cervical cancer incidence in vaccine-era cohorts (not adenocarcinoma-specific in the retrieved excerpt). (shao2024researchprogresson pages 4-4)

**Secondary prevention/screening:** HPV-based screening is effective for HPV-associated lesions but may under-detect HPV-independent adenocarcinomas (notably gastric-type) because HPV testing can be negative and lesions can be deeply infiltrative with bland cytology; conization and MRI correlation are often needed for suspected gastric-type disease. (kerwin2023adenocarcinomaofthe pages 3-4, kerwin2023adenocarcinomaofthe pages 1-3)

---

## 14. Other species / natural disease
No evidence on naturally occurring cervical adenocarcinoma in non-human species was retrieved in the current tool run; therefore no evidence-grade comparative species claims are made.

---

## 15. Model organisms / model systems
The retrieved excerpts did not provide a focused, evidence-backed summary of cervical adenocarcinoma model organisms (e.g., specific PDX/organoid systems) beyond noting that preclinical validation and PDX work exist in other cervical cancer histologies (not adenocarcinoma-specific in the extracted evidence). (friedman2023assessingthegenomic pages 2-3)

---

## Expert synthesis and analysis (authoritative perspectives, 2023–2024 emphasis)
1) **Pathology has shifted from morphology-only subtyping to etiology-linked classification (HPVA vs HPVI)** because it better captures clinically meaningful differences (age/stage at presentation, prognosis, and potential targetable biology). (carvalho2023prognosisdeterminationof pages 2-2, park2020cervicaladenocarcinomaintegration pages 11-13)
2) **HPV-independent gastric-type disease is a key unmet need** due to frequent screening negativity (p16-/HPV-) and deep infiltrative growth; multimodality diagnosis (deep biopsy/cone + immunostains + MRI) is essential. (kerwin2023adenocarcinomaofthe pages 3-4, kerwin2023adenocarcinomaofthe pages 1-3)
3) **2023–2024 systemic-therapy landscape is rapidly changing**: pembrolizumab added to definitive chemoradiation (KEYNOTE-A18) represents a major shift in locally advanced disease management, while ADCs (tisotumab vedotin) and combination immuno-antiangiogenic regimens (BEATcc) are expanding options in recurrent/metastatic disease. (NCT07368985 chunk 1, ang2024evolvingstandardsand pages 4-5, ketch2024pharmacotherapyforcervical pages 1-3)

---

## High-yield facts summary table
| Topic | Key points (concise) | Quantitative data | Source (first author year) | URL |
|---|---|---|---|---|
| High-yield facts for cervical adenocarcinoma | WHO 2020/IECC classifies endocervical adenocarcinoma into HPV-associated (defined morphologically by apical mitoses/apoptotic bodies; includes usual type and mucinous/villoglandular variants) versus HPV-independent (includes gastric, clear cell, mesonephric, endometrioid/NOS); HPV-independent tumors present older/at higher stage and have worse survival. (carvalho2023prognosisdeterminationof pages 2-2, pistolesi2023cervicaladenocarcinomaa pages 1-2, carvalho2023prognosisdeterminationof pages 3-3) | In one 2023 cohort: 24-month survival 76.7% HPVA vs 56.7% HPVI; 60-month survival 64.1% vs 42.5%; mean OS 73.3 vs 42.4 months. | Carvalho 2023 | https://doi.org/10.1002/ijgo.14442 |
| HPV genotype association | Most cervical adenocarcinomas are HPV-associated; dominant genotypes are HPV16, HPV18, and HPV45, with HPV18 relatively enriched in adenocarcinoma. hrHPV prevalence is lower than in squamous carcinoma and drops sharply in HPV-independent histologies. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33, sznurkowski2024thepolishsociety pages 3-4, shao2024researchprogresson pages 4-4) | Overall hrHPV positivity in endocervical adenocarcinoma ~62–90%; usual type 60–95%; HPV16/18 together account for ~70–98.3% of HPV-positive cases; multiple HPV coinfection ~10%. | Shao 2024 / Sznurkowski 2024 | https://doi.org/10.1097/md.0000000000039957 ; https://doi.org/10.3390/jcm13154351 |
| Gastric-type adenocarcinoma (GAS) | Rare HPV-independent mucinous endocervical adenocarcinoma, historically including “adenoma malignum/minimal deviation adenocarcinoma”; often bland cytology, deep stromal infiltration, and aggressive behavior. (kerwin2023adenocarcinomaofthe pages 1-3, kerwin2023adenocarcinomaofthe pages 3-4) | HPV-independent tumors ~15% of endocervical adenocarcinomas; GAS ~10–15% of cervical adenocarcinomas; reported 5-year disease-specific survival 38% for GAS vs 74% for non-gastric types; biopsy sensitivity ≈50%. | Kerwin 2023 | https://doi.org/10.1007/s00261-022-03724-w |
| Silva pattern A/B/C | Silva classification applies to HPV-associated adenocarcinoma: A = non-destructive invasion; B = limited destructive invasion; C = diffuse destructive invasion/desmoplasia. Risk rises from A to C and informs conservative vs more extensive surgery. (park2020cervicaladenocarcinomaintegration pages 11-13, stolnicu2021cervicalcancerwhats pages 4-6, pistolesi2023cervicaladenocarcinomaa pages 1-2) | Pattern A: no nodal metastasis or recurrence in initial series; Pattern B: ~5% lymph node metastasis, ~3% recurrence, ~1% death; Pattern C: ~22.5% nodal metastasis and ~19.7% recurrence. | Park 2020 / Stolnicu 2021 | https://doi.org/10.1111/his.13995 ; https://doi.org/10.1016/j.mpdhp.2021.09.002 |
| SEER racial disparities | Population-based SEER analysis showed major racial disparities in cervical adenocarcinoma survival; Black women had the worst stage-specific outcomes despite not having the highest incidence. (cohen2023racialandethnic pages 4-5, cohen2023racialandethnic pages 7-8, cohen2023racialandethnic pages 1-2) | Regional adenocarcinoma 5-year relative survival: Black 37.6% vs White 61.5% vs Hispanic 65.1%; distant: Black 9.2% vs White 21.1% vs Hispanic 24.9%. Overall adenocarcinoma incidence ~0.5/100,000. | Cohen 2023 | https://doi.org/10.1200/JCO.22.01424 |
| Genomics and actionability | Prospective sequencing identified recurrent actionable alterations; ERBB2 and KRAS were common, and STK11 was enriched in gastric/clear cell-associated subset. Sequencing enabled trial matching in routine practice. (friedman2023assessingthegenomic pages 11-12, friedman2023assessingthegenomic pages 17-18, friedman2023assessingthegenomic pages 2-3) | ERBB2 12% (22/177), KRAS 12% (21/177), STK11 33% in CAS (7/21); 37% had ≥1 potentially actionable alteration; 17% enrolled on trials, 10% matched by sequencing. | Friedman 2023 | https://doi.org/10.1158/1078-0432.CCR-23-1078 |
| KEYNOTE-A18 | Phase 3 randomized double-blind study of pembrolizumab plus standard cisplatin-based chemoradiotherapy followed by maintenance pembrolizumab vs placebo plus chemoradiotherapy in newly diagnosed high-risk locally advanced cervical cancer; eligible histologies included squamous, adenocarcinoma, and adenosquamous. (NCT04221945 chunk 1, NCT07368985 chunk 1, NCT04221945 chunk 2) | Enrollment 1,060; reported 2-year PFS 68% vs 57% (absolute benefit 11%); primary endpoints PFS and OS. | Merck/NCT04221945 2020 | https://clinicaltrials.gov/study/NCT04221945 |
| innovaTV 301 | Phase 3 randomized open-label trial of tisotumab vedotin vs investigator’s-choice chemotherapy in second-/third-line recurrent or metastatic cervical cancer. Published interim efficacy figures were highlighted in 2024 review. (ang2024evolvingstandardsand pages 4-5, NCT04697628 chunk 6, NCT04697628 chunk 1) | Enrollment 502; interim OS 11.5 vs 9.5 months (HR 0.70); PFS 4.2 vs 2.9 months (HR 0.67). | Ang 2024 / NCT04697628 | https://doi.org/10.3802/jgo.2024.35.e65 ; https://clinicaltrials.gov/study/NCT04697628 |
| innovaTV 204 | Multicenter open-label single-arm phase 2 trial of tisotumab vedotin in previously treated recurrent/metastatic cervical cancer. (NCT03438396 chunk 1, NCT03438396 chunk 3) | Enrollment 102; tisotumab vedotin 2.0 mg/kg IV every 3 weeks; primary endpoint confirmed objective response by independent review per RECIST v1.1. | Seagen/NCT03438396 2018 | https://clinicaltrials.gov/study/NCT03438396 |
| BEATcc | First-line advanced cervical cancer trial adding atezolizumab to bevacizumab plus platinum-taxane chemotherapy; 2024 review identified this as practice changing. (ang2024evolvingstandardsand pages 4-5) | Median PFS 13.7 vs 10.4 months (HR 0.62); median OS 32.1 vs 22.8 months (HR 0.68). | Ang 2024 | https://doi.org/10.3802/jgo.2024.35.e65 |
| Tisotumab vedotin efficacy signal | Anti–tissue factor ADC with clinically meaningful single-agent activity in pretreated recurrent/metastatic cervical cancer; activity summarized in 2024 review and supported later by phase 3 data. (ang2024evolvingstandardsand pages 4-5) | ORR 24%; median duration of response 8.3 months in innovaTV204. | Ang 2024 | https://doi.org/10.3802/jgo.2024.35.e65 |


*Table: This table compiles high-yield, citation-backed facts on classification, epidemiology, pathology, genomics, and recent therapeutic trials in cervical adenocarcinoma. It is designed as a compact reference for rapid knowledge-base entry and clinical/research orientation.*

---

## Key statistics (quick reference)
* hrHPV positivity in endocervical adenocarcinoma: **~62–90% overall**, usual type **~60–95%**. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33)
* HPV16/18 attribution among HPV-positive EAC: **~70–98.3%**. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33)
* Gastric-type proportion: **~10–15%** of cervical adenocarcinomas; HPV-independent tumors **~15%** of endocervical adenocarcinomas. (kerwin2023adenocarcinomaofthe pages 1-3)
* Silva Pattern C: nodal metastasis risk reported **~22.5%**; recurrence **~19.7%** (HPV-associated). (park2020cervicaladenocarcinomaintegration pages 11-13)
* SEER regional-stage adenocarcinoma 5-year survival: Black **37.6%** vs White **61.5%** vs Hispanic **65.1%**. (cohen2023racialandethnic pages 4-5, cohen2023racialandethnic media b2fbd237)
* KEYNOTE-A18 linked excerpt: 2-year PFS **68% vs 57%** (absolute +11%). (NCT07368985 chunk 1)

---

## Direct abstract quotes (for evidence traceability)
* Park (Histopathology, 2020) emphasizes classification transformation: “*separation of cervical adenocarcinomas into HPV‐associated (HPVA) and HPV‐independent has resulted in a transformation of the classification system for cervical adenocarcinomas*.” ()
* Friedman (Clin Cancer Res, 2023) describes clinical utility of prospective profiling: “*Tumor genomic profiling can facilitate the selection of targeted/immunotherapies, as well as clinical trial enrollment, for patients with cervical cancer*.” (friedman2023assessingthegenomic pages 2-3)

(Note: quotes are limited to abstracts/excerpts available in the retrieved context; additional primary-abstract quotations for other topics would require retrieval of the corresponding full abstracts.)

---

## URLs (selected)
* Cohen et al., J Clin Oncol, 2023-02 — https://doi.org/10.1200/JCO.22.01424 (cohen2023racialandethnic pages 4-5)
* Friedman et al., Clin Cancer Res, 2023-08 — https://doi.org/10.1158/1078-0432.CCR-23-1078 (friedman2023assessingthegenomic pages 2-3)
* Kerwin et al., Abdominal Radiology, 2023-11 — https://doi.org/10.1007/s00261-022-03724-w (kerwin2023adenocarcinomaofthe pages 1-3)
* Park, Histopathology, 2020-12 — https://doi.org/10.1111/his.13995 (park2020cervicaladenocarcinomaintegration pages 11-13)
* KEYNOTE-A18 trial registry — https://clinicaltrials.gov/study/NCT04221945 (NCT04221945 chunk 1)
* innovaTV 301 registry — https://clinicaltrials.gov/study/NCT04697628 (NCT04697628 chunk 1)
* innovaTV 204 registry — https://clinicaltrials.gov/study/NCT03438396 (NCT03438396 chunk 1)


References

1. (carvalho2023prognosisdeterminationof pages 2-2): Carla Fabrine Carvalho, Larissa Bastos Eloy Costa, Natasha Caroline Sanches, Ingrid Iara Damas, Liliana Aparecida Lucci De Angelo Andrade, and Diama Bhadra Vale. Prognosis determination of endocervical adenocarcinomas morphologically reclassified as <scp>hpv</scp> associated or <scp>hpv</scp> independent. Sep 2023. URL: https://doi.org/10.1002/ijgo.14442, doi:10.1002/ijgo.14442. This article has 4 citations and is from a peer-reviewed journal.

2. (pulkkinenUnknownyearatypicalendocervicalcells pages 24-29): J PULKKINEN. Atypical endocervical cells in pap smears. Unknown journal, Unknown year.

3. (carvalho2023prognosisdeterminationof pages 3-3): Carla Fabrine Carvalho, Larissa Bastos Eloy Costa, Natasha Caroline Sanches, Ingrid Iara Damas, Liliana Aparecida Lucci De Angelo Andrade, and Diama Bhadra Vale. Prognosis determination of endocervical adenocarcinomas morphologically reclassified as <scp>hpv</scp> associated or <scp>hpv</scp> independent. Sep 2023. URL: https://doi.org/10.1002/ijgo.14442, doi:10.1002/ijgo.14442. This article has 4 citations and is from a peer-reviewed journal.

4. (kerwin2023adenocarcinomaofthe pages 1-3): Clara M. Kerwin, Matt Markese, Marisa R. Moroney, Lynelle P. Smith, and Nayana U. Patel. Adenocarcinoma of the uterine cervix, gastric-type (gas): a review of the literature focused on pathology and multimodality imaging. Abdominal Radiology, 48:713-723, Nov 2023. URL: https://doi.org/10.1007/s00261-022-03724-w, doi:10.1007/s00261-022-03724-w. This article has 23 citations and is from a peer-reviewed journal.

5. (sznurkowski2024thepolishsociety pages 3-4): Jacek J. Sznurkowski, Lubomir Bodnar, Łukasz Szylberg, Agnieszka Zołciak-Siwinska, Anna Dańska-Bidzińska, Dagmara Klasa-Mazurkiewicz, Agnieszka Rychlik, Artur Kowalik, Joanna Streb, Mariusz Bidziński, and Włodzimierz Sawicki. The polish society of gynecological oncology guidelines for the diagnosis and treatment of cervical cancer (v2024.0). Journal of Clinical Medicine, 13:4351, Jul 2024. URL: https://doi.org/10.3390/jcm13154351, doi:10.3390/jcm13154351. This article has 10 citations.

6. (cohen2023racialandethnic pages 4-5): Camryn M. Cohen, Nicolas Wentzensen, Philip E. Castle, Mark Schiffman, Rosemary Zuna, Rebecca C. Arend, and Megan A. Clarke. Racial and ethnic disparities in cervical cancer incidence, survival, and mortality by histologic subtype. Journal of Clinical Oncology, 41:1059-1068, Feb 2023. URL: https://doi.org/10.1200/jco.22.01424, doi:10.1200/jco.22.01424. This article has 171 citations and is from a highest quality peer-reviewed journal.

7. (NCT04221945 chunk 1):  Study of Chemoradiotherapy With or Without Pembrolizumab (MK-3475) For The Treatment of Locally Advanced Cervical Cancer (MK-3475-A18/KEYNOTE-A18/ENGOT-cx11/GOG-3047). Merck Sharp & Dohme LLC. 2020. ClinicalTrials.gov Identifier: NCT04221945

8. (shao2024researchprogresson pages 4-4): Ning Shao. Research progress on human papillomavirus-negative cervical cancer: a review. Medicine, 103:e39957, Oct 2024. URL: https://doi.org/10.1097/md.0000000000039957, doi:10.1097/md.0000000000039957. This article has 11 citations and is from a peer-reviewed journal.

9. (pulkkinenUnknownyearatypicalendocervicalcells pages 29-33): J PULKKINEN. Atypical endocervical cells in pap smears. Unknown journal, Unknown year.

10. (shao2024researchprogresson pages 1-2): Ning Shao. Research progress on human papillomavirus-negative cervical cancer: a review. Medicine, 103:e39957, Oct 2024. URL: https://doi.org/10.1097/md.0000000000039957, doi:10.1097/md.0000000000039957. This article has 11 citations and is from a peer-reviewed journal.

11. (shao2024researchprogresson pages 4-5): Ning Shao. Research progress on human papillomavirus-negative cervical cancer: a review. Medicine, 103:e39957, Oct 2024. URL: https://doi.org/10.1097/md.0000000000039957, doi:10.1097/md.0000000000039957. This article has 11 citations and is from a peer-reviewed journal.

12. (kerwin2023adenocarcinomaofthe pages 3-4): Clara M. Kerwin, Matt Markese, Marisa R. Moroney, Lynelle P. Smith, and Nayana U. Patel. Adenocarcinoma of the uterine cervix, gastric-type (gas): a review of the literature focused on pathology and multimodality imaging. Abdominal Radiology, 48:713-723, Nov 2023. URL: https://doi.org/10.1007/s00261-022-03724-w, doi:10.1007/s00261-022-03724-w. This article has 23 citations and is from a peer-reviewed journal.

13. (friedman2023assessingthegenomic pages 11-12): Claire F. Friedman, Vignesh Ravichandran, Kathryn Miller, Chad Vanderbilt, Qin Zhou, Alexia Iasonos, Malavika Vivek, Pamela Mishra, Mario M. Leitao, Vance Broach, Yukio Sonoda, Chrisann Kyi, Dmitriy Zamarin, Roisin E. O'Cearbhaill, Jason Konner, Michael F. Berger, Britta Weigelt, Amir Momeni Boroujeni, Kay J. Park, Carol Aghajanian, David B. Solit, and Mark T.A. Donoghue. Assessing the genomic landscape of cervical cancers: clinical opportunities and therapeutic targets. Clinical Cancer Research, 29:4660-4668, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1078, doi:10.1158/1078-0432.ccr-23-1078. This article has 23 citations and is from a highest quality peer-reviewed journal.

14. (friedman2023assessingthegenomic pages 2-3): Claire F. Friedman, Vignesh Ravichandran, Kathryn Miller, Chad Vanderbilt, Qin Zhou, Alexia Iasonos, Malavika Vivek, Pamela Mishra, Mario M. Leitao, Vance Broach, Yukio Sonoda, Chrisann Kyi, Dmitriy Zamarin, Roisin E. O'Cearbhaill, Jason Konner, Michael F. Berger, Britta Weigelt, Amir Momeni Boroujeni, Kay J. Park, Carol Aghajanian, David B. Solit, and Mark T.A. Donoghue. Assessing the genomic landscape of cervical cancers: clinical opportunities and therapeutic targets. Clinical Cancer Research, 29:4660-4668, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1078, doi:10.1158/1078-0432.ccr-23-1078. This article has 23 citations and is from a highest quality peer-reviewed journal.

15. (scholl2023raidsatlasof pages 1-3): Suzy Scholl, Diana Bello Roufai, Linda Larbi Chérif, and Maud Kamal. Raids atlas of significant genetic and protein biomarkers in cervical cancer. Journal of Gynecologic Oncology, Aug 2023. URL: https://doi.org/10.3802/jgo.2023.34.e74, doi:10.3802/jgo.2023.34.e74. This article has 4 citations and is from a peer-reviewed journal.

16. (park2020cervicaladenocarcinomaintegration pages 11-13): Kay J. Park. Cervical adenocarcinoma: integration of hpv status, pattern of invasion, morphology and molecular markers into classification. Histopathology, 76:112-127, Dec 2020. URL: https://doi.org/10.1111/his.13995, doi:10.1111/his.13995. This article has 155 citations and is from a domain leading peer-reviewed journal.

17. (stolnicu2021cervicalcancerwhats pages 4-6): Simona Stolnicu. Cervical cancer: what's new in classification, morphology, molecular findings and prognosis of glandular precursor and invasive lesions. Diagnostic Histopathology, 27:483-492, Dec 2021. URL: https://doi.org/10.1016/j.mpdhp.2021.09.002, doi:10.1016/j.mpdhp.2021.09.002. This article has 4 citations.

18. (park2020cervicaladenocarcinomaintegration pages 4-6): Kay J. Park. Cervical adenocarcinoma: integration of hpv status, pattern of invasion, morphology and molecular markers into classification. Histopathology, 76:112-127, Dec 2020. URL: https://doi.org/10.1111/his.13995, doi:10.1111/his.13995. This article has 155 citations and is from a domain leading peer-reviewed journal.

19. (cho2023gastrictypeendocervicaladenocarcinoma pages 2-4): HAEYON CHO, SUJIN PARK, and HYUN-SOO KIM. Gastric-type endocervical adenocarcinoma: comprehensive cytopathological analysis and comparison with usual-type endocervical adenocarcinoma. In Vivo, 37:1173-1181, Jan 2023. URL: https://doi.org/10.21873/invivo.13192, doi:10.21873/invivo.13192. This article has 10 citations and is from a peer-reviewed journal.

20. (cohen2023racialandethnic pages 7-8): Camryn M. Cohen, Nicolas Wentzensen, Philip E. Castle, Mark Schiffman, Rosemary Zuna, Rebecca C. Arend, and Megan A. Clarke. Racial and ethnic disparities in cervical cancer incidence, survival, and mortality by histologic subtype. Journal of Clinical Oncology, 41:1059-1068, Feb 2023. URL: https://doi.org/10.1200/jco.22.01424, doi:10.1200/jco.22.01424. This article has 171 citations and is from a highest quality peer-reviewed journal.

21. (cohen2023racialandethnic media b2fbd237): Camryn M. Cohen, Nicolas Wentzensen, Philip E. Castle, Mark Schiffman, Rosemary Zuna, Rebecca C. Arend, and Megan A. Clarke. Racial and ethnic disparities in cervical cancer incidence, survival, and mortality by histologic subtype. Journal of Clinical Oncology, 41:1059-1068, Feb 2023. URL: https://doi.org/10.1200/jco.22.01424, doi:10.1200/jco.22.01424. This article has 171 citations and is from a highest quality peer-reviewed journal.

22. (cohen2023racialandethnic media 3662e2f0): Camryn M. Cohen, Nicolas Wentzensen, Philip E. Castle, Mark Schiffman, Rosemary Zuna, Rebecca C. Arend, and Megan A. Clarke. Racial and ethnic disparities in cervical cancer incidence, survival, and mortality by histologic subtype. Journal of Clinical Oncology, 41:1059-1068, Feb 2023. URL: https://doi.org/10.1200/jco.22.01424, doi:10.1200/jco.22.01424. This article has 171 citations and is from a highest quality peer-reviewed journal.

23. (stolnicu2021cervicalcancerwhats pages 3-4): Simona Stolnicu. Cervical cancer: what's new in classification, morphology, molecular findings and prognosis of glandular precursor and invasive lesions. Diagnostic Histopathology, 27:483-492, Dec 2021. URL: https://doi.org/10.1016/j.mpdhp.2021.09.002, doi:10.1016/j.mpdhp.2021.09.002. This article has 4 citations.

24. (cho2023gastrictypeendocervicaladenocarcinoma pages 1-2): HAEYON CHO, SUJIN PARK, and HYUN-SOO KIM. Gastric-type endocervical adenocarcinoma: comprehensive cytopathological analysis and comparison with usual-type endocervical adenocarcinoma. In Vivo, 37:1173-1181, Jan 2023. URL: https://doi.org/10.21873/invivo.13192, doi:10.21873/invivo.13192. This article has 10 citations and is from a peer-reviewed journal.

25. (stolnicu2023villoglandularpatternin pages 6-8): Simona Stolnicu, Maria J. Brito, Georgia Karpathiou, Lynn Hoang, Ana Felix, Claudia Mateoiu, Daniela Fanni, Armando Reques, Angel Garcia, David Hardisson, Canan K. Talu, Antonia Furtado, Nadeem Abu-Rustum, Robert A. Soslow, and Kay J. Park. Villoglandular pattern in hpv-associated endocervical adenocarcinoma is associated with excellent prognosis: a reappraisal of 31 cases using iecc and silva pattern classification. International Journal of Gynecological Pathology, 42:270-277, Nov 2023. URL: https://doi.org/10.1097/pgp.0000000000000916, doi:10.1097/pgp.0000000000000916. This article has 10 citations and is from a peer-reviewed journal.

26. (ketch2024pharmacotherapyforcervical pages 1-3): Peter W. Ketch, Rennan S. Zaharias, and Charles A. Leath. Pharmacotherapy for cervical cancer: current standard of care and new perspectives. Expert Opinion on Pharmacotherapy, 25:1591-1603, Aug 2024. URL: https://doi.org/10.1080/14656566.2024.2395379, doi:10.1080/14656566.2024.2395379. This article has 2 citations and is from a peer-reviewed journal.

27. (sznurkowski2024thepolishsociety pages 1-2): Jacek J. Sznurkowski, Lubomir Bodnar, Łukasz Szylberg, Agnieszka Zołciak-Siwinska, Anna Dańska-Bidzińska, Dagmara Klasa-Mazurkiewicz, Agnieszka Rychlik, Artur Kowalik, Joanna Streb, Mariusz Bidziński, and Włodzimierz Sawicki. The polish society of gynecological oncology guidelines for the diagnosis and treatment of cervical cancer (v2024.0). Journal of Clinical Medicine, 13:4351, Jul 2024. URL: https://doi.org/10.3390/jcm13154351, doi:10.3390/jcm13154351. This article has 10 citations.

28. (NCT04221945 chunk 2):  Study of Chemoradiotherapy With or Without Pembrolizumab (MK-3475) For The Treatment of Locally Advanced Cervical Cancer (MK-3475-A18/KEYNOTE-A18/ENGOT-cx11/GOG-3047). Merck Sharp & Dohme LLC. 2020. ClinicalTrials.gov Identifier: NCT04221945

29. (NCT07368985 chunk 1): Prof. Dr. Remi A. Nout. Pembrolizumab and Lenvatinib in Patients With High Risk Locally Advanced Cervix Cancer. Prof. Dr. Remi A. Nout. 2026. ClinicalTrials.gov Identifier: NCT07368985

30. (ang2024evolvingstandardsand pages 1-2): Daniel Jia Ming Ang and Jack Junjie Chan. Evolving standards and future directions for systemic therapies in cervical cancer. Journal of Gynecologic Oncology, Jan 2024. URL: https://doi.org/10.3802/jgo.2024.35.e65, doi:10.3802/jgo.2024.35.e65. This article has 21 citations and is from a peer-reviewed journal.

31. (NCT03438396 chunk 1):  A Trial of Tisotumab Vedotin in Cervical Cancer. Seagen Inc.. 2018. ClinicalTrials.gov Identifier: NCT03438396

32. (NCT04697628 chunk 1):  Tisotumab Vedotin vs Chemotherapy in Recurrent or Metastatic Cervical Cancer. Seagen, a wholly owned subsidiary of Pfizer. 2021. ClinicalTrials.gov Identifier: NCT04697628

33. (ang2024evolvingstandardsand pages 4-5): Daniel Jia Ming Ang and Jack Junjie Chan. Evolving standards and future directions for systemic therapies in cervical cancer. Journal of Gynecologic Oncology, Jan 2024. URL: https://doi.org/10.3802/jgo.2024.35.e65, doi:10.3802/jgo.2024.35.e65. This article has 21 citations and is from a peer-reviewed journal.

34. (friedman2023assessingthegenomic pages 17-18): Claire F. Friedman, Vignesh Ravichandran, Kathryn Miller, Chad Vanderbilt, Qin Zhou, Alexia Iasonos, Malavika Vivek, Pamela Mishra, Mario M. Leitao, Vance Broach, Yukio Sonoda, Chrisann Kyi, Dmitriy Zamarin, Roisin E. O'Cearbhaill, Jason Konner, Michael F. Berger, Britta Weigelt, Amir Momeni Boroujeni, Kay J. Park, Carol Aghajanian, David B. Solit, and Mark T.A. Donoghue. Assessing the genomic landscape of cervical cancers: clinical opportunities and therapeutic targets. Clinical Cancer Research, 29:4660-4668, Aug 2023. URL: https://doi.org/10.1158/1078-0432.ccr-23-1078, doi:10.1158/1078-0432.ccr-23-1078. This article has 23 citations and is from a highest quality peer-reviewed journal.

35. (pistolesi2023cervicaladenocarcinomaa pages 1-2): SABINA PISTOLESI, GIUSEPPE NICOLÒ FANELLI, FRANCESCO GIUDICE, FRANCESCA GARBINI, ANTONIO GIUSEPPE NACCARATO, STEFANIA COSIO, MARTA CARETTO, and ANGIOLO GADDUCCI. Cervical adenocarcinoma: a still under-investigated malignancy. AntiCancer Research, 43:53-58, Dec 2023. URL: https://doi.org/10.21873/anticanres.16133, doi:10.21873/anticanres.16133. This article has 3 citations and is from a peer-reviewed journal.

36. (cohen2023racialandethnic pages 1-2): Camryn M. Cohen, Nicolas Wentzensen, Philip E. Castle, Mark Schiffman, Rosemary Zuna, Rebecca C. Arend, and Megan A. Clarke. Racial and ethnic disparities in cervical cancer incidence, survival, and mortality by histologic subtype. Journal of Clinical Oncology, 41:1059-1068, Feb 2023. URL: https://doi.org/10.1200/jco.22.01424, doi:10.1200/jco.22.01424. This article has 171 citations and is from a highest quality peer-reviewed journal.

37. (NCT04697628 chunk 6):  Tisotumab Vedotin vs Chemotherapy in Recurrent or Metastatic Cervical Cancer. Seagen, a wholly owned subsidiary of Pfizer. 2021. ClinicalTrials.gov Identifier: NCT04697628

38. (NCT03438396 chunk 3):  A Trial of Tisotumab Vedotin in Cervical Cancer. Seagen Inc.. 2018. ClinicalTrials.gov Identifier: NCT03438396