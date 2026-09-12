---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T20:43:37.867633'
end_time: '2026-08-31T20:56:02.230068'
duration_seconds: 744.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia 48
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
  total_terms: 18
  verified: 18
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
  path: Spinocerebellar_Ataxia_48-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia 48
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 48** covering all of the
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
- **Disease Name:** Spinocerebellar Ataxia 48
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 48** covering all of the
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


# Spinocerebellar Ataxia Type 48 (SCA48): Disease-Characteristics Report

## Executive summary

Spinocerebellar ataxia type 48 (SCA48; **ATX-STUB1/SCA-STUB1**) is a rare, usually adult-onset, progressive neurodegenerative disorder caused primarily by **heterozygous germline variants in STUB1**, which encodes the co-chaperone and E3 ubiquitin ligase CHIP. Its characteristic combination is cerebellar ataxia, cerebellar atrophy, and a frequently early cognitive-affective or psychiatric syndrome; tremor, parkinsonism, pyramidal signs, dystonia, chorea, neuropathy, epilepsy, and autonomic symptoms broaden the phenotype. The largest retrieved cohort found candidate STUB1 variants in 30/440 ataxia families (approximately 7%), with cognitive impairment in 54% of carriers, but this is a diagnostic-cohort proportion—not population prevalence. Mean onset was 40.0 ± 13.8 years, with a 17–74-year range and marked age-dependent penetrance. (roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 1-2)

The strongest current model is that many SCA48 cases are **monogenic STUB1 disorders**, while intermediate **TBP** CAG/CAA expansions and possibly variants in other ataxia genes can modify penetrance or severity. Three unrelated 2024 cases had pathogenic/likely pathogenic STUB1 variants, normal TBP alleles, and SCA48, directly supporting monogenic causation. (zochowski2024caseseriesof pages 3-5)

No SCA48-specific disease-modifying treatment, validated prognostic biomarker, population incidence estimate, or interventional clinical trial was identified. Current implementation consists of molecular diagnosis, counseling and cascade testing, rehabilitation, assistive care, and symptom-directed management.

---

## 1. Disease information

### Definition

SCA48 is a Mendelian, autosomal-dominant spinocerebellar degeneration in which cognitive-affective dysfunction may precede conventional motor ataxia by years. The original family showed a continuum from dysexecutive symptoms to severe cerebellar cognitive-affective syndrome (CCAS) and finally truncal ataxia, with neurodegeneration initially concentrated in cerebellar regions supporting cognition and emotion. (genis2018heterozygousstub1mutation pages 1-2)

### Identifiers and nomenclature

- **Preferred name:** Spinocerebellar ataxia type 48.
- **Synonyms:** SCA48; ATX-STUB1; SCA-STUB1; autosomal-dominant STUB1-related ataxia; dominant cerebellar ataxia with cognitive-affective syndrome.
- **OMIM phenotype:** **618093**.
- **Causal gene:** **STUB1**, OMIM **607207**; chromosome **16p13.3**. (genis2018heterozygousstub1mutation pages 1-2)
- **MONDO:** A dedicated, confidently verified MONDO identifier was not recovered; it should not be inferred from identifiers for other SCA subtypes. Open Targets did not return a specific SCA48–STUB1 record in the retrieved search, illustrating incomplete database indexing rather than evidence against the association. (OpenTargets Search: spinocerebellar ataxia type 48)
- **Orphanet:** No dedicated identifier was verified from the retrieved material.
- **ICD-10:** Usually represented under a nonspecific hereditary ataxia category, commonly **G11.8/G11.9**, depending on jurisdiction; there is no verified SCA48-specific code.
- **ICD-11/MeSH:** No SCA48-specific term was verified; broader hereditary/cerebellar ataxia concepts are used.
- **Suggested MONDO mapping:** map to a dedicated SCA48 concept if present in the target terminology release, with parent concepts *autosomal dominant cerebellar ataxia* and *spinocerebellar ataxia*; do not substitute SCA1 or another numbered subtype.

### Evidence granularity

The evidence is principally **aggregated disease-level evidence** derived from pedigrees, multicenter research cohorts, case series, imaging studies, and postmortem pathology—not population EHR surveillance. Individual-patient observations contribute materially because the disorder was only delineated in 2018 and remains exceptionally rare. The discovery study followed one family for more than a decade using serial neurological/neuropsychological assessments, MRI, SPECT, and genetics. (genis2018heterozygousstub1mutation pages 1-2)

---

## 2. Etiology, risk, and protective factors

### Primary cause

The initiating lesion is generally a **heterozygous germline pathogenic or likely pathogenic STUB1 sequence variant**. Frameshift, nonsense, splice, in-frame deletion, and missense variants are reported throughout the coding sequence, including the N-terminal tetratricopeptide-repeat (TPR) chaperone-binding region and C-terminal U-box E3-ligase region. The original pathogenic variant was **c.823_824delCT (p.Leu275Aspfs*16)**. (genis2018heterozygousstub1mutation pages 1-2, roux2020clinicalneuropathologicaland pages 2-3)

### Genetic risk and modifiers

- **Family history:** An affected first-degree relative raises prior probability, but negative family history does not exclude SCA48 because de novo variants, late onset, and incomplete penetrance occur. A de novo **c.155C>G (p.Ala52Gly)** TPR-domain variant caused progressive ataxia with pan-cerebellar atrophy. (umano2022themolecularbasis pages 1-2)
- **TBP:** Intermediate-length TBP alleles—typically discussed around 40–46 or 40–49 CAG/CAA repeats—can coexist with STUB1 variants. A 2023 digenic cohort described a severe multidomain ataxia-dementia phenotype, reduced cerebellar cortex and brainstem volumes, and implications for recurrence-risk calculations. (nanetti2023complexataxia‐dementiaphenotype pages 1-2)
- **Countervailing evidence:** Three 2024 Australian probands had normal TBP alleles (34/35, 35/35, and 34/35 repeats) yet unequivocal SCA48 phenotypes, supporting STUB1 monogenic disease. (zochowski2024caseseriesof pages 3-5)
- **Penetrance example:** One p.Pro243Leu carrier without a TBP expansion remained asymptomatic at age 77, whereas STUB1 plus TBP45 segregated with severe, fully penetrant disease in another family. This supports—but does not prove—a modifier role. (winter2025tbprepeatexpansion pages 6-10)
- **Other proposed modifiers:** second hits in **AFG3L2, PRKCG, and TBP** were found in three families; their causal magnitude remains uncertain. (roux2020clinicalneuropathologicaland pages 1-2)
- **Sex:** A multicenter cohort was 72% female (36/50), and maternal transmission was frequent, prompting a hypothesis of sex-dependent penetrance. This was not consistently replicated and should not be treated as established biology. (roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 3-4)

### Environmental, lifestyle, infectious, and protective factors

No reproducible environmental toxin, occupational exposure, infection, diet, smoking pattern, exercise exposure, or protective allele has been established as causing or preventing SCA48. Cellular stress can expose functional defects in mutant CHIP experimentally, but this is not evidence that ordinary heat or environmental stress causes human disease. (umano2022themolecularbasis pages 1-2)

No validated gene–environment interaction is known. Avoiding alcohol intoxication, sedating medication, and other factors that acutely worsen balance is sensible clinical risk reduction, not primary prevention of the molecular disease.

---

## 3. Phenotypes

The principal ontology-ready phenotypes, frequencies, temporal characteristics, and functional consequences are summarized below.

| Domain / phenotype | Evidence / frequency and temporal characteristics | Suggested HPO term | Functional / QoL consequence |
|---|---|---|---|
| Cerebellar ataxia / gait ataxia | Core phenotype. Discovery family: late truncal ataxia emerging after years of cognitive-affective symptoms; adult-onset, slowly progressive (genis2018heterozygousstub1mutation pages 1-2). Multicenter cohort: mean age at onset 40.0 ± 13.8 years, range 17–74; age at onset highly variable (roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 1-2). Australian 2024 series: ataxia in 3/3, onset ages 32, 57, 61; summary of all reported patients in that series: gait ataxia 8/9 (zochowski2024caseseriesof pages 3-5, zochowski2024caseseriesof pages 6-8). | HP:0001251 | Progressive imbalance, falls, loss of independent mobility; disease-specific QoL metrics not reported in collected SCA48 sources. |
| Dysarthria | Common motor cerebellar sign. Australian 2024 series: dysarthria 3/3; presenting symptom in 2/3 (zochowski2024caseseriesof pages 3-5, zochowski2024caseseriesof pages 5-6). Qualitative reports across families describe adult-onset progressive speech impairment (li2024clinicalandfunctional pages 1-2). | HP:0001260 | Reduced speech intelligibility and communication; no SCA48-specific QoL scale reported. |
| Cerebellar cognitive-affective syndrome / cognitive impairment | Hallmark non-motor feature. Discovery family: 6 fully affected patients showed cognitive-affective syndrome; 3 presymptomatic carriers already had focal cerebellar atrophy before ataxia (genis2018heterozygousstub1mutation pages 1-2). Multicenter cohort: cognitive impairment in 54% of STUB1 variant carriers, predominantly frontal syndrome (roux2020clinicalneuropathologicaland pages 1-2). Australian 2024 series: cognitive impairment 2/3 (zochowski2024caseseriesof pages 3-5). | HP:0100543 | Executive dysfunction, memory/language deficits, impaired daily planning and judgment; no standardized SCA48 QoL outcome reported. |
| Psychiatric / behavioral symptoms | Frequently reported qualitatively: depression, anxiety, behavioral changes, psychiatric dysfunction (zochowski2024caseseriesof pages 3-5, li2024clinicalandfunctional pages 1-2). Large Dutch family had prominent behavioral changes with cognitive decline (mol2020clinicalandpathologic pages 1-2). In the 9-patient summary from the Australian report, psychiatric symptoms were 6/9 (zochowski2024caseseriesof pages 6-8). | HP:0000708 | Major impact on social/occupational functioning and caregiver burden; no disease-specific QoL metrics available. |
| Tremor | Increasingly recognized feature. Australian 2024 series: tremor 3/3, with rest tremor in 2 and action tremor in 1; summary frequency 3/9 in prior aggregate comparison cited in the same report (zochowski2024caseseriesof pages 5-6, zochowski2024caseseriesof pages 6-8). Can precede or accompany ataxia (rest tremor was presenting symptom in 1/3) (zochowski2024caseseriesof pages 3-5). | HP:0001337 | Impairs handwriting, feeding, and fine motor tasks; no SCA48-specific QoL metric reported. |
| Dysmetria / limb incoordination | Discovery and later case reports describe complete motor cerebellar syndrome with dysmetria (genis2018heterozygousstub1mutation pages 1-2). Australian 2024 series: dysmetria 2/3 (zochowski2024caseseriesof pages 3-5). | HP:0001310 | Fine motor inaccuracy affecting reaching, dressing, and utensil use; no formal QoL data reported. |
| Oculomotor abnormalities | Qualitative recurrent feature: oculomotor abnormalities and dysmetric saccades reported in SCA48 literature summarized in 2024 series (zochowski2024caseseriesof pages 3-5). In that series, ocular abnormalities occurred in 1/3 and impaired upward gaze in 1 patient (zochowski2024caseseriesof pages 3-5). | HP:0000508 | Visual tracking difficulties may worsen gait/balance and reading; QoL metrics unavailable. |
| Pyramidal signs / hypertonia / pathologic reflexes | Positive pyramidal tract signs described as part of phenotypic spectrum (li2024clinicalandfunctional pages 1-2). Australian 2024 series: pathologic reflexes 2/3, hypertonia 2/3, extensor plantar responses reported in individual cases (zochowski2024caseseriesof pages 3-5). | HP:0002495 | Adds stiffness and gait disability to cerebellar syndrome; no formal SCA48 QoL data reported. |
| Parkinsonism / bradykinesia / rigidity | Recognized less-common but recurrent feature. Dutch pedigree: gait disturbance could present as ataxia or parkinsonism (mol2020clinicalandpathologic pages 1-2). Australian 2024 series: bradykinesia 1/3, cogwheel rigidity 1/3, parkinsonian rest tremor in 2/3 (zochowski2024caseseriesof pages 3-5, zochowski2024caseseriesof pages 6-8). | HP:0001300 | Slowness and rigidity worsen mobility and upper-limb function; QoL metrics unavailable. |
| Chorea / dystonia / hyperkinetic features | Reported as rarer clinical features in qualitative summaries (zochowski2024caseseriesof pages 3-5, li2024clinicalandfunctional pages 1-2). Dystonic head posturing documented in one 2024 Australian case (zochowski2024caseseriesof pages 3-5). | HP:0002072 / HP:0001332 | May complicate diagnosis and interfere with speech/posture; no SCA48-specific QoL data. |
| Peripheral neuropathy / sensory loss / areflexia | Rarer but documented. Australian 2024 series: one patient had length-dependent sensorimotor axonal peripheral neuropathy on nerve conduction study with sensory loss, absent ankle jerks, pes cavus/hammer toes, and Romberg sign (1/3) (zochowski2024caseseriesof pages 3-5). Qualitative summaries mention peripheral neuropathies (zochowski2024caseseriesof pages 3-5). | HP:0009830 | Sensory loss and neuropathy worsen gait instability and distal weakness; QoL metrics unavailable. |
| Dysphagia | Qualitative feature in disease summaries; explicitly present in 1/3 Australian patients and among presenting symptoms in 1/3 (zochowski2024caseseriesof pages 3-5). | HP:0002015 | Risk for choking, nutrition problems, and aspiration burden; no SCA48-specific swallowing QoL measure reported. |
| Bladder dysfunction | Reported in one Australian patient as urinary urgency/incontinence during progression (1/3) (zochowski2024caseseriesof pages 3-5). | HP:0000020 | Can reduce independence and increase caregiver burden; QoL metrics unavailable. |
| Cerebellar atrophy on MRI | Highly consistent biomarker-level phenotype. Discovery pedigree: vermian and hemispheric atrophy; presymptomatic focal vermian/paravermian and lobules VI–VII atrophy before ataxia (genis2018heterozygousstub1mutation pages 1-2). Australian 2024 series: cerebellar atrophy 3/3, often diffuse (zochowski2024caseseriesof pages 3-5). Umano 2022 de novo case: prominent pan-cerebellar atrophy (umano2022themolecularbasis pages 1-2). | HP:0001272 | Correlates with progressive motor/cognitive disability; no direct MRI-QoL linkage quantified in collected SCA48 studies. |
| Purkinje cell loss / cerebellar degeneration (pathology) | Neuropathology: massive Purkinje cell loss in vermis and major loss in hemispheres reported in heterozygous STUB1 patient(s) (roux2020clinicalneuropathologicaland pages 1-2). Additional reports found subtotal Purkinje cell loss, molecular layer atrophy, p62-positive inclusions, and thalamic/brainstem degeneration (gorcenco2024clinicalandgenetic pages 9-9). Temporal pattern inferred as downstream pathology of progressive disease. | HP:0007366 | Likely substrate of worsening coordination and cognition; patient-reported QoL metrics not available. |


*Table: This table summarizes ontology-ready clinical phenotypes for spinocerebellar ataxia 48 using only collected evidence. It distinguishes exact frequencies from qualitative reports and notes where disease-specific quality-of-life data are unavailable.*

Additional observations include dysphagia, urinary urgency/incontinence, epilepsy in rare reports, distal wasting, pes cavus, hammer toes, myoclonus, and abnormal saccades. In the 2024 three-patient series, ataxia, dysarthria, tremor, and cerebellar atrophy each occurred in 3/3; cognitive impairment and dysmetria in 2/3; ocular abnormality, muscle wasting, sensory loss, neuropathy, dysphagia, bladder dysfunction, and bradykinesia occurred in individual patients. These small denominators must not be interpreted as population frequencies. (zochowski2024caseseriesof pages 3-5, zochowski2024caseseriesof pages 5-6)

**Abstract quotation—discovery phenotype:** “Six patients fully developed cognitive-affective and complete motor cerebellar syndrome associated with vermian and hemispheric cerebellar atrophy.” The same abstract reports focal vermian/paravermian and lobules VI–VII atrophy in three presymptomatic carriers. (genis2018heterozygousstub1mutation pages 1-2)

No SCA48-specific EQ-5D, SF-36, PROMIS, or validated patient-reported outcome data were recovered. Nevertheless, gait instability and falls impair mobility; dysarthria and dysphagia impair communication and nutrition; executive/behavioral disease compromises employment, decision-making, relationships, and independent living.

---

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** STUB1 (STIP1 homology and U-box containing protein 1).
- **Protein:** CHIP, the C-terminus of HSC70-interacting protein.
- **Core functions:** molecular co-chaperone and E3 ubiquitin ligase at the interface of protein folding and degradation.
- **Domains:** N-terminal TPR repeats recruit HSP70/HSP90-family chaperones; the central helical region supports dimerization; the C-terminal U-box recruits E2 conjugating enzymes and mediates ubiquitination. (umano2022themolecularbasis pages 1-2, pakdaman2021chipproteinubox pages 1-2)
- **Suggested GO molecular functions:** ubiquitin-protein transferase activity; ubiquitin-protein ligase activity; heat-shock protein binding; chaperone binding.
- **Suggested GO biological processes:** protein ubiquitination; proteasome-mediated ubiquitin-dependent protein catabolic process; cellular protein quality control; response to unfolded protein; regulation of autophagy/mitophagy; neuron apoptotic process.

### Variant spectrum and interpretation

In 440 ataxia families, 26 different STUB1 variants were detected in 30 families. They included missense, nonsense/stop-gain, splice, frameshift, and in-frame deletion variants distributed across the coding sequence; no simple variant hot spot or robust genotype–phenotype correlation was established. Filtering used gnomAD minor allele frequency <0.001 and CADD >20. Most variants were absent or ultrarare; reported nonzero frequencies were generally approximately 1.5–3.3 × 10⁻⁵. (roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 3-4)

Representative variants include:

- **p.Leu275Aspfs*16:** pathogenic discovery-family frameshift. (genis2018heterozygousstub1mutation pages 1-2)
- **c.689_692del, p.Tyr230Cysfs*9:** pathogenic frameshift. (zochowski2024caseseriesof pages 3-5)
- **c.669+1G>A:** likely pathogenic canonical splice variant. (zochowski2024caseseriesof pages 3-5)
- **c.327_328insCT, p.Tyr110Leufs*21:** likely pathogenic loss-of-function variant. (zochowski2024caseseriesof pages 3-5)
- **c.832del, p.Glu278fs:** U-box frameshift with dominant-negative functional evidence. (chen2021clinicalandfunctional pages 1-2)
- **c.155C>G, p.Ala52Gly:** initially VUS, subsequently supported by de novo status and functional/animal evidence. (umano2022themolecularbasis pages 1-2)
- **c.755A>C, p.Tyr252Ser:** reported as VUS but supported experimentally by reduced CHIP level/ligase function and increased tau aggregation; clinical classification should be periodically reassessed rather than automatically upgraded. (li2024clinicalandfunctional pages 1-2)

Variants are **constitutional/germline**, not somatic tumor mutations. Large chromosomal abnormalities are not the established usual cause. CMA, karyotyping, and FISH therefore have low first-line yield unless another syndromic or copy-number disorder is suspected.

### Mode of action

Evidence supports several nonexclusive mechanisms: haploinsufficiency/loss of function, dominant-negative interference, reduced protein stability, defective chaperone binding, altered oligomerization, and impaired E3-ligase activity. The p.Glu278fs protein impaired interaction with UBE2D1 and produced a dominant-negative effect; p.Ala52Gly retained intrinsic E3 activity but had reduced chaperone affinity and cellular stability. Thus, “loss of CHIP-mediated proteostasis” is more accurate than a single universal molecular mechanism. (chen2021clinicalandfunctional pages 1-2, umano2022themolecularbasis pages 1-2)

No validated SCA48-specific epigenetic signature, DNA-methylation disorder, modifier locus from GWAS, or recurrent structural rearrangement was identified.

---

## 5. Environmental information

SCA48 is not infectious, toxic, nutritional, occupational, or radiation-induced. Environmental exposures have not been shown to alter penetrance. Lifestyle measures are supportive: safe aerobic/strength activity as tolerated, fall prevention, nutritional monitoring when dysphagia occurs, and avoidance of substances that worsen coordination. These measures may reduce complications but do not prevent inheritance or molecular onset.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A **heterozygous STUB1 variant** leads to reduced, unstable, mislocalized, or functionally abnormal CHIP protein. (chen2021clinicalandfunctional pages 1-2, umano2022themolecularbasis pages 1-2, li2024clinicalandfunctional pages 1-2)
2. Abnormal CHIP leads to defective chaperone engagement through the TPR domain and/or defective E2 recruitment and ubiquitin-ligase activity through the U-box. (umano2022themolecularbasis pages 1-2, pakdaman2021chipproteinubox pages 1-2)
3. These defects lead to impaired ubiquitination and proteasomal/autophagic disposal of damaged or chaperone-bound proteins, resulting in loss of neuronal proteostasis. (umano2022themolecularbasis pages 1-2, pakdaman2021chipproteinubox pages 1-2)
4. **Branch A—demonstrated in vitro:** impaired clearance leads to accumulation/aggregation of tau and α-synuclein, caspase-3 activation, and apoptosis. (chen2021clinicalandfunctional pages 1-2, li2024clinicalandfunctional pages 1-2)
5. **Branch B—modifier model, partly inferred:** reduced CHIP/CASA-mediated clearance leads to persistence of intermediate polyglutamine-expanded TBP; this can amplify cognitive, extrapyramidal, and ataxic disease in digenic TBP/STUB1 families. (winter2025tbprepeatexpansion pages 6-10, nanetti2023complexataxia‐dementiaphenotype pages 1-2)
6. Proteostasis failure and stress vulnerability lead to Purkinje-cell dysfunction, dendritic disorganization, and neuronal inclusions; human postmortem tissue demonstrates marked Purkinje-cell loss and ubiquitin/p62-positive inclusions. (mol2020clinicalandpathologic pages 1-2, roux2020clinicalneuropathologicaland pages 1-2, pakdaman2021chipproteinubox pages 1-2)
7. Purkinje-cell and cerebellar network degeneration leads first in some patients to dysfunction of vermian/paravermian and lobules VI–VII cognitive-affective circuits, followed by more diffuse cerebellar degeneration. (genis2018heterozygousstub1mutation pages 1-2)
8. Diffuse cerebellar and variable brainstem, basal-ganglia, cortical, peripheral-nerve, and long-tract involvement results in progressive ataxia, dysarthria, cognitive-affective disease, tremor/parkinsonism, pyramidal signs, and occasional neuropathy or epilepsy. (mol2020clinicalandpathologic pages 1-2, gorcenco2024clinicalandgenetic pages 9-9, zochowski2024caseseriesof pages 3-5)

### Cellular and tissue mechanisms

The best-supported vulnerable cell is the **cerebellar Purkinje neuron**. Human pathology shows massive or subtotal Purkinje-cell loss, molecular-layer atrophy, and p62/ubiquitin inclusions. One family showed inclusions in cerebellum, neocortex, and brainstem; another case had broader thalamic/brainstem degeneration, demonstrating pathological heterogeneity. (mol2020clinicalandpathologic pages 1-2, gorcenco2024clinicalandgenetic pages 9-9, roux2020clinicalneuropathologicaland pages 1-2)

Suggested **Cell Ontology** mappings include Purkinje cell (**CL:0000121**), cerebellar granule cell, neuron, astrocyte, and peripheral sensory/motor neuron where clinically implicated. Suggested **GO cellular components** include cytosol, nucleus, proteasome complex, autophagosome, mitochondrion, neuronal soma, and Purkinje-cell dendritic arbor. CHIP normally has polarized somatodendritic expression; pathogenic missense variants can cause distal dendritic mislocalization.

### Molecular profiling and advanced technologies

No replicated patient-derived SCA48 transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic diagnostic signature was identified through 2024. Functional evidence instead comes from recombinant biochemistry, transfected neuronal/cell systems, neuropathology, and animal models. Claims about immune activation, systemic metabolism, mTOR, Wnt, MAPK, or PI3K-AKT as core SCA48 pathways would presently be speculative.

---

## 7. Anatomical structures affected

- **Primary organ/system:** central nervous system, especially cerebellum.
- **Primary sites:** cerebellar cortex, vermis, paravermis, hemispheres, lobules VI–VII, Purkinje-cell layer, molecular layer, and dentate nuclei. Suggested UBERON terms: cerebellum (**UBERON:0002037**), cerebellar cortex, cerebellar vermis, cerebellar hemisphere, dentate nucleus.
- **Secondary/variable sites:** brainstem, basal ganglia, neocortex, thalamus, hippocampus, spinal/long motor tracts, and peripheral nerves. The 2023 TBP/STUB1 cohort showed significantly reduced brainstem volume; one pathology series found p62-positive inclusions in cerebellum, neocortex, and brainstem. (mol2020clinicalandpathologic pages 1-2, nanetti2023complexataxia‐dementiaphenotype pages 1-2)
- **Peripheral tissue:** length-dependent sensorimotor axonal neuropathy has been objectively demonstrated in an individual case. (zochowski2024caseseriesof pages 3-5)
- **Subcellular compartments:** cytosol and neuronal soma/dendrites; ubiquitin-proteasome and autophagy machinery; nucleus in cases with intranuclear inclusions; mitochondria are biologically plausible through CHIP-regulated mitophagy but not yet a validated human diagnostic compartment.
- **Lateralization:** degeneration is generally bilateral/diffuse, although motor manifestations such as rest tremor, rigidity, or plantar responses may be asymmetric. (zochowski2024caseseriesof pages 3-5)

---

## 8. Temporal development

SCA48 usually has **insidious, chronic, progressive adult onset**, but onset from adolescence to old age is documented. The multicenter mean was 40.0 ± 13.8 years (range 17–74). (roux2020clinicalneuropathologicaland pages 2-3)

A practical, nonvalidated staging framework is:

1. **Preclinical:** pathogenic-variant carrier, potentially with focal cerebellar atrophy but no motor ataxia.
2. **Early:** cognitive/affective change, subtle gait imbalance, dysarthria, tremor, or psychiatric presentation.
3. **Intermediate:** overt gait/limb ataxia, falls, dysarthria, movement disorder, pyramidal signs, and declining executive function.
4. **Advanced:** diffuse cerebellar atrophy, severe CCAS/dementia, dysphagia, incontinence, and dependence for daily activities.

The sequence varies: cognitive-affective disease can precede ataxia, whereas other patients first develop gait ataxia or tremor. One STUB1/TBP45 patient progressed from onset at 29 years to full daily dependency by 41, but this severe digenic example should not be generalized to monogenic SCA48. (winter2025tbprepeatexpansion pages 6-10)

No spontaneous remission is expected. No validated annual SARA progression rate, median disease duration, or critical therapeutic window has been established. Presymptomatic cerebellar atrophy suggests that a future disease-modifying intervention may need to begin before overt motor conversion. (genis2018heterozygousstub1mutation pages 1-2)

---

## 9. Inheritance and population

### Inheritance

- **Pattern:** autosomal dominant; a heterozygous affected individual theoretically transmits the variant to 50% of offspring.
- **Penetrance:** incomplete, age-dependent, and potentially modifier-dependent. An unaffected heterozygous parent at 65 and another carrier at 77 have been described. (winter2025tbprepeatexpansion pages 6-10, roux2020clinicalneuropathologicaland pages 3-4)
- **Expressivity:** highly variable, including cognitive-first, ataxia-first, tremor/parkinsonism-first, and multisystem phenotypes.
- **De novo disease:** established. (umano2022themolecularbasis pages 1-2)
- **Anticipation:** not established for monogenic STUB1 disease. Apparent anticipation can be confounded by ascertainment and TBP repeat inheritance.
- **Mosaicism:** no established germline-mosaicism rate.
- **Consanguinity:** not relevant to typical dominant SCA48, but important when distinguishing biallelic STUB1-related SCAR16.

### Epidemiology

No reliable population prevalence, annual incidence, carrier frequency, birth prevalence, or mortality rate exists. The general SCA incidence figure of approximately 1.5/100,000 quoted in the discovery paper applies to the broader SCA group, not SCA48. (genis2018heterozygousstub1mutation pages 1-2)

In a selected multicenter ataxia series, STUB1 variants were found in 30/440 families (approximately 7%); this indicates diagnostic importance among unsolved/dominant ataxias but cannot be converted into general-population prevalence. Patients have been reported across Spain, Italy, France, the Netherlands, Turkey, Belgium, Germany, Britain, Taiwan, China, Korea, Sweden, and Australia, without a confirmed founder population. (zochowski2024caseseriesof pages 3-5, roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 1-2)

The apparent female enrichment (approximately 70–72%) in one cohort is hypothesis-generating; a true sex ratio remains unresolved. (roux2020clinicalneuropathologicaland pages 2-3, roux2020clinicalneuropathologicaland pages 1-2)

---

## 10. Diagnostics

### Clinical and imaging assessment

Suspect SCA48 in progressive ataxia—especially when accompanied or preceded by executive/behavioral/psychiatric dysfunction, tremor, parkinsonism, chorea, dystonia, or pyramidal signs. Recommended assessment includes:

- neurological examination and standardized ataxia rating, preferably **SARA**;
- formal neuropsychological testing emphasizing executive function, verbal fluency, affect, memory, and social cognition;
- brain MRI with careful assessment of vermian and hemispheric cerebellar atrophy, lobules VI–VII, dentate nuclei, brainstem, basal ganglia, and white matter;
- speech/swallow evaluation, falls and occupational assessment;
- EMG/nerve-conduction studies when sensory loss, wasting, areflexia, or pes cavus is present;
- EEG only when seizures are suspected.

The diagnostic triad is a compatible progressive phenotype, selective/diffuse cerebellar atrophy, and a causative heterozygous STUB1 variant. (zochowski2024caseseriesof pages 3-5)

### Genetic testing algorithm

1. Exclude acquired/treatable causes of progressive ataxia according to presentation—medication/toxin exposure, alcohol, vitamin E/B12/thiamine deficiency, thyroid disease, autoimmune/paraneoplastic ataxia, infection, neoplasm, and structural disease.
2. Test common repeat-expansion ataxias appropriate to ancestry and phenotype. In the retrieved cases these included SCA1, 2, 3, 6, 7, 12, 17, Friedreich ataxia, and related loci. (zochowski2024caseseriesof pages 3-5, roux2020clinicalneuropathologicaland pages 1-2)
3. Use a comprehensive ataxia panel containing **STUB1**, with single-nucleotide, indel, splice, and copy-number analysis.
4. If negative or the phenotype is atypical, use WES or preferably WGS, while recognizing that routine exome sequencing can miss repeat expansions, deep intronic variants, and some structural variants.
5. Confirm candidate variants by Sanger sequencing and perform segregation/de novo testing.
6. Independently size **TBP CAG/CAA repeats**, because an intermediate expansion can alter interpretation, penetrance, phenotype, and counseling. (winter2025tbprepeatexpansion pages 6-10, nanetti2023complexataxia‐dementiaphenotype pages 1-2)
7. Apply ACMG/AMP criteria cautiously. Functional studies can support a VUS but should be integrated with rarity, phenotype, segregation, and de novo evidence.

CMA, karyotype, FISH, and mitochondrial-genome testing are not routine SCA48 confirmation tests, although a broad panel/WGS may assess copy-number and mitochondrial alternatives. RNA sequencing may help resolve splice variants but is not a validated standalone diagnostic.

### Differential diagnosis

Important alternatives include SCA17/TBP disease, digenic TBP/STUB1 disease, SCAR16/biallelic STUB1 disease, Huntington disease and phenocopies, frontotemporal dementia, multiple-system atrophy-cerebellar type, RFC1/CANVAS, SCA27B/FGF14 expansion, common polyglutamine SCAs, SPG7, AFG3L2/SCA28, PRKCG/SCA14, mitochondrial ataxias, and acquired immune/toxic/nutritional causes. Biallelic STUB1 disease more often has earlier-onset multisystem ataxia and may include hypogonadism, but phenotypic overlap is substantial.

### Screening

There is no newborn or population screening. Once a familial pathogenic variant is established, offer genetics-led **cascade testing** to adult relatives, with pretest counseling about age-dependent penetrance and uncertain prognosis. Predictive testing in minors is generally inappropriate for a predominantly adult-onset disorder unless a clear childhood medical benefit exists.

---

## 11. Outcome and prognosis

SCA48 is chronic and usually progressive. Major morbidity arises from falls, impaired mobility and hand coordination, dysarthria/dysphagia, cognitive-behavioral decline, psychiatric disease, and eventual dependence. Some patients remain mildly affected for years, while severe STUB1/TBP presentations can reach daily dependency within approximately a decade. (winter2025tbprepeatexpansion pages 6-10, zochowski2024caseseriesof pages 3-5)

No SCA48-specific 5- or 10-year survival, life expectancy, standardized disability trajectory, aspiration rate, institutionalization rate, or disease-specific mortality estimate is available. Recovery of lost neurodegenerative function is not expected, although rehabilitation and assistive technology can improve safety and functional compensation.

Potential adverse prognostic features—still unvalidated—include early cognitive/psychiatric disease, extensive cerebellar/brainstem atrophy, intermediate TBP expansion, and multisystem neurological involvement. No fluid biomarker such as neurofilament light has been validated specifically for SCA48.

---

## 12. Treatment and current applications

### Disease-modifying therapy and trials

There is **no approved SCA48-specific disease-modifying drug, gene therapy, ASO, siRNA, cell therapy, or surgical treatment**. Searches retrieved no SCA48-specific interventional ClinicalTrials.gov study. Trials of riluzole, varenicline, or N-acetyl-L-leucine in other ataxia genotypes cannot be extrapolated as evidence of SCA48 efficacy.

### Current real-world management

Care should be coordinated by neurology, clinical genetics, rehabilitation medicine, neuropsychology/psychiatry, physiotherapy, occupational therapy, speech-language pathology, dietetics, and social services.

- **Ataxia/falls:** balance and coordination training, strength/conditioning, gait aids, home-safety modifications, orthotics, wheelchair assessment, and driving/work review. Suggested NCIT concepts: Physical Therapy; Occupational Therapy; Rehabilitation Therapy.
- **Dysarthria/dysphagia:** speech therapy, communication devices, instrumental swallow assessment, texture modification, nutrition monitoring, and enteral feeding when clinically necessary. Suggested NCIT: Speech Therapy; Swallowing Therapy; Enteral Nutrition.
- **Tremor/dystonia/parkinsonism:** individualized symptomatic trials by a movement-disorder specialist; evidence is anecdotal and no SCA48 response rate is established. Botulinum toxin may be considered for focal dystonia. Suggested NCIT: Pharmacologic Therapy; Botulinum Toxin Therapy.
- **Spasticity:** stretching, physiotherapy, and standard antispasticity agents when functionally useful.
- **Psychiatric/cognitive disease:** neuropsychological evaluation, structured routines, caregiver education, psychotherapy, and conventional treatment of depression, anxiety, psychosis, or behavioral disturbance.
- **Neuropathy and bladder symptoms:** standard neuropathic-pain, foot-care, orthotic, continence, and urological management.
- **Complication prevention:** vaccination and pulmonary care are routine health maintenance, not SCA48-specific therapy; monitor aspiration, malnutrition, fractures, and caregiver strain.

### Experimental directions

Mechanistically attractive strategies include restoring CHIP expression or function, enhancing chaperone/proteasome/autophagy capacity, preventing toxic protein accumulation, and targeting modifier pathways. However, CHIP has many substrates and systemic functions, making nonspecific activation or replacement potentially hazardous. The p.Ala52Gly animal work showed that raising normal CHIP can be neuroprotective in experimental systems, but no human efficacy or safety evidence exists. (umano2022themolecularbasis pages 1-2)

No SCA48 pharmacogenomic guidance, combination regimen, treatment response rate, or disease-specific adverse-event dataset is available.

---

## 13. Prevention

- **Primary prevention:** the germline mutation cannot be prevented by lifestyle or vaccination. Reproductive options after identification of a familial pathogenic variant include preimplantation genetic testing, prenatal diagnosis, donor gametes, and adoption, following nondirective counseling.
- **Secondary prevention/early detection:** cascade testing of adult relatives; baseline neurological, cognitive, and MRI assessment where appropriate; periodic follow-up of confirmed carriers. There is no evidence-based surveillance interval.
- **Tertiary prevention:** fall prevention, exercise and rehabilitation, aspiration/nutrition surveillance, psychiatric treatment, bone-health measures, assistive devices, and caregiver support.
- **Public health:** no population, newborn, infectious, or environmental-control program is indicated.

Counseling must address the nominal 50% transmission risk, incomplete and age-dependent penetrance, variable severity, possible de novo disease, and the potential influence of TBP alleles. (winter2025tbprepeatexpansion pages 6-10, nanetti2023complexataxia‐dementiaphenotype pages 1-2, roux2020clinicalneuropathologicaland pages 3-4)

---

## 14. Other species and natural disease

No well-established naturally occurring SCA48-equivalent disease in companion animals, livestock, or wildlife was identified. Accordingly, no breed-specific VBO annotation, veterinary prevalence, zoonotic potential, or cross-species transmission applies.

The **STUB1/CHIP proteostasis function is strongly conserved**, supporting comparative experimental work. Relevant taxa include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Danio rerio* (7955), *Caenorhabditis elegans* (6239), and common cultured human-cell systems. This is inherited molecular disease, not transmissible disease.

---

## 15. Model organisms

### Zebrafish

A *Danio rerio* stub1 mutant truncating the CHIP U-box showed impaired ubiquitination of HSC70 and CHIP, decreased brain 26S-proteasome activity, reduced Purkinje-cell number and soma size, abnormal Purkinje dendrites, and behavioral changes. It did **not** show gross cerebellar atrophy, an important limitation relative to human disease. (pakdaman2021chipproteinubox pages 1-2)

**Abstract quotation:** “no gross cerebellar atrophy was evident in mutant fish,” but the fish displayed reduced Purkinje-cell number/size and abnormal dendritic organization. (pakdaman2021chipproteinubox pages 1-2)

### C. elegans

Transgenic expression of human CHIP p.Ala52Gly produced neurodegeneration and constituted an initial variant-specific SCA48 animal model. The model is useful for stress sensitivity and modifier screening but lacks a vertebrate cerebellum and cannot reproduce CCAS or human MRI anatomy. (umano2022themolecularbasis pages 1-2)

### Mouse and developmental systems

Manipulation of CHIP expression affected differentiation and migration of cerebellar granule-neuron progenitors. This supports a role in cerebellar development and neuronal homeostasis but does not by itself reproduce the full adult-onset dominant human syndrome. (chen2021clinicalandfunctional pages 1-2)

### Cellular and biochemical models

Recombinant-protein assays, HEK293 and neuronal systems, minigene assays, ubiquitination assays, protein-stability studies, and apoptosis assays have been used to classify variants and dissect TPR-versus-U-box dysfunction. These models demonstrate defective chaperone affinity, E2 interaction, ubiquitination, protein stability, tau/α-synuclein accumulation, and caspase activation. Their limitation is that overexpression and acute stress may not reflect decades-long human Purkinje-cell disease. (chen2021clinicalandfunctional pages 1-2, umano2022themolecularbasis pages 1-2, li2024clinicalandfunctional pages 1-2)

---

## Evidence appraisal and major knowledge gaps

The human genetic association is strong: cosegregation in multiple pedigrees, independent pathogenic variants, de novo occurrences, consistent cerebellar phenotypes, and convergent functional evidence. The principal unresolved issue is not whether monoallelic STUB1 can cause SCA48, but why penetrance and phenotype vary so markedly and how often TBP or other alleles materially modify disease.

Highest-priority research needs are an international genotype-curated registry; prospective SARA, cognitive, speech/swallow, digital-gait, and MRI natural history; penetrance estimates stratified by variant domain, age, sex, and TBP repeat size; validated fluid/imaging biomarkers; patient-reported quality-of-life studies; and faithful mammalian knock-in models. The 2024 monogenic case series and Chinese functional study strengthened variant interpretation, but neither supplies population epidemiology or treatment evidence. (zochowski2024caseseriesof pages 3-5, li2024clinicalandfunctional pages 1-2)

### Key publication details

- Genis et al., **published online October 31, 2018**, *Neurology*, DOI/URL: https://doi.org/10.1212/WNL.0000000000006550 — discovery pedigree and OMIM 618093. (genis2018heterozygousstub1mutation pages 1-2)
- Roux et al., **accepted June 26, 2020**, *Genetics in Medicine*, DOI/URL: https://doi.org/10.1038/s41436-020-0899-x — 440-family cohort and neuropathology. (roux2020clinicalneuropathologicaland pages 1-2)
- Mol et al., **June 2020**, *Neurology Genetics*, DOI/URL: https://doi.org/10.1212/NXG.0000000000000417 — large pedigree and ubiquitin/p62 inclusions. (mol2020clinicalandpathologic pages 1-2)
- Chen et al., **September 2021**, *Journal of Biomedical Science*, DOI/URL: https://doi.org/10.1186/s12929-021-00763-1 — dominant-negative U-box mechanism. (chen2021clinicalandfunctional pages 1-2)
- Pakdaman et al., **September 24, 2021**, *Frontiers in Molecular Neuroscience*, DOI/URL: https://doi.org/10.3389/fnmol.2021.723912 — zebrafish model. (pakdaman2021chipproteinubox pages 1-2)
- Umano et al., **published online April 7, 2022**, *Journal of Biological Chemistry*, DOI/URL: https://doi.org/10.1016/j.jbc.2022.101899 — p.Ala52Gly biochemical and *C. elegans* model. (umano2022themolecularbasis pages 1-2)
- Nanetti et al., **published online February 17, 2023**, *Movement Disorders*, DOI/URL: https://doi.org/10.1002/mds.29352 — digenic TBP/STUB1 phenotype. (nanetti2023complexataxia‐dementiaphenotype pages 1-2)
- Li et al., **2024**, *Orphanet Journal of Rare Diseases* 19:471, DOI/URL: https://doi.org/10.1186/s13023-024-03456-8 — Chinese pedigree and p.Tyr252Ser functional study. (li2024clinicalandfunctional pages 1-2)
- Zochowski et al., **December 2024**, *Cerebellum*, DOI/URL: https://doi.org/10.1007/s12311-024-01762-2 — three cases without TBP expansions. (zochowski2024caseseriesof pages 3-5)

PMIDs were not present in the retrieved full-text metadata and are therefore not supplied speculatively; the DOI URLs above provide stable primary-source resolution.

References

1. (roux2020clinicalneuropathologicaland pages 2-3): Thomas Roux, Mathieu Barbier, Mélanie Papin, Claire-Sophie Davoine, Sabrina Sayah, Giulia Coarelli, Perrine Charles, Cecilia Marelli, Livia Parodi, Christine Tranchant, Cyril Goizet, Stephan Klebe, Ebba Lohmann, Lionel Van Maldergem, Christine van Broeckhoven, Marie Coutelier, Christelle Tesson, Giovanni Stevanin, Charles Duyckaerts, Alexis Brice, Alexandra Durr, Alexandra Durr, Giovanni Stevanin, Alexis Brice, Frédéric Darios, Sylvie Forlani, Pitié-Salpêtrière Site, Guillaume Banneau, Cécile Cazeneuve, Perrine Charles, Charles Duyckaerts, Bertrand Fontaine, Jean-Philippe Azulay, Odile Boesfplug-Tanguy, Cyril Goizet, Didier Hannequin, Jamilé Hazan, Andrea Burgo, Christophe Verny, Michel Koenig, Pierre Labauge, Cecilia Marelli, Karine N’guyen, Diana Rodriguez, Soraya Belarbi, Abdelmadjid Hamri, Meriem Tazir, Sylvia Boesch, Massimo Pandolfo, Jardim Laura, Velina Guergueltcheva, Ivalo Tournev, Olga Lucia Pedraza Linarès, Jørgen E. Nielsen, Kirsten Svenstrup, Maha Zaki, Peter Bauer, Lüdger Schöls, Rebecca Schüle, Alexander Lossos, Maria-Teresa Bassi, Manuela Basso, Enrico Bertini, Alfredo Brusco, Carlo Casali, Giorgio Casari, Chiara Criscuolo, Alessandro Filla, Laura Orsi, Filippo M. Santorelli, Enza Maria Valente, Marinela Vavla, Giovanni Vazza, André Megarbane, Ali Benomar, Berry Kremer, Willeke Van Roon-Mom, Richard Roxburgh, Anne Kjersti Erichsen, Chantal Tallaksen, Isabel Alonso, Paula Coutinho, José Léal Loureiro, Jorge Sequeiros, Mustapha Salih, Vladimir S. Kostic, Idoia Rouco Axpe, Liena Elsayed, Martin Arce Paucar, Samir Roumani, Soong Bing-Wen, Evan Reid, Nethisinghe Suran, Thomas Warner, and Nicholas Wood. Clinical, neuropathological, and genetic characterization of stub1 variants in cerebellar ataxias: a frequent cause of predominant cognitive impairment. Nov 2020. URL: https://doi.org/10.1038/s41436-020-0899-x, doi:10.1038/s41436-020-0899-x. This article has 54 citations and is from a highest quality peer-reviewed journal.

2. (roux2020clinicalneuropathologicaland pages 1-2): Thomas Roux, Mathieu Barbier, Mélanie Papin, Claire-Sophie Davoine, Sabrina Sayah, Giulia Coarelli, Perrine Charles, Cecilia Marelli, Livia Parodi, Christine Tranchant, Cyril Goizet, Stephan Klebe, Ebba Lohmann, Lionel Van Maldergem, Christine van Broeckhoven, Marie Coutelier, Christelle Tesson, Giovanni Stevanin, Charles Duyckaerts, Alexis Brice, Alexandra Durr, Alexandra Durr, Giovanni Stevanin, Alexis Brice, Frédéric Darios, Sylvie Forlani, Pitié-Salpêtrière Site, Guillaume Banneau, Cécile Cazeneuve, Perrine Charles, Charles Duyckaerts, Bertrand Fontaine, Jean-Philippe Azulay, Odile Boesfplug-Tanguy, Cyril Goizet, Didier Hannequin, Jamilé Hazan, Andrea Burgo, Christophe Verny, Michel Koenig, Pierre Labauge, Cecilia Marelli, Karine N’guyen, Diana Rodriguez, Soraya Belarbi, Abdelmadjid Hamri, Meriem Tazir, Sylvia Boesch, Massimo Pandolfo, Jardim Laura, Velina Guergueltcheva, Ivalo Tournev, Olga Lucia Pedraza Linarès, Jørgen E. Nielsen, Kirsten Svenstrup, Maha Zaki, Peter Bauer, Lüdger Schöls, Rebecca Schüle, Alexander Lossos, Maria-Teresa Bassi, Manuela Basso, Enrico Bertini, Alfredo Brusco, Carlo Casali, Giorgio Casari, Chiara Criscuolo, Alessandro Filla, Laura Orsi, Filippo M. Santorelli, Enza Maria Valente, Marinela Vavla, Giovanni Vazza, André Megarbane, Ali Benomar, Berry Kremer, Willeke Van Roon-Mom, Richard Roxburgh, Anne Kjersti Erichsen, Chantal Tallaksen, Isabel Alonso, Paula Coutinho, José Léal Loureiro, Jorge Sequeiros, Mustapha Salih, Vladimir S. Kostic, Idoia Rouco Axpe, Liena Elsayed, Martin Arce Paucar, Samir Roumani, Soong Bing-Wen, Evan Reid, Nethisinghe Suran, Thomas Warner, and Nicholas Wood. Clinical, neuropathological, and genetic characterization of stub1 variants in cerebellar ataxias: a frequent cause of predominant cognitive impairment. Nov 2020. URL: https://doi.org/10.1038/s41436-020-0899-x, doi:10.1038/s41436-020-0899-x. This article has 54 citations and is from a highest quality peer-reviewed journal.

3. (zochowski2024caseseriesof pages 3-5): Yan Zochowski, Kishore R. Kumar, Matthew Katz, Paul Darveniza, Michel Tchan, Renee Smyth, Susan Tomlinson, Kathy H. C. Wu, and Stephen Tisch. Case series of cerebellar ataxia with tremor due to heterozygous stub1 variants (sca48) without tbp expansions: further evidence for sca48 as a monogenic disease. Cerebellum (London, England), Dec 2024. URL: https://doi.org/10.1007/s12311-024-01762-2, doi:10.1007/s12311-024-01762-2. This article has 4 citations.

4. (genis2018heterozygousstub1mutation pages 1-2): David Genis, Sara Ortega-Cubero, Hector San Nicolás, Jordi Corral, Josep Gardenyes, Laura de Jorge, Eva López, Berta Campos, Elena Lorenzo, Raúl Tonda, Sergi Beltran, Montserrat Negre, María Obón, Brigitte Beltran, Laura Fàbregas, Berta Alemany, Fabián Márquez, Lluís Ramió-Torrentà, Jordi Gich, Víctor Volpini, and Pau Pastor. Heterozygous <i>stub1</i> mutation causes familial ataxia with cognitive affective syndrome (sca48). Nov 2018. URL: https://doi.org/10.1212/wnl.0000000000006550, doi:10.1212/wnl.0000000000006550. This article has 132 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: spinocerebellar ataxia type 48): Open Targets Query (spinocerebellar ataxia type 48, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (umano2022themolecularbasis pages 1-2): A. Umano, K. Fang, Z. Qu, J.B. Scaglione, S. Altinok, C.J. Treadway, E.T. Wick, E. Paulakonis, C. Karunanayake, S. Chou, T.M. Bardakjian, P. Gonzalez-Alegre, R.C. Page, J.C. Schisler, N.G. Brown, D. Yan, and K.M. Scaglione. The molecular basis of spinocerebellar ataxia type 48 caused by a de novo mutation in the ubiquitin ligase chip. May 2022. URL: https://doi.org/10.1016/j.jbc.2022.101899, doi:10.1016/j.jbc.2022.101899. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (nanetti2023complexataxia‐dementiaphenotype pages 1-2): Lorenzo Nanetti, Stefania Magri, Mario Fichera, Anna Castaldo, Anna Nigri, Chiara Pinardi, Alessia Mongelli, Lidia Sarro, Davide Pareyson, Marina Grisoli, Cinzia Gellera, Daniela Di Bella, Caterina Mariotti, and Franco Taroni. Complex ataxia‐dementia phenotype in patients with digenic tbp/stub1 spinocerebellar ataxia. Movement Disorders, 38:665-675, Feb 2023. URL: https://doi.org/10.1002/mds.29352, doi:10.1002/mds.29352. This article has 24 citations and is from a highest quality peer-reviewed journal.

8. (winter2025tbprepeatexpansion pages 6-10): Jonathan De Winter, Liedewei Van de Vondel, Kristof Van Schil, Tine Deconinck, Katrien Storm, Karine Geens, Charlotte Sommeling, David Crosiers, Emke Marechal, Willem De Ridder, Peter De Jonghe, and Jonathan Baets. Tbp repeat expansion analysis in patients carrying heterozygous stub1 variants. Movement Disorders, Feb 2025. URL: https://doi.org/10.1002/mds.30147, doi:10.1002/mds.30147. This article has 4 citations and is from a highest quality peer-reviewed journal.

9. (roux2020clinicalneuropathologicaland pages 3-4): Thomas Roux, Mathieu Barbier, Mélanie Papin, Claire-Sophie Davoine, Sabrina Sayah, Giulia Coarelli, Perrine Charles, Cecilia Marelli, Livia Parodi, Christine Tranchant, Cyril Goizet, Stephan Klebe, Ebba Lohmann, Lionel Van Maldergem, Christine van Broeckhoven, Marie Coutelier, Christelle Tesson, Giovanni Stevanin, Charles Duyckaerts, Alexis Brice, Alexandra Durr, Alexandra Durr, Giovanni Stevanin, Alexis Brice, Frédéric Darios, Sylvie Forlani, Pitié-Salpêtrière Site, Guillaume Banneau, Cécile Cazeneuve, Perrine Charles, Charles Duyckaerts, Bertrand Fontaine, Jean-Philippe Azulay, Odile Boesfplug-Tanguy, Cyril Goizet, Didier Hannequin, Jamilé Hazan, Andrea Burgo, Christophe Verny, Michel Koenig, Pierre Labauge, Cecilia Marelli, Karine N’guyen, Diana Rodriguez, Soraya Belarbi, Abdelmadjid Hamri, Meriem Tazir, Sylvia Boesch, Massimo Pandolfo, Jardim Laura, Velina Guergueltcheva, Ivalo Tournev, Olga Lucia Pedraza Linarès, Jørgen E. Nielsen, Kirsten Svenstrup, Maha Zaki, Peter Bauer, Lüdger Schöls, Rebecca Schüle, Alexander Lossos, Maria-Teresa Bassi, Manuela Basso, Enrico Bertini, Alfredo Brusco, Carlo Casali, Giorgio Casari, Chiara Criscuolo, Alessandro Filla, Laura Orsi, Filippo M. Santorelli, Enza Maria Valente, Marinela Vavla, Giovanni Vazza, André Megarbane, Ali Benomar, Berry Kremer, Willeke Van Roon-Mom, Richard Roxburgh, Anne Kjersti Erichsen, Chantal Tallaksen, Isabel Alonso, Paula Coutinho, José Léal Loureiro, Jorge Sequeiros, Mustapha Salih, Vladimir S. Kostic, Idoia Rouco Axpe, Liena Elsayed, Martin Arce Paucar, Samir Roumani, Soong Bing-Wen, Evan Reid, Nethisinghe Suran, Thomas Warner, and Nicholas Wood. Clinical, neuropathological, and genetic characterization of stub1 variants in cerebellar ataxias: a frequent cause of predominant cognitive impairment. Nov 2020. URL: https://doi.org/10.1038/s41436-020-0899-x, doi:10.1038/s41436-020-0899-x. This article has 54 citations and is from a highest quality peer-reviewed journal.

10. (zochowski2024caseseriesof pages 6-8): Yan Zochowski, Kishore R. Kumar, Matthew Katz, Paul Darveniza, Michel Tchan, Renee Smyth, Susan Tomlinson, Kathy H. C. Wu, and Stephen Tisch. Case series of cerebellar ataxia with tremor due to heterozygous stub1 variants (sca48) without tbp expansions: further evidence for sca48 as a monogenic disease. Cerebellum (London, England), Dec 2024. URL: https://doi.org/10.1007/s12311-024-01762-2, doi:10.1007/s12311-024-01762-2. This article has 4 citations.

11. (zochowski2024caseseriesof pages 5-6): Yan Zochowski, Kishore R. Kumar, Matthew Katz, Paul Darveniza, Michel Tchan, Renee Smyth, Susan Tomlinson, Kathy H. C. Wu, and Stephen Tisch. Case series of cerebellar ataxia with tremor due to heterozygous stub1 variants (sca48) without tbp expansions: further evidence for sca48 as a monogenic disease. Cerebellum (London, England), Dec 2024. URL: https://doi.org/10.1007/s12311-024-01762-2, doi:10.1007/s12311-024-01762-2. This article has 4 citations.

12. (li2024clinicalandfunctional pages 1-2): Jiaqi Li, Wenyi Xie, Jian-Min Chen, Chun-Zuan Xu, Ya-Li Huang, Sheng Chen, Chang-Yun Liu, Ying-Qian Lu, and Zhang-Yu Zou. Clinical and functional characterization of a novel stub1 mutation in a chinese spinocerebellar ataxia 48 pedigree. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03456-8, doi:10.1186/s13023-024-03456-8. This article has 2 citations and is from a peer-reviewed journal.

13. (mol2020clinicalandpathologic pages 1-2): Merel O. Mol, Jeroen G.J. van Rooij, Esther Brusse, Annemieke J.M.H. Verkerk, Shamiram Melhem, Wilfred F.A. den Dunnen, Patrizia Rizzu, Chiara Cupidi, John C. van Swieten, and Laura Donker Kaat. Clinical and pathologic phenotype of a large family with heterozygous <i>stub1</i> mutation. Jun 2020. URL: https://doi.org/10.1212/nxg.0000000000000417, doi:10.1212/nxg.0000000000000417. This article has 30 citations.

14. (gorcenco2024clinicalandgenetic pages 9-9): Sorina Gorcenco, Efthymia Kafantari, Joel Wallenius, Christin Karremo, Erik Alinder, Sigurd Dobloug, Maria Landqvist Waldö, Elisabet Englund, Hans Ehrencrona, Klas Wictorin, Kristina Karrman, and Andreas Puschmann. Clinical and genetic analyses of a swedish patient series diagnosed with ataxia. Journal of Neurology, 271:526-542, Oct 2024. URL: https://doi.org/10.1007/s00415-023-11990-x, doi:10.1007/s00415-023-11990-x. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (pakdaman2021chipproteinubox pages 1-2): Yasaman Pakdaman, Elsa Denker, Eirik Austad, William H. J. Norton, Hans O. Rolfsnes, Laurence A. Bindoff, Charalampos Tzoulis, Ingvild Aukrust, Per M. Knappskog, Stefan Johansson, and Ståle Ellingsen. Chip protein u-box domain truncation affects purkinje neuron morphology and leads to behavioral changes in zebrafish. Frontiers in Molecular Neuroscience, Sep 2021. URL: https://doi.org/10.3389/fnmol.2021.723912, doi:10.3389/fnmol.2021.723912. This article has 7 citations.

16. (chen2021clinicalandfunctional pages 1-2): Huan-Yun Chen, Chia-Lang Hsu, Han-Yi Lin, Yung-Feng Lin, Shih-Feng Tsai, Yu-Jung Ho, Ye-Ru Li, Jin-Wu Tsai, Shu-Chun Teng, and Chin-Hsien Lin. Clinical and functional characterization of a novel stub1 frameshift mutation in autosomal dominant spinocerebellar ataxia type 48 (sca48). Journal of Biomedical Science, Sep 2021. URL: https://doi.org/10.1186/s12929-021-00763-1, doi:10.1186/s12929-021-00763-1. This article has 15 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_48-deep-research-falcon_artifacts/artifact-00.md)

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
| Terms checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.