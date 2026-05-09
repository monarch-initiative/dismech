---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T12:01:33.545727'
end_time: '2026-05-07T12:21:30.795708'
duration_seconds: 1197.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inherited Ichthyosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inherited Ichthyosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inherited Ichthyosis** covering all of the
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
- **Disease Name:** Inherited Ichthyosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inherited Ichthyosis** covering all of the
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


# Inherited Ichthyosis — Disease Characteristics Research Report (2023–2024 emphasis)

## Target disease
**Disease name:** Inherited ichthyosis (collective term; includes congenital ichthyoses and other Mendelian disorders of cornification)

**Scope note:** “Inherited ichthyosis” is not a single disorder but a heterogeneous group of Mendelian disorders of cornification with shared core features of generalized scaling/hyperkeratosis and barrier dysfunction, spanning non‑syndromic (skin-limited) and syndromic forms. (xiang2025theclinicalspectrum pages 1-2, fioretti2024comprehensivemolecularanalysis pages 1-2, panda2025moleculargeneticsand pages 2-3)

**MONDO ID:** Not retrieved in the available tool-evidence corpus; cannot be asserted from current sources.

**Key synonyms / related terms (commonly used in the retrieved sources):**
- *Congenital ichthyosis / congenital ichthyoses (CI)* (marathe2023topicalisotretinoin(tmb001) pages 1-3, ho2024alteredskinmicrobiome pages 2-4)
- *Autosomal recessive congenital ichthyosis (ARCI)* including lamellar ichthyosis (LI), congenital ichthyosiform erythroderma (CIE), harlequin ichthyosis (HI), self‑improving collodion ichthyosis (SICI) (fioretti2024comprehensivemolecularanalysis pages 1-2, fioretti2024comprehensivemolecularanalysis pages 2-3)
- *X‑linked ichthyosis / X‑linked recessive ichthyosis* (XLI/XLRI) (fioretti2024comprehensivemolecularanalysis pages 1-2, marathe2023topicalisotretinoin(tmb001) pages 1-3)

**Data provenance:** The evidence used here is aggregated from peer‑reviewed cohort studies, reviews, and ClinicalTrials.gov registry records (not individual EHR-level data). (fioretti2024comprehensivemolecularanalysis pages 1-2, diociaiuti2024crosssectionalstudyon pages 4-5, marathe2023topicalisotretinoin(tmb001) pages 1-3, ho2024alteredskinmicrobiome pages 2-4)

---

## 1. Disease information

### Overview and current understanding
Inherited ichthyoses are genetic disorders of keratinization/cornification characterized clinically by persistent scaling and hyperkeratosis, often with erythema, fissuring, pruritus, and susceptibility to infection, reflecting defective epidermal barrier function. (fioretti2024comprehensivemolecularanalysis pages 1-2, panda2025moleculargeneticsand pages 2-3, ho2024alteredskinmicrobiome pages 2-4)

A 2024 cohort paper summarizes the diagnostic principle that clinical phenotype and family history guide suspicion, but molecular diagnosis is required for correct classification: **“only the identification of the genetic defect allows the correct classification.”** (Fioretti 2024, *Biomedicines*, published May 2024; https://doi.org/10.3390/biomedicines12051112) (fioretti2024comprehensivemolecularanalysis pages 1-2)

### Key identifiers
From the retrieved evidence set, explicit code mappings (ICD‑10/ICD‑11/MeSH/OMIM/Orphanet/MONDO) were not captured as structured fields. An ICD‑10 anchor frequently used clinically for congenital ichthyosis is Q80.* (not directly supported by the retrieved evidence, so not asserted).

**Evidence limitation:** Because OMIM/Orphanet/MONDO/MeSH identifiers are not present in the retrieved full texts/chunks, this report cannot provide verified identifier lists without additional database retrieval.

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in genes required for epidermal barrier formation, cornified envelope assembly, keratin cytoskeleton integrity, and epidermal lipid metabolism. In multiple sources, inherited ichthyosis is described as involving **>50 genes**. (xiang2025theclinicalspectrum pages 1-2, fioretti2024comprehensivemolecularanalysis pages 1-2, panda2025moleculargeneticsand pages 2-3)

**Key genetic etiologies highlighted in recent clinical cohorts and reviews:**
- ARCI genes: **TGM1, ALOX12B, CYP4F22, ABCA12, ALOXE3, NIPAL4, CERS3, PNPLA1, SDR9C7** (diociaiuti2024crosssectionalstudyon pages 4-5, diociaiuti2024crosssectionalstudyon media 464df4f0)
- Common ichthyosis types: **FLG** (ichthyosis vulgaris), **STS** (X‑linked ichthyosis), **ABCA12** (harlequin ichthyosis), **TGM1** (lamellar ichthyosis) (panda2025moleculargeneticsand pages 3-4, fioretti2024comprehensivemolecularanalysis pages 1-2)

### 2.2 Risk factors
- **Genetic:** Having biallelic pathogenic variants in ARCI genes (autosomal recessive), or hemizygous pathogenic variants/deletions for X‑linked forms; positive family history and consanguinity increase risk for recessive forms (the latter is implied by recessive genetics; explicit consanguinity statistics were not retrieved in the current evidence set). (fioretti2024comprehensivemolecularanalysis pages 2-3)
- **Clinical complication risk:** High burden of microbial infections is common in congenital ichthyosis cohorts (e.g., 94.4% in one study), consistent with barrier defect–mediated infection susceptibility. (ho2024alteredskinmicrobiome pages 2-4)

### 2.3 Protective factors and GxE
No protective genetic variants or explicit gene–environment interaction studies were retrieved in the available corpus; therefore, no evidence-based protective factors can be asserted.

---

## 3. Phenotypes

### 3.1 Core phenotypes (with recent frequency data)
A 2024 Italian ARCI cohort (n=74) quantified several common features (selected examples):
- **Hypohidrosis:** 54/74 (73.0%) (HPO suggestion: *Hypohidrosis* [HP:0000966]) (diociaiuti2024crosssectionalstudyon pages 4-5)
- **Heat intolerance:** 46/74 (62.2%) (HPO: *Heat intolerance* [HP:0002046]) (diociaiuti2024crosssectionalstudyon pages 4-5)
- **Ear deformities:** 22/74 (29.7%) (HPO: *Abnormality of the ear* [HP:0000598]) (diociaiuti2024crosssectionalstudyon pages 4-5)
- **Alopecia:** 16/74 (21.6%) (HPO: *Alopecia* [HP:0001596]) (diociaiuti2024crosssectionalstudyon pages 4-5)

A 2024 Southeast Asian congenital ichthyosis study (n=36) reported very high symptom/complication burden:
- **Hyperkeratosis:** 100% (HPO: *Hyperkeratosis* [HP:0000962])
- **Itch (pruritus):** 97.2% (HPO: *Pruritus* [HP:0000989])
- **Microbial infection:** 94.4% (HPO: *Recurrent infections* [HP:0002719] or *Skin infection* [HP:0001045])
- **Erythroderma:** 72.2% (HPO: *Erythroderma* [HP:0001019]) (ho2024alteredskinmicrobiome pages 2-4)

### 3.2 Phenotype characteristics (onset, progression)
- Many subtypes are congenital or present in the first months of life, including collodion membrane presentations in ARCI. In a 2024 diagnostic cohort, 6/17 were born encased in a collodion membrane (3 improved after shedding), while 11/17 had scaling at birth or in the first month. (fioretti2024comprehensivemolecularanalysis pages 2-3)
- Course is typically chronic, with severity varying by genotype and subtype (e.g., higher mean severity scores in TGM1 and ABCA12 groups vs other ARCI genes). (diociaiuti2024crosssectionalstudyon pages 4-5, diociaiuti2024crosssectionalstudyon media 464df4f0)

### 3.3 Quality of life (QoL)
- Congenital ichthyosis is consistently described as having substantial QoL impact, with severe itch and complications; one prospective qualitative study (NCT05610306) specifically targeted biological/psychological/social impacts and care gaps in adults ≥30 years with congenital ichthyosis. (NCT05610306 chunk 1)
- A 2024 congenital ichthyosis cohort study reported mental health difficulty in **53% (19/36)** of patients, emphasizing psychosocial burden. (ho2024alteredskinmicrobiome pages 2-4)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (high-confidence examples from recent cohorts)
**ARCI (example gene distribution in a 2024 Italian cohort, n=74):**
- TGM1: 18/74 (24.3%)
- ALOX12B: 18/74 (24.3%)
- CYP4F22: 12/74 (16.2%)
- ABCA12: 9/74 (12.2%)
- ALOXE3: 7/74 (9.5%)
- NIPAL4: 7/74 (9.5%)
- CERS3 / PNPLA1 / SDR9C7: 1/74 each (1.4%) (diociaiuti2024crosssectionalstudyon pages 4-5, diociaiuti2024crosssectionalstudyon media 464df4f0)

**Visual evidence (gene frequencies and severity scores):** (diociaiuti2024crosssectionalstudyon media 464df4f0)

### 4.2 Pathogenic variant classes and consequences
Across cohorts, variant classes include SNVs/indels and structural variants (e.g., microduplications in **TGM1** and microdeletions affecting **CYP4F22** and **NIPAL4** in the Italian ARCI study). (diociaiuti2024crosssectionalstudyon pages 4-5)

Mechanistic consequence examples (review-level):
- X‑linked ichthyosis: STS deficiency leading to cholesterol sulfate accumulation and barrier disruption (review summary). (panda2025moleculargeneticsand pages 1-2, panda2025moleculargeneticsand pages 2-3)

**Direct mechanistic quote (review-level framing):** **“The disturbance in the epidermal barrier function is at the core of ichthyosis pathogenesis.”** (panda2025moleculargeneticsand pages 2-3)

### 4.3 Modifier genes, epigenetics
No modifier-gene or epigenetic datasets specific to inherited ichthyosis were retrieved in the current corpus.

---

## 5. Environmental information

Inherited ichthyosis is primarily genetic. Environmental factors in the retrieved sources are mainly relevant to *complications* and *management* (e.g., infection risk and wound care). A detailed toxin/lifestyle exposure literature was not retrieved; thus no evidence-based environmental risk factor list is provided.

---

## 6. Mechanism / pathophysiology

### 6.1 Barrier defect → inflammation → infection susceptibility
A mechanistic chain supported by 2024 data:
1) Germline variants in barrier/cornification genes and lipid metabolism genes →
2) Altered epidermal structure and barrier permeability →
3) Dysbiosis with reduced commensals and increased pathogenic colonization →
4) Systemic and cutaneous immune activation (Th17/Th2 and JAK/STAT signatures) →
5) Clinical manifestations: scaling/hyperkeratosis, pruritus, infections, impaired wound healing.

The 2024 Southeast Asian study explicitly links microbiome changes and immune signaling: **“Microbiome meta-analysis revealed distinct microbial populations, reduced commensal microbiota, and higher colonization by pathogenic species. This correlated with increased production of inflammatory cytokines, including Th17 and JAK/STAT signaling, in peripheral blood mononuclear cells.”** (Ho 2024, *Human Genomics*, Apr 2024; https://doi.org/10.1186/s40246-024-00603-x) (ho2024alteredskinmicrobiome pages 1-2)

Additional quantitative immuno-microbiome findings include elevated neutrophils across congenital ichthyosis clusters and increased STAT3 phosphorylation (pY705) in several dysbiosis clusters, consistent with JAK/STAT pathway activation. (ho2024alteredskinmicrobiome pages 10-13)

### 6.2 Cell types (CL) and GO terms (suggestions)
Based on inflammation and barrier biology reported:
- **Cell types (CL term suggestions):**
  - Keratinocyte (CL:0000312)
  - Neutrophil (CL:0000775)
  - CD4-positive, alpha-beta T cell (CL:0000624) including Th17 and Th2 subsets
  - Peripheral blood mononuclear cell (broad category; not a single CL type)

- **GO biological process term suggestions:**
  - Keratinization (GO:0031424)
  - Epidermis development (GO:0008544)
  - Skin barrier establishment (GO:0061436)
  - Defense response to bacterium (GO:0042742)
  - IL‑17 signaling pathway (GO:0038111)
  - JAK‑STAT cascade (GO:0007259)

### 6.3 Model organism / experimental mechanism note
A review source notes that **SMS2 knockout** in mice produced an ichthyotic phenotype with epidermal hyperplasia and hyperkeratosis, supporting lipid pathway involvement in barrier integrity. (panda2025moleculargeneticsand pages 2-3)

---

## 7. Anatomical structures affected

### Organ/tissue level
- Primary: skin/epidermis (UBERON suggestion: skin UBERON:0002097; epidermis UBERON:0001003).
- Common secondary involvement in cohorts includes wounds/infections and complications such as sepsis in severe subtypes. In the 2024 congenital ichthyosis cohort, lethal infant sepsis occurred in **6** cases (4 HI, 1 LI, 1 EI). (ho2024alteredskinmicrobiome pages 2-4)

### Subcellular/cellular compartments (GO cellular component suggestions)
- Cornified envelope (GO:0001533)
- Keratin filament (GO:0045095)
- Lamellar body (GO:0042599) (suggested by ARCI ultrastructural discussion context; direct GO mapping not explicitly provided in the evidence corpus)

---

## 8. Temporal development

- **Onset:** Many forms are congenital/early infancy, including collodion membrane presentations in ARCI (see diagnostic cohort description). (fioretti2024comprehensivemolecularanalysis pages 2-3)
- **Course:** Chronic lifelong disease with variable severity, influenced by genotype; a 2024 ARCI cohort demonstrated gene-associated severity differences (e.g., higher mean severity in TGM1 vs CYP4F22). (diociaiuti2024crosssectionalstudyon pages 4-5, diociaiuti2024crosssectionalstudyon media 464df4f0)

---

## 9. Inheritance and population

### Inheritance patterns
- ARCI is typically autosomal recessive with biallelic variants in barrier/lipid pathway genes (e.g., TGM1, ALOX12B). (diociaiuti2024crosssectionalstudyon pages 4-5, fioretti2024comprehensivemolecularanalysis pages 2-3)
- X‑linked ichthyosis affects males with X‑linked STS involvement (XLI/XLRI). (fioretti2024comprehensivemolecularanalysis pages 1-2, marathe2023topicalisotretinoin(tmb001) pages 1-3)

### Epidemiology (recently cited quantitative estimates)
A 2024 molecular diagnostic paper cited global frequency estimates:
- **ARCI prevalence:** ~**1:100,000–300,000** worldwide
- **X‑linked ichthyosis incidence:** ~**1:2000–1:6000 male newborns** (fioretti2024comprehensivemolecularanalysis pages 1-2)

A 2023 review excerpt (from *Nature Reviews Disease Primers*) includes country-level prevalence figures presented in mixed formats; for example, it lists the United States as **200,000 patients (61 per 100,000)**. (gutierrezcerrajero2023ichthyosis pages 11-13)

**Evidence caveat:** The extracted 2023 primer chunks available in this tool run are not the full article and include tabulated prevalence figures without full definitional context; therefore, these values should be treated as secondary/compiled epidemiology rather than primary incidence studies. (gutierrezcerrajero2023ichthyosis pages 11-13)

---

## 10. Diagnostics

### 10.1 Clinical evaluation and pathology
Clinical evaluation plus family history guides initial classification, but phenotypic overlap and evolution can make subtyping difficult. The 2024 NGS study emphasizes that definitive classification requires DNA analysis. (fioretti2024comprehensivemolecularanalysis pages 2-3)

Review-level sources note that confirmation may include skin biopsy histology and electron microscopy in selected settings. (panda2025moleculargeneticsand pages 1-2)

### 10.2 Genetic testing (current real-world implementation)
**Multi-gene NGS panels / WES/WGS:**
- A 2024 Italian series used targeted filtering across **54 ichthyosis/erythrokeratoderma genes** in a high‑coverage NGS workflow and achieved molecular diagnosis in all 17/17 patients. (fioretti2024comprehensivemolecularanalysis pages 2-3)
- The authors conclude comprehensive molecular testing can function as a first-tier diagnostic classifier for nonsyndromic ichthyosis. (fioretti2024comprehensivemolecularanalysis pages 1-2)

**Direct quote (diagnostic rationale):** **“only the identification of the genetic defect allows the correct classification.”** (fioretti2024comprehensivemolecularanalysis pages 1-2)

### 10.3 Differential diagnosis
Not systematically extractable from this evidence corpus; however, the diagnostic cohorts emphasize overlap across ichthyosis subtypes and the need for genetic confirmation. (fioretti2024comprehensivemolecularanalysis pages 2-3)

---

## 11. Outcome / prognosis

Severity and complications vary strongly by subtype and genotype.

**Infection/sepsis outcomes (2024 congenital ichthyosis cohort):**
- **6 lethal infant sepsis cases** (4 HI, 1 LI, 1 EI)
- **10 treatable childhood sepsis cases** (HI 3/8; IV 7/15) (ho2024alteredskinmicrobiome pages 2-4)

**Evidence limitation:** Survival/life expectancy estimates for specific inherited ichthyosis subtypes were not comprehensively retrieved (outside this cohort’s sepsis outcomes).

---

## 12. Treatment

### 12.1 Standard-of-care (symptomatic) therapy (general)
Symptom-directed care typically includes emollients/humectants/keratolytics and, in more severe disease, systemic retinoids; however, this report emphasizes recent targeted therapeutics and trial evidence because detailed guideline text was not available in the retrieved corpus. (panda2025moleculargeneticsand pages 2-3)

### 12.2 Recent developments (2023–2024): topical retinoid formulation (TMB‑001)
**Topical isotretinoin (TMB‑001), Phase 2b CONTROL study (published May 2023):**
- Population: participants ≥9 years with confirmed XLRI or ARCI‑lamellar ichthyosis; n=33 randomized 1:1:1. (marathe2023topicalisotretinoin(tmb001) pages 1-3)
- Efficacy responders reported in excerpt: **VIIS‑50** achieved by **64% / 40% / 33%** (TMB‑001 0.05% / 0.1% / vehicle) and **IGA success** by **55% / 40% / 8%**, with mean baseline BSA affected 74%. (marathe2023topicalisotretinoin(tmb001) pages 3-4)
- Safety: **“Topical isotretinoin (tmb-001) treatment for 12 weeks did not result in clinically relevant laboratory abnormalities…”** (Marathe 2023, *Dermatology and Therapy*, May 2023; https://doi.org/10.1007/s13555-023-00923-1). (marathe2023topicalisotretinoin(tmb001) pages 1-3)

**Application/implementation:** The study highlights a potential path to retinoid efficacy with reduced systemic laboratory toxicity compared with oral retinoids, which are known to cause clinically significant lab changes. (marathe2023topicalisotretinoin(tmb001) pages 1-3)

**MAXO suggestions:** topical retinoid therapy; topical keratolytic therapy (ontology IDs not retrieved in corpus).

### 12.3 Recent developments: topical gene therapy for TGM1-deficient ARCI (KB105)
**KB105 (HSV‑1 vector expressing human TGM1; topical gel):**
- **Phase I/II registry (NCT04047732; first posted 2019):** intra‑patient comparison; up to 6 adults with genetically confirmed TGM1-deficient ARCI (null mutation) and lamellar ichthyosis; includes immunofluorescence measurement of TG1 in treated skin. (https://clinicaltrials.gov/study/NCT04047732) (NCT04047732 chunk 1)
- **Phase 2 registry (NCT05735158; posted 2023):** intrasubject randomized, placebo-controlled, triple-masked study; enrollment 15; includes participants ≥6 months with genetically confirmed TGM1-deficient ARCI and lamellar ichthyosis; weekly application; primary endpoint composite IGA responder at Week 9. (https://clinicaltrials.gov/study/NCT05735158) (NCT05735158 chunk 1)

**Expert/authoritative interpretation:** These trials operationalize a pathogenesis‑based approach (gene replacement in skin) enabled by localized topical delivery, aligning with review-level framing that gene therapy is emerging for ichthyosis. (panda2025moleculargeneticsand pages 1-2)

**MAXO suggestions:** gene therapy; topical gene delivery (IDs not retrieved in corpus).

### 12.4 Biologics / immune-phenotype–guided therapy
**Secukinumab (anti‑IL‑17A) in ichthyoses, Phase 2 trial:**
- NCT03041038: randomized, crossover, quadruple‑masked Phase 2; n=20; included ARCI (LI/CIE), epidermolytic ichthyosis, and Netherton syndrome; primary efficacy outcome reduction at Week 16 in Ichthyosis Area Severity Index (IASI). (NCT03041038 chunk 1)

**Dupilumab repurposing trial for pruritic genetic inflammatory skin disorders (includes genetic skin disorders; ichthyosis may be included depending on phenotype):**
- NCT05649098: open-label pilot; n=30; primary goal is improvement in itch, targeting ≥50% of patients achieving ≥2‑point Worst Itch NRS reduction. (NCT05649098 chunk 1)

**Mechanism–application link:** The observed Th17/JAK/STAT activation and infection susceptibility in congenital ichthyosis supports the clinical rationale for immunomodulatory trials in selected immune-phenotypes. (ho2024alteredskinmicrobiome pages 1-2, NCT03041038 chunk 1)

---

## 13. Prevention

Primary prevention of inherited ichthyosis is limited (genetic disorders), but **secondary prevention** is feasible via early genetic diagnosis and counseling; diagnostic studies emphasize that NGS enables precise diagnosis and genetic counseling. (fioretti2024comprehensivemolecularanalysis pages 1-2, fioretti2024comprehensivemolecularanalysis pages 2-3)

---

## 14. Other species / natural disease

No OMIA/veterinary natural disease evidence was retrieved in this tool run; cannot be asserted.

---

## 15. Model organisms

Evidence in this corpus is limited; one review reports an ichthyosis-like phenotype in **SMS2 knockout mice**, supporting sphingomyelin/lipid pathway contributions to epidermal homeostasis. (panda2025moleculargeneticsand pages 2-3)

---

## Recent quantitative findings summary (for knowledge base ingestion)
The table below consolidates key 2023–2024 quantitative findings across genetics, cohorts, mechanistic studies, and therapeutic trials.

| Study / dataset | Year | Population / design | Key quantitative findings | URL | Citations |
|---|---:|---|---|---|---|
| Diociaiuti et al., Italian ARCI cohort | 2024 | Cross-sectional single-center cohort of 74 genetically diagnosed ARCI patients | Subtypes: lamellar ichthyosis 50/74 (67.5%), CIE 18/74 (24.3%), harlequin ichthyosis 2/74 (2.7%), other ARCI 4/74 (5.4%). Mutated genes: **TGM1** 18/74 (24.3%), mean severity score **40.3 ± 14.1**; **ALOX12B** 18/74 (24.3%), **23.2 ± 11.3**; **CYP4F22** 12/74 (16.2%), **17.9 ± 5.1**; **ABCA12** 9/74 (12.2%; higher severity than most other genes); **ALOXE3** 7/74 (9.5%); **NIPAL4** 7/74 (9.5%); **CERS3**, **PNPLA1**, **SDR9C7** 1/74 each (1.4%). 83 distinct sequence variants, including 25 previously undescribed; 2 microduplications in TGM1 and 2 microdeletions affecting CYP4F22/NIPAL4. Frequent features: hypohidrosis 54/74 (73.0%), heat intolerance 46/74 (62.2%), ear deformities 22/74 (29.7%), alopecia 16/74 (21.6%). | https://doi.org/10.1159/000536366 | (diociaiuti2024crosssectionalstudyon pages 4-5, diociaiuti2024crosssectionalstudyon media 464df4f0) |
| Fioretti et al., NGS first-tier molecular testing | 2024 | 17 unrelated Italian patients with nonsyndromic ichthyosis; massively parallel sequencing of >50 ichthyosis-related genes; unaffected comparison set n=300 | Molecular cause identified in **17/17 (100%)**. Diagnoses: **8/17 ARCI** (ALOX12B, NIPAL4, TGM1), **3/17** with biallelic **FLG** loss-of-function, **6/11 males** with X-linked ichthyosis. **24** disease-causing alleles detected, including **8 novel** variants; included a synonymous **TGM1** variant causing a splicing defect. Study supports multigene NGS as an effective first-tier diagnostic/classification test. | https://doi.org/10.3390/biomedicines12051112 | (fioretti2024comprehensivemolecularanalysis pages 1-2, fioretti2024comprehensivemolecularanalysis pages 2-3) |
| Marathe et al., TMB-001 CONTROL Phase 2b | 2023 | Randomized, double-blind, vehicle-controlled phase 2b trial; participants ≥9 years with genetically confirmed XLRI or ARCI-lamellar ichthyosis | **33** enrolled: TMB-001 0.05% **n=11**, TMB-001 0.1% **n=10**, vehicle **n=12**; subtype split **52% ARCI-LI / 48% XLRI**. Key efficacy: **VIIS-50** achieved by **64% / 40% / 33%** (0.05% / 0.1% / vehicle); **IGA success** by **55% / 40% / 8%**. Mean baseline BSA affected **74%**. Safety: 3/33 (**9%**) withdrew due to treatment-emergent AEs; **no serious AEs or deaths**; laboratory abnormalities were isolated/asymptomatic and authors reported **no clinically significant laboratory changes** through 12 weeks. | https://doi.org/10.1007/s13555-023-00923-1 | (marathe2023topicalisotretinoin(tmb001) pages 3-4, marathe2023topicalisotretinoin(tmb001) pages 1-3, NCT04154293 chunk 2) |
| Ho et al., microbiome / inflammation / JAK-STAT study | 2024 | Southeast Asian case-control study with congenital ichthyosis patients and healthy controls; WES plus skin metagenomics and immune profiling | Cohort: **36 CI patients + 15 controls** (total 51); mean age **10.2 years**, median follow-up **4.3 years**. Subtypes: IV **15**, HI **8**, LI **3**, EI **4**, TTD **3**, ARC **1**, SLS **2**. Clinical burden: hyperkeratosis **100%**, itch **97.2%**, microbial infection **94.4%**, erythroderma **72.2%**, mental health difficulty **53% (19/36)**. Sepsis: **6 lethal infant cases** (4 HI, 1 LI, 1 EI) plus **10 treatable childhood sepsis cases** (HI 3/8; IV 7/15). Genetics: **20 novel + 31 recurrent/pathogenic variants**. Mechanistic findings: reduced commensals, increased pathogenic colonization, elevated **Th17** and **JAK/STAT** signaling; all CI clusters showed elevated neutrophils, eosinophils elevated in one cluster, and **STAT3 pY705** increased in P2/P3/P4. | https://doi.org/10.1186/s40246-024-00603-x | (ho2024alteredskinmicrobiome pages 10-13, ho2024alteredskinmicrobiome pages 1-2, ho2024alteredskinmicrobiome pages 2-4) |
| KB105 topical gene therapy, NCT04047732 | 2019 registry record | Phase I/II intra-patient topical gene therapy trial for TGM1-deficient ARCI | Planned enrollment **up to 6 adults**. KB105 is a replication-incompetent, non-integrating HSV-1 vector expressing human **TGM1** in topical gel. Key inclusion: genetically confirmed **TGM1-deficient ARCI** with a **null TGM1 mutation**, clinical diagnosis of lamellar ichthyosis, age **≥18 years**, target-area IGA **3–4**. Primary focus: safety/tolerability and IGA improvement over ~12 weeks. | https://clinicaltrials.gov/study/NCT04047732 | (NCT04047732 chunk 1) |
| KB105 topical gene therapy, NCT05735158 | 2023 registry record | Phase 2, intrasubject randomized, placebo-controlled, triple-masked study of topical KB105 | Planned enrollment **15** children/adults. Weekly topical KB105 vs matched placebo on paired target areas, with optional open-label area. Key inclusion: age **≥6 months**, genetically confirmed **TGM1-deficient ARCI**, clinical diagnosis of lamellar ichthyosis, paired target areas with same scaling severity and severity **≥3**. Primary endpoint: composite IGA responder at **Week 9**. | https://clinicaltrials.gov/study/NCT05735158 | (NCT05735158 chunk 1) |


*Table: This table compiles recent quantitative findings across genetics, clinical cohorts, immune/microbiome studies, and therapeutic trials in inherited ichthyosis. It highlights sample sizes, subtype distributions, gene frequencies, severity metrics, and design features most useful for a disease knowledge base.*

---

## Evidence gaps (what is not currently supported by the retrieved corpus)
- Verified MONDO/Orphanet/OMIM/MeSH/ICD mappings for the umbrella term “inherited ichthyosis”.
- Comprehensive modifier gene / epigenetic associations.
- Systematic environmental risk/protective factors.
- Detailed guideline algorithms for treatment stratified by subtype (a 2024 guideline update appears in search results but was unobtainable in this run).



References

1. (xiang2025theclinicalspectrum pages 1-2): Ruiyu Xiang, Xin Huang, Yihe Liu, Shuya Sun, Di Hua, Ran Mo, Yong Yang, and Zhiming Chen. The clinical spectrum of rare inherited ichthyosis in china: a review of thirty-five cases. Acta Dermato-Venereologica, Jul 2025. URL: https://doi.org/10.2340/actadv.v105.41100, doi:10.2340/actadv.v105.41100. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (fioretti2024comprehensivemolecularanalysis pages 1-2): Tiziana Fioretti, Fabrizio Martora, Ilaria De Maggio, Adelaide Ambrosio, Carmelo Piscopo, Sabrina Vallone, Felice Amato, Diego Passaro, Fabio Acquaviva, Francesca Gaudiello, Daniela Di Girolamo, Valeria Maiolo, Federica Zarrilli, Speranza Esposito, Giuseppina Vitiello, Luigi Auricchio, Elena Sammarco, Daniele De Brasi, Roberta Petillo, Antonella Gambale, Fabio Cattaneo, Rosario Ammendola, Paola Nappa, and Gabriella Esposito. Comprehensive molecular analysis of disease-related genes as first-tier test for early diagnosis, classification, and management of patients affected by nonsyndromic ichthyosis. Biomedicines, 12:1112, May 2024. URL: https://doi.org/10.3390/biomedicines12051112, doi:10.3390/biomedicines12051112. This article has 2 citations.

3. (panda2025moleculargeneticsand pages 2-3): Suman Panda. Molecular genetics and pathogenesis of ichthyosis. Annals of Medical and Surgical Dermatology, Jan 2025. URL: https://doi.org/10.61577/amsd.2023.100004, doi:10.61577/amsd.2023.100004. This article has 1 citations.

4. (marathe2023topicalisotretinoin(tmb001) pages 1-3): Kalyani Marathe, Joyce M. C. Teng, Scott Guenthner, Christopher G. Bunick, Steven Kempers, Kimmie Eads, Leslie Castelo-Soccio, Alan M. Mendelsohn, Jessica Raiz, and Dédée F. Murrell. Topical isotretinoin (tmb-001) treatment for 12 weeks did not result in clinically relevant laboratory abnormalities in participants with congenital ichthyosis in the phase 2b control study. Dermatology and Therapy, 13:1255-1264, May 2023. URL: https://doi.org/10.1007/s13555-023-00923-1, doi:10.1007/s13555-023-00923-1. This article has 6 citations.

5. (ho2024alteredskinmicrobiome pages 2-4): Minh Ho, Huynh-Nga Nguyen, Minh Van Hoang, Tien Thuy Thi Bui, Bao-Quoc Vu, Truc Huong Thi Dinh, Hoa Thi My Vo, Diana C. Blaydon, Sherif A. Eldirany, Christopher G. Bunick, and Chi-Bao Bui. Altered skin microbiome, inflammation, and jak/stat signaling in southeast asian ichthyosis patients. Human Genomics, Apr 2024. URL: https://doi.org/10.1186/s40246-024-00603-x, doi:10.1186/s40246-024-00603-x. This article has 14 citations and is from a peer-reviewed journal.

6. (fioretti2024comprehensivemolecularanalysis pages 2-3): Tiziana Fioretti, Fabrizio Martora, Ilaria De Maggio, Adelaide Ambrosio, Carmelo Piscopo, Sabrina Vallone, Felice Amato, Diego Passaro, Fabio Acquaviva, Francesca Gaudiello, Daniela Di Girolamo, Valeria Maiolo, Federica Zarrilli, Speranza Esposito, Giuseppina Vitiello, Luigi Auricchio, Elena Sammarco, Daniele De Brasi, Roberta Petillo, Antonella Gambale, Fabio Cattaneo, Rosario Ammendola, Paola Nappa, and Gabriella Esposito. Comprehensive molecular analysis of disease-related genes as first-tier test for early diagnosis, classification, and management of patients affected by nonsyndromic ichthyosis. Biomedicines, 12:1112, May 2024. URL: https://doi.org/10.3390/biomedicines12051112, doi:10.3390/biomedicines12051112. This article has 2 citations.

7. (diociaiuti2024crosssectionalstudyon pages 4-5): Andrea Diociaiuti, Marialuisa Corbeddu, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Tonia Samela, Simona Giancristoforo, Adriano Angioni, Giovanna Zambruno, Antonio Novelli, Rita Alaggio, Damiano Abeni, and May El Hachem. Cross-sectional study on autosomal recessive congenital ichthyoses: association of genotype with disease severity, phenotypic, and ultrastructural features in 74 italian patients. Dermatology (Basel, Switzerland), 240:397-413, Apr 2024. URL: https://doi.org/10.1159/000536366, doi:10.1159/000536366. This article has 10 citations.

8. (diociaiuti2024crosssectionalstudyon media 464df4f0): Andrea Diociaiuti, Marialuisa Corbeddu, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Tonia Samela, Simona Giancristoforo, Adriano Angioni, Giovanna Zambruno, Antonio Novelli, Rita Alaggio, Damiano Abeni, and May El Hachem. Cross-sectional study on autosomal recessive congenital ichthyoses: association of genotype with disease severity, phenotypic, and ultrastructural features in 74 italian patients. Dermatology (Basel, Switzerland), 240:397-413, Apr 2024. URL: https://doi.org/10.1159/000536366, doi:10.1159/000536366. This article has 10 citations.

9. (panda2025moleculargeneticsand pages 3-4): Suman Panda. Molecular genetics and pathogenesis of ichthyosis. Annals of Medical and Surgical Dermatology, Jan 2025. URL: https://doi.org/10.61577/amsd.2023.100004, doi:10.61577/amsd.2023.100004. This article has 1 citations.

10. (NCT05610306 chunk 1):  Quality of Life in Middle-aged and Older Patients With Congenital Ichthyosis. Maastricht University Medical Center. 2022. ClinicalTrials.gov Identifier: NCT05610306

11. (panda2025moleculargeneticsand pages 1-2): Suman Panda. Molecular genetics and pathogenesis of ichthyosis. Annals of Medical and Surgical Dermatology, Jan 2025. URL: https://doi.org/10.61577/amsd.2023.100004, doi:10.61577/amsd.2023.100004. This article has 1 citations.

12. (ho2024alteredskinmicrobiome pages 1-2): Minh Ho, Huynh-Nga Nguyen, Minh Van Hoang, Tien Thuy Thi Bui, Bao-Quoc Vu, Truc Huong Thi Dinh, Hoa Thi My Vo, Diana C. Blaydon, Sherif A. Eldirany, Christopher G. Bunick, and Chi-Bao Bui. Altered skin microbiome, inflammation, and jak/stat signaling in southeast asian ichthyosis patients. Human Genomics, Apr 2024. URL: https://doi.org/10.1186/s40246-024-00603-x, doi:10.1186/s40246-024-00603-x. This article has 14 citations and is from a peer-reviewed journal.

13. (ho2024alteredskinmicrobiome pages 10-13): Minh Ho, Huynh-Nga Nguyen, Minh Van Hoang, Tien Thuy Thi Bui, Bao-Quoc Vu, Truc Huong Thi Dinh, Hoa Thi My Vo, Diana C. Blaydon, Sherif A. Eldirany, Christopher G. Bunick, and Chi-Bao Bui. Altered skin microbiome, inflammation, and jak/stat signaling in southeast asian ichthyosis patients. Human Genomics, Apr 2024. URL: https://doi.org/10.1186/s40246-024-00603-x, doi:10.1186/s40246-024-00603-x. This article has 14 citations and is from a peer-reviewed journal.

14. (gutierrezcerrajero2023ichthyosis pages 11-13): Carlos Gutiérrez-Cerrajero, Eli Sprecher, Amy S. Paller, Masashi Akiyama, Juliette Mazereeuw-Hautier, Angela Hernández-Martín, and Rogelio González-Sarmiento. Ichthyosis. Nature Reviews Disease Primers, 9:1-23, Jan 2023. URL: https://doi.org/10.1038/s41572-022-00412-3, doi:10.1038/s41572-022-00412-3. This article has 93 citations.

15. (marathe2023topicalisotretinoin(tmb001) pages 3-4): Kalyani Marathe, Joyce M. C. Teng, Scott Guenthner, Christopher G. Bunick, Steven Kempers, Kimmie Eads, Leslie Castelo-Soccio, Alan M. Mendelsohn, Jessica Raiz, and Dédée F. Murrell. Topical isotretinoin (tmb-001) treatment for 12 weeks did not result in clinically relevant laboratory abnormalities in participants with congenital ichthyosis in the phase 2b control study. Dermatology and Therapy, 13:1255-1264, May 2023. URL: https://doi.org/10.1007/s13555-023-00923-1, doi:10.1007/s13555-023-00923-1. This article has 6 citations.

16. (NCT04047732 chunk 1):  Topical KB105 Gene Therapy for the Treatment of TGM1-deficient Autosomal Recessive Congenital Ichthyosis (ARCI). Krystal Biotech, Inc.. 2019. ClinicalTrials.gov Identifier: NCT04047732

17. (NCT05735158 chunk 1):  Topical KB105 for the Treatment of TGM1-deficient Autosomal Recessive Congenital Ichthyosis (ARCI). Krystal Biotech, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05735158

18. (NCT03041038 chunk 1): Amy Paller. The Efficacy and Safety of Secukinumab in Patients With Ichthyoses. Northwestern University. 2016. ClinicalTrials.gov Identifier: NCT03041038

19. (NCT05649098 chunk 1): Amy Paller. Repurposing Dupilumab for Management of Pruritic Genetic Inflammatory Skin Disorders. Northwestern University. 2023. ClinicalTrials.gov Identifier: NCT05649098

20. (NCT04154293 chunk 2):  A Vehicle Controlled Study to Evaluate Safety and Efficacy of Topical TMB-001 for Treatment of Congenital Ichthyosis. Timber Pharmaceuticals Inc.. 2019. ClinicalTrials.gov Identifier: NCT04154293