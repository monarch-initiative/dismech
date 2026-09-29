---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T20:28:03.372342'
end_time: '2026-09-03T20:36:45.380316'
duration_seconds: 522.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Syndromic X-linked Intellectual Disability 94
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 47
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
  path: Syndromic_X-linked_Intellectual_Disability_94-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Syndromic X-linked Intellectual Disability 94
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Syndromic X-linked Intellectual Disability 94** covering all of the
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
- **Disease Name:** Syndromic X-linked Intellectual Disability 94
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Syndromic X-linked Intellectual Disability 94** covering all of the
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


# Syndromic X-linked intellectual disability 94: disease-characteristics report

## Executive summary and scope

Syndromic X-linked intellectual disability 94 is a very rare **GRIA3-related neurodevelopmental disorder** caused by altered function or dosage of the X-chromosomal AMPA-receptor subunit GluA3. The current concept is broader than the historical male-predominant syndrome: pathogenic **loss-of-function (LoF) and gain-of-function (GoF) alleles produce partly distinct phenotypes**, and females can be affected, particularly by de novo heterozygous GoF variants. The best recent dataset comprises only 25 affected individuals, so frequencies are provisional rather than population estimates. In that series, all 25 had global developmental impairment, 12/25 seizures, 14/25 movement disorders, 13/25 hypotonia, and 10/25 hypertonia. GoF was associated with earlier seizures and hypertonia, whereas LoF was associated with hypotonia and sleep disturbance. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)

This report treats “syndromic X-linked intellectual disability 94,” historical **Wu-type X-linked syndromic intellectual developmental disorder**, and the broader **GRIA3-related neurodevelopmental disorder** as overlapping concepts. The broader term is preferable when describing heterozygous affected females or GoF disease that does not follow a simple recessive model. Evidence is predominantly aggregated from small pedigrees, case reports, and one multicenter cohort—not electronic-health-record incidence data.

| Evidence domain | Key finding with exact quantitative values where available | Evidence type | Source/date/DOI |
|---|---|---|---|
| Contemporary genotype–phenotype spectrum | Among **25 patients from 23 families** carrying 17 functionally abnormal variants, all had global developmental impairment: **9/25 moderate**, **12/25 severe**; **12/25** had seizures, **13/25** hypotonia, **10/25** hypertonia, and **14/25** movement disorders, including hyperekplexia or nonepileptic erratic myoclonus in **8/25**. Testing of one frameshift and 43 missense variants found **31 function-altering LoF/GoF variants** and **13 apparently neutral variants**. Median seizure onset was **1 month for GoF** versus **16 months for LoF**. | Human clinical cohort; in-vitro electrophysiology | Rinaldi et al., *Brain*; online **2023-12-01**, 2024 volume; [DOI 10.1093/brain/awad403](https://doi.org/10.1093/brain/awad403) (rinaldi2024gainoffunctionandlossoffunction pages 1-3) |
| Structural variant and prenatal diagnosis | A hemizygous **GRIA3 exon 5–12 deletion** was found in an affected male with intellectual disability, schizophrenia, brain atrophy, seizures, and episodic irritability. The pregnant woman and maternal grandmother were heterozygous; amniotic-fluid testing detected the familial deletion in the fetus. | Human pedigree; prenatal molecular diagnosis | Wang et al., *Biomedical Journal of Scientific & Technical Research*; published **2023-09-15**; [DOI 10.26717/BJSTR.2023.52.008322](https://doi.org/10.26717/BJSTR.2023.52.008322) (jiang2023geneticanalysisand pages 1-2) |
| Female developmental and epileptic encephalopathy | A 13-year-old girl carried de novo heterozygous **NM_007325.5:c.1982T>C, p.Met661Thr**, absent from several population databases and classified **likely pathogenic**. Hypertonia was present at birth; seizures began at **3 months**. Carbamazepine and ethosuximide were ineffective; lamotrigine, clobazam, levetiracetam, and lacosamide gradually controlled seizures. | Human clinical case; WES and segregation | Okano et al., *Human Genome Variation*; published **2023-02-02**; [DOI 10.1038/s41439-023-00232-1](https://doi.org/10.1038/s41439-023-00232-1) (okano2023gria3p.met661thrvariant pages 1-3) |
| Genotype-guided symptomatic treatment | A boy with de novo hemizygous **GRIA3 c.1844C>T, p.Ala615Val** had neurodevelopmental impairment, seizures, hypertonia, and hyperreflexia. **Carbamazepine ameliorated seizures and hypertonia**. Patch-clamp recordings showed slower receptor desensitization and deactivation, supporting GoF. | Human case; in-vitro electrophysiology; transgenic fly | Hamanaka et al., *Human Genetics*; published online **2022-01-15**; [DOI 10.1007/s00439-021-02416-7](https://doi.org/10.1007/s00439-021-02416-7) (hamanaka2022ameliorationofa pages 1-2) |
| Sleep–wake phenotype and allelic mouse model | Two brothers with severe developmental delay and **p.Ala653Thr** had wake periods up to **106 hours** and sleep periods up to **48 hours**. In vitro, the variant stabilized the channel in a closed conformation. CRISPR knock-in hemizygous mice had fewer brief sleep/activity bouts and enhanced period lengthening under constant light. | Human pedigree; in vitro; CRISPR knock-in mouse | Davies et al., *Human Molecular Genetics*; advance publication **2017-07-14**; [DOI 10.1093/hmg/ddx270](https://doi.org/10.1093/hmg/ddx270) (davies2017apointmutation pages 1-2) |
| Knockout behavior and monoamines | Compared with wild-type littermates (**n=14**), knockout mice (**n=13**) showed increased aggression (**p=0.011**), sociality (**p=0.01**), male–male interaction (**p=0.005**), peripheral activity (**p=0.037**), and minor rotarod impairment (**p=0.016**). Striatal dopamine increased (**p=0.034**) and olfactory-bulb serotonin turnover decreased (**p=0.002**). | Germline knockout mouse; behavioral and neurochemical assays | Adamczyk et al., *Behavioural Brain Research*; **2012-04-01**; [DOI 10.1016/j.bbr.2012.01.007](https://doi.org/10.1016/j.bbr.2012.01.007) (adamczyk2012glua3deficiencyinmice pages 1-3) |
| AMPAR interaction proteomics | Hippocampal proteomics in wild-type and **Gria3**-knockout mice showed that GluA2/3 receptors most strongly co-purified with **CNIH-2, TARP-γ2/Stargazin, and Noelin-1/OLFM1**, identifying subtype-specific partners involved in receptor trafficking and gating. | Mouse hippocampal interaction proteomics | van der Spek et al., *Cells*; published **2022-11-17**; [DOI 10.3390/cells11223648](https://doi.org/10.3390/cells11223648) (spek2022expressionandinteraction pages 1-2) |
| Brain-region-specific molecular profiling | Bulk RNA-seq across six brain regions at **1 and 3 months** found **153 regional DEG calls/148 unique DEGs at 1 month** and **209/201 at 3 months**, with downregulated activity-regulated genes and region-specific immune, glial, and oligodendrocyte-pathway changes. Synaptic proteome composition was also altered. | Mouse transcriptomics and synaptic proteomics; **non-peer-reviewed preprint** | Huang et al., *bioRxiv*; posted **2024-11-17**; [DOI 10.1101/2024.11.15.623468](https://doi.org/10.1101/2024.11.15.623468) (huang2024brainregionspecificchangesand pages 1-3) |


*Table: Compact evidence matrix covering clinical genotype–phenotype findings, prenatal diagnosis, functional studies, treatment observations, and animal or omics models relevant to GRIA3-related syndromic X-linked intellectual disability 94.*

## 1. Disease information

### Definition

The disorder is a congenital or early-childhood neurodevelopmental syndrome characterized by developmental delay/intellectual disability, variably accompanied by epilepsy, altered muscle tone, movement disorder, behavioral or psychiatric manifestations, sleep disturbance, dysmorphism, and occasionally cerebellar or cerebral structural abnormalities. GRIA3 encodes GluA3, a pore-forming component of postsynaptic AMPA-type ionotropic glutamate receptors that mediate rapid excitatory neurotransmission. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, okano2023gria3p.met661thrvariant pages 1-3)

### Identifiers and nomenclature

- **OMIM disease:** **#300699**, reported as Wu-type X-linked syndromic intellectual developmental disorder/MRXSW in the retrieved literature. (hu2026reclassificationofthe pages 1-2)
- **OMIM gene:** **GRIA3, *305915**. (okano2023gria3p.met661thrvariant pages 1-3)
- **Gene location:** **Xq25**. (hu2026reclassificationofthe pages 1-2, okano2023gria3p.met661thrvariant pages 1-3)
- **Common names:** syndromic X-linked intellectual disability 94; MRX94; GRIA3-related neurodevelopmental disorder; GRIA3-related intellectual developmental disorder; Wu-type X-linked syndromic intellectual developmental disorder.
- **MONDO, Orphanet, MeSH, ICD-10/ICD-11:** a disease-specific identifier was not verified in the retrieved primary literature. A knowledge base should not infer an exact MONDO or Orphanet code without direct ontology-database verification. Clinically, nonspecific intellectual-developmental-disorder and epilepsy codes may be used, but they are not equivalent to a molecular diagnosis.

**Source granularity:** Published evidence is disease-level aggregation of individually phenotyped patients and families. No prevalence study based on EHRs or administrative claims was identified.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a **germline pathogenic or likely pathogenic GRIA3 alteration**. Reported classes include missense variants, canonical splice variants, frameshift variants, multi-exon deletions or duplications, larger rearrangements, and balanced translocations disrupting GRIA3. Approximately 20 variants had been reported by early 2023, although the 2024 functional study substantially expanded the tested missense spectrum. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, okano2023gria3p.met661thrvariant pages 1-3)

Examples include:

- **LoF/closed-channel:** p.Ala653Thr, which stabilized the receptor in a closed conformation and was associated with severe developmental delay and extreme sleep–wake disturbance. (davies2017apointmutation pages 1-2)
- **GoF:** c.1844C>T, p.Ala615Val, with slowed desensitization/deactivation, hypertonia, hyperreflexia, and seizures. (hamanaka2022ameliorationofa pages 1-2)
- **Likely GoF phenotype:** de novo c.1982T>C, p.Met661Thr in an affected girl; absent from EVS, 1000 Genomes, dbSNP, gnomAD, and HGVD and classified likely pathogenic under ACMG criteria PS2/PM2/PP2/PP3. Direct electrophysiology was not performed. (okano2023gria3p.met661thrvariant pages 1-3)
- **Splice disruption:** c.268+1G>C caused exon-2 skipping in a minigene assay and was reclassified from VUS to likely pathogenic. (hu2026reclassificationofthe pages 4-5, hu2026reclassificationofthe pages 1-2)
- **Structural LoF:** exon 5–12 deletion segregating through carrier females in a Chinese family. (jiang2023geneticanalysisand pages 1-2)
- **Additional familial missense alleles:** c.2360A>G, p.Glu787Gly, and c.1888G>C, p.Gly630Arg. (rinaldi2022myoclonicstatusepilepticus pages 1-2, philips2014xexomesequencingin pages 4-6)

The 2024 study tested one frameshift and 43 rare missense alleles: **31 altered receptor function as LoF or GoF and 13 appeared functionally neutral**. This is important diagnostically: rarity and missense location alone are insufficient evidence of pathogenicity. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)

### Environmental, lifestyle, infectious, and protective factors

No environmental exposure, infection, diet, smoking, alcohol use, occupational exposure, or lifestyle factor has been demonstrated to cause or materially modify this Mendelian disorder. No validated protective allele, modifier gene, or environmental protective factor is known. Family history and male sex increase prior probability for inherited hemizygous LoF disease, but they are not environmental risk factors.

No disease-specific gene–environment interaction has been established. Light sensitivity in the p.Ala653Thr mouse and sleep phenotype suggests that environmental light can modulate circadian expression after the genetic lesion, but this is not evidence that light causes the disorder. (davies2017apointmutation pages 1-2)

## 3. Phenotypes

The following frequencies derive from the 25-person functional cohort and should not be generalized as precise population frequencies:

- **Global developmental impairment/intellectual disability:** 25/25; moderate in 9/25 and severe in 12/25. Suggested HPO: **Global developmental delay (HP:0001263), Intellectual disability (HP:0001249), Severe global developmental delay**. Onset is infancy/early childhood and impairment is generally lifelong. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Epilepsy/seizures:** 12/25. Types included focal motor 6/12, unknown-onset motor 4/12, focal impaired-awareness 1/12, absence/atypical absence 2/12, myoclonic 5/12, generalized tonic-clonic 1/12, and atonic 1/12. Suggested HPO: **Seizure (HP:0001250), Myoclonic seizure (HP:0002123), Focal motor seizure, Absence seizure**. GoF median onset was 1 month versus 16 months for LoF. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Hypotonia:** 13/25, enriched among LoF cases. HPO: **Muscular hypotonia (HP:0001252)**. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Hypertonia/spasticity/hyperreflexia:** 10/25, enriched among GoF cases. HPO: **Hypertonia (HP:0001276), Hyperreflexia (HP:0001347), Spasticity (HP:0001257)**. Hypertonia can be congenital, as in the p.Met661Thr girl. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, okano2023gria3p.met661thrvariant pages 1-3)
- **Movement disorder:** 14/25; hyperekplexia or nonepileptic erratic myoclonus in 8/25. HPO: **Movement abnormality (HP:0100022), Hyperekplexia (HP:0002169), Myoclonus (HP:0001336), Chorea (HP:0002072)**. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Sleep disturbance:** particularly associated with LoF. Two p.Ala653Thr brothers remained awake for up to **106 hours** and slept for up to **48 hours**. HPO: **Abnormal sleep pattern (HP:0002360), Sleep–wake cycle disturbance**. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, davies2017apointmutation pages 1-2)
- **Behavioral/psychiatric manifestations:** autism, self-injury, aggression, emotional instability, psychosis-like symptoms, hallucinations, and spatial-memory deficits have been reported. In one Finnish family, three adult males had severe ID, autistic features, self-injury, and aggressive outbursts. Suggested HPO: **Autistic behavior (HP:0000729), Aggressive behavior (HP:0000718), Self-injurious behavior (HP:0100716), Psychotic episodes (HP:0000725)**. (hu2026reclassificationofthe pages 4-5, philips2014xexomesequencingin pages 4-6)
- **Brain abnormalities:** reported findings include cerebellar hypoplasia, cerebral or frontal atrophy, and ventricular enlargement, but imaging may be normal. Suggested HPO: **Cerebellar hypoplasia (HP:0001321), Cerebral atrophy (HP:0002059), Ventriculomegaly (HP:0002119)**. In the p.Met661Thr case, slight frontal atrophy and ventricular enlargement were not progressive at age 13. (rinaldi2022myoclonicstatusepilepticus pages 1-2, okano2023gria3p.met661thrvariant pages 1-3)
- **Motor/orthopedic consequences:** delayed milestones, impaired gait, scoliosis, hip dislocation, and bedridden status can occur in severe disease. HPO: **Delayed gross motor development (HP:0002194), Gait disturbance (HP:0001288), Scoliosis (HP:0002650), Hip dislocation (HP:0002827)**. (okano2023gria3p.met661thrvariant pages 1-3)
- **Growth/dysmorphism:** short stature, macrocephaly, constitutional weakness, and variable facial dysmorphism have been described but are not universal. The p.Met661Thr girl lacked characteristic facies. (rinaldi2022myoclonicstatusepilepticus pages 1-2, jiang2023geneticanalysisand pages 1-2, okano2023gria3p.met661thrvariant pages 1-3)

**Quality of life:** No validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was identified. Nevertheless, severe cognitive and language impairment, refractory epilepsy, abnormal tone, impaired mobility, behavioral dysregulation, and sleep disruption can substantially restrict communication, education, autonomy, and caregiver sleep. This functional impact is inferred from case descriptions rather than standardized instruments.

## 4. Genetic and molecular information

- **Causal gene:** **GRIA3**; protein GluA3/GluR3; Xq25; OMIM *305915. HGNC numerical identifier was not verified in the retrieved sources. (okano2023gria3p.met661thrvariant pages 1-3)
- **Origin:** Germline. Both inherited and de novo disease occur. No evidence supports a somatic disease mechanism.
- **Inheritance:** Historically X-linked recessive/semidominant. Hemizygous males frequently inherit LoF alleles from clinically healthy mothers; however, de novo hemizygous male disease and heterozygous female disease are established. Nearly all affected females in the recent cohort carried de novo heterozygous GoF variants. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Functional consequences:** LoF mechanisms include disrupted transcription/splicing, reduced protein stability, reduced ion permeation, or stabilization of a closed channel. GoF commonly prolongs receptor activation by slowing deactivation/desensitization. Both too little and too much AMPAR activity can impair neurodevelopment. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, davies2017apointmutation pages 1-2, hamanaka2022ameliorationofa pages 1-2)
- **Population frequency:** Individual disease alleles are generally absent or extremely rare in population databases. Absence from gnomAD was documented for c.268+1G>C and p.Met661Thr. Exact allele frequencies for every reported variant were not available. (hu2026reclassificationofthe pages 4-5, okano2023gria3p.met661thrvariant pages 1-3)
- **ACMG classification:** Classification must be variant-specific. Functional electrophysiology, RNA studies, segregation, de novo status, and population absence are particularly valuable. A functionally neutral rare missense allele should not automatically be labeled pathogenic. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
- **Modifier genes:** None validated.
- **Epigenetics:** Skewed X-chromosome inactivation is a plausible determinant of female severity, but no reproducible disease-specific methylation episignature has been established. (rubino2025nonconvulsivestatusepilepticus pages 7-8, hu2026reclassificationofthe pages 1-2)
- **Chromosomal abnormalities:** GRIA3-disrupting translocations, deletions, duplications, and multi-exon copy-number changes are reported. Some Xq25 duplications may include neighboring genes, complicating attribution.

## 5. Environmental information

No toxin, radiation exposure, pollutant, lifestyle behavior, nutritional deficiency, or infectious agent is known to cause GRIA3-related XLID94. Consequently, CTD-style chemical–disease causality and pathogen annotations are not currently justified. Routine avoidance of neurotoxic exposures is sensible general care but is not disease-specific prevention.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline **GRIA3 sequence or structural variant** leads to altered GluA3 abundance, assembly, trafficking, or channel gating.
2. Altered GluA3 leads to **LoF or GoF of GluA3-containing AMPA receptors** at postsynaptic membranes.
3. LoF leads to reduced/abnormally brief excitatory currents, whereas GoF leads to prolonged or excessive currents through slowed deactivation/desensitization.
4. Abnormal AMPAR current leads to disturbed excitatory synaptic transmission, synaptic plasticity, and excitation–inhibition balance in developing neural circuits.
5. Circuit dysfunction leads to impaired learning, memory, language, motor development, behavior, and sleep regulation; excessive or mistimed excitation can lead to epilepsy and hypertonic/hyperkinetic phenotypes.
6. **Inferred branch:** chronic synaptic dysfunction leads to region- and age-specific transcriptional and proteomic adaptation in neurons and glia, potentially contributing to psychiatric and behavioral manifestations.

### Mechanistic detail

AMPARs are glutamate-gated cation channels assembled as tetramers from GluA1–GluA4. GluA3-containing receptors are concentrated at the postsynaptic density and participate in rapid excitatory transmission and activity-dependent plasticity. In hippocampus, GluA2/3 is the second major AMPAR population after GluA1/2. Suggested GO terms include **AMPA glutamate receptor activity (GO:0004971), ionotropic glutamate receptor signaling pathway (GO:0035235), chemical synaptic transmission (GO:0007268), regulation of synaptic plasticity (GO:0048167), learning or memory (GO:0007611), and transmembrane ion transport (GO:0034220)**. (okano2023gria3p.met661thrvariant pages 1-3, spek2022expressionandinteraction pages 1-2)

The strongest genotype-specific human mechanism comes from electrophysiology. p.Ala653Thr stabilized a closed channel, while p.Ala615Val slowed desensitization and deactivation and behaved as GoF. In the large 2024 study, 31/44 tested rare variants altered function, establishing bidirectional channel dysfunction rather than uniform haploinsufficiency. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, davies2017apointmutation pages 1-2, hamanaka2022ameliorationofa pages 1-2)

Interaction proteomics showed that hippocampal GluA2/3 receptors preferentially co-purify with **CNIH2, CACNG2/TARP-γ2 (stargazin), and OLFM1/Noelin-1**, proteins affecting receptor biogenesis, trafficking, surface expression, mobility, and gating. Relevant compartments are **postsynaptic membrane (GO:0045211), postsynaptic density (GO:0014069), AMPA glutamate receptor complex (GO:0032281), neuronal synapse (GO:0098984), and plasma membrane**. (spek2022expressionandinteraction pages 1-2)

A 2024 mouse preprint found downregulated activity-regulated genes in cortical regions and region-specific immune-, glial-, and oligodendrocyte-related changes after a Gria3 protein-truncating mutation. Across six regions there were 148 unique differentially expressed genes at one month and 201 at three months. This supports downstream network adaptation but remains **non-peer-reviewed** and models schizophrenia-associated Gria3 LoF rather than XLID94 directly. (huang2024brainregionspecificchangesand pages 1-3)

No disease-specific human metabolomic, lipidomic, single-cell, spatial-transcriptomic, or methylation signature was identified. There is no established primary immune, inflammatory, apoptotic, autophagic, mitochondrial, or metabolic lesion. Any glial/immune signal presently appears downstream and model-derived.

**Suggested cell ontology annotations:** neuron (**CL:0000540**), glutamatergic neuron (**CL:0000679**), cerebral-cortex neuron, hippocampal neuron, thalamic neuron, spinal motor neuron, oligodendrocyte (**CL:0000128**), astrocyte (**CL:0000127**), and microglial cell (**CL:0000129**). Direct disease causality is strongest for neurons; glial annotations are based mainly on mouse profiling.

## 7. Anatomical structures affected

- **Primary organ/system:** central nervous system and nervous system.
- **Brain regions implicated clinically or experimentally:** cerebral cortex, frontal/prefrontal cortex, hippocampus, thalamus, striatum, cerebellum, substantia nigra, and sleep/circadian circuits. GluA3-containing AMPARs are broadly distributed, especially in hippocampus, cortex, and thalamus. (huang2024brainregionspecificchangesand pages 1-3, okano2023gria3p.met661thrvariant pages 1-3)
- **Peripheral/secondary structures:** corticospinal and motor systems are implicated by hypertonia, hyperreflexia, gait abnormalities, scoliosis, and hip dislocation; these musculoskeletal changes are likely secondary to neurologic impairment. (okano2023gria3p.met661thrvariant pages 1-3)
- **Subcellular localization:** postsynaptic plasma membrane, postsynaptic density, AMPAR tetramer, dendritic/synaptic compartments; ER-associated biogenesis and receptor trafficking are relevant upstream processes. (spek2022expressionandinteraction pages 1-2)
- **Suggested UBERON terms:** brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), hippocampal formation (**UBERON:0002421**), thalamus (**UBERON:0001897**), striatum (**UBERON:0002435**), cerebellum (**UBERON:0002037**), spinal cord (**UBERON:0002240**), and skeletal muscle (**UBERON:0001134**, secondary involvement).
- **Lateralization:** No consistent unilateral or asymmetric pattern is established.

## 8. Temporal development

The disorder begins prenatally at the molecular level and manifests congenitally or during infancy/early childhood. Developmental delay is chronic and usually recognized as milestones are missed. GoF disease can present with neonatal hypertonia and seizures in the first months; LoF-associated seizures tend to begin later, with cohort medians of 1 versus 16 months respectively. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, okano2023gria3p.met661thrvariant pages 1-3)

There is no validated staging system. The typical course is lifelong developmental impairment with variable evolution of seizures, tone, movement symptoms, behavior, and sleep. Structural brain findings are not necessarily progressive: slight frontal atrophy/ventricular enlargement in one girl had not worsened by age 13. Adult familial cases demonstrate survival into at least the fifth decade, but longitudinal data remain sparse. (philips2014xexomesequencingin pages 4-6, okano2023gria3p.met661thrvariant pages 1-3)

No spontaneous molecular remission is expected. Seizures and psychiatric symptoms can improve with treatment. Early childhood is plausibly a critical intervention period because AMPARs influence neural-circuit development, but no trial has established a disease-specific therapeutic window.

## 9. Inheritance and population

### Epidemiology

No population-based prevalence, incidence, geographic-distribution, or carrier-frequency estimate was identified. Published patients number in the dozens, indicating an ultra-rare disorder, but ascertainment and functional reclassification are still evolving. A prevalence “per 100,000” cannot be responsibly calculated from case reports.

### Genetic epidemiology

- **Pattern:** X-linked with sex- and mechanism-dependent expression; “X-linked recessive” describes many familial LoF pedigrees but is incomplete for de novo GoF disease in females. (rinaldi2024gainoffunctionandlossoffunction pages 1-3, hu2026reclassificationofthe pages 1-2)
- **Sex ratio:** Historically strongly male-biased. By 2023, only five affected females had been highlighted in one review of approximately 20 reported variants; newer cohorts establish female disease more firmly. (okano2023gria3p.met661thrvariant pages 1-3)
- **Penetrance:** Apparently high in hemizygous males carrying clearly pathogenic alleles, but exact penetrance is unknown. Heterozygous female penetrance is variable, likely influenced by variant mechanism and X inactivation.
- **Expressivity:** Markedly variable, ranging from moderate ID and sleep disturbance to profound developmental and epileptic encephalopathy.
- **Anticipation:** Not reported; no repeat expansion is involved.
- **Mosaicism/germline mosaicism:** Theoretically possible for de novo variants, but no quantified recurrence risk or proven recurrent germline mosaicism was identified.
- **Founder effect/consanguinity:** No established founder allele; consanguinity is not a characteristic risk because the disorder is X-linked.
- **Ethnicity/geography:** Families have been reported from multiple populations, including Chinese, Japanese, Finnish, and Italian cohorts, without demonstrated population enrichment. (rinaldi2022myoclonicstatusepilepticus pages 1-2, philips2014xexomesequencingin pages 4-6, jiang2023geneticanalysisand pages 1-2, okano2023gria3p.met661thrvariant pages 1-3)

## 10. Diagnostics

### Clinical evaluation

There are no disease-specific consensus clinical criteria. Suspicion should arise in a child—especially a boy—with unexplained developmental delay/ID plus epilepsy, hypotonia or hypertonia, myoclonus/hyperekplexia, disturbed sleep, autism/aggression, or an X-linked family history.

Recommended phenotyping includes neurologic and developmental examination, standardized cognitive/adaptive assessment, speech-language evaluation, movement-disorder assessment, sleep history, hearing/vision assessment, and psychiatric/behavioral review. EEG is indicated for seizures or episodic events. Brain MRI may identify cerebellar hypoplasia, cerebral/frontal atrophy, or ventriculomegaly but is not a molecular biomarker. (rinaldi2022myoclonicstatusepilepticus pages 1-2, okano2023gria3p.met661thrvariant pages 1-3)

No diagnostic blood chemistry, enzyme assay, metabolite, protein biomarker, biopsy, EMG pattern, or histopathologic criterion is established.

### Genetic testing strategy

1. **First-line:** trio WES or WGS with single-nucleotide, indel, and copy-number calling; alternatively, a comprehensive neurodevelopmental/epilepsy panel including **GRIA3**.
2. **Confirm:** Sanger confirmation and family segregation analysis.
3. **CNV-sensitive testing:** exon-level deletion/duplication analysis, MLPA/qPCR, read-depth CNV calling, or chromosomal microarray. Standard exome SNV analysis can miss multi-exon deletions. The Chinese exon 5–12 deletion was identified only after targeted comprehensive testing following unrevealing SNV/indel analysis. (jiang2023geneticanalysisand pages 1-2)
4. **RNA studies:** patient RNA, RT-PCR, or a minigene assay can resolve splice VUS; c.268+1G>C was upgraded after demonstration of exon-2 skipping. (hu2026reclassificationofthe pages 4-5, hu2026reclassificationofthe pages 1-2)
5. **Functional electrophysiology:** useful in research/advanced diagnostics for missense VUS because LoF, GoF, and apparently neutral variants coexist. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)
6. **CMA/karyotype/FISH:** appropriate when a large Xq25 rearrangement is suspected or exome/genome analysis indicates a structural lesion.
7. **Not routinely relevant:** mitochondrial sequencing and repeat-expansion testing unless the broader differential diagnosis warrants them.

The p.Met661Thr case illustrates a typical workflow: microarray was negative, trio WES detected a de novo heterozygous variant, population databases were negative, and ACMG evidence supported likely pathogenicity. (okano2023gria3p.met661thrvariant pages 1-3)

### Differential diagnosis

Important alternatives include other GRIA-related disorders (**GRIA1, GRIA2, GRIA4**), NMDA-receptor disorders, DLG3-related XLID, creatine-transporter deficiency, fragile X syndrome, MECP2-related disease, FOXG1 syndrome, STXBP1/SCN2A-related developmental epileptic encephalopathy, and other X-linked ID genes. Distinguishing evidence is a pathogenic GRIA3 variant with segregation and, for missense variants, compatible functional data.

### Screening

GRIA3 disease is not included in routine newborn biochemical screening. Cascade testing of at-risk maternal relatives is appropriate after identifying a familial allele. Carrier, prenatal, and preimplantation genetic testing are technically feasible. Amniotic-fluid testing successfully detected the familial exon 5–12 deletion in one fetus. (jiang2023geneticanalysisand pages 1-2)

## 11. Outcome and prognosis

No survival curve, standardized mortality rate, or life-expectancy estimate exists. Adult affected males aged 35–57 years were described in a Finnish family, showing that survival into later adulthood is possible, but this does not establish normal life expectancy. (philips2014xexomesequencingin pages 4-6)

The major morbidity is lifelong neurodevelopmental disability. Severe cases may remain nonverbal or bedridden and develop orthopedic complications. Epilepsy may be drug-resistant, although control can improve over time; psychiatric and sleep symptoms can require long-term treatment. (hu2026reclassificationofthe pages 4-5, okano2023gria3p.met661thrvariant pages 1-3)

Potential prognostic indicators are **functional variant class and sex**: GoF correlates with earlier seizures, hypertonia, movement disorders, and greater severity; LoF correlates with later seizures, hypotonia, and sleep disturbance. These are cohort-level associations, not deterministic predictions for an individual. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)

No validated molecular prognostic biomarker or quality-of-life instrument has been developed. Recovery of established intellectual disability has not been demonstrated; functional gains are expected mainly through developmental therapies and control of seizures, tone, sleep, and behavior.

## 12. Treatment

There is no approved GRIA3 disease-modifying therapy and no disease-specific randomized trial was identified. Management is multidisciplinary and phenotype-directed.

### Pharmacotherapy

- **Epilepsy:** standard antiseizure treatment guided by seizure type and EEG. In the p.Met661Thr girl, carbamazepine and ethosuximide were ineffective, while lamotrigine, clobazam, levetiracetam, and lacosamide gradually improved control. (okano2023gria3p.met661thrvariant pages 1-3)
- **Mechanism-informed GoF treatment:** in one boy with p.Ala615Val GoF, carbamazepine—described by the authors as suppressing presynaptic glutamate release—ameliorated both seizures and hypertonia. This is a single case, not evidence for universal efficacy, and contrasts with carbamazepine failure in another unfunctionally characterized allele. (okano2023gria3p.met661thrvariant pages 1-3, hamanaka2022ameliorationofa pages 1-2)
- **Psychiatric/sleep symptoms:** risperidone and clozapine reportedly improved psychiatric manifestations, and lorazepam improved sleep in one family. These observations are uncontrolled. (hu2026reclassificationofthe pages 4-5)
- **AMPAR modulators:** positive modulators and antagonists normalized selected variant currents in experimental assays, but no compound has established clinical efficacy in XLID94. Variant direction must be known because enhancing a GoF receptor or inhibiting a LoF receptor could be harmful. (xiangwei2023clinicalandfunctional pages 1-6)

Suggested NCIt concepts include **Anticonvulsant Therapy, Carbamazepine, Levetiracetam, Lamotrigine, Clobazam, Lacosamide, Antipsychotic Agent, Physical Therapy, Occupational Therapy, Speech and Language Therapy, and Genetic Counseling**. Exact NCIt numerical codes should be verified directly before database ingestion.

### Supportive and rehabilitative care

Early-intervention services, individualized education, speech/augmentative communication therapy, occupational and physical therapy, tone management, mobility equipment, orthopedic surveillance, behavioral therapy, sleep intervention, nutritional assessment, and caregiver support are appropriate. Epilepsy rescue planning and sudden-death risk counseling should follow general epilepsy standards.

There is no established role for surgery except treatment of complications such as hip dislocation or scoliosis. No gene replacement, CRISPR, antisense, cell therapy, RNA therapy, immunotherapy, or pharmacogenomic guideline is available for GRIA3 disease.

## 13. Prevention

The causal germline variant cannot be prevented by lifestyle modification, vaccination, or exposure avoidance.

- **Primary prevention:** genetic counseling and reproductive options for known carrier families, including preimplantation genetic testing, chorionic-villus sampling, amniocentesis, or use of donor gametes.
- **Secondary prevention:** prompt genetic diagnosis, cascade testing, early developmental intervention, and surveillance for epilepsy, movement disorder, sleep disturbance, and behavioral illness.
- **Tertiary prevention:** seizure control, aspiration and injury prevention, contracture/orthopedic management, communication support, and caregiver education.

For a carrier mother, each pregnancy has a 50% probability of transmitting the variant; expected clinical consequences depend on fetal sex, variant mechanism, and—among females—X inactivation. A de novo result lowers but does not eliminate recurrence because parental germline mosaicism cannot be excluded. The 2023 family report demonstrates technical feasibility of prenatal detection but should not be treated as a population-screening recommendation. (jiang2023geneticanalysisand pages 1-2)

No vaccine, prophylactic drug, public-health sanitation measure, or environmental intervention is disease-specific.

## 14. Other species and natural disease

- **Mouse:** *Mus musculus*, NCBI Taxonomy **10090**; ortholog **Gria3**.
- **Fruit fly:** *Drosophila melanogaster*, NCBI Taxonomy **7227**; used as a transgenic expression system for human mutant GluA3.
- **Human:** *Homo sapiens*, NCBI Taxonomy **9606**.

No naturally occurring veterinary disease equivalent was identified in companion animals, livestock, or wildlife. There is no transmission or zoonotic potential. Comparative relevance derives from evolutionary conservation of AMPAR channel architecture and synaptic function rather than natural cross-species disease.

## 15. Model organisms and experimental systems

### Mouse models

- **Gria3 knockout mice:** Germline hemizygous knockout mice showed increased aggression, sociality, peripheral activity, minor motor/balance deficits, elevated striatal dopamine, and reduced olfactory-bulb serotonin turnover. They did not reproduce the profound human intellectual disability phenotype, limiting face validity, but support roles in behavior, motor control, and monoaminergic circuitry. (adamczyk2012glua3deficiencyinmice pages 1-3)
- **p.Ala653Thr CRISPR knock-in:** Reproduced altered sleep/activity architecture and enhanced light-induced period lengthening, providing unusually strong allele-specific human–mouse concordance for sleep regulation. (davies2017apointmutation pages 1-2)
- **Protein-truncating Gria3 model:** Multi-region RNA-seq and synaptic proteomics revealed age- and region-dependent activity-regulated, glial, immune, oligodendrocyte, and synaptic changes. Because this was a 2024 bioRxiv preprint and modeled a schizophrenia-associated PTV, extrapolation to XLID94 should remain cautious. (huang2024brainregionspecificchangesand pages 1-3)

### Cellular and invertebrate systems

- **HEK293/heterologous cells and Xenopus oocytes:** Used for patch clamp or voltage clamp to measure current amplitude, agonist potency, desensitization, deactivation, and pharmacologic rescue. These systems define LoF versus GoF but lack native neuronal development and circuit context. (xiangwei2023clinicalandfunctional pages 1-6, hamanaka2022ameliorationofa pages 1-2)
- **Minigene assay:** HEK293T testing demonstrated exon-2 skipping from c.268+1G>C. It validates aberrant splicing but not tissue-specific transcript abundance. (hu2026reclassificationofthe pages 4-5)
- **Drosophila transgenics:** Co-expression of p.Ala615Val with the leaky Lurcher alteration produced developmental defects, supporting GoF interaction. Species and receptor-composition differences limit direct clinical translation. (hamanaka2022ameliorationofa pages 1-2)
- **Mouse hippocampal interaction proteomics:** Defined GluA2/3-associated CNIH2, TARP-γ2, and OLFM1 complexes and provides a resource for studying trafficking/gating modifiers. (spek2022expressionandinteraction pages 1-2)

No patient-derived iPSC neuron, brain organoid, rat, zebrafish, or *C. elegans* XLID94 model was identified in the retrieved evidence. Such models would be valuable for developmental timing, cell-type specificity, X-inactivation in females, and allele-specific drug screening.

## Recent developments and expert interpretation

The decisive recent advance is the online-December-2023/2024-volume *Brain* study demonstrating that GRIA3 disease is not a unitary haploinsufficiency syndrome. Its abstract states: **“Thirty-one variants alter receptor function and show loss-of-function (LoF) or gain-of-function (GoF) properties, whereas 13 appeared neutral.”** It further reports that **“GoF variants were associated with more severe outcomes,”** with median seizure onset at one month versus 16 months for LoF. This functional taxonomy should now guide variant interpretation, prognosis, and any future precision therapy. (rinaldi2024gainoffunctionandlossoffunction pages 1-3)

A second advance is recognition of affected females. The 2023 p.Met661Thr report states: **“Here, we report a female patient with developmental and epileptic encephalopathy who carries the novel de novo GRIA3 variant.”** Together with the multicenter cohort, this argues against excluding GRIA3 because the patient is female. (okano2023gria3p.met661thrvariant pages 1-3)

A third advance is preliminary precision pharmacology. Hamanaka and colleagues concluded that **“drugs suppressing glutamatergic neurotransmission may ameliorate this phenotype”** after carbamazepine improved a GoF case. This is biologically coherent but remains an N-of-1 observation, and the contrasting failure of carbamazepine in another patient demonstrates that treatment cannot yet be generalized without variant-level functional evidence. (okano2023gria3p.met661thrvariant pages 1-3, hamanaka2022ameliorationofa pages 1-2)

Finally, 2024 mouse multi-omics suggests that primary AMPAR dysfunction generates broader, brain-region-specific neuronal and glial adaptations. This is hypothesis-generating rather than clinically validated because the study was not peer reviewed and did not directly model every XLID94 allele. (huang2024brainregionspecificchangesand pages 1-3)

## Evidence limitations

The evidence base remains small and vulnerable to referral, publication, and ascertainment bias. Phenotype frequencies come from 25 patients, standardized natural-history and quality-of-life studies are absent, and many alleles lack electrophysiologic validation. No prevalence, mortality, penetrance, carrier-frequency, formal diagnostic guideline, randomized treatment trial, or approved targeted therapy is available. PMIDs were not present in the retrieved full-text metadata; therefore, DOI URLs and publication dates are supplied rather than risking incorrect PMID assignment. The 2012 article proposing GRIA3 silencing through an upstream noncoding duplication was explicitly retrieved as **retracted** and was not used as affirmative evidence.

References

1. (rinaldi2024gainoffunctionandlossoffunction pages 1-3): Berardo Rinaldi, Allan Bayat, Linda G Zachariassen, Jia-Hui Sun, Yu-Han Ge, Dan Zhao, Kristine Bonde, Laura H Madsen, Ilham Abdimunim Ali Awad, Duygu Bagiran, Amal Sbeih, Syeda Maidah Shah, Shaymaa El-Sayed, Signe M Lyngby, Miriam G Pedersen, Charlotte Stenum-Berg, Louise Claudia Walker, Ilona Krey, Andrée Delahaye-Duriez, Lisa T Emrick, Krystal Sully, Chaya N Murali, Lindsay C Burrage, Julie Ana Plaud Gonzalez, Mered Parnes, Jennifer Friedman, Bertrand Isidor, Jérémie Lefranc, Sylvia Redon, Delphine Heron, Cyril Mignot, Boris Keren, Mélanie Fradin, Christele Dubourg, Sandra Mercier, Thomas Besnard, Benjamin Cogne, Wallid Deb, Clotilde Rivier, Donatella Milani, Maria Francesca Bedeschi, Claudia Di Napoli, Federico Grilli, Paola Marchisio, Suzanna Koudijs, Danielle Veenma, Emanuela Argilli, Sally Ann Lynch, Ping Yee Billie Au, Fernando Eduardo Ayala Valenzuela, Carolyn Brown, Diane Masser-Frye, Marilyn Jones, Leslie Patron Romero, Wenhui Laura Li, Erin Thorpe, Laura Hecher, Jessika Johannsen, Jonas Denecke, Vanda McNiven, Anna Szuto, Emma Wakeling, Vincent Cruz, Valerie Sency, Heng Wang, Juliette Piard, Fanny Kortüm, Theresia Herget, Tatjana Bierhals, Angelo Condell, Bruria Ben Zeev, Simranpreet Kaur, John Christodoulou, Amelie Piton, Christiane Gertrud Zweier, Cornelia Kraus, Alessia Micalizzi, Marina Trivisano, Nicola Specchio, Gaetan Lesca, Rikke S Møller, Zeynep Tümer, Maria Musgaard, Benedicte Gerard, Johannes R Lemke, Yun Stone Shi, and Anders S Kristensen. Gain-of-function and loss-of-function variants in gria3 lead to distinct neurodevelopmental phenotypes. Brain : a journal of neurology, Dec 2024. URL: https://doi.org/10.1093/brain/awad403, doi:10.1093/brain/awad403. This article has 40 citations.

2. (jiang2023geneticanalysisand pages 1-2): Yanting Jiang. Genetic analysis and prenatal diagnosis of a chinese pedigree affected with syndromic x-linked intellectual disability 94 due to exon 5-12 deletion in gria3 gene. Sep 2023. URL: https://doi.org/10.26717/bjstr.2023.52.008322, doi:10.26717/bjstr.2023.52.008322. This article has 0 citations.

3. (okano2023gria3p.met661thrvariant pages 1-3): Satomi Okano, Yoshio Makita, Akie Miyamoto, Genya Taketazu, Kayano Kimura, Ikue Fukuda, Hajime Tanaka, Kumiko Yanagi, and Tadashi Kaname. Gria3 p.met661thr variant in a female with developmental epileptic encephalopathy. Human Genome Variation, Feb 2023. URL: https://doi.org/10.1038/s41439-023-00232-1, doi:10.1038/s41439-023-00232-1. This article has 10 citations.

4. (hamanaka2022ameliorationofa pages 1-2): Kohei Hamanaka, Keita Miyoshi, Jia-Hui Sun, Keisuke Hamada, Takao Komatsubara, Ken Saida, Naomi Tsuchida, Yuri Uchiyama, Atsushi Fujita, Takeshi Mizuguchi, Benedicte Gerard, Allan Bayat, Berardo Rinaldi, Mitsuhiro Kato, Jun Tohyama, Kazuhiro Ogata, Yun Stone Shi, Kuniaki Saito, Satoko Miyatake, and Naomichi Matsumoto. Amelioration of a neurodevelopmental disorder by carbamazepine in a case having a gain-of-function gria3 variant. Human Genetics, 141:283-293, Jan 2022. URL: https://doi.org/10.1007/s00439-021-02416-7, doi:10.1007/s00439-021-02416-7. This article has 14 citations and is from a peer-reviewed journal.

5. (davies2017apointmutation pages 1-2): Benjamin Davies, Laurence A Brown, Ondrej Cais, Jake Watson, Amber J Clayton, Veronica T Chang, Daniel Biggs, Christopher Preece, Polinka Hernandez-Pliego, Jon Krohn, Amarjit Bhomra, Stephen R F Twigg, Andrew Rimmer, Alexander Kanapin, Arjune Sen, Zenobia Zaiwalla, Gil McVean, Russell Foster, Peter Donnelly, Jenny C Taylor, Edward Blair, David Nutt, A Radu Aricescu, Ingo H Greger, Stuart N Peirson, Jonathan Flint, and Hilary C Martin. A point mutation in the ion conduction pore of ampa receptor gria3 causes dramatically perturbed sleep patterns as well as intellectual disability. Human Molecular Genetics, 26:3869-3882, Jul 2017. URL: https://doi.org/10.1093/hmg/ddx270, doi:10.1093/hmg/ddx270. This article has 66 citations and is from a domain leading peer-reviewed journal.

6. (adamczyk2012glua3deficiencyinmice pages 1-3): Abby Adamczyk, Rebeca Mejias, Kogo Takamiya, Jennifer Yocum, Irina N. Krasnova, Juan Calderon, Jean Lud Cadet, Richard L. Huganir, Mikhail V. Pletnikov, and Tao Wang. Glua3-deficiency in mice is associated with increased social and aggressive behavior and elevated dopamine in striatum. Behavioural Brain Research, 229:265-272, Apr 2012. URL: https://doi.org/10.1016/j.bbr.2012.01.007, doi:10.1016/j.bbr.2012.01.007. This article has 96 citations and is from a peer-reviewed journal.

7. (spek2022expressionandinteraction pages 1-2): Sophie J. F. van der Spek, Nikhil J. Pandya, Frank Koopmans, Iryna Paliukhovich, Roel C. van der Schors, Mylene Otten, August B. Smit, and Ka Wan Li. Expression and interaction proteomics of glua1- and glua3-subunit-containing ampars reveal distinct protein composition. Cells, 11(22):3648, Nov 2022. URL: https://doi.org/10.3390/cells11223648, doi:10.3390/cells11223648. This article has 23 citations.

8. (huang2024brainregionspecificchangesand pages 1-3): Wei-Chao Huang, Ryan Kast, Kira Perzel Mandell, Borislav Dejanovic, Kevin Bonanno, Sameer Aryal, Zohreh Farsi, Jonathan Wilde, Dongqing Wang, Xian Gao, Hasmik Keshishian, Steven A. Carr, Guoping Feng, and Morgan Sheng. Brain-region-specific changes and dysregulation of activity regulated genes in gria3 mutant mice, a genetic animal model of schizophrenia. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.15.623468, doi:10.1101/2024.11.15.623468. This article has 4 citations.

9. (hu2026reclassificationofthe pages 1-2): Lina Hu, Yuqiong Chai, Xiaofei Liu, Yanan Wang, and Hongwei Jiang. Reclassification of the gria3 splice-site variant in an x-linked family with intellectual disability and psychiatric symptoms. Frontiers in Genetics, Aug 2026. URL: https://doi.org/10.3389/fgene.2026.1914453, doi:10.3389/fgene.2026.1914453. This article has 0 citations and is from a peer-reviewed journal.

10. (hu2026reclassificationofthe pages 4-5): Lina Hu, Yuqiong Chai, Xiaofei Liu, Yanan Wang, and Hongwei Jiang. Reclassification of the gria3 splice-site variant in an x-linked family with intellectual disability and psychiatric symptoms. Frontiers in Genetics, Aug 2026. URL: https://doi.org/10.3389/fgene.2026.1914453, doi:10.3389/fgene.2026.1914453. This article has 0 citations and is from a peer-reviewed journal.

11. (rinaldi2022myoclonicstatusepilepticus pages 1-2): Berardo Rinaldi, Yu-Han Ge, Elena Freri, Arianna Tucci, Tiziana Granata, Margherita Estienne, Jia-Hui Sun, Bénédicte Gérard, Allan Bayat, Stephanie Efthymiou, Cristina Gervasini, Yun Stone Shi, Henry Houlden, Paola Marchisio, and Donatella Milani. Myoclonic status epilepticus and cerebellar hypoplasia associated with a novel variant in the gria3 gene. Neurogenetics, 23:27-35, Nov 2022. URL: https://doi.org/10.1007/s10048-021-00666-1, doi:10.1007/s10048-021-00666-1. This article has 10 citations and is from a peer-reviewed journal.

12. (philips2014xexomesequencingin pages 4-6): Anju K Philips, Auli Sirén, Kristiina Avela, Mirja Somer, Maarit Peippo, Minna Ahvenainen, Fatma Doagu, Maria Arvio, Helena Kääriäinen, Hilde Van Esch, Guy Froyen, Stefan A Haas, Hao Hu, Vera M Kalscheuer, and Irma Järvelä. X-exome sequencing in finnish families with intellectual disability - four novel mutations and two novel syndromic phenotypes. Orphanet Journal of Rare Diseases, 9:49-49, Apr 2014. URL: https://doi.org/10.1186/1750-1172-9-49, doi:10.1186/1750-1172-9-49. This article has 102 citations and is from a peer-reviewed journal.

13. (rubino2025nonconvulsivestatusepilepticus pages 7-8): Alfonso Rubino, Giorgia Bruno, Gabriella Errichiello, Fabio Acquaviva, Daniele De Brasi, Alfonsina Tirozzi, Pia Santangelo, Carmela Russo, Antonio Varone, Geremia Zito Marinosci, and Pia Bernardo. Non-convulsive status epilepticus and mild neurodevelopmental phenotype in a female with a novel p.thr657ala variant in the gria3 gene. Children, 12(12):1654, Dec 2025. URL: https://doi.org/10.3390/children12121654, doi:10.3390/children12121654. This article has 0 citations.

14. (xiangwei2023clinicalandfunctional pages 1-6): Wenshu XiangWei, Riley E. Perszyk, Nana Liu, Yuchen Xu, Subhrajit Bhattacharya, Gil H. Shaulsky, Constance Smith-Hicks, Ali Fatemi, Andrew E. Fry, Kate Chandler, Tao Wang, Julie Vogt, Julie S. Cohen, Alex R. Paciorkowski, Annapurna Poduri, Yuehua Zhang, Shuang Wang, Yuping Wang, Qiongxiang Zhai, Fang Fang, Jie Leng, Kathryn Garber, Scott J. Myers, Robin-Tobias Jauss, Kristen L. Park, Timothy A. Benke, Johannes R. Lemke, Hongjie Yuan, Yuwu Jiang, and Stephen F. Traynelis. Clinical and functional consequences of gria variants in patients with neurological diseases. Cellular and Molecular Life Sciences, Nov 2023. URL: https://doi.org/10.1007/s00018-023-04991-6, doi:10.1007/s00018-023-04991-6. This article has 22 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Syndromic_X-linked_Intellectual_Disability_94-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.