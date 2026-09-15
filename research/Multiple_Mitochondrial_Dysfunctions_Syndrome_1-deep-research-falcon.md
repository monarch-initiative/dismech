---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T02:48:02.730581'
end_time: '2026-09-06T02:58:12.198271'
duration_seconds: 609.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 1
  mondo_id: MONDO:0011582
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 54
  verified: 54
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0011582
    reported_labels:
    - if available
    ontology_label: multiple mitochondrial dysfunctions syndrome 1
  - term_id: HP:0001252
    reported_labels:
    - Common in clinical series
    ontology_label: Hypotonia
  - term_id: HP:0002154
    reported_labels:
    - Glycine elevated in 7/7 in Ahting et al
    ontology_label: Hyperglycinemia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Multiple_Mitochondrial_Dysfunctions_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 1
- **MONDO ID:** MONDO:0011582 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 1** covering all of the
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
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 1
- **MONDO ID:** MONDO:0011582 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 1** covering all of the
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


# Multiple Mitochondrial Dysfunctions Syndrome 1 (MMDS1)

## Executive summary

Multiple mitochondrial dysfunctions syndrome 1 is an ultra-rare, autosomal-recessive mitochondrial disorder caused by biallelic pathogenic variants in **NFU1**, a late-acting iron–sulfur-cluster carrier. Classical MMDS1 is a neonatal/infantile multisystem encephalopathy characterized by hypotonia, feeding failure, developmental arrest or regression, hyperglycinemia, lactic acidosis, respiratory failure, cavitating leukoencephalopathy, and frequently pulmonary arterial hypertension (PAH). Most historically reported severe cases died in infancy. More recent genotype-led ascertainment has established a broader **NFU1-related disease continuum**, extending to childhood-onset, slowly progressive or episodic hereditary spastic paraplegia (HSP) with substantially longer survival. (ahting2015clinicalbiochemicaland pages 1-2, kaiyrzhanov2022phenotypiccontinuumof pages 1-2, lebigot2021areviewof pages 4-5)

NFU1 deficiency impairs transfer of [4Fe–4S] clusters to selected mitochondrial clients. Particularly important consequences are loss of lipoic-acid synthase activity and protein lipoylation, dysfunction of pyruvate and α-ketoglutarate dehydrogenases and the glycine-cleavage system, respiratory-chain impairment, and—according to 2023 patient-fibroblast work—attenuated mitochondrial protein synthesis. No approved disease-modifying treatment or MMDS1-specific interventional trial was identified; management remains multidisciplinary and supportive. (jain2020assemblyofthe pages 2-2, zhong2023bola3andnfu1 pages 1-2, ahting2015clinicalbiochemicaland pages 5-6)

| Domain | High-confidence finding | Quantitative evidence | Evidence type/source |
|---|---|---|---|
| Disease/gene identity | MMDS1 is an autosomal-recessive mitochondrial iron–sulfur-cluster maturation disorder caused by biallelic **NFU1** variants; identifiers include **MONDO:0011582** and **OMIM 605711**. | More than 35 affected individuals had been reported worldwide by 2021. | Aggregated disease-target evidence and systematic review (OpenTargets Search: Multiple mitochondrial dysfunctions syndrome 1-NFU1, lebigot2021areviewof pages 2-4, lebigot2021areviewof pages 4-5) |
| Severe infantile phenotype | Classical MMDS1 causes neonatal/infantile encephalopathy with hypotonia, feeding failure, respiratory disease, neurologic regression, and early death. | In one seven-patient cohort, **6/7** died within 6 months; an earlier 20-patient summary recorded **20/20 deaths**. | Human clinical cohort and literature review (ahting2015clinicalbiochemicaland pages 1-2, alfadhel2017mitochondrialironsulfurcluster pages 6-6) |
| Milder NFU1–HSP continuum | Hypomorphic biallelic missense variants can cause pure or complex hereditary spastic paraplegia with longer survival, demonstrating broader expressivity than classical MMDS1. | **19** individuals from **10** families: HSP-predominant disease in **16/19** and neurodevelopmental delay with severe hypotonia in **3/19**. | Multicenter human cohort (kaiyrzhanov2022phenotypiccontinuumof pages 1-2) |
| Diagnostic biomarkers | Elevated lactate and glycine, reduced pyruvate-dehydrogenase activity, and respiratory-chain defects—especially complexes I and II—are important biochemical clues but are not individually specific. | Ahting cohort: elevated lactate **5/6**, elevated glycine **7/7**, PDH deficiency **5/5**, and complex I/II+III defects **4/5** tested. | Human biochemical cohort (ahting2015clinicalbiochemicaland pages 1-2) |
| MRI | Typical imaging shows symmetric progressive or cavitating white-matter disease; basal-ganglia, thalamic, brainstem, spinal-cord, and corpus-callosum abnormalities may occur. White-matter disease also accompanies milder NFU1-HSP. | White-matter abnormalities were present in all members of the reported 19-person NFU1-continuum cohort. | Human MRI cohorts and systematic review (lebigot2021areviewof pages 6-7, ahting2015clinicalbiochemicaland pages 5-6, kaiyrzhanov2022phenotypiccontinuumof pages 1-2) |
| Core mechanism | Defective NFU1-mediated **[4Fe–4S]** delivery compromises LIAS and selected respiratory proteins, reducing protein lipoylation and impairing PDH, α-ketoglutarate dehydrogenase, glycine cleavage, and oxidative phosphorylation. | ISCU2 and ISCA1 donate clusters to NFU1; FDX2 assists formation of its bridging [4Fe–4S] cluster. | Biochemical/cellular mechanistic study supported by patient biochemistry (jain2020assemblyofthe pages 2-2, ahting2015clinicalbiochemicaland pages 1-2) |
| Pulmonary hypertension | Pulmonary arterial hypertension is a major, sometimes fatal MMDS1 manifestation, particularly reported with **p.Gly208Cys**. A humanized NFU1 rat reproduced pulmonary vascular remodeling and sex-biased susceptibility. | PAH was estimated in approximately **70%** of reported Gly208Cys-associated cases; penetrance was greater in female than male mutant rats. | Human case synthesis and CRISPR rat model (niihori2020ratswitha pages 1-5, lebigot2021areviewof pages 6-7) |
| Treatment/trials | No approved disease-modifying treatment or MMDS1-specific interventional trial was identified; documented care is supportive, including respiratory, nutritional, cardiac/pulmonary, neurologic, rehabilitative, and palliative management. | Registry search returned **no relevant MMDS1 interventional trial**; severe published cases received measures such as artificial ventilation and palliative care. | Trial-registry search and human clinical reports (ahting2015clinicalbiochemicaland pages 5-6, lebigot2021areviewof pages 4-5) |
| Key 2023 development: translation | NFU1-mutant patient fibroblasts revealed previously unrecognized attenuation of mitochondrial protein synthesis; the proposed route is ISCA1–NFU1 delivery of a [4Fe–4S] cluster to METTL17 during small mitoribosomal-subunit assembly. | No NFU1-specific clinical effect size reported. | Patient-derived fibroblasts and mechanistic cell studies, published October 2023 (zhong2023bola3andnfu1 pages 1-2) |
| Key 2023 development: neuromuscular signaling | Patient-specific *C. elegans* NFU1 variants caused allele-dependent cholinergic dysfunction: Gly147Arg produced acetylcholine hypersensitivity rescued by reducing acetylcholine release, whereas Gly166Cys predominantly caused postsynaptic hypersensitivity. | Reducing acetylcholine release rescued nearly all measured Gly147Arg neuromuscular phenotypes. | CRISPR *C. elegans* model, published February 2023; therapeutic relevance remains preclinical (kropp2023patientspecificvariantsof pages 11-11, kropp2023patientspecificvariantsof pages 1-2) |


*Table: Concise synthesis of established clinical, biochemical, mechanistic, and model-system evidence for NFU1-related MMDS1, including quantitative cohort findings and major 2023 advances.*

## 1. Disease information

### Definition and classification

MMDS1 is a nuclear-encoded mitochondrial Fe–S protein-maturation disorder. It is one of a group of MMDS disorders caused by defects in late mitochondrial [4Fe–4S]-cluster assembly or delivery. It is best regarded as the severe end of the broader **NFU1-related disorder** spectrum rather than as an invariant infantile phenotype. (lebigot2021areviewof pages 2-4, kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0011582.
- **OMIM phenotype:** **605711**. Some literature tables label this number directly as MMDS1. (alfadhel2017mitochondrialironsulfurcluster pages 6-6, lebigot2021areviewof pages 4-5)
- **Gene:** **NFU1**, approved name *NFU1 iron-sulfur cluster scaffold*; Ensembl **ENSG00000169599**. Open Targets identifies NFU1 as the single associated target for MONDO:0011582. (OpenTargets Search: Multiple mitochondrial dysfunctions syndrome 1-NFU1)
- **Common names:** multiple mitochondrial dysfunctions syndrome 1; MMDS1; NFU1 deficiency; NFU1-related mitochondrial disease; NFU1-related disorder; mitochondrial [4Fe–4S]-protein maturation defect.
- **ICD/MeSH:** No uniquely specific ICD-10, ICD-11, or MeSH code was established in the retrieved literature. Coding generally falls under inherited mitochondrial/metabolic or neurologic disease categories and should not be treated as MMDS1-specific.

The evidence summarized here is predominantly **aggregated disease-level literature**, supplemented by small patient cohorts, individual case reports, patient-derived fibroblasts, and engineered animal models. It is not derived from a population-scale EHR dataset.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

MMDS1 is caused by **germline biallelic NFU1 variants**—homozygous or compound heterozygous—leading to partial or severe loss of NFU1-mediated Fe–S-cluster delivery. This is a monogenic autosomal-recessive disorder, not an infectious, toxic, lifestyle, or environmentally acquired disease. (kropp2021allelespecificmitochondrialstress pages 1-2, kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

### Genetic risk factors

Reported disease alleles include missense, splice-altering, frameshift, and deletion/insertion alleles. Recurrently reported substitutions include **p.Gly208Cys**, **p.Gly189Arg**, p.Arg182Gln, p.Arg182Trp, p.Gly190Arg, p.Arg21Pro, and p.Cys210Phe; reported splice/frameshift alleles include c.302+3A>G with predicted p.Val56Glyfs*9. Variant nomenclature has differed across transcripts/publications and should be normalized to the current MANE transcript before database loading. (alfadhel2017mitochondrialironsulfurcluster pages 6-6, ahting2015clinicalbiochemicaland pages 5-6)

The p.Gly208Cys allele alters the region surrounding NFU1’s conserved Cys motif and can increase cluster retention while impairing transfer to recipient proteins. p.Gly189Arg has repeatedly been associated with residual function and, in some patients, later onset or longer survival, although genotype–phenotype prediction remains imperfect. (lebigot2021areviewof pages 6-7)

All established disease variants are germline. No somatic MMDS1 mechanism, repeat expansion, aneuploidy, recurrent translocation, or epigenetic primary cause is established. The retrieved studies do not provide reliable gnomAD allele frequencies, carrier-frequency estimates, or a ClinGen-curated penetrance value; individual pathogenic alleles are expected to be very rare.

### Environmental and protective factors

No toxin, diet, smoking behavior, radiation exposure, pathogen, or occupational exposure is known to cause MMDS1. No validated protective genetic variant, diet, supplement, or lifestyle intervention has been demonstrated.

A clinically important interaction is **metabolic stress**: fever or infection frequently preceded reversible or irreversible neurologic decompensation in the 19-person milder NFU1 cohort, and an infectious episode preceded severe regression in a reported cavitating-leukoencephalopathy case. Infection is therefore a trigger of deterioration in genetically affected individuals, not the underlying cause. (kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

Sex may modify PAH expression: female CRISPR Nfu1-mutant rats developed PAH more often than males, while males showed increased ISCU expression and complex-IV activity. This is compelling model evidence but not a validated human MMDS1 sex-risk estimate. (niihori2020ratswitha pages 1-5)

## 3. Phenotypes

### Classical severe MMDS1

| Phenotype | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Global developmental delay/arrest and regression | Sign; neonatal/infantile, severe and progressive or crisis-associated | Characteristic across historical cases | HP:0001263; HP:0002376 |
| Generalized/axial hypotonia | Sign; early, often severe | Common in clinical series | HP:0001252 |
| Feeding difficulty, poor feeding, vomiting, failure to thrive | Symptom/sign; early and progressive | Recurrent | HP:0011968; HP:0002013; HP:0001508 |
| Respiratory distress, apnea, stridor, respiratory failure | Sign; episodic or progressive, potentially fatal | Recurrent | HP:0002098; HP:0002104; HP:0010307; HP:0002878 |
| Seizures or myoclonus | Neurologic sign; variable | Reported repeatedly | HP:0001250; HP:0001336 |
| Spasticity, dystonia, tetraparesis or motor loss | Neurologic sign; progressive or crisis-associated | Variable; central in milder HSP spectrum | HP:0001257; HP:0001332; HP:0002273 |
| Pulmonary hypertension/right-heart failure | Cardiopulmonary sign; severe and sometimes acute/fatal | Important MMDS1 clue; approximately 70% quoted for Gly208Cys-associated cases in the rat-study background | HP:0002092; HP:0001708 |
| Leukoencephalopathy, sometimes cavitating | MRI sign; often symmetric and progressive | Highly characteristic | HP:0002415; HP:0012444 |
| Lactic/metabolic acidosis | Laboratory abnormality; persistent or crisis-related | Lactate elevated in 5/6 in Ahting et al. | HP:0003128; HP:0001942 |
| Hyperglycinemia | Laboratory abnormality | Glycine elevated in 7/7 in Ahting et al. | HP:0002154 |
| Cardiomyopathy/hepatopathy/tubulopathy | Secondary multisystem signs | Occasional | HP:0001638; HP:0001392; HP:0000124 |

These manifestations and additional findings—lethargy, abnormal myelination, brainstem or spinal-cord lesions, punctate hemorrhage, basal-ganglia/thalamic lesions, and corpus-callosum abnormalities—are documented across small cohorts and reviews. (lebigot2021areviewof pages 6-7, ahting2015clinicalbiochemicaland pages 5-6, lebigot2021areviewof pages 4-5)

### Quantitative clinical evidence

In Ahting et al.’s seven-patient cohort, six patients had fatal infantile encephalopathy and PAH leading to death within the first six months. Biochemical testing showed PDH deficiency in 5/5, respiratory-chain I and II+III defects in 4/5, elevated lactate in 5/6, and elevated glycine in 7/7. (ahting2015clinicalbiochemicaland pages 1-2)

A 2017 literature table summarized 20 neonatal/infantile patients and recorded 20/20 deaths, reflecting ascertainment of the severe historical phenotype rather than present-day survival across all NFU1-related disease. (alfadhel2017mitochondrialironsulfurcluster pages 6-6)

### Milder NFU1-related HSP phenotype

The pivotal 2022 multicenter study described 19 affected individuals from ten families with ultra-rare biallelic missense variants: **16/19** had early-onset pure or complex HSP with longer survival, while **3/19** had neurodevelopmental delay with severe hypotonia. Febrile decompensation was common, and white-matter abnormalities were present throughout the cohort. The authors’ central conclusion was that MMDS1 and HSP represent “two ends of the NFU1-related phenotypic continuum.” (kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

### Quality of life

No MMDS1-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or health-utility study was located. Functional burden can nevertheless be inferred to be profound: severe cases require respiratory and feeding support and often palliative care; longer-surviving HSP cases experience progressive gait impairment, spasticity, neuropathy, and vulnerability to febrile regression. Formal per-phenotype QoL estimates are unavailable. (ahting2015clinicalbiochemicaland pages 5-6, kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

## 4. Genetic and molecular information

### Causal gene and protein

**NFU1** encodes a mitochondrial late-acting Fe–S carrier that assembles or accepts a bridging [4Fe–4S] cluster and transfers it to a restricted set of recipient proteins. ISCU2 and ISCA1 donate [2Fe–2S] precursors; NFU1 dimerization and FDX2-assisted reductive coupling produce the [4Fe–4S] form. A conserved C-terminal hydrophobic patch mediates interactions with ISCU2/ISCA1. (jain2020assemblyofthe pages 2-2)

Suggested annotations include:

- **GO biological process:** iron–sulfur cluster assembly (GO:0016226); iron–sulfur cluster transport/transfer; mitochondrial respiratory-chain complex assembly; protein lipoylation; mitochondrial translation.
- **GO molecular function:** iron–sulfur cluster binding; metal-cluster carrier activity.
- **GO cellular component:** mitochondrial matrix (GO:0005759); mitochondrion (GO:0005739).
- **Chemical entities:** [4Fe–4S] cluster; [2Fe–2S] cluster; lipoate/lipoic acid; pyruvate; lactate; glycine; α-ketoglutarate. Appropriate ChEBI identifiers should be validated against the current ontology release.

### Variant consequences

Most variants act through loss or reduction of function: impaired protein stability, cluster acquisition, oligomerization, or cluster transfer. Engineered variants form an allelic series rather than behaving as uniform nulls. This helps explain variable expressivity and the MMDS1–HSP continuum. (kropp2021allelespecificmitochondrialstress pages 1-2, kropp2021allelespecificmitochondrialstress pages 2-4)

For clinical curation, each variant requires transcript-normalized HGVS, zygosity, segregation, functional evidence, population frequency, and current ClinVar/ACMG classification. The literature predates uniform application of current ACMG/AMP specifications, so “reported pathogenic” should not automatically be copied as a contemporary laboratory classification.

### Modifiers and epigenetics

No human modifier gene has been validated. Increased ISCU expression was associated with relative protection from PAH in male mutant rats, providing a mechanistic modifier hypothesis rather than a human clinical modifier. No reproducible disease-specific DNA-methylation signature, histone alteration, chromatin defect, or pathogenic epimutation is known. (niihori2020ratswitha pages 1-5)

## 5. Environmental information

Environmental exposures are not etiologic. The main clinically relevant external stressors are fever, infection, fasting/catabolism, dehydration, and other metabolic stresses that may exceed already restricted mitochondrial reserve. The febrile association is supported by human cohorts, whereas fasting and catabolic-risk recommendations are extrapolated from mitochondrial medicine practice rather than MMDS1 trials. (kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

No infectious agent is specifically causal, and MMDS1 is neither communicable nor zoonotic.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic NFU1 pathogenic variants lead to** reduced abundance, abnormal oligomerization, impaired cluster acquisition, or defective transfer by mitochondrial NFU1.
2. **Defective NFU1 leads to** failure of late [4Fe–4S]-cluster delivery to selected recipient proteins; ISCU2/ISCA1-to-NFU1 transfer and FDX2-assisted cluster formation are upstream biochemical steps. (jain2020assemblyofthe pages 2-2)
3. **Insufficient [4Fe–4S] delivery leads to** reduced activity/stability of lipoic-acid synthase and selected respiratory-chain/aconitase targets. (jain2020assemblyofthe pages 2-2, kaiyrzhanov2022phenotypiccontinuumof pages 1-2)
4. **LIAS dysfunction leads to** deficient lipoylation of the E2/H components of pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, branched-chain ketoacid dehydrogenase, and the glycine-cleavage system.
5. **Loss of PDH/KGDH activity leads to** impaired carbon entry and flux through the tricarboxylic-acid cycle, reduced oxidative ATP generation, pyruvate-to-lactate diversion, and accumulation of organic-acid intermediates.
6. **Glycine-cleavage failure leads to** hyperglycinemia, which may compound neurologic dysfunction.
7. **Respiratory-chain dysfunction leads to** reduced oxidative phosphorylation, altered redox state, membrane-potential loss, and variant-dependent reactive oxygen species/reactive iron stress. (kropp2021allelespecificmitochondrialstress pages 11-12, kropp2021allelespecificmitochondrialstress pages 1-2)
8. **NFU1 deficiency also leads to** impaired [4Fe–4S] loading of METTL17 during small-mitoribosomal-subunit assembly—**proposed rather than fully proven in vivo**—and results in attenuated mitochondrial protein synthesis in patient fibroblasts. (zhong2023bola3andnfu1 pages 1-2)
9. **Energy/redox/translation failure leads to** dysfunction and injury in high-demand oligodendroglial, neuronal, muscular, respiratory, myocardial, and pulmonary-vascular cells; the exact cell-death sequence is partly inferred.
10. **White-matter injury leads to** leukoencephalopathy, regression, hypotonia/spasticity and seizures, while pulmonary-vascular metabolic remodeling leads to PAH, right-ventricular hypertrophy and potentially fatal right-heart failure. The vascular causal link is supported directly in mutant rats. (niihori2020ratswitha pages 1-5)

### Cellular and tissue interpretation

The hallmark white-matter disease suggests high vulnerability of oligodendrocytes (**CL:0000128**), their precursors (**CL:0002453**), and myelinated axons/neurons (**CL:0000540**), although human single-cell confirmation is unavailable. Pulmonary arterial endothelial cells (**CL:0000115**) and vascular smooth-muscle cells (**CL:0000359**) are implicated by vascular remodeling; cardiomyocytes (**CL:0000746**) and skeletal myocytes (**CL:0000188**) are affected through energy failure.

Suggested GO processes include oxidative phosphorylation (GO:0006119), aerobic respiration (GO:0009060), mitochondrial translation (GO:0032543), response to oxidative stress (GO:0006979), axon ensheathment (GO:0008366), and regulation of membrane potential. Inflammation, adaptive immunity, Wnt, MAPK, PI3K–AKT, and mTOR are not established primary disease pathways.

### Molecular profiling

- **Proteomic/biochemical:** reduced lipoylated mitochondrial proteins and recipient-enzyme activities are the most reproducible molecular signature. (ahting2015clinicalbiochemicaland pages 1-2, jain2020assemblyofthe pages 2-2)
- **Metabolomic:** elevated lactate, pyruvate and glycine; occasional urinary α-ketoglutarate, glutarate, or 2-hydroxybutyrate. (lebigot2021areviewof pages 6-7, alfadhel2017mitochondrialironsulfurcluster pages 6-6)
- **Translation profiling:** 2023 work demonstrated reduced mitochondrial pulse-label synthesis in NFU1-mutant fibroblasts and connected NFU1 to METTL17/mitoribosome assembly. (zhong2023bola3andnfu1 pages 1-2)
- **Single-cell/spatial transcriptomics/multi-omics:** no MMDS1-specific human atlas was located.
- **Functional genomics:** CRISPR models in rat and *C. elegans* are available; no clinically validated genome-wide therapeutic screen was found.

## 7. Anatomical structures affected

### Organ and system level

The primary systems are the **central nervous system**, neuromuscular system, lungs/pulmonary vasculature, and systemic energy metabolism. Secondary involvement includes heart/right ventricle, skeletal muscle, liver, kidney tubules, and respiratory apparatus. (ahting2015clinicalbiochemicaland pages 5-6, lebigot2021areviewof pages 4-5)

Suggested UBERON mappings include brain (UBERON:0000955), cerebral white matter (UBERON:0002437), corpus callosum (UBERON:0002336), basal ganglion (UBERON:0002420), thalamus (UBERON:0001897), brainstem (UBERON:0002298), spinal cord (UBERON:0002240), lung (UBERON:0002048), pulmonary artery (UBERON:0002012), heart (UBERON:0000948), skeletal muscle tissue (UBERON:0001134), liver (UBERON:0002107), and kidney (UBERON:0002113). Identifier validation against the target ontology version is advised.

### Subcellular level

The initiating defect is in the mitochondrial matrix and affects Fe–S carriers, respiratory-chain machinery, TCA-cycle/lipoylated complexes, glycine cleavage, and mitoribosome assembly. No consistent lateralization is expected; MRI abnormalities are generally bilateral/symmetric.

## 8. Temporal development

Classical disease begins neonatally or in early infancy, sometimes after an initially unremarkable period. The course is usually rapidly progressive, with feeding and respiratory deterioration, metabolic acidosis, encephalopathy, regression, and PAH. Onset from birth to approximately nine months was represented in early clinical literature. (ahting2015clinicalbiochemicaland pages 1-2)

Longer-surviving NFU1 disease may begin in infancy or childhood with motor delay, lower-limb spasticity, gait disturbance, or hypotonia. Its course may be slowly progressive or relapsing/stepwise, with febrile illnesses producing reversible or permanent loss of function. (kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

There are no validated stages. A practical clinical framework is: presymptomatic genetically affected; early developmental/metabolic abnormalities; established neurologic or cardiopulmonary disease; crisis/decompensation; and advanced respiratory/right-heart or severe neurologic failure. Spontaneous remission is not established, although partial recovery after febrile decompensation occurs in some milder patients.

## 9. Inheritance and population

Inheritance is autosomal recessive. Parents of an affected individual are usually heterozygous carriers; for a couple in whom both partners carry the relevant familial allele, each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability, assuming ordinary Mendelian segregation.

By 2021, more than 35 MMDS1 patients from multiple continents had been published, but this is a literature count—not prevalence. No reliable incidence per 100,000, prevalence, carrier frequency, sex ratio, or population-based survival estimate exists. (lebigot2021areviewof pages 2-4, lebigot2021areviewof pages 4-5)

Consanguinity is present in some families but is not required; both consanguineous homozygous and non-consanguineous compound-heterozygous families are reported. A recurrent p.Gly208Cys allele occurred in Spanish/French patients and has been described as a founder allele, but its population carrier frequency is not established in the retrieved evidence. (ahting2015clinicalbiochemicaland pages 1-2, ahting2015clinicalbiochemicaland pages 5-6)

Penetrance appears high for individuals with two clearly damaging alleles, but severity is highly variable and formal penetrance estimates are unavailable. There is no evidence of anticipation. Germline mosaicism has not been quantified; standard counseling should acknowledge a small residual recurrence risk after an apparently de novo allele.

## 10. Diagnostics

### When to suspect MMDS1

Consider NFU1 disease in a neonate or infant with combinations of hyperglycinemia, lactic acidosis, hypotonia/regression, respiratory failure, PAH, and symmetric or cavitating leukoencephalopathy. Also consider it in early-onset HSP with white-matter abnormalities, especially where fever precipitates neurologic decline. (ahting2015clinicalbiochemicaland pages 5-6, kaiyrzhanov2022phenotypiccontinuumof pages 1-2)

### Recommended investigations

1. **Urgent chemistry/metabolic testing:** blood gas, lactate, pyruvate, glucose, electrolytes, liver/renal indices; plasma amino acids with glycine; CSF lactate and amino acids when clinically safe; urine organic acids; acylcarnitines and standard metabolic crisis studies.
2. **Cardiopulmonary evaluation:** ECG, echocardiography with PA-pressure/right-heart assessment, oxygenation and respiratory review. PAH may be a decisive clue and requires specialist confirmation.
3. **Neurodiagnostics:** brain MRI with diffusion-weighted imaging and spectroscopy where available; EEG for seizures; EMG/nerve-conduction studies in HSP/neuropathy phenotypes.
4. **Biochemical confirmation:** PDH activity, respiratory-chain enzyme studies, succinate dehydrogenase/complex-II assessment, and immunoblotting for lipoylated DLAT/DLST/GCSH in fibroblasts or muscle can support pathogenicity. In Ahting et al., the combination of PDH and respiratory-chain testing had high yield, but normal results in one tissue do not exclude milder disease. (ahting2015clinicalbiochemicaland pages 1-2, lebigot2021areviewof pages 6-7)
5. **Genetic confirmation:** sequence and deletion/duplication analysis of **NFU1**, preferably through a mitochondrial disease, leukodystrophy, hyperglycinemia, or HSP multigene panel, or trio WES/WGS. The 2021 review explicitly concluded that large NGS panels or exome sequencing are needed for confirmation. (lebigot2021areviewof pages 2-4)
6. **RNA analysis:** fibroblast RNA/cDNA testing is useful for suspected splice variants or when only one pathogenic allele is found.

WGS is useful for deep intronic, structural, or otherwise unresolved variants; WES is effective for coding/splice-region variants. Chromosomal microarray, karyotype, FISH, mtDNA-only sequencing, and repeat-expansion testing are not first-line tests for a classic NFU1 presentation, although mtDNA analysis may be included in a broad mitochondrial workup.

### Differential diagnosis

Key alternatives are MMDS2–5/other late Fe–S maturation disorders (**BOLA3, IBA57, ISCA2, ISCA1**), primary lipoate-synthesis defects (**LIAS, LIPT1, LIPT2**), glycine-cleavage disorders (**GLDC, AMT, GCSH**), primary PDH-complex defects, other mitochondrial respiratory-chain disorders, and cavitating leukodystrophies including APOPT1-related disease. NFU1 is favored by combined PDH/lipoylation and respiratory-chain defects, hyperglycinemia, PAH, and characteristic white-matter disease, but molecular confirmation is required. (kropp2021allelespecificmitochondrialstress pages 29-30, ahting2015clinicalbiochemicaland pages 5-6)

There are no validated standalone clinical diagnostic criteria. Prenatal molecular diagnosis is possible only after familial variants are established. MMDS1 is not a standard universal newborn-screening condition; biochemical markers lack adequate specificity and no proven early disease-modifying therapy currently satisfies classic screening criteria.

## 11. Outcomes and prognosis

Historical prognosis was extremely poor: 6/7 patients in a 2015 cohort died by six months, and an older 20-patient literature summary recorded 20/20 deaths. These figures should not be generalized to every genotype because later cohorts uncovered longer-surviving HSP phenotypes. (ahting2015clinicalbiochemicaland pages 1-2, alfadhel2017mitochondrialironsulfurcluster pages 6-6)

Major causes or mediators of death include respiratory failure, PAH/right-heart failure, severe metabolic decompensation, and progressive encephalopathy. Prognostic indicators likely include age at onset, residual NFU1 activity, variant class, PAH, ventilatory dependence, severity of white-matter disease, and recurrent crises, but no validated prognostic score or biomarker exists.

Survivors may have persistent intellectual, motor, spastic, dystonic, neuropathic, respiratory, and feeding disability. There are no 5- or 10-year survival curves and no controlled treatment-versus-no-treatment survival analysis.

## 12. Treatment and current applications

### Current standard: supportive multidisciplinary care

No therapy has been shown to restore NFU1 function or alter survival in controlled human studies. Published severe cases received interventions such as artificial ventilation and palliative care. (ahting2015clinicalbiochemicaland pages 5-6)

Practical management includes:

- stabilization of airway, breathing, circulation, glucose and acid–base balance during crises;
- early enteral nutrition assessment and aspiration prevention;
- seizure-directed therapy guided by EEG and mitochondrial-drug safety;
- respiratory support, secretion management, sleep/ventilation studies and vaccination;
- serial echocardiography and expert PAH/right-heart management;
- physical, occupational, speech, feeding and spasticity therapies;
- hearing, vision, orthopedic, hepatic and renal surveillance according to phenotype;
- early palliative-care involvement in severe disease.

These map broadly to NCIT concepts for supportive care, mechanical ventilation, enteral nutrition, physical therapy, occupational therapy, speech therapy, anticonvulsant therapy, and palliative care. Exact NCIT codes should be verified in the intended terminology release.

### Drugs and advanced therapeutics

No NFU1-specific approved drug, established pharmacogenomic rule, gene therapy, cell therapy, ASO/siRNA therapy, or enzyme-replacement therapy exists. Empiric “mitochondrial cocktails,” lipoic acid, thiamine, riboflavin, biotin, carnitine, antioxidants, or dichloroacetate lack MMDS1 efficacy evidence and can carry risks; they should not be represented as proven therapies.

A 2023 *C. elegans* study found that reducing acetylcholine release rescued nearly all Gly147Arg neuromuscular phenotypes, raising an allele-specific cholinergic-treatment hypothesis. The opposite/partly postsynaptic behavior of Gly166Cys underscores why this is **not** yet a general treatment recommendation. (kropp2023patientspecificvariantsof pages 11-11, kropp2023patientspecificvariantsof pages 1-2)

The tool-based ClinicalTrials.gov search found no relevant MMDS1/NFU1 interventional trial. Accordingly, response rates, adverse-event frequencies, treatment algorithms, and combination-therapy outcomes are unavailable.

## 13. Prevention

Primary prevention through lifestyle modification is not possible because MMDS1 is inherited. Effective reproductive prevention options after molecular diagnosis include genetic counseling, carrier testing of the reproductive partner and relatives, cascade testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease.

Secondary prevention consists of early recognition in siblings and at-risk relatives, baseline cardiopulmonary/MRI/metabolic assessment, and rapid treatment of fever, infection, poor intake, dehydration, and catabolism. Families should receive a written emergency plan. These measures are clinically rational but have not been tested in MMDS1 trials.

Tertiary prevention targets aspiration, contractures, malnutrition, respiratory infections, seizures, PAH/right-heart failure, and avoidable metabolic stress. Routine age-appropriate immunization, including respiratory-pathogen vaccines, is appropriate; no disease-specific vaccine or prophylactic medication exists.

## 14. Other species and natural disease

NFU1 and mitochondrial Fe–S transfer are evolutionarily conserved. Relevant experimental species include:

- *Rattus norvegicus* — NCBI Taxonomy **10116**;
- *Caenorhabditis elegans* — NCBI Taxonomy **6239**;
- *Homo sapiens* — NCBI Taxonomy **9606**.

No well-established naturally occurring NFU1-MMDS1 veterinary syndrome, breed predisposition, VBO mapping, zoonotic transmission, or cross-species infectious susceptibility was identified. Comparative evidence is therefore principally from induced genetic models rather than natural animal disease.

## 15. Model organisms and advanced experimental systems

### CRISPR Nfu1-G206C rat

The rat mutation corresponds to human p.Gly208Cys. Homozygous rats developed elevated right-ventricular pressure, right-ventricular hypertrophy, pulmonary-artery remodeling, and severe angio-obliterative vascular changes. Both sexes had reduced complex-II activity/expression, PDH activity, and lipoate binding, but PAH was more penetrant in females; males showed preserved NFU1 oligomerization, increased ISCU and increased complex-IV activity. This is strong in-vivo causal evidence linking NFU1 dysfunction to PAH. Its major limitation is incomplete recapitulation of fatal infantile encephalopathy: the animals survived to adulthood. (niihori2020ratswitha pages 1-5)

### Patient-variant *C. elegans*

CRISPR recreation of five patient variants in *nfu-1* produced an allelic series of respiratory dysfunction, membrane-potential changes, oxidative stress and reactive mitochondrial iron. Reactive iron occurred only with some alleles, showing that iron dyshomeostasis is a variant-dependent contributor rather than a universal mechanism. DAF-16 and SKN-1 stress responses and body-wall-muscle reporter changes were allele specific. (kropp2021allelespecificmitochondrialstress pages 11-12, kropp2021allelespecificmitochondrialstress pages 1-2)

A subsequent 2023 study found opposite cholinergic effects from Gly147Arg and Gly166Cys. Gly147Arg produced acetylcholine hypersensitivity and was rescued by reducing acetylcholine release; Gly166Cys produced predominantly postsynaptic hypersensitivity through an unresolved mechanism. Limitations include species differences, homozygous modeling of variants that may occur as compound heterozygotes in patients, and inability to model human PAH or white-matter disease. (kropp2023patientspecificvariantsof pages 11-11, kropp2023patientspecificvariantsof pages 1-2)

### Human fibroblasts and recent developments

Patient fibroblasts remain the most directly relevant functional system for testing protein lipoylation, respiratory-chain activity, splice effects, and NFU1 abundance. The principal recent advance was Zhong et al. (published October 2023; DOI: https://doi.org/10.1093/nar/gkad842), which identified attenuated mitochondrial protein synthesis in NFU1-mutant fibroblasts and proposed ISCA1–NFU1-mediated [4Fe–4S] insertion into METTL17 during mitoribosome assembly. The abstract states that patient fibroblasts display “previously unrecognized attenuation of mitochondrial protein synthesis.” (zhong2023bola3andnfu1 pages 1-2)

The other major 2023 development was Kropp et al. (published February 2023; DOI: https://doi.org/10.1242/dmm.049594), whose abstract reports that the two modeled variants had “altered acetylcholine signaling at neuromuscular junctions, but opposite effects on activity and motility.” (kropp2023patientspecificvariantsof pages 1-2)

No comparably transformative MMDS1-specific human clinical study from 2024 was identified in the retrieved literature. Thus, the current frontier remains mechanistic—mitoribosome biology, variant-specific stress responses, pulmonary vascular metabolism, and functional classification of rare alleles—rather than clinical therapeutics.

## Evidence limitations and knowledge-base cautions

MMDS1 evidence is dominated by small, retrospective, genotype-enriched cohorts and case reports. Historical mortality and PAH frequencies are susceptible to severe-phenotype ascertainment. Variant-level phenotypes can be confounded by compound heterozygosity, tissue-specific residual activity, inconsistent transcript numbering, and heterogeneous biochemical testing. Animal rescue findings must not be presented as human treatment evidence.

Formal prevalence, penetrance, carrier frequency, natural-history curves, standardized QoL data, validated diagnostic criteria, prospective biomarkers, controlled treatment outcomes, and human single-cell or spatial-omics data are unavailable. Claims labeled “not identified” reflect the literature and registry searches conducted for this report, not proof that no unpublished data exist.

## Selected primary and authoritative sources

1. Cameron JM et al. *American Journal of Human Genetics*. Published October 2011. “Mutations in iron-sulfur cluster scaffold genes NFU1 and BOLA3…” PMID **21944046**; DOI: https://doi.org/10.1016/j.ajhg.2011.08.011. (kropp2021allelespecificmitochondrialstress pages 29-30)
2. Navarro-Sastre A et al. Original NFU1 fatal mitochondrial disease report. Published 2011. PMID **22077971**. (kropp2021allelespecificmitochondrialstress pages 29-30)
3. Invernizzi F et al. *Frontiers in Genetics*. Published November 2014. DOI: https://doi.org/10.3389/fgene.2014.00412. Described infection-associated regression, lactic acidosis, hyperglycinemia, complex-II/PDH deficiency and cavitating leukoencephalopathy.
4. Ahting U et al. *Frontiers in Genetics* 6:123. Published 13 April 2015. PMID **25918518**; DOI: https://doi.org/10.3389/fgene.2015.00123. (OpenTargets Search: Multiple mitochondrial dysfunctions syndrome 1-NFU1, ahting2015clinicalbiochemicaland pages 1-2)
5. Jain A et al. *Human Molecular Genetics* 29:3165–3182. Published August 2020. DOI: https://doi.org/10.1093/hmg/ddaa172. (jain2020assemblyofthe pages 2-2)
6. Niihori M et al. *American Journal of Respiratory Cell and Molecular Biology* 62:231–242. Published February 2020. DOI: https://doi.org/10.1165/rcmb.2019-0065OC. (niihori2020ratswitha pages 1-5)
7. Lebigot E et al. *Biomedicines* 9:989. Published August 2021. DOI: https://doi.org/10.3390/biomedicines9080989. (lebigot2021areviewof pages 2-4, lebigot2021areviewof pages 4-5)
8. Kropp PA et al. *PLOS Genetics* 17:e1009771. Published 27 August 2021. DOI: https://doi.org/10.1371/journal.pgen.1009771. (kropp2021allelespecificmitochondrialstress pages 1-2)
9. Kaiyrzhanov R et al. *Annals of Clinical and Translational Neurology* 9:2025–2035. Published October 2022. DOI: https://doi.org/10.1002/acn3.51679. (kaiyrzhanov2022phenotypiccontinuumof pages 1-2)
10. Kropp PA et al. *Disease Models & Mechanisms* 16. Published February 2023. DOI: https://doi.org/10.1242/dmm.049594. (kropp2023patientspecificvariantsof pages 1-2)
11. Zhong H et al. *Nucleic Acids Research* 51:11797–11812. Published October 2023. DOI: https://doi.org/10.1093/nar/gkad842. (zhong2023bola3andnfu1 pages 1-2)

References

1. (ahting2015clinicalbiochemicaland pages 1-2): Uwe Ahting, Johannes A. Mayr, Arnaud V. Vanlander, Steven A. Hardy, Saikat Santra, Christine Makowski, Charlotte L. Alston, Franz A. Zimmermann, Lucia Abela, Barbara Plecko, Marianne Rohrbach, Stephanie Spranger, Sara Seneca, Boris Rolinski, Angela Hagendorff, Maja Hempel, Wolfgang Sperl, Thomas Meitinger, Joél Smet, Robert W. Taylor, Rudy Van Coster, Peter Freisinger, Holger Prokisch, and Tobias B. Haack. Clinical, biochemical, and genetic spectrum of seven patients with nfu1 deficiency. Frontiers in Genetics, Apr 2015. URL: https://doi.org/10.3389/fgene.2015.00123, doi:10.3389/fgene.2015.00123. This article has 116 citations and is from a peer-reviewed journal.

2. (kaiyrzhanov2022phenotypiccontinuumof pages 1-2): Rauan Kaiyrzhanov, Maha S. Zaki, Tracy Lau, Sambuddha Sen, Reza Azizimalamiri, Mina Zamani, Gözde Yeşil Sayin, Taru Hilander, Stephanie Efthymiou, Viorica Chelban, Ruth Brown, Kyle Thompson, Maria Irene Scarano, Jaya Ganesh, Kairgali Koneev, Ismail Musab Gülaçar, Richard Person, Dinara Sadykova, Yerdan Maidyrov, Tahereh Seifi, Aizhan Zadagali, Geneviève Bernard, Katrina Allis, Houda Zghal Elloumi, Amanda Lindy, Ehsan Taghiabadi, Sumit Verma, Rachel Logan, Brian Kirmse, Renkui Bai, Shaimaa M. Khalaf, Mohamed S. Abdel‐Hamid, Alireza Sedaghat, Gholamreza Shariati, Mahmoud Issa, Jawaher Zeighami, Hasnaa M. Elbendary, Garry Brown, Robert W. Taylor, Hamid Galehdari, Joseph J. Gleeson, Christopher J. Carroll, James A. Cowan, Andres Moreno‐De‐Luca, Henry Houlden, and Reza Maroofian. Phenotypic continuum of nfu1 ‐related disorders. Annals of Clinical and Translational Neurology, 9:2025-2035, Oct 2022. URL: https://doi.org/10.1002/acn3.51679, doi:10.1002/acn3.51679. This article has 9 citations and is from a peer-reviewed journal.

3. (lebigot2021areviewof pages 4-5): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

4. (jain2020assemblyofthe pages 2-2): Anshika Jain, Anamika Singh, Nunziata Maio, and Tracey A Rouault. Assembly of the [4fe–4s] cluster of nfu1 requires the coordinated donation of two [2fe–2s] clusters from the scaffold proteins, iscu2 and isca1. Human Molecular Genetics, 29(19):3165-3182, Aug 2020. URL: https://doi.org/10.1093/hmg/ddaa172, doi:10.1093/hmg/ddaa172. This article has 27 citations and is from a domain leading peer-reviewed journal.

5. (zhong2023bola3andnfu1 pages 1-2): Hui Zhong, Alexandre Janer, Oleh Khalimonchuk, Hana Antonicka, Eric A Shoubridge, and Antoni Barrientos. Bola3 and nfu1 link mitoribosome iron–sulfur cluster assembly to multiple mitochondrial dysfunctions syndrome. Oct 2023. URL: https://doi.org/10.1093/nar/gkad842, doi:10.1093/nar/gkad842. This article has 39 citations and is from a highest quality peer-reviewed journal.

6. (ahting2015clinicalbiochemicaland pages 5-6): Uwe Ahting, Johannes A. Mayr, Arnaud V. Vanlander, Steven A. Hardy, Saikat Santra, Christine Makowski, Charlotte L. Alston, Franz A. Zimmermann, Lucia Abela, Barbara Plecko, Marianne Rohrbach, Stephanie Spranger, Sara Seneca, Boris Rolinski, Angela Hagendorff, Maja Hempel, Wolfgang Sperl, Thomas Meitinger, Joél Smet, Robert W. Taylor, Rudy Van Coster, Peter Freisinger, Holger Prokisch, and Tobias B. Haack. Clinical, biochemical, and genetic spectrum of seven patients with nfu1 deficiency. Frontiers in Genetics, Apr 2015. URL: https://doi.org/10.3389/fgene.2015.00123, doi:10.3389/fgene.2015.00123. This article has 116 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: Multiple mitochondrial dysfunctions syndrome 1-NFU1): Open Targets Query (Multiple mitochondrial dysfunctions syndrome 1-NFU1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (lebigot2021areviewof pages 2-4): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

9. (alfadhel2017mitochondrialironsulfurcluster pages 6-6): Majid Alfadhel, Marwan Nashabat, Qais Abu Ali, and Khalid Hundallah. Mitochondrial iron-sulfur cluster biogenesis from molecular understanding to clinical disease. Neurosciences, 22:4-13, Jan 2017. URL: https://doi.org/10.17712/nsj.2017.1.20160542, doi:10.17712/nsj.2017.1.20160542. This article has 33 citations and is from a peer-reviewed journal.

10. (lebigot2021areviewof pages 6-7): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

11. (niihori2020ratswitha pages 1-5): Maki Niihori, Cody A. Eccles, Sergey Kurdyukov, Marina Zemskova, Mathews Valuparampil Varghese, Anna A. Stepanova, Alexander Galkin, Ruslan Rafikov, and Olga Rafikova. Rats with a human mutation of nfu1 develop pulmonary hypertension. Feb 2020. URL: https://doi.org/10.1165/rcmb.2019-0065oc, doi:10.1165/rcmb.2019-0065oc. This article has 49 citations and is from a peer-reviewed journal.

12. (kropp2023patientspecificvariantsof pages 11-11): Peter A. Kropp, Philippa Rogers, Sydney E. Kelly, Rebecca McWhirter, Willow D. Goff, Ian M. Levitan, David M. Miller, and Andy Golden. Patient-specific variants of nfu1/nfu-1 disrupt cholinergic signaling in a model of multiple mitochondrial dysfunctions syndrome 1. Feb 2023. URL: https://doi.org/10.1242/dmm.049594, doi:10.1242/dmm.049594. This article has 1 citations and is from a domain leading peer-reviewed journal.

13. (kropp2023patientspecificvariantsof pages 1-2): Peter A. Kropp, Philippa Rogers, Sydney E. Kelly, Rebecca McWhirter, Willow D. Goff, Ian M. Levitan, David M. Miller, and Andy Golden. Patient-specific variants of nfu1/nfu-1 disrupt cholinergic signaling in a model of multiple mitochondrial dysfunctions syndrome 1. Feb 2023. URL: https://doi.org/10.1242/dmm.049594, doi:10.1242/dmm.049594. This article has 1 citations and is from a domain leading peer-reviewed journal.

14. (kropp2021allelespecificmitochondrialstress pages 1-2): Peter A. Kropp, Jing Wu, Michael Reidy, Sanjay Shrestha, Kyle Rhodehouse, Philippa Rogers, Michael N. Sack, and Andy Golden. Allele-specific mitochondrial stress induced by multiple mitochondrial dysfunctions syndrome 1 pathogenic mutations modeled in caenorhabditis elegans. Aug 2021. URL: https://doi.org/10.1371/journal.pgen.1009771, doi:10.1371/journal.pgen.1009771. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (kropp2021allelespecificmitochondrialstress pages 2-4): Peter A. Kropp, Jing Wu, Michael Reidy, Sanjay Shrestha, Kyle Rhodehouse, Philippa Rogers, Michael N. Sack, and Andy Golden. Allele-specific mitochondrial stress induced by multiple mitochondrial dysfunctions syndrome 1 pathogenic mutations modeled in caenorhabditis elegans. Aug 2021. URL: https://doi.org/10.1371/journal.pgen.1009771, doi:10.1371/journal.pgen.1009771. This article has 12 citations and is from a domain leading peer-reviewed journal.

16. (kropp2021allelespecificmitochondrialstress pages 11-12): Peter A. Kropp, Jing Wu, Michael Reidy, Sanjay Shrestha, Kyle Rhodehouse, Philippa Rogers, Michael N. Sack, and Andy Golden. Allele-specific mitochondrial stress induced by multiple mitochondrial dysfunctions syndrome 1 pathogenic mutations modeled in caenorhabditis elegans. Aug 2021. URL: https://doi.org/10.1371/journal.pgen.1009771, doi:10.1371/journal.pgen.1009771. This article has 12 citations and is from a domain leading peer-reviewed journal.

17. (kropp2021allelespecificmitochondrialstress pages 29-30): Peter A. Kropp, Jing Wu, Michael Reidy, Sanjay Shrestha, Kyle Rhodehouse, Philippa Rogers, Michael N. Sack, and Andy Golden. Allele-specific mitochondrial stress induced by multiple mitochondrial dysfunctions syndrome 1 pathogenic mutations modeled in caenorhabditis elegans. Aug 2021. URL: https://doi.org/10.1371/journal.pgen.1009771, doi:10.1371/journal.pgen.1009771. This article has 12 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Multiple_Mitochondrial_Dysfunctions_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011582` (4 mentions) - the report calls it "if available"; MONDO calls it **multiple mitochondrial dysfunctions syndrome 1**
- `HP:0001252` (1 mention) - the report calls it "Common in clinical series"; HP calls it **Hypotonia**
- `HP:0002154` (1 mention) - the report calls it "Glycine elevated in 7/7 in Ahting et al"; HP calls it **Hyperglycinemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016226` (1 mention) - the report calls it "GO biological process:** iron–sulfur cluster assembly"; GO calls it **iron-sulfur cluster assembly**
- `GO:0005759` (1 mention) - the report calls it "GO cellular component:** mitochondrial matrix"; GO calls it **mitochondrial matrix**