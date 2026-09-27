---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T19:27:21.820880'
end_time: '2026-09-24T19:43:41.854282'
duration_seconds: 980.03
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: MyD88 Deficiency
  mondo_id: MONDO:0012839
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
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0012839
    reported_labels:
    - if available
    ontology_label: pyogenic bacterial infections due to MyD88 deficiency
  - term_id: NCIT:C15617
    reported_labels:
    - Antibiotic Therapy
    - "At the *first* suspicion of infection, given the blunted warning signs \u2014\
      \ the single most important acute intervention"
    ontology_label: Monoclonal Antibody 17-1A/sargramostim
  - term_id: NCIT:C603
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Isotretinoin
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MyD88_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MyD88_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MyD88 Deficiency
- **MONDO ID:** MONDO:0012839 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MyD88 Deficiency** covering all of the
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

# MyD88 Deficiency (MONDO:0012839): Comprehensive Disease Characteristics Report

## Summary

**MyD88 deficiency is a rare autosomal recessive inborn error of immunity (primary immunodeficiency) caused by biallelic germline loss-of-function mutations in *MYD88* (chromosome 3p22.2), the intracellular adaptor protein that nucleates the "Myddosome" signaling complex downstream of most Toll-like receptors (TLRs) and all interleukin-1 receptor (IL-1R) family receptors.** Loss of MyD88 abolishes NF-κB– and MAPK-driven pro-inflammatory signaling through these receptors, producing a strikingly *narrow* clinical phenotype: patients suffer early-onset, recurrent, and often life-threatening **invasive pyogenic bacterial infections**, overwhelmingly dominated by *Streptococcus pneumoniae*, while retaining normal resistance to most viruses, fungi, parasites, and the vast majority of bacteria. The disease is clinically indistinguishable from IRAK-4 deficiency, its immediate downstream kinase partner.

A defining and clinically dangerous feature is a **weak or delayed systemic inflammatory response** (low or absent fever, low CRP) even during overwhelming invasive infection, which undermines early clinical detection and drives mortality. The natural history is bimodal in risk: mortality is highest in the first years of life (first invasive infection before age 2 in ~88% of patients, neonatal in ~33%), and outcomes improve markedly with age as adaptive immunity progressively compensates. More recent work has expanded the recognized phenotype beyond pyogenic bacteria to include a substantially increased risk of **hypoxemic COVID-19 pneumonia** (mediated by defective TLR7-dependent type I interferon production in plasmacytoid dendritic cells) and a selective defect in **T-independent anti-polysaccharide IgM** antibody responses linked to reduced marginal-zone-like B cells.

Management is preventive and supportive: **lifelong antibiotic prophylaxis, pneumococcal (and other) vaccination, immunoglobulin replacement, and aggressive empirical antibiotics** at the first suspicion of infection. There is no approved gene-specific or curative therapy in routine use. This report synthesizes 8 confirmed findings drawn from 24 reviewed papers, spanning the disease's genetics, mechanism, clinical spectrum, epidemiology, diagnostics, prognosis, treatment, and its mouse model, and maps them onto the 15-section disease-characteristics template.

---

## Key Findings

### Finding 1 — A narrow but lethal pyogenic-infection immunodeficiency

MyD88 deficiency was first defined by **von Bernuth et al. (Science 2008)** in nine children from unrelated kindreds carrying autosomal recessive *MYD88* loss-of-function alleles. These patients experienced *"life-threatening, often recurrent pyogenic bacterial infections, including invasive pneumococcal disease"* yet were *"otherwise healthy, with normal resistance to other microbes"* ([PMID: 18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/)). The mechanistic conclusion drawn from this experiment of nature was that *"the MyD88-dependent TLRs and IL-1Rs are therefore essential for protective immunity to a small number of pyogenic bacteria, but redundant for host defense to most natural infections."* This redundancy — surprising given the central position of MyD88 in innate immunity — is the single most important conceptual takeaway of the disease and stands in sharp contrast to the broad susceptibility seen in the mouse knockout (Finding 6). The corresponding OMIM entry is **#612260**.

### Finding 2 — Clinical cohort: pneumococcus dominates, inflammation is blunted, onset is early, early mortality is high

The largest natural-history study, **Picard et al. (Medicine 2010)**, pooled 48 IRAK-4– and 12 MyD88-deficient patients across 37 kindreds in 15 countries and found the two disorders **clinically indistinguishable** ([PMID: 21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/)). Key quantitative features:

| Feature | Value |
|---|---|
| Invasive pneumococcal disease | 41/60 patients (**68%**) — *"The leading threat was invasive pneumococcal disease"* |
| *Pseudomonas aeruginosa* invasive infection | ~16% |
| *Staphylococcus aureus* invasive infection | ~16% |
| First invasive infection before age 2 | **88.3%** (53/60) |
| First invasive infection in neonatal period | **32.7%** (19/60) |
| Deaths | 24 total; 10 during the first invasive episode |
| Recurrent invasive infection among survivors | **72%** |
| Systemic inflammation | *"usually weak or delayed"* |

The blunted inflammatory response — *"Systemic signs of inflammation were usually weak or delayed"* — is pathognomonic and clinically treacherous: patients can be severely septic with minimal fever or CRP elevation. Crucially, **outcome improves with age**, indicating that adaptive immunity (antibody-mediated and other MyD88-independent mechanisms) progressively substitutes for the missing innate pathway.

### Finding 3 — Mechanism: MyD88 nucleates the Myddosome

The molecular lesion sits at the apex of a defined signaling complex. **Lin, Lo & Wu (Nature 2010)** solved the crystal structure of the MyD88–IRAK4–IRAK2 death-domain (DD) complex, revealing a **left-handed helical oligomer of 6 MyD88, 4 IRAK4, and 4 IRAK2 death domains** ([PMID: 20485341](https://pubmed.ncbi.nlm.nih.gov/20485341/)). Assembly is strictly hierarchical: *"MyD88 recruits IRAK4 and the MyD88-IRAK4 complex recruits the IRAK4 substrates IRAK2 or the related IRAK1. Formation of these Myddosome complexes brings the kinase domains of IRAKs into proximity for phosphorylation and activation."* This structural understanding explains why the loss of the single upstream adaptor is catastrophic for the whole pathway, and why MyD88 and IRAK-4 deficiencies are phenotypically identical.

Functional validation of patient variants comes from **George et al. (2011)**, who showed that the death-domain missense variants **S34Y and R98C** *"showed severely reduced NF-κB activation due to reduced homo-oligomerization and IRAK4 interaction"* ([PMID: 20966070](https://pubmed.ncbi.nlm.nih.gov/20966070/)). This directly links specific pathogenic alleles to a defect in Myddosome nucleation and downstream NF-κB output.

### Finding 4 — Expanded phenotype: hypoxemic COVID-19 via impaired pDC type I IFN

**García-García et al. (J Exp Med 2023)** reported 22 unvaccinated MyD88- or IRAK-4-deficient patients infected with SARS-CoV-2 (17 kindreds, 8 countries); 16 were hospitalized (6 moderate, 4 severe, 6 critical, 1 death). Risk of hypoxemic pneumonia **increased with age**, and the odds ratio for requiring invasive mechanical ventilation versus general-population controls was a striking **74.7 (95% CI 26.8–207.8, P<0.001)** ([PMID: 36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/)). The authors note these patients *"were long thought to be selectively vulnerable to pyogenic bacteria, but also have a high risk of hypoxemic COVID-19 pneumonia,"* attributable to *"impaired TLR7-dependent type I IFN production by pDCs, which do not sense SARS-CoV-2 correctly."* This finding is mechanistically important because it demonstrates a specific viral vulnerability arising from the loss of the endosomal-TLR7 → MyD88 → type I IFN axis in plasmacytoid dendritic cells, complementing the classical bacterial phenotype.

### Finding 5 — Humoral defect: impaired T-independent IgM and reduced marginal-zone-like B cells

**Maglione et al. (J Immunol 2014)** demonstrated a B-cell/antibody component to the disease: *"patients with IRAK-4 and MyD88 deficiencies have reduced serum IgM, but not IgG antibody, recognizing T-independent bacterial antigens"* and *"have fewer immunoglobulin M (IgM)⁺IgD⁺CD27⁺ B cells"* ([PMID: 25320238](https://pubmed.ncbi.nlm.nih.gov/25320238/)). Specific IgM quantity correlated with the frequency of this marginal-zone-like B-cell subset, and patient cells showed impaired TLR7/TLR9-induced proliferation of this population. This provides a satisfying mechanistic link between the innate signaling defect and susceptibility to **encapsulated (polysaccharide-coated) pyogenic bacteria** such as *S. pneumoniae*, whose control depends heavily on rapid T-independent anti-polysaccharide IgM.

### Finding 6 — The mouse model: broad TLR/IL-1 defect, but broader infection susceptibility than humans

**Adachi/Akira et al. (Immunity 1998)** generated *Myd88⁻/⁻* mice, establishing the foundational model. These mice *"have defects in T cell proliferation as well as induction of acute phase proteins and cytokines in response to IL-1"* and abolished IL-18-induced IFN-γ, NK activity, and NF-κB/JNK activation, confirming that *"MyD88 is a critical component in the signaling cascade that is mediated by IL-1 receptor as well as IL-18 receptor"* ([PMID: 9697844](https://pubmed.ncbi.nlm.nih.gov/9697844/)). Importantly, later *Myd88⁻/⁻* studies revealed susceptibility to a *broad* range of pathogens — a notable **species discordance** with the narrow human phenotype. This discordance is itself a scientifically important observation: it implies redundancy mechanisms operate differently (or more robustly) in humans, and it is a key limitation for translating mouse findings.

### Finding 7 — Management: prophylaxis and vigilance help, but breakthrough disease remains lethal

The therapeutic reality is captured by **McKelvie et al. (2014)**, a case of an IRAK-4-deficient girl (clinically identical to MyD88 deficiency) *"managed with antibiotic prophylaxis (sulfa/trimethoprim/PenV, then - due to neutropenia - Cefprozil), pneumococcal vaccination (PCV-7, Pneumovax23, PCV-13) and vigilance"* ([PMID: 24596024](https://pubmed.ncbi.nlm.nih.gov/24596024/)). She remained infection-free for six years with satisfactory (but short-lived) IgG responses to pneumococcal polysaccharide — yet **died within 24 hours** of an insidious *S. pneumoniae* serotype 6C meningitis presenting with only a low fever. The case crystallizes the central danger: *"IRAK-4 deficiency causes IL-1R and TLR signaling failure, resulting in minimal clinical features despite invasive bacterial infection."* Prophylaxis reduces but does not eliminate the risk of fulminant, clinically silent invasive disease.

### Finding 8 — Genetic basis: biallelic germline LoF *MYD88*, the mechanistic opposite of somatic *MYD88* L265P

The disease is caused by **biallelic germline loss-of-function variants in *MYD88*** (HGNC:7562; NCBI Gene 4615; locus 3p22.2). MyD88 is a 296-amino-acid adaptor with an N-terminal death domain and a C-terminal TIR (Toll/IL-1R) domain. First-described alleles are **private and heterogeneous** point mutations and small deletions (e.g., E52del, L93P, R196C) ([PMID: 18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/)). Death-domain missense variants S34Y and R98C abolish signaling by impairing homo-oligomerization and IRAK4 recruitment ([PMID: 20966070](https://pubmed.ncbi.nlm.nih.gov/20966070/); *"human individuals carrying rare, naturally occurring MYD88 point mutations suffer from reoccurring life-threatening infections"*). Critically, these germline LoF variants are the **mechanistic opposite** of the recurrent *somatic activating* **MYD88 L265P** mutation that constitutively drives NF-κB in B-cell lymphomas (Waldenström macroglobulinemia, ABC-DLBCL) — a distinction essential for correct interpretation of any *MYD88* variant.

---

## The 15-Section Disease Characteristics Report

### 1. Disease Information

MyD88 deficiency is a rare **autosomal recessive primary immunodeficiency / inborn error of immunity** in which loss of the MyD88 adaptor protein cripples signaling through most TLRs and all IL-1R-family receptors, producing selective vulnerability to a small set of pyogenic bacteria (chiefly *Streptococcus pneumoniae*).

- **Key identifiers:** OMIM **#612260**; MONDO:**0012839**; the *MYD88* gene is HGNC:7562 / NCBI Gene 4615 / OMIM *602170. (Orphanet, ICD-10/ICD-11, and MeSH identifiers were not independently verified in this investigation and should be confirmed against those resources; the disorder falls under the IUIS category "Defects in intrinsic and innate immunity.")
- **Synonyms / alternative names:** MyD88 deficiency; MYD88 deficiency; recurrent pyogenic bacterial infections due to MyD88 deficiency; myeloid differentiation primary response 88 deficiency. It is frequently grouped clinically with its phenocopy, **IRAK-4 deficiency**.
- **Information source:** Knowledge derives from **aggregated disease-level resources** — small international case series and cohorts (e.g., von Bernuth 2008; Picard 2010) rather than large EHR datasets, reflecting the disorder's rarity.

### 2. Etiology

- **Disease causal factor:** Purely **genetic** — biallelic germline loss-of-function variants in *MYD88* (Finding 8). The clinical *manifestations* are triggered by **infection** (encapsulated pyogenic bacteria; and SARS-CoV-2), so the phenotype is a gene × pathogen interaction.
- **Genetic risk factors:** The causal variants themselves; no established common susceptibility loci or modifier genes are documented for this Mendelian disorder. **Consanguinity** raises the risk of homozygosity (autosomal recessive).
- **Environmental risk factors:** Exposure to invasive pyogenic bacteria (especially *S. pneumoniae*, *P. aeruginosa*, *S. aureus*) and to SARS-CoV-2. **Age** is a major modifier — risk of severe bacterial disease is highest in early childhood, whereas COVID-19 risk *increases* with age (Findings 2, 4).
- **Protective factors:** **Maturation of adaptive immunity with age** is the principal protective factor for bacterial disease (outcomes improve with age; Finding 2). Acquired pathogen-specific antibodies (vaccine- or infection-induced) can partially substitute for the missing innate pathway — analogous to the antibody-mediated rescue described in TIRAP deficiency ([PMID: 28235196](https://pubmed.ncbi.nlm.nih.gov/28235196/)).
- **Gene–environment interaction:** The disease is a textbook example — a fixed genetic lesion produces catastrophic disease only upon encounter with a specific narrow set of pathogens, while most microbial exposures are handled normally via redundant (MyD88-independent) pathways.

### 3. Phenotypes

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Recurrent invasive pyogenic bacterial infection | Clinical sign | Neonatal–early childhood | Severe/life-threatening | ~72% recurrent in survivors | HP:0006532 / HP:0002718 (recurrent bacterial infections) |
| Invasive pneumococcal disease (sepsis, meningitis) | Clinical sign | Early childhood | Severe | 68% | HP:0032262 (streptococcal infection); HP:0001287 (meningitis) |
| Blunted / weak systemic inflammatory response (low fever, low CRP) | Lab/clinical sign | From onset | Characteristic | "usually weak or delayed" | HP:0011947 (abnormal inflammatory response); HP:0001945 (fever) — often *absent* |
| Hypoxemic COVID-19 pneumonia | Clinical sign | Age-increasing | Moderate–critical | 16/22 hospitalized in reported cohort | HP:0002090 (pneumonia); HP:0012418 (hypoxemia) |
| Reduced serum IgM to T-independent antigens | Lab abnormality | Constitutional | Selective | Consistent | HP:0002850 (decreased circulating IgM) |
| Skin/soft-tissue infections, abscesses | Clinical sign | Childhood | Variable | Common | HP:0025084; HP:0001880 |

Symptom progression is **episodic** (discrete invasive infection episodes) superimposed on a lifelong constitutional immune defect. **Quality-of-life impact** derives from recurrent hospitalizations, need for lifelong prophylaxis, infection-related sequelae (e.g., post-meningitic neurological damage), and the psychological burden of unpredictable, rapidly fatal infections; disease-specific QoL instruments have not been applied in this rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** ***MYD88*** (HGNC:7562; NCBI Gene 4615; 3p22.2; OMIM *602170). Protein: 296-aa adaptor, N-terminal **death domain** + C-terminal **TIR domain**.
- **Pathogenic variants:** Private, heterogeneous — point mutations and small deletions. Examples: **E52del, L93P, R196C** (von Bernuth 2008), and death-domain missense **S34Y, R98C** (George 2011). Variant **classification:** pathogenic/likely pathogenic per functional and ACMG evidence.
- **Variant types:** missense, small in-frame deletion, nonsense, and splice/frameshift — all converging on **loss of function**.
- **Allele frequency:** Individually **very rare/private** in population databases (gnomAD); biallelic genotypes are exceedingly rare.
- **Origin & functional consequence:** **Germline, loss-of-function** (impaired Myddosome assembly / NF-κB activation). This contrasts categorically with the **somatic gain-of-function MYD88 L265P** of B-cell lymphomas (Finding 8).
- **Modifier genes / epigenetics / chromosomal abnormalities:** No established disease-specific modifier genes, epigenetic marks, or large chromosomal rearrangements are documented; the disorder is monogenic and point-mutation driven.

### 5. Environmental Information

- **Infectious agents (central):** *Streptococcus pneumoniae* (dominant), *Pseudomonas aeruginosa*, *Staphylococcus aureus*; and **SARS-CoV-2** (hypoxemic pneumonia). NCBI Taxonomy: *S. pneumoniae* txid1313; *P. aeruginosa* txid287; *S. aureus* txid1280; SARS-CoV-2 txid2697049.
- **Environmental toxins / occupational exposures / lifestyle factors:** No established role; the disease is not driven by toxins, radiation, smoking, diet, or pollution. The relevant "environmental" exposure is microbial.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic germline loss-of-function mutation in *MYD88*** (e.g., S34Y, R98C, E52del) **leads to** absent or non-functional MyD88 adaptor protein. *(demonstrated — Findings 1, 8)*
2. Absent functional MyD88 **prevents nucleation of the Myddosome** (the 6:4:4 MyD88–IRAK4–IRAK2/1 death-domain helical oligomer), because MyD88's death domain can no longer homo-oligomerize or recruit IRAK4. *(demonstrated — Findings 3, 8)*
3. Failure of Myddosome assembly **prevents IRAK4-mediated phosphorylation/activation of IRAK1/2**, **which results in** failure to activate TRAF6 → IKK → **NF-κB** and **MAPK** cascades. *(demonstrated — Finding 3)*
4. Loss of NF-κB/MAPK output **abolishes downstream signaling from most TLRs (except TLR3 and partly TLR4) and all IL-1R-family receptors (IL-1R, IL-18R, IL-33R)**, **leading to** failure to produce pro-inflammatory cytokines (IL-6, TNF, IL-1β amplification) and acute-phase responses. *(demonstrated — Findings 1, 6)*

   **Branch A — Innate myeloid/epithelial defense (bacterial):**
   5A. Impaired TLR/IL-1R signaling in macrophages, neutrophils, dendritic and epithelial cells **results in** defective early recognition and clearance of pyogenic, encapsulated bacteria, and a **weak/delayed systemic inflammatory response**. *(demonstrated — Findings 1, 2)*
   6A. **Leads to** recurrent, rapidly progressive, clinically silent **invasive pyogenic bacterial disease** (pneumococcal sepsis/meningitis). *(demonstrated — Findings 2, 7)*

   **Branch B — Humoral/marginal-zone defect (bacterial):**
   5B. Loss of TLR7/TLR9 signaling in B cells **reduces the marginal-zone-like IgM⁺IgD⁺CD27⁺ B-cell pool** and **impairs T-independent anti-polysaccharide IgM**. *(demonstrated — Finding 5)*
   6B. **Contributes to** impaired control of polysaccharide-encapsulated bacteria (esp. *S. pneumoniae*). *(inferred link to Branch A phenotype — Finding 5)*

   **Branch C — Antiviral pDC defect (SARS-CoV-2):**
   5C. Loss of endosomal **TLR7 → MyD88 signaling in plasmacytoid dendritic cells** **impairs type I interferon production** upon SARS-CoV-2 sensing. *(demonstrated — Finding 4)*
   6C. **Results in** increased risk of **hypoxemic COVID-19 pneumonia** (OR for invasive ventilation ≈ 74.7). *(demonstrated — Finding 4)*

7. **Compensation:** With age, maturation of MyD88-independent adaptive immunity (pathogen-specific antibody) **progressively substitutes**, **leading to** improving bacterial-infection outcomes over time. *(demonstrated — Finding 2)*

**Molecular pathways:** TLR/IL-1R signaling → MyD88 → IRAK4 → IRAK1/2 → TRAF6 → TAK1 → IKK → **NF-κB**; parallel **MAPK/JNK/p38** activation; endosomal **TLR7 → IRF7 → type I IFN** (in pDCs). (KEGG "Toll-like receptor signaling pathway" hsa04620; Reactome "MyD88 cascade initiated on plasma membrane" R-HSA-166058.)
**Cellular processes:** innate immune inflammation, cytokine production, phagocyte activation/killing, B-cell proliferation.
**Immune involvement:** **immunodeficiency** (not autoimmunity); combined innate-signaling and T-independent humoral defect.
**Suggested GO terms:** GO:0002755 (MyD88-dependent toll-like receptor signaling pathway), GO:0007249 (I-κB kinase/NF-κB signaling), GO:0032760 (positive regulation of TNF production), GO:0045087 (innate immune response), GO:0006954 (inflammatory response).
**Suggested CL terms:** CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000784 (plasmacytoid dendritic cell), CL:0000787 (memory B cell / marginal-zone-like B cell), CL:0000236 (B cell).

### 7. Anatomical Structures Affected

- **Organ / body-system level:** The **immune/hematopoietic system** is primary. Clinically affected organs reflect sites of invasive infection: **lungs** (pneumonia — UBERON:0002048), **meninges/CNS** (meningitis — UBERON:0002360; UBERON:0000955), **bloodstream** (sepsis — UBERON:0000178), **skin and soft tissue** (abscesses — UBERON:0002097), **bone/joints** (osteomyelitis/arthritis). Secondary involvement includes post-meningitic neurological sequelae.
- **Tissue / cell level:** Myeloid phagocytes (macrophages CL:0000235, neutrophils CL:0000775), dendritic cells including pDCs (CL:0000784), and B-lymphocyte subsets (marginal-zone-like B cells). Epithelial barriers (airway epithelium) also rely on MyD88 for defense.
- **Subcellular level:** Signaling occurs at the **plasma membrane and endosomal membranes** (TLRs) and in the **cytoplasm** (Myddosome assembly, NF-κB pathway). Suggested GO cellular-component terms: GO:0010008 (endosome membrane), GO:0005886 (plasma membrane), GO:0005829 (cytosol).
- **Lateralization:** Not applicable — a systemic immune defect; infection sites vary.

### 8. Temporal Development

- **Onset:** Typically **neonatal to early childhood**. First invasive infection before age 2 in **88.3%**, neonatal in **32.7%** (Finding 2). Onset of individual episodes is **acute**, often fulminant.
- **Progression / course:** **Episodic** invasive infections on a **chronic, lifelong** constitutional immune deficiency. Recurrence in **72%** of survivors.
- **Critical period:** **Early childhood is the window of greatest vulnerability and highest mortality**; risk attenuates with age as adaptive immunity matures (a key window for intensive prophylaxis and vaccination). Notably, **COVID-19 risk trends in the opposite direction, increasing with age** (Finding 4).
- **Remission pattern:** No spontaneous remission of the underlying defect; "improvement" reflects age-dependent adaptive compensation and effective prophylaxis.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic germline LoF *MYD88*). **Consanguinity** increases risk. Heterozygous carriers are healthy.
- **Penetrance / expressivity:** High penetrance for susceptibility, but **variable expressivity** in infection frequency, severity, and age of first episode — partly explained by stochastic pathogen exposure and adaptive compensation.
- **Epidemiology:** **Ultra-rare.** The defining cohorts total only a few dozen patients worldwide (12 MyD88-deficient among 60 combined MyD88/IRAK-4 patients in the largest series; Finding 2). Precise prevalence/incidence figures are not established; it is best described as an "orphan" inborn error of immunity affecting far fewer than 1 in 1,000,000.
- **Population / geography:** Reported across many countries (15 in Picard 2010; 8 in García-García 2023) without a defined ethnic predilection; specific alleles are private/family-specific rather than founder mutations.
- **Sex ratio:** Autosomal (not X-linked); no strong sex bias documented.

### 10. Diagnostics

- **Laboratory / functional immunology:** The functional hallmark is **impaired pro-inflammatory cytokine production (e.g., IL-6, TNF) in response to TLR and IL-1R agonists** in whole blood/leukocytes/fibroblasts, with preserved responses to TLR3 and some TLR4 readouts. A **characteristically low CRP and blunted acute-phase response during invasive infection** is a critical (and dangerous) diagnostic clue (Findings 2, 7).
- **Immunoglobulins:** Reduced serum **IgM to T-independent polysaccharide antigens**; reduced IgM⁺IgD⁺CD27⁺ B cells on flow cytometry (Finding 5).
- **Microbiology / imaging:** Blood cultures, CSF studies, and imaging directed at the invasive site (chest imaging for pneumonia; MRI for meningitis).
- **Genetic testing (definitive):** **Sanger single-gene sequencing of *MYD88*, targeted immunodeficiency gene panels, or whole-exome/whole-genome sequencing** confirm biallelic LoF variants. Functional validation (NF-κB reporter, cytokine assays) supports variant classification. Given the phenocopy with IRAK-4 deficiency, panels should include *IRAK4*.
- **Differential diagnosis:** **IRAK-4 deficiency** (clinically indistinguishable — requires genetics to separate), other congenital neutropenias, complement deficiencies, asplenia/hyposplenism, antibody deficiencies (e.g., specific polysaccharide antibody deficiency), NEMO/IκBα defects, and TIRAP/IRAK-1 defects.
- **Screening:** No routine newborn screening exists (the TREC newborn screen for SCID does not detect this disorder). **Cascade/family genetic testing** is indicated once a proband variant is known.

### 11. Outcome / Prognosis

- **Mortality:** **High in early childhood.** In the Picard cohort, **24 deaths among 60 patients**, with **10 deaths during the first invasive episode** (Finding 2). Death can occur within 24 hours of an insidious presentation despite prophylaxis (Finding 7).
- **Age-dependent improvement:** **Outcome improves with age** as adaptive immunity compensates — the dominant prognostic factor.
- **Morbidity:** Recurrent invasive infections (72% of survivors), potential permanent sequelae (post-meningitic neurological deficits, hearing loss), and the burden of lifelong prophylaxis.
- **Prognostic factors:** Age (younger = worse for bacterial disease), timeliness of empirical antibiotic treatment, adherence to prophylaxis/vaccination, and — for COVID-19 — older age (worse). No validated molecular prognostic biomarker exists; the **blunted inflammatory response is itself an adverse feature** because it delays recognition.

### 12. Treatment

There is no approved gene-corrective or curative standard-of-care; management is **preventive and supportive** (Findings 2, 7):

| Modality | Details | Suggested NCIT |
|---|---|---|
| **Antibiotic prophylaxis** | Continuous (e.g., trimethoprim-sulfamethoxazole, penicillin V; alternatives such as cefprozil if cytopenias) | NCIT:C15617 (Antibiotic Therapy) |
| **Vaccination** | Pneumococcal conjugate + polysaccharide (PCV-7/PCV-13, PPSV23), plus *Haemophilus influenzae* type b, meningococcal | NCIT:C15346 (Vaccine Therapy) |
| **Immunoglobulin replacement (IVIG/SCIG)** | Provides passive pathogen-specific antibody, compensating for defective T-independent IgM | NCIT:C603 (Immunoglobulin Therapy) |
| **Aggressive empirical antibiotics** | At the *first* suspicion of infection, given the blunted warning signs — the single most important acute intervention | NCIT:C15617 |
| **Patient/family education & vigilance** | Low threshold for medical evaluation; emergency antibiotic access | — |

- **Pharmacogenomics / targeted / gene / cell / RNA therapy:** No routine gene-specific, targeted, cell-, or RNA-based therapy is established. **Hematopoietic stem cell transplantation** is not standard given age-dependent improvement, though it is conceptually curative for the hematopoietic defect. Gene therapy is discussed as a future prospect in the inborn-errors-of-immunity literature ([PMID: 41369391](https://pubmed.ncbi.nlm.nih.gov/41369391/)) but is not clinically available for this disorder.
- **Combination / personalized strategy:** The mainstay is a **combination** of prophylaxis + vaccination + immunoglobulin + rapid empirical treatment, individualized to infection history.

### 13. Prevention

- **Primary prevention:** Not possible for the genetic lesion; relevant primary prevention is against infection — **vaccination and antibiotic prophylaxis** (Finding 7).
- **Secondary prevention:** **Early detection of infection** despite blunted signs — heightened vigilance, family education, low threshold for cultures and empirical antibiotics.
- **Tertiary prevention:** Prevention of infection complications and recurrences through sustained prophylaxis and immunoglobulin replacement.
- **Genetic counseling / reproductive options:** For autosomal recessive disease with a known variant — **carrier testing, cascade screening, prenatal testing, and preimplantation genetic diagnosis** are available. Counseling on 25% recurrence risk for future pregnancies of carrier couples; consanguinity counseling.
- **Immunization is central:** Unlike many primary immunodeficiencies where live vaccines are contraindicated, polysaccharide/conjugate and inactivated vaccines are actively recommended here.

### 14. Other Species / Natural Disease

- **Taxonomy / orthology:** *MYD88* is highly conserved. Mouse *Myd88* (NCBI Gene 17874; *Mus musculus* txid10090) is the principal experimental ortholog; orthologs exist across vertebrates.
- **Natural disease in other species:** No well-characterized naturally occurring MyD88-deficiency disease in companion animals or wildlife is documented in this investigation; the animal knowledge base is essentially the **engineered mouse knockout** (Finding 6), not spontaneous veterinary disease.
- **Comparative pathology / evolutionary conservation:** The MyD88 → IRAK → NF-κB module is evolutionarily ancient and broadly conserved. However, there is a **notable human–mouse phenotypic discordance**: *Myd88⁻/⁻* mice show *broad* infection susceptibility, whereas humans show a *narrow* pyogenic-bacterial phenotype (Finding 6), indicating species differences in pathway redundancy.
- **Zoonotic potential:** Not applicable (a host genetic disorder, not a transmissible disease).

### 15. Model Organisms

- **Primary model:** The ***Myd88⁻/⁻* knockout mouse** (Adachi/Akira, Immunity 1998; Finding 6) — a **mammalian, whole-body gene-targeted knockout**. It faithfully reproduces the **signaling defect**: abolished IL-1– and IL-18–mediated responses, impaired acute-phase/cytokine induction, defective NF-κB/JNK activation, and impaired Th1 responses.
- **Phenotype recapitulation:** Excellent for the **molecular/signaling** phenotype and for demonstrating MyD88's role as an essential adaptor. **Limitation:** the mouse displays **broader pathogen susceptibility** than the narrow human phenotype, so it *over-predicts* clinical vulnerability and cannot fully model the human redundancy that spares patients from most infections.
- **Other models:** Patient-derived **fibroblasts and leukocytes** serve as in vitro systems (TLR/IL-1R agonist stimulation, NF-κB reporter assays) for functional variant validation (e.g., S34Y/R98C studies; Findings 3, 8). Conditional/tissue-specific *Myd88* mice (e.g., epithelial-specific) have illuminated organ-level roles in related contexts.
- **Resources:** Mouse Genome Informatics (MGI), IMPC, IMSR for *Myd88* alleles.

---

## Mechanistic Model / Interpretation

```
   GERMLINE BIALLELIC LoF MYD88 (3p22.2; e.g., S34Y, R98C, E52del)
                     │  (Findings 1, 8)
                     ▼
   No functional MyD88 adaptor  ──►  MYDDOSOME CANNOT FORM
   (death domain can't oligomerize / recruit IRAK4)   (Finding 3)
                     │
                     ▼
   No IRAK4→IRAK1/2 activation ─► no TRAF6/TAK1/IKK ─► NO NF-κB / MAPK
                     │  (Finding 3)
        ┌────────────┼───────────────────────────┐
        ▼            ▼                             ▼
 [Branch A]     [Branch B]                    [Branch C]
 Myeloid/epith. B-cell TLR7/9 defect          pDC TLR7 defect
 TLR/IL-1R       ↓ MZ-like IgM+IgD+CD27+       ↓ type I IFN
 defense fails   ↓ T-indep. anti-poly IgM      (Finding 4)
 + weak          (Finding 5)                        │
 inflammation                                       ▼
 (Findings 1,2)       └──────────┐          Hypoxemic COVID-19
        │                        ▼          (OR ~74.7 for IMV)
        ▼            Poor control of encapsulated
 Recurrent invasive  pyogenic bacteria (S. pneumoniae)
 pyogenic bacterial  ◄──────────┘
 disease; silent
 presentation → death
 (Findings 2, 7)
        │
        ▼
 AGE-DEPENDENT ADAPTIVE COMPENSATION → improving prognosis (Finding 2)
```

The unifying interpretation is that MyD88 sits at a **single obligatory node** for a large family of innate receptors, yet in humans this node proves **redundant for defense against most microbes** — the immune system's layered architecture (complement, MyD88-independent TLR3/TRIF, adaptive antibody) covers the great majority of threats. The disease therefore reveals which pathogens are *uniquely* dependent on MyD88-driven innate inflammation and rapid T-independent IgM: encapsulated pyogenic bacteria (above all *S. pneumoniae*), plus — via the specialized pDC TLR7/type I IFN branch — SARS-CoV-2. The **blunted inflammatory response** is not incidental but a direct consequence of the lesion, and it is the proximate cause of much of the mortality because it removes the clinical "alarm." Finally, the age-dependent improvement provides both prognostic guidance and a therapeutic rationale: passive antibody (immunoglobulin) and active vaccination substitute for the missing innate arm.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [18669862](https://pubmed.ncbi.nlm.nih.gov/18669862/) | von Bernuth et al., *Science* 2008 | Founding description; AR inheritance, narrow pyogenic phenotype, pathway redundancy (Findings 1, 8) |
| [21057262](https://pubmed.ncbi.nlm.nih.gov/21057262/) | Picard et al., *Medicine* 2010 | Largest cohort; infection spectrum, onset, mortality, blunted inflammation, IRAK-4 equivalence (Finding 2) |
| [20485341](https://pubmed.ncbi.nlm.nih.gov/20485341/) | Lin, Lo & Wu, *Nature* 2010 | Myddosome crystal structure; hierarchical assembly mechanism (Finding 3) |
| [20966070](https://pubmed.ncbi.nlm.nih.gov/20966070/) | George et al., 2011 | S34Y/R98C impair oligomerization & NF-κB; links variants to mechanism (Findings 3, 8) |
| [36880831](https://pubmed.ncbi.nlm.nih.gov/36880831/) | García-García et al., *J Exp Med* 2023 | Expanded phenotype: hypoxemic COVID-19; pDC TLR7/type I IFN mechanism (Finding 4) |
| [25320238](https://pubmed.ncbi.nlm.nih.gov/25320238/) | Maglione et al., *J Immunol* 2014 | T-independent IgM defect; reduced marginal-zone-like B cells (Finding 5) |
| [9697844](https://pubmed.ncbi.nlm.nih.gov/9697844/) | Adachi/Akira et al., *Immunity* 1998 | *Myd88⁻/⁻* mouse model; IL-1/IL-18 signaling loss (Finding 6) |
| [24596024](https://pubmed.ncbi.nlm.nih.gov/24596024/) | McKelvie et al., 2014 | Management regimen and fatal breakthrough despite prophylaxis (Finding 7) |
| [17004992](https://pubmed.ncbi.nlm.nih.gov/17004992/) | Albiger et al., 2007 | TLR9/MyD88 in early pneumococcal defense — supports pathogen-specificity |
| [28235196](https://pubmed.ncbi.nlm.nih.gov/28235196/) | Israel et al., 2017 (TIRAP) | Antibody-mediated rescue of innate deficiency — supports adaptive compensation concept |
| [41369391](https://pubmed.ncbi.nlm.nih.gov/41369391/) | Review, IEI/TLRs in children | Context: diagnostic assays, future gene-therapy perspectives |

All quoted snippets in the Key Findings section are verbatim from the cited abstracts. Evidence types span **human clinical** (von Bernuth, Picard, García-García, Maglione, McKelvie), **structural/in vitro** (Lin/Wu, George), and **model organism** (Adachi/Akira).

---

## Limitations and Knowledge Gaps

- **Extreme rarity → small numbers:** The pivotal cohorts total only a few dozen patients (with MyD88-deficient individuals a minority of pooled MyD88/IRAK-4 series). Prevalence, incidence, precise mortality rates, and sex/geographic distributions are therefore imprecise.
- **Phenocopy conflation:** Much clinical data pool MyD88 and IRAK-4 deficiency because they are indistinguishable; some MyD88-specific quantitative estimates are inferred from the combined cohort.
- **Identifiers partially unverified:** Orphanet, ICD-10/ICD-11, and MeSH identifiers were not independently confirmed in this investigation and should be validated against those primary resources before database ingestion.
- **Human–mouse discordance:** The *Myd88⁻/⁻* mouse over-predicts susceptibility, limiting its use for modeling the human redundancy — the mechanistic basis of the human's narrow phenotype remains incompletely explained.
- **Allele frequency & penetrance quantitation:** Because variants are private, population allele frequencies and formal penetrance/expressivity metrics are not tabulated here.
- **Therapeutic evidence is observational:** Management recommendations rest on case series and expert practice, not randomized trials; the true efficacy of each preventive component is not quantified.
- **Epigenetics, modifiers, QoL:** No disease-specific epigenetic data, validated genetic modifiers, or formal quality-of-life measurements were identified.

---

## Proposed Follow-up Experiments / Actions

1. **Verify and complete cross-references:** Confirm Orphanet, ICD-10/ICD-11, MeSH, and MONDO mappings directly from those resources to finalize Section 1 identifiers.
2. **Compile a curated *MYD88* variant table** from ClinVar/HGMD with ACMG classifications, variant type, domain location (death vs TIR), functional data, and gnomAD frequencies — to enrich Section 4.
3. **Quantitative natural-history synthesis:** Aggregate published MyD88-specific cases (separating them from IRAK-4) to derive age-stratified infection incidence, causative organisms, and survival curves.
4. **Mechanistic dissection of human redundancy:** Comparative functional immunology (e.g., single-cell profiling of patient vs control innate cells under defined stimuli) to explain why humans tolerate MyD88 loss for most pathogens while mice do not.
5. **Prospective assessment of COVID-19 and other viral risks** in genotyped patients, and evaluation of type I IFN or vaccination strategies for the pDC/TLR7 branch (Finding 4).
6. **Evaluate immunoglobulin replacement and prophylaxis efficacy** systematically (registry-based), including optimal antibiotic choice and vaccination schedules, given the demonstrated risk of fatal breakthrough disease.
7. **Biomarker development for the "silent infection" problem:** Identify early molecular indicators of invasive infection that do not depend on the MyD88-driven acute-phase response (which is blunted), to enable earlier intervention.

---

*Report compiled from 8 confirmed findings and 24 reviewed papers across a 5-iteration autonomous investigation. Evidence classes: human clinical, structural/in vitro, and model organism. All direct quotations are verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](MyD88_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MyD88_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012839` (2 mentions) - the report calls it "if available"; MONDO calls it **pyogenic bacterial infections due to MyD88 deficiency**
- `NCIT:C15617` (2 mentions) - the report calls it "Antibiotic Therapy", "At the *first* suspicion of infection, given the blunted warning signs — the single most important acute intervention"; NCIT calls it **Monoclonal Antibody 17-1A/sargramostim**
- `NCIT:C603` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Isotretinoin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002850` (1 mention) - the report calls it "decreased circulating IgM"; HP calls it **Decreased circulating IgM concentration**
- `GO:0007249` (1 mention) - the report calls it "I-κB kinase/NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0032760` (1 mention) - the report calls it "positive regulation of TNF production"; GO calls it **positive regulation of tumor necrosis factor production**, and lists "positive regulation of TNF production" among its other names
- `CL:0000787` (1 mention) - the report calls it "memory B cell / marginal-zone-like B cell"; CL calls it **memory B cell**
- `NCIT:C15346` (1 mention) - the report calls it "Vaccine Therapy"; NCIT calls it **Vaccination**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15617` - called "Antibiotic Therapy", "At the *first* suspicion of infection, given the blunted warning signs — the single most important acute intervention"
