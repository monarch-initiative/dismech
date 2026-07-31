---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:19:35.938128'
end_time: '2026-07-31T00:27:02.870506'
duration_seconds: 446.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Agnathia-Otocephaly Complex
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Agnathia-Otocephaly_Complex-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Agnathia-Otocephaly Complex
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Agnathia-Otocephaly Complex** covering all of the
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
- **Disease Name:** Agnathia-Otocephaly Complex
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Agnathia-Otocephaly Complex** covering all of the
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


# Agnathia–Otocephaly Complex: Disease Characteristics Report

## Executive summary and evidence limits

Agnathia–otocephaly complex (AOC; AGOTC) is an ultra-rare, congenital craniofacial developmental disorder defined by absent or profoundly hypoplastic mandible together with abnormal ventromedial displacement—occasionally midline fusion—of the external ears. Microstomia, microglossia or aglossia, severe upper-airway obstruction, and forebrain anomalies may accompany the mandibular defect. Current evidence supports **OTX2** and **PRRX1** as principal disease genes, but many cases remain molecularly unexplained; **SMAD3** has only limited case-level support. The disorder originates during early embryonic patterning of the rostral head and first pharyngeal arch rather than representing a progressive postnatal disease. Human evidence consists predominantly of fetal or neonatal case reports and small series. Consequently, robust prevalence, penetrance, survival, and treatment-response statistics do not exist.

The strongest mechanistic evidence comes from *Otx2* mutant mice: heterozygous loss produces dosage- and genetic-background-dependent otocephaly-like defects, whereas homozygous loss deletes nearly all structures anterior to rhombomere 3. These experiments implicate disrupted cranial-neural-crest/ectomesenchymal development, deficient growth of the rostral neuroepithelium, and failed first-arch mandibular patterning. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 6-7)

| Domain | Finding | Suggested ontology terms | Evidence strength/notes |
|---|---|---|---|
| Definition / core phenotype | Agnathia-otocephaly complex is a rare congenital craniofacial malformation centered on absent or severely hypoplastic mandible with ventromedial ear malposition/fusion and often severe oral anomalies; associated findings can include microstomia, microglossia/aglossia, and holoprosencephaly-like brain defects. | MONDO: agnathia-otocephaly complex (if available); HPO: agnathia, micrognathia, synotia/melotia, microstomia, aglossia, microglossia, holoprosencephaly; UBERON: mandible, external ear, tongue, first pharyngeal arch | Moderate-high disease-level support from review-style and summary evidence; exact ontology IDs should be verified in MONDO/HPO before ingestion (behunova2025facialbonedefects pages 19-20) |
| Established causal gene: OTX2 | OTX2 is an established disease gene for otocephaly/agnathia-dysgnathia spectrum; human reports include point mutations and an in-frame duplication, with apparent variable expressivity/incomplete penetrance across reported families/individuals. | HGNC: OTX2; GO: anterior/posterior pattern specification, craniofacial development; CL: cranial neural crest cell | High confidence at gene level from foundational human genetics plus strong developmental model support; exact variant assertions/classifications require ClinVar/primary-paper verification (behunova2025facialbonedefects pages 19-20, matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 9-10) |
| Established causal gene: PRRX1 | PRRX1 is an established disease gene for recurrent agnathia-otocephaly in some families/cases, supporting a monogenic developmental etiology in a subset of patients. | HGNC: PRRX1; GO: craniofacial development, mesenchyme development | High confidence at gene level from indexed primary human literature metadata and disease summaries; exact recurrence risk and variant nomenclature should be checked in the original reports (behunova2025facialbonedefects pages 19-20) |
| Emerging / limited gene evidence: SMAD3 | SMAD3 has been reported in an expanded phenotype including agnathia-otocephaly, but current support appears limited to isolated case-level evidence rather than broad replication. | HGNC: SMAD3; GO: TGF-beta signaling pathway | Low-moderate confidence; best treated as emerging/limited evidence pending replication and curation in disease-gene validity frameworks (behunova2025facialbonedefects pages 19-20) |
| Developmental mechanism | Best-supported mechanism is disruption of rostral head patterning involving cranial neural crest and first pharyngeal arch ectomesenchyme; mandibular/pre-mandibular arch structures are particularly vulnerable, explaining agnathia, ear displacement, tongue/palate anomalies, and associated anterior cranial defects. | GO: neural crest cell development, pharyngeal arch morphogenesis, craniofacial skeleton development; CL: cranial neural crest cell, ectomesenchymal cell; UBERON: first pharyngeal arch, Meckel cartilage, mandible | High mechanistic plausibility from Otx2 mouse data and craniofacial developmental literature; direct human mechanistic assays are sparse (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 10-11, mina2001regulationofmandibular pages 5-6, matsuo1995mouseotx2functions pages 6-7) |
| Prenatal diagnosis | Current real-world diagnosis is primarily prenatal imaging-based: first-trimester or later ultrasound, often supplemented by fetal MRI/3D imaging for facial anatomy, airway planning, and associated CNS anomalies. | HPO: prenatal onset; RadLex/UBERON labels: fetal ultrasound, fetal MRI, mandible, airway | Moderate confidence; contemporary practice is supported mainly by case reports/series and review metadata rather than trials. Useful for obstetric counseling and delivery planning (behunova2025facialbonedefects pages 19-20) |
| Airway management / EXIT | Severe cases may require planned airway management at delivery, including consideration of EXIT when airway obstruction is anticipated. This is an implementation issue rather than disease-specific therapy. | MAXO: airway management, tracheostomy, EXIT procedure; HPO: upper airway obstruction | Moderate confidence from recent case-report metadata and broader anticipated-airway-obstruction consensus literature; no disease-specific comparative trials identified (behunova2025facialbonedefects pages 19-20) |
| Reconstruction / longitudinal care | Rare long-term survivors may undergo staged craniofacial reconstruction, including mandibular reconstruction (for example free fibula flap) and multidisciplinary speech/feeding/airway management. | MAXO: mandibular reconstruction, feeding support, speech therapy, tracheostomy care | Low-moderate confidence because evidence is limited to highly selected survivor case reports and surgical experience; not generalizable to most prenatal/lethal presentations (behunova2025facialbonedefects pages 19-20) |
| Prognosis | Prognosis is usually poor, with many cases resulting in fetal demise, termination, stillbirth, or death in the neonatal period because of severe craniofacial and airway compromise; survival into childhood/adulthood is rare and typically involves intensive supportive/surgical care. | HPO: neonatal death, respiratory insufficiency; MAXO: palliative/supportive care | Moderate confidence from cumulative case literature and model-consistent severity; precise survival statistics are unavailable because the condition is ultra-rare and literature is case based (behunova2025facialbonedefects pages 19-20) |
| OTX2 mouse model | Otx2 heterozygous mice show otocephaly-like craniofacial defects with dosage sensitivity, affecting mandible, anterior skull, eyes, nasal structures, and first arch derivatives; homozygous loss causes severe rostral truncation. The model strongly recapitulates core developmental biology of the human disorder. | MGI: Otx2 mouse model; GO: rostral head development, neural crest development; UBERON: mandible, basisphenoid, nasal capsule | High-value mechanistic model with strong face validity for craniofacial patterning; limitations include species differences and incomplete capture of full human phenotypic heterogeneity (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 10-11, matsuo1995mouseotx2functions pages 1-2, matsuo1995mouseotx2functions pages 6-7, matsuo1995mouseotx2functions pages 11-12) |


*Table: This table condenses the most actionable disease-knowledge findings for Agnathia-Otocephaly Complex, pairing each domain with suggested ontology labels and a brief evidence-strength assessment. It is useful for knowledge-base curation because it highlights established versus emerging findings and marks where evidence is mainly case-based or model-based.*

## 1. Disease information

### Definition

AOC is a **malformation sequence/complex**, not an acquired disease. Its defining lesion is agnathia or extreme mandibular hypoplasia. The shortened lower face allows the ears to occupy an unusually low and medial position; terms such as **melotia** describe ventromedial auricular displacement and **synotia** describes fusion of the ears. Associated manifestations include severe microstomia, microglossia or aglossia, and sometimes holoprosencephaly. Ear position can be strikingly abnormal even when intrinsic auricular anatomy and postnatal hearing are relatively preserved in survivors. (behunova2025facialbonedefects pages 19-20)

### Synonyms

Common labels include:

- agnathia–otocephaly complex;
- agnathia–microstomia–synotia syndrome;
- otocephaly;
- otocephaly–dysgnathia complex;
- agnathia–holoprosencephaly complex, when forebrain malformation is present;
- dysgnathia complex or severe isolated agnathia, in partially overlapping literature.

“Otocephaly” should not be interpreted as a primary ear disease: the central developmental defect is loss or severe underdevelopment of mandibular/rostral craniofacial structures.

### Identifiers and coding

- **MONDO:** a dedicated MONDO concept should be verified in the current MONDO release before database ingestion; no confidently verified identifier was recovered in this search.
- **OMIM:** records for agnathia/otocephaly and the relevant *OTX2*/*PRRX1* phenotypes exist, but an exact disease-level number was not verified from the retrieved full text and should not be inferred.
- **Orphanet:** listed as an ultra-rare developmental anomaly; verify the current ORPHA identifier directly in Orphadata before ingestion.
- **MeSH:** generally indexed through congenital jaw abnormalities, agnathia, craniofacial abnormalities, or holoprosencephaly rather than a consistently used dedicated heading.
- **ICD-10/ICD-11:** no highly specific disease code is established in the retrieved evidence. Practical coding ordinarily uses congenital malformation of facial bones/jaw, with additional codes for brain, ear, airway, or digestive abnormalities.

This report combines **aggregated disease-level resources and published literature**. It does not use EHR-derived individual-level data. Most primary clinical evidence nevertheless originates from individual fetuses, neonates, or exceptionally surviving children.

## 2. Etiology

### Causal factors and genetic risk

AOC is etiologically heterogeneous.

1. **OTX2** encodes an orthodenticle homeobox transcription factor essential for anterior neural and craniofacial patterning. Human heterozygous variants—including sequence variants and an in-frame duplication—have been reported across anophthalmia, pituitary, forebrain, and otocephaly/dysgnathia phenotypes. The foundational human report is Chassaing et al., *Journal of Medical Genetics*, published May 2012, DOI: https://doi.org/10.1136/jmedgenet-2012-100892. Strong mouse evidence supports haploinsufficiency, dosage sensitivity, variable expressivity, and genetic-background modification. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 9-10)

2. **PRRX1** encodes a paired-related homeobox transcription factor involved in craniofacial mesenchyme. Recurrent familial AOC caused by a replication-slippage variant was reported by Dasouki et al., *American Journal of Medical Genetics A*, published April 2013, DOI: https://doi.org/10.1002/ajmg.a.35879. Disease summaries identify *PRRX1* together with *OTX2* as a principal causal gene. (behunova2025facialbonedefects pages 19-20)

3. **SMAD3** was implicated in a 2020 report expanding the phenotypic spectrum of SMAD3-related disease to agnathia–otocephaly (Meier et al., *Molecular Genetics & Genomic Medicine*, February 2020, DOI: https://doi.org/10.1002/mgg3.1178). This should be represented as **limited/emerging evidence**, not as equivalent to the replicated *OTX2* association.

4. **Chromosomal abnormalities** have occasionally been described in the broader otocephaly literature. Chromosomal microarray is therefore appropriate, but no single recurrent copy-number change is established as the predominant cause.

5. **Phenocopies and syndromic overlap:** severe agnathia can occur in tetra-amelia syndromes caused by biallelic loss of **WNT3** or **RSPO2**. Such cases should not automatically be merged with classic AOC. RSPO2 expression in limb buds, branchial arches, and lung mesenchyme explains the combined craniofacial, limb, and pulmonary phenotype. (behunova2025facialbonedefects pages 17-19)

### Environmental and lifestyle risk

Older human reports have proposed maternal diabetes, alcohol, and teratogenic exposures, but no exposure has a replicated disease-specific effect estimate. In mice, ethanol can generate related craniofacial defects in susceptible C57BL/6 backgrounds, supporting biological plausibility for gene–environment interaction, but this is not proof of causation in human AOC. (matsuo1995mouseotx2functions pages 7-9)

Smoking, diet, exercise, occupation, infection, radiation, and parental age have no established AOC-specific risk estimates. Maternal copper/mining exposure was discussed in a 2020 case from the Katanga Copperbelt (DOI: https://doi.org/10.1002/bdr2.1758), but a single ecological/case observation cannot establish causality.

### Protective factors and gene–environment interaction

No protective allele, medication, diet, or lifestyle intervention has been demonstrated. Standard preconception measures—avoidance of alcohol and known teratogens, diabetes control, and folate supplementation—remain general congenital-anomaly prevention measures, not proven AOC-specific prevention. The marked strain dependence of *Otx2* heterozygous mouse phenotypes demonstrates **modifier-gene effects**: C57BL/6 enhanced severe/lethal craniofacial disease, whereas CBA background suppressed it. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9)

## 3. Phenotypes

All core manifestations are prenatal/congenital and structurally stable after development; their consequences, such as airway obstruction or feeding impairment, become acute at delivery.

| Phenotype | Type, course, and likely frequency | Suggested HPO label |
|---|---|---|
| Absent mandible | Defining physical sign; congenital, severe, nonprogressive | Agnathia |
| Severe mandibular hypoplasia | May replace complete agnathia in milder spectrum cases | Micrognathia; mandibular hypoplasia |
| Ventromedially displaced ears | Defining sign, usually bilateral; intrinsic hearing may be less impaired than position suggests | Low-set ears; abnormal ear position; melotia |
| Midline-fused ears | Severe end of auricular-position spectrum; not obligatory | Synotia |
| Very small oral aperture | Common/severe; compromises access, feeding, and airway management | Microstomia |
| Small or absent tongue | Commonly described; severe feeding, speech, and airway consequences | Microglossia; aglossia |
| Airway obstruction/respiratory failure | Immediate perinatal emergency; major mortality driver | Upper-airway obstruction; respiratory insufficiency |
| Polyhydramnios | Prenatal secondary sign caused by impaired swallowing | Polyhydramnios |
| Holoprosencephaly/cyclopia spectrum | Variable, not obligatory; indicates extensive anterior patterning failure | Holoprosencephaly; cyclopia |
| Eye/nasal abnormalities | Variable microphthalmia, anophthalmia, abnormal nose or nasal cavities | Microphthalmia; anophthalmia; abnormality of the nose |
| Palatal/choanal abnormalities | Variable; increase airway and feeding morbidity | Cleft palate; choanal atresia |
| Situs inversus/visceral anomalies | Reported in a subset, not defining | Situs inversus totalis; congenital heart defect |

Microstomia, micro-/aglossia, and holoprosencephaly are recognized components, while ear defects may principally involve position rather than hearing. (behunova2025facialbonedefects pages 19-20) Quantitative percentages cannot be assigned reliably because publication bias, inconsistent terminology, and tiny case series dominate the evidence.

**Quality of life:** no AOC-specific EQ-5D, SF-36, PROMIS, or caregiver-burden dataset was found. In survivors, tracheostomy dependence, impaired oral feeding, inability to articulate normally, facial difference, repeated reconstruction, and communication needs imply profound lifelong effects. These conclusions arise from selected survivor reports rather than population-level measurement.

## 4. Genetic and molecular information

### Gene-level interpretation

- **OTX2:** strongest disease mechanism is heterozygous germline loss of function/haploinsufficiency, although altered-function in-frame variants are also reported. Human expressivity spans severe lethal otocephaly to ocular, pituitary, palatal, or velopharyngeal phenotypes. A 2015 in-frame duplication report is available at https://doi.org/10.1038/jhg.2014.122.
- **PRRX1:** germline variants disrupting a developmental transcription factor can cause recurrent familial AOC. Both dominant and recessive interpretations have appeared across limited literature; recurrence counseling must therefore be variant- and family-specific rather than based solely on the syndrome label.
- **SMAD3:** provisional/limited association. Functional connection to TGF-β signaling is plausible, but replication is insufficient.
- **WNT3/RSPO2:** relevant mainly to the differential diagnosis of tetra-amelia with agnathia, especially where limb absence is present. (behunova2025facialbonedefects pages 17-19)

Exact HGNC IDs, ClinVar accessions, HGVS variants, ACMG classifications, and gnomAD/TOPMed frequencies were not recoverable from the full-text evidence assembled here. They should be populated by variant-level ClinVar and gnomAD queries rather than inferred from article titles. Causal variants are expected to be germline and extremely rare; there is no evidence that somatic mutation is a routine mechanism.

### Modifiers, epigenetics, and structural variation

The clearest modifier evidence is the strain-dependent penetrance of *Otx2* haploinsufficiency in mice. No named human modifier allele, founder variant, disease-specific methylation signature, histone abnormality, repeat expansion, or mitochondrial cause is established. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9)

## 5. Environmental information

No infectious agent causes AOC, and the disorder is neither contagious nor zoonotic. No disease-specific association has been validated for pollution, smoking, alcohol, pharmaceuticals, occupational exposure, or nutritional deficiency. Experimental ethanol susceptibility and isolated exposure-associated reports justify careful maternal exposure history, but not attribution of an individual case without stronger evidence. (matsuo1995mouseotx2functions pages 7-9)

Suggested chemical ontology annotation, only when documented in a case or model: **CHEBI: ethanol**. Do not encode copper, glyphosate, or other chemicals as established causes from case-level evidence.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** reduced or altered activity of an anterior-patterning transcription factor—most securely OTX2, and in some families PRRX1—or another early developmental insult.
2. **Early embryonic defect:** abnormal specification, proliferation, survival, or patterning of rostral neuroepithelium and cranial neural crest/ectomesenchyme.
3. **Arch-level defect:** failure of distal first-pharyngeal-arch mandibular mesenchyme to grow and differentiate into Meckel cartilage, dentary/mandible, and related tissues.
4. **Anatomical sequence:** absent mandible shortens the lower face; the ears remain low and move medially, while tongue, oral cavity, palate, and nasal structures develop abnormally.
5. **Downstream clinical consequences:** impaired fetal swallowing produces polyhydramnios; at birth, absent mandibular support, abnormal tongue/oral anatomy, and restricted airway cause respiratory obstruction and feeding failure. Coexisting forebrain malformation worsens neurologic and survival outcomes.

In *Otx2* heterozygous mice, affected structures include the distal Meckel cartilage, dentary, maxilla, palate, anterior skull base, nasal capsule, eyes, and selected neural-crest-derived ganglia. Hyoid-arch structures can remain preserved, demonstrating a rostrally restricted developmental field defect. (matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 10-11, mina2001regulationofmandibular pages 5-6, matsuo1995mouseotx2functions pages 6-7)

At 9.5–10.5 days post coitum, mutant mice show retarded rostral neuroepithelial development and reduced mitotic activity; homozygotes lack forebrain and midbrain and terminate anterior to rhombomere 3. This supports a dosage-dependent failure of tissue growth and regional identity rather than post-developmental tissue destruction. (matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 6-7)

### Pathways and ontology suggestions

- **GO biological processes:** neural crest cell development; neural crest cell migration; pharyngeal arch morphogenesis; embryonic cranial skeleton morphogenesis; anterior/posterior pattern specification; regionalization; regulation of cell proliferation; palate development; eye development.
- **Cell Ontology:** cranial neural crest cell; ectomesenchymal cell; neuroepithelial cell; chondrocyte; osteoblast; oral epithelial cell.
- **GO cellular components:** nucleus and chromatin are relevant because OTX2/PRRX1/SMAD3 are transcriptional regulators; no lysosomal, mitochondrial, ion-channel, or protein-aggregation defect is established.
- **Signaling:** OTX2-centered transcriptional patterning, TGF-β/SMAD signaling, and—primarily in differential syndromes—WNT/RSPO signaling. FGF8 and BMP4 participate in first-arch patterning, but a direct disease-specific biochemical defect in either pathway has not been demonstrated.

No validated patient transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, organoid, CRISPR-screen, or multi-omics signature was found. Immune activation, inflammation, fibrosis, ischemia, and metabolic intoxication are not recognized primary mechanisms.

## 7. Anatomical structures affected

### Primary structures

- mandible/dentary and Meckel cartilage;
- first pharyngeal arch and its ectomesenchyme;
- oral aperture, floor of mouth, and tongue;
- external ears, principally their position;
- palate, pharynx, and upper airway.

### Variable secondary structures

- forebrain and midbrain, including holoprosencephaly;
- eyes, optic structures, nose, nasal cavities, and anterior skull base;
- middle-ear ossicles and tympanic bone;
- heart, lungs, gastrointestinal tract, limbs, and laterality structures in syndromic or phenocopy cases.

Mouse data show particularly severe defects anterior to the basisphenoid, including the basisphenoid/presphenoid region, orbitosphenoid, nasal capsule/septum, ethmoid cartilage, tongue, palate, and olfactory tissues. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 6-7)

**Suggested UBERON labels:** first pharyngeal arch; mandible; Meckel cartilage; tongue; oral cavity; external ear; middle ear; palate; pharynx; forebrain; midbrain; nasal cavity; cranial neural crest. The mandibular and auricular findings are ordinarily bilateral/midline-patterned rather than unilateral.

## 8. Temporal development

AOC begins during **early embryogenesis**, when anterior neural structures and the first arch are being specified. It is recognizable prenatally and is fully congenital. It does not have conventional early/intermediate/advanced clinical stages, remission, relapse, or adult onset.

- **Critical developmental window:** gastrulation through early pharyngula/first-arch development.
- **Prenatal evolution:** impaired swallowing can lead to progressive polyhydramnios; imaging recognition may improve as mandibular absence and abnormal ear position become conspicuous.
- **Perinatal critical window:** delivery is the major intervention point because airway obstruction can be immediately fatal.
- **Postnatal course in survivors:** the malformation is stable, but airway, feeding, speech, dentofacial growth, and reconstructive requirements change with age.

*Otx2* expression in relevant mouse rostral tissues begins around 7.5 dpc, with first-arch and neuroepithelial abnormalities apparent by 8.5–10.5 dpc. (matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 10-11, matsuo1995mouseotx2functions pages 6-7)

## 9. Inheritance and population

### Epidemiology

AOC is generally described as **extremely rare**, historically on the order of approximately one case per tens of thousands of births, but no recent population registry provides a precise, reproducible incidence or prevalence estimate. Published counts combine spontaneous abortions, terminated pregnancies, stillbirths, and live births and are vulnerable to underdiagnosis and inconsistent terminology. No credible annual incidence per 100,000, sex ratio, ethnic enrichment, geographic cluster, or age distribution can therefore be stated.

### Inheritance

- Most cases are sporadic.
- *OTX2*-related disease is commonly modeled as autosomal dominant with variable expressivity and incomplete penetrance. Mouse heterozygotes demonstrate haploinsufficiency and strong genetic-background effects. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 7-9)
- *PRRX1*-related recurrence requires family-specific interpretation; parental testing is essential.
- De novo occurrence, parental mosaicism, inherited variants with reduced penetrance, and autosomal-recessive phenocopies must all be considered.
- No anticipation mechanism, repeat expansion, founder effect, or population carrier frequency is established.
- Consanguinity increases concern for recessive syndromic mimics, including tetra-amelia, but is not a universal AOC risk factor.

## 10. Diagnostics

### Prenatal diagnosis

The principal test is targeted **fetal ultrasonography**, with midsagittal facial views used to assess the mandibular profile. Three-dimensional ultrasound can clarify absent jaw anatomy and abnormal ear position. Findings that should prompt suspicion include absent mandibular shadow/profile, microstomia, low medial ears, abnormal tongue, polyhydramnios, and associated holoprosencephaly. A four-case first-trimester series was published in 2019 (DOI: https://doi.org/10.1002/jum.14759).

**Fetal MRI** is useful for confirming mandibular absence, defining tongue/pharyngeal relationships, evaluating the brain, and planning airway management. Fetal echocardiography and a detailed anatomic survey assess syndromic involvement.

### Postnatal assessment

When live birth is planned, evaluation may include:

- direct airway endoscopy;
- CT/3D CT for skeletal anatomy and reconstruction;
- brain MRI;
- echocardiography and abdominal/renal imaging;
- audiology, despite potentially preserved hearing;
- feeding/swallow studies;
- dental, speech, and craniofacial assessment.

No serum enzyme, metabolite, protein biomarker, electrophysiologic signature, or histopathologic criterion is diagnostic.

### Genetic-testing strategy

1. **Chromosomal microarray** as a first-tier test for a fetus with multiple congenital anomalies.
2. **Trio exome or genome sequencing**, particularly when microarray is nondiagnostic.
3. Analysis should prioritize **OTX2** and **PRRX1**, while considering **SMAD3** cautiously and phenotype-directed genes such as **WNT3/RSPO2** in limb-reduction syndromes.
4. Sequence analysis should be paired with deletion/duplication detection; genome sequencing may detect noncoding, structural, or mosaic variants missed by exome sequencing.
5. Confirm candidate variants by an orthogonal method and test parents for inheritance/mosaicism.

Karyotyping remains useful when aneuploidy or a large rearrangement is suspected. FISH is targeted rather than routine. Mitochondrial, repeat-expansion, liquid-biopsy, metabolomic, and epigenomic tests have no established role.

### Differential diagnosis

- severe isolated micrognathia/Pierre Robin sequence—mandible is present and ears are not characteristically fused;
- Treacher Collins and other mandibulofacial dysostoses—bilateral mandibular/zygomatic hypoplasia rather than complete agnathia;
- cerebrocostomandibular syndrome;
- acrofacial dysostoses;
- tetra-amelia syndromes—major limb absence with *WNT3* or *RSPO2* involvement; (behunova2025facialbonedefects pages 17-19)
- holoprosencephaly syndromes with severe facial anomalies;
- hypoglossia–hypodactyly spectrum;
- caudal/first-arch disruption phenotypes from teratogenic exposures.

There are no universally adopted formal diagnostic criteria beyond recognition of the defining anatomical complex.

## 11. Outcome and prognosis

Prognosis is usually poor because severe airway obstruction is present at birth and major CNS or visceral anomalies may coexist. Fetal loss, termination after prenatal diagnosis, stillbirth, and early neonatal death dominate the literature. Nevertheless, isolated forms with successful airway establishment can survive into childhood or adulthood.

No defensible 5-year or 10-year survival rates, life expectancy, standardized disability estimates, or prognostic biomarker models exist. Important case-specific prognostic factors are:

- complete agnathia versus residual mandibular tissue;
- airway anatomy and feasibility of tracheostomy/EXIT;
- brain malformation severity;
- pulmonary, cardiac, gastrointestinal, and laterality anomalies;
- ability to establish enteral nutrition;
- access to multidisciplinary craniofacial care.

Long-term complications include chronic airway dependence, aspiration, enteral-feeding dependence, speech/communication impairment, dental malocclusion or absent dentition, facial-growth disturbance, and repeated surgery. Recovery of the absent mandible does not occur spontaneously.

## 12. Treatment and current real-world implementation

There is no curative drug, pathway-targeted therapy, gene therapy, RNA therapy, cell therapy, immunotherapy, or pharmacogenomic treatment. No relevant interventional clinical trial was identified.

### Perinatal airway algorithm

1. Prenatally define facial, pharyngeal, pulmonary, and CNS anatomy.
2. Conduct multidisciplinary counseling involving maternal–fetal medicine, neonatology, anesthesiology, pediatric otolaryngology, craniofacial/plastic surgery, genetics, and palliative care.
3. If airway obstruction is expected and active neonatal treatment is selected, plan delivery at a tertiary fetal center.
4. Consider an **ex-utero intrapartum treatment (EXIT)** procedure to maintain placental oxygenation while securing the airway. A 2023 isolated-AOC EXIT case is reported at https://doi.org/10.12659/AJCR.939016.
5. Establish a surgical airway when oral or nasal intubation is impossible; provide ventilation and intensive care.

Suggested MAXO labels: fetal imaging; delivery planning; airway management; endotracheal intubation; tracheostomy; EXIT procedure; mechanical ventilation.

### Nutrition and rehabilitation

Enteral feeding through nasogastric or gastrostomy access is often necessary. Survivors require speech-language therapy, augmentative communication, audiology, dental/orthodontic management, occupational therapy, psychosocial support, and coordinated craniofacial follow-up.

### Reconstruction

Highly selected survivors may undergo staged mandibular reconstruction, distraction procedures, bone grafting, or vascularized free-flap reconstruction. A 2023 report described a free fibula flap in a 10-year-old with severe AOC (Cohen et al., *Journal of Craniofacial Surgery*, published October 2023, DOI: https://doi.org/10.1097/SCS.0000000000009017). Such reports demonstrate technical feasibility but do not provide generalizable response rates.

Suggested MAXO labels: mandibular reconstruction; free tissue transfer; bone grafting; gastrostomy; speech therapy; feeding therapy; orthodontic treatment; palliative care.

## 13. Prevention

No AOC-specific primary prevention is proven. Appropriate measures are:

- preconception genetic counseling after an affected pregnancy;
- parental testing when a fetal pathogenic variant is identified;
- avoidance of alcohol and recognized teratogens and optimization of maternal diabetes as general congenital-anomaly prevention;
- targeted early ultrasound in subsequent pregnancies;
- chorionic-villus sampling or amniocentesis for a known familial variant;
- preimplantation genetic testing for a confirmed familial pathogenic variant.

There is no vaccine, prophylactic medication, newborn-screening program, or population carrier-screening recommendation. Secondary prevention consists of early prenatal detection and delivery planning; tertiary prevention focuses on avoiding hypoxic airway injury, aspiration, malnutrition, and reconstructive complications.

## 14. Other species and natural disease

Comparable congenital agnathia/otocephaly phenotypes have been observed in vertebrates, but a well-defined naturally inherited veterinary syndrome with breed-specific epidemiology was not identified. There is no transmission or zoonotic potential.

Relevant taxonomy for the principal experimental model is **Mus musculus**, NCBI Taxonomy **10090**. Orthologous *Otx2* is evolutionarily conserved in anterior head patterning. Comparative interpretation should distinguish naturally occurring malformations from engineered mutants and teratogen-induced phenocopies.

## 15. Model organisms

### Otx2 mouse

The most informative model is the engineered *Otx2* loss-of-function mouse described by Matsuo et al., *Genes & Development*, published November 1995, DOI: https://doi.org/10.1101/gad.9.21.2646.

- **Heterozygotes:** approximately half-normal gene dosage, variable micrognathia/agnathia, eye and nasal defects, anterior skull-base abnormalities, and perinatal death; a few animals survive. (matsuo1995mouseotx2functions pages 2-3, matsuo1995mouseotx2functions pages 1-2)
- **Homozygotes:** profound rostral truncation with loss of forebrain and midbrain anterior to rhombomere 3, demonstrating an earlier and more severe phenotype than typical human AOC. (matsuo1995mouseotx2functions pages 7-9, matsuo1995mouseotx2functions pages 1-2)
- **Recapitulated biology:** dosage sensitivity, first-arch/mandibular abnormalities, anterior neurocranial defects, ocular anomalies, and variable severity.
- **Applications:** defining embryonic critical periods, lineage dependence, modifier effects, and candidate pathways.
- **Limitations:** homozygous mutants are substantially more severe than human disease; strain effects complicate penetrance; mouse auricular and airway anatomy differ from humans; the model does not reproduce every visceral or neurologic association.

The strongest experimental observations include defects in distal first-arch structures and relative sparing of more caudal/hyoid derivatives, supporting a region-specific rather than generalized neural-crest failure. (matsuo1995mouseotx2functions pages 9-10, matsuo1995mouseotx2functions pages 10-11, mina2001regulationofmandibular pages 5-6)

## Recent developments, expert interpretation, and research priorities

Recent clinical progress has been practical rather than molecular: prenatal recognition, fetal MRI, planned EXIT airway management, and complex childhood mandibular reconstruction now make survival possible in carefully selected isolated cases. The 2023 EXIT and free-fibula reports are important demonstrations of feasibility, not evidence of standardized efficacy. The 2021 disease-focused review, Dubucs et al., “Re-focusing on agnathia-otocephaly complex,” DOI: https://doi.org/10.1007/s00784-020-03443-w, emphasizes that AOC is a heterogeneous developmental spectrum requiring precise phenotyping rather than reliance on historical terminology.

A 2025 micro-CT analysis further showed that superficially similar agnathia can arise in tetra-amelia and other neurocristopathies, reinforcing the need to separate classic AOC from syndromic phenocopies. Biallelic *WNT3*/*RSPO2* disease should particularly be considered when limb and pulmonary abnormalities coexist. (behunova2025facialbonedefects pages 17-19)

The principal unresolved questions are the proportion attributable to *OTX2* and *PRRX1*, the role of noncoding or structural variants, human modifier genes underlying incomplete penetrance, and whether single-cell or spatial studies can identify the exact vulnerable cranial-neural-crest populations. International prospective case registration with standardized HPO phenotyping is needed before credible frequencies, survival estimates, or genotype–phenotype correlations can be calculated.

## Evidence-source classification and quotation note

- **Human clinical/genetic evidence:** fetal/neonatal case reports, small prenatal series, family reports, and exceptional survivor surgical reports.
- **Model-organism evidence:** engineered *Otx2* mouse studies provide the strongest causal developmental evidence.
- **In-vitro/omics evidence:** no disease-specific patient-cell, organoid, single-cell, proteomic, or metabolomic dataset was identified.
- **Computational evidence:** useful for variant prioritization but not independently diagnostic.

Exact verbatim abstract text was not available for most human papers in the retrieved corpus; therefore, no purported “direct abstract quotations” are fabricated here. One defensible summary from the retrieved recent literature is that AOC is characterized by severe microstomia, micro-/aglossia, possible holoprosencephaly, and pathogenic involvement of *PRRX1* and *OTX2*. (behunova2025facialbonedefects pages 19-20) PMID values should likewise be imported from PubMed records during curation rather than inferred from DOI metadata.

References

1. (matsuo1995mouseotx2functions pages 2-3): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

2. (matsuo1995mouseotx2functions pages 7-9): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

3. (matsuo1995mouseotx2functions pages 9-10): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

4. (matsuo1995mouseotx2functions pages 6-7): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

5. (behunova2025facialbonedefects pages 19-20): Jana Behunova, Helga Rehder, Anton Dobsak, Susanne G. Kircher, Lucas L. Boer, Andreas A. Mueller, Janina M. Patsch, Eduard Winter, Roelof-Jan Oostra, Eva Piehslinger, and Karoline M. Reich. Facial bone defects associated with lateral facial clefts tessier type 6, 7 and 8 in syndromic neurocristopathies: a detailed micro-ct analysis on historical museum specimens. Biology, 14:872, Jul 2025. URL: https://doi.org/10.3390/biology14070872, doi:10.3390/biology14070872. This article has 1 citations.

6. (matsuo1995mouseotx2functions pages 10-11): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

7. (mina2001regulationofmandibular pages 5-6): Mina Mina. Regulation of mandibular growth and morphogenesis. Critical reviews in oral biology and medicine : an official publication of the American Association of Oral Biologists, 12 4:276-300, Jul 2001. URL: https://doi.org/10.1177/10454411010120040101, doi:10.1177/10454411010120040101. This article has 80 citations.

8. (matsuo1995mouseotx2functions pages 1-2): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

9. (matsuo1995mouseotx2functions pages 11-12): I. Matsuo, Shigem Kuratani, Chiham Kimura, N. Takeda, and S. Aizawa. Mouse otx2 functions in the formation and patterning of rostral head. Genes & development, 9 21:2646-58, Nov 1995. URL: https://doi.org/10.1101/gad.9.21.2646, doi:10.1101/gad.9.21.2646. This article has 813 citations and is from a highest quality peer-reviewed journal.

10. (behunova2025facialbonedefects pages 17-19): Jana Behunova, Helga Rehder, Anton Dobsak, Susanne G. Kircher, Lucas L. Boer, Andreas A. Mueller, Janina M. Patsch, Eduard Winter, Roelof-Jan Oostra, Eva Piehslinger, and Karoline M. Reich. Facial bone defects associated with lateral facial clefts tessier type 6, 7 and 8 in syndromic neurocristopathies: a detailed micro-ct analysis on historical museum specimens. Biology, 14:872, Jul 2025. URL: https://doi.org/10.3390/biology14070872, doi:10.3390/biology14070872. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Agnathia-Otocephaly_Complex-deep-research-falcon_artifacts/artifact-00.md)