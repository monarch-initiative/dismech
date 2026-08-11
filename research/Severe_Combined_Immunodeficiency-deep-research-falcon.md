---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T12:08:57.624888'
end_time: '2026-06-22T12:16:48.706243'
duration_seconds: 471.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Severe Combined Immunodeficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Combined Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency** covering all of the
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
- **Disease Name:** Severe Combined Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency** covering all of the
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


I apologize, but I'm unable to complete the comprehensive disease characteristics research report for Severe Combined Immunodeficiency (SCID) as requested. While I successfully retrieved relevant scientific literature covering SCID's clinical features, genetics, treatment approaches, newborn screening, and outcomes, I encountered technical difficulties with the evidence gathering system that prevented me from systematically extracting and organizing the detailed information needed for a comprehensive report across all 15 sections you specified.

From the papers I was able to access, I can provide the following preliminary overview based on the retrieved documents:

## Disease Overview

Severe Combined Immunodeficiency (SCID) is a rare, life-threatening inherited immunodeficiency disorder characterized by profound defects in T lymphocyte development and function, often affecting both cellular and humoral immunity (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, dhomakonda2025areviewon pages 1-2, dvorak2023thediagnosisof pages 1-3). SCID is considered a pediatric emergency and, if left untreated, typically results in death within the first two years of life due to severe opportunistic infections (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, vignesh2021clinicalimmunologicaland pages 1-2).

## Key Identifiers and Synonyms

SCID is also known as "bubble boy disease" or "living in the bubble" syndrome, named after the historical practice of isolating affected children in sterile environments (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2).

## Epidemiology and Prevalence

Recent data from newborn screening programs indicate that SCID occurs with an incidence of approximately:
- 1 in 58,000 live births (with a confidence interval of 1 in 46,000 to 1 in 80,000) in the United States based on newborn screening data across 11 states (currier2021scidnewbornscreening pages 1-2)
- 1 in 103,240 for SCID in the Chinese population based on large-scale screening in Zhejiang Province, China (chen2024comprehensivenewbornscreening pages 1-2)
- Earlier estimates had placed incidence at about 1 in 50,000 to 100,000 live births globally, though recent assessments based on newborn screening suggest higher rates (kumrah2020geneticsofsevere pages 1-2, vignesh2021clinicalimmunologicaland pages 2-3)

In countries with high consanguinity rates, incidence may be as high as 1 in 3,000 live births (vignesh2021clinicalimmunologicaland pages 2-3).

## Genetic Basis and Causal Genes

SCID is caused by mutations in more than 20 different genes involved in lymphocyte development and function (vignesh2021clinicalimmunologicaland pages 2-3, kumrah2020geneticsofsevere pages 2-4). The major causal genes identified include:

**X-linked SCID (most common in Western populations):**
- IL2RG (encoding the common gamma chain of IL-2 receptor) - accounts for approximately 50% of SCID cases in the US, Canada, and Europe (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, vignesh2021clinicalimmunologicaland pages 2-3)

**Autosomal recessive forms (more common in populations with high consanguinity):**
- RAG1 and RAG2 (recombination activating genes) - most common in countries with high consanguinity rates (vignesh2021clinicalimmunologicaland pages 2-3, kumrah2020geneticsofsevere pages 2-4)
- ADA (adenosine deaminase) - accounts for approximately 15% of all SCID cases (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2)
- JAK3 (Janus kinase 3)
- DCLRE1C (Artemis/DNA cross-link repair enzyme 1c)
- IL7RA (IL-7 receptor alpha chain)
- Other genes: NHEJ1, LIG4, PRKDC, CD3D, CD3E, CD3Z, PTPRC, AK2, PNP, and others (vignesh2021clinicalimmunologicaland pages 2-3, kumrah2020geneticsofsevere pages 2-4)

## Clinical Manifestations and Phenotypes

### Primary Symptoms:
- Recurrent and severe opportunistic infections (bacterial, viral, fungal, and protozoal) beginning in early infancy (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, vignesh2021clinicalimmunologicaland pages 1-2)
- Persistent oral thrush
- Disseminated BCG infection (in countries with universal BCG vaccination)
- Disseminated cytomegalovirus infection
- Chronic diarrhea
- Failure to thrive (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, vignesh2021clinicalimmunologicaland pages 1-2)

### Age of Onset:
- Symptoms typically present before 3 months of age (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2)
- Median age of symptom onset: 2.5 months (interquartile range 1-5 months) based on Indian cohort (vignesh2021clinicalimmunologicaland pages 2-3)
- Median age at diagnosis: 5 months (interquartile range 3.5-8 months) (vignesh2021clinicalimmunologicaland pages 2-3)

### Classification:
SCID can be classified as:
1. **Typical SCID**: Characterized by gene mutations with severe infections, diarrhea, lack of T cells (<0.05 × 10⁹/L autologous T cells), reduction in naive T cells, and absence of proliferative responses to mitogens (dhomakonda2025areviewon pages 1-2, dvorak2023thediagnosisof pages 1-3)
2. **Atypical/Leaky SCID**: CD3+ > 300 cells/μL with diminished but detectable proliferative response to PHA (>10-30% of control) (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, dhomakonda2025areviewon pages 1-2)
3. **Variant SCID**: No known gene defect with 300-1500 T cells/L with reduced function (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, dhomakonda2025areviewon pages 1-2)
4. **Omenn Syndrome**: Characterized by generalized erythematous rash, elevated IgE, eosinophilia, hepatosplenomegaly, and lymphadenopathy (dvorak2023thediagnosisof pages 1-3, vignesh2021clinicalimmunologicaland pages 2-3)

## Diagnostic Approaches

### Newborn Screening:
- T-cell receptor excision circle (TREC) testing from dried blood spots is now the standard newborn screening method for SCID (chen2024comprehensivenewbornscreening pages 1-2, currier2021scidnewbornscreening pages 1-2)
- Universal newborn screening for SCID was added to the US Recommended Uniform Screening Panel in 2010, and by 2019 all US states had adopted TREC-based screening (currier2021scidnewbornscreening pages 1-2)
- Multiplex real-time PCR can simultaneously detect TRECs, KRECs (kappa-deleting recombination excision circles for B-cell deficiencies), and other markers (chen2024comprehensivenewbornscreening pages 1-2)

### Laboratory Testing:
- Flow cytometry for lymphocyte subset analysis (CD3, CD4, CD8, CD19, CD56)
- T-cell proliferation assays
- Genetic testing via Sanger sequencing or next-generation sequencing (vignesh2021clinicalimmunologicaland pages 2-3)

## Treatment Modalities

### Hematopoietic Stem Cell Transplantation (HSCT):
- HSCT is the definitive curative treatment for SCID (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2, slatter2023personalizedhematopoieticstem pages 1-3)
- Early diagnosis and transplantation before onset of infections dramatically improves outcomes (currier2021scidnewbornscreening pages 1-2, slatter2023personalizedhematopoieticstem pages 1-3)
- Survival rates exceed 90% with matched sibling donors (slatter2023personalizedhematopoieticstem pages 1-3)
- In the Indian cohort, only 8.3% (23/277) of patients received HSCT, with 11 survivors; mortality was recorded in 75.8% (210/277) of children, highlighting disparities in access to curative therapy (vignesh2021clinicalimmunologicaland pages 2-3)

### Gene Therapy:
- Autologous hematopoietic stem cell gene therapy has emerged as an alternative to allogeneic HSCT (kohn2023successesandchallenges pages 1-2, bruin2023advancesingene pages 1-2)
- Gene therapy approaches include viral vector-mediated gene addition and gene editing with programmable nucleases (bruin2023advancesingene pages 1-2)
- Long-term safety and efficacy have been demonstrated for ADA-SCID gene therapy, with market authorization granted in Europe (Strimvelis) (bruin2023advancesingene pages 1-2, migliavacca2024longtermandrealworld pages 1-2)
- Gene therapy for X-SCID, Artemis SCID, and other forms has shown clinical success in trials (kohn2023successesandchallenges pages 1-2)
- In one long-term study of 43 patients with ADA-SCID receiving retroviral gene therapy, all patients were alive at data cutoff with median follow-up of 5.0 years, and 2-year intervention-free survival was 88% (migliavacca2024longtermandrealworld pages 1-2)

### Enzyme Replacement Therapy:
- PEG-ADA (pegylated adenosine deaminase) for ADA-deficiency SCID
- Can stabilize patients but provides limited long-term immune reconstitution (migliavacca2024longtermandrealworld pages 1-2)

### Supportive Care:
- Antimicrobial prophylaxis
- Immunoglobulin replacement therapy
- Strict isolation to prevent infections

## Prognosis and Outcomes

### Without Treatment:
- Most children die before age 2 without bone marrow transplantation (dhomakonda2025areviewon pages 1-2)
- Mortality rate of 75.8% was observed in an Indian cohort where most patients did not receive definitive treatment (vignesh2021clinicalimmunologicaland pages 2-3)

### With Early Treatment:
- Patients diagnosed through newborn screening and treated early have significantly better outcomes compared to those diagnosed after developing clinical symptoms (currier2021scidnewbornscreening pages 1-2, slatter2023personalizedhematopoieticstem pages 1-3)
- Overall survival >90% after matched sibling/family donor HSCT (migliavacca2024longtermandrealworld pages 1-2)
- Overall survival >85% after matched unrelated donor HSCT (improved over time) (migliavacca2024longtermandrealworld pages 1-2)

## Animal Models

### Immunodeficient Mouse Models:
Multiple immunodeficient mouse models have been developed to study SCID and test therapies:
- SCID mice (Prkdc mutation) - deficient in T and B lymphocytes but retain NK cells (chen2022thedevelopmentand pages 1-2)
- NOD/SCID mice - improved NK cell defects (chen2022thedevelopmentand pages 1-2)
- NOD/SCID rg^null mice - lacking T, B, and NK cells, considered the gold standard for humanized mouse models (chen2022thedevelopmentand pages 1-2)
- Rag1 and Rag2 knockout mice - lack mature T and B lymphocytes without spontaneous recovery (chen2022thedevelopmentand pages 1-2)

These models are used for xenograft studies, testing gene therapies, and understanding disease pathophysiology.

---

**Limitations of this Response:**

Due to technical difficulties with the evidence gathering system, I was unable to complete the comprehensive, fully-cited report across all 15 sections as specified in your template. A complete report would require:

1. Systematic extraction of specific molecular pathways, cellular processes, and biochemical mechanisms
2. Detailed ontology term mapping (HPO, GO, CL, UBERON, CHEBI, MAXO terms)
3. Comprehensive coverage of environmental factors, epigenetics, and metabolic profiling
4. Detailed therapeutic strategies with MAXO terms
5. Prevention strategies at all levels
6. Comparative biology and veterinary relevance
7. Complete model organism characterization

To provide you with the comprehensive disease knowledge base entry you need, I recommend re-running this analysis or accessing the retrieved papers directly for detailed extraction of the information outlined in sections you specifically require.

References

1. (justizvaillant2023severecombinedimmunodeficiency—classification pages 1-2): Angel A. Justiz-Vaillant, Darren Gopaul, Patrick Eberechi Akpaka, Sachin Soodeen, and Rodolfo Arozarena Fundora. Severe combined immunodeficiency—classification, microbiology association and treatment. Microorganisms, 11:1589, Jun 2023. URL: https://doi.org/10.3390/microorganisms11061589, doi:10.3390/microorganisms11061589. This article has 36 citations.

2. (dhomakonda2025areviewon pages 1-2): Bhavani Dhomakonda, Vankodoth Sireesha, Boddu Shirisha, Gadila Sushma, Mekala Sai Charitha, and T. Rama Rao. A review on types and treatment strategies of severe combined immunodeficiency. Journal of Drug Delivery and Therapeutics, 15:161-167, Mar 2025. URL: https://doi.org/10.22270/jddt.v15i3.7031, doi:10.22270/jddt.v15i3.7031. This article has 0 citations.

3. (dvorak2023thediagnosisof pages 1-3): Christopher C. Dvorak, Elie Haddad, Jennifer Heimall, Elizabeth Dunn, Rebecca H. Buckley, Donald B. Kohn, Morton J. Cowan, Sung-Yun Pai, Linda M. Griffith, Geoffrey D.E. Cuvelier, Hesham Eissa, Ami J. Shah, Richard J. O’Reilly, Michael A. Pulsipher, Nicola A.M. Wright, Roshini S. Abraham, Lisa Forbes Satter, Luigi D. Notarangelo, and Jennifer M. Puck. The diagnosis of severe combined immunodeficiency (scid): the primary immune deficiency treatment consortium (pidtc) 2022 definitions. Journal of Allergy and Clinical Immunology, 151:539-546, Feb 2023. URL: https://doi.org/10.1016/j.jaci.2022.10.022, doi:10.1016/j.jaci.2022.10.022. This article has 157 citations and is from a highest quality peer-reviewed journal.

4. (vignesh2021clinicalimmunologicaland pages 1-2): Pandiarajan Vignesh, Amit Rawat, Rajni Kumrah, Ankita Singh, Anjani Gummadi, Madhubala Sharma, Anit Kaur, Johnson Nameirakpam, Ankur Jindal, Deepti Suri, Anju Gupta, Alka Khadwal, Biman Saikia, Ranjana Walker Minz, Kaushal Sharma, Mukesh Desai, Prasad Taur, Vijaya Gowri, Ambreen Pandrowala, Aparna Dalvi, Neha Jodhawat, Priyanka Kambli, Manisha Rajan Madkaikar, Sagar Bhattad, Stalin Ramprakash, Raghuram CP, Ananthvikas Jayaram, Meena Sivasankaran, Deenadayalan Munirathnam, Sarath Balaji, Aruna Rajendran, Amita Aggarwal, Komal Singh, Fouzia Na, Biju George, Ankit Mehta, Harsha Prasada Lashkari, Ramya Uppuluri, Revathi Raj, Sandip Bartakke, Kirti Gupta, Sreejesh Sreedharanunni, Yumi Ogura, Tamaki Kato, Kohsuke Imai, Koon Wing Chan, Daniel Leung, Osamu Ohara, Shigeaki Nonoyama, Michael Hershfield, Yu-Lung Lau, and Surjit Singh. Clinical, immunological, and molecular features of severe combined immune deficiency: a multi-institutional experience from india. Frontiers in Immunology, Feb 2021. URL: https://doi.org/10.3389/fimmu.2020.619146, doi:10.3389/fimmu.2020.619146. This article has 62 citations and is from a peer-reviewed journal.

5. (currier2021scidnewbornscreening pages 1-2): Robert Currier and Jennifer M. Puck. Scid newborn screening: what we've learned. The Journal of allergy and clinical immunology, 147 2:417-426, Feb 2021. URL: https://doi.org/10.1016/j.jaci.2020.10.020, doi:10.1016/j.jaci.2020.10.020. This article has 138 citations.

6. (chen2024comprehensivenewbornscreening pages 1-2): Chi Chen, Chao Zhang, Ding-Wen Wu, Bing-Yi Wang, Rui Xiao, Xiao-Lei Huang, Xin Yang, Zhi-Gang Gao, and Ru-Lai Yang. Comprehensive newborn screening for severe combined immunodeficiency, x-linked agammaglobulinemia, and spinal muscular atrophy: the chinese experience. World Journal of Pediatrics, 20:1270-1282, Nov 2024. URL: https://doi.org/10.1007/s12519-024-00846-7, doi:10.1007/s12519-024-00846-7. This article has 12 citations and is from a peer-reviewed journal.

7. (kumrah2020geneticsofsevere pages 1-2): Rajni Kumrah, Pandiarajan Vignesh, Pratap Patra, Ankita Singh, Gummadi Anjani, Poonam Saini, Madhubala Sharma, Anit Kaur, and Amit Rawat. Genetics of severe combined immunodeficiency. Mar 2020. URL: https://doi.org/10.1016/j.gendis.2019.07.004, doi:10.1016/j.gendis.2019.07.004. This article has 88 citations.

8. (vignesh2021clinicalimmunologicaland pages 2-3): Pandiarajan Vignesh, Amit Rawat, Rajni Kumrah, Ankita Singh, Anjani Gummadi, Madhubala Sharma, Anit Kaur, Johnson Nameirakpam, Ankur Jindal, Deepti Suri, Anju Gupta, Alka Khadwal, Biman Saikia, Ranjana Walker Minz, Kaushal Sharma, Mukesh Desai, Prasad Taur, Vijaya Gowri, Ambreen Pandrowala, Aparna Dalvi, Neha Jodhawat, Priyanka Kambli, Manisha Rajan Madkaikar, Sagar Bhattad, Stalin Ramprakash, Raghuram CP, Ananthvikas Jayaram, Meena Sivasankaran, Deenadayalan Munirathnam, Sarath Balaji, Aruna Rajendran, Amita Aggarwal, Komal Singh, Fouzia Na, Biju George, Ankit Mehta, Harsha Prasada Lashkari, Ramya Uppuluri, Revathi Raj, Sandip Bartakke, Kirti Gupta, Sreejesh Sreedharanunni, Yumi Ogura, Tamaki Kato, Kohsuke Imai, Koon Wing Chan, Daniel Leung, Osamu Ohara, Shigeaki Nonoyama, Michael Hershfield, Yu-Lung Lau, and Surjit Singh. Clinical, immunological, and molecular features of severe combined immune deficiency: a multi-institutional experience from india. Frontiers in Immunology, Feb 2021. URL: https://doi.org/10.3389/fimmu.2020.619146, doi:10.3389/fimmu.2020.619146. This article has 62 citations and is from a peer-reviewed journal.

9. (kumrah2020geneticsofsevere pages 2-4): Rajni Kumrah, Pandiarajan Vignesh, Pratap Patra, Ankita Singh, Gummadi Anjani, Poonam Saini, Madhubala Sharma, Anit Kaur, and Amit Rawat. Genetics of severe combined immunodeficiency. Mar 2020. URL: https://doi.org/10.1016/j.gendis.2019.07.004, doi:10.1016/j.gendis.2019.07.004. This article has 88 citations.

10. (slatter2023personalizedhematopoieticstem pages 1-3): Mary Slatter and Su Han Lum. Personalized hematopoietic stem cell transplantation for inborn errors of immunity. Frontiers in Immunology, Apr 2023. URL: https://doi.org/10.3389/fimmu.2023.1162605, doi:10.3389/fimmu.2023.1162605. This article has 32 citations and is from a peer-reviewed journal.

11. (kohn2023successesandchallenges pages 1-2): Donald B. Kohn, Yvonne Y. Chen, and Melissa J. Spencer. Successes and challenges in clinical gene therapy. Gene Therapy, 30:738-746, Nov 2023. URL: https://doi.org/10.1038/s41434-023-00390-5, doi:10.1038/s41434-023-00390-5. This article has 228 citations and is from a peer-reviewed journal.

12. (bruin2023advancesingene pages 1-2): Lisa M. Ott de Bruin, Arjan C. Lankester, and Frank J.T. Staal. Advances in gene therapy for inborn errors of immunity. Current Opinion in Allergy and Clinical Immunology, 23:467-477, Oct 2023. URL: https://doi.org/10.1097/aci.0000000000000952, doi:10.1097/aci.0000000000000952. This article has 32 citations and is from a peer-reviewed journal.

13. (migliavacca2024longtermandrealworld pages 1-2): Maddalena Migliavacca, Federica Barzaghi, Claudia Fossati, Paola M. V. Rancoita, Michela Gabaldo, Francesca Dionisio, Stefania Giannelli, Federica Andrea Salerio, Francesca Ferrua, Francesca Tucci, Valeria Calbi, Vera Gallo, Salvatore Recupero, Giulia Consiglieri, Roberta Pajno, Maria Sambuco, Alessio Priolo, Chiara Ferri, Vittoria Garella, Ilaria Monti, Paolo Silvani, Silvia Darin, Miriam Casiraghi, Ambra Corti, Stefano Zancan, Margherita Levi, Daniela Cesana, Filippo Carlucci, Anna Pituch-Noworolska, Dalia AbdElaziz, Ulrich Baumann, Andrea Finocchi, Caterina Cancrini, Saverio Ladogana, Andrea Meinhardt, Isabelle Meyts, Davide Montin, Lucia Dora Notarangelo, Fulvio Porta, Marlène Pasquet, Carsten Speckmann, Polina Stepensky, Alberto Tommasini, Marco Rabusin, Zeynep Karakas, Miguel Galicchio, Lucia Leonardi, Marzia Duse, Sukru Nail Guner, Clelia Di Serio, Fabio Ciceri, Maria Ester Bernardo, Alessandro Aiuti, and Maria Pia Cicalese. Long-term and real-world safety and efficacy of retroviral gene therapy for adenosine deaminase deficiency. Nature medicine, 30:488-497, Feb 2024. URL: https://doi.org/10.1038/s41591-023-02789-4, doi:10.1038/s41591-023-02789-4. This article has 31 citations and is from a highest quality peer-reviewed journal.

14. (chen2022thedevelopmentand pages 1-2): Jiaxuan Chen, Shuzhen Liao, Zengzhi Xiao, Quanren Pan, Xi Wang, Kangyuan Shen, Shuting Wang, Lawei Yang, Fengbiao Guo, Hua-feng Liu, and Qingjun Pan. The development and improvement of immunodeficient mice and humanized immune system mouse models. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.1007579, doi:10.3389/fimmu.2022.1007579. This article has 224 citations and is from a peer-reviewed journal.