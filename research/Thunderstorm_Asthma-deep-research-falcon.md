---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T04:01:45.070322'
end_time: '2026-06-30T04:32:02.439995'
duration_seconds: 1817.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thunderstorm Asthma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Thunderstorm_Asthma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thunderstorm Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Thunderstorm Asthma** covering all of the
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
- **Disease Name:** Thunderstorm Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Thunderstorm Asthma** covering all of the
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


# Comprehensive Research Report: Thunderstorm Asthma

## 1. Disease Information

### Overview
Thunderstorm asthma (TA) is defined as acute asthma attacks or bronchospasm occurring immediately after thunderstorms, characterized by sudden onset, large-scale outbreaks, and potentially fatal acute exacerbations (xiao2026triggeringmechanismsof pages 2-4, xiao2026triggeringmechanismsof pages 1-2). It represents a unique clinical entity at the intersection of meteorology, aerobiology, and allergic respiratory disease, in which specific atmospheric conditions during thunderstorms generate respirable bioaerosols that trigger mass asthma events in sensitized populations (xiao2026triggeringmechanismsof pages 1-2).

### Key Identifiers
- **ICD-10/ICD-11:** Coded under J45 (Asthma) with environmental trigger specification. MeSH terms include "Asthma" (D001249), "Rhinitis, Allergic, Seasonal" (D006255), and "Hypersensitivity" (D006967) (NCT07055542 chunk 1).
- **MONDO ID:** No specific MONDO entry exists for thunderstorm asthma as a distinct disease entity; it is classified within the broader asthma spectrum.
- **Common synonyms:** Epidemic thunderstorm asthma (ETSA), thunderstorm-related asthma, thunderstorm allergy and asthma, storm-associated asthma.

### Information Source
The information in this report is derived from aggregated disease-level resources, including population-based epidemiological studies, case series from epidemic events, mechanistic research studies, and clinical trial registries.

---

## 2. Etiology

### Disease Causal Factors
Thunderstorm asthma follows a tripartite pathophysiological framework involving: (1) environmental triggers, (2) epithelial barrier disruption, and (3) immune dysregulation (xiao2026triggeringmechanismsof pages 2-4). The primary causal mechanism involves pollen rupture during thunderstorms: dry updrafts entrain whole pollen grains (10–100 μm) into thunderstorm clouds where high humidity causes them to rupture via osmotic shock, releasing approximately 700 starch granules as sub-pollen particles (SPPs) smaller than 2.5 μm (damato2015meteorologicalconditionsclimate pages 9-10, cecchi2025polleninducedasthmaa pages 3-4). Cold downdrafts then carry these pollen fragments to ground level, where they penetrate lower airways and trigger asthma attacks in sensitized individuals (damato2015meteorologicalconditionsclimate pages 9-10).

Multiple concurrent meteorological factors contribute: strong convection, humidity shifts, electrical activity, sudden temperature drops, and strong winds that dramatically alter bioaerosol profiles and disperse allergens and microbes (xiao2026triggeringmechanismsof pages 7-9). The 2016 Melbourne event demonstrated a 250% increase in ruptured grass pollen particles during the storm (xiao2026triggeringmechanismsof pages 2-4).

### Risk Factors

#### Environmental Risk Factors
- **Seasonal allergic rhinitis (SAR):** The predominant risk factor—SAR patients constituted 87% of emergency presentations in Melbourne 2016 and 79.35% in Hohhot, China (xiao2026triggeringmechanismsof pages 2-4).
- **Pollen sensitization:** 96% of affected individuals in one study had positive skin prick tests to ryegrass pollen, with an adjusted odds ratio of 23.0 compared to other asthma patients (damato2015meteorologicalconditionsclimate pages 9-10). In Melbourne, 90% of thunderstorm asthma cases reported recent hay fever symptoms compared with 69% of other asthma patients (damato2015meteorologicalconditionsclimate pages 9-10).
- **Outdoor exposure during thunderstorms:** Critical exposure factor; individuals who remained indoors with closed windows were protected (damato2015meteorologicalconditionsclimate pages 9-10).
- **High atmospheric pollen concentrations:** Epidemics occur only during seasons with high airborne allergenic pollen levels (damato2015meteorologicalconditionsclimate pages 9-10).
- **Urban residence:** Urban areas show higher TA risk due to elevated pollution and airborne allergen concentrations (xiao2026triggeringmechanismsof pages 4-5).
- **Air pollutants:** PM2.5, PM10, ozone, and NOx interact synergistically with fragmented pollen to compromise epithelial barriers and enhance allergen sensitization (xiao2026triggeringmechanismsof pages 4-5, xiao2026triggeringmechanismsof pages 15-16).

#### Genetic Risk Factors
- **17q21 locus:** Contains variants affecting GSDMB and ORMDL3 expression levels, influencing asthma risk. Specific SNPs (rs72163891 and rs7216389) alter mucosal GSDMB levels and IFN class responses (xiao2026triggeringmechanismsof pages 9-11).
- **TLR polymorphisms:** TLR4 polymorphisms (e.g., D298G/N397I) amplify inflammatory responses to storm-dispersed allergens and Gram-negative bacteria. TLR5 and TLR7 expression is reduced by 40% and 60% respectively in severe asthma patients, decreasing clearance of inhaled pathogens (xiao2026triggeringmechanismsof pages 7-9).
- **Epithelial barrier genes:** FLG (filaggrin) and SPINK5 gene variants affect barrier integrity and increase susceptibility (xiao2026triggeringmechanismsof pages 1-2).
- **Epigenetic modifications:** DNA methylation and histone modifications dynamically regulate susceptibility genes (xiao2026triggeringmechanismsof pages 1-2).
- **Microbiome-host interactions:** Airway microbial dysbiosis, including decreased microbial diversity and dysregulated short-chain fatty acid metabolism, interacts with environmental exposures to modulate susceptibility (xiao2026triggeringmechanismsof pages 1-2).

#### Other Risk Factors
- Smoking, obesity, and glucocorticoid-resistant asthma increase susceptibility (xiao2026triggeringmechanismsof pages 9-11).
- Suboptimal asthma treatment (damato2015meteorologicalconditionsclimate pages 9-10).
- Asian/Indian ethnicity groups showed higher susceptibility in Melbourne (xiao2026triggeringmechanismsof pages 2-4).

### Protective Factors
- **Staying indoors with closed windows during thunderstorms** provides direct protection (damato2015meteorologicalconditionsclimate pages 9-10).
- **Regular inhaled corticosteroid use** may be protective by reducing airway hyperresponsiveness (damato2015meteorologicalconditionsclimate pages 9-10).
- **Optimal asthma treatment** reduces risk of severe exacerbations during thunderstorm events (damato2015meteorologicalconditionsclimate pages 9-10).

### Gene-Environment Interactions
Gene-environment interactions are pivotal in determining individual susceptibility to TA. Genetic variations in innate immunity (particularly TLR polymorphisms) combine with thunderstorm-specific environmental dispersal of allergens and microbes to amplify inflammatory responses (xiao2026triggeringmechanismsof pages 7-9). The interaction of 17q21 genetic variants with environmental factors such as viruses and pollutants during thunderstorms increases acute asthma episode risk (xiao2026triggeringmechanismsof pages 9-11). Geographic variations in TLR polymorphisms further influence TA risk by interacting with region-specific environmental exposures and allergen profiles (xiao2026triggeringmechanismsof pages 7-9). The specific mechanisms of these gene-environment interactions remain an active area of research and have hindered construction of precise risk prediction models (xiao2026triggeringmechanismsof pages 1-2).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
Thunderstorm asthma presents as acute-onset asthma with the following features:

- **Acute bronchospasm:** Sudden onset wheezing, chest tightness, shortness of breath occurring within minutes to hours of thunderstorm onset (xiao2026triggeringmechanismsof pages 2-4).
- **Severe dyspnea:** Can rapidly progress to severe respiratory insufficiency requiring ICU admission (damato2015meteorologicalconditionsclimate pages 9-10).
- **Rhinitis symptoms:** Nasal congestion, sneezing, rhinorrhea frequently accompany or precede bronchospasm. Suggested HPO: HP:0003193 (Allergic rhinitis).
- **Cough:** Productive or non-productive cough. Suggested HPO: HP:0012735 (Cough).
- **Near-fatal/fatal asthma:** In severe cases, acute respiratory failure requiring mechanical ventilation (damato2015meteorologicalconditionsclimate pages 9-10). Suggested HPO: HP:0002878 (Respiratory failure).

### Phenotype Characteristics
- **Age of onset:** Can affect any age, but thunderstorms increase children's hospital visit risk by 27% with precipitation increases; each 1°C temperature drop increases risk among adults under 65 by 1.4% (xiao2026triggeringmechanismsof pages 2-4).
- **Severity:** Variable—ranges from mild bronchospasm to near-fatal or fatal asthma attacks (damato2015meteorologicalconditionsclimate pages 9-10).
- **Progression:** Episodic—directly linked to thunderstorm events during pollen seasons. Onset is typically acute (within 20-30 minutes of thunderstorm) (xiao2026triggeringmechanismsof pages 1-2).
- **Frequency:** Seasonal, dependent on co-occurrence of high pollen counts and thunderstorm activity.

### Quality of Life Impact
Thunderstorm asthma episodes can cause acute, severe disruption of daily functioning, with mass emergency department presentations overwhelming healthcare systems. A 3-year longitudinal study documented persistent asthma symptoms following the 2016 Melbourne event, suggesting lasting impact on respiratory health in some individuals.

### Suggested HPO Terms
- HP:0002099 (Asthma)
- HP:0003193 (Allergic rhinitis)
- HP:0002094 (Dyspnea)
- HP:0012735 (Cough)
- HP:0002878 (Respiratory failure)
- HP:0100785 (Wheezing)
- HP:0002098 (Respiratory distress)

---

## 4. Genetic/Molecular Information

### Susceptibility Genes (Not Causal in Mendelian Sense)
Thunderstorm asthma is a complex, multifactorial condition without single-gene causation. However, several genes modify susceptibility:

- **GSDMB** (Gasdermin B, 17q21): Variants affect mucosal expression levels and IFN responses; SNP rs7216389 is strongly associated with asthma susceptibility (xiao2026triggeringmechanismsof pages 9-11).
- **ORMDL3** (ORMDL Sphingolipid Biosynthesis Regulator 3, 17q21): Altered expression levels influence asthma risk through the 17q21 genomic locus (xiao2026triggeringmechanismsof pages 9-11).
- **TLR4** (Toll-like receptor 4): Polymorphisms such as D298G/N397I amplify inflammatory responses to allergens and LPS from storm-dispersed Gram-negative bacteria (xiao2026triggeringmechanismsof pages 7-9).
- **TLR5** and **TLR7**: Reduced expression (40% and 60% reductions respectively in severe asthma) impairs clearance of inhaled pathogens, increasing airway inflammation during thunderstorm events (xiao2026triggeringmechanismsof pages 7-9).
- **FLG** (Filaggrin): Epithelial barrier-related gene; variants compromise barrier integrity (xiao2026triggeringmechanismsof pages 1-2).
- **SPINK5** (Serine Peptidase Inhibitor Kazal Type 5): Epithelial barrier-related gene affecting susceptibility (xiao2026triggeringmechanismsof pages 1-2).

### Epigenetic Information
Dynamic changes in DNA methylation and histone modifications contribute to thunderstorm asthma susceptibility (xiao2026triggeringmechanismsof pages 1-2). These epigenetic modifications can be influenced by environmental exposures and may explain why some sensitized individuals are more vulnerable than others during identical thunderstorm events.

---

## 5. Environmental Information

### Environmental Factors
- **Pollen:** Ryegrass (*Lolium perenne*) pollen is the primary trigger in temperate zones (particularly Australia and Europe), while Parietaria, olive, and Artemisia pollen are implicated in other regions (cecchi2025polleninducedasthmaa pages 4-6, damato2015meteorologicalconditionsclimate pages 9-10). Pollen grains rupture via osmotic pressure to release sub-pollen particles (SPPs) of 0.5–2.5 μm diameter (cecchi2025polleninducedasthmaa pages 3-4).
- **Air pollution:** PM2.5, PM10, ozone, and NOx show positive correlations with asthma hospital visits and interact synergistically with fragmented pollen (xiao2026triggeringmechanismsof pages 2-4, xiao2026triggeringmechanismsof pages 15-16).
- **Fungal spores:** Alternaria alternata and other fungal molds dispersed during thunderstorms contribute to the bioaerosol mixture (xiao2026triggeringmechanismsof pages 17-18).
- **Meteorological conditions:** Sudden temperature drops, humidity increases, strong winds, heavy rainfall, and electrical discharge from lightning all contribute to pollen rupture and bioaerosol dispersal (xiao2026triggeringmechanismsof pages 2-4, xiao2026triggeringmechanismsof pages 4-5).

### Climate Change Impact
Climate change is driving significant increases in thunderstorm asthma frequency: 8 major TA events were documented from 1983–1999 compared to 17 events from 2000–2024, paralleling climate change-driven increases in extreme convective weather, extended pollen seasons, and enhanced pollen allergenicity (xiao2026triggeringmechanismsof pages 2-4). Warming temperatures extend pollen seasons and increase pollen levels globally, while thunderstorms are becoming more likely to coincide with elevated pollen counts (xiao2026triggeringmechanismsof pages 15-16). Rising CO2 levels enhance plant photosynthesis and reproductive capacity, resulting in increased pollen production (damato2015meteorologicalconditionsclimate pages 1-2).

---

## 6. Mechanism / Pathophysiology

### Causal Chain

The pathophysiology follows an "environmental trigger → epithelial barrier disruption → immune dysregulation" framework (xiao2026triggeringmechanismsof pages 1-2):

**Step 1 – Environmental Trigger (Upstream):**
Thunderstorms create unique atmospheric conditions. Dry updrafts entrain whole pollen grains into cloud bases where osmotic shock from high humidity causes rupture, releasing approximately 700 starch granules per grain as sub-pollen particles (SPPs) < 2.5 μm. Cold downdrafts distribute these to ground level alongside PM2.5, ozone, and fungal spores, forming complex bioaerosols (damato2015meteorologicalconditionsclimate pages 9-10, xiao2026triggeringmechanismsof pages 5-7).

**Step 2 – Epithelial Barrier Disruption (Intermediate):**
SPPs and associated bioaerosols cause tight junction disruption, with pollen proteases cleaving occludin, claudins, E-cadherin, and ZO-1 proteins (xiao2026triggeringmechanismsof pages 4-5). This leads to impaired mucociliary clearance and increased epithelial permeability. Damaged epithelial cells release alarmins—IL-25, IL-33, and TSLP—which serve as the pathological hub linking environmental triggers to immune activation (xiao2026triggeringmechanismsof pages 1-2, xiao2026triggeringmechanismsof pages 5-7).

**Step 3 – Immune Dysregulation (Downstream):**
- **Type 2 pathway (ILC2/Th2 axis):** Alarmins activate ILC2 cells and dendritic cells, promoting Th2 differentiation. IL-4, IL-5, and IL-13 production drives IgE upregulation, eosinophil activation and infiltration, and increased mucus production (xiao2026triggeringmechanismsof pages 5-7).
- **IgE-mediated responses:** Elevated allergen-specific IgE binds to high-affinity FcεRI receptors on mast cells and basophils, causing histamine and inflammatory mediator release (xiao2026triggeringmechanismsof pages 5-7).
- **Non-type 2 pathway (Th17/neutrophilic):** IL-6/IL-17-mediated neutrophilic inflammation contributes, particularly in severe or steroid-resistant cases (xiao2026triggeringmechanismsof pages 15-16).
- **TLR-mediated innate immunity:** TLRs recognize storm-generated microbial components, activating NF-κB signaling and releasing TNF-α, IL-1β, and IL-6 (xiao2026triggeringmechanismsof pages 7-9).
- **Aryl hydrocarbon receptor:** Activated by pollutant-pollen aggregates in airway epithelial cells (xiao2026triggeringmechanismsof pages 7-9).

**Step 4 – Clinical Manifestation:**
Cascading immune and environmental insults cause severe epithelial damage, goblet cell hyperplasia, mucus overproduction, and airway smooth muscle contraction, culminating in acute bronchospasm and severe asthma attacks (xiao2026triggeringmechanismsof pages 7-9).

### Molecular Pathways
- NF-κB signaling pathway (inflammatory cytokine production)
- IgE-FcεRI signaling (mast cell degranulation)
- IL-4/IL-13 JAK-STAT6 pathway (Th2 polarization)
- IL-5 signaling (eosinophil recruitment)
- IL-17 pathway (neutrophilic inflammation)
- Aryl hydrocarbon receptor pathway

### Suggested GO Terms
- GO:0006955 (Immune response)
- GO:0006954 (Inflammatory response)
- GO:0002377 (Immunoglobulin production)
- GO:0045576 (Mast cell activation)
- GO:0030595 (Leukocyte chemotaxis)
- GO:0043312 (Neutrophil degranulation)

### Suggested CL Terms (Cell Types)
- CL:0000236 (B cell)
- CL:0000545 (T-helper 2 cell)
- CL:0000897 (CD4-positive, alpha-beta memory T cell)
- CL:0000771 (Eosinophil)
- CL:0000097 (Mast cell)
- CL:0000623 (Natural killer cell)
- CL:0001065 (ILC2 cell)
- CL:0002063 (Type II pneumocyte)
- CL:0000082 (Epithelial cell of lung)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Lungs (lower airways, bronchi, bronchioles) — UBERON:0002048 (lung)
- **Secondary:** Upper airways (nasal mucosa, sinuses) — UBERON:0001707 (nasal cavity); conjunctivae

### Tissue and Cell Level
- **Airway epithelium:** Bronchial and bronchiolar epithelial cells with tight junction disruption (xiao2026triggeringmechanismsof pages 4-5)
- **Smooth muscle:** Airway smooth muscle contraction (xiao2026triggeringmechanismsof pages 7-9)
- **Mucosa:** Goblet cell hyperplasia and mucus overproduction (xiao2026triggeringmechanismsof pages 7-9)
- **Immune cells:** Eosinophils, mast cells, ILC2 cells, Th2 cells, neutrophils

### Body Systems
- Respiratory system (primary)
- Immune system (secondary — allergic/inflammatory cascade)

---

## 8. Temporal Development

### Onset
- **Age of onset:** Any age; affects both children and adults. Children show increased hospital visit risk with precipitation (27% increase), while adults under 65 show 1.4% increased risk per 1°C temperature drop (xiao2026triggeringmechanismsof pages 2-4).
- **Onset pattern:** Acute — symptoms develop within 20–30 minutes to hours of thunderstorm onset during pollen season (xiao2026triggeringmechanismsof pages 1-2).

### Progression
- **Disease course:** Episodic — directly linked to thunderstorm events during high pollen seasons
- **Duration:** Self-limited in most cases, though some patients may develop persistent asthma symptoms
- **Critical period:** The first 30 hours after a thunderstorm event during pollen season represent the critical vulnerability window (xiao2026triggeringmechanismsof pages 1-2)

### Patterns
- Seasonal clustering during spring/summer pollen seasons
- Increasing frequency over time: 8 major events in 1983–1999 vs. 17 events in 2000–2024 (xiao2026triggeringmechanismsof pages 2-4)

---

## 9. Inheritance and Population

### Epidemiology
Thunderstorm asthma is not a continuous-prevalence disease but rather an episodic, epidemic phenomenon. Its frequency is increasing globally due to climate change (xiao2026triggeringmechanismsof pages 2-4).

### Population Demographics
- **Geographic distribution:** Documented across multiple continents including Australia, Europe (Italy, UK), Middle East (Kuwait, Iran), Asia (China—Hohhot, Yulin), North America (USA, Canada), New Zealand, and Israel (xiao2026triggeringmechanismsof pages 17-18, xiao2026triggeringmechanismsof pages 2-4).
- **Affected populations:** Individuals with seasonal allergic rhinitis and pollen sensitization are predominantly affected. Geographic clustering reveals higher susceptibility among Asian/Indian ethnicity groups in Melbourne (xiao2026triggeringmechanismsof pages 2-4).
- **Climate zones:** Temperate zones are linked to grass pollen and type 2 inflammation; arid zones show mixed phenotypes with drought-tolerant pollens like Artemisia and Salsola (xiao2026triggeringmechanismsof pages 2-4).

The following table summarizes major documented thunderstorm asthma events worldwide:

| Location | Year | Key allergen(s) / trigger profile | Affected individuals / scale | Outcomes / notable findings | Evidence |
|---|---:|---|---|---|---|
| Melbourne, Victoria, Australia | 2016 | Grass pollen, especially ryegrass; thunderstorm-associated ruptured pollen particles | 3,365 emergency presentations for breathing problems within 30 hours; 476 additional asthma admissions; 672% increase in ED visits; 992% increase in admissions | 10 deaths; described as the most severe documented epidemic thunderstorm asthma event; 87% of emergency presentations had seasonal allergic rhinitis | (xiao2026triggeringmechanismsof pages 1-2, xiao2026triggeringmechanismsof pages 2-4) |
| Wagga Wagga, New South Wales, Australia | not stated in retrieved evidence | Ryegrass pollen during thunderstorm conditions | 215 asthmatic subjects attended emergency department | 41 hospital admissions; 96% had positive skin tests to ryegrass pollen | (damato2015meteorologicalconditionsclimate pages 9-10) |
| Naples, Italy | 2004 | Parietaria pollen during thunderstorm conditions | 7 patients with severe asthma attacks | 1 near-fatal case requiring ICU admission for severe bronchial obstruction and acute respiratory insufficiency; all 7 sensitized to Parietaria pollen | (damato2015meteorologicalconditionsclimate pages 9-10) |
| Hohhot, China | not stated in retrieved evidence | Arid-zone pollen profile, including drought-tolerant pollens such as Artemisia/Salsola | Exact event count not provided in retrieved evidence | 79.35% of cases had seasonal allergic rhinitis; cited as a major recent outbreak in an arid region | (xiao2026triggeringmechanismsof pages 2-4) |
| Ahvaz, Iran (southwest region) | not stated in retrieved evidence | Thunderstorm-linked aeroallergen outbreak; specific allergen not detailed in retrieved evidence | Exact event count not provided in retrieved evidence | Cited as a major outbreak region in global epidemiology summaries | (xiao2026triggeringmechanismsof pages 17-18, xiao2026triggeringmechanismsof pages 2-4) |
| Kuwait | not stated in retrieved evidence | Thunderstorm-linked aeroallergen outbreak in desert climate; specific allergen not detailed in retrieved evidence | Exact event count not provided in retrieved evidence | Fatal and near-fatal cases reported in a desert-country setting | (xiao2026triggeringmechanismsof pages 17-18) |
| New Zealand | not stated in retrieved evidence | Thunderstorm-related aeroallergen exposure; specific allergen not detailed in retrieved evidence | Case/event numbers not provided in retrieved evidence | Confirms thunderstorm-related asthma can occur outside Australia in comparable pollen seasons | (xiao2026triggeringmechanismsof pages 17-18) |
| Canada | not stated in retrieved evidence | Thunderstorm-linked aeroallergen exposure; specific allergen not detailed in retrieved evidence | Case/event numbers not provided in retrieved evidence | Listed among documented countries with thunderstorm asthma reports | (xiao2026triggeringmechanismsof pages 17-18) |
| Israel | not stated in retrieved evidence | Thunderstorm-linked aeroallergen exposure; specific allergen not detailed in retrieved evidence | Case/event numbers not provided in retrieved evidence | Listed among documented countries with thunderstorm asthma reports | (xiao2026triggeringmechanismsof pages 17-18) |
| United Kingdom | not stated in retrieved evidence | Thunderstorm-linked pollen sensitization; specific allergen not detailed in retrieved evidence | Case/event numbers not provided in retrieved evidence | Referenced in global summaries as part of documented thunderstorm asthma literature | (xiao2026triggeringmechanismsof pages 17-18) |


*Table: This table summarizes major documented thunderstorm asthma outbreaks and reports worldwide, highlighting geography, likely allergens, scale, and clinical outcomes. It is useful for comparing recurrent epidemiologic patterns across temperate and arid settings.*

---

## 10. Diagnostics

### Clinical Diagnosis
Thunderstorm asthma is primarily a clinical-epidemiological diagnosis based on:
- Acute asthma presentation temporally associated with a thunderstorm event
- Occurrence during high pollen season
- Evidence of pollen sensitization (skin prick testing, serum specific IgE)

### Biomarkers
- **Serum specific IgE (sp-IgE)** to ryegrass pollen and allergen sub-components (Lol p 1, Lol p 5, Phl p 2, Phl p 5) — the CARISTA study is investigating sp-IgE thresholds as key predictive biomarkers (NCT07055542 chunk 1).
- **Blood eosinophil levels** — inflammatory cell marker assessed in the CARISTA study (NCT07055542 chunk 1).
- **Skin prick testing** to grass pollen — 96% positivity to ryegrass in affected populations (damato2015meteorologicalconditionsclimate pages 9-10).

### Functional Tests
- **Spirometry (FEV1):** Lung function testing to assess baseline airway obstruction and asthma severity (NCT07055542 chunk 1).
- **Peak expiratory flow:** For monitoring acute bronchospasm.

### Differential Diagnosis
- Conventional asthma exacerbation (non-thunderstorm related)
- Anaphylaxis
- Acute bronchitis
- Hyperventilation syndrome
- Pulmonary embolism
- Foreign body aspiration

### Screening
The CARISTA study (NCT07055542) is developing a biomarker-based risk assessment tool to identify individuals at high risk of seasonal allergic and thunderstorm asthma, using sp-IgE thresholds, lung function, eosinophil levels, and allergen component sensitization profiles (NCT07055542 chunk 1).

---

## 11. Outcome/Prognosis

### Mortality
The 2016 Melbourne event—the most severe documented epidemic thunderstorm asthma event—resulted in 10 deaths within 30 hours (xiao2026triggeringmechanismsof pages 1-2). Near-fatal cases requiring ICU admission have been documented in Naples and other locations (damato2015meteorologicalconditionsclimate pages 9-10). One case report documented a relapse in a pregnant woman who experienced near-fatal asthma 7 years after an initial thunderstorm episode (damato2015meteorologicalconditionsclimate pages 9-10).

### Morbidity
During the 2016 Melbourne event, emergency departments experienced a 672% increase in visits for breathing problems (3,365 total visits) with 476 additional asthma admissions representing a 992% increase (xiao2026triggeringmechanismsof pages 1-2). Healthcare system surge capacity was severely strained.

### Disease Course
Most cases are self-limited with appropriate acute treatment. However, longitudinal studies suggest some patients develop persistent asthma symptoms following severe thunderstorm asthma episodes.

---

## 12. Treatment

### Acute Management
- **Inhaled bronchodilators (SABA):** First-line for acute bronchospasm relief (xiao2026triggeringmechanismsof pages 13-15). Suggested MAXO: MAXO:0000381 (Bronchodilator therapy).
- **Oxygen therapy:** For severe hypoxemic cases (damato2015meteorologicalconditionsclimate pages 9-10).
- **Systemic corticosteroids:** Intravenous methylprednisolone for severe attacks (damato2015meteorologicalconditionsclimate pages 9-10). Suggested MAXO: MAXO:0000647 (Corticosteroid therapy).

### Chronic/Preventive Management
- **Inhaled corticosteroids (ICS):** Stabilize epithelial barrier function and reduce airway inflammation with consistent use; may be protective against thunderstorm-induced attacks (xiao2026triggeringmechanismsof pages 13-15, damato2015meteorologicalconditionsclimate pages 9-10). Suggested MAXO: MAXO:0001001 (Inhaled corticosteroid therapy).
- **Triple therapy (ICS/LABA/LAMA):** For patients with inadequately controlled type 2 inflammation (xiao2026triggeringmechanismsof pages 13-15).
- **Allergen immunotherapy (AIT):** Disease-modifying treatment for long-term management, administered subcutaneously, sublingually, or orally (xiao2026triggeringmechanismsof pages 13-15). Suggested MAXO: MAXO:0001189 (Allergen immunotherapy).
- **Biologic agents:** Anti-IgE (omalizumab), anti-IL-5, and anti-IL-4R biologics for severe cases with persistent type 2 inflammation (xiao2026triggeringmechanismsof pages 13-15). Suggested MAXO: MAXO:0001195 (Biologic therapy).

### Active Clinical Trial
The **CARISTA Study** (NCT07055542, University of Melbourne, recruiting since August 2025, estimated completion 2030) is enrolling 530 adults with seasonal allergic rhinitis to develop a biomarker-based risk assessment tool for predicting and preventing seasonal allergic and thunderstorm asthma exacerbations (NCT07055542 chunk 1, NCT07055542 chunk 2).

---

## 13. Prevention

### Primary Prevention
- **Avoidance of outdoor exposure during thunderstorms:** The most effective prevention; remaining indoors with closed windows during thunderstorm events in pollen season is protective (damato2015meteorologicalconditionsclimate pages 9-10).
- **Early warning systems:** Integrating meteorological data with allergen concentration tracking to generate timely TA risk alerts. Machine learning models enhance detection of severe weather events coinciding with high pollen levels, enabling patients to receive alerts to stay indoors (xiao2026triggeringmechanismsof pages 15-16, xiao2026triggeringmechanismsof pages 12-13).
- **Public health education:** Targeted health education for vulnerable populations (asthma/allergic rhinitis patients) to enhance self-protection skills and emergency response capabilities (xiao2026triggeringmechanismsof pages 12-13).
- **Air quality interventions:** Strengthening air quality standards to reduce pollutants (PM2.5, O3, NO2) and implementing urban greening to mitigate airborne allergen concentrations (xiao2026triggeringmechanismsof pages 12-13).

### Secondary Prevention
- **Pollen monitoring systems:** Real-time monitoring and funding for pollen monitoring to provide accurate data for treatment decisions and allergen avoidance (xiao2026triggeringmechanismsof pages 15-16).
- **Wearable sensors and digital health:** Personal health parameter monitoring through wearable devices and smart health management systems (xiao2026triggeringmechanismsof pages 13-15, xiao2026triggeringmechanismsof pages 12-13).
- **Cross-departmental collaboration:** Coordination among meteorological, public health, and medical institutions for rapid response (xiao2026triggeringmechanismsof pages 12-13).

### Tertiary Prevention
- **Individualized treatment pathways:** Based on risk assessment including symptom management, exacerbation risk, type 2 inflammatory markers, allergic conditions, and comorbidities (xiao2026triggeringmechanismsof pages 15-16).
- **Collaborative multidisciplinary care:** Involving pulmonologists, allergists, and otolaryngologists (xiao2026triggeringmechanismsof pages 15-16).
- **Targeted interventions for disadvantaged communities:** Addressing socioeconomic factors affecting susceptibility (xiao2026triggeringmechanismsof pages 12-13).

---

## 14. Other Species / Natural Disease

### Veterinary Relevance
Thunderstorm asthma is primarily a human condition linked to allergic sensitization. While horses can develop recurrent airway obstruction (equine asthma) triggered by environmental allergens, specific thunderstorm-triggered asthma epidemics in animals have not been well documented. Grass pollen affects multiple mammalian species, and companion animals (dogs, cats) can develop pollen-allergic conditions, though thunderstorm-specific triggering has not been systematically studied.

---

## 15. Model Organisms

### Model Systems
No specific animal models have been developed exclusively for thunderstorm asthma. However, relevant model systems include:
- **Murine models of pollen-induced asthma:** Ovalbumin-sensitized and pollen-challenged mouse models recapitulate aspects of IgE-mediated airway inflammation.
- **Sub-pollen particle exposure models:** In vitro studies using osmotically ruptured pollen particles to study allergenicity at the component level.
- **Airway epithelial cell cultures:** Human bronchial epithelial cells exposed to pollen extracts and particulate matter to study tight junction disruption, alarmin release, and barrier function.

### Limitations
Current models do not fully recapitulate the mass-exposure, acute-onset nature of thunderstorm asthma or the complex bioaerosol mixtures (pollen fragments + pollutants + fungal spores) encountered during real thunderstorm events.

---

## Summary and Future Directions

Thunderstorm asthma is an increasingly recognized, climate-sensitive public health emergency characterized by mass acute asthma events triggered by the confluence of thunderstorm meteorology and high allergenic pollen concentrations. The pathophysiology involves a cascade from environmental trigger (pollen rupture to sub-pollen particles) through epithelial barrier disruption to immune dysregulation via both type 2 (ILC2/Th2/IgE) and non-type 2 (Th17/neutrophilic) pathways (xiao2026triggeringmechanismsof pages 1-2, xiao2026triggeringmechanismsof pages 15-16). Climate change is amplifying the risk by extending pollen seasons, increasing pollen concentrations, and generating more frequent severe thunderstorms (xiao2026triggeringmechanismsof pages 2-4, xiao2026triggeringmechanismsof pages 15-16). Future research priorities include development of validated early warning systems using machine learning, identification of predictive biomarkers through studies like CARISTA (NCT07055542 chunk 1), elucidation of gene-environment interactions governing individual susceptibility (xiao2026triggeringmechanismsof pages 1-2), and implementation of integrated public health response frameworks across meteorological and healthcare systems (xiao2026triggeringmechanismsof pages 12-13).

References

1. (xiao2026triggeringmechanismsof pages 2-4): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (xiao2026triggeringmechanismsof pages 1-2): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

3. (NCT07055542 chunk 1):  Creating A Risk Assessment Tool for Thunderstorm Asthma: the CARISTA Study. University of Melbourne. 2025. ClinicalTrials.gov Identifier: NCT07055542

4. (damato2015meteorologicalconditionsclimate pages 9-10): G. D'Amato, S. Holgate, R. Pawankar, D. Ledford, L. Cecchi, M. Al‐Ahmad, Fatma Al-Enezi, S. Al‐Muhsen, I. Ansotegui, C. Baena-Cagnani, David J. Baker, H. Bayram, K. Bergmann, L. Boulet, J. Buters, M. D’Amato, Sofia Dorsano, J. Douwes, S. E. Finlay, D. Garrasi, Maximiliano Gómez, T. Haahtela, R. Halwani, Youssouf Hassani, B. Mahboub, G. Marks, P. Michelozzi, M. Montagni, C. Nunes, J. J. Oh, Todor A Popov, J. Portnoy, E. Ridolo, N. Rosário, M. Rottem, M. Sánchez-Borges, Elopy Sibanda, J. Sienra-Monge, C. Vitale, and I. Annesi-Maesano. Meteorological conditions, climate change, new emerging factors, and asthma and related allergic disorders. a statement of the world allergy organization. The World Allergy Organization Journal, Jul 2015. URL: https://doi.org/10.1186/s40413-015-0073-0, doi:10.1186/s40413-015-0073-0. This article has 764 citations and is from a peer-reviewed journal.

5. (cecchi2025polleninducedasthmaa pages 3-4): L. Cecchi, M. Martini, K. Jaubashi, A.M. Marra, A. Musarra, F. Papia, A. Vaghi, G. Valenti, B. Yang, and M.B. Bilò. Pollen-induced asthma: a specific pheno-endotype of disease? European Annals of Allergy and Clinical Immunology, 57:197, Sep 2025. URL: https://doi.org/10.23822/eurannaci.1764-1489.403, doi:10.23822/eurannaci.1764-1489.403. This article has 3 citations and is from a peer-reviewed journal.

6. (xiao2026triggeringmechanismsof pages 7-9): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

7. (xiao2026triggeringmechanismsof pages 4-5): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

8. (xiao2026triggeringmechanismsof pages 15-16): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (xiao2026triggeringmechanismsof pages 9-11): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (cecchi2025polleninducedasthmaa pages 4-6): L. Cecchi, M. Martini, K. Jaubashi, A.M. Marra, A. Musarra, F. Papia, A. Vaghi, G. Valenti, B. Yang, and M.B. Bilò. Pollen-induced asthma: a specific pheno-endotype of disease? European Annals of Allergy and Clinical Immunology, 57:197, Sep 2025. URL: https://doi.org/10.23822/eurannaci.1764-1489.403, doi:10.23822/eurannaci.1764-1489.403. This article has 3 citations and is from a peer-reviewed journal.

11. (xiao2026triggeringmechanismsof pages 17-18): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

12. (damato2015meteorologicalconditionsclimate pages 1-2): G. D'Amato, S. Holgate, R. Pawankar, D. Ledford, L. Cecchi, M. Al‐Ahmad, Fatma Al-Enezi, S. Al‐Muhsen, I. Ansotegui, C. Baena-Cagnani, David J. Baker, H. Bayram, K. Bergmann, L. Boulet, J. Buters, M. D’Amato, Sofia Dorsano, J. Douwes, S. E. Finlay, D. Garrasi, Maximiliano Gómez, T. Haahtela, R. Halwani, Youssouf Hassani, B. Mahboub, G. Marks, P. Michelozzi, M. Montagni, C. Nunes, J. J. Oh, Todor A Popov, J. Portnoy, E. Ridolo, N. Rosário, M. Rottem, M. Sánchez-Borges, Elopy Sibanda, J. Sienra-Monge, C. Vitale, and I. Annesi-Maesano. Meteorological conditions, climate change, new emerging factors, and asthma and related allergic disorders. a statement of the world allergy organization. The World Allergy Organization Journal, Jul 2015. URL: https://doi.org/10.1186/s40413-015-0073-0, doi:10.1186/s40413-015-0073-0. This article has 764 citations and is from a peer-reviewed journal.

13. (xiao2026triggeringmechanismsof pages 5-7): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

14. (xiao2026triggeringmechanismsof pages 13-15): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

15. (NCT07055542 chunk 2):  Creating A Risk Assessment Tool for Thunderstorm Asthma: the CARISTA Study. University of Melbourne. 2025. ClinicalTrials.gov Identifier: NCT07055542

16. (xiao2026triggeringmechanismsof pages 12-13): Zhimin Xiao, Yilin Shi, Dongpeng Zhao, Ying Wang, and Yan Gu. Triggering mechanisms of acute thunderstorm asthma: epithelial barrier disruption and immune dysregulation. Respiratory Research, Feb 2026. URL: https://doi.org/10.1186/s12931-026-03532-6, doi:10.1186/s12931-026-03532-6. This article has 1 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Thunderstorm_Asthma-deep-research-falcon_artifacts/artifact-00.md)