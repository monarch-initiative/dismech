---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-12T10:35:09.794670'
end_time: '2026-08-12T10:45:16.970579'
duration_seconds: 607.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glomerulonephritis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Glomerulonephritis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glomerulonephritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Glomerulonephritis** covering all of the
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
- **Disease Name:** Glomerulonephritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Glomerulonephritis** covering all of the
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


# Glomerulonephritis: comprehensive disease-characteristics report

## Executive summary and scope

**Glomerulonephritis (GN) is not one disease but a heterogeneous group of disorders characterized by inflammation and immune-mediated injury of renal glomeruli.** Histologic patterns alone do not consistently identify cause; current expert thinking increasingly divides GN into **infection-related, autoimmune, alloimmune, autoinflammatory/complement-mediated, and monoclonal gammopathy-related** categories because this better links mechanism to treatment. Acute disease commonly produces hematuria, proteinuria, hypertension, edema, and reduced glomerular filtration; severe crescentic disease can cause rapidly progressive kidney failure. Kidney biopsy remains central because these clinical manifestations are nonspecific. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)

The principal evidence limitation is therefore conceptual: syndrome-level statements about a single causal gene, inheritance pattern, incidence, treatment, or prognosis are usually invalid. Those fields must be recorded by **etiologic subtype**.

A useful overview of the major mechanistic classes follows.

| Class / examples | Initiating cause | Biopsy / serologic signature | Key genes / pathways | Typical clinical course | Current mechanism-aligned treatment |
|---|---|---|---|---|---|
| **Infection-related GN** (post-streptococcal GN; bacterial/viral/parasitic infection-associated GN) | Infection-triggered glomerular injury via immune-complex deposition, direct glomerular cell damage, molecular mimicry, and/or superantigen effects; control of infection is central (subtype-specific) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, casuscelli2023autoimmunityandinfection pages 1-2) | Kidney biopsy required for subtype distinction in many cases; immune-complex/complement-associated patterns may be seen; supportive serologies depend on trigger (for example antistreptolysin O/anti-DNase B in post-streptococcal disease) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, casuscelli2023autoimmunityandinfection pages 1-2) | Innate immunity, immune complexes, complement activation; immunopathogenesis-based GN framework classifies this separately from autoimmune GN (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, casuscelli2023autoimmunityandinfection pages 1-2) | Often acute nephritic presentation with hematuria, proteinuria, hypertension; may be self-limited or progress depending on pathogen, host factors, and delay in treatment (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, casuscelli2023autoimmunityandinfection pages 1-2) | **Treat infection first**; supportive nephritic care, then selective immunosuppression only when appropriate to subtype/severity (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, casuscelli2023autoimmunityandinfection pages 1-2) |
| **IgA nephropathy / IgA vasculitis nephritis** | Mucosal immune dysregulation with aberrant IgA biology and nephritogenic immune-complex deposition; genetic and environmental factors both contribute (subtype-specific) (park2024glomerularspatialtranscriptomics pages 1-2, davies2024thecurrentuse pages 1-2) | Mesangial IgA-dominant deposition on biopsy; mesangial proliferation is both diagnostic and prognostic in IgAN; clinical presentation ranges from asymptomatic urinary abnormalities to acute GN (park2024glomerularspatialtranscriptomics pages 1-2) | Multi-hit IgA pathway; podocyte injury marker **TCF21** upregulated in IgAN; vascular-development, adhesion, and extracellular-matrix programs enriched in proliferative IgAN; GWAS-informed susceptibility noted in recent reviews (park2024glomerularspatialtranscriptomics pages 1-2, davies2024thecurrentuse pages 1-2) | Usually chronic/indolent but heterogeneous; about **~20%** of IgAN patients progress to ESKD in the cited 2024 study summary; IgA vasculitis nephritis tends to be more severe in adults (park2024glomerularspatialtranscriptomics pages 1-2) | Optimized supportive care first; corticosteroids in selected higher-risk disease; emerging mechanism-based agents include **targeted-release budesonide**, B-cell/APRIL-directed therapies, SGLT2 inhibitors, endothelin receptor antagonists, and complement inhibitors (subtype-specific, evidence strength varies) (park2024glomerularspatialtranscriptomics pages 1-2, davies2024thecurrentuse pages 1-2) |
| **Lupus nephritis (LN)** | Autoimmune GN driven by systemic lupus with autoantibodies, immune complexes, complement activation, and kidney-resident/immune-cell interactions (subtype-specific) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2) | Kidney biopsy is the **gold standard**; creatinine and urinalysis are baseline tests; class III/IV ± V classification guides therapy; serologies are subtype specific to SLE/LN (roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2) | Autoantibodies, complement, inflammatory kidney-stroma/immune-cell crosstalk; biomarkers under development in serum/urine; ancestry-associated risk gradients noted in recent reviews (roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2) | Relapsing-remitting or chronic progressive; occurs in up to **50% of adult SLE** and **80% of juvenile-onset SLE**; about **30%** may progress to ESKD within 15 years in one 2024 consensus summary (reisneto2024iibraziliansociety pages 1-2) | Induction: **MMF**, cyclophosphamide, **MMF+tacrolimus**, or **MMF+belimumab**; maintenance: **MMF** or azathioprine first line; rituximab for refractory disease; newer targeted agents include **voclosporin** and belimumab, with additional complement/B-cell pathway trials ongoing (roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2, lichtnekert2022lupusnephritiscurrent pages 14-15) |
| **ANCA-associated pauci-immune GN** | Autoimmune small-vessel vasculitis with pathogenic neutrophil-directed autoimmunity; severe crescentic GN phenotype is typical (subtype-specific) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, engesser2024immuneprofilingbasedtargeting pages 1-2) | Pauci-immune necrotizing/crescentic GN on biopsy with supportive **ANCA** serology; histologic scores such as Berden, RRS, and MCCS help prognosis (engesser2024immuneprofilingbasedtargeting pages 1-2) | Th1/Th17/Tc1/Tc17 inflammatory programs; complement C5a axis is therapeutically relevant; spatial/single-cell data identified pathogenic cytokine-producing T cells (engesser2024immuneprofilingbasedtargeting pages 1-2) | Often rapidly progressive with AKI/RPGN; kidney failure risk remains substantial without prompt treatment (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, engesser2024immuneprofilingbasedtargeting pages 1-2) | Standard therapy remains glucocorticoids plus cyclophosphamide and/or rituximab; **avacopan** aligns with C5a-pathway biology; exploratory precision approach: **ustekinumab** in 4 relapsing ANCA-GN patients showed improvement over 26 weeks (engesser2024immuneprofilingbasedtargeting pages 1-2) |
| **Anti-GBM disease** | Autoimmune GN caused by antibodies to the glomerular basement membrane; classic severe crescentic GN/RPGN subtype (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Linear GBM-directed immunostaining on biopsy with circulating anti-GBM antibodies; biopsy remains central for confirmation and severity assessment (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Autoantibody-mediated injury to glomerular filtration barrier; downstream crescent formation and necroinflammation (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Typically acute, aggressive, rapidly progressive kidney failure; may include pulmonary involvement in Goodpasture spectrum (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Rapid immunosuppression plus **plasma exchange** to remove pathogenic antibodies, alongside corticosteroids/cytotoxic therapy (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) |
| **C3 glomerulopathy / C3 glomerulonephritis** | Autoinflammatory/complement-mediated GN from dysregulated alternative complement pathway (subtype-specific) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, OpenTargets Search: glomerulonephritis) | C3-dominant biopsy pattern distinguishes this complement-mediated class; complement serologies/genetic workup may support diagnosis (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, OpenTargets Search: glomerulonephritis) | Strong disease-target associations include **CFH, C3, CFHR5, CFB, CFHR1, CFI**; complement dysregulation is the defining pathway (OpenTargets Search: glomerulonephritis) | Often chronic with recurrent/persistent hematuria-proteinuria and CKD progression; course is heterogeneous (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, OpenTargets Search: glomerulonephritis) | Mechanism-aligned therapy focuses on **complement inhibition** and complement-directed trial enrollment; supportive CKD/proteinuria management remains important (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, OpenTargets Search: glomerulonephritis) |
| **Monoclonal gammopathy-related GN** (for example MGRS-associated GN) | Nephrotoxic monoclonal immunoglobulin or light/heavy chain–related glomerular injury from plasma-cell or B-cell clone (subtype-specific) (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Biopsy pattern varies by deposit type; identification of a pathogenic monoclonal protein/clone is central to classification (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Monoclonal immunoglobulin-driven injury; clone biology rather than generic histology should drive treatment (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Often chronic/progressive unless the responsible clone is controlled; renal phenotype depends on deposit composition and location (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | **Clone-directed therapy**: plasma-cell– or B-cell–targeted treatment rather than nonspecific GN immunosuppression alone (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) |
| **Alloimmune GN** (transplant-related alloimmune glomerular injury) | Alloimmune responses to non-self renal antigens after transplantation; distinct from autoimmune GN (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Diagnosis relies on biopsy plus transplant immunopathology context; antibody/complement staining patterns may support alloimmune injury (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Adaptive alloimmunity, antigen presentation, antibody-mediated injury, complement activation (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Variable; may be subacute or chronic and contribute to graft dysfunction/loss (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) | Mechanism-aligned approach is **suppression of adaptive immunity** with transplant-directed immunosuppression optimization (anders2023glomerulonephritisimmunopathogenesisand pages 1-2) |


*Table: This table summarizes the major mechanistic glomerulonephritis classes and key subtype-specific features relevant to diagnosis, pathobiology, course, and treatment. It is useful as a compact knowledge-base scaffold because GN is heterogeneous and treatment increasingly follows mechanism rather than histology alone.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** glomerulonephritis.
* **Synonyms:** GN; glomerular nephritis; nephritic glomerular disease. “Nephritis” is broader and should not be treated as an exact synonym because it includes tubulointerstitial disease.
* **MONDO:** **MONDO:0002462**. Subtype examples include C3 glomerulonephritis, MONDO:0013892; primary membranoproliferative GN, MONDO:0018904; and immunoglobulin-mediated MPGN, MONDO:0014005. (OpenTargets Search: glomerulonephritis)
* **MeSH:** *Glomerulonephritis*; individual forms have additional descriptors.
* **ICD-10-CM:** GN is distributed across **N00–N08** according to acute/chronic status and morphologic lesion; rapidly progressive nephritic syndrome is N01 and unspecified nephritic syndrome N05. A single ICD code should not replace subtype coding.
* **ICD-11:** classified within glomerular diseases according to clinical/pathologic subtype.
* **OMIM/Orphanet:** no single syndrome-wide entry is biologically adequate. Entries apply to specific inherited forms, such as complement-mediated disease or CFHR5 nephropathy.

The report synthesizes **aggregated disease-level resources, published cohorts, biopsies, trials, and model studies**. It contains no individual EHR-level patient data. A recent expert definition states that GN comprises “heterogeneous immune-mediated disorders characterized by inflammation of the filtration units of the kidney.” (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Causal classes

1. **Autoimmune:** ANCA-associated GN, anti-GBM disease, lupus nephritis (LN), IgA nephropathy (IgAN), and IgA vasculitis nephritis.
2. **Infection-related:** post-streptococcal and infection-associated GN linked to bacterial, viral, fungal, or parasitic disease. Mechanisms include immune-complex deposition, direct cellular damage, molecular mimicry, and superantigens. (casuscelli2023autoimmunityandinfection pages 1-2)
3. **Complement/autoinflammatory:** C3 glomerulopathy caused by alternative-pathway dysregulation.
4. **Monoclonal gammopathy-related:** nephrotoxic monoclonal immunoglobulin produced by a B-cell or plasma-cell clone.
5. **Alloimmune:** glomerular injury in a transplanted kidney.
6. **Secondary immune-complex disease:** chronic infection, autoimmune disease, malignancy, drugs, or systemic inflammatory disease.

### Genetic susceptibility

There is **no universal GN gene**. High-confidence subtype-specific associations include **CFH, C3, CFHR5, CFB, CFHR1, CFI, CFHR2**, and occasionally **DGKE** in complement-mediated/MPGN phenotypes. OpenTargets ranks CFH, DGKE, and CFHR5 among the strongest GN associations and links these findings to published and expert-panel evidence. (OpenTargets Search: glomerulonephritis)

Other important susceptibility relationships include HLA loci in autoimmune GN, **PLA2R1** in membranous nephropathy, and **APOL1 G1/G2** risk genotypes—especially in people with recent African ancestry—as modifiers of FSGS-pattern disease and adverse kidney outcomes rather than causes of all GN. African biopsy data show marked geographic heterogeneity and identify APOL1 risk variants as a plausible contributor to the high FSGS burden. (ekrikpo2023prevalenceanddistribution pages 1-3)

**Variant interpretation:** complement-gene variants may be pathogenic, likely pathogenic, or VUS under ACMG/AMP criteria; interpretation requires phenotype, segregation, functional complement studies, and population frequency. Most causal variants are **germline** and rare. CFHR rearrangements may be copy-number/structural variants; CFH/C3/CFB variants can be missense or loss-/gain-of-function depending on the gene and allele. Somatic variants are not a routine cause of GN, although an acquired hematologic clone can cause monoclonal gammopathy-related GN. Chromosomal aneuploidy, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not routine syndrome-level tests.

### Environmental and host risk factors

Risk depends on subtype: infection exposure; autoimmune predisposition; older age and frailty; ancestry; systemic lupus; chronic liver or gastrointestinal disease; malignancy; smoking; obesity; hypertension; and nephrotoxic or immune-modulating drugs can contribute. Infection and GN are bidirectional: pathogens can trigger GN, whereas urinary immunoglobulin loss and immunosuppressive treatment increase subsequent infection risk. Post-streptococcal disease peaks at approximately ages 3–12 and has male predominance. (casuscelli2023autoimmunityandinfection pages 1-2)

**Gene–environment paradigm:** inherited complement dysregulation may remain clinically silent until infection activates complement; mucosal infection or microbiome perturbation can amplify production of nephritogenic IgA in genetically susceptible IgAN; inflammatory interferon states can interact with APOL1 high-risk genotypes. This is probabilistic, not simple Mendelian causation.

### Protective factors

No broadly validated **genetic protective allele** prevents GN. Practical protective factors are subtype-specific: vaccination and prompt infection treatment; avoidance of tobacco, obesity, excessive sodium, and nephrotoxins; blood-pressure and proteinuria control; disease control before pregnancy; and adherence to maintenance therapy. Evidence is strongest for preventing progression and complications, not for preventing every incident GN case.

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Microscopic or gross hematuria | Laboratory/sign; often episodic in IgAN and persistent in active proliferative GN | **HP:0000790 Hematuria** |
| Proteinuria | Laboratory abnormality; mild to nephrotic-range; major prognostic and response marker | **HP:0000093 Proteinuria** |
| Reduced GFR/AKI | Laboratory/functional; abrupt in RPGN or progressive in chronic GN | **HP:0001919 Acute kidney injury**, **HP:0012622 Chronic kidney disease** |
| Hypertension | Clinical sign; common in acute nephritic and chronic disease | **HP:0000822 Hypertension** |
| Edema | Physical sign; periorbital/peripheral to generalized | **HP:0000969 Edema** |
| Oliguria | Symptom/sign in severe acute disease | **HP:0100520 Oliguria** |
| Hypoalbuminemia/hyperlipidemia | Laboratory abnormalities in nephrotic overlap | **HP:0003073 Hypoalbuminemia**, **HP:0003124 Hypercholesterolemia** |
| Glomerular crescents | Histopathologic manifestation of severe capillary-wall injury | **HP:0031263 Crescentic glomerulonephritis** |
| Kidney failure | Advanced outcome requiring dialysis/transplantation | **HP:0003774 End-stage renal disease** |

Acute GN commonly combines hypertension, hematuria, and proteinuria. IgAN ranges from asymptomatic urinary abnormalities to acute GN; approximately 20% progressed to ESKD in the population summarized by a 2024 spatial-transcriptomic study. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2, park2024glomerularspatialtranscriptomics pages 1-2)

Age, severity, and frequency vary sharply by subtype: post-infectious GN is common in children; IgAN often begins in adolescence or early/middle adulthood; LN is concentrated in patients with SLE and may be especially frequent in juvenile-onset disease; ANCA-GN is predominantly adult/older-adult; genetic complement disease can begin in childhood or adulthood. Symptoms can be episodic, relapsing-remitting, rapidly progressive, or chronically progressive.

**Quality of life:** fatigue, edema, dietary restrictions, medication toxicity, recurrent admissions, dialysis, infertility concerns, and infection anxiety impair physical, social, and occupational functioning. GN-specific EQ-5D/SF-36 estimates cannot be generalized across subtypes; these should be captured with CKD- and disease-specific patient-reported outcome instruments.

## 4. Genetic, molecular, and epigenetic information

GN is usually **multifactorial/polygenic**, except for defined monogenic complement or structural disorders. Complement-associated genes should be stored as subtype-level causal/modifier genes: **CFH, CFI, CFB, C3, CFHR1–5, DGKE**. **PLA2R1** is principally a susceptibility/antigen-related locus in membranous nephropathy, and **MS4A1/CD20, NR3C1, TNFSF13B/BAFF**, and complement genes are therapeutic targets rather than necessarily causal genes. (OpenTargets Search: glomerulonephritis)

For knowledge-base ingestion:

* Record exact HGVS variants only from ClinVar/ClinGen or a diagnostic report; do not infer a pathogenic variant from a gene association.
* Record germline inheritance by specific disorder—AD, AR, or complex susceptibility may all occur in complement disease. Penetrance is often incomplete and trigger-dependent; expressivity is variable.
* Founder effects are established for some subtype/population-specific alleles, including CFHR5 nephropathy and APOL1 risk haplotypes, but there is no syndrome-wide carrier frequency.
* Genetic anticipation is not characteristic. Germline mosaicism is possible in principle but not a defining GN feature.
* DNA methylation, chromatin accessibility, interferon-regulated transcription, and immune-cell epigenetic states are active research areas, not clinical diagnostic markers.

A 2024 IgAN spatial study found **77 upregulated and 55 downregulated genes** in proliferative M1-IgAN versus controls; **TCF21** was consistently increased as an early podocyte-injury marker, while adhesion, vascular-development, and extracellular-matrix programs were enriched. (park2024glomerularspatialtranscriptomics pages 1-2)

## 5. Environmental and infectious information

Relevant agents include **group A streptococci, Staphylococcus aureus, infective-endocarditis pathogens, hepatitis B and C viruses, HIV, SARS-CoV-2, and selected parasites**. Pathogen attribution requires clinical microbiology and subtype-specific evidence; detection of an organism alone does not prove causation. Infection can act through circulating immune complexes, planted antigens, complement activation, molecular mimicry, or superantigens. (casuscelli2023autoimmunityandinfection pages 1-2)

Drug-related or exposure-related glomerular injury can follow immune-checkpoint inhibitors, anti-TNF agents, selected antibiotics, hydralazine, propylthiouracil, levamisole-adulterated cocaine, and other agents, depending on phenotype. Smoking and air pollution are plausible inflammatory/vascular modifiers but not established universal causes. High sodium intake, obesity, and poor blood-pressure control principally accelerate progression.

## 6. Mechanism and pathophysiology

### Causal chain

**Trigger or loss of tolerance → antibody/immune-complex, complement, clone, or T-cell activation → deposition or in-situ glomerular binding → endothelial, mesangial, GBM, and podocyte injury → leukocyte recruitment and capillary-wall rupture → hematuria/proteinuria and reduced filtration → parietal epithelial-cell proliferation/crescents → extracellular-matrix deposition, glomerulosclerosis, tubulointerstitial fibrosis, and CKD.** (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)

Upstream processes are antigen generation, mucosal immune dysregulation, autoantibody formation, complement dysregulation, and clone formation. Downstream processes include cytokine release, oxidative injury, necrosis, crescent formation, podocyte loss, maladaptive repair, and fibrosis. Effector Th1/Th17 and CD8 T-cell responses are implicated in crescentic GN, while podocytes function both as filtration-barrier cells and immune-responsive cells. (linke2022pathogenictcellresponses pages 21-22)

**Suggested GO biological processes:** complement activation (GO:0006956), inflammatory response (GO:0006954), adaptive immune response (GO:0002250), immune-complex clearance (GO:0002434), leukocyte migration (GO:0050900), apoptotic process (GO:0006915), extracellular-matrix organization (GO:0030198), and tissue remodeling (GO:0048771).

**Suggested Cell Ontology classes:** podocyte (**CL:0000653**), glomerular endothelial cell, mesangial cell, parietal epithelial cell, macrophage (**CL:0000235**), neutrophil (**CL:0000775**), CD4 T cell (**CL:0000624**), CD8 T cell (**CL:0000625**), B cell (**CL:0000236**), and plasma cell (**CL:0000786**).

### Molecular profiling and 2023–2024 advances

A 2024 systematic review included **27 omics studies and 1,818 participants**: 18 proteomic and 9 metabolomic studies; samples were urine in 19 studies, blood in 4, and biopsy tissue in 6. Proposed signatures addressed diagnosis, phenotype, progression, and treatment response, but most remain unvalidated. The clinically important precedent is anti-PLA2R discovery in membranous nephropathy; candidate FSGS proteins include LAMP1 and ACSL4. The authors concluded that “further larger-scale research is required.” (davies2024thecurrentuse pages 1-2, davies2024thecurrentuse pages 13-15)

Spatial profiling of IgAN demonstrates molecular heterogeneity even among histologically similar glomeruli. In ANCA-GN, single-cell/spatial profiling of 34 patients identified cytokine-producing Th1/Th17 and cytotoxic T-cell niches and nominated IL-12/23 blockade as a therapeutic strategy. (park2024glomerularspatialtranscriptomics pages 1-2, engesser2024immuneprofilingbasedtargeting pages 1-2)

Metabolic changes include local hypoxia, oxidative stress, altered lipid handling, mitochondrial dysfunction, and increased matrix synthesis; these are generally downstream/shared CKD programs rather than diagnostic biochemical defects.

## 7. Anatomical structures affected

The primary organ is the **kidney**, usually bilaterally. The primary site is the **renal glomerulus**—capillary endothelium, glomerular basement membrane, mesangium, podocytes, slit diaphragm, and Bowman capsule/parietal epithelium. Secondary tubulointerstitial inflammation and fibrosis are major determinants of irreversible function loss. Suggested anatomy terms include **UBERON:0002113 kidney**, **UBERON:0000074 renal glomerulus**, and **UBERON:0001229 renal tubule**.

Relevant subcellular compartments include the podocyte actin cytoskeleton, slit diaphragm, GBM extracellular matrix, lysosome/endosome, mitochondrion, nucleus/chromatin, and complement-active extracellular space. Suggested GO cellular components include extracellular matrix (GO:0031012), basement membrane (GO:0005604), cell–cell junction (GO:0005911), mitochondrion (GO:0005739), lysosome (GO:0005764), and nucleus (GO:0005634).

Secondary organs depend on cause: lungs in anti-GBM disease and ANCA vasculitis; skin, joints, gut, and lungs in systemic vasculitis; cardiovascular system in hypertension/CKD; and multiple organs in SLE. GN is generally bilateral rather than lateralized.

## 8. Temporal development

* **Acute:** infection-related GN and some immune-complex flares.
* **Rapidly progressive:** ANCA, anti-GBM, and severe immune-complex crescentic GN; this is a treatment emergency.
* **Relapsing-remitting:** LN, ANCA vasculitis, and some IgA/complement diseases.
* **Slowly progressive:** IgAN, C3 glomerulopathy, and persistent immune-complex disease.
* **Self-limited:** many childhood post-streptococcal cases, although adult/infection-associated cases can have poor outcomes.

Stages are best represented as active urinary/inflammatory disease, partial response, complete response/remission, relapse, chronic scarring/CKD, and kidney failure—not as a universal numbered GN staging system. The critical intervention window is before crescents and interstitial fibrosis become irreversible.

For LN, a 2024 consensus defines target renal response as stable/improved kidney function plus proteinuria reduction of **25% by 3 months, 50% by 6 months, and to <0.8 g/day by 12 months**. (reisneto2024iibraziliansociety pages 1-2)

## 9. Inheritance and population epidemiology

There is no reliable global incidence for aggregate GN because biopsy policies, coding, age structure, infection burden, and subtype distribution differ. In one US Medicare cohort, up to **1.2%** had GN; GN accounted for **18.7% of CKD in Germany** and **30–36% of ESKD among US children/adolescents** in the epidemiologic synthesis cited by Anders and colleagues. African American, Hispanic, Asian, and First Nations populations bear disproportionate burdens. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)

An African meta-analysis of **17 studies, 6,494 biopsy patients, and eight countries** found pooled distributions of FSGS **26.1%**, minimal-change disease **22.4%**, membranous nephropathy **8.4%**, MPGN **6.4%**, mesangioproliferative GN **6.4%**, post-infectious GN **2.6%**, IgAN **2.6%**, and crescentic GN **1.4%**. Only four studies used the full light-microscopy/immunofluorescence/electron-microscopy combination, illustrating ascertainment bias. (ekrikpo2023prevalenceanddistribution pages 1-3)

LN affects approximately **40% of patients with SLE** in a 2024 review and is more prevalent among Hispanic, African, and Asian than White populations. A separate 2024 consensus reports up to **50% of adult** and **80% of juvenile-onset SLE** patients. These differences reflect population and definition, not necessarily contradiction. (roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2)

Most GN is multifactorial. Monogenic inheritance, penetrance, founder effect, consanguinity, carrier frequency, and cascade testing should be recorded only for a confirmed genetic subtype.

## 10. Diagnostics

### Clinical work-up

1. Confirm glomerular injury: urinalysis and microscopy for dysmorphic erythrocytes/RBC casts; urine albumin- or protein-to-creatinine ratio; serum creatinine/eGFR, albumin, electrolytes, CBC, and blood pressure.
2. Define mechanism: C3/C4; ANA, anti-dsDNA; ANCA with PR3/MPO specificity; anti-GBM; hepatitis B/C and HIV testing; cultures when infection is possible; ASO/anti-DNase B when indicated; serum/urine electrophoresis, immunofixation, and free light chains; cryoglobulins; anti-PLA2R for membranous nephropathy.
3. **Kidney biopsy:** light microscopy, immunofluorescence, and electron microscopy. IF is essential for immunoglobulin, complement, light-chain, and linear-versus-granular pattern recognition. Clinical signs alone cannot reliably distinguish subtypes. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)
4. Imaging: renal ultrasound mainly assesses size, obstruction, anatomy, and biopsy safety; CT/MRI/PET are not primary GN diagnostic tests.

The 2024 biomarker review concludes that noninvasive biomarkers are increasingly useful, but biopsy still cannot generally be replaced. Anti-PLA2R is a real-world biomarker success; other urinary biomarkers and multi-analyte algorithms remain investigational. (davies2024thecurrentuse pages 13-15)

### Histologic patterns and differential diagnosis

Distinguish immune-complex proliferative GN, pauci-immune necrotizing/crescentic GN, linear anti-GBM disease, C3-dominant GN, membranous disease, and monoclonal deposits. Important mimics include acute tubular injury, interstitial nephritis, diabetic kidney disease, hypertensive nephrosclerosis, thrombotic microangiopathy, hereditary Alport/COL4 disease, and podocytopathy.

### Genetic testing

Use a **phenotype-driven complement or glomerulopathy panel**, escalating to WES/WGS when onset is pediatric/young, familial, syndromic, steroid-resistant, recurrent after transplant, or biopsy/serology suggests complement dysregulation. WGS is particularly useful for CFHR structural variants not captured by routine exome sequencing. CMA, karyotype, FISH, mtDNA, and repeat-expansion tests are not routine unless another phenotype indicates them.

Population screening is not recommended. Screen high-risk people with urinalysis, albuminuria, blood pressure, and creatinine; use cascade genetic testing only after a familial pathogenic variant is established.

## 11. Outcomes and prognosis

Outcome ranges from complete recovery to relapsing disease, CKD, ESKD, cardiovascular events, serious infection, and death. Prognosis is driven by baseline eGFR/creatinine, proteinuria, hypertension, age, speed of treatment, normal-glomerulus fraction, crescents/necrosis, and chronicity/interstitial fibrosis.

In a 2024 ANCA-GN cohort of **152 adults**, median age was **63.8 years** and follow-up **46.9 months**; **59 (38.8%)** reached ESKD/eGFR <15 and 20 died. Hypertension, creatinine, and percentage of normal glomeruli independently predicted ESKD; Renal Risk Score and Mayo Chronicity Score remained independently predictive. (engesser2024immuneprofilingbasedtargeting pages 1-2)

For LN, one 2024 consensus estimates that **30% progress to ESKD within 15 years**, underscoring the importance of early proteinuria response and prevention of flares. (reisneto2024iibraziliansociety pages 1-2)

Nephrotic overlap adds thromboembolism, infection, malnutrition, dyslipidemia, and cardiovascular risk; membranous nephropathy has particularly high thrombosis risk. (wendt2024anupdatedcomprehensive pages 1-2)

No syndrome-wide 5- or 10-year survival estimate is meaningful. Quality-of-life and mortality analyses should be stratified by subtype, CKD stage, dialysis/transplant status, age, and immunosuppressive exposure.

## 12. Treatment and real-world implementation

### General strategy

* Treat the cause rather than the biopsy label alone.
* Control blood pressure and proteinuria with ACE inhibitor/ARB where tolerated; consider SGLT2 inhibition in proteinuric CKD according to kidney function and indication.
* Restrict excess sodium, manage edema with diuretics, avoid nephrotoxins, treat dyslipidemia and cardiovascular risk, and adjust drug doses to GFR.
* Use glucocorticoids and immunosuppression only when mechanism and activity justify infection/toxicity risk.

### Subtype-directed therapy

* **Infection-related GN:** eradicate infection and provide supportive care; indiscriminate immunosuppression can be harmful.
* **ANCA-GN:** glucocorticoid-sparing induction with rituximab or cyclophosphamide; avacopan targets C5a receptor biology; maintenance commonly uses rituximab or other guideline-directed therapy.
* **Anti-GBM:** urgent plasma exchange plus glucocorticoid and cyclophosphamide-based immunosuppression when recovery is plausible.
* **LN class III/IV ± V:** MMF, cyclophosphamide, MMF+tacrolimus, or MMF+belimumab for induction; MMF or azathioprine for maintenance; rituximab for refractory disease. Voclosporin and belimumab are major recent additions. (roveta2024lupusnephritisfrom pages 1-2, reisneto2024iibraziliansociety pages 1-2)
* **IgAN:** optimized supportive care; selected high-risk patients may receive targeted-release budesonide or carefully selected glucocorticoid therapy. Emerging targets include APRIL/BAFF, complement, endothelin, and B/plasma cells.
* **C3 glomerulopathy:** supportive therapy and complement-pathway-directed therapy/trials after excluding infection and monoclonal gammopathy.
* **Monoclonal gammopathy-related GN:** B-cell- or plasma-cell clone-directed therapy.

Suggested NCIt intervention concepts include corticosteroid therapy, immunosuppressive therapy, rituximab therapy, cyclophosphamide therapy, mycophenolate therapy, plasma exchange, complement-inhibitor therapy, dialysis, and kidney transplantation. Chemical annotations may include glucocorticoids, cyclophosphamide, mycophenolate mofetil, rituximab, belimumab, voclosporin, avacopan, ACE inhibitors, ARBs, and SGLT2 inhibitors; exact CHEBI identifiers should be resolved against the current ontology release.

### Experimental and precision therapies

A 2024 proof-of-concept study used spatial/single-cell data to nominate ustekinumab. Four relapsing ANCA-GN patients received **90 mg subcutaneously at weeks 0, 4, 12, and 24** with low-dose cyclophosphamide/steroids; all improved clinically over 26 weeks. This is promising but uncontrolled and far too small to establish efficacy. (engesser2024immuneprofilingbasedtargeting pages 1-2)

Current-development examples include **NCT06277427** (BCMA CAR-T in refractory ANCA vasculitis/LN; recruiting, n=24), **NCT06419205** (phase 2 ADX-097 in IgAN/LN/C3G; recruiting, n=30), **NCT05732402** (povetacicept in autoantibody-associated glomerular disease; phase 1/2, n=72), and **NCT05083364** (ARO-C3; completed phase 1/2, n=62). Trial availability and status should be verified at https://clinicaltrials.gov before use.

No established syndrome-wide pharmacogenomic dosing guideline exists. Genotype primarily informs disease mechanism and transplant recurrence risk rather than routine drug metabolism.

## 13. Prevention

* **Primary:** vaccination; sanitation and infection control; prompt treatment of streptococcal/endovascular infections; avoidance of cocaine/levamisole and causative drugs; smoking cessation; healthy weight and blood-pressure control. Vaccination does not prevent autoimmune GN generally but reduces infection triggers and treatment complications.
* **Secondary:** urinalysis, albuminuria, creatinine/eGFR, and blood pressure in SLE, systemic vasculitis, chronic infection, monoclonal gammopathy, or genetically at-risk relatives. All SLE patients should undergo creatinine and urinalysis screening for renal involvement. (reisneto2024iibraziliansociety pages 1-2)
* **Tertiary:** proteinuria/BP control, relapse monitoring, vaccination before immunosuppression where possible, Pneumocystis prophylaxis when indicated, bone and gastric protection, fertility preservation counseling, thrombosis-risk assessment, and CKD cardiovascular care.
* **Genetic counseling:** appropriate for confirmed complement or other monogenic disease; discuss incomplete penetrance, variable expressivity, donor selection, recurrence after transplantation, and reproductive options.

There is no population newborn-screening program or prophylactic medication appropriate for GN as a whole.

## 14. Other species and natural disease

Naturally occurring immune-complex and infectious GN occurs in dogs, cats, horses, livestock, and wildlife, but veterinary nomenclature and prevalence are species- and cause-specific. Dogs develop immune-complex GN associated with chronic infection, neoplasia, and systemic inflammatory disease; breed-associated hereditary glomerulopathies more often model structural GBM or podocyte disorders than aggregate human GN. No single VBO breed term or cross-species transmission model applies.

GN itself is **not zoonotically transmitted**. A zoonotic or vector-borne pathogen can infect humans and animals and independently trigger immune renal injury, but the glomerular lesion is a host response rather than a transmissible phenotype. Orthologs of complement, immunoglobulin, cytokine, and GBM genes are highly conserved across mammals.

## 15. Model organisms and experimental systems

* **Nephrotoxic-serum/nephrotoxic-nephritis mice:** rapid antibody-mediated crescentic GN; useful for complement, neutrophil, macrophage, Th1/Th17, crescent, and fibrosis studies. Limitation: artificial immunization and compressed time course.
* **Lupus-prone mice:** MRL/lpr, NZB/W F1, and related strains reproduce autoantibodies, immune-complex GN, proteinuria, and aspects of systemic autoimmunity. Strain-specific biology and treatment responses limit direct translation.
* **IgAN models:** grouped ddY, humanized/transgenic and immunization models reproduce parts of aberrant IgA production, immune-complex deposition, and mesangial injury. Only primates produce the human IgA1 subclass, so no mouse model captures the entire human multi-hit pathway.
* **Anti-GBM/ANCA models:** antibody-transfer and antigen-immunization models isolate autoantibody, neutrophil, and complement effects but incompletely reproduce spontaneous human loss of tolerance.
* **In vitro systems:** cultured podocytes, glomerular endothelial and mesangial cells, kidney organoids, glomerulus-on-chip systems, and patient-derived cells support mechanistic and drug studies but lack complete circulation and immunity.

A recent model review emphasizes that rodents remain dominant because genetically modified strains are available, while organoids, kidney-on-chip, zebrafish, and larger animals are emerging. Model selection must match the mechanistic question; there is no universally faithful “GN model.”

## Evidence interpretation and key authoritative conclusions

The strongest current expert position is that histology remains indispensable but should be integrated with mechanism. Anders and colleagues argue that lesion patterns “do not align well with their diverse pathological mechanisms” and propose treatment according to immunopathogenesis. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)

Recent technologies support this transition but are not yet replacements for conventional care. The 2024 biomarker literature concludes that biopsy “still cannot be replaced by non-invasive strategies,” while the proteomic/metabolomic review found promising markers but emphasized the need for larger validation studies. (davies2024thecurrentuse pages 1-2, davies2024thecurrentuse pages 13-15)

### Selected recent sources

* Anders H-J et al. **Glomerulonephritis: immunopathogenesis and immunotherapy.** *Nature Reviews Immunology*. Published January 2023. DOI/URL: https://doi.org/10.1038/s41577-022-00816-y. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2)
* Park S et al. **Glomerular spatial transcriptomics of IgA nephropathy according to mesangial proliferation.** *Scientific Reports*. Published January 2024. https://doi.org/10.1038/s41598-024-52581-8. (park2024glomerularspatialtranscriptomics pages 1-2)
* Davies E et al. **The current use of proteomics and metabolomics in glomerulonephritis.** *Journal of Nephrology*. Published April 2024. https://doi.org/10.1007/s40620-024-01923-w. (davies2024thecurrentuse pages 1-2)
* Engesser J et al. **Immune profiling-based targeting of pathogenic T cells with ustekinumab in ANCA-associated GN.** *Nature Communications*. Published September 2024. https://doi.org/10.1038/s41467-024-52525-w. (engesser2024immuneprofilingbasedtargeting pages 1-2)
* dos Reis-Neto ET et al. **II Brazilian Society of Rheumatology consensus for lupus nephritis.** *Advances in Rheumatology*. Published June 2024. https://doi.org/10.1186/s42358-024-00386-8. (reisneto2024iibraziliansociety pages 1-2)
* Roveta A et al. **Lupus nephritis from pathogenesis to new therapies.** *International Journal of Molecular Sciences*. Published August 2024. https://doi.org/10.3390/ijms25168981. (roveta2024lupusnephritisfrom pages 1-2)
* Ekrikpo UE et al. **Primary glomerular diseases in Africa: systematic review and meta-analysis.** *Pan African Medical Journal*. Published August 2023. https://doi.org/10.11604/pamj.2023.45.153.40741. (ekrikpo2023prevalenceanddistribution pages 1-3)

**Knowledge-base recommendation:** represent “glomerulonephritis” as a parent syndrome and attach genes, variants, epidemiology, biomarkers, prognosis, treatments, inheritance, and models to mechanistically and histopathologically defined child entities. This avoids false syndrome-wide assertions and reflects current expert understanding.

References

1. (anders2023glomerulonephritisimmunopathogenesisand pages 1-2): Hans-Joachim Anders, A. Richard Kitching, Nelson Leung, and Paola Romagnani. Glomerulonephritis: immunopathogenesis and immunotherapy. Nature Reviews. Immunology, 23:1-19, Jan 2023. URL: https://doi.org/10.1038/s41577-022-00816-y, doi:10.1038/s41577-022-00816-y. This article has 247 citations.

2. (casuscelli2023autoimmunityandinfection pages 1-2): Chiara Casuscelli, Elisa Longhitano, Veronica Maressa, Silvia Di Carlo, Luigi Peritore, Simone Di Lorenzo, Vincenzo Calabrese, Valeria Cernaro, and Domenico Santoro. Autoimmunity and infection in glomerular disease. Microorganisms, 11:2227, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092227, doi:10.3390/microorganisms11092227. This article has 14 citations.

3. (park2024glomerularspatialtranscriptomics pages 1-2): Sehoon Park, Minji Kang, Yong Chul Kim, Dong Ki Kim, Kook-Hwan Oh, Kwon Wook Joo, Yon Su Kim, Hyun Je Kim, Kyung Chul Moon, and Hajeong Lee. Glomerular spatial transcriptomics of iga nephropathy according to the presence of mesangial proliferation. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52581-8, doi:10.1038/s41598-024-52581-8. This article has 12 citations and is from a peer-reviewed journal.

4. (davies2024thecurrentuse pages 1-2): Elin Davies, Andrew Chetwynd, Garry McDowell, Anirudh Rao, and Louise Oni. The current use of proteomics and metabolomics in glomerulonephritis: a systematic literature review. Journal of Nephrology, 37:1209-1225, Apr 2024. URL: https://doi.org/10.1007/s40620-024-01923-w, doi:10.1007/s40620-024-01923-w. This article has 12 citations and is from a peer-reviewed journal.

5. (roveta2024lupusnephritisfrom pages 1-2): Annalisa Roveta, Emanuele Luigi Parodi, Brigida Brezzi, Francesca Tunesi, Valentina Zanetti, Guido Merlotti, Alessia Francese, Antonio G. Maconi, and Marco Quaglia. Lupus nephritis from pathogenesis to new therapies: an update. International Journal of Molecular Sciences, 25:8981, Aug 2024. URL: https://doi.org/10.3390/ijms25168981, doi:10.3390/ijms25168981. This article has 103 citations.

6. (reisneto2024iibraziliansociety pages 1-2): Edgard Torres dos Reis-Neto, Luciana Parente Costa Seguro, Emília Inoue Sato, Eduardo Ferreira Borba, Evandro Mendes Klumb, Lilian Tereza Lavras Costallat, Marta Maria das Chagas Medeiros, Eloisa Bonfá, Nafice Costa Araújo, Simone Appenzeller, Ana Carolina de Oliveira e Silva Montandon, Emily Figueiredo Neves Yuki, Roberto Cordeiro de Andrade Teixeira, Rosa Weiss Telles, Danielle Christinne Soares do Egypto, Francinne Machado Ribeiro, Andrese Aline Gasparin, Antonio Silaide de Araujo Junior, Cláudia Lopes Santoro Neiva, Debora Cerqueira Calderaro, and Odirlei Andre Monticielo. Ii brazilian society of rheumatology consensus for lupus nephritis diagnosis and treatment. Advances in Rheumatology, 64:1-25, Jun 2024. URL: https://doi.org/10.1186/s42358-024-00386-8, doi:10.1186/s42358-024-00386-8. This article has 22 citations.

7. (lichtnekert2022lupusnephritiscurrent pages 14-15): Julia Lichtnekert, Hans-Joachim Anders, and Maciej Lech. Lupus nephritis: current perspectives and moving forward. Journal of Inflammation Research, 15:6533-6552, Dec 2022. URL: https://doi.org/10.2147/jir.s363722, doi:10.2147/jir.s363722. This article has 32 citations and is from a peer-reviewed journal.

8. (engesser2024immuneprofilingbasedtargeting pages 1-2): Jonas Engesser, Robin Khatri, Darius Schaub, Yu Zhao, Hans-Joachim Paust, Zeba Sultana, Nariaki Asada, Jan-Hendrik Riedel, Varshi Sivayoganathan, Anett Peters, Anna Kaffke, Saskia-Larissa Jauch-Speer, Thiago Goldbeck-Strieder, Victor G. Puelles, Ulrich O. Wenzel, Oliver M. Steinmetz, Elion Hoxha, Jan-Eric Turner, Hans-Willi Mittrücker, Thorsten Wiech, Tobias B. Huber, Stefan Bonn, Christian F. Krebs, and Ulf Panzer. Immune profiling-based targeting of pathogenic t cells with ustekinumab in anca-associated glomerulonephritis. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52525-w, doi:10.1038/s41467-024-52525-w. This article has 50 citations and is from a highest quality peer-reviewed journal.

9. (OpenTargets Search: glomerulonephritis): Open Targets Query (glomerulonephritis, 26 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (ekrikpo2023prevalenceanddistribution pages 1-3): Udeme Ekpenyong Ekrikpo, Patience Ngozi Obiagwu, Aniema Isaac Udo, Ijezie Innocent Chukwuonye, Jean Jacques Noubiap, Ugochi Sophia Okpechi-Samuel, Udeme-Abasi Nelson Udoudo, Elliot Korateng Tannor, Stanley Chidozie Ngoka, Ikechukwu Okeke Mbah, Aminu Kasarawa Bello, and Ikechi Gareth Okpechi. Prevalence and distribution of primary glomerular diseases in africa: a systematic review and meta-analysis of observational studies. The Pan African Medical Journal, Aug 2023. URL: https://doi.org/10.11604/pamj.2023.45.153.40741, doi:10.11604/pamj.2023.45.153.40741. This article has 10 citations.

11. (linke2022pathogenictcellresponses pages 21-22): Alexandra Linke, Gisa Tiegs, and Katrin Neumann. Pathogenic t-cell responses in immune-mediated glomerulonephritis. Cells, 11:1625, May 2022. URL: https://doi.org/10.3390/cells11101625, doi:10.3390/cells11101625. This article has 53 citations.

12. (davies2024thecurrentuse pages 13-15): Elin Davies, Andrew Chetwynd, Garry McDowell, Anirudh Rao, and Louise Oni. The current use of proteomics and metabolomics in glomerulonephritis: a systematic literature review. Journal of Nephrology, 37:1209-1225, Apr 2024. URL: https://doi.org/10.1007/s40620-024-01923-w, doi:10.1007/s40620-024-01923-w. This article has 12 citations and is from a peer-reviewed journal.

13. (wendt2024anupdatedcomprehensive pages 1-2): R. Wendt, Alina Sobhani, P. Diefenhardt, Moritz Trappe, and Linus Alexander Völker. An updated comprehensive review on diseases associated with nephrotic syndromes. Biomedicines, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102259, doi:10.3390/biomedicines12102259. This article has 25 citations.

## Artifacts

- [Edison artifact artifact-00](Glomerulonephritis-deep-research-falcon_artifacts/artifact-00.md)