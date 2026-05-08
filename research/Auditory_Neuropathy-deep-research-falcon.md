---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:20:09.887236'
end_time: '2026-05-08T12:40:55.841284'
duration_seconds: 1245.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Auditory Neuropathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Auditory Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Auditory Neuropathy** covering all of the
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
- **Disease Name:** Auditory Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Auditory Neuropathy** covering all of the
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


# Auditory Neuropathy (Auditory Neuropathy Spectrum Disorder, ANSD): Disease Characteristics Research Report

## Executive summary
Auditory neuropathy spectrum disorder (ANSD) is a heterogeneous hearing disorder defined physiologically by evidence of preserved cochlear outer hair cell function (otoacoustic emissions and/or cochlear microphonics) with impaired neural transmission as reflected by abnormal or absent auditory brainstem responses (ABR). (wang2024clinicalandgenetic pages 3-4, wu2023outcomesofcochlear pages 1-2). Contemporary work frames ANSD as a spectrum of lesion sites (inner hair cell, ribbon synapse, spiral ganglion neuron terminals, demyelinating/axonal auditory nerve processes), which has direct implications for prognosis, cochlear implant outcomes, and emerging gene therapy—especially for presynaptic “auditory synaptopathy” due to biallelic OTOF variants. (saidia2023currentadvancesin pages 1-3, lin2020anintegrativeapproach pages 2-3, wang2024clinicalandgenetic pages 1-3).

| Concept | Details | Source (with DOI/URL and year) |
|---|---|---|
| Disease name | Auditory neuropathy; auditory neuropathy spectrum disorder (ANSD) | Wang et al., *Human Genetics* (2024), DOI: https://doi.org/10.1007/s00439-024-02652-7 (wang2024clinicalandgenetic pages 1-3) |
| Common synonym(s) | “Auditory neuropathy (AN) or auditory neuropathy spectrum disorder (ANSD)” | Wu et al., *Frontiers in Neuroscience* (2023), DOI: https://doi.org/10.3389/fnins.2023.1281884 (wu2023outcomesofcochlear pages 1-2) |
| Concise disease definition | Hearing impairment caused by impaired transmission of sound from the cochlea to the brain; lesion may involve inner hair cells, IHC ribbon synapse, postsynaptic spiral ganglion terminals, or auditory nerve demyelination/axonal loss | Saidia et al., *Journal of Clinical Medicine* (2023), DOI: https://doi.org/10.3390/jcm12030738 (saidia2023currentadvancesin pages 1-3) |
| Key diagnostic definition | Presence of otoacoustic emissions (OAE) and/or cochlear microphonics (CM) with absent or abnormal auditory brainstem responses (ABR) | Wang et al., *Human Genetics* (2024), DOI: https://doi.org/10.1007/s00439-024-02652-7; Wu et al., *Frontiers in Neuroscience* (2023), DOI: https://doi.org/10.3389/fnins.2023.1281884 (wang2024clinicalandgenetic pages 3-4, wu2023outcomesofcochlear pages 1-2) |
| Additional audiologic hallmarks | Poor speech perception despite relatively preserved pure-tone thresholds; absent stapedial reflex and absent contralateral OAE suppression are often observed | Saidia et al., *Journal of Clinical Medicine* (2023), DOI: https://doi.org/10.3390/jcm12030738 (saidia2023currentadvancesin pages 1-3) |
| MeSH identifier | not found in retrieved sources | not found in retrieved sources |
| ICD-10 identifier | not found in retrieved sources | not found in retrieved sources |
| ICD-11 identifier | not found in retrieved sources | not found in retrieved sources |
| MONDO identifier | not found in retrieved sources | not found in retrieved sources |
| Epidemiology: share among people with hearing loss | ANSD affects between 1.2% and 10% of people with hearing loss | Saidia et al., *Journal of Clinical Medicine* (2023), DOI: https://doi.org/10.3390/jcm12030738 (saidia2023currentadvancesin pages 1-3) |
| Epidemiology: share among hearing-loss cases in one cohort/reviewed populations | Auditory neuropathy affects 1.2%–8.4% of cases with hearing loss from different populations | Wang et al., *Human Genetics* (2024), DOI: https://doi.org/10.1007/s00439-024-02652-7 (wang2024clinicalandgenetic pages 1-3) |
| Epidemiology: school-age/severe-profound pediatric hearing loss | ANSD is observed in 4%–5% of all degrees of hearing loss and 10%–15% of school-age children with severe to profound SNHL | Jafari et al., *PLOS ONE* (2024), DOI: https://doi.org/10.1371/journal.pone.0304316 (jafari2024predictorsofcochlear pages 1-2) |
| Epidemiology: children with SNHL | Nearly 9.85% of 1,025 children with sensorineural hearing loss were identified to have ANSD | Wu et al., *Frontiers in Neuroscience* (2023), DOI: https://doi.org/10.3389/fnins.2023.1281884 (wu2023outcomesofcochlear pages 1-2) |
| Epidemiology: newborn prevalence | 0.006%–0.039% in low-risk newborn population | Wang et al., *Human Genetics* (2024), DOI: https://doi.org/10.1007/s00439-024-02652-7 (wang2024clinicalandgenetic pages 1-3) |
| Epidemiology: birth incidence and hearing-loss proportion | Incidence ~1–3 per 10,000 births; 8.4%–11% of children with permanent hearing loss | Smith thesis/excerpt (2018), DOI: https://doi.org/10.14288/1.0372052 (smith2018cochlearmicrophonicsfrom pages 17-21) |
| Screening limitation statistic | Newborn hearing screening may miss 30%–50% of ANSD cases | Smith thesis/excerpt (2018), DOI: https://doi.org/10.14288/1.0372052 (smith2018cochlearmicrophonicsfrom pages 17-21) |


*Table: This table summarizes core disease naming, diagnostic hallmarks, identifier availability in the retrieved sources, and key epidemiology statistics for auditory neuropathy spectrum disorder. It is useful as a quick-reference artifact for disease knowledge-base population.*

| Item | Population/Model | Key quantitative results | Publication date/Trial post date | URL/DOI/NCT | Notes |
|---|---|---|---|---|---|
| Wang 2024: large AN genetic cohort | Retrospective human cohort; 311 patients with auditory neuropathy (AN) | Pathogenic/likely pathogenic variants identified in 98/311 (31.5%); subgroup yields: trios 54.4%, families 56.2%, proband-only 22.9%; infants 45.7% vs non-infants 25.6%; bilateral AN 33.7% vs unilateral 0%; OTOF accounted for 96.6% (28/29) of OTOF-positive cases in infants; cohort was 93.6% bilateral AN; MRI auditory nerve abnormalities in 26.3%; CM recorded in 241 ears (77.5%); only 7.6% of ears elicited at least one ABR wave (wang2024clinicalandgenetic pages 1-3, wang2024clinicalandgenetic pages 12-14) | Published online 2024-03-08 | https://doi.org/10.1007/s00439-024-02652-7 | Identified OTOF and AIFM1 as the top two genes; study emphasizes different genetic spectra by age at onset and laterality (wang2024clinicalandgenetic pages 1-3, wang2024clinicalandgenetic pages 12-14) |
| Wu 2023: CI outcomes in AN | Human cohort; 75 AN patients receiving cochlear implantation; genetic testing in 46 | After CI, average aided thresholds: prelingual 38.25 ± 6.63 dB, post-lingual 32.58 ± 9.26 dB; CAP improved to 5.52 ± 1.64 (prelingual) and 6.00 ± 0.96 (post-lingual), both p < 0.001; SIR improved to 3.57 ± 1.22 and 4.15 ± 0.95, both p < 0.001; maximum speech recognition ranged 58–93% (prelingual) and 43–98% (post-lingual); CN deficiency associated with poorer CI speech outcomes (p = 0.008) (wu2023outcomesofcochlear pages 1-2, wu2023outcomesofcochlear pages 3-5) | 2023-11-13 | https://doi.org/10.3389/fnins.2023.1281884 | Included molecular etiologies such as TWIST1, ACTG1, m.A7445G, and ACTB CNV; OTOF subgroup showed CAP improvement from 0.10 ± 0.32 to 6.20 ± 1.32 and SIR from 1.00 to 3.83 ± 1.10 (wu2023outcomesofcochlear pages 3-5) |
| Jafari 2024: predictors of pediatric CI outcome | Matched case-control study; 66 implanted children, including 22 ANSD and 44 SNHL controls | No significant between-group differences across five open-set speech tests; average outcome scores ranged 88.40% to 95.65%; predictors of better post-CI speech perception were longer CI follow-up, younger age at CI activation, younger age at hearing-aid fitting, and use of two CIs (jafari2024predictorsofcochlear pages 1-2, jafari2024predictorsofcochlear pages 2-4) | 2024-05-29 | https://doi.org/10.1371/journal.pone.0304316 | ANSD cases had bilateral disease and no cochlear nerve deficiency on MRI; supports that children with ANSD can achieve outcomes similar to matched SNHL peers (jafari2024predictorsofcochlear pages 1-2, jafari2024predictorsofcochlear pages 2-4) |
| Buianova 2024: genetically determined ANSD in children | Human pediatric cohort; 20 children with clinically confirmed ANSD within a larger hearing-loss study | Variants found in 12/20 ANSD cases (60%); OTOF was the most frequent ANSD gene in 5/20 (25%); genetically determined hearing loss identified in 55.74% of children treated at center; among SNHL controls, GJB2 accounted for 56/102 (54.90%); parent-reported rehabilitation outcomes were poorer in ANSD vs SNHL; device-use months 14.35 ± 13.1 (ANSD) vs 20.37 ± 16.4 (SNHL); median satisfaction/QoL score 6 vs 7, p = 0.0026 (buianova2024heterogeneousgroupof pages 7-9, buianova2024heterogeneousgroupof pages 2-3) | 2024-11 | https://doi.org/10.3390/ijms252312554 | Report also cites early human AAV1-hOTOF experience in 5 children: no serious adverse effects; ABR thresholds improved from >95 dB to 50–85 dB with recovery of speech perception and sound localization (as summarized in paper) (buianova2024heterogeneousgroupof pages 7-9) |
| Forli 2023: temperature-sensitive ANSD | Single-patient case report; 7-year-old boy with TS-ANSD | Baseline mild-to-moderate hearing loss at low/mid frequencies worsening to severe-to-profound with fever/exercise; OAEs present, click/tone-burst ABRs generally absent; identified OTOF c.2521G>A missense variant plus 7.4 kb deletion; phenotype returned toward baseline after temperature normalized (forli2023temperaturesensitiveauditoryneuropathy pages 1-2) | 2023-02-13 | https://doi.org/10.3390/medicina59020352 | Illustrates OTOF-related temperature-sensitive phenotype; no inner-ear malformation on CT/MRI (forli2023temperaturesensitiveauditoryneuropathy pages 1-2) |
| Dmitriev 2023: OTOF missense prediction | Computational variant-classification study using OTOF missense variants linked to ANSD | Dataset included 270 annotated single amino-acid substitutions; random-forest ConStruct model achieved balanced accuracy 0.866 and AUC 0.903 by 5-fold cross-validation; evaluated 1302 OTOF VUS and prioritized 16 as most probable pathogenic variants (dmitriev2023predictingtheimpact pages 1-2) | 2023-12-07 | https://doi.org/10.3390/ijms242417240 | Useful for variant interpretation in OTOF-associated ANSD, especially early diagnosis and panel/WES interpretation (dmitriev2023predictingtheimpact pages 1-2) |
| NCT05821959: AAVAnc80-hOTOF interventional trial | Phase 1/2, non-randomized interventional trial; estimated n = 22 | Start date 2023-09-15; primary completion estimated 2028-10; dose levels up to 4.1E11 and 8.1E11 vg/cochlea; primary endpoint: frequency of adverse events through ~1 year; secondary endpoints include ABR threshold change; key inclusion: at least two OTOF mutations, profound bilateral SNHL by ABR, preserved DPOAEs, no cochlear implant in study ear(s) (NCT05821959 chunk 1) | First posted 2023-04-20 | NCT05821959; https://clinicaltrials.gov/study/NCT05821959 | Intracochlear AAVAnc80-hOTOF via Akouos delivery device; includes unilateral cohorts and bilateral expansion (NCT05821959 chunk 1) |
| NCT05788536 (CHORD): DB-OTO interventional trial | Phase 1/2, open-label multicenter trial; estimated n = 30 children/infants | Start date 2023-06-27; primary completion estimated 2032-02-28; primary endpoints: TEAEs up to week 104 and achievement of PTA threshold ≤70 dB; secondary endpoints include ABR to click up to week 48, ESP ≥3, PTA ≤45 dB and ≤25 dB, SAT milestones, speech perception and language measures; key inclusion: age <18 years, biallelic likely pathogenic/pathogenic OTOF variants, profound SNHL >90 dB HL, OAE or CM evidence of outer hair cell function, exclusion of non-OTOF AN risk factors (NCT05788536 chunk 1, NCT05788536 chunk 2) | First posted 2023-03-29 | NCT05788536; https://clinicaltrials.gov/study/NCT05788536 | Unilateral dose-escalation followed by bilateral expansion; registry record cites later derived publication on DB-OTO gene therapy (NCT05788536 chunk 1, NCT05788536 chunk 2) |
| NCT06696456: long-term follow-up after AAVAnc80-hOTOF | Observational post-intervention long-term follow-up study; estimated n = 30 | Start date 2024-11-11; completion estimated 2033-04; follows prior AK-OTOF-101 participants for ~4 additional years (total ~5 years after dosing); primary outcome: late-occurring adverse events; secondary outcome: ABR threshold change (NCT06696456 chunk 1) | First posted 2024-11-20 | NCT06696456; https://clinicaltrials.gov/study/NCT06696456 | Includes only individuals previously dosed with AAVAnc80-hOTOF in AK-OTOF-101; designed to assess durability and delayed safety signals (NCT06696456 chunk 1) |
| NCT05572073: OTOF natural history study | Observational retrospective/prospective natural history study; estimated n = 150 | Start date 2022-07-14; completion estimated 2029-02; primary outcome ABR from first audiologic data through 5-year prospective follow-up; secondary outcome OAE; inclusion requires bilateral SNHL with OTOF mutation(s), including AN/ANSD phenotype or history; prospective phase requires OAE/CM present and absent/abnormal ABR in at least one non-implanted ear; excludes cochlear nerve deficiency/dysplasia (NCT05572073 chunk 1) | First posted 2022-10-07 | NCT05572073; https://clinicaltrials.gov/study/NCT05572073 | Important enabling study for defining progression, candidate selection, and trial-readout baselines in otoferlin-mediated ANSD (NCT05572073 chunk 1) |


*Table: This table compiles the most decision-relevant recent quantitative findings from human ANSD cohorts, cochlear implantation studies, variant-interpretation work, and current OTOF gene therapy trials. It is useful as a compact evidence map for genetics, prognosis, rehabilitation outcomes, and translational trial design.*

| Gene | Inheritance pattern (as stated) | Lesion site class (as stated) | Evidence type | Key notes/phenotype | Key citation (DOI/URL/year) |
|---|---|---|---|---|---|
| OTOF | Autosomal recessive; biallelic pathogenic/likely pathogenic variants; DFNB9 (saidia2023currentadvancesin pages 3-4, forli2023temperaturesensitiveauditoryneuropathy pages 1-2, stalmann2021otoferlinisrequired pages 1-2) | Presynaptic; inner hair cell/ribbon synapse; auditory synaptopathy (lin2020anintegrativeapproach pages 2-3, saidia2023currentadvancesin pages 3-4, stalmann2021otoferlinisrequired pages 1-2) | Human cohort, case report, mouse, review, computational | Most common infant AN gene in a 311-case cohort; 96.6% (28/29) of OTOF-positive cases were in infants. Causes congenital/prelingual ANSD and temperature-sensitive ANSD; ~220 pathogenic variants reported; Otof-/- mice show synapse loss and progressive SGN/IHC/OHC degeneration. Variant-modeling study used 270 missense SAVs and prioritized 16 likely pathogenic VUS (wang2024clinicalandgenetic pages 1-3, forli2023temperaturesensitiveauditoryneuropathy pages 1-2, dmitriev2023predictingtheimpact pages 1-2, stalmann2021otoferlinisrequired pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; 10.3390/jcm12030738 / https://doi.org/10.3390/jcm12030738 / 2023; 10.3389/fncel.2021.677543 / https://doi.org/10.3389/fncel.2021.677543 / 2021 (wang2024clinicalandgenetic pages 1-3, saidia2023currentadvancesin pages 3-4, stalmann2021otoferlinisrequired pages 1-2) |
| AIFM1 | X-linked; AUNX1 (wang2024clinicalandgenetic pages 1-3, shi2024aiftranslocationinto pages 1-3) | Postsynaptic / auditory nerve-related; mitochondrial neuronal pathology affecting auditory pathway (wang2024clinicalandgenetic pages 1-3, qiu2023impairedaifchchd4interaction pages 1-2, shi2024aiftranslocationinto pages 1-3) | Human cohort, iPSC-derived neurons, mouse, review | Common non-infant AN gene in the large cohort; patient-iPSC neurons showed impaired AIF-CHCHD4 interaction, mitochondrial Ca2+ overload, ROS increase, and caspase-independent apoptosis. Knock-in mice developed progressive hearing loss from P30 with SGN loss and later demyelination (wang2024clinicalandgenetic pages 1-3, qiu2023impairedaifchchd4interaction pages 1-2, shi2024aiftranslocationinto pages 1-3) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; 10.1038/s41419-023-05899-6 / https://doi.org/10.1038/s41419-023-05899-6 / 2023; 10.1093/hmg/ddae010 / https://doi.org/10.1093/hmg/ddae010 / 2024 (wang2024clinicalandgenetic pages 1-3, qiu2023impairedaifchchd4interaction pages 1-2, shi2024aiftranslocationinto pages 1-3) |
| PRPS1 | X-linked (jafari2024predictorsofcochlear pages 1-2) | Not clearly localized in retrieved primary sources; listed among genetic predispositions to ANSD (jafari2024predictorsofcochlear pages 1-2) | Review / clinical overview | Mentioned as an X-linked cause/predisposition in pediatric ANSD overview; also detected among genes in a pediatric ANSD cohort (buianova2024heterogeneousgroupof pages 2-3, jafari2024predictorsofcochlear pages 1-2) | https://doi.org/10.1371/journal.pone.0304316 / 2024 (jafari2024predictorsofcochlear pages 1-2); 10.3390/ijms252312554 / https://doi.org/10.3390/ijms252312554 / 2024 (buianova2024heterogeneousgroupof pages 2-3) |
| OPA1 | Autosomal dominant (listed among dominant predisposition genes) (jafari2024predictorsofcochlear pages 1-2) | Postsynaptic / spiral ganglion-related (wang2024clinicalandgenetic pages 1-3) | Human cohort, review | Identified in both infant and non-infant groups in the 311-case cohort; review literature places OPA1 among dominant ANSD genes and postsynaptic lesions (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; https://doi.org/10.1371/journal.pone.0304316 / 2024 (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) |
| ATP1A3 | Autosomal dominant (listed among dominant predisposition genes) (jafari2024predictorsofcochlear pages 1-2) | Postsynaptic / spiral ganglion-related (wang2024clinicalandgenetic pages 1-3) | Human cohort, review | Found in both infant and non-infant subgroups in the large cohort; genotype-specific CI review summarized favorable CI outcomes for ATP1A3/CAPOS-associated ANSD (wang2024clinicalandgenetic pages 1-3, ismail2024systematicreviewof pages 2-4, jafari2024predictorsofcochlear pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; 10.1186/s43163-024-00677-3 / https://doi.org/10.1186/s43163-024-00677-3 / 2024 (wang2024clinicalandgenetic pages 1-3, ismail2024systematicreviewof pages 2-4) |
| PJVK | Autosomal recessive / DFNB59 (jafari2024predictorsofcochlear pages 1-2, lu2022genetherapywith pages 1-2) | Variable; auditory hair cells and first-order neurons/SGNs implicated; sometimes described as auditory neuropathy, sometimes cochlear origin (lu2022genetherapywith pages 1-2) | Human cohort/review, mouse, gene therapy | Listed as recessive ANSD gene; patients may show limited CI benefit. Pjvk-mutant mice show increased hearing thresholds, SGN degeneration, and vestibular dysfunction; Anc80L65-PJVK gene transfer improved cochlear/vestibular phenotypes (jafari2024predictorsofcochlear pages 1-2, lu2022genetherapywith pages 1-2) | https://doi.org/10.1371/journal.pone.0304316 / 2024; 10.1172/jci.insight.152941 / https://doi.org/10.1172/jci.insight.152941 / 2022 (jafari2024predictorsofcochlear pages 1-2, lu2022genetherapywith pages 1-2) |
| DIAPH3 | Autosomal dominant (jafari2024predictorsofcochlear pages 1-2) | Postsynaptic / spiral ganglion-related (wang2024clinicalandgenetic pages 1-3) | Review | Listed among dominant ANSD genes and mapped in review/classification work to postsynaptic spiral ganglion lesion class (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; https://doi.org/10.1371/journal.pone.0304316 / 2024 (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) |
| CACNA1D | Not stated in retrieved source set | Synaptic site (wang2024clinicalandgenetic pages 1-3) | Review | Named among genes affecting the synaptic site in AN classification reviews (wang2024clinicalandgenetic pages 1-3) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024 (wang2024clinicalandgenetic pages 1-3) |
| CABP2 | Not stated in retrieved source set | Synaptic site (wang2024clinicalandgenetic pages 1-3) | Review | Named among genes affecting the synaptic site in AN classification reviews; AAV approaches for Cabp2 are discussed in gene-therapy review (wang2024clinicalandgenetic pages 1-3, saidia2023currentadvancesin pages 11-12) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; 10.3390/jcm12030738 / https://doi.org/10.3390/jcm12030738 / 2023 (wang2024clinicalandgenetic pages 1-3, saidia2023currentadvancesin pages 11-12) |
| SLC17A8 | Autosomal dominant (listed among dominant predisposition genes) (jafari2024predictorsofcochlear pages 1-2) | Synaptic site (wang2024clinicalandgenetic pages 1-3) | Review | Listed among dominant ANSD genes; review classifies it as synaptic-site gene (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; https://doi.org/10.1371/journal.pone.0304316 / 2024 (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) |
| MPZ | Autosomal dominant (listed among dominant predisposition genes) (jafari2024predictorsofcochlear pages 1-2) | Auditory nerve / spiral ganglion cell bodies and proximal axons (wang2024clinicalandgenetic pages 1-3) | Review | Listed as dominant ANSD gene in pediatric overview and as nerve-level lesion gene in large-cohort mechanistic classification (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024; https://doi.org/10.1371/journal.pone.0304316 / 2024 (wang2024clinicalandgenetic pages 1-3, jafari2024predictorsofcochlear pages 1-2) |
| PMP22 | Not stated in retrieved source set | Auditory nerve / spiral ganglion cell bodies and proximal axons (wang2024clinicalandgenetic pages 1-3) | Review | Included in lesion-site classification as an auditory-nerve gene for AN (wang2024clinicalandgenetic pages 1-3) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024 (wang2024clinicalandgenetic pages 1-3) |
| TIMM8A | Not stated in retrieved source set | Auditory nerve / spiral ganglion cell bodies and proximal axons (wang2024clinicalandgenetic pages 1-3) | Review | Included in lesion-site classification as an auditory-nerve gene for AN (wang2024clinicalandgenetic pages 1-3) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024 (wang2024clinicalandgenetic pages 1-3) |
| NARS2 | Not stated in retrieved source set | Auditory nerve / spiral ganglion cell bodies and proximal axons (wang2024clinicalandgenetic pages 1-3) | Review | Included in lesion-site classification as an auditory-nerve gene for AN (wang2024clinicalandgenetic pages 1-3) | 10.1007/s00439-024-02652-7 / https://doi.org/10.1007/s00439-024-02652-7 / 2024 (wang2024clinicalandgenetic pages 1-3) |
| WFS1 | Not stated in retrieved source set | Presynaptic in the pediatric etiologic/site-of-lesion cohort (lin2020anintegrativeapproach pages 2-3) | Human cohort | One syndromic/genetic pediatric AN case carried WFS1 p.A684V in the 101-child cohort; study grouped WFS1 among presynaptic/genetic causes (lin2020anintegrativeapproach pages 2-3) | 10.1038/s41598-020-66877-y / https://doi.org/10.1038/s41598-020-66877-y / 2020 (lin2020anintegrativeapproach pages 2-3) |
| PLP1 | Not stated in retrieved source set | Postsynaptic in the pediatric etiologic/site-of-lesion cohort (lin2020anintegrativeapproach pages 2-3) | Human cohort | One syndromic/genetic pediatric AN case carried PLP1 duplication; study grouped Pelizaeus-Merzbacher disease/PLP1 among postsynaptic causes (lin2020anintegrativeapproach pages 2-3) | 10.1038/s41598-020-66877-y / https://doi.org/10.1038/s41598-020-66877-y / 2020 (lin2020anintegrativeapproach pages 2-3) |
| m.1555A>G | Mitochondrial (maternal inheritance implied by mitochondrial variant class) (jafari2024predictorsofcochlear pages 1-2) | Presynaptic in pediatric etiologic/site-of-lesion cohort (lin2020anintegrativeapproach pages 2-3) | Human cohort | Identified as a genetic cause in pediatric auditory neuropathy; study classified mitochondrial mutation among presynaptic causes (lin2020anintegrativeapproach pages 2-3, jafari2024predictorsofcochlear pages 1-2) | 10.1038/s41598-020-66877-y / https://doi.org/10.1038/s41598-020-66877-y / 2020; https://doi.org/10.1371/journal.pone.0304316 / 2024 (lin2020anintegrativeapproach pages 2-3, jafari2024predictorsofcochlear pages 1-2) |


*Table: This table maps Mendelian genes explicitly mentioned in the retrieved ANSD/auditory neuropathy sources to their reported inheritance patterns, mechanistic lesion-site classes, and evidence types. It is useful for connecting genotype to pathophysiology and for anticipating diagnosis, prognosis, and cochlear implant response.*

---

## 1. Disease information
### 1.1 What is the disease?
ANSD is a hearing impairment in which sound detection thresholds may be variable (mild to profound), but speech perception is often disproportionately poor because neural timing/synchrony is disrupted despite evidence of intact outer hair cell function. (saidia2023currentadvancesin pages 1-3, wu2023outcomesofcochlear pages 1-2).

**Current concept/definition (lesion-site spectrum):** A 2023 gene therapy-focused review defines ANSD as “hearing impairments characterized by an impaired transmission of sound from the cochlea to the brain” and explicitly enumerates candidate lesion sites: inner hair cells (IHCs), IHC ribbon synapse (presynaptic glutamate release), postsynaptic spiral ganglion neuron terminals, and demyelination/axonal loss within the auditory nerve. (saidia2023currentadvancesin pages 1-3).

### 1.2 Key identifiers
Within the retrieved source set, formal cross-ontology identifiers were not captured for MeSH/ICD-10/ICD-11/MONDO/Orphanet/OMIM as explicit IDs (artifact-00). (wang2024clinicalandgenetic pages 3-4).

**OMIM usage in recent research:** A 2024 large cohort study describes using OMIM “clinical synopsis advanced search” to find entries associated with “auditory neuropathy,” but the excerpted text does not list specific OMIM numbers for ANSD as a single entity. (wang2024clinicalandgenetic pages 3-4).

### 1.3 Synonyms/alternative names
Commonly used names include **auditory neuropathy (AN)** and **auditory neuropathy spectrum disorder (ANSD)**. (wu2023outcomesofcochlear pages 1-2, wang2024clinicalandgenetic pages 1-3).

### 1.4 Evidence sources
Evidence in this report comes from:
- Aggregated disease-level resources and reviews (e.g., Saidia et al. 2023) (saidia2023currentadvancesin pages 1-3)
- Large and moderate human cohorts (Wang et al. 2024; Wu et al. 2023; Jafari et al. 2024) (wang2024clinicalandgenetic pages 1-3, wu2023outcomesofcochlear pages 1-2, jafari2024predictorsofcochlear pages 1-2)
- Case report evidence for specific phenotypes (Forli et al. 2023 temperature-sensitive ANSD) (forli2023temperaturesensitiveauditoryneuropathy pages 1-2)
- Mechanistic human cellular models (patient iPSC-derived neurons for AIFM1) (qiu2023impairedaifchchd4interaction pages 1-2)
- Model organisms (OTOF and AIFM1 mouse models; PJVK mutant mouse and inner-ear gene transfer) (stalmann2021otoferlinisrequired pages 1-2, shi2024aiftranslocationinto pages 1-3, lu2022genetherapywith pages 1-2)
- Clinical trial registry entries for OTOF gene therapy and natural history studies (clinicaltrials.gov) (NCT05821959 chunk 1, NCT05788536 chunk 1, NCT06696456 chunk 1, NCT05572073 chunk 1)

---

## 2. Etiology
### 2.1 Disease causal factors
**Genetic causes (Mendelian):** Recent large-cohort sequencing shows a substantial Mendelian contribution, with pathogenic/likely pathogenic variants identified in 23 genes in 31.5% (98/311) of clinically diagnosed AN cases. (wang2024clinicalandgenetic pages 1-3). OTOF predominates in infant-onset AN, whereas AIFM1 is enriched in non-infant (later-onset) AN. (wang2024clinicalandgenetic pages 1-3).

**Acquired/non-genetic factors:** Contemporary clinical literature lists perinatal and environmental contributors such as hyperbilirubinemia, hypoxia/anoxia, infection, prematurity, ototoxic drug exposure, and cochlear nerve deficiency (CND) as risk factors/associations. (wu2023outcomesofcochlear pages 1-2).

### 2.2 Risk factors
#### Genetic risk factors
A 2024 pediatric cochlear implant outcome paper summarizes genetic predisposition as >40% in some cohorts and lists representative inheritance modes (AR, AD, X-linked, mitochondrial), giving examples including **OTOF, PJVK** (AR), **OPA1, MPZ, ATP1A3, SLC17A8, DIAPH3** (AD), **AIFM1** (X-linked), and mitochondrial variants. (jafari2024predictorsofcochlear pages 1-2).

#### Environmental/perinatal risk factors
In a 2023 cochlear implantation cohort paper, risk factors “highly related to AN” included hyperbilirubinemia, infection, prematurity, ototoxic drug exposure, cochlear nerve deficiency, and congenital brain anomalies. (wu2023outcomesofcochlear pages 1-2).

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interaction
Direct gene–environment interaction analyses were not identified in the retrieved sources. However, the lesion-site spectrum framework implies that environmental insults (e.g., hyperbilirubinemia, hypoxia) may preferentially drive postsynaptic/nerve forms, whereas specific genes (e.g., OTOF) drive presynaptic synaptopathy—potentially interacting with developmental timing and intervention windows. (lin2020anintegrativeapproach pages 2-3, saidia2023currentadvancesin pages 1-3).

---

## 3. Phenotypes
### 3.1 Core auditory phenotypes
**Key clinical/audiologic phenotype:** A defining feature is the discrepancy between relatively preserved cochlear outer hair cell activity and impaired neural conduction, manifesting as present OAE/CM with absent/abnormal ABR and poor speech perception (often especially in noise). (saidia2023currentadvancesin pages 1-3, jafari2024predictorsofcochlear pages 1-2).

**Suggested HPO terms (non-exhaustive):**
- Abnormal auditory brainstem response (suggest: *Abnormal auditory brainstem response* [HPO term exists])
- Sensorineural hearing impairment
- Speech discrimination abnormality / impaired speech perception (esp. in noise)
- Auditory neuropathy

### 3.2 Age of onset and course
A pediatric etiologic cohort study (n=101) reported that onset at birth was common (82/101; 81.2%), especially for acquired forms (46/48; 95.8%). (lin2020anintegrativeapproach pages 2-3).

A large 2024 AN cohort notes variability: hearing may improve, remain stable, or deteriorate; some cases showed progressive worsening with loss of OAEs and progressive decreases in speech recognition over follow-up. (wang2024clinicalandgenetic pages 12-14).

### 3.3 Frequency and variability
Population-level prevalence estimates vary by ascertainment:
- 1.2–8.4% of hearing-loss cases (multiple populations) and 0.006–0.039% in low-risk newborns in one large review/citation summary embedded in a 2024 cohort introduction. (wang2024clinicalandgenetic pages 1-3)
- 4–5% of all degrees of hearing loss and 10–15% of school-age children with severe-to-profound SNHL (clinical overview within a 2024 pediatric CI outcomes study). (jafari2024predictorsofcochlear pages 1-2)

### 3.4 Quality-of-life impact
A 2024 pediatric genetic cohort reported parent survey data suggesting rehabilitation satisfaction and QoL improvements were lower in ANSD than in SNHL comparators (median satisfaction/QoL score 6 vs 7; p=0.0026). (buianova2024heterogeneousgroupof pages 7-9).

---

## 4. Genetic / molecular information
### 4.1 Causal genes (selected, from retrieved evidence)
Recent cohort evidence supports a multi-gene Mendelian architecture with strong dependence on onset age and laterality.

- **Wang et al. 2024 (311 cases)**: 23 genes with pathogenic/likely pathogenic variants in 31.5% overall; OTOF and AIFM1 are the top two genes and show striking age dependence (OTOF mostly infant; AIFM1 non-infant). (wang2024clinicalandgenetic pages 1-3).
- **Buianova et al. 2024 (20 clinically confirmed pediatric ANSD)**: variants identified in 60% (12/20); OTOF 25% (5/20) with additional genes including PRPS1 and HOMER2, among others. (buianova2024heterogeneousgroupof pages 2-3).

(See artifact-02 for gene-by-gene mapping to lesion site and evidence type.) (wang2024clinicalandgenetic pages 1-3, lin2020anintegrativeapproach pages 2-3, lu2022genetherapywith pages 1-2).

### 4.2 Pathogenic variants and variant classes (OTOF example)
**OTOF variant spectrum and interpretation challenges:** A 2023 computational study constructed a dataset of **270** annotated OTOF single amino-acid substitutions related to ANSD and evaluated **1302** variants of uncertain significance (VUS), prioritizing **16** as “most probable pathogenic variants” based on predicted impact. The model achieved balanced accuracy **0.866** and AUC **0.903** (5-fold cross-validation). (dmitriev2023predictingtheimpact pages 1-2).

**Temperature-sensitive ANSD:** A 2023 case report identified OTOF **c.2521G>A** missense plus a **7.4 kb deletion**, in a child whose hearing thresholds worsened with fever/exercise and improved after temperature normalized; OAEs were present and ABRs generally absent. (forli2023temperaturesensitiveauditoryneuropathy pages 1-2).

### 4.3 Modifier genes
No modifier-gene evidence was identified in the retrieved sources.

### 4.4 Epigenetic information
No disease-specific epigenetic mechanisms were identified in the retrieved sources.

---

## 5. Environmental information
Non-genetic contributing factors are described mainly as perinatal and medical risk factors (e.g., hyperbilirubinemia, prematurity, infection, ototoxic drug exposure). (wu2023outcomesofcochlear pages 1-2). No toxin-specific or exposure-response analyses were identified in the retrieved sources.

---

## 6. Mechanism / pathophysiology
### 6.1 Lesion-site framework (current understanding)
ANSD is increasingly conceptualized as a **spectrum** spanning:
- **IHC dysfunction**
- **IHC ribbon synapse (presynaptic) synaptopathy**
- **Postsynaptic terminal / spiral ganglion neuron (SGN) dysfunction**
- **Auditory nerve demyelination/axonal loss**
This framework is explicitly stated in recent reviews and is operationalized in cohort analyses that classify cases as presynaptic versus postsynaptic based on genetics and ancillary tests. (saidia2023currentadvancesin pages 1-3, lin2020anintegrativeapproach pages 2-3).

### 6.2 Mechanistic causal chains (examples)
#### (A) OTOF-related presynaptic auditory synaptopathy
- **Trigger:** biallelic OTOF pathogenic variants impair otoferlin, a key IHC synaptic protein involved in vesicle exocytosis/rapid replenishment. (saidia2023currentadvancesin pages 3-4, stalmann2021otoferlinisrequired pages 1-2).
- **Primary defect:** impaired neurotransmitter release at the IHC ribbon synapse → absent/abnormal ABR with preserved outer hair cell measures (OAEs/CM). (saidia2023currentadvancesin pages 1-3, lin2020anintegrativeapproach pages 2-3).
- **Downstream biology (mouse natural history):** in Otof−/− mice, synapse counts drop from ~15/IHC at P14 to ~7 at 8 weeks and ~6 at 48 weeks, accompanied by SGN decline and progressive IHC loss (~75% of WT IHCs) plus later OHC dysfunction (DPOAE high-frequency decay by ~24 weeks). (stalmann2021otoferlinisrequired pages 1-2).

**GO process suggestions:** synaptic vesicle exocytosis; chemical synaptic transmission; glutamatergic synaptic transmission; auditory receptor cell synaptic transmission.

**Cell type (CL) suggestions:** cochlear inner hair cell; spiral ganglion neuron; Schwann cell (for neuropathic/demyelinating forms).

#### (B) AIFM1-related postsynaptic/nerve auditory neuropathy (mitochondrial-neurodegeneration axis)
**Human iPSC-neuron mechanism:** A 2023 mechanistic study using patient PBMC→iPSC→neurons reports that an AIFM1 c.1265G>A variant caused a splicing deletion producing altered AIF proteins, impairing AIF dimerization and weakening AIF–CHCHD4 interaction. This led to inhibited mitochondrial import of ETC subunits, increased ADP/ATP ratio, elevated ROS, impaired MICU1–MICU2 heterodimerization causing mitochondrial Ca2+ overload, calpain activation, AIF cleavage and nuclear translocation, and caspase-independent apoptosis; CRISPR correction improved neuronal physiology. (qiu2023impairedaifchchd4interaction pages 1-2).

**Mouse model (AUNX1):** A 2024 Aifm1 p.R450Q knock-in mouse showed progressive hearing loss beginning around P30, worsening by P60, and stabilizing until P210, with progressive SGN reduction (P30), ribbon loss (P60), later demyelination and mitochondrial abnormalities, and muscle atrophy by P210. (shi2024aiftranslocationinto pages 1-3).

**GO process suggestions:** mitochondrial calcium ion homeostasis; oxidative phosphorylation; reactive oxygen species metabolic process; regulation of apoptotic process; axon ensheathment / myelination.

#### (C) PJVK-related cochlear/neuronal vulnerability and gene therapy in mice
A 2022 preclinical study reports that recessive PJVK mutations cause pejvakin deficiency affecting hair cells and first-order neurons (SGNs), with limited benefit from cochlear implantation in some patients. In Pjvk mutant mice, Anc80L65-mediated PJVK transgene delivery led to robust pejvakin expression in cochlear/vestibular hair cells and neurons with morphologic restoration (including SGN density) and partial hearing recovery, plus vestibular recovery to WT levels. (lu2022genetherapywith pages 1-2).

### 6.3 Advanced technologies highlighted in recent work
- **Patient-derived iPSC neurons + isogenic CRISPR correction** to define ANSD mitochondrial mechanisms (AIFM1). (qiu2023impairedaifchchd4interaction pages 1-2)
- **Large-cohort sequencing (WGS/panels)** with subgroup stratification by onset age/laterality and ACMG classification workflows. (wang2024clinicalandgenetic pages 3-4, wang2024clinicalandgenetic pages 1-3)

---

## 7. Anatomical structures affected
### 7.1 Organ, tissue, and cell types
Primary organ/system: **inner ear (cochlea) and auditory nerve pathways**. (saidia2023currentadvancesin pages 1-3, wang2024clinicalandgenetic pages 1-3).

Key tissues/cells implicated by the lesion-site framework and model/human genetics:
- **Cochlear inner hair cells (IHCs)** and **IHC ribbon synapses** (OTOF synaptopathy). (stalmann2021otoferlinisrequired pages 1-2, saidia2023currentadvancesin pages 3-4)
- **Spiral ganglion neurons (SGNs)** and their terminals (postsynaptic forms; AIFM1; PJVK). (shi2024aiftranslocationinto pages 1-3, lu2022genetherapywith pages 1-2)
- **Auditory nerve myelination/axons** (demyelination/axonal loss described in AIFM1 model). (shi2024aiftranslocationinto pages 1-3)

**UBERON suggestions:** cochlea; organ of Corti; spiral ganglion; vestibulocochlear nerve.

**GO cellular component suggestions:** presynaptic active zone; synaptic ribbon; mitochondrion; myelin sheath.

---

## 8. Temporal development
### 8.1 Onset patterns
ANSD can be congenital/infant-onset or later onset; a large cohort suggests genetic spectra differ by onset age, with OTOF predominating in infants and AIFM1 in non-infants. (wang2024clinicalandgenetic pages 1-3).

### 8.2 Progression
Natural history can include stability, improvement, or deterioration; in the large cohort, some cases showed progressive worsening and loss of OAEs over time, with progressive decline in speech recognition. (wang2024clinicalandgenetic pages 12-14).

### 8.3 Critical periods
Intervention timing is emphasized indirectly by evidence that early cochlear implantation and longer CI use predict better outcomes in pediatric ANSD. (jafari2024predictorsofcochlear pages 1-2).

---

## 9. Inheritance and population
### 9.1 Epidemiology (recent/quantitative)
Key statistics from recent cohorts are summarized in artifact-00. Notable points include:
- AN affects 1.2–8.4% of hearing loss cases across populations and 0.006–0.039% in low-risk newborns (as cited in Wang et al. 2024). (wang2024clinicalandgenetic pages 1-3)
- In one CI cohort, **9.85% (of 1,025 children with SNHL)** were identified as ANSD (Almishaal et al. 2022 referenced in Wu et al. 2023). (wu2023outcomesofcochlear pages 1-2)
- A 2024 pediatric CI paper reports ANSD is observed in 4–5% of all degrees of hearing loss and 10–15% of school-age children with severe-to-profound SNHL. (jafari2024predictorsofcochlear pages 1-2)

### 9.2 Inheritance patterns
Inheritance patterns are diverse: autosomal recessive (e.g., OTOF, PJVK), autosomal dominant (e.g., OPA1, ATP1A3, DIAPH3), X-linked (AIFM1, PRPS1), and mitochondrial. (jafari2024predictorsofcochlear pages 1-2, wang2024clinicalandgenetic pages 1-3).

### 9.3 Population genetics / variant distribution
The retrieved sources did not provide gnomAD-based allele frequencies for specific variants; however, the Wang 2024 study documents filtering variants at population frequency <0.005 using gnomAD/1000G/ExAC in its sequencing pipeline. (wang2024clinicalandgenetic pages 3-4).

---

## 10. Diagnostics
### 10.1 Clinical diagnostic criteria
A large cohort study states inclusion criteria for AN as: (1) presence of OAE and/or CM and (2) abnormal or absent ABR. (wang2024clinicalandgenetic pages 3-4).

A 2023 gene therapy-focused review reiterates the hallmark profile: preserved OAE or CM with impaired/absent ABR, often with absent stapedial reflex and absent contralateral OAE suppression. (saidia2023currentadvancesin pages 1-3).

### 10.2 Genetic testing
Large cohort sequencing using WGS/panels identified pathogenic/likely pathogenic variants in 31.5% overall, with higher yields in trios/families than proband-only cases, supporting family-based sequencing when feasible. (wang2024clinicalandgenetic pages 1-3).

### 10.3 Differential diagnosis considerations
Cochlear nerve deficiency (CND) is an important anatomic/etiologic subgroup and is associated with poorer CI speech outcomes in a CI cohort. (wu2023outcomesofcochlear pages 3-5).

### 10.4 Screening and implementation
**Newborn screening limitation:** ANSD may be missed by screening strategies that rely primarily on OAEs, because OAEs can be preserved in ANSD; a large cohort also highlights dependence on OAE/CM and ABR for diagnosis. (wang2024clinicalandgenetic pages 3-4, saidia2023currentadvancesin pages 1-3).

---

## 11. Outcome / prognosis
### 11.1 Prognostic factors
**Cochlear nerve integrity:** CI outcomes are poorer in AN cases with cochlear nerve deficiency (p=0.008). (wu2023outcomesofcochlear pages 1-2).

**Intervention timing and exposure:** In a matched case-control pediatric study, improved speech perception outcomes were predicted by longer follow-up with CI, lower age at CI activation, and use of bilateral CIs; younger hearing-aid fitting age also correlated with better improvement. (jafari2024predictorsofcochlear pages 1-2).

### 11.2 Functional outcomes
In a 2023 CI cohort of 75 AN patients, post-CI aided thresholds improved to ~32–38 dB and CAP/SIR scores improved significantly in both prelingual and post-lingual onset groups. (wu2023outcomesofcochlear pages 1-2).

---

## 12. Treatment
### 12.1 Standard clinical management
Current clinical treatment options are commonly described as **hearing aids** and **cochlear implantation**, with outcomes depending on lesion site and cochlear nerve integrity. (saidia2023currentadvancesin pages 1-3, wu2023outcomesofcochlear pages 1-2).

### 12.2 Cochlear implantation: outcomes and predictors (recent data)
**Human cohort outcomes (Wu et al. 2023):**
- Aided thresholds after CI: prelingual 38.25 ± 6.63 dB; post-lingual 32.58 ± 9.26 dB. (wu2023outcomesofcochlear pages 1-2)
- CAP and SIR improvements were significant (p<0.001). (wu2023outcomesofcochlear pages 1-2)
- Maximum speech recognition ranged 58–93% (prelingual) and 43–98% (post-lingual). (wu2023outcomesofcochlear pages 1-2)

**Predictors (Jafari et al. 2024):**
- Children with ANSD achieved similar open-set speech perception outcomes as matched SNHL peers (average scores ~88.40%–95.65%). (jafari2024predictorsofcochlear pages 1-2)
- Predictors of optimal outcomes: longer CI follow-up, younger activation age, and two CIs. (jafari2024predictorsofcochlear pages 1-2)

**MAXO suggestions:** cochlear implantation; hearing aid therapy; audiologic rehabilitation; speech-language therapy.

### 12.3 Emerging / experimental: OTOF gene therapy and enabling natural history
Multiple OTOF-targeted intracochlear AAV programs are in Phase 1/2 clinical development:

- **Akouos/Lilly AAVAnc80-hOTOF trial (NCT05821959)**: first posted 2023-04-20; start 2023-09-15; primary endpoint safety (AEs) through ~1 year; secondary endpoints include ABR threshold change; includes participants with ≥2 OTOF mutations, profound bilateral SNHL by ABR, and preserved DPOAEs. (NCT05821959 chunk 1)
- **Regeneron (Decibel-origin) DB-OTO CHORD trial (NCT05788536)**: first posted 2023-03-29; start 2023-06-27; primary endpoints include TEAEs and achievement of PTA ≤70 dB (up to week 104); secondary endpoints include ABR to click and early speech perception milestones. (NCT05788536 chunk 1)
- **Long-term follow-up after AAVAnc80-hOTOF (NCT06696456)**: first posted 2024-11-20; monitors delayed safety and durability up to ~5 years post dosing. (NCT06696456 chunk 1)
- **OTOF natural history study (NCT05572073)**: first posted 2022-10-07; longitudinal ABR/OAE outcomes; excludes cochlear nerve deficiency/dysplasia and requires OTOF mutations; prospective phase requires OAE/CM present with absent/abnormal ABR in at least one non-implanted ear. (NCT05572073 chunk 1)

**Expert synthesis:** Recent reviews emphasize that current care remains device-based (HA/CI) and that gene therapy approaches are motivated by the ability to precisely localize lesion site and target presynaptic synaptopathy; preclinical outcomes depend strongly on timing of delivery. (saidia2023currentadvancesin pages 1-3, saidia2023currentadvancesin pages 11-12).

---

## 13. Prevention
No primary-prevention interventions specific to genetic ANSD are identified in the retrieved sources. Secondary prevention aligns with early detection (ABR-based components in newborn screening and early diagnostic workup) and early intervention (hearing technology, CI candidacy assessment), which are supported by evidence that younger intervention timing predicts better outcomes. (jafari2024predictorsofcochlear pages 1-2).

---

## 14. Other species / natural disease
The retrieved sources did not provide naturally occurring non-human (e.g., veterinary) disease evidence for ANSD.

---

## 15. Model organisms
### 15.1 Mouse models
- **OTOF/DFNB9 models:** Otof−/− mice show progressive synapse loss (from ~15 synapses/IHC at P14 to ~6 by 48 weeks) plus SGN decline and progressive hair-cell degeneration, with high-frequency DPOAE amplitude decay first observed at ~24 weeks. (stalmann2021otoferlinisrequired pages 1-2)
- **AIFM1/AUNX1 model:** Aifm1 p.R450Q KI mice recapitulate progressive auditory neuropathy with onset around P30, ribbon loss (P60), later demyelination, and mitochondrial pathology. (shi2024aiftranslocationinto pages 1-3)
- **PJVK models and gene transfer:** Pjvk mutant mice show cochlear and vestibular pathology; Anc80L65-mediated PJVK gene transfer partially restores hearing and normalizes vestibular function in mice. (lu2022genetherapywith pages 1-2)

### 15.2 Cellular models
- **Patient iPSC-derived neurons (AIFM1):** mechanism implicates mitochondrial Ca2+ overload, ROS elevation, and caspase-independent apoptosis; correction rescues phenotypes. (qiu2023impairedaifchchd4interaction pages 1-2)

---

## Direct abstract quotes supporting key claims (selected)
1) **Lesion-site spectrum and definition:** “Auditory neuropathy spectrum disorder (ANSD) refers to a range of hearing impairments characterized by an impaired transmission of sound from the cochlea to the brain.” (Saidia et al., 2023; abstract) (saidia2023currentadvancesin pages 3-4).

2) **Large-cohort genetic yield:** “In a retrospective cohort of 311 patients with AN, pathogenic and likely pathogenic variants of 23 genes were identified in 98 patients (31.5% in 311 patients)… Most of the OTOF gene (96.6%, 28/29) could only be identified in the infant group, while the AIFM1 gene could only be identified in the non-infant group.” (Wang et al., 2024; abstract) (wang2024clinicalandgenetic pages 1-3).

3) **CI outcomes in AN:** “After CI, the average aided hearing threshold for patients with prelingual and post-lingual onset was 38.25 ± 6.63 dB and 32.58 ± 9.26 dB, respectively… Speech outcomes of CI in cases with cochlear nerve (CN) deficiency were significantly poorer (p = 0.008).” (Wu et al., 2023; abstract) (wu2023outcomesofcochlear pages 1-2).

4) **AIFM1 iPSC mechanism and conclusion:** “This study demonstrates that the AIFM1 variant is one of the molecular bases of ANSD. Mitochondrial dysfunction, especially mCa2+ overload, plays a prominent role in ANSD associated with AIFM1.” (Qiu et al., 2023; abstract) (qiu2023impairedaifchchd4interaction pages 1-2).

---

## Limitations of this evidence set
- Formal ontology identifiers (MONDO, Orphanet, ICD, MeSH) were not present in the retrieved documents and were not inferred. (wang2024clinicalandgenetic pages 3-4).
- Variant-level population frequencies (gnomAD allele frequencies per variant) and penetrance/expressivity estimates by gene were not available in the retrieved texts.
- Some 2023–2024 high-impact ANSD management/outcomes papers were flagged as “unobtainable” by the paper retrieval system; therefore, this report prioritizes the accessible primary evidence and trial registry entries.

---

## Key URLs (access points)
- Wang et al. 2024 (*Human Genetics*): https://doi.org/10.1007/s00439-024-02652-7 (Published online 2024-03-08) (wang2024clinicalandgenetic pages 1-3)
- Wu et al. 2023 (*Frontiers in Neuroscience*): https://doi.org/10.3389/fnins.2023.1281884 (2023-11-13) (wu2023outcomesofcochlear pages 1-2)
- Jafari et al. 2024 (*PLOS ONE*): https://doi.org/10.1371/journal.pone.0304316 (2024-05-29) (jafari2024predictorsofcochlear pages 1-2)
- Saidia et al. 2023 (*J Clin Med*): https://doi.org/10.3390/jcm12030738 (2023-01) (saidia2023currentadvancesin pages 1-3)
- Forli et al. 2023 (*Medicina*): https://doi.org/10.3390/medicina59020352 (2023-02-13) (forli2023temperaturesensitiveauditoryneuropathy pages 1-2)
- Qiu et al. 2023 (*Cell Death & Disease*): https://doi.org/10.1038/s41419-023-05899-6 (2023-06) (qiu2023impairedaifchchd4interaction pages 1-2)
- Shi et al. 2024 (*Hum Mol Genet*): https://doi.org/10.1093/hmg/ddae010 (2024-03) (shi2024aiftranslocationinto pages 1-3)
- ClinicalTrials.gov NCT05821959: https://clinicaltrials.gov/study/NCT05821959 (First posted 2023-04-20) (NCT05821959 chunk 1)
- ClinicalTrials.gov NCT05788536: https://clinicaltrials.gov/study/NCT05788536 (First posted 2023-03-29) (NCT05788536 chunk 1)
- ClinicalTrials.gov NCT06696456: https://clinicaltrials.gov/study/NCT06696456 (First posted 2024-11-20) (NCT06696456 chunk 1)
- ClinicalTrials.gov NCT05572073: https://clinicaltrials.gov/study/NCT05572073 (First posted 2022-10-07) (NCT05572073 chunk 1)


References

1. (wang2024clinicalandgenetic pages 3-4): Hongyang Wang, Liping Guan, Xiaonan Wu, Jing Guan, Jin Li, Nan Li, Kaili Wu, Ya Gao, Dan Bing, Jianguo Zhang, Lan Lan, Tao Shi, Danyang Li, Wenjia Wang, Linyi Xie, Fen Xiong, Wei Shi, Lijian Zhao, Dayong Wang, Ye Yin, and Qiuju Wang. Clinical and genetic architecture of a large cohort with auditory neuropathy. Human Genetics, 143:293-309, Mar 2024. URL: https://doi.org/10.1007/s00439-024-02652-7, doi:10.1007/s00439-024-02652-7. This article has 19 citations and is from a peer-reviewed journal.

2. (wu2023outcomesofcochlear pages 1-2): Jie Wu, Jiyue Chen, Zhiwei Ding, Jialin Fan, Qiuquan Wang, Pu Dai, and Dongyi Han. Outcomes of cochlear implantation in 75 patients with auditory neuropathy. Frontiers in Neuroscience, Nov 2023. URL: https://doi.org/10.3389/fnins.2023.1281884, doi:10.3389/fnins.2023.1281884. This article has 7 citations and is from a peer-reviewed journal.

3. (saidia2023currentadvancesin pages 1-3): Anissa Rym Saidia, Jérôme Ruel, Amel Bahloul, Benjamin Chaix, Frédéric Venail, and Jing Wang. Current advances in gene therapies of genetic auditory neuropathy spectrum disorder. Journal of Clinical Medicine, 12:738, Jan 2023. URL: https://doi.org/10.3390/jcm12030738, doi:10.3390/jcm12030738. This article has 32 citations.

4. (lin2020anintegrativeapproach pages 2-3): Pei-Hsuan Lin, Chuan-Jen Hsu, Yin-Hung Lin, Yi-Hsin Lin, Shu-Yu Yang, Ting-Hua Yang, Pei-Lung Chen, Chen-Chi Wu, and Tien-Chen Liu. An integrative approach for pediatric auditory neuropathy spectrum disorders: revisiting etiologies and exploring the prognostic utility of auditory steady-state response. Scientific Reports, Jun 2020. URL: https://doi.org/10.1038/s41598-020-66877-y, doi:10.1038/s41598-020-66877-y. This article has 23 citations and is from a peer-reviewed journal.

5. (wang2024clinicalandgenetic pages 1-3): Hongyang Wang, Liping Guan, Xiaonan Wu, Jing Guan, Jin Li, Nan Li, Kaili Wu, Ya Gao, Dan Bing, Jianguo Zhang, Lan Lan, Tao Shi, Danyang Li, Wenjia Wang, Linyi Xie, Fen Xiong, Wei Shi, Lijian Zhao, Dayong Wang, Ye Yin, and Qiuju Wang. Clinical and genetic architecture of a large cohort with auditory neuropathy. Human Genetics, 143:293-309, Mar 2024. URL: https://doi.org/10.1007/s00439-024-02652-7, doi:10.1007/s00439-024-02652-7. This article has 19 citations and is from a peer-reviewed journal.

6. (jafari2024predictorsofcochlear pages 1-2): Zahra Jafari, Elizabeth M. Fitzpatrick, David R. Schramm, Isabelle Rouillon, and Amineh Koravand. Predictors of cochlear implant outcomes in pediatric auditory neuropathy: a matched case-control study. PLOS ONE, 19:e0304316, May 2024. URL: https://doi.org/10.1371/journal.pone.0304316, doi:10.1371/journal.pone.0304316. This article has 7 citations and is from a peer-reviewed journal.

7. (smith2018cochlearmicrophonicsfrom pages 17-21): Kyle Smith. Cochlear microphonics from auditory brainstem responses of infants with auditory neuropathy spectrum disorder. ArXiv, Jan 2018. URL: https://doi.org/10.14288/1.0372052, doi:10.14288/1.0372052. This article has 1 citations.

8. (wang2024clinicalandgenetic pages 12-14): Hongyang Wang, Liping Guan, Xiaonan Wu, Jing Guan, Jin Li, Nan Li, Kaili Wu, Ya Gao, Dan Bing, Jianguo Zhang, Lan Lan, Tao Shi, Danyang Li, Wenjia Wang, Linyi Xie, Fen Xiong, Wei Shi, Lijian Zhao, Dayong Wang, Ye Yin, and Qiuju Wang. Clinical and genetic architecture of a large cohort with auditory neuropathy. Human Genetics, 143:293-309, Mar 2024. URL: https://doi.org/10.1007/s00439-024-02652-7, doi:10.1007/s00439-024-02652-7. This article has 19 citations and is from a peer-reviewed journal.

9. (wu2023outcomesofcochlear pages 3-5): Jie Wu, Jiyue Chen, Zhiwei Ding, Jialin Fan, Qiuquan Wang, Pu Dai, and Dongyi Han. Outcomes of cochlear implantation in 75 patients with auditory neuropathy. Frontiers in Neuroscience, Nov 2023. URL: https://doi.org/10.3389/fnins.2023.1281884, doi:10.3389/fnins.2023.1281884. This article has 7 citations and is from a peer-reviewed journal.

10. (jafari2024predictorsofcochlear pages 2-4): Zahra Jafari, Elizabeth M. Fitzpatrick, David R. Schramm, Isabelle Rouillon, and Amineh Koravand. Predictors of cochlear implant outcomes in pediatric auditory neuropathy: a matched case-control study. PLOS ONE, 19:e0304316, May 2024. URL: https://doi.org/10.1371/journal.pone.0304316, doi:10.1371/journal.pone.0304316. This article has 7 citations and is from a peer-reviewed journal.

11. (buianova2024heterogeneousgroupof pages 7-9): Anastasiia A. Buianova, Marina V. Bazanova, Vera A. Belova, Galit A. Ilyina, Alina F. Samitova, Anna O. Shmitko, Anna V. Balakina, Anna S. Pavlova, Oleg N. Suchalko, Dmitriy O. Korostin, Anton S. Machalov, Nikolai A. Daikhes, and Denis V. Rebrikov. Heterogeneous group of genetically determined auditory neuropathy spectrum disorders. International Journal of Molecular Sciences, 25:12554, Nov 2024. URL: https://doi.org/10.3390/ijms252312554, doi:10.3390/ijms252312554. This article has 2 citations.

12. (buianova2024heterogeneousgroupof pages 2-3): Anastasiia A. Buianova, Marina V. Bazanova, Vera A. Belova, Galit A. Ilyina, Alina F. Samitova, Anna O. Shmitko, Anna V. Balakina, Anna S. Pavlova, Oleg N. Suchalko, Dmitriy O. Korostin, Anton S. Machalov, Nikolai A. Daikhes, and Denis V. Rebrikov. Heterogeneous group of genetically determined auditory neuropathy spectrum disorders. International Journal of Molecular Sciences, 25:12554, Nov 2024. URL: https://doi.org/10.3390/ijms252312554, doi:10.3390/ijms252312554. This article has 2 citations.

13. (forli2023temperaturesensitiveauditoryneuropathy pages 1-2): Francesca Forli, Silvia Capobianco, Stefano Berrettini, Luca Bruschini, Silvia Romano, Antonella Fogli, Veronica Bertini, and Francesco Lazzerini. Temperature-sensitive auditory neuropathy: report of a novel variant of otof gene and review of current literature. Medicina, 59:352, Feb 2023. URL: https://doi.org/10.3390/medicina59020352, doi:10.3390/medicina59020352. This article has 8 citations.

14. (dmitriev2023predictingtheimpact pages 1-2): Dmitry A. Dmitriev, Boris V. Shilov, Michail M. Polunin, Anton D. Zadorozhny, and Alexey A. Lagunin. Predicting the impact of otof gene missense variants on auditory neuropathy spectrum disorder. International Journal of Molecular Sciences, 24:17240, Dec 2023. URL: https://doi.org/10.3390/ijms242417240, doi:10.3390/ijms242417240. This article has 6 citations.

15. (NCT05821959 chunk 1):  Gene Therapy Trial for Otoferlin Gene-mediated Hearing Loss. Akouos, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05821959

16. (NCT05788536 chunk 1):  A Study of DB-OTO, an Adeno-Associated Virus (AAV) Based Gene Therapy, in Children/Infants With Hearing Loss Due to Otoferlin Mutations. Regeneron Pharmaceuticals. 2023. ClinicalTrials.gov Identifier: NCT05788536

17. (NCT05788536 chunk 2):  A Study of DB-OTO, an Adeno-Associated Virus (AAV) Based Gene Therapy, in Children/Infants With Hearing Loss Due to Otoferlin Mutations. Regeneron Pharmaceuticals. 2023. ClinicalTrials.gov Identifier: NCT05788536

18. (NCT06696456 chunk 1):  Long Term Follow-up Study of AAVAnc80-hOTOF Gene Therapy. Akouos, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06696456

19. (NCT05572073 chunk 1):  Otoferlin Gene-mediated Hearing Loss Natural History Study. Akouos, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05572073

20. (saidia2023currentadvancesin pages 3-4): Anissa Rym Saidia, Jérôme Ruel, Amel Bahloul, Benjamin Chaix, Frédéric Venail, and Jing Wang. Current advances in gene therapies of genetic auditory neuropathy spectrum disorder. Journal of Clinical Medicine, 12:738, Jan 2023. URL: https://doi.org/10.3390/jcm12030738, doi:10.3390/jcm12030738. This article has 32 citations.

21. (stalmann2021otoferlinisrequired pages 1-2): Ursula Stalmann, Albert Justin Franke, Hanan Al-Moyed, Nicola Strenzke, and Ellen Reisinger. Otoferlin is required for proper synapse maturation and for maintenance of inner and outer hair cells in mouse models for dfnb9. Frontiers in Cellular Neuroscience, Jul 2021. URL: https://doi.org/10.3389/fncel.2021.677543, doi:10.3389/fncel.2021.677543. This article has 45 citations.

22. (shi2024aiftranslocationinto pages 1-3): Tao Shi, Ziyi Chen, Jin Li, Hongyang Wang, and Qiuju Wang. Aif translocation into nucleus caused by aifm1 r450q mutation: generation and characterization of a mouse model for aunx1. Human Molecular Genetics, 33:905-918, Mar 2024. URL: https://doi.org/10.1093/hmg/ddae010, doi:10.1093/hmg/ddae010. This article has 3 citations and is from a domain leading peer-reviewed journal.

23. (qiu2023impairedaifchchd4interaction pages 1-2): Yue Qiu, Hongyang Wang, Mingjie Fan, Huaye Pan, J. Guan, Yangwei Jiang, Zexiao Jia, Kaiwen Wu, Hui Zhou, Qianqian Zhuang, Zhaoying Lei, Xue Ding, Huajian Cai, Yufei Dong, Le-Qin Yan, Aifu Lin, Yong Fu, Dong Zhang, Qingfeng Yan, and Qiuju Wang. Impaired aif-chchd4 interaction and mitochondrial calcium overload contribute to auditory neuropathy spectrum disorder in patient-ipsc-derived neurons with aifm1 variant. Cell Death &amp; Disease, Jun 2023. URL: https://doi.org/10.1038/s41419-023-05899-6, doi:10.1038/s41419-023-05899-6. This article has 20 citations and is from a peer-reviewed journal.

24. (ismail2024systematicreviewof pages 2-4): Naema Mohamed Ismail, Salma Badreldin Galal, Reda Mohamed Behairy, and Rasha Mohamed Sabry. Systematic review of outcomes of cochlear implantation of different genotypes in patients with auditory neuropathy spectrum disorder. The Egyptian Journal of Otolaryngology, Sep 2024. URL: https://doi.org/10.1186/s43163-024-00677-3, doi:10.1186/s43163-024-00677-3. This article has 2 citations.

25. (lu2022genetherapywith pages 1-2): Ying-Chang Lu, Yi-Hsiu Tsai, Yen-Huei Chan, Chin-Ju Hu, Chun-Ying Huang, Ru Xiao, Chuan-Jen Hsu, Luk H. Vandenberghe, Chen-Chi Wu, and Yen-Fu Cheng. Gene therapy with a synthetic adeno-associated viral vector improves audiovestibular phenotypes in pjvk-mutant mice. JCI Insight, Oct 2022. URL: https://doi.org/10.1172/jci.insight.152941, doi:10.1172/jci.insight.152941. This article has 24 citations and is from a domain leading peer-reviewed journal.

26. (saidia2023currentadvancesin pages 11-12): Anissa Rym Saidia, Jérôme Ruel, Amel Bahloul, Benjamin Chaix, Frédéric Venail, and Jing Wang. Current advances in gene therapies of genetic auditory neuropathy spectrum disorder. Journal of Clinical Medicine, 12:738, Jan 2023. URL: https://doi.org/10.3390/jcm12030738, doi:10.3390/jcm12030738. This article has 32 citations.