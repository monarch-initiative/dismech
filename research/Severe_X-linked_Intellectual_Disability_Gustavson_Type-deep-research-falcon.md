---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T20:38:01.981937'
end_time: '2026-09-04T20:47:49.762006'
duration_seconds: 587.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe X-linked Intellectual Disability Gustavson Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Severe_X-linked_Intellectual_Disability_Gustavson_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe X-linked Intellectual Disability Gustavson Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe X-linked Intellectual Disability Gustavson Type** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Severe X-linked Intellectual Disability Gustavson Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe X-linked Intellectual Disability Gustavson Type** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Severe X-linked Intellectual Disability, Gustavson Type

## Executive summary and evidence limits

Severe X-linked intellectual disability, Gustavson type—also called **Gustavson syndrome**—is an ultra-rare, syndromic neurodevelopmental disorder caused by the X-chromosomal **RBMX** in-frame deletion **NM_002139.4:c.484_486del, p.(Pro162del)**. The cardinal phenotype is profound intellectual and psychomotor disability with congenital or early-infantile microcephaly, epilepsy, severe visual and hearing impairment, spasticity, joint contractures, growth impairment, structural brain abnormalities, and death in early childhood, commonly during pulmonary infection. The causal variant was identified only recently: the definitive article appeared online on **5 June 2023** and in the March 2024 issue of *European Journal of Human Genetics* (DOI: https://doi.org/10.1038/s41431-023-01392-y; PMID **37277488**). The original clinical report was published in March 1993 (DOI: https://doi.org/10.1002/ajmg.1320450527; PMID **8456840**). (johansson2024gustavsonsyndromeis pages 1-2, OpenTargets Search: Severe X-linked intellectual disability Gustavson type, gustavson1993newxlinkedsyndrome pages 1-2)

The central limitation is that essentially all disease-specific human evidence comes from **one extended Swedish five-generation family**. The current pedigree contains 91 people, 36 of whom underwent sequencing, with approximately 10 affected relatives; the original report described seven affected children—six males and one female. Consequently, frequencies below describe that family rather than population-level estimates. There are no replicated unrelated families, prospective natural-history cohorts, validated clinical outcome measures, or disease-specific trials. (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 2-2, gustavson1993newxlinkedsyndrome pages 1-2)

| Domain | Best-supported finding | Evidence type/strength | Key identifier or quantitative datum |
|---|---|---|---|
| Disease identity | Severe X-linked intellectual disability, Gustavson type (Gustavson syndrome) | Curated disease-resource mapping; strong | **MONDO:0010661**; **OMIM 309555** (johansson2024gustavsonsyndromeis pages 5-7, OpenTargets Search: Severe X-linked intellectual disability Gustavson type) |
| Causal gene | **RBMX**, encoding RNA-binding motif protein X-linked/hnRNP G | Human segregation plus functional evidence; strong within one family | **ENSG00000147274**; sole Open Targets-associated gene (OpenTargets Search: Severe X-linked intellectual disability Gustavson type) |
| Causal variant | Hemizygous in-frame deletion removing conserved Pro162 | Human segregation and cellular/biochemical evidence; strong, but observed in one kindred | **NM_002139.4:c.484_486del; p.(Pro162del)** (johansson2024gustavsonsyndromeis pages 2-4) |
| Inheritance | X-linked inheritance; affected individuals inherited the allele through carrier mothers | Five-generation pedigree segregation; strong | Affected males are hemizygous; no male-to-male transmission (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 2-2) |
| Ascertainment | Evidence derives almost entirely from one extended Swedish pedigree, not a population cohort | Human familial evidence; major generalizability limitation | **91 pedigree members; 36 sequenced; 10 affected** in the extended study; original report described **7 affected people—6 males and 1 female** (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 2-2, gustavson1993newxlinkedsyndrome pages 1-2) |
| Female carriers | Most heterozygous females were clinically unaffected because the pathogenic X chromosome was preferentially silenced | Human X-inactivation and RNA evidence; strong for tested carriers | **11 asymptomatic carriers; 100:0 X-chromosome inactivation**; RNA expressed the wild-type allele (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-2) |
| Cardinal phenotype | Profound intellectual and psychomotor disability with microcephaly, growth impairment, epilepsy, optic atrophy/severe visual impairment, severe hearing impairment, spasticity/hypertonicity, and restricted large-joint mobility | Original human case series; strong for the family, but not independently replicated | All original seven were reported with the core severe neurologic-sensory phenotype (gustavson1993newxlinkedsyndrome pages 1-2, gustavson1993newxlinkedsyndrome pages 4-5) |
| Neuroanatomy | Structural abnormalities can include lissencephaly/thick cortex, vermian hypoplasia, posterior corpus-callosum thinning, Dandy–Walker malformation, cerebral atrophy, ventriculomegaly, and subependymal gliosis | Imaging/autopsy observations in individual patients; moderate and variable | Not established as universal because imaging and pathology data are sparse (johansson2024gustavsonsyndromeis pages 2-4, gustavson1993newxlinkedsyndrome pages 1-2) |
| Course and mortality | Congenital or early-infantile manifestations follow a severe lifelong course with death in infancy or early childhood | Original human natural-history evidence; strong within the family | Death generally **before age 4**; documented deaths at **6 months, 1 year, and 2 years 1 month**, often from pneumonia or pulmonary infection (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2) |
| Cellular expression profile | Pro162del altered neuronal-cell gene expression without a significant change in hnRNP G abundance or gross nuclear localization | Disease-variant SH-SY5Y experiment; moderate | **7 significant DEGs**: ZNF805, PCDHA10, and LYSMD3 upregulated; COL2A1, EVPL, TTN, and AC010207.1 downregulated; expression comparison **p=0.6641** (johansson2024gustavsonsyndromeis pages 5-7) |
| Transcriptional mechanism | Differentially expressed genes were enriched for transcription-factor and RNA-polymerase-II-related functions | Disease-variant transcriptomics; suggestive, not definitive | Supports disturbed RNA polymerase II transcription as a downstream mechanism (johansson2024gustavsonsyndromeis pages 7-8, johansson2024gustavsonsyndromeis pages 5-7) |
| SH3-domain interaction | Loss of Pro162 may weaken binding of a proposed polyproline-II motif to SH3 domains | Fluorescence-polarization and computational evidence; **uncertain and context-dependent** | Short peptide–BIN1-SH3 affinity: wild type **KD 150 μM** versus mutant **400 μM**; a longer peptide showed no clear mutant deficit and had **KD ≈30 μM** (johansson2024gustavsonsyndromeis pages 5-7) |
| Splicing mechanism | Aberrant RBMX transcript splicing was not detected for Pro162del | Patient RNA plus HeLa/SH-SY5Y minigene assays; evidence against this specific mechanism | No abnormal splicing in tested systems; other RBMX-dependent RNA-processing effects remain possible (johansson2024gustavsonsyndromeis pages 5-7) |
| Mechanistic interpretation | Altered SH3 interactions and RNA-polymerase-II transcription may impair neurodevelopment; direct links to individual clinical manifestations remain unproven | Integrated inference from segregation, transcriptomics, and biochemical assays | **Inferred**, not demonstrated in patient neural tissue or a Pro162del animal model (johansson2024gustavsonsyndromeis pages 7-8, johansson2024gustavsonsyndromeis pages 1-2) |
| Clinical trials | No Gustavson-syndrome-specific interventional trial was identified | Registry-search negative finding; absence of evidence | **0 disease-specific trials found** |
| Treatment | No disease-modifying, gene, RNA, or targeted therapy is established; care is supportive and phenotype-directed | Expert-practice extrapolation; **not tested specifically in Gustavson syndrome** | Seizure and respiratory care, nutritional and sensory support, spasticity/contracture management, and physical, occupational, and communication therapies |


*Table: Compact summary of the strongest clinical, genetic, and functional evidence for severe X-linked intellectual disability, Gustavson type. Uncertain mechanisms and evidence limited to the single known Swedish pedigree are explicitly marked.*

## 1. Disease information

### Definition

Gustavson syndrome is a **Mendelian X-linked syndromic intellectual-developmental disorder**. It is distinguished from Shashi syndrome, another RBMX-associated disorder, by its particular protein-domain lesion and much more severe neurologic, sensory, and survival phenotype. The 2024 authors reported only minor phenotypic overlap between the two syndromes and concluded that disruption of different hnRNP G domains likely produces different disease mechanisms and severities. (johansson2024gustavsonsyndromeis pages 7-8, tilliole2024hnrnpsrolesin pages 13-14)

### Identifiers and terminology

- **MONDO:** MONDO:0010661.
- **OMIM:** 309555.
- **Causal gene:** RBMX, Ensembl **ENSG00000147274**; protein name RNA-binding motif protein, X-linked/heterogeneous nuclear ribonucleoprotein G (**hnRNP G**).
- **Common names:** severe X-linked intellectual disability, Gustavson type; Gustavson syndrome; Gustavson-type X-linked syndromic intellectual developmental disorder; historically, “X-linked mental retardation syndrome with severe visual and hearing defects, epilepsy, spasticity, restricted joint mobility, and early death.”
- **Orphanet:** the Open Targets record contains an Orphanet genetic-association evidence item, but a numeric ORPHA identifier was not recoverable from the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or heading was identified. In practice, broader codes for intellectual developmental disorder, epilepsy, microcephaly, sensory impairment, and genetic syndromes would be used; these are not equivalent to a disease-specific identifier. (OpenTargets Search: Severe X-linked intellectual disability Gustavson type, johansson2024gustavsonsyndromeis pages 5-7)

The evidence is **aggregated family-level research and curated disease-resource evidence**, not an EHR-derived patient cohort. Individual case data were published for several children, but they all belong to the same pedigree. (johansson2024gustavsonsyndromeis pages 2-4, gustavson1993newxlinkedsyndrome pages 1-2)

## 2. Etiology

### Causal factor and genetic risk

The established cause is germline hemizygosity for **RBMX c.484_486del**, an in-frame three-nucleotide deletion removing Pro162 from a conserved tri-proline region. Genome and linked-read sequencing detected the allele after exome sequencing had difficulty resolving this GC-rich locus and its highly similar retrocopies. All tested affected relatives carried the variant; transmission occurred through heterozygous mothers. Open Targets lists RBMX as the sole associated target for MONDO:0010661, supported by Orphanet, EVA, UniProt, ClinVar-linked records, and PMIDs 37277488 and 8456840. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-4, OpenTargets Search: Severe X-linked intellectual disability Gustavson type)

The variant should be regarded as **pathogenic** on the combined evidence of phenotype-specific segregation, X-linked inheritance, evolutionary conservation, protective skewed X-inactivation in carriers, computational predictions, neuronal-cell transcriptional effects, and altered peptide–SH3 binding. Nevertheless, it is a private/founder-family allele rather than a recurrent variant demonstrated in unrelated cases. No population allele frequency was reported in the retrieved evidence; its absence or extreme rarity in reference populations is expected but should be verified directly in the current gnomAD release before database deposition. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-4)

### Female carriers and modifiers

Eleven clinically unaffected heterozygous females had **complete 100:0 skewing of X-chromosome inactivation**, preferentially silencing the pathogenic chromosome; cDNA analysis detected expression only from the wild-type allele. This is strong evidence that X-inactivation acts as a protective cellular modifier. One affected female was reported in 1993 and was X-chromatin positive, but the molecular basis of her expression—unfavorable tissue-specific X-inactivation, another chromosomal event, or a different mechanism—was not resolved. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-2, gustavson1993newxlinkedsyndrome pages 1-2)

RBMX retrocopies, particularly brain-expressed **RBMXL1** and RBMXL9, have been proposed as modifiers that might compensate for RBMX dysfunction. This remains a hypothesis for Gustavson syndrome, not demonstrated human modifier genetics. A 2024 review explicitly described retrocopy compensation as unproven. (tilliole2024hnrnpsrolesin pages 13-14)

### Environmental, lifestyle, infectious, and protective factors

No environmental exposure, lifestyle factor, toxin, diet, or infectious agent causes the disorder. Pulmonary infections are important **downstream complications and proximate causes of death**, not initiating causes. No environmental protective factor or disease-specific gene–environment interaction is established. Ordinary infection prevention, nutrition, aspiration management, and vaccination may reduce complications but cannot prevent the genetic neurodevelopmental lesion. (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2)

## 3. Phenotypes

The original seven children reportedly shared the core severe phenotype, but exact denominators for every feature are not consistently recoverable. Suggested HPO mappings should therefore be entered as family-level observations, with “very frequent” used only when supported by the original aggregate description.

- **Profound intellectual disability/developmental impairment:** congenital-to-infancy recognition; severe and lifelong, with major dependence in all daily activities. Suggested HPO: **Profound global developmental delay**, **Severe intellectual disability**, **Delayed psychomotor development**.
- **Microcephaly and impaired postnatal head growth:** congenital or rapidly evident in infancy. One infant had OFC 30 cm at birth (−2.5 SD) and 34 cm by 3.5 months (−6 SD). Suggested HPO: **Microcephaly (HP:0000252)** and **Progressive microcephaly** where documented.
- **Growth retardation/short stature:** congenital or childhood, severe in some patients. One birth length was 43 cm (−4 SD). Suggested HPO: **Intrauterine growth retardation**, **Short stature (HP:0004322)**, **Failure to thrive**.
- **Epilepsy:** neonatal or early-infantile onset; seizures began neonatally, at three weeks, or at one month in detailed cases and included myoclonic seizures. Suggested HPO: **Seizure (HP:0001250)**, **Neonatal seizure**, **Myoclonic seizure**.
- **Visual impairment:** optic atrophy with severe visual impairment or probable blindness, beginning in infancy. Suggested HPO: **Optic atrophy (HP:0000648)**, **Blindness (HP:0000618)**, **Severe visual impairment**.
- **Hearing impairment:** severe, often probable total deafness, beginning in infancy. Suggested HPO: **Sensorineural hearing impairment (HP:0000407)** or **Deafness**; the hearing-loss type was not consistently documented.
- **Spasticity/hypertonia:** early and severe, affecting mobility and contributing to contractures. Suggested HPO: **Spasticity (HP:0001257)** and **Hypertonia (HP:0001276)**.
- **Restricted large-joint mobility/contractures:** elbows, hips, knees, and feet could be affected; calcaneovalgus and equinovarus deformities were reported. Suggested HPO: **Joint contracture (HP:0001371)**, **Talipes equinovarus**, **Calcaneovalgus deformity**.
- **Brain malformations:** variable findings included lissencephaly with a very thick, dorsally predominant cortex; vermian hypoplasia; posterior corpus-callosum thinning; Dandy–Walker malformation; cerebral atrophy; ventriculomegaly; and subependymal gliotic nodules. Suggested HPO: **Lissencephaly (HP:0001339)**, **Cerebellar vermis hypoplasia**, **Thin corpus callosum**, **Dandy-Walker malformation (HP:0001305)**, **Cerebral atrophy**, and **Ventriculomegaly**. These are individual observations, not universal criteria. (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2, gustavson1993newxlinkedsyndrome pages 4-5)

Additional reported findings include dysplastic ears, mild micrognathia, high palate, hemangiomas, short stature, overweight in a later-surviving patient, congenital heart defects in the extended characterization, ureteral reflux, and neurogenic bladder. Hypogonadism and ophthalmoplegia were absent in the original syndrome comparison. (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2, gustavson1993newxlinkedsyndrome pages 4-5)

Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been reported. The clinical picture implies profound effects on mobility, communication, sensory access, feeding and self-care, with lifelong total-care needs during survival. That functional interpretation is clinically reasonable but was not measured with standardized patient-reported instruments.

## 4. Genetic and molecular information

**RBMX** is located at Xq26 and encodes hnRNP G, a predominantly nuclear RNA-binding protein. Relevant domains include an N-terminal RNA-recognition motif, an RGG/RG RNA-binding region, nascent-transcript targeting elements, and protein-interaction regions. Pro162 lies in a conserved polyproline region proposed to adopt a polyproline-II conformation and bind SH3 domains. (johansson2024gustavsonsyndromeis pages 1-2, johansson2024gustavsonsyndromeis pages 2-4)

The Gustavson allele is:

- Gene/transcript: **RBMX, NM_002139.4**.
- Variant: **c.484_486del; p.(Pro162del)**.
- Class: germline, X-chromosomal, in-frame deletion; hemizygous in affected males and heterozygous in carrier females.
- Functional direction: likely altered or partial loss of hnRNP G function, potentially with interaction-specific effects; a simple null mechanism has not been proven.
- Somatic origin: not supported.
- Structural abnormality: no large causal deletion, translocation, inversion, or aneuploidy was established; the causal lesion is a three-base deletion.
- Population frequency: not given in the retrieved primary study; no carrier-frequency estimate exists.
- Epigenetics: protective skewed X-inactivation is established in blood-derived carrier assays; no disease-specific DNA-methylation episignature or chromatin biomarker is known. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-4)

No validated second-site modifier allele has been identified. RBMXL1/RBMXL9 compensation is mechanistically plausible but unconfirmed for this pedigree. (tilliole2024hnrnpsrolesin pages 13-14)

## 5. Environmental information

The disorder is not attributed to toxins, radiation, pollution, occupation, smoking, alcohol, diet, or infection. Respiratory infections interact with severe neurologic disability, impaired mobility, and possibly swallowing/airway clearance to increase mortality risk; aspiration was not directly demonstrated in the retrieved reports. No zoonotic or transmissible component exists. (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. Germline **RBMX c.484_486del** **leads to** deletion of conserved Pro162 in hnRNP G.
2. Pro162 deletion **is inferred to alter** the conformation or partner specificity of a polyproline-II/SH3-interaction region; short-peptide testing **resulted in** weaker BIN1-SH3 affinity, although longer-peptide results were not concordant.
3. Altered hnRNP G interactions **lead to** changes in neuronal-cell gene regulation; SH-SY5Y cells expressing the variant **showed** seven significant differentially expressed genes and enrichment of RNA-polymerase-II transcription-related factors.
4. Dysregulated transcription/RNA processing during development **is inferred to impair** neural progenitor differentiation, cortical organization, and brain growth; this inference is supported by RBMX loss-of-function models but has not been demonstrated in Pro162del patient brain tissue.
5. Abnormal neurodevelopment **results in** microcephaly, cortical/cerebellar malformations, profound developmental disability, epilepsy, visual and hearing impairment, and upper-motor-neuron dysfunction.
6. Neurologic impairment and spasticity **lead to** severe immobility and joint contractures.
7. Severe multisystem disability **is inferred to increase** vulnerability to pulmonary infection and impaired airway clearance, which **resulted in** early childhood deaths in documented patients.
8. **Protective branch:** in heterozygous females, preferential inactivation of the mutant X **leads to** wild-type-only RBMX expression and usually an asymptomatic carrier state. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2, johansson2024gustavsonsyndromeis pages 7-8)

### Direct disease-variant evidence

No abnormal RBMX transcript splicing was detected in patient material, SH-SY5Y cells, or HeLa minigene experiments. Mutant and wild-type proteins remained predominantly nuclear, with no significant expression-intensity difference (**p=0.6641**). Thus, gross protein depletion, mislocalization, and aberrant splicing of the RBMX transcript itself are not demonstrated mechanisms. (johansson2024gustavsonsyndromeis pages 5-7)

RNA profiling found seven significant genes: **ZNF805, PCDHA10, and LYSMD3** were upregulated, whereas **COL2A1, EVPL, TTN, and AC010207.1** were downregulated. The top 100 expression changes were enriched for transcription factors and RNA-polymerase-II-associated processes. These results support transcriptional dysregulation, but they derive from a neuroblastoma-derived cell line rather than patient cortical neurons. (johansson2024gustavsonsyndromeis pages 7-8, johansson2024gustavsonsyndromeis pages 5-7)

Fluorescence-polarization assays showed that a short mutant peptide bound BIN1-SH3 about threefold more weakly than wild type (**KD approximately 400 μM versus 150 μM**). A longer peptide bound with approximately **30 μM** affinity without a clear mutant deficit. Natural cellular partners remain unknown. Accordingly, disturbed SH3 binding is a credible but **context-dependent hypothesis**, not a complete demonstrated pathway. (johansson2024gustavsonsyndromeis pages 5-7)

### Contextual RBMX biology

RBMX regulates pre-mRNA splice-site selection, RNA metabolism, sister-chromatid cohesion, centromere/kinetochore function, and DNA-damage responses. Zebrafish depletion establishes an essential role in brain development, while Xenopus experiments implicate Rbmx in neural and muscle development. These models support biological plausibility but do not reproduce the human Pro162 deletion. Shashi syndrome, caused by disruption of another hnRNP G domain, produces aberrant p53 activation and neuronal-differentiation defects; this should not be automatically assigned to Gustavson syndrome. (johansson2024gustavsonsyndromeis pages 7-8, tilliole2025rbmxfunctionalretrocopy pages 38-42)

Suggested annotations include **GO:0008380 RNA splicing**, **GO:0006357 regulation of transcription by RNA polymerase II**, **GO:0007062 sister chromatid cohesion**, **GO:0006281 DNA repair**, **GO:0007399 nervous system development**, and **GO:0030154 cell differentiation**. Candidate cell types are **neural stem cell/radial glial cell**, **neural progenitor cell**, **neuron**, **cortical neuron**, **Purkinje cell**, and **sensory neuron**; direct cell-type localization in Gustavson patient tissue is unavailable. Relevant cellular compartments are **nucleus**, **nucleoplasm**, **spliceosomal complex**, and chromatin/centromeric regions.

No Gustavson-specific metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, patient-iPSC, organoid, or CRISPR-screen dataset was identified.

## 7. Anatomical structures affected

The primary organ is the **brain/central nervous system**, with cerebral cortex, cerebellar vermis, corpus callosum, ventricular system, and possibly subependymal regions affected. Suggested UBERON mappings include **brain (UBERON:0000955)**, **cerebral cortex (UBERON:0000956)**, **cerebellum (UBERON:0002037)**, **cerebellar vermis**, and **corpus callosum (UBERON:0002336)**. (johansson2024gustavsonsyndromeis pages 2-4, gustavson1993newxlinkedsyndrome pages 1-2)

Secondary systems include the optic nerve/visual system, auditory system, skeletal muscle and large joints, respiratory system during fatal infection, urinary tract in at least one infant, and heart in some extended-family descriptions. Suggested terms include **optic nerve (UBERON:0000964)**, **inner ear (UBERON:0001846)**, **skeletal muscle tissue (UBERON:0001134)**, **joint**, **lung (UBERON:0002048)**, and **urinary bladder (UBERON:0001255)**. There is no consistent lateralization; sensory and motor findings appear bilateral/generalized. (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2)

## 8. Temporal development

Onset is congenital or neonatal/early infantile. Growth restriction and microcephaly may be present at birth; seizures can begin neonatally or during the first month; severe sensory and developmental abnormalities become evident in infancy. The course is chronic and severe rather than episodic or relapsing. Neurologic recovery or remission has not been reported. (gustavson1993newxlinkedsyndrome pages 1-2)

The critical biological period is inferred to be embryonic and early postnatal brain development, consistent with structural malformations and vertebrate Rbmx-depletion experiments. Clinically, infancy is the highest-risk period for seizures, feeding/respiratory complications, contracture development, and death. No formal disease staging system or measured progression rate exists. (johansson2024gustavsonsyndromeis pages 7-8, tilliole2025rbmxfunctionalretrocopy pages 38-42)

## 9. Inheritance and population

Inheritance is **X-linked recessive/sex-linked**, with severe expression in hemizygous males and protection of most heterozygous females through skewed X-inactivation. A carrier woman's theoretical conception risks are 50% transmission of the allele to each child; a son inheriting it is expected to be at high risk of severe disease, whereas a daughter inheriting it may be asymptomatic but cannot be assumed unaffected because X-inactivation is variable and one affected female was reported. These are Mendelian counseling probabilities, not empirically measured penetrance estimates. (johansson2024gustavsonsyndromeis pages 5-7, gustavson1993newxlinkedsyndrome pages 1-2)

Penetrance in hemizygous males appears high within the family, but confidence is limited by ascertainment. Female penetrance is incomplete and X-inactivation dependent. There is no evidence of anticipation. Germline mosaicism has not been reported but cannot be excluded in apparently de novo cases. The allele may represent a Swedish family-specific founder/private variant; no independent population distribution, prevalence, incidence, carrier frequency, consanguinity effect, or geographic gradient is known. The only defensible epidemiologic characterization is **ultra-rare, with one molecularly confirmed extended kindred**. (johansson2024gustavsonsyndromeis pages 2-4, johansson2024gustavsonsyndromeis pages 2-2)

## 10. Diagnostics

### Clinical recognition

The syndrome should be considered in a child—especially a boy—with profound global developmental delay, congenital/postnatal microcephaly, very early epilepsy, optic atrophy or blindness, severe hearing impairment, spasticity, contractures, growth restriction, brain malformation, and a maternal-family pattern of similarly affected males or early childhood deaths. Clinical findings are not sufficiently specific for diagnosis.

Baseline evaluation should be phenotype-directed: neurologic and developmental examination; EEG; brain MRI; formal ophthalmology including optic-nerve assessment; audiology; growth and nutritional assessment; swallow/aspiration assessment when indicated; respiratory review; orthopedic range-of-motion assessment; and cardiac/renal evaluation guided by findings. No diagnostic blood metabolite, enzyme assay, histopathologic marker, or circulating biomarker is established.

### Genetic testing strategy

1. **Known familial variant:** targeted Sanger or validated NGS testing for RBMX c.484_486del, followed by segregation testing.
2. **Matching phenotype without known family allele:** trio genome sequencing is particularly appropriate because the causal locus is GC-rich and complicated by RBMX-like retrocopies; exome sequencing missed the familial allele before genome/linked-read approaches resolved it.
3. **Panel/WES:** an intellectual-disability/epilepsy/brain-malformation panel including RBMX or trio WES may be used, but laboratories must document coverage and mapping quality for RBMX exon sequence and distinguish retrocopies.
4. **CMA:** useful for broader syndromic ID differentials and Xq26 copy-number changes, but it will not detect this three-base deletion.
5. **Karyotype/FISH:** low yield for the known lesion; reserve for suspected large rearrangements.
6. **RNA studies:** may help resolve splice VUS, but Pro162del did not produce detectable aberrant RBMX splicing.
7. Mitochondrial, repeat-expansion, liquid-biopsy, proteomic, metabolomic, or epigenomic testing is not disease-specific. (johansson2024gustavsonsyndromeis pages 5-7, johansson2024gustavsonsyndromeis pages 2-4)

Carrier testing and X-inactivation studies can aid interpretation, but blood X-inactivation does not guarantee the same pattern in brain and should not be used alone to predict a female fetus's phenotype.

### Differential diagnosis

Important alternatives include other syndromic XLID disorders, particularly **Shashi syndrome/RBMX-related neurodevelopmental disorder**, Christianson-type X-linked disorders, L1CAM-related disease, CASK-related microcephaly with pontine/cerebellar hypoplasia, MECP2-related disease in females, HNRNPU-related developmental epileptic encephalopathy, congenital infection, metabolic disease, and chromosomal/CNV syndromes. Gustavson syndrome is favored by the exact RBMX Pro162del allele and family segregation, not by phenotype alone. The 1993 authors differentiated it from syndromes characterized by hypogonadism, ophthalmoplegia, obesity/endocrine disease, renal/genital anomalies, neonatal hypotonia, anemia, coarse facies, or distinctive skeletal abnormalities. (tilliole2024hnrnpsrolesin pages 13-14, gustavson1993newxlinkedsyndrome pages 4-5)

## 11. Outcome and prognosis

Prognosis in the original family was poor. Reported deaths occurred at **6 months**, **1 year**, and **2 years 1 month**, and the extended description reports death generally before age four, often from pneumonia, bronchitis, or other pulmonary infection. No five- or ten-year survival estimate, mortality rate, or modern intensive-support outcome is available. (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2)

Expected morbidity includes profound cognitive and communication impairment, epilepsy, blindness/severe visual impairment, deafness, spasticity, immobility, joint deformity, growth/nutritional difficulty, and recurrent respiratory illness. Recovery of the underlying neurodevelopmental deficits has not been reported. Disease-specific prognostic biomarkers do not exist; likely clinical prognostic factors include seizure control, severity of brain malformation, swallowing/airway safety, nutritional state, mobility, and respiratory infections, but these have not been formally modeled.

## 12. Treatment and current applications

There is **no approved disease-modifying therapy** and no evidence for genotype-specific pharmacotherapy. Searches identified no Gustavson-specific interventional clinical trial or NCT record. There are no published response rates, comparative treatment cohorts, pharmacogenomic recommendations, gene therapy, RNA therapy, cell therapy, or surgery directed at RBMX dysfunction.

Real-world care is therefore multidisciplinary and phenotype-directed:

- individualized antiseizure medication and rescue planning (**NCIT: Anticonvulsant Therapy**);
- respiratory infection treatment, immunization, airway-clearance support, and assessment for aspiration;
- nutrition, feeding therapy, and enteral support when oral feeding is unsafe or inadequate (**NCIT: Nutritional Support**);
- physical and occupational therapy, positioning, orthoses, and contracture prevention (**NCIT: Physical Therapy; Occupational Therapy; Rehabilitation Therapy**);
- spasticity treatment with stretching, medication, focal botulinum toxin, or orthopedic procedures according to standard pediatric-neurology practice—not disease-specific evidence;
- audiologic amplification/communication support and low-vision services;
- augmentative and alternative communication, developmental services, and palliative-care involvement where burdens are severe;
- cardiology, urology, and orthopedic management when associated abnormalities are present.

Because pulmonary infection accounted for several deaths, respiratory and swallowing surveillance is a particularly rational management priority, although no syndrome-specific protocol has been tested. (johansson2024gustavsonsyndromeis pages 1-2, gustavson1993newxlinkedsyndrome pages 1-2)

## 13. Prevention

The mutation's occurrence cannot be prevented by lifestyle modification, vaccination, or environmental control. **Primary genetic prevention options** are nondirective reproductive counseling, preimplantation genetic testing for monogenic disease, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and use of donor gametes. **Secondary prevention** comprises cascade testing of at-risk maternal relatives and early molecular diagnosis of at-risk pregnancies or newborns. Population newborn screening is not indicated because the condition is extraordinarily rare and lacks a validated population assay or presymptomatic disease-modifying treatment.

**Tertiary prevention** should target seizures, aspiration, malnutrition, respiratory infection, pressure injury, hip displacement, and contractures. Routine childhood vaccines—including influenza and pneumococcal vaccination when clinically indicated—may reduce infectious morbidity but do not prevent Gustavson syndrome. Genetic counseling should discuss uncertain female penetrance and the limitations of using blood X-inactivation to forecast neurologic outcome.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility is known. Relevant experimental species are **Homo sapiens (NCBI Taxon 9606)**, **Danio rerio (7955)**, **Xenopus laevis (8355)**, and **Mus musculus (10090)**. Their RBMX/Rbmx orthologs are evolutionarily conserved, supporting the protein's developmental importance, but they should be annotated as experimental models rather than naturally occurring Gustavson syndrome. (johansson2024gustavsonsyndromeis pages 7-8, tilliole2025rbmxfunctionalretrocopy pages 38-42)

## 15. Model organisms and experimental systems

- **Zebrafish:** rbmx knockdown demonstrated that the gene is essential for brain development; published November 2005, DOI: https://doi.org/10.1002/dvdy.20432. This is loss-of-function support, not a Pro162del knock-in model. (tilliole2025rbmxfunctionalretrocopy pages 38-42)
- **Xenopus:** expression-cloning/depletion experiments found Rbmx necessary for embryogenesis and neural and muscle development; published July 2008, DOI: https://doi.org/10.1002/dvdy.21590. Again, this is gene-level rather than allele-specific evidence. (tilliole2025rbmxfunctionalretrocopy pages 38-42)
- **Human SH-SY5Y neuronal cells:** wild-type and Pro162del constructs enabled localization, expression, transcriptomic, and splicing analyses. This is the most direct disease-variant cellular model, but transformed neuroblastoma cells do not reproduce cortical development. (johansson2024gustavsonsyndromeis pages 5-7)
- **HeLa/minigene system:** used to test predicted splicing effects; no aberrant RBMX splicing was detected. Its non-neural context is a limitation. (johansson2024gustavsonsyndromeis pages 5-7)
- **Biochemical peptide model:** fluorescence polarization tested wild-type and ΔPro162 peptides against BIN1- and ASAP1-SH3 domains. It identified possible context-dependent interaction weakening but not the native cellular partner network. (johansson2024gustavsonsyndromeis pages 7-8, johansson2024gustavsonsyndromeis pages 5-7)

No validated Pro162del mouse, zebrafish knock-in, patient-derived iPSC, cortical organoid, or natural animal model was available in the 2023–2024 evidence. Such models are the key research gap for connecting altered hnRNP G interactions to specific cortical, sensory, motor, and survival phenotypes.

## Key primary-source quotations

The 2024 molecular paper's abstract states: **“Extensive genomic analyses of the family revealed hemizygosity for a novel in-frame deletion in RBMX in affected individuals (NM_002139.4; c.484_486del, p.(Pro162del)).”** It further reports: **“Carrier females were asymptomatic and presented with skewed X-chromosome inactivation, indicating silencing of the pathogenic allele.”** Finally, its mechanistic conclusion is appropriately cautious: **“The results indicate that disruption of different protein domains affects the severity of RBMX-associated intellectual disabilities.”** Publication: online 5 June 2023; volume publication 2024; PMID 37277488; DOI: https://doi.org/10.1038/s41431-023-01392-y. (johansson2024gustavsonsyndromeis pages 1-2, johansson2024gustavsonsyndromeis pages 2-2)

The original report described **“a family with an X-linked mental retardation syndrome involving seven children in two generations”** and its title enumerated the defining findings: severe intellectual disability, severely impaired vision, severe hearing defect, epileptic seizures, spasticity, restricted joint mobility, and early death. Publication: March 1993; PMID 8456840; DOI: https://doi.org/10.1002/ajmg.1320450527. (christianson1999xlinkedsevere pages 7-8, gustavson1993newxlinkedsyndrome pages 1-2)

## Overall assessment

The causal assignment of RBMX p.Pro162del is compelling within the Swedish pedigree, supported by segregation, protective X-inactivation, neuronal-cell expression changes, and biochemical interaction data. However, the path from altered hnRNP G molecular interactions to each clinical feature remains incompletely demonstrated. The most defensible current mechanism is **domain-specific disruption of RBMX-mediated transcriptional/RNA regulation during early neurodevelopment**, with disturbed SH3 binding as a plausible contributor rather than a settled mechanism. Replication in unrelated patients and allele-specific developmental models is required before estimating population penetrance, defining a complete phenotypic spectrum, or developing targeted therapy. (johansson2024gustavsonsyndromeis pages 7-8, johansson2024gustavsonsyndromeis pages 5-7)

References

1. (johansson2024gustavsonsyndromeis pages 1-2): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

2. (OpenTargets Search: Severe X-linked intellectual disability Gustavson type): Open Targets Query (Severe X-linked intellectual disability Gustavson type, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (gustavson1993newxlinkedsyndrome pages 1-2): Karl‐Henrik Gustavson, Göran Annerén, Helena Malmgren, Niklas Dahl, Carl‐Gustaf Ljunggren, and Hans Bäckman. New x-linked syndrome with severe mental retardation, severely impaired vision, severe hearing defect, epileptic seizures, spasticity, restricted joint mobility, and early death. American journal of medical genetics, 45 5:654-8, Mar 1993. URL: https://doi.org/10.1002/ajmg.1320450527, doi:10.1002/ajmg.1320450527. This article has 37 citations.

4. (johansson2024gustavsonsyndromeis pages 2-4): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (johansson2024gustavsonsyndromeis pages 2-2): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

6. (johansson2024gustavsonsyndromeis pages 5-7): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

7. (gustavson1993newxlinkedsyndrome pages 4-5): Karl‐Henrik Gustavson, Göran Annerén, Helena Malmgren, Niklas Dahl, Carl‐Gustaf Ljunggren, and Hans Bäckman. New x-linked syndrome with severe mental retardation, severely impaired vision, severe hearing defect, epileptic seizures, spasticity, restricted joint mobility, and early death. American journal of medical genetics, 45 5:654-8, Mar 1993. URL: https://doi.org/10.1002/ajmg.1320450527, doi:10.1002/ajmg.1320450527. This article has 37 citations.

8. (johansson2024gustavsonsyndromeis pages 7-8): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (tilliole2024hnrnpsrolesin pages 13-14): Pierre Tilliole, Simon Fix, and Juliette D. Godin. Hnrnps: roles in neurodevelopment and implication for brain disorders. Frontiers in Molecular Neuroscience, Jul 2024. URL: https://doi.org/10.3389/fnmol.2024.1411639, doi:10.3389/fnmol.2024.1411639. This article has 28 citations.

10. (tilliole2025rbmxfunctionalretrocopy pages 38-42): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

11. (christianson1999xlinkedsevere pages 7-8): Arnold L Christianson, Roger E Stevenson, C H van der Meyden, Julie Pelser, Francois W Theron, Petro L van Rensburg, Michael Chandler, and Charles E Schwartz. X linked severe mental retardation, craniofacial dysmorphology, epilepsy, ophthalmoplegia, and cerebellar atrophy in a large south african kindred is localised to xq24-q27. Journal of Medical Genetics, 36(10):759-766, Oct 1999. URL: https://doi.org/10.1136/jmg.36.10.759, doi:10.1136/jmg.36.10.759. This article has 144 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Severe_X-linked_Intellectual_Disability_Gustavson_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.