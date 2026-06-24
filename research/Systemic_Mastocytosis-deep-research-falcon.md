---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T08:49:49.721086'
end_time: '2026-06-19T09:05:22.428580'
duration_seconds: 932.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Systemic Mastocytosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Systemic_Mastocytosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Systemic Mastocytosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Systemic Mastocytosis** covering all of the
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
- **Disease Name:** Systemic Mastocytosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Systemic Mastocytosis** covering all of the
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


# Comprehensive Research Report: Systemic Mastocytosis

## 1. Disease Information

**Disease Name:** Systemic Mastocytosis (SM)
**Category:** Complex clonal hematopoietic/mast cell neoplasm

### Overview

Systemic mastocytosis is a rare clonal hematopoietic stem cell disease characterized by abnormal proliferation and accumulation of neoplastic mast cells in extracutaneous organs including bone marrow, skin, gastrointestinal tract, liver, and spleen (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2). The disease is caused by activating KIT mutations, predominantly KIT D816V, which induce ligand-independent KIT receptor activation and downstream signaling, leading to mast cell proliferation, survival, and activation (lee2023recentadvancesin pages 1-2, cilloni2024detectionofkit pages 1-2, toledo2023kitd816vmast pages 1-2). SM affects approximately 1 in 10,000 persons in the adult population according to Orphanet data (cilloni2024detectionofkit pages 1-2).

### Key Identifiers

While specific database identifiers were not fully retrieved, systemic mastocytosis is classified in:
- **WHO Classification:** Recognized as a distinct entity separated from myeloproliferative neoplasms since 2016, with updates in WHO 5th edition (2022) (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2)
- **ICC Classification:** International Consensus Classification (2022) with refined criteria (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)
- **ICD Classification:** Categorized under mast cell disorders
- **Orphanet:** Listed with prevalence data
- **Common Synonyms:** Mast cell disease, clonal mast cell disorder

### Data Sources

Information is derived from both disease-level aggregated resources (classification systems, expert reviews) and individual patient data compiled in registries and clinical studies (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2).

---

## 2. Etiology

### Disease Causal Factors

**Genetic:** The primary causal factor is somatic activating mutations in the KIT gene, most frequently KIT D816V (c.2447A>T, p.Asp816Val), present in 85-90% or >90% of adult SM cases (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, toledo2023kitd816vmast pages 1-2). The KIT D816V mutation is considered the pathogenic driver, inducing constitutive activation of the KIT tyrosine kinase receptor independent of its ligand stem cell factor (SCF), affecting key cellular pathways including proliferation, differentiation, survival, and activation (toledo2023kitd816vmast pages 1-2).

Other less common KIT mutations (<5% of cases) include V560G, D815K, D816Y, D816F, D816H, D820G, and insVI815-816 (pardanani2023systemicmastocytosisin pages 1-2).

**Mechanistic:** KIT encodes a Type III receptor tyrosine kinase expressed on mast cells, hematopoietic stem cells, germ cells, melanocytes, and interstitial cells of Cajal. The interaction between KIT and SCF plays a critical role in mast cell development, proliferation, maturation, chemotaxis, adhesion, and survival (pardanani2023systemicmastocytosisin pages 1-2, li2023reviewandupdates pages 2-4). Gain-of-function KIT mutations cause ligand-independent receptor activation and constitutive downstream signaling (toledo2023kitd816vmast pages 1-2).

### Risk Factors

**Genetic Risk Factors:**
- Multilineage involvement of hematopoiesis by KIT D816V is associated with higher tumor burden, additional mutations, and increased transformation risk to advanced SM (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)
- Co-occurring somatic mutations in genes frequently mutated in myeloid neoplasms, including ASXL1, RUNX1, SRSF2, NRAS, TET2, DNMT3A, CBL, EZH2, JAK2, KRAS, and SF3B1, are identified particularly in advanced SM and correlate with disease progression and poor survival (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)
- Approximately 12 genes (ASXL1, CBL, DNMT3A, EZH2, JAK2, KRAS, NRAS, SF3B1, RUNX1, SRSF2, TET2) are recurrently mutated in SM
- Hereditary alpha-tryptasemia (HαT), an autosomal dominant trait caused by increased TPSAB1 gene copy number encoding alpha-tryptase, shows increased prevalence (estimated 2-3×) in SM patients and may modify disease severity and symptom expression (beyens2023mastocytosisandrelated pages 1-5, li2023reviewandupdates pages 2-4)

**Environmental Risk Factors:** Given the clonal/genetic nature of SM, specific environmental risk factors have not been established. Age influences presentation—adults typically present between ages 20-50, while pediatric cutaneous mastocytosis occurs in ~75-80% of cases within the first two years of life (cilloni2024detectionofkit pages 1-2).

**Sex:** Male-to-female ratio is approximately 1:1 (cilloni2024detectionofkit pages 1-2).

### Protective Factors

No specific genetic or environmental protective factors have been identified given the clonal somatic mutation etiology.

### Gene-Environment Interactions

Not well established for SM given its clonal nature driven by somatic KIT mutations.

---

## 3. Phenotypes

| Classification domain | WHO 5th edition / ICC 2022 update | Key details | Evidence |
|---|---|---|---|
| Disease definition | Systemic mastocytosis (SM) | Rare clonal hematopoietic/mast cell neoplasm characterized by abnormal mast cell accumulation in extracutaneous organs; diagnosis integrates morphology, immunophenotype, molecular findings, and clinical features. Adult disease is usually systemic and clinically heterogeneous. | (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2) |
| Broad subtype grouping | Non-advanced SM | Includes bone marrow mastocytosis (BMM), indolent SM (ISM), and smoldering SM (SSM); generally lacks overt organ damage from mast cell infiltration. | (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2) |
| Broad subtype grouping | Advanced SM | Includes aggressive SM (ASM), SM with associated hematologic neoplasm (SM-AHN; ICC often uses SM-AMN for associated myeloid neoplasm), and mast cell leukemia (MCL); defined by organ damage, high disease burden, or associated hematologic malignancy. | (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2) |
| Major diagnostic criterion | WHO 2022 / ICC 2022 | Multifocal dense aggregates of mast cells (≥15 mast cells per aggregate) in bone marrow and/or other extracutaneous organs. ICC specifies tryptase- and/or CD117-positive mast cells in tissue sections. | (pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Minor diagnostic criterion 1 | WHO 2022 / ICC 2022 | ≥25% atypical or spindle-shaped mast cells in marrow smears/infiltrates; ICC wording emphasizes spindle-shaped or atypical immature morphology in marrow or extracutaneous tissue. | (cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Minor diagnostic criterion 2 | WHO 2022 / ICC 2022 | Activating KIT mutation present in bone marrow, blood, or extracutaneous tissue; recent criteria accept KIT D816V or another activating KIT mutation, not only codon 816. | (lee2023recentadvancesin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Minor diagnostic criterion 3 | WHO 2022 / ICC 2022 | Aberrant mast-cell expression of CD25 and/or CD2 and/or CD30. A key 2022-2023 update is incorporation of CD30 as a minor criterion. | (lee2023recentadvancesin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Minor diagnostic criterion 4 | WHO 2022 / ICC 2022 | Persistent baseline serum tryptase >20 ng/mL; does not count in SM with associated myeloid neoplasm in some settings, and should be interpreted with adjustment/caution in hereditary alpha-tryptasemia. | (pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Diagnostic rule | WHO 2022 / ICC 2022 | Diagnosis requires 1 major + 1 minor criterion, or if no major criterion is present, at least 3 minor criteria. | (pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| KIT mutation frequency | Adult SM overall | KIT mutations are present in >90% of mastocytosis/SM cases overall; KIT D816V is the dominant driver. Recent reviews report ~85–90% or >90% in adult SM; another 2023 review states ~90% of SM. | (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, toledo2023kitd816vmast pages 1-2) |
| BMM | WHO 2022 recognized subtype; also retained in current frameworks | Fulfills SM criteria, no skin lesions, no B-findings/C-findings, low disease burden, and no criteria for MCL or SM-AHN. Often suspected in severe anaphylaxis without skin lesions or unexplained osteoporosis/fracture. Prognosis is generally favorable/non-advanced. | (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, cilloni2024detectionofkit pages 1-2, beyens2023mastocytosisandrelated pages 5-8) |
| ISM | WHO 2022 recognized subtype; retained in ICC-era practice | Most common adult SM subtype; usually bone marrow infiltration <20%, no associated hematologic disease, at most 1 B-finding and no C-findings. Typical manifestations are mediator-related symptoms such as flushing, pruritus, GI symptoms, anaphylaxis, and osteoporosis/osteopenia. Life expectancy is often near normal. | (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2) |
| SSM | WHO 2022 recognized subtype; retained in ICC-era practice | SM with ≥2 B-findings and no C-findings; reflects higher mast cell burden than ISM and higher risk of progression to advanced SM. Clinical burden may include organomegaly without dysfunction, high tryptase, and marrow mast-cell burden. Prognosis is intermediate between ISM and advanced SM. | (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, lee2023recentadvancesin pages 3-5) |
| ASM | WHO 2022 recognized subtype; retained in ICC-era practice | Defined by one or more C-findings indicating organ damage due to mast cell infiltration. Clinical features may include cytopenias, malabsorption, hepatosplenomegaly, ascites, pathologic fractures, and organ dysfunction. Prognosis is poor relative to non-advanced SM. | (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5, toledo2023kitd816vmast pages 1-2) |
| SM-AHN / SM-AMN | WHO uses SM-AHN; Pardanani 2023 and ICC-focused sources emphasize SM-AMN for associated myeloid neoplasm | SM coexists with another hematologic neoplasm, commonly myeloid. Clinical course and management are strongly influenced by the associated neoplasm; tryptase may be less specific diagnostically. Prognosis is generally poor and depends on both SM burden and associated neoplasm biology. | (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| MCL | WHO 2022 recognized subtype; retained in ICC-era practice | Rare leukemic form with very high mast cell burden; may be aleukemic in some cases. Associated with severe systemic disease, rapid progression, and the worst prognosis among SM subtypes. | (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, toledo2023kitd816vmast pages 1-2) |
| B-findings | WHO/ICC disease burden markers | Used mainly to distinguish ISM from SSM; reflect high mast-cell burden without overt organ damage. Examples include high marrow mast-cell burden and markedly elevated tryptase. | (pardanani2023systemicmastocytosisin pages 1-2, lee2023recentadvancesin pages 3-5) |
| C-findings | WHO/ICC organ damage markers | Define aggressive disease/ASM when organ dysfunction is attributable to mast cell infiltration; examples include cytopenias, malabsorption/weight loss, liver dysfunction/portal hypertension/ascites, large osteolytic lesions/pathologic fractures, and hypersplenism. | (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, lee2023recentadvancesin pages 3-5) |
| Frequent symptom clusters across SM | Clinical phenotype summary | Recurrent anaphylaxis, flushing, pruritus/itching, urticaria/angioedema, abdominal pain, nausea, vomiting, diarrhea, syncope/presyncope, tachycardia, osteoporosis/osteopenia, and in advanced disease cytopenias and hepatosplenomegaly. | (cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5, beyens2023mastocytosisandrelated pages 5-8) |
| Important 2022-2023 classification updates | WHO 5th edition / ICC 2022 | Key refinements include recognition of BMM, addition of CD30 as a minor criterion, acceptance of any activating KIT mutation as a molecular minor criterion, continued integration of marrow morphology + immunophenotype + molecular testing, and refined B-/C-finding assessment for subtype assignment. | (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5) |
| Prognostic modifiers beyond subtype | Molecular risk stratification | Poor-risk co-mutations include ASXL1, RUNX1, SRSF2, and NRAS; multilineage KIT involvement and additional myeloid mutations are linked to progression and worse survival, especially in advanced SM. | (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, toledo2023kitd816vmast pages 1-2) |


*Table: This table summarizes systemic mastocytosis classification, diagnostic criteria, KIT mutation patterns, subtype-defining features, and prognosis using recent WHO 2022 and ICC 2022/2023-aligned sources. It is useful as a compact reference for comparing non-advanced and advanced SM entities.*

### Clinical Manifestations by Phenotype Type

**Symptoms Related to Mast Cell Mediator Release (Frequency: Common to Very Common in All SM Subtypes):**
- **HP:0001025** Urticaria (hives)
- **HP:0000989** Pruritus (itching)
- **HP:0000963** Flushing
- **HP:0002014** Diarrhea
- **HP:0002027** Abdominal pain
- **HP:0002017** Nausea and vomiting
- **HP:0012115** Hepatomegaly
- **HP:0001744** Splenomegaly
- **HP:0000822** Hypertension (or hypotension during anaphylaxis)
- **HP:0001962** Palpitations/tachycardia
- **HP:0001279** Syncope or presyncope
- **HP:0012378** Fatigue
- **HP:0001945** Fever

Severity: Variable from mild to life-threatening
Progression: Episodic or chronic
Frequency: Occurs in majority of SM patients (cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5, beyens2023mastocytosisandrelated pages 5-8)

**Anaphylaxis (Frequency: Common, especially with hymenoptera venom allergy):**
- **HP:0000969** Edema
- **HP:0025085** Bloody diarrhea (in severe cases)
- **HP:0002098** Respiratory distress
- **HP:0001297** Stroke (rare, severe)

Severity: Can be life-threatening
Onset: Acute, triggered
Frequency: Recurrent unprovoked anaphylaxis is a red flag for SM (beyens2023mastocytosisandrelated pages 1-5, beyens2023mastocytosisandrelated pages 5-8)

**Cutaneous Manifestations (Frequency: Common in Indolent SM, Variable in Advanced SM):**
- **HP:0001030** Fragile skin (in diffuse cutaneous mastocytosis)
- **HP:0007434** Generalized hyperpigmentation
- **HP:0000992** Cutaneous photosensitivity (Darier's sign—whealing upon stroking lesions)
- Maculopapular cutaneous mastocytosis (urticaria pigmentosa): red-brown macules/papules

Severity: Variable
Age of onset: Childhood for cutaneous mastocytosis, adult-onset often indicates ISM
Frequency: Present in majority of ISM cases; less common in advanced SM (beyens2023mastocytosisandrelated pages 1-5, beyens2023mastocytosisandrelated pages 5-8)

**Skeletal/Bone Manifestations (Frequency: Very Common, 30-75% of ISM patients):**
- **HP:0000939** Osteoporosis
- **HP:0002659** Increased susceptibility to fractures (pathological fractures)
- **HP:0100774** Hyperostosis (osteosclerosis in advanced disease)
- **HP:0002653** Bone pain

Severity: Moderate to severe, major source of morbidity especially in young men
Age of onset: Adult
Progression: Can be progressive in advanced SM (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, lee2023recentadvancesin pages 3-5, beyens2023mastocytosisandrelated pages 5-8)

**Hematological Abnormalities (Frequency: Common in Advanced SM, Rare in ISM):**
- **HP:0001903** Anemia
- **HP:0001873** Thrombocytopenia
- **HP:0001876** Pancytopenia
- **HP:0001880** Eosinophilia

Severity: Severe in advanced SM (C-finding)
Frequency: Defining feature of aggressive SM when present as organ dysfunction (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, lee2023recentadvancesin pages 3-5)

**Gastrointestinal Manifestations (Frequency: Common):**
- **HP:0002570** Steatorrhea
- **HP:0004325** Decreased body weight (malabsorption)
- **HP:0001824** Weight loss

Severity: Variable, severe in advanced SM
Frequency: Common in ISM (mediator-related), defining C-finding when malabsorption present in ASM (beyens2023mastocytosisandrelated pages 1-5, lee2023recentadvancesin pages 3-5)

**Hepatosplenic Manifestations (Frequency: Common in Advanced SM):**
- **HP:0001392** Abnormality of the liver
- **HP:0001410** Decreased liver function
- **HP:0001403** Macrovesicular hepatic steatosis
- **HP:0001541** Ascites
- **HP:0001409** Portal hypertension

Severity: Severe when present
Frequency: C-finding in advanced SM (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, lee2023recentadvancesin pages 3-5)

**Neuropsychiatric Manifestations (Frequency: Less Common but Recognized):**
- **HP:0002315** Headache
- **HP:0001250** Seizures
- **HP:0002076** Migraine
- **HP:0000709** Psychosis (rare)
- **HP:0000716** Depression

Severity: Variable
Frequency: Reported but less systematically studied (cilloni2024detectionofkit pages 1-2)

### Quality of Life Impact

Quality of life is significantly impaired across SM subtypes due to chronic symptoms, unpredictable anaphylaxis risk, bone disease with fracture risk, and in advanced disease, organ dysfunction. Mediator-related symptoms including flushing, pruritus, gastrointestinal disturbances, fatigue, and recurrent anaphylaxis substantially reduce daily functioning. Bone involvement causes chronic pain and mobility limitations. Advanced SM is associated with markedly reduced quality of life and life expectancy (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2).

---

## 4. Genetic/Molecular Information

### Causal Genes

**Primary Gene:** KIT (HGNC:6342, OMIM:164920)
**Gene Product:** KIT proto-oncogene, receptor tyrosine kinase (CD117)
**Chromosomal Location:** 4q12

### Pathogenic Variants

**Most Common Mutation:**
- KIT p.D816V (c.2447A>T): Present in 85-90% or >90% of adult SM cases
- Variant type: Missense mutation
- Allele frequency: Somatic mutation, not present in germline in typical SM
- Variant classification: Pathogenic driver mutation
- Functional consequence: Gain of function—constitutive KIT activation independent of SCF ligand
- Origin: Somatic (acquired), rarely germline in familial cases (~1.5% of mastocytosis) (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, toledo2023kitd816vmast pages 1-2)

**Other KIT Mutations (<5-10% of SM cases):**
- V560G (exon 11)
- D815K
- D816Y
- D816F
- D816H
- D820G
- insVI815-816
- Variant classification: Pathogenic
- Functional consequence: Gain of function
- Origin: Somatic (pardanani2023systemicmastocytosisin pages 1-2)

**Pediatric CM-Associated KIT Mutations:**
- Present in approximately 30% of childhood cutaneous mastocytosis
- Often involve different codons than D816V
- Some may be germline or early postzygotic (pardanani2023systemicmastocytosisin pages 1-2)

### Co-occurring Mutations (Associated Hematologic Neoplasm Component, Prognostic Impact)

**High-Risk Mutations Associated with Progression and Poor Survival:**
- ASXL1 (Additional Sex Combs Like 1): Epigenetic regulator
- RUNX1 (Runt-related transcription factor 1): Transcription factor
- SRSF2 (Serine and arginine rich splicing factor 2): Splicing factor
- NRAS (Neuroblastoma RAS viral oncogene homolog): Signaling molecule
- Variant type: Various (missense, frameshift, nonsense)
- Functional consequence: Loss of function (tumor suppressors/regulators) or gain of function (oncogenes)
- Origin: Somatic
- Frequency: Variable, enriched in advanced SM (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

**Other Recurrently Mutated Genes:**
- TET2 (Ten-eleven translocation 2): Epigenetic regulator
- DNMT3A (DNA methyltransferase 3 alpha): DNA methylation
- CBL (Casitas B-lineage lymphoma): E3 ubiquitin ligase
- EZH2 (Enhancer of zeste homolog 2): Histone methyltransferase
- JAK2, KRAS, SF3B1
- Origin: Somatic (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

### Modifier Genes

Hereditary alpha-tryptasemia (HαT) genotype:
- Gene: TPSAB1 (Tryptase alpha/beta 1)
- Mechanism: Germline copy number variation—increased copies of alpha-tryptase-encoding TPSAB1
- Effect: Elevates baseline serum tryptase levels (typically >8 ng/mL)
- Prevalence in general population: ~5%
- Prevalence in SM: Increased 2-3× compared to general population
- Impact: May modify symptom severity, particularly anaphylaxis risk, though clinical impact remains under investigation (beyens2023mastocytosisandrelated pages 1-5, li2023reviewandupdates pages 2-4)

### Epigenetic Information

Epigenetic dysregulation is implicated through mutations in epigenetic modifier genes including TET2 (demethylation), DNMT3A (DNA methylation), ASXL1 (chromatin remodeling), and EZH2 (histone methylation). These alterations affect gene expression and contribute to disease progression, particularly in advanced SM (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2).

### Chromosomal Abnormalities

Complex karyotype is identified as an adverse prognostic factor in advanced SM, associated with significantly worse overall survival (HR 4.2 [1.8-10.0], p=0.016 in allogeneic transplant cohort). Specific recurrent chromosomal translocations are not characteristic of typical SM, but cytogenetic abnormalities may be seen in associated hematologic neoplasms (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2).

---

## 5. Environmental Information

### Environmental Factors

Given the clonal genetic nature of SM driven by somatic KIT mutations, specific environmental toxins, radiation, or occupational exposures have not been established as causal factors.

### Lifestyle Factors

No specific lifestyle factors (smoking, diet, exercise, alcohol) have been established as causal. However, patients are advised to avoid known mast cell triggers including certain medications (NSAIDs, opiates, contrast agents), alcohol, temperature extremes, and physical/emotional stress to prevent mediator release and anaphylaxis (beyens2023mastocytosisandrelated pages 1-5).

### Infectious Agents

Not applicable—SM is not caused by infectious agents.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**KIT Signaling Cascade:**
- KIT receptor tyrosine kinase activation (normally by SCF binding, constitutive in KIT D816V)
- Receptor dimerization and autophosphorylation
- Activation of downstream pathways:
  - **MAPK/ERK pathway** (GO:0000165): Cell proliferation, differentiation
  - **PI3K-AKT-mTOR pathway** (GO:0014065): Cell survival, growth, metabolism
  - **JAK-STAT pathway** (GO:0007259): Gene transcription, proliferation
  - **Src family kinases:** Various signaling functions
- Result: Enhanced mast cell proliferation, survival, maturation defects, and activation (pardanani2023systemicmastocytosisin pages 1-2, li2023reviewandupdates pages 2-4, toledo2023kitd816vmast pages 1-2)

**FcεRI-Mediated Signaling:**
- High-affinity IgE receptor on mast cells
- Cross-linking by antigen-bound IgE triggers degranulation
- Synergistic enhancement with KIT signaling in neoplastic mast cells
- Contributes to mediator release and clinical symptoms (li2023reviewandupdates pages 2-4)

### Cellular Processes

**Abnormal Mast Cell Proliferation and Survival (GO:0008283, GO:0043066):**
- Constitutive KIT activation drives unchecked proliferation
- Resistance to apoptosis through PI3K-AKT pathway
- Accumulation in tissues (bone marrow, skin, GI tract, liver, spleen, bone) (pardanani2023systemicmastocytosisin pages 1-2, li2023reviewandupdates pages 2-4, toledo2023kitd816vmast pages 1-2)

**Impaired Mast Cell Differentiation and Maturation:**
- Abnormal mast cell morphology: spindle-shaped, hypogranular, atypical nuclei
- Aberrant immunophenotype: CD25+, CD2+, and/or CD30+ expression (normally absent on mature mast cells)
- Retained high CD117 (KIT) expression (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5)

**Mast Cell Activation and Degranulation (GO:0043303, GO:0043304):**
- Enhanced mediator release: histamine, tryptase, prostaglandin D2 (PGD2), leukotrienes (LTC4, LTD4, LTE4), platelet-activating factor
- Cytokine release: TNF-α, TNF-β, IL-1, IL-2, IL-3, IL-4, IL-5, IL-6, IL-9, IL-10, IL-13, GM-CSF
- Chemokine release: IL-8, MCP-1, MIP-1α
- Clinical manifestations: flushing, pruritus, urticaria, GI symptoms, anaphylaxis, cardiovascular symptoms (li2023reviewandupdates pages 2-4)

**Cell Type Involved:**
- Primary: Neoplastic mast cells (CL:0000097)
- Secondary: Osteoclasts, osteoblasts (bone disease), various inflammatory cells recruited by mast cell mediators

### Protein Dysfunction

**KIT Receptor:**
- Normal function: Ligand (SCF)-dependent activation, tightly regulated signaling
- Mutant KIT D816V: Constitutive activation independent of ligand
- Structural impact: Mutation in activation loop of tyrosine kinase domain stabilizes active conformation
- Resistance to some tyrosine kinase inhibitors (e.g., imatinib) (pardanani2023systemicmastocytosisin pages 1-2, toledo2023kitd816vmast pages 1-2)

### Metabolic Changes

Specific metabolic pathway alterations have not been comprehensively characterized, though mast cell mediators affect various metabolic processes including vascular permeability, smooth muscle contraction, and inflammatory responses.

### Immune System Involvement

**Mast Cell Function in Immunity:**
- Normally: Sentinel cells in innate and adaptive immunity, allergic reactions
- In SM: Dysregulated activation leads to chronic inflammation, exaggerated allergic responses, increased anaphylaxis risk
- Mechanism: Both IgE-dependent and IgE-independent mast cell activation
- Immune mediators: Cytokines, chemokines driving inflammatory milieu (li2023reviewandupdates pages 2-4)

### Tissue Damage Mechanisms

**Bone Involvement:**
- Dual effects: Osteoporosis (most common in ISM) and osteosclerosis (advanced SM)
- Pathogenesis: Mast cell-derived mediators (histamine, tryptase, TNF-α, IL-6, RANKL) promote osteoclastogenesis, suppress osteoblast function
- Outcome: Pathological fractures, bone pain, skeletal deformity (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2)

**Organ Infiltration (Advanced SM):**
- Mast cell accumulation in bone marrow, liver, spleen, GI tract
- Mechanisms: Direct infiltration causing organ dysfunction, fibrosis
- C-findings: Cytopenias (marrow), hepatic dysfunction/portal hypertension/ascites (liver), hypersplenism (spleen), malabsorption (GI) (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, lee2023recentadvancesin pages 3-5)

### Biochemical Abnormalities

- Elevated serum tryptase (>20 ng/mL): Reflects mast cell burden
- Elevated urinary histamine metabolites (N-methylhistamine, 1-methyl-4-imidazoleacetic acid)
- Increased prostaglandin D2 and leukotrienes
- These serve as biomarkers of mast cell activation and burden (li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5)

### Molecular Profiling

**Transcriptomics:**
- KIT D816V mast cells show upregulated expression of genes involved in innate immunity, inflammatory responses, and proliferation
- iPSC-derived KIT D816V mast cells recapitulate SM transcriptional signatures (toledo2023kitd816vmast pages 1-2)

**Proteomics:**
- Increased tryptase (beta-tryptase primarily), chymase, carboxypeptidase A3
- Aberrant surface markers: CD25, CD2, CD30 (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs Directly Affected:**
- **Bone marrow (UBERON:0002371):** Universal involvement in SM; dense mast cell infiltrates, spindle-shaped morphology
- **Skin (UBERON:0002097):** Maculopapular cutaneous involvement in ISM, less common in advanced SM
- **Bone (UBERON:0001474):** Osteoporosis, osteosclerosis, pathological fractures
- **Gastrointestinal tract (UBERON:0001555):** Mast cell infiltration, malabsorption in advanced disease
- **Liver (UBERON:0002107):** Hepatomegaly, portal fibrosis, dysfunction in advanced SM
- **Spleen (UBERON:0002106):** Splenomegaly, hypersplenism in advanced SM
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5, beyens2023mastocytosisandrelated pages 5-8)

**Secondary Organ Involvement:**
- Lymph nodes (UBERON:0000029): Lymphadenopathy in advanced disease
- Cardiovascular system (UBERON:0004535): Hypotension, tachycardia from mediator release, rare cardiac involvement

**Body Systems Involved:**
- Hematopoietic system (UBERON:0002390)
- Integumentary system (UBERON:0002416)
- Skeletal system (UBERON:0001434)
- Digestive system (UBERON:0001007)
- Immune system (UBERON:0002405)

### Tissue and Cell Level

**Tissue Types Affected:**
- Hematopoietic/lymphoid tissue (UBERON:0002193)
- Connective tissue (UBERON:0002384): Bone matrix, skin dermis
- Epithelial tissue (UBERON:0000483): GI mucosa

**Specific Cell Populations:**
- **Neoplastic mast cells (CL:0000097):** Abnormal morphology, immunophenotype, and function
- Osteoclasts (CL:0000092) and osteoblasts (CL:0000062): Dysregulated in bone disease
- Hepatocytes (CL:0000182): Affected in hepatic involvement
- Hematopoietic stem cells (CL:0000037): May harbor KIT D816V in multilineage involvement

### Subcellular Level

**Cellular Compartments Involved (GO Cellular Component):**
- Plasma membrane (GO:0005886): KIT receptor localization
- Cytoplasmic granules (GO:0031410): Mast cell secretory granules containing mediators
- Nucleus (GO:0005634): Altered gene transcription
- Mitochondria (GO:0005739): Involved in cellular metabolism and survival signaling

### Localization

**Anatomical Sites:**
- Bone marrow: Paratrabecular and perisinusoidal distribution of mast cells
- Skin: Dermis, perivascular areas
- GI tract: Lamina propria
- Liver: Portal areas
- Distribution: Bilateral, systemic (li2023reviewandupdates pages 2-4)

---

## 8. Temporal Development

### Onset

**Typical Age of Onset:**
- Adults: 20-50 years for systemic mastocytosis
- Children: 75-80% of cutaneous mastocytosis cases occur within first 2 years of life
- Pediatric CM often regresses spontaneously at puberty; adult-onset SM typically persists (beyens2023mastocytosisandrelated pages 1-5, cilloni2024detectionofkit pages 1-2)

**Onset Pattern:**
- Variable: Can be insidious (gradual symptom onset) or acute (sudden anaphylaxis)
- Many patients have long-standing symptoms before diagnosis (beyens2023mastocytosisandrelated pages 1-5)

### Progression

**Disease Stages:**
- **Non-advanced SM:** BMM, ISM, SSM—low mast cell burden, preserved organ function
- **Advanced SM:** ASM, SM-AHN, MCL—high disease burden, organ dysfunction (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

**Progression Rate:**
- ISM: Typically slow or stable, near-normal life expectancy
- SSM: Higher risk of progression to advanced SM (≥2 B-findings)
- ASM/SM-AHN/MCL: Rapid, aggressive course with poor prognosis
(li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Disease Course Pattern:**
- ISM: Chronic, stable or slowly progressive
- SSM: Chronic with risk of transformation
- ASM: Progressive
- MCL: Rapidly progressive
- Disease duration: Typically lifelong once established (except pediatric CM) (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5)

### Patterns

**Remission:**
- Spontaneous remission: Common in pediatric cutaneous mastocytosis (~50-80% by adolescence)
- Treatment-induced remission: Possible with tyrosine kinase inhibitors (midostaurin, avapritinib) but typically not curative
- Allogeneic stem cell transplant: Only potentially curative therapy (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Critical Periods:**
- Diagnosis: Early recognition critical for anaphylaxis prevention
- Transformation: SSM to ASM transformation represents critical disease acceleration
- Treatment initiation: Advanced SM requires prompt cytoreductive therapy (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence:** Approximately 1 case per 10,000 persons in adults (Orphanet data) (cilloni2024detectionofkit pages 1-2)

**Incidence:** Specific annual incidence data not well established due to disease rarity and diagnostic challenges.

### For Genetic Etiology

**Inheritance Pattern:**
- Typical SM: Sporadic, acquired somatic KIT mutations (non-inherited)
- Familial mastocytosis: Extremely rare (~1.5% of cases), may involve germline KIT mutations, pattern unclear but likely autosomal dominant with variable penetrance (beyens2023mastocytosisandrelated pages 1-5, cilloni2024detectionofkit pages 1-2)

**Penetrance:**
- Somatic KIT D816V: Not applicable (acquired)
- Germline KIT mutations (familial): Likely incomplete penetrance given rarity

**Expressivity:**
- Highly variable clinical phenotypes from indolent to aggressive disease
- Influenced by co-occurring mutations, multilineage involvement, and HαT status (lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Genetic Anticipation:** Not described

**Germline Mosaicism:** May occur but not well characterized

**Founder Effects:** Not described for KIT D816V as it arises somatically

**Consanguinity Role:** Not relevant for sporadic somatic mutations

**Carrier Frequency:** Not applicable (somatic disease)

### Population Demographics

**Affected Populations:**
- No specific ethnic predilection documented
- Affects diverse populations globally (cilloni2024detectionofkit pages 1-2)

**Geographic Distribution:**
- Worldwide distribution
- No known endemic areas (cilloni2024detectionofkit pages 1-2)

**Sex Ratio:**
- Approximately 1:1 male:female (cilloni2024detectionofkit pages 1-2)

**Age Distribution:**
- Adults: Peak onset 20-50 years
- Children: Peak onset <2 years for cutaneous forms (beyens2023mastocytosisandrelated pages 1-5, cilloni2024detectionofkit pages 1-2)

---

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests:**
- **Serum tryptase (LOINC:2338-5):** Baseline serum tryptase >20 ng/mL is a minor diagnostic criterion; normal range 1-15 ng/mL; must be adjusted for hereditary alpha-tryptasemia. Tryptase >200 ng/mL is a B-finding (high disease burden) (pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5)
- Complete blood count: Assess for cytopenias, eosinophilia
- Liver function tests: Assess hepatic involvement
- Serum alkaline phosphatase: May be elevated (B-finding)
- Serum albumin: May be decreased (malabsorption, C-finding)
- Urinary histamine metabolites: N-methylhistamine, 1-methyl-4-imidazoleacetic acid (mast cell activation markers)

**Biomarkers:**
- **Tryptase (serum, beta-tryptase isoforms):** Most specific mast cell biomarker, reflects burden and activation
- **CD25, CD2, CD30:** Aberrant surface markers on neoplastic mast cells (minor diagnostic criteria)
- Prostaglandin D2 and metabolites: Mast cell activation
- IgE levels: Assess atopic background (pardanani2023systemicmastocytosisin pages 1-2, li2023reviewandupdates pages 2-4, lee2023recentadvancesin pages 3-5)

**Imaging Studies:**
- **Bone densitometry (DEXA scan):** Evaluate osteoporosis/osteosclerosis
- **CT scan:** Assess organomegaly, lymphadenopathy, skeletal lesions
- **MRI:** Detailed bone marrow and organ assessment
- Abdominal ultrasound: Hepatosplenomegaly screening (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, beyens2023mastocytosisandrelated pages 5-8)

**Biopsy Findings:**
- **Bone marrow biopsy (major diagnostic criterion):** Multifocal dense aggregates of ≥15 mast cells (tryptase+, CD117+)
- Histopathology: Spindle-shaped or atypical mast cell morphology
- Immunohistochemistry: CD117+, tryptase+, CD25+, CD2+, and/or CD30+ (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5)

**Flow Cytometry:**
- Bone marrow or peripheral blood
- Aberrant mast cell immunophenotype: CD117+, CD25+, CD2+, CD30+
- Helps confirm minor diagnostic criteria (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, lee2023recentadvancesin pages 3-5)

### Genetic Testing

**Recommended Approach:**
- High-sensitivity KIT mutation testing from bone marrow or peripheral blood
- Test for KIT D816V first (most common)
- If negative, test for other KIT mutations (D815K, D816Y, V560G, etc.)

**Molecular Methods:**
- **Allele-specific PCR (AS-PCR):** High sensitivity for KIT D816V (detection limit ~0.1-1% variant allele frequency)
- **Digital droplet PCR (ddPCR):** Very high sensitivity (<0.01% VAF)
- **Next-generation sequencing (NGS):** Panel testing for KIT and co-occurring mutations (ASXL1, RUNX1, SRSF2, NRAS, TET2, etc.); standard NGS may miss low-VAF KIT mutations
- Bone marrow preferred over blood for highest sensitivity (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, toledo2023kitd816vmast pages 1-2)

**Tryptase Genotyping:**
- TPSAB1 copy number variation testing for hereditary alpha-tryptasemia
- Indicated when interpreting elevated baseline serum tryptase, especially for WHO/ICC minor criterion assessment
- Method: Droplet digital PCR (beyens2023mastocytosisandrelated pages 1-5, li2023reviewandupdates pages 2-4)

**Gene Panels:**
- Myeloid mutation panels including KIT, ASXL1, RUNX1, SRSF2, NRAS, TET2, DNMT3A, CBL, EZH2, JAK2
- Important for risk stratification in advanced SM (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

### Clinical Criteria

**WHO 2022 / ICC 2022 Diagnostic Criteria for SM:**

**Major Criterion:**
- Multifocal dense aggregates of mast cells (≥15 mast cells) in bone marrow and/or extracutaneous organs

**Minor Criteria (need 1 major + 1 minor, OR 3 minor criteria):**
1. ≥25% atypical/spindle-shaped mast cells in marrow or tissue
2. Activating KIT mutation (D816V or other) in marrow, blood, or tissue
3. Aberrant CD25 and/or CD2 and/or CD30 expression on mast cells
4. Persistent baseline serum tryptase >20 ng/mL (adjusted for HαT, not counted in SM-AMN)
(li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, lee2023recentadvancesin pages 3-5)

**Differential Diagnosis:**
- Mast cell activation syndrome (MCAS): Symptoms of mast cell activation without SM criteria
- Monoclonal mast cell activation syndrome (MMAS): Clonal mast cells (KIT+) but only 2 SM minor criteria
- Cutaneous mastocytosis: Skin-limited, no systemic involvement
- Secondary mast cell hyperplasia: Reactive, non-clonal
- Hypereosinophilic syndromes
- Other myeloid neoplasms (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, li2023reviewandupdates pages 2-4)

### Screening

**Indications for Bone Marrow Evaluation:**
- Adult-onset cutaneous lesions (typical urticaria pigmentosa/maculopapular lesions)
- Recurrent, unexplained, or severe anaphylaxis (especially without mucocutaneous symptoms)
- Hymenoptera venom allergy with severe anaphylaxis
- Persistent elevated baseline serum tryptase >20 ng/mL (adjusted for HαT)
- Unexplained osteoporosis or fragility fractures, especially lumbar spine
- REMA score or NICAS score suggesting high SM risk
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, beyens2023mastocytosisandrelated pages 5-8)

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Non-Advanced SM (ISM, BMM):**
- Life expectancy: Near normal, often compatible with normal lifespan
- Mortality primarily from anaphylaxis risk rather than disease progression (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Smoldering SM (SSM):**
- Intermediate prognosis
- Higher risk of progression to advanced SM compared to ISM (li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Advanced SM (ASM, SM-AHN, MCL):**
- Median overall survival (historical):
  - ASM/SM-AHN: Approximately 1.9-9.0 years (variable by subtype and treatment)
  - SM-AML: Median 3.3 years
  - MCL: Median 0.9 years (worst prognosis)
- Disease-specific mortality high in advanced SM
- Recent tyrosine kinase inhibitor therapies (avapritinib) have shown improved survival compared to best available therapy (HR 0.48 [0.29, 0.79], p=0.004) (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

### Prognostic Factors

**Adverse Prognostic Markers:**
- Advanced SM subtype (ASM, SM-AHN, MCL)
- Absence of KIT D816V (10/61, 16% of cohort, HR 2.9 [1.2-6.5], p<0.001)
- Complex karyotype (HR 4.2 [1.8-10.0], p=0.016)
- Co-occurring mutations: ASXL1, RUNX1, SRSF2, NRAS
- Multilineage KIT involvement
- Mast cell leukemia diagnosis
- Eosinophilia ≥1.5×10^9/L
- Lack of treatment response
- <3 cycles of cladribine treatment (if applicable)
(lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

**Favorable Prognostic Markers:**
- ISM or BMM subtype
- Presence of KIT D816V
- Absence of high-risk co-mutations
- Response to cytoreductive therapy (ASM/SM-AHN/MCL)
- Treatment response before allogeneic transplant (if applicable)
(lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

**Prognostic Scoring Systems:**
- MARS (Mutation-Adjusted Risk Score)
- IPSM (International Prognostic Scoring System for Mastocytosis)
- MAPS (Mutation-Augmented Prognostic Score)
- GPSM (Global Prognostic Score for Mastocytosis)
These incorporate genetic mutations, clinical parameters, and disease burden markers (lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

### Quality of Life

Quality of life is significantly impaired in SM due to chronic symptoms, anaphylaxis risk, bone disease, and in advanced disease, organ dysfunction and treatment toxicity. Tyrosine kinase inhibitors (avapritinib) have demonstrated improvements in quality of life measures through reduction of mast cell burden and symptom control (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2).

---

## 12. Treatment

### Pharmacotherapy

**Symptomatic/Mediator-Targeted Therapy (All SM Subtypes):**

*Antihistamines:*
- H1-antihistamines (e.g., cetirizine, loratadine, fexofenadine): For pruritus, urticaria, flushing
- H2-antihistamines (e.g., ranitidine, famotidine): For GI symptoms, acid suppression
- MAXO:0000058 (antihistamine therapy)
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*Mast Cell Stabilizers:*
- Cromolyn sodium: Oral for GI symptoms
- MAXO:0000624 (mast cell stabilizer therapy)
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*Leukotriene Antagonists:*
- Montelukast: For respiratory symptoms
(beyens2023mastocytosisandrelated pages 1-5)

*Epinephrine:*
- Auto-injector: Essential for all SM patients (anaphylaxis prevention)
- MAXO:0000724 (emergency medication)
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*Aspirin (in selected patients):*
- Low-dose for flushing (after tolerance testing)
(beyens2023mastocytosisandrelated pages 1-5)

*Proton Pump Inhibitors:*
- For GI symptoms, peptic ulcer disease
(beyens2023mastocytosisandrelated pages 1-5)

**Bone-Directed Therapy (ISM with Osteoporosis):**

*Bisphosphonates:*
- Alendronate, zoledronic acid: Anti-resorptive
- MAXO:0000127 (bisphosphonate therapy)
(li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5)

*Denosumab:*
- RANKL inhibitor: Anti-resorptive
(li2023reviewandupdates pages 1-2)

*Anabolic Agents:*
- Teriparatide, abaloparatide: Bone formation promotion
(li2023reviewandupdates pages 1-2)

**Cytoreductive Therapy (Advanced SM):**

*Tyrosine Kinase Inhibitors (TKIs):*

- **Midostaurin:** Multi-kinase inhibitor targeting KIT D816V, PKC, FLT3
  - FDA approved for advanced SM (ASM, SM-AHN, MCL)
  - Dosing: 100 mg PO BID
  - Response rate: 40-60% in advanced SM
  - MAXO:0000605 (tyrosine kinase inhibitor therapy)
  (lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

- **Avapritinib:** Selective KIT D816V inhibitor
  - FDA approved for advanced SM
  - Also approved for indolent SM based on PIONEER trial (2023)
  - Dosing: 200 mg PO daily (advanced SM), 25 mg PO daily (ISM)
  - Superior efficacy vs best available therapy in advanced SM: HR for overall survival 0.48 (95% CI 0.29-0.79, p=0.004)
  - Mean tryptase reduction 60.3% greater than BAT (p<0.001)
  - Duration of treatment significantly longer than BAT (HR 0.36, p<0.001)
  - Can reverse both osteoporosis and osteosclerosis
  - MAXO:0000605 (tyrosine kinase inhibitor therapy)
  (li2023reviewandupdates pages 1-2, lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*Purine Analogues:*
- **Cladribine (2-CdA):** Cytotoxic, mast cell debulking
  - Overall response rate: 41% (1st-line), 35% (2nd-line)
  - Median OS: 1.9 years (1st-line), 1.2 years (2nd-line)
  - Effective in some refractory cases
  - MAXO:0001487 (cladribine therapy)
  (beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*Interferon-alpha:*
- Historical role, diminishing use in TKI era
- May have role in resource-limited settings
- MAXO:0000091 (interferon therapy)
(pardanani2023systemicmastocytosisin pages 1-2)

*Imatinib:*
- Only effective for rare imatinib-sensitive KIT mutations (e.g., F522C, K509I in exon 9)
- Ineffective against KIT D816V due to steric hindrance
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

### Advanced Therapeutics

**Allogeneic Hematopoietic Cell Transplantation:**
- Only potentially curative therapy for advanced SM
- Indications: ASM, SM-AML, MCL in selected patients
- Median overall survival by subtype (German DRST/GREM registries, 1999-2021):
  - ASM/SM-AHN: 9.0 years
  - SM-AML: 3.3 years
  - MCL ± AHN: 0.9 years
- Favorable prognostic factors: Treatment response of SM and/or AHN prior to transplant
- Adverse factors: Absence of KIT D816V, complex karyotype
- MAXO:0000747 (allogeneic hematopoietic stem cell transplantation)
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Emerging Therapies (Investigational, Clinical Trials):**
- **Bezuclastinib:** Selective KIT inhibitor
- **Elenestinib:** Novel KIT inhibitor
- Combination strategies: TKI + chemotherapy for SM-AHN
- Mast cell silencing approaches: Siglec-8 agonists (lirentelimab), Siglec-6 agonists, CD200R agonists
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

### Treatment Outcomes

**Avapritinib (PATHFINDER/EXPLORER trials, advanced SM):**
- Overall response rate: ~75%
- Complete remission + partial remission rates: Significant
- Median duration of response: >2 years in responders
- Adverse events: Mostly manageable; cognitive effects, periorbital edema, GI toxicity
(lee2023recentadvancesin pages 1-2, pardanani2023systemicmastocytosisin pages 1-2)

**Midostaurin (advanced SM):**
- Overall response rate: 40-60%
- Side effects: GI toxicity, fatigue, cytopenias
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

### Treatment Strategy

**Treatment Algorithms:**

*ISM/BMM:*
1. Symptomatic therapy (antihistamines, mast cell stabilizers, epinephrine auto-injector)
2. Osteoporosis prevention/treatment
3. Avoidance of mast cell triggers
4. Consider avapritinib for refractory symptoms (based on PIONEER trial, 2023)
(li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*SSM:*
1. Similar to ISM with closer monitoring
2. Consider early cytoreductive therapy if progression
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*ASM:*
1. Tyrosine kinase inhibitor (avapritinib or midostaurin)
2. Supportive care
3. Consider allogeneic transplant in selected patients
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*SM-AHN:*
1. Treat AHN component (chemotherapy for AML, hypomethylating agents for MDS, etc.)
2. Add KIT inhibitor (midostaurin or avapritinib)
3. Consider allogeneic transplant
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

*MCL:*
1. Intensive therapy: TKI (avapritinib preferred)
2. Consider allogeneic transplant early if feasible
3. Clinical trial enrollment
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Personalized Medicine Approaches:**
- KIT mutation testing to guide TKI selection
- Tryptase genotyping (HαT) to interpret biomarkers and adjust thresholds
- Mutation profiling (ASXL1, RUNX1, SRSF2, NRAS) for risk stratification
- Treatment response assessment by tryptase reduction, molecular response (KIT D816V VAF)
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, cilloni2024detectionofkit pages 1-2, li2023reviewandupdates pages 2-4)

---

## 13. Prevention

### Prevention Levels

**Primary Prevention:**
Not applicable given clonal/somatic mutation etiology; no interventions prevent initial SM development.

**Secondary Prevention (Early Detection):**
- Screening high-risk individuals: Those with recurrent anaphylaxis, unexplained osteoporosis, persistent elevated tryptase
- Bone marrow biopsy when suspicion high (clinical criteria, biomarkers)
- Early diagnosis enables anaphylaxis preparedness and symptom management
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, beyens2023mastocytosisandrelated pages 5-8)

**Tertiary Prevention (Preventing Complications):**
- **Anaphylaxis prevention:** Epinephrine auto-injector, avoidance of triggers (NSAIDs, opiates, contrast agents, alcohol, temperature extremes, physical/emotional stress), venom immunotherapy (if hymenoptera allergy), premedication before procedures
- **Osteoporosis prevention:** Bone-directed therapy (bisphosphonates, denosumab), vitamin D/calcium supplementation, weight-bearing exercise
- **Disease progression monitoring:** Regular tryptase monitoring, bone marrow reassessment if clinical change, mutation monitoring
- **Infection prevention:** During cytoreductive therapy (prophylactic antibiotics/antivirals if indicated)
(li2023reviewandupdates pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

### Screening and Early Detection

**Screening Programs:**
- No population-based screening
- Targeted screening of symptomatic individuals and first-degree relatives (if familial mastocytosis)
(beyens2023mastocytosisandrelated pages 1-5)

**Genetic Screening:**
- Not routinely recommended given sporadic nature
- Consider in rare familial cases (germline KIT mutation testing)
- Tryptase genotyping (HαT) increasingly used to interpret tryptase elevations
(beyens2023mastocytosisandrelated pages 1-5, li2023reviewandupdates pages 2-4)

**Risk Stratification:**
- REMA score and NICAS score for anaphylaxis patients
- Prognostic scoring (MARS, IPSM, MAPS, GPSM) for advanced SM
(lee2023recentadvancesin pages 1-2, beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2, beyens2023mastocytosisandrelated pages 5-8)

### Counseling

**Genetic Counseling:**
- Indicated for familial mastocytosis cases
- Discussion of recurrence risk (very low for typical sporadic SM)
- Family planning guidance if germline KIT mutation identified
(beyens2023mastocytosisandrelated pages 1-5)

### Public Health

Public health interventions not applicable given rarity and non-communicable nature.

### Prophylaxis

**Medications:**
- Chronic antihistamines (H1 and H2 blockers)
- Mast cell stabilizers (cromolyn)
- Epinephrine auto-injector (all patients)
(beyens2023mastocytosisandrelated pages 1-5, pardanani2023systemicmastocytosisin pages 1-2)

**Procedures:**
- Venom immunotherapy (VIT) for hymenoptera venom allergy: Reduces anaphylaxis risk but may need lifelong continuation in SM
(beyens2023mastocytosisandrelated pages 1-5, beyens2023mastocytosisandrelated pages 5-8)

---

## 14. Other Species / Natural Disease

### Taxonomy and Natural Disease

**Species Affected:**
- Canine (Canis lupus familiaris, NCBI:txid9615): Canine mast cell tumors (MCTs) are common, often involving KIT mutations
- Feline (Felis catus, NCBI:txid9685): Feline mastocytosis described
- Murine (Mus musculus, NCBI:txid10090): Not naturally occurring but extensively modeled
(Brief mention in general literature; detailed veterinary data not extensively covered in retrieved sources)

**Gene Orthology:**
- KIT gene is highly conserved across mammals
- Human KIT (HGNC:6342) has orthologs in mouse (MGI:96677), dog, cat, other species

**Natural Disease in Animals:**
- Canine MCTs are common neoplasms; some harbor KIT mutations (exon 11 more common than D816V in dogs)
- Veterinary relevance: MCTs are important clinical problems in dogs; some response to toceranib (KIT inhibitor)
(Not primary focus of retrieved human-focused sources)

### Comparative Biology

Comparative pathology suggests conserved KIT signaling mechanisms across species; mast cell biology and KIT function are evolutionarily conserved.

---

## 15. Model Organisms

### Model Types

**Mammalian Models:**

*Mouse Models (Mus musculus, NCBI:txid10090):*
- Transgenic/knock-in models: Expression of KIT D816V or other activating KIT mutations in hematopoietic cells
- Transplantation models: KIT-mutant bone marrow transplant into recipient mice
- Phenotype recapitulation: Variable; some models show mast cell expansion, organomegaly, but may not fully recapitulate human SM features
- Limitations: Murine mast cell biology differs from human; incomplete phenotype reproduction
(toledo2023kitd816vmast pages 1-2)

**Induced Pluripotent Stem Cell (iPSC) Models:**
- Patient-derived iPSC lines carrying KIT D816V mutation
- Differentiation to mast cells in vitro
- Phenotype recapitulation: KIT D816V iPSC-derived mast cells show:
  - Increased mast cell numbers
  - Abnormal maturation kinetics
  - Activated phenotype
  - CD25 and CD30 expression
  - Transcriptional signature with upregulated innate/inflammatory response genes matching primary SM mast cells
- Applications: Disease modeling, drug screening, mechanistic studies
- Advantages: Unlimited cell source, patient-specific genetic background, close-to-human model
(toledo2023kitd816vmast pages 1-2)

**Potential Invertebrate/Other Models:**
- Zebrafish (Danio rerio, NCBI:txid7955): Emerging model for inflammation and mast cell research, though not specifically for SM modeling
- Utility: Rapid development, genetic tractability, in vivo imaging
(General zebrafish inflammation studies mentioned; not SM-specific in retrieved sources)

### Genetic Models

**Available Types:**
- Knock-in: KIT D816V introduced into mouse hematopoietic cells
- Transgenic: Conditional expression of mutant KIT
- Xenograft: Human SM cells or iPSC-derived mast cells transplanted into immunodeficient mice
(toledo2023kitd816vmast pages 1-2)

### Model Limitations

- Mouse models do not fully recapitulate all aspects of human SM (bone disease, mediator-related symptoms, clinical heterogeneity)
- iPSC models are in vitro, lack tissue microenvironment and systemic interactions
- Zebrafish lack true mast cells homologous to mammalian mast cells

### Applications

- **Mechanistic studies:** KIT signaling pathways, co-mutation effects, multilineage involvement
- **Drug screening:** Testing TKIs and novel therapeutics
- **Biomarker discovery:** Transcriptomics, proteomics in controlled models
(toledo2023kitd816vmast pages 1-2)

### Resources

- Mouse Genome Informatics (MGI): Mouse model data
- International Mouse Strain Resource (IMSR): Repository of mouse models
- iPSC repositories: Patient-derived lines available through research collaborations

---

## Summary

Systemic mastocytosis is a rare clonal hematopoietic neoplasm characterized by abnormal accumulation of neoplastic mast cells in bone marrow and extracutaneous organs. The disease is predominantly driven by the KIT D816V mutation (>90% of cases), which causes constitutive KIT receptor activation, leading to mast cell proliferation, survival, and activation. SM is classified into non-advanced subtypes (BMM, ISM, SSM) and advanced subtypes (ASM, SM-AHN, MCL) based on disease burden and organ dysfunction (WHO/ICC 2022 criteria). Clinical manifestations range from mediator-related symptoms (anaphylaxis, flushing, GI symptoms) to organ infiltration and dysfunction in advanced disease. Diagnosis requires integration of bone marrow morphology (major criterion: dense mast cell aggregates), immunophenotyping (CD25, CD2, CD30 expression), molecular testing (KIT mutations), and clinical findings. Serum tryptase serves as a key biomarker. Prognosis varies from near-normal life expectancy in ISM to poor survival in advanced SM. Treatment includes symptomatic management for all patients and cytoreductive therapy with tyrosine kinase inhibitors (midostaurin, avapritinib—FDA approved 2017 and 2021 respectively) for advanced disease. Avapritinib has demonstrated superior efficacy compared to best available therapy and is now approved for both advanced and indolent SM. Allogeneic stem cell transplantation remains the only potentially curative option. Research models include KIT-mutant mouse models and patient-derived iPSC-differentiated mast cells. Recent advances (2022-2024) include refined WHO/ICC diagnostic criteria incorporating CD30, improved KIT mutation detection methods, tryptase genotyping for HαT, and expanding indications for selective KIT inhibitors.

References

1. (li2023reviewandupdates pages 1-2): Julie Y. Li, Christopher B. Ryder, Hailing Zhang, Samuel G. Cockey, Elizabeth Hyjek, Lynn C. Moscinski, Elizabeth Sagatys, and Jinming Song. Review and updates on systemic mastocytosis and related entities. Cancers, 15:5626, Nov 2023. URL: https://doi.org/10.3390/cancers15235626, doi:10.3390/cancers15235626. This article has 39 citations.

2. (lee2023recentadvancesin pages 1-2): Hyun Jung Lee. Recent advances in diagnosis and therapy in systemic mastocytosis. Blood Research, 58:S96-S108, Apr 2023. URL: https://doi.org/10.5045/br.2023.2023024, doi:10.5045/br.2023.2023024. This article has 20 citations.

3. (pardanani2023systemicmastocytosisin pages 1-2): Animesh Pardanani. Systemic mastocytosis in adults: 2023 update on diagnosis, risk stratification and management. American Journal of Hematology, 98:1097-1116, May 2023. URL: https://doi.org/10.1002/ajh.26962, doi:10.1002/ajh.26962. This article has 137 citations and is from a domain leading peer-reviewed journal.

4. (cilloni2024detectionofkit pages 1-2): Daniela Cilloni, Beatrice Maffeo, Arianna Savi, Alice Costanza Danzero, Valentina Bonuomo, and Carmen Fava. Detection of kit mutations in systemic mastocytosis: how, when, and why. International Journal of Molecular Sciences, 25:10885, Oct 2024. URL: https://doi.org/10.3390/ijms252010885, doi:10.3390/ijms252010885. This article has 18 citations.

5. (toledo2023kitd816vmast pages 1-2): Marcelo A. S. de Toledo, Xuhuang Fu, Tiago Maié, Eva M. Buhl, Katrin Götz, Susanne Schmitz, Anne Kaiser, Peter Boor, Till Braunschweig, Nicolas Chatain, Ivan G. Costa, Tim H. Brümmendorf, Steffen Koschmieder, and Martin Zenke. Kit d816v mast cells derived from induced pluripotent stem cells recapitulate systemic mastocytosis transcriptional profile. International Journal of Molecular Sciences, 24:5275, Mar 2023. URL: https://doi.org/10.3390/ijms24065275, doi:10.3390/ijms24065275. This article has 10 citations.

6. (li2023reviewandupdates pages 2-4): Julie Y. Li, Christopher B. Ryder, Hailing Zhang, Samuel G. Cockey, Elizabeth Hyjek, Lynn C. Moscinski, Elizabeth Sagatys, and Jinming Song. Review and updates on systemic mastocytosis and related entities. Cancers, 15:5626, Nov 2023. URL: https://doi.org/10.3390/cancers15235626, doi:10.3390/cancers15235626. This article has 39 citations.

7. (beyens2023mastocytosisandrelated pages 1-5): Michiel Beyens, Jessy Elst, Marie-Line van der Poorten, Athina Van Gasse, Alessandro Toscano, Anke Verlinden, Katrien Vermeulen, Marie-Berthe Maes, J. N. G. Hanneke Oude Elberink, Didier Ebo, and Vito Sabato. Mastocytosis and related entities: a practical roadmap. Acta Clinica Belgica, 78:325-335, Oct 2023. URL: https://doi.org/10.1080/17843286.2022.2137631, doi:10.1080/17843286.2022.2137631. This article has 11 citations and is from a peer-reviewed journal.

8. (lee2023recentadvancesin pages 3-5): Hyun Jung Lee. Recent advances in diagnosis and therapy in systemic mastocytosis. Blood Research, 58:S96-S108, Apr 2023. URL: https://doi.org/10.5045/br.2023.2023024, doi:10.5045/br.2023.2023024. This article has 20 citations.

9. (beyens2023mastocytosisandrelated pages 5-8): Michiel Beyens, Jessy Elst, Marie-Line van der Poorten, Athina Van Gasse, Alessandro Toscano, Anke Verlinden, Katrien Vermeulen, Marie-Berthe Maes, J. N. G. Hanneke Oude Elberink, Didier Ebo, and Vito Sabato. Mastocytosis and related entities: a practical roadmap. Acta Clinica Belgica, 78:325-335, Oct 2023. URL: https://doi.org/10.1080/17843286.2022.2137631, doi:10.1080/17843286.2022.2137631. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Systemic_Mastocytosis-deep-research-falcon_artifacts/artifact-00.md)