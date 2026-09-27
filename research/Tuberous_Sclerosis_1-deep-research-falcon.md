---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:06:11.358613'
end_time: '2026-07-31T00:20:13.865686'
duration_seconds: 842.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)
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
  path: Tuberous_Sclerosis_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)** covering all of the
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
- **Disease Name:** Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tuberous Sclerosis 1 (TSC1-Related Tuberous Sclerosis Complex)** covering all of the
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


# TSC1-Related Tuberous Sclerosis Complex: Disease Characteristics Research Report

## Scope and evidence note

This report treats **Tuberous Sclerosis 1** as the molecular subtype of tuberous sclerosis complex (TSC) caused by a pathogenic **TSC1** variant. Most diagnostic, epidemiologic, surveillance, and therapeutic evidence is reported for combined TSC1/TSC2 cohorts; where evidence is specifically TSC1-stratified, that distinction is stated. The principal current authority is the 2021 International TSC Consensus guideline (published October 2021; DOI: https://doi.org/10.1016/j.pediatrneurol.2021.07.011). Recent sources prioritized include 2023–2024 molecular, single-cell, clinical-practice, and trial data.

| domain | key fact | quantitative/current evidence | suggested ontology identifiers |
|---|---|---|---|
| Disease identity | TSC1-related tuberous sclerosis complex is the TSC subtype caused by pathogenic variants in **TSC1**, a multisystem mTORopathy with hamartomas/hamartia affecting brain, skin, kidney, heart, lung, and eye | MONDO disease association for **tuberous sclerosis 1**: **MONDO:0008612**; broader TSC disease listed as autosomal dominant and multisystem in consensus/gene reviews (OpenTargets Search: tuberous sclerosis 1,tuberous sclerosis complex-TSC1, man2024thegeneticsof pages 1-2, dufneralmeida2024molecularandfunctional pages 1-2) | MONDO:0008612; MeSH: Tuberous Sclerosis; ICD terms: tuberous sclerosis complex |
| Disease identifiers | Broader disease identifiers are better established than subtype-specific coding; subtype can be represented by MONDO disease + causal gene | TSC consensus recognizes diagnosis by clinical criteria or pathogenic **TSC1/TSC2** variant in normal tissue (dufneralmeida2024molecularandfunctional pages 1-2, northrup2021updatedinternationaltuberous pages 10-14) | MONDO:0008612; OMIM disease: tuberous sclerosis complex (OMIM exact disease subtype IDs not confirmed here) |
| Causal gene | **TSC1** encodes **hamartin**, core component of TSC complex, negative regulator of mTORC1 | TSC1 maps to **9q34.1**, has **23 exons**; in one 2024 cohort, 18/106 molecular diagnoses (17%) were TSC1 and 88/106 (83%) TSC2 (dufneralmeida2024molecularandfunctional pages 1-2) | HGNC: **TSC1**; Ensembl: **ENSG00000165699** (OpenTargets Search: tuberous sclerosis 1,tuberous sclerosis complex-TSC1); OMIM gene: **TSC1 / MIM 605284** (dufneralmeida2024molecularandfunctional pages 1-2) |
| Inheritance | Usually **autosomal dominant** with high penetrance and marked variable expressivity; many cases are de novo or mosaic | Incidence/prevalence estimates across TSC: ~1:5,800 to 1:13,520 live births in review; global incidence often cited ~1 per 6,000–10,000 live births (man2024thegeneticsof pages 1-2, jansen2020burdenofillness pages 1-2) | Inheritance: HP:0000006 Autosomal dominant inheritance |
| Mosaicism | Somatic mosaicism is an important cause of milder or mutation-negative presentations and can still transmit to offspring | 10–15% of clinically diagnosed TSC has no variant found by conventional testing; high-depth NGS can reveal low-level mosaic variants; mosaic individuals may have fewer manifestations but require surveillance (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 8-9, northrup2021updatedinternationaltuberous pages 10-14) | HP:0001417 Mosaicism |
| TSC1 variant spectrum | TSC1 pathogenic variants include intragenic deletions, nonsense, missense, duplication, splice/intronic changes; loss of function predominates | Sicilian TSC1 cohort: intragenic deletions **48.4%**, nonsense **38.7%**, missense **9.6%**, duplication **3.2%**; 45.1% inherited and 54.9% sporadic/de novo in that cohort (pratico2025geneticscreeningof pages 3-4) | Sequence ontology terms: nonsense_variant, frameshift_variant, splice_region_variant, intragenic_deletion, missense_variant |
| Phenotype: epilepsy | Epilepsy is a core neurologic phenotype and often the earliest clinically important manifestation | Consensus: focal seizures and epileptic spasms occur in **63–78%** of infants with TSC; in one TSC1 cohort epilepsy in **64.5%**, mean onset **35.4 months** (northrup2021updatedinternationaltuberous pages 10-14, pratico2025geneticscreeningof pages 3-4) | HPO: Seizure; Focal seizure; Epileptic spasm; Developmental epileptic encephalopathy (if applicable) |
| Phenotype: cortical tubers / migration lines | Structural brain lesions are hallmark brain findings underlying seizures and neurodevelopmental morbidity | TSC1 cohort: cortical tubers **67.8%**, subependymal nodules **51.6%** (pratico2025geneticscreeningof pages 3-4); consensus revised criterion to “multiple cortical tubers and/or radial migration lines” (northrup2021updatedinternationaltuberous pages 10-14) | HPO: Cortical tuber; Radial migration line; Subependymal nodule |
| Phenotype: TAND / neurodevelopment | TSC-associated neuropsychiatric disorders span behavioral, psychiatric, intellectual, academic, and psychosocial domains | TAND issues affect up to ~90% across TSC literature review; TSC1 cohort autism spectrum disorder **12.9%** and cognitive outcome ranged from normal **51.6%** to severe deficit **16.1%** (singh2023treatmentresistantepilepsyand pages 1-3, pratico2025geneticscreeningof pages 3-4) | HPO: Autism; Intellectual disability; Attention-deficit/hyperactivity disorder; Anxiety; Behavioral abnormality |
| Phenotype: renal angiomyolipoma | Renal angiomyolipoma is a common, clinically actionable manifestation | TOSCA: **1,062/2,211 (48%)** had angiomyolipoma; median angiomyolipoma diagnosis age **13 years**; more common in females; TSC1-associated lesions develop later and are smaller/less likely growing on average (kingswood2020renalmanifestationsof pages 1-2) | HPO: Renal angiomyolipoma; Chronic kidney disease; Hypertension |
| Phenotype: pulmonary LAM | Pulmonary lymphangioleiomyomatosis is mainly an adult female complication, milder in TSC-LAM than sporadic LAM | LAM occurs in **30–40% of adult females** with TSC at childbearing age; spontaneous pneumothorax in up to **70%** of LAM patients (jansen2020burdenofillness pages 1-2) | HPO: Lymphangioleiomyomatosis; Pneumothorax; Dyspnea |
| Phenotype: skin lesions | Facial angiofibromas and other cutaneous hamartomas are major diagnostic clues | Skin lesions are major criteria in consensus; topical and systemic mTOR-targeted therapies are in active clinical use/trials (northrup2021updatedinternationaltuberous pages 10-14, NCT05495425 chunk 1) | HPO: Facial angiofibromas; Fibrous cephalic plaque; Hypomelanotic macule; Ungual fibroma |
| Phenotype: cardiac rhabdomyoma | Cardiac rhabdomyomas are common prenatal/infant manifestations and can trigger diagnosis | In a Japanese claims study, cardiac rhabdomyoma was the highest-incidence manifestation among those diagnosed before age 2 (**54.8%**) (from abstract summary) (man2024thegeneticsof pages 1-2) | HPO: Cardiac rhabdomyoma; Arrhythmia |
| Mechanism | TSC1/hamartin forms complex with TSC2/tuberin and TBC1D7; the complex acts as a GAP toward **RHEB**, restraining **mTORC1** | Loss of TSC1/2 increases **RHEB-GTP**, activates TORC1, elevates p70 S6 kinase signaling, upregulates anabolic metabolism and cell growth (dufneralmeida2024molecularandfunctional pages 1-2, zucco2018thegenerationand pages 35-40) | GO: regulation of TORC1 signaling; GTPase activator activity; negative regulation of cell growth |
| Pathophysiology chain | Upstream: TSC1 loss of function → TSC complex destabilization → RHEB activation → mTORC1 hyperactivation; downstream: altered growth, migration, synaptogenesis, metabolism, autophagy suppression, hamartoma formation, epileptogenesis | Single-cell cortical tuber study found preserved neuronal subtypes but major transcriptomic shifts in principal neurons and upper-layer GABAergic neurons, reduced mitochondrial respiration, switch to fatty-acid metabolism, and neuron-specific AMPA signaling candidate in epileptogenesis (sørensen2024singlecellprofilingof pages 1-3) | GO: positive regulation of cell growth; regulation of neuron differentiation; synaptogenesis; fatty acid metabolic process; mitochondrial respiration; macroautophagy |
| Cellular processes | mTOR dysregulation affects neuronal maturation, axonal growth, myelination, gliosis, BBB integrity, and seizure networks | Human BBB microphysiologic model showed increased permeability in TSC-mutant BBB rescued by wild-type astrocytes or rapamycin; glial/myelination abnormalities described in TSC models and tissue (brown2024rescueofimpaired pages 1-2, zimmer2020tuberoussclerosiscomplex pages 6-7) | GO: blood-brain barrier establishment/maintenance; gliogenesis; myelination; astrocyte activation |
| Anatomy | Primary affected organs: brain, kidney, skin, heart, lung, eye; secondary systemic effects include neuropsychiatric, renal, respiratory and cardiovascular complications | Consensus surveillance spans brain MRI, abdominal MRI, chest CT/PFTs, dermatology, dental, cardiac echo/EKG, ophthalmology (northrup2021updatedinternationaltuberous pages 40-43) | UBERON: brain, kidney, skin, heart, lung, retina |
| Cell types | High-value implicated cell types include principal/glutamatergic neurons, GABAergic interneurons, astrocytes, oligodendrocytes/NG2 glia, vascular endothelial/barrier cells, smooth muscle-like LAM cells | Single-cell tuber data highlight principal neurons and layer 1–2 GABAergic neurons; BBB model implicates astrocyte support and endothelial-barrier dysfunction; glial review emphasizes astrocytes, oligodendrocytes, NG2 glia, microglia (sørensen2024singlecellprofilingof pages 1-3, brown2024rescueofimpaired pages 1-2, zimmer2020tuberoussclerosiscomplex pages 6-7) | CL: glutamatergic neuron; GABAergic interneuron; astrocyte; oligodendrocyte; NG2 glial cell; endothelial cell; microglial cell |
| Subcellular localization | Disease biology centers on lysosome-associated mTORC1 regulation and signaling to translation/metabolism pathways | TSC complex regulates RHEB-dependent TORC1; mTORC1-driven phosphorylation changes and metabolic rewiring are central (dufneralmeida2024molecularandfunctional pages 1-2, zucco2018thegenerationand pages 35-40, sørensen2024singlecellprofilingof pages 1-3) | GO Cellular Component: lysosome; lysosomal membrane; mTORC1 complex; cytosol |
| Diagnostics | Definite diagnosis can be established by clinical criteria or pathogenic **TSC1/TSC2** variant | Consensus: **11 major** and **7 minor** clinical features; failure to detect variant does **not** exclude TSC; high-depth NGS needed for low-level mosaicism/intronic causes (northrup2021updatedinternationaltuberous pages 10-14) | HPO/clinical terms for major criteria; MONDO:0008612; gene-based diagnosis with TSC1 |
| Genetic testing strategy | Use multigene NGS panel or exome/genome with copy-number detection; escalate to high-read-depth methods and RNA/splice evaluation when negative but suspicion remains | Current molecular testing identifies pathogenic TSC1/TSC2 variant in nearly **90%** of definite TSC; 2024 Brazilian cohort identified alterations in **91%** (106/116) (dufneralmeida2024molecularandfunctional pages 1-2, northrup2021updatedinternationaltuberous pages 10-14) | Testing ontology names: NGS gene panel; exome sequencing; genome sequencing; MLPA/CNV analysis; RNA splicing assay |
| Surveillance | Lifelong organ-based surveillance is standard; key intervals are consensus-defined | Brain MRI every **1–3 years** in asymptomatic patients <25 years; infant EEG every **6 weeks** to 12 months, then every **3 months** to 24 months; abdominal MRI every **1–3 years**; baseline chest CT in females and symptomatic males ≥18 years (northrup2021updatedinternationaltuberous pages 40-43, northrup2021updatedinternationaltuberous pages 43-45) | MAXO-like actions: brain MRI surveillance; EEG monitoring; abdominal MRI surveillance; pulmonary function testing |
| Treatment: seizure control | First-line infantile spasm therapy is **vigabatrin**; everolimus and a specific cannabidiol formulation are approved for TSC-associated seizures; surgery for refractory focal epilepsy | Real-world everolimus: epilepsy responders (≥50% reduction) **31%** overall, **46%** if <18 years vs **14%** if ≥18 years (cockerell2023effectivenessandsafety pages 1-2); consensus recommends epilepsy surgery after failure of 3 medications in appropriate candidates (northrup2021updatedinternationaltuberous pages 40-43) | MAXO: antiseizure medication treatment; epilepsy surgery; CHEBI: vigabatrin, everolimus, cannabidiol |
| Treatment: mTOR inhibition | **Everolimus/sirolimus** target the core disease pathway and are used for SEGA, renal angiomyolipoma, LAM, and seizures in selected settings | Real-world everolimus adverse effects in **95%**; common oral ulceration/stomatitis **63%**, URTI **38%**, cholesterol increase **41%**, anemia **30%**, leucopenia **25%**; grade 3–4 AEs **36%** (cockerell2023effectivenessandsafety pages 1-2) | MAXO: mTOR inhibitor therapy; CHEBI: everolimus, sirolimus/rapamycin |
| Treatment: renal disease | For asymptomatic growing angiomyolipoma >3 cm, mTOR inhibitor is first-line; embolization + corticosteroids for acute hemorrhage | Consensus and kidney recommendations support MRI surveillance and pre-emptive intervention; TOSCA found no renal hemorrhage after starting mTOR inhibitor in substudy patients (northrup2021updatedinternationaltuberous pages 43-45, kingswood2020renalmanifestationsof pages 1-2) | MAXO: renal angiomyolipoma treatment; arterial embolization; corticosteroid therapy; CHEBI: everolimus, sirolimus |
| Treatment: pulmonary disease | mTOR inhibitor is treatment of choice for clinically significant TSC-LAM | Recommended when FEV1 <70% predicted, abnormal DLCO, air trapping, oxygen desaturation, or rapid decline (northrup2021updatedinternationaltuberous pages 43-45) | MAXO: pulmonary mTOR inhibitor treatment; pulmonary function monitoring |
| Treatment: dermatology | Topical sirolimus formulations are in real-world use and late-phase trials for facial angiofibromas/skin lesions | Phase 3 NPC-12Y topical sirolimus 0.2% gel trial completed; 43 participants, primary endpoint at 12 weeks for angiofibroma improvement (NCT05495425 chunk 1) | MAXO: topical skin lesion treatment; CHEBI: sirolimus |
| Quality of life / burden | Disease burden is high for patients and caregivers, beyond tumor counts alone | TOSCA QoL study: negative effect on education/career in **42.1%** of patients; caregivers reported family-life impact **76.5%**; pain/discomfort **35%**; anxiety/depression **43.4%** (jansen2020burdenofillness pages 1-2) | HPO/clinical terms: pain, anxiety, depression; psychosocial burden terms |
| Prognosis | Prognosis is variable and improved by multidisciplinary surveillance and pathway-based treatment, but neurologic, renal, and pulmonary complications remain major causes of morbidity | TSC-related epilepsy and organ complications drive burden; kidney and pulmonary surveillance designed to prevent hemorrhage, CKD, pneumothorax, and progression (jansen2020burdenofillness pages 1-2, kingswood2020renalmanifestationsof pages 1-2, northrup2021updatedinternationaltuberous pages 43-45) | Outcome ontology names: chronic disease course; variable expressivity |
| Prevention / early intervention | No primary prevention of genotype; secondary/tertiary prevention relies on early diagnosis, family testing, surveillance, pre-symptomatic EEG monitoring, and early treatment | Pre-emptive vigabatrin before clinical seizures may delay/prevent onset in high-risk infants with epileptiform EEG; genetic counseling recommended for all families (northrup2021updatedinternationaltuberous pages 10-14, northrup2021updatedinternationaltuberous pages 40-43) | MAXO: genetic counseling; cascade testing; EEG screening; early antiseizure therapy |
| Current trials | Active/complete 2022–2025 studies are testing pathway-targeted and adjunctive therapies | **NCT05534672** rapamycin vs placebo in drug-resistant TSC epilepsy; **NCT05104983** sirolimus prevention in infants; **NCT05323734** ganaxolone phase 3 completed; **NCT05059327** basimglurant phase 2 completed; **NCT02962414** long-term everolimus safety; **NCT05495425** topical sirolimus gel completed (NCT02962414 chunk 1, NCT05534672 chunk 1, NCT05104983 chunk 1, NCT05495425 chunk 1, NCT05323734 chunk 1, NCT05059327 chunk 1) | ClinicalTrials.gov IDs as identifiers |
| Model organisms / systems | Widely used models include mouse, rat, zebrafish, Drosophila, MEFs, patient iPSCs, organoids, and neurovascular chips | Tsc1/Tsc2 models recapitulate seizures, gliosis, myelination defects, tumor biology, and pathway dependence; human models add BBB and cell-type-specific developmental readouts but may not fully recapitulate full cortical complexity or lifelong multisystem disease (zucco2018thegenerationand pages 40-44, zucco2018thegenerationand pages 35-40, sørensen2024singlecellprofilingof pages 1-3, brown2024rescueofimpaired pages 1-2, zimmer2020tuberoussclerosiscomplex pages 6-7) | NCBI Taxon: **10090** Mus musculus; **10116** Rattus norvegicus; **7955** Danio rerio; **7227** Drosophila melanogaster; model system names: patient-derived iPSC, cortical organoid, neurovascular unit chip |


*Table: This table condenses the most knowledge-base-ready facts for TSC1-related tuberous sclerosis complex, including identifiers, genetics, mechanisms, phenotypes, surveillance, treatment, and model systems. It emphasizes ontology-friendly mappings and quantitative evidence from consensus guidelines, recent studies, and active clinical trials.*

## 1. Disease information

### Definition

TSC1-related TSC is a congenital, autosomal-dominant, multisystem tumor-predisposition and neurodevelopmental disorder caused by loss of hamartin-mediated restraint of mTOR complex 1 (mTORC1). It produces hamartia and usually benign hamartomas in brain, skin, kidney, heart, lung, and retina, together with epilepsy and TSC-associated neuropsychiatric disorders (TAND). A useful recent abstract description is: **“Tuberous sclerosis complex (TSC) is an autosomal dominant neurodevelopmental disorder and multisystem disease caused by pathogenic DNA alterations in the TSC1 and TSC2 tumor suppressor genes.”** (Dufner-Almeida et al., published 3 November 2024; DOI: https://doi.org/10.3390/genes15111432). (dufneralmeida2024molecularandfunctional pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0008612, *tuberous sclerosis 1*; broader TSC is MONDO:0001734. Open Targets links MONDO:0008612 to **TSC1**, Ensembl ENSG00000165699. (OpenTargets Search: tuberous sclerosis 1,tuberous sclerosis complex-TSC1)
- **OMIM:** disease commonly indexed as **Tuberous sclerosis-1 / TSC1, OMIM 191100**; gene **TSC1, OMIM 605284**. The retrieved molecular paper explicitly confirms MIM 605284 for TSC1. (dufneralmeida2024molecularandfunctional pages 1-2)
- **MeSH:** Tuberous Sclerosis, **D014402**. (NCT05534672 chunk 1)
- **ICD-10-CM:** Q85.1, Tuberous sclerosis.
- **ICD-11:** LD2D.0, Tuberous sclerosis.
- **Orphanet:** ORPHA:805, Tuberous sclerosis complex.
- Common names: **tuberous sclerosis complex**, TSC, **Bourneville disease**, Bourneville–Pringle disease, epiloia, TSC1-related TSC.

The evidence is predominantly **aggregated disease-level evidence** from consensus guidelines, registries, cohorts, trials, and laboratory studies. The 2024 Japanese diagnostic-flow study is EHR-like administrative evidence derived from health-insurance claims, whereas TOSCA is an international disease registry. Individual case reports are informative for unusually mild or mosaic phenotypes but should not define population frequencies.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary causal factor

The necessary initiating cause is a heterozygous pathogenic or likely pathogenic **TSC1** alteration. TSC1 lies at 9q34.1, comprises 23 exons, and encodes hamartin. Hamartin stabilizes the TSC protein complex containing TSC2/tuberin and TBC1D7. The complex acts as a GAP for RHEB; its loss increases RHEB-GTP, mTORC1 kinase activity, S6K phosphorylation, anabolic metabolism, and cell growth. (zucco2018thegenerationand pages 35-40, dufneralmeida2024molecularandfunctional pages 1-2)

Lesions frequently follow tumor-suppressor **two-hit biology**: a constitutional or mosaic first hit is followed by somatic inactivation of the remaining allele. This is strongly supported in renal, cutaneous, pulmonary, and other tumors, although a demonstrable second hit is inconsistent in cortical tubers; haploinsufficiency, low-level cell-restricted second hits, and non-cell-autonomous signaling may all contribute to brain disease. (zucco2018thegenerationand pages 40-44, man2024thegeneticsof pages 8-9)

### Genetic risk factors

- A pathogenic germline TSC1 variant confers high, age-dependent penetrance but markedly variable expressivity.
- De novo and postzygotic mosaic variants are common contributors. Approximately two-thirds of all TSC is sporadic/de novo and one-third familial, although proportions vary by ascertainment. (man2024thegeneticsof pages 1-2)
- Higher accessible-tissue mosaic variant allele fraction sometimes correlates with more clinical features, but studies are inconsistent. One 2024 review reports median VAFs of 7.74% for mosaic TSC1 versus 1.93% for mosaic TSC2 and notes a proposed—but unvalidated—possibility that TSC1 VAF below 3% in blood/saliva may be less likely to satisfy clinical criteria. (man2024thegeneticsof pages 8-9)
- Compared with TSC2, TSC1 disease is, on average, milder, with later/smaller renal angiomyolipomas and less severe epilepsy; this is a population tendency, not a reliable individual prognosis. (pratico2025geneticscreeningof pages 8-9, kingswood2020renalmanifestationsof pages 1-2)
- No reproducibly validated modifier gene currently supports routine clinical risk prediction. Variation in second-hit timing, lineage, tissue distribution, variant type, residual complex function, and mosaic fraction likely explains substantial variability.

### Environmental and lifestyle factors

There is no established toxin, infection, diet, occupation, smoking exposure, or lifestyle behavior that causes Mendelian TSC1-related TSC. Environmental factors instead modify complications:

- Smoking and exogenous estrogen are clinically relevant concerns in pulmonary LAM; patients should avoid smoking, and estrogen-containing therapy requires individualized pulmonary assessment.
- Pregnancy may accelerate angiomyolipoma or LAM-related risk through hormonal and hemodynamic effects; this is complication modification, not disease causation.
- CYP3A4/P-glycoprotein inducers or inhibitors, infections, surgery, diet, and adherence alter mTOR-inhibitor exposure and safety.
- Sleep deprivation, fever, and missed medication can lower seizure threshold but do not create TSC lesions.

No proven **genetic protective allele** or environmental intervention prevents TSC after conception. Lower mosaic burden and TSC1 rather than TSC2 genotype are associated with milder average expression, but are not actionable protective factors. The strongest practical “protection” is secondary prevention through surveillance and early treatment.

## 3. Phenotypes

### Neurologic and neurodevelopmental

- **Epilepsy**—symptom/clinical sign; usually infancy or early childhood, episodic and often progressive toward drug resistance. Consensus data indicate focal seizures or epileptic spasms in **63–78% of infants**. In a TSC1-specific Sicilian cohort, epilepsy occurred in **64.5%**, with mean onset 35.4 months; 35% were drug resistant. Suggested HPO: Seizure, Focal-onset seizure, Epileptic spasm, Drug-resistant epilepsy. (pratico2025geneticscreeningof pages 3-4, northrup2021updatedinternationaltuberous pages 10-14)
- **Cortical tubers and radial migration lines**—congenital imaging/pathology signs, structurally stable but epileptogenic consequences evolve. TSC1 cohort frequencies were 67.8% for cortical tubers and 51.6% for subependymal nodules. HPO: Cortical tuber, Radial migration line, Subependymal nodule. (pratico2025geneticscreeningof pages 3-4)
- **SEGA**—usually childhood/adolescence; may enlarge and cause hydrocephalus, headache, vomiting, visual change, or behavioral deterioration. Reported in up to 24% in broad TSC cohorts. HPO: Subependymal giant cell astrocytoma, Hydrocephalus. (cockerell2023effectivenessandsafety pages 1-2)
- **TAND**—behavioral, psychiatric, intellectual, academic, neuropsychological, and psychosocial abnormalities, collectively affecting approximately 90% across TSC literature. In the cited TSC1 cohort, ASD was 12.9%; cognition was normal in 51.6% and severely impaired in 16.1%. Severity ranges from subtle school difficulties to profound disability. Suggested HPO: Intellectual disability, Autism, Attention deficit–hyperactivity disorder, Anxiety, Depressive disorder, Sleep abnormality, Aggressive behavior. (pratico2025geneticscreeningof pages 3-4, singh2023treatmentresistantepilepsyand pages 1-3, northrup2021updatedinternationaltuberous pages 10-14)
- **White-matter/hypomyelination abnormalities**—imaging and tissue sign; associated with altered neural connectivity, cognition, and ASD. Both oligodendrocyte-autonomous mTOR dysregulation and abnormal neuron–glia signaling are implicated. HPO: Abnormal cerebral white matter morphology, Hypomyelination. (zimmer2020tuberoussclerosiscomplex pages 6-7)

### Renal

- **Renal angiomyolipoma (AML)**—imaging/structural manifestation, commonly bilateral and multiple; prevalence and size rise with age. TOSCA recorded AML in **1,062/2,211 (48%)**, median diagnosis age 13 years. Females had more lesions, lesions >3 cm, growing lesions, and interventions. TSC1 lesions arose later and were smaller/less often growing on average, but by age 40 the proportion needing intervention did not differ clearly from TSC2. HPO: Renal angiomyolipoma, Renal hemorrhage. (kingswood2020renalmanifestationsof pages 1-2)
- **Renal cysts, hypertension, declining GFR/CKD**, and uncommon renal-cell carcinoma are important lifelong complications. HPO: Renal cyst, Hypertension, Chronic kidney disease, Renal cell carcinoma.

### Skin, dental, eye, heart, and lung

- **Hypomelanotic macules** may be congenital; shagreen patches, fibrous cephalic plaques, facial angiofibromas, and ungual fibromas appear from childhood onward and may progress. HPO terms: Hypopigmented skin macule, Facial angiofibroma, Shagreen patch, Ungual fibroma, Fibrous cephalic plaque.
- **Dental enamel pits and intraoral fibromas** are usually chronic signs. HPO: Dental enamel pits, Oral fibroma.
- **Retinal astrocytic hamartoma and achromic retinal patch** are often asymptomatic/stable but can impair vision. HPO: Retinal hamartoma, Retinal hypopigmentation.
- **Cardiac rhabdomyoma** is often prenatal/neonatal, may obstruct flow or cause arrhythmia, and usually regresses. In a Japanese claims cohort diagnosed before age two, rhabdomyoma was the most frequent initial manifestation, at 54.8%. HPO: Cardiac rhabdomyoma, Cardiac arrhythmia. (man2024thegeneticsof pages 1-2)
- **TSC-LAM**—progressive cystic lung disease, predominantly in adult females. It occurs in about **30–40% of adult females** with TSC; pneumothorax occurs in up to 70% of patients with LAM. HPO: Lymphangioleiomyomatosis, Cystic lung disease, Pneumothorax, Dyspnea, Chylous effusion. (jansen2020burdenofillness pages 1-2)
- **Multifocal micronodular pneumocyte hyperplasia** is usually stable and clinically mild. HPO: Multifocal micronodular pneumocyte hyperplasia.

### Quality-of-life impact

TOSCA’s 143-person QoL substudy found education/career impairment in 42.1% of patients, family-life/social/work effects reported by 76.5% of caregivers, pain/discomfort in 35%, and anxiety/depression in 43.4%. Only 36.8% of adults described a smooth pediatric-to-adult transition. (jansen2020burdenofillness pages 1-2)

A 2024 German matched study found adults with TSC epilepsy had EQ-5D-3L utility 0.705 and VAS 0.577, 60% unemployment, and markedly higher direct and productivity costs than matched idiopathic generalized or focal epilepsy groups. These burden estimates apply to TSC epilepsy overall, not specifically TSC1.

## 4. Genetic and molecular information

### Gene and variant classes

- **TSC1:** HGNC symbol TSC1; Ensembl ENSG00000165699; OMIM 605284; chromosome 9q34.1; protein hamartin, RefSeq NP_000359.1. (OpenTargets Search: tuberous sclerosis 1,tuberous sclerosis complex-TSC1, dufneralmeida2024molecularandfunctional pages 1-2)
- Disease mechanism: **loss of function**, primarily haploinsufficiency plus lesion-specific second hit.
- Pathogenic classes: nonsense, frameshift, canonical splice, exon/multiexon deletion, whole-gene deletion, duplications disrupting the reading frame, deep-intronic splice variants, and functionally established missense/in-frame variants.
- A TSC1-specific cohort reported intragenic deletions 48.4%, nonsense 38.7%, missense 9.6%, and duplication 3.2%, but this regional sample should not be treated as a universal spectrum. (pratico2025geneticscreeningof pages 3-4)
- Pathogenic TSC1 alleles are individually rare and generally absent or at extremely low frequency in gnomAD. A population frequency incompatible with this rare, highly penetrant disorder argues against pathogenicity.
- Germline, constitutional mosaic, and tissue-restricted somatic variants occur. Germline variants permit vertical transmission; mosaic variants may be missed in blood and still involve gonads.

A 2024 Brazilian molecular study detected pathogenic TSC1/TSC2 alterations in **106/116 (91%)** clinically definite cases: 18 TSC1 (17%) and 88 TSC2 (83%); 35 were novel. Its abstract states: **“Functional assessment can help establish variant pathogenicity and is a useful adjunct to DNA analysis.”** (dufneralmeida2024molecularandfunctional pages 1-2)

### Variant classification

Classification should follow ACMG/AMP criteria with TSC-specific evidence: predicted null consequence, segregation/de novo status, rarity, RNA evidence, copy-number evidence, and validated functional demonstration of impaired TSC complex suppression of mTORC1. A VUS is **not** a molecular diagnostic criterion. Functional assays are particularly valuable for missense, in-frame, and splice-region changes. (rosengren2020mutationalanalysisof pages 8-9, dufneralmeida2024molecularandfunctional pages 1-2)

### Mosaicism, chromosomal abnormalities, and epigenetics

Conventional testing is negative in 10–15% of clinically definite cases. High-depth sequencing can uncover mosaic variants; RNA analysis can identify deep-intronic splice defects. A negative blood test does not exclude TSC. Mosaic cases average fewer features, but can develop any manifestation and can transmit a non-mosaic variant. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 8-9, northrup2021updatedinternationaltuberous pages 10-14)

Large TSC1 deletions are uncommon but detectable by deletion/duplication analysis. Karyotyping has low yield. Unlike the TSC2/PKD1 contiguous-gene deletion syndrome at 16p13.3, there is no common TSC1 contiguous-gene syndrome. No validated disease-defining methylation episignature or epigenetic test is in routine use; reported chromatin changes are mainly downstream of altered metabolism/mTOR signaling.

## 5. Environmental information

TSC1-related TSC is not infectious or environmentally acquired and has no zoonotic or transmissible component. No causal bacteria, virus, fungus, parasite, radiation, occupational exposure, alcohol exposure, dietary pattern, or pollutant has been established. Clinically relevant modifiers include tobacco exposure in pulmonary disease, estrogen/pregnancy in LAM and AML, seizure precipitants, and drug–drug interactions during mTOR inhibition. The guideline specifically directs clinicians to inquire about tobacco exposure and pulmonary symptoms in adults. (northrup2021updatedinternationaltuberous pages 40-43)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** germline or mosaic TSC1 loss-of-function variant.
2. **Protein-complex defect:** reduced/unstable hamartin compromises TSC1–TSC2–TBC1D7 complex activity.
3. **Small-GTPase signaling:** inadequate TSC2 GAP activity leaves RHEB predominantly GTP-bound.
4. **Core pathway:** constitutive lysosome-associated mTORC1 activation.
5. **Downstream processes:** increased S6K/4E-BP-dependent translation, ribosome and lipid/nucleotide biosynthesis, cellular hypertrophy/proliferation; suppression of autophagy and lysosome biogenesis; feedback inhibition of PI3K–AKT; altered mitochondrial, synaptic, and myelination programs.
6. **Cell/tissue outcomes:** dysplastic/cytomegalic neurons, reactive astrocytes, abnormal neuronal migration and connectivity, impaired oligodendrocyte maturation, smooth-muscle-like PEComas/AML and LAM cells, and hamartoma formation.
7. **Clinical outcomes:** epilepsy/TAND, SEGA, renal AML/CKD/hemorrhage, skin lesions, cardiac rhabdomyoma, and pulmonary LAM. (zucco2018thegenerationand pages 35-40, dufneralmeida2024molecularandfunctional pages 1-2, sørensen2024singlecellprofilingof pages 1-3, zimmer2020tuberoussclerosiscomplex pages 6-7)

Suggested GO terms include negative regulation of TORC1 signaling, regulation of small GTPase-mediated signal transduction, negative regulation of cell growth, macroautophagy, neuron migration, synapse organization, gliogenesis, myelination, mitochondrial respiration, fatty-acid metabolic process, and blood–brain barrier maintenance. Relevant compartments are lysosomal membrane, lysosome, cytosol, TSC complex, and mTORC1 complex.

### Cellular and immune/tissue mechanisms

Neurons exhibit altered maturation, axonal/dendritic growth, excitability, AMPA signaling, and synaptic plasticity. Astrocyte Tsc1 deletion in mice causes astrogliosis and seizures, demonstrating non-neuronal causality. Oligodendrocyte/NG2-glia effects include abnormal maturation and hypomyelination. Microglial and cytokine activation is observed downstream in epileptogenic tissue, but TSC is not primarily autoimmune or immunodeficient. Renal and pulmonary lesions can undergo vascular remodeling, cystic destruction, hemorrhage, fibrosis, and loss of organ function. (zucco2018thegenerationand pages 40-44, zimmer2020tuberoussclerosiscomplex pages 6-7)

Suggested CL terms: glutamatergic neuron, GABAergic interneuron, astrocyte, oligodendrocyte, oligodendrocyte precursor/NG2 glial cell, microglial cell, endothelial cell, vascular smooth-muscle cell, renal epithelial cell, and pulmonary lymphangioleiomyomatosis cell.

### Molecular profiling and advanced technologies

A 2024 single-nucleus RNA-seq preprint of resected cortical tubers found that, despite disrupted lamination, virtually all neuronal subtypes and layer-associated transcriptional identities were retained. Principal neurons and layer 1–2 GABAergic neurons had the largest expression changes. Neuronal—but not glial—networks showed reduced mitochondrial respiration and a switch toward fatty-acid metabolism; neuron-specific AMPA-receptor signaling was nominated as an epileptogenic target. The authors’ abstract states: **“TSC neuronal, but not glial, networks exhibited massive metabolic reorganization with a reduction in mitochondrial respiration and a concomitant switch to fatty acid metabolism.”** This is important but remains non-peer-reviewed. (Sørensen et al., posted 31 October 2024; DOI: https://doi.org/10.1101/2024.10.31.621014). (sørensen2024singlecellprofilingof pages 1-3)

A peer-reviewed 2024 iPSC/microfluidic neurovascular-unit study found increased permeability in a TSC2-mutant BBB model, rescued by wild-type astrocytes or rapamycin. Although TSC2-based, it supports a shared mTOR-dependent neurovascular mechanism relevant to TSC1. Its abstract states: **“This can be rescued by wild type astrocytes or by treatment with rapamycin.”** (Brown et al., May 2024; DOI: https://doi.org/10.1186/s11689-024-09543-y). (brown2024rescueofimpaired pages 1-2)

No metabolomic, lipidomic, spatial-transcriptomic, or circulating biomarker signature is yet validated for clinical diagnosis or prognosis. Single-cell data are mechanistically promising but not diagnostic.

## 7. Anatomical structures affected

- **Brain:** cerebral cortex/cortical tubers, subcortical white matter/radial migration lines, subependymal zone/SEN, foramen of Monro/SEGA. UBERON suggestions: brain, cerebral cortex, cerebral white matter, lateral ventricle, subependymal zone.
- **Kidneys:** bilateral renal cortex/medulla and vasculature, with AML and cysts. UBERON: kidney, renal cortex, renal medulla.
- **Skin and appendages:** facial dermis, lumbosacral connective tissue, periungual tissue. UBERON: skin of face, nail, dermis.
- **Heart:** ventricular myocardium, usually prenatal rhabdomyoma. UBERON: heart, myocardium.
- **Lung/lymphatics:** diffuse bilateral lung parenchyma in LAM and pulmonary nodules in MMPH. UBERON: lung, lung parenchyma, lymphatic vessel.
- **Eye:** retina and optic disc. UBERON: retina.
- **Oral cavity and skeleton:** enamel, gingiva, sclerotic axial bone lesions.

Renal lesions are commonly bilateral; LAM is diffuse bilateral; brain lesions are multifocal and asymmetric rather than predictably lateralized.

## 8. Temporal development

TSC is lifelong and biologically begins prenatally. Cardiac rhabdomyomas may be detected in fetal life; hypomelanotic macules and cortical lesions are congenital. Epileptiform EEG abnormalities and seizures commonly emerge in the first two years, a critical window for neurodevelopment. Facial angiofibromas and neuropsychiatric manifestations evolve through childhood. SEGA risk is greatest in childhood through young adulthood. Renal AML burden rises through adolescence/adulthood, with TOSCA showing a peak of new AMLs at 18–40 years. LAM is primarily adult and female-predominant. (kingswood2020renalmanifestationsof pages 1-2, northrup2021updatedinternationaltuberous pages 10-14, northrup2021updatedinternationaltuberous pages 40-43)

The course is chronic and variable, combining stable congenital lesions, episodic seizures, and slowly progressive tumors/organ dysfunction. Cardiac rhabdomyomas often regress spontaneously; AML, SEGA, and angiofibromas frequently regress during mTOR inhibition but can regrow after withdrawal. There is no conventional disease staging system or spontaneous systemic remission.

## 9. Inheritance and population

Inheritance is autosomal dominant. Penetrance is high/near-complete with age, but expressivity ranges from subclinical adult disease to severe infantile epilepsy and multiorgan involvement. Each child of an individual with a constitutional heterozygous variant has a 50% transmission risk. Mosaic parental transmission risk is below 50% but cannot be inferred reliably from blood VAF because gonadal involvement may differ. Apparent unaffected parents can have low-level somatic/gonadal mosaicism. Anticipation is not established; consanguinity is not etiologically relevant; a “carrier” generally has the disorder because this is dominant. (man2024thegeneticsof pages 1-2, man2024thegeneticsof pages 8-9, northrup2021updatedinternationaltuberous pages 10-14)

Overall incidence is approximately 1 per 6,000–10,000 live births, with recent reviews spanning 1:5,800–1:13,520. No robust ethnic or geographic predilection exists; differences mainly reflect ascertainment. Both sexes inherit TSC equally, although renal AML severity and LAM are female-predominant. (man2024thegeneticsof pages 1-2, jansen2020burdenofillness pages 1-2, kingswood2020renalmanifestationsof pages 1-2)

## 10. Diagnostics

### Diagnostic criteria

A **definite molecular diagnosis** is established by a pathogenic TSC1 or TSC2 variant in normal tissue. A VUS is insufficient. A **definite clinical diagnosis** requires two major features or one major plus at least two minor features; possible TSC requires one major feature or at least two minor features. The 2021 criteria comprise 11 major and seven minor features, with “multiple cortical tubers and/or radial migration lines” replacing nonspecific “cortical dysplasia” and sclerotic bone lesions restored as a minor criterion. (northrup2021updatedinternationaltuberous pages 10-14, man2024thegeneticsof pages 8-9)

Major features include hypomelanotic macules, angiofibromas or fibrous cephalic plaque, ungual fibromas, shagreen patch, multiple retinal hamartomas, multiple cortical tubers/radial migration lines, subependymal nodules, SEGA, cardiac rhabdomyoma, LAM, and at least two renal AMLs. LAM plus AML alone is not sufficient for definite clinical diagnosis because both can co-occur in sporadic LAM.

### Baseline clinical tests

At diagnosis: brain MRI; awake/sleep EEG and prolonged video-EEG if needed; abdominal MRI, blood pressure, and GFR; dermatologic, dental, and dilated ophthalmic examination; ECG at all ages and echocardiography in pediatric patients; chest CT in adult females and symptomatic adult males, followed by PFT/6-minute walk testing if cystic disease is present. MRI is preferred for renal imaging because **25–30% of AMLs are fat-poor** and may be missed by ultrasound. (northrup2021updatedinternationaltuberous pages 10-14, northrup2021updatedinternationaltuberous pages 40-43)

### Genetic testing pathway

1. Parallel sequencing of **TSC1 and TSC2**, preferably on an NGS panel with high read depth.
2. Exon-level and whole-gene deletion/duplication analysis, such as validated NGS-CNV calling plus MLPA.
3. If negative with strong clinical suspicion: ultra-deep sequencing of blood and a second tissue such as saliva/buccal cells; affected-tissue sequencing when ethically available; genome sequencing for intronic/structural variants; RNA studies for splice effects.
4. Targeted familial-variant testing for relatives, prenatal diagnosis, or preimplantation testing once a familial variant is known.

WES can detect coding variants but may miss mosaic, intronic, and structural alterations. WGS improves noncoding/structural detection but still requires adequate depth and mosaic-aware analysis. CMA is useful mainly for large deletions; karyotype and FISH have little routine utility. Mitochondrial and repeat-expansion tests are not indicated. Current molecular methods identify a causal alteration in nearly 90% of definite TSC; the 2024 Brazilian study reached 91%. (dufneralmeida2024molecularandfunctional pages 1-2, northrup2021updatedinternationaltuberous pages 10-14)

### Differential diagnosis

Important alternatives include isolated cardiac rhabdomyoma, focal cortical dysplasia and other mTORopathies (DEPDC5/NPRL2/NPRL3, MTOR, RHEB, AKT3, PIK3CA, PTEN), Birt–Hogg–Dubé syndrome, neurofibromatosis, MEN1, sporadic LAM, sporadic AML/PEComa, polycystic kidney disease, and hypomelanosis of Ito. Distribution of characteristic skin findings, SEN/SEGA, multiple tubers/radial bands, bilateral AML, and molecular testing distinguish TSC.

### Surveillance

- Brain MRI every 1–3 years in asymptomatic patients younger than 25; more frequently for growing SEGA.
- EEG every six weeks through 12 months and every three months through 24 months in asymptomatic infants; thereafter based on clinical need.
- Abdominal MRI every 1–3 years lifelong; blood pressure and renal function at least annually.
- Annual TAND screen; formal assessments at infancy, preschool, school entry, adolescence, and early adulthood.
- Baseline CT at ≥18 years in females and symptomatic males; repeat CT/PFT according to LAM findings.
- Pediatric echo every 1–3 years until regression is established; ECG every 3–5 years.
- Annual skin and ophthalmic review; dental examination every six months. (northrup2021updatedinternationaltuberous pages 40-43, northrup2021updatedinternationaltuberous pages 43-45)

## 11. Outcomes and prognosis

No single genotype-specific five- or ten-year survival estimate is sufficiently robust. Survival is often near normal in mildly affected TSC1 disease, but population mortality exceeds that of the general population. Major causes include epilepsy/SUDEP, SEGA complications, renal hemorrhage/CKD, and pulmonary LAM. Neurologic disability is driven especially by early seizure onset, refractory epilepsy, tuber burden, and TAND. Renal risk rises with AML size/growth, hypertension, repeated embolization/nephrectomy, and cystic disease. Pulmonary prognosis depends on FEV1/DLCO decline, pneumothorax, and chylous complications.

Current surveillance and pre-emptive therapy have improved prognosis. In TOSCA’s renal substudy, no patient bled after starting an mTOR inhibitor, although the sample was too small for definitive comparative inference. (kingswood2020renalmanifestationsof pages 1-2)

Recovery is manifestation-specific: seizures can remit, cardiac tumors regress, and mTOR inhibitors shrink tumors, but the underlying germline disorder persists. Established intellectual disability or chronic organ damage is incompletely reversible.

## 12. Treatment

### Epilepsy and neurodevelopment

- **Vigabatrin** is first-line for TSC infantile spasms; if full-dose treatment fails after two weeks, ACTH, synthetic ACTH, or prednisolone is recommended. Serial ophthalmic monitoring is used because of retinal/visual-field toxicity. MAXO: antiseizure pharmacotherapy; ophthalmic monitoring. (northrup2021updatedinternationaltuberous pages 30-34, northrup2021updatedinternationaltuberous pages 40-43)
- Other seizure types receive syndrome-appropriate antiseizure drugs. A purified cannabidiol formulation and everolimus are approved for TSC-associated seizures. Ketogenic diet, vagus-nerve stimulation, and other neuromodulation are options in selected refractory cases.
- Epilepsy surgery should be evaluated after failure of approximately three appropriate medications, particularly with focal seizures and developmental regression, at an experienced TSC center. MAXO: resective epilepsy surgery, video-EEG monitoring, ketogenic dietary therapy. (northrup2021updatedinternationaltuberous pages 40-43)
- Behavioral, educational, speech/language, occupational, psychiatric, and sleep interventions should be tailored to the individual TAND profile; mTOR inhibitors are not established general TAND therapy.

### mTOR-targeted therapy

**Everolimus** is used for growing SEGA not requiring immediate surgery, asymptomatic growing renal AML >3 cm, and refractory focal-onset TSC seizures. **Sirolimus** is used particularly for clinically significant LAM and in some jurisdictions/indications. These are disease-pathway-directed but suppress rather than permanently correct mTOR activation.

EXIST trials reported ≥50% volume reduction in 35% of SEGA and 42% of renal AML recipients. In EXIST-3, ≥50% seizure reduction occurred in 28% at low exposure and 40% at high exposure. (cockerell2023effectivenessandsafety pages 1-2)

In a 2023 Norway/Denmark real-world series of 64 patients, 31% of 45 epilepsy patients achieved ≥50% seizure reduction; response was 46% in patients under 18 versus 14% in adults. Among 29 AML patients, 38% had ≥30% diameter reduction and 59% were stable after a mean 37 months. Three SEGAs shrank 71%, 43%, and 48%. Adverse events affected 95%; stomatitis/oral ulceration occurred in 63%, upper-respiratory infection in 38%, hypercholesterolemia in 41%, anemia in 30%, leukopenia in 25%, and grade 3–4 events in 36%. The abstract concludes: **“Close follow-up is needed for this group, especially for children and patients who may not be able to report adverse effects.”** (published December 2023; DOI: https://doi.org/10.1186/s13023-023-02982-1). (cockerell2023effectivenessandsafety pages 1-2)

Monitor CBC, renal/liver chemistry, fasting lipids/glucose, urine protein, infection, stomatitis, pulmonary symptoms, menstrual/ovarian effects, vaccination status, wound healing, and CYP3A/P-gp interactions. MAXO: mTOR-inhibitor therapy, therapeutic drug monitoring, laboratory surveillance. CHEBI entities: everolimus and sirolimus/rapamycin.

### Organ-specific procedures

- **SEGA:** urgent surgical resection for acute symptomatic obstruction/hydrocephalus; mTOR inhibitor or surgery for growing asymptomatic tumors; CSF diversion if necessary.
- **Renal AML:** mTOR inhibitor first-line for asymptomatic growing AML >3 cm; selective arterial embolization plus corticosteroids for acute hemorrhage. Avoid nephrectomy whenever possible. MAXO: arterial embolization, nephron-sparing surgery.
- **LAM:** sirolimus/everolimus for FEV1 <70% predicted, abnormal DLCO, air trapping/desaturation, rapid decline, or problematic chylous disease; pleural intervention for recurrent pneumothorax; transplant for end-stage disease. (northrup2021updatedinternationaltuberous pages 43-45)
- **Skin:** topical sirolimus, laser, or surgery for angiofibromas; surgery/laser for symptomatic fibromas. The completed phase 3 NPC-12Y study tested 0.2% topical sirolimus gel twice daily in 43 participants. (NCT05495425 chunk 1)
- **Cardiac:** observation for regressing asymptomatic rhabdomyoma; antiarrhythmic or surgical/mTOR-directed therapy for severe obstruction or refractory arrhythmia.

No CPIC/PharmGKB genotype-guided regimen specific to TSC1 is established. Treatment is phenotype- and pharmacokinetic-guided rather than TSC1-variant-guided.

### Recent and ongoing trials

- **NCT05104983 (TSC-STEPS):** phase 2, randomized, triple-blind sirolimus prevention trial in 64 seizure-free infants aged ≤6 months; primary outcome is time to seizure onset by 12 months. (NCT05104983 chunk 1)
- **NCT05534672 (RaRE-TS):** phase 3 randomized double-blind rapamycin versus placebo for drug-resistant TSC epilepsy, estimated n=200. (NCT05534672 chunk 1)
- **NCT02962414:** active long-term open-label everolimus safety rollover from EXIST-3, n=206, with follow-up approaching ten years. (NCT02962414 chunk 1)
- **NCT05323734 (TrustTSC):** completed phase 3 ganaxolone trial, n=129, in TSC-related epilepsy; results were first posted in 2025 and therefore were not available as a 2024 peer-reviewed outcome in the retrieved evidence. (NCT05323734 chunk 1)
- **NCT05059327:** completed phase 2 crossover study of the mGluR5 inhibitor basimglurant, n=61. (NCT05059327 chunk 1)
- **NCT05495425:** completed phase 3 topical sirolimus-gel study, n=43. (NCT05495425 chunk 1)

Gene replacement, CRISPR editing, ASO/siRNA, and cell therapy remain preclinical; no approved treatment corrects the TSC1 allele.

## 13. Prevention

### Primary prevention

There is no vaccine, lifestyle intervention, or medication that prevents a de novo TSC1 mutation. Reproductive options following molecular diagnosis include genetic counseling, targeted prenatal diagnosis, and IVF with preimplantation genetic testing. Because expressivity is unpredictable, genotype establishes risk but does not accurately predict severity.

### Secondary prevention

Cascade testing identifies mildly affected relatives. Fetal echocardiography can detect rhabdomyoma. Population newborn screening is not routine, but infants identified prenatally or through family testing should enter immediate MRI/EEG surveillance. Early control of electrographic and clinical seizures is a major prevention target. The guideline notes that pre-emptive vigabatrin may delay seizure onset in infants with epileptiform EEG, although evidence that it improves long-term neurodevelopment beyond very early treatment of clinical seizures is mixed. (northrup2021updatedinternationaltuberous pages 10-14)

### Tertiary prevention

Lifelong MRI, EEG, renal, pulmonary, cardiac, skin, eye, dental, and TAND surveillance seeks to prevent hydrocephalus, status epilepticus/SUDEP, renal hemorrhage/CKD, pneumothorax/respiratory failure, and avoidable disability. Smoking avoidance, blood-pressure control, renal preservation, infection prevention during immunosuppression, and treatment adherence are practical measures.

## 14. Other species and natural disease

Orthologous Tsc1 genes are highly conserved in mammals and other metazoans. Key taxa include human **NCBI Taxon 9606**, mouse **10090**, rat **10116**, zebrafish **7955**, and Drosophila **7227**. No well-established, prevalent naturally occurring veterinary syndrome equivalent to human germline TSC1-related multisystem TSC was identified in the retrieved evidence. Sporadic hamartomas in animals should not be assumed to constitute inherited TSC. The condition is noninfectious, non-zoonotic, and cannot transmit across species.

Conservation of the TSC–RHEB–mTOR axis supports comparative experiments, but organ spectrum, cortical architecture, lifespan, and requirement for second hits differ across species.

## 15. Model organisms and experimental systems

- **Conditional Tsc1 mice:** GFAP-Cre models reproduce astrogliosis, neuronal disorganization, seizures, and premature death; neuron-specific knockouts model hypertrophy, altered excitability, synaptic defects, and abnormal neuron–oligodendrocyte signaling; oligodendrocyte-lineage deletion perturbs myelination. These demonstrate cell-autonomous and non-cell-autonomous mechanisms and rapamycin responsiveness. Limitations include severe engineered biallelic loss and mouse–human cortical differences. (zucco2018thegenerationand pages 40-44, zimmer2020tuberoussclerosiscomplex pages 6-7)
- **Tsc1 heterozygous mice:** useful for learning, social behavior, synaptic plasticity, and haploinsufficiency, but generally do not reproduce the full human tumor burden.
- **Eker rat (Tsc2):** landmark spontaneous tumor model validating second-hit/LOH biology, especially renal tumors. It is mechanistically relevant to TSC1 but is not a Tsc1 model. (zucco2018thegenerationand pages 40-44)
- **Zebrafish and Drosophila:** permit rapid developmental, growth, neuronal, and modifier/drug screens. Their conserved TOR signaling is a strength; absence of a human-like cortex and incomplete multiorgan pathology are major limitations. (brown2024rescueofimpaired pages 1-2)
- **MEFs and engineered cell lines:** quantify p-S6K/p-S6/4E-BP1, complex stability, and RHEB/mTORC1 suppression for variant classification and drug screening. They lack tissue architecture.
- **Patient-derived iPSC neurons, astrocytes, oligodendrocytes, cardiomyocytes, and organoids:** preserve human genetic background and model lineage-specific differentiation, excitability, myelination, and mTOR dependence. Organoids add developmental cellular diversity but lack mature vasculature, immune integration, and lifelong organ interactions.
- **Microfluidic neurovascular-unit chips:** the 2024 BBB study showed TSC-mutant barrier leak rescued by wild-type astrocytes or rapamycin, offering a platform for lineage dissection and pharmacologic testing. (brown2024rescueofimpaired pages 1-2)
- **Resected human tubers with single-nucleus/spatial methods:** highest direct human relevance for cell-type states and epileptogenic networks, but confounded by end-stage disease, antiseizure treatment, surgery selection, and limited normal pediatric controls. The 2024 single-cell study explicitly cautioned that animal and iPSC-neuron models cannot fully reproduce human cortical neuronal complexity. (sørensen2024singlecellprofilingof pages 1-3)

## Overall expert assessment

TSC1-related TSC is best understood as a **developmental mosaic tumor-suppressor disorder and canonical mTORopathy**, not merely a collection of benign tumors. TSC1 generally predicts a milder average phenotype than TSC2, but individual management must never be relaxed on genotype alone: mosaic TSC1 can be clinically subtle, conventional blood testing can be negative, and severe neurologic, renal, or pulmonary disease remains possible. The strongest current real-world implementation is coordinated lifelong multidisciplinary surveillance coupled to early epilepsy treatment and lesion-directed mTOR inhibition. The most important 2023–2024 developments are higher-yield molecular diagnosis with functional variant assessment, genotype/mosaicism-aware sequencing, real-world long-term mTOR-inhibitor safety data, preventive sirolimus trials in infants, and single-cell evidence that metabolic and neuron-specific circuit remodeling—not simple loss of neuronal identity—may underlie cortical-tuber epileptogenesis. (dufneralmeida2024molecularandfunctional pages 1-2, sørensen2024singlecellprofilingof pages 1-3, cockerell2023effectivenessandsafety pages 1-2, man2024thegeneticsof pages 8-9, NCT05104983 chunk 1)

References

1. (OpenTargets Search: tuberous sclerosis 1,tuberous sclerosis complex-TSC1): Open Targets Query (tuberous sclerosis 1,tuberous sclerosis complex-TSC1, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (man2024thegeneticsof pages 1-2): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 52 citations.

3. (dufneralmeida2024molecularandfunctional pages 1-2): Luiz Gustavo Dufner-Almeida, Laís F. M. Cardozo, Mariana R. Schwind, Danielly Carvalho, Juliana Paula G. Almeida, Andrea Maria Cappellano, Thiago G. P. Alegria, Santoesha Nanhoe, Mark Nellist, Maria Rita Passos-Bueno, Silvana Chiavegatto, Nasjla S. Silva, Sérgio Rosemberg, Ana Paula A. Pereira, Sérgio Antônio Antoniuk, and Luciana A. Haddad. Molecular and functional assessment of tsc1 and tsc2 in individuals with tuberous sclerosis complex. Genes, 15:1432, Nov 2024. URL: https://doi.org/10.3390/genes15111432, doi:10.3390/genes15111432. This article has 11 citations.

4. (northrup2021updatedinternationaltuberous pages 10-14): Hope Northrup, Mary E. Aronow, E. Martina Bebin, John Bissler, Thomas N. Darling, Petrus J. de Vries, Michael D. Frost, Zoë Fuchs, Elizabeth S. Gosnell, Nishant Gupta, Anna C. Jansen, Sergiusz Jóźwiak, J. Chris Kingswood, Timothy K. Knilans, Francis X. McCormack, Ashley Pounders, Steven L. Roberds, David F. Rodriguez-Buritica, Jonathan Roth, Julian R. Sampson, Steven Sparagana, Elizabeth Anne Thiele, Howard L. Weiner, James W. Wheless, Alexander J. Towbin, Darcy A. Krueger, Nicholas M.P. Annear, Mary E. Aronow, Ute Bartels, E. Martina Bebin, Moncef Berhouma, John J. Bissler, Klemens Budde, Anna Byars, Harry Chugani, Edward W. Cowen, Peter B. Crino, Paolo Curatolo, Thomas N. Darling, Petrus de Vries, Daniel F. Dilling, David W. Dunn, Rosmary Ekong, Kevin C. Ess, David N. Franz, Michael Frost, Zoë D.B. Fuchs, Elizabeth Gosnell, Lisa Guay-Woodford, Nishant Gupta, Luciana Haddad, Anne Halbert, Adelaide A. Hebert, Elizabeth P. Henske, Gregory L. Holmes, Dena Hook, John Hulbert, Anna Jansen, Simon R. Johnson, Sergiusz Jóźwiak, Bryan King, J. Christopher Kingswood, Timothy K. Knilans, Mary Kay Koenig, Bruce Korf, Darcy A. Krueger, David J. Kwiatkowski, Francis X. McCormack, Joel Moss, David Mowat, Kate Mowrey, Rima Nabbout, Mark D. Nellist, Hope Northrup, Finbar O'Callaghan, Uday Patel, Ashley Pounders, E. Steve Roach, Steven L. Roberds, David Rodriguez-Buritica, Robb Romp, Jonathan Roth, Micaela Rozenberg, Stephen J. Ruoss, Mustafa Sahin, Julian Sampson, Joshua A. Samuels, Matthias Sauter, Catherine A. Smith, Keyomaurs Soltani, Steven Sparagana, Shoba Srivastava, Clare Stuart, Joyce M.C. Teng, Elizabeth A. Thiele, Alexander J. Towbin, Andrew Trout, Agnies van Eeghen, Stephanie Vanclooster, Henry Z. Wang, Mari Wataya-Kaneda, Howard L. Weiner, James W. Wheless, Patricia Witman, Tim Wright, Joyce Y. Wu, and Lisa Young. Updated international tuberous sclerosis complex diagnostic criteria and surveillance and management recommendations. Pediatric Neurology, 123:50-66, Oct 2021. URL: https://doi.org/10.1016/j.pediatrneurol.2021.07.011, doi:10.1016/j.pediatrneurol.2021.07.011. This article has 832 citations and is from a peer-reviewed journal.

5. (jansen2020burdenofillness pages 1-2): Anna C. Jansen, Stephanie Vanclooster, Petrus J. de Vries, Carla Fladrowski, Guillaume Beaure d'Augères, Tom Carter, Elena Belousova, Mirjana P. Benedik, Vincent Cottin, Paolo Curatolo, Maria Dahlin, Lisa D'Amato, José C. Ferreira, Martha Feucht, Christoph Hertzberg, Sergiusz Jozwiak, John A. Lawson, Alfons Macaya, Ruben Marques, Rima Nabbout, Finbar O'Callaghan, Jiong Qin, Valentin Sander, Matthias Sauter, Seema Shah, Yukitoshi Takahashi, Renaud Touraine, Sotiris Youroukos, Bernard Zonnenberg, and J. Chris Kingswood. Burden of illness and quality of life in tuberous sclerosis complex: findings from the tosca study. Frontiers in Neurology, Aug 2020. URL: https://doi.org/10.3389/fneur.2020.00904, doi:10.3389/fneur.2020.00904. This article has 50 citations and is from a peer-reviewed journal.

6. (man2024thegeneticsof pages 8-9): Alice Man, Matteo Di Scipio, Shan Grewal, Yujin Suk, Elisabetta Trinari, Resham Ejaz, and Robyn Whitney. The genetics of tuberous sclerosis complex and related mtoropathies: current understanding and future directions. Genes, 15:332, Mar 2024. URL: https://doi.org/10.3390/genes15030332, doi:10.3390/genes15030332. This article has 52 citations.

7. (pratico2025geneticscreeningof pages 3-4): Andrea Domenico Praticò, Claudia Di Napoli, Stefania Salafia, Edoardo Dammino, Maria Piccione, Francesco Calì, Renato Scifo, Michele Vecchio, Andrea Zonta, Maria Bonsignore, Maurizio Elia, Manuela Lo Bianco, Agata Polizzi, and Martino Ruggieri. Genetic screening of tuberous sclerosis complex in sicily with a focus on neurological manifestations. Scientific Reports, Jun 2025. URL: https://doi.org/10.1038/s41598-025-04718-6, doi:10.1038/s41598-025-04718-6. This article has 3 citations and is from a peer-reviewed journal.

8. (singh2023treatmentresistantepilepsyand pages 1-3): Avantika Singh, Aristides Hadjinicolaou, Jurriaan M Peters, and Catherine L Salussolia. Treatment-resistant epilepsy and tuberous sclerosis complex: treatment, maintenance, and future directions. Neuropsychiatric Disease and Treatment, 19:733-748, Apr 2023. URL: https://doi.org/10.2147/ndt.s347327, doi:10.2147/ndt.s347327. This article has 23 citations and is from a peer-reviewed journal.

9. (kingswood2020renalmanifestationsof pages 1-2): J. Chris Kingswood, Elena Belousova, Mirjana P. Benedik, Tom Carter, Vincent Cottin, Paolo Curatolo, Maria Dahlin, Lisa D'Amato, Guillaume Beaure d'Augères, Petrus J. de Vries, José C. Ferreira, Martha Feucht, Carla Fladrowski, Christoph Hertzberg, Sergiusz Jozwiak, John A. Lawson, Alfons Macaya, Ruben Marques, Rima Nabbout, Finbar O'Callaghan, Jiong Qin, Valentin Sander, Seema Shah, Yukitoshi Takahashi, Renaud Touraine, Sotiris Youroukos, Bernard Zonnenberg, Anna C. Jansen, and Matthias Sauter. Renal manifestations of tuberous sclerosis complex: key findings from the final analysis of the tosca study focussing mainly on renal angiomyolipomas. Frontiers in Neurology, Sep 2020. URL: https://doi.org/10.3389/fneur.2020.00972, doi:10.3389/fneur.2020.00972. This article has 75 citations and is from a peer-reviewed journal.

10. (NCT05495425 chunk 1):  Clinical Study of NPC-12Y Gel in Patients With Skin Lesions Associated With TSC. Nobelpharma. 2022. ClinicalTrials.gov Identifier: NCT05495425

11. (zucco2018thegenerationand pages 35-40): Avery J. Zucco. The generation and characterization of a human induced pluripotent stem cell model for the tuberous sclerosis complex. ArXiv, Jan 2018. URL: https://doi.org/10.7282/t3-9ahy-yx47, doi:10.7282/t3-9ahy-yx47. This article has 0 citations.

12. (sørensen2024singlecellprofilingof pages 1-3): Frederik Nørby Friis Sørensen, Tin Luka Petanjek, Mirte Scheper, Rasmus Rydbirk, Irina Korshunova, Jasper Anink, Angelika Mühlebner, James D. Mills, Zdravko Petanjek, Eleonora Aronica, and Konstantin Khodosevich. Single-cell profiling of cortical tubers in tuberous sclerosis complex shows molecular structure preservation and massive reorganization of metabolism. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.31.621014, doi:10.1101/2024.10.31.621014. This article has 4 citations.

13. (brown2024rescueofimpaired pages 1-2): Jacquelyn A. Brown, Shannon L. Faley, Monika Judge, Patricia Ward, Rebecca A. Ihrie, Robert Carson, Laura Armstrong, Mustafa Sahin, John P. Wikswo, Kevin C. Ess, and M. Diana Neely. Rescue of impaired blood-brain barrier in tuberous sclerosis complex patient derived neurovascular unit. Journal of Neurodevelopmental Disorders, May 2024. URL: https://doi.org/10.1186/s11689-024-09543-y, doi:10.1186/s11689-024-09543-y. This article has 4 citations and is from a peer-reviewed journal.

14. (zimmer2020tuberoussclerosiscomplex pages 6-7): Till S. Zimmer, Diede W. M. Broekaart, Victoria-Elisabeth Gruber, Erwin A. van Vliet, Angelika Mühlebner, and Eleonora Aronica. Tuberous sclerosis complex as disease model for investigating mtor-related gliopathy during epileptogenesis. Frontiers in Neurology, Sep 2020. URL: https://doi.org/10.3389/fneur.2020.01028, doi:10.3389/fneur.2020.01028. This article has 59 citations and is from a peer-reviewed journal.

15. (northrup2021updatedinternationaltuberous pages 40-43): Hope Northrup, Mary E. Aronow, E. Martina Bebin, John Bissler, Thomas N. Darling, Petrus J. de Vries, Michael D. Frost, Zoë Fuchs, Elizabeth S. Gosnell, Nishant Gupta, Anna C. Jansen, Sergiusz Jóźwiak, J. Chris Kingswood, Timothy K. Knilans, Francis X. McCormack, Ashley Pounders, Steven L. Roberds, David F. Rodriguez-Buritica, Jonathan Roth, Julian R. Sampson, Steven Sparagana, Elizabeth Anne Thiele, Howard L. Weiner, James W. Wheless, Alexander J. Towbin, Darcy A. Krueger, Nicholas M.P. Annear, Mary E. Aronow, Ute Bartels, E. Martina Bebin, Moncef Berhouma, John J. Bissler, Klemens Budde, Anna Byars, Harry Chugani, Edward W. Cowen, Peter B. Crino, Paolo Curatolo, Thomas N. Darling, Petrus de Vries, Daniel F. Dilling, David W. Dunn, Rosmary Ekong, Kevin C. Ess, David N. Franz, Michael Frost, Zoë D.B. Fuchs, Elizabeth Gosnell, Lisa Guay-Woodford, Nishant Gupta, Luciana Haddad, Anne Halbert, Adelaide A. Hebert, Elizabeth P. Henske, Gregory L. Holmes, Dena Hook, John Hulbert, Anna Jansen, Simon R. Johnson, Sergiusz Jóźwiak, Bryan King, J. Christopher Kingswood, Timothy K. Knilans, Mary Kay Koenig, Bruce Korf, Darcy A. Krueger, David J. Kwiatkowski, Francis X. McCormack, Joel Moss, David Mowat, Kate Mowrey, Rima Nabbout, Mark D. Nellist, Hope Northrup, Finbar O'Callaghan, Uday Patel, Ashley Pounders, E. Steve Roach, Steven L. Roberds, David Rodriguez-Buritica, Robb Romp, Jonathan Roth, Micaela Rozenberg, Stephen J. Ruoss, Mustafa Sahin, Julian Sampson, Joshua A. Samuels, Matthias Sauter, Catherine A. Smith, Keyomaurs Soltani, Steven Sparagana, Shoba Srivastava, Clare Stuart, Joyce M.C. Teng, Elizabeth A. Thiele, Alexander J. Towbin, Andrew Trout, Agnies van Eeghen, Stephanie Vanclooster, Henry Z. Wang, Mari Wataya-Kaneda, Howard L. Weiner, James W. Wheless, Patricia Witman, Tim Wright, Joyce Y. Wu, and Lisa Young. Updated international tuberous sclerosis complex diagnostic criteria and surveillance and management recommendations. Pediatric Neurology, 123:50-66, Oct 2021. URL: https://doi.org/10.1016/j.pediatrneurol.2021.07.011, doi:10.1016/j.pediatrneurol.2021.07.011. This article has 832 citations and is from a peer-reviewed journal.

16. (northrup2021updatedinternationaltuberous pages 43-45): Hope Northrup, Mary E. Aronow, E. Martina Bebin, John Bissler, Thomas N. Darling, Petrus J. de Vries, Michael D. Frost, Zoë Fuchs, Elizabeth S. Gosnell, Nishant Gupta, Anna C. Jansen, Sergiusz Jóźwiak, J. Chris Kingswood, Timothy K. Knilans, Francis X. McCormack, Ashley Pounders, Steven L. Roberds, David F. Rodriguez-Buritica, Jonathan Roth, Julian R. Sampson, Steven Sparagana, Elizabeth Anne Thiele, Howard L. Weiner, James W. Wheless, Alexander J. Towbin, Darcy A. Krueger, Nicholas M.P. Annear, Mary E. Aronow, Ute Bartels, E. Martina Bebin, Moncef Berhouma, John J. Bissler, Klemens Budde, Anna Byars, Harry Chugani, Edward W. Cowen, Peter B. Crino, Paolo Curatolo, Thomas N. Darling, Petrus de Vries, Daniel F. Dilling, David W. Dunn, Rosmary Ekong, Kevin C. Ess, David N. Franz, Michael Frost, Zoë D.B. Fuchs, Elizabeth Gosnell, Lisa Guay-Woodford, Nishant Gupta, Luciana Haddad, Anne Halbert, Adelaide A. Hebert, Elizabeth P. Henske, Gregory L. Holmes, Dena Hook, John Hulbert, Anna Jansen, Simon R. Johnson, Sergiusz Jóźwiak, Bryan King, J. Christopher Kingswood, Timothy K. Knilans, Mary Kay Koenig, Bruce Korf, Darcy A. Krueger, David J. Kwiatkowski, Francis X. McCormack, Joel Moss, David Mowat, Kate Mowrey, Rima Nabbout, Mark D. Nellist, Hope Northrup, Finbar O'Callaghan, Uday Patel, Ashley Pounders, E. Steve Roach, Steven L. Roberds, David Rodriguez-Buritica, Robb Romp, Jonathan Roth, Micaela Rozenberg, Stephen J. Ruoss, Mustafa Sahin, Julian Sampson, Joshua A. Samuels, Matthias Sauter, Catherine A. Smith, Keyomaurs Soltani, Steven Sparagana, Shoba Srivastava, Clare Stuart, Joyce M.C. Teng, Elizabeth A. Thiele, Alexander J. Towbin, Andrew Trout, Agnies van Eeghen, Stephanie Vanclooster, Henry Z. Wang, Mari Wataya-Kaneda, Howard L. Weiner, James W. Wheless, Patricia Witman, Tim Wright, Joyce Y. Wu, and Lisa Young. Updated international tuberous sclerosis complex diagnostic criteria and surveillance and management recommendations. Pediatric Neurology, 123:50-66, Oct 2021. URL: https://doi.org/10.1016/j.pediatrneurol.2021.07.011, doi:10.1016/j.pediatrneurol.2021.07.011. This article has 832 citations and is from a peer-reviewed journal.

17. (cockerell2023effectivenessandsafety pages 1-2): Ine Cockerell, Jakob Christensen, Christina E. Hoei-Hansen, Lotte Holst, Mikkel Grenaa Frederiksen, Aart Imran Issa-Epe, Bård Nedregaard, Ragnar Solhoff, Ketil Heimdal, Cecilie Johannessen Landmark, Caroline Lund, and Terje Nærland. Effectiveness and safety of everolimus treatment in patients with tuberous sclerosis complex in real-world clinical practice. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02982-1, doi:10.1186/s13023-023-02982-1. This article has 29 citations and is from a peer-reviewed journal.

18. (NCT02962414 chunk 1):  Roll-over Study to Collect and Assess Long-term Safety of Everolimus in Patients With TSC and Refractory Seizures Who Have Completed the EXIST-3 Study [CRAD001M2304] and Who Are Benefitting From Continued Treatment. Novartis Pharmaceuticals. 2017. ClinicalTrials.gov Identifier: NCT02962414

19. (NCT05534672 chunk 1): Katarzyna Kotulska. Placebo Controlled Study to Assess the Efficacy and Safety of Rapamycin in Drug Resistant Epilepsy Associated With Tuberous Sclerosis Complex. Katarzyna Kotulska. 2023. ClinicalTrials.gov Identifier: NCT05534672

20. (NCT05104983 chunk 1): Darcy Krueger. Stopping TSC Onset and Progression 2B: Sirolimus TSC Epilepsy Prevention Study. Darcy Krueger. 2021. ClinicalTrials.gov Identifier: NCT05104983

21. (NCT05323734 chunk 1):  Adjunctive GNX Treatment Compared With Placebo in Children and Adults With TSC-related Epilepsy. Marinus Pharmaceuticals. 2022. ClinicalTrials.gov Identifier: NCT05323734

22. (NCT05059327 chunk 1):  Basimglurant (NOE-101) in Children, Adolescents, and Young Adults With TSC. Noema Pharma AG. 2022. ClinicalTrials.gov Identifier: NCT05059327

23. (zucco2018thegenerationand pages 40-44): Avery J. Zucco. The generation and characterization of a human induced pluripotent stem cell model for the tuberous sclerosis complex. ArXiv, Jan 2018. URL: https://doi.org/10.7282/t3-9ahy-yx47, doi:10.7282/t3-9ahy-yx47. This article has 0 citations.

24. (pratico2025geneticscreeningof pages 8-9): Andrea Domenico Praticò, Claudia Di Napoli, Stefania Salafia, Edoardo Dammino, Maria Piccione, Francesco Calì, Renato Scifo, Michele Vecchio, Andrea Zonta, Maria Bonsignore, Maurizio Elia, Manuela Lo Bianco, Agata Polizzi, and Martino Ruggieri. Genetic screening of tuberous sclerosis complex in sicily with a focus on neurological manifestations. Scientific Reports, Jun 2025. URL: https://doi.org/10.1038/s41598-025-04718-6, doi:10.1038/s41598-025-04718-6. This article has 3 citations and is from a peer-reviewed journal.

25. (rosengren2020mutationalanalysisof pages 8-9): Thomas Rosengren, Santoesha Nanhoe, Luis Gustavo Dufner de Almeida, Bitten Schönewolf-Greulich, Lasse Jonsgaard Larsen, Caroline Amalie Brunbjerg Hey, Morten Dunø, Jakob Ek, Lotte Risom, Mark Nellist, and Lisbeth Birk Møller. Mutational analysis of tsc1 and tsc2 in danish patients with tuberous sclerosis complex. Scientific Reports, Jun 2020. URL: https://doi.org/10.1038/s41598-020-66588-4, doi:10.1038/s41598-020-66588-4. This article has 31 citations and is from a peer-reviewed journal.

26. (northrup2021updatedinternationaltuberous pages 30-34): Hope Northrup, Mary E. Aronow, E. Martina Bebin, John Bissler, Thomas N. Darling, Petrus J. de Vries, Michael D. Frost, Zoë Fuchs, Elizabeth S. Gosnell, Nishant Gupta, Anna C. Jansen, Sergiusz Jóźwiak, J. Chris Kingswood, Timothy K. Knilans, Francis X. McCormack, Ashley Pounders, Steven L. Roberds, David F. Rodriguez-Buritica, Jonathan Roth, Julian R. Sampson, Steven Sparagana, Elizabeth Anne Thiele, Howard L. Weiner, James W. Wheless, Alexander J. Towbin, Darcy A. Krueger, Nicholas M.P. Annear, Mary E. Aronow, Ute Bartels, E. Martina Bebin, Moncef Berhouma, John J. Bissler, Klemens Budde, Anna Byars, Harry Chugani, Edward W. Cowen, Peter B. Crino, Paolo Curatolo, Thomas N. Darling, Petrus de Vries, Daniel F. Dilling, David W. Dunn, Rosmary Ekong, Kevin C. Ess, David N. Franz, Michael Frost, Zoë D.B. Fuchs, Elizabeth Gosnell, Lisa Guay-Woodford, Nishant Gupta, Luciana Haddad, Anne Halbert, Adelaide A. Hebert, Elizabeth P. Henske, Gregory L. Holmes, Dena Hook, John Hulbert, Anna Jansen, Simon R. Johnson, Sergiusz Jóźwiak, Bryan King, J. Christopher Kingswood, Timothy K. Knilans, Mary Kay Koenig, Bruce Korf, Darcy A. Krueger, David J. Kwiatkowski, Francis X. McCormack, Joel Moss, David Mowat, Kate Mowrey, Rima Nabbout, Mark D. Nellist, Hope Northrup, Finbar O'Callaghan, Uday Patel, Ashley Pounders, E. Steve Roach, Steven L. Roberds, David Rodriguez-Buritica, Robb Romp, Jonathan Roth, Micaela Rozenberg, Stephen J. Ruoss, Mustafa Sahin, Julian Sampson, Joshua A. Samuels, Matthias Sauter, Catherine A. Smith, Keyomaurs Soltani, Steven Sparagana, Shoba Srivastava, Clare Stuart, Joyce M.C. Teng, Elizabeth A. Thiele, Alexander J. Towbin, Andrew Trout, Agnies van Eeghen, Stephanie Vanclooster, Henry Z. Wang, Mari Wataya-Kaneda, Howard L. Weiner, James W. Wheless, Patricia Witman, Tim Wright, Joyce Y. Wu, and Lisa Young. Updated international tuberous sclerosis complex diagnostic criteria and surveillance and management recommendations. Pediatric Neurology, 123:50-66, Oct 2021. URL: https://doi.org/10.1016/j.pediatrneurol.2021.07.011, doi:10.1016/j.pediatrneurol.2021.07.011. This article has 832 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Tuberous_Sclerosis_1-deep-research-falcon_artifacts/artifact-00.md)