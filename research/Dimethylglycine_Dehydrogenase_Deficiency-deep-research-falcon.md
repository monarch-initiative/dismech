---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T13:58:46.995300'
end_time: '2026-05-11T14:13:30.425167'
duration_seconds: 883.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dimethylglycine Dehydrogenase Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
trajectory_id: 0ab9e2d2-7601-4bbe-ba01-e26bfce94cfd
artifact_count: 1
artifacts:
- filename: artifact-00.md
  path: Dimethylglycine_Dehydrogenase_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dimethylglycine Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dimethylglycine Dehydrogenase Deficiency** covering all of the
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
- **Disease Name:** Dimethylglycine Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dimethylglycine Dehydrogenase Deficiency** covering all of the
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


# Dimethylglycine Dehydrogenase Deficiency (DMGDH deficiency; hyperdimethylglycinemia): Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Dimethylglycine dehydrogenase deficiency
- **Category:** Mendelian / inborn error of metabolism (one‑carbon/choline degradation pathway)
- **Key identifier available from retrieved sources:** **OMIM 605850** (reported in mechanistic/structural papers) (augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not identified in the retrieved corpus for this run; these identifiers should be added from external ontology resources during curation (limitation of this tool-run).

## Executive summary
Dimethylglycine dehydrogenase deficiency is an ultra‑rare inborn error of choline catabolism/one‑carbon metabolism caused by loss of function in **DMGDH**, a mitochondrial **FAD- and tetrahydrofolate (THF)**‑dependent enzyme that oxidatively demethylates **N,N‑dimethylglycine (DMG)** to **sarcosine**. The canonical human phenotype is mild and has been described primarily in a **single adult patient**, featuring a **lifelong fish‑like odor**, **muscle fatigue/weakness**, and **persistent creatine kinase (CK) elevation**, with massively increased **DMG** in serum and urine. Diagnosis relies on **targeted metabolite measurement** (historically by **^1H NMR spectroscopy** of urine/serum) and confirmatory **molecular genetic testing** identifying **biallelic DMGDH variants** (e.g., **A326G; p.His109Arg**). Evidence for disease mechanism and variant pathogenicity is strengthened by biochemical/structural characterization of the H109R variant showing marked impairment in substrate affinity/cofactor incorporation and catalytic efficiency. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, mcandrew2008molecularbasisof pages 1-3, moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 1-1)

| Disease name / synonym used | Causal gene | Key reported patient findings (clinical, biochemical, diagnostics) | Key quantitative lab values | Pathogenic variant / frequency | Evidence type |
|---|---|---|---|---|---|
| Dimethylglycine dehydrogenase deficiency; hyperdimethylglycinemia; “defect in dimethylglycine dehydrogenase”; sometimes discussed with fish-odor syndromes because odor was a presenting complaint (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-1, moolenaar2001invivoand pages 89-94) | **DMGDH** (mitochondrial dimethylglycine dehydrogenase) (mcandrew2008molecularbasisof pages 1-3, augustin2016structureandbiochemical pages 1-3) | Single reported index patient: 38-year-old man of African ancestry; fish-like body odor since age 5, worse with stress/exertion; unusual muscle fatigue/weakness; normal intelligence/overall good health; persistent CK elevation. Biochemical hallmark was marked accumulation of dimethylglycine with absent detectable sarcosine. Diagnosis used **1H NMR** of urine/serum, confirmed by **13C NMR**, **GC-MS**, and later **molecular testing**; trimethylaminuria was excluded by fish challenge and low urinary trimethylamine (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 1-1, moolenaar2001invivoand pages 94-98, moolenaar1999defectindimethylglycine pages 1-2, moolenaar1999defectindimethylglycine pages 3-4, moolenaar1999defectindimethylglycine pages 5-5, moolenaar2001invivoand pages 98-101) | Serum DMG **221** vs ref **1–5**; urine DMG **457** and **441 mmol/mol creatinine** vs ref **1–26** (age >2 months); CK **1066 U/L** vs ref **30–270 U/L** (~4× ULN). Urine trimethylamine **<2 mmol/mol creatinine**; trimethylamine N-oxide **55 mmol/mol creatinine** (ref **20–125**) (moolenaar1999defectindimethylglycine pages 4-5, moolenaar2001invivoand pages 94-98, moolenaar1999defectindimethylglycine pages 1-2, moolenaar1999defectindimethylglycine pages 3-4, moolenaar2001invivoand pages 98-101, moolenaar1999defectindimethylglycine media 773767bc) | Homozygous **A326G** causing **H109R (His109Arg)** near flavin attachment site; reported as disease-causing in the index patient (walker2012trimethylaminuriaanddimethylglycine pages 3-5, mcandrew2008molecularbasisof pages 1-3, moolenaar1999defectindimethylglycine pages 1-1) | Human case report / diagnostic discovery study (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 1-1) |
| Dimethylglycine dehydrogenase deficiency (OMIM 605850); mild/non-fatal disorder with DMG accumulation and fish-like odor (augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3) | **DMGDH** (augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3) | Recombinant/structural studies linked H109R to decreased expression, reduced FAD saturation, lower thermal stability, impaired substrate affinity, and lower catalytic efficiency, providing mechanistic support for the patient phenotype of DMG accumulation, muscle fatigue, and odor (mcandrew2008molecularbasisof pages 4-6, mcandrew2008molecularbasisof pages 6-8, augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3) | WT kinetics: Km1 **0.039 ± 0.010 mmol/L**, Km2 **15.4 ± 1.2 mmol/L**; with 4 mmol/L THF, Km2 **1.10 ± 0.55 mmol/L**. H109R: ~**47%** WT bound flavin in one expression system; **27-fold** lower specific activity, **65-fold** higher Km, ~**1800-fold** lower catalytic efficiency in one study; other study reported ~**10-fold** lower catalytic efficiency and **15–25-fold** higher Km (mcandrew2008molecularbasisof pages 4-6, augustin2016structureandbiochemical pages 7-9, mcandrew2008molecularbasisof pages 1-3, augustin2016structureandbiochemical pages 1-3, mcandrew2008molecularbasisof pages 6-8) | **H109R** present in ExAC **58/118,656 alleles (0.049%)**, noted as predominantly in individuals of African descent (augustin2016structureandbiochemical pages 1-3) | Biochemical / structural study (mcandrew2008molecularbasisof pages 4-6, augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3) |
| Dimethylglycine dehydrogenase deficiency in choline-related inherited metabolic disease reviews; very rare / likely autosomal recessive disorder (walker2012trimethylaminuriaanddimethylglycine pages 3-5) | **DMGDH** (walker2012trimethylaminuriaanddimethylglycine pages 3-5) | Chapter/review sources summarize that only one case had been reported at that time; disease blocks choline catabolism, causing major DMG accumulation in plasma/urine; suggested practical diagnosis is raised plasma/urine DMG, ideally sampled when odor present. Proton NMR is emphasized as useful; routine liver biopsy would be needed for enzyme confirmation because activity is not normally detectable in blood cells/fibroblasts. Management suggestions included counseling, dietary choline restriction, avoiding excessive sweating; antibiotics to alter gut flora not indicated; riboflavin alone did not help, and folate plus riboflavin was suggested as a trial (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 5-5) | Plasma DMG increase described as ~**100-fold** and urine increase ~**20-fold**; healthy adult plasma reference **1–5 µmol/L**; urine reference **<26 mmol/mol creatinine** after age 2 months, with higher neonatal values up to ~**550 mmol/mol creatinine** in first 2 months (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 4-5) | Homozygous **A326G / H109R** summarized as causative in the known patient (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-1) | Review / book chapter (walker2012trimethylaminuriaanddimethylglycine pages 3-5) |


*Table: This table condenses the core literature on dimethylglycine dehydrogenase deficiency, including the nomenclature used, the causal gene, the single well-described human case, key quantitative laboratory abnormalities, and the main pathogenic variant with biochemical evidence. It is useful as a quick reference for disease curation and knowledge base population.*

---

## 1. Disease information
### 1.1 What is the disease?
Dimethylglycine dehydrogenase deficiency (also called hyperdimethylglycinemia) is a genetic metabolic disorder in which impaired DMGDH activity blocks the mitochondrial step converting DMG to sarcosine, leading to **marked accumulation of DMG in body fluids** and a **mild clinical phenotype** in the best‑described patient. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-1, moolenaar1999defectindimethylglycine pages 1-2)

### 1.2 Common synonyms / alternative names (from primary literature)
- “Dimethylglycine dehydrogenase deficiency” (walker2012trimethylaminuriaanddimethylglycine pages 3-5, augustin2016structureandbiochemical pages 7-9)
- “Hyperdimethylglycinemia” (used as a descriptor for DMG elevation in the discovery paper) (moolenaar1999defectindimethylglycine pages 1-1)
- “Defect in dimethylglycine dehydrogenase” (title/terminology of original case report) (moolenaar1999defectindimethylglycine pages 1-1)

### 1.3 Evidence source type
The disease description is derived primarily from:
- **Individual human case report/discovery study** using metabolomics/NMR and molecular genetics (moolenaar1999defectindimethylglycine pages 1-1, moolenaar1999defectindimethylglycine pages 1-2)
- **Authoritative chapter-level synthesis** describing rarity, diagnostic approach, and management suggestions (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Biochemical/structural functional studies** of the disease-associated variant (mcandrew2008molecularbasisof pages 1-3, augustin2016structureandbiochemical pages 1-3)

---

## 2. Etiology
### 2.1 Disease causal factors
- **Genetic cause:** Biallelic pathogenic variants in **DMGDH**. The index patient was **homozygous for A326G**, encoding **p.His109Arg (H109R)**. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, mcandrew2008molecularbasisof pages 1-3)
- **Mechanistic cause:** Loss of DMGDH enzymatic function causing failure of DMG demethylation and consequent accumulation of DMG in blood/urine. (augustin2016structureandbiochemical pages 1-3, moolenaar1999defectindimethylglycine pages 1-1)

### 2.2 Risk factors
- **Genetic:** Having biallelic loss‑of‑function or severely hypomorphic variants in DMGDH (autosomal recessive inferred). A chapter review states the disorder is “likely autosomal recessive” and notes “only one case” had been reported at that time. (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Environmental:** No validated environmental risk factors were identified; symptoms (odor) were reported to worsen with **stress/exertion** in the index patient (not a cause, but a trigger/modifier of symptom expression). (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective genetic variants or gene–environment interactions specific to disease penetrance were reported in the retrieved literature. Given the extremely limited case count, these remain unknown.

---

## 3. Phenotypes
### 3.1 Reported human phenotypes (best-described index case)
**Clinical signs/symptoms**
- Fish‑like body odor beginning in childhood (age 5) and persisting into adulthood. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)
- Unusual muscle fatigue and/or mild muscle weakness. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, mcandrew2008molecularbasisof pages 1-3, moolenaar1999defectindimethylglycine pages 1-2)
- Normal intelligence and generally good health otherwise reported in the original case. (moolenaar1999defectindimethylglycine pages 1-2)

**Laboratory abnormalities**
- Markedly increased DMG in serum and urine (quantified in Table 1 of discovery report). (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine media 773767bc)
- Persistently increased serum/plasma creatine kinase (~4× upper limit of normal). (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)

**Phenotype timing and severity**
- **Age of onset:** childhood for odor complaint (age ~5). (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)
- **Course:** chronic/lifelong in the index patient. (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Severity:** described as mild/non‑fatal in later mechanistic literature. (augustin2016structureandbiochemical pages 7-9)

### 3.2 Suggested HPO terms (mapping based on described features)
(These are ontology suggestions for curation; HPO IDs not retrieved in this run.)
- Fishy body odor / abnormal body odor: **Abnormal body odor**
- Fatigue: **Fatigue**
- Muscle weakness: **Muscle weakness**
- Elevated creatine kinase: **Elevated circulating creatine kinase concentration**
- Increased dimethylglycine: **Abnormal circulating metabolite concentration** (specific metabolite annotation may require custom term)

### 3.3 Quantitative phenotype-associated data
Table 1 in the original Clinical Chemistry report provides the key quantitative biochemical phenotype:
- **Serum DMG:** **221** (reported as mmol/L in excerpt) vs reference **1–5** (moolenaar1999defectindimethylglycine pages 4-5)
- **Urine DMG:** **457** and **441 mmol/mol creatinine** vs reference **1–26** (for age >2 months) (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine media 773767bc)
- **Creatine kinase:** **1066 U/L** (ref 30–270 U/L) (moolenaar1999defectindimethylglycine pages 1-2)

**Visual evidence:** Table 1/Figure 5 showing these abnormalities and age-related urine DMG reference distribution are captured as cropped images. (moolenaar1999defectindimethylglycine media 773767bc, moolenaar1999defectindimethylglycine media 214a655b)

### 3.4 Quality of life impact
The index case reported severe psychosocial impact from persistent odor (qualitative description in follow-on NMR paper). (moolenaar2001invivoand pages 94-98)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **DMGDH** encodes mitochondrial dimethylglycine dehydrogenase, a covalently flavinylated enzyme requiring THF. (augustin2016structureandbiochemical pages 1-3, moolenaar1999defectindimethylglycine pages 1-2)

### 4.2 Pathogenic variant(s)
- **Index disease variant:** **c.326A>G; p.His109Arg (H109R)**, homozygous in the reported patient. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, mcandrew2008molecularbasisof pages 1-3)

### 4.3 Functional consequences (variant-level)
Two independent functional analyses support pathogenicity:
- H109R shows reduced flavin incorporation/cofactor saturation, markedly impaired substrate affinity and/or catalytic efficiency, and reduced stability—mechanistic routes to decreased enzymatic flux and DMG accumulation. (mcandrew2008molecularbasisof pages 4-6, augustin2016structureandbiochemical pages 7-9, augustin2016structureandbiochemical pages 1-3)
- Quantitatively, one study reports the H109R mutant as having a **~65‑fold increase in Km** and **~27‑fold decrease in activity**, with overall **~1800‑fold loss in catalytic efficiency** (after accounting for flavination), consistent with a severe hypomorphic/LOF allele. (mcandrew2008molecularbasisof pages 4-6)

### 4.4 Population frequency context
The H109R allele was observed in ExAC at **58/118,656 alleles (0.049%)**, predominantly in individuals of African descent, highlighting that population presence does not exclude pathogenicity for autosomal recessive disease when homozygosity is rare. (augustin2016structureandbiochemical pages 1-3)

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic findings, or chromosomal abnormalities were reported for DMGDH deficiency in the retrieved sources.

---

## 5. Environmental information
No established environmental toxins, lifestyle factors, or infectious triggers are reported as causal. Symptom fluctuation with stress/exertion (odor worsening) is noted in the index case. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Molecular pathway and causal chain
**Upstream:** Dietary choline → betaine → DMG (as part of choline catabolism / methyl group metabolism).

**Core defect:** DMGDH is a mitochondrial **FAD- and THF-dependent** enzyme that demethylates DMG to sarcosine; THF accepts the methyl group (preventing release of formaldehyde). (augustin2016structureandbiochemical pages 1-3)

**Downstream biochemical consequence:** DMGDH deficiency results in **marked accumulation of DMG** in serum and urine, and **absent/undetectable sarcosine** in the original biochemical profile. (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 1-2)

**Clinical consequence (known):** fish‑like odor (likely from volatile DMG), fatigue/weakness, and elevated CK. However, because the phenotype is based on very few individuals, links beyond metabolite accumulation remain uncertain. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 5-5)

### 6.2 Suggested GO biological process / cellular component terms
(ontology suggestions)
- **GO: one‑carbon metabolic process**
- **GO: choline metabolic process / betaine metabolic process**
- **GO: glycine metabolic process**
- **GO cellular component:** mitochondrial matrix (DMGDH is mitochondrial) (augustin2016structureandbiochemical pages 1-3)

### 6.3 Suggested cell types (Cell Ontology)
No specific cell type pathology is described; enzyme is liver‑relevant in catabolism. For curation, consider:
- Hepatocyte (primary site of choline metabolism; inferred, not directly evidenced here)
- Skeletal muscle cell (given CK and fatigue; speculative)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level (evidence-based)
- **Muscle involvement:** suggested by fatigue/weakness and persistently elevated CK. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-2)

### 7.2 Suggested UBERON terms
- Skeletal muscle tissue (UBERON suggestion)
- Liver (UBERON suggestion; diagnostic enzyme assay discussion implies liver relevance) (walker2012trimethylaminuriaanddimethylglycine pages 3-5)

### 7.3 Subcellular localization
- **Mitochondrial enzyme** (matrix-associated) consistent with biochemical characterization. (augustin2016structureandbiochemical pages 1-3)

---

## 8. Temporal development
- **Onset:** childhood for odor (age ~5). (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Course:** chronic/lifelong; no defined staging described. (walker2012trimethylaminuriaanddimethylglycine pages 3-5)

---

## 9. Inheritance and population
### 9.1 Inheritance
- Inferred **autosomal recessive** (chapter source: “likely autosomal recessive”; index patient homozygous). (walker2012trimethylaminuriaanddimethylglycine pages 3-5)

### 9.2 Epidemiology
- Extremely rare; as of the chapter publication, “only one case has been reported.” (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- No robust incidence/prevalence estimates were identified in the retrieved sources.

### 9.3 Population/ancestry
- Index case: described as a man of **African ancestry**. (moolenaar1999defectindimethylglycine pages 1-2)
- H109R allele: enriched in ExAC African ancestry subset. (augustin2016structureandbiochemical pages 1-3)

---

## 10. Diagnostics
### 10.1 Core diagnostic biomarker
- **Elevated DMG in plasma/serum and urine** is the defining biochemical abnormality. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 4-5)

### 10.2 Laboratory methods (real-world implementations)
- **^1H NMR spectroscopy** of urine and serum was a key diagnostic approach in the discovery study; DMG displayed characteristic singlets (2.93 and 3.80 ppm) and was confirmed by spiking experiments. (moolenaar1999defectindimethylglycine pages 4-5)
- **GC‑MS** confirmation can be performed, but the discovery paper notes DMG can be missed by routine organic-acid workflows using solvent extraction (lost during ethyl acetate extraction). (moolenaar1999defectindimethylglycine pages 3-4, walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Fish‑challenge testing** and urinary trimethylamine measures were used to exclude trimethylaminuria in the presenting “fish odor” complaint. (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 3-4)

### 10.3 Enzyme assay
A chapter notes DMGDH activity is not normally detectable in blood cells/fibroblasts, so confirmatory enzyme testing would require **liver tissue (biopsy)**—a major practical limitation. (walker2012trimethylaminuriaanddimethylglycine pages 3-5)

### 10.4 Genetic testing
Confirmatory diagnosis is via **DMGDH sequencing** to identify biallelic pathogenic variants (e.g., A326G/H109R). (moolenaar1999defectindimethylglycine pages 1-1, walker2012trimethylaminuriaanddimethylglycine pages 3-5)

### 10.5 Differential diagnosis
Given the presenting symptom of fish-like odor, differential considerations include trimethylaminuria; DMGDH deficiency can be distinguished by **massively elevated DMG** and low trimethylamine after fish challenge. (moolenaar1999defectindimethylglycine pages 4-5, moolenaar1999defectindimethylglycine pages 3-4)

---

## 11. Outcome / prognosis
- Later biochemical/structural literature describes the disorder as **non‑fatal** and typically **mild**. (augustin2016structureandbiochemical pages 7-9)
- No survival statistics, long-term organ outcomes, or standardized quality-of-life metrics were identified, due to limited case ascertainment.

---

## 12. Treatment
### 12.1 Evidence-based interventions (limited)
No established disease-modifying therapy exists.

**Riboflavin trial (index case):** The original report states the patient received **riboflavin 10 mg/day for 3 months without clinical improvement**. (moolenaar1999defectindimethylglycine pages 3-4)

**Supportive/empiric measures (expert opinion from authoritative chapter):**
- Counseling
- Dietary **choline restriction** and avoidance of excessive sweating (odor management)
- Antibiotics to alter intestinal microflora “not indicated”
- Suggested trial of folate with riboflavin (hypothesis-driven, not proven)
(walker2012trimethylaminuriaanddimethylglycine pages 3-5)

### 12.2 Suggested MAXO terms
(ontology suggestions)
- Dietary modification / dietary choline restriction
- Vitamin supplementation (riboflavin; folate)
- Genetic counseling

### 12.3 Clinical trials
No DMGDH deficiency–specific trials were retrieved.

---

## 13. Prevention
- **Primary prevention:** not applicable in the usual sense for an autosomal recessive condition.
- **Secondary prevention:** early biochemical/genetic diagnosis may reduce psychosocial morbidity by explaining odor and guiding supportive measures. (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- **Genetic counseling:** indicated for families once a causative DMGDH genotype is identified (inferred from AR inheritance and chapter guidance). (walker2012trimethylaminuriaanddimethylglycine pages 3-5)

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were identified in the retrieved sources.

---

## 15. Model organisms / experimental systems
### 15.1 Human protein functional models
Functional evidence is largely derived from recombinant enzyme studies and structural biology (including a reported PDB structure for human DMGDH in one study). (augustin2016structureandbiochemical pages 1-3)

### 15.2 Need for in vivo models
The molecular basis paper notes that additional DMGDH‑deficient humans or an appropriate mouse model would be needed to resolve genotype–phenotype questions. (mcandrew2008molecularbasisof pages 8-8)

---

## Recent developments (prioritizing 2023–2024)
Direct 2023–2024 primary case expansions were not available in the retrievable corpus for this run. As a proxy for “latest research” relevant to real‑world implementation, the most concrete near‑term development is the continued mainstreaming of **broad metabolomics and sequencing** for rare disease diagnosis (with older but still relevant metabolomics evidence in this run). For example, DI‑HRMS metabolomics has been evaluated for inborn errors using dried blood spots and plasma; one limitation noted is that some workflows may fail to recognize DMGDH deficiency depending on feature detection/annotation. (moolenaar2001invivoand pages 98-101)

---

## Key primary sources (URLs and publication dates)
- Moolenaar SH et al. **“Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: NMR spectroscopy study.”** *Clinical Chemistry* (Apr **1999**). https://doi.org/10.1093/clinchem/45.4.459 (moolenaar1999defectindimethylglycine pages 1-1)
- McAndrew R et al. **“Molecular basis of dimethylglycine dehydrogenase deficiency associated with pathogenic variant H109R.”** *Journal of Inherited Metabolic Disease* (Oct **2008**). https://doi.org/10.1007/s10545-008-0999-2 (mcandrew2008molecularbasisof pages 1-3)
- Walker V, Wevers RA. **“Trimethylaminuria and Dimethylglycine Dehydrogenase Deficiency.”** In *Inborn Metabolic Diseases* (Jan **2012**). https://doi.org/10.1007/978-3-540-28785-8_31 (walker2012trimethylaminuriaanddimethylglycine pages 3-5)
- Augustin P et al. **“Structure and biochemical properties of recombinant human dimethylglycine dehydrogenase and comparison to the disease-related H109R variant.”** *FEBS Journal* (Oct **2016**). https://doi.org/10.1111/febs.13828 (augustin2016structureandbiochemical pages 1-3)

---

## Clinical trials / registries relevant to real-world implementation
- **CoRDS (Coordination of Rare Diseases at Sanford)** observational registry / natural history infrastructure: **NCT01793168** (first posted Feb **2013**, recruiting; last update posted May **2025**). https://clinicaltrials.gov/study/NCT01793168 (NCT01793168 chunk 2, NCT01793168 chunk 1)

---

## Limitations of the current evidence base
1. The human phenotype and natural history remain weakly defined because the core evidence is dominated by a single well-described individual and secondary summaries. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 1-1)
2. Standard disease identifiers beyond OMIM (e.g., MONDO, Orphanet, ICD, MeSH) were not found in the retrieved set and must be added via direct ontology database queries.
3. Therapeutic guidance is largely expert opinion and hypothesis-driven supplementation trials rather than controlled clinical evidence. (walker2012trimethylaminuriaanddimethylglycine pages 3-5, moolenaar1999defectindimethylglycine pages 3-4)


References

1. (augustin2016structureandbiochemical pages 7-9): Peter Augustin, Altijana Hromic, Tea Pavkov‐Keller, Karl Gruber, and Peter Macheroux. Structure and biochemical properties of recombinant human dimethylglycine dehydrogenase and comparison to the disease‐related h109r variant. The Febs Journal, 283:3587-3603, Oct 2016. URL: https://doi.org/10.1111/febs.13828, doi:10.1111/febs.13828. This article has 27 citations.

2. (augustin2016structureandbiochemical pages 1-3): Peter Augustin, Altijana Hromic, Tea Pavkov‐Keller, Karl Gruber, and Peter Macheroux. Structure and biochemical properties of recombinant human dimethylglycine dehydrogenase and comparison to the disease‐related h109r variant. The Febs Journal, 283:3587-3603, Oct 2016. URL: https://doi.org/10.1111/febs.13828, doi:10.1111/febs.13828. This article has 27 citations.

3. (walker2012trimethylaminuriaanddimethylglycine pages 3-5): Valerie Walker and Ron A. Wevers. Trimethylaminuria and dimethylglycine dehydrogenase deficiency. Inborn Metabolic Diseases, pages 381-385, Jan 2012. URL: https://doi.org/10.1007/978-3-540-28785-8\_31, doi:10.1007/978-3-540-28785-8\_31. This article has 3 citations.

4. (mcandrew2008molecularbasisof pages 1-3): Ryan McAndrew, Jerry Vockley, and Jung-Ja P. Kim. Molecular basis of dimethylglycine dehydrogenase deficiency associated with pathogenic variant h109r. Journal of Inherited Metabolic Disease, 31:761-768, Oct 2008. URL: https://doi.org/10.1007/s10545-008-0999-2, doi:10.1007/s10545-008-0999-2. This article has 14 citations and is from a peer-reviewed journal.

5. (moolenaar1999defectindimethylglycine pages 4-5): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

6. (moolenaar1999defectindimethylglycine pages 1-1): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

7. (moolenaar2001invivoand pages 89-94): Sytske H. Moolenaar, Marjo S. van der Knaap, Udo F. H. Engelke, Petra J. W. Pouwels, Fokje S. M. Janssen‐Zijlstra, Nanda M. Verhoeven, Cornelis Jakobs, and Ron A. Wevers. In vivo and in vitro nmr spectroscopy reveal a putative novel inborn error involving polyol metabolism. NMR in Biomedicine, 14:167-176, May 2001. URL: https://doi.org/10.1002/nbm.690, doi:10.1002/nbm.690. This article has 58 citations and is from a peer-reviewed journal.

8. (moolenaar2001invivoand pages 94-98): Sytske H. Moolenaar, Marjo S. van der Knaap, Udo F. H. Engelke, Petra J. W. Pouwels, Fokje S. M. Janssen‐Zijlstra, Nanda M. Verhoeven, Cornelis Jakobs, and Ron A. Wevers. In vivo and in vitro nmr spectroscopy reveal a putative novel inborn error involving polyol metabolism. NMR in Biomedicine, 14:167-176, May 2001. URL: https://doi.org/10.1002/nbm.690, doi:10.1002/nbm.690. This article has 58 citations and is from a peer-reviewed journal.

9. (moolenaar1999defectindimethylglycine pages 1-2): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

10. (moolenaar1999defectindimethylglycine pages 3-4): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

11. (moolenaar1999defectindimethylglycine pages 5-5): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

12. (moolenaar2001invivoand pages 98-101): Sytske H. Moolenaar, Marjo S. van der Knaap, Udo F. H. Engelke, Petra J. W. Pouwels, Fokje S. M. Janssen‐Zijlstra, Nanda M. Verhoeven, Cornelis Jakobs, and Ron A. Wevers. In vivo and in vitro nmr spectroscopy reveal a putative novel inborn error involving polyol metabolism. NMR in Biomedicine, 14:167-176, May 2001. URL: https://doi.org/10.1002/nbm.690, doi:10.1002/nbm.690. This article has 58 citations and is from a peer-reviewed journal.

13. (moolenaar1999defectindimethylglycine media 773767bc): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

14. (mcandrew2008molecularbasisof pages 4-6): Ryan McAndrew, Jerry Vockley, and Jung-Ja P. Kim. Molecular basis of dimethylglycine dehydrogenase deficiency associated with pathogenic variant h109r. Journal of Inherited Metabolic Disease, 31:761-768, Oct 2008. URL: https://doi.org/10.1007/s10545-008-0999-2, doi:10.1007/s10545-008-0999-2. This article has 14 citations and is from a peer-reviewed journal.

15. (mcandrew2008molecularbasisof pages 6-8): Ryan McAndrew, Jerry Vockley, and Jung-Ja P. Kim. Molecular basis of dimethylglycine dehydrogenase deficiency associated with pathogenic variant h109r. Journal of Inherited Metabolic Disease, 31:761-768, Oct 2008. URL: https://doi.org/10.1007/s10545-008-0999-2, doi:10.1007/s10545-008-0999-2. This article has 14 citations and is from a peer-reviewed journal.

16. (moolenaar1999defectindimethylglycine media 214a655b): Sytske H Moolenaar, Jo Poggi-Bach, Udo FH Engelke, Jacqueline MB Corstiaensen, Arend Heerschap, Jan GN de Jong, Barbara A Binzak, Jerry Vockley, and Ron A Wevers. Defect in dimethylglycine dehydrogenase, a new inborn error of metabolism: nmr spectroscopy study. Clinical chemistry, 45 4:459-64, Apr 1999. URL: https://doi.org/10.1093/clinchem/45.4.459, doi:10.1093/clinchem/45.4.459. This article has 100 citations and is from a highest quality peer-reviewed journal.

17. (mcandrew2008molecularbasisof pages 8-8): Ryan McAndrew, Jerry Vockley, and Jung-Ja P. Kim. Molecular basis of dimethylglycine dehydrogenase deficiency associated with pathogenic variant h109r. Journal of Inherited Metabolic Disease, 31:761-768, Oct 2008. URL: https://doi.org/10.1007/s10545-008-0999-2, doi:10.1007/s10545-008-0999-2. This article has 14 citations and is from a peer-reviewed journal.

18. (NCT01793168 chunk 2):  Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford. Sanford Health. 2010. ClinicalTrials.gov Identifier: NCT01793168

19. (NCT01793168 chunk 1):  Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford. Sanford Health. 2010. ClinicalTrials.gov Identifier: NCT01793168