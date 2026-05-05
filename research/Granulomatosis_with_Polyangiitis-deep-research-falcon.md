---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-01T07:16:52.599215'
end_time: '2026-05-01T07:35:04.395563'
duration_seconds: 1091.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Granulomatosis with Polyangiitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Granulomatosis with Polyangiitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Granulomatosis with Polyangiitis** covering all of the
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
- **Disease Name:** Granulomatosis with Polyangiitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Granulomatosis with Polyangiitis** covering all of the
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


## Comprehensive Disease Characteristics Report: Granulomatosis with Polyangiitis (GPA)

### Target disease
Granulomatosis with polyangiitis (GPA) is a rare systemic disease characterized by granulomatous inflammation of the respiratory tract and necrotizing vasculitis of small-to-medium vessels, most often associated with anti‑neutrophil cytoplasmic antibodies (ANCA) targeting proteinase‑3 (PR3). Classic organ involvement includes upper airways (ENT), lungs, and kidneys (“ELK”), although essentially any organ system can be affected. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

**Important evidence limitation (PMIDs):** The full texts retrieved in this run (Frontiers in Medicine review; ACR/EULAR criteria paper excerpts; cohort studies; ClinicalTrials.gov records; genetics reviews/GWAS excerpts) did not reliably expose PubMed IDs in the available text chunks. Therefore, PMID-level citations and direct abstract quotes cannot be provided from the tool outputs; instead, this report cites the retrieved sources by DOI/URL and the internal evidence IDs shown in parentheses.

---

## 1. Disease information

### 1.1 Concise overview
GPA is a systemic ANCA-associated vasculitis (AAV) with necrotizing vasculitis and granulomatous inflammation, typically involving ENT tract, lungs, and kidneys. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

### 1.2 Synonyms / alternative names
* Granulomatosis with polyangiitis
* Wegener’s granulomatosis (historical eponym referenced in genetics/GWAS literature) (xie2013associationofgranulomatosis pages 1-2)

### 1.3 Key identifiers (ontology and coding systems)
The current evidence set did **not** include machine-readable entries from OMIM, Orphanet, MeSH, ICD‑10/ICD‑11, or MONDO. Accordingly, the following fields cannot be populated from tool-grounded evidence in this run:
* **MONDO ID:** not retrieved
* **OMIM / Orphanet / MeSH / ICD‑10/ICD‑11:** not retrieved

### 1.4 Evidence sources (individual vs aggregated)
This report is derived from aggregated disease-level resources (reviews, consensus/criteria papers, cohort studies, systematic reviews) and trial registry entries rather than EHR-derived individual case series (except where retrospective cohorts use administrative claims). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2, kramer2024remissioninductiontherapies pages 1-2, NCT07176546 chunk 1)

---

## 2. Etiology

### 2.1 Primary causal factors (current understanding)
GPA is generally considered **multifactorial**, with strong immunogenetic risk and autoimmunity centered on PR3‑ANCA in many patients. The disease is strongly associated with PR3‑ANCA by serology (see Diagnostics) and with genetic loci tied to antigen presentation (HLA class II) and the PR3/alpha‑1 antitrypsin axis. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6, alberici2015geneticaspectsof pages 4-4)

### 2.2 Genetic risk factors (susceptibility loci)
Evidence from GWAS and genetic summaries supports a **polygenic architecture** with a prominent HLA class II signal:

* **HLA-DP region (HLA‑DPB1/HLA‑DPA1):** A 2013 GWAS of GPA reported genome‑wide significant association at HLA‑DP (e.g., rs9277554 combined P=1.92×10−50; rs9277341 P=2.18×10−39), and the association was reported as fully accounted for by **HLA‑DPB1*04**. (Xie et al., 2013; https://doi.org/10.1002/art.38036) (xie2013associationofgranulomatosis pages 1-2)
* **SEMA6A:** The same GWAS reported an independent non‑MHC locus near **SEMA6A** (rs26595) with combined P=2.09×10−8. (xie2013associationofgranulomatosis pages 1-2)
* **SERPINA1 and PRTN3:** A 2015 genetics review summarizing GWAS signals reported associations for **SERPINA1** (e.g., rs7151526; PR3+ subgroup OR 0.53, P=5.6×10−12) and **PRTN3** (rs62132295; PR3+ subgroup OR 0.73, P=2.6×10−7). (https://doi.org/10.1093/ndt/gfu386) (alberici2015geneticaspectsof pages 4-4)
* **Replication/functional framing:** A 2017 large genetic study (AAV cases and controls) reported strong HLA‑DPB1 effects (e.g., rs141530235 OR 2.99; rs1042169 OR 2.82) and described associations at **SERPINA1**, **PTPN22**, and a **PRTN3** locus correlated with increased PRTN3 expression in neutrophils. (https://doi.org/10.1002/art.40034) (merkel2017identificationoffunctional pages 1-4)

**Protective variants / penetrance / inheritance:** No evidence in the retrieved set quantified penetrance, carrier frequency, or protective alleles specifically for GPA; the genetic evidence supports complex/polygenic susceptibility rather than Mendelian inheritance. (merkel2017identificationoffunctional pages 1-4, alberici2015geneticaspectsof pages 4-4)

### 2.3 Environmental and infectious risk factors; gene–environment interactions
No tool-retrieved sources in this run provided specific environmental (e.g., silica), lifestyle (e.g., smoking), or infectious triggers for GPA, nor explicit gene–environment interaction analyses. This remains an evidence gap for this report.

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Major phenotype spectrum with frequencies (examples)
The phenotype of GPA is heterogeneous, but a recurring pattern is ENT + pulmonary + renal involvement.

**ENT manifestations**
* ENT involvement/signs are common (reported 80–100%). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)
* Examples of reported ENT symptom frequencies: nasal crusting 75%, excessive nose‑blowing 70%, nasal obstruction 65%, epistaxis 59%; saddle‑nose deformity is described and one source reports saddle nose in 25%. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)

**Pulmonary manifestations**
* Pulmonary involvement is frequently reported (e.g., 62–90%). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3)
* Pulmonary nodules/mass lesions: 40–70%; cavitation: 20–50%. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3)
* Diffuse alveolar hemorrhage (DAH): 8.8–36% in GPA. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)

**Renal manifestations**
* Renal involvement: 70–85% during the course of disease; renal insufficiency at presentation: 11–17%; worsening GFR reported in 24.3%. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

**Ophthalmologic/orbital and oral manifestations**
* Ophthalmologic signs: 50–60%; orbital lesions: 5–30%. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)
* A systematic review reports ocular/orbital involvement in 16–78%, and up to 27% of patients presenting initially with ophthalmic symptoms. (moin2023ocularandorbital pages 1-2)
* Oral involvement: 6–13%; “strawberry” gingival hyperplasia reported in 61.5% (in a cited subgroup context). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

**Neurologic manifestations**
* Peripheral nervous system involvement: 11–44%; CNS involvement: 3–11.7% (often hypertrophic pachymeningitis). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)

### 3.2 Onset and course
GPA can have substantial diagnostic delay: time from first symptoms to diagnosis ranged from 1 month to >3 years, and 36% of patients had symptoms for >1 year before diagnosis in one synthesis. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

### 3.3 Quality of life impact (PROs)
Quantitative QoL effect sizes were not extractable from the retrieved text chunks. However, the following instruments are explicitly used as outcome measures in contemporary GPA/AAV trials focusing on steroid‑sparing approaches:
* **SF‑36** and **EQ‑5D‑5L** were used in the 2024 ADVOCATE rituximab‑subgroup analysis of avacopan. (geetha2024efficacyandsafety pages 4-5)
* **SNOT‑22** and **AAV‑PRO** are key secondary endpoints in an avacopan trial focused on ENT disease activity in GPA (NCT07176546). (NCT07176546 chunk 1)

### 3.4 Suggested HPO terms (non-exhaustive; to be curated)
Based on phenotypes explicitly described in the evidence set:
* ENT: nasal crusting; epistaxis; chronic sinusitis; nasal septum perforation; saddle nose deformity. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)
* Pulmonary: pulmonary nodules; cavitary lung lesions; diffuse alveolar hemorrhage; hemoptysis. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)
* Renal: rapidly progressive glomerulonephritis; hematuria; proteinuria; decreased glomerular filtration rate. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6, draibe2024diagnosisandtreatment pages 2-3)
* Ocular: scleritis; episcleritis; uveitis; proptosis; orbital mass. (moin2023ocularandorbital pages 1-2, draibe2024diagnosisandtreatment pages 2-3)
* Neurologic: mononeuritis multiplex; cranial neuropathy; hypertrophic pachymeningitis/headache. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)

---

## 4. Genetic / molecular information

### 4.1 “Causal genes” vs susceptibility genes
GPA is not established as a monogenic disorder in the retrieved evidence; instead, **susceptibility loci** (HLA-DP, SERPINA1, PRTN3, SEMA6A, PTPN22) are repeatedly supported by GWAS and genetic syntheses. (merkel2017identificationoffunctional pages 1-4, alberici2015geneticaspectsof pages 4-4, xie2013associationofgranulomatosis pages 1-2)

### 4.2 ANCA serotypes and molecular targets
PR3‑ANCA is the dominant serotype in GPA, with MPO‑ANCA more characteristic of MPA (and certain pulmonary phenotypes such as ILD). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

### 4.3 Mechanistic chain (current evidence-supported skeleton)
1. Genetic predisposition (notably HLA class II DP) supports altered antigen presentation and adaptive immune recognition. (xie2013associationofgranulomatosis pages 1-2, merkel2017identificationoffunctional pages 1-4)
2. Autoimmune effector phase characterized by PR3‑ANCA in many patients; ANCA positivity helps define phenotypes and informs classification/diagnosis. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)
3. Inflammatory vascular injury and granulomatous inflammation lead to organ manifestations in ENT tract, lungs (nodules/cavitation/DAH), and kidneys (pauci‑immune GN). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)
4. Complement pathway targeting has become clinically actionable: avacopan antagonizes **C5a receptor 1 (C5AR1)** and demonstrates glucocorticoid‑sparing efficacy in AAV (including GPA). (geetha2024efficacyandsafety pages 1-2, geetha2024efficacyandsafety pages 4-5)

### 4.4 Suggested GO (biological process) and CL (cell type) terms (evidence-aligned; to be curated)
While the retrieved sources did not provide omics-level pathway enumerations, the disease and therapies point to:
* GO BP (suggestions): neutrophil activation; complement activation; adaptive immune response; antigen processing and presentation; inflammatory response; vasculature development/vasculitis-related processes. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6, geetha2024efficacyandsafety pages 1-2)
* CL (suggestions): neutrophil; macrophage; T cell; B cell; endothelial cell. (merkel2017identificationoffunctional pages 1-4)

### 4.5 Epigenetics and multi-omics
No GPA-specific epigenomic/transcriptomic/proteomic/metabolomic results were retrieved in this run; this is an evidence gap.

---

## 5. Environmental information
No GPA-specific environmental, lifestyle, pollutant, occupational, or infectious triggers were retrieved from the current evidence set.

---

## 6. Mechanism / pathophysiology (expanded notes from retrieved evidence)

### 6.1 Serology-based phenotyping and diagnostic performance
ANCA specificity is clinically informative. Antigen-specific PR3/MPO assays are recommended over indirect immunofluorescence in the reviewed diagnostic updates. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

### 6.2 Complement pathway as an actionable mechanism
Avacopan (TAVNEOS), a C5a receptor antagonist, is being deployed to reduce glucocorticoid exposure while maintaining disease control in AAV. ADVOCATE subgroup analyses demonstrate sustained remission and reduced steroid toxicity signals (see Treatment). (geetha2024efficacyandsafety pages 1-2, geetha2024efficacyandsafety pages 4-5)

---

## 7. Anatomical structures affected

### 7.1 Organ-level and system-level involvement (with suggested UBERON mapping targets)
* Upper airway / ENT (nasal passages, paranasal sinuses, ear structures) (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)
* Lungs (pulmonary parenchyma; alveolar capillaries in DAH; airway structures in tracheobronchial disease) (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)
* Kidneys (glomeruli—pauci‑immune GN; renal cortex) (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6, draibe2024diagnosisandtreatment pages 2-3)
* Eyes and orbit (scleritis/uveitis/orbital mass) (moin2023ocularandorbital pages 1-2, draibe2024diagnosisandtreatment pages 2-3)
* Peripheral and central nervous system (mononeuritis multiplex; pachymeningitis) (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5)

### 7.2 Tissue/cell-level and subcellular-level
The retrieved evidence supports immune and vascular pathology but did not supply histologic microanatomy beyond “granuloma/giant cells on biopsy” and “pauci‑immune glomerulonephritis.” (pyo2023comparisonofthe pages 2-4)

---

## 8. Temporal development

### 8.1 Onset patterns
The evidence set indicates substantial variation and frequent delay in diagnosis, with reported symptom-to-diagnosis intervals from 1 month to >3 years and 36% of patients symptomatic for >1 year pre-diagnosis. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

### 8.2 Disease course
GPA is framed as chronic with relapsing-remitting features requiring close follow-up. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recently summarized)
* AAV prevalence estimate: 200–400 per million (200–400/1,000,000). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)
* GPA annual incidence in European adults: ~7.7–15.4 per million; one Swedish study reported 15.4/million. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)
* Pediatric GPA incidence: ~0.88–1.8 per million. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

### 9.2 Population demographics
* Peak age at diagnosis varies by cohort; one summary mentions peaks at 45–55 and 65–74 years. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)

### 9.3 Inheritance model
The available evidence supports complex polygenic risk rather than Mendelian inheritance. (merkel2017identificationoffunctional pages 1-4, alberici2015geneticaspectsof pages 4-4)

---

## 10. Diagnostics

### 10.1 Current diagnostic approach
A key practical constraint is that **validated diagnostic criteria for GPA are not established**; diagnosis is based on a synthesis of clinical features plus supportive laboratory testing (ANCA), imaging, and histology, acknowledging that biopsy may be infeasible and/or non‑specific. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

### 10.2 ANCA testing (quantitative performance)
From the 2024 diagnostic update:
* PR3‑ANCA sensitivity for GPA: 74% (MPO‑ANCA sensitivity for GPA: 11%). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)
* Specificity (PR3/MPO antigen-specific assays): mean 97% (range 93–99%). (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)
* ANCA‑seronegative proportion reported as ~8.5%. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6)

### 10.3 Classification criteria update (2022 ACR/EULAR)
The 2022 ACR/EULAR GPA criteria are a **points-based classification tool** intended for research classification, not as a stand‑alone diagnostic algorithm, and require appropriate entry criteria and exclusion of mimics. (https://doi.org/10.1002/art.41986) (robson20222022americancollege pages 5-6)

Items and weights available from a 2023 summary of the criteria include:
* nasal passage involvement (+3)
* cartilaginous involvement (+2)
* conductive/sensorineural hearing loss (+1)
* PR3‑ANCA/c‑ANCA positivity (+5)
* MPO‑ANCA/p‑ANCA positivity (−1)
* eosinophils ≥1000/µL (−4)
* granuloma/granulomatous inflammation/giant cells on biopsy (+2)
* pauci‑immune glomerulonephritis (+1)
* two radiology items were retained with positive weights in the summary, but the excerpt did not include the precise radiology item wording. (pyo2023comparisonofthe pages 2-4)

Threshold: classification if cumulative score ≥5 (one summary reported “>5”). (pyo2023comparisonofthe pages 2-4, robson20222022americancollege pages 5-6)

Performance: the criteria were reported (in the retrieved summary text) to have sensitivity 93% and specificity 94% in a validation set. (robson20222022americancollege pages 5-6)

**Visual evidence note:** A retrieved figure crop from the criteria document shows the *MPA* scoring table (not the GPA table) but visually confirms the ACR/EULAR points-based approach and how PR3‑ANCA/nasal involvement are used as discriminators across AAV subtypes. (robson20222022americancollege media d7729245)

### 10.4 Biopsy and imaging
Biopsy is “strongly recommended” but is not always feasible and may show non-specific features; imaging supports detection of pulmonary nodules/masses/cavitation and sinonasal inflammation. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3)

---

## 11. Outcomes / prognosis

### 11.1 Relapse and long-term outcomes (recent cohort data)
A 2024 multicenter European cohort (1999–2022; classified by 2022 criteria) reported:
* Overall relapse rate: 34.6% (124/358). (kramer2024remissioninductiontherapies pages 4-5)
* Relapse rate was higher in GPA than MPA: 41.3% vs 25.9% (p=0.006). (kramer2024remissioninductiontherapies pages 4-5)
* Composite renal endpoint occurred in 25.4% and was more frequent in MPA than GPA (31.7% vs 21.2%, p=0.028). (kramer2024remissioninductiontherapies pages 4-5)

### 11.2 Kidney outcome markers in steroid-sparing complement inhibition
In the ADVOCATE rituximab subgroup analysis, urinary albumin-to-creatinine ratio (UACR) improved more with avacopan (LS mean ~−42%) versus prednisone taper (~+6%). (geetha2024efficacyandsafety pages 4-5)

**Survival and disease-specific mortality:** Not retrievable from current evidence set.

---

## 12. Treatment

### 12.1 Contemporary standard approaches (supported by evidence in this run)
Modern GPA care generally integrates:
* Immunosuppression/biologics for induction and maintenance (e.g., rituximab; cyclophosphamide in some settings)
* Glucocorticoid-sparing strategies
* Infection prophylaxis during intensive immunosuppression (e.g., PJP prophylaxis)

The detailed regimen algorithms (dose schedules by phenotype/severity) were not fully extractable from the retrieved guideline texts in this run; however, multiple high-quality 2024 sources document evolving steroid-sparing approaches and real-world practice trends. (geetha2024efficacyandsafety pages 4-5, kramer2024remissioninductiontherapies pages 1-2)

### 12.2 Recent developments (2023–2024 prioritized): avacopan (C5aR1 antagonist)
**Efficacy/safety in RCT subgroup analysis (2024):** In the rituximab induction subgroup of ADVOCATE (NCT02994927), avacopan showed:
* Sustained remission at week 52: 71.0% (avacopan) vs 56.1% (prednisone taper). (geetha2024efficacyandsafety pages 5-5)
* Relapse after achieving BVAS=0 by week 52: 8.7% vs 20.2%. (geetha2024efficacyandsafety pages 4-5)
* Lower cumulative prednisone-equivalent exposure weeks 0–26: mean 1417 mg vs 3265 mg. (geetha2024efficacyandsafety pages 4-5)
* Serious adverse events: 34.6% vs 39.3% (as reported in trial summary text). (geetha2024efficacyandsafety pages 1-2)

**Real-world implementation (2024 DAH cohort):** In a single-center retrospective cohort of 15 patients with AAV presenting with diffuse alveolar hemorrhage, avacopan use was associated with most patients achieving remission during a median 17-week follow-up, but there were serious infections including one death; authors highlighted practical implementation uncertainties (timing, taper strategy, access, long-term safety). (falde2024treatmentofantineutrophil pages 1-2)

**Ongoing/registered trials (real-world implementation trajectory):**
* **ENT-focused trial:** NCT07176546 (not yet recruiting; estimated 2026 start) tests avacopan vs placebo added to standard care for active ENT GPA; primary endpoint is ENT remission without relapse at week 52 with no glucocorticoid exposure in the prior 4 weeks; key secondary endpoints include SNOT‑22 and AAV‑PRO and ENT surgeries/flares. (NCT07176546 chunk 1)
* **ARRIA phase 4:** NCT06611696 (started 2024-11-15) compares avacopan + short-term reduced-dose glucocorticoid + rituximab versus a 20-week reduced-dose glucocorticoid regimen + rituximab in new-onset GPA/MPA; primary endpoint is remission at 26 weeks (BVAS=0 and <5 mg/day prednisolone) and secondary endpoints include VDI and SF‑36 through 104 weeks. (NCT06611696 chunk 1)

### 12.3 Rituximab vs cyclophosphamide trends and outcomes (real-world)
In the 2024 European cohort, cyclophosphamide remained frequently used, but rituximab use increased after 2013; relapse was more common in GPA than MPA. (kramer2024remissioninductiontherapies pages 1-2, kramer2024remissioninductiontherapies pages 4-5)

### 12.4 Supportive care / prophylaxis: PJP prophylaxis with TMP‑SMX during rituximab
A 2023 US administrative claims cohort of rituximab-treated GPA (MarketScan 2011–2020) reported:
* TMP‑SMX prophylaxis dispensed in 23% (426/1877); median persistence 141 days (IQR 83–248). (https://doi.org/10.1186/s13075-023-03114-7) (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)
* Prednisone ≥20 mg/day (vs none) strongly associated with prophylaxis (OR 3.96; 95% CI 3.0–5.2). (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)
* Female sex negatively associated with prophylaxis dispensing (OR 0.63; 95% CI 0.5–0.8). (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)
These data suggest incomplete real-world uptake of guideline-recommended prophylaxis and provide targets for quality improvement. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 6-7)

### 12.5 Suggested MAXO terms (examples; to be curated)
* Complement inhibition / C5a receptor antagonism (avacopan) (geetha2024efficacyandsafety pages 1-2)
* B‑cell depletion therapy (rituximab) (geetha2024efficacyandsafety pages 1-2)
* Cytotoxic immunosuppression (cyclophosphamide) (kramer2024remissioninductiontherapies pages 1-2)
* Pneumocystis jirovecii pneumonia prophylaxis (trimethoprim‑sulfamethoxazole) (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)

---

## 13. Prevention
Evidence in this run supports **tertiary prevention** via infection prophylaxis during immunosuppression (TMP‑SMX for PJP in rituximab-treated GPA), but did not yield evidence-based primary prevention strategies (e.g., vaccination schedules, exposure reduction) specific to GPA. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)

---

## 14. Other species / natural disease
No evidence on naturally occurring GPA in non-human species was retrieved in this run.

---

## 15. Model organisms
No evidence on specific GPA model organisms (e.g., murine PR3-ANCA models) was retrieved in this run.

---

## Cross-cutting quantitative summary table
| Domain | Finding (with numbers) | Population/Context | Source (author/year/DOI) |
|---|---|---|---|
| A. Disease overview & organ involvement | GPA is a rare systemic necrotizing vasculitis with granulomatous inflammation of the respiratory tract and small-/medium-vessel vasculitis; classically affects upper airways, lungs, and kidneys | Disease overview; any organ may be affected | Potentas-Policewicz & Fijolek 2024, Front Med, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2) |
| A. Disease overview & organ involvement | ENT involvement/signs: 80–100% | GPA clinical phenotype | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5) |
| A. Disease overview & organ involvement | Nasal crusting 75%; excessive nose-blowing 70%; nasal obstruction 65%; epistaxis 59%; saddle nose 25% | ENT manifestations in GPA | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5) |
| A. Disease overview & organ involvement | Pulmonary involvement 62–90%; pulmonary nodules/mass lesions 40–70%; cavitation 20–50% | GPA pulmonary disease | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3) |
| A. Disease overview & organ involvement | Diffuse alveolar hemorrhage (DAH) 8.8–36% | GPA pulmonary capillaritis/DAH | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5) |
| A. Disease overview & organ involvement | Kidney involvement 70–85%; renal insufficiency at presentation 11–17%; worsening GFR 24.3% | GPA renal disease course | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| A. Disease overview & organ involvement | Ocular/orbital disease 16–78%; up to 27% present initially with ophthalmic symptoms | Systematic review of ocular/orbital GPA | Moin et al. 2023, doi:10.22336/rjo.2023.38 (moin2023ocularandorbital pages 1-2) |
| A. Disease overview & organ involvement | Ophthalmologic signs 50–60%; orbital lesions 5–30% | GPA extra-renal manifestations | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| A. Disease overview & organ involvement | Oral involvement 6–13%; “strawberry” gingival hyperplasia 61.5% | GPA oral manifestations | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| A. Disease overview & organ involvement | CNS involvement 3–11.7%; PNS involvement 11–44% | GPA neurologic disease | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5) |
| B. ANCA test performance | PR3-ANCA sensitivity for GPA 74% | Diagnostic serology for GPA | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| B. ANCA test performance | MPO-ANCA sensitivity for GPA 11% | Diagnostic serology for GPA | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| B. ANCA test performance | MPO-ANCA sensitivity for MPA 73%; PR3-ANCA sensitivity for MPA 7% | Comparator data highlighting GPA/MPA serologic separation | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| B. ANCA test performance | Specificity of PR3/MPO antigen-specific assays: mean 97% (range 93–99%) | AAV serology; antigen-specific assays preferred over IIF | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| B. ANCA test performance | ANCA-negative proportion about 8.5% | GPA diagnostic workup | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6) |
| B. ANCA test performance | In ocular/orbital GPA case review: c-ANCA 59.2%, p-ANCA 10.8%, granulomas 47.7% | 306 published ocular/orbital GPA cases | Moin et al. 2023, doi:10.22336/rjo.2023.38 (moin2023ocularandorbital pages 1-2) |
| C. 2022 ACR/EULAR classification criteria | Classification threshold: cumulative score ≥5 (one summary reported >5); intended for classification, not diagnosis | Requires prior diagnosis of small-/medium-vessel vasculitis and exclusion of mimics | Robson et al. 2022, Arthritis Rheumatol, doi:10.1002/art.41986; Pyo et al. 2023, doi:10.3349/ymj.2022.0435 (pyo2023comparisonofthe pages 2-4, robson20222022americancollege pages 5-6) |
| C. 2022 ACR/EULAR classification criteria | Available weighted items: nasal passage involvement +3; cartilaginous involvement +2; hearing loss +1; PR3-ANCA/c-ANCA positivity +5; MPO-ANCA/p-ANCA positivity −1; eosinophils ≥1000/µL −4 | GPA scoring items available from review/criteria summary | Pyo et al. 2023, doi:10.3349/ymj.2022.0435 (pyo2023comparisonofthe pages 2-4) |
| C. 2022 ACR/EULAR classification criteria | Additional available weighted items: granuloma/granulomatous inflammation/giant cells on biopsy +2; pauci-immune glomerulonephritis +1; 2 radiology items retained with positive weights but details truncated in excerpt | Incomplete item extraction from available evidence | Pyo et al. 2023, doi:10.3349/ymj.2022.0435 (pyo2023comparisonofthe pages 2-4) |
| C. 2022 ACR/EULAR classification criteria | Validation cohort sizes: development set 578 GPA cases/652 comparators; validation set 146 GPA cases/161 comparators | Original derivation/validation study | Robson et al. 2022, doi:10.1002/art.41986 (from search result summary) (robson20222022americancollege pages 5-6) |
| C. 2022 ACR/EULAR classification criteria | Performance: sensitivity 93% (95% CI 87–96), specificity 94% (95% CI 89–97) | Validation set; research classification performance | Robson et al. 2022, doi:10.1002/art.41986 (from search result summary) (robson20222022americancollege pages 5-6) |
| C. 2022 ACR/EULAR classification criteria | Real-world concordance in previously diagnosed GPA: 48/65 reclassified, 73.8% concordance | Korean application study comparing 2022 criteria with prior criteria | Pyo et al. 2023, doi:10.3349/ymj.2022.0435 (pyo2023comparisonofthe pages 2-4) |
| D. Epidemiology | AAV prevalence estimated at 200–400 per million | Aggregated AAV epidemiology | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2) |
| D. Epidemiology | GPA annual incidence in European adults about 7.7–15.4 per million; Swedish study 15.4/million | Adult epidemiology | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2) |
| D. Epidemiology | Pediatric GPA incidence about 0.88–1.8 per million | Pediatric epidemiology | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2) |
| D. Epidemiology | Diagnostic delay ranged from 1 month to >3 years; 36% had symptoms >1 year before diagnosis | GPA natural history/diagnostic delay | Potentas-Policewicz & Fijolek 2024, doi:10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2) |
| E. Treatment developments | Avacopan RTX subgroup: remission at week 26 77.6% vs 75.7%; sustained remission at week 52 71.0% vs 56.1% | ADVOCATE rituximab induction subgroup; avacopan vs prednisone taper | Geetha et al. 2024, Ann Rheum Dis, doi:10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 5-5, gattu2024superiorityofavacopan pages 5-6, geetha2024efficacyandsafety pages 1-2) |
| E. Treatment developments | Avacopan RTX subgroup relapse after BVAS=0 by week 52: 8.7% vs 20.2% | ADVOCATE rituximab subgroup | Geetha et al. 2024, doi:10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 4-5) |
| E. Treatment developments | Prednisone-equivalent cumulative exposure weeks 0–26: mean 1417 mg vs 3265 mg | Avacopan vs prednisone taper on RTX background | Geetha et al. 2024, doi:10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 4-5) |
| E. Treatment developments | UACR change favored avacopan: about −42% vs +6%; LS mean difference −45 (95% CI −60 to −24) | RTX subgroup renal response | Geetha et al. 2024, doi:10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 4-5) |
| E. Treatment developments | Serious adverse events 34.6% vs 39.3% | RTX subgroup, avacopan vs prednisone taper | Geetha et al. 2024, doi:10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 1-2) |
| E. Treatment developments | Real-world DAH cohort on avacopan: n=15, median age 66, median follow-up 17 weeks; most achieved remission, but 2 serious infections including 1 death | Single-center real-world adjunctive avacopan use in severe AAV with DAH | Falde et al. 2024, doi:10.1002/acr2.11726 (falde2024treatmentofantineutrophil pages 1-2) |
| E. Treatment developments | TMP-SMX prophylaxis in RTX-treated GPA: 426/1877 (23%) overall; new-user subgroup 281/919 (31%); median persistence 141 days (IQR 83–248); 42% continued ≥6 months | US administrative claims cohort, 2011–2020 | Mendel et al. 2023, Arthritis Res Ther, doi:10.1186/s13075-023-03114-7 (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 2-4, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 6-7) |
| E. Treatment developments | Factors associated with TMP-SMX dispensing: prednisone ≥20 mg/day OR 3.96 (95% CI 3.0–5.2); prednisone 1–19 mg/day OR 2.63 (1.8–3.8); methotrexate OR 1.48 (1.04–2.1); ICU hospitalization OR 1.95 (1.4–2.7); female sex OR 0.63 (0.5–0.8) | RTX-treated GPA; prophylaxis targeting higher-risk patients | Mendel et al. 2023, doi:10.1186/s13075-023-03114-7 (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 2-4, mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 6-7) |
| F. Genetics | HLA-DPB1/HLA-DPA1 class II DP locus strongly associated; rs9277554 combined P=1.92×10^-50 and rs9277341 P=2.18×10^-39; signal accounted for by HLA-DPB1*04 | 2013 GWAS, 492 GPA cases/1506 controls with replication in 528 cases/1228 controls | Xie et al. 2013, Arthritis Rheum, doi:10.1002/art.38036 (xie2013associationofgranulomatosis pages 1-2) |
| F. Genetics | SEMA6A rs26595 reached genome-wide significance, P=2.09×10^-8 | GPA GWAS non-MHC locus | Xie et al. 2013, doi:10.1002/art.38036 (xie2013associationofgranulomatosis pages 1-2) |
| F. Genetics | HLA-DP rs3117242: OR 5.39, P=3.1×10^-85 in GPA; OR 7.03, P=6.2×10^-89 in PR3+ subgroup | European GWAS summary for GPA/PR3-AAV | Alberici et al. 2015, NDT, doi:10.1093/ndt/gfu386 (alberici2015geneticaspectsof pages 4-4) |
| F. Genetics | SERPINA1 rs7151526: OR 0.59, P=2.4×10^-9 in GPA+MPA; OR 0.53, P=5.6×10^-12 in PR3+ subgroup; rs28929474 OR 2.9 in PR3-ANCA+ AAV | Non-HLA susceptibility locus involving alpha-1 antitrypsin pathway | Alberici et al. 2015, doi:10.1093/ndt/gfu386; Dahlqvist et al. 2022, doi:10.1093/rheumatology/keab912 (alberici2015geneticaspectsof pages 4-4, merkel2017identificationoffunctional pages 1-4) |
| F. Genetics | PRTN3 rs62132295: OR 0.78, P=2.6×10^-5 in GPA; stronger in PR3-ANCA+ subgroup OR 0.73, P=2.6×10^-7 | PR3 autoantigen gene association | Alberici et al. 2015, doi:10.1093/ndt/gfu386 (alberici2015geneticaspectsof pages 4-4) |
| F. Genetics | Merkel 2017 replication/GWAS: HLA-DPB1 rs141530235 OR 2.99 and rs1042169 OR 2.82; PRTN3 locus linked to increased neutrophil PRTN3 expression; SERPINA1 and PTPN22 also significant | 1986 AAV cases and 4723 controls | Merkel et al. 2017, doi:10.1002/art.40034 (merkel2017identificationoffunctional pages 1-4) |


*Table: This table compiles key quantitative facts on granulomatosis with polyangiitis from the gathered evidence, including organ involvement, ANCA performance, classification criteria, epidemiology, treatment outcomes, and genetic associations. It is designed as a compact reference for the main numeric findings and their sources.*

---

## Key recent developments and expert-level synthesis (2023–2024 emphasis)
1. **Diagnostic modernization and phenotyping:** Recent synthesis emphasizes that formal diagnostic criteria remain lacking and clinicians rely on multimodal evaluation; nevertheless, classification/phenotyping advances (especially PR3‑ANCA vs MPO‑ANCA distinction) are reshaping research cohorts and informing targeted approaches. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2, potentaspolicewicz2024granulomatosiswithpolyangiitis pages 20-22)
2. **Steroid-sparing era:** Avacopan has strong 2024 evidence in rituximab-treated AAV showing improved sustained remission and reduced relapse alongside markedly reduced glucocorticoid exposure, with ongoing trials extending these concepts into organ-specific (ENT) endpoints and longer-term damage/QoL outcomes. (geetha2024efficacyandsafety pages 4-5, NCT07176546 chunk 1, NCT06611696 chunk 1)
3. **Implementation gaps in supportive care:** Despite recommendations for PJP prophylaxis during AAV induction, real-world TMP‑SMX dispensing in rituximab-treated GPA was only ~23%, suggesting a measurable care gap and opportunity for improved preventive practice. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)

---

## URLs and publication dates for key sources used (examples)
* Potentas-Policewicz & Fijolek. *Frontiers in Medicine* (Aug 2024). https://doi.org/10.3389/fmed.2024.1369233 (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2)
* Robson et al. *Arthritis & Rheumatology* (Feb 2022). https://doi.org/10.1002/art.41986 (robson20222022americancollege pages 5-6)
* Geetha et al. *Annals of the Rheumatic Diseases* (Feb 2024). https://doi.org/10.1136/ard-2023-224816 (geetha2024efficacyandsafety pages 1-2)
* Mendel et al. *Arthritis Research & Therapy* (Jul 2023). https://doi.org/10.1186/s13075-023-03114-7 (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2)
* Xie et al. *Arthritis & Rheumatism* (Aug 2013). https://doi.org/10.1002/art.38036 (xie2013associationofgranulomatosis pages 1-2)
* ClinicalTrials.gov NCT06611696 (trial record, 2024). https://clinicaltrials.gov/study/NCT06611696 (NCT06611696 chunk 1)
* ClinicalTrials.gov NCT07176546 (trial record, 2026). https://clinicaltrials.gov/study/NCT07176546 (NCT07176546 chunk 1)


References

1. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 1-2): Malgorzata Potentas-Policewicz and Justyna Fijolek. Granulomatosis with polyangiitis: clinical characteristics and updates in diagnosis. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1369233, doi:10.3389/fmed.2024.1369233. This article has 49 citations.

2. (xie2013associationofgranulomatosis pages 1-2): Gang Xie, Delnaz Roshandel, Richard Sherva, Paul A. Monach, Emily Yue Lu, Tabitha Kung, Keisha Carrington, Steven S. Zhang, Sara L. Pulit, Stephan Ripke, Simon Carette, Paul F. Dellaripa, Jeffrey C. Edberg, Gary S. Hoffman, Nader Khalidi, Carol A. Langford, Alfred D. Mahr, E. William St.Clair, Philip Seo, Ulrich Specks, Robert F. Spiera, John H. Stone, Steven R. Ytterberg, Soumya Raychaudhuri, Paul I. W. de Bakker, Lindsay A. Farrer, Christopher I. Amos, Peter A. Merkel, and Katherine A. Siminovitch. Association of granulomatosis with polyangiitis (wegener's) with <i>hla–dpb1*04</i> and <i>sema6a</i> gene variants: evidence from genome‐wide analysis. Arthritis &amp; Rheumatism, 65:2457-2468, Aug 2013. URL: https://doi.org/10.1002/art.38036, doi:10.1002/art.38036. This article has 229 citations.

3. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 1-2): Arielle Mendel, Hassan Behlouli, Cristiano Soares de Moura, Évelyne Vinet, Jeffrey R. Curtis, and Sasha Bernatsky. Trimethoprim-sulfamethoxazole prophylaxis during treatment of granulomatosis with polyangiitis with rituximab in the united states of america: a retrospective cohort study. Arthritis Research & Therapy, Jul 2023. URL: https://doi.org/10.1186/s13075-023-03114-7, doi:10.1186/s13075-023-03114-7. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (kramer2024remissioninductiontherapies pages 1-2): Stefan Krämer, Kristian Vogt, Theresa Maria Schreibing, Martin Busch, Tobias Schmitt, Raoul Bergner, Sebastian Mosberger, Thomas Neumann, and Thomas Rauen. Remission induction therapies and long-term outcomes in granulomatosis with polyangiitis and microscopic polyangiitis: real-world data from a european cohort. Rheumatology International, Dec 2024. URL: https://doi.org/10.1007/s00296-024-05757-4, doi:10.1007/s00296-024-05757-4. This article has 10 citations and is from a peer-reviewed journal.

5. (NCT07176546 chunk 1): Robert Spiera, MD. TAVNEOS for Otolaryngologic Manifestations of Granulomatosis With Polyangiitis. Robert Spiera, MD. 2026. ClinicalTrials.gov Identifier: NCT07176546

6. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 5-6): Malgorzata Potentas-Policewicz and Justyna Fijolek. Granulomatosis with polyangiitis: clinical characteristics and updates in diagnosis. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1369233, doi:10.3389/fmed.2024.1369233. This article has 49 citations.

7. (alberici2015geneticaspectsof pages 4-4): F. Alberici, D. Martorana, and A. Vaglio. Genetic aspects of anti-neutrophil cytoplasmic antibody-associated vasculitis. Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association, 30 Suppl 1:i37-45, Dec 2015. URL: https://doi.org/10.1093/ndt/gfu386, doi:10.1093/ndt/gfu386. This article has 63 citations.

8. (merkel2017identificationoffunctional pages 1-4): Peter A. Merkel, Gang Xie, Paul A. Monach, Xuemei Ji, Dominic J. Ciavatta, Jinyoung Byun, Benjamin D. Pinder, Ai Zhao, Jinyi Zhang, Yohannes Tadesse, David Qian, Matthew Weirauch, Rajan Nair, Alex Tsoi, Christian Pagnoux, Simon Carette, Sharon Chung, David Cuthbertson, John C. Davis, Paul F. Dellaripa, Lindsy Forbess, Ora Gewurz‐Singer, Gary S. Hoffman, Nader Khalidi, Curry Koening, Carol A. Langford, Alfred D. Mahr, Carol McAlear, Larry Moreland, E. Philip Seo, Ulrich Specks, Robert F. Spiera, Antoine Sreih, E. William St.Clair, John H. Stone, Steven R. Ytterberg, James T. Elder, Jia Qu, Toshiki Ochi, Naoto Hirano, Jeffrey C. Edberg, Ronald J. Falk, Christopher I. Amos, and Katherine A. Siminovitch. Identification of functional and expression polymorphisms associated with risk for antineutrophil cytoplasmic autoantibody–associated vasculitis. Arthritis & Rheumatology (Hoboken, N.j.), 69:1054-1066, Apr 2017. URL: https://doi.org/10.1002/art.40034, doi:10.1002/art.40034. This article has 205 citations.

9. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 4-5): Malgorzata Potentas-Policewicz and Justyna Fijolek. Granulomatosis with polyangiitis: clinical characteristics and updates in diagnosis. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1369233, doi:10.3389/fmed.2024.1369233. This article has 49 citations.

10. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 2-3): Malgorzata Potentas-Policewicz and Justyna Fijolek. Granulomatosis with polyangiitis: clinical characteristics and updates in diagnosis. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1369233, doi:10.3389/fmed.2024.1369233. This article has 49 citations.

11. (moin2023ocularandorbital pages 1-2): Kayvon Moin, Madeleine Marta Yeakle, A. Parrill, Victoria Anne Garofalo, A. Tsiyer, Daniel Bishev, Dhir Gala, Joshua Fogel, Alexander James Hatsis, Tyler Wickas, P. Anand, and Marcelle Morcos. Ocular and orbital manifestations of granulomatosis with polyangiitis: a systematic review of published cases. Romanian Journal of Ophthalmology, 67:214-221, Oct 2023. URL: https://doi.org/10.22336/rjo.2023.38, doi:10.22336/rjo.2023.38. This article has 20 citations.

12. (geetha2024efficacyandsafety pages 4-5): Duvuru Geetha, Anisha Dua, Huibin Yue, Jason Springer, Carlo Salvarani, David Jayne, Peter Merkel, C. Au Peh, A. Chakera, B. Cooper, J. Kurtkoti, D. Langguth, V. Levidiotis, G. Luxton, P. Mount, D. Mudge, E. Noble, R. Phoon, A. Ritchie, J. Ryan, M. Suranyi, A. Rosenkranz, A. Kronbichler, N. Demoulin, C. Bovy, R. Hellemans, J. Hougardy, B. Sprangers, K. Wissing, C. Pagnoux, S. Barbour, S. Brachemi, S. Cournoyer, L. Girard, L. Laurin, P. Liang, D. Philibert, M. Walsh, V. Tesar, R. Becvar, P. Horak, I. Rychlik, W. Szpirt, H. Dieperink, J. Gregersen, P. Ivarsen, E. Krarup, C. Lyngsoe, C. Rigothier, J. Augusto, A. Belot, D. Chauveau, D. Cornec, N. Jourde-Chiche, M. Ficheux, A. Karras, A. Klein, F. Maurier, R. Mesbah, O. Moranne, A. Neel, T. Quemeneur, D. Saadoun, B. Terrier, P. Zaoui, M. Schaier, U. Benck, R. Bergner, M. Busch, J. Floege, F. Grundmann, H. Haller, M. Haubitz, B. Hellmich, J. Henes, B. Hohenstein, C. Hugo, C. Iking-Konert, F. Arndt, T. Kubacki, I. Kotter, P. Lamprecht, T. Lindner, J. Halbritter, H. Mehling, U. Schönermarck, N. Venhoff, V. Vielhauer, O. Witzke, I. Szombati, G. Szucs, G. Garibotto, F. Alberici, E. Brunetta, L. Dagna, S. De Vita, G. Emmi, A. Gabrielli, L. Manenti, F. Pieruzzi, D. Roccatello, C. Salvarani, M. Harigai, H. Dobashi, T. Atsumi, S. Fujimoto, N. Hagino, A. Ihata, S. Kaname, Y. Kaneko, A. Katagiri, M. Katayama, Y. Kirino, K. Kitagawa, A. Komatsuda, H. Kono, T. Kurasawa, R. Matsumura, T. Mimura, A. Morinobu, Y. Murakawa, T. Naniwa, T. Nanki, N. Ogawa, H. Oshima, K. Sada, E. Sugiyama, T. Takeuchi, H Taki, N. Tamura, T. Tsukamoto, K. Yamagata, M. Yamamura, P. van Daele, A. Rutgers, Y. Teng, R. Walker, I. Chua, M. Collins, K. Rabindranath, J. de Zoysa, M. Svensson, B. Grevbo, S. Kalstad, M. Little, M. Clarkson, E. Molloy, I. Agraz Pamplona, J. Anton, V. Barrio Lucia, S. Ciggaran, M. Cinta Cid, M. Diaz Encarnacion, X. Fulladosa Oliveras, M. Jose Soler, H. Marco Rusinol, M. Praga, L. Quintana Porras, A. Segarra, A. Bruchfeld, M. Segelmark, I. Soveri, E. Thomaidi, K. Westman, T. Neumann, M. Burnier, T. Daikeler, J. Dudler, T. Hauser, H. Seeger, B. Vogt, D. Jayne, J. Burton, R. Al Jayyousi, T. Amin, J. Andrews, L. Baines, P. Brogan, B. Dasgupta, T. Doulton, O. Flossmann, S. Griffin, J. Harper, L. Harper, D. Kidder, R. Klocke, P. Lanyon, R. Luqmani, J. McLaren, D. Makanjuola, L. McCann, A. Nandagudi, S. Selvan, E. O’Riordan, M. Patel, R. Patel, C. Pusey, R. Rajakariar, J. Robson, M. Robson, A. Salama, L. Smyth, J. Sznajd, J. Taylor, P. Merkel, A. Sreih, E. Belilos, A. Bomback, J. Carlin; Y, Chang Chen Lin, V. Derebail, S. Dragoi, A. Dua, L. Forbess, D. Geetha, P. Gipson, R. Gohh, G.T. Greenwood, S. Hugenberg, R. Jimenez, M. Kaskas, T. Kermani, A. Kivitz, C. Koening, C. Langford, G. Marder, A. Mohamed, P. Monach, N. Neyra, G. Niemer, J. Niles, R. Obi, C. Owens, D. Parks, A. Podoll, B. Rovin, R. Sam, W. Shergy, A. Silva, R. Spiera, J. Springer, C. Striebich, A. Swarup, S. Thakar, A. Tiliakos, Y. Tsai, D. Waguespack, and M. Chester Wasko. Efficacy and safety of avacopan in patients with anca-associated vasculitis receiving rituximab in a randomised trial. Annals of the Rheumatic Diseases, 83:223-232, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224816, doi:10.1136/ard-2023-224816. This article has 63 citations and is from a highest quality peer-reviewed journal.

13. (draibe2024diagnosisandtreatment pages 2-3): Juliana Bordignon Draibe, Helena Marco, Meritxell Ibernon, Irene Agraz, Carola Arcal, Xoana Barros, Victoria Cabrera, Iara Da Silva, Montserrat Díaz, Xavier Fulladosa, Elena Guillén, Patricia Lescano, Laura Martínez Valenzuela, Eva Márquez, Nadia Martín, Ana Merino, Maru Navarro, Eva Rodríguez, Mª José Soler, Joan Torras, and Luís F. Quintana. Diagnosis and treatment of renal anca vasculitis: a summary of the consensus document of the catalan group for the study of glomerular diseases (glomcat). Journal of Clinical Medicine, 13:6793, Nov 2024. URL: https://doi.org/10.3390/jcm13226793, doi:10.3390/jcm13226793. This article has 2 citations.

14. (geetha2024efficacyandsafety pages 1-2): Duvuru Geetha, Anisha Dua, Huibin Yue, Jason Springer, Carlo Salvarani, David Jayne, Peter Merkel, C. Au Peh, A. Chakera, B. Cooper, J. Kurtkoti, D. Langguth, V. Levidiotis, G. Luxton, P. Mount, D. Mudge, E. Noble, R. Phoon, A. Ritchie, J. Ryan, M. Suranyi, A. Rosenkranz, A. Kronbichler, N. Demoulin, C. Bovy, R. Hellemans, J. Hougardy, B. Sprangers, K. Wissing, C. Pagnoux, S. Barbour, S. Brachemi, S. Cournoyer, L. Girard, L. Laurin, P. Liang, D. Philibert, M. Walsh, V. Tesar, R. Becvar, P. Horak, I. Rychlik, W. Szpirt, H. Dieperink, J. Gregersen, P. Ivarsen, E. Krarup, C. Lyngsoe, C. Rigothier, J. Augusto, A. Belot, D. Chauveau, D. Cornec, N. Jourde-Chiche, M. Ficheux, A. Karras, A. Klein, F. Maurier, R. Mesbah, O. Moranne, A. Neel, T. Quemeneur, D. Saadoun, B. Terrier, P. Zaoui, M. Schaier, U. Benck, R. Bergner, M. Busch, J. Floege, F. Grundmann, H. Haller, M. Haubitz, B. Hellmich, J. Henes, B. Hohenstein, C. Hugo, C. Iking-Konert, F. Arndt, T. Kubacki, I. Kotter, P. Lamprecht, T. Lindner, J. Halbritter, H. Mehling, U. Schönermarck, N. Venhoff, V. Vielhauer, O. Witzke, I. Szombati, G. Szucs, G. Garibotto, F. Alberici, E. Brunetta, L. Dagna, S. De Vita, G. Emmi, A. Gabrielli, L. Manenti, F. Pieruzzi, D. Roccatello, C. Salvarani, M. Harigai, H. Dobashi, T. Atsumi, S. Fujimoto, N. Hagino, A. Ihata, S. Kaname, Y. Kaneko, A. Katagiri, M. Katayama, Y. Kirino, K. Kitagawa, A. Komatsuda, H. Kono, T. Kurasawa, R. Matsumura, T. Mimura, A. Morinobu, Y. Murakawa, T. Naniwa, T. Nanki, N. Ogawa, H. Oshima, K. Sada, E. Sugiyama, T. Takeuchi, H Taki, N. Tamura, T. Tsukamoto, K. Yamagata, M. Yamamura, P. van Daele, A. Rutgers, Y. Teng, R. Walker, I. Chua, M. Collins, K. Rabindranath, J. de Zoysa, M. Svensson, B. Grevbo, S. Kalstad, M. Little, M. Clarkson, E. Molloy, I. Agraz Pamplona, J. Anton, V. Barrio Lucia, S. Ciggaran, M. Cinta Cid, M. Diaz Encarnacion, X. Fulladosa Oliveras, M. Jose Soler, H. Marco Rusinol, M. Praga, L. Quintana Porras, A. Segarra, A. Bruchfeld, M. Segelmark, I. Soveri, E. Thomaidi, K. Westman, T. Neumann, M. Burnier, T. Daikeler, J. Dudler, T. Hauser, H. Seeger, B. Vogt, D. Jayne, J. Burton, R. Al Jayyousi, T. Amin, J. Andrews, L. Baines, P. Brogan, B. Dasgupta, T. Doulton, O. Flossmann, S. Griffin, J. Harper, L. Harper, D. Kidder, R. Klocke, P. Lanyon, R. Luqmani, J. McLaren, D. Makanjuola, L. McCann, A. Nandagudi, S. Selvan, E. O’Riordan, M. Patel, R. Patel, C. Pusey, R. Rajakariar, J. Robson, M. Robson, A. Salama, L. Smyth, J. Sznajd, J. Taylor, P. Merkel, A. Sreih, E. Belilos, A. Bomback, J. Carlin; Y, Chang Chen Lin, V. Derebail, S. Dragoi, A. Dua, L. Forbess, D. Geetha, P. Gipson, R. Gohh, G.T. Greenwood, S. Hugenberg, R. Jimenez, M. Kaskas, T. Kermani, A. Kivitz, C. Koening, C. Langford, G. Marder, A. Mohamed, P. Monach, N. Neyra, G. Niemer, J. Niles, R. Obi, C. Owens, D. Parks, A. Podoll, B. Rovin, R. Sam, W. Shergy, A. Silva, R. Spiera, J. Springer, C. Striebich, A. Swarup, S. Thakar, A. Tiliakos, Y. Tsai, D. Waguespack, and M. Chester Wasko. Efficacy and safety of avacopan in patients with anca-associated vasculitis receiving rituximab in a randomised trial. Annals of the Rheumatic Diseases, 83:223-232, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224816, doi:10.1136/ard-2023-224816. This article has 63 citations and is from a highest quality peer-reviewed journal.

15. (pyo2023comparisonofthe pages 2-4): Jung Yoon Pyo, Lucy Eunju Lee, Yong-Beom Park, and Sang-Won Lee. Comparison of the 2022 acr/eular classification criteria for antineutrophil cytoplasmic antibody-associated vasculitis with previous criteria. Yonsei Medical Journal, 64:11, Jan 2023. URL: https://doi.org/10.3349/ymj.2022.0435, doi:10.3349/ymj.2022.0435. This article has 95 citations and is from a peer-reviewed journal.

16. (robson20222022americancollege pages 5-6): Joanna C. Robson, Peter C. Grayson, Cristina Ponte, Ravi Suppiah, Anthea Craven, Andrew Judge, Sara Khalid, Andrew Hutchings, Richard A. Watts, Peter A. Merkel, and Raashid A. Luqmani. 2022 american college of rheumatology/european alliance of associations for rheumatology classification criteria for granulomatosis with polyangiitis. Arthritis &amp; Rheumatology, 74:393-399, Feb 2022. URL: https://doi.org/10.1002/art.41986, doi:10.1002/art.41986. This article has 797 citations and is from a highest quality peer-reviewed journal.

17. (robson20222022americancollege media d7729245): Joanna C. Robson, Peter C. Grayson, Cristina Ponte, Ravi Suppiah, Anthea Craven, Andrew Judge, Sara Khalid, Andrew Hutchings, Richard A. Watts, Peter A. Merkel, and Raashid A. Luqmani. 2022 american college of rheumatology/european alliance of associations for rheumatology classification criteria for granulomatosis with polyangiitis. Arthritis &amp; Rheumatology, 74:393-399, Feb 2022. URL: https://doi.org/10.1002/art.41986, doi:10.1002/art.41986. This article has 797 citations and is from a highest quality peer-reviewed journal.

18. (kramer2024remissioninductiontherapies pages 4-5): Stefan Krämer, Kristian Vogt, Theresa Maria Schreibing, Martin Busch, Tobias Schmitt, Raoul Bergner, Sebastian Mosberger, Thomas Neumann, and Thomas Rauen. Remission induction therapies and long-term outcomes in granulomatosis with polyangiitis and microscopic polyangiitis: real-world data from a european cohort. Rheumatology International, Dec 2024. URL: https://doi.org/10.1007/s00296-024-05757-4, doi:10.1007/s00296-024-05757-4. This article has 10 citations and is from a peer-reviewed journal.

19. (geetha2024efficacyandsafety pages 5-5): Duvuru Geetha, Anisha Dua, Huibin Yue, Jason Springer, Carlo Salvarani, David Jayne, Peter Merkel, C. Au Peh, A. Chakera, B. Cooper, J. Kurtkoti, D. Langguth, V. Levidiotis, G. Luxton, P. Mount, D. Mudge, E. Noble, R. Phoon, A. Ritchie, J. Ryan, M. Suranyi, A. Rosenkranz, A. Kronbichler, N. Demoulin, C. Bovy, R. Hellemans, J. Hougardy, B. Sprangers, K. Wissing, C. Pagnoux, S. Barbour, S. Brachemi, S. Cournoyer, L. Girard, L. Laurin, P. Liang, D. Philibert, M. Walsh, V. Tesar, R. Becvar, P. Horak, I. Rychlik, W. Szpirt, H. Dieperink, J. Gregersen, P. Ivarsen, E. Krarup, C. Lyngsoe, C. Rigothier, J. Augusto, A. Belot, D. Chauveau, D. Cornec, N. Jourde-Chiche, M. Ficheux, A. Karras, A. Klein, F. Maurier, R. Mesbah, O. Moranne, A. Neel, T. Quemeneur, D. Saadoun, B. Terrier, P. Zaoui, M. Schaier, U. Benck, R. Bergner, M. Busch, J. Floege, F. Grundmann, H. Haller, M. Haubitz, B. Hellmich, J. Henes, B. Hohenstein, C. Hugo, C. Iking-Konert, F. Arndt, T. Kubacki, I. Kotter, P. Lamprecht, T. Lindner, J. Halbritter, H. Mehling, U. Schönermarck, N. Venhoff, V. Vielhauer, O. Witzke, I. Szombati, G. Szucs, G. Garibotto, F. Alberici, E. Brunetta, L. Dagna, S. De Vita, G. Emmi, A. Gabrielli, L. Manenti, F. Pieruzzi, D. Roccatello, C. Salvarani, M. Harigai, H. Dobashi, T. Atsumi, S. Fujimoto, N. Hagino, A. Ihata, S. Kaname, Y. Kaneko, A. Katagiri, M. Katayama, Y. Kirino, K. Kitagawa, A. Komatsuda, H. Kono, T. Kurasawa, R. Matsumura, T. Mimura, A. Morinobu, Y. Murakawa, T. Naniwa, T. Nanki, N. Ogawa, H. Oshima, K. Sada, E. Sugiyama, T. Takeuchi, H Taki, N. Tamura, T. Tsukamoto, K. Yamagata, M. Yamamura, P. van Daele, A. Rutgers, Y. Teng, R. Walker, I. Chua, M. Collins, K. Rabindranath, J. de Zoysa, M. Svensson, B. Grevbo, S. Kalstad, M. Little, M. Clarkson, E. Molloy, I. Agraz Pamplona, J. Anton, V. Barrio Lucia, S. Ciggaran, M. Cinta Cid, M. Diaz Encarnacion, X. Fulladosa Oliveras, M. Jose Soler, H. Marco Rusinol, M. Praga, L. Quintana Porras, A. Segarra, A. Bruchfeld, M. Segelmark, I. Soveri, E. Thomaidi, K. Westman, T. Neumann, M. Burnier, T. Daikeler, J. Dudler, T. Hauser, H. Seeger, B. Vogt, D. Jayne, J. Burton, R. Al Jayyousi, T. Amin, J. Andrews, L. Baines, P. Brogan, B. Dasgupta, T. Doulton, O. Flossmann, S. Griffin, J. Harper, L. Harper, D. Kidder, R. Klocke, P. Lanyon, R. Luqmani, J. McLaren, D. Makanjuola, L. McCann, A. Nandagudi, S. Selvan, E. O’Riordan, M. Patel, R. Patel, C. Pusey, R. Rajakariar, J. Robson, M. Robson, A. Salama, L. Smyth, J. Sznajd, J. Taylor, P. Merkel, A. Sreih, E. Belilos, A. Bomback, J. Carlin; Y, Chang Chen Lin, V. Derebail, S. Dragoi, A. Dua, L. Forbess, D. Geetha, P. Gipson, R. Gohh, G.T. Greenwood, S. Hugenberg, R. Jimenez, M. Kaskas, T. Kermani, A. Kivitz, C. Koening, C. Langford, G. Marder, A. Mohamed, P. Monach, N. Neyra, G. Niemer, J. Niles, R. Obi, C. Owens, D. Parks, A. Podoll, B. Rovin, R. Sam, W. Shergy, A. Silva, R. Spiera, J. Springer, C. Striebich, A. Swarup, S. Thakar, A. Tiliakos, Y. Tsai, D. Waguespack, and M. Chester Wasko. Efficacy and safety of avacopan in patients with anca-associated vasculitis receiving rituximab in a randomised trial. Annals of the Rheumatic Diseases, 83:223-232, Feb 2024. URL: https://doi.org/10.1136/ard-2023-224816, doi:10.1136/ard-2023-224816. This article has 63 citations and is from a highest quality peer-reviewed journal.

20. (falde2024treatmentofantineutrophil pages 1-2): Sam D. Falde, Amos Lal, Rodrigo Cartin‐Ceba, Lester E. Mertz, Fernando C. Fervenza, Ladan Zand, Matthew J. Koster, Kenneth J. Warrington, Augustine S. Lee, Nabeel Aslam, Andy Abril, and Ulrich Specks. Treatment of antineutrophil cytoplasmic antibody–associated vasculitis with diffuse alveolar hemorrhage with avacopan. ACR Open Rheumatology, 6:707-716, Jul 2024. URL: https://doi.org/10.1002/acr2.11726, doi:10.1002/acr2.11726. This article has 11 citations and is from a peer-reviewed journal.

21. (NCT06611696 chunk 1): Shunsuke Furuta. Avacopan vs Reduced-dose Glucocorticoids in ANCA-associated Vasculitis. Chiba University. 2024. ClinicalTrials.gov Identifier: NCT06611696

22. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 6-7): Arielle Mendel, Hassan Behlouli, Cristiano Soares de Moura, Évelyne Vinet, Jeffrey R. Curtis, and Sasha Bernatsky. Trimethoprim-sulfamethoxazole prophylaxis during treatment of granulomatosis with polyangiitis with rituximab in the united states of america: a retrospective cohort study. Arthritis Research & Therapy, Jul 2023. URL: https://doi.org/10.1186/s13075-023-03114-7, doi:10.1186/s13075-023-03114-7. This article has 5 citations and is from a domain leading peer-reviewed journal.

23. (gattu2024superiorityofavacopan pages 5-6): Rishma Gattu, Michelle Demory Beckler, and Marc M. Kesselman. Superiority of avacopan and mepolizumab to glucocorticoid tapering in the treatment of anti-neutrophil cytoplasmic antibody (anca)-associated vasculitis: a systematic review. Cureus, Aug 2024. URL: https://doi.org/10.7759/cureus.67161, doi:10.7759/cureus.67161. This article has 5 citations.

24. (mendel2023trimethoprimsulfamethoxazoleprophylaxisduring pages 2-4): Arielle Mendel, Hassan Behlouli, Cristiano Soares de Moura, Évelyne Vinet, Jeffrey R. Curtis, and Sasha Bernatsky. Trimethoprim-sulfamethoxazole prophylaxis during treatment of granulomatosis with polyangiitis with rituximab in the united states of america: a retrospective cohort study. Arthritis Research & Therapy, Jul 2023. URL: https://doi.org/10.1186/s13075-023-03114-7, doi:10.1186/s13075-023-03114-7. This article has 5 citations and is from a domain leading peer-reviewed journal.

25. (potentaspolicewicz2024granulomatosiswithpolyangiitis pages 20-22): Malgorzata Potentas-Policewicz and Justyna Fijolek. Granulomatosis with polyangiitis: clinical characteristics and updates in diagnosis. Frontiers in Medicine, Aug 2024. URL: https://doi.org/10.3389/fmed.2024.1369233, doi:10.3389/fmed.2024.1369233. This article has 49 citations.