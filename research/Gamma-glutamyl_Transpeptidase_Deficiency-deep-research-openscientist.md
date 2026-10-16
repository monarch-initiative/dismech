---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T02:48:31.536853'
end_time: '2026-10-15T03:05:50.702117'
duration_seconds: 1039.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Gamma-glutamyl Transpeptidase Deficiency
  mondo_id: MONDO:0009285
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
citation_count: 13
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 17
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:26536828
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 12
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009285
    reported_labels:
    - MONDO
    ontology_label: gamma-glutamyl transpeptidase deficiency
  - term_id: HP:0001249
    reported_labels:
    - Clinical sign
    ontology_label: Intellectual disability
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0006534
    ontology_label: obsolete cysteine metabolic process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Gamma-glutamyl_Transpeptidase_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Gamma-glutamyl_Transpeptidase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gamma-glutamyl Transpeptidase Deficiency
- **MONDO ID:** MONDO:0009285 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gamma-glutamyl Transpeptidase Deficiency** covering all of the
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

# Gamma-glutamyl Transpeptidase Deficiency (Glutathionuria): Comprehensive Disease Characteristics Report

**Disease:** Gamma-glutamyl Transpeptidase Deficiency (Glutathionuria)
**MONDO ID:** MONDO:0009285 · **OMIM:** 231950 · **Category:** Mendelian (autosomal recessive inborn error of metabolism)
**Report date:** 2026-10-15

---

## Summary

Gamma-glutamyl transpeptidase (GGT) deficiency, historically termed **glutathionuria**, is an **ultra-rare autosomal recessive inborn error of the γ-glutamyl (glutathione) cycle** caused by biallelic loss-of-function variants in **GGT1** on chromosome 22q11.23. The disease was described biochemically in the 1970s–1980s but its molecular cause was only proven in 2018, when whole-genome sequencing of two affected siblings revealed a **16.9 kb homozygous intragenic deletion in GGT1**, with the parents and a healthy sibling confirmed as carriers/wild-type — providing the first direct genetic evidence of autosomal recessive inheritance [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/).

The **core biochemical defect** is a failure of extracellular glutathione (GSH) catabolism. GGT is a membrane-bound ectoenzyme on the apical (brush-border) surface of transport/secretory epithelia — most importantly the renal proximal tubule — where it initiates breakdown of filtered and plasma glutathione and salvages cysteine. When the enzyme is absent, glutathione cannot be reclaimed and is lost in the urine. This produces the diagnostic hallmark of **glutathionuria plus glutathionemia**, accompanied by elevated plasma γ-glutamylcysteine, cysteine and cysteinylglycine, with serum/tissue GGT activity that is very low or undetectable. Notably, plasma amino acid levels and renal amino acid reabsorption remain normal, demonstrating that the γ-glutamyl cycle is **not** essential for amino acid transport.

The **human clinical phenotype** is remarkably mild relative to the dramatic biochemical abnormality: fewer than ~8 patients have ever been reported, and the dominant features are **neurological/cognitive** (intellectual disability, developmental delay, behavioral problems), with variable, generally mild, expressivity. By contrast, **Ggt1-knockout and ENU-mutant mice** display a severe multisystem phenotype — growth failure, cataracts, lethargy, infertility, osteopenia and shortened lifespan — all traced to **systemic cysteine/GSH depletion** and all **reversible with cysteine repletion** (N-acetylcysteine or the cysteine prodrug L-2-oxothiazolidine-4-carboxylate, OTZ). The species discrepancy likely reflects paralog redundancy (the human GGT family has 13 homologous genes) and differences in GSH handling. No approved disease-specific therapy exists for humans; management is supportive, and prevention relies on genetic counseling and cascade testing. Mechanistic causality (cysteine depletion as the proximate cause) is proven only in the mouse model and is inferred, but not formally trialed, in humans.

---

## 1. Disease Information

**Overview.** GGT deficiency is a Mendelian inborn error of metabolism in which absence of the ectoenzyme gamma-glutamyl transpeptidase blocks the first step of extracellular glutathione degradation. The clinical and biochemical entity is defined by massive urinary and plasma glutathione accumulation ("glutathionuria" / "glutathionemia") in the setting of absent GGT enzyme activity.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009285 |
| OMIM | 231950 (Glutathionuria) |
| Gene | GGT1 — HGNC:4250; NCBI Gene 2678; Ensembl ENSG00000100031 |
| Cytogenetic locus | 22q11.23 (GRCh38 chr22:24,594,811–24,629,005) |
| Orphanet | Glutathionuria (gamma-glutamyltransferase deficiency) — rare metabolic disease |
| MeSH | Closest concepts: "gamma-Glutamyltransferase"; "Glutathione / metabolism" |

**Synonyms / alternative names:** Glutathionuria; Gamma-glutamyltransferase deficiency; Gamma-glutamyl transferase deficiency; γ-GT deficiency; Glutathionemia (describes the associated plasma finding).

**Source of information.** The knowledge base is derived almost entirely from **aggregated disease-level resources and individual published case reports** (not EHR-scale data). The total human experience is **fewer than ~8 patients**, so the evidence is case-level, supplemented substantially by **mouse model** data. "A rare disease, with only six patients reported in the literature" [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/).

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic loss-of-function variants in GGT1**, inherited in an autosomal recessive pattern. The first molecular proof was a **16.9 kb homozygous intragenic deletion in GGT1 with a 13 bp insertion at the breakpoint** identified by whole-genome sequencing in two affected siblings: "Whole-genome sequencing revealed the presence of a 16.9 kb homozygous deletion in GGT1, one of the genes encoding enzymes with γ-glutamyl transpeptidase activity in the human genome" [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/). Earlier case series inferred autosomal recessive inheritance from reduced fibroblast GGT activity in clinically normal, presumably heterozygous, parents [PMID: 6118466](https://pubmed.ncbi.nlm.nih.gov/6118466/); [PMID: 238530](https://pubmed.ncbi.nlm.nih.gov/238530/).

**Genetic risk factors.** The sole established genetic risk factor is inheritance of two pathogenic GGT1 alleles. No susceptibility loci or modifier genes have been formally established in humans (the ultra-rare case count precludes association studies). gnomAD constraint metrics indicate GGT1 is moderately intolerant to heterozygous LOF (see Section 4), yet heterozygous carriers are clinically healthy, consistent with recessive disease.

**Environmental risk factors.** None established. There is no evidence that toxins, lifestyle, occupational exposure, age or sex trigger or modify the primary Mendelian disease. (Separately, acquired/pharmacologic GGT inhibition can phenocopy the biochemistry: administration of γ-glutamyl amino acids or transpeptidase inhibitors induces glutathionuria in mice — relevant mechanistically but not an etiology of the inherited disease [PMID: 2873573](https://pubmed.ncbi.nlm.nih.gov/2873573/); [PMID: 34150](https://pubmed.ncbi.nlm.nih.gov/34150/).)

**Protective factors.** None characterized in humans. In mice, provision of an alternative cysteine source (N-acetylcysteine, OTZ) is "protective" against the downstream consequences — not a protection against the genetic lesion itself but a bypass of its metabolic consequence.

**Gene–environment interactions.** Not characterized for this Mendelian disorder. Mechanistically, dietary cysteine/protein intake would be expected to modulate the severity of cysteine deficiency (as shown pharmacologically in mice), but this interaction has not been formally studied in human patients.

---

## 3. Phenotypes

The human phenotype is dominated by **neurological/cognitive and behavioral** features, superimposed on a profound but clinically "silent" biochemical abnormality.

| Phenotype | Type | HPO term (suggested) | Onset | Severity | Frequency (of reported cases) |
|---|---|---|---|---|---|
| Glutathionuria (massive urinary GSH) | Laboratory abnormality | — (metabolite; CHEBI:16856 glutathione) | Congenital/neonatal (biochemical) | Marked/constant | ~100% (defining) |
| Glutathionemia (elevated plasma GSH) | Laboratory abnormality | — | Congenital (biochemical) | Marked/constant | ~100% (defining) |
| Intellectual disability | Clinical sign | HP:0001249 | Childhood | Mild–moderate, variable | Several reported cases |
| Developmental delay / psychomotor delay | Clinical sign | HP:0001263 | Infancy/childhood | Mild | Molecularly confirmed siblings |
| Behavioral abnormality | Behavioral | HP:0000708 | Childhood | Variable (severe in one case) | Multiple cases |
| Mild neurological symptoms (non-specific) | Clinical sign | HP:0000707 (abnormality of nervous system) | Childhood | Mild | Confirmed cases |
| Tall, slender (Marfanoid) habitus | Physical manifestation | HP:0001519 / HP:0001548 | Childhood/adolescence | — | 1 case report |

Key supporting quotes: "A mentally retarded young woman with severe behaviour problems was found to excrete large amounts of glutathione due to a generalized gamma-glutamyl transpeptidase deficiency" [PMID: 6118466](https://pubmed.ncbi.nlm.nih.gov/6118466/); and the two molecularly confirmed siblings presented as "two siblings with mild psychomotor developmental delay and mild neurological symptoms, who presented a markedly increased excretion of glutathione in urine" [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/). Two Japanese brothers showed retarded mental development and a tall slender (Marfan-like) habitus [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/).

**Phenotype characteristics.** Onset is effectively **congenital** for the biochemical defect; clinical (cognitive/behavioral) features emerge in **childhood**. Severity is **variable and generally mild** in the genetically confirmed patients. Progression appears **stable/non-progressive** rather than degenerative, though natural-history data are essentially absent.

**Quality-of-life impact.** Not formally measured with any instrument (EQ-5D/SF-36/PROMIS). Impact is inferred to arise chiefly from the degree of intellectual disability and behavioral difficulties; the biochemical abnormality itself appears clinically well-tolerated.

---

## 4. Genetic / Molecular Information

**Causal gene.** **GGT1** (HGNC:4250; NCBI Gene 2678; Ensembl ENSG00000100031), chromosome **22q11.23**, GRCh38 chr22:24,594,811–24,629,005; canonical transcript ENST00000400382.

**Pathogenic variants.**
- The index molecularly proven lesion is a **16.9 kb homozygous intragenic deletion** (structural/copy-number variant) with a 13 bp insertion at the breakpoint — a **loss-of-function** allele requiring WGS/CNV analysis to detect (standard exome would likely miss it) [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/).
- Variant classification: **pathogenic** (biallelic LOF causing a loss-of-function disease).
- Variant types expected across the disorder: structural deletions, and (by inference) nonsense/frameshift/splice/missense LOF alleles.
- **Somatic vs germline:** germline.
- **Functional consequence:** loss of function (absent enzyme activity).

**gnomAD constraint (v2).** Observed/expected LOF = 21/56 (oe_lof 0.375; 90% CI 0.27–0.54), pLI 0.82, missense Z 4.88 — GGT1 is relatively intolerant to heterozygous LOF, yet heterozygous carriers are clinically healthy, consistent with a recessive mechanism.

**Protein and family.** GGT belongs to the **N-terminal nucleophile (Ntn) hydrolase superfamily**. It is translated as a single-chain precursor that undergoes **autocatalytic cleavage** into a large and a small subunit, forming the mature, membrane-bound heterodimeric ectoenzyme; the N-terminal **threonine of the small subunit (human hGGT1 Thr-381)** is the catalytic nucleophile. "γ-Glutamyl transpeptidases (γ-GTs) are members of N-terminal nucleophile hydrolase superfamily. They are synthetized as single-chain precursors, which are then cleaved to form mature enzymes" [PMID: 26536828](https://pubmed.ncbi.nlm.nih.gov/26536828/); "Thr-381 is locked into a single conformation as an acyl bond forms between the substrate and the enzyme" [PMID: 33187988](https://pubmed.ncbi.nlm.nih.gov/33187988/).

**Paralogs / redundancy.** The human GGT family comprises **13 homologous genes (GGT1–7 and GGTLC1–3)** on chromosomes 20 and 22: "The human GGT family comprises 13 homologous genes (e.g., GGT1-7 and GGTLC1-3) localized on chromosomes 20 and 22" [PMID: 41316810](https://pubmed.ncbi.nlm.nih.gov/41316810/) — a likely explanation for residual activity and the comparatively mild human phenotype.

**Modifier genes / epigenetics / chromosomal abnormalities.** No disease-specific modifier genes, epigenetic marks, or recurrent chromosomal abnormalities have been established for GGT deficiency. The causal lesion (structural deletion within 22q11.23) is itself a focal copy-number change but not a large cytogenetic abnormality.

**Suggested ontology terms:** HGNC:4250 (GGT1); GO:0036374 (glutathione hydrolase activity); GO:0006751 (glutathione catabolic process); CHEBI:16856 (glutathione).

---

## 5. Environmental Information

- **Environmental factors:** None established as causal or contributory to the inherited disease.
- **Lifestyle factors:** None established. Dietary cysteine/protein intake is a mechanistically plausible modifier of downstream cysteine deficiency (by analogy to cysteine supplementation rescuing mice), but this is not demonstrated in patients.
- **Infectious agents:** Not applicable — this is a Mendelian metabolic disorder with no infectious etiology or trigger.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in GGT1** (e.g., 16.9 kb homozygous deletion) → **loss of functional GGT protein** on epithelial brush-border membranes (demonstrated in humans; [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/)).
2. Absent membrane-bound GGT → **failure to hydrolyze extracellular/filtered glutathione** at the renal proximal tubule brush border and other epithelia (demonstrated; [PMID: 42531](https://pubmed.ncbi.nlm.nih.gov/42531/)).
3. Failure of GSH breakdown → **glutathione is not reclaimed and is lost in urine** → **glutathionuria + glutathionemia**, with accumulation of γ-glutamylcysteine, cysteine and cysteinylglycine in plasma (demonstrated in humans; [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/)).
4. Loss of extracellular GSH → **impaired cysteine salvage** (GGT normally liberates cysteine for de novo intracellular GSH/protein synthesis) → **intracellular cysteine deficiency** (proven in mouse; inferred in human; [PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/)).
5. **Branch A (mouse, severe):** Tissue cysteine/GSH depletion → growth failure, cataracts, lethargy, shortened lifespan; reproductive failure via suppressed IGF-1 and FSH; skeletal osteopenia/dwarfism via chondrocyte proliferation defect and osteoblast/osteoclast imbalance → **all reversible with N-acetylcysteine / OTZ** (proven in mouse; [PMID: 12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/); [PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/); [PMID: 12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/)).
6. **Branch B (human, mild):** Residual cysteine supply (likely from paralogous GGT enzymes and dietary intake) limits systemic depletion → **mild, mainly neurological/cognitive phenotype** (intellectual disability, developmental delay, behavioral problems) rather than the severe mouse syndrome (inferred; [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/); [PMID: 41316810](https://pubmed.ncbi.nlm.nih.gov/41316810/)).

```
GGT1 biallelic LOF
      │
      ▼
Absent brush-border GGT ectoenzyme (kidney proximal tubule, etc.)
      │
      ▼
Extracellular/filtered glutathione NOT hydrolyzed
      │
      ├────────────► Urinary GSH loss ─► GLUTATHIONURIA + GLUTATHIONEMIA
      │                                   (↑ γ-glutamylcysteine, cysteine, cysteinylglycine)
      ▼
Impaired cysteine salvage ─► intracellular cysteine deficiency
      │
      ├── MOUSE (severe): growth failure, cataracts, infertility (↓IGF-1/↓FSH),
      │                   osteopenia  ── reversible by NAC / OTZ
      │
      └── HUMAN (mild): neurocognitive/behavioral phenotype
                        (buffered by GGT paralogs + diet)
```

### Supporting detail by category

- **Molecular pathways / biochemistry:** The **γ-glutamyl cycle / glutathione catabolism**. GGT initiates extracellular GSH degradation, "hydrolyzing extracellular GSH and providing the cell with the recovery of cysteine, which is necessary for de novo intracellular GSH and protein biosynthesis" [PMID: 37739139](https://pubmed.ncbi.nlm.nih.gov/37739139/). KEGG: glutathione metabolism (map00480).
- **Cellular processes:** Redox homeostasis maintenance via cysteine supply; in mouse, chondrocyte proliferation and osteoblast/osteoclast balance are affected [PMID: 12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/).
- **Protein dysfunction:** Complete loss of function of the Ntn-hydrolase ectoenzyme (no functional heterodimer formed).
- **Metabolic changes:** Disrupted glutathione and sulfur-amino-acid (cysteine) metabolism; "Tissue GSH deficiency is the proximate cause of the phenotypic abnormalities associated with murine gamma-GT deficiency" [PMID: 12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/).
- **Immune involvement:** Not a feature of the inherited deficiency.
- **Tissue damage mechanisms:** Secondary to cysteine/GSH depletion (impaired antioxidant capacity) in mouse tissues.
- **Biochemical abnormality:** Enzyme deficiency — absent γ-glutamyl transpeptidase activity (<1 IU/L serum).
- **Molecular profiling:** No disease-specific transcriptomic/proteomic/metabolomic datasets exist for human patients beyond targeted metabolite measurements (elevated GSH and thiols).

**Suggested ontology terms:** GO:0006751 (glutathione catabolic process); GO:0036374 (glutathione hydrolase activity); GO:0006534 (cysteine metabolic process); GO:0006749 (glutathione metabolic process); CL:1000838 (kidney proximal convoluted tubule epithelial cell); CHEBI:16856 (glutathione); CHEBI:17561 (L-cysteine).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary site of metabolic lesion / GSH wasting:** the **kidney**, specifically the **proximal tubule brush border**. "the enzyme is primarily associated with the luminal surface of the brush border membrane of the proximal straight tubule" [PMID: 42531](https://pubmed.ncbi.nlm.nih.gov/42531/).
- **Clinically affected system (human):** **central nervous system / brain** (cognitive and behavioral phenotype).
- GGT is also expressed in other transport/secretory epithelia: "found in certain epithelial cells in anatomical sites that are involved in transport and secretory activities (e.g., renal tubule, jejunal villi, choroid plexus, ciliary body)" [PMID: 45011](https://pubmed.ncbi.nlm.nih.gov/45011/) — hence biliary tract, jejunum, choroid plexus and ciliary body are enzyme-expressing sites.
- **Body systems involved:** urinary (biochemical), nervous (clinical), and (in mouse) reproductive, skeletal, ocular.

**Tissue and cell level.** Epithelial tissue — chiefly **renal proximal tubule epithelial cells** (apical brush border). Suggested CL terms: CL:1000838 (kidney proximal convoluted tubule epithelial cell), CL:0000066 (epithelial cell).

**Subcellular level.** GGT is a **plasma-membrane ectoenzyme** anchored on the external/apical surface. Suggested GO cellular component: GO:0005886 (plasma membrane); GO:0016324 (apical plasma membrane); GO:0031526 (brush border membrane).

**Localization.** Suggested UBERON terms: UBERON:0001231 (nephron tubule) / UBERON:0004134 (proximal convoluted tubule); UBERON:0001088 (urine); UBERON:0000955 (brain). Lateralization is **bilateral/systemic** (the enzyme defect is generalized, not focal).

---

## 8. Temporal Development

- **Onset:** The biochemical defect is **congenital**; clinical (neurocognitive) features present in **infancy/childhood**. Onset pattern is **insidious/chronic** rather than acute.
- **Progression:** Appears **stable/non-progressive** based on the few reported cases; no staging system exists. Natural-history and longitudinal data are essentially absent.
- **Disease course:** **Chronic, lifelong** metabolic abnormality.
- **Remission:** No spontaneous remission of the biochemical defect; metabolic consequences are (in mouse) **treatment-reversible** with cysteine repletion.
- **Critical periods:** Not defined in humans; by analogy to mouse growth/reproductive phenotypes, childhood/developmental windows would be the plausible period for any metabolic intervention.

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** Fewer than ~8 patients have ever been reported worldwide; precise prevalence/incidence are unknown and almost certainly underestimated. "this condition has probably been underdiagnosed due the difficulty to routinely analyze glutathione in clinical samples" [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/).

**Genetic parameters.**
- **Inheritance pattern:** **Autosomal recessive**, now directly proven by segregation in a confirmed family: "genetic characterization of the patients' parents and a healthy sibling has provided direct genetic evidence regarding the autosomal recessive nature of this disease" [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/).
- **Penetrance/expressivity:** The biochemical phenotype appears fully penetrant; the neurological phenotype shows **variable expressivity** and uncertain penetrance given tiny numbers. More broadly for γ-glutamyl cycle disorders: "All disorders are very rare and inherited in an autosomal recessive manner. Most of the mutations are leaky so that many patients have residual enzyme activity" [PMID: 17397529](https://pubmed.ncbi.nlm.nih.gov/17397529/).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects:** None documented.
- **Consanguinity:** Homozygosity for a structural deletion in the index family is consistent with a role for shared ancestry/consanguinity, as is typical of rare AR disease, though not explicitly characterized.
- **Carrier frequency:** Unknown; cannot be reliably estimated from gnomAD for a disease defined largely by structural variants.

**Population demographics.** No ethnic predilection established (reported cases include European and Japanese patients [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/)). No defined geographic clustering, sex ratio, or age distribution given the few cases.

---

## 10. Diagnostics

**Diagnostic approach.** Diagnosis rests on the **biochemical demonstration of glutathionuria + glutathionemia together with very low/absent serum and tissue GGT activity (<1 IU/L)**, confirmed by **GGT1 sequencing** [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/); [PMID: 6118466](https://pubmed.ncbi.nlm.nih.gov/6118466/).

**Clinical/laboratory tests.**
- Quantitative **urine and plasma glutathione** (markedly elevated), plus γ-glutamylcysteine, cysteine, cysteinylglycine. "Glutathionaemia and glutathionuria were evident in both brothers. The analyses of sulphydryl compounds in the plasma ... and urine indicated high concentrations of glutathione, gamma-glutamylcysteine, cysteine and cysteinylglycine" [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/).
- **Serum GGT enzyme activity** (very low/undetectable). LOINC: serum GGT activity (e.g., LOINC 2324-2).
- **Diagnostic pitfall:** on routine amino-acid chromatography, thiol compounds produce "a large peak in the citrulline position," which can mislead — "Urine amino acid analysis on an automatic analyser showed a slightly increased excretion of cystine and a large peak in the citrulline position due, at least in part, to thio-compounds" [PMID: 15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/).

**Genetic testing.** **GGT1 sequencing** is confirmatory. Because the index lesion was a **16.9 kb structural deletion**, **WGS or CNV/deletion-duplication analysis** may be required — standard whole-exome sequencing can miss such events [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/). Single-gene testing or a metabolic gene panel including GGT1 is appropriate; chromosomal microarray may detect larger deletions.

**Omics-based diagnostics.** Targeted **metabolomics** (thiol/glutathione quantification by HPLC/LC-MS) is effectively the functional diagnostic test; no transcriptomic/proteomic diagnostic is established.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria exist. Differential diagnosis includes other γ-glutamyl cycle / glutathione-metabolism disorders (e.g., glutathione synthetase deficiency / 5-oxoprolinuria, γ-glutamylcysteine synthetase deficiency) — distinguished by their specific metabolite patterns and enzyme assays [PMID: 17397529](https://pubmed.ncbi.nlm.nih.gov/17397529/). The citrulline-position peak also raises a spurious concern for a urea-cycle abnormality that must be excluded.

**Screening.** Not included in standard newborn screening because glutathione is not measured in routine metabolic panels [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/). Cascade/carrier testing is feasible once a family's GGT1 variant is known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No evidence of reduced survival in reported human patients; the biochemical abnormality appears compatible with normal life span. (Mouse knockouts, by contrast, have shortened life spans.)
- **Morbidity/function:** Driven by the neurocognitive phenotype — intellectual disability and behavioral difficulties account for functional impact. No validated QoL data.
- **Disease course/complications:** Chronic and apparently non-progressive; no characteristic organ-failure complications documented in humans.
- **Recovery potential:** The genetic/biochemical defect is permanent. Downstream metabolic consequences are, in principle, modifiable (mouse data), but human cognitive outcomes are not known to be reversible.
- **Prognostic factors/biomarkers:** None validated. Degree of intellectual disability is the main determinant of outcome in reported cases; true genotype–phenotype correlations cannot be drawn from <8 patients.

---

## 12. Treatment

**There is no approved disease-specific pharmacotherapy; human management is supportive.** No targeted, gene, cell, RNA, immunologic or surgical therapy exists.

**Rational (mechanism-based, mouse-validated) strategy — cysteine repletion.** In Ggt-deficient mice, supplying an alternative cysteine source corrects the downstream phenotype:
- **N-acetylcysteine (NAC)** restores gonad size, hormone levels and fertility, and ameliorates skeletal abnormalities: "N-acetylcysteine treatment of GGT-/- mice ameliorates their skeletal abnormalities by normalizing chondrocytes proliferation and osteoblastic function" [PMID: 12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/); reproductive rescue [PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/). Suggested NCIT: Acetylcysteine (NCIT:C28159).
- **L-2-oxothiazolidine-4-carboxylate (OTZ / procysteine)**, a cysteine prodrug, partially restores liver GSH and improves growth/behavior in mice [PMID: 12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/).

These approaches are **not formally trialed in human patients** — they represent a biologically rational but unproven therapeutic avenue for humans.

**Supportive/rehabilitative care.** Developmental, educational and behavioral support for intellectual disability and behavioral problems, as for other causes of neurodevelopmental impairment.

**Pharmacogenomics / personalized medicine:** Not applicable beyond genotype-confirmed diagnosis guiding counseling.

---

## 13. Prevention

- **Primary prevention:** Not possible for a Mendelian disorder; relies on **genetic counseling** and reproductive options for at-risk couples.
- **Secondary prevention / early detection:** Not currently part of newborn screening (glutathione is not routinely measured) [PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/). Targeted glutathione measurement should be considered in unexplained intellectual disability with abnormal amino-acid chromatography (the citrulline-position pitfall).
- **Tertiary prevention:** Mechanistically, cysteine repletion (NAC/OTZ) could in theory prevent downstream metabolic complications, extrapolating from mouse data; unproven in humans.
- **Genetic screening/counseling:** Once a family's GGT1 variant(s) are known, **carrier testing, cascade screening, prenatal and preimplantation genetic testing** are feasible. **Genetic counseling** (25% recurrence risk per pregnancy for carrier couples) is the mainstay of prevention.
- **Immunization / public-health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Best-characterized outside humans in the **house mouse (Mus musculus; NCBI Taxon 10090)**.
- **Orthologous gene:** mouse **Ggt1 (NCBI Gene 14598; MGI)**.
- **Natural disease:** No well-documented naturally occurring GGT1-deficiency disease in companion animals or wildlife is recorded in the knowledge base; the mouse disease is experimentally induced (ENU mutagenesis or targeted knockout), not naturally arising.
- **Comparative biology:** The mouse recapitulates the **core metabolic lesion** (glutathionuria, glutathionemia, reduced liver GSH) well, but is **far more severe** than human disease — a key cross-species difference likely reflecting human GGT paralog redundancy (13 family genes; [PMID: 41316810](https://pubmed.ncbi.nlm.nih.gov/41316810/)) and species differences in GSH handling.
- **Evolutionary conservation:** The Ntn-hydrolase GGT mechanism is deeply conserved from bacteria to mammals [PMID: 26536828](https://pubmed.ncbi.nlm.nih.gov/26536828/).
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Principal models — mouse.** Two mouse models are the main disease models:
1. **ENU-induced GGTenu1 mutant**, discovered via aminoaciduria screening: "A mouse mutant with glutathionuria was discovered by screening for amino acidurias in the progeny of ethylnitrosourea-mutagenized mice" [PMID: 9139708](https://pubmed.ncbi.nlm.nih.gov/9139708/).
2. **Targeted Ggt1 knockout** (Lieberman lab) [PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/); [PMID: 12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/).

**Model characteristics / phenotype recapitulation.** Both reproduce the **biochemistry faithfully**: autosomal-recessive glutathionuria/glutathionemia, reduced liver GSH. Additional (more severe than human) features: **growth failure, cataracts, coat-color defects, lethargy, infertility, osteopenia/dwarfism, and shortened life span** [PMID: 9139708](https://pubmed.ncbi.nlm.nih.gov/9139708/); [PMID: 12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/). Reproductive failure is attributed to intracellular cysteine deficiency: mice are "growth retarded as a result of cysteine deficiency secondary to excessive glutathione excretion in urine" [PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/).

**Model limitations.** The mouse is **more severe** than human disease and does not model the predominantly mild neurocognitive human phenotype — a discrepancy attributed to paralog redundancy and species GSH-handling differences.

**Applications.** The models established the **proximate mechanism** (tissue GSH/cysteine deficiency) and **therapeutic reversibility** (NAC/OTZ), underpinning the rational treatment hypothesis for humans.

**Resources:** MGI (mouse Ggt1, Gene 14598). No established zebrafish/Drosophila/C. elegans/organoid disease models are recorded for this condition in the knowledge base.

---

## Mechanistic Model / Interpretation

The disease is best understood as a **failure of the salvage arm of the glutathione (γ-glutamyl) cycle**. Glutathione synthesized intracellularly (predominantly in liver) is exported to plasma and filtered at the glomerulus; the renal proximal-tubule brush-border GGT normally hydrolyzes this extracellular GSH, releasing amino acids (notably **cysteine**) for reuptake and reuse. When GGT1 is lost, this salvage step fails: glutathione cannot be reclaimed and spills into urine (**glutathionuria**) while accumulating in plasma (**glutathionemia**), and the cell is deprived of recovered cysteine.

Whether that cysteine deprivation becomes clinically significant depends on **how much redundant/alternative cysteine supply remains**. In mice — with the sharpest metabolic dependence and (apparently) less effective buffering — systemic cysteine/GSH depletion produces a severe, multisystem, life-shortening phenotype that is **fully bypassable** by feeding cysteine (NAC) or a cysteine prodrug (OTZ). In humans, the presence of **13 GGT-family paralogs** plus dietary cysteine appears to buffer systemic cysteine supply, so the phenotype is limited to a **mild, chiefly neurocognitive** presentation. This two-branch model (identical upstream lesion; divergent downstream severity set by cysteine-supply redundancy) reconciles the dramatic human biochemistry with the surprisingly benign human clinical course, and it directly motivates **cysteine-repletion therapy** as the rational — though still unproven in humans — intervention.

| Feature | Human disease | Mouse model |
|---|---|---|
| Glutathionuria / glutathionemia | Yes (marked) | Yes (marked) |
| Serum GGT activity | Absent/very low | Absent/very low |
| Growth failure | Not prominent | Severe |
| Cataracts / infertility / osteopenia | Not reported | Present |
| Neurocognitive phenotype | Prominent (mild-moderate ID, behavior) | Not the focus |
| Life span | Apparently normal | Shortened |
| Rescue by NAC / OTZ | Untested | Demonstrated |

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/) | *GGT deficiency from large homozygous GGT1 deletion* | **Molecular proof of causal gene & AR inheritance**; rarity/underdiagnosis; mild human phenotype |
| [15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/) | *Two Japanese brothers with hereditary GGT deficiency* | Biochemical signature; diagnostic pitfall (citrulline peak); Marfanoid habitus |
| [6118466](https://pubmed.ncbi.nlm.nih.gov/6118466/) | *Glutathionuria: GGT deficiency* | Human CNS/behavioral phenotype; normal amino-acid transport |
| [238530](https://pubmed.ncbi.nlm.nih.gov/238530/) | *Glutathionuria: inborn error from tissue GGT deficiency* | Early definition; tissue enzyme deficiency |
| [42531](https://pubmed.ncbi.nlm.nih.gov/42531/) | *Rat renal GGT characterization* | Localizes GGT to proximal-tubule brush border; GSH reclamation; normal amino-acid reabsorption |
| [45011](https://pubmed.ncbi.nlm.nih.gov/45011/) | *New aspects of glutathione metabolism/translocation* | Epithelial anatomical distribution of GGT |
| [34150](https://pubmed.ncbi.nlm.nih.gov/34150/) | *Translocation of GSH to GGT; glutathionuria after inhibition* | Mechanism: GSH translocation; inhibition phenocopies disease |
| [2873573](https://pubmed.ncbi.nlm.nih.gov/2873573/) | *Induction of glutathionuria by γ-glutamyl amino acids* | Pharmacologic phenocopy; substrate competition |
| [9139708](https://pubmed.ncbi.nlm.nih.gov/9139708/) | *Mice with genetic GGT deficiency* | ENU GGTenu1 model origin & phenotype |
| [11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/) | *Reproductive defects in GGT-deficient mice* | Cysteine-deficiency mechanism; NAC rescue of fertility |
| [12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/) | *OTZ supplementation in murine GGT deficiency* | Tissue GSH deficiency as proximate cause; OTZ rescue |
| [12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/) | *Reversible skeletal abnormalities in GGT-deficient mice* | Bone phenotype; NAC reversibility |
| [26536828](https://pubmed.ncbi.nlm.nih.gov/26536828/) | *Maturation mechanism of γ-GTs* | Ntn-hydrolase family; autocatalytic maturation |
| [33187988](https://pubmed.ncbi.nlm.nih.gov/33187988/) | *Crystal structures of human GGT1* | Catalytic Thr-381 mechanism |
| [37739139](https://pubmed.ncbi.nlm.nih.gov/37739139/) | *Targeting GGT (review)* | Physiologic role: cysteine recovery, redox homeostasis |
| [41316810](https://pubmed.ncbi.nlm.nih.gov/41316810/) | *GGT molecular family* | 13-gene paralog family (redundancy rationale) |
| [17397529](https://pubmed.ncbi.nlm.nih.gov/17397529/) | *Inborn errors of glutathione metabolism* | AR inheritance; leaky mutations/variable expressivity |

**Consistency.** The findings are internally consistent: physiologic localization studies (brush border; [PMID: 42531](https://pubmed.ncbi.nlm.nih.gov/42531/)) explain the urinary-loss phenotype; pharmacologic inhibition experiments ([PMID: 34150](https://pubmed.ncbi.nlm.nih.gov/34150/); [PMID: 2873573](https://pubmed.ncbi.nlm.nih.gov/2873573/)) phenocopy the inherited defect; mouse genetics ([PMID: 11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/); [PMID: 12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/); [PMID: 12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/)) establish causality and reversibility; and human genetics ([PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/)) confirm the gene and inheritance. The main **tension** in the evidence base is the **severity mismatch** between mouse and human, addressed by the paralog-redundancy hypothesis.

---

## Limitations and Knowledge Gaps

1. **Tiny human sample (<8 patients):** prevalence, penetrance, expressivity, sex ratio, and genotype–phenotype correlations cannot be reliably estimated.
2. **Mechanism in humans is inferred:** cysteine depletion as the proximate cause and NAC/OTZ reversibility are proven only in mice; never formally demonstrated or trialed in human patients.
3. **No validated biomarkers of prognosis** and **no natural-history studies**.
4. **Causal spectrum incomplete:** only a structural deletion is molecularly proven; the full allelic spectrum (point mutations) and carrier frequency remain undefined; structural variants may be missed by standard exome sequencing.
5. **Species discrepancy unresolved at the molecular level:** the paralog-redundancy explanation is plausible but not directly tested.
6. **No disease-specific therapy** is approved or trialed in humans.
7. **Under-ascertainment:** glutathione is not in standard screens, so the true disease burden is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **International case finding / registry:** Prospectively measure urine and plasma glutathione in unexplained intellectual disability with the "citrulline-position" chromatographic peak; aggregate cases to estimate prevalence and phenotype spectrum.
2. **Define the GGT1 allelic spectrum:** Apply WGS/CNV-aware pipelines (not exome alone) in suspected cases to catalog point and structural variants; estimate carrier frequency from large population datasets with structural-variant calling.
3. **Test the cysteine-depletion mechanism in humans:** Measure intracellular/erythrocyte cysteine and GSH in confirmed patients; correlate with clinical severity.
4. **Pilot cysteine-repletion therapy:** Given mouse reversibility and NAC's established safety, consider an n-of-1 or small compassionate-use trial of NAC/OTZ with biochemical (plasma/urine GSH, cysteine) and developmental endpoints.
5. **Interrogate paralog redundancy:** Quantify residual GGT activity from paralogs (GGT5, etc.) in patient tissues/iPSC-derived cells; model double-paralog loss to test the severity-buffering hypothesis.
6. **Improve the human-relevant model:** Engineer humanized or paralog-sensitized mouse/organoid models that reproduce the mild human neurocognitive phenotype for mechanism and therapy testing.
7. **Ontology/knowledge-base annotation:** Finalize mappings (MONDO:0009285; GGT1/HGNC:4250; HP:0001249, HP:0001263, HP:0000708; GO:0006751/GO:0036374; UBERON proximal tubule; CHEBI:16856 glutathione; NCIT:C28159 acetylcysteine) for the disease entry.

---

*Evidence source legend:* Human clinical = case reports/series ([PMID: 29483667](https://pubmed.ncbi.nlm.nih.gov/29483667/), [15702405](https://pubmed.ncbi.nlm.nih.gov/15702405/), [6118466](https://pubmed.ncbi.nlm.nih.gov/6118466/), [238530](https://pubmed.ncbi.nlm.nih.gov/238530/)); Model organism = mouse ([PMID: 9139708](https://pubmed.ncbi.nlm.nih.gov/9139708/), [11089562](https://pubmed.ncbi.nlm.nih.gov/11089562/), [12757858](https://pubmed.ncbi.nlm.nih.gov/12757858/), [12810527](https://pubmed.ncbi.nlm.nih.gov/12810527/)); In vitro/structural ([PMID: 33187988](https://pubmed.ncbi.nlm.nih.gov/33187988/), [26536828](https://pubmed.ncbi.nlm.nih.gov/26536828/)); Reviews ([PMID: 37739139](https://pubmed.ncbi.nlm.nih.gov/37739139/), [17397529](https://pubmed.ncbi.nlm.nih.gov/17397529/), [41316810](https://pubmed.ncbi.nlm.nih.gov/41316810/)).


## Artifacts

- [OpenScientist final report](Gamma-glutamyl_Transpeptidase_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Gamma-glutamyl_Transpeptidase_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:26536828` (7 mentions) - The maturation mechanism of γ-glutamyl transpeptidases: Insights from the crystal structure of a precursor mimic of the enzyme from Bacillus licheniformis and from site-directed mutagenesis studies.
  - shared terms: enzyme, genetic

Weighed against this report's own most characteristic terms: `human`, `disease`, `cysteine`, `glutathione`, `phenotype`, `ggt`, `mouse`, `deficiency`, `ggt1`, `gsh`, `glutathionuria`, `biochemical`, `patient`, `metabolic`, `enzyme`, `gene`, `genetic`, `otz`, `activity`, `clinical`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009285` (3 mentions) - the report calls it "MONDO"; MONDO calls it **gamma-glutamyl transpeptidase deficiency**
- `HP:0001249` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Intellectual disability**
- `HP:0001263` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006534` (obsolete cysteine metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000708` (2 mentions) - the report calls it "Behavioral"; HP calls it **Atypical behavior**, and lists "Behavioral changes" among its other names
- `HP:0000707` (1 mention) - the report calls it "abnormality of nervous system"; HP calls it **Abnormality of the nervous system**
- `GO:0036374` (3 mentions) - the report calls it "glutathione hydrolase activity"; GO calls it **glutathione gamma-glutamate hydrolase**, and lists "glutathione hydrolase activity" among its other names
- `GO:0006534` (1 mention) - the report calls it "cysteine metabolic process"; GO calls it **obsolete cysteine metabolic process**
- `UBERON:0004134` (1 mention) - the report calls it "proximal convoluted tubule"; UBERON calls it **proximal tubule**, and lists "proximal kidney tubule" among its other names