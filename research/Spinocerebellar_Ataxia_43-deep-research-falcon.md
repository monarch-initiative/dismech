---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:23:53.659477'
end_time: '2026-07-30T23:31:57.270108'
duration_seconds: 483.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar Ataxia 43
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spinocerebellar_Ataxia_43-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia 43
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 43** covering all of the
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
- **Disease Name:** Spinocerebellar Ataxia 43
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 43** covering all of the
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


# Spinocerebellar Ataxia Type 43 (SCA43): Disease-Characteristics Report

## Executive summary and evidence appraisal

Spinocerebellar ataxia type 43 (SCA43) is an exceptionally rare, late-onset, autosomal-dominant neurologic disorder characterized by **axonal polyneuropathy plus cerebellar ataxia**. The disease was defined in 2016 in one five-generation Belgian family carrying heterozygous **MME p.Cys143Tyr (p.C143Y)**. Among seven living affected relatives, all seven had late-onset sensorimotor axonal polyneuropathy and six had cerebellar ataxia. Consequently, most phenotype frequencies, penetrance estimates, and prognostic statements remain family-specific rather than population-level facts. No replicated SCA43 cohort, disease-specific treatment trial, validated biomarker, or pathogenic-variant model was identified through the 2024 literature horizon. (depondt2016mmemutationin pages 1-2)

| Domain | Best-supported SCA43-specific finding | Evidence strength/limitations |
|---|---|---|
| Disease identity | Spinocerebellar ataxia type 43; MONDO:0014867; Open Targets also maps the disease to EFO:0009060 and MME as the associated target (OpenTargets Search: spinocerebellar ataxia type 43-MME) | Disease ontology support exists, but disease-target evidence is sparse and ultimately anchored to the original family report (OpenTargets Search: spinocerebellar ataxia type 43-MME, depondt2016mmemutationin pages 1-2) |
| Ascertainment | Evidence comes from one five-generation Belgian family with 28 sampled relatives and 7 living affected individuals (depondt2016mmemutationin pages 1-2) | Very small sample size; single-family ascertainment strongly limits generalizability, penetrance estimation, phenotype frequencies, and epidemiology (depondt2016mmemutationin pages 1-2) |
| Causal gene/variant | Heterozygous MME variant p.Cys143Tyr / p.C143Y identified as the disease-segregating variant (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 3-4) | Best current causal evidence is cosegregation plus rarity/prediction; no independent SCA43 family replication in the retrieved evidence (depondt2016mmemutationin pages 3-4) |
| Inheritance | Autosomal dominant transmission in the reported pedigree (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 2-3) | Inheritance is well supported for this family, but broader penetrance and expressivity across populations remain unknown (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 3-4) |
| Age at onset | Late onset, reported between 42 and 68 years in affected family members (depondt2016mmemutationin pages 2-3) | Based only on the index family; no natural-history cohort available (depondt2016mmemutationin pages 2-3) |
| Core phenotype | Sensorimotor axonal polyneuropathy in 7/7 affected individuals; cerebellar ataxia in 6/7 (depondt2016mmemutationin pages 1-2) | Strongest phenotype data are family-specific; frequencies may reflect ascertainment rather than true disease spectrum (depondt2016mmemutationin pages 1-2) |
| Additional neurologic features | Reported features include gait/balance problems, dysarthria, hypometric saccades, cerebellar nystagmus, areflexia, distal amyotrophy, pes cavus, and hypoesthesia (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4) | Clinical detail is useful but derives from a handful of examined relatives; not all features were present in all patients (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4) |
| Imaging | Brain MRI showed cerebellar vermis atrophy (depondt2016mmemutationin pages 2-3) | Imaging evidence is disease-specific but limited to reported family members; no longitudinal imaging dataset (depondt2016mmemutationin pages 2-3) |
| Electrophysiology/pathology | Electrophysiology showed progressive severe motor axonal neuropathy with increased F-response latency, preserved sensory responses, and normal conduction velocities; one nerve biopsy showed CMT2-type axonal pathology (depondt2016mmemutationin pages 2-3) | Strong for neuropathy characterization in this family; limited pathology data and no disease biomarker validation (depondt2016mmemutationin pages 2-3) |
| Variant rarity | p.Cys143Tyr was absent from dbSNP, EVS, and ExAC at the time of publication; not found in 96 additional unrelated dominant ataxia cases screened by the authors (depondt2016mmemutationin pages 3-4) | Supports rarity, but database status may change over time; absence in another 96 cases underscores rarity rather than prevalence (depondt2016mmemutationin pages 3-4) |
| Mechanistic interpretation | MME encodes neprilysin, a zinc-dependent metalloprotease; dominant p.Cys143Tyr likely acts through a mechanism other than simple haploinsufficiency because recessive loss-of-function MME disease usually lacks cerebellar involvement (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 4-4) | Mechanism remains unresolved; functional studies were explicitly called for by the authors (depondt2016mmemutationin pages 4-5) |
| Epidemiology | No robust prevalence or incidence estimates identified for SCA43 (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 3-4) | Major evidence gap due to rarity and single-family basis (depondt2016mmemutationin pages 1-2) |
| Diagnostics | Best-supported diagnosis is clinical suspicion of dominant late-onset ataxia with axonal neuropathy followed by sequencing-based confirmation of MME (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 3-4) | No SCA43-specific diagnostic guideline or validated biomarker panel identified (depondt2016mmemutationin pages 2-3) |
| Treatment/trials | No SCA43-specific disease-modifying treatment, interventional trial, or gene-targeted therapy identified in retrieved sources (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 4-5) | Management is therefore extrapolated from broader hereditary ataxia/neuropathy supportive care, not direct SCA43 evidence (depondt2016mmemutationin pages 4-5) |
| Omics/biomarkers | No SCA43-specific transcriptomic, proteomic, metabolomic, or validated fluid biomarker study identified (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 4-5) | Major evidence gap limiting mechanism and trial-readiness work (depondt2016mmemutationin pages 4-5) |
| Models | No validated SCA43 p.Cys143Tyr model identified; Mme knockout mice do not recapitulate severe human axonal neuropathy and are not an established SCA43 model (depondt2016mmemutationin pages 4-5) | Important translational limitation; model-organism support is weak for this specific disease entity (depondt2016mmemutationin pages 4-5) |


*Table: This table summarizes the strongest disease-specific evidence currently available for spinocerebellar ataxia type 43. It highlights the core clinical-genetic findings and the major limitations created by single-family ascertainment and lack of replication, epidemiology, treatment trials, omics, and validated models.*

**Evidence labels used below:** **[Human—direct]** denotes the Belgian SCA43 family; **[Human—indirect]** denotes other MME-associated neuropathies; **[Model]** denotes animal evidence; and **[Inference]** denotes biologically plausible but unproven interpretation.

## 1. Disease information

### Definition

SCA43 is a Mendelian neurodegenerative disease in which dominantly inherited MME dysfunction produces a slowly progressive, late-onset combination of cerebellar and peripheral-nerve disease. It is not a repeat-expansion SCA. The defining publication described it as “dominant spinocerebellar ataxia with neuropathy.” (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 1-2)

### Identifiers and synonyms

- **MONDO:** **MONDO:0014867**.
- **EFO:** **EFO:0009060**.
- **Causal target association:** MME, Ensembl **ENSG00000196549**. (OpenTargets Search: spinocerebellar ataxia type 43-MME)
- **Synonyms:** spinocerebellar ataxia 43; spinocerebellar ataxia type 43; SCA43; dominant spinocerebellar ataxia with neuropathy; MME-related dominant ataxia with neuropathy.
- **OMIM/Orphanet:** a stable disease-specific identifier was not established from the retrieved primary evidence; these should be verified directly before database ingestion rather than inferred.
- **ICD-10/ICD-11 and MeSH:** no SCA43-specific code was identified. Broader hereditary ataxia/polyneuropathy codes are used clinically but are not uniquely identifying.

The evidence is **aggregated family-level research**, not an EHR-derived patient registry: 28 relatives were sampled, seven living affected relatives were characterized, and clinical records were reviewed. (depondt2016mmemutationin pages 1-2)

## 2. Etiology

### Causal factor

**[Human—direct]** The established cause is a germline heterozygous missense variant in **MME**, encoding neprilysin: **p.Cys143Tyr/p.C143Y**. It cosegregated with disease in the five-generation pedigree and was absent from dbSNP, EVS, and ExAC, the latter then comprising 60,706 individuals. It was also absent from 96 additional unrelated people with genetically unexplained dominant ataxia. (depondt2016mmemutationin pages 3-4)

The original genomic coordinate was reported as a G→A transition at chromosome 3q25.2, position 156,317,031. Because transcript/build-dependent HGVS expressions were not fully resolved in the retrieved evidence, a clinical report should state the reference transcript and genome build explicitly before assigning a cDNA HGVS expression. (depondt2016mmemutationin pages 3-4)

### Risk factors

- **Genetic:** carrying the familial heterozygous p.Cys143Tyr allele is the only demonstrated SCA43 risk factor. Family history compatible with autosomal-dominant late-onset ataxia/neuropathy materially raises prior probability.
- **Age:** manifestations occurred at 42–68 years, making increasing age an expression-related factor rather than an independent cause. (depondt2016mmemutationin pages 2-3)
- **Sex, ancestry, modifiers, environment, occupation, toxins, alcohol, smoking, diet, infection:** no SCA43-specific associations are known.

Other MME variants may cause dominant late-onset axonal neuropathy or biallelic recessive neuropathy without cerebellar disease. These entities should not automatically be labeled SCA43. In particular, simple MME loss of function appears insufficient to explain the distinctive dominant cerebellar phenotype. (depondt2016mmemutationin pages 4-4, depondt2016mmemutationin pages 4-5)

### Protective factors and gene–environment interaction

No genetic protective allele, environmental protective factor, or validated gene–environment interaction has been reported. Avoiding neurotoxic exposures and excess alcohol is reasonable general ataxia/neuropathy care, but it is not evidence-based primary prevention for SCA43.

## 3. Phenotypes

The frequencies below are descriptive proportions from seven affected relatives and have wide uncertainty.

- **Axonal sensorimotor polyneuropathy:** 7/7 reported affected individuals; late onset and progressive. Suggested HPO: **HP:0000763** (sensory neuropathy), **HP:0007002** (motor axonal neuropathy), **HP:0009830** (peripheral axonal neuropathy). Electrophysiology was motor-predominant, with prolonged F-response latency, preserved sensory responses, and normal conduction velocity in reported examinations. (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 2-3)
- **Cerebellar ataxia:** 6/7; mixed cerebellar and afferent gait dysfunction, slowly progressive. HPO: **HP:0001251** (ataxia), **HP:0002066** (gait ataxia), **HP:0002072** (cerebellar atrophy). (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 2-3)
- **Gait/balance impairment:** common presenting problem; the proband developed balance difficulty at approximately 58 years. HPO: **HP:0001288** (gait disturbance), **HP:0002321** (falls, if documented prospectively). (depondt2016mmemutationin pages 2-3)
- **Distal weakness/amyotrophy and pes cavus:** lower-limb wasting and cavus feet were reported. HPO: **HP:0003693** (distal muscle weakness), **HP:0008944** (distal lower-limb amyotrophy), **HP:0001761** (pes cavus). (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)
- **Areflexia/hyporeflexia and sensory loss:** absent Achilles reflexes and hypoesthesia were reported. HPO: **HP:0001284** (areflexia), **HP:0001265** (hyporeflexia), **HP:0003474** (sensory impairment). (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)
- **Dysarthria:** HPO **HP:0001260**. (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)
- **Oculomotor findings:** hypometric saccades and cerebellar nystagmus. HPO suggestions: **HP:0000641** (dysmetric saccades) and **HP:0000639** (nystagmus). (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)
- **Tremor, cogwheel rigidity, and palmomental reflex:** present in individual relatives; frequencies cannot be generalized. HPO: **HP:0001337** (tremor), **HP:0002063** (rigidity). (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)
- **Pectus carinatum:** distinctive but inconstant; HPO **HP:0000768**. (depondt2016mmemutationin pages 3-4)
- **Cognition:** no cognitive impairment was reported in the family. This is an observed absence, not proof that cognition is invariably preserved. (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 2-3)

### Quality-of-life effects

No EQ-5D, SF-36, PROMIS, SARA-based longitudinal quality-of-life, or caregiver-burden study exists for SCA43. Nevertheless, progressive imbalance, distal weakness, sensory impairment, and dysarthria plausibly impair walking, fall safety, communication, employment, and activities of daily living. This is clinical inference rather than quantified SCA43 evidence.

## 4. Genetic and molecular information

- **Gene:** **MME** (membrane metalloendopeptidase; neprilysin/CD10), chromosome **3q25.2**; Ensembl ENSG00000196549. (OpenTargets Search: spinocerebellar ataxia type 43-MME, depondt2016mmemutationin pages 3-4)
- **Protein:** neprilysin/NEP, a zinc-dependent M13-family metalloprotease with a short cytoplasmic N terminus, transmembrane helix, and large extracellular catalytic domain. It is expressed broadly, including neurons, CNS axons/synaptic terminals, and peripheral Schwann cells. (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 4-4)
- **Defining variant:** heterozygous germline **p.Cys143Tyr** missense variant. Cys143 is invariant across examined species and forms a disulfide bridge with Cys411; substitution is predicted to disrupt protein structure. SIFT, PolyPhen-2, and PROVEAN predicted damage. (depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 3-4)
- **Population frequency:** absent from the cited historical databases, including ExAC n=60,706; a current gnomAD version and exact transcript should be rechecked during curation. (depondt2016mmemutationin pages 3-4)
- **Classification:** compelling disease-candidate evidence includes rarity, segregation, conservation, computational predictions, and phenotypic fit. However, the retrieved study predates or did not provide a modern ClinGen expert-panel classification, independent-family replication, or variant-specific functional assay. A knowledge base should preserve the submitting laboratory’s current ClinVar classification rather than automatically assigning “pathogenic.”
- **Origin:** constitutional/germline; no somatic disease mechanism is implicated.
- **Mechanistic class:** dominant-negative or altered-function/gain-of-abnormal-function is more plausible than simple haploinsufficiency, because complete/biallelic MME loss causes peripheral neuropathy without the same dominant cerebellar phenotype. This remains unproven. (depondt2016mmemutationin pages 4-4, depondt2016mmemutationin pages 4-5)

No SCA43 modifier genes, epigenetic signature, pathogenic structural variant, chromosomal rearrangement, anticipation mechanism, or repeat expansion is known.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, dietary pattern, smoking behavior, alcohol exposure, exercise pattern, or infectious agent has been shown to cause or trigger SCA43. The disorder is not infectious or transmissible. Environmental evaluation remains important diagnostically because alcohol, medications, vitamin deficiencies, immune disease, and toxins can cause acquired ataxia or neuropathy and may compound disability, but they are differential diagnoses rather than established SCA43 determinants.

## 6. Mechanism and pathophysiology

### Supported molecular framework

Neprilysin cleaves multiple bioactive peptides, including neuropeptides and amyloid-β. Cys143 lies in the N-terminal peptidase M13 region and normally forms a disulfide bridge with Cys411. The p.Cys143Tyr substitution is therefore predicted to perturb folding, trafficking, stability, catalytic behavior, substrate selectivity, or intermolecular interactions. Variant-specific biochemical evidence is absent. (depondt2016mmemutationin pages 4-5)

### Proposed causal chain

1. **Upstream trigger:** germline heterozygous MME p.Cys143Tyr.
2. **Protein-level event:** disruption of the Cys143–Cys411 disulfide bond and altered neprilysin structure/function.
3. **Cellular event:** abnormal peptide processing and/or toxic dominant interference in neurons, axons, synaptic terminals, or Schwann cells.
4. **Tissue effects:** progressive long-axon degeneration produces distal motor-predominant neuropathy; cerebellar circuit dysfunction/degeneration produces vermian atrophy and ataxia.
5. **Clinical effects:** gait imbalance, distal weakness and wasting, areflexia, sensory symptoms, dysarthria, and oculomotor abnormalities. Steps 2–4 remain mechanistic hypotheses rather than experimentally proven SCA43 pathways. (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4, depondt2016mmemutationin pages 4-5)

The authors suggested altered processing of dynorphin peptides as one hypothesis because dynorphins are neprilysin substrates and PDYN causes another dominant ataxia, SCA23. This is pathway convergence, not proof of dynorphin accumulation in SCA43. (depondt2016mmemutationin pages 4-5)

### Ontology suggestions

- **GO biological process:** proteolysis (**GO:0006508**), neuropeptide catabolic process (**GO:0010813**), regulation of synaptic signaling, axon maintenance (**GO:0048675**), peripheral nervous system development/maintenance, and cerebellar neuron differentiation. Only protease/neuropeptide terms are direct MME-function annotations; degeneration terms are disease-level suggestions.
- **GO molecular function:** metalloendopeptidase activity (**GO:0004222**), zinc-ion binding (**GO:0008270**).
- **GO cellular component:** plasma membrane (**GO:0005886**), neuronal projection/axon and synaptic terminal; precise curated MME annotations should be imported from GO/UniProt.
- **Cell Ontology:** neuron (**CL:0000540**), cerebellar Purkinje cell (**CL:0000121**, plausible but not histologically demonstrated), Schwann cell (**CL:0002573**), peripheral sensory neuron (**CL:0000101**) and motor neuron (**CL:0000100**).

No SCA43-specific transcriptomic, single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, methylomic, CRISPR-screen, or multi-omic dataset was identified. There is likewise no demonstrated immune, inflammatory, mitochondrial, autophagic, or oxidative-stress signature.

## 7. Anatomical structures affected

- **Primary systems:** central and peripheral nervous systems.
- **CNS:** cerebellum, particularly the vermis on MRI; clinically, cerebellar motor/oculomotor circuits. Suggested UBERON: cerebellum **UBERON:0002037**, cerebellar vermis **UBERON:0004728**.
- **PNS:** peripheral motor and sensory nerves, especially long lower-limb axons. UBERON suggestions: peripheral nervous system **UBERON:0000010**, peripheral nerve **UBERON:0001021**.
- **Musculoskeletal secondary manifestations:** distal lower-limb muscle atrophy and pes cavus arise downstream of neuropathy.
- **Subcellular:** cell surface/plasma membrane and extracellular catalytic domain of neprilysin; axons and synaptic terminals are expression/localization sites. (depondt2016mmemutationin pages 2-3, depondt2016mmemutationin pages 4-4)

Disease is bilateral/systemic rather than characteristically unilateral. No SCA43 autopsy series establishes Purkinje-cell loss, regional neuropathology, or subcellular inclusions.

## 8. Temporal development

Onset is **adult/late adult, chronic, and insidious**, reported from 42 to 68 years. The proband developed gait/balance problems and distal lower-limb pain at approximately 58 years and was examined at 69. The course was slowly progressive, with increasing motor neuropathy and cerebellar disability. (depondt2016mmemutationin pages 2-3)

A practical descriptive staging scheme—not a validated SCA43 scale—is:

1. **Early:** distal pain/sensory symptoms or subtle imbalance.
2. **Intermediate:** evident gait ataxia, areflexia, pes cavus, distal weakness/amyotrophy, dysarthria or eye-movement signs.
3. **Advanced:** severe motor axonal neuropathy and increasing mobility impairment.

There are no established remission patterns, episodic attacks, critical treatment windows, annual SARA progression rate, or median disease duration. The disease should be regarded as chronic and lifelong after onset.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant, with vertical transmission and complete cosegregation in the reported pedigree. (depondt2016mmemutationin pages 1-2, depondt2016mmemutationin pages 3-4)
- **Penetrance:** apparently high among older carriers in this family, but exact lifetime penetrance cannot be estimated from seven affected individuals. Age dependence is likely because onset was after age 42.
- **Expressivity:** variable; one affected person had neuropathy without recognized cerebellar ataxia, while others had combined disease. (depondt2016mmemutationin pages 1-2)
- **Anticipation:** not reported and biologically not expected for a missense variant.
- **Mosaicism, founder effect, consanguinity, carrier frequency:** unknown/not demonstrated.
- **Sex ratio:** not estimable.
- **Geography/ancestry:** defining pedigree was Belgian; no population enrichment has been established.
- **Prevalence/incidence:** unknown. Failure to find the variant among 96 additional dominant-ataxia cases supports extreme rarity but is not a prevalence estimate. (depondt2016mmemutationin pages 3-4)

For counseling, a heterozygous affected person has a theoretical **50% transmission probability per pregnancy**, but age-dependent penetrance and phenotype severity cannot be predicted accurately.

## 10. Diagnostics

### Clinical evaluation

Suspect SCA43 when an adult has a family history consistent with dominant inheritance and the combination of slowly progressive cerebellar ataxia and axonal neuropathy. Assessment should include neurologic examination, pedigree, formal ataxia rating such as SARA, gait/fall assessment, ocular-motor examination, strength, reflexes, sensory testing, and cognition.

- **MRI:** assess cerebellar/vermian atrophy and exclude structural disease. Vermian atrophy supports but does not uniquely diagnose SCA43. (depondt2016mmemutationin pages 2-3)
- **Nerve conduction/EMG:** document axonal motor-sensory neuropathy; reported findings included progressive severe motor involvement, prolonged F responses, preserved sensory responses, and normal velocities. (depondt2016mmemutationin pages 2-3)
- **Biopsy:** one nerve biopsy showed CMT2-type axonal pathology, but biopsy is neither specific nor routinely required when molecular testing is available. (depondt2016mmemutationin pages 2-3)
- **Laboratory exclusion:** test for acquired/treatable causes according to presentation—vitamin B12, vitamin E, thiamine, thyroid disease, diabetes, paraproteinemia, autoimmune/paraneoplastic disease, infection, medication and toxic exposures. No SCA43 biochemical biomarker exists.

### Genetic testing strategy

1. Exclude common dominant repeat expansions and other high-priority ataxia causes according to ancestry/phenotype; standard exome sequencing can miss repeat expansions.
2. Use a comprehensive ataxia-plus-neuropathy panel that includes **MME**, or WES/WGS with copy-number and mitochondrial analysis as indicated.
3. Confirm candidate MME variants by orthogonal sequencing and perform familial segregation.
4. Interpret inheritance and phenotype carefully: biallelic MME loss is associated mainly with recessive axonal neuropathy, while monoallelic variants may confer incompletely penetrant neuropathy susceptibility; not every MME variant establishes SCA43. (depondt2016mmemutationin pages 4-4, depondt2016mmemutationin pages 4-5)

The founding discovery combined linkage analysis with WES and Sanger confirmation. Linkage localized a 3q23–q26.31 interval with LOD 2.47. (depondt2016mmemutationin pages 2-3)

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion assays do not directly detect a single-nucleotide MME missense variant, though they may be used in unresolved differential diagnosis. RNA sequencing, proteomics, metabolomics, epigenomics, and liquid biopsy have no validated SCA43 diagnostic role.

### Differential diagnosis

Important alternatives include common repeat-expansion SCAs; RFC1-related CANVAS; FGF14 GAA-expansion ataxia; SPG7; SETX-related ataxia; POLG and other mitochondrial ataxias; COA7-related ataxia-neuropathy; sensory ataxias; recessive or dominant MME-related CMT2; multiple-system atrophy-cerebellar type; immune, nutritional, toxic, and paraneoplastic ataxias. The combined dominant pedigree, axonal neuropathy, and pathogenic MME variant distinguish SCA43, but none of the clinical findings alone is specific.

### Screening

There is no population or newborn screening. Once a familial variant is established, targeted cascade testing is technically straightforward. Predictive testing of asymptomatic adults should occur with genetic counseling because onset, penetrance, and severity are uncertain. Prenatal and preimplantation genetic testing are technically possible for a confirmed familial pathogenic variant.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, five- or ten-year survival, hospitalization rate, or disease-specific cause-of-death analysis exists. Available evidence supports slow progression rather than acute lethality. Major expected morbidity includes falls, impaired ambulation, distal weakness/wasting, sensory complications, communication difficulty, and loss of independence. (depondt2016mmemutationin pages 2-3)

There is no evidence of spontaneous recovery or remission. No validated prognostic biomarker exists. Plausible clinical prognostic indicators include age at onset, baseline gait impairment, neuropathy severity, fall frequency, assistive-device requirement, SARA trajectory, and MRI progression, but none has been validated in SCA43.

## 12. Treatment

### Disease-modifying treatment

No approved SCA43-specific pharmacotherapy, neprilysin-directed therapy, gene therapy, CRISPR therapy, antisense oligonucleotide, siRNA, cell therapy, or immunotherapy exists. No SCA43-specific interventional trial or NCT identifier was identified. Because neprilysin has many substrates and systemic cardiovascular/renal roles, empirically increasing or inhibiting it could have unintended effects and is not justified outside research.

### Symptomatic and rehabilitative management

Management should be individualized and multidisciplinary:

- **Physical therapy:** balance, coordination, strength, aerobic conditioning, gait training, fall prevention, and home exercise. Suggested MAXO: physical therapy (**MAXO:0000011**) and exercise therapy.
- **Occupational therapy:** activities-of-daily-living adaptation, home safety, driving/work assessment, and energy conservation.
- **Mobility aids/orthotics:** cane, walker, wheelchair when necessary; ankle-foot orthoses and podiatry/orthopedic review for foot deformity. Suggested MAXO concepts: assistive device prescription and orthotic management.
- **Speech-language therapy:** dysarthria assessment and augmentative communication; swallowing evaluation if dysphagia emerges.
- **Neuropathic pain:** standard individualized agents such as gabapentinoids, serotonin–norepinephrine reuptake inhibitors, or tricyclics may be considered, accounting for sedation and fall risk. No SCA43 response rate is available.
- **Tremor/rigidity:** phenotype-directed symptomatic trials may be considered by a movement-disorders specialist, but evidence is anecdotal/non-specific.
- **Surveillance:** falls, mobility, pain, foot ulcers, contractures, nutrition/swallowing, mood, sleep, and caregiver needs.

No treatment algorithm or pharmacogenomic association specific to SCA43 has been validated. Surgical treatment is not disease modifying; orthopedic intervention is reserved for severe deformity. Deep-brain stimulation and noninvasive stimulation remain experimental for degenerative ataxia and have no SCA43-specific evidence.

## 13. Prevention

- **Primary prevention:** no lifestyle or medication prevents expression in a carrier. Reproductive options after counseling include donor gametes, prenatal diagnosis, or preimplantation genetic testing.
- **Secondary prevention:** cascade testing can identify adult relatives at risk; periodic neurologic examination may detect early gait or neuropathy manifestations, although evidence that presymptomatic surveillance alters biology is absent.
- **Tertiary prevention:** fall prevention, exercise, orthoses, foot care, pain treatment, swallowing/speech surveillance, vaccination and general health maintenance can reduce complications but do not prevent the genetic disease.
- **Immunization, antimicrobial prophylaxis, environmental remediation, and public-health control:** not disease-specific or applicable.

Suggested MAXO concepts include genetic counseling, familial variant testing, prenatal genetic testing, preimplantation genetic testing, fall-risk assessment, and rehabilitation therapy.

## 14. Other species and natural disease

MME orthologues are evolutionarily conserved in mammals, and conservation of Cys143 supports functional importance. However, no naturally occurring veterinary disorder was identified as a direct SCA43 analogue, and there is no zoonotic or cross-species transmission. (depondt2016mmemutationin pages 3-4)

Relevant taxa for comparative work include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Rattus norvegicus** (10116), and **Danio rerio** (7955). Orthologue-specific NCBI Gene IDs should be imported directly from NCBI/Alliance rather than inferred from the human identifier.

## 15. Model organisms and experimental systems

No validated p.Cys143Tyr knock-in mouse, rat, zebrafish, Drosophila, organoid, patient-derived iPSC, or Purkinje-cell model was identified. **Mme-null mice do not develop the severe axonal neuropathy seen in humans**, demonstrating species differences and making a knockout an inadequate direct model of dominant SCA43. (depondt2016mmemutationin pages 4-5)

Priority models should include:

1. heterozygous **Mme p.Cys143Tyr knock-in mice** with longitudinal gait, rotarod, eye-movement, nerve-conduction, cerebellar MRI, and histopathology;
2. patient-derived iPSC sensory neurons, motor neurons, Schwann cells, and cerebellar/Purkinje-like neurons;
3. isogenic CRISPR-corrected controls;
4. assays of neprilysin abundance, membrane trafficking, dimerization, zinc-dependent catalytic activity, and substrate-specific peptide processing;
5. proteomic/neuropeptidomic comparison of wild-type, heterozygous missense, and biallelic-null states.

Such systems could distinguish haploinsufficiency from dominant-negative or neomorphic action and test why the cerebellum is affected by p.Cys143Tyr but generally spared in biallelic loss-of-function neuropathy.

## Key primary source and abstract quotations

**Depondt et al., “MME mutation in dominant spinocerebellar ataxia with neuropathy (SCA43),” Neurology: Genetics, published October 2016. DOI:** https://doi.org/10.1212/NXG.0000000000000094. The abstract states: **“Affected individuals presented with late-onset sensorimotor axonal polyneuropathy; all but one also had cerebellar ataxia.”** It also states: **“We identified a variant in the MME gene, p.C143Y, that was absent from control databases, cosegregated with the phenotype, and was predicted to have a strong damaging effect.”** Finally, the authors concluded that **“Functional studies are needed to identify the mechanisms underlying these differences.”** (depondt2016mmemutationin pages 1-2)

## Research priorities and curation cautions

The highest priorities are independent case replication, current ClinVar/gnomAD reassessment of p.Cys143Tyr, standardized phenotyping with SARA and neuropathy scales, longitudinal MRI/electrophysiology, variant-specific biochemical studies, and a knock-in model. Until such evidence exists, SCA43 should be represented as a **single-family, MME-associated dominant ataxia-neuropathy syndrome**. Database curators should not merge it indiscriminately with recessive MME-related CMT2T, dominant late-onset MME neuropathy without ataxia, or nonspecific MME susceptibility alleles. (depondt2016mmemutationin pages 4-4, depondt2016mmemutationin pages 4-5, depondt2016mmemutationin pages 3-4)

References

1. (depondt2016mmemutationin pages 1-2): Chantal Depondt, Simona Donatello, Myriam Rai, François Charles Wang, Mario Manto, Nicolas Simonis, and Massimo Pandolfo. <i>mme</i> mutation in dominant spinocerebellar ataxia with neuropathy (sca43). Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000094, doi:10.1212/nxg.0000000000000094. This article has 47 citations.

2. (OpenTargets Search: spinocerebellar ataxia type 43-MME): Open Targets Query (spinocerebellar ataxia type 43-MME, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (depondt2016mmemutationin pages 4-5): Chantal Depondt, Simona Donatello, Myriam Rai, François Charles Wang, Mario Manto, Nicolas Simonis, and Massimo Pandolfo. <i>mme</i> mutation in dominant spinocerebellar ataxia with neuropathy (sca43). Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000094, doi:10.1212/nxg.0000000000000094. This article has 47 citations.

4. (depondt2016mmemutationin pages 3-4): Chantal Depondt, Simona Donatello, Myriam Rai, François Charles Wang, Mario Manto, Nicolas Simonis, and Massimo Pandolfo. <i>mme</i> mutation in dominant spinocerebellar ataxia with neuropathy (sca43). Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000094, doi:10.1212/nxg.0000000000000094. This article has 47 citations.

5. (depondt2016mmemutationin pages 2-3): Chantal Depondt, Simona Donatello, Myriam Rai, François Charles Wang, Mario Manto, Nicolas Simonis, and Massimo Pandolfo. <i>mme</i> mutation in dominant spinocerebellar ataxia with neuropathy (sca43). Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000094, doi:10.1212/nxg.0000000000000094. This article has 47 citations.

6. (depondt2016mmemutationin pages 4-4): Chantal Depondt, Simona Donatello, Myriam Rai, François Charles Wang, Mario Manto, Nicolas Simonis, and Massimo Pandolfo. <i>mme</i> mutation in dominant spinocerebellar ataxia with neuropathy (sca43). Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000094, doi:10.1212/nxg.0000000000000094. This article has 47 citations.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_43-deep-research-falcon_artifacts/artifact-00.md)