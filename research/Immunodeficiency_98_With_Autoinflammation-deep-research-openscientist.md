---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T20:52:47.020048'
end_time: '2026-09-13T21:09:35.190292'
duration_seconds: 1008.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 98 With Autoinflammation
  mondo_id: MONDO:0024777
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
citation_count: 7
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 13
  relevance_assessed: 13
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0024777
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 98 with autoinflammation, X-linked
  - term_id: HP:0001903
    reported_labels:
    - Lab abnormality
    ontology_label: Anemia
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0005528
    reported_labels:
    - BMF
    ontology_label: Bone marrow hypocellularity
  - term_id: HP:0002719
    reported_labels:
    - Symptom
    ontology_label: Recurrent infections
  - term_id: HP:0002720
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating IgA concentration
  - term_id: HP:0001890
    reported_labels:
    - Lab abnormality
    ontology_label: Autoimmune hemolytic anemia
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_98_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_98_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 98 With Autoinflammation
- **MONDO ID:** MONDO:0024777 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 98 With Autoinflammation** covering all of the
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

# Immunodeficiency 98 With Autoinflammation (IMD98 / TLR8 Gain-of-Function): Comprehensive Disease Profile

**MONDO:0024777 · OMIM 301078 · Orphanet 675628 · Gene: TLR8 (Xp22.2) · Inheritance: X-linked dominant**

---

## Summary

**Immunodeficiency 98 with autoinflammation (IMD98)** is a rare, recently defined X-linked dominant inborn error of immunity (IEI) caused by **gain-of-function (GOF) missense variants in *TLR8***, the gene encoding the endosomal single-stranded-RNA (ssRNA) sensor Toll-like receptor 8. It occupies a distinctive position at the "interface" between bone-marrow-failure (BMF) disorders and inborn errors of immunity: affected individuals present simultaneously with **severe, refractory neutropenia and marrow myeloid hypoplasia** on the one hand and **systemic autoinflammation, lymphoproliferation, and humoral immune defects** on the other. The disease was first delineated in 2021 by Aluri and colleagues, who identified six unrelated males, and was substantially expanded in 2026 by Arnold and colleagues (n = 10, including the first female patient).

The molecular mechanism is now well supported. *TLR8* sits at the Xp22.2 locus and encodes a leucine-rich-repeat horseshoe receptor that forms a preformed dimer in the endosome; upon binding ssRNA degradation products (uridine plus short oligonucleotides) or imidazoquinoline chemical agonists, the dimer reorganizes to bring the two C-termini into proximity and trigger MyD88/TIRAP → IRAK → NF-κB/IRF5 signaling. IMD98 pathogenic variants (recurrent hotspots at codons **Phe494** and **Gly572**, plus **Leu433Phe** and **Ala518Thr**) **stabilize the active dimer**, producing constitutive/hyper-responsive proinflammatory signaling. Strikingly, a majority of patients carry **low-level somatic mosaic variants** (variant allele fraction typically 7–30 %), so routine germline genetic testing can miss the diagnosis. gnomAD constraint metrics (missense Z = 3.49; pLI = 0.92) confirm that *TLR8* is strongly intolerant of missense variation, consistent with a pathogenic missense/GOF mechanism.

Clinically, IMD98 is **often fatal without treatment** — the two childhood-onset patients in the expanded cohort who did not undergo transplant died of disease. **Allogeneic hematopoietic cell transplantation (HCT) is currently the only curative therapy**, with five of seven transplanted patients surviving 1–3 years with full donor chimerism and resolution of the disease phenotype (albeit with high rates of post-HCT cytopenia and graft-versus-host disease). Because human TLR8 differs functionally from mouse TLR8, murine models poorly recapitulate the disease, and patient iPSC-derived myeloid cells and HEK293 NF-κB reporter assays are the principal experimental systems. This report consolidates the disease profile across all 15 knowledge-base sections.

---

## Key Findings

### Finding 1 — IMD98 is an X-linked dominant disorder caused by TLR8 gain-of-function variants

The founding study (Aluri et al., 2021) identified **six unrelated males** with a shared syndrome of neutropenia, recurrent infections, lymphoproliferation, humoral immune defects, and in some cases bone marrow failure, all carrying one of **three different variants in the X-linked gene *TLR8***. Critically, **five of the six patients carried somatic (mosaic) variants with less than 30 % mosaicism**, establishing a dominant disease mechanism operating even at low variant allele burden. All identified variants conferred gain of function.

> "We identified 6 unrelated males with neutropenia, infections, lymphoproliferation, humoral immune defects, and in some cases bone marrow failure associated with 3 different variants in the X-linked gene TLR8, encoding the endosomal Toll-like receptor 8 (TLR8)." — [PMID: 33512449](https://pubmed.ncbi.nlm.nih.gov/33512449/)

> "5 patients had somatic variants in TLR8 with <30% mosaicism, suggesting a dominant mechanism responsible for the clinical phenotype" — [PMID: 33512449](https://pubmed.ncbi.nlm.nih.gov/33512449/)

The 2026 expansion (Arnold et al.) broadened the phenotype to **10 patients** and, importantly, described the **first female patient**, who presented during infancy with pure red cell aplasia due to a **germline** *TLR8* variant. Peripheral-blood VAF ranged from 7–26 %, and onset spanned 9 months to 28 years. The female germline case, together with the predominance of affected males and the dominant behavior of low-VAF mosaic variants, is consistent with **X-linked dominant** inheritance.

> "We identify the first female patient with TLR8 GOF who presented during infancy with pure red cell aplasia due to a germ line TLR8 variant" — [PMID: 41370196](https://pubmed.ncbi.nlm.nih.gov/41370196/)

### Finding 2 — TLR8 is an endosomal ssRNA sensor signaling via MyD88/NF-κB; GOF causes constitutive proinflammatory signaling

TLR8 is a pattern-recognition receptor localized to the endosome that senses **degradation products of single-stranded RNA**. Crystallographic work (Tanji et al., 2013, 2015) demonstrated that TLR8 is a leucine-rich-repeat horseshoe that exists as a **preformed dimer**; agonist binding at two distinct sites reorganizes the dimer so that the two C-terminal TIR domains are brought into proximity, enabling downstream signaling.

> "Upon ligand stimulation, the TLR8 dimer was reorganized such that the two C termini were brought into proximity." — [PMID: 23520111](https://pubmed.ncbi.nlm.nih.gov/23520111/)

> "TLR8 recognized two degradation products of ssRNA—uridine and a short oligonucleotide—at two distinct sites" — [PMID: 25599397](https://pubmed.ncbi.nlm.nih.gov/25599397/)

In IMD98, GOF variants confer increased or constitutive responsiveness. Aluri et al. showed that patient iPSC-derived myeloid cells had increased responsiveness to TLR8 stimulation and a proinflammatory phenotype, with activated T cells, elevated serum cytokines, and impaired B-cell maturation — directly linking TLR8 GOF to the autoinflammatory and immune-dysregulatory clinical picture.

> "immune phenotyping demonstrated a proinflammatory phenotype with activated T cells and elevated serum cytokines associated with impaired B-cell maturation" — [PMID: 33512449](https://pubmed.ncbi.nlm.nih.gov/33512449/)

### Finding 3 — Clinical phenotype: refractory neutropenia, marrow myeloid hypoplasia, LGL expansion, lymphoproliferation; HCT is curative

Arnold et al. (2026, n = 10) provide the most detailed natural-history and management data. **All patients had neutropenia**, most severe and refractory to medical therapy; **anemia and thrombocytopenia were common**. Bone marrow characteristically demonstrated **severe myeloid hypoplasia and activated T-cell infiltrates and/or aggregates**. An **increased number of large granular lymphocytes (LGLs)** was identified in 5 of 10 patients. Eight patients had somatic mosaicism (VAF 7–26 %), and onset ranged from 9 months to 28 years.

> "All patients had neutropenia, most with severe neutropenia refractory to medical therapy. Anemia and thrombocytopenia were common. Bone marrow characteristically demonstrated severe myeloid hypoplasia and activated T-cell infiltrates and/or aggregates." — [PMID: 41370196](https://pubmed.ncbi.nlm.nih.gov/41370196/)

> "An increased number of large granular lymphocytes (LGLs) was identified in 5 patients." — [PMID: 41370196](https://pubmed.ncbi.nlm.nih.gov/41370196/)

Prognosis is grave without definitive therapy, but **allogeneic HCT is curative**. Seven patients underwent transplant with high rates of post-HCT cytopenia and GVHD; five are surviving 1–3 years post-HCT with full donor chimerism and phenotype resolution. The two childhood-onset patients who did not undergo HCT died of disease.

> "Five patients are surviving at 1 to 3 years after HCT with full donor myeloid and T-cell chimerism, and resolution of disease phenotype. The 2 patients who presented during childhood and did not undergo HCT ultimately died from disease." — [PMID: 41370196](https://pubmed.ncbi.nlm.nih.gov/41370196/)

### Finding 4 — Specific TLR8 GOF variants (e.g., A518T) stabilize the active dimer and enhance NF-κB-driven cytokine secretion

Skenteris et al. (2026) characterized a novel hemizygous missense variant, **A518T**, in two male siblings with recurrent infections and systemic inflammation. Functional studies confirmed the GOF mechanism at the signaling level: the variant enhanced NF-κB activation and increased proinflammatory cytokine secretion versus wild-type upon stimulation. Computational modeling provided a structural rationale — the substitution introduces additional water-mediated hydrogen bonds that **stabilize the active TLR8 homodimer interface**. Interestingly, protein assays showed reduced mutant abundance due to faster turnover/proteasomal degradation, indicating the GOF is not simply a consequence of increased protein levels but of altered signaling per molecule.

> "Functional studies showed that the TLR8 A518T variant enhanced NF-κB activation and increased secretion of proinflammatory cytokines compared with WT TLR8 upon stimulation, consistent with a gain-of-function effect." — [PMID: 41729082](https://pubmed.ncbi.nlm.nih.gov/41729082/)

> "Computational modeling predicted enhanced structural stabilization of the active TLR8 homodimer interface via additional water-mediated hydrogen bonds introduced by the A518T substitution." — [PMID: 41729082](https://pubmed.ncbi.nlm.nih.gov/41729082/)

Broader X-chromosome immunology literature (Miquel et al., 2023) places these observations in context: TLR7 and TLR8, encoded at the Xp locus, are causal in sex-biased autoimmunity via gene-dosage effects or gain-of-function mutations.

### Finding 5 — Mouse TLR8 is a poor model; human downstream signaling uses MyD88-TIRAP-IRAK-IRF5/NF-κB

A recurring theme with therapeutic and experimental implications is that **mouse TLR8 does not faithfully model human TLR8**. Although rodent and non-rodent TLR8 primary sequences are similar, the antiviral compound R848 that activates the TLR8 pathway is **species-specific**, with sequence variation concentrated near the ligand-binding site (LRR14–15).

> "The primary sequences of rodent and non-rodent TLR8s are similar, but the antiviral compound (R848) that activates the TLR8 pathway is species-specific." — [PMID: 21949866](https://pubmed.ncbi.nlm.nih.gov/21949866/)

Human TLR8 signals through a **TIRAP-MyD88 complex** that drives IRAK1/Akt/IKK activity and IRF5 dimerization for IRF5-regulated cytokines (IFNβ, IL-12); this TIRAP requirement is not recapitulated in mouse. Human IRAK-2 (which, unlike mouse, has no inhibitory splice variants) is required for TLR8-mediated NF-κB/p38 activation and TNF induction. Tissue-expression studies further show TLR8 protein strongly expressed in human but essentially undetectable in mouse pancreatic islets.

> "P7-Pen failed to inhibit murine TLR7 responses, which correlated with a lack of TIRAP recruitment to MyD88 in mouse macrophages" — [PMID: 41159953](https://pubmed.ncbi.nlm.nih.gov/41159953/)

### Finding 6 — ClinVar catalogs recurrent pathogenic TLR8 variants at hotspot codons Phe494 and Gly572

ClinVar (transcript NM_138636.5) curates several disease-associated *TLR8* variants to "Immunodeficiency 98 with autoinflammation, X-linked," revealing **mutational hotspots**:

| Variant (protein) | cDNA | ClinVar classification | Notes |
|---|---|---|---|
| p.Leu433Phe | c.1299G>C | Pathogenic | |
| p.Phe494Tyr | c.1481T>A | Likely pathogenic | Hotspot codon 494 |
| p.Phe494Leu | c.1482C>A | Pathogenic | Hotspot codon 494 |
| p.Gly572Val | c.1715G>T | Pathogenic | Condition: autoimmune hemolytic anemia; systemic autoinflammation |
| p.Gly572Asp | c.1715G>A | Pathogenic | Hotspot codon 572 |
| p.Glu133fs | c.396del | Likely pathogenic | Frameshift |
| p.Ser31Pro / p.Gln110Glu / p.Pro432Leu | — | VUS | Uncertain significance |

Recurrent substitutions at **Phe494** and **Gly572** indicate mutational hotspots. *TLR8* has 314 total ClinVar records, including large Xp deletions unrelated to IMD98.

### Finding 7 — TLR8 is strongly constrained against missense variation in gnomAD

gnomAD (GRCh38) constraint metrics for *TLR8* (ENSG00000101916; NCBI 51311; HGNC:15632; chrX:12,906,620–12,923,169; Xp22.2) support a pathogenic missense/GOF mechanism:

- **Missense Z-score = 3.49** (strong missense constraint; observed/expected = 0.71, 90 % CI 0.66–0.76)
- **LoF pLI = 0.92**, oe_lof = 0.27 (observed 5 vs expected 18.5 LoF variants)

The IMD98 pathogenic variants (Leu433Phe, Phe494Tyr/Leu, A518T, Gly572Val/Asp) are private/ultra-rare and absent or vanishingly rare in gnomAD — consistent with severe, highly penetrant GOF alleles under strong negative selection.

### Finding 8 — Verified disease identifiers and cross-references

Per EBI OLS4 (MONDO ontology) for MONDO:0024777 "immunodeficiency 98 with autoinflammation, X-linked":

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0024777 |
| OMIM | 301078 |
| Orphanet | 675628 |
| Disease Ontology (DOID) | 0061068 |
| GARD | 0027130 |
| MedGen | C1805285 (UID 1805285) |
| UMLS | C5676883 |
| Gene | TLR8 · HGNC:15632 · ENSG00000101916 · NCBI Gene 51311 · Xp22.2 |

**Synonyms:** IMD98; X-linked immunodeficiency with autoinflammation; "inflammation, neutropenia, bone marrow failure, and lymphoproliferation caused by TLR8."

---

## Section-by-Section Report

### 1. Disease Information

IMD98 is a rare monogenic inborn error of immunity that manifests as a combined **bone-marrow-failure + autoinflammation** syndrome. Onset of recurrent infections with lymphoproliferation and autoinflammation typically occurs in the first decade of life; mostly males are affected, and carrier females may have mild symptoms. Immune dysregulation includes hypogammaglobulinemia and reduced memory B cells, skewed T-cell subsets, increased proinflammatory cytokines, activated T cells and monocytes, and autoimmune cytopenias including neutropenia. Identifiers are listed in Finding 8. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO) and **individual-patient case series** (Aluri 2021; Arnold 2026; Skenteris 2026) rather than EHR-scale data — the disease is ultra-rare (≈16 reported patients total across the primary literature).

### 2. Etiology

**Causal factor:** monogenic — **gain-of-function missense variants in *TLR8***. Variants arise as **germline** (including the first female case) or, more commonly, **low-level somatic mosaic** events (VAF ~7–30 %). **Genetic risk factors:** hemizygous male sex (single X); recurrent hotspot variants at Phe494 and Gly572; other pathogenic alleles Leu433Phe and A518T. **Modifier genes:** none formally established; downstream signaling components (MyD88, TIRAP, IRAK1/2, IRF5) are mechanistic candidates. **Environmental risk/protective factors and gene–environment interactions:** none established; TLR8 endogenous ligands are ssRNA degradation products, and infection-associated RNA could plausibly amplify signaling, but this is not demonstrated. No protective alleles are described.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Neutropenia (severe, refractory) | Lab abnormality | HP:0001875 / HP:0000823 | All patients (10/10 Arnold) |
| Anemia | Lab abnormality | HP:0001903 | Common |
| Thrombocytopenia | Lab abnormality | HP:0001873 | Common |
| Bone marrow myeloid hypoplasia | Lab/histology | HP:0005528 (BMF) | Characteristic |
| Recurrent infections | Symptom | HP:0002719 | Core feature |
| Lymphoproliferation | Clinical sign | HP:0002732 / HP:0002716 | Core feature |
| Increased large granular lymphocytes | Lab abnormality | — | 5/10 |
| Hypogammaglobulinemia / reduced memory B cells | Lab abnormality | HP:0002720 | Present |
| Systemic autoinflammation / elevated cytokines | Lab/symptom | HP:0002090-adjacent | Present |
| Autoimmune cytopenias (e.g., AIHA, pure red cell aplasia) | Lab abnormality | HP:0001890 | Present; PRCA in female germline case |

**Onset:** first decade in most, but range 9 months–28 years. **Severity:** severe and often refractory. **Progression:** progressive without treatment, frequently fatal. **QoL impact:** substantial — recurrent infections, transfusion/G-CSF dependence, marrow failure, and transplant morbidity.

### 4. Genetic / Molecular Information

**Causal gene:** *TLR8* (HGNC:15632; Xp22.2). **Pathogenic variants:** missense predominate (Leu433Phe, Phe494Tyr/Leu, A518T, Gly572Val/Asp) plus a likely-pathogenic frameshift (Glu133fs); classifications per ACMG/ClinVar range from Pathogenic to VUS (Finding 6). **Allele frequency:** private/ultra-rare, absent or vanishingly rare in gnomAD (Finding 7). **Somatic vs germline:** both — most patients mosaic (VAF 7–30 %), minority germline. **Functional consequence:** **gain of function** via stabilization of the active dimer (Findings 2, 4). **Modifier genes / epigenetics / chromosomal abnormalities:** not established for IMD98 (note: large Xp deletions in ClinVar are unrelated to this GOF disease).

### 5. Environmental Information

No environmental, lifestyle, or infectious causal agents are established. TLR8's physiologic ligands are ssRNA degradation products (uridine + short oligonucleotides), so RNA from infections is a plausible but unproven amplifier of GOF signaling. The disease is fundamentally **genetically determined**.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **germline or somatic mosaic GOF missense variant in *TLR8*** (e.g., Phe494, Gly572, Leu433Phe, A518T) arises → **leads to** an amino-acid substitution in the endosomal TLR8 ectodomain/dimer interface.
2. The substitution **stabilizes the active TLR8 homodimer** (demonstrated computationally and functionally for A518T; inferred structurally for hotspot residues) → **results in** increased/constitutive receptor activation independent of, or hypersensitive to, ssRNA ligand.
3. Active TLR8 dimer brings the two C-terminal TIR domains into proximity → **recruits** the **TIRAP–MyD88** adaptor complex (human-specific requirement).
4. MyD88 → **activates** **IRAK1/IRAK2** → **IKK/NF-κB** and **IRF5** dimerization → **drives** transcription of proinflammatory cytokines.
5. Excess cytokine output → **produces** systemic autoinflammation, activated T cells and monocytes, and (branch A) **marrow suppression** → severe refractory neutropenia, myeloid hypoplasia, anemia, thrombocytopenia; and (branch B) **immune dysregulation** → impaired B-cell maturation, hypogammaglobulinemia, reduced memory B cells, lymphoproliferation, LGL expansion, autoimmune cytopenias.
6. Untreated → **progresses to** bone marrow failure and death (inferred from fatal untreated childhood cases); replacing the mutant hematopoietic compartment by **allogeneic HCT** → resolves the phenotype.

**Molecular pathways:** endosomal TLR → MyD88/TIRAP → IRAK → NF-κB (GO:0034163 regulation of TLR8 signaling; GO:0043123 positive regulation of NF-κB) and IRF5. **Cellular processes:** inflammation, myeloid differentiation arrest, T-cell activation. **Protein dysfunction:** GOF via dimer-interface stabilization. **Immune involvement:** simultaneous immunodeficiency (humoral defect) and autoinflammation. **Cell types (CL):** neutrophils/myeloid progenitors (CL:0000775 / CL:0000037 HSC), T cells (CL:0000084), monocytes (CL:0000576), large granular lymphocytes/NK-T. **Subcellular compartment:** endosome (GO:0005768).

### 7. Anatomical Structures Affected

**Primary organ:** bone marrow (UBERON:0002371) and the hematopoietic/immune system (UBERON:0002390 / UBERON:0000178 blood). **Secondary:** lymphoid organs — spleen and lymph nodes (lymphoproliferation; UBERON:0002106, UBERON:0000029). **Body system:** hematopoietic/immune. **Tissue/cell level:** myeloid lineage (hypoplasia), activated T-cell infiltrates, LGLs, B cells (impaired maturation). **Subcellular:** endosomal membrane (TLR8 localization). **Lateralization:** systemic/bilateral (not focal).

### 8. Temporal Development

**Onset:** pediatric in most (first decade), range 9 months–28 years; germline female case in infancy. **Pattern:** chronic-progressive with autoinflammatory features; refractory to standard therapy. **Course:** progressive marrow failure and infection; **often fatal without HCT**. **Remission:** treatment-induced (transplant), with full donor chimerism and phenotype resolution; no spontaneous remission described. **Critical period:** early definitive treatment (HCT) before irreversible marrow failure/complications.

### 9. Inheritance and Population

**Inheritance:** **X-linked dominant.** Predominantly affected males (hemizygous); the first female patient had a germline variant with infantile presentation; carrier females may be mildly symptomatic. Somatic mosaic variants behave dominantly even at low VAF. **Penetrance/expressivity:** high penetrance in males; variable expressivity/onset. **Epidemiology:** ultra-rare — ~16 patients in the literature; true prevalence/incidence unknown (not quantified in registries). **Founder effects/consanguinity:** none (mostly de novo/mosaic). **Carrier frequency:** not established. **Sex ratio:** strongly male-predominant.

### 10. Diagnostics

**Genetic testing is definitive**, but must account for **somatic mosaicism**: deep next-generation sequencing (high read depth) of *TLR8* on peripheral blood and, ideally, on affected tissue (bone marrow/sorted myeloid cells) is required, because low-VAF variants can be missed by standard germline WES/panels. **Recommended approach:** targeted *TLR8* sequencing / IEI-BMF gene panels with high-depth NGS and mosaicism-aware variant calling; WES/WGS with careful low-VAF analysis. **Supporting labs:** CBC (neutropenia, anemia, thrombocytopenia), bone marrow biopsy (myeloid hypoplasia, activated T-cell infiltrates, LGLs), immunoglobulins (hypogammaglobulinemia), B-cell memory subsets, cytokine profiling, T-cell activation markers. **Functional confirmation:** NF-κB reporter / cytokine-secretion assays in HEK293 or patient iPSC-derived myeloid cells demonstrate GOF. **Differential diagnosis:** other IEI/BMF "interface disorders," severe congenital neutropenia, T-LGL leukemia, autoimmune lymphoproliferative syndrome, other autoinflammatory syndromes; UNC93B1-GOF (which enhances TLR7/TLR8 signaling causing SLE/chilblain lupus, PMID 38869500) is a mechanistically related differential.

### 11. Outcome / Prognosis

**Without treatment:** poor — the two untreated childhood-onset patients died of disease. **With allogeneic HCT:** curative in the majority — 5 of 7 transplanted patients surviving 1–3 years with full donor myeloid and T-cell chimerism and resolution of phenotype, though with high rates of post-HCT cytopenia and GVHD. **Prognostic factors:** early definitive therapy; transplant-related complications are the main threat to survival after HCT. **Morbidity:** transfusion/growth-factor dependence, infection burden, transplant morbidity.

### 12. Treatment

- **Definitive/curative:** **allogeneic hematopoietic cell transplantation** (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) — the only established cure; replaces the mutant hematopoietic compartment.
- **Supportive:** G-CSF (variable response; neutropenia often refractory), transfusions, antimicrobial prophylaxis, immunoglobulin replacement for humoral defect.
- **Immunomodulation / precision candidates (rational, mechanism-based):** because signaling flows through TLR8 → MyD88 → IRAK → NF-κB/IRF5, targeted inhibition (e.g., IRAK inhibitors, JAK inhibitors for cytokine-driven inflammation, or TLR7/8 antagonists / TIRAP-MyD88 inhibitors such as the P7-Pen tool compound, PMID 41159953) is a plausible bridge-to-transplant or steroid-sparing strategy — **investigational only.**
- **Pharmacogenomics/gene therapy/RNA therapy:** none established.

### 13. Prevention

No primary prevention exists for a de novo/mosaic monogenic GOF disorder. **Secondary prevention:** early genetic diagnosis (mosaicism-aware sequencing) enables timely HCT before irreversible marrow failure. **Genetic counseling:** recurrence risk is generally low for somatic mosaic/de novo variants but non-negligible for germline cases (X-linked dominant); counseling and, where a germline variant is identified, cascade/prenatal testing are appropriate. **Tertiary prevention:** infection prophylaxis and transplant-complication management.

### 14. Other Species / Natural Disease

No naturally occurring animal disease equivalent is described. Comparative genomics shows TLR8 is broadly conserved across mammals, yet **human and mouse TLR8 diverge functionally** (species-specific R848 responsiveness and downstream TIRAP requirement; Finding 5), and TLR8 protein is strongly expressed in human but not mouse pancreatic islets. Orthologs exist (mouse *Tlr8*, NCBI Gene 170744) but do not model the human GOF disease. No zoonotic or cross-species transmission (non-infectious genetic disease).

### 15. Model Organisms

**Mouse is a poor model** for reasons above. The **principal experimental systems** are: (1) **patient iPSC-derived myeloid cells**, which recapitulate increased TLR8 responsiveness and the proinflammatory phenotype; and (2) **HEK293 NF-κB reporter assays** transfected with WT vs mutant TLR8 to quantify GOF (used for A518T and other variants). These capture the signaling GOF and cytokine output but do not fully reproduce the in vivo marrow-failure/lymphoproliferation phenotype. Humanized or knock-in models are not established and would need to address human-specific TLR8 ligand recognition and TIRAP-dependent signaling.

---

## Mechanistic Model / Interpretation

```
 TLR8 GOF missense variant (germline or somatic mosaic, VAF ~7–30%)
   │  hotspots: Phe494, Gly572; also Leu433Phe, Ala518Thr
   ▼
 Stabilized ACTIVE TLR8 homodimer in the endosome
   │  (extra water-mediated H-bonds at dimer interface; A518T shown)
   ▼
 C-terminal TIR domains juxtaposed → TIRAP–MyD88 recruitment (human-specific)
   ▼
 IRAK1/IRAK2 → IKK/NF-κB  +  IRF5 dimerization
   ▼
 Excess proinflammatory cytokines / systemic autoinflammation
   ├──────────────► Branch A: Bone marrow suppression
   │                 → severe refractory neutropenia, myeloid hypoplasia,
   │                   anemia, thrombocytopenia, activated-T/LGL marrow infiltrates
   └──────────────► Branch B: Immune dysregulation
                     → impaired B-cell maturation, hypogammaglobulinemia,
                       reduced memory B cells, lymphoproliferation,
                       autoimmune cytopenias (e.g., PRCA, AIHA)
   ▼
 Untreated → progressive BMF → death
 Allogeneic HCT → replace mutant hematopoietic compartment → phenotype resolves
```

**Upstream vs downstream:** the mutation and dimer stabilization are the upstream drivers; NF-κB/IRF5-driven cytokine excess is the central node; marrow failure and humoral defects are downstream manifestations. The mosaic-yet-dominant behavior implies that even a minority of hematopoietic cells bearing the GOF allele can drive a systemic inflammatory milieu sufficient to suppress normal marrow — explaining why HCT (eliminating the mutant clone) is curative.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [33512449](https://pubmed.ncbi.nlm.nih.gov/33512449/) | *Immunodeficiency and bone marrow failure with mosaic and germline TLR8 GOF* | Founding cohort; gene discovery; mosaicism; GOF; proinflammatory phenotype (F1, F2) |
| [41370196](https://pubmed.ncbi.nlm.nih.gov/41370196/) | *Clinical characteristics, management, and HCT of patients with TLR8 GOF* | Expanded cohort (n=10); phenotype, LGLs, HCT outcomes, first female (F1, F3) |
| [41729082](https://pubmed.ncbi.nlm.nih.gov/41729082/) | *Structural modeling and functional characterization of a novel GOF TLR8 variant* | A518T functional + structural GOF evidence (F4) |
| [23520111](https://pubmed.ncbi.nlm.nih.gov/23520111/) | *Structural reorganization of the TLR8 dimer by agonists* | Activation mechanism GOF dysregulates (F2) |
| [25599397](https://pubmed.ncbi.nlm.nih.gov/25599397/) | *TLR8 senses degradation products of ssRNA* | TLR8 ligand biology (F2) |
| [21949866](https://pubmed.ncbi.nlm.nih.gov/21949866/) | *Species-specific ligand recognition in TLR8* | Mouse is a poor model (F5) |
| [41159953](https://pubmed.ncbi.nlm.nih.gov/41159953/) | *TIRAP-MyD88 inhibitor blocks TLR7/8 IFN responses* | Human-specific TIRAP-MyD88-IRF5 pathway; species difference (F5) |
| [21606490](https://pubmed.ncbi.nlm.nih.gov/21606490/) | *Human IRAK-2 essential for TLR-mediated TNF regulation* | Human IRAK-2 requirement in TLR8 signaling (F5) |
| [28028829](https://pubmed.ncbi.nlm.nih.gov/28028829/) | *Localization of nucleic-acid-sensing TLRs in human/mouse pancreas* | TLR8 human vs mouse expression difference (F5) |
| [36119097](https://pubmed.ncbi.nlm.nih.gov/36119097/) | *GOF defects in TLR8 — interface disorders* | Framing as BMF/IEI interface disorder; diagnostics/therapeutics |
| [36641351](https://pubmed.ncbi.nlm.nih.gov/36641351/) | *Influence of X chromosome in sex-biased autoimmune diseases* | TLR7/8 Xp locus causal via dosage/GOF (F4 context) |
| [38869500](https://pubmed.ncbi.nlm.nih.gov/38869500/) | *GOF UNC93B1 variants cause SLE/chilblain lupus* | Mechanistically related TLR7/8 hyperactivation; differential dx |
| [27742543](https://pubmed.ncbi.nlm.nih.gov/27742543/) | *TLR7 dual receptor structure* | Comparative structural context for TLR7/8 activation |

Evidence source types: **human clinical** (33512449, 41370196), **in vitro functional/structural** (41729082, 23520111, 25599397, 21606490, 41159953), **comparative/computational** (21949866, 28028829, 36641351). Ontology cross-references (MONDO/OMIM/Orphanet/DOID/GARD/MedGen/UMLS) and constraint metrics (gnomAD) are from curated databases (Findings 6–8).

---

## Limitations and Knowledge Gaps

- **Small n.** The entire evidence base rests on ~16 reported patients across three primary case series; prevalence, incidence, penetrance, and full phenotypic spectrum remain uncertain.
- **Registry-level epidemiology absent.** No cases-per-100,000 estimates; the disease is too new and rare.
- **Mosaicism complicates diagnosis and prevalence estimation** — low-VAF cases are likely under-ascertained by standard testing.
- **No faithful animal model.** Species-specific TLR8 biology means in vivo mechanistic and preclinical therapeutic studies are constrained to human cell/iPSC systems.
- **Variant-level genotype–phenotype correlation** (e.g., whether Phe494 vs Gly572 vs A518T differ in severity or onset) is not yet defined.
- **Non-transplant targeted therapies** (IRAK/JAK/TLR8 inhibitors) are rational but unproven in this disease.
- **Modifier genes, epigenetics, and environmental triggers** are unstudied.

## Proposed Follow-up Experiments / Actions

1. **Establish an international IMD98/TLR8-GOF registry** to define natural history, genotype–phenotype correlations, and true epidemiology, with standardized deep-sequencing (mosaicism-aware) diagnostic protocols.
2. **Systematic functional characterization** of all reported and future *TLR8* variants in a uniform NF-κB reporter + cytokine-secretion + dimer-stability platform (extending the A518T approach) to build an ACMG-grade functional evidence resource.
3. **Preclinical testing of targeted signal-pathway inhibitors** (IRAK1/4 inhibitors, JAK inhibitors, TIRAP-MyD88 or TLR8 antagonists) in patient iPSC-derived myeloid cells as bridge-to-transplant / steroid-sparing candidates.
4. **Develop a humanized TLR8 knock-in mouse** (accounting for human ligand recognition and TIRAP dependence) to model marrow failure/lymphoproliferation in vivo.
5. **Single-cell multi-omics of patient marrow** to map the mutant-clone-driven inflammatory circuit and identify the cell populations mediating myeloid suppression.
6. **Optimize HCT protocols** to reduce the high post-transplant cytopenia and GVHD rates observed in the cohort.
7. **Prospective evaluation of biomarkers** (cytokine signatures, activated-T/LGL burden, VAF dynamics) for diagnosis, prognosis, and treatment-response monitoring.

---

*Report compiled from 9 confirmed findings and 18 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMIDs) or curated databases (ClinVar, gnomAD, EBI OLS4/MONDO).*


## Artifacts

- [OpenScientist final report](Immunodeficiency_98_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_98_With_Autoinflammation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0024777` (3 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 98 with autoinflammation, X-linked**
- `HP:0001903` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Anemia**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0005528` (1 mention) - the report calls it "BMF"; HP calls it **Bone marrow hypocellularity**
- `HP:0002719` (1 mention) - the report calls it "Symptom"; HP calls it **Recurrent infections**
- `HP:0002720` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating IgA concentration**
- `HP:0001890` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Autoimmune hemolytic anemia**