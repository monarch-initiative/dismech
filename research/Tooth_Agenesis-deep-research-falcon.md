---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T10:38:27.536372'
end_time: '2026-06-22T10:56:55.800058'
duration_seconds: 1108.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tooth Agenesis
  mondo_id: ''
  category: Genetic
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
  path: Tooth_Agenesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tooth Agenesis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tooth Agenesis** covering all of the
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
- **Disease Name:** Tooth Agenesis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Tooth Agenesis** covering all of the
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


# Comprehensive Research Report: Tooth Agenesis

## 1. Disease Information

### Overview
Tooth agenesis is a congenital developmental anomaly characterized by the failure of one or more teeth to develop (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 1-2, fallea2025dissectingthegenetic pages 1-2). It represents the most common manifestation of defective dental morphogenesis in humans and can range from the absence of a single tooth to complete absence of all teeth (fallea2025dissectingthegenetic pages 1-2).

### Classification and Nomenclature
The condition is classified based on the number of congenitally missing teeth (excluding third molars):

- **Hypodontia**: Developmental absence of one to five teeth (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 2-4)
- **Oligodontia**: Agenesis of six or more teeth (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 2-4)
- **Anodontia**: Complete absence of all teeth (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 2-4)

### Common Synonyms and Alternative Names
- Dental agenesis
- Congenital tooth agenesis (CTA)
- Selective tooth agenesis (for specific tooth patterns)
- Tooth number anomaly
(meade2023toothagenesisan pages 1-2, fallea2025dissectingthegenetic pages 1-2)

### Key Identifiers
- **HPO Terms**: 
  - HP:0009804 (Tooth agenesis - general)
  - HP:0001592 (Selective tooth agenesis)
  - HP:0011079 (Impacted tooth)
  - HP:0200160 (Agenesis of maxillary incisor)
  - HP:0000706 (Eruption failure)
(fallea2025dissectingthegenetic pages 4-6)

- **OMIM Entries** (Examples of associated conditions):
  - Selective tooth agenesis 1: OMIM #106600 (MSX1-related)
  - Selective tooth agenesis 3: related to PAX9
  - X-linked hypohidrotic ectodermal dysplasia: OMIM #305100 (EDA-related)
  - Selective tooth agenesis 9: GREM2-related
  - Selective tooth agenesis 10: TSPEAR-related
(modafferi2025geneticaspectsof pages 5-7)

### Data Sources
The information synthesized here derives from both aggregated disease-level resources (OMIM, Orphanet, HPO database, systematic reviews) and individual clinical cohorts reported in recent literature (2020-2025) (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 1-2, fallea2025dissectingthegenetic pages 1-2).

---

## 2. Etiology

### Disease Causal Factors

Tooth agenesis has a multifactorial etiology involving genetic, epigenetic, and environmental factors (fallea2025dissectingthegenetic pages 1-2, meade2023toothagenesisan pages 3-4, meade2023toothagenesisan pages 2-3).

**Genetic Causes**: The majority of tooth agenesis cases have a strong genetic basis. Over 300 genes contribute to tooth development, with approximately 20 genes confirmed to be associated with permanent tooth agenesis (su2024edavariantsare pages 1-2). The most frequently implicated genes include EDA, MSX1, WNT10A, and PAX9, each associated with specific patterns of missing teeth and involved in both isolated and syndromic forms (modafferi2025geneticaspectsof pages 1-2, modafferi2025geneticaspectsof pages 5-7).

**Mechanistic Pathways**: Gene mutations result in impaired molecular signaling during odontogenesis, including:
- Disruption of epithelial-mesenchymal interactions
- Malfunctioning of extracellular matrix molecules
- Defective signaling pathways (Wnt, BMP, FGF, SHH, TNF receptor pathways)
- Impairment of molecules facilitating cell adhesion
(meade2023toothagenesisan pages 3-4)

### Risk Factors

**Genetic Risk Factors**:

1. **Causal Variants**: Pathogenic or likely pathogenic variants in key developmental genes cause tooth agenesis (modafferi2025geneticaspectsof pages 5-7). Recent genetic analyses identified frameshift and missense mutations as the most frequent variant types in ClinVar database for tooth agenesis (fallea2025dissectingthegenetic pages 4-6).

2. **Susceptibility Loci**: Genome-wide association studies (GWAS) have identified multiple SNPs and susceptibility loci significantly associated with tooth agenesis, including:
   - rs147680216 within WNT10A (strongly linked to premolar agenesis)
   - rs6738629 near GCC2 (implicated in craniofacial morphogenesis)
   - Variants in ADAMTS9, PRICKLE2, BMP7, MSX2, ROBO1/2
   - rs4498834 (ASCL5/CACNA1S), rs35822372 (FOXI3), chr2:108,896,996 (EDAR), rs2034604 (ARHGAP15)
(fallea2025dissectingthegenetic pages 2-4)

3. **Modifier Genes**: While specific modifier genes affecting severity or expression are not extensively detailed in the gathered literature, the variable expressivity and incomplete penetrance observed suggest the presence of genetic modifiers (meade2023toothagenesisan pages 2-3).

**Environmental Risk Factors**:

1. **Chemotherapy and Radiation**: Therapeutic radiation doses of 2000-4000 centigray during treatment for childhood cancers result in dental anomalies often involving agenesis. Increased doses of chemotherapeutic agents (vincristine, cyclophosphamide, doxorubicin) over long treatment periods are associated with increased tooth agenesis (meade2023toothagenesisan pages 3-4).

2. **Maternal Exposures**:
   - Thalidomide use during pregnancy may result in hypodontia in offspring
   - Rubella infection during pregnancy has been proposed as a causative factor
   - Maternal smoking and/or alcohol consumption during pregnancy have been associated with craniofacial anomalies; as hypodontia and some craniofacial anomalies share specific signaling pathways, a correlation is speculated
(meade2023toothagenesisan pages 3-4)

3. **Age and Sex**: Female sex appears to be a risk factor, with females showing higher prevalence (female:male ratio 1.22:1, 95% CI 1.14-1.3) (meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 4-5).

4. **Family History**: Having a first-degree relative with tooth agenesis significantly increases risk, with approximately 37.5% of cases following a familial autosomal dominant inheritance pattern (meade2023toothagenesisan pages 2-3, fallea2025dissectingthegenetic pages 2-4).

### Protective Factors
No specific protective factors (genetic or environmental) that reduce the risk of tooth agenesis are documented in the gathered 2020-2025 literature.

### Gene-Environment Interactions
The etiology is commonly accepted as multifactorial, comprising genetic, epigenetic, and environmental factors working in combination (meade2023toothagenesisan pages 3-4, meade2023toothagenesisan pages 2-3). However, specific gene-environment interaction mechanisms (e.g., how environmental exposures modify effects of specific genotypes) are not extensively detailed in the gathered sources. The observation that maternal smoking correlates with craniofacial anomalies which share signaling pathways with hypodontia suggests potential gene-environment interactions through common developmental pathways (meade2023toothagenesisan pages 3-4).

---

## 3. Phenotypes

### Phenotype Types and Clinical Manifestations

**Primary Phenotype**: The hallmark phenotype is the **congenital absence of one or more teeth**, confirmed by clinical examination and radiographic evaluation showing no tooth development at the expected developmental timepoint (meade2023toothagenesisan pages 1-2).

**Commonly Affected Teeth** (in descending order of prevalence, excluding third molars):
1. Mandibular second premolars (35, 45): 29.9%
2. Maxillary lateral incisors (12, 22): 24.3%
3. Maxillary second premolars (15, 25): 13.7%
4. Mandibular central incisors (31, 41): 6.1%
5. Mandibular lateral incisors (32, 42): 4.3%
(meade2023toothagenesisan pages 2-3)

For deciduous teeth specifically, EDA variants causing deciduous tooth agenesis showed highest missing rates in:
- Mandibular deciduous central incisors: 100%
- Maxillary deciduous lateral incisors: 98.8%
- Mandibular deciduous lateral incisors: 97.7%
(su2024edavariantsare pages 1-2)

**Associated Dental Anomalies** (frequencies among affected individuals):
- **Peg-shaped lateral incisors**: 18-46.7%
- **Retained primary teeth**: up to 60%
- **Microdontia** (smaller crown and root size): 20.6%
- **Taurodontism**: up to 38%
- **Transposition**: 4.7%
- **Delayed dental development**: commonly observed
- **Primary tooth infra-occlusion**: up to 65.7% of individuals with missing second premolars have infra-occlusion of the corresponding primary molar
(meade2023toothagenesisan pages 4-5, meade2023toothagenesisan pages 3-4)

**Craniofacial and Occlusal Features**:
- **Class III malocclusion**: higher prevalence among those with tooth agenesis compared to other malocclusion types
- **Reduced overjet**: progressive reduction with increasing number of missing teeth
- **Increased interincisal angle**: correlates with number of missing teeth
- **Shortened upper and lower dental arch lengths**: correlates with number of missing teeth
- **Midfacial hypoplasia**: especially in cleft-associated cases
- **Transverse constriction of maxilla**, facial divergence, and anterior projection of chin symphysis are associated with dental agenesis
(meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 4-5, fallea2025dissectingthegenetic pages 2-4)

### Phenotype Characteristics

**Age of Symptom Onset**: 
- **Developmental/Congenital**: Tooth agenesis originates during embryonic development, affecting tooth formation at initiation, bud, cap, or bell stages
- **Diagnostic Age**: Diagnosis typically occurs when expected tooth eruption does not happen:
  - Primary teeth: by age 3 years
  - Permanent teeth: by 13-14 years (excluding third molars)
  - Specific teeth have typical eruption windows; failure of a contralateral tooth to erupt within 4-6 months of its antimere indicates likely absence
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Symptom Severity**:
- **Mild** (Hypodontia): 1-5 teeth missing; represents majority of cases (75% have one or two missing teeth)
- **Moderate to Severe** (Oligodontia): 6 or more teeth missing; estimated prevalence 0.08-0.25% in permanent dentition
- **Very Severe** (Anodontia): Complete absence of all teeth; extremely rare
(meade2023toothagenesisan pages 2-3, su2024edavariantsare pages 1-2)

Severity varies significantly with genotype. For example, in a 2024 cohort with EDA variants and deciduous tooth agenesis, patients averaged 15.4 missing deciduous teeth, demonstrating severe oligodontia (su2024edavariantsare pages 1-2).

**Symptom Progression**:
- **Non-progressive**: The number of missing teeth is determined during development and does not change over time (teeth that fail to develop will never develop)
- **Lifelong functional and aesthetic impacts**: persist throughout life, requiring ongoing management
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Frequency Among Affected Individuals**:
- **Non-syndromic tooth agenesis**: most common presentation (approximately 73% of genetic diagnoses)
- **Syndromic tooth agenesis**: approximately 27% of genetic diagnoses
- Among those with missing teeth: 41.9% missing only one tooth, 39.7% missing two, 7.2% missing three, 5.4% missing four, 1.7% missing five, 3.1% missing six or more
(meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 5-7)

### Quality of Life Impact

**Functional Impacts**:
- **Chewing capacity impairment**: especially pronounced after exfoliation of primary teeth without permanent successors
- **Speech difficulties**: particularly in cases with anterior tooth loss or severe oligodontia
- **Mastication problems**: affecting nutrition from childhood in severe deciduous tooth agenesis; may result in delayed growth and development
(meade2023toothagenesisan pages 3-4, su2024edavariantsare pages 1-2)

**Psychosocial Impacts**:
- **Adverse effects on social and emotional well-being**: documented in quality-of-life studies
- **Aesthetic concerns**: particularly impactful when anterior teeth (incisors, canines) are missing in visible areas
- **Psychological disorders**: abnormalities in facial appearance can impact social lives of patients
(meade2023toothagenesisan pages 3-4, su2024edavariantsare pages 1-2)

**Overall Disease Burden**: Tooth agenesis can be associated with significant functional, aesthetic, and psychosocial problems, often requiring multi- and interdisciplinary management throughout life (meade2023toothagenesisan pages 1-2).

### Suggested HPO Terms

Based on the gathered evidence, the following HPO terms are appropriate for annotating tooth agenesis phenotypes:

- **HP:0009804**: Tooth agenesis (general term for absence of teeth)
- **HP:0001592**: Selective tooth agenesis (agenesis specifically affecting one of the classes: incisor, premolar, or molar)
- **HP:0011079**: Impacted tooth (associated phenotype)
- **HP:0200160**: Agenesis of maxillary incisor (specific localization)
- **HP:0000706**: Eruption failure (related developmental tooth phenotype)

Additional relevant HPO terms based on associated phenotypes could include terms for microdontia, peg-shaped teeth, taurodontism, delayed eruption, and malocclusion (fallea2025dissectingthegenetic pages 4-6).

---

## 4. Genetic/Molecular Information

### Causal Genes

A comprehensive table summarizing the major genes associated with tooth agenesis is provided below:

| Gene | HGNC ID | Core function in odontogenesis | Reported inheritance in TA | Syndromic / non-syndromic association | Teeth/patterns most often affected | OMIM-associated condition(s) noted in gathered evidence | Key 2020–2025 references |
|---|---:|---|---|---|---|---|---|
| EDA | HGNC:3157 | Encodes ectodysplasin A, a TNF-family ligand that binds EDAR and activates NF-κB signaling required for ectodermal appendage and tooth development | X-linked; can show variable expressivity | Both; selective tooth agenesis and X-linked hypohidrotic ectodermal dysplasia | Strong anterior pattern; mandibular deciduous central incisors, mandibular lateral incisors, maxillary lateral incisors; average 15.4 missing deciduous teeth in one 2024 cohort | XLHED OMIM #305100; selective tooth agenesis locus on Xq13.1 | Su 2024; Modafferi 2025 (su2024edavariantsare pages 1-2, modafferi2025geneticaspectsof pages 5-7) |
| MSX1 | HGNC:7391 | Homeobox transcription factor; regulator within BMP/Wnt-linked craniofacial and tooth development programs | Usually autosomal dominant | Both; isolated TA plus syndromic/cleft-associated forms | Often isolated tooth deficiencies; classic association with familial oligodontia; pattern not fully specified in gathered passages | Selective tooth agenesis 1 / hypodontia OMIM #106600; orofacial cleft OMIM #608874; Witkop syndrome OMIM #189500; Wolf-Hirschhorn syndrome OMIM #194190 | Meade 2023; Modafferi 2025 (meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7) |
| WNT10A | HGNC:12722 | WNT ligand central to Wnt/β-catenin signaling during epithelial-mesenchymal interactions in tooth morphogenesis | Autosomal dominant and autosomal recessive reported | Both; common cause of isolated hypodontia/oligodontia and ectodermal dysplasia-related disease | Frequently implicated in permanent tooth agenesis; specific tooth pattern not detailed in gathered passages | Odonto-onycho-dermal dysplasia / ectodermal dysplasia 16; Schöpf-Schulz-Passarge syndrome | Modafferi 2025; Raju 2024; Song 2023 (modafferi2025geneticaspectsof pages 5-7, fallea2025dissectingthegenetic pages 2-4) |
| PAX9 | HGNC:8616 | Paired-box transcription factor active in dental mesenchyme; disturbances can arrest development at bud stage | Autosomal dominant | Primarily non-syndromic in gathered evidence | Strong association with missing molars; also represented among severe deciduous TA cases | Selective tooth agenesis 3 | Meade 2023; Su 2024; Modafferi 2025 (meade2023toothagenesisan pages 3-4, su2024edavariantsare pages 1-2, modafferi2025geneticaspectsof pages 5-7) |
| AXIN2 | HGNC:904 | Negative regulator/scaffold in Wnt signaling pathway | Often autosomal dominant in familial TA literature; inheritance not explicitly detailed in gathered excerpts | Primarily non-syndromic but clinically important systemic association | Lower incisor agenesis and some oligodontia forms | Tooth agenesis with colorectal cancer susceptibility association noted; specific OMIM not provided in gathered passages | Meade 2023; Fallea 2025 (meade2023toothagenesisan pages 3-4, fallea2025dissectingthegenetic pages 1-2) |
| LRP6 | HGNC:6698 | Wnt co-receptor required for effective Wnt pathway activation in tooth development | Autosomal dominant | Both; selective TA and systemic coronary artery disease association | Included among major TA genes; specific tooth pattern not detailed in gathered passages | Selective tooth agenesis; coronary artery disease, autosomal dominant | Modafferi 2025; Fallea 2025 (modafferi2025geneticaspectsof pages 5-7, fallea2025dissectingthegenetic pages 1-2) |
| PITX2 | HGNC:9004 | Paired-like homeodomain transcription factor involved in craniofacial patterning and tooth morphogenesis | Autosomal dominant | Both; tooth-size/tooth-number anomalies and Axenfeld-Rieger spectrum | Variation in tooth dimensions; can appear in deciduous TA | Axenfeld-Rieger syndrome type 1; ring dermoid of cornea | Modafferi 2025; Su 2024 (modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2) |
| TSPEAR | HGNC:26961 | Protein implicated in ectodermal development; recurrently linked to oligodontia/ectodermal dysplasia phenotypes | Often biallelic / autosomal recessive in reported ectodermal dysplasia cases | Both, but strong syndromic overlap with ectodermal dysplasia | Non-syndromic oligodontia reported; exact tooth pattern not specified in gathered passages | Tooth agenesis selective 10; ectodermal dysplasia-related phenotypes | Modafferi 2025; Bowles 2021 (modafferi2025geneticaspectsof pages 5-7) |
| GREM2 | HGNC:16008 | BMP antagonist (DAN family) modulating developmental signaling balance in odontogenesis | Autosomal dominant | Non-syndromic selective TA in gathered evidence | Specific tooth pattern not detailed in gathered passages | Selective tooth agenesis 9 | Modafferi 2025; Fallea 2025 (modafferi2025geneticaspectsof pages 5-7, fallea2025dissectingthegenetic pages 2-4) |
| BMP4 | HGNC:1071 | BMP ligand in developmental signaling networks controlling tooth morphogenesis | Not specified in gathered passages | Both candidate/causal roles reported | Rarely represented in severe deciduous TA cohort; specific tooth pattern not detailed | Not specified in gathered passages | Su 2024; BMP pathway reviews 2023 (su2024edavariantsare pages 1-2, fallea2025dissectingthegenetic pages 2-4) |
| EDAR | HGNC:2895 | Receptor for EDA; activates downstream NF-κB signaling essential for ectodermal appendage development | Can contribute in ectodermal/EDA-pathway TA; inheritance not specified in gathered excerpts | Both, especially syndromic ectodermal dysplasia spectrum | Specific tooth pattern not detailed in gathered passages | Ectodysplasin/EDAR pathway-associated TA and ectodermal dysplasia | Fallea 2025; Su 2024 (fallea2025dissectingthegenetic pages 1-2, su2024edavariantsare pages 1-2) |
| EDARADD | HGNC:2897 | EDAR-associated death domain adaptor; transduces EDA–EDAR signaling to NF-κB | Inheritance not specified in gathered passages | Both, mainly ectodermal dysplasia/TA pathway gene | Rare cause in deciduous TA cohort; specific tooth pattern not detailed | EDA-pathway ectodermal dysplasia / tooth agenesis association | Fallea 2025; Su 2024 (fallea2025dissectingthegenetic pages 1-2, su2024edavariantsare pages 1-2) |
| KREMEN1 | HGNC:21241 | Kringle-domain transmembrane protein that modulates Wnt signaling | Autosomal recessive | Both; hair/tooth ectodermal dysplasia phenotype emphasized | Specific tooth pattern not detailed in gathered passages | Ectodermal dysplasia 13, hair/tooth type | Modafferi 2025 (modafferi2025geneticaspectsof pages 5-7) |
| SMOC2 | HGNC:11186 | SPARC-related modular calcium-binding extracellular protein involved in craniofacial/dental matrix biology | Autosomal recessive | Syndromic/complex dental phenotype and non-isolated severe dental anomaly | Associated with microdontia and misshapen teeth in addition to reduced tooth number | Dentin dysplasia type I with microdontia and misshapen teeth | Modafferi 2025; Fallea 2025 (modafferi2025geneticaspectsof pages 5-7, fallea2025dissectingthegenetic pages 2-4) |


*Table: This table summarizes the principal genes implicated in tooth agenesis, integrating gene function, inheritance, clinical context, and characteristic dental patterns from the gathered 2020–2025 literature. It is useful for building disease knowledge-base entries and for prioritizing diagnostic genes in syndromic and non-syndromic cases.*

The genes most frequently implicated in tooth agenesis are **MSX1**, **EDA**, and **PAX9** (fallea2025dissectingthegenetic pages 1-2). However, the genetic landscape is heterogeneous, involving at least 14 major genes and numerous additional candidates identified through whole-exome sequencing studies (modafferi2025geneticaspectsof pages 1-2, modafferi2025geneticaspectsof pages 5-7).

**Gene-Specific Highlights**:

1. **EDA (Ectodysplasin A)**: Accounts for approximately 86.9% of deciduous tooth agenesis cases and is a major contributor to X-linked hypohidrotic ectodermal dysplasia (su2024edavariantsare pages 1-2). Located on chromosome Xq12-q13.1, EDA encodes a 391 amino acid TNF-family protein with transmembrane, furin cleavage, collagen, and TNF homologous domains critical for tooth development (su2024edavariantsare pages 1-2).

2. **MSX1 (Muscle Segment Homeobox 1)**: The first gene identified in non-syndromic tooth agenesis in humans. Encodes a transcriptional repressor involved in both Wnt and BMP4 pathways. In one study, 62.02% of patients with MSX1 pathogenic variants presented with isolated tooth agenesis, 21.25% with oral clefts, 10% with Witkop syndrome, and 6.25% with Wolf-Hirschhorn syndrome (modafferi2025geneticaspectsof pages 5-7).

3. **WNT10A**: Pathogenic variants are the most frequent genetic cause of isolated hypodontia and oligodontia, mostly with autosomal recessive inheritance. This gene family is essential for regulating growth processes in orofacial tissues and dental development (modafferi2025geneticaspectsof pages 5-7).

4. **PAX9 (Paired Box Gene 9)**: Codes for transcription factors in tooth mesenchyme; disturbances abort development at the bud stage and are strongly associated with missing molars (meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2).

### Pathogenic Variants

**Variant Classification**: 
According to ClinVar database analysis for tooth agenesis, 401 germline genetic variants are classified as likely pathogenic or pathogenic. The most frequent variant types include:
- Frameshift mutations
- Missense mutations
(fallea2025dissectingthegenetic pages 4-6)

**Specific Examples of Pathogenic Variants** (from 2020-2025 literature):

*EDA variants*:
- 54 different variants identified in 8 genes across 84 patients with severe deciduous tooth agenesis
- Variable phenotypes ranging from selective tooth agenesis to severe oligodontia even within genotype (homozygotes and heterozygotes showing variable presentations)
- Average of 12.6 missing teeth across 23 cases with EDA pathogenic variants
(su2024edavariantsare pages 1-2)

*WNT10A variants*:
- Novel variant A135S identified in congenital tooth agenesis whole-exome sequencing study
- Recurrent WNT10A variants rs121908120 and rs121908119 identified in GWAS
(fallea2025dissectingthegenetic pages 2-4)

*TSPEAR variants*:
- Compound heterozygous variants (L219P, I419Lfs*150) identified
- Biallelic loss-of-function variants primarily associated with ectodermal dysplasia and tooth agenesis
(su2024edavariantsare pages 1-2)

*LRP6 variants*:
- Three extremely rare variants identified: c.4154A>G (p.Asn1385Ser), c.3940G>A (p.Gly1314Ser), c.448G>A (p.Asp150Asn)
(fallea2025dissectingthegenetic pages 2-4)

**Allele Frequency**: Specific population allele frequencies for tooth agenesis-associated variants are not extensively detailed in the gathered literature, though variants are described as "rare" or "extremely rare" in population databases.

**Somatic vs. Germline**: The variants causing tooth agenesis are **germline** (constitutional) mutations affecting development (fallea2025dissectingthegenetic pages 4-6).

**Functional Consequences**:
- **Loss of function**: Most common consequence; tooth development arrest
- **Gain of function**: Not prominently reported in gathered literature
- **Dominant negative**: Potential mechanism for some variants, though not extensively detailed
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7)

### Modifier Genes

While specific modifier genes are not extensively characterized in the gathered literature, the observed variable expressivity and incomplete penetrance suggest the presence of genetic modifiers influencing phenotypic severity (meade2023toothagenesisan pages 2-3, fallea2025dissectingthegenetic pages 2-4).

### Epigenetic Information

DNA methylation, histone modifications, and chromatin changes affecting tooth agenesis are recognized as part of the multifactorial etiology but are not extensively detailed with specific mechanisms in the gathered 2020-2025 literature (fallea2025dissectingthegenetic pages 1-2, meade2023toothagenesisan pages 3-4).

### Chromosomal Abnormalities

**Large-Scale Genetic Changes**:
Chromosomal abnormalities contribute significantly to tooth agenesis etiology, including:

1. **Aneuploidy**:
   - **Down syndrome (Trisomy 21)**: Estimated total prevalence of permanent tooth agenesis in Down syndrome (excluding third molars) is 54.6%, with important heterogeneity across studies (meade2023toothagenesisan pages 3-4)
   - **Williams syndrome**: Associated with tooth agenesis (fallea2025dissectingthegenetic pages 1-2)

2. **Structural Variations**:
   - Deletions and duplications contribute to tooth agenesis etiology
   - Copy number variations affecting developmental gene dosage
(fallea2025dissectingthegenetic pages 1-2)

---

## 5. Environmental Information

### Environmental Factors

**Toxins and Radiation**:
- **Therapeutic radiation**: Doses of 2000-4000 centigray during treatment for childhood cancers cause dental anomalies often involving agenesis
- **Chemotherapy**: Increased doses of vincristine, cyclophosphamide, and doxorubicin over long treatment periods associated with increased tooth agenesis
(meade2023toothagenesisan pages 3-4)

**Pollution and Occupational Exposure**: Not specifically documented in the gathered literature as risk factors for tooth agenesis.

### Lifestyle Factors

**Maternal Behaviors**:
- **Smoking**: Maternal smoking during pregnancy associated with craniofacial anomalies; correlation with hypodontia speculated due to shared signaling pathways
- **Alcohol consumption**: Maternal alcohol consumption during pregnancy associated with craniofacial anomalies
(meade2023toothagenesisan pages 3-4)

**Diet, Exercise**: Not specifically implicated as risk factors in gathered literature.

### Infectious Agents

**Maternal Rubella**: Rubella infection during pregnancy has been proposed as a causative factor of hypodontia in newborns (meade2023toothagenesisan pages 3-4).

No bacterial, fungal, or parasitic causes of tooth agenesis are documented in the gathered literature.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The molecular mechanisms underlying tooth agenesis involve disruption of multiple interconnected signaling pathways essential for odontogenesis:

**1. Wnt/β-Catenin Signaling Pathway**:
- **Key components**: WNT10A (ligand), LRP6 (co-receptor), AXIN2 (negative regulator/scaffold), DKK1 and SOST (modulators)
- **Function**: Central to epithelial-mesenchymal interactions during tooth morphogenesis; controls tooth initiation, patterning, and differentiation
- **Disruption effects**: Mutations in AXIN2 disrupt Wnt pathway regulation, making tooth development unlikely to occur. WNT10A is the most frequent genetic cause of isolated hypodontia/oligodontia. LRP6 mutations compromise pathway activation
(meade2023toothagenesisan pages 3-4, fallea2025dissectingthegenetic pages 2-4, modafferi2025geneticaspectsof pages 5-7)

**2. TNF Receptor Binding / EDA-EDAR-EDARADD-NF-κB Pathway**:
- **Key components**: EDA (ligand), EDAR (receptor), EDARADD (adaptor), NF-κB (transcription factor)
- **Function**: Essential for ectodermal appendage development including teeth; EDA binds EDAR, activating NF-κB signaling
- **Disruption effects**: EDA pathway variants account for 86.9% of deciduous tooth agenesis and cause X-linked hypohidrotic ectodermal dysplasia
(fallea2025dissectingthegenetic pages 1-2, su2024edavariantsare pages 1-2)

**3. mTOR Signaling Pathway**:
- **Key components**: AXIN2, FGFR1, LRP6, WNT10A, WNT10B
- **Function**: Regulates cell growth, proliferation, and differentiation during tooth development
(fallea2025dissectingthegenetic pages 1-2)

**4. BMP Signaling Pathway**:
- **Key components**: BMP4 (ligand), GREM2 (BMP antagonist), BMP receptors, SMAD proteins
- **Function**: Critical for odontoblast differentiation, epithelial-mesenchymal interactions, and dental patterning; MSX1 is involved in BMP4 pathway
- **Disruption effects**: Dysregulated BMP signaling disrupts odontogenic specification and arrests development
(fallea2025dissectingthegenetic pages 2-4, modafferi2025geneticaspectsof pages 5-7)

**5. SHH (Sonic Hedgehog) Signaling**:
- **Function**: Mediates craniofacial and tooth development; interacts with BMP and FGF8 signaling pathways
- **Expression**: Primarily expressed in dental epithelium from initiation to root formation stages
(fallea2025dissectingthegenetic pages 2-4)

**6. FGF (Fibroblast Growth Factor) Signaling**:
- **Function**: Regulates epithelial-mesenchymal interactions during tooth morphogenesis
- **Interactions**: Forms regulatory networks with SHH, BMP, and Wnt pathways
(fallea2025dissectingthegenetic pages 2-4)

### Cellular Processes

**1. Epithelial-Mesenchymal Interactions**:
- Reciprocal signaling between dental epithelium and dental mesenchyme is fundamental to tooth development
- Wnt, BMP, FGF, and SHH pathways mediate these interactions
- Disruption arrests development at specific stages
(meade2023toothagenesisan pages 3-4, fallea2025dissectingthegenetic pages 2-4)

**2. Dental Lamina Development**:
- Tooth development initiates from dental lamina in the embryonic oral epithelium
- Developmental arrest can occur at initiation, bud, cap, or bell stages
- PAX9 disturbances specifically abort development at bud stage
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7)

**3. Odontoblast and Ameloblast Differentiation**:
- Dental mesenchymal stem cells differentiate into odontoblasts (dentin-forming cells)
- Dental epithelial cells differentiate into ameloblasts (enamel-forming cells)
- Gli1+ cells in dental tissues demonstrate stem cell properties including multipotency and self-renewal
- Wnt3a specifically induces NKD1+ subpopulation with secretory odontoblast characteristics through NKD1-MSX1 axis
(fallea2025dissectingthegenetic pages 2-4)

**4. Cell Adhesion and Matrix Formation**:
- Impairment of molecules facilitating cell adhesion contributes to agenesis
- Malfunctioning of extracellular matrix molecules disrupts tissue organization
(meade2023toothagenesisan pages 3-4)

### Protein Dysfunction

**1. Transcription Factor Abnormalities**:
- **MSX1**: Transcriptional repressor; mutations impair dental patterning and BMP/Wnt pathway regulation
- **PAX9**: Paired-box transcription factor active in dental mesenchyme; mutations arrest development at bud stage
- **PITX2**: Paired-like homeodomain transcription factor; mutations affect craniofacial patterning and tooth morphogenesis
- **MSX1 nuclear translocation defects**: Impaired nuclear translocation of MSX1 is a known cause of tooth agenesis
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7)

**2. Receptor and Ligand Dysfunction**:
- **EDA protein domains**: Transmembrane (TM), furin cleavage, collagen, and TNF homologous domains are hot spots for agenesis-causing variants. Proper multimerization and EDAR binding depend on intact domain structure
- **LRP6 dysfunction**: Compromises Wnt pathway co-receptor activation
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

### Metabolic Changes

Specific alterations in energy metabolism, lipid metabolism, or amino acid metabolism as primary mechanisms of tooth agenesis are not detailed in the gathered 2020-2025 literature.

### Immune System Involvement

Tooth agenesis is primarily a developmental disorder, and immune system involvement is not a primary pathogenic mechanism in the gathered literature.

### Tissue Damage Mechanisms

**Developmental Arrest** rather than tissue damage is the primary mechanism. Specific stages of arrest:
- **Initiation stage**: Failure of dental lamina to form tooth buds
- **Bud stage**: PAX9 disruption specifically arrests at this stage
- **Cap and bell stages**: Later arrests can occur depending on affected pathway
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 5-7)

### Biochemical Abnormalities

**Enzyme and Receptor Deficiencies**:
While not extensively detailed as enzyme deficiencies, the condition involves:
- Disrupted signaling transduction (EDA-EDAR-EDARADD pathway, Wnt pathway)
- Transcription factor dysfunction (MSX1, PAX9, PITX2)
- Receptor dysfunction (EDAR, LRP6)
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

### Molecular Profiling

**Transcriptomics/Gene Expression**:
- Wnt signaling pathway gene expression profiles during early tooth development show stage-specific patterns
- WNT10A expression shifts from dental epithelium to mesenchyme during development (E15.5)
- SOST and DKK1 expression enriched in dental mesenchyme
- Single-cell transcriptomic profiling identified distinct NKD1+ subpopulation with odontoblast characteristics induced by Wnt3a
(fallea2025dissectingthegenetic pages 2-4)

**Functional Genomics**:
- SCENIC analysis identified MSX1 as key transcription factor regulating NKD1+ lineage specification
- CUT&Tag analysis demonstrated MSX1 occupancy at promoters of odontogenic regulators
(fallea2025dissectingthegenetic pages 2-4)

### Suggested Ontology Terms

**GO Biological Processes**:
- GO:0042476 (odontogenesis)
- GO:0060562 (epithelial tube morphogenesis)
- GO:0001944 (vasculature development)
- GO:0030513 (positive regulation of BMP signaling pathway)
- GO:0016055 (Wnt signaling pathway)

**CL Cell Types**:
- CL:0000065 (ectoderm-derived cell)
- CL:0000066 (epithelial cell)
- CL:0000222 (mesodermal cell)
- CL:0000449 (mesenchymal stem cell)
- CL:0000060 (odontoblast)
- CL:0000067 (ameloblast)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs Directly Affected**:
- **Teeth** (UBERON:0001091): The primary affected organs, with developmental absence
- **Alveolar bone**: Secondary underdevelopment and atrophy due to lack of tooth development
- **Maxilla** and **Mandible**: Growth and development can be affected, particularly in severe oligodontia

**Body Systems Involved**:
- **Digestive system** (oral cavity component): Primary site of manifestation
- **Craniofacial complex**: Structural development affected in syndromic and severe non-syndromic forms
(meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 4-5, su2024edavariantsare pages 1-2)

### Tissue and Cell Level

**Specific Tissue Types Affected**:
- **Dental epithelium**: Site of Wnt10a expression and ameloblast differentiation
- **Dental mesenchyme**: Site of PAX9 expression and odontoblast differentiation
- **Dental lamina**: Primordial tissue from which teeth develop
- **Enamel organ**: Epithelial structure forming enamel

**Specific Cell Populations Targeted**:
- **Dental epithelial cells**: Express WNT10A, undergo ameloblast differentiation
- **Dental mesenchymal stem cells/progenitors**: Differentiate into odontoblasts
- **Odontoblasts** (CL:0000060): Dentin-forming cells; NKD1+ subpopulation identified
- **Ameloblasts** (CL:0000067): Enamel-forming cells; show robust Wnt10a expression at developing cusp tip
- **Gli1-positive cells**: Demonstrate stem cell properties including multipotency and self-renewal
(fallea2025dissectingthegenetic pages 2-4)

### Subcellular Level

**Cellular Compartments Involved**:
- **Membrane** (GO:0016020): EDA transmembrane domains critical for signaling
- **Nucleus** (GO:0005634): Transcription factors MSX1, PAX9, PITX2 function in nucleus; MSX1 nuclear translocation required
- **Extracellular matrix** (GO:0031012): SMOC2 and other matrix proteins involved
- **Extracellular space** (GO:0005615): EDA ligand, Wnt ligands, BMP ligands secreted

### Localization

**Specific Anatomical Sites** (with UBERON terms where applicable):
- **Maxilla** (UBERON:0002397): Maxillary lateral incisors (24.3% of all agenesis), maxillary second premolars (13.7%)
- **Mandible** (UBERON:0001684): Mandibular second premolars (29.9% of all agenesis - most common), mandibular central incisors (6.1%), mandibular lateral incisors (4.3%)
- **Deciduous dentition**: Mandibular deciduous central incisors, maxillary/mandibular deciduous lateral incisors preferentially affected in EDA-related cases
(meade2023toothagenesisan pages 2-3, su2024edavariantsare pages 1-2)

**Lateralization**:
- **Bilateral**: More common than unilateral (83.3% bilateral in one study)
- **Unilateral**: Less frequent
- **Left side**: In cleft-associated tooth agenesis, left-side involvement more common; in general population, lateralization patterns vary by tooth type
(modafferi2025geneticaspectsof pages 4-5, fallea2025dissectingthegenetic pages 2-4)

---

## 8. Temporal Development

### Onset

**Typical Age of Onset**:
- **Developmental/Congenital**: The condition originates during embryonic development when tooth germs are forming (intrauterine period)
- **Diagnostic age**: Clinical diagnosis typically occurs at expected eruption times:
  - Primary dentition: diagnosed by age 3 years when primary teeth should have erupted
  - Permanent dentition: diagnosed from approximately age 6-14 years as permanent teeth are expected to erupt (all permanent teeth except third molars should erupt by 13-14 years)
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Onset Pattern**:
- **Developmental defect**: The absence of tooth development is determined during embryogenesis and early fetal development
- **Clinical manifestation**: Becomes apparent when expected tooth eruption does not occur
- **Detection**: Often first detected by failure of contralateral tooth to erupt within 4-6 months of its antimere
(meade2023toothagenesisan pages 1-2)

### Progression

**Disease Stages**:
Tooth agenesis does not have traditional disease stages of progression, but can be characterized by:
- **Severity stages**: Hypodontia (1-5 teeth) → Oligodontia (≥6 teeth) → Anodontia (all teeth)
- **Developmental arrest stage**: Can occur at initiation, bud, cap, or bell stages of tooth development
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 2-4)

**Progression Rate**:
- **Non-progressive**: The number and location of missing teeth is determined during development and does not change over time
- **Static condition**: Teeth that fail to develop will never develop; no worsening of the primary defect occurs
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Disease Course Pattern**:
- **Stable/Non-progressive**: Primary developmental defect is stable
- **Lifelong impact**: Functional and aesthetic consequences persist throughout life and may require ongoing management
- **Secondary complications**: Can develop over time (malocclusion, bone atrophy, TMD) but these are consequences rather than progression of the primary defect
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 3-4)

**Disease Duration**:
- **Chronic lifelong condition**: Effects persist throughout life, requiring long-term multidisciplinary management
(meade2023toothagenesisan pages 1-2, su2024edavariantsare pages 1-2)

### Patterns

**Critical Periods**:
- **Embryonic tooth development stages**: Initiation (6-7 weeks), bud (8 weeks), cap (9-10 weeks), bell (11-12 weeks for primary teeth; later for permanent teeth)
- **Vulnerable developmental windows**: Disruption during specific stages leads to agenesis
- **Growth periods**: Timing of interventions is critical during active growth phases (mixed dentition, adolescent growth spurt) for optimal orthodontic and prosthodontic outcomes
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 4-5)

**Remission Patterns**: Not applicable - tooth agenesis is a developmental defect with permanent absence of affected teeth.

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence**:
- **Overall permanent dentition (excluding third molars)**: 6.4% (95% CI: 5.7-7.2%)
- **Range**: 0.4% to 36.4% depending on population and geographic location
- **Primary dentition**: 0.4% to 2.4%
- **Oligodontia (≥6 teeth)**: 0.08% to 0.25%
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3, su2024edavariantsare pages 1-2)

**Geographic Distribution**:
- **Africa**: 13.4%
- **Europe**: 7%
- **Australia**: 6.3% (Caucasian population)
- **North America**: 5.0%
- **Latin America**: 4.4%
- **Asia**: 8.5-10.8% (varies by study and population)
- **Japan**: 3.8-10.8% (variability across studies; recent large survey suggests 3.8%)
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 4-5)

**Incidence**: Specific incidence data (new cases per 100,000 per year) are not provided in the gathered literature, as tooth agenesis is a congenital condition typically measured by prevalence.

### For Genetic Etiology

**Inheritance Pattern**:
- **Autosomal Dominant**: Approximately 37.5% of cases follow familial autosomal dominant pattern with variable expressivity and penetrance (meade2023toothagenesisan pages 2-3, fallea2025dissectingthegenetic pages 2-4)
- **Autosomal Recessive**: Particularly for WNT10A (most frequent cause of isolated hypodontia/oligodontia), TSPEAR, KREMEN1, SMOC2 (modafferi2025geneticaspectsof pages 5-7)
- **X-linked**: EDA gene (Xq12-q13.1) causes X-linked hypohidrotic ectodermal dysplasia and selective tooth agenesis (modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)
- **Multifactorial/Polygenic**: Many cases show complex inheritance involving multiple genes and environmental factors (fallea2025dissectingthegenetic pages 1-2, fallea2025dissectingthegenetic pages 2-4)

**Penetrance**:
- **Incomplete/Variable**: Common observation across multiple genes
- **Age-dependent**: May appear age-dependent as manifestation is at expected eruption times
- **Gene-specific variation**: Different genes show different penetrance patterns
(meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 5-7)

**Expressivity**:
- **Highly variable**: Even within families carrying the same mutation, number and pattern of missing teeth can vary significantly
- **Sex-influenced**: EDA heterozygous females may show mild phenotypes or be unaffected, while hemizygous males are typically more severely affected
- **Example**: In one EDA cohort, two heterozygotes showed no or only one missing tooth, while two homozygotes had similarly mild presentations, but a third homozygous patient showed severe oligodontia with 15 missing permanent teeth
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

**Genetic Anticipation**: Not documented as a feature of tooth agenesis in the gathered literature (would require repeat expansion disorders).

**Germline Mosaicism**: Not specifically detailed in the gathered 2020-2025 literature.

**Founder Effects**:
While specific founder mutations are not extensively detailed in the gathered literature, population-specific patterns suggest potential founder effects may exist.

**Consanguinity Role**:
- Likely increases risk for autosomal recessive forms (WNT10A, TSPEAR, KREMEN1, SMOC2)
- Not extensively quantified in gathered literature
(modafferi2025geneticaspectsof pages 5-7)

**Carrier Frequency**:
Specific carrier frequencies for tooth agenesis alleles in general populations are not provided in the gathered 2020-2025 literature.

### Population Demographics

**Affected Populations**:
- **Ethnic/demographic variation**: 
  - Higher prevalence in some Asian populations (8.5-10.8%) and African populations (13.4%)
  - Lower in Latin American populations (4.4%)
  - Intermediate in European (7%) and North American (5.0%) populations
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Sex Ratio**:
- **Female:Male = 1.22:1 (95% CI: 1.14-1.3)**: Females more commonly affected overall
- **Gender-specific patterns**: Maxillary left lateral incisor agenesis more common in males (p=0.019), while mandibular right lateral incisor and bilateral mandibular lateral incisor agenesis more common in females
- **Primary dentition**: No gender-related differences reported
(meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 4-5, fallea2025dissectingthegenetic pages 2-4)

**Age Distribution**:
As a congenital condition, all affected individuals are affected from birth, though clinical manifestation occurs at expected eruption ages (early childhood for primary teeth, childhood/adolescence for permanent teeth) (meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests**: 
Standard laboratory chemistry tests (blood, urine) are not primary diagnostic methods for tooth agenesis, which is primarily a clinical and radiographic diagnosis.

**Biomarkers**: 
Specific circulating protein or metabolite biomarkers for diagnosing tooth agenesis are not documented in the gathered 2020-2025 literature. The condition is diagnosed through clinical and imaging evaluation.

**Imaging Studies**:
- **Panoramic radiograph (OPG/orthopantomogram)**: Primary imaging modality to visualize presence/absence of tooth buds and developing teeth
- **Cone Beam Computed Tomography (CBCT)**: Provides three-dimensional assessment of tooth development and alveolar bone
- **Periapical radiographs**: Can supplement panoramic imaging for specific areas
(meade2023toothagenesisan pages 1-2)

**Functional Tests**: Not applicable for primary diagnosis of tooth agenesis.

**Electrophysiology**: Not applicable.

**Biopsy Findings**: Not required or applicable for tooth agenesis diagnosis.

**Pathology Findings**: Tooth agenesis is characterized by **developmental absence** rather than pathological tissue changes. Histologically, no tooth germ develops at the affected site.

### Genetic Testing

**Overview**:
Genetic testing is increasingly important for:
- Confirming diagnosis, especially in familial cases
- Distinguishing syndromic from non-syndromic forms
- Guiding genetic counseling and family planning
- Predicting patterns of missing teeth based on genotype
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

**Whole Genome Sequencing (WGS)**:
- Utility: Can identify both coding and non-coding variants, structural variations
- Application: Research setting; comprehensive analysis
(fallea2025dissectingthegenetic pages 2-4)

**Whole Exome Sequencing (WES)**:
- Utility: Identifies variants in protein-coding regions (exome)
- Application: Used successfully in recent cohort studies to identify novel and known variants in EDA, WNT10A, PAX9, TSPEAR
- Success rate: Variable; can identify causal variants when panel testing is negative
- Example: WES used in 84 patients with severe deciduous tooth agenesis, identifying variants in 8 genes
(su2024edavariantsare pages 1-2)

**Gene Panels**:
- **GenoDENT panel**: 567 genes; achieved 60% diagnostic rate for dental anomalies (including amelogenesis imperfecta, which shares gene panel utility)
- **Recommended panel genes for tooth agenesis**: EDA, MSX1, WNT10A, PAX9, AXIN2, LRP6, PITX2, TSPEAR, GREM2, BMP4, EDAR, EDARADD, KREMEN1, SMOC2, and others
- **Utility**: Cost-efficient, validated technique offering targeted analysis of known causal genes
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

**Single Gene Testing**:
- **Application**: When specific gene suspected based on phenotype (e.g., EDA for deciduous agenesis, PAX9 for molar agenesis, MSX1 for familial oligodontia)
- **Method**: Typically Sanger sequencing for variant confirmation
(su2024edavariantsare pages 1-2)

**Chromosomal Microarray (CMA)**:
- **Utility**: Can detect deletions, duplications, and copy number variations
- **Application**: Relevant when structural chromosomal abnormalities suspected (Down syndrome, Williams syndrome associations)
(fallea2025dissectingthegenetic pages 1-2)

**Karyotyping**:
- **Utility**: Identifies large chromosomal abnormalities (aneuploidy, translocations)
- **Application**: When syndromic presentation suggests chromosomal disorder
(fallea2025dissectingthegenetic pages 1-2)

**FISH (Fluorescence In Situ Hybridization)**: 
Can be used for specific locus analysis but not primary diagnostic approach for tooth agenesis.

**Mitochondrial DNA Testing**: 
Not a primary method for tooth agenesis diagnosis (nuclear genes implicated).

**Repeat Expansion Testing**: 
Not applicable - tooth agenesis not associated with repeat expansion disorders.

### Clinical Criteria

**Standardized Diagnostic Criteria**:
- **Clinical definition**: Tooth suspected of being developmentally absent if it has not erupted into the mouth AND is not evident on radiograph at an expected timepoint
- **Radiographic confirmation required**: Definitive diagnosis determined by radiographic evaluation
- **Timing considerations**: All primary teeth should have erupted by 3 years; all permanent teeth (except third molars) by 13-14 years
- **Contralateral comparison**: Failure of contralateral tooth to erupt within 4-6 months of its antimere indicates likely absence
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 2-3)

**Differential Diagnosis**:
- **Delayed eruption**: Distinguish from true agenesis; chronological development can vary widely (e.g., second premolars can commence development as late as 9-10 years)
- **Impaction**: Tooth developed but cannot erupt due to physical impediment
- **Ankylosis**: Primary tooth fails to exfoliate due to fusion with alveolar bone
- **Extraction/trauma**: Acquired tooth loss vs. congenital absence
- **Ectopic eruption**: Tooth developed but erupted in abnormal position
(meade2023toothagenesisan pages 1-2, fallea2025dissectingthegenetic pages 4-6)

### Screening

**Screening for Asymptomatic Individuals**:
- **Family members of affected individuals**: Recommended clinical and radiographic screening, especially in familial/autosomal dominant cases
- **Cascade screening**: Genetic testing of relatives when causative variant identified in proband
- **Prenatal testing**: Available for familial cases with known pathogenic variant
- **Carrier screening**: Relevant for X-linked EDA variants and autosomal recessive forms
(modafferi2025geneticaspectsof pages 5-7)

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Life Expectancy**:
Tooth agenesis itself is not a life-threatening condition and does not directly affect life expectancy. However, in severe syndromic forms (e.g., ectodermal dysplasia), associated systemic features may impact overall health (meade2023toothagenesisan pages 1-2, su2024edavariantsare pages 1-2).

**Mortality Rate**: 
Tooth agenesis is not associated with increased mortality.

**Disease-Specific Mortality**: 
None - this is not a life-threatening condition.

### Morbidity and Function

**Morbidity**:
Significant disease-related disability and health impacts include:
- **Functional impairment**: Chewing, mastication, speech
- **Aesthetic concerns**: Particularly with anterior tooth absence
- **Psychosocial morbidity**: Impact on social and emotional well-being
- **Nutritional impact**: In severe cases affecting multiple teeth from early childhood
(meade2023toothagenesisan pages 3-4, su2024edavariantsare pages 1-2)

**Disability Outcomes**:
Long-term functional impairments:
- **Mastication inefficiency**: Lifelong if untreated
- **Speech articulation difficulties**: Especially with anterior tooth loss
- **Occlusal dysfunction**: Related to malocclusion development
- **TMD (Temporomandibular Disorders)**: Higher prevalence in those with posterior tooth loss in multiple quadrants
(meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 4-5)

**Quality of Life Measures**:
- Studies using hypodontia-specific quality of life tools found that presentation and planned treatment of hypodontia adversely impacted social and emotional well-being
- Chewing capacity impairment noted especially after primary tooth exfoliation when no permanent successors develop
- Aesthetic concerns in visible anterior regions significantly impact quality of life
(meade2023toothagenesisan pages 3-4)

### Disease Course

**Complications**:
- **Malocclusion**: Especially Class III malocclusion; higher prevalence than in general population
- **Alveolar bone underdevelopment/atrophy**: Lack of tooth development leads to insufficient alveolar bone development; progressive atrophy in edentulous areas
- **Temporomandibular disorders (TMD)**: Higher risk in patients with posterior tooth loss
- **Speech difficulties**: Particularly with anterior tooth gaps
- **Delayed growth and development**: In severe deciduous tooth agenesis affecting masticatory function from infancy
- **Infra-occlusion of primary teeth**: Up to 65.7% of individuals with missing second premolars have infra-occlusion of the corresponding primary molar
- **Occlusal changes**: Reduced overjet, increased interincisal angle, shortened dental arch lengths
(meade2023toothagenesisan pages 4-5, meade2023toothagenesisan pages 3-4, modafferi2025geneticaspectsof pages 4-5)

**Recovery Potential**:
- **No spontaneous recovery**: Teeth that fail to develop will never develop
- **Treatment-dependent improvement**: Functional and aesthetic outcomes depend entirely on prosthetic, orthodontic, and surgical interventions
- **Prognosis with treatment**: Generally good functional outcomes achievable with multidisciplinary care
(meade2023toothagenesisan pages 1-2)

### Prediction

**Prognostic Factors**:
- **Number of missing teeth**: More missing teeth → greater functional impact and treatment complexity
- **Location of missing teeth**: Anterior vs. posterior; aesthetic vs. functional primary concerns
- **Syndromic vs. non-syndromic**: Syndromic forms may have additional health complications
- **Age at diagnosis and treatment initiation**: Early diagnosis facilitates timely intervention during growth, enhancing long-term outcomes
- **Patient age and growth status**: Treatment timing relative to growth critical for optimal orthodontic/prosthetic outcomes
(meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 1-2, meade2023toothagenesisan pages 4-5)

**Prognostic Biomarkers**:
- **Genotype**: Specific genes and variants can predict pattern and severity of missing teeth
  - EDA variants → severe deciduous agenesis, anterior pattern
  - PAX9 variants → molar agenesis
  - WNT10A variants → common cause of oligodontia
- **Family history**: Familial cases suggest higher risk of additional affected family members
(modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

---

## 12. Treatment

### Pharmacotherapy

**Pharmacological Treatments**: 
There are currently no established pharmacological treatments that can induce development of congenitally missing teeth in clinical practice. However, experimental approaches are under investigation (see Experimental section below).

**Pharmacogenomics**: 
Not applicable for standard tooth agenesis treatment, as no routine pharmacotherapy exists. In the context of experimental regenerative therapies, genetic understanding may guide personalized approaches in the future.

### Advanced Therapeutics

**Experimental/Emerging Therapies**:

1. **Antibody-based therapy**:
   - **Anti-USAG-1 antibody treatment**: In development for treating congenital tooth agenesis
   - **Mechanism**: Antibody-mediated pathway modulation targeting tooth regeneration
   - **Status**: Experimental; showing promise in preclinical studies
   (su2024edavariantsare pages 1-2)

2. **Wnt pathway modulation**:
   - **Wnt3a-based approaches**: Promotes in situ dentin formation through NKD1-MSX1 axis-mediated odontogenic differentiation
   - **Mechanism**: Wnt3a orchestrates upregulation of NKD1/MSX1 expression, triggering odontogenic gene activation
   - **Application**: Could enhance reparative dentin formation and potentially tooth regeneration
   (su2024edavariantsare pages 1-2)

3. **Cell therapy**:
   - **Dental pulp stem cell (DPSC) therapy**: Used successfully for periodontal regeneration; potential application to tooth regeneration
   - **Evidence**: Multi-center RCT (132 patients) showed DPSC injection improved bone defect depth and clinical attachment level
   - **Mechanism**: DPSCs promote tissue regeneration through differentiation and paracrine effects
   - **Status**: Clinical trials for periodontal applications; tooth regeneration application experimental
   (su2024edavariantsare pages 1-2)

4. **Tooth regeneration approaches**:
   - **Stem cell-driven biomedical technologies**: Engineering scaffolds, organoid models, molecular targeted strategies
   - **Whole tooth reconstruction**: From tooth development biology to clinical application
   - **Xenotransplantation**: Using genetically modified animals for tooth germ development
   - **Status**: Largely preclinical/experimental; represents future direction
   (su2024edavariantsare pages 1-2)

### Surgical and Interventional

**Surgical Interventions**:

1. **Dental implant placement**:
   - **Single-tooth implants**: For individual missing teeth, particularly maxillary lateral incisors
   - **Multiple implants**: For oligodontia cases
   - **Timing**: After growth completion (typically late adolescence/young adulthood)
   - **Outcomes**: Generally excellent for aesthetic and functional rehabilitation
   (meade2023toothagenesisan pages 4-5, su2024edavariantsare pages 1-2)

2. **Bone grafting**:
   - **Indication**: To add bone volume to areas of tooth agenesis where alveolar bone is deficient
   - **Application**: Prepares site for implant placement
   - **Method**: Autogenous, allogeneic, or xenogeneic bone grafts
   (su2024edavariantsare pages 1-2)

3. **Extraction of retained primary teeth**:
   - **Timing considerations**: Early extraction when infra-occlusion is severe and adverse effects on occlusion observed
   - **Outcome**: May result in spontaneous space closure, potentially avoid worsening of bony defects
   - **Challenges**: Space closure more predictable in maxilla than mandible
   (meade2023toothagenesisan pages 4-5)

4. **Orthognathic surgery**:
   - **Application**: For severe skeletal discrepancies associated with tooth agenesis
   - **Combination**: Often combined with orthodontic and prosthetic treatment
   (su2024edavariantsare pages 1-2)

### Supportive and Rehabilitative

**Orthodontic Interventions**:

1. **Space closure**:
   - **Approach**: Mesialize posterior teeth to close spaces of missing teeth
   - **Application**: Particularly for missing premolars or lateral incisors in certain cases
   - **Advantage**: Avoids prosthetic replacement

2. **Space management**:
   - **Approach**: Maintain or create appropriate space for future implant or prosthetic restoration
   - **Tools**: Fixed appliances, temporary anchorage devices (TADs)

3. **Growth modification**:
   - **Application**: Address skeletal discrepancies during late mixed/permanent dentition
   - **Timing**: Critical during active growth phases

4. **Fixed orthodontic appliances**:
   - **Function**: Leveling, aligning, space management, pre-prosthetic tooth positioning
   - **Anchorage**: Temporary anchorage devices help overcome challenges associated with reduced tooth number
   (meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 4-5, su2024edavariantsare pages 1-2)

**Prosthodontic Interventions**:

1. **Dental implant-supported crowns**:
   - **Application**: Definitive restoration for single or multiple missing teeth
   - **Materials**: Zirconia, porcelain-fused-to-metal, all-ceramic
   - **Timing**: Post-growth

2. **Resin-bonded bridges (Maryland bridges)**:
   - **Application**: Minimally invasive restoration for single missing anterior teeth
   - **Advantage**: Preserves adjacent tooth structure

3. **Removable partial dentures**:
   - **Application**: Multiple missing teeth, especially in growing patients or when implants not feasible
   - **Types**: Acrylic, flexible framework, cast metal framework

4. **Composite resin build-up**:
   - **Application**: Build-up of malformed primary and permanent teeth to improve aesthetics and function
   - **Timing**: Can be done in young children for aesthetic and functional improvement

5. **Veneers**:
   - **Application**: Improve aesthetics of adjacent teeth, can reshape canines to resemble lateral incisors

6. **CAD/CAM prosthetic rehabilitation**:
   - **Advantage**: Precise, digital workflow for complex rehabilitation
   (meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 4-5, su2024edavariantsare pages 1-2)

**Supportive Care**:
- **Speech therapy**: For articulation difficulties
- **Nutritional counseling**: Especially in severe childhood cases
- **Psychological support**: Address aesthetic and psychosocial concerns
(meade2023toothagenesisan pages 1-2, su2024edavariantsare pages 1-2)

### Treatment Strategy

**Treatment Algorithms**:
- **Multidisciplinary team approach essential**: Orthodontists, prosthodontists, oral surgeons, pediatric dentists, geneticists
- **Early diagnosis critical**: Facilitates timely intervention during growth
- **Age-appropriate interventions**:
  - Early childhood (primary/early mixed dentition): Removable appliances, composite build-up
  - Adolescence (active growth): Orthodontic treatment, growth modification
  - Post-growth (young adulthood): Definitive implant/prosthetic rehabilitation
- **Personalized treatment planning**: Based on number and location of missing teeth, skeletal pattern, patient preferences
(meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 1-2, meade2023toothagenesisan pages 4-5)

**Combination Therapies**:
Most treatment plans combine:
- Orthodontic tooth movement
- Prosthodontic rehabilitation
- Surgical interventions (extraction, implants, bone grafting)
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 4-5, su2024edavariantsare pages 1-2)

**Treatment Outcomes**:
- **Success rates**: Generally favorable with multidisciplinary approach
- **Aesthetic outcomes**: Good to excellent with modern materials and techniques
- **Functional outcomes**: Significant improvement in mastication, speech, quality of life
(meade2023toothagenesisan pages 1-2, su2024edavariantsare pages 1-2)

### Suggested MAXO Terms

Based on the treatment modalities described:
- MAXO:0000004 (orthodontic treatment)
- MAXO:0000011 (dental implant placement)
- MAXO:0000127 (prosthodontic treatment)
- MAXO:0001298 (bone grafting)
- MAXO:0000571 (tooth extraction)
- MAXO:0000756 (stem cell therapy - experimental)

---

## 13. Prevention

### Prevention Levels

**Primary Prevention** (preventing disease occurrence):
- **Limited options**: Since tooth agenesis is predominantly genetic, primary prevention opportunities are limited
- **Avoidance of teratogenic exposures**:
  - Avoid unnecessary chemotherapy/radiation during pregnancy and childhood when possible
  - Maternal smoking cessation during pregnancy
  - Avoid thalidomide and other known teratogens during pregnancy
- **Genetic counseling**: Pre-conception counseling for couples with family history
(meade2023toothagenesisan pages 3-4)

**Secondary Prevention** (early detection and intervention):
- **Clinical monitoring**: Regular dental examinations in childhood to detect delayed or failed eruption
- **Radiographic surveillance**: Appropriate-age radiographic evaluation to confirm tooth development
- **Family screening**: In familial cases, siblings and offspring should receive early dental evaluation
- **Genetic screening**: In families with known pathogenic variants, cascade genetic testing of relatives
(meade2023toothagenesisan pages 1-2)

**Tertiary Prevention** (preventing complications):
- **Early orthodontic intervention**: To manage space, guide eruption of existing teeth, prepare for future restoration
- **Timely prosthetic rehabilitation**: Prevent alveolar bone atrophy, malocclusion development, TMD
- **Multidisciplinary treatment planning**: Comprehensive early planning prevents worsening of functional and aesthetic complications
- **Psychological support**: Prevent or address psychosocial complications
(meade2023toothagenesisan pages 1-2, meade2023toothagenesisan pages 4-5)

### Immunization

Not applicable - tooth agenesis is not vaccine-preventable.

### Screening and Early Detection

**Screening Programs**:
- **Clinical dental screening**: Regular dental examinations in childhood
- **Radiographic screening**: Age-appropriate panoramic radiographs or CBCT when tooth agenesis suspected
- **High-risk population screening**: Family members of affected individuals

**Genetic Screening**:
- **Carrier screening**: For X-linked EDA variants in families with known mutations
- **Prenatal testing**: Chorionic villus sampling or amniocentesis available for couples with known familial pathogenic variant
- **Preimplantation genetic diagnosis**: Option for couples undergoing IVF with known familial variant

**Risk Stratification**:
- **Family history**: First-degree relatives of affected individuals at increased risk
- **Genetic testing**: Identifies at-risk individuals before clinical manifestation
(modafferi2025geneticaspectsof pages 5-7)

### Behavioral Interventions

**Lifestyle Modifications**:
- **Maternal health**: Smoking cessation, alcohol avoidance during pregnancy
- **Avoidance of teratogens**: During pregnancy and early childhood
(meade2023toothagenesisan pages 3-4)

### Counseling

**Genetic Counseling**:
- **Risk assessment**: For familial cases (37.5% of cases familial)
- **Inheritance pattern explanation**: Autosomal dominant, autosomal recessive, X-linked depending on gene
- **Recurrence risk counseling**: Based on inheritance pattern and family history
- **Reproductive options**: Discussion of prenatal testing, preimplantation genetic diagnosis
- **Cascade testing**: Recommendation for testing of at-risk family members
- **Psychosocial support**: Addressing concerns about affected children
(meade2023toothagenesisan pages 2-3, modafferi2025geneticaspectsof pages 5-7)

### Public Health

**Public Health Interventions**:
While tooth agenesis is primarily genetic and not readily preventable through population-level public health measures, relevant interventions include:
- **Avoidance of unnecessary radiation**: Especially in children
- **Maternal health education**: Regarding teratogen avoidance during pregnancy
(meade2023toothagenesisan pages 3-4)

### Prophylaxis

**Preventive Measures**:
No specific prophylactic medications or procedures can prevent tooth agenesis in genetically susceptible individuals. Prevention focuses on early detection and timely intervention to prevent secondary complications (meade2023toothagenesisan pages 1-2).

---

## 14. Other Species / Natural Disease

### Taxonomy

**Species Affected**:
Natural occurrence of tooth agenesis in non-human species is not extensively documented in the gathered 2020-2025 human-focused literature. However, model organisms are used extensively for research:

- **Mus musculus** (House mouse) - NCBI:txid10090: Primary model organism
- **Rattus norvegicus** (Norway rat) - NCBI:txid10116: Used for tooth development studies  
- **Sus scrofa** (Pig/Miniature pig): Used for odontoblast and tooth germ studies
(fallea2025dissectingthegenetic pages 2-4, su2024edavariantsare pages 1-2)

### Natural Disease

**Naturally Occurring Disease**:
While the gathered literature does not extensively document naturally occurring tooth agenesis in companion animals or wildlife, it is likely to occur given genetic conservation.

### Comparative Biology

**Comparative Pathology** and **Evolutionary Conservation**:

Tooth development mechanisms are highly conserved across mammalian species, making mouse models particularly relevant:

1. **Msx1 knockout mice**:
   - **Phenotype**: Show tooth agenesis with facial and dental abnormalities including cleft palate
   - **Relevance**: Mimics human MSX1-related tooth agenesis and demonstrates gene function conservation
   (modafferi2025geneticaspectsof pages 5-7)

2. **Lrp4 mutant mice**:
   - **Phenotype**: Supernumerary incisors observed
   - **Relevance**: Demonstrates LRP4 role in tooth number regulation; mutations in humans associated with mesiodens and tooth agenesis
   (fallea2025dissectingthegenetic pages 2-4)

3. **Axin2 knockout mice**:
   - **Phenotype**: Variably show tooth agenesis; heterozygous knockout mice demonstrate dose-dependent effects
   - **Relevance**: Models AXIN2-related human tooth agenesis with variable expressivity
   (su2024edavariantsare pages 1-2)

4. **Lrp4 and Sostdc1 knockout mice**:
   - **Phenotype**: Multiple dental anomalies including supernumerary incisors and molars
   - **Mechanism**: Disrupts negative feedback loop between Wnt/β-catenin, BMP, and SHH signaling during bud and cap stages
   (fallea2025dissectingthegenetic pages 2-4)

**Odontoblast Differentiation Studies**:
- Mouse and miniature pig models used to identify NKD1+ subpopulations with secretory odontoblast characteristics
- Conserved spatial distribution and co-localization with DSPP in developing tooth germs across murine, miniature pig, and human models
- Demonstrates functional conservation of odontogenic mechanisms
(su2024edavariantsare pages 1-2)

### Model Organisms

**Model Types and Systems**:

1. **Mouse (Mus musculus)**:
   - **Most common model organism**: Extensively used due to genetic tractability, short generation time, conservation of developmental pathways
   - **Databases**: MGI (Mouse Genome Informatics), IMPC (International Mouse Phenotyping Consortium)
   
2. **Rat (Rattus norvegicus)**:
   - **Application**: RNA-seq analysis of Wnt signaling molecules at different stages of tooth germ development
   - **Database**: RGD (Rat Genome Database)

3. **Miniature pig**:
   - **Application**: Odontoblast and tooth germ developmental studies
   - **Advantage**: Larger size, similar dental anatomy to humans

**Genetic Models Available**:

1. **Knockout models**:
   - Msx1 knockout
   - Axin2 knockout
   - Lrp4 knockout
   - Sostdc1 knockout

2. **Transgenic models**:
   - Models expressing reporters for Wnt pathway components (Wnt10a, Dkk1, Sost)
   - Gli1-positive cell lineage tracing models

**Model Characteristics**:

**Phenotype Recapitulation**:
- **Tooth agenesis**: Mouse knockout models successfully recapitulate human tooth agenesis phenotypes
- **Associated features**: Cleft palate (Msx1-/-), craniofacial abnormalities mirror human syndromic presentations
- **Pathway disruption**: Models demonstrate disruption of Wnt, BMP, SHH, EDA pathways similar to human disease

**Model Limitations**:
- **Species differences**: Mouse dentition differs from human (continuously growing incisors, different tooth number and morphology)
- **Deciduous vs. permanent dentition**: Mice have only one dentition; cannot fully model deciduous vs. permanent tooth-specific agenesis
- **Genetic background effects**: Phenotype severity can vary with genetic background strain
- **Incomplete penetrance**: May not fully recapitulate variable human expressivity

**Research Applications**:
- **Pathway elucidation**: Understanding Wnt, BMP, SHH, FGF, EDA signaling in odontogenesis
- **Gene function studies**: Determining roles of specific genes in tooth development
- **Therapeutic testing**: Preclinical testing of regenerative approaches (stem cell therapy, antibody treatments, growth factor delivery)
- **Genotype-phenotype correlation**: Understanding how specific mutations affect tooth development

**Resources**:
- MGI (Mouse Genome Informatics): https://www.informatics.jax.org/
- IMPC (International Mouse Phenotyping Consortium)
- RGD (Rat Genome Database)
(fallea2025dissectingthegenetic pages 2-4, modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2)

---

## Summary

This comprehensive research report on tooth agenesis synthesizes current knowledge from 2020-2025 literature, emphasizing recent developments in genetic understanding, molecular mechanisms, diagnostics, and emerging therapies. Tooth agenesis is a common congenital dental anomaly with significant functional, aesthetic, and psychosocial impacts, affecting approximately 6.4% of the population for permanent dentition.

The condition has a strong genetic basis involving at least 14 major genes (notably EDA, MSX1, WNT10A, PAX9) and multiple signaling pathways (Wnt/β-catenin, TNF receptor/EDA-EDAR, mTOR, BMP, SHH, FGF). Diagnosis relies on clinical examination and radiographic evaluation, with genetic testing increasingly important for confirming etiology and guiding management. Treatment requires multidisciplinary coordination of orthodontic, prosthodontic, and surgical approaches, with exciting experimental therapies (stem cell-based regeneration, anti-USAG-1 antibodies, Wnt pathway modulation) under development.

Early diagnosis and intervention during growth periods are critical for optimal long-term outcomes. Genetic counseling is essential for familial cases. Mouse models have proven invaluable for understanding developmental mechanisms and testing therapeutic approaches. The field is rapidly evolving toward regenerative solutions that may eventually enable biological tooth replacement (meade2023toothagenesisan pages 1-2, modafferi2025geneticaspectsof pages 1-2, fallea2025dissectingthegenetic pages 1-2, modafferi2025geneticaspectsof pages 5-7, su2024edavariantsare pages 1-2).

References

1. (meade2023toothagenesisan pages 1-2): Maurice J. Meade and Craig W. Dreyer. Tooth agenesis: an overview of diagnosis, aetiology and management. Dec 2023. URL: https://doi.org/10.1016/j.jdsr.2023.07.001, doi:10.1016/j.jdsr.2023.07.001. This article has 74 citations.

2. (modafferi2025geneticaspectsof pages 1-2): Clarissa Modafferi, Ilaria Tucci, Francesco Maria Bogliardi, Elena Gimondo, Pietro Chiurazzi, Elisabetta Tabolacci, and Cristina Grippaudo. Genetic aspects of tooth agenesis. Genes, 16:582, May 2025. URL: https://doi.org/10.3390/genes16050582, doi:10.3390/genes16050582. This article has 8 citations.

3. (fallea2025dissectingthegenetic pages 1-2): Antonio Fallea, Mirella Vinci, Simona L’Episcopo, Massimiliano Bartolone, Antonino Musumeci, Alda Ragalmuto, Simone Treccarichi, and Francesco Calì. Dissecting the genetic contribution of tooth agenesis. International Journal of Molecular Sciences, 26:10485, Oct 2025. URL: https://doi.org/10.3390/ijms262110485, doi:10.3390/ijms262110485. This article has 9 citations.

4. (modafferi2025geneticaspectsof pages 2-4): Clarissa Modafferi, Ilaria Tucci, Francesco Maria Bogliardi, Elena Gimondo, Pietro Chiurazzi, Elisabetta Tabolacci, and Cristina Grippaudo. Genetic aspects of tooth agenesis. Genes, 16:582, May 2025. URL: https://doi.org/10.3390/genes16050582, doi:10.3390/genes16050582. This article has 8 citations.

5. (fallea2025dissectingthegenetic pages 4-6): Antonio Fallea, Mirella Vinci, Simona L’Episcopo, Massimiliano Bartolone, Antonino Musumeci, Alda Ragalmuto, Simone Treccarichi, and Francesco Calì. Dissecting the genetic contribution of tooth agenesis. International Journal of Molecular Sciences, 26:10485, Oct 2025. URL: https://doi.org/10.3390/ijms262110485, doi:10.3390/ijms262110485. This article has 9 citations.

6. (modafferi2025geneticaspectsof pages 5-7): Clarissa Modafferi, Ilaria Tucci, Francesco Maria Bogliardi, Elena Gimondo, Pietro Chiurazzi, Elisabetta Tabolacci, and Cristina Grippaudo. Genetic aspects of tooth agenesis. Genes, 16:582, May 2025. URL: https://doi.org/10.3390/genes16050582, doi:10.3390/genes16050582. This article has 8 citations.

7. (meade2023toothagenesisan pages 3-4): Maurice J. Meade and Craig W. Dreyer. Tooth agenesis: an overview of diagnosis, aetiology and management. Dec 2023. URL: https://doi.org/10.1016/j.jdsr.2023.07.001, doi:10.1016/j.jdsr.2023.07.001. This article has 74 citations.

8. (meade2023toothagenesisan pages 2-3): Maurice J. Meade and Craig W. Dreyer. Tooth agenesis: an overview of diagnosis, aetiology and management. Dec 2023. URL: https://doi.org/10.1016/j.jdsr.2023.07.001, doi:10.1016/j.jdsr.2023.07.001. This article has 74 citations.

9. (su2024edavariantsare pages 1-2): Lanxin Su, Bichen Lin, Miao Yu, Yang Liu, Shichen Sun, Hailan Feng, Haochen Liu, and Dong Han. Eda variants are responsible for approximately 90% of deciduous tooth agenesis. International Journal of Molecular Sciences, 25:10451, Sep 2024. URL: https://doi.org/10.3390/ijms251910451, doi:10.3390/ijms251910451. This article has 9 citations.

10. (fallea2025dissectingthegenetic pages 2-4): Antonio Fallea, Mirella Vinci, Simona L’Episcopo, Massimiliano Bartolone, Antonino Musumeci, Alda Ragalmuto, Simone Treccarichi, and Francesco Calì. Dissecting the genetic contribution of tooth agenesis. International Journal of Molecular Sciences, 26:10485, Oct 2025. URL: https://doi.org/10.3390/ijms262110485, doi:10.3390/ijms262110485. This article has 9 citations.

11. (modafferi2025geneticaspectsof pages 4-5): Clarissa Modafferi, Ilaria Tucci, Francesco Maria Bogliardi, Elena Gimondo, Pietro Chiurazzi, Elisabetta Tabolacci, and Cristina Grippaudo. Genetic aspects of tooth agenesis. Genes, 16:582, May 2025. URL: https://doi.org/10.3390/genes16050582, doi:10.3390/genes16050582. This article has 8 citations.

12. (meade2023toothagenesisan pages 4-5): Maurice J. Meade and Craig W. Dreyer. Tooth agenesis: an overview of diagnosis, aetiology and management. Dec 2023. URL: https://doi.org/10.1016/j.jdsr.2023.07.001, doi:10.1016/j.jdsr.2023.07.001. This article has 74 citations.

## Artifacts

- [Edison artifact artifact-00](Tooth_Agenesis-deep-research-falcon_artifacts/artifact-00.md)