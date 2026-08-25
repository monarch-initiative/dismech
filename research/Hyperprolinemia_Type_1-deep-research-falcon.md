---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-08T17:48:25.013489'
end_time: '2026-08-08T18:00:11.217268'
duration_seconds: 706.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hyperprolinemia Type 1
  mondo_id: ''
  category: Metabolic Disorder
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
  path: Hyperprolinemia_Type_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyperprolinemia Type 1
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Hyperprolinemia Type 1** covering all of the
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
- **Disease Name:** Hyperprolinemia Type 1
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Hyperprolinemia Type 1** covering all of the
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


# Hyperprolinemia Type 1: comprehensive disease-characteristics report

**Scope and evidence note.** Hyperprolinemia type 1 (HPI) is exceptionally rare, and the modern literature consists mainly of reviews, small case series, individual cases, mechanistic experiments, and studies of **22q11.2 deletion syndrome (22q11.2DS)**. The latter is not equivalent to isolated biallelic HPI: a 22q11.2 deletion removes one copy of **PRODH** together with many other genes. Psychiatric findings from 22q11.2DS therefore require cautious interpretation. No disease-specific 2023–2024 natural-history cohort or therapeutic trial with outcome data was identified.

The following table gives an evidence-weighted knowledge-base synopsis.

| Knowledge-base field | Summary | Ontology/identifier suggestions | Evidence status | Key citations |
|---|---|---|---|---|
| Disease / identifiers | Hyperprolinemia type 1 (HPI) is a rare inborn error of proline degradation caused by deficiency of proline dehydrogenase (PRODH, also called proline oxidase). It should be distinguished from hyperprolinemia type 2, which is due to ALDH4A1/P5CDH deficiency. Information here is disease-level, aggregated from literature and curated resources, not EHR-derived. | MONDO:0009400; MeSH/ICD/OMIM/Orphanet: verify in source database before KB ingestion | Established for disease concept and distinction from HPII | (OpenTargets Search: Hyperprolinemia type 1-PRODH, dalili2023clinicalfeaturesand pages 11-13, yao2022prolinemetabolismin pages 4-5) |
| Causal gene / inheritance | Primary causal gene: PRODH (proline dehydrogenase 1). Inheritance is autosomal recessive. Open Targets links HPI most strongly to PRODH; other associations are much weaker and not sufficient to assign causality. | Gene: PRODH; HGNC/Ensembl can be added from gene database; MONDO:0009400 | Established for PRODH and AR inheritance; uncertain for other candidate associations | (OpenTargets Search: Hyperprolinemia type 1-PRODH, dalili2023clinicalfeaturesand pages 11-13) |
| Biochemical defect | Loss or reduction of mitochondrial PRODH activity impairs oxidation of L-proline to P5C, disrupting the proline→P5C→glutamate pathway. Reported hallmark is elevated proline in plasma, CSF, and urine; urine may also contain glycine and hydroxyproline. Human reviews describe proline elevations up to ~10-fold above normal in PRODH defects. | GO suggestions: proline catabolic process; mitochondrial inner membrane; CHEBI: L-proline, glutamate | Established for elevated proline and pathway position; downstream neurotoxicity mechanisms remain partly inferred | (dalili2023clinicalfeaturesand pages 11-13, patriarca2021themultifacetedroles pages 6-9, cappelletti2018prolineoxidasecontrols pages 1-2, yao2022prolinemetabolismin pages 3-4) |
| Core phenotypes | Phenotype spectrum is highly variable: some individuals are asymptomatic, while reported manifestations include developmental delay/intellectual disability, behavioral problems, autism spectrum disorder, seizures/epilepsy, schizophrenia or schizoaffective phenotypes, nephropathy, and rare movement-disorder presentations. Nervous system involvement predominates in the literature. | HPO suggestions: Hyperprolinemia; Seizure; Developmental delay; Intellectual disability; Behavioral abnormality; Autism; Schizophrenia; Nephropathy | Mixed: hyperprolinemia is established; neuropsychiatric associations are reported but incompletely penetrant and sometimes confounded | (dalili2023clinicalfeaturesand pages 11-13, patriarca2021themultifacetedroles pages 6-9, yao2022prolinemetabolismin pages 4-5) |
| Diagnosis | Diagnostic approach centers on elevated proline in plasma/CSF/urine plus molecular confirmation of PRODH variants. P5C measurement helps distinguish HPI from HPII. Differential diagnosis includes ALDH4A1-related HPII and secondary hyperprolinemia in syndromic contexts such as 22q11.2 deletion. | HPO: Hyperprolinemia; Gene testing: PRODH; Differential: ALDH4A1-related hyperprolinemia type 2 | Established for biochemical testing strategy; no universally standardized diagnostic criteria retrieved | (dalili2023clinicalfeaturesand pages 11-13, yao2022prolinemetabolismin pages 4-5) |
| Treatment | No proven disease-modifying therapy was identified. Review evidence states dietary proline restriction does not improve clinical manifestations. Current care is supportive and phenotype-directed (e.g., seizure, developmental, psychiatric management). A vitamin D trial targeting schizophrenia-associated hyperprolinemia was withdrawn before enrollment, so no efficacy data exist. | NCIT suggestions: Supportive care; Dietary management; Anticonvulsant therapy; Psychiatric management | Established absence of proven therapy in retrieved evidence; experimental vitamin D concept remains untested | (dalili2023clinicalfeaturesand pages 11-13, NCT02197286 chunk 1, NCT02197286 chunk 2) |
| Prognosis / course | Prognosis appears variable and often compatible with long survival, especially in mild or asymptomatic cases, but robust survival statistics were not retrieved. The course is usually chronic biochemical hyperprolinemia with heterogeneous neurologic/psychiatric expression rather than a clearly staged progressive disorder. | HPO suggestions depend on phenotype burden; no specific prognosis ontology added | Uncertain due to sparse natural-history data and small cohorts | (dalili2023clinicalfeaturesand pages 11-13, yao2022prolinemetabolismin pages 4-5) |
| Epidemiology / population | HPI is rare. Reliable prevalence, incidence, carrier frequency, sex ratio, and founder-mutation data were not retrieved in the available evidence set. In a 22q11.2 deletion cohort, 35% had hyperprolinemia, but that figure should not be used as HPI prevalence. | MONDO:0009400 | Rarity established; population statistics largely unavailable here | (koning2015prodhrs450046and pages 1-2, koning2015prodhrs450046and pages 5-7, koning2015prodhrs450046and pages 4-5) |
| Model systems | Experimental evidence includes PRODH expression studies in U87 glioblastoma cells and Prodh-deficient mouse work discussed in reviews. Cell models show mitochondrial localization and effects on intracellular proline, glutamate, and glutamine; mouse literature supports relevance to sensorimotor-gating and neurobehavioral phenotypes, but not full recapitulation of human HPI heterogeneity. | CL suggestion: glial cell / astrocyte-like cell line context for U87; GO: mitochondrial inner membrane | Useful mechanistic support; translational limits should be noted | (cappelletti2018prolineoxidasecontrols pages 1-2, cappelletti2018prolineoxidasecontrols pages 10-12, cappelletti2018prolineoxidasecontrols pages 15-16, cappelletti2018prolineoxidasecontrols pages 6-7, cappelletti2018prolineoxidasecontrols pages 7-10) |
| Key evidence caveats | Much of the neuropsychiatric literature is confounded by 22q11.2 deletion syndrome, where PRODH hemizygosity co-occurs with many other deleted genes and modifiers such as COMT. Reported associations with IQ, startle, schizophrenia, or ASD are inconsistent, often based on small samples, and should not be overinterpreted as universal features of isolated HPI. | Annotation note: tag psychiatric findings as variable/uncertain association | Important caution for KB curation | (koning2015prodhrs450046and pages 1-2, koning2015prodhrs450046and pages 10-11, koning2015prodhrs450046and pages 7-8, koning2015prodhrs450046and pages 8-10, koning2015prodhrs450046and pages 5-7, koning2015prodhrs450046and pages 4-5, koning2015prodhrs450046and pages 12-12, yao2022prolinemetabolismin pages 3-4) |


*Table: This table provides a compact, evidence-weighted summary of Hyperprolinemia Type 1 for knowledge-base curation. It separates well-established disease facts from more uncertain neuropsychiatric associations and highlights where identifiers or epidemiologic values should be verified externally before ingestion.*

## 1. Disease information

### Definition

HPI is an **autosomal-recessive inborn error of amino-acid metabolism** caused by deficient mitochondrial proline dehydrogenase activity. Impaired first-step degradation of L-proline produces persistent hyperprolinemia and often increased urinary proline. The phenotype ranges from an incidental, apparently benign biochemical finding to variably penetrant neurologic, developmental, behavioral, or psychiatric manifestations. A 2023 review states that HPI may be asymptomatic or accompanied by behavioral problems, intellectual disability, autism-spectrum features, and seizures. [Dalili et al., published August 2023, DOI/URL](https://doi.org/10.5812/ans-136721) (dalili2023clinicalfeaturesand pages 11-13)

### Identifiers and synonyms

- **MONDO:** **MONDO:0009400**.
- **OMIM:** commonly indexed as **239500**; verify against the live OMIM record before database ingestion.
- **Orphanet:** commonly indexed as **ORPHA:419**; live-database verification is recommended.
- **MeSH:** usually represented under *Hyperprolinemia* rather than a reliably distinct type-1 descriptor.
- **ICD-10-CM:** no specific HPI code; usually mapped to **E72.5, Disorders of glycine metabolism**, which includes disorders of proline metabolism.
- **ICD-11:** use the current inborn-error/amino-acid-metabolism hierarchy; no reliably validated HPI-specific code was recovered.
- **Synonyms:** hyperprolinemia I; hyperprolinaemia type I; proline oxidase deficiency; proline dehydrogenase deficiency; PRODH deficiency.

The retrieved information is **aggregated disease-level evidence**, not individual EHR-derived information. Open Targets identifies PRODH as the dominant disease-associated target and links the association to PMIDs 11891283, 12217952, 15662599, 17135275, 24816252, and 27604308. Weaker automated associations to DGCR6 or PRODH2 should not be interpreted as established HPI causality. (OpenTargets Search: Hyperprolinemia type 1-PRODH)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The established cause is **biallelic germline loss or marked reduction of function in PRODH**, located at 22q11.21. PRODH encodes mitochondrial proline dehydrogenase/proline oxidase, the FAD-dependent enzyme catalyzing L-proline oxidation to Δ¹-pyrroline-5-carboxylate (P5C). HPI is not infectious, autoimmune, toxic, or lifestyle-caused. (dalili2023clinicalfeaturesand pages 11-13, cappelletti2018prolineoxidasecontrols pages 1-2)

### Genetic risk and modifiers

- The highest-risk genotype is biallelic pathogenic/likely pathogenic **PRODH** variation.
- A 22q11.2 deletion creates **PRODH hemizygosity**, but usually does not by itself establish classic recessive HPI; elevated proline may result from reduced dosage, an affected remaining allele, or broader metabolic modifiers.
- **COMT Val158Met** has been investigated as a neural modifier in 22q11.2DS because COMT and PRODH are both within or related to the deleted-region phenotype. In 45 adults with 22q11.2DS, 35% of those measured were hyperprolinemic, and a proline-by-COMT interaction affected startle reactivity, but not full-scale IQ or prepulse inhibition. Small genotype groups, medication exposure, and deletion-wide confounding make this preliminary rather than an established modifier relationship. [de Koning et al., June 2015](https://doi.org/10.1007/s00213-015-3971-5) (koning2015prodhrs450046and pages 1-2, koning2015prodhrs450046and pages 10-11)

### Environmental and protective factors

No environmental exposure is known to cause inherited HPI, and no validated genetic or environmental protective factor has been demonstrated. Potentially relevant **biochemical modifiers**, not proven causes, include:

- dietary proline load and fasting/postprandial state;
- renal or hepatic dysfunction affecting amino-acid handling;
- medications such as **valproate**, recognized in the withdrawn clinical trial as a cause of increased proline;
- vitamin-D status, proposed to influence PRODH expression but never clinically validated in HPI.

Dietary proline restriction has not reliably improved clinical manifestations. Thus, low-proline intake should not be labeled a proven protective intervention. (dalili2023clinicalfeaturesand pages 11-13, NCT02197286 chunk 1, NCT02197286 chunk 2)

## 3. Phenotypes

Frequencies for isolated, molecularly confirmed HPI are not robustly known. Reported manifestations should be annotated as **variable** or **occasional**, rather than universal.

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Elevated plasma proline | Core laboratory abnormality; congenital metabolic defect, chronic; reported up to approximately tenfold normal | **Hyperprolinemia, HP:0010916** |
| Increased urinary proline | Laboratory abnormality; glycine and hydroxyproline may also be excreted | Aminoaciduria (**HP:0003355**, broad) |
| Asymptomatic biochemical phenotype | No symptoms despite persistent hyperprolinemia; apparently common enough to make pathogenicity/penetrance assessment difficult | Asymptomatic (**HP:0000001**, if accepted locally) |
| Developmental delay/intellectual disability | Neurodevelopmental; generally childhood-recognized; severity variable | Global developmental delay **HP:0001263**; Intellectual disability **HP:0001249** |
| Behavioral abnormality | Childhood or later; nonspecific | Behavioral abnormality **HP:0000708** |
| Autism-spectrum features | Reported association, frequency unknown | Autistic behavior **HP:0000729** |
| Seizures/epilepsy | Childhood or later; can be severe or uncontrolled in reported patients, but not obligatory | Seizure **HP:0001250** |
| Schizophrenia/psychosis | Mainly adolescent/adult literature; association is inconsistent and heavily influenced by 22q11.2DS studies | Schizophrenia **HP:0100753**; Psychosis **HP:0000709** |
| White-matter abnormality | Rare case-level imaging finding | Abnormal CNS myelination **HP:0003429** or leukoencephalopathy term after imaging confirmation |
| Nephropathy | Rarely reported; causal attribution uncertain | Nephropathy **HP:0000112** |
| Myoclonus/ataxia | Rare case-report phenotype, including a 2023 report; not established as a typical HPI feature | Myoclonus **HP:0001336**; Ataxia **HP:0001251** |

The literature explicitly describes both nephropathy, seizures, intellectual disability, and schizophrenia and a benign phenotype without neurologic problems. This is strong evidence for **variable expressivity and incomplete clinical penetrance**, but not for precise phenotype frequencies. (yao2022prolinemetabolismin pages 4-5)

**Quality of life.** No HPI-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was identified. QoL effects are therefore inferred from the burden of epilepsy, cognitive disability, autism, movement disorder, or psychosis, when present—not from the biochemical abnormality alone.

## 4. Genetic and molecular information

### Causal gene and protein

- **Gene:** **PRODH**; approved name *proline dehydrogenase 1*.
- **Ensembl:** **ENSG00000100033**.
- **Location:** chromosome 22q11.21.
- **Protein:** mitochondrial proline dehydrogenase/proline oxidase, a flavoprotein associated with the inner mitochondrial membrane.
- **Origin:** constitutional/germline; somatic variation is not the HPI mechanism.
- **Functional class:** chiefly loss of function or severe hypomorphism.

### Pathogenic variants

Reported disease-associated alleles include missense, truncating, splice-altering, and deletion alleles. The **p.Leu441Pro (L441P)** missense substitution is a functionally studied example associated with hyperprolinemia and schizophrenia-related reports. In U87 cells it retained mitochondrial targeting but had reduced stability and approximately twofold lower normalized activity; raw mitochondrial activity was three- to fivefold below wild type. Earlier estimates suggested over 70% reduction. [Cappelletti et al., published April 2018, PMID 29698449](https://doi.org/10.1371/journal.pone.0196283) (cappelletti2018prolineoxidasecontrols pages 15-16, cappelletti2018prolineoxidasecontrols pages 7-10)

Variant-level pathogenicity must be adjudicated using current **ClinVar submissions, ACMG/AMP criteria, segregation, biochemical phenotype, functional evidence, and gnomAD ancestry-specific frequency**. This is important because HPI may be mild and metabolic-gene databases can contain historical misclassification. The retrieved corpus did not support a complete, current list of pathogenic variants or defensible per-variant population frequencies.

### Other molecular categories

- **Modifier genes:** COMT is a candidate modifier in the 22q11.2 context, not a confirmed HPI modifier. In one small cohort, PRODH rs450046 C carriers had lower mean FSIQ (60.2 versus 73.7; *p*=0.009), but there were only six C-allele carriers and no direct proline–FSIQ association. (koning2015prodhrs450046and pages 5-7, koning2015prodhrs450046and pages 4-5)
- **Epigenetics:** no reproducible HPI-specific methylation or chromatin signature is established.
- **Chromosomal abnormalities:** 22q11.2 deletions can include PRODH, but constitute a multisystem copy-number syndrome rather than isolated HPI.
- **Anticipation/germline mosaicism:** no repeat-expansion anticipation is relevant; germline mosaicism is theoretically possible but not established as a recurrent feature.

## 5. Environmental information

No toxin, pollutant, radiation exposure, occupational factor, infection, smoking behavior, alcohol exposure, or exercise pattern is an established cause of HPI. Diet contributes substrate but does not create the inherited enzyme defect. Secondary or transient elevations should prompt assessment of nutritional state, liver and renal function, medications, and preanalytic conditions. There is no zoonotic or infectious component.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** biallelic PRODH loss/reduction of function.
2. **Protein defect:** decreased activity of mitochondrial FAD-dependent proline dehydrogenase.
3. **Primary biochemical block:** reduced L-proline oxidation to P5C.
4. **Metabolic consequence:** proline accumulates in plasma, urine, and sometimes CSF; flux from P5C through ALDH4A1/P5C dehydrogenase to glutamate is altered.
5. **Downstream neural hypotheses:** high extracellular proline can interfere with excitatory presynaptic transmission; altered proline/P5C/glutamate cycling may disturb glutamate, glutamine, GABA, TCA-anaplerotic, and redox homeostasis.
6. **Clinical consequence:** incompletely penetrant neurodevelopmental, seizure, behavioral, or psychiatric phenotypes in susceptible individuals.

PRODH is a FAD-dependent mitochondrial enzyme, whereas P5C is subsequently converted to glutamate by NAD-dependent P5C dehydrogenase. Glutamate is both an excitatory neurotransmitter and precursor of glutamine and GABA. (cappelletti2018prolineoxidasecontrols pages 1-2, yao2022prolinemetabolismin pages 3-4)

### Evidence by level

**Human biochemical/clinical evidence.** Reviews describe proline in plasma and CSF at up to approximately tenfold normal in PRODH defects and variable cognitive or neurologic dysfunction. The exact relationship between proline concentration and symptoms is not linear or reliably predictive. (patriarca2021themultifacetedroles pages 6-9, cappelletti2018prolineoxidasecontrols pages 2-4)

**Human-cell evidence.** In U87 glioblastoma cells, PRODH expression reduced intracellular proline from 44.2 to 32.3–33.1 pmol/10⁴ cells at 24 hours and subsequently altered glutamate and glutamine. This supports pathway coupling but does not prove neuronal toxicity in patients. Proline above 30 μM at synaptic terminals has been reported to inhibit glutamate release. (cappelletti2018prolineoxidasecontrols pages 10-12)

**Redox/mitochondrial inference.** PRODH transfers electrons during proline oxidation and can influence ROS production. A p53→PRODH→ROS→apoptosis axis is demonstrated in stress/cancer contexts, but it should not be asserted as a proven tissue-injury mechanism in HPI. (patriarca2021themultifacetedroles pages 6-9)

**Immune and tissue injury.** No primary autoimmunity, immunodeficiency, inflammation, fibrosis, ischemia, or necrosis mechanism is established for isolated HPI.

### Suggested ontology annotations

- **GO biological process:** proline catabolic process; cellular amino-acid catabolic process; glutamate metabolic process; regulation of synaptic transmission, glutamatergic; oxidation–reduction process.
- **GO molecular function:** proline dehydrogenase activity; oxidoreductase activity acting on CH–NH₂ group donors; FAD binding.
- **GO cellular component:** mitochondrial inner membrane; mitochondrion.
- **CHEBI:** L-proline **CHEBI:17203**; L-glutamate **CHEBI:29985**; Δ¹-pyrroline-5-carboxylate; FAD; GABA **CHEBI:16865**.
- **Candidate cell types:** neuron **CL:0000540**; glutamatergic neuron **CL:0000679**; GABAergic neuron **CL:0000617**; astrocyte **CL:0000127**. These are mechanistically plausible, not proven selective targets.

### Molecular profiling and advanced technologies

No HPI-specific patient-cohort transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, organoid, or CRISPR-screen signature was identified. U87-cell metabolite measurements are mechanistic profiling, not a validated diagnostic omics signature.

## 7. Anatomical structures affected

The **nervous system** is the principal clinically implicated system when disease is symptomatic. Relevant regions inferred from neurotransmission and model work include cerebral cortex, prefrontal cortex, hippocampal circuits, and white matter; no consistent focal lesion or lateralization is established. Rare renal involvement has been reported but is not well characterized. (yao2022prolinemetabolismin pages 4-5, yao2022prolinemetabolismin pages 3-4)

Suggested annotations:

- **UBERON:** brain **UBERON:0000955**; cerebral cortex **UBERON:0000956**; hippocampal formation **UBERON:0002421**; white matter; kidney **UBERON:0002113**.
- **Tissues:** nervous tissue and, secondarily, renal tissue where clinically implicated.
- **Subcellular:** mitochondrial inner membrane, where PRODH functions.
- **Lateralization:** not applicable.

## 8. Temporal development

The enzyme defect is **congenital and lifelong**, but biochemical detection and clinical onset vary. Developmental delay, autism, or epilepsy generally emerge in childhood; psychotic illness, where genuinely associated, generally emerges later. Asymptomatic individuals may be detected incidentally at any age.

There is no accepted stage system. The biochemical condition is chronic; the clinical course can be stable, episodic where seizures or psychiatric symptoms occur, or rarely progressive in reported movement/neurologic presentations. No defined remission pattern, critical treatment window, or validated longitudinal trajectory exists.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Penetrance:** high for biochemical hyperprolinemia in individuals with severe biallelic deficiency, but apparently incomplete for clinical manifestations.
- **Expressivity:** markedly variable.
- **Sex ratio:** no established sex bias.
- **Prevalence/incidence:** reliably quantified population estimates are unavailable; HPI is considered very rare.
- **Carrier frequency/founder effects:** no robust global carrier frequency or consistently replicated founder allele was identified.
- **Consanguinity:** increases the probability of biallelic rare alleles, as for other recessive conditions, but disease-specific risk estimates are unavailable.

In a 22q11.2DS cohort, 12/34 measured individuals (35%) met the investigators’ hyperprolinemia thresholds; median proline was 281.5 μmol/L, range 159–929 μmol/L. This is a **syndromic, genetically selected sample and must not be used as HPI prevalence**. (koning2015prodhrs450046and pages 4-5)

## 10. Diagnostics

### Recommended approach

1. **Confirm biochemistry:** quantitative plasma amino acids, preferably fasting and repeated. Urine amino acids can document prolinuria; CSF amino acids are not routinely necessary.
2. **Differentiate type 1 from type 2:** assess urinary P5C or a validated equivalent. P5C accumulation/excretion favors **ALDH4A1-related HPII**, whereas HPI generally lacks marked P5C excretion. (dalili2023clinicalfeaturesand pages 11-13)
3. **Molecular confirmation:** sequence and deletion/duplication analysis of **PRODH**. A broader metabolic/neurodevelopmental panel or exome/genome sequencing is reasonable for complex phenotypes or negative single-gene testing.
4. **Variant interpretation:** integrate segregation, phase, biochemical magnitude, ClinVar/gnomAD evidence, and functional data.
5. **Phenotype assessment:** developmental and neuropsychological evaluation, EEG for suspected seizures, MRI only for neurologic indications, renal/liver studies to exclude secondary contributors.

### Genetic-test utility

- **Single-gene or panel testing:** first-line when biochemical HPI is clear.
- **WES/WGS:** useful for atypical cases, detecting alternative diagnoses and coding variants; WGS may improve CNV and noncoding detection.
- **CMA:** indicated when congenital anomalies, dysmorphism, cardiac disease, immune abnormalities, or hypocalcemia suggest 22q11.2DS.
- **Karyotype/FISH:** not routine for isolated HPI; targeted FISH may detect a known 22q11.2 deletion but CMA is more comprehensive.
- **mtDNA and repeat-expansion tests:** not indicated by the core disorder.
- **Enzyme assay:** specialized PRODH assays may support diagnosis but are not widely standardized clinically.

### Differential diagnosis

- **Hyperprolinemia type 2:** biallelic **ALDH4A1/P5C dehydrogenase** deficiency; generally higher proline and P5C excretion, with a stronger seizure association.
- **22q11.2 deletion syndrome:** multisystem phenotype with PRODH hemizygosity.
- Secondary hyperprolinemia from liver/renal dysfunction, nutritional state, or drugs.
- Other aminoacidopathies and neurodevelopmental/metabolic epilepsies.

There are no universally accepted clinical diagnostic criteria beyond persistent biochemical hyperprolinemia plus compatible molecular findings. Newborn screening is not routinely implemented, and isolated proline is not a standard core newborn-screening analyte.

## 11. Outcome and prognosis

No disease-specific five- or ten-year survival, mortality rate, or life-expectancy estimate exists. Mild or asymptomatic HPI appears compatible with normal longevity. Morbidity is driven by associated epilepsy, intellectual/developmental disability, behavioral disorder, movement disorder, nephropathy, or psychiatric illness—not by plasma proline alone.

Prognostic factors remain unvalidated. Plausible factors are residual enzyme activity, magnitude/persistence of hyperprolinemia, presence of a 22q11.2 deletion or second diagnosis, early developmental burden, and seizure control. No FDA-qualified prognostic biomarker or validated proline threshold predicts outcome.

## 12. Treatment

### Current clinical implementation

There is **no approved disease-modifying pharmacotherapy**, gene therapy, RNA therapy, cell therapy, enzyme replacement, or surgery for HPI. A 2023 review concluded that “no effective treatment exists” and that proline-restricted diets do not improve clinical manifestations. (dalili2023clinicalfeaturesand pages 11-13)

Management is individualized:

- antiseizure therapy according to epilepsy type;
- developmental, educational, speech, occupational, and physical therapies;
- standard evidence-based treatment of psychiatric illness;
- renal care if nephropathy is present;
- nutritional supervision if dietary manipulation is attempted, avoiding protein inadequacy.

Suggested NCIt intervention concepts include **Supportive Care**, **Anticonvulsant Therapy**, **Psychiatric Therapy**, **Occupational Therapy**, **Physical Therapy**, **Speech Therapy**, and **Dietary Intervention**. Exact NCIt codes should be resolved in the current release.

### Clinical trials and experimental therapy

**NCT02197286**, “Targeted Vitamin D Treatment of Schizophrenia-Associated Hyperprolinemia,” proposed 4,000 IU/day vitamin D3 versus placebo for ten weeks in 80 adults with schizophrenia-spectrum illness, vitamin-D insufficiency, and sex-specific fasting hyperprolinemia. The rationale was putative vitamin-D regulation of PRODH expression. The Phase 2 study was **withdrawn before enrollment because of personnel changes; enrollment was zero**, so it generated no efficacy or safety data. It was not a trial specifically in molecularly confirmed HPI. [ClinicalTrials.gov NCT02197286](https://clinicaltrials.gov/study/NCT02197286) (NCT02197286 chunk 1, NCT02197286 chunk 2)

No active disease-specific gene, RNA, cell, or targeted-therapy trial was identified.

## 13. Prevention

Because HPI is inherited, lifestyle modification cannot prevent the causal genotype.

- **Primary prevention:** genetic counseling, carrier testing for relatives after a familial variant is identified, reproductive options including prenatal diagnosis and preimplantation genetic testing.
- **Secondary prevention:** cascade testing and early biochemical/molecular diagnosis in siblings; prompt developmental and seizure assessment.
- **Tertiary prevention:** control seizures and psychiatric symptoms, developmental intervention, medication review, and prevention of nutritional harm.
- **Vaccination/public health/environmental prophylaxis:** no disease-specific role.

For two confirmed carrier parents, the Mendelian risk per pregnancy is 25% affected, 50% carrier, and 25% neither familial allele, assuming both variants are truly pathogenic and in trans.

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxonomy **9606**.
- **Mouse ortholog/model:** *Mus musculus*, Taxonomy **10090**, **Prodh**.
- Orthologs also occur in zebrafish, Drosophila, and *C. elegans*, reflecting conservation of proline metabolism.

No well-established naturally occurring companion-animal or livestock syndrome directly equivalent to human PRODH-related HPI was identified in the retrieved evidence. Accordingly, breed-specific VBO terms, veterinary prevalence, and natural-disease importance cannot be assigned. There is no transmission or zoonotic potential.

## 15. Model organisms and experimental systems

### Mouse

Prodh-deficient mice are the principal genetic model. Foundational work reported hyperprolinemia and abnormal sensorimotor gating, supporting a link between proline metabolism and neural circuit function. Reviews emphasize altered neurobehavioral/synaptic phenotypes, but mice do not reproduce the full heterogeneity of human intellectual disability, psychosis, or asymptomatic disease. The landmark study is Gogos et al., *Nature Genetics* 1999, “The gene encoding proline dehydrogenase modulates sensorimotor gating in mice,” DOI [10.1038/7777](https://doi.org/10.1038/7777).

### Human cellular model

Wild-type and L441P PRODH expressed in **U87 human glioblastoma cells** localize to mitochondria. The variant preserves localization but reduces activity/stability; manipulation of PRODH changes intracellular proline, glutamate, and glutamine. This model is useful for enzyme kinetics and metabolic coupling but is a transformed glial-like cell line, not a patient neuron or intact brain. (cappelletti2018prolineoxidasecontrols pages 1-2, cappelletti2018prolineoxidasecontrols pages 10-12, cappelletti2018prolineoxidasecontrols pages 7-10)

### Other potential systems

Zebrafish, fly, worm, patient fibroblasts, iPSC-derived neurons/astrocytes, and cerebral organoids are plausible platforms for functional studies and high-throughput screening, but no validated HPI-specific organoid or single-cell model was identified. Future work should prioritize isogenic PRODH knockout/knock-in iPSC models, direct measurement of synaptic proline/glutamate/GABA flux, and genotype–residual-activity–phenotype correlation.

## Recent developments and expert assessment

The most recent disease-relevant literature does not reveal a new approved therapy. Instead, 2023–2024 work has refined three interpretive points:

1. Modern aminoacidopathy reviews still characterize HPI as diagnostically biochemical, clinically heterogeneous, and without effective disease-modifying treatment. (dalili2023clinicalfeaturesand pages 11-13)
2. Contemporary cognition/psychiatry reviews continue to implicate PRODH and proline metabolism, but associations do not establish that isolated HPI inevitably causes schizophrenia.
3. Variant interpretation must account for mild/asymptomatic disease, ancestry-specific frequency, historical misclassification, and 22q11.2 confounding. Open Targets supports PRODH with multiple human-genetic literature items, whereas other gene associations are substantially weaker. (OpenTargets Search: Hyperprolinemia type 1-PRODH)

**Expert synthesis:** the most defensible disease model is a highly penetrant **biochemical** disorder with variably penetrant **clinical** consequences. Persistent elevated proline plus biallelic functionally consequential PRODH variants establishes the diagnosis; proline elevation alone does not predict neurologic or psychiatric outcome. Major unmet needs are a genotype-defined international registry, standardized fasting proline/P5C protocols, residual-activity assays, longitudinal neurodevelopmental outcomes, and controlled treatment studies.

## Selected abstract quotations and key sources

- Yao and Han’s 2022 review states: **“Proline plays a multifaceted role in protein synthesis, redox balance, cell fate regulation, brain development, and other cellular and physiological processes.”** [Published November 2022, DOI 10.14348/molcells.2022.0115](https://doi.org/10.14348/molcells.2022.0115) (yao2022prolinemetabolismin pages 4-5, yao2022prolinemetabolismin pages 3-4)
- Cappelletti et al. state: **“Proline is oxidized to glutamate in the mitochondria and the FAD-containing enzyme proline oxidase (PO) catalyzes the first step in L-proline degradation pathway.”** [Published April 2018, PMID 29698449](https://pubmed.ncbi.nlm.nih.gov/29698449/) (cappelletti2018prolineoxidasecontrols pages 1-2)
- The same primary study concludes: **“the proline pathway links cellular proline levels with those of glutamate and glutamine.”** (cappelletti2018prolineoxidasecontrols pages 1-2)
- The 2023 aminoacidopathy review summarizes HPI as autosomal recessive PRODH/proline-oxidase deficiency and reports no effective therapy or clinical improvement from proline restriction. [Published August 2023](https://doi.org/10.5812/ans-136721) (dalili2023clinicalfeaturesand pages 11-13)

**Evidence gaps should remain explicit in the knowledge base:** no reliable HPI prevalence/incidence, phenotype percentages, survival statistics, validated QoL instrument, complete penetrance estimate, proven protective factor, standardized therapeutic algorithm, active disease-specific interventional trial, or established patient multi-omics signature was found.

References

1. (OpenTargets Search: Hyperprolinemia type 1-PRODH): Open Targets Query (Hyperprolinemia type 1-PRODH, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (dalili2023clinicalfeaturesand pages 11-13): Setila Dalili, Ali Talea, Monireh Aghajany-Nasab, Navid Alirezapour Asl Miandoab, Shahin Koohmanaee, Seyede Tahoura Hakemzadeh, Amir Mohammad Ghanbari, and Nazanin Medghalchi. Clinical features and laboratory diagnosis of aminoacidopathies: a narrative review. Archives of Neuroscience, Aug 2023. URL: https://doi.org/10.5812/ans-136721, doi:10.5812/ans-136721. This article has 6 citations.

3. (yao2022prolinemetabolismin pages 4-5): Yuxiao Yao and Weiping Han. Proline metabolism in neurological and psychiatric disorders. Molecules and Cells, 45:781-788, Nov 2022. URL: https://doi.org/10.14348/molcells.2022.0115, doi:10.14348/molcells.2022.0115. This article has 37 citations and is from a peer-reviewed journal.

4. (patriarca2021themultifacetedroles pages 6-9): Eduardo J. Patriarca, Federica Cermola, Cristina D’Aniello, Annalisa Fico, Ombretta Guardiola, Dario De Cesare, and Gabriella Minchiotti. The multifaceted roles of proline in cell behavior. Frontiers in Cell and Developmental Biology, Aug 2021. URL: https://doi.org/10.3389/fcell.2021.728576, doi:10.3389/fcell.2021.728576. This article has 149 citations.

5. (cappelletti2018prolineoxidasecontrols pages 1-2): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

6. (yao2022prolinemetabolismin pages 3-4): Yuxiao Yao and Weiping Han. Proline metabolism in neurological and psychiatric disorders. Molecules and Cells, 45:781-788, Nov 2022. URL: https://doi.org/10.14348/molcells.2022.0115, doi:10.14348/molcells.2022.0115. This article has 37 citations and is from a peer-reviewed journal.

7. (NCT02197286 chunk 1): James D. Clelland. Targeted Vitamin D Treatment of Schizophrenia-Associated Hyperprolinemia. NYU Langone Health. 2015. ClinicalTrials.gov Identifier: NCT02197286

8. (NCT02197286 chunk 2): James D. Clelland. Targeted Vitamin D Treatment of Schizophrenia-Associated Hyperprolinemia. NYU Langone Health. 2015. ClinicalTrials.gov Identifier: NCT02197286

9. (koning2015prodhrs450046and pages 1-2): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

10. (koning2015prodhrs450046and pages 5-7): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

11. (koning2015prodhrs450046and pages 4-5): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

12. (cappelletti2018prolineoxidasecontrols pages 10-12): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

13. (cappelletti2018prolineoxidasecontrols pages 15-16): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

14. (cappelletti2018prolineoxidasecontrols pages 6-7): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

15. (cappelletti2018prolineoxidasecontrols pages 7-10): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

16. (koning2015prodhrs450046and pages 10-11): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

17. (koning2015prodhrs450046and pages 7-8): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

18. (koning2015prodhrs450046and pages 8-10): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

19. (koning2015prodhrs450046and pages 12-12): Mariken B. de Koning, Esther D. A. van Duin, Erik Boot, Oswald J. N. Bloemen, Jaap A. Bakker, Kathryn M. Abel, and Thérèse A. M. J. van Amelsvoort. Prodh rs450046 and proline x comt val158met interaction effects on intelligence and startle in adults with 22q11 deletion syndrome. Psychopharmacology, 232:3111-3122, Jun 2015. URL: https://doi.org/10.1007/s00213-015-3971-5, doi:10.1007/s00213-015-3971-5. This article has 19 citations and is from a peer-reviewed journal.

20. (cappelletti2018prolineoxidasecontrols pages 2-4): Pamela Cappelletti, Elena Tallarita, Valentina Rabattoni, Paola Campomenosi, Silvia Sacchi, and Loredano Pollegioni. Proline oxidase controls proline, glutamate, and glutamine cellular concentrations in a u87 glioblastoma cell line. PLoS ONE, 13:e0196283, Apr 2018. URL: https://doi.org/10.1371/journal.pone.0196283, doi:10.1371/journal.pone.0196283. This article has 46 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hyperprolinemia_Type_1-deep-research-falcon_artifacts/artifact-00.md)
