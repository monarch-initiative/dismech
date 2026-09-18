---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T20:28:22.725749'
end_time: '2026-09-03T20:43:15.477642'
duration_seconds: 892.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability X-linked 102
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Intellectual_Disability_X-linked_102-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability X-linked 102
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability X-linked 102** covering all of the
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
- **Disease Name:** Intellectual Disability X-linked 102
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability X-linked 102** covering all of the
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


# Intellectual Disability, X-linked 102 (DDX3X-related neurodevelopmental disorder)

## Executive summary and scope

**Intellectual Disability, X-linked 102 (MRX102)** is the historical OMIM name for **DDX3X-related neurodevelopmental disorder (DDX3X syndrome)**, an early-onset Mendelian neurodevelopmental condition caused principally by pathogenic germline variants in **DDX3X**, which encodes an ATP-dependent DEAD-box RNA helicase. It predominantly affects females through de novo heterozygous variants; viable affected males usually carry missense or splice-altering alleles with residual function. The phenotype combines developmental/intellectual disability, severe speech-language impairment, motor and tone abnormalities, behavioral disorders, and variably abnormal brain development. DDX3X variants account for approximately **1–3% of otherwise unexplained intellectual disability in females**, making this an individually rare but comparatively frequent monogenic cause of female ID. This percentage is a diagnostic-cohort fraction, not population prevalence. (lennox2020pathogenicddx3xmutations pages 1-3, dai2022expansionofclinical pages 4-5)

The strongest mechanistic model is disruption of RNA unwinding and translational control in neural progenitors, followed by altered cell-cycle dynamics, neurogenesis and neuronal migration. Severe missense alleles may additionally form abnormal RNA–protein granules and are strongly associated with polymicrogyria and more severe outcomes. No approved disease-modifying treatment or interventional DDX3X trial was identified; current practice is molecular diagnosis, multidisciplinary surveillance, early developmental therapy, communication support, and symptom-directed treatment. (lennox2020pathogenicddx3xmutations pages 1-3, NCT03718910 chunk 1)

The following table provides a knowledge-base-oriented synopsis.

| Domain | Key facts | Quantitative evidence | Suggested ontology terms | Evidence type/key source |
|---|---|---|---|---|
| Identity | Intellectual Disability, X-linked 102 is the historical label for **DDX3X-related neurodevelopmental disorder**; synonyms include **DDX3X syndrome**, **MRX102**, and **X-linked intellectual disability–hypotonia–movement disorder syndrome**. | OMIM phenotype **300958**; MONDO **MONDO:0018709**. | MONDO:0018709; OMIM:300958 | Aggregated disease resources and foundational human genetics (lennox2020pathogenicddx3xmutations pages 1-3, OpenTargets Search: -DDX3X) |
| Causal gene | Caused by pathogenic germline variants in **DDX3X**, encoding DEAD-box helicase 3 X-linked, an ATP-dependent RNA helicase and regulator of RNA metabolism and translation. | DDX3X: Ensembl **ENSG00000215301**; foundational PMID **26235985**. | Suggested: HGNC gene **DDX3X**; GO RNA-helicase activity and RNA-metabolic-process terms | Human genetics plus biochemical/model evidence (lennox2020pathogenicddx3xmutations pages 1-3, lukin2024emergingxlinkedgenes pages 8-9, OpenTargets Search: -DDX3X) |
| Inheritance and sex effects | Usually an X-linked disorder caused by **de novo heterozygous** variants in females. Affected males generally carry hypomorphic missense or splice-altering variants; complete loss of function is presumed poorly tolerated or embryonically lethal in hemizygous males. DDX3X escapes X-chromosome inactivation, and skewing does not reliably prevent disease. | DDX3X variants account for approximately **1–3%** of unexplained female ID. In a combined male series, **27/30** had missense and **3/30** splice-site variants; no truncating variants were reported. | HP:0001417 X-linked inheritance; suggested: abnormal X-chromosome inactivation | Human cohorts, family studies, allele-specific expression (lennox2020pathogenicddx3xmutations pages 1-3, kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, sun2022casereportde pages 8-8) |
| Core neurodevelopmental phenotype | Developmental delay or intellectual disability is the defining feature; language, motor, and adaptive development are commonly impaired, with severity ranging from mild to profound. | Chinese cohort: **23/23 (100%)** had ID/DD. Prospective cohort: **80%** met ID criteria. Male cohort: all had DD and/or ID; first words occurred at **18 months–8 years**. | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0000750 Delayed speech and language development; HP:0001270 Motor delay | Human prospective and retrospective cohorts (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, dai2022expansionofclinical pages 4-5, hoye2022aberrantcorticaldevelopment pages 30-31) |
| Speech and communication | Expressive language is often disproportionately affected; some individuals remain minimally verbal or nonverbal. Early speech-language assessment and augmentative and alternative communication are clinically appropriate. | Published summaries estimate approximately **52%** of affected females remain nonverbal after age five; language was the most impaired developmental domain in one 23-person cohort. | HP:0001344 Severe expressive language delay; suggested: absent speech; NCIT supportive communication intervention | Human cohorts and clinical-care literature (dai2022expansionofclinical pages 4-5, stefaniak2022autisticlikebehaviorsassociated pages 6-8) |
| Autism, ADHD, behavior | ASD traits, ADHD, sensory-processing differences, anxiety, self-injury, stereotypies, and other behavioral difficulties occur variably. Anxiety and self-injurious behavior may be especially important clinical burdens. | Prospective cohort: ASD **60%**, ADHD **53%**. Chinese cohort: **13/17** exceeded an ASD-risk screening cutoff. Comparative study: **23** females with DDX3X variants had significantly higher anxiety and self-injury scores than 23 females with other genetic IDs. | HP:0000729 Autistic behavior; HP:0007018 Attention deficit hyperactivity disorder; HP:0100716 Self-injurious behavior; suggested: anxiety and sensory-processing abnormality | Prospective and comparative human behavioral studies (dai2022expansionofclinical pages 4-5, hoye2022aberrantcorticaldevelopment pages 30-31) |
| Tone, movement, and motor function | Hypotonia is common but hypertonia, spasticity, ataxia, dystonic or other movement abnormalities can occur. Motor limitations affect mobility, self-care, and participation. | Chinese cohort: tone abnormalities **17/23 (73.9%)**. Male cohort: motor delay **17/18**. Earlier pooled data reported ataxia in **7/53 (13.2%)**. | HP:0001252 Hypotonia; HP:0001276 Hypertonia; HP:0001251 Ataxia; HP:0100022 Abnormality of movement | Human cohorts and case series (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, scala2019threedenovo pages 5-6, dai2022expansionofclinical pages 4-5) |
| Feeding, growth, and systemic findings | Feeding difficulty, ophthalmologic abnormalities, scoliosis or joint laxity, dysmorphism, and occasional congenital anomalies are reported. Hypothyroidism was proposed as an expanded phenotype but requires replication. | Chinese cohort: feeding difficulty **13/23 (56.5%)**, ophthalmologic problems **11/23 (47.8%)**, hypothyroidism **6/23 (26.1%)**. | HP:0011968 Feeding difficulties; HP:0000478 Abnormality of the eye; HP:0002650 Scoliosis; HP:0000821 Hypothyroidism | Human cohort; some findings are cohort-specific (dai2022expansionofclinical pages 4-5) |
| Epilepsy and electrophysiology | Seizures occur in a minority, with heterogeneous electroclinical presentations; abnormal EEG can occur without clinical epilepsy. | Chinese cohort: seizures **6/23 (26.1%)**, abnormal EEG **9/23 (39.1%)**. Earlier pooled series: seizures **6/53 (11.3%)**. | HP:0001250 Seizure; HP:0002353 EEG abnormality | Human cohorts (scala2019threedenovo pages 5-6, dai2022expansionofclinical pages 4-5) |
| Neuroimaging | MRI can be normal or show polymicrogyria, corpus-callosum dysgenesis, ventriculomegaly, delayed myelination, cerebellar/brainstem anomalies, or reduced brain volume. Recurrent severe missense variants correlate strongly with polymicrogyria and worse outcomes. | Chinese cohort: structural MRI abnormalities **15/23 (65.2%)**. Earlier pooled series: abnormal MRI **16/53 (30.2%)**, callosal abnormality **7/53 (13.2%)**. PMG prevalence across reports approximately **7–12%**. | HP:0002126 Polymicrogyria; HP:0007370 Abnormality of the corpus callosum; HP:0002119 Ventriculomegaly; HP:0012448 Delayed myelination | Human imaging cohorts and genotype–phenotype study (lennox2020pathogenicddx3xmutations pages 1-3, edey2023x‐linkedneuronalmigration pages 9-10, scala2019threedenovo pages 5-6, dai2022expansionofclinical pages 4-5) |
| Pathogenic variants | Disease-associated variants include nonsense, frameshift, canonical and noncanonical splice, missense, in-frame deletion, insertion, and duplication alleles. Female truncating variants usually support haploinsufficiency; severe helicase-domain missense variants may exert dominant-negative or toxic effects through impaired RNA release and granule formation. Population allele frequencies are variant-specific and must be checked in current gnomAD/ClinVar records. | Largest mechanistic cohort included **107** affected individuals; a Chinese cohort found **22** deleterious de novo variants among **2,317** probands. | SO terms suggested by variant: missense_variant, frameshift_variant, stop_gained, splice_region_variant; ACMG P/LP/VUS | Human molecular cohorts plus functional assays (lennox2020pathogenicddx3xmutations pages 1-3, kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, moresco2021anovelde pages 4-6, dai2022expansionofclinical pages 4-5) |
| Mechanism | DDX3X dysfunction impairs ATP-dependent RNA unwinding, translation of structured transcripts, and RNA-protein-granule dynamics. This disrupts neural-progenitor cell-cycle timing, neurogenic divisions, neuron production and migration, producing abnormal cortical lamination or PMG and downstream cognitive, language, motor, and behavioral impairment. Wnt effects are established in earlier experiments; newer model evidence links DDX3X loss to impaired **CREBBP-mRNA stabilization and Notch signaling**. | Severe missense variants show the strongest human association with PMG and severe outcomes; quantitative molecular effects vary by allele/model. | GO:0006396 RNA processing; GO:0006412 translation; GO:0007049 cell cycle; GO:0022008 neurogenesis; GO:0001764 neuron migration; suggested Wnt- and Notch-signaling GO terms | Human genotype–phenotype correlation; mouse, cell, biochemical, ribosome-profiling, zebrafish and Xenopus evidence (lennox2020pathogenicddx3xmutations pages 1-3, edey2023x‐linkedneuronalmigration pages 9-10, lukin2024emergingxlinkedgenes pages 8-9, hoye2022aberrantcorticaldevelopment pages 30-31) |
| Cells, tissues, and compartments | The primary affected organ is the developing CNS, especially fetal cerebral cortex. Implicated cells include radial glia/neural stem and progenitor cells, migrating neurons, and cortical excitatory neurons. Relevant compartments include cytoplasmic ribonucleoprotein granules, ribosomes, nucleus, and cytoplasm. | Mouse haploinsufficiency produces reduced brain volume and abnormal cortical lamination; conditional loss reduces neurogenesis. | UBERON:0000955 brain; suggested cerebral cortex; CL:0000047 neuronal stem cell; CL:0000540 neuron; GO:0035770 ribonucleoprotein granule; suggested ribosome/nucleus/cytoplasm terms | Mouse and cellular models; anatomical inference from human MRI (lennox2020pathogenicddx3xmutations pages 1-3, boitnott2021developmentalandbehavioral pages 25-28, hoye2022aberrantcorticaldevelopment pages 30-31) |
| Diagnosis | Diagnosis requires a compatible neurodevelopmental phenotype plus a pathogenic/likely pathogenic germline DDX3X variant. Trio exome/genome sequencing is preferred for unexplained ID/DD because it establishes de novo status and detects broad differential diagnoses. A neurodevelopmental panel including DDX3X or single-gene sequencing with deletion/duplication analysis is also usable. CMA detects CNVs but usually misses single-nucleotide variants; karyotype, FISH, mtDNA and repeat-expansion testing are not targeted tests for this disorder. | No disease-specific biochemical biomarker. WES identified **22 female de novo variants** in a 2,317-proband cohort; male diagnoses may require cautious interpretation and functional evidence. | NCIT suggested: Genetic Testing, Whole Exome Sequencing, Whole Genome Sequencing, Chromosomal Microarray; HP phenotype terms for variant prioritization | Clinical sequencing cohorts and expert interpretation (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, dai2022expansionofclinical pages 4-5) |
| Clinical evaluation | Baseline evaluation should be multidisciplinary: developmental/cognitive and adaptive assessment; speech-language and AAC evaluation; neurologic examination; ASD/ADHD/anxiety and sensory assessment; feeding/growth, vision and hearing assessment; musculoskeletal review; EEG if seizure concern; MRI when neurologic signs, seizures, abnormal head growth, or significant motor findings warrant it. | NCT03718910 used a three-day neurologic, psychiatric, developmental, medical, EEG, visual-evoked-potential and eye-tracking battery in **15** participants. | NCIT suggested: Neurologic Examination, Developmental Assessment, Magnetic Resonance Imaging, Electroencephalography, Ophthalmologic Examination | Expert-care recommendations and observational implementation; individual schedules remain phenotype-driven (lukin2024emergingxlinkedgenes pages 8-9, NCT03718910 chunk 1) |
| Management | No approved disease-modifying therapy exists. Care is symptomatic and supportive: early developmental intervention; speech-language/AAC, occupational and physical therapy; behavioral and educational supports; feeding therapy/nutrition; standard antiseizure treatment; management of tone, movement, sleep, anxiety/ADHD, scoliosis, vision, hearing, and endocrine problems as clinically indicated. | No disorder-specific response-rate or comparative-treatment data. Case-level therapy reports cannot establish efficacy. | NCIT suggested: Supportive Care, Physical Therapy, Occupational Therapy, Speech Therapy, Behavioral Therapy, Anticonvulsant Therapy, Nutritional Support | Expert opinion and case-level implementation (lukin2024emergingxlinkedgenes pages 8-9, stefaniak2022autisticlikebehaviorsassociated pages 6-8) |
| Research and trials | Clinical research is currently centered on natural history, deep phenotyping, biomarkers and patient registries rather than interventional molecular therapy. | **NCT03718910**: completed observational study, **15** participants, May 23, 2018–June 1, 2020. **NCT01238250 (Simons Searchlight)**: recruiting umbrella observational registry, planned enrollment **100,000** across eligible genetic conditions. | NCIT suggested: Observational Study, Natural History Study, Patient Registry | ClinicalTrials.gov registry evidence (NCT03718910 chunk 1) |
| Prognosis and course | Onset is congenital/early childhood and the neurodevelopmental disability is generally lifelong. Severity and independence vary widely. Limited reports describe later motor decline in some individuals or males with hypomorphic alleles, but progression is not established as the typical course. | No disease-specific life-expectancy, survival, mortality, remission, or validated prognostic-biomarker estimates are available. | HP:0003593 Infantile onset or suggested early-childhood onset; suggested chronic course | Human cohorts and rare longitudinal observations; major evidence gaps remain (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, lennox2020pathogenicddx3xmutations pages 1-3) |
| Epidemiology | Ultra-rare Mendelian disorder found across ancestries; ascertainment is strongly female-biased because most recognized cases are de novo heterozygous females. No founder effect, endemic region, or reliable population prevalence/incidence has been established. | Approximately **1–3% of unexplained female ID**, not 1–3% of all females. Disease-specific carrier frequency is unavailable. | MONDO:0018709; HP:0001417 | Sequencing-cohort estimate, not population epidemiology (lennox2020pathogenicddx3xmutations pages 1-3, dai2022expansionofclinical pages 4-5) |
| Risk, protection, and environment | The causal risk is a pathogenic germline DDX3X variant. Variant class/location, residual activity, sex, DDX3Y compensation in males, and possibly X-inactivation modify expression. No validated environmental causal, protective, infectious, toxin, lifestyle, dietary, occupational, immune, or gene–environment factor is known. | No quantified environmental effect sizes or protective alleles reported. | Suggested: genetic modifier; X-chromosome inactivation; not applicable for infectious-agent ontology | Human genetics and model-based modifier evidence; explicit knowledge gap (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, hoye2022aberrantcorticaldevelopment pages 30-31, sun2022casereportde pages 8-8) |
| Prevention and counseling | The phenotype cannot be prevented after a causal de novo variant arises. Primary prevention consists of reproductive counseling and optional prenatal or preimplantation testing after the familial variant is known. Cascade testing is appropriate for inherited male-family alleles; parental testing also assesses recurrence risk, although low residual risk from germline mosaicism remains after an apparently de novo result. Tertiary prevention is early therapy and complication surveillance. | Exact germline-mosaicism and recurrence rates are unavailable; no newborn population screening or prophylactic medication is established. | NCIT suggested: Genetic Counseling, Prenatal Genetic Testing, Preimplantation Genetic Testing, Cascade Testing, Early Intervention | Standard Mendelian-genetics practice informed by de novo/inherited cohorts (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, moresco2021anovelde pages 4-6) |
| Models and comparative biology | Available experimental systems include Ddx3x haploinsufficient and neural conditional-knockout mice, zebrafish functional assays, Xenopus neural-crest models, and cultured neural progenitor/neuronal systems. Models reproduce neurogenesis, cortical-lamination, motor, behavioral, and brain-volume abnormalities but cannot capture the full human language and adaptive phenotype. No naturally occurring veterinary equivalent or zoonotic transmission is established. | Ddx3x+/− mice show developmental, sensory and motor delays, adult hyperactivity/anxiety-like behavior, cognitive/motor deficits and reduced brain volume. | NCBI Taxon suggested: Homo sapiens, Mus musculus, Danio rerio, Xenopus tropicalis; NCIT suggested: Animal Model, Cell Culture Model | Mouse, zebrafish, Xenopus and in-vitro evidence (boitnott2021developmentalandbehavioral pages 25-28, hoye2022aberrantcorticaldevelopment pages 30-31) |
| Explicit unavailable items | No validated metabolomic, lipidomic, circulating-protein, epigenomic or liquid-biopsy diagnostic signature; no established modifier gene, protective variant, pharmacogenomic rule, surgical treatment, gene/cell/RNA therapy, immunotherapy, or disease-specific prevention program. Somatic DDX3X cancer variants must not be conflated with germline DDX3X syndrome. | No approved targeted drug and no interventional DDX3X-syndrome trial identified in the searched evidence. | Ontology mapping not applicable until evidence exists | Negative database/registry finding and evidence-gap assessment (OpenTargets Search: -DDX3X, NCT03718910 chunk 1) |


*Table: Concise knowledge-base table integrating identifiers, genetics, phenotypes, mechanisms, diagnosis, management, research studies, ontology suggestions, and explicit evidence gaps for Intellectual Disability X-linked 102.*

## 1. Disease information

### Definition and identifiers

* **Preferred contemporary name:** DDX3X-related neurodevelopmental disorder.
* **Historical names:** Intellectual disability, X-linked 102; mental retardation, X-linked 102; MRX102; DDX3X syndrome; MRXSSB; X-linked intellectual disability–hypotonia–movement disorder syndrome.
* **OMIM phenotype:** **300958**.
* **MONDO:** **MONDO:0018709**, “X-linked intellectual disability-hypotonia-movement disorder syndrome.” Open Targets maps DDX3X to this entity and to intellectual disability, supported principally by the foundational human report PMID 26235985. (lukin2024emergingxlinkedgenes pages 8-9, OpenTargets Search: -DDX3X)
* **Gene:** **DDX3X**, approved name *DEAD-box helicase 3 X-linked*; Ensembl **ENSG00000215301**. (OpenTargets Search: -DDX3X)
* **Orphanet:** the retrieved mapping associated DDX3X with the broader Orphanet category **ORPHA:777, X-linked non-syndromic intellectual disability**, but this is less specific than MONDO:0018709/OMIM:300958 and should not replace the disease-specific label. (OpenTargets Search: -DDX3X)
* **ICD-10/ICD-11 and MeSH:** no unique DDX3X/MRX102 code was identified. Coding ordinarily uses the applicable generic intellectual-developmental-disorder, developmental-delay, autism, epilepsy, movement-disorder, or congenital-malformation code. MeSH likewise has broader concepts rather than a disease-specific heading.

This report synthesizes **aggregated disease-level resources, published cohorts and individual case reports**. It is not derived from a single patient’s EHR. Cohort estimates must not be interpreted as population-based frequencies because recruitment was generally through diagnostic sequencing or specialty clinics.

## 2. Etiology, risk, protection, and gene–environment interaction

The primary cause is a **germline pathogenic or likely pathogenic DDX3X variant**. In females, most established cases are sporadic de novo heterozygous variants. Reported classes include missense, nonsense, frameshift, canonical and noncanonical splice variants, in-frame deletions, insertions, and duplications. Female truncating variants generally support haploinsufficiency, whereas recurrent helicase-domain missense variants may have dominant-negative or toxic effects in addition to reduced helicase activity. (lennox2020pathogenicddx3xmutations pages 1-3, moresco2021anovelde pages 4-6, dai2022expansionofclinical pages 4-5)

Important genetic determinants of severity are variant class, location within the ATP-binding/helicase domains, residual protein activity, and sex. In the recent combined male series, **27/30 males had missense variants and 3/30 had splice-site variants; no truncating male variant was reported**, supporting poor viability of complete hemizygous loss of function. Recurrent male substitutions included p.Arg351Gln and p.Arg488Cys. Some variants remain incompletely classified and require functional evidence. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8)

DDX3X escapes X-chromosome inactivation. X-inactivation can modify dosage but is not reliably protective: one symptomatic female had extreme preferential inactivation of the mutant X, yet allele-specific expression remained approximately 70% normal and 30% mutant, insufficient to prevent disease. (sun2022casereportde pages 8-8)

No reproducible environmental, infectious, toxic, occupational, dietary, lifestyle, immune, or prenatal exposure causes have been established. No protective DDX3X allele, validated modifier gene, or preventive lifestyle exposure is known. Consequently, a disease-specific gene–environment interaction has not been demonstrated. Ordinary environmental and educational circumstances may affect functional attainment and quality of life, but they are not known causes of the molecular disorder.

## 3. Phenotypes

Clinical onset is congenital or in infancy, usually recognized through delayed milestones, hypotonia, feeding difficulty, or abnormal motor development. Frequencies vary by ascertainment and age.

* **Global developmental delay/intellectual disability:** defining and lifelong, ranging from mild to profound. All 23 participants in a Chinese cohort had ID/DD; in a prospectively assessed cohort, 80% met formal ID criteria. Suggested HPO: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**. (dai2022expansionofclinical pages 4-5, hoye2022aberrantcorticaldevelopment pages 30-31)
* **Speech-language disorder:** expressive language is often disproportionately impaired; first words in the recent male cohort occurred from 18 months to 8 years, median 24 months. Some affected individuals remain nonverbal. Suggested HPO: **HP:0000750 Delayed speech and language development**, severe expressive-language impairment/absent speech where applicable. Communication limitation substantially affects education, social participation, and autonomy. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, dai2022expansionofclinical pages 4-5)
* **Motor delay and abnormal tone:** motor delay occurred in 17/18 assessable males; tone abnormalities occurred in 17/23 (73.9%) in the Chinese cohort. Hypotonia is common, but hypertonia, spasticity, dystonia, ataxia, and other movement disorders occur. Suggested HPO: **HP:0001270 Motor delay**, **HP:0001252 Hypotonia**, **HP:0001276 Hypertonia**, **HP:0001251 Ataxia**. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, dai2022expansionofclinical pages 4-5)
* **Autism and ADHD:** prospective gold-standard assessment found ASD in 60% and ADHD in 53%; 13/17 assessed Chinese participants exceeded an ASD-risk screening threshold. Suggested HPO: **HP:0000729 Autistic behavior**, **HP:0007018 ADHD**. (dai2022expansionofclinical pages 4-5, hoye2022aberrantcorticaldevelopment pages 30-31)
* **Anxiety, self-injury and sensory abnormalities:** a 2023 comparative study of 23 affected females and 23 females with other genetic IDs found significantly greater anxiety and self-injurious behavior in the DDX3X group, although autism characteristics did not differ between groups. These problems can markedly affect family life, safety, schooling, and community participation. Suggested HPO: anxiety, **HP:0100716 Self-injurious behavior**, and abnormal sensory processing. (hoye2022aberrantcorticaldevelopment pages 30-31)
* **Feeding and growth:** feeding difficulties occurred in 13/23 (56.5%) in the Chinese cohort. Growth abnormalities and reduced subcutaneous fat occur variably. Suggested HPO: **HP:0011968 Feeding difficulties**. (dai2022expansionofclinical pages 4-5)
* **Ophthalmologic findings:** reported in 11/23 (47.8%) in one cohort; manifestations are heterogeneous. Suggested HPO: **HP:0000478 Abnormality of the eye**. (dai2022expansionofclinical pages 4-5)
* **Seizures/EEG:** seizures occurred in 6/23 (26.1%) and abnormal EEG in 9/23 (39.1%) in the Chinese cohort, versus seizures in 6/53 (11.3%) in an earlier pooled series. Suggested HPO: **HP:0001250 Seizure**, **HP:0002353 EEG abnormality**. (scala2019threedenovo pages 5-6, dai2022expansionofclinical pages 4-5)
* **Musculoskeletal findings:** scoliosis, joint laxity and gait or postural abnormalities occur variably. Suggested HPO: **HP:0002650 Scoliosis**, generalized joint hypermobility when present.
* **Endocrine:** hypothyroidism was observed in 6/23 (26.1%) in one Chinese cohort, but this expanded phenotype requires independent replication and should not yet be considered universal. Suggested HPO: **HP:0000821 Hypothyroidism**. (dai2022expansionofclinical pages 4-5)

Brain MRI may be normal or show polymicrogyria, corpus-callosum hypoplasia/agenesis, ventriculomegaly, delayed myelination, white-matter abnormalities, cerebellar or brainstem anomalies. Structural abnormalities occurred in 15/23 (65.2%) in the Chinese cohort, while an earlier pooled series found abnormal MRI in 16/53 (30.2%) and callosal abnormalities in 7/53 (13.2%). Across reports, polymicrogyria occurs in approximately 7–12%; among DDX3X-associated PMG cases, epilepsy and ID were reported in 42% and 68%, respectively. Suggested HPO: **HP:0002126 Polymicrogyria**, **HP:0007370 Abnormality of the corpus callosum**, **HP:0002119 Ventriculomegaly**, and delayed myelination. (edey2023x‐linkedneuronalmigration pages 9-10, scala2019threedenovo pages 5-6, dai2022expansionofclinical pages 4-5)

## 4. Genetic and molecular information

DDX3X is an X-linked, dosage-sensitive RNA-helicase gene. The 2015 foundational study established the association; its title and central conclusion were: **“Mutations in DDX3X Are a Common Cause of Unexplained Intellectual Disability with Gender-Specific Effects on Wnt Signaling.”** PMID **26235985**, published August 2015; DOI: https://doi.org/10.1016/j.ajhg.2015.07.004. (lukin2024emergingxlinkedgenes pages 8-9, hoye2022aberrantcorticaldevelopment pages 30-31)

The largest mechanistic clinical series included 107 affected individuals and demonstrated a strong relationship between recurrent dominant missense variants, polymicrogyria, and severe outcomes. Its abstract states: **“Severe DDX3X missense mutations profoundly disrupt RNA helicase activity and induce ectopic RNA-protein granules and aberrant translation in neural progenitors and neurons.”** PMID **32135084**, published May 6, 2020; DOI: https://doi.org/10.1016/j.neuron.2020.01.042. (lennox2020pathogenicddx3xmutations pages 1-3, lukin2024emergingxlinkedgenes pages 8-9)

A representative case carried de novo **c.625C>G (p.His209Asp)** immediately upstream of the ATP-binding domain and had bilateral frontal PMG, delayed myelination and a thin corpus callosum. This variant was absent from the mother and predicted deleterious, but lacked a direct functional assay; its molecular mechanism therefore remains inferred. (moresco2021anovelde pages 4-6)

Most well-established alleles are absent or extremely rare in population databases because of strong negative selection. Nevertheless, allele frequency and ClinVar classification must be checked **variant by variant** against the current transcript/build; no single population frequency applies to the disease. Germline—not somatic—origin defines this syndrome. Somatic DDX3X variants in malignancies are a separate biological context and must not be used as evidence of constitutional DDX3X syndrome.

No validated modifier gene is established. DDX3Y compensation in male developing cortex is supported experimentally but is not a conventional inherited modifier allele. No disease-specific methylation episignature or clinically validated epigenetic biomarker is established. Large DDX3X deletions or X-chromosome rearrangements can theoretically cause the phenotype, but ordinary cases are sequence-level or small indel variants; cytogenetic abnormalities are not the dominant mechanism.

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, smoking, alcohol, diet, exercise, occupational exposure, or infection causes DDX3X syndrome. These factors can influence general health and developmental support needs but are not known etiologic agents. No zoonotic or transmissible component exists.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A pathogenic germline **DDX3X** variant **leads to** reduced dosage or allele-specific dysfunction of an ATP-dependent RNA helicase.
2. Impaired helicase activity **leads to** defective RNA unwinding, RNA metabolism, translation of structured transcripts, and—particularly for severe missense alleles—abnormal RNA–protein granules.
3. These RNA/translation defects **lead to** altered neural-progenitor cell-cycle duration and neurogenic divisions; newer model work also links DDX3X loss to reduced stabilization of **CREBBP mRNA** and dysfunctional **Notch signaling**.
4. Altered progenitor behavior **leads to** depletion or imbalance of neural stem/progenitor pools and abnormal production of excitatory and inhibitory neurons.
5. Reduced neurogenesis plus impaired neuronal migration and cortical lamination **leads to** abnormal cerebral-cortex development; the severe-missense branch can result in polymicrogyria, while other branches produce callosal, ventricular, myelination, or brain-volume abnormalities.
6. Abnormal cortical circuitry and broader neurodevelopment **result in** intellectual, language, motor, behavioral, sensory and seizure phenotypes. The final circuit-to-symptom link is biologically compelling but partly inferred rather than directly demonstrated in humans.

DDX3X participates in transcriptional regulation, splicing, nuclear mRNA export, cytoplasmic translation and ribonucleoprotein-granule biology. Experimental evidence places it upstream of cortical neuronal generation, migration and differentiation. Wnt-related effects were reported in the foundational study; Xenopus work additionally connects DDX3-dependent translation of RAC1 to AKT–GSK3β signaling, β-catenin/Snai1 stability and neural-crest development. These pathways may help explain craniofacial findings but should not be assumed to mediate every neurological phenotype. (lennox2020pathogenicddx3xmutations pages 1-3, edey2023x‐linkedneuronalmigration pages 9-10, lukin2024emergingxlinkedgenes pages 8-9)

In mouse neural progenitors, Ddx3x loss changes cell-cycle dynamics and translation, reducing neurogenesis; complete female neural-progenitor loss can produce microcephaly, while heterozygous females and hemizygous males show reduced neuron generation without necessarily marked microcephaly. The 2024 PNAS study added evidence that Ddx3x deficiency reduces the neural-stem-cell pool and disrupts excitatory/inhibitory differentiation through CREBBP-mRNA stabilization and Notch signaling. These are model findings, not yet validated therapeutic targets in patients. (hoye2022aberrantcorticaldevelopment pages 30-31)

Suggested ontology annotations include **GO:0006396 RNA processing**, **GO:0006412 translation**, **GO:0007049 cell cycle**, **GO:0022008 neurogenesis**, **GO:0001764 neuron migration**, canonical Wnt signaling, Notch signaling, and RNA-helicase activity. Suggested cell terms include neural stem cell/neural progenitor, radial glial cell, migrating neuron, cortical glutamatergic neuron and inhibitory interneuron. Relevant compartments include cytoplasmic ribonucleoprotein granule, ribosome, nucleus and cytoplasm.

No reproducible disease-specific metabolomic, lipidomic, immune, inflammatory or proteomic signature has been established. Ribosome profiling and transcript-level analyses are research tools, not diagnostic biomarkers. Single-cell, spatial-transcriptomic and integrated human multi-omic disease maps remain limited.

## 7. Anatomical structures affected

The primary organ is the **brain**, particularly the developing cerebral cortex. Relevant suggested annotations are **UBERON:0000955 brain**, cerebral cortex, corpus callosum, cerebral white matter, lateral ventricle, cerebellum and brainstem. Human imaging implicates both hemispheres; no consistent lateralization is established. (lennox2020pathogenicddx3xmutations pages 1-3, scala2019threedenovo pages 5-6)

At tissue/cell level, cortical neural progenitors/radial glia, newly generated and migrating neurons, cortical projection neurons, and potentially excitatory/inhibitory neuronal balance are central. Ddx3x+/− mice exhibit reduced brain volume, disproportionate cortical and amygdala effects, cortical thinning and defective lamination. Suggested Cell Ontology terms include **CL:0000047 neural stem cell** and **CL:0000540 neuron**, supplemented by radial-glial and cortical-neuron terms. (boitnott2021developmentalandbehavioral pages 25-28)

Secondary systems may include ocular, gastrointestinal/feeding, musculoskeletal and, less consistently, endocrine or congenital cardiac structures. These are variable manifestations rather than evidence of generalized progressive organ degeneration.

## 8. Temporal development

The molecular lesion is present from conception and acts during embryonic/fetal neurodevelopment. Clinical recognition is typically in infancy or early childhood through chronic/insidious failure to meet milestones rather than an acute event. The condition is lifelong; there is no established staging system or remission pattern.

Most evidence supports a developmental encephalopathy with relatively stable core disability, although skills and behavior evolve with age and intervention. Rare reports describe later neurological or motor decline, particularly in some males with hypomorphic alleles, but progression is not established as the usual course. Critical intervention windows are early childhood language, motor, adaptive and social development; this is a clinical-developmental principle rather than proof that early treatment reverses the molecular lesion. Male diagnoses may be delayed: in the 2025 cohort, median age at variant identification was 8 years, range 9 months–47 years. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3)

## 9. Inheritance and population

The typical pattern is **X-linked dominant/de novo in females**, with sex-dependent viability and expression. Affected males can have de novo or maternally inherited hypomorphic alleles; mildly affected or apparently unaffected carrier females occur in such families. A proven p.Arg79Lys allele caused partial loss of function and mild-to-moderate ID with progressive spasticity in two brothers, illustrating residual-function inheritance. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8, sun2022casereportde pages 8-8)

Penetrance is high for clearly pathogenic de novo female variants but cannot be expressed as a precise universal percentage. Expressivity is markedly variable. Anticipation is not reported. Parental germline mosaicism is biologically possible after an apparently de novo result, but no robust disease-specific recurrence percentage is available. No established founder variant, consanguinity association, geographic concentration, ancestry-specific enrichment, or population carrier frequency is known.

No reliable prevalence or incidence per 100,000 exists. The best repeated statistic is **1–3% of unexplained female ID in sequencing cohorts**. Recent evidence indicates more than 1,000 females have reportedly been diagnosed worldwide, but this is an ascertainment count rather than epidemiology. The sex ratio is strongly female-biased among recognized cases because complete loss of function is poorly tolerated in males. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3, lennox2020pathogenicddx3xmutations pages 1-3)

## 10. Diagnostics

Diagnosis requires a compatible neurodevelopmental phenotype and a pathogenic/likely pathogenic **germline DDX3X variant** interpreted under ACMG/AMP criteria.

1. **Preferred approach:** trio exome or genome sequencing for unexplained DD/ID, particularly in a female with severe speech delay, tone/movement abnormalities, ASD features, or characteristic MRI findings. Trio analysis establishes de novo status and improves interpretation.
2. **Alternatives:** a comprehensive neurodevelopmental/ID panel containing DDX3X, or DDX3X sequencing with deletion/duplication analysis when clinical suspicion is high.
3. **CMA:** useful for the broad DD/ID differential and DDX3X-containing deletions but does not reliably detect single-nucleotide or small indel variants.
4. **Karyotype/FISH:** reserved for suspected large X-chromosomal rearrangements; not routine DDX3X tests.
5. **RNA studies:** potentially useful for noncanonical splice variants or unresolved VUSs, but not a standardized first-line assay.
6. **Not indicated specifically:** mitochondrial-DNA testing and repeat-expansion assays unless another diagnosis is suspected.

There is no disease-specific blood, urine, enzyme, metabolite, proteomic, epigenomic or liquid-biopsy biomarker. Baseline assessment should document development, cognition/adaptive function, speech and communication, neurologic status, tone and movement, behavior/ASD/ADHD/anxiety, feeding/growth, hearing, vision and musculoskeletal findings. EEG is symptom-driven; brain MRI is appropriate with seizures, abnormal neurologic findings, head-growth abnormalities or significant motor impairment.

Differential diagnoses include Rett/MECP2-related disorders, CDKL5 disorder, FOXG1 syndrome, CASK-related disorders, WDR45-related neurodegeneration, TUBA1A/tubulinopathies and other polymicrogyria genes, USP9X-related disorder, PCDH19 epilepsy, cerebral palsy and other monogenic neurodevelopmental conditions. A DDX3X case initially labeled cerebral palsy illustrates why a static motor phenotype plus unexplained ID should prompt genomic investigation. (moresco2021anovelde pages 4-6)

Computer-assisted facial phenotyping is emerging but is adjunctive: a 2024 benchmark found MRX102 among syndromes correctly ranked first by tested facial tools, yet such algorithms cannot establish diagnosis or replace molecular confirmation.

## 11. Outcome and prognosis

The principal morbidity is lifelong impairment of communication, learning, adaptive functioning, mobility and behavioral regulation. Functional outcomes range widely; variant type and brain malformation provide some prognostic information. Missense/in-frame-deletion groups have, on average, more severe language, motor and adaptive impairment than protein-truncating groups, and recurrent severe missense variants associated with PMG predict poorer outcomes. These are group trends, not deterministic individual predictions. (lennox2020pathogenicddx3xmutations pages 1-3, hoye2022aberrantcorticaldevelopment pages 30-31)

There are no validated 5- or 10-year survival rates, life-expectancy estimates, disease-specific mortality rates, quality-adjusted-life-year studies or prognostic blood biomarkers. Available data do not demonstrate a uniformly life-limiting disorder. Complications include epilepsy, feeding and nutritional difficulty, falls or mobility restriction, scoliosis, sleep and behavioral problems, and caregiver burden. Complete recovery is not expected, but developmental gains and improved participation can occur with therapy and accommodations.

## 12. Treatment and current implementation

No FDA/EMA-approved DDX3X-specific drug, gene therapy, cell therapy, RNA therapy, CRISPR treatment or targeted molecular therapy exists. No evidence supports pharmacologically inhibiting DDX3X in this germline haploinsufficiency disorder; oncology-directed DDX3X strategies are not transferable.

Current care is individualized and multidisciplinary:

* early developmental and special-education intervention;
* speech-language therapy and early augmentative/alternative communication for minimally verbal children;
* physical and occupational therapy for tone, coordination, gait, posture, fine-motor and sensory needs;
* feeding therapy and nutritional/gastroenterology support;
* standard antiseizure medication selected by seizure type;
* standard evidence-based management of ADHD, anxiety, sleep disturbance, irritability or self-injury;
* orthopedic/physiatric management of scoliosis, contracture or mobility limitations;
* vision, hearing and endocrine treatment when abnormalities are documented.

A case-level report described behavioral therapy, proprioceptive/vestibular intervention and hippotherapy, followed by improved peer interaction and less obsessive behavior. This is uncontrolled evidence and cannot establish treatment efficacy. (stefaniak2022autisticlikebehaviorsassociated pages 6-8)

Suggested NCIT intervention mappings include Genetic Counseling, Developmental Assessment, Speech Therapy, Augmentative and Alternative Communication, Occupational Therapy, Physical Therapy, Behavioral Therapy, Nutritional Support, Anticonvulsant Therapy, EEG and MRI. Disease-specific response rates and adverse-event data are unavailable.

**Clinical research:** NCT03718910 was a completed, observational cross-sectional study at Mount Sinai, enrolling 15 participants from May 23, 2018 to June 1, 2020. Participants underwent three days of developmental, behavioral, neurologic, psychiatric, medical, EEG, visual-evoked-potential and eye-tracking assessment; samples could support DNA and iPSC research. It characterized natural history rather than testing treatment. The broader Simons Searchlight registry also includes eligible genetic neurodevelopmental conditions. No interventional DDX3X trial was found. (NCT03718910 chunk 1)

## 13. Prevention

The occurrence of a new de novo variant cannot presently be prevented by lifestyle or medication. Primary prevention is therefore limited to reproductive options after a familial variant is known: genetic counseling, parental testing, prenatal diagnosis and preimplantation genetic testing. Cascade testing is especially relevant in families with an inherited male hypomorphic allele. A negative parental blood test substantially lowers but does not eliminate recurrence risk because gonadal mosaicism remains possible.

There is no population newborn screen, vaccine, prophylactic medication or general-population carrier-screening program. Secondary prevention consists of prompt genomic diagnosis and early developmental intervention. Tertiary prevention includes seizure recognition, nutritional support, mobility/scoliosis surveillance, communication access and proactive behavioral/mental-health care.

## 14. Other species and natural disease

Orthologs are experimentally studied in **Mus musculus** (mouse; NCBI Taxon 10090), **Danio rerio** (zebrafish; 7955) and **Xenopus tropicalis** (western clawed frog; 8364). No well-established naturally occurring veterinary counterpart, breed predisposition, animal-health burden, zoonotic transmission or cross-species infectious susceptibility is known. The relevant comparative finding is evolutionary conservation of DDX3-dependent RNA metabolism and neurodevelopment, not a naturally transmitted disease.

## 15. Model organisms

* **Mouse Ddx3x haploinsufficiency:** reproduces developmental, sensory and motor delay, adult hyperactivity/anxiety-like behavior, cognitive and motor deficits, reduced brain volume and abnormal cortical lamination. It has construct and partial face validity but cannot model human language or complex adaptive disability. (boitnott2021developmentalandbehavioral pages 25-28)
* **Conditional neural-progenitor knockout:** demonstrates dosage- and sex-dependent effects on cell-cycle timing, neurogenic divisions, cortical neuron production and microcephaly. Ribosome profiling identifies DDX3X-dependent translated transcripts. (hoye2022aberrantcorticaldevelopment pages 30-31)
* **Cellular/biochemical systems:** severe missense proteins show impaired RNA-helicase activity, abnormal RNA–protein granules and aberrant translation in progenitors and neurons. (lennox2020pathogenicddx3xmutations pages 1-3)
* **Zebrafish:** functional rescue/perturbation assays established partial loss of function for the inherited male p.Arg79Lys allele.
* **Xenopus:** DDX3 depletion disrupts neural-crest induction and craniofacial morphogenesis through RAC1 translation and AKT–GSK3β/β-catenin signaling.

These models support mechanism and target discovery, but none has yet produced a clinically validated therapy.

## Recent developments, 2023–2024

Recent work has shifted from syndrome discovery toward quantitative behavior, communication, sex biology and pathway resolution. The 2023 comparative study showed that anxiety and self-injury—not simply autism severity—may be distinctive clinical burdens in girls and young women with DDX3X variants. (hoye2022aberrantcorticaldevelopment pages 30-31)

A 2024 review emphasized that DDX3X belongs to an expanding group of X-linked neurodevelopmental genes whose effects in females cannot be understood through a simple recessive model; escape from X-inactivation, allele class and sex-specific compensation are central. (lukin2024emergingxlinkedgenes pages 8-9)

The 2024 mechanistic advance linked DDX3X deficiency to **CREBBP-mRNA destabilization, impaired Notch signaling, reduced neural-stem-cell pools and excitatory/inhibitory differentiation imbalance**. This strengthens the causal chain but remains preclinical. Concurrent clinical literature increasingly advocates early augmentative communication rather than waiting for speech to emerge. No 2023–2024 research established a disease-modifying intervention.

## Evidence limitations

Most clinical datasets are small, referral-based and cross-sectional, with inconsistent assessment and age distribution. Apparent phenotype frequencies therefore differ substantially across cohorts. Many rare systemic findings are single-case observations. Variant-level conclusions should use current ClinVar/gnomAD records and an appropriate DDX3X transcript rather than syndrome-level generalization. Population prevalence, lifespan, longitudinal progression, treatment response, environmental modifiers, protective factors, molecular biomarkers and human single-cell/spatial multi-omics remain major knowledge gaps.

References

1. (lennox2020pathogenicddx3xmutations pages 1-3): Ashley L. Lennox, Mariah L. Hoye, Ruiji Jiang, Bethany L. Johnson-Kerner, Lindsey A. Suit, Srivats Venkataramanan, Charles J. Sheehan, Fernando C. Alsina, Brieana Fregeau, Kimberly A. Aldinger, Ching Moey, Iryna Lobach, Alexandra Afenjar, Dusica Babovic-Vuksanovic, Stéphane Bézieau, Patrick R. Blackburn, Jens Bunt, Lydie Burglen, Philippe M. Campeau, Perrine Charles, Brian H.Y. Chung, Benjamin Cogné, Cynthia Curry, Maria Daniela D’Agostino, Nataliya Di Donato, Laurence Faivre, Delphine Héron, A. Micheil Innes, Bertrand Isidor, Boris Keren, Amy Kimball, Eric W. Klee, Paul Kuentz, Sébastien Küry, Dominique Martin-Coignard, Ghayda Mirzaa, Cyril Mignot, Noriko Miyake, Naomichi Matsumoto, Atsushi Fujita, Caroline Nava, Mathilde Nizon, Diana Rodriguez, Lot Snijders Blok, Christel Thauvin-Robinet, Julien Thevenon, Marie Vincent, Alban Ziegler, William Dobyns, Linda J. Richards, A. James Barkovich, Stephen N. Floor, Debra L. Silver, and Elliott H. Sherr. Pathogenic ddx3x mutations impair rna metabolism and neurogenesis during fetal cortical development. May 2020. URL: https://doi.org/10.1016/j.neuron.2020.01.042, doi:10.1016/j.neuron.2020.01.042. This article has 251 citations and is from a highest quality peer-reviewed journal.

2. (dai2022expansionofclinical pages 4-5): Yuwei Dai, Zhuanyi Yang, Jialing Guo, Haoyu Li, Jiaoe Gong, Yuanyuan Xie, Bo Xiao, Hua Wang, and Lili Long. Expansion of clinical and genetic spectrum of ddx3x neurodevelopmental disorder in 23 chinese patients. Frontiers in Molecular Neuroscience, Mar 2022. URL: https://doi.org/10.3389/fnmol.2022.793001, doi:10.3389/fnmol.2022.793001. This article has 21 citations.

3. (NCT03718910 chunk 1): Alexander Kolevzon. DDX3X Syndrome -The Seaver Autism Center for Research and Treatment is Characterizing DDX3X-related Neurodevelopmental Disorders Using Genetic, Medical, and Neuropsychological Measures.. Icahn School of Medicine at Mount Sinai. 2018. ClinicalTrials.gov Identifier: NCT03718910

4. (OpenTargets Search: -DDX3X): Open Targets Query (-DDX3X, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (lukin2024emergingxlinkedgenes pages 8-9): Jeronimo Lukin, Corinne M. Smith, and Silvia De Rubeis. Emerging x-linked genes associated with neurodevelopmental disorders in females. Oct 2024. URL: https://doi.org/10.1016/j.conb.2024.102902, doi:10.1016/j.conb.2024.102902. This article has 12 citations and is from a peer-reviewed journal.

6. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 7-8): Milou G. P. Kennis, Dmitrijs Rots, Arjan Bouman, Charlotte W. Ockeloen, Caroline Boelen, Carlo L. M. Marcelis, Bert B. A. de Vries, Mariet W. Elting, Quinten Waisfisz, Mohnish Suri, Esperanza Font-Montgomery, Dawn S. Peck, Deirdre E. Donnelly, R. Curtis Rogers, Ruth Richardson, Roseline Caumes, Boris Chaumette, Cécile Louveau, Suzanne C. E. H. Sallevelt, Saskia M. Maas, Jeroen J. Smits, Mieke M. van Haelst, Rebecca J. Levy, Helen Stewart, Bart L. Loeys, Rolph Pfundt, Tjitske Kleefstra, and Lot Snijders Blok. Ddx3x-related neurodevelopmental disorder in males – presenting a new cohort of 19 males and a literature review. European Journal of Human Genetics, 33:980-988, Mar 2025. URL: https://doi.org/10.1038/s41431-025-01832-x, doi:10.1038/s41431-025-01832-x. This article has 12 citations and is from a domain leading peer-reviewed journal.

7. (sun2022casereportde pages 8-8): Yi-xi Sun, Yangwen Qian, Haixi Sun, Min Chen, Yuqin Luo, Xiao-jing Xu, K. Yan, Li-ya Wang, Junjie Hu, and Minyue Dong. Case report: de novo ddx3x mutation caused intellectual disability in a female with skewed x-chromosome inactivation on the mutant allele. Frontiers in Genetics, Oct 2022. URL: https://doi.org/10.3389/fgene.2022.999442, doi:10.3389/fgene.2022.999442. This article has 11 citations and is from a peer-reviewed journal.

8. (kennis2025ddx3xrelatedneurodevelopmentaldisorder pages 2-3): Milou G. P. Kennis, Dmitrijs Rots, Arjan Bouman, Charlotte W. Ockeloen, Caroline Boelen, Carlo L. M. Marcelis, Bert B. A. de Vries, Mariet W. Elting, Quinten Waisfisz, Mohnish Suri, Esperanza Font-Montgomery, Dawn S. Peck, Deirdre E. Donnelly, R. Curtis Rogers, Ruth Richardson, Roseline Caumes, Boris Chaumette, Cécile Louveau, Suzanne C. E. H. Sallevelt, Saskia M. Maas, Jeroen J. Smits, Mieke M. van Haelst, Rebecca J. Levy, Helen Stewart, Bart L. Loeys, Rolph Pfundt, Tjitske Kleefstra, and Lot Snijders Blok. Ddx3x-related neurodevelopmental disorder in males – presenting a new cohort of 19 males and a literature review. European Journal of Human Genetics, 33:980-988, Mar 2025. URL: https://doi.org/10.1038/s41431-025-01832-x, doi:10.1038/s41431-025-01832-x. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (hoye2022aberrantcorticaldevelopment pages 30-31): Mariah L Hoye, Lorenzo Calviello, Abigail J Poff, Nna-Emeka Ejimogu, Carly R Newman, Maya D Montgomery, Jianhong Ou, Stephen N Floor, and Debra L Silver. Aberrant cortical development is driven by impaired cell cycle and translational control in a ddx3x syndrome model. Jun 2022. URL: https://doi.org/10.7554/elife.78203, doi:10.7554/elife.78203. This article has 64 citations and is from a domain leading peer-reviewed journal.

10. (stefaniak2022autisticlikebehaviorsassociated pages 6-8): Urszula Stefaniak, Roksana Malak, Ewa Mojs, and Włodzimierz Samborski. Autistic-like behaviors associated with a novel non-canonical splice-site ddx3x variant: a case report of a rare clinical syndrome. Mar 2022. URL: https://doi.org/10.3390/brainsci12030390, doi:10.3390/brainsci12030390. This article has 11 citations.

11. (scala2019threedenovo pages 5-6): Marcello Scala, Annalaura Torella, Mariasavina Severino, Giovanni Morana, Raffaele Castello, Andrea Accogli, Antonio Verrico, Maria Stella Vari, Gerarda Cappuccio, Michele Pinelli, Giuseppina Vitiello, Gaetano Terrone, Alessandra D’Amico, Vincenzo Nigro, and Valeria Capra. Three de novo ddx3x variants associated with distinctive brain developmental abnormalities and brain tumor in intellectually disabled females. European Journal of Human Genetics, 27:1254-1259, Apr 2019. URL: https://doi.org/10.1038/s41431-019-0392-7, doi:10.1038/s41431-019-0392-7. This article has 62 citations and is from a domain leading peer-reviewed journal.

12. (edey2023x‐linkedneuronalmigration pages 9-10): Juliet Edey, Payam Soleimani‐Nouri, Amelia Dawson‐Kavanagh, Muhamad Saad Imran Azeem, and Vasso Episkopou. X‐linked neuronal migration disorders: gender differences and insights for genetic screening. International Journal of Developmental Neuroscience, 83:581-599, Aug 2023. URL: https://doi.org/10.1002/jdn.10290, doi:10.1002/jdn.10290. This article has 11 citations and is from a peer-reviewed journal.

13. (moresco2021anovelde pages 4-6): Giada Moresco, Jole Costanza, Carlo Santaniello, Ornella Rondinone, Federico Grilli, Elisabetta Prada, Simona Orcesi, Ilaria Coro, Anna Pichiecchio, Paola Marchisio, Monica Miozzo, Laura Fontana, and Donatella Milani. A novel de novo ddx3x missense variant in a female with brachycephaly and intellectual disability: a case report. Italian Journal of Pediatrics, Mar 2021. URL: https://doi.org/10.1186/s13052-021-01033-4, doi:10.1186/s13052-021-01033-4. This article has 17 citations and is from a peer-reviewed journal.

14. (boitnott2021developmentalandbehavioral pages 25-28): Andrea Boitnott, Dévina C Ung, Marta Garcia-Forn, Kristi Niblo, Danielle Mendonca, Michael Flores, Sylvia Maxwell, Jacob Ellegood, Lily R Qiu, Dorothy E Grice, Jason P Lerch, Mladen-Roko Rasin, Joseph D Buxbaum, Elodie Drapeau, and Silvia De Rubeis. Developmental and behavioral phenotypes in a new mouse model of ddx3x syndrome. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.22.427482, doi:10.1101/2021.01.22.427482. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Intellectual_Disability_X-linked_102-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.

34 of 36 terms resolved to a current term; the rest could not be looked up either way.