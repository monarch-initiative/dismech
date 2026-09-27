---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T21:06:17.323145'
end_time: '2026-08-18T21:14:57.753330'
duration_seconds: 520.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Late-Onset Pompe Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 9
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Late-Onset_Pompe_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Late-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Late-Onset Pompe Disease** covering all of the
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
- **Disease Name:** Late-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Late-Onset Pompe Disease** covering all of the
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


# Late-Onset Pompe Disease: Comprehensive Disease-Characteristics Report

## Executive summary

Late-onset Pompe disease (LOPD) is a rare, chronic, autosomal-recessive lysosomal glycogen-storage myopathy caused by biallelic pathogenic variants in **GAA**. Partial deficiency of lysosomal acid α-glucosidase causes glycogen accumulation, lysosomal expansion, blocked autophagic flux, metabolic stress, and progressive injury of skeletal and respiratory muscle. Unlike classic infantile Pompe disease, LOPD usually lacks severe hypertrophic cardiomyopathy. Its defining clinical problems are slowly progressive proximal/axial weakness and diaphragmatic respiratory insufficiency, which can occur independently of limb weakness. Diagnosis relies on low GAA activity—usually screened by dried blood spot—and confirmation by molecular testing and/or a second-tissue enzyme assay. Disease-modifying treatment is lifelong enzyme replacement therapy (ERT), supplemented by respiratory, rehabilitative, nutritional, orthopedic, and psychosocial care.

The most authoritative recent clinical source located was the November 2024 MetabERN pathway, developed using systematic review, AGREE II, and GRADE methods [DOI/URL](https://doi.org/10.1186/s13023-024-03373-w). Its central expert position is that Pompe care should be standardized, multidisciplinary, and initiated before irreversible muscle damage develops. (parenti2024theeuropeanreference pages 11-13, parenti2024theeuropeanreference pages 6-8, parenti2024theeuropeanreference pages 13-14)

| Domain | Key facts | Suggested ontology terms |
|---|---|---|
| Disease identity / identifiers | Late-onset Pompe disease (LOPD) is the attenuated, non-classic form of Pompe disease/glycogen storage disease type II caused by deficient lysosomal acid alpha-glucosidase; typically presents after infancy with progressive skeletal and respiratory muscle involvement and little/no hypertrophic cardiomyopathy (labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 1-2) | MONDO: Late-onset Pompe disease *(exact ID not confirmed here)*; OMIM: Pompe disease **232300**; MeSH: Pompe Disease *(ID not confirmed here)* |
| Synonyms | Acid maltase deficiency; glycogen storage disease type II; late-onset acid alpha-glucosidase deficiency; non-classic Pompe disease (parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10) | MONDO exact synonyms *(curate locally)* |
| Data provenance | Information is disease-level, aggregated from guidelines, reviews, cohorts, clinical trials, and registries rather than individual EHR-only evidence (ozdamar2023expertopinionon pages 4-6, parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10) | Evidence model: aggregated disease knowledge |
| Causal gene / inheritance | Caused by biallelic pathogenic variants in **GAA**; autosomal recessive inheritance. Residual GAA activity is higher in LOPD than infantile disease and correlates with attenuated severity (parenti2024theeuropeanreference pages 6-8, labella2023acomprehensiveupdate pages 8-10) | HGNC: **GAA**; GO: glycogen catabolic process; inheritance term: autosomal recessive inheritance |
| Common pathogenic / notable variants | The splice variant **c.-32-13T>G** is the most common in many Caucasian cohorts; substantial allelic heterogeneity exists with hundreds of disease-associated variants. Pseudodeficiency alleles can complicate diagnosis and should not be overcalled as pathogenic (alandydy2019variableclinicalfeatures pages 1-2, moschetti2024mutationspectrumof pages 1-2, giliberto2024frompastto pages 12-15) | Sequence ontology classes: splice-region variant, missense variant, frameshift variant, nonsense variant; ClinVar/ACMG classification terms |
| Hallmark phenotype: proximal/axial weakness | Core phenotype is progressive proximal limb-girdle and axial/paraspinal weakness, often with exercise intolerance, fatigue, and difficulty climbing stairs/rising from chairs (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 2-3) | HPO: **Proximal muscle weakness (HP:0003701)**; **Limb-girdle muscle weakness (HP:0003325)**; **Axial muscle weakness (HP:0003327)**; **Exercise intolerance (HP:0003546)**; **Fatigue (HP:0012378)** |
| Hallmark phenotype: respiratory involvement | Diaphragmatic/intercostal weakness may precede marked limb weakness; restrictive ventilatory insufficiency, sleep-disordered breathing, morning headache, impaired cough, and respiratory failure drive major morbidity/mortality (ozdamar2023expertopinionon pages 3-4, labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 1-2) | HPO: **Respiratory insufficiency (HP:0002093)**; **Restrictive ventilatory defect (HP:0002091)**; **Sleep apnea (HP:0010535)**; **Dyspnea (HP:0002094)** |
| Additional manifestations | HyperCKemia may be present but can be normal; myalgia, scoliosis/spinal deformity, winged scapula, osteopenia/osteoporosis, dysphagia, and reported cerebrovascular abnormalities such as aneurysms/vertebrobasilar dolichoectasia (ozdamar2023expertopinionon pages 3-4, parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 2-3) | HPO: **Elevated creatine kinase (HP:0003236)**; **Myalgia (HP:0003326)**; **Scoliosis (HP:0002650)**; **Dysphagia (HP:0002015)**; **Osteoporosis (HP:0000939)**; **Intracranial aneurysm (HP:0004942)** |
| Anatomy affected | Primary organs/tissues: skeletal muscle and respiratory muscles, especially paraspinal, abdominal, hip extensor, and diaphragm-related musculature; secondary systems include bone, GI/swallowing, and cerebrovascular structures (parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 2-3) | UBERON: skeletal muscle tissue; diaphragm; respiratory system; CL: **skeletal muscle cell/myofiber** *(exact CL ID not confirmed here)*; **macrophage** |
| Temporal course / natural history | Onset is juvenile-to-adult and often insidious. Diagnostic delay may span **5-30 years**; untreated disease shows progressive decline in respiratory function and ambulation, with FVC deterioration detectable within ~2 years and 6MWT decline within ~9 years in natural-history observations summarized by experts (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 4-6) | HPO onset modifiers: juvenile onset, adult onset; course: progressive |
| Core mechanism | Loss of lysosomal GAA prevents normal glycogen hydrolysis, causing lysosomal glycogen accumulation, swollen lysosomes, and progressive myofiber dysfunction; skeletal muscle pathology is strongly linked to autophagic buildup and impaired lysosome-autophagosome fusion (monceau2024decodingthemuscle pages 1-2, do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 4-5) | GO: **glycogen catabolic process**; **lysosome organization**; **autophagy**; **macroautophagy**; GO-CC: **lysosome**; **autophagosome** |
| Downstream molecular pathology | Human and model data show autophagy gene upregulation, reduced mTORC1 activity, AMPK activation, impaired oxidative phosphorylation, mitochondrial/ribosomal dysfunction, oxidative stress, ubiquitinated aggregates, and p62/SQSTM1 accumulation (monceau2024decodingthemuscle pages 1-2, monceau2024decodingthemuscle pages 2-3, moriggi2021muscleproteomicprofile pages 1-2, do2024failureofautophagy pages 5-7) | GO: **regulation of mTOR signaling**; **AMPK signaling** *(pathway label; exact GO term curate locally)*; **mitochondrial ATP synthesis coupled electron transport**; **response to oxidative stress**; **protein ubiquitination** |
| Cell types implicated | Main affected cells are skeletal myofibers; 2024 single-nucleus/spatial transcriptomics also found increased regenerative/slow fibers and macrophages in LOPD muscle (monceau2024decodingthemuscle pages 1-2) | CL: **skeletal muscle cell** *(exact ID not confirmed here)*; **slow-twitch skeletal muscle fiber** *(term curate locally)*; **myoblast/regenerating myonucleus** *(term curate locally)*; **macrophage (CL:0000235)** |
| Omics findings | Single-nucleus RNA-seq plus spatial transcriptomics in **8 LOPD** biopsies and **4 controls** identified early reduced glycolysis, increased lipid/amino-acid metabolism, autophagy activation, and vacuole-specific inflammation/apoptosis/regeneration signals; proteomics found **178** altered proteins, with only **47** normalized after 1 year of ERT (monceau2024decodingthemuscle pages 1-2, moriggi2021muscleproteomicprofile pages 1-2) | GO: **glycolytic process**; **lipid catabolic/metabolic process**; **amino acid metabolic process**; **apoptotic process**; **muscle regeneration** *(curate exact GO term)* |
| Diagnostic approach | First-line screening is **dried blood spot GAA enzyme activity** followed by confirmatory GAA testing in leukocytes/fibroblasts/muscle and/or molecular testing. Normal CK, EMG, or biopsy does **not** exclude LOPD (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 1-2) | NCIT-style diagnostics: dried blood spot assay; enzyme activity assay; molecular genetic testing |
| Diagnostic tests / findings | EMG may show myopathic changes with myotonic discharges, especially in paraspinal muscles; muscle MRI often shows paravertebral/abdominal/hip extensor involvement; biopsy shows vacuolar myopathy with glycogen storage (ozdamar2023expertopinionon pages 3-4, labella2023acomprehensiveupdate pages 8-10) | HPO: **Myopathic EMG abnormalities (HP:0003457)** *(confirm locally)*; pathology term: vacuolar myopathy; imaging term: muscle MRI abnormality |
| Biomarkers / monitoring | CK may be mildly elevated or normal; AST/ALT may rise; urinary **glucose tetrasaccharide/Glc4 (Hex4)**, BNP/pro-BNP, vacuolated PAS-positive lymphocytes, dystromirs (**miR-1-3p, miR-133a-3p, miR-206**), and neurofilament light chain are reported monitoring biomarkers (parenti2024theeuropeanreference pages 6-8, labella2023acomprehensiveupdate pages 8-10, labella2023acomprehensiveupdate pages 21-22, byrne2024longtermsafetyand pages 1-2) | CHEBI: glucose tetrasaccharide *(exact CHEBI ID not confirmed here)*; biomarker labels: CK, BNP, pro-BNP, miR-1-3p, miR-133a-3p, miR-206, NfL |
| Functional monitoring | Recommended serial assessments include seated/supine FVC, polysomnography where indicated, MRC/manual muscle testing, 6-minute walk test, timed tests, hand-held dynamometry, ECG/echocardiography, and periodic brain/cerebrovascular imaging in selected patients (ozdamar2023expertopinionon pages 4-6, parenti2024theeuropeanreference pages 11-13, parenti2024theeuropeanreference pages 6-8, labella2023acomprehensiveupdate pages 8-10) | NCIT-style procedures: spirometry; polysomnography; 6-minute walk test; electromyography; echocardiography; magnetic resonance imaging |
| Differential diagnosis | Limb-girdle muscular dystrophies, inflammatory myopathies, mitochondrial disorders, other glycogenoses, and oculopharyngeal muscular dystrophy should be considered; pseudodeficiency alleles can mimic low enzyme activity (parenti2024theeuropeanreference pages 11-13, ozdamar2023expertopinionon pages 1-2, giliberto2024frompastto pages 12-15) | Differential set terms: limb-girdle muscular dystrophy; inflammatory myopathy; mitochondrial myopathy; oculopharyngeal muscular dystrophy |
| Epidemiology / population | Rare disease; often cited prevalence/incidence is roughly **1 in 40,000-57,000**, with under-recognition likely. Geographic/population carrier frequencies and predicted prevalence vary substantially, including higher predicted prevalence in some East Asian datasets (alandydy2019variableclinicalfeatures pages 1-2, sharshakova2026pompediseasepathogenesis pages 1-2, aguilargonzalez2022isogenicgaakomurine pages 1-2) | ORDO/epidemiology labels: rare disease; prevalence estimate |
| Prognosis / burden | Chronic lifelong disorder with reduced survival in adult/non-classic Pompe disease and substantial HRQoL impact. Respiratory insufficiency remains a major cause of morbidity and mortality despite ERT (ozdamar2023expertopinionon pages 1-2, byrne2024longtermsafetyand pages 1-2) | HPO: **Reduced life expectancy (HP:0003676)** *(use cautiously)*; patient-reported outcome domains: physical function, fatigue, mobility, self-care |
| Approved disease-modifying therapy: alglucosidase alfa | First-generation recombinant human GAA; licensed dose **20 mg/kg every 2 weeks IV**. Improves/stabilizes 6MWT and FVC, but benefit often plateaus after ~2-3 years with later decline in many patients (labella2023acomprehensiveupdate pages 11-12, parenti2024theeuropeanreference pages 13-14) | NCIT-style intervention: **Enzyme Replacement Therapy**; drug label: **alglucosidase alfa** |
| Approved disease-modifying therapy: avalglucosidase alfa | Next-generation rhGAA with enhanced mannose-6-phosphate targeting; approved FDA 2021 / EMA 2022. In expert-summary data, FVC gain at week 49 was **2.89% vs 0.46%** for alglucosidase comparator (ozdamar2023expertopinionon pages 4-6, parenti2024theeuropeanreference pages 13-14) | NCIT-style intervention: **Enzyme Replacement Therapy**; drug label: **avalglucosidase alfa** |
| Approved disease-modifying therapy: cipaglucosidase alfa + miglustat | Two-component therapy approved in adults with LOPD (EMA 2023 noted in guideline evidence). Long-term studies show maintained/stable respiratory and walking outcomes with biomarker improvement; phase I/II used **20 mg/kg IV biweekly cipaglucosidase alfa + 260 mg oral miglustat** (byrne2024longtermsafetyand pages 1-2, parenti2024theeuropeanreference pages 13-14) | NCIT-style interventions: **Enzyme Replacement Therapy** + **Pharmacological Chaperone Therapy/Enzyme Stabilizer**; drug labels: **cipaglucosidase alfa**, **miglustat** |
| Supportive care | Multidisciplinary management includes pulmonary support/ventilation, airway clearance, physical therapy, swallowing/nutrition assessment, orthopedic/bone health management, psychological care, pregnancy planning, and QoL monitoring (parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 2-3) | NCIT-style interventions: noninvasive ventilation; physical therapy; occupational therapy; nutritional support; speech/swallow therapy |
| Experimental / active trials | **RESOLUTE (NCT04093349)**: AAV gene transfer (**SPK-3006**), phase 1/2, active-not-recruiting, adults on prior ERT; additional interventional studies include **S-606001** add-on therapy (**NCT07123155**) and extension (**NCT07750990**) (NCT04093349 chunk 1, NCT07123155 chunk 1, NCT07750990 chunk 1) | NCIT-style intervention: **Gene Therapy**; AAV vector gene transfer; small-molecule add-on therapy |
| Prevention / screening | No primary environmental prevention. Secondary prevention centers on newborn screening where available, early recognition of asymptomatic/presymptomatic cases, carrier testing, cascade family testing, reproductive counseling, and early treatment before fixed muscle damage (ozdamar2023expertopinionon pages 4-6, labella2023acomprehensiveupdate pages 8-10) | NCIT-style interventions: newborn screening; carrier screening; genetic counseling; cascade screening |
| Environmental / infectious factors | No established infectious cause. No convincing environmental toxin/lifestyle cause for disease occurrence; non-genetic factors mainly influence complications and management rather than primary causation (labella2023acomprehensiveupdate pages 8-10, ozdamar2023expertopinionon pages 1-2) | Not applicable / no established environmental etiologic ontology term |
| Model organisms / natural disease | Key preclinical systems include **Gaa knockout mouse**, murine GAA-KO muscle cell lines, and naturally occurring animal models including **Japanese quail**; models recapitulate lysosomal glycogen storage and autophagic pathology and are used for ERT/gene-therapy development (aguilargonzalez2022isogenicgaakomurine pages 1-2, do2024failureofautophagy pages 7-8) | NCBI Taxon: **Mus musculus**; **Coturnix japonica**; model types: knockout mouse, muscle cell line, natural animal model |


*Table: This compact table summarizes the most actionable disease-knowledge fields for late-onset Pompe disease, including genetics, core phenotypes, mechanisms, diagnostics, therapies, epidemiology, and models. It is designed for rapid knowledge-base curation with conservative ontology suggestions and evidence-linked claims.*

## 1. Disease information

**Definition and category.** LOPD is the attenuated juvenile/adult spectrum of Pompe disease, a Mendelian lysosomal storage disorder, glycogen storage disease, metabolic myopathy, and autophagic myopathy. Common names are **glycogen storage disease type II**, **acid maltase deficiency**, **acid α-glucosidase deficiency**, non-classic Pompe disease, juvenile-onset Pompe disease, and adult-onset Pompe disease. LOPD is generally defined by onset after infancy and residual enzyme activity; boundaries based on age vary among publications. (aguilargonzalez2022isogenicgaakomurine pages 1-2, ozdamar2023expertopinionon pages 1-2)

**Identifiers.** Pompe disease is **OMIM 232300**. Appropriate disease-level mappings include MeSH *Pompe Disease*, Orphanet *Pompe disease*, and ICD-10-CM **E74.02** (Pompe disease). ICD-11 places Pompe disease under glycogen-storage disorders. The exact LOPD-specific MONDO identifier was not verified in the retrieved evidence and should be resolved directly against the current MONDO release rather than inferred. The evidence summarized here is aggregated from guidelines, cohorts, trials, and disease registries—not individual EHR records.

A concise abstract statement from the 2023 review is: **“Pompe disease … is an autosomal recessive disorder caused by mutations in the GAA gene.”** [Published August 2023; DOI/URL](https://doi.org/10.3390/biom13091279). (labella2023acomprehensiveupdate pages 8-10)

## 2. Etiology, risk, protection, and gene–environment interaction

The necessary cause is **biallelic germline GAA dysfunction**. GAA, at chromosome 17q25, encodes lysosomal acid α-glucosidase, which hydrolyzes α-1,4 and α-1,6 glycogen linkages. LOPD commonly retains approximately 2–40% assay-dependent residual activity, versus <1% in classic infantile disease; residual activity broadly predicts phenotype but does not completely explain expressivity. (moschetti2024mutationspectrumof pages 1-2, parenti2024theeuropeanreference pages 6-8)

The major “risk factors” are therefore two pathogenic parental alleles, family history, ancestry-associated founder/common alleles, and consanguinity. The European splice variant **NM_000152.5:c.-32-13T>G** is particularly common in affected White populations and permits some correctly spliced transcript. In one 18-person LOPD cohort it occurred in 16/18 patients. More than 900 disease-associated GAA variants have been catalogued across missense, nonsense, frameshift, splice, indel, and larger rearrangement classes. (alandydy2019variableclinicalfeatures pages 1-2, moschetti2024mutationspectrumof pages 1-2)

No toxin, infection, smoking behavior, diet, occupation, or radiation exposure is an established primary cause. Exercise, nutrition, intercurrent infection, and respiratory care can alter function or complications but do not determine whether genetically susceptible individuals have Pompe disease. No validated protective GAA allele, environmental prevention, or reproducible disease-modifier gene is established for routine clinical use. Exercise-gene polymorphisms and other modifiers remain investigational. Gene–environment interaction evidence is therefore limited chiefly to how activity, nutrition, aging, infection, and treatment interact with a fixed enzymatic defect.

## 3. Phenotypes and quality of life

LOPD is heterogeneous and insidious. Core manifestations are:

* **Proximal lower-limb and limb-girdle weakness** (HP:0003701/HP:0003325), difficulty climbing stairs or rising from a chair, waddling gait, and exercise intolerance (HP:0003546).
* **Axial/paraspinal weakness** (HP:0003327), lumbar hyperlordosis, scapular winging, scoliosis (HP:0002650), and later contractures.
* **Respiratory-muscle and diaphragmatic weakness**, restrictive ventilatory defect (HP:0002091), orthopnea/dyspnea, impaired cough, sleep-disordered breathing or sleep apnea (HP:0010535), morning headache, recurrent infection, and respiratory failure (HP:0002093). Respiratory dysfunction may precede conspicuous limb weakness and is the principal cause of morbidity and mortality. (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 2-3, ozdamar2023expertopinionon pages 1-2)
* **Laboratory abnormalities:** CK may be normal or elevated—sometimes up to 15-fold—while AST/ALT can be mildly elevated. Normal CK does not exclude disease. (ozdamar2023expertopinionon pages 3-4, labella2023acomprehensiveupdate pages 8-10)
* **Other multisystem findings:** fatigue (HP:0012378), myalgia (HP:0003326), dysphagia (HP:0002015), feeding/nutritional difficulties, low bone density/osteoporosis (HP:0000939), and occasional hearing, gastrointestinal, urinary, or cerebrovascular abnormalities. Intracranial aneurysm and vertebrobasilar dolichoectasia have been reported, but their population frequency and screening yield remain uncertain. Cardiac disease is usually absent or mild, although occasional cardiomyopathy occurs. (alandydy2019variableclinicalfeatures pages 1-2, parenti2024theeuropeanreference pages 11-13)

Severity ranges from asymptomatic hyperCKemia to wheelchair and ventilator dependence. In one small cohort, 12/18 used BiPAP, 5/18 had scoliosis, 3/18 cardiomyopathy, and 2/18 cerebral aneurysm; these are descriptive referral-cohort frequencies, not generalizable prevalence estimates. (alandydy2019variableclinicalfeatures pages 1-2)

LOPD impairs mobility, self-care, work, social participation, fatigue, and emotional well-being. PROMIS, EQ-5D-5L, Rasch-built Pompe-specific Activity, and Subject’s Global Impression of Change are relevant instruments. In PROPEL, 90% receiving cipaglucosidase alfa plus miglustat versus 59% receiving alglucosidase/placebo were responders for perceived ability to move around at week 52 (P=0.0005). (byrne2024longtermsafetyand pages 1-2)

## 4. Genetic and molecular information

**Causal gene:** **GAA**; germline, autosomal recessive, loss-of-function. Variants may reduce transcription/splicing, folding, lysosomal trafficking, proteolytic maturation, or catalytic activity. The phenotype reflects the combined residual function of both alleles, but genotype–phenotype correlation is imperfect. In a 2024 Italian screen of 2,934 symptomatic referrals, 39 had low enzyme activity plus two causal variants and 22 carried variants of uncertain significance. (moschetti2024mutationspectrumof pages 2-3, moschetti2024mutationspectrumof pages 3-5)

Variant interpretation should follow ACMG/AMP and ClinGen Lysosomal Diseases Variant Curation Expert Panel specifications. Pseudodeficiency alleles lower activity against artificial substrates without causing Pompe disease. **c.271G>A (p.Asp91Asn)** was classified as benign in the cited analysis; overcalling it can produce inappropriate ERT and obscure another diagnosis. Sequence analysis should be supplemented by deletion/duplication analysis if two explanatory alleles are not found; RNA studies can resolve cryptic splice variants. Allele frequencies must be checked variant-by-variant in current gnomAD/ClinVar releases. (giliberto2024frompastto pages 12-15)

No recurrent aneuploidy, translocation, repeat expansion, mitochondrial-DNA defect, or somatic driver defines LOPD. CMA, karyotyping, FISH, and repeat-expansion testing are not first-line tests. Disease-specific epigenetic alterations are not validated diagnostic or prognostic markers.

## 5. Environmental information

Environmental, infectious, and lifestyle causes are **not applicable as primary etiology**. Respiratory infections can precipitate decompensation; immobility aggravates deconditioning, osteoporosis, and contractures. Carefully prescribed aerobic and resistance activity, adequate protein/energy intake, vaccination, airway clearance, and avoidance of prolonged inactivity support health but do not correct GAA deficiency.

## 6. Mechanism and pathophysiology

The causal chain is:

**biallelic GAA loss → deficient lysosomal glycogen hydrolysis → glycogen-filled/swollen lysosomes → lysosomal rupture/trafficking disturbance and failed autophagosome–lysosome fusion → autophagic debris, p62/SQSTM1 and ubiquitinated-protein accumulation → AMPK activation, reduced mTORC1 signaling, altered TFEB activity, oxidative stress and mitochondrial dysfunction → myofibrillar disorganization, apoptosis/regeneration, weakness and respiratory failure.** (monceau2024decodingthemuscle pages 1-2, do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 4-5)

Autophagic lesions in adult muscle may exceed the apparent lysosomal enlargement; biopsies show autophagic vacuoles in approximately 30–40% of fibers, and buildup can occupy up to 40% of fiber volume in knockout mice. Type II myofibers are particularly affected in models. Autophagic debris also impedes recombinant-enzyme delivery, helping explain incomplete skeletal-muscle response. TFEB overexpression or experimental mTORC1 restoration can reverse buildup in model systems, but neither is established human therapy. Suggested annotations include GO *glycogen catabolic process*, *macroautophagy*, *lysosome organization*, *response to oxidative stress*, and GO cellular components *lysosome* and *autophagosome*. Principal CL mapping is skeletal muscle cell/myofiber; macrophages and regenerative myogenic cells are downstream participants. (do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 4-5)

**Recent multi-omics.** A 2024 study applied single-nucleus RNA-seq to biopsies from eight LOPD patients and four matched controls and spatially compared normal, non-vacuolated, and vacuolated fibers. Early non-vacuolated fibers had reduced glycolysis with increased lipid/amino-acid metabolism; affected tissue showed more slow/regenerative fibers and macrophages, autophagy upregulation, reduced ribosomal/mitochondrial programs, and defective oxidative phosphorylation. Inflammation, apoptosis, and regeneration were concentrated in vacuolated fibers. [Published July 2024; DOI/URL](https://doi.org/10.1093/brain/awae249). (monceau2024decodingthemuscle pages 1-2, monceau2024decodingthemuscle pages 2-3)

Proteomics identified 178 altered muscle proteins, of which only 47 normalized after one year of ERT; oxidative metabolism, contractile regulation, cytoskeletal remodeling, ER stress, unfolded-protein response, and lysosomal-tethering abnormalities persisted. [Published March 2021; DOI/URL](https://doi.org/10.3390/ijms22062850). (moriggi2021muscleproteomicprofile pages 1-2, moriggi2021muscleproteomicprofile pages 16-17)

## 7. Anatomical structures

Primary involvement is bilateral, generally symmetric skeletal muscle: pelvic-girdle, hip extensors, thigh, paraspinal/axial, abdominal-wall, diaphragm, and intercostal muscles. Respiratory muscle involvement may be disproportionate. Secondary targets include bulbar/swallowing musculature, bone, smooth muscle, and cerebral arterial walls. The relevant subcellular compartments are lysosome, autophagosome, mitochondrion, ER, and cytosol. Suggested UBERON mappings include skeletal muscle tissue, diaphragm, abdominal muscle, paraspinal muscle, respiratory system, and cerebral artery. (parenti2024theeuropeanreference pages 11-13, labella2023acomprehensiveupdate pages 8-10)

## 8. Temporal development

Onset may occur from childhood through late adulthood and is usually chronic and insidious. Disease is lifelong, variably progressive, and does not spontaneously remit. Diagnostic delay is commonly **5–30 years**, and nearly one-third of patients may initially receive another diagnosis. Untreated natural-history summaries report detectable FVC deterioration within approximately two years and 6-minute-walk deterioration over longer intervals, around nine years, although individual trajectories vary greatly. Early treatment is the main modifiable prognostic opportunity because established fatty replacement and autophagic destruction are incompletely reversible. (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 4-6)

## 9. Inheritance and population

Inheritance is autosomal recessive: each pregnancy of two heterozygous carriers has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Penetrance for genuinely pathogenic biallelic genotypes is high but age-dependent; expressivity is markedly variable. Anticipation is not recognized. Germline mosaicism is theoretically possible but not a characteristic feature.

Frequently cited overall Pompe prevalence is approximately **1:40,000–1:57,000**, but newborn sequencing estimates suggest underdiagnosis and marked ancestry variation. Population-database modeling estimated carrier frequencies of 1.7% in Koreans and 0.7% in Japanese, corresponding to predicted genetic prevalences of 1:13,657 and 1:78,013; such predictions include uncertainty from penetrance and variant classification. Both sexes are affected approximately equally. (alandydy2019variableclinicalfeatures pages 1-2, aguilargonzalez2022isogenicgaakomurine pages 1-2)

## 10. Diagnostics and screening

**Recommended pathway:** recognize unexplained proximal/axial weakness, diaphragmatic restriction, exercise intolerance, or hyperCKemia → dried-blood-spot GAA assay → confirm low activity in leukocytes, fibroblasts, or muscle and identify two pathogenic/likely pathogenic GAA alleles. A second independent method is important because sample quality and pseudodeficiency can cause false positives. (ozdamar2023expertopinionon pages 3-4, ozdamar2023expertopinionon pages 1-2)

Assess CK, AST/ALT, urinary Glc4/Hex4, seated and supine FVC, maximal inspiratory/expiratory pressures, sleep study/oximetry, cough flow, MRC strength, dynamometry, timed tests, and 6MWT. A >25% seated-to-supine FVC fall suggests diaphragmatic weakness. EMG may show myopathy and paraspinal myotonic discharges without clinical myotonia. MRI characteristically identifies paraspinal, abdominal, and hip-extensor involvement. Biopsy—now reserved for unresolved cases—shows PAS-positive, acid-phosphatase-positive glycogen vacuoles and autophagic pathology. (ozdamar2023expertopinionon pages 3-4, labella2023acomprehensiveupdate pages 8-10)

Potential monitoring biomarkers include urinary Glc4/Hex4, CK, BNP/pro-BNP where cardiac disease is suspected, vacuolated PAS-positive lymphocytes, miR-1-3p/miR-133a-3p/miR-206, and neurofilament light; none replaces clinical respiratory and motor assessment. (parenti2024theeuropeanreference pages 6-8, labella2023acomprehensiveupdate pages 21-22)

Differentials include limb-girdle muscular dystrophy, inflammatory or mitochondrial myopathy, other glycogenoses, spinal muscular disease, congenital myopathy, Danon disease, and oculopharyngeal muscular dystrophy. Normal CK, EMG, or biopsy does not exclude LOPD. (giliberto2024frompastto pages 12-15, ozdamar2023expertopinionon pages 3-4, parenti2024theeuropeanreference pages 11-13)

WES/WGS or neuromuscular panels are useful when phenotype is atypical or single-gene analysis is incomplete; RNA sequencing can establish splice effects. Newborn screening, presymptomatic sibling testing, carrier/cascade screening, prenatal diagnosis, and preimplantation genetic testing are technically feasible after familial variants are known.

## 11. Outcome and prognosis

Respiratory insufficiency, infection, and progressive neuromuscular disability dominate morbidity and mortality. Adult survival is reduced, but robust contemporary 5- or 10-year survival percentages are not established because of rarity, phenotypic heterogeneity, and treatment-era change. Prognosis is better with earlier diagnosis, greater baseline motor/FVC reserve, lower fixed fatty replacement, and sustained treatment. ERT generally improves or stabilizes function initially but does not reliably reverse advanced disease; many patients plateau after two to three years and subsequently decline. (byrne2024longtermsafetyand pages 1-2, labella2023acomprehensiveupdate pages 11-12)

## 12. Treatment and real-world implementation

* **Alglucosidase alfa:** recombinant human GAA, 20 mg/kg IV every two weeks; first approved in 2006. The 90-person LOTS trial improved/stabilized 6MWD and percent-predicted FVC. Infusion reactions and anti-drug antibodies occur; skeletal-muscle uptake and durability are limited. (labella2023acomprehensiveupdate pages 11-12, parenti2024theeuropeanreference pages 13-14)
* **Avalglucosidase alfa:** second-generation rhGAA enriched for mannose-6-phosphate receptor targeting, 20 mg/kg every two weeks. COMET established non-inferiority to alglucosidase; an expert summary reported week-49 FVC gains of 2.89 versus 0.46 percentage points, without statistically confirmed superiority. FDA approval was in 2021 and EMA approval in 2022. (ozdamar2023expertopinionon pages 4-6, labella2023acomprehensiveupdate pages 11-12)
* **Cipaglucosidase alfa plus miglustat:** high-M6P rhGAA plus an oral enzyme stabilizer. A phase I/II regimen used cipaglucosidase 20 mg/kg IV plus miglustat 260 mg orally every two weeks. At up to 48 months, ambulatory ERT-experienced patients maintained approximately 5–6% predicted 6MWD improvement, while ERT-naïve patients had approximately 10–12%; FVC was stable in experienced patients and improved 3–8% in the small naïve cohort. CK and Hex4 improved, with safety resembling alglucosidase. EMA approval occurred in 2023; subsequent US approval applies to selected adults inadequately responding to current ERT. [Published December 2024; DOI/URL](https://doi.org/10.1007/s00415-023-12096-0). (byrne2024longtermsafetyand pages 1-2, parenti2024theeuropeanreference pages 13-14)

Suggested NCIT intervention concepts are *enzyme replacement therapy*, *alglucosidase alfa*, *avalglucosidase alfa*, *cipaglucosidase alfa*, *miglustat*, *noninvasive ventilation*, *physical therapy*, and *gene therapy*; exact codes should be validated against the current NCIT release.

Supportive management includes individualized submaximal aerobic/resistance therapy without overwork injury, stretching and contracture prevention, mobility aids, noninvasive ventilation, airway-clearance/cough-assist techniques, vaccination, prompt infection treatment, swallowing and nutritional assessment, bone-health care, occupational therapy, and psychosocial support. ERT should begin promptly in symptomatic patients and in presymptomatic patients with objective weakness or respiratory abnormality; clinically silent individuals require approximately six-month surveillance. (ozdamar2023expertopinionon pages 4-6, parenti2024theeuropeanreference pages 11-13)

**Experimental therapy.** RESOLUTE (**NCT04093349**) is an active-not-recruiting phase 1/2 dose-escalation study of AAV vector **SPK-3006** in adults previously treated with ERT; four participants were enrolled, with five-year safety and immune follow-up. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT04093349). Gene therapy’s goals are sustained endogenous GAA secretion and cross-correction, but capsid immunity, transgene immunity, dose toxicity, durability, and skeletal-muscle delivery remain unresolved. (NCT04093349 chunk 1)

## 13. Prevention

There is no vaccine, exposure avoidance, or lifestyle intervention that prevents the genetic disease. **Primary genetic prevention/options** include carrier testing, genetic counseling, prenatal diagnosis, and preimplantation genetic testing. **Secondary prevention** comprises newborn/cascade screening and treatment before irreversible weakness. **Tertiary prevention** includes ERT, respiratory surveillance/support, vaccination, airway clearance, safe exercise, fall/contracture prevention, bone care, and nutrition. Each sibling of an affected individual should receive targeted familial-variant and/or enzyme testing.

## 14. Natural disease in other species

Pompe-like natural GAA deficiency has been described in Japanese quail (*Coturnix japonica*, NCBI Taxon 93934), with additional spontaneous glycogen-storage models reported across domestic species. It is inherited/metabolic, not transmissible or zoonotic. Comparative pathology includes lysosomal glycogen storage and muscle dysfunction, although species differ in severity, cardiac involvement, and treatment response. (aguilargonzalez2022isogenicgaakomurine pages 1-2)

## 15. Model organisms

The principal model is the **Gaa-knockout mouse** (*Mus musculus*, Taxon 10090), which reproduces absent enzyme, skeletal/cardiac glycogen storage, weakness, autophagic buildup, and impaired ERT delivery. Its limitations are severe/null-genotype biology, strain-dependent phenotype, and imperfect modeling of decades-long human LOPD. Japanese quail offers a natural model. CRISPR-generated GAA-knockout murine myotubes reproduce absent activity, glycogen excess, increased autophagy, and reduced cation-independent mannose-6-phosphate receptor and support ERT/gene-therapy screening. Human fibroblasts, primary myoblasts, and patient-derived iPSC muscle systems provide genotype-specific in-vitro models but incompletely reproduce mature muscle architecture and systemic respiratory disease. (aguilargonzalez2022isogenicgaakomurine pages 1-2, do2024failureofautophagy pages 7-8)

## Evidence limitations

Phenotype percentages are highly cohort-dependent; several manifestations lack population-level frequency estimates. Variant frequencies and ontology identifiers should be revalidated against live ClinVar, gnomAD, HPO, MONDO, UBERON, GO, CL, CHEBI, and NCIT releases before database ingestion. Most retrieved sources reported DOI rather than PMID metadata; therefore, DOI-linked primary papers are supplied rather than inventing unverified PMIDs. The strongest 2023–2024 evidence comprises expert pathways/reviews, small rare-disease cohorts, and extension studies; comparative long-term effectiveness among newer ERTs remains uncertain without direct head-to-head trials.

References

1. (parenti2024theeuropeanreference pages 11-13): Giancarlo Parenti, Simona Fecarotta, Marianna Alagia, Federica Attaianese, Alessandra Verde, Antonietta Tarallo, Vincenza Gragnaniello, Athanasia Ziagaki, Maria Jose’ Guimaraes, Patricio Aguiar, Andreas Hahn, Olga Azevedo, Maria Alice Donati, Beata Kiec-Wilk, Maurizio Scarpa, Nadine A. M. E. van der Beek, Mireja Del Toro Riera, Dominique P. Germain, Hidde Huidekoper, Johanna M. P. van den Hout, Ans T. van der Ploeg, Ivo Baric, Spyros Batzios, Nadia Belmatoug, Andrea Bordugo, Annet M. Bosch, Anais Brassier, Alberto Burlina, David Cassiman, Brigitte Chabrol, Efstathia Chronopoulou, Maria Luz Couce-Pico, Niklas Darin, Anibh M. Das, Francois G. Debray, Patrick Deegan, Luisa M. de Abreu Freire Diogo Matos, Javier De Las Heras Montero, Maja Di Rocco, Dries Dobbelaere, Francois Eyskens, Ana Ferreira, Ana M. Gaspar, Serena Gasperini, Antonio González-Meneses López, Salvatore Grosso, Nathalie Guffon-Fouilhoux, Julia Hennermann, Tarekegn G. Hiwot, Simon Jones, Sandra Kingma, Veroniki Komninaka, Elena Martín-Hernández, Esmeralda Martins, Diana Miclea, György Pfliegler, Esmeralda Rodrigues, Dariusz Rokicki, Dominique Roland, Frank Rutsch, Alessandro Salviati, Ivailo Tournev, Kurt Ullrich, Peter M. van Hasselt, Suresh Vijay, Natalie Weinhold, Peter Witters, and Jiri Zeman. The european reference network for metabolic diseases (metabern) clinical pathway recommendations for pompe disease (acid maltase deficiency, glycogen storage disease type ii). Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03373-w, doi:10.1186/s13023-024-03373-w. This article has 28 citations and is from a peer-reviewed journal.

2. (parenti2024theeuropeanreference pages 6-8): Giancarlo Parenti, Simona Fecarotta, Marianna Alagia, Federica Attaianese, Alessandra Verde, Antonietta Tarallo, Vincenza Gragnaniello, Athanasia Ziagaki, Maria Jose’ Guimaraes, Patricio Aguiar, Andreas Hahn, Olga Azevedo, Maria Alice Donati, Beata Kiec-Wilk, Maurizio Scarpa, Nadine A. M. E. van der Beek, Mireja Del Toro Riera, Dominique P. Germain, Hidde Huidekoper, Johanna M. P. van den Hout, Ans T. van der Ploeg, Ivo Baric, Spyros Batzios, Nadia Belmatoug, Andrea Bordugo, Annet M. Bosch, Anais Brassier, Alberto Burlina, David Cassiman, Brigitte Chabrol, Efstathia Chronopoulou, Maria Luz Couce-Pico, Niklas Darin, Anibh M. Das, Francois G. Debray, Patrick Deegan, Luisa M. de Abreu Freire Diogo Matos, Javier De Las Heras Montero, Maja Di Rocco, Dries Dobbelaere, Francois Eyskens, Ana Ferreira, Ana M. Gaspar, Serena Gasperini, Antonio González-Meneses López, Salvatore Grosso, Nathalie Guffon-Fouilhoux, Julia Hennermann, Tarekegn G. Hiwot, Simon Jones, Sandra Kingma, Veroniki Komninaka, Elena Martín-Hernández, Esmeralda Martins, Diana Miclea, György Pfliegler, Esmeralda Rodrigues, Dariusz Rokicki, Dominique Roland, Frank Rutsch, Alessandro Salviati, Ivailo Tournev, Kurt Ullrich, Peter M. van Hasselt, Suresh Vijay, Natalie Weinhold, Peter Witters, and Jiri Zeman. The european reference network for metabolic diseases (metabern) clinical pathway recommendations for pompe disease (acid maltase deficiency, glycogen storage disease type ii). Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03373-w, doi:10.1186/s13023-024-03373-w. This article has 28 citations and is from a peer-reviewed journal.

3. (parenti2024theeuropeanreference pages 13-14): Giancarlo Parenti, Simona Fecarotta, Marianna Alagia, Federica Attaianese, Alessandra Verde, Antonietta Tarallo, Vincenza Gragnaniello, Athanasia Ziagaki, Maria Jose’ Guimaraes, Patricio Aguiar, Andreas Hahn, Olga Azevedo, Maria Alice Donati, Beata Kiec-Wilk, Maurizio Scarpa, Nadine A. M. E. van der Beek, Mireja Del Toro Riera, Dominique P. Germain, Hidde Huidekoper, Johanna M. P. van den Hout, Ans T. van der Ploeg, Ivo Baric, Spyros Batzios, Nadia Belmatoug, Andrea Bordugo, Annet M. Bosch, Anais Brassier, Alberto Burlina, David Cassiman, Brigitte Chabrol, Efstathia Chronopoulou, Maria Luz Couce-Pico, Niklas Darin, Anibh M. Das, Francois G. Debray, Patrick Deegan, Luisa M. de Abreu Freire Diogo Matos, Javier De Las Heras Montero, Maja Di Rocco, Dries Dobbelaere, Francois Eyskens, Ana Ferreira, Ana M. Gaspar, Serena Gasperini, Antonio González-Meneses López, Salvatore Grosso, Nathalie Guffon-Fouilhoux, Julia Hennermann, Tarekegn G. Hiwot, Simon Jones, Sandra Kingma, Veroniki Komninaka, Elena Martín-Hernández, Esmeralda Martins, Diana Miclea, György Pfliegler, Esmeralda Rodrigues, Dariusz Rokicki, Dominique Roland, Frank Rutsch, Alessandro Salviati, Ivailo Tournev, Kurt Ullrich, Peter M. van Hasselt, Suresh Vijay, Natalie Weinhold, Peter Witters, and Jiri Zeman. The european reference network for metabolic diseases (metabern) clinical pathway recommendations for pompe disease (acid maltase deficiency, glycogen storage disease type ii). Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03373-w, doi:10.1186/s13023-024-03373-w. This article has 28 citations and is from a peer-reviewed journal.

4. (labella2023acomprehensiveupdate pages 8-10): Beatrice Labella, Stefano Cotti Piccinelli, Barbara Risi, Filomena Caria, Simona Damioli, Enrica Bertella, Loris Poli, Alessandro Padovani, and Massimiliano Filosto. A comprehensive update on late-onset pompe disease. Biomolecules, 13:1279, Aug 2023. URL: https://doi.org/10.3390/biom13091279, doi:10.3390/biom13091279. This article has 76 citations.

5. (ozdamar2023expertopinionon pages 1-2): Sevim Erdem Ozdamar, Ayse Filiz Koc, Hacer Durmus Tekce, Dilcan Kotan, Ahmet Hakan Ekmekci, Ihsan Sukru Sengun, Ayse Nur Yuceyar, and Kayihan Uluc. Expert opinion on the diagnostic odyssey and management of late-onset pompe disease: a neurologist's perspective. Frontiers in Neurology, May 2023. URL: https://doi.org/10.3389/fneur.2023.1095134, doi:10.3389/fneur.2023.1095134. This article has 14 citations and is from a peer-reviewed journal.

6. (ozdamar2023expertopinionon pages 4-6): Sevim Erdem Ozdamar, Ayse Filiz Koc, Hacer Durmus Tekce, Dilcan Kotan, Ahmet Hakan Ekmekci, Ihsan Sukru Sengun, Ayse Nur Yuceyar, and Kayihan Uluc. Expert opinion on the diagnostic odyssey and management of late-onset pompe disease: a neurologist's perspective. Frontiers in Neurology, May 2023. URL: https://doi.org/10.3389/fneur.2023.1095134, doi:10.3389/fneur.2023.1095134. This article has 14 citations and is from a peer-reviewed journal.

7. (alandydy2019variableclinicalfeatures pages 1-2): Jousef Alandy-dy, Marie Wencel, Kathy Hall, Julie Simon, Yanjun Chen, Erik Valenti, Jade Yang, Deeksha Bali, Anita Lakatos, Namita Goyal, Tahseen Mozaffar, and Virginia Kimonis. Variable clinical features and genotype-phenotype correlations in 18 patients with late-onset pompe disease. Annals of Translational Medicine, 7:276-276, Jul 2019. URL: https://doi.org/10.21037/atm.2019.06.48, doi:10.21037/atm.2019.06.48. This article has 25 citations.

8. (moschetti2024mutationspectrumof pages 1-2): Marta Moschetti, Alessia Lo Curto, Miriam Giacomarra, Daniele Francofonte, Carmela Zizzo, Elisa Messina, Giovanni Duro, and Paolo Colomba. Mutation spectrum of gaa gene in pompe disease: current knowledge and results of an italian study. International Journal of Molecular Sciences, 25:9139, Aug 2024. URL: https://doi.org/10.3390/ijms25179139, doi:10.3390/ijms25179139. This article has 9 citations.

9. (giliberto2024frompastto pages 12-15): F. Giliberto, P. Buonfiglio, Gabriel Capellino, C. L. Massini, Viviana Dalamón, L. Luce, M. Carcione, C. M. –. Roentgen, and Prof. PhD. Florencia Giliberto. From past to present: pompe disease, pseudodeficiency alleles, and diagnostic challenges. MedRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.03.24314698, doi:10.1101/2024.10.03.24314698. This article has 0 citations.

10. (ozdamar2023expertopinionon pages 3-4): Sevim Erdem Ozdamar, Ayse Filiz Koc, Hacer Durmus Tekce, Dilcan Kotan, Ahmet Hakan Ekmekci, Ihsan Sukru Sengun, Ayse Nur Yuceyar, and Kayihan Uluc. Expert opinion on the diagnostic odyssey and management of late-onset pompe disease: a neurologist's perspective. Frontiers in Neurology, May 2023. URL: https://doi.org/10.3389/fneur.2023.1095134, doi:10.3389/fneur.2023.1095134. This article has 14 citations and is from a peer-reviewed journal.

11. (ozdamar2023expertopinionon pages 2-3): Sevim Erdem Ozdamar, Ayse Filiz Koc, Hacer Durmus Tekce, Dilcan Kotan, Ahmet Hakan Ekmekci, Ihsan Sukru Sengun, Ayse Nur Yuceyar, and Kayihan Uluc. Expert opinion on the diagnostic odyssey and management of late-onset pompe disease: a neurologist's perspective. Frontiers in Neurology, May 2023. URL: https://doi.org/10.3389/fneur.2023.1095134, doi:10.3389/fneur.2023.1095134. This article has 14 citations and is from a peer-reviewed journal.

12. (monceau2024decodingthemuscle pages 1-2): Alexandra Monceau, Rasya Gokul Nath, Xavier Suárez-Calvet, Olimpia Musumeci, Antonio Toscano, Biruta Kierdaszuk, Anna Kostera-Pruszczyk, Cristina Domínguez-González, Aurelio Hernández-Lain, Carmen Paradas, Eloy Rivas, George Papadimas, Constantinos Papadopoulos, Margarita Chrysanthou-Piterou, Eduard Gallardo, Montse Olivé, James Lilleker, Mark E Roberts, Domenica Marchese, Giulia Lunazzi, Holger Heyn, Esther Fernández-Simón, Elisa Villalobos, James Clark, Panos Katsikis, Catherine Collins, Priyanka Mehra, Zoe Laidler, Amy Vincent, Giorgio Tasca, Chiara Marini-Bettolo, Michela Guglieri, Volker Straub, Nina Raben, and Jordi Díaz-Manera. Decoding the muscle transcriptome of patients with late-onset pompe disease reveals markers of disease progression. Brain, 147:4213-4226, Jul 2024. URL: https://doi.org/10.1093/brain/awae249, doi:10.1093/brain/awae249. This article has 9 citations and is from a highest quality peer-reviewed journal.

13. (do2024failureofautophagy pages 7-8): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 17 citations.

14. (do2024failureofautophagy pages 4-5): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 17 citations.

15. (monceau2024decodingthemuscle pages 2-3): Alexandra Monceau, Rasya Gokul Nath, Xavier Suárez-Calvet, Olimpia Musumeci, Antonio Toscano, Biruta Kierdaszuk, Anna Kostera-Pruszczyk, Cristina Domínguez-González, Aurelio Hernández-Lain, Carmen Paradas, Eloy Rivas, George Papadimas, Constantinos Papadopoulos, Margarita Chrysanthou-Piterou, Eduard Gallardo, Montse Olivé, James Lilleker, Mark E Roberts, Domenica Marchese, Giulia Lunazzi, Holger Heyn, Esther Fernández-Simón, Elisa Villalobos, James Clark, Panos Katsikis, Catherine Collins, Priyanka Mehra, Zoe Laidler, Amy Vincent, Giorgio Tasca, Chiara Marini-Bettolo, Michela Guglieri, Volker Straub, Nina Raben, and Jordi Díaz-Manera. Decoding the muscle transcriptome of patients with late-onset pompe disease reveals markers of disease progression. Brain, 147:4213-4226, Jul 2024. URL: https://doi.org/10.1093/brain/awae249, doi:10.1093/brain/awae249. This article has 9 citations and is from a highest quality peer-reviewed journal.

16. (moriggi2021muscleproteomicprofile pages 1-2): Manuela Moriggi, Daniele Capitanio, Enrica Torretta, Pietro Barbacini, Cinzia Bragato, Patrizia Sartori, Maurizio Moggio, Lorenzo Maggi, Marina Mora, and Cecilia Gelfi. Muscle proteomic profile before and after enzyme replacement therapy in late-onset pompe disease. International Journal of Molecular Sciences, 22:2850, Mar 2021. URL: https://doi.org/10.3390/ijms22062850, doi:10.3390/ijms22062850. This article has 19 citations.

17. (do2024failureofautophagy pages 5-7): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 17 citations.

18. (labella2023acomprehensiveupdate pages 21-22): Beatrice Labella, Stefano Cotti Piccinelli, Barbara Risi, Filomena Caria, Simona Damioli, Enrica Bertella, Loris Poli, Alessandro Padovani, and Massimiliano Filosto. A comprehensive update on late-onset pompe disease. Biomolecules, 13:1279, Aug 2023. URL: https://doi.org/10.3390/biom13091279, doi:10.3390/biom13091279. This article has 76 citations.

19. (byrne2024longtermsafetyand pages 1-2): Barry J. Byrne, Benedikt Schoser, Priya S. Kishnani, Drago Bratkovic, Paula R. Clemens, Ozlem Goker-Alpan, Xue Ming, Mark Roberts, Matthias Vorgerd, Kumaraswamy Sivakumar, Ans T. van der Ploeg, Mitchell Goldman, Jacquelyn Wright, Fred Holdbrook, Vipul Jain, Elfrida R. Benjamin, Franklin Johnson, Sheela Sitaraman Das, Yasmine Wasfi, and Tahseen Mozaffar. Long-term safety and efficacy of cipaglucosidase alfa plus miglustat in individuals living with pompe disease: an open-label phase i/ii study (atb200-02). Journal of Neurology, 271:1787-1801, Dec 2024. URL: https://doi.org/10.1007/s00415-023-12096-0, doi:10.1007/s00415-023-12096-0. This article has 24 citations and is from a domain leading peer-reviewed journal.

20. (sharshakova2026pompediseasepathogenesis pages 1-2): Alexandra Sharshakova, Alisa Fattakhova, Valeriya Solovyeva, Albert Sufianov, Galina Sufianova, Grigorii Kutovoi, and Albert Rizvanov. Pompe disease: pathogenesis, molecular mechanisms, neurological aspects, diagnostics and modern therapeutic approaches. International Journal of Molecular Sciences, 27:3703, Apr 2026. URL: https://doi.org/10.3390/ijms27083703, doi:10.3390/ijms27083703. This article has 1 citations.

21. (aguilargonzalez2022isogenicgaakomurine pages 1-2): Araceli Aguilar-González, Juan Elías González-Correa, Eliana Barriocanal-Casado, Iris Ramos-Hernández, Miguel A. Lerma-Juárez, Sara Greco, Juan José Rodríguez-Sevilla, Francisco Javier Molina-Estévez, Valle Montalvo-Romeral, Giuseppe Ronzitti, Rosario María Sánchez-Martín, Francisco Martín, and Pilar Muñoz. Isogenic gaa-ko murine muscle cell lines mimicking severe pompe mutations as preclinical models for the screening of potential gene therapy strategies. International Journal of Molecular Sciences, 23:6298, Jun 2022. URL: https://doi.org/10.3390/ijms23116298, doi:10.3390/ijms23116298. This article has 5 citations.

22. (labella2023acomprehensiveupdate pages 11-12): Beatrice Labella, Stefano Cotti Piccinelli, Barbara Risi, Filomena Caria, Simona Damioli, Enrica Bertella, Loris Poli, Alessandro Padovani, and Massimiliano Filosto. A comprehensive update on late-onset pompe disease. Biomolecules, 13:1279, Aug 2023. URL: https://doi.org/10.3390/biom13091279, doi:10.3390/biom13091279. This article has 76 citations.

23. (NCT04093349 chunk 1):  A Gene Transfer Study for Late-Onset Pompe Disease (RESOLUTE). Spark Therapeutics, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04093349

24. (NCT07123155 chunk 1):  Study of S-606001 as an Add-on to Enzyme Replacement Therapy (ERT) in Participants With Late-onset Pompe Disease (LOPD). Shionogi. 2025. ClinicalTrials.gov Identifier: NCT07123155

25. (NCT07750990 chunk 1):  An Extension Study of S-606001 in Participants With Late-onset Pompe Disease (LOPD). Shionogi. 2026. ClinicalTrials.gov Identifier: NCT07750990

26. (moschetti2024mutationspectrumof pages 2-3): Marta Moschetti, Alessia Lo Curto, Miriam Giacomarra, Daniele Francofonte, Carmela Zizzo, Elisa Messina, Giovanni Duro, and Paolo Colomba. Mutation spectrum of gaa gene in pompe disease: current knowledge and results of an italian study. International Journal of Molecular Sciences, 25:9139, Aug 2024. URL: https://doi.org/10.3390/ijms25179139, doi:10.3390/ijms25179139. This article has 9 citations.

27. (moschetti2024mutationspectrumof pages 3-5): Marta Moschetti, Alessia Lo Curto, Miriam Giacomarra, Daniele Francofonte, Carmela Zizzo, Elisa Messina, Giovanni Duro, and Paolo Colomba. Mutation spectrum of gaa gene in pompe disease: current knowledge and results of an italian study. International Journal of Molecular Sciences, 25:9139, Aug 2024. URL: https://doi.org/10.3390/ijms25179139, doi:10.3390/ijms25179139. This article has 9 citations.

28. (moriggi2021muscleproteomicprofile pages 16-17): Manuela Moriggi, Daniele Capitanio, Enrica Torretta, Pietro Barbacini, Cinzia Bragato, Patrizia Sartori, Maurizio Moggio, Lorenzo Maggi, Marina Mora, and Cecilia Gelfi. Muscle proteomic profile before and after enzyme replacement therapy in late-onset pompe disease. International Journal of Molecular Sciences, 22:2850, Mar 2021. URL: https://doi.org/10.3390/ijms22062850, doi:10.3390/ijms22062850. This article has 19 citations.

## Artifacts

- [Edison artifact artifact-00](Late-Onset_Pompe_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.