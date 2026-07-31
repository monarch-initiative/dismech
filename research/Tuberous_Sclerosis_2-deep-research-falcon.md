---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:04:27.979824'
end_time: '2026-07-31T00:16:08.965298'
duration_seconds: 700.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tuberous Sclerosis 2
  mondo_id: MONDO:0013199
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Tuberous_Sclerosis_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberous Sclerosis 2
- **MONDO ID:** MONDO:0013199 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis 2** covering all of the
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
- **Disease Name:** Tuberous Sclerosis 2
- **MONDO ID:** MONDO:0013199 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis 2** covering all of the
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


# Tuberous Sclerosis 2 (TSC2-associated tuberous sclerosis): comprehensive disease-characteristics report

## Scope and evidence note

“Tuberous sclerosis 2” is the gene-specific Mendelian subtype of **tuberous sclerosis complex (TSC)** caused by pathogenic variants in **TSC2**. Most clinical criteria, epidemiology, surveillance recommendations, and therapeutic trials enroll mixed TSC1/TSC2 cohorts; they are therefore labeled below as **broader-TSC evidence** rather than assumed to be TSC2-specific. TSC2-specific conclusions are strongest for molecular causation and genotype–phenotype severity.

| domain | key finding/statistic | ontology/identifier suggestions | evidence type |
|---|---|---|---|
| Disease identity | Tuberous sclerosis 2 is represented as MONDO:0013199 and is associated with target/gene TSC2 (ENSG00000103197) (OpenTargets Search: tuberous sclerosis 2-TSC2) | MONDO:0013199; Ensembl: ENSG00000103197; gene symbol: TSC2 | Aggregated disease-target resource |
| Nosology/relationship to broader disease | Clinically, TSC2-associated disease falls within tuberous sclerosis complex (TSC), a multisystem disorder caused by pathogenic variants in TSC1 or TSC2; requested entry is the TSC2-associated Mendelian subtype (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2) | MONDO:0013199; MeSH term on trial records: D014402 Tuberous Sclerosis; category: Mendelian | Human review/clinical synthesis |
| Inheritance | TSC is autosomal dominant; approximately one third of cases are inherited and the other two thirds are due to de novo and/or mosaic pathogenic variants in TSC1/TSC2 (man2024thegeneticsof pages 1-2) | HPO inheritance: Autosomal dominant inheritance [HP:0000006]; concept: mosaicism | Human review/clinical synthesis |
| Mosaicism / mutation-negative cases | About 15% of patients have no mutation identified by conventional testing; mosaic and intronic TSC1/TSC2 variants account for many such cases, with mosaic variants identified in up to 58% of no-mutation-identified individuals in cited studies summarized by the review (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8) | Variant concept: somatic mosaicism; testing implication: deep sequencing/tissue testing | Human review/clinical synthesis |
| Molecular cause | TSC1/TSC2 normally inhibit RHEB and suppress mTORC1; pathogenic TSC2 loss-of-function disrupts the TSC complex, causing mTORC1 hyperactivation and abnormal cell growth/hamartomas (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 4-5) | Pathway: mTORC1 signaling; GO suggestion: regulation of TOR signaling; disease mechanism: loss of function | Human review/clinical synthesis + pathway mapping |
| Mechanistic causal chain | TSC2 inactivation → loss of inhibition of RHEB → mTORC1 hyperactivation → increased cell growth/protein synthesis and reduced autophagy → hamartomas and neurodevelopmental abnormalities, especially in brain, kidney, heart, lung, skin (feliciano2020theneurodevelopmentalpathogenesis pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2) | GO suggestions: autophagy, cell growth, protein phosphorylation; UBERON: brain, kidney, heart, lung, skin | Human review + foundational mechanistic review |
| Genotype-phenotype severity | TSC2 pathogenic variants are associated with more severe phenotypes than TSC1, including higher risk of renal malignancies, cardiac rhabdomyomas, intellectual disability, infantile epileptic spasms, drug-resistant epilepsy, developmental delay, ADHD, and ASD (man2024thegeneticsof pages 7-8) | Phenotype terms: infantile spasms, intellectual disability, ASD, ADHD | Human review/clinical synthesis |
| Variant spectrum in a recent cohort | In 116 individuals with definite TSC, pathogenic DNA alterations were identified in 106 (91%); 88/106 (83%) were in TSC2 and 18/106 (17%) in TSC1; 35 variants were novel (dufneralmeida2024molecularandfunctional pages 11-14) | TSC2; variant classes assessed included missense and in-frame deletions | Human clinical molecular cohort |
| Contiguous gene syndrome | TSC2/PKD1 contiguous gene deletion syndrome occurs in up to 5% of TSC patients and is relevant when large deletions/coexisting cystic kidney disease are present (dufneralmeida2024molecularandfunctional pages 11-14) | PKD1; contiguous gene deletion syndrome | Human clinical molecular cohort/review |
| Major phenotype frequency: epilepsy | In TOSCA (n=2,093), epilepsy occurred in 83.5%; focal seizures were most common (66.9%); median age at epilepsy diagnosis was 1 year, and 78% were diagnosed at age ≤2 years (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 1-2) | HPO: Seizure [HP:0001250]; Focal-onset seizure [HP:0007359] | Human registry |
| Major phenotype frequency: cortical and subependymal lesions | TOSCA frequencies: cortical tubers 82.2%; subependymal nodules 78.2%; SEGA 24.4%; median SEGA diagnosis age 8 years, with 26.4% diagnosed before age 2 (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 8-10) | HPO: Cortical tuber; Subependymal nodule; Subependymal giant cell astrocytoma; UBERON: cerebral cortex, lateral ventricle | Human registry |
| Major phenotype frequency: renal/cardiac/skin/lung | TOSCA baseline frequencies: renal angiomyolipoma 47.2%; cardiac rhabdomyoma 34.3%; facial angiofibromas 57.3%; hypomelanotic macules 66.8%; shagreen patch 27.4%; forehead plaque 14.1%; LAM 6.9% overall in registry (kingswood2017tuberoussclerosisregistry pages 1-2) | HPO: Renal angiomyolipoma, Cardiac rhabdomyoma, Facial angiofibroma, Hypomelanotic macule; UBERON: kidney, heart, skin, lung | Human registry |
| Neuropsychiatric burden / QoL relevance | TAND affects ~90% of individuals over the lifetime; in TOSCA, academic/scholastic difficulties were reported in 57.8%, autism spectrum disorder in 20.7%, ADHD in 19.6%, anxiety in 9.1%, depression in 6.1%, and intellectual disability in 54.9% of tested patients (kingswood2017tuberoussclerosisregistry pages 2-5, vanclooster2022theresearchlandscape pages 1-2) | HPO/psychiatric terms: Intellectual disability, Autism spectrum disorder, ADHD, Anxiety, Depression; TAND | Human registry + scoping review |
| Epidemiology | Reported incidence ranges from 1:5800 to 1:13,520 live births; other reviews summarize incidence as 1:6000 to 1:10,000 live births and prevalence around 1 in 20,000 people; Japan-specific prevalence cited as 1 in 10,300 live births (man2024thegeneticsof pages 1-2, conte2024therapeuticapproachesto pages 1-2, okanishi2024diagnosticflowanalysis pages 1-2) | Epidemiology field; rare disease | Human review + claims study |
| Mortality/morbidity | Leading morbidity/mortality drivers summarized in recent reviews include brain tumours/SEGA, epilepsy-related complications including SUDEP/status epilepticus, renal complications, and respiratory disease/LAM (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2) | Outcome terms: SUDEP, renal complication, respiratory complication | Human review/clinical synthesis |
| Diagnostic delay / real-world implementation | In a Japanese claims study, renal tumors as first manifestation had the longest time-to-diagnosis (median 23 to up to 91 months); for patients with epilepsy, diagnosis was faster at TSC clinics than non-TSC clinics (median 11.5 vs 19.0 months; p=0.0379) (okanishi2024diagnosticflowanalysis pages 1-2) | Care pathway; specialized TSC clinic | Real-world human claims study |
| Diagnostic approach and genetics | Molecular diagnosis confirms the clinical diagnosis in a large proportion of cases; functional assessment of TSC2 variants can help establish pathogenicity; contemporary reviews emphasize sequencing plus evaluation for deep intronic variants, CNVs, and mosaicism, often requiring re-phenotyping/re-genotyping and sometimes non-blood tissues (dufneralmeida2024molecularandfunctional pages 11-14, man2024thegeneticsof pages 7-8) | Gene testing: TSC2/TSC1 sequencing; CNV analysis; deep intronic analysis; mosaicism testing | Human clinical molecular cohort + review |
| Prenatal diagnosis | Prenatal TSC commonly presents with cardiac rhabdomyomas; prenatal management literature review identified 8 papers covering 10 pregnant women treated with mTOR inhibitors and 3 prenatal mouse studies (racioppi2024prenatalmtorinhibitors pages 1-2) | Prenatal screening; fetal ultrasound/echo context | Human case-series review + animal prenatal studies |
| Approved/established targeted therapy | Everolimus is approved for TSC-associated partial-onset seizures (age ≥2 years), and for SEGA and AML; mTOR inhibitors also reduce TSC-related lesions including kidney AMLs, SEGAs, and facial angiofibromas (conte2024therapeuticapproachesto pages 4-5) | CHEBI/drug: everolimus; MAXO suggestion: mTOR inhibitor therapy | Human review summarizing trials/approvals |
| Renal AML treatment statistic | In a 50-patient adult cohort, low-dose everolimus produced an average AML volume reduction of 52% versus 60% with conventional dose, with significantly less stomatitis and irregular menstruation in the low-dose group (kingswood2017tuberoussclerosisregistry pages 2-5) | Renal angiomyolipoma; MAXO: everolimus treatment | Human clinical treatment cohort |
| Epilepsy treatment: vigabatrin | Preventive vigabatrin reduced risk of seizures, infantile spasms, and drug-resistant epilepsy in one summarized study, but no difference in developmental delay or autism at 2 years; PREVeNT delayed/reduced infantile spasms but not focal seizures/drug-resistant epilepsy or cognitive outcomes at age 2 (conte2024therapeuticapproachesto pages 4-5) | Drug: vigabatrin; HPO: Infantile spasms | Human review summarizing trials |
| Epilepsy treatment: cannabidiol | Cannabidiol was authorized in the EU in April 2021 as adjunctive therapy for TSC-associated seizures in patients aged ≥2 years (conte2024therapeuticapproachesto pages 4-5) | Drug: cannabidiol; MAXO: antiseizure pharmacotherapy | Human review/regulatory summary |
| LAM treatment | Sirolimus has been the FDA-approved mainstay treatment for LAM since 2015 and supports pulmonary function control/decreased lymphatic symptoms in LAM (conte2024therapeuticapproachesto pages 4-5) | Drug: sirolimus; phenotype: lymphangioleiomyomatosis | Human review/clinical synthesis |
| Adverse effects of mTOR inhibitors | Important adverse effects include mouth ulceration/stomatitis, immunosuppression, and infection risk; in young patients sirolimus side effects summarized as common but not life- or health-threatening included anemia, hyperlipidemia, and thrombocytosis (conte2024therapeuticapproachesto pages 4-5) | Safety annotation; AE terms | Human review/clinical synthesis |
| Experimental trial: seizure prevention | TSC-STEPS (NCT05104983) is a Phase II randomized, double-blind, placebo-controlled multisite trial testing early sirolimus in infants 0–6 months to prevent or delay seizure onset; planned enrollment 64; primary outcome time to seizure onset by 12 months (NCT05104983 chunk 1) | ClinicalTrials.gov: NCT05104983; prevention trial | Interventional trial registry |
| Experimental trial: drug-resistant epilepsy | RaRE-TS (NCT05534672) is a Phase III randomized, double-blind, placebo-controlled trial of rapamycin versus placebo for drug-resistant epilepsy associated with TSC; estimated enrollment 200; primary endpoint includes ≥50% seizure reduction and adverse events (NCT05534672 chunk 1) | ClinicalTrials.gov: NCT05534672 | Interventional trial registry |
| Experimental trial: NMDA-modulator | Astroscape (NCT06392009) is an open-label phase 1/2 study of radiprodil for treatment-resistant seizures/behavioral symptoms in TSC or FCD II; estimated enrollment 30 total, about 20 with TSC (NCT06392009 chunk 1) | ClinicalTrials.gov: NCT06392009; drug: radiprodil | Interventional trial registry |
| Cellular/organoid models | 2024 TSC2 iPSC-derived cortical organoids showed disrupted neurogenesis, synaptogenesis, gliogenesis/reactive astrogliosis, neuron-reactive astrocyte crosstalk, synaptic transmission, neuronal network activity, mitochondrial translational integrity, and neurofilament formation; findings resembled resected TSC cortical tissue (niu2024longitudinalmultiomicsreveals pages 1-6) | CL suggestions: neuron, astrocyte; GO: synaptogenesis, gliogenesis, mitochondrial translation | In vitro human organoid + matched surgical tissue comparison |
| Animal models | Zebrafish and other mTORopathy models are used to study TSC-related epilepsy and neuropathology; model summaries note TSC1/TSC2 overactivation of mTOR pathway with epilepsy/benign tumors, but translational limits remain for exact human multisystem phenotype capture (abreu2023developingnovelexperimental pages 3-4) | Model organism: zebrafish; disease mechanism: mTORopathy | Model organism review |
| Evidence limitations | Much of the recent TSC2-specific mechanistic work is review-based or preprint/in vitro; several phenotype and treatment frequencies derive from broader TSC cohorts rather than TSC2-only cohorts, so TSC2-specific extrapolation should be done cautiously (niu2024longitudinalmultiomicsreveals pages 1-6, kingswood2017tuberoussclerosisregistry pages 2-5, man2024thegeneticsof pages 1-2) | Evidence flag: broader TSC vs TSC2-specific | Evidence appraisal |


*Table: This compact table summarizes database-ready facts for TSC2-associated tuberous sclerosis, including identifiers, mechanism, phenotype frequencies, diagnostics, therapies, trials, and model systems. It is restricted to claims directly supported by gathered evidence contexts.*

## 1. Disease information

TSC2-associated TSC is an autosomal-dominant neurocutaneous and tumor-predisposition disorder characterized by age-dependent hamartomas and dysplastic lesions of the brain, kidneys, skin, heart, lungs, and eyes. Neurological disease—particularly early epilepsy, cortical malformations, and TSC-associated neuropsychiatric disorders (TAND)—usually contributes the greatest childhood burden; renal and pulmonary disease becomes increasingly important in adults. A recent review calls TSC the “prototypical mTORopathy.” (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2)

**Identifiers and synonyms**

- **MONDO:** MONDO:0013199, “tuberous sclerosis 2.” Open Targets maps this entity to **TSC2**, Ensembl **ENSG00000103197**. (OpenTargets Search: tuberous sclerosis 2-TSC2)
- **Gene/protein:** TSC2, *TSC complex subunit 2*; protein **tuberin**. TSC2 is the catalytic GAP-containing component of the TSC1–TSC2–TBC1D7 complex.
- **Common names:** TSC2-associated tuberous sclerosis complex; tuberous sclerosis type 2; Bourneville disease/Bourneville–Pringle disease (historical, generally applied to TSC overall).
- **MeSH:** Tuberous Sclerosis, **D014402**, as represented in trial indexing. (NCT05534672 chunk 1)
- **OMIM:** commonly represented as tuberous sclerosis-2, **OMIM 613254**, with **TSC2 OMIM 191092**. These identifiers should be verified directly against OMIM before production ingestion because OMIM itself was not retrievable in the supplied evidence set.
- **Orphanet:** TSC is generally ORPHA:805; Orphanet does not usually separate routine clinical care into TSC1- and TSC2-specific diseases.
- **ICD:** ICD-10-CM **Q85.1** (tuberous sclerosis); ICD coding does not distinguish TSC2. ICD-11 should be mapped to the current tuberous-sclerosis entity in the implementation’s release because codes may change between versions.

The evidence summarized here is primarily **aggregated disease-level evidence**—international registry, cohorts, reviews, and trial records—not individual EHR data. The Japanese diagnostic-flow study is aggregated claims data from the JMDC database. (kingswood2017tuberoussclerosisregistry pages 2-5, okanishi2024diagnosticflowanalysis pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factors

The primary cause is a heterozygous pathogenic **loss-of-function TSC2 variant**, constitutional or mosaic. Approximately one third of all TSC is inherited; roughly two thirds results from de novo and/or mosaic variants. There is no established infectious, toxic, dietary, or occupational cause. (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2)

Tumor-like lesions frequently follow a tumor-suppressor “two-hit” model: constitutional TSC2 haploinsufficiency creates susceptibility and a somatic second hit inactivates the remaining allele in a lesion-forming lineage. Timing and anatomical distribution of mosaic/second-hit events help explain focal lesions and variable expressivity.

### Genetic risk factors

- Having an affected heterozygous parent gives each pregnancy a **50% transmission risk**, although phenotype cannot be predicted reliably because expressivity is highly variable.
- TSC2 variants generally produce more severe disease than TSC1 variants, including greater risks of infantile epileptic spasms, drug-resistant epilepsy, intellectual/developmental disability, cardiac rhabdomyoma, renal disease/malignancy, ADHD, and autism. TSC2-associated epilepsy tends to begin earlier and may respond less favorably to epilepsy surgery. (man2024thegeneticsof pages 7-8)
- Truncating variants and variants disrupting critical TSC2 domains tend to be more severe than variants preserving residual expression. Deep-intronic or noncoding variants and low-level mosaicism often cause attenuated disease, although exceptions are important. CNVs account for up to about 10% in some cohorts. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8)
- A deletion extending into adjacent **PKD1** produces **TSC2–PKD1 contiguous-gene deletion syndrome**, with early, severe polycystic kidney disease; it may account for up to 5% of TSC in some clinical series. (dufneralmeida2024molecularandfunctional pages 11-14)

A 2024 Brazilian study found a molecular alteration in 106/116 clinically definite cases (91.4%): 88/106 (83%) were TSC2 and 18/106 (17%) TSC1; 35 were novel. Exact abstract quote: “Pathogenic DNA alterations were identified in 106 cases (91%); 18 (17%) in TSC1 and 88 (83%) in TSC2.” Functional assays demonstrated disrupted TSC-complex activity for seven TSC2 variants. Published November 2024; DOI: https://doi.org/10.3390/genes15111432. (dufneralmeida2024molecularandfunctional pages 11-14)

### Environmental and protective factors

No environmental exposure is known to cause inherited TSC2 disease, and no validated genetic or lifestyle factor prevents penetrance. Environmental and physiological inputs—growth factors, insulin, nutrients/amino acids, energy status, oxygen, and cellular stress—normally converge on PI3K–AKT–TSC–RHEB–mTOR signaling; loss of TSC2 reduces the pathway’s ability to respond appropriately, but this is mechanistic modulation rather than an established epidemiological gene–environment interaction. (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 4-5)

Practical “protective factors” are therefore **secondary/tertiary prevention**: presymptomatic EEG monitoring, early seizure treatment, blood-pressure and kidney preservation, smoking avoidance in pulmonary disease, and avoidance of exogenous estrogen where LAM risk is clinically relevant. Evidence for specific diets, exercise regimens, supplements, or protective alleles is insufficient.

## 3. Phenotypes

The following frequencies are from **TOSCA**, an international registry of 2,093 individuals at 170 sites in 31 countries, and describe mixed-genotype TSC. Median enrollment age was 13 years and median diagnostic age 1 year; 5.9% were diagnosed prenatally. (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 1-2)

### Neurological and neurodevelopmental

- **Epilepsy** — symptom/sign; **83.5%** in TOSCA, focal seizures 66.9%; 78% were diagnosed by age 2. Typical onset is in the first months/year, with focal seizures or infantile spasms; severity ranges from controlled to drug resistant, the latter affecting about two thirds in some series. Suggested HPO: **Seizure HP:0001250**, focal-onset seizure, infantile spasms, hypsarrhythmia. Early, frequent, and refractory seizures predict poorer cognition and substantial caregiver/QOL burden. (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2)
- **Cortical tubers** — imaging/pathological sign; 82.2% in TOSCA and 88–100% in some series. Congenital and generally structurally persistent, though epileptogenic activity is dynamic. Tubers contain disorganized cortex, dysplastic neurons, giant cells, and abnormal astrocytes. Suggested HPO: cortical tuber; abnormal cortical gyration/architecture. (kingswood2017tuberoussclerosisregistry pages 2-5, conte2024therapeuticapproachesto pages 1-2)
- **Subependymal nodules (SENs)** — imaging sign; 78.2%; congenital/childhood, often stable and calcifying. Suggested HPO: subependymal nodule. (kingswood2017tuberoussclerosisregistry pages 2-5)
- **Subependymal giant-cell astrocytoma (SEGA)** — benign glioneuronal tumor; 24.4% in TOSCA, median diagnosis age 8 years and 26.4% diagnosed before 2; 36.7% of ongoing SEGAs showed growth, particularly from 5–18 years. Growth near the foramen of Monro can cause hydrocephalus, raised intracranial pressure, seizure worsening, and cognitive/behavioral decline. Suggested HPO: SEGA, hydrocephalus. (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 8-10, conte2024therapeuticapproachesto pages 1-2)
- **Developmental delay/intellectual disability** — developmental/behavioral phenotype; 54.9% among assessed TOSCA patients; another mechanistic review estimates approximately 50%. Severity is variable, and TSC2 carriers are at higher risk, especially with early epilepsy. Suggested HPO: **Global developmental delay HP:0001263**, **Intellectual disability HP:0001249**. (feliciano2020theneurodevelopmentalpathogenesis pages 1-2, kingswood2017tuberoussclerosisregistry pages 2-5, man2024thegeneticsof pages 7-8)
- **TAND** — umbrella covering behavioral, psychiatric, intellectual, academic, neuropsychological, and psychosocial manifestations; affects approximately 90% over a lifetime. TOSCA reported scholastic difficulty 57.8%, ASD 20.7%, ADHD 19.6%, anxiety 9.1%, and depression 6.1%, but underassessment is substantial. Suggested HPO: autism, attention-deficit/hyperactivity disorder, anxiety, depression, sleep disturbance, aggressive behavior. (kingswood2017tuberoussclerosisregistry pages 2-5, vanclooster2022theresearchlandscape pages 1-2)

### Renal, pulmonary, cardiac, skin, and eye

- **Renal angiomyolipomas (AMLs):** 47.2% in TOSCA and reported to approach 80% after age 40; often bilateral/multiple and progressive. Complications include pain, aneurysm, retroperitoneal hemorrhage, hypertension, CKD, and treatment-related nephron loss. HPO: renal angiomyolipoma; hematuria; renal hemorrhage. (kingswood2017tuberoussclerosisregistry pages 1-2, kingswood2017tuberoussclerosisregistry pages 8-10)
- **Renal cysts/PKD and renal-cell carcinoma:** cysts range from limited disease to severe childhood PKD in TSC2–PKD1 deletions; RCC is uncommon but occurs younger than sporadic RCC. HPO: renal cyst, polycystic kidney dysplasia, renal insufficiency.
- **Cardiac rhabdomyoma:** 34.3% in TOSCA; commonly detected prenatally or in infancy and often regresses. Large lesions can cause obstruction, arrhythmia, low output, or hydrops. HPO: cardiac rhabdomyoma, fetal cardiac tumor, arrhythmia. (kingswood2017tuberoussclerosisregistry pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2)
- **LAM/cystic lung disease:** 6.9% in the age-mixed TOSCA cohort, but CT-screened adult-woman estimates are much higher; a 2024 review cites about 30%. It is a slowly progressive, low-grade metastasizing neoplasm, predominantly in women, causing dyspnea, pneumothorax, chylous effusion, and declining lung function. HPO: pulmonary lymphangioleiomyomatosis, lung cyst, pneumothorax. (kingswood2017tuberoussclerosisregistry pages 1-2, conte2024therapeuticapproachesto pages 1-2)
- **Skin:** hypomelanotic macules 66.8%, facial angiofibromas 57.3%, shagreen patches 27.4%, forehead plaques 14.1% in TOSCA. Lesions are age dependent: hypomelanotic macules may be congenital; facial angiofibromas and ungual fibromas often accrue later. HPO: hypopigmented skin macule, facial angiofibroma, shagreen patch, periungual fibroma. (kingswood2017tuberoussclerosisregistry pages 1-2)
- **Retina:** retinal hamartomas and achromic patches may support diagnosis; vision impact is usually limited unless location is critical. HPO: retinal hamartoma.

### Quality of life

Disease burden arises from seizures, cognitive/behavioral disability, disfiguring skin lesions, renal/pulmonary morbidity, repeated imaging/procedures, medication toxicity, and caregiver demands. The 2023 TSC-PROM created 82-item self-report and 75-item proxy versions across physical function, mental function, activity/participation, and social support; internal consistency was strong (Cronbach α 0.78–0.97). DOI: https://doi.org/10.1186/s12916-023-03012-4, published August 2023. TAND remains under-assessed and under-treated despite its near-universal lifetime burden. (vanclooster2022theresearchlandscape pages 1-2)

## 4. Genetic and molecular information

### Causal gene and variants

- **TSC2:** chromosome 16p13.3; HGNC symbol TSC2; Ensembl ENSG00000103197; protein tuberin. (OpenTargets Search: tuberous sclerosis 2-TSC2)
- Disease-causing classes include nonsense, frameshift, canonical and noncanonical splice variants, deleterious missense and in-frame indels, exon-level or whole-gene deletions/duplications, complex rearrangements, deep-intronic variants, and mosaic variants. The expected mechanism is **loss of function**, not gain of function or dominant-negative activity.
- Germline heterozygous variants create systemic disease; postzygotic mosaic variants produce variable tissue distribution. Somatic second hits occur in individual lesions.
- Pathogenic TSC2 alleles should generally be absent or extremely rare in gnomAD/other population databases because TSC is rare and highly penetrant. No universal allele frequency can be assigned: frequency is variant specific. Common population variants are not accepted as causal without compelling functional/segregation evidence.
- ClinVar classifications range from pathogenic/likely pathogenic to VUS and conflicting. Functional demonstration of failure to suppress TORC1 can help resolve selected missense or in-frame variants, but should be integrated with ACMG/AMP evidence rather than used alone. (dufneralmeida2024molecularandfunctional pages 11-14)

Approximately 15% of clinically diagnosed patients are mutation-negative by conventional testing. Recent studies summarized in a 2024 review found mosaic variants in up to 58% and intronic variants in up to 40% of previously mutation-negative individuals. Exact review quote: “Notably, 15% of patients have no mutation identified by conventional genetic testing.” DOI: https://doi.org/10.3390/genes15030332, published March 4, 2024. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8)

### Modifier and epigenetic evidence

No modifier gene is sufficiently validated for routine clinical prediction. Candidate contributors include variant position/residual transcript, second-hit timing, mosaic fraction and tissue distribution, and possibly other mTOR-pathway alleles. Mitochondrial-genome variation was investigated but showed no correlation with TSC clinical features in the study summarized by the 2024 review. (man2024thegeneticsof pages 7-8)

Disease-specific DNA methylation, histone, or chromatin signatures are not validated diagnostic or prognostic biomarkers. Epigenetic remodeling is biologically plausible downstream of chronic mTORC1 activation, but current evidence is insufficient for a knowledge-base assertion of a recurrent causal epimutation.

### Chromosomal abnormalities

Large 16p13.3 deletions may remove TSC2 alone or TSC2 plus neighboring PKD1. CMA can detect sufficiently large deletions, but exon-scale CNVs require validated NGS-CNV or MLPA analysis. Conventional karyotyping is insensitive to most causal variants; FISH is reserved for selected known deletions/rearrangements.

## 5. Environmental information

TSC2 disease is not caused by toxins, radiation, infection, smoking, diet, alcohol, or occupation. Lifestyle affects complications rather than genetic occurrence. Relevant management modifiers include avoiding smoking and unnecessary pulmonary injury in LAM, careful estrogen counseling in women at LAM risk, maintaining cardiovascular/renal health, and avoiding nephrotoxic practices where alternatives exist. No vaccine or antimicrobial prevention is disease-specific. The dry-skin association reported in a Japanese claims cohort is not evidence of an environmental cause. (okanishi2024diagnosticflowanalysis pages 1-2)

## 6. Mechanism and pathophysiology

### Core causal chain

**Pathogenic TSC2 loss of function → destabilized/inactive TSC1–TSC2–TBC1D7 complex → failure of tuberin GAP activity toward RHEB-GTP → persistent RHEB–mTORC1 signaling → increased protein/lipid/nucleotide synthesis and cell size, reduced autophagy, altered metabolism and differentiation → dysplastic cells, hamartomas, cortical-network dysfunction, epilepsy, and organ-specific tissue injury.** (feliciano2020theneurodevelopmentalpathogenesis pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2)

Upstream inputs include PI3K–AKT growth-factor signaling, amino acids, AMPK/energy status, oxygen, and stress. Downstream outputs include S6K and 4E-BP–dependent translation, autophagy suppression, altered mitochondrial/metabolic function, abnormal cell-cycle/growth programs, and feedback effects on PI3K–AKT. mTORC1 dysregulation is primary; inflammation, gliosis, fibrosis, excitatory/inhibitory imbalance, hemorrhage, obstruction, and organ failure are downstream.

### Brain and epilepsy

Cortical lesions show disrupted six-layer architecture, cytomegalic/dysplastic neurons, giant cells, and abnormal astrocytes. Altered GABA transporters and glutamate receptors, reduced GABAergic inhibition, increased glutamatergic excitation, abnormal neuronal migration/synaptogenesis, and reactive astrogliosis create epileptogenic networks; apparently normal perituberal cortex may also generate seizures. (racioppi2024prenatalmtorinhibitors pages 1-2)

A 2024 TSC2 iPSC cortical-organoid preprint combined longitudinal transcriptomic, proteomic, cellular, and electrophysiological analyses. It found disrupted neurogenesis, synaptogenesis, gliogenesis/reactive astrogliosis, NLGN–NRXN neuron–astrocyte communication, mitochondrial translation, neurofilament formation, synaptic transmission, and network activity, with similar disturbances in resected human cortex. This is **in-vitro/preprint evidence**, not yet a validated clinical biomarker. DOI: https://doi.org/10.1101/2024.10.07.617121, October 2024. (niu2024longitudinalmultiomicsreveals pages 1-6)

### Kidney, lung, heart, and skin

Kidney lesions arise through lineage- and developmental-context-dependent second hits, mTORC1-driven proliferation, abnormal vascular/adipose/smooth-muscle differentiation, cystogenesis, aneurysm/hemorrhage, and progressive parenchymal loss. LAM cells show mTORC1-dependent smooth-muscle-like proliferation and metastatic behavior, causing cystic destruction and lymphatic abnormalities. Cardiac rhabdomyomas reflect prenatal mTOR-driven myocardial overgrowth but often involute after birth. Skin hamartomas reflect fibrovascular and follicular-cell overgrowth.

### Suggested ontology annotations

- **GO biological process:** negative regulation of TOR signaling; TORC1 signaling; regulation of cell growth; macroautophagy; protein translation; neurogenesis; neuronal migration; synapse organization; gliogenesis; mitochondrial translation; regulation of GTPase activity.
- **GO cellular component:** TSC1–TSC2 complex; lysosomal membrane; cytosol; mTORC1 complex; synapse; mitochondrion.
- **Cell Ontology:** neuron; GABAergic interneuron; astrocyte/reactive astrocyte; neural stem/progenitor cell; radial glial cell; renal epithelial cell; vascular smooth-muscle cell; fibroblast; cardiomyocyte; retinal cell. Exact CL identifiers should be resolved against the ontology release used by the knowledge base.

## 7. Anatomical structures affected

Primary systems are nervous, renal/urinary, integumentary, cardiovascular, respiratory/lymphatic, and ocular. Suggested UBERON mappings include cerebral cortex, subependymal zone/lateral ventricle, kidney, heart/myocardium, lung, skin, nail, and retina. Brain lesions may be multifocal and bilateral but are often asymmetric; renal AMLs/cysts are commonly bilateral; LAM is diffuse bilateral lung disease. (kingswood2017tuberoussclerosisregistry pages 1-2, racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2)

At the subcellular level, the critical signaling interface is cytosolic/lysosome-associated RHEB–mTORC1 regulation; downstream abnormalities involve translational machinery, autophagosomes/lysosomes, synapses, cytoskeleton/neurofilaments, and mitochondria. (feliciano2020theneurodevelopmentalpathogenesis pages 1-2, niu2024longitudinalmultiomicsreveals pages 1-6)

## 8. Temporal development and natural history

TSC is congenital and lifelong, but manifestations are strongly age dependent. Cardiac rhabdomyomas and cortical lesions may be prenatal; hypomelanotic macules and seizures commonly emerge in infancy. Epilepsy typically starts in the first year, and earlier onset is associated with worse long-term development. SEGA growth is concentrated in childhood and adolescence. Facial angiofibromas, ungual fibromas, AMLs, renal dysfunction, and LAM become more prominent with age. (kingswood2017tuberoussclerosisregistry pages 2-5, kingswood2017tuberoussclerosisregistry pages 8-10, racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 1-2)

There is no uniform staging system. A practical trajectory is: **prenatal/infant detection → early epilepsy/neurodevelopmental vulnerability → childhood SEGA/TAND burden → accumulating renal, dermatologic, and pulmonary morbidity in adulthood**. Individual lesions may remain stable, progress, regress spontaneously (especially rhabdomyomas), or shrink under mTOR inhibition; regrowth can occur after stopping therapy. The critical intervention window is infancy, before or soon after epileptiform EEG activity and clinical seizures.

## 9. Inheritance and population

Incidence estimates range from approximately 1:5,800 to 1:13,520 live births; recent summaries commonly cite 1:6,000–1:10,000. Overall prevalence is approximately 1:20,000, although ascertainment and age structure matter. A Japanese source cites approximately 1:10,300 live births. (okanishi2024diagnosticflowanalysis pages 1-2, conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2)

Inheritance is autosomal dominant with traditionally high/near-complete penetrance but marked age dependence and variable expressivity. Two thirds of cases are de novo/mosaic, so family history is often negative. Germline/gonadal mosaicism means recurrence risk after an apparently de novo event is above the general-population risk but well below 50% unless parental constitutional disease is established. Anticipation is not recognized; consanguinity is not etiologically important. There is no established sex difference in overall genetic occurrence, although LAM is strongly female predominant. No robust ethnic predisposition has been established; reported geographic differences more likely reflect ascertainment. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8)

TOSCA molecular testing found TSC1 variants in 19.7% and TSC2 in 63.3% of tested participants. A Mexican cohort reported 82% sporadic and 18% familial disease; TSC2 variants predominated. These are referral-cohort proportions, not carrier-frequency estimates. (reynafabian2020firstcomprehensivetsc1tsc2 pages 12-13, kingswood2017tuberoussclerosisregistry pages 2-5)

## 10. Diagnostics

### Clinical criteria

Under the 2021 International TSC Consensus framework, a **pathogenic TSC1 or TSC2 variant is independently diagnostic**. Clinically, definite TSC requires either two major features or one major plus at least two minor features; possible TSC is one major or at least two minor features. Major features include hypomelanotic macules, angiofibromas/fibrous cephalic plaque, ungual fibromas, shagreen patch, multiple retinal hamartomas, multiple cortical tubers/radial migration lines, multiple SENs, SEGA, cardiac rhabdomyoma, LAM, and multiple renal AMLs. Minor features include confetti skin lesions, dental enamel pits, intraoral fibromas, retinal achromic patch, multiple renal cysts, and nonrenal hamartomas. LAM plus AML without another feature should not alone establish definite TSC.

### Baseline evaluation and surveillance

A newly diagnosed person requires brain MRI, EEG and seizure history, comprehensive TAND assessment, renal MRI plus blood pressure/eGFR, dermatologic and dental examination, ophthalmology, cardiac evaluation, and age/sex-appropriate pulmonary assessment. Typical consensus implementation includes brain MRI every 1–3 years in asymptomatic patients under 25 with SEGA risk; renal MRI every 1–3 years lifelong with annual BP/eGFR; annual TAND screening; frequent EEG in asymptomatic infants and urgent prolonged EEG with concerning events; and HRCT/pulmonary-function surveillance for adult women or symptomatic patients. Exact intervals must be individualized.

Real-world evidence shows the value of specialized clinics: Japanese patients with epilepsy were diagnosed faster at TSC clinics than elsewhere (median 11.5 versus 19.0 months; p=0.0379), while renal tumors as the first manifestation produced delays of 23 to as much as 91 months. DOI: https://doi.org/10.1186/s13023-024-03460-y, published December 2024. (okanishi2024diagnosticflowanalysis pages 1-2)

### Genetic testing workflow

1. Sequence **TSC1 and TSC2** with high coverage and validated CNV calling.
2. If negative, perform deletion/duplication testing such as MLPA if not already covered.
3. Reanalyze for splice-region/deep-intronic variants; RNA studies or minigene assays may establish splicing consequences.
4. Investigate low-level mosaicism with ultra-deep sequencing and, where appropriate, affected skin, tumor, buccal/saliva, urine-derived cells, or resected tissue rather than blood alone.
5. WGS is particularly useful for intronic/structural variants and mosaic discovery. WES can identify coding variants but may miss deep intronic variants, some CNVs, and low-level mosaicism.
6. Use CMA when a large deletion/contiguous-gene syndrome is suspected. Karyotype/FISH have limited routine sensitivity. Mitochondrial and repeat-expansion testing are not indicated.

Molecular testing confirms diagnosis and enables cascade/prenatal testing, but a negative result does not exclude clinically definite TSC. (dufneralmeida2024molecularandfunctional pages 11-14, man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8)

### Imaging, electrophysiology, pathology, and biomarkers

MRI is preferred for cortical tubers, SENs/SEGA, and renal lesions; fetal ultrasound/echocardiography detects rhabdomyomas, and fetal MRI may identify brain lesions. EEG is central to presymptomatic infant monitoring. HRCT and pulmonary-function tests evaluate LAM. Echocardiography/ECG assess rhabdomyoma and arrhythmia. There is no validated blood metabolite, proteomic, epigenomic, or liquid-biopsy diagnostic biomarker. Phospho-S6 immunoreactivity is a useful tissue marker of mTORC1 activation but is not disease specific.

Differentials include isolated cardiac rhabdomyoma, sporadic LAM or AML, Birt–Hogg–Dubé syndrome, neurofibromatosis, PTEN/PIK3CA/AKT3/RHEB/DEPDC5-related mTORopathies, focal cortical dysplasia type II, isolated SEGA-like tumors, and autosomal-dominant polycystic kidney disease. (man2024thegeneticsof pages 4-5)

## 11. Outcomes and prognosis

TSC is chronic and not spontaneously curable, but modern surveillance and mTOR-targeted treatment substantially reduce preventable morbidity. No reliable genotype-specific 5- or 10-year survival rate was identified. Leading serious outcomes include status epilepticus/SUDEP, obstructive SEGA/hydrocephalus, renal hemorrhage or CKD, and respiratory disease/LAM. Recent expert synthesis identifies “brain tumours, sudden unexpected death from epilepsy, and respiratory conditions” among leading morbidity/mortality causes; another emphasizes epilepsy and renal complications. (conte2024therapeuticapproachesto pages 1-2, man2024thegeneticsof pages 1-2)

Poorer prognosis is associated with TSC2 rather than TSC1 variants, truncating/critical-domain variants, early infantile spasms, high seizure burden/drug resistance, severe developmental delay, growing SEGA, large/aneurysmal AMLs, impaired renal function, and progressive LAM. Mosaicism or residual-function variants often predict milder disease, but are not sufficiently deterministic to reduce surveillance. (man2024thegeneticsof pages 7-8)

## 12. Treatment

Treatment is manifestation directed and multidisciplinary; genotype establishes pathway biology but currently does not select different approved drugs within TSC2 disease.

### Neurological

- **Vigabatrin** is first-line for TSC-associated infantile spasms and commonly for early focal seizures in infants. Preventive trials reduced or delayed infantile spasms, but PREVeNT did not prevent focal seizures/drug-resistant epilepsy or improve cognition at age 2. Important toxicity is potentially irreversible visual-field loss. Suggested MAXO: antiseizure-agent therapy; EEG surveillance. (conte2024therapeuticapproachesto pages 4-5)
- Other antiseizure medicines are individualized; ketogenic diet, vagus-nerve stimulation, and resective/ablative epilepsy surgery are considered for refractory focal epilepsy. Early surgical evaluation is important where a resectable network exists.
- **Everolimus**, an allosteric mTORC1 inhibitor, is approved as adjunctive treatment for TSC-associated focal/partial-onset seizures in patients aged at least 2 years and for appropriate SEGA and AML. Adverse effects include stomatitis/mouth ulcers, infection/immunosuppression, cytopenias, dyslipidemia, menstrual disturbance, and noninfectious pneumonitis. Suggested MAXO: mTOR-inhibitor therapy; therapeutic-drug monitoring. (conte2024therapeuticapproachesto pages 4-5)
- **Cannabidiol** is approved/authorized as adjunctive TSC seizure therapy, including EU authorization from age 2 in April 2021. Monitor sedation, diarrhea, appetite, liver enzymes, and interactions, particularly with clobazam/valproate. (conte2024therapeuticapproachesto pages 4-5)
- **SEGA:** everolimus for growing lesions not requiring immediate surgery; neurosurgical resection for acute hydrocephalus, mass effect, or suitable definitive treatment. A single-center study found surgery declined from 86% before mTOR inhibitors to 12% afterward, illustrating real-world implementation.

### Renal, pulmonary, skin, and cardiac

- **AML:** everolimus is first-line for asymptomatic but growing AML generally >3 cm; acute hemorrhage is treated with selective arterial embolization plus corticosteroid prophylaxis. Nephron-sparing surgery is preferred when necessary; avoid routine nephrectomy. A 50-adult cohort reported mean AML-volume reduction of 52% with low-dose versus 60% conventional-dose everolimus, with less stomatitis and menstrual irregularity at low dose. Suggested MAXO: renal MRI surveillance, arterial embolization, nephron-sparing surgery. 
- **LAM:** sirolimus is the disease-modifying standard for abnormal/declining lung function or clinically important disease and has been FDA approved since 2015; transplantation is reserved for advanced disease. (conte2024therapeuticapproachesto pages 4-5)
- **Skin:** topical sirolimus/rapamycin, laser, or surgery for facial angiofibromas; surgery/laser for symptomatic ungual fibromas.
- **Cardiac rhabdomyoma:** observation if asymptomatic; antiarrhythmic/supportive care, surgery, or short-course sirolimus/everolimus for severe obstruction or inoperable disease. Prenatal maternal mTOR inhibition remains experimental. (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 4-5)
- Rehabilitation includes developmental intervention, physical/occupational/speech therapy, school supports, behavioral/psychiatric care, and caregiver support.

There is no established CPIC/PharmGKB genotype-guided regimen specific to TSC2. Dosing is instead individualized by age, organ function, interacting drugs, trough concentration, toxicity, and clinical response.

### Active/recent experimental directions

- **TSC-STEPS, NCT05104983:** phase II, randomized triple-masked trial of early sirolimus versus placebo in 64 seizure-free infants aged 0–6 months; primary endpoints are time to seizure by 12 months and severe/serious adverse events. https://clinicaltrials.gov/study/NCT05104983 (NCT05104983 chunk 1)
- **RaRE-TS, NCT05534672:** phase III double-blind rapamycin/placebo trial, estimated n=200, drug-resistant TSC epilepsy; primary efficacy threshold is at least 50% weekly seizure reduction. https://clinicaltrials.gov/study/NCT05534672 (NCT05534672 chunk 1)
- **Astroscape, NCT06392009:** phase Ib/IIa open-label radiprodil, an NR2B-NMDA negative allosteric modulator, in approximately 20 TSC and 10 FCD-II participants. https://clinicaltrials.gov/study/NCT06392009 (NCT06392009 chunk 1)

Gene replacement, CRISPR/base editing, ASO/siRNA, and other RNA therapies remain preclinical; safe restoration of a large tumor-suppressor gene across multiple organs and mosaic lesions is a major challenge.

## 13. Prevention

Primary population prevention is not available. For known familial variants, genetic counseling enables cascade testing, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for monogenic disease. Fetal rhabdomyoma should prompt fetal echocardiography, detailed imaging, parental examination, and TSC1/TSC2 testing.

Secondary prevention consists of early molecular/clinical diagnosis, presymptomatic infant EEG surveillance, prompt seizure treatment, and age-based brain/kidney/lung screening. Preventive vigabatrin evidence is mixed: it can delay/reduce infantile spasms but has not consistently improved two-year cognitive outcome. Prenatal mTOR-inhibitor evidence comprises only three mouse studies and eight papers describing ten treated pregnant women; tumors often shrank, but fetal growth and neurodevelopmental safety remain uncertain. Exact abstract quote: “Three prenatal mouse studies and eight papers reporting on ten pregnant women treated with mTOR inhibitors were identified.” DOI: https://doi.org/10.3390/jcm13216335, published October 23, 2024. (racioppi2024prenatalmtorinhibitors pages 1-2, conte2024therapeuticapproachesto pages 4-5)

Tertiary prevention includes seizure control and SUDEP counseling, SEGA surveillance, renal BP/eGFR and imaging surveillance, AML embolization before catastrophic hemorrhage where indicated, LAM monitoring and smoking/estrogen counseling, vaccination before immunosuppression where appropriate, dental/skin care, and annual TAND screening.

## 14. Other species and natural disease

Orthologous Tsc2 genes are evolutionarily conserved across vertebrates and invertebrates, including **Mus musculus** (NCBI Taxon 10090), **Rattus norvegicus** (10116), **Danio rerio** (7955), and **Drosophila melanogaster** (7227). The RHEB–TOR growth-control mechanism is deeply conserved.

Robust evidence for a prevalent, naturally occurring breed-specific veterinary syndrome directly equivalent to human TSC2-associated multisystem TSC was not identified. Accordingly, no VBO breed term or zoonotic/transmission assertion is justified. TSC is genetic, not infectious, and has no zoonotic potential.

## 15. Model organisms and experimental systems

- **Mouse:** germline homozygous loss is generally embryonic lethal, so heterozygous, conditional, mosaic, or cell-type-specific knockout models are used. Neural progenitor/neuron/astrocyte deletion models reproduce cytomegaly, cortical disorganization, gliosis, seizures, and early mortality; kidney-lineage models produce cystic/tumor phenotypes. Rapalogs often rescue growth and seizure phenotypes, but treatment dependence and species neurodevelopmental differences limit translation.
- **Rat:** the Eker rat carries a Tsc2 defect and develops renal tumors; it is useful for tumor biology and pharmacology but incompletely reproduces human cortical/TAND disease.
- **Zebrafish:** tsc2/mTORopathy models permit live developmental imaging and medium-throughput antiseizure/drug screening. A 2023 review emphasizes zebrafish as translational models for cortical-malformation-associated, treatment-resistant epilepsy, while recognizing that fish cannot reproduce the full human multisystem and cognitive phenotype. DOI: https://doi.org/10.3390/ijms24021530, published January 2023. (abreu2023developingnovelexperimental pages 3-4)
- **Drosophila/yeast/C. elegans:** powerful for conserved TOR growth/autophagy genetics but anatomically remote from human cortical, renal, and pulmonary disease.
- **Human cellular systems:** TSC2-null or patient-derived cells, CRISPR-isogenic iPSCs, 2D neurons/astrocytes, cortical organoids, renal organoids, and lesion-derived cultures support variant testing and drug discovery. The 2024 cortical-organoid study is notable for longitudinal single-cell/multi-omic and electrophysiological characterization, but remains a preprint and lacks immune, vascular, endocrine, and whole-organ pharmacokinetic context. (niu2024longitudinalmultiomicsreveals pages 1-6)

## Evidence limitations and expert interpretation

1. The disease entry is gene-specific, but most frequency and treatment evidence is from mixed TSC1/TSC2 cohorts; those figures should not be stored as TSC2-only penetrance estimates.
2. TSC2 generally predicts more severe disease, but intra- and interfamilial variability is too large for deterministic counseling. Expert reviews emphasize domain, residual transcript, mosaic fraction, and second-hit context rather than gene name alone. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 7-8)
3. No validated environmental cause, protective allele, epigenetic diagnostic signature, circulating biomarker, or genotype-specific pharmacogenomic algorithm was identified.
4. TAND, adult natural history, LMIC populations, nonpharmacological interventions, and long-term effects of preventive therapy remain under-studied. In a scoping review, only 10% of 153 cohort studies included interventions and none was nonpharmacological. (vanclooster2022theresearchlandscape pages 1-2)
5. PMID metadata were not consistently exposed by the retrieved full texts. DOIs, publication dates, and URLs are therefore supplied where available rather than inventing PMID values.

References

1. (OpenTargets Search: tuberous sclerosis 2-TSC2): Open Targets Query (tuberous sclerosis 2-TSC2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (conte2024therapeuticapproachesto pages 1-2): Elena Conte, Brigida Boccanegra, Giorgia Dinoi, Michael Pusch, Annamaria De Luca, Antonella Liantonio, and Paola Imbrici. Therapeutic approaches to tuberous sclerosis complex: from available therapies to promising drug targets. Biomolecules, 14:1190, Sep 2024. URL: https://doi.org/10.3390/biom14091190, doi:10.3390/biom14091190. This article has 22 citations.

3. (man2024thegeneticsof pages 1-2): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 52 citations.

4. (man2024thegeneticsof pages 7-8): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 52 citations.

5. (racioppi2024prenatalmtorinhibitors pages 1-2): Giacomo Racioppi, Martina Proietti Checchi, Giorgia Sforza, Alessandra Voci, Luigi Mazzone, Massimiliano Valeriani, and Romina Moavero. Prenatal mtor inhibitors in tuberous sclerosis complex: current insights and future directions. Journal of Clinical Medicine, 13:6335, Oct 2024. URL: https://doi.org/10.3390/jcm13216335, doi:10.3390/jcm13216335. This article has 10 citations.

6. (man2024thegeneticsof pages 4-5): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 52 citations.

7. (feliciano2020theneurodevelopmentalpathogenesis pages 1-2): David M. Feliciano. The neurodevelopmental pathogenesis of tuberous sclerosis complex (tsc). Frontiers in Neuroanatomy, Jul 2020. URL: https://doi.org/10.3389/fnana.2020.00039, doi:10.3389/fnana.2020.00039. This article has 82 citations.

8. (dufneralmeida2024molecularandfunctional pages 11-14): Luiz Gustavo Dufner-Almeida, Laís F. M. Cardozo, Mariana R. Schwind, Danielly Carvalho, Juliana Paula G. Almeida, Andrea Maria Cappellano, Thiago G. P. Alegria, Santoesha Nanhoe, Mark Nellist, Maria Rita Passos-Bueno, Silvana Chiavegatto, Nasjla S. Silva, Sérgio Rosemberg, Ana Paula A. Pereira, Sérgio Antônio Antoniuk, and Luciana A. Haddad. Molecular and functional assessment of tsc1 and tsc2 in individuals with tuberous sclerosis complex. Genes, 15:1432, Nov 2024. URL: https://doi.org/10.3390/genes15111432, doi:10.3390/genes15111432. This article has 11 citations.

9. (kingswood2017tuberoussclerosisregistry pages 2-5): John C. Kingswood, Guillaume B. d’Augères, Elena Belousova, José C. Ferreira, Tom Carter, Ramon Castellana, Vincent Cottin, Paolo Curatolo, Maria Dahlin, Petrus J. de Vries, Martha Feucht, Carla Fladrowski, Gabriella Gislimberti, Christoph Hertzberg, Sergiusz Jozwiak, John A. Lawson, Alfons Macaya, Rima Nabbout, Finbar O’Callaghan, Mirjana P. Benedik, Jiong Qin, Ruben Marques, Valentin Sander, Matthias Sauter, Yukitoshi Takahashi, Renaud Touraine, Sotiris Youroukos, Bernard Zonnenberg, and Anna C. Jansen. Tuberous sclerosis registry to increase disease awareness (tosca) – baseline data on 2093 patients. Orphanet Journal of Rare Diseases, Jan 2017. URL: https://doi.org/10.1186/s13023-016-0553-5, doi:10.1186/s13023-016-0553-5. This article has 310 citations and is from a peer-reviewed journal.

10. (kingswood2017tuberoussclerosisregistry pages 1-2): John C. Kingswood, Guillaume B. d’Augères, Elena Belousova, José C. Ferreira, Tom Carter, Ramon Castellana, Vincent Cottin, Paolo Curatolo, Maria Dahlin, Petrus J. de Vries, Martha Feucht, Carla Fladrowski, Gabriella Gislimberti, Christoph Hertzberg, Sergiusz Jozwiak, John A. Lawson, Alfons Macaya, Rima Nabbout, Finbar O’Callaghan, Mirjana P. Benedik, Jiong Qin, Ruben Marques, Valentin Sander, Matthias Sauter, Yukitoshi Takahashi, Renaud Touraine, Sotiris Youroukos, Bernard Zonnenberg, and Anna C. Jansen. Tuberous sclerosis registry to increase disease awareness (tosca) – baseline data on 2093 patients. Orphanet Journal of Rare Diseases, Jan 2017. URL: https://doi.org/10.1186/s13023-016-0553-5, doi:10.1186/s13023-016-0553-5. This article has 310 citations and is from a peer-reviewed journal.

11. (kingswood2017tuberoussclerosisregistry pages 8-10): John C. Kingswood, Guillaume B. d’Augères, Elena Belousova, José C. Ferreira, Tom Carter, Ramon Castellana, Vincent Cottin, Paolo Curatolo, Maria Dahlin, Petrus J. de Vries, Martha Feucht, Carla Fladrowski, Gabriella Gislimberti, Christoph Hertzberg, Sergiusz Jozwiak, John A. Lawson, Alfons Macaya, Rima Nabbout, Finbar O’Callaghan, Mirjana P. Benedik, Jiong Qin, Ruben Marques, Valentin Sander, Matthias Sauter, Yukitoshi Takahashi, Renaud Touraine, Sotiris Youroukos, Bernard Zonnenberg, and Anna C. Jansen. Tuberous sclerosis registry to increase disease awareness (tosca) – baseline data on 2093 patients. Orphanet Journal of Rare Diseases, Jan 2017. URL: https://doi.org/10.1186/s13023-016-0553-5, doi:10.1186/s13023-016-0553-5. This article has 310 citations and is from a peer-reviewed journal.

12. (vanclooster2022theresearchlandscape pages 1-2): Stephanie Vanclooster, Stacey Bissell, Agnies M. van Eeghen, Nola Chambers, Liesbeth De Waele, Anna W. Byars, Jamie K. Capal, Sebastián Cukier, Peter Davis, Jennifer Flinn, Sugnet Gardner-Lubbe, Tanjala Gipson, Tosca-Marie Heunis, Dena Hook, J. Christopher Kingswood, Darcy A. Krueger, Aubrey J. Kumm, Mustafa Sahin, Eva Schoeters, Catherine Smith, Shoba Srivastava, Megumi Takei, Robert Waltereit, Anna C. Jansen, and Petrus J. de Vries. The research landscape of tuberous sclerosis complex–associated neuropsychiatric disorders (tand)—a comprehensive scoping review. Journal of Neurodevelopmental Disorders, Feb 2022. URL: https://doi.org/10.1186/s11689-022-09423-3, doi:10.1186/s11689-022-09423-3. This article has 48 citations and is from a peer-reviewed journal.

13. (okanishi2024diagnosticflowanalysis pages 1-2): Tohru Okanishi, Ikuo Fujimori, Mariko Yamada, Takumi Tajima, Mari Wataya-Kaneda, Kuniaki Seyama, and Takashi Hatano. Diagnostic flow analysis of tuberous sclerosis complex in japan: a retrospective claims database study. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03460-y, doi:10.1186/s13023-024-03460-y. This article has 3 citations and is from a peer-reviewed journal.

14. (conte2024therapeuticapproachesto pages 4-5): Elena Conte, Brigida Boccanegra, Giorgia Dinoi, Michael Pusch, Annamaria De Luca, Antonella Liantonio, and Paola Imbrici. Therapeutic approaches to tuberous sclerosis complex: from available therapies to promising drug targets. Biomolecules, 14:1190, Sep 2024. URL: https://doi.org/10.3390/biom14091190, doi:10.3390/biom14091190. This article has 22 citations.

15. (NCT05104983 chunk 1): Darcy Krueger. Stopping TSC Onset and Progression 2B: Sirolimus TSC Epilepsy Prevention Study. Darcy Krueger. 2021. ClinicalTrials.gov Identifier: NCT05104983

16. (NCT05534672 chunk 1): Katarzyna Kotulska. Placebo Controlled Study to Assess the Efficacy and Safety of Rapamycin in Drug Resistant Epilepsy Associated With Tuberous Sclerosis Complex. Katarzyna Kotulska. 2023. ClinicalTrials.gov Identifier: NCT05534672

17. (NCT06392009 chunk 1):  Astroscape: A Study of Radiprodil on Safety, Tolerability, Pharmacokinetics, and Effect on Seizures and Behavioral Symptoms in Patients With TSC or FCD Type II. GRIN Therapeutics, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06392009

18. (niu2024longitudinalmultiomicsreveals pages 1-6): Weibo Niu, Shaojun Yu, Xiangru Li, Zhen Wang, Rui Chen, Christina Michalski, Arman Jahangiri, Youssef Zohdy, Joshua J Chern, Ted J Whitworth, Jianjun Wang, Jie Xu, Ying Zhou, Zhaohui Qin, Bingshan Li, Michael J Gambello, Junmin Peng, and Zhexing Wen. Longitudinal multi-omics reveals pathogenic <i>tsc2</i> variants disrupt developmental trajectories of human cortical organoids derived from tuberous sclerosis complex. BioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.07.617121, doi:10.1101/2024.10.07.617121. This article has 6 citations.

19. (abreu2023developingnovelexperimental pages 3-4): Murilo S. de Abreu, Konstantin A. Demin, Maria M. Kotova, Foad Mirzaei, Sanobar Shariff, Burhan Kantawala, Ksenia V. Zakharchenko, Tatiana O. Kolesnikova, Karen Dilbaryan, Artem Grigoryan, Konstantin B. Yenkoyan, and Allan V. Kalueff. Developing novel experimental models of m-toropathic epilepsy and related neuropathologies: translational insights from zebrafish. Jan 2023. URL: https://doi.org/10.3390/ijms24021530, doi:10.3390/ijms24021530. This article has 11 citations.

20. (reynafabian2020firstcomprehensivetsc1tsc2 pages 12-13): Miriam E. Reyna-Fabián, Nancy L. Hernández-Martínez, Miguel A. Alcántara-Ortigoza, Jorge T. Ayala-Sumuano, Sergio Enríquez-Flores, José A. Velázquez-Aragón, Alfredo Varela-Echavarría, Carlos G. Todd-Quiñones, and Ariadna González-del Angel. First comprehensive tsc1/tsc2 mutational analysis in mexican patients with tuberous sclerosis complex reveals numerous novel pathogenic variants. Scientific Reports, Apr 2020. URL: https://doi.org/10.1038/s41598-020-62759-5, doi:10.1038/s41598-020-62759-5. This article has 43 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Tuberous_Sclerosis_2-deep-research-falcon_artifacts/artifact-00.md)