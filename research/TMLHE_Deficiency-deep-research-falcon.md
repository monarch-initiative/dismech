---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-06T15:29:56.847236'
end_time: '2026-08-06T15:36:33.059238'
duration_seconds: 396.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: epsilon-trimethyllysine hydroxylase deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 9
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: TMLHE_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** epsilon-trimethyllysine hydroxylase deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **epsilon-trimethyllysine hydroxylase deficiency** covering all of the
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
- **Disease Name:** epsilon-trimethyllysine hydroxylase deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **epsilon-trimethyllysine hydroxylase deficiency** covering all of the
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


# Epsilon-N-trimethyllysine hydroxylase deficiency: disease-characteristics report

## Executive assessment

**Epsilon-N-trimethyllysine hydroxylase deficiency (TMLHE deficiency)** is an X-linked defect in the first reaction of endogenous L-carnitine biosynthesis. The biochemical phenotype—loss of TMLHE function with accumulation of its substrate, trimethyllysine—is substantially better established than the clinical syndrome. Published human observations associate hemizygous loss-of-function variants with autism spectrum disorder (ASD), intellectual disability (ID), or regressive developmental symptoms, but penetrance is very low and unaffected deficient males occur. It should therefore be represented cautiously as an **X-linked biochemical deficiency and proposed neurodevelopmental susceptibility condition**, not as a uniformly penetrant monogenic cause of autism. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 1-2)

| domain | established finding | evidence strength | suggested ontology/database annotation |
|---|---|---|---|
| Identity | Epsilon-N-trimethyllysine hydroxylase deficiency refers to deficiency of TMLHE, the enzyme catalyzing the first step of endogenous carnitine biosynthesis; current human literature supports a biochemical defect and possible neurodevelopmental risk state rather than a uniformly defined, fully penetrant Mendelian syndrome (nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 1-2) | Moderate for biochemical identity; low-moderate for syndrome definition | Gene: **TMLHE**; pathway/database: carnitine biosynthesis; disease ontology term/ID: **MONDO ID verification needed** |
| Gene / locus / inheritance | **TMLHE** is located on **Xq28**; reported pathogenic or likely deleterious events are **germline** hemizygous variants/deletions in males, consistent with **X-linked** inheritance (nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 4-5) | Moderate | HGNC: **TMLHE**; chromosomal location: **Xq28**; inheritance: **X-linked inheritance (HP:0001417)** |
| Molecular defect | Reported human variants include **c.229C>T (p.Arg77\*)**, **c.730G>C (p.Asp244His)**, and **c.1107G>T / p.Glu369Asp**; functional work indicated **loss of function**, including markedly reduced mRNA for the nonsense allele (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 4-5) | Moderate | Variant classes: nonsense, missense, exon deletion; sequence databases: ClinVar/OMIM **ID verification needed** |
| Biochemical defect | Deficiency blocks the first step of carnitine biosynthesis from trimethyllysine, producing substrate accumulation; plasma **trimethyllysine (TML)** was increased about **2-3-fold** in affected individuals, while free carnitine was mildly decreased or within normal range in reported cases (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9) | Moderate | CHEBI: **L-carnitine (CHEBI:16347)**; metabolite term for trimethyllysine: **CHEBI ID verification needed** |
| Biomarkers | Most established biomarker is **elevated plasma trimethyllysine**; reduced TMLHE transcript/protein activity is supportive in research settings; carnitine concentration alone may be insensitive because endogenous synthesis contributes only part of total body carnitine supply (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 9-9) | Moderate for TML; low for broader biomarker panel | Laboratory abnormality annotation: elevated trimethyllysine **HPO term/ID verification needed**; metabolomics/database: targeted plasma amino-acid/acylcarnitine or LC-MS/MS profiling |
| Reported phenotypes | Human reports link TMLHE deficiency/variants mainly to **autism spectrum disorder** and sometimes **intellectual disability**, especially in affected males from multiplex autism families; evidence supports susceptibility association, not phenotype specificity (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 1-2, nava2012analysisofthe pages 4-5) | Low-moderate | HPO: **Autistic behavior (HP:0000729)**; **Intellectual disability (HP:0001249)** |
| Penetrance / prevalence caveat | Available evidence indicates **low penetrance** for neurodevelopmental disease. One study cited exon 2 deletion in **3/691 ASD males vs 1/896 male controls** and estimated penetrance around **2-4%**; statistical support was limited and authors treated TMLHE deficiency as a **risk factor/susceptibility factor**, not a deterministic cause (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9) | Moderate for caveat; low for precise penetrance | Population genetics resources: gnomAD/ClinVar **ID verification needed**; disease characterization: susceptibility/risk factor annotation rather than fully penetrant monogenic disease |
| Diagnosis | Best-supported diagnostic approach is **molecular testing of TMLHE** together with **targeted biochemical testing** showing elevated plasma trimethyllysine; array CGH/exome sequencing can detect exon deletions or sequence variants (nava2012analysisofthe pages 1-2, nava2012analysisofthe pages 4-5) | Moderate | Testing modalities: single-gene sequencing, exome sequencing, CNV analysis/array CGH; GTR/OMIM **ID verification needed** |
| Treatment evidence | No established standard therapy or trial-supported disease-modifying treatment was identified. Literature cited a **single case report** describing improvement in regressive autism symptoms after **L-carnitine supplementation**, but this remains **case-level, non-confirmatory evidence** (carillo2020lcarnitineindrosophila pages 14-15) | Low | NCIT: **Levocarnitine / L-carnitine ID verification needed**; supportive care annotation |
| Prognosis | Natural history, long-term outcomes, mortality, and genotype-phenotype correlations are **not well established** because published human cases are few and phenotypes are heterogeneous (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9) | Low | Prognosis/natural history: **data not established** |
| Model / mechanistic context | Mechanistic interpretation centers on reduced endogenous carnitine biosynthesis and possible downstream effects on mitochondrial fatty-acid oxidation/brain energetics; Drosophila and other model discussions provide biologic plausibility, but direct disease-model evidence specific to human TMLHE deficiency is limited in the retrieved evidence (carillo2020lcarnitineindrosophila pages 14-15) | Low-moderate | GO biological process: **carnitine biosynthetic process**; cellular component/process IDs **verification needed** |
| Major unknowns | Unresolved issues include whether TMLHE deficiency constitutes a distinct Mendelian disease entity, true population prevalence, full biomarker spectrum beyond TML, penetrance modifiers, sex-specific expressivity, treatment responsiveness, and whether newborn or carrier screening is clinically justified (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, carillo2020lcarnitineindrosophila pages 14-15) | High confidence that these are unknowns | Knowledge-base flags: evidence gap; **ID verification needed** for disease ontology mapping |


*Table: This compact table summarizes what is currently established, uncertain, and clinically actionable about epsilon-N-trimethyllysine hydroxylase deficiency. It is designed for direct use in a disease knowledge base, with evidence strength and suggested ontology/database annotations.*

## 1. Disease information

### Definition and nomenclature

The preferred biochemical name is **epsilon-N-trimethyllysine hydroxylase deficiency**; common alternatives include **ε-N-trimethyllysine hydroxylase deficiency**, **trimethyllysine hydroxylase epsilon deficiency**, **TMLHE deficiency**, and **X-linked carnitine-biosynthesis deficiency**. TMLHE is at Xq28 and encodes the enzyme catalyzing hydroxylation of protein-derived N6,N6,N6-trimethyllysine, the first committed reaction in endogenous carnitine synthesis. (nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 4-5)

No dedicated MONDO, Orphanet, ICD-10/11, or MeSH identifier was verified from the retrieved evidence. For knowledge-base purposes, these fields should be marked **not verified/not specifically assigned**, rather than mapping the condition directly to autism. OMIM, ClinVar, HGNC, and current MONDO releases should be checked at ingestion time. The available information is primarily **aggregated from published families, case-control cohorts, functional assays, and one treatment case report**, not from EHR-scale natural-history data.

### Foundational primary evidence

Nava et al., published October 2012, reported a TMLHE nonsense variant in two brothers with autism and ID and two additional missense substitutions after screening 501 males with ASD. The abstract states: **“Functional analyses confirmed that the mutations were associated with a loss-of-function and led to an increase in trimethyllysine, the precursor of carnitine biosynthesis, in the plasma of patients.”** DOI: https://doi.org/10.1038/tp.2012.102. (nava2012analysisofthe pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

The primary cause of the biochemical deficiency is a **germline hemizygous loss-of-function alteration in TMLHE in a male**. Reported classes include exon-level deletions, nonsense variants, and functionally damaging missense variants. In females, heterozygosity and X-inactivation are expected to modulate biochemical expression, but clinical penetrance has not been quantified. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9)

Reported variants include **c.229C>T (p.Arg77\*)**, **c.730G>C (p.Asp244His)**, and **c.1107G>T (p.Glu369Asp)**. The p.Arg77\* allele was absent from 508 tested healthy male controls; functional studies showed markedly reduced transcript, consistent with nonsense-mediated decay. The reported variants increased plasma trimethyllysine, supporting loss of enzyme activity. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 4-5)

TMLHE deficiency is best interpreted as a **risk factor requiring additional modifiers**, rather than a sufficient cause of ASD. One study estimated only 2–4% penetrance of ASD for an exon-2 deletion and observed it in 3/691 males with ASD versus 1/896 male controls; this difference was not statistically significant (reported P=0.3). These data strongly caution against classifying every hemizygous deletion as clinically pathogenic solely on the basis of ASD risk. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9)

No replicated genetic protective variant, modifier gene, environmental toxin, infection, lifestyle risk factor, or protective exposure has been established. Diet is a biologically plausible modifier because only about 25% of the human carnitine pool is synthesized endogenously, with most supplied by food; consequently, low dietary carnitine during a developmental window has been proposed to unmask risk. This remains a hypothesis, not a proven gene–environment interaction. (nava2012analysisofthe pages 9-9)

## 3. Phenotypes

The reported clinical phenotype is predominantly neurodevelopmental and highly variable:

- **Autistic behavior / ASD** — suggested HPO: **HP:0000729, Autistic behavior**. Onset is in early childhood by ASD diagnostic convention, but TMLHE-specific onset distributions and frequencies are unavailable.
- **Intellectual disability** — **HP:0001249**. Moderate ID was reported in brothers carrying p.Arg77\*; ID is not demonstrably universal. (nava2012analysisofthe pages 1-2, nava2012analysisofthe pages 4-5)
- **Developmental regression** — suggested HPO: **HP:0002376, Developmental regression**. This is supported principally by the published treatment case rather than a cohort. (carillo2020lcarnitineindrosophila pages 14-15)
- **Elevated plasma trimethyllysine** — laboratory abnormality; a dedicated HPO identifier should be verified. Approximately two- to threefold elevation was observed in reported affected males. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9)
- **Mildly reduced free carnitine** — suggested HPO family: abnormal circulating carnitine concentration, exact term verification required. Carnitine could remain within the reference interval, so it is not a sensitive stand-alone phenotype. (nava2012analysisofthe pages 7-9)

There is no reliable percentage for any clinical feature among all biochemically deficient individuals. Severity ranges from apparently unaffected to autism with ID or regression. Progression, episodicity, adult phenotype, and disease-specific quality-of-life scores have not been studied. Any QoL burden should be attributed to the person’s neurodevelopmental phenotype rather than presumed from TMLHE genotype alone.

## 4. Genetic and molecular information

**Causal/susceptibility gene:** **TMLHE**, Xq28. HGNC and NCBI Gene numeric identifiers should be verified against current releases. The implicated alleles are germline; there is no evidence that somatic TMLHE variants cause this condition. (nava2012analysisofthe pages 7-9)

Functional consequence is principally **loss of function**. Reported evidence includes substrate accumulation, approximately tenfold reduction of TMLHE mRNA in affected cells, and restoration of nonsense-transcript abundance by the nonsense-mediated-decay inhibitor emetine in vitro. Emetine was a mechanistic experiment, not a therapy. (nava2012analysisofthe pages 9-10)

Variant classifications must be assigned allele by allele using current ClinVar/ACMG evidence. Because the neurodevelopmental association is incompletely penetrant, “pathogenic for biochemical TMLHE deficiency” and “pathogenic for ASD” are not equivalent assertions. Population allele frequencies should be drawn directly from the current gnomAD version; the retrieved study noted only 18 nonsynonymous variants among approximately 48,700 X chromosomes in then-available databases, but this historical figure should not replace current allele-frequency data. (nava2012analysisofthe pages 7-9)

No validated modifier gene, disease-specific epigenetic signature, recurrent translocation, aneuploidy, dominant-negative mechanism, or gain-of-function mechanism has been established. Exon deletions are the principal relevant structural abnormality.

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, occupational exposures, smoking, alcohol, or infectious agents cause TMLHE deficiency. Dietary carnitine is mechanistically relevant because it can bypass endogenous synthesis, but neither a minimum protective intake nor a high-risk dietary pattern has been established. The disease is noninfectious and nontransmissible. (nava2012analysisofthe pages 9-9)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** hemizygous loss-of-function TMLHE variant or exon deletion.
2. **Primary biochemical lesion:** deficient ε-N-trimethyllysine hydroxylation, blocking the first step of endogenous carnitine synthesis.
3. **Direct biomarker:** accumulation of trimethyllysine; reported plasma levels were approximately two- to threefold above controls.
4. **Downstream metabolic hypothesis:** reduced endogenous carnitine availability may constrain mitochondrial import of long-chain fatty acyl groups and β-oxidation, particularly when dietary carnitine is inadequate.
5. **Proposed tissue consequence:** altered neuronal/glial bioenergetics or neuromodulation during brain development.
6. **Possible manifestation:** ASD, ID, or developmental regression in a small, incompletely penetrant subset. Steps 1–3 are demonstrated in humans; steps 4–6 remain incompletely validated as a causal chain. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, nava2012analysisofthe pages 9-9)

Relevant suggested annotations include **carnitine biosynthetic process**, **fatty-acid beta-oxidation**, **mitochondrial fatty-acid transport**, and **cellular energy homeostasis**; exact GO identifiers should be validated before database loading. Suggested cellular compartment is the **mitochondrion** (GO:0005739) for downstream carnitine-shuttle biology, although TMLHE’s own subcellular localization should be annotated from reviewed UniProt rather than inferred. Suggested chemicals are **L-carnitine (CHEBI:16347)** and N6,N6,N6-trimethyl-L-lysine (CHEBI identifier verification required).

No TMLHE-deficiency-specific immune, inflammatory, fibrotic, apoptotic, single-cell, spatial-transcriptomic, proteomic, lipidomic, epigenomic, organoid, or CRISPR-screen signature has been established. The most informative molecular profile currently is targeted metabolomics.

## 7. Anatomical structures affected

The **brain/nervous system** is implicated clinically by ASD and ID, but no reproducible neuroanatomical lesion or laterality is known. Suggested anatomy includes **brain (UBERON:0000955)** and broader central nervous system annotations. Candidate cell types include **neuron (CL:0000540)** and glial cells, but direct cell-type-specific human evidence is absent.

Liver, kidney, and brain participate in endogenous carnitine synthesis, whereas mitochondrial fatty-acid oxidation is systemic. Nevertheless, no primary hepatic, renal, cardiac, skeletal-muscle, or pathological tissue injury has been established in TMLHE-deficient people. (nava2012analysisofthe pages 9-9)

## 8. Temporal development

Clinical onset, when present, appears pediatric and neurodevelopmental. Regression has been reported in an individual case, but no stages, progression rate, remission pattern, lifespan trajectory, or critical treatment window has been established. A prenatal/early-childhood vulnerability window is biologically plausible but unproven. The biochemical genotype is lifelong; the clinical course may remain asymptomatic because penetrance is low.

## 9. Inheritance and population

Inheritance is **X-linked**, with hemizygous males showing the clearest biochemical effect. Suggested HPO inheritance term: **HP:0001417, X-linked inheritance**. Female heterozygotes may have intermediate metabolite effects depending on X-inactivation, but clinical penetrance is undefined. (nava2012analysisofthe pages 7-9)

The frequently cited exon-2 deletion has been described as relatively common—approximately 1 in 350 males in earlier literature—yet neurodevelopmental penetrance was estimated at only 2–4%. The directly retrieved case-control data were 3/691 ASD males versus 1/896 male controls and were nonsignificant. Thus, carrier/deficiency frequency must not be equated with disease prevalence. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9)

Incidence, prevalence of symptomatic disease, sex ratio among symptomatic carriers, founder effects, consanguinity contribution, anticipation, germline mosaicism, ethnicity-specific risk, and geographic distribution are unknown. X-linked transmission rather than consanguinity is the principal counseling consideration.

## 10. Diagnostics

### Recommended approach

1. Establish the clinical indication, such as ASD/ID/regression plus a suggestive family history or incidental TMLHE finding.
2. Perform **targeted plasma LC–MS/MS** for trimethyllysine and carnitine; where available, include downstream carnitine-biosynthesis intermediates.
3. Test **TMLHE** by sequencing plus exon-level deletion/duplication analysis. Exome sequencing may detect coding variants but can miss single-exon CNVs without validated CNV calling; genome sequencing or chromosomal microarray may identify larger deletions.
4. Confirm segregation and maternal carrier status.
5. Interpret genotype jointly with the biochemical phenotype and avoid assigning ASD causality from genotype alone. (nava2012analysisofthe pages 1-2, nava2012analysisofthe pages 4-5)

Plasma trimethyllysine is the strongest reported biomarker. Free carnitine may be only mildly reduced and remain normal. Enzyme/transcript assays are research-level tests. MRI, EEG, EMG, ECG, biopsy, histopathology, karyotype, FISH, mitochondrial DNA analysis, and repeat-expansion testing have no disease-specific diagnostic role unless independently indicated.

Differential diagnoses include primary systemic carnitine deficiency due to **SLC22A5**, other carnitine-biosynthesis defects, nutritional carnitine deficiency, organic acidemias with secondary carnitine depletion, fatty-acid oxidation disorders, and the broad genetic differential of ASD/ID. Unlike primary carnitine-transporter deficiency, TMLHE deficiency is characterized most specifically by upstream trimethyllysine accumulation and may not cause profound systemic carnitine depletion.

No standardized clinical diagnostic criteria or population newborn-screening program exists. Cascade biochemical/genetic testing may be considered in a family with a confirmed variant, with counseling about uncertain and low neurodevelopmental penetrance.

## 11. Outcome and prognosis

There are no survival curves, mortality rates, life-expectancy estimates, validated disability outcomes, or prognostic biomarkers. No evidence shows that isolated biochemical deficiency shortens life. Morbidity, when present, is dominated by ASD, ID, and possible regression. Prognosis should therefore be individualized according to developmental functioning and comorbidities rather than inferred from TMLHE status. Natural-history cohorts are a major unmet need.

## 12. Treatment

**L-carnitine/levocarnitine supplementation** is a rational bypass therapy, but evidence is limited. A 2015 case report described improvement of regressive autism symptoms after carnitine supplementation; this is uncontrolled, subject to placebo and developmental-course effects, and does not establish efficacy, dose optimization, treatment window, or response rate. (carillo2020lcarnitineindrosophila pages 14-15)

Accordingly:

- There is no approved TMLHE-specific therapy, consensus algorithm, or randomized trial.
- Treatment should not be presented as proven to prevent or reverse autism.
- If clinically attempted, it should be supervised by a metabolic specialist with baseline and follow-up developmental measures, plasma carnitine/metabolites, dose documentation, adherence, and adverse-event surveillance.
- Standard ASD/ID care—developmental pediatrics, speech-language therapy, occupational therapy, behavioral/educational support, and management of comorbidities—remains essential.

Suggested intervention annotations are **levocarnitine/L-carnitine supplementation** and developmental rehabilitation; current NCIT identifiers should be verified. Emetine is not a therapeutic candidate despite its in-vitro effect on nonsense-mediated decay. No gene therapy, editing, RNA therapy, cell therapy, surgery, immunotherapy, or pharmacogenomic strategy is established. The tool search identified no relevant registered disease-specific interventional trial.

## 13. Prevention

The genetic defect itself cannot currently be prevented by lifestyle modification. Primary prevention options are reproductive: genetic counseling, carrier testing of at-risk female relatives, prenatal diagnosis, and preimplantation genetic testing after confirmation of a familial variant. Counseling must emphasize low and uncertain clinical penetrance.

Secondary prevention through newborn or general-population screening is not currently justified by validated evidence. Targeted early testing may be reasonable in informative families, but proof that presymptomatic carnitine prevents neurodevelopmental disease is lacking. Tertiary prevention consists of early developmental assessment and support and, if supplementation is undertaken, specialist monitoring. Vaccination, infectious prophylaxis, environmental remediation, and public-health isolation are not applicable.

## 14. Other species and natural disease

No naturally occurring veterinary TMLHE-deficiency syndrome, breed predisposition, zoonotic potential, or cross-species transmission was established in the retrieved literature. Orthologues and pathway conservation are expected across animals, but NCBI Gene, Taxon, OMIA, and VBO identifiers should be verified directly before annotation.

## 15. Model organisms

Drosophila can synthesize L-carnitine and possesses a transport system broadly analogous to the human pathway. Fly studies support roles for carnitine metabolism in glial fatty-acid oxidation, energy homeostasis, and neurodegeneration; however, these are pathway models rather than a validated model recapitulating the low-penetrance human TMLHE-ASD phenotype. (carillo2020lcarnitineindrosophila pages 14-15)

The appropriate model hierarchy would include TMLHE-null cell lines for metabolite rescue, patient-derived induced pluripotent stem-cell neurons/glia, and conditional animal knockouts exposed to defined carnitine diets. Such systems could test whether dietary carnitine modifies brain energetics and behavior. At present, no model provides validated prediction of human clinical response.

## Recent developments and evidence gaps

The 2023–2024 literature has expanded interest in metabolic testing and carnitine-related signatures in autism, but it has not supplied a disease-specific prospective TMLHE cohort, randomized treatment trial, definitive penetrance estimate, or validated newborn-screening marker panel. The core disease-specific evidence therefore remains the 2011–2015 genetic, biochemical, and case-report literature. This absence of recent confirmatory studies is itself important: clinical interpretation should remain conservative.

### Knowledge-base conclusion

The most defensible entry is: **“X-linked TMLHE loss-of-function biochemical deficiency, characterized by elevated trimethyllysine and proposed as a low-penetrance susceptibility factor for autism/intellectual disability.”** The evidence is strong for gene-to-enzyme-to-metabolite causation, moderate-to-weak for gene-to-neurodevelopmental-phenotype causation, and very weak for treatment efficacy. Major unresolved fields are symptomatic prevalence, modifiers, natural history, diagnostic thresholds, and prospective benefit of early carnitine supplementation. (nava2012analysisofthe pages 9-10, nava2012analysisofthe pages 7-9, carillo2020lcarnitineindrosophila pages 14-15)

References

1. (nava2012analysisofthe pages 9-10): C. Nava, F. Lamari, D. Heron, C. Mignot, Agnès Rastetter, Agnès Rastetter, Agnès Rastetter, B. Keren, D. Cohen, A. Faudet, D. Bouteiller, M. Gilleron, A. Jacquette, S. Whalen, A. Afenjar, D. Perisse, Claudine Laurent, Claudine Laurent, C. Dupuits, C. Gautier, C. Gautier, M. Gérard, G. Huguet, G. Huguet, S. Caillet, B. Leheup, M. Leboyer, C. Gillberg, R. Delorme, T. Bourgeron, T. Bourgeron, A. Brice, and C. Depienne. Analysis of the chromosome x exome in patients with autism spectrum disorders identified novel candidate genes, including tmlhe. Translational Psychiatry, 2:e179-e179, Oct 2012. URL: https://doi.org/10.1038/tp.2012.102, doi:10.1038/tp.2012.102. This article has 146 citations and is from a peer-reviewed journal.

2. (nava2012analysisofthe pages 7-9): C. Nava, F. Lamari, D. Heron, C. Mignot, Agnès Rastetter, Agnès Rastetter, Agnès Rastetter, B. Keren, D. Cohen, A. Faudet, D. Bouteiller, M. Gilleron, A. Jacquette, S. Whalen, A. Afenjar, D. Perisse, Claudine Laurent, Claudine Laurent, C. Dupuits, C. Gautier, C. Gautier, M. Gérard, G. Huguet, G. Huguet, S. Caillet, B. Leheup, M. Leboyer, C. Gillberg, R. Delorme, T. Bourgeron, T. Bourgeron, A. Brice, and C. Depienne. Analysis of the chromosome x exome in patients with autism spectrum disorders identified novel candidate genes, including tmlhe. Translational Psychiatry, 2:e179-e179, Oct 2012. URL: https://doi.org/10.1038/tp.2012.102, doi:10.1038/tp.2012.102. This article has 146 citations and is from a peer-reviewed journal.

3. (nava2012analysisofthe pages 1-2): C. Nava, F. Lamari, D. Heron, C. Mignot, Agnès Rastetter, Agnès Rastetter, Agnès Rastetter, B. Keren, D. Cohen, A. Faudet, D. Bouteiller, M. Gilleron, A. Jacquette, S. Whalen, A. Afenjar, D. Perisse, Claudine Laurent, Claudine Laurent, C. Dupuits, C. Gautier, C. Gautier, M. Gérard, G. Huguet, G. Huguet, S. Caillet, B. Leheup, M. Leboyer, C. Gillberg, R. Delorme, T. Bourgeron, T. Bourgeron, A. Brice, and C. Depienne. Analysis of the chromosome x exome in patients with autism spectrum disorders identified novel candidate genes, including tmlhe. Translational Psychiatry, 2:e179-e179, Oct 2012. URL: https://doi.org/10.1038/tp.2012.102, doi:10.1038/tp.2012.102. This article has 146 citations and is from a peer-reviewed journal.

4. (nava2012analysisofthe pages 4-5): C. Nava, F. Lamari, D. Heron, C. Mignot, Agnès Rastetter, Agnès Rastetter, Agnès Rastetter, B. Keren, D. Cohen, A. Faudet, D. Bouteiller, M. Gilleron, A. Jacquette, S. Whalen, A. Afenjar, D. Perisse, Claudine Laurent, Claudine Laurent, C. Dupuits, C. Gautier, C. Gautier, M. Gérard, G. Huguet, G. Huguet, S. Caillet, B. Leheup, M. Leboyer, C. Gillberg, R. Delorme, T. Bourgeron, T. Bourgeron, A. Brice, and C. Depienne. Analysis of the chromosome x exome in patients with autism spectrum disorders identified novel candidate genes, including tmlhe. Translational Psychiatry, 2:e179-e179, Oct 2012. URL: https://doi.org/10.1038/tp.2012.102, doi:10.1038/tp.2012.102. This article has 146 citations and is from a peer-reviewed journal.

5. (nava2012analysisofthe pages 9-9): C. Nava, F. Lamari, D. Heron, C. Mignot, Agnès Rastetter, Agnès Rastetter, Agnès Rastetter, B. Keren, D. Cohen, A. Faudet, D. Bouteiller, M. Gilleron, A. Jacquette, S. Whalen, A. Afenjar, D. Perisse, Claudine Laurent, Claudine Laurent, C. Dupuits, C. Gautier, C. Gautier, M. Gérard, G. Huguet, G. Huguet, S. Caillet, B. Leheup, M. Leboyer, C. Gillberg, R. Delorme, T. Bourgeron, T. Bourgeron, A. Brice, and C. Depienne. Analysis of the chromosome x exome in patients with autism spectrum disorders identified novel candidate genes, including tmlhe. Translational Psychiatry, 2:e179-e179, Oct 2012. URL: https://doi.org/10.1038/tp.2012.102, doi:10.1038/tp.2012.102. This article has 146 citations and is from a peer-reviewed journal.

6. (carillo2020lcarnitineindrosophila pages 14-15): Maria Rosaria Carillo, Carla Bertapelle, Filippo Scialò, Mario Siervo, Gianrico Spagnuolo, Michele Simeone, Gianfranco Peluso, and Filomena Anna Digilio. L-carnitine in drosophila: a review. Antioxidants, 9:1310, Dec 2020. URL: https://doi.org/10.3390/antiox9121310, doi:10.3390/antiox9121310. This article has 40 citations.

## Artifacts

- [Edison artifact artifact-00](TMLHE_Deficiency-deep-research-falcon_artifacts/artifact-00.md)