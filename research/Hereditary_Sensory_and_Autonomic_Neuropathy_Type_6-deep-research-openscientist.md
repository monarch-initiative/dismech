---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T15:44:07.518593'
end_time: '2026-09-06T16:03:28.285824'
duration_seconds: 1160.77
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hereditary Sensory and Autonomic Neuropathy Type 6
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 19
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 19
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0013839
    reported_labels:
    - MONDO
    ontology_label: hereditary sensory and autonomic neuropathy type 6
  - term_id: DOID:0070151
    reported_labels:
    - Disease Ontology
    ontology_label: hereditary sensory and autonomic neuropathy type 6
  - term_id: GO:0030424
    reported_labels:
    - Cellular component:* axon
    ontology_label: axon
  labels_variant: 10
  unresolvable_prefixes:
  - ORPHA
  - GARD
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_6-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Sensory and Autonomic Neuropathy Type 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Sensory and Autonomic Neuropathy Type 6** covering all of the
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

# Hereditary Sensory and Autonomic Neuropathy Type VI (HSAN-VI): Comprehensive Disease Characterization Report

**Disease:** Hereditary Sensory and Autonomic Neuropathy Type 6 (HSAN-VI)
**MONDO ID:** MONDO:0013839 | **OMIM:** #614653 | **Orphanet:** ORPHA:314381
**Causal gene:** *DST* (dystonin / BPAG1) | **Inheritance:** Autosomal recessive
**Category:** Mendelian (ultra-rare)

---

## Summary

Hereditary Sensory and Autonomic Neuropathy Type VI (HSAN-VI) is an ultra-rare, autosomal recessive disorder of the peripheral nervous system caused by biallelic loss-of-function of the **neuronal DST-a isoforms** of the *DST* gene (dystonin, also known as bullous pemphigoid antigen 1 / BPAG1). Dystonin-a proteins are large plakin-family **cytoskeletal cross-linkers (spectraplakins)** that physically tether the actin microfilament, intermediate filament (neurofilament), and microtubule networks within sensory and autonomic neurons. When these isoforms are lost, the axonal cytoskeleton disorganizes, axonal transport fails, the endoplasmic reticulum/nuclear envelope becomes dysfunctional, and autophagic flux is impaired — collectively driving progressive degeneration of dorsal root ganglion (DRG) sensory neurons and autonomic neurons. As of 2025, the disease remains vanishingly rare, with only about 15 reported patients carrying 11 distinct *DST* variants (mostly compound heterozygous).

Clinically, HSAN-VI presents on a **severity spectrum graded by which DST-a isoforms are ablated**. At the severe end lies fetal/neonatal lethal disease — arthrogryposis multiplex congenita (now formalized as lethal congenital contracture syndrome 12, LCCS12), severe neonatal hypotonia, respiratory and feeding failure, profound pain insensitivity, and prominent dysautonomia (alacrima, labile blood pressure and temperature, cardiac arrhythmia). At the milder end is adult-onset, slowly progressive sensory neuropathy with painless ulcers. Residual expression of **DST-A3** acts as an endogenous protective modifier that preserves microtubule stability and softens the phenotype. *DST* is one member of a four-disorder single-gene allelic series, along with epidermolysis bullosa simplex 3 (EBS3, from loss of the epithelial DST-e isoform), congenital myopathy 29 (CMYO29, from loss of the muscular DST-b isoform), and LCCS12.

Diagnosis is molecular — exome/genome sequencing or hereditary-neuropathy gene panels, with copy-number analysis needed given the very large *DST* locus. There is **no approved disease-modifying therapy**; management is entirely supportive and multidisciplinary (airway/respiratory support, nutrition, corneal protection, wound/ulcer prevention, autonomic monitoring). The **dystonia musculorum (dt) mouse** faithfully recapitulates the human disease and has provided proof-of-concept that neuronal DST-a2 gene restoration partially rescues the phenotype, defining a rational future therapeutic direction.

---

## 1. Disease Information

**Overview.** HSAN-VI is an autosomal recessive subtype within the hereditary sensory and autonomic neuropathy (HSAN) family. It manifests severe pain insensitivity, neonatal hypotonia, respiratory and feeding difficulties, lack of psychomotor development, and autonomic abnormalities. The underlying cause is pathogenic variants in *DST*, which encodes dystonin ([PMID: 40938507](https://pubmed.ncbi.nlm.nih.gov/40938507/)):

> "HSAN-VI (OMIM: 614653) is an autosomal recessive subtype which manifests severe pain insensitivity, neonatal hypotonia, respiratory and feeding difficulties, lack of psychomotor development and autonomic abnormalities. Pathogenic variants in the DST gene, which encodes dystonin have been identified as the underlying cause of HSAN-VI. Thus far, only 15 HSAN-VI patients associated with 11 DST variants, mostly compound heterozygous, have been identified in the literature."

**Key identifiers (database-verified).**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0013839 |
| OMIM | #614653 |
| Orphanet | ORPHA:314381 |
| Disease Ontology | DOID:0070151 |
| GARD | GARD:0012987 |
| MedGen | 761278 |
| UMLS | C3539003 |
| ICD-10 | G60.8 (group level only) |
| ICD-11 | 8C10.Y (group level only) |
| MeSH | D009477 — *Hereditary Sensory and Autonomic Neuropathies* (group level only) |

Importantly, **no ICD or MeSH code exists specifically for HSAN-VI** — those classifications apply only at the broader HSAN group level; the granular MONDO term carries no ICD/MeSH mapping.

**Synonyms / alternative names.** HSAN VI; HSAN type 6; familial dysautonomia with contractures; DST hereditary sensory and autonomic neuropathy.

**Information source.** The disease-level knowledge base entry is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO, HPO/JAX) combined with a small number of **individual patient case reports** — reflecting the ultra-rare nature of the disorder.

---

## 2. Etiology

**Primary cause — genetic.** HSAN-VI is a monogenic Mendelian disorder caused by **biallelic (recessive) loss-of-function variants in the neuronal DST-a isoforms** of *DST*. There is no known environmental, infectious, or acquired cause. Disease requires two damaged alleles; heterozygous carriers are asymptomatic.

**Genetic risk factors.** The causal variants are within *DST* itself. *DST* is strongly loss-of-function constrained at the gene level (gnomAD: LOEUF ≈ 0.32, observed/expected LoF = 0.29 [253 observed vs 875.2 expected], pLI = 1, missense Z = 3.68), consistent with an essential developmental gene. The specific set of DST-a isoforms disrupted by a given variant is the principal determinant of severity (see Sections 3, 4, 6).

**Modifier genes / modifier alleles.** The clearest modifier is **isoform-intrinsic**: residual expression of DST-A3 partially compensates for loss of DST-A1/A2 and reduces severity ([PMID: 29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/)). No independent trans-acting modifier gene has been established.

**Environmental risk / protective factors.** None identified — this is a fully penetrant Mendelian disorder. There are no reported environmental toxins, lifestyle factors, or protective exposures. **Consanguinity** raises the risk of homozygosity (several reported cases are from consanguineous unions).

**Gene–environment interactions.** Not applicable / none reported.

---

## 3. Phenotypes

HSAN-VI is annotated by HPO/JAX with **39 phenotype terms** under OMIM:614653. Core features span sensory, autonomic, respiratory, gastrointestinal, and skeletal domains.

| Domain | Phenotype | HPO term |
|--------|-----------|----------|
| Sensory | Sensory neuropathy / pain insensitivity | HP:0000763 |
| Sensory | Areflexia | HP:0001284 |
| Neurodevelopment | Profound global developmental delay | HP:0012736 |
| Autonomic | Alacrima (reduced tears) | HP:0000522 |
| Autonomic | Absent corneal reflex | HP:0034252 |
| Autonomic (secondary) | Corneal scarring | HP:0000559 |
| Autonomic | Hyperhidrosis | HP:0000975 |
| Autonomic | Tachycardia | HP:0001649 |
| Autonomic | Bradycardia | HP:0001662 |
| Autonomic | Hypertension / labile BP | HP:0000822 |
| Autonomic | Hyperpyrexia / temperature instability | HP:0033031 |
| Respiratory | Neonatal respiratory distress | HP:0002643 |
| Respiratory | Apnea | HP:0002104 |
| Respiratory | Stridor | HP:0010307 |
| Respiratory | Aspiration | HP:0002835 |
| Respiratory | Bilateral vocal cord paresis | HP:0012822 |
| Motor tone | Hypotonia (generalized/neonatal/axial) | HP:0001319 / HP:0001290 / HP:0001252 |
| GI | Gastroesophageal reflux | HP:0002020 |
| GI | Feeding difficulties | HP:0011968 |
| GI | Poor suck | HP:0002033 |
| Skeletal | Talipes equinovarus (club foot) | HP:0001762 |
| Skeletal | Flexion contracture | HP:0001371 |
| Inheritance | Autosomal recessive inheritance | HP:0000007 |

**Phenotype characteristics.**
- **Age of onset:** Predominantly **congenital/neonatal** in the severe form (arthrogryposis, hypotonia, respiratory distress at birth); the mild allelic form can be **adult-onset**.
- **Severity:** **Variable** — from intrauterine/neonatal lethal to slowly progressive adult neuropathy.
- **Progression:** **Progressive** neuronal degeneration; severe forms are rapidly fatal, milder forms slowly worsen.
- **Frequency:** In the severe neonatal phenotype, pain insensitivity, hypotonia, respiratory/feeding difficulty, and autonomic instability are near-universal among reported cases.

**Quality-of-life impact.** Profound. In severe disease, affected infants have no meaningful psychomotor development, require ventilatory and nutritional support, and are at constant risk from autonomic crises, aspiration, and self-injury/corneal damage due to insensitivity to pain. The dysautonomia closely mirrors that of Riley–Day syndrome (familial dysautonomia).

---

## 4. Genetic / Molecular Information

**Causal gene.** *DST* (dystonin / BPAG1). HGNC:1090; NCBI Gene 667; Ensembl ENSG00000151914; gene OMIM 113810; UniProt Q03001; located at **chr6p12.1** (GRCh38 chr6:56,457,981–56,955,274, minus strand). *DST* is very large and produces multiple tissue-specific isoform classes by alternative splicing: **DST-a (neuronal, a1/a2/a3)**, **DST-b (muscular, b1/b2/b3)**, and **DST-e (epithelial)** ([PMID: 34897952](https://pubmed.ncbi.nlm.nih.gov/34897952/), [PMID: 37603210](https://pubmed.ncbi.nlm.nih.gov/37603210/)). HSAN-VI arises specifically from **loss of the neuronal DST-a isoforms** ([PMID: 35276021](https://pubmed.ncbi.nlm.nih.gov/35276021/)):

> "This mutation resides within the plakin domain of BPAG1 and ablates all isoforms of this protein, leading to novel extracutaneous phenotypes consistent with HSAN-VI"

**The DST four-disorder allelic series.** A key organizing insight is that *DST* is a single locus underlying four distinct allelic disorders, resolvable by which isoform(s) a variant disrupts ([PMID: 40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/)):

| Disorder | Isoform lost | Phenotype |
|----------|-------------|-----------|
| **HSAN-VI** | DST-a (neuronal) | Sensory/autonomic neuropathy |
| **EBS3 / EBSB2** | DST-e (epithelial) | Epidermolysis bullosa simplex |
| **CMYO29** (congenital myopathy 29) | DST-b (muscular) | Neonatal myopathy, arthrogryposis, dilated cardiomyopathy |
| **LCCS12** (lethal congenital contracture syndrome 12) | DST-a + DST-b | Severe fetal/neonatal lethal arthrogryposis |

[PMID: 40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/): *"We propose redefining DST as a disease-associated gene linked to four distinct allelic disease phenotypes … The location of the variant within DST allows for phenotype prediction."*

**Pathogenic variants.** Reported HSAN-VI variants are **compound heterozygous or homozygous LoF and missense** changes affecting DST-a. Representative pathogenic/likely-pathogenic examples (ClinVar) include:
- c.22558del p.(Leu7520fs) — frameshift
- p.His269Arg / c.905A>G p.(His302Arg) — missense
- p.Arg1269Ter — nonsense (also annotated to LCCS12)
- p.Ala203Glu — missense in the actin-binding domain; recombinant protein loses actin binding ([PMID: 30371979](https://pubmed.ncbi.nlm.nih.gov/30371979/))
- c.1118C>T p.Pro373Leu — homozygous, consanguineous ([PMID: 34897952](https://pubmed.ncbi.nlm.nih.gov/34897952/))

**Variant types:** missense, frameshift, nonsense, and splice variants. **Classification** per ACMG/AMP: pathogenic and likely pathogenic records dominate ClinVar for HSAN-VI. **Allele frequency:** individual pathogenic alleles are extremely rare/private in gnomAD, consistent with the disorder's rarity and LoF constraint. **Origin:** germline. **Functional consequence:** **loss of function** (loss of the neuronal cytolinker).

**Modifier genes / epigenetics / chromosomal abnormalities.** The principal modifier is the **DST-A3 isoform** (intragenic compensation). No specific epigenetic mechanism (DNA methylation, histone modification) or recurrent large-scale chromosomal abnormality has been described for HSAN-VI. Given the size of *DST*, however, copy-number/structural analysis is diagnostically relevant.

---

## 5. Environmental Information

Not applicable. HSAN-VI is a purely genetic Mendelian disorder. There are **no established environmental factors, lifestyle factors, or infectious agents** that cause, trigger, or protect against the disease. Consanguinity is a demographic risk factor for recessive homozygosity but is not an environmental exposure per se.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (mutation → clinical manifestation)

1. **Biallelic LoF variants in the neuronal DST-a isoforms** *lead to* absence or dysfunction of dystonin-a cytolinker protein in sensory and autonomic neurons.
2. Loss of dystonin-a *results in* **failure to physically tether actin microfilaments to intermediate filaments (neurofilaments) and microtubules** — the protein's core function ([PMID: 8752219](https://pubmed.ncbi.nlm.nih.gov/8752219/)).
3. Cytolinker loss *leads to* **disorganization of the axonal cytoskeleton**, including disrupted actin organization (patient cells; p.Ala203Glu abolishes actin binding) and loss/aggregation of neurofilament proteins such as α-internexin ([PMID: 30371979](https://pubmed.ncbi.nlm.nih.gov/30371979/), [PMID: 16691115](https://pubmed.ncbi.nlm.nih.gov/16691115/)).
4. Cytoskeletal disorganization *results in* **impaired fast axonal transport** in both orthograde and retrograde directions, with focal axonal swellings ([PMID: 12859670](https://pubmed.ncbi.nlm.nih.gov/12859670/)).
5. In parallel, dystonin loss *results in* **endoplasmic reticulum / nuclear-envelope dysfunction and ER stress** ([PMID: 18638474](https://pubmed.ncbi.nlm.nih.gov/18638474/)) **and impaired autophagic flux** (autophagosome accumulation, elevated LC3-II) ([PMID: 26043942](https://pubmed.ncbi.nlm.nih.gov/26043942/)).
6. Loss of microtubule-stabilizing function *leads to* **microtubule instability with reduced tubulin acetylation** in severe alleles — partially rescued when DST-A3 is upregulated ([PMID: 29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/)).
7. These converging insults *drive* **progressive degeneration of DRG sensory neurons** (and autonomic neurons), with caspase-3 activation in aggregate-laden neurons ([PMID: 16691115](https://pubmed.ncbi.nlm.nih.gov/16691115/)) — selectively affecting NT-3-responsive muscle afferents and GDNF-responsive neurons ([PMID: 11241383](https://pubmed.ncbi.nlm.nih.gov/11241383/)).
8. **Sensory neuron loss** *manifests as* pain insensitivity, areflexia, and sensory ataxia; **muscle-spindle/afferent degeneration** *manifests as* hypotonia and ataxia ([PMID: 9242412](https://pubmed.ncbi.nlm.nih.gov/9242412/)).
9. **Branch — autonomic:** degeneration of autonomic/afferent circuits *results in* dysautonomia — alacrima, labile blood pressure and temperature, and cardiac arrhythmia via disrupted afferent neural circuits ([PMID: 42028226](https://pubmed.ncbi.nlm.nih.gov/42028226/)) — plus GI dysmotility ([PMID: 31814231](https://pubmed.ncbi.nlm.nih.gov/31814231/)).

### Detail

**Molecular architecture (UniProt Q03001, canonical 7570 aa).** Dystonin-a is a spectraplakin with an N-terminal tandem calponin-homology **actin-binding domain (CH1–CH2)**, an SH3 domain, 37 spectrin/plakin repeats, two EF-hands (calcium binding), and a C-terminal **GAR microtubule-binding domain**. This bipartite architecture is what allows it to bridge actin at one end and microtubules/intermediate filaments at the other ([PMID: 8752219](https://pubmed.ncbi.nlm.nih.gov/8752219/), [PMID: 26778567](https://pubmed.ncbi.nlm.nih.gov/26778567/)).

**GO annotations.**
- *Molecular function:* microtubule binding (GO:0008017), microtubule plus-end binding (GO:0051010), calcium ion binding (GO:0005509), integrin binding (GO:0005178).
- *Biological process:* retrograde axonal transport (GO:0008090), cytoskeleton organization (GO:0007010).
- *Cellular component:* axon (GO:0030424), ER membrane (GO:0005789), nuclear envelope (GO:0005635), microtubule/IF/actin cytoskeleton.

**Cellular processes:** cytoskeletal disorganization, impaired intracellular transport, ER stress, impaired autophagy, and ultimately apoptosis. **Upstream** events are the cytolinker loss and cytoskeletal failure; **downstream** events are transport failure, organelle stress, and neuronal death. **Cell types involved:** DRG sensory neurons (CL:0000101 sensory neuron), autonomic neurons, and Schwann cells (CL:0002573) — Schwann-cell-specific loss produces a late-onset neuropathy with hypomyelination ([PMID: 32445516](https://pubmed.ncbi.nlm.nih.gov/32445516/)).

---

## 7. Anatomical Structures Affected

**Organ / system level.** The **peripheral nervous system** is primary — specifically the **dorsal root ganglia** (UBERON:0000044) and the **sensory and autonomic divisions** of the PNS. Secondary/complication involvement spans:
- **Respiratory system** (UBERON:0001004) — respiratory distress, apnea, vocal cord paresis, aspiration.
- **Cardiovascular system** — arrhythmia, labile blood pressure.
- **Gastrointestinal tract** (UBERON:0001555) — reflux, dysmotility, feeding failure.
- **Eye / cornea** (UBERON:0000964 / UBERON:0000411) — alacrima with secondary corneal scarring.
- **Musculoskeletal system** — contractures, club foot, hypotonia (secondary to afferent/muscle-spindle loss).

**Tissue / cell level.** Nervous tissue; specific vulnerable populations are **sensory neurons** (CL:0000101), **peripheral sensory neurons / DRG neurons**, **autonomic neurons**, and **Schwann cells** (CL:0002573). Selectively vulnerable subtypes: NT-3-responsive muscle afferents and GDNF-responsive neurons ([PMID: 11241383](https://pubmed.ncbi.nlm.nih.gov/11241383/)).

**Subcellular level.** Axon (GO:0030424); microtubule/IF/actin cytoskeleton; ER membrane (GO:0005789); nuclear envelope (GO:0005635) ([PMID: 18638474](https://pubmed.ncbi.nlm.nih.gov/18638474/)).

**Localization / lateralization.** Bilateral and generally symmetric peripheral involvement.

---

## 8. Temporal Development

**Onset.** Predominantly **congenital/neonatal** in severe disease (arthrogryposis at birth, neonatal hypotonia and respiratory distress); an allelic milder form is **adult-onset**. The dystonia musculorum mouse shows that pathology is **restricted largely to postnatal development** despite broad developmental expression of neuronal BPAG1 ([PMID: 9242412](https://pubmed.ncbi.nlm.nih.gov/9242412/)).

**Progression.** **Progressive** degeneration. In the mouse model, massive postnatal DRG neuron degeneration culminates in death at ~4 weeks. In humans, the course ranges from intrauterine/neonatal lethal (LCCS12 end) to slowly progressive over decades (mild adult end).

**Patterns.** No spontaneous remission. The developmental **critical period** in the mouse is early postnatal life — the window when transgenic DST-a2 restoration partially rescues the phenotype ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)) — suggesting an early therapeutic window in humans.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare. Only ~15 HSAN-VI patients (11 *DST* variants) reported worldwide as of 2025 ([PMID: 40938507](https://pubmed.ncbi.nlm.nih.gov/40938507/)). Precise prevalence/incidence figures are unavailable; Orphanet classifies it among ultra-rare disorders.

**Inheritance.** **Autosomal recessive** (HP:0000007). Biallelic (homozygous or compound heterozygous) variants are required.

**Penetrance / expressivity.** Penetrance appears **complete** for biallelic LoF, but **expressivity is highly variable**, graded by the specific DST-a isoforms disrupted and by residual DST-A3 compensation.

**Genetic anticipation.** Not applicable (not a repeat-expansion disorder).

**Founder effects / consanguinity.** No established founder mutation. **Consanguinity** contributes to homozygous cases (multiple reported families are consanguineous, e.g., [PMID: 34897952](https://pubmed.ncbi.nlm.nih.gov/34897952/), [PMID: 40938507](https://pubmed.ncbi.nlm.nih.gov/40938507/)).

**Carrier frequency.** Not formally established; expected to be very low given rarity.

**Demographics.** No sex predilection (autosomal). Cases reported across diverse populations (including a Pakistani family). No endemic geographic clustering.

---

## 10. Diagnostics

**Genetic testing is the diagnostic mainstay.** HSAN-VI has no pathognomonic biochemical marker; diagnosis rests on identifying **biallelic pathogenic DST-a variants**.

- **Whole exome / whole genome sequencing (WES/WGS):** high utility — the typical route to diagnosis after nonspecific presentation. In one case, karyotype, Prader-Willi assay, SMA panel, and myotonic dystrophy panel were all negative before a comprehensive neuropathy panel/sequencing detected the *DST* variant ([PMID: 42563873](https://pubmed.ncbi.nlm.nih.gov/42563873/)).
- **Hereditary-neuropathy gene panels** including *DST*.
- **Copy-number / structural variant analysis:** important given the very large *DST* locus (single-nucleotide panels may miss deletions/duplications).
- Isoform-aware interpretation is essential — variant position predicts whether DST-a, DST-b, DST-e, or combinations are affected, and hence the disorder ([PMID: 40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/)).

**Supporting clinical/electrophysiologic tests.** Nerve conduction studies and sural nerve biopsy show sensory axonal loss; electron microscopy of peripheral nerve can reveal **severe hypomyelination and dramatically reduced fiber density** ([PMID: 37431644](https://pubmed.ncbi.nlm.nih.gov/37431644/)). Areflexia and absent corneal reflex are clinical signs. Autonomic testing documents dysautonomia (alacrima, labile BP/temperature, arrhythmia).

**Differential diagnosis.** Other HSAN subtypes (I–V, VII, VIII), familial dysautonomia / Riley–Day syndrome (autonomic overlap), congenital myopathies and arthrogryposis syndromes, spinal muscular atrophy, and myotonic dystrophy (to be excluded, as in the case above).

**Screening.** No population newborn screening exists. **Cascade carrier testing** of at-risk relatives and **prenatal/preimplantation genetic testing** are available once the familial variants are known.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Prognosis is **poor in severe forms**. LCCS12-end disease is intrauterine or neonatal lethal; severe HSAN-VI infants often die in early life from respiratory failure, aspiration, or autonomic crises. The dystonia musculorum mouse dies at ~4 weeks. Milder adult-onset forms are compatible with prolonged survival but progressive disability.

**Morbidity / function.** Very high — profound global developmental delay, no meaningful psychomotor progress in severe cases, dependence on ventilatory and nutritional support, recurrent injury from pain insensitivity (corneal scarring, self-mutilation, painless ulcers/fractures), and autonomic instability.

**Complications.** Aspiration pneumonia, respiratory failure, corneal ulceration/scarring, cardiac arrhythmia, GI dysmotility/reflux, contractures.

**Recovery potential.** None with current care; management is supportive only.

**Prognostic factors.** The strongest predictor is the **molecular genotype** — which DST-a isoforms are ablated and whether DST-A3 is preserved. Variants ablating all three neuronal isoforms (a1/a2/a3) produce the most severe disease; preservation of DST-A3 predicts milder disease ([PMID: 29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/), [PMID: 40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/)).

---

## 12. Treatment

**No approved disease-modifying therapy exists.** Care is entirely **supportive and multidisciplinary** (NCIT: Supportive Care Intervention):

- **Respiratory:** airway management, CPAP/ventilatory support, treatment of aspiration.
- **Nutrition/GI:** feeding support (NG/gastrostomy), reflux and dysmotility management.
- **Ophthalmologic:** artificial tears/lubrication and corneal protection to prevent scarring from alacrima and absent corneal reflex.
- **Wound/injury prevention:** protective measures against painless ulcers, burns, fractures, and self-injury (analogous to other HSANs).
- **Autonomic:** cardiac rhythm monitoring, blood-pressure and temperature management.
- **Rehabilitation:** physical/occupational therapy for contractures and hypotonia; orthopedic management of club foot/contractures.
- **Genetic counseling** for the family.

**Pharmacogenomics / targeted / immunotherapy:** none applicable.

**Experimental / future therapeutics.** The most compelling proof-of-concept is **neuronal DST-a isoform gene restoration**: transgenic re-expression of neuronal dystonin isoform 2 (DST-a2) partially rescued the dt mouse and extended lifespan ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)). This nominates gene-replacement/gene-therapy strategies as a rational (though pre-clinical) direction. No registered clinical trials (NCT) for HSAN-VI–specific therapies are established.

---

## 13. Prevention

Because HSAN-VI is Mendelian with no environmental component, prevention is **reproductive/genetic**, not lifestyle-based.

- **Primary prevention:** genetic counseling for at-risk couples (especially consanguineous families); carrier testing.
- **Secondary prevention:** prenatal diagnosis and preimplantation genetic testing (PGT) once familial variants are identified; cascade testing of relatives.
- **Tertiary prevention:** vigilant supportive care to prevent complications (corneal protection, aspiration precautions, wound/injury prevention, autonomic monitoring).
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

**Model species / orthologs.** The mouse ortholog *Dst* (dystonin/Bpag1; NCBI Gene 13518) is the basis of the naturally occurring and engineered **dystonia musculorum (dt)** mutant. The gene and its cytolinker function are evolutionarily conserved across mammals. No significant naturally occurring companion-animal or wildlife disease equivalent to human HSAN-VI has been prominently reported; the mouse is the dominant natural/genetic model. Evolutionary conservation of the actin–intermediate-filament linker function is demonstrated by the phenotypic parallels between mouse and human ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)).

**Zoonotic potential / transmission.** None (non-communicable genetic disease).

---

## 15. Model Organisms

**Primary model — the dystonia musculorum (dt) mouse.** Homozygous *Dst*-mutant mice phenocopy HSAN-VI, exhibiting progressive limb contractures, dystonia, ataxia, dysautonomia, and early postnatal death (~4 weeks) ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)):

> "Phenotypically, dt mice are similar to HSAN-VI patients, manifesting progressive limb contractures, dystonia, dysautonomia and early postnatal death."

**Model types available.** A rich allelic series exists, disrupting different Dst isoform combinations:
- Classical spontaneous alleles (e.g., **Dst-dt-27J**) disrupting A1/A2/A3 → severe disease.
- Milder alleles (e.g., **Dst-dt-Tg4**) where **Dst-A3 upregulation** maintains tubulin acetylation and microtubule stability → less severe phenotype ([PMID: 29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/)):

  > "Maintenance of microtubule stability in Dstdt-Tg4 dorsal root ganglia could be attributed to an upregulation in Dst-A3 expression as a compensation for the absence of Dst-A1 and -A2 in Dstdt-Tg4 sensory neurons."

- **Gene-trap alleles** disrupting actin-binding-domain isoforms, with LacZ reporter for expression mapping ([PMID: 25195653](https://pubmed.ncbi.nlm.nih.gov/25195653/)).
- **Conditional / cell-type-specific** models dissecting contributions: Schwann-cell-specific loss → late-onset neuropathy and sensory ataxia with hypomyelination ([PMID: 32445516](https://pubmed.ncbi.nlm.nih.gov/32445516/)); afferent-circuit disruption → cardiac arrhythmia ([PMID: 42028226](https://pubmed.ncbi.nlm.nih.gov/42028226/)); GI-focused analysis → slowed motility, thinned colon mucus, altered microbiota ([PMID: 31814231](https://pubmed.ncbi.nlm.nih.gov/31814231/)).
- **Rescue model:** transgenic neuronal DST-a2 re-expression partially rescues and extends lifespan ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)).

**Phenotype recapitulation.** Excellent — the dt mouse reproduces the sensory-autonomic neuropathy, DRG degeneration, cytoskeletal/transport defects, autophagy and ER stress phenotypes, and dysautonomia (cardiac, GI). **Limitations:** motor/dystonic and cerebellar features are more prominent in mouse; species differences in isoform expression and lifespan; the human severe fetal (LCCS12) end is not fully captured by every allele.

**Patient-derived in vitro models.** Patient fibroblasts show defective actin cytoskeleton organization, delayed adhesion/spreading/migration, and recombinant p.Ala203Glu dystonin that cannot bind actin ([PMID: 30371979](https://pubmed.ncbi.nlm.nih.gov/30371979/)):

> "Functional studies showed defects in actin cytoskeleton organization and consequent delayed cell adhesion, spreading and migration, while recombinant p.Ala203Glu dystonin loses the ability to bind actin."

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF variant in neuronal DST-a isoforms (chr6p12.1)
                          │
                          ▼
     Loss of dystonin-a cytolinker in sensory/autonomic neurons
                          │
                          ▼
  Failure to cross-link  actin ── neurofilament ── microtubule
                          │
        ┌─────────────────┼──────────────────┬───────────────────┐
        ▼                 ▼                  ▼                   ▼
  Cytoskeletal       Impaired fast       ER stress /         Impaired
  disorganization    axonal transport    nuclear-envelope    autophagy
  (α-internexin      (ortho + retro)     dysfunction         (↑LC3-II)
   aggregation)
        │                 │                  │                   │
        └─────────────────┴──────────────────┴───────────────────┘
                          ▼
        Microtubule instability (↓tubulin acetylation)
        [Modifier: residual DST-A3 stabilizes microtubules → milder disease]
                          ▼
        Progressive DRG sensory + autonomic neuron degeneration
        (selective loss of NT-3/GDNF-responsive neurons; caspase-3)
                          │
        ┌─────────────────┴───────────────────┐
        ▼                                      ▼
  SENSORY branch                        AUTONOMIC branch
  pain insensitivity, areflexia,        alacrima, labile BP/temp,
  sensory ataxia, painless ulcers       arrhythmia, GI dysmotility,
  (+ muscle-spindle loss → hypotonia)   respiratory/feeding failure
```

The unifying interpretation is that HSAN-VI is a **cytoskeletal-linker (spectraplakin) disease of neurons**: dystonin-a is the physical bridge that holds the three neuronal cytoskeletal systems together, and its loss causes structural collapse of the axon with secondary failures of transport, organelle homeostasis, and quality control (autophagy). Sensory and autonomic neurons — with their long axons and high transport demands — are selectively vulnerable. The **isoform-graded severity** (which DST-a isoforms are lost, with DST-A3 as a built-in protective modifier) elegantly explains the clinical spectrum and is the central prognostic and therapeutic insight.

---

## Evidence Base

| PMID | Contribution | Type |
|------|-------------|------|
| [40938507](https://pubmed.ncbi.nlm.nih.gov/40938507/) | Defines OMIM ID, AR inheritance, core phenotype, causal gene, patient count (~15) | Human clinical |
| [40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/) | Establishes DST four-disorder allelic series; variant position predicts phenotype | Human clinical + molecular |
| [35276021](https://pubmed.ncbi.nlm.nih.gov/35276021/) | Distinguishes DST/BPAG1 loss in HSAN-VI vs EBS; plakin-domain variant ablates all isoforms | Human clinical |
| [37431644](https://pubmed.ncbi.nlm.nih.gov/37431644/) | Severe congenital end (arthrogryposis); hypomyelination + reduced fiber density | Human clinical |
| [30371979](https://pubmed.ncbi.nlm.nih.gov/30371979/) | Patient-cell actin cytoskeleton defect; p.Ala203Glu loses actin binding | In vitro / human |
| [34897952](https://pubmed.ncbi.nlm.nih.gov/34897952/) | Isoform structure (a/b/e); novel homozygous consanguineous variant | Human clinical |
| [24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/) | dt mouse phenocopies HSAN-VI; DST-a2 transgene rescue | Model organism |
| [11241383](https://pubmed.ncbi.nlm.nih.gov/11241383/) | Selective vulnerability of NT-3/GDNF-responsive neurons | Model organism |
| [29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/) | DST-A3 upregulation preserves microtubule stability → milder disease (modifier) | Model organism |
| [12859670](https://pubmed.ncbi.nlm.nih.gov/12859670/) | Impaired orthograde + retrograde fast axonal transport | Model organism |
| [26043942](https://pubmed.ncbi.nlm.nih.gov/26043942/) | Impaired autophagic flux (↑LC3-II) | Model organism |
| [18638474](https://pubmed.ncbi.nlm.nih.gov/18638474/) | ER stress / ER–nuclear-envelope dysfunction in DRG neurons | Model organism |
| [16691115](https://pubmed.ncbi.nlm.nih.gov/16691115/) | α-internexin aggregation, caspase-3 activation → apoptosis mechanism | Model organism |
| [8752219](https://pubmed.ncbi.nlm.nih.gov/8752219/) | Establishes BPAG1n as actin–IF cytolinker; axonal architecture perturbed in null mice | Model organism |
| [9242412](https://pubmed.ncbi.nlm.nih.gov/9242412/) | Postnatal-restricted pathology; muscle-spindle degeneration → ataxia | Model organism |
| [32445516](https://pubmed.ncbi.nlm.nih.gov/32445516/) | Schwann-cell-specific Dst loss → late-onset neuropathy, sensory ataxia | Model organism |
| [42028226](https://pubmed.ncbi.nlm.nih.gov/42028226/) | Afferent-circuit disruption → cardiac arrhythmia (autonomic mechanism) | Model organism |
| [31814231](https://pubmed.ncbi.nlm.nih.gov/31814231/) | GI pathology: slowed motility, thinned mucus, altered microbiota | Model organism |
| [25195653](https://pubmed.ncbi.nlm.nih.gov/25195653/) | Gene-trap model; actin-binding-domain isoform loss → dt; CNS circuit involvement | Model organism |
| [42563873](https://pubmed.ncbi.nlm.nih.gov/42563873/) | Diagnostic odyssey; genetic testing yields diagnosis after negative panels | Human clinical |
| [37603210](https://pubmed.ncbi.nlm.nih.gov/37603210/) | Review of tissue-specific DST isoform roles (neural/muscle/skin) | Review |
| [26778567](https://pubmed.ncbi.nlm.nih.gov/26778567/) | Overview of neuronal BPAG1 isoform structure/function | Review |

**Consistency of evidence.** The mechanistic model is strongly convergent: multiple independent mouse studies (transport, autophagy, ER stress, cytoskeleton, cell-type-specific and autonomic) and human patient/cell data all point to a single unifying cytolinker-loss mechanism. No study in the reviewed corpus contradicts the core model.

---

## Limitations and Knowledge Gaps

- **Ultra-rarity:** With only ~15 reported patients, human genotype–phenotype data are sparse; frequency estimates for individual phenotypes are qualitative rather than precise percentages, and no formal prevalence/incidence figures exist.
- **Mechanistic inference from mouse:** Much of the causal chain (transport, autophagy, ER stress, autonomic circuits) is demonstrated in the dt mouse and inferred to hold in humans; direct human tissue confirmation is limited.
- **No human natural-history study or validated quality-of-life instrument** is available; prognostic granularity relies on molecular genotype.
- **No epigenetic, biomarker, or metabolomic signature** has been defined for HSAN-VI.
- **Therapeutics are pre-clinical:** gene-restoration rescue is shown only in mouse; no human trials.
- **Isoform-level diagnostics** require careful, position-aware variant interpretation not universally standardized across laboratories.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international HSAN-VI patient registry** to aggregate genotype–phenotype data, define phenotype frequencies quantitatively, and support natural-history studies — directly addressing the call in [PMID: 42563873](https://pubmed.ncbi.nlm.nih.gov/42563873/) for collective analysis.
2. **Systematic isoform-resolution variant curation** in *DST*: build a locus-specific database mapping variant position → affected isoform(s) → predicted disorder (HSAN-VI / EBS3 / CMYO29 / LCCS12) to operationalize the prediction framework from [PMID: 40497796](https://pubmed.ncbi.nlm.nih.gov/40497796/).
3. **Advance neuronal DST-a gene-replacement therapy** from the dt-mouse proof-of-concept ([PMID: 24381311](https://pubmed.ncbi.nlm.nih.gov/24381311/)) toward AAV/gene-editing preclinical programs, testing the early-postnatal critical window.
4. **Test DST-A3 up-modulation** as a therapeutic strategy, given its natural protective effect on microtubule stability ([PMID: 29982604](https://pubmed.ncbi.nlm.nih.gov/29982604/)).
5. **Human iPSC-derived sensory/autonomic neuron models** from patient variants to confirm the mouse-derived causal chain (transport, autophagy, ER stress) in human cells.
6. **Autonomic phenotyping protocols** (cardiac rhythm, thermoregulation, GI motility) for patients, guided by the mouse circuit findings ([PMID: 42028226](https://pubmed.ncbi.nlm.nih.gov/42028226/), [PMID: 31814231](https://pubmed.ncbi.nlm.nih.gov/31814231/)), to standardize monitoring and complication prevention.
7. **Formalize corneal-protection and injury-prevention care pathways**, given the high morbidity from alacrima, absent corneal reflex, and pain insensitivity.

---

*Report compiled from 5 iterations, 8 confirmed findings, and 25 reviewed papers. Identifiers verified against MONDO/OLS, OMIM, Orphanet, HGNC, Ensembl, UniProt, gnomAD, ClinVar, and HPO/JAX.*


## Artifacts

- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_6-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 32 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013839` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hereditary sensory and autonomic neuropathy type 6**
- `DOID:0070151` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **hereditary sensory and autonomic neuropathy type 6**
- `GO:0030424` (2 mentions) - the report calls it "Cellular component:* axon"; GO calls it **axon**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000763` (1 mention) - the report calls it "Sensory neuropathy / pain insensitivity"; HP calls it **Sensory neuropathy**
- `HP:0000522` (1 mention) - the report calls it "Alacrima (reduced tears)"; HP calls it **Alacrima**
- `HP:0000822` (1 mention) - the report calls it "Hypertension / labile BP"; HP calls it **Hypertension**
- `HP:0033031` (1 mention) - the report calls it "Hyperpyrexia / temperature instability"; HP calls it **Hyperpyrexia**
- `HP:0001762` (1 mention) - the report calls it "Talipes equinovarus (club foot)"; HP calls it **Talipes equinovarus**
- `HP:0000007` (2 mentions) - the report calls it "Autosomal recessive inheritance", "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `GO:0008017` (1 mention) - the report calls it "Molecular function:* microtubule binding"; GO calls it **microtubule binding**
- `GO:0008090` (1 mention) - the report calls it "Biological process:* retrograde axonal transport"; GO calls it **retrograde axonal transport**
- `UBERON:0000044` (1 mention) - the report calls it "dorsal root ganglia"; UBERON calls it **dorsal root ganglion**, and lists "dorsal root ganglia" among its other names
- `UBERON:0001555` (1 mention) - the report calls it "Gastrointestinal tract"; UBERON calls it **digestive tract**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Autosomal recessive inheritance", "Autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `GARD`, `OMIM`.
