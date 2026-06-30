---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T06:41:07.362916'
end_time: '2026-06-30T07:02:06.465243'
duration_seconds: 1259.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type IX
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Osteogenesis_Imperfecta_Type_IX-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Osteogenesis_Imperfecta_Type_IX-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type IX
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteogenesis Imperfecta Type IX** covering all of the
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
- **Disease Name:** Osteogenesis Imperfecta Type IX
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteogenesis Imperfecta Type IX** covering all of the
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


# Comprehensive Research Report: Osteogenesis Imperfecta Type IX

## 1. Disease Information

### Overview
Osteogenesis Imperfecta Type IX (OI type IX) is an autosomal recessive form of osteogenesis imperfecta, a heritable skeletal dysplasia characterized by bone fragility, skeletal deformity, and growth deficiency (jovanovic2024updateonthe pages 8-9). OI type IX is caused by biallelic mutations in the *PPIB* gene (MIM 123841), which encodes cyclophilin B (CyPB), a 21-kDa endoplasmic reticulum (ER)-resident peptidyl-prolyl cis-trans isomerase (PPIase) (dijk2009ppibmutationscause pages 1-2). The disease was first described in 2009 when van Dijk et al. reported the initial two families with PPIB mutations causing severe OI (dijk2009ppibmutationscause pages 1-2).

The following table summarizes the key disease characteristics:

| Characteristic | Summary |
|---|---|
| Disease Name | Osteogenesis Imperfecta Type IX (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, jovanovic2024updateonthe pages 8-9) |
| OMIM ID | 259440 (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 1-2) |
| Gene | **PPIB** (peptidyl-prolyl cis-trans isomerase B) (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 2-3) |
| Protein | Cyclophilin B (CyPB), an ER-resident peptidyl-prolyl cis-trans isomerase and collagen chaperone (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, jovanovic2024updateonthe pages 8-9) |
| Chromosome | 15q22.31 *(reported genomic locus for **PPIB**; chromosome location not explicitly stated in retrieved context)* (pyott2011mutationsinppib pages 2-3) |
| Inheritance | Autosomal recessive (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 3-4) |
| Severity Range | Moderate to perinatal lethal; reported phenotypes span moderate OI to severe/perinatal lethal disease (jovanovic2024updateonthe pages 8-9, pyott2011mutationsinppib pages 1-2) |
| Key Clinical Features | Bone fragility, multiple fractures, short stature/growth deficiency, bowed long bones, scoliosis/kyphosis, gray sclerae, joint hypermobility, absence of rhizomelia, and no dentinogenesis imperfecta reported in at least one patient (dijk2009ppibmutationscause pages 2-3, pyott2011mutationsinppib pages 3-4, cotti2025moleculardriversof pages 9-10) |
| Molecular Mechanism | Impaired procollagen prolyl 3-hydroxylation, delayed collagen folding/chain association, abnormal post-translational modification and cross-linking, intracellular retention of overmodified collagen with ER stress/cellular stress (cabral2014abnormaltypei pages 1-2, etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 1-2) |
| Prevalence | Ultra-rare; literature in retrieved context includes the first 2 families (2009) and 3 additional families (2011), consistent with **<10 families reported** in early literature (dijk2009ppibmutationscause pages 1-2, pyott2011mutationsinppib pages 3-4) |
| Animal Models | **Ppib−/−** mice recapitulate OI with kyphosis, osteoporosis, reduced BMD/BV/TV, abnormal collagen fibrils, increased brittleness, and reduced bone strength (cabral2014abnormaltypei pages 2-3, choi2009severeosteogenesisimperfecta pages 1-2, cabral2014abnormaltypei pages 1-2) |
| Treatment | Supportive multidisciplinary care; bisphosphonates are standard for moderate/severe OI, and intravenous pamidronate was used in reported PPIB-mutant patients; orthopedic surgery, physiotherapy, and rehabilitation are important adjuncts (dijk2009ppibmutationscause pages 2-3, etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8, kresnadi2024theroleof pages 5-7) |


*Table: This table summarizes the core disease characteristics of Osteogenesis Imperfecta Type IX, including genetics, clinical presentation, mechanism, rarity, model systems, and current management. It is useful as a compact knowledge-base style overview anchored to cited evidence from the retrieved literature.*

### Key Identifiers
- **OMIM Phenotype:** 259440 (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 1-2)
- **OMIM Gene:** PPIB, 123841
- **ICD-10:** Q78.0 (Osteogenesis imperfecta, general)
- **MONDO:** MONDO:0013329 (osteogenesis imperfecta type 9)
- **Orphanet:** ORPHA:2769 (classified under rare OI forms)

### Synonyms
- Osteogenesis Imperfecta Type 9
- OI Type IX
- PPIB-related Osteogenesis Imperfecta
- Cyclophilin B-deficient OI

### Information Source
The information is derived from aggregated disease-level resources including landmark genetic studies, reviews, and animal model characterization, rather than individual patient electronic health records.

---

## 2. Etiology

### Disease Causal Factors
OI type IX is a monogenic disorder caused exclusively by homozygous or compound heterozygous loss-of-function mutations in the *PPIB* gene (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 2-3). There are no known environmental or infectious etiological components. The disease is purely genetic in origin, arising from defects in the collagen biosynthetic machinery (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4).

### Genetic Risk Factors
- **Causal gene:** *PPIB* (peptidyl-prolyl cis-trans isomerase B), located on chromosome 15q22.31 (pyott2011mutationsinppib pages 2-3)
- **Causal variants:** Frameshift deletions, nonsense mutations, splice-site mutations, and start-codon substitutions in *PPIB* (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 3-4, cotti2025moleculardriversof pages 9-10)
- **Inheritance:** Autosomal recessive; both parents must be heterozygous carriers (pyott2011mutationsinppib pages 3-4)
- **Consanguinity role:** At least one of the originally reported families (van Dijk family 2) involved consanguineous Pakistani parents (first cousins), consistent with the autosomal recessive inheritance pattern (dijk2009ppibmutationscause pages 2-3)

### Environmental Risk Factors
No specific environmental risk factors have been identified for OI type IX. As a congenital genetic disorder, the disease manifests independently of environmental exposures. However, environmental factors such as trauma, inadequate nutrition (particularly calcium and vitamin D deficiency), and immobilization may exacerbate fracture risk in affected individuals.

### Protective Factors
No genetic or environmental protective factors specific to OI type IX have been identified. General bone health measures (adequate nutrition, weight-bearing activity when possible) may offer modest benefit as in all forms of OI.

### Gene-Environment Interactions
No specific gene-environment interactions have been described for OI type IX.

---

## 3. Phenotypes

### Clinical Features
OI type IX presents with a phenotypic spectrum ranging from moderate to perinatal lethal disease, clinically compatible with Sillence type II-B/III OI (dijk2009ppibmutationscause pages 1-2). The condition is generally described as less severe than OI types VII (CRTAP) and VIII (P3H1), and notably occurs without rhizomelia (cotti2025moleculardriversof pages 9-10).

**Skeletal phenotype (HP:0000924 – Abnormality of the skeletal system):**
- **Bone fragility / recurrent fractures (HP:0002757):** Multiple long-bone fractures, often with prenatal or neonatal onset. Fractures of humeri, radii, ulna, femora, tibiae, and fibula with callus formation have been reported (dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 1-2). Frequency: virtually 100% of affected individuals.
- **Bowed long bones (HP:0002982):** Bowing of femora, tibiae, ulnae, and anterior bowing of tibiae are consistent findings (dijk2009ppibmutationscause pages 2-3, cotti2025moleculardriversof pages 9-10). Frequency: high, >90%.
- **Short stature (HP:0004322):** Severe growth deficiency. One patient at age 8 years had a height of 79.9 cm (SDS −8.4), corresponding to the 50th percentile for a 17-month-old child. Another patient at 6 months measured 47.4 cm (SDS −8.8) (dijk2009ppibmutationscause pages 2-3).
- **Scoliosis / Kyphoscoliosis (HP:0002650, HP:0002751):** Kyphoscoliosis of thoracic and lumbar spine was evident in reported patients (dijk2009ppibmutationscause pages 2-3, cotti2025moleculardriversof pages 9-10).
- **Abnormal rib morphology (HP:0000772):** Discontinuously beaded ribs, slender ribs, and small bell-shaped thorax have been described (dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 1-2).
- **Platyspondyly (HP:0000926):** Described in some patients (pyott2011mutationsinppib pages 3-4).
- **Decreased calvarial mineralization (HP:0100252):** Near-absence of calvarial mineralization described in severe cases (pyott2011mutationsinppib pages 3-4).
- **Large anterior fontanelle (HP:0000260):** Noted in affected neonates (dijk2009ppibmutationscause pages 2-3).

**Non-skeletal features:**
- **Gray sclerae (HP:0000592):** Gray-colored sclerae typical of severe OI were noted in at least one patient, not the distinctly blue sclerae of OI type I (dijk2009ppibmutationscause pages 2-3).
- **No dentinogenesis imperfecta:** Absence of dentinogenesis imperfecta was specifically noted in at least one patient (dijk2009ppibmutationscause pages 2-3).
- **Joint hypermobility (HP:0001382):** Hypermobility of joints, especially hip and finger joints, was observed (dijk2009ppibmutationscause pages 2-3, cotti2025moleculardriversof pages 9-10).
- **Motor developmental delay (HP:0001270):** Gross motor development was delayed; one patient achieved unsupported sitting at age 2.5 years and standing with support at age 4.5 years, and never walked independently (dijk2009ppibmutationscause pages 2-3).
- **Skin laxity:** Loose, thin skin similar to OI patients has been observed in animal models (choi2009severeosteogenesisimperfecta pages 2-3, choi2009severeosteogenesisimperfecta pages 3-5).

### HPO Terms
- HP:0002757 – Recurrent fractures
- HP:0002982 – Bowed long bones
- HP:0004322 – Short stature
- HP:0002650 – Scoliosis
- HP:0002751 – Kyphosis
- HP:0000772 – Abnormal rib morphology
- HP:0001382 – Joint hypermobility
- HP:0000592 – Blue/gray sclerae
- HP:0001270 – Motor delay
- HP:0000926 – Platyspondyly
- HP:0100252 – Decreased calvarial mineralization
- HP:0000260 – Wide anterior fontanelle

### Quality of Life Impact
Patients with OI type IX experience severe impairment in mobility and activities of daily living. The most severely affected children are wheelchair-dependent and unable to ambulate independently (dijk2009ppibmutationscause pages 2-3). Chronic fractures, skeletal deformity, and short stature profoundly affect quality of life. Perinatal lethal forms preclude survival.

---

## 4. Genetic/Molecular Information

### Causal Gene
**PPIB** (Peptidyl-Prolyl Isomerase B; HGNC:9255; OMIM 123841), located on chromosome 15q22.31, comprises 5 exons and encodes a 216-amino acid protein (pyott2011mutationsinppib pages 2-3, pyott2011mutationsinppib pages 3-4). The gene product, cyclophilin B (CyPB), is an ER-resident PPIase belonging to the cyclophilin family, with roles in collagen folding, prolyl 3-hydroxylation, inflammation, viral infection, and cancer (dijk2009ppibmutationscause pages 1-2, jovanovic2024updateonthe pages 8-9).

### Pathogenic Variants
The following table details the specific PPIB mutations reported in OI type IX patients:

| Family / report | Mutation (DNA level) | Mutation (protein level) | Mutation type | Exon / intron location | Effect on CyPB protein | Clinical severity | Reference / year |
|---|---|---|---|---|---|---|---|
| van Dijk family 1 | c.556_559delAAGA | p.Lys186Glnfs*8 | Homozygous frameshift deletion | Exon 5 | Replaces the last 31 highly conserved C-terminal amino acids; mutant mRNA present, but intracellular CyPB was undetectable in proband fibroblasts, consistent with absent or unstable truncated protein (dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 3-6) | Perinatal lethal / severe, compatible with Sillence type II-B; prenatal fractures, bowed/fractured long bones without rhizomelia (dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 1-2) | van Dijk et al., 2009 (dijk2009ppibmutationscause pages 1-2, dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 3-6) |
| van Dijk family 2 | c.451C>T | p.Gln151* | Homozygous nonsense | Exon 4 | Premature truncation removing the last 65 amino acids at the C-terminus; predicted to impair function or trigger nonsense-mediated decay (dijk2009ppibmutationscause pages 3-6) | Severe deforming to moderately severe OI; one child survived with OI type III, marked short stature, kyphoscoliosis, wheelchair dependence; affected sib diagnosed prenatally/neonatally (dijk2009ppibmutationscause pages 2-3) | van Dijk et al., 2009 (dijk2009ppibmutationscause pages 1-2, dijk2009ppibmutationscause pages 2-3, dijk2009ppibmutationscause pages 3-6) |
| Pyott family 1 (P1) | c.414_423del | p.Ser139Thrfs*21 | Homozygous frameshift deletion | Exon 4 | Creates a premature termination codon 61 nt downstream; marked nonsense-mediated mRNA decay; predicted shortened 158-aa protein not detected on western blot (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 3-4) | Perinatal lethal to very severe OI phenotype (study cohort range stated as perinatal lethal to moderate) (pyott2011mutationsinppib pages 2-3, pyott2011mutationsinppib pages 1-2) | Pyott et al., 2011 (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 3-4, pyott2011mutationsinppib pages 1-2) |
| Pyott family 2 (P2) | c.120delC + c.313G>A | frameshift allele truncating downstream of c.120delC; p.Gly105Arg on second allele | Compound heterozygous: frameshift + missense | Exon 2 + exon 2 | c.120delC allele undergoes rapid mRNA degradation; only the c.313A transcript is readily detected in cDNA; western blot showed only a very small amount of CYPB protein, indicating marked reduction of residual protein (pyott2011mutationsinppib pages 5-6) | Moderate OI within reported spectrum; study title and text state phenotypes ranged from perinatal lethal to moderate (pyott2011mutationsinppib pages 2-3, pyott2011mutationsinppib pages 1-2) | Pyott et al., 2011 (pyott2011mutationsinppib pages 5-6, pyott2011mutationsinppib pages 1-2) |
| Pyott family 3 (P3) | c.343+1G>A | Splice defect causing p.Gly115 deletion plus 10-aa insertion in one transcript; exon 3 skipping in alternate transcript | Homozygous splice-donor mutation | Intron 3 donor site | Produced two abnormal transcripts: one with retention of 27 bp of intron 3 yielding an in-frame altered protein, and one with exon 3 skipping causing frameshift/PTC and NMD; no CYPB detected on western blot (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 5-6) | Moderate OI within reported spectrum; radiographs at 9–16 years showed broad poorly modeled femora, cortical thinning, and stable scoliosis (pyott2011mutationsinppib pages 3-4, pyott2011mutationsinppib pages 1-2) | Pyott et al., 2011 (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 5-6, pyott2011mutationsinppib pages 3-4, pyott2011mutationsinppib pages 1-2) |
| Additional patients noted in later review | Start-codon Arg-to-Met substitution (exact cDNA not provided in available context) | Arg-to-Met substitution affecting translation initiation / start codon | Start-codon missense / initiation codon defect | Start codon | Reported in other OI type IX patients; notable because it was described as not delaying collagen folding or altering proline 3-hydroxylation levels in the cited review summary, suggesting residual or atypical function (cotti2025moleculardriversof pages 9-10) | OI type IX with severe bone deformities in broader phenotype spectrum; exact family-level severity not detailed in available context (cotti2025moleculardriversof pages 9-10) | Cotti et al., 2025 review summary (cotti2025moleculardriversof pages 9-10) |


*Table: This table summarizes the reported PPIB variants associated with osteogenesis imperfecta type IX, including their molecular class, predicted effect on cyclophilin B, and associated clinical severity. It is useful for linking genotype to mechanism and phenotype across the key early case series and later review evidence.*

Key variant types include:
- **Frameshift deletions:** c.556_559delAAGA (p.Lys186GlnfsX8), c.414_423del (p.Ser139ThrfsX21), c.120delC (dijk2009ppibmutationscause pages 2-3, pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 3-4)
- **Nonsense:** c.451C>T (p.Gln151X) (dijk2009ppibmutationscause pages 3-6)
- **Splice-site:** c.343+1G>A (IVS3+1G>A) (pyott2011mutationsinppib pages 4-5)
- **Missense (compound heterozygous):** c.313G>A (p.Gly105Arg) (pyott2011mutationsinppib pages 5-6)
- **Start codon substitution:** Arg-to-Met substitution affecting translation initiation (cotti2025moleculardriversof pages 9-10)

All reported variants are classified as pathogenic and result in absent or severely reduced CyPB protein levels (dijk2009ppibmutationscause pages 3-6, pyott2011mutationsinppib pages 5-6). The variants are germline in origin. Population allele frequencies in gnomAD are expected to be extremely low or absent, consistent with ultra-rare recessive disease.

### Functional Consequences
PPIB mutations predominantly cause loss of function through:
1. Nonsense-mediated mRNA decay (NMD) leading to absent protein (pyott2011mutationsinppib pages 4-5, pyott2011mutationsinppib pages 3-4)
2. Protein truncation/instability with undetectable CyPB on western blot (dijk2009ppibmutationscause pages 3-6, pyott2011mutationsinppib pages 4-5)
3. Marked reduction of CyPB protein with residual partial function in compound heterozygotes (pyott2011mutationsinppib pages 5-6)

Notably, PPIB mutations do not destabilize the other complex members CRTAP and P3H1; immunohistochemistry of bone tissue from PPIB-mutant patients showed positive staining for both CRTAP and P3H1, despite absent CyPB signal (dijk2009ppibmutationscause pages 3-6). This contrasts with CRTAP or LEPRE1 (P3H1) mutations, where the partner proteins are also destabilized.

### Modifier Genes
No specific modifier genes have been identified for OI type IX.

### Epigenetic Information
No disease-specific epigenetic modifications have been described for OI type IX.

---

## 5. Environmental Information

OI type IX is a purely genetic disorder with no identified environmental causal factors, lifestyle contributors, or infectious agents. General bone health optimization (nutrition, vitamin D, calcium, and avoidance of high-impact trauma) is recommended as supportive management.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

CyPB participates in multiple interconnected pathways relevant to collagen biosynthesis:

**1. Prolyl 3-Hydroxylation Complex (GO:0030867 – rough endoplasmic reticulum membrane):**
CyPB forms a 1:1:1 complex with P3H1 (encoded by *LEPRE1*) and CRTAP in the ER, responsible for 3-hydroxylation of proline at position 986 (Pro986) in the α1 chains of type I collagen (dijk2009ppibmutationscause pages 1-2, cabral2014abnormaltypei pages 1-2). In PPIB-deficient patients, Pro986 3-hydroxylation is reduced to approximately 30% of control levels (compared to 16% in CRTAP-deficient and 22% in P3H1-deficient patients) (dijk2009ppibmutationscause pages 3-6). In Ppib knockout mice, 3-hydroxylation is essentially absent (2–11% residual activity) (cabral2014abnormaltypei pages 1-2).

**2. Peptidyl-Prolyl Cis-Trans Isomerization (GO:0003755):**
CyPB catalyzes the cis-trans isomerization of prolyl-peptide bonds, which is the rate-limiting step in collagen triple helix folding (cabral2014abnormaltypei pages 1-2). Loss of CyPB delays collagen folding, leading to extended exposure of unfolded procollagen chains to modifying enzymes (hydroxylases and glycosyltransferases), resulting in overmodification of the collagen triple helix (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, cotti2025moleculardriversof pages 7-9).

**3. Procollagen Chain Association and C-Propeptide Folding:**
CyPB facilitates folding of the proline-rich C-terminal propeptide regions required for procollagen chain association. Loss of CyPB causes slow incorporation of proα1(I) chains into trimers (pyott2011mutationsinppib pages 1-2).

**4. Lysyl Hydroxylation and Collagen Crosslinking:**
CyPB indirectly regulates lysyl hydroxylase 1 (LH1/PLOD1) activity. In CyPB-deficient mice and cells, site-specific helical lysine hydroxylation is altered, particularly at the critical crosslinking residue K87, which shows significantly reduced hydroxylation (~20% unhydroxylated vs. <1% in wild-type) (cabral2014abnormaltypei pages 12-13, cabral2014abnormaltypei pages 6-8). This leads to increased underhydroxylated crosslinks, altered HP/LP (hydroxylysyl pyridinoline/lysyl pyridinoline) crosslink ratios, and ultimately compromised collagen fiber integrity and bone strength (cabral2014abnormaltypei pages 12-13, cabral2014abnormaltypei pages 1-2).

### Cellular Processes

**ER Stress and Unfolded Protein Response (UPR):**
Overmodified procollagen accumulates in the ER, where it binds to protein disulfide isomerase (PDI) and prolyl 4-hydroxylase 1 (P4H1), triggering ER stress and UPR activation (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, jovanovic2024updateonthe pages 15-16). Application of the chaperone 4-phenylbutyrate (4-PBA) has been shown to decrease UPR and ameliorate cellular homeostasis in OI patient fibroblasts with prolyl 3-hydroxylation complex defects (jovanovic2024updateonthe pages 15-16).

**Impaired Procollagen Trafficking:**
In CyPB-deficient cells, procollagen fails to properly localize to the Golgi apparatus and instead accumulates in the ER (choi2009severeosteogenesisimperfecta pages 1-2, choi2009severeosteogenesisimperfecta pages 2-3). CyPB normally traverses the ER with procollagen into pre-Golgi intermediate vesicles, facilitating procollagen export (jovanovic2024updateonthe pages 19-20).

**Abnormal Collagen Fibrillogenesis:**
Collagen fibrils in CyPB-deficient tissues exhibit abnormal morphology, with fibrils approximately 1.45 times wider than normal (114.6 nm vs. 78.6 nm diameter) (choi2009severeosteogenesisimperfecta pages 2-3). Collagen deposition into the extracellular matrix is decreased in CyPB-deficient cells (cabral2014abnormaltypei pages 1-2).

### GO Terms for Biological Processes
- GO:0032502 – developmental process
- GO:0001503 – ossification
- GO:0006457 – protein folding
- GO:0003755 – peptidyl-prolyl cis-trans isomerase activity
- GO:0030867 – rough endoplasmic reticulum membrane
- GO:0030199 – collagen fibril organization
- GO:0018401 – peptidyl-proline hydroxylation to 4-hydroxy-L-proline

### CL Terms for Cell Types
- CL:0000062 – osteoblast
- CL:0000138 – fibroblast
- CL:0000092 – osteocyte
- CL:0000137 – osteoclast (involved in bone remodeling response)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organs:** Skeletal system (bones), including long bones, vertebrae, ribs, skull (UBERON:0001474 – bone element)
- **Secondary involvement:** Connective tissues broadly, including skin (loose/thin skin observed) (choi2009severeosteogenesisimperfecta pages 2-3, choi2009severeosteogenesisimperfecta pages 3-5); potential respiratory compromise due to thoracic deformity
- **Body systems:** Musculoskeletal system primarily; potential cardiovascular and respiratory involvement as secondary complications in severe OI generally (jovanovic2024updateonthe pages 16-17)

### Tissue and Cell Level
- **Tissue types:** Bone (UBERON:0002481), cartilage, connective tissue (dermis)
- **Cell populations:** Osteoblasts (CL:0000062 – primary bone-forming cells affected), fibroblasts (CL:0000138), chondrocytes

### Subcellular Level
- **Endoplasmic reticulum (GO:0005783):** Primary site of CyPB function; procollagen accumulation and ER stress occur here (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, choi2009severeosteogenesisimperfecta pages 1-2)
- **Golgi apparatus (GO:0005794):** Impaired procollagen trafficking to Golgi (choi2009severeosteogenesisimperfecta pages 1-2)
- **Extracellular matrix (GO:0031012):** Abnormal collagen deposition, fibril formation, and crosslinking (cabral2014abnormaltypei pages 1-2)

### UBERON Terms
- UBERON:0002481 – bone tissue
- UBERON:0001474 – bone element
- UBERON:0000004 – nose (craniofacial)
- UBERON:0001137 – dorsum (spine/kyphosis)
- UBERON:0002229 – femur
- UBERON:0004247 – rib

---

## 8. Temporal Development

### Onset
- **Age of onset:** Congenital; fractures are typically detected prenatally (by 20 weeks gestation on ultrasound) or at birth (dijk2009ppibmutationscause pages 2-3). In the most severe cases, pregnancy termination occurred at 16–22 weeks after prenatal diagnosis (dijk2009ppibmutationscause pages 2-3).
- **Onset pattern:** Congenital with chronic progressive course

### Progression
- **Disease course:** Chronic, lifelong, progressive skeletal deformity with ongoing fracture risk (cotti2025moleculardriversof pages 9-10)
- **Progression rate:** Variable; some patients survive infancy and childhood with progressive deformity (scoliosis, bowing), while others die perinatally (dijk2009ppibmutationscause pages 2-3, pyott2011mutationsinppib pages 1-2)
- **Milestones in reported patients:** One patient (P2-1, van Dijk family 2) had no new fractures between birth and age 3 years while on pamidronate therapy, achieved unsupported sitting at age 2.5 years, standing with support at 4.5 years, and remained wheelchair-dependent at age 7 years (dijk2009ppibmutationscause pages 2-3)

### Critical Periods
- Prenatal period is critical for diagnosis (ultrasound detection of fractures/bowing)
- Growth periods in childhood represent windows for maximal bisphosphonate benefit (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8)

---

## 9. Inheritance and Population

### Epidemiology
- **Overall OI prevalence:** Approximately 1 in 15,000–20,000 births worldwide (chetty2021theevolutionof pages 5-6)
- **OI type IX prevalence:** Ultra-rare; only a handful of families have been reported since the initial description in 2009. The initial reports included 2 families (4 affected individuals) by van Dijk et al. (2009) and 3 additional families by Pyott et al. (2011) (dijk2009ppibmutationscause pages 1-2, pyott2011mutationsinppib pages 3-4). Additional cases have been reported subsequently, including a Chinese pedigree (Jiang et al. 2017, not fully available in current search).
- **Proportion of OI:** Recessive forms collectively account for approximately 10% of all OI cases, with PPIB mutations representing an extremely small fraction of these (chetty2021theevolutionof pages 5-6)

### Inheritance Pattern
- **Autosomal recessive (AR)** (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4, pyott2011mutationsinppib pages 3-4)
- **Penetrance:** Complete in homozygotes/compound heterozygotes for pathogenic variants
- **Expressivity:** Variable; phenotype ranges from moderate OI to perinatal lethal (jovanovic2024updateonthe pages 8-9, pyott2011mutationsinppib pages 1-2)
- **Carrier frequency:** Unknown but expected to be extremely low
- **Consanguinity:** Consanguinity has been documented in at least one family (first-cousin Pakistani parents) (dijk2009ppibmutationscause pages 2-3)
- **Geographic distribution:** Cases reported from diverse ethnic backgrounds including North European and Pakistani families (dijk2009ppibmutationscause pages 2-3), and Chinese families
- **Sex ratio:** No sex predilection; males and females equally affected (autosomal inheritance)

---

## 10. Diagnostics

### Clinical Tests
- **Radiographic findings (imaging):** Skeletal surveys reveal shortened/bowed long bones, fractures with callus formation, discontinuously beaded ribs, bell-shaped thorax, platyspondyly, irregular metaphyses, decreased calvarial mineralization, and osteopenia (dijk2009ppibmutationscause pages 2-3, pyott2011mutationsinppib pages 3-4, dijk2009ppibmutationscause pages 1-2)
- **Bone densitometry (DXA):** Decreased bone mineral density (BMD) Z-scores (dijk2014osteogenesisimperfectaclinical pages 5-7)
- **Collagen electrophoresis:** Overmodification of type I collagen (slower electrophoretic migration) on SDS-PAGE analysis of fibroblast-produced collagen, with normal thermal stability—distinguishing it from dominant collagen mutations (pyott2011mutationsinppib pages 2-3, pyott2011mutationsinppib pages 1-2)
- **Prenatal ultrasound:** Advanced ultrasound at 20 weeks gestation can detect long-bone fractures and bowing (dijk2009ppibmutationscause pages 2-3)

### Genetic Testing
- **Recommended approach:** Next-generation sequencing (NGS) gene panels for OI-related genes including *COL1A1*, *COL1A2*, *CRTAP*, *LEPRE1*, *PPIB*, *SERPINH1*, *FKBP10*, *SERPINF1*, *IFITM5*, and other known OI genes (dinulescu2024newperspectivesof pages 2-4)
- **Whole exome sequencing (WES):** Useful for identifying PPIB mutations, particularly in cases where standard collagen gene testing is negative
- **Single gene testing:** Sanger sequencing of *PPIB* (5 exons and adjacent intronic sequences) can confirm suspected mutations (dijk2009ppibmutationscause pages 2-3)
- **Confirmation:** Western blot analysis using anti-CyPB antibodies can confirm absence or reduction of CyPB protein (dijk2009ppibmutationscause pages 3-6, pyott2011mutationsinppib pages 5-6)

### Differential Diagnosis
- OI type VII (CRTAP mutations): Similar phenotype but typically more severe, with rhizomelia
- OI type VIII (P3H1/LEPRE1 mutations): Similar phenotype, generally more severe
- OI types I–IV (COL1A1/COL1A2 mutations): Dominant inheritance pattern
- OI type X (SERPINH1/HSP47 mutations): Autosomal recessive, severe
- Bruck syndrome (FKBP10/PLOD2 mutations): OI with congenital contractures

Key distinguishing features of OI type IX include: autosomal recessive inheritance, absence of rhizomelia, generally milder than types VII/VIII, partial preservation of Pro986 3-hydroxylation in some patients, and CRTAP/P3H1 proteins remaining stable despite CyPB deficiency (dijk2009ppibmutationscause pages 3-6, cotti2025moleculardriversof pages 9-10).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Severity spectrum:** Ranges from perinatal lethal (pregnancies terminated at 16–22 weeks, or neonatal death) to long-term survival with severe disability (dijk2009ppibmutationscause pages 2-3, pyott2011mutationsinppib pages 1-2)
- **Surviving patients:** Some patients survive into childhood and beyond with moderate to severe OI. One patient was alive and wheelchair-dependent at age 8 years (dijk2009ppibmutationscause pages 2-3); another (Pyott P3) had stable scoliosis at age 16 years (pyott2011mutationsinppib pages 3-4)
- **Mouse model lifespan:** Ppib−/− mice have a typical lifespan of 40–50 weeks, compared to normal mouse lifespan, indicating significant life-shortening effect of CyPB deficiency (choi2009severeosteogenesisimperfecta pages 2-3)

### Morbidity and Function
- Wheelchair dependence in surviving severely affected patients (dijk2009ppibmutationscause pages 2-3)
- Progressive skeletal deformity limiting mobility
- Chronic bone pain requiring management
- Respiratory compromise potential from thoracic deformity

### Complications
- Progressive kyphoscoliosis
- Respiratory insufficiency (major cause of mortality in severe OI generally) (jovanovic2024updateonthe pages 16-17)
- Potential cardiovascular complications as in other severe OI types (jovanovic2024updateonthe pages 16-17)

---

## 12. Treatment

### Pharmacotherapy
**Bisphosphonates (MAXO:0001298 – bisphosphonate administration):**
- Intravenous pamidronate has been directly used in reported OI type IX patients. One patient (P2-1) received 0.5 mg/kg/day IV pamidronate for 3 consecutive days every 6 weeks, starting at age 2 weeks; another (P2-2) commenced pamidronate shortly after birth (dijk2009ppibmutationscause pages 2-3)
- Bisphosphonates bind to hydroxyapatite crystals and induce osteoclast apoptosis, reducing bone resorption and increasing bone mass (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8)
- IV bisphosphonate therapy has positive effects on skeletal pain, bone mass, and mobility in OI generally, though reduction in fracture rate has not been conclusively demonstrated in controlled trials (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8, dwan2016bisphosphonatetherapyfor pages 5-6)
- It is not clear whether patients with recessive OI respond identically to those with dominant OI (alharbi2016asystematicoverview pages 5-6)

**Denosumab:**
- A monoclonal antibody against RANKL showing promise in OI, particularly types III, IV, and VI, by increasing BMD and reducing fracture risk (kresnadi2024theroleof pages 8-9)
- No specific data on denosumab use in OI type IX have been reported

**Other agents under investigation:**
- Sclerostin inhibitors (anti-sclerostin antibodies) have shown increases in bone formation rate and bone mass in murine models (dinulescu2024newperspectivesof pages 2-4)
- Teriparatide (recombinant PTH) and TGF-β antibodies are being explored (dinulescu2024newperspectivesof pages 2-4)
- 4-Phenylbutyrate (4-PBA) has shown amelioration of ER stress/UPR in OI fibroblasts in vitro (jovanovic2024updateonthe pages 15-16)

### Surgical and Interventional (MAXO:0000004 – surgical procedure)
- Intramedullary rodding with telescopic rods for severe long-bone bowing and fracture stabilization (dinulescu2024newperspectivesof pages 2-4, kresnadi2024theroleof pages 5-7)
- Orthopedic management of fractures

### Supportive and Rehabilitative (MAXO:0000950 – physical therapy)
- Physical therapy and occupational therapy for mobility optimization (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8, kresnadi2024theroleof pages 5-7)
- Muscle strengthening provides osteoanabolic stimulus (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8)
- Wheelchair and assistive device provision
- Pain management

### Experimental Therapies
- Gene therapy approaches using viral vectors and CRISPR are being explored for OI generally but are at preclinical stages (dinulescu2024newperspectivesof pages 2-4, alharbi2016asystematicoverview pages 5-6)
- Bone marrow/mesenchymal stem cell transplantation shows promise in animal models (dinulescu2024newperspectivesof pages 2-4)
- No OI type IX-specific clinical trials were identified in the current search

---

## 13. Prevention

### Primary Prevention
- No primary prevention is available for this genetic disorder

### Genetic Counseling (MAXO:0000079 – genetic counseling)
- Genetic counseling is essential for families with affected individuals
- Carrier testing can identify heterozygous parents for recurrence risk assessment (25% per pregnancy for carrier couples) (pyott2011mutationsinppib pages 3-4)
- Preimplantation genetic diagnosis (PGD) and prenatal diagnosis via chorionic villus sampling or amniocentesis are available for families with known mutations (dijk2009ppibmutationscause pages 2-3)

### Prenatal Screening
- Prenatal ultrasound at 20 weeks gestation can detect skeletal abnormalities including fractures and bowing (dijk2009ppibmutationscause pages 2-3)
- Molecular testing of chorionic villus cells can confirm diagnosis when family mutations are known; overmodification of collagen type I in chorionic villi cells was used for prenatal diagnosis in one family (dijk2009ppibmutationscause pages 2-3)

### Tertiary Prevention
- Regular bisphosphonate therapy during growth to maximize bone mass
- Fracture prevention strategies including safe environments and activity modification
- Regular monitoring of bone density, growth, and spinal alignment

---

## 14. Other Species / Natural Disease

No naturally occurring PPIB-mutation OI has been documented in companion animals or wildlife. The orthologous gene *Ppib* in mouse (*Mus musculus*, NCBI Taxon: 10090) has been studied extensively through knockout models.

---

## 15. Model Organisms

### Ppib Knockout Mouse (Ppib−/−)

Two independent Ppib knockout mouse models have been generated and characterized:

**Choi et al. (2009) model (choi2009severeosteogenesisimperfecta pages 1-2, choi2009severeosteogenesisimperfecta pages 2-3):**
- Generated using Cre/lox system targeting exon 3 of Ppib
- Phenotype: kyphosis appearing at 8 weeks of age and progressing with age; severe osteoporosis; reduced bone density on DXA; abnormal collagen fibril morphology (fibrils ~1.45× wider than normal, 114.6 nm vs. 78.6 nm); absence of rhizomelia; loose/thin skin; reduced body mass; lifespan approximately 40–50 weeks
- Molecular findings: essentially absent Pro986 3-hydroxylation; substantially reduced P3H1 levels (while CRTAP unaffected); impaired procollagen localization to Golgi; procollagen accumulation in ER

**Cabral/Marini et al. (2014) model (cabral2014abnormaltypei pages 1-2, cabral2014abnormaltypei pages 2-3, cabral2014abnormaltypei pages 3-6):**
- Phenotype: small body size (~25% less body weight); reduced femoral aBMD and BV/TV; reduced mechanical properties with 48% less energy required to fracture, 37% reduced stiffness; dramatically increased brittleness (77% reduced post-yield displacement, 89% reduced plastic energy); deformed rib cage; kyphosis
- Molecular findings: only 2–11% residual prolyl 3-hydroxylation; slower collagen folding but treatment with cyclosporine A (CsA) caused further delay, suggesting existence of another collagen PPIase; site-specific underhydroxylation at K87 (~20% unhydroxylated vs. <1% wild-type) and K933; increased underhydroxylated crosslinks; altered HP/LP crosslink ratio; decreased collagen deposition into matrix; abnormal fibril structure

### Phenotype Recapitulation
Both models faithfully recapitulate the human OI type IX phenotype, including bone fragility, osteoporosis, kyphosis, growth deficiency, abnormal collagen fibrils, and absence of rhizomelia (choi2009severeosteogenesisimperfecta pages 1-2). The models have been essential for understanding the molecular pathophysiology, particularly the dual role of CyPB in both prolyl 3-hydroxylation and collagen crosslinking regulation.

### Model Limitations
- Mouse lifespan does not fully model the chronic decades-long disease course in humans
- Some molecular findings differ between human patients and mice (e.g., complete absence of Pro986 3-hydroxylation in mice vs. partial preservation in some human patients) (cotti2025moleculardriversof pages 9-10)
- No zebrafish or other non-mammalian models for OI type IX have been reported

### Resources
- International Mouse Phenotyping Consortium (IMPC) for Ppib mutant mice
- Model organism databases: MGI (Mouse Genome Informatics), IMSR (International Mouse Strain Resource)

---

## Summary

Osteogenesis Imperfecta Type IX is an ultra-rare autosomal recessive bone fragility disorder caused by loss-of-function mutations in *PPIB*, encoding cyclophilin B (CyPB). The disease was first described in 2009 and fewer than 10 families have been reported in the literature (dijk2009ppibmutationscause pages 1-2, pyott2011mutationsinppib pages 3-4). CyPB is a multifunctional ER-resident protein that serves as a peptidyl-prolyl cis-trans isomerase, molecular chaperone, and component of the P3H1/CRTAP/CyPB prolyl 3-hydroxylation complex (jovanovic2024updateonthe pages 8-9, dijk2009ppibmutationscause pages 1-2). Its deficiency leads to delayed collagen folding, overmodification, impaired crosslinking, ER stress, and ultimately fragile bone with diminished mechanical properties (cabral2014abnormaltypei pages 1-2, etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4). The clinical phenotype spans moderate to perinatal lethal severity, with features including multiple fractures, severe short stature, bowed long bones, kyphoscoliosis, and gray sclerae (dijk2009ppibmutationscause pages 2-3, cotti2025moleculardriversof pages 9-10). Current management relies on bisphosphonate therapy, orthopedic intervention, and supportive care, with novel therapeutic approaches including gene therapy and anti-sclerostin antibodies under investigation for OI broadly (dinulescu2024newperspectivesof pages 2-4, etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8). Ppib knockout mice provide valuable preclinical models that faithfully recapitulate the human disease phenotype (cabral2014abnormaltypei pages 2-3, choi2009severeosteogenesisimperfecta pages 1-2).

References

1. (jovanovic2024updateonthe pages 8-9): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 76 citations and is from a peer-reviewed journal.

2. (dijk2009ppibmutationscause pages 1-2): Fleur S. van Dijk, Isabel M. Nesbitt, Eline H. Zwikstra, Peter G.J. Nikkels, Sander R. Piersma, Silvina A. Fratantoni, Connie R. Jimenez, Margriet Huizer, Alice C. Morsman, Jan M. Cobben, Mirjam H.H. van Roij, Mariet W. Elting, Jonathan I.M.L. Verbeke, Liliane C.D. Wijnaendts, Nick J. Shaw, Wolfgang Högler, Carole McKeown, Erik A. Sistermans, Ann Dalton, Hanne Meijers-Heijboer, and Gerard Pals. Ppib mutations cause severe osteogenesis imperfecta. American journal of human genetics, 85 4:521-7, Oct 2009. URL: https://doi.org/10.1016/j.ajhg.2009.09.001, doi:10.1016/j.ajhg.2009.09.001. This article has 354 citations and is from a highest quality peer-reviewed journal.

3. (etich2020osteogenesisimperfecta—pathophysiologyand pages 2-4): Julia Etich, Lennart Leßmeier, Mirko Rehberg, Helge Sill, Frank Zaucke, Christian Netzer, and Oliver Semler. Osteogenesis imperfecta—pathophysiology and therapeutic options. Molecular and Cellular Pediatrics, Aug 2020. URL: https://doi.org/10.1186/s40348-020-00101-9, doi:10.1186/s40348-020-00101-9. This article has 113 citations.

4. (pyott2011mutationsinppib pages 1-2): Shawna M. Pyott, Ulrike Schwarze, Helena E. Christiansen, Melanie G. Pepin, Dru F. Leistritz, Richard Dineen, Catharine Harris, Barbara K. Burton, Brad Angle, Katherine Kim, Michael D. Sussman, MaryAnn Weis, David R. Eyre, David W. Russell, Kevin J. McCarthy, Robert D. Steiner, and Peter H. Byers. Mutations in ppib (cyclophilin b) delay type i procollagen chain association and result in perinatal lethal to moderate osteogenesis imperfecta phenotypes. Human molecular genetics, 20 8:1595-609, Apr 2011. URL: https://doi.org/10.1093/hmg/ddr037, doi:10.1093/hmg/ddr037. This article has 164 citations and is from a domain leading peer-reviewed journal.

5. (pyott2011mutationsinppib pages 2-3): Shawna M. Pyott, Ulrike Schwarze, Helena E. Christiansen, Melanie G. Pepin, Dru F. Leistritz, Richard Dineen, Catharine Harris, Barbara K. Burton, Brad Angle, Katherine Kim, Michael D. Sussman, MaryAnn Weis, David R. Eyre, David W. Russell, Kevin J. McCarthy, Robert D. Steiner, and Peter H. Byers. Mutations in ppib (cyclophilin b) delay type i procollagen chain association and result in perinatal lethal to moderate osteogenesis imperfecta phenotypes. Human molecular genetics, 20 8:1595-609, Apr 2011. URL: https://doi.org/10.1093/hmg/ddr037, doi:10.1093/hmg/ddr037. This article has 164 citations and is from a domain leading peer-reviewed journal.

6. (pyott2011mutationsinppib pages 3-4): Shawna M. Pyott, Ulrike Schwarze, Helena E. Christiansen, Melanie G. Pepin, Dru F. Leistritz, Richard Dineen, Catharine Harris, Barbara K. Burton, Brad Angle, Katherine Kim, Michael D. Sussman, MaryAnn Weis, David R. Eyre, David W. Russell, Kevin J. McCarthy, Robert D. Steiner, and Peter H. Byers. Mutations in ppib (cyclophilin b) delay type i procollagen chain association and result in perinatal lethal to moderate osteogenesis imperfecta phenotypes. Human molecular genetics, 20 8:1595-609, Apr 2011. URL: https://doi.org/10.1093/hmg/ddr037, doi:10.1093/hmg/ddr037. This article has 164 citations and is from a domain leading peer-reviewed journal.

7. (dijk2009ppibmutationscause pages 2-3): Fleur S. van Dijk, Isabel M. Nesbitt, Eline H. Zwikstra, Peter G.J. Nikkels, Sander R. Piersma, Silvina A. Fratantoni, Connie R. Jimenez, Margriet Huizer, Alice C. Morsman, Jan M. Cobben, Mirjam H.H. van Roij, Mariet W. Elting, Jonathan I.M.L. Verbeke, Liliane C.D. Wijnaendts, Nick J. Shaw, Wolfgang Högler, Carole McKeown, Erik A. Sistermans, Ann Dalton, Hanne Meijers-Heijboer, and Gerard Pals. Ppib mutations cause severe osteogenesis imperfecta. American journal of human genetics, 85 4:521-7, Oct 2009. URL: https://doi.org/10.1016/j.ajhg.2009.09.001, doi:10.1016/j.ajhg.2009.09.001. This article has 354 citations and is from a highest quality peer-reviewed journal.

8. (cotti2025moleculardriversof pages 9-10): Silvia Cotti, Wendy Pérez Franco, and Antonella Forlino. Molecular drivers of osteogenesis imperfecta: a cellular and extracellular collagen disease. Clinical Science, 139(24):1733-1768, Dec 2025. URL: https://doi.org/10.1042/cs20255642, doi:10.1042/cs20255642. This article has 3 citations and is from a peer-reviewed journal.

9. (cabral2014abnormaltypei pages 1-2): Wayne A. Cabral, Irina Perdivara, MaryAnn Weis, Masahiko Terajima, Angela R. Blissett, Weizhong Chang, Joseph E. Perosky, Elena N. Makareeva, Edward L. Mertz, Sergey Leikin, Kenneth B. Tomer, Kenneth M. Kozloff, David R. Eyre, Mitsuo Yamauchi, and Joan C. Marini. Abnormal type i collagen post-translational modification and crosslinking in a cyclophilin b ko mouse model of recessive osteogenesis imperfecta. PLoS Genetics, 10:e1004465, Jun 2014. URL: https://doi.org/10.1371/journal.pgen.1004465, doi:10.1371/journal.pgen.1004465. This article has 143 citations and is from a domain leading peer-reviewed journal.

10. (cabral2014abnormaltypei pages 2-3): Wayne A. Cabral, Irina Perdivara, MaryAnn Weis, Masahiko Terajima, Angela R. Blissett, Weizhong Chang, Joseph E. Perosky, Elena N. Makareeva, Edward L. Mertz, Sergey Leikin, Kenneth B. Tomer, Kenneth M. Kozloff, David R. Eyre, Mitsuo Yamauchi, and Joan C. Marini. Abnormal type i collagen post-translational modification and crosslinking in a cyclophilin b ko mouse model of recessive osteogenesis imperfecta. PLoS Genetics, 10:e1004465, Jun 2014. URL: https://doi.org/10.1371/journal.pgen.1004465, doi:10.1371/journal.pgen.1004465. This article has 143 citations and is from a domain leading peer-reviewed journal.

11. (choi2009severeosteogenesisimperfecta pages 1-2): Jae Won Choi, Shari L. Sutor, Lonn Lindquist, Glenda L. Evans, Benjamin J. Madden, H. Robert Bergen, Theresa E. Hefferan, Michael J. Yaszemski, and Richard J. Bram. Severe osteogenesis imperfecta in cyclophilin b–deficient mice. PLoS Genetics, 5:e1000750, Dec 2009. URL: https://doi.org/10.1371/journal.pgen.1000750, doi:10.1371/journal.pgen.1000750. This article has 123 citations and is from a domain leading peer-reviewed journal.

12. (etich2020osteogenesisimperfecta—pathophysiologyand pages 7-8): Julia Etich, Lennart Leßmeier, Mirko Rehberg, Helge Sill, Frank Zaucke, Christian Netzer, and Oliver Semler. Osteogenesis imperfecta—pathophysiology and therapeutic options. Molecular and Cellular Pediatrics, Aug 2020. URL: https://doi.org/10.1186/s40348-020-00101-9, doi:10.1186/s40348-020-00101-9. This article has 113 citations.

13. (kresnadi2024theroleof pages 5-7): Agus Kresnadi, Tri Wahyu Martanto, Arif Zulkarnain, and Hizbillah Yazid. The role of denosumab and bisphosphonate in osteogenesis imperfecta: a literature review. Salud, Ciencia y Tecnología, 4:894, Apr 2024. URL: https://doi.org/10.56294/saludcyt2024894, doi:10.56294/saludcyt2024894. This article has 1 citations.

14. (pyott2011mutationsinppib pages 4-5): Shawna M. Pyott, Ulrike Schwarze, Helena E. Christiansen, Melanie G. Pepin, Dru F. Leistritz, Richard Dineen, Catharine Harris, Barbara K. Burton, Brad Angle, Katherine Kim, Michael D. Sussman, MaryAnn Weis, David R. Eyre, David W. Russell, Kevin J. McCarthy, Robert D. Steiner, and Peter H. Byers. Mutations in ppib (cyclophilin b) delay type i procollagen chain association and result in perinatal lethal to moderate osteogenesis imperfecta phenotypes. Human molecular genetics, 20 8:1595-609, Apr 2011. URL: https://doi.org/10.1093/hmg/ddr037, doi:10.1093/hmg/ddr037. This article has 164 citations and is from a domain leading peer-reviewed journal.

15. (choi2009severeosteogenesisimperfecta pages 2-3): Jae Won Choi, Shari L. Sutor, Lonn Lindquist, Glenda L. Evans, Benjamin J. Madden, H. Robert Bergen, Theresa E. Hefferan, Michael J. Yaszemski, and Richard J. Bram. Severe osteogenesis imperfecta in cyclophilin b–deficient mice. PLoS Genetics, 5:e1000750, Dec 2009. URL: https://doi.org/10.1371/journal.pgen.1000750, doi:10.1371/journal.pgen.1000750. This article has 123 citations and is from a domain leading peer-reviewed journal.

16. (choi2009severeosteogenesisimperfecta pages 3-5): Jae Won Choi, Shari L. Sutor, Lonn Lindquist, Glenda L. Evans, Benjamin J. Madden, H. Robert Bergen, Theresa E. Hefferan, Michael J. Yaszemski, and Richard J. Bram. Severe osteogenesis imperfecta in cyclophilin b–deficient mice. PLoS Genetics, 5:e1000750, Dec 2009. URL: https://doi.org/10.1371/journal.pgen.1000750, doi:10.1371/journal.pgen.1000750. This article has 123 citations and is from a domain leading peer-reviewed journal.

17. (dijk2009ppibmutationscause pages 3-6): Fleur S. van Dijk, Isabel M. Nesbitt, Eline H. Zwikstra, Peter G.J. Nikkels, Sander R. Piersma, Silvina A. Fratantoni, Connie R. Jimenez, Margriet Huizer, Alice C. Morsman, Jan M. Cobben, Mirjam H.H. van Roij, Mariet W. Elting, Jonathan I.M.L. Verbeke, Liliane C.D. Wijnaendts, Nick J. Shaw, Wolfgang Högler, Carole McKeown, Erik A. Sistermans, Ann Dalton, Hanne Meijers-Heijboer, and Gerard Pals. Ppib mutations cause severe osteogenesis imperfecta. American journal of human genetics, 85 4:521-7, Oct 2009. URL: https://doi.org/10.1016/j.ajhg.2009.09.001, doi:10.1016/j.ajhg.2009.09.001. This article has 354 citations and is from a highest quality peer-reviewed journal.

18. (pyott2011mutationsinppib pages 5-6): Shawna M. Pyott, Ulrike Schwarze, Helena E. Christiansen, Melanie G. Pepin, Dru F. Leistritz, Richard Dineen, Catharine Harris, Barbara K. Burton, Brad Angle, Katherine Kim, Michael D. Sussman, MaryAnn Weis, David R. Eyre, David W. Russell, Kevin J. McCarthy, Robert D. Steiner, and Peter H. Byers. Mutations in ppib (cyclophilin b) delay type i procollagen chain association and result in perinatal lethal to moderate osteogenesis imperfecta phenotypes. Human molecular genetics, 20 8:1595-609, Apr 2011. URL: https://doi.org/10.1093/hmg/ddr037, doi:10.1093/hmg/ddr037. This article has 164 citations and is from a domain leading peer-reviewed journal.

19. (cotti2025moleculardriversof pages 7-9): Silvia Cotti, Wendy Pérez Franco, and Antonella Forlino. Molecular drivers of osteogenesis imperfecta: a cellular and extracellular collagen disease. Clinical Science, 139(24):1733-1768, Dec 2025. URL: https://doi.org/10.1042/cs20255642, doi:10.1042/cs20255642. This article has 3 citations and is from a peer-reviewed journal.

20. (cabral2014abnormaltypei pages 12-13): Wayne A. Cabral, Irina Perdivara, MaryAnn Weis, Masahiko Terajima, Angela R. Blissett, Weizhong Chang, Joseph E. Perosky, Elena N. Makareeva, Edward L. Mertz, Sergey Leikin, Kenneth B. Tomer, Kenneth M. Kozloff, David R. Eyre, Mitsuo Yamauchi, and Joan C. Marini. Abnormal type i collagen post-translational modification and crosslinking in a cyclophilin b ko mouse model of recessive osteogenesis imperfecta. PLoS Genetics, 10:e1004465, Jun 2014. URL: https://doi.org/10.1371/journal.pgen.1004465, doi:10.1371/journal.pgen.1004465. This article has 143 citations and is from a domain leading peer-reviewed journal.

21. (cabral2014abnormaltypei pages 6-8): Wayne A. Cabral, Irina Perdivara, MaryAnn Weis, Masahiko Terajima, Angela R. Blissett, Weizhong Chang, Joseph E. Perosky, Elena N. Makareeva, Edward L. Mertz, Sergey Leikin, Kenneth B. Tomer, Kenneth M. Kozloff, David R. Eyre, Mitsuo Yamauchi, and Joan C. Marini. Abnormal type i collagen post-translational modification and crosslinking in a cyclophilin b ko mouse model of recessive osteogenesis imperfecta. PLoS Genetics, 10:e1004465, Jun 2014. URL: https://doi.org/10.1371/journal.pgen.1004465, doi:10.1371/journal.pgen.1004465. This article has 143 citations and is from a domain leading peer-reviewed journal.

22. (jovanovic2024updateonthe pages 15-16): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 76 citations and is from a peer-reviewed journal.

23. (jovanovic2024updateonthe pages 19-20): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 76 citations and is from a peer-reviewed journal.

24. (jovanovic2024updateonthe pages 16-17): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 76 citations and is from a peer-reviewed journal.

25. (chetty2021theevolutionof pages 5-6): Manogari Chetty, Imaan Amina Roomaney, and Peter Beighton. The evolution of the nosology of osteogenesis imperfecta. Clinical Genetics, 99:42-52, Nov 2021. URL: https://doi.org/10.1111/cge.13846, doi:10.1111/cge.13846. This article has 48 citations and is from a peer-reviewed journal.

26. (dijk2014osteogenesisimperfectaclinical pages 5-7): F.S. Van Dijk and D.O. Sillence. Osteogenesis imperfecta: clinical diagnosis, nomenclature and severity assessment. American Journal of Medical Genetics. Part a, 164:1470-1481, Apr 2014. URL: https://doi.org/10.1002/ajmg.a.36545, doi:10.1002/ajmg.a.36545. This article has 1005 citations and is from a peer-reviewed journal.

27. (dinulescu2024newperspectivesof pages 2-4): Alexandru Dinulescu, Alexandru-Sorin Păsărică, Mădălina Carp, Andrei Dușcă, Irina Dijmărescu, Mirela Luminița Pavelescu, Daniela Păcurar, and Alexandru Ulici. New perspectives of therapies in osteogenesis imperfecta—a literature review. Journal of Clinical Medicine, 13:1065, Feb 2024. URL: https://doi.org/10.3390/jcm13041065, doi:10.3390/jcm13041065. This article has 25 citations.

28. (dwan2016bisphosphonatetherapyfor pages 5-6): Kerry Dwan, Carrie A Phillipi, Robert D Steiner, and Donald Basel. Bisphosphonate therapy for osteogenesis imperfecta. The Cochrane database of systematic reviews, 10:CD005088, Oct 2016. URL: https://doi.org/10.1002/14651858.cd005088.pub4, doi:10.1002/14651858.cd005088.pub4. This article has 559 citations.

29. (alharbi2016asystematicoverview pages 5-6): Samir Abdulkarim Alharbi. A systematic overview of osteogenesis imperfecta. ArXiv, 5:1-9, Jan 2016. URL: https://doi.org/10.4172/2168-9547.1000150, doi:10.4172/2168-9547.1000150. This article has 44 citations.

30. (kresnadi2024theroleof pages 8-9): Agus Kresnadi, Tri Wahyu Martanto, Arif Zulkarnain, and Hizbillah Yazid. The role of denosumab and bisphosphonate in osteogenesis imperfecta: a literature review. Salud, Ciencia y Tecnología, 4:894, Apr 2024. URL: https://doi.org/10.56294/saludcyt2024894, doi:10.56294/saludcyt2024894. This article has 1 citations.

31. (cabral2014abnormaltypei pages 3-6): Wayne A. Cabral, Irina Perdivara, MaryAnn Weis, Masahiko Terajima, Angela R. Blissett, Weizhong Chang, Joseph E. Perosky, Elena N. Makareeva, Edward L. Mertz, Sergey Leikin, Kenneth B. Tomer, Kenneth M. Kozloff, David R. Eyre, Mitsuo Yamauchi, and Joan C. Marini. Abnormal type i collagen post-translational modification and crosslinking in a cyclophilin b ko mouse model of recessive osteogenesis imperfecta. PLoS Genetics, 10:e1004465, Jun 2014. URL: https://doi.org/10.1371/journal.pgen.1004465, doi:10.1371/journal.pgen.1004465. This article has 143 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Osteogenesis_Imperfecta_Type_IX-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Osteogenesis_Imperfecta_Type_IX-deep-research-falcon_artifacts/artifact-01.md)