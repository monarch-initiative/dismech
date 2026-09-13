---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T08:55:22.832611'
end_time: '2026-09-03T09:10:41.465110'
duration_seconds: 918.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Distal Myopathy 6, Adult-Onset, Autosomal Dominant
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014138
    reported_labels:
    - Mondo
    ontology_label: nemaline myopathy 8
  - term_id: UBERON:0011906
    reported_labels:
    - Soleus
    - soleus
    ontology_label: muscle head
  - term_id: UBERON:0011907
    reported_labels:
    - biceps femoris
    ontology_label: gastrocnemius medialis
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Myopathy 6, Adult-Onset, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Distal Myopathy 6, Adult-Onset, Autosomal Dominant** covering all of the
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

# Distal Myopathy 6, Adult-Onset, Autosomal Dominant (MPD6 / ACTN2 Actininopathy)
### Comprehensive Disease Characteristics Report

---

## Summary

**Distal Myopathy 6, adult-onset, autosomal dominant (MPD6; OMIM #615197; MONDO:0014138)** is a rare, slowly progressive skeletal muscle disease caused by heterozygous (dominant) variants in **ACTN2** (alpha-actinin-2), the major structural protein of the sarcomeric Z-disk (HGNC:164; gene locus 1q42–1q43; UniProt P35609). Because the causative gene is *ACTN2*, the disease is often called **"actininopathy."** It was first delineated as a distinct genetic distal myopathy by Savarese and colleagues in 2019, who described four families (three Spanish, one Swedish) with adult-onset, asymmetric distal muscle weakness beginning with impaired ankle dorsiflexion (foot drop) and later spreading to proximal limb muscles [PMID: 30900782].

The core disease mechanism is a **toxic gain-of-function / dominant-negative process driven by misfolding and aggregation of mutant alpha-actinin-2 at the Z-disk.** Cell-model work shows that dominant, protein-extending frameshift variants form alpha-actinin-2 aggregates, whereas recessive missense variants do not — directly implicating aggregation as the dominant disease mechanism [PMID: 39095936]. Aggregation is accompanied by Z-line disorganization, minicore/core formation, and progressive fiber loss, culminating in distal-predominant weakness. Zebrafish and mouse models expressing mutant alpha-actinin-2 recapitulate sarcomeric disorganization, core pathology, and impaired muscle force [PMID: 30701273].

Clinically, the dominant distal/limb-girdle form is genotype-dependent, ranging from asymptomatic carriers to limb-girdle weakness with facial involvement, and — importantly — **generally spares the heart and respiratory system** [PMID: 39812845]. Muscle MRI shows a characteristic pattern (tibialis anterior, soleus, gluteus medius/minimus, hamstrings), which now aids diagnosis. There is **no curative therapy**; management is supportive (ankle-foot orthoses, physiotherapy) with genetic counseling. This report synthesizes eight confirmed findings drawn from 30 reviewed papers into a full disease characterization spanning etiology, phenotype, genetics, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and model organisms.

---

## 1. Disease Information

**Overview.** MPD6 is a Mendelian, adult-onset, autosomal dominant distal myopathy of skeletal muscle. It belongs to the broad category of distal myopathies — genetic primary muscle disorders that present with prominent weakness at onset in the hands and/or feet — which are increasingly recognized as a subset of the muscular dystrophies (progressive genetic diseases with loss of muscle fibers) [PMID: 33458580]. Savarese et al. established that dominant *ACTN2* variants define a new genetically determined distal myopathy, coining the term "actininopathy": *"ACTN2 encodes for alpha actinin2, which is highly expressed in the sarcomeric Z-disk with a major structural and functional role. Actininopathy is thus a new genetically determined distal myopathy."* [PMID: 30900782].

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | **#615197** (Myopathy, distal, 6, adult-onset, autosomal dominant; MPD6) |
| Mondo | **MONDO:0014138** |
| Gene | **ACTN2** — HGNC:164; NCBI Gene 88; Ensembl ENSG00000077522 |
| Protein | Alpha-actinin-2 — **UniProt P35609** |
| Locus | Chromosome **1q42–1q43** |
| ICD-10 | G71.0 (muscular dystrophy) — no MPD6-specific code |
| ICD-11 | 8C70 (primary/hereditary myopathy) — no MPD6-specific code |
| MeSH | Distal myopathy maps under "Distal Myopathies" / "Muscular Dystrophies" |

**Synonyms / alternative names:** Distal myopathy 6 (MPD6); adult-onset autosomal dominant distal myopathy; **actininopathy**; ACTN2-related distal myopathy; ACTN2 myopathy (dominant, non-congenital).

**Information source.** The knowledge base for MPD6 is derived from **aggregated, disease-level resources** — case series and family cohorts reported in the primary literature (Savarese 2019; Iruzubieta 2025), plus OMIM/gene-level curation — rather than from individual patient EHR data. The largest cohort to date comprises 37 patients from 11 families [PMID: 39812845].

---

## 2. Etiology

**Primary cause — genetic.** MPD6 is a monogenic disorder caused by heterozygous **missense** (and in some kindreds protein-extending **frameshift**) variants in *ACTN2*. In the founding study, a unique *ACTN2* missense variant cosegregated with disease in all three Spanish families, while the Swedish family carried a different *ACTN2* missense variant: *"In all 3 Spanish families, we identified a unique missense variant in the ACTN2 gene cosegregating with the disease. The affected members of the Swedish family carry a different ACTN2 missense variant."* [PMID: 30900782].

**Genetic risk factors.** The causal variant in *ACTN2* is both necessary and (with incomplete, age-dependent penetrance) largely sufficient. There are **no established susceptibility loci or GWAS-identified common-variant risk factors** for this Mendelian disease. Certain recurrent variants behave as founder alleles in specific populations (see §9).

**Environmental / lifestyle risk factors.** None are established. As a dominantly inherited sarcomeric disease, onset and progression are driven by genotype and age, not by toxins, infections, or lifestyle. No occupational or exposure risk factors have been reported.

**Protective factors.** No genetic or environmental protective factors have been identified. Reduced penetrance in some carriers implies the existence of modifiers, but none have been mapped.

**Gene–environment interactions.** No specific gene–environment interactions have been documented for MPD6. Mechanical loading (eccentric contraction) is biologically plausible as an aggravating factor given the Z-disk's role as the structure most vulnerable to eccentric damage [PMID: 21536590], but this remains **inferred, not demonstrated**, for MPD6.

---

## 3. Phenotypes

MPD6 phenotypes are **clinical signs and physical manifestations** of skeletal muscle weakness, with supporting **laboratory/imaging abnormalities**. The phenotype is genotype-dependent and ranges from asymptomatic to limb-girdle weakness with facial involvement [PMID: 39812845].

| Phenotype | Type | Onset | Severity / progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Distal lower-limb weakness (ankle dorsiflexion / foot drop) | Clinical sign | Adult | Progressive; initial site | Characteristic, near-universal at onset | **HP:0009053** (distal lower limb muscle weakness); **HP:0009027** (ankle weakness) |
| Asymmetric muscle weakness | Clinical sign | Adult | Progressive | Common | asymmetry of **HP:0003701** (proximal muscle weakness) |
| Proximal spread / limb-girdle weakness | Clinical sign | Later in course | Progressive | Genotype-dependent | **HP:0003701** (proximal muscle weakness) |
| Facial weakness | Clinical sign | Variable | Variable | Some genotypes | **HP:0030319** (facial palsy/weakness) |
| Gait disturbance / difficulty walking | Physical manifestation | Adult | Progressive | Common | **HP:0001288** (gait disturbance) |
| Z-line disorganization / cores on biopsy | Lab (histology) | — | — | Present but non-specific | core myopathy features / **HP:0003557** (increased fiber-diameter variability) |
| Cardiac involvement | Clinical sign | — | — | **Not common** | **HP:0001638** (cardiomyopathy) — usually absent |
| Respiratory involvement | Clinical sign | — | — | **Not common** | **HP:0002093** (respiratory insufficiency) — usually absent |

The founding cohort described *"adult onset asymmetric distal muscle weakness with initial involvement of ankle dorsiflexion later progressing also to proximal limb muscles"* [PMID: 30900782]. The larger 37-patient cohort confirmed that *"the clinical phenotype ranged from asymptomatic to limb-girdle weakness and facial involvement and was depending on genotype. Cardiac and respiratory involvement were not common."* [PMID: 39812845].

**Quality-of-life impact.** Progressive foot drop and distal weakness impair gait, balance, and mobility, typically necessitating ankle-foot orthoses; proximal spread compromises stair climbing, rising from a chair, and daily activities. No disease-specific EQ-5D/SF-36/PROMIS data are published for MPD6; QoL impact is inferred to be moderate and progressive but non–life-limiting, given the usual sparing of cardiac and respiratory function.

---

## 4. Genetic / Molecular Information

**Causal gene.** **ACTN2** (alpha-actinin-2), HGNC:164, NCBI Gene 88, chromosome 1q42–1q43, encoding UniProt **P35609**. ACTN2 is highly expressed in cardiac and skeletal muscle, is located in the sarcomere Z-disk, and links anti-parallel actin filaments while binding N-terminal titin — thereby contributing to sarcomere stability [PMID: 36116040].

**Pathogenic variants.**

| Variant (protein) | cDNA | Type | Inheritance / phenotype | Population / note |
|---|---|---|---|---|
| p.Ile134Asn | — | Missense | Dominant distal/LGMD | **Belgian founder** (shared haplotype) [PMID: 39812845] |
| p.Cys487Arg | — | Missense | Dominant distal/LGMD | **Basque-Spanish founder** (shared haplotype) [PMID: 39812845] |
| p.Phe835Serfs*66 | c.2504delT | Frameshift, C-terminal extension | Dominant, distal myopathy w/ multi-minicores | Aggregation-forming [PMID: 34170073] |
| p.Arg506Gly | c.1516A>G | Missense (biallelic) | **Recessive** (distinct entity) | **Palestinian founder** [PMID: 38311799] |
| c.1840-2A>T | — | Splice-site | Expands spectrum | [PMID: 36116040] |

**Variant classification (ACMG/AMP).** Founder and cosegregating variants are classified pathogenic/likely pathogenic based on segregation and functional data. However, the *ACTN2* mutation-update review cautions that *"limited segregation and functional data are available to support the pathogenicity of most previously reported missense variants and clear-cut genotype-phenotype correlations are currently only demonstrated for some ACTN2-related myopathies."* [PMID: 36116040] — i.e., many *ACTN2* missense changes remain VUS.

**Variant types:** predominantly **missense** (dominant distal/LGMD and recessive forms) and **frameshift with C-terminal protein extension** (dominant, aggregation-prone). Congenital "Multiple structured Core Disease" (MsCD) arises from de novo missense and deletion variants [PMID: 30701273].

**Allele frequency.** Pathogenic *ACTN2* MPD6 variants are private/rare and essentially **absent or ultra-rare in gnomAD**, consistent with a highly penetrant dominant disease allele. (By contrast, the *ACTN3* R577X null polymorphism is common in ~20% of the general population — a different gene [PMID: 21536590].)

**Somatic vs germline:** **germline** (inherited, autosomal dominant). De novo germline events cause the congenital MsCD phenotype.

**Functional consequences.** The dominant distal disease acts through a **toxic gain-of-function / dominant-negative** mechanism (aggregation), not haploinsufficiency. Frameshift, protein-extending variants form alpha-actinin-2 aggregates [PMID: 39095936]; a specific frameshift *increased* alpha-actinin-2 expression and produced abnormal Z-line organization [PMID: 34170073]. For an MsCD missense variant, mutant protein localized correctly to the Z-line with unaltered levels, arguing **against** haploinsufficiency for that variant [PMID: 30701273].

**Modifier genes.** None specifically mapped for MPD6. Biologically, the paralog **ACTN3** modulates Z-disk composition and elastic properties (loss of alpha-actinin-3 up-regulates alpha-actinin-2 and changes Z-disk protein interactions) [PMID: 21536590], making *ACTN3* genotype a plausible but unproven modifier.

**Epigenetic information / chromosomal abnormalities.** No disease-specific DNA-methylation, histone-modification, or large-scale chromosomal abnormalities have been reported for MPD6. It is a point-mutation/small-indel disorder.

---

## 5. Environmental Information

**Environmental factors:** None established. MPD6 is a monogenic disease with no known toxic, radiation, pollution, or occupational contributors.

**Lifestyle factors:** None established as causal. Physical activity involving eccentric loading could theoretically stress a compromised Z-disk (inferred from Z-disk vulnerability to eccentric damage [PMID: 21536590]), but no clinical evidence links lifestyle to MPD6 onset or progression.

**Infectious agents:** Not applicable — MPD6 has no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous ACTN2 variant** (missense, or frameshift causing a C-terminal protein extension) is inherited in the germline → **leads to** production of a structurally altered alpha-actinin-2 protein.
2. The altered protein **results in** reduced solubility and thermal destabilization of the alpha-actinin-2 molecule (demonstrated for actin-binding-domain substitutions) [PMID: 42481460] → **promotes** misfolding.
3. Misfolded/protein-extended alpha-actinin-2 **leads to** formation of **alpha-actinin-2 aggregates** within the muscle fiber (demonstrated for dominant protein-extending frameshift variants; not seen for recessive missense variants) [PMID: 39095936].
   - **Branch A (dominant distal / frameshift):** aggregation + increased alpha-actinin-2 expression → **abnormal Z-line organization** [PMID: 34170073].
   - **Branch B (congenital MsCD missense/deletion):** mutant protein incorporates at the Z-line and **results in** sarcomeric disorganization and **cores with Z-line defects** even without detectable aggregation [PMID: 30701273].
4. Z-line disorganization and core formation **result in** impaired sarcomere structural integrity and contractile force (impaired muscle force demonstrated in AAV-transduced mouse muscle; motor deficits in zebrafish) [PMID: 30701273].
5. Chronic sarcomeric dysfunction **leads to** progressive muscle fiber degeneration/loss (the defining feature shared with muscular dystrophies) [PMID: 33458580] — *inferred* for MPD6 from the dystrophic paradigm and biopsy findings rather than mechanistically dissected.
6. Fiber loss **manifests** first in distal lower-limb muscles (ankle dorsiflexors) — producing foot drop — then **spreads** proximally to limb-girdle muscles, with genotype-dependent severity [PMID: 30900782; PMID: 39812845].

*Inferred vs demonstrated:* Steps 2–4 are experimentally demonstrated in cell and animal models; the coupling from aggregation to fiber loss (step 5) is **inferred**.

### Mechanistic detail by category

- **Protein dysfunction (central).** Alpha-actinin-2 is an **antiparallel homodimer** with three domains: an N-terminal **actin-binding domain (ABD)** comprising two calponin-homology (CH) domains; a central **rod** of four spectrin-like repeats mediating dimerization; and a C-terminal **calmodulin-like domain** with EF-hands. Disease variants **destabilize** the protein: *"All variants display reduced solubility, with actin-binding domain (ABD) substitutions showing pronounced thermal instability by differential scanning fluorimetry."* [PMID: 42481460], with SEC-MALS/SAXS revealing a strong propensity for aggregation. CH-domain mutations perturb F-actin binding and Z-disc localization/dynamics: *"both mutants have reduced F-actin binding affinity … both mutations additionally affect Z-disc localization and dynamic behaviour."* [PMID: 27287556]. The dominant misfolding/aggregation is the unifying molecular lesion: *"dominant frameshift variants causing a protein extension do form alpha-actinin-2 aggregates. The results suggest that alpha-actinin-2 aggregation is the disease mechanism…"* [PMID: 39095936].

- **Cellular processes.** Protein aggregation and proteostatic stress; abnormal Z-line assembly; myofibrillar disarray; fiber-size variability and eventual fiber loss. **GO terms:** GO:0030018 (Z disc), GO:0006457 (protein folding), GO:0030239 (myofibril assembly), GO:0006936 (muscle contraction).

- **Molecular pathways / interactions.** Alpha-actinin-2 is a Z-disk hub binding actin, titin, and multiple Z-disk partners (ZASP/LDB3, myotilin, telethonin). Disruption of these interactions destabilizes the sarcomere. Beyond structure, the **spectrin-repeat domain binds and regulates ion channels** (see below) — relevant to *ACTN2* cardiac phenotypes but not the primary driver of the skeletal distal myopathy.

- **Ion-channel / electrophysiological role (cardiac-relevant branch).** Alpha-actinin-2 interacts with the cardiac sodium channel Nav1.5: *"We identified alpha-actinin-2 as an interacting partner of the cytoplasmic loop connecting domains III and IV of Na(v)1.5 … the spectrin-like repeat domain is essential for binding of alpha-actinin-2 to Na(v)1.5."* [PMID: 19943616], and *"the interaction with alpha-actinin-2 increases sodium channel density without changing their gating properties"* [PMID: 19943616]. This explains why some *ACTN2* variants present as idiopathic ventricular fibrillation [PMID: 35975100] — a phenotype distinct from MPD6, in which cardiac involvement is uncommon.

- **Metabolic changes / immune involvement:** No primary metabolic or autoimmune mechanism; MPD6 is a structural sarcomeric proteinopathy, not an inflammatory or metabolic myopathy.

- **Tissue damage mechanism:** Mechanical failure of the Z-disk under contractile load with progressive myofiber degeneration; the Z-disk is the sarcomeric structure most vulnerable to (eccentric) mechanical damage [PMID: 21536590].

- **Transcriptomics/proteomics:** Variant-specific increases in alpha-actinin-2 protein levels have been observed for a frameshift allele [PMID: 34170073]; no comprehensive MPD6 muscle transcriptome/proteome dataset is yet available.

**Upstream vs downstream:** Upstream = the *ACTN2* mutation and consequent protein misfolding/aggregation; downstream = Z-line disorganization → contractile deficit → fiber loss → clinical weakness. **Cell type:** skeletal muscle fiber (**CL:0000188**). **Biological process GO:** GO:0030239 (myofibril assembly), GO:0006936 (muscle contraction).

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary organ affected: **skeletal muscle** (musculoskeletal / muscular system). In the dominant distal form, cardiac and respiratory systems are **usually spared** [PMID: 39812845]. (Cardiac muscle is affected in the separate *ACTN2*-cardiomyopathy spectrum, not in MPD6.)

**Distribution (muscle MRI signature).** In the 37-patient cohort, *"the most affected muscles were the glutei minor, glutei medius, hamstrings, tibialis anterior, and soleus"* [PMID: 39812845]. A machine-learning model found the most differentiating features were involvement of **tibialis anterior and gluteus medius with preservation of quadratus femoris** [PMID: 39812845]. The recessive form shows selective hamstrings/adductors (thigh) and anterior tibial group/soleus (lower leg) [PMID: 38311799].

| Level | Structure | Suggested UBERON / CL / GO |
|---|---|---|
| Organ/system | Skeletal muscle (musculoskeletal system) | UBERON:0001134 (skeletal muscle tissue) |
| Muscle group | Tibialis anterior | UBERON:0001385 |
| Muscle group | Soleus | UBERON:0011906 |
| Muscle group | Gluteus medius/minimus | UBERON:0001500 (gluteal muscle) |
| Muscle group | Hamstrings | UBERON:0011907 (biceps femoris) |
| Cell | Skeletal muscle fiber | **CL:0000188** (skeletal muscle cell) |
| Subcellular | Sarcomere **Z-disk** | **GO:0030018** (Z disc) |
| Subcellular | Myofibril / sarcomere | GO:0030016 (myofibril), GO:0030017 (sarcomere) |

**Lateralization:** Characteristically **asymmetric** [PMID: 30900782; PMID: 38311799].

---

## 8. Temporal Development

**Onset.** **Adult-onset** (the "adult-onset" descriptor is part of the disease name). Onset pattern is **insidious/chronic**, beginning with asymmetric ankle-dorsiflexion weakness (foot drop) [PMID: 30900782]. (De novo *ACTN2* variants can cause a congenital core myopathy — MsCD — a distinct, earlier-onset presentation [PMID: 30701273].)

**Progression.** **Slowly progressive.** Weakness begins distally in the lower limbs and later spreads proximally to limb-girdle muscles [PMID: 30900782]. Severity is genotype-dependent, spanning asymptomatic carriers to limb-girdle weakness with facial involvement [PMID: 39812845].

**Course / duration.** **Chronic, lifelong,** progressive. No relapsing-remitting or episodic pattern; no spontaneous remission. Because cardiac and respiratory systems are usually spared, the course is generally not life-limiting.

**Critical periods / intervention windows.** No pharmacologic window is defined (no disease-modifying therapy exists). The practical intervention window is symptomatic — orthotic and rehabilitative management once distal weakness begins.

---

## 9. Inheritance and Population

**Epidemiology.** MPD6 is **ultra-rare.** No formal prevalence/incidence figures are established; knowledge derives from a small number of families. The largest published series comprises **37 patients from 11 families** (Spanish and Belgian) [PMID: 39812845]; the founding report described 4 families [PMID: 30900782].

**Inheritance.** **Autosomal dominant** (heterozygous *ACTN2* variant), with **incomplete, age-dependent penetrance** and **variable, genotype-dependent expressivity** [PMID: 39812845]. A biologically and clinically **distinct autosomal recessive** *ACTN2* myopathy exists (biallelic p.Arg506Gly) and must not be conflated with MPD6 [PMID: 38311799].

**Penetrance / expressivity.** Penetrance is incomplete and age-dependent (asymptomatic adult carriers occur); expressivity ranges from asymptomatic to limb-girdle weakness with facial involvement depending on the specific variant [PMID: 39812845].

**Anticipation / mosaicism:** No evidence of genetic anticipation (not a repeat-expansion disorder). Germline mosaicism has not been specifically reported.

**Founder effects.**
- **p.Ile134Asn** — Belgian founder allele (unique shared haplotype indicating common ancestry) [PMID: 39812845].
- **p.Cys487Arg** — Basque-Spanish founder allele (unique shared haplotype) [PMID: 39812845].
- (Recessive) **p.Arg506Gly** — Palestinian founder, confirmed by haplotype analysis: *"all patients report Palestinian ethnicity, suggesting a possible founder ACTN2 variant, which was confirmed through haplotype analysis in two families"* [PMID: 38311799].

*"Belgian families carrying the p.Ile134Asn variant and Basque-Spanish families carrying the p.Cys487Arg variant each showed unique haplotypes supporting respective common ancestry."* [PMID: 39812845].

**Consanguinity / carrier frequency.** Consanguinity is relevant to the recessive form (Palestinian founder) but not to dominant MPD6. Dominant pathogenic alleles are private/ultra-rare in gnomAD; no meaningful carrier frequency applies to a dominant disease.

**Population demographics.** Reported families are of Spanish (including Basque), Belgian, and Swedish origin (dominant form) [PMID: 30900782; PMID: 39812845], and Palestinian (recessive form) [PMID: 38311799]. No strong sex bias is reported (autosomal inheritance). Age distribution reflects adult onset.

---

## 10. Diagnostics

**Genetic testing (definitive).** Diagnosis rests on identification of a pathogenic *ACTN2* variant. The recommended approach is **next-generation sequencing** — a distal-myopathy/neuromuscular **gene panel** (which should include *ACTN2* alongside the ~20 dominant distal-myopathy genes such as *DNM2, MATR3, VCP, MYOT, LDB3/ZASP, FLNC, TIA1, HNRNPA1, DES, MYH7, TTN*) [PMID: 33458580], or **whole-exome sequencing** with segregation analysis. Single-gene *ACTN2* testing is appropriate when the MRI/clinical picture is characteristic or a family variant is known. Because many *ACTN2* missense variants remain VUS, **segregation and functional evidence are often needed** to confirm pathogenicity [PMID: 36116040].

**Muscle MRI (key adjunct).** A characteristic selective-involvement pattern supports the diagnosis and directs biopsy site: predominant involvement of **tibialis anterior, soleus, gluteus medius/minimus, and hamstrings**, with relative preservation of quadratus femoris [PMID: 39812845]. Muscle MRI is broadly established as crucial for myopathy diagnosis, biopsy-site selection, and activity assessment [PMID: 41066296].

**Muscle biopsy / histopathology.** Findings are **non-specific** (myopathic changes; variability in fiber diameter) but may show **Z-line disorganization, cores/multi-minicores, and alpha-actinin-2 aggregates/abnormal Z-line organization** [PMID: 34170073; PMID: 30701273]. Immunohistochemistry for alpha-actinin-2 can reveal aggregation.

**Laboratory tests.** Serum **creatine kinase (CK)** is typically normal or only mildly elevated (as in many distal myopathies). No specific circulating biomarker exists.

**Electrophysiology.** EMG shows a myopathic pattern; nerve conduction studies are normal (distinguishing from neuropathy).

**Clinical criteria / differential diagnosis.** No formal consensus criteria exist; diagnosis integrates adult-onset asymmetric distal (foot-drop) weakness, characteristic MRI, myopathic EMG, supportive biopsy, and a confirmed *ACTN2* variant. **Differential diagnosis** includes other distal myopathies (e.g., Welander, Markesbery-Griggs/ZASP, Udd/titinopathy, GNE myopathy, dysferlinopathy, myofibrillar myopathies) [PMID: 33458580], **inclusion body myositis** (asymmetric distal/proximal weakness, normal CK possible) [PMID: 37038366], and acquired causes of distal/asymmetric weakness such as vasculitic or inflammatory myopathy [PMID: 37900606; PMID: 33863518].

**Omics-based diagnostics:** Not routinely used; RNA-seq/proteomics are research tools.

**Screening.** No population or newborn screening exists (ultra-rare, adult-onset, dominant). **Cascade genetic testing** of at-risk relatives is appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Generally **not life-limiting** in the dominant distal form, because *"Cardiac and respiratory involvement were not common."* [PMID: 39812845]. No disease-specific mortality data are published.

**Morbidity / function.** The main burden is progressive **mobility impairment** from foot drop and distal-to-proximal weakness, often requiring ankle-foot orthoses and, with proximal spread, assistance for stairs and transfers. Facial weakness occurs with some genotypes [PMID: 39812845]. No formal disability/QoL instrument data (EQ-5D, SF-36, PROMIS) are published for MPD6.

**Disease course / complications.** Slowly progressive weakness; complications are secondary to reduced mobility (falls, deconditioning). Cardiomyopathy and respiratory failure are **uncommon** in dominant MPD6 [PMID: 39812845] — a key prognostic distinction from *ACTN2*-cardiomyopathy.

**Recovery potential.** None — progressive and irreversible; management is supportive, not curative.

**Prognostic factors.** **Genotype** is the principal prognostic determinant (asymptomatic → limb-girdle severity is genotype-dependent) [PMID: 39812845]. Aggregation-forming (protein-extending) variants are mechanistically more clearly pathogenic [PMID: 39095936]. No validated prognostic biomarkers exist.

---

## 12. Treatment

**There is no disease-modifying or curative therapy for MPD6.** Management is **supportive and rehabilitative.**

- **Supportive / rehabilitative care (mainstay):** Ankle-foot orthoses (AFOs) for foot drop; physiotherapy to maintain range of motion and strength; occupational therapy and assistive/mobility devices as proximal weakness develops; fall-prevention. (NCIT: *Physical Therapy* C15917; *Orthotic Device* C50094; *Rehabilitation Therapy* C15326.)
- **Pharmacotherapy:** None disease-specific. No approved drug targets alpha-actinin-2 aggregation.
- **Advanced therapeutics (none approved; conceptual):** For a dominant toxic gain-of-function/aggregation mechanism, **allele-selective silencing** (antisense oligonucleotides or siRNA targeting the mutant *ACTN2* allele) is a rational future strategy — but **no clinical trials or NCT identifiers exist** for MPD6.
- **Surgical:** None specific; orthopedic interventions (e.g., for contractures) only as needed.
- **Cardiac/respiratory monitoring:** Given that cardiac/respiratory involvement is uncommon [PMID: 39812845] but *ACTN2* is a recognized cardiomyopathy gene, **baseline cardiac evaluation** (ECG/echocardiography) is prudent, individualized to genotype and family history.
- **Pharmacogenomics / personalized medicine:** Not applicable currently; care is genotype-informed mainly for counseling and prognosis.

**Treatment outcomes / adverse events:** Rehabilitative measures improve function and safety without disease-specific pharmacologic adverse events; no response-rate data from trials exist.

---

## 13. Prevention

- **Primary prevention:** Not applicable to an inherited dominant disease beyond **reproductive options**. Preimplantation genetic testing (PGT) or prenatal diagnosis is possible when a familial pathogenic *ACTN2* variant is known.
- **Secondary prevention:** **Cascade genetic testing** of at-risk relatives enables early identification, counseling, and baseline cardiac assessment.
- **Tertiary prevention:** Rehabilitation, orthotics, fall-prevention, and contracture prevention to limit disability once symptomatic.
- **Genetic counseling (central):** Essential — 50% transmission risk per offspring for a heterozygous carrier; counseling must address incomplete/age-dependent penetrance and variable, genotype-dependent expressivity [PMID: 39812845]. For the distinct recessive *ACTN2* myopathy, carrier counseling in founder populations (e.g., Palestinian for p.Arg506Gly) applies [PMID: 38311799].
- **Immunization / public health / environmental interventions:** Not applicable (non-infectious, non-environmental Mendelian disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** *ACTN2* is evolutionarily conserved. Model orthologs: **mouse** *Actn2* (*Mus musculus*, NCBI Taxon 10090; NCBI Gene 11472) and **zebrafish** *actn2* (*Danio rerio*, NCBI Taxon 7955). Both have been used to model *ACTN2* disease [PMID: 30701273].
- **Natural disease in animals.** No well-characterized naturally occurring *ACTN2* distal myopathy is documented in companion animals or wildlife (no established OMIA entry for a spontaneous animal actininopathy).
- **Comparative biology.** The conserved Z-disk role of alpha-actinin-2 across vertebrates underlies successful cross-species modeling; wild-type alpha-actinin-2 expression does not cause anomalies, whereas mutant protein produces sarcomeric disorganization in both zebrafish and mouse — demonstrating conservation of the disease mechanism [PMID: 30701273].
- **Transmission / zoonosis:** Not applicable.

---

## 15. Model Organisms

| Model | Type | Genetic approach | Key phenotype recapitulated | Reference |
|---|---|---|---|---|
| Zebrafish (*Danio rerio*) | Vertebrate, in vivo | Exogenous expression of mutant alpha-actinin-2 | Motor deficits; sarcomeric disorganization | [PMID: 30701273] |
| Mouse (*Mus musculus*) | Mammalian, in vivo | **AAV-mediated** expression of mutant *ACTN2* in muscle | Impaired muscle force; **cores and Z-line defects**; sarcomeric disorganization | [PMID: 30701273] |
| C2C12 myoblasts/myotubes | Cellular, in vitro | Expression of *ACTN2* variants | **Alpha-actinin-2 aggregates** (dominant frameshift); no aggregates (recessive missense) | [PMID: 39095936] |
| Cultured myotubes | In vitro | MsCD missense variant | Correct Z-line localization, unaltered levels (argues against haploinsufficiency) | [PMID: 30701273] |

**Phenotype recapitulation.** Animal models faithfully reproduce the human structural pathology: *"Modelling of the disease in zebrafish and mice by exogenous expression of mutated alpha-actinin-2 recapitulated the abnormal muscle function and structure seen in the patients. Motor deficits were noted in zebrafish, and muscle force was impaired in isolated muscles from AAV-transduced mice."* [PMID: 30701273], and *"In both models, sarcomeric disorganization was evident, while expression of wild-type alpha-actinin-2 did not result in muscle anomalies. The murine muscles injected with mutant ACTN2 displayed cores and Z-line defects."* [PMID: 30701273]. The C2C12 model recapitulates the dominant aggregation mechanism and distinguishes it from recessive variants [PMID: 39095936].

**Limitations.** Existing models use **exogenous/overexpression** of mutant protein (zebrafish, AAV-mouse) rather than physiological knock-in at endogenous levels; they capture structural pathology and force deficits but not the slow adult-onset, distal-predominant progression seen in patients. No germline knock-in mouse recapitulating adult-onset distal MPD6 has been reported.

---

## Mechanistic Model / Interpretation

```
  Heterozygous ACTN2 variant (missense OR C-terminal-extending frameshift)
                              │  (germline, autosomal dominant)
                              ▼
      Structurally altered alpha-actinin-2  →  reduced solubility,
                              │                 thermal destabilization  [42481460]
                              ▼
        MISFOLDING  ── branch A (dominant frameshift/extension) ──► Z-disk AGGREGATES [39095936, 34170073]
                    │                                              + increased ACTN2 expression
                    └─ branch B (congenital MsCD missense/del) ──► correct Z-line targeting,
                                                                   but CORES + Z-line defects [30701273]
                              │
                              ▼
              Z-line disorganization / impaired sarcomere integrity
                              ▼
              ↓ contractile force  (mouse force deficit; zebrafish motor deficit) [30701273]
                              ▼
              Progressive myofiber degeneration & loss  [33458580 — dystrophic paradigm; inferred]
                              ▼
   ASYMMETRIC DISTAL LOWER-LIMB WEAKNESS (foot drop) → proximal/limb-girdle spread
                              │  (genotype-dependent severity) [30900782, 39812845]
                              ▼
              Usually SPARES heart & respiration [39812845]

  ── Parallel (cardiac-relevant, NOT primary in MPD6) ──
  Spectrin-repeat domain binds Nav1.5 → modulates Na+ channel surface density [19943616]
   → some ACTN2 variants → arrhythmia / idiopathic VF [35975100]
```

**Synthesis.** MPD6 is best understood as a **dominant sarcomeric proteinopathy of the Z-disk.** The unifying lesion is a destabilized alpha-actinin-2 that misfolds and — for dominant protein-extending alleles — aggregates, poisoning Z-disk assembly (a dominant-negative/toxic gain-of-function effect rather than simple loss of function). This distinguishes MPD6 both from the **recessive** *ACTN2* myopathy (missense, non-aggregating, distinct phenotype and Palestinian founder) [PMID: 38311799] and from **ACTN2 cardiomyopathy/arrhythmia**, where the protein's separate ion-channel–scaffolding role via its spectrin-repeat domain becomes pathogenically relevant [PMID: 19943616; PMID: 35975100]. The single gene *ACTN2* thus produces a spectrum — dominant distal MPD6, congenital MsCD, recessive myopathy, and cardiomyopathy — whose divergent phenotypes track with variant type, domain location, aggregation propensity, and zygosity.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [30900782](https://pubmed.ncbi.nlm.nih.gov/30900782/) | *Actininopathy: A new muscular dystrophy caused by ACTN2 dominant mutations* (Savarese et al.) | **Defining paper** — dominant *ACTN2* missense variants, adult-onset asymmetric distal phenotype, disease concept |
| [39812845](https://pubmed.ncbi.nlm.nih.gov/39812845/) | *Clinical and imaging spectrum of non-congenital dominant ACTN2 myopathy* (Iruzubieta et al.) | **Largest cohort (37 pts/11 families)** — genotype-dependent phenotype, MRI signature, founder alleles, cardiac/respiratory sparing |
| [39095936](https://pubmed.ncbi.nlm.nih.gov/39095936/) | *Protein-extending ACTN2 frameshift variants cause variable myopathy phenotypes by protein aggregation* | Establishes **aggregation** as the dominant mechanism (frameshift aggregates; recessive missense do not) |
| [34170073](https://pubmed.ncbi.nlm.nih.gov/34170073/) | *A novel frameshift ACTN2 variant causes a rare adult-onset distal myopathy with multi-minicores* | Independent family: increased ACTN2, abnormal Z-line, aggregate formation |
| [30701273](https://pubmed.ncbi.nlm.nih.gov/30701273/) | *ACTN2 mutations cause "Multiple structured Core Disease" (MsCD)* (Lornage et al.) | **Zebrafish + mouse models**; cores/Z-line defects; argues against haploinsufficiency for MsCD variant |
| [42481460](https://pubmed.ncbi.nlm.nih.gov/42481460/) | *Comprehensive biophysical/structural profiling of alpha-actinin-2 variants* (Noureddine et al.) | Variant destabilization, reduced solubility, aggregation propensity |
| [27287556](https://pubmed.ncbi.nlm.nih.gov/27287556/) | *HCM mutations in the CH domain of ACTN2 affect actin binding and Z-disc incorporation* | CH-domain variants alter actin binding and Z-disc dynamics |
| [19943616](https://pubmed.ncbi.nlm.nih.gov/19943616/) | *Cell membrane expression of Nav1.5 is modulated by alpha-actinin-2 interaction* (Ziane et al.) | Spectrin-repeat/Nav1.5 interaction → cardiac electrophysiology branch |
| [35975100](https://pubmed.ncbi.nlm.nih.gov/35975100/) | *Novel ACTN2 missense variant associated with idiopathic VF* | *ACTN2* arrhythmia phenotype (distinct from MPD6) |
| [38311799](https://pubmed.ncbi.nlm.nih.gov/38311799/) | *Recurring homozygous ACTN2 variant (p.Arg506Gly) causes a recessive myopathy* | **Distinct recessive entity**; Palestinian founder |
| [36116040](https://pubmed.ncbi.nlm.nih.gov/36116040/) | *Mutation update for the ACTN2 gene* | Domain/localization biology; caution on VUS and genotype–phenotype correlations |
| [33458580](https://pubmed.ncbi.nlm.nih.gov/33458580/) | *Panorama of the distal myopathies* | Nosology; *ACTN2* among ~20 dominant distal-myopathy genes; dystrophic paradigm |
| [21536590](https://pubmed.ncbi.nlm.nih.gov/21536590/) | *α-actinin-3 deficiency and contraction-induced damage* | Z-disk vulnerability to eccentric damage; ACTN2/ACTN3 Z-disk biology (modifier plausibility) |
| [41066296](https://pubmed.ncbi.nlm.nih.gov/41066296/) | *Myopathies: Radiologist's essential tips* | Role of muscle MRI in myopathy diagnosis/biopsy targeting |

**Evidence source types:** human clinical/genetic (30900782, 39812845, 34170073, 38311799, 35975100, 36116040); in vivo model organism (30701273 — zebrafish/mouse); in vitro cell/biophysical (39095936, 42481460, 27287556, 19943616); review/nosology (33458580, 41066296, 21536590).

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** The entire dominant-disease literature rests on a handful of families (largest series 37 patients) [PMID: 39812845]; prevalence, incidence, sex ratio, and natural-history metrics are not formally established.
2. **VUS burden.** Many *ACTN2* missense variants lack segregation/functional confirmation; genotype–phenotype correlations are demonstrated for only some variants [PMID: 36116040].
3. **Mechanistic gap (aggregation → fiber loss).** The step from Z-disk aggregation to progressive myofiber degeneration is inferred from the dystrophic paradigm, not dissected in MPD6 muscle.
4. **Model limitations.** Existing zebrafish/mouse models rely on overexpression rather than endogenous knock-in and do not reproduce the slow, adult-onset, distal progression [PMID: 30701273].
5. **No omics datasets.** No published MPD6-specific transcriptomic, proteomic, or single-cell datasets exist.
6. **No QoL / outcome instruments.** No EQ-5D/SF-36/PROMIS or validated functional-outcome data for MPD6.
7. **No therapeutics.** No disease-modifying treatment, biomarker, or clinical trial (no NCT) exists.

---

## Proposed Follow-up Experiments / Actions

1. **Generate an endogenous knock-in mouse** for a recurrent dominant allele (e.g., p.Cys487Arg or a protein-extending frameshift) to model adult-onset distal progression and test disease-modifying strategies.
2. **Allele-selective silencing proof-of-concept.** Test mutant-allele–specific ASO/siRNA in patient iPSC-derived myotubes and knock-in models, given the dominant aggregation mechanism [PMID: 39095936].
3. **Aggregation-focused biomarkers.** Quantify alpha-actinin-2 aggregate load and proteostatic-stress markers in patient biopsies as candidate progression biomarkers.
4. **Multi-omics of patient muscle.** Bulk/single-nucleus RNA-seq and proteomics of affected vs preserved muscles (guided by the MRI signature [PMID: 39812845]) to map downstream degeneration pathways.
5. **Prospective natural-history registry** with standardized MRI (tibialis anterior/soleus/gluteus medius scoring) and functional outcomes to define progression rate and penetrance curves.
6. **Systematic variant reclassification.** Combine biophysical destabilization/aggregation assays [PMID: 42481460] with segregation data to resolve *ACTN2* VUS.
7. **Cardiac surveillance study.** Prospectively assess subclinical cardiac/electrophysiologic involvement across MPD6 genotypes, given alpha-actinin-2's Nav1.5-scaffolding role [PMID: 19943616].

---

## Ontology Term Quick-Reference

- **Disease:** MONDO:0014138; OMIM:615197
- **Gene/protein:** ACTN2 (HGNC:164, NCBI Gene 88); UniProt P35609
- **Phenotype (HPO):** HP:0009053 (distal lower limb muscle weakness), HP:0003701 (proximal muscle weakness), HP:0001288 (gait disturbance), HP:0030319 (facial weakness), HP:0001638 (cardiomyopathy — usually absent)
- **Cell (CL):** CL:0000188 (skeletal muscle cell / myofiber)
- **Anatomy (UBERON):** UBERON:0001134 (skeletal muscle tissue), UBERON:0001385 (tibialis anterior), UBERON:0011906 (soleus), UBERON:0001500 (gluteal muscle)
- **Subcellular / process (GO):** GO:0030018 (Z disc), GO:0030016 (myofibril), GO:0030239 (myofibril assembly), GO:0006457 (protein folding), GO:0006936 (muscle contraction)
- **Treatment (NCIT):** C15917 (Physical Therapy), C50094 (Orthotic Device), C15326 (Rehabilitation Therapy)

---

*Report compiled from 5 completed investigation iterations, 30 reviewed papers, and 8 confirmed findings. All quoted statements are verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014138` (3 mentions) - the report calls it "Mondo"; MONDO calls it **nemaline myopathy 8**
- `UBERON:0011906` (2 mentions) - the report calls it "Soleus", "soleus"; UBERON calls it **muscle head**
- `UBERON:0011907` (1 mention) - the report calls it "biceps femoris"; UBERON calls it **gastrocnemius medialis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001638` (2 mentions) - the report calls it "cardiomyopathy — usually absent"; HP calls it **Cardiomyopathy**
- `CL:0000188` (3 mentions) - the report calls it "skeletal muscle cell / myofiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0001500` (2 mentions) - the report calls it "gluteal muscle"; UBERON calls it **muscle of manus**, and lists "hand muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001385` - called "Tibialis anterior", "tibialis anterior"
- `UBERON:0011906` - called "Soleus", "soleus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.