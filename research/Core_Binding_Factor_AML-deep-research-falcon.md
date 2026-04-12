---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:07:52.600932'
end_time: '2026-04-05T14:20:58.702895'
duration_seconds: 786.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Myeloid Leukemia, Core Binding Factor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Myeloid Leukemia, Core Binding Factor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, Core Binding Factor** covering all of the
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
- **Disease Name:** Acute Myeloid Leukemia, Core Binding Factor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, Core Binding Factor** covering all of the
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


## Comprehensive Research Report: Core-Binding Factor Acute Myeloid Leukemia (CBF-AML)

### Target disease
- **Disease name:** Acute Myeloid Leukemia, Core Binding Factor (CBF-AML)
- **Category:** Myeloid neoplasm; acute leukemia defined by recurrent balanced rearrangements
- **Key defining lesions:** **t(8;21)(q22;q22) RUNX1::RUNX1T1** and **inv(16)(p13.1;q22)/t(16;16)(p13.1;q22) CBFB::MYH11** (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)
- **MONDO ID:** Not found in the retrieved evidence corpus (see “Gaps/limitations”).

---

## 1. Disease information

### 1.1 Overview (current understanding)
Core-binding factor AML is a molecularly and cytogenetically defined subset of AML characterized by the recurrent rearrangements t(8;21) producing the **RUNX1::RUNX1T1** fusion and inv(16)/t(16;16) producing the **CBFB::MYH11** fusion; these are commonly grouped because both disrupt the core-binding factor (CBF) transcriptional complex and are generally considered favorable-risk with high complete remission (CR) rates after intensive therapy. (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)

### 1.2 Common synonyms / alternative names
- **Core-binding factor AML / CBF-AML** (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)
- **AML with RUNX1::RUNX1T1** (t(8;21)) (boscaro2023modernriskstratification pages 4-5, kanellou2023deregulatedgeneexpression pages 1-2)
- **AML with CBFB::MYH11** (inv(16)/t(16;16)) (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)

### 1.3 Key identifiers
Within this tool session, only **general AML** MONDO/EFO identifiers were returned by OpenTargets, not a distinct MONDO entry for CBF-AML; hence ontology identifiers below are provided as *suggestions* where not directly evidenced. (boscaro2023modernriskstratification pages 4-5)

### 1.4 Evidence source type
This report integrates:
- **Aggregated disease-level resources:** narrative reviews and guideline-oriented risk stratification reviews (george2023therapyrelatedcorebinding pages 4-5, boscaro2023modernriskstratification pages 4-5)
- **Human clinical cohorts/real-world studies:** venetoclax/HMA cohorts (zhang2023efficacyofvenetoclax pages 1-2, chen2024efficacyofvenetoclax pages 8-11)
- **Mechanistic/model systems:** primary murine HSPC proteogenomics with validation in primary human AML cells (day2024proteogenomicanalysisreveals pages 1-2, day2024proteogenomicanalysisreveals media 35681b36)

---

## 2. Etiology

### 2.1 Primary causal factors
CBF-AML is primarily driven by **acquired (somatic) chromosomal rearrangements** that generate CBF fusion oncogenes, which impair differentiation and require cooperating lesions for overt leukemia. (george2023therapyrelatedcorebinding pages 1-2)

### 2.2 Risk factors

#### 2.2.1 Therapy-related CBF-AML (t-CBF-AML)
CBF-AML can arise as a **therapy-related AML** following cytotoxic chemotherapy and/or radiation. Therapy-related CBF-AML is estimated to represent **~5–15% of CBF-AML** cases. (george2023therapyrelatedcorebinding pages 1-2)

**Latency:** exposure class is associated with latency differences: alkylating agents/radiotherapy are associated with t-AML after **~5–10 years**, whereas topoisomerase II inhibitors can be followed by t-AML within **~1–3 years**. (george2023therapyrelatedcorebinding pages 1-2)

#### 2.2.2 Genetic/cooperating risk (two-hit model)
A “two-hit” framework is described in which **class II events** (CBF fusions: RUNX1::RUNX1T1 or CBFB::MYH11) drive differentiation arrest, while cooperating **class I signaling mutations** (e.g., **KIT, FLT3, RAS**) provide proliferative/survival signaling. (george2023therapyrelatedcorebinding pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors specific to CBF-AML were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
The retrieved corpus supports an interaction between **therapy exposure** (environmental/iatrogenic) and acquisition of **balanced translocations** (including CBF fusions), but does not provide quantitative gene–environment interaction models. (boscaro2023modernriskstratification pages 4-5)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (high-level)
CBF-AML manifests as AML with marrow failure and circulating disease; within the retrieved evidence, explicit symptom frequencies are sparse. However, several measurable and clinically actionable phenotypes are supported:

- **Leukocytosis**: in a de novo CBF-AML cohort, inv(16)/CBFB::MYH11 cases had higher presenting WBC than t(8;21) cases, consistent with clinically observed proliferative differences. (qin2022comprehensivemutationprofile pages 2-3)
- **Relapse despite CR**: RUNX1::RUNX1T1 AML is noted to have substantial relapse risk; one study background notes “approximately 50% of patients relapse” despite achieving CR. (kanellou2023deregulatedgeneexpression pages 1-2)
- **Infectious complications / functional unfitness**: in a venetoclax+HMA cohort of newly diagnosed unfit CBF-AML, many patients were ineligible for intensive therapy due to active infections/sepsis and organ comorbidities, indicating infection burden as a practical phenotype/complication in real-world populations. (zhang2023efficacyofvenetoclax pages 1-2)

### 3.2 Suggested HPO terms (examples; not exhaustive)
A curated mapping table is provided below (artifact-01), including cytopenia, leukocytosis, recurrent infections, and fatigue as common AML-relevant phenotypes. (qin2022comprehensivemutationprofile pages 1-2, zhang2023efficacyofvenetoclax pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal fusion genes (defining)
- **RUNX1::RUNX1T1** (t(8;21)) (boscaro2023modernriskstratification pages 4-5, kanellou2023deregulatedgeneexpression pages 1-2)
- **CBFB::MYH11** (inv(16)/t(16;16)) (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)

### 4.2 Common cooperating (somatic) mutations: quantitative frequencies
A targeted NGS cohort of **134 de novo CBF-AML** patients reported the following co-mutation frequencies (overall cohort): **KIT 33.6%**, **NRAS 33.6%**, **FLT3 18.7%**, **KRAS 13.4%**, with low frequencies of canonical epigenetic modifier mutations (**IDH1 1.5%, IDH2 0.7%, DNMT3A 2.2%, TET2 7.5%**). (qin2022comprehensivemutationprofile pages 1-2)

Fusion-type heterogeneity was substantial: **NRAS** and **KRAS** were enriched in CBFB::MYH11 (NRAS 53.7% vs 20.0%; KRAS 27.8% vs 3.8%), whereas **cohesin complex mutations** were enriched in RUNX1::RUNX1T1 (11.3% vs 0%). (qin2022comprehensivemutationprofile pages 5-7, qin2022comprehensivemutationprofile pages 8-9)

### 4.3 Cytogenetic “secondary” changes
In the same de novo cohort, **41.0%** had additional cytogenetic abnormalities; common events included **−X/−Y (24.6%)** and **+22 (9.7%)**, with +22 particularly frequent in inv(16) (20.1%). (qin2022comprehensivemutationprofile pages 2-3)

### 4.4 Epigenetic / transcriptomic notes
RUNX1::RUNX1T1 AML is described as transcriptionally reprogrammed; one transcriptomic analysis notes that RUNX1/RUNX1T1 occupies >4000 genomic sites and that it has been reported to “regulate alternative RNA splicing and induce transcriptome re-organization in leukemic cells.” (kanellou2023deregulatedgeneexpression pages 2-4)

---

## 5. Environmental information

### 5.1 Environmental/iatrogenic contributors
The main environment-linked contributor supported in the retrieved evidence is **prior cytotoxic chemotherapy and/or radiotherapy** leading to therapy-related CBF-AML, with class-specific latency differences. (george2023therapyrelatedcorebinding pages 1-2)

No infectious etiologies were identified.

---

## 6. Mechanism / pathophysiology

### 6.1 Mechanistic “causal chain” (integrated)
1) **Initiation**: acquisition of RUNX1::RUNX1T1 or CBFB::MYH11 creates a differentiation-blocking transcriptional perturbation (class II lesion). (george2023therapyrelatedcorebinding pages 1-2)
2) **Cooperation**: frequent signaling co-mutations (KIT/FLT3/RAS) enhance proliferation/survival, promoting expansion and progression. (qin2022comprehensivemutationprofile pages 1-2, george2023therapyrelatedcorebinding pages 1-2)
3) **Persistence/relapse biology**: residual leukemic clones can be tracked by fusion-transcript MRD and are associated with relapse risk; relapse remains a major clinical issue, particularly in subsets such as RUNX1::RUNX1T1. (george2023therapyrelatedcorebinding pages 4-5, kanellou2023deregulatedgeneexpression pages 1-2)

### 6.2 Key 2024 mechanistic advance (CBFB::MYH11): cytoplasmic sequestration of RUNX1
A 2024 **proteogenomic** study (TurboID proximity labeling) demonstrated that CBFB::MYH11 has a predominantly **cytoplasmic interactome**, and that CBFB::MYH11 can **sequester RUNX1 into cytoplasmic aggregates**, reducing nuclear CBF function; this was validated in primary human AML cells. (day2024proteogenomicanalysisreveals pages 1-2, day2024proteogenomicanalysisreveals pages 2-4)

**Visual evidence:** cytoplasmic localization and RUNX1 aggregate sequestration are shown in cropped figure panels from the Day et al. JCI paper. (day2024proteogenomicanalysisreveals media 35681b36, day2024proteogenomicanalysisreveals media e05b6c7f)

A 2024 JCI commentary emphasized this as a pathogenic mechanism (“cytoplasmic transcription factor sequestration”). (shilatifard2024cytoplasmictranscriptionfactor pages 1-1)

### 6.3 Suggested GO and CL terms (examples)
A curated suggestion table is provided (artifact-01), including **hematopoietic cell differentiation (GO:0030098)**, **chromatin organization (GO:0006325)**, and cell types such as **CD34+ hematopoietic progenitors**. (kanellou2023deregulatedgeneexpression pages 2-4, kreissig2023decipheringacutemyeloid pages 1-2)

---

## 7. Anatomical structures affected

CBF-AML primarily involves:
- **Bone marrow** (UBERON:0002371; primary disease compartment and sampling site) (kanellou2023deregulatedgeneexpression pages 1-2)
- **Peripheral blood** (UBERON:0000178; circulating blasts and blood-based monitoring) (kanellou2023deregulatedgeneexpression pages 1-2)

Subcellular localization is mechanistically relevant in CBFB::MYH11 AML: **cytoplasmic** sequestration of RUNX1 by the fusion. (day2024proteogenomicanalysisreveals pages 2-4, day2024proteogenomicanalysisreveals media 35681b36)

---

## 8. Temporal development

### 8.1 Onset
CBF-AML tends to occur at **younger age at diagnosis** and is often **de novo**, though therapy-related cases occur and tend to be older. (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 6-8)

### 8.2 Progression and relapse
Despite favorable-risk classification and high CR rates, relapse remains clinically important; RUNX1::RUNX1T1 AML is noted to have high relapse rates (~50% in a background statement). (kanellou2023deregulatedgeneexpression pages 1-2)

---

## 9. Inheritance and population

CBF-AML is not described as a Mendelian inherited disorder in the retrieved sources; it is driven by somatic fusion events. (george2023therapyrelatedcorebinding pages 1-2)

### 9.1 Epidemiology
- **CBF-AML fraction of AML:** ~10–15% of newly diagnosed AML. (boscaro2023modernriskstratification pages 4-5)
- **General AML incidence (not CBF-specific):** SEER rates since 2010 reported as >4.2 per 100,000/year. (kanellou2023deregulatedgeneexpression pages 1-2)

---

## 10. Diagnostics

### 10.1 Defining diagnostic tests
- **Cytogenetics / fusion detection:** diagnosis is defined by detecting t(8;21) or inv(16)/t(16;16) and corresponding fusions. (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2)

### 10.2 MRD monitoring (real-world implementation)
A 2023 review emphasizes **qRT-PCR/RT-qPCR** quantification of RUNX1::RUNX1T1 and CBFB::MYH11 transcripts as a preferred high-sensitivity MRD method; flow cytometry is useful but qPCR is preferred. (george2023therapyrelatedcorebinding pages 4-5)

**Clinically used thresholds (examples):**
- RUNX1::RUNX1T1: **>3-log reduction** at end of induction and **≥4-log reduction** at mid-consolidation associated with improved relapse-free survival. (george2023therapyrelatedcorebinding pages 4-5)
- CBFB::MYH11: post-induction **>10 copies normalized to 10^5 ABL** associated with inferior molecular response/higher relapse risk. (george2023therapyrelatedcorebinding pages 4-5)

**Assay normalization example (clinical cohort):** a 2023 CBF-AML venetoclax/HMA cohort monitored MRD by RT-qPCR with fusion copies normalized to **ABL** (“copies per 10^5 copies of ABL”). (zhang2023efficacyofvenetoclax pages 1-2)

### 10.3 Differential diagnosis
Differential diagnosis details (e.g., distinction from AML with other recurrent genetic abnormalities, mixed phenotype acute leukemia, APL) were not explicitly provided in the retrieved evidence corpus.

---

## 11. Outcome / prognosis

### 11.1 Response and survival (intensive therapy context)
CBF-AML is generally considered chemosensitive with **CR ~85–90%** reported in a 2023 risk-stratification review and **>85%** in a 2023 therapy-related CBF review. (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 4-5)

A 2023 review summarizes long-term outcome benchmarks from intensive regimens and GO intensification (e.g., MRC AML15 **8-year survival 66%** with FLAG-Ida/HiDAC; GO-containing regimens with favorable long-term survival statistics). (george2023therapyrelatedcorebinding pages 4-5)

### 11.2 Therapy-related CBF-AML outcomes
Therapy-related CBF-AML has **worse overall survival than de novo CBF-AML** but better outcomes than therapy-related AML with unfavorable cytogenetics; one summary comparison reports OS 100 weeks (t-CBF-AML) vs 621 weeks (de novo CBF-AML). (george2023therapyrelatedcorebinding pages 4-5)

### 11.3 Prognostic modifiers
Cooperating receptor tyrosine kinase mutations (e.g., KIT, FLT3) are repeatedly highlighted as clinically relevant, and MRD depth is emphasized as a strong prognostic factor. (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 1-2)

---

## 12. Treatment

### 12.1 Standard-of-care (intensive) backbone
A 2023 review summarizes the standard approach as **cytarabine/anthracycline induction (e.g., “7+3”)** followed by **high-dose cytarabine (HiDAC) consolidation**, consistent with CBF-AML chemosensitivity. (george2023therapyrelatedcorebinding pages 4-5)

### 12.2 Addition of gemtuzumab ozogamicin (GO)
Addition of **gemtuzumab ozogamicin (GO)** to intensive chemotherapy is described as improving response and long-term outcomes in favorable/intermediate-risk AML including CBF-AML, and is integrated in CBF-focused regimens such as FLAG-GO in some centers. (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 9-10)

### 12.3 Venetoclax + hypomethylating agent (HMA) in unfit CBF-AML (recent real-world development)
A 2023 retrospective cohort of **30 newly diagnosed unfit CBF-AML** treated with **venetoclax + azacitidine or decitabine** found markedly different induction response by fusion subtype:
- t(8;21): **CR/CRi 31% (4/13)** after one cycle
- inv(16)/t(16;16): **CR/CRi 100% (17/17)** after one cycle
- overall: **2-year OS 92.2% (95% CI 70.8–98.0%)** with MRD assessed by fusion RT-qPCR normalized to ABL. (zhang2023efficacyofvenetoclax pages 1-2)

This study explicitly states clinical background definitions and standard practice: “Core binding factor acute myeloid leukemia (CBF-AML) features the recurrent chromosomal rearrangements… which encode the RUNX1::RUNX1T1 and CBFB::MYH11 fusion genes.” (zhang2023efficacyofvenetoclax pages 1-2)

A 2024 real-world study (preprint) in favorable-risk unfit AML also reports CBF-subtype-specific CR/CRi differences (RUNX1::RUNX1T1 35.7% vs CBFB::MYH11 90.9%) and demonstrates that MRD negativity strongly associates with improved 2-year OS/EFS. (chen2024efficacyofvenetoclax pages 8-11)

### 12.4 Transplantation strategy (expert synthesis)
Because of high response rates, **allogeneic transplantation is often not routine in CR1** for standard favorable-risk CBF-AML; however, MRD persistence and inability to complete therapy are cited as reasons to consider early donor search/transplant. (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 6-8)

### 12.5 Ongoing/real-world clinical trials (applications)
The retrieved ClinicalTrials.gov records show active development of risk- and genotype-directed therapies:
- **NCT06917911** (NCI MyeloMATCH; Phase II; NOT_YET_RECRUITING; est. 2026): compares adding **venetoclax** vs **gemtuzumab ozogamicin** to **7+3** in CBF-AML; primary endpoint is **CR without MRD by multiparameter flow cytometry**. URL: https://clinicaltrials.gov/study/NCT06917911 (NCT06917911 chunk 1)
- **NCT03686345** (Phase II; terminated per retrieved metadata): **midostaurin + standard chemotherapy** in core-binding factor leukemia; record links to publication **PMID: 39659145**. URL: https://clinicaltrials.gov/study/NCT03686345 (NCT03686345 chunk 2)
- **NCT06783790** (Phase II; recruiting; 2025): for relapsed AML after allo-HSCT with CBF fusions and **KIT D816/N822** mutations; regimen combines **avapritinib + azacitidine + venetoclax**. URL: https://clinicaltrials.gov/study/NCT06783790 (NCT06783790 chunk 1)
- **NCT07028073** (recruiting; 2025): “new treatment” for newly diagnosed **KIT-mutated CBF-AML** (details incomplete in excerpt). URL: https://clinicaltrials.gov/study/NCT07028073 (NCT07028073 chunk 2)

### 12.6 Suggested MAXO terms
Suggested treatment/monitoring mappings (MAXO IDs not retrievable from evidence corpus) are provided in artifact-01. (george2023therapyrelatedcorebinding pages 4-5, zhang2023efficacyofvenetoclax pages 1-2)

---

## 13. Prevention

No disease-specific primary prevention strategies were identified beyond general minimization of exposure to leukemogenic cytotoxic therapies when clinically feasible; the strongest “secondary prevention” concept in the retrieved evidence is **early relapse detection via MRD monitoring** (qRT-PCR or flow cytometry/NGS depending on protocol). (george2023therapyrelatedcorebinding pages 4-5, NCT06917911 chunk 1)

---

## 14. Other species / natural disease
No naturally occurring CBF-AML analogs in other species were identified in the retrieved evidence corpus.

---

## 15. Model organisms

### 15.1 Key model systems and what they capture
- **Primary murine HSPCs (ex vivo) + retroviral transduction:** TurboID-fused oncofusion constructs in lineage-depleted murine progenitors enabled interactome mapping, with validation in primary human AML for key phenotypes (cytoplasmic CBFB::MYH11 and RUNX1 sequestration). (day2024proteogenomicanalysisreveals pages 1-2, day2024proteogenomicanalysisreveals pages 2-4)
- **Primary human CD34+ HSPC models:** a 2023 review emphasizes genetically manipulating healthy-donor human CD34+ cells as an approach to model leukemic growth driven by fusion transcription factors, highlighting that murine-to-human transferability is limited. (kreissig2023decipheringacutemyeloid pages 1-2)

### 15.2 Translational limitations (expert analysis)
Xenografts in immunodeficient mice lack adaptive immunity and have species-specific microenvironmental differences that “can lead to biased results,” and ex vivo systems cannot recapitulate full organismal complexity; thus complementary models are needed. (kreissig2023decipheringacutemyeloid pages 12-13)

---

## Structured summary tables

The following tables are provided to support knowledge-base population and curation.

| Category | Finding / Metric | Quantitative detail | Source (year) | PMID | URL | Citation |
|---|---|---|---|---|---|---|
| Definition / identifiers | Core-binding factor acute myeloid leukemia (CBF-AML) | Defined by **t(8;21)(q22;q22) / RUNX1::RUNX1T1** and **inv(16)(p13.1q22) or t(16;16)(p13.1;q22) / CBFB::MYH11** | Boscaro et al. 2023; George et al. 2023 |  | https://doi.org/10.3390/cancers15133512 ; https://doi.org/10.2217/ijh-2022-0004 | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| Epidemiology | Approximate proportion of AML | CBF-AML accounts for **~10–15%** of newly diagnosed AML; George review also cites **roughly 15% of AML** | Boscaro et al. 2023; George et al. 2023 |  | https://doi.org/10.3390/cancers15133512 ; https://doi.org/10.2217/ijh-2022-0004 | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| Genomic landscape cohort | De novo CBF-AML cohort analyzed by NGS | **n=134** total; **80 RUNX1-RUNX1T1**, **54 CBFB-MYH11**; 112-gene panel, ~1000× coverage, VAF >3% | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 2-3) |
| Co-mutations | KIT mutation frequency | **33.6% overall (45/134)**; **35.0% RUNX1-RUNX1T1** vs **31.5% CBFB-MYH11** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 5-7) |
| Co-mutations | NRAS mutation frequency | **33.6% overall (45/134)**; **20.0% RUNX1-RUNX1T1 (16/80)** vs **53.7% CBFB-MYH11 (29/54)** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 5-7) |
| Co-mutations | KRAS mutation frequency | **13.4% overall (18/134)**; **3.8% RUNX1-RUNX1T1 (3/80)** vs **27.8% CBFB-MYH11 (15/54)** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 5-7) |
| Co-mutations | FLT3 mutation frequency | **18.7% overall (25/134)**; similar rates across fusion types | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 5-7) |
| Co-mutations | Epigenetic modifier mutation frequencies | **IDH1 1.5%**, **IDH2 0.7%**, **DNMT3A 2.2%**, **TET2 7.5%** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 8-9) |
| Co-mutations / pathways | Signaling-pathway mutation burden | **86.6% overall (116/134)**; **80.0% RUNX1-RUNX1T1** vs **96.3% CBFB-MYH11** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 5-7, qin2022comprehensivemutationprofile pages 7-8) |
| Co-mutations / pathways | Cohesin-complex mutations | **6.7% overall (9/134)**; **11.3% RUNX1-RUNX1T1**, **0% CBFB-MYH11** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 5-7, qin2022comprehensivemutationprofile pages 8-9) |
| Cytogenetics | Secondary chromosomal abnormalities | **41.0% (55/134)** overall; **45.0% t(8;21)** vs **35.2% inv(16)/t(16;16)**; common changes: **-X/-Y 24.6% (33/134)**, **+22 9.7% (13/134)** | Qin et al. 2022 |  | https://doi.org/10.4274/tjh.galenos.2022.2021.0641 | (qin2022comprehensivemutationprofile pages 2-3) |
| MRD diagnostics | Preferred MRD method | **qRT-PCR / RT-qPCR** for **RUNX1::RUNX1T1** and **CBFB::MYH11** is the preferred, highly sensitive MRD method; flow cytometry useful but qPCR preferred | George et al. 2023 |  | https://doi.org/10.2217/ijh-2022-0004 | (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 10-11) |
| MRD thresholds | RUNX1::RUNX1T1 molecular response thresholds | **>3-log reduction** at end of induction and **≥4-log reduction** at mid-consolidation associated with improved relapse-free survival | George et al. 2023 |  | https://doi.org/10.2217/ijh-2022-0004 | (george2023therapyrelatedcorebinding pages 4-5) |
| MRD thresholds | CBFB::MYH11 molecular threshold | Post-induction **>10 CBFB::MYH11 copies normalized to 10^5 ABL** associated with lower-quality molecular response / higher relapse risk | George et al. 2023 |  | https://doi.org/10.2217/ijh-2022-0004 | (george2023therapyrelatedcorebinding pages 4-5) |
| Standard intensive therapy context | Complete remission rate with standard intensive therapy | Reported CR rate **85–90%** in CBF-AML; review also states CR rates **>85%** with induction/consolidation approaches | Boscaro et al. 2023; George et al. 2023 |  | https://doi.org/10.3390/cancers15133512 ; https://doi.org/10.2217/ijh-2022-0004 | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 4-5) |
| Standard intensive therapy context | Selected long-term survival statistics | MRC AML15: **8-year survival 66%** with FLAG-Ida + HiDAC; GO-containing approaches cited with **8-year OS after CR 72%**, **5-year survival 76% vs 54%** in favorable cytogenetics, and **FLAG-GO 5-year OS 71%, 5-year RFS 87%** | George et al. 2023 |  | https://doi.org/10.2217/ijh-2022-0004 | (george2023therapyrelatedcorebinding pages 4-5) |
| VEN+HMA cohort | Newly diagnosed unfit CBF-AML treated with VEN+HMA | **n=30** total; **13 t(8;21)** and **17 inv(16)/t(16;16)** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2) |
| VEN+HMA genomics | Baseline mutation frequencies in Zhang cohort | **KIT 53% (16/30)**, **RAS 33% (10/30)**, **FLT3 13% (4/30)**, **TP53 0%** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2, zhang2023efficacyofvenetoclax pages 2-3) |
| VEN+HMA MRD assay | Molecular monitoring method in Zhang cohort | Real-time quantitative RT-PCR of fusion transcripts normalized to **ABL**, reported as **copies per 10^5 ABL** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2) |
| VEN+HMA efficacy | CR/CRi after one cycle: t(8;21) | **31% (4/13)** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2) |
| VEN+HMA efficacy | CR/CRi after one cycle: inv(16)/t(16;16) | **100% (17/17)** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2, zhang2023efficacyofvenetoclax pages 2-3) |
| VEN+HMA molecular response | CBFB::MYH11 transcript level after one cycle | Median **340 copies** (range **0–20,650**) among inv(16)/t(16;16) patients after one cycle | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2) |
| VEN+HMA survival | Overall survival in Zhang cohort | **2-year OS 92.2%** (95% CI **70.8–98.0%**); median follow-up **11.6 months** | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 1-2) |
| VEN+HMA interpretation | Subtype-specific activity | Authors report VEN+HMA appears useful for **inv(16)/t(16;16)** AML, whereas **t(8;21)** predicts minimal benefit | Zhang et al. 2023 |  | https://doi.org/10.1038/s41408-023-00928-1 | (zhang2023efficacyofvenetoclax pages 3-4) |
| VA preprint cohort | Favorable-risk unfit AML real-world study with CBF subsets | **n=70** total favorable-risk AML; **14 RUNX1::RUNX1T1**, **11 CBFB::MYH11** | Chen et al. 2024 preprint |  | https://doi.org/10.21203/rs.3.rs-5301043/v1 | (chen2024efficacyofvenetoclax pages 8-11) |
| VA preprint efficacy | CR/CRi by subtype | **RUNX1::RUNX1T1 35.7% (5/14)**; **CBFB::MYH11 90.9% (10/11)**; overall cohort **84.3% (59/70)** | Chen et al. 2024 preprint |  | https://doi.org/10.21203/rs.3.rs-5301043/v1 | (chen2024efficacyofvenetoclax pages 8-11) |
| VA preprint MRD / outcomes | MRD-negativity and survival | After 2 consolidation cycles, MRD negativity **85.0% (17/20)** in VA group vs **73.3% (22/30)** in chemotherapy group; MRD-negative patients had better **2-year OS 89.8% vs 65.6% (p=0.01)** and **2-year EFS 51.4% vs 0% (p<0.01)** | Chen et al. 2024 preprint |  | https://doi.org/10.21203/rs.3.rs-5301043/v1 | (chen2024efficacyofvenetoclax pages 8-11) |


*Table: This table compiles core identifiers, genomic features, MRD thresholds, and recent venetoclax-based outcome data for core-binding factor AML. It is useful as a compact reference for disease definition, co-mutation patterns, and subtype-specific treatment response.*

| Category | Entity / clinical concept | Suggested ontology term | Identifier / status | Evidence / rationale | Citation |
|---|---|---|---|---|---|
| Disease | Core-binding factor acute myeloid leukemia | Core-binding factor acute myeloid leukemia | MONDO not found in retrieved evidence | CBF-AML defined by RUNX1::RUNX1T1 and CBFB::MYH11 rearrangements; specific MONDO term was not retrieved in available context | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| Disease subtype | AML with t(8;21)(q22;q22.1); RUNX1::RUNX1T1 | Acute myeloid leukemia with RUNX1::RUNX1T1 | Suggested only | One defining CBF-AML subtype in retrieved reviews and cohorts | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| Disease subtype | AML with inv(16)(p13.1q22) / t(16;16)(p13.1;q22); CBFB::MYH11 | Acute myeloid leukemia with CBFB::MYH11 | Suggested only | One defining CBF-AML subtype in retrieved reviews and cohorts | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| HPO phenotype | Cytopenia | Cytopenia | HP:0001871 | Common AML manifestation; relevant umbrella phenotype for marrow failure in CBF-AML | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| HPO phenotype | Anemia | Anemia | HP:0001903 | Suggested for symptomatic marrow failure and fatigue | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| HPO phenotype | Thrombocytopenia | Thrombocytopenia | HP:0001873 | Suggested for bleeding tendency in AML | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| HPO phenotype | Neutropenia | Neutropenia | HP:0001875 | Suggested for infection susceptibility in AML | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| HPO phenotype | Leukocytosis | Leukocytosis | HP:0001974 | Supported by CBF-AML cohort studies showing elevated WBC, especially inv(16)/CBFB::MYH11 | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 2-3) |
| HPO phenotype | Recurrent infections / increased infection susceptibility | Recurrent infections | HP:0002719 | Suggested because infections are common clinical consequences of AML-associated neutropenia and were a frequent reason patients were unfit for intensive therapy | (zhang2023efficacyofvenetoclax pages 1-2) |
| HPO phenotype | Bleeding tendency | Abnormal bleeding | HP:0001892 | Suggested for thrombocytopenia-associated bleeding manifestations | (george2023therapyrelatedcorebinding pages 1-2) |
| HPO phenotype | Fatigue | Fatigue | HP:0012378 | Suggested common symptom of AML/anemia | (kanellou2023deregulatedgeneexpression pages 1-2) |
| GO process | Differentiation block / altered hematopoiesis | Hematopoietic cell differentiation | GO:0030098 | Core mechanism of CBF fusions; two-hit model emphasizes differentiation impairment | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 2-4) |
| GO process | Transcriptional dysregulation | Regulation of DNA-templated transcription | GO:0006355 | RUNX1::RUNX1T1 acts through transcriptional repression/rewiring | (shilatifard2024cytoplasmictranscriptionfactor pages 1-1, kanellou2023deregulatedgeneexpression pages 1-2) |
| GO process | Chromatin remodeling | Chromatin organization | GO:0006325 | CBF leukemia mechanisms include chromatin remodeling and altered transcriptional programs | (day2024proteogenomicanalysisreveals pages 18-18, kanellou2023deregulatedgeneexpression pages 16-17) |
| GO process | Aberrant proliferation | Cell population proliferation | GO:0008283 | Cooperating kinase/RAS lesions promote proliferation in two-hit leukemogenesis | (george2023therapyrelatedcorebinding pages 1-2, qin2022comprehensivemutationprofile pages 1-2) |
| GO process | Signaling activation | Intracellular signal transduction | GO:0035556 | Frequent KIT/FLT3/RAS pathway co-mutations support signaling-process involvement | (qin2022comprehensivemutationprofile pages 1-2, qin2022comprehensivemutationprofile pages 5-7) |
| GO process | Residual leukemic persistence / relapse biology | Regulation of cell death | GO:0010941 | Suggested because relapse and treatment resistance remain major clinical issues in CBF-AML | (kanellou2023deregulatedgeneexpression pages 1-2, day2024proteogenomicanalysisreveals pages 18-18) |
| Cell Ontology | Hematopoietic stem/progenitor cell (CD34+) | Hematopoietic stem cell / hematopoietic progenitor cell | CL:0000037 / CL:0000826 | Human primary CD34+ HSPCs are a key experimental system for AML transcription-factor modeling | (kanellou2023deregulatedgeneexpression pages 2-4) |
| Cell Ontology | Myeloid progenitor | Myeloid progenitor cell | CL:0000051 | CBF-AML arises in myeloid progenitor context | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| Cell Ontology | Myeloblast | Myeloblast | CL:0000763 | Suggested malignant blast cell type in AML | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| Cell Ontology | Leukemic blast | Hematopoietic blast cell | CL:0008001 | Suggested broader blast-cell mapping when exact myeloblast annotation is uncertain | (george2023therapyrelatedcorebinding pages 1-2) |
| UBERON anatomy | Bone marrow | Bone marrow | UBERON:0002371 | Primary disease site and sampling compartment in AML/CBF-AML | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| UBERON anatomy | Peripheral blood | Blood | UBERON:0000178 | Disease commonly involves circulating blasts / blood-based monitoring | (george2023therapyrelatedcorebinding pages 1-2, kanellou2023deregulatedgeneexpression pages 1-2) |
| GO cellular component | Nucleus | Nucleus | GO:0005634 | RUNX1::RUNX1T1 acts in nuclear repressor complexes | (day2024proteogenomicanalysisreveals pages 1-2, shilatifard2024cytoplasmictranscriptionfactor pages 1-1) |
| GO cellular component | Cytoplasm | Cytoplasm | GO:0005737 | CBFB::MYH11 is predominantly cytoplasmic and sequesters RUNX1 in cytoplasmic aggregates | (day2024proteogenomicanalysisreveals pages 1-2, day2024proteogenomicanalysisreveals pages 2-4, day2024proteogenomicanalysisreveals media 35681b36) |
| MAXO therapy | Induction chemotherapy | Induction chemotherapy | MAXO suggested; exact ID not retrieved | Standard initial therapy for CBF-AML | (george2023therapyrelatedcorebinding pages 4-5, boscaro2023modernriskstratification pages 4-5) |
| MAXO therapy | Cytarabine-based therapy / HiDAC consolidation | Cytarabine therapy | MAXO suggested; exact ID not retrieved | Cytarabine sensitivity and HiDAC consolidation are central in CBF-AML care | (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |
| MAXO therapy | Gemtuzumab ozogamicin-containing therapy | Gemtuzumab ozogamicin therapy | MAXO suggested; exact ID not retrieved | Addition of GO improves long-term outcomes in favorable/intermediate AML including CBF-AML | (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 9-10) |
| MAXO therapy | Venetoclax-based therapy | Venetoclax therapy | MAXO suggested; exact ID not retrieved | Recent non-intensive strategy with subtype-specific activity in CBF-AML | (zhang2023efficacyofvenetoclax pages 1-2, chen2024efficacyofvenetoclax pages 8-11) |
| MAXO therapy | Hypomethylating-agent therapy | Azacitidine therapy | MAXO suggested; exact ID not retrieved | Used with venetoclax in unfit/newly diagnosed CBF-AML cohorts | (zhang2023efficacyofvenetoclax pages 1-2, chen2024efficacyofvenetoclax pages 8-11) |
| MAXO therapy | Allogeneic transplantation | Allogeneic hematopoietic stem cell transplantation | MAXO suggested; exact ID not retrieved | Considered selectively; often not routine in CR1 for standard favorable-risk CBF-AML | (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 10-11) |
| MAXO monitoring | Molecular MRD assessment | MRD monitoring by qRT-PCR | MAXO suggested; exact ID not retrieved | Preferred MRD method uses qRT-PCR for RUNX1::RUNX1T1 and CBFB::MYH11 transcripts | (george2023therapyrelatedcorebinding pages 4-5, zhang2023efficacyofvenetoclax pages 1-2) |
| Note | Validation status | These ontology mappings are suggestions | Not exhaustively validated in retrieved texts | Intended to support knowledge-base curation; several exact ontology IDs, especially MAXO and MONDO subtype terms, were not directly retrieved from context | (boscaro2023modernriskstratification pages 4-5, george2023therapyrelatedcorebinding pages 1-2) |


*Table: This table proposes ontology mappings for disease, phenotypes, mechanisms, cell types, anatomy, and interventions relevant to core-binding factor AML. It is useful as a curation aid, but several identifiers—especially MONDO subtype and MAXO treatment IDs—were not directly validated in the retrieved evidence.*

---

## Gaps / limitations of this tool-grounded report
- **Disease ontology IDs:** A specific **MONDO ID for “CBF-AML”** was not recovered in the retrieved evidence; only general AML identifiers were returned by OpenTargets.
- **PMIDs:** Many included sources in this session are open-access journal articles with DOIs, but PMIDs were not consistently present in the retrieved text excerpts; the ClinicalTrials.gov record for NCT03686345 explicitly lists **PMID 39659145**. (NCT03686345 chunk 2)
- **Differential diagnosis and symptom frequency tables:** Not available in the retrieved corpus; phenotype content is therefore high-level and supplemented with ontology suggestions.

---

## Key recent references (prioritizing 2023–2024; URLs and dates)
- Day RB et al. *J Clin Invest.* **Dec 2024**. “Proteogenomic analysis reveals cytoplasmic sequestration of RUNX1 by the AML-initiating CBFB::MYH11 oncofusion protein.” https://doi.org/10.1172/jci176311 (day2024proteogenomicanalysisreveals pages 1-2, day2024proteogenomicanalysisreveals media 35681b36)
- Shilatifard A. *J Clin Invest.* **Feb 2024**. “Cytoplasmic transcription factor sequestration drives the pathogenesis of a rearranged leukemia.” https://doi.org/10.1172/jci179105 (shilatifard2024cytoplasmictranscriptionfactor pages 1-1)
- Zhang K et al. *Blood Cancer J.* **Oct 2023**. Venetoclax + HMA in newly diagnosed unfit CBF-AML. https://doi.org/10.1038/s41408-023-00928-1 (zhang2023efficacyofvenetoclax pages 1-2)
- Boscaro E et al. *Cancers (Basel).* **Jul 2023**. Modern AML risk stratification (includes CBF-AML). https://doi.org/10.3390/cancers15133512 (boscaro2023modernriskstratification pages 4-5)
- George B et al. *Int J Hematol Oncol.* **Feb 2023**. Therapy-related CBF-AML review (MRD thresholds, therapy context). https://doi.org/10.2217/ijh-2022-0004 (george2023therapyrelatedcorebinding pages 4-5, george2023therapyrelatedcorebinding pages 1-2)


References

1. (boscaro2023modernriskstratification pages 4-5): Eleonora Boscaro, Irene Urbino, Federica Maria Catania, Giulia Arrigo, Carolina Secreto, Matteo Olivi, Stefano D’Ardia, Chiara Frairia, Valentina Giai, Roberto Freilone, Dario Ferrero, Ernesta Audisio, and Marco Cerrano. Modern risk stratification of acute myeloid leukemia in 2023: integrating established and emerging prognostic factors. Cancers, 15:3512, Jul 2023. URL: https://doi.org/10.3390/cancers15133512, doi:10.3390/cancers15133512. This article has 35 citations.

2. (george2023therapyrelatedcorebinding pages 1-2): Binsah George, Binoy Yohannan, Virginia Mohlere, and Anneliese Gonzalez. Therapy-related core binding factor acute myeloid leukemia. International Journal of Hematologic Oncology, Feb 2023. URL: https://doi.org/10.2217/ijh-2022-0004, doi:10.2217/ijh-2022-0004. This article has 8 citations.

3. (kanellou2023deregulatedgeneexpression pages 1-2): Peggy Kanellou, Ilias Georgakopoulos-Soares, and Apostolos Zaravinos. Deregulated gene expression profiles and regulatory networks in adult and pediatric runx1/runx1t1-positive aml patients. Cancers, 15:1795, Mar 2023. URL: https://doi.org/10.3390/cancers15061795, doi:10.3390/cancers15061795. This article has 9 citations.

4. (george2023therapyrelatedcorebinding pages 4-5): Binsah George, Binoy Yohannan, Virginia Mohlere, and Anneliese Gonzalez. Therapy-related core binding factor acute myeloid leukemia. International Journal of Hematologic Oncology, Feb 2023. URL: https://doi.org/10.2217/ijh-2022-0004, doi:10.2217/ijh-2022-0004. This article has 8 citations.

5. (zhang2023efficacyofvenetoclax pages 1-2): Keyuan Zhang, Xiang Zhang, Yang Xu, Shengli Xue, Huiying Qiu, Xiaowen Tang, Yue Han, Suning Chen, Aining Sun, Yanming Zhang, Depei Wu, and Ying Wang. Efficacy of venetoclax combined with hypomethylating agents in young, and unfit patients with newly diagnosed core binding factor acute myeloid leukemia. Blood Cancer Journal, Oct 2023. URL: https://doi.org/10.1038/s41408-023-00928-1, doi:10.1038/s41408-023-00928-1. This article has 32 citations and is from a domain leading peer-reviewed journal.

6. (chen2024efficacyofvenetoclax pages 8-11): Qi Chen, Ying Wu, Wenjing Yu, Xiaolu Zhu, Xuying Pei, Wenbing Duan, Jinsong Jia, Jing Wang, Xiaosu Zhao, Guorui Ruan, Yingjun Chang, Hongxia Shi, Xiaojun Huang, and Hao Jiang. Efficacy of venetoclax and azacitidine based therapy in favorable-risk unfit acute myeloid leukemia: a real-world study. Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-5301043/v1, doi:10.21203/rs.3.rs-5301043/v1.

7. (day2024proteogenomicanalysisreveals pages 1-2): Ryan B. Day, Julia A. Hickman, Ziheng Xu, Casey D.S. Katerndahl, Francesca Ferraro, Sai Mukund Ramakrishnan, Petra Erdmann-Gilmore, Robert W. Sprung, Yiling Mi, R. Reid Townsend, Christopher A. Miller, and Timothy J. Ley. Proteogenomic analysis reveals cytoplasmic sequestration of runx1 by the acute myeloid leukemia–initiating cbfb::myh11 oncofusion protein. Journal of Clinical Investigation, Dec 2024. URL: https://doi.org/10.1172/jci176311, doi:10.1172/jci176311. This article has 14 citations and is from a highest quality peer-reviewed journal.

8. (day2024proteogenomicanalysisreveals media 35681b36): Ryan B. Day, Julia A. Hickman, Ziheng Xu, Casey D.S. Katerndahl, Francesca Ferraro, Sai Mukund Ramakrishnan, Petra Erdmann-Gilmore, Robert W. Sprung, Yiling Mi, R. Reid Townsend, Christopher A. Miller, and Timothy J. Ley. Proteogenomic analysis reveals cytoplasmic sequestration of runx1 by the acute myeloid leukemia–initiating cbfb::myh11 oncofusion protein. Journal of Clinical Investigation, Dec 2024. URL: https://doi.org/10.1172/jci176311, doi:10.1172/jci176311. This article has 14 citations and is from a highest quality peer-reviewed journal.

9. (qin2022comprehensivemutationprofile pages 2-3): Wei Qin, Xiayu Chen, Hong Jie Shen, Zheng Wang, Xiaohui Cai, Naike Jiang, and Haiying Hua. Comprehensive mutation profile in acute myeloid leukemia patients with runx1-runx1t1 or cbfb-myh11 fusions. Turkish Journal of Hematology, 39:84-93, Apr 2022. URL: https://doi.org/10.4274/tjh.galenos.2022.2021.0641, doi:10.4274/tjh.galenos.2022.2021.0641. This article has 11 citations.

10. (qin2022comprehensivemutationprofile pages 1-2): Wei Qin, Xiayu Chen, Hong Jie Shen, Zheng Wang, Xiaohui Cai, Naike Jiang, and Haiying Hua. Comprehensive mutation profile in acute myeloid leukemia patients with runx1-runx1t1 or cbfb-myh11 fusions. Turkish Journal of Hematology, 39:84-93, Apr 2022. URL: https://doi.org/10.4274/tjh.galenos.2022.2021.0641, doi:10.4274/tjh.galenos.2022.2021.0641. This article has 11 citations.

11. (qin2022comprehensivemutationprofile pages 5-7): Wei Qin, Xiayu Chen, Hong Jie Shen, Zheng Wang, Xiaohui Cai, Naike Jiang, and Haiying Hua. Comprehensive mutation profile in acute myeloid leukemia patients with runx1-runx1t1 or cbfb-myh11 fusions. Turkish Journal of Hematology, 39:84-93, Apr 2022. URL: https://doi.org/10.4274/tjh.galenos.2022.2021.0641, doi:10.4274/tjh.galenos.2022.2021.0641. This article has 11 citations.

12. (qin2022comprehensivemutationprofile pages 8-9): Wei Qin, Xiayu Chen, Hong Jie Shen, Zheng Wang, Xiaohui Cai, Naike Jiang, and Haiying Hua. Comprehensive mutation profile in acute myeloid leukemia patients with runx1-runx1t1 or cbfb-myh11 fusions. Turkish Journal of Hematology, 39:84-93, Apr 2022. URL: https://doi.org/10.4274/tjh.galenos.2022.2021.0641, doi:10.4274/tjh.galenos.2022.2021.0641. This article has 11 citations.

13. (kanellou2023deregulatedgeneexpression pages 2-4): Peggy Kanellou, Ilias Georgakopoulos-Soares, and Apostolos Zaravinos. Deregulated gene expression profiles and regulatory networks in adult and pediatric runx1/runx1t1-positive aml patients. Cancers, 15:1795, Mar 2023. URL: https://doi.org/10.3390/cancers15061795, doi:10.3390/cancers15061795. This article has 9 citations.

14. (day2024proteogenomicanalysisreveals pages 2-4): Ryan B. Day, Julia A. Hickman, Ziheng Xu, Casey D.S. Katerndahl, Francesca Ferraro, Sai Mukund Ramakrishnan, Petra Erdmann-Gilmore, Robert W. Sprung, Yiling Mi, R. Reid Townsend, Christopher A. Miller, and Timothy J. Ley. Proteogenomic analysis reveals cytoplasmic sequestration of runx1 by the acute myeloid leukemia–initiating cbfb::myh11 oncofusion protein. Journal of Clinical Investigation, Dec 2024. URL: https://doi.org/10.1172/jci176311, doi:10.1172/jci176311. This article has 14 citations and is from a highest quality peer-reviewed journal.

15. (day2024proteogenomicanalysisreveals media e05b6c7f): Ryan B. Day, Julia A. Hickman, Ziheng Xu, Casey D.S. Katerndahl, Francesca Ferraro, Sai Mukund Ramakrishnan, Petra Erdmann-Gilmore, Robert W. Sprung, Yiling Mi, R. Reid Townsend, Christopher A. Miller, and Timothy J. Ley. Proteogenomic analysis reveals cytoplasmic sequestration of runx1 by the acute myeloid leukemia–initiating cbfb::myh11 oncofusion protein. Journal of Clinical Investigation, Dec 2024. URL: https://doi.org/10.1172/jci176311, doi:10.1172/jci176311. This article has 14 citations and is from a highest quality peer-reviewed journal.

16. (shilatifard2024cytoplasmictranscriptionfactor pages 1-1): Ali Shilatifard. Cytoplasmic transcription factor sequestration drives the pathogenesis of a rearranged leukemia. The Journal of Clinical Investigation, Feb 2024. URL: https://doi.org/10.1172/jci179105, doi:10.1172/jci179105. This article has 0 citations.

17. (kreissig2023decipheringacutemyeloid pages 1-2): Sophie Kreissig, Roland Windisch, and Christian Wichmann. Deciphering acute myeloid leukemia associated transcription factors in human primary cd34+ hematopoietic stem/progenitor cells. Cells, 13:78, Dec 2023. URL: https://doi.org/10.3390/cells13010078, doi:10.3390/cells13010078. This article has 1 citations.

18. (george2023therapyrelatedcorebinding pages 6-8): Binsah George, Binoy Yohannan, Virginia Mohlere, and Anneliese Gonzalez. Therapy-related core binding factor acute myeloid leukemia. International Journal of Hematologic Oncology, Feb 2023. URL: https://doi.org/10.2217/ijh-2022-0004, doi:10.2217/ijh-2022-0004. This article has 8 citations.

19. (george2023therapyrelatedcorebinding pages 9-10): Binsah George, Binoy Yohannan, Virginia Mohlere, and Anneliese Gonzalez. Therapy-related core binding factor acute myeloid leukemia. International Journal of Hematologic Oncology, Feb 2023. URL: https://doi.org/10.2217/ijh-2022-0004, doi:10.2217/ijh-2022-0004. This article has 8 citations.

20. (NCT06917911 chunk 1):  Testing the Addition of Venetoclax or Gemtuzumab Ozogamicin (GO) to Usual Treatment Regimen (Cytarabine and Daunorubicin, "7+3") for Core Binding Factor Acute Myeloid Leukemia (CBF-AML) to Improve Response (A MyeloMATCH Treatment Trial). National Cancer Institute (NCI). 2026. ClinicalTrials.gov Identifier: NCT06917911

21. (NCT03686345 chunk 2):  Midostaurin Associated With Standard Chemotherapy in Patients With Core-binding Factor Leukemia. Niguarda Hospital. 2018. ClinicalTrials.gov Identifier: NCT03686345

22. (NCT06783790 chunk 1):  Avapritinib Combined With Azacitidine and Venetoclax in the Treatment of Relapsed AML After Allo-HSCT. Institute of Hematology & Blood Diseases Hospital, China. 2025. ClinicalTrials.gov Identifier: NCT06783790

23. (NCT07028073 chunk 2): Chen Suning. A New Treatment of Newly Diagnosed KIT Mutation CBF-Acute Myeloid Leukemia. The First Affiliated Hospital of Soochow University. 2025. ClinicalTrials.gov Identifier: NCT07028073

24. (kreissig2023decipheringacutemyeloid pages 12-13): Sophie Kreissig, Roland Windisch, and Christian Wichmann. Deciphering acute myeloid leukemia associated transcription factors in human primary cd34+ hematopoietic stem/progenitor cells. Cells, 13:78, Dec 2023. URL: https://doi.org/10.3390/cells13010078, doi:10.3390/cells13010078. This article has 1 citations.

25. (qin2022comprehensivemutationprofile pages 7-8): Wei Qin, Xiayu Chen, Hong Jie Shen, Zheng Wang, Xiaohui Cai, Naike Jiang, and Haiying Hua. Comprehensive mutation profile in acute myeloid leukemia patients with runx1-runx1t1 or cbfb-myh11 fusions. Turkish Journal of Hematology, 39:84-93, Apr 2022. URL: https://doi.org/10.4274/tjh.galenos.2022.2021.0641, doi:10.4274/tjh.galenos.2022.2021.0641. This article has 11 citations.

26. (george2023therapyrelatedcorebinding pages 10-11): Binsah George, Binoy Yohannan, Virginia Mohlere, and Anneliese Gonzalez. Therapy-related core binding factor acute myeloid leukemia. International Journal of Hematologic Oncology, Feb 2023. URL: https://doi.org/10.2217/ijh-2022-0004, doi:10.2217/ijh-2022-0004. This article has 8 citations.

27. (zhang2023efficacyofvenetoclax pages 2-3): Keyuan Zhang, Xiang Zhang, Yang Xu, Shengli Xue, Huiying Qiu, Xiaowen Tang, Yue Han, Suning Chen, Aining Sun, Yanming Zhang, Depei Wu, and Ying Wang. Efficacy of venetoclax combined with hypomethylating agents in young, and unfit patients with newly diagnosed core binding factor acute myeloid leukemia. Blood Cancer Journal, Oct 2023. URL: https://doi.org/10.1038/s41408-023-00928-1, doi:10.1038/s41408-023-00928-1. This article has 32 citations and is from a domain leading peer-reviewed journal.

28. (zhang2023efficacyofvenetoclax pages 3-4): Keyuan Zhang, Xiang Zhang, Yang Xu, Shengli Xue, Huiying Qiu, Xiaowen Tang, Yue Han, Suning Chen, Aining Sun, Yanming Zhang, Depei Wu, and Ying Wang. Efficacy of venetoclax combined with hypomethylating agents in young, and unfit patients with newly diagnosed core binding factor acute myeloid leukemia. Blood Cancer Journal, Oct 2023. URL: https://doi.org/10.1038/s41408-023-00928-1, doi:10.1038/s41408-023-00928-1. This article has 32 citations and is from a domain leading peer-reviewed journal.

29. (day2024proteogenomicanalysisreveals pages 18-18): Ryan B. Day, Julia A. Hickman, Ziheng Xu, Casey D.S. Katerndahl, Francesca Ferraro, Sai Mukund Ramakrishnan, Petra Erdmann-Gilmore, Robert W. Sprung, Yiling Mi, R. Reid Townsend, Christopher A. Miller, and Timothy J. Ley. Proteogenomic analysis reveals cytoplasmic sequestration of runx1 by the acute myeloid leukemia–initiating cbfb::myh11 oncofusion protein. Journal of Clinical Investigation, Dec 2024. URL: https://doi.org/10.1172/jci176311, doi:10.1172/jci176311. This article has 14 citations and is from a highest quality peer-reviewed journal.

30. (kanellou2023deregulatedgeneexpression pages 16-17): Peggy Kanellou, Ilias Georgakopoulos-Soares, and Apostolos Zaravinos. Deregulated gene expression profiles and regulatory networks in adult and pediatric runx1/runx1t1-positive aml patients. Cancers, 15:1795, Mar 2023. URL: https://doi.org/10.3390/cancers15061795, doi:10.3390/cancers15061795. This article has 9 citations.
