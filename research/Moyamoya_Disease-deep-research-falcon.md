---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T18:26:49.281789'
end_time: '2026-05-04T18:43:42.646899'
duration_seconds: 1013.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Moyamoya Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Moyamoya Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Moyamoya Disease** covering all of the
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
- **Disease Name:** Moyamoya Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Moyamoya Disease** covering all of the
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


# Moyamoya Disease (MMD): Comprehensive Disease Characteristics Report (2023–2025 prioritized)

## 1. Disease Information

### 1.1 Concise overview
Moyamoya disease (MMD) is a chronic, progressive cerebrovascular arteriopathy characterized by stenosis/occlusion centered on the terminal intracranial internal carotid arteries (and proximal branches) with development of abnormal collateral networks that produce a classic “moyamoya” (“puff-of-smoke”) appearance on angiography and related imaging (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 2-3, uchiyama2024adultmoyamoyadisease pages 2-3, uchiyama2024adultmoyamoyadisease pages 3-4).

Direct abstract quote (management review, 2024): “Moyamoya disease (MMD) is characterized by idiopathic, progressive stenosis of the circle of Willis and the terminal portion of the internal carotid arteries with the development of prominent small collateral vessels and a characteristic moyamoya or puff-of-smoke radiographic appearance.” (Oct 2024, Journal of Neurosurgery; URL: https://doi.org/10.3171/2024.1.jns221977) (kappel2024managementofmoyamoya pages 1-2).

### 1.2 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
In the retrieved evidence, only OMIM:252350 was explicitly observed; MONDO, Orphanet (ORPHA), ICD-10/ICD-11 codes, and MeSH unique IDs were not present in the accessible excerpts (artifact-00). (kappel2024managementofmoyamoya pages 1-2, santos2025managementofmoyamoyab pages 3-4).

### 1.3 Common synonyms and alternative names
Common alternate labels used in the retrieved literature include *moyamoya vasculopathy*, *moyamoya arteriopathy*, *moyamoya syndrome (MMS)* (syndromic/secondary forms), and *quasi-moyamoya disease* (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2).

### 1.4 Evidence source type
The information in this report is derived primarily from aggregated disease-level resources (peer-reviewed reviews, meta-analyses, and primary research studies), rather than individual EHR-derived patient summaries (artifact-00). (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2).

| Field | Value | Notes/Evidence |
|---|---|---|
| Disease name | Moyamoya disease | Canonical name used throughout recent reviews; abbreviated MMD (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Abbreviation | MMD | Explicitly defined as “Moyamoya disease (MMD)” (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Related condition name | Moyamoya syndrome | Distinct term for moyamoya-like vasculopathy associated with other diseases/conditions; abbreviated MMS (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Abbreviation | MMS | Explicitly defined as “moyamoya syndrome (MMS)” (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Umbrella term / broader label | Moyamoya vasculopathy | Used as an umbrella term (MMV) in review literature (calandrelli2026moyamoyavasculopathyand pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Abbreviation | MMV | Explicitly defined as “Moyamoya vasculopathy (MMV)” (calandrelli2026moyamoyavasculopathyand pages 1-2) |
| Synonym / related descriptor | Moyamoya arteriopathy | Used in recent management review as a related descriptor (kappel2024managementofmoyamoya pages 1-2) |
| Synonym / related descriptor | Quasi-moyamoya disease | Reported as a synonym/related label for syndromic or associated forms in review literature (kappel2024managementofmoyamoya pages 1-2) |
| Synonym / related descriptor | Moyamoya-like vasculopathy | Used to describe associated/systemic-disease forms (uchiyama2024adultmoyamoyadisease pages 1-2) |
| Synonym / related descriptor | Moyamoya-like patterns | Used for atypical radiologic patterns within the moyamoya spectrum (calandrelli2026moyamoyavasculopathyand pages 1-2) |
| Descriptive imaging phrase | Puff-of-smoke appearance | Characteristic collateral appearance repeatedly cited as descriptive terminology rather than a formal synonym (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2) |
| OMIM | 252350 | Retrieved evidence includes OMIM:252350 linked to moyamoya disease in older literature snippets (uchiyama2024adultmoyamoyadisease media e5baf62b) |
| MONDO ID | Not found in retrieved sources | No explicit MONDO identifier present in the provided evidence excerpts (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Orphanet / ORPHA ID | Not found in retrieved sources | No explicit Orphanet identifier present in the provided evidence excerpts (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| ICD-10 code | Not found in retrieved sources | No explicit ICD-10 code present in the provided evidence excerpts (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| ICD-11 code | Not found in retrieved sources | No explicit ICD-11 code present in the provided evidence excerpts (calandrelli2026moyamoyavasculopathyand pages 1-2, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| MeSH descriptor | Moyamoya disease | MeSH-tagged disease term explicitly present in systematic-review indexing text, though no MeSH ID was provided in the evidence (santos2025managementofmoyamoyab pages 3-4, santos2025managementofmoyamoyaa pages 3-4) |
| MeSH ID | Not found in retrieved sources | Evidence shows MeSH term usage/subheadings but not the numeric/unique MeSH identifier (santos2025managementofmoyamoyab pages 3-4, santos2025managementofmoyamoyaa pages 3-4) |
| Evidence source level | Aggregated disease-level resources and reviews | Information summarized in retrieved evidence comes from reviews/guidelines and disease-level literature, not individual-patient EHR datasets (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |


*Table: This table compiles the key names, abbreviations, and formal identifiers for Moyamoya disease that were explicitly available in the retrieved evidence. It is useful for normalizing terminology for a disease knowledge base while clearly flagging identifiers not found in the provided sources.*

---

## 2. Etiology

### 2.1 Disease causal factors (genetic, environmental, mechanistic)
MMD is widely treated as a multifactorial disease with strong genetic susceptibility (most prominently RNF213 in East Asian populations) and additional environmental/inflammatory “second hits” contributing to penetrance and progression (kappel2024managementofmoyamoya pages 2-3, tan2024exploringrnf213in pages 4-6).

Key genetic susceptibility is emphasized in 2024–2025 reviews, including RNF213 and additional genes (e.g., ACTA2, DIAPH1, HLA, and rare Mendelian causes such as GUCY1A3 and BRCC3 in syndromic/familial contexts) (kappel2024managementofmoyamoya pages 1-2, he2025advancesinmoyamoya pages 8-10, he2025advancesinmoyamoya pages 13-14).

### 2.2 Risk factors
#### 2.2.1 Genetic risk factors
**RNF213 p.R4810K (c.14576G>A; founder in East Asia)** is strongly enriched among East Asian MMD patients compared with the general population, with reported patient frequencies Japanese 90.1%, Korean 78.9%, Chinese 23.1% versus population carrier frequencies Japanese 2.5%, Korean 2.7%, Chinese 0.9% (Jul 2024 review; URL: https://doi.org/10.1159/000540254) (uchiyama2024adultmoyamoyadisease pages 2-3). A 2024 review further summarizes very large effect sizes in meta-analysis (ORs ~184 Japan, ~110 Korea, ~32 China) and also reports association with overall stroke risk in broader cohorts (OR 1.91, 95% CI 1.55–2.36) (Dec 2024 review; URL: https://doi.org/10.3390/biomedicines13010017) (tan2024exploringrnf213in pages 2-4).

**Incomplete penetrance and zygosity effects**: a 2024 RNF213-focused review reports low penetrance among heterozygotes (“1/150–1/300 of heterozygous carriers actually develop MMD”) with much higher incidence among homozygotes (“exceeding 78%”), emphasizing the need for additional modifiers and caution about population screening (tan2024exploringrnf213in pages 4-6).

#### 2.2.2 Environmental/clinical risk factors and triggers
**Radiation exposure** is emphasized as a risk factor for moyamoya syndrome (secondary moyamoya arteriopathy) (kappel2024managementofmoyamoya pages 2-3).

**Infectious/immune exposure as a progression modifier (gene–environment interaction)**: In a prospective cohort of 275 MMD patients, both RNF213 p.R4810K carrier status and a composite infectious-burden (IB) score were independently associated with more severe intracranial stenosis (Willis narrowing score). The RNF213 variant had OR 2.832 (95% CI 1.347–5.955; P=0.006) and IB had OR 1.771 (95% CI 1.286–2.439; P<0.001) for severe stenosis; high IB (≥5) corresponded to 50.0% severe stenosis vs 21.6% in low IB, adjusted aOR 3.212 (95% CI 1.861–5.542) (Mar 2025; URL: https://doi.org/10.1161/jaha.124.036830) (zeng2025rnf213variantand pages 5-8).

#### 2.2.3 Protective factors
No explicit protective genetic variants or modifiable protective exposures were identified in the retrieved evidence excerpts; therefore, this section remains incompletely populated from available sources.

### 2.3 Gene–environment interactions
The 2025 prospective cohort provides direct evidence of gene–environment contributions to stenosis severity (RNF213 variant and infectious burden), and further shows interaction with modifiable metabolic factors: stronger IB effects in subgroups with higher BMI, triglycerides, and homocysteine (interaction P values reported <0.05 in the cohort report) (zeng2025rnf213variantand pages 1-2, zeng2025rnf213variantand pages 5-8).

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes and patterns
Common clinical manifestations across the lifespan include transient ischemic attacks (TIAs), ischemic stroke, intracranial hemorrhage (more prominent in adults), seizures, headache, and cognitive impairment/cognitive decline (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 2-3, chakrabarti2025moyamoyadiseasephysiological pages 3-4).

Epidemiologic phenotype patterns reported in the 2024 management review include:
- Pediatric series: 67.8% presenting with stroke and 2.8% hemorrhage (kappel2024managementofmoyamoya pages 1-2).
- Adult Japanese cohort: 21% intracerebral hemorrhage (kappel2024managementofmoyamoya pages 1-2).

### 3.2 Age of onset and progression
MMD shows a **bimodal age distribution**, with pediatric diagnoses typically in ages ~5–9 years and adult presentation commonly in the 5th–6th decades (kappel2024managementofmoyamoya pages 2-3).

### 3.3 Quality of life impact
Recent reviews emphasize neurocognitive sequelae and cognitive deficits as important contributors to morbidity and quality-of-life impact, motivating ongoing registry studies centered on cognition and imaging biomarkers (NCT05619068 chunk 1, kappel2024managementofmoyamoya pages 1-2).

### 3.4 Suggested HPO terms
A structured phenotype-to-HPO mapping based on the retrieved evidence is provided below.

| Clinical phenotype | Suggested HPO term(s) | Typical age group (pediatric/adult) | Notes on frequency/severity if available from evidence |
|---|---|---|---|
| Ischemic stroke / cerebral infarction | HP:0001297 Cerebral infarction; Ischemic stroke | Both; especially pediatric | Most common presentation overall; pediatric series cited in review reported 67.8% presenting with stroke, while children more often present with ischemia than hemorrhage (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 2-3) |
| Transient ischemic attack | HP:0002326 Transient ischemic attack | Both; common in pediatric and early disease | Frequently reported presenting manifestation; pediatric patients often present with stroke/TIA; RNF213-associated disease linked to earlier onset and TIAs in some summaries (kappel2024managementofmoyamoya pages 2-3, bagyinszky2025multisystemicimpactof pages 4-6) |
| Intracranial hemorrhage / hemorrhagic stroke | HP:0002170 Intracranial hemorrhage; Hemorrhagic stroke | More common in adults | Adult patients are nearly twice as likely as pediatric patients to present with intracranial hemorrhage; one adult Japanese cohort cited 21% intracerebral hemorrhage, versus only 2.8% hemorrhage in a pediatric series (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 2-3) |
| Seizures | HP:0001250 Seizure | Both; often pediatric but can occur in either | Recognized clinical manifestation; listed among common presentations in recent reviews, though no robust frequency estimate was provided in retrieved evidence (chakrabarti2025moyamoyadiseasephysiological pages 3-4, calandrelli2026moyamoyavasculopathyand pages 5-6) |
| Headache | HP:0002315 Headache | Both | Reported as a common presenting symptom in recent reviews; frequency not quantified in retrieved evidence (chakrabarti2025moyamoyadiseasephysiological pages 3-4) |
| Cognitive impairment / cognitive decline | HP:0100543 Cognitive impairment; Neurocognitive dysfunction | Both; may be more evident in chronic disease and adults | Reviews note cognitive deficits and neurocognitive sequelae affecting quality of life; homozygous RNF213 carriers may have greater cognitive impairment (chakrabarti2025moyamoyadiseasephysiological pages 3-4, bagyinszky2025multisystemicimpactof pages 4-6) |
| Developmental delay / neurodevelopmental impact | HP:0001263 Global developmental delay; Developmental delay | Pediatric | Pediatric chronic cerebral hypoperfusion can manifest with developmental delay; highlighted in review-level evidence rather than quantified cohort data (chakrabarti2025moyamoyadiseasephysiological pages 3-4) |
| Hemiparesis / focal neurologic deficit | HP:0001269 Hemiparesis; Focal neurologic deficit | Both | Common downstream manifestation of ischemic or hemorrhagic events; not separately quantified in retrieved evidence but clinically central to stroke presentation (kappel2024managementofmoyamoya pages 1-2, chakrabarti2025moyamoyadiseasephysiological pages 3-4) |
| Posterior cerebral artery involvement | HP term label: Posterior cerebral artery stenosis/occlusion | Both; associated with more severe disease | Important vascular phenotype and risk marker; associated with perioperative cerebral infarction risk (OR 2.62) and with RNF213-related severity in several reports (uchiyama2024adultmoyamoyadisease pages 3-4, bagyinszky2025multisystemicimpactof pages 4-6) |
| Progressive intracranial arterial stenosis / occlusion | HP term label: Intracranial arterial stenosis; Cerebral artery occlusion | Both | Core vascular phenotype of disease; terminal ICA-centered stenosis/occlusion with moyamoya collaterals is required for diagnosis. Severe stenosis is associated with RNF213 variant carriage and higher infectious burden (RNF213 OR 2.832; IB OR 1.771 for severe WNS) (uchiyama2024adultmoyamoyadisease pages 3-4, zeng2025rnf213variantand pages 5-8, zeng2025rnf213variantand pages 1-2) |
| Abnormal collateral vessel formation ("puff-of-smoke") | HP term label: Abnormal cerebral collateral circulation | Both | Hallmark angiographic phenotype; characteristic collateral network defines the disease radiographically, but this is an imaging phenotype rather than a patient-reported symptom (kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 2-3, uchiyama2024adultmoyamoyadisease pages 3-4) |
| Asymptomatic moyamoya arteriopathy | HP term label: Asymptomatic cerebrovascular disease | Both; increasingly detected in adults | Increasingly recognized through imaging; historical reports in review cite asymptomatic cases rising from 1.5% to 17.8%, with AMORE showing 1.0% annual stroke risk per hemisphere over 5 years (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 5-6) |


*Table: This table maps major clinical and vascular phenotypes of moyamoya disease to suggested HPO terms and summarizes age-pattern and severity/frequency notes drawn from the retrieved evidence. It is useful for structured phenotype annotation in a disease knowledge base.*

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and susceptibility genes
**RNF213** is the major susceptibility gene in East Asian MMD and is also discussed as a broader vasculopathy gene with diverse phenotypes (uchiyama2024adultmoyamoyadisease pages 2-3, tan2024exploringrnf213in pages 2-4).

Additional MMD-related genes are highlighted in 2024–2025 review literature (often as syndromic or secondary moyamoya causes/associations): **GUCY1A3**, **BRCC3**, and genes implicated in vascular smooth muscle and arterial disease spectra such as **ACTA2**, **DIAPH1**, and immune loci such as **HLA** (kappel2024managementofmoyamoya pages 1-2, he2025advancesinmoyamoya pages 8-10, he2025advancesinmoyamoya pages 13-14).

| Gene (HGNC symbol) | Variant/example | Evidence type (human genetic association/functional model) | Key finding | Key quantitative statistic | Source (PMID/DOI/URL if in evidence) |
|---|---|---|---|---|---|
| RNF213 | p.R4810K / c.14576G>A (also described as p.R4859K in one review) | Human genetic association | Major East Asian founder susceptibility variant for moyamoya disease; strongly enriched in familial and sporadic cases; associated with earlier onset and more severe disease | Japanese/Korean/Chinese MMD patient frequencies 90.1% / 78.9% / 23.1% vs general population 2.5% / 2.7% / 0.9%; OR ~144 for definite MMD and ~54 for unilateral MMD in cited cohorts (uchiyama2024adultmoyamoyadisease pages 2-3). Another review: Japan OR 184.04, Korea 109.77, China 31.53; stroke OR 1.91 (95% CI 1.55–2.36) (tan2024exploringrnf213in pages 2-4) | Uchiyama & Fujimura 2024, DOI: 10.1159/000540254, https://doi.org/10.1159/000540254 (uchiyama2024adultmoyamoyadisease pages 2-3); Tan et al. 2024, DOI: 10.3390/biomedicines13010017, https://doi.org/10.3390/biomedicines13010017 (tan2024exploringrnf213in pages 2-4) |
| RNF213 | p.R4810K / c.14576G>A | Human genetic association; penetrance analysis | Strong effect but incomplete penetrance; zygosity influences severity and age at onset | General East Asian population frequency around 1–2%; only ~1/150–1/300 heterozygous carriers develop MMD, while homozygous disease incidence exceeds 78%; homozygotes median onset 3 years vs 7 years in heterozygotes (tan2024exploringrnf213in pages 4-6, tan2024exploringrnf213in pages 2-4) | Tan et al. 2024, DOI: 10.3390/biomedicines13010017, https://doi.org/10.3390/biomedicines13010017 (tan2024exploringrnf213in pages 2-4, tan2024exploringrnf213in pages 4-6) |
| RNF213 | Loss-of-function; pathogenic mutations including CNV deletion and disease-associated missense variants | Functional model + human pathology | RNF213 loss promotes pathological angiogenesis and vascular remodeling; implicated in Hippo/YAP/TAZ→VEGFR2 dysregulation and intimal hyperplasia | In HBMECs, RNF213 knockdown increased endothelial proliferation/migration/tube formation; YAP/TAZ activation with p-TAZ/TAZ ~0.61 and p-YAP/YAP ~0.43; surface VEGFR2 ~1.28-fold and intracellular VEGFR2 ~0.59-fold vs control; severe WNS OR 2.832 for RNF213 variant in a prospective cohort (ye2023rnf213lossoffunctionpromotes pages 11-13, ye2023rnf213lossoffunctionpromotes pages 10-11, zeng2025rnf213variantand pages 5-8) | Ye et al. 2023, DOI: 10.1093/brain/awad225, https://doi.org/10.1093/brain/awad225 (ye2023rnf213lossoffunctionpromotes pages 11-13, ye2023rnf213lossoffunctionpromotes pages 10-11, ye2023rnf213lossoffunctionpromotes pages 1-2, ye2023rnf213lossoffunctionpromotes pages 2-3); Zeng et al. 2025, DOI: 10.1161/JAHA.124.036830, https://doi.org/10.1161/jaha.124.036830 (zeng2025rnf213variantand pages 5-8) |
| RNF213 | Rare C-terminal / non-p.R4810K variants | Human genetic association | Allelic heterogeneity outside East Asia; rare C-terminal RNF213 variants reported in Caucasian moyamoya cases | Variant rare/absent in White/Caucasian cohorts in one review (maximum allele frequency reported 0.0006; absent in one WES series of 125 Caucasian patients) (he2025advancesinmoyamoya pages 8-10) | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 8-10, bagyinszky2025multisystemicimpactof pages 17-18) |
| GUCY1A3 | Loss-of-function mutations; compound heterozygous familial variants | Human genetic association | Supports nitric oxide/soluble guanylate cyclase pathway involvement; implicated in familial/syndromic moyamoya | Two compound heterozygotes among 96 sequenced cases in one report; larger case-control study (255 patients vs 300 controls) showed no association in another dataset (he2025advancesinmoyamoya pages 13-14) | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 13-14) |
| BRCC3 | Deletions / loss-of-function | Human genetic association | Causes X-linked syndromic moyamoya in case reports/families; supports abnormal angiogenesis pathway | Population studies referenced in a review showed no difference outside syndromic cases; quantitative association not established in broader cohorts in retrieved evidence (he2025advancesinmoyamoya pages 13-14) | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 13-14) |
| ACTA2 | Pathogenic mutations (specific variant not provided in retrieved evidence) | Review-level human genetic association | Implicated as a moyamoya-related gene beyond RNF213; especially relevant to syndromic/monogenic vasculopathy spectrum | No variant-specific quantitative statistic provided in retrieved evidence | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 8-10); Kappel et al. 2024, DOI: 10.3171/2024.1.JNS221977, https://doi.org/10.3171/2024.1.jns221977 (kappel2024managementofmoyamoya pages 1-2) |
| DIAPH1 | Pathogenic mutations (specific variant not provided in retrieved evidence) | Review-level human genetic association | Listed among MMD-related genes beyond RNF213 in recent review literature | No variant-specific quantitative statistic provided in retrieved evidence | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 8-10) |
| HLA | HLA susceptibility loci/alleles (not specified in retrieved evidence) | Review-level human genetic association | HLA-region genetic susceptibility has been reported in MMD, supporting immune/inflammatory contribution | No variant-specific quantitative statistic provided in retrieved evidence | He et al. 2025, DOI: 10.1002/mco2.70054, https://doi.org/10.1002/mco2.70054 (he2025advancesinmoyamoya pages 8-10) |


*Table: This table summarizes the principal genes and representative variants implicated in moyamoya disease from the retrieved evidence, emphasizing RNF213 p.R4810K and other genes named in recent reviews. It is useful for quickly distinguishing strong human genetic associations from lower-detail review-level gene mentions and mechanistic model evidence.*

### 4.2 Pathogenic variants (example variants and mechanistic consequences)
#### RNF213 loss-of-function mechanisms (primary 2023 functional study)
A key 2023 Brain paper provides multi-system mechanistic evidence that RNF213 loss-of-function promotes pathological angiogenesis via Hippo pathway dysregulation:

Direct abstract quote (Jul 2023, Brain): “RNF213 deletion exacerbated pathological angiogenesis… Reduced RNF213 expression led to increased endothelial cell proliferation, migration and tube formation… Endothelial knockdown of RNF213 activated the Hippo pathway effector Yes-associated protein (YAP)/tafazzin (TAZ) and promoted the overexpression of the downstream effector VEGFR2… inhibition of YAP/TAZ… reversed RNF213 knockdown-induced angiogenesis.” (URL: https://doi.org/10.1093/brain/awad225) (ye2023rnf213lossoffunctionpromotes pages 1-2).

Quantitative molecular readouts reported include altered Hippo phosphorylation ratios and VEGFR2 trafficking: p-TAZ/TAZ ~0.61 and p-YAP/YAP ~0.43 (lower than control), with increased surface VEGFR2 (~1.28-fold) and reduced intracellular VEGFR2 (~0.59-fold) in RNF213 knockdown endothelial cells (ye2023rnf213lossoffunctionpromotes pages 11-13).

#### RNF213 variant penetrance and severity
RNF213 p.R4810K shows incomplete penetrance in heterozygotes with very high incidence in homozygotes, consistent with a “susceptibility + second hit” model rather than a fully penetrant Mendelian cause in most populations (tan2024exploringrnf213in pages 4-6).

### 4.3 Modifier genes
The retrieved excerpts do not provide a validated list of modifier genes with quantified effect on severity; however, multiple reviews frame MMD as polygenic/multifactorial with additional genes (ACTA2/DIAPH1/HLA and others) that may influence phenotype heterogeneity (he2025advancesinmoyamoya pages 8-10).

### 4.4 Epigenetic information (2024 focus)
A 2024 Molecular Therapy – Nucleic Acids review summarizes multiple epigenetic layers implicated in MMD:
- **DNA methylation**: promoter hypomethylation of **SORT1** in endothelial colony-forming cells (ECFCs) from MMD patients, with increased SORT1 expression and downstream pro-angiogenic factor changes (VEGF/VEGFR-1/bFGF/MMP9 up; Ang-1 and thrombospondin 2 down) (xu2024insightsintothe pages 3-4).
- **Histone modifications**: reduced acetyl-histone H3K27 binding at **RALDH2** promoter with reduced RALDH2 expression (retinoic acid synthesis) in ECFCs; HDAC inhibitor **panobinostat** reportedly restored impaired angiogenic potential in that context (xu2024insightsintothe pages 3-4).
- **Noncoding RNAs**: multiple circulating or CSF miRNA/circRNA signatures are discussed as candidate biomarkers and mechanistic drivers; examples include serum let-7c, CSF exosome miRNA panels, and multiple differentially expressed circRNAs (xu2024insightsintothe pages 16-17, xu2024insightsintothe pages 13-14).

---

## 5. Environmental Information

### 5.1 Environmental factors
The retrieved 2024 management review identifies **CNS infections** and **radiation exposure** (particularly for moyamoya syndrome) as notable non-genetic contributors, alongside circulating cytokines/growth factors and autoantibodies as signals of inflammatory contribution (kappel2024managementofmoyamoya pages 1-2).

### 5.2 Lifestyle/metabolic factors
The prospective gene–environment cohort indicates that infectious-burden associations with stenosis severity were amplified among patients with higher BMI, triglycerides, and homocysteine—suggesting potentially modifiable metabolic contexts may influence progression (zeng2025rnf213variantand pages 1-2).

### 5.3 Infectious agents
The infectious-burden score in the prospective cohort was built from antibody titers to HSV-1/2, CMV, Toxoplasma, rubella, and EBV, and was associated with more severe stenosis in MMD (zeng2025rnf213variantand pages 2-4, zeng2025rnf213variantand pages 5-8).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (integrated current understanding)
A synthesis supported by the retrieved evidence is:
1) **Genetic susceptibility** (especially RNF213 p.R4810K in East Asia) establishes a predisposition with incomplete penetrance (uchiyama2024adultmoyamoyadisease pages 2-3, tan2024exploringrnf213in pages 4-6).
2) **Second-hit exposures** (e.g., inflammatory/infectious burden; radiation in syndromic cases) and metabolic context can contribute to progression/severity (zeng2025rnf213variantand pages 5-8, kappel2024managementofmoyamoya pages 2-3).
3) At the vessel wall level, disease is characterized by steno-occlusive remodeling and collateral network formation; RNF213 perturbation can drive **endothelial dysfunction and aberrant angiogenesis** (kappel2024managementofmoyamoya pages 1-2, ye2023rnf213lossoffunctionpromotes pages 1-2).
4) A demonstrated molecular axis in endothelial models is **Hippo pathway “off” signaling → YAP/TAZ activation → VEGFR2 dysregulation/trafficking changes → hyperangiogenic phenotype**, observed in human brain microvascular endothelial cells and corroborated in mouse and zebrafish models (ye2023rnf213lossoffunctionpromotes pages 10-11, ye2023rnf213lossoffunctionpromotes pages 11-13, ye2023rnf213lossoffunctionpromotes pages 1-2).

### 6.2 Molecular pathways (examples supported by retrieved evidence)
- **Hippo pathway / YAP–TAZ–TEAD** and **VEGF/VEGFR2** signaling dysregulation in RNF213 loss-of-function endothelial models (ye2023rnf213lossoffunctionpromotes pages 10-11, ye2023rnf213lossoffunctionpromotes pages 1-2).
- **Inflammatory signaling** and barrier integrity: management review summarizes associations with cytokines/growth factors, autoantibodies, and blood–brain barrier junctional protein alterations as part of the mechanistic landscape (kappel2024managementofmoyamoya pages 2-3).

### 6.3 Immune system involvement
Immune/inflammatory contributions are supported by (i) review-level discussions of cytokines/autoantibodies/infections and (ii) the prospective infectious-burden severity association (kappel2024managementofmoyamoya pages 1-2, zeng2025rnf213variantand pages 5-8).

### 6.4 Suggested ontology terms
**GO biological process (suggestions)**: angiogenesis; regulation of endothelial cell proliferation; regulation of endothelial cell migration; VEGF receptor signaling pathway; Hippo signaling; regulation of vascular remodeling; inflammatory response; blood–brain barrier maintenance (ye2023rnf213lossoffunctionpromotes pages 1-2, kappel2024managementofmoyamoya pages 2-3).

**CL cell types (suggestions)**: brain microvascular endothelial cell; vascular smooth muscle cell; endothelial colony-forming cell (ECFC) (ye2023rnf213lossoffunctionpromotes pages 1-2, xu2024insightsintothe pages 3-4).

---

## 7. Anatomical Structures Affected

### 7.1 Organ and vascular territories
Primary involvement is intracranial arterial circulation centered on the terminal intracranial internal carotid artery and proximal MCA/ACA involvement; collateral networks form near the lesions (uchiyama2024adultmoyamoyadisease pages 3-4).

### 7.2 Lateralization
Updated diagnostic criteria allow **unilateral** disease; unilateral cases can progress to bilateral disease (uchiyama2024adultmoyamoyadisease pages 1-2, uchiyama2024adultmoyamoyadisease pages 3-4).

### 7.3 Suggested UBERON terms (suggestions)
Intracranial internal carotid artery; middle cerebral artery; anterior cerebral artery; circle of Willis; basal ganglia; periventricular white matter.

---

## 8. Temporal Development

### 8.1 Onset
Bimodal onset/diagnosis: pediatric (~5–9 years) and adult (5th–6th decades) (kappel2024managementofmoyamoya pages 2-3).

### 8.2 Progression
MMD is described as progressive steno-occlusive arteriopathy. In asymptomatic cases, a disease registry analysis cited in the management review reports an annual stroke risk of 1.0% per moyamoya hemisphere over the first 5 years, with a predominance of hemorrhagic strokes among events (85.7%) (kappel2024managementofmoyamoya pages 2-3, kappel2024managementofmoyamoya pages 5-6).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (statistics)
The 2024 management review provides region-specific incidence and prevalence trends:
- Japan incidence reported 0.35/100,000 (1994) to 0.54/100,000 (2003) (kappel2024managementofmoyamoya pages 2-3).
- Korea incidence increased 1.7→2.3/100,000 (2007–2011) and prevalence increased 8.2→16.1/100,000 by 2011 (kappel2024managementofmoyamoya pages 2-3).
- Taiwan incidence increased 0.14→0.20/100,000 person-years (2000–2011) (kappel2024managementofmoyamoya pages 2-3).
- Denmark incidence ~0.07/100,000 person-years (2008–2017) and U.S. ~0.086/100,000 person-years (kappel2024managementofmoyamoya pages 2-3).

Sex ratio: approximately 1.8–2.2 female-to-male ratio is reported (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 2-3).

Familial aggregation: family history reported in ~10–15% (kappel2024managementofmoyamoya pages 2-3).

### 9.2 Inheritance and penetrance
RNF213 p.R4810K is best described (in these sources) as a strong susceptibility allele with autosomal-dominant pattern and incomplete penetrance; penetrance is very low for heterozygotes but much higher for homozygotes (tan2024exploringrnf213in pages 4-6, tan2024exploringrnf213in pages 2-4).

---

## 10. Diagnostics

### 10.1 Clinical criteria and imaging
The 2021 Revised Diagnostic Criteria for MMD (Japanese RCMD guidance, summarized in 2024 review literature) include:
- Diagnosis can be made in **unilateral or bilateral** cases.
- Required radiologic features include stenosis/occlusion centered on the terminal intracranial ICA and the presence of moyamoya vessels (abnormal vascular networks) near the occlusive lesions.
- Heavy T2-weighted MRI demonstration of decreased outer diameter of terminal ICA/horizontal MCA is emphasized to distinguish MMD from atherosclerosis; 3D-CISS MRI is highlighted as useful for this differentiation (uchiyama2024adultmoyamoyadisease pages 3-4, uchiyama2024adultmoyamoyadisease pages 1-2).

A visual table from the 2024 review shows the **Suzuki angiographic staging system (I–VI)** and indicates where the diagnostic criteria table is located in the paper (uchiyama2024adultmoyamoyadisease media e5baf62b, uchiyama2024adultmoyamoyadisease media aace831c).

### 10.2 Scoring systems
Quantitative MRA scoring (Houkin MRA score) correlating with Suzuki staging is used to grade arterial involvement (uchiyama2024adultmoyamoyadisease pages 2-3, uchiyama2024adultmoyamoyadisease pages 3-4).

### 10.3 Differential diagnosis
MMD must be distinguished from mimics such as intracranial atherosclerosis; imaging emphasis on outer arterial diameter reduction on heavy T2/3D-CISS supports this differentiation (uchiyama2024adultmoyamoyadisease pages 3-4).

---

## 11. Outcome / Prognosis

### 11.1 Natural history and stroke risk
Asymptomatic MMD is increasingly detected on imaging; a registry analysis cited in the 2024 management review reported **1.0% annual stroke risk per hemisphere** over 5 years, with 85.7% hemorrhagic among observed strokes (kappel2024managementofmoyamoya pages 1-2, kappel2024managementofmoyamoya pages 5-6).

### 11.2 Post-surgical functional outcomes (pediatric meta-analysis)
In pediatric revascularization meta-analysis (37 studies; 2,460 patients; 4,432 hemispheres), functional outcomes at last follow-up (mRS 0–1) were pooled at ~80.38% for indirect bypass and ~87.44% for direct/combined bypass; mortality was very low (pooled indirect bypass mortality 0.30%) (Feb 2023; URL: https://doi.org/10.1007/s00381-023-05868-6) (lee2023surgicalrevascularizationsfor pages 12-13).

---

## 12. Treatment

### 12.1 Current standard of care and real-world implementation
**Surgical revascularization** is the mainstay for symptomatic MMD, including direct, indirect, and combined extracranial-intracranial bypass techniques; indirect approaches rely on angiogenic potential and are described as more effective in children, while direct/combined bypasses are described as more effective in adults (kappel2024managementofmoyamoya pages 5-6).

**Adjunctive antiplatelet therapy** (e.g., aspirin in pediatric practice in the U.S.) is used for ischemic symptom prevention, though the retrieved evidence excerpts did not provide pooled randomized effect estimates (kappel2024managementofmoyamoya pages 5-6).

### 12.2 Comparative effectiveness and safety (pediatric)
Pediatric meta-analysis found no significant differences between direct/combined versus indirect bypass for stroke recurrence, morbidity, or mortality, but direct/combined had better angiographic revascularization (Matsushima Grade A/B RR 1.12, 95% CI 1.02–1.24) and higher wound complication risk (RR 2.54, 95% CI 1.82–3.55) (lee2023surgicalrevascularizationsfor pages 1-2).

### 12.3 Postoperative monitoring and complications
A 2025 systematic review/meta-analysis supports noninvasive **ultrasonography** for postoperative bypass assessment with predictive changes in STA/ECA flow parameters (e.g., STA PSV MD 28.26 within 2 weeks for high bypass capacity) (santos2025managementofmoyamoyaa pages 1-3).

### 12.4 MAXO suggestions
A structured treatment-to-MAXO mapping (labels suggested) is provided below.

| Treatment/strategy | MAXO term suggestion (label) | Indication (e.g., symptomatic ischemic, hemorrhagic, pediatric) | Evidence summary | Key quantitative outcome if available | Sources |
|---|---|---|---|---|---|
| Direct extracranial-intracranial bypass (e.g., STA-MCA bypass) | surgical revascularization procedure; extracranial-intracranial arterial bypass | Symptomatic adult MMD, especially ischemic; also used in hemorrhagic disease | Review evidence indicates surgical revascularization is the mainstay for symptomatic disease; direct and combined bypass appear more effective than indirect bypass in adults for prevention of recurrent stroke/hemorrhage. Endovascular stenting has generally not prevented progression, reinforcing surgery as standard definitive therapy. | Adult comparative metrics not quantified in retrieved full evidence excerpts; qualitative consensus favors direct/combined over indirect in adults. | (kappel2024managementofmoyamoya pages 5-6, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Indirect bypass (e.g., EDAS/EMS/encephaloduroarteriosynangiosis-based approaches) | indirect cerebral revascularization procedure | Pediatric MMD/MMS; symptomatic ischemic disease; patients with small recipient vessels | Indirect procedures rely on angiogenic potential and are described as particularly effective in children. Pediatric meta-analysis found indirect bypass to be overall safe and effective, though angiographic collateralization was somewhat better with direct/combined strategies. | In pediatric meta-analysis, no significant difference vs direct/combined for stroke recurrence, morbidity, or mortality; wound complications were lower than direct/combined. | (kappel2024managementofmoyamoya pages 5-6, lee2023surgicalrevascularizationsfor pages 1-2, lee2023surgicalrevascularizationsfor pages 12-13) |
| Combined direct + indirect bypass | combined surgical revascularization procedure | Adult symptomatic MMD; selected pediatric cases; situations seeking immediate + delayed collateral supply | Reviews report combined/direct bypasses perform better in adults than indirect alone. Pediatric meta-analysis suggests improved long-term angiographic revascularization versus indirect bypass, but without clear long-term stroke or mortality advantage. | Matsushima Grade A/B angiographic revascularization favored direct/combined over indirect: RR 1.12 (95% CI 1.02-1.24); wound complications higher with direct/combined: RR 2.54 (95% CI 1.82-3.55). | (kappel2024managementofmoyamoya pages 5-6, lee2023surgicalrevascularizationsfor pages 1-2, lee2023surgicalrevascularizationsfor pages 12-13) |
| Antiplatelet therapy (aspirin; clopidogrel; short dual antiplatelet therapy in some adults) | antiplatelet therapy | Adjunctive therapy for ischemic presentations; peri-diagnostic/medical management; pediatric aspirin commonly used in U.S. practice | Antiplatelet therapy is used as adjunctive medical management, especially for ischemic symptoms. Review notes aspirin is commonly used in children and some adult studies suggest fewer ischemic events with aspirin, clopidogrel, or short dual therapy, but this is adjunctive rather than disease-modifying. | No pooled effect size provided in retrieved evidence excerpts. | (kappel2024managementofmoyamoya pages 5-6, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Conservative management with serial imaging surveillance | clinical surveillance; watchful waiting | Asymptomatic MMD; some stable MMS/MMV cases; patients without clear hemodynamic compromise | Asymptomatic disease is generally managed conservatively with watchful waiting and serial imaging. For moyamoya syndrome/vasculopathy, conservative management plus treatment of the underlying disorder is emphasized unless progressive symptoms or chronic hemodynamic insufficiency develop. | AMORE study cited in review: annual stroke risk 1.0% per moyamoya hemisphere over 5 years; 85.7% of strokes were hemorrhagic. | (kappel2024managementofmoyamoya pages 5-6, kappel2024managementofmoyamoya pages 2-3, calandrelli2026moyamoyavasculopathyand pages 5-6, kappel2024managementofmoyamoya pages 1-2) |
| Secondary prevention directed at underlying syndrome/comorbidity | secondary prevention strategy; treatment of underlying disease | Moyamoya syndrome / quasi-moyamoya associated with radiation, autoimmune disease, sickle cell disease, NF1, etc. | MMS is defined by moyamoya-pattern arteriopathy with comorbid conditions. Management is pattern-specific and often conservative, emphasizing treatment of the associated condition and surveillance; revascularization is considered for progressive neurologic symptoms/hemodynamic insufficiency. | No quantitative comparative outcome in retrieved excerpts. | (uchiyama2024adultmoyamoyadisease pages 2-3, calandrelli2026moyamoyavasculopathyand pages 5-6, kappel2024managementofmoyamoya pages 1-2, uchiyama2024adultmoyamoyadisease pages 1-2) |
| Postoperative ultrasonographic bypass assessment | postoperative imaging assessment; ultrasonography monitoring | After revascularization surgery to assess bypass function/capacity | Ultrasound is a noninvasive postoperative monitoring tool for bypass capacity when compared with confirmatory imaging. It is useful for identifying high bypass capacity after surgery. | Meta-analysis of 8 cohort studies/301 hemispheres: early high-capacity bypass associated with increased STA PSV (MD 28.26, p<0.0001), MFV (MD 22.97, p=0.03), EDV (MD 33.45, p<0.0001), and lower RI (MD -0.09, p=0.006). | (santos2025managementofmoyamoyaa pages 1-3) |
| Risk-stratified perioperative management | perioperative management | Surgical candidates with prior infarction, PCA involvement, advanced MRA severity | Meta-analysis identified factors associated with perioperative cerebral infarction, supporting enhanced perioperative monitoring and risk stratification rather than a distinct therapy. | Posterior cerebral artery involvement OR 2.62 (95% CI 1.36-5.06); higher preoperative MRA grade OR 2.81 (95% CI 1.27-6.22); previous infarction OR 2.52 (95% CI 1.69-3.75). | (santos2025managementofmoyamoyaa pages 1-3) |
| Growth-factor/angiogenesis adjuncts (VEGF, HGF, PDGF; investigational) | pro-angiogenic therapy | Experimental adjunct to improve collateral formation after bypass | Current reviews describe no approved disease-modifying therapy; proposed future approaches include growth-factor augmentation to improve neovascularization and bypass vessel ingrowth. | No clinical efficacy data in retrieved evidence excerpts. | (kappel2024managementofmoyamoya pages 5-6) |
| Gene-targeted therapy / CRISPR-style approaches (investigational) | gene therapy | Future personalized therapy for familial/genetically susceptible MMD | Reviews highlight RNF213 and other susceptibility genes as rationale for future genome-informed therapies, but these remain conceptual/experimental and not established clinical care. | No human outcome data in retrieved evidence excerpts. | (kappel2024managementofmoyamoya pages 5-6, ye2023rnf213lossoffunctionpromotes pages 11-13, ye2023rnf213lossoffunctionpromotes pages 1-2) |


*Table: This table summarizes current and emerging management strategies for moyamoya disease, aligned to suggested MAXO-style action labels. It is useful for mapping evidence-based interventions, indications, and quantitative outcomes into a structured disease knowledge base.*

### 12.5 Experimental and clinical-trial landscape (real-world ongoing research)
Recent/ongoing ClinicalTrials.gov records in the retrieved evidence include:
- **NCT04205578** (Phase 3 RCT): dl-3-n-butylphthalide (NBP) perioperative adjunct after EC–IC bypass; planned enrollment 450; primary endpoints include perioperative ischemic stroke and death within 30 days (registered 2020) (NCT04205578 chunk 1).
- **NCT04917003** (randomized controlled interventional; phase NA): remote ischemic conditioning (RIC) + EDAS vs EDAS in ischemic MMD; enrollment 60; primary outcome change in relative CBF in operative MCA territory at 3 months (registered 2021) (NCT04917003 chunk 1).
- **NCT02319980** (Phase 3 randomized): combined revascularization (STA–MCA + EDMS) vs conservative management in adult hemorrhagic MMD; enrollment 360; primary includes strokes/death within 30 days and ipsilateral recurrent bleeding up to 5 years (registered 2015) (NCT02319980 chunk 1).
- **NCT02982135** (non-randomized interventional): direct vs indirect bypass in adult hemorrhagic MMD; enrollment 300; primary outcome rebleeding events over 5–10 years (registered 2016) (NCT02982135 chunk 1).
- **NCT05619068** (prospective observational registry): evolution/prognosis with imaging biomarkers and cognitive decline; enrollment 300; compares conservative vs revascularization pathways (registered 2022) (NCT05619068 chunk 1).

---

## 13. Prevention

### 13.1 Primary prevention
No validated primary prevention strategy is established in the retrieved evidence excerpts; genetic susceptibility has incomplete penetrance and likely requires additional triggers (tan2024exploringrnf213in pages 4-6).

### 13.2 Secondary and tertiary prevention
Secondary prevention focuses on stroke prevention and surveillance, including conservative management with serial imaging for asymptomatic cases and surgical revascularization for symptomatic or hemodynamically compromised disease, with adjunctive antiplatelet therapy commonly used for ischemic presentations (kappel2024managementofmoyamoya pages 5-6).

---

## 14. Other Species / Natural Disease
No naturally occurring disease in non-human species was identified in the retrieved evidence excerpts.

---

## 15. Model Organisms

### 15.1 Model types and what they show
A high-impact 2023 study used **RNF213-deficient mice and zebrafish** to demonstrate increased/pathological angiogenesis, and used **human brain microvascular endothelial cell (HBMEC) knockdown** to demonstrate increased proliferation/migration/tube formation linked to Hippo/YAP/TAZ→VEGFR2 signaling (ye2023rnf213lossoffunctionpromotes pages 1-2, ye2023rnf213lossoffunctionpromotes pages 11-13).

These models support a mechanistic link from genetic perturbation (RNF213 loss-of-function) to endothelial behavior changes and abnormal vascular network development consistent with moyamoya-like collateral formation, while recognizing that reproducing the full steno-occlusive large-artery phenotype in models remains challenging (ye2023rnf213lossoffunctionpromotes pages 1-2).

---

# Visual evidence note
Tables summarizing the Suzuki angiographic staging system and the 2021 RCMD diagnostic/imaging criteria are present as extracted images from the 2024 review (uchiyama2024adultmoyamoyadisease media e5baf62b, uchiyama2024adultmoyamoyadisease media aace831c).

# Evidence and coverage limitations
- Formal ontology codes (MONDO, ORPHA, ICD-10/11, MeSH unique ID) were not present in the accessible retrieved excerpts, so they cannot be asserted from this evidence alone (artifact-00).
- Several requested areas (protective factors; specific validated prognostic biomarkers; robust adult comparative surgical outcome statistics) were only partially supported by the retrieved evidence set.



References

1. (kappel2024managementofmoyamoya pages 1-2): Ari D Kappel, Abdullah H. Feroze, Erickson F. Torio, Madhav Sukumaran, and Rose Du. Management of moyamoya disease: a review of current and future therapeutic strategies. Journal of Neurosurgery, 141:975-982, Oct 2024. URL: https://doi.org/10.3171/2024.1.jns221977, doi:10.3171/2024.1.jns221977. This article has 27 citations and is from a domain leading peer-reviewed journal.

2. (kappel2024managementofmoyamoya pages 2-3): Ari D Kappel, Abdullah H. Feroze, Erickson F. Torio, Madhav Sukumaran, and Rose Du. Management of moyamoya disease: a review of current and future therapeutic strategies. Journal of Neurosurgery, 141:975-982, Oct 2024. URL: https://doi.org/10.3171/2024.1.jns221977, doi:10.3171/2024.1.jns221977. This article has 27 citations and is from a domain leading peer-reviewed journal.

3. (uchiyama2024adultmoyamoyadisease pages 2-3): S. Uchiyama and Miki Fujimura. Adult moyamoya disease and moyamoya syndrome: what is new? Cerebrovascular Diseases Extra, 14:86-94, Jul 2024. URL: https://doi.org/10.1159/000540254, doi:10.1159/000540254. This article has 15 citations and is from a peer-reviewed journal.

4. (uchiyama2024adultmoyamoyadisease pages 3-4): S. Uchiyama and Miki Fujimura. Adult moyamoya disease and moyamoya syndrome: what is new? Cerebrovascular Diseases Extra, 14:86-94, Jul 2024. URL: https://doi.org/10.1159/000540254, doi:10.1159/000540254. This article has 15 citations and is from a peer-reviewed journal.

5. (santos2025managementofmoyamoyab pages 3-4): DE Santos, G Chmutin, and E Chmutin. Management of moyamoya disease: a systematic review and meta-analysis on surgical revascularization, outcomes and clinical manifestations. Unknown journal, 2025.

6. (calandrelli2026moyamoyavasculopathyand pages 1-2): Rosalinda Calandrelli, Carlo Augusto Mallio, Caterina Bernetti, Luca Massimi, and Fabio Pilato. Moyamoya vasculopathy and atypical moyamoya-like patterns: insights into diagnosis and therapeutic implications. NeuroSci, 7:27, Feb 2026. URL: https://doi.org/10.3390/neurosci7010027, doi:10.3390/neurosci7010027. This article has 0 citations.

7. (uchiyama2024adultmoyamoyadisease pages 1-2): S. Uchiyama and Miki Fujimura. Adult moyamoya disease and moyamoya syndrome: what is new? Cerebrovascular Diseases Extra, 14:86-94, Jul 2024. URL: https://doi.org/10.1159/000540254, doi:10.1159/000540254. This article has 15 citations and is from a peer-reviewed journal.

8. (uchiyama2024adultmoyamoyadisease media e5baf62b): S. Uchiyama and Miki Fujimura. Adult moyamoya disease and moyamoya syndrome: what is new? Cerebrovascular Diseases Extra, 14:86-94, Jul 2024. URL: https://doi.org/10.1159/000540254, doi:10.1159/000540254. This article has 15 citations and is from a peer-reviewed journal.

9. (santos2025managementofmoyamoyaa pages 3-4): DE Santos, G Chmutin, and E Chmutin. Management of moyamoya disease: a systematic review and meta-analysis on surgical revascularization, outcomes and clinical manifestations. Unknown journal, 2025.

10. (tan2024exploringrnf213in pages 4-6): Benjamin Y. Q. Tan, Charlene H. P. Kok, Megan B. J. Ng, Shaun Loong, Eric Jou, Leonard L. L. Yeo, Weiping Han, Christopher D. Anderson, Chiea Chuen Khor, and Poh San Lai. Exploring rnf213 in ischemic stroke and moyamoya disease: from cellular models to clinical insights. Biomedicines, 13:17, Dec 2024. URL: https://doi.org/10.3390/biomedicines13010017, doi:10.3390/biomedicines13010017. This article has 10 citations.

11. (he2025advancesinmoyamoya pages 8-10): Shihao He, Zhenyu Zhou, Michelle Y. Cheng, Xiaokuan Hao, Terrance Chiang, Yanru Wang, Junze Zhang, Xilong Wang, Xun Ye, Rong Wang, Gary K. Steinberg, and Yuanli Zhao. Advances in moyamoya disease: pathogenesis, diagnosis, and therapeutic interventions. MedComm, Jan 2025. URL: https://doi.org/10.1002/mco2.70054, doi:10.1002/mco2.70054. This article has 31 citations.

12. (he2025advancesinmoyamoya pages 13-14): Shihao He, Zhenyu Zhou, Michelle Y. Cheng, Xiaokuan Hao, Terrance Chiang, Yanru Wang, Junze Zhang, Xilong Wang, Xun Ye, Rong Wang, Gary K. Steinberg, and Yuanli Zhao. Advances in moyamoya disease: pathogenesis, diagnosis, and therapeutic interventions. MedComm, Jan 2025. URL: https://doi.org/10.1002/mco2.70054, doi:10.1002/mco2.70054. This article has 31 citations.

13. (tan2024exploringrnf213in pages 2-4): Benjamin Y. Q. Tan, Charlene H. P. Kok, Megan B. J. Ng, Shaun Loong, Eric Jou, Leonard L. L. Yeo, Weiping Han, Christopher D. Anderson, Chiea Chuen Khor, and Poh San Lai. Exploring rnf213 in ischemic stroke and moyamoya disease: from cellular models to clinical insights. Biomedicines, 13:17, Dec 2024. URL: https://doi.org/10.3390/biomedicines13010017, doi:10.3390/biomedicines13010017. This article has 10 citations.

14. (zeng2025rnf213variantand pages 5-8): Chaofan Zeng, Peicong Ge, Zihan Yin, Junlin Lu, Xiaofan Yu, Junsheng Li, Yuanren Zhai, Chenglong Liu, Qiheng He, Wei Liu, Jia Wang, Xingju Liu, Xun Ye, Qian Zhang, Rong Wang, Yan Zhang, Dong Zhang, and Jizong Zhao. <i>rnf213</i> variant and infectious burden associated with intracranial artery stenosis in moyamoya disease. Journal of the American Heart Association, Mar 2025. URL: https://doi.org/10.1161/jaha.124.036830, doi:10.1161/jaha.124.036830. This article has 2 citations.

15. (zeng2025rnf213variantand pages 1-2): Chaofan Zeng, Peicong Ge, Zihan Yin, Junlin Lu, Xiaofan Yu, Junsheng Li, Yuanren Zhai, Chenglong Liu, Qiheng He, Wei Liu, Jia Wang, Xingju Liu, Xun Ye, Qian Zhang, Rong Wang, Yan Zhang, Dong Zhang, and Jizong Zhao. <i>rnf213</i> variant and infectious burden associated with intracranial artery stenosis in moyamoya disease. Journal of the American Heart Association, Mar 2025. URL: https://doi.org/10.1161/jaha.124.036830, doi:10.1161/jaha.124.036830. This article has 2 citations.

16. (chakrabarti2025moyamoyadiseasephysiological pages 3-4): Kaustov Chakrabarti. Moyamoya disease: physiological mechanisms and treatment approaches. Apr 2025. URL: https://doi.org/10.20944/preprints202504.1113.v1, doi:10.20944/preprints202504.1113.v1.

17. (NCT05619068 chunk 1): Xin Lou. The Evolution and Prognosis of Moyamoya Disease. Chinese PLA General Hospital. 2022. ClinicalTrials.gov Identifier: NCT05619068

18. (bagyinszky2025multisystemicimpactof pages 4-6): Eva Bagyinszky, YoungSoon Yang, and Seong Soo A. An. Multisystemic impact of rnf213 arg4810lys: a comprehensive review of moyamoya disease and associated vasculopathies. International Journal of Molecular Sciences, 26:7864, Aug 2025. URL: https://doi.org/10.3390/ijms26167864, doi:10.3390/ijms26167864. This article has 5 citations.

19. (calandrelli2026moyamoyavasculopathyand pages 5-6): Rosalinda Calandrelli, Carlo Augusto Mallio, Caterina Bernetti, Luca Massimi, and Fabio Pilato. Moyamoya vasculopathy and atypical moyamoya-like patterns: insights into diagnosis and therapeutic implications. NeuroSci, 7:27, Feb 2026. URL: https://doi.org/10.3390/neurosci7010027, doi:10.3390/neurosci7010027. This article has 0 citations.

20. (kappel2024managementofmoyamoya pages 5-6): Ari D Kappel, Abdullah H. Feroze, Erickson F. Torio, Madhav Sukumaran, and Rose Du. Management of moyamoya disease: a review of current and future therapeutic strategies. Journal of Neurosurgery, 141:975-982, Oct 2024. URL: https://doi.org/10.3171/2024.1.jns221977, doi:10.3171/2024.1.jns221977. This article has 27 citations and is from a domain leading peer-reviewed journal.

21. (ye2023rnf213lossoffunctionpromotes pages 11-13): Fei Ye, Xingyang Niu, Feng Liang, Yuanyuan Dai, Jie Liang, Jiaoxing Li, Xiaoxin Wu, Hanyue Zheng, Tiewei Qi, and Wenli Sheng. Rnf213 loss-of-function promotes pathological angiogenesis in moyamoya disease via the hippo pathway. Brain, 146:4674-4689, Jul 2023. URL: https://doi.org/10.1093/brain/awad225, doi:10.1093/brain/awad225. This article has 60 citations and is from a highest quality peer-reviewed journal.

22. (ye2023rnf213lossoffunctionpromotes pages 10-11): Fei Ye, Xingyang Niu, Feng Liang, Yuanyuan Dai, Jie Liang, Jiaoxing Li, Xiaoxin Wu, Hanyue Zheng, Tiewei Qi, and Wenli Sheng. Rnf213 loss-of-function promotes pathological angiogenesis in moyamoya disease via the hippo pathway. Brain, 146:4674-4689, Jul 2023. URL: https://doi.org/10.1093/brain/awad225, doi:10.1093/brain/awad225. This article has 60 citations and is from a highest quality peer-reviewed journal.

23. (ye2023rnf213lossoffunctionpromotes pages 1-2): Fei Ye, Xingyang Niu, Feng Liang, Yuanyuan Dai, Jie Liang, Jiaoxing Li, Xiaoxin Wu, Hanyue Zheng, Tiewei Qi, and Wenli Sheng. Rnf213 loss-of-function promotes pathological angiogenesis in moyamoya disease via the hippo pathway. Brain, 146:4674-4689, Jul 2023. URL: https://doi.org/10.1093/brain/awad225, doi:10.1093/brain/awad225. This article has 60 citations and is from a highest quality peer-reviewed journal.

24. (ye2023rnf213lossoffunctionpromotes pages 2-3): Fei Ye, Xingyang Niu, Feng Liang, Yuanyuan Dai, Jie Liang, Jiaoxing Li, Xiaoxin Wu, Hanyue Zheng, Tiewei Qi, and Wenli Sheng. Rnf213 loss-of-function promotes pathological angiogenesis in moyamoya disease via the hippo pathway. Brain, 146:4674-4689, Jul 2023. URL: https://doi.org/10.1093/brain/awad225, doi:10.1093/brain/awad225. This article has 60 citations and is from a highest quality peer-reviewed journal.

25. (bagyinszky2025multisystemicimpactof pages 17-18): Eva Bagyinszky, YoungSoon Yang, and Seong Soo A. An. Multisystemic impact of rnf213 arg4810lys: a comprehensive review of moyamoya disease and associated vasculopathies. International Journal of Molecular Sciences, 26:7864, Aug 2025. URL: https://doi.org/10.3390/ijms26167864, doi:10.3390/ijms26167864. This article has 5 citations.

26. (xu2024insightsintothe pages 3-4): Shuangxiang Xu, Tong-Tong Chen, Jin Yu, Lei Wan, Jianjian Zhang, Jincao Chen, Wei Wei, and Xiang Li. Insights into the regulatory role of epigenetics in moyamoya disease: current advances and future prospectives. Molecular Therapy - Nucleic Acids, 35:102281, Sep 2024. URL: https://doi.org/10.1016/j.omtn.2024.102281, doi:10.1016/j.omtn.2024.102281. This article has 12 citations.

27. (xu2024insightsintothe pages 16-17): Shuangxiang Xu, Tong-Tong Chen, Jin Yu, Lei Wan, Jianjian Zhang, Jincao Chen, Wei Wei, and Xiang Li. Insights into the regulatory role of epigenetics in moyamoya disease: current advances and future prospectives. Molecular Therapy - Nucleic Acids, 35:102281, Sep 2024. URL: https://doi.org/10.1016/j.omtn.2024.102281, doi:10.1016/j.omtn.2024.102281. This article has 12 citations.

28. (xu2024insightsintothe pages 13-14): Shuangxiang Xu, Tong-Tong Chen, Jin Yu, Lei Wan, Jianjian Zhang, Jincao Chen, Wei Wei, and Xiang Li. Insights into the regulatory role of epigenetics in moyamoya disease: current advances and future prospectives. Molecular Therapy - Nucleic Acids, 35:102281, Sep 2024. URL: https://doi.org/10.1016/j.omtn.2024.102281, doi:10.1016/j.omtn.2024.102281. This article has 12 citations.

29. (zeng2025rnf213variantand pages 2-4): Chaofan Zeng, Peicong Ge, Zihan Yin, Junlin Lu, Xiaofan Yu, Junsheng Li, Yuanren Zhai, Chenglong Liu, Qiheng He, Wei Liu, Jia Wang, Xingju Liu, Xun Ye, Qian Zhang, Rong Wang, Yan Zhang, Dong Zhang, and Jizong Zhao. <i>rnf213</i> variant and infectious burden associated with intracranial artery stenosis in moyamoya disease. Journal of the American Heart Association, Mar 2025. URL: https://doi.org/10.1161/jaha.124.036830, doi:10.1161/jaha.124.036830. This article has 2 citations.

30. (uchiyama2024adultmoyamoyadisease media aace831c): S. Uchiyama and Miki Fujimura. Adult moyamoya disease and moyamoya syndrome: what is new? Cerebrovascular Diseases Extra, 14:86-94, Jul 2024. URL: https://doi.org/10.1159/000540254, doi:10.1159/000540254. This article has 15 citations and is from a peer-reviewed journal.

31. (lee2023surgicalrevascularizationsfor pages 12-13): Keng Siang Lee, John J. Y. Zhang, Sanjay Bhate, Vijeya Ganesan, Dominic Thompson, Greg James, and Adikarige Haritha Dulanka Silva. Surgical revascularizations for pediatric moyamoya: a systematic review, meta-analysis, and meta-regression analysis. Child's Nervous System, 39:1225-1243, Feb 2023. URL: https://doi.org/10.1007/s00381-023-05868-6, doi:10.1007/s00381-023-05868-6. This article has 23 citations.

32. (lee2023surgicalrevascularizationsfor pages 1-2): Keng Siang Lee, John J. Y. Zhang, Sanjay Bhate, Vijeya Ganesan, Dominic Thompson, Greg James, and Adikarige Haritha Dulanka Silva. Surgical revascularizations for pediatric moyamoya: a systematic review, meta-analysis, and meta-regression analysis. Child's Nervous System, 39:1225-1243, Feb 2023. URL: https://doi.org/10.1007/s00381-023-05868-6, doi:10.1007/s00381-023-05868-6. This article has 23 citations.

33. (santos2025managementofmoyamoyaa pages 1-3): DE Santos, G Chmutin, and E Chmutin. Management of moyamoya disease: a systematic review and meta-analysis on surgical revascularization, outcomes and clinical manifestations. Unknown journal, 2025.

34. (NCT04205578 chunk 1): yuanli Zhao. NBP in Patients With Moyamoya Disease of High Risk for Ischemic Cerebrovascular Events. yuanli Zhao. 2020. ClinicalTrials.gov Identifier: NCT04205578

35. (NCT04917003 chunk 1): Ji Xunming,MD,PhD. Safety and Efficacy of Remote Ischemic Conditioning Combined EDAS on Ischemic Moyamoya Disease. Capital Medical University. 2021. ClinicalTrials.gov Identifier: NCT04917003

36. (NCT02319980 chunk 1): Hanqiang Jiang,MD. The Adult Hemorrhagic Moyamoya Surgery Study. Huashan Hospital. 2015. ClinicalTrials.gov Identifier: NCT02319980

37. (NCT02982135 chunk 1): liuxingju. Direct Bypass Versus Indirect Bypass in Treatment of Adults Hemorrhagic Moyamoya Disease. liuxingju. 2016. ClinicalTrials.gov Identifier: NCT02982135