---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T19:28:48.183932'
end_time: '2026-05-06T19:39:31.437236'
duration_seconds: 643.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cutaneous larva migrans
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cutaneous larva migrans
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Cutaneous larva migrans** covering all of the
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
- **Disease Name:** Cutaneous larva migrans
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Cutaneous larva migrans** covering all of the
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


# Cutaneous Larva Migrans (CLM) — Disease Characteristics Research Report

## 1. Disease information

### Overview / current definition
Cutaneous larva migrans (CLM) is a zoonotic, hookworm-related dermatosis caused by penetration of animal hookworm larvae and their subsequent superficial migration within human skin, producing intensely pruritic, slowly advancing, linear/serpiginous tracks (“creeping eruption”). (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)

A representative clinical image (serpiginous plaque) and histopathologic confirmation (organism in stratum corneum with eosinophil-rich infiltrate) are shown in the 2023 Dermatology Online Journal report. (johanis2023cutaneouslarvamigrans media 1be38c9c, johanis2023cutaneouslarvamigrans media a6ff90a3)

### Synonyms / alternative names
Synonyms used in the clinical/review literature include: hookworm-related cutaneous larva migrans (HrCLM), creeping eruption, zoonotic hookworm infection, serpiginous linear dermatitis, ground itch, sandworm, and plumber’s itch. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3)

### Key identifiers (ontology/coding)
* **MeSH:** “Cutaneous Larva Migrans” / “Larva Migrans, Cutaneous” is used as an indexed subject term in the biomedical literature; however, the **MeSH ID** was not present in the retrieved full-text snippets. (guarda2026importedcutaneouslarva pages 4-7)
* **ICD-10/ICD-11:** A CLM-specific ICD code was not explicitly stated in the CLM-focused papers retrieved here; several sources refer generally to use of ICD groupings/codes in datasets, but without giving a CLM code. (shrestha2024cutaneouslarvamigrans pages 1-2)
* **MONDO:** A MONDO ID was **not found in the retrieved evidence**.

### Evidence source type
The evidence retrieved here is primarily **aggregated disease-level reviews**, **case reports**, and **case series/outbreak investigations** in humans (travel medicine, dermatology), with supporting epidemiologic and quality-of-life cohort studies. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, hasni2024cutaneouslarvamigrans pages 2-6, schuster2011lifequalityimpairment pages 1-2)

| Category | Details (concise) | Key sources (with DOI/URL + year) |
|---|---|---|
| Definition / synonyms | Zoonotic, hookworm-related dermatosis caused by intraepidermal migration of non-human hookworm larvae, producing intensely pruritic, linear/serpiginous “creeping” tracks. Synonyms reported in the evidence: hookworm-related cutaneous larva migrans (HrCLM), creeping eruption, zoonotic hookworm infection, serpiginous linear dermatitis, ground itch, sandworm, plumber’s itch. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3) | Rodriguez-Morales et al., 2021, https://doi.org/10.1007/s40475-021-00239-0 |
| Key identifiers | MeSH term name appears in indexed literature as “Cutaneous Larva Migrans” / “Larva Migrans, Cutaneous” (term name evidenced, numeric ID not found in provided evidence). ICD-10/11 specific code not directly given for CLM in the provided disease-focused sources; broader helminthiasis coding context only. MONDO ID: not found in evidence. (guarda2026importedcutaneouslarva pages 4-7, shrestha2024cutaneouslarvamigrans pages 1-2) | Guarda et al., 2026, https://doi.org/10.7759/cureus.104834; Shrestha et al., 2024, https://doi.org/10.1097/ms9.0000000000001512 |
| Main causal organisms | Most commonly Ancylostoma braziliense; also Ancylostoma caninum, Ancylostoma ceylanicum, and Uncinaria stenocephala are implicated. Humans are accidental/dead-end hosts; larvae generally do not mature in the intestine. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, currie2025cutaneouslarvamigrans pages 6-7, elmi2025cutaneouslarvamigrans pages 1-3) | Rodriguez-Morales et al., 2021, https://doi.org/10.1007/s40475-021-00239-0; Currie et al., 2025, https://doi.org/10.3390/tropicalmed10060163 |
| Typical exposure / risk factors | Barefoot walking or lying on contaminated sand/soil, especially beaches and sandboxes; contact with dog/cat feces or untreated pets; muddy/wet soil exposure; travel to tropical/subtropical regions; some occupational exposures (farming, gardening, animal handling). Pediatric risk is prominent in some recent series. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, hasni2024cutaneouslarvamigrans pages 2-6, shrestha2024cutaneouslarvamigrans pages 1-2, johanis2023cutaneouslarvamigrans pages 1-3) | Rodriguez-Morales et al., 2021, https://doi.org/10.1007/s40475-021-00239-0; Hasni et al., 2024, https://doi.org/10.5001/omj.2028.07; Shrestha et al., 2024, https://doi.org/10.1097/ms9.0000000000001512; Johanis et al., 2023, https://doi.org/10.5070/d329461906 |
| First-line treatments / example dosing | Oral ivermectin is generally preferred first-line: single dose 150–200 µg/kg (adult example 12 mg), repeat if needed. Albendazole is an effective alternative: 400 mg/day for 3–7 days; some reports/series recommend 400 mg once daily for 5 days or 400 mg/day for 1 week. Topical 10% albendazole is an option when oral therapy is contraindicated (e.g., very small children). Cryotherapy is not recommended. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, johanis2023cutaneouslarvamigrans pages 3-5, hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7) | Hochedez & Caumes, 2007, https://doi.org/10.1111/j.1708-8305.2007.00148.x; Johanis et al., 2023, https://doi.org/10.5070/d329461906; Hasni et al., 2024, https://doi.org/10.5001/omj.2028.07 |
| Key 2023–2024 developments | 2024 Oman urban outbreak/case series linked cases to heavy rainfall, puddles/mud, and recommended surveillance plus municipal/agricultural collaboration; 7/9 cases (78%) were pediatric. 2023 northeastern US case highlighted possible geographic expansion beyond classic tropical zones and climate-linked spread. 2024 Nepal pediatric review emphasized neglected burden, footwear/pet deworming prevention, and pediatric treatment guidance. 2024 Sudan report described successful combination albendazole + ivermectin in 2 cases amid concern about emerging anthelmintic resistance. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7, johanis2023cutaneouslarvamigrans pages 1-3, shrestha2024cutaneouslarvamigrans pages 3-4, currie2025cutaneouslarvamigrans pages 13-13) | Hasni et al., 2024, https://doi.org/10.5001/omj.2028.07; Johanis et al., 2023, https://doi.org/10.5070/d329461906; Shrestha et al., 2024, https://doi.org/10.1097/ms9.0000000000001512; Shamad et al., 2024, https://doi.org/10.7759/cureus.64665 |


*Table: This compact table summarizes the most actionable disease-characteristics evidence for cutaneous larva migrans, including definition, likely identifiers, causes, exposures, treatment, and recent 2023–2024 developments. It is designed for quick knowledge-base population and citation tracing.*

## 2. Etiology

### Primary causal factors (infectious)
CLM is most often attributed to zoonotic hookworms of dogs/cats. Reviews emphasize **Ancylostoma braziliense** as a principal cause, with other implicated species including **Ancylostoma caninum** and **Uncinaria stenocephala**. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, elmi2025cutaneouslarvamigrans pages 1-3, currie2025cutaneouslarvamigrans pages 6-7)

Humans are accidental/dead-end hosts; larvae generally do not mature to adult intestinal worms in humans. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3)

### Risk factors
Commonly supported risks include:
* **Bare-skin contact with contaminated sand/soil**, especially **beaches** and sandboxes (walking barefoot, sitting/lying on sand). (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)
* **Exposure to dog/cat feces or untreated pets** (domestic or stray), especially in resource-poor settings. (shrestha2024cutaneouslarvamigrans pages 1-2, johanis2023cutaneouslarvamigrans pages 1-3)
* **Occupational soil exposure** (e.g., farming, gardening, animal handling). (elmi2025cutaneouslarvamigrans pages 1-3, hasni2024cutaneouslarvamigrans pages 2-6)
* **Climate/environmental events**: a 2024 Oman case series reported a cluster occurring “mainly after periods of rainfall” and noted recent contact with “water puddles or mud” across cases, supporting a role for unusual wet conditions facilitating larval survival/exposure. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7)

### Protective factors
Direct, empirically quantified protective factors were not provided in the retrieved primary studies. Prevention recommendations (Section 13) imply protective effects of **consistent footwear** and avoidance of direct contact with contaminated sand/soil. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, shrestha2024cutaneouslarvamigrans pages 1-2)

### Genetic risk / protective factors; gene–environment interactions
CLM is not a genetic disease; **no causal human genes/variants** or gene–environment interaction studies were present in the retrieved evidence.

## 3. Phenotypes (clinical presentation)

### Core clinical phenotypes
The typical presentation is a **pruritic, erythematous, linear/serpiginous track** that migrates to adjacent skin over time. (johanis2023cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)

A 2023 abstract states CLM is “characterized by erythematous, twisting, and linear plaques that can migrate to adjacent skin.” (johanis2023cutaneouslarvamigrans pages 1-3)

Common sites reflect exposure (feet/ankles; sometimes thighs/buttocks). (guarda2026importedcutaneouslarva pages 4-7, johanis2023cutaneouslarvamigrans pages 1-3)

### Complications / atypical features
Complications described across recent and foundational sources include:
* **Secondary bacterial infection** due to excoriation/scratching. (guarda2026importedcutaneouslarva pages 4-7, shrestha2024cutaneouslarvamigrans pages 3-4)
* **Vesiculobullous lesions** and **folliculitis** (including “hookworm folliculitis”/follicular CLM). (johanis2023cutaneouslarvamigrans pages 1-3, hochedez2007hookwormrelatedcutaneouslarva pages 4-6)
* Rare systemic manifestations such as **Löffler syndrome** are mentioned as exceptional. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, hasni2024cutaneouslarvamigrans pages 6-7)

Shrestha et al. (2024) summarizes that routine investigations are often normal and that complications can include secondary bacterial infection, allergy, and rare internal migration; the abstract explicitly notes the lesion was initially misdiagnosed as fungal infection and later became “intensely pruritic.” (shrestha2024cutaneouslarvamigrans pages 1-2)

### Onset, severity, progression
CLM is often **subacute** after exposure, with lesions migrating over days to weeks; the condition is generally **self-limited**, with larvae dying after several weeks if untreated (reported as ~5–6 weeks in a 2024 review/case report). (shrestha2024cutaneouslarvamigrans pages 3-4)

### Quality-of-life impact (statistics)
In a cohort of **91 adults and children** in Manaus, Brazil, **91.5%** had “a considerable reduction of skin disease-associated life quality” at diagnosis; the most frequent restrictions were **intense pruritus (93.4%)**, **sleep disturbance (73.6%)**, and **shame (64.8%)**. (schuster2011lifequalityimpairment pages 1-2)

QoL improved rapidly with ivermectin; by four weeks, **73.3%** considered disease-associated life quality to have returned to normal in the abstract, and detailed results show a median mDLQI drop from 5 to 0 with most participants reporting normalization. (schuster2011lifequalityimpairment pages 1-2, schuster2011lifequalityimpairment pages 3-4)

### Suggested HPO terms
(Approximate mappings based on described phenotypes; HPO IDs not retrieved in evidence snippets.)
* Serpiginous/migratory skin lesion: **Skin lesion**, **Erythema**, **Linear skin lesion**
* Pruritus: **Pruritus**
* Excoriations: **Excoriation**
* Vesicles/bullae: **Vesicle**, **Bulla**
* Sleep disturbance from itch: **Insomnia**
* Eosinophilia (sometimes): **Eosinophilia**

## 4. Genetic / molecular information

No human causal genes, pathogenic variants, modifier genes, or epigenetic mechanisms were identified in the retrieved evidence; CLM is fundamentally an **infectious/parasitic exposure-driven** condition.

## 5. Environmental information

### Environmental factors
Key environmental determinants are **soil/sand contamination with animal feces** and conditions that permit larval development/survival in the environment (warmth and moisture). (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7, johanis2023cutaneouslarvamigrans pages 3-5)

A 2024 Oman cluster associated CLM occurrence with unusual rainfall events and muddy/puddled environments, implying environmental moisture as a practical outbreak driver. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7)

### Lifestyle factors
Walking barefoot and lying directly on sand/soil are recurring behavioral risks. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, hochedez2007hookwormrelatedcutaneouslarva pages 4-6)

### Infectious agents (pathogens)
Most commonly dog/cat hookworms (Ancylostoma spp.). (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, elmi2025cutaneouslarvamigrans pages 1-3)

## 6. Mechanism / pathophysiology

### Causal chain (trigger → mechanism → phenotype)
1. **Environmental contamination** with infective larvae from dog/cat hookworms (feces contaminating sand/soil). (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)
2. **Skin penetration** of infective larvae after bare-skin contact with contaminated substrate. (guarda2026importedcutaneouslarva pages 4-7)
3. **Intraepidermal migration** of larvae in humans (who are accidental hosts), producing a moving inflammatory focus along the larval path. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)
4. **Local inflammation with eosinophils** contributes to intense pruritus and visible serpiginous tracks; histology in a U.S. case showed organism in the stratum corneum with a dermal mixed infiltrate including eosinophils. (johanis2023cutaneouslarvamigrans media a6ff90a3)
5. **Downstream consequences**: scratching/excoriation → secondary bacterial infection; atypical manifestations include bullae or folliculitis. (guarda2026importedcutaneouslarva pages 4-7, hochedez2007hookwormrelatedcutaneouslarva pages 4-6)

### Immune involvement / tissue injury
Evidence supports eosinophil-rich inflammation as a recurring histologic pattern, consistent with helminth-driven type 2 inflammation. (johanis2023cutaneouslarvamigrans media a6ff90a3)

### Suggested ontology terms
* **GO (biological process):** inflammatory response; eosinophil chemotaxis; leukocyte migration; pruritus (as neuro-immune symptom)
* **CL (cell types):** eosinophil; keratinocyte; dermal macrophage; T cell
* **UBERON (anatomy):** skin of foot; epidermis; stratum corneum; dermis

### Molecular profiling / omics
No transcriptomic/proteomic/metabolomic profiling studies were identified in the retrieved evidence.

## 7. Anatomical structures affected

### Organ/system level
Primary organ: **skin** (typically exposed areas such as foot/ankle, thigh, buttocks). (guarda2026importedcutaneouslarva pages 4-7, johanis2023cutaneouslarvamigrans pages 1-3)

### Tissue/cell level
Primary tissue layer: **epidermis/stratum corneum** with associated dermal inflammation; organism within stratum corneum is documented histologically. (johanis2023cutaneouslarvamigrans media a6ff90a3)

## 8. Temporal development

### Onset and course
CLM is typically **acute-to-subacute** following exposure and is often self-limited if untreated, although symptoms can persist for weeks; treatment shortens duration substantially. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, shrestha2024cutaneouslarvamigrans pages 3-4)

### Remission
After ivermectin treatment in a Brazilian cohort, lesion resolution and QoL normalization occurred within weeks for most patients. (schuster2011lifequalityimpairment pages 1-2, schuster2011lifequalityimpairment pages 3-4)

## 9. Inheritance and population

### Epidemiology and geography
CLM is classically associated with tropical/subtropical climates and beach exposure, but recent case literature highlights **possible geographic expansion**.

A 2023 report emphasized that although CLM is traditionally tropical, clinicians should recognize expanding spread, including a case acquired in New England. (johanis2023cutaneouslarvamigrans pages 1-3)

### Recent outbreak/case-series data (2023–2024)
* **Oman (Seeb, Muscat), 2022–2024:** “nine cases of CLM” were reported, **78% pediatric** (7/9), with cases occurring mainly after rainfall events and with exposure to puddles/mud. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7)

### Endemic-community prevalence (older but quantitative)
In Manaus, Brazil, CLM prevalence was reported in the QoL study background as **up to ~4% overall and 15% in young children** in slum communities (contextualizing the burden). (schuster2011lifequalityimpairment pages 1-2)

## 10. Diagnostics

### Clinical diagnosis
Diagnosis is predominantly **clinical**, based on characteristic serpiginous/migratory track morphology and exposure history; Oman outbreak cases did not require biopsy. (hasni2024cutaneouslarvamigrans pages 2-6)

### Laboratory testing
Routine laboratory investigations are often normal; eosinophilia may occur but is not required for diagnosis. (elmi2025cutaneouslarvamigrans pages 1-3, hochedez2007hookwormrelatedcutaneouslarva pages 4-6)

### Histopathology / biopsy
Biopsy is not routinely required, but may confirm diagnosis; one 2023 U.S. case described punch biopsy at the leading edge with histology consistent with hookworm. (johanis2023cutaneouslarvamigrans pages 1-3, johanis2023cutaneouslarvamigrans media a6ff90a3)

### Differential diagnosis
A recent review of refractory CLM emphasized important mimics and broader differential diagnoses for migratory lesions, including **Strongyloides** (larva currens—migrates much faster), **Gnathostoma**, and other parasitic and non-parasitic causes; the differential list included dracunculiasis, fascioliasis, loiasis, paragonimiasis, tungiasis, and myiasis. (currie2025cutaneouslarvamigrans pages 6-7)

A Cureus case report additionally lists common outpatient differentials such as tinea corporis, contact dermatitis, scabies, cellulitis, and arthropod bites. (guarda2026importedcutaneouslarva pages 4-7)

## 11. Outcome / prognosis

### Natural history
CLM is usually self-limited and confined to the skin; however, morbidity can be substantial due to pruritus and sleep disturbance. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, schuster2011lifequalityimpairment pages 1-2)

### Treatment outcomes (statistics)
* **Travelers (prospective study):** ivermectin achieved an overall **97% cure rate** in a prospective series; **77%** cured after a single dose and **23% (14/64)** required additional treatment because of relapse/non-response; median time to pruritus disappearance **3 days** and lesion disappearance **7 days**; superinfection occurred in **8%** (5 cases). (bouchaud2000cutaneouslarvamigrans pages 4-5)
* **Endemic-community QoL cohort:** substantial QoL restoration within weeks after ivermectin (median mDLQI improved to near-normal by 2–4 weeks). (schuster2011lifequalityimpairment pages 1-2, schuster2011lifequalityimpairment pages 3-4)

## 12. Treatment

### First-line pharmacotherapy (real-world implementation)
* **Ivermectin (oral):** widely recommended first-line; cohort-series cure rates reported as **94–100%** in most series (lowest 81% in one series), with repeat dosing sometimes required. (johanis2023cutaneouslarvamigrans pages 3-5, bouchaud2000cutaneouslarvamigrans pages 4-5)
* **Albendazole (oral):** effective alternative; dosing commonly **400 mg/day for 3–7 days**, with some practice recommending 400 mg once daily for 5 days (e.g., Oman outbreak recommendation) or 400 mg/day for 1 week in a retrospective series. (johanis2023cutaneouslarvamigrans pages 3-5, hasni2024cutaneouslarvamigrans pages 2-6)

### Pediatric considerations
A 2024 case report/review notes a WHO consultation indicating albendazole/mebendazole safety in children ≥12 months and advises against treatment under 12 months; topical therapies may be used when oral therapy is contraindicated. (shrestha2024cutaneouslarvamigrans pages 3-4)

### Topical/adjunctive therapy
Topical 10% albendazole is described as an alternative when oral ivermectin/albendazole are contraindicated (e.g., very small children), though multiple lesions/folliculitis may respond less well. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, shrestha2024cutaneouslarvamigrans pages 3-4)

### Treatment developments (2023–2024)
* **Outbreak practice variation (Oman 2024):** variability in albendazole prescribing prompted a recommended standardized regimen of **albendazole 400 mg once daily for five days** and improved surveillance. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7)
* **Combination therapy and resistance concern:** a 2024 two-patient report from Sudan described successful **combined albendazole + ivermectin** and framed it as potentially relevant amid concerns about emerging antihelminthic resistance. (currie2025cutaneouslarvamigrans pages 13-13)

### Suggested MAXO terms (treatments)
* Anthelmintic therapy; ivermectin administration; albendazole administration; topical anthelmintic therapy; antipruritic therapy (antihistamine); treatment of secondary bacterial infection (antibiotic therapy).

## 13. Prevention

### Primary prevention (behavioral/environmental)
Evidence-based recommendations emphasize:
* **Consistent footwear** and avoidance of direct skin contact with potentially contaminated sand/soil (beaches, sandboxes). (hochedez2007hookwormrelatedcutaneouslarva pages 4-6, shrestha2024cutaneouslarvamigrans pages 1-2)
* **Pet deworming** and management of stray dogs/cats to reduce environmental contamination. (shrestha2024cutaneouslarvamigrans pages 1-2, guarda2026importedcutaneouslarva pages 4-7)

### Public health / One Health implementations
The 2024 Oman outbreak report explicitly calls for stronger surveillance and multi-sectoral action, including “electronic notification” of cases, “environmental eradication campaigns,” and collaboration between **Ministry of Health, municipality, and agriculture**—a practical One Health approach to prevention. (hasni2024cutaneouslarvamigrans pages 6-7)

## 14. Other species / natural disease

CLM is a zoonosis originating from **dogs and cats** harboring hookworm infections; environmental contamination with animal feces is repeatedly cited as central to transmission. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3, guarda2026importedcutaneouslarva pages 4-7)

## 15. Model organisms

No experimental model organism systems were described in the retrieved evidence set. Mechanistic inference relies largely on veterinary parasitology of canine/feline hookworms and human clinical/histopathologic observation. (currie2025cutaneouslarvamigrans pages 6-7, johanis2023cutaneouslarvamigrans media a6ff90a3)

---

## Recent developments and expert synthesis (emphasis 2023–2024)

1. **Climate/environment linkage in applied settings:** The Oman 2024 case series/outbreak suggests extreme weather and unusual rainfall may precipitate local clusters through increased muddy exposure and larval survival, highlighting a need for climate-aware surveillance. (hasni2024cutaneouslarvamigrans pages 2-6, hasni2024cutaneouslarvamigrans pages 6-7)
2. **Geographic expansion beyond classic tropics:** A 2023 U.S. case acquired in New England illustrates potential northward spread and the importance of clinician vigilance in temperate regions. (johanis2023cutaneouslarvamigrans pages 1-3)
3. **Treatment standardization and access:** Recent practice-focused papers emphasize ivermectin as preferred first-line but also document the operational reality of variable dosing practices and the need for standardized regimens and surveillance. (johanis2023cutaneouslarvamigrans pages 3-5, hasni2024cutaneouslarvamigrans pages 6-7)
4. **Emerging resistance concerns (One Health):** Clinical reports of refractory disease and calls for combination therapy are framed in the broader context of expanding macrocyclic lactone use in animals and emerging multi-drug resistance in animal hookworms, implying a One Health antimicrobial-resistance problem. (currie2025cutaneouslarvamigrans pages 13-13, currie2025cutaneouslarvamigrans pages 6-7)

## Key limitations of this evidence package
* Many retrieved clinical sources are case reports/series; robust incidence/prevalence estimates for CLM at national/global scale were not present in the retrieved texts.
* The retrieved full texts did not provide MONDO/MeSH numeric identifiers or CLM-specific ICD codes.
* Several 2023–2024 items were unobtainable in the current retrieval set; additional targeted PubMed/ontology queries would likely improve identifier completeness.


References

1. (rodriguezmorales2021cutaneouslarvamigrans pages 1-3): Alfonso J. Rodriguez-Morales, Natalia González-Leal, Maria Camila Montes-Montoya, Lorena Fernández-Espíndola, D. Katterine Bonilla-Aldana, José María Azeñas- Burgoa, Juan Carlos Diez de Medina, Verónica Rotela-Fisch, Melany Bermudez-Calderon, Kovy Arteaga-Livias, Fredrikke Dam Larsen, and José A. Suárez. Cutaneous larva migrans. Current Tropical Medicine Reports, 8:190-203, Apr 2021. URL: https://doi.org/10.1007/s40475-021-00239-0, doi:10.1007/s40475-021-00239-0. This article has 25 citations and is from a peer-reviewed journal.

2. (guarda2026importedcutaneouslarva pages 4-7): Diego Guarda, Cristóbal Norambuena, Priscilla Marquez, Gerardo Bascuñan, and Diego I Mendez-Villanueva. Imported cutaneous larva migrans in an adolescent traveler: a case report from chile. Cureus, Mar 2026. URL: https://doi.org/10.7759/cureus.104834, doi:10.7759/cureus.104834. This article has 0 citations.

3. (johanis2023cutaneouslarvamigrans media 1be38c9c): Michael Johanis, Karan S Cheema, Peter A Young, Saisindhu Narala, Atif Saleem, Roberto A Novoa, and Gordon H Bae. Cutaneous larva migrans in the northeastern us. Dermatology Online Journal, Sep 2023. URL: https://doi.org/10.5070/d329461906, doi:10.5070/d329461906. This article has 7 citations and is from a peer-reviewed journal.

4. (johanis2023cutaneouslarvamigrans media a6ff90a3): Michael Johanis, Karan S Cheema, Peter A Young, Saisindhu Narala, Atif Saleem, Roberto A Novoa, and Gordon H Bae. Cutaneous larva migrans in the northeastern us. Dermatology Online Journal, Sep 2023. URL: https://doi.org/10.5070/d329461906, doi:10.5070/d329461906. This article has 7 citations and is from a peer-reviewed journal.

5. (shrestha2024cutaneouslarvamigrans pages 1-2): Amrita Shrestha, Kusha K.C., Abal Baral, Rojina Shrestha, and Rabina Shrestha. Cutaneous larva migrans in a child: a case report and review of literature. Annals of Medicine and Surgery, 86:530-534, Nov 2024. URL: https://doi.org/10.1097/ms9.0000000000001512, doi:10.1097/ms9.0000000000001512. This article has 10 citations.

6. (hochedez2007hookwormrelatedcutaneouslarva pages 4-6): Patrick Hochedez and Eric Caumes. Hookworm-related cutaneous larva migrans. Journal of travel medicine, 14 5:326-33, Sep 2007. URL: https://doi.org/10.1111/j.1708-8305.2007.00148.x, doi:10.1111/j.1708-8305.2007.00148.x. This article has 213 citations and is from a domain leading peer-reviewed journal.

7. (hasni2024cutaneouslarvamigrans pages 2-6): Alya AL Hasni, Asma Al Musalhi, Fatma AL Ghashri, Zainab AL Hinai, Isra Al Mahruqi, and Amal AL Sedairi. Cutaneous larva migrans outbreak in seeb wilaya: a case series. Oman Medical Journal, Jan 2024. URL: https://doi.org/10.5001/omj.2028.07, doi:10.5001/omj.2028.07. This article has 0 citations.

8. (schuster2011lifequalityimpairment pages 1-2): Angela Schuster, Hannah Lesshafft, Sinésio Talhari, Silás Guedes de Oliveira, Ralf Ignatius, and Hermann Feldmeier. Life quality impairment caused by hookworm-related cutaneous larva migrans in resource-poor communities in manaus, brazil. PLoS Neglected Tropical Diseases, 5:e1355, Nov 2011. URL: https://doi.org/10.1371/journal.pntd.0001355, doi:10.1371/journal.pntd.0001355. This article has 51 citations and is from a domain leading peer-reviewed journal.

9. (currie2025cutaneouslarvamigrans pages 6-7): Bart J. Currie, Jessica Hoopes, and Bonny Cumming. Cutaneous larva migrans refractory to therapy with ivermectin: case report and review of implicated zoonotic pathogens, epidemiology, anthelmintic drug resistance and therapy. Tropical Medicine and Infectious Disease, 10:163, Jun 2025. URL: https://doi.org/10.3390/tropicalmed10060163, doi:10.3390/tropicalmed10060163. This article has 2 citations.

10. (elmi2025cutaneouslarvamigrans pages 1-3): T Elmi, A Ghorbannia Delavar, and M Taheri. Cutaneous larva migrans: clinical challenges and insights from a case report with a literature review. Unknown journal, 2025.

11. (johanis2023cutaneouslarvamigrans pages 1-3): Michael Johanis, Karan S Cheema, Peter A Young, Saisindhu Narala, Atif Saleem, Roberto A Novoa, and Gordon H Bae. Cutaneous larva migrans in the northeastern us. Dermatology Online Journal, Sep 2023. URL: https://doi.org/10.5070/d329461906, doi:10.5070/d329461906. This article has 7 citations and is from a peer-reviewed journal.

12. (johanis2023cutaneouslarvamigrans pages 3-5): Michael Johanis, Karan S Cheema, Peter A Young, Saisindhu Narala, Atif Saleem, Roberto A Novoa, and Gordon H Bae. Cutaneous larva migrans in the northeastern us. Dermatology Online Journal, Sep 2023. URL: https://doi.org/10.5070/d329461906, doi:10.5070/d329461906. This article has 7 citations and is from a peer-reviewed journal.

13. (hasni2024cutaneouslarvamigrans pages 6-7): Alya AL Hasni, Asma Al Musalhi, Fatma AL Ghashri, Zainab AL Hinai, Isra Al Mahruqi, and Amal AL Sedairi. Cutaneous larva migrans outbreak in seeb wilaya: a case series. Oman Medical Journal, Jan 2024. URL: https://doi.org/10.5001/omj.2028.07, doi:10.5001/omj.2028.07. This article has 0 citations.

14. (shrestha2024cutaneouslarvamigrans pages 3-4): Amrita Shrestha, Kusha K.C., Abal Baral, Rojina Shrestha, and Rabina Shrestha. Cutaneous larva migrans in a child: a case report and review of literature. Annals of Medicine and Surgery, 86:530-534, Nov 2024. URL: https://doi.org/10.1097/ms9.0000000000001512, doi:10.1097/ms9.0000000000001512. This article has 10 citations.

15. (currie2025cutaneouslarvamigrans pages 13-13): Bart J. Currie, Jessica Hoopes, and Bonny Cumming. Cutaneous larva migrans refractory to therapy with ivermectin: case report and review of implicated zoonotic pathogens, epidemiology, anthelmintic drug resistance and therapy. Tropical Medicine and Infectious Disease, 10:163, Jun 2025. URL: https://doi.org/10.3390/tropicalmed10060163, doi:10.3390/tropicalmed10060163. This article has 2 citations.

16. (schuster2011lifequalityimpairment pages 3-4): Angela Schuster, Hannah Lesshafft, Sinésio Talhari, Silás Guedes de Oliveira, Ralf Ignatius, and Hermann Feldmeier. Life quality impairment caused by hookworm-related cutaneous larva migrans in resource-poor communities in manaus, brazil. PLoS Neglected Tropical Diseases, 5:e1355, Nov 2011. URL: https://doi.org/10.1371/journal.pntd.0001355, doi:10.1371/journal.pntd.0001355. This article has 51 citations and is from a domain leading peer-reviewed journal.

17. (bouchaud2000cutaneouslarvamigrans pages 4-5): Olivier Bouchaud, S. Houzé, R. Schiemann, Rémy Durand, P. Ralaimazava, Catherine Ruggeri, and Jean-Pierre Coulaud. Cutaneous larva migrans in travelers: a prospective study, with assessment of therapy with ivermectin. Clinical infectious diseases : an official publication of the Infectious Diseases Society of America, 31 2:493-8, Aug 2000. URL: https://doi.org/10.1086/313942, doi:10.1086/313942. This article has 179 citations.