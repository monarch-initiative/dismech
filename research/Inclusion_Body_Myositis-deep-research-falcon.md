---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T15:35:44.209063'
end_time: '2026-07-30T15:48:22.646034'
duration_seconds: 758.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inclusion Body Myositis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Inclusion_Body_Myositis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inclusion Body Myositis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Inclusion Body Myositis** covering all of the
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
- **Disease Name:** Inclusion Body Myositis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Inclusion Body Myositis** covering all of the
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


# Inclusion Body Myositis: Disease Characteristics Research Report

## Scope and evidence standard

This report concerns **sporadic inclusion body myositis (sIBM)**—hereafter IBM—not hereditary inclusion-body myopathies. Evidence is principally aggregated disease-level information from peer-reviewed cohorts, trials, reviews, and ClinicalTrials.gov, not individual EHR records. Recent 2023–2024 human tissue, single-nucleus, spatial-transcriptomic, and multi-omics studies are prioritized. Where a PMID was not present in the retrieved record, the DOI and URL are supplied rather than an unverified PMID.

The following table provides a compact knowledge-base summary; details and evidence qualifications follow.

| Domain | Key facts for knowledge base | Suggested ontology terms | Evidence boundaries / notes |
|---|---|---|---|
| Identity / ontology | Inclusion body myositis (IBM), often specified as sporadic inclusion body myositis (sIBM), is an acquired idiopathic inflammatory myopathy of older adults with slowly progressive, asymmetric weakness, especially of deep finger flexors and quadriceps; MONDO identifier supported in retrieved evidence: **MONDO:0007827**; hereditary inclusion-body myopathies are distinct entities and should not be merged with sIBM (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2, OpenTargets Search: inclusion body myositis, nagy2023inclusionbodymyositis pages 5-6) | MONDO:0007827; MeSH/ICD/Orphanet: not established in retrieved evidence; distinguish from GNE myopathy, VCP-related inclusion body myopathy, MYH2- and LAMA2-related hereditary IBM forms (nagy2023inclusionbodymyositis pages 5-6) | Do **not** infer unsupported OMIM/Orphanet/ICD identifiers from this evidence set; Open Targets association list includes GNE/MYH2/ACVR2B but does not establish causality for sporadic IBM (OpenTargets Search: inclusion body myositis) |
| Phenotype / natural history | Typical phenotype: painless, asymmetric, slowly progressive weakness affecting quadriceps, deep finger flexors, and often foot extensors; common falls and dysphagia; atypical presentations can include isolated dysphagia, asymptomatic hyper-CKemia, foot drop, axial weakness, and facial/bulbar involvement. Most patients lose ambulation or become wheelchair dependent about **10–15 years** after onset; dysphagia is frequent and worsens quality of life (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2, naddaf2022inclusionbodymyositis pages 6-7) | HPO suggestions: muscle weakness, quadriceps weakness, finger flexor weakness, dysphagia, falls, foot drop, muscle atrophy, reduced hand grip, impaired ambulation | Precise HPO IDs were not provided in retrieved evidence; frequency estimates vary by cohort and diagnostic criteria (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2) |
| Etiology / genetics | Etiology remains unresolved and appears multifactorial, integrating immune, degenerative, mitochondrial, and aging-related mechanisms. Genetic susceptibility is linked mainly to the **HLA/MHC region**; reported associated alleles include **HLA-DRB1*03:01, *01:01, *13:01** and possibly **CCR5**. Rare variants reported in some IBM cohorts include **VCP, SQSTM1, FYCO1**, but these do not establish monogenic causation for sporadic IBM (nagy2023inclusionbodymyositis pages 2-5, nagy2023inclusionbodymyositis pages 5-6) | Gene symbols: HLA-DRB1, CCR5, VCP, SQSTM1, FYCO1; disease distinction terms: hereditary inclusion-body myopathy, GNE myopathy | No firmly established protective genetic or environmental factors were identified in retrieved evidence. Evidence for infectious/environmental triggers is suggestive rather than causal; associations with HIV and hepatitis C support shared immune-exhaustion pathways, not proven causation (nelke2022inclusionbodymyositis pages 1-2) |
| Pathology / mechanisms | Core pathology combines **endomysial CD8+ T-cell inflammation**, invasion of non-necrotic **MHC-I–expressing** fibers, rimmed vacuoles, protein aggregates (**p62/SQSTM1, TDP-43, LC3, amyloid-related material**), mitochondrial abnormalities, ER stress, oxidative/nitrative stress, and impaired autophagy/proteasome function. IFN-γ-driven immune activation is prominent. Recent advanced-technology studies show: selective loss of **type 2 myonuclei/type 2A fibers**, increased **cytotoxic T cells** and **cDC1**, myofiber stress programs (**GADD45A, NORAD**), protein degradation program (**RNF7**), IBM-specific **ACHE** upregulation suggesting functional denervation, and senescent **fibro-adipogenic progenitors (FAPs)** with loss of **collagen XV** and SASP-like features. Mitochondrial DNA abnormalities and metabolic disarrangements are prominent (greenberg2019inclusionbodymyositis pages 10-11, guglielmi2024sporadicinclusionbody pages 1-2, nelke2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 2-5, guglielmi2024sporadicinclusionbody pages 20-22, wischnewski2024celltypemapping pages 1-2, cantosantos2023integratedmultiomicsanalysis pages 2-3, nelke2023senescentfibroadipogenicprogenitors pages 1-2) | GO suggestions: antigen processing and presentation, interferon-gamma signaling, autophagy, proteasomal protein catabolism, mitochondrial organization, oxidative stress response, cellular senescence, complement activation; CL suggestions: CD8-positive alpha-beta T cell, conventional dendritic cell 1, fibro-adipogenic progenitor, skeletal muscle fiber | Causal ordering remains debated: some evidence argues autoimmunity is upstream of degeneration, but refractoriness to immunosuppression and strong cell-autonomous/mitochondrial findings indicate mixed mechanisms (greenberg2019inclusionbodymyositis pages 10-11, guglielmi2024sporadicinclusionbody pages 1-2, nelke2023senescentfibroadipogenicprogenitors pages 1-2) |
| Diagnostics | Diagnosis is clinicopathologic and multimodal: characteristic weakness pattern plus muscle biopsy, CK, EMG, MRI, and supportive serology. Anti-cN1A antibodies have reported **specificity ~90–95%** but variable **sensitivity ~37–76%**. Biopsy features include endomysial inflammation, rimmed vacuoles, T-cell invasion of non-necrotic fibers, ragged-red/COX-negative fibers, p62/TDP-43-positive inclusions, and sometimes tubulofilaments. ENMC-style criteria are emphasized in reviews; MRI and EMG support but are not standalone diagnostic tests (greenberg2019inclusionbodymyositis pages 5-7, nagy2023inclusionbodymyositis pages 1-2, naddaf2022inclusionbodymyositis pages 6-7) | Diagnostic feature suggestions: muscle biopsy finding, electromyography abnormality, creatine kinase increased, anti-cN1A antibody positive, muscle MRI abnormality | Exact ENMC text, CK ranges, MRI pattern details, and differential-diagnosis algorithms were not fully extractable from retrieved evidence. Genetic testing is mainly useful to exclude hereditary IBM mimics rather than confirm sporadic IBM (nagy2023inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 5-6) |
| Epidemiology / prognosis | IBM is the most prevalent inflammatory myopathy of older adults / most common acquired myopathy in people >50 years in cited reviews. Reported prevalence varies widely by geography and case ascertainment: about **5–180 per million** in reviews; among those ≥50 years, estimates cited include **1–182 per million**. Male predominance is roughly **2:1**. Mean age at onset is around **60 years**. Mortality is modestly increased; major causes of death include **aspiration pneumonia** and respiratory complications. Early-onset IBM is rare and severe: in one Swedish population-based study prevalence was **1.2 per million** and incidence **0.12 per million/year**, with median onset age **36** and median survival from diagnosis **14 years** (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2) | Epidemiology annotations: prevalence, incidence, male sex predominance, adult onset, late onset | Prevalence/incidence vary greatly with criteria and whether age-restricted denominators are used. Early-onset IBM should be represented separately from classic late-onset sIBM (guglielmi2024sporadicinclusionbody pages 1-2) |
| Current care | No approved disease-modifying pharmacotherapy is established in retrieved evidence. Real-world management is supportive: monitor swallowing and respiratory status, annual dysphagia screening/history, speech-language pathology referral, adaptive food consistencies/volumes, mobility aids, exercise/physical therapy, and fall prevention. IVIG may give **temporary dysphagia benefit** in selected patients but does not clearly alter overall disease course. Cricopharyngeal dilation or myotomy may help obstructive dysphagia; botulinum toxin has case-series support. Conventional immunosuppressants are generally ineffective (naddaf2022inclusionbodymyositis pages 1-2, naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14) | MAXO-style action suggestions: swallow evaluation, speech therapy, physical therapy, exercise therapy, mobility aid provision, respiratory monitoring, intravenous immunoglobulin administration, cricopharyngeal myotomy, endoscopic dilation | Prevention is mainly **tertiary**: reduce falls, aspiration, malnutrition, and respiratory complications. No evidence-supported primary prevention, population screening, or vaccine strategy was identified (naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14) |
| Experimental therapies | Key interventional programs from retrieved evidence: **sirolimus** (mTOR inhibition/autophagy; phase 3 **NCT04789070**, active-not-recruiting, target enrollment 140; earlier phase 2b missed primary quadriceps endpoint but showed some secondary functional signals), **ABC008 / ulviprubart** (anti-KLRG1 cytotoxic T-cell depletion; phase 1 **NCT04659031** completed; phase 2/3 **NCT05721573** completed, enrollment 272), **arimoclomol** (heat-shock response/proteostasis; large randomized trial **NCT02753530**, publication not directly retrieved here but summarized in review literature as not practice-changing), **bimagrumab** (ACVR2B/myostatin pathway; **NCT01925209**, **NCT02573467**, failed primary 6MWT endpoint despite lean-mass effects), **phenylbutyrate** (**NCT04421677**), blood-flow restricted exercise (**NCT02317094**), adipose-derived regenerative/cell therapies (**NCT04975841**, **NCT05032131**), and withdrawn REGN2477+REGN1033 (**NCT03710941**) (guglielmi2024sporadicinclusionbody pages 19-20, guglielmi2024sporadicinclusionbody pages 18-19, naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14) | Trial/target suggestions: ACVR2B, KLRG1, mTOR signaling, heat-shock response, autophagy modulation, cell therapy | Many trials remain negative, incomplete, or unpublished in full within retrieved evidence. No therapy can yet be described as established standard disease-modifying care for sporadic IBM (guglielmi2024sporadicinclusionbody pages 19-20, naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14) |


*Table: Compact evidence table for sporadic inclusion body myositis covering identity, phenotype, mechanisms, diagnostics, prognosis, and treatments. It highlights quantitative findings, ontology suggestions, and key evidence limits without inventing unsupported identifiers.*

## 1. Disease information

IBM is an acquired, chronic, progressive inflammatory-degenerative skeletal-muscle disease. Its characteristic phenotype is painless, frequently asymmetric weakness of the **deep finger flexors and knee extensors**, often accompanied by quadriceps atrophy, falls, and dysphagia. It usually begins after age 45–50 and is the most prevalent acquired inflammatory myopathy of older adults. Unlike most other idiopathic inflammatory myopathies, it is poorly responsive to conventional immunosuppression. (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2)

**Names and identifiers**

- Preferred name: inclusion body myositis.
- Synonyms: sporadic inclusion body myositis, sIBM, IBM; older literature sometimes uses “sporadic inflammatory inclusion-body myositis.”
- **MONDO:0007827**, supported by the retrieved Open Targets disease mapping. (OpenTargets Search: inclusion body myositis)
- MeSH, Orphanet, OMIM, ICD-10, and ICD-11 identifiers were not directly verified in the retrieved primary text and should be imported only after validation against the current source databases. IBM should not be conflated with GNE myopathy or VCP-, MYH2-, LAMA2-, SQSTM1-, or HNRNPA2B1-related hereditary inclusion-body disorders. (OpenTargets Search: inclusion body myositis, nagy2023inclusionbodymyositis pages 5-6)

A concise 2024 description is: “slowly progressive asymmetrical muscle weakness, predominantly affecting the quadriceps, deep finger flexors, and foot extensors.” [Guglielmi et al., February 2024, DOI/URL: https://doi.org/10.3390/ijms25052742]. (guglielmi2024sporadicinclusionbody pages 1-2)

## 2. Etiology and risk factors

### Causal model

The initiating cause is unknown. Current expert interpretation is a multifactorial interaction among age-related susceptibility, adaptive autoimmunity, myofiber stress, defective proteostasis/autophagy, mitochondrial dysfunction, and tissue-resident stromal-cell abnormalities. Whether immune injury or cell-autonomous degeneration is the first event remains disputed. The strong HLA signal and clonally expanded cytotoxic T cells support an upstream autoimmune component; treatment refractoriness and persistent senescent/degenerative programs indicate that downstream autonomous mechanisms can maintain disease. (greenberg2019inclusionbodymyositis pages 10-11, guglielmi2024sporadicinclusionbody pages 1-2, nagy2023inclusionbodymyositis pages 2-5, nelke2023senescentfibroadipogenicprogenitors pages 1-2)

### Genetic susceptibility—not Mendelian causation

IBM has **no established single causal gene or Mendelian inheritance pattern**. The strongest association is in the HLA/MHC region; an Immunochip study of 2,566 European idiopathic inflammatory-myopathy cases found genome-wide-significant MHC association, with reported IBM-associated alleles including **HLA-DRB1*03:01, HLA-DRB1*01:01, and HLA-DRB1*13:01**. CCR5 and rare variants in proteostasis/autophagy genes such as **VCP, SQSTM1, and FYCO1** have been reported, but none is a validated monogenic explanation for ordinary sIBM. (nagy2023inclusionbodymyositis pages 2-5, nagy2023inclusionbodymyositis pages 5-6)

Open Targets lists GNE, MYH2, and ACVR2B under the broad IBM label, but the retrieved records contain no causal genetic evidence for GNE or MYH2 in sporadic IBM. GNE and MYH2 are principally relevant to inherited mimics, whereas ACVR2B is a therapeutic target studied with bimagrumab. (OpenTargets Search: inclusion body myositis)

### Demographic and environmental factors

- **Age** is the strongest established risk context: mean onset is approximately 60 years.
- **Male sex** is associated with roughly twice the frequency of disease.
- Familial sIBM is exceptional; family history should prompt reconsideration of a hereditary myopathy.
- HIV and hepatitis C have been associated with IBM-like disease and premature immune-cell exhaustion, but neither is established as a general cause of sIBM. No toxin, occupation, smoking pattern, diet, alcohol exposure, or other lifestyle factor has reproducibly been shown to cause IBM. (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, nelke2022inclusionbodymyositis pages 1-2)

### Protective factors and gene–environment interaction

No validated genetic protective allele, diet, exposure, drug, vaccination, or behavioral intervention prevents IBM. Gene–environment interaction remains hypothetical: HLA-mediated antigen presentation may interact with aging, chronic immune stimulation, mitochondrial damage, or infection, but no quantitative interaction model has been established. Absence of evidence should not be encoded as evidence of no interaction.

## 3. Phenotypes

| Phenotype | Character and course | Frequency/severity evidence | Suggested HPO annotation |
|---|---|---|---|
| Finger-flexor weakness/atrophy | Painless, distal upper-limb, often asymmetric; impaired grip and fine hand use | Defining/common phenotype | Finger flexor weakness; distal upper-limb muscle weakness; muscle atrophy |
| Quadriceps/knee-extensor weakness | Progressive proximal lower-limb weakness; difficulty rising, stairs, knee buckling | Defining/common; major cause of falls and loss of ambulation | Quadriceps weakness; proximal lower-limb weakness |
| Falls and gait impairment | Progressive; may precede diagnosis | Common; wheelchair dependence usually follows in 10–15 years | Frequent falls; abnormal gait; impaired mobility |
| Dysphagia | Predominantly pharyngeal; can be presenting or isolated; aspiration risk | Common, clinically important, and associated with premature mortality | Dysphagia; oropharyngeal dysphagia; aspiration |
| Foot drop | Distal lower-limb involvement, sometimes atypical presentation | Less common | Foot dorsiflexor weakness; foot drop |
| Axial, neck, facial, or bulbar weakness | Usually later or atypical | Uncommon/variable | Axial muscle weakness; neck muscle weakness; facial weakness |
| Hyper-CKemia | Usually modest; occasionally asymptomatic presentation | Variable | Elevated serum creatine kinase |
| Respiratory complications | Often secondary to aspiration or advanced neuromuscular weakness | Important mortality driver rather than usual initial phenotype | Respiratory insufficiency; recurrent aspiration pneumonia |

These phenotype assignments are supported by recent clinical reviews describing asymmetric finger-flexor/quadriceps weakness, foot-extensor involvement, dysphagia, and atypical axial or bulbar presentations. (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2)

Quality of life deteriorates through loss of grip, stair climbing, transfers, independent ambulation, safe oral intake, and social participation. A 2024 analysis of 150 trial participants found mean IBM Functional Rating Scale (IBMFRS) 27.4±4.6; a decline of at least two points represented meaningful deterioration. IBMFRS showed adequate internal consistency (α=0.79) and excellent test–retest reliability (ICC 0.84–0.87). [Salam et al., July 2024, https://doi.org/10.1136/jnnp-2024-333617].

## 4. Genetic and molecular information

### Causal variants and chromosomal abnormalities

No pathogenic germline variant, somatic mutation, recurrent chromosomal abnormality, copy-number change, or repeat expansion defines sIBM. Consequently, ACMG variant classification, carrier frequency, penetrance, anticipation, germline mosaicism, founder effects, and prenatal testing are **not applicable to typical sIBM**.

Hereditary mimics include:

- **GNE**—GNE myopathy, OMIM 608209 in the retrieved review;
- **VCP**—multisystem proteinopathy/inclusion-body myopathy with Paget disease and frontotemporal degeneration;
- **MYH2**—myopathy with congenital joint contractures, OMIM 605637 in the retrieved review;
- **LAMA2**—a reported hereditary inclusion-body phenotype with leukoencephalopathy;
- **SQSTM1, HNRNPA2B1**, and related multisystem proteinopathy genes in appropriate syndromic presentations. (OpenTargets Search: inclusion body myositis, nagy2023inclusionbodymyositis pages 5-6)

### Modifiers and epigenetics

HLA alleles may modify susceptibility and phenotype, but validated severity-modifier genes are lacking. Disease-specific DNA-methylation, histone-modification, or chromatin biomarkers are not sufficiently established for clinical annotation. The recent evidence base is predominantly transcriptomic rather than epigenomic.

## 5. Environmental information

No reproducible causal toxin, radiation exposure, pollutant, occupational agent, dietary exposure, smoking pattern, or alcohol association is established. Chronic HIV or HCV infection may generate IBM-like muscle disease through persistent antigenic stimulation and senescent/exhausted CD8 T-cell biology, but this is association and mechanistic analogy, not proof that these pathogens cause ordinary IBM. (nelke2022inclusionbodymyositis pages 1-2)

Exercise should not be classified as a primary protective exposure. Once IBM is present, supervised resistance/aerobic programs appear safe and may improve strength or conditioning, although consistent mobility improvement has not been demonstrated. (guglielmi2024sporadicinclusionbody pages 19-20)

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream susceptibility:** aging muscle plus HLA-mediated immune susceptibility and an unidentified initiating antigen or stressor.
2. **Adaptive immune activation:** clonally expanded, terminally differentiated CD8+CD28−/CD57+/KLRG1+ cytotoxic T cells accumulate in endomysium and invade non-necrotic fibers.
3. **IFN-γ/MHC-I loop:** IFN-γ promotes myofiber MHC-I expression, antigen presentation, ER stress, and further cytotoxic recognition; perforin and granzymes contribute to injury.
4. **Cell-autonomous amplification:** oxidative/nitrative and ER stress, impaired ubiquitin–proteasome activity, defective autophagy/mitophagy, and mitochondrial DNA damage impair protein and organelle turnover.
5. **Degeneration:** rimmed vacuoles and aggregates containing p62/SQSTM1, TDP-43, LC3, VCP, and other proteins accumulate; type-2 fibers are selectively lost, denervation-like programs emerge, and muscle is replaced by fat/connective tissue.
6. **Clinical expression:** finger-flexor and quadriceps weakness, falls, loss of hand function and ambulation, and pharyngeal weakness causing dysphagia and aspiration. (greenberg2019inclusionbodymyositis pages 10-11, guglielmi2024sporadicinclusionbody pages 1-2, nagy2023inclusionbodymyositis pages 2-5, wischnewski2024celltypemapping pages 1-2)

In human biopsy material, invasion of non-necrotic fibers is reported to be about eight times more frequent than amyloid-containing fibers, supporting the expert view that immune injury can precede visible aggregation. Nonetheless, the autoimmune-first model is not proven universally. (greenberg2019inclusionbodymyositis pages 10-11)

### Mitochondria and metabolism

IBM muscle has COX-deficient/ragged-red fibers, mtDNA deletions and duplications, impaired mitophagy, and oxidative stress. One synthesis reported median mtDNA heteroplasmy around 10% in IBM versus 1% in controls, with broader ranges of 1–35% versus 0.2–3%. These abnormalities may be downstream of chronic inflammation but can themselves release danger signals and perpetuate non-apoptotic injury and inflammation. (nelke2022inclusionbodymyositis pages 1-2)

### Autoantibodies

Anti-cytosolic 5′-nucleotidase 1A (**anti-cN1A**, also NT5C1A/Mup44) occurs in up to approximately 60% of cases, but it is neither sufficiently sensitive nor uniquely specific to establish diagnosis or mechanism. Its pathogenic importance remains uncertain. (guglielmi2024sporadicinclusionbody pages 1-2, nagy2023inclusionbodymyositis pages 2-5, greenberg2019inclusionbodymyositis pages 5-7)

### 2023–2024 advanced profiling

- **Wischnewski et al., Nature Aging, June 2024:** snRNA-seq of quadriceps from 8 IBM, 4 immune-mediated necrotizing myopathy, and 7 controls generated 93,345 nuclei; spatial transcriptomics added 7,462 spots. IBM showed selective type-2 myonuclear loss, increased cytotoxic T cells and conventional type-1 dendritic cells, GADD45A/NORAD stress programs, RNF7-associated protein degradation, p62 aggregates, and IBM-specific ACHE upregulation consistent with functional denervation. https://doi.org/10.1038/s43587-024-00645-9. (wischnewski2024celltypemapping pages 1-2)
- **Nelke et al., Acta Neuropathologica, September 2023:** biopsies from 16 IBM, 16 controls, and 16 necrotizing-myopathy patients identified fibro-adipogenic progenitors—not myofibers—as the principal senescent population. IBM FAPs expressed p21, β-galactosidase activity, inflammatory secretory programs, and lost collagen XV required for myofiber integrity and neuromuscular-junction support. https://doi.org/10.1007/s00401-023-02637-2. (nelke2023senescentfibroadipogenicprogenitors pages 1-2)
- **Cantó-Santos et al., Antioxidants, August 2023:** multi-compartment RNA/metabolite profiling included saliva, urine, plasma, fibroblasts, and muscle. It found respiratory-chain/oxidative-stress abnormalities and proposed urinary L-pyroglutamic plus orotic acid as a 100%-sensitivity/100%-specificity signature in a very small discovery cohort; this is exploratory and requires independent validation. https://doi.org/10.3390/antiox12081639. (cantosantos2023integratedmultiomicsanalysis pages 2-3)

Suggested GO terms include interferon-gamma-mediated signaling, antigen processing and presentation, T-cell-mediated cytotoxicity, autophagy, mitophagy, proteasomal protein catabolism, response to oxidative stress, ER stress, cellular senescence, and mitochondrial organization. Suggested CL concepts include skeletal muscle fiber, CD8-positive αβ T cell, conventional dendritic cell type 1, fibro-adipogenic progenitor, macrophage, and satellite cell.

## 7. Anatomical structures affected

The primary organ is **skeletal muscle**. Selective sites include quadriceps/knee extensors, forearm deep finger flexors, ankle dorsiflexors, and pharyngeal/cricopharyngeal musculature; neck and facial muscles can be involved. Disease is generally bilateral but characteristically asymmetric. Cardiac muscle, skin, brain, and peripheral nerves are not primary target organs, although peripheral neuropathy and systemic autoimmune comorbidities occur more often than expected. (naddaf2022inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2)

Suggested UBERON concepts: skeletal musculature, quadriceps femoris, flexor digitorum profundus, tibialis anterior, pharyngeal muscle, and upper esophageal sphincter. Relevant GO cellular components include mitochondrion, lysosome/autolysosome, endoplasmic reticulum, proteasome complex, sarcoplasm, myonucleus, and neuromuscular junction.

## 8. Temporal development

Onset is usually insidious after age 45–50, with diagnostic delay often extending several years. The course is chronic, lifelong, and steadily progressive rather than episodic or relapsing-remitting. Strength declines have been estimated at approximately 4–28% per year across measures and cohorts. Cane-free ambulation is commonly lost around 7.5–10 years, and wheelchair dependence develops around 13–15 years after onset. Spontaneous or durable treatment-induced remission is not characteristic. (nagy2023inclusionbodymyositis pages 1-2, greenberg2019inclusionbodymyositis pages 5-7)

Rare early-onset IBM exists. In a 2023 western-Swedish population study, six patients had median onset at 36 years (range 34–45), quadriceps decline of 1.21±0.2 N or 0.91±0.2% per month, swallowing difficulty in five of six, and median survival from diagnosis of 14 years. [Lindgren et al., July 2023, https://doi.org/10.1007/s00415-023-11878-w].

There is no validated biological “critical period,” but early recognition permits fall prevention, exercise, swallowing surveillance, nutrition intervention, and trial participation before irreversible disability.

## 9. Inheritance and population epidemiology

IBM is sporadic and likely multifactorial/polygenic; classic Mendelian inheritance, penetrance, carrier frequency, anticipation, consanguinity effects, and germline mosaicism do not apply.

Reported prevalence varies from approximately **5–180 per million**, reflecting geography, age structure, ascertainment, and diagnostic criteria. Estimates restricted to people aged ≥50 can range from roughly 1–182 per million. Male:female ratio is approximately 2:1, and mean onset is near 60 years. (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 1-2)

No robust ethnic hierarchy is established. Higher reported prevalence in populations of European ancestry may reflect HLA background, population age, specialist access, and ascertainment. Geographic comparisons should therefore preserve denominator age and diagnostic criteria.

## 10. Diagnostics

### Clinical and laboratory work-up

Diagnosis is multimodal: characteristic weakness pattern, CK, EMG, muscle MRI, serology, and biopsy. CK is generally normal to moderately raised rather than at the very high levels typical of necrotizing autoimmune myopathy. EMG may show mixed myopathic and apparent neurogenic changes and is supportive, not specific. MRI helps identify selective muscle atrophy/fatty replacement and an appropriate biopsy site. (nagy2023inclusionbodymyositis pages 1-2)

### Anti-cN1A

Reported specificity is approximately **90–95%**, but sensitivity varies widely, about **37–76%**. Positive results support IBM only in the appropriate clinical context because anti-cN1A can occur in Sjögren disease, lupus, and other conditions; a negative test does not exclude IBM. (greenberg2019inclusionbodymyositis pages 5-7)

### Biopsy

Canonical findings are:

- endomysial CD8-rich inflammation;
- invasion of non-necrotic MHC-I-positive fibers;
- rimmed vacuoles;
- p62/SQSTM1- and TDP-43-positive sarcoplasmic inclusions;
- COX-negative and ragged-red fibers;
- congophilic aggregates and, on electron microscopy, 15–18-nm tubulofilaments.

Not every feature is present in an early or poorly targeted biopsy. Clinicopathologic criteria incorporating weakness distribution, inflammation, invasion, and rimmed vacuoles have reported sensitivity near 90% and specificity near 96% in the cited synthesis. (greenberg2019inclusionbodymyositis pages 5-7, nagy2023inclusionbodymyositis pages 1-2)

### Differential diagnosis

Important mimics are polymyositis, immune-mediated necrotizing myopathy, antisynthetase/overlap myositis, muscular dystrophies, GNE myopathy, VCP multisystem proteinopathy, myofibrillar myopathy, dysferlinopathy, motor-neuron disease, peripheral neuropathy, sarcoid/granulomatous myopathy, and structural causes of dysphagia. Steroid-refractory “polymyositis,” especially with finger-flexor or quadriceps selectivity, should trigger reassessment for IBM.

### Genetic and omics testing

WES/WGS, panels, mtDNA testing, repeat-expansion testing, CMA, karyotyping, and FISH are not confirmatory tests for typical IBM. A hereditary-myopathy panel or exome/genome analysis is appropriate for early onset, family history, atypical distribution, Paget disease, dementia, motor-neuron disease, congenital contractures, or absent inflammation. Experimental urine metabolomics and tissue transcriptomics are not validated clinical diagnostics. (cantosantos2023integratedmultiomicsanalysis pages 2-3, nagy2023inclusionbodymyositis pages 5-6)

There is no population, newborn, carrier, or cascade screening program.

## 11. Outcome and prognosis

IBM causes severe long-term disability: loss of grip and fine hand function, recurrent falls, impaired transfers, wheelchair dependence, dysphagia, weight loss, aspiration, and caregiver dependence. Most patients do not recover lost strength. Longevity is mildly reduced compared with the general population, with aspiration pneumonia and respiratory complications the leading disease-related causes of death. (naddaf2022inclusionbodymyositis pages 1-2, nagy2023inclusionbodymyositis pages 1-2)

Reported associated conditions include peripheral neuropathy (approximately 2.7-fold greater likelihood), Sjögren syndrome (6.2-fold), and hematologic malignancy including T-cell large-granular-lymphocytic leukemia (3.9-fold), although these associations do not make IBM a conventional paraneoplastic syndrome. (naddaf2022inclusionbodymyositis pages 1-2, damian2022inclusionbodymyositis pages 1-2)

Prognosis is driven primarily by baseline severity, disease duration, rate of lower-limb decline, dysphagia/aspiration, respiratory complications, falls, and nutritional status. No molecular prognostic biomarker is validated. Anti-cN1A has inconsistent phenotype/prognosis associations.

## 12. Treatment

### Current real-world strategy

There is **no established disease-modifying drug**. Conventional glucocorticoids, methotrexate, azathioprine, and most tested biologics generally fail to produce durable functional benefit and can add toxicity. Management is multidisciplinary and supportive. (naddaf2022inclusionbodymyositis pages 1-2, guglielmi2024sporadicinclusionbody pages 19-20, schmidt2018currentclassificationand pages 12-14)

1. **Physical and occupational therapy:** individualized resistance/aerobic exercise, contracture prevention, energy conservation, home modification, orthoses, canes/walkers, wheelchairs, transfer devices, and fall prevention. Exercise studies suggest strength benefit but not consistent mobility improvement. Suggested MAXO: physical therapy, exercise therapy, occupational therapy, assistive-device provision. (guglielmi2024sporadicinclusionbody pages 19-20)
2. **Swallowing care:** at least annual symptom screening, speech-language assessment, videofluoroscopy or endoscopy when indicated, texture/volume adaptation, nutrition support, and aspiration precautions. Temporary benefit from IVIG is reported in selected dysphagic patients, but IVIG does not alter overall progression. Cricopharyngeal dilation, botulinum toxin, or myotomy may help selected obstructive cases; myotomy is irreversible. Suggested MAXO: swallow evaluation, speech therapy, intravenous immunoglobulin administration, endoscopic dilation, botulinum-toxin injection, cricopharyngeal myotomy. (guglielmi2024sporadicinclusionbody pages 18-19, naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14)
3. **Respiratory and general care:** monitor cough, nocturnal hypoventilation, aspiration, weight, and vaccinations appropriate for age and respiratory risk; treat infection promptly.

### Major experimental programs

- **Arimoclomol**, a heat-shock-response/proteostasis amplifier, was tested in a 150-participant, 20-month randomized trial (NCT02753530). The 2023 Lancet Neurology publication did not establish clinically meaningful efficacy; it is not standard care.
- **Bimagrumab**, an anti-ACVR2B antibody intended to increase muscle mass, was tested in NCT01925209 (251 participants) and extension NCT02573467 (211). It increased lean mass in some studies but failed the primary 6-minute-walk functional endpoint, illustrating that hypertrophy does not necessarily restore diseased muscle function. (OpenTargets Search: inclusion body myositis, schmidt2018currentclassificationand pages 12-14)
- **Sirolimus/rapamycin** inhibits mTOR, restrains effector T cells, and promotes autophagy. A 44-person phase 2b study missed its primary quadriceps-strength endpoint but showed signals on selected secondary outcomes. Phase 3 NCT04789070 enrolled approximately 140 and was active, not recruiting, in the retrieved registry snapshot. (naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14)
- **ABC008/ulviprubart** is an anti-KLRG1 monoclonal antibody designed to deplete highly differentiated cytotoxic T cells while sparing broader immunity. Phase 1 NCT04659031 enrolled 19; phase 2/3 NCT05721573 enrolled 272 and was listed completed in the retrieved registry snapshot. Peer-reviewed definitive functional efficacy was not available in the retrieved evidence, so it remains investigational. (guglielmi2024sporadicinclusionbody pages 18-19, naddaf2022inclusionbodymyositis pages 6-7)
- Other approaches include phenylbutyrate (NCT04421677; phase 1, 10 participants), blood-flow-restricted exercise (NCT02317094; 22), adipose-derived regenerative cells (NCT04975841; 9), intramuscular adipose stromal-vascular-fraction therapy (NCT05032131; planned 32), and follistatin gene transfer. None is established therapy. (guglielmi2024sporadicinclusionbody pages 19-20)

No validated IBM pharmacogenomic algorithm, approved gene therapy, RNA therapy, or genotype-guided treatment exists.

## 13. Prevention

**Primary prevention:** unavailable because the initiating cause and modifiable risk factors are unknown. No vaccine, prophylactic medication, dietary strategy, or environmental intervention prevents IBM.

**Secondary prevention:** no asymptomatic population screening is recommended. Earlier clinical recognition—particularly of asymmetric finger-flexor/quadriceps weakness or otherwise unexplained late-life dysphagia—can reduce diagnostic delay and avoid ineffective immunosuppression.

**Tertiary prevention:** the practical priority. It includes fall-risk assessment, mobility aids, supervised exercise, home safety modification, swallowing surveillance, aspiration precautions, nutrition/weight monitoring, respiratory assessment, vaccination according to routine age/risk schedules, and treatment of osteoporosis or infection. These measures prevent complications rather than disease onset. (naddaf2022inclusionbodymyositis pages 6-7, schmidt2018currentclassificationand pages 12-14)

Genetic counseling is indicated only when early onset, family history, Paget disease, dementia, congenital contractures, or another syndromic clue suggests a hereditary inclusion-body myopathy.

## 14. Other species and naturally occurring disease

No well-validated naturally occurring animal disease faithfully reproducing human sporadic IBM was established in the retrieved evidence. Accordingly, no specific companion-animal breed, VBO term, cross-species transmission route, or zoonotic potential should be assigned. IBM is not infectious or zoonotic.

Reports of vacuolar/inclusion-body myopathies in animals should not automatically be treated as orthologous sIBM because they may lack the characteristic human combination of HLA-linked autoimmunity, clonally expanded cytotoxic T cells, selective finger-flexor/quadriceps disease, aging, and proteostatic pathology.

## 15. Model organisms and experimental systems

The absence of a faithful model is a major translational bottleneck. **VCP-mutant mice** reproduce portions of hereditary VCP multisystem proteinopathy but only partially model sporadic IBM and cannot establish sIBM drug efficacy. (guglielmi2024sporadicinclusionbody pages 19-20)

Available reductionist systems include patient muscle biopsies, primary myoblasts, fibroblasts, ex-vivo immune cells, and induced stress/protein-aggregation paradigms. IBM primary myoblast studies have shown that the mitochondria-targeting compound MA-5 can increase ATP and reduce mitochondrial reactive oxygen species, but cultured cells do not recreate chronic HLA-restricted immunity, aging stroma, selective muscle distribution, or years-long progression. (guglielmi2024sporadicinclusionbody pages 20-22)

Recent human-biopsy snRNA-seq and spatial transcriptomics are therefore especially valuable because they preserve disease-relevant cell composition and tissue location, although they are cross-sectional and cannot alone establish causal ordering. (wischnewski2024celltypemapping pages 1-2, nelke2023senescentfibroadipogenicprogenitors pages 1-2)

## Overall expert assessment

IBM is best represented as an **acquired, late-onset, HLA-associated inflammatory-degenerative myopathy without a validated monogenic cause**. The strongest current model is a self-reinforcing circuit in which clonally expanded cytotoxic T cells and IFN-γ/MHC-I signaling initiate or amplify myofiber injury, while proteostasis failure, mitochondrial damage, type-2-fiber vulnerability, functional denervation, and senescent fibro-adipogenic progenitors make the process progressively autonomous and resistant to broad immunosuppression. The most important 2023–2024 advance is the cell-type-resolved demonstration that IBM involves not only lymphocytes and myofibers but also dendritic cells and senescent stromal progenitors. Clinically, early diagnosis and rigorous tertiary prevention remain more effective than any current pharmacotherapy; sirolimus and KLRG1-directed therapy represent rational but still investigational attempts to address the immune–degenerative interface. (greenberg2019inclusionbodymyositis pages 10-11, wischnewski2024celltypemapping pages 1-2, nelke2023senescentfibroadipogenicprogenitors pages 1-2)

References

1. (naddaf2022inclusionbodymyositis pages 1-2): Elie Naddaf. Inclusion body myositis: update on the diagnostic and therapeutic landscape. Frontiers in Neurology, Sep 2022. URL: https://doi.org/10.3389/fneur.2022.1020113, doi:10.3389/fneur.2022.1020113. This article has 73 citations and is from a peer-reviewed journal.

2. (nagy2023inclusionbodymyositis pages 1-2): Sara Nagy, Alaa Khan, Pedro M. Machado, and Henry Houlden. Inclusion body myositis: from genetics to clinical trials. Journal of Neurology, 270:1787-1797, Nov 2023. URL: https://doi.org/10.1007/s00415-022-11459-3, doi:10.1007/s00415-022-11459-3. This article has 32 citations and is from a domain leading peer-reviewed journal.

3. (guglielmi2024sporadicinclusionbody pages 1-2): Valeria Guglielmi, Marta Cheli, Paola Tonin, and Gaetano Vattemi. Sporadic inclusion body myositis at the crossroads between muscle degeneration, inflammation, and aging. International Journal of Molecular Sciences, 25:2742, Feb 2024. URL: https://doi.org/10.3390/ijms25052742, doi:10.3390/ijms25052742. This article has 21 citations.

4. (OpenTargets Search: inclusion body myositis): Open Targets Query (inclusion body myositis, 14 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (nagy2023inclusionbodymyositis pages 5-6): Sara Nagy, Alaa Khan, Pedro M. Machado, and Henry Houlden. Inclusion body myositis: from genetics to clinical trials. Journal of Neurology, 270:1787-1797, Nov 2023. URL: https://doi.org/10.1007/s00415-022-11459-3, doi:10.1007/s00415-022-11459-3. This article has 32 citations and is from a domain leading peer-reviewed journal.

6. (naddaf2022inclusionbodymyositis pages 6-7): Elie Naddaf. Inclusion body myositis: update on the diagnostic and therapeutic landscape. Frontiers in Neurology, Sep 2022. URL: https://doi.org/10.3389/fneur.2022.1020113, doi:10.3389/fneur.2022.1020113. This article has 73 citations and is from a peer-reviewed journal.

7. (nagy2023inclusionbodymyositis pages 2-5): Sara Nagy, Alaa Khan, Pedro M. Machado, and Henry Houlden. Inclusion body myositis: from genetics to clinical trials. Journal of Neurology, 270:1787-1797, Nov 2023. URL: https://doi.org/10.1007/s00415-022-11459-3, doi:10.1007/s00415-022-11459-3. This article has 32 citations and is from a domain leading peer-reviewed journal.

8. (nelke2022inclusionbodymyositis pages 1-2): Christopher Nelke, Felix Kleefeld, Corinna Preusse, Tobias Ruck, and Werner Stenzel. Inclusion body myositis and associated diseases: an argument for shared immune pathologies. Acta Neuropathologica Communications, Jun 2022. URL: https://doi.org/10.1186/s40478-022-01389-6, doi:10.1186/s40478-022-01389-6. This article has 44 citations and is from a peer-reviewed journal.

9. (greenberg2019inclusionbodymyositis pages 10-11): Steven A. Greenberg. Inclusion body myositis: clinical features and pathogenesis. Nature Reviews Rheumatology, 15:257-272, Mar 2019. URL: https://doi.org/10.1038/s41584-019-0186-x, doi:10.1038/s41584-019-0186-x. This article has 338 citations and is from a domain leading peer-reviewed journal.

10. (guglielmi2024sporadicinclusionbody pages 20-22): Valeria Guglielmi, Marta Cheli, Paola Tonin, and Gaetano Vattemi. Sporadic inclusion body myositis at the crossroads between muscle degeneration, inflammation, and aging. International Journal of Molecular Sciences, 25:2742, Feb 2024. URL: https://doi.org/10.3390/ijms25052742, doi:10.3390/ijms25052742. This article has 21 citations.

11. (wischnewski2024celltypemapping pages 1-2): Sven Wischnewski, Thomas Thäwel, Chiseko Ikenaga, Anna Kocharyan, Celia Lerma-Martin, Amel Zulji, Hans-Werner Rausch, David Brenner, Leonie Thomas, Michael Kutza, Brittney Wick, Tim Trobisch, Corinna Preusse, Maximilian Haeussler, Jan Leipe, Albert Ludolph, Angela Rosenbohm, Ahmet Hoke, Michael Platten, Jochen H. Weishaupt, Clemens J. Sommer, Werner Stenzel, Thomas E. Lloyd, and Lucas Schirmer. Cell type mapping of inflammatory muscle diseases highlights selective myofiber vulnerability in inclusion body myositis. Nature Aging, 4:969-983, Jun 2024. URL: https://doi.org/10.1038/s43587-024-00645-9, doi:10.1038/s43587-024-00645-9. This article has 34 citations and is from a peer-reviewed journal.

12. (cantosantos2023integratedmultiomicsanalysis pages 2-3): Judith Cantó-Santos, Laura Valls-Roca, Ester Tobías, Clara Oliva, Francesc Josep García-García, Mariona Guitart-Mampel, Félix Andújar-Sánchez, Anna Esteve-Codina, Beatriz Martín-Mur, Joan Padrosa, Raquel Aránega, Pedro J. Moreno-Lozano, José César Milisenda, Rafael Artuch, Josep M. Grau-Junyent, and Glòria Garrabou. Integrated multi-omics analysis for inferring molecular players in inclusion body myositis. Antioxidants, 12:1639, Aug 2023. URL: https://doi.org/10.3390/antiox12081639, doi:10.3390/antiox12081639. This article has 4 citations.

13. (nelke2023senescentfibroadipogenicprogenitors pages 1-2): Christopher Nelke, Christina B. Schroeter, Lukas Theissen, Corinna Preusse, Marc Pawlitzki, Saskia Räuber, Vera Dobelmann, Derya Cengiz, Felix Kleefeld, Andreas Roos, Benedikt Schoser, Anna Brunn, Eva Neuen-Jacob, Jana Zschüntzsch, Sven G. Meuth, Werner Stenzel, and Tobias Ruck. Senescent fibro-adipogenic progenitors are potential drivers of pathology in inclusion body myositis. Acta Neuropathologica, 146:725-745, Sep 2023. URL: https://doi.org/10.1007/s00401-023-02637-2, doi:10.1007/s00401-023-02637-2. This article has 32 citations and is from a highest quality peer-reviewed journal.

14. (greenberg2019inclusionbodymyositis pages 5-7): Steven A. Greenberg. Inclusion body myositis: clinical features and pathogenesis. Nature Reviews Rheumatology, 15:257-272, Mar 2019. URL: https://doi.org/10.1038/s41584-019-0186-x, doi:10.1038/s41584-019-0186-x. This article has 338 citations and is from a domain leading peer-reviewed journal.

15. (schmidt2018currentclassificationand pages 12-14): Jens Schmidt. Current classification and management of inflammatory myopathies. Journal of Neuromuscular Diseases, 5:109-129, May 2018. URL: https://doi.org/10.3233/jnd-180308, doi:10.3233/jnd-180308. This article has 405 citations and is from a peer-reviewed journal.

16. (guglielmi2024sporadicinclusionbody pages 19-20): Valeria Guglielmi, Marta Cheli, Paola Tonin, and Gaetano Vattemi. Sporadic inclusion body myositis at the crossroads between muscle degeneration, inflammation, and aging. International Journal of Molecular Sciences, 25:2742, Feb 2024. URL: https://doi.org/10.3390/ijms25052742, doi:10.3390/ijms25052742. This article has 21 citations.

17. (guglielmi2024sporadicinclusionbody pages 18-19): Valeria Guglielmi, Marta Cheli, Paola Tonin, and Gaetano Vattemi. Sporadic inclusion body myositis at the crossroads between muscle degeneration, inflammation, and aging. International Journal of Molecular Sciences, 25:2742, Feb 2024. URL: https://doi.org/10.3390/ijms25052742, doi:10.3390/ijms25052742. This article has 21 citations.

18. (damian2022inclusionbodymyositis pages 1-2): Laura Damian, Cristian Cezar Login, Carolina Solomon, Cristina Belizna, Svetlana Encica, Laura Urian, Ciprian Jurcut, Bogdan Stancu, and Romana Vulturar. Inclusion body myositis and neoplasia: a narrative review. International Journal of Molecular Sciences, 23:7358, Jul 2022. URL: https://doi.org/10.3390/ijms23137358, doi:10.3390/ijms23137358. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Inclusion_Body_Myositis-deep-research-falcon_artifacts/artifact-00.md)