---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-26T23:39:40.430334'
end_time: '2026-09-26T23:57:55.567711'
duration_seconds: 1095.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Streptococcal Pharyngitis
  mondo_id: MONDO:0021783
  category: Infectious Disease
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
citation_count: 43
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 43
  on_topic: 30
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 18
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0021783
    reported_labels:
    - Mondo
    ontology_label: streptococcal sore throat
  - term_id: MONDO:0005295
    reported_labels:
    - rheumatic heart disease
    ontology_label: intermittent vascular claudication
  - term_id: UBERON:0002007
    reported_labels:
    - heart valve
    ontology_label: medulla of lymph node
  - term_id: NCIT:C61785
    reported_labels:
    - Penicillin
    ontology_label: Hydrocortisone Acetate
  - term_id: NCIT:C287
    reported_labels:
    - Amoxicillin
    ontology_label: Aspirin
  labels_variant: 9
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Streptococcal_Pharyngitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Streptococcal_Pharyngitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Streptococcal Pharyngitis
- **MONDO ID:** MONDO:0021783 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Streptococcal Pharyngitis** covering all of the
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

# Streptococcal Pharyngitis (MONDO:0021783): A Comprehensive Disease Characteristics Report

*Category: Infectious Disease · Evidence base: 55 papers reviewed, 12 confirmed findings*

---

## Summary

**Streptococcal pharyngitis is an acute, usually self-limited infectious tonsillopharyngitis caused by Group A Streptococcus (*Streptococcus pyogenes*, GAS).** The organism — a Gram-positive, catalase-negative, β-hemolytic coccus growing in chains — colonizes the pharyngeal epithelium of the upper respiratory tract, which is a major human reservoir. Adhesion and colonization, mediated by virulence factors including M protein, streptokinase, and pili (T-antigen), are the initiating mechanistic steps. The infection produces a characteristic clinical picture of abrupt fever, severe sore throat, odynophagia, tonsillar exudate, palatal petechiae, a swollen red uvula, and tender anterior cervical lymphadenopathy, typically in children aged 5–15 years.

The disproportionate clinical importance of this common illness derives not from the acute pharyngitis itself — which resolves in most patients within a week — but from its **complications**. These fall into two branches: (1) *suppurative* complications from local/contiguous spread (peritonsillar and retropharyngeal abscess, otitis media, sinusitis, mastoiditis, and rarely intracranial extension); and (2) *non-suppurative autoimmune sequelae* driven by molecular mimicry between streptococcal antigens (particularly M protein) and human tissue — acute rheumatic fever (ARF), rheumatic heart disease (RHD), acute post-streptococcal glomerulonephritis (APSGN), and neuropsychiatric sequelae (Sydenham chorea; the proposed PANDAS entity). Only a small fraction of infections progress to these sequelae, and this progression is gated by host genetics, chiefly HLA class II alleles.

Clinically, **diagnosis requires microbiological confirmation** (rapid antigen detection test [RADT], throat culture, or molecular point-of-care test) rather than clinical scoring alone, because GAS pharyngitis is phenotypically indistinguishable from viral and non-group-A streptococcal causes. **Treatment with penicillin or amoxicillin — to which GAS remains universally susceptible** — provides modest symptomatic benefit but importantly reduces suppurative complications and lowers ARF incidence by 70–80%. The autoimmune sequelae are diagnosed by dedicated frameworks (the 2015 revised Jones criteria for ARF, with Doppler echocardiography), and secondary benzathine penicillin G prophylaxis prevents progression of latent RHD (GOAL randomized controlled trial). RHD affects more than 40.5 million people worldwide and causes ~306,000 deaths annually, making primary and secondary prevention of streptococcal pharyngitis a global public-health priority.

---

## Disease Information (Section 1)

Streptococcal pharyngitis (also "strep throat," GAS/GABHS pharyngitis, streptococcal tonsillopharyngitis, streptococcal sore throat) is an acute bacterial infection of the pharynx and tonsils caused by *Streptococcus pyogenes*. Key identifiers:

| Resource | Identifier |
|---|---|
| **Mondo** | MONDO:0021783 |
| **ICD-10** | J02.0 (streptococcal pharyngitis); J03.00 (acute streptococcal tonsillitis) |
| **ICD-11** | CA02.0 |
| **MeSH** | Pharyngitis (D010612); *Streptococcus pyogenes* (D013297); Streptococcal Infections (D013290) |
| **NCBI Taxonomy** | *Streptococcus pyogenes*, txid1314 |
| **SNOMED CT** | 43878008 (streptococcal sore throat) |

The information for this disease is derived from **aggregated disease-level resources** — clinical guidelines, Cochrane systematic reviews, epidemiological studies, and mechanistic literature — rather than individual patient EHR records (though some cited cohorts, e.g., PMID 34805428, are EHR-based). OMIM and Orphanet do not assign a primary entry to streptococcal pharyngitis itself (it is not a Mendelian disorder), though related host-susceptibility phenotypes for rheumatic fever/RHD appear in the genetics literature.

---

## Key Findings

### F001 — *Streptococcus pyogenes* (Group A Streptococcus) is the causal agent

GAS is a Gram-positive, catalase-negative, β-hemolytic coccus that grows in chains and colonizes the upper respiratory tract, which serves as a major reservoir. Bacterial **adhesion and colonization of the pharyngeal epithelium are the initiating steps** of infection, mediated by virulence factors including M protein and streptokinase.

> *"The upper respiratory tract and skin are major reservoirs for GAS infections. The ability of GAS to establish an infection in the new host at these anatomical sites primarily results from two distinct physiological processes, namely bacterial adhesion and colonization."* — [PMID: 27312939](https://pubmed.ncbi.nlm.nih.gov/27312939/)

> *"It is known to cause a wide range of infections in children, ranging from mild upper respiratory tract infections, such as pharyngitis, to severe invasive disease."* — [PMID: 40572286](https://pubmed.ncbi.nlm.nih.gov/40572286/)

**Ontology suggestions:** infectious agent NCBITaxon:1314 (*S. pyogenes*); GO:0007155 (cell adhesion); UBERON:0006562 (pharynx); CL:0000066 (epithelial cell).

### F002 — Post-streptococcal autoimmune sequelae (ARF, RHD, APSGN) arise via molecular mimicry

Acute rheumatic fever is an autoimmune disorder that follows GAS pharyngitis or impetigo in children and adolescents and may evolve into rheumatic heart disease with persistent valve damage. GAS triggers post-infectious sequelae — APSGN, ARF, and RHD — attributed largely to **molecular mimicry** between streptococcal antigens (e.g., M protein) and human tissue proteins. Critically, detection and treatment of streptococcal pharyngitis reduces ARF incidence by 70–80%, confirming the causal link.

> *"Acute rheumatic fever (ARF) is an autoimmune disorder resulting from Group A Streptococcus (GAS) pharyngitis or impetigo in children and adolescents, which may evolve to rheumatic heart disease (RHD) with persistent cardiac valve damage."* — [PMID: 40484016](https://pubmed.ncbi.nlm.nih.gov/40484016/)

> *"GAS also notably triggers post-infectious immune sequelae, including acute poststreptococcal glomerulonephritis (APSGN), acute rheumatic fever (ARF), and rheumatic heart disease (RHD), which are major health burdens, especially in low-income countries."* — [PMID: 40572286](https://pubmed.ncbi.nlm.nih.gov/40572286/)

> *"Detection and treatment of streptococcal pharyngitis in children reduces acute rheumatic fever by 70-80%."* — [PMID: 41956705](https://pubmed.ncbi.nlm.nih.gov/41956705/)

**Ontology suggestions:** GO:0002250 (adaptive immune response); GO:0042110 (T cell activation); MONDO:0005295 (rheumatic heart disease); UBERON:0002007 (heart valve).

### F003 — Diagnosis requires microbiological confirmation; clinical scores are insufficient alone

Children with GABHS pharyngitis typically present with abrupt fever, intense throat pain, odynophagia, an inflamed pharynx, enlarged erythematous tonsils, a red swollen uvula, and tender anterior cervical lymphadenopathy. Because these features overlap with viral causes, suspected cases **should be confirmed by microbiological testing** (culture, RADT, or molecular point-of-care test) before starting antibiotics. Clinical scores perform poorly: in a pediatric cohort, a Centor score ≥3 had only 22.3% sensitivity and 79.0% specificity for RADT positivity, and 17.1% of RADT-negative patients had positive throat cultures.

> *"Children with GABHS pharyngitis typically present with an abrupt onset of fever, intense pain in the throat, pain on swallowing, an inflamed pharynx, enlarged and erythematous tonsils, a red and swollen uvula, enlarged tender anterior cervical lymph nodes."* — [PMID: 37493159](https://pubmed.ncbi.nlm.nih.gov/37493159/)

> *"Patients suspected of having GABHS pharyngitis should be confirmed by microbiologic testing (e.g., culture, rapid antigen detection test, molecular point-of-care test) of a throat swab specimen prior to the initiation of antimicrobial therapy."* — [PMID: 37493159](https://pubmed.ncbi.nlm.nih.gov/37493159/)

> *"The Centor score alone does not seem to be of any utility in guiding the diagnosis of suspected streptococcal pharyngitis."* — [PMID: 39528865](https://pubmed.ncbi.nlm.nih.gov/39528865/)

Supporting this, a systematic review and meta-analysis of McIsaac and Centor scores concluded both are "equally ineffective at triaging patients who need antibiotics" ([PMID: 38182052](https://pubmed.ncbi.nlm.nih.gov/38182052/)). Cough and coryza are useful to *rule out* GAS; adding RADT to a Centor 3–4 raises positive predictive value to ~93% ([PMID: 34535115](https://pubmed.ncbi.nlm.nih.gov/34535115/)). In college students, GAS and non-group-A streptococcal pharyngitis were clinically indistinguishable ([PMID: 34805428](https://pubmed.ncbi.nlm.nih.gov/34805428/)).

**Ontology / lab-test suggestions:** HP:0025439 (pharyngitis); LOINC 626-2 (throat culture); LOINC 60489-2 (*S. pyogenes* rapid Ag).

### F004 — GAS remains universally penicillin-susceptible; antibiotics give modest symptomatic benefit but prevent complications

GAS remains universally susceptible to penicillin, though macrolide and lincosamide resistance is increasing among invasive isolates, with uncertain clinical consequences. Antibiotics provide only modest benefit for sore-throat symptoms, but effectiveness increases in patients with GABHS-positive swabs.

> *"GAS remains universally susceptible to penicillin but there are increasing reports of macrolide and lincosamide resistance, particularly in invasive isolates, with uncertain clinical consequences."* — [PMID: 39259691](https://pubmed.ncbi.nlm.nih.gov/39259691/)

> *"Antibiotics provide only modest benefit in treating sore throat, although their effectiveness increases in people with positive throat swabs for group A beta-haemolytic streptococci (GABHS)."* — [PMID: 37965935](https://pubmed.ncbi.nlm.nih.gov/37965935/) (Cochrane)

The Cochrane comparative-antibiotics review (19 trials, 5,839 participants) found **no clinically relevant differences** between cephalosporins/macrolides and penicillin for symptom resolution; given low cost and absence of resistance, penicillin remains first-line ([PMID: 33728634](https://pubmed.ncbi.nlm.nih.gov/33728634/)). Where penicillin V is unavailable, amoxicillin 50 mg/kg/day for 10 days is first choice, with macrolides reserved for type-I penicillin allergy ([PMID: 22691611](https://pubmed.ncbi.nlm.nih.gov/22691611/)).

**Ontology suggestions (NCIT/CHEBI):** NCIT:C61785 (Penicillin); NCIT:C287 (Amoxicillin); CHEBI:17334 (penicillin); CHEBI:2676 (amoxicillin).

### F005 — Host HLA class II alleles modulate susceptibility to post-streptococcal rheumatic fever/RHD

Only a small fraction of GAS pharyngitis episodes progress to rheumatic carditis, implicating host genetics. A meta-analysis (13 studies; 1,065 patients / 1,691 controls) identified **HLA-DRB1\*07 as a susceptibility allele (OR ≈ 1.68)** and **HLA-DRB1\*15 as protective**. GWAS implicate the HLA-DQA1–HLA-DQB1 region and the immunoglobulin heavy-chain locus (IGHV4-61) on chromosome 14. Twin studies show much higher RF concordance in monozygotic (19%) than dizygotic (2.5%) twins. TNFA-308 and mannose-binding lectin (MBL) variants are also associated.

> *"The results of the meta-analysis suggest that the differential presentation of autoimmune peptides by HLA-DRB1\*07 (susceptible) and HLA-DRB1\*15 (protective) alleles with different affinities may play a crucial role in the pathogenesis of RF/RHD."* — [PMID: 32967480](https://pubmed.ncbi.nlm.nih.gov/32967480/)

> *"Early findings implicate not only HLA, particularly the HLA-DQA1 to HLA-DQB1 region, but also the immunoglobulin heavy chain locus, including the IGHV4-61 gene segment, on chromosome 14."* — [PMID: 31519994](https://pubmed.ncbi.nlm.nih.gov/31519994/)

> *"the high concordance rate for RF in monozygotic twins (19%) compared to dizygotic twins (2.5%), and the high familial incidence of RF suggest the involvement of host genetic factors in susceptibility to RF"* — [PMID: 37406855](https://pubmed.ncbi.nlm.nih.gov/37406855/)

An independent HLA study found HLA-DRB1\*13, DRB5\*, and DRB3\* to be protective against rheumatic valve damage ([PMID: 16426242](https://pubmed.ncbi.nlm.nih.gov/16426242/)); MBL deficiency and TNFA-308 associations were reviewed in [PMID: 17804571](https://pubmed.ncbi.nlm.nih.gov/17804571/). **HGNC genes:** HLA-DRB1, HLA-DQA1, HLA-DQB1, IGHV4-61, TNF, MBL2.

### F006 — Streptococcal superantigens (SpeA) link pharyngitis to scarlet fever and subvert immunity; the M1UK clone is emerging

Streptococcal pyrogenic exotoxin A (SpeA) expression is epidemiologically linked to tonsillo-pharyngitis and scarlet-fever outbreaks. As a superantigen, SpeA drives massive tonsil T-cell proliferation with proinflammatory cytokine release, yet paradoxically causes **B-cell apoptosis and abrogation of IgA/IgM/IgG production**, subverting protective humoral immunity. The emergent **M1UK variant** (27 SNPs distinct from M1global) is characterized by increased *speA* expression and is driving surges in scarlet fever and invasive disease.

> *"Streptococcal pyrogenic exotoxin (Spe) A expression is epidemiologically linked to streptococcal tonsillo-pharyngitis and outbreaks of scarlet fever"* — [PMID: 30815853](https://pubmed.ncbi.nlm.nih.gov/30815853/)

> *"marked B cell apoptosis and abrogation of total immunoglobulin (Ig)A, IgM, and IgG production occurred in the presence of SpeA and other superantigens"* — [PMID: 30815853](https://pubmed.ncbi.nlm.nih.gov/30815853/)

> *"M1UK differs from progenitor M1global genotype by 27 single-nucleotide polymorphisms and is characterized by increased speA superantigen expression in vitro."* — [PMID: 39206960](https://pubmed.ncbi.nlm.nih.gov/39206960/)

Genomic surveillance in Shanghai documented a parallel rise in *emm1* isolates carrying *speA*, *speC*, and *spd1* virulence genes and *ermB*/*tetM* resistance determinants ([PMID: 32562850](https://pubmed.ncbi.nlm.nih.gov/32562850/)). **GO:** GO:0050852 (T cell receptor signaling); GO:0006915 (apoptotic process).

### F007 — Lewis rat autoimmune valvulitis (RAV) model recapitulates M-protein-driven rheumatic carditis

Immunization of Lewis rats with recombinant GAS M5 protein induces mitral valvulitis and myocarditis with CD3⁺/CD4⁺/CD68⁺ mononuclear infiltration of valve tissue and P-R-interval prolongation on ECG — features resembling human rheumatic carditis. Both anti-M5 antibodies and M5-specific T cells transfer carditis to naïve syngeneic rats, and repeat M-protein exposure exacerbates cardiac damage via an enhanced **anti-cardiac-myosin antibody** response. An M5 B-repeat peptide (aa 161–180) induces lymphocytes cross-reactive to cardiac myosin.

> *"serum plus in vitro expanded rM5-specific T-cells from hyperimmune rats were capable of transferring carditis to naïve syngeneic animals"* — [PMID: 31062619](https://pubmed.ncbi.nlm.nih.gov/31062619/)

> *"repetitive booster immunization with GAS-derived recombinant M protein (rM5) resulted in an enhanced anti-cardiac myosin antibody response that may contribute to the breaking of immune tolerance leading to RF/RHD"* — [PMID: 27562362](https://pubmed.ncbi.nlm.nih.gov/27562362/)

> *"Rats immunized with streptococcal M5 protein developed valvular lesions, distinguished by infiltration of CD3(+), CD4(+), and CD68(+) cells into valve tissue"* — [PMID: 19273562](https://pubmed.ncbi.nlm.nih.gov/19273562/)

This model directly demonstrates the molecular-mimicry mechanism (F002) is *pathogenic and transferable*. Detailed induction protocols are consolidated in [PMID: 42261692](https://pubmed.ncbi.nlm.nih.gov/42261692/). **CL terms:** CL:0000084 (T cell), CL:0000624 (CD4⁺ T cell), CL:0000235 (macrophage, CD68⁺).

### F008 — GAS pharyngitis causes suppurative and non-suppurative complications; antibiotics reduce them

**Suppurative** complications (local spread) include peritonsillar/retropharyngeal abscess (quinsy), sinusitis, mastoiditis, otitis media, and rarely orbital cellulitis, meningitis, brain abscess, and intracranial venous sinus thrombosis. **Non-suppurative (autoimmune)** complications include ARF, APSGN, and neuropsychiatric sequelae (Sydenham chorea; the proposed PANDAS entity with anti-D1R dopamine-receptor autoantibodies targeting the basal ganglia). A Cochrane meta-analysis (27 trials, 2,835 cases) found antibiotics reduced acute otitis media (RR 0.30, 95% CI 0.15–0.58), quinsy, and ARF by more than two-thirds (RR 0.22, 95% CI 0.02–2.08).

> *"Complications associated to group-A streptococcal pharyingitis include non-suppurative complications such as acute rheumatic fever and glomerulonephritis and suppurative complications such as peritonsillar or retropharyngeal abscess, sinusitis, mastoiditis, otitis media, meningitis, brain abscess, or thrombosis of the intracranial venous sinuses."* — [PMID: 23067784](https://pubmed.ncbi.nlm.nih.gov/23067784/)

> *"Antibiotics reduced the incidence of acute otitis media (RR 0.30; 95% CI 0.15 to 0.58)"* — [PMID: 17054126](https://pubmed.ncbi.nlm.nih.gov/17054126/)

> *"Emerging molecular evidence identifies anti-D1R autoantibodies, acting via G protein-and beta-arrestin-mediated signalling, as candidate bi[omarkers]"* — [PMID: 42196589](https://pubmed.ncbi.nlm.nih.gov/42196589/)

The PANDAS/PANS construct remains controversial but biologically plausible; single-cell RNA-seq of a Sydenham chorea patient showed B-cell HLA-DR/DQ upregulation and plasma-cell proteasomal activation, supporting a B-cell-mediated autoantibody hypothesis ([PMID: 40859454](https://pubmed.ncbi.nlm.nih.gov/40859454/); [PMID: 42603022](https://pubmed.ncbi.nlm.nih.gov/42603022/)). **HP terms:** HP:0000388 (otitis media), HP:0000246 (sinusitis), HP:0002072 (chorea for Sydenham).

### F009 — GAS pili (T-antigen) mediate adhesion/colonization and are leading vaccine candidates

GAS pili are surface-exposed structures involved in adhesion and colonization; the major component is the **T-antigen**, which multimerizes to form the pilus shaft and is encoded in the FCT genomic region. A multivalent T-antigen fusion vaccine (TeeVax1–3; 18 T-antigens) produced opsonophagocytic, cross-reactive antibodies covering ~95% of 21 T-antigens and conferred protection against invasive disease in mice. Mucosal delivery of GAS pili via *Lactococcus lactis* generated neutralizing/opsonophagocytic antibodies and improved nasopharyngeal GAS clearance.

> *"Pili of Group A Streptococcus (GAS) are surface-exposed structures involved in adhesion and colonisation of the host during infection. The major protein component of the GAS pilus is the T-antigen, which multimerises to form the pilus shaft."* — [PMID: 33623073](https://pubmed.ncbi.nlm.nih.gov/33623073/)

> *"Combining TeeVax1-3 produced a robust antibody response in rabbits that was cross-reactive to a full panel of 21 T-antigens, expected to provide over 95% vaccine coverage."* — [PMID: 33623073](https://pubmed.ncbi.nlm.nih.gov/33623073/)

> *"intranasal immunisation of mice improved clearance rates of GAS after nasopharyngeal challenge"* — [PMID: 28775292](https://pubmed.ncbi.nlm.nih.gov/28775292/)

No licensed GAS vaccine yet exists; pilus/T-antigen and M-protein-based approaches are the leading strategies ([PMID: 38543606](https://pubmed.ncbi.nlm.nih.gov/38543606/)). **GO:** GO:0009289 (pilus); GO:0007155 (cell adhesion).

### F010 — The ARF sequela is diagnosed by the 2015 revised Jones criteria (AHA)

The 2015 AHA revision of the Jones criteria is the international gold standard for diagnosing ARF. It **stratifies by population risk**, offering two diagnostic pathways — prioritizing specificity in low-risk and sensitivity in moderate/high-risk populations — recommends Doppler echocardiography in all suspected/confirmed cases, and allows **subclinical carditis** to fulfill a major criterion. Evidence of antecedent GAS infection (elevated/rising ASO or anti-DNase B, or positive throat culture/RADT) is a required supporting criterion.

> *"update those criteria to also take into account recent evidence supporting the use of Doppler echocardiography in the diagnosis of carditis as a major manifestation of acute rheumatic fever"* — [PMID: 25908771](https://pubmed.ncbi.nlm.nih.gov/25908771/)

> *"the criteria consider the risk within a population and offer two separate diagnostic pathways that prioritise specificity among those at low risk and sensitivity among those at moderate/high risk"* — [PMID: 27326214](https://pubmed.ncbi.nlm.nih.gov/27326214/)

**Lab biomarkers:** anti-streptolysin O (ASO), anti-DNase B. **Imaging:** Doppler echocardiography.

### F011 — APSGN presents as immune-complex nephritic syndrome with hypocomplementemia

APSGN is an acute autoimmune kidney condition triggered by pharyngitis or skin infection with **specific nephritogenic *S. pyogenes* strains**; it is the most common cause of pediatric acute glomerulonephritis globally. Children present with a nephritic picture: edema, painless hematuria, and hypertension. In a 100-child cohort, low serum C3 occurred in 93.5%, elevated anti-DNase B in 100%, and elevated ASO in 85%; biopsy showed post-infectious nephritis with immune-complex deposits (some crescentic). Treatment is largely supportive (managing hypertension/fluid overload). Incidence is strongly tied to childhood socioeconomic disadvantage and dropped after COVID-19 non-pharmaceutical interventions.

> *"Acute post-streptococcal glomerulonephritis (APSGN) is an acute autoimmune kidney condition triggered by skin infection or pharyngitis caused by specific strains of Streptococcus pyogenes (Group A streptococcus)."* — [PMID: 40174621](https://pubmed.ncbi.nlm.nih.gov/40174621/)

> *"Children typically present with a nephritic clinical picture: oedema, painless haematuria and hypertension."* — [PMID: 40174621](https://pubmed.ncbi.nlm.nih.gov/40174621/)

> *"C3 levels were low in 86/92 (93.5%) children; 94/94 (100%) children had elevated anti-deoxyribonuclease-B (anti-DNase-B) levels; and 80/94 (85%) also had elevated anti-streptolysin O titre (ASOT) at presentation"* — [PMID: 38170231](https://pubmed.ncbi.nlm.nih.gov/38170231/)

APSGN hospitalizations fell markedly after COVID-19 NPIs ([PMID: 38688264](https://pubmed.ncbi.nlm.nih.gov/38688264/)); in Nepal, C3 was depressed in 61.9–100% of cases and pyoderma was the dominant preceding route ([PMID: 40119285](https://pubmed.ncbi.nlm.nih.gov/40119285/)). An experimental rabbit study proposed that GAS IgG-binding surface proteins trigger anti-IgG immune-complex formation and glomerular deposition, offering a complementary (non-mimicry) pathogenic route for APSGN ([PMID: 15676011](https://pubmed.ncbi.nlm.nih.gov/15676011/)). **HP terms:** HP:0000790 (hematuria), HP:0000969 (edema), HP:0000822 (hypertension), HP:0000093 (proteinuria); **UBERON:0000074** (renal glomerulus).

### F012 — Secondary benzathine penicillin G prophylaxis prevents progression of latent RHD (GOAL RCT)

The **GOAL randomized controlled trial** (Uganda; 916 children/adolescents aged 5–17 with echocardiographically confirmed latent RHD) compared intramuscular penicillin G benzathine every 4 weeks for 2 years versus no prophylaxis. Echocardiographic progression at 2 years was significantly lower in the prophylaxis arm, establishing that secondary antibiotic prophylaxis prevents progression of screen-detected latent RHD.

> *"Participants were randomly assigned to receive either injections of penicillin G benzathine (also known as benzathine benzylpenicillin) every 4 weeks for 2 years or no prophylaxis."* — [PMID: 34767321](https://pubmed.ncbi.nlm.nih.gov/34767321/)

> *"Rheumatic heart disease affects more than 40.5 million people worldwide and results in 306,000 deaths annually."* — [PMID: 34767321](https://pubmed.ncbi.nlm.nih.gov/34767321/)

Natural-history data show untreated moderate-to-severe latent RHD progresses in ~47.6% of cases, with younger age and morphological mitral-valve features as risk factors ([PMID: 28972003](https://pubmed.ncbi.nlm.nih.gov/28972003/)). The GOAL protocol powered for a 50% relative risk reduction, randomizing 916 participants ([PMID: 31301533](https://pubmed.ncbi.nlm.nih.gov/31301533/)). **NCIT:** benzathine benzylpenicillin (NCIT:C47476).

---

## Mechanistic Model / Interpretation

### Ordered causal chain

```
1. GAS is transmitted via respiratory droplets and CONTACTS pharyngeal epithelium.
2. Surface adhesins (M protein, pili/T-antigen, fibronectin-binding proteins)
   MEDIATE adhesion → LEADS TO colonization of the tonsillar/pharyngeal mucosa. [F001, F009]
3. Colonization + secreted toxins (streptolysins, SpeA superantigen, proteases)
   TRIGGER local innate inflammation → RESULTS IN the acute pharyngitis phenotype
   (fever, sore throat, tonsillar exudate, tender cervical nodes). [F001, F003, F006]
        |
        |-- BRANCH A (suppurative): unchecked local spread LEADS TO peritonsillar/
        |   retropharyngeal abscess, otitis media, sinusitis, mastoiditis, and rarely
        |   intracranial extension. [F008]
        |
        |-- BRANCH B (immune / non-suppurative):
            4B. Antigen presentation of streptococcal peptides (M protein, N-acetyl-
                glucosamine) by susceptible HLA class II alleles (DRB1*07, DQA1/DQB1)
                ACTIVATES cross-reactive CD4+ T cells and B cells. [F002, F005]
            5B. Molecular mimicry → cross-reactive antibodies + T cells RECOGNIZE
                human cardiac myosin, valve endothelium, glomerular / neuronal antigens.
                (Demonstrated & transferable in Lewis rat RAV model.) [F002, F007]
                  |
                  |-- Cardiac branch: valvulitis/carditis → RESULTS IN acute rheumatic
                  |   fever → repeated exposure LEADS TO chronic rheumatic heart disease. [F007, F010, F012]
                  |-- Renal branch: immune-complex deposition in glomeruli (nephritogenic
                  |   strains) → RESULTS IN APSGN nephritic syndrome + hypocomplementemia. [F011]
                  |-- Neuro branch (inferred/controversial): anti-neuronal / anti-D1R
                      autoantibodies target basal ganglia → Sydenham chorea / PANDAS. [F008]
```

### Upstream vs downstream

| Layer | Element | Direction |
|---|---|---|
| **Initiating lesion** | GAS adhesion/colonization of pharynx (M protein, pili) | Most upstream [F001, F009] |
| **Amplifier** | Superantigen (SpeA) T-cell activation; humoral subversion | Upstream–mid [F006] |
| **Gatekeeper** | Host HLA class II genotype (DRB1\*07 susceptible; DRB1\*15 protective) | Determines whether Branch B proceeds [F005] |
| **Effector (autoimmune)** | Cross-reactive antibodies + T cells vs cardiac myosin/valve/glomerulus/neurons | Downstream [F002, F007, F011] |
| **Clinical endpoint** | Pharyngitis (acute) → ARF/RHD, APSGN, chorea (weeks–years later) | Terminal |

### Cell types and processes

Pharyngeal/tonsillar **epithelial cells** (CL:0000066) are the primary infection site; tonsillar **CD4⁺ T cells** (CL:0000624) and **B cells** (CL:0000236) mediate the superantigen response and autoimmunity; **macrophages** (CL:0000235, CD68⁺) and **plasma cells** infiltrate target tissues. Key GO biological processes: GO:0007155 (cell adhesion), GO:0050852 (TCR signaling), GO:0002250 (adaptive immune response), GO:0006956 (complement activation, APSGN), GO:0006915 (apoptosis, superantigen-induced B-cell death). Anatomy: UBERON:0006562 (pharynx), UBERON:0002372 (tonsil), UBERON:0002007 (heart valve), UBERON:0000074 (glomerulus), UBERON:0002420 (basal ganglia).

---

## Evidence Base

| PMID | Role in report | What it supports |
|---|---|---|
| [27312939](https://pubmed.ncbi.nlm.nih.gov/27312939/) | Primary | Pharynx as reservoir; adhesion/colonization as initiating steps (F001) |
| [40572286](https://pubmed.ncbi.nlm.nih.gov/40572286/) | Primary | GAS causes pharyngitis; triggers APSGN/ARF/RHD sequelae (F001, F002) |
| [40484016](https://pubmed.ncbi.nlm.nih.gov/40484016/) | Primary | ARF as autoimmune sequela evolving to RHD (F002) |
| [41956705](https://pubmed.ncbi.nlm.nih.gov/41956705/) | Primary | Treating pharyngitis reduces ARF 70–80% (F002) |
| [37493159](https://pubmed.ncbi.nlm.nih.gov/37493159/) | Review | Clinical phenotype; need for microbiological confirmation (F003) |
| [39528865](https://pubmed.ncbi.nlm.nih.gov/39528865/) | Primary | Centor score inadequate alone (F003) |
| [38182052](https://pubmed.ncbi.nlm.nih.gov/38182052/) | Meta-analysis | McIsaac/Centor equally ineffective for triage (F003) |
| [34535115](https://pubmed.ncbi.nlm.nih.gov/34535115/) | Primary | Cough/coryza rule out GAS; RADT+Centor PPV 93% (F003) |
| [34805428](https://pubmed.ncbi.nlm.nih.gov/34805428/) | EHR cohort | GAS vs non-group-A pharyngitis clinically indistinguishable (F003) |
| [39259691](https://pubmed.ncbi.nlm.nih.gov/39259691/) | Review | Universal penicillin susceptibility; macrolide resistance (F004) |
| [33728634](https://pubmed.ncbi.nlm.nih.gov/33728634/) | Cochrane | No antibiotic superior to penicillin; penicillin first-line (F004) |
| [22691611](https://pubmed.ncbi.nlm.nih.gov/22691611/) | Guideline | Amoxicillin dosing; macrolides for penicillin allergy (F004) |
| [32967480](https://pubmed.ncbi.nlm.nih.gov/32967480/) | Meta-analysis | HLA-DRB1\*07 susceptible; DRB1\*15 protective (F005) |
| [31519994](https://pubmed.ncbi.nlm.nih.gov/31519994/) | GWAS review | HLA-DQ + IGHV4-61 loci (F005) |
| [37406855](https://pubmed.ncbi.nlm.nih.gov/37406855/) | Primary | Twin concordance 19% vs 2.5% (F005) |
| [16426242](https://pubmed.ncbi.nlm.nih.gov/16426242/) | Primary | DRB1\*13/DRB5\*/DRB3\* protective (F005) |
| [17804571](https://pubmed.ncbi.nlm.nih.gov/17804571/) | Review | TNFA-308, MBL deficiency, DR7-restricted M5 recognition (F005) |
| [30815853](https://pubmed.ncbi.nlm.nih.gov/30815853/) | Primary | SpeA links to pharyngitis/scarlet fever; B-cell apoptosis (F006) |
| [39206960](https://pubmed.ncbi.nlm.nih.gov/39206960/) | Primary | M1UK clone, 27 SNPs, increased speA (F006) |
| [32562850](https://pubmed.ncbi.nlm.nih.gov/32562850/) | Primary | emm1 rise, speA/speC virulence genes (F006) |
| [31062619](https://pubmed.ncbi.nlm.nih.gov/31062619/) | Model organism | M5 Ab/T cells transfer carditis (F007) |
| [27562362](https://pubmed.ncbi.nlm.nih.gov/27562362/) | Model organism | Repeat M-protein → anti-cardiac-myosin Ab (F007) |
| [19273562](https://pubmed.ncbi.nlm.nih.gov/19273562/) | Model organism | CD3/CD4/CD68 valve infiltration (F007) |
| [23067784](https://pubmed.ncbi.nlm.nih.gov/23067784/) | Case/review | Suppurative + non-suppurative complication list (F008) |
| [17054126](https://pubmed.ncbi.nlm.nih.gov/17054126/) | Cochrane | Antibiotics reduce otitis media RR 0.30 (F008) |
| [42196589](https://pubmed.ncbi.nlm.nih.gov/42196589/) | Review | Anti-D1R autoantibodies in PANDAS (F008) |
| [40859454](https://pubmed.ncbi.nlm.nih.gov/40859454/) | scRNA-seq | B-cell HLA-DR/DQ upregulation in Sydenham chorea (F008) |
| [33623073](https://pubmed.ncbi.nlm.nih.gov/33623073/) | Primary | Pili/T-antigen; TeeVax ~95% coverage (F009) |
| [28775292](https://pubmed.ncbi.nlm.nih.gov/28775292/) | Model organism | Mucosal pilus vaccine improves clearance (F009) |
| [25908771](https://pubmed.ncbi.nlm.nih.gov/25908771/) | Guideline | 2015 Jones criteria; echocardiography (F010) |
| [27326214](https://pubmed.ncbi.nlm.nih.gov/27326214/) | Guideline | Risk-stratified diagnostic pathways (F010) |
| [40174621](https://pubmed.ncbi.nlm.nih.gov/40174621/) | Review | APSGN definition + nephritic phenotype (F011) |
| [38170231](https://pubmed.ncbi.nlm.nih.gov/38170231/) | Primary | Lab frequencies: C3 low 93.5%, anti-DNase B 100% (F011) |
| [15676011](https://pubmed.ncbi.nlm.nih.gov/15676011/) | Model organism | IgG-binding proteins → immune complexes (APSGN/carditis) (F011) |
| [34767321](https://pubmed.ncbi.nlm.nih.gov/34767321/) | RCT | GOAL: BPG prevents latent RHD progression; 40.5M affected (F012) |
| [28972003](https://pubmed.ncbi.nlm.nih.gov/28972003/) | Cohort | Latent RHD natural history: 47.6% progression (F012) |

**Evidence-source mix:** human clinical (guidelines, RCTs, cohorts, meta-analyses) dominates; model-organism data (Lewis rat RAV, mouse/rabbit vaccine and immune-complex studies) supports mechanism; in-vitro data (tonsil superantigen assays) and computational/genomic surveillance (M1UK, emm typing, GWAS) complete the picture.

---

## Section-by-Section Coverage Notes

- **Etiology (2):** Infectious cause = GAS (F001). Genetic *risk modifiers* are host HLA class II (F005) — these gate autoimmune sequelae, not primary infection. Environmental risk factors: crowding, school age (5–15 y), winter/early-spring seasonality, socioeconomic disadvantage (esp. APSGN/RHD). Gene–environment interaction: susceptible HLA + GAS exposure is required for ARF (F002, F005).
- **Phenotypes (3):** Fever (HP:0001945), pharyngitis (HP:0025439), odynophagia/dysphagia (HP:0002015), tonsillar exudate, cervical lymphadenopathy (HP:0002751), palatal petechiae, scarlatiniform rash (scarlet fever). Childhood onset; mild–moderate, self-limited/episodic. Sequela phenotypes: carditis (HP:0001635), chorea (HP:0002072), hematuria (HP:0000790).
- **Genetic/molecular (4):** No causal *human* gene (not Mendelian). Susceptibility loci: HLA-DRB1, HLA-DQA1/DQB1, IGHV4-61, TNF, MBL2 (F005). Pathogen genetics: emm/M-protein types, speA, M1UK 27-SNP variant (F006).
- **Environmental (5):** Respiratory droplet transmission; crowding; infectious agent NCBITaxon:1314. No toxin/occupational etiology.
- **Anatomy (7):** Primary — pharynx/tonsils (UBERON:0006562, UBERON:0002372); epithelial tissue. Secondary — heart valves (mitral > aortic), renal glomeruli, basal ganglia, middle ear/sinuses.
- **Temporal (8):** Acute onset; self-limited over ~1 week. ARF latency ~2–4 weeks post-pharyngitis; APSGN ~1–2 weeks (throat) / 3–6 weeks (skin); RHD develops over years with recurrent infection.
- **Epidemiology (9):** GAS pharyngitis is among the most common outpatient infections; ~15–30% of pediatric sore throats. Not inherited (polygenic host susceptibility for sequelae). RHD >40.5M prevalent, ~306,000 deaths/yr (F012), concentrated in low/middle-income countries and Indigenous populations.
- **Diagnostics (10):** RADT/culture/molecular throat swab (F003); ASO & anti-DNase B serology (retrospective); C3 for APSGN (F011); Doppler echocardiography for ARF/RHD (F010). No genetic/omics diagnostics in routine use.
- **Prognosis (11):** Acute pharyngitis excellent (self-limited). RHD is the principal mortality driver. APSGN generally favorable short-term renal outcome in children.
- **Treatment (12):** Penicillin V / amoxicillin first-line (10-day course); benzathine penicillin G for adherence and secondary prophylaxis; macrolides/cephalosporins for penicillin allergy (F004). Supportive analgesia/antipyretics. No gene/cell/RNA therapies applicable.
- **Prevention (13):** Primary — treat pharyngitis to prevent ARF (F002); community programs (PMID 41956705). Secondary — 4-weekly benzathine penicillin G prevents latent RHD progression (GOAL RCT, F012). No licensed vaccine; T-antigen/pilus and M-protein candidates in development (F009).
- **Other species / models (14–15):** GAS is a human-restricted pathogen; the **Lewis rat autoimmune valvulitis model** and mouse nasopharyngeal-challenge / rabbit immune-complex models are the principal experimental systems (F007, F009, F011).

---

## Limitations and Knowledge Gaps

1. **No licensed human GAS vaccine.** T-antigen (TeeVax) and M-protein candidates show promise in animal models (F009), but human efficacy, safety (avoiding autoimmune cross-reactivity), and broad strain coverage remain unproven.
2. **PANDAS/PANS remains contested.** The anti-D1R/anti-neuronal autoantibody mechanism and even the diagnostic entity are supported by translational and single-cell data (F008) but lack universally accepted, reproducible biomarkers.
3. **Host-genetics effect sizes are modest.** HLA associations (OR ≈ 1.68 for DRB1\*07) explain only part of susceptibility; GWAS in ARF/RHD are still emerging and underpowered outside a few populations (F005).
4. **Quantitative ARF-prevention estimate rests on a single Cochrane analysis** with a wide CI (RR 0.22, 95% CI 0.02–2.08) because ARF is now rare in high-income trial settings (F008); most trials were not conducted where complication risk is highest.
5. **Animal models are imperfect.** The Lewis rat reproduces valvulitis/carditis but not the full spectrum (chronic scarring, chorea, glomerulonephritis) of human disease, and no model recapitulates natural pharyngeal transmission-to-sequela progression.
6. **Molecular-profiling gaps:** limited human transcriptomic/proteomic/metabolomic signatures of acute pharyngitis specifically (as opposed to invasive GAS or RHD tissue).
7. **Strain–sequela specificity** (nephritogenic vs rheumatogenic emm types) is described but not mechanistically resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Advance a multivalent GAS vaccine** combining T-antigen (TeeVax) and conserved M-protein epitopes toward controlled human infection / phase-appropriate trials, with rigorous screening for cardiac-myosin cross-reactivity before human dosing (extends F007, F009).
2. **Single-cell + spatial transcriptomics of tonsillar tissue** during acute GAS pharyngitis vs viral pharyngitis, to map the epithelial–immune interface and superantigen-driven T/B-cell dynamics (extends F006).
3. **Prospective HLA-genotyped cohort** linking pharyngitis episodes to ARF/APSGN outcomes to refine risk stratification (validate DRB1\*07/DRB1\*15 and DQ/IGHV4-61; F005) and enable precision secondary prophylaxis.
4. **Define serum/CSF autoantibody panels (anti-cardiac-myosin, anti-D1R, anti-lysoganglioside)** with standardized assays to test PANDAS/Sydenham diagnostic reproducibility (F008).
5. **Scale echocardiographic screening + benzathine penicillin G programs** in endemic regions, building on GOAL to define cost-effectiveness and adherence-support models (F012).
6. **Molecular surveillance of M1UK and emm1/emm12 clones** with paired virulence-gene and antimicrobial-resistance profiling to anticipate scarlet-fever/invasive-disease surges (F006).
7. **Nephritogenic-strain mechanistic studies** to identify the specific streptococcal antigen(s) (e.g., NAPlr, SpeB, IgG-binding proteins) driving immune-complex glomerulonephritis and to explain throat- vs skin-route differences (F011).

---

*Report compiled from 12 confirmed findings and 55 reviewed papers across 5 investigation iterations. Evidence quotes are verbatim from cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Streptococcal_Pharyngitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Streptococcal_Pharyngitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 43 |
| On topic | 30 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 32 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0021783` (2 mentions) - the report calls it "Mondo"; MONDO calls it **streptococcal sore throat**
- `MONDO:0005295` (1 mention) - the report calls it "rheumatic heart disease"; MONDO calls it **intermittent vascular claudication**
- `UBERON:0002007` (2 mentions) - the report calls it "heart valve"; UBERON calls it **medulla of lymph node**
- `NCIT:C61785` (1 mention) - the report calls it "Penicillin"; NCIT calls it **Hydrocortisone Acetate**
- `NCIT:C287` (1 mention) - the report calls it "Amoxicillin"; NCIT calls it **Aspirin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1314` (2 mentions) - the report calls it "S. pyogenes"; NCBITaxon calls it **Streptococcus pyogenes**
- `GO:0050852` (2 mentions) - the report calls it "T cell receptor signaling", "TCR signaling"; GO calls it **T cell receptor signaling pathway**, and lists "TCR signaling pathway" among its other names
- `GO:0006915` (2 mentions) - the report calls it "apoptotic process", "apoptosis, superantigen-induced B-cell death"; GO calls it **apoptotic process**, and lists "apoptotic programmed cell death" among its other names
- `CL:0000624` (2 mentions) - the report calls it "CD4⁺ T cell", "CD4⁺ T cells"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000235` (2 mentions) - the report calls it "macrophage, CD68⁺"; CL calls it **macrophage**
- `HP:0002072` (2 mentions) - the report calls it "chorea for Sydenham"; HP calls it **Chorea**, and lists "Choreiform movements" among its other names
- `UBERON:0000074` (2 mentions) - the report calls it "glomerulus"; UBERON calls it **renal glomerulus**, and lists "glomerulus" among its other names
- `GO:0006956` (1 mention) - the report calls it "complement activation, APSGN"; GO calls it **complement activation**
- `UBERON:0002420` (1 mention) - the report calls it "basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000066` - called "epithelial cell", "epithelial cells"
- `GO:0050852` - called "T cell receptor signaling", "TCR signaling"
- `GO:0006915` - called "apoptotic process", "apoptosis, superantigen-induced B-cell death"
- `CL:0000624` - called "CD4⁺ T cell", "CD4⁺ T cells"