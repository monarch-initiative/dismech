---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:41:53.425008'
end_time: '2026-07-31T00:48:26.401592'
duration_seconds: 392.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Agnathia-Otocephaly Complex
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
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
- **Category:** Mendelian

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
- **Category:** Mendelian

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


# Agnathia–Otocephaly Complex: Disease Characteristics Research Report

**Scope and evidence note.** Agnathia–otocephaly complex (AGOTC) is ultra-rare; consequently, most human evidence consists of fetal or neonatal case reports, small case series, pathology reviews, and individual molecular diagnoses. Frequencies, penetrance, survival rates, and treatment-response statistics are therefore not estimable reliably. Assertions below are labeled when evidence is limited or model-derived.

| Domain | Summary | Key details / evidence level | Suggested structured terms / notes |
|---|---|---|---|
| Definition / core phenotype | Rare congenital first-pharyngeal-arch malformation complex characterized by severe mandibular underdevelopment or absence with abnormal ear position and oral anomalies; holoprosencephaly is variably present. | Review text states AGOTC is a "rare malformation with failure of the first arch development" characterized by agnathia, ventromedial ear position, microstomia, and holoprosencephaly (human review evidence) (kruszka2018syndromesassociatedwith pages 4-6). | HPO: Agnathia, Microstomia, Synotia/abnormal ear position, Aglossia/Microglossia, Holoprosencephaly. UBERON: mandible, external ear, oral cavity, forebrain. |
| Key genes and evidence level | Genetic heterogeneity is supported, but evidence is limited to rare families/case reports and reviews. | **PRRX1**: associated with AGOTC in human reports/reviews (moderate human evidence from rare familial cases/reviews) (kruszka2018syndromesassociatedwith pages 4-6). **OTX2**: reported in otocephaly-dysgnathia/AGOTC spectrum in case literature cited by reviews/search results; not directly retrieved in context here (suggestive but not directly quoted in retrieved context). **SMAD3**: emerging prenatal association from case literature noted in recent review/search results; evidence currently very limited and syndromic expansion remains uncertain. **CRKL**: not established AGOTC gene in humans, but loss in mouse produces overlapping craniofacial/forebrain phenotype (model evidence) (miller2014amousesplicesite pages 1-2). | HGNC genes: PRRX1, OTX2, SMAD3, CRKL. Label OTX2/SMAD3 as limited evidence here because no direct full-text context was retrieved. |
| Inheritance | Likely genetically heterogeneous; both de novo and familial recurrence have been reported in literature, but inheritance is not uniform across all cases. | PRRX1-related disease has been described in recurrent familial settings in the broader literature, but the retrieved review emphasizes association rather than a single consistent inheritance mode; many cases are sporadic. For AGOTC overall, inheritance should be recorded as **variable / not fully defined**. | Ontology note: Mendelian disorder category is appropriate, but case-level inheritance should be captured gene-by-gene. |
| Onset / prognosis | Congenital, detected prenatally or at birth; prognosis is usually poor and often lethal because of severe craniofacial and airway anomalies, with rare long-term survivors requiring major supportive/surgical care. | Onset is prenatal/congenital by definition. Review and case-literature searches indicate many cases are lethal; however, rare survival into childhood/adulthood has been reported outside retrieved context. Prognosis should be marked **usually lethal; rare survival**. | HPO: Congenital onset. Important complications: airway obstruction, feeding difficulty, associated brain malformations. |
| Diagnosis | Primarily prenatal/postnatal anatomic diagnosis supported by imaging and genomic testing. | Typical workflow: prenatal ultrasound ± 3D ultrasound and fetal MRI to define absent/hypoplastic mandible, abnormal ear position, polyhydramnios, and associated anomalies; postnatal exam/autopsy; genomic testing via trio exome/genome or targeted craniofacial/developmental gene analysis. No standardized disease-specific biomarker or formal diagnostic criteria were identified. | HPO/LOINC-style annotations: prenatal ultrasound finding, fetal MRI finding, exome sequencing. Mark laboratory biomarkers as unavailable. |
| Management | No disease-modifying therapy; management is supportive and anatomy-driven, especially airway planning. | Reported real-world approaches include pregnancy counseling, multidisciplinary delivery planning, EXIT-based airway establishment in selected fetuses, tracheostomy/intubation when feasible, feeding and respiratory support, and palliative care when anomalies are incompatible with sustained survival. Evidence base is case-report level; no trials found. | MAXO suggestions: airway management, tracheostomy, ex utero intrapartum treatment (EXIT), feeding support, palliative care, genetic counseling. |
| Epidemiology | Extremely rare; robust prevalence/incidence estimates unavailable. | The retrieved review explicitly describes AGOTC as rare (kruszka2018syndromesassociatedwith pages 4-6). Published literature consists mainly of isolated case reports and small reviews; no reliable population prevalence, incidence, sex ratio, or carrier frequency was identified in retrieved context. | Record prevalence/incidence as **unknown; ultra-rare based on case literature**. |
| Principal ontology terms | Core developmental, anatomical, and phenotype mappings for knowledge-base use. | Biological process: first pharyngeal arch development; craniofacial morphogenesis; forebrain development. Cell types: cranial neural crest-derived mesenchymal cells / first-arch mesenchyme. Model evidence supports disrupted oropharyngeal developmental signaling and altered retinoic acid/endothelin signaling in overlapping mouse phenotypes (miller2014amousesplicesite pages 1-2). | GO: craniofacial development, pharyngeal arch development, forebrain development. CL: cranial neural crest cell, mesenchymal cell. UBERON: mandible, tongue, external ear, forebrain. HPO: agnathia, microstomia, aglossia, synotia, holoprosencephaly. |


*Table: This table condenses the most clinically and biologically relevant facts about Agnathia-Otocephaly Complex for knowledge-base entry use. It highlights what is established, what is supported only by limited case-based evidence, and where data remain unavailable.*

## 1. Disease information

AGOTC is a congenital malformation spectrum caused by severe failure of first-pharyngeal-arch development. Its defining combination is absence or extreme hypoplasia of the mandible, a very small mouth, and ventromedial displacement or fusion of the ears; absent or hypoplastic tongue and forebrain anomalies may coexist. An authoritative review states directly: **“Agnathia-Otocephaly complex (AGOTC) is a rare malformation with failure of the first arch development”** and identifies agnathia, ventromedial ears, microstomia, and holoprosencephaly as characteristic findings. Importantly, holoprosencephaly is variable rather than obligatory. (kruszka2018syndromesassociatedwith pages 4-6)

**Synonyms:** agnathia–otocephaly complex; otocephaly; agnathia–microstomia–synotia syndrome; agnathia–microstomia–synotia–aglossia complex; otocephaly–dysgnathia complex. “Isolated agnathia” should not automatically be equated with full AGOTC.

**Identifiers:** OMIM commonly treats the molecularly defined spectrum under **Agnathia–otocephaly complex (AGOTC)** and related PRRX1/OTX2 entries; Orphanet uses **agnathia–otocephaly complex**. A stable disease-specific ICD-10 or ICD-11 code is not generally used; cases are coded under congenital craniofacial/mandibular malformations. MeSH indexing usually uses combinations such as *Jaw Abnormalities*, *Micrognathism*, *Ear Deformities, Congenital*, and *Holoprosencephaly*. MONDO should be verified against the current MONDO release before database ingestion because mappings and preferred labels can change; do not infer an identifier from similarly named isolated-agnathia entities.

The information is primarily **aggregated disease-level literature derived from individual fetuses, neonates, and rare survivors**, not population-scale EHR data.

## 2. Etiology, risk, and protective factors

### Genetic causes

AGOTC is genetically heterogeneous.

* **PRRX1** encodes a paired-related homeobox transcription factor involved in mesenchymal and craniofacial morphogenesis. Human PRRX1 variants have been associated with AGOTC, including recurrent familial disease attributed to replication slippage. The retrieved review specifically names PRRX1 as an associated gene but notes that PRRX1-associated AGOTC cases in that literature did not have holoprosencephaly, supporting phenotypic heterogeneity. (kruszka2018syndromesassociatedwith pages 4-6)
* **OTX2**, a dosage-sensitive homeobox regulator of anterior neural and craniofacial development, has been implicated by heterozygous variants in the otocephaly–dysgnathia spectrum. The key primary report is Chassaing et al., *Journal of Medical Genetics*, published May 2012, DOI: https://doi.org/10.1136/jmedgenet-2012-100892. An in-frame OTX2 duplication was subsequently reported with AGOTC/asymmetric velopharyngeal insufficiency: Sergouniotis et al., published January 2015, DOI: https://doi.org/10.1038/jhg.2014.122.
* **SMAD3** has been proposed from a prenatal AGOTC case as an expansion of the SMAD3-related phenotype. This is **limited single-case evidence**, not proof that SMAD3 is a recurrent AGOTC gene: Meier et al., published February 2020, DOI: https://doi.org/10.1002/mgg3.1178.
* **Chromosomal/CNV causes:** cytogenetically abnormal cases have been reported, but no single recurrent AGOTC-defining chromosomal lesion is established. CMA remains appropriate because AGOTC can occur within a multiple-malformation presentation.

### Environmental and gene–environment factors

Case reports have temporally associated AGOTC with maternal topical salicylate, first-trimester oxymetazoline, and other exposures. These uncontrolled observations cannot establish teratogenic causality. No reproducible lifestyle, infectious, occupational, sex-specific, or maternal-age risk factor has been demonstrated. Reports of drug exposure should therefore be encoded as **suspected exposure associations**, not causes.

No validated genetic or environmental protective factors exist. There are no demonstrated protective alleles, dietary interventions, vaccines, or prophylactic drugs. A specific human gene–environment interaction has not been established.

## 3. Phenotypes

All core manifestations begin during embryogenesis and are present congenitally. Severity is usually extreme and anatomically stable; downstream respiratory and feeding consequences emerge at birth.

| Manifestation | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Absent mandible/mandibular arch | Physical sign; congenital, severe, nonprogressive | Defining or near-defining | **Agnathia** (verify current HP identifier) |
| Extreme mandibular hypoplasia | Physical sign; congenital | Spectrum cases | **Micrognathia, HP:0000347** |
| Microstomia | Physical sign; congenital, severe | Core feature | **Microstomia, HP:0000160** |
| Ventromedial ears, closely approximated or fused ears | Physical sign; congenital | Core otocephaly feature | **Abnormal external ear position**; **Synotia** where fused |
| Aglossia or microglossia | Physical sign; congenital | Common but not obligatory | **Aglossia, HP:0010295**; microglossia |
| Holoprosencephaly | Structural CNS sign; congenital; severity variable | Variable; not required and not consistently present in PRRX1 cases | **Holoprosencephaly, HP:0001360**; subtype terms when known |
| Pharyngeal occlusion/upper-airway obstruction | Clinical/anatomic sign; immediate neonatal emergency | Major determinant of survival | **Upper airway obstruction, HP:0002781** |
| Polyhydramnios | Prenatal sign, secondary to impaired swallowing | Recurrently reported | **Polyhydramnios, HP:0001561** |
| Feeding/swallowing impairment | Functional sign; severe and persistent in survivors | Expected from oral/pharyngeal anatomy | **Dysphagia, HP:0002015**; feeding difficulties |
| Respiratory failure/distress | Clinical sign at birth | Common consequence of airway anatomy | **Neonatal respiratory distress, HP:0002643** |
| Associated cranial, cardiac, skeletal, or visceral anomalies | Structural signs | Variable; especially in syndromic cases | Use case-specific HPO terms |

The related agnathia–microstomia–synotia phenotype is described as presenting with agnathia, mandibular hypoplasia, anteromedial ears, microstomia, and aglossia or microglossia; some reported cases also have holoprosencephaly. (kruszka2018syndromesassociatedwith pages 4-6)

**Quality of life:** no validated AGOTC-specific EQ-5D, SF-36, PROMIS, or caregiver-burden datasets exist. In survivors, tracheostomy/ventilation, enteral feeding, impaired speech, hearing problems, repeated craniofacial procedures, and neurologic disability can impose profound lifelong burdens.

## 4. Genetic and molecular information

### Genes and variants

| Gene | Role/evidence | Variant classes and functional interpretation |
|---|---|---|
| **PRRX1** (HGNC:9142) | Best-supported recurrent AGOTC gene; mesenchymal homeobox transcription factor | Reported pathogenic alleles include sequence/length-changing variants; disease mechanism is generally disruption of transcription-factor dosage/function. Variant-level ACMG classification must be taken from the exact ClinVar record, not assigned generically. |
| **OTX2** (HGNC:8522) | Human otocephaly–dysgnathia/AGOTC-spectrum evidence | Heterozygous sequence variants and an in-frame duplication have been reported; altered dosage or transcriptional function is plausible. Variable expressivity is substantial. |
| **SMAD3** (HGNC:6769) | Candidate/limited AGOTC association | A prenatal case expanded the SMAD3 phenotype; insufficient recurrent evidence to designate all SMAD3 variants as AGOTC-causing. |
| **CRKL** (HGNC:2363) | Modifier/candidate pathway evidence, not established monogenic human AGOTC gene | Mouse splice-loss causes overlapping micrognathia, aglossia, pharyngeal occlusion, and holoprosencephaly with altered signaling. (miller2014amousesplicesite pages 1-2) |

Variants causing severe congenital disease are expected to be germline and very rare or absent from population databases, but exact gnomAD/1000 Genomes/TOPMed frequencies must be recorded **variant by variant**. There is no evidence that somatic variants, repeat expansions, or mitochondrial variants are typical causes. No validated modifier gene, protective allele, founder variant, methylation signature, or disease-specific epigenetic biomarker has been established.

PRRX1 loss of function is biologically credible as a dosage mechanism: a separate human PRRX1 truncating allele failed to transactivate downstream targets in a reporter assay, demonstrating that truncation can abolish transcriptional activity, although that family had atrial fibrillation/patent ductus arteriosus rather than AGOTC. This supports protein-function interpretation but not direct AGOTC pathogenicity for every loss-of-function allele.

## 5. Environmental information

There is no confirmed toxin, radiation exposure, pollutant, diet, smoking pattern, alcohol exposure, or infection that specifically causes AGOTC. Published exposure cases—including topical salicylate and oxymetazoline—are hypothesis-generating only. No infectious organism or zoonotic agent is implicated. CHEBI annotations should be attached only to documented case exposures, with relation **“temporally associated with”**, not “causes disease.”

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream developmental disruption:** pathogenic alteration in a craniofacial/anterior-patterning transcriptional regulator such as PRRX1 or OTX2, or potentially signaling mediator SMAD3.
2. **Cellular target:** cranial neural crest-derived ectomesenchyme and mesenchymal progenitors populating the first pharyngeal arch, with possible concomitant disruption of anterior neuroectoderm/forebrain patterning.
3. **Process failure:** abnormal migration, proliferation, survival, differentiation, and patterning of first-arch mesenchyme; deficient formation of Meckel cartilage and mandibular skeletal/connective tissues.
4. **Primary anatomy:** absent/severely hypoplastic mandible, microstomia, abnormal tongue and pharyngeal development, and secondary ventromedial approximation of ears.
5. **Downstream physiology:** impaired fetal swallowing produces polyhydramnios; at delivery, pharyngeal occlusion and inability to intubate cause hypoxia or death; feeding and speech remain profoundly impaired in survivors.
6. **Parallel forebrain pathway:** where anterior neural patterning is also disrupted, holoprosencephaly and neurologic impairment occur. The absence of HPE in some molecularly confirmed cases shows that mandibular and forebrain phenotypes can dissociate. (kruszka2018syndromesassociatedwith pages 4-6)

A Crkl-deficient mouse provides pathway-level evidence. Its phenotype includes micrognathia, pharyngeal occlusion, aglossia, and holoprosencephaly, alongside increased retinoic-acid and endothelin signaling. The authors conclude that Crkl has a central role in signaling in the developing oropharyngeal complex. This is mechanistic model evidence, not proof that altered CRKL causes most human AGOTC. (miller2014amousesplicesite pages 1-2)

**Suggested GO biological processes:** pharyngeal arch development; neural crest cell migration/differentiation; craniofacial morphogenesis; skeletal system morphogenesis; cartilage development; anterior neural plate/forebrain development; regulation of transcription by RNA polymerase II; TGF-β receptor signaling.

**Suggested cells:** cranial neural crest cell; ectomesenchymal cell; chondrocyte progenitor; osteoblast progenitor; pharyngeal-arch mesenchymal cell. Use **CL:0000333 mesenchymal cell** and the current CL term for neural crest cell after ontology-release validation.

**Subcellular components:** PRRX1, OTX2, and SMAD3 act predominantly through nuclear transcriptional regulation; suggested GO-CC terms include nucleus, nucleoplasm, transcription-regulator complex, and for SMAD signaling, cytoplasm-to-nucleus translocation. No AGOTC-specific metabolic, immune, inflammatory, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature has been validated.

## 7. Anatomical structures affected

**Primary structures:** first pharyngeal arch, mandible/Meckel cartilage, oral cavity, tongue, pharynx, external/middle ear region, and upper airway. **Secondary/variable structures:** forebrain, palate, cranial base, heart, limbs, and other viscera in syndromic cases.

**Suggested UBERON mappings:** first pharyngeal arch; mandible (**UBERON:0001684**); Meckel cartilage; oral cavity (**UBERON:0000167**); tongue (**UBERON:0001723**); pharynx (**UBERON:0001042**); external ear; forebrain (**UBERON:0001890**). Exact IDs should be validated against the target ontology release.

The defect is generally bilateral/midline and severe rather than a unilateral mandibular anomaly. At the cellular level, affected tissues are neural-crest-derived connective tissue, cartilage, bone, oral/pharyngeal epithelium, and associated muscle patterning.

## 8. Temporal development

AGOTC begins during early embryonic craniofacial patterning, when cranial neural crest populates the first arch and mandibular structures are specified. It is therefore **congenital, prenatal-onset, and non-remitting**. The structural malformation itself is not progressive; clinical deterioration at birth reflects abrupt loss of placental gas exchange in the presence of an unmanageable airway.

There are no validated disease stages. A clinically useful temporal framework is: (1) embryonic malformation; (2) prenatal detection, often with polyhydramnios; (3) delivery/airway crisis; and (4) chronic airway, feeding, speech, hearing, reconstructive, and neurologic morbidity in rare survivors. The critical intervention window is **before and during delivery**, when fetal imaging and an airway plan—including possible EXIT—can change immediate survival.

## 9. Inheritance and population

No reliable population prevalence or incidence exists. AGOTC is best classified as **ultra-rare**, based on isolated reports and small series rather than registries. There are no defensible sex-ratio, ethnicity, geographic-distribution, carrier-frequency, or age-distribution estimates.

Inheritance is gene- and variant-dependent. Many cases are sporadic and potentially de novo; recurrent familial PRRX1-associated disease demonstrates that recurrence can be Mendelian. Variable expressivity is clear across the otocephaly–dysgnathia spectrum. Penetrance is not quantified. Anticipation is not reported. Germline mosaicism cannot be excluded after an apparently de novo event. Consanguinity is relevant when a recessive mechanism is suspected, but it is not a universal feature. No robust founder effect is known.

## 10. Diagnostics

### Prenatal diagnosis

* **Two-dimensional ultrasound:** absent mandibular contour, abnormal facial profile, microstomia, low/medial ears, inability to visualize normal tongue, polyhydramnios, and associated CNS or visceral anomalies.
* **Three-dimensional ultrasound:** improves surface visualization and parental/surgical understanding; first-trimester diagnosis has been reported.
* **Fetal MRI:** defines tongue/pharyngeal obstruction, airway anatomy, forebrain, and associated abnormalities and is particularly useful for delivery planning.
* **Postmortem examination/autopsy:** remains valuable for complete phenotyping and genotype–phenotype interpretation when pregnancy ends in fetal or neonatal death.

A 2023 primary report described prenatal diagnosis followed by an **ex-utero intrapartum treatment (EXIT)** strategy for isolated AGOTC: Suemitsu et al., published April 2023, DOI: https://doi.org/10.12659/AJCR.939016. A 2024 prenatal case reinforces that current diagnostic literature remains case-based: Konukcu, published December 2024, DOI: https://doi.org/10.1002/bdr2.2421.

### Genetic testing workflow

1. Detailed phenotype and three-generation pedigree.
2. Conventional karyotype when aneuploidy or rearrangement is suspected.
3. **Chromosomal microarray** to detect pathogenic CNVs.
4. **Trio exome or genome sequencing**, prioritizing PRRX1, OTX2, and phenotype-driven craniofacial/forebrain genes; genome sequencing may detect noncoding or structural changes missed by exome sequencing.
5. Sanger/orthogonal confirmation, parental segregation, and recurrence-risk interpretation.

A small “AGOTC panel” may miss newly associated genes; trio ES/GS is preferable when rapid testing is available. FISH is useful only for a suspected locus-specific rearrangement. Mitochondrial and repeat-expansion testing have no routine role. RNA sequencing may clarify splice variants but is not established as a clinical AGOTC assay.

**Differential diagnosis:** severe isolated micrognathia/Pierre Robin sequence; auriculocondylar syndrome; mandibulofacial dysostoses (Treacher Collins, Nager, Miller syndromes); cerebro-costo-mandibular syndrome; hypomandibular faciocranial syndrome; persistent buccopharyngeal membrane; acrofacial dysostoses; and syndromic holoprosencephaly. The defining absence of the mandibular arch plus ventromedial/synotic ears distinguishes classic AGOTC.

No formal consensus diagnostic criteria, laboratory biomarker, newborn-screening assay, or population-screening program exists.

## 11. Outcome and prognosis

AGOTC is usually lethal through stillbirth, termination after prenatal diagnosis, or neonatal airway failure. Precise overall, 5-year, or 10-year survival rates are unavailable. Holoprosencephaly, complete pharyngeal occlusion, severe prematurity, pulmonary complications, and multiple-organ anomalies worsen prognosis. Better outcomes are associated with a patent distal airway, absence of major brain/visceral anomalies, prenatal diagnosis, and successful airway establishment.

Rare long-term survival demonstrates that AGOTC is not invariably fatal. A longitudinal surgical report followed a severely affected individual from birth into adulthood: Golinko et al., published November 2015, DOI: https://doi.org/10.1097/SCS.0000000000002150. Such survivors may have chronic tracheostomy dependence, recurrent respiratory complications, enteral-feeding dependence, hearing/speech impairment, and repeated reconstruction. There are no validated prognostic molecular biomarkers or quality-of-life datasets.

## 12. Treatment and real-world implementation

There is **no pharmacologic, gene, RNA, cell, or immune therapy** that reverses the embryonic malformation. ClinicalTrials.gov searching identified no relevant interventional AGOTC trial.

### Practical management

* Prenatal multidisciplinary conference: maternal–fetal medicine, neonatology, pediatric anesthesia, otolaryngology, craniofacial surgery, genetics, radiology, nursing, palliative care, and ethics.
* Delivery at a tertiary center with a predefined airway algorithm.
* If imaging suggests airway obstruction but a potentially viable distal airway, consider **EXIT-to-airway**, fetoscopic evaluation, tracheoscopy, or tracheostomy. Evidence is limited to case reports, including the 2023 EXIT report above.
* Postnatal respiratory support, tracheostomy care, gastrostomy/enteral nutrition, aspiration prevention, hearing evaluation, communication support, and staged individualized craniofacial reconstruction.
* When anatomy or associated anomalies are incompatible with sustained survival, comfort-focused palliative care is appropriate.

**Suggested MAXO terms:** genetic counseling; prenatal ultrasonography; fetal MRI; exome sequencing; airway management; endotracheal intubation; tracheostomy; mechanical ventilation; gastrostomy; enteral feeding; reconstructive surgery; palliative care. EXIT may require a local extension if no exact MAXO term exists.

Treatment-response percentages and comparative adverse-event rates are unavailable. Pharmacogenomics is not relevant to the underlying defect.

## 13. Prevention

There is no proven primary prevention beyond standard preconception and prenatal care and avoidance of unnecessary potentially teratogenic exposures. Vaccination is not relevant.

**Secondary prevention/early detection:** targeted first-trimester and mid-trimester ultrasound in a pregnancy with prior AGOTC; diagnostic testing for a known familial variant using chorionic-villus sampling or amniocentesis; preimplantation genetic testing for monogenic disease where a pathogenic familial variant is known.

**Tertiary prevention:** prenatal airway assessment and planned tertiary-center delivery can reduce catastrophic unplanned airway failure; feeding and respiratory support may prevent aspiration, malnutrition, and hypoxic injury.

Genetic counseling should explain genetic heterogeneity, uncertainty after negative testing, potential germline mosaicism, and gene-specific recurrence. A negative panel does not reduce recurrence risk to zero.

## 14. Other species and natural disease

Comparable congenital agnathia/otocephaly can occur sporadically in domestic animals as a developmental anomaly, but no well-established breed-specific, ortholog-defined natural veterinary disorder equivalent to human PRRX1/OTX2-related AGOTC was identified. No VBO breed annotation is justified. There is no zoonotic potential or cross-species transmission.

Orthologs include mouse **Prrx1, Otx2, Smad3,** and **Crkl**. Their conservation supports comparative developmental study, but engineered phenocopies should not be encoded as naturally occurring disease.

## 15. Model organisms and advanced systems

### Mouse

* **Prrx1-deficient mice:** craniofacial and skeletal defects support PRRX1’s role in mesenchymal morphogenesis. Depending on allele/background, models do not necessarily reproduce the complete human ear–mandible–forebrain combination.
* **Crkl “snoopy” splice mutant:** loss of Crkl protein produces variably penetrant micrognathia, pharyngeal occlusion, aglossia, and holoprosencephaly and alters retinoic-acid/endothelin signaling. It is useful for first-arch/oropharyngeal pathway analysis but is not a direct genetically matched model for most human AGOTC. (miller2014amousesplicesite pages 1-2)
* **Otx2 models:** useful for anterior neural and craniofacial dosage biology, but early lethality and species-/allele-specific phenotypes complicate direct translation.

### Human cellular systems

Human pluripotent stem cells can be differentiated into expandable **PRRX1-positive limb-bud-like mesenchymal cells**, providing a tractable system for mesenchymal differentiation, cartilage formation, variant functionalization, and chemical screening. The reported platform used PRRX1 reporter cells, RNA-seq, and three-dimensional chondrogenic differentiation; it is not yet an AGOTC organoid and does not reproduce first-arch spatial patterning or airway anatomy. (yamada2021inductionandexpansion pages 1-11)

Promising future approaches include cranial-neural-crest/first-arch organoids, isogenic CRISPR knock-in lines, single-cell transcriptomics, and spatial profiling of model craniofacial tissues. As of 2024, these remain research opportunities rather than validated AGOTC diagnostics or treatments.

## Recent developments and expert assessment

The most clinically consequential recent development is refinement of prenatal imaging and **planned fetal-airway intervention**, illustrated by the 2023 EXIT case. The 2024 literature remains dominated by prenatal case recognition rather than molecular cohorts or therapeutic studies. This reflects the disorder’s extreme rarity, early lethality, inconsistent nomenclature, and incomplete postmortem genomic investigation.

The authoritative interpretation is therefore cautious: AGOTC is a developmental endpoint rather than a single-gene syndrome; PRRX1 and OTX2 are the principal established genes, SMAD3 is an emerging limited association, and mouse/pathway findings should not be mistaken for confirmed human causation. Building a useful disease knowledge base will require case-level capture of anatomy, HPE status, complete variant data, parental segregation, pregnancy outcome, airway anatomy, and survival rather than relying on a single aggregate phenotype label.

References

1. (kruszka2018syndromesassociatedwith pages 4-6): Paul Kruszka and Maximilian Muenke. Syndromes associated with holoprosencephaly. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 178:229-237, May 2018. URL: https://doi.org/10.1002/ajmg.c.31620, doi:10.1002/ajmg.c.31620. This article has 94 citations.

2. (miller2014amousesplicesite pages 1-2): Kerry A. Miller, Tiong Y. Tan, Megan F. Welfare, Susan M. White, Zornitza Stark, Ravi Savarirayan, Trent Burgess, Andrew A. Heggie, Georgina Caruana, John F. Bertram, John F. Bateman, and Peter G. Farlie. A mouse splice-site mutant and individuals with atypical chromosome 22q11.2 deletions demonstrate the crucial role for crkl in craniofacial and pharyngeal development. Molecular Syndromology, 5:276-286, Nov 2014. URL: https://doi.org/10.1159/000368865, doi:10.1159/000368865. This article has 21 citations and is from a peer-reviewed journal.

3. (yamada2021inductionandexpansion pages 1-11): Daisuke Yamada, Masahiro Nakamura, Tomoka Takao, Shota Takihira, Aki Yoshida, Shunsuke Kawai, Akihiro Miura, Lu Ming, Hiroyuki Yoshitomi, Mai Gozu, Kumi Okamoto, Hironori Hojo, Naoyuki Kusaka, Ryosuke Iwai, Eiji Nakata, Toshifumi Ozaki, Junya Toguchida, and Takeshi Takarada. Induction and expansion of human prrx1+ limb-bud-like mesenchymal cells from pluripotent stem cells. Nature Biomedical Engineering, 5:926-940, Aug 2021. URL: https://doi.org/10.1038/s41551-021-00778-x, doi:10.1038/s41551-021-00778-x. This article has 67 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Agnathia-Otocephaly_Complex-deep-research-falcon_artifacts/artifact-00.md)