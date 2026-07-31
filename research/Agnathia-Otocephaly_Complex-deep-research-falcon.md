---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:14:30.287382'
end_time: '2026-07-31T00:20:12.308165'
duration_seconds: 342.02
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


# Agnathia–Otocephaly Complex: Disease Characteristics Report

## Executive summary

Agnathia–otocephaly complex (AOC; also **otocephaly–agnathia complex**, **agnathia–holoprosencephaly–synotia syndrome**, and historically **otocephaly**) is an extremely rare, usually lethal congenital craniofacial malformation spectrum. Its defining defect is absence or extreme hypoplasia of the mandible, accompanied by abnormally low, ventromedially displaced ears that may meet in the midline (synotia), with microstomia and abnormalities of the tongue, palate, airway, and sometimes forebrain. It represents early failure of first-pharyngeal-arch and cranial-neural-crest development rather than a postnatal progressive disease.

Human molecular evidence establishes marked locus and allelic heterogeneity. **OTX2** and **PRRX1** are the best-supported reported genes; individual reports have implicated additional loci, including **SMAD3**, but these secondary associations require replication. Developmental studies place the disorder within interacting FGF, SHH, BMP, endothelin-1, WNT, and Notch gene-regulatory networks controlling cranial-neural-crest survival, pharyngeal-arch polarity, and cartilage-versus-bone differentiation. No disease-modifying treatment or interventional trial was identified.

The evidence base is unusually limited: case reports, fetal pathology series, small prenatal-imaging series, and developmental models predominate. Consequently, numerical phenotype frequencies, penetrance, incidence, survival rates, quality-of-life scores, and treatment-response statistics are not reliably known.

| Domain | Summary | Ontology / IDs | Evidence |
|---|---|---|---|
| Definition | Rare congenital craniofacial malformation complex characterized by severe first pharyngeal arch developmental failure, classically including agnathia or extreme mandibular hypoplasia with ventromedial/displaced ears (synotia/melotia) and frequent microstomia/agnathia-spectrum anomalies; often lethal because of major airway and associated malformations. | Confirmed disease label: Agnathia-Otocephaly Complex; Suggested ontology: MONDO not confirmed from retrieved evidence; Suggested MeSH/ICD/Orphanet lookup required in curated databases. | (barske2016competitionbetweenjaggednotch pages 30-31, fabik2021themandibularand pages 14-16) |
| Identifiers | Evidence retrieved here is mainly from aggregated disease-level case reports/reviews plus prenatal case literature, not EHR cohorts. No exact OMIM/Orphanet/MONDO identifier was directly confirmed in the retrieved context. | Confirmed: none from retrieved context; Suggested: add OMIM/Orphanet/MONDO after database verification. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Core phenotype / HPO | Core features include agnathia, severe micrognathia, otocephaly/synotia, mandibular arch defects, loss or severe reduction of Meckel cartilage derivatives, and frequent associated craniofacial anomalies. Suggested HPO terms: Agnathia, Micrognathia, Synotia/Melotia, Microstomia, Cleft palate, Glossoptosis/agnathia-spectrum tongue anomalies, Holoprosencephaly when present. | Confirmed exact HPO IDs: none from retrieved context; Suggested HPO mapping only. | (barske2016competitionbetweenjaggednotch pages 30-31, fabik2021themandibularand pages 18-20, fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 16-17) |
| Genes | Human genetic evidence supports heterogeneity with OTX2 and PRRX1 as the most established reported disease genes; SMAD3 has been reported as an emerging/expanded phenotype association. | Confirmed gene symbols: OTX2, PRRX1; Suggested/emerging: SMAD3. HGNC IDs not confirmed from retrieved context. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Inheritance | Usually sporadic, but recurrent familial cases have been reported. Evidence includes a heterozygous PRRX1 frameshift and a consanguineous family report, indicating genetic heterogeneity and possible variable inheritance patterns rather than a single consistent mode. Recurrence counseling is therefore case-specific and should incorporate molecular findings. | Confirmed inheritance mode: not singularly established in retrieved context; Suggested labels: de novo/autosomal dominant in some OTX2 or PRRX1 cases, possible recessive mechanism in some families. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Mechanism / pathophysiology | Developmental mechanism centers on abnormal neural crest–derived mandibular/hyoid arch patterning and osteochondroprogenitor fate. Relevant upstream pathways include SHH, FGF8/FGF3, BMP, EDN1, Jagged-Notch, and transcriptional regulators such as PRRX1/PRRX2, DLX5/6, HAND2, MEIS/PBX. Model evidence indicates Prrx1/Prrx2 loss can shift chondrogenic vs osteogenic fate and disrupt Meckel cartilage; ISL1 loss causes agnathia. | Suggested GO terms: neural crest cell development, pharyngeal arch morphogenesis, cartilage development, ossification; Suggested CL term: cranial neural crest cell. Exact IDs not confirmed here. | (fabik2021themandibularand pages 18-20, fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 24-25, fabik2021themandibularand pages 16-17) |
| Diagnosis | Most cases are identified prenatally or at birth by characteristic craniofacial anatomy. Prenatal ultrasound and fetal MRI are key for detecting absent/severely hypoplastic mandible and abnormal low/medial ear position; molecular diagnosis may use trio exome/genome sequencing or targeted testing of OTX2/PRRX1 where suspected. | Suggested modalities: prenatal ultrasound, fetal MRI, postnatal exam, genomic sequencing; no disease-specific diagnostic criteria ID confirmed. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Prognosis | Prognosis is generally poor; the condition is frequently perinatally lethal due to profound craniofacial malformation and airway compromise, especially in severe agnathic presentations and when associated brain or multisystem malformations are present. Survivors appear uncommon and likely represent milder spectrum disease. | Suggested outcome terms: perinatal lethality, respiratory failure/airway compromise; exact ontology IDs not confirmed. | (barske2016competitionbetweenjaggednotch pages 30-31, fabik2021themandibularand pages 14-16) |
| Management | No disease-specific curative therapy is established. Management is supportive and individualized: prenatal counseling, delivery planning, airway stabilization at birth when feasible, evaluation for associated anomalies, palliative care in lethal presentations, and genetic counseling for recurrence risk. | Suggested MAXO terms: genetic counseling, prenatal imaging, airway management, palliative care, surgical airway/feeding support if survivable; exact MAXO IDs not confirmed. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Epidemiology | Extremely rare. Robust prevalence/incidence estimates were not identified in retrieved evidence; literature remains dominated by isolated case reports and small reviews/series. | Confirmed quantitative estimate: none from retrieved context. | (barske2016competitionbetweenjaggednotch pages 30-31) |
| Models | Mouse and zebrafish developmental models are informative rather than exact disease replicas. Prrx1/Prrx2 compound knockout mice show severe lower jaw defects and altered osteogenic/chondrogenic balance; zebrafish studies place prrx1 genes in BMP/EDN1/Notch-regulated facial cartilage differentiation networks; ISL1 loss causes agnathia in mouse developmental studies cited by review literature. | Suggested species terms: Mus musculus, Danio rerio; exact model registry IDs not confirmed. | (fabik2021themandibularand pages 18-20, fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 24-25, fabik2021themandibularand pages 16-17) |
| Evidence gaps | Major gaps include lack of validated epidemiology, no standardized clinical diagnostic criteria, incomplete genotype-phenotype correlation, sparse confirmed variant-level data in the retrieved context, little evidence for environmental/protective factors, no interventional trials, and limited 2023-2024 advances beyond additional prenatal case-based reports and developmental reviews. | Suggested curation actions: verify OMIM/Orphanet/MONDO/HPO/MAXO IDs in authoritative databases; add variant-level ClinVar/gnomAD evidence separately. | (barske2016competitionbetweenjaggednotch pages 30-31, fabik2021themandibularand pages 18-20, fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 24-25, fabik2021themandibularand pages 16-17) |


*Table: This compact table summarizes high-yield knowledge-base facts for Agnathia-Otocephaly Complex, including what is confirmed from the retrieved evidence versus what still requires database verification. It is useful for rapid curation of disease definition, phenotype, genetics, mechanism, diagnosis, prognosis, and evidence gaps.*

## 1. Disease information

### Definition and scope

AOC is a congenital malformation complex characterized by:

* **Agnathia** or extreme mandibular hypoplasia;
* **Otocephaly**, meaning ventromedial displacement of the external ears, often with **synotia**;
* Microstomia and tongue defects, ranging from microglossia or hypoglossia to aglossia;
* Severe upper-airway distortion or obstruction;
* Variable associated anomalies, particularly holoprosencephaly and other craniofacial, cardiac, skeletal, gastrointestinal, genitourinary, or limb defects.

The term describes a spectrum. Complete agnathia with synotia is its most severe form, whereas rare survivors generally have less complete mandibular deficiency. The retrieved evidence derives from **aggregated disease-level literature and individual published fetuses or children**, not representative EHR cohorts or population registries.

### Identifiers and terminology

* **Preferred label:** Agnathia–otocephaly complex.
* **Common alternatives:** otocephaly; agnathia–otocephaly; otocephaly–dysgnathia complex; agnathia–holoprosencephaly–synotia syndrome; agnathia with synotia/melotia.
* **OMIM:** AOC is commonly indexed as the agnathia–otocephaly complex phenotype, but an exact phenotype identifier was not directly verified in the retrieved full-text evidence and should be confirmed against the current OMIM release before ingestion.
* **Orphanet/MONDO/MeSH:** Dedicated or mapped rare-malformation concepts may exist, but exact current identifiers were not recoverable from the source corpus. Do not assign an unverified identifier automatically.
* **ICD-10/ICD-11:** No highly specific disease code was found; cases are generally represented under congenital malformations of facial bones/jaw or other specified congenital facial malformations.

## 2. Etiology

### Genetic causal factors

AOC is genetically heterogeneous.

1. **OTX2** encodes a homeobox transcription factor essential for anterior neural plate, forebrain, eye, pituitary, and craniofacial development. Heterozygous sequence variants and deletions have been reported across an OTX2-related spectrum that includes classic AOC, mandibular dysostosis, eye defects, and pituitary abnormalities. The landmark human study was Chassaing *et al.*, *Journal of Medical Genetics*, May 2012, DOI: https://doi.org/10.1136/jmedgenet-2012-100892. An in-frame OTX2 duplication was subsequently reported with AOC and asymmetric velopharyngeal insufficiency (Sergouniotis *et al.*, January 2015; DOI: https://doi.org/10.1038/jhg.2014.122).

2. **PRRX1** encodes a paired-related homeobox transcription factor active in craniofacial mesenchyme. Human reports include a **heterozygous frameshift** and recurrent disease attributed to **DNA-replication slippage in PRRX1**. These data support a dominant loss-of-function mechanism in at least some families, although individual case reports do not establish universal inheritance or penetrance (Dasouki *et al.*, April 2013; DOI: https://doi.org/10.1002/ajmg.a.35879). (barske2016competitionbetweenjaggednotch pages 30-31)

3. **SMAD3** was proposed in a fetal case as an expansion of the SMAD3-related phenotype to include agnathia–otocephaly (Meier *et al.*, February 2020; DOI: https://doi.org/10.1002/mgg3.1178). This should be curated as **limited/emerging human evidence**, not equivalent to the replicated OTX2/PRRX1 associations.

4. Cytogenetic abnormalities and non-diagnostic molecular findings have been described in individual cases, reinforcing heterogeneity, but no recurrent chromosomal lesion accounts for most AOC.

### Variant interpretation

Reported disease variants include frameshift, missense or other coding changes, in-frame duplication, and whole-gene/segmental deletions. They are constitutional/germline findings, not somatic disease drivers. Exact ACMG classification must be performed variant by variant using segregation, de-novo status, functional evidence, ClinVar assertions, and population frequency. Because severe AOC is strongly selected against, genuinely causal fully penetrant variants are expected to be absent or exceptionally rare in population databases; that expectation is not a substitute for direct gnomAD review.

### Environmental and maternal factors

Historic literature has discussed maternal diabetes and teratogenic exposures, but causal evidence is weak. A fetus with AOC and limb defects was reported following first-trimester maternal oxymetazoline exposure (Menezes *et al.*, August 2016; DOI: https://doi.org/10.1111/jog.13014); a single temporal association cannot establish teratogenicity. No validated infectious, dietary, occupational, tobacco, alcohol, radiation, or pollution cause was identified.

### Risk, protective, and gene–environment factors

* **Established risk:** a pathogenic familial variant in an implicated gene; prior affected pregnancy when no cause has been identified may still indicate parental germline mosaicism or an undetected inherited mechanism.
* **Possible risk:** consanguinity in selected families, although AOC is not uniformly recessive; one consanguineous report alone is insufficient to assign a general AR mode. (barske2016competitionbetweenjaggednotch pages 30-31)
* **Protective variants or modifiers:** none validated.
* **Environmental protective factors:** none disease-specific established. Standard preconception control of diabetes and avoidance of nonessential potentially teratogenic exposures are prudent but not proven AOC-specific prevention.
* **Gene–environment interaction:** biologically plausible because pharyngeal-arch development depends on tightly timed signaling, but no human interaction has been quantified.

## 3. Phenotypes

All defining manifestations are **prenatal/congenital**, anatomically stable after formation, and usually severe. “Progression” is therefore inappropriate; morbidity evolves from the fixed malformation, especially airway and feeding consequences.

| Manifestation | Type and course | Frequency/effect | Suggested HPO term |
|---|---|---|---|
| Absent mandible | Physical sign; congenital, severe, nonprogressive | Defining in complete AOC | Agnathia |
| Extreme mandibular hypoplasia | Physical sign; congenital | Spectrum feature, including milder survivors | Micrognathia / mandibular hypoplasia |
| Medial/ventral ear displacement | Physical sign | Defining otocephalic feature | Abnormal external-ear position |
| Midline fusion or approximation of ears | Physical sign | Common in severe classic cases | Synotia; melotia where appropriate |
| Small oral opening | Physical sign | Common; compromises access, feeding, airway | Microstomia |
| Absent/small tongue | Physical sign | Variable | Aglossia; hypoglossia; microglossia |
| Cleft or abnormal palate | Physical sign | Variable | Cleft palate / abnormality of the palate |
| Airway obstruction/respiratory failure | Clinical sign | Major proximate cause of neonatal death | Upper-airway obstruction; respiratory insufficiency |
| Polyhydramnios | Prenatal sign | May result from impaired fetal swallowing | Polyhydramnios |
| Holoprosencephaly or other CNS anomaly | Imaging/pathology sign | Variable, not required | Holoprosencephaly and subtype-specific terms |
| Ocular/pituitary defects | Clinical/imaging findings | Especially relevant to OTX2-related disease | Microphthalmia/anophthalmia; pituitary abnormality as observed |
| Limb, cardiac, gastrointestinal, renal or genital anomalies | Physical/imaging signs | Case-dependent | Map each observed lesion separately |

Reliable percentages cannot be calculated from ascertainment-biased case reports. Likewise, no validated AOC-specific EQ-5D, SF-36, PROMIS, behavioral, psychiatric, or laboratory phenotype data exist. For rare survivors, dependence on airway/feeding support, impaired speech and oral function, hearing impairment, repeated surgery, and neurodevelopmental disability may profoundly affect quality of life.

## 4. Genetic and molecular information

### Gene-level annotation

* **OTX2:** transcriptional regulator; likely haploinsufficiency or disruption of DNA-binding/transcriptional activity in many cases. Its broad developmental role explains variable eye, forebrain, pituitary, and mandibular manifestations.
* **PRRX1:** mesenchymal homeobox regulator affecting craniofacial skeletal progenitor differentiation. Reported frameshift/slippage alleles support loss of function. (barske2016competitionbetweenjaggednotch pages 30-31)
* **SMAD3:** TGF-β pathway signal transducer; currently limited AOC-specific evidence.

No validated modifier gene, disease-specific methylation episignature, recurrent histone abnormality, somatic mutation, repeat expansion, mitochondrial defect, or founder allele was identified. No carrier frequency can be estimated responsibly.

### Chromosomal abnormalities

Chromosomal microarray remains relevant because congenital-malformation phenotypes can result from copy-number changes encompassing OTX2 or other developmental loci. Karyotyping is appropriate when aneuploidy or a large rearrangement is suspected, but neither karyotype nor FISH is the preferred stand-alone test for sequence-level OTX2/PRRX1 variants.

## 5. Environmental information

There is no established environmental form of AOC and no evidence that it is infectious or transmissible. The oxymetazoline-exposed pregnancy is hypothesis-generating only. Lifestyle factors have not been evaluated in controlled studies. No CHEBI annotation should be entered as causative based solely on isolated exposure reports.

## 6. Mechanism and pathophysiology

### Causal developmental chain

**Upstream developmental disruption**—for example OTX2 or PRRX1 dysfunction, or disturbed FGF/SHH/BMP/EDN1 signaling—occurs during early craniofacial patterning. This alters survival, migration, positional identity, or differentiation of **cranial neural crest-derived ectomesenchyme** in the first pharyngeal arch. Abnormal dorsoventral patterning and osteochondral fate selection then impair Meckel cartilage and mandibular-bone formation. Loss of mandibular support produces microstomia, abnormal tongue/palate positioning, and ventromedial relocation of the ears. The resulting distorted upper airway and associated forebrain/multisystem defects cause perinatal respiratory failure and lethality.

### Pathways and cellular processes

* SHH from oropharyngeal epithelium supports mesenchymal survival and Meckel-cartilage development.
* FGF8/FGF3 contribute to pharyngeal-endoderm segmentation, neural-crest-cell survival, and osteogenic expression; experimental loss of FGF8 produces mandibular-cartilage hypoplasia.
* BMP and endothelin-1 establish pharyngeal-arch dorsoventral pattern. WNT contributes to chondroblast-versus-osteoblast fate choice. SOX9, RUNX2, and SP7 govern downstream skeletal differentiation. (fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 16-17)
* The conserved EDN1–DLX5/6–HAND2 axis specifies ventral mandibular/hyoid-arch identity, interacting with MEIS/PBX and PRRX factors. (fabik2021themandibularand pages 24-25)
* Prrx1/Prrx2 compound-mutant mice have a micrognathic, anteriorly fused lower jaw, reduced dentition, expanded RUNX2-positive regions, accelerated osteogenesis, and loss of Meckel cartilage—evidence that incorrect chondrogenic/osteogenic allocation can generate the mandibular phenotype. (fabik2021themandibularand pages 18-20)
* Experimental loss of ISL1 in relevant embryonic lineages causes agnathia, illustrating that AOC is a convergent endpoint of several regulatory disruptions rather than a single-gene syndrome. (fabik2021themandibularand pages 14-16)

Suggested annotations include **GO: neural crest cell development/migration; pharyngeal arch morphogenesis; cartilage development; chondrocyte differentiation; osteoblast differentiation; ossification; embryonic cranial skeleton morphogenesis**. Suggested cell types are **cranial neural crest cell**, pharyngeal-arch ectomesenchymal cell, chondroprogenitor/chondrocyte, and osteoprogenitor/osteoblast. Exact ontology identifiers should be validated against the current GO and Cell Ontology releases.

### Omics and advanced technologies

No reproducible patient transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omics signature was identified. There is also no validated CRISPR screen specific to AOC. Current mechanistic interpretation largely extrapolates from conventional developmental genetics and model-organism expression/perturbation studies.

## 7. Anatomical structures affected

**Primary:** mandible, Meckel cartilage and other first-arch derivatives; oral cavity; tongue; palate; external ears; pharyngeal airway.

**Secondary/associated:** forebrain, eyes, pituitary, middle/external ear, hyoid region, heart, lungs, gastrointestinal tract, kidneys/genital tract, and limbs depending on genotype and case.

**Tissue/cell level:** neural crest-derived craniofacial mesenchyme, cartilage, bone, oral/pharyngeal epithelium, and developing neural tissues.

**Subcellular:** no disease-specific organelle pathology. OTX2 and PRRX1 are principally nuclear transcription factors; SMAD3 transduces signals to the nucleus.

Suggested anatomical mappings include **UBERON: mandible, Meckel cartilage, first pharyngeal arch, hyoid arch, tongue, oral cavity, palate, external ear, pharynx, forebrain, eye, and pituitary gland**. Ear displacement is generally bilateral and medial in classic disease, but asymmetry can occur.

## 8. Temporal development

Onset is embryonic, during early craniofacial and pharyngeal-arch formation. The critical vulnerability window is therefore in the first trimester, well before clinical birth. Prenatal manifestations may become visible in the first trimester with high-quality imaging, although diagnosis is often easier later.

There are no conventional early/intermediate/end-stage disease stages, remission, relapse, or postnatal disease progression. Severe cases culminate in fetal demise, termination after prenatal diagnosis, stillbirth, or neonatal death. Rare survivors represent incomplete/milder developmental forms rather than remission.

## 9. Inheritance and population

### Epidemiology

AOC is **ultra-rare**. The literature is composed primarily of isolated cases and small fetal/pathology or ultrasound series; robust incidence and prevalence per 100,000, sex ratio, geographic gradients, ethnic enrichment, and age distributions are unavailable. Claims such as “one per tens of thousands of births” vary across secondary sources and should not be entered as high-confidence statistics without a defined denominator.

### Inheritance

Most reported cases are sporadic. De-novo dominant variation is plausible and documented for portions of the OTX2/PRRX1 spectrum; familial recurrence and a heterozygous PRRX1 frameshift have also been reported. A consanguineous case has been cited, but this does not make AOC generally autosomal recessive. (barske2016competitionbetweenjaggednotch pages 30-31)

Penetrance and expressivity are insufficiently quantified and likely gene- and allele-dependent. OTX2 in particular shows broad variable expressivity. Germline mosaicism should be discussed after an apparently de-novo event. No anticipation, founder effect, or population-specific carrier frequency is established.

## 10. Diagnostics

### Prenatal and clinical diagnosis

The principal diagnostic test is detailed fetal ultrasound, looking for absent mandibular contour, extreme micrognathia, abnormal facial profile, low/medial ears, microstomia, polyhydramnios, and associated anomalies. Three-dimensional ultrasound can improve surface depiction; fetal MRI clarifies airway, tongue, palate, ear position, and CNS anatomy. First-trimester diagnosis has been demonstrated in a four-case series (Rodriguez *et al.*, August 2019; DOI: https://doi.org/10.1002/jum.14759). Recent literature remains case-based, including a 2024 prenatal case report (Konukcu, December 2024; DOI: https://doi.org/10.1002/bdr2.2421).

Postmortem examination, radiography or CT, and placental/fetal pathology can confirm anatomy and document associated malformations. There is no characteristic biochemical biomarker, blood test, enzyme assay, electrophysiologic result, or histochemical stain.

### Recommended genetic workflow

1. Detailed fetal and parental phenotyping and three-generation pedigree.
2. Chromosomal microarray, particularly for a fetus with multiple congenital anomalies.
3. Trio exome or genome sequencing, with copy-number and structural-variant analysis.
4. Focused review of **OTX2** and **PRRX1**, plus phenotype-directed analysis of other craniofacial-development genes; **SMAD3** should be interpreted cautiously.
5. Parental testing of a candidate variant to determine inheritance and recurrence implications.
6. Genome reanalysis when initial testing is negative.

WGS may detect noncoding, structural, or complex variants missed by WES. RNA sequencing could help selected splice variants but is not an established diagnostic assay. Mitochondrial DNA and repeat-expansion testing are not routinely indicated. FISH is useful only for confirming a suspected locus-specific rearrangement.

### Differential diagnosis

Differentials include isolated severe micrognathia; Pierre Robin sequence; cerebro-costo-mandibular syndrome; mandibulofacial and acrofacial dysostoses, including Treacher Collins and Nager syndromes; auriculocondylar syndrome; aglossia–adactylia/hypoglossia–hypodactylia spectrum; tetra-amelia syndromes; holoprosencephaly-associated facial malformations; and amniotic-band or teratogenic craniofacial disruption. The combination of complete mandibular absence and ventromedial/synotic ears strongly supports AOC.

## 11. Outcome and prognosis

Classic complete AOC is generally perinatally lethal because a functional airway cannot be established and severe CNS or multisystem anomalies may coexist. No meaningful five- or ten-year survival statistic exists. Rare longer-term survivors have less severe anatomy, so their outcomes cannot be generalized to complete agnathia.

Major complications are airway obstruction, respiratory failure, inability to feed or swallow, aspiration, hearing impairment, speech impairment, and morbidity from associated brain, cardiac, or other malformations. Prognosis is determined chiefly by residual mandibular/oropharyngeal anatomy, feasibility of airway access, CNS involvement, and associated organ defects. No molecular prognostic biomarker is validated.

## 12. Treatment

There is no approved pharmacotherapy, gene therapy, RNA therapy, cell therapy, or molecularly targeted treatment. No relevant interventional clinical trial was retrieved.

Management is multidisciplinary and goal-directed:

* Prenatal counseling and serial imaging;
* Delivery at a tertiary center if active neonatal intervention is chosen;
* Anticipated difficult-airway planning involving maternal–fetal medicine, neonatology, anesthesiology, otolaryngology, craniofacial surgery, and ethics/palliative care;
* EXIT-to-airway or immediate surgical-airway strategies may be considered in exceptional anatomically feasible cases, but evidence consists of individual reports rather than response-rate studies;
* Enteral feeding access, aspiration prevention, hearing assessment, and staged craniofacial reconstruction for survivors;
* Comfort-focused perinatal care when airway establishment is impossible or anomalies are incompatible with sustained life.

Suggested MAXO concepts are **prenatal ultrasonography, fetal MRI, genetic testing, genetic counseling, airway management, tracheostomy, assisted ventilation, gastrostomy/enteral feeding, craniofacial surgery, hearing evaluation, and palliative care**. Exact MAXO codes require current ontology lookup. Pharmacogenomics and combination-drug algorithms are not applicable.

## 13. Prevention

No vaccine, medication, lifestyle program, or environmental intervention is proven to prevent AOC.

* **Primary prevention:** preconception counseling, optimized maternal health and diabetes control, folate according to standard pregnancy guidance, and avoidance of unnecessary potentially teratogenic exposures; these are general measures, not AOC-specific proven prophylaxis.
* **Secondary prevention/early detection:** targeted first-trimester ultrasound after a prior affected pregnancy; diagnostic chorionic-villus sampling or amniocentesis when a familial pathogenic variant is known.
* **Reproductive options:** parental testing, preimplantation genetic testing for a known familial variant, donor gametes, or prenatal diagnosis.
* **Tertiary prevention:** planned delivery, airway strategy, feeding support, and surveillance of associated anomalies to reduce complications.

When no molecular diagnosis is found, recurrence cannot be assumed to be zero because of germline mosaicism or undetected inherited variants.

## 14. Other species and natural disease

No established, naturally recurring veterinary syndrome directly equivalent to human AOC was identified, and the condition is not infectious or zoonotic. Orthologous developmental genes are conserved across vertebrates, particularly mouse (**Mus musculus**, NCBI Taxonomy 10090) and zebrafish (**Danio rerio**, NCBI Taxonomy 7955). Comparative relevance lies in conserved mandibular/hyoid-arch patterning, not cross-species transmission.

## 15. Model organisms

### Mouse

Prrx1/Prrx2 compound-mutant mice reproduce severe lower-jaw dysmorphogenesis, altered dentition, loss of Meckel cartilage, and inappropriate osteogenic differentiation. These models directly test mesenchymal lineage allocation but do not necessarily reproduce the complete human combination of agnathia, synotia, airway anatomy, and OTX2-associated eye/forebrain disease. (fabik2021themandibularand pages 18-20)

Conditional perturbations of Isl1 and pathway components demonstrate that SHH, FGF, BMP, WNT, EDN1–DLX–HAND, and other networks can converge on agnathia or mandibular hypoplasia. (fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 24-25, fabik2021themandibularand pages 16-17)

### Zebrafish

Zebrafish prrx1a/prrx1b experiments place PRRX activity downstream of BMP and in interaction with endothelin-1 and Jagged–Notch control of facial-cartilage differentiation. The model is powerful for live imaging and genetic pathway dissection, but zebrafish jaw anatomy differs substantially from the human mandible and cannot model neonatal airway lethality directly. The relevant study was Barske *et al.*, *PLOS Genetics*, April 2016, DOI: https://doi.org/10.1371/journal.pgen.1005967. (barske2016competitionbetweenjaggednotch pages 30-31, fabik2021themandibularand pages 24-25)

### Evidence classification and current research status

* **Human clinical evidence:** individual fetuses, neonates, rare survivors, and small prenatal/pathology series.
* **Human genetic evidence:** strongest for OTX2 and PRRX1; emerging for SMAD3.
* **Model-organism evidence:** strong for conserved pharyngeal-arch regulatory biology, but incomplete recapitulation of the full syndrome.
* **In-vitro/omics evidence:** sparse and not clinically validated.
* **2023–2024 developments:** chiefly improved prenatal recognition and additional case reporting; no disease-specific trial, approved therapy, validated biomarker, single-cell atlas, or population-scale natural-history study was found.

## Evidence limitations and curation recommendations

The principal limitation is not merely rarity but **denominator-free ascertainment**: published severe fetuses overrepresent lethality, while rare survivors overrepresent milder anatomy. Accordingly, qualitative labels are preferable to fabricated percentages. Variant assertions should be independently checked in ClinVar, gnomAD, HGNC, and the primary report before knowledge-base release. Exact HPO, MONDO, UBERON, GO, CL, and MAXO identifiers should likewise be resolved against current ontology versions rather than inferred from labels.

A useful direct mechanistic statement from the mandibular-arch review is that the mandibular and hyoid arches form the facial skeleton and that most viscerocranial skeletal tissue differentiates from neural crest; the review further emphasizes conserved regulatory networks in mouse and zebrafish (Fabik *et al.*, July 2021; DOI: https://doi.org/10.3390/ijms22147529). The model evidence supports the present consensus that AOC is a developmental neurocristopathy/pharyngeal-arch patterning disorder, while the human reports show that several genetic lesions can produce that common anatomical endpoint. (fabik2021themandibularand pages 18-20, fabik2021themandibularand pages 14-16, fabik2021themandibularand pages 24-25, fabik2021themandibularand pages 16-17)

References

1. (barske2016competitionbetweenjaggednotch pages 30-31): Lindsey Barske, Amjad Askary, Elizabeth Zuniga, B. Balczerski, Paul Bump, J. Nichols, J. Gage Crump, and Mary C Mullins. Competition between jagged-notch and endothelin1 signaling selectively restricts cartilage formation in the zebrafish upper face. PLOS Genetics, 12:e1005967, Apr 2016. URL: https://doi.org/10.1371/journal.pgen.1005967, doi:10.1371/journal.pgen.1005967. This article has 85 citations and is from a domain leading peer-reviewed journal.

2. (fabik2021themandibularand pages 14-16): Jaroslav Fabik, Viktorie Psutkova, and Ondrej Machon. The mandibular and hyoid arches—from molecular patterning to shaping bone and cartilage. International Journal of Molecular Sciences, 22:7529, Jul 2021. URL: https://doi.org/10.3390/ijms22147529, doi:10.3390/ijms22147529. This article has 32 citations.

3. (fabik2021themandibularand pages 18-20): Jaroslav Fabik, Viktorie Psutkova, and Ondrej Machon. The mandibular and hyoid arches—from molecular patterning to shaping bone and cartilage. International Journal of Molecular Sciences, 22:7529, Jul 2021. URL: https://doi.org/10.3390/ijms22147529, doi:10.3390/ijms22147529. This article has 32 citations.

4. (fabik2021themandibularand pages 16-17): Jaroslav Fabik, Viktorie Psutkova, and Ondrej Machon. The mandibular and hyoid arches—from molecular patterning to shaping bone and cartilage. International Journal of Molecular Sciences, 22:7529, Jul 2021. URL: https://doi.org/10.3390/ijms22147529, doi:10.3390/ijms22147529. This article has 32 citations.

5. (fabik2021themandibularand pages 24-25): Jaroslav Fabik, Viktorie Psutkova, and Ondrej Machon. The mandibular and hyoid arches—from molecular patterning to shaping bone and cartilage. International Journal of Molecular Sciences, 22:7529, Jul 2021. URL: https://doi.org/10.3390/ijms22147529, doi:10.3390/ijms22147529. This article has 32 citations.

## Artifacts

- [Edison artifact artifact-00](Agnathia-Otocephaly_Complex-deep-research-falcon_artifacts/artifact-00.md)