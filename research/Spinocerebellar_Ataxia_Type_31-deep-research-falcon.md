---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T13:16:09.586252'
end_time: '2026-09-02T13:24:20.370011'
duration_seconds: 490.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia Type 31
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 38
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  obsolete_terms:
  - term_id: GO:0051603
    ontology_label: obsolete proteolysis involved in protein catabolic process
    replaced_by: GO:0030163
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spinocerebellar_Ataxia_Type_31-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 31
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 31** covering all of the
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
- **Disease Name:** Spinocerebellar Ataxia Type 31
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 31** covering all of the
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


# Spinocerebellar Ataxia Type 31 (SCA31): Disease Characteristics Report

## Executive summary

Spinocerebellar ataxia type 31 (SCA31) is a rare, late-onset, slowly progressive, autosomal-dominant cerebellar neurodegenerative disorder caused by a complex pentanucleotide-repeat insertion at chromosome 16q22.1 in an intronic region shared by **BEAN1** and **TK2**. The disease-associated element is approximately 2.5–3.8 kb and contains `(TGGAA)n`, `(TAGAA)n`, `(TAAAA)n`, and `(TAAAATAGAA)n`; among these, `(TGGAA)n` is the motif consistently associated with pathogenicity. SCA31 has a pronounced Japanese founder effect and is essentially absent from most non-Japanese populations. Clinically, it is usually a relatively “pure” cerebellar syndrome beginning near 60 years of age, with gait/truncal and limb ataxia and dysarthria. Human pathology and experimental data support toxic gain-of-function by brain-expressed `(UGGAA)n` RNA, nuclear RNA foci, altered RNA-binding-protein homeostasis, repeat-associated translation of poly-WNGME pentapeptide protein, and selective Purkinje-cell injury. No disease-modifying treatment has been established; current care is supportive, while toxic-RNA-binding compounds and manipulation of RNA chaperones remain preclinical concepts. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 7-9)

The following table provides a compact knowledge-base representation.

| Domain | Key findings | Quantitative / implementation details | Suggested ontology terms | Evidence |
|---|---|---|---|---|
| Identity / identifiers | Spinocerebellar ataxia type 31 (SCA31), a disease-level aggregated Mendelian disorder; one of the most common autosomal-dominant cerebellar ataxias in Japan; also described as a pure cerebellar ataxia | MONDO:0007296; common synonyms: SCA31, spinocerebellar ataxia 31; other identifiers not firmly established from available context | MONDO:0007296 | (OpenTargets Search: spinocerebellar ataxia type 31-BEAN1,TK2, ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2) |
| Inheritance | Autosomal dominant; strong founder effect in Japan; age-dependent expression is likely, but formal penetrance estimates are not established in the available context | Founder disease; essentially absent in most non-Japanese populations except reported Japanese diaspora cases; anticipation not established from available context | HP:0000006 (Autosomal dominant inheritance) | (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7) |
| Causal lesion | Pathogenic lesion is a 2.5-3.8 kb complex pentanucleotide repeat insertion in the shared intronic region of BEAN1 and TK2 at 16q22.1; (TGGAA)n is the disease-segregating pathogenic motif | Repeat composition includes (TGGAA)n, (TAGAA)n, (TAAAA)n, and (TAAAATAGAA)n; controls may carry nonpathogenic short (TAAAA)8-20 tracts; healthy controls rarely have insertions lacking TGGAA (~0.23%) | Gene: BEAN1, TK2; SO conceptually: intronic repeat expansion / short tandem repeat expansion | (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9) |
| Phenotype / onset | Late-onset, slowly progressive cerebellar ataxia with truncal and limb ataxia, dysarthria/cerebellar speech, reduced muscle tone; usually without brainstem involvement; occasional reported parkinsonism or blepharospasm | Mean onset about 58.5-63.8 years; considered among the latest-onset SCAs | HP:0001251 (Ataxia); HP:0002060 (Dysarthria); HP:0001252 (Hypotonia); HP:0002313 (Cerebellar atrophy) | (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7) |
| Progression / prognosis | Chronic lifelong course with slow progression; quantitative natural history available; disability accumulates gradually | SARA progression ~0.8 points/year; wheelchair dependence around 79.4 ± 1.7 years; death around 88.5 ± 0.7 years in reported cohort summaries | HP:0001251; NCIT:C99568 (Wheelchair dependence, approximate mapping not guaranteed) | (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 5-7) |
| Anatomy / pathology | Primary pathology is cerebellar, especially Purkinje-cell-predominant degeneration and cerebellar cortical atrophy; upper vermis atrophy is typical on MRI | Purkinje-cell nuclear RNA foci seen in ~30% of patient Purkinje cells; foci ~0.2-1.8 µm; pathology includes Purkinje cell loss, shrinkage, halo-like amorphous material, calbindin-positive somatic sprouts, synaptophysin-positive terminals, ubiquitin-positive degradation granules, Golgi fragmentation | UBERON:0002037 (cerebellum); UBERON:0002245 (cerebellar vermis); CL:0000121 (Purkinje cell); GO:0005730 (nucleolus not established), GO:0005634 (nucleus) | (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 5-7) |
| Mechanism | Repeat is bidirectionally transcribed; brain-specific BEAN1-derived (UGGAA)n RNA forms toxic secondary structures and RNA foci in Purkinje-cell nuclei; UGGAA RNA binds TDP-43, FUS, hnRNPA2/B1; toxicity is likely mediated by RNA toxicity plus repeat-associated translation to pentapeptide repeat protein | TDP-43 acts as an RNA chaperone in fly/in vitro systems and suppresses toxicity; UGGAA translation yields poly-WNGME pentapeptide repeat protein detected in patient Purkinje cells; some mechanistic steps remain inferred rather than fully proven in humans | GO:0008380 (RNA splicing, broad RBP relevance); GO:0003723 (RNA binding); GO:0016070 (RNA metabolic process); GO:0034644 (cellular response to UV? not applicable); GO:0031047 (gene silencing by RNA not established) | (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 9-11) |
| Diagnostics | Real-world diagnosis relies on targeted repeat-expansion testing in suspected hereditary ataxia; Southern blot and PCR-based methods are described; long-read sequencing and WGS-based repeat detection are emerging adjuncts for complex repeat loci | Historical SCA31 mapping used Southern blot, BAC tiling/shotgun sequencing, PCR/Sanger; 2014 hybrid short+long read sequencing resolved 2.3-3.1 kb SCA31 repeats in 11 samples; current general ataxia RE practice uses repeat-primed PCR or Southern blot, with WGS pipelines increasingly feasible | NCIT:C120299 (Genetic Testing); NCIT:C71484 (Magnetic Resonance Imaging); HP:0001272 (Cerebellar atrophy on neuroimaging, approximate phenotype mapping) | (ishikawa2023spinocerebellarataxiatype pages 1-2, ishikawa2023spinocerebellarataxiatype pages 2-3) |
| Treatment / trials | No disease-modifying therapy is established in available SCA31-specific context; management is supportive and rehabilitative; experimental preclinical strategies target toxic RNA structure/RBP balance | Preclinical naphthyridine carbamate dimer (NCD) binds UGGAA repeats and reduced foci/degeneration in fly systems; trial search found no clearly relevant SCA31-specific interventional trial | NCIT:C15413 (Physical Therapy); NCIT:C15697 (Occupational Therapy); NCIT:C94533 (Speech Therapy); experimental small-molecule therapy not established | (zhang2022mechanisticandtherapeutic pages 9-11) |
| Epidemiology | Strongly enriched in Japan; reported as the third most frequent SCA in Japan; rare in neighboring Asian populations and absent from large European cohorts; Brazilian cases linked to Japanese ancestry support founder effect | One review notes 99.7% of controls carry short 8-20 TAAAA repeats at the locus; disease largely population-restricted | MONDO:0007296; HP:0012823 (Founder effect, no HPO term standardly used for disease, use narrative) | (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7) |
| Environmental / protective factors | No established environmental, infectious, lifestyle, or protective factors were identified in the available SCA31-specific evidence; gene-environment interaction not established | Not established / unknown | None reliably assignable | (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2) |
| Models | Drosophila transgenic models expressing expanded UGGAA/TGGAA repeats recapitulate RNA foci, degeneration, locomotor defects, and shortened lifespan; used for modifier and small-molecule testing | Toxicity is length- and expression-level-dependent; TDP-43/FUS/hnRNPA2B1 co-expression ameliorates phenotypes; poly-WNGME burden correlates with severity in flies | NCBITaxon:7227 (Drosophila melanogaster); CL terms not directly applicable to fly eye models; GO:0003723 (RNA binding) | (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 9-11) |


*Table: This table condenses the highest-confidence, knowledge-base-ready facts on Spinocerebellar Ataxia Type 31, including its causal repeat expansion, core phenotype, mechanistic evidence, diagnostics, and model systems. It also flags domains where the current evidence is limited or not established.*

## 1. Disease information

### Definition and classification

SCA31 is a **Mendelian autosomal-dominant repeat-expansion disorder** and neurodegenerative cerebellar ataxia. Its cardinal manifestation is progressive cerebellar ataxia, generally without the prominent brainstem, pyramidal, peripheral-neuropathic, cognitive, or systemic manifestations found in many multisystem SCAs. The source material summarized here is principally **aggregated disease-level evidence** from pedigrees, clinical cohorts, human postmortem tissue, and experimental models—not individual EHR records. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7)

### Identifiers and synonyms

- **MONDO:** **MONDO:0007296**.
- **Principal names:** spinocerebellar ataxia type 31; spinocerebellar ataxia 31; **SCA31**.
- **Historical/locus terminology:** chromosome 16q22.1-linked autosomal-dominant cerebellar ataxia; the phenotype was historically associated with “16q-ADCA.”
- **Disease-associated targets:** Open Targets links SCA31 to **BEAN1** (Ensembl ENSG00000166546) and, with substantially weaker association evidence, **TK2** (ENSG00000166548). The underlying literature records include PMIDs **17611710, 19878914, 22992774, 20301317**, and **35084690**. (OpenTargets Search: spinocerebellar ataxia type 31-BEAN1,TK2)
- **OMIM/Orphanet/MeSH and dedicated ICD codes:** not reliably established in the retrieved evidence. General coding systems may classify the condition under hereditary ataxia or spinocerebellar ataxia rather than a unique SCA31 code; these mappings should be verified directly against current releases before database ingestion.

A concise statement from the November 2023 disease review is: **“Spinocerebellar ataxia type 31 (SCA31) is one of the most common forms of autosomal-dominant cerebellar ataxia in Japan.”** DOI: [10.1038/s10038-022-01091-4](https://doi.org/10.1038/s10038-022-01091-4). (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The causal lesion is a **germline, heterozygous, complex intronic pentanucleotide-repeat expansion** at 16q22.1. It lies in an intron shared by oppositely transcribed **BEAN1** and **TK2**. Disease alleles are approximately 2.5–3.8 kb and contain several repeat motifs, but `(TGGAA)n` is the sequence that segregates with SCA31 and was not observed on control chromosomes in the foundational comparisons. Short `(TAAAA)8–20` alleles are common in unaffected Japanese controls. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2)

### Risk factors

- **Genetic:** inheritance of the disease-associated `(TGGAA)n`-containing expansion is the primary risk factor. Longer insertion length correlates inversely with age at onset, although repeat composition and technical measurement complexity limit simple repeat-count prediction. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9)
- **Family history:** an affected first-degree relative is a major clinical risk indicator under autosomal-dominant inheritance.
- **Population ancestry:** Japanese ancestry substantially raises prior probability because of a strong founder effect. Cases outside Japan have notably included people of Japanese descent, including Brazilian families. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7)
- **Age:** age is not an etiologic exposure, but clinical penetrance is strongly age-dependent because onset is usually in late adulthood.
- **Sex:** no reproducible sex-specific risk or sex-ratio difference was established in the retrieved studies.
- **Modifier genes:** TDP-43/**TARDBP**, **FUS**, and **HNRNPA2B1** modify toxicity experimentally, but they are not established human genetic modifier loci. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 9-11)

### Environmental and protective factors

No validated toxin, infection, diet, smoking pattern, alcohol exposure, occupational factor, medication, or other environmental exposure has been shown to cause or specifically modify SCA31. No protective human allele, dietary intervention, or lifestyle factor has been validated. Consequently, a specific SCA31 gene–environment interaction is **not established**. General avoidance of alcohol excess and cerebellotoxic medications may reduce superimposed ataxia but does not prevent the inherited disease.

## 3. Phenotypes

### Core phenotype

| Manifestation | Type and characteristics | Suggested HPO term |
|---|---|---|
| Gait/truncal ataxia | Core sign; late-onset and slowly progressive; progressively compromises balance and independent ambulation | **HP:0002066** Gait ataxia; **HP:0001251** Ataxia; **HP:0002078** Truncal ataxia |
| Limb ataxia/dysmetria | Common cerebellar sign, usually progressive | **HP:0002070** Limb ataxia; **HP:0001310** Dysmetria |
| Dysarthria/cerebellar speech | Common progressive sign affecting communication | **HP:0001260** Dysarthria / current HPO preferred cerebellar dysarthria mapping should be release-verified |
| Cerebellar atrophy | MRI and pathological abnormality, particularly cerebellar cortex/upper vermis; brainstem relatively spared | **HP:0001272** Cerebellar atrophy |
| Hypotonia/reduced tone | Reported in clinical descriptions; less defining than ataxia | **HP:0001252** Hypotonia |
| Parkinsonism | Uncommon/non-core; occasional L-DOPA-responsive cases reported | **HP:0001300** Parkinsonism |
| Blepharospasm | Uncommon/non-core | **HP:0000643** Blepharospasm |

Mean reported onset ranges from **58.5 ± 10.3 years** to **63.8 years**, making SCA31 one of the latest-onset SCAs. The course is chronic and progressive rather than episodic, relapsing, or remitting. Available reports do not supply robust percentage frequencies for every symptom; ataxia and dysarthria are core, whereas parkinsonism and blepharospasm are occasional. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7)

### Functional and quality-of-life effects

Progressive gait and balance impairment affect community mobility, falls risk, driving, self-care, and ultimately independent ambulation. Dysarthria impairs communication, while limb incoordination affects feeding, writing, dressing, and other fine-motor tasks. Wheelchair dependence was reported at a mean age of **79.4 ± 1.7 years**. No SCA31-specific EQ-5D, SF-36, PROMIS, or validated disease-specific quality-of-life estimates were identified. SARA is the principal quantitative neurological severity scale reported. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 5-7)

## 4. Genetic and molecular information

### Genes and variant class

- **BEAN1**—brain expressed associated with NEDD4 1; principal disease-linked gene/locus in Open Targets.
- **TK2**—thymidine kinase 2; shares the affected intronic interval and is transcribed in the opposite direction. This SCA31 mechanism is distinct from recessive coding-variant **TK2 deficiency**.
- **Variant type:** complex intronic tandem-repeat insertion/expansion; germline; heterozygous.
- **Functional class:** toxic gain of function at the RNA level, with an additional toxic repeat-associated translation product; not a conventional BEAN1 or TK2 coding loss-of-function allele. (OpenTargets Search: spinocerebellar ataxia type 31-BEAN1,TK2, ishikawa2023spinocerebellarataxiatype pages 2-3, zhang2022mechanisticandtherapeutic pages 7-9)

The repeat is bidirectionally transcribed. BEAN1 produces brain-specific `(UGGAA)n`-containing RNA, whereas the opposite TK2 direction produces `(UUCCA)n` RNA more broadly. The clinical and pathological restriction to the nervous system, together with BEAN1’s brain-restricted expression, supports the `(UGGAA)n` transcript as the dominant pathogenic species. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2)

### Classification, frequency, and structural features

The canonical expansion is pathogenic by segregation, population specificity, human pathology, and functional-model evidence. Conventional SNV-focused ACMG/AMP criteria are not sufficient by themselves for this complex repeat; laboratories should use repeat-expansion-specific validation and locus expertise. Approximately **99.7%** of controls in one summary carried short `(TAAAA)8–20` repeats, and control insertions lacking TGGAA were rare (approximately **0.23%**). Standard gnomAD SNV allele-frequency fields are not an adequate representation of this lesion. (zhang2022mechanisticandtherapeutic pages 7-9, ishikawa2023spinocerebellarataxiatype pages 2-3)

No established large deletion, translocation, inversion, aneuploidy, somatic mosaic mechanism, DNA-methylation signature, or chromatin biomarker specific to SCA31 was found. Somatic repeat instability is biologically plausible for repeat diseases but was not established as a clinical driver in the retrieved SCA31 evidence.

## 5. Environmental information

SCA31 is not infectious, zoonotic, toxic, radiation-induced, or lifestyle-caused. No infectious agent or environmental trigger is implicated. Alcohol, sedatives, anticonvulsants, and other cerebellar-toxic exposures can worsen balance nonspecifically and should be reviewed clinically, but they are not SCA31 causes. CTD-style disease–chemical causal relationships and SCA31-specific lifestyle-effect estimates were not identified.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline `(TGGAA)n`-containing complex repeat expansion in the shared **BEAN1/TK2** intron **leads to** bidirectional transcription of expanded noncoding repeat RNA at 16q22.1. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2019molecularmechanismsand pages 1-3)
2. Brain-specific BEAN1 transcription **results in** expanded `(UGGAA)n` RNA in cerebellar neurons, especially Purkinje cells. (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2)
3. `(UGGAA)n` RNA folds into abnormal hairpin-like structures with GGA loops **leading to** nuclear RNA-foci formation; this is demonstrated in human SCA31 Purkinje cells. (zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 9-11)
4. The structured RNA **leads to** binding and altered availability/activity of TDP-43, FUS, and hnRNPA2/B1; whether classical sequestration alone is sufficient for human disease remains incompletely demonstrated. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9)
5. **Branch A:** disturbed RNA–RNA-binding-protein equilibrium **results in** RNA-mediated cellular toxicity; fly rescue by RBP co-expression supports causality, but downstream human transcript targets remain insufficiently defined. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 9-11)
6. **Branch B:** repeat-associated non-AUG translation of `(UGGAA)n` **results in** poly-WNGME pentapeptide-repeat protein; this product is detected in patient Purkinje cells and correlates with toxicity in flies. (zhang2022mechanisticandtherapeutic pages 7-9)
7. RNA and translated-product toxicity **lead to** Golgi fragmentation, ubiquitin-positive degradation granules, abnormal somatic sprouts/synaptic remodeling, Purkinje-cell shrinkage and loss; the exact ordering of these downstream events is partly inferred. (zhang2022mechanisticandtherapeutic pages 5-7)
8. Progressive Purkinje-cell and cerebellar cortical degeneration **results in** cerebellar atrophy, impaired cerebellar output, gait/limb ataxia, and dysarthria. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7)

### Mechanistic detail and evidence strength

**Human evidence:** RNA foci occur in approximately **30%** of examined patient Purkinje cells and measure about **0.2–1.8 μm**. Poly-WNGME material has also been detected in affected Purkinje cells. Neuropathology shows Purkinje-cell loss and shrinkage, halo-like amorphous structures containing calbindin-positive somatic sprouts and synaptophysin-positive terminals, ubiquitin-positive granules, and Golgi fragmentation. (zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 5-7)

**Model evidence:** In Drosophila, `(TGGAA)80–100`/expanded `(UGGAA)n` expression causes nuclear and cytoplasmic foci, compound-eye degeneration, shortened lifespan, and progressive locomotor defects in a length- and expression-dependent fashion. Co-expression of TDP-43, FUS, or hnRNPA2/B1 reduces toxicity. TDP-43 appears to act as an **RNA chaperone**, remodeling abnormal UGGAA RNA rather than simply increasing its degradation, and also reduces pentapeptide-repeat synthesis. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 9-11)

**Pathways and profiling:** No well-validated primary Wnt, MAPK, mTOR, PI3K–AKT, metabolic, immune, or inflammatory pathway has been established for SCA31. Likewise, no mature single-cell, spatial-transcriptomic, patient proteomic, metabolomic, lipidomic, or integrated multi-omic signature was identified. The best-supported biology is repeat-RNA structure, RNA-binding-protein homeostasis, noncanonical translation, protein quality control, Golgi integrity, and neuronal degeneration.

**Suggested GO terms:** GO:0003723 RNA binding; GO:0016070 RNA metabolic process; GO:0006412 translation; GO:0006914 autophagy only if directly documented in a future dataset; GO:0008219 cell death; GO:0051603 proteolysis involved in cellular protein catabolic process; GO:0007005 mitochondrion organization is **not currently supported as a core SCA31 mechanism**. Suggested cell ontology: **CL:0000121 Purkinje cell**, with cerebellar granule neurons and glia not yet established as primary targets.

## 7. Anatomical structures affected

- **Organ/system:** central nervous system, principally cerebellum.
- **Regional localization:** cerebellar cortex and upper vermis; MRI generally shows cerebellar atrophy without substantial brainstem atrophy.
- **Cell:** Purkinje neurons are the best-established vulnerable population.
- **Subcellular compartments:** nucleus/RNA foci; cytoplasm for translated pentapeptide material; Golgi apparatus and protein-degradation compartments are pathologically altered.
- **Lateralization:** bilateral/diffuse rather than unilateral; no consistent asymmetry is established.

Suggested terms include **UBERON:0002037 cerebellum**, **UBERON:0002245 cerebellar vermis**, **CL:0000121 Purkinje cell**, **GO:0005634 nucleus**, **GO:0005794 Golgi apparatus**, and **GO:0005737 cytoplasm**. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 5-7)

## 8. Temporal development

Onset is insidious and typically late adult/geriatric, averaging roughly 59–64 years. The course is monophasic, chronic, lifelong, and slowly progressive, without spontaneous remission. A natural-history summary reports **SARA worsening of approximately 0.8 points/year**, wheelchair use near age 79, and death near age 88.5. These are cohort means rather than deterministic predictions for an individual. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 5-7)

Practical stages are: (1) subtle imbalance or dysarthria; (2) clinically evident gait and limb ataxia with retained ambulation; (3) assistive-device dependence; and (4) advanced mobility dependence. These are pragmatic clinical stages, not formally validated SCA31 staging criteria. The long presymptomatic period creates a theoretical intervention window for future allele- or RNA-directed therapies, but no biomarker-defined critical window is established.

## 9. Inheritance and population

SCA31 is autosomal dominant; each child of a heterozygous affected person has a **50% transmission risk**. Penetrance is likely strongly age-dependent, but a precise age-specific penetrance curve was not identified. Expressivity is variable, although the phenotype is usually relatively pure and slowly progressive. An inverse repeat-length/onset relationship exists. Robust genetic anticipation, germline mosaicism rates, de novo frequency, and carrier frequency have not been established. Consanguinity is not a causal factor for this dominant disorder. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9)

SCA31 is described as the **third most frequent SCA in Japan** in one review, but a reliable population prevalence per 100,000 and annual incidence were not available in the retrieved evidence. It is rare in neighboring Asian groups and absent from large European cohorts; Japanese-ancestry cases abroad reinforce a founder origin. No convincing male:female imbalance is known. (ishikawa2023spinocerebellarataxiatype pages 1-2, zhang2022mechanisticandtherapeutic pages 5-7)

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with late-onset, slowly progressive, predominantly cerebellar ataxia; a three-generation pedigree and Japanese ancestry increase suspicion. Examination should document gait, stance, limb coordination, speech, ocular motor function, tone, pyramidal/extrapyramidal signs, neuropathy, cognition, swallowing, and falls. Serial **SARA** scoring is suitable for monitoring.

Brain MRI typically demonstrates cerebellar—often upper vermian—atrophy with relative brainstem sparing. MRI supports localization and excludes acquired mimics but is not molecularly diagnostic. No validated blood, CSF, protein, metabolite, neurofilament, electrophysiological, or liquid-biopsy biomarker is specific to SCA31. Biopsy is not indicated for routine diagnosis. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2)

### Genetic testing strategy

1. Order a **targeted SCA31 repeat-expansion assay** when phenotype/ancestry suggests SCA31, or include it in a comprehensive repeat-expansion ataxia panel.
2. Use locus-specific PCR/fragment methods where technically validated; because the allele is large and compositionally complex, confirmatory **Southern blot**, long-range PCR, or validated long-read analysis may be required.
3. Standard WES generally performs poorly because the lesion is intronic and much larger than an exome read. A negative WES does **not** exclude SCA31.
4. Short-read WGS with dedicated repeat-expansion software is more useful than WES but may not fully resolve motif composition. Long-read sequencing can directly characterize complex alleles and interruptions.
5. CMA, karyotyping, FISH, and mitochondrial DNA testing are not first-line assays for the canonical lesion.

Historical discovery used Southern blotting, BAC tiling/shotgun sequencing, and PCR/Sanger analysis. A hybrid sequencing study resolved 2.3–3.1-kb SCA31 alleles at nucleotide resolution in 11 samples. More broadly, 2023 work characterizes repeat-primed PCR and Southern blot as current repeat-expansion diagnostic standards and identifies WGS pipelines as an increasingly practical first step. (ishikawa2023spinocerebellarataxiatype pages 1-2, ishikawa2023spinocerebellarataxiatype pages 2-3)

### Differential diagnosis

Important inherited differentials include SCA6 and other late-onset dominant “pure” cerebellar ataxias, SCA5, SCA26, SCA30, SCA36, RFC1-related CANVAS, and episodic ataxias. Acquired and sporadic mimics include multiple-system atrophy–cerebellar type, immune/paraneoplastic ataxia, alcohol or medication toxicity, nutritional deficiencies, thyroid disease, structural lesions, and degenerative idiopathic late-onset cerebellar ataxia. Molecular confirmation distinguishes SCA31 from phenotypically overlapping SCAs.

Cascade testing of adult relatives is appropriate after counseling. Predictive testing of asymptomatic adults should include informed consent and discussion of age-dependent onset, uncertain individual prognosis, psychological effects, insurance/employment issues where relevant, and reproductive choices. Testing asymptomatic minors is generally deferred for an adult-onset condition without proven preventive therapy.

## 11. Outcome and prognosis

SCA31 produces gradually accumulating neurological disability but appears compatible with survival into advanced age in reported cohorts. Mean wheelchair dependence near **79.4 years** and death near **88.5 years** suggest that many affected people retain substantial longevity, although these numbers should not be interpreted as controlled life-expectancy estimates. No validated 5- or 10-year survival rates, disease-specific mortality rates, or treatment-stratified survival data were identified. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 5-7)

Major morbidity consists of falls, impaired mobility and activities of daily living, communication difficulty, and advanced dependence. Dysphagia, aspiration, deconditioning, fractures, and social isolation should be monitored as general complications of progressive ataxia, although SCA31-specific rates are unavailable. Recovery of lost cerebellar neurons is not expected; rehabilitation can preserve function and compensate for deficits. Earlier onset/longer alleles and baseline severity may predict greater lifetime disability, but no validated multivariable prognostic calculator or molecular prognostic biomarker exists.

## 12. Treatment

### Current clinical management

There is no approved SCA31-specific disease-modifying pharmacotherapy, gene therapy, cell therapy, ASO, siRNA, or surgical treatment. Care is multidisciplinary:

- physical therapy for balance, gait, strength, aerobic conditioning, falls prevention, and mobility aids;
- occupational therapy and home-safety/adaptive-equipment assessment;
- speech-language therapy for dysarthria and swallowing assessment when indicated;
- nutrition support if intake or swallowing declines;
- management of mood, sleep, pain, spasticity, parkinsonism, or blepharospasm when present;
- avoidance of unnecessary sedating or cerebellotoxic drugs.

Suggested NCIt intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Genetic Counseling**, **Assistive Device**, and **Supportive Care**; exact NCIt identifiers should be release-verified before ingestion.

### Experimental strategies

- Enhancing or mimicking the RNA-chaperone actions of TDP-43, FUS, or hnRNPA2/B1 may reduce abnormal UGGAA structure and translation, but systemic manipulation of these pleiotropic proteins could itself be hazardous. (ishikawa2019molecularmechanismsand pages 1-3, ishikawa2023spinocerebellarataxiatype pages 1-2)
- **Naphthyridine carbamate dimer (NCD)** preferentially binds UGGAA repeats, reduces RNA foci and TDP-43 interaction, and ameliorates fly-eye degeneration. This remains preclinical and has no established human response rate or safety profile. (zhang2022mechanisticandtherapeutic pages 9-11)
- Allele-selective ASOs, RNA degradation, inhibition of repeat-associated translation, and gene editing are rational future approaches but were not demonstrated clinically in the retrieved SCA31 literature.

The clinical-trial search produced no clearly SCA31-specific interventional trial. Trials for recessive **TK2 deficiency** are mechanistically unrelated and must not be misclassified as SCA31 trials.

## 13. Prevention

There is no vaccine, medication, lifestyle intervention, environmental remediation, or population screening program that prevents the expansion carrier state.

- **Primary prevention:** reproductive genetic counseling; where desired and legally available, preimplantation genetic testing or prenatal diagnosis after the familial expansion has been molecularly defined.
- **Secondary prevention:** cascade/predictive testing in consenting adult relatives and neurological surveillance; this may shorten diagnostic delay but has not been shown to prevent onset.
- **Tertiary prevention:** falls prevention, exercise and rehabilitation, swallowing surveillance, mobility aids, home modification, and management of complications.
- **Newborn screening:** not indicated because of late onset, rarity, population restriction, and absence of proven presymptomatic treatment.

## 14. Other species and natural disease

No naturally occurring SCA31-equivalent disease was identified in companion animals, livestock, or wildlife. The disorder has no infectious transmission or zoonotic potential. Although **BEAN1** and **TK2** orthologs occur across vertebrates, the pathogenic human repeat configuration and Japanese founder haplotype are the relevant disease features. Species-level NCBI Gene IDs and VBO breed terms were not established in the retrieved material.

## 15. Model organisms

The best-developed model is transgenic **Drosophila melanogaster** (**NCBI Taxonomy 7227**) expressing expanded TGGAA/UGGAA repeats. It recapitulates RNA foci, repeat-length/expression-dependent degeneration, locomotor decline, reduced lifespan, and poly-WNGME production. It has enabled genetic modifier experiments with TDP-43, FUS, and hnRNPA2/B1 and testing of NCD. (ishikawa2019molecularmechanismsand pages 1-3, zhang2022mechanisticandtherapeutic pages 7-9, zhang2022mechanisticandtherapeutic pages 9-11)

Limitations are substantial: fly compound-eye degeneration is not human cerebellar ataxia; transgene overexpression may exceed endogenous levels; repeat context and aging differ from the native human locus; and fly rescue does not establish human efficacy or safety. No well-validated knock-in mouse, rat, zebrafish, patient iPSC-derived Purkinje-cell, cerebellar organoid, or naturally occurring animal model was identified in the retrieved evidence.

## Recent developments and evidence gaps

The key recent disease-focused source is Ishikawa’s **November 2023** review, which consolidates the Japanese founder genetics, brain-specific bidirectional transcription, Purkinje-cell RNA foci, and RNA-chaperone model ([DOI 10.1038/s10038-022-01091-4](https://doi.org/10.1038/s10038-022-01091-4)). Its abstract states that the complex repeat **“lies in an intronic segment shared by two genes, BEAN1 … and TK2 … transcribed in mutually opposite directions”** and that `(UGGAA)n` forms **“abnormal RNA structures, called RNA foci, in cerebellar Purkinje cell nuclei.”** (ishikawa2023spinocerebellarataxiatype pages 2-3, ishikawa2023spinocerebellarataxiatype pages 1-2)

The most relevant 2023–2024 field-wide developments are improved WGS repeat-detection pipelines, increasing clinical use of long-read sequencing for large complex expansions, and continued use of CRISPR-enabled Drosophila models for repeat-disease mechanism and therapeutic screening. These advances improve SCA31 diagnosis and model design but have not yet produced a human disease-modifying therapy.

Critical gaps include precise population prevalence and penetrance, prospective modern natural-history cohorts, validated fluid/imaging biomarkers, native-locus mammalian and human iPSC models, cell-type-resolved omics, direct quantification of RNA versus poly-WNGME contributions in humans, and SCA31-specific interventional trials. Claims about immune activation, mitochondrial dysfunction, epigenetic silencing, environmental modifiers, and systemic disease should therefore be recorded as **not established**, rather than inferred from other repeat-expansion ataxias.

References

1. (ishikawa2023spinocerebellarataxiatype pages 2-3): Kinya Ishikawa. Spinocerebellar ataxia type 31 (sca31). Journal of Human Genetics, 68:153-156, Nov 2023. URL: https://doi.org/10.1038/s10038-022-01091-4, doi:10.1038/s10038-022-01091-4. This article has 15 citations and is from a peer-reviewed journal.

2. (ishikawa2019molecularmechanismsand pages 1-3): Kinya Ishikawa and Yoshitaka Nagai. Molecular mechanisms and future therapeutics for spinocerebellar ataxia type 31 (sca31). Neurotherapeutics, 16:1106-1114, Oct 2019. URL: https://doi.org/10.1007/s13311-019-00804-6, doi:10.1007/s13311-019-00804-6. This article has 24 citations and is from a peer-reviewed journal.

3. (ishikawa2023spinocerebellarataxiatype pages 1-2): Kinya Ishikawa. Spinocerebellar ataxia type 31 (sca31). Journal of Human Genetics, 68:153-156, Nov 2023. URL: https://doi.org/10.1038/s10038-022-01091-4, doi:10.1038/s10038-022-01091-4. This article has 15 citations and is from a peer-reviewed journal.

4. (zhang2022mechanisticandtherapeutic pages 7-9): Nan Zhang and Tetsuo Ashizawa. Mechanistic and therapeutic insights into ataxic disorders with pentanucleotide expansions. May 2022. URL: https://doi.org/10.3390/cells11091567, doi:10.3390/cells11091567. This article has 15 citations.

5. (OpenTargets Search: spinocerebellar ataxia type 31-BEAN1,TK2): Open Targets Query (spinocerebellar ataxia type 31-BEAN1,TK2, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (zhang2022mechanisticandtherapeutic pages 5-7): Nan Zhang and Tetsuo Ashizawa. Mechanistic and therapeutic insights into ataxic disorders with pentanucleotide expansions. May 2022. URL: https://doi.org/10.3390/cells11091567, doi:10.3390/cells11091567. This article has 15 citations.

7. (zhang2022mechanisticandtherapeutic pages 9-11): Nan Zhang and Tetsuo Ashizawa. Mechanistic and therapeutic insights into ataxic disorders with pentanucleotide expansions. May 2022. URL: https://doi.org/10.3390/cells11091567, doi:10.3390/cells11091567. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_Type_31-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051603` (obsolete proteolysis involved in protein catabolic process) (1 mention) - replaced by `GO:0030163`

38 of 39 terms resolved to a current term; the rest could not be looked up either way.