---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T17:36:16.590465'
end_time: '2026-09-16T17:45:40.528442'
duration_seconds: 563.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Periodontal Ehlers-Danlos Syndrome
  mondo_id: MONDO:0007527
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 32
  not_found: 1
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.029
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007527
    reported_labels:
    - if available
    ontology_label: Ehlers-Danlos syndrome, periodontitis type
  unresolved_terms:
  - HP:0001490
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Periodontal_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Periodontal Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007527 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Periodontal Ehlers-Danlos Syndrome** covering all of the
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
- **Disease Name:** Periodontal Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007527 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Periodontal Ehlers-Danlos Syndrome** covering all of the
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


# Periodontal Ehlers–Danlos Syndrome: Disease-Characteristics Report

## Executive summary

Periodontal Ehlers–Danlos syndrome (pEDS) is an ultra-rare, autosomal-dominant connective-tissue disorder caused by heterozygous pathogenic variants in **C1R** or **C1S**. Its defining manifestations are generalized absence of attached gingiva from childhood and severe, rapidly progressive periodontitis, often followed by premature tooth loss. Easy bruising, pretibial hemosiderotic plaques, skin fragility, distal joint hypermobility, hoarseness, vascular abnormalities, and usually asymptomatic cerebral white-matter disease may accompany the oral phenotype. Unlike most EDS subtypes, pEDS arises from dysregulated complement serine proteases rather than a primary collagen-gene defect. Functional evidence now indicates both constitutive complement activation and direct degradation of type-I collagen by activated C1s. No disease-modifying therapy or pEDS-specific interventional trial has been established; early molecular diagnosis, meticulous lifelong periodontal care, and complication-directed surveillance are current practice.

The strongest quantitative findings are summarized below.

| Domain | Key finding/statistic | Evidence type and year |
|---|---|---|
| Clinical phenotype | Among 93 mutation-positive individuals: early-onset periodontitis 99%, gingival recession 98%, absent/thin attached gingiva 93%, easy bruising 96%, skin fragility 83%, pretibial hyperpigmentation 83%, and joint hypermobility 44%; first tooth loss occurred at ages 2–30 years and complete tooth loss at 14–48 years. | International human cohort, 2016 |
| Pediatric phenotype | All 12 children who inherited the familial pathogenic variant had generalized absence of attached gingiva; all 7 non-carriers lacked it. Easy bruising occurred in 8/12 carriers and 0/7 non-carriers; only 2/12 carriers met full clinical criteria at ages 8 and 13. | Prospective family study, 2021 |
| Adult systemic phenotype | In 21 molecularly confirmed adults from 12 families: easy bruising 90%, pretibial plaques 81%, skin fragility 71%, vocal changes 38%, joint hypermobility 24%, and leukodystrophy in 89% of those imaged; molecular diagnosis occurred at ages 21–73 years. | Multicenter human cohort, 2023 |
| Complement mechanism | Functional analysis of 16 C1R variants showed abnormal intracellular processing, failure to integrate into the C1 complex, extracellular catalytic C1r/C1s activity, activated C1s in patient-fibroblast supernatants, and cleavage of added C4 without microbial stimulation. | Patient fibroblast and transfected-cell experiments, 2019 |
| Molecular profiling | RNA sequencing of monocytes and gingival fibroblasts from two patients found differential expression only in monocytes, enriched for neutrophil-mediated immunity, bacterial response, TNF-α and IL-17 pathways; MMP9, VEGFA, IL10, IL1A, IL1B, IL2RA and IL6 findings were validated by qPCR/ELISA. | Exploratory human transcriptomics, 2022 |
| Extracellular-matrix injury | Activated C1s directly degraded collagen I in cell culture and in vitro; patient fibroblasts showed rapid, extensive collagen remodeling, and activated C1s completely degraded collagen I at 40°C. | Patient-fibroblast and biochemical experiments, 2023 |


*Table: Compact synthesis of the principal clinical, pediatric, molecular and mechanistic evidence for periodontal Ehlers-Danlos syndrome. Sources: (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2, angwin2023nonoralmanifestationsin pages 1-2, grobner2019c1rmutationstrigger pages 1-2, liao2022transcriptomeanalysisof pages 1-2, amberger2023degradationofcollagen pages 1-2)*

## 1. Disease information

### Definition and classification

pEDS is a Mendelian EDS subtype characterized by early severe periodontitis, lack of attached gingiva, and systemic connective-tissue fragility. It was formerly designated **Ehlers–Danlos syndrome type VIII**, **EDS VIII**, or **periodontitis-type EDS**. The discovery study described it as an autosomal-dominant disorder involving periodontal inflammation, premature tooth loss, joint laxity, and generally mild cutaneous abnormalities (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2).

**Identifiers**

- **MONDO:** MONDO:0007527, “Ehlers-Danlos syndrome, periodontitis type.” Open Targets maps this disease to C1R and C1S (OpenTargets Search: periodontal Ehlers-Danlos syndrome-C1R,C1S).
- **OMIM phenotype entries:** **130080** and **617174**, commonly corresponding to C1R- and C1S-associated periodontal EDS, respectively (amberger2023degradationofcollagen pages 1-2, grobner2019c1rmutationstrigger pages 1-2).
- **Gene OMIM entries:** **C1R, MIM 613785**; **C1S, MIM 120580** (liao2022transcriptomeanalysisof pages 1-2, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
- **ICD:** No specific ICD-10 code was established in the retrieved literature; it is ordinarily classified under Ehlers–Danlos syndrome/other specified congenital connective-tissue disorders. A dedicated ICD-11 entity was not verified.
- **MeSH:** No pEDS-specific MeSH heading was verified; indexing generally uses *Ehlers-Danlos Syndrome* and *Periodontitis*.

The evidence summarized here is **aggregated disease-level evidence** from published cohorts, family studies, and experimental work—not individual EHR-derived data. The principal discovery cohort included 19 families/107 examined individuals, with a molecular cause identified in 17 families and 93 mutation-positive individuals (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2).

## 2. Etiology, risk, protection, and environment

### Primary cause

The cause is a **germline heterozygous pathogenic variant in C1R or C1S**, usually a missense change or in-frame insertion/deletion affecting the complement C1 proteases. Fifteen of 17 molecularly solved families in the original series had C1R variants and two had C1S variants (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2).

The molecular effect is better described as **gain of abnormal proteolytic function or loss of physiological control**, rather than simple haploinsufficiency. Heterozygous loss-of-function alleles are reportedly asymptomatic, whereas pEDS alleles cause abnormal processing, activation, and extracellular protease activity (grobner2019c1rmutationstrigger pages 1-2).

### Risk factors

- **Genetic:** An affected parent or known familial C1R/C1S pathogenic variant is the principal risk factor. Each child of a heterozygous affected person has a theoretical 50% transmission risk.
- **Family history:** A clinically affected first-degree relative is a major diagnostic criterion (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
- **Dental plaque/biofilm:** Biofilm is not the primary cause, but it is an important downstream inflammatory trigger. Constitutively activated complement is hypothesized to produce disproportionate gingival inflammation after mild plaque accumulation (liao2022transcriptomeanalysisof pages 1-2, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
- **Age:** Absence of attached gingiva is congenital or evident in childhood, while destructive periodontal disease is age-dependent and usually begins during childhood or adolescence (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
- **Temperature:** Activated C1s completely degraded collagen I at 40°C in vitro. This is mechanistically interesting but does **not** establish fever, climate, or occupational heat as a clinical risk factor (amberger2023degradationofcollagen pages 1-2).

No reproducible sex, ethnic, dietary, smoking, toxicant, occupational, or infectious-agent susceptibility factor specific to pEDS has been demonstrated. Ordinary periodontal exposures, especially smoking and poor oral hygiene, should still be avoided because they plausibly add to an already highly susceptible periodontium, but pEDS-specific effect sizes are unavailable.

### Protective factors and gene–environment interactions

No protective C1R/C1S alleles, modifier genes, or validated pharmacologic protective factors are known. The pediatric investigators concluded that early recognition may permit better dental hygiene and potentially prevent or delay early tooth loss, but controlled prevention data are absent (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2). The best-supported gene–environment model is therefore:

**C1R/C1S pathogenic variant → constitutive local protease/complement activity → exaggerated response to otherwise modest oral biofilm → accelerated periodontal inflammation and tissue destruction.**

## 3. Phenotypes

### Oral and dental manifestations

- **Generalized lack of attached gingiva** — clinical sign; **HP:0000169 Gingival abnormality** is a broad suggested term, supplemented by a proposed specific annotation “absence of attached gingiva.” It is present from childhood and appears highly penetrant. In a prospective study, all 12 variant-positive children had the finding and all seven non-carriers lacked it (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
- **Early-onset severe periodontitis** — clinical sign; suggested **HP:0000704 Periodontitis** and **HP:0006308 Premature loss of teeth**. In the original mutation-positive cohort, periodontitis occurred in 99%; median diagnosis or first periodontal tooth loss was 14 years, range 2–35 years. First tooth loss occurred at 2–30 years and complete tooth loss at 14–48 years; 16% had prepubertal disease before age ten (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, wu2022periodontaldiseaseassociated pages 15-19, kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Gingival recession/thin fragile gingiva** — clinical sign; suggested **HP:0000169 Gingival abnormality**. Gingival recession occurred in 98%, and thin or absent attached gingiva in 93% (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5).
- **Alveolar-bone and periodontal-support loss** — progressive radiographic/clinical sign; suggested **HP:0000704 Periodontitis**. The affected unit includes gingiva, periodontal ligament, root cementum, and alveolar bone (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).

These oral manifestations impair chewing, speech, appearance, self-confidence, and maintenance of natural dentition. No pEDS-specific EQ-5D, SF-36, PROMIS, or validated oral-health quality-of-life dataset was identified.

### Cutaneous, musculoskeletal, vascular, and other manifestations

Suggested HPO annotations include:

- **Easy bruising — HP:0000978:** 96% in the original cohort and 90% in a 2023 adult cohort; often present in childhood (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Pretibial hyperpigmentation/hemosiderotic plaques — HP:0001045 Vitiligo is not appropriate; use HP:0001000 Abnormality of skin pigmentation plus a disease-specific descriptor:** 83% in the original series and 81% in the 2023 adults (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Skin fragility — HP:0001030 Fragile skin:** 83% originally and 71% in the recent adult cohort (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Mild skin hyperextensibility — HP:0000974:** 73%; abnormal scarring and prominent vasculature each occurred in approximately 50% (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Joint hypermobility — HP:0001382**, often distal and mild: 44% in the original cohort but 24% in the 2023 adult cohort, demonstrating ascertainment and age/cohort variability (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Hoarse/vocally altered voice — HP:0001609 Hoarse voice:** 38% in the 2023 cohort (angwin2023nonoralmanifestationsin pages 1-2).
- **Leukoencephalopathy/white-matter abnormalities — HP:0002352 Leukoencephalopathy:** found in 89% of imaged adults in the 2023 series. The denominator was only those imaged, and many lesions appear clinically silent; it should not be interpreted as 89% population prevalence (angwin2023nonoralmanifestationsin pages 1-2).
- **Recurrent infection — HP:0002719:** approximately 40% in the original cohort (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).
- **Aneurysm — HP:0002617:** approximately 16%; arterial dissection and rare vessel or organ rupture have also been reported (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6, amberger2023degradationofcollagen pages 1-2).
- **Hernia — HP:0000776**, **acrogeria — HP:0001490**, marfanoid facial appearance, poor wound healing, and rare gastrointestinal rupture are recognized but incompletely quantified (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2, angwin2023nonoralmanifestationsin pages 1-2).

## 4. Genetic and molecular information

### Causal genes

- **C1R** — complement C1r; Ensembl **ENSG00000159403**; MIM **613785**.
- **C1S** — complement C1s; Ensembl **ENSG00000182326**; MIM **120580**.

Open Targets records five C1R and four C1S disease-association evidence items for MONDO:0007527, including PubMed-linked evidence **PMID 27745832** for the 2016 gene-discovery paper (published October 2016; DOI [10.1016/j.ajhg.2016.08.019](https://doi.org/10.1016/j.ajhg.2016.08.019)) (OpenTargets Search: periodontal Ehlers-Danlos syndrome-C1R,C1S).

### Pathogenic variants and consequences

Reported examples include **C1R p.Val50Asp, p.Cys309Trp, p.Cys371Trp**, **C1R c.1339T>C, p.(Cys447Arg)**, and **C1S p.Cys294Arg and p.Val316del** (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, angwin2023nonoralmanifestationsin pages 4-5, bally2019twodifferentmissense pages 1-2). Variant classes are predominantly missense and in-frame deletions/insertions; truncating haploinsufficient alleles are not the characteristic cause.

Variants cluster in or affect CUB and CCP/Sushi domains, subunit interfaces, interdomain hinges, disulfide-forming cysteines, or C1q-binding regions. Functional consequences include local misfolding, abnormal intracellular cleavage, retention or aggregation, failure to integrate normally into the C1 complex, and release of catalytically active fragments (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, grobner2019c1rmutationstrigger pages 1-2, bally2019twodifferentmissense pages 1-2).

For **C1S p.Val316del and p.Cys294Arg**, both variants produced an identical approximately 40-kDa **Fg40** fragment generated by cleavage between Lys353 and Cys354. The fragment retained the serine-protease domain but lacked the N-terminal C1-interaction region, allowing activity to escape normal regulation; it retained esterolytic and HMGB1-cleaving activity but had impaired canonical C4 cleavage (bally2019twodifferentmissense pages 1-2).

All reported disease variants are germline. The 2019 C1S study noted that pathogenic C1S variants were family-specific and absent from ExAC/gnomAD at that time (bally2019twodifferentmissense pages 1-2). Current per-variant gnomAD frequencies and ACMG classifications should be retrieved directly at curation time because databases are updated continuously. No validated modifier gene, protective allele, disease-specific epigenetic signature, recurrent chromosomal abnormality, somatic mechanism, or genetic anticipation is established.

## 5. Environmental, lifestyle, and infectious information

pEDS is not environmentally caused and is not infectious. Oral dysbiotic plaque bacteria act as local inflammatory stimuli, as in conventional periodontitis, but abnormal host complement/protease regulation makes the response unusually destructive. No specific bacterium, virus, fungus, toxin, pollutant, radiation exposure, diet, alcohol exposure, or occupation has been shown to cause pEDS (liao2022transcriptomeanalysisof pages 1-2, grobner2019c1rmutationstrigger pages 1-2).

Meticulous plaque control, avoidance of smoking, and routine periodontal maintenance are biologically reasonable risk-reduction measures. Their pEDS-specific efficacy has not been quantified in randomized studies.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous pEDS-associated C1R or C1S variant leads to** abnormal folding, intracellular processing, cleavage, secretion, or assembly of C1r/C1s.
2. **Abnormal processing leads to** intracellular activation of C1r and/or C1s and extracellular release of activated C1s or active proteolytic fragments, often outside the normal C1 complex (demonstrated in transfected cells and patient fibroblasts) (grobner2019c1rmutationstrigger pages 1-2, bally2019twodifferentmissense pages 1-2).
3. **Extracellular activated C1s leads to two mechanistic branches:**
   - **Branch A—immune:** cleavage of complement substrates, including C4 in C1R-variant fibroblast experiments, **leads to** local classical-complement activation without a microbial trigger (demonstrated) (grobner2019c1rmutationstrigger pages 1-2).
   - **Branch B—matrix:** direct cleavage of type-I collagen and potentially decorin, HMGB1, and MMP9-related substrates **leads to** accelerated extracellular-matrix turnover (collagen-I cleavage demonstrated; broader substrate contribution partly inferred) (amberger2023degradationofcollagen pages 1-2, bally2019twodifferentmissense pages 1-2).
4. **Complement dysregulation plus dental biofilm leads to** exaggerated gingival innate inflammation, with monocyte/neutrophil, TNF-α, IL-17, and bacterial-response programs implicated (transcriptomic association; causality not yet proven) (liao2022transcriptomeanalysisof pages 1-2).
5. **Inflammation and matrix proteolysis lead to** loss of stable collagen organization in attached gingiva, periodontal ligament, skin, and vascular connective tissues (partly demonstrated in fibroblasts and ultrastructure; tissue-level extrapolation remains inferential) (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6, amberger2023degradationofcollagen pages 1-2).
6. **Fragile gingiva and progressive destruction of periodontal ligament and alveolar bone lead to** recession, periodontal pockets, tooth mobility, and premature tooth loss (human clinical evidence) (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).
7. **Systemic connective-tissue injury leads to** easy bruising, pretibial plaques, skin fragility, abnormal scarring, mild hypermobility, vocal changes, vascular complications, and possibly white-matter abnormalities; the precise mechanism for several non-oral features remains unresolved (angwin2023nonoralmanifestationsin pages 1-2).

### Cellular and molecular detail

Functional analysis of 16 C1R variants showed that none integrated normally into C1 in the overexpression system. Patient fibroblast supernatants contained activated C1s and cleaved added C4, whereas control fibroblasts secreted pro-C1s without increased C4 activation (grobner2019c1rmutationstrigger pages 1-2). This supports **constitutive complement initiation**, not complement deficiency.

The 2023 collagen study found rapid, extensive remodeling of collagen in patient fibroblasts and direct collagen-I degradation by activated C1s. The authors’ central conclusion was that pEDS is “not solely mediated by activation of the complement cascade” but also by inappropriate C1s-mediated matrix degradation (amberger2023degradationofcollagen pages 1-2).

Electron microscopy in human tissues showed reduced collagen content, variable fibril diameters, and abnormal fibril shapes. Conventional fibroblast assays did not consistently demonstrate impaired synthesis or secretion of collagens I, III, or V, supporting excessive turnover rather than defective collagen biosynthesis as the primary lesion (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).

### Molecular profiling

RNA sequencing of monocytes and gingival fibroblasts from **two patients** found differential expression only in monocytes. Enrichment involved neutrophil-mediated immunity, response to bacteria, TNF-α and IL-17 pathways; **MMP9, VEGFA, IL10, IL1A, IL1B, IL2RA, and IL6** were validated by qPCR and ELISA. The authors described this as the first pEDS transcriptomic dataset, but the sample was too small for diagnostic or prognostic use (liao2022transcriptomeanalysisof pages 1-2).

No replicated proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, multi-omics, CRISPR-screen, or organoid study specific to pEDS was identified.

**Suggested GO biological processes:** classical complement activation (GO:0006958), complement activation (GO:0006956), proteolysis (GO:0006508), collagen catabolic process (GO:0030574), extracellular-matrix organization (GO:0030198), inflammatory response (GO:0006954), neutrophil-mediated immunity (GO:0002446), and response to bacterium (GO:0009617).

**Suggested cell types:** fibroblast (**CL:0000057**), monocyte (**CL:0000576**), neutrophil (**CL:0000775**), gingival epithelial cell, periodontal-ligament fibroblast, osteoblast (**CL:0000062**), and osteoclast (**CL:0000092**). Direct pEDS evidence is strongest for fibroblasts and circulating monocytes.

## 7. Anatomical structures affected

The primary organ system is the **oral cavity/periodontium**:

- gingiva and attached gingiva;
- alveolar mucosa;
- periodontal ligament;
- alveolar bone;
- root cementum;
- teeth secondarily lost through periodontal-support failure.

Suggested UBERON annotations include **gingiva (UBERON:0001828)**, oral cavity, tooth, periodontal ligament, cementum, and alveolar bone. The attached gingiva is keratinized tissue tethered to periosteum by type-I collagen; periodontitis progressively damages gingival attachment, periodontal ligament, cementum, and alveolar bone (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).

Secondary sites include dermis and subcutaneous tissues, pretibial skin, joints/ligaments, blood-vessel walls, laryngeal/vocal tissues, and cerebral white matter. Disease is generalized rather than lateralized.

At the subcellular level, implicated compartments include the rough endoplasmic reticulum/secretory pathway, extracellular space, complement C1 complex, and collagen-rich extracellular matrix. Suggested GO cellular components are endoplasmic-reticulum lumen (GO:0005788), extracellular region (GO:0005576), collagen-containing extracellular matrix (GO:0062023), and C1 complex (GO:0005602).

## 8. Temporal development

The disease is lifelong and genetically present from conception. Generalized absence of attached gingiva can be identified in childhood before destructive periodontal disease develops. Only two of 12 variant-positive children, aged 8 and 13, met full 2017 clinical criteria, demonstrating age-dependent ascertainment and the limitations of adult-oriented criteria in children (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).

A practical course is:

1. **Early/presymptomatic stage:** absent attached gingiva, thin fragile gums, easy bruising.
2. **Childhood/adolescent stage:** plaque-sensitive gingivitis, gingival recession, early attachment and alveolar-bone loss.
3. **Progressive stage:** rapidly destructive generalized periodontitis, tooth mobility, recurrent periodontal treatment.
4. **Advanced stage:** partial or complete premature tooth loss; implants or prosthetic rehabilitation may be considered but are challenging.
5. **Systemic adult stage:** cumulative bruising/pretibial plaques, skin fragility, vocal changes, vascular abnormalities, and detectable white-matter lesions in some patients.

Spontaneous remission has not been established. Periodontal inflammation may be controlled, but lost attachment and bone do not spontaneously regenerate. Childhood is the most important intervention window because attached-gingiva abnormalities precede tooth loss.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Penetrance appeared 100% among identified individuals in the 2019 functional-study summary, although ascertainment bias and age-dependent manifestations should be considered (grobner2019c1rmutationstrigger pages 1-2). Expressivity is variable, particularly for joint, skin, vascular, neurologic, and vocal manifestations.

Prevalence and incidence are unknown. More than 100 patients had been described by 2022, but this is a case count rather than population prevalence (wu2022periodontaldiseaseassociated pages 15-19). No reliable incidence per 100,000, carrier frequency, founder effect, ethnic enrichment, geographic gradient, or sex difference has been established. The 2023 adult cohort’s 5:16 male:female ratio is too small and referral-selected to establish sex bias (angwin2023nonoralmanifestationsin pages 1-2).

Variants are commonly private to individual families; no recurrent C1S founder allele was evident in the 2019 study (bally2019twodifferentmissense pages 1-2). De novo occurrence is possible for any dominant disorder, but its pEDS proportion and germline-mosaicism risk are not quantified. Consanguinity is not etiologically relevant to the usual dominant form.

## 10. Diagnostics

### Clinical criteria

The 2017 classification lists four major criteria:

1. severe, intractable periodontitis of early onset in childhood or adolescence;
2. lack of attached gingiva;
3. pretibial plaques;
4. an affected first-degree relative meeting clinical criteria.

Minor criteria include easy bruising, mainly distal joint hypermobility, skin hyperextensibility/fragility or abnormal scars, recurrent infections, hernias, marfanoid facial features, acrogeria, and prominent vasculature. The original formulation used three major plus one minor criterion; later clinical summaries emphasize that major criterion 1 or 2 plus additional major/minor findings should prompt mandatory molecular confirmation (angwin2023nonoralmanifestationsin pages 1-2, kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).

### Recommended work-up

1. **Periodontal examination:** gingival phenotype, recession, probing depths, clinical-attachment loss, bleeding/inflammation, tooth mobility, and plaque burden.
2. **Dental imaging:** panoramic and intraoral radiographs to quantify alveolar-bone loss. Early-onset periodontitis in the discovery study was operationalized in selected families as at least four interproximal sites with attachment loss ≥6 mm and probing depth ≥5 mm, or complete mobility-related tooth loss by age 35 (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2).
3. **Clinical genetics examination:** skin, scars, bruising, pretibial plaques, distal joints, hernias, vascular history, voice, and family pedigree.
4. **Molecular testing:** sequencing and deletion/duplication analysis of **C1R and C1S**, preferably within a validated EDS/aggressive-periodontitis panel. A known familial variant can be tested directly.
5. **Broader sequencing:** EDS/connective-tissue panels or WES/WGS are useful when phenotype is atypical or first-line testing is negative. WES/WGS is not superior to targeted testing for a clearly affected family unless structural, deep-intronic, or alternative diagnoses are suspected.
6. **CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing:** not routine because pEDS is a sequence-variant disorder, not a characteristic chromosomal, mitochondrial, or repeat-expansion condition.

There is no validated blood complement level, enzyme assay, collagen biomarker, RNA signature, or biopsy criterion that replaces molecular confirmation. Routine complement assays may be normal; one family showed no consistent systemic classical-pathway abnormality (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6).

### Differential diagnosis

Important differentials include:

- other EDS subtypes, especially classical and vascular EDS—distinguished by their causal genes and absence of the characteristic generalized attached-gingiva defect;
- hypermobile EDS—lacks a known monogenic marker and does not characteristically cause destructive childhood periodontitis;
- Papillon–Lefèvre syndrome (**CTSC**, autosomal recessive), with palmoplantar keratoderma and severe periodontitis;
- leukocyte-adhesion deficiency, cyclic/severe congenital neutropenia, and other immunodeficiencies with infection-associated periodontitis;
- hypophosphatasia (**ALPL**), characterized by premature tooth loss with mineralization abnormalities;
- acatalasemia/Takahara disease;
- isolated familial aggressive periodontitis;
- vascular connective-tissue disorders such as Loeys–Dietz or Marfan syndrome when vascular/marfanoid findings dominate.

### Screening

Population or newborn screening is not indicated. **Cascade testing** of first-degree relatives is appropriate once a familial pathogenic variant is known. At-risk children should receive early gingival examination and molecular testing because absence of attached gingiva may precede other criteria.

## 11. Outcome and prognosis

No robust survival curves, disease-specific mortality rate, or reduction in life expectancy have been published. Most morbidity arises from severe periodontal destruction, premature tooth loss, prosthetic burden, bruising, skin fragility, and occasional vascular or organ complications. Rare arterial aneurysm/dissection or rupture could be life-threatening, but absolute risk is uncertain (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6, amberger2023degradationofcollagen pages 1-2).

Natural teeth may be lost beginning in early childhood, and complete tooth loss has been reported from adolescence through middle adulthood. Prognosis is variable and likely improved by early diagnosis and intensive periodontal maintenance, although treatment-response percentages are unavailable (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5, wu2022periodontaldiseaseassociated pages 15-19).

Potential prognostic indicators are early alveolar-bone loss, uncontrolled plaque inflammation, rapid attachment loss, and prior vascular events. No validated molecular prognostic biomarker or genotype–phenotype calculator exists. The quality-of-life burden has not been quantified with pEDS-specific instruments.

## 12. Treatment and real-world implementation

There is no approved therapy that corrects C1R/C1S dysregulation. Current management is preventive and supportive:

- **Periodontal care:** early referral to a periodontist; meticulous home plaque control; frequent professional cleaning and periodontal reassessment; prompt treatment of gingivitis and periodontal pockets; preservation of natural teeth where feasible.
- **Dental rehabilitation:** restorative dentistry, removable or fixed prostheses, and carefully selected implant therapy. Published clinical experience indicates high peri-implant disease/failure risk, so implants require conservative selection and intensive maintenance (sollazzo2022olliersdisease pages 40-45).
- **Antimicrobials:** antiseptics or antibiotics may be used for conventional periodontal indications, not as chronic disease-specific therapy. No pEDS response rate is established.
- **Surgery/procedures:** use atraumatic technique, careful hemostasis and suturing, and anticipate friable gingiva, bruising, and impaired wound healing.
- **Musculoskeletal/supportive care:** individualized physiotherapy, joint protection, pain management, and occupational therapy when symptomatic.
- **Vascular care:** baseline specialist assessment and individualized noninvasive surveillance may be considered when there is a personal/family vascular history; evidence does not support a universal pEDS imaging interval.
- **Voice/neurologic care:** ENT evaluation for persistent hoarseness and neurologic assessment when symptoms accompany white-matter imaging abnormalities.

Suggested NCIT intervention annotations include **Genetic Counseling**, **Genetic Testing**, **Dental Examination**, **Periodontal Therapy**, **Dental Prophylaxis**, **Antibiotic Therapy**, **Physical Therapy**, and **Surgical Procedure**. Exact NCIT concept identifiers should be verified against the current terminology release.

Complement inhibitors, C1r/C1s inhibitors, MMP-directed therapy, and matrix-protective approaches are mechanistically attractive but remain experimental. The search identified no pEDS-specific interventional ClinicalTrials.gov study, gene therapy, RNA therapy, cell therapy, CRISPR therapy, or validated pharmacogenomic strategy.

## 13. Prevention

**Primary prevention of the genotype** is not possible after conception. Reproductive options include genetic counseling, prenatal diagnosis, and preimplantation genetic testing for a known familial pathogenic variant.

**Secondary prevention** consists of cascade testing and early oral examination of at-risk children. The prospective pediatric study’s key conclusion was: “Generalized lack of attached gingiva is a pathognomonic feature of pEDS,” and early diagnosis may permit hygiene measures before destructive periodontitis develops (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2).

**Tertiary prevention** includes meticulous plaque control, periodontal maintenance, smoking avoidance, prompt infection treatment, tooth-preservation strategies, cautious procedural planning, and surveillance tailored to vascular or other systemic manifestations. Vaccination has no disease-specific preventive role beyond standard immunization schedules.

## 14. Other species and natural disease

C1R and C1S are evolutionarily conserved complement genes with mammalian orthologs. However, no naturally occurring veterinary disorder conclusively homologous to human **C1R/C1S-associated periodontal EDS** was identified. EDS-like connective-tissue fragility occurs in domestic animals, but these conditions should not be annotated as pEDS without orthologous molecular evidence. pEDS is noninfectious and has no zoonotic or cross-species transmission potential.

## 15. Model organisms and experimental systems

The most informative pEDS systems are currently **human cellular and biochemical models**:

- primary dermal fibroblasts from genetically confirmed patients;
- patient gingival fibroblasts;
- peripheral-blood monocytes;
- HEK293T/HEK293-F cells expressing mutant C1R or C1S;
- recombinant C1s fragments and purified collagen-I proteolysis assays.

These models reproduce abnormal processing, unregulated protease activity, C4 cleavage, inflammatory transcriptional changes, and collagen turnover, but cannot capture the complete oral microbiome, periodontal biomechanics, vascular disease, or longitudinal tooth loss (liao2022transcriptomeanalysisof pages 1-2, amberger2023degradationofcollagen pages 1-2, grobner2019c1rmutationstrigger pages 1-2, bally2019twodifferentmissense pages 1-2).

A 2021 review found engineered mouse or zebrafish models for 14 of 20 EDS-associated genes overall, but the retrieved evidence did not document a validated **C1r/C1s pEDS knock-in animal model** that recapitulates absent attached gingiva and early tooth loss (vroman2021animalmodelsof pages 1-2). Development of heterozygous knock-in models carrying human gain-of-function alleles would be valuable for testing complement/protease inhibitors and gene-specific interventions.

## Evidence quality and current research gaps

The evidence base is dominated by one international discovery cohort, small multicenter phenotype cohorts, family studies, and mechanistic cell/in-vitro experiments. Recent advances are the 2022 monocyte transcriptome study, the 2023 adult systemic-phenotype series, and the 2023 demonstration that activated C1s directly degrades collagen I. Their principal abstract statements respectively report differential expression “only in monocytes,” leukodystrophy in “89% of those imaged,” and that activated C1s “degrades collagen I in cell culture and in in vitro assays” (liao2022transcriptomeanalysisof pages 1-2, angwin2023nonoralmanifestationsin pages 1-2, amberger2023degradationofcollagen pages 1-2).

Major unmet needs are population epidemiology, prospective natural-history data, validated cardiovascular and neurologic surveillance guidance, standardized treatment outcomes, quality-of-life studies, replicated multi-omics, animal models, and trials of complement- or protease-directed treatment. No retrieved 2024 primary study materially changed the established pEDS disease model; the most consequential recent mechanistic evidence remains the March 2023 collagen-I study.

References

1. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 149 citations and is from a highest quality peer-reviewed journal.

2. (kapfererseebacher2021prospectiveclinicalinvestigations pages 1-2): Ines Kapferer-Seebacher, Elizabeth Oakley-Hannibal, Ulrike Lepperdinger, Diana Johnson, Neeti Ghali, Angela F. Brady, Glenda Sobey, Johannes Zschocke, and Fleur S. van Dijk. Prospective clinical investigations of children with periodontal ehlers–danlos syndrome identify generalized lack of attached gingiva as a pathognomonic feature. Feb 2021. URL: https://doi.org/10.1038/s41436-020-00985-y, doi:10.1038/s41436-020-00985-y. This article has 38 citations and is from a highest quality peer-reviewed journal.

3. (angwin2023nonoralmanifestationsin pages 1-2): C. Angwin, J. Zschocke, T. Kammin, E. Björck, J. Bowen, A. Brady, H. Burns, C. Cummings, R. Gardner, N. Ghali, R. Gröbner, J. Harris, Michael Denis Higgins, D. Johnson, U. Lepperdinger, D. Milnes, F. Pope, R. Sehra, I. Kapferer-Seebacher, G. Sobey, and F. V. van Dijk. Non-oral manifestations in adults with a clinical and molecularly confirmed diagnosis of periodontal ehlers-danlos syndrome. Frontiers in Genetics, May 2023. URL: https://doi.org/10.3389/fgene.2023.1136339, doi:10.3389/fgene.2023.1136339. This article has 10 citations and is from a peer-reviewed journal.

4. (grobner2019c1rmutationstrigger pages 1-2): Rebekka Gröbner, Ines Kapferer-Seebacher, Albert Amberger, Rita Redolfi, Fabien Dalonneau, Erik Björck, Di Milnes, Isabelle Bally, Veronique Rossi, Nicole Thielens, Heribert Stoiber, Christine Gaboriaud, and Johannes Zschocke. C1r mutations trigger constitutive complement 1 activation in periodontal ehlers-danlos syndrome. Frontiers in Immunology, Nov 2019. URL: https://doi.org/10.3389/fimmu.2019.02537, doi:10.3389/fimmu.2019.02537. This article has 49 citations and is from a peer-reviewed journal.

5. (liao2022transcriptomeanalysisof pages 1-2): Zhuoyi Liao, Tian Zhao, Ningxiang Wang, Jiaqi Chen, Weibin Sun, and Juan Wu. Transcriptome analysis of monocytes and fibroblasts provides insights into the molecular features of periodontal ehlers-danlos syndrome. Frontiers in Genetics, Apr 2022. URL: https://doi.org/10.3389/fgene.2022.834928, doi:10.3389/fgene.2022.834928. This article has 1 citations and is from a peer-reviewed journal.

6. (amberger2023degradationofcollagen pages 1-2): Albert Amberger, Johanna Pertoll, Pia Traunfellner, Ines Kapferer-Seebacher, Heribert Stoiber, Lars Klimaschewski, Nicole Thielens, Christine Gaboriaud, and Johannes Zschocke. Degradation of collagen i by activated c1s in periodontal ehlers-danlos syndrome. Frontiers in Immunology, Mar 2023. URL: https://doi.org/10.3389/fimmu.2023.1157421, doi:10.3389/fimmu.2023.1157421. This article has 12 citations and is from a peer-reviewed journal.

7. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 149 citations and is from a highest quality peer-reviewed journal.

8. (OpenTargets Search: periodontal Ehlers-Danlos syndrome-C1R,C1S): Open Targets Query (periodontal Ehlers-Danlos syndrome-C1R,C1S, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (wu2022periodontaldiseaseassociated pages 15-19): Juan Wu, Wai Keung Leung, and Weibin Sun. Periodontal disease associated with genetic disorders. Dentistry, Feb 2022. URL: https://doi.org/10.5772/intechopen.97497, doi:10.5772/intechopen.97497. This article has 1 citations.

10. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 149 citations and is from a highest quality peer-reviewed journal.

11. (angwin2023nonoralmanifestationsin pages 4-5): C. Angwin, J. Zschocke, T. Kammin, E. Björck, J. Bowen, A. Brady, H. Burns, C. Cummings, R. Gardner, N. Ghali, R. Gröbner, J. Harris, Michael Denis Higgins, D. Johnson, U. Lepperdinger, D. Milnes, F. Pope, R. Sehra, I. Kapferer-Seebacher, G. Sobey, and F. V. van Dijk. Non-oral manifestations in adults with a clinical and molecularly confirmed diagnosis of periodontal ehlers-danlos syndrome. Frontiers in Genetics, May 2023. URL: https://doi.org/10.3389/fgene.2023.1136339, doi:10.3389/fgene.2023.1136339. This article has 10 citations and is from a peer-reviewed journal.

12. (bally2019twodifferentmissense pages 1-2): Isabelle Bally, Fabien Dalonneau, Anne Chouquet, Rebekka Gröbner, Albert Amberger, Ines Kapferer-Seebacher, Heribert Stoiber, Johannes Zschocke, Nicole M. Thielens, Véronique Rossi, and Christine Gaboriaud. Two different missense c1s mutations, associated to periodontal ehlers-danlos syndrome, lead to identical molecular outcomes. Frontiers in Immunology, Dec 2019. URL: https://doi.org/10.3389/fimmu.2019.02962, doi:10.3389/fimmu.2019.02962. This article has 23 citations and is from a peer-reviewed journal.

13. (sollazzo2022olliersdisease pages 40-45): V Sollazzo and V Sollazzo. Ollier's disease. Unknown journal, 2022.

14. (vroman2021animalmodelsof pages 1-2): Robin Vroman, Anne-Marie Malfait, Rachel E. Miller, Fransiska Malfait, and Delfien Syx. Animal models of ehlers–danlos syndromes: phenotype, pathogenesis, and translational potential. Frontiers in Genetics, Oct 2021. URL: https://doi.org/10.3389/fgene.2021.726474, doi:10.3389/fgene.2021.726474. This article has 26 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Periodontal_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007527` (3 mentions) - the report calls it "if available"; MONDO calls it **Ehlers-Danlos syndrome, periodontitis type**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001490` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`