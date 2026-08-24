---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-02T01:16:42.620447'
end_time: '2026-08-02T01:24:54.842911'
duration_seconds: 492.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hennekam lymphangiectasia-lymphedema syndrome 1
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
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 1** covering all of the
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
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 1** covering all of the
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


# Hennekam lymphangiectasia–lymphedema syndrome 1

## Executive summary

Hennekam lymphangiectasia–lymphedema syndrome 1 (HKLLS1) is an ultra-rare, autosomal-recessive generalized lymphatic dysplasia caused by biallelic germline variants in **CCBE1**. Its defining manifestations are congenital or early-onset, often progressive lymphedema; visceral lymphangiectasia, particularly of the intestine; characteristic facial morphology; and variably impaired neurodevelopment. Severe fetal disease may present as nonimmune hydrops fetalis, pleural/pericardial effusions, pulmonary hypoplasia, and fetal death. The central molecular lesion is inadequate CCBE1-assisted, ADAMTS3-mediated activation of pro-VEGF-C, reducing VEGFR3 signaling in lymphatic endothelial cells and disrupting embryonic lymphangiogenesis. There is no curative or genotype-directed treatment; management is supportive and multidisciplinary. Published evidence remains dominated by small series and individual cases, and no HKLLS1-specific interventional trial was identified.

A structured, ontology-oriented summary is provided below.

| domain | evidence-backed fact | suggested ontology terms/IDs | evidence type/limitations |
|---|---|---|---|
| Disease identity | Hennekam lymphangiectasia-lymphedema syndrome 1 is the CCBE1-related subtype of Hennekam syndrome, a generalized lymphatic dysplasia with lymphedema, lymphangiectasia, characteristic facial features, and variable intellectual/developmental impairment (roukens2015functionaldissectionof pages 1-3, lee2018hennekamsyndromea pages 1-3) | Disease: Hennekam lymphangiectasia-lymphedema syndrome 1 (MONDO: verify); Hennekam syndrome (OMIM #235510 verify subtype mapping); MeSH: verify | Human clinical + mechanistic review/context; disease identifiers should be verified in OMIM/MONDO for subtype specificity |
| Causal gene | Biallelic pathogenic variants in **CCBE1** cause HKLLS1; CCBE1 encodes collagen and calcium-binding EGF domain-containing protein 1, a secreted extracellular matrix protein essential for lymphatic development (roukens2015functionaldissectionof pages 1-3, melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | Gene: **CCBE1** (HGNC: verify; NCBI Gene: verify); Protein: CCBE1 (UniProt: verify) | Human genetic + animal/mechanistic evidence; exact database IDs should be verified |
| Inheritance | The disorder is autosomal recessive; reported affected individuals carry homozygous or compound heterozygous CCBE1 variants (lee2018hennekamsyndromea pages 1-3, melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | Inheritance: HP:0000007 Autosomal recessive inheritance | Human clinical/genetic evidence; penetrance not well quantified |
| Variant spectrum | Published CCBE1 disease variants include missense, frameshift, and other loss-of-function or hypomorphic alleles; one reported prenatal HKLLS1 case had compound heterozygous **c.683_684insT p.Leu229fs** and **c.335C>T p.Thr112Ile** variants (roukens2015functionaldissectionof pages 1-3, melber2018novelmutationin pages 2-4) | Sequence variant terms: SO:0001589 frameshift_variant; SO:0001583 missense_variant; ACMG class: pathogenic/likely pathogenic (verify per submission) | Human genetic evidence; allele frequencies and classification depend on current ClinVar/gnomAD review |
| Core edema phenotype | Edema is usually congenital and often progressive, commonly involving limbs, genitalia, and face (melber2018novelmutationin pages 1-2) | HP:0001004 Lymphedema; HP:0009826 Facial edema; HP:0010318 Edema; onset: HP:0003577 Congenital onset | Human clinical evidence; frequency across CCBE1-only cases is not robustly quantified |
| Lymphangiectasia phenotype | Maldevelopment of the lymphatic system preferentially affects intestines and limbs, and can also affect pleura, pericardium, kidneys, lungs, and mesentery; case-level imaging documented pulmonary and mesenteric/small-bowel lymphangiectasia (melber2018novelmutationin pages 1-2, lee2018hennekamsyndromea pages 3-5) | HP:0100769 Intestinal lymphangiectasia; HP:0005381 Pleural effusion; HP:0001698 Pericardial effusion; HP term for pulmonary lymphangiectasia: verify; UBERON small intestine UBERON:0002108; lung UBERON:0002048; pleura UBERON:0000977; pericardium UBERON:0002408; kidney UBERON:0002113 | Human clinical/imaging evidence; some involved-organ phenotypes are reported across Hennekam syndrome broadly rather than CCBE1-only cohorts |
| Neurodevelopment | Developmental delay/intellectual disability is variable; one pediatric case showed delays in gross motor, fine motor, personal-social, and functional activities (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5) | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Human clinical evidence; severity spectrum broad and incompletely quantified |
| Facial phenotype | Characteristic face may include flat/flattened midface, broad depressed nasal bridge, hypertelorism, epicanthal folds, small or narrow mouth, and other dysmorphic features, partly attributed to prenatal facial lymphedema (betterman2020atypicalcadherinfat4 pages 1-2, lee2018hennekamsyndromea pages 1-3, melber2018novelmutationin pages 1-2) | HP:0012368 Flat face; HP:0000316 Hypertelorism; HP:0000280 Coarse face verify/not specific; HP:0000426 Depressed nasal bridge; HP:0000286 Epicanthus; HP:0000208 Small mouth | Human clinical evidence; exact HPO term mapping for each facial feature should be confirmed case-by-case |
| Prenatal presentation | HKLLS1 can present prenatally as recurrent nonimmune hydrops fetalis with cystic hygroma, pleural/pericardial effusions, scalp edema, ascites, hepatomegaly, and hypoplastic lungs (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | HP:0001789 Hydrops fetalis; HP:0000476 Scalp edema; HP:0000473 Cystic hygroma; HP:0001541 Ascites; HP:0002240 Hepatomegaly; HP:0002089 Pulmonary hypoplasia | Human prenatal case evidence; based on case report, so not all patients present this way |
| Pathophysiology | CCBE1 is a crucial regulator of **VEGF-C/VEGFR3** signaling; it enhances proteolytic processing/activation of VEGF-C via **ADAMTS3**, enabling lymphatic endothelial sprouting and lymphangiogenesis (roukens2015functionaldissectionof pages 1-3, betterman2020atypicalcadherinfat4 pages 1-2) | Pathway: VEGF-C/VEGFR3 signaling pathway (Reactome/KEGG: verify); GO:0001946 lymphangiogenesis; GO:0001525 angiogenesis; GO term for VEGF-C activation/proteolytic processing: verify | Strong mechanistic support from mouse, zebrafish, and in vitro systems; human inference is biologically well supported but indirect |
| Cellular context | The key affected cell population is the **lymphatic endothelial cell (LEC)**; CCBE1-dependent VEGF-C signaling is required for LEC migration/sprouting from embryonic veins and lymphatic vessel morphogenesis (roukens2015functionaldissectionof pages 1-3, betterman2020atypicalcadherinfat4 pages 1-2) | Cell Ontology: lymphatic endothelial cell (CL ID: verify); GO:0035855 megakaryocyte? not relevant; GO:0043542 endothelial cell migration verify; UBERON cardinal vein: verify | Animal/mechanistic evidence; cell ontology ID should be verified before KB ingestion |
| Protein/domain mechanism | CCBE1 contains EGF/calcium-binding EGF domains and collagen repeat domains; functional studies indicate collagen domains are crucial for VEGF-C activation, while EGF domains are required for full in vivo lymphangiogenic activity (roukens2015functionaldissectionof pages 1-3) | Protein domains: EGF-like domain (InterPro/Pfam: verify); collagen repeat domain (InterPro/Pfam: verify) | Mouse, zebrafish, in vitro domain-dissection evidence; not a routine clinical biomarker |
| Anatomy affected | Primary involvement is the lymphatic vasculature across limb soft tissues and viscera; secondary involvement may include intestine, lung, pleura, pericardium, mesentery, face, and possibly kidney (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2) | UBERON lymph vessel: UBERON:0002019 verify; small intestine UBERON:0002108; mesentery UBERON:0002385; lung UBERON:0002048; face UBERON:0001684; limb UBERON:0002101/0002102 verify | Human imaging/clinical evidence; organ distribution heterogeneous |
| Diagnostic workup | Diagnosis is clinical plus imaging and molecular confirmation. Reported tests include lymphatic scan showing absent visible lymphatic flow, CT angiography for lymphedema, chest CT and abdominal ultrasound for lymphangiectasia, MRI for CNS findings, and prenatal WES after nondiagnostic karyotype/microarray/workup (lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | NCIT: Whole Exome Sequencing (verify); LOINC/NCIT for lymphoscintigraphy, CT angiography, MRI, ultrasound: verify; HP:0000478 Abnormality of the eye? not relevant | Human clinical evidence; no universally standardized disease-specific diagnostic criteria were identified |
| Genetic testing strategy | WES is useful when phenotype is nonspecific, especially in prenatal hydrops; trio exome identified causal CCBE1 variants after normal karyotype, microarray, infectious, hematologic, and metabolic testing (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | Test strategy terms: trio exome sequencing (NCIT: verify); prenatal diagnosis (NCIT: verify) | Human prenatal case evidence; WGS/panel utility for HKLLS1 specifically not systematically studied |
| Differential diagnosis | Differential diagnosis includes other monogenic primary lymphedema/generalized lymphatic dysplasia disorders involving genes such as FAT4, ADAMTS3, FLT4/VEGFR3, VEGFC, PIEZO1, EPHB4, FOXC2, GATA2 and related syndromic/non-syndromic hydrops etiologies (betterman2020atypicalcadherinfat4 pages 1-2, melber2018novelmutationin pages 1-2) | Differential disease terms: primary lymphedema (MONDO/Orphanet verify); generalized lymphatic dysplasia (verify) | Mostly broader disease-context evidence; not an exhaustive formal differential list |
| Laboratory findings | Intestinal lymphangiectasia can cause hypoproteinemia, hypoalbuminemia, hypogammaglobulinemia, lymphopenia, and growth problems, although these were absent in one pediatric case with mesenteric lymphangiectasia (lee2018hennekamsyndromea pages 3-5) | HP:0003073 Hypoproteinemia; HP:0003075 Hypoalbuminemia; HP:0004313 Hypogammaglobulinemia; HP:0001888 Lymphopenia; HP:0001510 Growth delay | Evidence mainly from syndrome-level literature/case discussion rather than CCBE1-only cohort statistics |
| Treatment/supportive care | No curative therapy is established. Supportive lymphedema care includes complete decongestive therapy: manual lymph drainage, compression bandaging/garments, exercise, skin care/rehabilitation; one Hennekam case improved arm circumference after 7 sessions (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5) | NCIT: Manual Lymphatic Drainage (verify); Compression Bandage (verify); Exercise Therapy (NCIT: verify); Physical Therapy (NCIT: C15329 verify) | Disease-specific evidence is limited to single-case rehabilitation report; larger lymphedema trial data are not HKLLS1-specific |
| Enteropathy management | For protein-losing enteropathy due to intestinal lymphangiectasia, recommended supportive management includes high-protein, low-fat diet with medium-chain triglyceride supplementation (lee2018hennekamsyndromea pages 3-5) | NCIT/CHEBI: Medium-Chain Triglyceride (verify); dietary management term (verify) | Syndrome-level supportive recommendation; efficacy in HKLLS1 not tested in controlled trials |
| Surgical/interventional care | Surgery is considered a last resort for severe lymphedema that does not respond to conservative treatment (lee2018hennekamsyndromea pages 3-5) | NCIT surgical procedure for lymphedema: verify | Supportive statement from case discussion/referenced literature; no HKLLS1 surgical outcomes series identified |
| Prognosis | Prognosis is variable and depends on extent of visceral lymphatic involvement; prenatal hydrops and pulmonary involvement are poor prognostic features, whereas surviving children may have chronic morbidity dominated by edema and developmental issues (lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2) | Prognostic features: HP:0001789 Hydrops fetalis; HP:0002089 Pulmonary hypoplasia; HP:0001004 Lymphedema | Evidence from case reports and syndrome-level observations; no survival curves or life-expectancy estimates specific to HKLLS1 |
| Prevention/genetic counseling | Primary prevention is not available for the Mendelian disease itself; secondary prevention/reproductive options include carrier testing of parents, recurrence-risk counseling for autosomal recessive inheritance, and prenatal molecular diagnosis if familial variants are known (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4) | HP:0000007 Autosomal recessive inheritance; prenatal diagnosis term (NCIT: verify); carrier testing term (NCIT: verify) | Logic follows established Mendelian counseling practice; disease-specific counseling guidelines not identified |
| Recent developments (2023-2024 relevance) | Recent literature continues to frame CCBE1 disease within dysregulated lymphatic **VEGFR3 signaling** and developmental lymphatic biology, but no 2023-2024 HKLLS1-specific therapeutic breakthrough or interventional trial was identified (betterman2020atypicalcadherinfat4 pages 1-2, NCT06327412 chunk 1) | Pathway annotations above; clinical trial terms: primary lymphedema exercise trial NCT06327412 | Recent sources are mostly mechanistic or broader lymphedema-focused, not subtype-specific |
| Major data gaps | Major gaps include subtype-specific prevalence/incidence, natural history, penetrance/expressivity estimates, standardized diagnostic criteria, validated biomarkers, genotype-phenotype correlations across CCBE1 alleles, long-term QoL data, and controlled treatment studies specific to HKLLS1 (lee2018hennekamsyndromea pages 1-3, melber2018novelmutationin pages 1-2) | Evidence gap annotation; ontology IDs not applicable | Explicitly based on absence of robust cohort-level evidence in retrieved sources |


*Table: This table summarizes ontology-ready, evidence-backed facts for CCBE1-related Hennekam lymphangiectasia-lymphedema syndrome 1 only. It is designed to support knowledge-base curation while clearly flagging where identifiers or conclusions require verification or where evidence remains sparse.*

## 1. Disease information

### Definition and nomenclature

HKLLS1 is the **CCBE1-related subtype** of Hennekam syndrome. The broader syndrome is characterized by congenital lymphedema and lymphangiectasia, unusual facial morphology—at least partly attributed to intrauterine facial edema—and variable intellectual disability. The disease was first clinically delineated in 1989; CCBE1 was established as a cause in 2009. A 2018 clinical report stated that fewer than 50 Hennekam cases had then been reported, although that number included genetically heterogeneous Hennekam syndrome rather than CCBE1-confirmed HKLLS1 alone. Approximately 25% of clinically suspected Hennekam cases have been reported to carry CCBE1 variants. These historical estimates should not be interpreted as contemporary population prevalence. (betterman2020atypicalcadherinfat4 pages 1-2, lee2018hennekamsyndromea pages 1-3, melber2018novelmutationin pages 1-2)

**Identifiers and synonyms**

- **OMIM:** 235510, Hennekam lymphangiectasia–lymphedema syndrome 1/Hennekam syndrome. The retrieved literature explicitly associates OMIM 235510 with the CCBE1-related disorder. (betterman2020atypicalcadherinfat4 pages 1-2)
- **MONDO:** a subtype-specific MONDO identifier was not securely established from the retrieved primary literature and should be verified against the current MONDO release before ingestion.
- **Orphanet:** use the current Orphanet entry for Hennekam syndrome/generalized lymphatic dysplasia; subtype mapping should likewise be verified in the live database.
- **ICD-10/ICD-11:** no uniquely specific HKLLS1 code was identified. Coding generally falls under congenital lymphatic malformations or hereditary lymphedema.
- **MeSH:** no disease-specific MeSH heading was identified; “Lymphedema,” “Lymphangiectasis,” and “Lymphatic Abnormalities” are appropriate broader concepts.
- Synonyms include **Hennekam syndrome type 1**, **CCBE1-related Hennekam syndrome**, **Hennekam lymphangiectasia–lymphedema syndrome**, and historically **lymphedema–lymphangiectasia–intellectual disability syndrome**.

This report synthesizes **aggregated disease-level literature plus individual published patients and experimental models**. It is not derived from an electronic-health-record cohort.

**Important disambiguation:** HKLLS1 is distinct from FAT4-related Hennekam syndrome type 2 and ADAMTS3-related type 3. It is also entirely distinct from **Menke–Hennekam syndrome**, a CREBBP/EP300-associated neurodevelopmental disorder.

## 2. Etiology, risk, protection, and environment

### Causal factor

The primary cause is **biallelic germline pathogenic or likely pathogenic variation in CCBE1**, usually homozygous or compound heterozygous. CCBE1 encodes a secreted extracellular-matrix-associated protein required for lymphatic development. Disease alleles include missense and truncating/frameshift variants affecting its cysteine-rich, EGF-like, calcium-binding EGF-like, or collagen-repeat regions. (roukens2015functionaldissectionof pages 1-3, melber2018novelmutationin pages 1-2)

No infectious, toxic, dietary, occupational, radiation, smoking, or other lifestyle cause is established. Maternal exposures do not cause the Mendelian disorder. Environmental factors may, however, alter complications: trauma, obesity, immobility, heat, skin injury, or infection can aggravate lymphedema generally, but HKLLS1-specific interaction studies are unavailable.

### Risk and protective factors

- **Genetic risk:** having two disease-causing CCBE1 alleles. For two confirmed heterozygous parents, the expected risk per pregnancy is 25% affected, 50% carrier, and 25% unaffected/non-carrier.
- **Family history/consanguinity:** consanguinity increases the probability that both parents carry the same rare allele, but compound-heterozygous disease also occurs in nonconsanguineous families.
- **Sex:** no established sex bias.
- **Modifier genes, protective variants, or protective alleles:** none validated.
- **Gene–environment interactions:** no formal HKLLS1 G×E evidence.

## 3. Phenotypic spectrum

The available literature does not provide reliable CCBE1-only percentages for most manifestations. Frequencies below are therefore qualitative unless an explicit statistic is available.

### Core lymphatic phenotypes

- **Lymphedema**—usually congenital, chronic, and often progressive; limbs, face, and genitalia are common sites. It may be generalized, asymmetric, or occasionally concentrated in one limb. Functional effects include heaviness, restricted motion, impaired mobility or hand use, recurrent skin infection risk, and psychosocial burden. Suggested HPO: **HP:0001004 Lymphedema**, **HP:0009826 Facial edema**, and **HP:0003577 Congenital onset**. (lee2018hennekamsyndromea pages 1-3, melber2018novelmutationin pages 1-2)
- **Intestinal lymphangiectasia** can produce protein-losing enteropathy, diarrhea, malabsorption, edema, growth failure, hypoalbuminemia, hypoproteinemia, lymphopenia, and hypogammaglobulinemia. Some radiologically affected patients retain normal protein and albumin, demonstrating variable functional severity. Suggested HPO: **HP:0100769 Intestinal lymphangiectasia**, **HP:0003075 Hypoalbuminemia**, **HP:0001888 Lymphopenia**, and **HP:0004313 Hypogammaglobulinemia**. (lee2018hennekamsyndromea pages 3-5)
- Other visceral sites include lungs, pleura, pericardium, mesentery, and kidneys. Pleural or pericardial effusion and congenital pulmonary lymphangiectasia can cause respiratory compromise. (melber2018novelmutationin pages 2-4, lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2)

### Craniofacial and neurodevelopmental phenotypes

Reported facial findings include a flat midface, broad/depressed nasal bridge, hypertelorism, epicanthal folds, bulbous nasal tip, small or narrow mouth, low-set or dysplastic ears, smooth philtrum, and dental anomalies. Suggested HPO terms include **HP:0012368 Flat face**, **HP:0000426 Depressed nasal bridge**, **HP:0000316 Hypertelorism**, **HP:0000286 Epicanthus**, and **HP:0000208 Small mouth**. (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2)

Development ranges from near-normal to global developmental delay or intellectual disability. Motor, fine-motor, adaptive, and personal-social domains may be affected. Seizures were reported in approximately 33% of the broader historical Hennekam literature, but this is not a reliable CCBE1-specific estimate. Suggested HPO: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**, and **HP:0001250 Seizure**. (lee2018hennekamsyndromea pages 3-5)

### Prenatal and severe presentations

HKLLS1 can present as recurrent nonimmune hydrops fetalis. In one molecularly confirmed family, affected pregnancies manifested at 15–18 weeks with scalp edema, ascites, cystic hygroma, pleural/pericardial effusions, hepatomegaly, and pulmonary hypoplasia. Lymphatic dysplasias account for an estimated 5–15% of nonimmune hydrops generally, and nonimmune hydrops has reported fetal mortality of 50–98%; neither statistic is specific to HKLLS1. Suggested HPO: **HP:0001789 Hydrops fetalis**, **HP:0000473 Cystic hygroma**, **HP:0001541 Ascites**, **HP:0005381 Pleural effusion**, and **HP:0002089 Pulmonary hypoplasia**. (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4)

## 4. Genetic and molecular information

### Gene and inheritance

- **Gene:** **CCBE1**, collagen and calcium-binding EGF domains 1.
- **Origin:** constitutional/germline; no somatic disease mechanism is established.
- **Inheritance:** autosomal recessive, suggested HPO **HP:0000007**.
- **Functional class:** loss-of-function or hypomorphic alleles impair CCBE1’s lymphangiogenic activity.

A prenatal case carried maternally inherited **NM_133459.3:c.683_684insT, p.Leu229fs** and paternally inherited **c.335C>T, p.Thr112Ile**. At publication, the frameshift appeared in 14/277,032 gnomAD chromosomes and p.Thr112Ile in 1/246,160; neither was observed homozygously in the reported data. The first was classified as pathogenic loss-of-function and the second as likely pathogenic on rarity, conservation, domain location, segregation, and computational evidence. (melber2018novelmutationin pages 2-4)

By 2015, nine causal CCBE1 variants had been described in the analyzed literature. Most affected the N-terminal cysteine-rich/EGF regions; two involved collagen repeats. This is historical rather than a complete current ClinVar/HGMD count. No validated modifier gene, epigenetic signature, recurrent chromosomal abnormality, anticipation, or germline-mosaicism rate is known. (roukens2015functionaldissectionof pages 1-3)

## 5. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic CCBE1 dysfunction reduces functional extracellular CCBE1.
2. **Growth-factor processing defect:** CCBE1 normally promotes **ADAMTS3-mediated proteolytic activation of pro-VEGF-C**.
3. **Signaling deficit:** reduced mature VEGF-C lowers activation of **VEGFR3/FLT4** on lymphatic endothelial cells.
4. **Developmental failure:** embryonic lymphatic endothelial progenitors are specified but migrate/sprout inadequately from cardinal veins; lymphatic vessels become sparse, malformed, or functionally insufficient.
5. **Clinical consequences:** interstitial-fluid accumulation causes lymphedema; visceral lymphatic dilation/leakage causes intestinal protein loss, effusions, pulmonary disease, and—in severe fetal cases—hydrops. (betterman2020atypicalcadherinfat4 pages 1-2, roukens2015functionaldissectionof pages 1-3)

The domain-dissection study’s abstract states: **“deleting the collagen domains of CCBE1 has a much stronger effect on CCBE1 activity than deleting the EGF domains”** and concludes that the collagen domains are crucial for VEGF-C activation, whereas EGF domains are needed for full in-vivo lymphangiogenic activity. This is supported by knock-in mice, zebrafish rescue/signaling experiments, and in-vitro VEGF-C processing assays. (roukens2015functionaldissectionof pages 1-3)

Suggested annotations include **GO:0001946 lymphangiogenesis**, endothelial-cell migration, growth-factor proteolytic processing, VEGF receptor signaling, and extracellular-matrix organization. The principal cell type is the **lymphatic endothelial cell**; relevant compartments include extracellular space/matrix and the lymphatic endothelial plasma membrane. Downstream VEGFR3 signaling engages PI3K–AKT and MAPK–ERK, but the primary HKLLS1 defect lies upstream at VEGF-C maturation rather than constitutive activation of those pathways.

No reproducible disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or epigenomic patient signature has been established.

## 6. Anatomy and temporal development

Primary disease resides in the **lymphatic vasculature**, especially lymphatic capillaries and collecting pathways of limb soft tissue and viscera. Relevant anatomical concepts include lymph vessels, skin/subcutis, small intestine, mesentery, lung, pleura, pericardium, kidney, face, external genitalia, and limbs. Affected edema may be bilateral/generalized or markedly asymmetric. (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2)

Onset is prenatal or congenital in many patients. The course is chronic and lifelong; peripheral edema may progress, whereas visceral manifestations may be stable, intermittent, or severe from birth. There are no validated disease stages. Critical periods include fetal lymphatic development, the neonatal respiratory period in pulmonary disease, and early childhood for nutrition and neurodevelopmental intervention.

## 7. Epidemiology and population genetics

No reliable prevalence, incidence, carrier-frequency, sex-ratio, or life-table estimate exists for molecularly confirmed HKLLS1. The statement “fewer than 50 cases” in 2018 refers to Hennekam syndrome broadly and reflects ascertainment and publication, not population prevalence. Cases occur across multiple ancestries; no geographically restricted endemic population or robust founder effect is established. Expressivity is markedly variable, while penetrance among individuals carrying two clearly damaging alleles is presumed high but has not been formally quantified. (lee2018hennekamsyndromea pages 1-3)

## 8. Diagnosis

### Clinical and laboratory evaluation

Suspect HKLLS1 with congenital/early lymphedema plus visceral lymphangiectasia, characteristic facial morphology, developmental differences, or unexplained nonimmune hydrops. Evaluation may include:

- Limb circumference/volume and bioimpedance.
- Lymphoscintigraphy or other lymphatic imaging; one case showed no visible lymphatic flow in the affected arm.
- Ultrasound, CT, or MRI to assess intestinal/mesenteric, pulmonary, pleural, pericardial, renal, and CNS involvement.
- CBC with lymphocyte count; total protein, albumin, immunoglobulins, electrolytes, fat-soluble vitamins, and growth/nutritional status.
- Stool α1-antitrypsin clearance where protein-losing enteropathy is suspected.
- Pulmonary and cardiac assessment when effusions or respiratory symptoms occur. (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5)

### Molecular testing

A practical sequence is a **primary-lymphedema/generalized-lymphatic-dysplasia panel** including CCBE1, FAT4, ADAMTS3, FLT4, VEGFC, PIEZO1, EPHB4, FOXC2, GATA2, and other phenotype-driven genes, or trio WES/WGS when presentation is nonspecific. Confirm candidate variants and parental phase by Sanger sequencing or equivalent. Exon-level deletion/duplication analysis should be included if the assay does not detect copy-number variants.

In recurrent fetal hydrops, trio WES diagnosed HKLLS1 after normal karyotype, microarray, infectious studies, hematologic testing, and metabolic evaluation. The report’s key message was: **“WES is a useful approach for diagnosing rare single-gene conditions with nonspecific phenotypes and should be considered early in the diagnostic process of investigating fetal abnormalities.”** (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4)

CMA, karyotyping, and FISH do not diagnose typical sequence-level CCBE1 disease, although they may exclude chromosomal differentials. Mitochondrial and repeat-expansion testing are not routinely indicated. No validated RNA, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic exists.

### Differential diagnosis

Key differentials include FAT4- and ADAMTS3-related Hennekam syndromes; PIEZO1-related generalized lymphatic dysplasia; FLT4/VEGFR3- or VEGFC-related primary lymphedema; FOXC2 lymphedema-distichiasis; GATA2 deficiency/Emberger syndrome; EPHB4-related lymphatic anomalies; primary intestinal lymphangiectasia; CD55-deficient CHAPLE syndrome; Noonan-spectrum disorders; chromosomal syndromes; and infectious, cardiac, hematologic, metabolic, or structural causes of fetal hydrops. (betterman2020atypicalcadherinfat4 pages 1-2, melber2018novelmutationin pages 1-2)

There are no universally accepted HKLLS1-specific clinical diagnostic criteria. Molecular confirmation is strongly preferred because Hennekam syndrome is genetically heterogeneous.

## 9. Outcome and prognosis

Natural-history data, five- or ten-year survival, and life expectancy are unavailable. Prognosis varies with visceral involvement:

- Hydrops, severe pulmonary lymphangiectasia, pulmonary hypoplasia, or large effusions may be fatal prenatally or neonatally.
- Intestinal lymphangiectasia can cause chronic malnutrition, immunoglobulin/lymphocyte loss, infection susceptibility, and growth impairment.
- Chronic limb edema can cause reduced function, tissue fibrosis, recurrent cellulitis, pain or heaviness, and impaired quality of life.
- Developmental outcome ranges from nearly normal to significant disability.

One review cited in the rehabilitation report noted that pulmonary complications are directly relevant to survival. No validated molecular prognostic biomarker or genotype-based risk calculator exists. (lee2018hennekamsyndromea pages 3-5, melber2018novelmutationin pages 1-2)

## 10. Treatment and real-world implementation

### Lymphedema management

No curative therapy exists. Standard care is **complete decongestive therapy**, combining compression, exercise, skin care, and usually manual lymph drainage, followed by maintenance garments. In one 28-month-old Hennekam patient, seven sessions—including manual drainage, ≥20-hour/day bandaging, exercise, activities-of-daily-living training, and low-level laser—reduced upper-arm circumference from 22 to 19 cm and forearm circumference from 22.5 to 21 cm. This is disease-specific but only single-patient evidence. (lee2018hennekamsyndromea pages 3-5)

A broader randomized lymphedema trial, **NCT01748604**, enrolled 194 patients and compared manual drainage plus pneumatic compression and multilayer bandaging with regimens omitting manual drainage. It was not HKLLS1-specific and its registry text does not establish subtype-specific efficacy. (NCT01748604 chunk 1)

Suggested NCIT intervention concepts: physical therapy, manual lymphatic drainage, compression bandaging/garments, exercise therapy, skin care, and intermittent pneumatic compression.

### Visceral and supportive management

Protein-losing enteropathy is managed with a **high-protein, low-fat diet enriched in medium-chain triglycerides**, with replacement of vitamins, minerals, albumin, or immunoglobulin when clinically indicated. Respiratory effusions, chylothorax, infection, seizures, dental problems, developmental delay, and feeding difficulties require organ-specific care. Surgery is reserved for severe, function-limiting lymphedema refractory to conservative management; no controlled HKLLS1 surgical series exists. (lee2018hennekamsyndromea pages 3-5)

There is no approved CCBE1 replacement, VEGF-C therapy, gene therapy, RNA therapy, cell therapy, or pharmacogenomic algorithm. Although VEGF-C/VEGFR3 biology is an attractive target, augmenting lymphangiogenesis in humans raises safety and delivery concerns and remains experimental.

### Trials and 2023–2024 developments

No HKLLS1-specific interventional trial was found. A 2024 study of aerobic exercise in primary lower-extremity lymphedema, **NCT06327412**, planned 35 adults and assessed limb volume, function, VO₂max, and quality of life; its registry status was unknown and it was not genotype-specific. It therefore cannot be taken as evidence of efficacy in HKLLS1. (NCT06327412 chunk 1)

Recent 2023–2024 research has refined the broader VEGFR3 signaling and lymphatic-development framework, but no disease-specific therapeutic breakthrough, large natural-history cohort, or prospective treatment trial was identified. The most authoritative mechanistic interpretation remains that CCBE1 and ADAMTS3 regulate VEGF-C activation upstream of VEGFR3.

## 11. Prevention

Because HKLLS1 is inherited, lifestyle-based primary prevention is not available. Prevention focuses on:

- **Genetic counseling and cascade testing** after identifying familial variants.
- Carrier testing of reproductive partners or at-risk adult relatives.
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants.
- Preimplantation genetic testing for monogenic disease where desired and legally available.
- Early fetal imaging in at-risk pregnancies, recognizing that a normal early scan does not exclude disease.
- Tertiary prevention through compression, meticulous skin care, prompt treatment of cellulitis, nutritional surveillance, and developmental intervention.

No vaccine, medication, or environmental intervention prevents the underlying disorder.

## 12. Other species and model organisms

No well-established naturally occurring veterinary counterpart was identified, and the disorder is not infectious or zoonotic.

### Zebrafish

Loss of **ccbe1** disrupts lymphovenous sprouting from the cardinal vein, formation of parachordal lymphangioblasts, and major lymphatic vessels. Zebrafish provide rapid in-vivo assays of VEGF-C signaling and variant/domain rescue. Their principal limitation is that they do not reproduce the full human craniofacial, cognitive, intestinal, and chronic edema phenotype. (schultemerker2011lymphaticvascularmorphogenesis pages 7-9, roukens2015functionaldissectionof pages 1-3)

### Mouse

Ccbe1-null embryos specify PROX1-positive lymphatic progenitors but fail to achieve normal migration and lymphatic-network formation. Mice lacking CCBE1 collagen domains phenocopy knockout animals, whereas deletion of EGF domains permits rudimentary lymphatics. These models strongly support developmental causality but severe embryonic phenotypes limit long-term treatment studies. (roukens2015functionaldissectionof pages 1-3)

### In-vitro systems

VEGF-C-processing assays show that CCBE1’s collagen domains are required to enhance ADAMTS3-mediated VEGF-C activation. Human lymphatic endothelial cells are appropriate for downstream signaling and migration studies, although no validated HKLLS1 patient-derived organoid or iPSC platform was identified. (roukens2015functionaldissectionof pages 1-3)

## 13. Evidence limitations and expert assessment

The evidence base is constrained by extreme rarity, genetic heterogeneity, historical grouping of CCBE1-, FAT4-, ADAMTS3-, and genetically unresolved cases, and publication bias toward severe or unusual presentations. Consequently, syndrome-wide percentages should not automatically be assigned to HKLLS1. Current expert interpretation supports a high-confidence causal chain from biallelic CCBE1 dysfunction to deficient VEGF-C activation and developmental lymphatic failure, but clinical genotype–phenotype prediction remains weak. Priority research needs are an international molecular registry, longitudinal natural-history and quality-of-life studies, standardized outcome measures, systematic ClinVar/functional curation, and genotype-specific therapeutic development.

## Key publications and URLs

1. Alders M, et al. **Mutations in CCBE1 cause generalized lymph vessel dysplasia in humans.** *Nature Genetics*. December 2009;41:1272–1274. PMID: **19935664**. https://doi.org/10.1038/ng.484. This is the landmark human gene-discovery study cited by subsequent clinical literature. (lee2018hennekamsyndromea pages 3-5)
2. Roukens MG, et al. **Functional Dissection of the CCBE1 Protein: A Crucial Requirement for the Collagen Repeat Domain.** *Circulation Research*. May 2015;116:1660–1669. https://doi.org/10.1161/CIRCRESAHA.116.304949. (roukens2015functionaldissectionof pages 1-3)
3. Lee YG, et al. **Hennekam Syndrome: A Case Report.** *Annals of Rehabilitation Medicine*. February 2018;42:184–188. https://doi.org/10.5535/arm.2018.42.1.184. (lee2018hennekamsyndromea pages 1-3, lee2018hennekamsyndromea pages 3-5)
4. Melber DJ, et al. **Novel mutation in CCBE1 as a cause of recurrent hydrops fetalis from Hennekam lymphangiectasia-lymphedema syndrome-1.** *Clinical Case Reports*. Published October 2018;6:2358–2363. https://doi.org/10.1002/ccr3.1804. (melber2018novelmutationin pages 1-2, melber2018novelmutationin pages 2-4)
5. Betterman KL, et al. **Atypical cadherin FAT4 orchestrates lymphatic endothelial cell polarity in response to flow.** *Journal of Clinical Investigation*. Published May 18, 2020;130:3315–3328. https://doi.org/10.1172/JCI99027. Although centered on FAT4, it authoritatively contextualizes the CCBE1–ADAMTS3–VEGF-C/VEGFR3 axis and distinguishes Hennekam genetic subtypes. (betterman2020atypicalcadherinfat4 pages 1-2)
6. ClinicalTrials.gov. **NCT01748604: Physical Therapies in the Decongestive Treatment of Lymphedema.** First posted December 12, 2012. https://clinicaltrials.gov/study/NCT01748604. (NCT01748604 chunk 1)
7. ClinicalTrials.gov. **NCT06327412: Effects of Aerobic Exercise in Primary Lower Extremity Lymphedema.** First posted March 25, 2024. https://clinicaltrials.gov/study/NCT06327412. (NCT06327412 chunk 1)

References

1. (roukens2015functionaldissectionof pages 1-3): M. Guy Roukens, Josi Peterson-Maduro, Yvonne Padberg, Michael Jeltsch, Veli-Matti Leppänen, Frank L. Bos, Kari Alitalo, Stefan Schulte-Merker, and Dörte Schulte. Functional dissection of the ccbe1 protein: a crucial requirement for the collagen repeat domain. Circulation Research, 116:1660-1669, May 2015. URL: https://doi.org/10.1161/circresaha.116.304949, doi:10.1161/circresaha.116.304949. This article has 72 citations and is from a highest quality peer-reviewed journal.

2. (lee2018hennekamsyndromea pages 1-3): Yeong Guk Lee, Seung Chan Kim, Si-Bog Park, and Mi Jung Kim. Hennekam syndrome: a case report. Annals of Rehabilitation Medicine, 42:184-188, Feb 2018. URL: https://doi.org/10.5535/arm.2018.42.1.184, doi:10.5535/arm.2018.42.1.184. This article has 11 citations.

3. (melber2018novelmutationin pages 1-2): Dora J. Melber, Tara S. Andreasen, Rong Mao, Tatiana Tvrdik, Christine E. Miller, Thomas R. Moore, Douglas A. Woelkers, and Leah M. Lamale‐Smith. Novel mutation in ccbe 1 as a cause of recurrent hydrops fetalis from hennekam lymphangiectasia‐lymphedema syndrome‐1. Clinical Case Reports, 6:2358-2363, Oct 2018. URL: https://doi.org/10.1002/ccr3.1804, doi:10.1002/ccr3.1804. This article has 7 citations.

4. (melber2018novelmutationin pages 2-4): Dora J. Melber, Tara S. Andreasen, Rong Mao, Tatiana Tvrdik, Christine E. Miller, Thomas R. Moore, Douglas A. Woelkers, and Leah M. Lamale‐Smith. Novel mutation in ccbe 1 as a cause of recurrent hydrops fetalis from hennekam lymphangiectasia‐lymphedema syndrome‐1. Clinical Case Reports, 6:2358-2363, Oct 2018. URL: https://doi.org/10.1002/ccr3.1804, doi:10.1002/ccr3.1804. This article has 7 citations.

5. (lee2018hennekamsyndromea pages 3-5): Yeong Guk Lee, Seung Chan Kim, Si-Bog Park, and Mi Jung Kim. Hennekam syndrome: a case report. Annals of Rehabilitation Medicine, 42:184-188, Feb 2018. URL: https://doi.org/10.5535/arm.2018.42.1.184, doi:10.5535/arm.2018.42.1.184. This article has 11 citations.

6. (betterman2020atypicalcadherinfat4 pages 1-2): Kelly L. Betterman, Drew L. Sutton, Genevieve A. Secker, Jan Kazenwadel, Anna Oszmiana, Lillian Lim, Naoyuki Miura, Lydia Sorokin, Benjamin M. Hogan, Mark L. Kahn, Helen McNeill, and Natasha L. Harvey. Atypical cadherin fat4 orchestrates lymphatic endothelial cell polarity in response to flow. Journal of Clinical Investigation, 130:3315-3328, May 2020. URL: https://doi.org/10.1172/jci99027, doi:10.1172/jci99027. This article has 71 citations and is from a highest quality peer-reviewed journal.

7. (NCT06327412 chunk 1): Havva Talay Çalış. The Effects of Aerobic Exercise in Patients With Primary Lower Extremity Lymphedema. Kayseri City Hospital. 2024. ClinicalTrials.gov Identifier: NCT06327412

8. (NCT01748604 chunk 1): Isabel Forner-Cordero, MD, PhD.. Physical Therapies in the Decongestive Treatment of Lymphedema. Isabel Forner-Cordero, MD, PhD.. 2004. ClinicalTrials.gov Identifier: NCT01748604

9. (schultemerker2011lymphaticvascularmorphogenesis pages 7-9): Stefan Schulte-Merker, Amélie Sabine, and Tatiana V. Petrova. Lymphatic vascular morphogenesis in development, physiology, and disease. Jun 2011. URL: https://doi.org/10.1084/jem2086oia15, doi:10.1084/jem2086oia15. This article has 532 citations.

## Artifacts

- [Edison artifact artifact-00](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)