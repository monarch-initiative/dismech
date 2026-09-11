---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T10:21:18.941440'
end_time: '2026-09-04T10:40:47.297006'
duration_seconds: 1168.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bilateral Microtia-Deafness-Cleft Palate Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 2
  off_topic: 1
  off_topic_references:
  - DOI:10.5152/iao.2019.7383
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bilateral_Microtia-Deafness-Cleft_Palate_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bilateral Microtia-Deafness-Cleft Palate Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bilateral Microtia-Deafness-Cleft Palate Syndrome** covering all of the
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
- **Disease Name:** Bilateral Microtia-Deafness-Cleft Palate Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bilateral Microtia-Deafness-Cleft Palate Syndrome** covering all of the
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


# Bilateral Microtia–Deafness–Cleft Palate Syndrome

## Executive summary

Bilateral microtia–deafness–cleft palate syndrome is an exceptionally rare congenital Mendelian disorder caused, in its defining family, by a homozygous missense variant in **HOXA2**. It is characterized by bilateral Marx type II microtia, prelingual symmetric severe-to-profound mixed hearing impairment, and partial/incomplete cleft palate. The entire syndrome-specific evidence base consists essentially of **four affected relatives in one consanguineous Iranian family** reported in 2008; unilateral cochlear absence was found in one person. Consequently, pedigree fractions must not be interpreted as population frequencies, and prevalence, penetrance outside that family, prognosis, and treatment-response statistics remain unknown. The association is catalogued as **MONDO:0012854** and linked to HOXA2 in contemporary disease–target resources. (alasti2009geneticsofmicrotia pages 11-14, alasti2009geneticsofmicrotia pages 18-20, OpenTargets Search: Bilateral microtia-deafness-cleft palate syndrome-HOXA2)

| Domain | Syndrome-specific established evidence | Evidence basis | Confidence/limitations |
|---|---|---|---|
| Identity | Bilateral microtia-deafness-cleft palate syndrome; MONDO:0012854; HOXA2-associated Mendelian disorder. | Disease–target aggregation identifies HOXA2 as the sole associated target (OpenTargets Search: Bilateral microtia-deafness-cleft palate syndrome-HOXA2). | High for MONDO identity and HOXA2 association; other identifiers should not be inferred without direct database confirmation. |
| Human evidence base | Reported in one consanguineous Iranian pedigree with four affected individuals. | Original family report and subsequent HOX-disorder review (alasti2009geneticsofmicrotia pages 11-14, alasti2009geneticsofmicrotia pages 18-20). | Very limited: four relatives from one family; percentages calculated from this pedigree are not population frequencies. |
| Genetics | Autosomal-recessive segregation of homozygous HOXA2 p.Gln186Lys (p.Q186K), affecting a highly conserved homeodomain residue. | Primary linkage and sequencing study (alasti2009geneticsofmicrotia pages 11-14, alasti2009geneticsofmicrotia pages 18-20). | Strong segregation evidence in the original pedigree; historical variant interpretation predates current ACMG/AMP criteria, so a contemporary laboratory should reassess classification and transcript-level HGVS nomenclature. |
| Mapping and functional support | Linked to chromosome 7p14.3–p15.3 with maximum multipoint LOD 4.17; p.Q186K was absent from 231 Iranian and 109 Belgian controls. Structural modeling predicted loss of a homeodomain–DNA phosphate hydrogen bond and altered DNA binding. | Primary human genetic and computational study (alasti2009geneticsofmicrotia pages 11-14). | Strong linkage and rarity evidence; protein effect was modeled computationally rather than demonstrated with a syndrome-specific cellular functional assay. |
| Core phenotype | Congenital bilateral Marx type II microtia, prelingual symmetric severe-to-profound mixed hearing impairment, and partial/incomplete cleft palate. | Original report summarized in authoritative review (alasti2009geneticsofmicrotia pages 11-14). | High within the pedigree; penetrance and expressivity in unrelated families remain unknown. |
| Inner-ear involvement | Unilateral cochlear absence occurred in one affected individual, showing that inner-ear involvement is possible in addition to predominant external- and middle-ear disease. | Human clinical/imaging observation (alasti2009geneticsofmicrotia pages 11-14). | Moderate; single-patient observation and not a reliable frequency estimate. |
| Mechanism | Reduced HOXA2 homeobox transcription-factor function is inferred to impair second-pharyngeal-arch cranial-neural-crest identity and patterning, leading to malformed pinna and middle-ear skeletal structures; abnormal palate development provides a route to cleft palate. | Human variant modeling plus Hoxa2 mouse developmental studies (alasti2009geneticsofmicrotia pages 11-14, cox2014thegeneticsof pages 3-3, alasti2009geneticsofmicrotia pages 5-8). | Biologically compelling but partly inferred; the complete molecular chain has not been demonstrated in patient-derived cells or tissues. |
| Mouse-model evidence | Hoxa2-deficient mice lack pinnae, have transformed or duplicated middle-ear skeletal elements and a wide secondary-palate cleft, and die shortly after birth; ectopic expression experiments establish a dosage-sensitive role in pharyngeal-arch identity. | Knockout/ developmental evidence summarized in reviews and primary-model literature (alasti2009geneticsofmicrotia pages 11-14, cox2014thegeneticsof pages 3-3, cox2014thegeneticsof pages 3-4). | Strong developmental evidence, but null-mouse lethality and severity exceed the surviving human missense phenotype. |
| Diagnosis | Molecular confirmation should identify biallelic HOXA2 variants after detailed craniofacial examination and audiologic assessment; diagnostic ABR should be performed by 2–3 months, with air- and bone-conduction thresholds. Temporal-bone CT/MRI is selected according to age, anatomy, suspected inner-ear disease, and surgical planning. | HOXA2 family evidence plus general microtia/atresia expert guidance (truong2022integratedmicrotiaand pages 4-6, truong2022integratedmicrotiaand pages 2-4, paul2021congenitalabnormalitiesassociated pages 3-3). | Genetic testing is syndrome-directed; audiologic and imaging pathways are extrapolated because no syndrome-specific diagnostic guideline exists. |
| Management | Phenotype-directed multidisciplinary care may include early amplification and speech/language intervention, bone-conduction hearing systems when appropriate, anatomy-dependent atresia/hearing surgery, cleft-palate repair and speech therapy, and coordinated auricular reconstruction. | General microtia/atresia consensus and integrated-care recommendations (truong2022integratedmicrotiaand pages 4-6, zhang2019internationalconsensusrecommendations pages 2-3, truong2022integratedmicrotiaand pages 16-17, truong2022integratedmicrotiaand pages 1-2). | No HOXA2-specific outcome data; treatment must account for the mixed hearing loss and possible cochlear aplasia rather than assuming isolated conductive loss. |
| Epidemiology and natural history | Syndrome-specific prevalence, incidence, carrier frequency, sex ratio, life expectancy, and longitudinal progression are unknown. | Only one pedigree has established the recessive syndromic phenotype (alasti2009geneticsofmicrotia pages 11-14, alasti2009geneticsofmicrotia pages 18-20). | Very low epidemiologic certainty; general microtia prevalence or sex ratios must not be assigned to this syndrome. |
| Disease-modifying therapy and trials | No established pharmacologic, gene, RNA, or cell therapy and no syndrome-specific interventional trial were identified; current care treats hearing, palate, speech, and reconstructive consequences. | Available disease evidence and microtia management literature (OpenTargets Search: Bilateral microtia-deafness-cleft palate syndrome-HOXA2, truong2022integratedmicrotiaand pages 4-6, zhang2019internationalconsensusrecommendations pages 2-3). | Search-dependent negative finding; broader ear-reconstruction or hearing-device studies are not evidence for correction of the HOXA2 developmental lesion. |
| 2024 development | A distant approximately 600-kb craniofacial global control region was shown to interact with anterior HOXA genes; deletion in mice produced highly penetrant skull defects and orofacial clefts resembling Hoxa2-null phenotypes, while human copy-number changes were associated with severe craniofacial abnormalities. | Human embryonic epigenomics, mouse deletion experiments, and human CNV cases (wilderman2024adistantglobal pages 13-13, wilderman2024adistantglobal pages 1-2). | Important HOXA regulatory insight, but not direct evidence that this control region causes the named p.Q186K recessive syndrome or changes current treatment. |


*Table: This table separates observations established in the single reported HOXA2-associated pedigree from mouse-mechanistic evidence and clinical guidance extrapolated from broader microtia, hearing-loss, and cleft-care literature.*

## Evidence-grading note

In this report, **direct evidence** means observations from the original human family; **supportive human evidence** means other HOXA2-related microtia families; **model evidence** means principally mouse developmental experiments; and **extrapolated care** means guidance for microtia/aural atresia, congenital hearing loss, or cleft palate generally. This distinction is essential because no syndrome-specific cohort, guideline, therapeutic trial, patient-derived model, or longitudinal natural-history study was identified.

## 1. Disease information

### Definition and nomenclature

The disorder is a congenital craniofacial and auditory developmental syndrome comprising:

* bilateral microtia, reported as **Marx type II**;
* congenital/prelingual, symmetric, severe-to-profound **mixed** hearing impairment; and
* partial or incomplete cleft palate.

The original article’s abstract described “a consanguineous Iranian family segregating with autosomal-recessive bilateral microtia, mixed symmetrical severe to profound hearing impairment, and partial cleft palate.” The report was published in April 2008 in *The American Journal of Human Genetics* as Alasti et al., “A Mutation in HOXA2 Is Responsible for Autosomal-Recessive Microtia in an Iranian Family,” DOI: https://doi.org/10.1016/j.ajhg.2008.03.014, PMID **18394579**. An erratum appeared in September 2008, DOI: https://doi.org/10.1016/j.ajhg.2008.08.014; it did not alter the principal genetic result. (alasti2009geneticsofmicrotia pages 18-20, alasti2008amutationin pages 1-1)

### Identifiers

* **MONDO:** MONDO:0012854.
* **OMIM phenotype:** commonly catalogued as *Microtia, hearing impairment, and cleft palate* / bilateral microtia–deafness–cleft palate syndrome; MIM **612290** is reported in secondary disease tables. Because the retrieved primary evidence did not reproduce the live OMIM record, database curators should verify the current preferred title and number before import.
* **Gene:** **HOXA2**, homeobox A2; Ensembl ENSG00000105996. Open Targets identifies HOXA2 as the sole associated target for MONDO:0012854. (OpenTargets Search: Bilateral microtia-deafness-cleft palate syndrome-HOXA2)
* **Orphanet:** no syndrome-specific ORPHA number was confirmed in the retrieved evidence.
* **ICD-10/ICD-11 and MeSH:** no unique syndrome-specific code or heading was identified. Component abnormalities should be coded separately rather than assigning a broader syndrome code without verification.

Common names include **bilateral microtia-deafness-cleft palate syndrome**, **HOXA2-related autosomal-recessive microtia**, and **microtia, hearing impairment, and cleft palate**. “HOXA2-related disorder” is broader and also includes autosomal-dominant, usually nonsyndromic microtia with variable hearing impairment; those dominant conditions should not be merged with this recessive phenotype. Supportive reports show that heterozygous HOXA2 loss-of-function can cause dominant bilateral microtia and variable hearing loss without the defining cleft-palate phenotype. (meddaugh2020novelhoxa2variant pages 3-3)

The evidence is **aggregated disease-level literature derived from a small family study**, not EHR-derived individual-patient data.

## 2. Etiology

### Causal factor

The defining cause is a **germline homozygous HOXA2 homeodomain missense variant, p.Gln186Lys (p.Q186K)**, segregating recessively in the Iranian pedigree. Genome-wide linkage mapped the locus to **7p14.3–p15.3**, with a maximum multipoint LOD score of **4.17**. The variant was absent from **231 Iranian and 109 Belgian controls**—680 control chromosomes if all were diploid and unrelated. Structural modeling predicted displacement of the mutant lysine side chain from a DNA phosphate group, loss of a hydrogen bond, and impaired DNA-binding activity. (alasti2009geneticsofmicrotia pages 11-14)

A commonly reported transcript-level rendering is **c.557A>C (p.Gln186Lys)**, but clinical laboratories should normalize HGVS against the current MANE transcript rather than copying historical nomenclature uncritically. The original interpretation predates ACMG/AMP standards. The combination of strong linkage, recessive segregation, absence from controls, conservation, phenotype concordance, and model support is compelling, but the retrieved evidence did not show a patient-cell transcription assay. Thus, **pathogenic/likely pathogenic reassessment in a current clinical laboratory** is preferable to treating the historical label as an automatically current ClinVar classification.

### Risk factors

* **Genetic:** biallelic pathogenic HOXA2 variation; consanguinity increased the probability of homozygosity in the original family.
* **Family history:** an affected sibling or similarly affected relative is a major diagnostic clue.
* **Environmental, infectious, lifestyle, maternal-age, sex, and occupational risks:** none have been demonstrated for this molecularly defined syndrome.
* **Modifier genes:** none established. BMP4, BMP5 and TWSG1 have been investigated within Hoxa2-regulated auricular programs, but they are not validated modifiers of the human p.Gln186Lys syndrome. (sparascio2017studyofmolecular pages 16-20)

General microtia studies discuss maternal/perinatal and environmental associations, but those data must not be assigned to this single-gene syndrome. General microtia prevalence and associated-anomaly figures likewise do not estimate this syndrome’s incidence. (llanos2023riskfactorsfor pages 5-7, wahdini2024genotypephenotypeassociationsin pages 14-16)

### Protective factors and gene–environment interaction

No protective allele, diet, exposure, medication, or lifestyle intervention is known. No syndrome-specific gene–environment interaction has been demonstrated. Standard avoidance of recognized teratogens is sound prenatal practice but is not proven to prevent HOXA2-associated disease.

## 3. Phenotypes

All principal findings are congenital, although hearing impairment may be documented only after newborn screening or diagnostic audiology.

| Phenotype | Type and characteristics | Frequency evidence | Suggested HPO term |
|---|---|---|---|
| Bilateral Marx type II microtia | Physical sign; congenital, stable structural malformation; severity substantial but short of anotia | Core finding in the four reported relatives; not a population frequency | Bilateral microtia, **HP:0008551**; Microtia, **HP:0008551**—verify the current bilateral child term/version |
| Mixed hearing impairment | Functional sign; prelingual, symmetric, severe-to-profound; likely lifelong without habilitation | Core family phenotype | Mixed hearing impairment, **HP:0000410**; Severe hearing impairment, **HP:0012715**; Profound hearing impairment, **HP:0012714**; Congenital hearing impairment, **HP:0008527** |
| Partial/incomplete cleft palate | Congenital physical sign; stable anatomical defect until repaired | Core family phenotype | Cleft palate, **HP:0000175**; Incomplete cleft palate—use current HPO child term if available |
| Unilateral cochlear aplasia | Imaging/anatomical abnormality; congenital, nonprogressive | One of four reported patients, but **1/4 is not a generalizable frequency** | Absent cochlea, **HP:0011372**; Unilateral abnormality qualifier where supported |
| External/middle-ear malformation | Structural correlate inferred from microtia and mixed conductive component; directly emphasized in the clinical review | Predominant affected auditory compartments; exact person-level frequency unavailable | Abnormal external ear morphology, **HP:0000356**; Abnormal middle ear morphology, **HP:0000370** |

The literature does not establish developmental delay, intellectual disability, seizures, renal disease, cardiac disease, immunodeficiency, or metabolic abnormalities as features of this syndrome. These should not be added based merely on broader syndromic-microtia differentials.

### Quality-of-life consequences

No syndrome-specific EQ-5D, SF-36, PROMIS, speech, educational, or psychosocial data exist. Expected burdens include impaired access to spoken language from bilateral severe/profound prelingual hearing loss, feeding and speech difficulties from cleft palate, repeated procedures, and appearance-related psychosocial stress. These are extrapolations. A 2023 narrative review of 64 microtia/craniofacial-microsomia studies found care stressful from diagnosis, possible social and language risks, and generally high satisfaction after reconstruction/canaloplasty; it did not study this HOXA2 syndrome specifically.

## 4. Genetic and molecular information

**HOXA2** encodes a nuclear homeobox transcription factor that binds DNA through its homeodomain and specifies positional identity during craniofacial development. The disease allele is germline, not somatic. No recurrent founder allele, carrier frequency, gnomAD frequency, or additional unrelated recessive family with the full triad was established in the retrieved evidence.

The p.Gln186Lys substitution affects a highly conserved residue in the DNA-binding homeodomain. Its modeled effect—loss of a DNA-contact hydrogen bond—supports reduced transcription-factor function. Complete biochemical loss of function, gain of function, or dominant-negative activity was not directly demonstrated in patient cells; the recessive inheritance and mouse loss-of-function concordance favor a **hypomorphic/loss-of-function mechanism**. (alasti2009geneticsofmicrotia pages 11-14)

Other heterozygous nonsense/frameshift HOXA2 alleles cause dominant microtia with variable hearing impairment, demonstrating dosage sensitivity but a distinguishable phenotype and inheritance pattern. Reported dominant alleles include truncating variants around Glu224, Glu229, and Gln235; these are useful differential evidence, not variants causing the defining recessive syndrome. (meddaugh2020novelhoxa2variant pages 3-3)

No syndrome-specific:

* modifier gene;
* DNA-methylation “episignature”;
* histone/chromatin biomarker;
* pathogenic aneuploidy, translocation, or inversion;
* somatic variant;
* repeat expansion; or
* mitochondrial lesion

has been reported.

A 2024 study identified an approximately **600-kb noncoding global control region** between NPVF and NFE2L3 that interacts over long distances with anterior HOXA genes in human and mouse embryonic craniofacial tissue. Mouse deletion caused perinatal lethality, skull defects, and highly penetrant orofacial clefts resembling Hoxa2-null phenotypes; two humans with de novo copy-number changes had severe craniofacial abnormalities. This is important evidence for HOXA regulatory architecture, but it is **not evidence that those CNVs cause MONDO:0012854**, nor does it reclassify p.Gln186Lys. (wilderman2024adistantglobal pages 13-13, wilderman2024adistantglobal pages 1-2)

## 5. Environmental information

No toxin, radiation exposure, pollution source, infection, diet, smoking, alcohol exposure, or other lifestyle factor has been shown to cause or modify this HOXA2 syndrome. It is noninfectious and nontransmissible. Environmental associations reported for microtia overall concern etiologically heterogeneous cases and cannot be causally imported into this Mendelian entry.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous HOXA2 p.Gln186Lys leads to** alteration of a conserved homeodomain residue.
2. **The altered homeodomain is predicted to lead to** loss of a DNA-contact hydrogen bond and reduced/abnormal DNA binding; this step is computationally supported rather than demonstrated in patient cells. (alasti2009geneticsofmicrotia pages 11-14)
3. **Reduced HOXA2 transcriptional function is inferred to lead to** defective positional specification and patterning of rhombomere-4-derived cranial neural crest populating the second pharyngeal arch.
4. **Defective second-arch identity leads to** abnormal proliferation/differentiation and homeotic patterning of neural-crest-derived auricular and middle-ear mesenchyme.
5. **Auricular-patterning failure results in** bilateral microtia; **middle-ear skeletal malformation results in** a major conductive component of hearing loss. Mouse experiments strongly support these branches. (cox2014thegeneticsof pages 3-3, cox2014thegeneticsof pages 3-4, alasti2009geneticsofmicrotia pages 5-8)
6. **A parallel or downstream disturbance of otic development results in** a sensorineural component and, in one human, unilateral cochlear aplasia; the exact human cellular route is not demonstrated.
7. **Abnormal HOXA2-dependent palatal growth/patterning leads to** incomplete fusion of the secondary palate and partial cleft palate; this is supported strongly by Hoxa2-null mice and inferred for humans. (alasti2009geneticsofmicrotia pages 11-14)
8. **The combined ear and palate lesions result in** congenital craniofacial difference, severe-to-profound prelingual mixed hearing loss, and risks to feeding, speech, language, education, and psychosocial well-being.

### Pathway and cellular detail

HOXA2 is better understood as a **developmental transcriptional identity regulator** than as a component of one canonical kinase cascade. Its critical context is the HOX regulatory network in cranial neural crest and pharyngeal-arch mesenchyme. Proposed downstream auricular effectors include **BMP4, BMP5, and TWSG1**, linking HOXA2 to BMP-dependent cartilage proliferation and differentiation, but their exact contribution to the human syndrome is unproven. (sparascio2017studyofmolecular pages 16-20)

Relevant suggested ontology annotations include:

* **GO biological process:** anterior/posterior pattern specification (GO:0009952); embryonic cranial skeleton morphogenesis (GO:0048701); neural crest cell development (GO:0014032); pharyngeal system development (GO:0060037); ear morphogenesis (GO:0042471); palate development (GO:0060021); regulation of transcription by RNA polymerase II (GO:0006357).
* **GO molecular function:** sequence-specific DNA-binding transcription-factor activity (use the current HOX-specific child term); DNA binding (GO:0003677).
* **GO cellular component:** nucleus (GO:0005634); transcription regulator complex (GO:0005667, where experimentally appropriate).
* **Cell Ontology:** neural crest cell (**CL:0000333**); cranial neural crest cell—use current CL term if available; chondrocyte (**CL:0000138**); osteoblast (**CL:0000062**); fibroblast (**CL:0000057**); otic epithelial and palatal mesenchymal cells require version-checked mappings.

There is no evidence for primary inflammation, autoimmunity, immunodeficiency, fibrosis, ischemia, enzyme deficiency, channelopathy, or systemic metabolic disturbance. No syndrome-specific patient transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial transcriptome, CRISPR screen, organoid, or multi-omics profile was identified. Broader 2024 microtia cartilage studies reporting noncoding-RNA and extracellular-matrix signatures used nonsyndromic tissue and should not be annotated as HOXA2-syndrome molecular profiles.

## 7. Anatomical structures affected

Primary sites are the **bilateral auricles/pinnae**, external and middle auditory apparatus, palate, and potentially inner ear/cochlea. The external and middle ear derive substantially from first- and second-pharyngeal-arch structures, whereas the inner ear has otic-placode origins. HOXA2 is especially important in second-arch cranial-neural-crest mesenchyme; mixed arch origins help explain why some auricular substructures, such as the tragus, may be relatively spared. (cox2014thegeneticsof pages 3-4, alasti2009geneticsofmicrotia pages 5-8)

Suggested anatomical mappings:

* auricle/pinna — **UBERON:0001757**;
* external ear — UBERON current external-ear term;
* middle ear — **UBERON:0001756**;
* auditory ossicle — **UBERON:0001684**;
* cochlea — **UBERON:0001844**;
* secondary palate — **UBERON:0001717**;
* second pharyngeal arch — use the current UBERON developmental-structure term;
* cranial neural crest — use the current UBERON/CL developmental mapping.

Subcellular dysfunction is centered on the **nucleus** and DNA-bound transcriptional regulatory complexes. Lateralization is bilateral for microtia and reported hearing impairment; cochlear aplasia was unilateral in one individual.

## 8. Temporal development

The initiating defect acts during **embryonic craniofacial organogenesis**, particularly pharyngeal-arch, auricular, ossicular, otic, and palatal development. The anatomical malformations are congenital and structurally stable rather than inflammatory, episodic, or relapsing.

Hearing impairment is congenital/prelingual and expected to be lifelong, although its functional impact can improve markedly with early amplification, surgery when anatomically suitable, and communication intervention. Cleft palate persists until repaired; residual velopharyngeal, speech, dental, or otologic problems can continue afterward. No syndrome-specific stages, progression rate, remission pattern, or adult natural history have been documented.

Critical clinical windows are early infancy for objective hearing diagnosis and amplification, infancy for feeding and palate planning, early childhood for speech/language intervention, and later childhood for anatomy-dependent auditory and auricular reconstruction. These windows derive from general care standards, not a HOXA2-specific trial. (truong2022integratedmicrotiaand pages 4-6, truong2022integratedmicrotiaand pages 2-4)

## 9. Inheritance and population

Inheritance in the defining pedigree is **autosomal recessive**. For two heterozygous carrier parents, standard Mendelian counseling gives each pregnancy a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele, assuming full genotype penetrance. Actual penetrance of p.Gln186Lys cannot be estimated independently from one pedigree.

Only four affected individuals from one consanguineous Iranian family were reported in the available HOX-disorder literature. There are no defensible syndrome-specific estimates of prevalence, incidence, sex ratio, carrier frequency, geographic distribution, age distribution, founder effect, germline-mosaicism rate, or reproductive fitness. (alasti2009geneticsofmicrotia pages 11-14, alasti2009geneticsofmicrotia pages 18-20)

General microtia estimates—such as 0.8–17.5 per 10,000 births, male predominance, or mainly unilateral disease—describe heterogeneous microtia and **must not populate this syndrome’s epidemiology fields**. A 2024 systematic review included 1,459 microtia patients across 40 phenotype papers but did not establish syndrome-specific population statistics for the recessive HOXA2 triad. (wahdini2024genotypephenotypeassociationsin pages 14-16)

Anticipation is not expected for a missense allele and has not been observed. Variable expressivity is suggested by cochlear aplasia in only one relative, but precise penetrance and expressivity remain unknown.

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with congenital bilateral microtia plus objective bilateral hearing loss and cleft-palate examination. Infants with microtia/atresia should be referred directly to pediatric audiology regardless of newborn-screening outcome. Diagnostic **auditory brainstem response** should ideally be completed by two months and no later than three months, including air- and bone-conduction thresholds and masked bone conduction where feasible. Tympanometry and otoacoustic emissions should be performed where anatomy permits, followed by behavioral audiometry from approximately six months and regular monitoring through early childhood. These recommendations are extrapolated from expert microtia/atresia guidance. (truong2022integratedmicrotiaand pages 4-6, truong2022integratedmicrotiaand pages 2-4)

Temporal-bone high-resolution noncontrast CT defines canal, ossicular, middle-ear, and cochlear anatomy and is useful for reconstructive candidacy. Routine CT is often deferred until approximately age five or until operative planning, limiting radiation exposure; earlier imaging may be justified for sensorineural loss, suspected cholesteatoma/fistula, or major inner-ear disease. Diffusion-weighted MRI is useful when cholesteatoma is suspected, and MRI is important for cochlear nerve and membranous-labyrinth assessment when cochlear implantation is considered. (truong2022integratedmicrotiaand pages 4-6, paul2021congenitalabnormalitiesassociated pages 3-3)

Cleft evaluation should include feeding, airway, otologic, speech-language, dental/orthodontic, and velopharyngeal assessment. No blood chemistry, urine test, enzyme assay, biopsy, metabolite, or circulating biomarker diagnoses the syndrome.

### Genetic testing strategy

1. In a patient with the defining triad and recessive pedigree, perform **sequence analysis of HOXA2 with deletion/duplication analysis**.
2. A comprehensive hearing-loss/craniofacial-malformation panel including HOXA2 is reasonable when the phenotype is less specific.
3. **Trio WES or WGS** is preferred when targeted testing is negative, when additional anomalies suggest another syndrome, or when noncoding/structural variation is suspected.
4. **Chromosomal microarray** is useful for multiple congenital anomalies or concern for CNVs, including 22q11.2 deletion and regulatory rearrangements; it does not reliably detect a small HOXA2 missense variant.
5. Karyotype/FISH are reserved for cytogenetically indicated cases. Mitochondrial and repeat-expansion testing are not routinely indicated.

Familial variants require Sanger or equivalent orthogonal confirmation and segregation analysis. RNA sequencing is not an established diagnostic test for p.Gln186Lys, although it may help investigate splice or regulatory variants in unresolved cases.

### Differential diagnosis

Important alternatives include:

* **Autosomal-dominant HOXA2-related microtia:** vertical transmission, often nonsyndromic and without cleft palate.
* **Treacher Collins syndrome:** TCOF1/POLR1D/POLR1C-related mandibulofacial dysostosis, malar/mandibular hypoplasia and eyelid findings.
* **Nager syndrome:** mandibulofacial dysostosis plus preaxial upper-limb defects.
* **22q11.2 deletion syndrome:** palatal defect with cardiac, immune, calcium, and characteristic craniofacial findings.
* **Branchio-oto-renal spectrum:** branchial anomalies, preauricular pits and renal disease.
* **HOXA1-related disorder:** horizontal-gaze palsy, brainstem/autonomic and cardiovascular findings, and sensorineural deafness.
* **Craniofacial microsomia/OAV spectrum:** facial asymmetry, epibulbar dermoids and vertebral abnormalities.
* **Diamond–Blackfan anemia-associated craniofacial disease:** macrocytic anemia/red-cell aplasia.

There are no standardized syndrome-specific clinical diagnostic criteria; molecular confirmation is therefore important.

### Screening

This syndrome is not part of routine biochemical newborn screening. Applicable measures are universal newborn hearing screening, immediate diagnostic follow-up, and **cascade testing** for the familial HOXA2 variant. Carrier, prenatal, and preimplantation testing are technically possible once the familial pathogenic variant is established.

## 11. Outcome and prognosis

No survival curves, mortality rates, life-expectancy estimates, hospitalization rates, or validated prognostic biomarkers exist. The four reported human patients survived beyond the neonatal period, unlike Hoxa2-null mice; therefore, mouse neonatal lethality should not be assigned to affected humans. (alasti2009geneticsofmicrotia pages 11-14)

Likely long-term morbidity is auditory-communication disability, reconstructive burden, and cleft-associated feeding, speech, dental, and psychosocial effects. Prognosis depends more on anatomy and access/timing of habilitation than on a demonstrated progressive molecular process. Particularly relevant prognostic features include residual cochlear and cochlear-nerve anatomy, bone-conduction thresholds, middle-ear anatomy, device use, age at intervention, palate repair result, and access to speech/language and educational services. No molecular marker predicts severity.

## 12. Treatment

There is no therapy that reverses the embryonic HOXA2 lesion. Care is individualized and multidisciplinary, involving clinical genetics, pediatric otolaryngology, audiology, cleft/craniofacial surgery, plastic surgery, speech-language pathology, dentistry/orthodontics, pediatrics, psychology, and educational services. Close coordination is essential because canal/hearing surgery can affect later auricular reconstruction. (zhang2019internationalconsensusrecommendations pages 2-3, truong2022integratedmicrotiaand pages 1-2)

### Hearing and communication

For bilateral disease, expert guidance recommends diagnostic assessment by 2–3 months, amplification by about **4 months**, and early intervention by **3–6 months**. Nonimplantable bone-conduction systems—softband BAHA/Ponto-type processors or adhesive systems—are common early options where cochlear function is adequate. Because the syndrome causes **mixed**, not necessarily purely conductive, loss and can include cochlear aplasia, treatment must be based on ear-specific air/bone thresholds and imaging. Cochlear implantation may be considered only when sensorineural loss is severe/profound and a stimulable cochlea/cochlear nerve is present; unilateral cochlear absence can make that side unsuitable. (truong2022integratedmicrotiaand pages 4-6, silva2023taskforceguideline pages 2-3)

Atresiaplasty or middle-ear reconstruction requires adequate inner-ear function and favorable anatomy. International consensus supports the Jahrsdoerfer CT scale and generally considers a score of at least 7 favorable. Implantable bone-conduction or middle-ear devices are typically considered after approximately age five, depending on device approval, skull thickness, anatomy, and local practice. (zhang2019internationalconsensusrecommendations pages 2-3)

Suggested NCIt concepts include **Hearing Aid Device**, **Bone Conduction Hearing Device**, **Cochlear Implantation**, **Auditory Rehabilitation**, and **Speech Therapy**; exact NCIt codes should be version-checked.

### Palate and speech

Primary palatoplasty is generally performed during infancy within an accredited cleft pathway, followed by surveillance for fistula, velopharyngeal dysfunction, otitis media, hearing deterioration, dentofacial growth, and articulation. Speech-language therapy is often required. Exact timing and technique should follow the treating cleft team’s protocol; no HOXA2-specific comparison exists.

### Auricular reconstruction

Options include autologous costal cartilage reconstruction, porous polyethylene framework, or an adhesive/osseointegrated prosthesis. Consensus sources place autologous cartilage reconstruction approximately from **5–9 years onward**, often around nine years when rib cartilage is adequate; porous polyethylene may be considered after about five years. Canal surgery should be sequenced with the reconstruction method—generally before polyethylene reconstruction but after or combined with rib-cartilage reconstruction. (zhang2019internationalconsensusrecommendations pages 2-3, truong2022integratedmicrotiaand pages 16-17)

### Pharmacotherapy and advanced therapeutics

No disease-specific drug, pharmacogenomic recommendation, gene therapy, genome editing, RNA therapy, cell therapy, immunotherapy, or targeted molecular therapy exists. Medicines are used only for routine perioperative care, otitis, pain, or other complications.

### Trials

No interventional trial specifically for MONDO:0012854 or HOXA2 p.Gln186Lys was identified. Trials of hearing devices or ear reconstruction in heterogeneous microtia/ear-aplasia populations are not disease-modifying and cannot supply syndrome-specific response rates.

## 13. Prevention

Because the disorder is inherited, lifestyle modification, vaccination, sanitation, and prophylactic medication cannot prevent expression in a fetus who inherits the causal biallelic genotype.

* **Primary prevention:** nondirective genetic counseling; carrier testing of at-risk relatives; reproductive options including prenatal diagnosis and preimplantation genetic testing for the known familial variant.
* **Secondary prevention:** newborn hearing screening followed by rapid diagnostic ABR, molecular diagnosis, amplification, and early communication intervention. These prevent avoidable developmental consequences, not the congenital malformations.
* **Tertiary prevention:** palate repair, hearing habilitation, speech-language therapy, dental/orthodontic care, psychosocial and educational support, and surveillance for ear-canal or reconstructive complications.

For carrier parents, recurrence counseling is 25% per pregnancy under standard autosomal-recessive assumptions. Testing should be accompanied by counseling about uncertain phenotype prediction, especially the risk of inner-ear involvement.

## 14. Other species and natural disease

No naturally occurring animal disease proven to reproduce the complete human bilateral microtia–deafness–cleft-palate syndrome from the orthologous p.Gln186Lys allele was identified. There is no zoonotic or cross-species transmission.

The most relevant ortholog is mouse **Hoxa2** in *Mus musculus* (NCBI Taxonomy **10090**). HOXA2 function is evolutionarily conserved in vertebrate craniofacial patterning. Other animal microtia caused by distinct genes or enhancer duplications may inform auricular morphogenesis but should not be represented as natural HOXA2 syndrome.

## 15. Model organisms

### Mouse models

Hoxa2-null mice lack the external pinna, exhibit transformations/duplications of middle-ear bones, and develop a wide secondary-palate cleft. They die within about 24 hours, probably because the cleft prevents effective feeding. These models strongly recapitulate the affected anatomical systems but are more severe than the surviving human missense phenotype. (alasti2009geneticsofmicrotia pages 11-14)

Lineage and ectopic-expression experiments establish that Hoxa2 specifies second-pharyngeal-arch identity in cranial-neural-crest-derived mesenchyme. Loss produces homeotic transformation and duplicated first-arch-like skeletal elements; ectopic first-arch expression can produce mirror-image auricular duplication. These models are useful for dissecting pinna, auditory-meatus, ossicle, and palate morphogenesis. (cox2014thegeneticsof pages 3-3, alasti2009geneticsofmicrotia pages 5-8)

Dosage experiments also show that cranial neural crest is highly sensitive to Hoxa2 level: ectopic expression at approximately 60% of normal second-arch levels was sufficient for pinna duplication, while higher levels produced progressively broader homeotic or destructive craniofacial phenotypes. This supports dosage sensitivity but does not quantify residual activity of human p.Gln186Lys.

### Advanced models and limitations

The 2024 global-control-region deletion mouse provides a regulatory model for anterior HOXA insufficiency and orofacial clefting, not a precise knock-in model of the human missense allele. (wilderman2024adistantglobal pages 1-2)

No syndrome-specific p.Gln186Lys knock-in mouse, zebrafish model, patient-derived fibroblast/iPSC line, cranial-neural-crest culture, ear organoid, palate organoid, or CRISPR rescue study was identified. A priority model would be an isogenic human iPSC pair differentiated into cranial neural crest and chondro-osteogenic derivatives, coupled to HOXA2 occupancy and target-gene assays. Such work could distinguish partial loss of DNA binding from altered target specificity and test why the human phenotype is viable whereas complete mouse loss is lethal.

## Recent developments and research priorities

The most important 2023–2024 development is not a new treatment but recognition that anterior HOXA expression depends on distant, tissue-specific regulatory architecture. Human embryonic craniofacial epigenomics and mouse deletion experiments now show that noncoding structural variants far from HOXA2 can perturb the same developmental program. Meanwhile, a 2024 systematic review confirmed substantial genetic heterogeneity across microtia and concluded that more complete genotype–phenotype datasets are needed. These findings support using WGS and CNV analysis in unresolved cases, but they do not expand the proven case count for the defining recessive syndrome. (wilderman2024adistantglobal pages 13-13, wilderman2024adistantglobal pages 1-2, wahdini2024genotypephenotypeassociationsin pages 14-16)

The highest-priority knowledge gaps are: identification of unrelated biallelic HOXA2 cases; contemporary ACMG/AMP curation and population-frequency analysis of p.Gln186Lys; standardized deep phenotyping of auditory canals, ossicles, cochleae and palate; long-term hearing, speech, educational and psychosocial outcomes; and patient-derived functional models. Until such data exist, the disease knowledge-base entry should prominently state **“ultra-rare; evidence based on one family; frequencies and prognosis unknown.”**

References

1. (alasti2009geneticsofmicrotia pages 11-14): F Alasti and G Van Camp. Genetics of microtia and associated syndromes. Mar 2009. URL: https://doi.org/10.1136/jmg.2008.062158, doi:10.1136/jmg.2008.062158. This article has 222 citations and is from a domain leading peer-reviewed journal.

2. (alasti2009geneticsofmicrotia pages 18-20): F Alasti and G Van Camp. Genetics of microtia and associated syndromes. Mar 2009. URL: https://doi.org/10.1136/jmg.2008.062158, doi:10.1136/jmg.2008.062158. This article has 222 citations and is from a domain leading peer-reviewed journal.

3. (OpenTargets Search: Bilateral microtia-deafness-cleft palate syndrome-HOXA2): Open Targets Query (Bilateral microtia-deafness-cleft palate syndrome-HOXA2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (cox2014thegeneticsof pages 3-3): Timothy C. Cox, Esra D. Camci, Siddharth Vora, Daniela V. Luquetti, and Eric E. Turner. The genetics of auricular development and malformation: new findings in model systems driving future directions for microtia research. European journal of medical genetics, 57 8:394-401, Aug 2014. URL: https://doi.org/10.1016/j.ejmg.2014.05.003, doi:10.1016/j.ejmg.2014.05.003. This article has 125 citations and is from a peer-reviewed journal.

5. (alasti2009geneticsofmicrotia pages 5-8): F Alasti and G Van Camp. Genetics of microtia and associated syndromes. Mar 2009. URL: https://doi.org/10.1136/jmg.2008.062158, doi:10.1136/jmg.2008.062158. This article has 222 citations and is from a domain leading peer-reviewed journal.

6. (cox2014thegeneticsof pages 3-4): Timothy C. Cox, Esra D. Camci, Siddharth Vora, Daniela V. Luquetti, and Eric E. Turner. The genetics of auricular development and malformation: new findings in model systems driving future directions for microtia research. European journal of medical genetics, 57 8:394-401, Aug 2014. URL: https://doi.org/10.1016/j.ejmg.2014.05.003, doi:10.1016/j.ejmg.2014.05.003. This article has 125 citations and is from a peer-reviewed journal.

7. (truong2022integratedmicrotiaand pages 4-6): Mai Thy Truong, Yi-Chun Carol Liu, Jocelyn Kohn, Sivakumar Chinnadurai, David A. Zopf, Melissa Tribble, Paul B. Tanner, Kathleen Sie, and Kay W. Chang. Integrated microtia and aural atresia management. Frontiers in Surgery, Dec 2022. URL: https://doi.org/10.3389/fsurg.2022.944223, doi:10.3389/fsurg.2022.944223. This article has 39 citations.

8. (truong2022integratedmicrotiaand pages 2-4): Mai Thy Truong, Yi-Chun Carol Liu, Jocelyn Kohn, Sivakumar Chinnadurai, David A. Zopf, Melissa Tribble, Paul B. Tanner, Kathleen Sie, and Kay W. Chang. Integrated microtia and aural atresia management. Frontiers in Surgery, Dec 2022. URL: https://doi.org/10.3389/fsurg.2022.944223, doi:10.3389/fsurg.2022.944223. This article has 39 citations.

9. (paul2021congenitalabnormalitiesassociated pages 3-3): Antoine Paul, Sophie Achard, François Simon, Nicolas Garcelon, Erea Noel Garabedian, Vincent Couloigner, Charlotte Celerier, and Françoise Denoyelle. Congenital abnormalities associated with microtia: a 10-years retrospective study. Jul 2021. URL: https://doi.org/10.1016/j.ijporl.2021.110764, doi:10.1016/j.ijporl.2021.110764. This article has 24 citations and is from a peer-reviewed journal.

10. (zhang2019internationalconsensusrecommendations pages 2-3): Tian-yu Zhang, Neil Bulstrode, Kay W. Chang, Yang-Sun Cho, Henning Frenzel, Dan Jiang, Bradley W. Kesser, Ralf Siegert, and Jean-Michel Triglia. International consensus recommendations on microtia, aural atresia and functional ear reconstruction. Aug 2019. URL: https://doi.org/10.5152/iao.2019.7383, doi:10.5152/iao.2019.7383. This article has 175 citations and is from a peer-reviewed journal.

11. (truong2022integratedmicrotiaand pages 16-17): Mai Thy Truong, Yi-Chun Carol Liu, Jocelyn Kohn, Sivakumar Chinnadurai, David A. Zopf, Melissa Tribble, Paul B. Tanner, Kathleen Sie, and Kay W. Chang. Integrated microtia and aural atresia management. Frontiers in Surgery, Dec 2022. URL: https://doi.org/10.3389/fsurg.2022.944223, doi:10.3389/fsurg.2022.944223. This article has 39 citations.

12. (truong2022integratedmicrotiaand pages 1-2): Mai Thy Truong, Yi-Chun Carol Liu, Jocelyn Kohn, Sivakumar Chinnadurai, David A. Zopf, Melissa Tribble, Paul B. Tanner, Kathleen Sie, and Kay W. Chang. Integrated microtia and aural atresia management. Frontiers in Surgery, Dec 2022. URL: https://doi.org/10.3389/fsurg.2022.944223, doi:10.3389/fsurg.2022.944223. This article has 39 citations.

13. (wilderman2024adistantglobal pages 13-13): Andrea Wilderman, Eva D’haene, Machteld Baetens, Tara N. Yankee, Emma Wentworth Winchester, Nicole Glidden, Ellen Roets, Jo Van Dorpe, Sandra Janssens, Danny E. Miller, Miranda Galey, Kari M. Brown, Rolf W. Stottmann, Sarah Vergult, K. Nicole Weaver, Samantha A. Brugmann, Timothy C. Cox, and Justin Cotney. A distant global control region is essential for normal expression of anterior hoxa genes during mouse and human craniofacial development. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44506-2, doi:10.1038/s41467-023-44506-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

14. (wilderman2024adistantglobal pages 1-2): Andrea Wilderman, Eva D’haene, Machteld Baetens, Tara N. Yankee, Emma Wentworth Winchester, Nicole Glidden, Ellen Roets, Jo Van Dorpe, Sandra Janssens, Danny E. Miller, Miranda Galey, Kari M. Brown, Rolf W. Stottmann, Sarah Vergult, K. Nicole Weaver, Samantha A. Brugmann, Timothy C. Cox, and Justin Cotney. A distant global control region is essential for normal expression of anterior hoxa genes during mouse and human craniofacial development. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44506-2, doi:10.1038/s41467-023-44506-2. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (alasti2008amutationin pages 1-1): Fatemeh Alasti, Abdorrahim Sadeghi, Mohammad Hossein Sanati, Mohammad Farhadi, Elliot Stollar, Thomas Somers, and Guy Van Camp. A mutation in hoxa2 is responsible for autosomal-recessive microtia in an iranian family. Sep 2008. URL: https://doi.org/10.1016/j.ajhg.2008.08.014, doi:10.1016/j.ajhg.2008.08.014. This article has 141 citations.

16. (meddaugh2020novelhoxa2variant pages 3-3): Hannah R. Meddaugh and Regina M. Zambrano. Novel hoxa2 variant presenting with microtia and variable hearing impairment in four-generation pedigree. Clinical Dysmorphology, 29:104-106, Apr 2020. URL: https://doi.org/10.1097/mcd.0000000000000297, doi:10.1097/mcd.0000000000000297. This article has 6 citations and is from a peer-reviewed journal.

17. (sparascio2017studyofmolecular pages 16-20): F Piceci Sparascio. Study of molecular basis of oculo-auricolo-vertebral-spectrum. Unknown journal, 2017.

18. (llanos2023riskfactorsfor pages 5-7): Sheyla Teresa Navas Llanos and Carmen Barba Guzmán Variña. Risk factors for microtia and preventive approaches. Sapienza: International Journal of Interdisciplinary Studies, 4:e23046, Sep 2023. URL: https://doi.org/10.51798/sijis.v4isi1.707, doi:10.51798/sijis.v4isi1.707. This article has 2 citations.

19. (wahdini2024genotypephenotypeassociationsin pages 14-16): Siti Isya Wahdini, Fina Idamatussilmi, Rachmaniar Pramanasari, Almas Nur Prawoto, Citrawati Dyah Kencono Wungu, Indri Lakhsmi Putri, and Gunadi. Genotype-phenotype associations in microtia: a systematic review. Orphanet Journal of Rare Diseases, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03142-9, doi:10.1186/s13023-024-03142-9. This article has 17 citations and is from a peer-reviewed journal.

20. (silva2023taskforceguideline pages 2-3): VAR Silva, HF Pauna, and J Lavinsky. Task force guideline of brazilian society of otology–hearing loss in children–part ii–treatment. Unknown journal, 2023.

## Artifacts

- [Edison artifact artifact-00](Bilateral_Microtia-Deafness-Cleft_Palate_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 2 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.5152/iao.2019.7383` (3 mentions) - International Consensus Recommendations on Microtia, Aural Atresia and Functional Ear Reconstruction
  - shared terms: microtia

Weighed against this report's own most characteristic terms: `disease`, `microtia`, `hoxa2`, `palate`, `syndrome`, `clinical`, `hearing`, `human`, `gene`, `genetic`, `bilateral`, `cleft`, `phenotype`, `loss`, `model`, `variant`, `affected`, `syndrome-specific`, `molecular`, `diagnostic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0009952` (1 mention) - the report calls it "GO biological process:** anterior/posterior pattern specification"; GO calls it **anterior/posterior pattern specification**
- `GO:0005634` (1 mention) - the report calls it "GO cellular component:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

Every term resolved, and every label the report gave matched.