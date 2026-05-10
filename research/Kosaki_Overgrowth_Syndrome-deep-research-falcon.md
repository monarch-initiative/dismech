---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:21:13.840866'
end_time: '2026-05-09T10:36:01.538337'
duration_seconds: 887.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kosaki Overgrowth Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kosaki Overgrowth Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Kosaki Overgrowth Syndrome** covering all of the
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
- **Disease Name:** Kosaki Overgrowth Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Kosaki Overgrowth Syndrome** covering all of the
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


# Kosaki Overgrowth Syndrome (KOGS) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Kosaki overgrowth syndrome (KOGS)
- **Category:** Genetic overgrowth/connective-tissue disorder
- **Causal gene:** **PDGFRB** (platelet-derived growth factor receptor beta)
- **Ontology mapping:** MONDO **MONDO_0014704** (“skeletal overgrowth–craniofacial dysmorphism–hyperelastic skin–white matter lesions syndrome”), used as an ontology-style label for the same entity in OpenTargets (OpenTargets Search: Kosaki overgrowth syndrome).

| Disease name | Synonyms / alternate names | MONDO ID | OMIM disease ID | Causal gene (symbol; OMIM) | Notes on terminology | Sources |
|---|---|---|---|---|---|---|
| Kosaki overgrowth syndrome | KOGS; PDGFRB-related overgrowth syndrome; skeletal overgrowth-craniofacial dysmorphism-hyperelastic skin-white matter lesions syndrome | MONDO:0014704 | OMIM:616592 | PDGFRB; OMIM:173410 | Current disease label in case series/reviews is **Kosaki overgrowth syndrome**. Open Targets maps PDGFRB to the MONDO disease name **skeletal overgrowth-craniofacial dysmorphism-hyperelastic skin-white matter lesions syndrome**, which appears to represent the same entity in ontology-oriented resources. | (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, OpenTargets Search: Kosaki overgrowth syndrome) |
| Skeletal overgrowth-craniofacial dysmorphism-hyperelastic skin-white matter lesions syndrome | Kosaki overgrowth syndrome; KOGS | MONDO:0014704 | OMIM:616592 | PDGFRB; OMIM:173410 | Descriptive/ontology-style synonym emphasizing the core phenotype: skeletal overgrowth, craniofacial dysmorphism, hyperelastic skin, and white matter lesions. Useful for cross-resource harmonization. | (OpenTargets Search: Kosaki overgrowth syndrome, takenouchi2019kosakiovergrowthsyndrome pages 1-3) |
| PDGFRB-related disorder spectrum entry relevant to KOGS | PDGFRB-activating variant spectrum (broader umbrella); overlaps with Penttinen syndrome and infantile myofibromatosis | Not disease-specific in cited sources | KOGS within OMIM:616592 | PDGFRB; OMIM:173410 | Several reviews argue that KOGS is part of a broader **PDGFRB activating variant spectrum**, but KOGS remains a clinically recognizable syndrome with its own OMIM entry. | (foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2021progressivecerebraland pages 4-5, wenger2020activatingvariantsin pages 2-4, wenger2020activatingvariantsin pages 14-15) |


*Table: This table summarizes the main disease names, cross-resource identifiers, and terminology mappings used for Kosaki overgrowth syndrome. It is useful for harmonizing OMIM/MONDO naming with the PDGFRB-related disease spectrum in a knowledge base.*

---

## 1. Disease Information

### Overview / definition
Kosaki overgrowth syndrome is an **ultra-rare, clinically recognizable** overgrowth/connective-tissue syndrome caused by **heterozygous activating (gain-of-function) PDGFRB variants**, classically presenting with **postnatal skeletal overgrowth**, **hyperelastic/fragile skin with poor wound healing**, **lipodystrophy/progeroid features**, **scoliosis/joint contractures**, and a characteristic neuroimaging pattern of **periventricular white matter lesions** and **posterior fossa anomalies**; an important recent expansion of the phenotype includes **progressive, potentially fatal cerebrovascular and coronary aneurysms** (foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2021progressivecerebraland pages 2-4, takenouchi2019kosakiovergrowthsyndrome pages 3-4).

### Key identifiers (best available from accessible corpus)
- **OMIM disease:** **616592** (Kosaki overgrowth syndrome) (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4)
- **OMIM gene:** **PDGFRB** **173410** (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2)
- **MONDO:** **MONDO_0014704** (OpenTargets mapping) (OpenTargets Search: Kosaki overgrowth syndrome)

**Not found in the currently accessible full-text corpus:** Orphanet ID, MeSH ID, ICD-10/ICD-11 codes.

### Synonyms / alternative names
- “KOGS” (common abbreviation) (foster2020kosakiovergrowthsyndrome pages 1-2)
- “PDGFRB-related overgrowth syndrome” / part of a “PDGFRB activating variant spectrum” (broader umbrella across overlapping phenotypes) (wenger2020activatingvariantsin pages 2-4, wenger2020activatingvariantsin pages 14-15)
- Ontology-style name emphasizing core features: “skeletal overgrowth–craniofacial dysmorphism–hyperelastic skin–white matter lesions syndrome” (OpenTargets Search: Kosaki overgrowth syndrome)

### Evidence type
The KOGS knowledge base is primarily derived from **individual patients in case reports/case series** and subsequent synthesis reviews (e.g., 2017 expansion; 2019 clinical review; 2020 case series with vascular complications; 2021 longitudinal imaging of original patients) (minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4, foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2021progressivecerebraland pages 2-4).

---

## 2. Etiology

### Disease causal factors
**Primary cause:** germline **gain-of-function PDGFRB variants** (typically missense) leading to constitutive receptor tyrosine kinase signaling (minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 1-3, foster2020kosakiovergrowthsyndrome pages 10-11).

A mechanistic genotype contrast is explicitly described: **“hypermorphic mutations in PDGFRB lead to Kosaki overgrowth syndrome… whereas hypomorphic mutations lead to idiopathic basal ganglia calcification”** (minatogawa2017expansionofthe pages 1-2).

### Risk factors
- **Genetic:** presence of a germline activating PDGFRB variant; de novo occurrence is common in classic KOGS (minatogawa2017expansionofthe pages 1-2, foster2020kosakiovergrowthsyndrome pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4).
- **Age-related progression risk:** vascular complications appear **progressive** and may emerge with age; Foster et al. note that features are progressive and it is “probably that vascular complications may develop with age” (foster2020kosakiovergrowthsyndrome pages 10-11).

No environmental risk modifiers have been established in the accessible literature.

### Protective factors / Gene–environment interaction
No protective factors or gene–environment interaction evidence specific to KOGS was identified in the accessible corpus.

---

## 3. Phenotypes

### Phenotypic spectrum (with suggested HPO terms)
| Phenotypic feature | Clinical category | Reported frequency / count | Phenotype details | Suggested HPO term(s) | Key source(s) |
|---|---|---:|---|---|---|
| Periventricular white matter lesions / signal abnormalities | Neuroimaging abnormality | 100% (all reported patients in 2019 review) | Best detected on FLAIR; described as periventricular white matter hyperintensities/signal abnormalities and considered a core radiologic hallmark | HP:0002500 Cerebral white matter abnormality; HP:0007054 Periventricular white matter abnormalities | (takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Posterior fossa arachnoid cysts / posterior fossa protrusion | Neuroimaging structural abnormality | ~83% (5/6) | Enlarged posterior fossa subarachnoid space/arachnoid cysts; part of recurrent CNS imaging pattern | HP:0002276 Arachnoid cyst; HP:0002280 Dandy-Walker malformation (when present) | (takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3) |
| Lipodystrophy / progressive loss of subcutaneous fat | Connective tissue / body composition | ~83% | Progressive periorbital and generalized subcutaneous fat loss contributes to prematurely aged/progeroid appearance | HP:0009125 Lipodystrophy; HP:0007495 Prematurely aged appearance | (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Hyperelastic, thin, fragile, translucent skin with poor wound healing | Dermatologic / connective tissue | Common; described as universal in small review cohort for hyperelastic/thin/fragile skin | Includes velvety/translucent skin, widened scarring, skin hyperextensibility, poor wound healing | HP:0000974 Hyperelastic skin; HP:0008066 Thin skin; HP:0001030 Fragile skin; HP:0001058 Poor wound healing | (minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 4-5, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Postnatal skeletal overgrowth / tall stature | Growth abnormality | Hallmark feature; frequency not numerically stated in accessible texts | Height >2 SD, large hands/feet or palms/soles; overgrowth is postnatal rather than clearly prenatal | HP:0000098 Tall stature; HP:0001161 Broad hand or HP:0100807 Large hand; HP:0001173 Broad foot or HP:0001833 Large foot | (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 4-5, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Macrocephaly | Growth / craniofacial | Reported; frequency not available in accessible texts | May be pronounced from birth in some patients | HP:0000256 Macrocephaly | (gawlinski2018phenotypeexpansionand pages 1-4) |
| Craniosynostosis | Craniofacial / skeletal | ~33% | Can involve multiple sutures; cranial deformity and skull radiograph abnormalities reported | HP:0001363 Craniosynostosis | (foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3) |
| Distinctive craniofacial dysmorphism | Craniofacial | Frequent, but no pooled % in accessible texts | Frontal prominence, supraorbital ridges, ptosis/proptosis, apparent hypertelorism, wide nasal bridge, high columella, triangular face, long palpebral fissures with lateral ectropion | HP:0002007 Frontal bossing; HP:0009912 Hypertelorism; HP:0000508 Ptosis; HP:0000589 Narrow palpebral fissure / HP:0000637 Long palpebral fissure; HP:0000601 Facial asymmetry not specific; HP:0000286 Epicanthus not established | (foster2020kosakiovergrowthsyndrome pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Scoliosis | Musculoskeletal | Reported in multiple patients; no pooled % in accessible texts | Often progressive; may occur with vertebral scalloping/widened spinal canal | HP:0002650 Scoliosis; HP:0000929 Abnormality of the vertebral column | (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Joint contractures / camptodactyly / joint stiffness | Musculoskeletal | Reported; frequency not available | Progressive flexion contractures and camptodactyly broadened phenotype in later series | HP:0001371 Flexion contracture; HP:0004209 Camptodactyly; HP:0001387 Joint stiffness | (foster2020kosakiovergrowthsyndrome pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4) |
| Intellectual disability / cognitive impairment | Neurodevelopmental | ~20% | Variable psychomotor and cognitive outcome; neurological deterioration is not universal | HP:0001249 Intellectual disability; HP:0001263 Global developmental delay | (foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4, foster2020kosakiovergrowthsyndrome pages 8-9) |
| Neurological deterioration / white matter disease progression | Neurologic | Variable; no pooled % | Progressive neurologic decline reported in some individuals, often alongside white matter abnormalities | HP:0002344 Progressive neurologic deterioration; HP:0002500 Cerebral white matter abnormality | (foster2020kosakiovergrowthsyndrome pages 1-2, minatogawa2017expansionofthe pages 1-2) |
| Hydrocephalus / ventriculomegaly | Neuroimaging structural abnormality | Reported; frequency not available | Includes obstructive ventriculomegaly/hydrocephalus, sometimes requiring shunting; may co-occur with Dandy-Walker variant | HP:0000238 Hydrocephalus; HP:0002119 Ventriculomegaly | (foster2020kosakiovergrowthsyndrome pages 2-4, minatogawa2017expansionofthe pages 1-2, foster2020kosakiovergrowthsyndrome pages 8-9) |
| Dandy-Walker malformation / variant | Neuroimaging structural abnormality | Reported; frequency not available | Part of posterior fossa malformation spectrum in some patients | HP:0001305 Dandy-Walker malformation | (foster2020kosakiovergrowthsyndrome pages 2-4, minatogawa2017expansionofthe pages 1-2, maurer2025knowingandtreating pages 2-2) |
| Infantile myofibromatosis / myofibroma | Tumor-like mesenchymal manifestation | ~33% | Infantile-onset myofibromas are part of the PDGFRB-associated spectrum and occur in a subset of KOGS patients | HP:0100014 Myofibroma / infantile myofibromatosis-related term if curated locally | (takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3) |
| Cardiac abnormalities | Cardiovascular | At least 2/6 patients in 2019 review | Reported defects include dilated sinus of Valsalva, mitral valve bowing, mild pulmonic stenosis with post-stenotic dilatation, and coronary artery aneurysm | HP:0001644 Dilatation of the aorta; HP:0001634 Mitral valve prolapse/bowing-related term; HP:0001642 Pulmonic stenosis; HP:0031639 Coronary artery aneurysm | (takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 4-5) |
| Cerebrovascular aneurysms / arterial dolichoectasia / tortuosity | Cardiovascular / neurovascular | Reported in multiple later cases; exact pooled prevalence not established | Basilar artery fusiform aneurysm, vertebrobasilar dolichoectasia, cervical/intracranial artery dysplasia and tortuosity; can cause stroke or fatal rupture | HP:0004942 Cerebral aneurysm; HP:0033650 Arterial tortuosity; HP:0100601 Dolichoectasia | (takenouchi2021progressivecerebraland pages 2-4, foster2020kosakiovergrowthsyndrome pages 1-2, foster2020kosakiovergrowthsyndrome pages 2-4, foster2020kosakiovergrowthsyndrome pages 8-9) |
| Stroke / thrombosis secondary to aneurysm | Neurovascular complication | Rare but severe; count not pooled | Ischaemic stroke from basilar artery aneurysm thrombosis and fatal rupture have been reported | HP:0001297 Stroke; HP:0004420 Arterial thrombosis | (foster2020kosakiovergrowthsyndrome pages 1-2, foster2020kosakiovergrowthsyndrome pages 2-4) |
| Prematurely aged / progeroid appearance | General / connective tissue | Progressive; frequency not pooled | Often linked to lipodystrophy and skin/connective-tissue changes; more apparent with age | HP:0007495 Prematurely aged appearance | (foster2020kosakiovergrowthsyndrome pages 1-2, maurer2025knowingandtreating pages 2-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Widely spaced teeth / delayed or abnormal dentition | Craniofacial / dental | Reported; frequency not available | Dental spacing and delayed eruption have been described in phenotype expansions | HP:0000687 Widely spaced teeth; HP:0000684 Delayed eruption of teeth | (foster2020kosakiovergrowthsyndrome pages 1-2, maurer2025knowingandtreating pages 2-2) |
| Carpal tunnel syndrome | Neuromuscular / peripheral nerve | Reported as novel association; frequency unknown | Pediatric CTS reported in at least one additional KOGS patient/family context | HP:0001382 Carpal tunnel syndrome | (foster2020kosakiovergrowthsyndrome pages 1-2) |


*Table: This table summarizes the reported clinical and imaging features of Kosaki overgrowth syndrome, including approximate frequencies where available from small case series and reviews. It also suggests HPO mappings to support structured disease-knowledge-base annotation.*

### Key phenotype frequencies / statistics (from small cohorts)
From Takenouchi et al. (2019) synthesis of the early cohort:
- **Periventricular white matter signal abnormalities:** **100%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4)
- **Posterior fossa arachnoid cysts/anomalies:** **~83%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4)
- **Lipodystrophy:** **~83%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4)
- **Craniosynostosis:** **~33%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4)
- **Intellectual disability (IQ < 70):** **~20%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4)
- **Infantile myofibromatosis/myofibromas:** **~33%** (takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3)
- **Cardiac abnormalities:** at least **2/6** early reported patients (takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 4-5)

### Vascular phenotype and real-world impact
Cerebrovascular complications have become central to current understanding. Foster et al. report “**fusiform aneurysm of the basilar artery**” with severe outcomes including thrombosis/stroke and fatal rupture, concluding that “**cerebrovascular complications are part of the phenotypic spectrum**” and that “**vascular imaging is indicated**” (foster2020kosakiovergrowthsyndrome pages 1-2). Longitudinal follow-up of the original patients demonstrated **progressive** basilar/vertebral and coronary arterial dilation and aneurysm evolution beginning in adolescence/early adulthood (takenouchi2021progressivecerebraland pages 2-4).

### Quality-of-life impact
In the broader PDGFRB activating-variant spectrum, imatinib therapy in one severe pediatric case was reported to improve multiple manifestations and “**most importantly significant improvement in quality of life**” (wenger2020activatingvariantsin pages 12-14). Although not exclusively KOGS, this informs real-world functional outcomes for PDGFRB-driven progressive connective-tissue disease.

---

## 4. Genetic / Molecular Information

### Causal gene
- **PDGFRB** (receptor tyrosine kinase) is the established causal gene (minatogawa2017expansionofthe pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 1-3).

### Pathogenic variant spectrum
Recurrent KOGS-associated variants described in multiple unrelated patients include:
- **PDGFRB c.1751C>G p.(Pro584Arg)** (minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3)
- **PDGFRB c.1696T>C p.(Trp566Arg)** (minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, takenouchi2019kosakiovergrowthsyndrome pages 1-3)

A later case series added a novel de novo variant:
- **PDGFRB c.1477A>T p.(Ser493Cys)** (foster2020kosakiovergrowthsyndrome pages 1-2, foster2020kosakiovergrowthsyndrome pages 2-4)

These are described as **activating / gain-of-function** and are interpreted as pathogenic/likely pathogenic in clinical genetics practice (minatogawa2017expansionofthe pages 1-2, foster2020kosakiovergrowthsyndrome pages 2-4).

### Inheritance pattern and mosaicism
KOGS is most often **autosomal dominant due to de novo heterozygous variants** in PDGFRB (minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4, foster2020kosakiovergrowthsyndrome pages 2-4). However, the broader PDGFRB activating-variant spectrum includes **variable expressivity**, **adult-onset manifestations**, and **mosaic** presentations (wenger2020activatingvariantsin pages 2-4, chenbhanich2021segmentalovergrowthand pages 1-2).

A key diagnostic lesson from mosaic PDGFRB vascular/overgrowth disease: blood exome may be negative; affected-tissue testing can reveal mosaic variants absent from blood (chenbhanich2021segmentalovergrowthand pages 1-2, chenbhanich2021segmentalovergrowthand pages 2-4).

### Modifier genes / epigenetics
No validated human modifier genes for KOGS were identified in the accessible corpus, but mechanistic work indicates **STAT1 acts as a major genetic modifier** of phenotypic direction (wasting vs overgrowth) in a PDGFRβ-activating mouse model (he2017stat1modulatestissue pages 8-9).

---

## 5. Environmental Information
No non-genetic environmental, lifestyle, or infectious contributors have been established for KOGS in the accessible literature.

---

## 6. Mechanism / Pathophysiology

### Current mechanistic understanding (causal chain)
1. **Trigger:** germline activating PDGFRB variant → ligand-independent PDGFRβ activation (maurer2025knowingandtreating pages 2-2, he2017stat1modulatestissue pages 2-3).
2. **Cellular signaling consequences:** downstream signaling varies by allele strength and context, including:
   - **STAT1 phosphorylation / interferon-like transcriptional programs** described as a general feature of PDGFRβ-activating mutations (he2017stat1modulatestissue pages 2-3, guerit2021pdgfreceptormutations pages 6-8).
   - **PI3K–AKT pathway activation** reported in at least one individual with KOGS and discussed as a mechanism for overgrowth/cardiovascular abnormalities (wenger2020activatingvariantsin pages 16-16, foster2020kosakiovergrowthsyndrome pages 10-11).
3. **Tissue-level outcomes:** dysregulated mesenchymal/perivascular signaling alters connective tissue and vascular integrity, plausibly driving:
   - **Skeletal overgrowth** (abnormal growth and bone remodeling)
   - **Skin hyperextensibility/fragility** (extracellular matrix remodeling)
   - **Lipodystrophy/progeroid features** (adipose progenitor differentiation shifts toward pro-fibrotic states)
   - **Pericyte/vascular smooth muscle dysfunction** → arterial ectasia/tortuosity → aneurysm risk (PDGFRB expression in pericytes and vascular smooth muscle is highlighted in the aneurysm/overgrowth mosaic report) (chenbhanich2021segmentalovergrowthand pages 2-4, guerit2021pdgfreceptormutations pages 8-9).

### Proposed ontology terms
- **GO (biological process):** receptor tyrosine kinase signaling; PI3K signaling; JAK-STAT signaling; extracellular matrix organization; regulation of vascular smooth muscle cell proliferation; pericyte development.
- **CL (cell types):** pericyte; vascular smooth muscle cell; fibroblast; mesenchymal progenitor cell (chenbhanich2021segmentalovergrowthand pages 2-4, guerit2021pdgfreceptormutations pages 8-9).
- **UBERON (anatomy):** cerebral arteries (basilar/vertebral); coronary arteries; white matter of cerebral hemispheres; posterior fossa.

### Recent developments (2023–2024 priority)
A 2024 overgrowth diagnostics review emphasizes that clinicians “**should consider molecular genetic testing as a first diagnostic step in overgrowth syndromes**” and highlights AI-assisted phenotype-driven approaches and deep sequencing for mosaicism detection (prawitt2024molecularmechanismsof pages 1-2, prawitt2024molecularmechanismsof pages 9-10). While not KOGS-specific, these methods are directly applicable to PDGFRB-related overgrowth, especially where mosaicism is suspected.

---

## 7. Anatomical Structures Affected

### Organ / system level
- **Musculoskeletal:** long bone overgrowth, scoliosis, contractures; craniosynostosis (takenouchi2019kosakiovergrowthsyndrome pages 3-4, gawlinski2018phenotypeexpansionand pages 1-4).
- **Skin/adipose/connective tissue:** hyperelastic fragile skin; progressive lipodystrophy (takenouchi2019kosakiovergrowthsyndrome pages 4-5, takenouchi2019kosakiovergrowthsyndrome pages 3-4).
- **Central nervous system:** periventricular white matter lesions; posterior fossa arachnoid cysts/protrusion; hydrocephalus/Dandy-Walker variant in some cases (takenouchi2019kosakiovergrowthsyndrome pages 3-4, minatogawa2017expansionofthe pages 1-2, foster2020kosakiovergrowthsyndrome pages 2-4).
- **Cardiovascular:** coronary aneurysms and other cardiac abnormalities; progressive cerebrovascular aneurysms/dolichoectasia (takenouchi2019kosakiovergrowthsyndrome pages 4-5, takenouchi2021progressivecerebraland pages 2-4, foster2020kosakiovergrowthsyndrome pages 1-2).

### Tissue/cell level (inferred from mechanistic/vascular reports)
- **Perivascular cells:** pericytes and vascular smooth muscle cells (chenbhanich2021segmentalovergrowthand pages 2-4).
- **Connective tissue fibroblasts/mesenchymal cells:** implicated by PDGFRβ biology and mouse models (he2017stat1modulatestissue pages 8-9).

---

## 8. Temporal Development

### Onset
KOGS is described primarily as **postnatal** skeletal overgrowth (foster2020kosakiovergrowthsyndrome pages 1-2, takenouchi2019kosakiovergrowthsyndrome pages 3-4).

### Progression
Multiple features are described as **progressive**, including progeroid appearance and vascular complications (foster2020kosakiovergrowthsyndrome pages 10-11). Serial imaging in original patients demonstrated progressive cerebrovascular and coronary artery dilation beginning in teenage years/early 20s (takenouchi2021progressivecerebraland pages 2-4).

---

## 9. Inheritance and Population

### Epidemiology
No robust prevalence/incidence estimates were identified in the accessible corpus. Available evidence supports that KOGS is **ultra-rare**.

### Case counts / rarity statistics (available)
- Foster et al. state KOGS was first described in 2015 and that “**to date, six patients have been reported**” prior to their three additional cases (foster2020kosakiovergrowthsyndrome pages 1-2).
- A collaborative consortium document summarizes that published case reports comprise “**around 10**” to “**about 15**” patients worldwide (maurer2025knowingandtreating pages 2-2).

### Inheritance nuances
- Predominantly **de novo autosomal dominant** (minatogawa2017expansionofthe pages 1-2, gawlinski2018phenotypeexpansionand pages 1-4).
- **Mosaicism** can produce related segmental overgrowth/aneurysm phenotypes and can require tissue testing (chenbhanich2021segmentalovergrowthand pages 1-2, chenbhanich2021segmentalovergrowthand pages 2-4).

Penetrance cannot be reliably estimated due to the very small number of described individuals.

---

## 10. Diagnostics

### Clinical recognition
A key diagnostic gestalt is the constellation of skeletal overgrowth + characteristic skin/connective-tissue features + CNS white matter lesions/posterior fossa findings; Takenouchi et al. state that this phenotype “**should prompt genetic analysis of the PDGFRB**” (takenouchi2019kosakiovergrowthsyndrome pages 1-3).

### Genetic testing approaches used in reported cases
- **Exome sequencing**, **targeted overgrowth panel**, and **whole-genome sequencing** have all been used to identify PDGFRB variants in KOGS (foster2020kosakiovergrowthsyndrome pages 2-4).
- **Sanger confirmation** and **parental testing** used to establish de novo status (foster2020kosakiovergrowthsyndrome pages 2-4).
- For suspected mosaic vascular/segmental disease: authors advise “**Germline and/or somatic testing for PDGFRB gene should be obtained**” and document cases where blood exome was not diagnostic but tissue testing was (chenbhanich2021segmentalovergrowthand pages 1-2, chenbhanich2021segmentalovergrowthand pages 2-4).

### Imaging and monitoring at/after diagnosis
- Foster et al. recommend baseline vascular screening: “**baseline vascular screening with echocardiogram, cerebral MRI and angioMRI**… at diagnosis and again in adult life” (foster2020kosakiovergrowthsyndrome pages 10-11).
- Wenger et al. recommend MRA at diagnosis and intermittently and broader vascular screening (brain/neck/chest/abdomen/pelvis) in the PDGFRB activating-variant spectrum, motivated by aneurysm risk (wenger2020activatingvariantsin pages 14-15).

### Differential diagnosis
- Shprintzen–Goldberg syndrome and atypical Ehlers–Danlos syndrome were considered clinically in one KOGS case before genetic diagnosis (foster2020kosakiovergrowthsyndrome pages 2-4).
- Other overgrowth differentials in broader workups include Sotos, Weaver, and Beckwith–Wiedemann spectrum (kamien2018aclinicalreview pages 8-11).
- Other PDGFRB-related differentials: Penttinen syndrome, infantile myofibromatosis, and idiopathic basal ganglia calcification (takenouchi2019kosakiovergrowthsyndrome pages 1-3, minatogawa2017expansionofthe pages 1-2).

---

## 11. Outcome / Prognosis

Long-term outcome is incompletely defined due to rarity, but major morbidity and mortality contributors are increasingly recognized as **progressive vascular aneurysms**.

- Foster et al. document thrombotic stroke and fatal rupture, emphasizing serious cerebrovascular risk (foster2020kosakiovergrowthsyndrome pages 1-2).
- In the original patients, progressive basilar/vertebral and coronary dilation could lead to fatal complications even with interventions (takenouchi2021progressivecerebraland pages 2-4).

---

## 12. Treatment

### Targeted therapies (precision medicine)
Evidence supports PDGFRB activating disorders as kinase-dependent and potentially responsive to TKIs:
- Foster et al.: activating PDGFRB variants “**are responsive to imatinib… suggesting that individuals with KOGS might also be candidates for treatment with tyrosine kinase inhibitors**” (foster2020kosakiovergrowthsyndrome pages 10-11).
- Wenger et al. report “robust and rapid” clinical responses to **imatinib** in several PDGFRB-activating cases; one severe case improved contractures and “significant improvement in quality of life” (wenger2020activatingvariantsin pages 12-14, wenger2020activatingvariantsin pages 2-4, wenger2020activatingvariantsin pages 14-15).
- Mosaic PDGFRB p.Tyr562Cys aneurysm/overgrowth disease included **sorafenib** exposure, but aneurysm progression and rupture still occurred (chenbhanich2021segmentalovergrowthand pages 2-4).

### Supportive/monitoring management
- **Vascular surveillance imaging** (echocardiogram + MRI/MRA; potentially whole-body arterial imaging) is repeatedly recommended given progressive aneurysm risk (foster2020kosakiovergrowthsyndrome pages 10-11, wenger2020activatingvariantsin pages 14-15, chenbhanich2021segmentalovergrowthand pages 1-2).
- **Optimal blood pressure control** is recommended to reduce vascular wall tension and potentially slow dilation (takenouchi2021progressivecerebraland pages 2-4, takenouchi2021progressivecerebraland pages 4-5).

### MAXO suggestions
Representative MAXO mappings are summarized in the management artifact.

| Domain | Recommendation / intervention | Details / evidence | Suggested MAXO term(s) | Citations |
|---|---|---|---|---|
| Genetic diagnostics | PDGFRB-focused testing when phenotype is suggestive | Characteristic combination of skeletal overgrowth, distinctive facial features, hyperelastic/fragile skin, and cerebral white matter lesions should prompt PDGFRB analysis; KOGS is caused by activating PDGFRB variants. | MAXO: genetic testing; MAXO: sequence analysis | (takenouchi2019kosakiovergrowthsyndrome pages 1-3, foster2020kosakiovergrowthsyndrome pages 1-2) |
| Genetic diagnostics | Whole-exome sequencing (WES) | WES was used diagnostically in reported KOGS cases and is recommended in overgrowth workups where phenotype overlaps multiple syndromes; useful for detecting heterozygous de novo PDGFRB variants. | MAXO: exome sequencing | (foster2020kosakiovergrowthsyndrome pages 2-4, kamien2018aclinicalreview pages 8-11, prawitt2024molecularmechanismsof pages 1-2) |
| Genetic diagnostics | Whole-genome sequencing (WGS) | WGS identified PDGFRB variants in KOGS cohorts; broader overgrowth reviews recommend molecular genetic testing early and support WGS when it improves diagnostic yield. | MAXO: genome sequencing | (foster2020kosakiovergrowthsyndrome pages 2-4, prawitt2024molecularmechanismsof pages 9-10, prawitt2024molecularmechanismsof pages 1-2) |
| Genetic diagnostics | Targeted multigene overgrowth panel | Custom NGS panels including overgrowth genes were successfully used in KOGS; panel/exome approaches are favored because differential diagnosis includes Sotos, Weaver, Beckwith-Wiedemann spectrum, Shprintzen-Goldberg, atypical EDS, Penttinen syndrome, and infantile myofibromatosis. | MAXO: multigene panel testing | (foster2020kosakiovergrowthsyndrome pages 2-4, kamien2018aclinicalreview pages 8-11, foster2020kosakiovergrowthsyndrome pages 10-11) |
| Genetic diagnostics | Sanger confirmation and parental testing | Reported variants were confirmed by bidirectional Sanger sequencing, with parental testing demonstrating de novo occurrence in multiple patients. | MAXO: confirmatory genetic testing | (foster2020kosakiovergrowthsyndrome pages 2-4, foster2020kosakiovergrowthsyndrome pages 1-2) |
| Mosaicism workup | Somatic testing of affected tissue when blood testing is negative | In mosaic PDGFRB disease, blood exome sequencing may be non-diagnostic; affected skin/biopsy tissue testing detected pathogenic variants absent from blood. This is relevant for segmental overgrowth/vascular phenotypes within the PDGFRB activating spectrum. | MAXO: biopsy-based molecular testing | (chenbhanich2021segmentalovergrowthand pages 1-2, chenbhanich2021segmentalovergrowthand pages 2-4) |
| Imaging at diagnosis | Brain MRI | Used to detect white matter lesions, ventriculomegaly/hydrocephalus, posterior fossa arachnoid cysts, Dandy-Walker malformation, and other structural brain abnormalities in KOGS. | MAXO: magnetic resonance imaging | (foster2020kosakiovergrowthsyndrome pages 2-4, takenouchi2019kosakiovergrowthsyndrome pages 3-4) |
| Imaging at diagnosis | Cerebral MR angiography / angioMRI | Recommended because cerebrovascular complications, including basilar artery fusiform aneurysms and dolichoectasia, are part of the KOGS spectrum. Suggested at diagnosis and again in adult life. | MAXO: magnetic resonance angiography | (foster2020kosakiovergrowthsyndrome pages 10-11) |
| Imaging surveillance | Serial neurovascular imaging | Repeat imaging is advised because aneurysms can be progressive and life-threatening; in mosaic/vascular PDGFRB disease, repeating imaging within 6–12 months after detection was considered reasonable. | MAXO: longitudinal imaging surveillance | (takenouchi2021progressivecerebraland pages 2-4, chenbhanich2021segmentalovergrowthand pages 1-2, wenger2020activatingvariantsin pages 14-15) |
| Cardiovascular evaluation | Echocardiography | Recommended for baseline vascular/cardiac screening; coronary aneurysms and other cardiac abnormalities have been reported in KOGS and broader PDGFRB activating variant spectrum. | MAXO: echocardiography | (foster2020kosakiovergrowthsyndrome pages 10-11, takenouchi2019kosakiovergrowthsyndrome pages 3-4, takenouchi2019kosakiovergrowthsyndrome pages 4-5) |
| Systemic vascular screening | Whole-body arterial tree imaging | Recommended after diagnosis in PDGFRB activating variant-related phenotypes to assess cervico-encephalic, coronary, and other arterial aneurysms/ectasia; MRA/CTA of brain, neck, chest, abdomen, and pelvis has been proposed. | MAXO: vascular imaging; MAXO: whole-body imaging | (chenbhanich2021segmentalovergrowthand pages 1-2, chenbhanich2021segmentalovergrowthand pages 2-4, wenger2020activatingvariantsin pages 14-15) |
| Risk reduction | Optimal blood pressure control | Suggested to reduce vascular wall tension and potentially slow progression of arterial dilation/aneurysms; specifically recommended once vascular risk in KOGS became apparent. | MAXO: blood pressure management; MAXO: antihypertensive therapy | (takenouchi2021progressivecerebraland pages 2-4, takenouchi2021progressivecerebraland pages 4-5) |
| Targeted therapy | Imatinib | Strongest therapeutic evidence in PDGFRB activating variant spectrum: rapid/robust responses reported in three children, including improvement in myofibromas and one severe progressive phenotype with improved joint contractures, coarse facial features, midfoot circumference, and quality of life. KOGS-specific literature suggests patients may be candidates for TKIs. | MAXO: tyrosine kinase inhibitor therapy; MAXO: imatinib administration | (wenger2020activatingvariantsin pages 12-14, wenger2020activatingvariantsin pages 2-4, wenger2020activatingvariantsin pages 14-15, foster2020kosakiovergrowthsyndrome pages 10-11) |
| Targeted therapy | Sunitinib / related TKIs | In vitro PDGFRB mutants were reported as sensitive to tyrosine kinase inhibitors including sunitinib; clinical-spectrum reviews cite experience with imatinib and sunitinib as supporting kinase-dependent disease, but direct KOGS-specific outcome data are limited. | MAXO: tyrosine kinase inhibitor therapy; MAXO: sunitinib administration | (wenger2020activatingvariantsin pages 12-14, wenger2020activatingvariantsin pages 14-15, wenger2020activatingvariantsin pages 16-16) |
| Targeted therapy | Sorafenib | Used in a patient with mosaic PDGFRB p.Tyr562Cys-associated overgrowth/aneurysms, but no clear clinical benefit was established and aneurysm progression/rupture still occurred; consortium reports also mention sorafenib exposure in PDGFRB-related disease. | MAXO: tyrosine kinase inhibitor therapy; MAXO: sorafenib administration | (chenbhanich2021segmentalovergrowthand pages 2-4, maurer2025knowingandtreating pages 2-2) |
| Treatment selection | Consider in vitro drug-sensitivity studies on patient fibroblasts | Emerging consortium recommendation: fibroblast testing may help determine which TKI most effectively blocks PDGFRB signaling for a given patient, especially because response appears variable. | MAXO: functional assay-guided treatment selection | (maurer2025knowingandtreating pages 2-2, maurer2025knowingandtreating pages 4-5) |
| Supportive monitoring | Assess treatment efficacy, safety, QoL, and symptom burden longitudinally | Observational study NCT05953857 is designed to track symptom burden, quality of life, TKI efficacy, and safety over long-term follow-up in KOGS/Penttinen syndrome due to activating PDGFRB variants. | MAXO: longitudinal clinical monitoring; MAXO: adverse event monitoring; MAXO: quality of life assessment | (NCT05953857 chunk 1, maurer2025knowingandtreating pages 5-6) |
| Clinical research | Enroll in observational registry / natural history study | IKKoPeS (NCT05953857) is a multicenter observational study for treated and untreated KOGS/Penttinen patients with activating PDGFRB variants; estimated enrollment 30, first posted 2023-07-20. | MAXO: clinical trial enrollment; MAXO: registry enrollment | (NCT05953857 chunk 1) |


*Table: This table summarizes currently reported diagnostic strategies, vascular surveillance approaches, and targeted management options for Kosaki overgrowth syndrome and the broader PDGFRB activating variant spectrum. It highlights where evidence is strongest, especially for imaging surveillance and tyrosine kinase inhibitor use.*

### Clinical trials / real-world implementations
**ClinicalTrials.gov NCT05953857** (“Knowing and Treating Kosaki/Penttinen Syndromes”, IKKoPeS) is a **prospective observational** study designed to follow treated and untreated patients with activating PDGFRB variants and to assess whether TKIs “could bring clinical benefit” (first posted **2023-07-20**, estimated start **2023-10**, estimated enrollment **30**; estimated completion **2048-10**) (NCT05953857 chunk 1). Primary/secondary outcomes include symptom burden and the proportion with QoL improvement or side effects under TKI (NCT05953857 chunk 1).

URL: https://clinicaltrials.gov/study/NCT05953857 (registry details summarized from record) (NCT05953857 chunk 1).

---

## 13. Prevention
Primary prevention is not applicable for a de novo genetic disorder. However, **secondary/tertiary prevention** is clinically relevant:
- **Genetic counseling** for recurrence risk (typically low for de novo, but consider parental mosaicism in principle).
- **Surveillance to prevent complications:** early vascular screening and repeat imaging to detect aneurysms before rupture/thrombosis (foster2020kosakiovergrowthsyndrome pages 10-11, takenouchi2021progressivecerebraland pages 2-4).

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary analogs of KOGS were identified in the accessible corpus.

---

## 15. Model Organisms
A key mechanistic model is the **Pdgfrb gain-of-function mouse** (e.g., Pdgfrb D849V). STAT1 acts as a modifier that can shift phenotype between autoinflammatory wasting and progressive overgrowth, mapping conceptually onto the Penttinen vs Kosaki phenotypic axis and supporting PDGFRB hyperactivity as a driver mechanism (he2017stat1modulatestissue pages 8-9, he2017stat1modulatestissue pages 2-3).

---

## 2023–2024 “Latest research” highlights (highest relevance within accessible corpus)
- **Overgrowth diagnostics modernization (2024):** increased emphasis on early genomic testing (WES/WGS and deep sequencing for mosaicism) and the integration of AI-supported phenotype-to-genotype workflows in overgrowth disorders (prawitt2024molecularmechanismsof pages 1-2, prawitt2024molecularmechanismsof pages 9-10).
- **Real-world longitudinal research infrastructure (2023):** formal long-term observational study registration for KOGS/Penttinen syndromes focused on TKI benefit/risk and symptom burden (NCT05953857; first posted 2023-07-20) (NCT05953857 chunk 1).

---

## Key evidence quotes (for knowledge-base evidence items)
- Vascular surveillance recommendation: “**we suggest that clinicians consider baseline vascular screening with echocardiogram, cerebral MRI and angioMRI for individuals with KOGS at diagnosis and again in adult life**” (foster2020kosakiovergrowthsyndrome pages 10-11).
- KOGS vascular phenotype conclusion: “**cerebrovascular complications are part of the phenotypic spectrum**” and “**vascular imaging is indicated**” (foster2020kosakiovergrowthsyndrome pages 1-2).
- Genotype–phenotype contrast: “**hypermorphic mutations in PDGFRB lead to Kosaki overgrowth syndrome… whereas hypomorphic mutations lead to idiopathic basal ganglia calcification**” (minatogawa2017expansionofthe pages 1-2).
- Spectrum/QoL under targeted therapy: imatinib improved disease manifestations and “**most importantly significant improvement in quality of life**” in a severe PDGFRB-activating case (wenger2020activatingvariantsin pages 12-14).

---

## Notes on gaps / limitations of this report
- Several identifiers (Orphanet, MeSH, ICD-10/ICD-11) and population prevalence/incidence estimates were not retrievable from the currently accessible full-text corpus and are therefore not asserted here.
- Published evidence is largely case-based; frequencies and prognostic estimates are based on small numbers and may change as registries (e.g., NCT05953857) mature.


References

1. (OpenTargets Search: Kosaki overgrowth syndrome): Open Targets Query (Kosaki overgrowth syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (foster2020kosakiovergrowthsyndrome pages 1-2): Alison Foster, Basile Chalot, Thalia Antoniadi, Elise Schaefer, Rebecca Keelagher, Gavin Ryan, Quentin Thomas, Christophe Philippe, Ange‐Line Bruel, Arthur Sorlin, Christel Thauvin‐Robinet, Marc Bardou, Maxime Luu, Veronique Quenardelle, Valerie Wolff, Jessica Woodley, Pierre Vabres, Derek Lim, Rebecca Igbokwe, Annie Joseph, Harriet Walker, Andrea Jester, Jonathan Ellenbogen, Diana Johnson, Bethanie Rooke, Celia Moss, Trevor Cole, and Laurence Faivre. Kosaki overgrowth syndrome: a novel pathogenic variant in <scp><i>pdgfrb</i></scp> and expansion of the phenotype including cerebrovascular complications. Clinical Genetics, 98:19-31, May 2020. URL: https://doi.org/10.1111/cge.13752, doi:10.1111/cge.13752. This article has 31 citations and is from a peer-reviewed journal.

3. (minatogawa2017expansionofthe pages 1-2): Mari Minatogawa, Toshiki Takenouchi, Yu Tsuyusaki, Fuminori Iwasaki, Tomoko Uehara, Kenji Kurosawa, Kenjiro Kosaki, and Cynthia J. Curry. Expansion of the phenotype of kosaki overgrowth syndrome. American Journal of Medical Genetics Part A, 173:2422-2427, Jun 2017. URL: https://doi.org/10.1002/ajmg.a.38310, doi:10.1002/ajmg.a.38310. This article has 45 citations.

4. (gawlinski2018phenotypeexpansionand pages 1-4): Paweł Gawliński, M. Pelc, E. Ciara, S. Jhangiani, Elżbieta Jurkiewicz, Tomasz Gambin, Tomasz Gambin, Agnieszka Różdżyńska-Świątkowska, M. Dawidziuk, Z. Coban-Akdemir, D. L. Guilbride, D. Muzny, J. R. Lupski, J. R. Lupski, and M. Krajewska-Walasek. Phenotype expansion and development in kosaki overgrowth syndrome. Clinical Genetics, 93:919-924, Apr 2018. URL: https://doi.org/10.1111/cge.13192, doi:10.1111/cge.13192. This article has 31 citations and is from a peer-reviewed journal.

5. (takenouchi2019kosakiovergrowthsyndrome pages 1-3): Toshiki Takenouchi, Hironobu Okuno, and Kenjiro Kosaki. Kosaki overgrowth syndrome: a newly identified entity caused by pathogenic variants in platelet‐derived growth factor receptor‐beta. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 181:650-657, Nov 2019. URL: https://doi.org/10.1002/ajmg.c.31755, doi:10.1002/ajmg.c.31755. This article has 19 citations.

6. (takenouchi2021progressivecerebraland pages 4-5): Toshiki Takenouchi, Kazuki Kodo, Fumito Yamazaki, Hirofumi Nakatomi, and Kenjiro Kosaki. Progressive cerebral and coronary aneurysms in the original two patients with kosaki overgrowth syndrome. American Journal of Medical Genetics Part A, 185:1003-999, Dec 2021. URL: https://doi.org/10.1002/ajmg.a.62027, doi:10.1002/ajmg.a.62027. This article has 6 citations.

7. (wenger2020activatingvariantsin pages 2-4): Tara L. Wenger, Randall A. Bly, Natalie Wu, Catherine M. Albert, Julie Park, Joseph Shieh, Jirat Chenbhanich, Carrie L. Heike, Margaret P. Adam, Irene Chang, Angela Sun, Danny E. Miller, Anita E. Beck, Deepti Gupta, Markus D. Boos, Elaine H. Zackai, David Everman, Shireen Ganapathi, Meredith Wilson, John Christodoulou, Yuri A. Zarate, Cynthia Curry, Dong Li, Anne Guimier, Jeanne Amiel, Hakon Hakonarson, Richard Webster, Elizabeth J. Bhoj, Jonathan A. Perkins, John P. Dahl, and William B. Dobyns. Activating variants in pdgfrb result in a spectrum of disorders responsive to imatinib monotherapy. American Journal of Medical Genetics Part A, 182:1576-1591, Jun 2020. URL: https://doi.org/10.1002/ajmg.a.61615, doi:10.1002/ajmg.a.61615. This article has 37 citations.

8. (wenger2020activatingvariantsin pages 14-15): Tara L. Wenger, Randall A. Bly, Natalie Wu, Catherine M. Albert, Julie Park, Joseph Shieh, Jirat Chenbhanich, Carrie L. Heike, Margaret P. Adam, Irene Chang, Angela Sun, Danny E. Miller, Anita E. Beck, Deepti Gupta, Markus D. Boos, Elaine H. Zackai, David Everman, Shireen Ganapathi, Meredith Wilson, John Christodoulou, Yuri A. Zarate, Cynthia Curry, Dong Li, Anne Guimier, Jeanne Amiel, Hakon Hakonarson, Richard Webster, Elizabeth J. Bhoj, Jonathan A. Perkins, John P. Dahl, and William B. Dobyns. Activating variants in pdgfrb result in a spectrum of disorders responsive to imatinib monotherapy. American Journal of Medical Genetics Part A, 182:1576-1591, Jun 2020. URL: https://doi.org/10.1002/ajmg.a.61615, doi:10.1002/ajmg.a.61615. This article has 37 citations.

9. (takenouchi2021progressivecerebraland pages 2-4): Toshiki Takenouchi, Kazuki Kodo, Fumito Yamazaki, Hirofumi Nakatomi, and Kenjiro Kosaki. Progressive cerebral and coronary aneurysms in the original two patients with kosaki overgrowth syndrome. American Journal of Medical Genetics Part A, 185:1003-999, Dec 2021. URL: https://doi.org/10.1002/ajmg.a.62027, doi:10.1002/ajmg.a.62027. This article has 6 citations.

10. (takenouchi2019kosakiovergrowthsyndrome pages 3-4): Toshiki Takenouchi, Hironobu Okuno, and Kenjiro Kosaki. Kosaki overgrowth syndrome: a newly identified entity caused by pathogenic variants in platelet‐derived growth factor receptor‐beta. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 181:650-657, Nov 2019. URL: https://doi.org/10.1002/ajmg.c.31755, doi:10.1002/ajmg.c.31755. This article has 19 citations.

11. (foster2020kosakiovergrowthsyndrome pages 10-11): Alison Foster, Basile Chalot, Thalia Antoniadi, Elise Schaefer, Rebecca Keelagher, Gavin Ryan, Quentin Thomas, Christophe Philippe, Ange‐Line Bruel, Arthur Sorlin, Christel Thauvin‐Robinet, Marc Bardou, Maxime Luu, Veronique Quenardelle, Valerie Wolff, Jessica Woodley, Pierre Vabres, Derek Lim, Rebecca Igbokwe, Annie Joseph, Harriet Walker, Andrea Jester, Jonathan Ellenbogen, Diana Johnson, Bethanie Rooke, Celia Moss, Trevor Cole, and Laurence Faivre. Kosaki overgrowth syndrome: a novel pathogenic variant in <scp><i>pdgfrb</i></scp> and expansion of the phenotype including cerebrovascular complications. Clinical Genetics, 98:19-31, May 2020. URL: https://doi.org/10.1111/cge.13752, doi:10.1111/cge.13752. This article has 31 citations and is from a peer-reviewed journal.

12. (takenouchi2019kosakiovergrowthsyndrome pages 4-5): Toshiki Takenouchi, Hironobu Okuno, and Kenjiro Kosaki. Kosaki overgrowth syndrome: a newly identified entity caused by pathogenic variants in platelet‐derived growth factor receptor‐beta. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 181:650-657, Nov 2019. URL: https://doi.org/10.1002/ajmg.c.31755, doi:10.1002/ajmg.c.31755. This article has 19 citations.

13. (foster2020kosakiovergrowthsyndrome pages 8-9): Alison Foster, Basile Chalot, Thalia Antoniadi, Elise Schaefer, Rebecca Keelagher, Gavin Ryan, Quentin Thomas, Christophe Philippe, Ange‐Line Bruel, Arthur Sorlin, Christel Thauvin‐Robinet, Marc Bardou, Maxime Luu, Veronique Quenardelle, Valerie Wolff, Jessica Woodley, Pierre Vabres, Derek Lim, Rebecca Igbokwe, Annie Joseph, Harriet Walker, Andrea Jester, Jonathan Ellenbogen, Diana Johnson, Bethanie Rooke, Celia Moss, Trevor Cole, and Laurence Faivre. Kosaki overgrowth syndrome: a novel pathogenic variant in <scp><i>pdgfrb</i></scp> and expansion of the phenotype including cerebrovascular complications. Clinical Genetics, 98:19-31, May 2020. URL: https://doi.org/10.1111/cge.13752, doi:10.1111/cge.13752. This article has 31 citations and is from a peer-reviewed journal.

14. (foster2020kosakiovergrowthsyndrome pages 2-4): Alison Foster, Basile Chalot, Thalia Antoniadi, Elise Schaefer, Rebecca Keelagher, Gavin Ryan, Quentin Thomas, Christophe Philippe, Ange‐Line Bruel, Arthur Sorlin, Christel Thauvin‐Robinet, Marc Bardou, Maxime Luu, Veronique Quenardelle, Valerie Wolff, Jessica Woodley, Pierre Vabres, Derek Lim, Rebecca Igbokwe, Annie Joseph, Harriet Walker, Andrea Jester, Jonathan Ellenbogen, Diana Johnson, Bethanie Rooke, Celia Moss, Trevor Cole, and Laurence Faivre. Kosaki overgrowth syndrome: a novel pathogenic variant in <scp><i>pdgfrb</i></scp> and expansion of the phenotype including cerebrovascular complications. Clinical Genetics, 98:19-31, May 2020. URL: https://doi.org/10.1111/cge.13752, doi:10.1111/cge.13752. This article has 31 citations and is from a peer-reviewed journal.

15. (maurer2025knowingandtreating pages 2-2): A Maurer, L Mirakovska, A Foster, and K Kosaki. 'knowing and treating kosaki/penttinen syndrome'international collaborative consortium: recommendations for follow-up, natural history and a real-life observational …. Unknown journal, 2025.

16. (wenger2020activatingvariantsin pages 12-14): Tara L. Wenger, Randall A. Bly, Natalie Wu, Catherine M. Albert, Julie Park, Joseph Shieh, Jirat Chenbhanich, Carrie L. Heike, Margaret P. Adam, Irene Chang, Angela Sun, Danny E. Miller, Anita E. Beck, Deepti Gupta, Markus D. Boos, Elaine H. Zackai, David Everman, Shireen Ganapathi, Meredith Wilson, John Christodoulou, Yuri A. Zarate, Cynthia Curry, Dong Li, Anne Guimier, Jeanne Amiel, Hakon Hakonarson, Richard Webster, Elizabeth J. Bhoj, Jonathan A. Perkins, John P. Dahl, and William B. Dobyns. Activating variants in pdgfrb result in a spectrum of disorders responsive to imatinib monotherapy. American Journal of Medical Genetics Part A, 182:1576-1591, Jun 2020. URL: https://doi.org/10.1002/ajmg.a.61615, doi:10.1002/ajmg.a.61615. This article has 37 citations.

17. (chenbhanich2021segmentalovergrowthand pages 1-2): Jirat Chenbhanich, Yan Hu, Steven Hetts, Daniel Cooke, Christopher Dowd, Patrick Devine, Bianca Russell, Sung Hae L. Kang, Vivian Y. Chang, Adib A. Abla, Patricia Cornett, Iwei Yeh, Hane Lee, Julian A. Martinez‐Agosto, Ilona J. Frieden, and Joseph T. Shieh. Segmental overgrowth and aneurysms due to mosaic pdgfrb p.(tyr562cys). American Journal of Medical Genetics Part A, 185:1430-1436, Mar 2021. URL: https://doi.org/10.1002/ajmg.a.62126, doi:10.1002/ajmg.a.62126. This article has 16 citations.

18. (chenbhanich2021segmentalovergrowthand pages 2-4): Jirat Chenbhanich, Yan Hu, Steven Hetts, Daniel Cooke, Christopher Dowd, Patrick Devine, Bianca Russell, Sung Hae L. Kang, Vivian Y. Chang, Adib A. Abla, Patricia Cornett, Iwei Yeh, Hane Lee, Julian A. Martinez‐Agosto, Ilona J. Frieden, and Joseph T. Shieh. Segmental overgrowth and aneurysms due to mosaic pdgfrb p.(tyr562cys). American Journal of Medical Genetics Part A, 185:1430-1436, Mar 2021. URL: https://doi.org/10.1002/ajmg.a.62126, doi:10.1002/ajmg.a.62126. This article has 16 citations.

19. (he2017stat1modulatestissue pages 8-9): Chaoyong He, Shayna C. Medley, Jang Kim, Chengyi Sun, Hae Ryong Kwon, Hiromi Sakashita, Yair Pincu, Longbiao Yao, Danielle Eppard, Bojie Dai, William L. Berry, Timothy M. Griffin, and Lorin E. Olson. Stat1 modulates tissue wasting or overgrowth downstream from pdgfrβ. Genes & Development, 31:1666-1678, Aug 2017. URL: https://doi.org/10.1101/gad.300384.117, doi:10.1101/gad.300384.117. This article has 47 citations and is from a highest quality peer-reviewed journal.

20. (he2017stat1modulatestissue pages 2-3): Chaoyong He, Shayna C. Medley, Jang Kim, Chengyi Sun, Hae Ryong Kwon, Hiromi Sakashita, Yair Pincu, Longbiao Yao, Danielle Eppard, Bojie Dai, William L. Berry, Timothy M. Griffin, and Lorin E. Olson. Stat1 modulates tissue wasting or overgrowth downstream from pdgfrβ. Genes & Development, 31:1666-1678, Aug 2017. URL: https://doi.org/10.1101/gad.300384.117, doi:10.1101/gad.300384.117. This article has 47 citations and is from a highest quality peer-reviewed journal.

21. (guerit2021pdgfreceptormutations pages 6-8): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 154 citations and is from a domain leading peer-reviewed journal.

22. (wenger2020activatingvariantsin pages 16-16): Tara L. Wenger, Randall A. Bly, Natalie Wu, Catherine M. Albert, Julie Park, Joseph Shieh, Jirat Chenbhanich, Carrie L. Heike, Margaret P. Adam, Irene Chang, Angela Sun, Danny E. Miller, Anita E. Beck, Deepti Gupta, Markus D. Boos, Elaine H. Zackai, David Everman, Shireen Ganapathi, Meredith Wilson, John Christodoulou, Yuri A. Zarate, Cynthia Curry, Dong Li, Anne Guimier, Jeanne Amiel, Hakon Hakonarson, Richard Webster, Elizabeth J. Bhoj, Jonathan A. Perkins, John P. Dahl, and William B. Dobyns. Activating variants in pdgfrb result in a spectrum of disorders responsive to imatinib monotherapy. American Journal of Medical Genetics Part A, 182:1576-1591, Jun 2020. URL: https://doi.org/10.1002/ajmg.a.61615, doi:10.1002/ajmg.a.61615. This article has 37 citations.

23. (guerit2021pdgfreceptormutations pages 8-9): Emilie Guérit, Florence Arts, Guillaume Dachy, Boutaina Boulouadnine, and Jean-Baptiste Demoulin. Pdgf receptor mutations in human diseases. Cellular and Molecular Life Sciences, 78:3867-3881, Jan 2021. URL: https://doi.org/10.1007/s00018-020-03753-y, doi:10.1007/s00018-020-03753-y. This article has 154 citations and is from a domain leading peer-reviewed journal.

24. (prawitt2024molecularmechanismsof pages 1-2): Dirk Prawitt and Thomas Eggermann. Molecular mechanisms of human overgrowth and use of omics in its diagnostics: chances and challenges. Frontiers in Genetics, Jun 2024. URL: https://doi.org/10.3389/fgene.2024.1382371, doi:10.3389/fgene.2024.1382371. This article has 5 citations and is from a peer-reviewed journal.

25. (prawitt2024molecularmechanismsof pages 9-10): Dirk Prawitt and Thomas Eggermann. Molecular mechanisms of human overgrowth and use of omics in its diagnostics: chances and challenges. Frontiers in Genetics, Jun 2024. URL: https://doi.org/10.3389/fgene.2024.1382371, doi:10.3389/fgene.2024.1382371. This article has 5 citations and is from a peer-reviewed journal.

26. (kamien2018aclinicalreview pages 8-11): Benjamin Kamien, Anne Ronan, Gemma Poke, Ingrid Sinnerbrink, Gareth Baynam, Michelle Ward, William T. Gibson, Tracy Dudding-Byth, and Rodney J. Scott. A clinical review of generalized overgrowth syndromes in the era of massively parallel sequencing. Molecular Syndromology, 9:70-82, Jan 2018. URL: https://doi.org/10.1159/000484532, doi:10.1159/000484532. This article has 56 citations and is from a peer-reviewed journal.

27. (maurer2025knowingandtreating pages 4-5): A Maurer, L Mirakovska, A Foster, and K Kosaki. 'knowing and treating kosaki/penttinen syndrome'international collaborative consortium: recommendations for follow-up, natural history and a real-life observational …. Unknown journal, 2025.

28. (NCT05953857 chunk 1):  Knowing and Treating Kosaki/Penttinen Syndromes. Centre Hospitalier Universitaire Dijon. 2023. ClinicalTrials.gov Identifier: NCT05953857

29. (maurer2025knowingandtreating pages 5-6): A Maurer, L Mirakovska, A Foster, and K Kosaki. 'knowing and treating kosaki/penttinen syndrome'international collaborative consortium: recommendations for follow-up, natural history and a real-life observational …. Unknown journal, 2025.
