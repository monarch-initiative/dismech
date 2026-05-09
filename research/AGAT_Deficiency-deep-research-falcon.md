---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-02T23:38:50.863036'
end_time: '2026-05-02T23:48:43.874766'
duration_seconds: 593.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: AGAT Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AGAT Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **AGAT Deficiency** covering all of the
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
- **Disease Name:** AGAT Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **AGAT Deficiency** covering all of the
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


# AGAT Deficiency (GATM-related creatine synthesis defect) — Comprehensive Disease Characteristics Report

**Target disease:** AGAT Deficiency (autosomal recessive creatine biosynthesis disorder; a cerebral creatine deficiency disorder). (mulik2023creatinedeficiencydisorders pages 2-3, longo2011disordersofcreatine pages 2-3)

**Key recent sources prioritized:**
- ClinGen CCDS Variant Curation Expert Panel (VCEP) specifications for **GATM** variant interpretation (May 2024). (goldstein2024clingenvariantcuration pages 3-4)
- Review of creatine deficiency disorders (Mar 2023). (mulik2023creatinedeficiencydisorders pages 2-3)
- CCDS diagnostic implementation statistics (Swiss laboratory study, Jan 2025). (kaufman2025diagnosticdelayin pages 1-2)
- MRS case report demonstrating treatment response (Dec 2024). (garg2024magneticresonancespectroscopy pages 2-4)

---

## 1. Disease Information

### 1.1 Definition / overview
AGAT deficiency is an ultrarare **inborn error of creatine biosynthesis** caused by biallelic loss-of-function variants in **GATM**, encoding **L-arginine:glycine amidinotransferase (AGAT)**, the first step in creatine synthesis. It causes **cerebral creatine deficiency** detectable by proton magnetic resonance spectroscopy (1H-MRS) and a neurodevelopmental phenotype (developmental delay/intellectual disability with prominent speech-language impairment), often with myopathy/proximal weakness. (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, longo2011disordersofcreatine pages 2-3)

### 1.2 Key identifiers and ontologies
- **MONDO:** **MONDO:0012996 (AGAT deficiency)** (from Open Targets disease-target association output). (ndika2012developmentalprogressand pages 1-2)
- **OMIM (disease):** **612718** (AGAT deficiency) (longo2011disordersofcreatine pages 2-3)
- **OMIM (gene):** **GATM 602360** (mulik2023creatinedeficiencydisorders pages 2-3)

**Not retrieved in this tool run (needs external lookup to complete):** Orphanet ID, MeSH ID, ICD-10/ICD-11 codes.

### 1.3 Synonyms / alternative names
- **L-arginine:glycine amidinotransferase deficiency** (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **GATM-related creatine deficiency / creatine synthesis defect** (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Cerebral creatine deficiency disorder/syndrome (CCDD/CCDS)**, enzyme-defect subgroup (kaufman2025diagnosticdelayin pages 1-2)

**Note:** The synonym “cerebral creatine deficiency syndrome 3” appears in a CCDS case-report context (garg2024magneticresonancespectroscopy pages 2-4) but was not consistently used across the core genetics/biochemical literature retrieved here.

### 1.4 Evidence sources (patient-level vs aggregated)
Most clinical knowledge is derived from **individual case reports and small case series** (e.g., 16 patients worldwide in a 2015 cohort) and synthesized in reviews and expert-consensus variant interpretation guidance (ClinGen VCEP). (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, goldstein2024clingenvariantcuration pages 3-4)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **GATM** leading to deficient AGAT enzyme activity (loss of function), impairing endogenous creatine synthesis. (mulik2023creatinedeficiencydisorders pages 2-3, goldstein2024clingenvariantcuration pages 3-4)

**Authoritative expert consensus (ClinGen VCEP, 2024):** the panel “determined loss-of-function is the disease mechanism” for GATM and applies the ACMG/AMP PVS1 framework to null variants expected to undergo NMD. (goldstein2024clingenvariantcuration pages 3-4)

### 2.2 Risk factors
- **Genetic risk factor:** inheriting two pathogenic **GATM** alleles (autosomal recessive). Heterozygous parents are typically asymptomatic. (mulik2023creatinedeficiencydisorders pages 2-3)
- **Consanguinity:** reported in at least one adult case report family structure. (verma2010arginineglycineamidinotransferasedeficiency pages 1-3)

No specific environmental/exogenous risk factors were identified in the retrieved evidence; AGAT deficiency is primarily a Mendelian enzymatic disorder.

### 2.3 Protective factors
No validated protective genetic variants or environmental protective factors were identified in the retrieved human evidence.

**Model-organism inference:** systemic AGAT deficiency in mice was associated with protection from metabolic syndrome (a separate phenotype outside the core neurodevelopmental disorder), suggesting complex systemic metabolic consequences of creatine depletion. (ndika2012developmentalprogressand pages 1-2)

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence specific to AGAT deficiency was identified in the retrieved literature.

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum
Across the largest human cohort retrieved (n=16), the dominant presentation was neurodevelopmental impairment with frequent myopathy:
- **Intellectual disability/developmental delay:** 15/16 patients. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Myopathy/proximal muscle weakness:** 8/16 patients. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Language delay / severe speech-language disorder:** commonly reported. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, pintilie2021ararebut pages 4-5)
- **Behavioral/psychiatric features (including autistic-like features):** reported in multiple families/reviews. (pintilie2021ararebut pages 4-5, ndika2012developmentalprogressand pages 1-2)
- **Seizures:** rare/variable; present in some reports. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, ndika2012developmentalprogressand pages 1-2)

### 3.2 Age of onset, severity, and progression
- **Age at diagnosis** has ranged from **3 weeks to 23 years** across early literature summarized in a case report review. (ndika2012developmentalprogressand pages 5-6)
- Adult presentations emphasizing **insidious proximal weakness** beginning in late adolescence/early adulthood have been described. (verma2010arginineglycineamidinotransferasedeficiency pages 1-3)
- Neurodevelopmental outcomes are strongly **time-dependent** with treatment initiation (see Treatment section). (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

### 3.3 Laboratory/biochemical phenotypes (laboratory abnormalities)
- **Low/undetectable guanidinoacetate (GAA) in urine and plasma** is a hallmark. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, mulik2023creatinedeficiencydisorders pages 2-3)
- **Low (or low-normal) creatine** in body fluids and **absent/markedly reduced brain creatine peak** by 1H-MRS. (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3)

### 3.4 Suggested HPO terms (non-exhaustive)
Based on retrieved clinical descriptions:
- Developmental delay — **HP:0001263** (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- Intellectual disability — **HP:0001249** (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- Speech delay / severe speech impairment — **HP:0000750** (speech delay) / **HP:0002463** (aphasia may be too specific) (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- Hypotonia — **HP:0001252** (ndika2012developmentalprogressand pages 1-2)
- Proximal muscle weakness / myopathy — **HP:0003701** (proximal muscle weakness) / **HP:0003198** (myopathy) (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- Seizures — **HP:0001250** (ndika2012developmentalprogressand pages 1-2)
- Autistic-like behavior / behavioral abnormality — **HP:0000729** (autistic behavior) / **HP:0000708** (behavioral abnormality) (pintilie2021ararebut pages 4-5)

**Note:** HPO IDs are standard ontology suggestions; the supporting evidence for the phenotype presence is from the cited papers above.

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene
- **Gene:** **GATM** (encodes AGAT; mitochondrial glycine amidinotransferase). (longo2011disordersofcreatine pages 2-3)

### 4.2 Inheritance
- **Autosomal recessive** inheritance with **biallelic pathogenic variants**. (mulik2023creatinedeficiencydisorders pages 2-3, goldstein2024clingenvariantcuration pages 3-4)

### 4.3 Pathogenic variant spectrum and examples
Reported variant types include truncating/null variants, missense variants, and splice variants. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 5-7)

Examples explicitly mentioned in retrieved evidence:
- **c.484+1G>T** (splice) in a long-term supplementation case series context. (ndika2012developmentalprogressand pages 1-2)
- **p.W149X** (nonsense) reported in the Longo review excerpt and as a shared variant in an Italian family follow-up cohort (p.Trp149*). (longo2011disordersofcreatine pages 2-3, battini2017fifteenyearfollowupof pages 2-4)
- **1111_1112insA** (frameshift insertion) in a two-patient report. (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2)
- **R169X** (nonsense) in an adult-onset myopathy report. (verma2010arginineglycineamidinotransferasedeficiency pages 1-3)

### 4.4 Variant interpretation guidance (expert consensus; 2024)
The **ClinGen CCDS VCEP** created **gene- and disease-specific ACMG/AMP specifications** for **GATM**, explicitly integrating disease biomarkers (GAA/creatine in body fluids and brain MRS creatine) into phenotype evidence (PP4) via a points-based system. (goldstein2024clingenvariantcuration pages 8-9, goldstein2024clingenvariantcuration pages 13-18)

Key quantitative thresholds reported for GATM by the VCEP include:
- **Estimated prevalence** used for calculations: **1 in 3,450,000** (goldstein2024clingenvariantcuration pages 4-6)
- Allele frequency thresholds: **BA1 >0.0005**, **BS1 >0.0001**, **PM2_supporting <0.000055**. (goldstein2024clingenvariantcuration pages 13-18)

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal abnormalities specific to AGAT deficiency were identified in the retrieved evidence.

---

## 5. Environmental Information
No disease-specific environmental toxins, lifestyle contributors, or infectious triggers were identified in the retrieved evidence. AGAT deficiency is primarily a genetic enzymatic deficiency. (mulik2023creatinedeficiencydisorders pages 2-3, goldstein2024clingenvariantcuration pages 3-4)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core biochemical pathway defect
AGAT catalyzes the first and rate-limiting step of creatine biosynthesis:
- **Arginine + glycine → guanidinoacetate (GAA) + ornithine**. (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2, verma2010arginineglycineamidinotransferasedeficiency pages 1-3)

Loss of AGAT activity causes:
- **Marked reduction of GAA** production (low/undetectable GAA in urine/plasma). (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Secondary creatine deficiency**, including in brain, detectable as absent/markedly reduced creatine signal by 1H-MRS. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3)

### 6.2 Causal chain (upstream → downstream)
- **Upstream trigger:** biallelic loss-of-function variants in GATM → reduced/absent AGAT enzyme function. (goldstein2024clingenvariantcuration pages 3-4)
- **Metabolic consequence:** low GAA and deficient creatine synthesis → inadequate creatine/phosphocreatine availability, particularly in energy-demanding tissues (brain, muscle). (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Clinical consequence:** neurodevelopmental impairment with major speech/language deficits and myopathy/proximal weakness; seizures variably. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

### 6.3 Key biochemical abnormalities (diagnostic biomarkers)
- Low/undetectable GAA in plasma/urine and low creatine; absent or markedly decreased brain creatine peak on 1H-MRS. (mulik2023creatinedeficiencydisorders pages 2-3)

### 6.4 Suggested GO and CL terms (mechanism-oriented suggestions)
- **GO:0006600** creatine biosynthetic process (general) (supported conceptually by creatine synthesis defect described in multiple sources). (mulik2023creatinedeficiencydisorders pages 2-3, edvardson2010larginineglycineamidinotransferase(agat) pages 1-2)
- **GO:0003848** arginine:glycine amidinotransferase activity (enzyme function) (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2)
- **CL terms (likely impacted cell types):**
  - Neurons (e.g., cortical neurons) and skeletal muscle myocytes as high-energy demand cell types implicated by clinical phenotype and MRS/myopathy findings. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Central nervous system:** cerebral creatine deficiency on MRS, neurodevelopmental phenotype. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3, garg2024magneticresonancespectroscopy pages 2-4)
- **Skeletal muscle:** proximal myopathy/weakness in many patients; adult myopathy presentations reported. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, verma2010arginineglycineamidinotransferasedeficiency pages 1-3)

### 7.2 Suggested UBERON terms (examples)
- Brain — **UBERON:0000955** (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3)
- Skeletal muscle tissue — **UBERON:0001134** (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

### 7.3 Subcellular localization (suggested)
AGAT is encoded by mitochondrial glycine amidinotransferase (gene-level description in review literature), suggesting mitochondrial relevance in creatine biosynthesis and cellular energy buffering. (longo2011disordersofcreatine pages 2-3)

---

## 8. Temporal Development

### 8.1 Onset
Common onset is in infancy/early childhood with developmental delay and speech delay, though diagnosis may occur later and adult-onset myopathy has been described. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, verma2010arginineglycineamidinotransferasedeficiency pages 1-3, ndika2012developmentalprogressand pages 5-6)

### 8.2 Progression/course
- Without early treatment, persistent neurocognitive and language deficits may occur. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, battini2017fifteenyearfollowupof pages 7-8)
- With treatment, cerebral creatine can be replenished over months (tracked by serial MRS), and muscle symptoms may improve relatively rapidly. (verma2010arginineglycineamidinotransferasedeficiency pages 1-3, battini2017fifteenyearfollowupof pages 4-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (rarity)
AGAT deficiency is consistently described as **ultrarare**, with <20–25 individuals reported in the literature in recent summaries. (mulik2023creatinedeficiencydisorders pages 2-3, goldstein2024clingenvariantcuration pages 1-3)

### 9.2 Prevalence / carrier frequency estimates
- A 2023 review reports an **estimated carrier frequency of 0.077%** (method not detailed in excerpt). (mulik2023creatinedeficiencydisorders pages 2-3)
- ClinGen VCEP (for variant-frequency threshold setting) used an **estimated prevalence of 1 in 3,450,000** for GATM-related disease. (goldstein2024clingenvariantcuration pages 4-6)

### 9.3 Penetrance/expressivity
ClinGen VCEP treated biallelic pathogenic variants in GATM as **fully penetrant** for purposes of allele-frequency calculations and variant interpretation (maximum genetic contribution and penetrance set to 100%). (goldstein2024clingenvariantcuration pages 4-6)

---

## 10. Diagnostics

### 10.1 Core diagnostic tests and biomarkers
**Biochemical testing**
- **Urine and plasma GAA and creatine** measurements are central; low/undetectable GAA with low creatine supports AGAT deficiency. (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

**Neuroimaging**
- **1H-MRS:** absent/markedly decreased brain creatine peak is a hallmark; MRI can be normal. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3, garg2024magneticresonancespectroscopy pages 2-4)

**Genetic confirmation**
- **GATM sequencing** (single gene, panel, WES/WGS) to confirm biallelic pathogenic variants. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8)

**Functional confirmation**
- In uncertain genetic cases, **AGAT enzyme activity in fibroblasts** may help resolve interpretation. (mulik2023creatinedeficiencydisorders pages 2-3, goldstein2024clingenvariantcuration pages 13-18)

### 10.2 Real-world diagnostic implementation and delays (statistics)
A Swiss cross-sectional/systems study (2015–2023) on cerebral creatine deficiency disorders reported:
- Diagnostic/therapeutic delay **3–32 months (mean 13.8 months)** in their cohort. (kaufman2025diagnosticdelayin pages 1-2)
- Total **4,967** guanidinoacetate and creatine measurements performed (urine+plasma) across two Swiss centers (2015–2023). (kaufman2025diagnosticdelayin pages 4-5)
- Testing volume increased from **312 analyses (2015) to 883 (2023)**. (kaufman2025diagnosticdelayin pages 2-4)
- **Urine** is described as “the preferred sample for CCDD detection” and “clearly the best matrix for the initial selective screening.” (kaufman2025diagnosticdelayin pages 1-2, kaufman2025diagnosticdelayin pages 6-8)

### 10.3 Differential diagnosis (high-level)
AGAT deficiency should be differentiated from other cerebral creatine deficiency disorders:
- **GAMT deficiency** (elevated GAA rather than low) and **SLC6A8 creatine transporter deficiency** (different urine creatine/creatinine patterns; often poor response to creatine). (mulik2023creatinedeficiencydisorders pages 1-2, kaufman2025diagnosticdelayin pages 1-2)

### 10.4 Screening
**Newborn screening feasibility and challenges**
- The 2015 cohort argues AGAT deficiency is “an ideal candidate for newborn screening” because early treatment can prevent adverse outcomes, but notes it is “difficult to devise a sensitive screening algorithm based on GAA quantitation alone,” proposing multianalyte DBS algorithms or enzyme assay approaches. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8)

---

## 11. Outcome / Prognosis

### 11.1 Prognosis with treatment (long-term data)
A 15-year follow-up cohort (Italy; 4 patients) indicates:
- Long-term oral creatine is generally **safe and well tolerated**; renal function was preserved with monitoring, though occasional kidney stones and other side effects occurred. (battini2017fifteenyearfollowupof pages 4-7)
- Early treatment can prevent adverse developmental outcomes; later-treated patients often have persistent neurocognitive deficits, but adaptive functioning can improve. (battini2017fifteenyearfollowupof pages 1-2)

### 11.2 Prognostic factors
**Age at treatment initiation** is repeatedly highlighted as the dominant prognostic factor for neurocognitive outcomes. (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)

---

## 12. Treatment

### 12.1 Standard-of-care pharmacotherapy
**Creatine monohydrate supplementation** is the main disease-specific therapy.

**Dosing ranges reported across studies:**
- **100–800 mg/kg/day** across cohorts and reviews. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, mulik2023creatinedeficiencydisorders pages 2-3)
- A 2023 review states: “**While all 3 disorders are currently treated with creatine supplementation**,” and specifies for AGAT deficiency that oral creatine has been used and benefit depends on early initiation. (mulik2023creatinedeficiencydisorders pages 1-2)

**Evidence for time-dependent neurocognitive benefit (review):**
- Cognitive restoration reported when treatment started **<2 years**, but not when started after age **10** in the 2023 review summary. (mulik2023creatinedeficiencydisorders pages 2-3)

**Long-term treatment strategies / tapering (Italian follow-up cohort):**
- Symptomatic patients began at ~**400 mg/kg/day**, later reduced to **200–300 mg/kg/day**, then **100 mg/kg/day** guided by MRS and biochemical monitoring. (battini2017fifteenyearfollowupof pages 1-2)

### 12.2 Treatment outcomes
- Creatine supplementation often increases cerebral creatine on MRS and improves myopathy; however, complete normalization of cerebral creatine is not universal even with very high doses. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8)
- In an MRS-focused clinical case report (44-month-old), pretreatment MRS had no definable creatine peak at 3.0 ppm and follow-up MRS at 5 months showed reappearance of the creatine peak after supplementation. (garg2024magneticresonancespectroscopy pages 2-4)

### 12.3 Adverse effects and monitoring
Reported adverse events/side effects with chronic creatine therapy include:
- **Weight gain**, **polyuria/polydipsia**, **transient diarrhea** with dose increases, **urinary creatine crystals**, and **kidney stones** (at least one asymptomatic). (battini2017fifteenyearfollowupof pages 4-7, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8)

Monitoring strategies include serial urine/plasma creatine and GAA and periodic MRS (1H/31P) to track brain replenishment and guide dosing. (battini2017fifteenyearfollowupof pages 4-7)

### 12.4 Pregnancy management (real-world implementation)
A pregnancy case report (2020) describes a woman with AGAT deficiency requiring close monitoring due to increased creatine demand:
- Abstract quote: “**Biochemical monitoring of Cr in biological fluids of the mother revealed a decline of the Cr concentrations… requiring prompt correction of the Cr dose.**” (Sep 2020). (alessandri2020increasedcreatinedemand pages 1-2)
- The mother’s creatine dose was increased (e.g., to 3 g/day mid-pregnancy), and the infant had normal brain creatine and typical developmental milestones at one year. (alessandri2020increasedcreatinedemand pages 2-4, alessandri2020increasedcreatinedemand pages 1-2)

### 12.5 Suggested MAXO terms (treatment action ontology; suggestions)
- **Creatine supplementation therapy** (oral) (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2)
- **Magnetic resonance spectroscopy monitoring** (treatment-response monitoring) (battini2017fifteenyearfollowupof pages 4-7)
- **Genetic counseling** (autosomal recessive disorder; prenatal testing possible when familial variants known) (mulik2023creatinedeficiencydisorders pages 2-3)

---

## 13. Prevention

### 13.1 Primary/secondary prevention
No primary prevention exists for a Mendelian enzymatic deficiency, but **secondary prevention** via **early detection and early creatine supplementation** is repeatedly emphasized.

**Early treatment prevention concept:**
- A 2023 review notes the disorders are treatable with creatine, and early treatment in AGAT deficiency can prevent adverse outcomes. (mulik2023creatinedeficiencydisorders pages 2-3)
- A 2015 cohort states: “**Early treatment seems to prevent adverse developmental outcomes.**” (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8)

### 13.2 Newborn screening implementation
- **Early Check expanded newborn screening program** includes AGAT deficiency on its screening panel and operationalizes confirmatory testing and genetic counseling after positive screens (observational cohort; estimated enrollment 30,000 newborns). (NCT03655223 chunk 2)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary cases were retrievable in the accessible full texts for this run (a relevant 2026 dog paper was listed as unobtainable by the search tool). Therefore, no curated cross-species natural disease entry can be provided from the current evidence set.

---

## 15. Model Organisms

### 15.1 Mouse model evidence
An AGAT-deficient mouse model has been used to study systemic creatine depletion and metabolic consequences; one study reports that **AGAT deficiency protects from metabolic syndrome** (model-organism phenotype not directly equivalent to the human neurodevelopmental disorder but informative for systemic pathway biology). (ndika2012developmentalprogressand pages 1-2)

---

## Key abstract quotes (supporting major claims)

1. **Creatine deficiency disorders review (Mar 2023):**
- “**Biallelic pathogenic variants in GATM result in l-arginine:glycine amidinotransferase deficiency.**” (mulik2023creatinedeficiencydisorders pages 2-3)

2. **Pregnancy in AGAT deficiency (Sep 2020):**
- “**Biochemical monitoring of Cr in biological fluids of the mother revealed a decline of the Cr concentrations… requiring prompt correction of the Cr dose.**” (alessandri2020increasedcreatinedemand pages 1-2)

3. **Long-term Italian follow-up (Feb 2017):**
- “**Consecutive MRS examinations have confirmed that Cr depletion in AGAT-d patients is reversible under Cr supplementation.**” (ndika2012developmentalprogressand pages 1-2)

---

## Summary artifact
The following table provides a compact disease knowledge-base-ready summary (identifiers, biomarkers, phenotypes, diagnostics, dosing, outcomes, screening):

| Domain | Key facts | Key sources (citation ids) | URLs/publication years when available |
|---|---|---|---|
| Disease/identifiers | AGAT deficiency is a GATM-related cerebral creatine deficiency disorder, inherited in an autosomal recessive manner; reported as ultrarare with fewer than 20-25 patients/individuals described in the literature. OMIM identifiers reported in gathered evidence include AGAT deficiency OMIM #612718 and GATM gene OMIM #602360. MONDO association evidence supports MONDO:0012996 for AGAT deficiency. | (mulik2023creatinedeficiencydisorders pages 2-3, mulik2023creatinedeficiencydisorders pages 1-2, longo2011disordersofcreatine pages 2-3) | Mulik 2023: https://doi.org/10.5152/turkarchpediatr.2023.23022; Longo 2011: https://doi.org/10.1002/ajmg.c.30292; Open Targets evidence includes MONDO_0012996 |
| Gene/mechanism | GATM encodes AGAT, the first/rate-limiting enzyme of creatine biosynthesis, catalyzing arginine + glycine to guanidinoacetate (GAA) and ornithine. Disease mechanism is loss of function; ClinGen CCDS VCEP applies PVS1 to GATM and considers AGAT deficiency a fully penetrant autosomal recessive creatine synthesis disorder. | (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2, goldstein2024clingenvariantcuration pages 3-4, goldstein2024clingenvariantcuration pages 4-6) | Edvardson 2010: https://doi.org/10.1016/j.ymgme.2010.06.021; Goldstein 2024: https://doi.org/10.1016/j.ymgme.2024.108362 |
| Biochemical signature | Hallmark profile: very low/undetectable GAA in urine and plasma, low or low-normal creatine/creatinine in urine, plasma, and sometimes CSF, with absent or markedly decreased brain creatine peak on 1H-MRS. Pretreatment cerebral creatine is markedly reduced or absent in essentially all studied patients. | (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 5-7, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3) | Mulik 2023: https://doi.org/10.5152/turkarchpediatr.2023.23022; Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003 |
| Core phenotypes | Most common manifestations are developmental delay/intellectual disability and severe speech/language delay; behavioral problems/autistic-like features are frequent. Myopathy/proximal muscle weakness occurs in about half of reported patients or 8/16 in the largest series; hypotonia, failure to thrive/low weight, and rare seizures have also been reported. | (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, pintilie2021ararebut pages 4-5, verma2010arginineglycineamidinotransferasedeficiency pages 1-3, ndika2012developmentalprogressand pages 5-6) | Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; Pintilie 2021: https://doi.org/10.37897/rjp.2021.3.4; Verma 2010: https://doi.org/10.1212/wnl.0b013e3181e7cabd; Ndika 2012: https://doi.org/10.1016/j.ymgme.2012.01.017 |
| Onset/natural history | Age at diagnosis reported from 3 weeks to 23 years. Early infancy/childhood presentations predominate, but adult-onset or later-recognized myopathy has been described. Untreated disease can lead to persistent cognitive/language impairment; early-treated infants can remain asymptomatic or achieve normal neurodevelopment. | (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, verma2010arginineglycineamidinotransferasedeficiency pages 1-3, ndika2012developmentalprogressand pages 5-6, battini2017fifteenyearfollowupof pages 1-2) | Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; Verma 2010: https://doi.org/10.1212/wnl.0b013e3181e7cabd; Ndika 2012: https://doi.org/10.1016/j.ymgme.2012.01.017; Battini 2017: https://doi.org/10.1186/s13023-017-0577-5 |
| Diagnostics | Recommended workup includes urine and plasma GAA/creatine testing, brain 1H-MRS to document absent or reduced creatine peak, and confirmatory GATM sequencing; WES/WGS are alternatives. Functional confirmation can include AGAT enzyme activity in fibroblasts when variants are uncertain. ClinGen 2024 formalized phenotype/biomarker-based PP4 scoring using low GAA, low creatine, MRS findings, and enzyme activity. | (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8, goldstein2024clingenvariantcuration pages 8-9, goldstein2024clingenvariantcuration pages 13-18) | Mulik 2023: https://doi.org/10.5152/turkarchpediatr.2023.23022; Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; Goldstein 2024: https://doi.org/10.1016/j.ymgme.2024.108362 |
| MRS implementation | Brain MRI may be normal, but MRS is highly informative: absent/undefinable creatine peak at ~3.0 ppm is a characteristic finding, and follow-up MRS can document reappearance of the peak after treatment. | (garg2024magneticresonancespectroscopy pages 4-5, garg2024magneticresonancespectroscopy pages 2-4, garg2024magneticresonancespectroscopy pages 1-2) | Garg 2024: https://doi.org/10.25259/crcr_92_2024 |
| Treatment | Main disease-specific therapy is oral creatine monohydrate supplementation. Dosing reported across studies ranges from 100-800 mg/kg/day; common long-term regimens include ~400 mg/kg/day initially with later taper to 200-100 mg/kg/day based on MRS/biochemical monitoring. Adult case reports also used 5 g/day with later escalation to weight-based dosing. | (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 3-4, battini2017fifteenyearfollowupof pages 1-2, battini2017fifteenyearfollowupof pages 7-8) | Mulik 2023: https://doi.org/10.5152/turkarchpediatr.2023.23022; Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; Battini 2017: https://doi.org/10.1186/s13023-017-0577-5 |
| Treatment outcomes | Creatine supplementation significantly improves or normalizes muscle function in most patients and increases cerebral creatine on MRS, but complete normalization is not universal even at high doses. Developmental/cognitive outcomes are strongly time-dependent: treatment begun in infancy (<2 years in review evidence; as early as 4-16 months in case series) can prevent adverse neurodevelopmental outcomes, whereas treatment started after ~10 years yields limited cognitive recovery. | (mulik2023creatinedeficiencydisorders pages 2-3, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8, battini2017fifteenyearfollowupof pages 1-2, battini2017fifteenyearfollowupof pages 4-7) | Mulik 2023: https://doi.org/10.5152/turkarchpediatr.2023.23022; Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; Battini 2017: https://doi.org/10.1186/s13023-017-0577-5 |
| Monitoring/adverse effects | Monitoring strategies include serial plasma/urine creatine and GAA, neuropsychological assessment, and repeat brain MRS. Reported adverse effects are generally mild but include weight gain, polyuria/polydipsia, transient diarrhea with dose increases, urinary creatine crystals, and occasional kidney stones; renal function was generally preserved in long-term follow-up. | (battini2017fifteenyearfollowupof pages 1-2, battini2017fifteenyearfollowupof pages 4-7, battini2017fifteenyearfollowupof pages 7-8) | Battini 2017: https://doi.org/10.1186/s13023-017-0577-5 |
| Epidemiology/screening implementation | AGAT deficiency is an extreme ultrarare disorder; ClinGen used an estimated prevalence of ~1 in 3,450,000 for GATM-related disease in variant-classification threshold setting. Newborn screening is considered attractive because early treatment can prevent disease, but AGAT is harder to detect than GAMT using GAA alone; proposed approaches include multianalyte dried-blood-spot algorithms or enzyme assays. Early Check (NCT03655223) explicitly includes AGAT deficiency in an expanded newborn screening program, while BioCDS (NCT02934854) aimed to develop DBS mass-spectrometry biomarkers but was withdrawn with enrollment 0. | (goldstein2024clingenvariantcuration pages 4-6, stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8, NCT03655223 chunk 2, NCT02934854 chunk 1) | Goldstein 2024: https://doi.org/10.1016/j.ymgme.2024.108362; Stockler-Ipsiroglu 2015: https://doi.org/10.1016/j.ymgme.2015.10.003; NCT03655223: https://clinicaltrials.gov/study/NCT03655223 (2018-ongoing); NCT02934854: https://clinicaltrials.gov/study/NCT02934854 (2018, withdrawn) |


*Table: This table condenses the most actionable disease-level facts for GATM-related AGAT deficiency, including identifiers, biochemical hallmarks, clinical presentation, diagnostics, and treatment evidence with dosing ranges. It is useful as a quick-reference artifact for a disease knowledge base entry.*

---

## Clinical trials / real-world studies relevant to AGAT deficiency

1. **Early Check: Expanded Screening in Newborns** (ClinicalTrials.gov **NCT03655223**, posted 2018; observational; estimated enrollment 30,000)
- Explicitly lists **Agat Deficiency** on its screening panel and provides confirmatory testing and genetic counseling workflow. URL: https://clinicaltrials.gov/study/NCT03655223 (NCT03655223 chunk 2)

2. **Biomarker for Creatine Deficiency Syndromes (BioCDS)** (ClinicalTrials.gov **NCT02934854**, posted 2018; observational; **withdrawn**, enrollment 0)
- Proposed DBS LC/MRM-MS biomarker discovery/validation with **GATM** sequencing; withdrawn due to “Transition into BioMetabol.” URL: https://clinicaltrials.gov/study/NCT02934854 (NCT02934854 chunk 1)

---

## Important limitations of this report (data not retrieved in-tool)
- Orphanet/MeSH/ICD codes were not retrieved via the available full texts and would require targeted database queries.
- Variant-level allele frequencies in gnomAD and comprehensive ClinVar variant lists are not included beyond the ClinGen thresholds and exemplar variants available in the retrieved excerpts.
- Many phenotype frequencies beyond IDD (15/16) and myopathy (8/16) were not extractable from the provided excerpts and would require full-table extraction from primary cohorts.


References

1. (mulik2023creatinedeficiencydisorders pages 2-3): Crystal Mulik and Saadet Mercimek-Andrews. Creatine deficiency disorders: phenotypes, genotypes, diagnosis, and treatment outcomes. Turkish Archives of Pediatrics, 58:129-135, Mar 2023. URL: https://doi.org/10.5152/turkarchpediatr.2023.23022, doi:10.5152/turkarchpediatr.2023.23022. This article has 13 citations.

2. (longo2011disordersofcreatine pages 2-3): Nicola Longo, Orly Ardon, Rena Vanzo, Elizabeth Schwartz, and Marzia Pasquali. Disorders of creatine transport and metabolism. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 157:72-78, Feb 2011. URL: https://doi.org/10.1002/ajmg.c.30292, doi:10.1002/ajmg.c.30292. This article has 135 citations.

3. (goldstein2024clingenvariantcuration pages 3-4): Jennifer Goldstein, Amanda Thomas-Wilson, Emily Groopman, Vimla Aggarwal, Simona Bianconi, Raquel Fernandez, Kim Hart, Nicola Longo, Nicole Liang, Daniel Reich, Heidi Wallis, Meredith Weaver, Sarah Young, and Saadet Mercimek-Andrews. Clingen variant curation expert panel recommendations for classification of variants in gamt, gatm and slc6a8 for cerebral creatine deficiency syndromes. Molecular Genetics and Metabolism, 142:108362, May 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108362, doi:10.1016/j.ymgme.2024.108362. This article has 12 citations and is from a peer-reviewed journal.

4. (kaufman2025diagnosticdelayin pages 1-2): Christina Kaufman, Anaïs D’Andrea, Annette Hackenberg, Martin Poms, Olivier Braissant, and Johannes Häberle. Diagnostic delay in cerebral creatine deficiency disorders: lessons learned from a cross-sectional single center study, and guanidinoacetate and creatine measurements in switzerland between 2015 and 2023. Molecular and Cellular Pediatrics, Jan 2025. URL: https://doi.org/10.1186/s40348-024-00188-4, doi:10.1186/s40348-024-00188-4. This article has 2 citations.

5. (garg2024magneticresonancespectroscopy pages 2-4): Ankita Garg, Rajiv Gupta, Jayesh Ashok Kumar Modi, and Debolina Kabiraj. Magnetic resonance spectroscopy as a diagnostic tool in cerebral creatine deficiency syndrome 3. Case Reports in Clinical Radiology, 0:1-5, Dec 2024. URL: https://doi.org/10.25259/crcr\_92\_2024, doi:10.25259/crcr\_92\_2024. This article has 0 citations.

6. (edvardson2010larginineglycineamidinotransferase(agat) pages 1-2): Simon Edvardson, Stanley H. Korman, Amir Livne, Avraham Shaag, Ann Saada, Ruppen Nalbandian, Hyla Allouche-Arnon, J. Moshe Gomori, and Rachel Katz-Brull. L-arginine:glycine amidinotransferase (agat) deficiency: clinical presentation and response to treatment in two patients with a novel mutation. Molecular Genetics and Metabolism, 101:228-232, Oct 2010. URL: https://doi.org/10.1016/j.ymgme.2010.06.021, doi:10.1016/j.ymgme.2010.06.021. This article has 72 citations and is from a peer-reviewed journal.

7. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 1-2): Sylvia Stockler-Ipsiroglu, Delia Apatean, Roberta Battini, Suzanne DeBrosse, Kimberley Dessoffy, Simon Edvardson, Florian Eichler, Katherine Johnston, David M. Koeller, Sonia Nouioua, Meriem Tazir, Ashok Verma, Monica D. Dowling, Klaas J. Wierenga, Andrea M. Wierenga, Victor Zhang, and Lee-Jun C. Wong. Arginine:glycine amidinotransferase (agat) deficiency: clinical features and long term outcomes in 16 patients diagnosed worldwide. Molecular Genetics and Metabolism, 116:252-259, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.003, doi:10.1016/j.ymgme.2015.10.003. This article has 82 citations and is from a peer-reviewed journal.

8. (ndika2012developmentalprogressand pages 1-2): Joseph D.T. Ndika, Kathreen Johnston, James A. Barkovich, Michael D. Wirt, Patricia O'Neill, Ofir T. Betsalel, Cornelis Jakobs, and Gajja S. Salomons. Developmental progress and creatine restoration upon long-term creatine supplementation of a patient with arginine:glycine amidinotransferase deficiency. Molecular Genetics and Metabolism, 106:48-54, May 2012. URL: https://doi.org/10.1016/j.ymgme.2012.01.017, doi:10.1016/j.ymgme.2012.01.017. This article has 48 citations and is from a peer-reviewed journal.

9. (verma2010arginineglycineamidinotransferasedeficiency pages 1-3): Ashok Verma. Arginine:glycine amidinotransferase deficiency: a treatable metabolic encephalomyopathy. Neurology, 75:186-188, Jul 2010. URL: https://doi.org/10.1212/wnl.0b013e3181e7cabd, doi:10.1212/wnl.0b013e3181e7cabd. This article has 24 citations and is from a highest quality peer-reviewed journal.

10. (pintilie2021ararebut pages 4-5): Sebastian Romeo Pintilie, Adriana Fodor, Marius Bembea, Codruța Diana Petchesi, Simona Grad, Laura Damian, and Romana Vulturar. A rare but treatable inborn error of metabolism: arginine glycine amidinotransferase (agat) deficiency. Romanian Journal of Pediatrics, 70:186-191, Sep 2021. URL: https://doi.org/10.37897/rjp.2021.3.4, doi:10.37897/rjp.2021.3.4. This article has 0 citations.

11. (ndika2012developmentalprogressand pages 5-6): Joseph D.T. Ndika, Kathreen Johnston, James A. Barkovich, Michael D. Wirt, Patricia O'Neill, Ofir T. Betsalel, Cornelis Jakobs, and Gajja S. Salomons. Developmental progress and creatine restoration upon long-term creatine supplementation of a patient with arginine:glycine amidinotransferase deficiency. Molecular Genetics and Metabolism, 106:48-54, May 2012. URL: https://doi.org/10.1016/j.ymgme.2012.01.017, doi:10.1016/j.ymgme.2012.01.017. This article has 48 citations and is from a peer-reviewed journal.

12. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 2-3): Sylvia Stockler-Ipsiroglu, Delia Apatean, Roberta Battini, Suzanne DeBrosse, Kimberley Dessoffy, Simon Edvardson, Florian Eichler, Katherine Johnston, David M. Koeller, Sonia Nouioua, Meriem Tazir, Ashok Verma, Monica D. Dowling, Klaas J. Wierenga, Andrea M. Wierenga, Victor Zhang, and Lee-Jun C. Wong. Arginine:glycine amidinotransferase (agat) deficiency: clinical features and long term outcomes in 16 patients diagnosed worldwide. Molecular Genetics and Metabolism, 116:252-259, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.003, doi:10.1016/j.ymgme.2015.10.003. This article has 82 citations and is from a peer-reviewed journal.

13. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 5-7): Sylvia Stockler-Ipsiroglu, Delia Apatean, Roberta Battini, Suzanne DeBrosse, Kimberley Dessoffy, Simon Edvardson, Florian Eichler, Katherine Johnston, David M. Koeller, Sonia Nouioua, Meriem Tazir, Ashok Verma, Monica D. Dowling, Klaas J. Wierenga, Andrea M. Wierenga, Victor Zhang, and Lee-Jun C. Wong. Arginine:glycine amidinotransferase (agat) deficiency: clinical features and long term outcomes in 16 patients diagnosed worldwide. Molecular Genetics and Metabolism, 116:252-259, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.003, doi:10.1016/j.ymgme.2015.10.003. This article has 82 citations and is from a peer-reviewed journal.

14. (battini2017fifteenyearfollowupof pages 2-4): Roberta Battini, M. Grazia Alessandrì, Claudia Casalini, Manuela Casarano, Michela Tosetti, and Giovanni Cioni. Fifteen-year follow-up of italian families affected by arginine glycine amidinotransferase deficiency. Orphanet Journal of Rare Diseases, Feb 2017. URL: https://doi.org/10.1186/s13023-017-0577-5, doi:10.1186/s13023-017-0577-5. This article has 22 citations and is from a peer-reviewed journal.

15. (goldstein2024clingenvariantcuration pages 8-9): Jennifer Goldstein, Amanda Thomas-Wilson, Emily Groopman, Vimla Aggarwal, Simona Bianconi, Raquel Fernandez, Kim Hart, Nicola Longo, Nicole Liang, Daniel Reich, Heidi Wallis, Meredith Weaver, Sarah Young, and Saadet Mercimek-Andrews. Clingen variant curation expert panel recommendations for classification of variants in gamt, gatm and slc6a8 for cerebral creatine deficiency syndromes. Molecular Genetics and Metabolism, 142:108362, May 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108362, doi:10.1016/j.ymgme.2024.108362. This article has 12 citations and is from a peer-reviewed journal.

16. (goldstein2024clingenvariantcuration pages 13-18): Jennifer Goldstein, Amanda Thomas-Wilson, Emily Groopman, Vimla Aggarwal, Simona Bianconi, Raquel Fernandez, Kim Hart, Nicola Longo, Nicole Liang, Daniel Reich, Heidi Wallis, Meredith Weaver, Sarah Young, and Saadet Mercimek-Andrews. Clingen variant curation expert panel recommendations for classification of variants in gamt, gatm and slc6a8 for cerebral creatine deficiency syndromes. Molecular Genetics and Metabolism, 142:108362, May 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108362, doi:10.1016/j.ymgme.2024.108362. This article has 12 citations and is from a peer-reviewed journal.

17. (goldstein2024clingenvariantcuration pages 4-6): Jennifer Goldstein, Amanda Thomas-Wilson, Emily Groopman, Vimla Aggarwal, Simona Bianconi, Raquel Fernandez, Kim Hart, Nicola Longo, Nicole Liang, Daniel Reich, Heidi Wallis, Meredith Weaver, Sarah Young, and Saadet Mercimek-Andrews. Clingen variant curation expert panel recommendations for classification of variants in gamt, gatm and slc6a8 for cerebral creatine deficiency syndromes. Molecular Genetics and Metabolism, 142:108362, May 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108362, doi:10.1016/j.ymgme.2024.108362. This article has 12 citations and is from a peer-reviewed journal.

18. (battini2017fifteenyearfollowupof pages 7-8): Roberta Battini, M. Grazia Alessandrì, Claudia Casalini, Manuela Casarano, Michela Tosetti, and Giovanni Cioni. Fifteen-year follow-up of italian families affected by arginine glycine amidinotransferase deficiency. Orphanet Journal of Rare Diseases, Feb 2017. URL: https://doi.org/10.1186/s13023-017-0577-5, doi:10.1186/s13023-017-0577-5. This article has 22 citations and is from a peer-reviewed journal.

19. (battini2017fifteenyearfollowupof pages 4-7): Roberta Battini, M. Grazia Alessandrì, Claudia Casalini, Manuela Casarano, Michela Tosetti, and Giovanni Cioni. Fifteen-year follow-up of italian families affected by arginine glycine amidinotransferase deficiency. Orphanet Journal of Rare Diseases, Feb 2017. URL: https://doi.org/10.1186/s13023-017-0577-5, doi:10.1186/s13023-017-0577-5. This article has 22 citations and is from a peer-reviewed journal.

20. (goldstein2024clingenvariantcuration pages 1-3): Jennifer Goldstein, Amanda Thomas-Wilson, Emily Groopman, Vimla Aggarwal, Simona Bianconi, Raquel Fernandez, Kim Hart, Nicola Longo, Nicole Liang, Daniel Reich, Heidi Wallis, Meredith Weaver, Sarah Young, and Saadet Mercimek-Andrews. Clingen variant curation expert panel recommendations for classification of variants in gamt, gatm and slc6a8 for cerebral creatine deficiency syndromes. Molecular Genetics and Metabolism, 142:108362, May 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108362, doi:10.1016/j.ymgme.2024.108362. This article has 12 citations and is from a peer-reviewed journal.

21. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 7-8): Sylvia Stockler-Ipsiroglu, Delia Apatean, Roberta Battini, Suzanne DeBrosse, Kimberley Dessoffy, Simon Edvardson, Florian Eichler, Katherine Johnston, David M. Koeller, Sonia Nouioua, Meriem Tazir, Ashok Verma, Monica D. Dowling, Klaas J. Wierenga, Andrea M. Wierenga, Victor Zhang, and Lee-Jun C. Wong. Arginine:glycine amidinotransferase (agat) deficiency: clinical features and long term outcomes in 16 patients diagnosed worldwide. Molecular Genetics and Metabolism, 116:252-259, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.003, doi:10.1016/j.ymgme.2015.10.003. This article has 82 citations and is from a peer-reviewed journal.

22. (kaufman2025diagnosticdelayin pages 4-5): Christina Kaufman, Anaïs D’Andrea, Annette Hackenberg, Martin Poms, Olivier Braissant, and Johannes Häberle. Diagnostic delay in cerebral creatine deficiency disorders: lessons learned from a cross-sectional single center study, and guanidinoacetate and creatine measurements in switzerland between 2015 and 2023. Molecular and Cellular Pediatrics, Jan 2025. URL: https://doi.org/10.1186/s40348-024-00188-4, doi:10.1186/s40348-024-00188-4. This article has 2 citations.

23. (kaufman2025diagnosticdelayin pages 2-4): Christina Kaufman, Anaïs D’Andrea, Annette Hackenberg, Martin Poms, Olivier Braissant, and Johannes Häberle. Diagnostic delay in cerebral creatine deficiency disorders: lessons learned from a cross-sectional single center study, and guanidinoacetate and creatine measurements in switzerland between 2015 and 2023. Molecular and Cellular Pediatrics, Jan 2025. URL: https://doi.org/10.1186/s40348-024-00188-4, doi:10.1186/s40348-024-00188-4. This article has 2 citations.

24. (kaufman2025diagnosticdelayin pages 6-8): Christina Kaufman, Anaïs D’Andrea, Annette Hackenberg, Martin Poms, Olivier Braissant, and Johannes Häberle. Diagnostic delay in cerebral creatine deficiency disorders: lessons learned from a cross-sectional single center study, and guanidinoacetate and creatine measurements in switzerland between 2015 and 2023. Molecular and Cellular Pediatrics, Jan 2025. URL: https://doi.org/10.1186/s40348-024-00188-4, doi:10.1186/s40348-024-00188-4. This article has 2 citations.

25. (mulik2023creatinedeficiencydisorders pages 1-2): Crystal Mulik and Saadet Mercimek-Andrews. Creatine deficiency disorders: phenotypes, genotypes, diagnosis, and treatment outcomes. Turkish Archives of Pediatrics, 58:129-135, Mar 2023. URL: https://doi.org/10.5152/turkarchpediatr.2023.23022, doi:10.5152/turkarchpediatr.2023.23022. This article has 13 citations.

26. (battini2017fifteenyearfollowupof pages 1-2): Roberta Battini, M. Grazia Alessandrì, Claudia Casalini, Manuela Casarano, Michela Tosetti, and Giovanni Cioni. Fifteen-year follow-up of italian families affected by arginine glycine amidinotransferase deficiency. Orphanet Journal of Rare Diseases, Feb 2017. URL: https://doi.org/10.1186/s13023-017-0577-5, doi:10.1186/s13023-017-0577-5. This article has 22 citations and is from a peer-reviewed journal.

27. (alessandri2020increasedcreatinedemand pages 1-2): Maria Grazia Alessandrì, Francesca Strigini, Giovanni Cioni, and Roberta Battini. Increased creatine demand during pregnancy in arginine: glycine amidino-transferase deficiency: a case report. BMC Pregnancy and Childbirth, Sep 2020. URL: https://doi.org/10.1186/s12884-020-03192-4, doi:10.1186/s12884-020-03192-4. This article has 15 citations and is from a peer-reviewed journal.

28. (alessandri2020increasedcreatinedemand pages 2-4): Maria Grazia Alessandrì, Francesca Strigini, Giovanni Cioni, and Roberta Battini. Increased creatine demand during pregnancy in arginine: glycine amidino-transferase deficiency: a case report. BMC Pregnancy and Childbirth, Sep 2020. URL: https://doi.org/10.1186/s12884-020-03192-4, doi:10.1186/s12884-020-03192-4. This article has 15 citations and is from a peer-reviewed journal.

29. (NCT03655223 chunk 2):  Early Check: Expanded Screening in Newborns. RTI International. 2018. ClinicalTrials.gov Identifier: NCT03655223

30. (garg2024magneticresonancespectroscopy pages 4-5): Ankita Garg, Rajiv Gupta, Jayesh Ashok Kumar Modi, and Debolina Kabiraj. Magnetic resonance spectroscopy as a diagnostic tool in cerebral creatine deficiency syndrome 3. Case Reports in Clinical Radiology, 0:1-5, Dec 2024. URL: https://doi.org/10.25259/crcr\_92\_2024, doi:10.25259/crcr\_92\_2024. This article has 0 citations.

31. (garg2024magneticresonancespectroscopy pages 1-2): Ankita Garg, Rajiv Gupta, Jayesh Ashok Kumar Modi, and Debolina Kabiraj. Magnetic resonance spectroscopy as a diagnostic tool in cerebral creatine deficiency syndrome 3. Case Reports in Clinical Radiology, 0:1-5, Dec 2024. URL: https://doi.org/10.25259/crcr\_92\_2024, doi:10.25259/crcr\_92\_2024. This article has 0 citations.

32. (stockleripsiroglu2015arginineglycineamidinotransferase(agat) pages 3-4): Sylvia Stockler-Ipsiroglu, Delia Apatean, Roberta Battini, Suzanne DeBrosse, Kimberley Dessoffy, Simon Edvardson, Florian Eichler, Katherine Johnston, David M. Koeller, Sonia Nouioua, Meriem Tazir, Ashok Verma, Monica D. Dowling, Klaas J. Wierenga, Andrea M. Wierenga, Victor Zhang, and Lee-Jun C. Wong. Arginine:glycine amidinotransferase (agat) deficiency: clinical features and long term outcomes in 16 patients diagnosed worldwide. Molecular Genetics and Metabolism, 116:252-259, Dec 2015. URL: https://doi.org/10.1016/j.ymgme.2015.10.003, doi:10.1016/j.ymgme.2015.10.003. This article has 82 citations and is from a peer-reviewed journal.

33. (NCT02934854 chunk 1):  Biomarker for Creatine Deficiency Syndromes (BioCDS). CENTOGENE GmbH Rostock. 2018. ClinicalTrials.gov Identifier: NCT02934854
