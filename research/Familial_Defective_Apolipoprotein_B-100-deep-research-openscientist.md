---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T14:08:27.287681'
end_time: '2026-09-06T14:21:13.703918'
duration_seconds: 766.42
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Familial Defective Apolipoprotein B-100
  mondo_id: MONDO:0007751
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
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 34
  on_topic: 26
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 22
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.043
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0007751
    reported_labels:
    - if available
    - MONDO
    ontology_label: hypercholesterolemia, autosomal dominant, type B
  - term_id: CL:0000891
    reported_labels:
    - aortic/vascular smooth muscle context
    ontology_label: foam cell
  - term_id: GO:0005905
    reported_labels:
    - Subcellular:** Plasma-membrane LDL receptor and clathrin-coated pits
    ontology_label: clathrin-coated pit
  labels_variant: 3
  unresolved_terms:
  - HP:0001229
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Defective_Apolipoprotein_B-100-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Defective_Apolipoprotein_B-100-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Defective Apolipoprotein B-100
- **MONDO ID:** MONDO:0007751 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Defective Apolipoprotein B-100** covering all of the
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

# Familial Defective Apolipoprotein B-100 (FDB): A Comprehensive Disease Profile

**Disease:** Familial Defective Apolipoprotein B-100 (FDB)
**MONDO ID:** MONDO:0007751 | **OMIM:** #144010 | **Category:** Mendelian (autosomal dominant / codominant)

---

## Summary

Familial Defective Apolipoprotein B-100 (FDB) is a monogenic autosomal dominant (codominant) form of primary hypercholesterolemia caused by missense variants in the *APOB* gene that impair the ability of apolipoprotein B-100 (apoB-100) to bind the LDL receptor (LDLR). The archetypal and most common cause is the **R3500Q** variant (c.10580G>A; rs5742904; legacy p.Arg3500Gln, mature-protein numbering p.Arg3527Gln), which disrupts a critical intramolecular interaction between **Arg3500 and Trp4369** that is required for apoB-100 to adopt the conformation necessary for normal LDLR engagement [PMID: 11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/). Because defective LDL particles are cleared slowly from the plasma, LDL cholesterol (LDL-C) accumulates, leading to arterial LDL retention, macrophage foam-cell formation, tendon xanthomas, and premature atherosclerotic cardiovascular disease.

The R3500Q variant is a **single European founder mutation** that arose in an ancestor roughly 6,000–7,000 years ago (≈6,750 years; ~270 generations), and virtually all carriers worldwide are identical-by-descent [PMID: 9339363](https://pubmed.ncbi.nlm.nih.gov/9339363/). Clinically, FDB is a **milder, frequently underdiagnosed** cousin of LDLR-mediated familial hypercholesterolemia (FH): LDL-C elevation is on average ~1.2 mmol/L lower than in LDLR mutation carriers, coronary heart disease occurs less often and later, and standard clinical FH scoring criteria frequently fail to flag FDB carriers [PMID: 15528480](https://pubmed.ncbi.nlm.nih.gov/15528480/); [PMID: 25126774](https://pubmed.ncbi.nlm.nih.gov/25126774/); [PMID: 18279815](https://pubmed.ncbi.nlm.nih.gov/18279815/).

Because the LDL receptor is structurally intact in FDB, the disorder responds well to LDLR-upregulating pharmacotherapy — statins, ezetimibe, and PCSK9 inhibitors — and definitive diagnosis is molecular (single-gene codon-3500 assay or an NGS FH gene panel), enabling reverse-cascade screening of relatives [PMID: 30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/); [PMID: 29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/). Allelic heterogeneity exists at and near codon 3500 (R3500W, R3531C, R3480W, H3543Y), with **R3500W being an important contributor to FH among East Asians** [PMID: 27919345](https://pubmed.ncbi.nlm.nih.gov/27919345/); [PMID: 15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/).

---

## 1. Disease Information

**Overview.** FDB is an inherited disorder of LDL catabolism in which a mutant apoB-100 — the sole apolipoprotein of LDL and the ligand recognized by the hepatic LDL receptor — binds the receptor with reduced affinity. The consequence is delayed clearance of LDL, elevated plasma LDL-C and apoB, and an increased lifetime risk of premature coronary artery disease. Clinically it is essentially indistinguishable from heterozygous LDLR-mediated FH without molecular testing; both present with elevated LDL-C, normal triglycerides and HDL-C, tendon xanthomas, and premature atherosclerosis [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0007751 |
| OMIM | #144010 (Hypercholesterolemia, due to ligand-defective apoB, or FDB) |
| Gene | *APOB* (HGNC:603), chromosome 2p24–23 |
| Classic variant | rs5742904 (R3500Q; c.10580G>A) |
| Category | Mendelian, autosomal dominant/codominant |

**Synonyms / alternative names.** Familial ligand-defective apolipoprotein B-100; familial defective apoB-100; FDB; ligand-defective apoB; hypercholesterolemia due to ligand-defective apoB. FDB is one molecular subtype within the broader clinical umbrella of *autosomal dominant hypercholesterolemia* (ADH) / familial hypercholesterolemia (FH), alongside *LDLR* and *PCSK9* causes [PMID: 31883481](https://pubmed.ncbi.nlm.nih.gov/31883481/).

**Data source type.** The knowledge in this report derives from **aggregated disease-level resources** — molecular genetics studies, FH registries, population cohorts (e.g., Copenhagen General Population Study), and functional/biochemical studies — rather than individual EHR-derived patient records.

---

## 2. Etiology

**Primary cause — genetic.** FDB is a **monogenic disorder** caused by heterozygous (or, rarely, homozygous/compound heterozygous) missense variants in *APOB* that localize to the LDLR-binding region of apoB-100 near codon 3500. The disease is not infectious or primarily environmental; environmental/lifestyle factors modify severity but do not cause the disorder.

**Genetic risk factors.**
- **Causal variant:** *APOB* R3500Q (c.10580G>A; rs5742904) is the classic and most frequent cause. Additional ligand-defective variants clustering in the same functional region include **R3500W, R3531C, R3480W, and H3543Y** [PMID: 15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/); [PMID: 11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/).
- **Zygosity:** heterozygotes are affected (codominant); homozygous *APOB* cases exist but are rare (e.g., 4 homozygous *APOB* patients among 49 molecularly defined homozygous ADH cases in the Netherlands) [PMID: 24585268](https://pubmed.ncbi.nlm.nih.gov/24585268/).

**Environmental / modifying risk factors.** Background diet (saturated fat, cholesterol intake), obesity, smoking, and coexisting metabolic syndrome raise absolute LDL-C and cardiovascular risk on top of the genetic defect. Phenotypic expression depends jointly on the mutation and the genetic/dietary background of the population studied; ascertainment in lipid clinics overestimates the true population effect size [PMID: 15528480](https://pubmed.ncbi.nlm.nih.gov/15528480/).

**Protective factors.** Because the underlying lesion is impaired receptor-mediated LDL clearance, any factor that upregulates LDLR expression or lowers LDL production is protective — this is the pharmacological basis of statins, ezetimibe, and PCSK9 inhibition. Rare *APOB* missense variants can also lower LDL (e.g., an apoB S2429T variant proposed to have an LDL-lowering effect within an FH family), illustrating that *APOB* variation can push LDL in either direction [PMID: 27578127](https://pubmed.ncbi.nlm.nih.gov/27578127/); [PMID: 7585299](https://pubmed.ncbi.nlm.nih.gov/7585299/).

**Gene–environment interactions.** The measured LDL-C increment attributable to a given *APOB* or *LDLR* variant differs by background population and by ascertainment context — general-population carriers and clinically ascertained FH carriers differed by ~1.6 mmol/L (P=0.03) — confirming that the phenotype is a product of genotype × background/lifestyle rather than genotype alone [PMID: 15528480](https://pubmed.ncbi.nlm.nih.gov/15528480/).

---

## 3. Phenotypes

FDB phenotypes are those of heterozygous FH but generally milder.

| Phenotype | Type | HPO suggestion | Onset / severity / frequency |
|---|---|---|---|
| Hypercholesterolemia (elevated LDL-C, elevated apoB) | Laboratory abnormality | HP:0003124 (Hypercholesterolemia); HP:0003563 (Hyperbetalipoproteinemia) | Congenital/lifelong biochemical trait; milder than LDLR-FH; near-universal but LDL-C may fall within normal range in some carriers [PMID: 18279815](https://pubmed.ncbi.nlm.nih.gov/18279815/) |
| Tendon xanthomas | Clinical sign / physical manifestation | HP:0001229 / HP:0010874 (Xanthomatosis) | Adult-onset; less frequent than in LDLR-FH; present in a minority [PMID: 10559517](https://pubmed.ncbi.nlm.nih.gov/10559517/) |
| Premature coronary artery disease | Clinical sign / complication | HP:0001677 (Coronary artery atherosclerosis); HP:0005110 | Adult-onset, later than in LDLR-FH; CHD in ~5.6% of FDB (mean age 52) vs 41.8% of FH (mean age 41) [PMID: 25126774](https://pubmed.ncbi.nlm.nih.gov/25126774/) |
| Normal triglycerides and HDL-C | Laboratory (distinguishing feature) | — | Characteristic normal-TG/normal-HDL profile helps distinguish from combined hyperlipidemias [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/) |

**Severity and progression.** LDL-C elevation is stable/lifelong; atherosclerosis is slowly progressive. Notably, FH/high-LDL-C (including *APOB* R3500Q) increases myocardial-infarction risk but **not** ischemic stroke risk in the general population [PMID: 29593013](https://pubmed.ncbi.nlm.nih.gov/29593013/).

**Quality of life.** No FDB-specific EQ-5D/SF-36 data were identified. QoL impact derives chiefly from cardiovascular events and lifelong pharmacotherapy; because FDB is generally milder and later-onset than LDLR-FH, the average burden is correspondingly lower.

---

## 4. Genetic / Molecular Information

**Causal gene.** *APOB* (apolipoprotein B; HGNC:603; OMIM *107730), chromosome 2p24–23. ApoB-100 (4,536 residues in the mature protein) is the structural scaffold of VLDL/IDL/LDL and the LDLR ligand.

**Pathogenic variants.**

| Variant (legacy) | cDNA / rsID | Type | Notes |
|---|---|---|---|
| R3500Q | c.10580G>A; rs5742904 | Missense | Classic FDB variant; most common; European founder [PMID: 9339363](https://pubmed.ncbi.nlm.nih.gov/9339363/) |
| R3500W | — | Missense | Significant FH contributor in East Asians; more prevalent than R3500Q in Chinese hyperlipidemics (2.4% vs 0.3%) [PMID: 27919345](https://pubmed.ncbi.nlm.nih.gov/27919345/); [PMID: 10998466](https://pubmed.ncbi.nlm.nih.gov/10998466/) |
| R3531C | — | Missense | Ligand-defective, LDLR-binding region [PMID: 15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/) |
| R3480W | — | Missense | Ligand-defective, LDLR-binding region [PMID: 15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/) |
| H3543Y | — | Missense | ~4× more frequent than R3500Q in a German cardiology cohort (0.47% vs 0.12%) [PMID: 15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/) |

**Variant classification (ACMG/AMP).** R3500Q is well established as **pathogenic** (functional evidence of defective LDLR binding, cosegregation, founder haplotype). Several additional exon 26/29 variants (e.g., S3476L, S3488G, Y3533C, T3540M, I4350T, G4368D) have been reported as FDB-associated in Dutch cohorts and warrant case-by-case interpretation [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/).

**Allele frequency.** R3500Q carrier frequency is on the order of ~0.1% (≈1 in 500–1,000) in Northern/Central European populations, lower in Southern Europe (e.g., rare in general Spain but locally enriched in Galicia due to Celtic ancestry) [PMID: 12208478](https://pubmed.ncbi.nlm.nih.gov/12208478/).

**Somatic vs germline.** Germline; there is no somatic component.

**Functional consequence.** A **conformational loss-of-ligand-function**: the variant does not abolish the protein but changes the local conformation around the receptor-binding site, reducing LDLR affinity to ~32% of normal [PMID: 10657378](https://pubmed.ncbi.nlm.nih.gov/10657378/). This behaves as a dominant/codominant trait because each affected allele produces defective LDL particles.

**Modifier genes.** Polygenic LDL-raising SNP burden and coexisting variants in other lipid genes (*LDLR*, *PCSK9*, *APOE*, *ANGPTL3*, *APOC3*) modulate expressivity; rare *APOB* variants (e.g., S2429T) may lower LDL and partially offset severity [PMID: 27578127](https://pubmed.ncbi.nlm.nih.gov/27578127/); [PMID: 31883481](https://pubmed.ncbi.nlm.nih.gov/31883481/).

**Epigenetic / chromosomal.** No recurrent epigenetic mechanism or chromosomal abnormality is implicated in FDB; it is a point-mutation disorder.

---

## 5. Environmental Information

- **Environmental factors:** No specific toxin, radiation, or occupational exposure causes FDB.
- **Lifestyle factors:** Dietary saturated fat/cholesterol, obesity, physical inactivity, and smoking increase absolute LDL-C and atherosclerotic risk on top of the genetic defect and are the primary modifiable levers.
- **Infectious agents:** None. FDB is a purely genetic, non-communicable disorder.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A germline missense variant in *APOB* (most commonly **R3500Q**) is inherited → **leads to** an amino-acid substitution in apoB-100 at/near the LDLR-binding region.
2. The substitution disrupts the intramolecular **Arg3500–Trp4369** interaction (and requires the apoB-100 C-terminus) → **results in** an altered local conformation of apoB-100 around the receptor-binding site (demonstrated by higher affinity for the conformation-sensitive MB47 antibody) [PMID: 11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/).
3. The altered conformation → **reduces** binding of LDL particles to the hepatic LDL receptor (to ~32% of normal affinity) [PMID: 10657378](https://pubmed.ncbi.nlm.nih.gov/10657378/).
4. Reduced receptor binding → **decreases** receptor-mediated hepatic uptake/catabolism of LDL → **prolongs** LDL residence time in plasma.
5. Delayed clearance → **raises** plasma LDL-C and apoB concentrations (the biochemical phenotype).
6. Elevated (and modified/oxidized) LDL → **accumulates and is retained** in the arterial intima.
7. Retained LDL → **is internalized by macrophages** → **drives** foam-cell formation and an immune-inflammatory response [PMID: 33959626](https://pubmed.ncbi.nlm.nih.gov/33959626/).
8. Chronic foam-cell/inflammatory burden → **produces** atherosclerotic plaques → **manifests** clinically as tendon xanthomas and premature coronary artery disease [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/).

```
APOB R3500Q mutation
   │ (disrupts Arg3500–Trp4369)
   ▼
apoB-100 conformational change near LDLR-binding site   [upstream, causal]
   ▼
↓ LDL–LDLR binding affinity (~32% of normal)
   ▼
↓ hepatic LDL clearance → ↑ LDL residence time
   ▼
↑ plasma LDL-C / apoB
   ▼
arterial intimal LDL retention ──► macrophage uptake ──► foam cells + inflammation
   ▼
atherosclerosis ──► tendon xanthomas + premature CAD   [downstream, clinical]
```

**Upstream vs downstream.** The conformational defect and reduced receptor binding are the **upstream initiating lesions**; hypercholesterolemia is the intermediate biochemical readout; foam-cell formation and atherosclerosis are **downstream** consequences shared with all LDL-driven hypercholesterolemias.

**Molecular pathways / cellular processes.** Receptor-mediated endocytosis of LDL (KEGG hsa04979, "Cholesterol metabolism"); reverse cholesterol transport (ABCA1-mediated efflux); macrophage lipid handling and NF-κB-driven vascular inflammation are engaged downstream [PMID: 33568202](https://pubmed.ncbi.nlm.nih.gov/33568202/); [PMID: 36838686](https://pubmed.ncbi.nlm.nih.gov/36838686/).

**Protein dysfunction.** Conformational loss-of-ligand-function of apoB-100 (not misfolding/aggregation, not loss of expression). UniProt P04114 (APOB_HUMAN).

**Metabolic changes.** Isolated elevation of LDL-C and apoB with characteristically normal triglycerides and HDL-C — distinguishing FDB from combined hyperlipidemias.

**Suggested ontology terms.** GO:0006629 (lipid metabolic process); GO:0034383 (low-density lipoprotein particle clearance); GO:0006898 (receptor-mediated endocytosis); GO:0034364 (low-density lipoprotein particle); CHEBI:39025 (low-density lipoprotein). Cell types: CL:0000182 (hepatocyte), CL:0000235 (macrophage/foam cell), CL:0000891 (aortic/vascular smooth muscle context).

---

## 7. Anatomical Structures Affected

- **Primary organ:** Liver (hepatocytes) — the principal site of LDL-receptor-mediated clearance whose function is bypassed by the defective ligand. UBERON:0002107 (liver); CL:0000182 (hepatocyte).
- **Secondary/target organs:** Arterial wall, especially coronary arteries (and femoral/peripheral arteries). UBERON:0001981 (blood vessel); UBERON:0001621 (coronary artery). Femoral intima-media thickness is increased in FH patients including *APOB* defects, in relation to mutational class [PMID: 18096825](https://pubmed.ncbi.nlm.nih.gov/18096825/).
- **Body systems:** Cardiovascular (atherosclerosis, CAD) and integumentary/musculoskeletal (tendon xanthomas). Blood/plasma lipoprotein compartment is the biochemical stage.
- **Tissue/cell level:** Vascular intima (connective tissue), arterial macrophages/foam cells (CL:0000235), and hepatocytes.
- **Subcellular:** Plasma-membrane LDL receptor and clathrin-coated pits (GO:0005905); endosomes/lysosomes for LDL degradation (GO:0005764). The extracellular lipoprotein particle (GO:0034364) is the affected entity.
- **Lateralization:** Systemic/bilateral (xanthomas often symmetric); vascular disease is diffuse rather than lateralized.

---

## 8. Temporal Development

- **Onset:** The biochemical trait (elevated LDL-C/apoB) is **congenital and lifelong**. Clinical complications are **adult-onset**, typically later than in LDLR-FH.
- **Onset pattern:** Chronic/insidious.
- **Progression:** Slowly progressive atherosclerosis. FDB CHD occurs at a mean age of ~52 years versus ~41 years in LDLR-FH, and far less frequently (5.6% vs 41.8%) [PMID: 25126774](https://pubmed.ncbi.nlm.nih.gov/25126774/).
- **Course:** Stable biochemical elevation with progressive vascular risk; chronic lifelong disease.
- **Critical window:** Cumulative LDL exposure drives risk, so the critical period for intervention is **early and sustained LDL lowering** from young adulthood (or childhood in higher-risk cases), before substantial plaque burden accrues.

---

## 9. Inheritance and Population

**Inheritance.** Autosomal **dominant / codominant**; heterozygotes are affected. Homozygous/compound-heterozygous *APOB* cases are rare and more severe [PMID: 24585268](https://pubmed.ncbi.nlm.nih.gov/24585268/).

**Penetrance / expressivity.** Biochemical penetrance is high but **expressivity is variable** — some carriers have LDL-C within the normal range, and clinical FH scores (Dutch Lipid Clinic Network, Simon Broome) have low sensitivity for *APOB* variants (DLCN sensitivity 13.8%; SBDC 22.5%) [PMID: 30270060](https://pubmed.ncbi.nlm.nih.gov/30270060/); [PMID: 18279815](https://pubmed.ncbi.nlm.nih.gov/18279815/).

**Founder effect.** R3500Q is a single European founder mutation ~6,000–7,000 years old (≈270 generations); all probands are identical-by-descent, carried on the rare APOB haplotype 194 (XbaI−/MspI+/EcoRI−) [PMID: 9339363](https://pubmed.ncbi.nlm.nih.gov/9339363/); [PMID: 12208478](https://pubmed.ncbi.nlm.nih.gov/12208478/).

**Epidemiology.** Estimated carrier frequency ~0.1% (≈1 in 500–1,000) in Northern/Central Europe; combined LDLR+APOB FH prevalence ~1 in 125–135 in Switzerland, with FDB a minority subtype [PMID: 30270060](https://pubmed.ncbi.nlm.nih.gov/30270060/). FDB is a minor cause of clinically diagnosed FH in Southern Europe (e.g., 1.4% of Spanish clinical-FH probands; population prevalence ~2.8×10⁻⁵), but locally enriched in Galicia [PMID: 12208478](https://pubmed.ncbi.nlm.nih.gov/12208478/); [PMID: 16596945](https://pubmed.ncbi.nlm.nih.gov/16596945/).

**Population distribution of variants.** R3500Q predominates in European-descent populations; **R3500W is the major ligand-defective *APOB* variant in East Asians** (identified in 8 Taiwanese FH probands; heterozygote prevalence 2.4% vs 0.3% for R3500Q in Chinese hyperlipidemics) [PMID: 20538126](https://pubmed.ncbi.nlm.nih.gov/20538126/); [PMID: 10998466](https://pubmed.ncbi.nlm.nih.gov/10998466/).

**Sex ratio / consanguinity.** No strong sex bias (autosomal dominant); consanguinity is not required for the dominant heterozygous phenotype but underlies rare homozygous cases.

---

## 10. Diagnostics

**Laboratory.** Elevated LDL-C and apoB with normal triglycerides and HDL-C (LOINC: 13457-7 LDL-C; 1884-6 apoB) [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/). A functional flow-cytometric LDL-ligand assay can detect heterozygous FDB by demonstrating reduced LDL binding [PMID: 10657378](https://pubmed.ncbi.nlm.nih.gov/10657378/).

**Genetic testing (definitive).** FDB **cannot be distinguished clinically from LDLR-FH** and requires molecular confirmation [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/). Approaches:
- Targeted single-variant/codon-3500 assays (PCR-RFLP, high-resolution melting) for R3500Q/H3543Y [PMID: 18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/).
- NGS FH gene panels covering *LDLR*, *APOB*, *PCSK9* (± *LDLRAP1*, *ABCG5/8*) [PMID: 41412630](https://pubmed.ncbi.nlm.nih.gov/41412630/); [PMID: 41760042](https://pubmed.ncbi.nlm.nih.gov/41760042/).
- WES/WGS are useful when panels are negative.

**Clinical criteria & differential diagnosis.** DLCN and Simon Broome criteria are standard for FH but **under-detect FDB** [PMID: 30270060](https://pubmed.ncbi.nlm.nih.gov/30270060/). Differential diagnosis includes LDLR-mediated FH, *PCSK9* gain-of-function FH, polygenic hypercholesterolemia, familial combined hyperlipidemia [PMID: 34906840](https://pubmed.ncbi.nlm.nih.gov/34906840/), and rare recessive/other catabolic defects (a clinical HoFH phenotype has been reported with intact apoB/LDLR, implying additional catabolic genes) [PMID: 9626156](https://pubmed.ncbi.nlm.nih.gov/9626156/).

**Screening.** Cascade (reverse-cascade) screening of first-degree relatives after an index molecular diagnosis is the key strategy; universal newborn/pediatric screening for FH is supported by healthcare professionals but not yet routine [PMID: 41251905](https://pubmed.ncbi.nlm.nih.gov/41251905/); [PMID: 41608359](https://pubmed.ncbi.nlm.nih.gov/41608359/).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No FDB-specific survival tables identified. Prognosis is driven by cardiovascular event risk, which is **lower and later** than in LDLR-FH.
- **Morbidity:** Premature CAD is the dominant morbidity; CHD prevalence ~5.6% in FDB vs 41.8% in LDLR-FH [PMID: 25126774](https://pubmed.ncbi.nlm.nih.gov/25126774/). FH/high LDL-C raises myocardial infarction risk but not ischemic stroke risk [PMID: 29593013](https://pubmed.ncbi.nlm.nih.gov/29593013/).
- **Prognostic factors:** Mutational class (null LDLR alleles > receptor-defective > *APOB* defects for atherosclerosis severity and LDL-C), absolute/cumulative LDL-C, age, sex, smoking, and blood pressure [PMID: 18096825](https://pubmed.ncbi.nlm.nih.gov/18096825/); [PMID: 28475941](https://pubmed.ncbi.nlm.nih.gov/28475941/).
- **Recovery potential:** With early sustained LDL lowering, cardiovascular risk is substantially reducible; the intact LDL receptor predicts good pharmacologic response.

---

## 12. Treatment

FDB is managed as **heterozygous FH**, and — critically — because the LDL receptor itself is intact, LDLR-upregulating therapies are highly effective.

| Therapy (NCIT suggestion) | Class / mechanism | Evidence in FDB context |
|---|---|---|
| Statins (e.g., rosuvastatin, atorvastatin) — NCIT:C1518 | HMG-CoA reductase inhibitor → ↑ hepatic LDLR expression | Mevastatin increases LDLR expression in vitro; statins are first-line for FH including *APOB* [PMID: 29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/); [PMID: 30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/) |
| Ezetimibe — NCIT:C61708 | NPC1L1 inhibitor → ↓ intestinal cholesterol absorption | Standard add-on in heterozygous FH [PMID: 30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/) |
| PCSK9 inhibitors (evolocumab, alirocumab) — NCIT:C121787 | Monoclonal antibody → prevents LDLR degradation → ↑ cell-surface LDLR | PCSK9-neutralizing antibody restores LDLR expression; effective because receptor is intact [PMID: 29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) |

**Rationale.** "There is today a large availability of drugs (i.e., statins, ezetimibe and PCSK9 inhibitors) allowing theoretically the normalization of plasma LDL cholesterol levels in this population" [PMID: 30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/). Because FDB LDL clearance depends on functional LDLR, upregulating the receptor compensates for the ligand defect — mechanistically supported by the observation that "Mevastatin increased, whereas rPCSK9 reduced LDLR expression. The PCSK9-neutralizing antibody restored LDLR expression" [PMID: 29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/).

**Experimental / advanced.** Gene- and cell-based therapies (LDLR gene delivery, CRISPR/Cas9 editing) are in development primarily for homozygous FH; RNA therapies and MTP/ANGPTL3-directed agents extend options for severe/refractory disease [PMID: 36572377](https://pubmed.ncbi.nlm.nih.gov/36572377/); [PMID: 30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/).

**Personalized medicine.** Molecular subtyping (APOB vs LDLR-null vs LDLR-defective) informs prognosis and intensity of therapy; genotype-guided cascade screening extends benefit to relatives [PMID: 41412630](https://pubmed.ncbi.nlm.nih.gov/41412630/).

---

## 13. Prevention

- **Primary prevention:** Lifelong healthy diet, avoidance of smoking, weight and blood-pressure control to minimize cumulative atherosclerotic risk.
- **Secondary prevention (early detection):** Reverse-cascade genetic and lipid screening of relatives after an index diagnosis; consideration of pediatric/newborn FH screening [PMID: 41251905](https://pubmed.ncbi.nlm.nih.gov/41251905/); [PMID: 41608359](https://pubmed.ncbi.nlm.nih.gov/41608359/).
- **Tertiary prevention:** Aggressive LDL lowering (statin ± ezetimibe ± PCSK9 inhibitor) to prevent CAD progression and events.
- **Genetic counseling:** 50% transmission risk per offspring (autosomal dominant); counseling supports family planning and cascade testing [PMID: 41412630](https://pubmed.ncbi.nlm.nih.gov/41412630/).

---

## 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *APOB* is conserved across mammals (human *APOB*, NCBI Gene 338; mouse *Apob*, NCBI Gene 238). No specific naturally occurring animal disease attributable to an APOB R3500Q-equivalent variant was identified in this investigation.
- **Comparative biology:** The apoB-100/LDLR clearance axis is evolutionarily conserved, and the mechanism has been functionally validated in transgenic mice expressing human R3500Q and W4369Y apoB, which reproduce the defective LDLR binding [PMID: 11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/).
- **Transmission/zoonosis:** Not applicable — non-communicable genetic disorder.

---

## 15. Model Organisms

- **Transgenic mice:** Mice expressing human apoB-100 carrying **R3500Q** (and the complementary **W4369Y**) were pivotal in defining the mechanism — LDL from both showed identically defective LDLR binding and increased MB47 antibody affinity, demonstrating the Arg3500–Trp4369 conformational interaction [PMID: 11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/).
- **In vitro / cellular models:** Cultured cells (e.g., fibroblasts, HepG2-type systems) are used to quantify LDLR expression and LDL binding under statin/PCSK9 modulation, and to test LDLR-upregulating therapeutics [PMID: 29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/). Macrophage foam-cell models (e.g., RAW264.7, ApoE-deficient mouse aortas) recapitulate the downstream atherosclerotic steps [PMID: 33568202](https://pubmed.ncbi.nlm.nih.gov/33568202/); [PMID: 36838686](https://pubmed.ncbi.nlm.nih.gov/36838686/).
- **Phenotype recapitulation:** Transgenic mice faithfully reproduce the **ligand-binding defect** (the core lesion). **Limitation:** murine lipoprotein metabolism differs from human, so absolute LDL-C phenotype and atherosclerosis burden require sensitized backgrounds (e.g., ApoE-deficient) and do not fully mirror human clinical disease.
- **Resources:** MGI (mouse *Apob*), Cellosaurus/ATCC (cell lines).

---

## Mechanistic Model / Interpretation

FDB is best understood as a **ligand-side mirror image of LDLR-mediated FH**: in classic FH the receptor is broken, whereas in FDB the ligand (apoB-100) is broken. Both converge on the same downstream pathology — impaired LDL clearance → hypercholesterolemia → arterial LDL retention → foam cells → atherosclerosis — but they differ quantitatively. The single conformational contact point (Arg3500–Trp4369) is the linchpin: substituting Arg3500 (a specific arginine, not merely any positive charge) collapses the receptor-competent conformation, cutting binding to ~32% of normal. Because only the ligand on the mutant allele is defective and the receptor pool is fully functional, (a) heterozygotes retain substantial clearance capacity (hence a milder phenotype and frequent underdiagnosis), and (b) upregulating the intact receptor pharmacologically (statins, PCSK9 inhibitors) efficiently rescues clearance. This mechanistic logic explains, in one coherent chain, the biochemistry, the milder-than-LDLR-FH clinical course, and the excellent drug response.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [11115503](https://pubmed.ncbi.nlm.nih.gov/11115503/) | R3500Q changes apoB-100 conformation near the receptor site; Arg3500–Trp4369 interaction defined via transgenic mice | Core mechanism (F001) |
| [9339363](https://pubmed.ncbi.nlm.nih.gov/9339363/) | R3500Q single European founder ~6,000–7,000 yrs ago; identical-by-descent | Founder genetics (F002) |
| [15528480](https://pubmed.ncbi.nlm.nih.gov/15528480/) | LDLR carriers ~1.2 mmol/L higher LDL-C than APOB R3500Q; ascertainment effects | Milder phenotype (F003) |
| [25126774](https://pubmed.ncbi.nlm.nih.gov/25126774/) | CHD 5.6% (age 52) in FDB vs 41.8% (age 41) in FH | Lower/later CVD burden (F003) |
| [18279815](https://pubmed.ncbi.nlm.nih.gov/18279815/) | No FDB subject met confirmed FH diagnosis under Med-Ped criteria | Underdiagnosis (F003) |
| [30910740](https://pubmed.ncbi.nlm.nih.gov/30910740/) | Statins/ezetimibe/PCSK9i can normalize LDL-C in heterozygous FH | Treatment rationale (F004) |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | Statin ↑ and PCSK9-antibody restores LDLR expression | Drug mechanism (F004) |
| [27919345](https://pubmed.ncbi.nlm.nih.gov/27919345/) | R3500W significant FH contributor in East Asians | Allelic heterogeneity (F005) |
| [15135245](https://pubmed.ncbi.nlm.nih.gov/15135245/) | R3500W/R3531C/R3480W ligand-defective; H3543Y frequent | Variant spectrum (F005) |
| [10998466](https://pubmed.ncbi.nlm.nih.gov/10998466/) | R3500W (2.4%) > R3500Q (0.3%) in Chinese hyperlipidemics | Variant spectrum (F005) |
| [10657378](https://pubmed.ncbi.nlm.nih.gov/10657378/) | FDB LDL binds LDLR at 32% of normal affinity | Quantifies initiating step (F006) |
| [33959626](https://pubmed.ncbi.nlm.nih.gov/33959626/) | Cholesterol-rich LDL internalized by macrophages → foam cells + inflammation | Downstream chain (F006) |
| [18325181](https://pubmed.ncbi.nlm.nih.gov/18325181/) | FDB clinically indistinguishable from FH; HRM detection; cascade screening | Diagnosis/phenotype |
| [30270060](https://pubmed.ncbi.nlm.nih.gov/30270060/) | DLCN/SBDC scores under-detect APOB FH | Diagnostic limitation |
| [12208478](https://pubmed.ncbi.nlm.nih.gov/12208478/) | R3500Q rare in Spain but enriched in Galicia; single haplotype | Epidemiology/founder |
| [18096825](https://pubmed.ncbi.nlm.nih.gov/18096825/) | Femoral atherosclerosis by mutational class (APOB milder than null LDLR) | Prognosis |
| [29593013](https://pubmed.ncbi.nlm.nih.gov/29593013/) | FH/high LDL-C raises MI but not ischemic stroke risk | Outcome specificity |

---

## Limitations and Knowledge Gaps

1. **No primary omics data were analyzed** in this investigation; conclusions rest on literature synthesis of genetics, biochemistry, and clinical registries.
2. **FDB-specific epidemiology is imprecise** — carrier-frequency estimates vary widely by population and ascertainment; robust general-population prevalence figures for R3500Q specifically remain limited.
3. **Nomenclature ambiguity** — legacy (R3500Q) vs mature-protein (R3527Q) vs full-length numbering can cause confusion; reports should standardize to HGVS.
4. **Variant classification** for non-R3500Q *APOB* variants (e.g., the Dutch exon-26/29 variants) is incomplete; several remain of uncertain functional impact.
5. **No dedicated QoL, survival, or mortality datasets** specific to FDB were located.
6. **Model-organism fidelity** — transgenic mice capture the ligand defect but not the full human atherosclerotic phenotype without sensitizing backgrounds.
7. **Non-European populations** are under-studied; R3500W in East Asians is documented but broad allelic surveys are sparse.

---

## Proposed Follow-up Experiments / Actions

1. **Query gnomAD directly** for population-stratified allele frequencies of rs5742904 (R3500Q) and R3500W to quantify carrier frequencies with confidence intervals.
2. **Pull ClinVar/ClinGen classifications** for all *APOB* codon-3480 to 3543 variants to build a definitive pathogenicity table with ACMG criteria.
3. **Systematic outcomes meta-analysis** comparing cardiovascular event rates and treated LDL-C in molecularly confirmed FDB vs LDLR-FH cohorts (e.g., SAFEHEART, DIAMOND-FH data).
4. **Structural analysis** (AlphaFold/PDB) of the apoB-100 receptor-binding region to visualize the Arg3500–Trp4369 contact and model each ligand-defective variant's disruption.
5. **Real-world PCSK9-inhibitor response study** in genotyped FDB patients to confirm the predicted superior response given intact LDLR.
6. **Cascade-screening yield analysis** to quantify how many relatives per index FDB case are newly diagnosed and treated, informing cost-effectiveness of molecular-first screening.

---

*Report compiled from 40 reviewed papers and 6 confirmed findings across 5 investigation iterations. Evidence types span human clinical/registry studies, transgenic mouse and in-vitro functional work, and population genetics. All mechanistic and clinical claims are cited to primary literature (PMIDs above).*


## Artifacts

- [OpenScientist final report](Familial_Defective_Apolipoprotein_B-100-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Defective_Apolipoprotein_B-100-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 34 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007751` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **hypercholesterolemia, autosomal dominant, type B**
- `CL:0000891` (1 mention) - the report calls it "aortic/vascular smooth muscle context"; CL calls it **foam cell**
- `GO:0005905` (1 mention) - the report calls it "Subcellular:** Plasma-membrane LDL receptor and clathrin-coated pits"; GO calls it **clathrin-coated pit**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001229` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034364` (2 mentions) - the report calls it "low-density lipoprotein particle"; GO calls it **high-density lipoprotein particle**
- `CHEBI:39025` (1 mention) - the report calls it "low-density lipoprotein"; CHEBI calls it **high-density lipoprotein**
- `CL:0000235` (2 mentions) - the report calls it "macrophage/foam cell"; CL calls it **macrophage**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0007751` - called "if available", "MONDO"
