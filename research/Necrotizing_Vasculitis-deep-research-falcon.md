---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T09:24:53.226798'
end_time: '2026-08-18T09:36:08.865765'
duration_seconds: 675.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Necrotizing Vasculitis
  mondo_id: MONDO:0800113
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Necrotizing_Vasculitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Necrotizing Vasculitis
- **MONDO ID:** MONDO:0800113 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Necrotizing Vasculitis** covering all of the
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
- **Disease Name:** Necrotizing Vasculitis
- **MONDO ID:** MONDO:0800113 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Necrotizing Vasculitis** covering all of the
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


# Necrotizing Vasculitis: Disease-Characteristics Research Report

**Target concept:** Necrotizing vasculitis  
**MONDO:** [MONDO:0800113](https://monarchinitiative.org/disease/MONDO:0800113)  
**Category:** Immune-mediated/autoimmune vasculitis  
**Evidence cutoff:** Literature prioritized through December 2024

## Executive interpretation

“Necrotizing vasculitis” is best represented in a knowledge base as a **histopathologic disease-pattern/umbrella concept**, not as one etiologically uniform syndrome. It denotes inflammatory destruction and necrosis of vessel walls. The strongest modern evidence concerns **ANCA-associated vasculitis (AAV)**—granulomatosis with polyangiitis (GPA), microscopic polyangiitis (MPA), eosinophilic granulomatosis with polyangiitis (EGPA), and renal-limited pauci-immune necrotizing crescentic glomerulonephritis—but necrotizing lesions also occur in polyarteritis nodosa, immune-complex vasculitis, infection-associated vasculitis, drug-associated disease, and monogenic disorders such as DADA2. Consequently, epidemiology, genetics, phenotype frequencies, prognosis, and treatment should be stored on the specific child diagnosis whenever possible, with MONDO:0800113 retained as a parent/pathology node. (OpenTargets Search: necrotizing vasculitis, xiao2016overviewofthe pages 1-1, kitching2020ancaassociatedvasculitis pages 51-55)

| domain | knowledge-base annotation | ontology suggestions | evidence caveat |
|---|---|---|---|
| Disease scope | **Necrotizing vasculitis** should be modeled primarily as a **pathologic/morphologic vasculitis pattern** characterized by vessel wall necrosis, not a single etiologically uniform disease entity. In current vasculitis nomenclature, it spans several syndromes, especially **ANCA-associated vasculitis (AAV)**, but also other entities such as polyarteritis nodosa/cutaneous arteritis depending on vessel size and context. (OpenTargets Search: necrotizing vasculitis, xiao2016overviewofthe pages 1-1, nakazawa2019pathogenesisandtherapeutic pages 9-9) | MONDO:0800113 necrotizing vasculitis; MeSH/ICD mapping should be treated cautiously; related disease labels: anti-neutrophil cytoplasmic antibody-associated vasculitis, granulomatosis with polyangiitis, microscopic polyangiitis, eosinophilic granulomatosis with polyangiitis | MONDO term exists, but literature often uses “necrotizing vasculitis” descriptively/histopathologically rather than as a discrete disease diagnosis. |
| Relationship to AAV | AAV is the best-supported modern clinical framework linked to necrotizing vasculitis: **pauci-immune small-vessel necrotizing inflammation** affecting kidney, lung, skin, ENT, nerves, and other organs. AAV includes GPA, MPA, and EGPA; renal-limited necrotizing crescentic GN is part of the spectrum. (xiao2016overviewofthe pages 1-1, kitching2020ancaassociatedvasculitis pages 51-55) | Related MONDO labels: anti-neutrophil cytoplasmic antibody-associated vasculitis; granulomatosis with polyangiitis; microscopic polyangiitis; eosinophilic granulomatosis with polyangiitis | Evidence is strongest for AAV, so many annotations below are **subtype-derived** rather than universal for all necrotizing vasculitis. |
| Core pathology | Hallmark lesion: **acute necrotizing inflammation of vessel walls**, often with **few or no immune deposits** in AAV, driven by activated leukocytes causing endothelial injury, fibrinoid necrosis, and downstream scarring/resolution. In kidney, classic lesion is **necrotizing crescentic glomerulonephritis**. (massicotteazarniouch2022mechanismsofvascular pages 9-11, xiao2016overviewofthe pages 1-1, kitching2020ancaassociatedvasculitis pages 51-55) | HPO labels: vasculitis, glomerulonephritis, hematuria, proteinuria; GO labels: neutrophil activation, complement activation, endothelial cell activation | “Pauci-immune” language applies mainly to AAV; immune-complex necrotizing vasculitis exists in other settings. |
| Major phenotypes/organs | Common high-yield manifestations in AAV-linked necrotizing vasculitis include **rapidly progressive glomerulonephritis**, pulmonary disease (nodules, infiltrates, alveolar hemorrhage), ENT disease (sinonasal inflammation/crusting), skin lesions (purpura/ulcers), peripheral neuropathy, constitutional symptoms, and hypertension with renal involvement. (draibe2024diagnosisandtreatment pages 2-3, kitching2020ancaassociatedvasculitis pages 51-55) | UBERON labels: kidney, glomerulus, lung, upper respiratory tract, skin, peripheral nerve, blood vessel; HPO labels: hematuria, proteinuria, pulmonary hemorrhage, sinusitis, hearing impairment, purpura, neuropathy | Organ spectrum differs by subtype: GPA is more granulomatous/ENT-pulmonary; MPA is more renal-pulmonary; EGPA adds eosinophilic/asthmatic features. |
| Key autoantigens / causal immune targets | Core autoantigen system in AAV: **MPO** and **PRTN3/PR3**. ANCA binding to surface-exposed MPO/PR3 on primed neutrophils drives neutrophil activation and vascular injury. (xiao2016overviewofthe pages 1-1, kitching2020ancaassociatedvasculitis pages 51-55) | Gene labels: **MPO**, **PRTN3**; protein labels: myeloperoxidase, proteinase 3 | Strongest mechanistic evidence for MPO-ANCA pathogenicity; PR3-ANCA pathogenicity is supported but historically less direct in animal transfer models. |
| Genetic susceptibility | Susceptibility is polygenic and subtype/serotype-biased; repeatedly implicated loci/genes include **HLA-DP** region, **SERPINA1**, and **PRTN3**, with additional immune loci reported in AAV precision-medicine/genetic studies. (yeo2024childhoodonsetancaassociatedvasculitis pages 14-16) | Gene labels: **HLA-DP** (region label; avoid exact ID if uncertain), **SERPINA1**, **PRTN3** | These are **risk-associated loci**, not monogenic causes of “necrotizing vasculitis” as an umbrella term. |
| Drug/therapeutic target genes | Clinically actionable targets strongly associated with AAV/necrotizing vasculitis include **MS4A1 (CD20)** for rituximab, **C5AR1** for avacopan, and **IL5** for mepolizumab in EGPA; Open Targets also links these to MONDO:0800113. (OpenTargets Search: necrotizing vasculitis) | **MS4A1/CD20**, **C5AR1**, **IL5** | Target-disease links are strongest for specific AAV subtypes and approved therapies, especially GPA/MPA for CD20 and C5aR1, EGPA for IL-5. |
| Immune cells | Central effector cell: **neutrophil**. Additional important cells: **B cells/plasmablasts** (ANCA production), **T cells** (pathogenic helper/cytotoxic programs), **monocytes/macrophages**, and **endothelial cells** as injury targets. (massicotteazarniouch2022mechanismsofvascular pages 9-11, xiao2016overviewofthe pages 1-1) | CL labels: neutrophil, B cell, T cell, monocyte, macrophage, endothelial cell | Relative contribution varies by tissue and subtype; eosinophils are particularly relevant in EGPA though not universal. |
| Renal tissue/cell programs | In ANCA glomerulonephritis, injury involves **glomerular endothelial cells**, infiltrating innate/adaptive immune cells, and crescent-forming epithelial compartments; recent spatial/single-cell work identified inflammatory niches and pathogenic T-cell signatures in kidney tissue. (draibe2024diagnosisandtreatment pages 2-3) | UBERON labels: kidney, renal glomerulus; CL labels: endothelial cell, CD4-positive T cell, CD8-positive T cell; GO labels: cell adhesion, cytokine-mediated signaling | Advanced omics data are currently **renal AAV-specific**, not broad evidence for every necrotizing vasculitis context. |
| Pathway mechanisms | Dominant mechanistic chain in AAV-linked necrotizing vasculitis: priming factors/infection-inflammatory milieu → surface MPO/PR3 exposure on neutrophils → ANCA binding/FcγR signaling → **alternative complement amplification with C5a** → endothelial adhesion/transmigration → ROS/protease/NET-mediated necrosis. (massicotteazarniouch2022mechanismsofvascular pages 9-11, xiao2016overviewofthe pages 1-1, nakazawa2019pathogenesisandtherapeutic pages 9-9) | GO labels: neutrophil degranulation, respiratory burst, complement activation alternative pathway, Fc receptor signaling, NET formation | This pathway is best established in **pauci-immune AAV**; other necrotizing vasculitides may involve different upstream triggers. |
| Diagnostics | Diagnostic workup typically integrates **ANCA serology (MPO-ANCA/PR3-ANCA)**, urinalysis/renal function, inflammatory markers, imaging, and—when feasible—**tissue biopsy** showing necrotizing vasculitis or pauci-immune necrotizing crescentic GN. Classification may additionally use 2022 ACR/EULAR criteria for GPA/MPA/EGPA. (draibe2024diagnosisandtreatment pages 2-3, kitching2020ancaassociatedvasculitis pages 67-70) | Diagnostic labels: ANCA serology, kidney biopsy, chest CT, urinalysis; pathology labels: pauci-immune necrotizing crescentic glomerulonephritis | Classification criteria are for **research classification**, not identical to clinical diagnosis; ANCA-negative cases exist. |
| Biomarkers | High-yield biomarkers: **PR3-ANCA**, **MPO-ANCA**; emerging/adjunct biomarker concepts include complement activation products and urinary inflammatory markers in renal vasculitis. (massicotteazarniouch2022mechanismsofvascular pages 9-11, kitching2020ancaassociatedvasculitis pages 67-70) | Biomarker labels: MPO-ANCA, PR3-ANCA, C5a, urinary soluble CD163 | Biomarker performance varies by organ involvement and relapse status; not all are validated for routine universal use. |
| Treatment classes | Main evidence-based treatment classes for AAV-pattern necrotizing vasculitis: **glucocorticoids**, **rituximab (anti-CD20)**, **cyclophosphamide**, maintenance agents (azathioprine, methotrexate, mycophenolate in selected settings), **avacopan (C5aR1 inhibitor)**, and **mepolizumab (anti-IL-5)** for EGPA. Plasma exchange is reserved for selected severe scenarios. (nakazawa2019pathogenesisandtherapeutic pages 9-9, draibe2024diagnosisandtreatment pages 2-3, yeo2024childhoodonsetancaassociatedvasculitis pages 14-16) | NCIT labels if used locally: glucocorticoid therapy, rituximab, cyclophosphamide, avacopan, mepolizumab, plasma exchange | Treatment should usually be attached to the **specific subtype/organ-threatening phenotype**, not blindly to MONDO:0800113 as an umbrella term. |
| Experimental / emerging therapy | Emerging approaches include **ustekinumab** for immune-profiled ANCA glomerulonephritis, **obinutuzumab** vs rituximab in current trials, and preclinical **CD19 CAR-T** strategies reducing MPO-ANCA-driven disease in mouse models. (draibe2024diagnosisandtreatment pages 2-3) | Intervention labels: ustekinumab, obinutuzumab, CD19 CAR-T cell therapy | These are experimental or early-stage and should not be represented as standard of care. |
| Data model recommendation | For a knowledge base, model **necrotizing vasculitis** as an umbrella/pathology node linked to child clinical entities and to histopathology/organ-specific manifestations; attach mechanistic and treatment assertions with **subtype qualifiers** (e.g., AAV, GPA, MPA, EGPA, renal AAV). (OpenTargets Search: necrotizing vasculitis, kitching2020ancaassociatedvasculitis pages 51-55) | Use MONDO node plus linked phenotype, anatomy, cell-type, pathway, and treatment annotations; preserve provenance and subtype qualifiers | Prevents overgeneralization from AAV literature to all necrotizing vasculitis contexts. |


*Table: This table provides compact, ontology-ready annotations for necrotizing vasculitis while emphasizing that the term is best treated as a histopathologic umbrella or pattern rather than a single etiologically uniform disease. It is useful for structuring knowledge-base entries with explicit caveats about when evidence is AAV-specific versus broadly applicable.*

## 1. Disease information

### Definition and nomenclature

The 2012 Chapel Hill framework defines AAV as **necrotizing vasculitis, with few or no immune deposits, predominantly affecting small vessels**. GPA adds necrotizing granulomatous respiratory inflammation; MPA lacks granulomatous inflammation; EGPA adds asthma, eosinophilia, and eosinophil-rich granulomatous inflammation. AAV also includes renal-limited pauci-immune necrotizing crescentic glomerulonephritis. The direct abstract wording from Xiao et al. is: **“Antineutrophil cytoplasmic autoantibodies (ANCA) are associated with a spectrum of necrotizing vasculitis including granulomatosis with polyangiitis, microscopic polyangiitis, eosinophilic granulomatosis with polyangiitis, and renal-limited necrotizing and crescentic glomerulonephritis.”** (Review; published December 2016; DOI [10.1159/000442323](https://doi.org/10.1159/000442323)). (xiao2016overviewofthe pages 1-1)

**Synonyms/descriptors:** necrotising vasculitis; necrotizing angiitis; fibrinoid necrotizing vasculitis; pauci-immune necrotizing vasculitis; ANCA-associated necrotizing vasculitis. These are not fully interchangeable: “pauci-immune” and “ANCA-associated” identify a mechanistic/pathologic subset.

**Identifiers:** MONDO:0800113 is supported. A single OMIM or Orphanet identifier is not appropriate because this is not one Mendelian or uniformly defined rare disease. ICD-10 commonly codes the specific syndrome—e.g., M30–M31 systemic necrotizing vasculopathies—rather than this histologic umbrella. ICD-11, MeSH, SNOMED CT, and Orphanet mappings should therefore be assigned at subtype level and verified against the release used by the knowledge base.

**Data provenance:** This report uses aggregated disease-level literature, guidelines, trial registries, and ontology resources—not individual EHR records. Recent real-world studies may use aggregated registry or administrative data, but no patient-level record was accessed.

## 2. Etiology

Necrotizing vasculitis has no single cause. Upstream categories include primary autoimmunity, immune complexes, infection, drugs/toxins, malignancy, and rare monogenic autoinflammation. In AAV, causation is multifactorial: genetic susceptibility and environmental or infectious priming lead to loss of tolerance to neutrophil proteins, predominantly **MPO** and **PR3**, followed by ANCA-mediated effector injury. (xiao2016overviewofthe pages 1-1)

### Risk factors

**Genetic susceptibility—not deterministic causation.** PR3-AAV is associated most strongly with the HLA-DP region, **SERPINA1**, and **PRTN3**; MPO-AAV has a different HLA architecture. These associations support classification by ANCA specificity rather than phenotype alone. Additional phenotype-dependent loci include **IL12B** and **IRF1**. No common pathogenic sequence variant, chromosomal abnormality, carrier frequency, or Mendelian penetrance can be assigned to MONDO:0800113. (yeo2024childhoodonsetancaassociatedvasculitis pages 14-16)

Rare monogenic mimics are clinically important. **ADA2/CECR1 loss-of-function variants** cause autosomal-recessive DADA2, which may present in childhood with PAN-like necrotizing arteritis, livedo, strokes, cytopenias, and immunodeficiency. Such cases warrant subtype-specific genetic testing rather than “necrotizing vasculitis” testing.

**Environmental/drug factors:** silica exposure is an epidemiologic risk for AAV. Well-established secondary triggers include hydralazine, propylthiouracil, minocycline, and levamisole-adulterated cocaine. Drug-associated cases may have unusually broad autoantibody profiles; withdrawal of the exposure is essential. PTU can alter NET formation and MPO immunogenicity. (kitching2020ancaassociatedvasculitis pages 51-55)

**Infectious factors:** infections can supply TNF and complement-mediated neutrophil-priming signals and may trigger or mimic AAV. Endocarditis, hepatitis B or C, HIV, and other infections must be excluded according to phenotype. Infection is not equivalent to transmissible AAV.

**Age/sex/geography:** AAV is predominantly adult-onset and rises with age; childhood disease is rare. GPA/PR3-AAV is relatively more common in populations of European ancestry and northern Europe, whereas MPA/MPO-AAV is relatively more common in East Asia. Sex effects are modest and subtype/cohort dependent.

### Protective factors and gene–environment interaction

No genetic allele, diet, supplement, exercise program, or environmental exposure is validated as specifically protective against the umbrella disease. Avoiding silica and culprit drugs is prudent for exposure reduction but has not been shown to prevent all primary disease. The plausible gene–environment chain is susceptibility genotype → infection/toxin-associated neutrophil priming or aberrant NET clearance → MPO/PR3 presentation → loss of B/T-cell tolerance → ANCA production. This remains probabilistic rather than a clinically validated individual-risk model. (xiao2016overviewofthe pages 1-1)

## 3. Phenotypes

Phenotypes are heterogeneous and often acute or subacute at onset, followed by relapsing-remitting or chronically damaging disease. Suggested HPO terms should be verified against the current HPO release.

- **Constitutional:** fever, fatigue, malaise, weight loss, myalgia and arthralgia; variable frequency and severity. Suggested HPO: Fever, Fatigue, Weight loss, Myalgia, Arthralgia.
- **Renal:** microscopic hematuria, red-cell casts, proteinuria, declining eGFR, hypertension, and rapidly progressive glomerulonephritis. Renal AAV commonly produces non-nephrotic proteinuria of approximately **1–3 g/day**. Severity ranges from urinary abnormalities to dialysis-requiring kidney failure. Suggested HPO: Hematuria, Proteinuria, Hypertension, Rapidly progressive glomerulonephritis, Renal insufficiency. (draibe2024diagnosisandtreatment pages 2-3)
- **Pulmonary:** nodules, masses, cavitation, infiltrates, interstitial lung disease, dyspnea, cough, and diffuse alveolar hemorrhage/hemoptysis. Suggested HPO: Pulmonary hemorrhage, Hemoptysis, Dyspnea, Pulmonary nodule, Interstitial pulmonary disease.
- **ENT/ocular:** chronic sinusitis, nasal crusting or bloody discharge, otitis/hearing loss, subglottic disease, orbital inflammation, scleritis. Especially characteristic of GPA. Suggested HPO: Chronic sinusitis, Epistaxis, Hearing impairment, Subglottic stenosis, Scleritis.
- **Skin:** palpable purpura, petechiae, ulcers, nodules, livedo and digital ischemia. Suggested HPO: Purpura, Skin ulcer, Livedo reticularis, Digital ischemia.
- **Neurologic:** painful mononeuritis multiplex, asymmetric sensorimotor neuropathy, and less commonly CNS ischemia/hemorrhage. Suggested HPO: Mononeuritis multiplex, Peripheral neuropathy, Neuropathic pain.
- **EGPA-specific:** adult-onset asthma, chronic rhinosinusitis/nasal polyps, eosinophilia, pulmonary infiltrates, neuropathy, and sometimes eosinophilic cardiac disease. Suggested HPO: Asthma, Eosinophilia, Nasal polyposis, Cardiomyopathy.
- **GI/cardiovascular:** abdominal pain, ischemia or bleeding; myocarditis/pericarditis and accelerated cardiovascular disease in selected phenotypes.

Frequency estimates must be attached to GPA, MPA, EGPA or the serotype, not to MONDO:0800113. In renal disease, biopsy-confirmed pauci-immune glomerulonephritis is a major disease-defining phenotype. In AAV generally, kidneys, lungs, ENT tract, skin, and peripheral nerves are the principal sites. (kitching2020ancaassociatedvasculitis pages 51-55)

**Quality of life:** Fatigue, pain, anxiety about relapse, treatment toxicity, work disability, and irreversible organ damage persist even during physician-rated remission. German registry data from 2007–2021 showed employment among patients younger than 65 rising from **47% to 57%**, but remaining below the general population; patient-reported outcomes largely did not improve despite lower physician-rated activity. This supports collecting SF-36, EQ-5D, PROMIS, fatigue, pain, work participation, and the AAV-PRO rather than disease activity alone.

## 4. Genetic and molecular information

### Causal genes and variants

There is **no universal causal gene**, no recurrent pathogenic variant, and no characteristic chromosome abnormality for necrotizing vasculitis. Primary AAV is polygenic/multifactorial. Therefore, ClinVar-style pathogenic/likely pathogenic/VUS classification, allele frequency, germline mosaicism, anticipation, carrier frequency, and karyotype findings are not applicable at umbrella level.

Relevant molecular categories are:

- **Autoantigens/effector proteins:** **MPO**, **PRTN3**.
- **Susceptibility/modifier loci:** HLA-DP-region alleles, **SERPINA1**, **PRTN3**, and phenotype-associated **IL12B/IRF1** signals.
- **Therapeutically validated targets:** **MS4A1/CD20** for rituximab, **C5AR1** for avacopan, and **IL5** for mepolizumab in EGPA. Open Targets links MONDO:0800113 most strongly to MS4A1 and C5AR1 and also to NR3C1, IL5 and purine-synthesis targets; these associations reflect drug evidence and must not be mislabeled as causal genes. (OpenTargets Search: necrotizing vasculitis)
- **Rare differential diagnoses:** ADA2/CECR1 in DADA2; subtype-directed panels can also include genes responsible for autoinflammation, immunodeficiency, complement dysregulation, and interferonopathies when onset is very early or atypical.

### Epigenetics

Aberrant control of neutrophil MPO/PRTN3 expression, DNA methylation and histone states has been reported in AAV, but no epigenetic mark is sufficiently validated for routine diagnosis or prognosis. Large chromosomal changes, repeat expansions, mitochondrial variants, and somatic cancer-type driver mutations are not established defining features.

## 5. Environmental information

Relevant non-genetic factors include respirable crystalline silica, selected drugs, levamisole-contaminated cocaine, and infection-associated immune activation. Smoking has inconsistent subtype-specific associations and should not be presented as a universal cause. Lifestyle management should address conventional cardiovascular risk, bone health, physical deconditioning, smoking cessation, and infection prevention, mainly to reduce morbidity rather than proven primary disease incidence.

Because infections can both trigger inflammation and mimic vasculitis, cultures, echocardiography, viral serology, and targeted microbiology should precede or accompany immunosuppression when clinically indicated. There is no zoonotic transmission.

## 6. Mechanism and pathophysiology

### Causal chain in pauci-immune AAV

1. **Upstream susceptibility and priming:** genetic susceptibility plus infectious/environmental inflammatory signals induce cytokines and alternative-complement activation.
2. **Antigen display:** primed neutrophils externalize MPO/PR3 from granules.
3. **ANCA ligation:** ANCA binds MPO/PR3, with Fcγ-receptor and Fab-dependent neutrophil activation.
4. **Amplification:** activated neutrophils generate complement fragments; **C5a–C5aR1** recruits and primes more neutrophils.
5. **Vascular injury:** adhesion to activated endothelium, respiratory burst, protease release, degranulation and NETosis injure endothelial cells and extracellular matrix.
6. **Morphology:** fibrinoid necrosis and leukocytoclasia develop; in glomeruli, capillary rupture drives crescent formation.
7. **Downstream outcome:** individual lesions evolve over approximately **1–2 weeks** toward resolution or fibrosis; continued waves of new lesions produce active systemic disease. Remission-induction stops new waves but cannot reverse all scar. (massicotteazarniouch2022mechanismsofvascular pages 9-11, xiao2016overviewofthe pages 1-1)

The strongest direct abstract statement is: **“Activated neutrophils adhere to and penetrate vessel walls, and they release toxic oxygen radicals and destructive enzymes that cause apoptosis and necrosis of the neutrophils as well as of the adjacent vessel wall cells and matrix.”** (Xiao et al., December 2016; DOI [10.1159/000442323](https://doi.org/10.1159/000442323)). (xiao2016overviewofthe pages 1-1)

Human samples show higher C3a, C5a and C5b-9 during active MPO- and PR3-AAV than in controls, with reductions in remission. Mouse C5aR blockade prevents or attenuates anti-MPO glomerulonephritis, and clinical C5aR1 inhibition validates this pathway therapeutically. (massicotteazarniouch2022mechanismsofvascular pages 9-11)

**Suggested GO biological processes:** neutrophil activation; neutrophil degranulation; respiratory burst; reactive oxygen species metabolic process; Fc receptor signaling; alternative complement activation; leukocyte adhesion to vascular endothelial cell; neutrophil extracellular-trap formation; endothelial-cell apoptotic process; extracellular-matrix disassembly; inflammatory response; wound healing/fibrosis.

**Suggested CL terms:** neutrophil; B cell; plasmablast/plasma cell; CD4-positive T cell; CD8-positive T cell; monocyte; macrophage; eosinophil (EGPA); endothelial cell; glomerular parietal epithelial cell; mesangial cell; podocyte.

### Molecular profiling and 2024 advances

A 2024 Nature Communications study applied spatial and single-cell transcriptomics to kidneys from **34 patients with ANCA glomerulonephritis**, identifying pro-inflammatory cytokine-producing CD4 and CD8 T-cell niches. Digital pharmacology nominated **ustekinumab** (IL-12/23 blockade); four patients with relapsing ANCA-GN subsequently received ustekinumab plus low-dose cyclophosphamide and glucocorticoids, and all showed clinical responses over 26 weeks. This is hypothesis-generating, uncontrolled precision-therapy evidence—not a treatment standard. Direct abstract quote: **“Here, using spatial and single-cell transcriptome analysis, we characterize inflammatory niches in kidney samples from 34 patients with ANCA-GN and identify proinflammatory, cytokine-producing CD4+ and CD8+ T cells as a pathogenic signature.”** Published September 2024; DOI [10.1038/s41467-024-52525-w](https://doi.org/10.1038/s41467-024-52525-w).

A 2024 spatial-transcriptomic preprint analyzed 32 ANCA, 19 lupus-nephritis, six anti-GBM, and six control kidneys, mapping more than 3.2 million cells. It proposed early PDGF signaling to parietal epithelial cells followed by macrophage/T-cell/renal-cell TGF-β signaling and sclerosis. As a preprint, it requires peer-reviewed validation.

## 7. Anatomical structures affected

**Primary:** small arteries, arterioles, capillaries, and venules; medium arteries in PAN-like disease. **Major organs:** kidney/glomerulus, lung/alveolar capillary bed, upper and lower respiratory tract, skin, peripheral nerve/vasa nervorum, eye/orbit, GI tract, and heart. Secondary damage includes chronic kidney disease, pulmonary fibrosis, hearing loss, neuropathic disability, and cardiovascular disease.

**Suggested UBERON labels:** blood vessel; arteriole; capillary; venule; kidney; renal glomerulus; lung; pulmonary alveolus; nasal cavity; paranasal sinus; trachea; skin; peripheral nerve; eye; gastrointestinal tract; heart.

**Subcellular compartments:** neutrophil azurophilic granule containing MPO/PR3, plasma membrane after priming, phagosome, cytosol, nucleus/chromatin during NETosis, and extracellular region/NET. Suggested GO-CC labels: azurophil granule, secretory granule, plasma membrane, extracellular region, chromatin, phagosome.

Disease is usually systemic, multifocal, patchy and asymmetric rather than consistently lateralized. Mononeuritis multiplex and ENT destruction may be particularly asymmetric.

## 8. Temporal development

Onset is usually adult and acute-to-subacute, although indolent ENT/pulmonary GPA and childhood AAV occur. Untreated organ-threatening disease can progress over days to weeks. Active AAV contains asynchronously initiated lesions, each evolving through stereotyped stages over about 1–2 weeks. (xiao2016overviewofthe pages 1-1)

A practical course model is: susceptibility/preclinical autoimmunity → symptomatic active disease → remission induction → treatment-induced remission → relapse or sustained remission → cumulative damage/organ failure. Disease is commonly relapsing-remitting; PR3-AAV generally relapses more often than MPO-AAV, whereas MPO-AAV more often leaves severe renal or fibrotic lung damage. Remission is usually treatment-induced, and spontaneous durable remission is unreliable. The critical intervention window is before irreversible crescentic renal scarring, alveolar hemorrhage, nerve infarction, or airway destruction.

## 9. Inheritance and population

Primary AAV and the umbrella necrotizing-vasculitis concept have **multifactorial/polygenic inheritance**, low familial recurrence, incomplete age-dependent susceptibility, and variable expression. Mendelian inheritance, anticipation, germline mosaicism, founder variants, carrier frequency and consanguinity are not generally applicable. These become relevant only for a defined monogenic mimic such as autosomal-recessive DADA2.

No defensible incidence or prevalence can be assigned to MONDO:0800113 because registry definitions and included diseases differ. AAV itself is rare, with strong geographic, ancestry and age variation; most published estimates are in the low tens per million person-years for incidence and tens to several hundred per million for prevalence. Those values should be stored with jurisdiction, calendar period and subtype rather than generalized to necrotizing vasculitis.

A 2024 Swedish population cohort of 374 AAV cases was **47% female**; under the EMA algorithm, 192 had GPA, 159 MPA, and 23 EGPA. Under 2022 ACR/EULAR criteria, 199 were GPA, 136 MPA and 22 EGPA; 1.1% met two categories and 3.5% were unclassifiable. This illustrates classification-dependent population statistics.

## 10. Diagnostics

### Clinical and laboratory approach

Diagnosis is integrative; no single test excludes or confirms every case.

1. Confirm compatible organ injury and urgency: CBC with differential/eosinophils, creatinine/eGFR, urinalysis with microscopy, urine protein quantification, CRP/ESR, liver tests.
2. Test high-quality antigen-specific **PR3-ANCA and MPO-ANCA immunoassays**. ANCA-negative disease exists, especially localized GPA and many EGPA cases.
3. Exclude mimics: blood cultures/endocarditis, hepatitis B/C and HIV where appropriate, anti-GBM antibodies, ANA/complement/cryoglobulins, infection, embolic disease, malignancy, thrombotic vasculopathy, and drug exposure.
4. Image the affected organ: chest radiograph/CT for nodules, cavitation, hemorrhage or ILD; sinus CT/MRI; echocardiography or vascular imaging as indicated.
5. Obtain tissue where feasible: kidney, skin, lung, ENT or nerve/muscle. Kidney biopsy typically shows focal/segmental necrotizing crescentic glomerulonephritis with few immune deposits by immunofluorescence. Biopsy also provides chronicity and prognostic information. (draibe2024diagnosisandtreatment pages 2-3, kitching2020ancaassociatedvasculitis pages 67-70)
6. Assess activity and damage using BVAS and Vasculitis Damage Index; monitor renal function, urine sediment/protein, blood count, immunoglobulins, infection and treatment toxicity. ANCA titers alone should not dictate treatment.

**Biomarkers:** MPO-/PR3-ANCA are clinically established. Complement fragments and urinary soluble CD163 are promising activity markers but not universal standalone diagnostics. ANCA, pathology and clinical phenotype can disagree.

### Classification criteria

The 2022 ACR/EULAR criteria are research-classification criteria applied after a small-/medium-vessel vasculitis diagnosis and exclusion of mimics—not screening or diagnostic criteria. GPA classification at a score ≥5 achieved **93% sensitivity and 94% specificity** in validation. A 2024 Japanese cohort, using EMA as reference, found sensitivity/specificity of 100%/96% for EGPA, 40%/97% for GPA and 90%/49% for MPA, demonstrating population and reference-standard limitations.

### Genetic/omics testing

Routine WES, WGS, CMA, karyotyping, FISH, mtDNA or repeat-expansion testing is not indicated for typical adult AAV. Use a vasculitis/autoinflammation/immunodeficiency panel or WES/WGS for childhood onset, family history, strokes, cytopenias, immunodeficiency, recurrent fever, or treatment-refractory atypical disease. RNA-seq, proteomics, metabolomics and epigenomics remain research tools. There is no population, newborn or asymptomatic genetic screening program.

## 11. Outcomes and prognosis

Modern immunosuppression transformed AAV from frequently fatal disease into a chronic relapsing-remitting condition, but mortality, kidney failure, infection, cardiovascular disease, malignancy and treatment toxicity remain substantial. (kitching2020ancaassociatedvasculitis pages 51-55)

Renal function is a dominant prognostic variable. The 2024 GLOMCAT consensus reports that patients with **eGFR <50 mL/min/1.73 m² face approximately a 50% risk of death or kidney failure within five years**. (draibe2024diagnosisandtreatment pages 2-3) Adverse factors include older age, severe renal impairment/dialysis, diffuse alveolar hemorrhage, cardiac disease, infection, high cumulative glucocorticoid/cyclophosphamide exposure and chronic scarring on biopsy. PR3-ANCA, prior relapse and persistent upper-airway disease predict relapse more than mortality.

Complications include ESRD, chronic pulmonary/ENT damage, subglottic stenosis, hearing loss, neuropathy, venous thromboembolism, cardiovascular events, osteoporosis, diabetes, infertility/cancer after cyclophosphamide, hypogammaglobulinemia after B-cell depletion, and opportunistic infection. Recovery is greatest when treatment precedes irreversible fibrosis; nerve, hearing, airway and advanced renal damage may be permanent.

## 12. Treatment

Treatment must follow the specific syndrome, organ severity, ANCA phenotype, comorbidity and fertility preferences.

### GPA/MPA and renal-limited AAV

**Organ-/life-threatening induction:** rituximab or cyclophosphamide plus a rapidly tapered glucocorticoid regimen. Rituximab is often preferred in relapsing PR3-AAV, younger patients needing fertility preservation, or prior cyclophosphamide exposure. Cyclophosphamide remains useful in fulminant disease. Avacopan, an oral **C5aR1 antagonist**, can reduce glucocorticoid exposure in eligible GPA/MPA patients. Suggested NCIT intervention labels: Rituximab Therapy, Cyclophosphamide Therapy, Corticosteroid Therapy, Avacopan, Immunosuppressive Therapy. (OpenTargets Search: necrotizing vasculitis, nakazawa2019pathogenesisandtherapeutic pages 9-9)

**ADVOCATE quantitative evidence:** among 214 rituximab-treated participants, week-26 remission occurred in **77.6%** with avacopan versus **75.7%** with prednisone taper; sustained week-52 remission was **71.0% versus 56.1%**. Serious adverse events occurred in **34.6% versus 39.3%**. Renal recovery, albuminuria reduction and glucocorticoid toxicity favored avacopan. Direct abstract conclusion: **“efficacy of treatment with avacopan compared with a prednisone taper was similar at week 26 and greater at week 52.”** Published February 2024; trial NCT02994927; DOI [10.1136/ard-2023-224816](https://doi.org/10.1136/ard-2023-224816).

**Non-organ-threatening disease:** glucocorticoids plus rituximab or, in selected patients, methotrexate/mycophenolate according to renal function and guideline context.

**Maintenance:** rituximab is generally preferred after severe GPA/MPA; azathioprine or methotrexate are alternatives. Duration is individualized, commonly at least 18–24 months and longer for high-relapse-risk PR3-AAV. Monitor IgG, infections, blood counts and renal/liver toxicity.

**Plasma exchange:** not routine for all severe AAV after PEXIVAS; consider selectively for anti-GBM overlap, exceptional life-threatening pulmonary hemorrhage, or very severe rapidly deteriorating renal disease after individualized risk assessment.

### EGPA

Glucocorticoids are foundational. Add cyclophosphamide or rituximab for organ-threatening vasculitic disease. **Mepolizumab**, targeting IL-5, is established for relapsing/refractory non-life-threatening eosinophilic/asthmatic disease and steroid sparing. Suggested NCIT terms: Mepolizumab, Anti-IL-5 Monoclonal Antibody Therapy.

### Supportive and real-world care

Provide Pneumocystis prophylaxis when immunosuppression warrants it, vaccination, osteoporosis and gastric-risk management, cardiovascular-risk treatment, fertility preservation before cyclophosphamide, rehabilitation, pain/neuropathy management, smoking cessation, psychosocial support, and nephrology/pulmonary/ENT/neurology collaboration. Surgery is reserved for damage—airway stenosis, reconstructive ENT disease, ischemic bowel, aneurysm, dialysis access or transplantation—not primary immune control.

### Experimental treatments and trials

- Ustekinumab: four-patient, immune-profile-guided pilot in relapsing ANCA-GN; investigational.
- Obinutuzumab versus rituximab: ObiVas phase II, ISRCTN13069630, planned n=26.
- Rituximab plus telitacicept: NCT05962840, phase IV, planned n=40.
- BDB-001 complement-directed programs: NCT05197842 completed phase I/II, n=93; later phase III programs are ongoing.
- CD19 CAR-T: preclinical MPO-AAV proof of principle; not standard clinical therapy.

No validated pharmacogenomic genotype currently selects induction therapy. Precision treatment is instead phenotype-, serotype-, organ-, relapse- and toxicity-guided.

## 13. Prevention

There is no validated primary prevention for idiopathic AAV. Avoid silica where occupationally feasible, avoid levamisole-contaminated cocaine, and discontinue culprit drugs. Genetic counseling is appropriate only for a suspected monogenic syndrome.

Secondary prevention consists of rapid recognition of hematuria, pulmonary hemorrhage, neuropathy or ENT destruction in symptomatic/high-risk patients; there is no population screening program. Tertiary prevention includes relapse monitoring, medication adherence, minimized glucocorticoid exposure, cardiovascular and renal protection, vaccination, infection prophylaxis, bone protection, malignancy surveillance after cyclophosphamide, and rehabilitation.

Administer indicated non-live vaccines—seasonal influenza, COVID-19, pneumococcal, recombinant zoster, hepatitis B where relevant—preferably before rituximab when disease urgency permits. Live vaccines are generally avoided during substantial immunosuppression. Screen for latent infection according to the planned therapy and local guidance.

## 14. Other species and natural disease

Necrotizing vasculitis occurs naturally in dogs, cats, horses and other species as heterogeneous immune-mediated, infectious, drug-associated or breed-associated syndromes. It is not one veterinary counterpart of MONDO:0800113. Therefore, no single breed ontology term, orthologous causal gene, prevalence, or inheritance pattern should be assigned.

Human AAV is not zoonotic and is not transmitted between species. Comparative value lies in conserved neutrophil, Fc-receptor, complement, endothelial-injury and repair pathways. Relevant taxa for experimental work include **Mus musculus** (NCBI Taxon 10090) and **Rattus norvegicus** (10116).

## 15. Model organisms

The canonical induced model is the **anti-MPO passive-transfer mouse model**: MPO-deficient mice are immunized with murine MPO; anti-MPO IgG or anti-MPO-producing splenocytes are transferred into wild-type recipients, producing pauci-immune necrotizing crescentic glomerulonephritis and sometimes pulmonary capillaritis. It directly demonstrates MPO-ANCA pathogenicity and is useful for complement, Fc receptor, neutrophil and treatment studies. C5/C5aR disruption protects mice, supporting complement amplification. (massicotteazarniouch2022mechanismsofvascular pages 9-11, xiao2016overviewofthe pages 1-1)

A 2024 preclinical study used CD19-targeted CAR-T cells in an MPO-AAV mouse model. CAR-T cells depleted B cells/plasmablasts, accelerated MPO-ANCA decline and protected against necrotizing crescentic GN. Direct abstract conclusion: **“Our proof-of-principle study may encourage further exploration of CAR T cells as a treatment for ANCA-vasculitis patients with the goal of drug-free remission.”** Published April 2024; DOI [10.1136/ard-2023-224875](https://doi.org/10.1136/ard-2023-224875).

Limitations include stronger recapitulation of MPO-AAV than PR3-AAV, short experimental time courses, induced rather than spontaneous autoimmunity, and incomplete modeling of human granulomatous ENT disease, relapse, age, infection and treatment toxicity. Additional systems include human neutrophil/endothelial coculture, organ-on-chip vascular assays, ex-vivo kidney tissue, and patient-derived single-cell/spatial atlases. No model fully reproduces the umbrella condition.

## Knowledge-base curation recommendations

1. Treat MONDO:0800113 as an **umbrella/pathology node** and attach incidence, phenotype frequencies, variants, prognosis and therapy to GPA, MPA, EGPA, PAN, DADA2 or another defined child diagnosis.
2. Qualify mechanistic assertions as **AAV-specific** unless evidence covers other necrotizing vasculitides.
3. Separate **susceptibility genes** from causal Mendelian genes and therapeutic targets. MS4A1/C5AR1/IL5 are clinically actionable targets, not universal causes. (OpenTargets Search: necrotizing vasculitis)
4. Record evidence type: human clinical/biopsy, guideline, registry, in vitro, mouse, computational or preprint.
5. Do not infer a pathogenic variant, inheritance mode, protective factor, population prevalence, or screening program where none is established.

References

1. (OpenTargets Search: necrotizing vasculitis): Open Targets Query (necrotizing vasculitis, 35 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (xiao2016overviewofthe pages 1-1): Hong Xiao, Peiqi Hu, Ronald J. Falk, and J. Charles Jennette. Overview of the pathogenesis of anca-associated vasculitis. Kidney Diseases, 1:205-215, Dec 2016. URL: https://doi.org/10.1159/000442323, doi:10.1159/000442323. This article has 164 citations and is from a peer-reviewed journal.

3. (kitching2020ancaassociatedvasculitis pages 51-55): A. Richard Kitching, Hans-Joachim Anders, Neil Basu, Elisabeth Brouwer, Jennifer Gordon, David R. Jayne, Joyce Kullman, Paul A. Lyons, Peter A. Merkel, Caroline O. S. Savage, Ulrich Specks, and Renate Kain. Anca-associated vasculitis. Nature Reviews Disease Primers, 6:1-27, Aug 2020. URL: https://doi.org/10.1038/s41572-020-0204-y, doi:10.1038/s41572-020-0204-y. This article has 1157 citations.

4. (nakazawa2019pathogenesisandtherapeutic pages 9-9): Daigo Nakazawa, Sakiko Masuda, Utano Tomaru, and Akihiro Ishizu. Pathogenesis and therapeutic interventions for anca-associated vasculitis. Nature Reviews Rheumatology, 15:91-101, Dec 2019. URL: https://doi.org/10.1038/s41584-018-0145-y, doi:10.1038/s41584-018-0145-y. This article has 571 citations and is from a domain leading peer-reviewed journal.

5. (massicotteazarniouch2022mechanismsofvascular pages 9-11): David Massicotte-Azarniouch, Carolina A. Herrera, J. Charles Jennette, Ronald J. Falk, and Meghan E. Free. Mechanisms of vascular damage in anca vasculitis. Seminars in Immunopathology, 44:325-345, Mar 2022. URL: https://doi.org/10.1007/s00281-022-00920-0, doi:10.1007/s00281-022-00920-0. This article has 58 citations and is from a domain leading peer-reviewed journal.

6. (draibe2024diagnosisandtreatment pages 2-3): Juliana Bordignon Draibe, Helena Marco, Meritxell Ibernon, Irene Agraz, Carola Arcal, Xoana Barros, Victoria Cabrera, Iara Da Silva, Montserrat Díaz, Xavier Fulladosa, Elena Guillén, Patricia Lescano, Laura Martínez Valenzuela, Eva Márquez, Nadia Martín, Ana Merino, Maru Navarro, Eva Rodríguez, Mª José Soler, Joan Torras, and Luís F. Quintana. Diagnosis and treatment of renal anca vasculitis: a summary of the consensus document of the catalan group for the study of glomerular diseases (glomcat). Journal of Clinical Medicine, 13:6793, Nov 2024. URL: https://doi.org/10.3390/jcm13226793, doi:10.3390/jcm13226793. This article has 3 citations.

7. (yeo2024childhoodonsetancaassociatedvasculitis pages 14-16): Liching Yeo, Asma Naheed, Chantelle Richards, and Coziana Ciurtin. Childhood-onset anca-associated vasculitis: from genetic studies to advances in pathogenesis, classification and novel therapeutic approaches. International Journal of Molecular Sciences, 25:13704, Dec 2024. URL: https://doi.org/10.3390/ijms252413704, doi:10.3390/ijms252413704. This article has 10 citations.

8. (kitching2020ancaassociatedvasculitis pages 67-70): A. Richard Kitching, Hans-Joachim Anders, Neil Basu, Elisabeth Brouwer, Jennifer Gordon, David R. Jayne, Joyce Kullman, Paul A. Lyons, Peter A. Merkel, Caroline O. S. Savage, Ulrich Specks, and Renate Kain. Anca-associated vasculitis. Nature Reviews Disease Primers, 6:1-27, Aug 2020. URL: https://doi.org/10.1038/s41572-020-0204-y, doi:10.1038/s41572-020-0204-y. This article has 1157 citations.

## Artifacts

- [Edison artifact artifact-00](Necrotizing_Vasculitis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.