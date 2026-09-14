---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T19:52:25.244852'
end_time: '2026-09-05T20:05:59.197336'
duration_seconds: 813.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sheehan Syndrome
  mondo_id: MONDO:0019618
  category: Acquired
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0019618
    reported_labels:
    - if available
    ontology_label: Sheehan syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sheehan_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sheehan Syndrome
- **MONDO ID:** MONDO:0019618 (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Sheehan Syndrome** covering all of the
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
- **Disease Name:** Sheehan Syndrome
- **MONDO ID:** MONDO:0019618 (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Sheehan Syndrome** covering all of the
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


# Sheehan Syndrome (MONDO:0019618): comprehensive disease-characteristics report

## Scope and evidence note

Sheehan syndrome (SS) is uncommon, geographically heterogeneous, and frequently diagnosed years after the causal obstetric event. Consequently, most evidence consists of retrospective cohorts, small prospective studies, reviews, and case reports rather than randomized trials. Figures below should therefore be encoded with their source population and ascertainment method. Database identifiers and ontology IDs not independently verified in the retrieved primary literature are marked for curator confirmation.

The following table provides a compact ontology-ready summary; the narrative that follows adds clinical and mechanistic detail.

| Domain | Key knowledge-base assertion | Suggested ontology terms/IDs | Evidence strength / limitations |
|---|---|---|---|
| Definition | Acquired postpartum hypopituitarism caused by ischemic necrosis or infarction of the pituitary, usually after severe postpartum hemorrhage with hypotension or shock. (karaca2025sheehansyndromea pages 1-2, powers2023adrenalcrisisin pages 1-2) | MONDO:0019618; Sheehan syndrome; acquired hypopituitarism; postpartum pituitary necrosis | Strong clinical and pathological consensus; predominantly observational evidence because the disease is rare. |
| Causal trigger | Severe obstetric blood loss and systemic hypoperfusion compromise perfusion of the pregnancy-enlarged pituitary. Possible modifiers include small sella, vasospasm, thrombosis, disseminated intravascular coagulation, and coagulation abnormalities; rare cases occur without recognized hemorrhage. (karaca2025sheehansyndromea pages 1-2, powers2023adrenalcrisisin pages 1-2) | Postpartum hemorrhage; hypovolemic shock; pituitary infarction; ischemic necrosis; term-name-only suggestions | Strong evidence for hemorrhage/hypoperfusion; modifier relationships are incompletely demonstrated and should not be encoded as independently sufficient causes. |
| Primary anatomy and cells | The anterior pituitary within the sella turcica is primarily injured; somatotroph, lactotroph, corticotroph, thyrotroph, and gonadotroph populations may be lost. Posterior-pituitary or stalk involvement is uncommon but can cause arginine-vasopressin deficiency. (d.2025adecadewith pages 1-2, matsuzaki2017acaseof pages 8-9) | UBERON: pituitary gland, anterior lobe of pituitary gland, sella turcica; CL term-name-only: somatotroph, lactotroph, corticotroph, thyrotroph, gonadotroph | Cell types are inferred from axis-specific hormone loss and pathology; Sheehan-specific single-cell validation is unavailable. Exact UBERON/CL identifiers should be database-verified before ingestion. |
| Lactation phenotype | Failure to lactate or agalactia is a classic early clue reflecting prolactin deficiency; one cited clinical series reported absent postpartum milk production in about 70%. (zain2022ararecase pages 4-5) | HP: Agalactia; HP: Hypoprolactinemia; exact IDs require verification | Common but not universal; frequency derives from older, referral-based cohorts and may not generalize. |
| Reproductive phenotype | Failure of menses to resume, secondary amenorrhea, infertility, loss of libido, and reduced axillary or pubic hair result from hypogonadotropic hypogonadism. Fertility can sometimes be restored with gonadotropin induction. (d.2025adecadewith pages 1-2, matsuzaki2017acaseof pages 8-9) | HP: Secondary amenorrhea; HP: Female infertility; HP: Hypogonadotropic hypogonadism; HP: Decreased libido; term-name-only suggestions | Strong clinical association; reported frequencies vary with residual pituitary function and age at diagnosis. |
| Adrenal phenotype | ACTH deficiency causes fatigue, nausea, hypoglycemia, hypotension, hyponatremia, and vulnerability to life-threatening adrenal crisis during illness, procedures, or interruption of glucocorticoids. (powers2023adrenalcrisisin pages 1-2, samman2025delayeddiagnosisof pages 3-4) | HP: Secondary adrenal insufficiency; HP: Hypotension; HP: Hypoglycemia; HP: Hyponatremia; HP: Adrenal crisis; exact IDs require verification | Strong clinical evidence; hyponatremia has been reported in approximately 33–69%, but estimates are heterogeneous. |
| Thyroid phenotype | Central hypothyroidism causes cold intolerance, dry skin, fatigue, bradycardia, weight change, and occasionally pericardial effusion or severe neuropsychiatric manifestations. One older series reported secondary hypothyroidism in 90%. (zain2022ararecase pages 4-5) | HP: Central hypothyroidism; HP: Cold intolerance; HP: Dry skin; HP: Bradycardia; HP: Pericardial effusion; term-name-only suggestions | Strong axis-level evidence; individual manifestation frequencies are uncertain and severe cardiac presentations are mainly case-based. |
| Growth-hormone and metabolic phenotype | GH deficiency is frequent and contributes, with hypogonadism and glucocorticoid overtreatment, to reduced lean mass, increased adiposity, insulin resistance, dyslipidemia, low-grade inflammation, endothelial dysfunction, impaired bone health, and reduced quality of life. (karaca2025sheehansyndromea pages 1-2, vasconcelos2024acasereport pages 7-8) | HP: Growth hormone deficiency; HP: Abnormal body composition; HP: Insulin resistance; HP: Hyperlipidemia; HP: Osteoporosis; term-name-only suggestions | Moderate evidence from small cohorts and extrapolation from hypopituitarism; causal contributions of individual hormone deficits are difficult to separate. |
| Posterior-pituitary phenotype | Central diabetes insipidus is rare but may present acutely with polyuria, hypernatremia, high serum osmolality, and dilute urine; it generally indicates extensive injury. (matsuzaki2017acaseof pages 8-9) | HP: Central diabetes insipidus; HP: Polyuria; HP: Hypernatremia; HP: Decreased urine osmolality; term-name-only suggestions | Supported chiefly by case reports and a systematic review of rare cases; population frequency is not established. |
| Diagnostic laboratory evidence | Diagnosis requires compatible obstetric history plus biochemical evidence of one or more pituitary-axis deficiencies: low target-gland hormones with low or inappropriately normal pituitary hormones. Cortisol/ACTH, free T4/TSH, prolactin, IGF-1, LH/FSH with estradiol, serum sodium, and osmolality are core assessments. (vasconcelos2024acasereport pages 7-8, d.2025adecadewith pages 1-2) | LOINC mappings should be assigned for each measured hormone after assay-specific review; SNOMED CT: hypopituitarism, central adrenal insufficiency, central hypothyroidism | Strong clinical practice basis, but no universally validated Sheehan-specific diagnostic criteria or single biomarker exists. Dynamic testing may be required for equivocal adrenal or GH function. |
| Imaging evidence | Acute MRI may show pituitary enlargement, abnormal signal, infarction, or absent enhancement; later evolution commonly produces pituitary atrophy and partial or complete empty sella. Normal early imaging does not exclude disease. (matsuzaki2017acaseof pages 8-9, samman2025delayeddiagnosisof pages 3-4) | UBERON: sella turcica, pituitary gland; RadLex/SNOMED CT: empty sella, pituitary infarction, pituitary atrophy; exact IDs require verification | Moderate evidence from serial case reports and cohorts; empty sella is supportive but neither necessary nor specific. |
| Treatment interventions | Replace glucocorticoids before levothyroxine when ACTH deficiency is possible; provide stress dosing and emergency education. Then individualize levothyroxine, estrogen–progestogen when appropriate, desmopressin for AVP deficiency, GH in selected adults, and gonadotropins for fertility. (vasconcelos2024acasereport pages 7-8, d.2025adecadewith pages 1-2) | NCIT term-name-only: Glucocorticoid Replacement Therapy, Thyroid Hormone Replacement Therapy, Estrogen Replacement Therapy, Growth Hormone Replacement Therapy, Desmopressin Therapy, Ovulation Induction; CHEBI term-name-only: hydrocortisone, levothyroxine, estradiol, progesterone, somatropin, desmopressin | Standard-of-care principles are strong and largely extrapolated from hypopituitarism guidelines; Sheehan-specific randomized trials and response-rate estimates are lacking. Exact NCIT/CHEBI identifiers require verification. |
| Epidemiology | Incidence has fallen markedly where emergency obstetric care is accessible but remains under-recognized in lower-resource settings and migrant populations. Reported estimates include 5.1 per 100,000 population in Iceland and up to 3.1% among parous women in selected populations; estimates are not directly comparable. (karaca2025sheehansyndromea pages 1-2) | Epidemiological annotation: acquired rare disease; female reproductive/postpartum population | Low-to-moderate certainty because methods, denominators, eras, and ascertainment differ; global incidence and prevalence remain unknown. |
| Genetics and molecular profiling | Sheehan syndrome is acquired and has no established causal gene, Mendelian inheritance pattern, pathogenic variant, penetrance, carrier frequency, or validated protective allele. Coagulation or inflammatory polymorphisms have been explored only as susceptibility modifiers. No disease-defining epigenomic, transcriptomic, proteomic, metabolomic, single-cell, spatial, or integrated multi-omic signature is validated. (karaca2025sheehansyndromea pages 1-2) | MONDO:0019618; inheritance: not applicable; causal-gene field: none established; omics-biomarker field: unsupported | Strong evidence against treating it as a monogenic disorder; modifier studies are small and unreplicated, so variants should not be encoded as causal. |
| Immune mechanism | Ischemic necrosis may expose pituitary antigens and theoretically perpetuate damage through anti-pituitary or anti-hypothalamic immunity, but prospective postpartum-hemorrhage data found antibodies absent despite hypopituitarism. | GO term-name-only: immune response, inflammatory response, response to ischemia | Conflicting, low-certainty evidence; autoimmunity is a hypothesis or secondary modifier, not an established initiating cause or diagnostic biomarker. |
| Animal and experimental models | No well-established naturally occurring veterinary equivalent, breed association, zoonotic transmission, or validated genetic model was identified. General hemorrhagic-shock, pituitary-ischemia, hypophysectomy, and hormone-deficiency models can investigate downstream biology but do not fully recapitulate pregnancy-associated human disease. | NCBI Taxonomy/VBO/OMIA fields: no supported disease-specific entry identified; model type: induced physiological model, term-name-only | Major evidence gap. Model claims require species- and protocol-specific primary validation before knowledge-base inclusion. |


*Table: Compact ontology-ready assertions spanning causation, anatomy, phenotypes, diagnosis, treatment, epidemiology, molecular evidence, and models. Unverified ontology identifiers and unsupported knowledge fields are explicitly distinguished from established evidence.*

## 1. Disease information

**Definition.** SS is acquired postpartum hypopituitarism caused by ischemic infarction/necrosis of the pregnancy-enlarged pituitary, usually after severe postpartum hemorrhage (PPH), hypotension, or hypovolemic shock. Injury predominantly affects the adenohypophysis and may produce partial or complete anterior-pituitary failure. A 2025 expert review succinctly defines it as “postpartum pituitary necrosis leading to severe hypopituitarism.” Although incidence has fallen with modern obstetric care, experts stress that SS remains an important, under-recognized cause of hypopituitarism, especially in lower-resource settings and migrant populations (published online 25 January 2025; DOI/URL: https://doi.org/10.1007/s11102-024-01481-1). (karaca2025sheehansyndromea pages 1-2)

**Synonyms:** Sheehan’s syndrome; postpartum hypopituitarism; postpartum pituitary necrosis; postpartum pituitary infarction; postpartum panhypopituitarism when all axes are affected; Simmonds–Sheehan syndrome is an older term. “Pituitary apoplexy” overlaps mechanistically but is not synonymous: apoplexy commonly denotes acute hemorrhage/infarction, often in a tumor, whereas SS is the obstetric ischemic syndrome.

**Identifiers—curator verification advised:**

- MONDO: **MONDO:0019618** (provided target identifier).
- ICD-10-CM commonly indexes SS under **E23.0, hypopituitarism**; some national modifications explicitly include Sheehan syndrome. ICD-11 mapping should be checked against the current release rather than inferred.
- MeSH: generally indexed through **Hypopituitarism** and postpartum/obstetric concepts; verify whether the current MeSH release exposes a dedicated supplementary concept.
- Orphanet and OMIM: SS is acquired, not a Mendelian phenotype. A dedicated OMIM disease entry is therefore not expected; verify the current Orphanet record before ingestion.

The report represents **aggregated disease-level literature**, not individual EHR data. Case reports are identified as such and should not be interpreted as prevalence estimates.

## 2. Etiology, risk and protective factors

### Causal factors

The principal cause is acute reduction of pituitary perfusion during or shortly after delivery. Pregnancy increases pituitary volume—principally through lactotroph hyperplasia—without a commensurate increase in portal blood supply, increasing susceptibility to systemic hypoperfusion. PPH, hypovolemia, hypotension, and shock then lead to ischemia and irreversible tissue loss. Proposed amplifiers include small sellar volume, arterial vasospasm, thrombosis, disseminated intravascular coagulation, and other coagulation abnormalities. Severe visible bleeding is highly characteristic but not obligatory; rare clinically compatible cases occur without recognized PPH (karaca2025sheehansyndromea pages 1-2, powers2023adrenalcrisisin pages 1-2).

**Obstetric risk factors** are therefore conditions that cause major hemorrhage or shock: uterine atony, retained placenta, placenta accreta spectrum or previa, uterine rupture, operative trauma, coagulopathy, and delayed access to transfusion or hemorrhage control. Inherited bleeding disorders may increase PPH risk, but they are not established direct causes of pituitary necrosis. A 2024 report of SS in factor XI deficiency is hypothesis-generating rather than proof of a disease-specific genetic association.

### Genetic and immune susceptibility

No causal gene or reproducible high-penetrance susceptibility locus is established. Small studies have explored thrombophilia/coagulation genes and inflammatory variants, but these should not be encoded as pathogenic SS variants. Likewise, anti-pituitary or anti-hypothalamic antibodies have been reported years after SS, leading to the hypothesis that necrosis exposes sequestered antigens and perpetuates loss. Evidence is inconsistent: in one prospective study of 20 women after moderate-to-severe PPH, 95% had at least one affected axis at four weeks, 60% initially met the study’s hypopituitarism criterion, and 25% still had hypopituitarism at six months, yet anti-pituitary antibodies were negative in all participants. Thus autoimmunity remains an unproven secondary modifier, not the initiating lesion or a validated biomarker.

### Environmental, lifestyle and infectious factors

The relevant “environment” is the obstetric-care environment: access to skilled delivery, blood products, rapid PPH control, anesthesia, intensive care, and postpartum follow-up. No toxin, pollutant, diet, smoking pattern, occupation, radiation exposure, or chronic infection is established as a disease-specific cause. Infection can **unmask** latent ACTH deficiency: a 2024 dengue case developed hypotension, hypoglycemia, and adrenal crisis, illustrating physiologic stress rather than infectious causation (July 2024; DOI: https://doi.org/10.31486/toj.24.0019).

### Protective factors

The strongest protective factors are prevention and immediate treatment of PPH: active third-stage labor management, rapid uterotonic therapy, tranexamic acid where indicated, surgical/interventional hemorrhage control, transfusion and correction of coagulopathy, maintenance of perfusion, and postpartum endocrine surveillance after severe hemorrhage. No validated protective allele, diet, drug prophylaxis directed specifically at SS, or vaccine exists.

## 3. Phenotypes

SS begins in reproductive-age adulthood after childbirth, but recognition may occur decades later. Severity ranges from one-axis deficiency to panhypopituitarism; progression may be insidious, with crises precipitated by infection, surgery, fasting, or medication interruption.

- **Prolactin/lactation:** agalactia or failure to establish lactation is often the earliest clue. Suggested HPO: *Agalactia*, *Hypoprolactinemia*. An older clinical series cited in recent literature reported absent milk production in approximately 70%; referral bias is likely (zain2022ararecase pages 4-5).
- **Gonadal axis:** failure of menses to resume, secondary amenorrhea, oligomenorrhea, infertility, low libido, vaginal dryness, and loss of axillary/pubic hair. Suggested HPO: *Secondary amenorrhea*, *Female infertility*, *Hypogonadotropic hypogonadism*, *Decreased libido*. Nearly universal hypogonadism has been reported in selected complete-SS cohorts (zain2022ararecase pages 4-5).
- **ACTH–cortisol axis:** fatigue, weakness, anorexia, nausea/vomiting, abdominal pain, weight loss, hypotension, hypoglycemia, hyponatremia, altered consciousness, and adrenal crisis. Suggested HPO: *Secondary adrenal insufficiency*, *Hypotension*, *Hypoglycemia*, *Hyponatremia*. One cited cohort reported adrenal failure in 55%; across heterogeneous reports, hyponatremia is approximately 33–69% (zain2022ararecase pages 4-5, samman2025delayeddiagnosisof pages 3-4).
- **TSH–thyroid axis:** central hypothyroidism causes cold intolerance, constipation, dry/coarse skin, bradycardia, fatigue, weight change, edema, anemia, cognitive slowing, depression, and occasionally pericardial effusion. Suggested HPO: *Central hypothyroidism*, *Cold intolerance*, *Dry skin*, *Bradycardia*, *Pericardial effusion*. Secondary hypothyroidism reached 90% in one older referral cohort (zain2022ararecase pages 4-5).
- **GH axis:** low IGF-1, reduced lean mass and exercise capacity, increased visceral fat, dyslipidemia, insulin resistance, impaired well-being, and adverse bone/cardiovascular phenotype. Suggested HPO: *Growth hormone deficiency*, *Decreased serum IGF-1*, *Abnormal body composition*, *Hyperlipidemia*. GH and prolactin deficiencies have been reported in 90–100% of selected series, but estimates vary with testing and case severity (vasconcelos2024acasereport pages 7-8, samman2025delayeddiagnosisof pages 3-4).
- **Posterior pituitary:** arginine-vasopressin deficiency/central diabetes insipidus is rare; features are polyuria, polydipsia, hypernatremia, high plasma osmolality, and dilute urine. Suggested HPO: *Central diabetes insipidus*, *Polyuria*, *Polydipsia*, *Hypernatremia*. Its occurrence generally implies extensive stalk/posterior injury (matsuzaki2017acaseof pages 8-9).
- **Acute neurological/cardiovascular manifestations:** severe headache, visual symptoms, seizures, coma, electrolyte disturbance, shock, respiratory failure, cardiomyopathy, pericardial effusion, or tamponade. These are uncommon and primarily case-supported. Acute presentations can mimic eclampsia, encephalitis, stroke, or cerebral venous thrombosis (matsuzaki2017acaseof pages 8-9, singh2023postpartumpituitaryapoplexy pages 4-4).
- **Bone and blood:** osteopenia/osteoporosis and fracture susceptibility reflect estrogen and GH deficiency, undertreatment, aging, and sometimes glucocorticoid excess. Normocytic anemia or pancytopenia can occur; one cited cohort found anemia in 80% of 65 patients versus 25% of controls (samman2025delayeddiagnosisof pages 3-4).
- **Behavioral/QOL:** depression, anxiety, cognitive slowing, low energy, sexual dysfunction, impaired work and physical capacity, and fertility loss are reported. A 2024 case found that replacement improved energy, physical capacity, temperature regulation, skin features, and sexual function, but validated SS-specific EQ-5D/SF-36 population norms are unavailable (vasconcelos2024acasereport pages 7-8).

## 4. Genetic and molecular information

SS is **acquired and non-Mendelian**. There are no established causal genes, HGNC-defined disease genes, pathogenic/likely pathogenic germline or somatic variants, chromosomal abnormalities, penetrance estimates, carrier frequencies, founder variants, anticipation, or germline mosaicism. Therefore WGS/WES, panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not routine SS diagnostics.

Candidate coagulation or inflammatory polymorphisms are unreplicated susceptibility observations, not ACMG-classifiable SS causes. No validated modifier gene or protective variant exists. No disease-defining DNA-methylation, chromatin, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omic signature was identified. Routine endocrine biochemistry—not molecular profiling—is the clinically actionable molecular readout.

## 5. Environmental information

The key non-genetic exposure is severe peripartum blood loss with systemic hypotension. Poor access to emergency obstetric care, delayed referral/transfusion, home delivery without skilled support, and inability to control PPH increase risk. Lifestyle factors do not initiate SS, although smoking, poor diet, inactivity, and glucocorticoid overtreatment can compound downstream cardiometabolic and skeletal morbidity. No causative infectious agent or zoonotic pathway applies.

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Pregnancy-driven lactotroph hyperplasia leads to** enlargement and increased metabolic demand of the anterior pituitary without proportionate vascular reserve.
2. **Severe PPH, hypotension, hypovolemia, or shock leads to** critically reduced hypophyseal/portal perfusion; vasospasm, thrombosis, DIC, or a small sella may amplify this step, but their independent roles remain incompletely demonstrated (karaca2025sheehansyndromea pages 1-2, powers2023adrenalcrisisin pages 1-2).
3. **Perfusion failure leads to** adenohypophyseal ischemia, infarction, and necrosis; acute MRI may show enlargement, abnormal signal, infarction, or absent enhancement (matsuzaki2017acaseof pages 8-9).
4. **Necrosis leads to** permanent loss of somatotrophs, lactotrophs, corticotrophs, thyrotrophs, and gonadotrophs; extension to the stalk/neurohypophysis occasionally results in AVP deficiency.
5. **Endocrine-cell loss results in branching deficiencies:**
   - PRL loss **leads to** agalactia;
   - LH/FSH loss **leads to** amenorrhea, estrogen deficiency, infertility, sexual dysfunction, and bone loss;
   - ACTH loss **leads to** hypocortisolism, impaired vascular tone/free-water excretion, hypoglycemia, hyponatremia, and adrenal crisis;
   - TSH loss **leads to** central hypothyroidism, metabolic slowing, bradycardia, edema, dyslipidemia, and neurocognitive symptoms;
   - GH loss **leads to** reduced IGF-1, adverse body composition, dyslipidemia, insulin resistance, low bone turnover, and impaired QOL;
   - AVP loss **leads to** polyuria, dilute urine, and hypernatremia.
6. **Tissue resorption and involution lead to** pituitary atrophy and eventually partial or complete empty sella; this evolution is demonstrated by serial case imaging (matsuzaki2017acaseof pages 8-9).
7. **Chronic hormone deficiency, plus possible replacement imbalance, leads to** cardiovascular, metabolic, skeletal, reproductive, and psychological morbidity. A 2023 expert review reports increased body fat, insulin resistance, coagulation abnormalities, leptin, low-grade inflammation, and endothelial dysfunction; untreated GH deficiency, hypogonadism, and glucocorticoid excess are plausible contributors.
8. **Necrotic antigen release may lead to** secondary pituitary autoimmunity and progressive dysfunction, but this branch is **inferred and conflicting**, not established.

No disease-specific Wnt, MAPK, mTOR, or PI3K–AKT driver has been demonstrated. The core processes are ischemia, necrosis, endocrine-cell depletion, altered water/glucose/lipid metabolism, and secondary systemic effects. Suggested GO biological-process terms include *response to ischemia*, *necrotic cell death*, *regulation of hormone secretion*, *glucose homeostasis*, *water homeostasis*, and *inflammatory response*. Suggested CL terms are *lactotroph*, *somatotroph*, *corticotroph*, *thyrotroph*, and *gonadotroph*; exact identifiers should be ontology-verified.

## 7. Anatomical structures affected

The **primary organ** is the pituitary gland, especially the anterior lobe in the sella turcica. Relevant UBERON term names are *pituitary gland*, *anterior lobe of pituitary gland*, *posterior lobe of pituitary gland*, *infundibular stalk*, and *sella turcica*. Injury is central and has no meaningful right/left lateralization.

Secondary effects involve adrenal cortex, thyroid, ovaries/uterus, mammary gland, liver/adipose tissue, skeleton, cardiovascular system, kidney/water balance, and brain. At the subcellular level, no SS-specific organelle lesion is established; hypoxic ATP failure, membrane disruption, and necrosis are generic ischemic processes rather than a validated mitochondrial or ER disease. Suggested GO cellular-component annotations should therefore remain at *cell*, *plasma membrane*, and hormone-secretory compartments only when supported by a specific experiment.

## 8. Temporal development

**Onset:** the causal lesion occurs peripartum. Acute SS is generally recognized within six weeks, but most disease is chronic and insidious. In a review of 21 acute cases, median postpartum presentation was 7.9 days for adrenal insufficiency, 4 days for DI, 18 days for hypothyroidism, and 9 days for panhypopituitarism (DOI: https://doi.org/10.1186/s12884-017-1380-y) (matsuzaki2017acaseof pages 8-9).

**MRI evolution:** during the first 20 days MRI may be normal or show enlargement/non-enhancement; lesions become more conspicuous around days 26–32, followed by gland flattening and partial/complete empty sella over subsequent months (matsuzaki2017acaseof pages 8-9).

**Course:** residual function determines whether deficits remain partial or progress to panhypopituitarism. Diagnostic delays of 9 ± 9.7 years in a French cohort and 15.35 ± 6.74 years in an Indian study have been cited; individual cases have been diagnosed more than 30–46 years later (vasconcelos2024acasereport pages 7-8, samman2025delayeddiagnosisof pages 3-4, zain2022ararecase pages 4-5). Necrotic tissue does not regenerate predictably; treatment controls deficiencies but is usually lifelong. The critical opportunities are immediate PPH resuscitation, evaluation of postpartum agalactia/amenorrhea, and stress-dose glucocorticoids during illness or procedures.

## 9. Inheritance and population

There is no inheritance pattern, sex ratio in the conventional genetic sense, or carrier state. By definition, clinically affected individuals have undergone pregnancy/delivery, although modern gender-inclusive documentation should record reproductive anatomy and pregnancy history rather than assume identity.

Epidemiology is uncertain because mild disease is missed and historical obstetric risk varies sharply. Reported figures include **5.1 per 100,000 population in Iceland**, SS accounting for approximately **6–8% of hypopituitarism etiologies**, and up to **3.1% of parous women** in selected high-risk populations. These estimates are not directly comparable. A Spanish estimate for all hypopituitarism—not SS specifically—was 45.5 per million prevalent and 4.2 per million incident cases annually and should not be mislabeled as SS incidence (karaca2025sheehansyndromea pages 1-2).

Burden is highest where PPH is common and emergency obstetric/transfusion services are limited. Cases also persist in high-income countries because of rare obstetric catastrophes, immigration from higher-risk regions, and decades-long diagnostic latency.

## 10. Diagnostics

### Practical diagnostic approach

1. **Recognize the context:** prior PPH, shock, transfusion, hysterectomy/embolization, inability to lactate, or persistent postpartum amenorrhea.
2. **Assess urgent physiology:** blood pressure, glucose, sodium, potassium, serum/plasma osmolality, renal function, CBC, and ECG. Hyponatremia with normal potassium is compatible with secondary adrenal insufficiency because aldosterone is usually preserved.
3. **Measure pituitary axes:** paired morning cortisol/ACTH; free T4/TSH; prolactin; IGF-1; LH/FSH with estradiol; and serum/urine osmolality if polyuria. Central deficits show low target-gland hormone with low or inappropriately normal trophic hormone. Dynamic cortisol or GH testing may be needed when basal results are equivocal.
4. **Pituitary MRI with contrast:** supportive acute findings are infarction, edema/enlargement, abnormal signal, or non-enhancement; chronic findings are atrophy and partial/complete empty sella. A normal early MRI does not exclude SS (matsuzaki2017acaseof pages 8-9, samman2025delayeddiagnosisof pages 3-4).
5. **Treat suspected adrenal crisis immediately:** testing must not delay parenteral hydrocortisone and fluid/glucose resuscitation.

There is no universally validated SS-specific score or molecular biomarker. Histology/biopsy is neither required nor appropriate in routine care. Genetic and omics tests have no established role.

### Differential diagnosis

- **Lymphocytic/postpartum hypophysitis:** often pituitary enlargement/stalk thickening and autoimmune association; PPH is not required.
- **Pituitary apoplexy in adenoma:** abrupt headache, ophthalmoplegia/visual loss and sellar mass, often requiring neurosurgical assessment.
- **Primary empty-sella syndrome:** imaging finding without the defining obstetric history; endocrine function may be normal.
- **Primary adrenal insufficiency:** elevated ACTH, hyperkalemia, mineralocorticoid deficiency, and hyperpigmentation distinguish it from central disease.
- **Primary hypothyroidism:** high TSH, unlike central hypothyroidism.
- **Postpartum thyroiditis, postpartum depression/chronic fatigue, functional hypothalamic amenorrhea, medication effects, infiltrative/infectious pituitary disease, traumatic brain injury, and congenital/genetic hypopituitarism.**
- Acute neurological presentations also require exclusion of eclampsia/PRES, cerebral venous thrombosis, meningitis/encephalitis, stroke, and osmotic/electrolyte disorders (singh2023postpartumpituitaryapoplexy pages 4-4).

No general-population screening is justified. **Targeted endocrine screening after moderate-to-severe PPH**, especially with agalactia, amenorrhea, hypotension, hyponatremia, hypoglycemia, or persistent fatigue, is reasonable; the prospective 20-woman PPH study found persistent hypopituitarism in 25% at six months, although this small estimate needs replication.

## 11. Outcome and prognosis

No robust SS-specific 5- or 10-year survival estimate is available. Prognosis is generally good with accurate lifelong replacement and emergency education, but untreated ACTH deficiency can be fatal. Morbidity includes recurrent adrenal crisis, severe hyponatremia/hypoglycemia, infertility, sexual dysfunction, osteoporosis, anemia, dyslipidemia, insulin resistance, obesity, endothelial dysfunction, premature cardiovascular disease, depression, and impaired QOL (karaca2025sheehansyndromea pages 1-2, vasconcelos2024acasereport pages 7-8).

A 2024 PCI case illustrates procedural risk: severe symptomatic hyponatremia did not respond to sodium alone but improved rapidly after **50 mg hydrocortisone** plus hypertonic sodium, supporting stress-dose glucocorticoids before major procedures in cortisol-deficient patients (April 2024; DOI: https://doi.org/10.3389/fcvm.2024.1353392).

Recovery of destroyed pituitary tissue is uncommon, though some early postpartum abnormalities improve and partial axes may persist. Prognosis depends on extent of necrosis, diagnostic delay, ACTH deficiency, adherence and stress dosing, avoidance of glucocorticoid over-replacement, appropriate sex-steroid/GH management, and control of cardiovascular and bone risks. No validated SS-specific prognostic molecular biomarker exists.

## 12. Treatment and real-world implementation

### Treatment algorithm

1. **Adrenal crisis or suspected ACTH deficiency:** administer parenteral hydrocortisone immediately with isotonic saline and dextrose as needed. For maintenance, individualized hydrocortisone is preferred; a commonly cited range is **10–20 mg/day in divided doses**, with the largest dose in the morning. Provide sick-day rules, dose escalation during fever/surgery/trauma, injectable emergency hydrocortisone, and medical-alert identification (vasconcelos2024acasereport pages 7-8).
2. **Replace glucocorticoid before levothyroxine.** Starting thyroid hormone first may increase cortisol clearance/metabolic demand and precipitate crisis. Titrate levothyroxine to clinical status and free T4—often the middle-to-upper reference range—not TSH, which is unreliable in central hypothyroidism (vasconcelos2024acasereport pages 7-8, samman2025delayeddiagnosisof pages 3-4).
3. **Hypogonadism:** estrogen replacement, with progestogen if the uterus is present, is generally continued until the average age of natural menopause when not contraindicated. Benefits include vasomotor, sexual, bone, and cardiometabolic protection. Suggested NCIT: *Estrogen Replacement Therapy*, *Progesterone Therapy*.
4. **Fertility:** pulsatile GnRH where hypothalamic function permits or, more commonly, hMG/FSH plus hCG with reproductive-endocrinology supervision. Successful pregnancy has been reported, but adrenal and thyroid doses require close monitoring; one review of 31 pregnancies in 27 women with hypopituitarism reported PPH in 8.7% and small-for-gestational-age newborns in 42.4% (matsuzaki2017acaseof pages 8-9).
5. **Adult GH deficiency:** selected patients may receive recombinant GH/somatropin after other axes are stable. Potential benefits are improved body composition, lipids, exercise capacity, bone remodeling, and QOL; edema, arthralgia, myalgia, glucose intolerance, cost, and uncertain hard cardiovascular outcomes limit use (karaca2025sheehansyndromea pages 1-2, vasconcelos2024acasereport pages 7-8).
6. **AVP deficiency:** desmopressin with sodium/fluid monitoring. Suggested NCIT: *Desmopressin Therapy*.
7. **Supportive care:** nutrition and weight-bearing/resistance exercise; calcium/vitamin D adequacy; DXA and fracture-risk assessment; treatment of osteoporosis, anemia, dyslipidemia, diabetes and hypertension; psychological support; sexual and fertility counseling.

There is no role for pituitary surgery unless another sellar lesion is present. No approved gene, cell, RNA, targeted, or immune therapy restores the necrotic gland. A ClinicalTrials.gov search found no relevant disease-specific interventional trial/NCT identifier. Current implementation therefore consists of individualized replacement, emergency preparedness, obstetric prevention, and multidisciplinary endocrinology–obstetric–primary-care follow-up.

## 13. Prevention

- **Primary:** prevent PPH and shock through skilled birth attendance, antenatal identification of placenta/coagulation risks, active management of the third stage, uterotonics, rapid tranexamic acid where guideline-indicated, hemorrhage protocols, blood-bank access, embolization/surgery, and maintenance of tissue perfusion.
- **Secondary:** flag severe PPH survivors; ask about lactation and menstrual recovery; check morning cortisol, free T4/TSH, sodium and other axes when symptomatic; arrange endocrine follow-up. Agalactia plus amenorrhea should not be dismissed as normal postpartum variation.
- **Tertiary:** lifelong replacement adherence, glucocorticoid sick-day education and emergency injection, perioperative stress dosing, regular thyroid/sex-steroid/GH review, and cardiovascular/bone surveillance.

No vaccine, population newborn/carrier screening, prenatal genetic diagnosis, or family cascade screening applies. Genetic counseling is not required for recurrence through inheritance; counseling should instead address future pregnancy, PPH recurrence, fertility treatment, and endocrine dose adjustment.

## 14. Other species/natural disease

No well-established naturally occurring veterinary equivalent, OMIA breed disorder, cross-species transmission, or zoonotic potential was identified. Postpartum hypopituitarism may theoretically follow severe hemorrhage in mammals, but isolated veterinary reports should not be equated with validated natural SS without species-specific pathology and endocrine confirmation. NCBI Taxon and VBO fields should therefore remain unpopulated pending direct evidence.

## 15. Model organisms

No standardized mouse, rat, zebrafish, invertebrate, organoid, iPSC, knockout, knock-in, or humanized model reproducing the full sequence—pregnancy-associated pituitary enlargement, obstetric hemorrhagic shock, selective postpartum infarction, chronic empty sella, and multi-axis failure—was identified. Hemorrhagic-shock/pituitary-ischemia preparations can study upstream perfusion injury; hypophysectomy or cell-specific hormone-deficiency models can study downstream endocrine consequences, but neither has full construct or phenotypic validity for SS. This is a substantial research gap. No causal gene exists for a faithful genetic knockout model.

## Recent developments and expert interpretation

The 2023–2024 literature has mainly refined **comorbidity recognition and emergency management**, rather than identifying a new molecular driver. The 2023 cardiometabolic review emphasizes adiposity, insulin resistance, inflammation, endothelial dysfunction and replacement imbalance. Recent 2024 cases demonstrate that infection, invasive procedures, or missed glucocorticoids can unmask life-threatening adrenal insufficiency; contemporary bone and cardiovascular studies reinforce proactive DXA and risk-factor surveillance, although Sheehan-specific hard-outcome data remain sparse (karaca2025sheehansyndromea pages 1-2, vasconcelos2024acasereport pages 7-8, powers2023adrenalcrisisin pages 1-2).

The most authoritative current interpretation is that SS is simultaneously **preventable obstetric ischemic injury** and **lifelong multisystem endocrine disease**. The highest-yield advances are not genomic: they are rapid PPH control, systematic postpartum recognition, correct hormone-replacement sequence, stress-dose education, and long-term cardiometabolic and skeletal care.

## Selected source links and brief abstract quotations

- Karaca Z, Keleştimur F. *Sheehan syndrome: a current approach to a dormant disease.* **Pituitary**, online 25 January 2025. https://doi.org/10.1007/s11102-024-01481-1. Abstract: “The nonspecific signs and symptoms of hypopituitarism result in significant delay in diagnosis and treatment.” (karaca2025sheehansyndromea pages 1-2)
- Vasconcelos AL et al. *A Case Report of Sheehan Syndrome: A Rare Cause of Hypopituitarism.* **Cureus**, February 2024. https://doi.org/10.7759/cureus.53544. Abstract: “Hormonal replacement therapy resolved several impairments in terms of general energy, physical capacity, temperature regulation, skin characteristics, and sexual function.” (vasconcelos2024acasereport pages 7-8)
- Gao J et al. *Old woman with Sheehan's syndrome suffered severe hyponatremia following percutaneous coronary intervention.* **Frontiers in Cardiovascular Medicine**, April 2024. https://doi.org/10.3389/fcvm.2024.1353392. Abstract: “Acute glucocorticoid deficiency under stress is very dangerous.”
- Powers P et al. *Adrenal Crisis in a Delayed Diagnosis of Sheehan Syndrome.* **Cureus**, 27 August 2023. https://doi.org/10.7759/cureus.44225. The report documents shock after interruption of chronic steroid therapy (powers2023adrenalcrisisin pages 1-2).
- Matsuzaki S et al. *A case of acute Sheehan’s syndrome and literature review.* **BMC Pregnancy and Childbirth**, June 2017. https://doi.org/10.1186/s12884-017-1380-y. Abstract: acute SS is a “rare but life-threatening complication of postpartum hemorrhage.” (matsuzaki2017acaseof pages 8-9)

PMIDs were not exposed in the retrieved full-text metadata for several sources; DOI URLs are therefore supplied rather than risking incorrect PMID assignment.

References

1. (karaca2025sheehansyndromea pages 1-2): Zuleyha Karaca and Fahrettin Kelestimur. Sheehan syndrome: a current approach to a dormant disease. Pituitary, Jan 2025. URL: https://doi.org/10.1007/s11102-024-01481-1, doi:10.1007/s11102-024-01481-1. This article has 27 citations and is from a peer-reviewed journal.

2. (powers2023adrenalcrisisin pages 1-2): Patrick Powers, Kathryn Jan, and Deepak Bommisetty. Adrenal crisis in a delayed diagnosis of sheehan syndrome. Aug 2023. URL: https://doi.org/10.7759/cureus.44225, doi:10.7759/cureus.44225. This article has 3 citations.

3. (d.2025adecadewith pages 1-2): Kayalvizhi D., Adedeji Yusuf Moradeyo, and Bhuvaneswari G. A decade with sheehan’s syndrome: a case report and personal experience. Case Reports in Endocrinology, Jan 2025. URL: https://doi.org/10.1155/crie/6010326, doi:10.1155/crie/6010326. This article has 0 citations.

4. (matsuzaki2017acaseof pages 8-9): Shinya Matsuzaki, Masayuki Endo, Yutaka Ueda, Kazuya Mimura, Aiko Kakigano, Tomomi Egawa-Takata, Keiichi Kumasawa, Kiyoshi Yoshino, and Tadashi Kimura. A case of acute sheehan’s syndrome and literature review: a rare but life-threatening complication of postpartum hemorrhage. BMC Pregnancy and Childbirth, Jun 2017. URL: https://doi.org/10.1186/s12884-017-1380-y, doi:10.1186/s12884-017-1380-y. This article has 104 citations and is from a peer-reviewed journal.

5. (zain2022ararecase pages 4-5): Ahmer Zain, Ashwin Sivakumar, Ozo Akah, Saher T Shiza, Ashwini Mahadevaiah, and Aadil Khan. A rare case of sheehan syndrome with cardiac tamponade. Apr 2022. URL: https://doi.org/10.7759/cureus.24329, doi:10.7759/cureus.24329. This article has 4 citations.

6. (samman2025delayeddiagnosisof pages 3-4): Basim S Samman, Abdullah F Alzarroug, Raghad Altayyar, Bayan S Alalawi, and Hatim Mahmoud. Delayed diagnosis of sheehan’s syndrome in an 89-year-old female: a case report and review of literature. Jun 2025. URL: https://doi.org/10.7759/cureus.85332, doi:10.7759/cureus.85332. This article has 1 citations.

7. (vasconcelos2024acasereport pages 7-8): Ana Luís Vasconcelos, Rita Pinto Ribeiro, Patrícia Claúdio Ferreira, Joana Maciel, and Rosário Araújo. A case report of sheehan syndrome: a rare cause of hypopituitarism. Feb 2024. URL: https://doi.org/10.7759/cureus.53544, doi:10.7759/cureus.53544. This article has 2 citations.

8. (singh2023postpartumpituitaryapoplexy pages 4-4): S Singh and S Jamal. Postpartum pituitary apoplexy masking as postpartum eclampsia: a rare case report. Unknown journal, 2023.

## Artifacts

- [Edison artifact artifact-00](Sheehan_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019618` (5 mentions) - the report calls it "if available"; MONDO calls it **Sheehan syndrome**