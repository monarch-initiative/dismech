---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-12T15:24:20.407110'
end_time: '2026-06-12T15:32:42.150004'
duration_seconds: 501.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lathyrism
  mondo_id: ''
  category: Environmental
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Lathyrism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lathyrism
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Lathyrism** covering all of the
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
- **Disease Name:** Lathyrism
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Lathyrism** covering all of the
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


## Comprehensive Research Report: Lathyrism (Environmental)

### Executive summary
Lathyrism is a toxin-mediated environmental disease classically linked to ingestion of *Lathyrus* spp. and characterized by distinct clinical subtypes: neurolathyrism (upper motor neuron syndrome with irreversible spastic paraparesis) due to β-ODAP/β-L-ODAP from grass pea (*Lathyrus sativus*), and connective-tissue lathyrism including osteolathyrism (skeletal deformities) and angiolathyrism (aortic aneurysm/dissection) driven by β-aminopropionitrile (BAPN), historically associated with *Lathyrus odoratus* exposure and widely used in animal models via lysyl oxidase inhibition. (bekelealemu2024thepotentialof pages 2-3, yesuf2024prevalenceassociatedfactors pages 1-5, carlson2002caseiz16753 pages 3-4, merico2021inhibitionoflysyl pages 1-2)

| Subtype | Primary trigger / toxin | Source exposure | Core clinical features | Key mechanism | 2023-2024+ key references | Evidence |
|---|---|---|---|---|---|---|
| Neurolathyrism | β-ODAP / β-L-ODAP (toxic β-isomer of ODAP) | Prolonged overconsumption of grass pea (*Lathyrus sativus*) seeds; risk heightened during drought/food insecurity | Irreversible spastic paraparesis/spastic paralysis of the legs; symmetrical spastic leg weakness; corticospinal/pyramidal tract degeneration; walking difficulty; sensory sparing often noted | Excitatory amino-acid neurotoxicity with AMPA receptor agonism, reduced glutamate/aspartate transport, intracellular Ca2+ overload, mitochondrial dysfunction, oxidative stress, and motor-neuron degeneration | Edwards et al., *Nat Commun* (Feb 2023), DOI: 10.1038/s41467-023-36503-2, https://doi.org/10.1038/s41467-023-36503-2; Bekele-Alemu et al., *Curr Issues Mol Biol* (Sep 2024), DOI: 10.3390/cimb46090626, https://doi.org/10.3390/cimb46090626; Yesuf et al. preprint (May 2024), DOI: 10.21203/rs.3.rs-4332232/v1, https://doi.org/10.21203/rs.3.rs-4332232/v1 | (bekelealemu2024thepotentialof pages 2-3, bekelealemu2024thepotentialof pages 5-7, yesuf2024prevalenceassociatedfactors pages 1-5, edwards2023genomicsandbiochemical pages 12-13, edwards2023genomicsandbiochemical pages 1-2) |
| Osteolathyrism | β-aminopropionitrile (BAPN) | Exposure to BAPN, classically from *Lathyrus odoratus* and related *Lathyrus* spp.; widely used experimentally to induce lathyrism | Bone deformity; periosteal proliferative exostoses; fibro-osseous/cartilaginous lesions at tendon insertion sites; defective bone collagen quality; reduced bone formation and increased resorption | Irreversible lysyl oxidase (LOX) inhibition causing deficient collagen cross-linking and impaired extracellular matrix maturation; poor collagen quality and altered bone remodeling | Suliman et al., *J Prosthodont Res* (Oct 2023), DOI: 10.2186/jpr.jpr_d_22_00249, https://doi.org/10.2186/jpr.jpr_d_22_00249 | (carlson2002caseiz16753 pages 3-4, suliman2023theeffectsof pages 1-2) |
| Angiolathyrism | β-aminopropionitrile (BAPN) | Exposure to BAPN from *Lathyrus odoratus* / related pulses; established animal-model lathyrogen | Aortic aneurysm, aortic dissection/rupture, ascending aortic wall disruption, arterial aneurysm with fatal rupture | LOX inhibition impairs collagen/elastin cross-linking in vascular ECM; associated with increased apoptosis, stimulated TGF-β/SMAD2 signaling, and MMP-2/MMP-9 upregulation | Merico et al., *Heart Vessels* (Jan 2021), DOI: 10.1007/s00380-020-01750-6, https://doi.org/10.1007/s00380-020-01750-6 | (merico2021inhibitionoflysyl pages 1-2, carlson2002caseiz16753 pages 1-3) |


*Table: This table summarizes the three main lathyrism subtypes by toxin, source exposure, clinical phenotype, mechanism, and recent key references. It is useful as a compact crosswalk between clinical presentation and toxicologic/pathophysiologic basis.*

---

## 1. Disease Information

### 1.1 Overview and current understanding
**Lathyrism** is an environmentally triggered, toxin-associated disorder caused by exposure to specific *Lathyrus* plant constituents leading to either (i) a neurodegenerative upper motor neuron syndrome (neurolathyrism) or (ii) connective-tissue pathology affecting bone and/or vasculature (osteo-/angiolathyrism). (bekelealemu2024thepotentialof pages 2-3, carlson2002caseiz16753 pages 3-4, merico2021inhibitionoflysyl pages 1-2)

**Neurolathyrism** is described as a neurodegenerative disease caused by “long-term overconsumption” of grass pea seeds containing the non-protein amino acid **β-ODAP**, producing an “irreversible spastic paraparesis of the legs while sparing sensory systems.” (bekelealemu2024thepotentialof pages 2-3)

A clinical case definition used in recent community work emphasized **symmetrical spastic leg weakness** with subacute/insidious onset, **no sensory deficit**, and **history of grass pea consumption** around onset. (yesuf2024prevalenceassociatedfactors pages 1-5)

### 1.2 Key identifiers and synonyms
*Evidence in retrieved sources was insufficient to reliably populate ontology identifiers.* The following identifiers were **not found** in the retrieved evidence and should be confirmed from OMIM/Orphanet/ICD/MeSH/MONDO directly before KB entry:
- MONDO ID: not found in evidence (needs ontology lookup)
- ICD-10/ICD-11 code(s): not found in evidence
- MeSH descriptor(s): not found in evidence
- Orphanet/OMIM identifiers: not found in evidence

**Synonyms / alternative names (from local usage / literature in evidence):**
- “Neurolathyrism” (disease subtype) (bekelealemu2024thepotentialof pages 2-3, yesuf2024prevalenceassociatedfactors pages 1-5)
- In Delanta, Ethiopia, the term “Yeguaya Beshita” is widely recognized as the local name for the condition (97.9% recognized the term). (yesuf2024prevalenceassociatedfactors pages 5-9)

### 1.3 Data provenance
The retrieved evidence includes **aggregated population research** (community cross-sectional surveys in Ethiopia) and **experimental/mechanistic work** (plant genomics/biochemistry and animal models). (yesuf2024prevalenceassociatedfactors pages 12-15, edwards2023genomicsandbiochemical pages 1-2, merico2021inhibitionoflysyl pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
#### Neurolathyrism (β-ODAP/β-L-ODAP; *L. sativus*)
- Etiology is associated with ingestion of *Lathyrus sativus* containing a glutamate-analog neurotoxin; neurolathyrism is explicitly linked to the neurotoxin **β-ODAP (β-L-ODAP)**. (yesuf2024prevalenceassociatedfactors pages 1-5, edwards2023genomicsandbiochemical pages 12-13)
- β-ODAP exists as α and β isomers; the **β-isomer** is described as the toxic form accounting for ~99% of ODAP. (bekelealemu2024thepotentialof pages 2-3)

#### Osteolathyrism / Angiolathyrism (BAPN; *L. odoratus*; LOX inhibition)
- BAPN is described as an **irreversible inhibitor of lysyl oxidase (LOX)**, disrupting collagen and elastin cross-linking and causing osteolathyrism and vascular lesions including aneurysm/rupture in animal models. (carlson2002caseiz16753 pages 3-4, merico2021inhibitionoflysyl pages 1-2)

### 2.2 Risk factors
#### Environmental / dietary
- Reliance on grass pea as a staple during adverse conditions: outbreaks are linked in review evidence to drought and reliance on grass pea as a major food source. (bekelealemu2024thepotentialof pages 2-3)
- Nutritional status: sulfur amino acid deficiency is highlighted as increasing β-ODAP toxicity; supplementation with sulfur-containing amino acids is presented as risk-mitigating. (bekelealemu2024thepotentialof pages 2-3, bekelealemu2024thepotentialof pages 5-7)

#### Population-level and sociodemographic (recent Ethiopia data)
A 2022 community-based study in Delanta district, Ethiopia (n=470 analyzed) reported 56 cases (11.9% of participants) and estimated population prevalence 6.6%. (yesuf2024prevalenceassociatedfactors pages 1-5)

Multivariable associated factors included:
- Male sex: AOR 3.569 (95% CI 1.794–7.098) (yesuf2024prevalenceassociatedfactors pages 12-15)
- Older age (>46): AOR 2.690 (95% CI 1.064–9.341) (yesuf2024prevalenceassociatedfactors pages 12-15)
- Inability to read: AOR 3.128 (95% CI 1.224–7.993) (yesuf2024prevalenceassociatedfactors pages 12-15)
- Family size (reported as “less than 5” in one excerpt): AOR 2.332 (95% CI 1.159–4.692) (yesuf2024prevalenceassociatedfactors pages 12-15)
- Farmland lease: AOR 2.734 (95% CI 1.23–6.06) (yesuf2024prevalenceassociatedfactors pages 12-15)

**Note:** Some odds ratio reporting appears inconsistently formatted across excerpts from the same preprint (e.g., “AOR=23%” with unusual CI formatting). Values above are taken from the excerpt that provided standard numeric AORs and CIs. (yesuf2024prevalenceassociatedfactors pages 12-15, yesuf2024prevalenceassociatedfactors pages 1-5)

### 2.3 Protective factors
Evidence in the retrieved dataset suggests:
- Sulfur amino acid adequacy/supplementation (methionine, cysteine) may reduce β-ODAP neurotoxicity risk. (bekelealemu2024thepotentialof pages 2-3)
- In neurolathyrism patients, **regular exercise** and **formal counselling** were associated with decreased odds of major depressive disorder (a comorbidity), suggesting plausible QoL-protective interventions in real-world care, though not primary prevention of neurolathyrism itself. (bimerew2024prevalenceofmajor pages 1-2)

### 2.4 Gene–environment interactions
No human genetic susceptibility loci/variants were identified in the retrieved evidence. However, genotype-by-environment (G×E) interactions are described in the context of **grass pea toxin content**, where classical breeding for low β-ODAP can be undermined by environmental effects increasing toxin levels. (bekelealemu2024thepotentialof pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotypes by subtype
#### Neurolathyrism (human clinical)
Clinical features include:
- Symmetrical spastic leg weakness, spastic gait, pyramidal signs (Babinski, clonus), progressive disability stages I–IV (walking stick dependence to bedridden with contractures). (yesuf2024prevalenceassociatedfactors pages 1-5)
- “Irreversible spastic paraparesis” of legs with sensory sparing is emphasized in recent review evidence. (bekelealemu2024thepotentialof pages 2-3)

**Suggested HPO terms (mapping; confirm exact best matches in HPO):**
- Spastic paraplegia: HP:0001258
- Spasticity: HP:0001257
- Abnormal gait: HP:0001288
- Hyperreflexia / Babinski sign: HP:0001347 / HP:0003487 (confirm)
- Contractures (advanced): HP:0001371

#### Osteolathyrism (connective tissue/bone)
- Bone deformity and periosteal proliferative exostoses at tendon insertion sites are described in BAPN intoxication; histology includes fibroblastic masses with cartilaginous and bone formation. (carlson2002caseiz16753 pages 3-4)

**Suggested HPO terms:**
- Exostoses: HP:0100777
- Abnormal bone morphology: HP:0003330
- Muscle atrophy (secondary): HP:0003202

#### Angiolathyrism (vascular)
- Aortic/arterial aneurysm and rupture/dissection is described with LOX inhibition by BAPN in animal models and mechanistic vascular wall disruption. (merico2021inhibitionoflysyl pages 1-2, carlson2002caseiz16753 pages 1-3)

**Suggested HPO terms:**
- Aortic aneurysm: HP:0004942
- Aortic dissection: HP:0002647

### 3.2 Onset, severity, progression
- Neurolathyrism can present with subacute/insidious onset and progresses across clinically staged disability levels (I–IV). (yesuf2024prevalenceassociatedfactors pages 1-5)
- In a neurolathyrism patient sample (Dawunt district), reported onset age range was 4–37 years (mean 17.32 ± 7.91) with disease duration 4–40 years (mean 17.95 ± 8.28), consistent with long-term disability. (bimerew2024prevalenceofmajor pages 2-4)

### 3.3 Quality-of-life and psychosocial impact (recent data)
- In Delanta, Ethiopia, substantial social impact was reported: 73% discontinued school and 21.4% were divorced after the disease. (yesuf2026neurolathyrismindelanta pages 1-2)
- Among adult neurolathyrism patients in Dawunt district, Ethiopia, major depressive disorder prevalence was **38.7%**. (bimerew2024prevalenceofmajor pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Human causal genes and pathogenic variants
Lathyrism is primarily an **environmental/toxin-mediated** condition in the retrieved sources; **no causal human genes or variants** were identified in the evidence provided. (bekelealemu2024thepotentialof pages 2-3, yesuf2024prevalenceassociatedfactors pages 1-5)

### 4.2 Plant/crop molecular genetics relevant to risk mitigation (2023–2024 priority)
A major 2023 advance was a long-read genome assembly for *L. sativus* and biochemical elucidation of the β-L-ODAP biosynthetic pathway.
- Edwards et al. (Nature Communications, Feb 2023) report an annotated ~6.5 Gbp *L. sativus* genome and identify a final-step **metabolon** involving **LsAAE3** (acyl-activating enzyme 3) and **LsBOS** (a BAHD acyltransferase), “CoA-activated to produce β-L-ODAP.” (edwards2023genomicsandbiochemical pages 1-2)
- Pathway-related loci include **CAS** (β-cyanoalanine synthase) and **CS** (cysteine synthase) genes, with multiple CS-like copies annotated. (edwards2023genomicsandbiochemical pages 2-4)

A 2024 review proposes gene-editing strategies:
- Bekele-Alemu et al. (Current Issues in Molecular Biology, Sep 2024) identify key enzymes **β-ODAP synthase (BOS)** and **β-cyanoalanine synthase (CAS)** and propose CRISPR/Cas9 strategies: BOS knockout, CAS knockout, BOS+CAS knockout, or targeted substitutions to reduce toxin while monitoring precursor accumulation. (bekelealemu2024thepotentialof pages 11-13)

**Suggested ontology mappings (plant/crop context; for KB cross-references):**
- Chemical entity: β-ODAP / β-L-ODAP (CHEBI ID not in evidence; needs CHEBI lookup)

---

## 5. Environmental Information

### 5.1 Environmental factors
- Food-system stressors: community data emphasize grass pea’s centrality as a primary food and note that “banning grass pea is not feasible” locally due to weather variability leading to overconsumption risk. (yesuf2024prevalenceassociatedfactors pages 5-9)

### 5.2 Lifestyle factors
No smoking/alcohol or other lifestyle exposures were identified as causal in the retrieved evidence. Exercise appears in the context of mental-health comorbidity reduction rather than primary disease prevention. (bimerew2024prevalenceofmajor pages 1-2)

### 5.3 Infectious agents
Not applicable based on retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Neurolathyrism causal chain (β-ODAP)
**Trigger:** prolonged exposure to β-ODAP/β-L-ODAP from grass pea diets (often under drought/food insecurity). (bekelealemu2024thepotentialof pages 2-3)

**Molecular/cellular:** β-ODAP is described as an excitatory amino acid agonist at AMPA receptors, associated with intracellular Ca2+ overload, mitochondrial respiration disturbance, reduced amino acid transport, and increased oxidative stress, leading to excitotoxic motor neuron degeneration and paralysis. (bekelealemu2024thepotentialof pages 5-7)

**Tissue/system:** degeneration of corticospinal/pyramidal tract neurons in spinal cord/leg cortex producing spastic paraparesis. (bekelealemu2024thepotentialof pages 2-3)

**Suggested GO biological processes (confirm in GO):**
- Excitotoxicity / glutamate receptor signaling pathway
- Neuron death: GO:0070997 (neuron death) (confirm)
- Oxidative stress response: GO:0006979

**Suggested CL cell types (confirm in Cell Ontology):**
- Motor neuron: CL:0000100

### 6.2 Osteo-/angiolathyrism causal chain (BAPN → LOX inhibition)
**Trigger:** BAPN exposure (classically linked to *L. odoratus* ingestion; also used experimentally). (carlson2002caseiz16753 pages 3-4, merico2021inhibitionoflysyl pages 1-2)

**Molecular:** BAPN irreversibly inhibits LOX, disrupting oxidative deamination of lysine/hydroxylysine residues in collagen/elastin and preventing normal intermolecular covalent cross-links required for tensile strength and ECM maturation. (carlson2002caseiz16753 pages 3-4, merico2021inhibitionoflysyl pages 1-2)

**Downstream vascular remodeling:** In a rat model, LOX inhibition is associated with increased apoptosis, stimulated TGF-β signaling (p-SMAD2), and increased MMP-2/MMP-9 expression contributing to ascending aorta disruption. (merico2021inhibitionoflysyl pages 1-2)

**Tissue/system manifestations:**
- Bone: periosteal exostoses and fibro-osseous lesions; impaired bone quality and remodeling. (carlson2002caseiz16753 pages 3-4, suliman2023theeffectsof pages 1-2)
- Vasculature: aortic/arterial aneurysm and fatal rupture in models. (merico2021inhibitionoflysyl pages 1-2, carlson2002caseiz16753 pages 1-3)

**Suggested GO terms:**
- Collagen fibril organization: GO:0030199
- Elastic fiber assembly: GO:0048251 (confirm)
- Extracellular matrix organization: GO:0030198
- TGF-β receptor signaling pathway: GO:0007179
- Matrix metalloproteinase activation / extracellular matrix disassembly: GO:0022617

**Suggested CL cell types:**
- Vascular smooth muscle cell: CL:0000192
- Fibroblast: CL:0000057
- Osteoblast: CL:0000062
- Osteocyte: CL:0000136

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- Neurolathyrism: central motor pathways (corticospinal/pyramidal tract) with predominant lower-limb functional deficit. (bekelealemu2024thepotentialof pages 2-3, yesuf2024prevalenceassociatedfactors pages 1-5)
- Angiolathyrism: ascending aorta / major arteries (aneurysm/dissection/rupture). (merico2021inhibitionoflysyl pages 1-2, carlson2002caseiz16753 pages 1-3)
- Osteolathyrism: bone at tendon insertion sites; impaired bone matrix/collagen quality. (carlson2002caseiz16753 pages 3-4, suliman2023theeffectsof pages 1-2)

### 7.2 Suggested UBERON terms (confirm exact IDs)
- Spinal cord (UBERON:0002240)
- Cerebral cortex / motor cortex (UBERON:0000956)
- Ascending aorta (UBERON:0001496)
- Femur (UBERON:0000981)

---

## 8. Temporal Development

- Neurolathyrism is described as lifelong/incurable spastic paralysis in the Ethiopian patient study context. (bimerew2024prevalenceofmajor pages 1-2)
- Community staging (I–IV) reflects progressive functional impairment from spastic gait to being bedridden with contractures. (yesuf2024prevalenceassociatedfactors pages 1-5)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Not applicable: evidence supports an environmental/toxin-driven etiology; no Mendelian inheritance described. (bekelealemu2024thepotentialof pages 2-3)

### 9.2 Epidemiology (recent statistics)
**Delanta district, Ethiopia (survey Nov–Dec 2022; posted May 2024):**
- n=470 analyzed; 56 cases (11.9% of participants) and “population-level prevalence … 6.6%.” (yesuf2024prevalenceassociatedfactors pages 1-5)

**Dawunt district, Ethiopia (community study referenced in BMC Psychiatry Apr 2024):**
- Point prevalence reported as 2.4% (95% CI 2.0–3.0). (bimerew2024prevalenceofmajor pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria (from recent community study definition)
Neurolathyrism diagnosis in community work relied on a clinical syndrome of spastic paraparesis with sensory sparing and dietary exposure history (grass pea consumption). (yesuf2024prevalenceassociatedfactors pages 1-5)

### 10.2 Differential diagnosis
No detailed differential diagnosis workup was found in the retrieved evidence; common differentials in clinical neurology (e.g., hereditary spastic paraplegia, myelopathy, MS, B12 deficiency) should be validated from clinical references not retrieved here.

### 10.3 Biomarkers / laboratory tests
No validated human diagnostic biomarker assays were identified in the retrieved evidence.

---

## 11. Outcome / Prognosis

- Neurolathyrism is described as **irreversible** with “lifelong incurable spastic paralysis of lower extremities” in the Ethiopian patient study context. (bimerew2024prevalenceofmajor pages 1-2)
- Major morbidity includes mobility impairment: in Delanta, 100% of cases had walking difficulty and 96.4% relied on a walking stick. (yesuf2024prevalenceassociatedfactors pages 9-12)

---

## 12. Treatment

### 12.1 Pharmacotherapy
No disease-modifying pharmacotherapy for established neurolathyrism was identified in the retrieved evidence.

### 12.2 Supportive and rehabilitative care
Evidence supports supportive interventions addressing disability and mental health:
- Formal counselling and regular exercise were associated with decreased odds of major depressive disorder among neurolathyrism patients. (bimerew2024prevalenceofmajor pages 1-2)

**Suggested MAXO terms (confirm IDs in MAXO):**
- Physical therapy / exercise therapy
- Psychological counselling
- Assistive device use (walking aids)

---

## 13. Prevention

### 13.1 Primary prevention (risk reduction)
The retrieved evidence supports prevention as primarily **food-system and agricultural/toxin-exposure mitigation**, including:
- Reducing β-ODAP in grass pea via plant breeding/genomics and potentially CRISPR-based targeting of BOS/CAS pathway genes. (bekelealemu2024thepotentialof pages 11-13, edwards2023genomicsandbiochemical pages 1-2)
- Nutritional strategies (improving sulfur amino acid adequacy) to reduce β-ODAP neurotoxicity risk. (bekelealemu2024thepotentialof pages 2-3)

### 13.2 Real-world implementations and applications
- Genomics-enabled crop improvement: availability of a high-quality *L. sativus* genome and identified biosynthetic genes provides a concrete implementation pathway for developing low-toxin cultivars for food security contexts. (edwards2023genomicsandbiochemical pages 1-2, edwards2023genomicsandbiochemical pages 2-4)
- Public health: the Delanta study explicitly calls for inclusion of lathyrism in national disease reporting and targeted prevention policies, reflecting real-world surveillance implications. (yesuf2024prevalenceassociatedfactors pages 1-5)

---

## 14. Other Species / Natural Disease

- Animal susceptibility is supported in lathyrism literature cited by aortic rupture in turkeys fed *L. odoratus* and BAPN-induced aneurysm/rupture models. (sherif2010insearchof pages 3-4, carlson2002caseiz16753 pages 1-3)

NCBI Taxon identifiers and OMIA links were not retrievable from the current evidence set.

---

## 15. Model Organisms

### 15.1 Induced models
- **BAPN (LOX inhibition) models** in rats reproduce key features of angiolathyrism (ascending aortic disruption, MMP/TGF-β activation) and osteolathyrism (defective collagen cross-linking/bone pathology). (merico2021inhibitionoflysyl pages 1-2, suliman2023theeffectsof pages 1-2)

### 15.2 Model limitations
The retrieved evidence does not provide direct head-to-head validation against human lathyrism phenotypes for all endpoints; caution is warranted when translating vascular/bone findings to human disease.

---

## Recent developments (2023–2024) highlighted
1. **Pathway resolution and genome resource:** 2023 *Nature Communications* work produced a chromosome-scale genome assembly and identified LsAAE3–LsBOS metabolon controlling final β-L-ODAP production. (edwards2023genomicsandbiochemical pages 1-2)
2. **Genome-editing proposals:** 2024 review proposed CRISPR/Cas9 targeting BOS and CAS (including multi-target strategies and amino-acid substitutions) to reduce β-ODAP. (bekelealemu2024thepotentialof pages 11-13)
3. **New epidemiologic measurements and social impact quantification:** 2024 Ethiopia community work provided updated prevalence estimates and quantified social consequences (school discontinuation, divorce) and mobility impairment rates. (yesuf2024prevalenceassociatedfactors pages 9-12, yesuf2026neurolathyrismindelanta pages 1-2)

---

## Evidence-based statistics (from recent studies)
- Delanta (Ethiopia) neurolathyrism prevalence: 56/470 (11.9% of participants) and estimated population prevalence 6.6%. (yesuf2024prevalenceassociatedfactors pages 1-5)
- Dawunt (Ethiopia) point prevalence: 2.4% (95% CI 2.0–3.0). (bimerew2024prevalenceofmajor pages 2-4)
- Neurolathyrism patient comorbidity: major depressive disorder prevalence 38.7% among adult neurolathyrism patients (PHQ-9 ≥10). (bimerew2024prevalenceofmajor pages 1-2)

---

## Direct quotes from abstracts (available in retrieved evidence)
- Bimerew et al. (BMC Psychiatry, Apr 2024) describes neurolathyrism as: “a chronic illness characterized by lifelong incurable spastic paralysis of lower extremities; causing permanent disability.” (bimerew2024prevalenceofmajor pages 1-2)
- The same abstract reports: “the prevalence of MDD was found to be 38.7%.” (bimerew2024prevalenceofmajor pages 1-2)

---

## Key references with URLs and dates (prioritizing 2023–2024)
- Edwards A. et al. *Nature Communications* (Feb 2023). “Genomics and biochemical analyses reveal a metabolon key to β-L-ODAP biosynthesis in *Lathyrus sativus*.” https://doi.org/10.1038/s41467-023-36503-2 (edwards2023genomicsandbiochemical pages 1-2)
- Bekele-Alemu A. et al. *Current Issues in Molecular Biology* (Sep 2024). “The Potential of CRISPR/Cas9 to Circumvent the Risk Factor Neurotoxin β-N-oxalyl-L-α, β-diaminopropionic acid…” https://doi.org/10.3390/cimb46090626 (bekelealemu2024thepotentialof pages 11-13)
- Yesuf A.E. et al. Preprint (May 2024). “Prevalence, Associated Factors, and Social Status of Patients with Neurolathyrisim in Delanta…” https://doi.org/10.21203/rs.3.rs-4332232/v1 (yesuf2024prevalenceassociatedfactors pages 1-5)
- Bimerew M. et al. *BMC Psychiatry* (Apr 2024). “Prevalence of major depressive disorder… among adult patients with neurolathyrism…” https://doi.org/10.1186/s12888-024-05755-7 (bimerew2024prevalenceofmajor pages 1-2)

---

## Major gaps in the retrieved evidence (needs follow-up retrieval for KB completeness)
- Standard disease identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) were not available in the retrieved text evidence.
- No primary human neuropathology/neuroimaging studies, nor prospective incidence estimates, were retrieved.
- No human genetic susceptibility data were retrieved.
- No formal diagnostic criteria guidelines or treatment guidelines were retrieved.

These gaps should be filled by targeted ontology lookup (MONDO/MeSH/ICD), and PubMed retrieval of clinical neurology reviews and historical/modern neuropathology studies.


References

1. (bekelealemu2024thepotentialof pages 2-3): Abreham Bekele-Alemu, Deribew Girma-Tola, and Ayalew Ligaba-Osena. The potential of crispr/cas9 to circumvent the risk factor neurotoxin β-n-oxalyl-l-α, β-diaminopropionic acid limiting wide acceptance of the underutilized grass pea (lathyrus sativus l.). Current Issues in Molecular Biology, 46:10570-10589, Sep 2024. URL: https://doi.org/10.3390/cimb46090626, doi:10.3390/cimb46090626. This article has 6 citations.

2. (yesuf2024prevalenceassociatedfactors pages 1-5): Andualem Endrias Yesuf, Eden Efrem Mersiehazen, Bemnet Yazew Abegaz, Samson Zegeye Endale, Beyadiglign Wondimu Gebresilssie, and Biniyam Jemaneh Batu. Prevalence, associated factors, and social status of patients with neurolathyrisim in delanta, amhara region, ethiopia: a community-based cross- sectional study. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4332232/v1, doi:10.21203/rs.3.rs-4332232/v1.

3. (carlson2002caseiz16753 pages 3-4): CS Carlson. Case i: z16753 (afip 3138054). Unknown journal, 2002.

4. (merico2021inhibitionoflysyl pages 1-2): Valeria Merico, Jacopo Francesco Imberti, Mario Zanoni, Giuseppe Boriani, Silvia Garagna, and Roberto Imberti. Inhibition of lysyl oxidase stimulates tgf-β signaling and metalloproteinases-2 and -9 expression and contributes to the disruption of ascending aorta in rats: protection by propylthiouracil. Heart and Vessels, 36:738-747, Jan 2021. URL: https://doi.org/10.1007/s00380-020-01750-6, doi:10.1007/s00380-020-01750-6. This article has 7 citations and is from a peer-reviewed journal.

5. (bekelealemu2024thepotentialof pages 5-7): Abreham Bekele-Alemu, Deribew Girma-Tola, and Ayalew Ligaba-Osena. The potential of crispr/cas9 to circumvent the risk factor neurotoxin β-n-oxalyl-l-α, β-diaminopropionic acid limiting wide acceptance of the underutilized grass pea (lathyrus sativus l.). Current Issues in Molecular Biology, 46:10570-10589, Sep 2024. URL: https://doi.org/10.3390/cimb46090626, doi:10.3390/cimb46090626. This article has 6 citations.

6. (edwards2023genomicsandbiochemical pages 12-13): Anne Edwards, Isaac Njaci, Abhimanyu Sarkar, Zhouqian Jiang, Gemy George Kaithakottil, Christopher Moore, Jitender Cheema, Clare E. M. Stevenson, Martin Rejzek, Petr Novák, Marielle Vigouroux, Martin Vickers, Roland H. M. Wouters, Pirita Paajanen, Burkhard Steuernagel, Jonathan D. Moore, Janet Higgins, David Swarbreck, Stefan Martens, Colin Y. Kim, Jing-Ke Weng, Sagadevan Mundree, Benjamin Kilian, Shiv Kumar, Matt Loose, Levi Yant, Jiří Macas, Trevor L. Wang, Cathie Martin, and Peter M. F. Emmrich. Genomics and biochemical analyses reveal a metabolon key to β-l-odap biosynthesis in lathyrus sativus. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36503-2, doi:10.1038/s41467-023-36503-2. This article has 43 citations and is from a highest quality peer-reviewed journal.

7. (edwards2023genomicsandbiochemical pages 1-2): Anne Edwards, Isaac Njaci, Abhimanyu Sarkar, Zhouqian Jiang, Gemy George Kaithakottil, Christopher Moore, Jitender Cheema, Clare E. M. Stevenson, Martin Rejzek, Petr Novák, Marielle Vigouroux, Martin Vickers, Roland H. M. Wouters, Pirita Paajanen, Burkhard Steuernagel, Jonathan D. Moore, Janet Higgins, David Swarbreck, Stefan Martens, Colin Y. Kim, Jing-Ke Weng, Sagadevan Mundree, Benjamin Kilian, Shiv Kumar, Matt Loose, Levi Yant, Jiří Macas, Trevor L. Wang, Cathie Martin, and Peter M. F. Emmrich. Genomics and biochemical analyses reveal a metabolon key to β-l-odap biosynthesis in lathyrus sativus. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36503-2, doi:10.1038/s41467-023-36503-2. This article has 43 citations and is from a highest quality peer-reviewed journal.

8. (suliman2023theeffectsof pages 1-2): Mubarak Suliman, Masako Nagasawa, Farah A. Al-Omari, and Katsumi Uoshima. The effects of collagen cross-link deficiency on osseointegration process of pure titanium implants. Journal of prosthodontic research, 68:449-455, Oct 2023. URL: https://doi.org/10.2186/jpr.jpr\_d\_22\_00249, doi:10.2186/jpr.jpr\_d\_22\_00249. This article has 2 citations and is from a domain leading peer-reviewed journal.

9. (carlson2002caseiz16753 pages 1-3): CS Carlson. Case i: z16753 (afip 3138054). Unknown journal, 2002.

10. (yesuf2024prevalenceassociatedfactors pages 5-9): Andualem Endrias Yesuf, Eden Efrem Mersiehazen, Bemnet Yazew Abegaz, Samson Zegeye Endale, Beyadiglign Wondimu Gebresilssie, and Biniyam Jemaneh Batu. Prevalence, associated factors, and social status of patients with neurolathyrisim in delanta, amhara region, ethiopia: a community-based cross- sectional study. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4332232/v1, doi:10.21203/rs.3.rs-4332232/v1.

11. (yesuf2024prevalenceassociatedfactors pages 12-15): Andualem Endrias Yesuf, Eden Efrem Mersiehazen, Bemnet Yazew Abegaz, Samson Zegeye Endale, Beyadiglign Wondimu Gebresilssie, and Biniyam Jemaneh Batu. Prevalence, associated factors, and social status of patients with neurolathyrisim in delanta, amhara region, ethiopia: a community-based cross- sectional study. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4332232/v1, doi:10.21203/rs.3.rs-4332232/v1.

12. (bimerew2024prevalenceofmajor pages 1-2): Melaku Bimerew, Teshome Gebremeskel, Biruk Beletew, Wondye Ayaliew, Mulugeta Wodaje, and Manay Ayalneh. Prevalence of major depressive disorder and its associated factors among adult patients with neurolathyrism in dawunt district, ethiopia; 2022: community-based cross-sectional study. BMC Psychiatry, Apr 2024. URL: https://doi.org/10.1186/s12888-024-05755-7, doi:10.1186/s12888-024-05755-7. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (bekelealemu2024thepotentialof pages 1-2): Abreham Bekele-Alemu, Deribew Girma-Tola, and Ayalew Ligaba-Osena. The potential of crispr/cas9 to circumvent the risk factor neurotoxin β-n-oxalyl-l-α, β-diaminopropionic acid limiting wide acceptance of the underutilized grass pea (lathyrus sativus l.). Current Issues in Molecular Biology, 46:10570-10589, Sep 2024. URL: https://doi.org/10.3390/cimb46090626, doi:10.3390/cimb46090626. This article has 6 citations.

14. (bimerew2024prevalenceofmajor pages 2-4): Melaku Bimerew, Teshome Gebremeskel, Biruk Beletew, Wondye Ayaliew, Mulugeta Wodaje, and Manay Ayalneh. Prevalence of major depressive disorder and its associated factors among adult patients with neurolathyrism in dawunt district, ethiopia; 2022: community-based cross-sectional study. BMC Psychiatry, Apr 2024. URL: https://doi.org/10.1186/s12888-024-05755-7, doi:10.1186/s12888-024-05755-7. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (yesuf2026neurolathyrismindelanta pages 1-2): Andualem Endrias Yesuf, Eden Efrem Mersiehazen, Bemnet Yazew Abegaz, Samson Zegeye Endale, Beyadiglign Wondimu Gebresilssie, and Biniyam Jemaneh Batu. Neurolathyrism in delanta, ethiopia: prevalence, associated factors, and social impact: a cross-sectional study. BMC Neurology, Apr 2026. URL: https://doi.org/10.1186/s12883-026-04871-z, doi:10.1186/s12883-026-04871-z. This article has 0 citations and is from a peer-reviewed journal.

16. (edwards2023genomicsandbiochemical pages 2-4): Anne Edwards, Isaac Njaci, Abhimanyu Sarkar, Zhouqian Jiang, Gemy George Kaithakottil, Christopher Moore, Jitender Cheema, Clare E. M. Stevenson, Martin Rejzek, Petr Novák, Marielle Vigouroux, Martin Vickers, Roland H. M. Wouters, Pirita Paajanen, Burkhard Steuernagel, Jonathan D. Moore, Janet Higgins, David Swarbreck, Stefan Martens, Colin Y. Kim, Jing-Ke Weng, Sagadevan Mundree, Benjamin Kilian, Shiv Kumar, Matt Loose, Levi Yant, Jiří Macas, Trevor L. Wang, Cathie Martin, and Peter M. F. Emmrich. Genomics and biochemical analyses reveal a metabolon key to β-l-odap biosynthesis in lathyrus sativus. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36503-2, doi:10.1038/s41467-023-36503-2. This article has 43 citations and is from a highest quality peer-reviewed journal.

17. (bekelealemu2024thepotentialof pages 11-13): Abreham Bekele-Alemu, Deribew Girma-Tola, and Ayalew Ligaba-Osena. The potential of crispr/cas9 to circumvent the risk factor neurotoxin β-n-oxalyl-l-α, β-diaminopropionic acid limiting wide acceptance of the underutilized grass pea (lathyrus sativus l.). Current Issues in Molecular Biology, 46:10570-10589, Sep 2024. URL: https://doi.org/10.3390/cimb46090626, doi:10.3390/cimb46090626. This article has 6 citations.

18. (yesuf2024prevalenceassociatedfactors pages 9-12): Andualem Endrias Yesuf, Eden Efrem Mersiehazen, Bemnet Yazew Abegaz, Samson Zegeye Endale, Beyadiglign Wondimu Gebresilssie, and Biniyam Jemaneh Batu. Prevalence, associated factors, and social status of patients with neurolathyrisim in delanta, amhara region, ethiopia: a community-based cross- sectional study. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4332232/v1, doi:10.21203/rs.3.rs-4332232/v1.

19. (sherif2010insearchof pages 3-4): H. M. F. Sherif. In search of a new therapeutic target for the treatment of genetically triggered thoracic aortic aneurysms and cardiovascular conditions: insights from human and animal lathyrism. Interactive CardioVascular and Thoracic Surgery, 11:271-276, Jun 2010. URL: https://doi.org/10.1510/icvts.2010.239681, doi:10.1510/icvts.2010.239681. This article has 29 citations.

## Artifacts

- [Edison artifact artifact-00](Lathyrism-deep-research-falcon_artifacts/artifact-00.md)