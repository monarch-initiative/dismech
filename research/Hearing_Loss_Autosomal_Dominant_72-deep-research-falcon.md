---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T14:58:34.520044'
end_time: '2026-09-04T15:05:47.203182'
duration_seconds: 432.68
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 72
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 1
reference_validation:
  total_references: 1
  verified: 1
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 1
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 18
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.053
  labels_checked: 2
  labels_matching: 0
  labels_variant: 2
  unresolved_terms:
  - HP:0004076
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hearing_Loss_Autosomal_Dominant_72-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 72
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 72** covering all of the
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
- **Disease Name:** Hearing Loss Autosomal Dominant 72
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 72** covering all of the
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


# Hearing Loss, Autosomal Dominant 72 (DFNA72): Disease-Characteristics Report

## Executive summary and evidence status

Hearing loss, autosomal dominant 72 (DFNA72) is an exceptionally rare, postlingual, progressive, nonsyndromic sensorineural hearing-loss phenotype attributed to heterozygous **SLC44A4** dysfunction. The published human evidence derives from a single four-generation Chinese pedigree: **SLC44A4 c.466A>G (p.Met156Val)** was found in all eight tested affected relatives and none of 13 tested unaffected relatives. Functional studies showed impaired choline uptake and acetylcholine synthesis in transfected cells, while zebrafish *slc44a4* knockdown produced auditory-system abnormalities that were rescued with human SLC44A4 RNA. Nevertheless, independent human replication, variant-specific animal modeling, population epidemiology, and disease-specific treatment studies were not identified through 2024. The gene–disease association should therefore be treated more cautiously than a repeatedly replicated deafness-gene relationship. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 6-7)

| Domain | Established finding | Evidence type | Confidence or limitation |
|---|---|---|---|
| Human genetic evidence | One four-generation Chinese pedigree with 37 members linked DFNA72 to heterozygous **SLC44A4 c.466A&gt;G (p.Met156Val)**. The variant occurred in all 8 tested affected relatives and none of 13 tested unaffected relatives; it was also absent from 1,000 ethnically matched controls and 500 sporadic hearing-loss cases. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4, ma2017slc44a4mutationcauses pages 9-9) | Human pedigree; whole-exome sequencing; Sanger segregation; case-control screening | Strong within-family segregation and rarity evidence, but only one pedigree and one candidate variant have been reported; independent human replication was not identified through 2024. |
| Clinical phenotype | Postlingual tinnitus and sensorineural hearing loss began at approximately **26–30 years**. Early loss primarily involved **0.5–4 kHz**, especially **1–2 kHz**, with approximately **40–50 dB HL** thresholds and a U-shaped or bowl-shaped audiogram; it progressed to involve all frequencies while generally retaining the mid-frequency configuration. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4) | Human clinical and audiometric observations | Findings were consistent among reported affected relatives, but phenotype frequencies and severity estimates cannot be generalized beyond the single family. |
| Nonsyndromic classification | Tympanometry and temporal-bone imaging were normal. No retrocochlear disorder, vertigo, ototoxic-drug or sustained-noise exposure, or cardiovascular, diabetic, visual, neurologic, or other syndromic manifestations were reported. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 1-2) | Human clinical examination; auditory brainstem response; CT and MRI; exposure history | Supports nonsyndromic sensorineural hearing loss in the original pedigree, although long-term surveillance data are limited. |
| Cellular function | In SH-SY5Y cells, mutant SLC44A4 produced lower **radiolabeled choline uptake** and reduced **acetylcholine synthesis** relative to wild-type SLC44A4. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 5-6) | In-vitro transfection and biochemical assays | Supports impaired transporter activity, but SH-SY5Y cells are not native human olivocochlear neurons or cochlear cells; the precise dominant mechanism remains unresolved. |
| Proposed pathophysiology | Reduced choline transport is proposed to limit acetylcholine production and release by medial olivocochlear neurons, weakening efferent regulation and protection of outer hair cells and thereby causing progressive hearing loss. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 6-7) | Mechanistic inference integrating cellular assays and auditory physiology | Biologically plausible but not demonstrated directly in affected human cochleae; haploinsufficiency, dominant-negative activity, and gain of function have not been distinguished. |
| Zebrafish model | Morpholino-mediated **slc44a4** knockdown caused abnormal otoliths, fewer or malformed inner-ear and lateral-line hair cells and neuromasts, abnormal stereocilia, and balance or startle deficits. Human SLC44A4 RNA rescued otolith, hair-cell, stereocilia, and hearing phenotypes. (ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 6-7) | Zebrafish loss-of-function and rescue experiments | Supports conserved auditory function and gene-level causality, but morpholino knockdown is not a p.Met156Val knock-in and may model loss of function rather than the human dominant allele. |
| Epidemiology and replication | No disease-specific prevalence, incidence, carrier-frequency, founder-effect, sex-ratio, or geographic estimates were identified. No additional independently replicated DFNA72 family was found through 2024. | Evidence-gap assessment | DFNA72 appears exceptionally rare, but its population frequency and gene-disease validity cannot be quantified confidently from available evidence. |
| Treatment and trials | No SLC44A4-targeted drug, gene therapy, RNA therapy, or DFNA72-specific clinical trial was identified. Current care is supportive: serial audiometry, hearing aids when beneficial, communication rehabilitation, and cochlear-implant evaluation for severe or profound functional loss. | Standard hearing-loss management extrapolated to DFNA72; clinical-trial evidence gap | No DFNA72-specific response rates or comparative outcomes are available; supportive interventions do not correct the molecular defect. |


*Table: Compact evidence map summarizing the human genetic, clinical, cellular, zebrafish, epidemiologic, and treatment evidence for SLC44A4-associated DFNA72. It emphasizes that the association rests on one pedigree despite supportive functional experiments.*

## 1. Disease information

**Definition.** DFNA72 is a Mendelian form of autosomal-dominant, postlingual, nonsyndromic sensorineural hearing loss characterized in the original family by a U-shaped or “bowl-shaped” audiogram, predominant mid-frequency impairment, tinnitus at onset, and subsequent progression across the frequency range. “DFNA” denotes autosomal-dominant nonsyndromic deafness; “72” is the assigned locus/disease number. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4)

**Names and synonyms:**

- Hearing loss, autosomal dominant 72
- Deafness, autosomal dominant 72
- DFNA72
- SLC44A4-related autosomal-dominant nonsyndromic hearing loss
- SLC44A4-related postlingual mid-frequency sensorineural hearing loss
- Autosomal-dominant hereditary postlingual nonsyndromic mid-frequency hearing loss

**Identifiers.** The disease is represented principally by its DFNA72/OMIM nomenclature. An exact MONDO identifier and a disease-specific Orphanet identifier could not be verified from the retrieved evidence. ICD-10 and ICD-11 do not provide a DFNA72-specific code; practical coding uses the appropriate general sensorineural-hearing-loss category, such as ICD-10-CM H90.3 when bilateral. Relevant MeSH concepts include *Hearing Loss, Sensorineural* and *Hearing Loss, Hereditary*. These broad codes must not be interpreted as unique DFNA72 identifiers.

**Data provenance.** Disease-specific clinical information is not an aggregate EHR-derived phenotype. It comes primarily from one research pedigree, HN-01, containing 37 members across four generations, supplemented by in-vitro and zebrafish experiments. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 9-9)

## 2. Etiology

### Causal factor

The reported initiating lesion is a germline heterozygous missense substitution in **SLC44A4**, encoding solute carrier family 44 member 4/choline transporter-like protein 4: **c.466A>G (p.Met156Val)** in exon 6. It segregated with hearing loss in the informative relatives and was absent from 1,000 ethnically matched controls and 500 individuals with sporadic hearing loss. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4)

The evidence supports impaired transporter function, but the precise dominant molecular mechanism—haploinsufficiency, dominant-negative interference, altered trafficking, or another gain-of-abnormal-function effect—has not been resolved.

### Risk factors

- **Genetic:** carrying the familial p.Met156Val allele is the only demonstrated DFNA72-specific risk factor. Family history consistent with autosomal-dominant transmission materially increases prior probability.
- **Environmental:** affected relatives reportedly lacked sustained noise exposure and ototoxic-drug exposure, arguing against those factors as the primary cause in that family. No DFNA72-specific effect sizes for noise, smoking, diet, infection, occupational exposure, age, or sex exist. (ma2017slc44a4mutationcauses pages 1-2)
- **Age:** age is relevant to expression because onset was postlingual at approximately 26–30 years, but it is not an independent etiologic factor. (ma2017slc44a4mutationcauses pages 2-3)

### Protective factors and gene–environment interaction

No protective allele, modifier gene, dietary intervention, or pharmacologic prophylaxis has been demonstrated. The proposed loss of medial olivocochlear protection suggests that noise might aggravate cochlear injury, but this is a mechanistic inference rather than a demonstrated human gene–environment interaction. Avoiding excessive noise and unnecessary ototoxic drugs is prudent general hearing conservation, not proven DFNA72-specific prevention. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 6-7)

## 3. Phenotypes

| Phenotype | Characteristics in the reported family | Suggested HPO term |
|---|---|---|
| Sensorineural hearing impairment | Postlingual; initially approximately 40–50 dB HL in the described early phenotype; progressive | Sensorineural hearing impairment, HP:0000407 |
| Mid-frequency hearing loss | Approximately 0.5–4 kHz, most prominent at 1–2 kHz; U-shaped/bowl-shaped audiogram | Mid-frequency hearing loss, HP:0008315 |
| Progressive hearing impairment | Gradually extends to all frequencies; some advanced measurements showed absent responses | Progressive hearing impairment, HP:0001730 |
| Bilateral hearing impairment | Family phenotype was consistent with bilateral nonsyndromic loss | Bilateral sensorineural hearing impairment, HP:0008619 |
| Adult/young-adult onset | Approximately 26–30 years, after speech acquisition | Adult onset, HP:0003581; Postlingual sensorineural hearing impairment, HP:0004076 |
| Tinnitus | Reported near the beginning of the clinical course | Tinnitus, HP:0000360 |

The frequency of each feature cannot be converted into robust population percentages because only one family was described. Hearing loss was reported by nine of 37 pedigree members; eight affected relatives underwent segregation testing. The published clinical evaluations found normal tympanograms and no retrocochlear abnormality on auditory brainstem response. CT/MRI showed normal cochleae, mastoids, ossicles, internal auditory meatuses, and membranous labyrinth. Vertigo and cardiovascular, diabetic, visual, neurologic, or other syndromic manifestations were not reported. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4, ma2017slc44a4mutationcauses pages 1-2)

**Quality of life.** No DFNA72-specific EQ-5D, SF-36, PROMIS, speech-recognition, employment, educational, or psychosocial data exist. Progressive mid-frequency loss would be expected to impair speech audibility and communication, but quantitative impact should not be assigned from this pedigree alone.

## 4. Genetic and molecular information

- **Gene:** **SLC44A4**, also called CTL4; protein class: membrane solute carrier/choline transporter-like protein.
- **Reported disease allele:** c.466A>G, p.Met156Val; heterozygous germline missense variant.
- **Segregation:** eight of eight tested affected relatives carried it; zero of 13 tested unaffected relatives carried it. (ma2017slc44a4mutationcauses pages 2-3)
- **Control observations:** absent from 1,000 ethnically matched controls and 500 sporadic-hearing-loss cases. An exact contemporary gnomAD/TOPMed allele frequency was not established in the retrieved evidence. (ma2017slc44a4mutationcauses pages 3-4)
- **Classification:** the original evidence supports a pathogenic/likely-pathogenic interpretation within that family, but a current ClinVar aggregate classification and ACMG evidence-code assignment were not verified here. Given the lack of independent families, laboratories should avoid treating every rare SLC44A4 variant as diagnostic.
- **Functional consequence:** p.Met156Val reduced radiolabeled choline uptake and acetylcholine synthesis relative to wild type in transfected SH-SY5Y cells. (ma2017slc44a4mutationcauses pages 5-6)
- **Modifier genes, epigenetics, structural abnormalities:** none reported. No causal copy-number variant, translocation, repeat expansion, mitochondrial lesion, methylation signature, or somatic event is known.

## 5. Environmental information

There is no evidence that toxins, radiation, air pollution, smoking, alcohol, diet, exercise, or an infectious agent causes DFNA72. The original family’s history did not identify chronic noise or ototoxic-drug exposure. Noise vulnerability is biologically plausible because medial olivocochlear signaling protects outer hair cells, but this has not been quantified in SLC44A4-variant carriers. DFNA72 is not infectious and has no zoonotic or person-to-person transmission. (ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 6-7)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. Heterozygous **SLC44A4 p.Met156Val** **leads to** reduced SLC44A4-mediated choline uptake, as demonstrated in transfected SH-SY5Y cells. (ma2017slc44a4mutationcauses pages 5-6)
2. Reduced intracellular choline availability **results in** diminished acetylcholine synthesis, demonstrated in the same cellular system. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 5-6)
3. Diminished acetylcholine synthesis is **inferred to lead to** reduced cholinergic output from medial olivocochlear efferent neurons; this step has not been measured directly in affected humans. (ma2017slc44a4mutationcauses pages 6-7)
4. Reduced medial olivocochlear signaling is **inferred to result in** impaired regulation of outer-hair-cell electromotility/cochlear amplification and reduced protection against acoustic injury. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 6-7)
5. Outer-hair-cell dysfunction or vulnerability **is inferred to lead to** mid-frequency cochlear threshold elevation and tinnitus.
6. Continuing cochlear dysfunction or injury **results clinically in** progressive, bilateral, postlingual sensorineural hearing loss that eventually involves broader frequencies. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4)

**Branch from gene dysfunction:** experimental reduction of zebrafish *slc44a4* **leads to** abnormal otoliths, reduced/malformed hair cells and neuromasts, abnormal stereocilia, and balance/startle deficits; rescue by human SLC44A4 RNA **supports** a conserved auditory role, although it does not reproduce the heterozygous human missense genotype. (ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 6-7)

### Molecular and cellular annotation

- **Primary process:** transmembrane choline transport and acetylcholine biosynthesis.
- **Proposed neural circuit:** medial olivocochlear efferent neuron → cholinergic synapse → cochlear outer hair cell.
- **Suggested GO biological processes:** transmembrane transport (GO:0055085), choline transport, acetylcholine biosynthetic process (GO:0008292), chemical synaptic transmission (GO:0007268), sensory perception of sound (GO:0007605), regulation of membrane potential (GO:0042391).
- **Suggested GO cellular components:** plasma membrane (GO:0005886), neuron projection, synapse (GO:0045202), cholinergic synapse, stereocilium bundle (GO:0032421).
- **Suggested Cell Ontology concepts:** cochlear outer hair cell; inner-ear hair cell; auditory neuron/spiral ganglion neuron; cholinergic neuron. Exact CL identifiers should be ontology-release validated before ingestion.

No disease-specific immune, inflammatory, apoptotic, autophagic, endocrine, metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, proteomic, or CRISPR-screen signature has been reported. The available biochemical phenotype is reduced choline uptake and acetylcholine production. No affected-human cochlear tissue has been profiled.

## 7. Anatomical structures affected

The primary organ is the **inner ear**, particularly the cochlear auditory apparatus. The proposed cellular targets are the medial olivocochlear efferent pathway and cochlear outer hair cells; zebrafish experiments additionally implicate sensory hair cells, stereocilia, otolith organs, and lateral-line neuromasts. Human temporal-bone imaging was structurally normal, indicating functional/microscopic rather than gross malformative disease. (ma2017slc44a4mutationcauses pages 3-4, ma2017slc44a4mutationcauses pages 6-7)

Suggested ontology annotations include:

- Inner ear — UBERON:0001846
- Cochlea — UBERON:0001844
- Organ of Corti — UBERON:0002227
- Hair cell stereocilium — GO:0032420/related release-validated term
- Plasma membrane — GO:0005886
- Synapse — GO:0045202

The loss appears bilateral. No secondary-organ disease has been established.

## 8. Temporal development

Onset was insidious and postlingual, consistently around 26–30 years in the reported family. Early disease involved tinnitus and mild-to-moderate mid-frequency threshold elevation, especially at 1–2 kHz. It then progressed chronically to involve the full tested frequency range while retaining a bowl-shaped configuration. Advanced disease could include absent responses at selected frequencies. There is no evidence of episodic fluctuation, spontaneous remission, relapse, or recovery of unaided thresholds. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4)

No validated stage system or annual dB progression rate exists. The likely intervention window is early after measurable threshold decline, when amplification and communication support can be introduced, but this has not been tested specifically in DFNA72.

## 9. Inheritance and population

Inheritance in HN-01 was autosomal dominant across four generations. The segregation pattern was fully concordant among tested relatives, but formal age-adjusted penetrance cannot be inferred because young noncarriers/carriers, ascertainment, and longitudinal follow-up were not fully characterized. Expressivity included progression and variable severity by age. Anticipation, germline mosaicism, consanguinity effects, parent-of-origin effects, and modifier loci have not been reported. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 9-9)

No prevalence, incidence, carrier frequency, sex ratio, founder frequency, or population-attributable fraction is available. The only reported family was Chinese; absence of p.Met156Val in 1,000 ethnically matched controls supports rarity but does not establish a geographically restricted founder effect. (ma2017slc44a4mutationcauses pages 3-4)

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with history, three-generation pedigree, otoscopy, pure-tone audiometry, speech audiometry, tympanometry, and serial comparison of thresholds. The characteristic clue is bilateral postlingual progressive mid-frequency SNHL with a U-shaped audiogram. Auditory brainstem response or otoacoustic-emission testing may help localize dysfunction; CT/MRI is reserved for atypical, asymmetric, conductive, vestibular, or retrocochlear presentations rather than confirming DFNA72. The original study tested 250–8,000 Hz and used tympanometry, ABR, otoacoustic emissions, CT, and MRI. (ma2017slc44a4mutationcauses pages 9-9)

### Genetic testing

1. Use a comprehensive hereditary-hearing-loss multigene panel that includes well-validated dominant genes and **SLC44A4**, with copy-number analysis where available.
2. If nondiagnostic, use exome or genome sequencing with phenotype-driven analysis; WES identified the familial candidate in HN-01. (ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 9-9)
3. Confirm candidate variants by Sanger sequencing and perform segregation in affected and sufficiently old unaffected relatives.
4. Interpret non-p.Met156Val SLC44A4 variants cautiously because disease evidence is not broadly replicated.

Single-gene SLC44A4 testing is most defensible when the familial variant is already known. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line tests for this phenotype unless other clinical findings indicate them. RNA-seq, proteomics, metabolomics, methylation testing, and liquid biopsy have no established diagnostic role.

**Differential diagnosis:** other causes of U-shaped/mid-frequency dominant hearing loss, including **TECTA**, **COL11A2**, **EYA4**, and **POU4F3**, as well as broader dominant deafness genes; acquired noise/ototoxic injury; autoimmune inner-ear disease; otosclerosis; and retrocochlear pathology. Normal tympanometry and imaging support a sensorineural rather than conductive or structural cause.

**Screening:** cascade genetic testing and baseline audiometry are appropriate for relatives after identification of a familial variant. Newborn physiologic screening may be normal because DFNA72 is postlingual.

## 11. Outcome and prognosis

No mortality attributable to DFNA72 has been reported, and there is no evidence of reduced life expectancy. Prognosis concerns chronic auditory morbidity rather than survival. The natural history in the single pedigree indicates progressive threshold deterioration without spontaneous remission. Severity at older ages and baseline progression are plausible prognostic factors, but no validated biomarker or prediction model exists. (ma2017slc44a4mutationcauses pages 2-3, ma2017slc44a4mutationcauses pages 3-4)

Potential long-term consequences include communication disability, reduced speech understanding—especially in noise—tinnitus burden, social isolation, and occupational impairment. DFNA72-specific disability-adjusted life years, quality-of-life scores, cochlear-implant outcomes, and treatment-response statistics are unavailable.

## 12. Treatment

There is no approved SLC44A4-targeted pharmacotherapy, choline-based treatment, RNA therapy, gene therapy, or genome-editing intervention. Reduced cellular choline uptake does **not** establish that oral choline will restore cochlear neurotransmission, and supplementation should not be presented as disease-modifying treatment.

Current management is extrapolated from standard sensorineural-hearing-loss care:

- Serial audiometry and speech testing
- Appropriately fitted hearing aids when thresholds impair communication
- Assistive listening technology, auditory rehabilitation, and communication accommodations
- Tinnitus counseling or sound-based management when required
- Cochlear-implant evaluation for severe/profound loss with inadequate aided speech recognition
- Hearing conservation and avoidance of unnecessary ototoxic exposure

Suggested NCIt intervention concepts include *Hearing Aid*, *Cochlear Implantation*, *Audiologic Rehabilitation*, *Genetic Counseling*, and *Supportive Care*; release-specific NCIt codes should be validated before database loading.

No DFNA72/SLC44A4-specific interventional trial or NCT identifier was found. Thus, there are no disease-specific response rates, comparative-effectiveness data, pharmacogenomic recommendations, or adverse-event estimates.

## 13. Prevention

**Primary prevention:** a germline pathogenic allele cannot be prevented by lifestyle modification. Reproductive options after counseling may include prenatal diagnosis or preimplantation genetic testing for a confirmed familial variant, subject to local law, ethics, and patient preferences.

**Secondary prevention:** cascade testing, baseline audiometry in at-risk relatives, and periodic surveillance can detect presymptomatic or early loss. Because onset is usually postlingual, a normal newborn screen does not exclude later DFNA72.

**Tertiary prevention:** timely amplification, hearing rehabilitation, communication support, and hearing conservation may reduce disability and avoidable superimposed cochlear injury. No vaccine, prophylactic drug, dietary regimen, or preventive procedure is disease specific.

## 14. Other species and natural disease

No naturally occurring SLC44A4-associated veterinary disease, breed predisposition, or zoonotic phenomenon was identified. Zebrafish (*Danio rerio*; NCBI Taxonomy 7955) possess a conserved *slc44a4* ortholog; reported human–zebrafish protein similarity was approximately 75.7%. Knockdown affected otic and lateral-line sensory structures, supporting evolutionary conservation of auditory function. (ma2017slc44a4mutationcauses pages 6-7)

This is an experimental induced phenotype, not evidence of naturally occurring DFNA72 in fish. Cross-species transmission is not applicable.

## 15. Model organisms

### Zebrafish model

Morpholino-mediated *slc44a4* knockdown produced smaller or abnormal inner-ear structures/otoliths, fewer neuromasts and sensory hair cells, malformed stereocilia, and abnormal balance or sound-startle behavior. Co-injection/restoration with human SLC44A4 RNA rescued otolith, hair-cell, stereocilia, and hearing phenotypes, supporting gene-level functional conservation. (ma2017slc44a4mutationcauses pages 3-4, ma2017slc44a4mutationcauses pages 1-2, ma2017slc44a4mutationcauses pages 6-7)

**Applications:** auditory-development studies, hair-cell biology, choline-transport investigation, and preliminary functional assessment of SLC44A4.

**Limitations:** the model used transient knockdown rather than a stable heterozygous p.Met156Val knock-in. It therefore resembles reduced gene function and cannot establish the exact dominant mechanism, adult-onset progression, human cochlear frequency pattern, or allele-specific therapeutic response.

### Cellular model

Transfected SH-SY5Y neuroblastoma cells demonstrated lower choline uptake and acetylcholine synthesis with mutant than wild-type SLC44A4. This is useful for transporter-function assays but does not reproduce mature human cochlear hair cells or olivocochlear circuitry. (ma2017slc44a4mutationcauses pages 8-9, ma2017slc44a4mutationcauses pages 5-6)

No mouse knock-in, conditional mammalian model, patient-derived iPSC hair-cell model, cochlear organoid, or CRISPR-engineered p.Met156Val model was identified.

## Recent developments, expert interpretation, and critical evidence gaps

No disease-specific 2023–2024 primary study or independent family was identified. Consequently, the 2017 pedigree remains the central evidence. The most important research priorities are: independent case ascertainment; contemporary ClinGen/ClinVar reassessment; accurate population-frequency analysis; stable p.Met156Val knock-in models; direct study of olivocochlear neurons and outer hair cells; longitudinal audiometric modeling; and allele-specific rescue studies.

The original publication’s metadata are inconsistent in the retrieved records: the article text identifies *Human Molecular Genetics* volume 26, pages 383–394, advance publication 23 December 2016, and DOI **10.1093/hmg/ddw394**, whereas the search record labels July 2017 and DOI **10.1093/hmg/ddx232**. Database ingestion should verify the publisher/PubMed record before assigning DOI or PMID. (ma2017slc44a4mutationcauses pages 1-2)

An exact abstract quotation could not be supplied reliably because the retrieved full-text evidence did not expose a stable verbatim abstract. The article title itself—“SLC44A4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss”—accurately states the authors’ principal conclusion, but should not be represented as an abstract quote. Overall, DFNA72 is a biologically plausible and clinically coherent candidate Mendelian disorder with strong segregation in one pedigree, but limited replication and insufficient evidence for disease-specific epidemiology, prognosis statistics, or precision treatment.

References

1. (ma2017slc44a4mutationcauses pages 2-3): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

2. (ma2017slc44a4mutationcauses pages 1-2): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

3. (ma2017slc44a4mutationcauses pages 6-7): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

4. (ma2017slc44a4mutationcauses pages 3-4): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

5. (ma2017slc44a4mutationcauses pages 9-9): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

6. (ma2017slc44a4mutationcauses pages 8-9): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

7. (ma2017slc44a4mutationcauses pages 5-6): Zhaoxin Ma, Wenjun Xia, Fei Liu, Jing Ma, Shaoyang Sun, Jin Zhang, Nan Jiang, Xu Wang, Jiongjiong Hu, and Duan Ma. Slc44a4 mutation causes autosomal dominant hereditary postlingual non-syndromic mid-frequency hearing loss. Jul 2017. URL: https://doi.org/10.1093/hmg/ddx232, doi:10.1093/hmg/ddx232. This article has 21 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hearing_Loss_Autosomal_Dominant_72-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 1 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004076` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0055085` (1 mention) - the report calls it "Suggested GO biological processes:** transmembrane transport"; GO calls it **transmembrane transport**
- `GO:0005886` (2 mentions) - the report calls it "Suggested GO cellular components:** plasma membrane"; GO calls it **plasma membrane**, and lists "integral component of plasma membrane" among its other names
