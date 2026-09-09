---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T16:51:35.368012'
end_time: '2026-09-03T17:14:26.809185'
duration_seconds: 1371.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: lethal polymalformative syndrome Boissel type / growth retardation,
    developmental delay, coarse facies and early death (GDFD), caused by homozygous
    FTO missense variants (NOT the FTO intron-1 obesity/BMI association locus)
  mondo_id: MONDO:0013050
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 82
  verified: 80
  not_found: 2
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.024
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0013050
    reported_labels:
    - if available
    - MONDO
    ontology_label: lethal polymalformative syndrome, Boissel type
  - term_id: GO:0033123
    reported_labels:
    - RNA demethylase activity
    ontology_label: positive regulation of purine nucleotide catabolic process
  - term_id: NCIT:C159670
    reported_labels:
    - Whole Exome Sequencing
    ontology_label: Bladder Leiomyosarcoma
  - term_id: NCIT:C122421
    reported_labels:
    - Lethal
    ontology_label: Agricultural Workers
  - term_id: NCIT:C15421
    reported_labels:
    - Supportive Care
    ontology_label: Postmenopausal
  unresolved_terms:
  - HP:000252
  - HP:0000281
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Lethal_Polymalformative_Syndrome_Boissel_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** lethal polymalformative syndrome Boissel type / growth retardation, developmental delay, coarse facies and early death (GDFD), caused by homozygous FTO missense variants (NOT the FTO intron-1 obesity/BMI association locus)
- **MONDO ID:** MONDO:0013050 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **lethal polymalformative syndrome Boissel type / growth retardation, developmental delay, coarse facies and early death (GDFD), caused by homozygous FTO missense variants (NOT the FTO intron-1 obesity/BMI association locus)** covering all of the
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
- **Disease Name:** lethal polymalformative syndrome Boissel type / growth retardation, developmental delay, coarse facies and early death (GDFD), caused by homozygous FTO missense variants (NOT the FTO intron-1 obesity/BMI association locus)
- **MONDO ID:** MONDO:0013050 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **lethal polymalformative syndrome Boissel type / growth retardation, developmental delay, coarse facies and early death (GDFD), caused by homozygous FTO missense variants (NOT the FTO intron-1 obesity/BMI association locus)** covering all of the
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


# Research report: biallelic **FTO**-related lethal polymalformative syndrome (Boissel type/GDFD)

## Scope and evidence standard

This report concerns the rare Mendelian disorder caused by **biallelic coding variants in FTO**, especially homozygous missense variants that impair FTO enzymatic function. It does **not** concern the common noncoding variants in FTO intron 1 associated with BMI and obesity. The disease evidence remains sparse: the defining 2009 report described nine relatives, detailed clinical information was available for eight, and subsequent publications have mostly been single-patient reports. Frequencies below therefore describe reported cases, not stable population estimates.

| Domain | Established Finding | Quantitative Evidence | Evidence Type/Strength | Suggested Ontology Terms |
| :--- | :--- | :--- | :--- | :--- |
| **Identifiers & Nomenclature** | Lethal polymalformative syndrome, Boissel type (GDFD). *Strictly distinct from the common intron-1 GWAS obesity/BMI locus.* | 1 primary Boissel cohort, 1 Caglayan case, 1 Open Targets mapping (boissel2009lossoffunctionmutationin pages 1-2, OpenTargets Search: lethal polymalformative syndrome Boissel type-FTO, caglayan2016apatientwith pages 1-2) | High / Clinical consensus & Database aggregation | MONDO:0013050, ENSG00000140718 |
| **Inheritance** | Autosomal Recessive | 100% of reported severe cases originated from consanguineous multiplex families (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 1-2) | High / Pedigree and autozygosity mapping | HP:0000007 (Autosomal recessive inheritance) |
| **Variants** | Biallelic/homozygous coding mutations. Pathogenic: c.947G>A (p.Arg316Gln), c.812A>C (p.His271Pro) | 9 cases (R316Q), 1 case (p.His271Pro) (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 3-5) | High / Genetic segregation & functional assays | SO:0001583 (missense_variant) |
| **Phenotypes: Growth & Survival** | Early lethality, severe postnatal growth retardation, failure to thrive, intrauterine growth retardation | Death < 3y (8/8), FTT (8/8), Postnatal growth retardation (8/8), IUGR (3/7) (boissel2009lossoffunctionmutationin pages 4-5) | High / Primary clinical cohort | HP:0001522, HP:0008897, HP:0001511 |
| **Phenotypes: Neurological** | Severe developmental delay, profound ID, postnatal microcephaly, hypertonicity, seizures, lissencephaly | Microcephaly (8/8), Delay (8/8), Hypertonia (6/6), Seizures (3/8), Lissencephaly (3/8) (boissel2009lossoffunctionmutationin pages 4-5, caglayan2016apatientwith pages 3-5) | High / Primary clinical cohort | HP:0001249, HP:000252, HP:0001250, HP:0001332 |
| **Phenotypes: Craniofacial** | Coarse facies, anteverted nostrils, thin vermilion, retrognathia, prominent alveolar ridge, short neck | Coarse face (7/7), Anteverted nostrils (7/7), Thin vermilion (7/7), Retrognathia (7/7) (boissel2009lossoffunctionmutationin pages 4-5) | High / Primary clinical cohort | HP:0000280, HP:0000448, HP:0000281, HP:0000470 |
| **Phenotypes: Systemic** | Congenital heart defects (VSD/hypertrophic cardiomyopathy), brachydactyly, deafness, cutis marmorata | Heart defect (6/8), Brachydactyly (6/6), Deafness (5/5), Cutis marmorata (7/7) (boissel2009lossoffunctionmutationin pages 4-5) | High / Primary clinical cohort | HP:0001627, HP:0001156, HP:0000365, HP:0000965 |
| **Mechanism: Molecular** | Loss of 2-oxoglutarate-dependent nucleic acid demethylase activity; failure to interact with cosubstrate | R316Q enzyme inactive in vitro (0% conversion of 2-oxoglutarate) (boissel2009lossoffunctionmutationin pages 2-4) | High / Recombinant protein biochemistry | GO:0033123 (RNA demethylase activity) |
| **Mechanism: Cellular** | Accelerated cellular senescence, perturbed Wnt signalling (decreased canonical beta-catenin, increased non-canonical Ca2+) | ~41% decrease in WNT3a-stimulated luciferase in FTO-depleted cells; senescent fibroblasts (boissel2009lossoffunctionmutationin pages 5-6, osborn2014lossoffto pages 4-7) | Moderate / In vitro fibroblast and cell-line assays | GO:0090398 (cellular senescence), GO:0016055 (Wnt signaling) |
| **Mechanism: Tissues** | Ciliary structural defects (ciliopathy), neural crest migration defects | Fewer/shorter motile cilia in Fto -/- mice and fto zebrafish morphants (osborn2014lossoffto pages 4-7) | Moderate / Model organisms only (human inferred) | GO:0005929 (cilium), CL:0000042 (neural crest cell) |
| **Diagnostics** | WES/WGS required for definitive diagnosis. *NOT ESTABLISHED*: specific blood/urine biomarkers | 100% molecular diagnosis via sequencing mapping to 16q12.2 (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 3-5) | High / Clinical genetics standard | NCIT:C159670 (Whole Exome Sequencing) |
| **Prognosis** | Generally lethal in infancy/toddlerhood (intercurrent infections); rarer missense alleles may permit childhood survival with profound ID | 8/8 R316Q died 1-30 months; 1 H271P survived past 5.5 years (IQ 23) (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 3-5) | High / Clinical observation | NCIT:C122421 (Lethal) |
| **Treatment & Prevention** | *NONE ESTABLISHED*. Supportive/palliative care only. No directed screening. | 0 active clinical trials or therapeutic guidelines (caglayan2016apatientwith pages 5-6) | NA / Evidence gap | NCIT:C15421 (Supportive Care) |
| **Animal Models** | Mouse Fto -/- shows postnatal lethality and growth restriction; Zebrafish fto morphant models human craniofacial/microcephaly defects | ~50% neonatal mouse lethality; >90% morphant zebrafish microcephaly (osborn2014lossoffto pages 4-7, mcmurray2013adultonsetglobal pages 1-2) | High / Recapitulates growth and cranial phenotype | NCIT:C14251 (Mouse), NCIT:C14316 (Zebrafish) |


*Table: A compact summary of the clinical, molecular, and prognostic features of lethal polymalformative syndrome (Boissel type) derived from primary patient cohorts and functional models.*

## 1. Disease information

### Definition and nomenclature

**Lethal polymalformative syndrome, Boissel type**, also called **growth retardation, developmental delay, coarse facies, and early death (GDFD)**, is an autosomal-recessive multiple-congenital-anomaly/neurodevelopmental disorder caused by biallelic pathogenic or plausibly pathogenic coding variants in **FTO**. The defining phenotype combines severe postnatal growth failure, acquired microcephaly, profound developmental impairment, characteristic coarse craniofacial dysmorphism, variable brain and cardiac malformations, and—in the original genotype—death during infancy or early childhood.

The disease-defining paper was Boissel et al., *American Journal of Human Genetics*, published online **25 June 2009** and in print **10 July 2009**, DOI [10.1016/j.ajhg.2009.06.002](https://doi.org/10.1016/j.ajhg.2009.06.002), **PMID: 19559399**. Its abstract states: “**a R316Q mutation, inactivating FTO enzymatic activity, is responsible for an autosomal-recessive lethal syndrome**,” and concludes that FTO is essential for normal human central-nervous-system and cardiovascular development. (boissel2009lossoffunctionmutationin pages 1-2)

### Identifiers

- **MONDO:** [MONDO:0013050](https://monarchinitiative.org/disease/MONDO:0013050), lethal polymalformative syndrome, Boissel type.
- **OMIM phenotype:** **MIM 612938**, commonly indexed as growth retardation, developmental delay, coarse facies, and early death/GDFD.
- **Gene:** **FTO**, MIM **610966**; Ensembl **ENSG00000140718**; approved name “FTO alpha-ketoglutarate dependent dioxygenase.” Open Targets currently identifies one associated target—FTO—with five evidence records and an aggregate association score of approximately 0.706. (OpenTargets Search: lethal polymalformative syndrome Boissel type-FTO)
- **Orphanet:** a disease association is represented through Orphanet-derived evidence in Open Targets, but a stable ORPHA number was not recoverable from the available source and should not be assigned without direct database verification. (OpenTargets Search: lethal polymalformative syndrome Boissel type-FTO)
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or descriptor was identified. Broader coding would use congenital-malformation, developmental-disorder, or genetic-syndrome categories.

The information is **aggregated from published pedigrees and case reports**, not EHR-derived population data. Open Targets is a disease-level aggregation; the primary evidence consists of individual patients and family segregation studies.

### Essential exclusion

Common FTO intron-1 alleles such as **rs9939609** are noncoding susceptibility markers for adiposity and are biologically and clinically distinct. The Boissel disorder results from **biallelic coding lesions** with severe developmental consequences. The original authors explicitly contrasted these entities. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 4-5)

## 2. Etiology, risk, protective, and environmental factors

### Causal factor

The established cause is **germline biallelic FTO dysfunction**, inherited autosomal recessively. In the original Palestinian-Arab family, autozygosity mapping identified a 6.5-Mb interval on 16q12 with maximum LOD score **4.16**, followed by detection of homozygous **c.947G>A, p.Arg316Gln (R316Q)**. It cosegregated with disease and was absent from **730 control chromosomes**, including 378 Palestinian-Arab chromosomes. (boissel2009lossoffunctionmutationin pages 1-2)

### Genetic risk factors

- Two carrier parents confer, for each pregnancy, the standard theoretical risks of **25% affected, 50% carrier, and 25% unaffected non-carrier**.
- **Consanguinity** materially increases the chance that both parents carry the same rare allele. Both the original multiplex pedigree and the later p.His271Pro case involved consanguinity. (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 2-3)
- No validated modifier gene is known. A later patient also carried homozygous truncating **CETP p.Arg403Ter**, explaining marked HDL abnormalities and complicating attribution of some laboratory findings, but not establishing CETP as an FTO-syndrome modifier. (caglayan2016apatientwith pages 3-5, caglayan2016apatientwith pages 2-3)

### Protective and environmental factors

No protective FTO allele, environmental prevention factor, diet, exposure, infection, or lifestyle factor has been shown to prevent the congenital syndrome. Intercurrent infection was associated with some deaths, but infection is a **complication/proximate cause of death**, not the initiating etiology. No gene–environment interaction specific to GDFD has been demonstrated. Statements about exercise or diet attenuating common FTO-obesity associations must not be transferred to this recessive developmental disorder.

## 3. Phenotypes

In the original cohort, all medically documented patients had severe failure to thrive, severe developmental delay, severe postnatal microcephaly, and death before age three. The small denominators and intrafamilial ascertainment preclude population-level prevalence estimates. (boissel2009lossoffunctionmutationin pages 2-4)

### Quantitative phenotype catalogue

| Clinical domain | Finding in original cohort | Suggested HPO term |
|---|---:|---|
| Growth | Severe failure to thrive **8/8**; intrauterine growth restriction **3/7** | HP:0001508 Failure to thrive; HP:0001511 Intrauterine growth retardation |
| Neurodevelopment | Severe developmental delay **8/8** | HP:0001263 Global developmental delay; HP:0010864 Severe developmental delay |
| Head growth | Severe postnatal microcephaly **8/8** | HP:0005484 Postnatal microcephaly |
| Tone | Hypertonicity **6/6** | HP:0001276 Hypertonia |
| Brain/neurology | Hydrocephalus **4/8**; lissencephaly **3/8**; seizures **3/8**; Dandy–Walker malformation **2/8**; brain atrophy **1/8** | HP:0000238, HP:0001339, HP:0001250, HP:0001305, HP:0012444 |
| Heart | VSD/atrioventricular defect/PDA grouped in **6/8**; hypertrophic cardiomyopathy **4/8** | HP:0001627 Abnormal heart morphology; HP:0001631 Atrial septal defect; HP:0001643 Patent ductus arteriosus; HP:0001639 Hypertrophic cardiomyopathy |
| Craniofacial | Anteverted nares **7/7**; thin vermilion **7/7**; retrognathia **7/7**; coarse face **7/7**; prominent alveolar ridge **6/6**; protruding tongue **3/7** | HP:0000463, HP:0000219, HP:0000278, HP:0000280, HP:0009085, HP:0010808 |
| Neck/skin | Short neck **7/7**; cutis marmorata **7/7** | HP:0000470; HP:0000965 |
| Limbs/nails | Drumstick fingers **6/6**; brachydactyly **6/6**; toenail hypoplasia **6/6** | HP:0001217; HP:0001156; HP:0001800 |
| Sensory | Neurosensory deafness **5/5**; optic-disc abnormality **3/7** | HP:0000407; HP:0012795 |
| Other | Weak cry **4/6**; umbilical hernia **4/6**; genital anomaly **4/7**; cleft palate/bifid uvula **3/6** | HP:0001612; HP:0001537; HP:0000078; HP:0000175/HP:0000193 |
| Survival | Death before three years **8/8**, specifically at **1–30 months** | HP:0003819 Death in infancy; HP:0001522 Death in childhood |

These counts come directly from Boissel et al.’s clinical table. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)

### Spectrum expansion and functional impact

A 2016 report described a girl homozygous for **p.His271Pro** who survived to at least 5.5 years, demonstrating that “lethal” is not universal across all biallelic missense genotypes. She had neonatal respiratory distress, microcephaly, severe delay, seizures, hearing loss, dysphagia, abnormal behavior, thin corpus callosum, craniosynostosis, osteopenia, and hepatosplenomegaly. She achieved head control after 10 months, independent sitting at two years, and walking at four years; IQ at age three was **23**. A seizure-associated regression at age five caused temporary loss of assisted walking and permanent loss of acquired words. (caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 3-5, caglayan2016apatientwith pages 2-3)

A 2023 case report, “A novel biallelic FTO variant causing multisystem anomalies with severe epilepsy, widening the spectrum of FTO syndrome,” added severe epilepsy to the recognized spectrum. However, its full case data were unavailable through the present retrieval, so exact variant and phenotype values should be imported only after primary-paper verification.

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data exist. The likely impact is nevertheless profound: severe cognitive, motor, communication, feeding, sensory, seizure, and cardiac morbidity results in complete dependence on caregivers.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** FTO; chromosome **16q12.2**; nine exons spanning more than 400 kb in the transcript used by the 2016 report.
- **Protein:** 505-amino-acid Fe(II)/2-oxoglutarate-dependent dioxygenase with an N-terminal catalytic double-stranded β-helix domain and a C-terminal α-helical domain.
- **Localization:** predominantly nuclear, with context-dependent nucleocytoplasmic shuttling. R316Q and His271Pro patient fibroblasts retained nuclear localization. (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 5-6, caglayan2016apatientwith pages 3-5)

Suggested annotations include **GO:0005634 nucleus**, **GO:0003676 nucleic acid binding**, **GO:0035515 oxidative RNA demethylase activity**, **GO:0016706 oxidoreductase activity acting on paired donors with 2-oxoglutarate**, and **CHEBI:18420 magnesium-independent iron(II)**/CHEBI terms for Fe²⁺ and 2-oxoglutarate as cofactors/cosubstrate.

### Reported variants

1. **FTO c.947G>A; p.Arg316Gln (R316Q), homozygous, germline.** The residue is invariant across FTO/AlkB homologues and stabilizes 2-oxoglutarate binding. Recombinant R316Q had no detectable uncoupled 2-oxoglutarate-to-succinate activity and was inactive against 3-methylthymine-containing DNA. This constitutes strong functional loss-of-function evidence. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)
2. **FTO ENST00000471389.1:c.812A>C; ENSP00000418823.1:p.His271Pro, homozygous, germline.** Both parents were heterozygous. The variant was absent from dbSNP, NHLBI ESP, 1000 Genomes, and approximately 3,000 Yale exomes examined at publication. Protein abundance and nuclear localization were preserved, FTO RNA was slightly reduced, and fibroblast proliferation/apoptosis was not detectably abnormal. (caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 3-5)

Modern ClinVar/ACMG classifications and current gnomAD frequencies should be rechecked against the exact reference transcript before database ingestion. The original evidence strongly supports pathogenicity of R316Q; p.His271Pro is supported by rarity, homozygosity, segregation, phenotype, and catalytic-domain location but lacked a direct enzyme assay in the retrieved report.

The variants are **constitutional germline**, not somatic. No recurrent pathogenic deletion, duplication, aneuploidy, translocation, repeat expansion, or mitochondrial lesion defines this disease. No validated disease-specific DNA-methylation signature, histone abnormality, or chromatin signature has been reported.

## 5. Environmental, lifestyle, and infectious information

No toxin, radiation, pollutant, occupation, smoking, diet, alcohol exposure, or infectious agent is etiologic. Lifestyle modification is not expected to correct a congenital biallelic enzymatic defect. Recurrent/intercurrent infections warrant prevention and prompt treatment because they contributed to early mortality in the original family. (boissel2009lossoffunctionmutationin pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic FTO catalytic-domain mutation leads to** absent or reduced FTO dioxygenase activity; this is demonstrated directly for R316Q. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)
2. **Loss of FTO activity leads to** disturbed demethylation and processing/stability/translation of methylated RNA substrates; this is biologically established for FTO generally, but the exact pathogenic RNA targets in patient tissues remain unresolved. (zhang2019thernademethylase pages 1-2, gulati2013thebiologyof pages 2-4)
3. **Altered RNA regulation is inferred to lead to two interacting downstream branches:**
   - **Developmental signaling branch:** reduced canonical Wnt/β-catenin signaling and increased noncanonical Wnt/Ca²⁺ signaling through CaMKII and PKCδ.
   - **Cell-maintenance branch:** impaired stress-response/DNA-repair transcript regulation, reduced proliferation, and premature cellular senescence or apoptosis susceptibility.
   These branches are demonstrated in model organisms/cells, not directly in affected fetal tissues. (boissel2009lossoffunctionmutationin pages 5-6, zhang2019thernademethylase pages 1-2, osborn2014lossoffto pages 4-7, osborn2014lossoffto pages 1-3)
4. **Wnt imbalance leads to** abnormal neural-crest migration and defective ciliogenesis in zebrafish and mouse models. (osborn2014lossoffto pages 4-7, osborn2014lossoffto pages 3-4, osborn2014lossoffto pages 1-3)
5. **Neural-crest/ciliary and proliferative defects are inferred to lead to** craniofacial dysmorphism, microcephaly, brain malformations, hearing abnormalities, cardiac defects, renal/laterality abnormalities in models, and generalized growth failure.
6. **Neural FTO deficiency leads to** reduced IGF-1 and impaired postnatal somatic/bone growth in mice, providing a plausible route to severe human growth restriction. (gao2010thefatmass pages 1-2)
7. **Multisystem developmental failure, profound neurologic impairment, feeding vulnerability, cardiac disease, and infection susceptibility lead to** severe disability and early death in the most damaging genotypes. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)

### Direct biochemical and cellular evidence

FTO is a non-haem Fe(II)/2-oxoglutarate-dependent enzyme. R316 normally forms stabilizing interactions with the 2-oxoglutarate cosubstrate. R316Q preserved nuclear localization but abolished both measured catalytic reactions. Patient fibroblasts showed reduced proliferation, hypertrophic/vacuolated morphology, shortened lifespan, and increased senescence-associated β-galactosidase. The authors cautioned that these cellular observations came from limited patient material. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 5-6, boissel2009lossoffunctionmutationin pages 2-4)

The later p.His271Pro fibroblasts did **not** reproduce the morphology, proliferation, or apoptosis abnormalities, suggesting allelic heterogeneity or assay/context dependence. Microarray analysis found at least twofold increases in selected retinol-metabolism, renin–angiotensin, xenobiotic-metabolism, and metabolic transcripts and decreases in cell-cycle genes including **E2F2, BUB1, CDC20, and CCNB1**. These are exploratory single-patient findings, not validated biomarkers. (caglayan2016apatientwith pages 5-6)

### Wnt, cilia, and neural crest

In FTO-depleted HEK293T cells, WNT3A-stimulated reporter activity fell by approximately **41%**. In zebrafish, fto knockdown reduced canonical β-catenin signaling, activated CaMKII/PKCδ, disrupted cranial and trunk neural-crest migration, and produced short, absent, or disorganized cilia. Resulting model phenotypes included microcephaly, craniofacial cartilage loss, renal cystogenesis, and abnormal left–right patterning. Mouse knockout tissue showed fewer or shorter cilia in choroid plexus, nasopharyngeal epithelium, and renal tubular epithelium, while cochlear kinocilia appeared relatively preserved. (osborn2014lossoffto pages 4-7, osborn2014lossoffto pages 3-4, osborn2014lossoffto pages 1-3)

Suggested terms: **GO:0016055 Wnt signaling pathway**, **GO:0060070 canonical Wnt signaling pathway**, **GO:0007223 Wnt/Ca²⁺ signaling**, **GO:0060271 cilium assembly**, **GO:0007368 determination of left/right symmetry**, **GO:0001755 neural crest cell migration**; **CL:0000042 neural crest cell**, **CL:0000066 epithelial cell**, **CL:0000098 sensory epithelial cell**, and **CL:0000525 syncytiotrophoblast** only if supported in a specific future dataset.

### Other molecular layers

- **mTOR/nutrient sensing:** FTO has been linked experimentally to amino-acid sensing and mTORC1, but a causal mTOR defect has not been demonstrated in GDFD patients.
- **Immune involvement:** no primary immunodeficiency, autoimmunity, or disease-defining inflammation has been established.
- **Metabolomics/lipidomics:** no reproducible syndrome-specific signature exists. The striking HDL values in the p.His271Pro patient were confounded by homozygous CETP truncation. (caglayan2016apatientwith pages 3-5, caglayan2016apatientwith pages 2-3)
- **Single-cell/spatial/multi-omics/CRISPR screens:** none specific to this syndrome were identified through 2024.
- **Recent context:** 2023–2024 RNA-modification research has refined FTO substrate and catalytic biology, but it has not yet yielded a validated GDFD biomarker or treatment.

## 7. Anatomical structures affected

### Organ and tissue levels

Primary systems are:

- **Central nervous system:** cerebral cortex, cerebellar/posterior-fossa structures, ventricles, corpus callosum, and global head/brain growth. Suggested UBERON terms: **UBERON:0000955 brain**, **UBERON:0000956 cerebral cortex**, **UBERON:0002037 cerebellum**, **UBERON:0002336 corpus callosum**.
- **Cardiovascular system:** ventricular/atrioventricular septa, ductus arteriosus, valves, pulmonary trunk, and myocardium. Human embryonic FTO expression was strong in ventricular myocardium, mitral and semilunar valves, and pulmonary-trunk wall. (boissel2009lossoffunctionmutationin pages 2-4)
- **Craniofacial skeleton and palate:** frontonasal and mandibular mesenchyme, jaws, alveolar ridge, palate, skull sutures.
- **Growth and musculoskeletal system:** long-bone and generalized somatic growth, digits, nails, hips, and bone mineralization.
- **Sensory organs:** auditory apparatus and optic disc/eyes.
- **Genitourinary and integumentary systems:** genital anomalies, umbilical hernia, cutis marmorata; renal pathology is more strongly supported in models than in the original human cohort.

FTO expression in human embryos was nearly ubiquitous, with enrichment in CNS, liver, developing pituitary, frontonasal/mandibular mesenchyme, and selected cardiac structures, consistent with multisystem disease. (boissel2009lossoffunctionmutationin pages 2-4)

### Subcellular level

The principal compartment is the **nucleus (GO:0005634)**, where FTO regulates methylated nucleic acids. The relevant structural compartment in model phenotypes is the **cilium (GO:0005929)**. No consistent lateralization is described in human patients; situs abnormalities are model-organism findings.

## 8. Temporal development

The disorder begins **prenatally or in early infancy**. IUGR occurred in 3/7 original patients, while postnatal growth failure and acquired microcephaly were universal among assessed patients. Congenital dysmorphism and malformations may be evident at birth; severe delay, hypertonia, feeding problems, seizures, and brain-volume abnormalities become apparent during infancy. (boissel2009lossoffunctionmutationin pages 2-4, caglayan2016apatientwith pages 2-3)

The course is chronic and generally progressive in functional impact rather than episodic. In the R316Q family, all documented patients died at **1–30 months**. The p.His271Pro patient survived beyond 5.5 years and acquired limited motor milestones, showing genotype-dependent variability. Seizures may cause regression. No spontaneous or treatment-induced remission has been reported. The embryonic/perinatal interval is likely the critical biological window: deleting Fto after six weeks in mice avoided the high lethality of germline deletion, although it still altered body composition. (mcmurray2013adultonsetglobal pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. The original pedigree comprised nine affected Palestinian-Arab relatives from a large consanguineous family. The later p.His271Pro patient was the child of second cousins. Both parents were heterozygous and clinically free of the severe syndrome. (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 2-3)

There are too few molecularly confirmed patients to calculate prevalence, incidence, penetrance, sex ratio, life expectancy by genotype, or carrier frequency. The condition is appropriately considered **ultra-rare**. No validated founder effect has been established, although R316Q occurred in one extended Palestinian-Arab pedigree. No anticipation is expected for a missense disorder, and none has been observed. Germline mosaicism has not been reported but cannot be excluded in apparently de novo families. Penetrance of severe biallelic catalytic-null genotypes appears high in the original pedigree; expressivity is variable across different alleles.

In 1,492 European controls, Boissel et al. found a coding-missense prevalence of **0.87%** but no homozygous missense or compound-heterozygous genotype. This is historical rather than a modern carrier-frequency estimate. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)

## 10. Diagnostics

### Clinical recognition

Consider biallelic FTO syndrome in an infant or child with the combination of:

1. congenital or severe postnatal growth failure;
2. postnatal microcephaly and profound developmental delay;
3. coarse/dysmorphic face, retrognathia, anteverted nares, short neck, brachydactyly, or nail hypoplasia;
4. structural brain, cardiac, hearing, eye, palate, or genital abnormalities;
5. consanguinity or affected siblings; and
6. no explanatory metabolic or chromosomal diagnosis.

There are no formal consensus criteria, enzyme reference ranges, or validated circulating biomarkers.

### Recommended testing workflow

1. **Trio whole-exome or whole-genome sequencing** with recessive analysis is preferred because the phenotype is genetically heterogeneous. Confirm candidate FTO variants and segregation by Sanger sequencing.
2. Ensure coverage of all FTO coding exons, splice junctions, and copy-number changes; phase two variants to establish **trans** configuration.
3. Apply current ACMG/AMP criteria using population frequency, segregation, phenotype match, conservation/catalytic-domain location, and functional evidence.
4. If only one allele is found, use genome sequencing and/or deletion–duplication analysis to search for noncoding, structural, or poorly covered second alleles.
5. **Chromosomal microarray** is useful in multiple congenital anomalies but cannot exclude sequence-level FTO disease. Karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless other findings indicate them.

The original family was solved by autozygosity mapping and sequencing; the p.His271Pro case was solved by WES after a normal female karyotype and absence of pathogenic exonic CNVs. (boissel2009lossoffunctionmutationin pages 1-2, caglayan2016apatientwith pages 1-2, caglayan2016apatientwith pages 3-5)

### Phenotypic evaluation after diagnosis

Recommended baseline evaluations, extrapolated from observed morbidity, include growth and nutritional assessment; developmental and neurologic examination; EEG if seizures are suspected; brain MRI; echocardiography and ECG; audiology; ophthalmology; swallowing/feeding assessment; renal ultrasound; skeletal/bone-health assessment; and liver enzymes/CK if clinically indicated. These are pragmatic surveillance recommendations, not evidence-based syndrome guidelines.

Suggested NCIT terms include **NCIT:C159570 Genetic Testing**, **NCIT:C101295 Whole Exome Sequencing**, **NCIT:C18477 Magnetic Resonance Imaging**, **NCIT:C38054 Echocardiography**, and **NCIT:C16525 Electroencephalography**.

### Differential diagnosis

Important alternatives include chromosomal copy-number disorders; congenital disorders of glycosylation; mitochondrial disease; ciliopathies; RASopathies; Coffin–Siris and Cornelia de Lange syndromes; neurodevelopmental syndromes with coarse facies; lysosomal storage disease; and other causes of syndromic craniosynostosis, lissencephaly, or Dandy–Walker malformation. Molecular testing is decisive because no single clinical feature is specific.

## 11. Outcome and prognosis

For homozygous R316Q, observed survival was poor: **8/8 clinically documented patients died before three years**, at ages **1–30 months**, from intercurrent infection or unidentified causes. No five- or ten-year survival estimate is statistically supportable. (boissel2009lossoffunctionmutationin pages 1-2, boissel2009lossoffunctionmutationin pages 2-4)

Prognosis across all biallelic FTO variants is more variable. Survival beyond 5.5 years with p.His271Pro shows that residual function or allele-specific effects may modify lethality, although profound intellectual and motor disability persisted. (caglayan2016apatientwith pages 3-5, caglayan2016apatientwith pages 2-3)

Major morbidity includes severe growth failure, developmental disability, seizures, dysphagia, hearing loss, cardiac disease, skeletal/bone abnormalities, and recurrent infection vulnerability. Recovery to normal function has not been reported. No validated prognostic biomarker exists. The most plausible prognostic factors are variant functional severity, extent of brain/cardiac malformation, feeding/respiratory status, seizure burden, and infection frequency, but none has been tested in a cohort.

## 12. Treatment and real-world management

No disease-modifying pharmacotherapy, approved targeted treatment, gene therapy, RNA therapy, cell therapy, or established surgical algorithm exists. Focused ClinicalTrials.gov searches found **no relevant interventional study**; obesity, diabetes, or exercise trials involving FTO are not trials of this syndrome.

Management is supportive and multidisciplinary:

- nutritional optimization, feeding therapy, aspiration assessment, and enteral feeding when required;
- standard antiseizure medication selected by seizure type and EEG;
- physical, occupational, speech/communication, and developmental therapies;
- hearing aids or other audiologic intervention;
- standard cardiology management and repair of hemodynamically significant congenital heart disease;
- treatment of respiratory and other infections, with routine vaccination;
- management of orthopedic, craniosynostosis, palate, hernia, genital, eye, and bone-health complications;
- palliative-care involvement for life-limiting disease.

In the p.His271Pro patient, neonatal and later seizures were treated with antiepileptic medication, but no genotype-directed response rate was reported. (caglayan2016apatientwith pages 2-3)

Suggested NCIT concepts: **NCIT:C15421 Supportive Care**, **NCIT:C15313 Palliative Therapy**, **NCIT:C15960 Physical Therapy**, **NCIT:C15311 Occupational Therapy**, **NCIT:C15961 Speech Therapy**, **NCIT:C15206 Enteral Nutrition**, and intervention-specific cardiac or craniofacial surgery concepts where applicable.

FTO inhibition is being investigated in unrelated obesity/cancer contexts, but is biologically unsuitable as replacement therapy for this loss-of-function syndrome. The original investigators specifically warned that FTO-inhibitor development should assess teratogenicity and toxicity because complete catalytic impairment causes congenital abnormalities. (boissel2009lossoffunctionmutationin pages 5-6)

## 13. Prevention

There is no lifestyle, vaccine, or medication capable of preventing disease in a genetically affected embryo.

- **Primary genetic prevention:** preconception carrier testing for relatives of an identified proband; partner testing; genetic counseling; IVF with preimplantation genetic testing for monogenic disease; donor gametes where desired.
- **Prenatal diagnosis:** targeted chorionic-villus sampling or amniocentesis for the known familial alleles. Detailed fetal ultrasound and echocardiography may detect growth or structural abnormalities but cannot reliably exclude disease.
- **Secondary prevention:** early molecular diagnosis and immediate screening for feeding, cardiac, neurologic, hearing, visual, and respiratory complications.
- **Tertiary prevention:** aspiration precautions, seizure control, infection prevention, nutrition, rehabilitation, and complication-specific surveillance.

Population newborn screening is not justified: incidence is unknown, no rapid biochemical marker exists, and no presymptomatic disease-modifying intervention is available. Cascade carrier testing is appropriate in extended consanguineous families.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome confidently equivalent to human biallelic FTO-GDFD was identified. Therefore, breed-specific VBO terms, veterinary prevalence, and zoonotic transmission are not applicable. The disorder is inherited, not infectious, and has no zoonotic potential.

Orthologues include mouse **Fto** (*Mus musculus*, NCBI Taxon **10090**) and zebrafish **fto** (*Danio rerio*, NCBI Taxon **7955**). FTO’s catalytic and developmental functions are evolutionarily conserved, but phenotype severity and organ involvement differ across species.

## 15. Model organisms and experimental systems

### Mouse

Global germline **Fto-knockout mice** show high perinatal/postnatal lethality, reduced body length, fat mass, and lean mass. One study reported that approximately **50% died within days after birth**; surviving animals had reduced length and weight. Conditional nervous-system deletion reproduced shorter body length, low body weight, low bone-mineral density, and reduced IGF-1, supporting a CNS-dependent component of growth control. (zhang2019thernademethylase pages 1-2, gao2010thefatmass pages 1-2, mcmurray2013adultonsetglobal pages 1-2)

Adult-onset global deletion avoided the developmental lethality, indicating that embryonic/perinatal FTO function is critical. Its later phenotype was predominantly reduced lean mass followed by relative fat gain, illustrating why adult metabolic models cannot be equated with congenital human disease. (mcmurray2013adultonsetglobal pages 1-2)

Osteoblast-specific and global deletion models developed reduced trabecular and cortical bone volume. RNA profiling implicated **Hspa1a** and other DNA-damage-response transcripts; Fto-null osteoblasts were more susceptible to UV/H₂O₂-induced damage and apoptosis, which could be normalized by Hspa1a expression or NF-κB inhibition. This supports a stress-protection mechanism but has not been demonstrated in patient bone. (zhang2019thernademethylase pages 1-2)

### Zebrafish

Antisense fto knockdown produced growth retardation, small eyes, body-axis shortening, microcephaly, severe craniofacial-cartilage loss, and abnormal neural-crest migration. A gross craniofacial phenotype occurred in **48/50** morphants, and deficient head cartilage in **36/41**, while p53 cotargeting failed to rescue it. Mouse Fto mRNA partially rescued laterality abnormalities, supporting specificity. (osborn2014lossoffto pages 3-4, osborn2014lossoffto pages 1-3)

### Cellular systems

Relevant systems include patient dermal fibroblasts, Fto-null mouse embryonic fibroblasts, FTO-depleted HEK293T cells, and osteoblast cultures. No validated patient-derived iPSC, cerebral organoid, knock-in R316Q animal, or high-throughput therapeutic-screen platform was identified.

### Model limitations

Morpholino knockdown can produce developmental artifacts and does not reproduce a specific human missense allele. Mouse null phenotypes incompletely recapitulate the human brain and cardiac malformations, while R316Q may retain protein capable of noncatalytic or toxic interactions. Boissel et al. explicitly considered—but regarded as unlikely—the possibility of another pathogenic lesion within the linked interval. Consequently, Wnt/ciliary, IGF-1, and osteoblast-stress mechanisms should be annotated as **model-supported/inferred in humans**, whereas R316Q catalytic inactivation, segregation, and patient-fibroblast senescence are direct human evidence. (boissel2009lossoffunctionmutationin pages 4-5)

## Recent developments and knowledge gaps, 2023–2024

The major disease-specific recent development was the **2023 case report** expanding the phenotype to multisystem abnormalities and severe epilepsy. Broader 2023–2024 work refined FTO/RNA-modification biology but did not establish a disease-specific treatment, clinical biomarker, single-cell atlas, natural-history registry, diagnostic guideline, or prospective cohort. No relevant registered interventional trial was found. Thus, the most authoritative quantitative clinical evidence remains the 2009 family and 2016 single-patient reports, while modern mechanistic interpretation relies substantially on animal and cellular models.

Priority research needs are: standardized reanalysis of every reported variant under current ACMG/AMP criteria; deposition of complete cases in ClinVar/DECIPHER; an international natural-history registry; direct measurement of m6A/m6Am and transcriptomic consequences in patient-derived neural and cardiac cells; R316Q and other allele-specific knock-in models; and evaluation of whether early replacement or editing of FTO can rescue developmental phenotypes without perturbing its dosage-sensitive metabolic functions.

References

1. (boissel2009lossoffunctionmutationin pages 1-2): Sarah Boissel, Orit Reish, Karine Proulx, Hiroko Kawagoe-Takaki, Barbara Sedgwick, Giles S.H. Yeo, David Meyre, Christelle Golzio, Florence Molinari, Noman Kadhom, Heather C. Etchevers, Vladimir Saudek, I. Sadaf Farooqi, Philippe Froguel, Tomas Lindahl, Stephen O'Rahilly, Arnold Munnich, and Laurence Colleaux. Loss-of-function mutation in the dioxygenase-encoding fto gene causes severe growth retardation and multiple malformations. American journal of human genetics, 85 1:106-11, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.002, doi:10.1016/j.ajhg.2009.06.002. This article has 501 citations and is from a highest quality peer-reviewed journal.

2. (OpenTargets Search: lethal polymalformative syndrome Boissel type-FTO): Open Targets Query (lethal polymalformative syndrome Boissel type-FTO, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (caglayan2016apatientwith pages 1-2): Ahmet O Çağlayan, Beyhan Tüysüz, Süleyman Coşkun, Jennifer Quon, Akdes S Harmancı, Jacob F Baranoski, Burçin Baran, E Zeynep Erson-Omay, Octavian Henegariu, Shrikant M Mane, Kaya Bilgüvar, Katsuhito Yasuno, and Murat Günel. A patient with a novel homozygous missense mutation in fto and concomitant nonsense mutation in cetp. Jan 2016. URL: https://doi.org/10.1038/jhg.2015.160, doi:10.1038/jhg.2015.160. This article has 20 citations and is from a peer-reviewed journal.

4. (caglayan2016apatientwith pages 3-5): Ahmet O Çağlayan, Beyhan Tüysüz, Süleyman Coşkun, Jennifer Quon, Akdes S Harmancı, Jacob F Baranoski, Burçin Baran, E Zeynep Erson-Omay, Octavian Henegariu, Shrikant M Mane, Kaya Bilgüvar, Katsuhito Yasuno, and Murat Günel. A patient with a novel homozygous missense mutation in fto and concomitant nonsense mutation in cetp. Jan 2016. URL: https://doi.org/10.1038/jhg.2015.160, doi:10.1038/jhg.2015.160. This article has 20 citations and is from a peer-reviewed journal.

5. (boissel2009lossoffunctionmutationin pages 4-5): Sarah Boissel, Orit Reish, Karine Proulx, Hiroko Kawagoe-Takaki, Barbara Sedgwick, Giles S.H. Yeo, David Meyre, Christelle Golzio, Florence Molinari, Noman Kadhom, Heather C. Etchevers, Vladimir Saudek, I. Sadaf Farooqi, Philippe Froguel, Tomas Lindahl, Stephen O'Rahilly, Arnold Munnich, and Laurence Colleaux. Loss-of-function mutation in the dioxygenase-encoding fto gene causes severe growth retardation and multiple malformations. American journal of human genetics, 85 1:106-11, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.002, doi:10.1016/j.ajhg.2009.06.002. This article has 501 citations and is from a highest quality peer-reviewed journal.

6. (boissel2009lossoffunctionmutationin pages 2-4): Sarah Boissel, Orit Reish, Karine Proulx, Hiroko Kawagoe-Takaki, Barbara Sedgwick, Giles S.H. Yeo, David Meyre, Christelle Golzio, Florence Molinari, Noman Kadhom, Heather C. Etchevers, Vladimir Saudek, I. Sadaf Farooqi, Philippe Froguel, Tomas Lindahl, Stephen O'Rahilly, Arnold Munnich, and Laurence Colleaux. Loss-of-function mutation in the dioxygenase-encoding fto gene causes severe growth retardation and multiple malformations. American journal of human genetics, 85 1:106-11, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.002, doi:10.1016/j.ajhg.2009.06.002. This article has 501 citations and is from a highest quality peer-reviewed journal.

7. (boissel2009lossoffunctionmutationin pages 5-6): Sarah Boissel, Orit Reish, Karine Proulx, Hiroko Kawagoe-Takaki, Barbara Sedgwick, Giles S.H. Yeo, David Meyre, Christelle Golzio, Florence Molinari, Noman Kadhom, Heather C. Etchevers, Vladimir Saudek, I. Sadaf Farooqi, Philippe Froguel, Tomas Lindahl, Stephen O'Rahilly, Arnold Munnich, and Laurence Colleaux. Loss-of-function mutation in the dioxygenase-encoding fto gene causes severe growth retardation and multiple malformations. American journal of human genetics, 85 1:106-11, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.002, doi:10.1016/j.ajhg.2009.06.002. This article has 501 citations and is from a highest quality peer-reviewed journal.

8. (osborn2014lossoffto pages 4-7): Daniel P. S. Osborn, Rosa Maria Roccasecca, Fiona McMurray, Victor Hernandez-Hernandez, Sriparna Mukherjee, Inês Barroso, Derek Stemple, Roger Cox, Philip L. Beales, and Sonia Christou-Savina. Loss of fto antagonises wnt signaling and leads to developmental defects associated with ciliopathies. PLoS ONE, 9:e87662, Feb 2014. URL: https://doi.org/10.1371/journal.pone.0087662, doi:10.1371/journal.pone.0087662. This article has 39 citations and is from a peer-reviewed journal.

9. (caglayan2016apatientwith pages 5-6): Ahmet O Çağlayan, Beyhan Tüysüz, Süleyman Coşkun, Jennifer Quon, Akdes S Harmancı, Jacob F Baranoski, Burçin Baran, E Zeynep Erson-Omay, Octavian Henegariu, Shrikant M Mane, Kaya Bilgüvar, Katsuhito Yasuno, and Murat Günel. A patient with a novel homozygous missense mutation in fto and concomitant nonsense mutation in cetp. Jan 2016. URL: https://doi.org/10.1038/jhg.2015.160, doi:10.1038/jhg.2015.160. This article has 20 citations and is from a peer-reviewed journal.

10. (mcmurray2013adultonsetglobal pages 1-2): Fiona McMurray, Chris D. Church, Rachel Larder, George Nicholson, Sara Wells, Lydia Teboul, Y. C. Loraine Tung, Debra Rimmington, Fatima Bosch, Veronica Jimenez, Giles S. H. Yeo, Stephen O'Rahilly, Frances M. Ashcroft, Anthony P. Coll, and Roger D. Cox. Adult onset global loss of the fto gene alters body composition and metabolism in the mouse. Jan 2013. URL: https://doi.org/10.1371/journal.pgen.1003166, doi:10.1371/journal.pgen.1003166. This article has 189 citations and is from a domain leading peer-reviewed journal.

11. (caglayan2016apatientwith pages 2-3): Ahmet O Çağlayan, Beyhan Tüysüz, Süleyman Coşkun, Jennifer Quon, Akdes S Harmancı, Jacob F Baranoski, Burçin Baran, E Zeynep Erson-Omay, Octavian Henegariu, Shrikant M Mane, Kaya Bilgüvar, Katsuhito Yasuno, and Murat Günel. A patient with a novel homozygous missense mutation in fto and concomitant nonsense mutation in cetp. Jan 2016. URL: https://doi.org/10.1038/jhg.2015.160, doi:10.1038/jhg.2015.160. This article has 20 citations and is from a peer-reviewed journal.

12. (zhang2019thernademethylase pages 1-2): Qian Zhang, Ryan C. Riddle, Qian Yang, Clifford R. Rosen, Denis C. Guttridge, Naomi Dirckx, Marie-Claude Faugere, Charles R. Farber, and Thomas L. Clemens. The rna demethylase fto is required for maintenance of bone mass and functions to protect osteoblasts from genotoxic damage. Proceedings of the National Academy of Sciences, 116:17980-17989, Aug 2019. URL: https://doi.org/10.1073/pnas.1905489116, doi:10.1073/pnas.1905489116. This article has 134 citations and is from a highest quality peer-reviewed journal.

13. (gulati2013thebiologyof pages 2-4): Pawan Gulati and Giles S. H. Yeo. The biology of fto: from nucleic acid demethylase to amino acid sensor. Diabetologia, 56:2113-2121, Jul 2013. URL: https://doi.org/10.1007/s00125-013-2999-5, doi:10.1007/s00125-013-2999-5. This article has 87 citations and is from a highest quality peer-reviewed journal.

14. (osborn2014lossoffto pages 1-3): Daniel P. S. Osborn, Rosa Maria Roccasecca, Fiona McMurray, Victor Hernandez-Hernandez, Sriparna Mukherjee, Inês Barroso, Derek Stemple, Roger Cox, Philip L. Beales, and Sonia Christou-Savina. Loss of fto antagonises wnt signaling and leads to developmental defects associated with ciliopathies. PLoS ONE, 9:e87662, Feb 2014. URL: https://doi.org/10.1371/journal.pone.0087662, doi:10.1371/journal.pone.0087662. This article has 39 citations and is from a peer-reviewed journal.

15. (osborn2014lossoffto pages 3-4): Daniel P. S. Osborn, Rosa Maria Roccasecca, Fiona McMurray, Victor Hernandez-Hernandez, Sriparna Mukherjee, Inês Barroso, Derek Stemple, Roger Cox, Philip L. Beales, and Sonia Christou-Savina. Loss of fto antagonises wnt signaling and leads to developmental defects associated with ciliopathies. PLoS ONE, 9:e87662, Feb 2014. URL: https://doi.org/10.1371/journal.pone.0087662, doi:10.1371/journal.pone.0087662. This article has 39 citations and is from a peer-reviewed journal.

16. (gao2010thefatmass pages 1-2): Xue Gao, Yong-Hyun Shin, Min Li, Fei Wang, Qiang Tong, and Pumin Zhang. The fat mass and obesity associated gene fto functions in the brain to regulate postnatal growth in mice. PLoS ONE, 5:e14005, Nov 2010. URL: https://doi.org/10.1371/journal.pone.0014005, doi:10.1371/journal.pone.0014005. This article has 287 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Lethal_Polymalformative_Syndrome_Boissel_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 82 |
| Resolved | 80 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013050` (6 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **lethal polymalformative syndrome, Boissel type**
- `GO:0033123` (1 mention) - the report calls it "RNA demethylase activity"; GO calls it **positive regulation of purine nucleotide catabolic process**
- `NCIT:C159670` (1 mention) - the report calls it "Whole Exome Sequencing"; NCIT calls it **Bladder Leiomyosarcoma**
- `NCIT:C122421` (1 mention) - the report calls it "Lethal"; NCIT calls it **Agricultural Workers**
- `NCIT:C15421` (2 mentions) - the report calls it "Supportive Care"; NCIT calls it **Postmenopausal**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:000252` (1 mention) - HP does not contain this term
- `HP:0000281` (1 mention) - HP does not contain this term

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013050` - called "if available", "MONDO"