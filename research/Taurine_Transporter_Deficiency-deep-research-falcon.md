---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T01:01:38.592468'
end_time: '2026-08-20T01:11:55.035774'
duration_seconds: 616.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Taurine transporter deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Taurine_Transporter_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Taurine transporter deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Taurine transporter deficiency** covering all of the
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
- **Disease Name:** Taurine transporter deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Taurine transporter deficiency** covering all of the
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


# Taurine Transporter Deficiency: Comprehensive Disease-Characteristics Report

## Executive summary

Taurine transporter deficiency is an exceptionally rare autosomal-recessive disorder caused by biallelic pathogenic variants in **SLC6A6**, which encodes the sodium/chloride-dependent taurine transporter TauT. Its most reproducible human manifestation is congenital or early-childhood retinal dystrophy; cardiomyopathy is clinically important but variably expressed. Affected patients have markedly reduced plasma taurine and severely impaired cellular taurine uptake. The only reported disease-directed treatment is oral taurine supplementation. In two siblings with a hypomorphic allele, 100 mg/kg/day normalized blood taurine, reversed systolic cardiomyopathy after 24 months, and stabilized retinal disease in the younger child. These results are promising but remain case-level evidence, not evidence from a controlled trial. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 1-2)

The human evidence base is extremely small: the original report comprised two siblings, while the latest multicenter study—conducted during 2019–2025 and published online December 4, 2025—added seven affected individuals from four families. No disease-specific primary human publication from 2023–2024 was identified; recent 2023–2024 literature primarily advances broader understanding of taurine biology rather than this Mendelian condition itself. (ullah2026earlyonsetretinopathyin pages 1-2)

| domain | best-supported finding | evidence type/strength | suggested ontology terms |
|---|---|---|---|
| Disease / gene / inheritance | Taurine transporter deficiency is a Mendelian disorder caused by biallelic loss-of-function or severe hypomorphic variants in **SLC6A6** (TauT), with autosomal recessive segregation in all reported families. Human evidence currently includes 2 affected siblings in one consanguineous family and 7 affected individuals from 4 unrelated families. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 1-2) | Direct human genetic and clinical evidence; strongest available but based on very small case series | SLC6A6; taurine transporter deficiency; autosomal recessive inheritance; MONDO term label if added in future |
| Retinal phenotype | Core phenotype is early-onset retinal degeneration spanning **Leber congenital amaurosis / early-onset retinal dystrophy** with poor vision or nystagmus from birth or early childhood, extinguished or severely depressed ERG, macular atrophy, pigmentary degeneration, and photoreceptor loss on OCT. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 3-4, ullah2026earlyonsetretinopathyin pages 1-2) | Direct human clinical evidence; consistent across all known cases | HP: Nystagmus; HP: Visual impairment; HP: Night blindness; HP: Abnormal electroretinogram; HP: Macular atrophy; HP: Retinal degeneration; Leber congenital amaurosis; early-onset retinal dystrophy |
| Cardiac phenotype | Cardiomyopathy was prominent in the 2020 family, with mild hypokinetic cardiomyopathy, systolic dysfunction, and LV dilation; in the expanded cohort, a shared structural cardiomyopathy phenotype was **not** consistently present, though short PR intervals were recurrent and cardiology follow-up was advised. (ansar2020taurinetreatmentof pages 2-4, ansar2020taurinetreatmentof pages 4-5, ullah2026earlyonsetretinopathyin pages 3-4, ullah2026earlyonsetretinopathyin pages 7-8) | Direct human evidence; variable expressivity, small numbers | HP: Cardiomyopathy; HP: Left ventricular dilatation; HP: Systolic dysfunction; HP: Short PR interval; cardiovascular system |
| Biochemical marker | Fasting plasma taurine is markedly reduced in affected individuals; the index family had nearly undetectable levels (**6–7 μmol/L**), and the multicenter cohort showed significantly lower taurine versus carriers and controls. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 1-2) | Direct human biochemical evidence; strong disease biomarker | taurine (CHEBI:15891); HP: Abnormal circulating amino acid concentration; low plasma taurine |
| Pathogenic variants | Reported disease-associated variants include **NM_003043.5:c.1196G>T p.(Gly399Val)** with ~15% residual transport, **NM_003043.6:c.746C>T p.(Thr249Ile)**, **c.880G>A p.(Ala294Thr)**, **c.1210-2389_1348-331del p.(Phe404_Glu449del)**, and **c.338G>A p.(Trp113Ter)**. Missense variants showed severe to complete transport loss; truncating/deletion alleles support loss of function. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 5-6, ullah2026earlyonsetretinopathyin pages 3-4, ullah2026earlyonsetretinopathyin pages 1-2) | Direct human molecular evidence with functional validation for key alleles | SLC6A6 missense variant; nonsense variant; exon deletion; loss of function; hypomorphic allele |
| Diagnosis | Best-supported diagnostic approach is **molecular testing of SLC6A6** in patients with LCA/EORD plus **fasting plasma taurine measurement**, retinal phenotyping (visual acuity, full-field ERG, multimodal imaging/OCT), and where possible functional transport or membrane-trafficking assays in HEK-293 cells or patient fibroblasts. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 1-2) | Direct human evidence; practical but not yet standardized by guidelines | whole-exome sequencing; genome sequencing; Sanger confirmation; electroretinography; optical coherence tomography; plasma taurine assay |
| Treatment | **Oral taurine supplementation** is the only disease-directed intervention reported. In the index family, **100 mg/kg/day** normalized blood taurine, reversed systolic cardiomyopathy after 24 months, and arrested retinal degeneration with clinical visual improvement in the younger child; a later retinal-only case normalized plasma taurine on **1–2 g/day** but had no short-term ophthalmic improvement. No side effects were reported in the treated family. (ansar2020taurinetreatmentof pages 1-2, ansar2020taurinetreatmentof pages 4-5, ullah2026earlyonsetretinopathyin pages 4-5) | Direct human therapeutic evidence; promising but limited to anecdotal/case evidence | taurine supplementation; oral administration; NCIT term label: Dietary Supplementation; investigational therapy |
| Mechanism / pathophysiology | Disease mechanism is impaired TauT-mediated taurine uptake from biallelic **SLC6A6** dysfunction, causing cellular taurine deficiency. Human functional work shows markedly reduced or absent transport; modeling places pathogenic residues in transmembrane regions important for ligand recognition, folding, trafficking, and transport cycling. Review/model literature supports downstream osmotic, mitochondrial, oxidative-stress, calcium-handling, and anti-apoptotic defects. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 5-6, baliou2020significanceoftaurine pages 4-6, baliou2020significanceoftaurine pages 8-9) | Mixed evidence: direct human functional evidence for transport loss; broader downstream mechanisms mainly model/review inference | sodium/chloride-dependent taurine transport; plasma membrane; mitochondrial dysfunction; oxidative stress; apoptosis; osmoregulation |
| Affected anatomy / cells | Highest-confidence affected structures are **retina** and **heart**. Within retina, human OCT/ERG data and model literature support major involvement of **photoreceptors**; retinal ganglion cell vulnerability is supported mainly by depletion models. Cardiac myocytes are implicated by the cardiomyopathy phenotype. (ansar2020taurinetreatmentof pages 2-4, ansar2020taurinetreatmentof pages 4-5, surai2021taurineasa pages 3-5) | Retina/heart: direct human evidence; specific cell-type detail partly inferred from models | UBERON: retina; UBERON: heart; photoreceptor cell; retinal ganglion cell; cardiomyocyte |
| Animal models | **Slc6a6/TauT knockout mice** develop retinal degeneration, cardiomyopathy/cardiac atrophy, skeletal muscle abnormalities, reproductive defects, and age-related multi-organ manifestations; chemically induced taurine depletion also causes photoreceptor and retinal ganglion cell loss. Taurine-deficient cats and dogs provide natural/comparative evidence for retinal degeneration and reversible cardiomyopathy. (ansar2020taurinetreatmentof pages 4-5, baliou2020significanceoftaurine pages 6-7, baliou2020significanceoftaurine pages 7-8, ullah2026earlyonsetretinopathyin pages 9-9) | Model and veterinary evidence; strong biologic support but indirect for human disease spectrum | knockout mouse model; taurine depletion model; retinal degeneration; dilated cardiomyopathy |
| Epidemiology / gaps | Prevalence, incidence, carrier frequency, penetrance, genotype-phenotype correlations, long-term natural history, and formal management guidelines are **not established**. No disease-specific registered interventional trial was identified in the tool search; current evidence remains based on rare case reports/series. (ullah2026earlyonsetretinopathyin pages 1-2, ullah2026earlyonsetretinopathyin pages 7-8) | Evidence gap / absence of data | rare disease; unknown prevalence; unknown penetrance; research gap |
| Recent developments | The key recent advance is the expanded multicenter cohort published online in **2025** showing 7 affected individuals from 4 families, broader allelic heterogeneity, consistent retinal phenotype, and functional confirmation of complete taurine transport loss for missense variants. No disease-specific 2023–2024 primary human expansion was identified in the retrieved evidence. (ullah2026earlyonsetretinopathyin pages 1-2, ullah2026earlyonsetretinopathyin pages 5-6) | Direct human evidence for 2025 expansion; explicit 2023–2024 evidence gap | cohort expansion; variant spectrum; functional validation |


*Table: This table summarizes the best-supported knowledge for SLC6A6-related taurine transporter deficiency across clinical, molecular, mechanistic, and translational domains. It is designed for knowledge-base use and clearly separates direct human evidence from model-based inference and current evidence gaps.*

## 1. Disease information

### Definition and scope

Taurine transporter deficiency is a **Mendelian membrane-transport disorder** in which deficient TauT activity prevents normal cellular accumulation of taurine. The clinical spectrum currently includes **SLC6A6-related Leber congenital amaurosis/early-onset retinal dystrophy (LCA/EORD)** and, in some patients, hypokinetic or dilated cardiomyopathy. The name should not be applied to acquired low-taurine states caused by diet, prematurity, parenteral nutrition, drugs, or unrelated systemic disease.

### Names and identifiers

- Preferred names: **taurine transporter deficiency**; **SLC6A6-related taurine transporter deficiency**.
- Phenotypic names: **SLC6A6-related early-onset retinal dystrophy**, **SLC6A6-related Leber congenital amaurosis**, and **SLC6A6 retinopathy with cardiomyopathy**.
- Gene: **SLC6A6**, approved name *solute carrier family 6 member 6*; protein TauT; Ensembl **ENSG00000131389**. (OpenTargets Search: taurine transporter deficiency-SLC6A6)
- Gene OMIM/MIM: **186854**, as stated in the index report. (ansar2020taurinetreatmentof pages 1-2)
- Disease OMIM, Orphanet, MONDO, MeSH, ICD-10, and ICD-11: a confidently disease-specific identifier was not established in the retrieved authoritative evidence. The condition may presently be represented under broader inherited retinal dystrophy or cardiomyopathy concepts. A dedicated MONDO assignment should not be inferred from similarly named taurine or amino-acid disorders.

The evidence is aggregated from published family studies, clinical examinations, molecular assays, and disease-level literature—not EHR-derived population data.

## 2. Etiology, risk, and protective factors

### Primary cause

The cause is **germline biallelic SLC6A6 dysfunction**. Reported disease alleles are severe loss-of-function or hypomorphic variants that reduce transporter activity, surface trafficking, or cycling. Unaffected heterozygous relatives retained sufficient transport and did not exhibit the retinal phenotype, supporting recessive inheritance and absence of clinically important haploinsufficiency in the observed families. (ullah2026earlyonsetretinopathyin pages 7-8, ullah2026earlyonsetretinopathyin pages 1-2)

### Genetic risk factors

Established risk factors are:

1. Two pathogenic SLC6A6 alleles in trans or homozygously;
2. parental consanguinity or shared ancestry, which increases homozygosity risk;
3. an affected sibling in an autosomal-recessive family.

The index Pakistani family and several subsequently reported families were consanguineous. No susceptibility loci, modifier genes, digenic interactions, founder allele, or germline mosaicism have been demonstrated. (ansar2020taurinetreatmentof pages 4-5, ullah2026earlyonsetretinopathyin pages 3-4)

### Environmental and protective factors

No environmental exposure causes the inherited disorder. Because taurine is obtained from endogenous synthesis and animal-derived foods, dietary supply could plausibly influence residual tissue availability, but no human gene–diet interaction has been quantified. Normal diet did not prevent disease in individuals with severe transporter dysfunction.

Oral taurine is the only demonstrated potentially protective intervention after diagnosis. Benefit appears greatest when residual transport remains and treatment begins before irreversible photoreceptor loss. This is a mechanistic and case-based inference, not a validated prevention guideline. The elder sibling who had already lost vision by age eight did not recover vision, whereas the younger sibling retained central photoreceptors and stabilized after treatment. (ansar2020taurinetreatmentof pages 4-5, ansar2020taurinetreatmentof pages 2-4)

Smoking, alcohol, exercise, toxins, infections, sex, and occupational exposures have no established disease-specific effect. There are no known genetically protective variants.

## 3. Phenotypes

### Ocular phenotype

The core phenotype is severe, bilateral, progressive retinal degeneration.

- **Onset:** birth to early childhood. Four individuals in one family had visual impairment and nystagmus from birth; another developed night blindness at one to two years. (ullah2026earlyonsetretinopathyin pages 3-4)
- **Symptoms/signs:** poor vision, nystagmus, night blindness, progressive daytime and color-vision loss, strabismus, and eventual blindness.
- **Electrophysiology:** severely reduced or extinguished scotopic and photopic ERGs; multifocal ERG may retain only minimal central responses early in disease. (ullah2026earlyonsetretinopathyin pages 3-4, ansar2020taurinetreatmentof pages 2-4)
- **Imaging:** attenuated retinal vessels, macular atrophy, pigmentary or salt-and-pepper degeneration, photoreceptor/outer nuclear layer loss, and a residual central island on OCT. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 4-5)
- **Severity/course:** variable but commonly severe and progressive. In the index family, the older male had only light perception at 15 years and had complete visual loss by age eight; the younger child retained central photoreceptors. A separate patient demonstrated progression of macular atrophy and clumped pigmentation between ages 11 and 18. (ansar2020taurinetreatmentof pages 4-5, ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 3-4)
- **Frequency:** retinal dystrophy was present in all seven affected individuals in the expanded cohort and both affected siblings in the index family, making it the most penetrant recognized manifestation. (ullah2026earlyonsetretinopathyin pages 1-2)

Suggested HPO terms: **Retinal degeneration**, **Leber congenital amaurosis**, **Visual impairment**, **Blindness**, **Nystagmus**, **Nyctalopia**, **Abnormal electroretinogram**, **Macular atrophy**, **Photoreceptor degeneration**, **Pigmentary retinal degeneration**, **Strabismus**, and **Color vision defect**.

### Cardiac phenotype

The index siblings had mild hypokinetic cardiomyopathy with systolic dysfunction, left-ventricular systolic dilation, and fractional shortening of 24–27%. Exercise testing was normal. After treatment, fractional shortening normalized to 32% in both. (ansar2020taurinetreatmentof pages 2-4)

Cardiac expression is variable. In the later cohort, cardiac structure and systolic function were generally preserved. Short PR intervals were observed in one family; one proband met ECG voltage criteria for left-ventricular hypertrophy with mild repolarization abnormalities, but echocardiography did not confirm hypertrophy. Other reported ejection fractions were 56%, 60%, and 65%. (ullah2026earlyonsetretinopathyin pages 3-4, ullah2026earlyonsetretinopathyin pages 4-5)

Suggested HPO terms: **Cardiomyopathy**, **Dilated cardiomyopathy**, **Left ventricular dilatation**, **Abnormal left ventricular systolic function**, **Short PR interval**, and **Abnormal ECG**.

### Other findings

Mild intellectual disability, motor-coordination dysfunction, facial dysmorphism, and oculomotor abnormalities occurred in isolated patients, but substantial autozygosity and possible additional recessive defects make attribution to SLC6A6 uncertain. One child had IQ 62. Brain MRI and hepatic ultrasound were normal in the index siblings. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 5-6, ullah2026earlyonsetretinopathyin pages 4-5)

No disease-specific validated quality-of-life instrument has been used. Severe childhood visual impairment would predict major effects on mobility, education, independence, and psychosocial well-being, while cardiomyopathy adds exercise and medical-monitoring burdens; these impacts have not been quantified with EQ-5D, SF-36, or PROMIS.

## 4. Genetic and molecular information

### Gene and protein

**SLC6A6** encodes a plasma-membrane, high-affinity, sodium- and chloride-dependent transporter belonging to the SLC6/GABA-transporter family. TauT is predicted to have 12 transmembrane helices. It concentrates taurine intracellularly against a steep gradient, especially in retina, myocardium, skeletal muscle, brain, kidney, and leukocytes. (surai2021taurineasa pages 3-5, yadav2025thetaurinetautaxis pages 5-7)

### Reported pathogenic variants

- **NM_003043.5:c.1196G>T, p.(Gly399Val):** homozygous hypomorphic missense allele; approximately 15% residual transport. Modeling predicts displacement of Tyr138, a ligand-recognition/transport residue. Reduced transport arose predominantly from impaired transporter cycling rather than reduced surface abundance. (ansar2020taurinetreatmentof pages 2-4, ansar2020taurinetreatmentof pages 1-2)
- **NM_003043.6:c.746C>T, p.(Thr249Ile):** homozygous missense allele in TM5; absent from gnomAD v4.1 and GME in the study; classified likely pathogenic. (ullah2026earlyonsetretinopathyin pages 5-6)
- **NM_003043.6:c.880G>A, p.(Ala294Thr):** homozygous pathogenic missense allele in TM6; gnomAD frequency **5.45 × 10⁻⁵**, with no homozygotes reported. It caused a 94% reduction in surface expression in the transfected system, 99% reduction in transport in patient fibroblasts, and 76% lower fibroblast surface expression, consistent with misfolding and trafficking failure. (ullah2026earlyonsetretinopathyin pages 5-6)
- **NM_003043.6:c.1210-2389_1348-331del, p.(Phe404_Glu449del):** homozygous 3,320-bp deletion affecting exon 11 and a transmembrane segment. (ullah2026earlyonsetretinopathyin pages 5-6, ullah2026earlyonsetretinopathyin pages 3-4)
- **NM_003043.6:c.338G>A, p.(Trp113Ter):** homozygous truncating nonsense allele. (ullah2026earlyonsetretinopathyin pages 3-4)

All reported disease variants are germline. No somatic mechanism, dominant-negative effect, gain of function, repeat expansion, or recurrent chromosomal abnormality is established. No validated modifier genes or disease-specific epigenetic signature is known.

## 5. Environmental information

No toxin, radiation exposure, infection, smoking behavior, or occupational factor is known to initiate this genetic disease. Chemically induced taurine depletion in animals—using the competitive transporter inhibitor guanidinoethane sulfonate or high β-alanine exposure—can reproduce retinal injury and illustrates biological vulnerability, but it is not evidence of a common human environmental cause. (ansar2020taurinetreatmentof pages 4-5)

A taurine-poor diet might worsen systemic deficiency where transport is residual, but this remains untested. Conversely, dietary taurine alone may be inadequate when TauT function is absent. Vaccination, antimicrobial prophylaxis, and pollution control are not disease-specific interventions.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**Biallelic SLC6A6 variant → reduced TauT abundance or transport cycling → impaired Na⁺/Cl⁻-coupled cellular taurine uptake → very low plasma/tissue taurine → failure of high-taurine tissues, particularly retina and heart → photoreceptor degeneration and variable cardiomyopathy.**

The human mechanistic link is strong: p.Gly399Val retained approximately 15% transport, while p.Ala294Thr and other severe missense alleles showed near-complete or complete transport loss. Plasma taurine in the index family was only 6–7 μmol/L. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 5-6, ullah2026earlyonsetretinopathyin pages 1-2)

### Downstream mechanisms

The following downstream processes are biologically plausible and well supported in models, but are not all directly measured in patient tissues:

1. **Mitochondrial dysfunction.** Taurine contributes to mitochondrial tRNA uridine modification and accurate translation of respiratory-chain proteins. Deficiency impairs complex I/NADH dehydrogenase function, ATP synthesis, and fatty-acid oxidation while increasing NADH, acetylcarnitine, and superoxide. (baliou2020significanceoftaurine pages 7-8, baliou2020significanceoftaurine pages 8-9)
2. **Oxidative stress.** High-taurine tissues lose antioxidant and membrane-stabilizing support. TauT-null hearts generate more mitochondrial ROS; retinal depletion causes oxidative injury, glial activation, synaptic loss, and photoreceptor damage. (surai2021taurineasa pages 3-5)
3. **Osmoregulation and cell-volume control.** Taurine acts as an organic osmolyte, with TauT regulation involving NFAT5/TonEBP and osmotic signaling. (baliou2020significanceoftaurine pages 7-8, baliou2020significanceoftaurine pages 8-9)
4. **Calcium handling and excitability.** Taurine modulates ion channels, calcium homeostasis, neuronal activity, and myocardial contractility; disruption may contribute to retinal signaling and cardiac dysfunction. (yadav2025thetaurinetautaxis pages 5-7)
5. **Proteostasis and cell death.** Deficiency increases unfolded-protein responses and protein aggregation and reduces anti-apoptotic protection. Photoreceptor apoptosis is prominent in knockout models. (baliou2020significanceoftaurine pages 6-7, baliou2020significanceoftaurine pages 7-8)

Suggested GO terms include **taurine transport**, **transmembrane transport**, **sodium ion transmembrane transport**, **chloride transmembrane transport**, **cellular osmoregulation**, **mitochondrial translation**, **oxidative phosphorylation**, **response to oxidative stress**, **regulation of calcium ion homeostasis**, **photoreceptor cell maintenance**, and **apoptotic process**. Suggested cellular component terms are **plasma membrane**, **integral component of plasma membrane**, **mitochondrion**, and **mitochondrial respiratory-chain complex I**.

No disease-specific human single-cell, spatial-transcriptomic, proteomic, lipidomic, epigenomic, CRISPR-screen, or multi-omic study was identified.

## 7. Anatomical structures affected

### Primary organs

- **Retina**: strongest and most consistent evidence. Suggested UBERON term: retina.
- **Heart/myocardium**: directly affected in some patients. Suggested UBERON terms: heart, myocardium, left ventricle.

### Tissues and cells

- Photoreceptors—both cone and rod systems—are strongly implicated by OCT and ERG.
- Retinal ganglion cells and retinal pigment epithelium are vulnerable in depletion models, but their contribution to the human phenotype is less directly established.
- Cardiomyocytes are implicated by systolic cardiomyopathy.

Suggested Cell Ontology labels: **photoreceptor cell**, **rod photoreceptor cell**, **cone photoreceptor cell**, **retinal ganglion cell**, **retinal pigment epithelial cell**, and **cardiac muscle cell/cardiomyocyte**.

Disease is bilateral in the eyes. Cardiac involvement is systemic rather than lateralized. Model organisms suggest possible skeletal-muscle, liver, kidney, brain, auditory, olfactory, reproductive, and immune involvement, but these are not yet established components of the human disorder. (baliou2020significanceoftaurine pages 6-7, baliou2020significanceoftaurine pages 7-8)

## 8. Temporal development

Onset is congenital or pediatric and usually insidious/progressive. LCA-like disease presents at birth or within the first six months, whereas EORD becomes evident after infancy but before age five. Visual deterioration can continue through childhood and adolescence, progressing from night blindness and nystagmus to macular atrophy and profound visual loss. (ullah2026earlyonsetretinopathyin pages 1-2)

Cardiomyopathy may be childhood-onset but could also be age dependent. Current numbers are insufficient to define stages or progression rates. The disease is lifelong; spontaneous remission has not been reported.

The likely therapeutic window is before irreversible photoreceptor loss and myocardial remodeling. Stabilization rather than regeneration is a realistic retinal goal. Treatment-induced cardiac recovery appears more feasible, as demonstrated by complete normalization in two children after 24 months. (ansar2020taurinetreatmentof pages 4-5)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. All affected individuals in the expanded cohort were homozygous, while available unaffected relatives were heterozygous carriers. Both sexes are affected. (ullah2026earlyonsetretinopathyin pages 1-2)

Prevalence, incidence, carrier frequency, penetrance, and sex ratio are unknown. The published patients originated from Pakistani, Italian, Egyptian/US, French, and Turkish-associated families, arguing against restriction to one population. Consanguinity was common but is not required. No founder effect has been demonstrated. (ullah2026earlyonsetretinopathyin pages 1-2, ullah2026earlyonsetretinopathyin pages 3-4, ullah2026earlyonsetretinopathyin pages 4-5)

Retinal penetrance appears high among known biallelic cases, but ascertainment through ophthalmic cohorts creates substantial bias. Cardiac expressivity is clearly variable. Genetic anticipation is not expected and has not been observed.

For two carrier parents, each pregnancy has the standard recessive probabilities: 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming both variants are fully pathogenic and no unusual reproductive mechanism.

## 10. Diagnostics

### Recommended clinical approach

1. **Recognize the phenotype:** congenital/early childhood bilateral retinal dystrophy, particularly with low taurine or cardiomyopathy.
2. **Ophthalmic assessment:** visual acuity, refraction, fundus examination, full-field ERG, OCT, fundus autofluorescence, and widefield imaging. Full-field stimulus testing may be useful where visual acuity is extremely poor. (ullah2026earlyonsetretinopathyin pages 4-5, ullah2026earlyonsetretinopathyin pages 1-2)
3. **Biochemistry:** fasting quantitative plasma amino acids with specific taurine measurement. Values of 6–7 μmol/L were seen in the index family; one later patient had 5 nmol/mL, rising to 29 nmol/mL on therapy against a stated age-adjusted range of 21–123 nmol/mL. (ansar2020taurinetreatmentof pages 1-2, ullah2026earlyonsetretinopathyin pages 4-5)
4. **Cardiac assessment:** ECG, echocardiography with EF and fractional shortening, and periodic surveillance even if baseline imaging is normal.
5. **Molecular confirmation:** inherited-retinal-disease panel including SLC6A6, WES, or WGS; confirm and phase variants by Sanger/family testing. WGS may be preferable when WES is negative because it can identify exon-level or intronic structural deletions.
6. **Functional confirmation where needed:** radiolabeled taurine uptake and surface-biotinylation/trafficking assays in patient fibroblasts or transfected cells. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 5-6)

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line unless the broader phenotype suggests another disorder. CMA could detect a large deletion but will miss most single-nucleotide alleles.

### Differential diagnosis

The principal differential is genetically heterogeneous LCA/EORD, including RPE65-, CEP290-, GUCY2D-, CRB1-, AIPL1-, and other IRD-related disease. Distinguishing clues for SLC6A6 deficiency are markedly reduced plasma taurine, cardiomyopathy or conduction findings, and biallelic SLC6A6 variants. Other considerations include nutritional/acquired taurine deficiency, mitochondrial disease, syndromic retinal dystrophies, and primary pediatric cardiomyopathy.

No consensus diagnostic criteria, newborn-screening program, or validated population cutoff for taurine transporter deficiency exists. A normal plasma taurine result should not automatically exclude a partial transporter defect, particularly after supplementation.

## 11. Outcome and prognosis

No survival curves, mortality rates, life-expectancy estimates, or formal disability statistics exist. Major morbidity is progressive visual disability. Untreated severe disease can lead to childhood blindness. Cardiac prognosis is uncertain but potentially modifiable.

Prognostic factors likely include:

- residual TauT activity;
- age at treatment;
- remaining central photoreceptor structure;
- baseline plasma taurine;
- presence and severity of cardiomyopathy;
- ability of supplementation to normalize circulating taurine.

These factors are biologically compelling but not validated in a prognostic model. The index family suggests that myocardium can recover and residual retina can stabilize, whereas established blindness is unlikely to reverse. No prognostic biomarker beyond plasma taurine, functional transport, and organ-specific testing has been validated. (ansar2020taurinetreatmentof pages 4-5, ansar2020taurinetreatmentof pages 2-4)

## 12. Treatment

### Oral taurine supplementation

Taurine—**2-aminoethanesulfonic acid**, suggested CHEBI **CHEBI:15891**—is the only reported disease-directed therapy.

**Index-family regimen:** an oral loading dose of 100 mg/kg, followed by **100 mg/kg/day in three divided doses of approximately 33 mg/kg every eight hours**. Blood taurine rose above 40 μmol/L. After 24 months, left-ventricular fractional shortening normalized from 24–27% to 32%; cardiomyopathy resolved in both siblings. The younger child's visual acuity reached 20/100 right eye and 20/160 left eye, with anatomical stability and preserved foveal photoreceptors. No adverse effects were reported. (ansar2020taurinetreatmentof pages 4-5, ansar2020taurinetreatmentof pages 2-4)

The authors’ abstract states: “Remarkably, after 24-months, the cardiomyopathy was corrected in both affected siblings, and in the 6-years-old, the retinal degeneration was arrested, and the vision was clinically improved.” (ansar2020taurinetreatmentof pages 1-2)

**Later case:** oral taurine began at 1 g/day and increased to 2 g/day. Plasma taurine rose from 5 to 12 and then 29 nmol/mL over 17 months, but ophthalmic examination and full-field stimulus testing remained essentially unchanged. This supports biochemical target engagement but not reversal of established retinal degeneration. (ullah2026earlyonsetretinopathyin pages 4-5)

Suggested NCIT intervention labels: **Dietary Supplementation**, **Oral Therapy**, **Supportive Care**, and **Investigational Agent**. Taurine treatment should presently be regarded as investigational and supervised by metabolic, ophthalmic, and cardiac specialists.

### Supportive management

- low-vision services, mobility training, educational accommodation, assistive technology, and occupational therapy;
- routine cardiology surveillance and guideline-based heart-failure therapy if needed;
- genetic counseling and cascade testing;
- monitoring plasma taurine, renal/liver chemistry, ECG/echo, visual function, and retinal structure during supplementation.

There is no established gene therapy, CRISPR therapy, ASO, siRNA, cell therapy, surgery, or immunotherapy. No disease-specific registered interventional trial was identified. Evidence from general heart-failure studies must not be treated as proof for SLC6A6 deficiency.

## 13. Prevention

Primary prevention is genetic rather than behavioral. Options for an identified family include carrier testing, cascade testing, reproductive counseling, prenatal diagnosis, and preimplantation genetic testing for the known familial variants.

Secondary prevention centers on early recognition: measure plasma taurine and test SLC6A6 in unexplained LCA/EORD, especially when cardiomyopathy is present. Early supplementation could prevent additional tissue injury, but this remains unproven outside case reports.

Tertiary prevention includes continued taurine supplementation where clinically chosen, cardiac surveillance, retinal monitoring, and low-vision rehabilitation. There is no relevant vaccine, antimicrobial prophylaxis, or population screening program.

## 14. Other species and natural disease

- **Domestic cat, *Felis catus* (NCBI Taxonomy 9685):** dietary taurine deficiency naturally causes retinal degeneration and dilated cardiomyopathy. Historical veterinary cardiomyopathy was reversible with taurine repletion, providing important comparative evidence. (ullah2026earlyonsetretinopathyin pages 9-9, ansar2020taurinetreatmentof pages 5-6)
- **Domestic dog, *Canis lupus familiaris* (NCBI Taxonomy 9615):** taurine-deficiency-associated dilated cardiomyopathy occurs in susceptible animals and can improve after diet change and supplementation. (ansar2020taurinetreatmentof pages 5-6, ansar2020taurinetreatmentof pages 4-5)
- No zoonotic transmission exists; the disorder is genetic/metabolic, not infectious.

These animal diseases phenocopy low-taurine physiology but are not necessarily caused by naturally occurring biallelic SLC6A6 variants. A breed-specific VBO annotation for SLC6A6 deficiency itself is therefore not justified from current evidence.

## 15. Model organisms

### Mouse

Global **Slc6a6/TauT knockout mice** are the principal genetic model. They exhibit 95–100% taurine loss in cardiac and skeletal muscle and 74–96% loss in other tissues. Phenotypes include early photoreceptor apoptosis and vision loss; cardiomyopathy with myofibrillar fragmentation, mitochondrial disruption, and swelling; skeletal-muscle necrosis and myofilament disorganization; auditory/olfactory and synaptic abnormalities; impaired reproduction; and later liver inflammation, fibrosis, and tumors. (baliou2020significanceoftaurine pages 6-7)

Cardiac mitochondrial findings include impaired complex I activity and fatty-acid oxidation. Aged knockout mice develop sarcopenia and up to a tenfold increase in p16INK4A. Exercise endurance is severely impaired, with more than an 80% reduction in treadmill running distance in reported models. (baliou2020significanceoftaurine pages 7-8, surai2021taurineasa pages 3-5)

**Strength:** excellent construct validity for systemic taurine-transport loss and good face validity for retinal and cardiac disease. **Limitations:** global null mice have broader and more severe multi-organ disease than currently documented in humans; human alleles include hypomorphs; species-specific taurine synthesis and diet complicate translation.

### Induced retinal-depletion models

Guanidinoethane sulfonate or β-alanine-mediated taurine depletion in rodents causes photoreceptor and retinal-ganglion-cell injury, oxidative stress, glial activation, synaptic loss, and increased susceptibility to light damage. These models are useful for testing supplementation timing and downstream neuroprotection but lack the exact human genotype. (ansar2020taurinetreatmentof pages 4-5)

### Cellular models

HEK-293/HEK-derived cells expressing mutant TauT and patient-derived fibroblasts are established functional systems. They quantify radiolabeled taurine uptake, kinetic parameters, membrane abundance, protein folding, and trafficking. Patient fibroblasts showed approximately 99% transport loss for p.Ala294Thr, making them a practical personalized model for variant classification and therapy screening. (ansar2020taurinetreatmentof pages 2-4, ullah2026earlyonsetretinopathyin pages 5-6)

No disease-specific iPSC-retinal organoid, engineered cardiac tissue, zebrafish knockout, Drosophila, or humanized knock-in model was identified in the retrieved literature.

## Recent developments and expert assessment

The principal recent advance is the expanded multicenter cohort published online on **December 4, 2025** in *JAMA Ophthalmology* (DOI: [10.1001/jamaophthalmol.2025.4875](https://doi.org/10.1001/jamaophthalmol.2025.4875)). It expanded the allelic spectrum to TM5/TM6 missense, nonsense, and exon-deletion variants; established a consistent LCA/EORD phenotype across four unrelated families; quantified lower taurine against carriers and controls; and showed complete transport loss for key missense alleles. The authors concluded that affected patients “may be candidates for investigational oral taurine supplementation.” (ullah2026earlyonsetretinopathyin pages 1-2)

The foundational therapeutic report was published online **December 31, 2019** and in *Human Molecular Genetics* volume 29 (2020), DOI: [10.1093/hmg/ddz303](https://doi.org/10.1093/hmg/ddz303). Its treatment response is biologically persuasive because biochemical correction, cardiac normalization, and retinal stabilization were concordant, but expert interpretation must remain cautious: only two siblings were treated, there was no untreated comparator, and retinal improvement was age- and stage-dependent. (ansar2020taurinetreatmentof pages 4-5, ansar2020taurinetreatmentof pages 1-2)

The most defensible current management principle is therefore **rapid molecular diagnosis plus early, monitored consideration of oral taurine**, accompanied by formal retinal and cardiac outcome measurement. Multicenter natural-history studies, standardized taurine pharmacokinetics, genotype-stratified dosing, and prospective controlled trials are the highest priorities.

## Major evidence gaps

1. No reliable prevalence, incidence, carrier-frequency, mortality, or life-expectancy estimate.
2. No formal OMIM disease number, Orphanet entry, MONDO identifier, ICD code, or MeSH heading was verified from the retrieved material.
3. No prospective natural-history cohort or randomized trial.
4. Uncertain penetrance and age dependence of cardiomyopathy.
5. No validated treatment threshold, target plasma level, duration, or long-term safety protocol.
6. No evidence that supplementation restores advanced retinal tissue.
7. No disease-specific newborn screening, clinical guideline, patient-reported outcome, multi-omic profile, or advanced therapeutic program.
8. Disease-specific 2023–2024 primary human literature was not identified; the decisive clinical expansion appeared online in late 2025.

References

1. (ansar2020taurinetreatmentof pages 1-2): Muhammad Ansar, Emmanuelle Ranza, Madhur Shetty, Sohail A Paracha, Maleeha Azam, Ilse Kern, Justyna Iwaszkiewicz, Omer Farooq, Constantin J Pournaras, Ariane Malcles, Mateusz Kecik, Carlo Rivolta, Waqar Muzaffar, Aziz Qurban, Liaqat Ali, Yacine Aggoun, Federico A Santoni, Periklis Makrythanasis, Jawad Ahmed, Raheel Qamar, Muhammad T Sarwar, L Keith Henry, and Stylianos E Antonarakis. Taurine treatment of retinal degeneration and cardiomyopathy in a consanguineous family with slc6a6 taurine transporter deficiency. Human molecular genetics, 29:618-623, Dec 2020. URL: https://doi.org/10.1093/hmg/ddz303, doi:10.1093/hmg/ddz303. This article has 75 citations and is from a domain leading peer-reviewed journal.

2. (ullah2026earlyonsetretinopathyin pages 1-2): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

3. (ansar2020taurinetreatmentof pages 2-4): Muhammad Ansar, Emmanuelle Ranza, Madhur Shetty, Sohail A Paracha, Maleeha Azam, Ilse Kern, Justyna Iwaszkiewicz, Omer Farooq, Constantin J Pournaras, Ariane Malcles, Mateusz Kecik, Carlo Rivolta, Waqar Muzaffar, Aziz Qurban, Liaqat Ali, Yacine Aggoun, Federico A Santoni, Periklis Makrythanasis, Jawad Ahmed, Raheel Qamar, Muhammad T Sarwar, L Keith Henry, and Stylianos E Antonarakis. Taurine treatment of retinal degeneration and cardiomyopathy in a consanguineous family with slc6a6 taurine transporter deficiency. Human molecular genetics, 29:618-623, Dec 2020. URL: https://doi.org/10.1093/hmg/ddz303, doi:10.1093/hmg/ddz303. This article has 75 citations and is from a domain leading peer-reviewed journal.

4. (ullah2026earlyonsetretinopathyin pages 3-4): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

5. (ansar2020taurinetreatmentof pages 4-5): Muhammad Ansar, Emmanuelle Ranza, Madhur Shetty, Sohail A Paracha, Maleeha Azam, Ilse Kern, Justyna Iwaszkiewicz, Omer Farooq, Constantin J Pournaras, Ariane Malcles, Mateusz Kecik, Carlo Rivolta, Waqar Muzaffar, Aziz Qurban, Liaqat Ali, Yacine Aggoun, Federico A Santoni, Periklis Makrythanasis, Jawad Ahmed, Raheel Qamar, Muhammad T Sarwar, L Keith Henry, and Stylianos E Antonarakis. Taurine treatment of retinal degeneration and cardiomyopathy in a consanguineous family with slc6a6 taurine transporter deficiency. Human molecular genetics, 29:618-623, Dec 2020. URL: https://doi.org/10.1093/hmg/ddz303, doi:10.1093/hmg/ddz303. This article has 75 citations and is from a domain leading peer-reviewed journal.

6. (ullah2026earlyonsetretinopathyin pages 7-8): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

7. (ullah2026earlyonsetretinopathyin pages 5-6): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

8. (ullah2026earlyonsetretinopathyin pages 4-5): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

9. (baliou2020significanceoftaurine pages 4-6): Stella Baliou, Anthony Kyriakopoulos, Maria Goulielmaki, Michalis Panayiotidis, Demetrios Spandidos, and Vassilios Zoumpourlis. Significance of taurine transporter (taut) in homeostasis and its layers of regulation. Molecular Medicine Reports, 22:2163-2173, Jul 2020. URL: https://doi.org/10.3892/mmr.2020.11321, doi:10.3892/mmr.2020.11321. This article has 111 citations and is from a peer-reviewed journal.

10. (baliou2020significanceoftaurine pages 8-9): Stella Baliou, Anthony Kyriakopoulos, Maria Goulielmaki, Michalis Panayiotidis, Demetrios Spandidos, and Vassilios Zoumpourlis. Significance of taurine transporter (taut) in homeostasis and its layers of regulation. Molecular Medicine Reports, 22:2163-2173, Jul 2020. URL: https://doi.org/10.3892/mmr.2020.11321, doi:10.3892/mmr.2020.11321. This article has 111 citations and is from a peer-reviewed journal.

11. (surai2021taurineasa pages 3-5): Peter F. Surai, Katie Earle-Payne, and Michael T. Kidd. Taurine as a natural antioxidant: from direct antioxidant effects to protective action in various toxicological models. Antioxidants, 10:1876, Nov 2021. URL: https://doi.org/10.3390/antiox10121876, doi:10.3390/antiox10121876. This article has 219 citations.

12. (baliou2020significanceoftaurine pages 6-7): Stella Baliou, Anthony Kyriakopoulos, Maria Goulielmaki, Michalis Panayiotidis, Demetrios Spandidos, and Vassilios Zoumpourlis. Significance of taurine transporter (taut) in homeostasis and its layers of regulation. Molecular Medicine Reports, 22:2163-2173, Jul 2020. URL: https://doi.org/10.3892/mmr.2020.11321, doi:10.3892/mmr.2020.11321. This article has 111 citations and is from a peer-reviewed journal.

13. (baliou2020significanceoftaurine pages 7-8): Stella Baliou, Anthony Kyriakopoulos, Maria Goulielmaki, Michalis Panayiotidis, Demetrios Spandidos, and Vassilios Zoumpourlis. Significance of taurine transporter (taut) in homeostasis and its layers of regulation. Molecular Medicine Reports, 22:2163-2173, Jul 2020. URL: https://doi.org/10.3892/mmr.2020.11321, doi:10.3892/mmr.2020.11321. This article has 111 citations and is from a peer-reviewed journal.

14. (ullah2026earlyonsetretinopathyin pages 9-9): Mukhtar Ullah, Atta Ur Rehman, Madhur Shetty, Michael D. Allen, Ehsan Ullah, Sabrina G. Signorini, Cyril Burin des Roziers, Rosalie M. Grijalva, Abdur Rashid, Asad Munir, Alessandra Pia Porretta, Enza Maria Valente, Aime R. Agather, Ioannis Dimopoulos, Robert B. Hufnagel, Edouard Malandain, Juliette Coursimault, Muhammad Ansar, Stylianos E. Antonarakis, Andrea Superti-Furga, Sanaullah Jan, Brian P. Brooks, Giacomo Calzetti, Bin Guan, Mathieu Quinodoz, L. Keith Henry, and Carlo Rivolta. Early-onset retinopathy in patients with variants in <i>slc6a6</i> leading to impaired taurine transport. JAMA Ophthalmology, 144(1):70, Jan 2026. URL: https://doi.org/10.1001/jamaophthalmol.2025.4875, doi:10.1001/jamaophthalmol.2025.4875. This article has 2 citations and is from a highest quality peer-reviewed journal.

15. (OpenTargets Search: taurine transporter deficiency-SLC6A6): Open Targets Query (taurine transporter deficiency-SLC6A6, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (yadav2025thetaurinetautaxis pages 5-7): Anshu Yadav, Bishal Patgiri, Jitendra Kumar, and Uddalak Das. The taurine-taut axis in hematologic malignancies: a review on redox homeostasis, mitochondrial trna stabilization, leukemic stem cell persistence, and therapeutic vulnerabilities. Unknown journal, Oct 2025. URL: https://doi.org/10.20944/preprints202510.1439.v1, doi:10.20944/preprints202510.1439.v1.

17. (ansar2020taurinetreatmentof pages 5-6): Muhammad Ansar, Emmanuelle Ranza, Madhur Shetty, Sohail A Paracha, Maleeha Azam, Ilse Kern, Justyna Iwaszkiewicz, Omer Farooq, Constantin J Pournaras, Ariane Malcles, Mateusz Kecik, Carlo Rivolta, Waqar Muzaffar, Aziz Qurban, Liaqat Ali, Yacine Aggoun, Federico A Santoni, Periklis Makrythanasis, Jawad Ahmed, Raheel Qamar, Muhammad T Sarwar, L Keith Henry, and Stylianos E Antonarakis. Taurine treatment of retinal degeneration and cardiomyopathy in a consanguineous family with slc6a6 taurine transporter deficiency. Human molecular genetics, 29:618-623, Dec 2020. URL: https://doi.org/10.1093/hmg/ddz303, doi:10.1093/hmg/ddz303. This article has 75 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Taurine_Transporter_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.