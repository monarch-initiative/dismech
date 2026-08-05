---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-02T11:14:26.578379'
end_time: '2026-07-02T11:32:05.181810'
duration_seconds: 1058.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Limb-Girdle Muscular Dystrophy, Autosomal Dominant
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Limb-Girdle Muscular Dystrophy, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Limb-Girdle Muscular Dystrophy, Autosomal Dominant** covering all of the
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
- **Disease Name:** Limb-Girdle Muscular Dystrophy, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Limb-Girdle Muscular Dystrophy, Autosomal Dominant** covering all of the
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


# Comprehensive Research Report: Limb-Girdle Muscular Dystrophy, Autosomal Dominant

## 1. Disease Information

### Overview

Autosomal dominant limb-girdle muscular dystrophy (AD-LGMD) encompasses a heterogeneous group of genetic muscle disorders characterized by progressive weakness of the shoulder and hip girdle musculature, inherited in an autosomal dominant pattern. AD-LGMDs represent approximately 10–15% of all LGMDs, with the remainder being autosomal recessive forms (costa2022lgmdd2tnpo3related pages 1-2). The limb-girdle muscular dystrophies as a whole include more than 30 subtypes caused by mutations in multiple genes, leading to weakness and progressive muscle degeneration (sun2025recentinsightsinto pages 5-7).

### Key Identifiers

- **OMIM:** LGMD1A (MIM 159000, MYOT); LGMD1B (MIM 159001, LMNA); LGMD1C (MIM 607801, CAV3); LGMD1E (MIM 615325, DES); TNPO3 gene OMIM 608423 (politano2024iscardiactransplantation pages 2-4, rodia2025novelinsightsinto pages 1-2)
- **Orphanet:** ORPHA:266 (Limb-girdle muscular dystrophy, general grouping)
- **ICD-10:** G71.0 (Muscular dystrophy)
- **ICD-11:** 8C70.0 (Limb-girdle muscular dystrophy)
- **MONDO:** MONDO:0015286 (autosomal dominant limb-girdle muscular dystrophy)

### Synonyms and Alternative Names

Historical nomenclature includes LGMD1A through LGMD1I (Erb's limb-girdle dystrophy variants). The 2018 ENMC workshop established a revised classification: dominant forms are now designated LGMDD1 through LGMDD5 (jeong2023tripartitemotifcontainingprotein pages 10-11). Several classical LGMD1 designations were excluded from the refined classification because they were associated with other diseases, had limited family documentation, or were misreported (jeong2023tripartitemotifcontainingprotein pages 10-11).

### Classification Summary

The following table summarizes all recognized and historically classified AD-LGMD subtypes:

| Current Name | Old Name | Gene | Chromosomal Locus | Protein | OMIM Disease ID | Age of Onset | Key Clinical Features |
|---|---|---|---|---|---|---|---|
| LGMDD1 | LGMD1D | DNAJB6 | 7q36.3 | DnaJ heat shock protein family member B6 | OMIM not confirmed in retrieved evidence | 2nd decade to upper middle age | Slowly progressive proximal weakness, often with distal involvement; fat infiltration on MRI; myofibrillar pathology/protein aggregation (sun2025recentinsightsinto pages 5-7, politano2024iscardiactransplantation pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 2-4) |
| LGMDD2 | LGMD1F | TNPO3 | 7q32.1 | Transportin-3 | OMIM not confirmed in retrieved evidence | Infancy to late adulthood; highly variable | Pelvic and shoulder girdle weakness, generalized atrophy, delayed walking in some cases, scapular winging/rigid spine/scoliosis, possible wheelchair dependence and respiratory insufficiency (sun2025recentinsightsinto pages 5-7, politano2024iscardiactransplantation pages 2-4, costa2022lgmdd2tnpo3related pages 1-2) |
| LGMDD3 | LGMD1G | HNRNPDL | 4p21 | Heterogeneous nuclear ribonucleoprotein D-like | OMIM not confirmed in retrieved evidence | Adult onset | Slowly progressive proximal limb weakness; rimmed vacuoles reported in muscle biopsy (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4) |
| LGMDD4 | LGMD1I | CAPN3 | Not confirmed in retrieved evidence | Calpain-3 | OMIM not confirmed in retrieved evidence | 8–15 years | Progressive scapular and pelvic girdle degeneration; severity may vary by mutation type (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4) |
| LGMDD5 | Bethlem myopathy (dominant collagen VI-related LGMD) | COL6A1, COL6A2, COL6A3 | Not confirmed in retrieved evidence | Collagen VI alpha chains 1/2/3 | OMIM not confirmed in retrieved evidence | 10–30 years | Slowly progressive weakness with proximal atrophy, ankle contractures; characteristic muscle MRI signs including “target” and “sandwich” signs (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 5-6, bouchard2023limb–girdlemusculardystrophies pages 2-4) |
| Excluded from revised LGMD classification | LGMD1A | MYOT | 5q31.2 | Myotilin | MIM 159000 | Late onset | Distal myopathy affecting ankles/feet/calves, may later involve proximal muscles; occasional respiratory insufficiency or cardiac failure (bouchard2023limb–girdlemusculardystrophies pages 2-4, politano2024iscardiactransplantation pages 2-4) |
| Excluded from revised LGMD classification | LGMD1B | LMNA | 1q22 | Lamin A/C | MIM 159001 | Variable; often childhood to adulthood | Proximal weakness with prominent cardiac arrhythmia/conduction disease risk; some reclassified toward Emery-Dreifuss spectrum (bouchard2023limb–girdlemusculardystrophies pages 2-4, politano2024iscardiactransplantation pages 2-4) |
| Excluded from revised LGMD classification | LGMD1C | CAV3 | 3p25.3 | Caveolin-3 | MIM 607801 | Variable; childhood to adulthood | HyperCKemia, calf hypertrophy, ankle contracture, exercise intolerance, cramps; overlapping caveolinopathy phenotypes including rippling muscle disease (bouchard2023limb–girdlemusculardystrophies pages 2-4, politano2024iscardiactransplantation pages 2-4) |
| Excluded from revised LGMD classification | LGMD1E | DES | 2q35 | Desmin | MIM 615325 | Not confirmed in retrieved evidence | Desmin aggregation/myofibrillar pathology, distal weakness, structural muscle abnormalities (bouchard2023limb–girdlemusculardystrophies pages 2-4, politano2024iscardiactransplantation pages 2-4) |
| Excluded from revised LGMD classification | LGMD1H | Unknown | Unknown | Unknown | Not confirmed in retrieved evidence | Not confirmed in retrieved evidence | Historical subtype with unresolved/unknown genetic basis; excluded from refined classification (bouchard2023limb–girdlemusculardystrophies pages 5-6, jeong2023tripartitemotifcontainingprotein pages 10-11) |


*Table: This table summarizes recognized autosomal dominant limb-girdle muscular dystrophy subtypes and historically named/excluded forms, with genes, loci, OMIM identifiers when available from retrieved evidence, onset, and hallmark clinical features. It is useful for mapping old and new nomenclature during knowledge-base curation.*

---

## 2. Etiology

### Disease Causal Factors

AD-LGMDs are exclusively genetic (Mendelian) disorders. Each subtype is caused by heterozygous pathogenic variants in a specific gene. The disease is inherited in an autosomal dominant pattern, meaning a single mutant allele is sufficient to cause disease (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4).

### Genetic Risk Factors (Causal Genes)

The currently recognized AD-LGMD subtypes and their causal genes are:

- **LGMDD1 (formerly LGMD1D):** *DNAJB6* (7q36.3) — encodes a co-chaperone of the HSP70 system involved in Z-disc organization and protein quality control. Mutations are primarily clustered in the G/F region and J domain (sun2025recentinsightsinto pages 5-7, sarparanta2020neuromusculardiseasesdue pages 9-11).
- **LGMDD2 (formerly LGMD1F):** *TNPO3* (7q32.1) — encodes transportin-3, a nuclear carrier for serine/arginine-rich (SR) proteins essential for mRNA splicing (rodia2025novelinsightsinto pages 1-2, costa2022lgmdd2tnpo3related pages 7-8).
- **LGMDD3 (formerly LGMD1G):** *HNRNPDL* (4p21) — encodes heterogeneous nuclear ribonucleoprotein D-like, involved in RNA binding and transcription regulation (sun2025recentinsightsinto pages 5-7, jeong2023tripartitemotifcontainingprotein pages 10-11).
- **LGMDD4 (formerly LGMD1I):** *CAPN3* — encodes calpain-3, a cysteine protease involved in sarcomeric remodeling (sun2025recentinsightsinto pages 5-7, jeong2023tripartitemotifcontainingprotein pages 10-11).
- **LGMDD5 (Bethlem myopathy):** *COL6A1, COL6A2, COL6A3* — encode collagen type VI subunits, components of the extracellular matrix (bouchard2023limb–girdlemusculardystrophies pages 5-6, jeong2023tripartitemotifcontainingprotein pages 10-11).

Historically classified but excluded from the revised LGMD classification are *MYOT* (LGMD1A), *LMNA* (LGMD1B), *CAV3* (LGMD1C), *DES* (LGMD1E), and LGMD1H (gene unknown) (bouchard2023limb–girdlemusculardystrophies pages 2-4, politano2024iscardiactransplantation pages 2-4, jeong2023tripartitemotifcontainingprotein pages 10-11).

### Environmental and Protective Factors

AD-LGMDs are monogenic disorders and are not significantly influenced by environmental risk factors. However, exercise interventions including aerobic and resistance training have demonstrated improvements in muscle strength and cardiorespiratory function across various LGMD subtypes (sun2025recentinsightsinto pages 18-21). No specific genetic protective factors or gene–environment interactions have been identified for AD-LGMD.

---

## 3. Phenotypes

### Core Clinical Features

The hallmark phenotype shared across AD-LGMD subtypes includes progressive proximal muscle weakness, elevated serum creatine kinase (CK) levels, and muscle fiber atrophy (sun2025recentinsightsinto pages 5-7). Individual subtypes exhibit distinct phenotypic patterns:

**LGMDD1 (DNAJB6-related):** Slowly progressive proximal limb weakness with onset from the 2nd decade to upper middle age, with distal involvement. MRI shows fat infiltration, and biopsies reveal rimmed vacuoles and increased internal nuclei (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4).

**LGMDD2 (TNPO3-related):** Highly variable presentation from infancy to late adulthood. Features include weakness of the pelvic and shoulder girdle muscles, generalized muscle atrophy, scapular winging, rigid spine, scoliosis, possible wheelchair dependence and respiratory insufficiency. Phenotypic variation is notable even within families (costa2022lgmdd2tnpo3related pages 1-2, sun2025recentinsightsinto pages 5-7).

**LGMDD3 (HNRNPDL-related):** Slowly progressive proximal limb weakness with adult onset. Rimmed vacuoles on muscle biopsy (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4).

**LGMDD4 (CAPN3 dominant):** Progressive scapular and pelvic girdle degeneration with onset at 8–15 years. Severity depends on mutation type, with missense mutations causing milder phenotypes than null mutations (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4).

**LGMDD5 (Bethlem myopathy):** Progressive weakness with proximal muscle atrophy, onset 10–30 years. Characteristic findings include ankle contractures and distinctive MRI signs ("target sign" and "sandwich sign") (bouchard2023limb–girdlemusculardystrophies pages 2-4, sun2025recentinsightsinto pages 5-7).

**Caveolinopathy (CAV3, formerly LGMD1C):** HyperCKemia in all patients, ankle contracture, calf hypertrophy, exercise intolerance, muscular cramps. May overlap with rippling muscle disease, familial hypertrophic cardiomyopathy, and distal myopathy phenotypes (bouchard2023limb–girdlemusculardystrophies pages 2-4).

### Suggested HPO Terms

- HP:0003202 — Skeletal muscle atrophy
- HP:0003560 — Muscular dystrophy
- HP:0003325 — Limb-girdle muscle weakness
- HP:0003236 — Elevated circulating creatine kinase concentration
- HP:0001371 — Flexion contracture
- HP:0002355 — Difficulty walking
- HP:0003701 — Proximal muscle weakness
- HP:0003557 — Increased variability in muscle fiber diameter
- HP:0003198 — Myopathy
- HP:0001644 — Dilated cardiomyopathy (LMNA-related)
- HP:0001638 — Cardiomyopathy
- HP:0002093 — Respiratory insufficiency

### Diagnostic Criteria

Diagnostic criteria for LGMD include: proximal or non-proximal muscle dystrophy, muscle fiber degeneration and necrosis, elevated serum CK levels, and muscle degenerative changes with fibrofatty infiltration (sun2025recentinsightsinto pages 5-7). The combination of clinical examination, muscle MRI, CK levels, muscle biopsy, and genetic testing constitutes the standard diagnostic approach. Cardiac involvement (22% of patients) and respiratory insufficiency (15.4%) should be assessed (lin2023clinicalfeaturesimaging pages 1-2).

### Diagnostic Testing

**Genetic Testing:** Next-generation sequencing (NGS) gene panels and whole exome sequencing (WES) have become the primary diagnostic tools. A definitive molecular diagnosis was obtained in 20% of a cohort of over 25,000 individuals with neuromuscular disorders, with diagnostic yields of up to 33% for muscular dystrophies specifically (doody2024definingclinicalendpoints pages 1-2). Multigene analysis is recommended over single-gene testing given significant phenotypic overlap (doody2024definingclinicalendpoints pages 1-2).

**Biomarkers:** Circulating miR-206 is a potential biomarker for disease progression, with significant elevation in LGMD patients compared to controls and 50–80-fold overexpression in severe cases (lin2023clinicalfeaturesimaging pages 1-2). MiR-1, miR-133a, and miR-206 are differentially expressed in serum and muscle, changing according to degrees of inflammation, fibrosis, and dystrophic progression (lin2023clinicalfeaturesimaging pages 1-2).

**Muscle Imaging:** MRI reveals fatty infiltration and replacement in affected muscles. Each subtype has characteristic patterns of muscle involvement on imaging (bouchard2023limb–girdlemusculardystrophies pages 2-4).

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

The following table provides a comprehensive overview of the molecular mechanisms underlying each AD-LGMD subtype:

| Subtype | Gene/Protein | Mechanism Type | Key Molecular Pathways Affected | Cellular Processes Disrupted | Key References |
|---|---|---|---|---|---|
| LGMDD1 (formerly LGMD1D) | **DNAJB6** / DnaJ heat shock protein family member B6 | **Toxic gain-of-function** | Hsp70 chaperone cycle dysregulation; proteostasis network; Z-disc protein quality control; autophagy-related stress pathways | Unregulated DNAJB6-Hsp70 binding, Hsp70 sequestration/depletion, protein misfolding, myofibrillar/Z-disc aggregation, vacuolar myopathy | (bengoechea2025inhibitionofdnajhsp70 pages 1-2, abayevavraham2023dnajb6mutantsdisplay pages 9-9, abayevavraham2023dnajb6mutantsdisplay pages 1-2, bengoechea2025inhibitionofdnajhsp70 pages 7-8, sarparanta2020neuromusculardiseasesdue pages 9-11, sarparanta2020neuromusculardiseasesdue pages 7-9) |
| LGMDD2 (formerly LGMD1F) | **TNPO3** / Transportin-3 | **Likely dominant toxic / loss-of-function mechanism** | Nuclear import of SR proteins; RNA metabolism and alternative splicing; myogenic regulatory factor signaling; autophagy | Impaired nuclear transport of splicing factors (e.g., SRSF1/SRSF2/RBM4/CPSF6), altered transcript processing, abnormal myogenic commitment, myofibrillar disarray, myofiber atrophy | (rodia2025novelinsightsinto pages 1-2, rodia2025novelinsightsinto pages 18-19, rodia2025novelinsightsinto pages 8-13, rodia2025novelinsightsinto pages 5-8, costa2022lgmdd2tnpo3related pages 7-8, costa2022lgmdd2tnpo3related pages 5-7) |
| LGMD1C / caveolinopathy (excluded from revised LGMD classification) | **CAV3** / Caveolin-3 | **Dominant negative with functional Caveolin-3 deficiency** | Caveolae biology; mTORC1 signaling; lysosomal cholesterol trafficking; mitochondrial homeostasis; Akt/p38 signaling | Caveolin-3 loss, reduced anabolic signaling, impaired protein synthesis, mitochondrial fragmentation and respiratory failure, altered cholesterol distribution, defective myoblast differentiation/fusion | (shah2023caveolin‐3losslinked pages 1-2, shah2020caveolin‐3deficiencyassociated pages 1-2, shah2020caveolin‐3deficiencyassociated pages 7-9, shah2020caveolin‐3deficiencyassociated pages 20-20, shah2020caveolin‐3deficiencyassociated pages 16-17, shah2020caveolin‐3deficiencyassociated pages 19-20) |
| LGMD1A / myotilinopathy (excluded from revised LGMD classification) | **MYOT** / Myotilin | **Unclear; dominant structural/protein-aggregation mechanism** | Sarcomere assembly; actin filament cross-linking; Z-disc organization | Disrupted actin cross-linking, impaired sarcomere assembly, myofibrillar instability, protein aggregate formation | (bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 5-6) |
| LGMD1B / laminopathy (excluded from revised LGMD classification) | **LMNA** / Lamin A/C | **Predominantly dominant negative / structural nuclear envelope dysfunction** | Nuclear lamina integrity; mechanotransduction; genome organization and transcriptional regulation | Nuclear envelope disruption, abnormal nuclear morphology, muscle fiber fragility, conduction-system/cardiac involvement in many patients | (bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 5-6) |
| LGMD1E / desminopathy (excluded from revised LGMD classification) | **DES** / Desmin | **Dominant protein-aggregation / filament disorganization mechanism** | Intermediate filament network; cytoskeletal organization; myofibril integrity | Desmin aggregation, irregular muscle fiber architecture, cytoskeletal collapse, myofibrillar degeneration | (bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 5-6) |
| LGMDD3 (formerly LGMD1G) | **HNRNPDL** / hnRNP D-like | **Likely dominant toxic protein/RNA-processing mechanism** | RNA binding and transcription/splicing regulation | Abnormal RNA handling, rimmed-vacuolar myopathy, progressive proximal weakness | (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 5-6, jeong2023tripartitemotifcontainingprotein pages 10-11) |
| LGMDD4 (formerly LGMD1I) | **CAPN3** / Calpain-3 | **Mutation-dependent; dominant pathogenic mechanism recognized but incompletely defined** | Sarcomere remodeling; muscle proteolysis; myofibrillar maintenance | Scapular/pelvic girdle degeneration, impaired sarcomeric maintenance, progressive muscle fiber loss | (sun2025recentinsightsinto pages 5-7, bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 5-6, jeong2023tripartitemotifcontainingprotein pages 10-11) |
| LGMDD5 (Bethlem myopathy spectrum) | **COL6A1/COL6A2/COL6A3** / Collagen VI | **Usually dominant structural extracellular-matrix mechanism** | Extracellular matrix organization; basement membrane-matrix interactions; muscle regeneration support | Matrix instability, impaired muscle fiber support, proximal weakness, contractures/ankle contracture, progressive fatty replacement | (bouchard2023limb–girdlemusculardystrophies pages 5-6, jeong2023tripartitemotifcontainingprotein pages 10-11, bouchard2023limb–girdlemusculardystrophies pages 2-4, sun2025recentinsightsinto pages 5-7) |


*Table: This table summarizes the main pathogenic mechanisms reported for autosomal dominant limb-girdle muscular dystrophy subtypes and historically associated dominant LGMD entities. It is useful for comparing whether disease biology is driven primarily by proteostasis failure, nuclear transport defects, membrane/caveola dysfunction, cytoskeletal aggregation, or extracellular matrix disruption.*

### LGMDD1 (DNAJB6) — Detailed Molecular Mechanism

DNAJB6 exists as two isoforms: the nuclear isoform DNAJB6a and the cytoplasmic isoform DNAJB6b, with the latter being the primary pathogenic isoform (findlay2023dnajb6isoformspecific pages 1-3). Disease-causing mutations are clustered in the G/F region near the α5 helix and in the J domain (sarparanta2020neuromusculardiseasesdue pages 9-11, sarparanta2020neuromusculardiseasesdue pages 7-9).

The pathogenic mechanism is a **toxic gain-of-function** dependent on DNAJB6-HSP70 interaction. Wild-type DNAJB6 possesses an autoinhibitory mechanism in its G/F domain that regulates J-domain interaction with HSP70. LGMDD1 mutations disrupt this autoinhibition, making the J-domain constitutively accessible for HSP70 binding (inoue2025moleculargeneticsof pages 6-8). The mutant DNAJB6 can thus "recruit and hyperactivate Hsp70 chaperones in an unregulated manner, depleting Hsp70 levels in myocytes, and resulting in the disruption of proteostasis" (abayevavraham2023dnajb6mutantsdisplay pages 1-2). This aberrant interaction leads to abnormal trapping of HSP70 at the Z-disc, impairing its normal rapid diffusion (bengoechea2025inhibitionofdnajhsp70 pages 1-2). Accumulated proteins include structural Z-disc proteins, RNA-binding stress-granule proteins, TDP-43, and various chaperones and cochaperones (HSPA8, CRYAB, HSPB8, SQSTM1, BAG3, STUB1), indicating widespread proteostasis disruption (sarparanta2020neuromusculardiseasesdue pages 7-9).

### LGMDD2 (TNPO3) — Detailed Molecular Mechanism

TNPO3 mutations produce a protein with an extended C-terminal domain that impairs nuclear transport of SR proteins essential for mRNA splicing and metabolism (rodia2025novelinsightsinto pages 1-2). Mutated TNPO3 fails to properly transport cargo proteins (SRSF1, SRSF2, RBM4, CPSF6) through the nuclear membrane, disrupting alternative splicing and protein synthesis. This leads to myofibrillar protein accumulation and disarray (costa2022lgmdd2tnpo3related pages 7-8). Recent zebrafish studies demonstrated that mutant TNPO3 caused myofibrillar disarray with perpendicularly oriented fibers resembling LGMDD2 patient muscle architecture (rodia2025novelinsightsinto pages 8-13). The mutation disrupts normal myogenic commitment and affects myogenic regulatory factor expression, representing impaired myogenesis as a core disease mechanism (rodia2025novelinsightsinto pages 18-19, rodia2025novelinsightsinto pages 5-8).

### CAV3 (Caveolinopathy) — Detailed Molecular Mechanism

The P104L mutation causes dramatic loss of Cav3 protein through a dominant negative mechanism, with the mutant protein being retained in the Golgi complex and subjected to proteasomal degradation rather than trafficking to the plasma membrane (shah2020caveolin‐3deficiencyassociated pages 7-9). Cav3 deficiency impairs mTORC1 signaling by disrupting lysosomal cholesterol trafficking, increasing lysosomal cholesterol content by 26% and suppressing mTORC1 activation, with phosphorylation of S6K1 and 4EBP1 reduced by 75–90% (shah2023caveolin‐3losslinked pages 1-2). Additionally, the P104L mutation causes mitochondrial fragmentation, shifting from predominantly tubular/elongated mitochondria (~65%) to fragmented/spheroid forms (>60%), with significant reductions in oxygen consumption rates (shah2020caveolin‐3deficiencyassociated pages 7-9). Loss of Cav3 also reduces cardiolipin content, increases mitochondrial cholesterol, elevates ROS production, and impairs myoblast differentiation through reduced Akt and p38 signaling (shah2020caveolin‐3deficiencyassociated pages 1-2, shah2020caveolin‐3deficiencyassociated pages 20-20, shah2020caveolin‐3deficiencyassociated pages 16-17).

### Suggested GO Terms

- GO:0006457 — Protein folding
- GO:0051085 — Chaperone cofactor-dependent protein refolding
- GO:0006606 — Protein import into nucleus
- GO:0000398 — mRNA splicing, via spliceosome
- GO:0007517 — Muscle organ development
- GO:0030240 — Skeletal muscle thin filament assembly
- GO:0045214 — Sarcomere organization
- GO:0031529 — Ruffle organization (caveolae)
- GO:0006914 — Autophagy

---

## 5. Anatomical Structures Affected

### Organ Level
- **Primary:** Skeletal muscle (UBERON:0001134), particularly proximal limb muscles
- **Secondary:** Heart (UBERON:0000948) — cardiac involvement in LMNA-related and some CAV3-related forms; respiratory system (UBERON:0001004) — restrictive respiratory insufficiency in ~15.4% of patients (lin2023clinicalfeaturesimaging pages 1-2)

### Tissue and Cell Level
- Skeletal muscle tissue (UBERON:0001134)
- Skeletal muscle fibers (CL:0000187 — skeletal muscle fiber)
- Myoblasts (CL:0000056 — myoblast)
- Satellite cells (CL:0000594 — skeletal muscle satellite cell)

### Subcellular Level
- Z-disc (GO:0030018) — aggregation of Z-disc proteins in LGMDD1
- Sarcomere (GO:0030017)
- Nucleus (GO:0005634) — nuclear transport disruption in LGMDD2
- Mitochondria (GO:0005739) — dysfunction in CAV3-related disease
- Caveolae (GO:0005901) — disrupted in CAV3-related disease
- Sarcoplasmic reticulum and plasma membrane

---

## 6. Temporal Development

### Onset
- LGMDD1: 2nd decade to upper middle age (sun2025recentinsightsinto pages 5-7)
- LGMDD2: Infancy to late adulthood, highly variable (costa2022lgmdd2tnpo3related pages 1-2, sun2025recentinsightsinto pages 5-7)
- LGMDD3: Adult onset (sun2025recentinsightsinto pages 5-7)
- LGMDD4: 8–15 years (sun2025recentinsightsinto pages 5-7)
- LGMDD5: 10–30 years (sun2025recentinsightsinto pages 5-7)

### Progression
Disease course is chronic and progressive, though the rate of progression varies substantially among subtypes and even within families. Some subtypes show stability until adulthood followed by slow progression, while others demonstrate early-onset disease with more rapid deterioration (costa2022lgmdd2tnpo3related pages 1-2). Cardiac involvement may present as sudden cardiac death, as documented in a patient with LMNA-related muscular dystrophy at age 37 (lin2023clinicalfeaturesimaging pages 1-2).

---

## 7. Epidemiology and Inheritance

### Epidemiology
LGMD collectively has a global incidence of approximately 0.7 per 100,000 and variable prevalence by region (doody2024definingclinicalendpoints pages 1-2). AD-LGMDs represent approximately 10–15% of all LGMDs (costa2022lgmdd2tnpo3related pages 1-2). In a US population-based study (MD STARnet, 2008–2016), LGMD was the most common diagnosis among 243 individuals with muscular dystrophy (138 cases), with a higher proportion of male individuals compared with female individuals (lin2023clinicalfeaturesimaging pages 1-2).

### Inheritance Pattern
All AD-LGMD subtypes follow an autosomal dominant inheritance pattern with variable expressivity and incomplete penetrance in some subtypes (sun2025recentinsightsinto pages 5-7, costa2022lgmdd2tnpo3related pages 1-2). The expressivity varies significantly even within the same family carrying the same pathogenic variant, as documented for TNPO3 and CAV3 mutations (costa2022lgmdd2tnpo3related pages 1-2). Somatic mosaicism has been documented in parents of LMNA-related muscular dystrophy probands (lin2023clinicalfeaturesimaging pages 1-2). De novo mutations are recognized, particularly in LMNA and DNAJB6 (lin2023clinicalfeaturesimaging pages 1-2).

---

## 8. Treatment

### Current Treatment — Symptomatic Management

Currently, only symptomatic treatments are available for AD-LGMD patients. Symptomatic therapy manages symptoms through interventions including nocturnal ventilation for respiratory impairment, β-blockers for cardiac involvement, nutritional adjustments, and physical rehabilitation, though it does not slow disease progression (sun2025recentinsightsinto pages 18-21). Exercise interventions, including aerobic and resistance training, have demonstrated improvements in muscle strength and cardiorespiratory function (sun2025recentinsightsinto pages 18-21). Suggested MAXO terms: MAXO:0000950 — Supportive care; MAXO:0001001 — Respiratory support.

### Experimental Therapeutics

**Small Molecule DNAJ-HSP70 Inhibitors (LGMDD1):** Treatment with a small-molecule inhibitor (JG231) of the DNAJ-HSP70 complex restored HSP70 mobility, improved muscle strength, and corrected myopathological features in LGMDD1 mouse models (bengoechea2025inhibitionofdnajhsp70 pages 1-2). This represents a promising therapeutic avenue as "interfering with DNAJB6-Hsp70 binding reverses the disease phenotype" (abayevavraham2023dnajb6mutantsdisplay pages 9-9).

**Isoform-Specific Knockdown (LGMDD1):** Morpholino antisense oligonucleotides targeting the DNAJB6b isoform (BPAS morpholinos) have shown therapeutic potential. Selective DNAJB6b reduction corrected 57% of disease-related proteins toward wild-type levels in F90I+/- myotubes, including HSP70 (findlay2023dnajb6isoformspecific pages 4-5). This approach was validated in primary mouse myotubes, human LGMDD1 myoblasts, and mouse skeletal muscle in vivo (findlay2022dnajb6isoformspecific pages 1-7, findlay2022dnajb6isoformspecific pages 13-17). Future clinical translation may involve peptide-conjugated phosphorodiamidate morpholinos or AAV-delivered U7-snRNA approaches (findlay2022dnajb6isoformspecific pages 7-13).

**RNAi Approaches:** RNAi approaches to knock down dominant mutations, such as myotilin mutations in LGMD1A, are under investigation (bouchard2023limb–girdlemusculardystrophies pages 9-11).

**Gene Editing:** CRISPR-Cas systems, base editing, and prime editing approaches have been explored, with some in vitro experiments successfully correcting mutations in LGMD models (bouchard2023limb–girdlemusculardystrophies pages 9-11).

**Clinical Trial Readiness:** The GRASP-LGMD Research Consortium (NCT03981289) is a multi-center study of 188 LGMD patients across 13 sites, including DNAJB6/LGMDD1 patients, designed to validate clinical outcome assessments for future clinical trials (doody2024definingclinicalendpoints pages 1-2).

---

## 9. Model Organisms

### LGMDD1 (DNAJB6) Models

**Transgenic Mouse Model:** Overexpression of mutant DNAJB6b-F93L under the MCK promoter produces an aggressive myopathy with 40% mortality by 2 months, desmin inclusions, and hnRNPA1/A2B1 aggregates recapitulating human LGMDD1 pathology (bengoechea2025inhibitionofdnajhsp70 pages 8-13).

**Knock-in Mouse Model:** A more physiologically relevant knock-in model expressing the LGMDD1 F90I mutation at endogenous levels develops progressive myopathy and has been used for preclinical therapeutic testing, including the DNAJ-HSP70 inhibitor JG231 (inoue2025moleculargeneticsof pages 8-10, bengoechea2025inhibitionofdnajhsp70 pages 8-13).

**C. elegans Model:** Blocking mutant DNAJB6-Hsp70 interaction rescues normal muscle morphology, and Hsp70 overexpression partially rescues disease phenotypes in C. elegans (abayevavraham2023dnajb6mutantsdisplay pages 9-9).

**Zebrafish Model:** Among the first in vivo models providing evidence that DNAJB6 mutations are pathogenic, demonstrating distinct muscle defects and implicating the cytoplasmic DNAJB6b isoform (inoue2025moleculargeneticsof pages 8-10).

### LGMDD2 (TNPO3) Models

**Zebrafish Model:** Microinjection of zebrafish embryos with mutant human TNPO3 mRNA caused body shortening, myofibrillar disarray, altered myosin patterning, and disrupted expression of myogenic regulatory factors (rodia2025novelinsightsinto pages 8-13, rodia2025novelinsightsinto pages 2-4). The model validates that TNPO3 mutations disrupt normal myogenic commitment and provides a platform for drug testing (rodia2025novelinsightsinto pages 18-19).

**C2C12 Cell Model:** Transfection of C2C12 cells with mutant TNPO3 demonstrated effects on muscle regulatory factor expression, p62 (autophagy marker), MuRF-1 (muscle atrophy marker), and desmin expression (rodia2025novelinsightsinto pages 5-8, rodia2025novelinsightsinto pages 4-5).

---

## 10. Prognosis and Outcomes

### Disease Course

AD-LGMDs generally follow a chronic progressive course, though the rate and severity vary markedly by subtype. LGMDD1 presents with slowly progressive proximal weakness, while LGMDD2 shows wide variability from childhood-onset with wheelchair dependence to adult-onset stable disease (costa2022lgmdd2tnpo3related pages 1-2, sun2025recentinsightsinto pages 5-7).

### Complications

Cardiac abnormalities were present in 22% of patients in one cohort, and one patient with LMNA-related muscular dystrophy experienced sudden cardiac death at age 37 (lin2023clinicalfeaturesimaging pages 1-2). Restrictive respiratory insufficiency was documented in 15.4% of patients (lin2023clinicalfeaturesimaging pages 1-2). Joint contractures, scoliosis, and scapular winging are common skeletal complications (costa2022lgmdd2tnpo3related pages 1-2, bouchard2023limb–girdlemusculardystrophies pages 2-4).

### Life Expectancy

Life expectancy varies by subtype. Most AD-LGMD forms have near-normal lifespan when cardiac involvement is monitored and managed, though LMNA-related forms carry risk of life-threatening cardiac arrhythmias. Specific longevity data for individual AD-LGMD subtypes remain limited.

---

## 11. Prevention

### Primary Prevention

As monogenic disorders, AD-LGMDs cannot be prevented through lifestyle modification. Primary prevention relies on genetic counseling and family planning.

### Genetic Counseling and Screening

Given autosomal dominant inheritance, affected individuals have a 50% risk of transmitting the disease to offspring. Genetic counseling is recommended for all affected families. Preimplantation genetic diagnosis (PGD) and prenatal testing are available when the familial mutation is known. Cascade genetic testing of at-risk family members is recommended.

### Secondary Prevention

Cardiac surveillance is essential for LMNA-related forms due to high risk of arrhythmias and sudden death. Regular respiratory function monitoring is recommended for all subtypes given the ~15% rate of restrictive pulmonary insufficiency (lin2023clinicalfeaturesimaging pages 1-2).

---

## 12. Summary and Current Challenges

AD-LGMD remains a diagnostic and therapeutic challenge due to its genetic heterogeneity, phenotypic variability, and rarity. The 2018 reclassification streamlined the nomenclature to five recognized subtypes (LGMDD1–D5), though several historically classified forms (MYOT, LMNA, CAV3, DES) remain clinically important entities that have been reclassified to other disease categories (jeong2023tripartitemotifcontainingprotein pages 10-11). The most promising therapeutic advances center on LGMDD1 (DNAJB6-related), where both small molecule inhibitors of the DNAJ-HSP70 interaction and isoform-specific antisense oligonucleotide knockdown approaches have shown preclinical efficacy (bengoechea2025inhibitionofdnajhsp70 pages 1-2, findlay2023dnajb6isoformspecific pages 4-5, findlay2023dnajb6isoformspecific pages 1-3). The GRASP-LGMD consortium represents a critical infrastructure development for clinical trial readiness (doody2024definingclinicalendpoints pages 1-2). Despite these advances, no disease-modifying therapies are yet available for human patients with any AD-LGMD subtype, and treatment remains supportive.

References

1. (costa2022lgmdd2tnpo3related pages 1-2): Roberta Costa, Maria Teresa Rodia, Serafina Pacilio, Corrado Angelini, and Giovanna Cenacchi. Lgmd d2 tnpo3-related: from clinical spectrum to pathogenetic mechanism. Frontiers in Neurology, Mar 2022. URL: https://doi.org/10.3389/fneur.2022.840683, doi:10.3389/fneur.2022.840683. This article has 27 citations and is from a peer-reviewed journal.

2. (sun2025recentinsightsinto pages 5-7): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

3. (politano2024iscardiactransplantation pages 2-4): Luisa Politano. Is cardiac transplantation still a contraindication in patients with muscular dystrophy-related end-stage dilated cardiomyopathy? a systematic review. International Journal of Molecular Sciences, 25:5289, May 2024. URL: https://doi.org/10.3390/ijms25105289, doi:10.3390/ijms25105289. This article has 12 citations.

4. (rodia2025novelinsightsinto pages 1-2): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

5. (jeong2023tripartitemotifcontainingprotein pages 10-11): Seung Yeon Jeong, Jun Hee Choi, Jooho Kim, Jin Seok Woo, and Eun Hui Lee. Tripartite motif-containing protein 32 (trim32): what does it do for skeletal muscle? Cells, 12:2104, Aug 2023. URL: https://doi.org/10.3390/cells12162104, doi:10.3390/cells12162104. This article has 14 citations.

6. (bouchard2023limb–girdlemusculardystrophies pages 2-4): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

7. (bouchard2023limb–girdlemusculardystrophies pages 5-6): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

8. (sarparanta2020neuromusculardiseasesdue pages 9-11): J. Sarparanta, P. Jonson, S. Kawan, and B. Udd. Neuromuscular diseases due to chaperone mutations: a review and some new results. International Journal of Molecular Sciences, Feb 2020. URL: https://doi.org/10.3390/ijms21041409, doi:10.3390/ijms21041409. This article has 91 citations.

9. (costa2022lgmdd2tnpo3related pages 7-8): Roberta Costa, Maria Teresa Rodia, Serafina Pacilio, Corrado Angelini, and Giovanna Cenacchi. Lgmd d2 tnpo3-related: from clinical spectrum to pathogenetic mechanism. Frontiers in Neurology, Mar 2022. URL: https://doi.org/10.3389/fneur.2022.840683, doi:10.3389/fneur.2022.840683. This article has 27 citations and is from a peer-reviewed journal.

10. (sun2025recentinsightsinto pages 18-21): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

11. (lin2023clinicalfeaturesimaging pages 1-2): Feng Lin, Kang Yang, Xin Lin, Ming Jin, Long Chen, Fu-ze Zheng, Liang-liang Qiu, Zhi-xian Ye, Hai-zhu Chen, Min-ting Lin, Ning Wang, and Zhi-qiang Wang. Clinical features, imaging findings and molecular data of limb-girdle muscular dystrophies in a cohort of chinese patients. Orphanet Journal of Rare Diseases, Nov 2023. URL: https://doi.org/10.1186/s13023-023-02897-x, doi:10.1186/s13023-023-02897-x. This article has 17 citations and is from a peer-reviewed journal.

12. (doody2024definingclinicalendpoints pages 1-2): Amy Doody, Lindsay N. Alfano, Jordi Díaz-Manera, Linda P Lowes, T. Mozaffar, Kathy Mathews, Conrad C. Weihl, Matthew Wicklund, Man Hung, J. Statland, Nicholas E. Johnson, Kathy Doris Peter Urvi John Carla Stacy Mathews Leung Kang Desai Vissing Zingariello Dixon, Kathy Mathews, Doris Leung, Peter Kang, Urvi Desai, J. Vissing, Carla Zingariello, and Stacy Dixon. Defining clinical endpoints in limb girdle muscular dystrophy: a grasp-lgmd study. BMC Neurology, Mar 2024. URL: https://doi.org/10.1186/s12883-024-03588-1, doi:10.1186/s12883-024-03588-1. This article has 10 citations and is from a peer-reviewed journal.

13. (bengoechea2025inhibitionofdnajhsp70 pages 1-2): R. Bengoechea, Andrew R. Findlay, Ankan K. Bhadra, Hao Shao, Kevin C. Stein, S. Pittman, J. Daw, Jason E. Gestwicki, Heather L. True, and Conrad C. Weihl. Inhibition of dnaj-hsp70 interaction improves strength in muscular dystrophy. The Journal of Clinical Investigation, May 2025. URL: https://doi.org/10.1172/jci194757, doi:10.1172/jci194757. This article has 48 citations.

14. (abayevavraham2023dnajb6mutantsdisplay pages 9-9): Meital Abayev-Avraham, Yehuda Salzberg, Dar Gliksberg, Meital Oren-Suissa, and Rina Rosenzweig. Dnajb6 mutants display toxic gain of function through unregulated interaction with hsp70 chaperones. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42735-z, doi:10.1038/s41467-023-42735-z. This article has 47 citations and is from a highest quality peer-reviewed journal.

15. (abayevavraham2023dnajb6mutantsdisplay pages 1-2): Meital Abayev-Avraham, Yehuda Salzberg, Dar Gliksberg, Meital Oren-Suissa, and Rina Rosenzweig. Dnajb6 mutants display toxic gain of function through unregulated interaction with hsp70 chaperones. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-42735-z, doi:10.1038/s41467-023-42735-z. This article has 47 citations and is from a highest quality peer-reviewed journal.

16. (bengoechea2025inhibitionofdnajhsp70 pages 7-8): R. Bengoechea, Andrew R. Findlay, Ankan K. Bhadra, Hao Shao, Kevin C. Stein, S. Pittman, J. Daw, Jason E. Gestwicki, Heather L. True, and Conrad C. Weihl. Inhibition of dnaj-hsp70 interaction improves strength in muscular dystrophy. The Journal of Clinical Investigation, May 2025. URL: https://doi.org/10.1172/jci194757, doi:10.1172/jci194757. This article has 48 citations.

17. (sarparanta2020neuromusculardiseasesdue pages 7-9): J. Sarparanta, P. Jonson, S. Kawan, and B. Udd. Neuromuscular diseases due to chaperone mutations: a review and some new results. International Journal of Molecular Sciences, Feb 2020. URL: https://doi.org/10.3390/ijms21041409, doi:10.3390/ijms21041409. This article has 91 citations.

18. (rodia2025novelinsightsinto pages 18-19): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

19. (rodia2025novelinsightsinto pages 8-13): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

20. (rodia2025novelinsightsinto pages 5-8): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

21. (costa2022lgmdd2tnpo3related pages 5-7): Roberta Costa, Maria Teresa Rodia, Serafina Pacilio, Corrado Angelini, and Giovanna Cenacchi. Lgmd d2 tnpo3-related: from clinical spectrum to pathogenetic mechanism. Frontiers in Neurology, Mar 2022. URL: https://doi.org/10.3389/fneur.2022.840683, doi:10.3389/fneur.2022.840683. This article has 27 citations and is from a peer-reviewed journal.

22. (shah2023caveolin‐3losslinked pages 1-2): Dinesh S. Shah, Raid B. Nisr, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 loss linked with the p104l lgmd‐1c mutation modulates skeletal muscle mtorc1 signalling and cholesterol homeostasis. Journal of Cachexia, Sarcopenia and Muscle, 14:2310-2326, Sep 2023. URL: https://doi.org/10.1002/jcsm.13317, doi:10.1002/jcsm.13317. This article has 6 citations and is from a domain leading peer-reviewed journal.

23. (shah2020caveolin‐3deficiencyassociated pages 1-2): Dinesh S. Shah, Raid B. Nisr, Clare Stretton, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 deficiency associated with the dystrophy p104l mutation impairs skeletal muscle mitochondrial form and function. Journal of Cachexia, Sarcopenia and Muscle, 11:838-858, Feb 2020. URL: https://doi.org/10.1002/jcsm.12541, doi:10.1002/jcsm.12541. This article has 40 citations and is from a domain leading peer-reviewed journal.

24. (shah2020caveolin‐3deficiencyassociated pages 7-9): Dinesh S. Shah, Raid B. Nisr, Clare Stretton, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 deficiency associated with the dystrophy p104l mutation impairs skeletal muscle mitochondrial form and function. Journal of Cachexia, Sarcopenia and Muscle, 11:838-858, Feb 2020. URL: https://doi.org/10.1002/jcsm.12541, doi:10.1002/jcsm.12541. This article has 40 citations and is from a domain leading peer-reviewed journal.

25. (shah2020caveolin‐3deficiencyassociated pages 20-20): Dinesh S. Shah, Raid B. Nisr, Clare Stretton, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 deficiency associated with the dystrophy p104l mutation impairs skeletal muscle mitochondrial form and function. Journal of Cachexia, Sarcopenia and Muscle, 11:838-858, Feb 2020. URL: https://doi.org/10.1002/jcsm.12541, doi:10.1002/jcsm.12541. This article has 40 citations and is from a domain leading peer-reviewed journal.

26. (shah2020caveolin‐3deficiencyassociated pages 16-17): Dinesh S. Shah, Raid B. Nisr, Clare Stretton, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 deficiency associated with the dystrophy p104l mutation impairs skeletal muscle mitochondrial form and function. Journal of Cachexia, Sarcopenia and Muscle, 11:838-858, Feb 2020. URL: https://doi.org/10.1002/jcsm.12541, doi:10.1002/jcsm.12541. This article has 40 citations and is from a domain leading peer-reviewed journal.

27. (shah2020caveolin‐3deficiencyassociated pages 19-20): Dinesh S. Shah, Raid B. Nisr, Clare Stretton, Gabriela Krasteva‐Christ, and Harinder S. Hundal. Caveolin‐3 deficiency associated with the dystrophy p104l mutation impairs skeletal muscle mitochondrial form and function. Journal of Cachexia, Sarcopenia and Muscle, 11:838-858, Feb 2020. URL: https://doi.org/10.1002/jcsm.12541, doi:10.1002/jcsm.12541. This article has 40 citations and is from a domain leading peer-reviewed journal.

28. (findlay2023dnajb6isoformspecific pages 1-3): Andrew R. Findlay, May M. Paing, Jil A. Daw, Meade Haller, Rocio Bengoechea, Sara K. Pittman, Shan Li, Feng Wang, Timothy M. Miller, Heather L. True, Tsui-Fen Chou, and Conrad C. Weihl. Dnajb6 isoform specific knockdown: therapeutic potential for limb girdle muscular dystrophy d1. Molecular Therapy - Nucleic Acids, 32:937-948, Jun 2023. URL: https://doi.org/10.1016/j.omtn.2023.05.017, doi:10.1016/j.omtn.2023.05.017. This article has 10 citations.

29. (inoue2025moleculargeneticsof pages 6-8): Michio Inoue. Molecular genetics of j-domain protein-related chaperonopathies in skeletal muscle. Journal of human genetics, Jul 2025. URL: https://doi.org/10.1038/s10038-025-01372-8, doi:10.1038/s10038-025-01372-8. This article has 0 citations and is from a peer-reviewed journal.

30. (findlay2023dnajb6isoformspecific pages 4-5): Andrew R. Findlay, May M. Paing, Jil A. Daw, Meade Haller, Rocio Bengoechea, Sara K. Pittman, Shan Li, Feng Wang, Timothy M. Miller, Heather L. True, Tsui-Fen Chou, and Conrad C. Weihl. Dnajb6 isoform specific knockdown: therapeutic potential for limb girdle muscular dystrophy d1. Molecular Therapy - Nucleic Acids, 32:937-948, Jun 2023. URL: https://doi.org/10.1016/j.omtn.2023.05.017, doi:10.1016/j.omtn.2023.05.017. This article has 10 citations.

31. (findlay2022dnajb6isoformspecific pages 1-7): Andrew R. Findlay, May M. Paing, Jil A. Daw, Rocio Bengoechea, Sara K. Pittman, Shan Li, Feng Wang, Timothy M. Miller, Heather L. True, Tsui-Fen Chou, and Conrad C. Weihl. Dnajb6 isoform specific knockdown: therapeutic potential for lgmdd1. bioRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.17.516920, doi:10.1101/2022.11.17.516920. This article has 1 citations.

32. (findlay2022dnajb6isoformspecific pages 13-17): Andrew R. Findlay, May M. Paing, Jil A. Daw, Rocio Bengoechea, Sara K. Pittman, Shan Li, Feng Wang, Timothy M. Miller, Heather L. True, Tsui-Fen Chou, and Conrad C. Weihl. Dnajb6 isoform specific knockdown: therapeutic potential for lgmdd1. bioRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.17.516920, doi:10.1101/2022.11.17.516920. This article has 1 citations.

33. (findlay2022dnajb6isoformspecific pages 7-13): Andrew R. Findlay, May M. Paing, Jil A. Daw, Rocio Bengoechea, Sara K. Pittman, Shan Li, Feng Wang, Timothy M. Miller, Heather L. True, Tsui-Fen Chou, and Conrad C. Weihl. Dnajb6 isoform specific knockdown: therapeutic potential for lgmdd1. bioRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.17.516920, doi:10.1101/2022.11.17.516920. This article has 1 citations.

34. (bouchard2023limb–girdlemusculardystrophies pages 9-11): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

35. (bengoechea2025inhibitionofdnajhsp70 pages 8-13): R. Bengoechea, Andrew R. Findlay, Ankan K. Bhadra, Hao Shao, Kevin C. Stein, S. Pittman, J. Daw, Jason E. Gestwicki, Heather L. True, and Conrad C. Weihl. Inhibition of dnaj-hsp70 interaction improves strength in muscular dystrophy. The Journal of Clinical Investigation, May 2025. URL: https://doi.org/10.1172/jci194757, doi:10.1172/jci194757. This article has 48 citations.

36. (inoue2025moleculargeneticsof pages 8-10): Michio Inoue. Molecular genetics of j-domain protein-related chaperonopathies in skeletal muscle. Journal of human genetics, Jul 2025. URL: https://doi.org/10.1038/s10038-025-01372-8, doi:10.1038/s10038-025-01372-8. This article has 0 citations and is from a peer-reviewed journal.

37. (rodia2025novelinsightsinto pages 2-4): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

38. (rodia2025novelinsightsinto pages 4-5): MT Rodia, M. Fazzina, Roberta Costa, MT Altieri, G. Sabbioni, E. D’Aversa, G. Breveglieri, E. Gatto, C. Bertolucci, S. Lombardi, M. Bergonzoni, R. Casadei, S. Santi, V. Papa, S. Ratti, G. Cenacchi, M. Borgatti, and F. Frabetti. Novel insights into the molecular mechanisms of lgmdd2: role of tnpo3 in experimental cell and zebrafish models. Cellular and Molecular Life Sciences, Nov 2025. URL: https://doi.org/10.1007/s00018-025-05954-9, doi:10.1007/s00018-025-05954-9. This article has 0 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-01.md)