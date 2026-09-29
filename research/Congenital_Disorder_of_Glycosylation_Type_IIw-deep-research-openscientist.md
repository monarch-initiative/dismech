---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T14:39:46.558056'
end_time: '2026-09-03T14:52:33.011499'
duration_seconds: 766.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: congenital disorder of glycosylation type IIw (SLC37A4-CDG)
  mondo_id: MONDO:0030437
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
citation_count: 9
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 28
  not_found: 0
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0030437
    reported_labels:
    - SLC37A4-CDG / CDG-IIw
    ontology_label: congenital disorder of glycosylation, type IIw
  obsolete_terms:
  - term_id: GO:0016021
    ontology_label: GO_0016021
    replaced_by: GO:0016020
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: GO:0018242
    ontology_label: obsolete protein O-linked glycosylation via serine
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Disorder_of_Glycosylation_Type_IIw-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Disorder_of_Glycosylation_Type_IIw-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** congenital disorder of glycosylation type IIw (SLC37A4-CDG)
- **MONDO ID:** MONDO:0030437 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **congenital disorder of glycosylation type IIw (SLC37A4-CDG)** covering all of the
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

# Congenital Disorder of Glycosylation Type IIw (SLC37A4-CDG): A Comprehensive Disease Characterization Report

**Disease:** Congenital disorder of glycosylation type IIw (SLC37A4-CDG)
**MONDO ID:** MONDO:0030437 · **OMIM:** 619525 · **Category:** Mendelian (autosomal dominant)
**Gene:** *SLC37A4* (glucose-6-phosphate transporter, G6PT / G6PT1) · **HGNC:** 4061

---

## Summary

SLC37A4-CDG (also designated congenital disorder of glycosylation type IIw, CDG-IIw; OMIM 619525; MONDO:0030437) is an **ultra-rare, autosomal-dominant Type II congenital disorder of glycosylation** caused by a **single recurrent, mostly *de novo* nonsense variant** in *SLC37A4*: **c.1267C>T (p.Arg423\*)**. This is a striking example of one gene producing two mechanistically opposite diseases. Biallelic **loss-of-function** of *SLC37A4* causes the classical autosomal-recessive **glycogen storage disease type 1b (GSD1b)**. In contrast, the heterozygous p.Arg423\* truncation removes the C-terminal endoplasmic reticulum (ER)-retention signal of the glucose-6-phosphate transporter (G6PT) while leaving the transporter's catalytic transport function largely intact. The truncated protein is **mislocalized from the ER to the Golgi apparatus**, where its presence disrupts Golgi glycosylation homeostasis and produces a congenital disorder of glycosylation rather than a glycogen storage disease.

Clinically, SLC37A4-CDG presents in infancy or childhood with **hepatopathy (liver dysfunction)** and a **severe, liver-derived multifactorial coagulopathy** — characteristically combining **antithrombin deficiency with factor XI deficiency** (and less often protein C, protein S, or factor IX deficiency), a profile that is distinct from the coagulation derangements of liver failure, disseminated intravascular coagulation (DIC), or vitamin K deficiency. Both bleeding and thrombotic complications can occur. Variable **cardiac involvement** and other multisystem features are also reported. Biochemically, patients show a **Type II serum transferrin/N-glycan pattern**, abnormal serum N-glycoprotein glycoforms, abnormal **bikunin proteoglycan isoforms**, and **endoglycosidase-H-sensitive serum N-glycans**, reflecting immature Golgi N-glycan processing and combined N-/O-glycosylation plus proteoglycan defects.

Diagnosis rests on recognition of the Type II CDG biochemical signature confirmed by **molecular identification of the recurrent c.1267C>T (p.Arg423\*) variant**, typically via exome or genome sequencing. There is **no curative or disease-specific therapy**; management is **supportive**, centered on correcting the coagulopathy (plasma/factor replacement, careful peri-procedural hemostatic monitoring) and surveillance of liver and cardiac function. Because the disorder is defined by a small number of published cases (roughly a dozen individuals across the founding reports), much of the epidemiology, natural history, penetrance, and prognosis remains incompletely characterized.

---

## Key Findings

### Finding 1 — A single recurrent dominant variant (p.Arg423\*) mislocalizes G6PT to the Golgi and causes CDG-IIw

SLC37A4-CDG is caused by a **recurrent heterozygous, predominantly *de novo* variant, c.1267C>T (p.Arg423\*)** in *SLC37A4*. Three independent reports converge on this identical variant. Marquardt et al. (2020) established the molecular mechanism: the nonsense mutation truncates the C-terminal cytoplasmic tail of the glucose-6-phosphate transporter, abolishing its ER-retention signal and creating a weak Golgi-retention signal, so the transporter is intracellularly **mislocalized to the Golgi**. As the authors state, *"The mutation abolishes the ER retention signal of the transporter and generates a weak Golgi retention signal. Intracellular mislocalization of the transporter leads to a congenital disorder of glycosylation instead of glycogen storage disease"* [PMID: 32884905].

Ng et al. (2021) reported a cohort of **seven heterozygous individuals** carrying the same variant, defining the core clinical triad: *"We report seven individuals who presented with liver dysfunction multifactorial coagulation deficiency and cardiac issues and were heterozygous for the same variant, c.1267C>T (p.Arg423\*)"* [PMID: 33964207]. Wilson et al. (2021) independently described a second patient with the identical heterozygous *de novo* c.1267C>T (p.R423\*) substitution [PMID: 33728255], reinforcing the recurrent, mutation-specific nature of the disorder.

This is the defining genetic feature of the disease: rather than a spectrum of loss-of-function alleles (as in recessive GSD1b), CDG-IIw is essentially a **single-variant, gain-of-mislocalization dominant disorder**.

### Finding 2 — The disorder produces a Type II CDG serum pattern with combined N-/O-glycosylation and proteoglycan defects and a liver-derived coagulopathy

Raynor et al. (2021) provided detailed biochemical characterization of **six affected individuals**, demonstrating that the disorder involves multiple, simultaneous glycosylation abnormalities arising from disrupted Golgi homeostasis. They found *"abnormal patterns for various serum N-glycoproteins and bikunin proteoglycan isoforms, together with specific alterations of the mass spectra of endoglycosidase H-released serum N-glycans"* [PMID: 34245688]. The endoglycosidase-H sensitivity of serum N-glycans indicates **incomplete/immature Golgi processing** of N-glycans — a hallmark of a Type II (Golgi-level) CDG.

Critically, the same work established the two central disease-level features: SLC37A4-CDG is *"characterized by a dominant inheritance and a major coagulopathy originating from the liver"* [PMID: 34245688]. The combination of abnormal N-glycoprotein glycoforms, altered O-linked proteoglycan (bikunin) isoforms, and a profound liver-derived hemostatic disturbance distinguishes this from other CDGs and from primary hepatic disease. Ng et al. (2021) corroborated the coagulation and hepatic phenotype in their seven-patient heterozygous cohort [PMID: 33964207].

### Finding 3 — SLC37A4 encodes the ER glucose-6-phosphate transporter; its normal biology explains why a C-terminal truncation causes CDG rather than GSD

*SLC37A4* encodes a **429-amino-acid, ~10-transmembrane-helix ER membrane protein** (G6PT) that transports glucose-6-phosphate (G6P) from the cytoplasm into the ER lumen, where glucose-6-phosphatase hydrolyzes it — a reaction central to glucose homeostasis and gluconeogenesis/glycogenolysis. Xia et al. (2025) solved cryo-EM structures of human G6PT (apo, G6P-bound, and chlorogenic-acid-bound), defining a substrate pocket with **subsite A (binding the phosphate)** and **subsite B (binding the glucose moiety)**, and showed that G6PT transport activity is enhanced by co-expression of glucose-6-phosphatase (G6PC) although the two proteins do not form a stable complex. As they summarize, *"The human glucose-6-phosphate transporter (G6PT) moves glucose-6-phosphate (G6P) into the lumen of endoplasmic reticulum, playing a vital role in glucose homeostasis"* [PMID: 41136424].

The key to understanding CDG-IIw lies in the transporter's C-terminus. Chen et al. (2000) showed that the C-terminal cytoplasmic tail contributes to folding/stability but that its most distal residues are dispensable for transport function: *"amino acids 415-417 in the cytoplasmic tail of the carboxyl-domain, extending from helix 10, also play a critical role in the correct folding of the transporter. However, the last 12 amino acids of the cytoplasmic tail play no essential role(s) in functional integrity"* [PMID: 10940311]. Because p.Arg423\* truncates only the terminal residues, the mutant transporter **retains its transport capability but loses the C-terminal ER-targeting/retention signal** — precisely the combination that produces mislocalization to the Golgi (Finding 1) rather than a non-functional transporter. This mechanistic contrast explains why the dominant CDG is biochemically opposite to the recessive GSD1b caused by biallelic loss-of-function.

### Finding 4 — Diagnosis combines a Type II serum transferrin/N-glycan signature with molecular confirmation; treatment is supportive

Diagnostic biochemistry integrates several assays: abnormal serum N-glycoprotein glycoforms (a **Type II CDG transferrin pattern**), abnormal bikunin proteoglycan isoforms, and endoglycosidase-H-sensitive serum N-glycans reflecting immature Golgi processing [PMID: 34245688; 33728255; 32884905]. Raynor et al. explicitly note the diagnostic utility of these markers: *"these data complement previous findings, help to better delineate SLC37A4-CDG and could present interest in diagnosing this disease"* [PMID: 34245688]. Definitive diagnosis requires **molecular confirmation of the recurrent heterozygous de novo c.1267C>T (p.Arg423\*)** variant, generally identified via exome/genome sequencing or targeted testing.

Unlike GSD1b, the dominant CDG is distinguished by a **liver-derived coagulopathy** as its dominant feature, rather than the fasting hypoglycemia and chronic neutropenia that dominate GSD1b. **No disease-specific or curative therapy exists**; management is supportive and centers on correcting the coagulopathy (plasma or factor replacement as clinically indicated) and monitoring liver and cardiac function. As therapeutic context, sugar-substrate approaches have been trialed in the related *SLC37A4* disorder GSD1b — *"we hypothesized the same pathomechanism in GSD-Ib and started a therapeutic trial with oral galactose and uridine"* [PMID: 28126686] — but such approaches have not been established for CDG-IIw.

### Finding 5 — The CDG coagulopathy has a characteristic factor profile that distinguishes it from liver failure, DIC, and vitamin K deficiency

Pascreau et al. (2023), in an ISTH state-of-the-art review of hemostatic defects in CDGs, defined the characteristic coagulation signature that applies to SLC37A4-CDG's liver-derived coagulopathy. CDG patients *"often present coagulation abnormalities characterized by low levels of procoagulant or anticoagulant factors. Antithrombin deficiency is frequently associated with factor XI deficiency and less frequently with a protein C, protein S, or factor IX deficiency. This coagulation profile differs from those observed in liver failure, disseminated intravascular coagulation, and vitamin K deficiency"* [PMID: 37193126]. This distinctive combination — **antithrombin + factor XI deficiency** as the core, with variable protein C/S and factor IX involvement — is diagnostically valuable because it separates a glycosylation-based coagulopathy from more common acquired causes.

Importantly, the hemostatic balance in CDG is precarious and bidirectional: *"Coagulopathy can lead to thrombotic and/or hemorrhagic complications"* [PMID: 37193126]. Patients are therefore at risk of **both bleeding and thrombosis**, requiring close hemostatic monitoring especially during acute illness, surgery, or other physiologic stress.

---

## Mechanistic Model / Interpretation

### Ordered causal chain

```
1. De novo point mutation SLC37A4 c.1267C>T  (germline, heterozygous)
        │  results in
        ▼
2. Premature stop codon p.Arg423* → truncation of the C-terminal
   cytoplasmic tail of the glucose-6-phosphate transporter (G6PT)
        │  which
        ▼
3. Removes the C-terminal ER-retention signal AND creates a weak
   Golgi-retention signal  (transport function itself preserved,
   because the distal ~12 residues are dispensable for transport)
        │  leads to
        ▼
4. Intracellular MISLOCALIZATION of G6PT from the ER to the Golgi
   apparatus  (dominant, gain-of-mislocalization effect)
        │  results in
        ▼
5. Disruption of Golgi glycosylation homeostasis
        │
        ├─► 5a. Impaired Golgi N-glycan maturation
        │        → endoglycosidase-H-sensitive serum N-glycans;
        │          Type II serum transferrin pattern
        │
        ├─► 5b. Abnormal O-linked proteoglycan processing
        │        → abnormal bikunin isoforms
        │
        └─► 5c. Under-/aberrant glycosylation of hepatically
                 synthesized glycoproteins (incl. coagulation factors
                 and their regulators)
        │  leads to
        ▼
6. Multisystem clinical manifestations:
     • Hepatopathy (liver dysfunction)
     • Liver-derived multifactorial coagulopathy
        (antithrombin ↓ + factor XI ↓ ± protein C/S ↓, factor IX ↓)
        → bleeding AND/OR thrombosis risk
     • Variable cardiac involvement
     • Other variable multisystem features
```

Steps 1–4 are directly demonstrated (mutation identification and cell-biological localization studies). Step 5 is supported by serum glycomics/proteoglycan data. The precise molecular link between Golgi-mislocalized G6PT and specific downstream glycosylation-enzyme dysfunction (step 5 → 6) is **partly inferred**: exactly how a mislocalized sugar-phosphate transporter perturbs Golgi glycosyltransferase/nucleotide-sugar homeostasis has not been fully resolved and represents the principal open mechanistic question.

### One gene, two opposite diseases

| Feature | GSD1b (recessive) | SLC37A4-CDG / CDG-IIw (dominant) |
|---|---|---|
| Gene | *SLC37A4* | *SLC37A4* |
| Inheritance | Autosomal recessive | Autosomal dominant (mostly *de novo*) |
| Molecular defect | Biallelic loss-of-function | Recurrent p.Arg423\* truncation |
| Effect on transporter | Non-functional / absent transport | Transport preserved, ER-retention lost |
| Localization | ER (or degraded) | **Mislocalized to Golgi** |
| Disease class | Glycogen storage disease | Congenital disorder of glycosylation (Type II) |
| Hallmark features | Fasting hypoglycemia, hepatomegaly, neutropenia | Hepatopathy, liver-derived coagulopathy, cardiac issues |
| Glycosylation | Normal | Abnormal (Type II serum transferrin, EndoH-sensitive N-glycans, abnormal bikunin) |

### Ontology term suggestions

- **Disease:** MONDO:0030437 (SLC37A4-CDG / CDG-IIw)
- **Gene/Protein (GO / cellular component):** GO:0005783 endoplasmic reticulum; GO:0005794 Golgi apparatus; GO:0016021 integral component of membrane; GO:0015152 glucose-6-phosphate transmembrane transporter activity; GO:0015760 glucose-6-phosphate transport
- **Biological process:** GO:0006486 protein glycosylation; GO:0006487 protein N-linked glycosylation; GO:0018242 protein O-linking; GO:0006094 gluconeogenesis; GO:0042593 glucose homeostasis
- **Cell types (CL):** CL:0000182 hepatocyte (primary site of coagulation-factor synthesis); CL:0000091 Kupffer cell (context)
- **Anatomy (UBERON):** UBERON:0002107 liver; UBERON:0000948 heart; UBERON:0001981 blood vessel (thrombosis/bleeding)
- **Chemical entities (CHEBI):** CHEBI:4170 D-glucose 6-phosphate; CHEBI:17234 glucose; CHEBI:16709 1,5-anhydro-D-glucitol (1,5-AG; relevant to related G6PT neutropenia biology)

---

## Section-by-Section Characterization

### 1. Disease Information
SLC37A4-CDG is a Mendelian, autosomal-dominant Type II congenital disorder of glycosylation caused by mislocalization of the ER glucose-6-phosphate transporter to the Golgi. **Identifiers:** MONDO:0030437; OMIM 619525; synonyms include **CDG-IIw**, **congenital disorder of glycosylation type IIw**, **SLC37A4-CDG**. It is distinct from GSD1b (also *SLC37A4*, OMIM 232220). Information is derived from **aggregated, disease-level case reports and small case series** (Marquardt 2020; Ng 2021; Wilson 2021; Raynor 2021), not from EHR/population resources.

### 2. Etiology
**Primary cause:** monogenic — the recurrent heterozygous *SLC37A4* c.1267C>T (p.Arg423\*) variant [PMID: 32884905; 33964207; 33728255]. **Genetic risk factor:** this specific variant is the sole known cause; no susceptibility loci or modifier genes are established. Most cases are *de novo*, so an affected parent is not required. **Environmental risk/protective factors and gene-environment interactions:** none established; the disorder is not known to depend on environmental triggers. No protective alleles are known.

### 3. Phenotypes
Reported phenotypes (from small cohorts) with suggested HPO terms:

| Phenotype | Type | Onset | Frequency (small cohorts) | HPO suggestion |
|---|---|---|---|---|
| Liver dysfunction / hepatopathy | Lab + clinical | Infancy–childhood | Core / most patients | HP:0001392 Abnormality of the liver; HP:0002910 Elevated hepatic transaminase |
| Multifactorial coagulopathy | Lab abnormality | Infancy–childhood | Core / most patients | HP:0001928 Abnormality of coagulation |
| Antithrombin deficiency | Lab abnormality | Variable | Characteristic | HP:0032154 Reduced antithrombin III activity |
| Factor XI deficiency | Lab abnormality | Variable | Frequent | HP:0004866 Abnormal factor XI |
| Bleeding and/or thrombosis | Clinical sign | Variable/episodic | Variable | HP:0001892 Abnormal bleeding; HP:0001977 Abnormal thrombosis |
| Cardiac involvement | Clinical sign | Variable | Reported in Ng cohort | HP:0001627 Abnormal heart morphology |
| Abnormal serum transferrin glycosylation | Lab abnormality | Congenital | Diagnostic | HP:0003642 Abnormal isoelectric focusing of serum transferrin |

Severity is **variable**; the coagulopathy can be severe and life-threatening. Quality-of-life data specific to CDG-IIw are not available given the tiny cohort.

### 4. Genetic / Molecular Information
**Causal gene:** *SLC37A4* (HGNC:4061), OMIM gene 602671, chromosome 11q23.3. **Pathogenic variant:** c.1267C>T, p.Arg423\* — a **nonsense/truncating** variant; recurrent and mostly *de novo*; classified pathogenic. **Functional consequence:** not a simple loss of function but a **dominant gain-of-mislocalization** (ER→Golgi) with preserved transport activity [PMID: 32884905; 10940311]. Allele frequency: effectively absent from population databases (private/de novo). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for CDG-IIw. (Note: for the related GSD1b/neutropenia biology, heterozygous *SLC5A10*/SGLT5 variants modify 1,5-AG handling [PMID: 35506446; 37594549], but this is not established as a modifier of CDG-IIw.)

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are known. The disease is purely genetic.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain. In brief: mutation → C-terminal truncation → loss of ER-retention + weak Golgi-retention → Golgi mislocalization of G6PT → disrupted Golgi glycosylation homeostasis → Type II N-glycan, O-glycan/proteoglycan, and coagulation-factor glycosylation defects → hepatopathy, coagulopathy, cardiac and multisystem manifestations. Molecular profiling to date is **glycomic/proteomic** (serum N-glycans, bikunin isoforms) [PMID: 34245688]; no transcriptomic, single-cell, or CRISPR-screen data specific to CDG-IIw are published.

### 7. Anatomical Structures Affected
**Primary organ:** liver (UBERON:0002107) — the source of the coagulopathy and site of hepatopathy. **Secondary/variable:** heart (UBERON:0000948); vasculature (thrombosis/hemorrhage). **Body systems:** hepatobiliary, hematologic/coagulation, cardiovascular. **Subcellular compartments:** endoplasmic reticulum (GO:0005783) and **Golgi apparatus (GO:0005794)** — the compartment where the mislocalized transporter exerts its pathogenic effect. **Cell type:** hepatocyte (CL:0000182). **Lateralization:** not applicable (systemic/metabolic disorder).

### 8. Temporal Development
**Onset:** congenital/pediatric — clinical presentation in infancy to childhood [PMID: 33964207]. **Course:** chronic, lifelong; the coagulopathy is a persistent risk that can fluctuate/episodically worsen with illness or procedures. Progression rate and long-term natural history are not well defined given limited follow-up. **Critical periods:** peri-procedural/peri-surgical and acute-illness windows are periods of heightened hemostatic vulnerability.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant, predominantly **de novo** [PMID: 32884905; 33964207; 33728255]. **Penetrance/expressivity:** appears highly penetrant for the specific variant but with **variable expressivity**; formal estimates are lacking. **Epidemiology:** ultra-rare — only ~10–14 individuals reported across the founding papers; true prevalence/incidence unknown. No founder effect, consanguinity role (not applicable for dominant de novo), sex bias, or ethnic predilection has been established. **Carrier frequency:** not applicable (dominant, de novo).

### 10. Diagnostics
**Biochemical screening:** Type II serum transferrin isoform pattern; abnormal serum N-glycoprotein glycoforms; abnormal bikunin proteoglycan isoforms; **endoglycosidase-H-sensitive serum N-glycans** [PMID: 34245688]. **Coagulation testing:** the characteristic **antithrombin + factor XI deficiency** profile (± protein C/S, factor IX) helps distinguish it from liver failure, DIC, and vitamin K deficiency [PMID: 37193126]. **Molecular confirmation:** identification of the recurrent heterozygous *SLC37A4* c.1267C>T (p.Arg423\*) variant — best via **whole-exome or whole-genome sequencing**, or targeted single-variant/single-gene testing. **Differential diagnosis:** GSD1b (recessive, same gene — but hypoglycemia/neutropenia dominant), other Type II CDGs, primary hepatic coagulopathy, DIC, vitamin K deficiency.

### 11. Outcome / Prognosis
No formal survival, mortality, or quality-of-life statistics exist for this ultra-rare disorder. The dominant prognostic concern is the **liver-derived coagulopathy**, which carries risk of both **hemorrhagic and thrombotic complications** [PMID: 37193126], alongside hepatopathy and variable cardiac involvement. Prognosis appears variable; close hemostatic and hepatic monitoring is the mainstay of risk reduction.

### 12. Treatment
**No curative or disease-specific therapy.** Management is **supportive**: correction of the coagulopathy with plasma and/or specific factor/anticoagulant-factor replacement guided by the individual factor profile, careful peri-procedural hemostatic planning, and surveillance/support of liver and cardiac function. Antithrombin concentrate and factor replacement may be considered for the specific deficiencies; anticoagulation decisions must balance the bidirectional bleeding/thrombosis risk. Sugar-substrate therapy (e.g., oral galactose ± uridine) has been trialed in the related disorder GSD1b [PMID: 28126686] but is **not established** for CDG-IIw. **Suggested NCIT terms:** NCIT:C15311 Supportive Care; NCIT:C561 Fresh Frozen Plasma; NCIT:C1685 Coagulation Factor.

### 13. Prevention
No primary prevention exists (mostly de novo). **Secondary prevention** = early biochemical/molecular diagnosis to guide hemostatic management and prevent bleeding/thrombotic events. **Tertiary prevention** = peri-procedural coagulation-factor optimization and organ-function surveillance. **Genetic counseling** is appropriate: recurrence risk for parents of a de novo case is low, but an affected individual would have a 50% transmission risk. **Prenatal/preimplantation testing** is technically feasible once the familial variant is known.

### 14. Other Species / Natural Disease
No naturally occurring animal disease attributable to this specific dominant *Slc37a4* mislocalization variant is reported. **Orthologs:** mouse *Slc37a4*, rat *Slc37a4* (well-conserved). Existing *Slc37a4* animal models pertain to the recessive GSD1b/neutropenia biology, not CDG-IIw. No zoonotic or cross-species relevance.

### 15. Model Organisms
No dedicated CDG-IIw animal model is published to date. Mechanistic work has relied on **in vitro cell-based localization studies** demonstrating ER→Golgi mislocalization of the mutant transporter [PMID: 32884905] and on **structural biology** (cryo-EM of human G6PT) [PMID: 41136424]. A knock-in mouse carrying the equivalent of p.Arg423\* would be the logical model to recapitulate the dominant CDG phenotype and is a key gap.

---

## Evidence Base

| PMID | Title (abbrev.) | Type | Contribution |
|---|---|---|---|
| [32884905](https://pubmed.ncbi.nlm.nih.gov/32884905/) | *SLC37A4-CDG: Mislocalization of G6PT to the Golgi* | Human + in vitro | Defines the founding mechanism: p.Arg423\* abolishes ER-retention, creates weak Golgi-retention → mislocalization → CDG not GSD |
| [33964207](https://pubmed.ncbi.nlm.nih.gov/33964207/) | *A mutation in SLC37A4 causes a dominantly inherited CDG* | Human (n=7) | Establishes recurrent variant + core triad: liver dysfunction, coagulopathy, cardiac issues |
| [33728255](https://pubmed.ncbi.nlm.nih.gov/33728255/) | *SLC37A4-CDG: Second patient* | Human case | Independent confirmation of recurrent de novo c.1267C>T (p.R423\*) |
| [34245688](https://pubmed.ncbi.nlm.nih.gov/34245688/) | *SLC37A4-CDG: New biochemical insights ... major coagulopathy* | Human (n=6) | Type II serum N-glycan / bikunin / EndoH signature; defines dominant inheritance + liver-derived coagulopathy; diagnostic markers |
| [41136424](https://pubmed.ncbi.nlm.nih.gov/41136424/) | *Structural basis for transport/inhibition of G6PT* | Structural (cryo-EM) | Defines normal G6PT function, G6P binding subsites, G6PC interaction |
| [10940311](https://pubmed.ncbi.nlm.nih.gov/10940311/) | *Structural requirements for stability/transport of G6PT* | In vitro | Shows C-terminal distal residues dispensable for transport → explains why p.Arg423\* retains function while losing ER targeting |
| [37193126](https://pubmed.ncbi.nlm.nih.gov/37193126/) | *Hemostatic defects in CDGs* | Review (ISTH) | Defines characteristic AT + FXI deficiency profile distinguishing CDG coagulopathy from liver failure/DIC/vitamin-K deficiency; bidirectional risk |
| [28126686](https://pubmed.ncbi.nlm.nih.gov/28126686/) | *Oral galactose therapy in GSD1b* | Human trial | Therapeutic context for related SLC37A4 disorder (sugar-substrate approach) |

Supporting/background literature on G6PT biology and GSD1: [10598822](https://pubmed.ncbi.nlm.nih.gov/10598822/), [10518030](https://pubmed.ncbi.nlm.nih.gov/10518030/), [25804016](https://pubmed.ncbi.nlm.nih.gov/25804016/), [12192101](https://pubmed.ncbi.nlm.nih.gov/12192101/), [11560776](https://pubmed.ncbi.nlm.nih.gov/11560776/), [11121425](https://pubmed.ncbi.nlm.nih.gov/11121425/), [10712583](https://pubmed.ncbi.nlm.nih.gov/10712583/), and the SGLT5/1,5-AG neutropenia biology in related G6PT deficiency [35506446](https://pubmed.ncbi.nlm.nih.gov/35506446/), [37594549](https://pubmed.ncbi.nlm.nih.gov/37594549/).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** The disease is defined by roughly a dozen published individuals, all carrying the same variant. Prevalence, incidence, penetrance estimates, sex ratio, natural history, and long-term prognosis are essentially unquantified.
2. **Mechanistic gap at step 5.** How a Golgi-mislocalized glucose-6-phosphate transporter specifically perturbs Golgi glycosylation enzymes / nucleotide-sugar or ion homeostasis is inferred, not mechanistically resolved. The link between the transporter's mislocalization and the observed N-/O-glycan and proteoglycan defects needs direct experimental demonstration.
3. **No animal model.** All mechanistic data are in vitro/structural; there is no in vivo model recapitulating the dominant CDG phenotype.
4. **Genotype restricted to one variant.** It is unknown whether other C-terminal truncating or ER-retention-disrupting variants could produce the same dominant CDG; the phenotype is currently variant-specific.
5. **No therapy data.** Management is empirically supportive; no trials, treatment-response rates, or targeted therapeutics exist for CDG-IIw specifically.
6. **Quality-of-life and outcome instruments** have not been applied to this cohort.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse (or zebrafish) model** carrying the murine equivalent of p.Arg423\* to test whether Golgi mislocalization reproduces the hepatopathy, Type II glycosylation defect, and coagulopathy in vivo.
2. **Direct Golgi mechanistic studies:** in hepatocyte-like cells (e.g., patient iPSC-derived hepatocytes or organoids), map how mislocalized G6PT alters Golgi nucleotide-sugar/ion pools and glycosyltransferase activity — closing the step-5 inference gap.
3. **Systematic coagulation-factor phenotyping** across all reported and future patients to quantify the frequency of antithrombin, factor XI, protein C/S, and factor IX deficiencies and correlate with bleeding/thrombosis events, informing prophylaxis algorithms.
4. **Establish an international patient registry** to capture natural history, penetrance, cardiac phenotype spectrum, and long-term outcomes.
5. **Structure-guided variant survey:** use the cryo-EM G6PT structure [PMID: 41136424] and the C-terminal targeting data [PMID: 10940311] to predict and functionally test whether additional C-terminal variants can cause CDG-IIw, refining the genotype definition.
6. **Test candidate supportive/targeted therapies** (e.g., glycosylation-substrate supplementation, factor-specific replacement strategies) in the model system before clinical translation.

---

*Report compiled from the confirmed knowledge state of a 5-iteration autonomous investigation. Evidence source types: human clinical case series (Marquardt, Ng, Wilson, Raynor), in vitro cell biology and biochemistry, structural biology (cryo-EM), and a clinical review of CDG hemostasis. Where data are absent for this ultra-rare disorder, this has been stated explicitly.*


## Artifacts

- [OpenScientist final report](Congenital_Disorder_of_Glycosylation_Type_IIw-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Disorder_of_Glycosylation_Type_IIw-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030437` (4 mentions) - the report calls it "SLC37A4-CDG / CDG-IIw"; MONDO calls it **congenital disorder of glycosylation, type IIw**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016021` (GO_0016021) (1 mention) - replaced by `GO:0016020`
- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`
- `GO:0018242` (obsolete protein O-linked glycosylation via serine) (1 mention)