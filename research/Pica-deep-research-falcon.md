---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-29T23:09:29.811139'
end_time: '2026-07-29T23:17:03.813060'
duration_seconds: 454.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pica
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Pica-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pica
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Pica** covering all of the
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
- **Disease Name:** Pica
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Pica** covering all of the
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


# Pica: comprehensive disease-characteristics report

## Executive summary

Pica is a feeding and eating disorder defined by persistent ingestion of non-nutritive, non-food substances for at least 1 month when the behavior is developmentally inappropriate and not part of a culturally or socially normative practice. Common forms include geophagia (earth/clay), pagophagia (ice), amylophagia (raw starch), trichophagia (hair), and ingestion of paper, paint, plaster, fabric, metal, or feces. It is a **behaviorally defined, heterogeneous syndrome**, not a single-gene metabolic disease. Its most reproducible associations are early childhood, pregnancy, autism spectrum disorder (ASD), intellectual/developmental disability (ID/DD), iron deficiency/anemia, sensory-seeking behavior, psychosocial adversity, and access to ingestible hazardous materials. Association does not establish direction of causation, particularly for iron deficiency.

The strongest recent longitudinal evidence is Papini et al. (online 2023; journal issue 2024), which found caregiver-reported pica behavior in 312/10,109 children (3.08%); prevalence was highest at 36 months (2.29%) and declined to 0.33% at 115 months. Of children ever reported to have pica, 19.55% had reports at two or more waves. The investigators explicitly cautioned that their measure did not establish all DSM criteria, including 1-month duration and cultural/developmental exclusions (https://doi.org/10.1002/eat.24111; published in *International Journal of Eating Disorders*, 2024) (papini2024prevalenceandrecurrence pages 1-3, papini2024prevalenceandrecurrence pages 11-13, papini2023prevalenceandrecurrence pages 7-11).

| domain | best-supported finding | key statistic/evidence | suggested ontology terms | evidence caveat |
|---|---|---|---|---|
| Definition / diagnosis | Pica is persistent ingestion of non-nutritive, non-food substances for at least 1 month, inappropriate to developmental stage and not culturally normative | DSM-style criteria summarized in review literature; ALSPAC authors note available cohort items did **not** capture full DSM criteria such as 1-month duration or cultural/developmental exclusion (leung2019picaacommon pages 3-4, papini2024prevalenceandrecurrence pages 11-13) | Candidate terms: pica; abnormal eating behavior; ingestion of nonfood substance; HPO candidate: pica | Much epidemiology measures **pica behavior** rather than confirmed DSM/ICD diagnosis |
| Autism / developmental disability epidemiology | Pica is substantially more common in children with ASD and in DD subgroups with ASD traits and/or ID | SEED study: ASD 23.2%, DD 8.4%, population controls 3.5%; ASD+ID 28.1%, ASD without ID 14.0%, DD with both ID and ASD characteristics 26.3%; adjusted prevalence ratios 4.4-8.0 (fields2021picaautismand pages 4-6, fields2021picaautismand pages 1-3) | Candidate terms: autism spectrum disorder; intellectual disability; developmental delay; feeding and eating disorder | Cross-sectional ascertainment via questionnaire item, not formal pica diagnosis; preschool-enriched sample limits generalization |
| General-childhood epidemiology | In general-population childhood cohorts, pica appears uncommon and tends to decline with age | ALSPAC: 312/10,109 children (3.08%) had reported pica behavior; highest at 36 months 2.29% (226 cases); recurrence at 2+ waves in 19.55%; prevalence declined to 0.33% by 115 months (papini2024prevalenceandrecurrence pages 1-3, papini2023prevalenceandrecurrence pages 7-11) | Candidate terms: childhood onset; recurrent behavior; pediatric feeding disorder phenotype | ALSPAC measured caregiver-reported behavior, not fully adjudicated diagnosis |
| Iron / anemia association | Iron deficiency and anemia are among the most consistently reported biological associations with pica | Review summarizes strong association with iron deficiency anemia; meta-analysis cited therein found pica cases had 2.35-fold greater odds of anemia; geophagia may reduce iron absorption and pagophagia is commonly linked with iron deficiency (leung2019picaacommon pages 2-3, leung2019picaacommon pages 3-4) | Candidate terms: iron deficiency anemia; geophagia; pagophagia; laboratory abnormality: low hemoglobin / iron deficiency | Evidence is largely associative and directionality remains unresolved; primary meta-analysis not directly extracted here |
| Complications | Major harms are gastrointestinal, toxicologic, infectious, dental, and nutritional | Reported complications include dental enamel erosion, infection/parasites, lead intoxication, anemia, choking, poisoning, intestinal obstruction/perforation, and other GI complications (papini2024prevalenceandrecurrence pages 1-3, fields2021picaautismand pages 1-3, leung2019picaacommon pages 3-4) | Candidate terms: intestinal obstruction; gastrointestinal perforation; lead poisoning; parasitic infection; dental enamel erosion; anemia | Complication frequency is poorly quantified; many reports derive from case series/reviews and severe presentations |
| Behavioral treatment | Best-supported management is behavioral assessment plus function-based intervention and environmental restriction of unsafe items | Fields et al. note empirical support for applied behavior analysis and functional analysis to identify sensory-seeking, automatic reinforcement, or social functions; prevention strategies include close monitoring, restricting access, childproof locks, and attention-occupying activities (fields2021picaautismand pages 6-8) | Candidate MAXO terms: behavioral therapy; applied behavior analysis; functional behavioral assessment; environmental modification; caregiver education | Evidence base is mainly specialized behavioral literature and case series; high-quality disorder-specific RCT evidence is limited in retrieved context |
| Genetics / omics gap | No established monogenic cause, susceptibility gene set, or validated omics signature is currently supported for pica as a primary psychiatric diagnosis | Retrieved disease-focused evidence emphasizes psychosocial, developmental, and micronutrient associations; no causal genes, pathogenic variants, transcriptomic, proteomic, metabolomic, or epigenomic biomarkers were identified in retrieved pica-specific sources (papini2024prevalenceandrecurrence pages 3-4, fields2021picaautismand pages 6-8) | Candidate terms: multifactorial disorder; gene-environment interaction; evidence gap | Absence here reflects current retrieved evidence, not proof of impossibility; comorbid neurodevelopmental disorders may have independent genetic etiologies |
| Animal-model gap | No standard experimental animal model for human psychiatric pica was identified in retrieved disease-focused literature | Veterinary literature notes pica-like behavior in animals, but retrieved search did not yield a validated translational model reproducing the human DSM/ICD syndrome (fields2021picaautismand pages 6-8) | Candidate terms: animal behavior abnormality; comparative phenotype; model-organism evidence gap | Important distinction between veterinary pica-like behaviors and a human psychiatric feeding/eating disorder construct |


*Table: This table condenses the most useful ontology-ready evidence for pica across diagnosis, epidemiology, complications, treatment, and evidence gaps. It is designed to support knowledge-base curation while clearly separating strong findings from limitations in the available literature.*

## 1. Disease information

### Definition and category

Pica is classified as a feeding/eating disorder. The core phenotype is repeated consumption of substances that have no conventional nutritional role. Normal infant mouthing, culturally sanctioned geophagia, and accidental foreign-body ingestion are not sufficient for the diagnosis. If pica occurs with another mental or medical disorder—including ASD, ID, schizophrenia, pregnancy, or iron deficiency—it should be diagnosed separately when sufficiently severe to warrant clinical attention (leung2019picaacommon pages 1-2, leung2019picaacommon pages 3-4).

**Common names and phenotype labels:** pica disorder, allotriophagy, non-food ingestion, dirt eating; geophagia/geophagy, pagophagia, amylophagia, trichophagia, lithophagia, and coprophagia describe substance-specific presentations rather than universally distinct diseases.

### Identifiers

| Resource | Identifier/label | Curation note |
|---|---|---|
| ICD-11 | **6B84, Pica** | Feeding or eating disorders chapter |
| ICD-10-CM | **F98.3, Pica of infancy and childhood**; adult coding may differ by national modification | Verify against the jurisdiction/version used by the knowledge base |
| DSM-5-TR | **307.52 (F98.3), Pica** | Psychiatric diagnostic designation |
| MeSH | **Pica**; commonly indexed as **D010842** | Confirm against current MeSH release before automated import |
| SNOMED CT | Pica / eating of non-food substances | Concept identifiers are edition-dependent |
| MONDO | Pica concept is represented in disease ontologies, but an exact MONDO accession was not verified in the retrieved primary literature | Do not populate an unverified numerical accession |
| OMIM/Orphanet | No established standalone Mendelian pica disorder entry was identified | Pica may be a phenotype of other genetic or developmental syndromes |

The evidence summarized here is primarily **aggregated disease-level literature**—birth cohorts, case-control studies, reviews, and case reports—not individual EHR-derived patient data. SEED used standardized assessments/questionnaires; ALSPAC used repeated caregiver reports (fields2021picaautismand pages 3-4, fields2021picaautismand pages 4-6).

## 2. Etiology, risk, and protective factors

Pica is best modeled as **multifactorial**.

* **Neurodevelopmental factors:** ASD, ID, and ASD-like characteristics are major risk markers. In SEED, pica prevalence was 23.2% in ASD, 8.4% in other DD, and 3.5% in population controls. Rates were 28.1% in ASD with ID, 14.0% in ASD without ID, and 26.3% in DD with both ID and ASD characteristics. Adjusted prevalence ratios for ASD-related groups were approximately 4.4–8.0 (Fields et al., *Pediatrics*, February 2021; https://doi.org/10.1542/peds.2020-0462) (fields2021picaautismand pages 4-6, fields2021picaautismand pages 1-3).
* **Micronutrient/hematologic factors:** Iron deficiency and anemia are consistently associated with pica, especially pagophagia and geophagia. A review citing a meta-analysis of 6,407 pica cases reported 2.35-fold higher odds of anemia. Zinc deficiency has also been reported, but evidence is less consistent. Reverse causality is plausible: deficiency may trigger craving, while clay/soil can bind iron or replace nutritious food and worsen deficiency (Leung & Hon, December 2019; https://doi.org/10.2174/1573396315666190313163530) (leung2019picaacommon pages 2-3, leung2019picaacommon pages 3-4).
* **Sensory and reinforcement factors:** Taste, texture, smell, oral stimulation, automatic reinforcement, inability to discriminate edible from inedible objects, and socially mediated reinforcement may maintain behavior. Sensory-processing difficulties in ASD provide a plausible pathway but are not a universal mechanism (papini2024prevalenceandrecurrence pages 3-4, fields2021picaautismand pages 6-8).
* **Psychosocial/environmental factors:** Lower socioeconomic status, neglect, emotional deprivation, family stress, maternal separation, migration/refugee status, and ready access to soil, peeling paint, or other hazardous material are reported risk correlates (leung2019picaacommon pages 2-3, leung2019picaacommon pages 1-2).
* **Physiologic states and comorbidity:** Pregnancy is a recognized context, as are sickle-cell disease, schizophrenia, obsessive-compulsive symptoms, depression, and other eating disturbances. These associations are heterogeneous and do not imply that each condition causes pica (leung2019picaacommon pages 2-3, leung2019picaacommon pages 1-2).

**Protective factors:** No validated genetic protective variant is known. Plausible environmental protection includes adequate iron and dietary nutrition, early developmental/behavioral screening, caregiver supervision, restricted access to hazardous items, lead-safe housing, and treatment of psychosocial stress. These are prevention/management principles rather than quantified causal protective effects (fields2021picaautismand pages 6-8).

**Gene–environment interaction:** No pica-specific G×E locus has been established. A reasonable but unproven model is that genetically influenced neurodevelopmental traits alter sensory processing, discrimination, or behavioral flexibility, while nutritional deficiency, stress, and environmental availability determine whether ingestion emerges and what is consumed.

## 3. Phenotypes

| Phenotype | Type and characteristics | Candidate ontology mapping |
|---|---|---|
| Persistent ingestion of non-food substances | Defining behavioral phenotype; ≥1 month for diagnosis; severity ranges from occasional ingestion to repetitive life-threatening behavior | HPO candidate: **Pica** / abnormal eating behavior |
| Geophagia, pagophagia, amylophagia, trichophagia | Substance-specific behavioral manifestations; may be chronic, episodic, or state-related | HPO/SNOMED substance-specific pica concepts where available |
| Oral sensory seeking/reduced edible–inedible discrimination | Behavioral/neurodevelopmental feature, especially in ASD/ID; frequency not established | HPO candidates: oral sensory seeking, abnormal eating behavior |
| Iron-deficiency anemia | Laboratory/systemic association or complication; not present in every patient | HPO: iron deficiency anemia, decreased hemoglobin, microcytic anemia |
| Abdominal pain, vomiting, constipation | Symptoms suggesting bezoar, obstruction, toxicity, or mucosal injury; episodic and exposure-dependent | HPO: abdominal pain, vomiting, constipation |
| Lead intoxication | Toxicologic complication of paint/contaminated-soil ingestion | HPO: increased blood lead concentration; lead poisoning |
| Dental erosion/injury | Physical complication of abrasive/hard substances | HPO: enamel abnormality/dental erosion |
| Choking, bezoar, obstruction, perforation | Acute-to-severe gastrointestinal/airway complications; uncommon but potentially fatal | HPO: choking, gastrointestinal foreign body, intestinal obstruction, GI perforation |
| Parasitic/infectious disease | Exposure-specific complication of contaminated earth or feces | HPO: parasitic infection; organism-specific terms |

Pica can begin after infancy, in childhood, during pregnancy, or in adulthood. In ALSPAC, it peaked at 36 months and generally declined; nine children showed fluctuating persistence from 36 to 115 months. ASD-associated rates remained approximately 10–14% across sampled ages, whereas population rates fell markedly. These findings indicate predominantly transient childhood behavior with a clinically important persistent subgroup (papini2023prevalenceandrecurrence pages 7-11).

Quality-of-life evidence is sparse and no validated pica-specific PROM is established. Reported impacts include constant supervision, restricted social participation, caregiver distress, disrupted family relationships, dental/medical burden, hospitalization, and surgery. The 2024 cohort paper cites weaker family relationships and reduced social contact, but quantitative EQ-5D/SF-36 estimates are unavailable (papini2024prevalenceandrecurrence pages 1-3).

## 4. Genetic and molecular information

No pica-specific **causal gene, HGNC locus, pathogenic germline or somatic variant, chromosomal abnormality, modifier gene, Mendelian inheritance pattern, penetrance estimate, carrier frequency, founder variant, or validated pharmacogenomic marker** is established in the retrieved disease-focused evidence. Therefore, assigning variants associated with ASD, ID, schizophrenia, or iron disorders directly to pica would be inappropriate.

Likewise, there is no validated pica-specific DNA-methylation signature, histone/chromatin alteration, transcriptomic profile, proteomic signature, metabolomic/lipidomic classifier, single-cell atlas, spatial-transcriptomic result, multi-omics model, or CRISPR/RNAi screen. WES, WGS, gene panels, CMA, karyotyping, FISH, mtDNA analysis, and repeat-expansion testing are **not diagnostic tests for isolated pica**. Genetic testing is appropriate only when developmental delay, dysmorphism, neurologic findings, congenital anomalies, or family history independently indicate an underlying genetic syndrome.

## 5. Environmental information

The clinically important environmental exposures are determined by the ingested substance:

* old paint, household dust, contaminated soil, imported remedies, pottery glaze, or occupational take-home dust → lead or other heavy metals;
* soil/feces → *Toxocara*, *Ascaris*, *Toxoplasma*, and other geographically specific pathogens;
* hair/fibers/plastic/metal → bezoar, obstruction, perforation, or toxicity;
* clay/starch → displacement of nutritious food, constipation, and impaired micronutrient absorption.

Dietary iron insufficiency and food insecurity may contribute. Smoking, alcohol, and exercise are not established primary pica determinants. Pica itself is not infectious or transmissible; infectious agents are complications of exposure, not causes of the psychiatric syndrome (leung2019picaacommon pages 2-3, leung2019picaacommon pages 3-4, fields2021picaautismand pages 1-3).

## 6. Mechanism and pathophysiology

There is no single established molecular pathway. Current evidence supports several partially overlapping causal chains:

1. **Micronutrient pathway:** inadequate intake/blood loss/increased requirement → iron depletion and anemia → altered appetite or sensory reward → craving/ingestion. Alternatively, soil/clay ingestion → iron binding, reduced absorption, or dietary displacement → worsening deficiency. Directionality remains unresolved (leung2019picaacommon pages 2-3).
2. **Neurodevelopmental-sensory pathway:** ASD/ID-associated sensory processing or poor edible–inedible discrimination → oral sensory seeking/non-food ingestion → reinforcement by texture/taste or stimulation → persistence (fields2021picaautismand pages 6-8).
3. **Behavioral pathway:** stress, low stimulation, attention contingencies, or automatic oral reinforcement → repeated ingestion → learned maintenance. Functional analysis is used because the maintaining consequence differs by patient (fields2021picaautismand pages 6-8).
4. **Downstream injury:** repeated exposure → toxicant absorption, infection, tooth damage, nutrient displacement, choking, or foreign-body accumulation → anemia, neurologic toxicity, bezoar, obstruction, ischemia, perforation, sepsis, or surgery (leung2019picaacommon pages 3-4, fields2021picaautismand pages 1-3).

Candidate GO mappings should be treated as broad process annotations, not demonstrated pica pathways: **sensory perception**, **feeding behavior**, **learning or memory**, **response to iron ion**, **intestinal absorption**, and **response to toxic substance**. Candidate cell types include CNS neurons involved in reward/feeding and intestinal epithelial cells, but no pica-specific affected cell population has been demonstrated. Protein dysfunction, immune dysregulation, apoptosis, autophagy, or canonical Wnt/MAPK/mTOR/PI3K-AKT abnormalities are not established mechanisms.

## 7. Anatomical structures affected

Pica has no fixed primary lesion. The defining behavior is generated within nervous-system/behavioral circuitry, but anatomy depends on exposure:

* **Digestive system:** oral cavity/teeth, esophagus, stomach, small and large intestine; UBERON candidates include mouth, tooth enamel, stomach, small intestine, colon.
* **Hematologic system:** blood and bone marrow consequences of iron deficiency or blood loss.
* **Nervous system:** secondary injury from lead or other neurotoxins; CNS involvement may also reflect a comorbid neurodevelopmental disorder.
* **Liver/kidney:** possible secondary toxicant injury.
* **Respiratory tract:** choking or aspiration.

No laterality is expected. No disease-specific subcellular compartment or GO Cellular Component term is justified.

## 8. Temporal development

Onset is usually insidious/repetitive rather than acute, although complications may present acutely. Developmentally normal mouthing must be distinguished from pica. In ALSPAC, prevalence fell from 2.29% at 36 months to 0.33% at 115 months; 61/312 affected children (19.55%) had pica at ≥2 waves. Autism and DD were associated with pica at every assessed wave from 36 to 115 months (papini2024prevalenceandrecurrence pages 1-3, papini2023prevalenceandrecurrence pages 7-11).

The course may be self-limited after correction of deficiency or pregnancy, or chronic/relapsing in ASD/ID and severe psychiatric illness. There is no formal staging system. Critical intervention windows are early childhood, pregnancy, emergence of anemia, and any onset of abdominal pain, vomiting, choking, neurologic symptoms, or suspected toxic exposure.

## 9. Inheritance and population epidemiology

No reliable global incidence per 100,000 person-years is available, partly because studies use different definitions and often measure behavior rather than DSM diagnosis. Contemporary estimates include:

* ALSPAC: 3.08% ever reported across five childhood waves; 2.29% at 36 months and 0.33% at 115 months (papini2024prevalenceandrecurrence pages 1-3, papini2023prevalenceandrecurrence pages 7-11).
* SEED preschool sample: 3.5% in population controls, 23.2% in ASD, and 8.4% in DD (fields2021picaautismand pages 4-6).
* Earlier studies summarized in the 2019 review varied enormously by population and ascertainment, including 27.8% in a 70-study pregnancy meta-analysis. Such estimates should not be pooled with confirmed diagnostic prevalence (leung2019picaacommon pages 2-3).

In ALSPAC, boys had higher reported prevalence than girls at age 9 (0.49% versus 0.16%), but pica does not have a universally established sex ratio. Geographic and ethnic variation is strongly confounded by cultural definitions, pregnancy, poverty, food insecurity, soil/paint exposure, and measurement. There is no established AD, AR, X-linked, mitochondrial, or polygenic inheritance model; anticipation, mosaicism, consanguinity, and carrier frequency are not applicable to isolated pica.

## 10. Diagnostics

### Clinical criteria

Diagnosis requires a careful interview establishing: (1) substances consumed; (2) frequency and ≥1-month duration; (3) developmental inappropriateness; (4) lack of cultural sanction; (5) access and context; and (6) clinical significance when another disorder or pregnancy is present. Caregiver observation is often necessary. A single questionnaire item identifies risk but does not establish diagnosis; ALSPAC could not assess all DSM requirements (papini2024prevalenceandrecurrence pages 11-13, fields2021picaautismand pages 3-4).

### Exposure-directed workup

* CBC, ferritin, serum iron, transferrin saturation/TIBC; consider reticulocytes and inflammatory markers when interpreting ferritin.
* Blood lead concentration when paint, dust, soil, pottery, imported products, or unexplained developmental/abdominal findings are relevant; test other metals according to exposure.
* Zinc and broader nutritional assessment when diet is restricted or malnutrition is suspected.
* Stool or pathogen-directed testing when contaminated soil/feces was ingested and epidemiology or symptoms support infection.
* Abdominal radiography for radiopaque material, obstruction, or constipation; ultrasound/CT/endoscopy as clinically indicated for bezoar, perforation, or unexplained pain/vomiting.
* Dental examination and developmental/psychiatric assessment, including ASD/ID, OCD-spectrum symptoms, psychosis, mood disorder, trauma, and functional behavioral assessment.

Reviews specifically recommend testing for anemia, lead poisoning, parasites, and imaging for gastrointestinal complications (leung2019picaacommon pages 2-3, leung2019picaacommon pages 3-4).

### Differential diagnosis

Exclude normal developmental mouthing, culturally sanctioned ingestion, accidental foreign-body ingestion, food insecurity without persistent non-food preference, ARFID, anorexia nervosa, rumination disorder, obsessive-compulsive behavior, psychosis/delusional ingestion, nonsuicidal self-injury, intentional poisoning, factitious disorder, dementia, Prader–Willi syndrome, and substance-specific behaviors such as trichotillomania with trichophagia. The distinction depends on motivation, duration, development, culture, and associated psychopathology.

No molecular biomarker, biopsy, EEG, PET/MRI signature, newborn screen, carrier screen, or population genetic screen exists for pica. The Pica, ARFID, and Rumination Disorder Interview (PARDI) can support structured assessment in children aged ≥2 years, but no available questionnaire captures every DSM criterion (papini2024prevalenceandrecurrence pages 10-11, papini2024prevalenceandrecurrence pages 11-13).

## 11. Outcome and prognosis

There are no meaningful pica-specific 5- or 10-year survival estimates. Mortality is uncommon but can occur through choking, poisoning, obstruction, perforation, sepsis, or severe toxic exposure. Morbidity ranges from minimal transient behavior to anemia, developmental neurotoxicity, parasitosis, dental injury, repeated hospitalization, and emergency surgery (leung2019picaacommon pages 3-4, fields2021picaautismand pages 1-3).

Prognosis is generally favorable for developmentally typical children when hazards are removed, deficiencies corrected, and discrimination/supervision established. Persistence is more likely where behavior is strongly automatically reinforced or accompanied by ASD/ID, severe psychiatric illness, continued stress, or continued access. Substance type, frequency, toxic burden, GI symptoms, iron status, developmental capacity, caregiver resources, and response to behavioral intervention are practical prognostic indicators. No validated molecular prognostic biomarker exists.

## 12. Treatment

No medication is approved specifically for pica, and no relevant pica-specific interventional trial was identified in the ClinicalTrials.gov search. Evidence is dominated by observational studies, single-case experimental designs, and specialist behavioral series rather than large randomized trials.

### Recommended stepped strategy

1. **Immediate safety/environmental control:** remove or lock away preferred hazardous items; repair peeling paint; increase supervision; alert school/daycare and all caregivers; provide safe competing activities/items. Candidate MAXO: environmental modification, caregiver education, safety monitoring (fields2021picaautismand pages 6-8).
2. **Medical correction:** treat iron deficiency with iron replacement and address bleeding/dietary causes; correct other demonstrated deficiencies rather than prescribing empirically. Treat lead toxicity, parasites, constipation, dental injury, or poisoning according to standard protocols. Candidate MAXO: laboratory monitoring, iron supplementation, toxicant removal/chelation where indicated, anti-infective therapy (leung2019picaacommon pages 2-3, leung2019picaacommon pages 3-4).
3. **Function-based behavioral treatment:** functional behavioral assessment/analysis followed by differential reinforcement, competing-stimulus approaches, response interruption/redirection or blocking, discrimination training, and caregiver generalization. Applied behavior analysis has the strongest disorder-specific empirical support, especially in ASD/ID, although evidence quality is mostly below RCT level. Candidate MAXO: behavioral therapy, applied behavior analysis, functional assessment (fields2021picaautismand pages 6-8).
4. **Psychological/psychiatric care:** CBT may be useful in cognitively able patients; treat comorbid OCD, psychosis, depression, or anxiety for their own indications. Antipsychotics, SSRIs, or other drugs should not be considered established pica pharmacotherapy.
5. **Intervention for complications:** endoscopic or surgical foreign-body/bezoar removal for obstruction, perforation, or non-passing hazardous objects. Candidate MAXO: diagnostic imaging, endoscopy, foreign-body removal, gastrointestinal surgery.

Pharmacogenomics, gene therapy, cell therapy, RNA therapeutics, targeted molecular therapy, and immunotherapy are not applicable based on current evidence.

## 13. Prevention

* **Primary:** adequate maternal/child nutrition; prevention and early treatment of iron deficiency; lead-safe housing; sanitation; safe storage/removal of ingestible hazards; developmentally appropriate enrichment and supervision.
* **Secondary:** ask directly about non-food ingestion in pregnancy, unexplained iron deficiency, ASD/ID, and recurrent abdominal/toxicologic presentations. Fields et al. recommend caregiver monitoring, restricting access, childproof locks, occupying activities, and communication among caregivers (fields2021picaautismand pages 6-8).
* **Tertiary:** repeated exposure review, laboratory monitoring where indicated, behavioral relapse plans, school/home coordination, and rapid evaluation of abdominal pain, vomiting, choking, or neurologic change.

Vaccination, antimicrobial prophylaxis, preimplantation testing, prenatal genetic diagnosis, carrier screening, and cascade genetic screening are not pica-prevention strategies.

## 14. Other species and natural disease

Pica-like or “depraved appetite” behavior occurs in cattle, dogs, cats, and other animals, often in association with nutritional imbalance, gastrointestinal disease, boredom, or behavioral disturbance. These are veterinary behavioral signs, not proof of a naturally occurring homolog of the human DSM/ICD psychiatric disorder. No pica-specific orthologous gene, breed ontology association, zoonotic transmission, or cross-species infectious mechanism is established. Human pica is not zoonotic.

## 15. Model organisms

No standardized mouse, rat, zebrafish, *Drosophila*, *C. elegans*, cell-line, organoid, iPSC, knockout, knock-in, transgenic, or humanized model recapitulates the complete human pica syndrome. Experimental consumption of kaolin by rodents is widely used as a proxy for nausea because rodents do not vomit; it should not be treated as a validated model of psychiatric pica. Relevant mechanisms are therefore studied indirectly through iron-deficiency models, sensory/reward paradigms, neurodevelopmental models, and behavioral reinforcement experiments. These models cannot reproduce the human developmental and cultural diagnostic exclusions.

## Evidence interpretation and current research gaps

The 2024 ALSPAC study is the major recent advance because it supplies repeated community-cohort measurements rather than only severe clinical cases. Its abstract reports: **“A total of 312 parents (3.08%) reported pica behaviors in their child”** and **“19.55% reported pica at least at two waves.”** It also concludes that children with DD or autism may benefit from screening between 36 and 115 months (https://doi.org/10.1002/eat.24111; December 2024 publication metadata) (papini2024prevalenceandrecurrence pages 1-3).

Fields et al. provide the strongest large preschool ASD/DD comparison. Their abstract reports that, versus 3.5% in population controls, prevalence was **“23.2%”** in ASD and **“8.4%”** in DD, reaching **“28.1%”** in ASD with ID (https://doi.org/10.1542/peds.2020-0462; February 2021) (fields2021picaautismand pages 4-6, fields2021picaautismand pages 1-3).

Major unresolved questions are: whether and how iron deficiency causes pica; development of validated multi-item diagnostic instruments; prospective adult and pregnancy trajectories; representative incidence and remission estimates; comparative effectiveness trials of behavioral components; standardized patient/caregiver quality-of-life measures; and molecular studies designed specifically around rigorously diagnosed pica. Current evidence does **not** support a pica-specific gene, protein, pathway, omics classifier, drug target, or animal model.

References

1. (papini2024prevalenceandrecurrence pages 1-3): Natalie M. Papini, Cynthia M. Bulik, Samuel J. R. A. Chawner, and Nadia Micali. Prevalence and recurrence of pica behaviors in early childhood within the alspac birth cohort. The International journal of eating disorders, 57:400-409, Dec 2024. URL: https://doi.org/10.1002/eat.24111, doi:10.1002/eat.24111. This article has 24 citations.

2. (papini2024prevalenceandrecurrence pages 11-13): Natalie M. Papini, Cynthia M. Bulik, Samuel J. R. A. Chawner, and Nadia Micali. Prevalence and recurrence of pica behaviors in early childhood within the alspac birth cohort. The International journal of eating disorders, 57:400-409, Dec 2024. URL: https://doi.org/10.1002/eat.24111, doi:10.1002/eat.24111. This article has 24 citations.

3. (papini2023prevalenceandrecurrence pages 7-11): Natalie M. Papini, Cynthia M. Bulik, Samuel JRA Chawner, and Nadia Micali. Prevalence and recurrence of pica behaviors in early childhood: findings from the alspac birth cohort. medRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.04.23290951, doi:10.1101/2023.06.04.23290951. This article has 5 citations.

4. (leung2019picaacommon pages 3-4): Alexander K.C. Leung and Kam Lun Hon. Pica: a common condition that is commonly missed - an update review. Dec 2019. URL: https://doi.org/10.2174/1573396315666190313163530, doi:10.2174/1573396315666190313163530. This article has 114 citations and is from a peer-reviewed journal.

5. (fields2021picaautismand pages 4-6): Victoria L. Fields, Gnakub N. Soke, Ann Reynolds, Lin H. Tian, Lisa Wiggins, Matthew Maenner, Carolyn DiGuiseppi, Tanja V.E. Kral, Kristina Hightshoe, and Laura A. Schieve. Pica, autism, and other disabilities. Pediatrics, Feb 2021. URL: https://doi.org/10.1542/peds.2020-0462, doi:10.1542/peds.2020-0462. This article has 98 citations and is from a highest quality peer-reviewed journal.

6. (fields2021picaautismand pages 1-3): Victoria L. Fields, Gnakub N. Soke, Ann Reynolds, Lin H. Tian, Lisa Wiggins, Matthew Maenner, Carolyn DiGuiseppi, Tanja V.E. Kral, Kristina Hightshoe, and Laura A. Schieve. Pica, autism, and other disabilities. Pediatrics, Feb 2021. URL: https://doi.org/10.1542/peds.2020-0462, doi:10.1542/peds.2020-0462. This article has 98 citations and is from a highest quality peer-reviewed journal.

7. (leung2019picaacommon pages 2-3): Alexander K.C. Leung and Kam Lun Hon. Pica: a common condition that is commonly missed - an update review. Dec 2019. URL: https://doi.org/10.2174/1573396315666190313163530, doi:10.2174/1573396315666190313163530. This article has 114 citations and is from a peer-reviewed journal.

8. (fields2021picaautismand pages 6-8): Victoria L. Fields, Gnakub N. Soke, Ann Reynolds, Lin H. Tian, Lisa Wiggins, Matthew Maenner, Carolyn DiGuiseppi, Tanja V.E. Kral, Kristina Hightshoe, and Laura A. Schieve. Pica, autism, and other disabilities. Pediatrics, Feb 2021. URL: https://doi.org/10.1542/peds.2020-0462, doi:10.1542/peds.2020-0462. This article has 98 citations and is from a highest quality peer-reviewed journal.

9. (papini2024prevalenceandrecurrence pages 3-4): Natalie M. Papini, Cynthia M. Bulik, Samuel J. R. A. Chawner, and Nadia Micali. Prevalence and recurrence of pica behaviors in early childhood within the alspac birth cohort. The International journal of eating disorders, 57:400-409, Dec 2024. URL: https://doi.org/10.1002/eat.24111, doi:10.1002/eat.24111. This article has 24 citations.

10. (leung2019picaacommon pages 1-2): Alexander K.C. Leung and Kam Lun Hon. Pica: a common condition that is commonly missed - an update review. Dec 2019. URL: https://doi.org/10.2174/1573396315666190313163530, doi:10.2174/1573396315666190313163530. This article has 114 citations and is from a peer-reviewed journal.

11. (fields2021picaautismand pages 3-4): Victoria L. Fields, Gnakub N. Soke, Ann Reynolds, Lin H. Tian, Lisa Wiggins, Matthew Maenner, Carolyn DiGuiseppi, Tanja V.E. Kral, Kristina Hightshoe, and Laura A. Schieve. Pica, autism, and other disabilities. Pediatrics, Feb 2021. URL: https://doi.org/10.1542/peds.2020-0462, doi:10.1542/peds.2020-0462. This article has 98 citations and is from a highest quality peer-reviewed journal.

12. (papini2024prevalenceandrecurrence pages 10-11): Natalie M. Papini, Cynthia M. Bulik, Samuel J. R. A. Chawner, and Nadia Micali. Prevalence and recurrence of pica behaviors in early childhood within the alspac birth cohort. The International journal of eating disorders, 57:400-409, Dec 2024. URL: https://doi.org/10.1002/eat.24111, doi:10.1002/eat.24111. This article has 24 citations.

## Artifacts

- [Edison artifact artifact-00](Pica-deep-research-falcon_artifacts/artifact-00.md)