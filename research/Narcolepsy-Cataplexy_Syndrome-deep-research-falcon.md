---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T12:34:08.849668'
end_time: '2026-05-11T12:56:00.410399'
duration_seconds: 1311.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Narcolepsy-Cataplexy Syndrome
  mondo_id: ''
  category: Neurological
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Narcolepsy-Cataplexy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Neurological

## Research Objectives

Please provide a comprehensive research report on **Narcolepsy-Cataplexy Syndrome** covering all of the
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
- **Disease Name:** Narcolepsy-Cataplexy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Neurological

## Research Objectives

Please provide a comprehensive research report on **Narcolepsy-Cataplexy Syndrome** covering all of the
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


# Narcolepsy–Cataplexy Syndrome (Narcolepsy Type 1, NT1): Comprehensive Disease Characteristics Report (2023–2024 emphasis)

## Scope and evidence note
This report focuses on **narcolepsy-cataplexy syndrome**, which aligns clinically with **narcolepsy type 1 (NT1)** (historically “narcolepsy with cataplexy”). Evidence was extracted from recent peer‑reviewed reviews, a 2023 multi‑ethnic GWAS, a 2024 high‑resolution HLA study, a 2024 preclinical orexin receptor agonist paper, and ClinicalTrials.gov records (registry years 2023–2026). Several requested identifiers (MONDO, MeSH, ICD‑10/ICD‑11, OMIM) and many PMIDs were **not present in retrieved sources**; these gaps are explicitly marked.

## 1. Disease information
### 1.1 Definition and overview
NT1 is a **rare chronic central disorder of hypersomnolence** characterized by **excessive daytime sleepiness (EDS)** and **cataplexy** and is strongly linked to **hypocretin/orexin deficiency** from loss of orexin-producing hypothalamic neurons. (baldini2024pediatricnarcolepsytype pages 1-2, coelho2024narcolepsyaninterface pages 2-3)

### 1.2 Names and synonyms
Key naming harmonization in recent sources:
- **Narcolepsy type 1 (NT1)** (baldini2024pediatricnarcolepsytype pages 1-2)
- **Narcolepsy with cataplexy** (older term mapped to NT1) (matota2023exploringtheliterature pages 1-2)
- **Narcolepsy-cataplexy syndrome** (explicit terminology used in a 2024 narrative review) (coelho2024narcolepsyaninterface pages 2-3)

### 1.3 Key identifiers (ontology/coding)
- **Orphanet**: **ORPHA:619284** is cited in a 2023 review as a narcolepsy group identifier. (matota2023exploringtheliterature pages 1-2)
- **Not found in retrieved evidence**: MONDO ID, MeSH descriptor ID, ICD‑10/ICD‑11 codes, OMIM IDs.

### 1.4 Evidence source type
The information summarized here is primarily derived from **aggregated disease-level resources** (reviews, GWAS, registry trials), not individual EHR-only cohorts; however, the GWAS includes large population biobank components and multi-center case collections. (ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 6-7)

| Item | Value | Source (with DOI/URL) | Publication date | Evidence citation id |
|---|---|---|---|---|
| Disease name / synonym | Narcolepsy type 1 (NT1) | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| Disease name / synonym | Narcolepsy with cataplexy (former terminology for NT1) | Mațotă et al., *NeuroSci*; DOI: 10.3390/neurosci4040022; https://doi.org/10.3390/neurosci4040022 | 2023-10 | (matota2023exploringtheliterature pages 1-2) |
| Disease name / synonym | Narcolepsy-cataplexy syndrome | Coelho, *Arquivos de Neuro-Psiquiatria*; DOI: 10.1055/s-0044-1779299; https://doi.org/10.1055/s-0044-1779299 | 2024-04 | (coelho2024narcolepsyaninterface pages 2-3) |
| Classification | Rare chronic central disorder of hypersomnolence | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| Key identifier | Orphanet: ORPHA:619284 | Mațotă et al., *NeuroSci*; DOI: 10.3390/neurosci4040022; https://doi.org/10.3390/neurosci4040022 | 2023-10 | (matota2023exploringtheliterature pages 1-2) |
| ICSD-3-TR diagnostic element | Excessive daytime sleepiness / irrepressible need to sleep or daytime lapses for at least 3 months | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| ICSD-3-TR diagnostic element | Cataplexy as a core diagnostic feature for NT1 | Coelho, *Arquivos de Neuro-Psiquiatria*; DOI: 10.1055/s-0044-1779299; https://doi.org/10.1055/s-0044-1779299 | 2024-04 | (coelho2024narcolepsyaninterface pages 2-3) |
| ICSD-3-TR diagnostic element | Low CSF hypocretin-1 / orexin-A: ≤110 pg/mL or less than one-third of normal mean values | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| ICSD-3-TR diagnostic element | MSLT mean sleep latency ≤8 minutes | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| ICSD-3-TR diagnostic element | MSLT shows ≥2 sleep-onset REM periods (SOREMPs) | Baldini et al., *Clinical and Translational Neuroscience*; DOI: 10.3390/ctn8030025; https://doi.org/10.3390/ctn8030025 | 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| ICSD-3-TR diagnostic element | Overnight polysomnography (PSG) should precede MSLT | Coelho, *Arquivos de Neuro-Psiquiatria*; DOI: 10.1055/s-0044-1779299; https://doi.org/10.1055/s-0044-1779299 | 2024-04 | (coelho2024narcolepsyaninterface pages 2-3) |


*Table: This table summarizes the core disease names, classification, available identifier, and ICSD-3-TR diagnostic elements for narcolepsy-cataplexy syndrome / narcolepsy type 1. It is useful as a compact reference for nomenclature harmonization and diagnosis-oriented knowledge-base entry building.*

## 2. Etiology
### 2.1 Primary causal factors (current understanding)
**Current consensus model:** NT1 arises from **selective loss of hypocretin/orexin (HCRT) neurons in the lateral hypothalamus** in genetically predisposed individuals, most consistent with an **immune-mediated (autoimmune) mechanism**, where **T cells** are strongly implicated. (coelho2024narcolepsyaninterface pages 2-3, xu2024theroleof pages 5-7, xu2024theroleof pages 1-2)

**Direct abstract-level support (quote):** A 2024 T-cell–focused narrative review states, “**The strong association between narcolepsy and the HLA-DQB1*06:02 allele strongly indicates an autoimmune etiology**…” and that “**Increasing evidence suggests that T cells play a critical role**…” (xu2024theroleof pages 1-2)

### 2.2 Genetic risk factors
#### HLA (major effect)
- NT1 shows strong association with **HLA-DQB1*06:02** in multiple sources. (baldini2024pediatricnarcolepsytype pages 1-2, coelho2024narcolepsyaninterface pages 2-3)
- **High-resolution HLA sequencing (2024)** quantified the association for **DQB1*06:02:01** with **OR 7.27** (95% CI 4.11–12.85; p=6.11×10^-15) and related class II alleles (DRB5*01:01:01, DRB1*15:01:01, DQA1*01:02:01). (hamdan2024high‐resolutionhlasequencing pages 3-4)
- The same 2024 study found the extended haplotype **DRB5*01:01:01–DRB1*15:01:01–DQA1*01:02:01–DQB1*06:02:01** enriched in NT1 (55.8% vs 15.3% in population controls; OR 7.01; p=1.98×10^-14). (hamdan2024high‐resolutionhlasequencing pages 4-5)

#### Non-HLA loci (2023 multi-ethnic GWAS)
A 2023 Nature Communications GWAS/meta-analysis (multi-ethnic) reports:
- Sample size: **6,073 NT1 cases and 84,856 controls**; plus a **Pandemrix® vaccination-related** subcohort of **245 cases** and **18,862 controls**. (ollila2023narcolepsyriskloci pages 6-7, ollilaUnknownyearmbati.ogeshwarsm… pages 7-8)
- Fine-mapped HLA signals including **DQ0602 (DQB1*06:02)** and additional signals (e.g., **DQB1*03:01, DPB1*04:02**). (ollila2023narcolepsyriskloci pages 1-2)
- Confirmed known immune loci (e.g., **TRA, TRB, CTSH, IFNAR1, ZNF365, TNFSF4**) and identified **seven novel loci** (**CD207, NAB1, IKZF4-ERBB3, CTSC, DENND1B, SIRPG, PRF1**). (ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 5-6)
- T-cell receptor usage effects implicating **TRAJ*24, TRAJ*28 and TRBV4-2**, consistent with antigen-specific, restricted TCR involvement. (ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 5-6)

### 2.3 Environmental/infectious risk factors (triggers)
- A 2024 review summarizes increased NT1 prevalence/incidence after **influenza A(H1N1)pdm09** and after **Pandemrix®** vaccination, consistent with gene–environment interaction. (xu2024theroleof pages 1-2)
- The same review reports a large effect size for the post‑pandemic/vaccine association: **2–14× increases in NT1 incidence** temporally associated with H1N1/Pandemrix in specific settings. (xu2024theroleof pages 1-2)
- Pediatric NT1 review notes incidence “peaks” after H1N1 and a link to **elevated anti-streptolysin O titers**, supporting a possible role of **streptococcal infection** as a trigger in some patients. (baldini2024pediatricnarcolepsytype pages 1-2)

### 2.4 Protective factors
A specific set of “protective factors” (genetic or environmental) was not systematically enumerated in the retrieved clinical reviews; however, the 2023 GWAS includes alleles described as protective within HLA fine-mapping (e.g., protective HLA effects) in excerpts. (ollila2023narcolepsyriskloci pages 3-4)

### 2.5 Gene–environment interaction (current understanding)
The 2023 GWAS explicitly frames NT1 as shaped by **genetic risk variants** interacting with **influenza infection/vaccination contexts**, and vaccination-triggered cases share similar genetic architecture (notably HLA and TRA signals), implying that environmental triggers act on a common susceptibility background. (ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 5-6)

## 3. Phenotypes
### 3.1 Core phenotype spectrum
Commonly described NT1 symptom cluster includes:
- **EDS** (irrepressible need to sleep/lapses) (baldini2024pediatricnarcolepsytype pages 1-2)
- **Cataplexy** (emotion-triggered sudden muscle tone loss with preserved consciousness) (severin2023exploringtheliterature pages 8-9)
- **Disrupted nocturnal sleep / sleep fragmentation** (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9)
- **Sleep paralysis** (baldini2024pediatricnarcolepsytype pages 1-2)
- **Hypnagogic/hypnopompic hallucinations** (baldini2024pediatricnarcolepsytype pages 1-2)
- Pediatric comorbidities such as **obesity** and **precocious puberty**, plus psychological/psychiatric and cognitive issues. (baldini2024pediatricnarcolepsytype pages 1-2)

### 3.2 Age of onset and course
- NT1 often begins in **childhood/adolescence**; one review reports **>50% of cases begin before age 18** and onset is common between **10–30 years**. (severin2023exploringtheliterature pages 8-9)
- The course is generally **chronic**; functional and psychosocial burden is emphasized in pediatric and general reviews. (baldini2024pediatricnarcolepsytype pages 1-2, matota2023exploringtheliterature pages 1-2)

### 3.3 HPO mapping suggestions
| Phenotype | HPO term suggestion(s) | Key description/statistics | QoL/functional impact | Source URL/DOI + date | Evidence citation id |
|---|---|---|---|---|---|
| Excessive daytime sleepiness | HP:0001262 Excessive daytime somnolence; HP:0012449 Abnormality of sleep-wake cycle | Core NT1 feature; ICSD-3/ICSD-3-TR-based descriptions require irrepressible need to sleep/daytime lapses for ≥3 months. Typical onset is in childhood/adolescence or young adulthood; >50% of cases begin before age 18 in one review, and common onset is between 10–30 years. Severity is often chronic and disabling rather than self-limited. | Major impairment in school/work performance, attention, driving safety, and social functioning; described as substantially reducing quality of life in children and adults. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Mațotă 2023, https://doi.org/10.3390/neurosci4040022, 2023-10; Severin 2023, https://doi.org/10.20944/preprints202309.0819.v1, 2023-09 | (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9, matota2023exploringtheliterature pages 1-2) |
| Cataplexy | HP:0002524 Cataplexy | Hallmark phenotype of NT1; defined as sudden loss of muscle tone with preserved consciousness, usually lasting <2 minutes and often triggered by strong emotions, especially pleasant emotions. May be partial or generalized; episodic course. | Causes falls, injury risk, embarrassment, activity avoidance, and marked social/occupational restriction; strongly contributes to disease burden. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Severin 2023, https://doi.org/10.20944/preprints202309.0819.v1, 2023-09 | (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9) |
| Sleep paralysis | HP:0031466 Sleep paralysis | Common associated REM-related symptom in NT1; often begins around the same disease period as EDS/cataplexy and tends to recur episodically. Pediatric review lists it among core symptoms; adult review includes it in the classic symptom complex. Frequency not quantified in retrieved excerpts. | Distressing episodes can provoke anxiety, fear of sleep, and impaired sleep confidence. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Mațotă 2023, https://doi.org/10.3390/neurosci4040022, 2023-10 | (baldini2024pediatricnarcolepsytype pages 1-2, matota2023exploringtheliterature pages 1-2) |
| Hypnagogic/hypnopompic hallucinations | HP:0002473 Hallucinations; HP:0031464 Hypnagogic hallucinations; HP:0031465 Hypnopompic hallucinations | Frequently reported REM-intrusion symptoms in NT1; pediatric NT1 review lists both hypnagogic and hypnopompic hallucinations. Often episodic/fluctuating rather than progressive. Specific prevalence not given in retrieved excerpts. | Can be frightening and disruptive, worsening sleep-related anxiety and daily well-being. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Mațotă 2023, https://doi.org/10.3390/neurosci4040022, 2023-10 | (baldini2024pediatricnarcolepsytype pages 1-2, matota2023exploringtheliterature pages 1-2) |
| Disrupted nocturnal sleep / sleep fragmentation | HP:0002360 Sleep disturbance; HP:0031354 Fragmented sleep | Despite hypersomnolence, NT1 commonly includes disturbed nighttime sleep/sleep fragmentation. Reviews describe disrupted night sleep as a core associated feature in pediatric and adult NT1; course is chronic/fluctuating. | Leads to nonrestorative sleep, worsened daytime functioning, fatigue, and may exacerbate EDS/cognitive symptoms. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Severin 2023, https://doi.org/10.20944/preprints202309.0819.v1, 2023-09 | (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9) |
| Weight gain / obesity | HP:0001513 Obesity; HP:0001824 Weight gain | Frequently reported comorbidity, especially in pediatric NT1; review notes obesity as a common associated condition and adult review notes weight gain among associated features. Likely early in disease course in many children, though precise frequency is not stated in retrieved excerpts. | Contributes additional psychosocial burden and cardiometabolic risk, worsening overall quality of life. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Severin 2023, https://doi.org/10.20944/preprints202309.0819.v1, 2023-09 | (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9) |
| Precocious puberty (pediatric) | HP:0000826 Precocious puberty | Pediatric NT1 review identifies precocious puberty as a recognized comorbidity in children/adolescents. Pediatric onset is common, making this especially relevant for early-onset NT1. Frequency not provided in retrieved excerpts. | May affect psychosocial development and compound pediatric disease burden, requiring multidisciplinary follow-up. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06 | (baldini2024pediatricnarcolepsytype pages 1-2) |
| Cognitive / psychiatric comorbidity | HP:0100543 Cognitive impairment; HP:0000708 Behavioral abnormality; HP:0000739 Anxiety; HP:0000716 Depression | Pediatric NT1 review notes cognitive aspects, psychological distress, and psychiatric disorders as common comorbidities; broader review emphasizes significant effects on daily functioning and social life. Course is chronic and may fluctuate with sleepiness severity. | Important contributor to impaired academic achievement, work productivity, emotional well-being, and social functioning. | Baldini 2024, https://doi.org/10.3390/ctn8030025, 2024-06; Mațotă 2023, https://doi.org/10.3390/neurosci4040022, 2023-10 | (baldini2024pediatricnarcolepsytype pages 1-2, matota2023exploringtheliterature pages 1-2) |


*Table: This table maps major narcolepsy type 1 phenotypes to suggested HPO terms and summarizes key clinical characteristics, onset patterns, and quality-of-life impacts from recent reviews. It is useful for structured disease knowledge-base curation and phenotype annotation.*

## 4. Genetic / molecular information
### 4.1 “Causal genes” vs susceptibility loci
For most patients, NT1 is not presented as a single-gene Mendelian disorder in the retrieved evidence; instead, it is a complex disorder with **strong HLA susceptibility** and additional immune-related loci (GWAS). (ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 6-7)

### 4.2 Key susceptibility loci and immune effector biology
- **HLA-DQB1*06:02** (class II antigen presentation; strongest association). (hamdan2024high‐resolutionhlasequencing pages 3-4)
- **TCR loci (TRA/TRB)**: variants affecting chain usage (TRAJ24/28, TRBV4-2), supporting restricted antigen specificity. (ollila2023narcolepsyriskloci pages 5-6)
- Cytotoxic pathway genes highlighted in GWAS: **PRF1** (perforin) and **CTSC** (cathepsin C), consistent with **CD8+ T-cell cytotoxic mechanisms**. (ollila2023narcolepsyriskloci pages 1-2, ollilaUnknownyearmbati.ogeshwarsm… pages 6-7)

### 4.3 Epigenetics and chromosomal abnormalities
No epigenetic signatures or chromosomal abnormalities were extractable from retrieved sources.

## 5. Environmental information
The most consistently discussed environmental factors are infectious/vaccine triggers:
- Influenza A(H1N1)pdm09 infection and **Pandemrix®** vaccination. (xu2024theroleof pages 1-2)
- Streptococcal exposure suggested by anti-streptolysin O findings in pediatric contexts. (baldini2024pediatricnarcolepsytype pages 1-2)
Other toxins/radiation/pollution exposures were not described in the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (trigger → mechanism → clinical manifestations)
A convergent mechanistic chain described across recent reviews and GWAS-derived interpretations is:
1) **Genetic predisposition** (especially HLA-DQB1*06:02 and related immune loci). (hamdan2024high‐resolutionhlasequencing pages 3-4, ollila2023narcolepsyriskloci pages 1-2)
2) **Environmental trigger** (e.g., influenza infection or specific vaccinations) initiating or amplifying immune priming. (xu2024theroleof pages 1-2)
3) **Antigen presentation** to CD4+ T cells (HLA class II) and development of autoreactive T-cell repertoires (TRA/TRB associations). (xu2024theroleof pages 5-7, ollila2023narcolepsyriskloci pages 5-6)
4) **CNS infiltration/activation**: microglial activation and inflammatory cytokines/chemokines, with IFN-γ–driven upregulation of MHC I on neurons facilitating recognition. (xu2024theroleof pages 5-7)
5) **Selective destruction of hypocretin/orexin neurons** by **CD8+ cytotoxic T cells**, leading to **CSF hypocretin deficiency**. (xu2024theroleof pages 5-7, xu2024theroleof pages 3-5)
6) Downstream physiology: orexin deficiency destabilizes wakefulness and REM boundaries, producing **EDS**, **cataplexy**, and REM intrusion phenomena. (thomaz2024treatmentofnarcolepsy pages 1-2, coelho2024narcolepsyaninterface pages 2-3)

### 6.2 Immune system involvement (expert synthesis)
A 2024 narrative review emphasizes that neurons express HLA class I (enabling CD8 recognition), while microglia can express HLA class II, supporting a two-arm immune model: CD4-driven priming/help and CD8-mediated cytotoxicity. (xu2024theroleof pages 5-7)

**Key abstract quotes (supporting specificity):**
- “**T cells in patients with narcolepsy target self-antigens of hypocretin neurons**…” and affected children show “**increased T-cell responses to orexins**.” (xu2024theroleof pages 11-12)

### 6.3 Biomarkers
- **CSF hypocretin‑1/orexin‑A**: ≤**110 pg/mL** or **<1/3 of normal** is cited as a diagnostic biomarker threshold in ICSD-3-TR‑based descriptions. (baldini2024pediatricnarcolepsytype pages 1-2)
- Autoantibodies:
  - Anti‑hypocretin receptor 2 (**anti‑HCRTR2**) autoantibodies were **not different between groups** and overall low in a 2024 study (p=0.8524), arguing against HCRTR2 as a common autoimmune target. (hamdan2024high‐resolutionhlasequencing pages 6-6)

### 6.4 Suggested ontology terms (mechanism)
- GO (Biological Process) suggestions consistent with described mechanisms:
  - antigen processing and presentation
  - T cell activation / regulation
  - cytotoxicity-mediated killing (perforin/granzyme pathway)
  - cytokine-mediated signaling and neuroinflammation
(These GO mappings are interpretive alignments to described mechanisms, not explicitly enumerated in the retrieved papers.)

- CL (Cell Ontology) suggestions:
  - CD4+ T cell, CD8+ T cell, regulatory T cell
  - dendritic cell
  - microglial cell
  - orexin/hypocretin-producing neuron (hypothalamic)
(These CL mappings align to cell types explicitly discussed across recent reviews.) (xu2024theroleof pages 5-7, xu2024theroleof pages 1-2)

## 7. Anatomical structures affected
- Primary site: **lateral hypothalamus** with loss of **hypocretin/orexin neurons**. (coelho2024narcolepsyaninterface pages 2-3, thomaz2024treatmentofnarcolepsy pages 1-2)
- Systems involved: central nervous system sleep–wake regulation networks (monoaminergic/cholinergic arousal systems are referenced as orexin targets). (thomaz2024treatmentofnarcolepsy pages 1-2)

Suggested UBERON alignment:
- hypothalamus (UBERON term not explicitly provided in retrieved sources).

## 8. Temporal development
- Onset often in childhood/adolescence; chronic and persistent course is repeatedly emphasized. (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 8-9)
- Diagnostic delay: a 2024 review notes **“a delay of over ten years for the diagnosis of narcolepsy around the world.”** (coelho2024narcolepsyaninterface pages 2-3)

## 9. Inheritance and population
### 9.1 Epidemiology (recently cited numbers)
- Pediatric state-of-the-art review (2024) reports:
  - Global mean prevalence ~**30/100,000** with a wide range (Israel **0.23/100,000** to Japan **160/100,000**). (baldini2024pediatricnarcolepsytype pages 1-2)
  - European incidence for narcolepsy with cataplexy ~**0.74/100,000 person-years**. (baldini2024pediatricnarcolepsytype pages 1-2)
- A 2023 review reports prevalence ~**0.02–0.05%** overall and gives example ranges for NT1 prevalence (~**25–50/100,000**) depending on study/country. (severin2023exploringtheliterature pages 3-5)

### 9.2 Genetic architecture
Evidence supports complex, polygenic susceptibility with major HLA contribution, rather than simple Mendelian inheritance in most cases. (ollila2023narcolepsyriskloci pages 1-2, hamdan2024high‐resolutionhlasequencing pages 3-4)

## 10. Diagnostics
### 10.1 Clinical criteria and tests
ICSD-3-TR-aligned elements described in recent reviews include:
- Daily sleepiness (irrepressible need to sleep/lapses) for ≥3 months. (baldini2024pediatricnarcolepsytype pages 1-2)
- Objective testing: **overnight PSG** followed by **MSLT**, with MSLT criteria of **mean sleep latency ≤8 minutes** and **≥2 SOREMPs**. (baldini2024pediatricnarcolepsytype pages 1-2, coelho2024narcolepsyaninterface pages 2-3)
- Biomarker alternative/support: **CSF hypocretin‑1 ≤110 pg/mL** (or <1/3 normal mean) can support diagnosis. (baldini2024pediatricnarcolepsytype pages 1-2)

### 10.2 Differential diagnosis (limited in retrieved evidence)
Differential diagnosis details were not comprehensively extractable from the retrieved excerpts; however, comparisons to other central hypersomnolence disorders (e.g., NT2, idiopathic hypersomnia) appear in diagnostic discussions. (baldini2024pediatricnarcolepsytype pages 1-2, hamdan2024high‐resolutionhlasequencing pages 6-6)

### 10.3 Screening tools
- Swiss Narcolepsy Scale (SNS) is described as a screening tool; a 2023 validation study reports **sensitivity 90.5% and specificity 100%** for diagnosing NT1 in a Turkish validation cohort. (severin2023exploringtheliterature pages 9-11)

## 11. Outcomes / prognosis
- NT1 is described as chronic with substantial functional morbidity and comorbidities affecting quality of life. (baldini2024pediatricnarcolepsytype pages 1-2, coelho2024narcolepsyaninterface pages 2-3)
- Mortality and life expectancy statistics were not present in retrieved sources.

## 12. Treatment
### 12.1 Current pharmacotherapy (real-world implementation)
Recent review-level sources list common first-line therapies:
- For EDS: **modafinil/armodafinil, pitolisant, sodium oxybate**, and **solriamfetol** (dopamine/norepinephrine reuptake inhibitor). (severin2023exploringtheliterature pages 9-11)
- For cataplexy: **sodium oxybate**, **venlafaxine**, and **pitolisant**. (severin2023exploringtheliterature pages 9-11)

Non-pharmacological measures include sleep hygiene and planned naps, especially emphasized in pediatric management. (baldini2024pediatricnarcolepsytype pages 1-2, severin2023exploringtheliterature pages 9-11)

### 12.2 Low-sodium oxybate (LXB; real-world considerations)
Low-sodium oxybate (LXB) is positioned as a long-term therapy option with reduced sodium burden:
- Contains **92% less sodium** than sodium oxybate (SXB). (schneider2023longtermtreatmentof pages 3-5, schneider2023longtermtreatmentof pages 1-2)
- US approvals summarized in 2023 review: narcolepsy (cataplexy or EDS) age ≥7 years (July 2020) and idiopathic hypersomnia adults (August 2021). (schneider2023longtermtreatmentof pages 5-6)
- Randomized-withdrawal phase 3 narcolepsy results summarized: cataplexy worsened on placebo vs no change on LXB (P<0.0001) and ESS also favored LXB (P<0.0001). (schneider2023longtermtreatmentof pages 3-5)
- Safety statistics in that review: **TEAEs 76.1%**, **discontinuation for TEAEs 11.9%** (including worsening cataplexy and nausea). (schneider2023longtermtreatmentof pages 3-5)

### 12.3 2023–2024 frontier development: orexin receptor agonists (disease-modifying symptomatic strategy)
A major recent development is the maturation of **orexin receptor 2 (OX2R) agonists** intended to replace missing orexin signaling.

**TAK-861 (oral OX2R agonist; 2024 preclinical):**
- Reported OX2R potency **EC50 2.5 nM** and selectivity ~**3000×** over OX1R, with wake-promoting **minimum effective dose 1 mg/kg p.o.** (mice and monkeys), and suppression of cataplexy-like episodes in NT1 mouse models. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 9-10)
- Supporting figure/table evidence is present in the preclinical paper (Table 1 and Figure 3) as extracted images. (mitsukawa2024tak861apotent media 756d74c0, mitsukawa2024tak861apotent media cd11b0df)

**Danavorexton (TAK-925; parenteral OX2R agonist):**
- Summarized as increasing wakefulness in animals and in humans (sleep-deprived healthy individuals) and improving sleepiness/cataplexy in NT1, but with parenteral route limitations. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 9-10)

**TAK-994 (oral OX2R agonist):**
- Development reportedly stopped due to **risk of drug-induced liver injury/off-target liver toxicity** despite phase 2 improvement in wakefulness/cataplexy metrics. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 9-10)

### 12.4 Clinical trial landscape (selected real-world implementations)
**TAK-861 registry trials (ClinicalTrials.gov):**
- Phase 2 NT1 trial: **NCT05687903**, enrollment 112 actual; primary endpoint change in MWT sleep latency at Week 8; secondary includes ESS and weekly cataplexy rate. (NCT05687903 chunk 1)
- Phase 3 NT1 trials: **NCT06470828** (enrollment 168 actual; 12 weeks; primary = MWT mean sleep latency) and **NCT06505031** (enrollment 105 actual; 12 weeks; similar primary). (NCT06470828 chunk 1, NCT06505031 chunk 1)
- Randomized-withdrawal design trial: **NCT07363720** (Phase 3; planned enrollment 88; primary = time to loss of response on ESS; secondary includes MWT and cataplexy rate). (NCT07363720 chunk 1)

### 12.5 MAXO suggestions (treatment actions; interpretive mappings)
- Wake-promoting pharmacotherapy (e.g., modafinil/solriamfetol/pitolisant)
- Oxybate therapy (sodium oxybate / low-sodium oxybate)
- Orexin receptor agonist therapy (OX2R agonists)
- Behavioral sleep intervention (scheduled naps, sleep hygiene)
(These MAXO alignments are provided as practical KB mappings; MAXO IDs were not present in retrieved sources.)

## 13. Prevention
No established primary prevention is described in retrieved evidence. Practical mitigation strategies include:
- early recognition and diagnosis (to reduce multi-year delays) (coelho2024narcolepsyaninterface pages 2-3)
- avoidance of known safety risks associated with symptoms (e.g., driving risk) and symptom control through therapy and behavioral measures. (severin2023exploringtheliterature pages 9-11)

## 14. Other species / natural disease
Direct evidence for naturally occurring narcolepsy in non-human species (e.g., canine narcolepsy) was not present in the retrieved sources.

## 15. Model organisms
Recent mechanistic/treatment development relies heavily on orexin-deficient mouse models:
- Preclinical evaluation of TAK-861 used **orexin/ataxin-3** and **orexin‑tTA;TetO DTA** mouse models, demonstrating improved wakefulness fragmentation and reduced cataplexy-like episodes. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 4-7)
These models recapitulate key features of NT1 related to orexin deficiency and provide a translational platform for orexin receptor agonists.

---

# Expert interpretation and synthesis (authoritative analysis)
1) The **strong HLA-DQB1*06:02 effect** (now quantified with high-resolution HLA sequencing) supports a model where antigen presentation is central, but the broader GWAS pattern (TCR loci + APC/innate antiviral response genes) points to a **highly specific, oligoclonal adaptive immune response** rather than generalized inflammation. (hamdan2024high‐resolutionhlasequencing pages 3-4, ollila2023narcolepsyriskloci pages 1-2, ollila2023narcolepsyriskloci pages 5-6)
2) The 2023 GWAS and 2024 T-cell review jointly support **gene–environment coupling**, where influenza-related exposures amplify risk in genetically predisposed individuals; vaccination-related NT1 cases show similar risk architecture to sporadic NT1, consistent with shared biology. (ollila2023narcolepsyriskloci pages 1-2, xu2024theroleof pages 1-2)
3) Therapeutically, the field is shifting from symptomatic stimulants and REM-modulating agents toward **pathway replacement** via **OX2R agonists**, with TAK-861 designed to address prior oral-agent limitations (notably TAK-994 liver toxicity risk) through higher potency and lower effective dosing. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 9-10)

---

# Key recent statistics (quick reference)
- Prevalence mean ~**30/100,000** globally (range **0.23–160/100,000** by country) (2024 review). (baldini2024pediatricnarcolepsytype pages 1-2)
- Incidence for narcolepsy with cataplexy in Europe ~**0.74/100,000 person-years** (2024 review). (baldini2024pediatricnarcolepsytype pages 1-2)
- HLA-DQB1*06:02:01 association in NT1: **OR 7.27** (2024 high-resolution sequencing). (hamdan2024high‐resolutionhlasequencing pages 3-4)
- GWAS sample size: **6,073 cases / 84,856 controls** (2023 Nature Communications). (ollila2023narcolepsyriskloci pages 6-7)
- LXB randomized-withdrawal narcolepsy trial summary: cataplexy and ESS endpoints **P<0.0001**; TEAEs **76.1%**, discontinuation **11.9%** (2023 review of trial program). (schneider2023longtermtreatmentof pages 3-5)

---

# Limitations and missing data elements (for KB completeness)
- **Identifiers not found** in retrieved evidence: MONDO ID, MeSH ID, ICD‑10/ICD‑11 codes, OMIM IDs.
- **PMIDs** were not available in the retrieved full-text excerpts; therefore, PMID-anchored citations could not be provided.
- **Mortality/life expectancy** statistics and robust **real-world effectiveness** datasets were not present in retrieved sources.
- **Cross-species naturally occurring disease** (e.g., canine narcolepsy) was not captured in the retrieved corpus.


References

1. (baldini2024pediatricnarcolepsytype pages 1-2): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

2. (coelho2024narcolepsyaninterface pages 2-3): Fernando Morgadinho Santos Coelho. Narcolepsy: an interface among neurology, immunology, sleep, and genetics. Arquivos de Neuro-Psiquiatria, 82:001-009, Apr 2024. URL: https://doi.org/10.1055/s-0044-1779299, doi:10.1055/s-0044-1779299. This article has 4 citations and is from a peer-reviewed journal.

3. (matota2023exploringtheliterature pages 1-2): Ana-Maria Mațotă, Andrei Bordeianu, Emilia Severin, and Alexandra Jidovu. Exploring the literature on narcolepsy: insights into the sleep disorder that strikes during the day. NeuroSci, 4:263-279, Oct 2023. URL: https://doi.org/10.3390/neurosci4040022, doi:10.3390/neurosci4040022. This article has 8 citations.

4. (ollila2023narcolepsyriskloci pages 1-2): Hanna M. Ollila, Eilon Sharon, Ling Lin, Nasa Sinnott-Armstrong, Aditya Ambati, Selina M. Yogeshwar, Ryan P. Hillary, Otto Jolanki, Juliette Faraco, Mali Einen, Guo Luo, Jing Zhang, Fang Han, Han Yan, Xiao Song Dong, Jing Li, Jun Zhang, Seung-Chul Hong, Tae Won Kim, Yves Dauvilliers, Lucie Barateau, Gert Jan Lammers, Rolf Fronczek, Geert Mayer, Joan Santamaria, Isabelle Arnulf, Stine Knudsen-Heier, May Kristin Lyamouri Bredahl, Per Medbøe Thorsby, Giuseppe Plazzi, Fabio Pizza, Monica Moresco, Catherine Crowe, Stephen K. Van den Eeden, Michel Lecendreux, Patrice Bourgin, Takashi Kanbayashi, Francisco J. Martínez-Orozco, Rosa Peraita-Adrados, Antonio Benetó, Jacques Montplaisir, Alex Desautels, Yu-Shu Huang, Thomas Damm Als, Adam Ziemann, Ali Abbasi, Anne Lehtonen, Apinya Lertratanakul, Bridget Riley-Gillis, Fedik Rahimov, Howard Jacob, Jeffrey Waring, Mengzhen Liu, Nizar Smaoui, Relja Popovic, Adam Platt, Athena Matakidou, Benjamin Challis, Dirk Paul, Glenda Lassi, Ioanna Tachmazidou, Antti Hakanen, Johanna Schleutker, Nina Pitkänen, Perttu Terho, Petri Virolainen, Arto Mannermaa, Veli-Matti Kosma, Chia-Yen Chen, Heiko Runz, Sally John, Sanni Lahdenperä, Stephanie Loomis, Susan Eaton, George Okafo, Heli Salminen-Mankonen, Marc Jung, Nathan Lawless, Zhihao Ding, Joseph Maranville, Marla Hochfeld, Robert Plenge, Shameek Biswas, Masahiro Kanai, Mutaamba Maasha, Wei Zhou, Outi Tuovila, Raimo Pakkanen, Jari Laukkanen, Teijo Kuopio, Kristiina Aittomäki, Antti Mäkitie, Natalia Pujol, Triin Laisk, Katriina Aalto-Setälä, Johanna Mäkelä, Marco Hautalahti, Sarah Smith, Tom Southerington, Eeva Kangasniemi, Henna Palin, Mika Kähönen, Sanna Siltanen, Tarja Laitinen, Felix Vaura, Jaana Suvisaari, Teemu Niiranen, Veikko Salomaa, Jukka Partanen, Mikko Arvas, Jarmo Ritari, Kati Hyvärinen, David Choy, Edmond Teng, Erich Strauss, Hao Chen, Hubert Chen, Jennifer Schutzman, Julie Hunkapiller, Mark McCarthy, Natalie Bowers, Rion Pendergrass, Tim Lu, Audrey Chu, Diptee Kulkarni, Fanli Xu, Joanna Betts, John Eicher, Jorge Esparza Gordillo, Laura Addis, Linda McCarthy, Rajashree Mishra, Janet Kumar, Margaret G. Ehm, Kirsi Auro, David Pulford, Anne Pitkäranta, Anu Loukola, Eero Punkka, Malla-Maria Linna, Olli Carpén, Taneli Raivio, Joni A. Turunen, Tomi P. Mäkelä, Aino Salminen, Antti Aarnisalo, Daniel Gordin, David Rice, Erkki Isometsä, Eveliina Salminen, Heikki Joensuu, Ilkka Kalliala, Johanna Mattson, Juha Sinisalo, Jukka Koskela, Kari Eklund, Katariina Hannula-Jouppi, Lauri Aaltonen, Marja-Riitta Taskinen, Martti Färkkilä, Minna Raivio, Oskari Heikinheimo, Paula Kauppi, Pekka Nieminen, Pentti Tienari, Pirkko Pussinen, Sampsa Pikkarainen, Terhi Ollila, Tiinamaija Tuomi, Timo Hiltunen, Tuomo Meretoja, Tuula Salo, Ulla Palotie, Antti Palomäki, Jenni Aittokallio, Juha Rinne, Kaj Metsärinne, Klaus Elenius, Laura Pirilä, Leena Koulu, Markku Voutilainen, Riitta Lahesmaa, Roosa Kallionpää, Sirkku Peltonen, Tytti Willberg, Ulvi Gursoy, Varpu Jokimaa, Aarno Palotie, Anastasia Kytölä, Andrea Ganna, Anu Jalanko, Aoxing Liu, Arto Lehisto, Awaisa Ghazal, Elina Kilpeläinen, Elisabeth Widen, Elmo Saarentaus, Esa Pitkänen, Hanna Ollila, Hannele Laivuori, Henrike Heyne, Huei-Yi Shen, Jaakko Kaprio, Joel Rämö, Juha Karjalainen, Juha Mehtonen, Jyrki Pitkänen, Kalle Pärn, Kati Donner, Katja Kivinen, L. Elisa Lahtela, Mari E. Niemi, Mari Kaunisto, Mart Kals, Mary Pat Reeve, Mervi Aavikko, Nina Mars, Oluwaseun Alexander Dada, Pietro Della Briotta Parolo, Priit Palta, Rigbe Weldatsadik, Risto Kajanne, Rodos Rodosthenous, Samuli Ripatti, Sanni Ruotsalainen, Satu Strausz, Shabbeer Hassan, Shanmukha Sampath Padmanabhuni, Shuang Luo, Susanna Lemmelä, Taru Tukiainen, Timo P. Sipilä, Tuomo Kiiskinen, Vincent Llorens, Mark Daly, Jiwoo Lee, Kristin Tsuo, Mitja Kurki, Amanda Elliott, Aki Havulinna, Juulia Partanen, Robert Yang, Dermot Reilly, Alessandro Porello, Amy Hart, Dawn Waterworth, Ekaterina Khramtsova, Karen He, Meijian Guan, Qingqin S. Li, Sauli Vuoti, Eric Green, Robert Graham, Sahar Mozaffari, Adriana Huertas-Vazquez, Andrey Loboda, Caroline Fox, Fabiana Farias, Jae-Hoon Sul, Jason Miller, Neha Raghavan, Simonne Longerich, Johannes Kettunen, Raisa Serpi, Reetta Hinttala, Tuomo Mantere, Anne Remes, Elisa Rahikkala, Johanna Huhtakangas, Kaisa Tasanen, Laura Huilaja, Laure Morin-Papunen, Maarit Niinimäki, Marja Vääräsmäki, Outi Uimari, Peeter Karihtala, Terhi Piltonen, Terttu Harju, Timo Blomster, Vuokko Anttonen, Hilkka Soininen, Kai Kaarniranta, Liisa Suominen, Margit Pelkonen, Maria Siponen, Mikko Kiviniemi, Oili Kaipiainen-Seppänen, Päivi Auvinen, Päivi Mäntylä, Reetta Kälviäinen, Valtteri Julkunen, Chris O’Donnell, Ma´en Obeidat, Nicole Renaud, Debby Ngo, Majd Mouded, Mike Mendelson, Anders Mälarstig, Heli Lehtonen, Jaakko Parkkinen, Kirsi Kalpala, Melissa Miller, Nan Bing, Stefan McDonough, Xinli Hu, Ying Wu, Airi Jussila, Annika Auranen, Argyro Bizaki-Vallaskangas, Hannu Uusitalo, Jukka Peltola, Jussi Hernesniemi, Katri Kaukinen, Laura Kotaniemi-Talonen, Pia Isomäki, Teea Salmi, Venla Kurra, Kirsi Sipilä, Auli Toivola, Elina Järvensivu, Essi Kaiharju, Hannele Mattsson, Kati Kristiansson, Lotta Männikkö, Markku Laukkanen, Markus Perola, Minna Brunfeldt, Päivi Laiho, Regis Wong, Sami Koskelainen, Sini Lähteenmäki, Sirpa Soini, Teemu Paajanen, Terhi Kilpi, Tero Hiekkalinna, Tuuli Sistonen, Clément Chatelain, Deepak Raipal, Katherine Klinger, Samuel Lessard, Fredrik Åberg, Mikko Hiltunen, Sami Heikkinen, Hannu Kankaanranta, Tuula Palotie, Iiris Hovatta, Kimmo Palin, Niko Välimäki, Sanna Toppila-Salmi, Eija Laakkonen, Eeva Sliz, Heidi Silven, Katri Pylkäs, Minna Karjalainen, Riikka Arffman, Susanna Savukoski, Jaakko Tyrmi, Manuel Rivas, Harri Siirtola, Iida Vähätalo, Javier Garcia-Tabuenca, Marianna Niemi, Mika Helminen, Tiina Luukkaala, Poul Jennum, Sona Nevsimalova, David Kemlink, Alex Iranzo, Sebastiaan Overeem, Aleksandra Wierzbicka, Peter Geisler, Karel Sonka, Makoto Honda, Birgit Högl, Ambra Stefani, Fernando Morgadinho Coelho, Vilma Mantovani, Eva Feketeova, Mia Wadelius, Niclas Eriksson, Hans Smedje, Pär Hallberg, Per Egil Hesla, David Rye, Zerrin Pelin, Luigi Ferini-Strambi, Claudio L. Bassetti, Johannes Mathis, Ramin Khatami, Adi Aran, Sheela Nampoothiri, Tomas Olsson, Ingrid Kockum, Markku Partinen, Markus Perola, Birgitte R. Kornum, Sina Rueger, Juliane Winkelmann, Taku Miyagawa, Hiromi Toyoda, Seik-Soon Khor, Mihoko Shimada, Katsushi Tokunaga, Manuel Rivas, Jonathan K. Pritchard, Neil Risch, Zoltan Kutalik, Ruth O’Hara, Joachim Hallmayer, Chun Jimmie Ye, and Emmanuel J. Mignot. Narcolepsy risk loci outline role of t cell autoimmunity and infectious triggers in narcolepsy. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-36120-z, doi:10.1038/s41467-023-36120-z. This article has 61 citations and is from a highest quality peer-reviewed journal.

5. (ollila2023narcolepsyriskloci pages 6-7): Hanna M. Ollila, Eilon Sharon, Ling Lin, Nasa Sinnott-Armstrong, Aditya Ambati, Selina M. Yogeshwar, Ryan P. Hillary, Otto Jolanki, Juliette Faraco, Mali Einen, Guo Luo, Jing Zhang, Fang Han, Han Yan, Xiao Song Dong, Jing Li, Jun Zhang, Seung-Chul Hong, Tae Won Kim, Yves Dauvilliers, Lucie Barateau, Gert Jan Lammers, Rolf Fronczek, Geert Mayer, Joan Santamaria, Isabelle Arnulf, Stine Knudsen-Heier, May Kristin Lyamouri Bredahl, Per Medbøe Thorsby, Giuseppe Plazzi, Fabio Pizza, Monica Moresco, Catherine Crowe, Stephen K. Van den Eeden, Michel Lecendreux, Patrice Bourgin, Takashi Kanbayashi, Francisco J. Martínez-Orozco, Rosa Peraita-Adrados, Antonio Benetó, Jacques Montplaisir, Alex Desautels, Yu-Shu Huang, Thomas Damm Als, Adam Ziemann, Ali Abbasi, Anne Lehtonen, Apinya Lertratanakul, Bridget Riley-Gillis, Fedik Rahimov, Howard Jacob, Jeffrey Waring, Mengzhen Liu, Nizar Smaoui, Relja Popovic, Adam Platt, Athena Matakidou, Benjamin Challis, Dirk Paul, Glenda Lassi, Ioanna Tachmazidou, Antti Hakanen, Johanna Schleutker, Nina Pitkänen, Perttu Terho, Petri Virolainen, Arto Mannermaa, Veli-Matti Kosma, Chia-Yen Chen, Heiko Runz, Sally John, Sanni Lahdenperä, Stephanie Loomis, Susan Eaton, George Okafo, Heli Salminen-Mankonen, Marc Jung, Nathan Lawless, Zhihao Ding, Joseph Maranville, Marla Hochfeld, Robert Plenge, Shameek Biswas, Masahiro Kanai, Mutaamba Maasha, Wei Zhou, Outi Tuovila, Raimo Pakkanen, Jari Laukkanen, Teijo Kuopio, Kristiina Aittomäki, Antti Mäkitie, Natalia Pujol, Triin Laisk, Katriina Aalto-Setälä, Johanna Mäkelä, Marco Hautalahti, Sarah Smith, Tom Southerington, Eeva Kangasniemi, Henna Palin, Mika Kähönen, Sanna Siltanen, Tarja Laitinen, Felix Vaura, Jaana Suvisaari, Teemu Niiranen, Veikko Salomaa, Jukka Partanen, Mikko Arvas, Jarmo Ritari, Kati Hyvärinen, David Choy, Edmond Teng, Erich Strauss, Hao Chen, Hubert Chen, Jennifer Schutzman, Julie Hunkapiller, Mark McCarthy, Natalie Bowers, Rion Pendergrass, Tim Lu, Audrey Chu, Diptee Kulkarni, Fanli Xu, Joanna Betts, John Eicher, Jorge Esparza Gordillo, Laura Addis, Linda McCarthy, Rajashree Mishra, Janet Kumar, Margaret G. Ehm, Kirsi Auro, David Pulford, Anne Pitkäranta, Anu Loukola, Eero Punkka, Malla-Maria Linna, Olli Carpén, Taneli Raivio, Joni A. Turunen, Tomi P. Mäkelä, Aino Salminen, Antti Aarnisalo, Daniel Gordin, David Rice, Erkki Isometsä, Eveliina Salminen, Heikki Joensuu, Ilkka Kalliala, Johanna Mattson, Juha Sinisalo, Jukka Koskela, Kari Eklund, Katariina Hannula-Jouppi, Lauri Aaltonen, Marja-Riitta Taskinen, Martti Färkkilä, Minna Raivio, Oskari Heikinheimo, Paula Kauppi, Pekka Nieminen, Pentti Tienari, Pirkko Pussinen, Sampsa Pikkarainen, Terhi Ollila, Tiinamaija Tuomi, Timo Hiltunen, Tuomo Meretoja, Tuula Salo, Ulla Palotie, Antti Palomäki, Jenni Aittokallio, Juha Rinne, Kaj Metsärinne, Klaus Elenius, Laura Pirilä, Leena Koulu, Markku Voutilainen, Riitta Lahesmaa, Roosa Kallionpää, Sirkku Peltonen, Tytti Willberg, Ulvi Gursoy, Varpu Jokimaa, Aarno Palotie, Anastasia Kytölä, Andrea Ganna, Anu Jalanko, Aoxing Liu, Arto Lehisto, Awaisa Ghazal, Elina Kilpeläinen, Elisabeth Widen, Elmo Saarentaus, Esa Pitkänen, Hanna Ollila, Hannele Laivuori, Henrike Heyne, Huei-Yi Shen, Jaakko Kaprio, Joel Rämö, Juha Karjalainen, Juha Mehtonen, Jyrki Pitkänen, Kalle Pärn, Kati Donner, Katja Kivinen, L. Elisa Lahtela, Mari E. Niemi, Mari Kaunisto, Mart Kals, Mary Pat Reeve, Mervi Aavikko, Nina Mars, Oluwaseun Alexander Dada, Pietro Della Briotta Parolo, Priit Palta, Rigbe Weldatsadik, Risto Kajanne, Rodos Rodosthenous, Samuli Ripatti, Sanni Ruotsalainen, Satu Strausz, Shabbeer Hassan, Shanmukha Sampath Padmanabhuni, Shuang Luo, Susanna Lemmelä, Taru Tukiainen, Timo P. Sipilä, Tuomo Kiiskinen, Vincent Llorens, Mark Daly, Jiwoo Lee, Kristin Tsuo, Mitja Kurki, Amanda Elliott, Aki Havulinna, Juulia Partanen, Robert Yang, Dermot Reilly, Alessandro Porello, Amy Hart, Dawn Waterworth, Ekaterina Khramtsova, Karen He, Meijian Guan, Qingqin S. Li, Sauli Vuoti, Eric Green, Robert Graham, Sahar Mozaffari, Adriana Huertas-Vazquez, Andrey Loboda, Caroline Fox, Fabiana Farias, Jae-Hoon Sul, Jason Miller, Neha Raghavan, Simonne Longerich, Johannes Kettunen, Raisa Serpi, Reetta Hinttala, Tuomo Mantere, Anne Remes, Elisa Rahikkala, Johanna Huhtakangas, Kaisa Tasanen, Laura Huilaja, Laure Morin-Papunen, Maarit Niinimäki, Marja Vääräsmäki, Outi Uimari, Peeter Karihtala, Terhi Piltonen, Terttu Harju, Timo Blomster, Vuokko Anttonen, Hilkka Soininen, Kai Kaarniranta, Liisa Suominen, Margit Pelkonen, Maria Siponen, Mikko Kiviniemi, Oili Kaipiainen-Seppänen, Päivi Auvinen, Päivi Mäntylä, Reetta Kälviäinen, Valtteri Julkunen, Chris O’Donnell, Ma´en Obeidat, Nicole Renaud, Debby Ngo, Majd Mouded, Mike Mendelson, Anders Mälarstig, Heli Lehtonen, Jaakko Parkkinen, Kirsi Kalpala, Melissa Miller, Nan Bing, Stefan McDonough, Xinli Hu, Ying Wu, Airi Jussila, Annika Auranen, Argyro Bizaki-Vallaskangas, Hannu Uusitalo, Jukka Peltola, Jussi Hernesniemi, Katri Kaukinen, Laura Kotaniemi-Talonen, Pia Isomäki, Teea Salmi, Venla Kurra, Kirsi Sipilä, Auli Toivola, Elina Järvensivu, Essi Kaiharju, Hannele Mattsson, Kati Kristiansson, Lotta Männikkö, Markku Laukkanen, Markus Perola, Minna Brunfeldt, Päivi Laiho, Regis Wong, Sami Koskelainen, Sini Lähteenmäki, Sirpa Soini, Teemu Paajanen, Terhi Kilpi, Tero Hiekkalinna, Tuuli Sistonen, Clément Chatelain, Deepak Raipal, Katherine Klinger, Samuel Lessard, Fredrik Åberg, Mikko Hiltunen, Sami Heikkinen, Hannu Kankaanranta, Tuula Palotie, Iiris Hovatta, Kimmo Palin, Niko Välimäki, Sanna Toppila-Salmi, Eija Laakkonen, Eeva Sliz, Heidi Silven, Katri Pylkäs, Minna Karjalainen, Riikka Arffman, Susanna Savukoski, Jaakko Tyrmi, Manuel Rivas, Harri Siirtola, Iida Vähätalo, Javier Garcia-Tabuenca, Marianna Niemi, Mika Helminen, Tiina Luukkaala, Poul Jennum, Sona Nevsimalova, David Kemlink, Alex Iranzo, Sebastiaan Overeem, Aleksandra Wierzbicka, Peter Geisler, Karel Sonka, Makoto Honda, Birgit Högl, Ambra Stefani, Fernando Morgadinho Coelho, Vilma Mantovani, Eva Feketeova, Mia Wadelius, Niclas Eriksson, Hans Smedje, Pär Hallberg, Per Egil Hesla, David Rye, Zerrin Pelin, Luigi Ferini-Strambi, Claudio L. Bassetti, Johannes Mathis, Ramin Khatami, Adi Aran, Sheela Nampoothiri, Tomas Olsson, Ingrid Kockum, Markku Partinen, Markus Perola, Birgitte R. Kornum, Sina Rueger, Juliane Winkelmann, Taku Miyagawa, Hiromi Toyoda, Seik-Soon Khor, Mihoko Shimada, Katsushi Tokunaga, Manuel Rivas, Jonathan K. Pritchard, Neil Risch, Zoltan Kutalik, Ruth O’Hara, Joachim Hallmayer, Chun Jimmie Ye, and Emmanuel J. Mignot. Narcolepsy risk loci outline role of t cell autoimmunity and infectious triggers in narcolepsy. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-36120-z, doi:10.1038/s41467-023-36120-z. This article has 61 citations and is from a highest quality peer-reviewed journal.

6. (xu2024theroleof pages 5-7): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

7. (xu2024theroleof pages 1-2): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

8. (hamdan2024high‐resolutionhlasequencing pages 3-4): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

9. (hamdan2024high‐resolutionhlasequencing pages 4-5): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

10. (ollilaUnknownyearmbati.ogeshwarsm… pages 7-8): HM Ollila, E Sharon, and L Lin. Mbati,., ogeshwar, sm,… mignot, e..(2023). Unknown journal, Unknown year.

11. (ollila2023narcolepsyriskloci pages 5-6): Hanna M. Ollila, Eilon Sharon, Ling Lin, Nasa Sinnott-Armstrong, Aditya Ambati, Selina M. Yogeshwar, Ryan P. Hillary, Otto Jolanki, Juliette Faraco, Mali Einen, Guo Luo, Jing Zhang, Fang Han, Han Yan, Xiao Song Dong, Jing Li, Jun Zhang, Seung-Chul Hong, Tae Won Kim, Yves Dauvilliers, Lucie Barateau, Gert Jan Lammers, Rolf Fronczek, Geert Mayer, Joan Santamaria, Isabelle Arnulf, Stine Knudsen-Heier, May Kristin Lyamouri Bredahl, Per Medbøe Thorsby, Giuseppe Plazzi, Fabio Pizza, Monica Moresco, Catherine Crowe, Stephen K. Van den Eeden, Michel Lecendreux, Patrice Bourgin, Takashi Kanbayashi, Francisco J. Martínez-Orozco, Rosa Peraita-Adrados, Antonio Benetó, Jacques Montplaisir, Alex Desautels, Yu-Shu Huang, Thomas Damm Als, Adam Ziemann, Ali Abbasi, Anne Lehtonen, Apinya Lertratanakul, Bridget Riley-Gillis, Fedik Rahimov, Howard Jacob, Jeffrey Waring, Mengzhen Liu, Nizar Smaoui, Relja Popovic, Adam Platt, Athena Matakidou, Benjamin Challis, Dirk Paul, Glenda Lassi, Ioanna Tachmazidou, Antti Hakanen, Johanna Schleutker, Nina Pitkänen, Perttu Terho, Petri Virolainen, Arto Mannermaa, Veli-Matti Kosma, Chia-Yen Chen, Heiko Runz, Sally John, Sanni Lahdenperä, Stephanie Loomis, Susan Eaton, George Okafo, Heli Salminen-Mankonen, Marc Jung, Nathan Lawless, Zhihao Ding, Joseph Maranville, Marla Hochfeld, Robert Plenge, Shameek Biswas, Masahiro Kanai, Mutaamba Maasha, Wei Zhou, Outi Tuovila, Raimo Pakkanen, Jari Laukkanen, Teijo Kuopio, Kristiina Aittomäki, Antti Mäkitie, Natalia Pujol, Triin Laisk, Katriina Aalto-Setälä, Johanna Mäkelä, Marco Hautalahti, Sarah Smith, Tom Southerington, Eeva Kangasniemi, Henna Palin, Mika Kähönen, Sanna Siltanen, Tarja Laitinen, Felix Vaura, Jaana Suvisaari, Teemu Niiranen, Veikko Salomaa, Jukka Partanen, Mikko Arvas, Jarmo Ritari, Kati Hyvärinen, David Choy, Edmond Teng, Erich Strauss, Hao Chen, Hubert Chen, Jennifer Schutzman, Julie Hunkapiller, Mark McCarthy, Natalie Bowers, Rion Pendergrass, Tim Lu, Audrey Chu, Diptee Kulkarni, Fanli Xu, Joanna Betts, John Eicher, Jorge Esparza Gordillo, Laura Addis, Linda McCarthy, Rajashree Mishra, Janet Kumar, Margaret G. Ehm, Kirsi Auro, David Pulford, Anne Pitkäranta, Anu Loukola, Eero Punkka, Malla-Maria Linna, Olli Carpén, Taneli Raivio, Joni A. Turunen, Tomi P. Mäkelä, Aino Salminen, Antti Aarnisalo, Daniel Gordin, David Rice, Erkki Isometsä, Eveliina Salminen, Heikki Joensuu, Ilkka Kalliala, Johanna Mattson, Juha Sinisalo, Jukka Koskela, Kari Eklund, Katariina Hannula-Jouppi, Lauri Aaltonen, Marja-Riitta Taskinen, Martti Färkkilä, Minna Raivio, Oskari Heikinheimo, Paula Kauppi, Pekka Nieminen, Pentti Tienari, Pirkko Pussinen, Sampsa Pikkarainen, Terhi Ollila, Tiinamaija Tuomi, Timo Hiltunen, Tuomo Meretoja, Tuula Salo, Ulla Palotie, Antti Palomäki, Jenni Aittokallio, Juha Rinne, Kaj Metsärinne, Klaus Elenius, Laura Pirilä, Leena Koulu, Markku Voutilainen, Riitta Lahesmaa, Roosa Kallionpää, Sirkku Peltonen, Tytti Willberg, Ulvi Gursoy, Varpu Jokimaa, Aarno Palotie, Anastasia Kytölä, Andrea Ganna, Anu Jalanko, Aoxing Liu, Arto Lehisto, Awaisa Ghazal, Elina Kilpeläinen, Elisabeth Widen, Elmo Saarentaus, Esa Pitkänen, Hanna Ollila, Hannele Laivuori, Henrike Heyne, Huei-Yi Shen, Jaakko Kaprio, Joel Rämö, Juha Karjalainen, Juha Mehtonen, Jyrki Pitkänen, Kalle Pärn, Kati Donner, Katja Kivinen, L. Elisa Lahtela, Mari E. Niemi, Mari Kaunisto, Mart Kals, Mary Pat Reeve, Mervi Aavikko, Nina Mars, Oluwaseun Alexander Dada, Pietro Della Briotta Parolo, Priit Palta, Rigbe Weldatsadik, Risto Kajanne, Rodos Rodosthenous, Samuli Ripatti, Sanni Ruotsalainen, Satu Strausz, Shabbeer Hassan, Shanmukha Sampath Padmanabhuni, Shuang Luo, Susanna Lemmelä, Taru Tukiainen, Timo P. Sipilä, Tuomo Kiiskinen, Vincent Llorens, Mark Daly, Jiwoo Lee, Kristin Tsuo, Mitja Kurki, Amanda Elliott, Aki Havulinna, Juulia Partanen, Robert Yang, Dermot Reilly, Alessandro Porello, Amy Hart, Dawn Waterworth, Ekaterina Khramtsova, Karen He, Meijian Guan, Qingqin S. Li, Sauli Vuoti, Eric Green, Robert Graham, Sahar Mozaffari, Adriana Huertas-Vazquez, Andrey Loboda, Caroline Fox, Fabiana Farias, Jae-Hoon Sul, Jason Miller, Neha Raghavan, Simonne Longerich, Johannes Kettunen, Raisa Serpi, Reetta Hinttala, Tuomo Mantere, Anne Remes, Elisa Rahikkala, Johanna Huhtakangas, Kaisa Tasanen, Laura Huilaja, Laure Morin-Papunen, Maarit Niinimäki, Marja Vääräsmäki, Outi Uimari, Peeter Karihtala, Terhi Piltonen, Terttu Harju, Timo Blomster, Vuokko Anttonen, Hilkka Soininen, Kai Kaarniranta, Liisa Suominen, Margit Pelkonen, Maria Siponen, Mikko Kiviniemi, Oili Kaipiainen-Seppänen, Päivi Auvinen, Päivi Mäntylä, Reetta Kälviäinen, Valtteri Julkunen, Chris O’Donnell, Ma´en Obeidat, Nicole Renaud, Debby Ngo, Majd Mouded, Mike Mendelson, Anders Mälarstig, Heli Lehtonen, Jaakko Parkkinen, Kirsi Kalpala, Melissa Miller, Nan Bing, Stefan McDonough, Xinli Hu, Ying Wu, Airi Jussila, Annika Auranen, Argyro Bizaki-Vallaskangas, Hannu Uusitalo, Jukka Peltola, Jussi Hernesniemi, Katri Kaukinen, Laura Kotaniemi-Talonen, Pia Isomäki, Teea Salmi, Venla Kurra, Kirsi Sipilä, Auli Toivola, Elina Järvensivu, Essi Kaiharju, Hannele Mattsson, Kati Kristiansson, Lotta Männikkö, Markku Laukkanen, Markus Perola, Minna Brunfeldt, Päivi Laiho, Regis Wong, Sami Koskelainen, Sini Lähteenmäki, Sirpa Soini, Teemu Paajanen, Terhi Kilpi, Tero Hiekkalinna, Tuuli Sistonen, Clément Chatelain, Deepak Raipal, Katherine Klinger, Samuel Lessard, Fredrik Åberg, Mikko Hiltunen, Sami Heikkinen, Hannu Kankaanranta, Tuula Palotie, Iiris Hovatta, Kimmo Palin, Niko Välimäki, Sanna Toppila-Salmi, Eija Laakkonen, Eeva Sliz, Heidi Silven, Katri Pylkäs, Minna Karjalainen, Riikka Arffman, Susanna Savukoski, Jaakko Tyrmi, Manuel Rivas, Harri Siirtola, Iida Vähätalo, Javier Garcia-Tabuenca, Marianna Niemi, Mika Helminen, Tiina Luukkaala, Poul Jennum, Sona Nevsimalova, David Kemlink, Alex Iranzo, Sebastiaan Overeem, Aleksandra Wierzbicka, Peter Geisler, Karel Sonka, Makoto Honda, Birgit Högl, Ambra Stefani, Fernando Morgadinho Coelho, Vilma Mantovani, Eva Feketeova, Mia Wadelius, Niclas Eriksson, Hans Smedje, Pär Hallberg, Per Egil Hesla, David Rye, Zerrin Pelin, Luigi Ferini-Strambi, Claudio L. Bassetti, Johannes Mathis, Ramin Khatami, Adi Aran, Sheela Nampoothiri, Tomas Olsson, Ingrid Kockum, Markku Partinen, Markus Perola, Birgitte R. Kornum, Sina Rueger, Juliane Winkelmann, Taku Miyagawa, Hiromi Toyoda, Seik-Soon Khor, Mihoko Shimada, Katsushi Tokunaga, Manuel Rivas, Jonathan K. Pritchard, Neil Risch, Zoltan Kutalik, Ruth O’Hara, Joachim Hallmayer, Chun Jimmie Ye, and Emmanuel J. Mignot. Narcolepsy risk loci outline role of t cell autoimmunity and infectious triggers in narcolepsy. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-36120-z, doi:10.1038/s41467-023-36120-z. This article has 61 citations and is from a highest quality peer-reviewed journal.

12. (ollila2023narcolepsyriskloci pages 3-4): Hanna M. Ollila, Eilon Sharon, Ling Lin, Nasa Sinnott-Armstrong, Aditya Ambati, Selina M. Yogeshwar, Ryan P. Hillary, Otto Jolanki, Juliette Faraco, Mali Einen, Guo Luo, Jing Zhang, Fang Han, Han Yan, Xiao Song Dong, Jing Li, Jun Zhang, Seung-Chul Hong, Tae Won Kim, Yves Dauvilliers, Lucie Barateau, Gert Jan Lammers, Rolf Fronczek, Geert Mayer, Joan Santamaria, Isabelle Arnulf, Stine Knudsen-Heier, May Kristin Lyamouri Bredahl, Per Medbøe Thorsby, Giuseppe Plazzi, Fabio Pizza, Monica Moresco, Catherine Crowe, Stephen K. Van den Eeden, Michel Lecendreux, Patrice Bourgin, Takashi Kanbayashi, Francisco J. Martínez-Orozco, Rosa Peraita-Adrados, Antonio Benetó, Jacques Montplaisir, Alex Desautels, Yu-Shu Huang, Thomas Damm Als, Adam Ziemann, Ali Abbasi, Anne Lehtonen, Apinya Lertratanakul, Bridget Riley-Gillis, Fedik Rahimov, Howard Jacob, Jeffrey Waring, Mengzhen Liu, Nizar Smaoui, Relja Popovic, Adam Platt, Athena Matakidou, Benjamin Challis, Dirk Paul, Glenda Lassi, Ioanna Tachmazidou, Antti Hakanen, Johanna Schleutker, Nina Pitkänen, Perttu Terho, Petri Virolainen, Arto Mannermaa, Veli-Matti Kosma, Chia-Yen Chen, Heiko Runz, Sally John, Sanni Lahdenperä, Stephanie Loomis, Susan Eaton, George Okafo, Heli Salminen-Mankonen, Marc Jung, Nathan Lawless, Zhihao Ding, Joseph Maranville, Marla Hochfeld, Robert Plenge, Shameek Biswas, Masahiro Kanai, Mutaamba Maasha, Wei Zhou, Outi Tuovila, Raimo Pakkanen, Jari Laukkanen, Teijo Kuopio, Kristiina Aittomäki, Antti Mäkitie, Natalia Pujol, Triin Laisk, Katriina Aalto-Setälä, Johanna Mäkelä, Marco Hautalahti, Sarah Smith, Tom Southerington, Eeva Kangasniemi, Henna Palin, Mika Kähönen, Sanna Siltanen, Tarja Laitinen, Felix Vaura, Jaana Suvisaari, Teemu Niiranen, Veikko Salomaa, Jukka Partanen, Mikko Arvas, Jarmo Ritari, Kati Hyvärinen, David Choy, Edmond Teng, Erich Strauss, Hao Chen, Hubert Chen, Jennifer Schutzman, Julie Hunkapiller, Mark McCarthy, Natalie Bowers, Rion Pendergrass, Tim Lu, Audrey Chu, Diptee Kulkarni, Fanli Xu, Joanna Betts, John Eicher, Jorge Esparza Gordillo, Laura Addis, Linda McCarthy, Rajashree Mishra, Janet Kumar, Margaret G. Ehm, Kirsi Auro, David Pulford, Anne Pitkäranta, Anu Loukola, Eero Punkka, Malla-Maria Linna, Olli Carpén, Taneli Raivio, Joni A. Turunen, Tomi P. Mäkelä, Aino Salminen, Antti Aarnisalo, Daniel Gordin, David Rice, Erkki Isometsä, Eveliina Salminen, Heikki Joensuu, Ilkka Kalliala, Johanna Mattson, Juha Sinisalo, Jukka Koskela, Kari Eklund, Katariina Hannula-Jouppi, Lauri Aaltonen, Marja-Riitta Taskinen, Martti Färkkilä, Minna Raivio, Oskari Heikinheimo, Paula Kauppi, Pekka Nieminen, Pentti Tienari, Pirkko Pussinen, Sampsa Pikkarainen, Terhi Ollila, Tiinamaija Tuomi, Timo Hiltunen, Tuomo Meretoja, Tuula Salo, Ulla Palotie, Antti Palomäki, Jenni Aittokallio, Juha Rinne, Kaj Metsärinne, Klaus Elenius, Laura Pirilä, Leena Koulu, Markku Voutilainen, Riitta Lahesmaa, Roosa Kallionpää, Sirkku Peltonen, Tytti Willberg, Ulvi Gursoy, Varpu Jokimaa, Aarno Palotie, Anastasia Kytölä, Andrea Ganna, Anu Jalanko, Aoxing Liu, Arto Lehisto, Awaisa Ghazal, Elina Kilpeläinen, Elisabeth Widen, Elmo Saarentaus, Esa Pitkänen, Hanna Ollila, Hannele Laivuori, Henrike Heyne, Huei-Yi Shen, Jaakko Kaprio, Joel Rämö, Juha Karjalainen, Juha Mehtonen, Jyrki Pitkänen, Kalle Pärn, Kati Donner, Katja Kivinen, L. Elisa Lahtela, Mari E. Niemi, Mari Kaunisto, Mart Kals, Mary Pat Reeve, Mervi Aavikko, Nina Mars, Oluwaseun Alexander Dada, Pietro Della Briotta Parolo, Priit Palta, Rigbe Weldatsadik, Risto Kajanne, Rodos Rodosthenous, Samuli Ripatti, Sanni Ruotsalainen, Satu Strausz, Shabbeer Hassan, Shanmukha Sampath Padmanabhuni, Shuang Luo, Susanna Lemmelä, Taru Tukiainen, Timo P. Sipilä, Tuomo Kiiskinen, Vincent Llorens, Mark Daly, Jiwoo Lee, Kristin Tsuo, Mitja Kurki, Amanda Elliott, Aki Havulinna, Juulia Partanen, Robert Yang, Dermot Reilly, Alessandro Porello, Amy Hart, Dawn Waterworth, Ekaterina Khramtsova, Karen He, Meijian Guan, Qingqin S. Li, Sauli Vuoti, Eric Green, Robert Graham, Sahar Mozaffari, Adriana Huertas-Vazquez, Andrey Loboda, Caroline Fox, Fabiana Farias, Jae-Hoon Sul, Jason Miller, Neha Raghavan, Simonne Longerich, Johannes Kettunen, Raisa Serpi, Reetta Hinttala, Tuomo Mantere, Anne Remes, Elisa Rahikkala, Johanna Huhtakangas, Kaisa Tasanen, Laura Huilaja, Laure Morin-Papunen, Maarit Niinimäki, Marja Vääräsmäki, Outi Uimari, Peeter Karihtala, Terhi Piltonen, Terttu Harju, Timo Blomster, Vuokko Anttonen, Hilkka Soininen, Kai Kaarniranta, Liisa Suominen, Margit Pelkonen, Maria Siponen, Mikko Kiviniemi, Oili Kaipiainen-Seppänen, Päivi Auvinen, Päivi Mäntylä, Reetta Kälviäinen, Valtteri Julkunen, Chris O’Donnell, Ma´en Obeidat, Nicole Renaud, Debby Ngo, Majd Mouded, Mike Mendelson, Anders Mälarstig, Heli Lehtonen, Jaakko Parkkinen, Kirsi Kalpala, Melissa Miller, Nan Bing, Stefan McDonough, Xinli Hu, Ying Wu, Airi Jussila, Annika Auranen, Argyro Bizaki-Vallaskangas, Hannu Uusitalo, Jukka Peltola, Jussi Hernesniemi, Katri Kaukinen, Laura Kotaniemi-Talonen, Pia Isomäki, Teea Salmi, Venla Kurra, Kirsi Sipilä, Auli Toivola, Elina Järvensivu, Essi Kaiharju, Hannele Mattsson, Kati Kristiansson, Lotta Männikkö, Markku Laukkanen, Markus Perola, Minna Brunfeldt, Päivi Laiho, Regis Wong, Sami Koskelainen, Sini Lähteenmäki, Sirpa Soini, Teemu Paajanen, Terhi Kilpi, Tero Hiekkalinna, Tuuli Sistonen, Clément Chatelain, Deepak Raipal, Katherine Klinger, Samuel Lessard, Fredrik Åberg, Mikko Hiltunen, Sami Heikkinen, Hannu Kankaanranta, Tuula Palotie, Iiris Hovatta, Kimmo Palin, Niko Välimäki, Sanna Toppila-Salmi, Eija Laakkonen, Eeva Sliz, Heidi Silven, Katri Pylkäs, Minna Karjalainen, Riikka Arffman, Susanna Savukoski, Jaakko Tyrmi, Manuel Rivas, Harri Siirtola, Iida Vähätalo, Javier Garcia-Tabuenca, Marianna Niemi, Mika Helminen, Tiina Luukkaala, Poul Jennum, Sona Nevsimalova, David Kemlink, Alex Iranzo, Sebastiaan Overeem, Aleksandra Wierzbicka, Peter Geisler, Karel Sonka, Makoto Honda, Birgit Högl, Ambra Stefani, Fernando Morgadinho Coelho, Vilma Mantovani, Eva Feketeova, Mia Wadelius, Niclas Eriksson, Hans Smedje, Pär Hallberg, Per Egil Hesla, David Rye, Zerrin Pelin, Luigi Ferini-Strambi, Claudio L. Bassetti, Johannes Mathis, Ramin Khatami, Adi Aran, Sheela Nampoothiri, Tomas Olsson, Ingrid Kockum, Markku Partinen, Markus Perola, Birgitte R. Kornum, Sina Rueger, Juliane Winkelmann, Taku Miyagawa, Hiromi Toyoda, Seik-Soon Khor, Mihoko Shimada, Katsushi Tokunaga, Manuel Rivas, Jonathan K. Pritchard, Neil Risch, Zoltan Kutalik, Ruth O’Hara, Joachim Hallmayer, Chun Jimmie Ye, and Emmanuel J. Mignot. Narcolepsy risk loci outline role of t cell autoimmunity and infectious triggers in narcolepsy. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-36120-z, doi:10.1038/s41467-023-36120-z. This article has 61 citations and is from a highest quality peer-reviewed journal.

13. (severin2023exploringtheliterature pages 8-9): Emilia Severin, Ana-Maria Mațotă, Andrei Bordeianu, and Alexandra Jidovu. Exploring the literature on narcolepsy: insights into the sleep disorder that strikes during the day. Sep 2023. URL: https://doi.org/10.20944/preprints202309.0819.v1, doi:10.20944/preprints202309.0819.v1.

14. (ollilaUnknownyearmbati.ogeshwarsm… pages 6-7): HM Ollila, E Sharon, and L Lin. Mbati,., ogeshwar, sm,… mignot, e..(2023). Unknown journal, Unknown year.

15. (xu2024theroleof pages 3-5): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

16. (thomaz2024treatmentofnarcolepsy pages 1-2): Tania G Thomaz, Billy McBenedict, Dennys K Meireles, Giovanna F Farias, Luiz C Almeida, Marina C de Almeida Leitão, Wilhelmina N Hauwanga, Bruno Lima Pessôa, and Maria Isabel do Nascimento. Treatment of narcolepsy type 1 with orexin: a systematic review. Cureus, Dec 2024. URL: https://doi.org/10.7759/cureus.76692, doi:10.7759/cureus.76692. This article has 3 citations.

17. (xu2024theroleof pages 11-12): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

18. (hamdan2024high‐resolutionhlasequencing pages 6-6): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

19. (severin2023exploringtheliterature pages 3-5): Emilia Severin, Ana-Maria Mațotă, Andrei Bordeianu, and Alexandra Jidovu. Exploring the literature on narcolepsy: insights into the sleep disorder that strikes during the day. Sep 2023. URL: https://doi.org/10.20944/preprints202309.0819.v1, doi:10.20944/preprints202309.0819.v1.

20. (severin2023exploringtheliterature pages 9-11): Emilia Severin, Ana-Maria Mațotă, Andrei Bordeianu, and Alexandra Jidovu. Exploring the literature on narcolepsy: insights into the sleep disorder that strikes during the day. Sep 2023. URL: https://doi.org/10.20944/preprints202309.0819.v1, doi:10.20944/preprints202309.0819.v1.

21. (schneider2023longtermtreatmentof pages 3-5): Logan D Schneider, Anne Marie Morse, Michael J Strunc, Joyce K Lee-Iannotti, and Richard K Bogan. Long-term treatment of narcolepsy and idiopathic hypersomnia with low-sodium oxybate. Nature and Science of Sleep, 15:663-675, Aug 2023. URL: https://doi.org/10.2147/nss.s412793, doi:10.2147/nss.s412793. This article has 11 citations and is from a peer-reviewed journal.

22. (schneider2023longtermtreatmentof pages 1-2): Logan D Schneider, Anne Marie Morse, Michael J Strunc, Joyce K Lee-Iannotti, and Richard K Bogan. Long-term treatment of narcolepsy and idiopathic hypersomnia with low-sodium oxybate. Nature and Science of Sleep, 15:663-675, Aug 2023. URL: https://doi.org/10.2147/nss.s412793, doi:10.2147/nss.s412793. This article has 11 citations and is from a peer-reviewed journal.

23. (schneider2023longtermtreatmentof pages 5-6): Logan D Schneider, Anne Marie Morse, Michael J Strunc, Joyce K Lee-Iannotti, and Richard K Bogan. Long-term treatment of narcolepsy and idiopathic hypersomnia with low-sodium oxybate. Nature and Science of Sleep, 15:663-675, Aug 2023. URL: https://doi.org/10.2147/nss.s412793, doi:10.2147/nss.s412793. This article has 11 citations and is from a peer-reviewed journal.

24. (mitsukawa2024tak861apotent pages 1-2): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 22 citations and is from a peer-reviewed journal.

25. (mitsukawa2024tak861apotent pages 9-10): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 22 citations and is from a peer-reviewed journal.

26. (mitsukawa2024tak861apotent media 756d74c0): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 22 citations and is from a peer-reviewed journal.

27. (mitsukawa2024tak861apotent media cd11b0df): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 22 citations and is from a peer-reviewed journal.

28. (NCT05687903 chunk 1):  A Study of TAK-861 in Participants With Narcolepsy Type 1. Takeda. 2023. ClinicalTrials.gov Identifier: NCT05687903

29. (NCT06470828 chunk 1):  A Study of TAK-861 for the Treatment of Narcolepsy Type 1. Takeda. 2024. ClinicalTrials.gov Identifier: NCT06470828

30. (NCT06505031 chunk 1):  A Study of TAK-861 in People With Narcolepsy Type 1. Takeda. 2024. ClinicalTrials.gov Identifier: NCT06505031

31. (NCT07363720 chunk 1):  A Trial of TAK-861 for the Treatment of Narcolepsy With Cataplexy. Takeda. 2026. ClinicalTrials.gov Identifier: NCT07363720

32. (mitsukawa2024tak861apotent pages 4-7): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 22 citations and is from a peer-reviewed journal.