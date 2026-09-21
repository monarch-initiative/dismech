---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:44:55.591319'
end_time: '2026-09-02T18:03:19.725543'
duration_seconds: 1104.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 6
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - Orphanet
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Radioulnar_Synostosis_with_Amegakaryocytic_Thrombocytopenia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia** covering all of the
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
- **Disease Name:** Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia** covering all of the
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


# Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia: Disease Characteristics Report

**Scope and evidence date.** This report treats radioulnar synostosis with amegakaryocytic thrombocytopenia (RUSAT) as an umbrella phenotype comprising **HOXA11-associated RUSAT1** and **MECOM-associated RUSAT2**. For MECOM, the broader term **MECOM-associated syndrome** is often preferable because radioulnar synostosis (RUS), thrombocytopenia, or both may be absent. Evidence is predominantly aggregated case reports and small family cohorts rather than population registries or individual EHR-derived data. No disease-specific management guideline or randomized therapeutic trial was identified.

| Entity / identifier | Causal gene and inheritance | Hallmark phenotype / course | Mechanism / evidence | Diagnostic / treatment implications |
|---|---|---|---|---|
| **Aggregate RUSAT syndrome** — MONDO:0011555; Orphanet:71289 | Genetically heterogeneous; established causes are heterozygous germline variants in **HOXA11** or **MECOM**, usually autosomal dominant, frequently de novo, with variable expressivity and incomplete penetrance (OpenTargets Search: Radioulnar synostosis with amegakaryocytic thrombocytopenia-HOXA11,MECOM, walne2018expandingthephenotypic pages 1-5) | Congenital proximal radioulnar synostosis with amegakaryocytic thrombocytopenia; thrombocytopenia may progress to pancytopenia, hypocellular marrow, and global bone-marrow failure. Either skeletal or hematologic manifestations can occasionally be absent in molecularly related disease. Suggested HPO: **Radioulnar synostosis**, **Thrombocytopenia**, **Pancytopenia**, **Hypocellular bone marrow**, **Decreased megakaryocytes** (walne2018expandingthephenotypic pages 1-5, germeshausen2018mecomassociatedsyndromea pages 1-2) | Developmental transcription-factor dysfunction links forelimb patterning to hematopoietic and megakaryocytic failure. The precise downstream causal network remains incompletely resolved (niihori2015mutationsinmecom pages 3-5, germeshausen2018mecomassociatedsyndromea pages 7-7) | Evaluate CBC/smear, marrow cellularity and megakaryocytes, bilateral forearm radiographs, family history, and germline **HOXA11/MECOM** testing. Severe marrow failure requires transfusion/infection support and consideration of allogeneic HSCT; orthopedic intervention is based on functional limitation (germeshausen2018mecomassociatedsyndromea pages 4-5, walne2018expandingthephenotypic pages 8-13) |
| **RUSAT1 / HOXA11-associated disease** — OMIM:605432 | **HOXA11**; heterozygous germline, autosomal dominant; familial cases established, with markedly variable hematologic expression (walne2018expandingthephenotypic pages 1-5, germeshausen2018mecomassociatedsyndromea pages 1-2) | Usually congenital bilateral RUS and thrombocytopenia from birth; reported spectrum ranges from no major hematologic problems to early bone-marrow failure. Additional findings can include clinodactyly, hip dysplasia, and sensorineural hearing loss. Suggested HPO: **Congenital onset**, **Abnormality of forearm**, **Clinodactyly**, **Sensorineural hearing impairment** (walne2018expandingthephenotypic pages 1-5, walne2018expandingthephenotypic pages 8-13) | HOXA11 is a homeobox transcription factor required for limb development and hematopoietic differentiation. Human genotype–phenotype evidence is strong, but subtype-specific downstream targets and pathway causality remain less well characterized than for MECOM (niihori2015mutationsinmecom pages 1-2, walne2018expandingthephenotypic pages 8-13) | Confirm with germline HOXA11 sequencing after clinical/radiographic recognition; include deletion/CNV analysis if sequencing is unrevealing. Monitor serial blood counts and marrow function. HSCT treats progressive marrow failure but does not correct congenital synostosis (walne2018expandingthephenotypic pages 1-5, walne2018expandingthephenotypic pages 8-13) |
| **RUSAT2 / MECOM-associated syndrome** — MONDO:0014758; OMIM:616738 | **MECOM**; pathogenic heterozygous germline variants or constitutional deletions; autosomal dominant, often de novo, with variable expressivity, incomplete penetrance, and occasional somatic genetic rescue (germeshausen2018mecomassociatedsyndromea pages 2-2, venugopal2024unravelingfacetsof pages 1-2, venugopal2024unravelingfacetsof pages 2-3) | Continuous spectrum from isolated RUS without cytopenia to congenital amegakaryocytic thrombocytopenia, pancytopenia, aplastic anemia, MDS, or severe neonatal BMF without RUS. Other features include clinodactyly/brachydactyly, cardiac or renal anomalies, B-cell deficiency, hearing loss, and vascular disease. In a 64-case literature summary: RUS 45.3%, pancytopenia 56.2%, thrombocytopenia 25.0%, and no cytopenia 12.5%. Suggested HPO: **B-cell lymphopenia**, **Aplastic anemia**, **Myelodysplasia**, **Congenital heart defect**, **Renal malformation** (huang2024anovelmissense pages 3-5, venugopal2024unravelingfacetsof pages 1-2) | MECOM/EVI1 zinc-finger variants impair DNA occupancy and alter AP-1 and TGF-β transcriptional responses; patient and mouse evidence supports reduced HSPC maintenance/self-renewal. MPL downregulation is not consistently demonstrated. Somatic copy-neutral 3q loss of heterozygosity can duplicate the wild-type allele and rescue hematopoiesis (niihori2015mutationsinmecom pages 3-5, germeshausen2018mecomassociatedsyndromea pages 7-7, venugopal2024unravelingfacetsof pages 2-3) | Use an inherited-BMF panel or trio WES/WGS with MECOM SNV/indel and CNV analysis; test nonhematopoietic DNA after HSCT or when somatic rescue is suspected. Assess CBC, marrow, B cells/immunoglobulins, hearing, renal and cardiac anatomy, and forearm radiographs. HSCT can normalize hematopoiesis; 2024 evidence supports long-term surveillance for clonal hematopoiesis, dysplasia, and myeloid malignancy (huang2024anovelmissense pages 3-5, venugopal2024unravelingfacetsof pages 1-2) |


*Table: Compact knowledge-base comparison of aggregate RUSAT and its HOXA11- and MECOM-associated subtypes, including identifiers, inheritance, phenotype, mechanism, ontology suggestions, and clinical implications.*

## 1. Disease information

RUSAT is a rare, congenital, inherited bone-marrow-failure syndrome coupling abnormal forearm development—usually proximal fusion of the radius and ulna—with deficient megakaryopoiesis and thrombocytopenia that can progress to pancytopenia. The synostosis severely restricts pronation and supination. Molecularly related disease spans isolated RUS, congenital amegakaryocytic thrombocytopenia, aplastic anemia, and global marrow failure with or without skeletal anomalies. The original MECOM study states: **“RUSAT is an inherited bone marrow failure syndrome, characterized by thrombocytopenia and congenital fusion of the radius and ulna.”** (niihori2015mutationsinmecom pages 1-2)

**Identifiers and synonyms**

- Aggregate syndrome: **MONDO:0011555**, **Orphanet:71289**.
- RUSAT1/HOXA11-associated disease: **OMIM 605432**.
- RUSAT2/MECOM-associated disease: **OMIM 616738**, **MONDO:0014758**.
- Broader MECOM phenotype: **MECOM-associated syndrome**, MONDO:0100458.
- Synonyms include *radio-ulnar synostosis–amegakaryocytic thrombocytopenia syndrome*, *RUSAT*, *congenital thrombocytopenia with radioulnar synostosis*, and historically *CTRUS*. OpenTargets links the aggregate entity to both MECOM and HOXA11, with primary-literature support from PMIDs **26581901**, **29540340**, and **11101832**. OSGEP appears as a low-score database association but is not an established RUSAT causal gene and should not be curated as such without independent validation. (OpenTargets Search: Radioulnar synostosis with amegakaryocytic thrombocytopenia-HOXA11,MECOM)
- No dedicated MeSH, ICD-10, or ICD-11 code was established in the retrieved evidence; coding ordinarily uses the relevant congenital limb-malformation and thrombocytopenia/bone-marrow-failure codes rather than a disease-specific code.

## 2. Etiology, risk, and protective factors

### Genetic causes

RUSAT is principally a **heterozygous germline transcription-factor disorder**:

1. **RUSAT1:** heterozygous pathogenic **HOXA11** variants. The landmark report identified HOXA11 disease in two unrelated families (Thompson & Nguyen, *Nature Genetics*, 1 December 2000; PMID **11101832**; DOI: https://doi.org/10.1038/82511). Subsequent cohorts indicate very few molecularly confirmed HOXA11 families. (germeshausen2018mecomassociatedsyndromea pages 1-2)
2. **RUSAT2/MECOM-associated syndrome:** heterozygous pathogenic **MECOM** sequence variants or constitutional deletions affecting 3q26.2. Variants are often de novo, although multigenerational autosomal-dominant transmission occurs. (walne2018expandingthephenotypic pages 1-5, germeshausen2018mecomassociatedsyndromea pages 2-2)

**Risk factors.** Carrying a pathogenic germline allele is the only established primary risk factor. Family history increases prior probability but may be absent because of de novo mutation, incomplete penetrance, mild parental disease, or somatic rescue. Sex, ethnicity, consanguinity, age, lifestyle, toxins, occupation, infection, and prenatal exposure are not established etiologic risk factors. No founder mutation or reliable carrier-frequency estimate is known.

**Protective factors.** No inherited protective allele, diet, lifestyle, medication, or environmental exposure has been validated. A notable endogenous modifier is **somatic genetic rescue**: in four individuals, copy-neutral loss of heterozygosity across chromosome 3q duplicated the residual wild-type MECOM allele in an expanding hematopoietic clone and was associated with milder or resolving cytopenia. This is a post-zygotic disease modifier, not a clinically deployable preventive factor. (venugopal2024unravelingfacetsof pages 2-3)

**Gene–environment interaction.** None has been demonstrated. Infections can aggravate morbidity in already cytopenic or immunodeficient patients but do not cause the Mendelian syndrome.

## 3. Phenotypes

The most useful phenotype summary comes from a 2024 review of **64 MECOM-associated individuals**. RUS occurred in **45.3%**; other skeletal malformations in **42.2%**; pancytopenia in **36/64 (56.2%)**; isolated thrombocytopenia in **16/64 (25.0%)**; and no cytopenia in **8/64 (12.5%)**. Reported extrahematologic frequencies were nail/facial abnormalities **23.4%**, neurologic findings **17.2%**, hearing impairment **14.1%**, renal abnormalities **9.4%**, precocious puberty **6.3%**, and immune dysfunction such as B-cell deficiency or hypogammaglobulinemia **10/64 (15.6%)**. The paper prints cardiac malformations as “27/64, 26.6%”; because 27/64 is 42.2%, that internally inconsistent statistic should be verified against its supplement before database ingestion. (huang2024anovelmissense pages 3-5)

### Core phenotypes and suggested HPO annotations

- **Congenital proximal radioulnar synostosis**—usually bilateral; stable structural defect but lifelong limitation of forearm rotation. Suggested: *Radioulnar synostosis*, *Bilateral radioulnar synostosis*, *Limited forearm supination/pronation*, *Congenital onset*. Functional impact ranges from mild compensation to difficulty feeding, dressing, personal hygiene, writing, and positioning the hand.
- **Thrombocytopenia / amegakaryocytic thrombocytopenia**—often neonatal or infantile, severe and persistent or occasionally improving. Suggested: *Thrombocytopenia*, *Decreased megakaryocytes*, *Petechiae*, *Ecchymosis*, *Abnormal bleeding*, *Intracranial hemorrhage*.
- **Progressive marrow failure**—thrombocytopenia may broaden to anemia, neutropenia, pancytopenia, hypocellular marrow, aplastic anemia, or MDS. Suggested: *Pancytopenia*, *Anemia*, *Neutropenia*, *Hypocellular bone marrow*, *Bone marrow failure*, *Myelodysplasia*. (germeshausen2018mecomassociatedsyndromea pages 4-5, walne2018expandingthephenotypic pages 8-13)
- **Hand and lower-limb anomalies**—clinodactyly, brachydactyly/brachymesophalangy, abnormal fifth phalanges, overlapping fingers, nail anomalies, hip dysplasia, and occasionally absent patella. Suggested: *Clinodactyly*, *Brachydactyly*, *Abnormality of the fifth finger*, *Nail abnormality*, *Hip dysplasia*, *Patellar aplasia*. (niihori2015mutationsinmecom pages 1-2, venugopal2024unravelingfacetsof pages 3-4)
- **Immune phenotype**—B-cell lymphopenia or hypogammaglobulinemia, with recurrent bacterial/fungal infection in severe cases. Suggested: *B-cell lymphopenia*, *Hypogammaglobulinemia*, *Recurrent infection*. (germeshausen2018mecomassociatedsyndromea pages 5-6, germeshausen2018mecomassociatedsyndromea pages 4-5)
- **Other variable manifestations**—sensorineural hearing loss, congenital heart defects, aortic dilatation, renal/urinary malformations, cleft palate, and occasional neurodevelopmental abnormalities. Suggested: *Sensorineural hearing impairment*, *Congenital heart defect*, *Aortic dilatation*, *Renal hypoplasia*, *Cleft palate*, *Intellectual disability*. (venugopal2024unravelingfacetsof pages 6-7, germeshausen2018mecomassociatedsyndromea pages 8-9, germeshausen2018mecomassociatedsyndromea pages 5-5)

No disease-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life study was identified. Quality-of-life effects are inferred from bleeding, transfusion dependence, infection, transplantation, and upper-limb functional restriction.

## 4. Genetic and molecular information

### Genes and representative variants

- **HOXA11** encodes a homeobox transcription factor involved in limb patterning and hematopoietic differentiation. The established RUSAT1 lesion is germline and heterozygous; published human evidence remains limited to a few families. (germeshausen2018mecomassociatedsyndromea pages 1-2, niihori2015mutationsinmecom pages 1-2)
- **MECOM** encodes alternatively transcribed/spliced MDS1, MDS1-EVI1, and EVI1 zinc-finger transcription-factor isoforms. It contains ten zinc fingers and regulates hematopoietic stem/progenitor-cell maintenance. (venugopal2024unravelingfacetsof pages 1-2)

The 2015 discovery study identified **NM_001105078:c.2266A>G (p.Thr756Ala), c.2252A>G (p.His751Arg), and c.2248C>T (p.Arg750Trp)**. All affected the conserved eighth C-terminal zinc finger or adjacent residues and were absent from 382 ancestry-matched controls and dbSNP, 1000 Genomes, HGVD, and ExAC. At least two were de novo. (niihori2015mutationsinmecom pages 1-2, niihori2015mutationsinmecom pages 2-3)

Other reported MECOM variants include **p.His751Tyr, p.Gln759Leu, p.Pro760Ser, p.Cys766Arg, p.Glu758Lys, p.Pro760Ala**, splice loss **c.2208-1_2208delGA**, and multiple frameshift/nonsense alleles and constitutional deletions. Missense variants associated with RUS cluster particularly around zinc fingers 8–9, whereas truncating variants are distributed more broadly and often produce severe marrow failure, although this is not an absolute genotype–phenotype rule. (walne2018expandingthephenotypic pages 1-5, germeshausen2018mecomassociatedsyndromea pages 4-5)

A January 2024 case identified de novo **NM_001105078.3:c.2285G>A (p.Arg762Lys)**, absent from public databases and classified **likely pathogenic** under ACMG criteria. The literature review counted 64 distinct variants: missense **35/64 (54.7%)**, deletion **8/64 (12.5%)**, frameshift **6/64 (9.4%)**, nonsense **6/64 (9.4%)**, splice **5/64 (7.8%)**, and unreported class **4/64**. (huang2024anovelmissense pages 3-5)

All established causal alleles are constitutional/germline; somatic MECOM overexpression or rearrangement in cancer is biologically distinct. Somatic copy-neutral 3q loss of heterozygosity may rescue germline disease. No validated modifier gene, disease-specific methylation signature, or causal epigenetic lesion has been established. Large constitutional 3q26 deletions involving MECOM can cause severe multisystem disease; therefore, copy-number analysis is important when sequencing is negative. (germeshausen2018mecomassociatedsyndromea pages 9-9, venugopal2024unravelingfacetsof pages 2-3)

## 5. Environmental information

No toxin, radiation exposure, pollutant, smoking, alcohol, diet, exercise pattern, occupational exposure, or infectious agent is known to initiate RUSAT. Viral testing in reported infants was used to exclude acquired congenital cytopenia rather than establish causation. Environmental and public-health interventions therefore do not prevent the primary disorder.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline **HOXA11** or **MECOM** lesion **leads to** abnormal activity or dosage of a developmental transcription factor.
2. In MECOM missense disease, disruption of conserved zinc-finger structure **leads to** reduced or altered DNA binding; in truncating/deletion disease, haploinsufficiency is inferred to **lead to** reduced MECOM function. (niihori2015mutationsinmecom pages 2-3, germeshausen2018mecomassociatedsyndromea pages 4-5)
3. Altered transcription-factor function **results in** dysregulation of hematopoietic stem/progenitor-cell self-renewal and survival; the exact target network remains incompletely defined. (venugopal2024unravelingfacetsof pages 1-2, germeshausen2018mecomassociatedsyndromea pages 7-7)
4. Reduced HSPC maintenance **leads to** depletion of early progenitors and impaired megakaryopoiesis, **resulting in** absent/reduced megakaryocytes and congenital thrombocytopenia. (germeshausen2018mecomassociatedsyndromea pages 5-5)
5. Continued progenitor exhaustion **leads to** multilineage failure, causing anemia, neutropenia, pancytopenia, aplastic marrow, and—occasionally—dysplasia or myeloid malignancy.
6. **Parallel developmental branch:** altered HOXA11/MECOM transcription during embryonic limb-bud patterning **leads to** abnormal segmentation/remodeling of radius and ulna, resulting in congenital proximal RUS; this developmental link is strongly genotype-associated but its intervening molecular steps remain inferred. (niihori2015mutationsinmecom pages 3-5)
7. **Additional branches:** developmental transcriptional disturbance can **lead to** hand, cardiac, renal, auditory, and B-cell abnormalities; exact tissue-specific pathways are incompletely demonstrated.
8. In some individuals, somatic copy-neutral 3q loss of heterozygosity **duplicates** the wild-type MECOM allele and **results in** clonal hematopoietic rescue. Conversely, age-related acquisition of ASXL1, DNMT3A, TET2, ETV6, or 20q-loss clones may **lead to** improved short-term cellular fitness but potentially increase dysplasia/malignancy risk. (venugopal2024unravelingfacetsof pages 2-3)

### Demonstrated versus inferred mechanisms

Structural modeling placed p.Arg750Trp at a predicted DNA-contact residue and implicated p.His751Arg in zinc-finger folding. ChIP-qPCR directly demonstrated reduced occupancy at **RUNX1 exon 1** for p.Arg750Trp and p.His751Arg and at the **CD109 promoter** for p.Arg750Trp. Reporter assays showed enhanced suppression of AP-1 signaling—interpreted as a gain-of-function effect—and attenuated suppression of TGF-β-responsive transcription—partial loss of function. The authors appropriately concluded: **“These functional assays suggest that transcriptional dysregulation by mutant EVI1 could be associated with the development of RUSAT.”** (niihori2015mutationsinmecom pages 1-2, niihori2015mutationsinmecom pages 3-5)

MPL is not a proven uniform downstream mediator. MECOM and MPL correlate positively in human AML, whereas murine work suggested Evi1 can repress Mpl. Patient CD34+CD38-low cells retained detectable MPL, and very high thrombopoietin was interpreted as secondary to depletion of MPL-expressing cells rather than direct proof of MECOM-mediated MPL suppression. (germeshausen2018mecomassociatedsyndromea pages 7-7, germeshausen2018mecomassociatedsyndromea pages 5-5)

**Suggested GO terms:** DNA-binding transcription-factor activity; regulation of transcription by RNA polymerase II; hematopoietic stem-cell maintenance; stem-cell self-renewal; megakaryocyte differentiation; platelet formation; embryonic limb morphogenesis; regulation of apoptotic process; TGF-β receptor signaling; AP-1-mediated transcription. **Suggested CL terms:** hematopoietic stem cell, hematopoietic multipotent progenitor cell, megakaryocyte progenitor, megakaryocyte, platelet, B lymphocyte, osteoblast/chondrocyte lineage cells. These are annotation suggestions, not all experimentally demonstrated disease-cell targets.

No disease-specific single-cell atlas, spatial transcriptomic dataset, metabolomic/lipidomic signature, or multi-omics diagnostic classifier was identified.

## 7. Anatomical structures affected

- **Primary:** proximal radius and ulna, elbow/forearm rotational unit; bone marrow and circulating blood.
- **Secondary/variable:** fingers, phalanges, nails, patella and hip; heart and aorta; kidneys/urinary tract; inner ear/auditory pathway; immune/B-cell compartment.
- **Tissues/cells:** developing skeletal connective tissue and cartilage/bone; hematopoietic stem/progenitor cells; megakaryocytes; B lymphocytes.
- **Subcellular:** MECOM and HOXA11 are nuclear transcription factors; relevant GO cellular-component annotations include **nucleus**, **chromatin**, and **transcription regulator complex**.
- **Localization:** RUS is usually proximal and bilateral, although unilateral or radiographically subtle disease can occur. Suggested UBERON concepts: radius, ulna, forearm, elbow joint, bone marrow, heart, aorta, kidney, inner ear.

## 8. Temporal development

The skeletal lesion is prenatal and congenital, generally structurally stable. Hematologic onset ranges from fetal hydrops or neonatal hemorrhage to childhood or late-adult disease. In the 2024 15-person cohort, onset ranged **from in utero to late adulthood**, and one carrier remained comparatively well into the sixth decade. (venugopal2024unravelingfacetsof pages 6-7, venugopal2024unravelingfacetsof pages 2-3)

Typical untreated trajectories are: isolated stable RUS; congenital thrombocytopenia that remains isolated or transiently improves; or thrombocytopenia progressing variably to pancytopenia and marrow failure. Somatic rescue may produce spontaneous hematologic remission, whereas clonal hematopoiesis and dysplasia may emerge with age. Critical intervention periods are severe neonatal bleeding and the transition to transfusion dependence, severe neutropenia, recurrent infection, cytogenetic abnormality, or dysplasia.

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with both de novo and familial variants. Penetrance is incomplete and expressivity exceptionally variable, including discordant skeletal and hematologic findings within families. Genetic anticipation is not established. Germline/gonadal mosaicism is theoretically possible but not quantified. No confirmed founder effect, ethnic enrichment, sex bias, incidence, or prevalence estimate exists; fewer than 100 MECOM-associated individuals had been reported by 2024, and HOXA11-confirmed disease is rarer still. These counts reflect publication ascertainment, not population prevalence. (germeshausen2018mecomassociatedsyndromea pages 2-2, venugopal2024unravelingfacetsof pages 1-2)

A 2024 cohort reported **12 losses among 16 pregnancies (75%)** in five mothers with detailed histories, versus quoted general-population loss rates of 15–25%. Some losses also occurred in wild-type relatives and fetal genotypes were unavailable, so this striking association is hypothesis-generating rather than a penetrance estimate. (venugopal2024unravelingfacetsof pages 2-3)

## 10. Diagnostics

### Recommended approach

1. **CBC with differential, reticulocytes, smear, and bleeding assessment.** Repeat serially because lineage involvement evolves.
2. **Bone-marrow aspirate/biopsy** when cytopenia is unexplained or progressive: assess cellularity, megakaryocytes, dysplasia, fibrosis, cytogenetics, and acquired myeloid variants.
3. **Bilateral forearm radiographs** to detect proximal RUS, even if external deformity is subtle. Hand/foot imaging may document associated skeletal anomalies.
4. **Germline testing:** inherited-BMF/thrombocytopenia panel containing **MECOM, HOXA11, MPL, RBM8A**, and relevant differential genes, or trio WES/WGS. Include MECOM exon-level and 3q26 copy-number/structural-variant analysis.
5. Use **nonhematopoietic DNA**—cultured skin fibroblasts, hair follicles, or carefully interpreted buccal samples—after HSCT or if somatic rescue/clonal hematopoiesis may mask the germline allele. (venugopal2024unravelingfacetsof pages 6-7, niihori2015mutationsinmecom pages 1-2)
6. Baseline evaluations should include hearing, B-cell count and immunoglobulins, echocardiography/aortic imaging, renal ultrasound and renal function, and orthopedic functional assessment.

The 2024 p.Arg762Lys case illustrates diagnostic severity: neutrophils **0.07×10⁹/L**, hemoglobin **17 g/L**, platelets **1×10⁹/L**, hypocellular marrow with megakaryocyte depletion, B cells **0.09×10⁹/L**, bilateral superior RUS, clinodactyly/brachydactyly, and subarachnoid hemorrhage. Infection, autoimmune, coagulation, hemoglobinopathy, chromosome-breakage, and karyotype studies were unrevealing; trio WES established diagnosis. (huang2024anovelmissense pages 1-3, huang2024anovelmissense pages 3-5)

### Differential diagnosis

Major alternatives are **MPL-related congenital amegakaryocytic thrombocytopenia**, thrombocytopenia-absent radius syndrome (**RBM8A**; absent radii with thumbs present rather than radioulnar fusion), Fanconi anemia, Diamond–Blackfan anemia, dyskeratosis congenita/telomere disorders, GATA2 deficiency, RUNX1/ETV6/ANKRD26-related thrombocytopenia, MYH9-related disease, neonatal alloimmune thrombocytopenia, congenital infection, sepsis/DIC, and other syndromic RUS disorders. Normal chromosome-breakage testing helps exclude Fanconi anemia but does not establish RUSAT. (germeshausen2018mecomassociatedsyndromea pages 4-5, walne2018expandingthephenotypic pages 8-13, germeshausen2018mecomassociatedsyndromea pages 1-2)

CMA/karyotype/FISH are useful when a constitutional deletion or acquired clone is suspected. Mitochondrial, repeat-expansion, liquid-biopsy, metabolomic, and epigenomic testing have no established disease-specific role. Population newborn screening is unavailable; cascade testing is appropriate after a familial variant is found.

## 11. Outcome and prognosis

There are no reliable 5- or 10-year survival rates. Prognosis depends chiefly on bleeding severity, depth and progression of marrow failure, infection, donor availability and HSCT complications, and acquisition of dysplastic/malignant clones. Severe neonatal disease may cause intracranial hemorrhage, sepsis, or early death; other carriers remain mildly affected into adulthood. Reported morbidity includes transfusion dependence, recurrent infection, transplant toxicity, hearing impairment, and permanent upper-limb restriction. (germeshausen2018mecomassociatedsyndromea pages 4-5)

Among **80 previously reported MECOM-associated individuals**, four myeloid malignancies—three adult MDS and one pediatric AML—were reported, approximately **5%**; this likely underestimates lifetime risk because many patients undergo early HSCT. The 2024 study added aplasia with dysplasia and another MDS case and found age-related clonal hematopoiesis in all three older cohort members. Long-term CBC, marrow/cytogenetic, and molecular surveillance is therefore reasonable, although no evidence-based interval is established. (venugopal2024unravelingfacetsof pages 1-2)

## 12. Treatment and current applications

**No drug corrects the germline transcription-factor defect.** Management is individualized in an inherited-BMF center.

- **Supportive hematology:** platelet and red-cell transfusions for clinically significant bleeding/anemia; antimicrobial treatment and prevention according to neutropenia/immune status; avoid unnecessary immune suppression when inherited failure is likely. IVIG and corticosteroids may be used initially when immune or alloimmune thrombocytopenia is suspected but do not correct RUSAT marrow failure. Suggested NCIT concepts: platelet transfusion, red-blood-cell transfusion, anti-infective therapy, supportive care. (huang2024anovelmissense pages 3-5, germeshausen2018mecomassociatedsyndromea pages 4-5)
- **Allogeneic HSCT:** the only established definitive treatment for progressive or severe hematopoietic failure. It corrects donor-derived hematopoiesis but not congenital skeletal or other fixed organ abnormalities. Outcomes are case-based and include successful count normalization as well as deaths from transplant complications or sepsis. (germeshausen2018mecomassociatedsyndromea pages 4-5)
- In the 2024 p.Arg762Lys case, matched-unrelated-donor HSCT at 16 months reduced transfusion and infection frequency; at age four, neutrophils were **3.82×10⁹/L**, hemoglobin **122 g/L**, and platelets **317×10⁹/L**. This is individual-level evidence, not a response-rate estimate. (huang2024anovelmissense pages 3-5)
- **Orthopedic care:** occupational/physical therapy and adaptive strategies for mild functional impairment. Corrective derotational osteotomy may improve hand position in severe fixed pronation but does not restore a normal proximal joint; evidence is extrapolated from congenital RUS generally, not RUSAT-specific cohorts.
- **Hearing, renal, cardiac, and immune care** should be phenotype directed. Aortic dilatation warrants cardiology follow-up; one of three affected individuals in the 2024 cohort progressed to a surgically significant aneurysm. (venugopal2024unravelingfacetsof pages 6-7, venugopal2024unravelingfacetsof pages 5-6)

No approved gene therapy, RNA therapy, targeted small molecule, or disease-specific interventional trial was identified. Somatic wild-type-allele rescue provides a biological rationale for future gene-corrected autologous transplantation or direct editing, but this remains expert translational speculation, not clinical evidence. (venugopal2024unravelingfacetsof pages 6-7)

## 13. Prevention

Primary lifestyle prevention is not possible. Effective prevention is genetic and complication focused:

- **Genetic counseling:** a heterozygous affected parent ordinarily has a 50% transmission risk per conception, but phenotype cannot be predicted reliably because expressivity is variable and somatic rescue may modify blood findings.
- **Reproductive options:** familial-variant prenatal diagnosis and preimplantation genetic testing are technically feasible; counseling should discuss uncertain severity and the preliminary pregnancy-loss signal.
- **Secondary prevention:** cascade testing, early CBCs and forearm imaging in at-risk relatives, and rapid genetic evaluation of congenital thrombocytopenia can prevent diagnostic delay and inappropriate immune therapy.
- **Tertiary prevention:** bleeding precautions, timely transfusion, infection prevention, avoidance of marrow-toxic exposure when possible, HSCT before irreversible complications, and surveillance for cytopenic progression, dysplasia, clonal hematopoiesis, hearing loss, renal/cardiac disease, and aortic dilatation.
- Vaccination follows standard and transplant/immunodeficiency-specific schedules; there is no disease-specific vaccine or chemoprophylaxis.

## 14. Other species and natural disease

No well-established naturally occurring veterinary equivalent, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. The relevant orthologues are conserved **Hoxa11** and **Mecom/Evi1** in laboratory species. RUSAT is noninfectious and has no zoonotic potential.

## 15. Model organisms and experimental systems

- **Mouse:** heterozygous deletion of Evi1 exon 4 markedly reduces early marrow hematopoietic cells; other Evi1 models support stemness-gene expression, HSC survival/self-renewal, embryonic limb and cardiac roles. These models reproduce aspects of hematopoietic/developmental biology but not consistently the complete human RUSAT phenotype. (germeshausen2018mecomassociatedsyndromea pages 7-7)
- **Junbo mouse:** an Evi1 p.Asn782Ile-equivalent allele predisposes to otitis media and hearing loss; it is useful for auditory biology but does not prove that human RUSAT hearing loss has the same mechanism. (niihori2015mutationsinmecom pages 3-5)
- **Cellular assays:** transfected-cell ChIP-qPCR and AP-1/TGF-β reporters demonstrate variant-dependent DNA-binding and transcriptional abnormalities. Patient lymphoblastoid cells carrying p.Glu758Lys showed modestly reduced MECOM protein in three experiments (P=0.041 and 0.035 versus controls). Limitations include nonphysiologic expression and use of cells that are not primary HSPCs or developing limb tissue. (niihori2015mutationsinmecom pages 3-5, walne2018expandingthephenotypic pages 14-16)
- **Patient hematopoietic samples:** reduced CD34-high/CD38-low progenitors, retained low MPL expression, elevated thrombopoietin, marrow hypocellularity, and absent megakaryocytes provide direct human evidence of progenitor and megakaryocyte failure. (germeshausen2018mecomassociatedsyndromea pages 5-5)

No validated disease-specific zebrafish, rat, Drosophila, organoid, or iPSC model was identified in the retrieved evidence.

## Recent developments and expert interpretation

The most important 2023–2024 advance is recognition that apparent “nonpenetrance” may reflect **somatic genetic rescue**, while older patients can develop **clonal hematopoiesis, multilineage dysplasia, and MDS**. In 15 newly described cases, seven had spontaneous resolution, attenuation, or late onset; four of six evaluable mild/resolving cases showed copy-neutral 3q loss of heterozygosity encompassing MECOM. This finding changes diagnostic practice: blood can be a misleading germline sample, and longitudinal marrow/genomic surveillance deserves consideration. (venugopal2024unravelingfacetsof pages 2-3)

A second advance is continued expansion of the variant spectrum and evidence that trio WES is clinically useful when congenital thrombocytopenia and skeletal findings coexist. The 2024 p.Arg762Lys case also documents normalization of counts after matched-unrelated HSCT. (huang2024anovelmissense pages 1-3, huang2024anovelmissense pages 3-5)

Authoritative interpretation favors **“MECOM-associated syndrome”** over restricting diagnosis to RUSAT2: neither RUS nor amegakaryocytic thrombocytopenia is obligatory, and disease can present as isolated orthopedic abnormality, isolated marrow failure, multisystem developmental disease, or late-onset cytopenia. (germeshausen2018mecomassociatedsyndromea pages 9-9, germeshausen2018mecomassociatedsyndromea pages 2-2)

## Key primary sources

1. Thompson AA, Nguyen LT. *Amegakaryocytic thrombocytopenia and radio-ulnar synostosis are associated with HOXA11 mutation.* **Nature Genetics.** 1 December 2000. PMID: **11101832**. https://doi.org/10.1038/82511
2. Niihori T, et al. *Mutations in MECOM, Encoding Oncoprotein EVI1, Cause Radioulnar Synostosis with Amegakaryocytic Thrombocytopenia.* **American Journal of Human Genetics.** 3 December 2015;97:848–854. PMID: **26581901**. https://doi.org/10.1016/j.ajhg.2015.10.010 (niihori2015mutationsinmecom pages 1-2)
3. Germeshausen M, et al. *MECOM-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia.* **Blood Advances.** March 2018;2:586–596. PMID: **29540340**. https://doi.org/10.1182/bloodadvances.2018016501 (germeshausen2018mecomassociatedsyndromea pages 1-2)
4. Walne AJ, et al. *Expanding the phenotypic and genetic spectrum of radioulnar synostosis associated hematological disease.* **Haematologica.** July 2018;103:e284–e287. PMID: **29519864**. https://doi.org/10.3324/haematol.2017.183855 (walne2018expandingthephenotypic pages 1-5)
5. Huang D, et al. *A novel missense mutation in the MECOM gene in a Chinese boy with radioulnar synostosis with amegakaryocytic thrombocytopenia.* **BMC Pediatrics.** January 2024;24:62. https://doi.org/10.1186/s12887-024-04552-1 (huang2024anovelmissense pages 1-3)
6. Venugopal P, et al. *Unraveling facets of MECOM-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion.* **Blood Advances.** 9 July 2024;8:3437–3443. https://doi.org/10.1182/bloodadvances.2023012331 (venugopal2024unravelingfacetsof pages 1-2)

**Evidence limitations:** RUSAT is ultra-rare; most statistics pool heterogeneous MECOM genotypes and ascertainment pathways. Frequencies are therefore descriptive of published cases, not unbiased penetrance estimates. HOXA11-specific natural-history and treatment data are particularly sparse, and most management recommendations are extrapolated from inherited marrow-failure and congenital-RUS practice.

References

1. (OpenTargets Search: Radioulnar synostosis with amegakaryocytic thrombocytopenia-HOXA11,MECOM): Open Targets Query (Radioulnar synostosis with amegakaryocytic thrombocytopenia-HOXA11,MECOM, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (walne2018expandingthephenotypic pages 1-5): Amanda Walne, Hemanth Tummala, Alicia Ellison, Shirleny Cardoso, Jasmin Sidhu, Gabriela Sciuccati, Tom Vulliamy, and Inderjeet Dokal. Expanding the phenotypic and genetic spectrum of radioulnar synostosis associated hematological disease. Haematologica, 103:e284-e287, Jul 2018. URL: https://doi.org/10.3324/haematol.2017.183855, doi:10.3324/haematol.2017.183855. This article has 34 citations.

3. (germeshausen2018mecomassociatedsyndromea pages 1-2): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

4. (niihori2015mutationsinmecom pages 3-5): Tetsuya Niihori, Meri Ouchi-Uchiyama, Yoji Sasahara, Takashi Kaneko, Yoshiko Hashii, Masahiro Irie, Atsushi Sato, Yuka Saito-Nanjo, Ryo Funayama, Takeshi Nagashima, Shin-ichi Inoue, Keiko Nakayama, Keiichi Ozono, Shigeo Kure, Yoichi Matsubara, Masue Imaizumi, and Yoko Aoki. Mutations in mecom, encoding oncoprotein evi1, cause radioulnar synostosis with amegakaryocytic thrombocytopenia. American journal of human genetics, 97 6:848-54, Dec 2015. URL: https://doi.org/10.1016/j.ajhg.2015.10.010, doi:10.1016/j.ajhg.2015.10.010. This article has 162 citations and is from a highest quality peer-reviewed journal.

5. (germeshausen2018mecomassociatedsyndromea pages 7-7): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

6. (germeshausen2018mecomassociatedsyndromea pages 4-5): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

7. (walne2018expandingthephenotypic pages 8-13): Amanda Walne, Hemanth Tummala, Alicia Ellison, Shirleny Cardoso, Jasmin Sidhu, Gabriela Sciuccati, Tom Vulliamy, and Inderjeet Dokal. Expanding the phenotypic and genetic spectrum of radioulnar synostosis associated hematological disease. Haematologica, 103:e284-e287, Jul 2018. URL: https://doi.org/10.3324/haematol.2017.183855, doi:10.3324/haematol.2017.183855. This article has 34 citations.

8. (niihori2015mutationsinmecom pages 1-2): Tetsuya Niihori, Meri Ouchi-Uchiyama, Yoji Sasahara, Takashi Kaneko, Yoshiko Hashii, Masahiro Irie, Atsushi Sato, Yuka Saito-Nanjo, Ryo Funayama, Takeshi Nagashima, Shin-ichi Inoue, Keiko Nakayama, Keiichi Ozono, Shigeo Kure, Yoichi Matsubara, Masue Imaizumi, and Yoko Aoki. Mutations in mecom, encoding oncoprotein evi1, cause radioulnar synostosis with amegakaryocytic thrombocytopenia. American journal of human genetics, 97 6:848-54, Dec 2015. URL: https://doi.org/10.1016/j.ajhg.2015.10.010, doi:10.1016/j.ajhg.2015.10.010. This article has 162 citations and is from a highest quality peer-reviewed journal.

9. (germeshausen2018mecomassociatedsyndromea pages 2-2): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

10. (venugopal2024unravelingfacetsof pages 1-2): Parvathy Venugopal, Peer Arts, Lucy C. Fox, Annet Simons, Devendra K. Hiwase, Peter G. Bardy, Annette Swift, David M. Ross, Lize F. D. van Vulpen, Arjan Buijs, Kelly L. Bolton, Bartlomiej Getta, Eliska Furlong, Tina Carter, Ingrid Krapels, Marlijn Hoeks, Adila Al Kindy, Farah Al Kindy, Sonja de Munnik, Pamela Evans, Mahalia S. B. Frank, Adam M. Bournazos, Sandra T. Cooper, Thuong Thi Ha, Matilda R. Jackson, Luis Arriola-Martinez, Kerry Phillips, Yvonne Brennan, Madhura Bakshi, Karen Ambler, Song Gao, Karin S. Kassahn, Rosalie Kenyon, Kevin Hung, Milena Babic, Alan McGovern, Lesley Rawlings, Cassandra Vakulin, Lucas Dejong, Rema Fathi, Simon McRae, Nicholas Myles, Dariusz Ladon, Marjolijn Jongmans, Roland P. Kuiper, Nicola K. Poplawski, Pasquale Barbaro, Piers Blombery, Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Unraveling facets of mecom-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion. Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012331, doi:10.1182/bloodadvances.2023012331. This article has 9 citations and is from a peer-reviewed journal.

11. (venugopal2024unravelingfacetsof pages 2-3): Parvathy Venugopal, Peer Arts, Lucy C. Fox, Annet Simons, Devendra K. Hiwase, Peter G. Bardy, Annette Swift, David M. Ross, Lize F. D. van Vulpen, Arjan Buijs, Kelly L. Bolton, Bartlomiej Getta, Eliska Furlong, Tina Carter, Ingrid Krapels, Marlijn Hoeks, Adila Al Kindy, Farah Al Kindy, Sonja de Munnik, Pamela Evans, Mahalia S. B. Frank, Adam M. Bournazos, Sandra T. Cooper, Thuong Thi Ha, Matilda R. Jackson, Luis Arriola-Martinez, Kerry Phillips, Yvonne Brennan, Madhura Bakshi, Karen Ambler, Song Gao, Karin S. Kassahn, Rosalie Kenyon, Kevin Hung, Milena Babic, Alan McGovern, Lesley Rawlings, Cassandra Vakulin, Lucas Dejong, Rema Fathi, Simon McRae, Nicholas Myles, Dariusz Ladon, Marjolijn Jongmans, Roland P. Kuiper, Nicola K. Poplawski, Pasquale Barbaro, Piers Blombery, Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Unraveling facets of mecom-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion. Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012331, doi:10.1182/bloodadvances.2023012331. This article has 9 citations and is from a peer-reviewed journal.

12. (huang2024anovelmissense pages 3-5): Duo-wen Huang, Mingyan Jiang, Yiping Zhu, Dong-jun Li, Xiaoxi Lu, and Ju Gao. A novel missense mutation in the mecom gene in a chinese boy with radioulnar synostosis with amegakaryocytic thrombocytopenia. BMC Pediatrics, Jan 2024. URL: https://doi.org/10.1186/s12887-024-04552-1, doi:10.1186/s12887-024-04552-1. This article has 2 citations and is from a peer-reviewed journal.

13. (venugopal2024unravelingfacetsof pages 3-4): Parvathy Venugopal, Peer Arts, Lucy C. Fox, Annet Simons, Devendra K. Hiwase, Peter G. Bardy, Annette Swift, David M. Ross, Lize F. D. van Vulpen, Arjan Buijs, Kelly L. Bolton, Bartlomiej Getta, Eliska Furlong, Tina Carter, Ingrid Krapels, Marlijn Hoeks, Adila Al Kindy, Farah Al Kindy, Sonja de Munnik, Pamela Evans, Mahalia S. B. Frank, Adam M. Bournazos, Sandra T. Cooper, Thuong Thi Ha, Matilda R. Jackson, Luis Arriola-Martinez, Kerry Phillips, Yvonne Brennan, Madhura Bakshi, Karen Ambler, Song Gao, Karin S. Kassahn, Rosalie Kenyon, Kevin Hung, Milena Babic, Alan McGovern, Lesley Rawlings, Cassandra Vakulin, Lucas Dejong, Rema Fathi, Simon McRae, Nicholas Myles, Dariusz Ladon, Marjolijn Jongmans, Roland P. Kuiper, Nicola K. Poplawski, Pasquale Barbaro, Piers Blombery, Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Unraveling facets of mecom-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion. Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012331, doi:10.1182/bloodadvances.2023012331. This article has 9 citations and is from a peer-reviewed journal.

14. (germeshausen2018mecomassociatedsyndromea pages 5-6): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

15. (venugopal2024unravelingfacetsof pages 6-7): Parvathy Venugopal, Peer Arts, Lucy C. Fox, Annet Simons, Devendra K. Hiwase, Peter G. Bardy, Annette Swift, David M. Ross, Lize F. D. van Vulpen, Arjan Buijs, Kelly L. Bolton, Bartlomiej Getta, Eliska Furlong, Tina Carter, Ingrid Krapels, Marlijn Hoeks, Adila Al Kindy, Farah Al Kindy, Sonja de Munnik, Pamela Evans, Mahalia S. B. Frank, Adam M. Bournazos, Sandra T. Cooper, Thuong Thi Ha, Matilda R. Jackson, Luis Arriola-Martinez, Kerry Phillips, Yvonne Brennan, Madhura Bakshi, Karen Ambler, Song Gao, Karin S. Kassahn, Rosalie Kenyon, Kevin Hung, Milena Babic, Alan McGovern, Lesley Rawlings, Cassandra Vakulin, Lucas Dejong, Rema Fathi, Simon McRae, Nicholas Myles, Dariusz Ladon, Marjolijn Jongmans, Roland P. Kuiper, Nicola K. Poplawski, Pasquale Barbaro, Piers Blombery, Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Unraveling facets of mecom-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion. Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012331, doi:10.1182/bloodadvances.2023012331. This article has 9 citations and is from a peer-reviewed journal.

16. (germeshausen2018mecomassociatedsyndromea pages 8-9): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

17. (germeshausen2018mecomassociatedsyndromea pages 5-5): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

18. (niihori2015mutationsinmecom pages 2-3): Tetsuya Niihori, Meri Ouchi-Uchiyama, Yoji Sasahara, Takashi Kaneko, Yoshiko Hashii, Masahiro Irie, Atsushi Sato, Yuka Saito-Nanjo, Ryo Funayama, Takeshi Nagashima, Shin-ichi Inoue, Keiko Nakayama, Keiichi Ozono, Shigeo Kure, Yoichi Matsubara, Masue Imaizumi, and Yoko Aoki. Mutations in mecom, encoding oncoprotein evi1, cause radioulnar synostosis with amegakaryocytic thrombocytopenia. American journal of human genetics, 97 6:848-54, Dec 2015. URL: https://doi.org/10.1016/j.ajhg.2015.10.010, doi:10.1016/j.ajhg.2015.10.010. This article has 162 citations and is from a highest quality peer-reviewed journal.

19. (germeshausen2018mecomassociatedsyndromea pages 9-9): Manuela Germeshausen, Phil Ancliff, Jaime Estrada, Markus Metzler, Eva Ponstingl, Horst Rütschle, Dirk Schwabe, Richard H. Scott, Sule Unal, Angela Wawer, Bernward Zeller, and Matthias Ballmaier. Mecom-associated syndrome: a heterogeneous inherited bone marrow failure syndrome with amegakaryocytic thrombocytopenia. Blood advances, 2 6:586-596, Mar 2018. URL: https://doi.org/10.1182/bloodadvances.2018016501, doi:10.1182/bloodadvances.2018016501. This article has 145 citations and is from a peer-reviewed journal.

20. (huang2024anovelmissense pages 1-3): Duo-wen Huang, Mingyan Jiang, Yiping Zhu, Dong-jun Li, Xiaoxi Lu, and Ju Gao. A novel missense mutation in the mecom gene in a chinese boy with radioulnar synostosis with amegakaryocytic thrombocytopenia. BMC Pediatrics, Jan 2024. URL: https://doi.org/10.1186/s12887-024-04552-1, doi:10.1186/s12887-024-04552-1. This article has 2 citations and is from a peer-reviewed journal.

21. (venugopal2024unravelingfacetsof pages 5-6): Parvathy Venugopal, Peer Arts, Lucy C. Fox, Annet Simons, Devendra K. Hiwase, Peter G. Bardy, Annette Swift, David M. Ross, Lize F. D. van Vulpen, Arjan Buijs, Kelly L. Bolton, Bartlomiej Getta, Eliska Furlong, Tina Carter, Ingrid Krapels, Marlijn Hoeks, Adila Al Kindy, Farah Al Kindy, Sonja de Munnik, Pamela Evans, Mahalia S. B. Frank, Adam M. Bournazos, Sandra T. Cooper, Thuong Thi Ha, Matilda R. Jackson, Luis Arriola-Martinez, Kerry Phillips, Yvonne Brennan, Madhura Bakshi, Karen Ambler, Song Gao, Karin S. Kassahn, Rosalie Kenyon, Kevin Hung, Milena Babic, Alan McGovern, Lesley Rawlings, Cassandra Vakulin, Lucas Dejong, Rema Fathi, Simon McRae, Nicholas Myles, Dariusz Ladon, Marjolijn Jongmans, Roland P. Kuiper, Nicola K. Poplawski, Pasquale Barbaro, Piers Blombery, Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Unraveling facets of mecom-associated syndrome: somatic genetic rescue, clonal hematopoiesis, and phenotype expansion. Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012331, doi:10.1182/bloodadvances.2023012331. This article has 9 citations and is from a peer-reviewed journal.

22. (walne2018expandingthephenotypic pages 14-16): Amanda Walne, Hemanth Tummala, Alicia Ellison, Shirleny Cardoso, Jasmin Sidhu, Gabriela Sciuccati, Tom Vulliamy, and Inderjeet Dokal. Expanding the phenotypic and genetic spectrum of radioulnar synostosis associated hematological disease. Haematologica, 103:e284-e287, Jul 2018. URL: https://doi.org/10.3324/haematol.2017.183855, doi:10.3324/haematol.2017.183855. This article has 34 citations.

## Artifacts

- [Edison artifact artifact-00](Radioulnar_Synostosis_with_Amegakaryocytic_Thrombocytopenia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `OMIM`.

3 of 6 terms resolved to a current term; the rest could not be looked up either way.