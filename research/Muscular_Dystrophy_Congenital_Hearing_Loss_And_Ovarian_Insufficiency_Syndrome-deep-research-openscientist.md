---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T17:41:01.255478'
end_time: '2026-09-07T18:09:30.155139'
duration_seconds: 1708.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency
    Syndrome
  mondo_id: MONDO:0859189
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 7
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 11
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35869884
  relevance_assessed: 15
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMID:31427080
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 49
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 23
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859189
    reported_labels:
    - Disease MONDO
    ontology_label: muscular dystrophy, congenital hearing loss, and ovarian insufficiency
      syndrome
  labels_variant: 1
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
  path: Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency Syndrome
- **MONDO ID:** MONDO:0859189 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency Syndrome** covering all of the
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

# Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency Syndrome (MDHLOV): A Comprehensive Disease Report

**Disease:** Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency Syndrome
**MONDO ID:** MONDO:0859189 · **OMIM:** #619518 (MDHLOV) · **Gene:** *GGPS1* (1q42.3)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Muscular Dystrophy, Congenital Hearing Loss, and Ovarian Insufficiency Syndrome (MDHLOV; also abbreviated MDHLO/MUDHLOV) is an **ultra-rare autosomal-recessive multisystem disorder** caused by biallelic hypomorphic missense variants in ***GGPS1***, the gene on chromosome 1q42.3 encoding **geranylgeranyl diphosphate synthase (GGPPS/GGDPS)**. This enzyme sits in the mevalonate/isoprenoid pathway and produces geranylgeranyl pyrophosphate (GGPP, C20), the lipid donor used to geranylgeranylate small GTPases (the Rab and Rho families). The syndrome was first defined by Foley et al. in 2020, who identified 5 different biallelic pathogenic *GGPS1* variants in 11 patients from 6 families, and has since been expanded by additional cohorts.

The core clinical picture is a **fully penetrant, congenital-onset, progressive proximal muscular dystrophy** (elevated creatine kinase; dystrophic histology with centrally nucleated fibers and rimmed vacuoles) accompanied by two variable extra-muscular features: **congenital sensorineural hearing loss** and, in post-pubertal females, **primary/premature ovarian insufficiency**. The combination of sensorineural hearing loss plus ovarian insufficiency overlaps clinically with **Perrault syndrome**, and *GGPS1* is now counted among the Perrault-syndrome gene set. Later reports have shown the two non-muscle features are variable — hearing loss was present in only 46% of one cohort, and at least one patient had isolated proximal weakness with hepatic transaminase elevation and spared hearing — expanding the phenotypic spectrum.

Mechanistically, reduced GGPP supply is inferred to impair prenylation-dependent membrane anchoring of small GTPases (particularly Rab proteins), degrading vesicle trafficking and the Ca²⁺-dependent sarcolemmal membrane-repair machinery. Direct functional support comes from **delayed membrane healing after laser injury in patient-derived myogenic cells** and a disease-specific **Y259C knock-in mouse**. There is **no disease-specific therapy**; management is supportive (respiratory care, hearing rehabilitation, hormone replacement for ovarian insufficiency, physical therapy, orthopedic management of scoliosis). This report consolidates 10 confirmed findings and 25 reviewed papers across all 15 requested sections.

---

## Key Findings

### Finding 1 — Biallelic *GGPS1* variants cause the muscle–ear–ovary triad

The foundational discovery (Foley et al., 2020) used **whole exome sequencing superimposed on shared-haplotype mapping** to identify biallelic *GGPS1* variants as the cause of this syndrome. Eleven patients across six families carried five distinct biallelic pathogenic variants. The gene product, **geranylgeranyl diphosphate synthase**, catalyzes the synthesis of geranylgeranyl pyrophosphate, the lipid precursor of geranylgeranylated proteins including small GTPases. The clinical triad was: proximal muscular dystrophy in all 11 patients (100%), congenital sensorineural hearing loss in 10 of 11, and primary ovarian insufficiency in all post-pubertal females. Inheritance is autosomal recessive.

> "We applied whole exome sequencing (WES) superimposed on shared haplotype regions to identify the initial biallelic variants in GGPS1." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)
> "In addition to proximal weakness, all but one patient presented with congenital sensorineural hearing loss, and all postpubertal females had primary ovarian insufficiency." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)

### Finding 2 — Hearing loss and ovarian insufficiency are variable; the spectrum includes hepatic involvement

Two subsequent reports broadened the phenotype. Kaiyrzhanov et al. (2022) described 11 additional individuals from 4 families with missense *GGPS1* variants in whom **hearing loss was present in only 46%**, and concluded the data "demonstrates that hearing loss and ovarian insufficiency might be a variable feature of the GGPS1-associated muscular dystrophy." Altassan et al. (2024) reported a patient who "presented with only proximal muscle weakness, and elevated liver transaminases with spared hearing function," adding **hepatic involvement** to the recognized spectrum and confirming that hearing can be spared.

> "hearing loss was present in only 46% of the individuals … demonstrates that hearing loss and ovarian insufficiency might be a variable feature of the GGPS1-associated muscular dystrophy." — [PMID: 35869884](https://pubmed.ncbi.nlm.nih.gov/35869884/)
> "The patient presented with only proximal muscle weakness, and elevated liver transaminases with spared hearing function." — [PMID: 38129970](https://pubmed.ncbi.nlm.nih.gov/38129970/)

**Interpretation:** Myopathy is the obligate, fully penetrant feature; sensorineural hearing loss and ovarian insufficiency show variable expressivity. This variable expressivity is why the disorder is sometimes ascertained as "Perrault-syndrome-like" and sometimes as an isolated congenital muscular dystrophy.

### Finding 3 — Mechanism: reduced GGPP impairs Rab/small-GTPase geranylgeranylation and sarcolemmal membrane repair

Foley et al. demonstrated **delayed membrane healing after laser injury in patient-derived myogenic cells** and generated a **Y259C knock-in mouse**, whose muscle histology was dystrophic with ultrastructural autophagic material and enlarged mitochondria. GGPP is the obligate lipid precursor for geranylgeranylation of small GTPases including the Rab family. Independent literature establishes the mechanistic links: Ca²⁺-dependent vesicle-fusion-based sarcolemmal resealing is an active, essential process in skeletal muscle and is defective in membrane-repair myopathies (Bansal et al., 2003); and Rab GTPases require C-terminal prenylation for membrane tethering. Removing the geranylgeranyl lipid group therefore strips Rabs of their ability to anchor to membranes and drive vesicle trafficking.

> "There was delayed membrane healing after laser injury in patient-derived myogenic cells." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)
> "Membrane repair is therefore an active process in skeletal muscle fibres." — [PMID: 12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/)
> "Rabs oscillate between an inactive GDP-bound conformation and an active GTP-bound state that is tethered to lipid membranes via a C-terminal prenylation site on conserved cysteine residues." — [PMID: 23663983](https://pubmed.ncbi.nlm.nih.gov/23663983/)

### Finding 4 — Identifiers and constraint: *GGPS1* is not LoF-constrained, consistent with recessive hypomorphic disease

| Attribute | Value |
|---|---|
| Disease MONDO | MONDO:0859189 |
| Disease OMIM | #619518 (MDHLOV) |
| MedGen / UMLS | C5561980 / 1794190 |
| Gene HGNC | HGNC:4249 |
| NCBI Gene | 9453 |
| Ensembl | ENSG00000152904 |
| Cytoband | 1q42.3 (GRCh38 chr1:235,327,350–235,344,544) |
| Gene MIM | 606982 |
| RefSeq transcript | NM_004837.4 |
| Aliases | MDHLO, MUDHLOV |

gnomAD constraint metrics show **pLI = 0.007**, observed/expected LoF = 0.53 (90% CI 0.36–0.82), and missense Z = 1.47 — i.e., *GGPS1* is **not** strongly haploinsufficient or LoF-intolerant. This is fully consistent with an autosomal-recessive mechanism in which biallelic **hypomorphic missense** alleles (partial loss of function), rather than complete nulls, cause disease. Complete loss of GGPP synthesis is presumed incompatible with life (see Finding 9).

### Finding 5 — Pathogenic missense variants cluster in the C-terminal catalytic/substrate-binding region

ClinVar (NM_004837.4) pathogenic/likely-pathogenic *GGPS1* SNVs cluster tightly:

| cDNA | Protein | ClinVar significance | Notes |
|---|---|---|---|
| c.776A>G | p.Tyr259Cys | Pathogenic | Used for the knock-in mouse |
| c.781C>G | p.Arg261Gly | Pathogenic | Most recurrent allele (mutational hotspot) |
| c.782G>A | p.Arg261His | Conflicting | Same residue hotspot |
| c.770T>G | p.Phe257Cys | Likely pathogenic | |
| c.854T>G | p.Val285Gly | Pathogenic | |
| c.764G>A | p.Gly255Asp | VUS | |
| c.790C>G | p.Leu264Val | VUS | |
| c.545T>C | p.Leu182Pro | VUS | |

All disease-causing variants are **ultra-rare missense substitutions** falling in specific catalytic domains of the enzyme, with **Arg261 an apparent mutational hotspot**. Large 1q42 copy-number variants in ClinVar are non-specific and not associated with this Mendelian disorder.

> "Ultra-rare biallelic pathogenic variants in geranylgeranyl diphosphate synthase 1 (GGPS1) have recently been associated with muscular dystrophy/hearing loss/ovarian insufficiency syndrome." — [PMID: 35869884](https://pubmed.ncbi.nlm.nih.gov/35869884/)
> "A total of 11 patients in 6 families carrying 5 different biallelic pathogenic variants in specific domains of GGPS1 were identified." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)

### Finding 6 — Pathogenic alleles are absent-to-ultra-rare in gnomAD v4

| Variant | Protein | gnomAD v4 alleles | Approx. AF | Homozygotes |
|---|---|---|---|---|
| c.776A>G | p.Tyr259Cys | 0 | absent | 0 |
| c.854T>G | p.Val285Gly | 0 | absent | 0 |
| c.781C>G | p.Arg261Gly | 34 | ~2.2×10⁻⁵ | 0 |
| c.782G>A | p.Arg261His | ~ | ~1.0×10⁻⁵ | 0 |
| c.545T>C | p.Leu182Pro (VUS) | 8 | ~4.7×10⁻⁶ | 0 |
| c.764G>A | p.Gly255Asp (VUS) | 1 | — | 0 |

**No homozygotes** are reported for any pathogenic allele, consistent with recessive selection against homozygous carriers. p.Arg261Gly is the most recurrent pathogenic allele.

### Finding 7 — HPO phenotype spectrum with frequencies

Curated HPO annotations (OMIM:619518; n ≈ 11 patients):

| Phenotype | HPO term | Frequency |
|---|---|---|
| Progressive muscle weakness | HP:0003323 | 11/11 (100%) |
| Congenital onset | HP:0003577 | 11/11 (100%) |
| Elevated serum creatine kinase | HP:0003236 | 9/9 (100%) |
| Centrally nucleated skeletal muscle fibers | HP:0003687 | 9/9 |
| Rimmed vacuoles | HP:0003805 | 9/9 |
| Skeletal muscle autophagosome accumulation | HP:0025717 | 2/9 |
| Mitochondrial hypertrophy | HP:0033686 | 1/9 |
| Sensorineural hearing impairment | HP:0000407 | 10/11 (91%)* |
| Premature ovarian insufficiency | HP:0008209 | 3/3 |
| Female infertility | HP:0008222 | 3/3 |
| Short stature | HP:0004322 | 8/11 |
| Failure to thrive | HP:0001508 | 7/10 |
| Respiratory insufficiency | HP:0002093 | 8/10 |
| Reduced forced vital capacity | HP:0032341 | 2/4 |
| Loss of ambulation | HP:0002505 | 5/11 |
| Scoliosis | HP:0002650 | 4/10 |
| Motor delay | HP:0001270 | — |
| Decreased fetal movement | HP:0001558 | — |
| Poor suck | HP:0002033 | — |
| Weak cry | HP:0001612 | — |
| Autosomal recessive inheritance | HP:0000007 | — |

*The 91% figure derives from the original Foley cohort; the pooled frequency across later cohorts is lower (~46% in Kaiyrzhanov et al.), reflecting variable expressivity.

### Finding 8 — GGPS1 protein: cytosolic prenyltransferase homohexamer localized to the sarcomere Z-line

UniProt **O95749** (human GGPS1, 300 aa) catalyzes the sequential trans-addition of isopentenyl diphosphate (IPP) onto dimethylallyl/geranyl/farnesyl diphosphate to form GGPP (C20). Its quaternary structure is a **homohexamer** (a trimer of homodimers), consistent with crystal structures of bacterial GGPP synthases (e.g., *Nonlabens dokdonensis*, which "forms a hexamer composed of homodimeric trimer"). Subcellular localization spans the cytoplasm, perinuclear region, and — notably for muscle disease — the **myofibril/sarcomere Z-line**. The UniProt disease annotation (MDHLO) reads: "An autosomal recessive disorder characterized by early-onset progressive muscle weakness, sensorineural hearing loss, and primary amenorrhea due to ovarian insufficiency. Some patients become wheelchair-bound by the second decade, whereas others have a milder phenotype and maintain independent ambulation."

> "GGPS1 encodes geranylgeranyl diphosphate synthase in the mevalonate/isoprenoid pathway, which catalyzes the synthesis of geranylgeranyl pyrophosphate, the lipid precursor of geranylgeranylated proteins including small guanosine triphosphatases." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)

### Finding 9 — Model organisms and evolutionary conservation

*GGPS1* is highly conserved with clear orthologs across the tree of life: mouse *Ggps1* (NCBI Gene 14593; MGI), rat *Ggps1* (291211), zebrafish *ggps1* (336798), *Xenopus ggps1* (549876), *Drosophila* (NCBI 38816), and *S. cerevisiae* **BTS1** (856036). Foley et al. generated a disease-specific **p.Tyr259Cys knock-in mouse**. Independent mouse work shows *Ggpps* has essential roles: skeletal-muscle-specific deletion causes insulin resistance via RhoA geranylgeranylation ([PMID: 26112408](https://pubmed.ncbi.nlm.nih.gov/26112408/)), and liver-specific deletion alters adipose remodeling via Rab27A-dependent extracellular-vesicle secretion ([PMID: 32024826](https://pubmed.ncbi.nlm.nih.gov/32024826/)). Global loss of *Ggpps* is not viable — consistent with GGPP being an essential isoprenoid and with the human disease requiring hypomorphic (not null) alleles.

> "the generation of a Y259C knock-in mouse were done." — [PMID: 32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/)
> "we generated mice with specific GGPPS deletions in their skeletal muscle tissue." — [PMID: 26112408](https://pubmed.ncbi.nlm.nih.gov/26112408/)

### Finding 10 — GGPS1 belongs to the polyprenyl-synthetase fold; disease residues line the catalytic domain

InterPro annotation of O95749: Pfam **PF00348** (polyprenyl synthetase domain); InterPro IPR000092 (polyprenyl synthetase-like family), IPR008949 (isoprenoid synthase domain superfamily), IPR033749 (conserved site); CDD cd00685 (trans-isoprenyl diphosphate synthases, head-to-tail); CATH G3DSA:1.10.600.10 (farnesyl-diphosphate-synthase homologous superfamily); PROSITE PS00444/PS00723; PANTHER PTHR12001 (GGPP synthase family). The pathogenic residues **Phe257, Tyr259, Arg261, and Val285** all fall within this C-terminal catalytic/substrate-binding domain, providing a structural rationale for their hypomorphic effect on enzyme activity.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Biallelic hypomorphic missense variant in GGPS1 (e.g., p.Tyr259Cys, p.Arg261Gly)
   in the C-terminal catalytic/substrate-binding domain
        │  leads to
        ▼
2. Partial loss of geranylgeranyl diphosphate synthase catalytic activity
   (homohexameric prenyltransferase; complete loss is lethal → only hypomorphs survive)
        │  results in
        ▼
3. Reduced cellular supply of geranylgeranyl pyrophosphate (GGPP, C20 isoprenoid)
        │  results in
        ▼
4. Impaired protein geranylgeranylation of small GTPases at their C-terminal
   cysteine motifs (Rab family; Rho family) [inferred from enzyme function + Rab biology]
        │  leads to
        ▼
5. Small GTPases fail to anchor to membranes → defective vesicle trafficking
   and membrane-associated signaling
        │
        ├──► (MUSCLE branch, demonstrated)
        │    6a. Defective Ca²⁺-dependent sarcolemmal membrane-repair vesicle fusion
        │        → delayed membrane resealing after injury (shown in patient myogenic cells)
        │        → chronic myofiber damage, autophagic/rimmed vacuoles, mitochondrial
        │          enlargement, central nucleation
        │        → PROGRESSIVE PROXIMAL MUSCULAR DYSTROPHY, ↑ creatine kinase (fully penetrant)
        │
        ├──► (COCHLEA branch, inferred)
        │    6b. Impaired trafficking in cochlear hair/supporting cells
        │        → CONGENITAL SENSORINEURAL HEARING LOSS (variable, ~46–91%)
        │
        └──► (OVARY branch, inferred)
             6c. Impaired trafficking / prenylation in ovarian granulosa/germ cells
                 → PRIMARY / PREMATURE OVARIAN INSUFFICIENCY (post-pubertal females)

   (LIVER branch, occasionally observed): hepatic transaminase elevation
```

**Upstream vs downstream.** The upstream lesion is the enzymatic deficit (steps 1–3); the downstream effectors are the under-prenylated small GTPases and the trafficking/repair failures they cause (steps 4–6). The muscle branch is the best-supported (direct patient-cell and mouse evidence); the cochlear and ovarian branches are mechanistically inferred by analogy to the same prenylation defect acting in tissues with high secretory/trafficking demand.

**Pathways, cell types, compartments.**
- **Molecular pathway:** mevalonate/isoprenoid biosynthesis → GGPP → protein geranylgeranylation; downstream RhoA/Rho-kinase and Rab-dependent vesicle trafficking.
- **Cellular processes (GO):** protein geranylgeranylation (GO:0018344), isoprenoid biosynthetic process (GO:0008299), plasma-membrane repair (GO:0001778), vesicle-mediated transport (GO:0016192), autophagy (GO:0006914).
- **Cell types (CL):** skeletal muscle fiber (CL:0000188), cochlear hair cell (CL:0000855), ovarian granulosa cell (CL:0000501), hepatocyte (CL:0000182).
- **Subcellular compartments (GO CC):** cytoplasm/cytosol (GO:0005829), sarcomere Z-disc (GO:0030018), myofibril (GO:0030016), sarcolemma (GO:0042383), mitochondrion (GO:0005739).
- **Chemical entities (CHEBI):** geranylgeranyl diphosphate (CHEBI:48861), isopentenyl diphosphate (CHEBI:128769), farnesyl diphosphate (CHEBI:175763).

### Relationship to Perrault syndrome

Because sensorineural hearing loss + ovarian insufficiency is the definition of **Perrault syndrome**, *GGPS1* is now listed among Perrault-syndrome genes alongside a set that is otherwise dominated by mitochondrial/peroxisomal genes (HSD17B4, HARS2, CLPP, LARS2, TWNK, ERAL1, RMND1, DAP3, PRORP, MRPL50, MRPL49, MRPS7, PEX6, TFAM). *GGPS1* is mechanistically distinct — an isoprenoid-pathway gene rather than a mitochondrial-translation gene — and is uniquely accompanied by a **prominent muscular dystrophy**, which is the discriminating feature at the bedside.

---

## Section-by-Section Disease Report

### 1. Disease Information
A rare Mendelian multisystem disorder: congenital-onset progressive proximal muscular dystrophy with variable sensorineural hearing loss and primary ovarian insufficiency. **Identifiers:** MONDO:0859189; OMIM #619518 (MDHLOV); MedGen C5561980; UMLS C5561980. **Synonyms:** MDHLO, MUDHLOV, "GGPS1-related/associated congenital muscular dystrophy," "GGPS1-associated muscular dystrophy with/without hearing loss." Information is derived from **aggregated disease-level resources** (OMIM/Orphanet/UniProt/ClinVar) built from a small number of published patient cohorts (≈22 patients total across three primary reports), not from EHR-scale data.

### 2. Etiology
**Causal factor:** purely genetic — biallelic hypomorphic missense variants in *GGPS1*. **Genetic risk factors:** the causal variants themselves (Finding 5); no established modifier genes. **Environmental risk/protective factors:** none identified — this is a monogenic disorder without known environmental modifiers. **Consanguinity** raises risk (homozygous alleles reported). **Gene-environment interactions:** none documented. Note: statins (HMG-CoA reductase inhibitors) reduce mevalonate-pathway flux upstream of GGPP and are theoretically of concern, but no clinical interaction data exist.

### 3. Phenotypes
See Finding 7 for the full HPO table with frequencies. **Obligate feature:** progressive proximal muscle weakness (HP:0003323), congenital onset (HP:0003577), elevated CK (HP:0003236). **Variable features:** sensorineural hearing loss (HP:0000407; ~46–91%), premature ovarian insufficiency (HP:0008209) in post-pubertal females, respiratory insufficiency (HP:0002093), short stature (HP:0004322), scoliosis (HP:0002650), loss of ambulation (HP:0002505). **Progression:** progressive; some patients wheelchair-bound by the second decade, others retain independent ambulation. **Quality-of-life impact:** substantial — mobility loss, respiratory compromise, deafness, and infertility.

### 4. Genetic/Molecular Information
**Causal gene:** *GGPS1* (HGNC:4249; gene MIM 606982; NM_004837.4). **Variants:** ultra-rare missense (Finding 5), clustered in the C-terminal catalytic domain, ACMG classifications ranging pathogenic → VUS. **Allele frequencies:** absent-to-ultra-rare in gnomAD v4 with no homozygotes (Finding 6). **Origin:** germline. **Functional consequence:** partial (hypomorphic) loss of enzyme function. **Modifier genes / epigenetics / chromosomal abnormalities:** none established for this disorder (large 1q42 CNVs in ClinVar are non-specific).

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known. Disease is fully explained by biallelic *GGPS1* genotype.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain, pathway/GO/CL/CHEBI annotations, and branch structure.

### 7. Anatomical Structures Affected
**Organ level (primary):** skeletal muscle (UBERON:0001134), esp. proximal limb-girdle muscles; **cochlea/inner ear** (UBERON:0001844); **ovary** (UBERON:0000992). **Secondary:** respiratory muscles/diaphragm → respiratory insufficiency; axial skeleton → scoliosis; **liver** (UBERON:0002107) in some. **Body systems:** musculoskeletal, auditory/sensory, endocrine/reproductive, respiratory. **Tissue/cell:** striated muscle fiber (CL:0000188), cochlear hair cells (CL:0000855), ovarian granulosa cells (CL:0000501). **Subcellular:** sarcomere Z-line/myofibril, sarcolemma, cytosol, mitochondria (enlarged on EM), autophagosomes. **Lateralization:** bilateral/symmetric.

### 8. Temporal Development
**Onset:** congenital (decreased fetal movement, weak cry, poor suck, motor delay). **Course:** chronic, progressive, lifelong. **Progression rate:** variable — wheelchair by second decade in severe cases vs. maintained ambulation in milder cases. Ovarian insufficiency manifests at expected puberty (primary amenorrhea / premature ovarian failure). **Critical periods:** perinatal and childhood for motor/respiratory decline; puberty for reproductive endocrine failure. No remission.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (HP:0000007). **Penetrance:** complete for myopathy; variable expressivity for hearing loss and ovarian insufficiency. **Epidemiology:** ultra-rare; no formal prevalence/incidence estimate (≈22 reported patients worldwide). **Founder/consanguinity:** homozygous alleles reported in consanguineous families; p.Arg261Gly is a recurrent (hotspot) allele. **Carrier frequency:** each pathogenic allele is absent-to-ultra-rare in gnomAD; no homozygotes observed. **Sex ratio:** both sexes affected by muscle/ear disease; ovarian insufficiency affects females only.

### 10. Diagnostics
**Laboratory:** elevated serum creatine kinase (near-universal). **Audiology:** confirms sensorineural hearing loss. **Endocrine:** elevated gonadotropins/low estradiol, primary amenorrhea in females (ovarian insufficiency). **Muscle biopsy/histopathology:** dystrophic changes, centrally nucleated fibers (HP:0003687), rimmed vacuoles (HP:0003805), autophagic material, enlarged mitochondria on EM. **Pulmonary function:** reduced forced vital capacity in some. **Genetic testing (definitive):** WES or WGS with shared-haplotype/segregation analysis identified the gene; targeted single-gene or Perrault-syndrome/congenital-muscular-dystrophy panel testing of *GGPS1* (NM_004837.4) confirms diagnosis. CMA/karyotype not informative. **Differential diagnosis:** other Perrault-syndrome genes (mitochondrial-translation/peroxisomal — CLPP, LARS2, HARS2, TWNK, MRPL49, PRORP, etc.), other congenital/limb-girdle muscular dystrophies (notably dysferlinopathy and other membrane-repair myopathies), and other causes of primary ovarian insufficiency. Prominent congenital muscular dystrophy plus the *GGPS1* genotype distinguishes MDHLOV from classic Perrault syndrome.

### 11. Outcome / Prognosis
Chronic, progressive, lifelong disability. **Motor:** loss of ambulation in a subset (5/11 in the original cohort). **Respiratory:** insufficiency in the majority — the principal driver of morbidity/mortality. **Reproductive:** infertility from ovarian insufficiency. **Sensory:** permanent hearing loss. No formal survival statistics; prognosis is dominated by respiratory muscle involvement and mobility loss. **Prognostic factors:** severity/onset of weakness and respiratory decline; genotype-phenotype correlation is suggested but not firmly established given small numbers.

### 12. Treatment
**No disease-specific/curative therapy exists.** Management is **supportive and multidisciplinary**: physical/occupational therapy and mobility aids; respiratory monitoring and non-invasive ventilation for respiratory insufficiency; hearing aids or cochlear implantation for sensorineural hearing loss; **hormone replacement therapy** for primary ovarian insufficiency (estrogen/progesterone; bone-health protection); orthopedic management (scoliosis, contractures); nutritional support for failure to thrive; genetic counseling. **Advanced/experimental therapeutics:** none approved; no gene, cell, or RNA therapies in trials for this disorder. Theoretically, substrate-supplementation or pathway-modulation strategies are of mechanistic interest but untested. **Pharmacogenomic caution:** statins (which lower mevalonate flux upstream of GGPP) are theoretically undesirable but have no specific evidence base here. Suggested NCIT intervention terms: physical therapy (NCIT:C15327), hormone replacement therapy (NCIT:C62556), mechanical ventilation (NCIT:C70909), cochlear implant (NCIT:C99913).

### 13. Prevention
No primary prevention (monogenic). **Genetic counseling** for at-risk families (25% recurrence risk per pregnancy for carrier couples). **Carrier and cascade testing** of relatives; **prenatal diagnosis** and **preimplantation genetic testing** are options once the familial variants are known. Newborn screening does not cover this disorder. Tertiary prevention = managing complications (respiratory support, HRT for bone health, scoliosis management).

### 14. Other Species / Natural Disease
No naturally occurring *GGPS1* disease is reported in companion animals or wildlife (no OMIA entry described). Orthologs are highly conserved (Finding 9): mouse *Ggps1* (14593), rat (291211), zebrafish (336798), *Xenopus* (549876), *Drosophila* (38816), yeast *BTS1* (856036). No zoonotic potential (non-infectious genetic disease).

### 15. Model Organisms
**Disease-specific model:** a **p.Tyr259Cys knock-in mouse** (Foley et al., 2020) recapitulates dystrophic muscle histology (autophagic material, enlarged mitochondria) — good recapitulation of the muscle phenotype; hearing/ovarian phenotypes less characterized. **Conditional deletion mice:** skeletal-muscle-specific *Ggpps* knockout (insulin resistance via RhoA prenylation; [PMID: 26112408](https://pubmed.ncbi.nlm.nih.gov/26112408/)) and liver-specific knockout (adipose remodeling via Rab27A; [PMID: 32024826](https://pubmed.ncbi.nlm.nih.gov/32024826/)) — model gene function but not the exact human disease. **Limitation:** global null is lethal, so only hypomorphic/conditional models are informative. Model resources: MGI, IMPC, IMSR. Complementary in-vitro model: **patient-derived myogenic cells** showing the membrane-repair defect.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32403198](https://pubmed.ncbi.nlm.nih.gov/32403198/) | *GGPS1 Mutations Cause MDHLOV Syndrome* (Foley 2020) | **Landmark gene-discovery paper.** Supports Findings 1, 3, 8, 9 — WES/haplotype discovery, clinical triad, enzyme function, delayed membrane repair in patient cells, Y259C knock-in mouse. |
| [35869884](https://pubmed.ncbi.nlm.nih.gov/35869884/) | *GGPS1-associated MD with and without hearing loss* (Kaiyrzhanov 2022) | Supports Findings 2, 5 — 11 more patients; hearing loss in only 46%; establishes variable expressivity and "ultra-rare biallelic" nature. |
| [38129970](https://pubmed.ncbi.nlm.nih.gov/38129970/) | *Expanding the phenotypic/genotypic spectrum* (Altassan 2024) | Supports Finding 2 — isolated proximal weakness + elevated transaminases with spared hearing; adds hepatic involvement. |
| [12736685](https://pubmed.ncbi.nlm.nih.gov/12736685/) | *Defective membrane repair in dysferlin-deficient MD* (Bansal 2003) | Supports Finding 3 — establishes active Ca²⁺-dependent sarcolemmal repair as a disease-relevant muscle process. |
| [23663983](https://pubmed.ncbi.nlm.nih.gov/23663983/) | *Oligomerization of rab/effector complexes* | Supports Finding 3 — Rab GTPases require C-terminal prenylation for membrane tethering; explains downstream defect. |
| [26112408](https://pubmed.ncbi.nlm.nih.gov/26112408/) | *Lipid-induced muscle insulin resistance via GGPPS/RhoA* | Supports Finding 9 — skeletal-muscle *Ggpps* conditional KO; RhoA geranylgeranylation. |
| [32024826](https://pubmed.ncbi.nlm.nih.gov/32024826/) | *Liver governs adipose remodelling via EVs* | Supports Finding 9 — liver *Ggpps* KO; Rab27A geranylgeranylation controls EV secretion. |
| [31427080](https://pubmed.ncbi.nlm.nih.gov/31427080/) | *Crystal structure of GGPP synthase (crtE)* | Supports Finding 8 — homohexameric (trimer-of-dimers) architecture of GGPP synthases. |
| [42283975](https://pubmed.ncbi.nlm.nih.gov/42283975/) | *Comprehensive insights into Perrault syndrome* | Context — places *GGPS1* among 15 Perrault-syndrome genes; clinical/genetic heterogeneity. |
| [24784578](https://pubmed.ncbi.nlm.nih.gov/24784578/), [27286750](https://pubmed.ncbi.nlm.nih.gov/27286750/), [32087766](https://pubmed.ncbi.nlm.nih.gov/32087766/), [26911675](https://pubmed.ncbi.nlm.nih.gov/26911675/) | Dysferlin/Annexin-A5/AMPK/ANO5 membrane-repair studies | Context — mechanistic framework for vesicle-fusion-based sarcolemmal repair, the process inferred to fail here. |
| [36116551](https://pubmed.ncbi.nlm.nih.gov/36116551/), [40325959](https://pubmed.ncbi.nlm.nih.gov/40325959/) | Rab prenylation/localization; Rep-deficiency retinal degeneration | Context — consequences of failed Rab geranylgeranylation (membrane mislocalization, cell death). |

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** The entire disease description rests on ≈22 patients across three primary reports; prevalence, incidence, survival, and robust genotype-phenotype correlations cannot be estimated.
2. **Inferred (not demonstrated) extra-muscular mechanism.** The membrane-repair defect is directly shown only in muscle. The cochlear and ovarian branches are mechanistic inferences from the shared prenylation defect; the specific under-prenylated GTPases and cellular events in inner ear and ovary have not been experimentally defined.
3. **Which Rab/Rho substrates are limiting?** Direct proteomic/prenylomic evidence identifying the specific hypoprenylated small GTPases in patient tissues is lacking.
4. **VUS burden.** Several *GGPS1* alleles (p.Gly255Asp, p.Leu264Val, p.Leu182Pro) remain VUS; functional enzymatic assays are needed for reclassification.
5. **No therapeutic data.** No trials, no natural-history registry, and no validated biomarkers for progression beyond CK.
6. **Model gaps.** Knock-in mouse muscle phenotype is described, but auditory and ovarian phenotypes in the model are not fully characterized; global null lethality limits modeling of complete deficiency.

---

## Proposed Follow-up Experiments / Actions

1. **Prenylomics in patient cells/tissues** — quantify unprenylated Rab/Rho GTPases (e.g., in-vitro prenylation with biotin-geranylgeranyl) in patient myoblasts, and if accessible, cochlear/granulosa-cell models, to directly test step 4 of the causal chain.
2. **Phenotype the Y259C knock-in mouse for hearing and fertility** — ABR audiometry and ovarian histology/reproductive assays to test the cochlear and ovarian branches in vivo.
3. **iPSC-derived organoids** — patient-derived iPSC inner-ear organoids and ovarian/granulosa models to interrogate tissue-specific trafficking defects.
4. **Functional reclassification of VUS** — express VUS alleles and measure GGPP-synthase catalytic activity/thermostability to move VUS toward pathogenic/benign.
5. **GGPP/mevalonate-pathway rescue screens** — test whether GGPP supplementation, geranylgeraniol, or upstream pathway modulation rescues membrane-repair kinetics in patient myogenic cells (proof-of-concept for a metabolic therapy).
6. **International registry** — establish a natural-history registry (via Perrault-syndrome and congenital-muscular-dystrophy networks) to capture prevalence, progression, respiratory outcomes, and genotype-phenotype correlations.
7. **Structural modeling of hotspot residues** — map Phe257/Tyr259/Arg261/Val285 onto the GGPP-synthase active site (homology/AlphaFold) to explain why Arg261 is a mutational hotspot.

---

*Report compiled from 10 confirmed findings and 25 reviewed publications over 5 investigation iterations. Evidence types are human clinical (patient cohorts), model organism (mouse conditional/knock-in), and in vitro (patient-derived myogenic cells; bacterial/structural enzymology).*


## Artifacts

- [OpenScientist final report](Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Muscular_Dystrophy_Congenital_Hearing_Loss_And_Ovarian_Insufficiency_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 4 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:35869884`: "hearing loss was present in only 46% of the individuals … demonstrates that hearing loss and ovarian insufficiency might be a variable feature of the GGPS1-associated muscular dystrophy."
  - closest text in source: "This report consolidates the disease-causing role of biallelic variants in GGPS1 and demonstrates that hearing loss and ovarian insufficiency might be a variable feature of the GGPS1-associated muscular dystrophy"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31427080` (1 mention) - Crystal structure of geranylgeranyl pyrophosphate synthase (crtE) from Nonlabens dokdonensis DSW-6.
  - shared terms: none

Weighed against this report's own most characteristic terms: `ovarian`, `loss`, `hearing`, `ggps1`, `insufficiency`, `muscle`, `ggpp`, `patient`, `gene`, `disease`, `mouse`, `primary`, `sensorineural`, `respiratory`, `allele`, `congenital`, `cell`, `pathogenic`, `variant`, `disorder`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859189` (3 mentions) - the report calls it "Disease MONDO"; MONDO calls it **muscular dystrophy, congenital hearing loss, and ovarian insufficiency syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001844` (1 mention) - the report calls it "cochlea/inner ear"; UBERON calls it **cochlea**, and lists "cochlear organ" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.