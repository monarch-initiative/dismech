---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-05T13:50:49.891074'
end_time: '2026-06-05T14:02:57.801981'
duration_seconds: 727.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peeling Skin Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peeling_Skin_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peeling Skin Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peeling Skin Syndrome** covering all of the
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
- **Disease Name:** Peeling Skin Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peeling Skin Syndrome** covering all of the
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


# Peeling Skin Syndrome (PSS) — Comprehensive Disease Characteristics Report (Mendelian)

## Target disease
**Disease name:** Peeling Skin Syndrome (PSS) (umbrella term covering acral and generalized genetic peeling disorders). (metze2026desmosomaltypeacantholysis—anew pages 10-12, velden2020mutationsinthe pages 1-2)

**Definition / overview:** PSS is characterized by superficial, often painless “spontaneous peeling of the stratum corneum without bleeding or pain.” (metze2026desmosomaltypeacantholysis—anew pages 10-12)

**Key concept (current understanding):** PSS represents a heterogeneous set of Mendelian disorders of cornification/skin fragility in which defective stratum corneum cohesion (often via corneodesmosome dysfunction or dysregulated desquamation proteolysis) causes superficial epidermal detachment/peeling. (has2018peelingskindisorders pages 1-2, komatsu2006elevatedhumantissue pages 1-2)

### Key identifiers (available from retrieved sources)
* **OMIM/MIM:**
  * Acral Peeling Skin Syndrome (APSS): **MIM 609796**. (stjernbrandt2024acralpeelingskin pages 1-2)
  * Peeling skin disease / inflammatory generalized PSS (often called PSS type B / PSS1): **MIM 270300**. (metze2026desmosomaltypeacantholysis—anew pages 10-12)
* **MONDO / ICD-10 / ICD-11 / MeSH:** Not available in the retrieved evidence set; should be added via dedicated ontology lookup (e.g., MONDO/Orphanet/MeSH portals).

### Synonyms and alternative names
* **Acral peeling skin syndrome (APSS)** (localized/acral form). (stjernbrandt2024acralpeelingskin pages 1-2)
* **Generalized peeling skin syndrome (GPSS)**; subdivided into non-inflammatory (type A) and inflammatory (type B). (kawakami2014acaseof pages 1-2, velden2020mutationsinthe pages 1-2)
* **Peeling skin disease (PSD)** is frequently used for the inflammatory generalized CDSN-related form. (velden2020mutationsinthe pages 1-2, oji2010lossofcorneodesmosin pages 6-7)
* **PLACK syndrome** (CAST-related: *Peeling skin, Leukonychia, Acral punctate keratoses, Cheilitis, Knuckle pads*). (vidya2023placksyndromeassociated pages 1-3, lin2015lossoffunctionmutationsin pages 1-2)

### Evidence source type
The information in this report is derived primarily from **aggregated disease-level resources (reviews/commentaries)** and **primary human case reports/series** with supporting **in vitro and animal model** data for specific genes (notably CDSN and FLG2). (has2018peelingskindisorders pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6, oji2010lossofcorneodesmosin pages 6-7)

---

## 1. Disease information (classification)

### Clinical classification used in the literature
A commonly used clinical framework divides PSS into:
1) **Acral PSS (APSS)** — predominant involvement of hands/feet. (kawakami2014acaseof pages 1-2, stjernbrandt2024acralpeelingskin pages 1-2)
2) **Generalized PSS** — widespread peeling/scaling. (kawakami2014acaseof pages 1-2, velden2020mutationsinthe pages 1-2)

Generalized PSS is further divided into:
* **Type A (non-inflammatory)** — associated with **CHST8** in some families. (kawakami2014acaseof pages 1-2, cabral2012wholeexomesequencingin pages 4-5)
* **Type B (inflammatory)** — associated with **CDSN** (corneodesmosin) and often includes pruritus and atopic features. (velden2020mutationsinthe pages 1-2, oji2010lossofcorneodesmosin pages 6-7)

A complementary gene/pathway framing is that peeling skin disorders arise from (i) **structural corneodesmosome/cornified envelope defects**, (ii) **crosslinking enzyme defects (transglutaminases)**, or (iii) **protease–inhibitor imbalance** leading to premature corneodesmosome cleavage and over-desquamation. (has2018peelingskindisorders pages 1-2, komatsu2006elevatedhumantissue pages 1-2)

---

## 2. Etiology

### Primary causal factors (genetic)
PSS is predominantly **genetic (Mendelian)**, most often **autosomal recessive** across major subtypes. (velden2020mutationsinthe pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6)

Key genes and gene→phenotype links supported by primary literature in this evidence set:

* **TGM5** (transglutaminase 5): causes **APSS** (autosomal recessive). (stjernbrandt2024acralpeelingskin pages 1-2, velden2020mutationsinthe pages 1-2)
  * Examples of pathogenic variants reported in recent APSS series include **c.337G>T p.(Gly113Cys)** and **c.763T>C p.(Trp255Arg)**. (stjernbrandt2024acralpeelingskin pages 1-2)

* **CSTA** (cystatin A; protease inhibitor in cornified envelope): causes APSS / exfoliative ichthyosis overlap; typically autosomal recessive loss-of-function. (krunic2013acralpeelingskin pages 1-2, lin2015lossoffunctionmutationsin pages 1-2)
  * Example: **c.64A>T p.Lys22X** segregating in a large consanguineous pedigree. (krunic2013acralpeelingskin pages 1-2)

* **CDSN** (corneodesmosin): causes inflammatory generalized PSS / peeling skin disease (often PSS1/PSS-B/PSD), typically autosomal recessive biallelic LOF; **monoallelic CDSN** variants can cause autosomal dominant hypotrichosis simplex of the scalp (distinct phenotype). (velden2020mutationsinthe pages 1-2)

* **CHST8**: implicated in **type A (non-inflammatory) generalized PSS** in some families. (kawakami2014acaseof pages 1-2, cabral2012wholeexomesequencingin pages 4-5)

* **FLG2** (filaggrin-2): biallelic loss-of-function causes **generalized ichthyotic peeling skin syndrome** with improvement by age in reported siblings. (bolling2018generalizedichthyoticpeeling pages 1-6)

* **CAST** (calpastatin; endogenous protease inhibitor): biallelic LOF causes **PLACK syndrome**, a generalized peeling phenotype with leukonychia, acral punctate keratoses, cheilitis, and knuckle pads. (lin2015lossoffunctionmutationsin pages 1-2, vidya2023placksyndromeassociated pages 1-3)

### Risk factors (genetic and environmental)
Because PSS is Mendelian, the dominant risk factor is **having biallelic pathogenic variants** in the relevant causal gene (subtype-dependent). (velden2020mutationsinthe pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6)

**Environmental exacerbating factors** (disease modifiers) are well described for APSS and some generalized forms:
* **Humidity, heat, moisture/water exposure, friction/trauma, perspiration/hyperhidrosis** commonly worsen acral peeling. (gierach2023acralpeelingskin pages 1-3, krunic2013acralpeelingskin pages 1-2, stjernbrandt2024acralpeelingskin pages 1-2)
* For FLG2-related generalized peeling, **warm humid environments** and **minor trauma** can exacerbate peeling. (bolling2018generalizedichthyoticpeeling pages 1-6)

### Protective factors / gene–environment interactions
No specific **protective factors** or formal **gene–environment interaction models** were identified in the retrieved evidence set.

---

## 3. Phenotypes (clinical spectrum) with ontology suggestions

### Core phenotype across PSS
* **Superficial skin peeling/desquamation** (stratum corneum detachment) that is often painless and non-bleeding. (metze2026desmosomaltypeacantholysis—anew pages 10-12)
  * Suggested HPO: **HP:0001053 (Abnormality of the skin)**; **HP:0000964 (Erythema)** when present; **HP:0000982 (Skin erosion)** in denuded areas.

### Acral peeling skin syndrome (APSS; often TGM5 or CSTA)
**Typical features**:
* Painless peeling affecting **hands and feet**; may include erythema, itching, erosions, and sometimes blisters. (stjernbrandt2024acralpeelingskin pages 1-2)
* Onset often from **birth**, but later onset can occur. (stjernbrandt2024acralpeelingskin pages 1-2)
* **Exacerbations** with humidity, friction, and hyperhidrosis are common. (stjernbrandt2024acralpeelingskin pages 1-2)
* CSTA pedigree: lifelong hand/foot peeling with **erythema, lichenification, maceration, pruritus**, and strong moisture/heat/friction sensitivity. (krunic2013acralpeelingskin pages 1-2)

Suggested HPO terms (examples):
* **HP:0030050** (Skin peeling) [term commonly used in HPO; verify exact ID in HPO browser]
* **HP:0000972 (Palmoplantar hyperkeratosis)** (if punctate keratoses/keratoderma)
* **HP:0000989 (Pruritus)**
* **HP:0012471 (Blistering of the skin)** (when blisters occur)

### Generalized non-inflammatory PSS (Type A; CHST8)
**Reported phenotype characteristics** in the Cabral et al. CHST8 study include an otherwise asymptomatic generalized peeling phenotype with **occasional pruritus** and without vesicles/pustules or mucous membrane/nail involvement; histology shows mild hyperkeratosis and splitting around the SG/SC interface. (cabral2012wholeexomesequencingin pages 4-5)

Suggested HPO:
* Skin peeling; pruritus (as above)
* **HP:0000958 (Dry skin)**

### Inflammatory generalized PSS / peeling skin disease (Type B / PSS1; CDSN)
**Hallmark features**:
* Onset at birth with **ichthyosiform erythroderma** and lifelong patchy superficial peeling, often with **severe pruritus**. (metze2026desmosomaltypeacantholysis—anew pages 10-12, valentin2021developmentofa pages 1-5)
* Systemic/atopic complications reported include **urticaria, angioedema, food allergies, asthma**, and lab findings of **elevated IgE and eosinophilia**. (metze2026desmosomaltypeacantholysis—anew pages 10-12)
* PSS1 causes major quality-of-life burden including impaired sleep and recurrent superinfections. (valentin2021developmentofa pages 1-5)

Quantitative examples from the evidence set:
* One CDSN-related patient had **IgE 2222 kU/L** (markedly elevated). (velden2020mutationsinthe pages 1-2)
* Corneodesmosome ultrastructure in one CDSN missense case showed reduced length and density vs control (length **386.2±149.5 nm vs 446.3±185.8 nm**; density **0.860±0.233 μm−1 vs 1.309±0.413 μm−1**, p<0.05). (kawakami2014acaseof pages 4-5)

Suggested HPO:
* **HP:0001041 (Ichthyosis)** / ichthyosiform erythroderma
* **HP:0000989 (Pruritus)**
* **HP:0002721 (Eosinophilia)**
* **HP:0003212 (Elevated circulating IgE)**
* **HP:0001022 (Food allergy)** [verify exact ID]

### FLG2-related generalized ichthyotic peeling skin syndrome
Phenotype from affected siblings:
* **Erythroderma at birth**, persistent dry skin and superficial peeling, worsened by **minor trauma** and **warm humid environments**; denuded areas heal with **hyperpigmentation without scarring**; hair/nails/mucosa unaffected; **clinical improvement with age**. (bolling2018generalizedichthyoticpeeling pages 1-6)

Suggested HPO:
* Ichthyosis/erythroderma; skin peeling; post-inflammatory hyperpigmentation (ontology mapping may vary).

### PLACK syndrome (CAST)
Core phenotype:
* “Generalised peeling, leukonychia, acral punctate keratoses, cheilitis, knuckle pads.” (vidya2023placksyndromeassociated pages 1-3)
* Peeling may occur spontaneously or after trauma and may occur with or without bullae. (vidya2023placksyndromeassociated pages 1-3)

Suggested HPO:
* **Leukonychia** (HP term exists)
* **Cheilitis** (HP term exists)
* **Knuckle pads** (HP term exists)
* **Punctate palmoplantar keratoderma** (HP term exists)

---

## 4. Genetic / molecular information

### Causal genes (supported in this evidence set)
* **TGM5** (APSS) (stjernbrandt2024acralpeelingskin pages 1-2)
* **CSTA** (APSS / exfoliative ichthyosis overlap) (krunic2013acralpeelingskin pages 1-2)
* **CHST8** (generalized PSS-A) (cabral2012wholeexomesequencingin pages 4-5)
* **CDSN** (PSS-B/PSS1/PSD) (velden2020mutationsinthe pages 1-2, oji2010lossofcorneodesmosin pages 6-7)
* **FLG2** (generalized ichthyotic peeling) (bolling2018generalizedichthyoticpeeling pages 1-6)
* **CAST** (PLACK) (lin2015lossoffunctionmutationsin pages 1-2)

### Variant classes and functional consequences
Across PSS genes, disease is frequently caused by **loss-of-function** variants (nonsense, frameshift, splice, deletions) consistent with reduced/absent protein affecting stratum corneum cohesion or protease regulation. (velden2020mutationsinthe pages 1-2, lin2015lossoffunctionmutationsin pages 1-2, krunic2013acralpeelingskin pages 1-2)

Examples:
* **CSTA p.Lys22X** (nonsense) in APSS pedigree. (krunic2013acralpeelingskin pages 1-2)
* **FLG2 p.Ser211\*** (nonsense) in generalized ichthyotic peeling. (bolling2018generalizedichthyoticpeeling pages 1-6)
* **CDSN LOF** (nonsense/deletions) in PSS1; CDSN protein absence contributes to subcorneal splitting and barrier failure. (valentin2021developmentofa pages 1-5, oji2010lossofcorneodesmosin pages 6-7)

### Modifier genes / epigenetics / chromosomal abnormalities
No robust modifier genes, epigenetic signatures, or chromosomal abnormalities were identified in the retrieved evidence set beyond copy-number/deletion events encompassing CDSN in some cases (reviewed). (pan2022atopicdermatitislikegenodermatosis pages 33-33)

---

## 5. Environmental information
PSS is not infectious; environmental factors are primarily **exacerbating triggers**:
* **Moisture/water exposure, humidity, heat, friction/trauma, sweating/hyperhidrosis** worsen APSS and some generalized forms. (krunic2013acralpeelingskin pages 1-2, stjernbrandt2024acralpeelingskin pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6)

---

## 6. Mechanism / pathophysiology

### Mechanistic causal chain (high-level)
**Gene LOF → impaired stratum corneum cohesion and/or dysregulated desquamation proteolysis → superficial cleavage at/within the stratum corneum → recurrent peeling/erosions → barrier dysfunction and (in inflammatory forms) itch/atopy/infection risk.** (has2018peelingskindisorders pages 1-2, oji2010lossofcorneodesmosin pages 6-7, komatsu2006elevatedhumantissue pages 1-2)

### Corneodesmosome and barrier defect axis (CDSN; inflammatory generalized PSS)
* CDSN encodes **corneodesmosin**, a key adhesion component in corneodesmosomes; loss causes severe barrier breakdown. (oji2010lossofcorneodesmosin pages 6-7)
* Functional/model evidence: murine **Cdsn knockout** results in early postnatal death from barrier breakdown and ~**10-fold increase in transepidermal water loss**, supporting CDSN’s essential barrier role. (oji2010lossofcorneodesmosin pages 6-7)
* Human reconstructed epidermis from patient keratinocytes shows absent CDSN staining and increased permeability (e.g., increased testosterone permeation) consistent with barrier defect. (oji2010lossofcorneodesmosin pages 6-7)

Suggested GO biological process terms:
* **GO:0030216 (Keratinocyte differentiation)**
* **GO:0061436 (Establishment of skin barrier)** (or related epidermal barrier GO term)
* **GO:0007155 (Cell adhesion)**

Suggested CL (cell types):
* **Keratinocyte** (CL:0000312)

Suggested UBERON (anatomy):
* **Epidermis**, **stratum corneum**, **stratum granulosum**.

### Protease–inhibitor imbalance / over-desquamation axis
* In PSS-type B patients, **kallikrein (hK) levels** and multiple serine protease activities were reported as elevated in stratum corneum and serum, supporting an “over-desquamation” mechanism via proteolytic cleavage of adhesion proteins. (komatsu2006elevatedhumantissue pages 1-2)
* CAST (calpastatin) and CSTA (cystatin A) are protease inhibitors; CAST LOF (PLACK) and CSTA LOF (APSS/exfoliative ichthyosis overlap) implicate dysregulated proteolysis and impaired adhesion. (lin2015lossoffunctionmutationsin pages 1-2, krunic2013acralpeelingskin pages 1-2)

### Cornified envelope / keratin compaction axis (FLG2)
* FLG2 deficiency leads to abnormal cornification: patient tissue shows parakeratosis, altered keratin/corneodesmosome-associated proteins (reduced corneodesmosin; altered desmoglein/desmocollin), and abnormal stratum corneum ultrastructure; an in vitro FLG2 knockdown model reproduces parakeratosis/loricrin downregulation/abnormal SC vesicles. (bolling2018generalizedichthyoticpeeling pages 1-6)

---

## 7. Anatomical structures affected
* Primary: **skin epidermis**, especially **stratum corneum** (and SG/SC interface depending on subtype). (gierach2023acralpeelingskin pages 1-3, bolling2018generalizedichthyoticpeeling pages 1-6)
* APSS: predominant involvement of **hands and feet** (acral skin; palms/soles and sometimes dorsal aspects). (stjernbrandt2024acralpeelingskin pages 1-2)
* CDSN-related inflammatory generalized PSS: generalized involvement; also hair follicle biology can be affected (CDSN expression in hair structures and AD hypotrichosis phenotype with monoallelic variants). (velden2020mutationsinthe pages 1-2, metze2026desmosomaltypeacantholysis—anew pages 10-12)

---

## 8. Temporal development
* APSS: often evident **from birth** but can present later; course is typically chronic with flares triggered by friction/humidity/sweating. (stjernbrandt2024acralpeelingskin pages 1-2)
* CDSN-related inflammatory generalized PSS: **onset at birth** with lifelong disease. (valentin2021developmentofa pages 1-5, metze2026desmosomaltypeacantholysis—anew pages 10-12)
* FLG2-related generalized peeling: **congenital onset** with improvement by age in a reported family. (bolling2018generalizedichthyoticpeeling pages 1-6)

---

## 9. Inheritance and population

### Inheritance patterns
Predominantly **autosomal recessive** across PSS subtypes (TGM5, CSTA, CDSN (biallelic), CHST8, FLG2, CAST). (velden2020mutationsinthe pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6, lin2015lossoffunctionmutationsin pages 1-2)

Notable exception:
* **Monoallelic CDSN variants** can cause **autosomal dominant hypotrichosis simplex of the scalp**, distinct from the recessive peeling phenotype. (velden2020mutationsinthe pages 1-2)

### Epidemiology / prevalence
Robust population prevalence is generally not provided in primary PSS reports within this evidence set. A specific prevalence estimate is reported for PLACK syndrome:
* **PLACK syndrome prevalence stated as 1:10,00,000** (as written in the case report). (vidya2023placksyndromeassociated pages 1-3)

### Population genetics / founder effects
* A recurrent APSS variant **TGM5 c.763T>C p.(Trp255Arg)** is described as a European founder variant, with reported gnomAD counts **78 occurrences overall and 49 in the Swedish ancestry group** (as reported by the authors). (stjernbrandt2024acralpeelingskin pages 1-2)

---

## 10. Diagnostics

### Clinical presentation and differential diagnosis
* APSS can be difficult to distinguish clinically from **localized epidermolysis bullosa simplex (EBS)**, and can also resemble keratosis palmaris et plantaris and allergic contact dermatitis. (stjernbrandt2024acralpeelingskin pages 1-2, gierach2023acralpeelingskin pages 1-3)
* Inflammatory generalized CDSN-related PSS can overlap with eczema/atopic presentations and has been confused with **Netherton syndrome**. (komatsu2006elevatedhumantissue pages 1-2, valentin2021developmentofa pages 1-5)

### Histopathology / ultrastructure
* APSS (reviewed): cleavage between **stratum corneum and stratum granulosum** is typical. (gierach2023acralpeelingskin pages 1-3)
* FLG2-related generalized peeling: separation in the **lower stratum corneum** with parakeratosis and ultrastructural corneocyte abnormalities. (bolling2018generalizedichthyoticpeeling pages 1-6)
* CDSN-related inflammatory generalized PSS: reduced corneodesmosome length/density has been quantified in at least one case; abnormal corneodesmosome biology is central. (kawakami2014acaseof pages 4-5)

### Genetic testing strategy (practical approach)
* Because APSS may mimic EBS, authors recommend gene testing panels that include **TGM5 and CSTA** and localized EBS genes, with sequence + copy-number analysis. (stjernbrandt2024acralpeelingskin pages 2-2, stjernbrandt2024acralpeelingskin pages 1-2)
* For generalized/inflammatory phenotypes, testing should include **CDSN** and should consider **large deletions/CNVs** (CDSN deletions have been reported). (pan2022atopicdermatitislikegenodermatosis pages 33-33)
* Whole-exome sequencing has been useful in genetically heterogeneous pedigrees (e.g., identifying CSTA p.Lys22X when linkage was uninformative). (krunic2013acralpeelingskin pages 1-2)

---

## 11. Outcome / prognosis
* APSS is generally described as relatively **mild** with recurrent peeling that heals without scarring and without systemic involvement in many cases, though symptoms may be burdensome and recurrent. (gierach2023acralpeelingskin pages 1-3, stjernbrandt2024acralpeelingskin pages 1-2)
* CDSN-related PSS1 is described as **severe**, with pronounced pruritus, sleep impairment, recurrent infections, and major quality-of-life impact; current therapies are unsatisfactory. (valentin2021developmentofa pages 1-5)
* FLG2-related generalized peeling in one family showed **marked improvement with age** and no scarring, although hyperpigmentation could follow denudation. (bolling2018generalizedichthyoticpeeling pages 1-6)

---

## 12. Treatment (current applications and real-world implementations)

### Current standard management (symptomatic/supportive)
* **Friction reduction / avoidance of triggers** (humidity, sweating, friction) and **skin softening/emollient-based care** are common practical measures. (stjernbrandt2024acralpeelingskin pages 1-2)
* In severe CDSN-related PSS1, symptomatic measures such as **balneotherapy and bland topical ointments** are used but are often inadequate. (valentin2021developmentofa pages 1-5)

Suggested MAXO terms (examples):
* **Topical emollient therapy** (MAXO term for emollient/moisturizer treatment)
* **Avoidance of triggering environmental exposure**

### Recent (2023–2024) treatment development: botulinum toxin for APSS
A 2024 report describes symptomatic benefit from **botulinum toxin A injections** in APSS, motivated by reduction of hyperhidrosis (a common exacerbating factor). (stjernbrandt2024acralpeelingskin pages 1-2)

Suggested MAXO:
* **Botulinum toxin therapy** (for hyperhidrosis-associated exacerbation)

### Pathogenesis-based / experimental therapies (preclinical)
A 2021 British Journal of Dermatology study developed a **protein-replacement approach** for CDSN-deficient PSS1 using recombinant CDSN in targeted liposomes, restoring CDSN staining and improving barrier function in CDSN-deficient epidermal equivalents in vitro. (valentin2021developmentofa pages 9-12, valentin2021developmentofa pages 1-5)

Suggested MAXO:
* **Protein replacement therapy**

### Topical calcipotriol (limited evidence)
A review of eczema-like genodermatoses notes a reported case of PSS treated successfully with **topical calcipotriol** (details not present in retrieved snippet). (pan2022atopicdermatitislikegenodermatosis pages 33-33)

### Clinical trials
No PSS-specific interventional trials were identified in the ClinicalTrials.gov search results retrieved during this run.

---

## 13. Prevention
Because PSS is genetic, **primary prevention** largely involves **genetic counseling**, carrier testing in affected families, and reproductive options when desired.

**Tertiary prevention** includes trigger avoidance (humidity, friction, sweating) and measures to reduce barrier breakdown/infections in severe forms. (valentin2021developmentofa pages 1-5, stjernbrandt2024acralpeelingskin pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary PSS analogs were identified in the retrieved evidence set.

---

## 15. Model organisms and experimental systems

### CDSN (in vivo and human skin models)
* Murine **Cdsn knockout** causes lethal barrier breakdown and dramatic TEWL increase, supporting causality and providing a strong in vivo model for CDSN-related PSS. (oji2010lossofcorneodesmosin pages 6-7)
* Patient-derived **reconstructed human epidermis** lacking CDSN shows defective barrier function and altered differentiation. (oji2010lossofcorneodesmosin pages 6-7)

### FLG2 (in vitro models)
* **FLG2 knockdown** models reproduce parakeratosis and other disease-relevant features, supporting a mechanistic link between FLG2 deficiency and impaired cornification/adhesion. (bolling2018generalizedichthyoticpeeling pages 1-6)

### CAST (human tissue + in vitro)
* CAST LOF shows reduced calpastatin staining in patient tissue and CAST knockdown impairs keratinocyte adhesion in vitro. (lin2015lossoffunctionmutationsin pages 1-2)

---

## Recent developments and latest research (prioritizing 2023–2024)

1) **Improved APSS clinical characterization and genetics in recent clinical reports (2023–2024):** 2023 and 2024 reports emphasize APSS triggers (humidity/friction/hyperhidrosis), genetic heterogeneity (TGM5 vs CSTA), and diagnostic confusion with localized EBS—supporting broader adoption of gene testing in recurrent acral blistering/peeling. (gierach2023acralpeelingskin pages 1-3, stjernbrandt2024acralpeelingskin pages 1-2)

2) **Therapeutic repurposing at the symptom-modifier level:** botulinum toxin A is reported as potentially beneficial for APSS by reducing sweating/hyperhidrosis-driven exacerbations. (stjernbrandt2024acralpeelingskin pages 1-2)

3) **Expansion of CAST-related PLACK phenotypes with new variants (2023):** a 2023 case report identifies a novel homozygous CAST frameshift leading to truncation and reiterates the PLACK phenotype (peeling + leukonychia + keratoses + cheilitis + knuckle pads), contributing to genotype expansion. (vidya2023placksyndromeassociated pages 1-3)

---

## Subtype crosswalk (summary table)
| Clinical entity/subtype | Key features | Causal gene(s) | Inheritance | Example variant(s) mentioned in evidence | Key triggers/exacerbating factors | Key references (PMID/DOI) |
|---|---|---|---|---|---|---|
| Acral peeling skin syndrome (APSS) | Painless superficial peeling/exfoliation mainly of hands and feet; may include erythema, itching, erosions, flaccid blisters; histologic cleavage between stratum corneum and granular layer; can mimic localized epidermolysis bullosa simplex (gierach2023acralpeelingskin pages 1-3, stjernbrandt2024acralpeelingskin pages 1-2) | **TGM5** | Autosomal recessive (stjernbrandt2024acralpeelingskin pages 1-2, velden2020mutationsinthe pages 1-2) | p.Gly113Cys / c.337G>T; p.Trp255Arg / c.763T>C; c.2T>C p.M1T; c.1037G>A; c.684+1G>A (stjernbrandt2024acralpeelingskin pages 2-2, stjernbrandt2024acralpeelingskin pages 1-2, krunic2013acralpeelingskin pages 1-2) | Humidity, friction/trauma, perspiration/hyperhidrosis, heat, water/moisture (gierach2023acralpeelingskin pages 1-3, stjernbrandt2024acralpeelingskin pages 1-2, krunic2013acralpeelingskin pages 1-2) | DOI: 10.5114/dr.2023.131389; 10.2340/actadv.v104.24305; 10.1159/000354572; 10.1111/1346-8138.17422 |
| Acral peeling skin syndrome due to **CSTA** | Lifelong acral peeling; some reports note overlap with exfoliative ichthyosis/fine scaling; skin fragility related to impaired adhesion/protease inhibition (stjernbrandt2024acralpeelingskin pages 1-2, krunic2013acralpeelingskin pages 1-2) | **CSTA** (cystatin A) | Autosomal recessive (consanguineous pedigree; homozygous LOF) (krunic2013acralpeelingskin pages 1-2) | p.Lys22Ter / p.Lys22X nonsense mutation (krunic2013acralpeelingskin pages 1-2) | Heat, friction, perspiration, excessive moisture, exposure to water (krunic2013acralpeelingskin pages 1-2) | DOI: 10.1111/pde.12092 |
| Generalized PSS type A / non-inflammatory generalized PSS | Generalized superficial peeling/scaling beginning in early childhood; non-inflammatory generalized form (gierach2023acralpeelingskin pages 1-3, kawakami2014acaseof pages 1-2, velden2020mutationsinthe pages 1-2) | **CHST8** | Autosomal recessive (kawakami2014acaseof pages 1-2, velden2020mutationsinthe pages 1-2) | R77W was historically proposed, but causality has been questioned in later work; no firmly validated pathogenic example variant was provided in gathered evidence (kawakami2014acaseof pages 1-2) | Mechanical friction reported to exacerbate generalized non-inflammatory PSS in a quiz/case context (bolling2018generalizedichthyoticpeeling pages 1-6) | DOI: 10.1016/j.ygeno.2012.01.005 |
| Generalized inflammatory peeling skin syndrome / PSS type B / PSS1 / peeling skin disease (PSD) | Congenital ichthyosiform erythroderma with lifelong patchy/superficial peeling, severe pruritus, burning red denuded patches with collarette; may show urticaria, angioedema, food allergies, asthma, elevated IgE/eosinophilia; due to corneodesmosomal dysfunction/barrier defect (metze2026desmosomaltypeacantholysis—anew pages 10-12, kawakami2014acaseof pages 3-4, velden2020mutationsinthe pages 1-2, kawakami2014acaseof pages 4-5) | **CDSN** (corneodesmosin) | Autosomal recessive for peeling skin disease; monoallelic CDSN variants instead can cause autosomal dominant hypotrichosis simplex of the scalp (velden2020mutationsinthe pages 1-2) | c.598C>T p.Gln200*; c.164_167dup p.Thr57Profs*6; c.1358G>A missense (velden2020mutationsinthe pages 1-2, kawakami2014acaseof pages 1-2) | Summer worsening reported; inflammatory/barrier-driven phenotype rather than classic friction-limited acral disease (kawakami2014acaseof pages 1-2, kawakami2014acaseof pages 4-5) | DOI: 10.1016/j.ajhg.2010.07.005; 10.1038/jid.2010.363; 10.1111/1346-8138.15136; 10.1159/000368823 |
| Generalized ichthyotic peeling skin syndrome due to **FLG2** | Recessive generalized skin-fragility/peeling with ichthyotic features; cleavage in lower stratum corneum, parakeratosis, reduced keratin 2/corneodesmosin/desmocollin-1/desmoglein-1, abnormal keratin compaction (bolling2018generalizedichthyoticpeeling pages 1-6, has2018peelingskindisorders pages 1-2) | **FLG2** | Recessive / biallelic loss-of-function (has2018peelingskindisorders pages 1-2, bolling2018generalizedichthyoticpeeling pages 1-6) | c.632C>G, p.Ser211*; p.Tyr355* also cited in commentary evidence (bolling2018generalizedichthyoticpeeling pages 1-6, has2018peelingskindisorders pages 1-2) | Not specifically stated in gathered evidence | DOI: 10.1016/j.jid.2018.01.038 |
| PLACK syndrome (related PSS phenotype) | Generalized peeling, leukonychia, acral punctate keratoses, cheilitis, knuckle pads; may also show xerosis, palmoplantar keratoderma, hyperkeratotic papules; distinct generalized AR peeling phenotype with impaired keratinocyte adhesion/apoptosis (vidya2023placksyndromeassociated pages 1-3, lin2015lossoffunctionmutationsin pages 1-2) | **CAST** (calpastatin) | Autosomal recessive (vidya2023placksyndromeassociated pages 1-3, lin2015lossoffunctionmutationsin pages 1-2) | p.Glu441Ter; homozygous exon 18 insertion causing frameshift/premature truncation (vidya2023placksyndromeassociated pages 1-3) | Spontaneous or trauma-associated peeling; bullae may follow trauma (vidya2023placksyndromeassociated pages 1-3) | PMID: 37317743; DOI: 10.25259/ijdvl_1138_2021; 10.1016/j.ajhg.2014.12.026 |


*Table: This table summarizes the main Peeling Skin Syndrome subtypes and closely related peeling disorders supported by the gathered evidence, including genes, inheritance, representative variants, triggers, and key references. It is useful as a compact crosswalk between clinical classification and molecular etiology.*

---

## Direct abstract quotations (as available in retrieved snippets)
* PSS definition (review excerpt): “**spontaneous peeling of the stratum corneum without bleeding or pain**.” (metze2026desmosomaltypeacantholysis—anew pages 10-12)
* Komatsu et al. 2006 (title reflects core mechanistic claim): “**Elevated human tissue kallikrein levels in the stratum corneum and serum of peeling skin syndrome-type B patients suggests an over-desquamation of corneocytes**.” (komatsu2006elevatedhumantissue pages 1-2)

---

## Notes on evidence limitations
* Several requested identifier fields (MONDO, MeSH, ICD-10/11, Orphanet IDs) were not retrievable from the current tool-based literature corpus; they should be populated by direct ontology/database queries.
* Some therapy claims (e.g., topical calcipotriol) are referenced secondarily in reviews without full primary-case detail in retrieved snippets; additional primary retrieval is recommended before encoding as high-confidence treatment evidence. (pan2022atopicdermatitislikegenodermatosis pages 33-33)



References

1. (metze2026desmosomaltypeacantholysis—anew pages 10-12): Dieter Metze, Kira Süßmuth, Clemens Metze, Vinzenz Oji, and Heiko Traupe. Desmosomal-type acantholysis—a new histologic pattern related to mutations of genes for desmosomal proteins. Dermatopathology, 13(2):17, Apr 2026. URL: https://doi.org/10.3390/dermatopathology13020017, doi:10.3390/dermatopathology13020017. This article has 0 citations.

2. (velden2020mutationsinthe pages 1-2): Jaap J. A. J. van der Velden, Michel van Geel, Jans J. Engelhart, Marcel F. Jonkman, and Peter M. Steijlen. Mutations in the cdsn gene cause peeling skin disease and hypotrichosis simplex of the scalp. The Journal of Dermatology, 47:3-7, Oct 2020. URL: https://doi.org/10.1111/1346-8138.15136, doi:10.1111/1346-8138.15136. This article has 15 citations.

3. (has2018peelingskindisorders pages 1-2): Cristina Has. Peeling skin disorders: a paradigm for skin desquamation. The Journal of investigative dermatology, 138 8:1689-1691, Aug 2018. URL: https://doi.org/10.1016/j.jid.2018.05.020, doi:10.1016/j.jid.2018.05.020. This article has 51 citations.

4. (komatsu2006elevatedhumantissue pages 1-2): Nahoko Komatsu, Yasushi Suga, Kiyofumi Saijoh, Amber C. Liu, Saba Khan, Yuki Mizuno, Shigaku Ikeda, Hua-Kang Wu, Arumugam Jayakumar, Gary L. Clayman, Fumiaki Shirasaki, Kazuhiko Takehara, and Eleftherios P. Diamandis. Elevated human tissue kallikrein levels in the stratum corneum and serum of peeling skin syndrome-type b patients suggests an over-desquamation of corneocytes. The Journal of investigative dermatology, 126 10:2338-42, Oct 2006. URL: https://doi.org/10.1038/sj.jid.5700379, doi:10.1038/sj.jid.5700379. This article has 84 citations.

5. (stjernbrandt2024acralpeelingskin pages 1-2): Anna-Lotta Stjernbrandt, Magnus Burstedt, Emma Holmbom, and Alexander Shayesteh. Acral peeling skin syndrome: two unusual cases and the therapeutic potential of botulinum toxin. Acta Dermato-Venereologica, 104:adv24305, Apr 2024. URL: https://doi.org/10.2340/actadv.v104.24305, doi:10.2340/actadv.v104.24305. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (kawakami2014acaseof pages 1-2): Hiroshi Kawakami, Masaki Uchiyama, Tatsuo Maeda, Takahiko Tsunoda, Yoshihiko Mitsuhashi, and Ryoji Tsuboi. A case of inflammatory generalized type of peeling skin syndrome possibly caused by a homozygous missense mutation of cdsn. Case Reports in Dermatology, 6:232-238, Oct 2014. URL: https://doi.org/10.1159/000368823, doi:10.1159/000368823. This article has 4 citations.

7. (oji2010lossofcorneodesmosin pages 6-7): Vinzenz Oji, Katja-Martina Eckl, Karin Aufenvenne, Marc Nätebus, Tatjana Tarinski, Katharina Ackermann, Natalia Seller, Dieter Metze, Gudrun Nürnberg, Regina Fölster-Holst, Monika Schäfer-Korting, Ingrid Hausser, Heiko Traupe, and Hans Christian Hennies. Loss of corneodesmosin leads to severe skin barrier defect, pruritus, and atopy: unraveling the peeling skin disease. American journal of human genetics, 87 2:274-81, Aug 2010. URL: https://doi.org/10.1016/j.ajhg.2010.07.005, doi:10.1016/j.ajhg.2010.07.005. This article has 291 citations and is from a highest quality peer-reviewed journal.

8. (vidya2023placksyndromeassociated pages 1-3): Aparna S. Vidya, Anza Khader, Keerankulangara Devi, Geetha Anandkumar Archana, Jose Reeshma, and Neerackal J. Reshma. Plack syndrome associated with alopecia areata and a novel homozygous base pair insertion in exon 18 of cast gene. Indian journal of dermatology, venereology and leprology, 90:1-4, May 2023. URL: https://doi.org/10.25259/ijdvl\_1138\_2021, doi:10.25259/ijdvl\_1138\_2021. This article has 6 citations.

9. (lin2015lossoffunctionmutationsin pages 1-2): Zhimiao Lin, Jiahui Zhao, Daniela Nitoiu, Claire A. Scott, Vincent Plagnol, Frances J.D. Smith, Neil J. Wilson, Christian Cole, Mary E. Schwartz, W.H. Irwin McLean, Huijun Wang, Cheng Feng, Lina Duo, Eray Yihui Zhou, Yali Ren, Lanlan Dai, Yulan Chen, Jianguo Zhang, Xun Xu, Edel A. O’Toole, David P. Kelsell, and Yong Yang. Loss-of-function mutations in cast cause peeling skin, leukonychia, acral punctate keratoses, cheilitis, and knuckle pads. American journal of human genetics, 96 3:440-7, Mar 2015. URL: https://doi.org/10.1016/j.ajhg.2014.12.026, doi:10.1016/j.ajhg.2014.12.026. This article has 63 citations and is from a highest quality peer-reviewed journal.

10. (bolling2018generalizedichthyoticpeeling pages 1-6): Maria C. Bolling, Sabrina Z. Jan, Anna M.G. Pasmooij, Henny H. Lemmink, Lude H. Franke, Vamsi K. Yenamandra, Richard J. Sinke, Peter C. van den Akker, and Marcel F. Jonkman. Generalized ichthyotic peeling skin syndrome due to flg2 mutations. Journal of Investigative Dermatology, 138:1881-1884, Aug 2018. URL: https://doi.org/10.1016/j.jid.2018.01.038, doi:10.1016/j.jid.2018.01.038. This article has 26 citations and is from a highest quality peer-reviewed journal.

11. (cabral2012wholeexomesequencingin pages 4-5): Rita M. Cabral, Mazen Kurban, Muhammad Wajid, Yutaka Shimomura, Lynn Petukhova, and Angela M. Christiano. Whole-exome sequencing in a single proband reveals a mutation in the chst8 gene in autosomal recessive peeling skin syndrome. Genomics, 99 4:202-8, Apr 2012. URL: https://doi.org/10.1016/j.ygeno.2012.01.005, doi:10.1016/j.ygeno.2012.01.005. This article has 74 citations and is from a peer-reviewed journal.

12. (krunic2013acralpeelingskin pages 1-2): Aleksandar L. Krunic, Kristina L. Stone, Michael A. Simpson, and John A. McGrath. Acral peeling skin syndrome resulting from a homozygous nonsense mutation in the csta gene encoding cystatin a. Pediatric Dermatology, Sep 2013. URL: https://doi.org/10.1111/pde.12092, doi:10.1111/pde.12092. This article has 56 citations and is from a peer-reviewed journal.

13. (gierach2023acralpeelingskin pages 1-3): Daria Gierach and Łukasz Kępczyński. Acral peeling skin syndrome. Dermatology Review, 110:567-573, Jan 2023. URL: https://doi.org/10.5114/dr.2023.131389, doi:10.5114/dr.2023.131389. This article has 2 citations.

14. (valentin2021developmentofa pages 1-5): F. Valentin, H. Wiegmann, T. Tarinski, H. Nikolenko, H. Traupe, E. Liebau, M. Dathe, and V. Oji. Development of a pathogenesis‐based therapy for peeling skin syndrome type 1*. British Journal of Dermatology, 184:1123-1131, Nov 2021. URL: https://doi.org/10.1111/bjd.19546, doi:10.1111/bjd.19546. This article has 21 citations and is from a highest quality peer-reviewed journal.

15. (kawakami2014acaseof pages 4-5): Hiroshi Kawakami, Masaki Uchiyama, Tatsuo Maeda, Takahiko Tsunoda, Yoshihiko Mitsuhashi, and Ryoji Tsuboi. A case of inflammatory generalized type of peeling skin syndrome possibly caused by a homozygous missense mutation of cdsn. Case Reports in Dermatology, 6:232-238, Oct 2014. URL: https://doi.org/10.1159/000368823, doi:10.1159/000368823. This article has 4 citations.

16. (pan2022atopicdermatitislikegenodermatosis pages 33-33): Chaolan Pan, Anqi Zhao, and Ming Li. Atopic dermatitis-like genodermatosis: disease diagnosis and management. Diagnostics, 12:2177, Sep 2022. URL: https://doi.org/10.3390/diagnostics12092177, doi:10.3390/diagnostics12092177. This article has 21 citations.

17. (stjernbrandt2024acralpeelingskin pages 2-2): Anna-Lotta Stjernbrandt, Magnus Burstedt, Emma Holmbom, and Alexander Shayesteh. Acral peeling skin syndrome: two unusual cases and the therapeutic potential of botulinum toxin. Acta Dermato-Venereologica, 104:adv24305, Apr 2024. URL: https://doi.org/10.2340/actadv.v104.24305, doi:10.2340/actadv.v104.24305. This article has 2 citations and is from a domain leading peer-reviewed journal.

18. (valentin2021developmentofa pages 9-12): F. Valentin, H. Wiegmann, T. Tarinski, H. Nikolenko, H. Traupe, E. Liebau, M. Dathe, and V. Oji. Development of a pathogenesis‐based therapy for peeling skin syndrome type 1*. British Journal of Dermatology, 184:1123-1131, Nov 2021. URL: https://doi.org/10.1111/bjd.19546, doi:10.1111/bjd.19546. This article has 21 citations and is from a highest quality peer-reviewed journal.

19. (kawakami2014acaseof pages 3-4): Hiroshi Kawakami, Masaki Uchiyama, Tatsuo Maeda, Takahiko Tsunoda, Yoshihiko Mitsuhashi, and Ryoji Tsuboi. A case of inflammatory generalized type of peeling skin syndrome possibly caused by a homozygous missense mutation of cdsn. Case Reports in Dermatology, 6:232-238, Oct 2014. URL: https://doi.org/10.1159/000368823, doi:10.1159/000368823. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](Peeling_Skin_Syndrome-deep-research-falcon_artifacts/artifact-00.md)