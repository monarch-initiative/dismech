---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T22:48:23.909834'
end_time: '2026-07-31T22:59:30.096907'
duration_seconds: 666.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cerebral Palsy
  mondo_id: ''
  category: Complex
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
  path: Cerebral_Palsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cerebral Palsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cerebral Palsy** covering all of the
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
- **Disease Name:** Cerebral Palsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cerebral Palsy** covering all of the
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


# Cerebral Palsy: Disease-Characteristics Research Report

## Executive summary

Cerebral palsy (CP) is not one etiologic disease but a clinically defined, heterogeneous group of permanent movement and posture disorders caused by a non-progressive disturbance of the developing fetal or infant brain. The original lesion does not progress, although musculoskeletal complications, pain, fatigue, and functional limitations may change across life. Current evidence rejects the older assumption that CP is principally synonymous with intrapartum asphyxia: prematurity, congenital maldevelopment, stroke, infection/inflammation, placental disease, neonatal injury, and an increasingly important genomic component all contribute. A 2024 review reports prevalence of approximately 1.6 per 1,000 live births in high-income countries versus 3.3 per 1,000 in low- and middle-income countries. Common associated impairments include cognitive impairment (~50%), epilepsy (~33%), language impairment (~33%), and inability to walk independently (~40%). (xu2024geneticpathwaysin pages 1-1)

The most important recent development is genomic reclassification. A 2024 *Nature Genetics* study of 327 parent-child trios identified pathogenic/likely pathogenic variants in 37 children (11%) and variants of uncertain significance in 58 (18%). A separate meta-analytic estimate cited in a 2024 *eBioMedicine* review was 23% for single-nucleotide variants and 5% for copy-number variants. Thus, CP remains a clinical syndrome, but a molecular diagnosis can refine recurrence risk, prognosis, surveillance, and occasionally treatment. (fehlings2024comprehensivewholegenomesequence pages 26-28, fehlings2024comprehensivewholegenomesequence pages 17-19, lewis2024potentialclinicalapplications pages 1-2)

The following compact knowledge-base summary precedes the detailed report.

| domain | high-confidence finding | quantitative data/example | ontology suggestions |
|---|---|---|---|
| Definition / IDs | Cerebral palsy (CP) is a group of permanent disorders of movement and posture due to a non-progressive disturbance/lesion of the developing fetal or infant brain; disease-level knowledge here is derived primarily from aggregated reviews, registries, and cohort studies rather than individual EHR alone. MONDO for cerebral palsy is available. (xu2024geneticpathwaysin pages 1-1, lewis2024potentialclinicalapplications pages 1-2, OpenTargets Search: cerebral palsy) | MONDO: `MONDO:0006497`; MeSH term present in ClinicalTrials browse: `D002547 Cerebral Palsy`. | MONDO:0006497; MeSH:D002547; HPO: HP:0100021 *Cerebral palsy* |
| Classification | Standard clinical subtype classification includes spastic, dyskinetic, ataxic, and hypotonic CP; function is commonly staged with GMFCS, MACS, CFCS, and EDACS. (xu2024geneticpathwaysin pages 2-3, novak2020stateofthe pages 4-6) | Slovenian pediatric cohort: spastic 85%, dyskinetic 13%, ataxic 2%. Functional systems: GMFCS I-V, MACS I-V. (silan2025unravellinggeneticetiology pages 1-2, novak2020stateofthe pages 4-6) | HPO: HP:0001257 *Spasticity*; HP:0001270 *Motor delay*; HP:0100022 *Dyskinetic cerebral palsy*; HP:0001251 *Ataxia* |
| Core phenotypes | CP is fundamentally a motor syndrome, often accompanied by cognitive, epilepsy, language, and mobility impairments; severity and participation limits vary widely. (xu2024geneticpathwaysin pages 1-1, xu2024geneticpathwaysin pages 2-3) | Approximate comorbidity frequencies from 2024 review: cognitive impairment ~50%, epilepsy ~33%, language impairment ~33%, ~40% unable to walk independently. (xu2024geneticpathwaysin pages 1-1) | HPO: HP:0001257 *Spasticity*; HP:0001263 *Developmental regression* not typical; HP:0001249 *Intellectual disability*; HP:0001250 *Seizure*; HP:0000750 *Delayed speech and language development* |
| Epidemiology | CP remains the most common childhood physical disability, with lower rates in many high-income settings than historically, but higher burden in low-/middle-income settings. (xu2024geneticpathwaysin pages 1-1, novak2020stateofthe pages 4-6, tegegne2023determinantsofcerebral pages 1-2) | Prevalence estimates: ~1.4-1.6 per 1,000 live births in some high-income settings; ~3.3-3.4 per 1,000 in LMIC settings; global range 1.5 to >4 per 1,000. Preterm infants account for ~43% of cases. (xu2024geneticpathwaysin pages 1-1, novak2020stateofthe pages 4-6, tegegne2023determinantsofcerebral pages 1-2) | MONDO:0006497; NCIT:C7639 *Preterm Birth*; HPO: HP:0001622 *Premature birth* |
| Etiology / risk factors | CP is etiologically heterogeneous: prematurity/low birth weight, low Apgar, intrauterine infection, congenital brain malformations, PROM, placental abruption, maternal disease, neonatal hyperbilirubinemia, stroke, and hypoxic-ischemic injury all contribute. (tegegne2023determinantsofcerebral pages 1-2, collins2024theimportanceof pages 1-2, xu2024geneticpathwaysin pages 2-3) | Systematic review found 40 consistent determinants from 95 articles; 24 studies implicated prematurity/low weight and 15 implicated low Apgar. HIE in term infants occurs in ~1.5/1,000 births and is a leading cause of CP. (tegegne2023determinantsofcerebral pages 1-2, collins2024theimportanceof pages 1-2) | HPO: HP:0001518 *Small for gestational age*; HP:0003819 *Abnormality of the placenta*; UBERON: placenta / brain; GO: GO:0006954 *inflammatory response* |
| Protective / preventive factors | Established prevention is mainly perinatal/neonatal: antenatal magnesium sulfate, antenatal corticosteroids, prophylactic caffeine in preterm infants, and therapeutic hypothermia for moderate-severe HIE. These are established care, not experimental. (novak2020stateofthe pages 4-6, klobucka2026evidenceandpractice pages 4-5) | Reported effect sizes/examples: magnesium sulfate prevents ~30% of CP in very preterm infants; therapeutic hypothermia prevents ~15% of hypoxia-associated cases when used within 6 hours. (novak2020stateofthe pages 4-6) | NCIT: magnesium sulfate, corticosteroid, caffeine, hypothermia; CHEBI: magnesium sulfate, caffeine |
| Genetic architecture | CP includes a substantial monogenic/CNV component and should not be treated as exclusively acquired. Recurrent genes/pathways converge on thrombosis, angiogenesis, mitochondrial/oxidative phosphorylation, neuronal migration, and autophagy, with overlap with broader neurodevelopmental disorders. (xu2024geneticpathwaysin pages 1-1, lewis2024potentialclinicalapplications pages 1-2) | Meta-analytic estimates cited in 2024 review: SNV molecular diagnostic yield ~23%, CNV yield ~5%. >100 recurrent genes discussed. (lewis2024potentialclinicalapplications pages 1-2) | HGNC gene examples: ATL1, CTNNB1, SPAST, PROC, COL4A1, L1CAM, KIF1A; GO: neuronal migration, oxidative phosphorylation, autophagy |
| 2024 genomics development | Trio whole-genome sequencing has now provided large-scale direct evidence for CP genomic architecture. This is a key recent development. (fehlings2024comprehensivewholegenomesequence pages 26-28, fehlings2024comprehensivewholegenomesequence pages 17-19, fehlings2024comprehensivewholegenomesequence pages 21-24) | Nature Genetics 2024 cohort: 327 trios; pathogenic/likely pathogenic variants in 37/327 (11%), VUS in 58/327 (18%), no clinically relevant variant in 232/327 (71%); P/LP group had more cognitive impairment (49%) and brain maldevelopments (11%). (fehlings2024comprehensivewholegenomesequence pages 17-19, fehlings2024comprehensivewholegenomesequence pages 21-24) | HGNC: MT-TQ, MT-TS1, MT-ND5; GO: GO:0005739 *mitochondrion*; HPO: HP:0001250 *Seizure*; HP:0001249 *Intellectual disability* |
| Example implicated genes | Multiple cohorts identified plausible/definite CP-related variants, supporting clinical heterogeneity and genetic testing. (silan2025unravellinggeneticetiology pages 1-2, yigit2026unmaskinggeneticetiologies pages 1-2) | Slovenian cohort: 9/136 (6.6%) with ATL1, CTNNB1, DYRK1, KMT2A, PROC, SPAST, ZC4H2, ZSWIM6; 2026 integrative genomic cohort found P/LP variants in 24/66 (36.4%) with genes including SPAST, KIF1A, PLA2G6, CTNNB1, L1CAM, SYNGAP1. (silan2025unravellinggeneticetiology pages 1-2, yigit2026unmaskinggeneticetiologies pages 1-2) | HGNC: ATL1, CTNNB1, SPAST, KIF1A, PLA2G6, L1CAM, SYNGAP1 |
| MRI / anatomy | Brain MRI is abnormal in most children with CP and helps classify etiology/anatomy; white matter injury is the most frequent MRI pattern, but normal MRI does not exclude CP or genetic causes. (lewis2024potentialclinicalapplications pages 1-2, silan2025unravellinggeneticetiology pages 1-2) | MRI categories (SCPE framework): maldevelopments, predominant white matter injury, predominant gray matter injury, miscellaneous abnormalities, normal. In one cited study: maldevelopments ~11%, white matter injury 49%, gray matter injury 21%; MRI abnormal in >80% overall. Normal MRI occurred in 42% of spastic diplegic CP in one series; 3/9 genetically solved Slovenian cases had normal MRI. (lewis2024potentialclinicalapplications pages 1-2, silan2025unravellinggeneticetiology pages 1-2) | UBERON: brain, cerebral white matter, cerebral cortex, basal ganglion, thalamus, cerebellum; HPO: HP:0002500 *Abnormal cerebral white matter morphology* |
| Pathophysiology / mechanism | A common mechanistic chain in acquired CP is prenatal/perinatal hypoxia-ischemia ± inflammation: reduced oxygen/blood flow causes primary energy failure, ATP depletion, lactate accumulation, ion pump failure, calcium overload, oxidative stress, necrosis/apoptosis, then secondary inflammatory injury affecting selective neurons and oligodendrocyte-lineage cells. (collins2024theimportanceof pages 1-2, koehler2018perinatalhypoxicischemicbrain pages 1-2) | HIE severe mortality cited at 25-50%; one-third to one-half of cooled survivors still had persistent neurologic abnormalities or low IQ at 6-7 years in large-animal review discussion. White matter injury and progenitor oligodendrocyte vulnerability are emphasized in fetal sheep and piglet models. (collins2024theimportanceof pages 1-2, koehler2018perinatalhypoxicischemicbrain pages 1-2) | GO: GO:0006091 *generation of precursor metabolites and energy*; GO:0006979 *response to oxidative stress*; GO:0006954 *inflammatory response*; CL: oligodendrocyte precursor cell, microglial cell, neuron |
| Diagnosis | Early diagnosis is increasingly feasible using clinical neurodevelopmental tools plus MRI; at-risk infants can often be identified far earlier than the historic 2-year diagnosis window. (klobucka2026evidenceandpractice pages 4-5, lewis2024potentialclinicalapplications pages 1-2) | Hammersmith Infant Neurological Examination + brain MRI allows reliable diagnosis in at-risk infants at ~5 months corrected age; reviews note prediction by 6-12 months and sometimes as early as 3 months corrected age with GMA/HINE/MRI. (klobucka2026evidenceandpractice pages 4-5, lewis2024potentialclinicalapplications pages 1-2) | NCIT: Magnetic Resonance Imaging; HPO: abnormal general movements; clinical tools: GMA, HINE, GMFCS |
| Differential / genomic workflow | Genetic evaluation is especially warranted when imaging/history are atypical or insufficient, including normal MRI, no clear perinatal insult, severe phenotype, family history, or CP-like/progressive presentations. This is increasingly recommended clinical workflow rather than purely research. (silan2025unravellinggeneticetiology pages 1-2, lewis2024potentialclinicalapplications pages 1-2) | 2024 review: SNV yield ~23% and CNV yield ~5%; Slovenian cohort identified cases despite normal MRI or unremarkable history. Advanced genomic review argues for WES/WGS and other state-of-the-art genomic approaches to improve diagnosis. (lewis2024potentialclinicalapplications pages 1-2, silan2025unravellinggeneticetiology pages 1-2) | NCIT: Whole Exome Sequencing, Whole Genome Sequencing, Chromosomal Microarray Analysis |
| Established treatment: rehabilitation | Best-supported rehabilitation is early, active, task-specific, and goal-directed; technology can augment but not replace motor learning. NDT-Bobath is not superior to usual care. (novak2020stateofthe pages 13-14, klobucka2026evidenceandpractice pages 4-5, klobucka2026evidenceandpractice pages 12-13) | Traffic-light review covered 182 interventions and 398 outcomes; effective allied health examples include CIMT, bimanual training, treadmill/partial body-weight support training, strength training, goal-directed training, and home programs. (novak2020stateofthe pages 4-6, novak2020stateofthe pages 13-14) | NCIT: Physical Therapy, Occupational Therapy, Constraint-Induced Movement Therapy, Treadmill Training |
| Established treatment: pharmacologic / surgical | Established management for selected impairments includes botulinum toxin, intrathecal baclofen, selective dorsal rhizotomy, hip surveillance, scoliosis correction, and anticonvulsants, typically combined with rehabilitation. (novak2020stateofthe pages 13-14, klobucka2026evidenceandpractice pages 12-13) | Strong-evidence examples from systematic review: botulinum toxin, intrathecal baclofen, selective dorsal rhizotomy, anti-convulsants, dentistry, hip surveillance, scoliosis correction. (novak2020stateofthe pages 13-14) | NCIT: Botulinum Toxin, Baclofen, Selective Dorsal Rhizotomy, Hip Surveillance, Scoliosis Surgery |
| Unsupported / low-evidence care | Some commonly promoted interventions lack convincing benefit and should be distinguished from evidence-based care. (klobucka2026evidenceandpractice pages 12-13) | Examples flagged as lacking evidence in rehabilitation review: hyperbaric oxygen therapy, craniosacral manipulation, unstructured sensory integration, passive stretching without task-specific goals. (klobucka2026evidenceandpractice pages 12-13) | NCIT: Hyperbaric Oxygen Therapy; supportive note: low-evidence / not established |
| Prognosis | The brain lesion is non-progressive, but disability is lifelong and functional trajectories vary by subtype, GMFCS level, comorbidity burden, and response to therapy. Prognosis is influenced by prematurity, HIE severity, cognition, and associated impairments. (xu2024geneticpathwaysin pages 1-1, klobucka2026evidenceandpractice pages 4-5, collins2024theimportanceof pages 1-2) | Severe HIE mortality 25-50%; in a cohort of infants <25 weeks, males were more likely to develop CP and impaired cognition than females. Quality-of-life burden is substantial but precise modern disease-wide mortality/life expectancy estimates were not retrieved in this conversation. (collins2024theimportanceof pages 1-2) | HPO: HP:0001263 *Global developmental delay*; HP:0001249 *Intellectual disability*; ICF/GMFCS useful for prognosis |
| Current experimental / real-world trials | Ongoing interventional work includes neuromodulation, robotic exoskeleton gait therapy, biomarker-linked gait therapy, and stem-cell/conditioned-medium studies. These are experimental, not standard of care. (NCT06586437 chunk 1, NCT05158218 chunk 1, NCT04360395 chunk 1, NCT04314687 chunk 1) | Examples: NCT06586437 neuromodulation of cortex/spinal cord, randomized, double-masked, n=50; NCT05158218 robotic exoskeleton gait training vs physical therapy, randomized, n=64; NCT04360395 gait therapy with neurophysiology responder analysis, n=120; NCT04314687 allogeneic umbilical cord MSCs ± conditioned medium vs standard therapy, phase 1/2, n=78. (NCT06586437 chunk 1, NCT05158218 chunk 1, NCT04360395 chunk 1, NCT04314687 chunk 1) | NCIT: Transcutaneous Current Stimulation, Robotic Exoskeleton, Gait Therapy, Mesenchymal Stem Cell Therapy |
| Animal / translational models | CP has no single standard natural veterinary analogue; experimental models focus on hypoxia-ischemia, inflammation, hemorrhage, and prematurity-related injury. Large animals improve clinical translatability; rodent models remain useful mechanistically. (collins2024theimportanceof pages 1-2, koehler2018perinatalhypoxicischemicbrain pages 1-2) | Large-animal examples: fetal sheep for progenitor oligodendrocyte vulnerability and white matter injury; newborn piglets for term HIE systems injury; non-human primates for cortical/basal ganglia/thalamic injury patterns; maternal immune activation is an important added risk-factor model. Hypothermia success in human neonates was informed by animal work. (collins2024theimportanceof pages 1-2, koehler2018perinatalhypoxicischemicbrain pages 1-2) | NCBI Taxon examples: Mus musculus, Rattus norvegicus, Ovis aries, Sus scrofa, Macaca mulatta; GO/CL: oligodendrocyte precursor, microglia, neuron |


*Table: This compact table summarizes high-confidence, evidence-backed facts for a cerebral palsy knowledge-base entry, spanning definition, phenotypes, epidemiology, genetics, diagnosis, treatment, prognosis, and models. It distinguishes established care from experimental approaches and includes ontology suggestions for structured annotation.*

## 1. Disease information

### Definition and classification

The accepted construct is a group of permanent disorders of movement and posture causing activity limitation, attributable to non-progressive disturbances in the developing fetal or infant brain. “Permanent” describes the motor disorder; “non-progressive” describes the causal brain disturbance—not the person’s changing phenotype. CP may be spastic, dyskinetic, ataxic, hypotonic, or mixed and may be unilateral or bilateral. Function is classified separately with the five-level Gross Motor Function Classification System (GMFCS), Manual Ability Classification System (MACS), Communication Function Classification System (CFCS), and Eating and Drinking Ability Classification System (EDACS). (xu2024geneticpathwaysin pages 1-1, xu2024geneticpathwaysin pages 2-3)

**Identifiers and synonyms**

- **MONDO:** MONDO:0006497.
- **MeSH:** D002547, *Cerebral Palsy*.
- **ICD-10-CM:** G80.-; important descendants include G80.0 spastic quadriplegic CP, G80.1 spastic diplegic CP, G80.2 spastic hemiplegic CP, G80.3 dyskinetic CP, G80.4 ataxic CP, G80.8 other CP, and G80.9 unspecified CP.
- **ICD-11:** under cerebral palsy in developmental motor disorders; implementation-specific codes should be verified against the current national ICD-11 release.
- **OMIM/Orphanet:** no single disease-wide Mendelian entry adequately represents CP because it is a descriptive syndrome; individual genetic CP/CP-mimic disorders have separate entries.
- **Synonyms:** infantile cerebral palsy, cerebral palsies, static encephalopathy (the latter is broader and potentially misleading), spastic diplegia/hemiplegia/quadriplegia when subtype-specific.

Open Targets recognizes MONDO:0006497 and associates CP-related evidence with genes including **SPAST, COL4A1, SNAP25, PMM2**, and with AP-4-complex genes in spastic quadriplegic CP; these associations mix causal-disease and therapeutic-target evidence and therefore must not all be interpreted as disease-causing CP genes. (OpenTargets Search: cerebral palsy)

**Data provenance:** the report concerns aggregated disease-level evidence from cohorts, registries, trials, and reviews. Individual EHR observations can establish a patient’s phenotype but are not the source of the disease-level assertions here.

## 2. Etiology

CP is best represented as an endpoint reached through multiple causal routes.

### Acquired and developmental factors

A 2023 systematic review identified 40 repeatedly reported determinants across 95 studies. Prematurity/low birth weight appeared in 24 studies and low Apgar score in 15. Other recurring factors were intrauterine infection, congenital brain malformation, premature rupture of membranes, placental abruption, maternal thyroid disease, fetal growth restriction, multiple gestation, neonatal CNS infection, stroke, and severe hyperbilirubinemia. Perinatal asphyxia was estimated to account for fewer than 10–20% of cases, emphasizing that temporal proximity to delivery does not prove intrapartum causation. (tegegne2023determinantsofcerebral pages 1-2)

Risk categories include:

- **Preconception/maternal:** diabetes, epilepsy, thyroid disease, obesity, anemia, hypertension and pre-eclampsia; extremes of maternal age and assisted reproduction can mark increased risk but are not individually deterministic.
- **Placental/fetal:** inflammation or infection, placental abruption/vascular malperfusion, congenital brain malformation, fetal growth restriction, multiple pregnancy, and fetal stroke.
- **Perinatal/neonatal:** extreme prematurity, very low birth weight, intraventricular hemorrhage, periventricular white-matter injury, neonatal encephalopathy/HIE, sepsis/meningitis, severe jaundice/kernicterus, hypoglycemia, and cardiorespiratory instability.
- **Postneonatal:** traumatic brain injury, CNS infection, stroke, drowning/hypoxia, and untreated status epilepticus during the early developmental period.

### Genetic factors and gene-environment interaction

Genetic etiologies include de novo dominant variants, autosomal-recessive disorders, X-linked disorders, mitochondrial variants, and CNVs. A genetic lesion may cause maldevelopment directly, predispose to thrombosis or stroke (**PROC, COL4A1/COL4A2**), alter neuronal migration or axonal transport (**CTNNB1, KIF1A, L1CAM, TUBA1A**), or impair mitochondrial metabolism. Genetics may also modify vulnerability to environmental injury. Maternal inflammation can prime fetal microglia and amplify damage from a subsequent hypoxic-ischemic insult—the experimentally supported “two-hit” model. (xu2024geneticpathwaysin pages 1-1, collins2024theimportanceof pages 1-2, lewis2024potentialclinicalapplications pages 1-2)

### Protective factors

No validated common protective human allele prevents CP. Established environmental/clinical protection is chiefly obstetric and neonatal: prevention of preterm birth and infection; antenatal corticosteroids when preterm delivery is expected; magnesium sulfate for fetal neuroprotection; caffeine in selected ventilated preterm infants; prompt resuscitation and treatment of jaundice, hypoglycemia and infection; and therapeutic hypothermia for eligible term/near-term infants with moderate-to-severe HIE. A major systematic review estimated approximately 30% prevention with antenatal magnesium sulfate in very-preterm populations and approximately 15% prevention of hypoxia-associated CP with timely hypothermia. (novak2020stateofthe pages 4-6)

## 3. Phenotypes

Motor manifestations begin in infancy or early childhood and vary from mild unilateral fine-motor impairment to profound four-limb and bulbar disability. The causal lesion is stable, but manifestations evolve with growth.

- **Spasticity**—velocity-dependent hypertonia, hyperreflexia, clonus; severity variable. Suggested HPO: **HP:0001257**.
- **Motor-development delay**—late head control, sitting, crawling or walking; infancy. **HP:0001270**.
- **Abnormal gait/toe walking/scissoring**—primarily ambulant spastic CP. **HP:0001288** (gait disturbance), HP:0002061 (lower-limb spasticity).
- **Dystonia/choreoathetosis**—fluctuating postures and involuntary movement, especially dyskinetic CP. **HP:0001332**, **HP:0002071**.
- **Ataxia/tremor/dysmetria**—usually childhood-recognized and non-degenerative. **HP:0001251**.
- **Unilateral weakness/asymmetry**—hemiplegic CP, often after perinatal stroke. **HP:0004374** or laterality-specific weakness terms.
- **Oromotor dysfunction, dysphagia, drooling**—severity tracks motor impairment; affects nutrition, aspiration risk and participation. **HP:0002015**, **HP:0002307**.
- **Speech/language impairment**—approximately one-third in a 2024 synthesis. **HP:0000750**, HP:0002465 (dysarthria). (xu2024geneticpathwaysin pages 1-1)
- **Intellectual/developmental impairment**—approximately 50%; highly variable. **HP:0001249**, **HP:0001263**.
- **Epilepsy**—approximately one-third; more frequent with cortical injury and severe bilateral CP. **HP:0001250**. (xu2024geneticpathwaysin pages 1-1)
- **Visual/hearing impairment**, pain, sleep disorder, constipation, reflux, scoliosis, hip displacement, contractures and low bone density are important associated or secondary phenotypes.

In a relatively unselected Slovenian cohort, 85% had spastic, 13% dyskinetic and 2% ataxic CP; 36% were GMFCS I. (silan2025unravellinggeneticetiology pages 1-2)

**Quality of life:** pain, communication barriers, feeding dependence, fatigue, reduced mobility and inaccessible environments can restrict education, employment, relationships and community participation. Quality of life is not reducible to GMFCS: communication, pain, autonomy, family support and environmental inclusion are major modifiers. Disease-specific instruments include CP-QOL; generic tools include EQ-5D-Y, PedsQL, PROMIS and adult SF-36.

## 4. Genetic and molecular information

### Architecture and implicated genes

CP has no single canonical causal gene. More than 100 recurrent genes have been reported, converging on axon guidance, synaptic function, vesicle transport, transcription, neuronal migration, thrombosis/angiogenesis, mitochondrial oxidative phosphorylation and autophagy. (xu2024geneticpathwaysin pages 1-1, lewis2024potentialclinicalapplications pages 1-2)

Examples include **CTNNB1, SPAST, ATL1, KIF1A, L1CAM, AP4B1, AP4E1, AP4M1, AP4S1, COL4A1, COL4A2, PROC, GNAO1, KCNQ2, TUBB4A, TUBA1A, PDHA1, FAR1, PLA2G6, SYNGAP1, ZC4H2, ZSWIM6**, and mitochondrial genes. These genes span dominant, recessive, X-linked and mitochondrial inheritance. They should be annotated to their specific molecular diagnoses rather than treated as interchangeable “CP genes.” (silan2025unravellinggeneticetiology pages 1-2, xu2024geneticpathwaysin pages 8-9, yigit2026unmaskinggeneticetiologies pages 1-2)

In the 2024 WGS study, 37/327 children (11%) had pathogenic/likely pathogenic variants and 58/327 (18%) had VUS. Cognitive impairment was more frequent in the P/LP group (49%) than in VUS (33%) or no-variant groups (22%; *p*=0.01). Mitochondrial variants included **MT-TQ, MT-TS1**, and **MT-ND5**. (fehlings2024comprehensivewholegenomesequence pages 17-19)

### Variant interpretation

Reported pathogenic classes include loss-of-function nonsense, frameshift and splice variants; missense variants with loss-, gain-, or altered-channel function; CNVs; structural variants; and mitochondrial variants. Most severe monogenic findings are rare or absent from population databases. Allele frequency and ACMG/AMP classification must be recorded variant-by-variant from the current ClinVar and gnomAD release; no valid disease-wide allele frequency exists. VUS must not direct irreversible treatment or reproductive decisions without further evidence.

### Modifiers, chromosomal and epigenetic findings

CNVs contribute an estimated ~5% diagnostic yield. Reported abnormalities include pathogenic deletions/duplications, but no single recurrent cytogenetic lesion defines CP. Epigenetic and methylation differences have been reported—including discordant monozygotic-twin studies—but causal direction and clinical utility remain unestablished. No validated modifier gene or methylation biomarker currently predicts severity in routine practice. (xu2024geneticpathwaysin pages 9-9, lewis2024potentialclinicalapplications pages 1-2)

## 5. Environmental information

Relevant exposures are principally developmental rather than adult lifestyle or occupational exposures. Maternal smoking, substance exposure, malnutrition, inadequate prenatal care, infection, obesity and socioeconomic disadvantage may alter risk through prematurity, fetal growth, placental function and access to care, but confounding is substantial. Environmental pollution and specific toxins are not established as direct common causes of CP.

Infectious contributors include maternal/fetal cytomegalovirus, toxoplasmosis, rubella, Zika virus and chorioamnionitis, and postnatal meningitis/encephalitis. Infection may cause direct neurotropism, malformation, vascular injury, or cytokine-mediated sensitization to hypoxia. Maternal or amniotic infection is a recognized risk factor for HIE, and maternal immune activation can produce persistent neuroimmune priming in models. (collins2024theimportanceof pages 1-2)

## 6. Mechanism and pathophysiology

### Acquired-injury causal chain

**Placental failure, infection, stroke or hypoxia-ischemia → reduced oxygen/glucose delivery → ATP depletion and anaerobic lactate accumulation → Na+/K+-pump failure and depolarization → glutamate excitotoxicity and intracellular Ca²⁺ accumulation → mitochondrial dysfunction, reactive oxygen species and protease activation → necrosis/apoptosis → secondary microglial/astrocytic inflammation → impaired oligodendrocyte maturation, myelination, axonal connectivity and neuronal circuit development → persistent motor-network dysfunction.** Primary energy failure is upstream; delayed excitotoxic, oxidative and inflammatory injury is downstream and supplies a therapeutic window. (collins2024theimportanceof pages 1-2)

Preterm brains are especially vulnerable in cerebral white matter and pre-oligodendrocytes; term HIE more often injures deep gray nuclei, thalamus, perirolandic cortex, hippocampus or watershed cortex depending on insult pattern. Motor manifestations then arise from altered corticospinal, basal-ganglia-thalamocortical, cerebellar, sensory and spinal networks.

### Genetic causal chains

Examples are **COL4A1/PROC dysfunction → vascular fragility or thrombosis → fetal/perinatal stroke → unilateral spastic CP**; **tubulin/cytoskeletal defects → abnormal neuronal migration/axon formation → cortical malformation → motor impairment and epilepsy**; and **mitochondrial/pyruvate-metabolism defects → energy failure in vulnerable neurons → CP-like motor syndrome**. Some genetic disorders are progressive and therefore CP mimics rather than CP itself.

**Suggested GO processes:** inflammatory response (GO:0006954), response to oxidative stress (GO:0006979), apoptotic process (GO:0006915), autophagy (GO:0006914), neuron migration (GO:0001764), axon guidance (GO:0007411), synaptic vesicle cycle (GO:0099504), myelination (GO:0042552), mitochondrial respiratory-chain complex assembly (GO:0033108), and angiogenesis (GO:0001525).

**Cell Ontology suggestions:** neuron (CL:0000540), cortical neuron, upper motor neuron, microglial cell (CL:0000129), astrocyte (CL:0000127), oligodendrocyte (CL:0000128), oligodendrocyte precursor cell, brain vascular endothelial cell and pericyte.

### Molecular profiling and advanced technology

Transcriptomic, proteomic, metabolomic and methylomic studies report inflammatory, oxidative, lipid/myelin and energy-metabolism signatures, but none is a validated diagnostic test. The 2024 genomic review highlights long-read WGS, transcriptomics, epigenomics and improved structural/repeat-variant detection as routes for unresolved cases. Single-cell and spatial studies are mechanistically promising but not yet mature enough to define a universal CP cell atlas or clinical signature. (lewis2024potentialclinicalapplications pages 1-2)

## 7. Anatomical structures affected

The primary organ is the developing CNS. MRI patterns include maldevelopment, predominant white-matter injury, predominant gray-matter injury, miscellaneous lesions, or normal imaging. MRI is abnormal in more than 80% overall in cited series; one classification study attributed approximately 49% to white-matter injury, 21% to predominant gray-matter injury and 11% to maldevelopment. (lewis2024potentialclinicalapplications pages 1-2)

Suggested anatomical annotations include **brain (UBERON:0000955), cerebral cortex, cerebral white matter, corticospinal tract, basal ganglion, thalamus, cerebellum, brainstem and spinal cord**. Secondary structures include skeletal muscle, tendon, joint, hip, spine, bone, respiratory tract and gastrointestinal tract. Unilateral lesions commonly produce contralateral hemiplegia; bilateral white-matter lesions often produce diplegia; extensive bilateral cortex/deep-gray injury may produce quadriplegic or dyskinetic CP.

At the subcellular level, implicated compartments include mitochondria (GO:0005739), synapse (GO:0045202), axon (GO:0030424), myelin sheath (GO:0043209), cytoskeleton and lysosome/autophagosome.

## 8. Temporal development

The causal disturbance occurs prenatally, perinatally, or in early infancy while motor systems are developing. Clinical recognition is usually insidious: abnormal general movements, asymmetry, persistent primitive reflexes, abnormal tone or delayed milestones appear over months. GMA, HINE and MRI can predict CP by 3–6 months corrected age in high-risk infants, although historic diagnosis often occurred around age two in high-income and later in low-resource settings. (klobucka2026evidenceandpractice pages 4-5, lewis2024potentialclinicalapplications pages 1-2)

CP is chronic and lifelong without a conventional staging or remission system. GMFCS motor trajectories are more useful than “disease stages.” The lesion is static, but contracture, hip displacement, scoliosis, pain, fatigue and mobility decline can develop; learning, adaptation and therapy can improve activity and participation. Critical windows include fetal/neonatal neuroprotection and the first years of activity-dependent neuroplasticity.

## 9. Inheritance and population

Prevalence is generally about 1.5–2 per 1,000 live births globally, with reported ranges exceeding 4 per 1,000 and higher rates in resource-limited settings. A 2020 synthesis reported a ~30% decline in high-income settings to approximately 1.4/1,000, while Bangladesh remained approximately 3.4/1,000. Preterm infants accounted for 43% of cases. (novak2020stateofthe pages 4-6, tegegne2023determinantsofcerebral pages 1-2)

CP overall is multifactorial and does not have one inheritance pattern. Molecular subtypes can be autosomal dominant—often de novo—autosomal recessive, X-linked, mitochondrial, or CNV-mediated. Penetrance, expressivity, germline mosaicism, founder effects and carrier frequency must therefore be stated for the specific diagnosed disorder. Anticipation is not characteristic of CP as a syndrome. Consanguinity increases the probability of recessive CP-like disorders but is not a general cause.

Males are modestly overrepresented in many cohorts; the 2024 WGS cohort was 59.3% male. Biological vulnerability and differential survival may contribute. Socioeconomic and geographic gradients reflect prematurity, infection, neonatal care, ascertainment and rehabilitation access rather than ethnicity as an intrinsic cause. (fehlings2024comprehensivewholegenomesequence pages 21-24, collins2024theimportanceof pages 1-2)

## 10. Diagnostics

### Clinical approach

Diagnosis is clinical: persistent disorder of movement/posture, activity limitation, onset during early development, and a non-progressive causal disturbance. Recommended assessment combines developmental history; neurologic examination; GMA in early infancy; HINE; standardized motor testing; hearing, vision, feeding, communication and cognitive assessment; and GMFCS/MACS/CFCS/EDACS classification. MRI is the principal etiologic imaging study. EEG is used for suspected seizures; EMG is reserved for specific neuromuscular differentials. There is no diagnostic blood test, biopsy or validated circulating biomarker.

### Genomic workflow

A pragmatic workflow is: **(1)** verify phenotype and progression; **(2)** brain MRI and review pregnancy/perinatal history; **(3)** genetics referral and trio ES or GS, with CNV detection; **(4)** CMA if CNVs are not robustly assessed; **(5)** mtDNA testing, metabolic assays, repeat-expansion, RNA or long-read sequencing when phenotype indicates; **(6)** periodic reanalysis. Normal MRI, congenital anomalies, dysmorphism, family history, severe intellectual disability/epilepsy, no plausible acquired insult, or an unexpectedly progressive/fluctuating course increase diagnostic suspicion, but absence of these red flags does not exclude a genetic cause. Meta-analytic yields cited in 2024 were ~23% for SNVs and ~5% for CNVs. (silan2025unravellinggeneticetiology pages 1-2, lewis2024potentialclinicalapplications pages 1-2)

### Differential diagnosis

Important mimics include hereditary spastic paraplegia (**SPAST, ATL1, AP-4 genes**), dopa-responsive dystonia, **GNAO1** disorders, GLUT1 deficiency, mitochondrial disease, leukodystrophy, spinal muscular/neuromuscular disease, Rett-spectrum disease, neurodegeneration with brain iron accumulation, metabolic disorders and structural spinal disease. Regression, episodic decompensation, progressive weakness/spasticity, neuropathy, organ involvement or MRI evolution should prompt reconsideration.

There is no population newborn screen for CP. High-risk infant follow-up and standardized developmental surveillance constitute targeted early detection. Molecular cascade or reproductive testing applies only after a familial diagnosis.

## 11. Outcome and prognosis

Most individuals survive into adulthood, but survival varies markedly with gross-motor severity, feeding and respiratory impairment, epilepsy and intellectual disability. Severe HIE has reported mortality of 25–50%, but that statistic concerns the antecedent neonatal syndrome rather than all CP. Modern disease-wide five- and ten-year survival estimates were not available in the retrieved evidence and should not be inferred from HIE cohorts. (collins2024theimportanceof pages 1-2)

Ambulation, communication and self-care are strongly related to GMFCS/MACS/CFCS levels. Major morbidity includes pain, contracture, hip displacement, scoliosis, fractures, aspiration, malnutrition, constipation, epilepsy, sleep disorders and mental-health difficulties. Recovery of destroyed tissue is limited, but neuroplasticity, assistive technology, surgery and environmental accommodations can produce meaningful gains. Prognostic molecular biomarkers are not validated; MRI pattern, HINE, GMA, GMFCS, cognition, feeding safety and epilepsy currently carry greater clinical utility.

## 12. Treatment

There is no single disease-modifying cure. Management should be individualized, family-centered, goal-directed and multidisciplinary.

### Established interventions

- **Rehabilitation:** active, intensive, task-specific practice; goal-directed training; home programs; bimanual training; constraint-induced movement therapy; strength/fitness and treadmill training; mobility, communication, feeding, occupational and speech therapy. Passive, non-goal-directed treatment is less effective. (novak2020stateofthe pages 13-14, klobucka2026evidenceandpractice pages 4-5)
- **Spasticity/dystonia:** oral baclofen, diazepam or selected alternatives; focal botulinum toxin A with active therapy/casting; intrathecal baclofen for selected generalized hypertonia. Drugs reduce symptoms but may cause weakness, sedation, dysphagia or systemic adverse effects.
- **Epilepsy/pain/bone and GI care:** indication-specific antiseizure medication, analgesia, bisphosphonates in selected low-bone-density cases, nutrition and reflux/constipation management.
- **Surgery:** selective dorsal rhizotomy for carefully selected spastic diplegia; orthopedic soft-tissue/bony procedures for contracture, hip displacement and gait; scoliosis correction; gastrostomy when safe nutrition cannot otherwise be maintained. Hip surveillance uses serial clinical examination and radiographic migration percentage. (klobucka2026evidenceandpractice pages 12-13)

Suggested NCIT intervention annotations include Physical Therapy, Occupational Therapy, Speech Therapy, Botulinum Toxin, Baclofen, Intrathecal Drug Administration, Selective Dorsal Rhizotomy, Orthopedic Surgery, Gastrostomy and Assistive Device.

No CP-specific CPIC pharmacogenomic algorithm is established. Genotype-guided treatment becomes relevant when testing reclassifies the phenotype—for example, a treatable neurotransmitter, transporter or metabolic disorder.

### Experimental therapies and trials

Stem cells, conditioned medium, non-invasive neuromodulation, robotic devices and other regenerative approaches remain investigational. They should not be marketed as proven restoration.

- **NCT06586437:** randomized, double-masked study of cortical/spinal transcutaneous current stimulation with imaging and neurophysiology; estimated **n=50**, active-not-recruiting. (NCT06586437 chunk 1)
- **NCT05158218:** robotic exoskeleton gait training versus conventional gait therapy, 24 sessions over eight weeks; randomized, assessor-masked, **n=64**, active-not-recruiting. (NCT05158218 chunk 1)
- **NCT04360395:** eight-week gait therapy with MEG/EEG, MRI and H-reflex characterization of responders; **n=120**, active-not-recruiting. (NCT04360395 chunk 1)
- **NCT04314687:** phase 1/2 randomized trial of intrathecal allogeneic umbilical-cord mesenchymal stromal cells with or without conditioned medium versus physiotherapy; **n=78**, active-not-recruiting. (NCT04314687 chunk 1)

Hyperbaric oxygen, craniosacral manipulation, unstructured sensory integration and passive stretching without task goals lack convincing evidence. (klobucka2026evidenceandpractice pages 12-13)

## 13. Prevention

**Primary prevention:** optimize maternal health and vaccination; reduce smoking/substance exposure; prevent and treat maternal infection; prevent medically avoidable prematurity; use antenatal corticosteroids and magnesium sulfate when indicated; ensure safe obstetric and neonatal care. Magnesium sulfate and therapeutic hypothermia have the clearest CP-specific neuroprotective evidence. (novak2020stateofthe pages 4-6)

**Secondary prevention:** identify high-risk infants using neonatal history, MRI/ultrasound, GMA and HINE; initiate early active intervention before a delayed definitive label; promptly treat seizures, jaundice, hypoglycemia and infection.

**Tertiary prevention:** hip surveillance, nutrition/aspiration management, vaccination, epilepsy care, bone-health monitoring, contracture prevention, communication support and accessible participation. Genetic counseling should explain that recurrence may be low after a de novo variant, 25% for many recessive diagnoses, 50% for some dominant diagnoses, or follow maternal mitochondrial inheritance—but only after variant-specific interpretation.

## 14. Other species and natural disease

CP is a human clinical construct; there is no single established naturally occurring veterinary equivalent with a CP-specific breed ontology. Animals can naturally sustain congenital malformations, neonatal hypoxia, stroke or infection and show non-progressive motor impairment, but calling these cases “cerebral palsy” is generally analogical. There is no transmission or zoonotic potential.

Relevant taxa for comparative studies include mouse (*Mus musculus*, NCBI Taxon 10090), rat (*Rattus norvegicus*, 10116), rabbit (*Oryctolagus cuniculus*, 9986), sheep (*Ovis aries*, 9940), pig (*Sus scrofa*, 9823), and rhesus macaque (*Macaca mulatta*, 9544). Orthologs of causal human genes are studied in species-specific databases; their relevance depends on the molecular subtype.

## 15. Model organisms

- **Rodent Rice–Vannucci HI model:** unilateral carotid ligation plus systemic hypoxia in neonatal mice/rats. Advantages are cost, genetic manipulation and molecular assays; limitations are unilateral, variably infarct-like injury and a small, lissencephalic, relatively white-matter-poor brain. (koehler2018perinatalhypoxicischemicbrain pages 1-2)
- **Perinatal rabbit HI:** produces hypertonia, postural and locomotor abnormalities resembling CP; useful for motor-phenotype studies but less genetically tractable.
- **Fetal sheep:** umbilical-cord occlusion or cerebral hypoperfusion; particularly useful for pre-oligodendrocyte vulnerability, white-matter injury and continuous fetal physiology.
- **Newborn piglet:** gyrencephalic brain and human-like gray/white-matter organization; hypoxia/hypoperfusion reproduces term-HIE systems injury and permits intensive-care monitoring.
- **Non-human primate:** partial asphyxia preferentially affects motor/somatosensory cortex, basal ganglia and thalamus, while complete asphyxia more strongly injures cerebellum, brainstem sensory nuclei and thalamus. Fidelity is high, but cost and ethical constraints are substantial. (koehler2018perinatalhypoxicischemicbrain pages 1-2)
- **Maternal-immune-activation plus HI models:** capture gene/environment and infection/hypoxia “two-hit” biology. Model validity depends critically on inflammatory stimulus, dose, developmental timing and HI severity. (collins2024theimportanceof pages 1-2)
- **Genetic/cellular systems:** knockout/knock-in animals, patient iPSC-derived neurons/glia, neural organoids and CRISPR-edited lines can test specific CP-associated variants, but cannot reproduce the full motor, placental and developmental context.

Animal work provided decisive translational support for neonatal hypothermia, illustrating the value of physiological large-animal models. No model reproduces the complete etiologic and phenotypic heterogeneity of human CP. (koehler2018perinatalhypoxicischemicbrain pages 1-2)

## Key 2023–2024 sources and exact abstract statements

1. **Fehlings et al., *Nature Genetics*, March 2024.** “Comprehensive whole-genome sequence analyses provide insights into the genomic architecture of cerebral palsy.” DOI/URL: https://doi.org/10.1038/s41588-024-01686-x. This primary human trio-WGS study is the strongest recent genomic evidence retrieved. (fehlings2024comprehensivewholegenomesequence pages 26-28, fehlings2024comprehensivewholegenomesequence pages 17-19)
2. **Lewis et al., *eBioMedicine*, August 2024.** Exact summary: “Recent advancements in genomic technologies offer additional opportunities to uncover variations in human genomes, transcriptomes, and epigenomes that have previously escaped detection.” DOI/URL: https://doi.org/10.1016/j.ebiom.2024.105229. (lewis2024potentialclinicalapplications pages 1-2)
3. **Xu et al., *Neural Regeneration Research*, September 2024.** Exact abstract statement: “It is now widely acknowledged that genetic mutations and alterations play a pivotal role in cerebral palsy development, which can be further influenced by environmental factors.” DOI/URL: https://doi.org/10.4103/1673-5374.385855. (xu2024geneticpathwaysin pages 1-1)
4. **Tegegne, *Sudanese Journal of Paediatrics*, 2023.** Exact abstract statement: “The commonest determinants of CP in children are premature babies and low weight, low Apgar scores, intrauterine infection, congenital brain malformations, thyroid disease, premature rupture of membrane (PROM) and placental abruption.” DOI/URL: https://doi.org/10.24911/SJP.106-1670589241. (tegegne2023determinantsofcerebral pages 1-2)
5. **Collins et al., *Biomedicines*, published 8 November 2024.** Exact abstract statement: “The only proven therapy for HIE is therapeutic hypothermia.” DOI/URL: https://doi.org/10.3390/biomedicines12112559. (collins2024theimportanceof pages 1-2)

## Evidence limitations

The strongest retrieved evidence supports definition, broad prevalence, genomic yield, MRI patterns, risk factors, neuroprotective interventions and selected rehabilitation approaches. Exact modern life-expectancy estimates, phenotype-specific quality-of-life effect sizes, validated CP-wide metabolomic/proteomic signatures, protective genetic alleles, and complete HGNC/OMIM/ClinVar variant-level mappings were not established in the retrieved corpus. Such fields should remain null or be populated only through a variant- or registry-specific curation rather than extrapolation.

References

1. (xu2024geneticpathwaysin pages 1-1): Yiran Xu, Yifei Li, Seidu A. Richard, Yanyan Sun, and Changlian Zhu. Genetic pathways in cerebral palsy: a review of the implications for precision diagnosis and understanding disease mechanisms. Neural Regeneration Research, 19:1499-1508, Sep 2024. URL: https://doi.org/10.4103/1673-5374.385855, doi:10.4103/1673-5374.385855. This article has 15 citations and is from a peer-reviewed journal.

2. (fehlings2024comprehensivewholegenomesequence pages 26-28): Darcy L. Fehlings, Mehdi Zarrei, Worrawat Engchuan, Neal Sondheimer, Bhooma Thiruvahindrapuram, Jeffrey R. MacDonald, Edward J. Higginbotham, Ritesh Thapa, Tarannum Behlim, Sabrina Aimola, Lauren Switzer, Pamela Ng, John Wei, Prakroothi S. Danthi, Giovanna Pellecchia, Sylvia Lamoureux, Karen Ho, Sergio L. Pereira, Jill de Rijke, Wilson W. L. Sung, Alireza Mowjoodi, Jennifer L. Howe, Thomas Nalpathamkalam, Roozbeh Manshaei, Siavash Ghaffari, Joseph Whitney, Rohan V. Patel, Omar Hamdan, Rulan Shaath, Brett Trost, Shannon Knights, Dawa Samdup, Anna McCormick, Carolyn Hunt, Adam Kirton, Anne Kawamura, Ronit Mesterman, Jan Willem Gorter, Nomazulu Dlamini, Daniele Merico, Murto Hilali, Kyle Hirschfeld, Kritika Grover, Nelson X. Bautista, Kara Han, Christian R. Marshall, Ryan K. C. Yuen, Padmaja Subbarao, Meghan B. Azad, Stuart E. Turvey, Piush Mandhane, Theo J. Moraes, Elinor Simons, George Maxwell, Michael Shevell, Gregory Costain, Jacques L. Michaud, Fadi F. Hamdan, Julie Gauthier, Kevin Uguen, Dimitri J. Stavropoulos, Richard F. Wintle, Maryam Oskoui, and Stephen W. Scherer. Comprehensive whole-genome sequence analyses provide insights into the genomic architecture of cerebral palsy. Nature genetics, 56:585-594, Mar 2024. URL: https://doi.org/10.1038/s41588-024-01686-x, doi:10.1038/s41588-024-01686-x. This article has 43 citations and is from a highest quality peer-reviewed journal.

3. (fehlings2024comprehensivewholegenomesequence pages 17-19): Darcy L. Fehlings, Mehdi Zarrei, Worrawat Engchuan, Neal Sondheimer, Bhooma Thiruvahindrapuram, Jeffrey R. MacDonald, Edward J. Higginbotham, Ritesh Thapa, Tarannum Behlim, Sabrina Aimola, Lauren Switzer, Pamela Ng, John Wei, Prakroothi S. Danthi, Giovanna Pellecchia, Sylvia Lamoureux, Karen Ho, Sergio L. Pereira, Jill de Rijke, Wilson W. L. Sung, Alireza Mowjoodi, Jennifer L. Howe, Thomas Nalpathamkalam, Roozbeh Manshaei, Siavash Ghaffari, Joseph Whitney, Rohan V. Patel, Omar Hamdan, Rulan Shaath, Brett Trost, Shannon Knights, Dawa Samdup, Anna McCormick, Carolyn Hunt, Adam Kirton, Anne Kawamura, Ronit Mesterman, Jan Willem Gorter, Nomazulu Dlamini, Daniele Merico, Murto Hilali, Kyle Hirschfeld, Kritika Grover, Nelson X. Bautista, Kara Han, Christian R. Marshall, Ryan K. C. Yuen, Padmaja Subbarao, Meghan B. Azad, Stuart E. Turvey, Piush Mandhane, Theo J. Moraes, Elinor Simons, George Maxwell, Michael Shevell, Gregory Costain, Jacques L. Michaud, Fadi F. Hamdan, Julie Gauthier, Kevin Uguen, Dimitri J. Stavropoulos, Richard F. Wintle, Maryam Oskoui, and Stephen W. Scherer. Comprehensive whole-genome sequence analyses provide insights into the genomic architecture of cerebral palsy. Nature genetics, 56:585-594, Mar 2024. URL: https://doi.org/10.1038/s41588-024-01686-x, doi:10.1038/s41588-024-01686-x. This article has 43 citations and is from a highest quality peer-reviewed journal.

4. (lewis2024potentialclinicalapplications pages 1-2): Sara A. Lewis, Andrew Ruttenberg, Tuğçe Iyiyol, Nahyun Kong, Sheng Chih Jin, and Michael C. Kruer. Potential clinical applications of advanced genomic analysis in cerebral palsy. Aug 2024. URL: https://doi.org/10.1016/j.ebiom.2024.105229, doi:10.1016/j.ebiom.2024.105229. This article has 5 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: cerebral palsy): Open Targets Query (cerebral palsy, 34 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (xu2024geneticpathwaysin pages 2-3): Yiran Xu, Yifei Li, Seidu A. Richard, Yanyan Sun, and Changlian Zhu. Genetic pathways in cerebral palsy: a review of the implications for precision diagnosis and understanding disease mechanisms. Neural Regeneration Research, 19:1499-1508, Sep 2024. URL: https://doi.org/10.4103/1673-5374.385855, doi:10.4103/1673-5374.385855. This article has 15 citations and is from a peer-reviewed journal.

7. (novak2020stateofthe pages 4-6): Iona Novak, Catherine Morgan, Michael Fahey, Megan Finch-Edmondson, Claire Galea, Ashleigh Hines, Katherine Langdon, Maria Mc Namara, Madison CB Paton, Himanshu Popat, Benjamin Shore, Amanda Khamis, Emma Stanton, Olivia P Finemore, Alice Tricks, Anna te Velde, Leigha Dark, Natalie Morton, and Nadia Badawi. State of the evidence traffic lights 2019: systematic review of interventions for preventing and treating children with cerebral palsy. Current Neurology and Neuroscience Reports, Feb 2020. URL: https://doi.org/10.1007/s11910-020-1022-z, doi:10.1007/s11910-020-1022-z. This article has 1632 citations and is from a domain leading peer-reviewed journal.

8. (silan2025unravellinggeneticetiology pages 1-2): Ula Arkar Silan, Ana Trebše, Jernej Kovač, Mihael Rogac, Anja Troha Gergeli, Robert Šket, Tina Bregant, David Neubauer, Borut Peterlin, and Damjan Osredkar. Unravelling genetic etiology of cerebral palsy: findings from a slovenian pediatric cohort. Frontiers in Neurology, Jul 2025. URL: https://doi.org/10.3389/fneur.2025.1615449, doi:10.3389/fneur.2025.1615449. This article has 1 citations and is from a peer-reviewed journal.

9. (tegegne2023determinantsofcerebral pages 1-2): Kaleab Tegegne. Determinants of cerebral palsy in children: systematic review. Sudanese journal of paediatrics, 23 2:126-144, Jan 2023. URL: https://doi.org/10.24911/sjp.106-1670589241, doi:10.24911/sjp.106-1670589241. This article has 13 citations.

10. (collins2024theimportanceof pages 1-2): Bailey Collins, Elise A. Lemanski, and Elizabeth Wright-Jin. The importance of including maternal immune activation in animal models of hypoxic–ischemic encephalopathy. Biomedicines, 12:2559, Nov 2024. URL: https://doi.org/10.3390/biomedicines12112559, doi:10.3390/biomedicines12112559. This article has 8 citations.

11. (klobucka2026evidenceandpractice pages 4-5): Stanislava Klobucká, Katarína Chamutyová, Robert Klobucký, Pavel Šiarnik, Ľudmila Podracká, and Branislav Kollár. Evidence and practice in the rehabilitation of patients with cerebral palsy: a structured narrative review informed by a systematic literature search. Bratislava Medical Journal, 127:1790-1812, Mar 2026. URL: https://doi.org/10.1007/s44411-026-00551-z, doi:10.1007/s44411-026-00551-z. This article has 2 citations.

12. (fehlings2024comprehensivewholegenomesequence pages 21-24): Darcy L. Fehlings, Mehdi Zarrei, Worrawat Engchuan, Neal Sondheimer, Bhooma Thiruvahindrapuram, Jeffrey R. MacDonald, Edward J. Higginbotham, Ritesh Thapa, Tarannum Behlim, Sabrina Aimola, Lauren Switzer, Pamela Ng, John Wei, Prakroothi S. Danthi, Giovanna Pellecchia, Sylvia Lamoureux, Karen Ho, Sergio L. Pereira, Jill de Rijke, Wilson W. L. Sung, Alireza Mowjoodi, Jennifer L. Howe, Thomas Nalpathamkalam, Roozbeh Manshaei, Siavash Ghaffari, Joseph Whitney, Rohan V. Patel, Omar Hamdan, Rulan Shaath, Brett Trost, Shannon Knights, Dawa Samdup, Anna McCormick, Carolyn Hunt, Adam Kirton, Anne Kawamura, Ronit Mesterman, Jan Willem Gorter, Nomazulu Dlamini, Daniele Merico, Murto Hilali, Kyle Hirschfeld, Kritika Grover, Nelson X. Bautista, Kara Han, Christian R. Marshall, Ryan K. C. Yuen, Padmaja Subbarao, Meghan B. Azad, Stuart E. Turvey, Piush Mandhane, Theo J. Moraes, Elinor Simons, George Maxwell, Michael Shevell, Gregory Costain, Jacques L. Michaud, Fadi F. Hamdan, Julie Gauthier, Kevin Uguen, Dimitri J. Stavropoulos, Richard F. Wintle, Maryam Oskoui, and Stephen W. Scherer. Comprehensive whole-genome sequence analyses provide insights into the genomic architecture of cerebral palsy. Nature genetics, 56:585-594, Mar 2024. URL: https://doi.org/10.1038/s41588-024-01686-x, doi:10.1038/s41588-024-01686-x. This article has 43 citations and is from a highest quality peer-reviewed journal.

13. (yigit2026unmaskinggeneticetiologies pages 1-2): Ayca Yigit, Ozlem Akgun-Dogan, Zeynep Ozkeserli, Gunseli Bayram Akcapınar, Semih Ayta, Pinar Gencpinar, Hulya Maras Genc, Busra Kutlubay, Bulent Kara, Hatice Gulhan Sozen, Nihat Bugra Agaoglu, Ozkan Ozdemir, Kaya Bilguvar, and Ugur Ozbek. Unmasking genetic etiologies in neurodevelopmental disorders characterized by cerebral palsy: insights from integrative genomic approaches. Frontiers in Neurology, Feb 2026. URL: https://doi.org/10.3389/fneur.2026.1742186, doi:10.3389/fneur.2026.1742186. This article has 0 citations and is from a peer-reviewed journal.

14. (koehler2018perinatalhypoxicischemicbrain pages 1-2): Raymond C Koehler, Zeng-Jin Yang, Jennifer K Lee, and Lee J Martin. Perinatal hypoxic-ischemic brain injury in large animal models: relevance to human neonatal encephalopathy. Journal of Cerebral Blood Flow & Metabolism, 38:2092-2111, Aug 2018. URL: https://doi.org/10.1177/0271678x18797328, doi:10.1177/0271678x18797328. This article has 109 citations and is from a highest quality peer-reviewed journal.

15. (novak2020stateofthe pages 13-14): Iona Novak, Catherine Morgan, Michael Fahey, Megan Finch-Edmondson, Claire Galea, Ashleigh Hines, Katherine Langdon, Maria Mc Namara, Madison CB Paton, Himanshu Popat, Benjamin Shore, Amanda Khamis, Emma Stanton, Olivia P Finemore, Alice Tricks, Anna te Velde, Leigha Dark, Natalie Morton, and Nadia Badawi. State of the evidence traffic lights 2019: systematic review of interventions for preventing and treating children with cerebral palsy. Current Neurology and Neuroscience Reports, Feb 2020. URL: https://doi.org/10.1007/s11910-020-1022-z, doi:10.1007/s11910-020-1022-z. This article has 1632 citations and is from a domain leading peer-reviewed journal.

16. (klobucka2026evidenceandpractice pages 12-13): Stanislava Klobucká, Katarína Chamutyová, Robert Klobucký, Pavel Šiarnik, Ľudmila Podracká, and Branislav Kollár. Evidence and practice in the rehabilitation of patients with cerebral palsy: a structured narrative review informed by a systematic literature search. Bratislava Medical Journal, 127:1790-1812, Mar 2026. URL: https://doi.org/10.1007/s44411-026-00551-z, doi:10.1007/s44411-026-00551-z. This article has 2 citations.

17. (NCT06586437 chunk 1): Max Kurz. Neuromodulation of the Cortex and Spinal Cord. Father Flanagan's Boys' Home. 2024. ClinicalTrials.gov Identifier: NCT06586437

18. (NCT05158218 chunk 1): Max Kurz. Robotic Exoskeleton Gait Training in Adolescents With Cerebral Palsy. Father Flanagan's Boys' Home. 2021. ClinicalTrials.gov Identifier: NCT05158218

19. (NCT04360395 chunk 1): Max Kurz. Igniting Mobility in Adolescents and Young Adults With Cerebral Palsy. Father Flanagan's Boys' Home. 2020. ClinicalTrials.gov Identifier: NCT04360395

20. (NCT04314687 chunk 1):  Stem Cell and Conditioned Medium for Cerebral Palsy. PT. Prodia Stem Cell Indonesia. 2021. ClinicalTrials.gov Identifier: NCT04314687

21. (xu2024geneticpathwaysin pages 8-9): Yiran Xu, Yifei Li, Seidu A. Richard, Yanyan Sun, and Changlian Zhu. Genetic pathways in cerebral palsy: a review of the implications for precision diagnosis and understanding disease mechanisms. Neural Regeneration Research, 19:1499-1508, Sep 2024. URL: https://doi.org/10.4103/1673-5374.385855, doi:10.4103/1673-5374.385855. This article has 15 citations and is from a peer-reviewed journal.

22. (xu2024geneticpathwaysin pages 9-9): Yiran Xu, Yifei Li, Seidu A. Richard, Yanyan Sun, and Changlian Zhu. Genetic pathways in cerebral palsy: a review of the implications for precision diagnosis and understanding disease mechanisms. Neural Regeneration Research, 19:1499-1508, Sep 2024. URL: https://doi.org/10.4103/1673-5374.385855, doi:10.4103/1673-5374.385855. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cerebral_Palsy-deep-research-falcon_artifacts/artifact-00.md)