---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T17:02:12.593160'
end_time: '2026-10-15T17:47:03.397804'
duration_seconds: 2690.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CLPB Deficiency 3-Methylglutaconic Aciduria Type VIIB
  mondo_id: MONDO:0014561
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
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 27
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.036
  labels_checked: 25
  labels_matching: 16
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014561
    reported_labels:
    - MONDO
    ontology_label: 3-methylglutaconic aciduria, type VIIB
  - term_id: HP:0001332
    reported_labels:
    - Movement disorder / dystonia
    ontology_label: Dystonia
  - term_id: NCIT:C1512
    reported_labels:
    - G-CSF / filgrastim
    ontology_label: Immunoconjugate
  labels_variant: 6
  unresolved_terms:
  - HP:0000844
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: 3-methylglutaconic_Aciduria_Type_VIIB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 3-methylglutaconic_Aciduria_Type_VIIB-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CLPB Deficiency 3-Methylglutaconic Aciduria Type VIIB
- **MONDO ID:** MONDO:0014561 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CLPB Deficiency 3-Methylglutaconic Aciduria Type VIIB** covering all of the
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

# CLPB Deficiency — 3-Methylglutaconic Aciduria Type VIIB (MEGCANN)

**Disease:** CLPB Deficiency 3-Methylglutaconic Aciduria Type VIIB
**MONDO ID:** MONDO:0014561 · **OMIM:** #616271 · **Orphanet:** ORPHA:445038 / ORPHA:324631
**Category:** Mendelian (inborn error of mitochondrial protein quality control)

---

## Summary

**CLPB deficiency (3-methylglutaconic aciduria type VIIB; MEGCANN) is an ultra-rare, autosomal-recessive inborn error of mitochondrial protein quality control caused by variants in the *CLPB* gene (11q13.4), which encodes a HAX1-activated AAA+ disaggregase/refoldase resident in the mitochondrial intermembrane space (IMS).** The protein's normal job is to disaggregate and refold stress-damaged proteins in the IMS; when its activity is lost, IMS client proteins (including HAX1 and HTRA2) aggregate and the SPY proteolytic quality-control complex (STOML2–PARL–YME1L1) is crippled. The clinical consequence is a severe multisystem syndrome combining **congenital neutropenia** (which can transform to MDS/leukemia), **intellectual disability**, **progressive brain atrophy**, **epilepsy**, **movement disorder (including dystonia)**, **cataracts**, and the biochemical hallmark **3-methylglutaconic aciduria (3-MGA)**.

The disease illustrates a striking genotype–phenotype architecture. **Biallelic loss-of-function** produces the full, often lethal, multisystem MEGCANN syndrome, whereas **monoallelic dominant-negative missense variants** — clustered near the ATP-binding pocket — cause a milder, neutropenia-predominant phenotype (frequently isolated severe congenital neutropenia, often without 3-MGA). This dual inheritance mechanism is explained structurally: the human CLPB ortholog Skd3 forms spiral hexamers that engage substrate via pore loops and stack head-to-head into dodecamers through adaptable ankyrin-repeat (ANK) interactions. SCN-linked subunits poison the hexamer (dominant-negative), while MGCA7-linked subunits do not. Consistent with this, gnomAD shows *CLPB* is **not haploinsufficient** (pLI ≈ 0), so monoallelic disease arises from protein poisoning rather than dosage loss.

**Prognosis is poor for the severe biallelic form** (~66% mortality; 50% four-year survival), with structural-impact predictions (nonsense-mediated decay, ankyrin-domain disruption) being stronger survival predictors than zygosity or age of onset. **No disease-specific or curative therapy exists.** Management is entirely supportive: G-CSF (filgrastim) for neutropenia with HSCT reserved for leukemic transformation, antiepileptics and rehabilitation for neurologic features, and cataract surgery. The 3-MGA biomarker itself is not treatable and is a fluctuant, sometimes-undetectable secondary metabolite rather than a disease driver.

---

## 1. Disease Information & Key Identifiers

| Resource | Identifier |
|---|---|
| Gene symbol | **CLPB** ("ClpB family mitochondrial disaggregase") |
| NCBI Gene | 81570 |
| HGNC | HGNC:30664 |
| Gene OMIM | 616254 |
| Ensembl | ENSG00000162129 |
| UniProt | Q9H078 |
| Cytogenetic locus | 11q13.4 (GRCh38 chr11:72,285,495–72,434,680, minus strand) |
| Disease OMIM | **#616271** (MEGCANN / MGCA7B) |
| MONDO | **MONDO:0014561** |
| Orphanet | ORPHA:445038 (and ORPHA:324631, "3-methylglutaconic aciduria type 7") |
| DOID | DOID:0081134, DOID:0110003 |
| GARD | 0017767 |
| MedGen / UMLS | C5676893 |
| SNOMED CT | 764860006 |

**Synonyms:** 3-methylglutaconic aciduria with cataracts, neurologic involvement, and neutropenia (MEGCANN); 3-methylglutaconic aciduria-cataract-neurologic involvement-neutropenia syndrome; MGA7; MGCA7; MGCA7B; "CLPB 3-methylglutaconic aciduria." Information in this report is derived from aggregated disease-level resources (OMIM, Orphanet, MONDO, gnomAD, ClinVar) and published patient cohorts, not from EHR/individual-patient data.

---

## 2. Etiology

- **Primary cause:** monogenic (Mendelian). Biallelic pathogenic variants in *CLPB* cause the full MEGCANN syndrome; monoallelic dominant-negative missense variants cause a neutropenia-predominant presentation. There is no environmental, infectious, or multifactorial etiology.
- **Genetic risk factors:** the causal variants themselves (see Section 4); consanguinity increases the chance of biallelic genotypes in affected families.
- **Environmental risk/protective factors:** none established — the disease is genetically determined.
- **Gene–environment interactions:** not applicable; no documented modifier exposures.

---

## 3. Phenotypes

Across cohorts, biallelic CLPB deficiency presents with a consistent constellation. Wortmann et al. (2021) summarized it: *"biallelic CLPB variants underlie a neurological phenotype ranging from nonprogressive intellectual disability to prenatal encephalopathy with progressive brain atrophy, movement disorder, cataracts, 3-methylglutaconic aciduria, and neutropenia."* The founding paper emphasized the severity range and malignancy risk: *"neutropenia that can develop into leukemia, a neurological phenotype ranging from nonprogressive intellectual disability to a prenatal encephalopathy with progressive brain atrophy, movement disorder, cataracts, and early death."* Neutropenia and intellectual disability are the hallmarks. [PMID: 34140661; PMID: 25597510]

| Phenotype | HPO term | Type | Onset / severity / frequency |
|---|---|---|---|
| Congenital neutropenia (→ leukemia/MDS) | HP:0000844 | Laboratory/hematologic | Congenital; hallmark; can transform to malignancy |
| Intellectual disability | HP:0001249 | Clinical sign | Hallmark; nonprogressive → severe |
| Developmental delay | HP:0001263 | Clinical sign | Early childhood; common |
| Progressive brain atrophy | HP:0012444 | Imaging/structural | Progressive in severe forms |
| Seizures / epilepsy | HP:0001250 | Clinical sign | Frequent in severe forms |
| Movement disorder / dystonia | HP:0001332 | Clinical sign | Common |
| Cataracts | HP:0000518 | Physical manifestation | Characteristic; surgically treatable |
| 3-methylglutaconic aciduria | HP:0003535 | Laboratory abnormality | Biochemical hallmark; fluctuant |

**Quality-of-life impact:** severe in the biallelic form — early mortality, profound neurodisability, recurrent infections, visual impairment, and lifelong dependency. The monoallelic neutropenia-predominant form has a comparatively better functional trajectory. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data are published for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene:** *CLPB* (NCBI Gene 81570; HGNC:30664; gene OMIM 616254), 11q13.4.

**Variant spectrum (ClinVar, queried Oct 2025):** ~954 *CLPB* records — ~157 pathogenic, ~38 likely pathogenic, ~692 of uncertain significance. Disease-causing classes:
- **Missense:** biallelic p.Arg408Gly abolishing ATPase (PMID 25597510); SCN-associated heterozygous missense clustering near the ATP-binding pocket (PMID 34115842).
- **Nonsense/frameshift:** stop/stop genotypes carry the highest disease burden (PMID 41719910).
- **Splice variants.**

All reported variants are **germline**; no somatic/cancer-driver role is established. **Functional consequence:** biallelic = loss of function (recessive); specific monoallelic missense = **dominant-negative**. In-silico structural impact (NMD, ankyrin-domain disruption) predicts survival (PMID 41719910).

**Population constraint (gnomAD, Oct 2025):** pLI ≈ 2.4×10⁻⁵ (not haploinsufficient); observed/expected LoF = 0.51 (40 observed vs 78.4 expected); LOEUF = 0.66; LoF Z = 3.68; missense Z = 1.53. Heterozygous LoF alleles occur in and are tolerated by the general population — explaining why a single null allele does **not** cause disease, whereas a single *poisoning* (dominant-negative) missense protein does. [PMID: 34115842]

**Modifier genes / epigenetics / chromosomal abnormalities:** no established modifier genes, epigenetic mechanisms, or large-scale chromosomal rearrangements for this disease; it is a single-gene disorder.

---

## 5. Environmental Information

Not applicable. CLPB deficiency is a purely genetic disorder with no documented environmental, lifestyle, or infectious contributors.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic (or dominant-negative monoallelic) pathogenic variant in *CLPB* (11q13.4)** → reduces or abolishes functional CLPB AAA+ disaggregase/refoldase protein in the mitochondrial intermembrane space. *(demonstrated — PMID 25597510, 34115842)*
2. **Loss of CLPB ATPase/refoldase activity** → CLPB can no longer disaggregate and refold stress-damaged IMS client proteins. Normal activation requires HAX1 binding the ankyrin domain to drive the active hexamer; this step fails. *(demonstrated — PMID 42244541, 36170828)*
3. **Loss of disaggregase activity → aggregation of IMS proteins** (CLPB, HAX1, HTRA2) under stress. *(demonstrated — PMID 38270563)*
4. **IMS protein aggregation → impaired SPY complex (STOML2–PARL–YME1L1) function** → degraded mitochondrial protein quality control. *(demonstrated — PMID 38270563)*
5. **Branch A (hematologic):** impaired IMS proteostasis + loss of the CLPB/HAX1 axis → impaired granulocytic differentiation and increased apoptosis of hematopoietic progenitors → congenital neutropenia → (with clonal pressure) risk of MDS/leukemia. *(demonstrated in cells — PMID 34115842)*
6. **Branch B (neurologic):** mitochondrial dysfunction in CNS → progressive neuronal loss → cerebral/cerebellar atrophy, intellectual disability, epilepsy, movement disorder. *(model-supported — PMID 25597510; inferred for human CNS)*
7. **Branch C (ophthalmologic):** mitochondrial/proteostatic stress in the lens → cataracts. *(observed clinically; mechanism inferred)*
8. **Branch D (biochemical):** impaired mitochondrial energy metabolism → acetyl-CoA buildup → trans-3-methylglutaconyl-CoA → 3-methylglutaconic acid excretion (secondary, fluctuant biomarker). *(mechanism inferred — PMID 39787888)*

```
   CLPB variant (11q13.4)
          |
   loss of CLPB disaggregase/refoldase  <-- (needs HAX1 cofactor; fails)
          |
   aggregation of IMS proteins (CLPB, HAX1, HTRA2)
          |
   SPY complex (STOML2-PARL-YME1L1) dysfunction
          |
   ------------------------------------------------
   |            |             |             |
 Hematologic  Neurologic    Ophthalmic    Metabolic
 neutropenia  brain atrophy  cataracts    acetyl-CoA buildup
 (-> leukemia) ID/epilepsy/             -> 3-MGA aciduria
               movement disorder          (fluctuant biomarker)
```

**Upstream vs downstream:** the mutation and loss of disaggregase activity are the upstream lesions; IMS aggregation and SPY dysfunction are the proximate molecular consequences; neutropenia, brain atrophy, cataracts, and 3-MGA are downstream, tissue-level manifestations. 3-MGA is the most downstream and least specific — a secondary readout of mitochondrial energy failure rather than a driver.

### Supporting detail

CLPB is *"a mitochondrial intermembrane space AAA+ domain-containing disaggregase"* (Baker et al., 2024). In CLPB-null cells, stress triggers aggregation specifically in the IMS and *"CLPB deficiency impeding SPY complex function by virtue of protein aggregation in the intermembrane space."* [PMID: 38270563] HAX1 is the direct activating cofactor: *"HAX1 is a direct stimulatory cofactor of CLPB. HAX1 promotes oligomerization of CLPB into an active disaggregase and stimulates the ATPase and refoldase activities of the oligomeric complex."* [PMID: 42244541] On the hematologic branch, *"Both genetic loss of CLPB and expression of CLPB variants result in impaired granulocytic differentiation of human hematopoietic progenitor cells and increased apoptosis."* [PMID: 34115842]

**3-MGA biochemistry:** CLPB deficiency is a **secondary** 3-MGA syndrome (impaired mitochondrial energy metabolism/membrane integrity), unlike primary MGCA1 (*AUH*, leucine catabolism). *"this accumulation is due to an underlying buildup of acetyl-CoA in the mitochondria from impaired function of the TCA cycle with ensuing formation of trans-3-methylglutaconyl CoA and its subsequent byproducts, including 3-MGA."* [PMID: 39787888]

**Ontology anchors:**
- GO biological process: GO:0042026 (protein refolding), GO:0051131 (chaperone-mediated protein complex assembly), GO:0006457 (protein folding).
- GO cellular component: **GO:0005758 (mitochondrial intermembrane space)**, GO:0005739 (mitochondrion).
- CL cell types: CL:0000775 (neutrophil), CL:0000037 (hematopoietic stem cell), CL:0000540 (neuron), CL:0000121 (Purkinje/cerebellar neuron).
- UBERON: UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0000965 (lens), UBERON:0002371 (bone marrow).
- CHEBI: 3-methylglutaconic acid; CHEBI:15351 (acetyl-CoA).

---

## 7. Anatomical Structures Affected

- **Primary organs / systems:** central nervous system (cerebrum and cerebellum; UBERON:0000955, UBERON:0002037), hematopoietic/immune system (bone marrow, neutrophil lineage; UBERON:0002371), eye/lens (UBERON:0000965).
- **Secondary involvement:** systemic consequences of neutropenia (recurrent infections).
- **Subcellular compartment:** **mitochondrial intermembrane space** (GO:0005758) is the defining site of molecular pathology.
- **Lateralization:** brain atrophy typically bilateral/symmetric; cataracts bilateral.

---

## 8. Temporal Development

- **Onset:** congenital/neonatal for the severe biallelic form (can be prenatal encephalopathy); neutropenia is congenital. Milder forms present in childhood.
- **Course:** progressive brain atrophy and neurodisability in severe forms; neutropenia is chronic with risk of leukemic transformation.
- **Critical window:** onset before 12 months of age predicts more severe disease (PMID 41719910).
- **3-MGA timing:** fluctuant and may appear only with delay in neonates — a diagnostic pitfall (PMID 31729175).

---

## 9. Inheritance & Population

- **Inheritance:** autosomal recessive (biallelic) for the full MEGCANN syndrome; **monoallelic de novo / dominant-negative** missense variants cause a neutropenia-predominant presentation.
- **Penetrance/expressivity:** highly variable expressivity (nonprogressive ID → lethal neonatal encephalopathy); severity tracks with variant class (NMD/ankyrin-disruption worst).
- **Constraint:** *CLPB* is LoF-tolerant in heterozygotes (pLI ≈ 0), confirming recessive biology plus a separate dominant-negative route.
- **Prevalence:** ultra-rare; Orphanet lists prevalence as unknown/<1:1,000,000; ~60–100 individuals reported worldwide (largest cohort = 63 patients, PMID 41719910).
- **Demographics:** pan-ethnic; consanguinity reported in some families; no established founder population; both sexes affected without strong sex bias.

---

## 10. Diagnostics

- **Biochemical:** urine organic acids showing elevated 3-MGA (fluctuant, may be absent/delayed — repeat testing advised); CBC showing neutropenia. Untargeted plasma metabolomics is an emerging, more sensitive screen (PMID 39787888).
- **Hematologic:** absolute neutrophil count; bone marrow examination (maturation-arrest pattern typical of SCN); surveillance for MDS/leukemia.
- **Imaging:** brain MRI showing cerebral/cerebellar atrophy (progressive).
- **Genetic testing (confirmatory, gold standard):** WES/WGS or targeted panels (mitochondrial/3-MGA/SCN panels including *CLPB*); single-gene *CLPB* sequencing when the phenotype is recognized. ClinVar/ACMG classification; structural-impact prediction (NMD, ankyrin-domain disruption) adds prognostic value (PMID 41719910).
- **Differential diagnosis:** other 3-MGA syndromes — Barth (*TAZ*, MGCA2), *OPA3* (MGCA3/Costeff), *DNAJC19* (MGCA5/DCMA), *HTRA2* (MGCA8), *YME1L1*, primary MGCA1 (*AUH*); other causes of severe congenital neutropenia (*ELANE*, *HAX1*, *G6PC3*).
- **Screening:** carrier/cascade testing in affected families; no population newborn screening exists for this disorder specifically.

---

## 11. Outcome / Prognosis

| Measure | Biallelic | Monoallelic |
|---|---|---|
| Mortality | 66% | 23% |
| 4-year survival | 50% | 82% |
| Burden by genotype | Stop/stop > missense combinations | Dominant-negative missense, milder |
| Strongest survival predictor | Structural impact (NMD, ANK disruption) > zygosity or onset age | — |

Onset before 12 months predicts more severe disease. Complications: life-threatening infection (from neutropenia), leukemic/MDS transformation, intractable epilepsy, progressive neurodisability, visual impairment from cataracts. [PMID: 41719910]

---

## 12. Treatment (NCIT anchors)

No disease-specific or curative therapy exists; care is multidisciplinary and symptom-directed. The neutropenia follows the SCN paradigm: *"Granulocyte colony-stimulating factor and hematopoietic stem cell transplantation are now the bedrock of standard care."* [PMID: 36485107] In mechanistically related HAX1-CN, *"All patients were initially treated with G-CSF with a sufficient increase in absolute neutrophil counts."* [PMID: 37193639]

- **G-CSF / filgrastim** (NCIT:C1512) — first-line for neutropenia.
- **Hematopoietic stem cell transplantation** (NCIT:C15431) — for leukemic transformation/refractory neutropenia.
- **Antiepileptic drugs** (NCIT:C264) — seizure control.
- **Cataract surgery** — lens opacity.
- **Rehabilitation** — PT/OT/speech therapy for neurodevelopmental support.

No gene therapy, RNA-based therapy, targeted small molecule, or pharmacogenomic guidance exists for this disease. 3-MGA itself is not specifically treatable. [PMID: 31030818]

---

## 13. Prevention

Primary prevention is limited to genetic counseling and reproductive options (carrier testing in at-risk families, prenatal/preimplantation genetic testing) given the Mendelian basis. Secondary prevention centers on early neutrophil monitoring and infection prophylaxis once diagnosed; tertiary prevention is leukemia surveillance and supportive multidisciplinary care. No vaccine or environmental intervention is applicable.

---

## 14. Other Species / Natural Disease

- **Evolutionary conservation:** CLPB orthologs exist across metazoa — *"The multicellular metazoan lineage acquired a novel chaperone in the mitochondrial intermembrane space."* [PMID: 42244541]
- **Natural veterinary disease:** none documented; relevance is as a research model, not a companion-animal disease.
- **Zoonotic potential:** not applicable (genetic disorder).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*) *clpb* morphant** — established in-vivo model: morpholino suppression produced a CNS phenotype with cerebellar/cerebral atrophy, rescued by WT but not mutant human *CLPB* mRNA. *"Suppression of clpb in zebrafish embryos induced a central nervous system phenotype that was consistent with cerebellar and cerebral atrophy that could be rescued by wild-type, but not mutant, human CLPB mRNA."* [PMID: 25597510] This demonstrates conserved neurodevelopmental requirement and loss-of-function causality.
- **Cellular/in-vitro models:** patient-derived fibroblasts (complexome profiling showing CLPB/HAX1 high-mass comigration, PMID 34140661); human hematopoietic progenitors and cell lines showing impaired granulocytic differentiation and increased apoptosis (PMID 34115842); CLPB-null cell lines showing IMS aggregation (PMID 38270563); reconstituted recombinant Skd3/CLPB disaggregase assays (PMID 36170828, 42244541).
- **Genetic model types available:** morpholino knockdown (zebrafish), gene knockout and variant-expression cell lines.
- **Limitations:** no established mammalian (mouse) genetic model in the reviewed literature; zebrafish morphants model neurodevelopmental but not the full multisystem phenotype.

---

## Mechanistic Model — Integrated Narrative

The unifying lesion is loss of a single mitochondrial IMS quality-control enzyme. Structurally, Cupo et al. (2022) showed that human CLPB (Skd3) *"adopts a spiral hexameric arrangement that engages substrate via pore-loop interactions in the nucleotide-binding domain (NBD). Substrate-bound Skd3 hexamers stack head-to-head via unique, adaptable ankyrin-repeat domain (ANK)-mediated interactions to form dodecamers."* The decisive insight for inheritance is that *"SCN-linked subunits sharply inhibit disaggregase activity, whereas MGCA7-linked subunits do not. These advances illuminate Skd3 structure and mechanism, explain SCN and MGCA7 inheritance patterns."* [PMID: 36170828]

This single structural fact resolves the genotype–phenotype puzzle:

| Allele configuration | Molecular effect | Clinical result |
|---|---|---|
| Biallelic LoF (stop/stop, severe missense) | No functional disaggregase | Full MEGCANN syndrome; ~66% mortality |
| Monoallelic missense near ATP pocket (SCN-type) | Poisons WT hexamer (dominant-negative) | Isolated severe congenital neutropenia, often no 3-MGA |
| Monoallelic null (heterozygous LoF) | Tolerated (pLI≈0) | Unaffected carrier |

The zygosity-stratified 63-patient cohort empirically confirmed this gradient: *"Death occurred in 66% of biallelic and 23% of monoallelic individuals,"* and *"Structural predictions — particularly variants causing nonsense-mediated decay or ankyrin domain disruption — were stronger survival predictors than zygosity or age of onset."* [PMID: 41719910]

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [25597510](https://pubmed.ncbi.nlm.nih.gov/25597510/) | *CLPB mutations cause 3-MGA, brain atrophy, ID, neutropenia, cataracts, movement disorder* | Founding gene discovery; zebrafish causality; core phenotype |
| [38270563](https://pubmed.ncbi.nlm.nih.gov/38270563/) | *CLPB disaggregase dysfunction impacts the SPY complex* | IMS disaggregase function; downstream SPY impairment |
| [42244541](https://pubmed.ncbi.nlm.nih.gov/42244541/) | *HAX1 drives assembly and activation of CLPB* | HAX1 activation mechanism; metazoan conservation |
| [41719910](https://pubmed.ncbi.nlm.nih.gov/41719910/) | *Zygosity-specific insights in 63 CLPB cases* | Genotype–outcome; mortality; prognostic predictors |
| [34115842](https://pubmed.ncbi.nlm.nih.gov/34115842/) | *Heterozygous CLPB variants cause severe congenital neutropenia* | Dominant-negative monoallelic mechanism; hematopoietic model |
| [34140661](https://pubmed.ncbi.nlm.nih.gov/34140661/) | *Neutropenia and ID are hallmarks of biallelic and de novo CLPB deficiency* | Phenotype enumeration; de novo dominant-negative |
| [36170828](https://pubmed.ncbi.nlm.nih.gov/36170828/) | *Structural features of Skd3 disaggregase* | Hexamer/dodecamer architecture; inheritance explanation |
| [39787888](https://pubmed.ncbi.nlm.nih.gov/39787888/) | *Untargeted metabolomics for 3-MGA syndromes* | 3-MGA biochemistry; biomarker limitations |
| [31729175](https://pubmed.ncbi.nlm.nih.gov/31729175/) | *Delayed appearance of 3-MGA-uria in neonates* | Diagnostic pitfall (fluctuant biomarker) |
| [36485107](https://pubmed.ncbi.nlm.nih.gov/36485107/) | *Genetics of SCN as gateway to personalized therapy* | G-CSF/HSCT standard of care |
| [37193639](https://pubmed.ncbi.nlm.nih.gov/37193639/) | *HAX1-related congenital neutropenia (SCNIR)* | G-CSF efficacy in partner-pathway disease |
| [31030818](https://pubmed.ncbi.nlm.nih.gov/31030818/) | *Congenital neutropenia in children* | Treatment paradigm (G-CSF, HSCT) |

**Evidence source types:** human clinical (25597510, 34140661, 41719910, 36485107, 37193639, 31030818, 39787888, 31729175); in-vitro/cellular (38270563, 34115842, 42244541); model organism (25597510 zebrafish); structural/computational (36170828, 42244541).

---

## Limitations and Knowledge Gaps

- **Small patient numbers.** Even the largest cohort is 63 individuals; prevalence, penetrance, and natural-history estimates carry wide uncertainty.
- **Neurologic mechanism partly inferred.** The link from IMS proteostasis failure to progressive brain atrophy is strongly model-supported (zebrafish) but the human CNS cell-type-specific pathway is not fully demonstrated.
- **3-MGA pathogenesis.** The route to 3-MGA in secondary syndromes (acetyl-CoA buildup → trans-3-methylglutaconyl-CoA) is a mechanistic hypothesis, not fully proven for CLPB specifically; 3-MGA is a fluctuant, insensitive biomarker.
- **No mammalian (mouse) genetic model** is established in the reviewed literature, limiting preclinical therapy testing.
- **Cataract and movement-disorder mechanisms** at the tissue/cellular level remain under-characterized.
- **No therapeutic trials.** All treatment evidence is extrapolated from the SCN/HAX1 paradigm, not CLPB-specific trials.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional mouse model** (tissue-specific *Clpb* knockout in hematopoietic and neural lineages) to test cell-autonomous mechanisms and serve as a preclinical platform.
2. **iPSC-derived neurons, cerebellar organoids, and granulocyte-differentiation assays** from patient cells to map cell-type-specific proteostatic collapse and screen small-molecule chaperone enhancers.
3. **Structure-guided therapeutics** exploiting the HAX1–CLPB activation axis — test whether boosting residual CLPB oligomerization/ATPase (or correcting dominant-negative poisoning) rescues disaggregase activity.
4. **Prospective natural-history registry** with standardized 3-MGA + plasma metabolomics, MRI, and neutrophil monitoring to validate the NMD/ankyrin-disruption prognostic predictor (PMID 41719910).
5. **Systematic reclassification of the ~692 VUS in ClinVar** using functional disaggregase assays and structural prediction to improve diagnostic yield.
6. **Evaluate HSCT timing and outcomes** specifically in CLPB patients (vs generic SCN), given the multisystem neurologic burden transplantation does not address.

---

*Report compiled from aggregated disease-level resources (OMIM, Orphanet, MONDO, gnomAD, ClinVar, UniProt, HGNC) and primary literature. All mechanistic and clinical claims are cited to PMID where available; ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT) are provided for knowledge-base population.*


## Artifacts

- [OpenScientist final report](3-methylglutaconic_Aciduria_Type_VIIB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](3-methylglutaconic_Aciduria_Type_VIIB-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
| Terms checked | 31 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 25 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014561` (2 mentions) - the report calls it "MONDO"; MONDO calls it **3-methylglutaconic aciduria, type VIIB**
- `HP:0001332` (1 mention) - the report calls it "Movement disorder / dystonia"; HP calls it **Dystonia**
- `NCIT:C1512` (1 mention) - the report calls it "G-CSF / filgrastim"; NCIT calls it **Immunoconjugate**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000844` (1 mention), reported as "Congenital neutropenia (→ leukemia/MDS)" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Developmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `HP:0012444` (1 mention) - the report calls it "Progressive brain atrophy"; HP calls it **Brain atrophy**
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `GO:0005758` (2 mentions) - the report calls it "mitochondrial intermembrane space", "Subcellular compartment:** **mitochondrial intermembrane space"; GO calls it **mitochondrial intermembrane space**
- `CL:0000121` (1 mention) - the report calls it "Purkinje/cerebellar neuron"; CL calls it **Purkinje cell**, and lists "Purkinje neuron" among its other names
- `NCIT:C264` (1 mention) - the report calls it "Antiepileptic drugs"; NCIT calls it **Anticonvulsant Agent**, and lists "Antiepileptics" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005758` - called "mitochondrial intermembrane space", "Subcellular compartment:** **mitochondrial intermembrane space"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.