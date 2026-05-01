---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:54.072209'
end_time: '2026-04-24T17:14:21.684377'
duration_seconds: 807.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oppositional Defiant Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oppositional Defiant Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Oppositional Defiant Disorder** covering all of the
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
- **Disease Name:** Oppositional Defiant Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Oppositional Defiant Disorder** covering all of the
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


## Comprehensive Research Report: Oppositional Defiant Disorder (ODD)

### Target Disease
- **Disease name:** Oppositional Defiant Disorder (ODD)
- **Category:** Psychiatric (childhood disruptive behavior disorder)
- **MONDO ID:** Not found in retrieved sources (gap noted).

---

## 1. Disease Information

### 1.1 Overview / concise definition
Oppositional Defiant Disorder (ODD) is a disruptive behavior disorder characterized by a persistent pattern of **angry/irritable mood**, **argumentative/defiant behavior**, and **vindictiveness** that causes distress or impairment. DSM-5-TR conceptualizes ODD symptoms across these three dimensions. (hawes2023oppositionaldefiantdisorder pages 1-6, hawes2023oppositionaldefiantdisorder pages 55-59)

A DSM-5–based diagnostic summary in the retrieved corpus describes ODD as **“a pattern of angry/irritable mood, argumentative/defiant behaviour, or vindictiveness lasting ≥ 6 months”** with a minimum number of symptoms and impairment, and severity specified by the number of settings affected. (hawes2023oppositionaldefiantdisorder pages 55-59)

### 1.2 Key identifiers / classification (available evidence)
**Important limitation:** The retrieved full texts did **not** provide explicit ICD-10/ICD-11 alphanumeric code strings, MeSH IDs, or MONDO IDs; the below reflects classification *placement* and specifier content only.

- **DSM-5-TR:** ODD is defined by symptom criteria and a severity specifier based on number of settings. (hawes2023oppositionaldefiantdisorder pages 16-19, hawes2023oppositionaldefiantdisorder pages 55-59)
- **ICD-10 vs ICD-11 placement (as stated in retrieved text):** one source states that in **ICD-10**, ODD was classified as a **subtype of Conduct Disorder**, whereas in **ICD-11** it is classified within a **“Disruptive behaviour or dissocial disorder”** grouping (with Conduct Disorder also included). (balia2020…behaviourin pages 26-29)
- **ICD-11 specifiers highlighted in the 2023 Primer:** ‘with limited prosocial emotions (LPE)’, ‘with chronic irritability-anger’, and ‘without chronic irritability-anger’. (hawes2023oppositionaldefiantdisorder pages 19-22)

### 1.3 Synonyms / alternative names
Common clinical phrasing includes **“oppositional-defiant behavior”** and **“oppositional defiant symptoms.”** (NCT06410495 chunk 1, NCT06194994 chunk 1)

### 1.4 Evidence source types
This report is based on **aggregated disease-level resources** (review/primer, meta-analysis), plus **human clinical trials/cohorts**, and molecular/physiology studies. (hawes2023oppositionaldefiantdisorder pages 1-6, boldrini2023systematicreviewand pages 9-12, ezpeleta2019firstincidenceage pages 1-2, barker2018amethylomewideassociation pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (multifactorial)
Current synthesis supports ODD as a **multifactorial** disorder arising from **interactions between genetic liability and environmental contexts**, with social-relationship mechanisms contributing to symptom maintenance. (hawes2023oppositionaldefiantdisorder pages 1-6)

### 2.2 Risk factors (genetic and environmental)

#### Genetic risk (heritability; polygenic architecture)
Twin/family evidence summarized in the 2023 Nature Reviews Disease Primers article indicates **moderate-to-high heritability** for ODD, with reported ranges **0.34–0.73**, and substantial non-shared environmental influence. (hawes2023oppositionaldefiantdisorder pages 6-9)

In a GWAS/candidate-gene study of ODD symptom dimensions in an ADHD clinical sample, the background states that ODD heritability has been estimated around **0.60**, while molecular findings were limited (no genome-wide significant hits in that study). (aebi2016gene‐setandmultivariate pages 1-2)

#### Environmental / psychosocial risk
A longitudinal cohort study (ages 3–9) identified risk factors for a first ODD episode including **negative affectivity**, **difficulties in inhibitory and emotional control**, **punitive parenting**, and **maternal internalising problems**, among others. (ezpeleta2019firstincidenceage pages 1-2)

### 2.3 Protective factors
Explicit protective factors were not enumerated as such in the retrieved excerpts. Indirectly, the treatment literature and longitudinal work imply that **early identification**, **supportive parenting practices**, and **evidence-based interventions** can improve outcomes and may function as protective influences at the population level. (hawes2023oppositionaldefiantdisorder pages 33-36, ezpeleta2019firstincidenceage pages 1-2)

### 2.4 Gene–environment and developmental embedding (epigenetic evidence)
A methylome-wide association study using DNA methylation at birth and trajectories of ODD behaviors (ages 7–13) reported that methylation signatures associated with ODD/headstrong trajectories were linked to **prenatal risk exposures** (e.g., maternal anxiety; cigarette smoking) and were partly genetically influenced, consistent with developmental embedding of exposures. The abstract states: **“DNA methylation associated with prenatal risk exposures of maternal anxiety (headstrong) and cigarette smoking (ODD and headstrong).”** (barker2018amethylomewideassociation pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype domains
ODD symptom dimensions (DSM-5-TR framing) include:
- **Angry/irritable mood**
- **Argumentative/defiant behavior**
- **Vindictiveness** (hawes2023oppositionaldefiantdisorder pages 1-6, hawes2023oppositionaldefiantdisorder pages 55-59)

DSM-5-TR criteria summarized in the 2023 Primer include 8 symptom items (e.g., temper loss, touchy/easily annoyed, angry/resentful; argues with authority figures; defies/refuses; deliberately annoys; blames others; spiteful/vindictive), with duration ≥6 months and impairment/distress requirements. (hawes2023oppositionaldefiantdisorder pages 55-59, hawes2023oppositionaldefiantdisorder pages 16-19)

### 3.2 Age of onset, progression, and frequency
- **Typical onset:** before age 8. (hawes2023oppositionaldefiantdisorder pages 1-6)
- **Preschool/childhood incidence:** In a Spanish cohort (ages 3–9), onset probability increased at age 4 (2.7%) and 5 (4.4%), decreased through age 7 (1.9%), then increased again to age 9 (3.6%); cumulative risk of new cases up to age 9 was **21.9%**. (ezpeleta2019firstincidenceage pages 1-2)

### 3.3 Heterogeneity and specifiers/subtypes
- ODD is heterogeneous; DSM symptom dimensions show differential associations with internalizing vs externalizing outcomes. (hawes2023oppositionaldefiantdisorder pages 16-19)
- ICD-11 specifiers include:
  - **With limited prosocial emotions (LPE)** (callous–unemotional traits; includes an ICD-11–only additional criterion of **“insensitivity to punishment”**) (hawes2023oppositionaldefiantdisorder pages 19-22)
  - **With chronic irritability-anger** vs **without chronic irritability-anger** (hawes2023oppositionaldefiantdisorder pages 19-22)

### 3.4 Quality-of-life and functioning impacts
ODD can persist into adolescence/adulthood and is associated with adverse outcomes across health, education, employment, and relationships, with heterogeneity (outcomes not inevitable if symptoms desist). (hawes2023oppositionaldefiantdisorder pages 33-36)

A symptom-level impairment study in a clinical ADHD/DBD cohort reported that individual ODD symptoms differ in functional impact; for example, the ODD symptom **“Argues with Adults”** contributed strongly to explained variance in global functional impairment linked to disruptive symptoms. (hawes2023oppositionaldefiantdisorder pages 6-9)

### 3.5 Suggested HPO terms (examples; ontology suggestions)
**Note:** These are suggested mappings based on the described clinical features; direct HPO database extraction was not performed in-tool.
- Irritable mood / anger: **HP:0000737 (Irritability)** (suggested)
- Temper outbursts: **HP:0000719 (Aggressive behavior)** (suggested)
- Defiant/argumentative behavior: **HP:0031936 (Oppositional behavior)** (suggested; term availability may vary)
- Vindictiveness/spitefulness: map to behavioral abnormality terms under **Abnormality of behavior (HP:0000708)** (suggested)
- Executive dysfunction: **HP:0031510 (Executive dysfunction)** (suggested)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes
No single causal gene is established for ODD in the retrieved evidence; ODD is best supported as **polygenic/multifactorial** with shared liability across externalizing phenotypes. (hawes2023oppositionaldefiantdisorder pages 6-9)

### 4.2 Molecular genetic findings (primary literature)
A GWAS/candidate-gene study of ODD subdimensions in ADHD evaluated polymorphisms in dopaminergic/serotonergic/oxytocin pathways (including DRD4 exon3 VNTR, 5-HTTLPR, OXTR SNPs) and performed multivariate GWAS, but reported no genome-wide significant loci; top-ranked genes formed an interaction landscape centered on **beta-catenin signaling** and **neurite outgrowth**. (aebi2016gene‐setandmultivariate pages 1-2)

A broader GWAS in ADHD with disruptive behavior disorders (including ODD/CD) identified genome-wide significant loci (e.g., rs7118422; OR 1.17), and found higher SNP-heritability for ADHD+DBDs vs ADHD alone (0.34 vs 0.20), with strong genetic correlations with aggression and antisocial behavior (rg ~0.81–0.82). (aebi2016gene‐setandmultivariate pages 1-2)

### 4.3 Epigenetic information
The methylome-wide study (birth methylation → ODD trajectories) supports epigenetic correlates and prenatal exposure associations (maternal anxiety; cigarette smoking). (barker2018amethylomewideassociation pages 1-2)

### 4.4 Somatic vs germline; allele frequencies; ClinVar-type variant annotations
Not available / not applicable in retrieved evidence.

---

## 5. Environmental Information

The retrieved evidence emphasizes psychosocial and family-system factors rather than toxins/occupational exposures.

- **Parenting and family mental health:** punitive parenting and maternal internalising problems were risk factors for first-episode ODD in a longitudinal cohort. (ezpeleta2019firstincidenceage pages 1-2)
- **Prenatal exposures:** maternal anxiety and cigarette smoking were associated with methylation signatures linked to ODD/headstrong trajectories. (barker2018amethylomewideassociation pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Systems-level mechanistic models
A key mechanistic account highlights **coercive parent–child cycles** maintained by social learning and reinforcement, potentially evolving into maladaptive relational strategies and sustaining oppositional behavior. (hawes2023oppositionaldefiantdisorder pages 55-59)

### 6.2 Neurocognitive mechanisms
ODD has been linked to deficits in reinforcement learning, emotion processing, and social cognition, including impaired learning from punishment and difficulties recognizing negative facial expressions (especially anger), and executive function/self-regulation deficits that may persist even without ADHD comorbidity. (hawes2023oppositionaldefiantdisorder pages 12-16)

A neuropsychological case-control study found that visual working memory and inhibitory control were impaired in ODD and CD groups vs controls, and that **anger recognition** was impaired in ODD; deficits were not explained by ADHD/internalizing comorbidity. (hawes2023oppositionaldefiantdisorder pages 16-19)

### 6.3 Neuroimaging correlates
The 2023 Primer summarizes structural MRI findings including reduced volumes in orbitofrontal and ventromedial prefrontal regions (some patterns suggested as more ODD-specific) and functional hypo-responsivity across amygdala/insula/OFC/ACC/striatal and other regions involved in emotion recognition/regulation, error processing, and reward learning. (hawes2023oppositionaldefiantdisorder pages 55-59)

### 6.4 Stress physiology / autonomic function (biomarker-adjacent)
The 2023 Primer notes associations between ODD and **lower basal cortisol** and **blunted cortisol responses to psychological stress**, and reports that cortisol hyporeactivity predicts weaker response to parent management training in ODD. (hawes2023oppositionaldefiantdisorder pages 12-16)

### 6.5 Suggested GO biological process terms (examples; suggestions)
- Emotion regulation: **GO:0019220 (regulation of nervous system process)** / **GO:0032091 (negative regulation of protein binding)** not specific; more appropriate is **GO:0019220**-like; specific emotion terms are limited in GO; consider **GO:0050890 (cognition)** and **GO:0007610 (behavior)** (suggested)
- Reward learning / reinforcement: **GO:0007611 (learning or memory)** (suggested)
- Stress response: **GO:0006950 (response to stress)** (suggested)

### 6.6 Suggested Cell Ontology (CL) terms (examples; suggestions)
Mechanisms implicate corticolimbic circuits; cell types are not directly assayed in retrieved evidence. Candidate CL terms for annotation (hypothesis-level):
- **CL:0000540 (neuron)**
- **CL:0000127 (astrocyte)**
- **CL:0000548 (animal cell)** (general)

---

## 7. Anatomical Structures Affected

ODD is primarily a neurobehavioral disorder with correlates in brain systems for emotion regulation, reward/punishment learning, and executive control.

Neuroimaging synthesis implicates:
- **Amygdala**, **anterior insula**, **orbitofrontal cortex**, **anterior cingulate cortex**, **striatum**, and ventromedial prefrontal regions, among others. (hawes2023oppositionaldefiantdisorder pages 55-59, hawes2023oppositionaldefiantdisorder pages 16-19)

Suggested UBERON terms (examples; suggestions):
- **UBERON:0000955 (brain)**
- **UBERON:0001873 (amygdala)**
- **UBERON:0000451 (prefrontal cortex)**
- **UBERON:0001882 (striatum)**

---

## 8. Temporal Development

- **Onset:** often before age 8; cohort evidence indicates preschool years are a critical period for onset risk and prevention targeting. (hawes2023oppositionaldefiantdisorder pages 1-6, ezpeleta2019firstincidenceage pages 1-2)
- **Course:** symptoms may desist or persist; persistence into adulthood is documented in longitudinal follow-up syntheses and predicts adverse outcomes across multiple domains. (hawes2023oppositionaldefiantdisorder pages 33-36)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Representative-sample point prevalence estimates cluster around **~3–5%** (meta-analyses summarized in the 2023 Primer: ~3.3% ages 5–18; ~3.9% ages 1–7). Clinical and juvenile-justice samples show substantially higher rates (clinical 28–65%; juvenile justice ~43%). (hawes2023oppositionaldefiantdisorder pages 6-9)

A cumulative lifetime prevalence estimate of **~10.2%** is mentioned in the 2023 Primer (noted as variable across samples). (hawes2023oppositionaldefiantdisorder pages 6-9)

### 9.2 Sex ratio
A modest male predominance is reported in childhood (~1.6–1.7:1), diminishing by adolescence; adult sex differences may be absent in some samples. (hawes2023oppositionaldefiantdisorder pages 6-9)

### 9.3 Genetic architecture
ODD shows moderate-to-high heritability and shared genetic liability with externalizing and internalizing phenotypes, loading on a higher-order externalizing genetic factor. (hawes2023oppositionaldefiantdisorder pages 6-9)

---

## 10. Diagnostics

### 10.1 Clinical criteria and assessment
DSM-5-TR criteria require ≥4 symptoms (of 8), duration ≥6 months, distress/impairment, and frequency thresholds depending on age (<5 years: most days; ≥5 years: at least once per week). (hawes2023oppositionaldefiantdisorder pages 16-19)

### 10.2 Specifiers and differential diagnosis considerations
ICD-11 introduces specifiers (LPE; chronic irritability-anger) that reflect heterogeneity and overlap with callous–unemotional traits and chronic irritability phenotypes. (hawes2023oppositionaldefiantdisorder pages 19-22)

The 2023 Primer notes that DSM-IV previously excluded ODD when CD was present, and DSM-5 removed that restriction, affecting prevalence estimation and diagnostic conventions. (hawes2023oppositionaldefiantdisorder pages 6-9)

### 10.3 Screening instruments and workflow (real-world)
The 2023 Primer describes a stepped approach: parent/teacher rating scales for screening, followed by more intensive clinical interviews/observations for those screening positive; obtaining multi-informant data is important because cross-setting symptoms indicate severity. Examples include ASEBA and BASC-3 (normed but not DSM-item aligned), SDQ (brief), and DSM-aligned scales like the DBD Rating Scale; parent-rated DBD showed **positive predictive power >0.90** for structured interview diagnoses in pediatric samples cited in the Primer. (hawes2023oppositionaldefiantdisorder pages 19-22)

Suggested MAXO terms:
- Screening for behavioral disorder: **MAXO:0000506 (screening procedure)** (suggested)
- Structured diagnostic interview: **MAXO:0000471 (psychiatric evaluation)** (suggested)

---

## 11. Outcome / Prognosis

ODD is associated with broad impairment and can persist into adulthood, but outcomes are heterogeneous; desistence is associated with better prognosis. (hawes2023oppositionaldefiantdisorder pages 33-36)

A Spanish cohort analysis reported that early onset was associated with markedly higher depression risk; one excerpt notes increased risk of depression “by **5.76**” versus children without ODD (as reported in the paper excerpt). (ezpeleta2019firstincidenceage pages 6-7)

Comorbidity profiles may predict worse functioning and poorer long-term treatment outcomes; in a clinical sample, the “Moderate Anxiety/High Conduct Problems” subgroup had worse executive functioning/emotional self-control and worse long-term psychosocial treatment outcomes. (halldorsdottir2023cooccurringconductproblems pages 1-2)

---

## 12. Treatment

### 12.1 Psychosocial interventions (first-line evidence base)
Parenting interventions grounded in social learning principles have the strongest empirical support across childhood and adolescence, with developmental staging enabling increased child participation and teacher/individual components for older youth. (hawes2023oppositionaldefiantdisorder pages 55-59)

A 2-year follow-up RCT comparing PMT vs PMT + group CBT (Coping Power Program) found long-term effectiveness of both arms for reduced disruptive behavior problems and harsh parenting and increased emotion regulation/social communication; combined treatment did not provide broad long-term benefits beyond PMT except earlier improvements in emotion regulation/social communication. (hawes2023oppositionaldefiantdisorder pages 1-6)

A 2024 RCT in Brazil comparing online vs face-to-face parent training (as add-ons to standard treatment) found: **“Parent training was effective in reducing symptoms of ADHD (p = 0.030) and ODD (p = 0.026) irrespective of modality (p = 1.000).”** (paiva2024parenttrainingfor pages 1-2)

A 2023 meta-analysis of psychosocial treatments for disruptive behavior disorders in adolescence synthesized RCTs across psychotherapy/training/counseling and delivery formats (group/family/individual/school-linked combined), supporting psychosocial treatment efficacy as a category while emphasizing methodological variation. (boldrini2023systematicreviewand pages 9-12)

Suggested MAXO terms:
- Behavioral parent training / parent management training: **MAXO:0000217 (behavior therapy)** (suggested)
- Cognitive behavioral therapy: **MAXO:0000127 (cognitive behavioral therapy)** (suggested)
- Telehealth delivery of behavioral intervention: **MAXO:0000753 (telemedicine)** (suggested)

### 12.2 Pharmacotherapy
No ODD-specific pharmacotherapy standard was established in the retrieved evidence; medication trials largely target **comorbid ADHD** with ODD outcomes.

Examples from ClinicalTrials.gov:
- **Atomoxetine** trial in ADHD + ODD (COMPLETED; N=181; primary endpoint SNAP-IV Revised ODD subscale at 9 weeks). (NCT00406354 chunk 1)
- **Clonidine extended-release oral suspension** (Onyda XR) Phase IV trial planned for ADHD + ODD with ODD outcomes including Conners 4 ODD scale. (NCT07044609 chunk 1, NCT07044609 chunk 2)

---

## 13. Prevention

The 2023 Primer emphasizes **early- to middle-childhood** as the key window when interventions may be most effective and economical and could prevent chronic antisocial trajectories. (hawes2023oppositionaldefiantdisorder pages 36-39, hawes2023oppositionaldefiantdisorder pages 33-36)

Prevention/implementation barriers include limited infrastructure in underserved areas, parental mental health/household adversity affecting engagement, and low mental health literacy (ODD dismissed as “bad behaviour”). (hawes2023oppositionaldefiantdisorder pages 36-39)

Suggested MAXO terms:
- Early intervention: **MAXO:0000747 (early intervention)** (suggested)
- Parenting support/education: **MAXO:0000208 (patient education)** (suggested)

---

## 14. Other Species / Natural Disease

No veterinary/natural disease analogs with explicit taxonomy identifiers were found in the retrieved evidence set; therefore, this section is **not available** from current sources.

---

## 15. Model Organisms

No validated model-organism systems specific to ODD were identified in the retrieved corpus; mechanistic evidence is largely human neuroimaging/psychophysiology and epidemiologic genetics rather than animal models. (hawes2023oppositionaldefiantdisorder pages 12-16, hawes2023oppositionaldefiantdisorder pages 55-59)

---

## 2023–2024 Recent Developments (high priority)

Key recent advances in 2023–2024 sources include:
1. **High-authority synthesis of ODD across diagnosis, epidemiology, mechanisms, and implementation** in Nature Reviews Disease Primers (2023), consolidating prevalence (~3–5%), comorbidity rates, heritability estimates, and identifying key mechanistic hypotheses (emotion-regulation circuitry; punishment sensitivity) and implementation gaps. (hawes2023oppositionaldefiantdisorder pages 1-6, hawes2023oppositionaldefiantdisorder pages 6-9, hawes2023oppositionaldefiantdisorder pages 33-36)
2. **Digital/online parent training implementation evidence** (2024 RCT) demonstrating online PT can reduce ODD symptoms comparably to face-to-face delivery, supporting scalable service delivery in low-resource contexts. (paiva2024parenttrainingfor pages 1-2)
3. **Phenotype stratification for prognosis/treatment response** in treatment-seeking youth, where co-occurring conduct problems and anxiety define subgroups with differential executive/emotion-control deficits and outcomes. (halldorsdottir2023cooccurringconductproblems pages 1-2)
4. **New/active trials focusing on moderators and comorbid targets**, including an RCT explicitly testing emotion regulation as a treatment moderator (NCT06194994) and digital dyadic sleep/insomnia intervention for youth with ODD (NCT06410495). (NCT06194994 chunk 1, NCT06410495 chunk 1)

---

## Evidence-synthesis Table (key sources)

| Source (first author, year) | Type (review/RCT/cohort/epigenetics/GWAS/registry) | Population | Key findings/statistics | Mechanism highlights | PMID | URL | Publication date/month |
|---|---|---|---|---|---|---|---|
| Hawes, 2023 | Review / Primer | ODD across child/adolescent populations; synthesizes epidemiology, diagnosis, neurobiology, treatment | Population prevalence ~3–5%; lifetime prevalence estimate ~10.2%; male predominance in childhood ~1.6–1.7:1; common co-occurrence: ADHD 28.9%, separation anxiety 20.3%, generalized anxiety 14.9%, depressive disorder 13.9%, CD 11.5%; heritability 0.34–0.73; onset typically before age 8; parenting interventions have strongest support, with brief early-childhood parenting interventions showing large effects and broader disruptive-behavior interventions moderate effects (hawes2023oppositionaldefiantdisorder pages 1-6, hawes2023oppositionaldefiantdisorder pages 6-9, hawes2023oppositionaldefiantdisorder pages 55-59, hawes2023oppositionaldefiantdisorder pages 33-36) | ODD conceptualized in dimensions (angry/irritable, argumentative/defiant, vindictive); coercive parent–child cycles; reduced amygdala/insula/OFC/ACC/striatal responses; altered reward/punishment processing; cortisol hypo-reactivity and autonomic hypoarousal support emotion-regulation and social-cognitive dysfunction models (hawes2023oppositionaldefiantdisorder pages 16-19, hawes2023oppositionaldefiantdisorder pages 12-16, hawes2023oppositionaldefiantdisorder pages 19-22) | Not in text | https://doi.org/10.1038/s41572-023-00441-6 | Jun 2023 |
| Ezpeleta, 2019 | Cohort | Spanish general-population children followed ages 3–9 | Probability of onset increased at age 4 (2.7%) and 5 (4.4%), decreased to age 7 (1.9%), rose again by age 9 (3.6%); cumulative risk of new ODD cases up to age 9 was 21.9%; pooled prevalence cited as 3.6%; early onset linked to higher depression comorbidity, later onset to greater impairment/symptom burden (ezpeleta2019firstincidenceage pages 1-2) | Risk factors for first episode included subthreshold ODD, high irritability/headstrong symptoms, ADHD and other comorbidity, negative affectivity, poor inhibitory/emotional control, punitive parenting, maternal internalizing problems (ezpeleta2019firstincidenceage pages 1-2) | Not in text | https://doi.org/10.1136/bmjopen-2018-022493 | Mar 2019 |
| Helander, 2023 | RCT follow-up | Children with ODD in randomized trial of parent management training (PMT) vs PMT + Coping Power Program | Two-year follow-up: both PMT alone and PMT+CBT reduced disruptive behavior problems and harsh parenting and improved emotion regulation/social communication; combination did not show significant long-term superiority over PMT alone overall (helander2023parentmanagementtraining pages 5-7) | Suggests durable benefit of parenting-focused intervention; emotion-regulation and social-communication skills are modifiable treatment targets (helander2023parentmanagementtraining pages 5-7) | Not in text | https://doi.org/10.1007/s10578-021-01306-3 | Jan 2023 |
| Paiva, 2024 | RCT | Families of children with ADHD and disruptive behavior/ODD symptoms in Brazil; standard treatment vs online PT vs face-to-face PT | ODD comorbidity in ADHD noted as reaching 50% in background; parent training reduced ADHD symptoms (p=0.030) and ODD symptoms (p=0.026) irrespective of online vs face-to-face modality (modality p=1.000); improved physical quality-of-life domains for children (p=0.009) and parents (p=0.050) (paiva2024parenttrainingfor pages 1-2) | Supports scalable digital/online parent-training implementation where access is limited; family environment emphasized as prognostically important (paiva2024parenttrainingfor pages 1-2) | Not in text | https://doi.org/10.3389/fpsyg.2024.1293244 | Feb 2024 |
| Boldrini, 2023 | Systematic review / meta-analysis | 17 RCTs, 1,954 adolescents (61% male), mean age 14.09 years, with ODD/CD/externalizing symptoms | Included psychotherapy, training, counseling, combined psychosocial interventions; designed to meta-analyze change in externalizing symptoms and acceptability across psychosocial treatments in adolescence (boldrini2023systematicreviewand pages 9-12) | Highlights real-world psychosocial treatment formats (group, family, individual, school-linked combined approaches) for adolescent disruptive behavior disorders, including ODD (boldrini2023systematicreviewand pages 9-12) | Not in text | https://doi.org/10.1016/j.jaac.2022.05.002 | May 2023 |
| Halldorsdottir, 2023 | Clinical cohort / treatment-outcome stratification | 134 treatment-seeking youths with ODD (mean age 9.67 years; 36.6% female) | Four profiles identified by anxiety and conduct symptoms; >30% of youths with ODD also meet CD criteria and up to 60% meet anxiety disorder criteria in cited clinical literature; Moderate Anxiety/High Conduct Problems subgroup had more severe behavior, worse emotional self-control/executive functioning, and worse long-term psychosocial treatment outcomes (halldorsdottir2023cooccurringconductproblems pages 1-2) | Supports heterogeneity model of ODD in which co-occurring anxiety and conduct problems mark distinct mechanisms and prognosis (negative emotionality, executive dysfunction) (halldorsdottir2023cooccurringconductproblems pages 1-2) | Not in text | https://doi.org/10.3390/ijerph20043405 | Feb 2023 |
| Aebi, 2016 | GWAS / candidate-gene study | Children/adolescents with ADHD assessed for ODD dimensions/subtypes | ODD heritability estimated around 0.60 in background; no hypothesis-driven association for DRD4, 5-HTTLPR, or OXTR variants; no genome-wide significant loci; inadequate parenting significantly associated with all ODD dimensions, especially defiant/vindictive behavior (aebi2016gene‐setandmultivariate pages 1-2) | Top-ranked genes converged in a protein interaction network centered on beta-catenin signaling and neurite outgrowth, suggesting neurodevelopmental pathway involvement (aebi2016gene‐setandmultivariate pages 1-2) | Not in text | https://doi.org/10.1002/ajmg.b.32346 | Jul 2016 |
| Barker, 2018 | Epigenetics / methylome-wide association | 671 mother–child pairs from epidemiological birth cohort; DNA methylation at birth linked to ODD trajectories ages 7–13 | Methylome-wide significant associations found for ODD and headstrong trajectories, not irritable; ODD worldwide lifetime prevalence quoted as 10%; majority of ODD cases have at least one concurrent psychiatric diagnosis (barker2018amethylomewideassociation pages 1-2) | Biological overlap between ODD/headstrong and ADHD; DNA methylation partly genetically influenced; prenatal maternal anxiety associated with headstrong methylation signatures and cigarette smoking with ODD/headstrong signals (barker2018amethylomewideassociation pages 1-2) | Not in text | https://doi.org/10.1111/cdev.12957 | Sep 2018 |
| Demontis, 2021 | GWAS | ADHD + disruptive behavior disorders (including ODD/CD): 3,802 cases, 31,305 controls, plus Chinese replication | Identified 3 genome-wide significant loci for ADHD+DBDs; chromosome 11 locus rs7118422 replicated across ancestries (P=3.15×10^-10, OR=1.17); SNP-heritability 0.34 for ADHD+DBDs vs 0.20 for ADHD alone; strong genetic correlations with aggression (rg=0.81) and antisocial behavior (rg=0.82) (aebi2016gene‐setandmultivariate pages 1-2) | Indicates ODD/CD comorbidity with ADHD reflects heavier common-variant burden and aggression-related polygenic loading (aebi2016gene‐setandmultivariate pages 1-2) | Not in text | https://doi.org/10.1038/s41467-020-20443-2 | Jan 2021 |
| Deters, 2020 | Neuropsychology / case-control | Youth aged 8–18 with ODD (n=44), CD (n=48, with/without ODD), and healthy controls (n=86) | Visual working memory and inhibitory control impaired in ODD and CD vs controls; anger recognition impaired in ODD; deficits not explained by comorbid ADHD or internalizing symptoms (hawes2023oppositionaldefiantdisorder pages 16-19) | Supports distinct neurocognitive deficits in ODD, especially inhibitory control and anger-recognition dysfunction, independent of ADHD comorbidity (hawes2023oppositionaldefiantdisorder pages 16-19) | Not in text | https://doi.org/10.1080/15622975.2020.1747114 | Apr 2020 |
| Thöne, 2023 | Symptom-level clinical study | 474 German school-age children in ESCAschool ADHD/disruptive behavior cohort (81% male; mean age 8.90 years) | ODD symptom “Argues with Adults” contributed 10% of explained variance in global functional impairment related to ODD/CD/CU symptoms; relationships with adults/children and recreational activities were especially linked to disruptive symptoms (hawes2023oppositionaldefiantdisorder pages 6-9) | Demonstrates that individual ODD symptoms differ in impact on functioning, useful for symptom-prioritized assessment and intervention planning (hawes2023oppositionaldefiantdisorder pages 6-9) | Not in text | https://doi.org/10.1007/s10862-023-10025-z | Mar 2023 |
| NCT06194994, 2024 | Registry / interventional trial | Planned 196 Icelandic-speaking children aged 6–12 with ODD | Recruiting RCT testing whether emotion regulation moderates response to Parent Management Training vs Tuning Your Temper CBT; outcomes include Disruptive Behaviour Rating Scale and K-SADS-PL diagnostic status pre, post, 6 and 18 months (NCT06194994 chunk 1, NCT06194994 chunk 2) | Explicitly tests precision-treatment hypothesis that emotion dysregulation is a mechanistic moderator of ODD treatment response (NCT06194994 chunk 1, NCT06194994 chunk 2) | Not in text | https://clinicaltrials.gov/study/NCT06194994 | Jan 2024 |
| NCT06410495, 2024 | Registry / interventional trial | Children aged 8–17 with prior ODD diagnosis and insomnia plus parents | Recruiting pilot web-based dyadic CBT-I trial (NiteCAPP SINCC); outcomes include daily sleep diary sleep efficiency/onset latency/total sleep time, actigraphy, HRV, and DBD checklist measures (NCT06410495 chunk 1) | Connects sleep dysregulation, parenting stress, and oppositional symptoms in a digital family-based implementation model (NCT06410495 chunk 1) | Not in text | https://clinicaltrials.gov/study/NCT06410495 | May 2024 |
| NCT07044609, 2025 | Registry / phase IV drug trial | Planned children aged 6–12 with ADHD and comorbid ODD | Not-yet-recruiting Phase IV randomized placebo-controlled trial of clonidine ER oral suspension; primary outcome ADHD-RS-5 change; secondary outcomes include Conners 4 ODD scale, CGI, sleep, vitals, ECG, labs, suicidality (NCT07044609 chunk 1, NCT07044609 chunk 2) | Illustrates ongoing pharmacologic implementation focused on ADHD+ODD comorbidity rather than ODD-only monotherapy (NCT07044609 chunk 1, NCT07044609 chunk 2) | Not in text | https://clinicaltrials.gov/study/NCT07044609 | Jul 2025 |
| NCT00406354, 2006 | Registry / phase IV drug trial | 181 children/adolescents aged 6–17 with ADHD and comorbid ODD in Germany | Completed 3-arm randomized double-blind placebo-controlled atomoxetine trial; primary endpoint SNAP-IV Revised ODD subscale at 9 weeks, with ADHD and family-impact secondary measures (NCT00406354 chunk 1) | Represents real-world psychopharmacology for ADHD+ODD comorbidity using ADHD-directed medication and ODD symptom outcomes (NCT00406354 chunk 1) | Not in text | https://clinicaltrials.gov/study/NCT00406354 | Nov 2006 |


*Table: This table summarizes the most important citable sources retrieved in the session on Oppositional Defiant Disorder, spanning reviews, cohorts, RCTs, molecular studies, and active clinical trials. It highlights the strongest recent evidence on epidemiology, mechanisms, and treatment implementation for rapid use in the final report.*

---

## Notes on evidence gaps and constraints
- **PMIDs:** Not available in the retrieved full-text excerpts for most sources; therefore, PMID fields are reported as “Not in text.”
- **MONDO/MeSH/ICD code strings:** Not identified in retrieved texts; report includes classification placement/specifiers but not alphanumeric codes.
- **ODD-specific pharmacotherapy efficacy:** Limited in retrieved evidence; pharmacotherapy evidence largely pertains to ADHD with comorbid ODD endpoints.


References

1. (hawes2023oppositionaldefiantdisorder pages 1-6): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

2. (hawes2023oppositionaldefiantdisorder pages 55-59): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

3. (hawes2023oppositionaldefiantdisorder pages 16-19): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

4. (balia2020…behaviourin pages 26-29): C Balia. … behaviour in children and adolescents with conduct disorder or oppositional defiant disorder: neuropsychological characterization and drug treatments. preliminary …. Unknown journal, 2020.

5. (hawes2023oppositionaldefiantdisorder pages 19-22): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

6. (NCT06410495 chunk 1): Melanie Stearns. Digital Dyadic Family Based Intervention to Improve Sleep in Children with ODD and Their Parents: NiteCAPP SINCC (Pilot). University of South Florida. 2024. ClinicalTrials.gov Identifier: NCT06410495

7. (NCT06194994 chunk 1): Urdur Njardvik. Emotion Regulation as a Moderator of Two Different Treatments for Children With ODD. University of Iceland. 2024. ClinicalTrials.gov Identifier: NCT06194994

8. (boldrini2023systematicreviewand pages 9-12): Tommaso Boldrini, Viola Ghiandoni, Elisa Mancinelli, Silvia Salcuni, and Marco Solmi. Systematic review and meta-analysis: psychosocial treatments for disruptive behavior symptoms and disorders in adolescence. Journal of the American Academy of Child and Adolescent Psychiatry, May 2023. URL: https://doi.org/10.1016/j.jaac.2022.05.002, doi:10.1016/j.jaac.2022.05.002. This article has 17 citations and is from a highest quality peer-reviewed journal.

9. (ezpeleta2019firstincidenceage pages 1-2): Lourdes Ezpeleta, J Blas Navarro, Nuria de la Osa, Eva Penelo, and Josep Maria Domènech. First incidence, age of onset outcomes and risk factors of onset of dsm-5 oppositional defiant disorder: a cohort study of spanish children from ages 3 to 9. BMJ Open, 9:e022493, Mar 2019. URL: https://doi.org/10.1136/bmjopen-2018-022493, doi:10.1136/bmjopen-2018-022493. This article has 29 citations and is from a peer-reviewed journal.

10. (barker2018amethylomewideassociation pages 1-2): Edward D Barker, Esther Walton, Charlotte A M Cecil, Richard Rowe, Sara R Jaffee, Barbara Maughan, Thomas G O'Connor, Argyris Stringaris, Alan J Meehan, Wendy McArdle, Caroline L Relton, and Tom R Gaunt. A methylome-wide association study of trajectories of oppositional defiant behaviors and biological overlap with attention deficit hyperactivity disorder. Child Development, 89:1839-1855, Sep 2018. URL: https://doi.org/10.1111/cdev.12957, doi:10.1111/cdev.12957. This article has 34 citations and is from a highest quality peer-reviewed journal.

11. (hawes2023oppositionaldefiantdisorder pages 6-9): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

12. (aebi2016gene‐setandmultivariate pages 1-2): Marcel Aebi, Marjolein M. J. van Donkelaar, Geert Poelmans, Jan K. Buitelaar, Edmund J. S. Sonuga‐Barke, Argyris Stringaris, IMAGE consortium, Stephen V. Faraone, Barbara Franke, Hans‐Christoph Steinhausen, and Kimm J. E. van Hulzen. Gene‐set and multivariate genome‐wide association analysis of oppositional defiant behavior subtypes in attention‐deficit/hyperactivity disorder. American Journal of Medical Genetics, 171:573-588, Jul 2016. URL: https://doi.org/10.1002/ajmg.b.32346, doi:10.1002/ajmg.b.32346. This article has 61 citations.

13. (hawes2023oppositionaldefiantdisorder pages 33-36): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

14. (hawes2023oppositionaldefiantdisorder pages 12-16): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

15. (ezpeleta2019firstincidenceage pages 6-7): Lourdes Ezpeleta, J Blas Navarro, Nuria de la Osa, Eva Penelo, and Josep Maria Domènech. First incidence, age of onset outcomes and risk factors of onset of dsm-5 oppositional defiant disorder: a cohort study of spanish children from ages 3 to 9. BMJ Open, 9:e022493, Mar 2019. URL: https://doi.org/10.1136/bmjopen-2018-022493, doi:10.1136/bmjopen-2018-022493. This article has 29 citations and is from a peer-reviewed journal.

16. (halldorsdottir2023cooccurringconductproblems pages 1-2): Thorhildur Halldorsdottir, Maria G Fraire, Deborah A. G. Drabick, and Thomas H. Ollendick. Co-occurring conduct problems and anxiety: implications for the functioning and treatment of youth with oppositional defiant disorder. International Journal of Environmental Research and Public Health, 20:3405, Feb 2023. URL: https://doi.org/10.3390/ijerph20043405, doi:10.3390/ijerph20043405. This article has 11 citations.

17. (paiva2024parenttrainingfor pages 1-2): Gabrielle Chequer de Castro Paiva, Jonas Jardim de Paula, Danielle de Souza Costa, Antônio Alvim-Soares, Daniel Augusto Ferreira e Santos, Julia Silva Jales, Marco Aurélio Romano-Silva, and Débora Marques de Miranda. Parent training for disruptive behavior symptoms in attention deficit hyperactivity disorder: a randomized clinical trial. Frontiers in Psychology, Feb 2024. URL: https://doi.org/10.3389/fpsyg.2024.1293244, doi:10.3389/fpsyg.2024.1293244. This article has 22 citations and is from a peer-reviewed journal.

18. (NCT00406354 chunk 1):  Comparison of Atomoxetine Versus Placebo in Children and Adolescents With ADHD and Comorbid ODD in Germany. Eli Lilly and Company. 2006. ClinicalTrials.gov Identifier: NCT00406354

19. (NCT07044609 chunk 1):  A Study to Assess the Effectiveness and Safety of Clonidine Extended-Release OnydaTM XR in Children With ADHD and ODD. Las Vegas Medical Research, LLC DBA Vector Clinical Trials. 2025. ClinicalTrials.gov Identifier: NCT07044609

20. (NCT07044609 chunk 2):  A Study to Assess the Effectiveness and Safety of Clonidine Extended-Release OnydaTM XR in Children With ADHD and ODD. Las Vegas Medical Research, LLC DBA Vector Clinical Trials. 2025. ClinicalTrials.gov Identifier: NCT07044609

21. (hawes2023oppositionaldefiantdisorder pages 36-39): David J. Hawes, Frances Gardner, Mark R. Dadds, Paul J. Frick, Eva R. Kimonis, Jeffrey D. Burke, and Graeme Fairchild. Oppositional defiant disorder. Nature Reviews Disease Primers, 9:1-17, Jun 2023. URL: https://doi.org/10.1038/s41572-023-00441-6, doi:10.1038/s41572-023-00441-6. This article has 98 citations.

22. (helander2023parentmanagementtraining pages 5-7): Maria Helander, Pia Enebrink, Clara Hellner, and Johan Ahlen. Parent management training combined with group-cbt compared to parent management training only for oppositional defiant disorder symptoms: 2-year follow-up of a randomized controlled trial. Child Psychiatry and Human Development, 54:1112-1126, Jan 2023. URL: https://doi.org/10.1007/s10578-021-01306-3, doi:10.1007/s10578-021-01306-3. This article has 22 citations and is from a peer-reviewed journal.

23. (NCT06194994 chunk 2): Urdur Njardvik. Emotion Regulation as a Moderator of Two Different Treatments for Children With ODD. University of Iceland. 2024. ClinicalTrials.gov Identifier: NCT06194994