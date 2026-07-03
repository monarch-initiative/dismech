---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-05T14:24:44.918457'
end_time: '2026-06-05T14:39:23.053674'
duration_seconds: 878.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dyskeratosis Congenita
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dyskeratosis_Congenita-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dyskeratosis Congenita
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dyskeratosis Congenita** covering all of the
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
- **Disease Name:** Dyskeratosis Congenita
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dyskeratosis Congenita** covering all of the
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


# Dyskeratosis Congenita (DC) — Comprehensive Disease Characteristics Report (Mendelian)

**Target disease:** Dyskeratosis congenita (DC)  
**Category:** Mendelian / inherited bone marrow failure syndrome; telomere biology disorder (TBD) / short-telomere syndrome (niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9).  
**MONDO ID:** Not available in the retrieved full-text evidence in this run (mazurek2023dyskeratosiscongenitaas pages 4-5).  

## Executive summary
Dyskeratosis congenita is an ultra-rare inherited, multisystem disorder within the telomere biology disorders spectrum, classically defined by the mucocutaneous triad of **nail dystrophy, abnormal/reticulated skin pigmentation, and oral leukoplakia**, and complicated by progressive **bone marrow failure** and increased **malignancy** and **fibrotic organ disease** risk (koldej2023dyskeratosiscongenitanatural pages 1-2, rolles2024inheritedtelomerebiology pages 8-9, niewisch2023clinicalmanifestationsof pages 1-2). Contemporary understanding frames DC as a disorder of **impaired telomere maintenance**, in which germline pathogenic variants across telomerase, shelterin, CST/replication, and telomerase RNA processing/trafficking pathways cause telomere shortening/dysfunction leading to stem cell exhaustion and tissue failure (revy2023geneticsofhuman pages 5-8, rolles2024inheritedtelomerebiology pages 8-9, mazurek2023dyskeratosiscongenitaas pages 1-2).

A recent 2024 high-impact genetic study expanded DC’s genetic architecture (including a newly implicated X-linked gene **POLA1** and expanded allelic series in **POT1** and **ZCCHC8**) and emphasized that a substantial fraction of clinically diagnosed cases remain genetically unresolved (tummala2024theevolvinggenetic pages 1-2, tummala2024theevolvinggenetic pages 3-5).

| Domain | Summary |
|---|---|
| Identifiers/synonyms | - Dyskeratosis congenita (DC) is also referred to as **Zinsser–Cole–Engman syndrome** in retrieved sources.<br>- It is classified as a **telomere biology disorder (TBD)** / short-telomere syndrome.<br>- Formal **OMIM, Orphanet, ICD-10/11, MeSH, MONDO** codes were **not in retrieved full-text evidence**. (ayas2026dyskeratosiscongenita pages 1-4, mazurek2023dyskeratosiscongenitaas pages 4-5, niewisch2023clinicalmanifestationsof pages 1-2) |
| Core definition | - DC is an **ultra-rare inherited multisystem bone marrow failure syndrome** caused principally by defects in **telomere maintenance**.<br>- The classic diagnostic triad is **nail dystrophy, abnormal/reticulated skin pigmentation, and oral leukoplakia**.<br>- Bone marrow failure and cancer predisposition are central disease-defining complications. (koldej2023dyskeratosiscongenitanatural pages 1-2, tummala2024theevolvinggenetic pages 1-2, rolles2024inheritedtelomerebiology pages 8-9, niewisch2023clinicalmanifestationsof pages 1-2) |
| Key phenotypes & frequencies | - Mucocutaneous triad frequencies reported in one 2023 review: **reticulated pigmentation ~90%, nail dystrophy ~88%, leukoplakia ~80%**.<br>- Bone marrow failure is a hallmark; some sources report **>90% by age 40**.<br>- Extra-hematologic disease includes **pulmonary fibrosis/interstitial lung disease**, **liver disease/portal hypertension**, premature hair graying, and cancer susceptibility; pulmonary fibrosis occurs in about **20%** in one review. (mazurek2023dyskeratosiscongenitaas pages 4-5, ayas2026dyskeratosiscongenita pages 1-4, wang2021pulmonaryfibrosisin pages 1-2, vittal2023progressionofliver pages 1-2, franke2025diagnosisandmanagement pages 7-10) |
| Natural history stats | - In a pediatric cohort (n=14), diagnosis occurred at **median age 8.5 years**; **13/14** progressed to bone marrow failure at **median age 8 years**.<br>- In the same cohort, **6/14 died**, at **median age 13 years**; all had hematologic manifestations at diagnosis and non-hematologic manifestations accumulated over follow-up.<br>- Adult/cryptic TBD can present later with isolated hematologic, pulmonary, or liver disease rather than the full triad. (koldej2023dyskeratosiscongenitanatural pages 1-2, niewisch2023clinicalmanifestationsof pages 1-2, franke2025diagnosisandmanagement pages 7-10) |
| Key causal genes & new 2024 findings | - Established genes in retrieved evidence include **DKC1, TERC, TERT, TINF2, RTEL1, NOP10, NHP2, CTC1, ACD/TPP1, PARN, WRAP53/TCAB1, DCLRE1B, RPA1, NPM1, NAF1** and others; inheritance can be **X-linked, autosomal dominant, or autosomal recessive**.<br>- A 2024 EMBO Molecular Medicine study reported that about **35%** of clinically diagnosed cases remain genetically unresolved and expanded the allelic architecture with **POLA1** (novel X-linked gene), plus additional **POT1** and **ZCCHC8** variants.<br>- Functional data linked new variants to disrupted **primase/CST/shelterin interactions**, reduced POLA1 catalytic activity, reduced POT1 binding to telomeric ssDNA, and ZCCHC8 deficiency with pervasive transcription/inflammation. (tummala2024theevolvinggenetic pages 1-2, tummala2024theevolvinggenetic pages 3-5, niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9) |
| Diagnostics (telomere length testing thresholds, screening yields) | - **Flow-FISH lymphocyte telomere length** is the current preferred functional screening test; a commonly used threshold is **<1st percentile for age** for strong support of TBD/DC diagnosis.<br>- In adults, one 2023 prospective cohort used standard suspicion criteria of **<10th percentile for age** and an extended criterion of **<6.5 kb in patients >40 years**.<br>- In 262 screened adults, shortened TL was found in **120**; among standard-screened patients with NGS material, **17/76 (22.4%)** had pathogenic/likely pathogenic variants and **17/76 (22.4%)** had VUS; main genes were **TERT, TERC, RTEL1**. (rolles2024inheritedtelomerebiology pages 8-9, tometten2023identificationofadult pages 1-2, tometten2023identificationofadult pages 6-7, tometten2023identificationofadult pages 3-4, niewisch2023clinicalmanifestationsof pages 5-5) |
| Treatments (androgens, HSCT, organ transplant considerations) | - **Androgens** (especially **danazol**, also oxymetholone/nandrolone) can improve counts; reported hematologic response rates range about **50–100%** short-term, with one study showing **11/12** patients gained telomere length (**mean +386 bp**) and **83% hematologic response at 24 months**.<br>- **HSCT/allo-HCT** is the only curative therapy for marrow failure/clonal evolution, but transplant morbidity is substantial; **reduced-intensity** and **radiation-avoiding** approaches are favored, and related donors carrying the familial defect should be avoided.<br>- Organ transplantation (especially **lung** and **liver**) may be required for end-organ failure, but telomere disorders increase risk of hematologic and immunosuppression-related complications. (rolles2024inheritedtelomerebiology pages 12-14, ayas2026dyskeratosiscongenita pages 9-12, rolles2024inheritedtelomerebiology pages 10-12, glass2026telomerebiology pages 17-18) |
| Epidemiology | - DC is consistently described as **ultra-rare/rare**.<br>- Retrieved prevalence estimates were approximately **1 case per 1,000,000** in one source and **1–9 per 1,000,000** in another review.<br>- One review noted marked male predominance in historical series (**male:female ~13:1**), though this may reflect enrichment of **X-linked DKC1** disease in some cohorts. (koldej2023dyskeratosiscongenitanatural pages 1-2, mazurek2023dyskeratosiscongenitaas pages 4-5) |


*Table: This table condenses the most actionable facts on dyskeratosis congenita and related telomere biology disorders from the retrieved evidence, including definition, phenotype spectrum, genetics, diagnostics, treatment, and epidemiology. It is designed to support rapid knowledge-base curation with source-linked statements.*

---

## 1. Disease information
### 1.1 What is the disease?
DC is an **inherited multisystem telomere biology disorder** characterized by the **classic mucocutaneous triad** and a high burden of **bone marrow failure (BMF)**, with additional complications including pulmonary and liver disease and cancer predisposition (koldej2023dyskeratosiscongenitanatural pages 1-2, rolles2024inheritedtelomerebiology pages 8-9, niewisch2023clinicalmanifestationsof pages 1-2).

### 1.2 Key identifiers (ontology/coding)
In the retrieved full-text evidence available for this report, specific cross-references (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO) were **not explicitly provided**, so they cannot be populated with evidence-based values here (mazurek2023dyskeratosiscongenitaas pages 4-5).

### 1.3 Synonyms / alternative names
- **Zinsser–Cole–Engman syndrome** (ayas2026dyskeratosiscongenita pages 1-4, mazurek2023dyskeratosiscongenitaas pages 4-5).
- DC is also referenced as the archetypal/“classic” childhood-onset form within the broader **telomere biology disorders** spectrum (niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9).

### 1.4 Evidence sources and aggregation level
The information in this report is derived primarily from:
- **Aggregated disease-level resources and reviews** (e.g., ASH Education Program review 2023; Transfusion Medicine and Hemotherapy review 2024; Nature Reviews Genetics 2023) (niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9, revy2023geneticsofhuman pages 5-8).
- **Cohort studies/natural history studies** (e.g., pediatric cohort natural history 2023; liver involvement cohort 2023; adult screening cohort 2023) (koldej2023dyskeratosiscongenitanatural pages 1-2, vittal2023progressionofliver pages 1-2, tometten2023identificationofadult pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants affecting **telomere maintenance** (telomerase, shelterin, CST complex/replication, telomerase RNA processing/trafficking), producing critically short telomeres and telomere dysfunction (niewisch2023clinicalmanifestationsof pages 1-2, revy2023geneticsofhuman pages 5-8, rolles2024inheritedtelomerebiology pages 8-9).

**Recent genetic expansion (2024):** A large 2024 DC/DC-like study identified novel pathogenic variants and newly implicated the X-linked gene **POLA1**; it also expanded allelic series for **POT1** and **ZCCHC8**, with functional work implicating disrupted interactions among primase, CST, and shelterin and inflammatory signatures from ZCCHC8 deficiency (tummala2024theevolvinggenetic pages 1-2, tummala2024theevolvinggenetic pages 3-5).

**Direct abstract-supported quote (2024 EMBO Mol Med):** the study “identify[ied]… novel pathogenic variants… and in the novel X-linked gene, **POLA1**” and reported functional impacts on “protein–protein interactions with primase, **CST**… and shelterin” (tummala2024theevolvinggenetic pages 1-2).

### 2.2 Risk factors
- **Genetic risk:** Pathogenic variants across multiple telomere genes; incomplete penetrance/variable expressivity is characteristic of TBDs, especially adult-onset “cryptic” presentations (niewisch2023clinicalmanifestationsof pages 1-2, revy2023geneticsofhuman pages 5-8).
- **Genetic anticipation:** Adult TBD reviews emphasize generational worsening linked to inheritance of **short telomere reserve** (tummala2024theevolvinggenetic pages 1-2, franke2025diagnosisandmanagement pages 7-10).

**Environmental/clinical risk modifiers (organ progression):** In a DC/TBD liver cohort, **pulmonary and/or vascular disease** predicted progression to clinically significant liver disease/portal hypertension, suggesting multisystem disease burden modifies organ risk (vittal2023progressionofliver pages 1-2).

### 2.3 Protective factors
No specific protective genetic variants or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not specifically delineated for DC in the retrieved evidence; however, clinical cohorts support that systemic comorbidities (pulmonary/vascular disease) modify progression of liver complications (vittal2023progressionofliver pages 1-2).

---

## 3. Phenotypes
### 3.1 Core mucocutaneous triad (suggested HPO terms)
- **Nail dystrophy / nail dysplasia** (HPO suggestion: *HP:0001597*). DC childhood-onset often includes nail changes (niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9).
- **Abnormal/reticulated skin pigmentation** (HPO suggestion: *HP:0000994* or related terms for skin hyperpigmentation). Frequency estimates in one review: **~90%** reticulated pigmentation (mazurek2023dyskeratosiscongenitaas pages 4-5).
- **Oral leukoplakia** (HPO suggestion: *HP:0002745*). Frequency estimate: **~80%** (mazurek2023dyskeratosiscongenitaas pages 4-5).

**Triad frequency data (review-level):** reticulated pigmentation ~90%, nail dystrophy ~88%, leukoplakia ~80% (mazurek2023dyskeratosiscongenitaas pages 4-5).

### 3.2 Hematologic phenotypes (suggested HPO terms)
- **Bone marrow failure / aplastic anemia** (HPO: *HP:0001915* / *HP:0001917*). BMF is a hallmark; one chapter reports **BMF in >90% by age 40** (ayas2026dyskeratosiscongenita pages 1-4).
- **Cytopenias:** thrombocytopenia (HPO: *HP:0001873*), neutropenia (HPO: *HP:0001875*), macrocytosis (HPO: *HP:0000256*), pancytopenia (HPO: *HP:0001876*) (definitions and use in a pediatric natural history cohort) (koldej2023dyskeratosiscongenitanatural pages 2-3, koldej2023dyskeratosiscongenitanatural pages 1-2).

**Pediatric natural history:** in a multicenter childhood-diagnosed cohort (n=14), *all* had hematologic manifestations at diagnosis; **13/14 progressed to BMF** at median age **8 years** (range 3–18) (koldej2023dyskeratosiscongenitanatural pages 1-2).

### 3.3 Pulmonary phenotypes (suggested HPO terms)
- **Interstitial lung disease / pulmonary fibrosis** (HPO: *HP:0006530* for pulmonary fibrosis). One review reports interstitial lung disease in **~20%** of DC patients (franke2025diagnosisandmanagement pages 7-10). A systematic review/case synthesis also states ~20% develop pulmonary fibrosis (wang2021pulmonaryfibrosisin pages 1-2).

### 3.4 Liver phenotypes (suggested HPO terms)
- **Cholestatic liver enzyme elevation / liver abnormality** (HPO suggestions may include abnormal liver function tests *HP:0002910*).
- **Portal hypertension** (HPO: *HP:0001405*).

**Cohort statistics (2023 Hepatology):** In a DC/TBD cohort (n=58), baseline hepatic abnormality was **72.4%** and **17.2%** developed clinically significant liver disease/portal hypertension over follow-up (median 6 years) (vittal2023progressionofliver pages 1-2).

### 3.5 Cancer predisposition
DC/TBDs are associated with increased malignancy risk; head and neck squamous cell carcinoma is highlighted as a frequent solid tumor in DC/TBD contexts, and leukemia/MDS risks are emphasized in reviews/chapters (ayas2026dyskeratosiscongenita pages 1-4, niewisch2023clinicalmanifestationsof pages 1-2).

### 3.6 Quality of life (QoL)
Disease morbidity is described as high and multisystemic in longitudinal pediatric follow-up, but specific validated QoL instruments (e.g., SF-36, PROMIS) and quantitative QoL scores were **not available in the retrieved evidence** (koldej2023dyskeratosiscongenitanatural pages 1-2).

---

## 4. Genetic / molecular information
### 4.1 Causal genes (selected; non-exhaustive; HGNC symbols)
Authoritative 2023–2024 reviews and studies list DC/TBD genes spanning multiple telomere modules, including:
- **Telomerase core:** *TERT, TERC* (revy2023geneticsofhuman pages 5-8, rolles2024inheritedtelomerebiology pages 8-9).
- **H/ACA RNP and telomerase RNA stability:** *DKC1, NHP2, NOP10, NAF1* (revy2023geneticsofhuman pages 5-8, niewisch2023clinicalmanifestationsof pages 1-2).
- **Telomerase trafficking/recruitment:** *WRAP53/TCAB1* and related factors (niewisch2023clinicalmanifestationsof pages 1-2, rolles2024inheritedtelomerebiology pages 8-9).
- **Shelterin / end protection:** *TINF2, POT1, ACD (TPP1)* (niewisch2023clinicalmanifestationsof pages 1-2, tummala2024theevolvinggenetic pages 3-5).
- **Replication/CST axis:** *CTC1* (and CST complex context), with emerging evidence that CST–Polα/primase interactions are critical (tummala2024theevolvinggenetic pages 3-5, mazurek2023dyskeratosiscongenitaas pages 1-2).
- **RNA processing / additional implicated loci:** *PARN, ZCCHC8* (tummala2024theevolvinggenetic pages 1-2, revy2023geneticsofhuman pages 5-8).

### 4.2 Variant classes and functional consequences
In the 2024 EMBO Molecular Medicine cohort, variant types included predominantly **missense** and **loss-of-function** categories, plus deletions/insertions (tummala2024theevolvinggenetic pages 1-2).

Mechanistic consequences from reviews include:
- Impaired telomerase activity/processivity/recruitment (TERT/TERC and recruitment factors) (niewisch2023clinicalmanifestationsof pages 1-2, revy2023geneticsofhuman pages 5-8).
- Reduced telomerase RNA stability/maturation (DKC1/NHP2/NOP10 axis) (revy2023geneticsofhuman pages 5-8, niewisch2023clinicalmanifestationsof pages 1-2).

### 4.3 Newly implicated genes/alleles (2024)
A 2024 DC/DC-like study:
- Reported a **novel X-linked gene POLA1** with functionally validated disease alleles and skewed X-inactivation in carrier mothers (tummala2024theevolvinggenetic pages 3-5).
- Expanded the allelic series of **POT1** with demonstrated reduced binding to telomeric ssDNA for pathogenic variants (tummala2024theevolvinggenetic pages 3-5).
- Expanded **ZCCHC8** variants associated with deficiency and inflammatory/transcriptional dysregulation signatures in blood (tummala2024theevolvinggenetic pages 1-2).

### 4.4 Modifier genes / polygenic background
The retrieved corpus includes evidence that incomplete penetrance/variable expressivity is common in TBDs and that broader genetic context contributes to variability; specific DC-focused protective modifiers were not identified in the retrieved evidence (niewisch2023clinicalmanifestationsof pages 1-2, revy2023geneticsofhuman pages 5-8).

---

## 5. Environmental information
No specific toxins, lifestyle exposures, or infectious triggers were identified as primary causal factors for DC in the retrieved evidence. Clinical guidance emphasizes the need to recognize DC/TBD prior to potentially harmful treatments (e.g., immunosuppression in fibrotic lung disease contexts) (wang2021pulmonaryfibrosisin pages 1-2).

---

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (upstream → downstream chain)
1. **Upstream trigger:** germline defects in telomere maintenance genes (telomerase, shelterin, CST, RNA processing/trafficking) (rolles2024inheritedtelomerebiology pages 8-9, revy2023geneticsofhuman pages 5-8).  
2. **Molecular consequence:** accelerated telomere shortening and/or telomere dysfunction (very short telomeres are characteristic; diagnostic thresholds often involve <1st percentile for age) (koldej2023dyskeratosiscongenitanatural pages 1-2, rolles2024inheritedtelomerebiology pages 8-9).  
3. **Cellular consequence:** activation of DNA damage responses leading to **senescence and/or apoptosis**, limiting replicative potential of high-turnover tissues (hematopoietic/immune/epithelial compartments) (niewisch2023clinicalmanifestationsof pages 1-2, glass2026telomerebiology pages 1-5).  
4. **Tissue consequence:** stem cell depletion and organ failure phenotypes: bone marrow failure, pulmonary/liver fibrosis; genomic instability contributes to cancer predisposition (ayas2026dyskeratosiscongenita pages 1-4, vittal2023progressionofliver pages 1-2).

### 6.2 Pathways and processes (suggested GO terms)
Suggested GO Biological Process terms consistent with the evidence:
- **Telomere maintenance** (GO:0000723)
- **DNA damage response, signal transduction by p53 class mediator** (GO:0030330)
- **Cellular senescence** (GO:0090398)
- **Apoptotic process** (GO:0006915)
- **Hematopoietic stem cell differentiation / hematopoiesis** (e.g., GO:0030097)

### 6.3 Cell types involved (suggested CL terms)
- **Hematopoietic stem cell** (CL:0000037)
- **Hematopoietic progenitor cell** (CL:0008001)
- **T cell / lymphocyte** (for telomere length assays and immune involvement) (rolles2024inheritedtelomerebiology pages 8-9, niewisch2023clinicalmanifestationsof pages 5-5)
- **Alveolar type II cell** (pulmonary fibrosis context; suggested CL:0002063) (carlier2026hematologicalcomplicationsin pages 2-3)

### 6.4 Mechanistic evidence from model systems
A CRISPR Ten1 knockout mouse (TEN1; CST complex) provides a DC-like in vivo model: Ten1 deficiency caused **telomere shortening**, short lifespan, **aplastic anemia**, **skin hyperpigmentation**, and broad organ pathology with activation of **p53/p21** signaling and evidence of reduced proliferation and increased apoptosis (sanzmoreno2025lossoften1 pages 1-2, sanzmoreno2025lossoften1 pages 3-6, sanzmoreno2025lossoften1 pages 2-3). This supports a causal mechanistic route from CST dysfunction → telomere attrition → p53-mediated tissue failure.

---

## 7. Anatomical structures affected
### 7.1 Organ level (suggested UBERON terms)
- **Bone marrow** (UBERON:0002371) and hematopoietic system (BMF) (ayas2026dyskeratosiscongenita pages 1-4, koldej2023dyskeratosiscongenitanatural pages 1-2).
- **Lung** (UBERON:0002048) (pulmonary fibrosis/ILD) (franke2025diagnosisandmanagement pages 7-10, wang2021pulmonaryfibrosisin pages 1-2).
- **Liver** (UBERON:0002107) (cholestatic abnormalities, portal hypertension) (vittal2023progressionofliver pages 1-2).
- **Skin** (UBERON:0002097) and mucosa/oral cavity (leukoplakia) (rolles2024inheritedtelomerebiology pages 8-9, mazurek2023dyskeratosiscongenitaas pages 4-5).

### 7.2 Tissue and cell level
- High-turnover tissues are emphasized as vulnerable to low telomere reserve, including hematopoietic and immune compartments; liver and lung involvement is prominent in DC/TBD cohorts (rolles2024inheritedtelomerebiology pages 8-9, vittal2023progressionofliver pages 1-2).

### 7.3 Subcellular localization (suggested GO cellular component)
- **Telomere** (GO:0000781)
- **Cajal body** (for WRAP53/TCAB1 biology; relevant to telomerase trafficking) (niewisch2023clinicalmanifestationsof pages 1-2)

---

## 8. Temporal development
### 8.1 Onset
- Classic DC often manifests in **childhood** with mucocutaneous features, while “cryptic” TBD/DC may present in adulthood with isolated marrow, lung, liver disease, or cancer (niewisch2023clinicalmanifestationsof pages 1-2, franke2025diagnosisandmanagement pages 7-10).

### 8.2 Progression
- Pediatric cohort: progressive accumulation of non-hematologic complications; high early hematologic morbidity with frequent progression to BMF and childhood/young-adult mortality (koldej2023dyskeratosiscongenitanatural pages 1-2).
- Liver cohort: baseline liver abnormalities common; subset progresses to portal hypertension over years of follow-up (vittal2023progressionofliver pages 1-2).

---

## 9. Inheritance and population
### 9.1 Epidemiology
- Prevalence estimate reported as ~**1 per 1,000,000** in one source (koldej2023dyskeratosiscongenitanatural pages 1-2).
- Another review reports **1–9 per 1,000,000** (mazurek2023dyskeratosiscongenitaas pages 4-5).

### 9.2 Inheritance patterns
DC/TBDs show all Mendelian modes:
- **X-linked recessive**, **autosomal dominant**, and **autosomal recessive** inheritance (niewisch2023clinicalmanifestationsof pages 1-2, tummala2024theevolvinggenetic pages 1-2).

### 9.3 Demographics
A review reports strong male predominance (male:female ~13:1), likely reflecting enrichment of X-linked disease in some series; population-level sex ratio remains uncertain from the retrieved evidence (mazurek2023dyskeratosiscongenitaas pages 4-5).

Data gaps (not in retrieved evidence): incidence rates, carrier frequency, geographic/ancestry founder effects.

---

## 10. Diagnostics
### 10.1 Clinical criteria (core recognition)
- The classic triad (nail dystrophy, skin pigmentation abnormalities, oral leukoplakia) plus hematologic and multisystem findings supports clinical suspicion (rolles2024inheritedtelomerebiology pages 8-9, niewisch2023clinicalmanifestationsof pages 1-2).

### 10.2 Telomere length testing (real-world implementation)
**Preferred functional test:** **Flow-FISH** telomere length measurement in leukocyte subsets; lymphocyte telomere length is described as sensitive and highly specific (rolles2024inheritedtelomerebiology pages 8-9).  
**Common diagnostic threshold:** lymphocyte telomere length **<1st percentile for age** by flow-FISH strongly supports TBD/DC (rolles2024inheritedtelomerebiology pages 8-9).  

**Adult screening algorithm and yield (2023 prospective cohort):**
- Standard suspicion: **<10th percentile for age**; extended adult criterion: **<6.5 kb in patients >40 years** (tometten2023identificationofadult pages 1-2, tometten2023identificationofadult pages 3-4).
- In 262 referred adults screened by flow-FISH, 120 had shortened telomeres; among standard-screened patients with NGS material, **17/76 (22.4%)** had pathogenic/likely pathogenic variants and **17/76 (22.4%)** had VUS (tometten2023identificationofadult pages 1-2).

### 10.3 Genetic testing strategy
Recent diagnostic pathways recommend:
- Telomere length testing as prescreen, followed by targeted **NGS panels** and, if unresolved, **WES/WGS** focused on telomere maintenance genes (rolles2024inheritedtelomerebiology pages 10-12).
- Recognition that a pathogenic variant is not found in all clinical cases (e.g., ~20% without identifiable cause in one review; ~35% unresolved in a 2024 DC cohort) (niewisch2023clinicalmanifestationsof pages 5-5, tummala2024theevolvinggenetic pages 1-2).

### 10.4 Differential diagnosis
- **Acquired aplastic anemia** vs inherited marrow failure/TBD: telomere testing helps discriminate; evaluation may include Fanconi anemia chromosome breakage testing when relevant (koldej2023dyskeratosiscongenitanatural pages 2-3, NCT01659606 chunk 2).

---

## 11. Outcome / prognosis
### 11.1 Survival and mortality (recent cohort data)
In a Spanish pediatric DC cohort (n=14):
- Median diagnosis age **8.5 years**; **13 progressed to bone marrow failure** at median age **8 years**.
- **6/14 died** at median age **13 years** (range 6–24) (koldej2023dyskeratosiscongenitanatural pages 1-2).

### 11.2 Major morbidity drivers and statistics
- **Bone marrow failure:** reported in **>90% by age 40** in a DC chapter (ayas2026dyskeratosiscongenita pages 1-4).
- **Liver disease:** baseline abnormality **72.4%**; **17.2%** progressed to portal hypertension (vittal2023progressionofliver pages 1-2).
- **Pulmonary fibrosis/ILD:** ~**20%** reported in reviews (franke2025diagnosisandmanagement pages 7-10, wang2021pulmonaryfibrosisin pages 1-2).

### 11.3 Prognostic factors
- Liver progression risk enriched in **recessive or TINF2-associated DC** and predicted by concurrent pulmonary/vascular disease (vittal2023progressionofliver pages 1-2).
- Pulmonary fibrosis systematic review suggests genotype–phenotype correlations (e.g., later ages in TERC/TERT; differences in survival by gene class), and warns against immunosuppression or lung biopsy in unrecognized DC-associated PF (wang2021pulmonaryfibrosisin pages 1-2).

---

## 12. Treatment
### 12.1 Pharmacotherapy — androgens
**Danazol and other androgens** are used as non-transplant therapies for TBD/DC-related marrow failure.
- A 2024 review summarizes androgen response evidence: oxymetholone hematologic responses around **69%** with frequent adverse effects; danazol with fewer side effects and reported hematologic responses (some studies **~83% at 24 months**) and telomere length gains in a subset (e.g., 11/12 gained TL; mean +386 bp) (rolles2024inheritedtelomerebiology pages 12-14).
- A DC chapter also reports observational hematologic response ~70% and prospective danazol trial response ~80%, while noting toxicity (liver enzyme elevation, virilization) and discontinuation risk (ayas2026dyskeratosiscongenita pages 4-7).

**MAXO suggestions:** androgen therapy (e.g., MAXO:0000058 pharmacotherapy; more specific term depends on MAXO mapping availability).

### 12.2 Hematopoietic stem cell transplantation (HSCT)
HSCT is described as the **only curative therapy** for DC marrow failure/clonal evolution, but outcomes are complicated by multisystem fragility (ayas2026dyskeratosiscongenita pages 9-12).

Key implementation considerations:
- Avoid related donors with the same pathogenic variant when possible (risk of graft failure and adverse outcomes) (rolles2024inheritedtelomerebiology pages 10-12).
- **Avoid radiation** in conditioning when possible because of late pulmonary toxicity and secondary malignancy concerns (ayas2026dyskeratosiscongenita pages 9-12).

**ClinicalTrials.gov implementation example:** A radiation- and alkylator-free HSCT regimen trial (NCT01659606) specifies conditioning with **alemtuzumab and fludarabine** and post-transplant immunosuppression options (mycophenolate plus cyclosporine or tacrolimus), with eligibility including DC and related syndromes (NCT01659606 chunk 2).

**MAXO suggestions:** hematopoietic stem cell transplantation (MAXO:0000747), reduced-intensity conditioning (MAXO term depends on available hierarchy).

### 12.3 Solid organ transplantation
For end-stage lung or liver disease, transplantation may be required; reviews emphasize higher complication risk and the need for careful pre-transplant TBD recognition (glass2026telomerebiology pages 17-18).

### 12.4 Experimental/clinical trials landscape (selected, based on retrieved trial records)
- **Danazol trial:** NCT01441037 (“Danazol for Genetic Bone Marrow and Lung Disorders”) targets aplastic anemia/pulmonary fibrosis/liver cirrhosis phenotypes, includes pediatric patients (min age 2 years), and cites a related NEJM publication (NCT01441037 chunk 2).
- **HSCT trials:** NCT02162420 includes transplant conditioning agents (alemtuzumab/fludarabine/cyclophosphamide/TBI, thymoglobulin) and includes “Secondary malignancies” as an outcome (NCT02162420 chunk 2).

Data gap: For some NCT records, **phase/enrollment/status fields were not present** in the retrieved text chunks; therefore they are not reported with evidence here (NCT01441037 chunk 2, NCT02162420 chunk 2).

---

## 13. Prevention
Primary prevention of genetic DC is not generally applicable beyond reproductive options; retrieved evidence emphasizes **surveillance and avoidance of harmful interventions** once disease is suspected/diagnosed.
- For DC-associated pulmonary fibrosis, the systematic review warns against empiric immunosuppression and diagnostic surgical lung biopsy before excluding DC/TBD (wang2021pulmonaryfibrosisin pages 1-2).

**MAXO suggestions:** genetic counseling (MAXO term), surveillance program (MAXO term).

---

## 14. Other species / natural disease
No naturally occurring veterinary DC analogs were identified in the retrieved evidence.

---

## 15. Model organisms
### 15.1 Mammalian model (mouse)
A **Ten1** (CST complex) CRISPR knockout mouse is described as a model of DC/TBD:
- Phenotypes: telomere attrition, short lifespan, skin hyperpigmentation, aplastic anemia/BMF, cerebellar hypoplasia, and multi-organ pathology (sanzmoreno2025lossoften1 pages 1-2, sanzmoreno2025lossoften1 pages 2-3).
- Mechanism: reduced proliferation, increased apoptosis, stem cell depletion, and activation of **p53/p21** signaling (sanzmoreno2025lossoften1 pages 1-2, sanzmoreno2025lossoften1 pages 3-6).

### 15.2 Cellular/ex vivo models
Reviews describe use of CD34+ HSPCs and variant cell models (e.g., DKC1 variant cells), including therapeutic strategy exploration via PAPD5/7 inhibition restoring telomere length/TERC levels in specific contexts (franke2025diagnosisandmanagement pages 15-17, revy2023geneticsofhuman pages 27-30).

---

## Notes on evidence gaps in this run
- **Ontology IDs** (OMIM/Orphanet/MeSH/ICD/MONDO) were not directly present in retrieved full texts; they should be populated by querying OMIM/Orphanet/MONDO directly in a follow-on curation step.
- QoL metrics and standardized diagnostic criteria statements (beyond telomere testing thresholds and clinical triad) were limited in retrieved evidence.

---

## Key recent sources prioritized (2023–2024)
- Tummala et al., *EMBO Molecular Medicine*, **Aug 2024**, “The evolving genetic landscape of telomere biology disorder dyskeratosis congenita.” https://doi.org/10.1038/s44321-024-00118-x (tummala2024theevolvinggenetic pages 1-2, tummala2024theevolvinggenetic pages 3-5)
- Rolles et al., *Transfusion Medicine and Hemotherapy*, **Jul 2024**, “Inherited Telomere Biology Disorders: Pathophysiology, Clinical Presentation, Diagnostics, and Treatment.” https://doi.org/10.1159/000540109 (rolles2024inheritedtelomerebiology pages 8-9, rolles2024inheritedtelomerebiology pages 12-14)
- Niewisch et al., *ASH Education Program*, **Dec 2023**, “Clinical manifestations of telomere biology disorders in adults.” https://doi.org/10.1182/hematology.2023000490 (niewisch2023clinicalmanifestationsof pages 1-2, niewisch2023clinicalmanifestationsof pages 5-5)
- Tometten et al., *HemaSphere*, **Apr 2023**, adult flow-FISH screening cohort. https://doi.org/10.1097/hs9.0000000000000874 (tometten2023identificationofadult pages 1-2, tometten2023identificationofadult pages 3-4)
- Vittal et al., *Hepatology*, **May 2023**, liver disease progression. https://doi.org/10.1097/hep.0000000000000461 (vittal2023progressionofliver pages 1-2)
- Koldej et al., *Frontiers in Pediatrics*, **Aug 2023**, pediatric natural history cohort. https://doi.org/10.3389/fped.2023.1182476 (koldej2023dyskeratosiscongenitanatural pages 1-2)


References

1. (niewisch2023clinicalmanifestationsof pages 1-2): Marena R. Niewisch, Fabian Beier, and Sharon A. Savage. Clinical manifestations of telomere biology disorders in adults. Hematology. American Society of Hematology. Education Program, 2023 1:563-572, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000490, doi:10.1182/hematology.2023000490. This article has 43 citations.

2. (rolles2024inheritedtelomerebiology pages 8-9): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 21 citations and is from a peer-reviewed journal.

3. (mazurek2023dyskeratosiscongenitaas pages 4-5): Maciej Mazurek, Joanna Madzio, and Wojciech Młynarski. Dyskeratosis congenita as a multifaceted bone marrow disorder. Acta Haematologica Polonica, Oct 2023. URL: https://doi.org/10.5603/ahp.95640, doi:10.5603/ahp.95640. This article has 4 citations.

4. (koldej2023dyskeratosiscongenitanatural pages 1-2): Rachel Koldej, S. Gadalla, Navarro Uria-O ﬁ cialdegui, M. L. U. FI. cialdegui, S. Navarro, L. Murillo-Sanjuán, C. Rodríguez-Vigil, M. I. Benitez-Carbante, C. Blazquez-Goñi, J. A. Salinas, and C. Díaz-de-Heredia. Dyskeratosis congenita: natural history of the disease through the study of a cohort of patients diagnosed in childhood. Frontiers in Pediatrics, Aug 2023. URL: https://doi.org/10.3389/fped.2023.1182476, doi:10.3389/fped.2023.1182476. This article has 8 citations.

5. (revy2023geneticsofhuman pages 5-8): Patrick Revy, Caroline Kannengiesser, and Alison A. Bertuch. Genetics of human telomere biology disorders. Nature Reviews Genetics, 24:86-108, Sep 2023. URL: https://doi.org/10.1038/s41576-022-00527-z, doi:10.1038/s41576-022-00527-z. This article has 251 citations and is from a domain leading peer-reviewed journal.

6. (mazurek2023dyskeratosiscongenitaas pages 1-2): Maciej Mazurek, Joanna Madzio, and Wojciech Młynarski. Dyskeratosis congenita as a multifaceted bone marrow disorder. Acta Haematologica Polonica, Oct 2023. URL: https://doi.org/10.5603/ahp.95640, doi:10.5603/ahp.95640. This article has 4 citations.

7. (tummala2024theevolvinggenetic pages 1-2): Hemanth Tummala, Amanda J Walne, Mohsin Badat, Manthan Patel, Abigail M Walne, Jenna Alnajar, Chi Ching Chow, Ibtehal Albursan, Jennifer M Frost, David Ballard, Sally Killick, Peter Szitányi, Anne M Kelly, Manoj Raghavan, Corrina Powell, Reinier Raymakers, Tony Todd, Elpis Mantadakis, Sophia Polychronopoulou, Nikolas Pontikos, Tianyi Liao, Pradeep Madapura, Upal Hossain, Tom Vulliamy, and Inderjeet Dokal. The evolving genetic landscape of telomere biology disorder dyskeratosis congenita. EMBO Molecular Medicine, 16:2560-2582, Aug 2024. URL: https://doi.org/10.1038/s44321-024-00118-x, doi:10.1038/s44321-024-00118-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

8. (tummala2024theevolvinggenetic pages 3-5): Hemanth Tummala, Amanda J Walne, Mohsin Badat, Manthan Patel, Abigail M Walne, Jenna Alnajar, Chi Ching Chow, Ibtehal Albursan, Jennifer M Frost, David Ballard, Sally Killick, Peter Szitányi, Anne M Kelly, Manoj Raghavan, Corrina Powell, Reinier Raymakers, Tony Todd, Elpis Mantadakis, Sophia Polychronopoulou, Nikolas Pontikos, Tianyi Liao, Pradeep Madapura, Upal Hossain, Tom Vulliamy, and Inderjeet Dokal. The evolving genetic landscape of telomere biology disorder dyskeratosis congenita. EMBO Molecular Medicine, 16:2560-2582, Aug 2024. URL: https://doi.org/10.1038/s44321-024-00118-x, doi:10.1038/s44321-024-00118-x. This article has 34 citations and is from a highest quality peer-reviewed journal.

9. (ayas2026dyskeratosiscongenita pages 1-4): Mouhab Ayas and Syed Osman Ahmed. Dyskeratosis congenita. Textbook of Bone Marrow Failure, pages 267-280, Jan 2026. URL: https://doi.org/10.1007/978-3-032-02386-5\_18, doi:10.1007/978-3-032-02386-5\_18. This article has 8 citations.

10. (wang2021pulmonaryfibrosisin pages 1-2): Ping Wang and Zuojun Xu. Pulmonary fibrosis in dyskeratosis congenita: a case report with a prisma-compliant systematic review. BMC Pulmonary Medicine, Sep 2021. URL: https://doi.org/10.1186/s12890-021-01645-w, doi:10.1186/s12890-021-01645-w. This article has 19 citations and is from a peer-reviewed journal.

11. (vittal2023progressionofliver pages 1-2): Anusha Vittal, Marena R. Niewisch, Sonia Bhala, Pujitha Kudaravalli, Farial Rahman, Julian Hercun, David E. Kleiner, Sharon A. Savage, Christopher Koh, Theo Heller, and Neelam Giri. Progression of liver disease and portal hypertension in dyskeratosis congenita and related telomere biology disorders. Hepatology, 78:1777-1787, May 2023. URL: https://doi.org/10.1097/hep.0000000000000461, doi:10.1097/hep.0000000000000461. This article has 18 citations and is from a highest quality peer-reviewed journal.

12. (franke2025diagnosisandmanagement pages 7-10): Madeline Franke, Alejandro Ferrer, and Mrinal M. Patnaik. Diagnosis and management of adult telomere biology disorders. Haematologica, 111:797-812, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287739, doi:10.3324/haematol.2025.287739. This article has 2 citations.

13. (tometten2023identificationofadult pages 1-2): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 25 citations and is from a peer-reviewed journal.

14. (tometten2023identificationofadult pages 6-7): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 25 citations and is from a peer-reviewed journal.

15. (tometten2023identificationofadult pages 3-4): Mareike Tometten, Martin Kirschner, Robert Meyer, Matthias Begemann, Insa Halfmeyer, Margherita Vieri, Kim Kricheldorf, Angela Maurer, Uwe Platzbecker, Markus Radsak, Philippe Schafhausen, Selim Corbacioglu, Britta Höchsmann, C. Matthias Wilk, Claas Hinze, Jörg Chromik, Michael Heuser, Michael Kreuter, Steffen Koschmieder, Jens Peter Panse, Susanne Isfort, Ingo Kurth, Tim Henrik Brümmendorf, and Fabian Beier. Identification of adult patients with classical dyskeratosis congenita or cryptic telomere biology disorder by telomere length screening using age-modified criteria. HemaSphere, Apr 2023. URL: https://doi.org/10.1097/hs9.0000000000000874, doi:10.1097/hs9.0000000000000874. This article has 25 citations and is from a peer-reviewed journal.

16. (niewisch2023clinicalmanifestationsof pages 5-5): Marena R. Niewisch, Fabian Beier, and Sharon A. Savage. Clinical manifestations of telomere biology disorders in adults. Hematology. American Society of Hematology. Education Program, 2023 1:563-572, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000490, doi:10.1182/hematology.2023000490. This article has 43 citations.

17. (rolles2024inheritedtelomerebiology pages 12-14): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 21 citations and is from a peer-reviewed journal.

18. (ayas2026dyskeratosiscongenita pages 9-12): Mouhab Ayas and Syed Osman Ahmed. Dyskeratosis congenita. Textbook of Bone Marrow Failure, pages 267-280, Jan 2026. URL: https://doi.org/10.1007/978-3-032-02386-5\_18, doi:10.1007/978-3-032-02386-5\_18. This article has 8 citations.

19. (rolles2024inheritedtelomerebiology pages 10-12): Benjamin Rolles, Mareike Tometten, Robert Meyer, Martin Kirschner, Fabian Beier, and Tim H. Brümmendorf. Inherited telomere biology disorders: pathophysiology, clinical presentation, diagnostics, and treatment. Transfusion Medicine and Hemotherapy, 51:292-309, Jul 2024. URL: https://doi.org/10.1159/000540109, doi:10.1159/000540109. This article has 21 citations and is from a peer-reviewed journal.

20. (glass2026telomerebiology pages 17-18): Joshua Glass, Emma Groarke, and Neal S. Young. Telomere biology. Textbook of Bone Marrow Failure, pages 249-266, Jan 2026. URL: https://doi.org/10.1007/978-3-032-02386-5\_17, doi:10.1007/978-3-032-02386-5\_17. This article has 0 citations.

21. (koldej2023dyskeratosiscongenitanatural pages 2-3): Rachel Koldej, S. Gadalla, Navarro Uria-O ﬁ cialdegui, M. L. U. FI. cialdegui, S. Navarro, L. Murillo-Sanjuán, C. Rodríguez-Vigil, M. I. Benitez-Carbante, C. Blazquez-Goñi, J. A. Salinas, and C. Díaz-de-Heredia. Dyskeratosis congenita: natural history of the disease through the study of a cohort of patients diagnosed in childhood. Frontiers in Pediatrics, Aug 2023. URL: https://doi.org/10.3389/fped.2023.1182476, doi:10.3389/fped.2023.1182476. This article has 8 citations.

22. (glass2026telomerebiology pages 1-5): Joshua Glass, Emma Groarke, and Neal S. Young. Telomere biology. Textbook of Bone Marrow Failure, pages 249-266, Jan 2026. URL: https://doi.org/10.1007/978-3-032-02386-5\_17, doi:10.1007/978-3-032-02386-5\_17. This article has 0 citations.

23. (carlier2026hematologicalcomplicationsin pages 2-3): François M. Carlier, Thomas Planté-Bordeneuve, Antoine Froidure, Carlos Graux, Marie-Astrid van Dievoet, Coline H. M. van Moorsel, and Thijs W. Hoffman. Hematological complications in solid organ transplant recipients with telomere biology disorders: a narrative review. Frontiers in Immunology, Jan 2026. URL: https://doi.org/10.3389/fimmu.2025.1718107, doi:10.3389/fimmu.2025.1718107. This article has 4 citations and is from a peer-reviewed journal.

24. (sanzmoreno2025lossoften1 pages 1-2): Adrián Sanz-Moreno, Lore Becker, Kan Xie, Patricia da Silva-Buttkus, Nathalia R. V. Dragano, Antonio Aguilar-Pimentel, Oana V. Amarie, Julia Calzada-Wack, Markus Kraiger, Stefanie Leuchtenberger, Claudia Seisenberger, Susan Marschall, Birgit Rathkolb, Enzo Scifo, Ting Liu, Anoja Thanabalasingam, Raul Sanchez-Vazquez, Paula Martinez, Maria A. Blasco, Sharon A. Savage, Helmut Fuchs, Dan Ehninger, Valérie Gailus-Durner, and Martin Hrabê de Angelis. Loss of ten1 in mice induces telomere shortening and models human dyskeratosis congenita. Science Advances, Apr 2025. URL: https://doi.org/10.1126/sciadv.adp8093, doi:10.1126/sciadv.adp8093. This article has 4 citations and is from a highest quality peer-reviewed journal.

25. (sanzmoreno2025lossoften1 pages 3-6): Adrián Sanz-Moreno, Lore Becker, Kan Xie, Patricia da Silva-Buttkus, Nathalia R. V. Dragano, Antonio Aguilar-Pimentel, Oana V. Amarie, Julia Calzada-Wack, Markus Kraiger, Stefanie Leuchtenberger, Claudia Seisenberger, Susan Marschall, Birgit Rathkolb, Enzo Scifo, Ting Liu, Anoja Thanabalasingam, Raul Sanchez-Vazquez, Paula Martinez, Maria A. Blasco, Sharon A. Savage, Helmut Fuchs, Dan Ehninger, Valérie Gailus-Durner, and Martin Hrabê de Angelis. Loss of ten1 in mice induces telomere shortening and models human dyskeratosis congenita. Science Advances, Apr 2025. URL: https://doi.org/10.1126/sciadv.adp8093, doi:10.1126/sciadv.adp8093. This article has 4 citations and is from a highest quality peer-reviewed journal.

26. (sanzmoreno2025lossoften1 pages 2-3): Adrián Sanz-Moreno, Lore Becker, Kan Xie, Patricia da Silva-Buttkus, Nathalia R. V. Dragano, Antonio Aguilar-Pimentel, Oana V. Amarie, Julia Calzada-Wack, Markus Kraiger, Stefanie Leuchtenberger, Claudia Seisenberger, Susan Marschall, Birgit Rathkolb, Enzo Scifo, Ting Liu, Anoja Thanabalasingam, Raul Sanchez-Vazquez, Paula Martinez, Maria A. Blasco, Sharon A. Savage, Helmut Fuchs, Dan Ehninger, Valérie Gailus-Durner, and Martin Hrabê de Angelis. Loss of ten1 in mice induces telomere shortening and models human dyskeratosis congenita. Science Advances, Apr 2025. URL: https://doi.org/10.1126/sciadv.adp8093, doi:10.1126/sciadv.adp8093. This article has 4 citations and is from a highest quality peer-reviewed journal.

27. (NCT01659606 chunk 2): Suneet Agarwal. Radiation- and Alkylator-free Bone Marrow Transplantation Regimen for Patients With Dyskeratosis Congenita. Boston Children's Hospital. 2012. ClinicalTrials.gov Identifier: NCT01659606

28. (ayas2026dyskeratosiscongenita pages 4-7): Mouhab Ayas and Syed Osman Ahmed. Dyskeratosis congenita. Textbook of Bone Marrow Failure, pages 267-280, Jan 2026. URL: https://doi.org/10.1007/978-3-032-02386-5\_18, doi:10.1007/978-3-032-02386-5\_18. This article has 8 citations.

29. (NCT01441037 chunk 2):  Danazol for Genetic Bone Marrow and Lung Disorders. National Heart, Lung, and Blood Institute (NHLBI). 2011. ClinicalTrials.gov Identifier: NCT01441037

30. (NCT02162420 chunk 2):  Hematopoietic Stem Cell Transplant for Dyskeratosis Congenita or Severe Aplastic Anemia. Masonic Cancer Center, University of Minnesota. 2015. ClinicalTrials.gov Identifier: NCT02162420

31. (franke2025diagnosisandmanagement pages 15-17): Madeline Franke, Alejandro Ferrer, and Mrinal M. Patnaik. Diagnosis and management of adult telomere biology disorders. Haematologica, 111:797-812, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287739, doi:10.3324/haematol.2025.287739. This article has 2 citations.

32. (revy2023geneticsofhuman pages 27-30): Patrick Revy, Caroline Kannengiesser, and Alison A. Bertuch. Genetics of human telomere biology disorders. Nature Reviews Genetics, 24:86-108, Sep 2023. URL: https://doi.org/10.1038/s41576-022-00527-z, doi:10.1038/s41576-022-00527-z. This article has 251 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dyskeratosis_Congenita-deep-research-falcon_artifacts/artifact-00.md)