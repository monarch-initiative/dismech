---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-13T13:52:23.236611'
end_time: '2026-05-13T14:06:46.549988'
duration_seconds: 863.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Xeroderma Pigmentosum
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Xeroderma_Pigmentosum-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Xeroderma Pigmentosum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Xeroderma Pigmentosum** covering all of the
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
- **Disease Name:** Xeroderma Pigmentosum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Xeroderma Pigmentosum** covering all of the
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


## Xeroderma Pigmentosum (XP): Comprehensive Disease Characteristics Report (2023–2024–prioritized)

### Executive summary
Xeroderma pigmentosum (XP) is a rare, autosomal recessive DNA-repair disorder characterized by extreme ultraviolet (UV) sensitivity, early-onset pigmentary changes, and a markedly increased risk of UV-induced skin cancers, with a subset of patients developing progressive neurodegeneration. XP is genetically heterogeneous, caused by biallelic pathogenic variants in nucleotide excision repair (NER) genes (XPA–XPG, ERCC genes and DDB2) or in the translesion synthesis polymerase gene POLH (XP-variant). Recent high-impact work (2023–2024) has quantified neurological burden and progression in a national cohort, linked specific XPA variants to neurodegeneration severity, profiled the genomic landscape of XP skin cancers, and advanced precision-medicine concepts such as antisense oligonucleotide (ASO) correction of deep intronic founder variants and in vitro “synthetic rescue” strategies. (garciamoreno2023neurologicaldiseasein pages 1-2, sagun2024differentgermlinevariants pages 1-2, yurchenko2023genomicmutationlandscape pages 1-2, senju2023deepintronicfounder pages 1-2, kobaisi2024syntheticrescueof pages 1-2)

---

## 1. Disease Information

### 1.1 Disease overview (definition and current understanding)
XP is a multisystemic disorder in which defects in repair of UV-induced DNA lesions (primarily bulky photoproducts) lead to profound photosensitivity with cutaneous and ocular injury, premature skin aging, and multiple early skin malignancies; some genotypes are additionally associated with progressive neurological disease. A practical clinical summary emphasizes: “Strict and consistent sun avoidance and protection and early detection and treatment of premalignant and malignant skin lesions are the mainstays of management,” and that “At present, there is no cure for XP.” (srivastava2021xerodermapigmentosum pages 2-5)

### 1.2 Key identifiers and controlled vocabulary
* **MeSH:** Xeroderma Pigmentosum (MeSH ID **D014983**) as used in ClinicalTrials.gov metadata. (NCT05159752 chunk 1)
* **OMIM:** XP complementation groups are referenced in the literature excerpt as XP-A to XP-G plus XP-variant (XPV). (schubert2019xerodermapigmentosumand pages 5-6, garciamoreno2023neurologicaldiseasein pages 1-2)
* **MONDO / Orphanet / ICD-10 / ICD-11:** Not reliably retrievable from the tool-accessible evidence during this run; therefore, MONDO and ORPHA identifiers are not asserted here.

### 1.3 Synonyms and alternative names
* “Xeroderma pigmentosum”
* “XP”
* “Xeroderma pigmentosum variant” / “XPV” (POLH-associated) (garciamoreno2023neurologicaldiseasein pages 1-2, yurchenko2023genomicmutationlandscape pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
The evidence used in this report includes (i) aggregated cohort studies (e.g., UK National XP Service prospective cohort), (ii) tumor genome profiling (multiple tumor genomes from multiple XP groups), (iii) mechanistic in vitro studies in patient-derived cells and engineered models, and (iv) clinical-trial registry data. (garciamoreno2023neurologicaldiseasein pages 1-2, yurchenko2023genomicmutationlandscape pages 1-2, kobaisi2024syntheticrescueof pages 1-2, NCT00002811 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor:** Germline (biallelic) pathogenic variants in DNA repair genes. XP is caused by mutations in NER genes (XPA–XPG; ERCC-family genes; DDB2) or POLH (translesion synthesis). (yurchenko2023genomicmutationlandscape pages 1-2, garciamoreno2023neurologicaldiseasein pages 1-2)

**Environmental trigger:** UV radiation exposure acts as the dominant environmental driver of DNA damage leading to photosensitivity and carcinogenesis in XP, motivating rigorous photoprotection as the key preventive/therapeutic strategy. (srivastava2021xerodermapigmentosum pages 2-5, NCT03445052 chunk 1)

### 2.2 Risk factors
* **Genetic:** Genotype determines mechanism (GG-NER vs TC-NER vs TLS) and influences risk of neurodegeneration and some clinical patterns (see Sections 4 and 6). (garciamoreno2023neurologicaldiseasein pages 1-2, sagun2024differentgermlinevariants pages 1-2)
* **Environmental:** UV exposure intensity and cumulative exposure are major modifiers of cutaneous carcinogenesis (behavioral adherence is therefore clinically critical). (NCT03445052 chunk 1)

### 2.3 Protective factors
* **Environmental/behavioral:** Effective, sustained UV avoidance and photoprotection reduce UVR reaching the face and are the only proven strategy to prevent skin cancer and eye disease in XP; this is the explicit basis for the XPAND behavioral intervention trial. (NCT03445052 chunk 1, srivastava2021xerodermapigmentosum pages 2-5)

### 2.4 Gene–environment interactions
XP is the archetypal gene–environment interaction disorder: impaired repair of UV-induced lesions causes disproportionate mutagenesis and carcinogenesis under UV exposure, and conversely, strict reduction of UV exposure is expected to reduce mutational input and cancer burden. Tumor-genome data directly demonstrate UV-mutagenesis patterns (e.g., CC>TT signatures) in XP skin cancers. (yurchenko2023genomicmutationlandscape pages 3-5, NCT03445052 chunk 1)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with suggested HPO terms)
Below is a high-yield phenotype list with ontology suggestions (HPO terms are suggested conceptually; exact IDs are not asserted when not tool-verified):

**Cutaneous**
* Severe photosensitivity / exaggerated sunburn reactions (HP: Photosensitivity)
* Freckling / lentigines and pigmentary changes (HP: Freckling; HP: Hyperpigmentation; HP: Hypopigmentation)
* Telangiectasia, atrophy, xerosis / premature photoaging (HP: Telangiectasia; HP: Cutaneous atrophy; HP: Xerosis)
* Multiple early-onset skin cancers: basal cell carcinoma, squamous cell carcinoma, melanoma (HP: Basal cell carcinoma; HP: Squamous cell carcinoma; HP: Melanoma)
  * Clinical management text describes early detection and treatment of premalignant/malignant lesions as central. (srivastava2021xerodermapigmentosum pages 2-5)

**Ophthalmological**
* Ocular UV sensitivity and damage requiring ophthalmologic surveillance (HP: Photophobia; HP: Keratitis) (not numerically quantified in tool evidence, but included in management follow-up recommendations). (srivastava2021xerodermapigmentosum pages 2-5)

**Neurological (subset, genotype-enriched)**
UK prospective cohort quantified neurological burden and progression:
* Neurological symptoms in **36/93 (38.7%)** of XP patients. (garciamoreno2023neurologicaldiseasein pages 1-2)
* Cerebellar ataxia progression tracked by SARA; significant annual progression in XPD (**0.91 points/year**, 95% CI 0.61–1.21) and XPA (**0.63 points/year**, 95% CI 0.38–0.89). (garciamoreno2023neurologicaldiseasein pages 1-2)
* Cognitive impairment shows strong genotype dependence (percentages by complementation group): XPA **58.4%**, XPC **17.6%**, XPD **85.0%**, XPE **15.1%**, XPG **83.2%**, XPV **4.3%**. (garciamoreno2023neurologicaldiseasein pages 10-11)
* Sensorineural hearing loss in **28/93 (30.1%)**. (garciamoreno2023neurologicaldiseasein pages 12-13)

Suggested HPO terms: HP: Cerebellar ataxia; HP: Cognitive impairment; HP: Sensorineural hearing impairment; HP: Peripheral neuropathy; HP: Hyporeflexia.

### 3.2 Age of onset, severity, and progression
* The UK cohort supports that neurological symptoms typically occur after cutaneous/ophthalmologic symptoms and include early- and late-onset forms with genotype clustering in XPA/XPD/XPG. (garciamoreno2023neurologicaldiseasein pages 1-2)
* XP-A genotype–neurodegeneration associations can be stratified into severe/intermediate/mild categories using a scoring approach at age 10 in a US natural-history cohort (n=18). (sagun2024differentgermlinevariants pages 1-2)

### 3.3 Quality-of-life impacts
XP is highly QoL-limiting due to lifelong UV avoidance, frequent procedures for lesions/cancers, and potential neurologic disability. XPAND explicitly targets adherence barriers to photoprotection because inadequate photoprotection increases cancer burden and life-threatening melanoma risk. (NCT03445052 chunk 1)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and complementation groups
XP is defined by biallelic pathogenic variants in **eight genotypes** (XPA, XPB/ERCC3, XPC, XPD/ERCC2, XPE/DDB2, XPF/ERCC4, XPG/ERCC5, and XPV/POLH). (garciamoreno2023neurologicaldiseasein pages 1-2)

| XP group / genotype | Causal gene | Core pathway role | Neurological involvement | High-signal recent evidence |
|---|---|---|---|---|
| XPA | **XPA** | Damage verification/scaffold in NER pre-incision complex; coordinates repair factors in GG-NER and TC-NER | **Yes, often prominent**; among the groups with the greatest neurologic burden and measurable progression | UK prospective cohort: XPA had frequent neurologic symptoms and significant SARA progression (~0.63 points/year); mutation severity correlated with faster progression. 2024 XP-A natural-history/genotype study linked variant class/location to severe, intermediate, or mild neurodegeneration. Management overview relevant for surveillance/supportive care. (garciamoreno2023neurologicaldiseasein pages 1-2, sagun2024differentgermlinevariants pages 1-2, srivastava2021xerodermapigmentosum pages 2-5) |
| XPB | **ERCC3 (XPB)** | TFIIH DNA translocase/helicase activity for DNA opening during NER; also transcription factor function | **Variable / can occur**; less common due to rarity, but neurologic disease can occur, especially in combined NER/transcription phenotypes | NER overview places XPB in TFIIH-mediated unwinding; UK cohort included very few XPB cases, limiting precision, but background notes combined GG-NER/TC-NER defect groups are more prone to neurodegeneration. Management overview relevant. (srivastava2021xerodermapigmentosum pages 2-5, garciamoreno2023neurologicaldiseasein pages 3-4, garciamoreno2023neurologicaldiseasein pages 2-3) |
| XPC | **XPC** | Primary lesion recognition in **global-genome NER (GG-NER)**; damage sensing/handover to TFIIH | **Usually no or mild/variable**; neurologic involvement uncommon but not absent | UK cohort: only 2/22 XPC patients (9.1%) had neurologic symptoms. 2024 XP-C rescue study identified PIK3C3 knockdown as an experimental synthetic-rescue strategy. 2023 skin-cancer genomics showed strong mutational burden/signature effects in XP-C tumors. Management overview relevant. (garciamoreno2023neurologicaldiseasein pages 10-11, kobaisi2024syntheticrescueof pages 1-2, yurchenko2023genomicmutationlandscape pages 1-2, srivastava2021xerodermapigmentosum pages 2-5) |
| XPD | **ERCC2 (XPD)** | TFIIH 5'→3' helicase/translocase for lesion verification and DNA opening in NER | **Yes, often prominent**; one of the groups with fastest neurologic progression | UK prospective cohort: XPD showed high neurologic burden and fastest reported SARA progression (~0.91 points/year), with frequent cognitive impairment, neuropathy, hearing loss, and MRI abnormalities. Mechanistic work also supports XPD as core NER motor protein. Management overview relevant. (garciamoreno2023neurologicaldiseasein pages 1-2, garciamoreno2023neurologicaldiseasein pages 10-11, garciamoreno2023neurologicaldiseasein pages 11-12, srivastava2021xerodermapigmentosum pages 2-5) |
| XPE | **DDB2 (XPE)** | UV-photoproduct recognition in GG-NER (especially CPD/6-4PP recognition with DDB complex), facilitates XPC recruitment | **Usually no / low frequency** | UK cohort found no neurologic complaints in XPE in this series. 2023 tumor-genome study showed XP-E tumors can have very high mutation burden, supporting strong skin-cancer susceptibility despite limited neurologic disease. Management overview relevant. (garciamoreno2023neurologicaldiseasein pages 9-10, yurchenko2023genomicmutationlandscape pages 1-2, srivastava2021xerodermapigmentosum pages 2-5) |
| XPF | **ERCC4 (XPF)** | Structure-specific endonuclease; 5' incision in NER with ERCC1 | **Variable**; can be mild in founder intronic forms, but neurologic disease exists in some XP-F/overlap cases | 2023 PNAS identified deep intronic **ERCC4/XPF** founder mutations in 17 Japanese XP-F cases; one founder allele accounts for ~10% of Japanese XP, with early-onset skin cancers and generally typical XP-F cutaneous disease, and ASOs restored XPF expression/repair in cells. UK cohort had few XPF cases, limiting neurologic estimates. Management overview relevant. (senju2023deepintronicfounder pages 1-2, senju2023deepintronicfounder pages 5-6, senju2023deepintronicfounder pages 2-3, garciamoreno2023neurologicaldiseasein pages 2-3, srivastava2021xerodermapigmentosum pages 2-5) |
| XPG | **ERCC5 (XPG)** | Structure-specific endonuclease; 3' incision in NER; also stabilizes repair complex | **Yes, often prominent** | UK cohort: XPG grouped with XPA/XPD as having high SARA scores, frequent cognitive impairment, hearing loss, MRI abnormalities, and substantial disability. Management overview relevant. (garciamoreno2023neurologicaldiseasein pages 1-2, garciamoreno2023neurologicaldiseasein pages 10-11, garciamoreno2023neurologicaldiseasein pages 11-12, srivastava2021xerodermapigmentosum pages 2-5) |
| XPV | **POLH** | **Translesion synthesis (TLS)** polymerase eta; error-free bypass of UV photolesions, especially CPDs; not a core NER factor | **Usually no / low frequency, but subtle abnormalities reported** | UK cohort reported no neurologic complaints in XPV, though some exam/ancillary abnormalities were detected. 2023 skin-cancer genomics showed XP-V tumors have distinctive mutational spectra and high TMB linked to POLH deficiency. Management overview relevant. (garciamoreno2023neurologicaldiseasein pages 9-10, garciamoreno2023neurologicaldiseasein pages 11-12, yurchenko2023genomicmutationlandscape pages 1-2, yurchenko2023genomicmutationlandscape pages 9-11, srivastava2021xerodermapigmentosum pages 2-5) |


*Table: This table summarizes the main xeroderma pigmentosum complementation groups, their causal genes, core repair roles, and whether neurologic involvement is typical or variable. It emphasizes high-yield 2023-2024 evidence plus a practical management overview source useful for clinical interpretation.*

### 4.2 Pathogenic variant classes and functional consequences
* XP results from loss-of-function or hypomorphic variants that reduce NER or TLS capacity; the management-focused mechanism summary describes lesion recognition (XPE/XPC), TFIIH-dependent opening (XPB/XPD), and dual incision by XPG (3′) and XPF/ERCC1 (5′). (srivastava2021xerodermapigmentosum pages 2-5)

**Genotype–phenotype (2024 XP-A focus):**
* A 2024 study of 18 XP-A patients (1973–2023) reports that variant type/location correlates with neurologic severity (severe vs intermediate vs mild) and that reduced repair is greatest in severe disease. (sagun2024differentgermlinevariants pages 1-2)

**Founder deep intronic variants (2023 XP-F in Japan):**
* Senju et al. identified **17 XP-F** cases with deep intronic ERCC4/XPF founder variants; an intron 1 founder allele (c.207+196T>A) has **MAF ~1/508** and accounts for ~10% of Japanese XP cases; ASOs restored XPF protein and DNA repair activity in cells, motivating precision ASO therapeutics and inclusion of this variant in routine genetic testing for Japanese XP. (senju2023deepintronicfounder pages 5-6, senju2023deepintronicfounder pages 1-2)

### 4.3 Allele frequencies / population genetics
* Japan has substantially higher XP prevalence than the US/Europe in recent synthesis: ~**1 in 22,000** in Japan vs ~**1 in 1,000,000** in the US/Europe (reported in 2024 XP-A paper background). (sagun2024differentgermlinevariants pages 1-2)
* Japanese founder ERCC4/XPF intron 1 allele MAF ~**0.002** and high contribution to national XP burden. (senju2023deepintronicfounder pages 1-2, senju2023deepintronicfounder pages 5-6)

### 4.4 Modifier genes (emerging)
A 2024 XP-C experimental study suggests cellular pathways outside canonical NER can modulate XP-C cellular phenotypes:
* In XP-C cells, PIK3C3 downregulation increased post-UV survival and promoted **~20% repair of 6-4 photoproducts**, with a major UVB resistance shift (LD50 **0.056 J/cm²** vs **0.013 J/cm²** control), implicating autophagy/UVRAG-linked regulation as a phenotype modifier and potential therapeutic target class (preclinical). (kobaisi2024syntheticrescueof pages 2-5, kobaisi2024syntheticrescueof pages 1-2)

### 4.5 Genetic testing approaches (current practice patterns)
* Diagnosis and trial eligibility often rely on functional DNA repair testing such as **unscheduled DNA synthesis (UDS)** assays (explicit inclusion criterion in the T4N5 chemoprevention trial) and genetic characterization, with complementation and sequencing used in national services. (NCT00002811 chunk 1, garciamoreno2023neurologicaldiseasein pages 1-2)

---

## 5. Epidemiology and Prognosis

### 5.1 Epidemiology
* Prevalence estimates cited in 2024 XP-A work: ~**1/1,000,000** (US/Europe) and ~**1/22,000** (Japan). (sagun2024differentgermlinevariants pages 1-2)
* A historical review excerpt reports incidence <1:1,000,000 in the USA/Europe and ~10-fold higher in more isolated populations, with consanguinity ~30% of cases (older data, used here only as context). (schubert2019xerodermapigmentosumand pages 5-6)

### 5.2 Cancer risk (statistics from recent studies)
**Magnitude of risk:**
* 2023 tumor-genome study summarizes XP as having increased skin cancer risk reaching “**several thousand-fold**” for some groups, and provides explicit magnitudes: up to **10,000-fold** increased risk for non-melanoma skin cancer and **2,000-fold** for melanoma; it also notes ~**34-fold** increased risk of internal tumors (epidemiological evidence). (yurchenko2023genomicmutationlandscape pages 1-2)

**Mutation burden as a mechanistic correlate (2023):**
* XP tumors (GG-NER defects: XP-C/XP-E; TLS defect: XP-V) “harbor **3.6-fold more mutations** than sporadic skin cancers, on average.” (yurchenko2023genomicmutationlandscape pages 9-11)
* UV-signature CC>TT double-base substitutions are enriched (e.g., XP-C ~0.2 vs sporadic ~0.03 in one comparison), supporting overwhelming UV mutational input when repair is defective. (yurchenko2023genomicmutationlandscape pages 1-2)

### 5.3 Neurologic prognosis
* Neurological disease is common and progressive in genotype-enriched groups, with measurable annual progression in SARA for XPA and XPD (see Section 3). Mutation severity score can function as a prognostic stratification variable for progression in XPA and XPD and for ADL decline in XPA. (garciamoreno2023neurologicaldiseasein pages 1-2)

---

## 6. Diagnostics

### 6.1 Clinical diagnosis
XP diagnosis is based on clinical features (early photosensitivity, pigmentary change, early skin cancers) plus confirmatory laboratory/genetic evidence. A management-focused description emphasizes multidisciplinary follow-up (pediatrics, dermatology, ophthalmology, neurology). (srivastava2021xerodermapigmentosum pages 2-5)

### 6.2 Functional laboratory tests
* **UDS (unscheduled DNA synthesis) assays** are explicitly used as a diagnostic confirmation method (e.g., inclusion for T4N5 trial; and as part of national cohort diagnostic workflows). (NCT00002811 chunk 1, garciamoreno2023neurologicaldiseasein pages 1-2)

### 6.3 Genetic testing
* Genotype classification across XPA, XPB, XPC, XPD, XPE, XPF, XPG, XPV is core for prognosis (neurological risk), surveillance, and trial stratification; deep intronic founder ERCC4 variants highlight the need to consider non-coding pathogenic alleles in specific populations. (garciamoreno2023neurologicaldiseasein pages 1-2, senju2023deepintronicfounder pages 5-6)

### 6.4 Differential diagnosis
Not systematically retrievable from tool evidence in this run; however, clinical-trial eligibility explicitly excludes overlap syndromes (Cockayne syndrome, trichothiodystrophy) for some interventions, reflecting key differentials among NER disorders. (NCT00002811 chunk 1)

---

## 7. Treatment and Current Applications (real-world implementation)

### 7.1 Core standard of care (real-world)
* There is no curative therapy; **UV avoidance and photoprotection** plus early lesion detection/treatment are foundational. (srivastava2021xerodermapigmentosum pages 2-5)
* Recommended care includes “Regular paediatric, dermatological, ophthalmological and neurological follow-up.” (srivastava2021xerodermapigmentosum pages 2-5)

**MAXO suggestions (not ID-verified):** photoprotection; dermatologic surveillance; excision/ablation of premalignant lesions; topical field therapies; systemic chemoprevention; genetic counseling.

### 7.2 Chemoprevention and lesion-directed therapies
A clinical summary lists:
* **Oral isotretinoin** (chemoprevention) (srivastava2021xerodermapigmentosum pages 2-5)
* Treatment of actinic keratoses and skin cancers by local therapies; topical agents (e.g., imiquimod, fluorouracil) are referenced as part of management options (not quantified here). (srivastava2021xerodermapigmentosum pages 2-5)

### 7.3 DNA repair enzyme topical therapy (historical but still informative)
**T4N5 liposome lotion trial (Phase 3 chemoprevention):**
* NCT00002811: randomized, double-blind, multicenter trial comparing **T4 endonuclease V (T4N5) liposome lotion** vs placebo to reduce actinic keratoses and protect against UV skin damage in XP. Enrollment projected 6–30; randomized 2:1 T4N5:placebo; diagnosis confirmed by UDS assay; ages 2–60. (NCT00002811 chunk 1)

### 7.4 Behavioral intervention to improve photoprotection (implementation science)
**XPAND Trial (NCT03445052):**
* RCT testing a tailored adherence intervention to reduce UVR dose to the face, measured via wrist dosimeter (SEDs) plus 15-minute interval diary weighting for protection behaviors; target sample size 24 (15 actual enrolled). The intervention uses seven sessions and behavior-change techniques and motivational interviewing. (NCT03445052 chunk 2)

### 7.5 Melanocortin pathway photoprotection strategy (clinical trials; 2023 updates)
**Afamelanotide (SCENESSE®) Phase IIa studies:**
* **NCT05159752 (CUV156)**: open-label Phase IIa in **XP-C**, evaluating safety and efficacy; primary endpoint change in **minimal erythema dose (MED)** baseline to day 76; secondary endpoints include UV-induced DNA damage/repair capacity, skin severity measures, melanin density, and QoL tools; afamelanotide implant administered every two weeks for 12 weeks (n=6 planned). Last update posted 2023-06-18; primary completion estimated 2024-03. (NCT05159752 chunk 1)
* **NCT05370235 (CUV152)**: open-label Phase IIa in **XP-C and XP-V**, primary endpoints MED change for each genotype; similar DNA damage/repair and QoL endpoints; recruitment sites include Belgium and Spain; last update posted 2023-09-21; primary completion estimated 2024-06. (NCT05370235 chunk 1)

### 7.6 Immunotherapy and targeted therapy for XP-associated cancers
A clinical management summary lists immunotherapies and targeted agents used for advanced skin cancers in XP, including **pembrolizumab, nivolumab, cemiplimab** and **vismodegib**. (srivastava2021xerodermapigmentosum pages 2-5)

Mechanistic rationale is supported by high tumor mutational burden and UV-mutational signatures in XP skin cancers, which can increase neoantigen load and may contribute to ICI responsiveness (inference supported by tumor-genome findings and the management listing; response rates not quantified here). (yurchenko2023genomicmutationlandscape pages 1-2, srivastava2021xerodermapigmentosum pages 2-5)

---

## 8. Prevention

### 8.1 Primary prevention
**Strict UV avoidance and rigorous photoprotection** (protective clothing, sunscreen, limiting outdoor exposure) is the cornerstone preventive approach and is explicitly the only means to prevent skin cancer/eye disease in XP clinical management. (NCT03445052 chunk 1)

### 8.2 Secondary prevention
* Frequent dermatologic surveillance and early treatment of premalignant lesions (actinic keratoses) and skin cancers is a major management theme and the basis for prevention trials (e.g., T4N5). (srivastava2021xerodermapigmentosum pages 2-5, NCT00002811 chunk 1)

### 8.3 Tertiary prevention
* Disability prevention and symptomatic management for neurologic disease: no effective disease-modifying therapy for neurodegeneration is noted in clinical overview; however, validated scales (SARA, ADL) now quantify progression and can support monitoring and future clinical trials. (srivastava2021xerodermapigmentosum pages 2-5, garciamoreno2023neurologicaldiseasein pages 1-2)

---

## 9. Mechanism / Pathophysiology (molecular-to-clinical causal chain)

### 9.1 Core mechanism: defective NER or TLS
**Upstream trigger:** UV exposure induces bulky DNA photoproducts.

**Molecular defect (NER):** Damage recognition by XPE/XPC, assembly/verification via XPA/RPA and TFIIH, DNA unwinding by XPB/XPD, dual incision by XPG and XPF/ERCC1, followed by repair synthesis/ligation. (srivastava2021xerodermapigmentosum pages 2-5)

**Variant mechanism (XPV):** Defect in POLH compromises error-free bypass of UV lesions during replication, altering mutational spectra. (yurchenko2023genomicmutationlandscape pages 9-11, yurchenko2023genomicmutationlandscape pages 1-2)

**Downstream consequences:** Failure to remove/bypass UV lesions causes mutations with characteristic UV signatures, high tumor mutation burden, and carcinogenesis; neurologic disease arises in subsets (often those with combined GG-NER/TC-NER disruption). (yurchenko2023genomicmutationlandscape pages 3-5, garciamoreno2023neurologicaldiseasein pages 1-2)

### 9.2 Tumor genomics as mechanistic readout (2023)
* XP skin cancers show markedly elevated mutational burden and enrichment for UV-associated mutation classes; GG-NER-defective and POLH-defective tumors exhibit distinctive patterns, and overall XP tumors average **3.6-fold** more mutations than sporadic skin cancers. (yurchenko2023genomicmutationlandscape pages 9-11)

### 9.3 Neurological disease mechanisms (current evidence)
The 2023 prospective cohort links genotype to neurologic progression and disability, establishing clinical endpoints (SARA/ADL) and demonstrating mutation-severity association with progression in XPA/XPD. While mechanistic hypotheses (e.g., endogenous lesions such as cyclopurines) are discussed, the key evidence here is phenotypic quantification and genotype stratification. (garciamoreno2023neurologicaldiseasein pages 1-2)

**Suggested GO biological-process terms (conceptual):** nucleotide excision repair; response to UV; DNA damage recognition; DNA helicase activity; DNA incision, 5′/3′ endonuclease activity; translesion synthesis; regulation of apoptosis.

**Suggested CL cell types (conceptual):** keratinocyte; melanocyte; fibroblast; peripheral neuron; cochlear neuron.

---

## 10. Anatomical structures affected

**Primary:** skin (UV-exposed areas), eyes; in neurologic XP, brain (cerebellum/global atrophy), peripheral nervous system (neuropathy), auditory system (cochlear involvement). (garciamoreno2023neurologicaldiseasein pages 1-2, garciamoreno2023neurologicaldiseasein pages 12-13)

**Suggested UBERON terms (conceptual):** skin; epidermis; cornea; retina; cerebellum; peripheral nerve; cochlea.

---

## 11. Temporal development

* XP is typically recognized in early life due to photosensitivity and pigmentary change; neurologic disease may present later and progresses measurably in XPA and XPD (annual SARA increases). (garciamoreno2023neurologicaldiseasein pages 1-2)

---

## 12. Inheritance and population

* **Inheritance:** autosomal recessive (explicitly stated in clinical trial description and cohort literature). (NCT03445052 chunk 1)
* **Population structure:** founder effects can markedly influence national case distributions (e.g., Japanese ERCC4/XPF deep intronic founder allele). (senju2023deepintronicfounder pages 5-6)

---

## 13. Other species / natural disease and 14. Model organisms
Model organism and cross-species natural disease information were not retrievable from the tool-accessible evidence in this run; therefore, no curated statements are made here.

---

## 15. Recent developments and latest research highlights (2023–2024)

1) **Neurologic natural history and endpoints (Brain, Dec 2023):** 93-patient prospective cohort; neurological symptoms in 38.7%; genotype-specific frequencies; quantified progression in XPA and XPD; proposes mutation severity as a prognostic biomarker for trial stratification. Publication date: Dec 2023. URL: https://doi.org/10.1093/brain/awad266 (garciamoreno2023neurologicaldiseasein pages 1-2)

2) **XP-A genotype–neurodegeneration correlation (PLOS Genetics, Dec 2024):** 18 XP-A patients examined across 1973–2023; XPA variant type/location associated with severe/intermediate/mild neurodegeneration; reinforces >1000-fold skin-cancer risk framing and provides contemporary prevalence estimates. Publication date: Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011265 (sagun2024differentgermlinevariants pages 1-2)

3) **Tumor genome landscape (Nature Communications, May 2023):** 38 XP skin-cancer genomes; high mutation burdens, UV signatures, and group-specific mutation patterns; provides quantitative risk magnitudes (up to 10,000-fold non-melanoma, 2,000-fold melanoma) and internal tumor risk framing. Publication date: May 2023. URL: https://doi.org/10.1038/s41467-023-38311-0 (yurchenko2023genomicmutationlandscape pages 1-2)

4) **Precision therapeutics for founder deep intronic variants (PNAS, Jun 2023):** ERCC4/XPF deep intronic founder alleles in Japan; ASO correction restores repair in patient cells; recommends including founder intron variant in testing. Publication date: Jun 2023. URL: https://doi.org/10.1073/pnas.2217423120 (senju2023deepintronicfounder pages 5-6)

5) **Synthetic rescue strategy in XP-C (Cell Death & Disease, Nov 2024):** kinase siRNA screen identifies PIK3C3; knockdown yields ~20% 6-4PP repair and improves UVB resistance (LD50 shift); supports autophagy/UVRAG-linked modulation as a potential therapeutic direction. Publication date: Nov 2024. URL: https://doi.org/10.1038/s41419-024-07186-4 (kobaisi2024syntheticrescueof pages 2-5)

---

## Notes on evidence limitations
* **PMIDs:** The tool-accessible excerpts provided DOIs and journal metadata but did not reliably surface PMIDs for the key 2023–2024 sources; therefore, PMIDs are not asserted.
* **MONDO/Orphanet/ICD identifiers:** Not available from tool evidence in this run.
* **Model organism evidence:** Not available from tool evidence in this run.

---

## Key data points (quick reference)
* Neurologic symptoms: **38.7% (36/93)** in UK cohort; SARA progression **0.91 points/year** (XPD) and **0.63 points/year** (XPA). (garciamoreno2023neurologicaldiseasein pages 1-2)
* Cognitive impairment frequencies: XPD **85.0%**, XPG **83.2%**, XPA **58.4%**, XPC **17.6%**, XPV **4.3%**. (garciamoreno2023neurologicaldiseasein pages 10-11)
* Skin cancer risk magnitude: up to **10,000-fold** (non-melanoma) and **2,000-fold** (melanoma) increases reported in 2023 tumor-genome study background. (yurchenko2023genomicmutationlandscape pages 1-2)
* Tumor mutational burden: XP tumors average **3.6-fold** more mutations than sporadic skin cancers. (yurchenko2023genomicmutationlandscape pages 9-11)
* Founder ERCC4 intron 1 allele: MAF **~1/508**, accounting for **~10%** of Japanese XP; ASOs restore repair in cells. (senju2023deepintronicfounder pages 5-6)
* Clinical trials: T4N5 topical DNA repair enzyme lotion (NCT00002811) (NCT00002811 chunk 1); afamelanotide Phase IIa studies (NCT05159752, NCT05370235) with MED and DNA damage endpoints (NCT05159752 chunk 1, NCT05370235 chunk 1); photoprotection adherence RCT XPAND (NCT03445052) using dosimetry (NCT03445052 chunk 2).


References

1. (garciamoreno2023neurologicaldiseasein pages 1-2): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

2. (sagun2024differentgermlinevariants pages 1-2): Jeffrey P. Sagun, Sikandar G. Khan, Kyoko Imoto, Deborah Tamura, Kyu-Seon Oh, John J. DiGiovanna, and Kenneth H. Kraemer. Different germline variants in the xpa gene are associated with severe, intermediate, or mild neurodegeneration in xeroderma pigmentosum patients. Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011265, doi:10.1371/journal.pgen.1011265. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (yurchenko2023genomicmutationlandscape pages 1-2): Andrey A. Yurchenko, Fatemeh Rajabi, Tirzah Braz-Petta, Hiva Fassihi, Alan Lehmann, Chikako Nishigori, Jinxin Wang, Ismael Padioleau, Konstantin Gunbin, Leonardo Panunzi, Fanny Morice-Picard, Pierre Laplante, Caroline Robert, Patricia L. Kannouche, Carlos F. M. Menck, Alain Sarasin, and Sergey I. Nikolaev. Genomic mutation landscape of skin cancers from dna repair-deficient xeroderma pigmentosum patients. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38311-0, doi:10.1038/s41467-023-38311-0. This article has 49 citations and is from a highest quality peer-reviewed journal.

4. (senju2023deepintronicfounder pages 1-2): Chikako Senju, Yuka Nakazawa, Taichi Oso, Mayuko Shimada, Kana Kato, Michiko Matsuse, Mariko Tsujimoto, Taro Masaki, Yasushi Miyazaki, Satoshi Fukushima, Satoshi Tateishi, Atsushi Utani, Hiroyuki Murota, Katsumi Tanaka, Norisato Mitsutake, Shinichi Moriwaki, Chikako Nishigori, and Tomoo Ogi. Deep intronic founder mutations identified in the ercc4/xpf gene are potential therapeutic targets for a high-frequency form of xeroderma pigmentosum. Proceedings of the National Academy of Sciences of the United States of America, Jun 2023. URL: https://doi.org/10.1073/pnas.2217423120, doi:10.1073/pnas.2217423120. This article has 14 citations and is from a highest quality peer-reviewed journal.

5. (kobaisi2024syntheticrescueof pages 1-2): Farah Kobaisi, Eric Sulpice, Ali Nasrallah, Patricia Obeïd, Hussein Fayyad-Kazan, Walid Rachidi, and Xavier Gidrol. Synthetic rescue of xeroderma pigmentosum c phenotype via pik3c3 downregulation. Cell Death &amp; Disease, Nov 2024. URL: https://doi.org/10.1038/s41419-024-07186-4, doi:10.1038/s41419-024-07186-4. This article has 2 citations and is from a peer-reviewed journal.

6. (srivastava2021xerodermapigmentosum pages 2-5): Gautam Srivastava and G. Srivastava. Xeroderma pigmentosum. Oxford Medical Case Reports, Jan 2021. URL: https://doi.org/10.1093/omcr/omab107, doi:10.1093/omcr/omab107. This article has 3 citations and is from a peer-reviewed journal.

7. (NCT05159752 chunk 1):  A Study to Evaluate the Safety and Efficacy of Afamelanotide in Patients With Xeroderma Pigmentosum (XP). Clinuvel Europe Limited. 2021. ClinicalTrials.gov Identifier: NCT05159752

8. (schubert2019xerodermapigmentosumand pages 5-6): Steffen Schubert and Steffen Emmert. Xeroderma pigmentosum and related diseases. ArXiv, pages 1743-1768, Dec 2019. URL: https://doi.org/10.1002/9781119142812.ch138, doi:10.1002/9781119142812.ch138. This article has 3 citations.

9. (NCT00002811 chunk 1):  T4N5 Liposome Lotion Compared With Placebo Lotion for Preventing Actinic Keratoses in Patients With Xeroderma Pigmentosum. Applied Genetics. 1996. ClinicalTrials.gov Identifier: NCT00002811

10. (NCT03445052 chunk 1):  XPAND Trial: Enhancing XP Photoprotection Activities - New Directions. Guy's and St Thomas' NHS Foundation Trust. 2018. ClinicalTrials.gov Identifier: NCT03445052

11. (yurchenko2023genomicmutationlandscape pages 3-5): Andrey A. Yurchenko, Fatemeh Rajabi, Tirzah Braz-Petta, Hiva Fassihi, Alan Lehmann, Chikako Nishigori, Jinxin Wang, Ismael Padioleau, Konstantin Gunbin, Leonardo Panunzi, Fanny Morice-Picard, Pierre Laplante, Caroline Robert, Patricia L. Kannouche, Carlos F. M. Menck, Alain Sarasin, and Sergey I. Nikolaev. Genomic mutation landscape of skin cancers from dna repair-deficient xeroderma pigmentosum patients. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38311-0, doi:10.1038/s41467-023-38311-0. This article has 49 citations and is from a highest quality peer-reviewed journal.

12. (garciamoreno2023neurologicaldiseasein pages 10-11): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (garciamoreno2023neurologicaldiseasein pages 12-13): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

14. (garciamoreno2023neurologicaldiseasein pages 3-4): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (garciamoreno2023neurologicaldiseasein pages 2-3): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

16. (garciamoreno2023neurologicaldiseasein pages 11-12): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (garciamoreno2023neurologicaldiseasein pages 9-10): Hector Garcia-Moreno, Douglas R Langbehn, Adesoji Abiona, Isabel Garrood, Zofia Fleszar, Marta Antonia Manes, Ana M Susana Morley, Emma Craythorne, Shehla Mohammed, Tanya Henshaw, Sally Turner, Harsha Naik, Istvan Bodi, Robert P E Sarkany, Hiva Fassihi, Alan R Lehmann, and Paola Giunti. Neurological disease in xeroderma pigmentosum: prospective cohort study of its features and progression. Brain, 146:5044-5059, Dec 2023. URL: https://doi.org/10.1093/brain/awad266, doi:10.1093/brain/awad266. This article has 20 citations and is from a highest quality peer-reviewed journal.

18. (senju2023deepintronicfounder pages 5-6): Chikako Senju, Yuka Nakazawa, Taichi Oso, Mayuko Shimada, Kana Kato, Michiko Matsuse, Mariko Tsujimoto, Taro Masaki, Yasushi Miyazaki, Satoshi Fukushima, Satoshi Tateishi, Atsushi Utani, Hiroyuki Murota, Katsumi Tanaka, Norisato Mitsutake, Shinichi Moriwaki, Chikako Nishigori, and Tomoo Ogi. Deep intronic founder mutations identified in the ercc4/xpf gene are potential therapeutic targets for a high-frequency form of xeroderma pigmentosum. Proceedings of the National Academy of Sciences of the United States of America, Jun 2023. URL: https://doi.org/10.1073/pnas.2217423120, doi:10.1073/pnas.2217423120. This article has 14 citations and is from a highest quality peer-reviewed journal.

19. (senju2023deepintronicfounder pages 2-3): Chikako Senju, Yuka Nakazawa, Taichi Oso, Mayuko Shimada, Kana Kato, Michiko Matsuse, Mariko Tsujimoto, Taro Masaki, Yasushi Miyazaki, Satoshi Fukushima, Satoshi Tateishi, Atsushi Utani, Hiroyuki Murota, Katsumi Tanaka, Norisato Mitsutake, Shinichi Moriwaki, Chikako Nishigori, and Tomoo Ogi. Deep intronic founder mutations identified in the ercc4/xpf gene are potential therapeutic targets for a high-frequency form of xeroderma pigmentosum. Proceedings of the National Academy of Sciences of the United States of America, Jun 2023. URL: https://doi.org/10.1073/pnas.2217423120, doi:10.1073/pnas.2217423120. This article has 14 citations and is from a highest quality peer-reviewed journal.

20. (yurchenko2023genomicmutationlandscape pages 9-11): Andrey A. Yurchenko, Fatemeh Rajabi, Tirzah Braz-Petta, Hiva Fassihi, Alan Lehmann, Chikako Nishigori, Jinxin Wang, Ismael Padioleau, Konstantin Gunbin, Leonardo Panunzi, Fanny Morice-Picard, Pierre Laplante, Caroline Robert, Patricia L. Kannouche, Carlos F. M. Menck, Alain Sarasin, and Sergey I. Nikolaev. Genomic mutation landscape of skin cancers from dna repair-deficient xeroderma pigmentosum patients. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38311-0, doi:10.1038/s41467-023-38311-0. This article has 49 citations and is from a highest quality peer-reviewed journal.

21. (kobaisi2024syntheticrescueof pages 2-5): Farah Kobaisi, Eric Sulpice, Ali Nasrallah, Patricia Obeïd, Hussein Fayyad-Kazan, Walid Rachidi, and Xavier Gidrol. Synthetic rescue of xeroderma pigmentosum c phenotype via pik3c3 downregulation. Cell Death &amp; Disease, Nov 2024. URL: https://doi.org/10.1038/s41419-024-07186-4, doi:10.1038/s41419-024-07186-4. This article has 2 citations and is from a peer-reviewed journal.

22. (NCT03445052 chunk 2):  XPAND Trial: Enhancing XP Photoprotection Activities - New Directions. Guy's and St Thomas' NHS Foundation Trust. 2018. ClinicalTrials.gov Identifier: NCT03445052

23. (NCT05370235 chunk 1):  A Study to Evaluate the Safety and Efficacy of Afamelanotide in Patients With Xeroderma Pigmentosum C and V. Clinuvel Europe Limited. 2022. ClinicalTrials.gov Identifier: NCT05370235

## Artifacts

- [Edison artifact artifact-00](Xeroderma_Pigmentosum-deep-research-falcon_artifacts/artifact-00.md)