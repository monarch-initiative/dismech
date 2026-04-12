---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T16:57:34.033848'
end_time: '2026-04-05T17:13:30.836719'
duration_seconds: 956.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Myeloid Leukemia, IDH-Mutated
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 63
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Myeloid Leukemia, IDH-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, IDH-Mutated** covering all of the
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
- **Disease Name:** Acute Myeloid Leukemia, IDH-Mutated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia, IDH-Mutated** covering all of the
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


# Disease Characteristics Research Report: Acute Myeloid Leukemia, IDH‑Mutated

## Target Disease
- **Disease name:** Acute myeloid leukemia (AML) with *IDH1* or *IDH2* mutation (“IDH‑mutated AML”). (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)
- **Category:** Hematologic malignancy (myeloid neoplasm) arising from clonal expansion of immature myeloid blasts. (shimony2023acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)
- **MONDO ID / OMIM / Orphanet / MeSH / ICD-10/ICD-11:** Not retrieved from the available sources in this tool run; below identifiers therefore cannot be asserted with citations.
- **Common synonyms/alternative names:** *IDH1-mutated AML*, *IDH2-mutated AML*, AML with *IDH1 R132* mutation, AML with *IDH2 R140/R172* mutation. (ivanov2024moleculartargetingof pages 2-4, fruchtman2024managementofisocitrate pages 1-2)
- **Evidence source types used here:** peer‑reviewed reviews (2023–2024 emphasized), clinical trial reports and FDA analyses, transplant cohort studies (2023–2024), pharmacovigilance (2024), and experimental model papers (mouse/zebrafish/human HSPCs). (fruchtman2024managementofisocitrate pages 1-2, norsworthy2020differentiationsyndromewith pages 3-4, wang2023transgenicidh2r172kand pages 1-2, pierangeli2024theleukemicisocitrate pages 1-2, peng2024arealworldstudy pages 1-2)

## 1. Disease Information (overview; “what is the disease?”)
AML is an aggressive marrow/blood cancer characterized by clonal proliferation of malignant hematopoietic blasts leading to marrow failure, commonly presenting with anemia, infections, and bleeding due to cytopenias. (shimony2023acutemyeloidleukemia pages 1-2, premnath2023paradigmshiftin pages 1-2)

“IDH‑mutated AML” refers to AML cases harboring somatic hotspot missense mutations in *IDH1* or *IDH2* that drive malignant transformation via production of the oncometabolite (R/D)-2‑hydroxyglutarate (2‑HG) and downstream epigenetic dysregulation and impaired myeloid differentiation. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

### Classification context (WHO/ICC; blast thresholds)
Recent AML classification systems emphasize molecular genetics.
- WHO (2022 revision) generally retains a **20% blast threshold** for AML but includes exceptions for some genetically defined AMLs. (shimony2023acutemyeloidleukemia pages 1-2)
- ICC (2022) allows genetically defined AML diagnoses at **≥10% blasts** for select genetic lesions and introduces an **MDS/AML** category for 10–19% blasts. (shimony2023acutemyeloidleukemia pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors (genetic/mechanistic)
The defining causal factor is **somatic gain‑of‑function (“neomorphic”) mutation** in *IDH1* or *IDH2* in leukemic cells. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

**Hotspot residues / pathogenic variants**
- *IDH1*: mutations cluster at **R132** (e.g., R132H, R132C, R132L, R132S, R132G). (ivanov2024moleculartargetingof pages 2-4, issa2021acutemyeloidleukemia pages 1-2)
- *IDH2*: mutations cluster at **R140** and **R172** (notably R140Q and R172K). (ivanov2024moleculartargetingof pages 2-4, fruchtman2024managementofisocitrate pages 1-2)

**Frequency in AML**
- Across reviews, IDH mutations are reported in ~**14–20%** of AML overall. (fruchtman2024managementofisocitrate pages 1-2)
- One treatment‑algorithm review reports an approximate breakdown of **~8% *IDH1*** and **~12% *IDH2*** among AML. (issa2021acutemyeloidleukemia pages 1-2)

### 2.2 Risk factors
No *IDH‑specific* environmental risk factors were identified in the retrieved sources for this run. Epidemiologically, AML overall is strongly age‑associated (median age ~68–70), which indirectly enriches for IDH‑mutated cases because IDH mutations are frequently found in older AML populations. (fruchtman2024managementofisocitrate pages 1-2, kantarjian2024currentstatusand pages 1-2)

### 2.3 Protective factors
No IDH‑specific protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
Not identified in retrieved sources for IDH‑mutated AML specifically.

## 3. Phenotypes
### 3.1 Core clinical phenotypes (human)
AML commonly presents with symptoms and signs driven by bone‑marrow failure:
- **Anemia** → fatigue, shortness of breath (HPO suggestion: **HP:0001903 Anemia**, **HP:0012378 Fatigue**, **HP:0002094 Dyspnea**). (premnath2023paradigmshiftin pages 1-2, bill2024impactofidh1 pages 1-6)
- **Neutropenia/immune dysfunction** → fever/infection (HPO: **HP:0002719 Recurrent infections**, **HP:0001945 Fever**). (premnath2023paradigmshiftin pages 1-2, bill2024impactofidh1 pages 1-6)
- **Thrombocytopenia** → bleeding/petechiae (HPO: **HP:0001873 Thrombocytopenia**, **HP:0000967 Petechiae**, **HP:0001892 Bleeding**). (bill2024impactofidh1 pages 1-6)

A representative case in a 2023 AML review illustrates typical cytopenias and blast burden (Hb 7.5 g/dL, WBC 2.3×10^9/L, platelets 27×10^9/L; 22% marrow myeloblasts). (shimony2023acutemyeloidleukemia pages 1-2)

### 3.2 Treatment‑emergent phenotype: IDH‑inhibitor differentiation syndrome (IDH‑DS)
IDH inhibitors can induce a differentiation syndrome characterized by systemic inflammatory/capillary leak manifestations. In an FDA systematic analysis of relapsed/refractory AML trials, adjudicated differentiation syndrome occurred in **19%** of patients treated with ivosidenib and **19%** with enasidenib; **median onset ~20 and 19 days**, respectively; and fatal cases occurred (**6% and 5%** among DS cases, respectively). (norsworthy2020differentiationsyndromewith pages 3-4)

Clinical manifestations used for case identification include dyspnea, unexplained fever, weight gain, hypotension, acute renal failure, and pulmonary infiltrates/pleuropericardial effusion. (norsworthy2020differentiationsyndromewith pages 3-4)

**Phenotype ontology suggestion for DS manifestations:**
- **HP:0002094 Dyspnea**, **HP:0001945 Fever**, **HP:0004325 Weight gain**, **HP:0002615 Hypotension**, **HP:0001919 Acute kidney injury**, **HP:0002090 Pneumonia/Pulmonary infiltrates**, **HP:0000967 Edema**.

### 3.3 Functional/QOL impact proxies
Transfusion dependence is a major functional burden; IDH‑directed therapy can restore hematopoiesis. In enasidenib‑treated relapsed/refractory IDH2‑mutant AML, **43.1%** of RBC transfusion‑dependent patients and **40.2%** of platelet transfusion‑dependent patients achieved transfusion independence. (stein2019molecularremissionand pages 1-4)

## 4. Genetic/Molecular Information
### 4.1 Causal genes
- **IDH1** (cytosolic/peroxisomal enzyme) and **IDH2** (mitochondrial enzyme) are the defining mutated genes. (fruchtman2024managementofisocitrate pages 1-2)

### 4.2 Pathogenic variants (somatic)
Hotspots: *IDH1* R132; *IDH2* R140/R172. (ivanov2024moleculartargetingof pages 2-4, fruchtman2024managementofisocitrate pages 1-2)

Somatic origin is typical for AML; the retrieved sources characterize these as acquired driver mutations in leukemia. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

### 4.3 Co-mutations / modifier context
IDH mutational subgroups show distinct co-mutation patterns with clinical implications (e.g., *NPM1*, *DNMT3A*, and pathway mutations) and can influence response and resistance. (testa2020isocitratedehydrogenasemutations pages 17-19, lang2023mechanismsofresistance pages 5-7)

A clinically important modifier concept is that **IDH2 R140** can behave as a clonal hematopoiesis–like lesion in transplant MRD contexts, with high diagnostic VAF and frequent persistence not necessarily tracking relapse risk. (bill2023impactofidh1andidh2mutationdetection pages 4-5, bill2024impactofidh1 pages 26-30)

### 4.4 Epigenetic information
IDH mutations promote a hypermethylated state via inhibition of α‑KG–dependent enzymes (TET2 DNA demethylation; histone demethylases), providing a mechanistic basis for epigenetic dysregulation in IDH‑mut AML. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

## 5. Environmental Information
No IDH‑specific environmental contributors were identified in the retrieved sources for this run.

## 6. Mechanism / Pathophysiology (causal chain)
### 6.1 Central oncometabolite mechanism
Mutant IDH enzymes lose normal catalytic behavior and acquire neomorphic activity converting α‑ketoglutarate into **2‑hydroxyglutarate (2‑HG)**. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

Accumulated 2‑HG competitively inhibits α‑KG–dependent dioxygenases (including **TET2** and histone demethylases), producing DNA/histone hypermethylation and enforcing a **myeloid differentiation block** that promotes leukemogenesis. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2)

### 6.2 Additional downstream mechanisms (selected)
- **DNA repair and genomic stability:** 2‑HG can inhibit DNA repair enzymes and contribute to genetic instability. (fruchtman2024managementofisocitrate pages 1-2)
- **BCL‑2 dependence:** IDH‑mutant cells show enhanced BCL‑2 dependence, providing biological rationale for venetoclax sensitivity. (nong2024commondrivermutations pages 7-8)

### 6.3 Model evidence supporting causality and reversibility
- **Primary human CD34+ HSPCs:** In a 2024 study modeling IDH mutants in normal HSPCs, “**CFU ability was dramatically compromised with a complete trilineage block of differentiation**,” and “**the block was reversed by specific inhibitors**,” supporting a direct causal effect and pharmacologic reversibility. (pierangeli2024theleukemicisocitrate pages 1-2)
- **Zebrafish AML models (IDH2R140Q or IDH2R172K + FLT3‑ITD):** adults developed leukemia with myeloid skewing, differentiation blockade, and transplantable disease; leukemic phenotypes were ameliorated by **enasidenib** (and quizartinib in combination). (wang2023transgenicidh2r172kand pages 1-2, wang2023transgenicidh2r172kand pages 4-7)
- **Mouse models:** inducible IDH2R140Q cooperates with other lesions (e.g., HOXA9/MEIS1a, FLT3) in vivo and deinduction of mutant IDH2 affects leukemia maintenance, consistent with a driver/maintenance role. (kats2014protooncogenicroleof pages 1-3)

### Suggested ontology terms
- **GO Biological Process:** hematopoietic cell differentiation; myeloid cell differentiation; regulation of DNA methylation; histone demethylation; cellular response to hypoxia/pseudohypoxia; regulation of apoptotic process (BCL‑2 dependence).
- **Cell Ontology (CL):** hematopoietic stem cell (HSC); hematopoietic progenitor cell; myeloblast; granulocyte–monocyte progenitor.

## 7. Anatomical Structures Affected
### Organ/tissue level
- **Primary site:** bone marrow hematopoiesis (UBERON suggestion: **UBERON:0002371 bone marrow**). (shimony2023acutemyeloidleukemia pages 1-2, bill2024impactofidh1 pages 1-6)
- **Peripheral blood involvement:** circulating blasts/cytopenias (UBERON: blood). (shimony2023acutemyeloidleukemia pages 1-2)
- **Secondary organ involvement:** splenomegaly is a prominent feature in AML models (and clinically can occur) (UBERON: spleen). (wang2023transgenicidh2r172kand pages 1-2)

### Cell/subcellular localization
- Leukemic clone arises from hematopoietic stem/progenitor compartments and produces immature myeloid blasts (CL: HSPC, myeloblast). (wang2023transgenicidh2r172kand pages 1-2, pierangeli2024theleukemicisocitrate pages 1-2)
- Subcellular: IDH1 is cytosolic/peroxisomal; IDH2 is mitochondrial (GO Cellular Component suggestions: cytosol/peroxisome/mitochondrion). (fruchtman2024managementofisocitrate pages 1-2)

## 8. Temporal Development
AML often has an acute/subacute presentation due to rapid marrow failure with symptomatic cytopenias. (premnath2023paradigmshiftin pages 1-2)

IDH inhibitor responses can take weeks and reflect differentiation rather than immediate cytotoxicity; in an ivosidenib trial summary the **median time to response** was ~**1.9 months**. (fruchtman2024managementofisocitrate pages 3-4)

## 9. Inheritance and Population
### 9.1 Epidemiology (AML overall; IDH‑mut AML subset frequency)
- AML overall incidence reported as **4.0 per 100,000**; age‑adjusted incidence higher in older adults (e.g., 18.8 per 100,000 in the elderly vs 4.9 per 100,000 in ages 50–64, per one 2024 review). (fruchtman2024managementofisocitrate pages 1-2)
- US AML is primarily a disease of older adults (median age 68–70). (kantarjian2024currentstatusand pages 1-2, premnath2023paradigmshiftin pages 1-2)
- IDH1/2 mutations together occur in ~**14–20%** of AML in reviews. (fruchtman2024managementofisocitrate pages 1-2)

### 9.2 Survival statistics (AML overall)
- A 2024 review reports 5‑year survival improved from **9% (1980)** to **27% (2017)**. (fruchtman2024managementofisocitrate pages 1-2)
- A 2023 review reports overall 5‑year survival **30.5%** for US cases diagnosed 2012–2018. (premnath2023paradigmshiftin pages 1-2)

## 10. Diagnostics
### 10.1 Clinical diagnosis
Diagnosis involves peripheral blood and bone marrow evaluation and includes morphology, immunophenotyping (flow cytometry), cytogenetics, and molecular testing; blast thresholds depend on WHO vs ICC (Section 1). (bill2024impactofidh1 pages 1-6, shimony2023acutemyeloidleukemia pages 1-2)

### 10.2 Molecular diagnostics for IDH mutations
- IDH1/2 mutations are typically detected by targeted sequencing panels (NGS) and/or hotspot assays (PCR/ddPCR), often on bone marrow samples in AML workups. (bill2024impactofidh1 pages 1-6, bill2023impactofidh1andidh2mutationdetection pages 1-2)
- In a transplant cohort study, diagnostic IDH mutation testing included exon 4 sequencing and NGS verification; the authors note NGS technical sensitivity of **~3% VAF**, motivating hotspot **ddPCR** assays for MRD-level detection. (bill2023impactofidh1andidh2mutationdetection pages 1-2)

**IHC limitations:** A 2024 review notes IDH1 R132H IHC can miss non‑R132H variants and may have ~5–10% false positives, thus molecular testing is often required. (ivanov2024moleculartargetingof pages 2-4)

### 10.3 MRD approaches (IDH-specific nuance)
Evidence supports variant‑specific interpretation of persistent IDH mutations:
- In a 2023 HSCT cohort, IDH MRD by ddPCR was common at HSCT (75%); persistence of **IDH1 R132** or **IDH2 R172** was associated with relapse risk, while persistent **IDH2 R140** (often high VAF) was less predictive and may reflect clonal hematopoiesis. (bill2023impactofidh1andidh2mutationdetection pages 4-5, bill2024impactofidh1 pages 26-30)
- A 2024 cohort (non‑myeloablative alloHCT with PTCy) found **no significant association** between persistent IDH mutations pre‑alloHCT and 3‑year outcomes, illustrating current uncertainty and the need for standardized thresholds and variant‑aware interpretation. (ravindra2024persistentidhmutations pages 1-4)

## 11. Outcome/Prognosis
Prognosis in AML is strongly age‑dependent and risk‑stratified by genetics and MRD; older adults historically have poor outcomes even with intensive therapy (e.g., median survival ~9 months and 5‑year survival ≤10% for >60 treated with 7+3 in one 2024 review). (kantarjian2024currentstatusand pages 1-2)

IDH mutation prognostic impact is context‑dependent (co-mutations and variant specifics), and current sources emphasize using broader molecular risk frameworks (e.g., ELN‑style risk) rather than treating IDH mutation alone as a definitive prognostic class. (bill2024impactofidh1 pages 9-13)

## 12. Treatment
### 12.1 Targeted therapies (approved)
**IDH1 inhibitors**
- **Ivosidenib**: in newly diagnosed IDH1‑mutant AML (subgroup, n=34) a 2024 review reports **CR 30.3%**, **CR/CRh 42.4%**, **median OS 12.6 months**; differentiation syndrome occurred **18%** (9% grade ≥3). (fruchtman2024managementofisocitrate pages 4-5)

**IDH2 inhibitors**
- **Enasidenib**: pivotal phase I/II program in relapsed/refractory IDH2‑mutant AML reported **ORR 38.8%**, **CR 19.6%**, **median OS 8.8 months**; grade 3–4 AEs included hyperbilirubinemia 10%, thrombocytopenia 7%, and differentiation syndrome 6%. (stein2019molecularremissionand pages 1-4)

### 12.2 Combination regimens and real‑world implementation
**Ivosidenib + azacitidine (frontline older/unfit; AGILE context)**
- A health‑economic analysis summarizes that in the randomized AGILE trial, ivosidenib+azacitidine improved event‑free survival (HR 0.33) and overall survival (HR 0.44) vs placebo+azacitidine in newly diagnosed older/unfit IDH1‑mutant AML. (bewersdorf2023costeffectivenessofazacitidine pages 1-2)

**Venetoclax + azacitidine (widely used low‑intensity backbone; IDH‑mut subset efficacy)**
- In pooled phase Ib/III analyses of treatment‑naïve, intensive‑ineligible AML, IDH1/2‑mutant patients had **CRc 79% vs 11%** (Ven+Aza vs Aza), **median OS 24.5 vs 6.2 months**, and **median duration of remission 29.5 vs 9.5 months**. (pollyea2022impactofvenetoclax pages 1-2)
- Subgroups: IDH1‑mutant CRc 66.7% (mOS 15.2 months) and IDH2‑mutant CRc 86.0% (mOS not reached). (pollyea2022impactofvenetoclax pages 1-2, pollyea2022impactofvenetoclax pages 5-5)

**Adverse events with Ven+Aza in IDH‑mut AML:** febrile neutropenia 42.0%, infections 59.3%, pneumonia 27.2%, grade ≥3 AEs 97.5% (in the cited excerpt). (pollyea2022impactofvenetoclax pages 6-7)

### 12.3 Safety: differentiation syndrome management (expert guidance)
A 2024 review outlines DS pathophysiology and management: prompt respiratory support and corticosteroids (dexamethasone 10 mg IV twice daily) with treatment interruption for severe cases. (fruchtman2024managementofisocitrate pages 3-4)

The FDA analysis describes an operational case‑finding algorithm and recommends dexamethasone 10 mg IV q12h until symptoms resolve (≥3 days), plus cytoreduction/supportive measures (hydroxyurea, diuretics, leukapheresis as needed). (norsworthy2020differentiationsyndromewith pages 3-4)

### 12.4 Post‑transplant / maintenance
Enasidenib has been studied as post‑alloHCT maintenance; the **visual summary** of a phase I study indicates no reported differentiation syndrome and provides relapse/survival curves and grade ≥3 AE tables. (fathi2022enasidenibasmaintenance media a35fe258, fathi2022enasidenibasmaintenance media 3bab0af4, fathi2022enasidenibasmaintenance media c85d33dd)

### 12.5 Ongoing clinical trials (selected; ClinicalTrials.gov)
- **NCT03839771 (HOVON150AML)**: Phase 3, randomized, placebo‑controlled trial adding ivosidenib (IDH1) or enasidenib (IDH2) to intensive induction/consolidation followed by up to 2 years maintenance; endpoints include EFS/OS/MRD‑negative CR and QoL. (NCT03839771 chunk 1)
- **NCT06387069 (RAPHAEL)**: Phase 3, relapsed/refractory IDH1/2‑mutant AML; HMPL‑306 monotherapy vs salvage chemo; cohorts by IDH1 R132 vs IDH2 R140/R172; recruiting. (NCT06387069 chunk 1)
- **NCT04603001**: Phase 1 covalent IDH inhibitor LY3410738; includes dose‑escalation triplet arm with venetoclax + azacitidine; active not recruiting. (NCT04603001 chunk 1)
- **NCT05401097 (I‑DATA)**: Phase 2 sequencing study comparing IDH inhibitor + azacitidine first vs venetoclax + azacitidine first in newly diagnosed IDH‑mut AML unfit for intensive therapy; recruiting. (NCT05401097 chunk 1)

### Suggested MAXO terms (treatment actions)
- **Small molecule therapy**, **targeted therapy**, **hypomethylating agent therapy**, **BCL2 inhibitor therapy**, **allogeneic hematopoietic stem cell transplantation**, **supportive care (transfusion support, antimicrobial therapy)**.

## 13. Prevention
### Primary prevention
No established primary prevention strategy specific to IDH‑mutated AML was identified in the retrieved sources.

### Secondary/tertiary prevention
- **Secondary prevention** relies on early recognition of cytopenias and prompt diagnostic evaluation with modern molecular profiling (WHO/ICC emphasize molecular integration). (shimony2023acutemyeloidleukemia pages 1-2)
- **Tertiary prevention** includes proactive management of infections/cytopenias and vigilance for differentiation syndrome during IDH inhibitor therapy (steroid protocols and supportive care). (fruchtman2024managementofisocitrate pages 3-4, norsworthy2020differentiationsyndromewith pages 3-4)

## 14. Other Species / Natural Disease
Not established as a naturally occurring veterinary disease entity in retrieved sources; experimental animal models are described below.

## 15. Model Organisms
### Zebrafish
Transgenic IDH2R140Q and IDH2R172K zebrafish (often combined with FLT3‑ITD) develop AML‑like disease with differentiation blockade, splenomegaly, transplantability to recipients, and therapeutic response to enasidenib. (wang2023transgenicidh2r172kand pages 1-2, wang2023transgenicidh2r172kand pages 4-7)

### Mouse
Inducible/tissue‑specific IDH2R140Q models cooperate with other lesions to drive acute leukemia and show that deinduction of mutant IDH2 impairs leukemia maintenance. (kats2014protooncogenicroleof pages 1-3)

### Primary human HSPCs
Human CD34+ HSPC experimental systems show direct differentiation blockade by IDH mutants with inhibitor reversibility (“complete trilineage block of differentiation” reversed by specific inhibitors). (pierangeli2024theleukemicisocitrate pages 1-2)

## 16. Real‑world implementation / pharmacovigilance (2024)
A 2024 pharmacovigilance analysis using WHO VigiAccess reported **4,072** adverse event reports for enasidenib and ivosidenib combined (2,776 for enasidenib; 1,296 for ivosidenib). Top reported events included off‑label use, death, fatigue, nausea, diarrhea, AML, drug ineffective, differentiation syndrome, and decreased platelet count. (peng2024arealworldstudy pages 1-2, peng2024arealworldstudy pages 4-6)

## Evidence summary table
The following table consolidates high‑yield, evidence‑backed facts (definitions, mechanisms, epidemiology, and treatment outcomes) with DOI URLs:

| Topic | Key finding with quantitative values where available | Source (first author, journal, year) | Publication date (month/year) | PMID | DOI URL |
|---|---|---|---|---|---|
| Definition | IDH-mutated AML is AML with somatic IDH1/IDH2 mutations that generate the oncometabolite 2-HG, causing epigenetic dysregulation and impaired myeloid differentiation; IDH1/2 mutations occur in roughly ~20% of AML overall. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2) | Issa, Blood Cancer Journal, 2021 | 06/2021 |  | https://doi.org/10.1038/s41408-021-00497-1 |
| Mutation hotspots | Hotspot substitutions occur almost exclusively at IDH1 R132 and IDH2 R140/R172; common variants include IDH1 R132H/R132C and IDH2 R140Q/R172K. (ivanov2024moleculartargetingof pages 2-4, fruchtman2024managementofisocitrate pages 1-2) | Ivanov, Int J Mol Sci, 2024 | 07/2024 |  | https://doi.org/10.3390/ijms25137337 |
| Prevalence in AML | Reviews report IDH mutations in ~14–20% of AML; one treatment algorithm reports ~8% IDH1 and ~12% IDH2. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2) | Fruchtman, Leukemia, 2024 | 04/2024 |  | https://doi.org/10.1038/s41375-024-02246-2 |
| Mechanism / pathophysiology | Mutant IDH converts α-ketoglutarate to R-2-hydroxyglutarate, which inhibits α-KG–dependent enzymes including TET2 and JmjC histone demethylases, producing DNA/histone hypermethylation and a differentiation block. (issa2021acutemyeloidleukemia pages 1-2, fruchtman2024managementofisocitrate pages 1-2, cerchione2021idh1idh2inhibitionin pages 1-2) | Cerchione, Front Oncol, 2021 | 03/2021 |  | https://doi.org/10.3389/fonc.2021.639387 |
| AML clinical presentation | AML commonly presents with cytopenia-related anemia, infection, and bleeding; an example 2023 review case showed pancytopenia with hemoglobin 7.5 g/dL, WBC 2.3×10^9/L, platelets 27×10^9/L, and 22% marrow myeloblasts. (bill2024impactofidh1 pages 1-6, shimony2023acutemyeloidleukemia pages 1-2) | Shimony, Am J Hematol, 2023 | 01/2023 |  | https://doi.org/10.1002/ajh.26822 |
| Classification thresholds (WHO/ICC) | WHO 2022 generally retains ≥20% blasts for AML, with no minimum for some genetically defined AML entities; ICC 2022 allows ≥10% blasts for genetically defined AML (except BCR::ABL1 requiring ≥20%) and introduces an MDS/AML category for 10–19% blasts. (shimony2023acutemyeloidleukemia pages 1-2, shimony2023acutemyeloidleukemia pages 5-6) | Shimony, Am J Hematol, 2023 | 01/2023 |  | https://doi.org/10.1002/ajh.26822 |
| Epidemiology / age distribution | AML overall incidence is reported as 4.0 per 100,000; age-adjusted incidence is 18.8 per 100,000 in older adults vs 4.9 per 100,000 in those aged 50–64; median age at diagnosis is ~68 years. (fruchtman2024managementofisocitrate pages 1-2, premnath2023paradigmshiftin pages 1-2) | Fruchtman, Leukemia, 2024 | 04/2024 |  | https://doi.org/10.1038/s41375-024-02246-2 |
| Survival statistics | AML 5-year survival improved from 9% in 1980 to 27% in 2017 in one review; another 2023 review reports overall 5-year survival 30.5% for 2012–2018 US cases. (fruchtman2024managementofisocitrate pages 1-2, premnath2023paradigmshiftin pages 1-2) | Premnath, Cancers, 2023 | 05/2023 |  | https://doi.org/10.3390/cancers15113002 |
| Older-adult outcomes | Older adults have substantially worse outcomes: one 2024 review states fit patients >60 years treated with intensive 7+3 have median survival ~9 months and 5-year survival ≤10%; before HMA-based therapy, older/unfit patients often had median survival 2–6 months. (kantarjian2024currentstatusand pages 1-2) | Kantarjian, Blood Cancer Journal, 2024 | 09/2024 |  | https://doi.org/10.1038/s41408-024-01143-2 |
| Ivosidenib monotherapy (newly diagnosed IDH1-mutant AML) | In newly diagnosed IDH1-mutant AML, ivosidenib monotherapy produced CR 30.3%, CR/CRh 42.4%, median OS 12.6 months; differentiation syndrome occurred in 18% (9% grade ≥3). (fruchtman2024managementofisocitrate pages 4-5) | Fruchtman, Leukemia, 2024 | 04/2024 |  | https://doi.org/10.1038/s41375-024-02246-2 |
| Ivosidenib + azacitidine (AGILE context) | In AGILE, ivosidenib + azacitidine significantly improved event-free survival (HR 0.33, 95% CI 0.16–0.69) and overall survival (HR 0.44, 95% CI 0.27–0.73) vs azacitidine alone in newly diagnosed older/ineligible IDH1-mutant AML. (bewersdorf2023costeffectivenessofazacitidine pages 1-2) | Bewersdorf, Leuk Lymphoma, 2023 | 12/2023 |  | https://doi.org/10.1080/10428194.2022.2140288 |
| Ivosidenib triplet / early combination data | A phase 1b study of ivosidenib + azacitidine in 23 newly diagnosed patients reported ORR 78.3% and CR 60.9%. (fruchtman2024managementofisocitrate pages 4-5) | Fruchtman, Leukemia, 2024 | 04/2024 |  | https://doi.org/10.1038/s41375-024-02246-2 |
| Enasidenib monotherapy (R/R IDH2-mutant AML) | In relapsed/refractory IDH2-mutant AML, enasidenib monotherapy achieved ORR 38.8% (95% CI 32.2–45.7), CR 19.6%, median OS 8.8 months; grade 3–4 treatment-related hyperbilirubinemia 10%, thrombocytopenia 7%, IDH differentiation syndrome 6%. (stein2019molecularremissionand pages 1-4) | Stein, Blood, 2019 | 02/2019 |  | https://doi.org/10.1182/blood-2018-08-869008 |
| Pooled outcomes for IDH inhibitors | A 2023 meta-analysis of 1,109 patients reported pooled outcomes for newly diagnosed IDH-mutated AML: CR 47%, ORR 65%, 2-year OS 45%; for R/R disease: CR 21%, ORR 40%, 2-year OS 15%, median OS 8.21 months, median EFS 4.73 months. (chen2023efficacyandsafety pages 6-8) | Chen, Clinical Epigenetics, 2023 | 07/2023 |  | https://doi.org/10.1186/s13148-023-01529-2 |
| Differentiation syndrome (FDA systematic analysis) | FDA adjudicated differentiation syndrome in 19% of ivosidenib-treated and 19% of enasidenib-treated R/R AML patients; median onset was 20 days for ivosidenib and 19 days for enasidenib; grade ≥3 reactions occurred in 68% and 66%, and fatal cases in 6% and 5%, respectively. (norsworthy2020differentiationsyndromewith pages 3-4) | Norsworthy, Clin Cancer Res, 2020 | 08/2020 |  | https://doi.org/10.1158/1078-0432.CCR-20-0834 |
| MRD / molecular monitoring | Persistent IDH mutations in remission can have prognostic value, but interpretation is variant-specific: IDH1/2 VAF >2.5% at day 30 was associated with short EFS; IDH1/2 VAF <0.2% after induction predicted longer DFS in reported cohorts. (testa2020isocitratedehydrogenasemutations pages 17-19) | Testa, Cancers, 2020 | 08/2020 |  | https://doi.org/10.3390/cancers12092427 |
| Post-transplant monitoring | In AML patients undergoing HSCT, diagnostic IDH mutation status did not significantly influence outcomes, but IDH1 R132 and IDH2 R172 positivity at HSCT was associated with inferior outcomes; IDH2 R140 was less informative and may behave more like clonal hematopoiesis. (bill2024impactofidh1 pages 1-6, bill2024impactofidh1 pages 9-13) | Bill, Blood Advances, 2023 | 02/2023 |  | https://doi.org/10.1182/bloodadvances.2021005789 |
| Resistance mechanisms | Resistance to IDH inhibitors includes second-site IDH mutations, isoform switching (IDH1↔IDH2), co-occurring RTK/RAS/FLT3 pathway mutations, clonal evolution, and stemness/epigenetic programs; these data support rational combinations such as IDH inhibitor + HMA and IDH inhibitor + venetoclax. (lang2023mechanismsofresistance pages 5-7, issa2021acutemyeloidleukemia pages 5-6, nong2024commondrivermutations pages 8-10) | Lang, Cancers, 2023 | 09/2023 |  | https://doi.org/10.3390/cancers15184573 |
| Real-world / implementation note | Enasidenib maintenance after allo-HCT showed survival and safety data in a phase I study, with no cases of differentiation syndrome reported in the visual summary. (fathi2022enasidenibasmaintenance media a35fe258) | Fathi, Blood Advances, 2022 | 11/2022 |  | https://doi.org/10.1182/bloodadvances.2022008632 |


*Table: This table summarizes high-yield, evidence-backed facts for IDH-mutated acute myeloid leukemia, including disease definition, genetics, mechanisms, classification, outcomes, therapies, toxicity, MRD, and epidemiology. It is designed for rapid reuse in a structured disease knowledge base.*

## Notes on evidence gaps
- Formal disease identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) were not retrieved in this run, so no identifier assertions are made.
- Some key trial-level details (e.g., full AGILE response and toxicity tables) were not directly available in the gathered full text snippets; the report therefore cites secondary summaries where necessary (and flags this limitation). (bewersdorf2023costeffectivenessofazacitidine pages 1-2)
- MRD utility of IDH mutations remains variant‑ and setting‑dependent, with conflicting 2023–2024 cohort conclusions; this uncertainty should be encoded in knowledge base assertions as context‑dependent. (ravindra2024persistentidhmutations pages 1-4, bill2023impactofidh1andidh2mutationdetection pages 4-5)


References

1. (issa2021acutemyeloidleukemia pages 1-2): Ghayas C. Issa and Courtney D. DiNardo. Acute myeloid leukemia with idh1 and idh2 mutations: 2021 treatment algorithm. Blood Cancer Journal, Jun 2021. URL: https://doi.org/10.1038/s41408-021-00497-1, doi:10.1038/s41408-021-00497-1. This article has 210 citations and is from a domain leading peer-reviewed journal.

2. (fruchtman2024managementofisocitrate pages 1-2): Harry Fruchtman, Zachary M. Avigan, Julian A. Waksal, Nicole Brennan, and John O. Mascarenhas. Management of isocitrate dehydrogenase 1/2 mutated acute myeloid leukemia. Leukemia, 38:927-935, Apr 2024. URL: https://doi.org/10.1038/s41375-024-02246-2, doi:10.1038/s41375-024-02246-2. This article has 41 citations and is from a highest quality peer-reviewed journal.

3. (shimony2023acutemyeloidleukemia pages 1-2): Shai Shimony, Maximilian Stahl, and Richard M. Stone. Acute myeloid leukemia: 2023 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:502-526, Jan 2023. URL: https://doi.org/10.1002/ajh.26822, doi:10.1002/ajh.26822. This article has 524 citations and is from a domain leading peer-reviewed journal.

4. (ivanov2024moleculartargetingof pages 2-4): Stanislav Ivanov, Olger Nano, Caroline Hana, Amalia Bonano-Rios, and Atif Hussein. Molecular targeting of the isocitrate dehydrogenase pathway and the implications for cancer therapy. International Journal of Molecular Sciences, 25:7337, Jul 2024. URL: https://doi.org/10.3390/ijms25137337, doi:10.3390/ijms25137337. This article has 21 citations.

5. (norsworthy2020differentiationsyndromewith pages 3-4): Kelly J. Norsworthy, Flora Mulkey, Emma C. Scott, Ashley F. Ward, Donna Przepiorka, Rosane Charlab, Sarah E. Dorff, Albert Deisseroth, Dickran Kazandjian, Rajeshwari Sridhara, Julia A. Beaver, Ann T. Farrell, R. Angelo de Claro, and Richard Pazdur. Differentiation syndrome with ivosidenib and enasidenib treatment in patients with relapsed or refractory idh-mutated aml: a u.s. food and drug administration systematic analysis. Clinical Cancer Research, 26:4280-4288, Aug 2020. URL: https://doi.org/10.1158/1078-0432.ccr-20-0834, doi:10.1158/1078-0432.ccr-20-0834. This article has 115 citations and is from a highest quality peer-reviewed journal.

6. (wang2023transgenicidh2r172kand pages 1-2): Dandan Wang, Lichuan Zheng, Bowie Yik Ling Cheng, Chun-Fung Sin, Runsheng Li, Sze Pui Tsui, Xinyu Yi, Alvin Chun Hang Ma, Bai Liang He, Anskar Yu Hung Leung, and Xuan Sun. Transgenic idh2r172k and idh2r140q zebrafish models recapitulated features of human acute myeloid leukemia. Oncogene, 42:1272-1281, Feb 2023. URL: https://doi.org/10.1038/s41388-023-02611-y, doi:10.1038/s41388-023-02611-y. This article has 14 citations and is from a domain leading peer-reviewed journal.

7. (pierangeli2024theleukemicisocitrate pages 1-2): Sara Pierangeli, Serena Donnini, Valerio Ciaurro, Francesca Milano, Valeria Cardinali, Sofia Sciabolacci, Gaetano Cimino, Ilaria Gionfriddo, Roberta Ranieri, Sabrina Cipriani, Eleonora Padiglioni, Roberta Iacucci Ostini, Tiziana Zei, Antonio Pierini, and Maria Paola Martelli. The leukemic isocitrate dehydrogenase (idh) 1/2 mutations impair myeloid and erythroid cell differentiation of primary human hematopoietic stem and progenitor cells (hspcs). Cancers, 16:2675, Jul 2024. URL: https://doi.org/10.3390/cancers16152675, doi:10.3390/cancers16152675. This article has 4 citations.

8. (peng2024arealworldstudy pages 1-2): Mengmeng Peng, Qian Guo, Zihan Dang, Baiquan Zhang, Manjuan Li, Zixuan Wang, Xuemian Lu, and Jie Lin. A real-world study of adverse drug reactions of two isocitrate dehydrogenase inhibitor based on the us fda adverse event reporting system and vigiaccess databases. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1489045, doi:10.3389/fphar.2024.1489045. This article has 3 citations.

9. (premnath2023paradigmshiftin pages 1-2): Naveen Premnath and Yazan F. Madanat. Paradigm shift in the management of acute myeloid leukemia—approved options in 2023. Cancers, 15:3002, May 2023. URL: https://doi.org/10.3390/cancers15113002, doi:10.3390/cancers15113002. This article has 13 citations.

10. (kantarjian2024currentstatusand pages 1-2): Hagop Kantarjian, Gautam Borthakur, Naval Daver, Courtney D. DiNardo, Ghayas Issa, Elias Jabbour, Tapan Kadia, Koji Sasaki, Nicholas J. Short, Musa Yilmaz, and Farhad Ravandi. Current status and research directions in acute myeloid leukemia. Blood Cancer Journal, Sep 2024. URL: https://doi.org/10.1038/s41408-024-01143-2, doi:10.1038/s41408-024-01143-2. This article has 113 citations and is from a domain leading peer-reviewed journal.

11. (bill2024impactofidh1 pages 1-6): M Bill. Impact of idh1 and idh2 mutation detection at diagnosis and in remission in acute myeloid leukemia patients receiving allogeneic transplantation. Unknown journal, 2024.

12. (stein2019molecularremissionand pages 1-4): Eytan M. Stein, Courtney D. DiNardo, Amir T. Fathi, Daniel A. Pollyea, Richard M. Stone, Jessica K. Altman, Gail J. Roboz, Manish R. Patel, Robert Collins, Ian W. Flinn, Mikkael A. Sekeres, Anthony S. Stein, Hagop M. Kantarjian, Ross L. Levine, Paresh Vyas, Kyle J. MacBeth, Alessandra Tosolini, Jason VanOostendorp, Qiang Xu, Ira Gupta, Thomas Lila, Alberto Risueno, Katharine E. Yen, Bin Wu, Eyal C. Attar, Martin S. Tallman, and Stéphane de Botton. Molecular remission and response patterns in patients with mutant-idh2 acute myeloid leukemia treated with enasidenib. Blood, 133 7:676-687, Feb 2019. URL: https://doi.org/10.1182/blood-2018-08-869008, doi:10.1182/blood-2018-08-869008. This article has 413 citations and is from a highest quality peer-reviewed journal.

13. (testa2020isocitratedehydrogenasemutations pages 17-19): Ugo Testa, Germana Castelli, and Elvira Pelosi. Isocitrate dehydrogenase mutations in myelodysplastic syndromes and in acute myeloid leukemias. Cancers, 12:2427, Aug 2020. URL: https://doi.org/10.3390/cancers12092427, doi:10.3390/cancers12092427. This article has 27 citations.

14. (lang2023mechanismsofresistance pages 5-7): Tonio Johannes Lukas Lang, Frederik Damm, Lars Bullinger, and Mareike Frick. Mechanisms of resistance to small molecules in acute myeloid leukemia. Cancers, 15:4573, Sep 2023. URL: https://doi.org/10.3390/cancers15184573, doi:10.3390/cancers15184573. This article has 13 citations.

15. (bill2023impactofidh1andidh2mutationdetection pages 4-5): Marius Bill, Madlen Jentzsch, Lara Bischof, Jessica Kohlschmidt, Juliane Grimm, Laura Katharina Schmalbrock, Donata Backhaus, Dominic Brauer, Karoline Goldmann, Georg-Nikolaus Franke, Vladan Vucinic, Dietger Niederwieser, Alice S. Mims, Uwe Platzbecker, Ann-Kathrin Eisfeld, and Sebastian Schwind. Impact of<i>idh1</i>and<i>idh2</i>mutation detection at diagnosis and in remission in patients with aml receiving allogeneic transplantation. Blood Advances, 7:436-444, Feb 2023. URL: https://doi.org/10.1182/bloodadvances.2021005789, doi:10.1182/bloodadvances.2021005789. This article has 42 citations and is from a peer-reviewed journal.

16. (bill2024impactofidh1 pages 26-30): M Bill. Impact of idh1 and idh2 mutation detection at diagnosis and in remission in acute myeloid leukemia patients receiving allogeneic transplantation. Unknown journal, 2024.

17. (nong2024commondrivermutations pages 7-8): Tiffany Nong, Shefali Mehra, and Justin Taylor. Common driver mutations in aml: biological impact, clinical considerations, and treatment strategies. Cells, 13:1392, Aug 2024. URL: https://doi.org/10.3390/cells13161392, doi:10.3390/cells13161392. This article has 22 citations.

18. (wang2023transgenicidh2r172kand pages 4-7): Dandan Wang, Lichuan Zheng, Bowie Yik Ling Cheng, Chun-Fung Sin, Runsheng Li, Sze Pui Tsui, Xinyu Yi, Alvin Chun Hang Ma, Bai Liang He, Anskar Yu Hung Leung, and Xuan Sun. Transgenic idh2r172k and idh2r140q zebrafish models recapitulated features of human acute myeloid leukemia. Oncogene, 42:1272-1281, Feb 2023. URL: https://doi.org/10.1038/s41388-023-02611-y, doi:10.1038/s41388-023-02611-y. This article has 14 citations and is from a domain leading peer-reviewed journal.

19. (kats2014protooncogenicroleof pages 1-3): Lev M. Kats, Markus Reschke, Riccardo Taulli, Olga Pozdnyakova, Kerri Burgess, Parul Bhargava, Kimberly Straley, Rahul Karnik, Alexander Meissner, Donald Small, Shinsan M. Su, Katharine Yen, Jiangwen Zhang, and Pier Paolo Pandolfi. Proto-oncogenic role of mutant idh2 in leukemia initiation and maintenance. Cell stem cell, 14 3:329-41, Mar 2014. URL: https://doi.org/10.1016/j.stem.2013.12.016, doi:10.1016/j.stem.2013.12.016. This article has 258 citations and is from a highest quality peer-reviewed journal.

20. (fruchtman2024managementofisocitrate pages 3-4): Harry Fruchtman, Zachary M. Avigan, Julian A. Waksal, Nicole Brennan, and John O. Mascarenhas. Management of isocitrate dehydrogenase 1/2 mutated acute myeloid leukemia. Leukemia, 38:927-935, Apr 2024. URL: https://doi.org/10.1038/s41375-024-02246-2, doi:10.1038/s41375-024-02246-2. This article has 41 citations and is from a highest quality peer-reviewed journal.

21. (bill2023impactofidh1andidh2mutationdetection pages 1-2): Marius Bill, Madlen Jentzsch, Lara Bischof, Jessica Kohlschmidt, Juliane Grimm, Laura Katharina Schmalbrock, Donata Backhaus, Dominic Brauer, Karoline Goldmann, Georg-Nikolaus Franke, Vladan Vucinic, Dietger Niederwieser, Alice S. Mims, Uwe Platzbecker, Ann-Kathrin Eisfeld, and Sebastian Schwind. Impact of<i>idh1</i>and<i>idh2</i>mutation detection at diagnosis and in remission in patients with aml receiving allogeneic transplantation. Blood Advances, 7:436-444, Feb 2023. URL: https://doi.org/10.1182/bloodadvances.2021005789, doi:10.1182/bloodadvances.2021005789. This article has 42 citations and is from a peer-reviewed journal.

22. (ravindra2024persistentidhmutations pages 1-4): Niveditha Ravindra, Laura W. Dillon, Gege Gui, Matthew Smith, Lukasz P. Gondek, Richard J. Jones, Adam Corner, Christopher S. Hourigan, and Alexander J. Ambinder. Persistent idh mutations are not associated with increased relapse or death in patients with idh-mutated acute myeloid leukemia undergoing allogeneic hematopoietic cell transplant with post-transplant cyclophosphamide. Bone Marrow Transplantation, 59:428-430, Jan 2024. URL: https://doi.org/10.1038/s41409-023-02189-9, doi:10.1038/s41409-023-02189-9. This article has 13 citations and is from a peer-reviewed journal.

23. (bill2024impactofidh1 pages 9-13): M Bill. Impact of idh1 and idh2 mutation detection at diagnosis and in remission in acute myeloid leukemia patients receiving allogeneic transplantation. Unknown journal, 2024.

24. (fruchtman2024managementofisocitrate pages 4-5): Harry Fruchtman, Zachary M. Avigan, Julian A. Waksal, Nicole Brennan, and John O. Mascarenhas. Management of isocitrate dehydrogenase 1/2 mutated acute myeloid leukemia. Leukemia, 38:927-935, Apr 2024. URL: https://doi.org/10.1038/s41375-024-02246-2, doi:10.1038/s41375-024-02246-2. This article has 41 citations and is from a highest quality peer-reviewed journal.

25. (bewersdorf2023costeffectivenessofazacitidine pages 1-2): Jan Philipp Bewersdorf, Kishan K. Patel, George Goshua, Rory M. Shallis, Nikolai A. Podoltsev, Maximilian Stahl, Eytan M. Stein, Scott F. Huntington, and Amer M. Zeidan. Cost-effectiveness of azacitidine and ivosidenib in newly diagnosed older, intensive chemotherapy-ineligible patients with <i>idh1</i> -mutant acute myeloid leukemia. Leukemia &amp; Lymphoma, 64:454-461, Dec 2023. URL: https://doi.org/10.1080/10428194.2022.2140288, doi:10.1080/10428194.2022.2140288. This article has 9 citations and is from a peer-reviewed journal.

26. (pollyea2022impactofvenetoclax pages 1-2): Daniel A. Pollyea, Courtney D. DiNardo, Martha L. Arellano, Arnaud Pigneux, Walter Fiedler, Marina Konopleva, David A. Rizzieri, B. Douglas Smith, Atsushi Shinagawa, Roberto M. Lemoli, Monique Dail, Yinghui Duan, Brenda Chyla, Jalaja Potluri, Catherine L. Miller, and Hagop M. Kantarjian. Impact of venetoclax and azacitidine in treatment-naïve patients with acute myeloid leukemia and idh1/2 mutations. Clinical Cancer Research, 28:2753-2761, Jan 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-3467, doi:10.1158/1078-0432.ccr-21-3467. This article has 194 citations and is from a highest quality peer-reviewed journal.

27. (pollyea2022impactofvenetoclax pages 5-5): Daniel A. Pollyea, Courtney D. DiNardo, Martha L. Arellano, Arnaud Pigneux, Walter Fiedler, Marina Konopleva, David A. Rizzieri, B. Douglas Smith, Atsushi Shinagawa, Roberto M. Lemoli, Monique Dail, Yinghui Duan, Brenda Chyla, Jalaja Potluri, Catherine L. Miller, and Hagop M. Kantarjian. Impact of venetoclax and azacitidine in treatment-naïve patients with acute myeloid leukemia and idh1/2 mutations. Clinical Cancer Research, 28:2753-2761, Jan 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-3467, doi:10.1158/1078-0432.ccr-21-3467. This article has 194 citations and is from a highest quality peer-reviewed journal.

28. (pollyea2022impactofvenetoclax pages 6-7): Daniel A. Pollyea, Courtney D. DiNardo, Martha L. Arellano, Arnaud Pigneux, Walter Fiedler, Marina Konopleva, David A. Rizzieri, B. Douglas Smith, Atsushi Shinagawa, Roberto M. Lemoli, Monique Dail, Yinghui Duan, Brenda Chyla, Jalaja Potluri, Catherine L. Miller, and Hagop M. Kantarjian. Impact of venetoclax and azacitidine in treatment-naïve patients with acute myeloid leukemia and idh1/2 mutations. Clinical Cancer Research, 28:2753-2761, Jan 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-3467, doi:10.1158/1078-0432.ccr-21-3467. This article has 194 citations and is from a highest quality peer-reviewed journal.

29. (fathi2022enasidenibasmaintenance media a35fe258): Amir T. Fathi, Haesook T. Kim, Robert J. Soiffer, Mark J. Levis, Shuli Li, Annette S. Kim, Alice S. Mims, Zachariah DeFilipp, Areej El-Jawahri, Steven L. McAfee, Andrew M. Brunner, Rupa Narayan, Laura W. Knight, Devon Kelley, AJ S. Bottoms, Lindsey H. Perry, Jonathan L. Wahl, Jennifer Brock, Elayne Breton, Vincent T. Ho, and Yi-Bin Chen. Enasidenib as maintenance following allogeneic hematopoietic cell transplantation for <i>idh2</i>-mutated myeloid malignancies. Blood Advances, 6:5857-5865, Nov 2022. URL: https://doi.org/10.1182/bloodadvances.2022008632, doi:10.1182/bloodadvances.2022008632. This article has 64 citations and is from a peer-reviewed journal.

30. (fathi2022enasidenibasmaintenance media 3bab0af4): Amir T. Fathi, Haesook T. Kim, Robert J. Soiffer, Mark J. Levis, Shuli Li, Annette S. Kim, Alice S. Mims, Zachariah DeFilipp, Areej El-Jawahri, Steven L. McAfee, Andrew M. Brunner, Rupa Narayan, Laura W. Knight, Devon Kelley, AJ S. Bottoms, Lindsey H. Perry, Jonathan L. Wahl, Jennifer Brock, Elayne Breton, Vincent T. Ho, and Yi-Bin Chen. Enasidenib as maintenance following allogeneic hematopoietic cell transplantation for <i>idh2</i>-mutated myeloid malignancies. Blood Advances, 6:5857-5865, Nov 2022. URL: https://doi.org/10.1182/bloodadvances.2022008632, doi:10.1182/bloodadvances.2022008632. This article has 64 citations and is from a peer-reviewed journal.

31. (fathi2022enasidenibasmaintenance media c85d33dd): Amir T. Fathi, Haesook T. Kim, Robert J. Soiffer, Mark J. Levis, Shuli Li, Annette S. Kim, Alice S. Mims, Zachariah DeFilipp, Areej El-Jawahri, Steven L. McAfee, Andrew M. Brunner, Rupa Narayan, Laura W. Knight, Devon Kelley, AJ S. Bottoms, Lindsey H. Perry, Jonathan L. Wahl, Jennifer Brock, Elayne Breton, Vincent T. Ho, and Yi-Bin Chen. Enasidenib as maintenance following allogeneic hematopoietic cell transplantation for <i>idh2</i>-mutated myeloid malignancies. Blood Advances, 6:5857-5865, Nov 2022. URL: https://doi.org/10.1182/bloodadvances.2022008632, doi:10.1182/bloodadvances.2022008632. This article has 64 citations and is from a peer-reviewed journal.

32. (NCT03839771 chunk 1):  A Study of Ivosidenib or Enasidenib in Combination With Induction Therapy and Consolidation Therapy, Followed by Maintenance Therapy in Patients With Newly Diagnosed Acute Myeloid Leukemia or Myedysplastic Syndrome EB2, With an IDH1 or IDH2 Mutation, Respectively, Eligible for Intensive Chemotherapy. Stichting Hemato-Oncologie voor Volwassenen Nederland. 2019. ClinicalTrials.gov Identifier: NCT03839771

33. (NCT06387069 chunk 1):  A Study to Evaluate HMPL-306 in Patients With IDH1or IDH2-mutated Acute Myeloid Leukemia. Hutchmed. 2024. ClinicalTrials.gov Identifier: NCT06387069

34. (NCT04603001 chunk 1):  Study of Oral LY3410738 in Patients With Advanced Hematologic Malignancies With IDH1 or IDH2 Mutations. Eli Lilly and Company. 2020. ClinicalTrials.gov Identifier: NCT04603001

35. (NCT05401097 chunk 1): Alice Mims. IDH Targeted/Non- Targeted vs Non-targeted/IDH-targeted Approaches in the Treatment of Newly Diagnosed IDH Mutated AML Patients Not Candidates for Intensive Induction Therapy (I- DATA Study). Alice Mims. 2022. ClinicalTrials.gov Identifier: NCT05401097

36. (peng2024arealworldstudy pages 4-6): Mengmeng Peng, Qian Guo, Zihan Dang, Baiquan Zhang, Manjuan Li, Zixuan Wang, Xuemian Lu, and Jie Lin. A real-world study of adverse drug reactions of two isocitrate dehydrogenase inhibitor based on the us fda adverse event reporting system and vigiaccess databases. Frontiers in Pharmacology, Nov 2024. URL: https://doi.org/10.3389/fphar.2024.1489045, doi:10.3389/fphar.2024.1489045. This article has 3 citations.

37. (cerchione2021idh1idh2inhibitionin pages 1-2): Claudio Cerchione, Alessandra Romano, Naval Daver, Courtney DiNardo, Elias Joseph Jabbour, Marina Konopleva, Farhad Ravandi-Kashani, Tapan Kadia, Maria Paola Martelli, Alessandro Isidori, Giovanni Martinelli, and Hagop Kantarjian. Idh1/idh2 inhibition in acute myeloid leukemia. Frontiers in Oncology, Mar 2021. URL: https://doi.org/10.3389/fonc.2021.639387, doi:10.3389/fonc.2021.639387. This article has 85 citations.

38. (shimony2023acutemyeloidleukemia pages 5-6): Shai Shimony, Maximilian Stahl, and Richard M. Stone. Acute myeloid leukemia: 2023 update on diagnosis, risk‐stratification, and management. American Journal of Hematology, 98:502-526, Jan 2023. URL: https://doi.org/10.1002/ajh.26822, doi:10.1002/ajh.26822. This article has 524 citations and is from a domain leading peer-reviewed journal.

39. (chen2023efficacyandsafety pages 6-8): Xiu Chen, Hongyun Xing, Xiaolu Xie, Liqiu Kou, Jun Li, and Yaling Li. Efficacy and safety of fda-approved idh inhibitors in the treatment of idh mutated acute myeloid leukemia: a systematic review and meta-analysis. Clinical Epigenetics, Jul 2023. URL: https://doi.org/10.1186/s13148-023-01529-2, doi:10.1186/s13148-023-01529-2. This article has 30 citations and is from a peer-reviewed journal.

40. (issa2021acutemyeloidleukemia pages 5-6): Ghayas C. Issa and Courtney D. DiNardo. Acute myeloid leukemia with idh1 and idh2 mutations: 2021 treatment algorithm. Blood Cancer Journal, Jun 2021. URL: https://doi.org/10.1038/s41408-021-00497-1, doi:10.1038/s41408-021-00497-1. This article has 210 citations and is from a domain leading peer-reviewed journal.

41. (nong2024commondrivermutations pages 8-10): Tiffany Nong, Shefali Mehra, and Justin Taylor. Common driver mutations in aml: biological impact, clinical considerations, and treatment strategies. Cells, 13:1392, Aug 2024. URL: https://doi.org/10.3390/cells13161392, doi:10.3390/cells13161392. This article has 22 citations.
