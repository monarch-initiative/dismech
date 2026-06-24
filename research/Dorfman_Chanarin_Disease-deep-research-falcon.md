---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T17:18:13.416427'
end_time: '2026-06-13T17:29:46.236425'
duration_seconds: 692.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dorfman-Chanarin Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dorfman_Chanarin_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dorfman-Chanarin Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dorfman-Chanarin Disease** covering all of the
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
- **Disease Name:** Dorfman-Chanarin Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dorfman-Chanarin Disease** covering all of the
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


## Comprehensive Research Report: Dorfman–Chanarin Disease (Chanarin–Dorfman Syndrome; Neutral Lipid Storage Disease with Ichthyosis)

### Target disease
Dorfman–Chanarin disease (more commonly **Chanarin–Dorfman syndrome, CDS**) is a **multisystem autosomal-recessive neutral-lipid storage disorder** characterized by **congenital ichthyosis** plus **systemic triacylglycerol (TAG) accumulation in cytoplasmic lipid droplets** across multiple tissues. (redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7)

| Topic | Key facts | Ontology/identifier suggestions | Key citations |
|---|---|---|---|
| Disease definition | Rare autosomal recessive neutral lipid storage disorder with ichthyosis; characterized by intracellular triacylglycerol accumulation in multiple tissues and non-bullous congenital ichthyosiform erythroderma/ichthyosis. Common alternate names: Chanarin–Dorfman syndrome (CDS), Dorfman–Chanarin syndrome, neutral lipid storage disease with ichthyosis (NLSDI). (demerjian2006barrierdysfunctionand pages 1-2, redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7) | OMIM/MIM: **275630**; ICD-10: **E75.5**; MONDO: not found in retrieved evidence; MeSH: not found in retrieved evidence; Orphanet: placeholder only in retrieved evidence | Demerjian 2006 DOI:10.1038/sj.jid.5700332 URL:https://doi.org/10.1038/sj.jid.5700332; Redaelli 2010 DOI:10.1186/1750-1172-5-33 URL:https://doi.org/10.1186/1750-1172-5-33; Fischer 2023 DOI:10.1515/medgen-2023-2006 URL:https://doi.org/10.1515/medgen-2023-2006 (demerjian2006barrierdysfunctionand pages 1-2, redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7) |
| Causal gene and inheritance | Caused by biallelic **ABHD5** variants; ABHD5 encodes **CGI-58**, a co-activator of **ATGL/PNPLA2**. Loss of ABHD5 impairs triglyceride hydrolysis, causing lipid-droplet accumulation. Autosomal recessive inheritance is consistently reported. ABHD5 gene MIM **604780** noted in retrieved evidence. (elsayed2023anovelabhd5 pages 1-3, redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7, schratter2022abhd5—aregulatorof pages 2-4) | Gene: **ABHD5/CGI-58**; OMIM gene: **604780**; Disease OMIM: **275630** | Elsayed 2023 DOI:10.1016/j.gendis.2022.08.005 URL:https://doi.org/10.1016/j.gendis.2022.08.005; Redaelli 2010 DOI:10.1186/1750-1172-5-33 URL:https://doi.org/10.1186/1750-1172-5-33; Schratter 2022 DOI:10.3390/metabo12111015 URL:https://doi.org/10.3390/metabo12111015 (elsayed2023anovelabhd5 pages 1-3, redaelli2010clinicalandgenetic pages 1-2, schratter2022abhd5—aregulatorof pages 2-4) |
| Epidemiology and reported case counts | Extremely rare. Reported counts have increased over time in the literature surveyed: ~**55 cases** by 2010; **128 reported patients** with **85 molecularly confirmed** by 2021 in one review; **151 reported patients worldwide** by 2021; fewer than **120 cases** stated in one 2023 case report/review, reflecting source-to-source update differences. Largest single-country cohort in retrieved evidence: **40 Turkish cases**. (redaelli2010clinicalandgenetic pages 1-2, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, tavian2021recurrentn209*abhd5 pages 1-2, mangukiya2023chanarindorfmansyndrome(cds) pages 1-2) | Rare disease; prevalence not provided in retrieved evidence | Redaelli 2010 DOI:10.1186/1750-1172-5-33 URL:https://doi.org/10.1186/1750-1172-5-33; Waheed 2021 DOI:10.1186/s43042-021-00189-2 URL:https://doi.org/10.1186/s43042-021-00189-2; Tavian 2021 DOI:10.4081/ejtm.2021.9796 URL:https://doi.org/10.4081/ejtm.2021.9796; Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889 (redaelli2010clinicalandgenetic pages 1-2, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, tavian2021recurrentn209*abhd5 pages 1-2, mangukiya2023chanarindorfmansyndrome(cds) pages 1-2) |
| Core clinical phenotype | Skin involvement is the dominant and often universal feature: congenital ichthyosis/NCIE; some patients are born as collodion babies; pruritus may be intense. Multisystem features include hepatomegaly/steatosis, myopathy or muscle weakness, hearing loss, cataracts/other ocular findings, CNS involvement, and occasional cardiomyopathy. (fischer2023syndromicichthyoses pages 6-7, mangukiya2023chanarindorfmansyndrome(cds) pages 1-2, elsayed2023anovelabhd5 pages 1-3, elammari2024considerhypertriglyceridemiain pages 1-2) | Suggested phenotype labels: congenital ichthyosis; hepatomegaly; hepatic steatosis; myopathy; cataract; sensorineural hearing loss | Fischer 2023 DOI:10.1515/medgen-2023-2006 URL:https://doi.org/10.1515/medgen-2023-2006; Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889; Elsayed 2023 DOI:10.1016/j.gendis.2022.08.005 URL:https://doi.org/10.1016/j.gendis.2022.08.005; El-Ammari 2024 DOI:10.7241/ourd.20244.22 URL:https://doi.org/10.7241/ourd.20244.22 (fischer2023syndromicichthyoses pages 6-7, mangukiya2023chanarindorfmansyndrome(cds) pages 1-2, elsayed2023anovelabhd5 pages 1-3, elammari2024considerhypertriglyceridemiain pages 1-2) |
| Phenotype frequencies/statistics | Retrieved reviews/case summaries report: **hepatomegaly 60%**, **myopathy 59%**, **ectropion 29%**, **cataract 22%**, **deafness 17%**, **splenomegaly 13%**; liver involvement reported in **>80%** in one 2023 paper and about **85%** in a 2021 cohort review; neurological symptoms in **~30%**; muscle involvement **40%** in one series. In genotype-stratified data, severe/truncating ABHD5 variants were associated with **36% myopathy** and **67.5% CK elevation** vs **15%** and **30%** for missense variants. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, elsayed2023anovelabhd5 pages 1-3, tavian2021recurrentn209*abhd5 pages 4-6) | Frequency data from aggregated literature, not formal registry prevalence | Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889; Elsayed 2023 DOI:10.1016/j.gendis.2022.08.005 URL:https://doi.org/10.1016/j.gendis.2022.08.005; Tavian 2021 DOI:10.4081/ejtm.2021.9796 URL:https://doi.org/10.4081/ejtm.2021.9796 (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, elsayed2023anovelabhd5 pages 1-3, tavian2021recurrentn209*abhd5 pages 4-6) |
| Diagnostic hallmark | **Jordans’ anomaly**—lipid vacuoles in granulocytes/leukocytes on peripheral blood smear—is the classic, simple diagnostic hallmark; reported as demonstrable by May–Grünwald–Giemsa/peripheral smear and considered characteristic/pathognomonic in multiple sources. Tissue biopsies can show neutral lipid droplets in skin, liver, muscle, kidney tubular epithelium, and other cells. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7, agrebi2023dorfman–chanarinsyndromewith pages 1-2) | Suggested diagnostic label: Jordans’ anomaly; peripheral smear for lipid vacuoles | Waheed 2021 DOI:10.1186/s43042-021-00189-2 URL:https://doi.org/10.1186/s43042-021-00189-2; Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889; Fischer 2023 DOI:10.1515/medgen-2023-2006 URL:https://doi.org/10.1515/medgen-2023-2006; Agrebi 2023 DOI:10.4103/ijn.ijn_203_22 URL:https://doi.org/10.4103/ijn.ijn_203_22 (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7, agrebi2023dorfman–chanarinsyndromewith pages 1-2) |
| Laboratory, imaging, pathology | Serum lipids may be normal, but liver enzymes and CK/CPK are often elevated; muscle enzymes elevated in **>50%** in one 2024 report. Imaging/pathology may show fatty liver, hepatomegaly, fibrosis/cirrhosis; kidney biopsy can reveal mesangial proliferative glomerulonephritis with extensive tubular lipid vacuoles in rare renal involvement. Skin barrier studies showed abnormal basal TEWL and SC integrity with lipid micro-inclusions in lamellar bodies. (redaelli2010clinicalandgenetic pages 1-2, elammari2024considerhypertriglyceridemiain pages 1-2, agrebi2023dorfman–chanarinsyndromewith pages 1-2, demerjian2006barrierdysfunctionand pages 1-2) | Suggested workup: AST/ALT/GGT, CK/CPK, liver ultrasound/FibroScan, biopsy if indicated | Redaelli 2010 DOI:10.1186/1750-1172-5-33 URL:https://doi.org/10.1186/1750-1172-5-33; El-Ammari 2024 DOI:10.7241/ourd.20244.22 URL:https://doi.org/10.7241/ourd.20244.22; Agrebi 2023 DOI:10.4103/ijn.ijn_203_22 URL:https://doi.org/10.4103/ijn.ijn_203_22; Demerjian 2006 DOI:10.1038/sj.jid.5700332 URL:https://doi.org/10.1038/sj.jid.5700332 (redaelli2010clinicalandgenetic pages 1-2, elammari2024considerhypertriglyceridemiain pages 1-2, agrebi2023dorfman–chanarinsyndromewith pages 1-2, demerjian2006barrierdysfunctionand pages 1-2) |
| Variant spectrum | Retrieved evidence notes substantial allelic heterogeneity. Counts vary by publication date: **45 different ABHD5 mutations** reported in one 2023 paper; **at least 78 mutations** in a 2023 review/case report; many mutation classes reported, including nonsense, missense, frameshift, splice-site, large deletions, and promoter/complex rearrangements. **77%** of variants were truncating in one 2023 source. Recurrent **N209\*** is especially common, accounting for **52% (21/40)** of Turkish cases and **16% (24/151)** of all reported cases in one 2021 review. (elsayed2023anovelabhd5 pages 1-3, mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, tavian2021recurrentn209*abhd5 pages 1-2, redaelli2010clinicalandgenetic pages 1-2) | Variant classes: truncating, missense, frameshift, splice-site, large deletion | Elsayed 2023 DOI:10.1016/j.gendis.2022.08.005 URL:https://doi.org/10.1016/j.gendis.2022.08.005; Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889; Tavian 2021 DOI:10.4081/ejtm.2021.9796 URL:https://doi.org/10.4081/ejtm.2021.9796; Redaelli 2010 DOI:10.1186/1750-1172-5-33 URL:https://doi.org/10.1186/1750-1172-5-33 (elsayed2023anovelabhd5 pages 1-3, mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, tavian2021recurrentn209*abhd5 pages 1-2, redaelli2010clinicalandgenetic pages 1-2) |
| Mechanism / pathophysiology | ABHD5/CGI-58 normally activates ATGL-mediated lipolysis and also interfaces with epidermal lipid metabolism; deficiency causes TAG accumulation in cytoplasmic lipid droplets across tissues and contributes to skin-barrier dysfunction. J Invest Dermatol data linked epidermal disease to lamellar-body lipid micro-inclusions, non-lamellar extracellular lipid phases, abnormal barrier function, and increased transepidermal water loss. (demerjian2006barrierdysfunctionand pages 1-2, fischer2023syndromicichthyoses pages 6-7, schratter2022abhd5—aregulatorof pages 2-4) | Mechanistic axis: ABHD5/CGI-58 → ATGL/PNPLA2 activation → triglyceride hydrolysis | Demerjian 2006 DOI:10.1038/sj.jid.5700332 URL:https://doi.org/10.1038/sj.jid.5700332; Fischer 2023 DOI:10.1515/medgen-2023-2006 URL:https://doi.org/10.1515/medgen-2023-2006; Schratter 2022 DOI:10.3390/metabo12111015 URL:https://doi.org/10.3390/metabo12111015 (demerjian2006barrierdysfunctionand pages 1-2, fischer2023syndromicichthyoses pages 6-7, schratter2022abhd5—aregulatorof pages 2-4) |
| Notable atypical/less common manifestations | Rare or less common manifestations in retrieved evidence include renal involvement/nephrotic syndrome, thyroid dysfunction in adults from a founder-mutation series, possible cardiomyopathy, cerebellar/white-matter abnormalities, developmental delay, and severe CNS malformations in isolated case reports. (agrebi2023dorfman–chanarinsyndromewith pages 1-2, elsayed2023anovelabhd5 pages 3-4) | Multisystem disease; no separate identifier in retrieved evidence | Agrebi 2023 DOI:10.4103/ijn.ijn_203_22 URL:https://doi.org/10.4103/ijn.ijn_203_22; Elsayed 2023 DOI:10.1016/j.gendis.2022.08.005 URL:https://doi.org/10.1016/j.gendis.2022.08.005 (agrebi2023dorfman–chanarinsyndromewith pages 1-2, elsayed2023anovelabhd5 pages 3-4) |
| Current management | No disease-specific approved therapy was identified in retrieved evidence. Management is supportive/multidisciplinary: low-fat or low-long-chain-fat diet, **medium-chain triglyceride (MCT) oil** supplementation, vitamin E, ursodeoxycholic acid, topical emollients, and selective use of **acitretin** for ichthyosis with monitoring. One case summary reported normalization of enzymes/loss of inclusions and **50% liver-size reduction after 1 year** on dietary/supportive therapy. Expert reviews emphasize early diagnosis for management of metabolic/cardiac complications and genetic counseling. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, elammari2024considerhypertriglyceridemiain pages 1-2, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, tavian2021recurrentn209*abhd5 pages 4-6, fischer2023syndromicichthyoses pages 6-7) | Supportive care; dietary therapy; dermatologic treatment | Mangukiya 2023 DOI:10.7759/cureus.43889 URL:https://doi.org/10.7759/cureus.43889; El-Ammari 2024 DOI:10.7241/ourd.20244.22 URL:https://doi.org/10.7241/ourd.20244.22; Waheed 2021 DOI:10.1186/s43042-021-00189-2 URL:https://doi.org/10.1186/s43042-021-00189-2; Tavian 2021 DOI:10.4081/ejtm.2021.9796 URL:https://doi.org/10.4081/ejtm.2021.9796; Fischer 2023 DOI:10.1515/medgen-2023-2006 URL:https://doi.org/10.1515/medgen-2023-2006 (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, elammari2024considerhypertriglyceridemiain pages 1-2, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2, tavian2021recurrentn209*abhd5 pages 4-6, fischer2023syndromicichthyoses pages 6-7) |
| Real-world implementations / research infrastructure | An international observational registry for **NLSD/TGCV and related diseases** is recruiting (**NCT02918032**, target enrollment ~**120**), capturing NLSDI/CDS and NLSDM with longitudinal outcomes including survival, CK, liver tests, thyroid tests, imaging, function, and biopsy data. Interventional studies retrieved are focused mainly on **NLSDM/PNPLA2** rather than ABHD5-NLSDI: **bezafibrate** Phase 4 (**NCT01527318**) and **CNT-02 medium-chain fatty acid capsules** (**NCT02830763**, terminated). (NCT02918032 chunk 1, NCT02830763 chunk 1, NCT01527318 chunk 1, NCT02918032 chunk 2, NCT02830763 chunk 2) | ClinicalTrials.gov: **NCT02918032**, **NCT01527318**, **NCT02830763** | ClinicalTrials.gov NCT02918032 URL:https://clinicaltrials.gov/study/NCT02918032; NCT01527318 URL:https://clinicaltrials.gov/study/NCT01527318; NCT02830763 URL:https://clinicaltrials.gov/study/NCT02830763 (NCT02918032 chunk 1, NCT02830763 chunk 1, NCT01527318 chunk 1, NCT02918032 chunk 2, NCT02830763 chunk 2) |


*Table: This table compiles the core identifiers, genetics, phenotypes, diagnostics, pathophysiology, management, and registry/trial landscape for Dorfman–Chanarin disease/Chanarin–Dorfman syndrome (NLSDI) using only the retrieved evidence. It is designed as a compact reference for building a disease knowledge base entry.*

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
CDS/NLSDI is an inborn error of neutral lipid metabolism in which defective intracellular lipolysis leads to TAG accumulation in leukocytes and parenchymal tissues, producing a hallmark blood-smear finding (Jordan’s anomaly) and a clinical spectrum dominated by congenital ichthyosis and frequent hepatic involvement. (redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7)

### 1.2 Key identifiers
* **OMIM/MIM (disease): 275630** (elsayed2023anovelabhd5 pages 1-3, demerjian2006barrierdysfunctionand pages 1-2, redaelli2010clinicalandgenetic pages 1-2)
* **OMIM/MIM (gene ABHD5): 604780** (redaelli2010clinicalandgenetic pages 1-2)
* **ICD-10:** **E75.5** (as indexed in one retrieved clinical summary source) (koc2025chanarindorfmansyndrome pages 1-4)
* **MONDO / Orphanet ORPHA / MeSH / ICD-11:** Not present in the retrieved evidence corpus; therefore not asserted here.

### 1.3 Synonyms and alternative names
* Chanarin–Dorfman syndrome (CDS) (redaelli2010clinicalandgenetic pages 1-2)
* Dorfman–Chanarin syndrome (agrebi2023dorfman–chanarinsyndromewith pages 1-2)
* Neutral lipid storage disease with ichthyosis (NLSDI) (demerjian2006barrierdysfunctionand pages 1-2, tavian2021recurrentn209*abhd5 pages 1-2)
* Neutral lipid storage disease (NLSD; broader umbrella that also includes NLSDM) (redaelli2010clinicalandgenetic pages 1-2, schratter2022abhd5—aregulatorof pages 2-4)

### 1.4 Evidence source type
The retrieved evidence is dominated by **aggregated disease-level reviews**, **case reports/series** (pediatric and adult), and **mechanistic studies** (human tissue/cell studies and mouse models). (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, agrebi2023dorfman–chanarinsyndromewith pages 1-2, demerjian2006barrierdysfunctionand pages 1-2, schratter2022abhd5—aregulatorof pages 2-4)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic):** biallelic pathogenic variants in **ABHD5** (also known as **CGI-58**) cause CDS/NLSDI. (redaelli2010clinicalandgenetic pages 1-2, schratter2022abhd5—aregulatorof pages 2-4)

**Core biochemical defect:** ABHD5 is required for efficient intracellular TAG breakdown by co-activating patatin-like phospholipases, particularly **ATGL/PNPLA2**. Mechanistically, Schratter et al. summarize that ABHD5 “**specifically interacts with ATGL and stimulates its TAG hydrolase activity many-fold in vitro**” and that “**During lipolysis, ATGL requires the presence of ABHD5 to efficiently hydrolyze TAG.**” (schratter2022abhd5—aregulatorof pages 4-5)

**Skin-specific causal axis:** ABHD5 also acts as a co-activator of **PNPLA1** in epidermal acylceramide (acylCer) formation; mutant ABHD5 linked to NLSDI fails to accelerate PNPLA1-mediated acylCer biosynthesis, contributing to barrier failure and ichthyosis. (schratter2022abhd5—aregulatorof pages 13-15, schratter2022abhd5—aregulatorof pages 12-13)

### 2.2 Risk factors
* **Consanguinity** is repeatedly present in case series (consistent with autosomal recessive inheritance). (elsayed2023anovelabhd5 pages 1-3, redaelli2010clinicalandgenetic pages 2-3)
* **Geographic clustering**: multiple sources note that many families/cases originate from Mediterranean and Middle Eastern populations. (mangukiya2023chanarindorfmansyndrome(cds) pages 1-2, redaelli2010clinicalandgenetic pages 1-2)

No environmental, infectious, or lifestyle risk factors were identified in the retrieved evidence.

### 2.3 Protective factors / gene–environment interactions
No protective genetic variants or gene–environment interaction evidence was identified in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Core phenotypes (with frequencies where available)
Aggregated literature summaries in the retrieved 2023 Cureus report list the following approximate frequencies among reported individuals:
* **Hepatomegaly: ~60%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* **Myopathy: ~59%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* **Ectropion: ~29%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* **Cataract: ~22%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* **Deafness: ~17%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* **Splenomegaly: ~13%** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)

A separate 2023 case-series paper reports broad system involvement frequencies as: **liver involvement “more than 80%,” muscle involvement “40%,” and neurological symptoms “almost 30%.”** (elsayed2023anovelabhd5 pages 1-3)

A 2021 cohort review further supports genotype-associated expressivity: severe/truncating ABHD5 variants were associated with higher rates of **myopathy (36%)** and **CK elevation (67.5%)** compared with missense variants (**15%** and **30%**, respectively). (tavian2021recurrentn209*abhd5 pages 4-6)

### 3.2 Phenotype characteristics
* **Onset:** skin findings are typically **congenital**; patients may be born as **collodion babies** and develop congenital ichthyosiform erythroderma/ichthyosis. (redaelli2010clinicalandgenetic pages 1-2, fischer2023syndromicichthyoses pages 6-7)
* **Progression:** hepatic disease may be progressive, with steatosis potentially advancing to fibrosis/cirrhosis and liver failure in some individuals. (fischer2023syndromicichthyoses pages 6-7, mangukiya2023chanarindorfmansyndrome(cds) pages 2-5)
* **Severity/variability:** multiple sources emphasize variable expressivity and limited genotype–phenotype predictability (e.g., “the severity of liver symptoms is highly variable”). (elsayed2023anovelabhd5 pages 1-3)

### 3.3 Notable less-common/expanded phenotypes (recent clinical literature)
* **Renal involvement** is uncommon but has been reported; a 2023 adult case report described nephrotic syndrome with kidney biopsy showing extensive lipid vacuoles in tubular epithelial cells. (agrebi2023dorfman–chanarinsyndromewith pages 1-2)
* **Hypertriglyceridemia** can be prominent in some patients presenting with congenital ichthyosis, and authors recommend considering CDS in this presentation. (elammari2024considerhypertriglyceridemiain pages 1-2)
* **Central nervous system involvement** can include developmental delay and structural abnormalities in severe pediatric cases. (elsayed2023anovelabhd5 pages 3-4)

### 3.4 Suggested HPO terms (non-exhaustive; based on phenotypes described in retrieved sources)
* Ichthyosis / congenital ichthyosiform erythroderma: **HP:0008064** (ichthyosis) (fischer2023syndromicichthyoses pages 6-7)
* Hepatomegaly: **HP:0002240** (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* Hepatic steatosis: **HP:0001397** (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, fischer2023syndromicichthyoses pages 6-7)
* Elevated transaminases: **HP:0002910** (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, redaelli2010clinicalandgenetic pages 1-2)
* Myopathy / muscle weakness: **HP:0003198** (myopathy), **HP:0001324** (muscle weakness) (fischer2023syndromicichthyoses pages 6-7, tavian2021recurrentn209*abhd5 pages 4-6)
* Cataract: **HP:0000518** (agrebi2023dorfman–chanarinsyndromewith pages 1-2, mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* Ectropion: **HP:0000656** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)
* Sensorineural hearing impairment: **HP:0000407** (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, fischer2023syndromicichthyoses pages 6-7)

(These are ontology suggestions; the cited sources describe the clinical features but do not supply HPO mappings.)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
* **ABHD5 (CGI-58)** is the disease gene for CDS/NLSDI. (redaelli2010clinicalandgenetic pages 1-2, schratter2022abhd5—aregulatorof pages 2-4)

### 4.2 Pathogenic variant spectrum (type/class)
Across studies, ABHD5 pathogenic variants include **nonsense, frameshift, splice-site, missense**, and **large genomic deletions**. (redaelli2010clinicalandgenetic pages 1-2, redaelli2010clinicalandgenetic pages 2-3, tavian2021recurrentn209*abhd5 pages 1-2)

**Truncating predominance:** One 2023 report states that **~77%** of ABHD5 variants reported in CDS were truncating. (elsayed2023anovelabhd5 pages 1-3)

**Recurrent variant:** The truncating **N209\*** variant is repeatedly highlighted as common; a 2021 review reports N209\* in **52% (21/40)** of Turkish cases and **16% (24/151)** of reported CDS cases. (tavian2021recurrentn209*abhd5 pages 1-2)

**Large deletions / genetic heterogeneity:** Redaelli et al. (2010) reported the first large deletions in ABHD5 and also described a clinically diagnosed patient without detectable ABHD5 mutations, suggesting possible genetic heterogeneity. (redaelli2010clinicalandgenetic pages 1-2, redaelli2010clinicalandgenetic pages 2-3)

### 4.3 Functional consequences
The dominant disease mechanism is **loss of ABHD5 co-activation of intracellular lipases**, causing impaired TAG hydrolysis and lipid droplet accumulation. (schratter2022abhd5—aregulatorof pages 4-5, elsayed2023anovelabhd5 pages 1-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes or epigenetic mechanisms were identified in the retrieved evidence.

---

## 5. Environmental information
No consistent non-genetic environmental contributors (toxins, exposures, infectious triggers) were identified in the retrieved evidence corpus.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (gene → molecular defect → cellular phenotype → clinical manifestations)
1. **Biallelic ABHD5 loss-of-function** (genetic trigger) (redaelli2010clinicalandgenetic pages 1-2)
2. **Reduced activation of ATGL/PNPLA2** and impaired intracellular TAG hydrolysis (molecular defect) (schratter2022abhd5—aregulatorof pages 4-5)
3. **Accumulation of cytoplasmic lipid droplets** (cellular phenotype), including **Jordan’s anomaly** in leukocytes and TAG accumulation in liver/muscle/skin (demerjian2006barrierdysfunctionand pages 1-2, fischer2023syndromicichthyoses pages 6-7)
4. **Tissue dysfunction:**
   * **Liver:** steatosis ± progression to fibrosis/cirrhosis (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, fischer2023syndromicichthyoses pages 6-7)
   * **Muscle/heart:** variable myopathy; in model systems, muscle-specific loss causes cardiac myopathy and impaired mitochondrial FA oxidation (schratter2022abhd5—aregulatorof pages 10-12)
   * **Skin:** defective barrier formation and congenital ichthyosis via disruption of epidermal lipid processing, including PNPLA1-dependent acylceramide synthesis (schratter2022abhd5—aregulatorof pages 12-13, schratter2022abhd5—aregulatorof pages 13-15)

### 6.2 Skin barrier mechanism (primary human pathophysiology evidence)
Demerjian et al. (2006) studied NLSDI patients and describe the disease as characterized by neutral lipid droplet accumulation (oil red O–positive TAG droplets) and pruritic ichthyosiform erythroderma, linking the disorder to epidermal lipid-processing defects and barrier dysfunction. (demerjian2006barrierdysfunctionand pages 1-2)

### 6.3 Key pathways and interacting proteins (ABHD5 biology)
ABHD5 is positioned as a ligand-regulated lipase co-activator that coordinates lipid-droplet protein interactions and lipid flux:
* Interacts with **perilipins (PLIN1/3/5)** and can be modulated by ligands that alter PLIN binding, influencing lipolysis. (schratter2022abhd5—aregulatorof pages 9-10)
* Interacts with **FABP4** (adipocyte FABP), which supports ATGL activity in an ABHD5-dependent fashion. (schratter2022abhd5—aregulatorof pages 9-10)
* Co-activates **PNPLA1** to promote ω-O-acylceramide synthesis, essential for the epidermal barrier. (schratter2022abhd5—aregulatorof pages 13-15, schratter2022abhd5—aregulatorof pages 12-13)

### 6.4 Suggested GO biological process terms (mechanism-oriented; based on described functions)
* **Neutral lipid catabolic process** (TAG hydrolysis/lipolysis) (schratter2022abhd5—aregulatorof pages 4-5)
* **Lipid droplet organization / lipid storage** (demerjian2006barrierdysfunctionand pages 1-2)
* **Skin barrier establishment** / **ceramide metabolic process** (acylCer axis) (schratter2022abhd5—aregulatorof pages 12-13)

### 6.5 Suggested CL (Cell Ontology) terms (primary implicated cell types)
* **Neutrophil** (Jordan’s anomaly in granulocytes) (fischer2023syndromicichthyoses pages 6-7)
* **Keratinocyte** (epidermal barrier defect) (schratter2022abhd5—aregulatorof pages 12-13)
* **Hepatocyte** (hepatic steatosis) (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5)
* **Myocyte** / **cardiomyocyte** (myopathy/cardiomyopathy) (fischer2023syndromicichthyoses pages 6-7, schratter2022abhd5—aregulatorof pages 10-12)

---

## 7. Anatomical structures affected

### 7.1 Organ-level involvement (consistent across sources)
* **Skin** (primary): congenital ichthyosis/NCIE; pruritus in some cases. (fischer2023syndromicichthyoses pages 6-7)
* **Liver** (frequent): hepatomegaly, steatosis, fibrosis/cirrhosis. (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, fischer2023syndromicichthyoses pages 6-7)
* **Skeletal muscle** (variable): myopathy, CK elevation. (tavian2021recurrentn209*abhd5 pages 4-6, fischer2023syndromicichthyoses pages 6-7)
* **Eye** (variable): cataract, ectropion. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, agrebi2023dorfman–chanarinsyndromewith pages 1-2)
* **Ear** (variable): sensorineural hearing impairment. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, fischer2023syndromicichthyoses pages 6-7)
* **Kidney** (rare): lipid vacuoles in tubular epithelial cells in an adult nephrotic presentation. (agrebi2023dorfman–chanarinsyndromewith pages 1-2)

### 7.2 Suggested UBERON terms (examples)
* Skin: **UBERON:0002097**
* Liver: **UBERON:0002107**
* Skeletal muscle: **UBERON:0001134**
* Kidney: **UBERON:0002113**

(These are ontology suggestions; UBERON IDs are not provided in the cited papers.)

---

## 8. Temporal development

* **Onset:** Typically **at birth** (congenital ichthyosis; sometimes collodion baby). (fischer2023syndromicichthyoses pages 6-7)
* **Course:** Multisystem involvement can be progressive, particularly hepatic disease (steatosis → fibrosis/cirrhosis), though severity varies. (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, elsayed2023anovelabhd5 pages 1-3)

---

## 9. Inheritance and population

### 9.1 Inheritance
**Autosomal recessive** inheritance is consistently reported. (mangukiya2023chanarindorfmansyndrome(cds) pages 1-2, redaelli2010clinicalandgenetic pages 1-2)

### 9.2 Epidemiology (case counts and geographic patterns)
Prevalence/incidence estimates were not found in the retrieved evidence; however, multiple sources provide case-count–based rarity estimates:
* ~**55 cases** reported by 2010. (redaelli2010clinicalandgenetic pages 1-2)
* **128** reported patients (with **85** molecularly confirmed) cited in a 2021 cohort study. (waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2)
* **151** reported patients worldwide cited in a 2021 review; largest single-country cohort noted as **40 cases in Turkey**. (tavian2021recurrentn209*abhd5 pages 1-2)
* A 2023 clinical review notes **<120 cases reported** and concentration in Mediterranean/Middle East populations (reflecting timing/source differences). (mangukiya2023chanarindorfmansyndrome(cds) pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical and laboratory diagnostics
**Hallmark test (high-yield, low-cost):** peripheral blood smear demonstrating lipid vacuoles in granulocytes/leukocytes (Jordan’s anomaly). A 2023 review emphasizes “a simple peripheral blood smear showing lipid droplets in granulocytes (Jordan anomaly).” (fischer2023syndromicichthyoses pages 6-7)

**Supportive laboratory findings:** elevated liver enzymes and/or CK/CPK can be present; muscle enzymes are reported as elevated in **>50%** of cases in one 2024 report. (elammari2024considerhypertriglyceridemiain pages 1-2)

**Histopathology:** may demonstrate neutral lipid accumulation in tissue biopsies. Examples include liver biopsy showing marked macrovesicular steatosis and fibrosis (with early cirrhosis considered) in a 2023 pediatric case, and kidney biopsy showing tubular lipid vacuoles in a rare renal presentation. (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, agrebi2023dorfman–chanarinsyndromewith pages 1-2)

### 10.2 Genetic testing
Diagnosis is confirmed by **ABHD5 sequencing** in reported cases/series. (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5, waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2)

**Variant detection considerations:** because large deletions can occur, molecular workups may need deletion/duplication analysis in addition to exon sequencing. (redaelli2010clinicalandgenetic pages 1-2)

### 10.3 Differential diagnosis
* **NLSD with myopathy (NLSDM)** due to **PNPLA2/ATGL** mutations: typically prominent myopathy/cardiac involvement but **no ichthyosis** (helps distinguish from CDS/NLSDI). (fischer2023syndromicichthyoses pages 6-7, schratter2022abhd5—aregulatorof pages 2-4)
* Other congenital ichthyoses/syndromic cornification disorders; expert reviews stress systematic assessment for extracutaneous organ involvement in ichthyosis patients. (fischer2023syndromicichthyoses pages 6-7)

---

## 11. Outcome / prognosis

Outcome is **variable**. Severe pediatric phenotypes can be complicated by recurrent infections and early death (e.g., pneumonia complications in one reported child). (elsayed2023anovelabhd5 pages 3-4)

Hepatic disease can progress to fibrosis/cirrhosis and potentially liver failure, and rare adult cases may demonstrate renal complications. (fischer2023syndromicichthyoses pages 6-7, agrebi2023dorfman–chanarinsyndromewith pages 1-2)

No quantitative survival curves or life expectancy estimates were found in the retrieved evidence.

---

## 12. Treatment

### 12.1 Current standard-of-care (supportive management)
No disease-specific approved therapy was identified in the retrieved evidence; management is symptomatic and preventive for organ complications:
* **Dietary fat modification** with restriction of long-chain fats and use of **medium-chain triglycerides (MCT)** is frequently described. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6, tavian2021recurrentn209*abhd5 pages 4-6)
* **Vitamin E** and **ursodeoxycholic acid (UDCA)** are reported as part of supportive regimens with “promising results” in a pediatric cohort. (waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2)
* **Emollients** for skin care are standard. (elammari2024considerhypertriglyceridemiain pages 1-2)
* **Acitretin** may improve ichthyosis in some cases but requires liver/lipid monitoring. (elammari2024considerhypertriglyceridemiain pages 1-2, tavian2021recurrentn209*abhd5 pages 4-6)

A 2023 case summary reports a response to dietary/supportive therapy including “**50% reduction** in liver size after one year” with normalization of enzymes and loss of leukocyte inclusions in a referenced patient experience. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6)

### 12.2 Experimental / emerging approaches and trials
**Clinical trials and registries:**
* **NCT02918032 (ClinicalTrials.gov; registered 2014; recruiting; observational registry)**: an international registry designed to characterize natural history, prognostic factors, and treatment effectiveness signals in NLSD/TGCV, explicitly including Chanarin–Dorfman syndrome and tracking multisystem outcomes (e.g., CK, liver enzymes, thyroid tests, imaging, function). (NCT02918032 chunk 1, NCT02918032 chunk 2)
* Interventional trials in the retrieved corpus are primarily directed to **NLSDM (PNPLA2/ATGL)** rather than ABHD5-NLSDI: **bezafibrate** (NCT01527318; registered 2011) and medium-chain fatty acid capsules **CNT-02** (NCT02830763; registered 2016; terminated). (NCT01527318 chunk 1, NCT02830763 chunk 1)

**Mechanism-driven therapeutic ideas:** Schratter et al. describe **synthetic ABHD5 ligands** that can disrupt ABHD5–PLIN interactions and promote lipolysis, though this is mechanistic and not a validated CDS therapy. (schratter2022abhd5—aregulatorof pages 9-10)

### 12.3 Suggested MAXO terms (examples)
* Dietary modification therapy (low-fat/MCT diet)
* Vitamin supplementation therapy (e.g., vitamin E)
* Bile acid therapy (ursodeoxycholic acid)
* Retinoid therapy (acitretin)

(MAXO IDs not present in retrieved evidence; suggestions only.)

---

## 13. Prevention
Primary prevention focuses on **genetic counseling** because CDS is autosomal recessive.

Expert reviews on syndromic ichthyoses emphasize that early diagnosis enables informed reproductive options including **prenatal and preimplantation genetic diagnosis** for families once the causal variant is known. (fischer2023syndromicichthyoses pages 6-7)

No newborn screening strategies were identified in the retrieved evidence.

---

## 14. Other species / natural disease
No naturally occurring CDS-equivalent disease in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms and experimental systems

### 15.1 Mouse models (ABHD5 deficiency)
A mechanistic review summarizes multiple informative Abhd5 mouse models:
* **Whole-body Abhd5 knockout**: systemic TAG accumulation with ichthyosiform skin phenotype and premature death. (schratter2022abhd5—aregulatorof pages 9-10)
* **Global/epidermis-specific Abhd5 loss**: lethal permeability-barrier defect with death from dehydration and loss of epidermal acylCers. (schratter2022abhd5—aregulatorof pages 12-13)
* **Liver-specific Abhd5 knockout**: pronounced hepatosteatosis progressing to NASH/fibrosis. (schratter2022abhd5—aregulatorof pages 13-15)
* **Muscle-specific Abhd5 loss**: cardiac myopathy and impaired mitochondrial FA oxidation. (schratter2022abhd5—aregulatorof pages 10-12)
* **Intestine-specific Abhd5 deficiency**: massive enterocyte TAG accumulation and altered chylomicron secretion. (schratter2022abhd5—aregulatorof pages 10-12)

### 15.2 Human cell systems
NLSDI patient fibroblasts exhibit severe TAG accumulation that can be functionally rescued; Schratter et al. report that “**the expression of functional ABHD5 in dermal NLSDI fibroblasts restored the TAG hydrolase activity and reversed the lipid storage phenotype in patient cells.**” (schratter2022abhd5—aregulatorof pages 5-7)

---

## Recent developments and 2023–2024 highlights (prioritized)

1. **2023 clinical genetics expansion:** New ABHD5 variants and heterogeneous phenotypes continue to be reported, reinforcing variable expressivity and multisystem involvement; one 2023 paper provides contemporary estimates of organ involvement frequencies (liver >80%, muscle ~40%, neurologic ~30%) and notes truncating variants as predominant. (elsayed2023anovelabhd5 pages 1-3)
2. **2023 syndromic ichthyosis expert framing:** A 2023 review situates CDS within syndromic ichthyoses/Mendelian cornification disorders and emphasizes systematic evaluation for organ involvement and use of simple smear-based screening (Jordan anomaly) followed by genetic confirmation. (fischer2023syndromicichthyoses pages 6-7)
3. **2024 diagnostic-awareness update:** A 2024 dermatology report emphasizes considering CDS in congenital ichthyosis with marked hypertriglyceridemia and highlights that Jordan bodies may occasionally be absent, underscoring the role of genetic confirmation. (elammari2024considerhypertriglyceridemiain pages 1-2)
4. **2024–present real-world implementation infrastructure:** Ongoing international observational registry activity (NCT02918032) provides a practical mechanism to collect longitudinal outcomes and evaluate management strategies across NLSD subtypes including CDS/NLSDI. (NCT02918032 chunk 1)

---

## Limitations of this report (evidence gaps)
* **MONDO, Orphanet, MeSH, and ICD-11 identifiers** were not present in the retrieved evidence corpus and are therefore not asserted.
* **Population allele frequencies (gnomAD/ExAC/TOPMed)** and **ClinVar/ACMG classifications** for specific variants were not retrievable with the available tools/evidence in this run.
* Robust **prevalence/incidence** estimates and **survival statistics** were not identified; the evidence primarily reports case counts and descriptive natural history.


References

1. (redaelli2010clinicalandgenetic pages 1-2): Chiara Redaelli, Rosalind A Coleman, Laura Moro, Catherine Dacou-Voutetakis, Solaf Mohamed Elsayed, Daniele Prati, Agostino Colli, Donatella Mela, Roberto Colombo, and Daniela Tavian. Clinical and genetic characterization of chanarin-dorfman syndrome patients: first report of large deletions in the abhd5 gene. Orphanet Journal of Rare Diseases, 5:33-33, Dec 2010. URL: https://doi.org/10.1186/1750-1172-5-33, doi:10.1186/1750-1172-5-33. This article has 66 citations and is from a peer-reviewed journal.

2. (fischer2023syndromicichthyoses pages 6-7): Judith Fischer, Alrun Hotz, and Katalin Komlosi. Syndromic ichthyoses. Medizinische Genetik, 35:23-32, Apr 2023. URL: https://doi.org/10.1515/medgen-2023-2006, doi:10.1515/medgen-2023-2006. This article has 7 citations.

3. (demerjian2006barrierdysfunctionand pages 1-2): Marianne Demerjian, Debra A. Crumrine, Leonard M. Milstone, Mary L. Williams, and Peter M. Elias. Barrier dysfunction and pathogenesis of neutral lipid storage disease with ichthyosis (chanarin-dorfman syndrome). The Journal of investigative dermatology, 126 9:2032-8, Sep 2006. URL: https://doi.org/10.1038/sj.jid.5700332, doi:10.1038/sj.jid.5700332. This article has 71 citations.

4. (elsayed2023anovelabhd5 pages 1-3): Solaf Mohamed Elsayed, Enza Torre, Daniela Tavian, Laura Moro, Corrado Angelini, Tawhida Y. Abdel Ghaffar, Khalid Zalata, Enas Ezzeldein Fahmy, and Sara Missaglia. A novel abhd5 mutation in two chanarin dorfman siblings with severe and heterogeneous clinical phenotype. May 2023. URL: https://doi.org/10.1016/j.gendis.2022.08.005, doi:10.1016/j.gendis.2022.08.005. This article has 2 citations.

5. (schratter2022abhd5—aregulatorof pages 2-4): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

6. (waheed2021chanarin–dorfmansyndromeclinicalgenetic pages 1-2): Nadia Waheed, Sadaqat Ijaz, and Zafar Fayyaz. Chanarin–dorfman syndrome: clinical/genetic features and natural history in six pakistani patients. Egyptian Journal of Medical Human Genetics, Aug 2021. URL: https://doi.org/10.1186/s43042-021-00189-2, doi:10.1186/s43042-021-00189-2. This article has 0 citations and is from a peer-reviewed journal.

7. (tavian2021recurrentn209*abhd5 pages 1-2): Daniela Tavian, Murat Durdu, Corrado Angelini, Enza Torre, and Sara Missaglia. Recurrent n209* abhd5 mutation in two unreported families with chanarin dorfman syndrome. European Journal of Translational Myology, May 2021. URL: https://doi.org/10.4081/ejtm.2021.9796, doi:10.4081/ejtm.2021.9796. This article has 5 citations and is from a peer-reviewed journal.

8. (mangukiya2023chanarindorfmansyndrome(cds) pages 1-2): Nisarg P Mangukiya, Safa Kaleem, D Ragasri Meghana, Lyluma Ishfaq, Gunjan Kochhar, Bejoi Mathew, Shivani Pulekar, Aashka C Lainingwala, Mihirkumar P Parmar, and Vishal Venugopal. Chanarin-dorfman syndrome (cds): a rare lipid metabolism disorder. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.43889, doi:10.7759/cureus.43889. This article has 3 citations.

9. (elammari2024considerhypertriglyceridemiain pages 1-2): Sara El-Ammari, Hanane Baybay, Imane Kacimi Alaoui, Sara Elloudi, Meryem Soughi, Zakia Douhi, and Fatima Zahra Mernissi. Consider hypertriglyceridemia in congenital ichthyosis. Our Dermatology Online, Oct 2024. URL: https://doi.org/10.7241/ourd.20244.22, doi:10.7241/ourd.20244.22. This article has 0 citations.

10. (mangukiya2023chanarindorfmansyndrome(cds) pages 5-6): Nisarg P Mangukiya, Safa Kaleem, D Ragasri Meghana, Lyluma Ishfaq, Gunjan Kochhar, Bejoi Mathew, Shivani Pulekar, Aashka C Lainingwala, Mihirkumar P Parmar, and Vishal Venugopal. Chanarin-dorfman syndrome (cds): a rare lipid metabolism disorder. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.43889, doi:10.7759/cureus.43889. This article has 3 citations.

11. (tavian2021recurrentn209*abhd5 pages 4-6): Daniela Tavian, Murat Durdu, Corrado Angelini, Enza Torre, and Sara Missaglia. Recurrent n209* abhd5 mutation in two unreported families with chanarin dorfman syndrome. European Journal of Translational Myology, May 2021. URL: https://doi.org/10.4081/ejtm.2021.9796, doi:10.4081/ejtm.2021.9796. This article has 5 citations and is from a peer-reviewed journal.

12. (agrebi2023dorfman–chanarinsyndromewith pages 1-2): Ikram Agrebi, Achraf Jaziri, Houda Kanoun, Najla Dammak, Mouna Boudabous, Salma Toumi, Soumaya Yaich, Nabil Tahri, Arwa Kammoun, Hafedh Makni, Khawla Kammoun, Tahya Boudawara, and Mohamed Ben Hmida. Dorfman–chanarin syndrome with renal involvement: a rare case report and literature review. Indian Journal of Nephrology, 33:472-475, Feb 2023. URL: https://doi.org/10.4103/ijn.ijn\_203\_22, doi:10.4103/ijn.ijn\_203\_22. This article has 1 citations and is from a peer-reviewed journal.

13. (elsayed2023anovelabhd5 pages 3-4): Solaf Mohamed Elsayed, Enza Torre, Daniela Tavian, Laura Moro, Corrado Angelini, Tawhida Y. Abdel Ghaffar, Khalid Zalata, Enas Ezzeldein Fahmy, and Sara Missaglia. A novel abhd5 mutation in two chanarin dorfman siblings with severe and heterogeneous clinical phenotype. May 2023. URL: https://doi.org/10.1016/j.gendis.2022.08.005, doi:10.1016/j.gendis.2022.08.005. This article has 2 citations.

14. (NCT02918032 chunk 1):  International Registry Study of Neutral Lipid Storage Disease (NLSD) / Triglyceride Deposit Cardiomyovasculopathy (TGCV) and Related Diseases. Translational Research Center for Medical Innovation, Kobe, Hyogo, Japan. 2014. ClinicalTrials.gov Identifier: NCT02918032

15. (NCT02830763 chunk 1):  Clinical Study on the Safety of CNT-02 for TGCV and NLSD-M. Translational Research Center for Medical Innovation, Kobe, Hyogo, Japan. 2016. ClinicalTrials.gov Identifier: NCT02830763

16. (NCT01527318 chunk 1):  The Effect of Fibrate Therapy in Two Patients With Neutral Lipid Storage Disease With Myopathy (NLSDM). Maastricht University Medical Center. 2011. ClinicalTrials.gov Identifier: NCT01527318

17. (NCT02918032 chunk 2):  International Registry Study of Neutral Lipid Storage Disease (NLSD) / Triglyceride Deposit Cardiomyovasculopathy (TGCV) and Related Diseases. Translational Research Center for Medical Innovation, Kobe, Hyogo, Japan. 2014. ClinicalTrials.gov Identifier: NCT02918032

18. (NCT02830763 chunk 2):  Clinical Study on the Safety of CNT-02 for TGCV and NLSD-M. Translational Research Center for Medical Innovation, Kobe, Hyogo, Japan. 2016. ClinicalTrials.gov Identifier: NCT02830763

19. (koc2025chanarindorfmansyndrome pages 1-4): A Koç and N Eren. Chanarindorfman syndrome. Unknown journal, 2025.

20. (schratter2022abhd5—aregulatorof pages 4-5): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

21. (schratter2022abhd5—aregulatorof pages 13-15): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

22. (schratter2022abhd5—aregulatorof pages 12-13): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

23. (redaelli2010clinicalandgenetic pages 2-3): Chiara Redaelli, Rosalind A Coleman, Laura Moro, Catherine Dacou-Voutetakis, Solaf Mohamed Elsayed, Daniele Prati, Agostino Colli, Donatella Mela, Roberto Colombo, and Daniela Tavian. Clinical and genetic characterization of chanarin-dorfman syndrome patients: first report of large deletions in the abhd5 gene. Orphanet Journal of Rare Diseases, 5:33-33, Dec 2010. URL: https://doi.org/10.1186/1750-1172-5-33, doi:10.1186/1750-1172-5-33. This article has 66 citations and is from a peer-reviewed journal.

24. (mangukiya2023chanarindorfmansyndrome(cds) pages 2-5): Nisarg P Mangukiya, Safa Kaleem, D Ragasri Meghana, Lyluma Ishfaq, Gunjan Kochhar, Bejoi Mathew, Shivani Pulekar, Aashka C Lainingwala, Mihirkumar P Parmar, and Vishal Venugopal. Chanarin-dorfman syndrome (cds): a rare lipid metabolism disorder. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.43889, doi:10.7759/cureus.43889. This article has 3 citations.

25. (schratter2022abhd5—aregulatorof pages 10-12): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

26. (schratter2022abhd5—aregulatorof pages 9-10): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

27. (schratter2022abhd5—aregulatorof pages 5-7): Margarita Schratter, Achim Lass, and Franz P. W. Radner. Abhd5—a regulator of lipid metabolism essential for diverse cellular functions. Metabolites, 12:1015, Oct 2022. URL: https://doi.org/10.3390/metabo12111015, doi:10.3390/metabo12111015. This article has 26 citations.

## Artifacts

- [Edison artifact artifact-00](Dorfman_Chanarin_Disease-deep-research-falcon_artifacts/artifact-00.md)