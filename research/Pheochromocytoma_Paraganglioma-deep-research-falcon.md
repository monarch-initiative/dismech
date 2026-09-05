---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T01:16:25.734740'
end_time: '2026-08-01T01:28:42.665976'
duration_seconds: 736.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pheochromocytoma and Paraganglioma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Pheochromocytoma_Paraganglioma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pheochromocytoma and Paraganglioma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Pheochromocytoma and Paraganglioma** covering all of the
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
- **Disease Name:** Pheochromocytoma and Paraganglioma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Pheochromocytoma and Paraganglioma** covering all of the
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


# Pheochromocytoma and Paraganglioma: Disease Characteristics Report

## Executive summary

Pheochromocytomas and paragangliomas (PPGLs) are rare neural-crest-derived neuroendocrine neoplasms. A pheochromocytoma (PCC) arises in adrenal-medullary chromaffin cells; a paraganglioma (PGL) arises in extra-adrenal sympathetic or parasympathetic paraganglia. Approximately 80–85% are adrenal PCCs and 15–20% are extra-adrenal PGLs. Catecholamine excess causes episodic or sustained cardiovascular and metabolic disease, while every PPGL is regarded as having some metastatic potential under current WHO classification. Germline predisposition occurs in roughly 30–40% overall and 70–80% of pediatric cases, making PPGL among the most heritable human tumors. Contemporary practice therefore combines biochemical diagnosis, molecular imaging, universal germline testing, surgery when feasible, lifelong risk-adapted surveillance, and genotype/target-informed systemic therapy. (t.2024pheochromocytomaanupdated pages 1-2, casey2024internationalconsensusstatement pages 1-2, cascon2023geneticbasesof pages 1-2)

A compact quantitative evidence summary is provided below.

| Domain | High-confidence quantitative finding/recommendation | Evidence type/year | Key source DOI or PMID where available |
|---|---|---|---|
| Epidemiology / heredity | PPGLs are rare neuroendocrine tumors; ~80–85% arise in adrenal medulla and ~15–20% are extra-adrenal paragangliomas; hereditary contribution is commonly ~30–40% overall (t.2024pheochromocytomaanupdated pages 1-2, cascon2023geneticbasesof pages 1-2) | Peer-reviewed reviews, 2023–2024 | 10.3389/fendo.2024.1433582; 10.1530/JME-22-0167 |
| Molecular classification | Three major molecular clusters: pseudohypoxia (cluster 1), kinase signaling (cluster 2), and Wnt-signaling / MAML3-CSDE1-associated cluster 3 (t.2024pheochromocytomaanupdated pages 1-2, cascon2023geneticbasesof pages 1-2, t.2024pheochromocytomaanupdated pages 3-6) | Peer-reviewed reviews, 2023–2024 | 10.3389/fendo.2024.1433582; 10.1530/JME-22-0167 |
| Major susceptibility genes | >20 driver/susceptibility genes reported; commonly cited genes include SDHA/B/C/D, SDHAF2, VHL, RET, NF1, TMEM127, MAX, FH, MDH2, SLC25A11, DLST, EPAS1/EGLN-related genes (cascon2023geneticbasesof pages 1-2, t.2024pheochromocytomaanupdated pages 3-6) | Peer-reviewed review, 2023; scoping review, 2024 | 10.1530/JME-22-0167; 10.3389/fendo.2024.1433582 |
| Phenotypes / symptom frequencies | Classic symptoms/signs are variable; one 2024 scoping review summarized hypertension 92%, sustained hypertension 48%, paroxysmal hypertension 44%, headache 59%, palpitations 50%, diaphoresis 50%, dizziness 67%, orthostatic hypotension 12% (t.2024pheochromocytomaanupdated pages 6-7) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Biochemical diagnosis | Plasma free metanephrines: sensitivity ~96%, specificity ~85%; suggested highly indicative thresholds in one review were normetanephrine >2.5 pmol/mL or metanephrine >1.4 pmol/mL; supine sampling after ≥30 min recumbency is recommended to reduce false positives (t.2024pheochromocytomaanupdated pages 3-6) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Urinary diagnosis | 24-hour urinary catecholamines/metanephrines: sensitivity ~87.5%, specificity ~99.7%; urinary metanephrine/creatinine linkage can improve accuracy (t.2024pheochromocytomaanupdated pages 3-6) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Adjunct biochemical marker | Plasma 3-methoxytyramine is recommended with metanephrines as a first-line biochemical marker set, especially relevant for dopamine/SDH-related biology (casey2020geneticstratificationof pages 4-5) | Peer-reviewed review, 2020 | 10.1093/hmg/ddaa201 |
| Clonidine suppression | For distinguishing false-positive norepinephrine elevations, clonidine suppression test reported sensitivity 97% and specificity 100%; <50% fall in plasma norepinephrine after clonidine is abnormal (t.2024pheochromocytomaanupdated pages 6-7) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Anatomic imaging | CT abdomen/pelvis is typical first localization test after biochemical evidence; CT sensitivity reported as 88% and accuracy 90–95% for tumors >1.3 cm in one review (t.2024pheochromocytomaanupdated pages 6-7) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Functional imaging detection rates | 68Ga-DOTA-SST PET/CT detection ~93% (95% CI 91–95) as first-line functional imaging in one review; 18F-DOPA PET/CT ~80% (95% CI 69–88) in hereditary cluster 2; 18F-FDG PET/CT ~74% (95% CI 46–91) as alternative (t.2024pheochromocytomaanupdated pages 7-8) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Genotype-specific imaging guidance | SDHx-related tumors: [68Ga]-DOTA-SSA PET/CT favored; VHL- and many kinase-cluster tumors: [18F]FDOPA PET/CT often most sensitive; [123I]MIBG sensitivity ~50–75% overall and <50% in SDHB-associated tumors (giacche2024pheochromocytoma–paragangliomasyndromea pages 10-12) | Review, 2024 | 10.3390/biomedicines12102385 |
| Genetic testing strategy | Germline testing is recommended for all PPGL patients; targeted NGS panels are described as current gold standard, rather than sequential gene-by-gene testing (cascon2023geneticbasesof pages 6-8, t.2024pheochromocytomaanupdated pages 7-8) | Peer-reviewed review, 2023; scoping review, 2024 | 10.1530/JME-22-0167; 10.3389/fendo.2024.1433582 |
| IHC / pathology support | Loss of SDHB staining is a useful screening/prognostic biomarker for SDHx-related disease; SDHA-, MAX-, and FH-related IHC can support variant interpretation; histopathology alone cannot diagnose malignancy, which requires metastasis (casey2020geneticstratificationof pages 4-5, cascon2023geneticbasesof pages 6-8, t.2024pheochromocytomaanupdated pages 7-8) | Reviews, 2020–2024 | 10.1093/hmg/ddaa201; 10.1530/JME-22-0167; 10.3389/fendo.2024.1433582 |
| Inheritance / penetrance example: SDHD | SDHD shows autosomal dominant inheritance modified by maternal imprinting; penetrance reported as 86% by age 50; tumors are mainly head-and-neck, with thoraco-abdominal PGL up to 22% and PCC 12–24% (cascon2023geneticbasesof pages 4-5) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Inheritance / penetrance example: SDHB | SDHB mutations occur in ~8–10% of PPGL; penetrance reported as ~30% by age 80 in one review; associated with thoraco-abdominal PGLs, H&N PGLs, and PCCs, with higher metastatic concern (cascon2023geneticbasesof pages 2-4, cascon2023geneticbasesof pages 4-5) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Inheritance / penetrance example: SDHA | SDHA pathogenic variants can be found in up to ~10% of PPGL in cited review datasets, with low penetrance estimated around 10% by age 70 and often apparently sporadic presentation (cascon2023geneticbasesof pages 4-5) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Syndrome example: VHL | ~20% of VHL patients develop PCC/PGL; VHL-related PPGL are often multifocal/bilateral (43–45%), metastatic in <5%, and median diagnosis age ~29 years (cascon2023geneticbasesof pages 4-5) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Syndrome example: MEN2 / RET | ~50% of MEN2 patients develop PCC; 50–80% of MEN2-associated PCCs are bilateral; only a small percentage metastasize (cascon2023geneticbasesof pages 5-6) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Syndrome example: NF1 | Estimated 0.1–5.7% of NF1 patients develop PPGL (3.3–13% in autopsy studies); NF1-associated PPGL are usually unilateral and metastasize up to ~10% (cascon2023geneticbasesof pages 5-6) | Peer-reviewed review, 2023 | 10.1530/JME-22-0167 |
| Syndrome example: MAX | MAX germline review of 109 carriers reported mean diagnosis age 32.8 years, bilateral PCC in 59/101 PCC cases, metastasis in 19/101 (~18.8%), and male:female ratio 1.3:1 (OpenTargets Search: pheochromocytoma,paraganglioma) | Aggregated case series/review, 2024 | 10.3389/fendo.2024.1442691 |
| Metastatic-risk markers | Independent correlates of metastatic risk reported in review include SDHB mutation plus norepinephrine/dopamine biochemical phenotype; larger size, extra-adrenal location, and cluster-1 biology are recurrent risk signals (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, t.2024pheochromocytomaanupdated pages 7-8) | Reviews, 2024 | 10.3390/biomedicines12102385; 10.3389/fendo.2024.1433582 |
| Aggressive disease biomarkers | Somatic ATRX alterations, TERT activation, and MAML3 fusions are associated with aggressive/metastatic behavior; MAML3 rearranged tumors had metastases in 37.5% in one cited review summary (casey2020geneticstratificationof pages 4-5, cascon2023geneticbasesof pages 6-8) | Reviews/pre-existing primary data synthesis | 10.1093/hmg/ddaa201; 10.1530/JME-22-0167 |
| Surgery | Minimally invasive/laparoscopic resection is generally suitable for most pheochromocytomas <5 cm; open surgery/lymph-node dissection may be preferred for larger, invasive, extra-adrenal, synchronous metastatic, or SDHB-associated tumors (t.2024pheochromocytomaanupdated pages 7-8) | Scoping review, 2024 | 10.3389/fendo.2024.1433582 |
| Perioperative blockade | Endocrine Society-based preparation: alpha-blockade first; phenoxybenzamine start 10 mg orally twice daily and titrate up to 1 mg/kg/day, or doxazosin; beta-blocker added 3–4 days later if needed; increased salt/water intake 10–14 days pre-op (t.2024pheochromocytomaanupdated pages 7-8) | Scoping review/guideline-based summary, 2024 | 10.3389/fendo.2024.1433582 |
| Metastatic radionuclide therapy: HSA-I-131-MIBG | FDA-approved in 2018 for metastatic PPGL; response rate ~30–40% in review summary; phase II multicenter trial of 68 patients: 25% had durable antihypertensive-medication reduction, 92% achieved partial response or stable disease within 12 months, median OS 36.7 months (95% CI 29.9–49.1) (t.2024pheochromocytomaanupdated pages 7-8) | Phase II trial summarized in 2024 review | 10.3389/fendo.2024.1433582 |
| Real-world MIBG outcome | Real-world study of 24 metastatic PPGL patients reported 38% objective response rate, 83% disease control rate, BP normalization in 56%, but notable grade 3–4 myelosuppression and one fatal pneumonitis (t.2024pheochromocytomaanupdated pages 8-9) | Real-world study summarized in review, 2024 | 10.3389/fendo.2024.1433582 |
| Chemotherapy | Conventional chemotherapy response is ~37% overall in review summary; complete responses are uncommon; temozolomide may be especially relevant in SDHB/MGMT-methylated disease (t.2024pheochromocytomaanupdated pages 8-9) | Review, 2024 | 10.3389/fendo.2024.1433582 |
| TKIs / targeted therapy | Sunitinib small studies showed disease control ~57–83% and median PFS ~4–13 months; FIRSTMAPP phase II reported 12-month PFS 36% on sunitinib vs 19% placebo; cabozantinib phase II ORR 25.0% (4/16 responders); axitinib phase II partial response 36% (t.2024pheochromocytomaanupdated pages 8-9) | Phase II and review summaries, 2024 | 10.3389/fendo.2024.1433582 |
| Surveillance | For metastatic PPGL, CT/MRI every 3–6 months in first year, then every 6–12 months if stable; secretory disease should have plasma free or 24-h urinary fractionated metanephrines at least every 6 months (t.2024pheochromocytomaanupdated pages 7-8, taieb2023clinicalconsensusguideline pages 19-21) | Review/guideline summaries, 2023–2024 | 10.3389/fendo.2024.1433582; 10.1016/S2213-8587(23)00038-4 |
| Pediatric disease | Pediatric PPGL accounts for ~10–20% of all PPGL; annual incidence ~0.5–2.0 per million children; median presentation age 11–15 years; hereditary background in ~70–80% (casey2024internationalconsensusstatement pages 1-2) | International consensus statement, 2024 | 10.17863/cam.111911 |
| Pediatric metastatic management | In pediatric metastatic PPGL, surgery is the only curative therapy; about 50% of treatment-naive patients may show stable disease at 1 year; radionuclide therapy is considered for avid tumors without rapid progression (casey2024internationalconsensusstatement pages 11-13) | International consensus statement, 2024 | 10.17863/cam.111911 |
| Recent single-cell findings | A 2024 preprint scRNA-seq study of 16 tissues from 5 PCC patients identified “metabolism-type” (NDUFA4L2/COX4I2) and “kinase-type” (RET/PNMT) tumors, with distinct immune microenvironments and potential therapeutic implications; this is preprint-level evidence (OpenTargets Search: pheochromocytoma,paraganglioma) | Preprint, 2024 | 10.1101/2023.03.26.534245 |
| Recent multi-omics findings | A 2024 preprint multi-omic analysis of 94 SDHB-deficient tumors from 79 patients linked TERT and ATRX alterations with metastatic disease, increased mutation load, and treatment-related profiles including MGMT overexpression/MMR deficiency; preprint-level evidence (OpenTargets Search: pheochromocytoma,paraganglioma) | Preprint, 2024 | 10.21203/rs.3.rs-4410500/v1 |
| Active recent trials | Examples from ClinicalTrials.gov search: NCT07714551 zanzalintinib phase II not yet recruiting (n=14); NCT07282587 ONC206 phase II recruiting (n=90); NCT03206060 Lu-177-DOTATATE phase II recruiting (n=130); NCT07680205 belzutifan impact on catecholamine metabolism phase II recruiting (n=12); NCT06429397 anlotinib + benmelstobart phase II not yet recruiting (n=22) (OpenTargets Search: pheochromocytoma,paraganglioma) | ClinicalTrials.gov records, current at retrieval | NCT07714551; NCT07282587; NCT03206060; NCT07680205; NCT06429397 |
| Evidence gaps | Limited high-level evidence for environmental/protective factors and gene–environment interactions; limited validated QoL datasets in retrieved evidence; no robust protective genetic variants established; comparative veterinary disease/model-system evidence was not substantively captured in retrieved contexts; several omics findings are from preprints and need peer-reviewed validation (t.2024pheochromocytomaanupdated pages 8-9, cascon2023geneticbasesof pages 1-2) | Evidence-gap summary from retrieved set | 10.3389/fendo.2024.1433582; 10.1530/JME-22-0167 |


*Table: This table compiles compact, knowledge-base–ready evidence on pheochromocytoma and paraganglioma across clinical, genetic, diagnostic, and treatment domains. It prioritizes quantitative findings and recent sources, while flagging areas where evidence remains sparse or preprint-only.*

## 1. Disease information

### Definition, category, and terminology

**Category:** rare neuroendocrine neoplasm; neural-crest/chromaffin-cell tumor; hereditary-cancer syndrome when caused by a germline pathogenic variant.

* **Pheochromocytoma:** adrenal-medullary PPGL.
* **Sympathetic PGL:** usually thoracic, abdominal, or pelvic; commonly catecholamine-secreting.
* **Parasympathetic PGL:** usually skull-base/head-and-neck, including carotid-body, vagal, jugulotympanic, and related sites; often nonsecretory.
* **Metastatic PPGL:** tumor present in a site where normal paraganglial tissue does not occur—commonly lymph node, bone, liver, or lung. Histology alone cannot establish benignity or reliably exclude future metastasis. (casey2020geneticstratificationof pages 4-5)

**Synonyms:** PPGL; PCC/PGL; phaeochromocytoma/paraganglioma; chromaffinoma; adrenal paraganglioma; extra-adrenal pheochromocytoma (older term); chemodectoma or glomus tumor for selected head-and-neck PGLs.

### Identifiers

* **MONDO:** pheochromocytoma **MONDO:0008233**; adrenal-gland pheochromocytoma **MONDO:0004974**; hereditary pheochromocytoma–paraganglioma **MONDO:0017366**; malignant adrenal-gland pheochromocytoma **MONDO:0006288**. (OpenTargets Search: pheochromocytoma,paraganglioma)
* **OMIM syndromes:** PGL1/SDHD 168000; PGL2/SDHAF2 601650; PGL3/SDHC 605373; PGL4/SDHB 115310; PGL5/SDHA 614165; PGL6/SLC25A11 618464; PGL7/DLST 618475; VHL 193300; MEN2 171400; NF1 162200. (cascon2023geneticbasesof pages 4-5, cascon2023geneticbasesof pages 5-6)
* **ICD-10-CM:** coding is site/behavior dependent, including D35.0 (benign adrenal neoplasm), D44.6/D44.7 (uncertain behavior of carotid body, aortic body, or other paraganglia), C74.1 (malignant adrenal medulla), and C75.4/C75.5 (malignant carotid/aortic body). These behavior-based labels do not fully reflect the WHO concept that all PPGLs have variable metastatic potential.
* **MeSH:** *Pheochromocytoma* and *Paraganglioma* are separate descriptors.

This report synthesizes **aggregated disease-level resources, cohorts, trials, and guidelines**, not individual EHR records. Variant interpretation for an actual patient still requires the original laboratory report, ACMG/AMP classification, phenotype, family segregation, and—where available—tumor evidence.

## 2. Etiology, risk, protective, and environmental factors

### Causal and susceptibility factors

PPGL is fundamentally a genetic/epigenetic neoplastic disease. Approximately 40% of patients carry an autosomal-dominant germline alteration, about 30% have a recognized somatic driver, and about 30% remain unexplained by currently known genes. More than 20 susceptibility/driver genes are established or strongly implicated. (cascon2023geneticbasesof pages 1-2, cascon2023geneticbasesof pages 2-4)

Major germline causes include **SDHA, SDHB, SDHC, SDHD, SDHAF2, VHL, RET, NF1, TMEM127, MAX, FH, MDH2, SLC25A11, DLST, EGLN1/2**, and less frequently other metabolic-pathway genes. Important somatic/postzygotic events include **NF1, VHL, RET, HRAS, FGFR1, EPAS1, H3-3A, CSDE1**, and **MAML3** rearrangements. Open Targets independently links PCC most strongly to MAX, TMEM127, RET, SDHB, VHL, SDHD, NF1, and SDHA. (OpenTargets Search: pheochromocytoma,paraganglioma, cascon2023geneticbasesof pages 1-2, cascon2023geneticbasesof pages 6-8)

Risk is increased by a pathogenic germline variant, family history, young age, multifocal/bilateral disease, previous PPGL, and syndromic findings such as medullary thyroid carcinoma, VHL lesions, neurofibromas/café-au-lait macules, renal-cell carcinoma, GIST, pituitary tumor, polycythemia, or uterine/cutaneous leiomyomas. SDHB alteration, extra-adrenal location, larger primary tumor, and a norepinephrine/dopamine biochemical phenotype correlate with metastatic risk. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, t.2024pheochromocytomaanupdated pages 7-8)

### Environment and gene–environment interaction

No infectious agent, toxin, occupational exposure, diet, smoking pattern, alcohol exposure, or other modifiable environmental factor is established as a primary PPGL cause. Likewise, no replicated protective lifestyle factor or protective human allele supports primary-prevention advice beyond general cardiovascular health. Hypoxia is mechanistically relevant because cluster-1 tumors constitutively activate a hypoxia-response program, but ordinary environmental hypoxia has not been shown to cause PPGL. Pregnancy can reveal or aggravate a previously occult secretory tumor; LHCGR expression in some tumors offers a plausible hormonal mechanism. (cascon2023geneticbasesof pages 2-4, t.2024pheochromocytomaanupdated pages 3-6)

Accordingly, **validated gene–environment interactions remain an evidence gap**. This is absence of convincing evidence, not proof that environmental modifiers never operate.

## 3. Phenotypes

| Phenotype | Typical character and frequency | Suggested HPO term |
|---|---|---|
| Hypertension | Sustained or episodic; pooled review figures: any hypertension 92%, sustained 48–55%, paroxysmal 30–45%; may cause crisis and target-organ injury | HP:0000822 Hypertension; HP:0004944 Episodic hypertension |
| Headache | Episodic, frequently associated with BP surges; approximately 40–59% | HP:0002315 Headache |
| Palpitations/tachycardia | Episodic; palpitations about 50%, tachycardia about 15% | HP:0001962 Palpitations; HP:0001649 Tachycardia |
| Diaphoresis/hyperhidrosis | Episodic, often accompanying crisis; approximately 50–60% | HP:0000975 Hyperhidrosis |
| Dizziness/syncope | Dizziness 67%, syncope approximately 40% in one synthesis | HP:0002321 Vertigo; HP:0001279 Syncope |
| Orthostatic hypotension | From volume contraction and receptor physiology; approximately 12% | HP:0001278 Orthostatic hypotension |
| Anxiety/tremor/pallor | Episodic sympathetic symptoms; anxiety approximately 19% in one synthesis | HP:0000739 Anxiety; HP:0001337 Tremor; HP:0000980 Pallor |
| Weight loss | Variable; approximately 30% | HP:0001824 Weight loss |
| Hyperglycemia/diabetes | Catecholamine-mediated inhibition of insulin secretion and altered glucose handling | HP:0003074 Hyperglycemia; HP:0000819 Diabetes mellitus |
| Tumor mass effects | Head-and-neck PGL: pulsatile mass, tinnitus, dysphagia, dysphonia or cranial-nerve deficits; abdominal tumors: pain/fullness | HP:0000360 Tinnitus; HP:0002015 Dysphagia; HP:0001618 Dysphonia |
| Laboratory abnormalities | Elevated plasma free or urinary fractionated metanephrines; dopamine-lineage tumors may elevate 3-methoxytyramine | HP:0500114 Elevated circulating catecholamine level |

These frequencies are heterogeneous across referral populations and genotypes and should not be interpreted as universal penetrance estimates. Cluster-1 tumors tend to be noradrenergic/dopaminergic and may produce sustained hypertension; cluster-2 adrenal tumors more often produce epinephrine and paroxysmal attacks. Nonsecretory head-and-neck PGLs can remain clinically silent until a mass or cranial-nerve deficit develops. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, t.2024pheochromocytomaanupdated pages 6-7, t.2024pheochromocytomaanupdated pages 3-6)

**Quality of life:** attacks restrict activity, sleep, driving, employment, and social participation; chronic uncertainty, hereditary risk, repeated imaging, cranial-nerve morbidity, pain, fatigue, and treatment toxicities further impair well-being. Robust genotype-stratified EQ-5D/SF-36 estimates remain limited in the retrieved literature.

## 4. Genetic and molecular information

### Molecular classes and causal chain

1. **Cluster 1A—TCA-cycle/SDH pseudohypoxia:** biallelic loss of SDHx, FH, MDH2, DLST, or related metabolism genes → succinate/fumarate accumulation → inhibition of α-ketoglutarate-dependent dioxygenases → HIF stabilization plus DNA/histone hypermethylation (CIMP) → angiogenesis, altered differentiation, invasion, and predominantly noradrenergic/dopaminergic secretion. SDHB tumors are particularly enriched for metastatic behavior. Suggested GO terms: tricarboxylic-acid cycle (GO:0006099), mitochondrial electron transport (GO:0006121), response to hypoxia (GO:0001666), DNA methylation (GO:0006306), angiogenesis (GO:0001525). (cascon2023geneticbasesof pages 2-4, cascon2023geneticbasesof pages 4-5, t.2024pheochromocytomaanupdated pages 3-6)
2. **Cluster 1B—VHL/EPAS1 pseudohypoxia:** impaired VHL-mediated HIF degradation or activating EPAS1/HIF-2α alteration → constitutive hypoxia transcription → vascular/metabolic tumor program. EPAS1 alterations can be postzygotic mosaic and associated with polycythemia and somatostatinoma. (cascon2023geneticbasesof pages 6-8, t.2024pheochromocytomaanupdated pages 3-6)
3. **Cluster 2—kinase signaling:** RET gain of function or loss of NF1, TMEM127, MAX and related regulators → RAS–MAPK, PI3K–AKT–mTOR, receptor-tyrosine-kinase, MYC/MAX, and translational activation → proliferation and an adrenal/adrenergic phenotype. Suggested GO: MAPK cascade (GO:0000165), PI3K signaling (GO:0014065), TOR signaling (GO:0031929), cell proliferation (GO:0008283). (cascon2023geneticbasesof pages 2-4, cascon2023geneticbasesof pages 5-6)
4. **Cluster 3—WNT altered:** somatic **MAML3–UBTF** fusions or **CSDE1** alterations → WNT/β-catenin and developmental transcriptional dysregulation → proliferation, angiogenesis, and invasion. MAML3 rearrangements represented 5–7% in one synthesis; 37.5% of fusion-positive tumors developed metastases in the cited series. (cascon2023geneticbasesof pages 1-2, cascon2023geneticbasesof pages 6-8)

### Variant interpretation

Pathogenic alterations include missense, nonsense, frameshift, splice, copy-number, deletion, loss-of-heterozygosity, fusion, promoter/epigenetic, and postzygotic mosaic events. Tumor-suppressor genes generally operate through loss of function and a somatic second hit; RET and EPAS1 commonly act through gain of function. Population frequency alone is insufficient, especially for low-penetrance SDHA variants. VUS must not direct predictive testing or irreversible management. Tumor LOH, metabolomics, and IHC—loss of SDHB/SDHA/MAX or positive 2-succinocysteine in FH-deficient disease—can supply functional evidence. (cascon2023geneticbasesof pages 6-8, cascon2023geneticbasesof pages 4-5)

### Penetrance and genotype–phenotype examples

* **SDHD:** autosomal dominant with parent-of-origin effect, usually disease after paternal transmission; reported penetrance 86% by age 50; predominantly head-and-neck PGL.
* **SDHB:** autosomal dominant, incomplete age-dependent penetrance—approximately 30% by age 80 in one synthesis; often a solitary thoracoabdominal PGL without family history; substantial metastatic concern.
* **SDHA:** low penetrance, approximately 10% by age 70; many probands appear sporadic.
* **VHL:** approximately 20% develop PPGL; 43–45% multifocal/bilateral, <5% metastatic, median diagnosis around 29 years.
* **RET/MEN2:** approximately 50% lifetime PCC risk; 50–80% bilateral; metastatic disease uncommon.
* **NF1:** clinically recognized PPGL in approximately 0.1–5.7%, higher in autopsy series; usually unilateral adrenal tumors.
* **MAX:** preferential paternal transmission has been reported. A 2024 aggregation of 109 carriers found 101 PCC cases, 59 bilateral tumors, 18.8% metastasis, and mean diagnosis age 32.8 years. (cascon2023geneticbasesof pages 4-5, cascon2023geneticbasesof pages 5-6)

No repeat expansion is implicated. Routine karyotyping and FISH are not first-line tests; chromosomal microarray may detect large deletions but is less efficient than a sequencing panel that includes deletion/duplication analysis. Mitochondrial **nuclear genes** are central, but mitochondrial-DNA testing is not routine.

### Recent single-cell and multi-omics research

A 2024 single-cell preprint analyzed 133,894 cells from 16 tissues in five PCC patients and proposed metabolism-type tumors marked by **NDUFA4L2/COX4I2** and kinase-type tumors marked by **RET/PNMT**, with distinct FGF, annexin, inflammatory, HLA-I, and T-cell microenvironments. This is hypothesis-generating because of the very small patient sample and preprint status. A separate 2024 preprint integrating seven assays in 94 SDHB-deficient tumors from 79 patients associated **TERT/ATRX** alterations with metastasis and identified MGMT overexpression and mismatch-repair deficiency as possible alkylator-resistance mechanisms. (OpenTargets Search: pheochromocytoma,paraganglioma)

A concise quote from the 2023 genetics review captures the field: **“there are currently more than 20 driver genes implicated in either the hereditary or the sporadic nature of the disease.”** It further reports that genetic diagnosis is achieved in approximately 75–80%. [Published April 2023; DOI](https://doi.org/10.1530/jme-22-0167). (cascon2023geneticbasesof pages 1-2)

## 5. Environmental information

There is no established infectious etiology and no evidence supporting vaccination, antimicrobial prophylaxis, toxin avoidance, or a specific diet as PPGL prevention. Exercise, caffeine, nicotine, sympathomimetics, stress, anesthesia, tumor manipulation, and selected drugs can **trigger symptoms or interfere with biochemical testing**, but are not proven tumor initiators. Pregnancy is a clinically important physiologic context because catecholamine excess threatens both mother and fetus; early recognition and alpha blockade improve outcomes. (t.2024pheochromocytomaanupdated pages 6-7, t.2024pheochromocytomaanupdated pages 3-6)

## 6. Pathophysiology

The clinical causal chain is:

**driver alteration/second hit → chromaffin or paraganglial-cell transformation → cluster-specific metabolic or kinase program → tumor growth ± catecholamine synthesis → α-adrenergic vasoconstriction, β-adrenergic chronotropy/inotropy, volume contraction, insulin suppression and lipolysis → hypertension, headache, sweating, palpitations, arrhythmia, cardiomyopathy, hyperglycemia and crisis.** Chronic or extreme catecholamine exposure can produce myocarditis/cardiomyopathy, stroke, pulmonary edema, intestinal ischemia/ileus, and acute kidney injury. (t.2024pheochromocytomaanupdated pages 6-7, t.2024pheochromocytomaanupdated pages 3-6)

Relevant cells include adrenal chromaffin cells (**CL:0000166**), sympathetic neurons (**CL:0000095**), sustentacular cells, endothelial cells (**CL:0000115**), fibroblasts (**CL:0000057**), macrophages (**CL:0000235**), and lymphocytes. Relevant compartments are mitochondrion (**GO:0005739**), mitochondrial respiratory-chain complex II (**GO:0005749**), nucleus (**GO:0005634**), and cytosol (**GO:0005829**). Immune-checkpoint therapy has shown limited activity to date; low CD8 infiltration and genotype-dependent antigen-presentation programs may contribute, but the immune landscape remains investigational.

## 7. Anatomical structures affected

Primary sites are adrenal medulla (**UBERON:0001235**), sympathetic chain/paraganglia, organ of Zuckerkandl, retroperitoneum, mediastinum, urinary bladder, pelvis, carotid body, vagal body, jugulotympanic region, and skull base. Sympathetic tumors are generally secretory; parasympathetic head-and-neck tumors are often nonsecretory. Hereditary disease is more often bilateral or multifocal. (t.2024pheochromocytomaanupdated pages 1-2, cascon2023geneticbasesof pages 2-4)

Secondary injury involves cardiovascular, cerebrovascular, renal, pulmonary, gastrointestinal, endocrine/metabolic, and peripheral/cranial nervous systems. Metastatic targets are especially lymph node, bone, liver, and lung. In an aggregation of 107 SDHA-associated cases, tumors were head-and-neck in 46% and abdominal in 43%; among metastatic cases, bone and lymph nodes were involved in 82% and 71%, respectively. (t.2024pheochromocytomaanupdated pages 1-2)

## 8. Temporal development

Most sporadic diagnoses occur at age 30–50, with similar sex distribution. Pediatric PPGL represents approximately 10–20% of all PPGL, has annual incidence around 0.5–2 per million children, and presents at median age 11–15. Childhood disease is hereditary in 70–80%. (t.2024pheochromocytomaanupdated pages 1-2, casey2024internationalconsensusstatement pages 1-2)

The course ranges from an incidental stable mass to episodic catecholamine attacks, acute crisis, slowly progressive multifocal disease, or aggressive metastasis. Recurrence/metastasis can emerge decades after apparently complete resection; therefore “five-year cure” is unsafe for high-risk genotypes. Approximately half of treatment-naïve metastatic pediatric patients may remain stable at one year, illustrating that immediate systemic treatment is not obligatory for every asymptomatic patient. (casey2024internationalconsensusstatement pages 11-13)

## 9. Inheritance and population epidemiology

PPGL is rare; precise incidence varies with case ascertainment and incidental imaging. It accounts for roughly 0.1% of hypertension in the 2024 synthesis. About 35–45% harbor a germline pathogenic variant, including 10–12% of apparently sporadic presentations. The usual pattern is autosomal dominant with incomplete, age-dependent, gene-specific penetrance; SDHD, SDHAF2, and sometimes MAX show parent-of-origin effects. De novo and postzygotic mosaic disease occur, notably in VHL, EPAS1, H3-3A, and NF1. (t.2024pheochromocytomaanupdated pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, cascon2023geneticbasesof pages 6-8)

No consistent overall sex bias is established. Founder variants exist in particular populations, but population-specific carrier frequency cannot be safely inferred from unselected gnomAD frequency because penetrance differs sharply by gene and variant. Consanguinity is not a major general risk factor for these predominantly dominant syndromes.

## 10. Diagnostics

### Biochemistry

First-line testing is **plasma free metanephrines** or **24-hour urinary fractionated metanephrines**, preferably measured by LC–MS/MS. Plasma sampling should occur after at least 20–30 minutes supine rest. A 2024 synthesis reported plasma sensitivity 96% and specificity 85%, and urinary sensitivity 87.5% and specificity 99.7%, although performance varies by assay and referral setting. Plasma 3-methoxytyramine improves detection of dopamine-producing and SDHx-related disease. Exercise, acute illness, stress, posture, tricyclics, MAO inhibitors, sympathomimetics, selected antipsychotics, and analytical interference can cause false positives. Borderline normetanephrine elevation may be evaluated with clonidine suppression after correcting confounders. (casey2020geneticstratificationof pages 4-5, t.2024pheochromocytomaanupdated pages 6-7, t.2024pheochromocytomaanupdated pages 3-6)

### Localization and staging

After biochemical confirmation, contrast CT of abdomen/pelvis is a usual first localization study; MRI is preferred in children, pregnancy, head-and-neck disease, and repeated hereditary surveillance. One review reported CT sensitivity of 88% and 90–95% localization accuracy for tumors >1.3 cm. (t.2024pheochromocytomaanupdated pages 6-7)

Functional imaging should be selected by genotype and therapeutic question:

* **^68Ga-DOTATATE/DOTA-SSA PET/CT:** favored for SDHx, multifocal, metastatic, and head-and-neck disease; pooled detection approximately 93%.
* **^18F-FDOPA PET/CT:** strong performance in VHL and cluster-2 adrenal disease; detection about 80% in one synthesis.
* **^18F-FDG PET/CT:** useful for aggressive, dedifferentiated, and SDHB-associated disease; reported detection about 74%.
* **^123I-MIBG:** principally to establish eligibility for ^131I-MIBG therapy; sensitivity 50–75% overall and <50% in SDHB-associated disease. (giacche2024pheochromocytoma–paragangliomasyndromea pages 10-12, t.2024pheochromocytomaanupdated pages 7-8, t.2024pheochromocytomaanupdated pages 8-9)

### Pathology and genetics

Histology typically shows nests/trabeculae (“zellballen”) of granular neuroendocrine cells with sustentacular cells. Useful markers include chromogranin A, synaptophysin, INSM1, GATA3, tyrosine hydroxylase, and sustentacular S100/SOX10. Cytokeratin is usually absent or focal. SDHB loss screens for SDH deficiency; combined SDHA loss points toward SDHA. FH/2SC and MAX staining can guide genotype. PASS and GAPP provide risk stratification but cannot prove benignity or reliably predict an individual outcome. (casey2020geneticstratificationof pages 4-5, t.2024pheochromocytomaanupdated pages 7-8, t.2024pheochromocytomaanupdated pages 3-6)

**All patients should be offered pre-test counseling and a germline multigene NGS panel** with deletion/duplication detection. A practical panel includes SDHA/B/C/D, SDHAF2, VHL, RET, NF1, TMEM127, MAX, FH, MDH2, SLC25A11, DLST and other validated laboratory genes. If germline testing is negative, paired tumor-normal sequencing can identify somatic drivers and mosaicism. Combined analysis detects a driver in approximately 75–80%. VUS must not trigger cascade testing. (cascon2023geneticbasesof pages 1-2, casey2020geneticstratificationof pages 4-5, cascon2023geneticbasesof pages 6-8)

### Differential diagnosis

Differentials include essential hypertension, panic disorder, hyperthyroidism, hypoglycemia, carcinoid syndrome, mast-cell activation, obstructive sleep apnea, medication/drug withdrawal, baroreflex failure, pseudopheochromocytoma, neuroblastoma, adrenal cortical adenoma/carcinoma, renal-cell carcinoma, schwannoma, and other neuroendocrine tumors. Biochemical metanephrine patterns, imaging location, and pathology resolve most cases.

## 11. Outcome and prognosis

Localized completely resected disease often has excellent long-term survival, but recurrence remains possible. Metastasis occurs in a minority—approximately 10–30% across heterogeneous series—and is more likely with SDHB/FH biology, extra-adrenal primary, larger tumor, dopamine/3-methoxytyramine production, high burden, and TERT/ATRX/MAML3 alterations. No single histologic or molecular marker is sufficiently accurate; expert reviews favor composite clinical, biochemical, imaging, pathological, and genomic assessment. (t.2024pheochromocytomaanupdated pages 1-2, giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6, casey2020geneticstratificationof pages 4-5)

Morbidity reflects catecholamine-mediated cardiovascular injury, treatment toxicity, cranial-nerve deficits after head-and-neck intervention, metastatic pain/fracture, renal dysfunction, and lifelong surveillance burden. The precise median survival of metastatic disease is highly variable and should not be represented by one pooled number. In the pivotal high-specific-activity ^131I-MIBG cohort, median overall survival was 36.7 months, but that selected treatment population is not equivalent to all metastatic PPGL. (t.2024pheochromocytomaanupdated pages 7-8)

## 12. Treatment

### Localized disease

Surgical excision is the only established curative treatment. Minimally invasive adrenalectomy is generally used for localized PCC under approximately 5–6 cm; open resection is favored for invasion, large/fragile tumors, selected SDHB-related PGLs, or when en-bloc resection and nodal dissection are required. Cortical-sparing adrenalectomy can preserve steroid function in selected bilateral hereditary PCC. Head-and-neck management may use observation, surgery, or radiotherapy according to growth, symptoms, cranial-nerve risk, age, and genotype. (t.2024pheochromocytomaanupdated pages 7-8)

Secretory tumors require preoperative **alpha blockade first**—phenoxybenzamine or a selective α1 antagonist such as doxazosin—plus salt/fluid repletion. A beta blocker may be added only after adequate alpha blockade for tachycardia; unopposed beta blockade can precipitate crisis. One guideline-based regimen starts phenoxybenzamine 10 mg twice daily, titrating up to 1 mg/kg/day, with beta blockade added 3–4 days later. Suggested NCIt concepts include adrenalectomy, tumor resection, phenoxybenzamine, doxazosin, and beta-adrenergic blockade. (t.2024pheochromocytomaanupdated pages 7-8)

### Metastatic/unresectable disease

* **Observation/local control:** appropriate for asymptomatic, low-volume, stable disease. Surgery, ablation, embolization, external-beam or stereotactic radiotherapy, and cementoplasty can address oligometastases, pain, impending fracture, compression, or hormone burden.
* **High-specific-activity ^131I-MIBG:** FDA-approved in 2018 for MIBG-avid advanced PPGL. In 68 treated patients, 25% had durable antihypertensive-medication reduction, 92% had partial response or stable disease within 12 months, and median OS was 36.7 months; nausea, fatigue, and myelosuppression were common. (t.2024pheochromocytomaanupdated pages 7-8)
* **^177Lu-DOTATATE PRRT:** used for strongly somatostatin-receptor-positive disease; current PPGL evidence is largely retrospective, with prospective phase II evaluation ongoing. (taieb2023clinicalconsensusguideline pages 19-21, t.2024pheochromocytomaanupdated pages 8-9)
* **CVD chemotherapy:** cyclophosphamide–vincristine–dacarbazine for rapidly progressive/high-burden disease; aggregated response approximately 37%, with complete responses uncommon.
* **Temozolomide:** oral alkylator, particularly rational in SDHB-deficient/MGMT-silenced disease; acquired MGMT expression or mismatch-repair defects may cause resistance. (t.2024pheochromocytomaanupdated pages 8-9)
* **Sunitinib:** FIRSTMAPP demonstrated 12-month progression-free survival in 36% versus 19% with placebo; grade 3–4 toxicities included asthenia and hypertension.
* **Cabozantinib:** Natalie phase II trial objective response 25% (4/16 evaluable patients).
* **Axitinib:** phase II partial response approximately 36% in the cited synthesis.
* **Immunotherapy:** not standard; response evidence remains limited. (t.2024pheochromocytomaanupdated pages 8-9)

Pharmacogenomic treatment selection currently reflects **tumor biology** more than host drug-metabolism genotype: MIBG/SLC6A2 avidity, SSTR expression, SDHB/MGMT status, VEGF-driven pseudohypoxia, and VHL/HIF-2α biology.

### Trials and recent development

Retrieved ClinicalTrials.gov examples include **NCT03206060**, phase II ^177Lu-DOTATATE, recruiting, target n=130; **NCT04394858**, temozolomide±olaparib, active/not recruiting, n=46; **NCT05636540**, ^18F-fluorThanatrace PARP-1 PET, recruiting, n=30; **NCT03946527**, lanreotide, active/not recruiting, n=10; and **NCT06429397**, anlotinib plus benmelstobart, phase II, not yet recruiting, n=22. Trial status changes over time and should be rechecked before clinical use.

## 13. Prevention

There is no vaccine or proven population-level primary prevention. The effective prevention strategy is **secondary and tertiary prevention**:

1. universal germline testing of affected patients;
2. cascade testing of relatives only for pathogenic/likely pathogenic actionable variants;
3. lifelong gene-specific biochemical and MRI surveillance;
4. recognition and treatment before pregnancy or elective surgery;
5. perioperative alpha blockade to prevent crisis;
6. prompt management of hypertension, arrhythmia, cardiomyopathy, diabetes, and skeletal metastases. (casey2024internationalconsensusstatement pages 11-13, taieb2023clinicalconsensusguideline pages 19-21, t.2024pheochromocytomaanupdated pages 7-8)

For SDHD carriers, expert consensus recommends annual plasma metanephrines and whole-body MRI every 2–3 years; other genes use age- and risk-adapted intervals. Reproductive counseling may include prenatal or preimplantation genetic testing after a familial pathogenic variant is established. Population newborn screening is not indicated.

## 14. Other species and natural disease

Naturally occurring PCC/PGL occurs in companion and laboratory animals, especially dogs, cattle, and rats, but the retrieved evidence did not support reliable breed-specific incidence or VBO mappings. These tumors are not infectious or zoonotic and have no cross-species transmission. Orthologues of SDHx, VHL, RET, NF1, TMEM127, MAX, FH, and EPAS1 are broadly conserved, making comparative pathology biologically relevant. Veterinary PCC commonly resembles human chromaffin neuroendocrine morphology and catecholamine biology, but species-specific natural history limits direct therapeutic extrapolation.

Suggested taxonomy identifiers are **Homo sapiens NCBI:9606**, **Mus musculus NCBI:10090**, **Rattus norvegicus NCBI:10116**, **Canis lupus familiaris NCBI:9615**, and **Bos taurus NCBI:9913**.

## 15. Model organisms and experimental systems

Common models include rat PC12 pheochromocytoma cells, mouse MPC cells and metastatic derivatives, human PPGL primary cultures, patient-derived xenografts, organoids/spheroids, SDHB/SDHD knockdown systems, and genetically engineered mice affecting Nf1, Ret, Vhl, Sdh genes, Hif2a/Epas1, or Myc pathways. Three-dimensional cultures better model gradients, extracellular matrix, and drug penetration than conventional monolayers. (OpenTargets Search: pheochromocytoma,paraganglioma)

Major limitations are difficulty maintaining differentiated human chromaffin cells, incomplete spontaneous metastasis, species-specific catecholamine biology, and failure of many single-gene mouse models to reproduce the complete human syndrome. Current best practice uses complementary systems: human tumor multi-omics for discovery; isogenic cell models for mechanism; 3-D cultures for microenvironment/drug screening; and xenograft or engineered-animal models for pharmacology and dissemination.

## Evidence appraisal and authoritative interpretation

The 2024 WHO-oriented molecular review emphasizes that all PPGLs are neoplasms with variable metastatic potential and that **“no single biomarker alone can reliably predict metastatic risk.”** [Published October 2024; DOI](https://doi.org/10.1007/s12022-024-09830-3). (t.2024pheochromocytomaanupdated pages 1-2)

The 2024 pediatric consensus—developed by 43 international experts—places germline testing, multidisciplinary care, genotype-adapted imaging, and lifelong surveillance at the center of management. [Published September 2024; DOI](https://doi.org/10.1038/s41574-024-01024-5). (casey2024internationalconsensusstatement pages 1-2, casey2024internationalconsensusstatement pages 11-13)

The clearest 2023–2024 advances are: broader universal paired germline/tumor sequencing; genotype-specific PET selection; prospective evidence for antiangiogenic TKIs; expansion of SSTR-directed theranostics; HIF-2α and DNA-repair-directed trials; and single-cell/multi-omics identification of microenvironment and resistance states. However, most treatment studies remain small because PPGL is rare, and several advanced-omics results are still preprints. (cascon2023geneticbasesof pages 1-2, t.2024pheochromocytomaanupdated pages 8-9)

**Principal sources:** Cascón et al., *Journal of Molecular Endocrinology*, April 2023, [DOI 10.1530/JME-22-0167](https://doi.org/10.1530/jme-22-0167); Taïeb et al., *Lancet Diabetes & Endocrinology*, May 2023, [DOI 10.1016/S2213-8587(23)00038-4](https://doi.org/10.1016/S2213-8587(23)00038-4); Casey et al., *Nature Reviews Endocrinology*, September 2024, [DOI 10.1038/s41574-024-01024-5](https://doi.org/10.1038/s41574-024-01024-5); Giacché et al., October 2024, [DOI 10.3390/biomedicines12102385](https://doi.org/10.3390/biomedicines12102385); Saavedra et al., *Frontiers in Endocrinology*, December 13, 2024, [DOI 10.3389/fendo.2024.1433582](https://doi.org/10.3389/fendo.2024.1433582).

References

1. (t.2024pheochromocytomaanupdated pages 1-2): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 47 citations.

2. (casey2024internationalconsensusstatement pages 1-2): Ruth T Casey, Emile Hendriks, Cheri Deal, Steven G Waguespack, Verena Wiegering, Antje Redlich, Scott Akker, Rathi Prasad, Martin Fassnacht, Roderick Clifton-Bligh, Laurence Amar, Stefan Bornstein, Letizia Canu, Evangelia Charmandari, Alexandra Chrisoulidou, Maria Currás Freixes, Ronald De Krijger, Luisa De Sanctis, Antonio Fojo, Amol J Ghia, Angela Huebner, Vasilis Kosmoliaptsis, Michaela Kuhlen, Marco Raffaelli, Charlotte Lussey-Lepoutre, Stephen D Marks, Naris Nilubol, Mirko Parasiliti-Caprino, Henri HJLM Timmers, Anna Lena Zietlow, Mercedes Robledo, Anne-Paule Gimenez-Roqueplo, Ashley B Grossman, David Taïeb, Eamonn R Maher, Jacques WM Lenders, Graeme Eisenhofer, Camilo Jimenez, Karel Pacak, and Christina Pamporaki. International consensus statement on the diagnosis and management of phaeochromocytoma and paraganglioma in children and adolescents. JournalArticle, Sep 2024. URL: https://doi.org/10.17863/cam.111911, doi:10.17863/cam.111911. This article has 69 citations.

3. (cascon2023geneticbasesof pages 1-2): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 92 citations and is from a peer-reviewed journal.

4. (t.2024pheochromocytomaanupdated pages 3-6): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 47 citations.

5. (t.2024pheochromocytomaanupdated pages 6-7): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 47 citations.

6. (casey2020geneticstratificationof pages 4-5): Ruth Casey, Hartmut PH Neumann, and Eamonn R Maher. Genetic stratification of inherited and sporadic phaeochromocytoma and paraganglioma: implications for precision medicine. Human molecular genetics, Oct 2020. URL: https://doi.org/10.1093/hmg/ddaa201, doi:10.1093/hmg/ddaa201. This article has 38 citations and is from a domain leading peer-reviewed journal.

7. (t.2024pheochromocytomaanupdated pages 7-8): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 47 citations.

8. (giacche2024pheochromocytoma–paragangliomasyndromea pages 10-12): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 10 citations.

9. (cascon2023geneticbasesof pages 6-8): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 92 citations and is from a peer-reviewed journal.

10. (cascon2023geneticbasesof pages 4-5): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 92 citations and is from a peer-reviewed journal.

11. (cascon2023geneticbasesof pages 2-4): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 92 citations and is from a peer-reviewed journal.

12. (cascon2023geneticbasesof pages 5-6): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 92 citations and is from a peer-reviewed journal.

13. (OpenTargets Search: pheochromocytoma,paraganglioma): Open Targets Query (pheochromocytoma,paraganglioma, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

14. (giacche2024pheochromocytoma–paragangliomasyndromea pages 5-6): Mara Giacché, Maria Chiara Tacchetti, Claudia Agabiti-Rosei, Francesco Torlone, Francesco Bandera, Claudia Izzi, and Enrico Agabiti-Rosei. Pheochromocytoma–paraganglioma syndrome: a multiform disease with different genotype and phenotype features. Oct 2024. URL: https://doi.org/10.3390/biomedicines12102385, doi:10.3390/biomedicines12102385. This article has 10 citations.

15. (t.2024pheochromocytomaanupdated pages 8-9): J. S. Saavedra T., Humberto Alejandro Nati-Castillo, L. A. Valderrama Cometa, Wilfredo A. Rivera-Martínez, Josué Asprilla, C. M. Castaño-Giraldo, Leonardo Sánchez S., Mishell Heredia-Espín, Marlon Arias-Intriago, and Juan S. Izquierdo-Condoy. Pheochromocytoma: an updated scoping review from clinical presentation to management and treatment. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1433582, doi:10.3389/fendo.2024.1433582. This article has 47 citations.

16. (taieb2023clinicalconsensusguideline pages 19-21): David Taïeb, George B Wanna, Maleeha Ahmad, Charlotte Lussey-Lepoutre, Nancy D Perrier, Svenja Nölting, Laurence Amar, Henri J L M Timmers, Zachary G Schwam, Anthony L Estrera, Michael Lim, Erqi Liu Pollom, Lucas Vitzthum, Isabelle Bourdeau, Ruth T Casey, Frédéric Castinetti, Roderick Clifton-Bligh, Eleonora P M Corssmit, Ronald R de Krijger, Jaydira Del Rivero, Graeme Eisenhofer, Hans K Ghayee, Anne-Paule Gimenez-Roqueplo, Ashley Grossman, Alessio Imperiale, Jeroen C Jansen, Abhishek Jha, Michiel N Kerstens, Henricus P M Kunst, James K Liu, Eamonn R Maher, Daniele Marchioni, Leilani B Mercado-Asis, Ozgur Mete, Mitsuhide Naruse, Naris Nilubol, Neeta Pandit-Taskar, Frédéric Sebag, Akiyo Tanabe, Jiri Widimsky, Leah Meuter, Jacques W M Lenders, and Karel Pacak. Clinical consensus guideline on the management of phaeochromocytoma and paraganglioma in patients harbouring germline sdhd pathogenic variants. May 2023. URL: https://doi.org/10.1016/s2213-8587(23)00038-4, doi:10.1016/s2213-8587(23)00038-4. This article has 113 citations and is from a highest quality peer-reviewed journal.

17. (casey2024internationalconsensusstatement pages 11-13): Ruth T Casey, Emile Hendriks, Cheri Deal, Steven G Waguespack, Verena Wiegering, Antje Redlich, Scott Akker, Rathi Prasad, Martin Fassnacht, Roderick Clifton-Bligh, Laurence Amar, Stefan Bornstein, Letizia Canu, Evangelia Charmandari, Alexandra Chrisoulidou, Maria Currás Freixes, Ronald De Krijger, Luisa De Sanctis, Antonio Fojo, Amol J Ghia, Angela Huebner, Vasilis Kosmoliaptsis, Michaela Kuhlen, Marco Raffaelli, Charlotte Lussey-Lepoutre, Stephen D Marks, Naris Nilubol, Mirko Parasiliti-Caprino, Henri HJLM Timmers, Anna Lena Zietlow, Mercedes Robledo, Anne-Paule Gimenez-Roqueplo, Ashley B Grossman, David Taïeb, Eamonn R Maher, Jacques WM Lenders, Graeme Eisenhofer, Camilo Jimenez, Karel Pacak, and Christina Pamporaki. International consensus statement on the diagnosis and management of phaeochromocytoma and paraganglioma in children and adolescents. JournalArticle, Sep 2024. URL: https://doi.org/10.17863/cam.111911, doi:10.17863/cam.111911. This article has 69 citations.

## Artifacts

- [Edison artifact artifact-00](Pheochromocytoma_Paraganglioma-deep-research-falcon_artifacts/artifact-00.md)