---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:11:33.315905'
end_time: '2026-10-01T20:56:48.910030'
duration_seconds: 2715.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due To MALT1 Deficiency
  mondo_id: MONDO:0014197
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42745540
  relevance_assessed: 14
  on_topic: 12
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014197
    reported_labels:
    - MONDO
    ontology_label: combined immunodeficiency due to MALT1 deficiency
  - term_id: HP:0005365
    reported_labels:
    - Abnormal B cell morphology
    ontology_label: obsolete Severe B lymphocytopenia
  - term_id: HP:0005387
    reported_labels:
    - Reduced antibody responses
    ontology_label: Combined immunodeficiency
  labels_variant: 5
  obsolete_terms:
  - term_id: HP:0005365
    ontology_label: obsolete Severe B lymphocytopenia
    replaced_by: HP:0010976
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_MALT1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_MALT1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To MALT1 Deficiency
- **MONDO ID:** MONDO:0014197 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To MALT1 Deficiency** covering all of the
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

# Combined Immunodeficiency Due to MALT1 Deficiency (IMD12): A Comprehensive Disease Characterization

**Disease:** Combined Immunodeficiency Due to MALT1 Deficiency
**MONDO ID:** MONDO:0014197 | **OMIM:** #615468 (Immunodeficiency-12, IMD12) | **Gene:** *MALT1* (HGNC:6819; OMIM *604860)
**Category:** Mendelian (autosomal recessive inborn error of immunity)

---

## Summary

Combined immunodeficiency due to MALT1 deficiency, also designated **Immunodeficiency-12 (IMD12; OMIM #615468; MONDO:0014197)**, is an ultra-rare autosomal recessive inborn error of immunity caused by biallelic loss-of-function variants in *MALT1*. MALT1 (mucosa-associated lymphoid tissue lymphoma translocation protein 1) is the only human paracaspase and serves as a core subunit of the **CARD11–BCL10–MALT1 (CBM) signalosome**, the molecular hub that couples antigen-receptor engagement on T and B lymphocytes to canonical NF-κB activation. When MALT1 function is lost, the CBM complex can no longer transmit antigen-receptor signals to the threshold required for effective lymphocyte activation, producing a disease that combines features of classical immunodeficiency (recurrent infection, poor antibody responses) with immune dysregulation (eczema, elevated IgE, eosinophilia, autoimmunity) — a duality that stems directly from MALT1's dual role in both effector-lymphocyte activation and regulatory T-cell (Treg) homeostasis.

Clinically, affected infants present in the first weeks to months of life (mean onset ~1.6 months) with recurrent bacterial, viral, and fungal infections (100%), skin involvement/eczema (100%), failure to thrive (100%), oral lesions (67%), chronic diarrhea (56%), and autoimmunity (44%). The characteristic laboratory signature includes eosinophilia (~67%), elevated IgE (~22%), typically normal T and NK cell counts but reduced B cells (89% of patients), arrest of B-cell maturation, and impaired specific antibody responses. The disorder is heavily enriched in consanguineous Middle Eastern, Turkish, and North African populations, consistent with a consanguinity/founder effect rather than a single global founder allele, and fewer than ~20 patients had been comprehensively characterized as of 2022.

The prognosis is poor with conservative management: immunoglobulin replacement and antimicrobial prophylaxis are largely ineffective, and infection-related mortality is high (5 of 9 patients died in the largest cohort). **Allogeneic hematopoietic stem cell transplantation (HSCT)** — which reconstitutes CBM-competent hematopoietic cells — is the only established curative therapy. MALT1 deficiency sits within the broader family of "**CBM-opathies**" (inborn errors of CARD11, BCL10, and MALT1), and its eczema/high-IgE/sinopulmonary-infection phenotype overlaps with DOCK8 deficiency and hyper-IgE syndromes, so molecular confirmation is required for diagnosis.

---

## 1. Disease Information

MALT1 deficiency is an autosomal recessive **combined immunodeficiency (CID)** with early-onset multisystem disease. It is formally classified as **Immunodeficiency-12 with susceptibility to viral, bacterial, and fungal infections (IMD12)**.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0014197 |
| OMIM (phenotype) | #615468 (IMD12) |
| OMIM (gene) | *604860 (*MALT1*) |
| HGNC | HGNC:6819 |
| Orphanet | Classified under combined immunodeficiencies (prevalence <1/1,000,000) |
| Gene locus | 18q21.32 |

**Synonyms / alternative names:** Immunodeficiency-12; IMD12; MALT1 deficiency; MALT1 paracaspase deficiency; combined immunodeficiency due to MALT1 deficiency; CBM-opathy (MALT1 type).

**Information source:** The disease-level characterization derives from aggregated case series and individual case reports in the primary literature (e.g., the 19-patient synthesis in [PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)), supplemented by mechanistic studies in cell lines and model organisms. Given extreme rarity, there are no EHR-scale or registry-scale datasets; all clinical data are individual-patient-derived and then aggregated.

---

## 2. Etiology

**Primary cause — genetic:** The disease is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *MALT1***. In consanguineous families the variants are typically homozygous. There is no environmental or infectious cause of the underlying disorder; infections are the *consequence* of the immune defect, not its cause.

**Genetic risk factors:** The sole causal factor is biallelic *MALT1* LOF. **Consanguinity** is the dominant population-level risk factor, as it dramatically increases the probability of homozygosity for rare recessive alleles. No modifier genes have been formally validated, though the broader severity of CBM-opathies depends on which component and residual protein function is affected.

**Environmental / lifestyle risk factors:** None established as causal. Pathogen exposure determines the pattern and timing of clinical infection but does not cause the immunodeficiency.

**Protective factors:** Heterozygous carriers are asymptomatic (one functional allele suffices). No protective modifier alleles have been described. The only "protective" intervention is definitive immune reconstitution via HSCT.

**Gene–environment interactions:** The genetic lesion sets a lowered threshold for immune failure; environmental pathogen load then determines clinical expression (severity/frequency of infections, triggering of eczema flares). This is a "genotype sets susceptibility, environment determines manifestation" relationship rather than a true molecular GxE interaction.

---

## 3. Phenotypes

Phenotype frequencies are drawn primarily from the largest cohort (9 new + 10 previously reported patients, n=19; [PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)).

| Phenotype | Type | Frequency | Suggested HPO term |
|-----------|------|-----------|--------------------|
| Recurrent infections (bacterial/viral/fungal) | Clinical sign | 100% | HP:0002719 (Recurrent infections) |
| Skin involvement / eczema / dermatitis | Physical manifestation | 100% | HP:0000964 (Eczema) / HP:0000988 (Skin rash) |
| Failure to thrive | Clinical sign | 100% | HP:0001508 (Failure to thrive) |
| Oral lesions (ulcers, candidiasis) | Clinical sign | 67% | HP:0000155 (Oral ulcer) |
| Chronic diarrhea / enteropathy | Symptom | 56% | HP:0002028 (Chronic diarrhea) |
| Autoimmunity | Clinical sign | 44% | HP:0002960 (Autoimmunity) |
| Eosinophilia | Lab abnormality | 67% | HP:0001880 (Eosinophilia) |
| Elevated serum IgE | Lab abnormality | 22% | HP:0003212 (Increased IgE level) |
| Reduced B cells | Lab abnormality | 89% (8/9) | HP:0010976 (B lymphocytopenia) |
| B-cell maturation arrest | Lab abnormality | Reported in cases | HP:0005365 (Abnormal B cell morphology) |
| Impaired specific antibody responses | Lab abnormality | Common | HP:0005387 (Reduced antibody responses) |

The phenotype frequencies come directly from the largest reported cohort ([PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)): *"The main clinical findings of the disease were recurrent infections (100%), skin involvement (100%), failure to thrive (100%), oral lesions (67%), chronic diarrhea (56%), and autoimmunity (44%)."*

**Phenotype characteristics:**
- **Age of onset:** Neonatal / early infancy — mean disease onset **1.6 ± 0.7 months** ([PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)): *"The mean age of patients and disease onset were 33 ± 17 and 1.6 ± 0.7 months, respectively."*
- **Severity:** Severe; life-threatening.
- **Progression:** Progressive without curative treatment; chronic/lifelong course punctuated by acute infectious episodes.
- **Immunophenotype:** *"The majority of patients had normal T and NK cells, while eight (89%) exhibited reduced B cells."* ([PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/))

**Quality of life impact:** Severe. Recurrent infections, chronic diarrhea/enteropathy, failure to thrive, and dermatitis substantially impair growth, nutrition, and daily function in infancy; the burden of hospitalization and the need for HSCT are profound. Formal QoL instrument data (EQ-5D, SF-36) are not available for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene:** *MALT1* (HGNC:6819; chromosome **18q21.32**; OMIM *604860). The gene encodes an **824-amino-acid paracaspase** — the only paracaspase in humans.

**Protein architecture** (relevant to loss-of-function mechanism):
- N-terminal **death domain**
- Two N-terminal **Ig-like (immunoglobulin-like) domains** (Ig1–Ig2; mediate BCL10 binding and oligomerization)
- Central **caspase-like (paracaspase) protease domain**
- C-terminal **Ig-like domain**

Crystallography (1.75 Å) shows the paracaspase domain adopts a fold nearly identical to classic caspases and homodimerizes to form an active protease that cleaves substrates after arginine residues ([PMID: 22158899](https://pubmed.ncbi.nlm.nih.gov/22158899/)): *"The paracaspase domain adopts a fold that is nearly identical to that of classic caspases and homodimerizes similarly to form an active protease."* The tandem Ig-like domains additionally mediate oligomerization important for signaling ([PMID: 21966355](https://pubmed.ncbi.nlm.nih.gov/21966355/)).

**Reported pathogenic variants** (all germline, biallelic, loss-of-function):

| Variant (cDNA / protein) | Domain | Type | Reference |
|--------------------------|--------|------|-----------|
| c.1411G>A; p.D471N | caspase-like | Missense (LOF) | [PMID: 40748513](https://pubmed.ncbi.nlm.nih.gov/40748513/) |
| c.762dup; p.Ile255TyrfsTer10 | N-terminal | Frameshift | [PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/) |
| p.K543R + p.M732T (compound het) | caspase-like / C-terminal | Hypomorphic missense | [PMID: 41882201](https://pubmed.ncbi.nlm.nih.gov/41882201/) |

Supporting quotes:
- *"The patient carried a novel pathogenic biallelic loss-of-function variant in MALT1 (c.1411G > A; p.D471N) located in the caspase-like domain, leading to severely reduced MALT1 protein expression."* ([PMID: 40748513](https://pubmed.ncbi.nlm.nih.gov/40748513/))
- *"Next-generation sequencing revealed a novel homozygous variant in the MALT1 gene (c.762dup in exon 5 of 17; p.Ile255TyrfsTer10); this variant is likely pathogenic, thus supporting the genetic diagnosis of immunodeficiency-12 (IMD12)."* ([PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/))
- *"the MALT1 K543R and M732T variants attenuated MALT1's enzymatic activity and compromised its protein stability"* ([PMID: 41882201](https://pubmed.ncbi.nlm.nih.gov/41882201/))

**Variant classification:** Pathogenic / likely pathogenic per ACMG/AMP, supported by functional assays demonstrating reduced protein and/or reduced protease/scaffold activity.

**Variant types:** Missense, frameshift, and nonsense have all been reported. **Functional consequence = loss of function** (reduced protein stability and/or reduced protease and scaffold activity).

**Allele frequency:** Pathogenic *MALT1* LOF alleles are essentially absent in the homozygous state in gnomAD, consistent with recessive severe disease.

**Somatic vs germline:** Disease-causing variants are **germline**. (Note: *MALT1* is also oncogenically activated in lymphoma via the somatic t(11;18) API2-MALT1 fusion and chronic CBM activation — a distinct, unrelated pathology.)

**Modifier genes / epigenetics / chromosomal abnormalities:** No validated modifier genes, disease-specific epigenetic signatures, or large-scale chromosomal abnormalities are described for the Mendelian deficiency.

---

## 5. Environmental Information

**Environmental factors:** No toxic, radiation, or occupational exposures contribute to this monogenic disease.

**Lifestyle factors:** Not applicable (disease of infancy).

**Infectious agents:** Pathogens are **downstream consequences**, not causes. The combined immunodeficiency predisposes to recurrent bacterial, viral, and fungal infections. Staphylococcal skin/soft-tissue infections and mucocutaneous candidiasis are notable, overlapping with the DOCK8/hyper-IgE differential ([PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/)). Chronic mucocutaneous candidiasis-type and other opportunistic infections reflect the combined T/B defect.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in *MALT1*** (missense/frameshift/nonsense) **lead to** severely reduced MALT1 protein and/or loss of paracaspase protease and scaffold activity.
2. Loss of functional MALT1 **results in** a non-functional or crippled **CARD11–BCL10–MALT1 (CBM) signalosome**, which normally assembles downstream of the T-cell receptor (TCR) and B-cell receptor (BCR).
3. A defective CBM complex **fails to transmit antigen-receptor signals** to the threshold required for **canonical NF-κB activation** (demonstrated by reduced p65/RelA phosphorylation).
4. Impaired NF-κB signaling **branches** into two consequences:
   - **(Branch A — effector/immunodeficiency):** reduced lymphocyte activation, proliferation, and cytokine output (deficient IL-2 and TNF-α), **leading to** impaired T-cell help, arrest of B-cell maturation at the transitional/naïve stage, reduced memory and total B cells, and poor specific antibody responses → **recurrent infections and (functional) agammaglobulinemia**.
   - **(Branch B — regulatory/dysregulation):** loss of MALT1 protease activity **results in** reduced regulatory T-cell (Treg) and follicular regulatory (Tfr) cell numbers and function, plus Th2 skewing, **leading to** autoimmunity, eczema/atopic dermatitis, eosinophilia, and elevated IgE.
5. The combined effector failure plus immune dysregulation **manifests clinically** as early-infancy combined immunodeficiency with infections, enteropathy, failure to thrive, dermatitis, and autoimmunity.

*(The branching in step 4 is directly inferred from the dual scaffold/protease biochemistry of MALT1 and is demonstrated in both patient cells and model organisms; see below.)*

### Molecular and cellular detail

**Molecular pathway (central):** The CBM signalosome bridges ITAM-coupled antigen receptors (TCR/BCR) to **NF-κB**, and also to **JNK** and **mTORC1** ([PMID: 30283440](https://pubmed.ncbi.nlm.nih.gov/30283440/)). MALT1 integrates receptor-derived signals and "*determines whether downstream nuclear factor kappa B (NF-κB) activation reaches thresholds required for effective immune responses*" ([PMID: 42745540](https://pubmed.ncbi.nlm.nih.gov/42745540/)): *"As a central component of the CARD11-BCL10-MALT1 (CBM) signalosome, MALT1 integrates receptor-derived signals and determines whether downstream nuclear factor kappa B (NF-kB) activation reaches thresholds required for effective immune responses."*

**Dual function of MALT1** ([PMID: 37126937](https://pubmed.ncbi.nlm.nih.gov/37126937/)): *"MALT1 acts as a scaffolding protein to drive activation of NF-κB transcription factors and as a protease to modulate signaling and immune activation by cleavage of distinct substrates."*
- **Scaffold function:** nucleates IKK activation → NF-κB.
- **Protease function:** cleaves negative regulators of NF-κB (**A20, CYLD, RelB**) and RNA-binding repressors (**Regnase-1, Roquin**), thereby sustaining lymphocyte proliferation/survival and shaping cytokine mRNA stability.

**Patient-level evidence:** A p.D471N LOF variant *"Impaired CBM-mediated NF-κB activation was confirmed by reduced phosphorylation of the p65 subunit, resulting in deficient production of IL-2 and TNF-α"* and *"This functional defect caused lower Tfr and Treg cells, a normal proportion of Tfh cells, with higher expression of activation markers PD-1 and ICOS"* ([PMID: 40748513](https://pubmed.ncbi.nlm.nih.gov/40748513/)). B-cell maturation arrest with elevated IgE and otherwise normal subset counts has been documented ([PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/)): *"He had elevated serum IgE and normal B- and T-lymphocyte subset counts, but there was an arrest in the B-cell maturation."*

**Treg dependence on MALT1 protease — mechanistic link (model organisms):** MALT1 protease activity in Tregs drives TCR-induced upregulation of **MYC**, supporting mitochondrial function and homeostatic Treg expansion ([PMID: 34668583](https://pubmed.ncbi.nlm.nih.gov/34668583/)): *"MALT1 protease activity controls the TCR-induced upregulation of the transcription factor MYC and the subsequent expression of MYC target genes in Tregs."* Thus the dysregulation branch is tied specifically to protease (not scaffold) function.

**Cell types involved (suggested CL terms):** CD4+ T cell (CL:0000624), CD8+ T cell (CL:0000625), regulatory T cell (CL:0000815), follicular regulatory T cell, B cell (CL:0000236), naïve/transitional B cell, memory B cell (CL:0000787), NK cell (CL:0000623), myeloid dendritic cell.

**Suggested GO terms:** antigen receptor-mediated signaling pathway (GO:0050851), I-κB kinase/NF-κB signaling (GO:0007249), positive regulation of NF-κB transcription factor activity (GO:0051092), T cell receptor signaling pathway (GO:0050852), B cell receptor signaling pathway (GO:0050853), regulatory T cell differentiation (GO:0045066), proteolysis (GO:0006508), cysteine-type endopeptidase activity (GO:0004197).

**Subcellular compartments (GO Cellular Component):** cytoplasm/cytosol (GO:0005829) where the CBM signalosome assembles; the signal terminates in the nucleus (GO:0005634) via NF-κB nuclear translocation.

**Immune system involvement:** Combined (T + B) immunodeficiency plus immune dysregulation (autoimmunity, atopy). This is the defining pathophysiology.

---

## 7. Anatomical Structures Affected

**Organ / system level:**
- **Immune/lymphoreticular system** (UBERON:0002405 immune system; UBERON:0000029 lymph node; UBERON:0002106 spleen; UBERON:0002370 thymus) — primary.
- **Skin** (UBERON:0002097) — eczema/dermatitis, staphylococcal infection.
- **Gastrointestinal tract** (UBERON:0001555 digestive tract) — chronic diarrhea/enteropathy.
- **Oral cavity / mucosa** (UBERON:0000167) — oral lesions, candidiasis.
- **Respiratory tract** (UBERON:0000065) — recurrent sinopulmonary infection.
- Systemic: failure to thrive reflects multi-organ nutritional/growth impact.

**Tissue and cell level:** Lymphoid tissue and peripheral blood leukocytes. Affected cell populations: T cells (including Tregs and Tfr), B cells (maturation arrest at transitional/naïve stage; reduced memory B cells), NK cells (numerically normal but functionally impaired), and myeloid dendritic cells.

**Subcellular level:** Cytoplasmic CBM signalosome assembly (GO:0005829); nuclear NF-κB-driven transcription (GO:0005634).

**Localization / lateralization:** Systemic and bilateral/diffuse (not a focal or lateralized disease).

---

## 8. Temporal Development

- **Onset:** Congenital genetic defect with clinical onset in the **neonatal period / early infancy** (mean 1.6 ± 0.7 months; [PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)). Onset pattern is early and progressive.
- **Progression:** Progressive and life-threatening without immune reconstitution; chronic/lifelong. Clinical course is punctuated by **acute infectious episodes** superimposed on chronic enteropathy, dermatitis, and failure to thrive.
- **Disease course pattern:** Chronic-progressive with episodic infectious exacerbations.
- **Remission:** No spontaneous remission. Durable remission/cure is achieved only through allogeneic HSCT.
- **Critical period / intervention window:** Early infancy — prompt molecular diagnosis and HSCT before irreversible infectious/organ damage is the key window of opportunity.

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive.** Affected individuals are homozygous (consanguineous families) or compound heterozygous for *MALT1* LOF variants; heterozygous carriers are asymptomatic.

**Epidemiology:** Ultra-rare. Only ~19 patients had been comprehensively characterized by 2022 (9 new + 10 previously reported; [PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)): *"We also analyzed ten previously reported patients to comprehensively evaluate genotype/phenotype correlation."* Additional single case reports have appeared since (Egyptian, Chinese patients). Orphanet lists prevalence as **<1/1,000,000**. No validated incidence figures exist.

**Penetrance / expressivity:** Biallelic LOF appears highly penetrant for combined immunodeficiency; expressivity is somewhat variable in the balance of immunodeficiency vs. dysregulation features and in residual B/T function, likely reflecting variant-specific residual activity (hypomorphic vs. null).

**Founder effects / consanguinity:** Reported families are frequently consanguineous with homozygous variants, heavily weighted toward **Middle Eastern/Turkish and North African** populations — consistent with a consanguinity/founder effect rather than a single global founder allele ([PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/): *"Next-generation sequencing revealed a novel homozygous variant in the MALT1 gene"*).

**Carrier frequency:** Not formally established; pathogenic LOF alleles are essentially absent in the homozygous state in gnomAD.

**Sex ratio / age distribution:** Both sexes affected (autosomal). Affected individuals are infants/young children.

---

## 10. Diagnostics

**Clinical / laboratory tests:**
- **Immunophenotyping (flow cytometry):** typically normal T and NK cell counts; **reduced B cells (89%)**; reduced memory B cells; arrest of B-cell maturation; reduced Treg/Tfr; elevated activation markers (PD-1, ICOS).
- **Immunoglobulins:** impaired specific antibody responses; may trend toward hypogammaglobulinemia/agammaglobulinemia; **elevated IgE** in a subset (~22%).
- **CBC:** **eosinophilia (~67%)**.
- **Functional assays:** reduced lymphocyte proliferation to anti-CD3; reduced NF-κB activation (↓phospho-p65) on PMA/ionomycin or receptor stimulation; deficient IL-2/TNF-α production. These functional readouts are central to confirming pathogenicity.

**Genetic testing (definitive):** Molecular confirmation is required because the clinical picture overlaps with other CBM-opathies, DOCK8 deficiency, and hyper-IgE syndromes.
- **Whole-exome / whole-genome sequencing (WES/WGS)** is the preferred first-line approach, especially given phenotypic overlap; upfront genomic sequencing shortens time to diagnosis in primary atopic disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).
- **Targeted inborn-errors-of-immunity (IEI)/SCID/CID gene panels** including *MALT1*, *CARD11*, *BCL10*, *CARD9*, *DOCK8*.
- **Single-gene *MALT1* sequencing** confirmed by Sanger; functional validation of variant impact strengthens classification.

**Clinical criteria / differential diagnosis:** No disease-specific consensus criteria exist; diagnosis rests on the combined immunodeficiency phenotype plus biallelic *MALT1* LOF with functional corroboration. **Differential diagnoses** to exclude: DOCK8 deficiency, hyper-IgE syndromes, other SCID/CID, BCL10 and CARD11 deficiencies (other CBM-opathies), IPEX, Omenn syndrome, and Wiskott-Aldrich syndrome. *"Although the presence of eczema, recurrent sinopulmonary, and staphylococcal infections are suggestive of DOCK8 deficiency, they are also a finding in CARD11 and MALT1 deficiency."* ([PMID: 39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/)). BCL10 deficiency shares an overlapping immunophenotype ([PMID: 34868072](https://pubmed.ncbi.nlm.nih.gov/34868072/): *"this patient displays a reduction in NK, γδT, Tregs, and T"*).

**Screening:** No population newborn screening specifically detects MALT1 deficiency; notably, SCID TREC-based newborn screening may be normal because T-cell numbers are often preserved — an important caveat. **Cascade/carrier testing** in affected consanguineous families is valuable.

---

## 11. Outcome / Prognosis

**Survival / mortality:** Poor without curative therapy. In the largest cohort, *"Immunoglobulin replacement and antibiotics prophylaxis were mostly ineffective in reducing the frequency of infections and other complications. One patient received hematopoietic stem cell transplantation (HSCT) and five patients died as a complication of life-threatening infections."* ([PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)). The p.D471N patient experienced early death ([PMID: 40748513](https://pubmed.ncbi.nlm.nih.gov/40748513/)).

**Morbidity:** High — recurrent severe infections, chronic enteropathy, failure to thrive, dermatitis, and autoimmune complications.

**Disease-specific complications:** Life-threatening bacterial/viral/fungal infections (leading cause of death), enteropathy with malnutrition, autoimmune manifestations.

**Recovery potential:** Minimal with supportive care alone; curative potential exists with successful allogeneic HSCT (reconstitutes CBM-competent hematopoietic cells).

**Prognostic factors:** Timing of diagnosis and access to HSCT; infection burden and organ damage at presentation; likely residual MALT1 function (hypomorphic vs. null variant).

---

## 12. Treatment

**Supportive / pharmacotherapy (largely palliative):**
- **Immunoglobulin replacement (IVIG/SCIG)** — NCIT: Intravenous Immunoglobulin Therapy. Largely ineffective at preventing infections in this disease.
- **Antimicrobial / antifungal / antiviral prophylaxis.** Mostly ineffective at reducing complications.
- **Management of enteropathy and dermatitis** — nutritional support, topical/skin care.

Supporting evidence: *"Immunoglobulin replacement and antibiotics prophylaxis were mostly ineffective in reducing the frequency of infections and other complications."* ([PMID: 35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/)).

**Curative / advanced therapeutics:**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — NCIT: Allogeneic Hematopoietic Stem Cell Transplantation (C15431). The **only established curative therapy**; reconstitutes CBM-competent lymphocytes. Reported in only a minority of patients to date; early transplantation before severe infectious damage is the goal.
- **Gene therapy / gene editing:** Not yet available; conceptually attractive given the monogenic, hematopoietic-restricted nature of the defect — a plausible future direction but no clinical programs reported.

**Pharmacologic caution — MALT1 inhibitors:** MALT1 protease *inhibitors* are in development for lymphoma and autoimmune disease. Importantly, pharmacological MALT1 inhibition reproduces an **IPEX-like, Treg-depleting autoimmune pathology** in animal models ([PMID: 32425939](https://pubmed.ncbi.nlm.nih.gov/32425939/)): *"pharmacological inhibition of MALT1 was associated with a rapid and dose-dependent reduction in Tregs and resulted in the progressive appearance of immune abnormalities and clinical signs of an IPEX-like pathology."* This underscores that *reducing* MALT1 function is deleterious — relevant both to understanding the patient phenotype and to avoiding iatrogenic harm.

**Treatment outcomes / strategy:** No formal treatment algorithms exist for this ultra-rare disease; management mirrors severe combined/combined immunodeficiency protocols (prophylaxis + definitive HSCT). Genotype-guided prognostication (null vs. hypomorphic) may refine urgency.

---

## 13. Prevention

- **Primary prevention:** Not possible for the monogenic disease itself. **Genetic counseling** for consanguineous families and carrier couples is the principal preventive measure; **preimplantation genetic diagnosis (PGD)** and **prenatal testing** are options when the familial variant is known.
- **Secondary prevention:** Early molecular diagnosis enables timely HSCT before irreversible infectious/organ damage. **Cascade screening** of at-risk relatives in affected families.
- **Tertiary prevention:** Infection prophylaxis, nutritional support, and vigilant management of autoimmune/atopic complications pending definitive therapy.
- **Immunization caveat:** As in other combined immunodeficiencies, **live vaccines are contraindicated**; vaccine responses are typically poor.
- **Public health:** Awareness of consanguinity-associated recessive IEI and incorporation of *MALT1* into IEI gene panels improve detection.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs:** *MALT1* is evolutionarily conserved in mammals. Mouse *Malt1* (NCBI Gene) is the principal ortholog used in disease modeling.

**Natural disease in animals:** No naturally occurring MALT1-deficiency disease is established in companion animals or wildlife (no prominent OMIA entry). However, **pharmacological MALT1 protease inhibition in rats and dogs** produces a progressive **IPEX-like pathology** with severe Treg reduction ([PMID: 32425939](https://pubmed.ncbi.nlm.nih.gov/32425939/)), demonstrating cross-species conservation of the Treg-dependent dysregulation mechanism.

**Comparative biology:** The scaffold/protease duality and CBM–NF-κB axis are conserved across mammals, making mouse models highly informative. **Zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse models** are the principal system and recapitulate the immunodeficiency–dysregulation duality:

| Model | Key phenotype | Reference |
|-------|---------------|-----------|
| *Malt1* knockout (complete) | Atopic-like dermatitis upon aging; Th2 skewing; ↑serum IgE; ↓Treg frequency and CTLA-4 | [PMID: 31632405](https://pubmed.ncbi.nlm.nih.gov/31632405/) |
| Protease-dead (catalytically inactive, scaffold-retaining) MALT1 knock-in | Spontaneous autoimmunity from Treg loss and increased effector T-cell activation | [PMID: 34668583](https://pubmed.ncbi.nlm.nih.gov/34668583/) |
| Treg-specific *Myc* deletion | Phenocopies lethal autoimmune syndrome (links MALT1 protease → MYC → Treg expansion) | [PMID: 34668583](https://pubmed.ncbi.nlm.nih.gov/34668583/) |
| Pharmacological MALT1 inhibition (rat/dog) | Progressive IPEX-like pathology, severe Treg reduction | [PMID: 32425939](https://pubmed.ncbi.nlm.nih.gov/32425939/) |

Supporting quotes:
- *"here we report that MALT1-deficient mice develop atopic-like dermatitis upon aging, which is preceded by Th2 skewing, an increase in serum IgE, and a decrease in Treg frequency and surface expression of the Treg functionality marker CTLA-4."* ([PMID: 31632405](https://pubmed.ncbi.nlm.nih.gov/31632405/))
- *"MALT1 protease activity controls the TCR-induced upregulation of the transcription factor MYC and the subsequent expression of MYC target genes in Tregs"* ([PMID: 34668583](https://pubmed.ncbi.nlm.nih.gov/34668583/))

**Phenotype recapitulation:** Strong for the atopy/Th2/IgE/Treg-loss axis (dysregulation branch). **Limitations:** Complete-knockout mice emphasize dysregulation/atopy; the severe early-infancy infectious mortality seen in humans is less fully modeled, and the separation of scaffold vs. protease contributions (via protease-dead knock-ins) does not perfectly mirror human null/hypomorphic variants. **Model databases:** MGI, IMPC, IMSR.

---

## Mechanistic Model (Synthesis)

```
   Biallelic LOF MALT1 variants (missense / frameshift / nonsense)
                         │  (↓ protein, ↓ protease + scaffold)
                         ▼
        Non-functional CARD11–BCL10–MALT1 (CBM) signalosome
                         │  downstream of TCR / BCR
                         ▼
     Antigen-receptor signal fails to reach NF-κB activation threshold
                 (↓ phospho-p65; also ↓ JNK, ↓ mTORC1)
                         │
         ┌───────────────┴────────────────┐
         ▼                                 ▼
  BRANCH A: EFFECTOR FAILURE         BRANCH B: REGULATORY FAILURE
  (loss of scaffold + protease)      (loss of protease → ↓MYC in Tregs)
  • ↓ IL-2, ↓ TNF-α                   • ↓ Treg / ↓ Tfr
  • B-cell maturation arrest          • Th2 skewing
  • ↓ memory & total B cells          • ↑ IgE, eosinophilia
  • poor antibody responses           • ↑ PD-1 / ICOS activation
         │                                 │
         ▼                                 ▼
  Recurrent infections,              Eczema/dermatitis,
  functional agammaglobulinemia      autoimmunity
         └───────────────┬────────────────┘
                         ▼
   Early-infancy COMBINED IMMUNODEFICIENCY + IMMUNE DYSREGULATION
   (infections, enteropathy, failure to thrive, oral lesions)
                         │
                         ▼
          Poor prognosis → curative only by allogeneic HSCT
```

The key unifying insight is that **MALT1's two biochemical activities map onto the two clinical faces of the disease**: scaffold-driven NF-κB loss drives effector/immunodeficiency features, while protease loss (via the MYC–mitochondrial axis in Tregs) drives the regulatory/dysregulation features. This is corroborated in patients (↓NF-κB, ↓IL-2/TNF-α, ↓Treg/Tfr) and in model organisms (protease-dead knock-ins → Treg-dependent autoimmunity; pharmacologic inhibition → IPEX-like pathology).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [35079916](https://pubmed.ncbi.nlm.nih.gov/35079916/) | *Expanding the Clinical and Immunological Phenotypes and Natural History of MALT1 Deficiency* | Largest cohort (n=19); phenotype frequencies, onset age, immunophenotype, poor outcome/HSCT |
| [40748513](https://pubmed.ncbi.nlm.nih.gov/40748513/) | *Loss of MALT1 Function in a Patient With CID* | p.D471N LOF variant; impaired NF-κB (↓p-p65), ↓IL-2/TNF-α, ↓Treg/Tfr |
| [42745540](https://pubmed.ncbi.nlm.nih.gov/42745540/) | *What Human MALT1 Deficiency Reveals About Immune Control* | CBM/NF-κB threshold signaling framework |
| [39017781](https://pubmed.ncbi.nlm.nih.gov/39017781/) | *A novel MALT1 variant (Egyptian patient)* | Frameshift p.Ile255TyrfsTer10; IMD12 designation; B-cell maturation arrest; DOCK8 differential |
| [41882201](https://pubmed.ncbi.nlm.nih.gov/41882201/) | *Novel heterozygous variants in CARD11 and MALT1* | Hypomorphic p.K543R/p.M732T reduce enzymatic activity and stability |
| [22158899](https://pubmed.ncbi.nlm.nih.gov/22158899/) | *Crystal structure of MALT1 paracaspase region* | Caspase-like fold, homodimerization, protease activity |
| [21966355](https://pubmed.ncbi.nlm.nih.gov/21966355/) | *Oligomeric structure of MALT1 tandem Ig-like domains* | Ig-domain oligomerization in signaling |
| [37126937](https://pubmed.ncbi.nlm.nih.gov/37126937/) | *Function and targeting of MALT1 paracaspase* | Dual scaffold/protease function; substrate cleavage (A20, CYLD, RelB, Regnase-1, Roquin) |
| [31632405](https://pubmed.ncbi.nlm.nih.gov/31632405/) | *MALT1-Deficient Mice Develop Atopic-Like Dermatitis* | KO mouse: atopy, Th2, ↑IgE, ↓Treg/CTLA-4 |
| [34668583](https://pubmed.ncbi.nlm.nih.gov/34668583/) | *MALT1 protease → MYC in Tregs* | Protease–MYC–mitochondrial axis for Treg expansion |
| [32425939](https://pubmed.ncbi.nlm.nih.gov/32425939/) | *Pharmacological MALT1 Inhibition → IPEX-Like Pathology* | Protease-specific loss → Treg-dependent autoimmunity (rat/dog) |
| [30283440](https://pubmed.ncbi.nlm.nih.gov/30283440/) | *The CBM-opathies* | Classification/spectrum of CARD11-BCL10-MALT1 inborn errors |
| [34868072](https://pubmed.ncbi.nlm.nih.gov/34868072/) | *Human BCL10 Deficiency* | Overlapping immunophenotype (↓NK, γδT, Treg, T) in the differential |

**Evidence source types:** Human clinical (cohorts/case reports: 35079916, 40748513, 39017781, 41882201, 34868072); in vitro/structural (22158899, 21966355, 37126937); model organism (31632405, 34668583, 32425939).

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (n≈19 + scattered case reports).** All epidemiology is case-derived; no validated prevalence/incidence, penetrance, or expressivity estimates. Phenotype frequencies may be biased by ascertainment toward severe/consanguineous cases.
2. **Genotype–phenotype correlation is incompletely resolved.** The spectrum of variant types (null vs. hypomorphic) and how residual activity modulates the immunodeficiency-vs-dysregulation balance remain under-characterized.
3. **HSCT outcome data are sparse** — only a minority of reported patients were transplanted; optimal conditioning, timing, and long-term outcomes are not established.
4. **Human mechanistic data are limited to a few patients;** much of the protease-vs-scaffold dissection relies on model organisms and pharmacology, which may not perfectly mirror human null/hypomorphic variants.
5. **No disease-specific QoL, biomarker-based prognostic, or newborn-screening data.** Standard SCID TREC screening may miss MALT1 deficiency because T-cell numbers are often preserved.
6. **No gene therapy** programs or formal treatment algorithms exist.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international MALT1-deficiency patient registry** to aggregate genotype, immunophenotype, treatment, and HSCT outcome data and derive robust natural-history and genotype–phenotype correlations.
2. **Systematic functional classification of *MALT1* variants** (NF-κB reporter, protease-cleavage, protein-stability assays) to build an ACMG-aligned variant interpretation resource distinguishing null vs. hypomorphic alleles.
3. **Define HSCT best practices** (timing, conditioning, donor source) through multicenter outcome analysis, and evaluate whether early transplantation (before severe infection) improves survival.
4. **Single-cell transcriptomic/immune profiling of patient PBMCs** to map, at cell-type resolution, the effector vs. regulatory lesions (B-cell maturation block, Treg/Tfr deficits) and identify candidate biomarkers.
5. **Preclinical evaluation of gene correction** (lentiviral *MALT1* addition or base/prime editing in patient HSPCs) given the monogenic, hematopoietic-restricted nature of the defect.
6. **Incorporate *MALT1* into standard IEI/SCID gene panels** and raise clinician awareness of the DOCK8/hyper-IgE phenotypic overlap and the SCID-screening blind spot (preserved T cells).

---

*Report compiled from autonomous multi-iteration literature synthesis (8 confirmed findings, 25 papers reviewed). All clinical and mechanistic claims are attributed to the cited primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_MALT1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_MALT1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:42745540`: "*determines whether downstream nuclear factor kappa B (NF-κB) activation reaches thresholds required for effective immune responses*"
  - closest text in source: "As a central component of the CARD11-BCL10-MALT1 (CBM) signalosome, MALT1 integrates receptor-derived signals and determines whether downstream nuclear factor kappa B (NF-kB) activation reaches thresholds required for effective immune responses"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014197` (3 mentions) - the report calls it "MONDO"; MONDO calls it **combined immunodeficiency due to MALT1 deficiency**
- `HP:0005365` (1 mention) - the report calls it "Abnormal B cell morphology"; HP calls it **obsolete Severe B lymphocytopenia**
- `HP:0005387` (1 mention) - the report calls it "Reduced antibody responses"; HP calls it **Combined immunodeficiency**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005365` (obsolete Severe B lymphocytopenia) (1 mention) - replaced by `HP:0010976`
- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001880` (1 mention) - the report calls it "Eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `HP:0003212` (1 mention) - the report calls it "Increased IgE level"; HP calls it **Increased circulating IgE concentration**, and lists "Increased circulating IgE level" among its other names
- `HP:0010976` (1 mention) - the report calls it "B lymphocytopenia"; HP calls it **Decreased total B cell count**, and lists "B lymphocytopenia" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0000167` (1 mention) - the report calls it "Oral cavity / mucosa"; UBERON calls it **oral cavity**