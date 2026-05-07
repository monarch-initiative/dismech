---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T12:02:14.509603'
end_time: '2026-05-07T12:33:35.256457'
duration_seconds: 1880.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Warburg micro syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Warburg micro syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Warburg micro syndrome** covering all of the
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
- **Disease Name:** Warburg micro syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Warburg micro syndrome** covering all of the
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


# Warburg Micro Syndrome (WARBM): Comprehensive Disease Characteristics Report

## Executive summary
Warburg Micro syndrome (also called **MICRO syndrome**) is an **extremely rare**, **autosomal recessive**, genetically heterogeneous neuro-ophthalmologic and neuroendocrine disorder characterized by congenital/early ocular malformations (notably congenital cataracts), severe neurodevelopmental impairment with brain malformations (e.g., corpus callosum hypoplasia/agenesis, cortical malformations), and hypogonadism/genital anomalies. The canonical disease genes are **RAB3GAP1, RAB3GAP2, RAB18, and TBC1D20**, which converge on **RAB18-regulated membrane trafficking**, **ER organization**, **lipid droplet biology**, and **autophagy**. Recent reports (2023) emphasize prenatal detection via fetal ultrasound plus rapid phenotype-driven sequencing. (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3, lallar2023congenitalcataractand pages 1-2, handley2015warburgmicrosyndrome pages 1-2)

## 1. Disease information
### 1.1 What is the disease?
WARBM is described in recent clinical genetics literature as a **rare autosomal recessive** disorder with **ocular, neurological/neurodevelopmental, and endocrine/neuroendocrine** abnormalities. Core features include microcephaly, microphthalmia, microcornea, congenital cataracts, optic atrophy, corpus callosum hypoplasia/agenesis, severe intellectual disability, spasticity, hypotonia, and hypogonadism. (ullah2023exomesequencingidentifies pages 1-5, akkus2023firstclinicalreport pages 1-2, pickerminh2014largehomozygousrab3gap1 pages 1-3)

### 1.2 Key identifiers and synonyms
A key practical identifier set in the retrieved primary literature is OMIM/MIM subtype mapping (WARBM1–4), alongside widely used synonyms/abbreviations (WARBM, WMS, MICRO syndrome). A structured identifier table is provided below.

| Disease / subtype | Synonyms / abbreviations in retrieved sources | Syndrome OMIM/MIM ID | Associated gene | Gene MIM ID | Not found in retrieved sources | Key citation sources |
|---|---|---|---|---|---|---|
| Warburg Micro syndrome (overall) | Warburg micro syndrome; Warburg Micro Syndrome; WARBM; WARBM syndrome; WMS; MICRO syndrome; Micro syndrome (akkus2023firstclinicalreport pages 5-6, ullah2023exomesequencingidentifies pages 9-13, bouzidi2022clinicalandgenetic pages 20-21) | Overall syndrome OMIM/MIM not explicitly provided in retrieved sources; subtype IDs available below (pickerminh2014largehomozygousrab3gap1 pages 1-3) | Genetically heterogeneous: RAB3GAP1, RAB3GAP2, RAB18, TBC1D20 (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3) | Gene MIMs available by subtype below (pickerminh2014largehomozygousrab3gap1 pages 1-3) | Orphanet ID not found; ICD-10 not found; ICD-11 not found; MeSH not found; MONDO not found in retrieved sources (pickerminh2014largehomozygousrab3gap1 pages 1-3, pickerminh2014largehomozygousrab3gap1 pages 3-5, akkus2023firstclinicalreport pages 5-6, ullah2023exomesequencingidentifies pages 9-13) | (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3, akkus2023firstclinicalreport pages 5-6, ullah2023exomesequencingidentifies pages 9-13, bouzidi2022clinicalandgenetic pages 20-21) |
| Warburg Micro syndrome 1 | WARBM1; Warburg Micro Syndrome 1 (pickerminh2014largehomozygousrab3gap1 pages 1-3, pickerminh2014largehomozygousrab3gap1 pages 3-5, pickerminh2014largehomozygousrab3gap1 pages 5-6) | MIM#600118 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | RAB3GAP1 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | MIM*602536 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | Orphanet ID not found; ICD-10 not found; ICD-11 not found; MeSH not found; MONDO not found in retrieved sources (pickerminh2014largehomozygousrab3gap1 pages 1-3) | (pickerminh2014largehomozygousrab3gap1 pages 1-3, pickerminh2014largehomozygousrab3gap1 pages 5-6) |
| Warburg Micro syndrome 2 | WARBM2; WMS2; Warburg micro syndrome 2 (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | MIM#614225 in one source; 212720 reported in one cataract review source (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | RAB3GAP2 (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | Gene MIM reported in subtype table source but not legible in retrieved summary; exact gene MIM not recoverable from provided context (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | Orphanet ID not found; ICD-10 not found; ICD-11 not found; MeSH not found; MONDO not found in retrieved sources (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) |
| Warburg Micro syndrome 3 | WARBM3; Warburg micro syndrome 3 (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | MIM#614222 (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | RAB18 (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | Gene MIM reported as *602207 in retrieved disease summary (ullah2023exomesequencingidentifies pages 1-5) | Orphanet ID not found; ICD-10 not found; ICD-11 not found; MeSH not found; MONDO not found in retrieved sources (pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) | (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3, bell2020congenitalcataracta pages 13-15) |
| Warburg Micro syndrome 4 | WARBM4; Warburg micro syndrome 4 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | MIM#615663 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | TBC1D20 (pickerminh2014largehomozygousrab3gap1 pages 1-3) | Gene MIM reported as *611663 in retrieved disease summary (ullah2023exomesequencingidentifies pages 1-5) | Orphanet ID not found; ICD-10 not found; ICD-11 not found; MeSH not found; MONDO not found in retrieved sources (pickerminh2014largehomozygousrab3gap1 pages 1-3) | (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3) |


*Table: This table compiles the identifiers and names for Warburg Micro syndrome and its subtypes using only retrieved evidence. It highlights available OMIM/MIM subtype information, associated genes, and explicitly notes identifier systems that were not found in the retrieved sources.*

**Note on missing identifiers:** In the retrieved corpus, explicit **Orphanet/Orpha codes, ICD-10/ICD-11 codes, MeSH headings, and MONDO identifiers** were not found; these should be populated from those databases directly in a production knowledge base workflow. (pickerminh2014largehomozygousrab3gap1 pages 1-3, pickerminh2014largehomozygousrab3gap1 pages 3-5, akkus2023firstclinicalreport pages 5-6)

### 1.3 Source type (individual vs aggregated)
Most disease feature statements in this report derive from **individual/family case reports/series** and **mechanistic primary studies** (human fibroblasts, fetal tissue, and animal models). Aggregated perspectives include an autophagy-disorders review and a congenital cataract management review, but much of the WARBM-specific evidence is patient-based. (dafsari2025anupdateon pages 7-9, bell2020congenitalcataracta pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants (loss-of-function or damaging variants) in **RAB3GAP1, RAB3GAP2, RAB18, or TBC1D20**. (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3)

**Key mechanistic framing:** Warburg Micro syndrome can be caused directly by **RAB18 deficiency** or indirectly via loss of its regulators (**RAB3GAP complex** or **TBC1D20**), with consequent alteration of RAB18 level/localization/dynamics. (handley2015warburgmicrosyndrome pages 1-2, handley2015warburgmicrosyndrome pages 2-3)

### 2.2 Risk factors
**Genetic risk factors:** autosomal recessive inheritance with frequent reports in consanguineous families; multiple series explicitly report consanguinity and segregation consistent with AR inheritance. (lallar2023congenitalcataractand pages 2-3, akkus2023firstclinicalreport pages 2-3, ullah2023exomesequencingidentifies pages 1-5, albayrak2021fromcataractto pages 1-2)

**Environmental risk factors:** Not supported as causal in the retrieved corpus. Case-based prenatal workups often include **TORCH testing** as an alternative explanation for fetal cataracts; negative TORCH results support a genetic etiology in those cases. (lallar2023congenitalcataractand pages 2-3)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No explicit gene–environment interactions were identified in the retrieved sources.

## 3. Phenotypes (with ontology suggestions)
### 3.1 Core phenotype domains and typical timing
WARBM is typically **congenital/early-onset** (ocular anomalies at birth or detectable prenatally; severe developmental impairment evident in infancy). Prenatal ultrasound detection of congenital cataracts can occur at ~18–25 weeks gestation in reports/cohorts. (lallar2023congenitalcataractand pages 1-2, wang2025prenatalultrasounddiagnosis pages 7-9, noel2025biallelicnullrab3gap1 pages 1-2)

### 3.2 Ocular phenotypes (symptoms/signs)
**Key features:** congenital bilateral cataracts, microphthalmia, microcornea, optic atrophy/optic nerve atrophy, and atrophic optic discs. (ullah2023exomesequencingidentifies pages 1-5, akkus2023firstclinicalreport pages 3-4, wang2025prenatalultrasounddiagnosis pages 7-9)

**Frequency examples from a 7-patient WARBM1 cohort:** bilateral congenital cataracts in 7/7; microphthalmia 5/7; microcornea 3/7; optic atrophy 3/7; photosensitivity 5/7. (albayrak2021fromcataractto pages 1-2)

**Suggested HPO terms (examples):**
- Congenital cataract **HP:0000519**
- Microphthalmia **HP:0000568**
- Microcornea **HP:0000482**
- Optic atrophy **HP:0000648**

**Affected anatomy (UBERON examples):** lens of eye (UBERON), optic nerve (UBERON), cornea (UBERON), retina (UBERON).

### 3.3 Neurodevelopmental / neurologic phenotypes
**Key features:** severe developmental delay/intellectual disability (often absent speech), hypotonia (reported as universal in compiled case literature), spasticity/spastic diplegia, and structural brain malformations including corpus callosum hypoplasia/agenesis and cortical malformations (pachygyria/polymicrogyria). (akkus2023firstclinicalreport pages 1-2, albayrak2021fromcataractto pages 2-3, pickerminh2014largehomozygousrab3gap1 pages 1-3)

**MRI findings:** hypoplasia/agenesis of corpus callosum, polymicrogyria/pachygyria, cerebral atrophy, cerebellar atrophy/hypoplasia, myelination defects. (noel2025biallelicnullrab3gap1 pages 1-2, pickerminh2014largehomozygousrab3gap1 pages 1-3, pickerminh2014largehomozygousrab3gap1 pages 3-5)

**Example cohort statistic:** In the 7-patient WARBM1 re-evaluation study, **corpus callosum hypoplasia was detected in all patients**, including complete agenesis in one. (albayrak2021fromcataractto pages 2-3)

**Suggested HPO terms (examples):**
- Global developmental delay **HP:0001263**
- Intellectual disability, severe/profound **HP:0010864 / HP:0002187**
- Hypotonia **HP:0001252**
- Spasticity **HP:0001257**
- Agenesis of corpus callosum **HP:0001274** / Corpus callosum hypoplasia **HP:0002079**
- Polymicrogyria **HP:0002126**

**Suggested brain anatomy (UBERON examples):** corpus callosum, cerebral cortex, cerebellum; optic chiasm is specifically noted as hypotrophic in one WARBM1 deletion case. (pickerminh2014largehomozygousrab3gap1 pages 3-5)

### 3.4 Neuroendocrine / genital phenotypes
**Key features:** hypogonadism with micropenis and cryptorchidism; described across case-based literature and emphasized as part of the core syndrome. (akkus2023firstclinicalreport pages 1-2, albayrak2021fromcataractto pages 2-3)

**Suggested HPO terms (examples):**
- Cryptorchidism **HP:0000028**
- Micropenis **HP:0000054**
- Hypogonadism **HP:0000135**

### 3.5 Other reported phenotypes/complications
**Skeletal/bone:** osteopenia/osteoporosis highlighted in a WARBM1 family with a large RAB3GAP1 deletion; vitamin D supplementation did not improve it in that report, supporting a potential primary disease association. (pickerminh2014largehomozygousrab3gap1 pages 3-5, pickerminh2014largehomozygousrab3gap1 pages 1-3)

**Peripheral neuropathy/cardiomyopathy:** cited as rare additional features in literature summarized by a 2023 case report. (akkus2023firstclinicalreport pages 5-6)

**Suggested HPO terms (examples):**
- Osteopenia **HP:0000938** / Osteoporosis **HP:0000939**
- Peripheral neuropathy **HP:0009830**
- Cardiomyopathy **HP:0001638**

### 3.6 Quality of life impact
Direct QoL instrument data (EQ-5D, SF-36, PROMIS) were not identified in the retrieved corpus. Functionally, severe neurodevelopmental impairment is common, including inability to achieve major motor and communication milestones in many reported cases. (akkus2023firstclinicalreport pages 1-2, albayrak2021fromcataractto pages 2-3)

## 4. Genetic / molecular information
### 4.1 Causal genes
Canonical WARBM genes: **RAB3GAP1, RAB3GAP2, RAB18, TBC1D20**. (ullah2023exomesequencingidentifies pages 1-5, pickerminh2014largehomozygousrab3gap1 pages 1-3)

### 4.2 Pathogenic variants and variant spectrum
A gene/variant summary table based on retrieved evidence is provided below.

| Subtype | Gene | Inheritance | Variant examples (HGVS) | Variant class | Study population / case count | Notable genotype–phenotype notes | Key sources (with DOI URLs) |
|---|---|---|---|---|---|---|---|
| WARBM1 | **RAB3GAP1** | Autosomal recessive | c.520C>T (p.Arg174Ter); c.559C>T (p.Arg187Ter) | Nonsense / predicted loss-of-function | 2 unrelated Turkish patients (2023 report) | Severe classic WARBM phenotype with microcephaly, microphthalmia, microcornea, bilateral congenital cataracts, severe intellectual disability, congenital hypotonia; parents heterozygous carriers (akkus2023firstclinicalreport pages 3-4) | Akkuş 2023, DOI: https://doi.org/10.1055/s-0043-1768693 (akkus2023firstclinicalreport pages 3-4) |
| WARBM1 | **RAB3GAP1** | Autosomal recessive | c.2891A>G (p.Gln964Arg) | Missense, ACMG likely pathogenic | Consanguineous Pakistani family; 2 affected siblings / 3 affected individuals reported in family context | Ocular anomalies, severe ID, spastic diplegia, hypogonadism, cerebral atrophy, corpus callosum hypoplasia, polymicrogyria; authors note RAB3GAP1 accounts for ~70% of WARBM cases (ullah2023exomesequencingidentifies pages 1-5, ullah2023exomesequencingidentifies pages 5-9) | Ullah 2023, DOI: https://doi.org/10.1002/jdn.10264 (ullah2023exomesequencingidentifies pages 1-5, ullah2023exomesequencingidentifies pages 5-9) |
| WARBM1 (prenatal) | **RAB3GAP1** | Autosomal recessive | c.131delT (p.Leu44Trpfs*50) | Frameshift | 1 fetus diagnosed prenatally at 18 weeks | Prenatal ultrasound clues were bilateral congenital cataracts and narrow cavum septi pellucidi; microarray normal; phenotype-driven NGS established diagnosis; 25% recurrence risk counseling and discussion of CVS/PGT-M for future pregnancies (lallar2023congenitalcataractand pages 1-2, lallar2023congenitalcataractand pages 2-3) | Lallar 2023, DOI: https://doi.org/10.1055/s-0043-57022 (lallar2023congenitalcataractand pages 1-2, lallar2023congenitalcataractand pages 2-3) |
| WARBM1 (prenatal/postnatal follow-up) | **RAB3GAP1** | Autosomal recessive | c.718C>T (p.Gln240*); c.1879dupA (p.Thr627Asnfs*4) | Nonsense + frameshift | 1 case (Case 17) from prenatal congenital cataract cohort | Prenatal bilateral cataracts; bilateral lensectomy at 3 months; optic nerve atrophy by 1 year and poor vision by age 4, illustrating that surgery may not normalize outcome when syndromic neuro-ophthalmic disease is present (wang2025prenatalultrasounddiagnosis pages 7-9) | Wang 2025, DOI: https://doi.org/10.2147/IJWH.S511730 (wang2025prenatalultrasounddiagnosis pages 7-9) |
| WARBM1 | **RAB3GAP1** | Autosomal recessive | c.258_261delAGAA (p.Gly88ArgfsTer5); c.2187_2188delGAinsCT (p.Met729_Lys730delinsIleTer); c.2606+1G>A; c.2861_2862dupGC (p.Pro955AlafsTer74) | Frameshift / in-frame truncating / splice-site | 7 probands newly characterized; literature review spanning 78 families | Authors state congenital cataract and corpus callosum hypo/agenesis are pathognomonic for WARBM; all 7 had bilateral congenital cataracts and corpus callosum involvement; variant spectrum skewed toward LoF (~44% frameshift, ~36% nonsense); reported ancestry enrichment among reviewed cases: Egyptian 33.33%, Pakistani 22.72%, Turkish 18.18% (albayrak2021fromcataractto pages 3-4, albayrak2021fromcataractto pages 1-2, albayrak2021fromcataractto pages 4-6, albayrak2021fromcataractto pages 2-3) | Albayrak 2021, DOI: https://doi.org/10.1002/ajmg.a.62234 (albayrak2021fromcataractto pages 3-4, albayrak2021fromcataractto pages 1-2, albayrak2021fromcataractto pages 4-6, albayrak2021fromcataractto pages 2-3) |
| WARBM1 | **RAB3GAP1** | Autosomal recessive | Large homozygous intragenic deletion spanning exons 4-15 (~50.4 kb; ~45% coding sequence) | Multi-exon deletion / structural loss-of-function | 2 affected siblings from consanguineous Kurdish-Armenian family | Typical WARBM1 phenotype with congenital cataracts, microphthalmia/microcornea, postnatal microcephaly, severe ID, pachygyria, corpus callosum dysgenesis/agenesis of splenium; osteopenia/osteoporosis highlighted as an additional feature (pickerminh2014largehomozygousrab3gap1 pages 3-5, pickerminh2014largehomozygousrab3gap1 pages 1-3) | Picker-Minh 2014, DOI: https://doi.org/10.1186/s13023-014-0113-9 (pickerminh2014largehomozygousrab3gap1 pages 3-5, pickerminh2014largehomozygousrab3gap1 pages 1-3) |
| WARBM3 | **RAB18** | Autosomal recessive | Specific human HGVS variants not provided in retrieved context; causal loss-of-function mutations established | Loss-of-function | Multiple WARBM families in primary discovery/functional literature; exact variant list not available in retrieved context | Primary mechanism is direct RAB18 deficiency; affected children present at birth with congenital cataracts; Rab18-mutant mice recapitulate congenital nuclear cataracts, atonic pupils, hind-limb weakness, enlarged lipid droplets, and neuronal cytoskeletal disorganization (handley2015warburgmicrosyndrome pages 1-2, carpanini2014anovelmouse pages 1-2, carpanini2014anovelmouse pages 3-4) | Bem 2011, DOI: https://doi.org/10.1016/j.ajhg.2011.03.012; Handley 2015, DOI: https://doi.org/10.1098/rsob.150047; Carpanini 2014, DOI: https://doi.org/10.1242/dmm.015222 (handley2015warburgmicrosyndrome pages 1-2, carpanini2014anovelmouse pages 1-2, carpanini2014anovelmouse pages 3-4) |
| WARBM4 | **TBC1D20** | Autosomal recessive | Specific human HGVS variants not provided in retrieved context; five distinct human loss-of-function mutations reported in 77 WARBM families screened | Loss-of-function | Human WARBM families plus blind sterile (**bs**) mouse model | TBC1D20 loss causes WARBM in humans and cataracts/male infertility in bs mice; shared cell phenotype includes aberrant lipid droplets/Golgi changes and defective autophagy flux, supporting a trafficking-autophagy disease mechanism (handley2015warburgmicrosyndrome pages 1-2, sidjanin2016tbc1d20mediatesautophagy pages 7-9, liegel2013lossoffunctionmutationsin pages 1-2) | Liegel 2013, DOI: https://doi.org/10.1016/j.ajhg.2013.10.011; Handley 2015, DOI: https://doi.org/10.1098/rsob.150047 (handley2015warburgmicrosyndrome pages 1-2, sidjanin2016tbc1d20mediatesautophagy pages 7-9, liegel2013lossoffunctionmutationsin pages 1-2) |
| WARBM2 | **RAB3GAP2** | Autosomal recessive | Representative HGVS variants not available in retrieved context | Loss-of-function | Causality established as one of the four canonical WARBM genes; detailed variant examples not recovered in retrieved corpus | RAB3GAP2 encodes the noncatalytic subunit of the RAB3GAP complex; together with RAB3GAP1 it functions as a GEF for RAB18, so WARBM2 is interpreted mechanistically as indirect RAB18 dysregulation with clinically overlapping phenotype (pickerminh2014largehomozygousrab3gap1 pages 1-3, handley2015warburgmicrosyndrome pages 1-2) | Picker-Minh 2014, DOI: https://doi.org/10.1186/s13023-014-0113-9; Handley 2015, DOI: https://doi.org/10.1098/rsob.150047 (pickerminh2014largehomozygousrab3gap1 pages 1-3, handley2015warburgmicrosyndrome pages 1-2) |


*Table: This table summarizes the Warburg Micro syndrome subtype–gene architecture and representative pathogenic variants that were explicitly supported by the retrieved literature. It is useful for quickly linking subtype, variant class, inheritance, and key genotype–phenotype observations, while clearly distinguishing genes with direct variant examples from genes supported mainly by causality studies in the retrieved context.*

Key statistics from a 2021 WARBM1 cohort + literature review: RAB3GAP1 variants skew toward **loss-of-function** classes (~44% frameshift and ~36% nonsense), with additional splice and deletion classes, and suggested exon hotspotting (e.g., exon 15). (albayrak2021fromcataractto pages 4-6)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No WARBM-specific modifier genes or epigenetic drivers were identified in the retrieved corpus.

A chromosomal microarray was reported as normal in a prenatal WARBM1 diagnosis workup, supporting a single-gene etiology in that case. (lallar2023congenitalcataractand pages 2-3)

## 5. Environmental information
No non-genetic environmental or infectious causal contributors were supported as disease causes in the retrieved corpus. Prenatal differential workup includes infectious testing (TORCH) when cataracts are detected, but genetic causation is confirmed when variants are identified. (lallar2023congenitalcataractand pages 2-3)

## 6. Mechanism / pathophysiology (current understanding)
### 6.1 Unifying concept: “RAB18 deficiency/dysregulation” trafficking disorder
A central mechanistic conclusion from a primary functional study is that WARBM can arise from **direct RAB18 loss** or **indirect dysregulation** through loss of the RAB3GAP complex or TBC1D20. (handley2015warburgmicrosyndrome pages 1-2)

**Mechanistic definitions (key concepts):**
- **RAB3GAP1/RAB3GAP2** form a complex that functions as a **GEF for RAB18**. (handley2015warburgmicrosyndrome pages 1-2)
- **TBC1D20** has **RAB18 GAP activity** in vitro and acts as a regulator essential for normal RAB18 cycling/dynamics and localization, including at the ER. (handley2015warburgmicrosyndrome pages 1-2, handley2015warburgmicrosyndrome pages 2-3)

### 6.2 Cellular processes implicated
**Vesicular trafficking / ER organization / lipid droplets:** Multiple primary sources link WARBM genes to ER structure and lipid droplet phenotypes; mutant cells show altered lipid droplet formation and size. (carpanini2014anovelmouse pages 1-2, liegel2013lossoffunctionmutationsin pages 1-2)

**Autophagy:** WARBM is discussed among multisystem autophagy-related disorders, and primary tissue/cell evidence supports disrupted autophagy flux in RAB3GAP1-associated disease. (dafsari2025anupdateon pages 7-9, noel2025biallelicnullrab3gap1 pages 14-15)

**Ciliogenesis (TBC1D20):** TBC1D20 loss links Rab11 vesicle accumulation, centrosomal actin remodeling, and enhanced ciliogenesis initiation; this provides a ciliopathy-adjacent mechanism potentially relevant to multisystem features. (zhai2025tbc1d20coordinatesvesicle pages 1-1, zhai2025tbc1d20coordinatesvesicle pages 1-2)

### 6.3 Causal chain (example synthesis)
Biallelic loss-of-function in RAB3GAP1/RAB3GAP2/TBC1D20 → RAB18 activation/cycling defects and broader Rab-dependent trafficking defects → altered ER organization, lipid droplet homeostasis, autophagy/autolysosome maturation defects → neurodevelopmental disruption (neuronal migration/corticogenesis, axonal/cytoskeletal stability) and lens/optic pathway pathology → congenital cataracts, brain malformations, optic atrophy, severe neurodevelopmental disability and hypogonadism. This chain is consistent with mechanistic assertions and model-organism phenotypes in the retrieved primary literature. (handley2015warburgmicrosyndrome pages 1-2, noel2025biallelicnullrab3gap1 pages 14-15, carpanini2014anovelmouse pages 1-2, cheng2015enumutagenesisidentifies pages 1-2)

### 6.4 Suggested ontology terms for mechanisms
**GO Biological Process (examples):**
- Autophagy (GO:0006914)
- Vesicle-mediated transport (GO:0016192)
- Endoplasmic reticulum organization (GO:0007029)
- Lipid droplet organization (GO:0005811; note GO term names may differ—use GO lookup)
- Cilium assembly (GO:0042384)

**GO Cellular Component (examples):**
- Endoplasmic reticulum
- Lipid droplet
- Golgi apparatus
- Centrosome

**Cell Ontology (CL) suggestions (examples):**
- Neuron (cortical projection neuron)
- Radial glial cell (for corticogenesis defects suggested by fetal brain evidence)
- Lens fiber cell / lens epithelial cell

## 7. Anatomical structures affected
**Primary organs/systems:** eye (lens/optic nerve), brain (cerebral cortex, corpus callosum, cerebellum), endocrine/reproductive system (gonads; hypothalamic-pituitary-gonadal axis inferred from hypogonadism). (akkus2023firstclinicalreport pages 1-2, pickerminh2014largehomozygousrab3gap1 pages 1-3)

**Subcellular compartments:** ER and lipid droplets are repeatedly implicated; centrosomal trafficking and actin remodeling are implicated for TBC1D20-related pathways. (handley2015warburgmicrosyndrome pages 2-3, zhai2025tbc1d20coordinatesvesicle pages 1-1)

## 8. Temporal development
**Onset:** congenital/early (cataracts at birth; prenatal ultrasound detection reported at 18–25 weeks). (lallar2023congenitalcataractand pages 1-2, wang2025prenatalultrasounddiagnosis pages 7-9)

**Progression:** neurologic dysfunction can be progressive (spasticity; progressive hind-limb weakness in Rab18−/− mice) and ocular/optic nerve pathology may progress (optic nerve atrophy noted postoperatively by 1 year in one case). (wang2025prenatalultrasounddiagnosis pages 7-9, carpanini2014anovelmouse pages 3-4)

## 9. Inheritance and population
### 9.1 Inheritance
**Autosomal recessive** inheritance is consistent across subtype definitions, segregation in families, and cohort reports. (pickerminh2014largehomozygousrab3gap1 pages 1-3, akkus2023firstclinicalreport pages 3-4, albayrak2021fromcataractto pages 1-2)

### 9.2 Epidemiology
The syndrome is repeatedly described as **extremely rare** and incidence is **unknown** in the retrieved corpus. (ullah2023exomesequencingidentifies pages 1-5, noel2025biallelicnullrab3gap1 pages 1-2)

**Case aggregation statistic:** One 2023 report notes RAB3GAP1 homozygous pathogenic variants reported in **67 families** (reflecting literature compilation rather than prevalence). (akkus2023firstclinicalreport pages 1-2)

**Gene contribution statistic:** RAB3GAP1 is described as the most common cause, estimated at ~70% in one 2023 family report and 75% in a 2021 WARBM1-focused paper. (ullah2023exomesequencingidentifies pages 1-5, albayrak2021fromcataractto pages 1-2)

**Geographic/ancestry patterns (from literature review):** Egyptian 33.33%, Pakistani 22.72%, Turkish 18.18% of reviewed RAB3GAP1-associated families (reflecting publication-ascertainment rather than true population prevalence). (albayrak2021fromcataractto pages 3-4)

## 10. Diagnostics
### 10.1 Clinical recognition
A practical clinical heuristic emphasized in a 2021 WARBM1 re-evaluation study is that **congenital cataract plus corpus callosum hypo/agenesis** is highly suggestive (“pathognomonic” in that paper) for WARBM in appropriate clinical context. (albayrak2021fromcataractto pages 1-2)

### 10.2 Imaging
- **Prenatal ultrasound:** bilateral echogenic lenses (cataracts) and abnormalities such as narrow cavum septi pellucidi can be clues prompting invasive testing; corpus callosum may appear normal at mid-gestation even in genetically confirmed cases. (lallar2023congenitalcataractand pages 2-3, noel2025biallelicnullrab3gap1 pages 1-2)
- **Postnatal MRI:** corpus callosum hypoplasia/agenesis, pachy/polymicrogyria, cerebral/cerebellar atrophy, myelination defects. (noel2025biallelicnullrab3gap1 pages 1-2, pickerminh2014largehomozygousrab3gap1 pages 3-5)

### 10.3 Genetic testing strategies (real-world implementations)
**Prenatal:** amniocentesis with microarray (to exclude CNVs) followed by phenotype-driven NGS or single-gene testing; confirm by parental Sanger sequencing; counseling includes recurrence risk (25%) and discussion of CVS and PGT-M. (lallar2023congenitalcataractand pages 2-3)

**Postnatal:** WES pipelines and/or NGS panels; variant filtering against population databases (gnomAD/1000 Genomes) and ACMG classification are used in recent reports. (ullah2023exomesequencingidentifies pages 1-5)

### 10.4 Differential diagnosis
Prenatal cataract workups explicitly consider infections and chromosomal/single-gene syndromes (e.g., TORCH; other syndromic causes of cataract and brain anomalies). (lallar2023congenitalcataractand pages 1-2, lallar2023congenitalcataractand pages 2-3)

## 11. Outcomes / prognosis
Formal survival statistics and life expectancy were not identified in the retrieved corpus. Available evidence indicates a severe neurodevelopmental course with profound disability and limited communication in many patients. (akkus2023firstclinicalreport pages 1-2, albayrak2021fromcataractto pages 2-3)

Visual outcomes can be poor even after early cataract surgery if optic nerve atrophy and broader neuro-ophthalmic disease are present (illustrated by a prenatally detected RAB3GAP1 WARBM case with lensectomy at 3 months and poor vision at age 4). (wang2025prenatalultrasounddiagnosis pages 7-9)

## 12. Treatment
### 12.1 Pharmacotherapy
No disease-modifying pharmacologic therapies were identified in the retrieved corpus.

### 12.2 Surgical and supportive interventions
**Cataract surgery:** performed in infancy in case reports/cohorts; early detection/intervention is emphasized as important for visual development in congenital cataract generally, but WARBM-specific outcomes depend on associated optic nerve/brain pathology. (wang2025prenatalultrasounddiagnosis pages 7-9, bell2020congenitalcataracta pages 1-2)

**Supportive care:** Multidisciplinary care is a standard implementation for congenital cataracts with systemic associations (ophthalmology, pediatrics, genetics, counseling, and educational/visual supports). For WARBM, additional supportive needs include neurodevelopmental therapies, orthopedic management for spasticity/contractures, and urology/endocrinology for hypogonadism/cryptorchidism. (bell2020congenitalcataracta pages 1-2, albayrak2021fromcataractto pages 2-3)

**MAXO suggestions (examples):**
- Cataract extraction (MAXO term to be selected)
- Vision rehabilitation (MAXO)
- Genetic counseling (MAXO)
- Physical therapy / occupational therapy / speech therapy (MAXO)

### 12.3 Experimental therapies / trials
No WARBM-targeted interventional trials were identified in the retrieved evidence. A large observational rare disease registry/natural history study exists (NCT01793168), which can support case capture and outcomes research rather than testing a disease-specific intervention. (wang2025prenatalultrasounddiagnosis pages 6-6)

## 13. Prevention
Primary prevention is not applicable in the typical sense for a monogenic AR disease, but **reproductive prevention strategies** are directly supported in prenatal diagnostic literature:
- **Carrier testing** of parents and family members
- **Prenatal diagnosis** (CVS/amniocentesis) with targeted sequencing
- **Preimplantation genetic testing for monogenic disease (PGT-M)** discussed as an option in at-risk couples
These were explicitly highlighted in a prenatal WARBM1 diagnosis report. (lallar2023congenitalcataractand pages 2-3)

## 14. Other species / natural disease
Naturally occurring RAB3GAP1 loss-of-function causes a WARBM-like syndrome (POANV) in dogs:
- **Alaskan Huskies:** exon 7 SINE insertion (recessive) associated with polyneuropathy, ocular abnormalities, neuronal vacuolation; euthanasia at 8–16 months; absent from 541 controls. (wiedmer2016arab3gap1sine pages 1-5)
- **Black Russian Terriers:** RAB3GAP1 c.743delC associated with polyneuropathy, ocular defects, and neuronal vacuolation. (mhlangamutangadura2016amutationin pages 1-2)

These provide comparative biology and translational modeling opportunities. (wiedmer2016arab3gap1sine pages 1-5, mhlangamutangadura2016amutationin pages 1-2)

## 15. Model organisms
**Mouse (Rab18):** Rab18−/− models recapitulate congenital cataracts/atonic pupils and neurologic dysfunction; cellular phenotypes include enlarged lipid droplets and neuronal cytoskeletal disruption; an ENU-derived Rab18 deletion model shows sensory axon degeneration including optic nerve degeneration, aligning with optic atrophy in humans. (carpanini2014anovelmouse pages 3-4, cheng2015enumutagenesisidentifies pages 1-2, carpanini2014anovelmouse pages 2-3)

**Mouse (Tbc1d20, blind sterile/bs):** bs mice exhibit cataracts and male infertility; cellular evidence supports disrupted autophagy flux with progressive cataractogenesis beginning in late embryogenesis (E17.5) and worsening postnatally. (sidjanin2016tbc1d20mediatesautophagy pages 7-9, liegel2013lossoffunctionmutationsin pages 1-2)

**Mechanistic utility:** These models support interrogation of Rab-regulated membrane trafficking, autophagy, lipid droplet biology, and neurodevelopmental processes relevant to WARBM. (handley2015warburgmicrosyndrome pages 1-2, carpanini2014anovelmouse pages 1-2)

## Recent developments and latest research emphasis (2023–2024)
- **2023 clinical genetics:** novel or newly reported **RAB3GAP1** variants in multiple families and detailed phenotyping; continued emphasis on AR inheritance and severe neuro-ophthalmic phenotype. (ullah2023exomesequencingidentifies pages 1-5, akkus2023firstclinicalreport pages 3-4)
- **2023 prenatal implementation:** fetal ultrasound identification of congenital cataracts (and narrow CSP) combined with rapid NGS-based diagnosis and explicit counseling for CVS/PGT-M. (lallar2023congenitalcataractand pages 2-3)
- **2024 mechanistic advance (cell biology):** Warburg Micro pathway genes are increasingly integrated into broader membrane-trafficking and lipid droplet biology frameworks, including mechanistic discussion of Rab/TBC regulation at ER–lipid droplet interfaces relevant to disease. (malis2024rab1bfacilitateslipid pages 1-2)

## Evidence gaps in the retrieved corpus
- Standardized cross-ontology identifiers (Orphanet, ICD-10/11, MeSH, MONDO) were not present in the retrieved PDFs and should be added from those databases.
- Quantitative prevalence/incidence and robust survival statistics are largely unavailable in the retrieved corpus.
- Disease-specific QoL instrument data and controlled clinical management guidelines are not present; care is largely extrapolated from congenital cataract management principles and case-based multidisciplinary practice.

## Key figure/table evidence from retrieved visual content
Picker-Minh et al. provide a consolidated phenotype table (Table 1) and neuroimaging/phenotype figure (Figure 1) supporting core neuroimaging abnormalities and osteopenia/osteoporosis as an additional manifestation in WARBM1. (pickerminh2014largehomozygousrab3gap1 media f5f15d26, pickerminh2014largehomozygousrab3gap1 media 30474c79, pickerminh2014largehomozygousrab3gap1 media cfa8e10c, pickerminh2014largehomozygousrab3gap1 media e76762b9)


References

1. (ullah2023exomesequencingidentifies pages 1-5): Wahid Ullah, Muhammad Ilyas, Muhammad Tariq, Maria Imdad, Ikram Ullah, Stephanie Efthymiou, Muhammad Faheem, Muhammad Abbas, Muhammad Aamir, Muhammad Nouman, and Henry Houlden. Exome sequencing identifies a novel pathogenic variant in rab3gap1 causing warburg micro syndrome in a pakistani family. International Journal of Developmental Neuroscience, 83:368-373, Apr 2023. URL: https://doi.org/10.1002/jdn.10264, doi:10.1002/jdn.10264. This article has 0 citations and is from a peer-reviewed journal.

2. (pickerminh2014largehomozygousrab3gap1 pages 1-3): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

3. (lallar2023congenitalcataractand pages 1-2): Meenakshi Lallar, Ladbans Kaur, Meetan Preet, and U. P. Singh. Congenital cataract and narrow csp: a clue to prenatal diagnosis of rab3gap1 -associated warburg micro syndrome. Journal of Fetal Medicine, 10:046-048, Apr 2023. URL: https://doi.org/10.1055/s-0043-57022, doi:10.1055/s-0043-57022. This article has 1 citations.

4. (handley2015warburgmicrosyndrome pages 1-2): Mark T. Handley, Sarah M. Carpanini, Girish R. Mali, Duska J. Sidjanin, Irene A. Aligianis, Ian J. Jackson, and David R. FitzPatrick. Warburg micro syndrome is caused by rab18 deficiency or dysregulation. Open Biology, 5:150047, Jun 2015. URL: https://doi.org/10.1098/rsob.150047, doi:10.1098/rsob.150047. This article has 55 citations and is from a peer-reviewed journal.

5. (akkus2023firstclinicalreport pages 1-2): Nejmiye Akkuş and Tuğba Akın Duman. First clinical report of two rab3gap1 pathogenic variant in warburg micro syndrome. Journal of Pediatric Genetics, 12:193-198, May 2023. URL: https://doi.org/10.1055/s-0043-1768693, doi:10.1055/s-0043-1768693. This article has 2 citations and is from a peer-reviewed journal.

6. (akkus2023firstclinicalreport pages 5-6): Nejmiye Akkuş and Tuğba Akın Duman. First clinical report of two rab3gap1 pathogenic variant in warburg micro syndrome. Journal of Pediatric Genetics, 12:193-198, May 2023. URL: https://doi.org/10.1055/s-0043-1768693, doi:10.1055/s-0043-1768693. This article has 2 citations and is from a peer-reviewed journal.

7. (ullah2023exomesequencingidentifies pages 9-13): Wahid Ullah, Muhammad Ilyas, Muhammad Tariq, Maria Imdad, Ikram Ullah, Stephanie Efthymiou, Muhammad Faheem, Muhammad Abbas, Muhammad Aamir, Muhammad Nouman, and Henry Houlden. Exome sequencing identifies a novel pathogenic variant in rab3gap1 causing warburg micro syndrome in a pakistani family. International Journal of Developmental Neuroscience, 83:368-373, Apr 2023. URL: https://doi.org/10.1002/jdn.10264, doi:10.1002/jdn.10264. This article has 0 citations and is from a peer-reviewed journal.

8. (bouzidi2022clinicalandgenetic pages 20-21): Aymane Bouzidi, Hicham Charoute, Majida Charif, Ghita Amalou, Mostafa Kandil, Abdelhamid Barakat, and Guy Lenaers. Clinical and genetic spectrums of 413 north african families with inherited retinal dystrophies and optic neuropathies. Orphanet Journal of Rare Diseases, May 2022. URL: https://doi.org/10.1186/s13023-022-02340-7, doi:10.1186/s13023-022-02340-7. This article has 22 citations and is from a peer-reviewed journal.

9. (pickerminh2014largehomozygousrab3gap1 pages 3-5): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

10. (pickerminh2014largehomozygousrab3gap1 pages 5-6): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

11. (bell2020congenitalcataracta pages 13-15): Suzannah J. Bell, Ngozi Oluonye, Philippa Harding, and Mariya Moosajee. Congenital cataract: a guide to genetic and clinical management. Therapeutic Advances in Rare Disease, Jan 2020. URL: https://doi.org/10.1177/2633004020938061, doi:10.1177/2633004020938061. This article has 90 citations.

12. (dafsari2025anupdateon pages 7-9): Hormos Salimi Dafsari, Diego Martinelli, Afshin Saffari, Darius Ebrahimi‐Fakhari, Manolis Fanto, Carlo Dionisi‐Vici, and Heinz Jungbluth. An update on autophagy disorders. Journal of Inherited Metabolic Disease, Oct 2025. URL: https://doi.org/10.1002/jimd.12798, doi:10.1002/jimd.12798. This article has 19 citations and is from a peer-reviewed journal.

13. (bell2020congenitalcataracta pages 1-2): Suzannah J. Bell, Ngozi Oluonye, Philippa Harding, and Mariya Moosajee. Congenital cataract: a guide to genetic and clinical management. Therapeutic Advances in Rare Disease, Jan 2020. URL: https://doi.org/10.1177/2633004020938061, doi:10.1177/2633004020938061. This article has 90 citations.

14. (handley2015warburgmicrosyndrome pages 2-3): Mark T. Handley, Sarah M. Carpanini, Girish R. Mali, Duska J. Sidjanin, Irene A. Aligianis, Ian J. Jackson, and David R. FitzPatrick. Warburg micro syndrome is caused by rab18 deficiency or dysregulation. Open Biology, 5:150047, Jun 2015. URL: https://doi.org/10.1098/rsob.150047, doi:10.1098/rsob.150047. This article has 55 citations and is from a peer-reviewed journal.

15. (lallar2023congenitalcataractand pages 2-3): Meenakshi Lallar, Ladbans Kaur, Meetan Preet, and U. P. Singh. Congenital cataract and narrow csp: a clue to prenatal diagnosis of rab3gap1 -associated warburg micro syndrome. Journal of Fetal Medicine, 10:046-048, Apr 2023. URL: https://doi.org/10.1055/s-0043-57022, doi:10.1055/s-0043-57022. This article has 1 citations.

16. (akkus2023firstclinicalreport pages 2-3): Nejmiye Akkuş and Tuğba Akın Duman. First clinical report of two rab3gap1 pathogenic variant in warburg micro syndrome. Journal of Pediatric Genetics, 12:193-198, May 2023. URL: https://doi.org/10.1055/s-0043-1768693, doi:10.1055/s-0043-1768693. This article has 2 citations and is from a peer-reviewed journal.

17. (albayrak2021fromcataractto pages 1-2): Hatice Mutlu Albayrak, Nursel H. Elçioğlu, Burcu Yeter, and Kadri Karaer. From cataract to syndrome diagnosis: revaluation of warburg‐micro syndrome type 1 patients. American Journal of Medical Genetics Part A, 185:2325-2334, May 2021. URL: https://doi.org/10.1002/ajmg.a.62234, doi:10.1002/ajmg.a.62234. This article has 9 citations.

18. (wang2025prenatalultrasounddiagnosis pages 7-9): Huizhu Wang, Xin Jin, Mengmeng Wang, Hezhou Li, Juan Wu, Ling Liu, Zhengfeng Zhu, M. Qiao, Yingying Wang, and Lili Li. Prenatal ultrasound diagnosis and prognosis analysis of fetal congenital cataract. International Journal of Women's Health, Volume 17:2729-2740, Aug 2025. URL: https://doi.org/10.2147/ijwh.s511730, doi:10.2147/ijwh.s511730. This article has 0 citations and is from a peer-reviewed journal.

19. (noel2025biallelicnullrab3gap1 pages 1-2): Emma Noël, Fabien Guimiot, Yline Capri, Marianne Alison, Asha Baskaran, Clémence Delcour, David Germanaud, Sophie Lebon, Caroline Storey, Nicolas de Roux, and Adeline Orts-Del’Immagine. Biallelic null rab3gap1 variants impair cortical development and autophagy in warburg micro syndrome: evidence from fetal brain tissue and patient fibroblasts. Acta Neuropathologica Communications, Dec 2025. URL: https://doi.org/10.1186/s40478-025-02204-8, doi:10.1186/s40478-025-02204-8. This article has 0 citations and is from a peer-reviewed journal.

20. (akkus2023firstclinicalreport pages 3-4): Nejmiye Akkuş and Tuğba Akın Duman. First clinical report of two rab3gap1 pathogenic variant in warburg micro syndrome. Journal of Pediatric Genetics, 12:193-198, May 2023. URL: https://doi.org/10.1055/s-0043-1768693, doi:10.1055/s-0043-1768693. This article has 2 citations and is from a peer-reviewed journal.

21. (albayrak2021fromcataractto pages 2-3): Hatice Mutlu Albayrak, Nursel H. Elçioğlu, Burcu Yeter, and Kadri Karaer. From cataract to syndrome diagnosis: revaluation of warburg‐micro syndrome type 1 patients. American Journal of Medical Genetics Part A, 185:2325-2334, May 2021. URL: https://doi.org/10.1002/ajmg.a.62234, doi:10.1002/ajmg.a.62234. This article has 9 citations.

22. (ullah2023exomesequencingidentifies pages 5-9): Wahid Ullah, Muhammad Ilyas, Muhammad Tariq, Maria Imdad, Ikram Ullah, Stephanie Efthymiou, Muhammad Faheem, Muhammad Abbas, Muhammad Aamir, Muhammad Nouman, and Henry Houlden. Exome sequencing identifies a novel pathogenic variant in rab3gap1 causing warburg micro syndrome in a pakistani family. International Journal of Developmental Neuroscience, 83:368-373, Apr 2023. URL: https://doi.org/10.1002/jdn.10264, doi:10.1002/jdn.10264. This article has 0 citations and is from a peer-reviewed journal.

23. (albayrak2021fromcataractto pages 3-4): Hatice Mutlu Albayrak, Nursel H. Elçioğlu, Burcu Yeter, and Kadri Karaer. From cataract to syndrome diagnosis: revaluation of warburg‐micro syndrome type 1 patients. American Journal of Medical Genetics Part A, 185:2325-2334, May 2021. URL: https://doi.org/10.1002/ajmg.a.62234, doi:10.1002/ajmg.a.62234. This article has 9 citations.

24. (albayrak2021fromcataractto pages 4-6): Hatice Mutlu Albayrak, Nursel H. Elçioğlu, Burcu Yeter, and Kadri Karaer. From cataract to syndrome diagnosis: revaluation of warburg‐micro syndrome type 1 patients. American Journal of Medical Genetics Part A, 185:2325-2334, May 2021. URL: https://doi.org/10.1002/ajmg.a.62234, doi:10.1002/ajmg.a.62234. This article has 9 citations.

25. (carpanini2014anovelmouse pages 1-2): Sarah M. Carpanini, Lisa McKie, Derek Thomson, Ann K. Wright, Sarah L. Gordon, Sarah L. Roche, Mark T. Handley, Harris Morrison, David Brownstein, Thomas M. Wishart, Michael A. Cousin, Thomas H. Gillingwater, Irene A. Aligianis, and Ian J. Jackson. A novel mouse model of warburg micro syndrome reveals roles for rab18 in eye development and organisation of the neuronal cytoskeleton. Disease Models & Mechanisms, 7:711-722, Apr 2014. URL: https://doi.org/10.1242/dmm.015222, doi:10.1242/dmm.015222. This article has 48 citations and is from a domain leading peer-reviewed journal.

26. (carpanini2014anovelmouse pages 3-4): Sarah M. Carpanini, Lisa McKie, Derek Thomson, Ann K. Wright, Sarah L. Gordon, Sarah L. Roche, Mark T. Handley, Harris Morrison, David Brownstein, Thomas M. Wishart, Michael A. Cousin, Thomas H. Gillingwater, Irene A. Aligianis, and Ian J. Jackson. A novel mouse model of warburg micro syndrome reveals roles for rab18 in eye development and organisation of the neuronal cytoskeleton. Disease Models & Mechanisms, 7:711-722, Apr 2014. URL: https://doi.org/10.1242/dmm.015222, doi:10.1242/dmm.015222. This article has 48 citations and is from a domain leading peer-reviewed journal.

27. (sidjanin2016tbc1d20mediatesautophagy pages 7-9): D. J. Sidjanin, Anna K. Park, Adam Ronchetti, Jamaria Martins, and William T. Jackson. Tbc1d20 mediates autophagy as a key regulator of autophagosome maturation. Autophagy, 12:1759-1775, Aug 2016. URL: https://doi.org/10.1080/15548627.2016.1199300, doi:10.1080/15548627.2016.1199300. This article has 84 citations and is from a domain leading peer-reviewed journal.

28. (liegel2013lossoffunctionmutationsin pages 1-2): Ryan P. Liegel, Mark T. Handley, Adam Ronchetti, Stephen Brown, Lars Langemeyer, Andrea Linford, Bo Chang, Deborah J. Morris-Rosendahl, Sarah Carpanini, Renata Posmyk, Verity Harthill, Eamonn Sheridan, Ghada M.H. Abdel-Salam, Paulien A. Terhal, Francesca Faravelli, Patrizia Accorsi, Lucio Giordano, Lorenzo Pinelli, Britta Hartmann, Allison D. Ebert, Francis A. Barr, Irene A. Aligianis, and Duska J. Sidjanin. Loss-of-function mutations in tbc1d20 cause cataracts and male infertility in blind sterile mice and warburg micro syndrome in humans. American journal of human genetics, 93 6:1001-14, Dec 2013. URL: https://doi.org/10.1016/j.ajhg.2013.10.011, doi:10.1016/j.ajhg.2013.10.011. This article has 145 citations and is from a highest quality peer-reviewed journal.

29. (noel2025biallelicnullrab3gap1 pages 14-15): Emma Noël, Fabien Guimiot, Yline Capri, Marianne Alison, Asha Baskaran, Clémence Delcour, David Germanaud, Sophie Lebon, Caroline Storey, Nicolas de Roux, and Adeline Orts-Del’Immagine. Biallelic null rab3gap1 variants impair cortical development and autophagy in warburg micro syndrome: evidence from fetal brain tissue and patient fibroblasts. Acta Neuropathologica Communications, Dec 2025. URL: https://doi.org/10.1186/s40478-025-02204-8, doi:10.1186/s40478-025-02204-8. This article has 0 citations and is from a peer-reviewed journal.

30. (zhai2025tbc1d20coordinatesvesicle pages 1-1): Denghui Zhai, Lamei Li, Difei Wang, Weishu Wang, Siyang Zhao, Xue Wang, Cheng Chen, Zixuan Zhu, Weiwen Bu, Mulin Yang, Hanxiao Yin, Ying Shan, Huijie Zhao, Christopher J. Westlake, Quanlong Lu, and Jun Zhou. Tbc1d20 coordinates vesicle transport and actin remodeling to regulate ciliogenesis. The Journal of cell biology, Apr 2025. URL: https://doi.org/10.1083/jcb.202406139, doi:10.1083/jcb.202406139. This article has 4 citations.

31. (zhai2025tbc1d20coordinatesvesicle pages 1-2): Denghui Zhai, Lamei Li, Difei Wang, Weishu Wang, Siyang Zhao, Xue Wang, Cheng Chen, Zixuan Zhu, Weiwen Bu, Mulin Yang, Hanxiao Yin, Ying Shan, Huijie Zhao, Christopher J. Westlake, Quanlong Lu, and Jun Zhou. Tbc1d20 coordinates vesicle transport and actin remodeling to regulate ciliogenesis. The Journal of cell biology, Apr 2025. URL: https://doi.org/10.1083/jcb.202406139, doi:10.1083/jcb.202406139. This article has 4 citations.

32. (cheng2015enumutagenesisidentifies pages 1-2): Chih-Ya Cheng, Jaw-Ching Wu, Jin-Wu Tsai, Fang-Shin Nian, Pei-Chun Wu, Lung-Sen Kao, Ming-Ji Fann, Shih-Jen Tsai, Ying-Jay Liou, Chin-Yin Tai, and Chen-Jee Hong. Enu mutagenesis identifies mice modeling warburg micro syndrome with sensory axon degeneration caused by a deletion in rab18. Experimental Neurology, 267:143-151, May 2015. URL: https://doi.org/10.1016/j.expneurol.2015.03.003, doi:10.1016/j.expneurol.2015.03.003. This article has 14 citations and is from a peer-reviewed journal.

33. (wang2025prenatalultrasounddiagnosis pages 6-6): Huizhu Wang, Xin Jin, Mengmeng Wang, Hezhou Li, Juan Wu, Ling Liu, Zhengfeng Zhu, M. Qiao, Yingying Wang, and Lili Li. Prenatal ultrasound diagnosis and prognosis analysis of fetal congenital cataract. International Journal of Women's Health, Volume 17:2729-2740, Aug 2025. URL: https://doi.org/10.2147/ijwh.s511730, doi:10.2147/ijwh.s511730. This article has 0 citations and is from a peer-reviewed journal.

34. (wiedmer2016arab3gap1sine pages 1-5): Michaela Wiedmer, Anna Oevermann, Stephanie E Borer-Germann, Daniela Gorgas, G Diane Shelton, Michaela Drögemüller, Vidhya Jagannathan, Diana Henke, and Tosso Leeb. A <i>rab3gap1</i> sine insertion in alaskan huskies with polyneuropathy, ocular abnormalities, and neuronal vacuolation (poanv) resembling human warburg micro syndrome 1 (warbm1). G3 Genes|Genomes|Genetics, 6:255-262, Feb 2016. URL: https://doi.org/10.1534/g3.115.022707, doi:10.1534/g3.115.022707. This article has 40 citations.

35. (mhlangamutangadura2016amutationin pages 1-2): Tendai Mhlanga-Mutangadura, Gary S. Johnson, Robert D. Schnabel, Jeremy F. Taylor, Gayle C. Johnson, Martin L. Katz, G. Diane Shelton, Teresa E. Lever, Elizabeth Giuliano, Nicolas Granger, Jeremy Shomper, and Dennis P. O'Brien. A mutation in the warburg syndrome gene, rab3gap1, causes a similar syndrome with polyneuropathy and neuronal vacuolation in black russian terrier dogs. Neurobiology of Disease, 86:75-85, Feb 2016. URL: https://doi.org/10.1016/j.nbd.2015.11.016, doi:10.1016/j.nbd.2015.11.016. This article has 29 citations and is from a domain leading peer-reviewed journal.

36. (carpanini2014anovelmouse pages 2-3): Sarah M. Carpanini, Lisa McKie, Derek Thomson, Ann K. Wright, Sarah L. Gordon, Sarah L. Roche, Mark T. Handley, Harris Morrison, David Brownstein, Thomas M. Wishart, Michael A. Cousin, Thomas H. Gillingwater, Irene A. Aligianis, and Ian J. Jackson. A novel mouse model of warburg micro syndrome reveals roles for rab18 in eye development and organisation of the neuronal cytoskeleton. Disease Models & Mechanisms, 7:711-722, Apr 2014. URL: https://doi.org/10.1242/dmm.015222, doi:10.1242/dmm.015222. This article has 48 citations and is from a domain leading peer-reviewed journal.

37. (malis2024rab1bfacilitateslipid pages 1-2): Yehonathan Malis, Shir Armoza-Eilat, Inbar Nevo-Yassaf, Anna Dukhovny, Ella H. Sklan, and Koret Hirschberg. Rab1b facilitates lipid droplet growth by er–to–lipid droplet targeting of dgat2. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.ade7753, doi:10.1126/sciadv.ade7753. This article has 14 citations and is from a highest quality peer-reviewed journal.

38. (pickerminh2014largehomozygousrab3gap1 media f5f15d26): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

39. (pickerminh2014largehomozygousrab3gap1 media 30474c79): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

40. (pickerminh2014largehomozygousrab3gap1 media cfa8e10c): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.

41. (pickerminh2014largehomozygousrab3gap1 media e76762b9): Sylvie Picker-Minh, Andreas Busche, Britta Hartmann, Birgit Spors, Eva Klopocki, Christoph Hübner, Denise Horn, and Angela M Kaindl. Large homozygous rab3gap1 gene microdeletion causes warburg micro syndrome 1. Orphanet Journal of Rare Diseases, Oct 2014. URL: https://doi.org/10.1186/s13023-014-0113-9, doi:10.1186/s13023-014-0113-9. This article has 8 citations and is from a peer-reviewed journal.