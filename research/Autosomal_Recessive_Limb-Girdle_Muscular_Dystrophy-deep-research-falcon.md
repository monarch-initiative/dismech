---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T10:29:32.805290'
end_time: '2026-06-30T10:49:36.377844'
duration_seconds: 1203.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Limb-Girdle Muscular Dystrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Limb-Girdle Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Limb-Girdle Muscular Dystrophy** covering all of the
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
- **Disease Name:** Autosomal Recessive Limb-Girdle Muscular Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Limb-Girdle Muscular Dystrophy** covering all of the
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


# Comprehensive Research Report: Autosomal Recessive Limb-Girdle Muscular Dystrophy (AR-LGMD)

---

## 1. Disease Information

### Overview
Autosomal recessive limb-girdle muscular dystrophies (AR-LGMDs) are a heterogeneous group of inherited muscular dystrophies characterized by progressive proximal muscle weakness predominantly affecting the shoulder and hip girdle muscles, leading to progressive disability (sun2025recentinsightsinto pages 1-5, sun2025recentinsightsinto pages 5-7). The classification of LGMDs has evolved substantially. At the 2017 European Neuromuscular Centre (ENMC) workshop, a revised nomenclature was established: autosomal dominant forms are designated LGMD D (type 1) and autosomal recessive forms LGMD R (type 2), with currently 31 recognized subtypes—26 of which are autosomal recessive (sun2025recentinsightsinto pages 5-7, sun2025recentinsightsinto pages 1-5). The autosomal recessive forms account for approximately 80–90% of all LGMD cases (sun2025recentinsightsinto pages 1-5, luglio2024hereditaryneuromusculardisorders pages 18-19).

### Key Identifiers
- **MONDO ID:** MONDO:0016971 (limb-girdle muscular dystrophy) (OpenTargets Search: limb-girdle muscular dystrophy)
- **OMIM:** Multiple entries per subtype (e.g., LGMD2A/OMIM #253600; LGMD2B/OMIM #253601; LGMD2C/OMIM #253700; LGMD2D/OMIM #608099; LGMD2E/OMIM #604286; LGMD2I/OMIM #607155)
- **Orphanet:** ORPHA:263 (limb-girdle muscular dystrophy); specific subtypes have individual Orphanet entries
- **ICD-10:** G71.0 (Muscular dystrophy); ICD-11: 8C73 (Limb girdle muscular dystrophy)
- **MeSH:** D049288 (Muscular Dystrophies, Limb-Girdle)

### Synonyms
Common synonyms include: Limb-girdle muscular dystrophy type 2 (LGMD2), Limb-girdle muscular dystrophy autosomal recessive, LGMD-R; subtype-specific names include calpainopathy (LGMDR1), dysferlinopathy (LGMDR2), sarcoglycanopathies (LGMDR3-R6), and dystroglycanopathies (LGMDR9, R11, R13-R15, R20).

---

## 2. Etiology

### Disease Causal Factors
AR-LGMDs are exclusively genetic in origin, caused by biallelic (homozygous or compound heterozygous) pathogenic variants in genes encoding proteins essential for skeletal muscle structure, membrane integrity, and cellular signaling (bouchard2023limb–girdlemusculardystrophies pages 5-6, lin2023clinicalfeaturesimaging pages 1-2). No environmental, infectious, or acquired causes are recognized.

### Genetic Risk Factors
The primary causal genes include CAPN3 (calpain 3), DYSF (dysferlin), SGCA/SGCB/SGCG/SGCD (sarcoglycans α/β/γ/δ), FKRP (fukutin-related protein), ANO5 (anoctamin 5), TCAP (telethonin), and numerous glycosyltransferase genes involved in α-dystroglycan modification (bouchard2023limb–girdlemusculardystrophies pages 5-6, bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2). Consanguinity substantially increases risk in populations with high rates of endogamy (lin2023clinicalfeaturesimaging pages 1-2).

### Gene-Environment Interactions
While no classical gene-environment interactions have been established for AR-LGMD, physical exercise may influence disease expression. In calpainopathy models, zebrafish with capn3b inactivation showed increased susceptibility to muscle defects with elevated muscle activity (akyurek2025zebrafishasa pages 6-7). The role of exercise as a modifying factor in human AR-LGMD is being investigated.

---

## 3. Phenotypes

### Core Phenotypes

**Progressive proximal muscle weakness** (HPO: HP:0003701 - Proximal muscle weakness): The hallmark feature across all AR-LGMD subtypes, affecting pelvic and shoulder girdle muscles with variable age of onset (sun2025recentinsightsinto pages 5-7).

**Elevated serum creatine kinase (CK)** (HPO: HP:0003236 - Elevated circulating creatine kinase concentration): Universally present across subtypes, ranging from 4,000 to over 40,000 U/L. In dysferlinopathy, CK levels reach 50–200 times normal values (anwar2024thedysferlinopathiesconundrum pages 2-3, anwar2024thedysferlinopathiesconundrum pages 3-4, sun2025recentinsightsinto pages 5-7).

**Muscle atrophy and fatty replacement** (HPO: HP:0003202 - Skeletal muscle atrophy): Progressive fibrofatty replacement of muscle tissue is characteristic, with distinct MRI patterns per subtype (bouchard2023limb–girdlemusculardystrophies pages 2-4, lin2023clinicalfeaturesimaging pages 1-2).

### Subtype-Specific Features

- **Calpainopathy (LGMDR1):** Onset 2–53 years; early contractures and scoliosis; approximately 80% of patients become wheelchair-bound between the second and fourth decades of life (lin2023clinicalfeaturesimaging pages 1-2, sun2025recentinsightsinto pages 5-7).
- **Dysferlinopathy (LGMDR2):** Onset typically 13–40 years; characteristic "dysferlin gait" from quadriceps weakness; "diamond-shaped" quadriceps bulge; 15–50% lose ambulation; cardiac involvement is rare (3–10%) but respiratory impairment affects 20–30% (anwar2024thedysferlinopathiesconundrum pages 3-4, bouchard2023limb–girdlemusculardystrophies pages 2-4).
- **Sarcoglycanopathies (LGMDR3–R6):** Usually childhood onset (<10 years); account for 10–15% of LGMD cases; calf hypertrophy; CK 4–180× upper limit of normal; loss of ambulation typically ages 12–16 years; dilated/hypertrophic cardiomyopathy and respiratory failure are important complications (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2).
- **LGMDR9 (FKRP-related):** Variable onset; progressive weakness with ~2% annual decline in respiratory function in adults; median loss of ambulation at age 43 for the common c.826C>A genotype (wicklund2025limbgirdlemusculardystrophy pages 2-3).

### Quality of Life Impact
Overall, approximately 60.8% of LGMD patients experience loss of ambulation, with early childhood-onset forms showing higher rates (71.1% becoming non-ambulatory by mean age 17.7 years) (luglio2024hereditaryneuromusculardisorders pages 18-19). Quality of life is significantly impacted with substantial disability, psychosocial challenges, and the need for multidisciplinary care (anwar2024thedysferlinopathiesconundrum pages 3-4).

### Suggested HPO Terms
- HP:0003701 (Proximal muscle weakness)
- HP:0003236 (Elevated circulating creatine kinase concentration)
- HP:0003202 (Skeletal muscle atrophy)
- HP:0003560 (Muscular dystrophy)
- HP:0001638 (Cardiomyopathy)
- HP:0002747 (Respiratory insufficiency due to muscle weakness)
- HP:0003551 (Difficulty climbing stairs)
- HP:0002359 (Frequent falls)
- HP:0008981 (Calf muscle hypertrophy)
- HP:0001371 (Flexion contracture)
- HP:0002650 (Scoliosis)
- HP:0003391 (Gowers sign)

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

The following table summarizes the major AR-LGMD subtypes with their causal genes:

| New Name | Old Name | Gene Symbol | Protein | Chromosomal Locus | Key Clinical Features | Age of Onset |
|---|---|---|---|---|---|---|
| LGMDR1 | LGMD2A | CAPN3 | Calpain-3 | 15q15.1 | Progressive proximal pelvic/shoulder weakness; early contractures and scoliosis may occur; posterior thigh involvement common; often wheelchair dependence in 2nd-4th decade (bouchard2023limb–girdlemusculardystrophies pages 2-4, lin2023clinicalfeaturesimaging pages 1-2, sun2025recentinsightsinto pages 5-7) | Variable, ~2-53 years; often childhood/adolescence (lin2023clinicalfeaturesimaging pages 1-2, sun2025recentinsightsinto pages 5-7) |
| LGMDR2 | LGMD2B | DYSF | Dysferlin | 2p13.2 | Proximal weakness with gluteus maximus/quadriceps involvement; very high CK; dysferlin gait; fatty replacement of posterior thigh/leg muscles; distal spread later (bouchard2023limb–girdlemusculardystrophies pages 2-4, anwar2024thedysferlinopathiesconundrum pages 2-3, anwar2024thedysferlinopathiesconundrum pages 3-4) | Usually teens to 30s; ~13-40 years (anwar2024thedysferlinopathiesconundrum pages 3-4, anwar2024thedysferlinopathiesconundrum pages 2-3) |
| LGMDR3 | LGMD2D | SGCA | α-Sarcoglycan | 17q21.33 | Pelvic girdle weakness, exercise intolerance, muscle atrophy; sarcoglycanopathy phenotype with possible calf hypertrophy and cardiomyopathy in severe cases (bouchard2023limb–girdlemusculardystrophies pages 2-4, lin2023clinicalfeaturesimaging pages 1-2, wicklund2025limbgirdlemusculardystrophy pages 2-3, sun2025recentinsightsinto pages 5-7) | Usually childhood, often <10 years (wicklund2025limbgirdlemusculardystrophy pages 2-3, sun2025recentinsightsinto pages 5-7) |
| LGMDR4 | LGMD2E | SGCB | β-Sarcoglycan | 4q12 | Weakness with fatty replacement in dorsal, spinal, and limb muscles; often severe sarcoglycanopathy with possible cardiac/respiratory involvement (bouchard2023limb–girdlemusculardystrophies pages 2-4, wicklund2025limbgirdlemusculardystrophy pages 2-3) | Usually childhood (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR5 | LGMD2C | SGCG | γ-Sarcoglycan | 13q12 | Variable severity, including severe childhood form; loss of ambulation before age 13 in severe cases; calf hypertrophy and high CK common (bouchard2023limb–girdlemusculardystrophies pages 2-4, wicklund2025limbgirdlemusculardystrophy pages 2-3) | Usually childhood (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR6 | LGMD2F | SGCD | δ-Sarcoglycan | 5q33.2-q33.3 | Variable sarcoglycanopathy phenotype; proximal weakness with risk of cardiomyopathy/respiratory complications (bouchard2023limb–girdlemusculardystrophies pages 2-4, lin2023clinicalfeaturesimaging pages 1-2, wicklund2025limbgirdlemusculardystrophy pages 2-3) | Usually childhood to adolescence (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR7 | LGMD2G | TCAP | Telethonin | 17q12 | Proximal weakness; relatively enriched in some populations (e.g., Southeast China) with founder variant c.26_33dupAGGTGCG/TCAP duplication reported frequently (bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2) | Variable; often childhood/adolescence (lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR9 | LGMD2I | FKRP | Fukutin-related protein | 19q13.32 | Dystroglycanopathy; progressive proximal weakness, elevated CK, muscle atrophy on MRI; respiratory decline (~2%/year in adults) and cardiomyopathy may occur; genotype influences severity (lin2023clinicalfeaturesimaging pages 1-2, wicklund2025limbgirdlemusculardystrophy pages 2-3) | Variable; often childhood to early adulthood (luglio2024hereditaryneuromusculardisorders pages 18-19, wicklund2025limbgirdlemusculardystrophy pages 2-3) |
| LGMDR11 | LGMD2K | POMT1 | Protein O-mannosyl-transferase 1 | 9q34.13 | Dystroglycanopathy; childhood-onset proximal weakness, may associate with broader multisystem involvement depending on severity (bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2) | Usually childhood (lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR12 | LGMD2L | ANO5 | Anoctamin-5 | 11p14.3 | Adult-onset proximal weakness; often asymmetric or mixed proximal/distal pattern in some patients; elevated CK; slower progression than classic childhood sarcoglycanopathies (OpenTargets Search: limb-girdle muscular dystrophy, wicklund2025limbgirdlemusculardystrophy pages 2-3) | Usually adulthood (wicklund2025limbgirdlemusculardystrophy pages 2-3) |
| LGMDR14 | LGMD2N | POMT2 | Protein O-mannosyl-transferase 2 | 14q24.3 | Dystroglycanopathy; childhood-onset girdle weakness with variable severity, sometimes with extra-muscular involvement in more severe allelic disease (bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2) | Usually childhood (lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR15 | LGMD2O | POMGNT1 | Protein O-linked mannose N-acetylglucosaminyltransferase 1 | 1p34.1 | Dystroglycanopathy; limb-girdle weakness with variable course and possible overlap with congenital muscular dystrophy spectrum (bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2) | Usually childhood (lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR18 | LGMD2S | TRAPPC11 | Trafficking protein particle complex subunit 11 | 4q35.1 | Proximal-distal weakness; reported association with fatty liver disease and diabetes in rare cases (bouchard2023limb–girdlemusculardystrophies pages 4-5, lin2023clinicalfeaturesimaging pages 1-2) | Variable; rare subtype, can present later than previously recognized (lin2023clinicalfeaturesimaging pages 1-2) |
| LGMDR21 | LGMD2Z | POGLUT1 | Protein O-glucosyltransferase 1 | 3q13.33 | Rare recessive LGMD with proximal weakness; linked to defective glycosylation/protein processing pathways (bouchard2023limb–girdlemusculardystrophies pages 5-6) | Variable, often childhood/adolescence (bouchard2023limb–girdlemusculardystrophies pages 5-6) |


*Table: This table summarizes the principal autosomal recessive limb-girdle muscular dystrophy subtypes, aligning old and new nomenclature with causal genes, proteins, loci, and hallmark clinical features. It is useful for rapid comparison across common sarcolemmal, sarcomeric, and dystroglycanopathy-associated forms.*

### Variant Types and Classification
Pathogenic variants across AR-LGMD genes include missense, nonsense, frameshift, splice-site, and structural variants. In calpainopathy, common mutations include c.2120A>G in Chinese populations and c.550del in European populations (lin2023clinicalfeaturesimaging pages 1-2). For dysferlinopathy, more than 600 mutations have been identified across the DYSF gene, with c.2997G>T frequent in Japanese patients and c.1375dup in Chinese patients (lin2023clinicalfeaturesimaging pages 1-2). The common FKRP founder mutation c.826C>A (p.Leu276Ile) is prevalent in European populations (wicklund2025limbgirdlemusculardystrophy pages 2-3). Variants are classified according to ACMG/AMP guidelines, with pathogenic and likely pathogenic variants deposited in ClinVar (OpenTargets Search: limb-girdle muscular dystrophy).

### Founder Effects
Several population-specific founder mutations have been documented: α-sarcoglycan mutations in Acadian populations; FKRP mutations in Hutterite communities; γ-sarcoglycan mutations in Romani (Gypsy) populations; SGCG mutations in Puerto Rican Hispanics; and TCAP c.26_33dupAGGTGTCG in Southeast Chinese populations (83.3% of LGMDR7 cases) (kang2023geneticpatternsof pages 9-10, lin2023clinicalfeaturesimaging pages 1-2).

### OpenTargets Disease-Target Associations
OpenTargets identifies 12 primary targets associated with LGMD (MONDO:0016971), with the highest association scores for CAPN3 (0.86), DYSF (0.86), LMNA (0.85), ANO5 (0.85), SGCA (0.85), SGCB (0.84), FKRP (0.84), GMPPB (0.83), SGCG (0.83), PLEC (0.82), TRAPPC11 (0.81), and DAG1 (0.81) (OpenTargets Search: limb-girdle muscular dystrophy).

---

## 5. Mechanism / Pathophysiology

### Molecular Pathways

The pathophysiology of AR-LGMD involves multiple interconnected cascades initiated by protein dysfunction at the muscle cell membrane:

**Dystrophin-Glycoprotein Complex (DGC) Disruption:** In sarcoglycanopathies, mutations in sarcoglycan genes destabilize the entire sarcoglycan complex and the DGC, which normally links the intracellular cytoskeleton to the extracellular matrix. This compromises sarcolemmal integrity, leading to muscle weakness, atrophy, and potential cardiac/respiratory failure (bozzi2025misregulationofthe pages 17-19, lin2023clinicalfeaturesimaging pages 1-2).

**Calcium Dysregulation:** Muscle membrane damage causes intracellular Ca²⁺ concentration to increase from 100 nM to 1–10 µM, activating calpain 3 protease. This calcium dysregulation initiates a three-level cascade: immediate calpain hyperactivation and protein degradation, middle-term mitochondrial permeability transition pore opening with decreased ATP production, and long-term fiber type conversion from slow-twitch to fast-twitch fibers (sun2025recentinsightsinto pages 14-16).

**Oxidative Stress:** ROS/RNS imbalance occurs with increased NADPH oxidase activity, lipid peroxidation (MDA), and protein carbonylation. ROS damages cell membranes, reduces myosin heavy chain contraction efficiency, and triggers NF-κB-mediated inflammatory cycles (sun2025recentinsightsinto pages 11-14, sun2025recentinsightsinto pages 14-16).

**Chronic Inflammation:** Mutations prevent proper macrophage switching from pro-inflammatory M1 to anti-inflammatory M2 phenotypes, causing sustained pro-inflammatory signaling, excessive cytokine release, and impaired muscle regeneration (sun2025recentinsightsinto pages 11-14).

**Autophagy and Ubiquitin-Proteasome System Dysregulation:** In FKRP-related dystroglycanopathies, mTORC1 hyperactivation correlates with fibrosis and acute regeneration markers. Autophagic flux is dysregulated, with blockage occurring independently of Akt/mTOR signaling changes. ERK1/2 kinase activity is reduced in severe hypoglycosylation cases (bozzi2025misregulationofthe pages 17-19).

**Mitochondrial Dysfunction:** Mitochondrial impairment represents a critical pathogenic mechanism involving impaired biogenesis, dynamics, and autophagy, with decreased ATP production (sun2025recentinsightsinto pages 14-16).

### Subtype-Specific Mechanisms

- **Calpainopathy (CAPN3):** Loss-of-function mutations inactivate the proteolytic function of calpain 3, disrupting Ca²⁺ release, sarcomere remodeling, muscle contraction, and NF-κB signaling (lin2023clinicalfeaturesimaging pages 1-2, bouchard2023limb–girdlemusculardystrophies pages 2-4).
- **Dysferlinopathy (DYSF):** Dysferlin deficiency disrupts Ca²⁺ homeostasis, vesicle trafficking, sarcolemmal resealing, and T-tubule system shaping (lin2023clinicalfeaturesimaging pages 1-2).
- **Dystroglycanopathies (FKRP, POMT1, POMT2, etc.):** Abnormal O-glycosylation of α-dystroglycan leads to impaired ECM binding and sarcolemmal instability (bouchard2023limb–girdlemusculardystrophies pages 5-6).

### Suggested GO Terms
- GO:0043034 (costamere)
- GO:0016529 (sarcoglycan complex)
- GO:0016010 (dystrophin-associated glycoprotein complex)
- GO:0042383 (sarcolemma)
- GO:0006816 (calcium ion transport)
- GO:0006954 (inflammatory response)
- GO:0006979 (response to oxidative stress)
- GO:0006914 (autophagy)

### Suggested Cell Ontology Terms
- CL:0000187 (muscle cell)
- CL:0000188 (cell of skeletal muscle)
- CL:0008002 (skeletal muscle fiber)
- CL:0000235 (macrophage)
- CL:0000057 (fibroblast)

---

## 6. Anatomical Structures Affected

### Primary Organs
- **Skeletal muscle** (UBERON:0001134): Proximal limb-girdle muscles are primary targets, including pelvic girdle (gluteus maximus, quadriceps, hip flexors) and shoulder girdle muscles (sun2025recentinsightsinto pages 5-7, anwar2024thedysferlinopathiesconundrum pages 2-3).
- **Heart** (UBERON:0000948): Cardiomyopathy (dilated or hypertrophic) occurs in sarcoglycanopathies and FKRP-related LGMD; cardiac abnormalities detected in 22% of one Chinese cohort (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2).
- **Respiratory system** (UBERON:0001004): Progressive respiratory muscle weakness with restrictive insufficiency (15.4% in one cohort); adults with LGMDR9 show ~2% annual decline in respiratory function (wicklund2025limbgirdlemusculardystrophy pages 2-3, lin2023clinicalfeaturesimaging pages 1-2).

### Tissue and Cell Level
- Skeletal muscle fibers (type I and type II)
- Sarcolemma and associated protein complexes
- Connective tissue (fibrotic replacement)
- Adipose tissue (fatty infiltration)

### Subcellular Level
- Sarcolemma (GO:0042383)
- Dystrophin-glycoprotein complex (GO:0016010)
- Sarcoplasmic reticulum (calcium handling)
- Mitochondria (GO:0005739)
- Lysosomes/autophagosomes (autophagy pathway)

---

## 7. Temporal Development

### Onset
Age of onset varies substantially by subtype: sarcoglycanopathies typically present in childhood (<10 years); calpainopathy has a wide range (2–53 years, commonly childhood/adolescence); dysferlinopathy presents in the late teens to thirties (13–40 years); LGMDR12 (ANO5) and LGMDR9 often present in adulthood (wicklund2025limbgirdlemusculardystrophy pages 2-3, anwar2024thedysferlinopathiesconundrum pages 3-4, sun2025recentinsightsinto pages 5-7).

### Progression
Disease progression is universally progressive but with variable rates. Sarcoglycanopathies tend toward rapid progression with loss of ambulation in adolescence. Dysferlinopathy shows slow progressive decline, with 15–50% losing ambulation (anwar2024thedysferlinopathiesconundrum pages 3-4). LGMDR9 (FKRP) with the common c.826C>A mutation has a later median age of ambulation loss (43 years) (wicklund2025limbgirdlemusculardystrophy pages 2-3). Calpainopathy results in wheelchair dependence typically in the second to fourth decade (lin2023clinicalfeaturesimaging pages 1-2).

### Patterns
The disease course is chronic, progressive, and lifelong with no spontaneous remission. There are no well-defined disease stages analogous to cancer staging, but clinical milestones include loss of independent ambulation, onset of respiratory support requirement, and cardiac involvement.

---

## 8. Inheritance and Population

### Epidemiology
LGMD prevalence estimates range from 1 in 14,500 to 1 in 123,000 individuals, varying by studied population (luglio2024hereditaryneuromusculardisorders pages 18-19). Calpainopathy (LGMDR1) specifically has an estimated prevalence of 6.8–10.2 per million worldwide and represents 30–40% of all LGMD cases (lin2023clinicalfeaturesimaging pages 1-2). Sarcoglycanopathy prevalence ranges from 0.31–0.58 per 100,000 depending on ethnicity and region (lin2023clinicalfeaturesimaging pages 1-2). The global carrier frequency for all autosomal recessive neuromuscular diseases is approximately 32.9% (OpenTargets Search: limb-girdle muscular dystrophy).

### Inheritance Pattern
All AR-LGMD subtypes follow autosomal recessive inheritance. Both parents must be carriers (heterozygous) for an affected child to be born (25% recurrence risk). Penetrance is generally high (complete or near-complete) for biallelic pathogenic variants, though expressivity is variable—even siblings with identical mutations can show different severity (luglio2024hereditaryneuromusculardisorders pages 18-19, bouchard2023limb–girdlemusculardystrophies pages 2-4).

### Population Demographics
In a Southeast Chinese cohort, LGMDR2 (36.6%) and LGMDR1 (29.3%) were the most common subtypes (lin2023clinicalfeaturesimaging pages 1-2). In the US MD STARnet surveillance network, the most common associated genes were FKRP, CAPN3, ANO5, and DYSF (kang2023geneticpatternsof pages 9-10). In Iranian populations, CAPN3 was the most frequently mutated gene (20%), followed by POMGNT1 and TTN (OpenTargets Search: limb-girdle muscular dystrophy). Geographic and ethnic variation is substantial (kang2023geneticpatternsof pages 9-10, kang2023geneticpatternsof pages 10-10).

---

## 9. Diagnostics

### Clinical Tests

**Serum Creatine Kinase (CK):** Markedly elevated in all subtypes; ranges from 4× to 200× upper limit of normal depending on subtype and stage. Dysferlinopathy characteristically shows CK levels 50–200× normal (anwar2024thedysferlinopathiesconundrum pages 2-3, sun2025recentinsightsinto pages 5-7).

**Muscle Biopsy:** Findings include dystrophic changes (varied fiber sizes, increased internal nuclei, necrosis, regeneration), inflammatory cell infiltration, fibrotic replacement, and fatty deposits. Immunohistochemistry reveals specific protein deficiencies (absent/reduced dysferlin, sarcoglycans, α-dystroglycan hypoglycosylation) (anwar2024thedysferlinopathiesconundrum pages 2-3, sun2025recentinsightsinto pages 5-7).

**Muscle MRI:** Reveals characteristic fatty infiltration patterns that differ by subtype. LGMDR1 shows more severe fatty infiltration of posterior thigh muscles, while LGMDR2 shows edema in lower leg muscles. "Target signs" in rectus femoris and "sandwich signs" in vastus lateralis have high diagnostic value. A "diamond on quadriceps" sign is characteristic of dysferlinopathy (bouchard2023limb–girdlemusculardystrophies pages 2-4, bouchard2023limb–girdlemusculardystrophies pages 11-12, lin2023clinicalfeaturesimaging pages 1-2).

**Electrophysiology:** EMG shows myopathic changes. Nerve conduction studies are typically normal.

**Cardiac monitoring:** Echocardiography and ECG for cardiomyopathy and rhythm disturbances, particularly in sarcoglycanopathies and FKRP-related LGMD (wicklund2025limbgirdlemusculardystrophy pages 2-3).

**Pulmonary function tests:** Forced vital capacity (FVC) monitoring for respiratory decline (wicklund2025limbgirdlemusculardystrophy pages 2-3).

### Genetic Testing
Next-generation sequencing (NGS) is the primary diagnostic approach, including targeted neuromuscular gene panels, whole exome sequencing (WES), and whole genome sequencing (WGS) (bouchard2023limb–girdlemusculardystrophies pages 11-12, lin2023clinicalfeaturesimaging pages 17-18). The diagnostic criteria established by the 2017 ENMC workshop require: (i) proximal or non-proximal muscle dystrophy; (ii) muscle fiber degeneration and necrosis; (iii) elevated serum CK levels; and (iv) muscle degenerative changes with fibrofatty infiltration (sun2025recentinsightsinto pages 5-7). A diagnostic approach typically progresses from clinical assessment and CK measurement, through muscle biopsy with immunohistochemistry, to genetic confirmation via NGS (wicklund2025limbgirdlemusculardystrophy pages 12-12).

### Differential Diagnosis
- Duchenne/Becker muscular dystrophy (X-linked)
- Facioscapulohumeral muscular dystrophy (FSHD)
- Emery-Dreifuss muscular dystrophy
- Metabolic myopathies (Pompe disease/GAA deficiency)
- Inflammatory myopathies (polymyositis, dermatomyositis)
- Congenital muscular dystrophies

### Biomarkers
miR-1, miR-133a, and miR-206 are differentially expressed in serum and muscle of LGMD animal models and change according to the degree of inflammation, fibrosis, muscle regeneration, and disease progression (OpenTargets Search: limb-girdle muscular dystrophy). Glycosylated α-dystroglycan is being evaluated as a biomarker for LGMDR9 severity.

---

## 10. Outcome/Prognosis

### Survival and Morbidity
Life expectancy varies by subtype. Severe sarcoglycanopathies and some dystroglycanopathies may lead to early mortality from cardiac and respiratory complications. Dysferlinopathy and milder forms of calpainopathy have near-normal life expectancy with appropriate cardiac and respiratory management (wicklund2025limbgirdlemusculardystrophy pages 2-3, anwar2024thedysferlinopathiesconundrum pages 3-4). In one Chinese cohort, a patient with LMNA-related muscular dystrophy experienced sudden cardiac death at age 37, highlighting the cardiac risks in certain subtypes (lin2023clinicalfeaturesimaging pages 1-2).

### Complications
- Loss of ambulation (60.8% overall; 71.1% for early childhood-onset forms by mean age 17.7 years) (luglio2024hereditaryneuromusculardisorders pages 18-19)
- Dilated or hypertrophic cardiomyopathy and rhythm disturbances (wicklund2025limbgirdlemusculardystrophy pages 2-3)
- Restrictive respiratory insufficiency (lin2023clinicalfeaturesimaging pages 1-2)
- Scoliosis and joint contractures (sun2025recentinsightsinto pages 5-7)
- Secondary metabolic complications (fatty liver, diabetes reported in rare cases) (lin2023clinicalfeaturesimaging pages 1-2)

---

## 11. Treatment

### Current Symptomatic Management
No curative treatments are currently approved. Management is primarily supportive, including corticosteroids (with limited evidence specific to LGMD), physical therapy, occupational therapy, orthopedic interventions, respiratory support (non-invasive ventilation), and cardiac management (ACE inhibitors, beta-blockers, pacemakers/ICDs as needed) (akyurek2025zebrafishasa pages 6-7, kaur2025towardsacure pages 12-14). MAXO terms: MAXO:0001298 (physical therapy), MAXO:0000016 (respiratory support), MAXO:0001001 (gene therapy).

### Gene Therapy (Experimental)
Gene therapy is the most actively pursued therapeutic modality for AR-LGMD:

**SRP-9003 (bidridistrogene xeboparvovec)** for LGMDR4/LGMD2E: Uses AAVrh74 vector with MHCK7 promoter to deliver full-length β-sarcoglycan gene. Phase 1/2 interim data showed dose-dependent SGCB expression (36.2–62.1% at 60 days) and significant CK reductions (−92.4 to −94.9%), maintained through 2 years with preliminary motor function improvements. Currently in Phase 3 trial (NCT06246513) (kaur2025towardsacure pages 14-16).

**ATA-200** for LGMDR5/LGMD2C: AAV8-based γ-sarcoglycan gene therapy in Phase 1b pediatric trials (NCT05973630) (kaur2025towardsacure pages 12-14).

**SRP-9004 (patidistrogene bexoparvovec)** for LGMDR3/LGMD2D: Completed Phase 1/2 (NCT01976091) with sustained α-sarcoglycan expression at 6 months post-treatment (bouchard2023limb–girdlemusculardystrophies pages 8-9).

**CRISPR/Cas9 approaches** for LGMDR1: Direct correction of CAPN3 mutations through double-strand breaks and wild-type allele insertion, with recent advances in non-viral delivery systems (kaur2025towardsacure pages 14-16).

**Exon skipping:** Antisense oligonucleotides have shown effectiveness in skipping exon 32 in dysferlin in vitro; multi-exon skipping cocktails have successfully corrected SGCG mutations in LGMDR5 patient-derived cell lines, though human clinical trials have not yet been conducted (bouchard2023limb–girdlemusculardystrophies pages 8-9, sun2025recentinsightsinto pages 18-21).

The following table summarizes key clinical trials:

| NCT Number | Study Title (abbreviated) | LGMD Subtype | Intervention/Drug | Phase | Status | Sponsor |
|---|---|---|---|---|---|---|
| NCT00494195 | Gene Transfer Therapy for LGMD2D | LGMD2D / LGMDR3 | AAV gene transfer (alpha-sarcoglycan) | Phase 1 | Completed | Nationwide Children's Hospital (bouchard2023limb–girdlemusculardystrophies pages 8-9) |
| NCT01344798 | AAV1-gamma-sarcoglycan Gene Therapy for LGMD2C | LGMD2C / LGMDR5 | AAV1-gamma-sarcoglycan | Phase 1 | Completed | Genethon (sun2025recentinsightsinto pages 18-21) |
| NCT01976091 | Safety Study of SRP-9004 for LGMD2D | LGMD2D / LGMDR3 | SRP-9004 (patidistrogene bexoparvovec) | Phase 1/2 | Completed | Sarepta Therapeutics, Inc. (bouchard2023limb–girdlemusculardystrophies pages 8-9) |
| NCT05876780 | Single-Dose SRP-9003 Study for LGMD2E/R4 | LGMD2E / LGMDR4 | SRP-9003 (bidridistrogene xeboparvovec; SGCB gene transfer) | Phase 1 | Active, not recruiting | Sarepta Therapeutics, Inc. (bouchard2023limb–girdlemusculardystrophies pages 8-9, kaur2025towardsacure pages 14-16) |
| NCT06246513 | Bidridistrogene Xeboparvovec Trial for LGMD2E/R4 | LGMD2E / LGMDR4 | SRP-9003 / bidridistrogene xeboparvovec | Phase 3 | Active, not recruiting | Sarepta Therapeutics, Inc. (kaur2025towardsacure pages 14-16) |
| NCT05906251 | SRP-6004 Gene Transfer Study for LGMD2B/R2 | LGMD2B / LGMDR2 | SRP-6004 (DYSF gene transfer) | Phase 1 | Terminated | Sarepta Therapeutics, Inc. (bouchard2023limb–girdlemusculardystrophies pages 8-9) |
| NCT05588401 | GenPHSats-bASKet Gene-edited Muscle Stem Cells | LGMD (basket study) | Autologous gene-edited muscle stem cells | Phase 1/2 | Unknown | Charite University, Berlin, Germany (bouchard2023limb–girdlemusculardystrophies pages 8-9) |
| NCT05973630 | ATA-200 for LGMD2C/R5 | LGMD2C / LGMDR5 | ATA-200 (AAV8 gamma-sarcoglycan gene therapy) | Phase 1b | Recruiting/ongoing | Asklepios BioPharmaceutical, Inc. / Atamyo Therapeutics (kaur2025towardsacure pages 12-14) |


*Table: This table summarizes key current and recent gene therapy trials for autosomal recessive LGMD subtypes, including sarcoglycanopathies and dysferlinopathy. It is useful for quickly comparing study phase, status, intervention, and sponsor across the most relevant programs.*

---

## 12. Prevention

### Primary Prevention
No primary prevention exists for AR-LGMD as it is a genetic disorder. Genetic counseling is essential for carrier identification, family planning, and recurrence risk assessment (luglio2024hereditaryneuromusculardisorders pages 18-19).

### Genetic Screening
- **Carrier screening:** Recommended for at-risk family members and populations with high consanguinity rates
- **Prenatal diagnosis:** Available through chorionic villus sampling or amniocentesis when family mutations are known
- **Preimplantation genetic testing (PGT):** Available for families with identified pathogenic variants (luglio2024hereditaryneuromusculardisorders pages 18-19)
- **Cascade screening:** Family members of affected individuals should be offered genetic testing

### Tertiary Prevention
Regular cardiac monitoring, respiratory function assessment, and physical rehabilitation to prevent complications and optimize function (wicklund2025limbgirdlemusculardystrophy pages 2-3).

---

## 13. Model Organisms

### Mouse Models
Multiple mouse models have been developed for AR-LGMD subtypes:

- **Dysferlinopathy:** BLA/J mice (A/J × C57BL/6 hybrid, retrotransposon in Dysf intron 4), extensively used for therapeutic studies; A/J mice (inbred, retrotransposon insertion); SJL/J mice (splice-site mutation with 15% residual dysferlin expression); and 129 and MMex38 strains. These models exhibit varying disease onset and progression patterns (anwar2024thedysferlinopathiesconundrum pages 15-16).
- **Sarcoglycanopathy:** Naturally occurring and genetically modified Sgca, Sgcb, and Sgcg knockout mice recapitulate human disease phenotypes. Sarcospan overexpression in Sgcg-null mice has been shown to protect against LGMDR5 by enabling substitution of γ-sarcoglycan by ζ-sarcoglycan (akyurek2025zebrafishasa pages 7-8).

### Zebrafish Models
Zebrafish (Danio rerio) have become increasingly important for LGMD research:

- **Calpainopathy:** capn3b-inactivated zebrafish generated using CRISPR/Cas9 show muscle damage under challenging conditions (akyurek2025zebrafishasa pages 6-7).
- **Dysferlinopathy:** Morpholino knockdown models used to understand dysferlin's role in muscle structure stabilization and sarcolemma repair (akyurek2025zebrafishasa pages 6-7, akyurek2025zebrafishasa pages 4-6).
- **Sarcoglycanopathies:** CRISPR/Cas9 knockout lines for β-SG and δ-SG showing progressive dystrophic phenotypes mirroring human disease (akyurek2025zebrafishasa pages 7-8, akyurek2025zebrafishasa pages 4-6).
- **Additional models:** TALEN-based exon skipping for collagen VI-related myopathies; morpholino depletion of telethonin/Tcap affecting sarcomere-membrane interaction (akyurek2025zebrafishasa pages 14-16, akyurek2025zebrafishasa pages 8-10).

These models are extensively used for drug screening, gene therapy testing, and understanding pathogenetic mechanisms (akyurek2025zebrafishasa pages 7-8, akyurek2025zebrafishasa pages 14-16).

---

## 14. Environmental Information and Lifestyle Factors

No specific environmental toxins, infectious agents, or lifestyle factors are known to cause AR-LGMD. However, physical exercise and activity patterns may influence disease expression and progression. Aerobic exercise at moderate intensity is generally recommended for maintaining function, while excessive strenuous activity may exacerbate muscle damage. Nutritional optimization and weight management are important supportive measures.

---

## 15. Summary

Autosomal recessive limb-girdle muscular dystrophies represent a complex group of at least 26 genetically distinct conditions unified by progressive proximal muscle weakness. The field has advanced substantially in recent years with the revised ENMC nomenclature system, improved genetic diagnostic capabilities through NGS, and—most promisingly—the emergence of AAV-based gene therapy clinical trials for sarcoglycanopathies and other subtypes. SRP-9003 for LGMDR4 has shown encouraging Phase 1/2 data with significant protein restoration and CK reduction, and has progressed to Phase 3 trials (kaur2025towardsacure pages 14-16). The heterogeneity across and within LGMD subtypes continues to present significant challenges for drug development, necessitating natural history studies and validated clinical outcome assessments to support future therapeutic trials (wicklund2025limbgirdlemusculardystrophy pages 2-3). Multidisciplinary management remains essential, combining cardiac and respiratory surveillance with physical rehabilitation, while gene therapy and other molecular approaches offer hope for disease-modifying treatments in the coming years.

References

1. (sun2025recentinsightsinto pages 1-5): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

2. (sun2025recentinsightsinto pages 5-7): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

3. (luglio2024hereditaryneuromusculardisorders pages 18-19): Agnese Luglio, Elena Maggi, Francesco Nicola Riviello, Alessandro Conforti, Ugo Sorrentino, and Daniela Zuccarello. Hereditary neuromuscular disorders in reproductive medicine. Genes, 15:1409, Oct 2024. URL: https://doi.org/10.3390/genes15111409, doi:10.3390/genes15111409. This article has 8 citations.

4. (OpenTargets Search: limb-girdle muscular dystrophy): Open Targets Query (limb-girdle muscular dystrophy, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (bouchard2023limb–girdlemusculardystrophies pages 5-6): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

6. (lin2023clinicalfeaturesimaging pages 1-2): Feng Lin, Kang Yang, Xin Lin, Ming Jin, Long Chen, Fu-ze Zheng, Liang-liang Qiu, Zhi-xian Ye, Hai-zhu Chen, Min-ting Lin, Ning Wang, and Zhi-qiang Wang. Clinical features, imaging findings and molecular data of limb-girdle muscular dystrophies in a cohort of chinese patients. Orphanet Journal of Rare Diseases, Nov 2023. URL: https://doi.org/10.1186/s13023-023-02897-x, doi:10.1186/s13023-023-02897-x. This article has 17 citations and is from a peer-reviewed journal.

7. (bouchard2023limb–girdlemusculardystrophies pages 4-5): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

8. (akyurek2025zebrafishasa pages 6-7): Eylem Emek Akyürek, Martina Erba, Francesco Dalla Barba, Dorianna Sandonà, and Roberta Sacchetto. Zebrafish as a model organism for research in rare genetic neuromuscular diseases. International Journal of Molecular Sciences, 26:8832, Sep 2025. URL: https://doi.org/10.3390/ijms26188832, doi:10.3390/ijms26188832. This article has 5 citations.

9. (anwar2024thedysferlinopathiesconundrum pages 2-3): Saeed Anwar and Toshifumi Yokota. The dysferlinopathies conundrum: clinical spectra, disease mechanism and genetic approaches for treatments. Biomolecules, 14:256, Feb 2024. URL: https://doi.org/10.3390/biom14030256, doi:10.3390/biom14030256. This article has 15 citations.

10. (anwar2024thedysferlinopathiesconundrum pages 3-4): Saeed Anwar and Toshifumi Yokota. The dysferlinopathies conundrum: clinical spectra, disease mechanism and genetic approaches for treatments. Biomolecules, 14:256, Feb 2024. URL: https://doi.org/10.3390/biom14030256, doi:10.3390/biom14030256. This article has 15 citations.

11. (bouchard2023limb–girdlemusculardystrophies pages 2-4): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

12. (wicklund2025limbgirdlemusculardystrophy pages 2-3): Matthew P. Wicklund, Lindsay N. Alfano, Nicholas E. Johnson, Peter B. Kang, Peter Marks, Katherine D. Mathews, Jerry R. Mendell, Louise Rodino-Klapac, Douglas Sproule, Nicole Verdun, and Kathryn Bryant. Limb-girdle muscular dystrophy scientific workshop: a multistakeholder discussion focused on charting the path forward for drug development. Neurology. Clinical practice, 15 5:e200496, Oct 2025. URL: https://doi.org/10.1212/cpj.0000000000200496, doi:10.1212/cpj.0000000000200496. This article has 1 citations.

13. (kang2023geneticpatternsof pages 9-10): Peter B. Kang, Magali Jorand-Fletcher, Wanfang Zhang, Suzanne W. McDermott, Reba Berry, Chelsea Chambers, Kristen N. Wong, Yara Mohamed, Shiny Thomas, Y Swamy Venkatesh, Christina Westfield, Nedra Whitehead, and Nicholas E. Johnson. Genetic patterns of selected muscular dystrophies in the muscular dystrophy surveillance, tracking, and research network. Neurology Genetics, Dec 2023. URL: https://doi.org/10.1212/nxg.0000000000200113, doi:10.1212/nxg.0000000000200113. This article has 7 citations.

14. (bozzi2025misregulationofthe pages 17-19): Manuela Bozzi, Francesca Sciandra, Maria Giulia Bigotti, and Andrea Brancaccio. Misregulation of the ubiquitin–proteasome system and autophagy in muscular dystrophies associated with the dystrophin–glycoprotein complex. Cells, 14:721, May 2025. URL: https://doi.org/10.3390/cells14100721, doi:10.3390/cells14100721. This article has 2 citations.

15. (sun2025recentinsightsinto pages 14-16): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

16. (sun2025recentinsightsinto pages 11-14): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

17. (kang2023geneticpatternsof pages 10-10): Peter B. Kang, Magali Jorand-Fletcher, Wanfang Zhang, Suzanne W. McDermott, Reba Berry, Chelsea Chambers, Kristen N. Wong, Yara Mohamed, Shiny Thomas, Y Swamy Venkatesh, Christina Westfield, Nedra Whitehead, and Nicholas E. Johnson. Genetic patterns of selected muscular dystrophies in the muscular dystrophy surveillance, tracking, and research network. Neurology Genetics, Dec 2023. URL: https://doi.org/10.1212/nxg.0000000000200113, doi:10.1212/nxg.0000000000200113. This article has 7 citations.

18. (bouchard2023limb–girdlemusculardystrophies pages 11-12): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

19. (lin2023clinicalfeaturesimaging pages 17-18): Feng Lin, Kang Yang, Xin Lin, Ming Jin, Long Chen, Fu-ze Zheng, Liang-liang Qiu, Zhi-xian Ye, Hai-zhu Chen, Min-ting Lin, Ning Wang, and Zhi-qiang Wang. Clinical features, imaging findings and molecular data of limb-girdle muscular dystrophies in a cohort of chinese patients. Orphanet Journal of Rare Diseases, Nov 2023. URL: https://doi.org/10.1186/s13023-023-02897-x, doi:10.1186/s13023-023-02897-x. This article has 17 citations and is from a peer-reviewed journal.

20. (wicklund2025limbgirdlemusculardystrophy pages 12-12): Matthew P. Wicklund, Lindsay N. Alfano, Nicholas E. Johnson, Peter B. Kang, Peter Marks, Katherine D. Mathews, Jerry R. Mendell, Louise Rodino-Klapac, Douglas Sproule, Nicole Verdun, and Kathryn Bryant. Limb-girdle muscular dystrophy scientific workshop: a multistakeholder discussion focused on charting the path forward for drug development. Neurology. Clinical practice, 15 5:e200496, Oct 2025. URL: https://doi.org/10.1212/cpj.0000000000200496, doi:10.1212/cpj.0000000000200496. This article has 1 citations.

21. (kaur2025towardsacure pages 12-14): Devinder Kaur and Akash Ajay. Towards a cure: emerging therapeutic advances for dmd, lgmd, and gnem- insights from pre-clinical and clinical research. Unknown journal, Dec 2025. URL: https://doi.org/10.20944/preprints202512.1267.v1, doi:10.20944/preprints202512.1267.v1.

22. (kaur2025towardsacure pages 14-16): Devinder Kaur and Akash Ajay. Towards a cure: emerging therapeutic advances for dmd, lgmd, and gnem- insights from pre-clinical and clinical research. Unknown journal, Dec 2025. URL: https://doi.org/10.20944/preprints202512.1267.v1, doi:10.20944/preprints202512.1267.v1.

23. (bouchard2023limb–girdlemusculardystrophies pages 8-9): Camille Bouchard and Jacques P. Tremblay. Limb–girdle muscular dystrophies classification and therapies. Journal of Clinical Medicine, 12:4769, Jul 2023. URL: https://doi.org/10.3390/jcm12144769, doi:10.3390/jcm12144769. This article has 73 citations.

24. (sun2025recentinsightsinto pages 18-21): Chen-Chen Sun, Jiang-Ling Xiao, Zhe Zhao, Heng-Yuan Liu, and Chang-Fa Tang. Recent insights into limb-girdle muscular dystrophy: impacts, therapy, and challenges. Histology and histopathology, pages 18929, Apr 2025. URL: https://doi.org/10.14670/hh-18-929, doi:10.14670/hh-18-929. This article has 3 citations and is from a peer-reviewed journal.

25. (anwar2024thedysferlinopathiesconundrum pages 15-16): Saeed Anwar and Toshifumi Yokota. The dysferlinopathies conundrum: clinical spectra, disease mechanism and genetic approaches for treatments. Biomolecules, 14:256, Feb 2024. URL: https://doi.org/10.3390/biom14030256, doi:10.3390/biom14030256. This article has 15 citations.

26. (akyurek2025zebrafishasa pages 7-8): Eylem Emek Akyürek, Martina Erba, Francesco Dalla Barba, Dorianna Sandonà, and Roberta Sacchetto. Zebrafish as a model organism for research in rare genetic neuromuscular diseases. International Journal of Molecular Sciences, 26:8832, Sep 2025. URL: https://doi.org/10.3390/ijms26188832, doi:10.3390/ijms26188832. This article has 5 citations.

27. (akyurek2025zebrafishasa pages 4-6): Eylem Emek Akyürek, Martina Erba, Francesco Dalla Barba, Dorianna Sandonà, and Roberta Sacchetto. Zebrafish as a model organism for research in rare genetic neuromuscular diseases. International Journal of Molecular Sciences, 26:8832, Sep 2025. URL: https://doi.org/10.3390/ijms26188832, doi:10.3390/ijms26188832. This article has 5 citations.

28. (akyurek2025zebrafishasa pages 14-16): Eylem Emek Akyürek, Martina Erba, Francesco Dalla Barba, Dorianna Sandonà, and Roberta Sacchetto. Zebrafish as a model organism for research in rare genetic neuromuscular diseases. International Journal of Molecular Sciences, 26:8832, Sep 2025. URL: https://doi.org/10.3390/ijms26188832, doi:10.3390/ijms26188832. This article has 5 citations.

29. (akyurek2025zebrafishasa pages 8-10): Eylem Emek Akyürek, Martina Erba, Francesco Dalla Barba, Dorianna Sandonà, and Roberta Sacchetto. Zebrafish as a model organism for research in rare genetic neuromuscular diseases. International Journal of Molecular Sciences, 26:8832, Sep 2025. URL: https://doi.org/10.3390/ijms26188832, doi:10.3390/ijms26188832. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy-deep-research-falcon_artifacts/artifact-01.md)