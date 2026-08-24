---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:50:09.158191'
end_time: '2026-08-01T18:58:43.805131'
duration_seconds: 514.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chung-Jansen Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Chung-Jansen_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chung-Jansen Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chung-Jansen Syndrome** covering all of the
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
- **Disease Name:** Chung-Jansen Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chung-Jansen Syndrome** covering all of the
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


# Chung–Jansen syndrome: disease-characteristics research report

## Executive summary

Chung–Jansen syndrome (CHUJANS) is a rare, autosomal-dominant Mendelian neurodevelopmental disorder caused principally by heterozygous loss of function of **PHIP**. Its core phenotype comprises developmental delay or intellectual/learning disability, behavioral or psychiatric abnormalities, a recognizable facial gestalt, and variably penetrant overweight or obesity. In the largest recent primary cohort available here—23 newly described individuals—developmental delay occurred in 22/23, learning disability/intellectual disability in 22/23, behavioral abnormalities in 20/23, weight problems in 13/23, and characteristic craniofacial findings in 23/23. Both de novo variants and transmission from mildly affected parents occur, demonstrating marked variable expressivity. (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

The most developed mechanistic model links deficient nuclear PHIP activity to reduced **POMC** transcription and impaired anorexigenic leptin–melanocortin signaling. Cellular experiments found that all tested disease/obesity-associated PHIP mutants reduced POMC-reporter activity; four variants showed dose-dependent dominant-negative effects, and case variants significantly reduced the nuclear-to-cytoplasmic PHIP ratio. This mechanism plausibly explains obesity but does not yet fully explain the neurodevelopmental phenotype. (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 10-11)

| Topic | Key finding | Evidence / source |
|---|---|---|
| Identity / identifiers | Chung-Jansen syndrome (CHUJANS), also called DIDOD syndrome; OMIM disease identifier reported as **#617991**. Disease-level identifiers beyond OMIM (e.g., MONDO, HPO set) should be treated as **needing database validation** if not independently verified. | 2023 cohort paper states CHUJANS, OMIM #617991; PHIP gene OMIM *612870 (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2) |
| Causal gene and mechanism | Primary causal gene is **PHIP** (pleckstrin homology domain interacting protein). Current understanding supports **PHIP haploinsufficiency** as the main disease mechanism; variant classes include truncating, missense, splice, and larger deletions. | Kampmeier et al., 2023, *Front Cell Dev Biol*, DOI: https://doi.org/10.3389/fcell.2022.1020609 (kampmeier2023phipassociatedchungjansensyndrome pages 1-2) |
| Inheritance | Usually **autosomal dominant** with many **de novo** cases, but inherited cases from **mildly affected parents** are documented, indicating **variable expressivity** and likely reduced/variable penetrance in some families. In the 23-person 2023 cohort, inheritance was seen in multiple maternal or paternal transmissions. | 2023 cohort summary and segregation analysis (Sanger/qPCR/FISH) (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2) |
| Strongest 2023 phenotype frequencies | In 23 newly reported individuals: developmental delay **22/23**, learning disability/intellectual disability **22/23**, behavioral abnormalities **20/23**, weight problems **13/23**, and characteristic craniofacial features **23/23**; cohort included **13 males / 10 females**. Facial pattern included large ears/earlobes, prominent eyebrows, anteverted nares, and long philtrum. | Kampmeier et al., 2023, DOI: https://doi.org/10.3389/fcell.2022.1020609 (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2, kampmeier2023phipassociatedchungjansensyndrome pages 3-5) |
| Clinical course / phenotype interpretation | Neurodevelopmental and behavioral features begin in childhood; obesity/overweight is common but variably penetrant and may emerge from childhood to puberty. Behavioral issues can include impulsivity, aggression, anxiety, hyperactivity, and autism-spectrum features; regular follow-up into adulthood was recommended. | 2023 cohort interpretation (kampmeier2023phipassociatedchungjansensyndrome pages 10-11) |
| Molecular evidence | PHIP has both **cytoplasmic** and **nuclear** functions. Functional data support obesity pathogenesis through impaired **POMC transcription** in the leptin-melanocortin pathway. Wild-type PHIP enhanced POMC transcription, whereas all tested PHIP mutants reduced it; some variants showed **dominant-negative** effects. Case variants also decreased the nuclear:cytoplasmic PHIP ratio (**p=0.004**). | Marenne et al., 2020, *Cell Metab*, DOI: https://doi.org/10.1016/j.cmet.2020.05.007 (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 10-11, marenne2020exomesequencingidentifies pages 1-3) |
| Obesity genetics signal | In severe childhood obesity sequencing analyses, **PHIP** showed an excess burden of very rare predicted deleterious variants; reported enrichment for obese cases had **p=4.58×10^-4** and **OR=2.4 [1.5–3.84]**. | Marenne et al., 2020, DOI: https://doi.org/10.1016/j.cmet.2020.05.007 (marenne2020exomesequencingidentifies pages 5-6) |
| Additional mechanistic biology | Published disease discussions also connect PHIP disruption with **replication fork stability / genome integrity** defects, although disease-specific pathway resolution remains incomplete. | 2023 disease cohort discussion (kampmeier2023phipassociatedchungjansensyndrome pages 12-13) |
| Diagnostics | Diagnosis is currently based on **genetic testing** plus clinical evaluation. Methods reported include **microarray, gene panels, exome sequencing**, followed by **Sanger sequencing, qPCR, and FISH** for confirmation/segregation. PHIP should be considered on DD/ID/behavioral abnormality/obesity panels. Facial phenotyping tools such as **GestaltMatcher** may support recognition but are not standalone diagnostics. | Kampmeier et al., 2023, DOI: https://doi.org/10.3389/fcell.2022.1020609 (kampmeier2023phipassociatedchungjansensyndrome pages 1-2, kampmeier2023phipassociatedchungjansensyndrome pages 3-5, kampmeier2023phipassociatedchungjansensyndrome pages 11-12) |
| Real-world implementation / registries | The main identified implementation resource is **Simons Searchlight** (**NCT01238250**), a recruiting, international, longitudinal **observational** registry collecting medical, behavioral, developmental, and genetic data from individuals with eligible neurodevelopmental genetic conditions, including PHIP-related disorders. It does **not** test treatments. | ClinicalTrials.gov NCT01238250 / Simons Searchlight (NCT01238250 chunk 1, NCT01238250 chunk 2) |
| Management / treatment | No disease-specific, evidence-based **disease-modifying therapy** or interventional trial was identified in the retrieved evidence. Current care is **multidisciplinary and phenotype-directed**: developmental/behavioral assessment, educational supports, obesity surveillance and management, and genetic counseling for families. | Derived from absence of interventional trial evidence plus cohort recommendations for follow-up (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, NCT01238250 chunk 1, NCT01238250 chunk 2) |
| Major evidence gaps | Population prevalence/incidence, validated survival data, disease-specific quality-of-life measures, penetrance estimates, genotype-phenotype correlations, standardized treatment algorithms, and validated MONDO/HPO identifier set remain **insufficiently defined** in the retrieved evidence. Disease-specific single-cell, spatial transcriptomic, proteomic, and metabolomic studies were not identified here. | Evidence gap synthesis from available cohort/mechanistic/registry sources (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, marenne2020exomesequencingidentifies pages 5-6, NCT01238250 chunk 1) |


*Table: This table condenses the highest-yield disease knowledge-base facts for Chung-Jansen syndrome, including identifiers, genetics, phenotype frequencies, mechanism, diagnostics, management, and evidence gaps. It is designed as a compact reference for curation and downstream database entry.*

## Evidence scope and limitations

The strongest disease-specific sources retrieved were Kampmeier et al., published **16 January 2023**, reporting 23 individuals ([DOI](https://doi.org/10.3389/fcell.2022.1020609)), and Marenne et al., published **June 2020**, providing human genetic and functional evidence for PHIP in severe childhood obesity ([DOI](https://doi.org/10.1016/j.cmet.2020.05.007)). PMID values were not exposed in the retrieved records and therefore are not supplied rather than guessed. The literature remains dominated by small, clinically ascertained cohorts and case reports; frequency estimates should not be interpreted as population prevalence. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, marenne2020exomesequencingidentifies pages 5-6)

## 1. Disease information

**Definition.** CHUJANS is a congenital/early-childhood neurodevelopmental syndrome due to PHIP dosage or functional deficiency. The disorder combines cognitive-developmental impairment, behavioral abnormalities, dysmorphic facial features, and susceptibility to excessive weight gain. (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

**Identifiers and names.**

- **OMIM:** #617991.
- **Causal-gene OMIM:** **PHIP**, *612870.
- **Common names:** Chung–Jansen syndrome; PHIP-associated Chung–Jansen syndrome; PHIP-related disorder; **DIDOD syndrome** (“developmental delay, intellectual disability, obesity, and dysmorphism”). (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)
- **MONDO:** a stable MONDO identifier was not verified in the retrieved evidence and should be validated directly against the current MONDO release before database ingestion.
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifiers were established by the retrieved primary literature. In practice, manifestations are coded separately—for example intellectual disability, developmental disorder, behavioral disorder, or obesity—rather than through a uniquely validated CHUJANS ICD code.

The evidence summarized here is **aggregated disease-level evidence** from research cohorts and registries, not individual EHR-derived information. The 2023 cohort collected standardized clinical and genetic information from referring geneticists in six European countries; it included 13 males and 10 females. (kampmeier2023phipassociatedchungjansensyndrome pages 3-5)

**Representative exact abstract statement:** “almost all individuals reported here show developmental delay (22/23), learning disability or ID (22/23), behavioral abnormalities (20/23), weight problems (13/23) and characteristic craniofacial features … (23/23).” (kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factors

The primary cause is a **heterozygous germline pathogenic PHIP alteration**, most commonly producing haploinsufficiency. Reported classes include nonsense and frameshift variants, splice variants, missense substitutions, intragenic/whole-gene deletions, and larger deletions involving PHIP plus neighboring genes. Larger deletions may produce blended or more complex phenotypes because additional genes are affected. (kampmeier2023phipassociatedchungjansensyndrome pages 1-2, kampmeier2023phipassociatedchungjansensyndrome pages 3-5)

### Genetic risk

A pathogenic PHIP allele is the principal risk factor. Variants may arise de novo or be inherited from a mildly affected parent. Five inherited cases were documented in the 23-person cohort, supporting vertical transmission and substantial intrafamilial variability. Loss-of-function variants may be more strongly associated with obesity than missense variants, although present sample sizes are insufficient for a definitive variant-class prognosis. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 2-3)

In severe-obesity sequencing, very rare predicted-deleterious PHIP variants were enriched in 2,737 cases versus 6,704 controls; the combined analysis reported **OR 2.4, 95% CI 1.5–3.84; p=4.58×10⁻⁴**. This supports PHIP as an obesity gene but did not reach a conventional exome-wide Bonferroni threshold, and obesity is not completely penetrant among CHUJANS patients. (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 10-11, marenne2020exomesequencingidentifies pages 1-3)

### Environmental, infectious, and lifestyle factors

No toxin, infection, radiation exposure, occupation, diet, or lifestyle factor is known to cause CHUJANS. Diet, physical activity, medications, sleep, and the family environment may modify weight or behavior after onset, but disease-specific gene–environment interaction studies were not found. There is no infectious agent and no zoonotic transmission.

### Protective factors

No validated protective PHIP allele, modifier gene, dietary exposure, medication, or lifestyle intervention has been shown to prevent the syndrome. Healthy nutrition and activity may mitigate secondary obesity but do not prevent the underlying neurodevelopmental disorder. Claims of molecular protection would presently be speculative.

## 3. Phenotypes

The following ontology terms are suggested for curation; exact HPO releases should be checked before production use.

| Phenotype | Frequency/course | Suggested HPO term |
|---|---|---|
| Developmental delay | 22/23 in the 2023 cohort; begins in infancy/childhood; chronic | Global developmental delay, **HP:0001263** |
| Learning disability/intellectual disability | 22/23; usually mild-to-moderate and variable; verbal ability may exceed performance ability | Intellectual disability, **HP:0001249**; learning disability, **HP:0001328** |
| Speech/language delay | Common but not universal; early childhood | Delayed speech and language development, **HP:0000750** |
| Behavioral abnormalities | 20/23 (87%); impulsivity, aggression, anxiety, hyperactivity, and autistic features reported | Behavioral abnormality, **HP:0000708**; hyperactivity, **HP:0000752**; anxiety, **HP:0000739**; autistic behavior, **HP:0000729** |
| Overweight/obesity | 13/23 had weight problems; combined reports suggest approximately 56–70%; onset ranges from childhood to puberty | Obesity, **HP:0001513**; childhood-onset obesity, **HP:0012743** |
| Hypotonia | Common; a combined 47-person summary reported 78% | Muscular hypotonia, **HP:0001252** |
| Feeding difficulty | Frequently reported in childhood; historical cohorts reported approximately 77–100%, but definitions varied | Feeding difficulties, **HP:0011968** |
| Facial gestalt | 23/23 in the 2023 cohort: large ears/earlobes, prominent eyebrows, anteverted nares, long philtrum | Large ears, **HP:0000400**; thick/prominent eyebrows, **HP:0000574**; anteverted nares, **HP:0000463**; long philtrum, **HP:0000343** |
| Constipation | Reported across cohorts, approximately 30–76%, depending on ascertainment | Constipation, **HP:0002019** |
| Balance/gait problems | Recurrent but incompletely quantified | Abnormality of coordination, **HP:0011443** or gait abnormality, **HP:0001288** |
| Seizures | Reported minority feature; not a defining universal manifestation | Seizure, **HP:0001250** |
| Orthopedic findings | Hip dysplasia and clubfoot reported in subsets | Developmental dysplasia of the hip, **HP:0001385**; talipes equinovarus, **HP:0001762** |

The cohort-level frequencies above are supported by direct denominators, whereas feeding, constipation, hypotonia, and seizure estimates vary among cohorts and ascertainment instruments. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 5-5, loid2026anovelphip pages 5-6)

**Quality of life.** No CHUJANS-specific EQ-5D, SF-36, PROMIS, or validated caregiver-burden study was identified. Nevertheless, cognitive limitations affect education and independent functioning; communication deficits, ADHD/autistic or aggressive behaviors affect family and social participation; hypotonia and coordination problems affect mobility; and obesity raises long-term metabolic and psychosocial burden. These are clinically plausible impacts, but quantitative CHUJANS-specific utility values are unavailable.

## 4. Genetic and molecular information

### Gene and variant interpretation

- **Gene:** PHIP, pleckstrin homology domain interacting protein.
- **Reference transcript used in the 2023 cohort:** **NM_017934.7**. (kampmeier2023phipassociatedchungjansensyndrome pages 3-5)
- **Origin:** constitutional/germline, not a somatic cancer disorder.
- **Inheritance:** autosomal dominant.
- **Primary mechanism:** haploinsufficiency; selected missense/truncating variants may also exert dominant-negative effects in reporter assays. (kampmeier2023phipassociatedchungjansensyndrome pages 1-2, marenne2020exomesequencingidentifies pages 5-6)
- **Population frequency expectation:** truly pathogenic alleles should be absent or extremely rare in gnomAD/other reference populations. Variant-specific frequencies must be queried directly because no universal value applies.
- **Classification:** truncating/deletion alleles affecting a loss-of-function-sensitive gene may satisfy ACMG/AMP pathogenic/likely-pathogenic evidence; missense variants require segregation, population, computational, domain, and preferably functional evidence. A VUS should not establish the diagnosis by itself.

No recurrent founder allele, anticipation, carrier frequency, or validated modifier gene has been established. Large deletions require attention to neighboring genes, while mildly affected transmitting parents demonstrate that phenotype prediction from genotype alone is unreliable. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

### Epigenetics and structural variation

A PHIP-associated DNA-methylation episignature has been reported secondarily and may overlap partially with signatures of other neurodevelopmental syndromes, suggesting possible future utility for resolving VUSs. However, the retrieved evidence did not provide sufficient primary validation metrics for routine diagnostic endorsement. (loid2026anovelphip pages 7-8, loid2026anovelphip pages 5-6)

Chromosomal microdeletions involving part or all of PHIP are established molecular causes. CMA detects copy-number loss; qPCR or FISH can confirm the deletion and parental segregation. Karyotyping is generally too low-resolution for small PHIP deletions. (kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

## 5. Environmental information

CHUJANS is not an environmentally acquired, infectious, toxicologic, occupational, or lifestyle disease. Environmental exposures can influence downstream obesity, development, education, and behavior, as in the general population, but no CHUJANS-specific CTD-style exposure association or formal gene–environment study was identified. Smoking, alcohol, pollution, radiation, and pathogens have no established etiologic role.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**Pathogenic PHIP allele → reduced or dysfunctional PHIP protein → impaired nuclear transcription/chromatin-replication functions and, for some alleles, altered intracellular localization → dysregulated developmental gene expression and POMC signaling → neurodevelopmental impairment plus reduced satiety/energy-homeostasis signaling → learning/behavioral abnormalities and obesity susceptibility.**

PHIP has at least two functionally relevant contexts. A cytoplasmic approximately 104-kDa isoform interacts with IRS-1/IRS-2 and participates in insulin/IGF-1 signaling. A larger approximately 230-kDa nuclear isoform, also described as DCAF14/REPID, binds chromatin and participates in DNA replication and transcription. Disease discussions additionally implicate replication-fork stability and genome integrity. (kampmeier2023phipassociatedchungjansensyndrome pages 12-13, marenne2020exomesequencingidentifies pages 5-6)

### POMC/leptin–melanocortin mechanism

Wild-type PHIP enhanced POMC transcription under basal and leptin-stimulated conditions. All tested mutant constructs reduced POMC-reporter activity, and four—T289P, D594E, Q1343X, and R1505Q—showed dose-dependent dominant-negative effects against wild-type PHIP. Case-associated variants also produced a significantly lower nuclear:cytoplasmic PHIP ratio than control variants (**p=0.004**). The proposed downstream consequence is diminished hypothalamic POMC-derived melanocortin signaling and impaired appetite suppression. (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 10-11, marenne2020exomesequencingidentifies pages 20-21)

This evidence is **in vitro**—HEK293/COS-7 transfection, luciferase reporters, leptin stimulation, and microscopy—not direct demonstration in patient hypothalamic neurons. It is therefore a strong mechanistic hypothesis for obesity, not yet a complete tissue-level causal proof. (marenne2020exomesequencingidentifies pages 10-11, marenne2020exomesequencingidentifies pages 20-21)

### Suggested ontology annotations

- **GO biological processes:** regulation of transcription by RNA polymerase II; DNA replication; replication-fork protection; maintenance of genome integrity; insulin receptor signaling; cellular response to leptin; regulation of feeding behavior; nervous-system development.
- **GO cellular components:** nucleus; chromatin; cytoplasm; replication fork.
- **Cell Ontology candidates:** neuron (**CL:0000540**), hypothalamic neuron, POMC-expressing neuron, neural progenitor cell, and adipocyte (**CL:0000136**). Only neuron-level and cell-line functional evidence is presently strong; disease-specific single-cell localization is not established.
- **Chemical ontology candidates:** leptin, insulin, glucose, and proopiomelanocortin-derived peptides; CHEBI identifiers should be verified against the current release.

No CHUJANS-specific patient transcriptome, proteome, metabolome, lipidome, spatial transcriptome, single-cell atlas, iPSC-neuron dataset, or CRISPR screen was identified. Consequently, claims about affected neuronal subclasses, metabolic signatures, immune activation, oxidative injury, fibrosis, or organ-specific cell death would be unsupported.

## 7. Anatomical structures affected

The **central nervous system** is the principal functional system affected, manifesting through cognition, language, motor coordination, tone, and behavior. The hypothalamic appetite-control network is mechanistically implicated by POMC findings, although direct patient-tissue confirmation is lacking. Suggested anatomy terms include brain (**UBERON:0000955**), central nervous system (**UBERON:0001017**), hypothalamus (**UBERON:0001898**), and cerebral cortex (**UBERON:0000956**). (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 1-3)

Secondary systems include adipose/metabolic tissues through obesity; craniofacial structures through dysmorphism; gastrointestinal tract through feeding difficulty and constipation; skeletal/musculoskeletal structures through hypotonia, balance problems, hip dysplasia, or clubfoot; and, in a minority, the nervous system through seizures. No consistent lateralization has been reported. (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 5-5)

At the subcellular level, the nucleus, chromatin/replication machinery, cytoplasm, and nuclear–cytoplasmic trafficking/localization are relevant. (kampmeier2023phipassociatedchungjansensyndrome pages 12-13, marenne2020exomesequencingidentifies pages 5-6)

## 8. Temporal development

CHUJANS is genetically present from conception and usually becomes clinically evident in infancy or early childhood through hypotonia, feeding problems, delayed milestones, or speech/learning difficulty. Facial characteristics may become more recognizable with age. Weight gain is variable and may begin in childhood or around puberty; therefore, normal early weight does not exclude later obesity. Behavioral and psychiatric manifestations may evolve with developmental demands and warrant continued surveillance into adulthood. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 3-5)

The course is **chronic and lifelong**, not relapsing-remitting. There are no validated disease stages, remission pattern, or predictable progression rate. Developmental skills may improve with therapy and education, but the genetic condition does not resolve. Early childhood is the main intervention window for speech, motor, educational, and behavioral support; longitudinal adult natural-history data remain sparse.

## 9. Inheritance and population

CHUJANS follows an **autosomal-dominant** pattern. Many affected individuals have de novo variants, but inherited disease from mildly affected mothers or fathers is established. For an affected heterozygous individual, the theoretical transmission probability is **50% per pregnancy**, although clinical severity cannot be predicted reliably. Parental testing is essential because subtle learning, behavioral, or weight manifestations may only be recognized retrospectively. (kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

Penetrance is not formally quantified and may be incomplete for individual manifestations—especially obesity—while expressivity is clearly variable. Germline mosaicism has not been quantified; after an apparently de novo result, recurrence risk is low but not zero because parental gonadal mosaicism cannot be excluded. No anticipation, founder effect, consanguinity association, ethnic enrichment, or geographic concentration has been established.

Population prevalence, incidence, carrier frequency, mortality, and age distribution are unknown. The 2023 cohort’s sex distribution—13 males and 10 females—does not support a meaningful sex bias and is consistent with autosomal inheritance. (kampmeier2023phipassociatedchungjansensyndrome pages 3-5)

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** developmental/learning disability plus behavioral problems, characteristic facial features, hypotonia or coordination problems, and/or childhood-onset overweight/obesity.
2. **First-line genomic testing:** trio exome or genome sequencing, or a comprehensive neurodevelopmental/syndromic-obesity panel that includes PHIP. Exome sequencing was a major discovery route in reported patients. (kampmeier2023phipassociatedchungjansensyndrome pages 3-5)
3. **Copy-number assessment:** ensure the platform detects exon-level/whole-gene deletions; otherwise add CMA or validated deletion/duplication analysis.
4. **Confirmation and segregation:** Sanger sequencing for sequence variants; qPCR/MLPA or orthogonal CNV assay for deletions; parental testing for inheritance and counseling. FISH may be useful for sufficiently large rearrangements. (kampmeier2023phipassociatedchungjansensyndrome pages 1-2)
5. **Variant interpretation:** apply ACMG/AMP criteria, phenotype fit, de novo/segregation data, gnomAD absence, and functional evidence. Do not use facial analysis alone.

WGS may detect sequence variants, CNVs, and structural/regulatory changes missed by panel or exome testing. RNA sequencing could clarify a suspected splice variant, and methylation profiling may eventually help selected VUS cases, but neither is yet a validated routine CHUJANS biomarker in the retrieved evidence.

There is no diagnostic blood chemistry, enzyme assay, metabolite, biopsy, EEG pattern, MRI signature, or circulating biomarker. EEG is indicated for suspected seizures; MRI, endocrine/metabolic laboratory testing, orthopedic imaging, sleep evaluation, and gastrointestinal assessment should be symptom-directed.

### Differential diagnosis

Important differentials include Prader–Willi syndrome, CUL4B-related Cabezas syndrome, other syndromic/monogenic obesity disorders, and neurodevelopmental syndromes with dysmorphism. GestaltMatcher analysis separated the average PHIP facial pattern from healthy controls, Prader–Willi syndrome, and CUL4B-related disorder, but could not reliably distinguish PHIP missense from loss-of-function or splice classes. Thus, facial AI is an adjunct to—not a replacement for—molecular testing. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 2-3, kampmeier2023phipassociatedchungjansensyndrome pages 11-12)

No population newborn screen is available. Cascade testing is appropriate after a familial pathogenic variant is identified.

## 11. Outcome and prognosis

No 5- or 10-year survival estimates, disease-specific mortality rate, or validated life-expectancy estimate exists. The available phenotype does not indicate a uniformly lethal disorder, but adult follow-up is too limited for strong longevity conclusions. Morbidity is primarily developmental, educational, behavioral, motor, and metabolic.

Long-term complications may include reduced independence, persistent communication/learning needs, psychiatric or behavioral morbidity, and obesity-associated hypertension, dyslipidemia, insulin resistance, fatty liver disease, sleep-disordered breathing, and orthopedic burden. These metabolic complications are plausible consequences of obesity, not yet quantified as CHUJANS-specific rates.

Prognosis is highly variable, even within families. Mildly affected transmitting parents show that adult functioning can be substantially better than in an ascertained child, while larger deletions or additional variants may worsen outcomes. No validated prognostic molecular biomarker exists. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 2-3)

## 12. Treatment and current applications

There is no approved PHIP-targeted or disease-modifying treatment. Current real-world care is multidisciplinary and phenotype-directed:

- early-intervention services and individualized education;
- speech/language, occupational, and physical therapy;
- neuropsychological evaluation and behavioral therapy;
- standard evidence-based treatment of ADHD, anxiety, aggression, autism-associated needs, constipation, seizures, orthopedic problems, and sleep disorders when present;
- longitudinal BMI, blood pressure, glucose/HbA1c, lipids, liver-health, nutrition, activity, and sleep surveillance;
- family support and genetic counseling.

Suggested NCIt intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Speech and Language Therapy**, **Behavioral Therapy**, **Nutritional Counseling**, and **Weight Management**; current NCIt codes should be validated before ingestion.

No response rate, syndrome-specific adverse-event profile, pharmacogenomic rule, gene therapy, ASO/siRNA therapy, cell therapy, CRISPR intervention, or targeted melanocortin therapy has been clinically established. Although POMC repression suggests a melanocortin-pathway rationale, extrapolating efficacy of drugs used for other genetic obesities would be premature without CHUJANS trials. (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 10-11)

**Current implementation:** Simons Searchlight, **NCT01238250**, is a recruiting, international, prospective observational registry with a planned enrollment of 100,000. It collects medical, developmental, learning, behavioral, and annual longitudinal data plus blood/saliva from eligible neurodevelopmental genetic conditions, including PHIP-related disorders. It is not an interventional treatment trial. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT01238250). (NCT01238250 chunk 1, NCT01238250 chunk 2)

## 13. Prevention

The de novo occurrence of many pathogenic variants means there is no lifestyle-based primary prevention. Relevant prevention is genetic and complication-focused:

- **Primary/reproductive:** genetic counseling, parental testing, prenatal diagnosis, and preimplantation genetic testing when a familial pathogenic variant is known.
- **Secondary:** early molecular diagnosis and prompt developmental, speech, behavioral, and nutritional intervention; cascade testing of relatives.
- **Tertiary:** prevent obesity-related metabolic disease, injuries related to hypotonia/coordination, untreated seizures, constipation complications, and avoidable educational or psychiatric deterioration.

There is no vaccine, antimicrobial prophylaxis, population screening program, or environmental intervention specific to CHUJANS. An apparently de novo result does not reduce recurrence risk to absolute zero because parental germline mosaicism remains possible.

## 14. Other species and natural disease

No naturally occurring PHIP-related CHUJANS analogue was identified in companion animals, livestock, or wildlife, and no breed-specific VBO annotation is currently justified. There is no zoonotic potential or cross-species transmission. PHIP is evolutionarily conserved, permitting comparative functional modeling, but conservation alone does not establish natural veterinary disease.

## 15. Model organisms

### Mouse

A **Phip-null mouse** has severe postnatal phenotypes: approximately **40% growth deficit by weaning**, hypoglycemia, and death at 4–5 weeks. This supports an essential role in growth and metabolic homeostasis. However, complete knockout is much more severe than typical heterozygous human CHUJANS and does not faithfully reproduce the human obesity phenotype; it is therefore informative for gene function but limited as a therapeutic model. (marenne2020exomesequencingidentifies pages 6-8)

### Cellular models

HEK293 POMC-luciferase assays and COS-7 localization experiments currently provide the strongest variant-level functional platform. They demonstrate impaired POMC transcription, altered localization, and dominant-negative behavior for selected variants. Limitations include overexpression, non-neuronal cell backgrounds, and absence of authentic hypothalamic circuitry. (marenne2020exomesequencingidentifies pages 5-6, marenne2020exomesequencingidentifies pages 20-21)

No well-validated PHIP-specific zebrafish, Drosophila, C. elegans, patient-derived iPSC neuron, brain organoid, conditional hypothalamic knockout, or humanized knock-in model was identified in the retrieved evidence. Priority models would include heterozygous LoF and patient-specific knock-in mice, POMC-neuron conditional models, and patient iPSC-derived neurons/hypothalamic organoids.

## Research priorities and expert assessment

The authoritative interpretation emerging from current evidence is that CHUJANS is a clinically recognizable but underdiagnosed PHIP dosage disorder with broader expressivity than the original “ID-obesity” label implies. Obesity is important but not obligatory; inherited mildly affected cases mean that trio analysis and careful parental phenotyping are essential. The 2023 investigators specifically recommended including PHIP in diagnostic testing for developmental delay/intellectual disability, behavioral abnormalities, and obesity, and emphasized behavioral and weight follow-up. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11, kampmeier2023phipassociatedchungjansensyndrome pages 1-2)

The highest-priority gaps are: population prevalence; prospective childhood-to-adult natural history; penetrance by variant class; standardized neurobehavioral and quality-of-life outcomes; direct functional studies in human neurons; validation of the methylation signature; and interventional studies addressing obesity and behavior. Registry participation through Simons Searchlight is presently the most concrete implementation for overcoming the small-cohort problem. (NCT01238250 chunk 1, NCT01238250 chunk 2)

References

1. (kampmeier2023phipassociatedchungjansensyndrome pages 2-3): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

2. (kampmeier2023phipassociatedchungjansensyndrome pages 1-2): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

3. (marenne2020exomesequencingidentifies pages 5-6): Gaëlle Marenne, Audrey E. Hendricks, Aliki Perdikari, Rebecca Bounds, Felicity Payne, Julia M. Keogh, Christopher J. Lelliott, Elana Henning, Saad Pathan, Sofie Ashford, Elena G. Bochukova, Vanisha Mistry, Allan Daly, Caroline Hayward, Nicholas J. Wareham, Stephen O’Rahilly, Claudia Langenberg, Eleanor Wheeler, Eleftheria Zeggini, I. Sadaf Farooqi, and Inês Barroso. Exome sequencing identifies genes and gene sets contributing to severe childhood obesity, linking phip variants to repressed pomc transcription. Cell Metabolism, 31:1107-1119.e12, Jun 2020. URL: https://doi.org/10.1016/j.cmet.2020.05.007, doi:10.1016/j.cmet.2020.05.007. This article has 92 citations and is from a highest quality peer-reviewed journal.

4. (marenne2020exomesequencingidentifies pages 10-11): Gaëlle Marenne, Audrey E. Hendricks, Aliki Perdikari, Rebecca Bounds, Felicity Payne, Julia M. Keogh, Christopher J. Lelliott, Elana Henning, Saad Pathan, Sofie Ashford, Elena G. Bochukova, Vanisha Mistry, Allan Daly, Caroline Hayward, Nicholas J. Wareham, Stephen O’Rahilly, Claudia Langenberg, Eleanor Wheeler, Eleftheria Zeggini, I. Sadaf Farooqi, and Inês Barroso. Exome sequencing identifies genes and gene sets contributing to severe childhood obesity, linking phip variants to repressed pomc transcription. Cell Metabolism, 31:1107-1119.e12, Jun 2020. URL: https://doi.org/10.1016/j.cmet.2020.05.007, doi:10.1016/j.cmet.2020.05.007. This article has 92 citations and is from a highest quality peer-reviewed journal.

5. (kampmeier2023phipassociatedchungjansensyndrome pages 3-5): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

6. (kampmeier2023phipassociatedchungjansensyndrome pages 10-11): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

7. (marenne2020exomesequencingidentifies pages 1-3): Gaëlle Marenne, Audrey E. Hendricks, Aliki Perdikari, Rebecca Bounds, Felicity Payne, Julia M. Keogh, Christopher J. Lelliott, Elana Henning, Saad Pathan, Sofie Ashford, Elena G. Bochukova, Vanisha Mistry, Allan Daly, Caroline Hayward, Nicholas J. Wareham, Stephen O’Rahilly, Claudia Langenberg, Eleanor Wheeler, Eleftheria Zeggini, I. Sadaf Farooqi, and Inês Barroso. Exome sequencing identifies genes and gene sets contributing to severe childhood obesity, linking phip variants to repressed pomc transcription. Cell Metabolism, 31:1107-1119.e12, Jun 2020. URL: https://doi.org/10.1016/j.cmet.2020.05.007, doi:10.1016/j.cmet.2020.05.007. This article has 92 citations and is from a highest quality peer-reviewed journal.

8. (kampmeier2023phipassociatedchungjansensyndrome pages 12-13): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

9. (kampmeier2023phipassociatedchungjansensyndrome pages 11-12): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

10. (NCT01238250 chunk 1):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

11. (NCT01238250 chunk 2):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

12. (kampmeier2023phipassociatedchungjansensyndrome pages 5-5): Antje Kampmeier, Elsa Leitão, Ilaria Parenti, Jasmin Beygo, Christel Depienne, Nuria C Bramswig, Tzung-Chien Hsieh, Alexandra Afenjar, Stefanie Beck-Wödl, Ute Grasshoff, Tobias B Haack, Emilia K Bijlsma, Claudia Ruivenkamp, Eva Lausberg, Miriam Elbracht, Maria K Haanpää, Hannele Koillinen, Uwe Heinrich, Imma Rost, Rami Abou Jamra, Denny Popp, Margarete Koch-Hogrebe, Kevin Rostasy, Vanesa López-González, María José Sanchez-Soler, Catarina Macedo, Ariane Schmetz, Carmen Steinborn, Sabine Weidensee, Hellen Lesmann, Felix Marbach, Pilar Caro, Christian P. Schaaf, Peter Krawitz, Dagmar Wieczorek, Frank J Kaiser, and Alma Kuechler. Phip-associated chung-jansen syndrome: report of 23 new individuals. Frontiers in Cell and Developmental Biology, Jan 2023. URL: https://doi.org/10.3389/fcell.2022.1020609, doi:10.3389/fcell.2022.1020609. This article has 24 citations.

13. (loid2026anovelphip pages 5-6): Petra Loid, Nina Vuorela, Kirsimari Aaltonen, Juha Kuittinen, and Outi Mäkitie. A novel phip variant in a family with severe early-onset obesity. Hormone research in paediatrics, pages 1-15, Oct 2026. URL: https://doi.org/10.1159/000542205, doi:10.1159/000542205. This article has 5 citations and is from a peer-reviewed journal.

14. (loid2026anovelphip pages 7-8): Petra Loid, Nina Vuorela, Kirsimari Aaltonen, Juha Kuittinen, and Outi Mäkitie. A novel phip variant in a family with severe early-onset obesity. Hormone research in paediatrics, pages 1-15, Oct 2026. URL: https://doi.org/10.1159/000542205, doi:10.1159/000542205. This article has 5 citations and is from a peer-reviewed journal.

15. (marenne2020exomesequencingidentifies pages 20-21): Gaëlle Marenne, Audrey E. Hendricks, Aliki Perdikari, Rebecca Bounds, Felicity Payne, Julia M. Keogh, Christopher J. Lelliott, Elana Henning, Saad Pathan, Sofie Ashford, Elena G. Bochukova, Vanisha Mistry, Allan Daly, Caroline Hayward, Nicholas J. Wareham, Stephen O’Rahilly, Claudia Langenberg, Eleanor Wheeler, Eleftheria Zeggini, I. Sadaf Farooqi, and Inês Barroso. Exome sequencing identifies genes and gene sets contributing to severe childhood obesity, linking phip variants to repressed pomc transcription. Cell Metabolism, 31:1107-1119.e12, Jun 2020. URL: https://doi.org/10.1016/j.cmet.2020.05.007, doi:10.1016/j.cmet.2020.05.007. This article has 92 citations and is from a highest quality peer-reviewed journal.

16. (marenne2020exomesequencingidentifies pages 6-8): Gaëlle Marenne, Audrey E. Hendricks, Aliki Perdikari, Rebecca Bounds, Felicity Payne, Julia M. Keogh, Christopher J. Lelliott, Elana Henning, Saad Pathan, Sofie Ashford, Elena G. Bochukova, Vanisha Mistry, Allan Daly, Caroline Hayward, Nicholas J. Wareham, Stephen O’Rahilly, Claudia Langenberg, Eleanor Wheeler, Eleftheria Zeggini, I. Sadaf Farooqi, and Inês Barroso. Exome sequencing identifies genes and gene sets contributing to severe childhood obesity, linking phip variants to repressed pomc transcription. Cell Metabolism, 31:1107-1119.e12, Jun 2020. URL: https://doi.org/10.1016/j.cmet.2020.05.007, doi:10.1016/j.cmet.2020.05.007. This article has 92 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Chung-Jansen_Syndrome-deep-research-falcon_artifacts/artifact-00.md)