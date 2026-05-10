---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T06:08:19.548479'
end_time: '2026-05-10T06:25:31.387682'
duration_seconds: 1031.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Narcolepsy
  mondo_id: ''
  category: Neurological
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Narcolepsy
- **MONDO ID:**  (if available)
- **Category:** Neurological

## Research Objectives

Please provide a comprehensive research report on **Narcolepsy** covering all of the
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
- **Disease Name:** Narcolepsy
- **MONDO ID:**  (if available)
- **Category:** Neurological

## Research Objectives

Please provide a comprehensive research report on **Narcolepsy** covering all of the
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


# Narcolepsy (Neurological) — Disease Characteristics Research Report

## Target disease
Narcolepsy is a chronic central disorder of hypersomnolence characterized by excessive daytime sleepiness (EDS) with rapid-eye-movement (REM) sleep dysregulation, and is currently classified into **narcolepsy type 1 (NT1)** and **narcolepsy type 2 (NT2)**. NT1 is strongly linked to **orexin/hypocretin deficiency** and commonly includes **cataplexy**; NT2 lacks cataplexy and typically does not show orexin deficiency, with etiology less well established. (biscarini2025narcolepsyandrapid pages 1-2, xu2025acomprehensivereview pages 1-2)

### Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The retrieved full texts did **not** contain authoritative identifier mappings (ICD-10/ICD-11, MeSH, OMIM, Orphanet, MONDO). Therefore, these identifiers cannot be populated from the current evidence set and should be curated from dedicated terminologies (e.g., ICD/MeSH/MONDO/Orphanet) outside this tool run.

### Common synonyms/alternate names
* Narcolepsy with cataplexy (historical; largely aligns with NT1) (ariascarrion2026narcolepsyasan pages 3-4)
* Narcolepsy without cataplexy (historical; overlaps NT2 and “borderland” phenotypes) (ariascarrion2026narcolepsyasan pages 3-4)
* Hypocretin/orexin-deficient narcolepsy (NT1 phenotype emphasis) (xu2025acomprehensivereview pages 1-2, mignot2002theroleof pages 5-6)

### Source type note
This report integrates **aggregated disease-level resources** (reviews, cohorts, pharmacovigilance databases) and some **patient-level** evidence (e.g., clinical diagnostic criteria tables compiled in reviews). (baldini2024pediatricnarcolepsytype pages 1-2, zhou2024evaluationofpitolisant pages 1-2)

## 1. Disease information (current understanding)
Narcolepsy is now commonly conceptualized as a disorder of sleep–wake and REM-state boundary control. A modern “systems” view emphasizes multisystem consequences of hypothalamic orexin dysfunction rather than only the classic symptom pentad. (ariascarrion2026narcolepsyasan pages 2-3)

**Direct abstract-supported definition/overview:** A review of REM sleep and narcolepsy summarizes that narcolepsy is divided into NT1 and NT2, with key criteria relying on SOREMPs captured on polysomnography (PSG) and the Multiple Sleep Latency Test (MSLT), and that NT1 mechanisms are partly elucidated through **HLA association** and **orexin/hypocretin deficiency**. (biscarini2025narcolepsyandrapid pages 1-2)

## 2. Etiology

### 2.1 Primary causal factors

#### NT1: orexin neuron loss with strong immune association
NT1 is linked to selective loss/dysfunction of hypothalamic orexin-producing neurons and is increasingly supported as an immune-mediated disease in genetically predisposed individuals. (xu2025acomprehensivereview pages 1-2, ariascarrion2026narcolepsyasan pages 5-6)

A narrative review of T-cell involvement states that NT1 can be understood via interplay of **genetic predisposition (notably HLA-DQB1*06:02)**, environmental triggers (e.g., H1N1 infection/vaccination), and immune mechanisms leading to hypocretin neuronal loss. (xu2024theroleof pages 1-2)

#### NT2: heterogeneous/less defined
NT2 typically lacks cataplexy and orexin deficiency; its causes remain less well defined. However, subgroups with intermediate orexin levels may overlap immunogenetically with NT1. (biscarini2025narcolepsyandrapid pages 1-2, hamdan2024high‐resolutionhlasequencing pages 1-2, hamdan2024high‐resolutionhlasequencing pages 3-3)

### 2.2 Risk factors

#### Genetic risk factors
* **HLA-DQB1*06:02 / extended haplotypes**: In a Swedish cohort, NT1 showed strong association with DRB5*01:01:01–DRB1*15:01:01–DQA1*01:02:01–DQB1*06:02:01 (OR 7.01, 95% CI 3.97–12.37) and additional genotype combinations reaching OR 23.61 (95% CI 4.48–110.76). (hamdan2024high‐resolutionhlasequencing pages 4-5)
* **HLA frequency enrichment**: A 2024 review notes DQB1*06:02 is present in ~98% of NT1 with cataplexy vs ~25% of the general population, and that homozygosity increases risk vs heterozygosity. (xu2024theroleof pages 2-3)
* **Non-HLA immune loci**: Reported susceptibility loci include TRA (T-cell receptor alpha locus), CTSH, PPAN, P2RY11, IL10RB, and CPT1B, consistent with immune and T-cell biology. (xu2024theroleof pages 3-5, xu2024theroleof pages 2-3)

#### Environmental/infectious and vaccine-associated risk factors
* **Influenza A/H1N1 infection and AS03-adjuvanted Pandemrix vaccination (2009–2010)** are repeatedly highlighted as environmental triggers linked to increased NT1 incidence in specific settings. (xu2024theroleof pages 1-2, xu2024theroleof pages 3-5, ariascarrion2026narcolepsyasan pages 5-6)

### 2.3 Protective factors
The retrieved evidence did not provide clearly defined protective genetic variants or modifiable environmental protective factors for narcolepsy in a way that can be summarized with specificity.

### 2.4 Gene–environment interaction (G×E)
The most consistent G×E framework in the retrieved literature is **HLA-driven antigen presentation + environmental priming** (H1N1 infection/vaccination) leading to **T-cell activation** and ultimately selective injury of orexin neurons. (xu2024theroleof pages 1-2, xu2024theroleof pages 7-8, ariascarrion2026narcolepsyasan pages 5-6)

## 3. Phenotypes (clinical features)

### 3.1 Core phenotypes (symptoms/signs)
**Classic symptom cluster** often includes EDS, cataplexy (NT1), disrupted nighttime sleep, sleep paralysis, and hypnagogic/hypnopompic hallucinations. Pediatric NT1 reviews explicitly enumerate these as core symptoms. (baldini2024pediatricnarcolepsytype pages 1-2, baldini2024pediatricnarcolepsytype pages 2-4)

**Pediatric-specific presentation nuances**
* EDS may be “masked” by hyperactivity/irritability and may be misdiagnosed as ADHD. (baldini2024pediatricnarcolepsytype pages 2-4)
* Cataplexy in children may have atypical semiology (“cataplectic facies” with facial hypotonia/ptosis and mixed hyperactive movements). (baldini2024pediatricnarcolepsytype pages 2-4)

### 3.2 Frequency, onset, progression (where available)
* **Disturbed nighttime sleep (DNS) frequency in pediatric NT1**: 53–78%. (baldini2024pediatricnarcolepsytype pages 2-4)
* **RBD in young patients with NT1**: NT1 reported as leading cause of RBD in young patients (up to 60%). (baldini2024pediatricnarcolepsytype pages 2-4)
* **Diagnostic/phenotype proportions in a spectrum framing**: A review proposes proportions such as “typical cataplexy and all biological markers” 50–80%, with additional borderland groups. (ariascarrion2026narcolepsyasan pages 2-3)

### 3.3 Quality-of-life impact
A pediatric state-of-the-art review emphasizes that NT1 impairs children’s quality of life and supports early diagnosis and multidisciplinary management, including behavioral and psychosocial interventions. (baldini2024pediatricnarcolepsytype pages 1-2)

### 3.4 Suggested HPO terms (non-exhaustive, mapping suggestions)
The retrieved sources support the following phenotype constructs; HPO codes should be verified in an ontology browser:
* Excessive daytime sleepiness (EDS) (baldini2024pediatricnarcolepsytype pages 2-4)
* Cataplexy (baldini2024pediatricnarcolepsytype pages 2-4)
* Sleep paralysis (baldini2024pediatricnarcolepsytype pages 1-2)
* Hypnagogic/hypnopompic hallucinations (baldini2024pediatricnarcolepsytype pages 1-2)
* Fragmented sleep / disturbed nighttime sleep (baldini2024pediatricnarcolepsytype pages 2-4)
* REM sleep behavior disorder (baldini2024pediatricnarcolepsytype pages 2-4)
* Rapid weight gain/obesity (pediatric onset-associated) (biscarini2025narcolepsyandrapid pages 5-6)
* Precocious puberty (pediatric onset-associated) (biscarini2025narcolepsyandrapid pages 5-6)

## 4. Genetic / molecular information

### 4.1 Causal genes
For idiopathic NT1, the dominant genetic signal is polygenic (not a single Mendelian “causal gene”). However, a REM-sleep/narcolepsy review notes that a **canine model** identified mutations in the **orexin receptor 2** pathway (historically important to orexin biology). (biscarini2025narcolepsyandrapid pages 1-2)

### 4.2 Susceptibility loci (selected)
* HLA class II region including DQB1*06:02 and extended haplotypes (hamdan2024high‐resolutionhlasequencing pages 4-5, xu2024theroleof pages 2-3)
* TRA locus (TCR alpha chain) (xu2024theroleof pages 2-3)
* Additional loci reported in a 2024 T-cell narrative review: CTSH rs34593439, PPAN rs1551570, P2RY11 rs2305795, IL10RB rs2834188, CPT1B rs5770917 (xu2024theroleof pages 3-5)

### 4.3 Biomarkers

#### CSF hypocretin-1 (orexin-A)
A landmark diagnostic study defined **CSF hypocretin-1 ≤110 pg/mL** as a best-performing diagnostic cutoff (with >200 pg/mL considered normal), and in “typical cataplexy” reported **sensitivity 87% and specificity 99%**. (mignot2002theroleof pages 5-6, mignot2002theroleof pages 8-9)

#### Autoantibodies
A 2024 high-resolution HLA/autoantibody study found **no difference** in anti-HCRTR2 autoantibody levels across NT1, NT2, idiopathic hypersomnia, and general population controls (p=.8524), suggesting hypocretin receptor 2 is unlikely to be a major autoimmune target in these cohorts. (hamdan2024high‐resolutionhlasequencing pages 1-2, hamdan2024high‐resolutionhlasequencing pages 6-6)

### 4.4 Epigenetics / omics
The retrieved evidence notes that epigenetic alterations have been reported (e.g., within immune loci), but does not provide specific methylation loci or standardized effect sizes in the excerpts available here. (xu2024theroleof pages 14-15, ariascarrion2026narcolepsyasan pages 7-8)

## 5. Mechanism / pathophysiology

### 5.1 Causal chain (NT1; synthesis)
1) **Genetic susceptibility**: strong HLA class II association (e.g., DQB1*06:02) and additional immune/TCR loci (xu2024theroleof pages 2-3, hamdan2024high‐resolutionhlasequencing pages 4-5)
2) **Environmental priming**: H1N1 influenza infection and/or Pandemrix vaccination in specific outbreaks (xu2024theroleof pages 1-2, xu2024theroleof pages 3-5)
3) **Immune activation and autoimmunity**: evidence supports autoreactive CD4+ and CD8+ T cells targeting orexin-related antigens; molecular mimicry is plausible but not fully resolved across studies (xu2024theroleof pages 7-8, ariascarrion2026narcolepsyasan pages 5-6)
4) **Selective orexin neuron loss/dysfunction**: substantial neuron loss has been estimated (75–95% loss in NT1 described in a systems review) (ariascarrion2026narcolepsyasan pages 5-6)
5) **Network-level consequences**: destabilized wake maintenance and REM boundary control producing EDS, SOREMPs, cataplexy, hallucinations, and sleep paralysis (xu2025acomprehensivereview pages 9-11, biscarini2025narcolepsyandrapid pages 1-2)

### 5.2 Cell types (CL suggestions) and biological processes (GO suggestions)
Evidence supports immune effector involvement and hypothalamic neuron injury:
* **CL terms (suggested)**: CD4-positive T cell; CD8-positive T cell; hypothalamic orexin neuron; histaminergic neuron (TMN) (TAK-861 depolarizes TMN histaminergic neurons via OX2R) (xu2024theroleof pages 7-8, mitsukawa2024tak861apotent pages 2-3)
* **GO biological processes (suggested)**: antigen processing and presentation (MHC class II); T cell activation; IFN-γ–mediated signaling and MHC I upregulation; regulation of sleep–wake cycle; regulation of REM sleep (xu2024theroleof pages 7-8, biscarini2025narcolepsyandrapid pages 1-2)

### 5.3 Anatomical localization (UBERON suggestions)
* Lateral hypothalamic area (orexin neuron field) (ariascarrion2026narcolepsyasan pages 3-4)
* Hypothalamus (disease framing as hypothalamic encephalopathy) (ariascarrion2026narcolepsyasan pages 2-3)

## 6. Epidemiology, inheritance, and population

### 6.1 Prevalence/incidence (selected values present in retrieved sources)
* A treatment review describes NT1 prevalence as approximately **~1 in 2000**. (xu2025acomprehensivereview pages 1-2)
* A systems review summarizes examples of claims/survey-based estimates (not a primary epidemiology study): U.S. prevalence **37.7/100,000** and incidence **2.6/100,000 person-years**; Japan claims prevalence **~37.5/100,000** and incidence **5.1/100,000 person-years**, with substantial geographic variation and diagnostic uncertainty (notably for NT2). (ariascarrion2026narcolepsyasan pages 3-4)

### 6.2 Inheritance pattern
The evidence supports narcolepsy (especially NT1) as **multifactorial/polygenic** with strong HLA association rather than Mendelian inheritance. (xu2024theroleof pages 2-3, xu2024theroleof pages 3-5)

### 6.3 Demographics and heterogeneity
Pediatric narcolepsy is emphasized as frequently beginning in childhood/adolescence, and pediatric phenotype has distinctive features (e.g., weight gain and atypical cataplexy semiology). (biscarini2025narcolepsyandrapid pages 5-6, baldini2024pediatricnarcolepsytype pages 2-4)

## 7. Diagnostics

### 7.1 Standard diagnostic criteria (ICSD-3-TR, 2023)
The pediatric NT1 review reproduces **ICSD-3-TR (2023) diagnostic criteria** for NT1 and NT2, including EDS duration, MSLT requirements (mean sleep latency ≤8 min and ≥2 SOREMPs), cataplexy status, and CSF hypocretin thresholds, and illustrates the ICSD-3-TR change that allows **nocturnal PSG SOREMP + cataplexy** to suffice for NT1 diagnosis even if MSLT is not definitive. (baldini2024pediatricnarcolepsytype media 3ad4bd72, baldini2024pediatricnarcolepsytype pages 8-9)

### 7.2 Core tests
* Overnight PSG + MSLT remain key objective tests, anchored on SOREMP detection. (biscarini2025narcolepsyandrapid pages 1-2)
* **CSF hypocretin-1** is described as the strongest biomarker in reviews and has robust test characteristics in foundational work. (ariascarrion2026narcolepsyasan pages 21-22, mignot2002theroleof pages 5-6)

### 7.3 Test performance and pediatric considerations
* **Nocturnal SOREMP** in pediatrics: reported specificity 97.3% and sensitivity 54.8% (reviewed pediatric data). (baldini2024pediatricnarcolepsytype pages 8-9)
* **CSF hypocretin**: ≤110 pg/mL cutoff with high specificity and good sensitivity for typical cataplexy. (mignot2002theroleof pages 5-6, mignot2002theroleof pages 8-9)

### 7.4 Differential diagnosis highlights (from pediatric review excerpts)
Diagnostic workup emphasizes excluding insufficient sleep and circadian disorders (actigraphy 7–10 days), and distinguishing NT2 from idiopathic hypersomnia (IH) via SOREMP patterns and/or total sleep time. (baldini2024pediatricnarcolepsytype pages 9-11)

## 8. Treatment (current applications and real-world implementation)

### 8.1 Symptomatic pharmacotherapy (current standard)
A synthesis review rates modafinil/armodafinil, solriamfetol, pitolisant, and sodium oxybate formulations as high-certainty, strong-recommendation symptomatic treatments. (ariascarrion2026narcolepsyasan pages 21-22)

**Pediatric regulatory status and practice**
A pediatric NT1 review notes:
* No approvals under age 6.
* Sodium oxybate is approved by **FDA and EMA for ages ≥7**.
* EMA approved **pitolisant in 2023** for patients >6 years with or without cataplexy. (baldini2024pediatricnarcolepsytype pages 11-13)

### 8.2 Oxybate dosing innovations (real-world implementation)
RESTORE (2024) evaluated switching from twice-nightly immediate-release oxybate to once-nightly extended-release sodium oxybate:
* **93.9%** (92/98) preferred once-nightly dosing.
* Prior to switching, **69.2%** had missed the second dose at least once; nocturnal mobility after the second dose was common, with reported falls and injuries.
* After switching, **91.2%** felt better able to follow the recommended dosing schedule.
These data emphasize adherence/safety burdens of middle-of-the-night redosing and a real-world rationale for simplified regimens. (roy2024restoreoncenightlyoxybate pages 1-2, roy2024restoreoncenightlyoxybate pages 2-3)

### 8.3 Mechanism-based “orexin restoration” therapeutics (recent developments)
A major 2023–2024 development area is **small-molecule OX2R agonists** designed to replace deficient orexin signaling.

**Preclinical evidence (2024): TAK-861 (oveporexton)**
A 2024 Scientific Reports study characterized TAK-861 as an oral OX2R-selective agonist with **OX2R EC50 2.5 nM** and ~3,000-fold selectivity over OX1R. It promoted wakefulness in mice and monkeys (minimum effective dose 1 mg/kg) and improved narcolepsy-like phenotypes in NT1 mouse models (orexin/ataxin-3 and orexin-tTA;TetO DTA), including reduced wake fragmentation and reduced cataplexy-like episodes. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 3-4, mitsukawa2024tak861apotent pages 2-3, mitsukawa2024tak861apotent pages 10-11)

**Clinical development (trial registry; real-world implementation horizon)**
Multiple trials are registered for orexin agonists including TAK-861 and danavorexton (TAK-925). Examples include completed and recruiting studies spanning Phase 1–3 (e.g., NCT05687903 Phase 2; Phase 3 trials listed for TAK-861; TAK-925 Phase 1 programs). (xu2025acomprehensivereview pages 9-11)

### 8.4 Safety signals and pharmacovigilance (recent data)
A 2024 FAERS analysis (2019–2023) identified signal counts: 50 signals/762 cases for pitolisant, 640/46,962 for sodium oxybate, 40/1,228 for solriamfetol, and 72/632 for modafinil. Psychiatric and nervous system disorders predominated; sodium oxybate showed strong respiratory-related signals (e.g., sleep apnea syndrome n=1326 with high disproportionality metrics) and hypertension signals. These are **signal-detection outputs** without denominators and cannot be interpreted as incidence rates, but they inform monitoring priorities. (zhou2024evaluationofpitolisant pages 1-2, zhou2024evaluationofpitolisant pages 8-9)

### 8.5 Suggested MAXO terms (treatment action ontology; mapping suggestions)
Based on interventions discussed:
* Pharmacotherapy for hypersomnolence / wake promotion (modafinil/armodafinil/solriamfetol/pitolisant) (ariascarrion2026narcolepsyasan pages 21-22)
* Oxybate therapy (sodium oxybate; low-sodium oxybate; once-nightly formulations) (roy2024restoreoncenightlyoxybate pages 1-2, baldini2024pediatricnarcolepsytype pages 11-13)
* Orexin receptor agonist therapy (OX2R agonists) (mitsukawa2024tak861apotent pages 1-2)
* Behavioral sleep intervention (planned naps, sleep hygiene, school programs) (baldini2024pediatricnarcolepsytype pages 1-2, baldini2024pediatricnarcolepsytype pages 11-13)

## 9. Prevention

### 9.1 Primary prevention
No established primary prevention strategy exists for idiopathic NT1/NT2.

### 9.2 Secondary/tertiary prevention (complication reduction)
Evidence supports **early diagnosis** and multidisciplinary management in pediatrics to reduce educational/psychosocial impact, plus careful monitoring for comorbidities (metabolic/endocrine, psychiatric) and medication adverse effects. (baldini2024pediatricnarcolepsytype pages 1-2, baldini2024pediatricnarcolepsytype pages 14-15)

### 9.3 Vaccine-related considerations
Pandemrix-associated risk signals are part of the etiologic history in some countries, but causality and generalization to modern vaccines are complex; a recent immunology-focused narrative emphasizes that mechanistic mimicry is plausible but incompletely resolved and that findings vary across studies. (xu2024theroleof pages 7-8, ariascarrion2026narcolepsyasan pages 5-6)

## 10. Other species / natural disease and model organisms

### 10.1 Model organisms used in current research
The orexin system has strong translational animal models. A 2024 preclinical therapeutic paper uses:
* **orexin/ataxin-3 mice** (orexin neuron degeneration model)
* **orexin-tTA;TetO DTA mice** (conditional orexin neuron ablation)
These models support evaluation of orexin-pathway therapeutics for wake consolidation and cataplexy-like behaviors. (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 10-11)

### 10.2 Model limitations
The retrieved evidence emphasizes that models typically capture fragments of the human phenotype (e.g., cataplexy-like episodes, fragmentation) and are most directly aligned with NT1 biology rather than NT2 heterogeneity. (mitsukawa2024tak861apotent pages 1-2, biscarini2025narcolepsyandrapid pages 1-2)

## 11. Key recent evidence summary table
The following table consolidates the most actionable recent and foundational evidence captured in this tool run.

| Topic | Key data/statistics | Source (first author, year, journal) | URL | Notes |
|---|---|---|---|---|
| ICSD-3-TR diagnostic criteria | 2023 ICSD-3-TR allows NT1 diagnosis when cataplexy is present together with a nocturnal PSG SOREMP, even without relying on MSLT/hypocretin confirmation; standard criteria still include mean sleep latency ≤8 min and ≥2 SOREMPs, or CSF hypocretin-1 ≤110 pg/mL / <1/3 of controls (baldini2024pediatricnarcolepsytype pages 8-9, baldini2024pediatricnarcolepsytype pages 1-2, baldini2024pediatricnarcolepsytype media 3ad4bd72) | Baldini, 2024, Clinical and Translational Neuroscience | https://doi.org/10.3390/ctn8030025 | Useful update for diagnostic workflows, especially pediatrics and difficult MSLT cases |
| Pediatric phenotypes | Disturbed nighttime sleep (DNS) affects 53–78% of pediatric NT1; REM sleep behavior disorder (RBD) is reported in up to 60% and may be early/severe in children (baldini2024pediatricnarcolepsytype pages 2-4) | Baldini, 2024, Clinical and Translational Neuroscience | https://doi.org/10.3390/ctn8030025 | Pediatric presentation can include atypical cataplexy and ADHD-like behaviors |
| CSF hypocretin biomarker | CSF hypocretin-1 cutoff ≤110 pg/mL (with >200 pg/mL considered normal); in typical cataplexy, sensitivity 87% and specificity 99%, PPV 96%, NPV 96% (mignot2002theroleof pages 5-6, mignot2002theroleof pages 8-9) | Mignot, 2002, Archives of Neurology | https://doi.org/10.1001/archneur.59.10.1553 | Strongest biomarker for NT1; interpretation needed in secondary hypothalamic disease |
| HLA associations | NT1-associated haplotype DRB5*01:01:01-DRB1*15:01:01-DQA1*01:02:01-DQB1*06:02:01: OR 7.01 (95% CI 3.97–12.37); genotype OR 9.15. Multilocus genotype including DRB4*01:03:01/DRB1*04:01:01/DQA1*03:02 or *03:03:01/DQB1*03:01:01: OR 23.61 (95% CI 4.48–110.76). Anti-HCRTR2 autoantibodies were not different across groups (p=.8524) (hamdan2024high‐resolutionhlasequencing pages 4-5, hamdan2024high‐resolutionhlasequencing pages 1-2, hamdan2024high‐resolutionhlasequencing pages 6-6) | Hamdan, 2024, International Journal of Immunogenetics | https://doi.org/10.1111/iji.12688 | Supports strong HLA-driven susceptibility; no support here for HCRTR2 autoantibody pathogenicity |
| T-cell autoimmunity and risk loci | NT1 is framed as predominantly T-cell–mediated autoimmunity; HLA-DQB1*06:02 present in ~98% of NT1 with cataplexy vs ~25% of general population; reported risk loci include TRA, CTSH rs34593439, PPAN rs1551570, P2RY11 rs2305795, IL10RB/rs2834188, CPT1B rs5770917; H1N1/Pandemrix implicated as environmental triggers (xu2024theroleof pages 2-3, xu2024theroleof pages 3-5, xu2024theroleof pages 7-8, xu2024theroleof pages 1-2) | Xu, 2024, International Journal of Molecular Sciences | https://doi.org/10.3390/ijms252211914 | Molecular mimicry is plausible but incompletely resolved |
| TAK-861 preclinical evidence | TAK-861 (oveporexton) activated OX2R with EC50 2.5 nM and ~3,000-fold selectivity over OX1R; improved wakefulness and reduced cataplexy-like episodes in orexin/ataxin-3 and orexin-tTA;TetO DTA mouse models; wake-promoting MED 1 mg/kg in mice and monkeys (mitsukawa2024tak861apotent pages 1-2, mitsukawa2024tak861apotent pages 3-4, mitsukawa2024tak861apotent pages 2-3, mitsukawa2024tak861apotent pages 10-11) | Mitsukawa, 2024, Scientific Reports | https://doi.org/10.1038/s41598-024-70594-1 | Mechanism-based therapy aimed at replacing lost orexin signaling |
| Oveporexton phase 2 outcomes | In NT1, 8-week trial: mean MWT change +12.5 to +25.4 min vs -1.2 placebo; ESS change -8.9 to -13.8 vs -2.5 placebo; weekly cataplexy at week 8: 2.48–5.89 vs 8.76 placebo depending on dose; common AEs insomnia 48%, urinary urgency 33%, urinary frequency 32%; no hepatotoxicity reported (abstract evidence from retrieved paper search) | Dauvilliers, 2025, New England Journal of Medicine | https://doi.org/10.1056/NEJMoa2405847 | Phase 2 TAK-861/oveporexton trial, NCT05687903 |
| Once-nightly oxybate preference | In RESTORE, 92/98 (93.9%) preferred once-nightly sodium oxybate after switching; 69.2% had missed the second IR oxybate dose at least once; 91.2% felt better able to follow dosing schedule; 92.6% would recommend ON-SXB (roy2024restoreoncenightlyoxybate pages 1-2, roy2024restoreoncenightlyoxybate pages 2-3, roy2024restoreoncenightlyoxybate pages 4-5) | Roy, 2024, Sleep Medicine: X | https://doi.org/10.1016/j.sleepx.2024.100122 | Highlights real-world burden of middle-of-the-night redosing |
| Real-world pharmacovigilance | FAERS 2019–2023 identified 50 signals/762 cases for pitolisant, 640/46,962 for sodium oxybate, 40/1,228 for solriamfetol, and 72/632 for modafinil; psychiatric and nervous system ADEs predominated. Sodium oxybate had notable signals for sleep apnea syndrome (n=1326), respiratory depression (n=104), apnea (n=95), and hypertension (n=1081) (zhou2024evaluationofpitolisant pages 1-2, zhou2024evaluationofpitolisant pages 3-4, zhou2024evaluationofpitolisant pages 8-9) | Zhou, 2024, Frontiers in Pharmacology | https://doi.org/10.3389/fphar.2024.1415918 | FAERS signals are hypothesis-generating, not incidence estimates |
| Epidemiology snapshot | Recent review summarized prevalence around 37.7/100,000 in the U.S. and incidence ~2.6/100,000 person-years; Japan claims data ~37.5/100,000 prevalence and 5.1/100,000 person-years incidence, with strong geographic variability (ariascarrion2026narcolepsyasan pages 3-4) | Arias-Carrión, 2026, Frontiers in Psychiatry | https://doi.org/10.3389/fpsyt.2026.1799520 | Useful contextual benchmark; not a primary epidemiology study |


*Table: This table compiles high-yield recent and foundational evidence for narcolepsy across diagnosis, biomarkers, immunogenetics, therapeutics, and real-world safety. It is useful as a quick-reference summary for a disease knowledge base entry.*

## 12. Notes on evidence gaps and curation requirements
* **Disease identifiers (ICD/MeSH/MONDO/OMIM/Orphanet)**: not present in the retrieved literature excerpts; must be curated separately.
* **NT2 biology and biomarkers**: evidence in this run supports heterogeneity and possible overlap subgroups (intermediate orexin), but a definitive mechanism is not established here. (hamdan2024high‐resolutionhlasequencing pages 3-3, hamdan2024high‐resolutionhlasequencing pages 1-2)
* **Autoantibodies**: HCRTR2 autoantibodies were not supported as disease-specific in the 2024 cohort study. (hamdan2024high‐resolutionhlasequencing pages 6-6)

## References (URLs and publication dates)
Primary sources used (examples; see citations inline):
* Baldini V. et al. Pediatric Narcolepsy Type 1: A State-of-the-Art Review. *Clinical and Translational Neuroscience*. 2024-06. https://doi.org/10.3390/ctn8030025 (baldini2024pediatricnarcolepsytype pages 1-2)
* Xu W. et al. The Role of T Cells in the Pathogenesis of Narcolepsy Type 1. *Int J Mol Sci*. 2024-11. https://doi.org/10.3390/ijms252211914 (xu2024theroleof pages 1-2)
* Hamdan S. et al. High-resolution HLA sequencing and hypocretin receptor 2 autoantibodies. *Int J Immunogenet*. 2024-06. https://doi.org/10.1111/iji.12688 (hamdan2024high‐resolutionhlasequencing pages 1-2)
* Mitsukawa K. et al. TAK-861 OX2R agonist preclinical study. *Scientific Reports*. 2024-09. https://doi.org/10.1038/s41598-024-70594-1 (mitsukawa2024tak861apotent pages 1-2)
* Roy A. et al. RESTORE once-nightly oxybate preference. *Sleep Medicine: X*. 2024-12. https://doi.org/10.1016/j.sleepx.2024.100122 (roy2024restoreoncenightlyoxybate pages 1-2)
* Zhou X. et al. FAERS pharmacovigilance analysis. *Front Pharmacol*. 2024-11. https://doi.org/10.3389/fphar.2024.1415918 (zhou2024evaluationofpitolisant pages 1-2)
* Mignot E. et al. CSF hypocretin measurement diagnostic performance. *Archives of Neurology*. 2002-10. https://doi.org/10.1001/archneur.59.10.1553 (mignot2002theroleof pages 5-6)


References

1. (biscarini2025narcolepsyandrapid pages 1-2): Francesco Biscarini, Lucie Barateau, Fabio Pizza, Giuseppe Plazzi, and Yves Dauvilliers. Narcolepsy and rapid eye movement sleep. Journal of Sleep Research, Jul 2025. URL: https://doi.org/10.1111/jsr.14277, doi:10.1111/jsr.14277. This article has 14 citations and is from a peer-reviewed journal.

2. (xu2025acomprehensivereview pages 1-2): Qinglin Xu, Yigang Chen, Tiantian Wang, Qiongbin Zhu, Jiahui Xu, and Lisan Zhang. A comprehensive review of current and emerging treatments for narcolepsy type 1. Journal of Clinical Medicine, 14:8444, Nov 2025. URL: https://doi.org/10.3390/jcm14238444, doi:10.3390/jcm14238444. This article has 1 citations.

3. (ariascarrion2026narcolepsyasan pages 3-4): Oscar Arias-Carrión, Emmanuel Ortega-Robles, Patricia Romano, and Carlos Pineda. Narcolepsy as an immune-associated hypothalamic encephalopathy: orexin dysfunction and implications for precision sleep medicine. Frontiers in Psychiatry, Apr 2026. URL: https://doi.org/10.3389/fpsyt.2026.1799520, doi:10.3389/fpsyt.2026.1799520. This article has 0 citations.

4. (mignot2002theroleof pages 5-6): Emmanuel Mignot, Gert Jan Lammers, Beth Ripley, Michele Okun, Sonia Nevsimalova, Sebastiaan Overeem, Jitka Vankova, Jed Black, John Harsh, Claudio Bassetti, Harald Schrader, and Seiji Nishino. The role of cerebrospinal fluid hypocretin measurement in the diagnosis of narcolepsy and other hypersomnias. Archives of neurology, 59 10:1553-62, Oct 2002. URL: https://doi.org/10.1001/archneur.59.10.1553, doi:10.1001/archneur.59.10.1553. This article has 1400 citations.

5. (baldini2024pediatricnarcolepsytype pages 1-2): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

6. (zhou2024evaluationofpitolisant pages 1-2): Xiaodan Zhou, Jia Chen, Bangtian Xu, and Li Chen. Evaluation of pitolisant, sodium oxybate, solriamfetol, and modafinil for the management of narcolepsy: a retrospective analysis of the faers database. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1415918, doi:10.3389/fphar.2024.1415918. This article has 4 citations.

7. (ariascarrion2026narcolepsyasan pages 2-3): Oscar Arias-Carrión, Emmanuel Ortega-Robles, Patricia Romano, and Carlos Pineda. Narcolepsy as an immune-associated hypothalamic encephalopathy: orexin dysfunction and implications for precision sleep medicine. Frontiers in Psychiatry, Apr 2026. URL: https://doi.org/10.3389/fpsyt.2026.1799520, doi:10.3389/fpsyt.2026.1799520. This article has 0 citations.

8. (ariascarrion2026narcolepsyasan pages 5-6): Oscar Arias-Carrión, Emmanuel Ortega-Robles, Patricia Romano, and Carlos Pineda. Narcolepsy as an immune-associated hypothalamic encephalopathy: orexin dysfunction and implications for precision sleep medicine. Frontiers in Psychiatry, Apr 2026. URL: https://doi.org/10.3389/fpsyt.2026.1799520, doi:10.3389/fpsyt.2026.1799520. This article has 0 citations.

9. (xu2024theroleof pages 1-2): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

10. (hamdan2024high‐resolutionhlasequencing pages 1-2): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

11. (hamdan2024high‐resolutionhlasequencing pages 3-3): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

12. (hamdan2024high‐resolutionhlasequencing pages 4-5): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

13. (xu2024theroleof pages 2-3): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

14. (xu2024theroleof pages 3-5): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

15. (xu2024theroleof pages 7-8): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

16. (baldini2024pediatricnarcolepsytype pages 2-4): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

17. (biscarini2025narcolepsyandrapid pages 5-6): Francesco Biscarini, Lucie Barateau, Fabio Pizza, Giuseppe Plazzi, and Yves Dauvilliers. Narcolepsy and rapid eye movement sleep. Journal of Sleep Research, Jul 2025. URL: https://doi.org/10.1111/jsr.14277, doi:10.1111/jsr.14277. This article has 14 citations and is from a peer-reviewed journal.

18. (mignot2002theroleof pages 8-9): Emmanuel Mignot, Gert Jan Lammers, Beth Ripley, Michele Okun, Sonia Nevsimalova, Sebastiaan Overeem, Jitka Vankova, Jed Black, John Harsh, Claudio Bassetti, Harald Schrader, and Seiji Nishino. The role of cerebrospinal fluid hypocretin measurement in the diagnosis of narcolepsy and other hypersomnias. Archives of neurology, 59 10:1553-62, Oct 2002. URL: https://doi.org/10.1001/archneur.59.10.1553, doi:10.1001/archneur.59.10.1553. This article has 1400 citations.

19. (hamdan2024high‐resolutionhlasequencing pages 6-6): Samia Hamdan, Pontus Wasling, and Alexander Lind. High‐resolution hla sequencing and hypocretin receptor 2 autoantibodies in narcolepsy type 1 and type 2. International Journal of Immunogenetics, 51:310-318, Jun 2024. URL: https://doi.org/10.1111/iji.12688, doi:10.1111/iji.12688. This article has 1 citations and is from a peer-reviewed journal.

20. (xu2024theroleof pages 14-15): Wenqi Xu, Wenting Ding, Yu Zhang, Shuanshuan Wang, Xianyu Yan, Yirui Xu, Xiaoying Zhi, and Rongzeng Liu. The role of t cells in the pathogenesis of narcolepsy type 1: a narrative review. International Journal of Molecular Sciences, 25:11914, Nov 2024. URL: https://doi.org/10.3390/ijms252211914, doi:10.3390/ijms252211914. This article has 4 citations.

21. (ariascarrion2026narcolepsyasan pages 7-8): Oscar Arias-Carrión, Emmanuel Ortega-Robles, Patricia Romano, and Carlos Pineda. Narcolepsy as an immune-associated hypothalamic encephalopathy: orexin dysfunction and implications for precision sleep medicine. Frontiers in Psychiatry, Apr 2026. URL: https://doi.org/10.3389/fpsyt.2026.1799520, doi:10.3389/fpsyt.2026.1799520. This article has 0 citations.

22. (xu2025acomprehensivereview pages 9-11): Qinglin Xu, Yigang Chen, Tiantian Wang, Qiongbin Zhu, Jiahui Xu, and Lisan Zhang. A comprehensive review of current and emerging treatments for narcolepsy type 1. Journal of Clinical Medicine, 14:8444, Nov 2025. URL: https://doi.org/10.3390/jcm14238444, doi:10.3390/jcm14238444. This article has 1 citations.

23. (mitsukawa2024tak861apotent pages 2-3): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 21 citations and is from a peer-reviewed journal.

24. (baldini2024pediatricnarcolepsytype media 3ad4bd72): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

25. (baldini2024pediatricnarcolepsytype pages 8-9): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

26. (ariascarrion2026narcolepsyasan pages 21-22): Oscar Arias-Carrión, Emmanuel Ortega-Robles, Patricia Romano, and Carlos Pineda. Narcolepsy as an immune-associated hypothalamic encephalopathy: orexin dysfunction and implications for precision sleep medicine. Frontiers in Psychiatry, Apr 2026. URL: https://doi.org/10.3389/fpsyt.2026.1799520, doi:10.3389/fpsyt.2026.1799520. This article has 0 citations.

27. (baldini2024pediatricnarcolepsytype pages 9-11): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

28. (baldini2024pediatricnarcolepsytype pages 11-13): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

29. (roy2024restoreoncenightlyoxybate pages 1-2): Asim Roy, Thomas Stern, John Harsh, J. Douglas Hudson, Akinyemi O. Ajayi, Bruce C. Corser, Emmanuel Mignot, Adrian Santamaria, Anne Marie Morse, Brian Abaluck, Sally Ibrahim, Paula K. Schweitzer, Katie Lancaster, Jordan Dubow, and Jennifer Gudeman. Restore: once-nightly oxybate dosing preference and nocturnal experience with twice-nightly oxybates. Sleep Medicine: X, 8:100122, Dec 2024. URL: https://doi.org/10.1016/j.sleepx.2024.100122, doi:10.1016/j.sleepx.2024.100122. This article has 9 citations.

30. (roy2024restoreoncenightlyoxybate pages 2-3): Asim Roy, Thomas Stern, John Harsh, J. Douglas Hudson, Akinyemi O. Ajayi, Bruce C. Corser, Emmanuel Mignot, Adrian Santamaria, Anne Marie Morse, Brian Abaluck, Sally Ibrahim, Paula K. Schweitzer, Katie Lancaster, Jordan Dubow, and Jennifer Gudeman. Restore: once-nightly oxybate dosing preference and nocturnal experience with twice-nightly oxybates. Sleep Medicine: X, 8:100122, Dec 2024. URL: https://doi.org/10.1016/j.sleepx.2024.100122, doi:10.1016/j.sleepx.2024.100122. This article has 9 citations.

31. (mitsukawa2024tak861apotent pages 1-2): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 21 citations and is from a peer-reviewed journal.

32. (mitsukawa2024tak861apotent pages 3-4): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 21 citations and is from a peer-reviewed journal.

33. (mitsukawa2024tak861apotent pages 10-11): Kayo Mitsukawa, Michiko Terada, Ryuji Yamada, Taku Monjo, Tetsuaki Hiyoshi, Masanori Nakakariya, Yuichi Kajita, Tatsuya Ando, Tatsuki Koike, and Haruhide Kimura. Tak-861, a potent, orally available orexin receptor 2-selective agonist, produces wakefulness in monkeys and improves narcolepsy-like phenotypes in mouse models. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70594-1, doi:10.1038/s41598-024-70594-1. This article has 21 citations and is from a peer-reviewed journal.

34. (zhou2024evaluationofpitolisant pages 8-9): Xiaodan Zhou, Jia Chen, Bangtian Xu, and Li Chen. Evaluation of pitolisant, sodium oxybate, solriamfetol, and modafinil for the management of narcolepsy: a retrospective analysis of the faers database. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1415918, doi:10.3389/fphar.2024.1415918. This article has 4 citations.

35. (baldini2024pediatricnarcolepsytype pages 14-15): Valentina Baldini, Francesco Biscarini, Giorgia Varallo, Fabio Pizza, and Giuseppe Plazzi. Pediatric narcolepsy type 1: a state-of-the-art review. Clinical and Translational Neuroscience, 8:25, Jun 2024. URL: https://doi.org/10.3390/ctn8030025, doi:10.3390/ctn8030025. This article has 4 citations.

36. (roy2024restoreoncenightlyoxybate pages 4-5): Asim Roy, Thomas Stern, John Harsh, J. Douglas Hudson, Akinyemi O. Ajayi, Bruce C. Corser, Emmanuel Mignot, Adrian Santamaria, Anne Marie Morse, Brian Abaluck, Sally Ibrahim, Paula K. Schweitzer, Katie Lancaster, Jordan Dubow, and Jennifer Gudeman. Restore: once-nightly oxybate dosing preference and nocturnal experience with twice-nightly oxybates. Sleep Medicine: X, 8:100122, Dec 2024. URL: https://doi.org/10.1016/j.sleepx.2024.100122, doi:10.1016/j.sleepx.2024.100122. This article has 9 citations.

37. (zhou2024evaluationofpitolisant pages 3-4): Xiaodan Zhou, Jia Chen, Bangtian Xu, and Li Chen. Evaluation of pitolisant, sodium oxybate, solriamfetol, and modafinil for the management of narcolepsy: a retrospective analysis of the faers database. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1415918, doi:10.3389/fphar.2024.1415918. This article has 4 citations.
