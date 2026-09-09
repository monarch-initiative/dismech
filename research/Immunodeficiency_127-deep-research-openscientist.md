---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:35:27.611908'
end_time: '2026-09-01T22:55:11.725729'
duration_seconds: 1184.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 127
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
citation_count: 1
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 12
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0032251
    reported_labels:
    - Tuberculosis
    ontology_label: Abnormal immune system morphology
  - term_id: CL:0000583
    reported_labels:
    - "Tissue/cell level:** mononuclear phagocytes \u2014 **alveolar macrophages"
    - alveolar macrophage
    ontology_label: alveolar macrophage
  - term_id: UBERON:0002048
    reported_labels:
    - lung
    - Primary organ:** **lung
    ontology_label: lung
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_127-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_127-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 127
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 127** covering all of the
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

# Immunodeficiency 127 (IMD127) — Comprehensive Disease Characteristics Report

**Prepared:** 2026-09-02 · Autonomous literature/database synthesis
**Primary source:** Arias, Neehus, Ogishi et al. "Tuberculosis in otherwise healthy adults with inherited TNF deficiency." *Nature* 633:417–425 (2024). **PMID: 39198650**; DOI 10.1038/s41586-024-07866-3. OMIM **#620977**.

> **Evidence caveat.** IMD127 is an ultra-rare, newly delineated Mendelian disorder described in **a single consanguineous Colombian family (2 affected first cousins)**. Nearly all disease-specific clinical facts derive from this one primary report. Mechanistic corroboration comes from in vitro/iPSC studies, mouse models, and the large pharmacovigilance literature on anti-TNF-associated tuberculosis. Where a statement is inference or extrapolation (e.g., standard TB therapy, epidemiology of TB generally), it is flagged.

---

## 1. Disease Information

**Overview.** Immunodeficiency-127 is an **autosomal recessive inborn error of immunity** characterized by **selective susceptibility to pulmonary tuberculosis (TB)** in otherwise healthy individuals. It is the **first described human inherited TNF (tumor necrosis factor) deficiency**. Affected individuals tolerate BCG vaccination normally, develop recurrent pulmonary *Mycobacterium tuberculosis* infection beginning in the late teens, and have no other consistent infectious or immunologic abnormality (Arias et al. 2024, PMID 39198650).

**Key identifiers.**
- **OMIM:** #620977 (IMMUNODEFICIENCY 127; IMD127); causative gene TNF #191160.
- **MONDO:** **MONDO:0975832** ("immunodeficiency 127") — confirmed via EBI OLS; maps to OMIM:620977.
- **Orphanet:** No specific ORPHA code identified for this newly described entity; conceptually within "Mendelian susceptibility to mycobacterial diseases" (ORPHA:319583) and rare primary immunodeficiency groupings.
- **ICD-11:** Best fit **4A00.0** (primary immunodeficiencies) / predisposition to infection; the clinical infection codes as tuberculosis (ICD-11 **1B1**; ICD-10 **A15–A19**).
- **ICD-10:** D84.9 (immunodeficiency, unspecified) for the trait; A15.- (respiratory TB, bacteriologically confirmed) for disease episodes.
- **MeSH:** No dedicated descriptor; relevant terms: "Tuberculosis, Pulmonary" (D014397), "Tumor Necrosis Factor-alpha" (D014409), "Immunologic Deficiency Syndromes" (D007153).

**Synonyms / alternative names:** Inherited TNF deficiency; **Autosomal recessive complete TNF deficiency** (OMIM's descriptor); Human TNF deficiency; TNF-deficiency Mendelian susceptibility to tuberculosis. OMIM notes the disorder is characterized by ROS-deficient alveolar macrophages, TB onset late in the second decade with common relapse, and infections that respond to medication.

**Data provenance:** Disease-level knowledge is derived from **individual patient data** (deep immunophenotyping of 2 related patients plus family segregation), complemented by **aggregated/experimental** resources (iPSC models, mouse KO literature, anti-TNF pharmacovigilance). Not an EHR-derived aggregate.

---

## 2. Etiology

**Primary cause — genetic.** Biallelic (homozygous) **loss-of-function variant in TNF** (6p21.33). The reported allele is a private frameshift (Section 4). Disease requires infectious exposure to *M. tuberculosis*: the genetic lesion creates susceptibility, and the environmental trigger (Mtb) precipitates disease → a clear **gene × environment (infection) interaction**.

**Genetic risk factors.**
- *Causal:* homozygous TNF null (`c.190_191ins20`, p.Pro64LeufsTer13).
- *Consanguinity* is a major enabling factor (autosomal recessive, private variant; patient homozygosity 1.14% and 2.1%). (PMID 39198650)
- *Related monogenic TB loci* (not modifiers of IMD127 per se, but the differential): TYK2 (incl. common P1104A), IL12RB1, IL12B, IL23R, IFNGR1/2, STAT1, ISG15 (PMID 32055999, 38025345).

**Environmental risk factor (obligate trigger):** exposure to/infection with *Mycobacterium tuberculosis* (NCBI Taxon 1773). General TB risk amplifiers (crowding, HIV, malnutrition, high-burden geography) plausibly apply but are unstudied in IMD127.

**Protective factors.** Not established. By inference, avoidance of Mtb exposure and latent-TB prophylaxis would be protective. Heterozygous carriers are clinically unaffected (recessive). No protective alleles described.

**Gene–environment interaction:** TNF-null genotype is clinically silent until Mtb challenge; conversely Mtb is controlled in TNF-sufficient hosts. This mirrors the acquired phenocopy in which anti-TNF biologics unmask latent TB (Section 12; PMID 29459143).

---

## 3. Phenotypes

Because n=2, "frequencies" below reflect the reported family; interpret cautiously.

| Phenotype | Type | HPO term | Onset | Severity/course | Frequency (this family) |
|---|---|---|---|---|---|
| Recurrent pulmonary tuberculosis | Clinical sign / infectious | **HP:0032262** (Pulmonary tuberculosis); parent HP:0032251 Tuberculosis; HP:0002205 Recurrent respiratory infections | Late teens (18, 19 y) | Recurrent/relapsing but treatment-responsive | 2/2 (100%) |
| Increased susceptibility to mycobacterial infection | Lab/immunologic predisposition | **HP:0004385** related; HP:0002718 (Recurrent bacterial infections) | Adolescent–adult | Selective to Mtb | 2/2 |
| Severe *Listeria monocytogenes* infection (during pregnancy) | Clinical sign / infectious | HP:0031386 (Listeria) / HP:0002718 | Adult | Severe, single episode | 1/2 |
| **Normal** BCG-vaccine tolerance (no BCG-osis) | Absence of expected phenotype | (negative finding) | — | — | 2/2 |
| Normal blood leukocyte subsets | Lab (normal) | — | — | Stable | 2/2 |
| Normal clinical/biological inflammatory responses | Lab (normal) | — | — | Normal | 2/2 |

**Notable negatives (diagnostically important):** No disseminated/extrapulmonary mycobacterial disease, no adverse vaccine reactions, no broad susceptibility to viral/fungal/pyogenic organisms, no autoimmunity, no developmental phenotype.

**Quality-of-life impact:** Driven by recurrent TB episodes (cough, fever, weight loss, treatment burden of multi-month antibiotics, relapse anxiety). Between episodes, patients are functionally healthy. No formal QoL instruments (EQ-5D/SF-36) reported.

---

## 4. Genetic / Molecular Information

**Causal gene:** **TNF** (tumor necrosis factor / TNF-alpha).
- HGNC: **11892**; NCBI Gene: **7124**; Ensembl: **ENSG00000232810**; UniProt: **P01375**; OMIM gene: **191160**.
- Locus: **chromosome 6p21.33**, within the **MHC class III region** (between LTA and LTB/HLA-B).

**Pathogenic variant (OMIM 191160.0007):**
- **cDNA:** `c.190_191ins20` (20-nt insertion), exon 2.
- **Protein:** `p.Pro64LeufsTer13` (P64Lfs*13) — frameshift beginning at codon 64 with a premature stop 13 residues downstream.
- **Type/class:** frameshift insertion → premature termination codon (predicted NMD and/or truncated non-functional protein).
- **Zygosity/origin:** homozygous **germline**; private to the family; **absent in extended relatives and population databases** (MAF <0.01 filter; not observed in gnomAD).
- **Functional consequence:** **complete loss of function.** HEK293 transduced with mutant TNF failed to induce NF-κB-dependent transcription; patient cells showed absent TNF expression, no secreted TNF, and no TNF induction to LPS/BCG/Listeria/IFNγ; **rescued by wildtype TNF** (PMID 39198650).
- **ACMG/AMP classification:** **Pathogenic** — null variant in a gene with established LOF mechanism (PVS1), co-segregation, absence in controls (PM2), functional damage (PS3).

**Modifier genes:** none identified (single family).

**Epigenetic information:** None reported for IMD127. (TNF expression is normally under complex transcriptional/epigenetic control at the MHC-III locus, but no disease-specific epigenetic change is described.)

**Chromosomal abnormalities:** None; point-level insertion, no cytogenetic lesion.

---

## 5. Environmental Information

- **Infectious agent (essential):** *Mycobacterium tuberculosis* (NCBI Taxon **1773**) — the disease-defining pathogen. *Listeria monocytogenes* (NCBI Taxon **1639**) caused one severe episode.
- **Weakly virulent mycobacteria tolerated:** *M. bovis* BCG (vaccine) was handled normally — a key contrast to IFN-γ-circuit defects.
- **Environmental/lifestyle/toxic factors:** none specifically implicated; general TB determinants (exposure intensity, HIV, crowding) presumably relevant but unstudied.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Homozygous TNF frameshift `c.190_191ins20` (p.P64Lfs*13)** *leads to* absence of functional TNF protein (no intracellular, transmembrane, or secreted TNF). *(Demonstrated: absent expression/secretion.)*
2. Absence of TNF *results in* loss of **autocrine/paracrine TNF→TNFR1 (TNFRSF1A) signaling** in mononuclear phagocytes. *(Demonstrated: no NF-κB induction; TNFR1-KO iPSC macrophages phenocopy.)*
3. Loss of TNF–TNFR1 signaling in **GM-CSF-matured monocyte-derived macrophages and alveolar-macrophage-like cells** *leads to* failure of the **NADPH-oxidase respiratory burst** (deficient reactive oxygen species production). *(Demonstrated in patient cells, TNF- and TNFR1-deficient iPSC macrophages, and TNF-blocker-treated control/lung macrophages.)*
4. Impaired respiratory burst *results in* **defective ROS-dependent intracellular killing of ingested *M. tuberculosis*** within lung macrophages. *(Inferred from respiratory-burst defect + rescue by TNF.)*
5. Defective mycobacterial killing in the alveolar compartment *leads to* **uncontrolled Mtb replication and recurrent pulmonary tuberculosis**. *(Observed clinical outcome.)*

**Branch point / redundancy:** Because TNF is **redundant** for (a) IFN-γ production (patients' IFN-γ and downstream cytokines were intact), (b) leukocyte development, (c) systemic inflammation, and (d) control of BCG and most other microbes, the phenotype is **narrowly restricted to Mtb in the lung**. This contrasts with (i) complete phagocyte respiratory-burst deficiency (chronic granulomatous disease), which causes multi-organism infection, and (ii) IFN-γ-circuit MSMD defects, which cause BCG-osis + environmental mycobacterial disease (PMID 39198650, 32055999).

### Mechanistic detail by category
- **Molecular pathways:** TNF–TNFR1 signaling → NF-κB activation (canonical); coupling to **NADPH oxidase (respiratory burst)**. KEGG **hsa04668** (TNF signaling), Reactome **R-HSA-75893** (TNF signaling), **R-HSA-1222556** (NF-κB). ROS generation ~ Reactome R-HSA-1222556 / phagosome pathways.
- **Cellular processes:** phagocytosis and **oxidative microbial killing** in macrophages; innate immune activation. GO: **GO:0045087** innate immune response; **GO:0006801** superoxide metabolic process; **GO:0045730** respiratory burst; **GO:0034612** response to TNF; **GO:0032496** response to LPS; **GO:0050832** defense response to fungus (n/a); **GO:0071356** cellular response to TNF.
- **Protein dysfunction:** TNF is a type II transmembrane homotrimeric cytokine cleaved by **TACE/ADAM17** to soluble TNF; the frameshift abolishes the mature TNF homology domain → loss of function (no misfolding/aggregation/gain-of-function).
- **Immune involvement:** isolated innate-immune effector defect (macrophage killing); adaptive immunity, granuloma-relevant cytokines (IFN-γ) intact clinically.
- **Tissue damage:** driven by unchecked Mtb infection (caseating granulomatous inflammation of lung) rather than a primary tissue-toxic mechanism.
- **Biochemical abnormality:** functional deficiency of the macrophage **respiratory burst / NADPH oxidase output** secondary to absent TNF signaling (not a primary CYBB/NCF defect).
- **Molecular profiling:** iPSC-derived macrophage models (TNF-KO, TNFR1-KO) used for functional dissection; no patient transcriptomic/proteomic/metabolomic datasets published. Respiratory-burst assays are the key functional readout.

**Cell types (CL):** **CL:0000583** alveolar macrophage; **CL:0000235** macrophage; **CL:0001054** CD14+ monocyte; **CL:0000576** monocyte. **Biological process (GO):** GO:0045730 (respiratory burst), GO:0071356 (cellular response to TNF).

---

## 7. Anatomical Structures Affected

- **Primary organ:** **lung** (UBERON:0002048); specifically alveolar/pulmonary parenchyma (UBERON:0002299 alveolus). Disease is **pulmonary and typically bilateral** as per TB.
- **Body system:** **respiratory system** (UBERON:0001004); **immune system** (UBERON:0002405) as the affected functional system.
- **Secondary involvement:** one patient had disseminated *Listeria* (systemic). Classic TB complications (pleura, mediastinal lymph nodes) possible but not emphasized.
- **Tissue/cell level:** mononuclear phagocytes — **alveolar macrophages (CL:0000583)** and monocyte-derived macrophages — are the pathogenically central cells; epithelial/lymphoid compartments intact.
- **Subcellular (GO cellular component):** phagosome (**GO:0045335**), plasma membrane (**GO:0005886**), NADPH oxidase complex (**GO:0043020**), extracellular space (**GO:0005615**) for secreted TNF.
- **Lateralization:** pulmonary TB is generally **bilateral/multifocal**; not a lateralized trait.

---

## 8. Temporal Development

- **Onset:** **adolescent/young-adult** — first TB episodes at ages **18 and 19**. No neonatal/childhood infections despite BCG exposure. Onset pattern: **subacute/chronic** (typical TB).
- **Progression:** **relapsing/recurrent** pulmonary TB; individual episodes are treatment-responsive; disease course over the reported follow-up shows **recurrence rather than relentless progression**.
- **Duration:** the underlying immunodeficiency is **lifelong**; clinical disease is **episodic**, contingent on Mtb exposure/reactivation.
- **Remission:** **treatment-induced** remission of each episode with anti-TB chemotherapy; relapse may occur.
- **Critical period / intervention window:** post-exposure and early infection — latent-TB detection and prophylaxis represent the key opportunity to prevent active disease.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic TNF LOF). Heterozygotes unaffected.
- **Epidemiology:** **Ultra-rare** — to date **1 family, 2 patients** worldwide (PMID 39198650). No prevalence/incidence estimate; effectively <1 per 10^6 (private variant). Broader context: only ~5–10% of Mtb-infected individuals develop TB, and monogenic causes account for a small fraction (e.g., TYK2 P1104A ~1% of TB in Europeans; PMID 32055999).
- **Penetrance:** appears **high upon Mtb exposure** but is **environment-dependent** (requires infection); true penetrance unknown with n=2.
- **Expressivity:** narrow, consistent (isolated pulmonary TB) in the two cases.
- **Anticipation / mosaicism:** not applicable / not reported.
- **Founder effect:** none — variant is **private** to this family.
- **Consanguinity:** central — multigenerational consanguineous pedigree; homozygosity mapping/linkage used for discovery.
- **Carrier frequency:** effectively 0 in populations (variant absent from gnomAD).
- **Population/geography:** single **Colombian** family; no ethnic predilection can be inferred. Sex: both cases female-inclusive (one episode occurred in pregnancy); no sex-ratio inference possible.

---

## 10. Diagnostics

**Clinical/laboratory workup:**
- **Confirm TB:** sputum smear microscopy for acid-fast bacilli, mycobacterial culture, NAAT (e.g., Xpert MTB/RIF), chest imaging (X-ray/CT showing pulmonary infiltrates/cavitation). (Standard TB diagnostics; RadLex/LOINC applicable.)
- **Immunologic screen (typically normal in IMD127):** normal CBC/leukocyte subsets, immunoglobulins, and IFN-γ responses — normality helps distinguish from other IEIs.
- **Functional immunology (research/specialist):** **absent TNF production** by stimulated whole blood/monocytes (LPS, BCG, IFN-γ) and **impaired macrophage respiratory burst** — the pathognomonic functional signature (PMID 39198650).
- **Biomarker:** undetectable serum/secreted TNF after stimulation; the defect is the biomarker.

**Genetic testing (definitive):**
- **WES or WGS** with homozygosity mapping is how the diagnosis was made; **single-gene TNF sequencing** confirms once suspected.
- **Gene panels:** include TNF alongside MSMD/IEI-to-TB genes (TYK2, IL12RB1, IL12B, IL23R, IFNGR1, IFNGR2, STAT1, ISG15, CYBB/CGD genes).
- CMA/karyotype/FISH/mtDNA/repeat testing: **not applicable** (point insertion).

**Clinical criteria / differential diagnosis:** No formal diagnostic criteria (novel disease). Diagnose when a young adult has **recurrent isolated pulmonary TB, normal BCG tolerance, no other infections, normal IFN-γ axis, and biallelic TNF LOF**. **Differential:** TYK2 deficiency (complete or P1104A homozygosity), IL-12Rβ1 deficiency, IFN-γR/STAT1 defects (usually BCG-osis + broader mycobacterial disease), chronic granulomatous disease (broad infection spectrum), HIV and acquired anti-TNF exposure (PMID 32055999, 38025345, 39198650).

**Screening:** cascade genetic testing of relatives; latent-TB screening (IGRA/TST) in gene-positive individuals.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No deaths reported among the 2 patients; **most TB episodes were successfully treated** (PMID 39198650). Untreated pulmonary TB carries substantial mortality generally, but with therapy prognosis appears **favorable** here.
- **Morbidity:** recurrent TB with associated symptoms and treatment burden; potential long-term pulmonary sequelae (bronchiectasis, fibrosis) as in recurrent TB (extrapolated).
- **Recovery potential:** good per episode with standard anti-TB therapy; **relapse/recurrence** is the main issue.
- **Prognostic factors:** timeliness of diagnosis and treatment, adherence, drug-susceptibility of the infecting strain, and ongoing Mtb exposure. No molecular prognostic biomarker beyond genotype.
- **QoL measures:** not formally assessed.

---

## 12. Treatment

**No disease-specific (TNF-replacement) therapy exists.** Management is **treatment and prevention of tuberculosis** plus consideration of the underlying immune defect.

- **Anti-tuberculous chemotherapy (standard of care; extrapolated from TB guidelines):** the **RIPE regimen** — **rifampin (NCIT:C769), isoniazid (NCIT:C566), pyrazinamide (NCIT:C1029), ethambutol (NCIT:C61785)** — typically 2 months intensive + 4 months continuation, adjusted for drug susceptibility. Relapses re-treated per susceptibility.
- **Secondary prophylaxis:** consider latent-TB/secondary preventive therapy (isoniazid or rifamycin-based) given recurrence risk; individualized.
- **Avoid TNF inhibitors** in these patients (would compound the defect) — conversely, this disease validates pre-anti-TNF TB screening in the general population.
- **Conceptual/targeted therapy (not yet applied):** because the respiratory-burst defect is **rescued by exogenous TNF** in vitro, **recombinant TNF or TNFR1 agonism** is a mechanistic (but risky/unproven) concept; likewise **recombinant IFN-γ** benefits IFN-γ-circuit TB but rationale is weaker here since the IFN-γ axis is intact. **No gene/cell therapy, RNA therapy, or clinical trials** exist for IMD127.
- **Pharmacogenomics:** standard TB-drug PGx applies (e.g., NAT2 acetylator status and isoniazid toxicity) but is not IMD127-specific.

NCIT intervention terms: Antitubercular Therapy (**NCIT:C15615**/antibiotic therapy), Rifampin (C769), Isoniazid (C566), Pyrazinamide (C1029), Ethambutol (C61785).

---

## 13. Prevention

- **Primary prevention:** avoid/limit Mtb exposure; **BCG is tolerated** and may be given (no BCG-osis), though its protective efficacy in this specific defect is unknown. Household TB source control.
- **Secondary prevention:** **latent-TB screening (IGRA/TST) and preventive therapy** in genotype-positive relatives; early symptom-triggered evaluation.
- **Tertiary prevention:** adherence support, monitoring for recurrence and pulmonary sequelae.
- **Genetic counseling:** autosomal recessive — 25% recurrence risk per pregnancy for carrier couples; cascade testing; the consanguineous context warrants counseling. Prenatal/preimplantation testing feasible for the known familial variant.
- **Public-health note:** IMD127 exemplifies why **TB screening is mandated before anti-TNF biologic therapy** in the general population (PMID 29459143).

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected host:** *Homo sapiens* (NCBI Taxon **9606**).
- **Orthologous gene:** mouse **Tnf** (NCBI Gene **21926**; MGI:104798); rat **Tnf** (NCBI Gene 24835). Highly conserved TNF-superfamily cytokine.
- **Natural animal disease:** No described naturally occurring inherited-TNF-deficiency disease in companion animals/wildlife (OMIA has no corresponding entry). TNF's anti-mycobacterial role is conserved across mammals (mouse KO data).
- **Comparative pathology:** Mouse Tnf/Tnfr1 loss produces **more severe, lethal** mycobacterial disease (failed granulomas, death from attenuated BCG/M. avium) than the narrow human TB-only phenotype — an important species difference (PMID 10878503, 11433391, 10861087).
- **Zoonotic/cross-species transmission:** not applicable (host genetic trait, not a transmissible disease).

---

## 15. Model Organisms

- **Cellular / iPSC (in vitro) — most disease-relevant:** patient-derived and gene-edited **TNF-KO and TNFR1-KO iPSC-derived, GM-CSF-matured macrophages** and **alveolar-macrophage-like (AML) cells**; TNF-blocker-treated healthy MDMs/AML and ex vivo lung macrophages. **Recapitulate** the respiratory-burst defect and demonstrate **TNF rescue** (PMID 39198650). Cellosaurus/ATCC-type resources apply for iPSC lines.
- **Mouse (mammalian, Mus musculus, Taxon 10090):**
  - Available models: **Tnf−/−**, **Tnf/Lta double-KO** (± LTα transgene), **Tnfrsf1a (TNFR1/TNFRp55)−/−**, **Tnfrsf1b (TNFR2)−/−**; conditional/humanized TNF strains via MGI/IMSR/MMRRC.
  - **Phenotype recapitulation:** reproduce mycobacterial susceptibility and establish **TNFR1 (not TNFR2)** as the essential receptor (PMID 10878503); model granuloma biology.
  - **Limitations:** phenotype is **broader and lethal** (susceptibility to BCG/M. avium, granuloma necrosis/disintegration, death) — does **not** capture the human specificity for virulent Mtb with sparing of BCG and other microbes; also TNF's roles in murine lymphoid architecture differ.
- **Applications:** dissecting TNF–TNFR1 → respiratory-burst axis; testing TNF/IFN-γ rescue; granuloma dynamics; anti-TNF safety modeling.
- **Resources:** MGI (Tnf MGI:104798), IMSR, MMRRC; Cellosaurus for iPSC/macrophage lines.

---

## Ontology term appendix (for KB population)
- **Disease:** OMIM:620977; MONDO → OMIM:620977 (verify term).
- **Gene/protein:** HGNC:11892 (TNF); NCBI Gene 7124; UniProt P01375; Ensembl ENSG00000232810.
- **HPO:** HP:0032262 (Pulmonary tuberculosis), HP:0032251 (Tuberculosis), HP:0002205 (Recurrent respiratory infections), HP:0002718 (Recurrent bacterial infections).
- **GO (BP):** GO:0045730 (respiratory burst), GO:0006801 (superoxide metabolic process), GO:0071356 (cellular response to TNF), GO:0045087 (innate immune response), GO:0032496 (response to LPS).
- **GO (CC):** GO:0045335 (phagosome), GO:0005615 (extracellular space), GO:0005886 (plasma membrane).
- **CL:** CL:0000583 (alveolar macrophage), CL:0000235 (macrophage), CL:0001054 (CD14+ monocyte).
- **UBERON:** UBERON:0002048 (lung), UBERON:0002299 (alveolus), UBERON:0001004 (respiratory system), UBERON:0002405 (immune system).
- **CHEBI:** CHEBI:26523 (reactive oxygen species), CHEBI:18421 (superoxide).
- **NCIT (treatment):** C769 (rifampin), C566 (isoniazid), C1029 (pyrazinamide), C61785 (ethambutol).
- **NCBI Taxon:** 9606 (human), 10090 (mouse), 1773 (M. tuberculosis), 1639 (L. monocytogenes).

---

## Supported vs. refuted hypotheses
- **Supported:** (1) Biallelic TNF LOF causes isolated susceptibility to pulmonary TB (autosomal recessive). (2) TNF is required for the macrophage respiratory burst that kills Mtb; rescued by TNF. (3) TNFR1 is the essential receptor (mouse + iPSC). (4) Anti-TNF drugs phenocopy the disease (2–5× TB risk). (5) TNF deficiency is mechanistically distinct from IFN-γ-circuit MSMD.
- **Refuted / not supported:** TNF is **not** broadly required for human host defense or systemic inflammation (patients otherwise healthy); the disorder does **not** cause BCG-osis or broad infection susceptibility (contrast with mouse KO and CGD).

## Limitations
Single family (n=2); no prevalence, penetrance, long-term survival, or QoL data; treatment is extrapolated from general TB guidelines; no human omics datasets; mouse models over-represent severity. Findings should be revisited as additional families are identified.

## Key references (PMID)
- 39198650 — Arias et al., *Nature* 2024 (primary description of IMD127 / inherited TNF deficiency).
- 32055999 — Boisson-Dupuis, monogenic basis of human TB.
- 35985287 — Casanova & Abel, rare-to-common infection genetics.
- 38025345 — Errami & Bousfiha, MSMD state of the art.
- 32602053 — Mahdaviani et al., MSMD cohort.
- 10878503 — Jacobs et al., TNFR1 vs TNFR2 in mycobacterial immunity (mouse).
- 11433391 — Bopst et al., TNF/LTα and BCG (mouse).
- 10861087 — Ehlers et al., TNFRp55 and M. avium granuloma disintegration (mouse).
- 29459143 — Baddley et al., ESGICH anti-TNF safety/TB.
- 42226371 — Alves et al., umbrella review of TB risk with biologics/JAKi.


## Artifacts

- [OpenScientist final report](Immunodeficiency_127-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_127-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 21 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032251` (2 mentions) - the report calls it "Tuberculosis"; HP calls it **Abnormal immune system morphology**
- `CL:0000583` (3 mentions) - the report calls it "Tissue/cell level:** mononuclear phagocytes — **alveolar macrophages", "alveolar macrophage"; CL calls it **alveolar macrophage**
- `UBERON:0002048` (2 mentions) - the report calls it "lung", "Primary organ:** **lung"; UBERON calls it **lung**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (2 mentions) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032496` (2 mentions) - the report calls it "response to LPS"; GO calls it **response to lipopolysaccharide**, and lists "response to LPS" among its other names
- `CL:0001054` (2 mentions) - the report calls it "CD14+ monocyte"; CL calls it **CD14-positive monocyte**, and lists "monocyte" among its other names
- `UBERON:0002299` (2 mentions) - the report calls it "alveolus"; UBERON calls it **alveolus of lung**, and lists "alveolus" among its other names
- `UBERON:0001004` (2 mentions) - the report calls it "respiratory system", "Body system:** **respiratory system"; UBERON calls it **respiratory system**
- `GO:0045335` (2 mentions) - the report calls it "phagosome"; GO calls it **phagocytic vesicle**, and lists "phagosome" among its other names
- `GO:0005615` (2 mentions) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000583` - called "Tissue/cell level:** mononuclear phagocytes — **alveolar macrophages", "alveolar macrophage"
- `UBERON:0002048` - called "lung", "Primary organ:** **lung"
- `UBERON:0001004` - called "respiratory system", "Body system:** **respiratory system"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.