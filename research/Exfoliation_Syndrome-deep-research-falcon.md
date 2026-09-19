---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T23:23:55.586851'
end_time: '2026-09-04T23:35:54.267271'
duration_seconds: 718.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Exfoliation Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 52
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 2
  verified: 2
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
  path: Exfoliation_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Exfoliation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Exfoliation Syndrome** covering all of the
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
- **Disease Name:** Exfoliation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Exfoliation Syndrome** covering all of the
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


# Exfoliation Syndrome: Disease Characteristics Research Report

**Scope.** This report distinguishes **exfoliation syndrome (XFS)**—the matrix-deposition disorder—from **exfoliation glaucoma (XFG)**, its major sight-threatening complication. Evidence labels used below are **human clinical**, **human observational**, **human molecular**, **in vitro**, **animal model**, or **computational**. Associations are not described as causal unless experimentally established.

The following table provides a knowledge-base-oriented synopsis.

| Knowledge-base domain | Evidence-based summary | Key quantitative values | Suggested ontology annotations | Evidence |
|---|---|---:|---|---|
| Identity and definition | Exfoliation syndrome (XFS; pseudoexfoliation syndrome, PXS/PEX) is a late-onset, systemic extracellular-matrix disorder characterized by progressive production and deposition of abnormal fibrillar exfoliation material, with clinically dominant manifestations in the ocular anterior segment. Exfoliation glaucoma (XFG/PXG) is the secondary open-angle glaucoma that may complicate XFS; it is not synonymous with uncomplicated XFS. | Estimated prevalence varies geographically from **<0.4% to >20%**; approximately **80 million** people may be affected worldwide. | **MONDO:0008327** exfoliation syndrome; MeSH concept: pseudoexfoliation syndrome; HPO: **HP:0003584** late onset | (li2021loxl1genepolymorphisms pages 1-2, bernstein2018exfoliationsyndromea pages 1-4, elhawy2012pseudoexfoliationsyndromea pages 1-2, OpenTargets Search: pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1) |
| Genetics | XFS is a complex, polygenic susceptibility disorder—not a proven Mendelian LOXL1 disease. Common coding and regulatory variants in **LOXL1** are the strongest replicated associations, but risk-allele reversal and high risk-allele frequencies across ancestries preclude classification as individually pathogenic variants. Additional GWAS loci include **CACNA1A, POMP, TMEM136, AGPAT1, RBMS3,** and **SEMA6A**. A rare LOXL1 coding variant was reported as protective. | 2017 GWAS: **9,035 cases and 17,008 controls** across 25 strata; initial LOXL1 SNP ORs reported in the range **2.46–20.10**. A 2021 meta-analysis included **5,022 cases and 8,962 controls**. | HGNC genes: **LOXL1, CACNA1A, POMP, TMEM136, AGPAT1, RBMS3, SEMA6A**; GO: extracellular-matrix organization, elastic-fiber assembly | (li2021loxl1genepolymorphisms pages 1-2, aung2017geneticassociationstudy pages 24-38, aboobakar2022thegeneticsof pages 6-8, OpenTargets Search: pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1) |
| Environment and gene–environment interaction | Age is the dominant non-genetic risk factor. Latitude, cold climate, greater summer outdoor exposure, reflected light over snow or water, UV-related skin-cancer history, heavy coffee intake, and low folate have observational associations. UV can induce LOXL1 and matrix responses experimentally, supporting—but not proving—a LOXL1–UV interaction. Sunglasses are a plausible protective exposure, but no intervention trial demonstrates prevention. | Each degree farther from the equator: OR **1.11** (95% CI 1.05–1.17); each additional summer outdoor hour/week: OR **1.04** (1.00–1.07); US work over snow/water: OR **3.86** (1.36–10.9); each 1% increase in sunglasses use: OR **0.98** (0.97–0.99), not replicated in Israel. | Exposure concepts: ultraviolet radiation, cold temperature, outdoor occupational exposure; CHEBI candidates for research annotation: folate, homocysteine, caffeine | (pasquale2014considerationforgeneenvironment pages 4-6, pasquale2014solarexposureand pages 1-2, pasquale2014considerationforgeneenvironment pages 2-4, kang2020cohortstudyof pages 6-7) |
| Core ocular phenotypes | Characteristic manifestations are white-gray fibrillar deposits on the anterior lens capsule and pupillary margin, iris depigmentation and peripupillary transillumination, poor pharmacologic mydriasis, trabecular hyperpigmentation, elevated or fluctuating intraocular pressure, zonular weakness, phacodonesis, lens subluxation/dislocation, cataract, and reduced corneal endothelial-cell density. Disease may appear unilateral but is often biologically asymmetric and ultimately bilateral. | Approximately **44%** has been estimated to progress to XFG, although estimates vary by cohort. | HPO suggestions: glaucoma, increased intraocular pressure, visual-field defect, cataract, lens subluxation, poor pupillary dilation, iris transillumination defect; UBERON: anterior lens capsule, iris, ciliary body, trabecular meshwork, zonular fibers, corneal endothelium | (li2021loxl1genepolymorphisms pages 1-2, rong2024lackofassociation pages 8-9, elhawy2012pseudoexfoliationsyndromea pages 1-2, borjan2023pseudoexfoliativesyndromein pages 2-3) |
| Mechanism | Genetic susceptibility and aging, potentially amplified by UV, oxidative stress, and low-grade inflammation, alter **TGF-β–LOXL1** signaling and elastic-fiber/ECM homeostasis. Increased or dysregulated matrix synthesis, LOXL1 misfolding, impaired proteasome–autophagy–lysosome clearance, mitochondrial dysfunction, and reduced antioxidant defense promote extracellular fibril accumulation. Deposits and liberated iris pigment obstruct trabecular outflow, raising intraocular pressure; sustained pressure and vascular/oxidative stress then cause retinal-ganglion-cell and optic-nerve injury. Several upstream links remain inferred rather than proven. | Early XFS aqueous-humor **IL-6 and IL-8 were about threefold higher** than controls. Lens-capsule RNA-seq identified **2,882 differentially expressed genes** in **25 XFS vs 39 controls**. | GO: extracellular-matrix organization, elastic-fiber assembly, response to oxidative stress, autophagy, lysosomal transport, mitochondrial respiratory-chain activity, TGF-β signaling; CL: lens epithelial cell, non-pigmented ciliary epithelial cell, iris pigment epithelial cell, trabecular-meshwork cell, fibroblast, retinal ganglion cell | (shyam2023geneticandepigenetic pages 43-47, bernstein2018exfoliationsyndromea pages 1-4, borras2018growthfactorsoxidative pages 8-10, mullany2022rnasequencingof pages 1-2) |
| Diagnosis | Diagnosis is clinical by slit-lamp examination before and after dilation, looking for exfoliation material, the classic lens-capsule pattern, pupillary-border deposits, poor dilation, transillumination defects, and zonular instability. Tonometry, gonioscopy, optic-disc examination, OCT retinal-nerve-fiber/ganglion-cell analysis, and automated perimetry stage ocular hypertension or XFG. There is no validated blood, genetic, omics, biopsy, imaging, or molecular test for routine diagnosis. | No standardized molecular diagnostic threshold or clinically validated predictive genetic test is available. | SNOMED/LOINC domains: slit-lamp examination, intraocular pressure, gonioscopy, automated visual-field testing, optic-nerve OCT | (rong2024lackofassociation pages 8-9, elhawy2012pseudoexfoliationsyndromea pages 1-2, aboobakar2022thegeneticsof pages 6-8, OpenTargets Search: pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1) |
| Prognosis and burden | XFS itself does not have an established disease-specific mortality effect, but it confers substantial ocular morbidity through XFG, cataract, zonular failure, and surgical complications. XFG generally has higher pressure, greater fluctuation, poorer medical response, and faster visual-field deterioration than primary open-angle glaucoma. | Three-year study: mean-deviation change **−3.17 dB** in XFG vs **−1.25 dB** in POAG; progression by guided progression analysis **58% vs 13%**. Indian tertiary cohort: XFG in **29%** of 6,284 XFS eyes and overall absolute blindness **28.2%** at presentation. | HPO: progressive visual-field loss, optic atrophy/glaucomatous optic neuropathy, visual impairment, blindness | (li2021loxl1genepolymorphisms pages 1-2, aboobakar2022thegeneticsof pages 6-8) |
| Treatment and implementation | No therapy removes exfoliation material or modifies the underlying systemic matrix disease. Uncomplicated XFS requires surveillance. XFG is treated by lowering intraocular pressure with standard topical agents, selective laser trabeculoplasty (SLT), lens extraction when indicated, trabeculectomy, drainage implants, or selected minimally invasive procedures. Cataract surgery requires anticipation of poor dilation and zonular weakness, with iris-expansion devices, capsular hooks, or capsular-tension rings as needed. | 2024 SLT series: IOP **26.7→18.9 mmHg** at 3 months, **29.2%** reduction, **69.4%** success. PreserFlo series: IOP **32.6→16.9 mmHg**, medications **3.4→1.0**, but **31%** reoperation and **17%** hypotony. Croatian registry: PEX cataract surgery cost **1.4-fold higher**. | NCIT suggestions: ophthalmic solution, selective laser trabeculoplasty, phacoemulsification, trabeculectomy, glaucoma drainage implant, minimally invasive glaucoma surgery, capsular-tension ring placement | (wakuda2024postoperativeoutcomesof pages 4-6, borjan2023pseudoexfoliativesyndromein pages 2-3, borjan2023pseudoexfoliativesyndromein pages 12-14, NCT04635020 chunk 1, NCT04416724 chunk 1) |
| Research and evidence gaps | Major gaps include the initiating lesion, functional interpretation of ancestry-dependent LOXL1 alleles, validated gene–environment interactions, reliable conversion biomarkers, single-cell and spatial atlases, faithful animal models, and disease-modifying therapy. Existing omics studies are generally small and require independent, multi-ancestry replication. Active implementation research includes phacoemulsification versus SLT and cataract surgery plus iStent versus SLT; completed XEN45 real-world evidence enrolled 350 participants, but the registry excerpt did not provide numerical outcomes. | Prediagnostic metabolomics: **205 incident XFG cases and 205 controls**, mean **11.8 years** before diagnosis; cortisone OR **0.49 per SD** (95% CI 0.32–0.74). CANPEX1: planned **n=200**; iStent-versus-laser trial: planned **n=285**; XEN45 observational study: **n=350**. | Study annotations: bulk RNA sequencing, metabolomics, prospective cohort study, randomized controlled trial, model-organism limitation | (bernstein2018exfoliationsyndromea pages 1-4, kang2022prediagnosticplasmametabolomics pages 1-2, mullany2022rnasequencingof pages 1-2, NCT06993311 chunk 1, NCT04416724 chunk 1, NCT04635020 chunk 1) |


*Table: Compact evidence-based summary of exfoliation syndrome identity, risk architecture, phenotypes, mechanism, diagnosis, prognosis, management, and research gaps. Quantitative findings and suggested knowledge-base ontology annotations are included.*

## 1. Disease information

### Definition

Exfoliation syndrome is a chronic, strongly age-dependent, complex disorder of extracellular-matrix (ECM) production and clearance. Abnormal fibrillar **exfoliation material (XFM)** accumulates most visibly in the ocular anterior segment—especially on the anterior lens capsule, pupillary margin, iris, ciliary body, zonules, and trabecular meshwork. Similar material has been reported histologically in visceral tissues, supporting the concept of a systemic matrix disorder, although its clinically established morbidity is predominantly ocular. A useful abstract-level definition is: **“Pseudoexfoliation syndrome (PXS) is a systemic condition with eye manifestations.”** (Human pathology/review.) (elhawy2012pseudoexfoliationsyndromea pages 1-2)

XFS is not synonymous with XFG. XFG is secondary, usually open-angle glaucoma caused when XFM and liberated iris pigment increase aqueous-outflow resistance and intraocular pressure (IOP), followed by glaucomatous retinal-ganglion-cell and optic-nerve injury. Estimates suggest that approximately 44% of affected people may develop XFG, but conversion varies by population, ascertainment, and follow-up. XFG accounts for approximately 25% of open-angle glaucoma worldwide in some estimates. (li2021loxl1genepolymorphisms pages 1-2, bernstein2018exfoliationsyndromea pages 1-4)

### Identifiers and synonyms

- **Preferred name:** exfoliation syndrome.
- **MONDO:** **MONDO:0008327**.
- **OMIM:** commonly represented as **Exfoliation syndrome 1 / XFS1, #177650**; database release should be checked before production ingestion.
- **MeSH:** *Exfoliation Syndrome* / *Pseudoexfoliation Syndrome*.
- **Common synonyms:** pseudoexfoliation syndrome, pseudo-exfoliation syndrome, PXS, PEX, PEXS, XFS, exfoliative syndrome, capsular glaucoma with pseudoexfoliation when glaucoma is present.
- **Related but distinct:** exfoliation glaucoma/pseudoexfoliation glaucoma (XFG/PXG/PEG); true capsular exfoliation, an occupational/infrared-associated delamination of the lens capsule, is not XFS.
- **ICD:** coding is jurisdiction/version dependent. XFS without glaucoma is generally placed under “other specified cataract/anterior-segment” categories, whereas capsular/exfoliation glaucoma is coded within secondary glaucoma categories. Exact ICD-10-CM/ICD-11 codes should be validated against the target terminology release rather than inferred from literature.

The evidence summarized here is aggregated disease-level evidence from cohorts, case-control studies, tissue studies, registries, GWAS, and reviews—not individual EHR-derived patient data.

## 2. Etiology and risk architecture

### Causal and susceptibility factors

XFS is **multifactorial and polygenic**. No single variant is necessary or sufficient. Aging is the dominant background determinant; genetic susceptibility, environmental exposure, ECM dysregulation, oxidative stress, inflammation, and impaired proteostasis converge over decades.

**LOXL1** is the strongest replicated susceptibility gene. It encodes lysyl oxidase-like 1, an enzyme involved in collagen/elastin cross-linking and elastic-fiber homeostasis. Common variants rs1048661, rs3825942, and rs2165241 are repeatedly associated with XFS/XFG, but their effects differ by ancestry and risk alleles can reverse direction between populations. A 2021 meta-analysis included 5,022 cases and 8,962 controls and found ancestry-dependent associations; this establishes susceptibility, not monogenic causality. [Li et al., published 28 April 2021, DOI](https://doi.org/10.1371/journal.pone.0250772). (li2021loxl1genepolymorphisms pages 1-2)

A major 2017 GWAS meta-analysis included **9,035 cases and 17,008 controls across 25 strata**, identifying a rare protective LOXL1 coding variant and susceptibility loci near/in **POMP, TMEM136, AGPAT1, RBMS3,** and **SEMA6A**, in addition to LOXL1 and CACNA1A. The protective variant is conventionally reported as **LOXL1 p.Tyr407Phe (p.Y407F)**. [Aung et al., May 2017, *Nature Genetics*, DOI](https://doi.org/10.1038/ng.3875). (aung2017geneticassociationstudy pages 24-38) Open Targets independently maps LOXL1 (ENSG00000129038) to MONDO:0008327 and links supporting literature including PMIDs **17690259, 18037624, 18385788, 19343041, 24938310,** and **36653562**. (OpenTargets Search: pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1)

These are common/rare **germline susceptibility alleles**, not somatic cancer-like mutations. They should not ordinarily be labeled “pathogenic” under ACMG/AMP Mendelian criteria. Population frequencies are too high, penetrance is incomplete and age dependent, and no validated carrier-frequency concept applies. There is no established role for aneuploidy, translocation, repeat expansion, mitochondrial mutation, germline mosaicism, anticipation, or consanguinity.

### Environmental and lifestyle factors

Human observational evidence implicates lifetime latitude, cold climate, greater summer outdoor exposure, and reflected light. In a US/Israeli case-control study of adults aged ≥60 years, each degree farther from the equator was associated with **11% higher odds** of XFS (OR 1.11, 95% CI 1.05–1.17); each additional average summer outdoor hour/week had OR 1.04 (1.00–1.07). US work over snow or water had OR 3.86 (1.36–10.9). Greater sunglasses use was inversely associated in the US (OR 0.98 per 1% increment) but not Israel. [Pasquale et al., December 2014, DOI](https://doi.org/10.1001/jamaophthalmol.2014.3326). These findings are vulnerable to recall, selection, and residual confounding and do not prove that UV causes XFS or sunglasses prevent it. (pasquale2014solarexposureand pages 1-2)

Other reported associations include heavy coffee/caffeine intake, low folate, higher homocysteine, outdoor occupations, more sunny days, and lower ambient temperature. Evidence for smoking, alcohol, diabetes, and cardiovascular factors is inconsistent and does not support causal classification. UV can upregulate lysyl-oxidase/ECM responses in experimental eye and skin systems, offering a plausible gene–environment mechanism, but replicated genotype-by-exposure interaction estimates remain lacking. (pasquale2014considerationforgeneenvironment pages 4-6, pasquale2014considerationforgeneenvironment pages 2-4, kang2020cohortstudyof pages 6-7)

**Protective factors:** LOXL1 p.Y407F is the clearest genetic protective association. Sunglasses/ocular UV protection and folate sufficiency are biologically plausible environmental protective factors, but neither has preventive-trial confirmation. No drug, dietary supplement, or behavior is proven to prevent XFS.

## 3. Phenotypes

XFS is generally **late-onset, insidious, chronic, progressive, and variably asymmetric**. It is uncommon before 50–60 years and becomes increasingly prevalent with age. A clinically unilateral presentation frequently represents asymmetric bilateral disease.

| Phenotype | Type and characteristics | Suggested HPO mapping |
|---|---|---|
| White-gray fibrillar deposits on anterior lens/pupillary border | Cardinal slit-lamp sign; progressive | Abnormality of lens/anterior eye morphology; local term may be required |
| Poor pharmacologic mydriasis | Clinical sign caused by iris stromal/sphincter changes; common and surgically important | Abnormal pupillary response / miosis |
| Peripupillary iris transillumination and pigment loss | Clinical sign; variable | Iris transillumination defect |
| Trabecular hyperpigmentation/Sampaolesi line | Gonioscopic sign | Abnormal anterior-chamber-angle morphology |
| Elevated/fluctuating IOP | Laboratory/functional measurement; absent in uncomplicated XFS, prominent in XFG | **Increased intraocular pressure** |
| Secondary open-angle glaucoma | Progressive optic neuropathy with field loss | Glaucoma; visual-field defect; optic atrophy |
| Zonular weakness, phacodonesis, lens subluxation/dislocation | Progressive structural phenotype; increases cataract-surgery risk | Phacodonesis; ectopia lentis/lens subluxation |
| Cataract | Age-associated comorbidity and major reversible cause of visual loss | Cataract |
| Reduced corneal endothelial density | Quantitative ocular sign reported in recent clinical studies | Corneal endothelial abnormality |
| Visual impairment/blindness | Downstream disability from cataract or XFG | Visual impairment; blindness |

The characteristic lens pattern and associated iris, zonular, and trabecular findings are well documented. Zonular loss can cause vitreous loss, lens or intraocular-lens complex dislocation, and difficult cataract surgery. (elhawy2012pseudoexfoliationsyndromea pages 1-2, borjan2023pseudoexfoliativesyndromein pages 2-3)

Quality of life declines primarily through visual-field loss, impaired acuity, medication burden, treatment adverse effects, surgery, and loss of independence. Disease-specific EQ-5D or PROMIS norms were not identified. In an Indian tertiary-care cohort of 6,284 XFS eyes, XFG was present in 29%; the study reported substantial visual impairment and **28.2% absolute blindness at presentation**, illustrating referral-setting burden rather than population risk.

## 4. Genetic, molecular, and epigenetic information

LOXL1 is a susceptibility gene, not a fully penetrant causal gene. Common coding variants include **p.Arg141Leu (rs1048661)** and **p.Gly153Asp (rs3825942)**; rs2165241 is intronic. Functional studies support effects on LOXL1 expression, processing, stability, or aggregation, but population-dependent allele reversal means simple loss-of-function/gain-of-function labels are inadequate. A cited functional study is Sharma et al., 2016, PMID **26997634**. (li2021loxl1genepolymorphisms pages 21-21)

Additional loci implicate calcium signaling (**CACNA1A**), proteasome maturation (**POMP**), membrane biology (**TMEM136**), phospholipid metabolism (**AGPAT1**), RNA binding/ECM regulation (**RBMS3**), and semaphorin signaling (**SEMA6A**). Earlier candidate-gene signals involving CNTNAP2, CLU, MMP1/MMP3, GST genes, adenosine receptors, and LYST are less definitive than GWAS evidence. (elhawy2012pseudoexfoliationsyndromea pages 1-2, aboobakar2022thegeneticsof pages 6-8)

Epigenetic regulation of LOXL1 and ECM/stress-response genes is an active hypothesis. DNA methylation, histone regulation, microRNAs, and environmentally responsive transcription may explain part of age and exposure dependence, but no epigenetic biomarker is clinically validated. No reproducible large chromosomal abnormality is established.

## 5. Environmental information

Relevant exposure categories are solar/ocular UV and reflected light, cold/latitude-associated climate, outdoor occupation, caffeine/coffee, and nutritional factors affecting folate–homocysteine metabolism. Non-melanoma skin cancer, used as a proxy for cumulative UV exposure, was associated with **40% higher XFG risk** in 120,307 US participants followed for >25 years (445 incident cases; adjusted RR 1.40, 95% CI 1.08–1.82), with stronger associations below age 65 and at northern latitudes. [Kang et al., March 2020, DOI](https://doi.org/10.1097/IJG.0000000000001496). This remains proxy-based observational evidence. (kang2020cohortstudyof pages 2-3, kang2020cohortstudyof pages 6-7)

No infectious bacterium, virus, fungus, or parasite has been established as a cause. Upregulation of “viral gene-expression pathways” in lens RNA-seq refers to host pathway annotation and must not be interpreted as evidence of infection. (mullany2022rnasequencingof pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Advanced age plus polygenic susceptibility—especially LOXL1 regulatory/coding architecture—leads to** vulnerable elastic-fiber and ECM homeostasis in anterior-segment tissues.
2. **Environmental stressors, plausibly ocular UV/cold-reflection exposure, lead to** oxidative stress and stress-responsive LOXL1/TGF-β expression; this interaction is biologically supported but partly inferred.
3. **TGF-β dysregulation, inflammation, and redox imbalance lead to** increased production and altered assembly of fibrillin-, elastin-, basement-membrane-, and LOXL1-containing matrix components.
4. **LOXL1 misfolding plus proteasome, autophagosome, lysosome, microtubule, and mitochondrial dysfunction leads to** defective intracellular quality control and extracellular accumulation of aggregated XFM; causality is strongest in patient-derived cellular work but remains incompletely demonstrated in vivo.
5. **XFM deposition on iris, lens, ciliary epithelium, zonules, and trabecular meshwork leads to two branches:**
   - **zonular/iris injury leads to** poor dilation, pigment liberation, phacodonesis, lens instability, and cataract-surgical complications;
   - **trabecular XFM and pigment loading leads to** increased aqueous-outflow resistance and elevated/fluctuating IOP.
6. **Sustained IOP and associated vascular/oxidative stress lead to** retinal-ganglion-cell axonal injury, optic-nerve cupping, progressive visual-field loss, and potentially irreversible blindness.

TGF-β1/2, LOXL1, fibrillin-1, LTBP1, clusterin, ApoE, and matrix metalloproteinase/tissue-inhibitor balance are central molecular candidates. Early XFS aqueous humor reportedly contains approximately threefold higher IL-6 and IL-8; IL-6 induces several XFM-associated ECM transcripts in cultured ciliary epithelial cells and Tenon fibroblasts. (shyam2023geneticandepigenetic pages 43-47, borras2018growthfactorsoxidative pages 8-10)

Patient-derived XFG Tenon fibroblasts exhibit defective lysosomal positioning, microtubule organization, autophagic processing, and mitochondrial health. The authors’ central model is LOXL1 proteopathy superimposed on impaired autophagic clearance. [Bernstein et al., July 2018, DOI](https://doi.org/10.1097/IJG.0000000000000919). (bernstein2018exfoliationsyndromea pages 1-4)

### Molecular profiling

- **Bulk RNA-seq:** Lens capsular epithelium from 25 XFS and 39 controls identified **2,882 differentially expressed genes**. The abstract reports: **“Genes associated with viral gene expression pathways were among the most upregulated, alongside genes encoding ribosomal and mitochondrial respiratory transport chain proteins.”** Cell-adhesion/type-IV-collagen transcripts were downregulated. [Mullany et al., 29 March 2022, DOI](https://doi.org/10.1167/iovs.63.3.26). (mullany2022rnasequencingof pages 1-2)
- **Prediagnostic metabolomics:** In 205 incident XFG cases and 205 matched controls, plasma collected a mean 11.8 years before diagnosis showed FDR-significant associations for lysophosphatidylcholines, phosphatidylethanolamine plasmalogens, triglycerides, and steroids. Cortisone had OR 0.49 per SD (95% CI 0.32–0.74). This is biomarker discovery, not clinical validation or proof of protection. [Kang et al., 11 August 2022, DOI](https://doi.org/10.1167/iovs.63.9.15). (kang2022prediagnosticplasmametabolomics pages 1-2)
- **Single-cell/spatial/CRISPR:** No mature XFS single-cell atlas, spatial transcriptomic reference, or replicated genome-wide functional screen was identified. These are priority gaps.

Suggested **GO terms** include extracellular matrix organization, elastic-fiber assembly, collagen fibril organization, TGF-β receptor signaling, response to oxidative stress, autophagy, lysosomal transport, proteasomal protein catabolism, mitochondrial electron transport, and inflammatory response. Suggested **CL concepts** include lens epithelial cell, non-pigmented ciliary epithelial cell, iris pigment epithelial cell, trabecular-meshwork cell, corneal endothelial cell, fibroblast, and retinal ganglion cell.

## 7. Anatomical structures affected

The primary organ is the **eye**, especially its anterior segment. Principal sites are anterior lens capsule, lens epithelium, iris pigment epithelium and stroma, pupillary sphincter, ciliary epithelium/body, zonular fibers, trabecular meshwork, Schlemm canal region, corneal endothelium, and iris vasculature. Secondary glaucomatous injury affects retinal ganglion cells, optic-nerve head/lamina cribrosa, and visual pathways.

Suggested **UBERON** concepts: eye, anterior segment of eye, lens capsule, iris, ciliary body, cornea/corneal endothelium, trabecular meshwork, retina, optic nerve. Suggested **GO cellular components:** extracellular matrix, elastic fiber, basement membrane, endoplasmic reticulum, autophagosome, lysosome, mitochondrion, and proteasome.

XFS may be clinically unilateral, but asymmetric bilateral involvement is common. Histologic deposits have been reported in lung, liver, kidney, gallbladder, skin, heart/pericardiac vessels, and cerebral meninges. Associations with cardiovascular, cerebrovascular, hearing, and systemic vascular disease remain heterogeneous; systemic screening beyond ordinary age-appropriate care is not established solely because XFS is present. (bora2024cardiovascularmanifestationsof pages 7-8, elhawy2012pseudoexfoliationsyndromea pages 1-2)

## 8. Temporal development

Onset is usually late adult/geriatric and insidious. A practical clinical continuum is: (1) early/asymmetric deposits with normal IOP; (2) established XFS with poor dilation, pigment release, and zonular dysfunction; (3) XFS with ocular hypertension; (4) XFG with structural/functional damage; and (5) advanced glaucoma or lens/IOL-bag instability.

The disorder is chronic and does not spontaneously remit. Apparent unilateral disease can convert to bilateral clinical disease over years. XFG can progress faster than POAG: over three years, one study observed mean-deviation change of **−3.17 dB versus −1.25 dB**, VFI change of **−7.65% versus −1.90%**, and guided-progression-analysis progression in **58% versus 13%**. Therefore, early recognition and tighter IOP targets are important.

## 9. Inheritance and population

Inheritance is **multifactorial/polygenic**, with familial aggregation, incomplete and strongly age-dependent penetrance, and variable expressivity. No conventional carrier state, anticipation, or Mendelian recurrence estimate is appropriate.

Published prevalence ranges from **<0.4% to >20%**, depending heavily on age, ancestry, geography, examination technique, and study design; approximately 80 million people have been estimated to be affected globally. Latitude examples cited in the gene–environment literature range from 1.1% in Sri Lanka to 22% in Finland, but cross-study methodological differences preclude a simple latitude-prevalence equation. (li2021loxl1genepolymorphisms pages 1-2, pasquale2014considerationforgeneenvironment pages 2-4)

High prevalence has been reported in Nordic, Mediterranean, Russian, Middle Eastern, South Asian, and some Indigenous populations, while XFS is not restricted to any ancestry. LOXL1 haplotypes and risk directions vary geographically. Female predominance appears in some older cohorts but is inconsistent after accounting for longevity and ascertainment; no universal sex ratio should be assigned. Incidence per 100,000/year is not globally standardized.

## 10. Diagnostics

Diagnosis is clinical:

1. Slit-lamp examination before and after dilation for pupillary-border and anterior-lens XFM, including the classic central disc/clear intermediate zone/peripheral granular ring.
2. Assessment of pupil dilation, iris transillumination, pigment dispersion, phacodonesis, lens position, and cataract.
3. Goldmann applanation tonometry, ideally at different times because IOP fluctuates.
4. Gonioscopy for angle configuration, trabecular pigmentation, and Sampaolesi line.
5. Optic-disc examination, OCT RNFL/ganglion-cell analysis, and standard automated perimetry to diagnose/stage XFG.
6. Pachymetry and corneal endothelial assessment when clinically or surgically indicated.

Differential diagnoses include pigment dispersion syndrome (younger, often male; Krukenberg spindle, mid-peripheral transillumination, posterior iris bowing), uveitic pigment/debris, true capsular exfoliation, amyloid or inflammatory deposits, and primary open-angle/angle-closure glaucoma. XFM on lens/pupil and zonular weakness favor XFS. (rong2024lackofassociation pages 8-9)

There is no recommended routine LOXL1 test: common risk alleles have poor specificity and ancestry-dependent effects. WGS, WES, panels, CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing have no routine diagnostic role. RNA-seq, proteomics, metabolomics, aqueous biomarkers, systemic immune indexes, and liquid biopsy remain research tools.

## 11. Outcome and prognosis

XFS is not known to shorten life expectancy directly, and disease-specific survival statistics are not applicable. Prognosis is driven by XFG severity, IOP level/fluctuation, baseline field loss, adherence, treatment response, cataract, corneal endothelial reserve, and zonular integrity.

XFG typically presents with higher IOP and more advanced damage and responds less predictably to medication than POAG. Irreversible glaucomatous loss does not recover; cataract-related acuity loss is often reversible, but surgery is technically more hazardous. Lens/IOL-bag dislocation may occur years after cataract surgery. The strongest modifiable prognostic factor is sustained IOP reduction. (aboobakar2022thegeneticsof pages 6-8, borjan2023pseudoexfoliativesyndromein pages 2-3)

## 12. Treatment

There is **no approved disease-modifying treatment** that stops XFM production or removes systemic deposits. Management targets complications.

- **XFS without glaucoma:** periodic IOP, optic-nerve, OCT, and field surveillance; document dilation and zonular status.
- **XFG pharmacotherapy:** prostaglandin analogues, beta-blockers, carbonic-anhydrase inhibitors, alpha-2 agonists, and rho-kinase inhibitors according to local glaucoma algorithms. Fixed combinations and preservative-free preparations can reduce treatment burden/ocular-surface toxicity. Pharmacogenomic prescribing is not established.
- **Laser:** SLT is often effective because the trabecular meshwork is pigmented. A 2024 series reported IOP reduction from **26.7 to 18.9 mmHg at three months**, a 29.2% reduction and 69.4% success, but durability requires follow-up.
- **Cataract surgery:** phacoemulsification may lower IOP and improves vision when cataract is significant. Surgeons should anticipate small pupil and zonular weakness; iris hooks/rings, capsular hooks, capsular-tension rings, careful hydrodissection, low-stress fluidics, and secure IOL planning may be required. In a Croatian registry, XFS surgery cost was **1.4-fold higher**; XFS was associated with longer surgery and more complications. [Borjan et al., December 2023, DOI](https://doi.org/10.3390/jcm13010038). (borjan2023pseudoexfoliativesyndromein pages 2-3, borjan2023pseudoexfoliativesyndromein pages 12-14)
- **Incisional glaucoma surgery:** trabeculectomy with antifibrotic, glaucoma drainage devices, selected angle surgery/MIGS, and cyclodestruction are options according to stage and target IOP. A 2024 PreserFlo series of 29 Asian XFG eyes reduced mean IOP from 32.6 to 16.9 mmHg and medications from 3.4 to 1.0, but had **31% reoperation** and **17% hypotony**, warranting caution. [Wakuda et al., October 2024, DOI](https://doi.org/10.3390/jcm13206132). (wakuda2024postoperativeoutcomesof pages 4-6, wakuda2024postoperativeoutcomesof pages 9-10)

Suggested **NCIT intervention concepts:** ophthalmic solution, prostaglandin analogue therapy, selective laser trabeculoplasty, phacoemulsification, intraocular-lens implantation, capsular-tension-ring placement, trabeculectomy, glaucoma drainage-device implantation, minimally invasive glaucoma surgery, and cyclophotocoagulation.

Current implementation studies include recruiting **CANPEX1** (phacoemulsification versus SLT; NCT04416724; planned n=200) and a Helsinki cataract-plus-iStent versus cataract-plus-SLT study (NCT04635020; planned n=285). A completed observational XEN45 study enrolled 350 participants (NCT06993311), although numerical results were unavailable in the retrieved registry record. These test pressure-lowering strategies, not molecular correction of XFS. (NCT06993311 chunk 1, NCT04416724 chunk 1, NCT04635020 chunk 1)

## 13. Prevention

- **Primary:** no proven prevention. UV-blocking eyewear is low risk and generally advisable for ocular health, but XFS-specific benefit is unproven. Maintain nutritional folate adequacy rather than prescribing high-dose supplementation. Evidence is insufficient to recommend caffeine restriction solely to prevent XFS.
- **Secondary:** careful dilated slit-lamp examination in older adults, especially those with family history, high-prevalence ancestry/geography, unilateral XFS, ocular hypertension, or unexplained poor dilation. Monitor both eyes.
- **Tertiary:** aggressive individualized IOP control, adherence support, regular fields/OCT, cataract-surgical precautions, and long-term monitoring for late IOL-bag instability.
- **Not applicable:** vaccination, newborn screening, prenatal diagnosis, carrier screening, prophylactic gene therapy, and population genetic screening.

## 14. Other species and natural disease

No infectious transmission or zoonotic potential exists. A fully validated naturally occurring veterinary counterpart with the characteristic human XFM phenotype is not established. LOXL1 and elastic-fiber biology are evolutionarily conserved, and canine ocular disorders have informed glaucoma research, but canine pigmentary glaucoma should not be annotated as natural XFS without direct pathology.

**Mus musculus** (NCBI Taxon **10090**) LOXL1-deficient models demonstrate systemic elastic-fiber defects and are useful for testing LOXL1 biology. However, they do not consistently reproduce the age-dependent ocular XFM, asymmetric human course, and conversion to XFG. A LOXL1-knockout elastin-homeostasis study is indexed by PMID **32533648**. (li2021loxl1genepolymorphisms pages 21-21, bernstein2018exfoliationsyndromea pages 1-4)

## 15. Model organisms and experimental systems

- **Human primary cells:** XFG patient-derived Tenon fibroblasts reproduce autophagy/lysosome positioning, microtubule, mitochondrial, LOXL1-processing, and clusterin phenotypes. This is presently one of the most disease-relevant mechanistic systems. Limitation: surgery-derived fibroblasts may reflect advanced glaucoma and treatment exposure rather than disease initiation. (bernstein2018exfoliationsyndromea pages 1-4)
- **Ocular cell culture:** lens epithelial, non-pigmented ciliary epithelial, and trabecular-meshwork cells are used for TGF-β, UV, oxidative-stress, cytokine, LOXL1, and ECM experiments. They permit perturbation but do not recreate aging, aqueous dynamics, or multicellular XFM assembly.
- **LOXL1-null mouse:** useful for elastic-fiber and gene-function studies but incompletely phenocopies human XFS.
- **Human surgical tissue/aqueous humor:** lens capsules, iris/ciliary tissue, aqueous humor, and XFM deposits support transcriptomics, proteomics, microscopy, and biochemical studies but are cross-sectional and often late-stage.
- **Major unmet need:** an age-dependent, ancestry-aware animal or organoid model that forms authentic XFM and progresses to ocular hypertension/XFG.

## Overall assessment

The authoritative interpretation is that XFS is an age-related systemic ECM aggregopathy with ocularly dominant disease. LOXL1 is central but not determinative; ancestry-dependent allele reversal, high risk-allele prevalence, environmental associations, and impaired stress/proteostasis pathways argue against a simple monogenic enzyme-deficiency model. The most immediate clinical opportunity is not genetic testing but earlier recognition, bilateral surveillance, tighter IOP control, and XFS-aware cataract planning. The principal research priorities are functional resolution of LOXL1 and newer loci, replicated gene–environment interaction studies, single-cell/spatial profiling, conversion biomarkers, faithful models, and therapies that reduce XFM production or restore proteostasis.

References

1. (li2021loxl1genepolymorphisms pages 1-2): Xiaoyan Li, Jie He, and Jian Sun. Loxl1 gene polymorphisms are associated with exfoliation syndrome/exfoliation glaucoma risk: an updated meta-analysis. PLoS ONE, 16:e0250772, Apr 2021. URL: https://doi.org/10.1371/journal.pone.0250772, doi:10.1371/journal.pone.0250772. This article has 27 citations and is from a peer-reviewed journal.

2. (bernstein2018exfoliationsyndromea pages 1-4): Audrey M. Bernstein, Robert Ritch, and Jose M. Wolosin. Exfoliation syndrome: a disease of autophagy and loxl1 proteopathy. Journal of glaucoma, 27 Suppl 1:S44-S53, Jul 2018. URL: https://doi.org/10.1097/ijg.0000000000000919, doi:10.1097/ijg.0000000000000919. This article has 34 citations and is from a peer-reviewed journal.

3. (elhawy2012pseudoexfoliationsyndromea pages 1-2): Eman Elhawy, Gautam Kamthan, Cecilia Q Dong, and John Danias. Pseudoexfoliation syndrome, a systemic disorder with ocular manifestations. Human Genomics, Oct 2012. URL: https://doi.org/10.1186/1479-7364-6-22, doi:10.1186/1479-7364-6-22. This article has 197 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1): Open Targets Query (pseudoexfoliation syndrome,exfoliation glaucoma-LOXL1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (aung2017geneticassociationstudy pages 24-38): Tin Aung, Mineo Ozaki, Mei Chin Lee, Ursula Schlötzer-Schrehardt, Gudmar Thorleifsson, Takanori Mizoguchi, Robert P Igo, Aravind Haripriya, Susan E Williams, Yury S Astakhov, Andrew C Orr, Kathryn P Burdon, Satoko Nakano, Kazuhiko Mori, Khaled Abu-Amero, Michael Hauser, Zheng Li, Gopalakrishnan Prakadeeswari, Jessica N Cooke Bailey, Alina Popa Cherecheanu, Jae H Kang, Sarah Nelson, Ken Hayashi, Shin-ichi Manabe, Shigeyasu Kazama, Tomasz Zarnowski, Kenji Inoue, Murat Irkec, Miguel Coca-Prados, Kazuhisa Sugiyama, Irma Järvelä, Patricio Schlottmann, S Fabian Lerner, Hasnaa Lamari, Yildirim Nilgün, Mukharram Bikbov, Ki Ho Park, Soon Cheol Cha, Kenji Yamashiro, Juan C Zenteno, Jost B Jonas, Rajesh S Kumar, Shamira A Perera, Anita S Y Chan, Nino Kobakhidze, Ronnie George, Lingam Vijaya, Tan Do, Deepak P Edward, Lourdes de Juan Marcos, Mohammad Pakravan, Sasan Moghimi, Ryuichi Ideta, Daniella Bach-Holm, Per Kappelgaard, Barbara Wirostko, Samuel Thomas, Daniel Gaston, Karen Bedard, Wenda L Greer, Zhenglin Yang, Xueyi Chen, Lulin Huang, Jinghong Sang, Hongyan Jia, Liyun Jia, Chunyan Qiao, Hui Zhang, Xuyang Liu, Bowen Zhao, Ya-Xing Wang, Liang Xu, Stéphanie Leruez, Pascal Reynier, George Chichua, Sergo Tabagari, Steffen Uebe, Matthias Zenkel, Daniel Berner, Georg Mossböck, Nicole Weisschuh, Ursula Hoja, Ulrich-Christoph Welge-Luessen, Christian Mardin, Panayiota Founti, Anthi Chatzikyriakidou, Theofanis Pappas, Eleftherios Anastasopoulos, Alexandros Lambropoulos, Arkasubhra Ghosh, Rohit Shetty, Natalia Porporato, Vijayan Saravanan, Rengaraj Venkatesh, Chandrashekaran Shivkumar, Narendran Kalpana, Sripriya Sarangapani, Mozhgan R Kanavi, Afsaneh Naderi Beni, Shahin Yazdani, Alireza lashay, Homa Naderifar, Nassim Khatibi, Antonio Fea, Carlo Lavia, Laura Dallorto, Teresa Rolle, Paolo Frezzotti, Daniela Paoli, Erika Salvi, Paolo Manunta, Yosai Mori, Kazunori Miyata, Tomomi Higashide, Etsuo Chihara, Satoshi Ishiko, Akitoshi Yoshida, Masahide Yanagi, Yoshiaki Kiuchi, Tsutomu Ohashi, Toshiya Sakurai, Takako Sugimoto, Hideki Chuman, Makoto Aihara, Masaru Inatani, Masahiro Miyake, Norimoto Gotoh, Fumihiko Matsuda, Nagahisa Yoshimura, Yoko Ikeda, Morio Ueno, Chie Sotozono, Jin Wook Jeoung, Min Sagong, Kyu Hyung Park, Jeeyun Ahn, Marisa Cruz-Aguilar, Sidi M Ezzouhairi, Abderrahman Rafei, Yaan Fun Chong, Xiao Yu Ng, Shuang Ru Goh, Yueming Chen, Victor H K Yong, Muhammad Imran Khan, Olusola O Olawoye, Adeyinka O Ashaye, Idakwo Ugbede, Adeola Onakoya, Nkiru Kizor-Akaraiwe, Chaiwat Teekhasaenee, Yanin Suwan, Wasu Supakontanasan, Suhanya Okeke, Nkechi J Uche, Ifeoma Asimadu, Humaira Ayub, Farah Akhtar, Ewa Kosior-Jarecka, Urszula Lukasik, Ignacio Lischinsky, Vania Castro, Rodolfo Perez Grossmann, Gordana Sunaric Megevand, Sylvain Roy, Edward Dervan, Eoin Silke, Aparna Rao, Priti Sahay, Pablo Fornero, Osvaldo Cuello, Delia Sivori, Tamara Zompa, Richard A Mills, Emmanuelle Souzeau, Paul Mitchell, Jie Jin Wang, Alex W Hewitt, Michael Coote, Jonathan G Crowston, Sergei Y Astakhov, Eugeny L Akopov, Anton Emelyanov, Vera Vysochinskaya, Gyulli Kazakbaeva, Rinat Fayzrakhmanov, Saleh A Al-Obeidan, Ohoud Owaidhah, Leyla Ali Aljasim, Balram Chowbay, Jia Nee Foo, Raphael Q Soh, Kar Seng Sim, Zhicheng Xie, Augustine W O Cheong, Shi Qi Mok, Hui Meng Soo, Xiao Yin Chen, Su Qin Peh, Khai Koon Heng, Rahat Husain, Su-Ling Ho, Axel M Hillmer, Ching-Yu Cheng, Francisco A Escudero-Domínguez, Rogelio González-Sarmiento, Frederico Martinon-Torres, Antonio Salas, Kessara Pathanapitoon, Linda Hansapinyo, Boonsong Wanichwecharugruang, Naris Kitnarong, Anavaj Sakuntabhai, Hip X Nguyn, Giang T T Nguyn, Trình V Nguyn, Werner Zenz, Alexander Binder, Daniela S Klobassa, Martin L Hibberd, Sonia Davila, Stefan Herms, Markus M Nöthen, Susanne Moebus, Robyn M Rautenbach, Ari Ziskind, Trevor R Carmichael, Michele Ramsay, Lydia Álvarez, Montserrat García, Héctor González-Iglesias, Pedro P Rodríguez-Calvo, Luis Fernández-Vega Cueto, Çilingir Oguz, Nevbahar Tamcelik, Eray Atalay, Bilge Batu, Dilek Aktas, Burcu Kasım, M Roy Wilson, Anne L Coleman, Yutao Liu, Pratap Challa, Leon Herndon, Rachel W Kuchtey, John Kuchtey, Karen Curtin, Craig J Chaya, Alan Crandall, Linda M Zangwill, Tien Yin Wong, Masakazu Nakano, Shigeru Kinoshita, Anneke I den Hollander, Eija Vesti, John H Fingert, Richard K Lee, Arthur J Sit, Bradford J Shingleton, Ningli Wang, Daniele Cusi, Raheel Qamar, Peter Kraft, Margaret A Pericak-Vance, Soumya Raychaudhuri, Steffen Heegaard, Tero Kivelä, André Reis, Friedrich E Kruse, Robert N Weinreb, Louis R Pasquale, Jonathan L Haines, Unnur Thorsteinsdottir, Fridbert Jonasson, R Rand Allingham, Dan Milea, Robert Ritch, Toshiaki Kubota, Kei Tashiro, Eranga N Vithana, Shazia Micheal, Fotis Topouzis, Jamie E Craig, Michael Dubina, Periasamy Sundaresan, Kari Stefansson, Janey L Wiggs, Francesca Pasutto, and Chiea Chuen Khor. Genetic association study of exfoliation syndrome identifies a protective rare variant at loxl1 and five new susceptibility loci. Nature Genetics, 49:993-1004, May 2017. URL: https://doi.org/10.1038/ng.3875, doi:10.1038/ng.3875. This article has 185 citations and is from a highest quality peer-reviewed journal.

6. (aboobakar2022thegeneticsof pages 6-8): Inas F. Aboobakar and Janey L. Wiggs. The genetics of glaucoma: disease associations, personalised risk assessment and therapeutic opportunities‐a review. Clinical & Experimental Ophthalmology, 50:143-162, Jan 2022. URL: https://doi.org/10.1111/ceo.14035, doi:10.1111/ceo.14035. This article has 64 citations and is from a peer-reviewed journal.

7. (pasquale2014considerationforgeneenvironment pages 4-6): Louis R. Pasquale, Jae H. Kang, and Janey L. Wiggs. Consideration for gene-environment interactions as novel determinants of exfoliation syndrome. International Ophthalmology Clinics, 54:29–41, Jan 2014. URL: https://doi.org/10.1097/iio.0000000000000040, doi:10.1097/iio.0000000000000040. This article has 11 citations and is from a peer-reviewed journal.

8. (pasquale2014solarexposureand pages 1-2): Louis R. Pasquale, Aliya Z. Jiwani, Tzukit Zehavi-Dorin, Arow Majd, Douglas J. Rhee, Teresa Chen, Angela Turalba, Lucy Shen, Stacey Brauner, Cynthia Grosskreutz, Matthew Gardiner, Sherleen Chen, Sheila Borboli-Gerogiannis, Scott H. Greenstein, Kenneth Chang, Robert Ritch, Stephanie Loomis, Jae H. Kang, Janey L. Wiggs, and Hani Levkovitch-Verbin. Solar exposure and residential geographic history in relation to exfoliation syndrome in the united states and israel. JAMA ophthalmology, 132 12:1439-45, Dec 2014. URL: https://doi.org/10.1001/jamaophthalmol.2014.3326, doi:10.1001/jamaophthalmol.2014.3326. This article has 93 citations and is from a highest quality peer-reviewed journal.

9. (pasquale2014considerationforgeneenvironment pages 2-4): Louis R. Pasquale, Jae H. Kang, and Janey L. Wiggs. Consideration for gene-environment interactions as novel determinants of exfoliation syndrome. International Ophthalmology Clinics, 54:29–41, Jan 2014. URL: https://doi.org/10.1097/iio.0000000000000040, doi:10.1097/iio.0000000000000040. This article has 11 citations and is from a peer-reviewed journal.

10. (kang2020cohortstudyof pages 6-7): Jae H. Kang, Trang VoPham, Francine Laden, Bernard A. Rosner, Barbara Wirostko, Robert Ritch, Janey L. Wiggs, Abrar Qureshi, Hongmei Nan, and Louis R. Pasquale. Cohort study of non-melanoma skin cancer and the risk of exfoliation glaucoma. Journal of Glaucoma, 29:448-455, Mar 2020. URL: https://doi.org/10.1097/ijg.0000000000001496, doi:10.1097/ijg.0000000000001496. This article has 13 citations and is from a peer-reviewed journal.

11. (rong2024lackofassociation pages 8-9): Shisong Rong and Xinting Yu. Lack of association between loxl1 variants and pigment dispersion syndrome/pigmentary glaucoma: a meta-analysis. Genes, 15:161, Jan 2024. URL: https://doi.org/10.3390/genes15020161, doi:10.3390/genes15020161. This article has 3 citations.

12. (borjan2023pseudoexfoliativesyndromein pages 2-3): Ivan Borjan, Robert Stanić, Ivna Pleština-Borjan, Maja Pavić, Silvia N. W. Hertzberg, Ljubo Znaor, Beáta Éva Petrovski, and Goran Petrovski. Pseudoexfoliative syndrome in cataract surgery—a quality register study and health economic analysis in the split-dalmatia county, croatia. Journal of Clinical Medicine, 13:38, Dec 2023. URL: https://doi.org/10.3390/jcm13010038, doi:10.3390/jcm13010038. This article has 8 citations.

13. (shyam2023geneticandepigenetic pages 43-47): KR Shyam and DP Alone. Genetic and epigenetic regulation of candidate genes associated with pseudoexfoliation. Unknown journal, 2023.

14. (borras2018growthfactorsoxidative pages 8-10): Teresa Borrás. Growth factors, oxidative damage, and inflammation in exfoliation syndrome. Journal of Glaucoma, 27:S54-S60, Jul 2018. URL: https://doi.org/10.1097/ijg.0000000000000904, doi:10.1097/ijg.0000000000000904. This article has 28 citations and is from a peer-reviewed journal.

15. (mullany2022rnasequencingof pages 1-2): Sean Mullany, Henry Marshall, Tiger Zhou, Daniel Thomson, Joshua M. Schmidt, Ayub Qassim, Lachlan S. W. Knight, Georgina Hollitt, Ella C. Berry, Thi Nguyen, Minh-Son To, David Dimasi, Abraham Kuot, Joshua Dubowsky, Rhys Fogarty, Michelle Sun, Luke Chehade, Shilpa Kuruvilla, Devaraj Supramaniam, James Breen, Shiwani Sharma, John Landers, Stewart Lake, Richard A. Mills, Mark M. Hassall, Weng O. Chan, Sonja Klebe, Emmanuelle Souzeau, Owen M. Siggs, and Jamie E. Craig. Rna sequencing of lens capsular epithelium implicates novel pathways in pseudoexfoliation syndrome. Mar 2022. URL: https://doi.org/10.1167/iovs.63.3.26, doi:10.1167/iovs.63.3.26. This article has 11 citations.

16. (wakuda2024postoperativeoutcomesof pages 4-6): Hiroyuki Wakuda, Ryota Aoki, and Shunsuke Nakakura. Postoperative outcomes of preserflo microshunt in patients with exfoliation glaucoma. Oct 2024. URL: https://doi.org/10.3390/jcm13206132, doi:10.3390/jcm13206132. This article has 6 citations.

17. (borjan2023pseudoexfoliativesyndromein pages 12-14): Ivan Borjan, Robert Stanić, Ivna Pleština-Borjan, Maja Pavić, Silvia N. W. Hertzberg, Ljubo Znaor, Beáta Éva Petrovski, and Goran Petrovski. Pseudoexfoliative syndrome in cataract surgery—a quality register study and health economic analysis in the split-dalmatia county, croatia. Journal of Clinical Medicine, 13:38, Dec 2023. URL: https://doi.org/10.3390/jcm13010038, doi:10.3390/jcm13010038. This article has 8 citations.

18. (NCT04635020 chunk 1): Prof. Mika Harju. Comparison Of iStent to Laser in Exfoliation Glaucoma Helsinki Study Group. Helsinki University Central Hospital. 2020. ClinicalTrials.gov Identifier: NCT04635020

19. (NCT04416724 chunk 1):  Phacoemulsification vs SLT as Initial Treatment for Pseudoexfoliation Glaucoma. Nova Scotia Health Authority. 2022. ClinicalTrials.gov Identifier: NCT04416724

20. (kang2022prediagnosticplasmametabolomics pages 1-2): Jae H. Kang, Oana Zeleznik, Lisa Frueh, Jessica Lasky-Su, A. Heather Eliassen, Clary Clish, Bernard A. Rosner, Louis R. Pasquale, and Janey L. Wiggs. Prediagnostic plasma metabolomics and the risk of exfoliation glaucoma. Aug 2022. URL: https://doi.org/10.1167/iovs.63.9.15, doi:10.1167/iovs.63.9.15. This article has 10 citations.

21. (NCT06993311 chunk 1): SARA POSE BAZARRA. Real World Evidence of Xen45 Gel Implant in Pseudoexfoliation Glaucoma. Xerencia de Xestión Integrada de Ferrol. 2018. ClinicalTrials.gov Identifier: NCT06993311

22. (li2021loxl1genepolymorphisms pages 21-21): Xiaoyan Li, Jie He, and Jian Sun. Loxl1 gene polymorphisms are associated with exfoliation syndrome/exfoliation glaucoma risk: an updated meta-analysis. PLoS ONE, 16:e0250772, Apr 2021. URL: https://doi.org/10.1371/journal.pone.0250772, doi:10.1371/journal.pone.0250772. This article has 27 citations and is from a peer-reviewed journal.

23. (kang2020cohortstudyof pages 2-3): Jae H. Kang, Trang VoPham, Francine Laden, Bernard A. Rosner, Barbara Wirostko, Robert Ritch, Janey L. Wiggs, Abrar Qureshi, Hongmei Nan, and Louis R. Pasquale. Cohort study of non-melanoma skin cancer and the risk of exfoliation glaucoma. Journal of Glaucoma, 29:448-455, Mar 2020. URL: https://doi.org/10.1097/ijg.0000000000001496, doi:10.1097/ijg.0000000000001496. This article has 13 citations and is from a peer-reviewed journal.

24. (bora2024cardiovascularmanifestationsof pages 7-8): Rajal R Bora, Roshan Prasad, Swapneel Mathurkar, Kashish Bhojwani, and Akshansh Prasad. Cardiovascular manifestations of pseudoexfoliation syndrome: a narrative review. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.51492, doi:10.7759/cureus.51492. This article has 10 citations.

25. (wakuda2024postoperativeoutcomesof pages 9-10): Hiroyuki Wakuda, Ryota Aoki, and Shunsuke Nakakura. Postoperative outcomes of preserflo microshunt in patients with exfoliation glaucoma. Oct 2024. URL: https://doi.org/10.3390/jcm13206132, doi:10.3390/jcm13206132. This article has 6 citations.

## Artifacts

- [Edison artifact artifact-00](Exfoliation_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.