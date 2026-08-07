---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-02T01:16:46.122401'
end_time: '2026-08-02T01:26:57.912809'
duration_seconds: 611.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hennekam lymphangiectasia-lymphedema syndrome 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 2** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 2** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Hennekam lymphangiectasia–lymphedema syndrome 2

## Executive summary and evidence scope

Hennekam lymphangiectasia–lymphedema syndrome 2 (HKLLS2) is an ultrarare, autosomal-recessive developmental lymphatic disorder caused by biallelic **FAT4** variants. Its defining manifestations are primary lymphedema/lymphangiectasia, characteristic craniofacial morphology, and variable developmental or intellectual involvement. The strongest subtype-specific evidence consists of a small number of molecularly confirmed patients and mechanistic studies in mutant mice; consequently, prevalence, penetrance, survival, and most phenotype frequencies remain unknown. By 2018, only 40 individuals with Hennekam syndrome of all molecular subtypes had been reported, 23 molecularly confirmed; this is not a FAT4-only denominator. (ivanovski2018vanmaldergemsyndrome pages 7-8, ivanovski2018vanmaldergemsyndrome pages 1-2)

| Domain | Evidence-backed finding | Knowledge-base annotation/caveat |
|---|---|---|
| Disease entity | **Hennekam lymphangiectasia-lymphedema syndrome 2** is a Mendelian syndromic primary lymphatic disorder; Open Targets maps it to **MONDO:0014454** and links the disease specifically to **FAT4** (OpenTargets Search: Hennekam lymphangiectasia-lymphedema syndrome 2-FAT4) | Disease-level resource plus primary literature; subtype-specific entry should be kept separate from CCBE1-related Hennekam syndrome 1 and ADAMTS3-related syndrome 3 (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 7-8) |
| Causal gene | Causal gene is **FAT4** (**FAT atypical cadherin 4**), a large atypical cadherin involved in planar cell polarity and development (medina2023structureofthe pages 1-2, OpenTargets Search: Hennekam lymphangiectasia-lymphedema syndrome 2-FAT4) | Use HGNC gene symbol **FAT4**; disease mechanism is consistent with impaired FAT4 function rather than a gain-of-function state (inference from recessive human disease and knockout/model data) (pujol2017dachsous1–fat4signalingcontrols pages 1-2, pujol2017dachsous1–fat4signalingcontrols pages 2-4) |
| Inheritance / variant class | Reported subtype 2 cases show **autosomal recessive**, **biallelic germline** FAT4 variants; example HS patient had homozygous **c.5297A>G (p.Asp1766Gly)**; prior reports include other homozygous/compound heterozygous damaging variants in FAT4-associated allelic disorders (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 1-2) | Variant interpretation should follow ACMG/AMP; currently available evidence supports damaging/likely loss-of-function biology, but subtype-specific variant spectrum remains sparse because the condition is ultrarare (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8) |
| Defining phenotype | Core phenotype is **lymphatic dysplasia** with **lymphedema** and **lymphangiectasia**, often with facial anomalies and variable developmental/intellectual effects; original syndrome description and later series emphasize edema of face/limbs/genitalia and intestinal lymphangiectasia (ivanovski2018vanmaldergemsyndrome pages 1-2) | Useful HPO terms: **Lymphedema (HP:0001004)**, **Intestinal lymphangiectasia**, **Generalized edema**, **Hypertelorism (HP:0000316)**, **Epicanthus (HP:0000286)**, **Developmental delay (HP:0001263)** / **Intellectual disability (HP:0001249)**; subtype 2 evidence is still based on very few FAT4-confirmed patients (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8) |
| FAT4 subtype clinical details | In the FAT4-confirmed HS case, features included respiratory distress at birth, generalized edema starting at **8 months**, recurrent respiratory/intestional infections, abdominal distension, umbilical hernia, periorbital edema, conical teeth, gingival hypertrophy, and normal-to-mildly affected cognition after speech delay (ivanovski2018vanmaldergemsyndrome pages 6-7) | This is strong patient-level evidence but mainly from isolated cases; do not overstate frequency estimates for FAT4 subtype 2 specifically (ivanovski2018vanmaldergemsyndrome pages 6-7) |
| Age of onset / natural history | Comparative review indicates **CCBE1-related HS often has lymphedema at birth**, whereas **FAT4-related HS can present later in childhood** (ivanovski2018vanmaldergemsyndrome pages 7-8) | This is one of the clearest subtype-distinguishing features currently available; still based on limited published cohorts (ivanovski2018vanmaldergemsyndrome pages 7-8) |
| Laboratory / GI manifestations | FAT4-HS can include **hypoalbuminemia**, **hypoproteinemia**, **hypogammaglobulinemia**, elevated IgE/eosinophilia, abdominal distension, and endoscopic evidence suggestive of intestinal lymphatic disease/protein loss (ivanovski2018vanmaldergemsyndrome pages 6-7) | Knowledge-base should distinguish direct findings (serum albumin/protein abnormalities) from histology, which may be nondiagnostic in some biopsies despite clinical suspicion (ivanovski2018vanmaldergemsyndrome pages 6-7) |
| Mechanism | FAT4 and **DCHS1** form a **heterophilic cadherin** receptor-ligand pair that regulates **planar cell polarity (PCP)**; in lymphatics this signaling controls **valve endothelial cell polarization** and **lymphatic valve morphogenesis** (pujol2017dachsous1–fat4signalingcontrols pages 1-2, pujol2017dachsous1–fat4signalingcontrols pages 2-4) | Useful GO/CL terms: **planar cell polarity**, **cell-cell adhesion**, **lymph vessel development**, **valve morphogenesis**; cell type: **lymphatic endothelial cell** / **valve endothelial cell**. Disease mechanism is supported directly by model systems and plausibly explains human lymphedema (pujol2017dachsous1–fat4signalingcontrols pages 1-2, pujol2017dachsous1–fat4signalingcontrols pages 4-8) |
| Mechanistic chain | Mouse data show overall lymphatic vessel architecture can be present, but valve formation is defective: mutant valve endothelial cells are disoriented and fail to form proper leaflets; ~**60% of valves were abnormal** in Fat4/Dchs1 mutants, with reduced proper orientation versus controls (pujol2017dachsous1–fat4signalingcontrols pages 1-2) | Upstream: FAT4-DCHS1 adhesion/polarity signaling. Downstream: impaired endothelial polarization, migration, and valve leaflet formation, leading to dysfunctional lymph drainage and lymphedema (pujol2017dachsous1–fat4signalingcontrols pages 1-2, pujol2017dachsous1–fat4signalingcontrols pages 4-8) |
| 2023-2024 research update | A 2023 structural study solved human **FAT4–DCHS1** binding-domain structures and showed the interface spans **EC1-4** of each protein with high-affinity binding; this refines the molecular basis of subtype 2 pathogenesis (medina2023structureofthe pages 1-2, medina2023structureofthe pages 9-10) | Recent mechanistic advance is structural rather than clinical; no 2023-2024 large natural-history cohort specific to FAT4-HS was identified in the retrieved evidence (medina2023structureofthe pages 1-2) |
| Diagnostics | Diagnostic approach is **clinical recognition of syndromic primary lymphedema** plus confirmation of lymphatic dysfunction (e.g., **lymphoscintigraphy**) and **molecular confirmation** of biallelic FAT4 variants using **lymphedema gene panel**, **WES**, or **WGS** (vignes2021primarylymphedemafrench pages 1-2, ivanovski2018vanmaldergemsyndrome pages 6-7) | Lymphoscintigraphy is useful to confirm lymphedema generally; targeted single-gene testing may miss atypical cases, so panel/exome/genome approaches are reasonable when phenotype is syndromic (vignes2021primarylymphedemafrench pages 1-2, ivanovski2018vanmaldergemsyndrome pages 6-7) |
| Differential diagnosis | Must be distinguished from other syndromic primary lymphedemas and from **Van Maldergem syndrome**; VMS shares facial gestalt/intellectual issues but has neonatal hypotonia, feeding/breathing problems, hearing loss, tracheal anomalies, and osteopenia rather than prominent lymphatic anomalies (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 7-8) | Also clinically exclude non-lymphatic causes of swelling such as **lipedema** and secondary lymphedema causes; these recommendations are extrapolated from primary lymphedema guidelines (vignes2021primarylymphedemafrench pages 1-2) |
| Management | No curative therapy is established; supportive care includes **complete decongestive therapy**, **compression bandaging/garments**, **manual lymph drainage**, **exercise**, skin care/hygiene, limb elevation, and education; intestinal lymphangiectasia/protein-losing enteropathy may benefit from **high-protein, low-fat / medium-chain triglyceride nutrition** and albumin support (lee2018hennekamsyndromea pages 3-5, musumeci2006cutaneousmanifestationsand pages 3-4, vignes2021primarylymphedemafrench pages 1-2) | NCIT-style intervention concepts: compression therapy, physical therapy, nutritional support. Most treatment evidence is syndrome-general or case-based rather than FAT4-subtype trials (musumeci2006cutaneousmanifestationsand pages 3-4, lee2018hennekamsyndromea pages 3-5) |
| Outcomes / QoL | Primary lymphedema can have major **functional and psychological** effects on quality of life, and cellulitis is a key complication; case evidence suggests edema reduction is achievable with conservative therapy (vignes2021primarylymphedemafrench pages 1-2, lee2018hennekamsyndromea pages 3-5) | No robust FAT4-specific survival or QoL cohort was identified; prognosis is therefore inferred from syndrome severity, organ involvement, and control of edema/protein loss (vignes2021primarylymphedemafrench pages 1-2) |
| Disease-modifying therapy / trials | **No approved disease-modifying therapy** or subtype-specific targeted therapy was identified; no relevant interventional trial specific to Hennekam syndrome was retrieved (lee2018hennekamsyndromea pages 3-5, vignes2021primarylymphedemafrench pages 1-2) | Important negative finding for knowledge base: management is supportive; research remains preclinical/mechanistic rather than therapeutic (pujol2017dachsous1–fat4signalingcontrols pages 2-4, medina2023structureofthe pages 1-2) |
| Evidence limitations | Condition is **ultrarare**; by 2018 only **40 HS patients** overall had been reported, with molecular heterogeneity across **CCBE1, FAT4, and ADAMTS3**, and only sparse FAT4-confirmed subtype 2 cases (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 7-8) | Frequency estimates, penetrance, genotype-phenotype correlation, prevalence, and many prognosis fields should be marked **not well established / insufficient subtype-specific data** (ivanovski2018vanmaldergemsyndrome pages 7-8) |


*Table: This compact table summarizes the most actionable disease-characteristic facts for FAT4-related Hennekam lymphangiectasia-lymphedema syndrome 2. It is designed for rapid population of a knowledge-base entry while clearly marking where evidence is subtype-specific versus extrapolated.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Hennekam lymphangiectasia–lymphedema syndrome 2.
* **Category:** Mendelian, syndromic primary lymphatic dysplasia.
* **MONDO:** **MONDO:0014454**.
* **Causal target:** **FAT4**, Ensembl **ENSG00000196159**, approved name *FAT atypical cadherin 4*. Open Targets reports five disease–target evidence records and an association score of 0.7685. (OpenTargets Search: Hennekam lymphangiectasia-lymphedema syndrome 2-FAT4)
* **OMIM:** commonly catalogued as **Hennekam lymphangiectasia–lymphedema syndrome 2, 616006**; **FAT4, 612411**. These identifiers should be checked against the live OMIM release before automated ingestion because OMIM itself was not directly retrieved in this search.
* **Orphanet:** Hennekam syndrome is represented at the broader syndrome level; a subtype-specific Orpha code was not verified from the retrieved evidence.
* **ICD-10/ICD-11 and MeSH:** no uniquely verified HKLLS2 code/heading was identified. Coding generally uses broader congenital/primary lymphedema, lymphangiectasia, or rare developmental-syndrome categories; these should not be treated as exact disease identifiers.

Synonyms include **FAT4-related Hennekam syndrome**, **Hennekam syndrome type 2**, **Hennekam lymphangiectasia–lymphedema syndrome, FAT4-related**, and, historically, *lymphedema–lymphangiectasia–intellectual disability syndrome*. The older term “mental retardation” occurs in historical publications but is no longer preferred.

The evidence combines aggregated disease resources (MONDO/Open Targets and reviews), small published case series, individual molecularly characterized patients, and experimental mouse/cell studies—not EHR-derived population data. The key clinical paper explicitly states: “Biallelic variants in FAT4 are associated with the two disorders, Van Maldergem syndrome … and Hennekam syndrome.” (ivanovski2018vanmaldergemsyndrome pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

HKLLS2 is caused by **biallelic germline FAT4 variants**, consistent with autosomal-recessive inheritance. The available human and knockout evidence supports reduced or disrupted FAT4 function; however, individual missense alleles require variant-level functional and ACMG/AMP assessment rather than automatic loss-of-function assignment. One reported patient was homozygous for **NM_001291303.1:c.5297A>G, p.Asp1766Gly**. The residue was conserved, the allele was absent from ExAC and 1000 Genomes, and predictions were damaging (SIFT 0.015; PolyPhen-2 0.991 HumDiv and 0.932 HumVar). (ivanovski2018vanmaldergemsyndrome pages 6-7)

### Risk factors

* **Genetic:** having two pathogenic/likely pathogenic FAT4 alleles is the principal established risk. Consanguinity increases the probability that both parents carry the same rare allele; the p.Asp1766Gly patient was born to first-cousin parents. (ivanovski2018vanmaldergemsyndrome pages 6-7)
* **Family history:** siblings of an affected person have a 25% recurrence risk when both parents are heterozygous carriers; unaffected siblings have a 2/3 carrier probability after excluding disease.
* **Environmental, infectious, lifestyle, occupational, age, and sex risks:** none are established as causes or susceptibility factors. Infections and diet may modify complications or edema burden but do not cause the Mendelian disorder.
* **Protective variants, modifier genes, or protective environmental exposures:** none validated.
* **Gene–environment interaction:** no HKLLS2-specific interaction has been demonstrated. Mechanical flow is biologically relevant to lymphatic-valve endothelial polarization, but evidence that exercise, diet, toxins, or infection alters penetrance of FAT4 disease is absent.

## 3. Phenotypes

Phenotype frequencies below must be interpreted cautiously: most are syndrome-wide observations, whereas the most detailed FAT4-specific evidence is essentially patient-level.

### Core manifestations and suggested HPO annotations

* **Primary lymphedema**—clinical sign/physical manifestation; **HP:0001004**. It may affect face/periorbital tissues, limbs, genitalia, or be generalized. FAT4-related edema can begin after birth or later in childhood, in contrast to the frequently congenital edema of CCBE1-related disease. Severity and distribution are variable and generally chronic. (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 7-8)
* **Lymphangiectasia**, especially intestinal—clinical/pathologic sign; suggested HPO: *intestinal lymphangiectasia*. It may cause protein-losing enteropathy, abdominal distension, malabsorption, diarrhea, ascites, hypoalbuminemia, and hypogammaglobulinemia. (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 1-2)
* **Generalized/pitting edema**—physical sign; suggested HPO: generalized edema/pitting edema. In one FAT4 patient it began at 8 months and included periorbital edema and abdominal distension. (ivanovski2018vanmaldergemsyndrome pages 6-7)
* **Characteristic face**—hypertelorism (**HP:0000316**), epicanthus (**HP:0000286**), flat/wide nasal bridge, midface hypoplasia, synophrys, small/low-set ears, small mouth, and full lower lip. Conical/irregular teeth and gingival hypertrophy can occur. (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8)
* **Developmental or intellectual effects**—suggested **HP:0001263** and **HP:0001249**. Syndrome-level descriptions emphasize mild intellectual disability, but expressivity is broad: the detailed p.Asp1766Gly patient had delayed complex language yet IQ 100–105, normal motor milestones, and normal brain MRI. (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8)
* **Growth abnormalities:** short stature and low weight were documented in the FAT4 patient (<3rd percentile at age seven); suggested HPO: short stature (**HP:0004322**) and underweight. (ivanovski2018vanmaldergemsyndrome pages 6-7)
* **Other reported findings:** umbilical hernia, abdominal distension, recurrent respiratory/intestinal infections, fetal fingertip pads, and blurred/elevated optic discs. These are not established as frequent subtype-defining features. (ivanovski2018vanmaldergemsyndrome pages 6-7)

### Laboratory abnormalities

In the p.Asp1766Gly patient, albumin was **2.2 g/dL**, total protein **3.8 g/dL**, IgM **<0.25 g/L**, IgG **<1.98 g/L**, IgE **410.7 IU/L**, and eosinophils **13.8%**. Endoscopy showed duodenal white spots and edematous/lacunar colonic mucosa, but biopsies did not demonstrate dilated lymphatics; thus, a negative focal biopsy does not exclude clinically important intestinal lymphatic disease. (ivanovski2018vanmaldergemsyndrome pages 6-7)

### Quality of life

No FAT4-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was found. Expert primary-lymphedema guidance states that functional and psychological repercussions can be major, while chronic swelling, garment burden, mobility restriction, appearance, recurrent cellulitis, dietary restriction, and developmental needs plausibly drive impairment. This is guideline-level extrapolation, not a measured HKLLS2 statistic. (vignes2021primarylymphedemafrench pages 1-2)

## 4. Genetic and molecular information

**FAT4** encodes a giant, calcium-dependent, atypical cadherin. The protein has **34 extracellular cadherin domains**, compared with 27 in DCHS1, and forms a heterophilic trans-cellular receptor–ligand pair with DCHS1. (medina2023structureofthe pages 1-2)

Pathogenic classes reported across FAT4-associated recessive disease include damaging missense and truncating/splice-disrupting alleles, generally in homozygous or compound-heterozygous state. Variants are constitutional/germline, not somatic. Exact gnomAD allele frequencies and ClinVar classifications must be retrieved allele by allele; the p.Asp1766Gly report predates current gnomAD and only establishes absence from ExAC/1000 Genomes. (ivanovski2018vanmaldergemsyndrome pages 6-7)

No validated HKLLS2 modifier gene, epigenetic signature, recurrent chromosomal abnormality, anticipation mechanism, or germline-mosaicism series was identified. **DCHS1** is a binding partner and an allelic-pathway gene, not an established modifier. Biallelic FAT4 variants can also produce **Van Maldergem syndrome 2**, demonstrating allelic phenotypic heterogeneity; no reliable genotype–phenotype correlation had been defined. (ivanovski2018vanmaldergemsyndrome pages 7-8, ivanovski2018vanmaldergemsyndrome pages 1-2)

## 5. Environmental, lifestyle, and infectious information

There is no evidence that toxins, radiation, pollution, smoking, alcohol, occupation, diet, or a pathogen initiates HKLLS2. Recurrent infection is a downstream complication of lymphatic dysfunction, skin-barrier disruption, protein loss, and hypogammaglobulinemia. Diet is therapeutic when intestinal lymphangiectasia is present; it is not primary prevention. Avoiding skin trauma and treating entry lesions may reduce cellulitis risk but cannot prevent the genetic disorder. (musumeci2006cutaneousmanifestationsand pages 3-4, vignes2021primarylymphedemafrench pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic damaging FAT4 variants reduce normal FAT4-mediated intercellular signaling.
2. **Molecular defect:** FAT4 cannot correctly engage DCHS1 across adjacent cells or transmit normal planar-cell-polarity information.
3. **Cellular defect:** lymphatic valve endothelial cells fail to polarize and reorient perpendicular to the vessel axis; collective migration, actin organization, and junctional rearrangement are impaired.
4. **Developmental defect:** valve initiation can occur and the broad lymphatic network can remain present, but valve leaflets fail to mature normally.
5. **Physiologic result:** incompetent lymph transport produces interstitial fluid retention and lymphedema; intestinal lymphatic dysfunction produces lymph/protein loss, hypoalbuminemia, immune-protein loss, edema, and malabsorption. (pujol2017dachsous1–fat4signalingcontrols pages 2-4, pujol2017dachsous1–fat4signalingcontrols pages 1-2)

In Fat4- and Dchs1-deficient mice, approximately **60% of lymphatic valves were abnormal** at P0. Only **23%** of FAT4-deficient and **43%** of DCHS1-deficient valve endothelial cells achieved the specified proper orientation, versus **83%** in controls. Overall lymphatic architecture and initial Prox1-high clusters were comparatively preserved, localizing the major defect to valve morphogenesis. Reduced FnEIIIA and integrin-α9 staining suggests impaired integrin-supported migration downstream. (pujol2017dachsous1–fat4signalingcontrols pages 1-2)

Although FAT4/DCHS1 can intersect Hippo signaling in other tissues, the lymphatic-valve study did not find significant junctional recruitment of TAZ or Merlin consistent with a simple canonical-Hippo mechanism. The best-supported lymphatic mechanism is therefore **planar cell polarity and endothelial polarization**, with Hippo involvement context-dependent rather than proven as the direct cause of HKLLS2 lymphatic disease. (pujol2017dachsous1–fat4signalingcontrols pages 2-4, pujol2017dachsous1–fat4signalingcontrols pages 14-15)

### Recent mechanistic development

Medina et al., accepted **1 February 2023** and published in *Nature Communications* 14:891, solved human FAT4–DCHS1 co-crystal structures. Their abstract reports that the binding interface extends across **EC1–EC4** and contains an unusually extensive salt-bridge network; extracellular phosphorylation may modulate binding. PDB entries include **8EGW** and **8EGX**. This provides structural—not yet therapeutic—resolution of the disease-relevant receptor–ligand interface. DOI: https://doi.org/10.1038/s41467-023-36435-x. (medina2023structureofthe pages 9-10, medina2023structureofthe pages 1-2)

### Suggested ontology annotations

* **GO biological processes:** planar cell polarity; cell–cell adhesion; endothelial cell migration; actin cytoskeleton organization; lymph vessel development; lymphatic valve morphogenesis; regulation of tissue fluid homeostasis.
* **GO cellular components:** plasma membrane, cell–cell junction, extracellular region/cadherin complex; mitochondrial association has been described for cleaved Fat-family intracellular domains but is not established as the HKLLS2 lymphatic mechanism.
* **Cell Ontology:** lymphatic endothelial cell; valve endothelial cell (use the closest current CL term and retain “Prox1-high lymphatic valve endothelial cell” as a textual qualifier).
* **Biochemical abnormality:** receptor/adhesion-signaling dysfunction rather than enzyme deficiency or ion-channel disease.

No HKLLS2-specific patient transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial transcriptome, CRISPR screen, or integrated multi-omics study was identified. Such fields should be recorded as **not available**, rather than inferred from general lymphedema datasets.

## 7. Anatomical structures affected

Primary sites are dermal/subcutaneous lymphatic vessels and collecting-vessel valves, with clinically visible involvement of extremities, face/periorbital tissues, genitalia, and abdominal wall. The gastrointestinal tract—particularly intestinal lacteals/lymphatics—is a major visceral site. Secondary involvement can include serous cavities through ascites/effusions, skin through chronic edema and fibrosis, and immune function through intestinal protein/immunoglobulin loss. (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 6-7)

Suggested annotations include **UBERON:** lymphatic vessel, lymphatic valve, skin/subcutaneous tissue, small intestine/duodenum, colon, face, upper limb, lower limb, external genitalia, and peritoneal cavity. Lymphedema may be bilateral/generalized or asymmetric/unilateral; one syndrome-level rehabilitation case had unilateral arm disease, but this was not genetically confirmed as FAT4-related. (lee2018hennekamsyndromea pages 3-5)

## 8. Temporal development

HKLLS2 is a congenital developmental disorder, even when swelling is not evident neonatally. FAT4-related lymphedema may emerge in infancy or later childhood; in the best-documented patient it began at **8 months**, while the comparative series states that FAT4 cases can begin later than CCBE1 cases, which are often edematous at birth. (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8)

The expected course is chronic and lifelong, with variable progression and fluctuation according to dependent fluid load, infection, protein loss, compression adherence, and tissue remodeling. Formal stages or subtype-specific progression rates do not exist. Spontaneous cure has not been documented. Early recognition is important before recurrent infection, fibrosis, adipose deposition, severe protein loss, or irreversible functional impairment develops. General primary-lymphedema guidance notes that lymph accumulation drives skin thickening and adipose deposition. (vignes2021primarylymphedemafrench pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Penetrance has not been quantified, expressivity is clearly variable, and no anticipation is expected. Consanguinity is represented in reported families but is not required. No validated founder allele, carrier frequency, ethnic enrichment, geographic concentration, sex ratio, incidence, or prevalence estimate exists for HKLLS2. (ivanovski2018vanmaldergemsyndrome pages 6-7, ivanovski2018vanmaldergemsyndrome pages 7-8)

The statement “40 patients” refers to all clinically reported Hennekam syndrome by 2018, not HKLLS2 prevalence. Of those, 13 had CCBE1 variants, two had ADAMTS3 variants, and many remained molecularly unresolved; therefore, these counts cannot support a population rate or FAT4 penetrance estimate. (ivanovski2018vanmaldergemsyndrome pages 7-8, ivanovski2018vanmaldergemsyndrome pages 1-2)

## 10. Diagnostics

### Recommended workflow

1. **Clinical assessment:** map edema distribution and onset; inspect skin and genitalia; document facial/dental, developmental, growth, GI, respiratory, neurologic, ophthalmic, hearing, skeletal, and family-history findings. Stemmer sign supports lymphedema but is not specific to HKLLS2. (vignes2021primarylymphedemafrench pages 1-2)
2. **Exclude acquired edema:** renal, hepatic, cardiac, venous, medication-related, infectious/filariasis, malnutrition, lipedema, and secondary lymphatic injury.
3. **Laboratory evaluation:** CBC; albumin/total protein; immunoglobulins; electrolytes, renal and hepatic indices; stool α1-antitrypsin clearance when protein-losing enteropathy is suspected; fat-soluble vitamins and micronutrients according to GI severity.
4. **Imaging:** limb **lymphoscintigraphy** can confirm impaired lymph transport. Ultrasound, MRI/MR lymphangiography, CT, echocardiography, or targeted organ imaging is selected by phenotype. (lee2018hennekamsyndromea pages 3-5, vignes2021primarylymphedemafrench pages 1-2)
5. **GI evaluation:** endoscopy/biopsy for suspected intestinal lymphangiectasia, recognizing patchiness and possible false-negative biopsy. (ivanovski2018vanmaldergemsyndrome pages 6-7)
6. **Molecular confirmation:** a comprehensive primary-lymphedema/lymphatic-anomaly panel including **FAT4, CCBE1, ADAMTS3, DCHS1, FLT4, FOXC2, GATA2, PIEZO1, EPHB4, CELSR1** and other validated genes is efficient. The published FAT4 patient was diagnosed on a 36-gene lymphedema panel. If negative, trio WES or WGS with copy-number and splice-aware analysis is appropriate. (ivanovski2018vanmaldergemsyndrome pages 6-7)

Single-gene FAT4 testing is reasonable when phenotype and segregation are highly characteristic. WES/WGS is particularly useful for atypical disease, phenotypic overlap with Van Maldergem syndrome, or a negative panel. CMA/karyotype may evaluate an alternative syndromic diagnosis but are not primary tests for a single-nucleotide/small-indel FAT4 disorder; karyotype and array-CGH were normal in reported cases. FISH, mitochondrial DNA, repeat-expansion, liquid-biopsy, proteomic, metabolomic, and epigenomic testing have no established diagnostic role. (ivanovski2018vanmaldergemsyndrome pages 6-7)

### Differential diagnosis

Major alternatives are CCBE1-related HKLLS1; ADAMTS3-related HKLLS3; Van Maldergem syndrome 2; Milroy disease/FLT4; lymphedema-distichiasis/FOXC2; PIEZO1-related generalized lymphatic dysplasia; GATA2 deficiency/Emberger syndrome; Noonan-spectrum disorders; primary intestinal lymphangiectasia; and CHAPLE/CD55 deficiency. VMS overlaps in face and neurodevelopment but more typically has neonatal hypotonia, feeding/breathing problems, tracheal anomalies, hearing loss, osteopenia, camptodactyly, and less prominent lymphatic disease. (ivanovski2018vanmaldergemsyndrome pages 1-2, ivanovski2018vanmaldergemsyndrome pages 7-8)

There are no universally accepted HKLLS2-specific diagnostic criteria and no population or newborn screening program. Cascade testing is appropriate after a familial variant is identified.

## 11. Outcome and prognosis

No 5- or 10-year survival, life expectancy, disease-specific mortality, or validated prognostic-biomarker data exist. Prognosis is probably driven by extent of lymphatic disease, protein-losing enteropathy, serous effusions, recurrent infection, nutritional deficiency, and developmental/airway or other organ involvement. This is clinical inference, not a validated model.

Morbidity includes chronic swelling, reduced mobility or dexterity, skin thickening/fibrosis, genital involvement, cellulitis/erysipelas, abdominal symptoms, malnutrition, hypoalbuminemia, immune-protein loss, and psychosocial burden. Cellulitis is the principal acute complication in primary lymphedema generally. Edema can improve substantially but usually requires lifelong control; structural lymphatic dysplasia is not expected to recover completely. (musumeci2006cutaneousmanifestationsand pages 3-4, vignes2021primarylymphedemafrench pages 1-2)

## 12. Treatment and current applications

There is **no approved FAT4-directed or curative therapy**. Care is multidisciplinary and phenotype-directed.

### Lymphedema care

Complete decongestive therapy combines low-stretch multilayer bandaging, appropriately fitted compression garments, manual lymph drainage where indicated, exercise with compression, skin care, weight/mobility optimization, limb elevation, and patient/family education. The French national protocol describes reduction with low-stretch bandages followed by long-term stabilization through exercise and compression. (vignes2021primarylymphedemafrench pages 1-2)

In one non-genotyped Hennekam case, seven sessions combining drainage, prolonged compression, exercise, and low-level laser therapy reduced upper-arm circumference from **22 to 19 cm** and forearm circumference from **22.5 to 21 cm**. This uncontrolled observation supports feasibility, not laser efficacy or FAT4-specific response. (lee2018hennekamsyndromea pages 3-5)

Suggested NCIT intervention concepts include **Compression Therapy**, **Physical Therapy**, **Exercise Therapy**, **Manual Lymphatic Drainage**, **Nutritional Support**, and **Genetic Counseling**; exact current NCIT codes should be resolved against the live thesaurus.

### Intestinal lymphangiectasia/protein loss

Use a high-protein, low-long-chain-fat diet with **medium-chain triglycerides**, individualized by a metabolic dietitian. Monitor growth, albumin, immunoglobulins, electrolytes, vitamins, and trace elements. Albumin infusion can be used for severe symptomatic hypoalbuminemia; the FAT4 patient received albumin after edema began. It replaces loss temporarily and does not correct the lymphatic defect. (ivanovski2018vanmaldergemsyndrome pages 6-7, musumeci2006cutaneousmanifestationsand pages 3-4)

### Infection and surgery

Meticulous hygiene, emollients, treatment of fissures/tinea, and prompt systemic antibiotics for cellulitis are central. Recurrent cellulitis may justify prophylactic antibiotics under specialist protocols. Debulking, lymphaticovenous anastomosis, vascularized lymph-node transfer, or other reconstructive procedures may be considered in selected refractory anatomy, but historical Hennekam surgery has had frequent recurrence/complications and no FAT4-specific outcome series exists. Intermittent pneumatic compression deserves caution in children or genital disease. (musumeci2006cutaneousmanifestationsand pages 3-4)

No HKLLS2 pharmacogenomic guidance, gene therapy, cell therapy, RNA therapy, immunotherapy, approved targeted drug, or relevant disease-specific interventional trial was identified. Patent searching likewise produced no credible FAT4-Hennekam therapeutic implementation.

## 13. Prevention

The genotype itself cannot be prevented by lifestyle change. **Primary reproductive prevention/options** include carrier testing of relatives, genetic counseling, prenatal diagnosis, and preimplantation genetic testing when familial pathogenic variants are known. **Secondary prevention** consists of early diagnosis in siblings and early assessment for edema, GI protein loss, growth failure, and developmental needs. **Tertiary prevention** includes compression/exercise, skin care, cellulitis education, nutritional surveillance, immunization according to routine schedules, and prompt treatment of infection. No disease-specific vaccine, chemoprophylaxis, environmental intervention, or public-health screening program exists. (musumeci2006cutaneousmanifestationsand pages 3-4, vignes2021primarylymphedemafrench pages 1-2)

## 14. Other species and natural disease

No naturally occurring veterinary syndrome clearly homologous to human FAT4-related HKLLS2 was identified. Thus, breed enrichment, VBO annotation, veterinary prevalence, transmission, and zoonotic potential are **not applicable/unknown**. FAT4 orthologs and the FAT–Dachsous polarity system are evolutionarily conserved across metazoans, but experimental ortholog phenotypes should not be described as spontaneous Hennekam disease. (medina2023structureofthe pages 1-2)

## 15. Model organisms

The principal model is the **Fat4-null mouse** (*Mus musculus*, NCBI Taxonomy 10090), with Dchs1-null mice serving as pathway-comparison models. Both are genetic knockout models. They reproduce defective lymphatic-valve endothelial orientation and leaflet morphogenesis, directly supporting the lymphedema mechanism; they also show broader developmental abnormalities and die shortly after birth, limiting modeling of chronic human survival and treatment response. (medina2023structureofthe pages 1-2, pujol2017dachsous1–fat4signalingcontrols pages 1-2)

Relevant in-vitro systems include cultured lymphatic endothelial cells and HEK293 co-expression assays. FAT4 and DCHS1 are recruited to cell–cell contacts; DCHS1 localizes to protrusions and junctions. These systems are useful for adhesion, polarization, phosphorylation, and variant-binding assays but do not reproduce whole-organ lymph flow, intestinal protein loss, or neurodevelopment. (pujol2017dachsous1–fat4signalingcontrols pages 2-4, medina2023structureofthe pages 9-10)

The 2023 structural work adds purified-protein crystallography and AlphaFold-assisted modeling, with structures **PDB 8EGW/8EGX**. No HKLLS2-specific zebrafish, organoid, patient-iPSC, rat, Drosophila disease-model, or humanized mouse treatment platform was identified in the retrieved literature. (medina2023structureofthe pages 9-10)

## Key exact quotations from primary/authoritative sources

* Ivanovski et al., published May 2018: **“Biallelic variants in FAT4 are associated with the two disorders, Van Maldergem syndrome (VMS) … and Hennekam syndrome (HS) ….”** DOI: https://doi.org/10.1002/ajmg.a.38652. (ivanovski2018vanmaldergemsyndrome pages 1-2)
* Pujol et al., published September 2017: **“The overall architecture of lymphatic vasculature is unaltered, yet both genes are specifically required for lymphatic valve morphogenesis.”** DOI: https://doi.org/10.1161/ATVBAHA.117.309818. (pujol2017dachsous1–fat4signalingcontrols pages 1-2)
* The same study concluded: **“This study highlights that valve defects may contribute to lymphedema in Hennekam syndrome caused by Fat4 mutations.”** (pujol2017dachsous1–fat4signalingcontrols pages 1-2)
* Medina et al., accepted 1 February 2023: **“The binding domains of Fat4 and Dchs1 form an extended interface along extracellular cadherin (EC) domains 1–4 of each protein.”** DOI: https://doi.org/10.1038/s41467-023-36435-x. (medina2023structureofthe pages 1-2)
* French National Diagnosis and Care Protocol, published January 2021: **“Treatment aims to prevent those complications, reduce the volume with low-stretch bandages, then stabilize it over the long term by exercises and wearing a compression garment.”** DOI: https://doi.org/10.1186/s13023-020-01652-w. (vignes2021primarylymphedemafrench pages 1-2)

## Evidence gaps and expert interpretation

The principal limitation is not conflicting evidence but scarcity. No large FAT4-specific natural-history cohort, registry-derived epidemiology, prospective treatment trial, standardized outcome set, patient-reported outcome study, or 2023–2024 subtype-specific clinical series was found. The most important recent advance is the 2023 structural definition of the FAT4–DCHS1 interface; 2024 literature mainly updates general lymphatic-development biology rather than HKLLS2 clinical care. Accordingly, exact phenotype percentages, sex ratios, prevalence, penetrance, life expectancy, response rates, allele frequencies, and prognostic biomarkers should be stored as **unknown**, while patient-level observations should retain their provenance and denominator. The most defensible current model is biallelic FAT4 dysfunction → disturbed DCHS1–FAT4 planar polarity → failed lymphatic-valve endothelial reorientation and leaflet maturation → impaired lymph transport, lymphedema, and visceral lymphangiectasia. (pujol2017dachsous1–fat4signalingcontrols pages 1-2, medina2023structureofthe pages 9-10, ivanovski2018vanmaldergemsyndrome pages 7-8)

References

1. (ivanovski2018vanmaldergemsyndrome pages 7-8): Ivan Ivanovski, Susan Akbaroghli, Marzia Pollazzon, Chiara Gelmini, Stefano Giuseppe Caraffi, Mahboubeh Mansouri, Zahra Chavoshzadeh, Simonetta Rosato, Valeria Polizzi, Giancarlo Gargano, Marielle Alders, Livia Garavelli, and Raoul C. Hennekam. Van maldergem syndrome and hennekam syndrome: further delineation of allelic phenotypes. American Journal of Medical Genetics Part A, 176:1166-1174, May 2018. URL: https://doi.org/10.1002/ajmg.a.38652, doi:10.1002/ajmg.a.38652. This article has 33 citations.

2. (ivanovski2018vanmaldergemsyndrome pages 1-2): Ivan Ivanovski, Susan Akbaroghli, Marzia Pollazzon, Chiara Gelmini, Stefano Giuseppe Caraffi, Mahboubeh Mansouri, Zahra Chavoshzadeh, Simonetta Rosato, Valeria Polizzi, Giancarlo Gargano, Marielle Alders, Livia Garavelli, and Raoul C. Hennekam. Van maldergem syndrome and hennekam syndrome: further delineation of allelic phenotypes. American Journal of Medical Genetics Part A, 176:1166-1174, May 2018. URL: https://doi.org/10.1002/ajmg.a.38652, doi:10.1002/ajmg.a.38652. This article has 33 citations.

3. (OpenTargets Search: Hennekam lymphangiectasia-lymphedema syndrome 2-FAT4): Open Targets Query (Hennekam lymphangiectasia-lymphedema syndrome 2-FAT4, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (medina2023structureofthe pages 1-2): Elliot Medina, Yathreb Easa, Daniel K. Lester, Eric K. Lau, David Sprinzak, and Vincent C. Luca. Structure of the planar cell polarity cadherins fat4 and dachsous1. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36435-x, doi:10.1038/s41467-023-36435-x. This article has 23 citations and is from a highest quality peer-reviewed journal.

5. (pujol2017dachsous1–fat4signalingcontrols pages 1-2): Francoise Pujol, Tina Hodgson, Ines Martinez-Corral, Anne-Catherine Prats, Danelle Devenport, Masatoshi Takeichi, Elisabeth Genot, Taija Mäkinen, Philippa Francis-West, Barbara Garmy-Susini, and Florence Tatin. Dachsous1–fat4 signaling controls endothelial cell polarization during lymphatic valve morphogenesis—brief report. Arteriosclerosis, Thrombosis, and Vascular Biology, 37:1732–1735, Sep 2017. URL: https://doi.org/10.1161/atvbaha.117.309818, doi:10.1161/atvbaha.117.309818. This article has 49 citations and is from a domain leading peer-reviewed journal.

6. (pujol2017dachsous1–fat4signalingcontrols pages 2-4): Francoise Pujol, Tina Hodgson, Ines Martinez-Corral, Anne-Catherine Prats, Danelle Devenport, Masatoshi Takeichi, Elisabeth Genot, Taija Mäkinen, Philippa Francis-West, Barbara Garmy-Susini, and Florence Tatin. Dachsous1–fat4 signaling controls endothelial cell polarization during lymphatic valve morphogenesis—brief report. Arteriosclerosis, Thrombosis, and Vascular Biology, 37:1732–1735, Sep 2017. URL: https://doi.org/10.1161/atvbaha.117.309818, doi:10.1161/atvbaha.117.309818. This article has 49 citations and is from a domain leading peer-reviewed journal.

7. (ivanovski2018vanmaldergemsyndrome pages 6-7): Ivan Ivanovski, Susan Akbaroghli, Marzia Pollazzon, Chiara Gelmini, Stefano Giuseppe Caraffi, Mahboubeh Mansouri, Zahra Chavoshzadeh, Simonetta Rosato, Valeria Polizzi, Giancarlo Gargano, Marielle Alders, Livia Garavelli, and Raoul C. Hennekam. Van maldergem syndrome and hennekam syndrome: further delineation of allelic phenotypes. American Journal of Medical Genetics Part A, 176:1166-1174, May 2018. URL: https://doi.org/10.1002/ajmg.a.38652, doi:10.1002/ajmg.a.38652. This article has 33 citations.

8. (pujol2017dachsous1–fat4signalingcontrols pages 4-8): Francoise Pujol, Tina Hodgson, Ines Martinez-Corral, Anne-Catherine Prats, Danelle Devenport, Masatoshi Takeichi, Elisabeth Genot, Taija Mäkinen, Philippa Francis-West, Barbara Garmy-Susini, and Florence Tatin. Dachsous1–fat4 signaling controls endothelial cell polarization during lymphatic valve morphogenesis—brief report. Arteriosclerosis, Thrombosis, and Vascular Biology, 37:1732–1735, Sep 2017. URL: https://doi.org/10.1161/atvbaha.117.309818, doi:10.1161/atvbaha.117.309818. This article has 49 citations and is from a domain leading peer-reviewed journal.

9. (medina2023structureofthe pages 9-10): Elliot Medina, Yathreb Easa, Daniel K. Lester, Eric K. Lau, David Sprinzak, and Vincent C. Luca. Structure of the planar cell polarity cadherins fat4 and dachsous1. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36435-x, doi:10.1038/s41467-023-36435-x. This article has 23 citations and is from a highest quality peer-reviewed journal.

10. (vignes2021primarylymphedemafrench pages 1-2): Stéphane Vignes, Juliette Albuisson, Laurence Champion, Joël Constans, Valérie Tauveron, Julie Malloizel, Isabelle Quéré, Laura Simon, Maria Arrault, Patrick Trévidic, Philippe Azria, and Annabel Maruani. Primary lymphedema french national diagnosis and care protocol (pnds; protocole national de diagnostic et de soins). Orphanet Journal of Rare Diseases, Jan 2021. URL: https://doi.org/10.1186/s13023-020-01652-w, doi:10.1186/s13023-020-01652-w. This article has 45 citations and is from a peer-reviewed journal.

11. (lee2018hennekamsyndromea pages 3-5): Yeong Guk Lee, Seung Chan Kim, Si-Bog Park, and Mi Jung Kim. Hennekam syndrome: a case report. Annals of Rehabilitation Medicine, 42:184-188, Feb 2018. URL: https://doi.org/10.5535/arm.2018.42.1.184, doi:10.5535/arm.2018.42.1.184. This article has 11 citations.

12. (musumeci2006cutaneousmanifestationsand pages 3-4): Maria Letizia Musumeci, Maria Rita Nasca, Rocco De Pasquale, Robert A. Schwartz, and Giuseppe Micali. Cutaneous manifestations and massive genital involvement in hennekam syndrome. Pediatric Dermatology, 23:239-242, May 2006. URL: https://doi.org/10.1111/j.1525-1470.2006.00225.x, doi:10.1111/j.1525-1470.2006.00225.x. This article has 23 citations and is from a peer-reviewed journal.

13. (pujol2017dachsous1–fat4signalingcontrols pages 14-15): Francoise Pujol, Tina Hodgson, Ines Martinez-Corral, Anne-Catherine Prats, Danelle Devenport, Masatoshi Takeichi, Elisabeth Genot, Taija Mäkinen, Philippa Francis-West, Barbara Garmy-Susini, and Florence Tatin. Dachsous1–fat4 signaling controls endothelial cell polarization during lymphatic valve morphogenesis—brief report. Arteriosclerosis, Thrombosis, and Vascular Biology, 37:1732–1735, Sep 2017. URL: https://doi.org/10.1161/atvbaha.117.309818, doi:10.1161/atvbaha.117.309818. This article has 49 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md)