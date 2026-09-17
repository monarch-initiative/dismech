---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T11:35:31.250258'
end_time: '2026-08-27T11:42:59.340480'
duration_seconds: 448.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adult-Onset_Proximal_Spinal_Muscular_Atrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant** covering all of the
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
- **Disease Name:** Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant** covering all of the
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


# Adult-Onset Proximal Spinal Muscular Atrophy, Autosomal Dominant

## Executive summary and scope

Adult-onset proximal spinal muscular atrophy, autosomal dominant is an ultra-rare inherited lower-motor-neuron disease mapped to **MONDO:0008453**. In the literature it is usually treated as the **Finkel-type spinal muscular atrophy/amyotrophic lateral sclerosis type 8 (ALS8) spectrum** caused by heterozygous pathogenic variation in **VAPB**, particularly **p.Pro56Ser (P56S)**. The classic phenotype is adult-onset, slowly progressive proximal weakness and neurogenic muscle atrophy, but the same variant can produce slowly progressive ALS or, less commonly, rapidly progressive conventional ALS. Thus, Finkel SMA is best considered one end of a variable VAPB-associated motor-neuron-disease spectrum rather than a uniformly discrete syndrome. Open Targets identifies VAPB as the only target associated with the exact MONDO disease label and links the association to the original discovery paper, PMID **15372378**. [Open Targets](https://platform.opentargets.org/), accessed through the disease-target record (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant)

The evidence base remains small. Most human data derive from extended Brazilian kindreds rather than population cohorts, EHR studies, or randomized trials. Recent disease-specific research in 2023–2024 was sparse; a 2023 Colombian report expanded the geographic phenotype, while a 2024 review emphasized that molecularly distinct non-5q SMAs require next-generation sequencing and still lack the approved therapies available for SMN1-related SMA. Accordingly, many epidemiologic frequencies, penetrance estimates, quality-of-life scores, and treatment-response statistics remain unknown.

The following table summarizes the principal knowledge-base fields.

| domain | evidence-supported value | ontology/database annotation suggestions | evidence type/limitations |
|---|---|---|---|
| Disease entity | Adult-onset proximal spinal muscular atrophy, autosomal dominant; clinically overlaps the Finkel-type SMA / ALS8 motor-neuron-disease spectrum; MONDO:0008453 (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant, larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2) | MONDO:0008453; disease synonyms to capture: Finkel type SMA, late-onset SMA, ALS8-spectrum motor neuron disease | MONDO/Open Targets plus literature synthesis; legacy disease naming is heterogeneous and may overlap with ALS8 rather than a fully separate entity |
| Key identifiers | MONDO resolved as MONDO:0008453; Open Targets links the disease specifically to VAPB; OMIM/Orphanet/ICD/MeSH mappings not securely resolved from retrieved evidence and should be marked unresolved pending manual curation (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant) | MONDO:0008453; Open Targets disease-target association; OMIM/Orphanet/ICD/MeSH: unresolved | Identifier evidence strong for MONDO/VAPB only; do not invent external IDs |
| Causal gene | VAPB (VAMP associated protein B and C) is the sole disease-associated target recovered in Open Targets for this disease label (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant) | HGNC gene: VAPB; Ensembl target in Open Targets: ENSG00000124164 | Disease-target evidence is consistent, but not a substitute for full locus curation |
| Pathogenic variant | Recurrent causative variant is VAPB p.Pro56Ser (P56S), a missense change in the MSP domain; described as codon 56 proline-to-serine change in exon 2 on chr20q13.33 (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, murage2023characterisationofa pages 30-33, borgese2021thelinkbetween pages 7-9) | HGVS protein: p.Pro56Ser; variant class: missense SNV; germline | Retrieved evidence supports pathogenicity, but population allele frequency and ClinVar assertion details were not retrieved here |
| Inheritance | Autosomal dominant (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, murage2023characterisationofa pages 30-33, borgese2021thelinkbetween pages 1-2) | HPO inheritance term suggestion: Autosomal dominant inheritance [HP:0000006] | Strong human family evidence; penetrance not quantitatively established in retrieved sources |
| Founder / population | Initially described in large Brazilian families; evidence supports a Portuguese founder effect in many reported ALS8/Finkel-spectrum families, although review literature notes broader occurrence beyond Brazil (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 21-22, borgese2021thelinkbetween pages 1-2) | Population annotation suggestion: founder effect in Brazilian/Portuguese ancestry; geographic note rather than ontology ID | Founder interpretation is literature-based and may not apply to every reported family |
| Typical onset | Late adult/adult onset, average around 50 years (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, larroquette2015vapbamyotrophiclateralsclerosis pages 14-15) | HPO onset suggestion: Adult onset [HP:0003581] | Mean age estimate is derived from family-series literature; precise distribution not established in retrieved evidence |
| Core phenotype | Slowly progressive lower motor neuron syndrome with proximal weakness and muscle atrophy; clinical heterogeneity ranges from late-onset SMA/Finkel phenotype to slowly progressive ALS and, less commonly, typical severe rapidly progressive ALS (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, murage2023characterisationofa pages 30-33, borgese2021thelinkbetween pages 1-2) | HPO suggestions: Proximal muscle weakness [HP:0003701], Muscle atrophy [HP:0003202], Fasciculations [HP:0002380], Lower motor neuron dysfunction/degeneration [suggest disease annotation], Motor neuron atrophy [HP:0007373] | Phenotype is well supported but frequency of each manifestation was not quantified in retrieved sources |
| Electrophysiology / pathology | Needle EMG shows fasciculations in limbs and tongue, large motor unit potentials with reduced recruitment; sensory studies and motor nerve conduction may remain normal. Muscle pathology is neurogenic, with chronic denervation/reinnervation-type changes (murage2023characterisationofa pages 30-33, larroquette2015vapbamyotrophiclateralsclerosis pages 7-9) | Diagnostic annotation suggestions: EMG evidence of chronic neurogenic change; muscle biopsy showing neurogenic atrophy | Detailed clinical-diagnostic data came from limited family/series evidence and model-human comparison |
| Primary anatomy affected | Lower motor neurons, especially spinal cord ventral horn and brainstem motor neurons; downstream involvement of neuromuscular junction and skeletal muscle (larroquette2015vapbamyotrophiclateralsclerosis pages 10-12, larroquette2015vapbamyotrophiclateralsclerosis pages 9-10) | UBERON suggestions: spinal cord ventral horn, brainstem motor nucleus, skeletal muscle, neuromuscular junction; CL suggestions: motor neuron | Strong model support and consistent human clinical inference; human tissue data in retrieved set are limited |
| Subcellular localization / mechanism | VAPB is an ER membrane protein; p.Pro56Ser causes mutant protein misfolding/aggregation tendency, loss of normal ER localization/function, altered ER homeostasis, disrupted ER-mitochondria tethering/contact sites, abnormal Ca2+ handling, and NMJ denervation/reinnervation changes (borgese2021thelinkbetween pages 7-9, larroquette2015vapbamyotrophiclateralsclerosis pages 14-15, larroquette2015vapbamyotrophiclateralsclerosis pages 15-17, murage2023characterisationofa pages 30-33) | GO/CC suggestions: endoplasmic reticulum membrane, mitochondria-associated ER membrane/contact site, neuromuscular junction; GO/BP suggestions: ER stress response, unfolded protein response, calcium homeostasis, autophagy, intracellular protein transport | Mechanistic evidence is largely from cell and animal models; exact dominant-negative vs haploinsufficiency balance remains debated |
| Mechanistic interpretation | Current understanding favors major loss-of-function/haploinsufficiency of VAPB, with possible dominant-negative effects from sequestration of wild-type VAP proteins in some systems (borgese2021thelinkbetween pages 7-9, larroquette2015vapbamyotrophiclateralsclerosis pages 15-17, borgese2021thelinkbetween pages 1-2) | Mechanism tags: loss of function; possible dominant negative | Important unresolved issue: overexpression systems emphasize aggregation, whereas patient-derived cells may show little visible aggregation |
| Environmental / protective factors | No disease-specific environmental triggers, lifestyle risks, infectious causes, or protective factors were identified in retrieved evidence (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2) | Mark as no disease-specific evidence found | Evidence gap, not evidence of absence |
| Diagnostics | Best-supported approach: clinical recognition of adult-onset proximal/lower-motor-neuron syndrome plus electrophysiology and confirmatory molecular testing of VAPB, especially p.Pro56Ser; broad non-5q SMA / motor neuron disease gene panels or exome/genome sequencing are reasonable when phenotype is atypical (murage2023characterisationofa pages 30-33, larroquette2015vapbamyotrophiclateralsclerosis pages 3-4) | Suggested testing workflow: EMG/NCS, targeted VAPB testing, multigene motor neuron disease/non-5q SMA panel, WES/WGS if negative | No disease-specific formal guideline retrieved; recommendation is evidence-bounded inference from reported cases and non-5q SMA review context |
| Differential diagnosis | Differentiate from 5q-SMA (SMN1-related), other non-5q SMAs, hereditary motor neuropathies, and familial/sporadic ALS presentations (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2) | Differential-diagnosis tags: 5q-SMA, non-5q SMA, hereditary motor neuropathy, ALS | No standardized disease-specific differential algorithm retrieved |
| Epidemiology | Ultra-rare; no robust prevalence or incidence estimate was identified in retrieved sources. Evidence is based mainly on kindreds and founder-associated case series (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, murage2023characterisationofa pages 30-33) | Orphan disease flag; prevalence/incidence unresolved | Major evidence gap |
| Prognosis | Course is usually slowly progressive in classic Finkel/ALS8 families, but marked intrafamilial/interfamilial variability exists, including rapidly progressive ALS phenotypes (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2) | Prognosis tags: chronic progressive disease; variable expressivity | No robust survival curves or validated prognostic biomarkers retrieved |
| Treatment | No approved disease-specific therapy for VAPB-associated adult-onset proximal SMA/Finkel disease was identified; management is supportive and extrapolated from motor neuron disease care (rehabilitation, mobility, respiratory/nutritional surveillance as clinically indicated) (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2) | NCIT suggestions: Physical Therapy, Occupational Therapy, Supportive Care, Genetic Counseling | Evidence gap for disease-specific efficacy studies; no relevant registered interventional trial was retrieved |
| Prevention / counseling | Primary prevention is not established. Secondary/tertiary prevention centers on early genetic diagnosis, cascade testing in at-risk relatives, and reproductive/genetic counseling for autosomal-dominant transmission risk (borgese2021thelinkbetween pages 1-2) | NCIT suggestion: Genetic Counseling; HPO inheritance annotation | Counseling recommendation inferred from monogenic AD disease practice; no disease-specific counseling guideline retrieved |
| Model systems | Disease-relevant models include VAPB P56S knock-in mice, VAPB transgenic/knockout mice, Drosophila VAP P58S models, rat ALS8 models, NSC34 motor-neuron-like cells, and patient-derived iPSC motor neurons (larroquette2015vapbamyotrophiclateralsclerosis pages 10-12, larroquette2015vapbamyotrophiclateralsclerosis pages 14-15, borgese2021thelinkbetween pages 7-9, larroquette2015vapbamyotrophiclateralsclerosis pages 7-9) | Model resources: mouse KI/KO/transgenic, fly model, rat model, iPSC motor neuron, cell line model | Strong preclinical ecosystem, but not all models recapitulate the slow human lower-motor-neuron phenotype equally well |


*Table: This table condenses the highest-confidence, evidence-supported facts for VAPB-associated adult-onset proximal spinal muscular atrophy/Finkel-type disease in a knowledge-base-friendly format. It highlights established findings, annotation suggestions, and the main evidence gaps requiring manual curation.*

## 1. Disease information

**Definition.** This is a hereditary, adult-onset degeneration/dysfunction of lower motor neurons, producing chronic denervation, proximal weakness, fasciculations, and muscle atrophy. “Proximal SMA” here must not be conflated with common **5q SMA**, which is caused by biallelic **SMN1** defects. VAPB disease is non-5q and autosomal dominant. Human presentations range from pure lower-motor-neuron/Finkel-type SMA to upper-and-lower-motor-neuron ALS8 (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4).

**Identifiers and synonyms.** Securely resolved: **MONDO:0008453** and causal target **VAPB/ENSG00000124164**. Useful synonyms are *adult-onset proximal spinal muscular atrophy, autosomal dominant*; *autosomal dominant late-adult spinal muscular atrophy*; *Finkel-type SMA*; *late-onset SMA, Finkel type*; and, when upper-motor-neuron involvement occurs, *ALS8* or *VAPB-associated motor neuron disease*. Exact OMIM, Orphanet, MeSH, ICD-10, and ICD-11 mappings were not securely recoverable and should be manually curated rather than inferred. ICD coding will generally fall under motor-neuron disease or spinal muscular atrophy, but no unique disease-specific ICD code was demonstrated in the retrieved evidence (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant).

**Evidence provenance.** The foundational 1981 report described two extended families with approximately **80 affected members**. Subsequent molecular work studied a large Brazilian family and six additional kindreds. Another summarized pedigree contained **28 affected people across four generations**. These are aggregated pedigree/publication data, not individual-level EHR data (murage2023characterisationofa pages 30-33).

## 2. Etiology, risk, and protective factors

The primary cause is a **germline heterozygous pathogenic VAPB variant**, most characteristically p.Pro56Ser. Autosomal-dominant inheritance makes an affected heterozygote’s transmission probability approximately 50% per pregnancy, although clinical risk also depends on age-dependent penetrance and variable expression. Quantitative penetrance has not been established in the retrieved studies (murage2023characterisationofa pages 30-33, borgese2021thelinkbetween pages 7-9).

The principal established risk factors are carrying the familial variant, increasing age, and family history. No reproducible sex difference was observed in the family evidence. No environmental toxin, infection, occupational exposure, diet, smoking behavior, or lifestyle factor has been shown to cause or materially modify VAPB-Finkel disease. Likewise, no validated protective allele, modifier gene, diet, medication, or gene–environment interaction is known. These are evidence gaps, not proof that modifiers do not exist (murage2023characterisationofa pages 30-33, larroquette2015vapbamyotrophiclateralsclerosis pages 3-4).

A Portuguese founder has been proposed for many p.Pro56Ser kindreds, with dissemination into Brazil and reports in North America, Germany, China, and elsewhere. However, broader geographic occurrence means that founder status should not be assumed for every p.Pro56Ser carrier (borgese2021thelinkbetween pages 21-22, borgese2021thelinkbetween pages 1-2).

## 3. Phenotypes

The phenotype is variably expressed and frequencies are not robustly quantified.

* **Proximal limb weakness**—usually insidious, adult-onset, mild-to-moderate initially, and progressive. Lower limbs are commonly prominent. Suggested HPO: **Proximal muscle weakness, HP:0003701**; **Lower-limb muscle weakness, HP:0007340**.
* **Muscle atrophy**—a clinical sign secondary to chronic denervation. Suggested HPO: **Muscle atrophy, HP:0003202**.
* **Fasciculations**, including limb and tongue fasciculations. Suggested HPO: **Fasciculations, HP:0002380**.
* **Muscle cramps** and sometimes postural tremor are reported within the broader ALS8 phenotype. Suggested HPO: **Muscle cramps, HP:0003394**; **Postural tremor, HP:0002173**.
* **Lower-motor-neuron dysfunction**—large motor-unit potentials, reduced recruitment, denervation/reinnervation, weakness, and reduced muscle bulk. Sensory examination and sensory conduction are generally preserved, supporting a motor-neuron rather than generalized peripheral-neuropathy process (murage2023characterisationofa pages 30-33).
* **Upper-motor-neuron signs** are absent in the classic Finkel SMA phenotype but can occur in ALS8-spectrum relatives. This distinction explains why the same familial variant has been described as SMA, atypical ALS, or conventional ALS (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, larroquette2015vapbamyotrophiclateralsclerosis pages 9-10).
* **Bulbar/respiratory involvement** is not a defining early feature of classic slowly progressive Finkel SMA, although tongue fasciculations and ALS-spectrum progression make surveillance appropriate. Disease-specific frequencies are unavailable.
* **Cognition/behavior** are generally not central to the classic definition; available evidence is insufficient to assign reliable frequencies or HPO annotations.

The best-supported onset estimate is an average near **50 years**, followed by chronic slow progression in the classic phenotype. Severe rapidly progressive ALS is a documented but less typical expression (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, larroquette2015vapbamyotrophiclateralsclerosis pages 14-15). No disease-specific EQ-5D, SF-36, PROMIS, or utility estimates were found. Expected quality-of-life effects arise from impaired walking, transfers, upper-limb tasks, fatigue, cramps, and eventual dependence on mobility or respiratory support, but these have not been quantified specifically for Finkel disease.

## 4. Genetic and molecular information

**Gene.** **VAPB** encodes VAMP-associated protein B/C, an integral endoplasmic-reticulum adaptor and membrane-contact-site protein. Open Targets lists it as the sole target for MONDO:0008453 (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant).

**Variant.** The recurrent lesion is **VAPB p.Pro56Ser**, a germline missense variant in exon 2 at chromosome 20q13.33. It changes a highly conserved proline in the N-terminal major-sperm-protein domain, close to the FFAT-motif-binding surface. The original molecular-discovery paper is Nishimura et al., *American Journal of Human Genetics*, published November 2004, DOI [10.1086/425287](https://doi.org/10.1086/425287), PMID **15372378**. Its abstract states that the same mutation occurred in kindreds with “different clinical courses, such as ALS8, late-onset SMA, and typical severe ALS with rapid progression,” directly supporting variable expressivity (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant).

The variant is pathogenic based on segregation in multiple affected families, recurrence, functional disruption, and disease-model phenotypes. The retrieved material did not provide a definitive current ClinVar star status, HGNC ID, dbSNP accession, genomic HGVS expression, or gnomAD/TOPMed allele frequency; these should be retrieved directly against the reference transcript before production annotation. It is a constitutional germline variant, not a somatic cancer alteration.

**Functional consequence.** p.Pro56Ser makes VAPB unstable, aggregation-prone, and functionally deficient. Overexpression systems show recruitment of wild-type VAP proteins into mutant ER-derived aggregates, supporting a dominant-negative component. Physiologic knock-in and patient-cell evidence increasingly favors **loss of function/haploinsufficiency**, because visible aggregates are not consistently found in patient-derived fibroblasts or iPSC motor neurons (borgese2021thelinkbetween pages 7-9). These mechanisms need not be mutually exclusive.

No validated human modifier gene, protective allele, disease-specific methylation signature, chromosomal rearrangement, repeat expansion, or recurrent structural variant is established. Drosophila genetic screens identified modifiers in proteolysis, vesicle/endocytic trafficking, apoptosis, and lipid-droplet biology, but these are experimental candidates rather than clinically validated human modifiers.

## 5. Environmental information

This is a monogenic neurodegenerative disease. There is no established causal role for toxins, radiation, pollution, occupation, smoking, alcohol, diet, exercise pattern, or infectious agents. Exercise and rehabilitation can preserve function but should not be represented as preventing the genetic disease. There is no zoonotic or transmissible component. Environmental and lifestyle datasets specific to VAPB-Finkel SMA were not found.

## 6. Mechanism and pathophysiology

A defensible causal chain is:

1. **Upstream genetic trigger:** heterozygous VAPB p.Pro56Ser alters the conserved MSP domain.
2. **Protein-level defect:** mutant VAPB is unstable, poorly soluble, mislocalized, and deficient in normal ER-adaptor interactions; in some systems it sequesters wild-type VAPB and interacting proteins.
3. **Organelle dysfunction:** reduced functional VAPB perturbs ER-to-Golgi trafficking, phosphoinositide/lipid homeostasis, ER proteostasis, autophagy, and ER–mitochondria membrane contacts.
4. **Stress signaling:** impaired ER homeostasis activates parts of the unfolded-protein/integrated-stress response. In knock-in motor neurons, PDI, BiP/GRP78, and phosphorylated eIF2α increase before overt motor deficits, while ATF4, ATF6, and CHOP are not uniformly increased—evidence for partial or compensated stress rather than a single terminal-apoptosis program (larroquette2015vapbamyotrophiclateralsclerosis pages 14-15, larroquette2015vapbamyotrophiclateralsclerosis pages 15-17).
5. **Calcium/energy consequences:** impaired VAPB-dependent contact-site tethering disturbs mitochondrial calcium handling and bioenergetic coupling. This is mechanistically plausible and strongly supported experimentally, but direct confirmation in human Finkel tissue remains limited.
6. **Selective cellular injury:** long, metabolically demanding spinal and brainstem lower motor neurons become dysfunctional, followed by distal axonal and neuromuscular-junction denervation.
7. **Tissue/clinical outcome:** compensatory sprouting and reinnervation initially preserve motor units, but chronic denervation produces grouped muscle-fiber atrophy, proximal weakness, fasciculations, cramps, and progressive disability (larroquette2015vapbamyotrophiclateralsclerosis pages 9-10, larroquette2015vapbamyotrophiclateralsclerosis pages 7-9).

**Suggested GO biological-process annotations:** response to endoplasmic-reticulum stress; unfolded-protein response; autophagy; calcium-ion homeostasis; intracellular protein transport; ER-to-Golgi vesicle-mediated transport; regulation of lipid transport; axonal transport; neuromuscular-junction development; motor-neuron apoptotic process. **Suggested GO cellular components:** endoplasmic-reticulum membrane; ER–mitochondrion membrane contact site; Golgi apparatus; cytoplasmic protein-containing aggregate; axon; presynaptic active zone; neuromuscular junction. **Suggested CL terms:** motor neuron (**CL:0000100**), spinal motor neuron, skeletal muscle fiber, and Schwann cell—the latter two primarily as downstream/secondary participants.

No validated disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, or single-cell signature is ready for clinical use. Patient-derived iPSC motor neurons and CRISPR-corrected isogenic cells are important emerging systems, but findings remain research-stage (landry2026investigationsofals pages 146-153).

## 7. Anatomical structures affected

The primary body system is the somatic motor nervous system. Principal sites are spinal-cord anterior/ventral-horn motor neurons, brainstem motor nuclei, their peripheral motor axons, and neuromuscular junctions. Skeletal muscle is affected secondarily through denervation. Sensory neurons and sensory nerves are relatively spared in the classic syndrome (murage2023characterisationofa pages 30-33, larroquette2015vapbamyotrophiclateralsclerosis pages 10-12).

Suggested UBERON annotations are **spinal cord**, **ventral horn of spinal cord**, **brainstem**, **motor nucleus**, **peripheral nerve**, and **skeletal muscle organ**. At the subcellular level, the ER membrane and ER–mitochondria contact sites are central. Mouse data show VAPB enrichment in lower and brainstem motor neurons, with lower expression in cerebrum, cerebellum, hippocampus, and glia (larroquette2015vapbamyotrophiclateralsclerosis pages 10-12). Weakness can be bilateral but may be clinically asymmetric; no fixed lateralization is defining.

## 8. Temporal development

Onset is chronic and insidious in adulthood, averaging approximately 50 years in reported ALS8/Finkel families. The classic course is slowly progressive over many years, without spontaneous remission. Some carriers instead develop rapidly progressive ALS, demonstrating substantial intra- and interfamilial variability (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4).

A practical staging framework—not a validated formal scale—is: early focal/proximal weakness and cramps; intermediate multiregional weakness with mobility impairment; advanced loss of ambulation or upper-limb function; and, in ALS-like cases, bulbar or respiratory insufficiency. There are no established critical treatment windows, but mechanistic models show ER stress and autophagic responses before motor deficits, supporting the general principle that future molecular treatment may work best presymptomatically or early (larroquette2015vapbamyotrophiclateralsclerosis pages 14-15, larroquette2015vapbamyotrophiclateralsclerosis pages 15-17).

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with variable expressivity and likely age-dependent penetrance. Genetic anticipation, germline mosaicism, and a consanguinity effect have not been demonstrated. Consanguinity is not expected to be a major determinant of an AD disorder. Carrier frequency cannot be estimated reliably because population prevalence and variant frequency are unknown (murage2023characterisationofa pages 30-33, borgese2021thelinkbetween pages 7-9).

The disease is ultra-rare. No defensible prevalence per 100,000 or annual incidence was found. Published evidence is enriched for Brazilian families of Portuguese ancestry, so case counts cannot be used as population rates. One large pedigree summary reports 28 affected members over four generations; the original clinical description reported two families with about 80 affected members. No consistent male:female difference was observed (murage2023characterisationofa pages 30-33).

## 10. Diagnostics

Diagnosis should combine phenotype, electrodiagnosis, exclusion of mimics, and molecular confirmation.

1. **Clinical assessment:** document distribution and progression of weakness, atrophy, fasciculations, reflexes, upper-motor-neuron signs, bulbar function, cognition, family history, and a three-generation pedigree.
2. **EMG/NCS:** needle EMG may show limb and tongue fasciculations, chronic large-amplitude motor-unit potentials, and reduced recruitment. Sensory responses and motor conduction velocities can remain normal, supporting anterior-horn-cell disease rather than demyelinating neuropathy (murage2023characterisationofa pages 30-33).
3. **Laboratory testing:** CK may be normal or mildly elevated in neurogenic disorders but no disease-specific range was recovered. Routine blood tests mainly exclude acquired mimics.
4. **Muscle biopsy:** generally unnecessary after molecular confirmation. When performed, it shows chronic neurogenic atrophy, including groups of small fibers, internal nuclei, and denervation/reinnervation patterns (larroquette2015vapbamyotrophiclateralsclerosis pages 7-9).
5. **Imaging and functional assessment:** MRI is principally used to exclude compressive myelopathy or structural disease; pulmonary function, swallowing evaluation, and mobility scales should follow clinical involvement. No diagnostic imaging biomarker exists.
6. **Genetic testing:** in a family with a known variant, use targeted VAPB testing. In an unresolved adult lower-motor-neuron syndrome, use a comprehensive non-5q SMA/hereditary motor-neuropathy/ALS panel including **VAPB, SMN1, SETX, BICD2, DYNC1H1, TRPV4, VRK1, SIGMAR1, SOD1, FUS, TARDBP, C9orf72**, and other phenotype-appropriate genes. Copy-number analysis and **SMN1** dosage should be technically covered where relevant. WES or WGS is appropriate after negative panel testing or for atypical families. Repeat-expansion testing, particularly C9orf72, requires a validated dedicated method because standard exome sequencing may miss it.
7. **Tests generally not indicated as first-line:** karyotype, FISH, CMA, mitochondrial sequencing, liquid biopsy, proteomics, or epigenomics, unless another phenotype suggests them.

Important differentials include 5q-SMA type IV, Kennedy disease/SBMA, other dominant non-5q SMAs and hereditary motor neuropathies, multifocal motor neuropathy, adult-onset Pompe disease, inclusion-body myositis, cervical/lumbosacral myelopathy, and familial/sporadic ALS. Molecular confirmation is particularly important because VAPB-related SMA and ALS overlap clinically.

No universally accepted disease-specific clinical criteria exist. The molecular diagnosis should use ACMG/AMP variant interpretation and segregation analysis; genetic counseling should accompany testing.

## 11. Outcome and prognosis

Classic Finkel disease usually progresses slowly, but there are no reliable five- or ten-year survival estimates, disease-specific mortality rates, or life-expectancy tables. Prognosis cannot safely be inferred from conventional ALS because some VAPB families survive far longer, whereas other carriers have severe rapidly progressive ALS (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4, borgese2021thelinkbetween pages 1-2).

Morbidity includes progressive gait impairment, falls, difficulty climbing stairs or rising, upper-limb functional loss, cramps, fatigue, and eventual dependence on assistive devices. Respiratory and bulbar complications are likely to drive mortality in ALS-like disease but are not well quantified in pure Finkel SMA. Age at onset, baseline functional involvement, rate of spread, and respiratory status are clinically relevant, but no validated VAPB-specific prognostic biomarker exists.

## 12. Treatment and current applications

There is **no approved VAPB-specific disease-modifying treatment** and no disease-specific interventional trial was identified in the ClinicalTrials.gov search. Nusinersen, risdiplam, and onasemnogene abeparvovec increase or replace SMN protein and are approved for **SMN1-related 5q SMA**; their mechanism does not address VAPB disease and they should not be represented as treatments for Finkel SMA.

Current real-world management is multidisciplinary and supportive:

* individualized physiotherapy, stretching, low-to-moderate-intensity conditioning, fall prevention, orthoses, mobility aids, and occupational therapy;
* management of cramps, spasticity if present, pain, fatigue, sleep, and mood using standard symptomatic practice;
* serial respiratory assessment and non-invasive ventilation/cough assistance when indicated;
* swallowing and nutritional assessment if bulbar involvement develops;
* speech/communication support and assistive technology;
* orthopedic management of contracture or deformity when needed; surgery is not disease-modifying;
* genetic counseling and psychosocial support.

Suggested NCIt intervention concepts are **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Respiratory Therapy**, **Noninvasive Ventilation**, **Nutritional Support**, **Assistive Device**, and **Genetic Counseling**. Exact NCIt codes should be resolved against the current release.

Experimental strategies suggested by models include restoring wild-type VAPB function, suppressing mutant transcript/protein, correcting p.Pro56Ser, improving ER proteostasis, stabilizing ER–mitochondria contacts, and modulating autophagy or stress responses. These remain preclinical. Mouse overexpression of wild-type VAPB has slowed denervation in other ALS models, but that does not establish efficacy in human ALS8/Finkel disease (borgese2021thelinkbetween pages 21-22).

## 13. Prevention

No vaccine, medication, environmental modification, or lifestyle intervention prevents expression of the pathogenic allele.

* **Primary prevention:** reproductive counseling, prenatal diagnosis, or preimplantation genetic testing may reduce transmission when the familial variant is known; these are preference-sensitive options, not obligatory prevention.
* **Secondary prevention:** cascade testing of adult relatives after informed consent can identify presymptomatic carriers. Population or newborn screening is not currently justified because prevalence is extremely low and no proven presymptomatic disease-modifying therapy exists.
* **Tertiary prevention:** early rehabilitation, fall prevention, contracture management, vaccination against routine respiratory pathogens, respiratory surveillance, nutrition/swallow management, and timely assistive devices may prevent complications.

Predictive testing should address age-dependent penetrance, uncertain severity, psychological effects, privacy, and reproductive choices.

## 14. Other species and natural disease

No naturally occurring veterinary disease securely homologous to human VAPB p.Pro56Ser Finkel SMA was identified. Consequently, no breed-specific VBO annotation, animal prevalence, veterinary transmission concern, or zoonotic potential can be assigned. **VAPB is evolutionarily conserved**, enabling engineered mouse, rat, fly, nematode, yeast, and cellular models, but engineered phenocopy is not equivalent to natural animal disease.

## 15. Model organisms and experimental systems

**Mouse.** Physiologic **Vapb P56S knock-in mice** develop late, slowly progressive motor impairment, partial denervation, neurogenic muscle pathology, ER stress, ubiquitinated-protein accumulation, and autophagic responses. Weakness becomes apparent around 11 months, while molecular pathology precedes behavior. At the NMJ, mutant mice had **29.3 ± 1.9 presynaptic boutons versus 16.6 ± 1.0 in wild type**, enlarged endplates, fragmentation, and chronic denervation/reinnervation (larroquette2015vapbamyotrophiclateralsclerosis pages 14-15, larroquette2015vapbamyotrophiclateralsclerosis pages 9-10). Larroquette et al., published September 2015, DOI [10.1093/hmg/ddv360](https://doi.org/10.1093/hmg/ddv360), is the key model study. Limitations include mild phenotype, preserved motor-neuron counts, and incomplete reproduction of severe human ALS.

**Transgenic and knockout mice.** Overexpression models variably form aggregates and often show weak behavioral phenotypes; knockout animals show only mild impairment. These discrepancies are central to the unresolved balance between toxic aggregation, dominant-negative activity, and haploinsufficiency (borgese2021thelinkbetween pages 7-9, larroquette2015vapbamyotrophiclateralsclerosis pages 15-17).

**Drosophila.** The homologous VAP P58S model produces aggregation, synaptic defects, impaired BMP signaling, and motor decline. Genetic screens identify trafficking, proteolysis, apoptosis, and lipid-droplet pathways as modifiers. Advantages are rapid in-vivo screening; limitations are invertebrate neuroanatomy and overexpression artifacts.

**Rat.** A 2023 University of Edinburgh study characterized an ALS8 rat model and summarized the three human clinical expressions—late-onset SMA, slowly progressive atypical ALS, and rapidly progressive ALS. This is recent but thesis-level rather than mature clinical evidence. DOI [10.7488/era/2973](https://doi.org/10.7488/era/2973), January 2023 (murage2023characterisationofa pages 30-33).

**Cellular systems.** NSC34 motor-neuron-like cells expressing p.Pro56Ser show increased susceptibility to ER-stress-related death. Patient fibroblasts and iPSC-derived motor neurons are more physiologic and do not consistently show the conspicuous aggregates seen in overexpression models. CRISPR-corrected isogenic iPSC lines permit direct attribution of stress and ER–mitochondria phenotypes to p.Pro56Ser (landry2026investigationsofals pages 146-153, borgese2021thelinkbetween pages 7-9).

## Evidence assessment and research priorities

The most authoritative human evidence remains the 2004 mutation-discovery study and the original extended-family observations. The strongest mechanistic evidence comes from knock-in mice, cell systems, and patient-derived iPSC models—not human motor-neuron tissue. Recent work has refined VAPB’s roles in ER contact sites and stress signaling, but 2023–2024 produced little disease-specific clinical epidemiology or therapeutic evidence.

Priority gaps are: prospective genotype-defined natural-history cohorts; age-specific penetrance and survival; standardized phenotype frequencies; respiratory, cognitive, and quality-of-life outcomes; direct gnomAD/ClinVar transcript-level curation; patient-derived motor-neuron multi-omics; biomarkers of progression; and genotype-specific interventional trials. Until these exist, database entries should explicitly distinguish **established human genetic/clinical facts**, **model-supported mechanisms**, and **clinical-management extrapolations**.

References

1. (OpenTargets Search: Adult-onset proximal spinal muscular atrophy, autosomal dominant): Open Targets Query (Adult-onset proximal spinal muscular atrophy, autosomal dominant, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (larroquette2015vapbamyotrophiclateralsclerosis pages 3-4): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

3. (borgese2021thelinkbetween pages 1-2): Nica Borgese, Nicola Iacomino, Sara Francesca Colombo, and Francesca Navone. The link between vapb loss of function and amyotrophic lateral sclerosis. Cells, 10:1865, Jul 2021. URL: https://doi.org/10.3390/cells10081865, doi:10.3390/cells10081865. This article has 56 citations.

4. (murage2023characterisationofa pages 30-33): Brenda Murage. Characterisation of a model of als8 in the rat. Jan 2023. URL: https://doi.org/10.7488/era/2973, doi:10.7488/era/2973. This article has 0 citations.

5. (borgese2021thelinkbetween pages 7-9): Nica Borgese, Nicola Iacomino, Sara Francesca Colombo, and Francesca Navone. The link between vapb loss of function and amyotrophic lateral sclerosis. Cells, 10:1865, Jul 2021. URL: https://doi.org/10.3390/cells10081865, doi:10.3390/cells10081865. This article has 56 citations.

6. (borgese2021thelinkbetween pages 21-22): Nica Borgese, Nicola Iacomino, Sara Francesca Colombo, and Francesca Navone. The link between vapb loss of function and amyotrophic lateral sclerosis. Cells, 10:1865, Jul 2021. URL: https://doi.org/10.3390/cells10081865, doi:10.3390/cells10081865. This article has 56 citations.

7. (larroquette2015vapbamyotrophiclateralsclerosis pages 14-15): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

8. (larroquette2015vapbamyotrophiclateralsclerosis pages 7-9): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

9. (larroquette2015vapbamyotrophiclateralsclerosis pages 10-12): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

10. (larroquette2015vapbamyotrophiclateralsclerosis pages 9-10): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

11. (larroquette2015vapbamyotrophiclateralsclerosis pages 15-17): Frédérique Larroquette, Lesley Seto, Perrine L. Gaub, Brishna Kamal, Deeann Wallis, Roxanne Larivière, Joanne Vallée, Richard Robitaille, and Hiroshi Tsuda. Vapb/amyotrophic lateral sclerosis 8 knock-in mice display slowly progressive motor behavior defects accompanying er stress and autophagic response. Human molecular genetics, 24 22:6515-29, Sep 2015. URL: https://doi.org/10.1093/hmg/ddv360, doi:10.1093/hmg/ddv360. This article has 70 citations and is from a domain leading peer-reviewed journal.

12. (landry2026investigationsofals pages 146-153): C Landry. Investigations of als pathogenesis reveal convergent mitochondrial dysfunction and divergent integrated stress response outcomes. Unknown journal, 2026.

## Artifacts

- [Edison artifact artifact-00](Adult-Onset_Proximal_Spinal_Muscular_Atrophy_Autosomal_Dominant-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.