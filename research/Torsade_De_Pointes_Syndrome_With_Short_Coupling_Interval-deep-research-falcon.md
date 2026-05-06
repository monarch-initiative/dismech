---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T13:43:00.656427'
end_time: '2026-05-06T13:59:15.716076'
duration_seconds: 975.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Torsade de Pointes Syndrome With Short Coupling Interval
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Torsade de Pointes Syndrome With Short Coupling Interval
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Torsade de Pointes Syndrome With Short Coupling Interval** covering all of the
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
- **Disease Name:** Torsade de Pointes Syndrome With Short Coupling Interval
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Torsade de Pointes Syndrome With Short Coupling Interval** covering all of the
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


# Torsade de Pointes Syndrome With Short Coupling Interval (Short‑Coupled TdP / Short‑Coupled Ventricular Fibrillation) — Comprehensive Research Report

## Executive summary
Short‑coupled torsades de pointes (scTdP), also called the **short‑coupled variant of torsade de pointes** and often discussed today under **short‑coupled ventricular fibrillation (SCVF)** / **Purkinje‑triggered idiopathic ventricular fibrillation**, is a malignant ventricular tachyarrhythmia syndrome characterized by **polymorphic VT/TdP and/or VF initiated by an extremely short‑coupled PVC** (classically ~200–300 ms) in patients **without baseline QT prolongation** and typically without overt structural heart disease. It carries high risk of syncope, electrical storm, and sudden cardiac death; **ICD therapy is the only consistently supported sudden‑death preventive intervention**, while **verapamil** can suppress episodes but is not fully protective. Increasing evidence implicates **His‑Purkinje/right ventricular endocavitary triggers** (e.g., moderator band insertion) and heterogeneous genetic contributions including **RYR2**, **SCN5A**, and **Purkinje‑repolarization risk haplotypes (e.g., DPP6)**. (leenhardt1994shortcoupledvariantof pages 1-3, leenhardt1994shortcoupledvariantof pages 9-10, wang2022shortcoupledvariantof pages 1-2, steinfurt2022catheterablationof pages 1-3, steinfurt2022catheterablationof pages 3-7)

---

## 1. Disease information

### 1.1 Definition and current understanding
The original description (Leenhardt et al., **1994-01**, *Circulation*) observed 14 patients with syncope and a typical TdP ECG pattern **without long‑QT syndrome**, in whom TdP had “**the unusual particularity of an extremely short coupling interval of the first beat or of the isolated premature beats (245±28 milliseconds)**.” (leenhardt1994shortcoupledvariantof pages 1-3)

The diagnosis is now commonly framed as **TdP/VF initiated by a short‑coupled PVC on a normal QT background**, resembling an “R‑on‑T” phenomenon. A 2022 systematic review summarizes it as “**TdP/VF triggered by a short‑coupled premature ventricular complex (PVC) on a normal QT interval**.” (wang2022shortcoupledvariantof pages 1-2)

A 2024 TdP mechanistic update notes that although TdP classically refers to long‑QT polymorphic VT, the term has also been used for polymorphic arrhythmias **without QT prolongation**, including “**short‑coupled variant of TdP currently known as short‑coupled ventricular fibrillation**.” (tsuji2024mechanismsoftorsades pages 1-2)

### 1.2 Synonyms / alternative names
* Short‑coupled variant of torsade de pointes (SCV‑TdP) (leenhardt1994shortcoupledvariantof pages 1-3)
* Short‑coupled torsade de pointes (scTdP) (wang2022shortcoupledvariantof pages 1-2)
* Short‑coupled ventricular fibrillation (SCVF) / short‑coupled idiopathic VF phenotype (tsuji2024mechanismsoftorsades pages 1-2, NCT05593757 chunk 1)
* Purkinje‑triggered idiopathic ventricular fibrillation (conceptual phenotype) (wang2022shortcoupledvariantof pages 12-14, steinfurt2022catheterablationof pages 3-7)

### 1.3 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Within the **retrieved evidence set**, explicit cross‑references to **OMIM, Orphanet, ICD‑10/ICD‑11, MeSH, or MONDO** were **not present**, and an OpenTargets disease lookup for “short‑coupled torsades de pointes” did not resolve a disease ID during tool execution. Therefore, these identifiers cannot be provided from the current evidence corpus and would require targeted ontology/database queries beyond the retrieved texts. (wang2022shortcoupledvariantof pages 1-2)

### 1.4 Evidence source type
Most knowledge for this entity comes from **case series, systematic reviews of case reports/series, and small retrospective ablation cohorts**, rather than large prospective epidemiologic cohorts. (wang2022shortcoupledvariantof pages 1-2, steinfurt2022catheterablationof pages 1-3)

---

## 2. Etiology

### 2.1 Primary causal factors
**Immediate trigger:** A **short‑coupled PVC** initiating polymorphic VT/TdP that often degenerates into VF. (wang2022shortcoupledvariantof pages 1-2, leenhardt1994shortcoupledvariantof pages 1-3)

**Substrate concept:** Many cases appear “idiopathic” on standard testing, but convergent data point to **His‑Purkinje/endocavitary trigger sites** (Purkinje fibers, moderator band, RVOT) and to **genetic/oligogenic susceptibility** affecting calcium handling or conduction. (wang2022shortcoupledvariantof pages 12-14, touathamici2021aspry1domain pages 1-2, steinfurt2022catheterablationof pages 3-7)

### 2.2 Risk factors
**Genetic risk factors / associations (examples with variant‑level detail):**
* **RYR2** variants reported in familial and sporadic scTdP phenotypes, including **p.M995V (c.2983A>G)** (familial SCV‑TdP) (kimura2017anryr2mutation pages 2-3) and **p.I784F (c.2350A>T)** (sudden death case), with functional evidence of increased spontaneous Ca2+ release/SOICR and “leaky channel” behavior under non‑stress conditions. (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 2-3)
* **SCN5A p.R800H (c.2399G>A)** identified in a scTdP patient within a 7‑patient cohort screened by a 45‑gene inherited‑arrhythmia panel; functional studies showed **shortened recovery from inactivation**. (sonoda2020scn5amutationidentified pages 1-2)
* **DPP6 risk haplotype**: discussed as a Purkinje‑specific repolarization acceleration mechanism creating gradients that predispose to short‑coupled PVCs; DPP6 haplotype carrier status is a **principal diagnostic criterion** for the ongoing QUEEN‑IVF trial. (steinfurt2022catheterablationof pages 3-7, NCT05593757 chunk 1)

**Family history:** In the original 1994 series, **4/14** had familial sudden death history. (leenhardt1994shortcoupledvariantof pages 1-3)

**Physiologic stressors:** scTdP episodes may occur at rest and are often not related to adrenergic stress in some series, but individual cases suggest fever/hyperthermia can exacerbate triggers. (leenhardt1994shortcoupledvariantof pages 9-10, ham2024anhipsccmapproach pages 1-2)

### 2.3 Protective factors
No specific protective genetic variants or environmental protective factors were identified in the retrieved corpus.

### 2.4 Gene–environment interactions
A 2024 patient‑specific hiPSC‑CM model in a fever‑associated VF/scTdP case supports a **temperature‑sensitive increase in abnormal calcium events**, suggesting hyperthermia as a potential trigger interacting with an underlying susceptibility: “**at 39 °C the incidence of [early after transients] further increased**.” (ham2024anhipsccmapproach pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
* **Syncope** (HPO suggestion: *Syncope* [HP:0001279]) — presenting symptom in original series and later reports. (leenhardt1994shortcoupledvariantof pages 1-3)
* **Ventricular fibrillation** (HPO suggestion: *Ventricular fibrillation* [HP:0001663]) — common degeneration endpoint. (leenhardt1994shortcoupledvariantof pages 1-3)
* **Torsades de pointes / polymorphic VT** (HPO suggestion: *Torsade de pointes* [HP:0001677]; *Ventricular tachycardia* [HP:0004756]) (leenhardt1994shortcoupledvariantof pages 1-3, wang2022shortcoupledvariantof pages 1-2)
* **Premature ventricular contractions** (HPO suggestion: *Premature ventricular contractions* [HP:0006689]) — short‑coupled trigger PVCs. (wang2022shortcoupledvariantof pages 1-2)
* **Sudden cardiac arrest** (HPO suggestion: *Cardiac arrest* [HP:0001695]) — frequent first presentation in modern cohorts. (steinfurt2022catheterablationof pages 1-3)
* **Electrical storm** (clinical term; HPO suggestion: map to recurrent VT/VF) — frequent in malignant presentations. (steinfurt2022catheterablationof pages 1-3)

### 3.2 ECG phenotype (defining features)
Key ECG features across cohorts include:
* **Extremely short PVC coupling interval**: mean **245±28 ms** in the original series (leenhardt1994shortcoupledvariantof pages 1-3); pooled mean **302±62 ms** in a systematic review (wang2022shortcoupledvariantof pages 1-2); ≤300 ms inclusion criterion used in several studies. (fujii2017atype2 pages 2-3)
* **Normal baseline QT/QTc**: described as normal QT in the original series and systematic review framing. (leenhardt1994shortcoupledvariantof pages 9-10, wang2022shortcoupledvariantof pages 1-2)

### 3.3 Age of onset, severity, and progression
* Adults: Leenhardt mean age **34.6±10** years; mean follow‑up 7 years. (leenhardt1994shortcoupledvariantof pages 1-3)
* Pediatric: infant electrical storm case at **10 months**, demonstrating possible very early onset. (kise2018electricalstormin pages 1-3)
* Severity: high risk of VF degeneration (10/14 in original series). (leenhardt1994shortcoupledvariantof pages 1-3)
* EP study: low inducibility by programmed stimulation in original series (2/14 inducible). (leenhardt1994shortcoupledvariantof pages 1-3)

### 3.4 Quality of life impact
While disease‑specific QoL instruments were not reported in the retrieved primary series, the need for ICD shocks and recurrent arrhythmias implies substantial QoL impact; the QUEEN‑IVF trial rationale notes recurrent shocks “can negatively affect quality of life.” (NCT05593757 chunk 1)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and candidate genes
Evidence in the retrieved corpus supports a **genetically heterogeneous** architecture with candidate/causal roles for **RYR2** and **SCN5A** in subsets, and a broader susceptibility framework including Purkinje‑specific repolarization modifiers (e.g., DPP6 haplotype) and possible oligogenic combinations. (sonoda2020scn5amutationidentified pages 1-2, touathamici2021aspry1domain pages 1-2, steinfurt2022catheterablationof pages 3-7, NCT05593757 chunk 1)

| Gene | Reported variant / finding | Disease context | Evidence type | Mechanistic implication | Allele frequency / prevalence notes | Citations |
|---|---|---|---|---|---|---|
| **RYR2** | **p.M995V, c.2983A>G** | Familial short-coupled variant of TdP (SCV-TdP) | Family report / candidate causal variant | Supports abnormal RyR2-mediated Ca2+ handling in scTdP; authors discuss prior RyR2-H29D evidence for diastolic Ca2+ leak under non-stress conditions, consistent with EAD/DAD-related triggering | No population frequency reported in retrieved context | (kimura2017anryr2mutation pages 2-3) |
| **RYR2** | **p.H29D** (previously reported) | scTdP / short-coupled ventricular arrhythmia | Prior case-based and functional literature summarized in later papers | Leaky RyR2 channel at diastolic Ca2+ under non-stress conditions; implicates spontaneous Ca2+ release as trigger substrate | No allele frequency reported in retrieved context | (kimura2017anryr2mutation pages 2-3, fujii2017atype2 pages 2-3) |
| **RYR2** | **p.I784F, c.2350A>T** | Patient with short-coupled premature ventricular beats/polymorphic VT, sudden death, normal QTc | Exome sequencing + functional assay in HEK293 cells + structural biophysics | Enhanced store-overload induced Ca2+ release (SOICR), conformational change in SPRY1 domain, increased propensity to spontaneous Ca2+ release, “leaky channel under non-stress conditions”; supports Ca2+ wave/NCX inward current/DAD-trigger mechanism | Extremely rare; **MAF 0.0008% in gnomAD exomes** | (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 2-3, touathamici2021aspry1domain pages 9-10, touathamici2021aspry1domain pages 10-11) |
| **SCN5A** | **p.R800H, c.2399G>A** | scTdP in a 38-year-old man; identified in a screen of 7 consecutive scTdP patients using a 45-gene inherited-arrhythmia panel | Cohort sequencing + heterologous functional expression | Shortened recovery time from inactivation of Nav1.5 channels; peak sodium current trend larger than WT; suggests altered sodium-channel kinetics can predispose to short-coupled triggering | No allele frequency reported in retrieved context | (sonoda2020scn5amutationidentified pages 1-2) |
| **GJA5 (Cx40)** | **p.A96S, c.286G>T** | Same scTdP/sudden death case carrying RYR2-I784F | Exome sequencing; mechanistic interpretation based on known Purkinje expression and prior pathogenicity for atrial fibrillation | May impair electrical coupling / reduce conduction velocity in Purkinje fibers, acting with RyR2-mediated Ca2+ dysregulation to facilitate reentry or triggered VF; supports possible oligogenic basis | Reported as rare; **MAF ~0.012–0.016%** in population databases cited in paper | (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 2-3, touathamici2021aspry1domain pages 9-10) |
| **TNNI3K** | **p.R244X** (nonsense) | Same scTdP/sudden death case carrying RYR2-I784F and GJA5-A96S | Exome sequencing / candidate modifier | Considered a possible susceptibility or modifier factor rather than clearly causal; hypothesized to contribute to conduction abnormalities in an oligogenic model | No population frequency reported in retrieved context | (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 9-10) |
| **DPP6** | **Risk haplotype / mutation (not a single variant specified in retrieved context)** | Short-coupled idiopathic VF phenotype; included in current trial eligibility as DPP6 haplotype carriers | Mechanistic cohort literature summarized in ablation paper; prospective trial stratification | Selectively accelerated Purkinje fiber repolarization causing strong repolarization gradients with adjacent ventricular muscle, creating substrate for re-entry and short-coupled PVCs | Prevalence not reported in retrieved context; carrier status explicitly used for enrollment in QUEEN-IVF | (steinfurt2022catheterablationof pages 3-7, NCT05593757 chunk 1, NCT05593757 chunk 2) |
| **RYR2 (gene-level association)** | Multiple rare variants reported across scTdP studies | scTdP / short-coupled idiopathic VF | Cohort subset sequencing and literature synthesis | RyR2 dysfunction linked to intracellular Ca2+ release abnormalities; a plausible upstream mechanism for Purkinje-triggered PVCs and VF/TdP in patients without structural heart disease | In Fujii et al., **7 scTdP cases** were identified within an IVF cohort; no family history of SCD in that subset | (fujii2017atype2 pages 2-3) |
| **Oligogenic model** | **RYR2-I784F + GJA5-A96S + TNNI3K-R244X** | Purkinje-fiber ectopy causing scTdP / sudden death | Integrative genetic + functional interpretation | Combined defects in Ca2+ sensitivity/release and conduction coupling may better explain Purkinje ectopy and VF than a single-gene model alone | No combined genotype frequency reported | (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 9-10) |


*Table: This table summarizes reported genetic associations for short-coupled torsade de pointes/short-coupled idiopathic ventricular fibrillation, including specific variants, evidence types, mechanistic interpretations, and frequency notes. It is useful for distinguishing stronger functionally supported findings from candidate or modifier associations.*

### 4.2 Pathogenic variants (examples)
* **RYR2 p.I784F (c.2350A>T)** is extremely rare (reported **MAF 0.0008%** in gnomAD exomes) and is functionally associated with increased spontaneous Ca2+ release/SOICR. (touathamici2021aspry1domain pages 2-3)
* **SCN5A p.R800H (c.2399G>A)** functional data indicate altered sodium channel inactivation recovery. (sonoda2020scn5amutationidentified pages 1-2)

### 4.3 Modifier genes / oligogenicity
Touat‑Hamici et al. propose a possible oligogenic basis: RyR2‑I784F alongside **GJA5 (Cx40)** and **TNNI3K** variants may collectively affect Ca2+ handling and conduction in Purkinje tissue. (touathamici2021aspry1domain pages 1-2, touathamici2021aspry1domain pages 9-10)

### 4.4 Epigenetics / chromosomal abnormalities
No epigenetic or chromosomal abnormality evidence was found in the retrieved corpus.

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
No consistent lifestyle, toxicologic, or occupational exposures were identified as causal in the retrieved evidence.

### 5.2 Infectious agents
Not established as a primary cause in the retrieved corpus; however, fever/hyperthermia coinciding with VF/scTdP in a 2024 patient‑specific study suggests systemic illness can be a trigger context even when a clear pathogen is not specified. (ham2024anhipsccmapproach pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (proposed)
1. **Upstream susceptibility** (genetic and/or microstructural): variants affecting **RyR2 Ca2+ release**, sodium channel kinetics (**SCN5A**), conduction coupling (**Cx40**), or Purkinje repolarization gradients (**DPP6 haplotype**). (sonoda2020scn5amutationidentified pages 1-2, touathamici2021aspry1domain pages 1-2, steinfurt2022catheterablationof pages 3-7)
2. **Cellular trigger formation**: abnormal intracellular Ca2+ handling can generate spontaneous Ca2+ release events (SOICR), activating NCX current and producing DADs that trigger ectopy. (touathamici2021aspry1domain pages 2-3)
3. **Tissue‑level trigger**: a **short‑coupled PVC** from the Purkinje system/endocavitary structures (e.g., moderator band insertion) occurs during the vulnerable period (R‑on‑T‑like), initiating polymorphic VT/TdP. (wang2022shortcoupledvariantof pages 1-2, steinfurt2022catheterablationof pages 3-7)
4. **Clinical arrhythmia manifestation**: polymorphic VT/TdP may degenerate to **VF**, causing syncope or sudden cardiac arrest. (leenhardt1994shortcoupledvariantof pages 1-3)

### 6.2 Purkinje vulnerability and modern mechanistic framing (2024 update)
A 2024 TdP mechanisms review (focused primarily on long‑QT TdP but discussing short‑coupled VF as a TdP‑spectrum label) reinforces the concept of triggered beats and substrate heterogeneity, and emphasizes Purkinje susceptibility to afterdepolarizations under IKr blockade, and the clinical role of Purkinje‑targeted ablation. (tsuji2024mechanismsoftorsades pages 1-2)

### 6.3 Patient‑specific cellular modeling (2024)
In a patient‑specific hiPSC‑CM study (**2024-12**, *Stem Cell Research & Therapy*), the abstract states: “**Membrane potential data from the patient also revealed shorter action potentials that, combined with the EATs, indicate the premature release of calcium during diastole, which could be responsible for the extrasystoles in the patient**.” (ham2024anhipsccmapproach pages 1-2)

### 6.4 Ontology term suggestions (mechanism‑linked)
**GO biological processes (suggestions):**
* Regulation of cardiac conduction; regulation of heart rate; calcium ion transport; regulation of membrane depolarization; regulation of action potential; intracellular calcium ion homeostasis.

**Cell Ontology (CL) cell types (suggestions):**
* Cardiac Purkinje cell; ventricular cardiomyocyte.

**UBERON anatomical structures (suggestions):**
* Heart; right ventricle; His‑Purkinje system; moderator band.

(These mappings are ontology suggestions based on mechanistic descriptions in the retrieved literature rather than explicit ontology annotations in the source texts.) (steinfurt2022catheterablationof pages 3-7, touathamici2021aspry1domain pages 2-3)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary affected system: **cardiovascular system**, specifically ventricular electrical rhythm. (leenhardt1994shortcoupledvariantof pages 1-3)

### 7.2 Tissue/cellular level and trigger sites
Evidence points to **His‑Purkinje/endocavitary structures** as frequent trigger sources.

A 2022 3D‑mapping ablation series reports: “**In four patients, the culprit PVC was mapped to the free wall insertion of the moderator band (MB) with a preceding Purkinje potential in two patients**.” (steinfurt2022catheterablationof pages 1-3)

---

## 8. Temporal development

### 8.1 Onset
Often young adulthood (mean ~mid‑30s) but can present in infancy. (leenhardt1994shortcoupledvariantof pages 1-3, kise2018electricalstormin pages 1-3)

### 8.2 Course
Episodic, unpredictable; may present as recurrent syncope, aborted sudden cardiac arrest, or electrical storm. Long‑term arrhythmia behavior is described as unpredictable in the original series. (leenhardt1994shortcoupledvariantof pages 9-10, steinfurt2022catheterablationof pages 1-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology
True population prevalence and incidence are not well quantified in the retrieved primary sources; much evidence is from case series and registries.

However, multiple sources emphasize rarity:
* The systematic review aggregated **22 case reports and 103 case series patients** (reflecting sparse case‑based literature). (wang2022shortcoupledvariantof pages 1-2)

### 9.2 Inheritance patterns
Both sporadic and familial presentations occur:
* Familial sudden death history in **4/14** patients in the 1994 series. (leenhardt1994shortcoupledvariantof pages 1-3)
* Familial RYR2‑associated SCV‑TdP supports heritable risk in some families. (kimura2017anryr2mutation pages 2-3)

Penetrance/expressivity are not quantifiable from the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Clinical criteria and ECG criteria
Key diagnostic elements include:
* Documented polymorphic VT/TdP or VF initiated by a **short‑coupled PVC**, typically **<300 ms** in classic descriptions (leenhardt1994shortcoupledvariantof pages 1-3, steinfurt2022catheterablationof pages 1-3) and **<350 ms** in the contemporary QUEEN‑IVF trial diagnostic criterion. (NCT05593757 chunk 1)
* **No baseline QT prolongation** / normal QTc, distinguishing from classic pause‑dependent long‑QT TdP. (leenhardt1994shortcoupledvariantof pages 1-3, wang2022shortcoupledvariantof pages 1-2)
* Exclusion of significant structural heart disease via echo/CMR/coronary assessment. (steinfurt2022catheterablationof pages 1-3, ham2024anhipsccmapproach pages 1-2)

| Source / cohort | Disease label / definition | Coupling interval (PVC → TdP/VF) | QT / QTc | Typical PVC morphology / origin | Key outcome statistics | Citations |
|---|---|---|---|---|---|---|
| Leenhardt 1994 original series (n=14) | New electrocardiographic entity: TdP in patients without structural heart disease or long-QT syndrome, triggered by an extremely short-coupled premature beat | Mean 245 ± 28 ms; isolated VPBs also consistently <300 ms | Normal QT interval; no evidence of long-QT syndrome | Homogeneous initiating VPB morphology in 9/14; not yet anatomically mapped in this era | 10/14 degenerated to VF; mean follow-up 7 years; 5 deaths total, 4 sudden; only 2/14 inducible on programmed stimulation; 9 alive at follow-up (3 ICD, 6 verapamil) | (leenhardt1994shortcoupledvariantof pages 1-3, leenhardt1994shortcoupledvariantof pages 9-10) |
| Wang 2022 systematic review (22 case reports + 103 case-series patients) | scTdP/scVF = TdP/VF triggered by short-coupled PVCs despite otherwise normal baseline ECG and no structural heart disease | Mean first coupling interval 302 ± 62 ms overall; historical syndrome range 200–300 ms; Purkinje origin 274 ± 28 ms vs RVOT 380 ± 70 ms; cutoff >319 ms predicts RVOT origin | Baseline QT normal; short QT syndrome marker discussed separately as QT ≤320 ms | Trigger PVC QRS 135 ± 17 ms overall; Purkinje origin narrower than RVOT (131 ± 17 vs 147 ± 8 ms); common origins are Purkinje system and RVOT | 58% received ICD; 22% arrhythmia recurrence; 92% alive during follow-up; ICD associated with better survival than no ICD (log-rank P=0.001) | (wang2022shortcoupledvariantof pages 8-11, wang2022shortcoupledvariantof pages 1-2, wang2022shortcoupledvariantof pages 2-4, wang2022shortcoupledvariantof pages 12-14) |
| Fujii 2017 scTdP subset within IVF cohort (n=7) | scTdP phenotype within idiopathic VF cohort | Inclusion threshold ≤300 ms; mean 282 ± 13 ms | Mean QTc 422 ± 21 ms (normal range overall) | Triggering PVC QRS width 138 ± 16 ms; mechanistic focus on RyR2/Ca2+ handling rather than fixed site mapping | All had arrhythmic syncope, documented VF, or TdP; mean EF 62%; no structural heart disease; no family history of sudden cardiac death in this cohort | (fujii2017atype2 pages 2-3) |
| Kimura 2017 familial RYR2-associated case | SCV-TdP described as rare syndrome in otherwise healthy young adults, often at rest and usually not inducible | Usually <300 ms | Distinct from long-QT, Brugada, and short-QT syndromes | Not site-mapped here; literature discussion supports calcium-handling/Purkinje-related triggers | Approx. 30% family history of sudden death in prior reports; typical onset 31–34 years; ICD recommended; RF ablation plus ICD/drugs useful | (kimura2017anryr2mutation pages 2-3) |
| Steinfurt 2022 ablation cohort (n=5) | Recurrent sc-TdP/VF with monomorphic short-coupled PVC trigger; authors argue this phenotype predominantly arises from moderator band free-wall insertion/Purkinje network | All <300 ms; individual cases 240–280 ms | Structural/ischemic heart disease excluded; syndrome defined by absence of QT prolongation in background literature | Monomorphic PVC with late-transition LBBB pattern, superior axis; 4/5 mapped to moderator band free-wall insertion, 1 to inferoseptal RV/papillary muscle region; Purkinje potential preceded PVC in 2/5 | 4/5 presented with sudden cardiac arrest, 1/5 with recurrent syncope; ablation eliminated sc-TdP in all; no recurrence at mean 2.7 years (range 6 months–8 years); all received ICD | (steinfurt2022catheterablationof pages 1-3, steinfurt2022catheterablationof pages 3-7) |
| Infant case 2018 | First reported infant with ScTdP/electrical storm | Extremely short 200–240 ms | QTc 380 ms; resting 12-lead ECG otherwise normal | PVC-triggered VF/VT; no structural heart disease on echo | Out-of-hospital cardiac arrest with VF; ICD implanted; sustained VT/VF controlled with verapamil plus amiodarone, though nonsustained VT persisted | (kise2018electricalstormin pages 1-3) |
| QUEEN-IVF trial (NCT05593757) diagnostic framework | Short-coupled idiopathic VF/PVT defined for trial enrollment after exclusion of competing syndromes/structural disease | Principal diagnostic criterion: documented PVT (≥3 beats) or VF initiated by PVC with coupling interval <350 ms; isolated PVC <350 ms after index arrest/syncope also eligible | Excludes resting HR-corrected QT <350 ms or >480 ms | Designed for short-coupled IVF phenotype; includes DPP6 haplotype carriers; excludes pathogenic/likely pathogenic RYR2 carriers and successful ablation without recurrence | Phase 2 open-label randomized crossover pilot; estimated n=24; primary endpoint = sustained ventricular arrhythmia severity score over 3 years; compares oral quinidine 200 mg TID vs verapamil 320–480 mg/day | (NCT05593757 chunk 1, NCT05593757 chunk 2) |


*Table: This table compiles the main diagnostic ECG features, coupling interval thresholds, QT/QTc characteristics, likely PVC origins, and outcome data for short-coupled torsades de pointes/short-coupled ventricular fibrillation. It is useful for comparing the original syndrome description, later systematic review data, mapping/ablation cohorts, and the current interventional trial framework.*

### 10.2 Electrophysiology study
Inducibility is often low: in the original series, “**Only 2 patients had a tachyarrhythmia inducible by programmed stimulation**.” (leenhardt1994shortcoupledvariantof pages 1-3)

### 10.3 Differential diagnosis
Differential considerations include:
* Classic torsades de pointes due to congenital/acquired **long‑QT syndrome** (long coupling interval trigger beat) (leenhardt1994shortcoupledvariantof pages 1-3)
* **Pause‑dependent TdP** versus short‑coupled PVC‑initiated polymorphic VT (QUEEN‑IVF excludes pause‑dependent TdP by R‑R criteria). (NCT05593757 chunk 1)
* Other heritable syndromes excluded in QUEEN‑IVF: **Brugada syndrome**, early repolarization syndrome, **CPVT**; also excludes baseline QTc <350 ms or >480 ms. (NCT05593757 chunk 1)

### 10.4 Genetic testing strategy
Evidence supports targeted inherited arrhythmia gene testing:
* A 45‑gene inherited‑arrhythmia panel in scTdP identified SCN5A p.R800H in 1/7 patients, illustrating panel utility in selected cases. (sonoda2020scn5amutationidentified pages 1-2)
* QUEEN‑IVF requires that “**Genetic testing has been initiated**” (results not required at inclusion), reflecting modern practice. (NCT05593757 chunk 1)

---

## 11. Outcome / prognosis

### 11.1 Mortality and sudden death
High risk is evident in early series:
* In the original 1994 cohort: “**During a mean follow-up of 7 years there were 5 deaths (4 sudden)**.” (leenhardt1994shortcoupledvariantof pages 1-3)

### 11.2 Prognostic effect of ICD
Systematic review data support ICD survival benefit: Kaplan–Meier analysis showed increased survival with ICD versus no ICD (log‑rank P=0.001). (wang2022shortcoupledvariantof pages 1-2)

### 11.3 Post‑ablation outcomes
In a 5‑patient multicenter ablation cohort, ablation eliminated sc‑TdP in all patients “**with no recurrence at mean 2.7 years (range 6 months to 8 years) of follow-up**.” (steinfurt2022catheterablationof pages 1-3)

---

## 12. Treatment

### 12.1 Core management principles
1. **Prevent sudden death:** ICD for secondary prevention is strongly supported, given residual sudden death risk despite drug suppression. (leenhardt1994shortcoupledvariantof pages 1-3, wang2022shortcoupledvariantof pages 1-2)
2. **Suppress short‑coupled triggers and reduce shocks:** verapamil, and in selected cases other antiarrhythmics, plus ablation when a culprit PVC is identifiable. (steinfurt2022catheterablationof pages 1-3, NCT05593757 chunk 1)

| Management domain | Intervention / strategy | Evidence / role in short-coupled TdP / short-coupled VF | Reported outcomes / recurrence | Suggested MAXO term(s) | Citations |
|---|---|---|---|---|---|
| Acute resuscitation | External defibrillation / cardioversion | Used for VF, polymorphic VT, electrical storm, and sudden cardiac arrest presentations; original and later case series describe frequent degeneration to VF requiring emergency shock therapy | In the original 14-patient series, 10/14 episodes deteriorated into VF; infant and adult case reports survived arrest with acute resuscitation | MAXO: defibrillation; MAXO: cardioversion | (kise2018electricalstormin pages 1-3, steinfurt2022catheterablationof pages 1-3, leenhardt1994shortcoupledvariantof pages 1-3) |
| Acute antiarrhythmic stabilization | Verapamil (IV/oral transition) | Most consistently reported drug for suppressing short-coupled PVC-triggered TdP/VF; considered first-line pharmacotherapy in many reports/reviews, though protection from sudden death is incomplete | Leenhardt: arrhythmias appeared responsive but sudden death still occurred; infant case: sustained VT/VF controlled after verapamil addition; Steinfurt cohort: effective in 1 patient; current QUEEN-IVF trial formally compares verapamil vs quinidine | MAXO: calcium channel blocker therapy; MAXO: antiarrhythmic agent therapy | (wang2022shortcoupledvariantof pages 1-2, kise2018electricalstormin pages 1-3, kimura2017anryr2mutation pages 2-3, touathamici2021aspry1domain pages 1-2, steinfurt2022catheterablationof pages 1-3, NCT05593757 chunk 1) |
| Acute antiarrhythmic stabilization | Ajmaline | Not standard first-line therapy, but in one mapped ablation cohort patient, ajmaline suppressed short-coupled PVCs and terminated VF, supporting sodium-channel–sensitive trigger mechanisms in select cases | In Steinfurt cohort patient #2, ajmaline suppressed PVCs and terminated VF before EP study | MAXO: sodium channel blocker therapy; MAXO: antiarrhythmic agent therapy | (steinfurt2022catheterablationof pages 3-7) |
| Acute adjunctive therapy | Amiodarone | Often ineffective or insufficient in scTdP/scVF, though sometimes required transiently in refractory electrical storm; not considered reliably protective | Leenhardt: unlike verapamil, amiodarone not apparently active; infant case required amiodarone initially because VF/VT was refractory to defibrillation, but longer-term control improved only after verapamil | MAXO: amiodarone therapy; MAXO: antiarrhythmic agent therapy | (kise2018electricalstormin pages 1-3, leenhardt1994shortcoupledvariantof pages 1-3) |
| Acute adjunctive therapy | Beta-blockers | Frequently ineffective in this phenotype compared with long-QT or catecholaminergic syndromes; often reported as failed prior therapy | Ineffective in original series and later case-based literature; specifically ineffective in patients from the ablation cohort | MAXO: beta-adrenergic receptor antagonist therapy | (kimura2017anryr2mutation pages 2-3, steinfurt2022catheterablationof pages 1-3, leenhardt1994shortcoupledvariantof pages 1-3) |
| Acute adjunctive therapy | Magnesium, lidocaine, procainamide, cilostazol | Mentioned in later cohort review as therapies that may fail; evidence for benefit in short-coupled TdP specifically is weak and inconsistent | Steinfurt introduction notes pharmacologic treatment failure with Mg2+, lidocaine, procainamide, quinidine, cilostazol in prior experience/literature; one cohort patient had lidocaine ineffective | MAXO: magnesium supplementation; MAXO: lidocaine therapy; MAXO: procainamide therapy | (steinfurt2022catheterablationof pages 1-3, steinfurt2022catheterablationof pages 3-7) |
| Acute electrical storm care | Isoproterenol / sympathetic modulation / deep sedation | No direct disease-specific efficacy data were retrieved for scTdP itself; broader electrical storm reviews discuss these approaches, but available short-coupled-specific sources emphasize culprit-PVC suppression, ICD, and ablation instead | Not established from disease-specific primary evidence retrieved here | MAXO: adrenergic agonist therapy; MAXO: sedation | (wang2022shortcoupledvariantof pages 1-2) |
| Chronic pharmacotherapy | Verapamil | Most consistently supported chronic suppressive drug; reduces ectopy/arrhythmia burden but does not reliably prevent sudden death, so should not replace definitive protection in high-risk patients | Original series: 6 survivors on verapamil alone, but overall 5 deaths (4 sudden) across 7-year follow-up; systematic review states verapamil partially suppresses arrhythmias but does not prevent SCD | MAXO: calcium channel blocker therapy; MAXO: sudden cardiac death prevention | (wang2022shortcoupledvariantof pages 1-2, leenhardt1994shortcoupledvariantof pages 1-3, leenhardt1994shortcoupledvariantof pages 9-10) |
| Chronic pharmacotherapy | Quinidine | Evidence is mixed and evolving; some contemporary reviews and the ongoing QUEEN-IVF trial support active evaluation, but older scTdP reports often found it ineffective | Included as comparator in randomized crossover pilot trial (quinidine 200 mg TID vs verapamil 320–480 mg/day); older familial review described quinidine as ineffective in SCV-TdP | MAXO: quinidine therapy; MAXO: antiarrhythmic agent therapy | (kimura2017anryr2mutation pages 2-3, NCT05593757 chunk 1, NCT05593757 chunk 2) |
| Chronic pharmacotherapy | Flecainide | Limited disease-specific evidence; used adjunctively in at least one ablated patient after procedure | In Steinfurt cohort, 1 patient remained free from VF for 2.5 years on flecainide after ablation | MAXO: flecainide therapy; MAXO: antiarrhythmic agent therapy | (steinfurt2022catheterablationof pages 3-7) |
| Chronic pharmacotherapy | Dantrolene / flecainide / verapamil screening in patient-specific hiPSC model | 2024 disease-modeling work suggested these agents altered calcium-handling parameters but did not reduce early after-transient incidence in that patient-derived cellular model | Supports mechanistic heterogeneity and need for individualized treatment; not yet clinical efficacy evidence | MAXO: calcium release modulator therapy; MAXO: experimental therapy | (ham2024anhipsccmapproach pages 1-2) |
| Device therapy | Implantable cardioverter-defibrillator (ICD) | Most important proven protection against sudden cardiac death; emphasized across original series, systematic review, and modern case series | Wang review: ICD associated with increased survival vs no ICD; original series suggested ICD because verapamil did not prevent sudden death; ablation cohort implanted ICD in all 5 patients for secondary prevention | MAXO: implantable cardioverter-defibrillator implantation; MAXO: sudden cardiac death prevention | (wang2022shortcoupledvariantof pages 8-11, wang2022shortcoupledvariantof pages 1-2, steinfurt2022catheterablationof pages 1-3, leenhardt1994shortcoupledvariantof pages 1-3, leenhardt1994shortcoupledvariantof pages 9-10) |
| Device therapy | Transvenous vs subcutaneous ICD | Both have been used for secondary prevention; some reviews caution about subcutaneous ICD limitations such as T-wave oversensing in this phenotype | Steinfurt cohort: 2 transvenous and 3 subcutaneous ICDs; systematic review notes subcutaneous ICDs may be problematic because of T-wave oversensing | MAXO: transvenous ICD implantation; MAXO: subcutaneous ICD implantation | (wang2022shortcoupledvariantof pages 12-14, steinfurt2022catheterablationof pages 3-7) |
| Catheter ablation | Purkinje potential-guided ablation | Key interventional strategy when a culprit short-coupled PVC is identifiable; especially relevant for Purkinje-origin triggers with preceding Purkinje potentials | Systematic review and ablation series support high success in suppressing recurrent TdP/VF; ICD backup remains prudent because late recurrences and occult substrate may persist | MAXO: catheter ablation; MAXO: electrophysiology study | (wang2022shortcoupledvariantof pages 12-14, tsuji2024mechanismsoftorsades pages 1-2, steinfurt2022catheterablationof pages 3-7, arnaud2025idiopathicventricularfibrillation pages 5-6) |
| Catheter ablation target | Moderator band free-wall insertion / moderator band complex | Best-defined contemporary target in recurrent scTdP/scVF with characteristic late-transition LBBB, superior-axis PVC morphology and coupling interval <300 ms | Steinfurt cohort: 4/5 culprit PVCs mapped to moderator band free-wall insertion; ablation eliminated sc-TdP in all 5 with no recurrence at mean 2.7 years (range 6 months to 8 years) | MAXO: catheter ablation; MAXO: intracardiac echocardiography-guided procedure | (steinfurt2022catheterablationof pages 1-3, steinfurt2022catheterablationof pages 3-7) |
| Catheter ablation target | RVOT origin | Less common but recognized malignant trigger source; longer coupling interval and wider PVC QRS than Purkinje-origin events | Wang review: RVOT-origin scTdP had coupling interval 380 ± 70 ms vs 274 ± 28 ms for Purkinje; cutoff >319 ms predicted RVOT origin | MAXO: catheter ablation; MAXO: right ventricular outflow tract ablation | (wang2022shortcoupledvariantof pages 8-11, wang2022shortcoupledvariantof pages 1-2) |
| Catheter ablation target | Papillary muscle / inferoseptal right ventricle | Alternative right ventricular endocavitary trigger locations when moderator band anatomy is not dominant | In Steinfurt cohort, 1/5 culprit PVCs arose from inferoseptal RV/papillary muscle region; all ablation procedures were acutely successful | MAXO: catheter ablation | (steinfurt2022catheterablationof pages 3-7) |
| Long-term strategy | Combined therapy: ICD + antiarrhythmic drug +/− ablation | Common real-world approach because drugs alone incompletely protect from SCD and ablation may eliminate the trigger but not all substrate | Familial/case literature recommends ICD, with RF ablation and drugs used to suppress recurrent fatal arrhythmias; modern sources propose ablation in recurrent VF/electrical storm and sometimes first-line when trigger is clear | MAXO: combination therapy; MAXO: implantable cardioverter-defibrillator implantation; MAXO: catheter ablation | (kimura2017anryr2mutation pages 2-3, steinfurt2022catheterablationof pages 1-3, wang2022shortcoupledvariantof pages 1-2, arnaud2025idiopathicventricularfibrillation pages 5-6) |


*Table: This table summarizes acute and chronic management approaches reported for short-coupled torsades de pointes and short-coupled ventricular fibrillation, including drugs, ICD therapy, and catheter ablation targets. It highlights where evidence is strongest, especially for ICD implantation and moderator-band/Purkinje-trigger ablation.*

### 12.2 Pharmacotherapy
**Verapamil**
* The original series concluded: “**verapamil is in our experience the only drug apparently active on the arrhythmias; however, it does not prevent sudden death**.” (leenhardt1994shortcoupledvariantof pages 1-3)
* Later synthesis similarly notes partial suppression without definitive sudden‑death protection. (wang2022shortcoupledvariantof pages 1-2)

**Quinidine**
* Evidence is mixed across historical reports; it is being actively tested prospectively in the QUEEN‑IVF crossover trial against verapamil. (NCT05593757 chunk 1)

### 12.3 Catheter ablation
High‑resolution mapping identifies frequent moderator band/Purkinje targets:
* The 2022 series concluded sc‑TdP “predominantly originates from the MB free wall insertion and its Purkinje network,” with excellent mid‑term outcomes. (steinfurt2022catheterablationof pages 1-3)

### 12.4 Device therapy
ICD is repeatedly emphasized:
* “Therefore, we strongly suggest the use of ICD therapy” in the original series’ long‑term discussion. (leenhardt1994shortcoupledvariantof pages 9-10)

### 12.5 Experimental / clinical trials
**QUEEN‑IVF (NCT05593757)**
* Title: *Quinidine Versus Verapamil in Short-coupled Idiopathic Ventricular Fibrillation* (QUEEN‑IVF), **open‑label randomized crossover pilot** (Phase 2), estimated **n=24**, start **2022-10-01**, last update posted **2023-09-13**.
* Interventions: **quinidine 200 mg TID** vs **verapamil 320–480 mg/day**.
* Primary endpoint: sustained ventricular arrhythmia severity score over 3 years. (NCT05593757 chunk 1)

ClinicalTrials.gov URL (registry): https://clinicaltrials.gov/study/NCT05593757 (NCT05593757 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No established population screening or primary prevention strategy exists due to rarity and uncertain penetrance.

### 13.2 Secondary/tertiary prevention
* **ICD implantation** is the principal sudden‑death preventive measure after presentation. (leenhardt1994shortcoupledvariantof pages 1-3, wang2022shortcoupledvariantof pages 1-2)
* **Ablation** can be considered to prevent recurrent VF/electrical storm and reduce ICD shocks when a culprit trigger PVC is mapped. (steinfurt2022catheterablationof pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring non‑human disease analogs were identified in the retrieved corpus.

---

## 15. Model organisms / experimental models

### 15.1 Human cellular model (2024)
A notable recent development is **patient‑specific hiPSC‑CM modeling** of scTdP/idiopathic VF with fever‑associated recurrences, demonstrating early after‑calcium transients and shorter action potentials and enabling pharmacologic screening in vitro. (ham2024anhipsccmapproach pages 1-2, ham2024anhipsccmapproach pages 2-4)

### 15.2 Suggested model systems (based on mechanism)
* hiPSC‑CMs with engineered RYR2 variants to study SOICR/DAD mechanisms.
* Purkinje‑enriched in vitro preparations (where feasible) given Purkinje‑centric trigger hypotheses.

---

## Notable statistics (recent and foundational)
* Original series: **245±28 ms** coupling interval; **10/14** degenerated to VF; **5 deaths (4 sudden)** over mean 7 years. (leenhardt1994shortcoupledvariantof pages 1-3)
* Systematic review (2022): pooled first coupling interval **302±62 ms**; Purkinje vs RVOT coupling intervals **274±28 vs 380±70 ms**; ICD associated with improved survival; 58% ICD implantation; 92% alive during follow‑up in aggregated cases. (wang2022shortcoupledvariantof pages 1-2, wang2022shortcoupledvariantof pages 8-11)
* Ablation cohort (2022): **4/5** mapped to moderator band free‑wall insertion; **no recurrence** at mean **2.7 years** follow‑up. (steinfurt2022catheterablationof pages 1-3)
* hiPSC‑CM phenotyping (2024): early after‑transients in **8.14%** of patient measurements vs **0%** in controls under normothermia, increasing at 39°C. (ham2024anhipsccmapproach pages 2-4)

---

## Key evidence excerpts (direct quotes from abstracts)
* Leenhardt 1994 (Circulation; 1994-01): “**there was no evidence of long QT syndrome, and the torsade had the unusual particularity of an extremely short coupling interval… (245±28 milliseconds)**.” (leenhardt1994shortcoupledvariantof pages 1-3)
* Leenhardt 1994 (Circulation; 1994-01): “**During a mean follow-up of 7 years there were 5 deaths (4 sudden)**.” (leenhardt1994shortcoupledvariantof pages 1-3)
* van Ham 2024 (Stem Cell Research & Therapy; 2024-12): “**Membrane potential data from the patient also revealed shorter action potentials that, combined with the EATs, indicate the premature release of calcium during diastole**…” (ham2024anhipsccmapproach pages 1-2)
* Steinfurt 2022 (Clinical Research in Cardiology; online 2021-03-26; print 2022): “**Catheter ablation… eliminated sc-TdP in all patients, with no recurrence at mean 2.7 years… of follow-up**.” (steinfurt2022catheterablationof pages 1-3)

---

## Evidence gaps / limitations in current report
* Ontology identifiers (MONDO/OMIM/Orphanet/MeSH/ICD) were not available in the retrieved texts and thus are not asserted here.
* Large-scale incidence/prevalence data remain limited in the retrieved corpus; most data are case series.
* Some 2023–2024 guideline‑level statements and a 2023 pharmacology review were not obtainable through the current retrieval, so therapy recommendations are based on available primary series, systematic review, and trial registry evidence.

---

## Appendix: URLs and publication dates for key sources (from retrieved metadata)
* Leenhardt et al. *Circulation* — **1994-01** — https://doi.org/10.1161/01.cir.89.1.206 (leenhardt1994shortcoupledvariantof pages 1-3)
* Wang et al. *Frontiers in Cardiovascular Medicine* — **2022-08** — https://doi.org/10.3389/fcvm.2022.922525 (wang2022shortcoupledvariantof pages 1-2)
* Steinfurt et al. *Clinical Research in Cardiology* — online **2021-03-26**, journal issue **2022** — https://doi.org/10.1007/s00392-021-01840-z (steinfurt2022catheterablationof pages 1-3)
* Sonoda et al. *Pacing and Clinical Electrophysiology* — **2020-05** — https://doi.org/10.1111/pace.13924 (sonoda2020scn5amutationidentified pages 1-2)
* Fujii et al. *Heart Rhythm* — **2017-01** — https://doi.org/10.1016/j.hrthm.2016.10.015 (fujii2017atype2 pages 2-3)
* Touat‑Hamici et al. *Scientific Reports* — **2021-03** — https://doi.org/10.1038/s41598-021-84373-9 (touathamici2021aspry1domain pages 1-2)
* Tsuji et al. *Frontiers in Cardiovascular Medicine* — **2024-03** — https://doi.org/10.3389/fcvm.2024.1363848 (tsuji2024mechanismsoftorsades pages 1-2)
* QUEEN‑IVF trial (ClinicalTrials.gov NCT05593757) — first posted **2022-10-25**, last update posted **2023-09-13** — https://clinicaltrials.gov/study/NCT05593757 (NCT05593757 chunk 1)

References

1. (leenhardt1994shortcoupledvariantof pages 1-3): A. Leenhardt, E. Glaser, M. Burguera, M. Nurnberg, P. Maison-Blanche, and P. Coumel. Short-coupled variant of torsade de pointes. a new electrocardiographic entity in the spectrum of idiopathic ventricular tachyarrhythmias. Circulation, 89 1:206-15, Jan 1994. URL: https://doi.org/10.1161/01.cir.89.1.206, doi:10.1161/01.cir.89.1.206. This article has 523 citations and is from a highest quality peer-reviewed journal.

2. (leenhardt1994shortcoupledvariantof pages 9-10): A. Leenhardt, E. Glaser, M. Burguera, M. Nurnberg, P. Maison-Blanche, and P. Coumel. Short-coupled variant of torsade de pointes. a new electrocardiographic entity in the spectrum of idiopathic ventricular tachyarrhythmias. Circulation, 89 1:206-15, Jan 1994. URL: https://doi.org/10.1161/01.cir.89.1.206, doi:10.1161/01.cir.89.1.206. This article has 523 citations and is from a highest quality peer-reviewed journal.

3. (wang2022shortcoupledvariantof pages 1-2): Guangqiang Wang, Lin Zhong, Hongxia Chu, Chunxiao Wang, and Xuefeng Zhu. Short-coupled variant of torsade de pointes: a systematic review of case reports and case series. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.922525, doi:10.3389/fcvm.2022.922525. This article has 6 citations and is from a peer-reviewed journal.

4. (steinfurt2022catheterablationof pages 1-3): Johannes Steinfurt, Babak Nazer, Martin Aguilar, Joshua Moss, Satoshi Higuchi, Markus Zarse, Luca Trolese, Alexander Gressler, Thomas S. Faber, Katja E. Odening, Manfred Zehender, Christoph Bode, Melvin M. Scheinman, Usha B. Tedrow, and Harilaos Bogossian. Catheter ablation of short-coupled variant of torsade de pointes. Clinical Research in Cardiology, 111:502-510, Mar 2022. URL: https://doi.org/10.1007/s00392-021-01840-z, doi:10.1007/s00392-021-01840-z. This article has 15 citations and is from a peer-reviewed journal.

5. (steinfurt2022catheterablationof pages 3-7): Johannes Steinfurt, Babak Nazer, Martin Aguilar, Joshua Moss, Satoshi Higuchi, Markus Zarse, Luca Trolese, Alexander Gressler, Thomas S. Faber, Katja E. Odening, Manfred Zehender, Christoph Bode, Melvin M. Scheinman, Usha B. Tedrow, and Harilaos Bogossian. Catheter ablation of short-coupled variant of torsade de pointes. Clinical Research in Cardiology, 111:502-510, Mar 2022. URL: https://doi.org/10.1007/s00392-021-01840-z, doi:10.1007/s00392-021-01840-z. This article has 15 citations and is from a peer-reviewed journal.

6. (tsuji2024mechanismsoftorsades pages 1-2): Yukiomi Tsuji, Masatoshi Yamazaki, Masafumi Shimojo, Satoshi Yanagisawa, Yasuya Inden, and Toyoaki Murohara. Mechanisms of torsades de pointes: an update. Frontiers in Cardiovascular Medicine, Mar 2024. URL: https://doi.org/10.3389/fcvm.2024.1363848, doi:10.3389/fcvm.2024.1363848. This article has 23 citations and is from a peer-reviewed journal.

7. (NCT05593757 chunk 1): Christian van der Werf. Quinidine Versus Verapamil in Short-coupled Idiopathic Ventricular Fibrillation. Academisch Medisch Centrum - Universiteit van Amsterdam (AMC-UvA). 2022. ClinicalTrials.gov Identifier: NCT05593757

8. (wang2022shortcoupledvariantof pages 12-14): Guangqiang Wang, Lin Zhong, Hongxia Chu, Chunxiao Wang, and Xuefeng Zhu. Short-coupled variant of torsade de pointes: a systematic review of case reports and case series. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.922525, doi:10.3389/fcvm.2022.922525. This article has 6 citations and is from a peer-reviewed journal.

9. (touathamici2021aspry1domain pages 1-2): Zahia Touat-Hamici, Malorie Blancard, Ruifang Ma, Lianyun Lin, Yasmine Iddir, Isabelle Denjoy, Antoine Leenhardt, Zhiguang Yuchi, and Pascale Guicheney. A spry1 domain cardiac ryanodine receptor variant associated with short-coupled torsade de pointes. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-84373-9, doi:10.1038/s41598-021-84373-9. This article has 13 citations and is from a peer-reviewed journal.

10. (kimura2017anryr2mutation pages 2-3): Mai Kimura, Taishi Fujisawa, Yoshiyasu Aizawa, Noritaka Matsuhashi, Shogo Ito, Kazuaki Nakajima, Shin Kashimura, Akira Kunitomi, Yoshinori Katsumata, Takahiko Nishiyama, Takehiro Kimura, Nobuhiro Nishiyama, Shinsuke Yuasa, Seiji Takatsuki, Kenjiro Kosaki, and Keiichi Fukuda. An ryr2 mutation found in a family with a short-coupled variant of torsade de pointes. International journal of cardiology, 227:367-369, Jan 2017. URL: https://doi.org/10.1016/j.ijcard.2016.11.052, doi:10.1016/j.ijcard.2016.11.052. This article has 9 citations and is from a peer-reviewed journal.

11. (touathamici2021aspry1domain pages 2-3): Zahia Touat-Hamici, Malorie Blancard, Ruifang Ma, Lianyun Lin, Yasmine Iddir, Isabelle Denjoy, Antoine Leenhardt, Zhiguang Yuchi, and Pascale Guicheney. A spry1 domain cardiac ryanodine receptor variant associated with short-coupled torsade de pointes. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-84373-9, doi:10.1038/s41598-021-84373-9. This article has 13 citations and is from a peer-reviewed journal.

12. (sonoda2020scn5amutationidentified pages 1-2): Keiko Sonoda, Seiko Ohno, Yukiko Shimizu, Kazuaki Kaitani, Takeru Makiyama, Yoshihisa Nakagawa, and Minoru Horie. <i>scn5a</i> mutation identified in a patient with short‐coupled variant of torsades de pointes. Pacing and Clinical Electrophysiology, 43:456-461, May 2020. URL: https://doi.org/10.1111/pace.13924, doi:10.1111/pace.13924. This article has 6 citations.

13. (ham2024anhipsccmapproach pages 1-2): Willem B. van Ham, Esmeralda E. M. Meijboom, Merel L. Ligtermoet, Jantine Monshouwer-Kloots, Anneline S. J. M. te Riele, Folkert W. Asselbergs, Eva van Rooij, Mimount Bourfiss, and Toon A. B. van Veen. An hipsc-cm approach for electrophysiological phenotyping of a patient-specific case of short-coupled tdp. Stem Cell Research & Therapy, Dec 2024. URL: https://doi.org/10.1186/s13287-024-04074-8, doi:10.1186/s13287-024-04074-8. This article has 0 citations and is from a peer-reviewed journal.

14. (fujii2017atype2 pages 2-3): Yusuke Fujii, Hideki Itoh, Seiko Ohno, Takashi Murayama, Nagomi Kurebayashi, Hisaaki Aoki, Malorie Blancard, Yoshihisa Nakagawa, Satoshi Yamamoto, Yumie Matsui, Mari Ichikawa, Keiko Sonoda, Tomoya Ozawa, Kimie Ohkubo, Ichiro Watanabe, Pascale Guicheney, and Minoru Horie. A type 2 ryanodine receptor variant associated with reduced ca2+ release and short-coupled torsades de pointes ventricular arrhythmia. Heart rhythm, 14 1:98-107, Jan 2017. URL: https://doi.org/10.1016/j.hrthm.2016.10.015, doi:10.1016/j.hrthm.2016.10.015. This article has 99 citations and is from a peer-reviewed journal.

15. (kise2018electricalstormin pages 1-3): Hiroaki Kise, Seiko Ohno, Yosuke Kono, Masashi Yoshizawa, Daisuke Harama, Asami Okafuji, Takako Toda, Keiichi Koizumi, Minako Hoshiai, Kanji Sugita, and Minoru Horie. Electrical storm in an infant with short‐coupled variant of torsade de pointes. Journal of Arrhythmia, 34:315-318, May 2018. URL: https://doi.org/10.1002/joa3.12071, doi:10.1002/joa3.12071. This article has 1 citations and is from a peer-reviewed journal.

16. (touathamici2021aspry1domain pages 9-10): Zahia Touat-Hamici, Malorie Blancard, Ruifang Ma, Lianyun Lin, Yasmine Iddir, Isabelle Denjoy, Antoine Leenhardt, Zhiguang Yuchi, and Pascale Guicheney. A spry1 domain cardiac ryanodine receptor variant associated with short-coupled torsade de pointes. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-84373-9, doi:10.1038/s41598-021-84373-9. This article has 13 citations and is from a peer-reviewed journal.

17. (touathamici2021aspry1domain pages 10-11): Zahia Touat-Hamici, Malorie Blancard, Ruifang Ma, Lianyun Lin, Yasmine Iddir, Isabelle Denjoy, Antoine Leenhardt, Zhiguang Yuchi, and Pascale Guicheney. A spry1 domain cardiac ryanodine receptor variant associated with short-coupled torsade de pointes. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-84373-9, doi:10.1038/s41598-021-84373-9. This article has 13 citations and is from a peer-reviewed journal.

18. (NCT05593757 chunk 2): Christian van der Werf. Quinidine Versus Verapamil in Short-coupled Idiopathic Ventricular Fibrillation. Academisch Medisch Centrum - Universiteit van Amsterdam (AMC-UvA). 2022. ClinicalTrials.gov Identifier: NCT05593757

19. (wang2022shortcoupledvariantof pages 8-11): Guangqiang Wang, Lin Zhong, Hongxia Chu, Chunxiao Wang, and Xuefeng Zhu. Short-coupled variant of torsade de pointes: a systematic review of case reports and case series. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.922525, doi:10.3389/fcvm.2022.922525. This article has 6 citations and is from a peer-reviewed journal.

20. (wang2022shortcoupledvariantof pages 2-4): Guangqiang Wang, Lin Zhong, Hongxia Chu, Chunxiao Wang, and Xuefeng Zhu. Short-coupled variant of torsade de pointes: a systematic review of case reports and case series. Frontiers in Cardiovascular Medicine, Aug 2022. URL: https://doi.org/10.3389/fcvm.2022.922525, doi:10.3389/fcvm.2022.922525. This article has 6 citations and is from a peer-reviewed journal.

21. (arnaud2025idiopathicventricularfibrillation pages 5-6): Marine Arnaud, Josselin Duchateau, and Mélèze Hocini. Idiopathic ventricular fibrillation: substrates, mechanisms and treatment. Arrhythmia &amp; Electrophysiology Review, Dec 2025. URL: https://doi.org/10.15420/aer.2025.34, doi:10.15420/aer.2025.34. This article has 1 citations and is from a peer-reviewed journal.

22. (ham2024anhipsccmapproach pages 2-4): Willem B. van Ham, Esmeralda E. M. Meijboom, Merel L. Ligtermoet, Jantine Monshouwer-Kloots, Anneline S. J. M. te Riele, Folkert W. Asselbergs, Eva van Rooij, Mimount Bourfiss, and Toon A. B. van Veen. An hipsc-cm approach for electrophysiological phenotyping of a patient-specific case of short-coupled tdp. Stem Cell Research & Therapy, Dec 2024. URL: https://doi.org/10.1186/s13287-024-04074-8, doi:10.1186/s13287-024-04074-8. This article has 0 citations and is from a peer-reviewed journal.