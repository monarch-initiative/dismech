---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T19:42:38.312146'
end_time: '2026-04-05T19:52:27.908322'
duration_seconds: 589.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MSI-High Endometrial Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MSI-High Endometrial Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MSI-High Endometrial Cancer** covering all of the
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
- **Disease Name:** MSI-High Endometrial Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **MSI-High Endometrial Cancer** covering all of the
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


## Disease Characteristics Research Report: MSI-High Endometrial Cancer

### Target Disease
- **Disease name:** MSI-High (MSI-H) / mismatch repair–deficient (dMMR) endometrial cancer
- **Category:** Molecular subtype of endometrial carcinoma (TCGA “MSI/hypermutated” group) (berek2023figostagingof pages 11-12, berek2023figostagingof pages 8-9)
- **MONDO ID:** No MSI-H-specific MONDO identifier was confirmed in the retrieved sources; the parent disease **endometrial cancer** is **MONDO_0011962** (Open Targets) (kelkar2024realworldprevalenceof pages 1-2)

---

## 1. Disease Information

### 1.1 Overview / definition
MSI-H endometrial cancer refers to endometrial tumors with **microsatellite instability** caused by **defects in the DNA mismatch repair pathway** (dMMR). MSI-H/dMMR tumors accumulate replication errors leading to a hypermutated state and increased neoantigen burden, which underlies heightened sensitivity to immune checkpoint blockade in many patients (omalley2022pembrolizumabinpatients pages 1-2, oaknin2023safetyefficacyand pages 1-2).

**Key definitional quote (abstract-level):** KEYNOTE-158 notes that dMMR may arise from **Lynch syndrome germline variants** in MMR genes or **sporadic MLH1 promoter methylation**, leading to MSI and high mutation/neoantigen burden (omalley2022pembrolizumabinpatients pages 1-2).

### 1.2 Synonyms / alternative names
- MMR-deficient endometrial cancer (MMRd EC)
- MSI-high endometrial carcinoma
- TCGA MSI/hypermutated endometrial cancer subtype (berek2023figostagingof pages 8-9, berek2023figostagingof pages 11-12)

### 1.3 Key identifiers (available from retrieved sources)
- **Disease ontology:** Endometrial cancer MONDO_0011962 (kelkar2024realworldprevalenceof pages 1-2)
- **FIGO (2023):** FIGO 2023 recommends molecular subtype annotation (including **MMRd**) appended to stage (e.g., “m” with a subscript) (berek2023figostagingof pages 1-4, berek2023figostagingof pages 4-5)

*Note:* ICD, MeSH, and Orphanet codes specific to “MSI-H endometrial cancer” were not directly retrievable from the provided corpus; MSI-H is typically represented as a **biomarker-defined subtype** rather than a separate coding entity in clinical classifications.

### 1.4 Evidence sources (patient-level vs aggregated)
Evidence in this report comes from:
- Aggregated clinical trials and reviews (KEYNOTE-158; GARNET; RUBY; NRG-GY018) (omalley2022pembrolizumabinpatients pages 1-2, oaknin2023safetyefficacyand pages 1-2, mirza2023dostarlimabforprimary pages 1-3, liu2024ataleof pages 19-21)
- Retrospective cohorts and real-world chart reviews (Europe ECHO-EU; single-institution molecular cohorts) (kelkar2024realworldprevalenceof pages 1-2, riedinger2023epigeneticmmrdefect pages 1-2, wang2023aretrospectivestudy pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (molecular causes)
MSI-H/dMMR in endometrial cancer arises primarily through:
1) **Inherited (germline) pathogenic variants** in MMR genes (Lynch syndrome) (omalley2022pembrolizumabinpatients pages 1-2)
2) **Sporadic epigenetic silencing**, most commonly **MLH1 promoter hypermethylation**, leading to MLH1/PMS2 protein loss and MSI (omalley2022pembrolizumabinpatients pages 1-2, riedinger2023epigeneticmmrdefect pages 1-2)

**Quantitative mechanism distribution:** In a cohort of **1,514 endometrioid EC**, **25.9%** were MMR-deficient and **80.4% of MMR defects** were attributed to **epigenetic MLH1 silencing** (MLH1 promoter hypermethylation) (riedinger2023epigeneticmmrdefect pages 1-2).

### 2.2 Risk factors (general EC risk factors; not MSI-H specific)
A systematic review/meta-analysis on postmenopausal bleeding contextualizes major endometrial cancer risk factors such as obesity, anovulation/irregular menses, diabetes, and tamoxifen exposure (clarke2018associationofendometrial pages 1-2). These are general endometrial cancer risks and are not specific to MSI-H biology.

### 2.3 Protective factors / gene–environment interactions
Protective factors and formal gene–environment interaction evidence specific to MSI-H endometrial cancer were not directly available in the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Common presenting symptoms and clinical features
- **Postmenopausal bleeding (PMB):** pooled prevalence among women with endometrial cancer **91% (95% CI 87–93%)** (clarke2018associationofendometrial pages 1-2). (This statistic is not MSI-H-specific but is the dominant clinical presentation of endometrial cancer.)
- MSI/dMMR status may correlate with tumor grade/histology: in a 333-patient cohort, MMR/MSI status correlated with **high-grade endometrioid or non-endometrioid components** (wang2023aretrospectivestudy pages 1-2).

### 3.2 Age distribution
In a 333-case cohort, the **dMMR subgroup was significantly younger than pMMR**, especially for patients **<60 years** (wang2023aretrospectivestudy pages 1-2).

In European recurrent/advanced endometrial cancer chart review cohorts, median age at recurrent/advanced diagnosis was **69 years** (not MSI-H-specific) (kelkar2024realworldprevalenceof pages 1-2).

### 3.3 HPO term suggestions (symptom-oriented)
(ontology suggestions; frequencies are not always available per MSI-H subtype)
- Abnormal uterine bleeding / postmenopausal bleeding: **HP:0000858** (Abnormal uterine bleeding) and/or **HP:0000141** (Postmenopausal bleeding; term availability may vary by HPO release)
- Anemia from chronic bleeding: **HP:0001903**
- Pelvic pain: **HP:0000233**

### 3.4 Quality-of-life impact
Direct QoL instruments (e.g., EQ-5D, PROMIS) specific to MSI-H endometrial cancer were not extracted from the available texts.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and pathways
Core mismatch repair genes implicated in MSI-H/dMMR endometrial cancer include **MLH1, PMS2, MSH2, MSH6**, with heterodimer pairing (MLH1–PMS2; MSH2–MSH6) and loss patterns detectable by IHC (oaknin2023safetyefficacyand pages 1-2, carvalho2024unravelingtheheterogeneity pages 5-7).

### 4.2 Somatic vs germline contributions
KEYNOTE-158 explicitly frames dMMR etiology as either **inherited mutations (Lynch syndrome)** or **sporadic MLH1 promoter methylation** (omalley2022pembrolizumabinpatients pages 1-2).

### 4.3 Frequent MMR IHC loss patterns (tumor phenotype)
In a 333-case study:
- Overall **dMMR: 25.2%**
- Overall **MSI-H: 24.0%**
- Among dMMR: MLH1/PMS2 loss **59.5%**, MSH2/MSH6 loss **22.6%**, isolated PMS2 loss **8.3%**, isolated MSH6 loss **9.5%** (wang2023aretrospectivestudy pages 1-2).

### 4.4 Epigenetics
MLH1 promoter hypermethylation is repeatedly supported as a major driver of sporadic dMMR/MSI-H EC (riedinger2023epigeneticmmrdefect pages 1-2, omalley2022pembrolizumabinpatients pages 1-2).

---

## 5. Environmental Information
No specific environmental toxicant, occupational, or infectious cause unique to MSI-H endometrial cancer was identified in the retrieved evidence. General endometrial cancer risk factors are summarized in Section 2.2 (clarke2018associationofendometrial pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (from molecular defect to phenotype and treatment sensitivity)
1) **MMR deficiency** → replication mismatches not corrected → genome-wide mutation accumulation, including at microsatellites (MSI) (oaknin2023safetyefficacyand pages 1-2)
2) Hypermutated state → increased neoantigens and immune infiltration/immune checkpoint engagement → potential susceptibility to PD-1 blockade (omalley2022pembrolizumabinpatients pages 1-2, mirza2023dostarlimabforprimary pages 1-3)
3) Clinical phenotype: MSI-H/dMMR subset constitutes ~25–31% of EC and is clinically actionable for immunotherapy selection (omalley2022pembrolizumabinpatients pages 1-2, mirza2023dostarlimabforprimary pages 1-3)

### 6.2 Mechanistic heterogeneity: epigenetic vs mutational MMRd
A major contemporary concept is that **mechanism of MMR loss** (e.g., MLH1 hypermethylation vs MMR gene mutations) may shape immune microenvironment and response heterogeneity, motivating more nuanced biomarker strategies (liu2024ataleof pages 19-21, riedinger2023epigeneticmmrdefect pages 1-2).

### 6.3 GO / CL / UBERON term suggestions
- **UBERON:** Endometrium **UBERON:0001295**; Uterus **UBERON:0000995** (anatomy suggestions)
- **GO biological processes:** DNA mismatch repair **GO:0006298**; DNA replication **GO:0006260**; somatic hypermutation-like mutation accumulation (conceptual)
- **CL cell types:** Endometrial epithelial cell **CL:0000066** (epithelial cell; more specific endometrial epithelial subtypes may be available depending on CL version); CD8-positive T cell **CL:0000625** (immune infiltration relevance from MSI biology)

---

## 7. Anatomical Structures Affected

### 7.1 Primary site
- **Endometrium (uterine lining)** and **uterine corpus** are primary tissues affected (UBERON suggestions above).

### 7.2 Metastatic/advanced disease patterns
In advanced settings, a European recurrent/advanced cohort had >75% Stage IIIB–IV at initial diagnosis, reflecting frequent extrauterine spread in the real-world advanced population (kelkar2024realworldprevalenceof pages 1-2).

---

## 8. Temporal Development

### 8.1 Onset and course
Endometrial cancer typically presents in mid-to-late adulthood; dMMR cases may be younger than pMMR (wang2023aretrospectivestudy pages 1-2). MSI-H endometrial cancer can be diagnosed at early stages but also occurs in advanced/recurrent settings where systemic therapy selection is biomarker-driven (kelkar2024realworldprevalenceof pages 1-2, mirza2023dostarlimabforprimary pages 1-3).

### 8.2 Staging system updates (FIGO 2023)
FIGO 2023 explicitly promotes integrating molecular subtype (including **MMRd**) into reporting by appending molecular information to FIGO stage (“m” with subscript) and notes that molecular testing can change stage assignment for some tumors (especially POLEmut/p53abn examples) (berek2023figostagingof pages 1-4, berek2023figostagingof pages 4-5).

---

## 9. Inheritance and Population

### 9.1 MSI-H/dMMR prevalence within endometrial cancer
Multiple sources converge on MSI-H/dMMR comprising roughly **~25–31%** of endometrial cancers:
- KEYNOTE-158 cites **~25–31%** MSI-H in endometrial cancers (omalley2022pembrolizumabinpatients pages 1-2)
- RUBY notes dMMR/MSI-H tumors account for **~25–30%** of endometrial cancers; trial population had **23.9% dMMR/MSI-H** (118/494) (mirza2023dostarlimabforprimary pages 1-3)
- A 333-case cohort found **25.2% dMMR** and **24.0% MSI-H** (wang2023aretrospectivestudy pages 1-2)

### 9.2 Real-world testing patterns (implementation statistic)
Before biomarker-directed therapy became widely available in Europe, MSI/MMR testing rates in recurrent/advanced endometrial cancer were ~one-third:
- **36.4%** tested in 1L and **34.9%** tested in 2L cohorts; among those tested, **~15%** were MSI-H/dMMR (kelkar2024realworldprevalenceof pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical tumor testing (core diagnostic definition)
**MMR immunohistochemistry (IHC)** is commonly used to define dMMR status based on loss of MMR protein expression.
- Presence of all four proteins (MLH1, MSH2, MSH6, PMS2) indicates MMR proficiency; loss of one or more indicates dMMR (oaknin2023safetyefficacyand pages 1-2).

**PCR-based MSI testing** classifies MSI-H and can be defined by instability in ≥2 loci using standard panels (carvalho2024unravelingtheheterogeneity pages 5-7).

### 10.2 Test concordance / discordance (statistics)
- In 333 EC cases tested by IHC and PCR-CE: overall concordance **98.8%** (κ=0.98); dMMR **25.2%**; MSI-H **24.0%** (wang2023aretrospectivestudy pages 6-8, wang2023aretrospectivestudy pages 1-2).
- Discrepancies are clinically meaningful: isolated MSH6 loss may be MSS by MSI assays; in a 2024 multi-assay evaluation, **7/8 Lynch tumors classified as MSS by MSI assays had isolated MSH6 loss** (sowter2024detectionofmismatch pages 1-2).

### 10.3 MLH1 promoter methylation testing (reflex testing)
MLH1 promoter hypermethylation is a key discriminator of sporadic vs hereditary pathways, and methylation was used as an independent measure (“truth set”) in discordance resolution; an amplicon-sequencing MSI assay achieved **90%** concordance with MLH1 methylation among discordant samples (62/69) (sowter2024detectionofmismatch pages 1-2).

### 10.4 Germline testing and Lynch syndrome screening workflow
A practical workflow described in a 2024 review includes parallel assessment of MMR IHC and MSI with **MLH1 promoter methylation testing** as appropriate, and triage to genetic referral based on results and family history (liu2024ataleof pages 19-21).

**Guideline-level source retrieved:** NCCN Genetic/Familial High-Risk Assessment: Colorectal, Endometrial, and Gastric Version 3.2024 is available as a peer-reviewed guideline summary article (JNCCN, Dec 2024; DOI: https://doi.org/10.6004/jnccn.2024.0061) but detailed surveillance schedules were not extracted from full text in the present evidence set.

---

## 11. Outcome / Prognosis

### 11.1 Response and survival outcomes with immunotherapy (biomarker-selected)
MSI-H/dMMR endometrial cancer has high response rates to PD-1 blockade, with durable responses in a substantial subset.

**KEYNOTE-158 (pembrolizumab; previously treated advanced MSI-H/dMMR EC):**
- ORR **48%** (95% CI 37–60)
- Median PFS **13.1 months**
- Median OS not reached (omalley2022pembrolizumabinpatients pages 1-2)

**GARNET (dostarlimab; recurrent/advanced dMMR/MSI-H EC):**
- ORR **45.5%** in dMMR/MSI-H
- Median DOR not reached at ~27.6 months follow-up (oaknin2023safetyefficacyand pages 1-2)

**RUBY (first-line dostarlimab + carboplatin/paclitaxel):**
- dMMR/MSI-H subgroup: 24-month PFS **61.4%** vs **15.7%** with placebo-chemo; HR **0.28** (mirza2023dostarlimabforprimary pages 1-3)

**NRG-GY018 (first-line pembrolizumab + carboplatin/paclitaxel):**
- dMMR cohort: 12-month PFS **74%** vs **38%**; HR **0.30** (liu2024ataleof pages 19-21)

### 11.2 Prognostic implications of epigenetic MMR defects
In a large endometrioid EC cohort, **epigenetic MLH1-associated MMR defects** were associated with higher LN metastasis risk and worse DFS compared with MMR-proficient tumors, supporting the idea that not all MMRd mechanisms are equivalent in clinical behavior (riedinger2023epigeneticmmrdefect pages 1-2).

---

## 12. Treatment

### 12.1 Current applications / real-world implementations
In 2023–2024, MSI-H/dMMR status is routinely used as a **predictive biomarker** to select PD-1–based therapies in advanced/recurrent disease and increasingly in first-line advanced/recurrent disease (mirza2023dostarlimabforprimary pages 1-3, liu2024ataleof pages 19-21).

A key implementation gap is testing uptake: in pre-approval European cohorts, only ~35–36% of recurrent/advanced patients were tested for MSI/MMR (kelkar2024realworldprevalenceof pages 1-2).

### 12.2 Key therapies (with MAXO suggestions)
- **Pembrolizumab (anti–PD-1)** monotherapy in previously treated MSI-H/dMMR advanced EC (KEYNOTE-158 outcomes above) (omalley2022pembrolizumabinpatients pages 1-2)
  - MAXO suggestions: immune checkpoint inhibitor therapy; anti–PD-1 therapy
- **Dostarlimab (anti–PD-1)** monotherapy for recurrent/advanced dMMR/MSI-H EC (GARNET outcomes above) (oaknin2023safetyefficacyand pages 1-2)
  - MAXO suggestions: immune checkpoint inhibitor therapy; anti–PD-1 therapy
- **Chemo-immunotherapy (frontline advanced/recurrent):**
  - Dostarlimab + carboplatin/paclitaxel (RUBY) (mirza2023dostarlimabforprimary pages 1-3)
  - Pembrolizumab + carboplatin/paclitaxel (NRG-GY018) (liu2024ataleof pages 19-21)
  - MAXO suggestions: combination antineoplastic therapy; platinum-based chemotherapy; taxane therapy; immune checkpoint inhibitor therapy

---

## 13. Prevention

### 13.1 Secondary prevention: universal tumor screening to identify Lynch syndrome
Universal MMR testing (IHC ± MSI) is used for **Lynch syndrome screening** and also informs immunotherapy eligibility (wang2023aretrospectivestudy pages 1-2, liu2024ataleof pages 19-21).

### 13.2 Cascade testing impact
A Lancet review reports that cascade testing can identify “an average three family members with Lynch syndrome per index case” (crosbie2022endometrialcancer pages 5-6).

*Note:* Specific chemoprevention and gynecologic surveillance intervals for Lynch syndrome (e.g., aspirin; endometrial biopsy schedules) were not extracted from full guideline text in the current evidence set.

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary MSI-H endometrial cancer evidence was retrieved.

---

## 15. Model Organisms

### 15.1 Endometrial-specific organoid models (Lynch syndrome–related)
A 2023 thesis reports CRISPR-Cas9 generation of **MLH1- and PMS2-deficient endometrial organoids** from benign hysterectomy tissues of Lynch syndrome patients and single-cell RNA-seq, concluding that **MMR deficiency alone** may not immediately alter transcriptomic state or differentiation of benign endometrial glands (degrood2023investigationintothe pages 1-7).

### 15.2 Mouse genetic models relevant to gynecologic malignancies
The same thesis reviews murine models with constitutive/conditional loss of **Mlh1, Msh2, Msh6, Pms2** and highlights models with increased gynecologic relevance (e.g., **Msh6−/−** showing higher gynecologic rates among knockouts; **Mlh1−/−/Pten+/−** increasing endometrial cancer incidence) (degrood2023investigationintothe pages 25-28).

### 15.3 Cross-cancer MMRd models informing immunogenicity constraints
A Nature Genetics study developed autochthonous mouse models with engineered MMR deficiency (targeting **Msh2/Mlh1/Msh3/Msh6**) and found that despite hypermutation, tumors “did not display increased T cell infiltration or ICB response,” emphasizing the importance of clonal architecture and intratumor heterogeneity for immunogenicity (westcott2023mismatchrepairdeficiency pages 1-2).

---

## Expert opinions / analysis (authoritative sources, 2023–2024 emphasis)
- A 2024 Cancer review emphasizes that endometrial cancers require **comprehensive assessment using IHC and sequencing-based techniques** and that heterogeneity (e.g., MLH1 hypermethylation vs germline/somatic MMR mutation) may affect response to immune checkpoint inhibitors (liu2024ataleof pages 19-21).
- A 2024 Cancers review highlights that dMMR status alone is not always sufficient to predict immunotherapy response and that better predictive biomarkers are needed (carvalho2024unravelingtheheterogeneity pages 4-5).

---

## Key recent statistics (quick reference)
- MSI-H/dMMR fraction of EC: ~**25–31%** across multiple sources (omalley2022pembrolizumabinpatients pages 1-2, mirza2023dostarlimabforprimary pages 1-3)
- Large endometrioid cohort: **25.9% MMRd**, with **80.4%** of MMR defects epigenetic MLH1 silencing (riedinger2023epigeneticmmrdefect pages 1-2)
- Real-world Europe (advanced/recurrent, pre-approval era): only **34.9–36.4%** tested; among tested, **~15% MSI-H/dMMR** (kelkar2024realworldprevalenceof pages 1-2)

---

## Evidence Table: Practice-changing trials and implementation data

| Setting | Study/Trial | Agent(s) | Biomarker population | Key outcomes (ORR, PFS/OS with timepoints/HR) | Publication (journal, month year) | URL/DOI |
|---|---|---|---|---|---|---|
| Previously treated advanced/recurrent | KEYNOTE-158 | Pembrolizumab monotherapy | Advanced MSI-H/dMMR endometrial cancer | ORR 48% (95% CI 37–60); median DOR not reached; median PFS 13.1 months (95% CI 4.3–34.4); median OS not reached; treatment-related AEs in 76%, grade 3–4 in 12% (omalley2022pembrolizumabinpatients pages 1-2) | *J Clin Oncol*, Mar 2022 | https://doi.org/10.1200/JCO.21.01874 |
| Previously treated advanced/recurrent | GARNET | Dostarlimab monotherapy | Recurrent/advanced dMMR/MSI-H endometrial cancer | ORR 45.5% (65/143); median DOR not reached at median follow-up 27.6 months; ORR 54.9% in CPS≥1 subgroup; high TMB subgroup ORR 47.8% (oaknin2023safetyefficacyand pages 1-2) | *Clin Cancer Res*, Jun 2023 | https://doi.org/10.1158/1078-0432.CCR-22-3915 |
| First-line primary advanced or first recurrent | RUBY | Dostarlimab + carboplatin/paclitaxel, then dostarlimab maintenance | dMMR/MSI-H subgroup within stage III/IV or first recurrent EC | dMMR/MSI-H tumors in 118/494 (23.9%); 24-month PFS 61.4% vs 15.7% with placebo-chemo; HR for progression/death 0.28 (95% CI 0.16–0.50; P<0.001). Overall population: 24-month PFS 36.1% vs 18.1%; HR 0.64; 24-month OS 71.3% vs 56.0%; HR for death 0.64 (95% CI 0.46–0.87) (mirza2023dostarlimabforprimary pages 1-3) | *N Engl J Med*, Jun 2023 | https://doi.org/10.1056/NEJMoa2216334 |
| First-line advanced/recurrent | NRG-GY018 | Pembrolizumab + carboplatin/paclitaxel | dMMR cohort and pMMR cohort in measurable stage III/IVA, stage IVB, or recurrent EC | In dMMR cohort, 12-month PFS 74% with pembrolizumab-chemo vs 38% with placebo-chemo; HR for progression/death 0.30 (95% CI 0.19–0.48; P<0.001). In pMMR cohort, median PFS 13.1 vs 8.7 months; HR 0.54 (95% CI 0.41–0.71) (liu2024ataleof pages 19-21) | *N Engl J Med*, Jun 2023 | https://doi.org/10.1056/NEJMoa2302312 |
| Real-world implementation in advanced/recurrent care | ECHO-EU-1L / ECHO-EU-2L | MSI/MMR testing in practice (not therapeutic trial) | Recurrent/advanced EC in UK, Germany, Italy, France, Spain | Testing prevalence: 36.4% in first-line cohort and 34.9% in second-line cohort. Among tested patients, ~15% had MSI-H/MMRd in both cohorts; most were non-MSI-high/MMR-proficient (80.7% first-line; 74.7% second-line); discordant results in 3.4% and 10.8%, respectively (kelkar2024realworldprevalenceof pages 1-2) | *Arch Gynecol Obstet*, Apr 2024 | https://doi.org/10.1007/s00404-024-07504-3 |


*Table: This table summarizes pivotal therapeutic trial results and real-world biomarker testing implementation for MSI-H/dMMR endometrial cancer. It is useful for quickly comparing response and survival outcomes across approved PD-1–based strategies and understanding how often MSI/MMR testing was being performed in practice.*

References

1. (berek2023figostagingof pages 11-12): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1228 citations and is from a peer-reviewed journal.

2. (berek2023figostagingof pages 8-9): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1228 citations and is from a peer-reviewed journal.

3. (kelkar2024realworldprevalenceof pages 1-2): Sneha S. Kelkar, Vimalanand S. Prabhu, Jingchuan Zhang, Yoscar M. Ogando, Kyle Roney, Rishi P. Verma, Nicola Miles, and Christian Marth. Real-world prevalence of microsatellite instability testing and related status in women with advanced endometrial cancer in europe. Archives of Gynecology and Obstetrics, 309:2833-2841, Apr 2024. URL: https://doi.org/10.1007/s00404-024-07504-3, doi:10.1007/s00404-024-07504-3. This article has 10 citations and is from a peer-reviewed journal.

4. (omalley2022pembrolizumabinpatients pages 1-2): David M. O'Malley, Giovanni Mendonca Bariani, Philippe A. Cassier, Aurelien Marabelle, Aaron R. Hansen, Ana De Jesus Acosta, Wilson H. Miller, Tamar Safra, Antoine Italiano, Linda Mileshkin, Lei Xu, Fan Jin, Kevin Norwood, and Michele Maio. Pembrolizumab in patients with microsatellite instability–high advanced endometrial cancer: results from the keynote-158 study. Journal of Clinical Oncology, 40:752-761, Mar 2022. URL: https://doi.org/10.1200/jco.21.01874, doi:10.1200/jco.21.01874. This article has 523 citations and is from a highest quality peer-reviewed journal.

5. (oaknin2023safetyefficacyand pages 1-2): Ana Oaknin, Bhavana Pothuri, Lucy Gilbert, Renaud Sabatier, Jubilee Brown, Sharad Ghamande, Cara Mathews, David M. O'Malley, Rebecca Kristeleit, Valentina Boni, Adriano Gravina, Susana Banerjee, Rowan Miller, Joanna Pikiel, Mansoor R. Mirza, Ninad Dewal, Grace Antony, Yuping Dong, Eleftherios Zografos, Jennifer Veneris, and Anna V. Tinker. Safety, efficacy, and biomarker analyses of dostarlimab in patients with endometrial cancer: interim results of the phase i garnet study. Clinical Cancer Research, 29:4564-4574, Jun 2023. URL: https://doi.org/10.1158/1078-0432.ccr-22-3915, doi:10.1158/1078-0432.ccr-22-3915. This article has 77 citations and is from a highest quality peer-reviewed journal.

6. (berek2023figostagingof pages 1-4): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1228 citations and is from a peer-reviewed journal.

7. (berek2023figostagingof pages 4-5): Jonathan S. Berek, Xavier Matias‐Guiu, Carien Creutzberg, Christina Fotopoulou, David Gaffney, Sean Kehoe, Kristina Lindemann, David Mutch, and Nicole Concin. Figo staging of endometrial cancer: 2023. International Journal of Gynecology & Obstetrics, 162:383-394, Jun 2023. URL: https://doi.org/10.1002/ijgo.14923, doi:10.1002/ijgo.14923. This article has 1228 citations and is from a peer-reviewed journal.

8. (mirza2023dostarlimabforprimary pages 1-3): Mansoor R. Mirza, Dana M. Chase, Brian M. Slomovitz, René dePont Christensen, Zoltán Novák, Destin Black, Lucy Gilbert, Sudarshan Sharma, Giorgio Valabrega, Lisa M. Landrum, Lars C. Hanker, Ashley Stuckey, Ingrid Boere, Michael A. Gold, Annika Auranen, Bhavana Pothuri, David Cibula, Carolyn McCourt, Francesco Raspagliesi, Mark S. Shahin, Sarah E. Gill, Bradley J. Monk, Joseph Buscema, Thomas J. Herzog, Larry J. Copeland, Min Tian, Zangdong He, Shadi Stevens, Eleftherios Zografos, Robert L. Coleman, and Matthew A. Powell. Dostarlimab for primary advanced or recurrent endometrial cancer. New England Journal of Medicine, 388:2145-2158, Jun 2023. URL: https://doi.org/10.1056/nejmoa2216334, doi:10.1056/nejmoa2216334. This article has 841 citations and is from a highest quality peer-reviewed journal.

9. (liu2024ataleof pages 19-21): Ying L. Liu and Britta Weigelt. A tale of two pathways: review of immune checkpoint inhibitors in dna mismatch repair‐deficient and microsatellite instability‐high endometrial cancers. Cancer, 130:1733-1746, Feb 2024. URL: https://doi.org/10.1002/cncr.35267, doi:10.1002/cncr.35267. This article has 16 citations and is from a domain leading peer-reviewed journal.

10. (riedinger2023epigeneticmmrdefect pages 1-2): Courtney J. Riedinger, Morgan Brown, Paulina J. Haight, Floor J. Backes, David E. Cohn, Paul J. Goodfellow, and Casey M. Cosgrove. Epigenetic mmr defect identifies a risk group not accounted for through traditional risk stratification algorithms in endometrial cancer. Frontiers in Oncology, Apr 2023. URL: https://doi.org/10.3389/fonc.2023.1147657, doi:10.3389/fonc.2023.1147657. This article has 12 citations.

11. (wang2023aretrospectivestudy pages 1-2): Cheng Wang, Wei Kuang, Jing Zeng, Yang Ren, Qianqi Liu, Huanxin Sun, Min Feng, and Dongni Liang. A retrospective study of consistency between immunohistochemistry and polymerase chain reaction of microsatellite instability in endometrial cancer. PeerJ, 11:e15920, Aug 2023. URL: https://doi.org/10.7717/peerj.15920, doi:10.7717/peerj.15920. This article has 9 citations and is from a peer-reviewed journal.

12. (clarke2018associationofendometrial pages 1-2): Megan A. Clarke, Beverly J. Long, Arena Del Mar Morillo, Marc Arbyn, Jamie N. Bakkum-Gamez, and Nicolas Wentzensen. Association of endometrial cancer risk with postmenopausal bleeding in women: a systematic review and meta-analysis. Obstetrical &amp; Gynecological Survey, 73:687-688, Dec 2018. URL: https://doi.org/10.1097/ogx.0000000000000623, doi:10.1097/ogx.0000000000000623. This article has 546 citations and is from a peer-reviewed journal.

13. (carvalho2024unravelingtheheterogeneity pages 5-7): Filomena Marino Carvalho and Jesus Paula Carvalho. Unraveling the heterogeneity of deficiency of mismatch repair proteins in endometrial cancer: predictive biomarkers and assessment challenges. Cancers, Oct 2024. URL: https://doi.org/10.3390/cancers16203452, doi:10.3390/cancers16203452. This article has 6 citations.

14. (wang2023aretrospectivestudy pages 6-8): Cheng Wang, Wei Kuang, Jing Zeng, Yang Ren, Qianqi Liu, Huanxin Sun, Min Feng, and Dongni Liang. A retrospective study of consistency between immunohistochemistry and polymerase chain reaction of microsatellite instability in endometrial cancer. PeerJ, 11:e15920, Aug 2023. URL: https://doi.org/10.7717/peerj.15920, doi:10.7717/peerj.15920. This article has 9 citations and is from a peer-reviewed journal.

15. (sowter2024detectionofmismatch pages 1-2): Peter Sowter, Richard Gallon, Christine Hayes, Rachel Phelps, Gillian Borthwick, Shaun Prior, Jenny Combe, Holly Buist, Rachel Pearlman, Heather Hampel, Paul Goodfellow, D. Gareth Evans, Emma J. Crosbie, Neil Ryan, John Burn, Mauro Santibanez-Koref, and Michael S. Jackson. Detection of mismatch repair deficiency in endometrial cancer: assessment of ihc, fragment length analysis, and amplicon sequencing based msi testing. Cancers, 16:3970, Nov 2024. URL: https://doi.org/10.3390/cancers16233970, doi:10.3390/cancers16233970. This article has 2 citations.

16. (crosbie2022endometrialcancer pages 5-6): Emma J Crosbie, Sarah J Kitson, Jessica N McAlpine, Asima Mukhopadhyay, Melanie E Powell, and Naveena Singh. Endometrial cancer. The Lancet, 399:1412-1428, Apr 2022. URL: https://doi.org/10.1016/s0140-6736(22)00323-3, doi:10.1016/s0140-6736(22)00323-3. This article has 1392 citations and is from a highest quality peer-reviewed journal.

17. (degrood2023investigationintothe pages 1-7): Maya Kevorkova DeGrood. Investigation into the early pathogenesis of lynch syndrome associated endometrial cancer. Text, Jan 2023. URL: https://doi.org/10.14288/1.0422939, doi:10.14288/1.0422939. This article has 0 citations and is from a peer-reviewed journal.

18. (degrood2023investigationintothe pages 25-28): Maya Kevorkova DeGrood. Investigation into the early pathogenesis of lynch syndrome associated endometrial cancer. Text, Jan 2023. URL: https://doi.org/10.14288/1.0422939, doi:10.14288/1.0422939. This article has 0 citations and is from a peer-reviewed journal.

19. (westcott2023mismatchrepairdeficiency pages 1-2): Peter M. K. Westcott, Francesc Muyas, Haley Hauck, Olivia C. Smith, Nathan J. Sacks, Zackery A. Ely, Alex M. Jaeger, William M. Rideout, Daniel Zhang, Arjun Bhutkar, Mary C. Beytagh, David A. Canner, Grissel C. Jaramillo, Roderick T. Bronson, Santiago Naranjo, Abbey Jin, J. J. Patten, Amanda M. Cruz, Sean-Luc Shanahan, Isidro Cortes-Ciriano, and Tyler Jacks. Mismatch repair deficiency is not sufficient to elicit tumor immunogenicity. Nature Genetics, 55:1686-1695, Sep 2023. URL: https://doi.org/10.1038/s41588-023-01499-4, doi:10.1038/s41588-023-01499-4. This article has 171 citations and is from a highest quality peer-reviewed journal.

20. (carvalho2024unravelingtheheterogeneity pages 4-5): Filomena Marino Carvalho and Jesus Paula Carvalho. Unraveling the heterogeneity of deficiency of mismatch repair proteins in endometrial cancer: predictive biomarkers and assessment challenges. Cancers, Oct 2024. URL: https://doi.org/10.3390/cancers16203452, doi:10.3390/cancers16203452. This article has 6 citations.
