---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T18:06:11.461022'
end_time: '2026-07-31T18:14:56.493214'
duration_seconds: 525.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: White-Sutton Syndrome
  mondo_id: ''
  category: Mendelian
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
  path: White-Sutton_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** White-Sutton Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **White-Sutton Syndrome** covering all of the
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
- **Disease Name:** White-Sutton Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **White-Sutton Syndrome** covering all of the
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


# White-Sutton Syndrome: Disease Characteristics Research Report

## Executive summary

White-Sutton syndrome (WHSUS) is a rare, congenital neurodevelopmental chromatin disorder caused by a heterozygous pathogenic variant in **POGZ**. It is usually sporadic because the causal variant arises de novo, although mildly affected parents and familial transmission have been documented. Developmental and speech delay, variable intellectual disability, hypotonia, behavioral or autism-spectrum manifestations, characteristic but subtle craniofacial findings, visual abnormalities, feeding and gastrointestinal problems, sleep disturbance, hearing loss, seizures, and a tendency toward overweight are the principal manifestations. Severity is highly variable, including within families. There is no disease-modifying treatment; diagnosis is molecular and management is individualized, multidisciplinary, and symptom directed. The most informative large analyses through 2024 remain the 2020 cohort of 22 people, the 2022 clinical synthesis of 101 people, and the 2022 genotype–phenotype analysis of 117 people. Disease-specific publications in 2023–2024 were predominantly case reports and mechanistic/model work rather than new large natural-history cohorts.

The following table provides a compact knowledge-base extraction; the narrative below supplies interpretation and additional ontology recommendations.

| Domain | Established findings | Evidence gaps / caveats | Suggested ontology terms | Key citations |
|---|---|---|---|---|
| Identifiers / synonyms | White-Sutton syndrome (WHSUS) is a rare neurodevelopmental disorder caused by heterozygous pathogenic variants in **POGZ**; OMIM **616364**. Related MONDO label reported as **intellectual disability-microcephaly-strabismus-behavioral abnormalities syndrome**; Open Targets also maps disease as **white-sutton syndrome**. Synonyms in the literature include **POGZ-related intellectual disability syndrome** and **POGZ-related neurodevelopmental disorder**. Disease-level information here is derived from aggregated published cohorts and curated disease resources, not EHR-only data. | MONDO/EFO mapping is resource-dependent in the gathered evidence; no single ICD-10/ICD-11 code was identified in the retrieved sources. | MONDO: **MONDO_0014606**; MeSH/ICD not established from gathered evidence | (batzir2020phenotypicexpansionof pages 1-2, OpenTargets Search: White-Sutton syndrome-POGZ, murch2022furtherdelineationof pages 1-2) |
| Causal gene / inheritance | Causal gene: **POGZ** (pogo transposable element derived with ZNF domain; Ensembl **ENSG00000143442**). Inheritance is **autosomal dominant / monoallelic**, most often **de novo**. In the 22-person cohort, 18/21 informative variants were de novo, 1 maternally inherited, 2 unknown; in the 117-patient aggregate, ~90% were de novo and ~10% inherited. | Penetrance is not well quantified; inherited cases show variable expressivity. Modifier genes are not established from the gathered evidence. | Gene: **POGZ**; inheritance: **autosomal dominant inheritance (HP:0000006)** | (batzir2020phenotypicexpansionof pages 3-5, OpenTargets Search: White-Sutton syndrome-POGZ, nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 1-2) |
| Variant spectrum | Predominantly **loss-of-function** variants: nonsense, frameshift, splice-site, larger deletions; missense variants are less common. In the 117-patient analysis: nonsense 41%, frameshift 40%, missense 8.5%, splice-site 7%, larger deletions 2.5%, in-frame deletions 1%. Variants often cluster in exon 19 / domains including proline-rich region, CENP-B DNA-binding and DDE transposase-related regions. Truncating variants predicted to **escape nonsense-mediated decay (NMD)** were associated with more severe phenotypes; missense and NMD-subjected variants tended to be milder. | Population allele frequencies (e.g., gnomAD counts) were not retrieved here. Functional classification of each specific variant remains case-dependent. Somatic disease role not supported; this is a germline disorder. | Sequence ontology suggestions: **stop_gained**, **frameshift_variant**, **splice_donor_variant**, **splice_acceptor_variant**, **copy_number_loss** | (batzir2020phenotypicexpansionof pages 12-13, batzir2020phenotypicexpansionof pages 3-5, nagy2022genotypephenotypecomparisonin pages 9-10, nagy2022genotypephenotypecomparisonin pages 1-2, murch2022furtherdelineationof pages 1-2) |
| Core phenotype frequencies | Across the 22-person cohort: **speech delay 100%**, learning difficulties 100%, **motor delay 86%**, **intellectual disability 87%**, **autism 37.5%**; ocular abnormalities, hearing loss, gait abnormalities, GI and GU anomalies were common. Sleep-disordered breathing symptoms suggestive of OSA occurred in **4/12 (33%)** tested. In the 117-patient aggregate, commonly reported features included facial dysmorphism 96%, speech delay 88%, global developmental delay 88%, ID 79%, behavioral abnormalities 75%, sleep disturbances 75%, ocular anomalies 63%, hypotonia 54%, sensorineural hearing impairment 54%, microcephaly 46%, seizures 60% (noting ascertainment/reporting variability). In the 12-person series, microcephaly was **8/12**, early feeding problems **7/11**, obesity **4/5** among those >10 years. | Frequencies vary substantially across cohorts because of incomplete reporting, ascertainment bias, and different denominators. Some features such as subtle genital anomalies and brachydactyly are likely underreported. | HPO suggestions: **Global developmental delay (HP:0001263)**, **Speech delay (HP:0000750)**, **Intellectual disability (HP:0001249)**, **Autism (HP:0000717)**, **Hypotonia (HP:0001252)**, **Microcephaly (HP:0000252)**, **Sensorineural hearing impairment (HP:0000407)**, **Abnormality of gait (HP:0001288)**, **Obesity/Overweight (HP:0001513/HP:0025385)**, **Obstructive sleep apnea (HP:0002870)** | (batzir2020phenotypicexpansionof pages 11-12, batzir2020phenotypicexpansionof pages 1-2, batzir2020phenotypicexpansionof pages 7-8, batzir2020phenotypicexpansionof pages 8-9, nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 5-6, murch2022furtherdelineationof pages 1-2) |
| Mechanism / pathophysiology | **Human genetics + model evidence** support POGZ as a **chromatin regulator** interacting with **HP1α**, involved in **chromosome segregation**, **mitotic progression**, and transcriptional repression/organization. Mouse nervous-system knockout data show **transcriptional upregulation**, especially in cerebellum, enrichment of dysregulated genes in **neurogenesis** and **synaptic processes**, reduced mitotic cells in embryonic cortex, smaller brain, and **Purkinje-cell electrophysiologic abnormalities** (reduced simple/complex spike firing, increased inhibitory input amplitude). A plausible causal chain is: POGZ haploinsufficiency or abnormal truncated protein effect -> heterochromatin/transcription dysregulation and altered neuronal developmental programs -> abnormal circuit development/function, especially cerebellar pathways -> developmental delay, ID, motor and behavioral phenotypes. | Direct human tissue mechanistic studies remain limited. No disease-specific transcriptomic/proteomic biomarker is established from the retrieved human studies. Epigenetic episignature evidence for WHSUS was not retrieved. | GO suggestions: **chromatin organization**, **negative regulation of transcription**, **mitotic chromosome segregation**, **neurogenesis**, **synaptic signaling**; CL suggestions: **Purkinje cell**, **cortical intermediate progenitor cell** | (batzir2020phenotypicexpansionof pages 2-3, sulimanlavie2020pogzdeficiencyleads pages 1-2, sulimanlavie2020pogzdeficiencyleads pages 2-3, nagy2022genotypephenotypecomparisonin pages 1-2) |
| Diagnostic approach | Diagnosis in published cohorts was usually made by **trio whole-exome sequencing**, **whole-genome sequencing**, or **intellectual-disability / neurodevelopmental gene panels**; some patients also had chromosomal microarray without an alternative diagnosis. Because the clinical phenotype is relatively nonspecific and variable, **genomic testing is the main diagnostic route**. In Baylor clinical exome data, POGZ variants were implicated in about **0.14%** of cases referred for neurodevelopmental indications. | No universally accepted clinical diagnostic criteria independent of molecular confirmation were identified. No validated biochemical biomarker, imaging signature, or episignature was retrieved from the gathered evidence. | NCIT/testing suggestions: **Whole Exome Sequencing**, **Whole Genome Sequencing**, **Next-Generation Sequencing Gene Panel**, **Chromosomal Microarray Analysis** | (batzir2020phenotypicexpansionof pages 12-13, batzir2020phenotypicexpansionof pages 8-9, murch2022furtherdelineationof pages 1-2) |
| Management | Current care is **supportive and multidisciplinary**: developmental/behavioral assessment, speech-language therapy, occupational/physical therapy, hearing and vision evaluation, feeding/GI support, obesity monitoring, sleep assessment (including for OSA), and seizure-directed neurology care when indicated. Published case series emphasize individualized therapies tailored to neurological, behavioral, and communication needs. | No disease-modifying drug, gene therapy, RNA therapy, or targeted therapy was identified in the gathered evidence. Treatment response rates are not established at syndrome level. | NCIT suggestions: **Speech Therapy**, **Occupational Therapy**, **Physical Therapy**, **Behavioral Intervention**, **Audiologic Assessment**, **Ophthalmologic Examination**, **Nutritional Support** | (batzir2020phenotypicexpansionof pages 11-12, batzir2020phenotypicexpansionof pages 1-2, murch2022furtherdelineationof pages 5-6, NCT07380594 chunk 1) |
| Epidemiology / prognosis | WHSUS is rare; exact population prevalence/incidence were not established in the retrieved sources. Literature available to the cohorts indicated >50 reported individuals by 2020, ~90 by 2022, and 117 patients in an aggregate genotype-phenotype analysis. Course is typically **pediatric-onset and chronic/lifelong**, with variable severity from mild learning/behavioral issues to severe ID and multisystem involvement. Survival/life-expectancy data were not identified; no specific excess mortality estimate was retrieved. | Prevalence, incidence, penetrance, carrier frequency, and mortality remain insufficiently defined from the gathered evidence. Long-term adult natural history remains sparse. | HPO course suggestions: **Childhood onset**, **Chronic course**, **Variable expressivity** | (batzir2020phenotypicexpansionof pages 1-2, nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 5-6, murch2022furtherdelineationof pages 1-2) |
| Trials / current research | Identified study: **NCT07380594**, *Descriptive Study of Psychiatric Symptoms in White-Sutton Syndrome* (CHU Dijon; observational; recruiting; estimated n=30; first posted 2026-02-02). It aims to define psychiatric manifestations using interviews and standardized scales in genetically confirmed individuals aged >6 years. | No interventional White-Sutton syndrome trials were identified in the gathered evidence. The located study is observational and future-dated relative to the requested 2023-2024 emphasis. | NCIT suggestions: **Observational Study**, **Psychiatric Assessment**, **Questionnaire** | (NCT07380594 chunk 1) |
| Models / comparative evidence | Best-supported model in gathered evidence: **nervous-system-specific conditional Pogz knockout mouse**. Reported phenotypes include microcephaly/smaller brain, growth impairment, altered embryonic neurogenesis, transcriptional dysregulation, cerebellar Purkinje-cell dysfunction, and behavioral abnormalities including learning and motor deficits, paralleling several human features. Earlier summaries also note **Drosophila** and possible **zebrafish** relevance, but detailed retrieved evidence here is strongest for mouse. | No naturally occurring veterinary disease equivalent was identified. Non-mouse models were mentioned in secondary discussion but not substantiated with detailed primary evidence in the gathered set. | Model ontology suggestions: **Mus musculus**; CL: **Purkinje cell**; UBERON: **cerebellum**, **cerebral cortex** | (batzir2020phenotypicexpansionof pages 11-12, nagy2022genotypephenotypecomparisonin pages 2-4, sulimanlavie2020pogzdeficiencyleads pages 2-3, sulimanlavie2020pogzdeficiencyleads pages 1-2) |


*Table: This table provides a compact knowledge-base summary of White-Sutton syndrome using only evidence gathered in this conversation. It highlights established findings, major evidence gaps, suggested ontology mappings, and supporting citations for rapid curation.*

## 1. Disease information

### Definition and identifiers

WHSUS is a **Mendelian, autosomal-dominant neurodevelopmental disorder** attributable to monoallelic pathogenic variants in **POGZ**, a chromatin-associated regulator at chromosome 1q21.3. Its clinical presentation ranges from mild learning or behavioral impairment to severe developmental disability with multisystem congenital anomalies. ClinGen/gene2phenotype evidence summarized by Open Targets classifies the POGZ–disease relationship as definitive. (batzir2020phenotypicexpansionof pages 2-3, OpenTargets Search: White-Sutton syndrome-POGZ)

* **OMIM:** 616364.
* **MONDO:** **MONDO:0014606**, labeled *intellectual disability–microcephaly–strabismus–behavioral abnormalities syndrome* in the retrieved mapping.
* **EFO/Open Targets:** EFO:0009079, *white-sutton syndrome*.
* **Gene:** POGZ; Ensembl ENSG00000143442; approved name *pogo transposable element derived with ZNF domain*.
* **Synonyms:** POGZ-related intellectual disability syndrome; POGZ-related neurodevelopmental disorder; intellectual disability–microcephaly–strabismus–behavioral abnormalities syndrome.
* **Orphanet, MeSH, ICD-10/ICD-11:** no verified disease-specific identifiers were recovered in the searched primary literature. In practice, nonspecific developmental-disorder, intellectual-disability, autism, epilepsy, or congenital-anomaly codes may be used, but these should not be represented as WHSUS-specific identifiers without verification.

The evidence synthesized here is principally **aggregated disease-level information** from published cohorts, DECIPHER/clinical laboratory series, ClinGen/Open Targets, and ClinicalTrials.gov—not an individual EHR-derived phenotype profile. The 2020 study used a genotype-first cohort and clinical laboratory database; the 2022 reports combined new individuals with literature cases. (batzir2020phenotypicexpansionof pages 1-2, murch2022furtherdelineationof pages 5-6, murch2022furtherdelineationof pages 1-2)

## 2. Etiology

### Causal and risk factors

The primary cause is a **germline heterozygous pathogenic or likely pathogenic POGZ variant**. In the 22-person Batzir cohort, 18 variants were de novo, one maternally inherited, and two had unknown inheritance. In the 117-person aggregate, approximately 90% were de novo and 10% inherited. Thus, a pathogenic POGZ allele is causal rather than merely a susceptibility factor. (batzir2020phenotypicexpansionof pages 3-5, nagy2022genotypephenotypecomparisonin pages 9-10)

The predominant disease alleles are protein-truncating variants, although splice variants, whole/partial-gene deletions, in-frame deletions, and a smaller number of deleterious missense variants occur. The 117-person analysis reported nonsense 41%, frameshift 40%, missense 8.5%, splice-site 7%, large deletions 2.5%, and in-frame deletions 1%. (nagy2022genotypephenotypecomparisonin pages 9-10)

### Environmental, infectious, and lifestyle factors

No toxin, infection, maternal exposure, diet, occupation, smoking, alcohol use, or other environmental factor is established as a cause of WHSUS. Lifestyle can influence secondary obesity, sleep-disordered breathing, constipation, and general health but does not cause the Mendelian disorder. No reproducible gene–environment interaction has been demonstrated.

### Protective factors and modifiers

No protective POGZ allele, modifier gene, or environmental exposure that prevents WHSUS has been established. Variant position and predicted nonsense-mediated decay (NMD) behavior modify severity: truncating alleles predicted to escape NMD, particularly in the proline-rich region, were associated with more severe disease, whereas missense and NMD-subjected alleles tended to be milder. These are probabilistic cohort associations, not deterministic prognostic rules. (batzir2020phenotypicexpansionof pages 12-13, nagy2022genotypephenotypecomparisonin pages 1-2)

## 3. Phenotypes

The strongest frequency estimates come from differently ascertained cohorts and are not directly interchangeable. Missing data and preferential publication of severely affected patients can inflate estimates—especially the 60% seizure frequency in one selected aggregate. Murch and colleagues specifically warned of variable reporting and likely underrecognition of subtle findings. (nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 5-6)

### Neurodevelopmental and behavioral manifestations

* **Global developmental delay**—usually recognized in infancy or early childhood; variable severity, chronic/lifelong. Reported in 88% of the 117-person analysis. Suggested HPO: **HP:0001263**.
* **Speech/language delay**—often especially prominent; 100% in the 22-person cohort and 88% in the 117-person analysis. Some individuals remain minimally verbal. HPO: **HP:0000750**, with **HP:0002463** for language impairment where appropriate. (batzir2020phenotypicexpansionof pages 1-2, batzir2020phenotypicexpansionof pages 8-9, nagy2022genotypephenotypecomparisonin pages 9-10)
* **Motor delay**—86% in the 22-person cohort; may coexist with hypotonia and gait abnormality. HPO: **HP:0001270** or HP:0001263. (batzir2020phenotypicexpansionof pages 8-9)
* **Intellectual disability/learning difficulty**—ID 87% in the 22-person series and 79% in the 117-person aggregate, but some patients have low-normal cognition or isolated learning/behavioral difficulties. Severity spans mild to severe. HPO: **HP:0001249**, **HP:0001328**. (batzir2020phenotypicexpansionof pages 11-12, nagy2022genotypephenotypecomparisonin pages 9-10)
* **Autism spectrum and behavior**—autism was 37.5% in the 22-person series; broader behavioral abnormalities were 75% in the aggregate. Anxiety, hyperactivity/attention problems, stereotypies, social withdrawal, compulsive features, and unusually friendly behavior have been described. HPO: **HP:0000717**, **HP:0000739**, **HP:0000752**, **HP:0000729** as individually documented. (batzir2020phenotypicexpansionof pages 8-9, nagy2022genotypephenotypecomparisonin pages 9-10, NCT07380594 chunk 1)
* **Hypotonia**—54% in the 117-person aggregate; generally childhood onset and variable. HPO: **HP:0001252**. (nagy2022genotypephenotypecomparisonin pages 9-10)
* **Seizures/EEG abnormalities**—seizures were reported in 60% in one selected aggregate, but other cohorts suggest lower or incompletely ascertained frequencies. Both epileptic and nonepileptic paroxysmal events and abnormal EEG without clinical seizures have been reported. HPO: **HP:0001250**, **HP:0002353**.
* **Sleep disturbance**—75% in the 117-person aggregate; symptoms consistent with obstructive sleep apnea occurred in 4/12 (33%) formally screened in the 22-person cohort. HPO: **HP:0002360**, **HP:0002870**. (batzir2020phenotypicexpansionof pages 1-2, nagy2022genotypephenotypecomparisonin pages 9-10)

### Growth, craniofacial, sensory, and systemic manifestations

* **Microcephaly:** 46% in the aggregate and 8/12 in the Murch series; HPO **HP:0000252**. Growth may otherwise be normal, short, or overweight. (nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 1-2)
* **Overweight/obesity:** the 2020 cohort had mean BMI z-score 0.59 and median 0.9, significantly above the reference population (p=0.0253); 4/5 patients older than ten years in the Murch series were obese. HPO **HP:0025385**, **HP:0001513**. (batzir2020phenotypicexpansionof pages 1-2, batzir2020phenotypicexpansionof pages 3-5, murch2022furtherdelineationof pages 1-2)
* **Facial gestalt:** broad/high forehead, midface hypoplasia, broad nasal root or flat bridge, tented/triangular mouth, and sometimes low-set ears; facial dysmorphism was reported in 96% of one aggregate. These findings are usually mild and not sufficiently specific for clinical diagnosis. HPO terms should be assigned feature-by-feature rather than using a single gestalt term. (batzir2020phenotypicexpansionof pages 1-2, batzir2020phenotypicexpansionof pages 3-5, nagy2022genotypephenotypecomparisonin pages 9-10)
* **Ocular abnormalities:** 63% in the aggregate; refractive errors, strabismus and, rarely, rod-cone dystrophy. HPO **HP:0000478**, **HP:0000486**, **HP:0000510** as applicable. (nagy2022genotypephenotypecomparisonin pages 9-10, murch2022furtherdelineationof pages 5-6)
* **Sensorineural hearing impairment:** 54% in the aggregate, although cohort ascertainment varies. HPO **HP:0000407**. (nagy2022genotypephenotypecomparisonin pages 9-10)
* **Feeding/GI:** early feeding difficulty occurred in 7/11 in one series. In the 22-person cohort, swallowing difficulty occurred in 53%, gastrostomy feeding in 23.5% (4/17), cyclic vomiting in 37.5% (6/16), and severe anatomical/clinical GI complications in 16% (3/19). Constipation, reflux, dysmotility, malrotation, intussusception, pancreatitis, rectal prolapse, and congenital diaphragmatic hernia have been reported. HPO: **HP:0011968**, **HP:0002020**, **HP:0002573**, **HP:0002019**, and condition-specific terms. (batzir2020phenotypicexpansionof pages 11-12, batzir2020phenotypicexpansionof pages 7-8, murch2022furtherdelineationof pages 1-2)
* **Gait abnormality:** common but inconsistently quantified; HPO **HP:0001288**.
* **Genitourinary anomalies:** male genital anomalies occurred in 4/14 (28.6%) in one cohort; duplicated renal drainage system and other urinary anomalies are rare. HPO terms should reflect the specific defect. (batzir2020phenotypicexpansionof pages 7-8, murch2022furtherdelineationof pages 5-6)
* **Structural brain, cardiac, craniofacial and diaphragmatic anomalies:** variably reported and usually uncommon. Major cardiovascular abnormalities were uncommon in the 2020 series; cleft lip/palate and congenital diaphragmatic hernia appear to be rare complications. (batzir2020phenotypicexpansionof pages 7-8, murch2022furtherdelineationof pages 5-6)

### Quality of life

No WHSUS-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life study was identified. Developmental, communication, behavioral, sleep, feeding, sensory, mobility, and seizure manifestations can impair education, autonomy, social participation, caregiver sleep, and family well-being. This impact is clinically plausible but has not been quantified adequately in syndrome-specific prospective studies.

## 4. Genetic and molecular information

**POGZ** is the only firmly established causal gene. The retrieved evidence did not support **NPC1** as a second WHSUS gene; its low Open Targets association likely reflects ontology/co-occurrence noise and should not be entered as causal. (OpenTargets Search: White-Sutton syndrome-POGZ)

Pathogenic alleles are germline and generally absent or extremely rare in population databases; POGZ is highly constrained against both protein-truncating and missense variation. Exact gnomAD frequencies must be checked variant-by-variant and were not available in the retrieved texts. Variant interpretation should follow ACMG/AMP criteria, incorporating de novo status, predicted loss of function in a constrained gene, population absence, phenotype consistency, segregation, and functional evidence. (murch2022furtherdelineationof pages 1-2)

The protein contains zinc-finger clusters, an HP1-binding motif, a proline-rich region, CENP-B DNA-binding domain, transposase-derived DDE domain, coiled-coil region, and integrase-binding motif. Many pathogenic variants occur in the large terminal exon/domain-rich region. In 117 patients, truncating alleles escaping NMD were associated with severe manifestations (p<0.0001), and variants in the proline-rich region showed the strongest severity association (p=0.0004). Missense variants were more often associated with milder disease (p=0.0421). The proposed dominant-negative or gain-of-function effect of stable truncated products remains an inference; classical haploinsufficiency remains important for alleles undergoing NMD or deletions. (batzir2020phenotypicexpansionof pages 12-13, nagy2022genotypephenotypecomparisonin pages 9-10, nagy2022genotypephenotypecomparisonin pages 1-2)

No validated modifier gene or WHSUS-specific blood DNA-methylation episignature was identified. Large deletions involving POGZ can cause the phenotype, but broader deletions require assessment for neighboring-gene effects. No repeat expansion, mitochondrial, or recurrent balanced rearrangement mechanism is established.

## 5. Environmental information

Environmental toxins, radiation, pollution, occupational exposure, infectious agents, smoking, alcohol, diet, and exercise are **not primary etiologic factors**. Diet, activity, sleep hygiene, and medications can modify obesity, constipation, sleep, and behavior after disease onset. WHSUS is neither infectious nor transmissible, and no zoonotic dimension exists.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

POGZ binds heterochromatin protein 1α and participates in chromatin organization, transcriptional regulation, chromosome segregation, kinetochore/mitotic processes, and Aurora-B-related chromosome dynamics. It also interacts with transcriptional/chromatin proteins including SP1 and CHD4 and co-occupies genomic loci with the autism-associated regulator ADNP. Expression is high during embryonic development, including fetal brain, supporting a developmental mechanism. (batzir2020phenotypicexpansionof pages 2-3, nagy2022genotypephenotypecomparisonin pages 1-2, murch2022furtherdelineationof pages 1-2)

### Causal chain

**Pathogenic POGZ allele → reduced normal POGZ dosage and/or abnormal stable truncated protein → impaired HP1-associated heterochromatin and transcriptional control, altered mitotic/neural-progenitor programs and synaptic-gene accessibility → abnormal neurogenesis and neuronal circuit maturation → cerebellar/cortical dysfunction → developmental, cognitive, motor, behavioral, seizure, and sleep phenotypes.** Pleiotropic transcriptional effects during embryogenesis plausibly contribute to craniofacial, GI, genitourinary, diaphragmatic, and other congenital anomalies, but these extra-neural links are less directly established.

### Model and cellular evidence

In a nervous-system-specific conditional mouse knockout, Pogz deficiency produced smaller absolute brain size, growth impairment, learning and motor deficits, and altered sociability. Embryonic cortex showed a 19% reduction in mitotic pHH3-positive cells in heterozygotes and 43.8% in homozygotes, with expansion of the Tbr2-positive intermediate-progenitor layer but no significant change in Pax6-positive apical progenitors. Complete germline knockout is embryonic lethal, limiting direct correspondence to viable heterozygous humans. (sulimanlavie2020pogzdeficiencyleads pages 2-3, sulimanlavie2020pogzdeficiencyleads pages 1-2)

Transcriptomic changes were predominantly gene upregulation—most marked in cerebellum—and enriched for neurogenesis, synaptic, and autism-related pathways. Cerebellar Purkinje cells showed reduced simple- and complex-spike firing and increased inhibitory synaptic-input amplitude. The authors’ abstract states: **“Our findings support a mechanism linking heterochromatin dysregulation to cerebellar circuit dysfunction and behavioral abnormalities in ASD.”** This is primary mouse/in-vitro evidence, not direct proof that every human manifestation is cerebellar in origin. Published 2020-11-17, DOI: https://doi.org/10.1038/s41467-020-19577-0. (sulimanlavie2020pogzdeficiencyleads pages 1-2)

Suggested annotations include GO **chromatin organization**, **negative regulation of transcription by RNA polymerase II**, **mitotic chromosome segregation**, **neurogenesis**, **regulation of synaptic signaling**, and **heterochromatin organization**; cellular components include **nucleus**, **chromatin**, **heterochromatin**, and **kinetochore**. Relevant Cell Ontology classes include **Purkinje cell**, **neuron**, **cortical neural progenitor cell**, and **intermediate progenitor cell**. No validated human metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, or multi-omic WHSUS signature was found through 2024.

## 7. Anatomical structures affected

The primary system is the **nervous system**, particularly the developing brain. Relevant locations include cerebral cortex (**UBERON:0000956**), cerebellum (**UBERON:0002037**), hippocampal formation, and their neuronal progenitors and mature neurons. Mouse evidence most directly implicates cortical progenitors and cerebellar Purkinje cells. (sulimanlavie2020pogzdeficiencyleads pages 2-3, sulimanlavie2020pogzdeficiencyleads pages 1-2)

Secondary involvement can include eyes/visual system, inner ear/auditory system, skeletal muscle or motor system through hypotonia, gastrointestinal tract, upper airway during sleep, kidney/urinary and reproductive systems, craniofacial structures, and—rarely—diaphragm, heart, or brain structure. Ocular and hearing abnormalities are frequently bilateral, but no consistent lateralization pattern is established. At the subcellular level, the nucleus, chromatin/heterochromatin, chromosomes, and kinetochore are principal compartments.

## 8. Temporal development

WHSUS is congenital in molecular origin and typically becomes clinically apparent during infancy or early childhood through hypotonia, feeding difficulty, delayed milestones, poor speech acquisition, microcephaly, or congenital anomalies. Some mildly affected people are diagnosed later through learning, psychiatric, or behavioral assessment. The 2020 cohort’s median diagnostic age was eight years, with a range from one week to 28 years, demonstrating diagnostic delay and broad ascertainment. (batzir2020phenotypicexpansionof pages 3-5)

The course is chronic and lifelong, not acute, relapsing-remitting, or self-limited. Developmental skills may improve with maturation and therapy, but core neurodevelopmental disability does not “remit.” Obesity may become more apparent later in childhood; seizures, sleep apnea, behavior, and GI problems may be episodic or evolve over time. No validated staging system or progression rate exists. Early childhood is the principal intervention window for speech, motor, communication, feeding, sensory, and behavioral support.

## 9. Inheritance and population

Inheritance is autosomal dominant, predominantly de novo. Vertical transmission demonstrates that affected individuals can reproduce; a carrier parent may be only mildly affected. Penetrance cannot be quantified reliably, although pathogenic truncating alleles generally appear clinically consequential. Expressivity is markedly variable. There is no evidence for anticipation, founder mutations, consanguinity dependence, or a population-specific carrier frequency. Parental germline mosaicism has not been quantified; as with other apparently de novo dominant disorders, a low residual recurrence risk should be discussed after negative parental blood testing.

No population prevalence or annual incidence estimate is established. The literature had reported more than 50 affected people by 2020, nearly 90 by 2021/2022, and 117 individuals were available for the large 2022 aggregate. POGZ diagnoses accounted for approximately 0.14% of clinical exomes referred for neurodevelopmental indications in one laboratory dataset, including 0.12% of autism, 0.19% of developmental-delay, and 0.18% of intellectual-disability referrals. These are **diagnostic-laboratory yields, not population prevalence**. (batzir2020phenotypicexpansionof pages 1-2, batzir2020phenotypicexpansionof pages 12-13, nagy2022genotypephenotypecomparisonin pages 9-10)

No robust ethnic, geographic, or sex disparity is established. The 117-person analysis included 62 males and 53 females with two sex entries apparently unavailable, broadly consistent with no major sex bias. (nagy2022genotypephenotypecomparisonin pages 2-4)

## 10. Diagnostics

### Recommended testing strategy

1. **Clinical recognition:** unexplained developmental/speech delay or ID, especially with hypotonia, autism/behavioral features, visual problems, microcephaly, hearing loss, feeding/GI difficulty, sleep disorder, or suggestive facial appearance.
2. **First-line genomic test:** trio WES or WGS is preferred for a nonspecific syndromic neurodevelopmental presentation. A comprehensive neurodevelopmental/ID/autism panel containing POGZ is appropriate where exome/genome sequencing is unavailable.
3. **Variant confirmation and segregation:** confirm the candidate variant and test both biological parents. Sanger sequencing remains useful for segregation; read-depth/CNV analysis is needed for exon or whole-gene deletions.
4. **CMA:** useful when congenital anomalies or ID suggest a copy-number disorder and can identify a deletion encompassing POGZ, but will miss most single-nucleotide and small indel alleles.
5. **WGS:** potentially detects coding variants, CNVs, structural variants, and noncoding/splice-altering variants missed by WES; evidence for a WHSUS-specific incremental yield has not yet been quantified.

Most reported individuals were diagnosed by trio WES, WGS, or an ID gene panel because the phenotype is insufficiently specific for reliable clinical diagnosis. (murch2022furtherdelineationof pages 1-2)

Karyotyping/FISH are not routine unless a larger rearrangement is suspected. Mitochondrial sequencing, repeat-expansion testing, biopsy, metabolomics, proteomics, and liquid biopsy have no disease-specific role. RNA sequencing may help resolve an uncertain splice variant but is not validated as routine WHSUS testing. No standardized clinical diagnostic criteria or biochemical biomarker exists.

### Baseline and surveillance evaluations

After molecular diagnosis: developmental/neuropsychological evaluation; speech-language and feeding/swallow assessment; growth and BMI; ophthalmology; audiology; neurologic examination; EEG if seizures or suspicious events occur; sleep evaluation/polysomnography when snoring, apnea, or daytime symptoms occur; and GI, renal, cardiac, or brain imaging guided by findings. Routine MRI in an asymptomatic patient is not supported by a syndrome-specific guideline.

Differential diagnoses include other chromatin-related syndromic neurodevelopmental disorders—particularly ADNP-related Helsmoortel–Van der Aa syndrome, CHAMP1-related disorder, KBG syndrome, Coffin-Siris spectrum, Wiedemann-Steiner syndrome, and CHD8-related disorder—as well as Angelman, Smith-Magenis, and nonsyndromic autism/ID. Molecular testing is usually required to distinguish them.

## 11. Outcome and prognosis

No 5- or 10-year survival, disease-specific mortality, or life-expectancy estimate is available. Available adult and inherited cases indicate survival into adulthood, but cohorts are too young and small for reassurance about normal life expectancy. Morbidity is primarily neurodevelopmental and functional rather than degenerative: communication disability, learning/ID, behavioral or psychiatric comorbidity, hypotonia/gait difficulty, sensory impairment, sleep apnea, obesity, feeding/GI problems, and seizures.

Recovery to a completely unaffected state is not expected, although functional gains can occur with education, therapy, communication support, seizure control, sensory correction, nutritional intervention, and treatment of sleep apnea or GI disease. Variant class/NMD behavior may inform broad severity expectations, but no prognostic biomarker or validated individual prediction model exists. (batzir2020phenotypicexpansionof pages 12-13, nagy2022genotypephenotypecomparisonin pages 1-2)

## 12. Treatment

There is **no approved disease-modifying pharmacotherapy, gene therapy, cell therapy, RNA therapy, or POGZ-targeted therapy**. Management is phenotype based:

* early-intervention services and individualized education;
* speech-language therapy, including augmentative and alternative communication;
* physical and occupational therapy for hypotonia, motor delay, gait, and daily-living skills;
* behavioral therapy and child/adult psychiatry for autism, anxiety, ADHD-like symptoms, compulsive behavior, aggression, or sleep-related behavior;
* conventional antiseizure medication selected by seizure type;
* hearing aids/cochlear or other audiologic intervention where indicated;
* glasses, strabismus treatment, and retinal follow-up where indicated;
* feeding therapy, swallow-safety measures, reflux/constipation treatment, nutrition support, and gastrostomy for severe feeding impairment;
* sleep hygiene, polysomnography, ENT evaluation, adenotonsillar treatment or positive-airway pressure for confirmed obstructive sleep apnea;
* healthy diet, activity support, and longitudinal BMI/metabolic monitoring;
* anomaly-specific surgical care, such as for malrotation, diaphragmatic hernia, clefting, or urinary defects.

Suggested NCIt intervention concepts include **Speech Therapy**, **Occupational Therapy**, **Physical Therapy**, **Behavior Therapy**, **Anticonvulsant Therapy**, **Hearing Aid**, **Nutritional Support**, **Gastrostomy**, and **Continuous Positive Airway Pressure**. There are no syndrome-specific response-rate or adverse-event datasets and no evidence-based combination algorithm.

The only disease-specific registered study recovered was **NCT07380594 (PSY-POGZ)**, a prospective observational—not therapeutic—study at CHU Dijon. It plans 30 genetically confirmed participants aged over six years and uses psychiatric interviews and standardized K-SADS/MINI instruments; it was first posted February 2, 2026 and is therefore outside the requested 2023–2024 priority window. (NCT07380594 chunk 1)

## 13. Prevention

A sporadic de novo pathogenic variant cannot ordinarily be prevented through behavioral or environmental modification. There is no vaccine, medication prophylaxis, newborn biochemical screening, or population screening program.

Primary reproductive prevention options are nondirective genetic counseling, prenatal diagnosis for a known familial variant, and preimplantation genetic testing for monogenic disease. For an apparently de novo case, parental testing refines recurrence counseling but does not eliminate the possibility of germline mosaicism. An affected heterozygous parent has a theoretical 50% transmission probability per pregnancy, with unpredictable severity because of variable expressivity.

Secondary/tertiary prevention consists of early genomic diagnosis, developmental intervention, seizure safety, hearing and vision screening, aspiration prevention, sleep-apnea recognition, weight management, and surveillance/treatment of GI or congenital complications. Cascade testing is appropriate in families with an inherited variant; general-population carrier screening is not justified.

## 14. Other species and natural disease

No naturally occurring WHSUS-equivalent disease in companion animals, livestock, or wildlife was identified, and no breed association or VBO term can currently be recommended. POGZ is evolutionarily conserved and orthologs exist in common research organisms, but comparative conservation alone is not evidence of naturally occurring veterinary disease. There is no transmission or zoonotic potential.

## 15. Model organisms

The best-characterized model is **Mus musculus** (NCBI Taxonomy 10090) with nervous-system-specific conditional Pogz deletion driven by Nestin-Cre. It recapitulates smaller brain, growth impairment, altered neurogenesis, learning and motor deficits, altered sociability, cerebellar transcriptional dysregulation, and Purkinje-cell physiology. Relevant applications include testing the consequences of dosage reduction on neural progenitors, chromatin/transcription, synaptic pathways, cerebellar circuitry, and behavior. (sulimanlavie2020pogzdeficiencyleads pages 2-3, sulimanlavie2020pogzdeficiencyleads pages 1-2)

Important limitations are that homozygous nervous-system knockout is more severe than the typical human heterozygous state, complete germline knockout is embryonic lethal, mouse sociability is not equivalent to human autism, and the model does not reliably reproduce the full human multisystem phenotype. Earlier literature mentions Drosophila and zebrafish approaches, but detailed primary evidence retrieved for this report was insufficient to specify validated WHSUS phenotypic recapitulation. (batzir2020phenotypicexpansionof pages 11-12, nagy2022genotypephenotypecomparisonin pages 2-4)

## Recent-development assessment and evidence gaps

Through 2024, the principal advances were refinement of genotype–phenotype relationships, recognition of inherited/mild disease and rare multisystem complications, and increasingly cell-type-specific mouse studies. The core 2022 result is captured directly in the authors’ abstract: **“Missense variants were more often associated with mild phenotypes (p = 0.0421) and truncating variants predicted to escape NMD presented with more severe phenotypes (p < 0.0001).”** Nagy et al., published January 15, 2022, DOI: https://doi.org/10.3390/genes13010154. (nagy2022genotypephenotypecomparisonin pages 1-2)

The key unresolved needs are a prospective multinational natural-history registry; standardized developmental, psychiatric, sleep, seizure, GI, and quality-of-life measures; adult outcome and mortality data; variant-level functional assays; human iPSC/organoid studies; human single-cell and multi-omic profiling; validated biomarkers; and preclinical evaluation of dosage-restoring or transcript-specific therapies. The currently available frequency estimates should therefore be treated as provisional rather than population-level penetrance figures.

References

1. (batzir2020phenotypicexpansionof pages 1-2): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

2. (OpenTargets Search: White-Sutton syndrome-POGZ): Open Targets Query (White-Sutton syndrome-POGZ, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (murch2022furtherdelineationof pages 1-2): Oliver Murch, Vani Jain, Andreas Benneche, Kay Metcalfe, Emma Hobson, Katrina Prescott, Kate Chandler, Neeti Ghali, Jenny Carmichael, Nicola C. Foulds, Julie Paulsen, Marie F. Smeland, Siren Berland, and Andrew E. Fry. Further delineation of the clinical spectrum of white–sutton syndrome: 12 new individuals and a review of the literature. European Journal of Human Genetics, 30:95-100, Oct 2022. URL: https://doi.org/10.1038/s41431-021-00961-3, doi:10.1038/s41431-021-00961-3. This article has 22 citations and is from a domain leading peer-reviewed journal.

4. (batzir2020phenotypicexpansionof pages 3-5): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

5. (nagy2022genotypephenotypecomparisonin pages 9-10): Dóra Nagy, Sarah Verheyen, Kristen M. Wigby, Artem Borovikov, Artem Sharkov, Valerie Slegesky, Austin Larson, Christina Fagerberg, Charlotte Brasch-Andersen, Maria Kibæk, Ingrid Bader, Rebecca Hernan, Frances A. High, Wendy K. Chung, Jolanda H. Schieving, Jana Behunova, Mateja Smogavec, Franco Laccone, Martina Witsch-Baumgartner, Joachim Zobel, Hans-Christoph Duba, and Denisa Weis. Genotype-phenotype comparison in pogz-related neurodevelopmental disorders by using clinical scoring. Genes, 13:154, Jan 2022. URL: https://doi.org/10.3390/genes13010154, doi:10.3390/genes13010154. This article has 33 citations.

6. (batzir2020phenotypicexpansionof pages 12-13): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

7. (nagy2022genotypephenotypecomparisonin pages 1-2): Dóra Nagy, Sarah Verheyen, Kristen M. Wigby, Artem Borovikov, Artem Sharkov, Valerie Slegesky, Austin Larson, Christina Fagerberg, Charlotte Brasch-Andersen, Maria Kibæk, Ingrid Bader, Rebecca Hernan, Frances A. High, Wendy K. Chung, Jolanda H. Schieving, Jana Behunova, Mateja Smogavec, Franco Laccone, Martina Witsch-Baumgartner, Joachim Zobel, Hans-Christoph Duba, and Denisa Weis. Genotype-phenotype comparison in pogz-related neurodevelopmental disorders by using clinical scoring. Genes, 13:154, Jan 2022. URL: https://doi.org/10.3390/genes13010154, doi:10.3390/genes13010154. This article has 33 citations.

8. (batzir2020phenotypicexpansionof pages 11-12): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

9. (batzir2020phenotypicexpansionof pages 7-8): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

10. (batzir2020phenotypicexpansionof pages 8-9): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

11. (murch2022furtherdelineationof pages 5-6): Oliver Murch, Vani Jain, Andreas Benneche, Kay Metcalfe, Emma Hobson, Katrina Prescott, Kate Chandler, Neeti Ghali, Jenny Carmichael, Nicola C. Foulds, Julie Paulsen, Marie F. Smeland, Siren Berland, and Andrew E. Fry. Further delineation of the clinical spectrum of white–sutton syndrome: 12 new individuals and a review of the literature. European Journal of Human Genetics, 30:95-100, Oct 2022. URL: https://doi.org/10.1038/s41431-021-00961-3, doi:10.1038/s41431-021-00961-3. This article has 22 citations and is from a domain leading peer-reviewed journal.

12. (batzir2020phenotypicexpansionof pages 2-3): Nurit Assia Batzir, Jennifer E. Posey, Xiaofei Song, Zeynep Coban Akdemir, Jill A. Rosenfeld, Chester W. Brown, Emily Chen, Shannon G. Holtrop, Elizabeth Mizerik, Margarita Nieto Moreno, Katelyn Payne, Annick Raas‐Rothschild, Richard Scott, Hilary J. Vernon, Neda Zadeh, James R. Lupski, and V. Reid Sutton. Phenotypic expansion of pogz‐related intellectual disability syndrome (white‐sutton syndrome). American Journal of Medical Genetics Part A, 182:38-52, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61380, doi:10.1002/ajmg.a.61380. This article has 70 citations.

13. (sulimanlavie2020pogzdeficiencyleads pages 1-2): Reut Suliman-Lavie, Ben Title, Yahel Cohen, Nanako Hamada, Maayan Tal, Nitzan Tal, Galya Monderer-Rothkoff, Bjorg Gudmundsdottir, Kristbjorn O. Gudmundsson, Jonathan R. Keller, Guo-Jen Huang, Koh-ichi Nagata, Yosef Yarom, and Sagiv Shifman. Pogz deficiency leads to transcription dysregulation and impaired cerebellar activity underlying autism-like behavior in mice. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19577-0, doi:10.1038/s41467-020-19577-0. This article has 67 citations and is from a highest quality peer-reviewed journal.

14. (sulimanlavie2020pogzdeficiencyleads pages 2-3): Reut Suliman-Lavie, Ben Title, Yahel Cohen, Nanako Hamada, Maayan Tal, Nitzan Tal, Galya Monderer-Rothkoff, Bjorg Gudmundsdottir, Kristbjorn O. Gudmundsson, Jonathan R. Keller, Guo-Jen Huang, Koh-ichi Nagata, Yosef Yarom, and Sagiv Shifman. Pogz deficiency leads to transcription dysregulation and impaired cerebellar activity underlying autism-like behavior in mice. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19577-0, doi:10.1038/s41467-020-19577-0. This article has 67 citations and is from a highest quality peer-reviewed journal.

15. (NCT07380594 chunk 1):  Descriptive Study of Psychiatric Symptoms in White-Sutton Syndrome. Centre Hospitalier Universitaire Dijon. 2026. ClinicalTrials.gov Identifier: NCT07380594

16. (nagy2022genotypephenotypecomparisonin pages 2-4): Dóra Nagy, Sarah Verheyen, Kristen M. Wigby, Artem Borovikov, Artem Sharkov, Valerie Slegesky, Austin Larson, Christina Fagerberg, Charlotte Brasch-Andersen, Maria Kibæk, Ingrid Bader, Rebecca Hernan, Frances A. High, Wendy K. Chung, Jolanda H. Schieving, Jana Behunova, Mateja Smogavec, Franco Laccone, Martina Witsch-Baumgartner, Joachim Zobel, Hans-Christoph Duba, and Denisa Weis. Genotype-phenotype comparison in pogz-related neurodevelopmental disorders by using clinical scoring. Genes, 13:154, Jan 2022. URL: https://doi.org/10.3390/genes13010154, doi:10.3390/genes13010154. This article has 33 citations.

## Artifacts

- [Edison artifact artifact-00](White-Sutton_Syndrome-deep-research-falcon_artifacts/artifact-00.md)