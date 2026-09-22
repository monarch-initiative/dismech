---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T22:41:14.922209'
end_time: '2026-09-05T23:28:01.705233'
duration_seconds: 2806.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Spinocerebellar Ataxia 16
  mondo_id: MONDO:0014339
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
citation_count: 18
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0000765
    reported_labels:
    - Autonomic dysfunction
    ontology_label: Abnormal thorax morphology
  - term_id: UBERON:0002037
    reported_labels:
    - "Primary:** central nervous system \u2014 cerebellum"
    ontology_label: cerebellum
  - term_id: UBERON:0002298
    reported_labels:
    - Secondary/associated:** brainstem
    ontology_label: brainstem
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spinocerebellar Ataxia 16
- **MONDO ID:** MONDO:0014339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spinocerebellar Ataxia 16** covering all of the
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

# Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16): A Comprehensive Disease Characterization

**MONDO:** MONDO:0014339 · **OMIM:** #615768 · **Category:** Mendelian (autosomal recessive) · **Causal gene:** *STUB1* (CHIP)

---

## Summary

**Autosomal Recessive Spinocerebellar Ataxia 16 (SCAR16; OMIM #615768; MONDO:0014339)** is an ultra-rare autosomal-recessive neurodegenerative disorder caused by **biallelic loss-of-function mutations in *STUB1***, the gene encoding **CHIP** (C-terminus of HSC70-Interacting Protein), a dual-function E3 ubiquitin ligase and Hsp70/Hsp90 co-chaperone located on chromosome 16p13.3. The disease was defined molecularly in 2014, when a homozygous *STUB1* missense variant (c.737C>T, p.Thr246Met) was identified in a Gordon Holmes syndrome family and shown to abolish CHIP's ubiquitin-ligase activity, with CHIP loss in mice reproducing ataxia and hypogonadism [PMID: 24113144]. It has been confirmed in only a small number of kindreds worldwide (~16 reported by 2020) and accounts for roughly 0.4% of cerebellar-ataxia cohorts, marking it as an uncommon cause of hereditary ataxia.

Clinically, SCAR16 is a multisystem neurodegenerative syndrome whose core features are slowly progressive cerebellar ataxia with pyramidal tract signs, cognitive decline, hypogonadotropic hypogonadism (constituting the classic **Gordon Holmes syndrome**), and extrapyramidal features (dystonia, parkinsonism, chorea). Brain MRI shows marked cerebellar atrophy in essentially all patients. The phenotypic spectrum is unusually broad, ranging from isolated slowly progressive ataxia to severe encephalopathy with dementia, spastic tetraparesis, epilepsy and autonomic dysfunction, with an age of onset spanning childhood to late adulthood (14–76 years).

Mechanistically, the disease reflects a collapse of cellular protein-quality control. CHIP normally bridges molecular chaperones (via its TPR domain) and the ubiquitin–proteasome system (via its U-box domain), ubiquitinating client proteins such as tau for degradation and regulating mitophagy. Pathogenic *STUB1* variants abolish ligase activity, promote CHIP self-aggregation, permit tau aggregation, and dysregulate PINK1/Parkin-mediated mitochondrial quality control, converging on degeneration of vulnerable neurons—most conspicuously cerebellar Purkinje cells and hypothalamic GnRH neurons. *STUB1* forms a notable allelic series: the same gene causes dominant SCA48, the two forms overlap in a clinical continuum, and *STUB1* variants interact digenically with intermediate *TBP* polyglutamine expansions to modify SCA17/SCA48 penetrance. No disease-modifying therapy exists; management is symptomatic and supportive.

---

## Key Findings

### Finding 1 — SCAR16 is caused by biallelic loss-of-function *STUB1* (CHIP) mutations that abolish E3 ubiquitin ligase activity

The foundational discovery came from Shi et al. (2014), who identified a **homozygous *STUB1* mutation, c.737C>T (p.Thr246Met)** — reference NM_005861 — in a family with Gordon Holmes syndrome: *"identified a homozygous mutation in STUB1 (NM_005861) c.737C→T, p.Thr246Met, a gene that encodes the protein CHIP (C-terminus of HSC70-interacting protein)"* [PMID: 24113144]. The same study established the mechanism as **loss of function**: *"Introduction of the Thr246Met mutation into CHIP results in a loss of ubiquitin ligase activity measured directly using recombinant proteins as well as in cell culture models. Loss of CHIP function in mice resulted in behavioral and reproductive impairments that mimic human ataxia and hypogonadism"* [PMID: 24113144].

Subsequent families have repeatedly confirmed this paradigm. A Chinese SCAR16 patient carried a novel compound-heterozygous genotype (a truncating p.Gln118* nonsense variant with p.Lys145Gln), again abolishing ligase activity, with the report stating that *"SCAR16 is caused by mutations in the STIP1 homology and U-box containing protein 1 (STUB1) gene"* [PMID: 41851873]. *STUB1* maps to **chromosome 16p13.3** (HGNC:11427; UniProt Q9UNE7); the encoded 303-aa CHIP protein is both an E3 ubiquitin ligase and an Hsc70/Hsp90 co-chaperone.

**Ontology anchors:** *STUB1* (HGNC:11427); MONDO:0014339 / OMIM #615768; GO:0004842 (ubiquitin-protein transferase activity); GO:0031072 (heat shock protein binding).

### Finding 2 — Core clinical phenotype: progressive cerebellar ataxia plus pyramidal signs, cognitive decline, hypogonadism, and extrapyramidal features with cerebellar atrophy on MRI

The concise clinical definition is that SCAR16 *"is characterized by cerebellar ataxia accompanied by pyramidal tract damage, cognitive decline, hypogonadism, and extrapyramidal symptoms"* [PMID: 41851873]. The combination of cerebellar ataxia with hypogonadotropic hypogonadism corresponds to the classic eponymous **Gordon Holmes syndrome**.

Cohort studies delineate the breadth of presentation. In a French *STUB1* cohort, *"Phenotypic findings associated with STUB1 pathogenic variations cover a broad spectrum, ranging from isolated slowly progressive ataxia to severe encephalopathy, and include extrapyramidal features"*, and — critically for diagnosis — *"The age at onset was highly variable, ranging from 14 to 76 years. Brain MRI showed marked cerebellar atrophy in all patients"* [PMID: 33417001]. At the severe end, Hayer et al. reported that *"All three subjects presented with a severe multisystemic phenotype including severe dementia, spastic tetraparesis, epilepsy, and autonomic dysfunction in addition to cerebellar ataxia, plus hypogonadism in one index patient"*, with DTI revealing widespread supra- and infratentorial tract degeneration [PMID: 28193273]. The Taiwan cohort showed SCAR16 can present either as isolated cerebellar ataxia or with cognitive impairment, uniformly with marked cerebellar atrophy [PMID: 32367277].

**Suggested HPO terms:**

| Phenotype | HPO term | Notes / frequency |
|---|---|---|
| Cerebellar ataxia (gait & limb) | HP:0001251 | Core, near-universal |
| Progressive cerebellar atrophy (MRI) | HP:0001272 / HP:0006888 | Marked, essentially all patients |
| Pyramidal signs / spasticity | HP:0002061 / HP:0001257 | Common |
| Dysarthria | HP:0001260 | Common |
| Cognitive decline / dementia | HP:0001268 / HP:0000726 | Variable, up to severe |
| Hypogonadotropic hypogonadism | HP:0000044 | Gordon Holmes component |
| Dystonia / parkinsonism / chorea | HP:0001332 / HP:0001300 / HP:0002072 | Extrapyramidal, variable |
| Seizures / epilepsy | HP:0001250 | Severe end of spectrum |
| Dysphagia | HP:0002015 | Advanced disease |
| Autonomic dysfunction | HP:0000765 | Severe end of spectrum |
| Peripheral neuropathy | HP:0009830 | Reported in spectrum |

### Finding 3 — *STUB1*/CHIP allelic series spans recessive (SCAR16) and dominant (SCA48) ataxia, with a digenic *STUB1*–*TBP* interaction modifying SCA17 penetrance

*STUB1* causes disease under both inheritance models: **autosomal-recessive SCAR16 (OMIM #615768)** and **autosomal-dominant SCA48 (OMIM #618093)**. Ravel et al. reported *"the first pathogenic variation associated with both dominant and recessive forms of inheritance (SCAR16 and SCA48)"* and described a clinical continuum between the two [PMID: 33417001]. SCA48 typically presents as adult-onset ataxia with a prominent cerebellar cognitive-affective/psychiatric syndrome (CCAS), often with chorea, parkinsonism, dystonia, and characteristic dentate-nucleus T2 hyperintensity [PMID: 31126790].

A further layer of genetic complexity is the digenic interaction between *STUB1* and *TBP*. Magri et al. showed that co-occurrence of *STUB1* variants with intermediate *TBP* polyglutamine (CAG/CAA) expansions explains the incomplete penetrance of SCA17/SCA48: *"Our data reveal an unexpected genetic interaction between STUB1 and TBP in the pathogenesis of SCA17"* [PMID: 34906452]. This positions *STUB1* dosage/function as a modifier of a repeat-expansion ataxia, and *TBP* repeat length as a modifier of *STUB1* disease.

### Finding 4 — Mechanistic basis: CHIP is a Hsp70/Hsp90 co-chaperone E3 ligase that ubiquitinates client proteins including tau; its loss impairs proteostasis

CHIP has a modular architecture coupling chaperone recognition to ubiquitination: an **N-terminal TPR domain** that binds Hsc70/Hsp90 (IPR011990/PF00515) and a **C-terminal U-box domain** carrying E3 ligase activity (IPR003613/PF04564). Both are required for function: using estrogen receptor-α as a substrate, *"both the U-box (containing ubiquitin ligase activity) and the tetratricopeptide repeat (TPR, essential for chaperone binding) domains within CHIP are required for CHIP-mediated ERalpha down-regulation"* [PMID: 16037132].

A neurologically relevant client is **tau**. CHIP *"recognizes the microtubule-binding repeat region of tau and preferentially ubiquitylates four-repeat tau compared with three-repeat tau"*, promoting tau degradation, reducing detergent-insoluble tau, and accumulating in neurofibrillary-tangle–bearing neurons in tauopathy [PMID: 15447663]. This provides a mechanistic thread from *STUB1* loss of function to neurodegeneration via failed clearance of an aggregation-prone neuronal protein. Loss of CHIP also has consequences at mitochondria and the sarcoplasmic reticulum, with CHIP-deficient mice accumulating toxic oligomers and tubular aggregates in skeletal muscle [PMID: 28593200].

### Finding 5 — SCAR16 is a very rare early-onset spastic ataxia with a broad multisystem spectrum

De Michele et al. noted biallelic *STUB1*/SCAR16 had been *"so far reported in 16 kindreds"* (as of 2020) and characterized it as *"early onset spastic ataxia and a wide disease spectrum, including cognitive dysfunction, hyperkinetic disorders, epilepsy, peripheral neuropathy, and hypogonadism"* [PMID: 32342324]. In a Taiwanese cerebellar-ataxia cohort, *"SCAR16 seems to be an uncommon ataxic syndrome, accounting for 0.4% (2/512) of our cohort with cerebellar ataxia"* [PMID: 32367277]. Onset spans childhood to late adulthood (14–76 years across the SCAR16/SCA48 spectrum) [PMID: 33417001]. Many reported families are consanguineous with homozygous variants, and at least one case arose via **maternal uniparental isodisomy** of chromosome 16 [PMID: 39728009], producing homozygosity without both parents carrying the variant.

### Finding 6 — CHIP dysfunction converges on multiple proteostasis pathways: impaired mitophagy, tau aggregation, and STUB1 self-aggregation

Beyond simple loss of ligase activity, disease-associated CHIP mutations perturb several downstream processes:

1. **Mitophagy dysregulation.** CHIP restrains the PINK1/Parkin axis: *"we demonstrate that CHIP acts as a negative regulator of the PTEN-induced kinase 1 (PINK1)/Parkin-mediated mitophagy pathway"*, and *"multiple disease-associated mutations in CHIP dysregulate mitophagy both in vitro and in vivo in C. elegans neurons"* [PMID: 39117117].
2. **Tau aggregation.** A pathogenic CHIP variant (p.Y252S) reduces CHIP level, abolishes ligase activity, and *"could cause tau aggregation, which is considered to contribute to the progression of neurodegenerative disorders"* [PMID: 39707479].
3. **STUB1 self-aggregation.** Pathogenic mutants are prone to CARP-mediated mono-ubiquitination and aggregation: *"pathogenic mutants of STUB1 are more prone than the wild-type to CARP2-mediated aggregate assembly"* [PMID: 36853170].
4. **Mitochondrial/SR pathology.** CHIP-null mice accumulate toxic oligomers and tubular aggregates in muscle, reflecting broad proteostatic failure [PMID: 28593200].

**Ontology anchors:** GO:0000423 (mitophagy); GO:0006914 (autophagy); GO:0043161 (proteasome-mediated ubiquitin-dependent protein catabolism); GO:0016567 (protein ubiquitination).

### Finding 7 — Model organisms recapitulate SCAR16

| Model | Genetic manipulation | Key phenotype | PMID |
|---|---|---|---|
| Mouse (*Mus musculus*, taxon 10090; *Stub1*, Gene 56424) | CHIP loss-of-function / knockout | Behavioral + reproductive impairment mimicking ataxia and hypogonadism; muscle mitochondrial/SR aggregates | [24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/); [28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/) |
| Zebrafish (*Danio rerio*, taxon 7955) | Chip U-box domain truncation | Altered Purkinje neuron morphology; behavioral changes | [34630034](https://pubmed.ncbi.nlm.nih.gov/34630034/) |
| C. elegans (taxon 6239) | Disease-associated CHIP mutations | Dysregulated neuronal mitophagy in vivo | [39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/) |
| Patient iPSCs | Compound-het *STUB1* (c.355C>T, c.880A>T) | Reprogrammed, tri-lineage differentiation | [29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/) |
| iPSC-neurons vs fibroblasts | Patient CHIP mutations | Cell-type-dependent altered heat-shock response | [33097556](https://pubmed.ncbi.nlm.nih.gov/33097556/) |

The mouse model reproduces the core Gordon Holmes phenotype: *"Loss of CHIP function in mice resulted in behavioral and reproductive impairments that mimic human ataxia and hypogonadism"* [PMID: 24113144]. A patient iPSC line was generated *"from a 12-year-old male patient with recessive spinocerebellar ataxia type 16 (OMIM #615768), carrying compound heterozygous mutations (c.355C>T, c.880A>T) in STUB1"* [PMID: 29679845]. The zebrafish U-box truncation directly implicates the Purkinje cell.

### Finding 8 — Diagnosis relies on next-generation sequencing plus MRI cerebellar atrophy, with functional assays to classify variants

Diagnosis is fundamentally genetic. Whole-exome sequencing — often with Sanger confirmation and, for allele phasing of compound/structural variants, long-range PCR — identifies biallelic *STUB1* variants: *"The whole-exome sequencing combined with long-range flanking polymerase chain reaction (PCR) were performed in a Chinese SCAR16 patient"* [PMID: 41851873]. Brain MRI is the key supportive test: *"The brain MRIs showed a marked cerebellar atrophy of the patients"* [PMID: 32367277], often extending to the brainstem [PMID: 36569391].

Imaging helps distinguish recessive SCAR16 from dominant SCA48: dentate-nucleus T2 hyperintensity is more typical of SCA48 — *"MRI showed a significant cerebellar atrophy, coupled to a T2-weighted hyperintensity affecting the dentate nuclei and extending to the middle cerebellar peduncles"* [PMID: 31126790]. Because many *STUB1* variants are missense VUS, **functional validation** (Western blot showing reduced/truncated CHIP; in vitro ubiquitin-ligase and tau-aggregation assays) establishes pathogenicity per ACMG [PMID: 41851873; PMID: 39707479]. Concurrent *TBP* repeat testing is advised given the digenic interaction [PMID: 34906452]. No specific blood/CSF biomarker exists; endocrine work-up (LH, FSH, sex hormones) evaluates hypogonadism.

### Finding 9 — SCAR16 is slowly progressive with no disease-modifying therapy; management is symptomatic and supportive

Across cohorts, SCAR16/*STUB1* disease is a **slowly progressive cerebellar ataxia** — *"All presented with slowly progressive cerebellar ataxia"* [PMID: 33417001] — though onset and severity are highly variable, from isolated ataxia to severe encephalopathy with *"severe dementia, spastic tetraparesis, epilepsy, and autonomic dysfunction in addition to cerebellar ataxia"* [PMID: 28193273]. Because the mechanism is loss of CHIP proteostasis function, there is **no curative or disease-modifying treatment**. Care is symptomatic and multidisciplinary: physiotherapy, occupational therapy and speech/swallowing therapy for ataxia and dysarthria; sex-hormone replacement for hypogonadism; and standard management of spasticity, dystonia/parkinsonism, seizures and dysphagia. Prognosis is driven by progressive disability (loss of independent ambulation) rather than a single defined survival figure.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *STUB1*** (missense abolishing catalysis, nonsense/frameshift truncation, or start-loss) *results in* absent or non-functional CHIP. *(Demonstrated: recombinant/cell ligase assays, Western blot — PMID: 24113144, 41851873.)*
2. Loss of CHIP's **U-box E3 ligase activity** and **TPR-mediated chaperone coupling** *leads to* failure to ubiquitinate and degrade chaperone-bound client proteins. *(Demonstrated for ERα and tau — PMID: 16037132, 15447663.)*
3. Impaired client clearance *results in* **accumulation/aggregation of substrates (e.g., four-repeat tau)** and **self-aggregation of mutant CHIP**. *(Demonstrated in vitro — PMID: 39707479, 36853170.)*
4. In parallel, loss of CHIP's negative regulation of the **PINK1/Parkin axis** *leads to* **dysregulated mitophagy** and mitochondrial/SR quality-control failure. *(Demonstrated in C. elegans neurons and CHIP-null mice — PMID: 39117117, 28593200.)*
5. Combined proteostatic and mitochondrial stress *results in* **degeneration of vulnerable neurons** — cerebellar Purkinje cells (branch A) and hypothalamic GnRH neurons (branch B). *(Purkinje: zebrafish U-box truncation — PMID: 34630034; GnRH/reproductive: inferred from hypogonadism + CHIP-null reproductive impairment — PMID: 24113144.)*
6. **Branch A — cerebellar Purkinje-cell loss** *leads to* progressive ataxia, dysarthria and MRI-visible cerebellar atrophy; corticospinal/extrapyramidal degeneration *leads to* pyramidal signs, dystonia, parkinsonism and chorea; cortical involvement *leads to* cognitive decline.
7. **Branch B — hypothalamic-pituitary GnRH-neuron dysfunction** *leads to* hypogonadotropic hypogonadism, completing Gordon Holmes syndrome.

```
   Biallelic STUB1 LoF
           |
   Loss of CHIP function (U-box ligase + TPR chaperone coupling)
           |
   -----------------------------------------
   |                                       |
 Failed client ubiquitination        Loss of PINK1/Parkin
 (tau, ERα) + CHIP self-aggregation   negative regulation
   |                                       |
 Protein aggregation                 Dysregulated mitophagy
   |                                       |
   -----------------------------------------
                     |
        Neuronal proteostatic + mitochondrial stress
                     |
        --------------------------------
        |                              |
  Purkinje / CNS neuron loss     GnRH neuron dysfunction
        |                              |
  Ataxia, pyramidal signs,       Hypogonadotropic
  cognitive decline,             hypogonadism
  extrapyramidal features,
  cerebellar atrophy on MRI
        \______________  ____________/
                       \/
              Gordon Holmes syndrome / SCAR16
```

**Upstream vs downstream:** The upstream lesion is loss of CHIP catalytic/co-chaperone function. Downstream consequences bifurcate into (a) a ubiquitin–proteasome/aggregation arm and (b) a mitophagy/mitochondrial arm, both feeding a common node of neuronal stress. **Cell types:** cerebellar Purkinje neurons (CL:0000121), hypothalamic GnRH neurons, broader CNS/upper motor neurons; skeletal myofibers show aggregate pathology in models. **Subcellular compartments:** cytosol/proteasome (GO:0000502), mitochondria (GO:0005739), chaperone machinery. **Pathways:** KEGG hsa04120 (ubiquitin-mediated proteolysis); Reactome mitophagy (PINK1/Parkin) and HSP90 chaperone cycle; EC 2.3.2.27 (U-box E3 ligase). **Key GO processes:** GO:0016567, GO:0000423, GO:0043161, GO:0034976.

### Anatomical structures affected

- **Primary:** central nervous system — cerebellum (UBERON:0002037), especially cortex/Purkinje layer, vermis and hemispheres.
- **Secondary/associated:** brainstem (UBERON:0002298), corticospinal/pyramidal tracts, cerebral cortex (cognition), basal ganglia circuits (extrapyramidal), hypothalamus (UBERON:0001898)/hypothalamic-pituitary-gonadal axis.
- **Lateralization:** bilateral, largely symmetric cerebellar atrophy.

---

## Evidence Base

| PMID | Title (abbreviated) | Support for findings |
|---|---|---|
| [24113144](https://pubmed.ncbi.nlm.nih.gov/24113144/) | *Ataxia and hypogonadism caused by loss of ubiquitin ligase activity of the U-box protein CHIP* | Landmark: identifies *STUB1*/CHIP (p.Thr246Met), demonstrates LoF, mouse phenocopy (F1, F4, F7) |
| [41851873](https://pubmed.ncbi.nlm.nih.gov/41851873/) | *Novel STUB1 p.(Gln118*) nonsense variant causing SCAR16* | Confirms gene/phenotype; WES + long-range PCR diagnostics; truncating LoF (F1, F2, F8) |
| [33417001](https://pubmed.ncbi.nlm.nih.gov/33417001/) | *Expanding the clinical spectrum of STUB1-associated ataxia* | Phenotype spectrum, 14–76 y onset, universal cerebellar atrophy, one variant → both SCAR16 & SCA48 (F2, F3, F9) |
| [28193273](https://pubmed.ncbi.nlm.nih.gov/28193273/) | *STUB1/CHIP mutations cause Gordon Holmes syndrome / multisystemic neurodegeneration* | Severe end of spectrum (F2, F9) |
| [34906452](https://pubmed.ncbi.nlm.nih.gov/34906452/) | *Digenic inheritance of STUB1 variants and TBP polyQ expansions* | STUB1–TBP digenic interaction (F3) |
| [31126790](https://pubmed.ncbi.nlm.nih.gov/31126790/) | *SCA48 in two Italian families* | Dominant SCA48 phenotype; dentate T2 hyperintensity distinguishing feature (F3, F8) |
| [16037132](https://pubmed.ncbi.nlm.nih.gov/16037132/) | *CHIP promotes degradation of estrogen receptor-alpha* | CHIP domain architecture (TPR + U-box) both required (F4) |
| [15447663](https://pubmed.ncbi.nlm.nih.gov/15447663/) | *CHIP poly-ubiquitylates four-repeat tau* | Tau as CHIP substrate; tauopathy link (F4, F6) |
| [39117117](https://pubmed.ncbi.nlm.nih.gov/39117117/) | *CHIP mutations impair negative regulation of mitophagy* | CHIP regulates PINK1/Parkin mitophagy; disease mutations dysregulate it (F6, F7) |
| [39707479](https://pubmed.ncbi.nlm.nih.gov/39707479/) | *Novel STUB1 mutation in a Chinese SCA48 pedigree* | Pathogenic CHIP variant → tau aggregation, reduced ligase activity (F6, F8) |
| [36853170](https://pubmed.ncbi.nlm.nih.gov/36853170/) | *CARPs regulate STUB1 mutant aggregation by mono-ubiquitination* | Mutant STUB1 self-aggregation (F6) |
| [28593200](https://pubmed.ncbi.nlm.nih.gov/28593200/) | *Skeletal muscle mitochondrial alterations in CHIP-/- mice* | Aggregate/mitochondrial pathology in CHIP-null model (F4, F6, F7) |
| [32367277](https://pubmed.ncbi.nlm.nih.gov/32367277/) | *SCAR16 in Taiwan* | Rarity (0.4%, 2/512); MRI cerebellar atrophy (F5, F8) |
| [32342324](https://pubmed.ncbi.nlm.nih.gov/32342324/) | *SCA48: last but not least* | SCAR16 in ~16 kindreds; wide spectrum (F5, F9) |
| [29679845](https://pubmed.ncbi.nlm.nih.gov/29679845/) | *STUB1/CHIP mutant iPSCs from a SCAR16 patient* | Patient-derived iPSC model (F7) |
| [34630034](https://pubmed.ncbi.nlm.nih.gov/34630034/) | *Chip U-box truncation affects Purkinje neuron morphology (zebrafish)* | Implicates Purkinje cells; in vivo vertebrate model (F7) |
| [39728009](https://pubmed.ncbi.nlm.nih.gov/39728009/) | *SCAR16 caused by maternal uniparental isodisomy* | Alternative route to biallelic *STUB1* (F5) |
| [36569391](https://pubmed.ncbi.nlm.nih.gov/36569391/) | *MRI findings in SCAR-16 STUB1 ataxia* | Cerebellar + brainstem atrophy; SCAR16 vs SCA48 imaging (F8) |
| [33097556](https://pubmed.ncbi.nlm.nih.gov/33097556/) | *CHIP mutations affect heat-shock response in fibroblasts vs iPSC-neurons* | Cell-type-specific proteostasis consequences (F7) |
| [33811518](https://pubmed.ncbi.nlm.nih.gov/33811518/) | *De novo STUB1 start-lost variant, multisystemic ataxia* | Supports LoF mechanism; mirrors systems affected in dominant disease |

**Evidence source types:** Human clinical cohorts/case reports (24113144, 41851873, 33417001, 28193273, 32367277, 32342324, 36569391, 39728009); in vitro/biochemical (16037132, 15447663, 36853170, 39707479); model organism (24113144 mouse, 34630034 zebrafish, 39117117 C. elegans, 28593200 mouse); cellular/iPSC (29679845, 33097556).

---

## Section-by-Section Reference (Research Template)

- **1. Disease information:** SCAR16 = autosomal recessive spinocerebellar ataxia 16 / STUB1-related ataxia / CHIP-related ataxia / Gordon Holmes syndrome (when with hypogonadism). Identifiers: OMIM #615768; MONDO:0014339; *STUB1* (HGNC:11427; NCBI Gene 10273; 16p13.3); Orphanet SCAR16; ICD-11 8A03 / ICD-10 G11; MeSH Spinocerebellar Ataxias. Related loci: SCA48 (OMIM #618093), SCA17-digenic. Source = aggregated case-level literature.
- **2. Etiology:** Monogenic — biallelic loss-of-function *STUB1* variants. Consanguinity and uniparental isodisomy are routes to homozygosity. Intermediate *TBP* polyQ length is a genetic modifier. No environmental/infectious/protective factors.
- **3. Phenotypes:** See Finding 2 table (HPO terms). Onset childhood–late adult; slowly progressive; variable severity. No validated disease-specific QoL instrument (SARA grades ataxia severity).
- **4. Genetic/molecular:** *STUB1* on 16p13.3; variant classes: missense (p.Thr246Met, p.Lys145Gln, p.Arg241Trp, p.Cys232Gly, p.Y252S), nonsense (p.Gln118*), start-loss (c.3G>A), compound het (c.355C>T + c.880A>T). Germline only; rare in gnomAD. Functional consequence = loss of function. *TBP* modifier; UPD reported.
- **5. Environmental:** None implicated — purely Mendelian.
- **6. Mechanism:** See Mechanistic Model (proteostasis + mitophagy failure → neuronal degeneration).
- **7. Anatomy:** Cerebellum (Purkinje layer) primary; brainstem, pyramidal tracts, cortex, basal ganglia, HPG axis secondary; bilateral/symmetric.
- **8. Temporal development:** Insidious onset; chronic, slowly progressive, lifelong; no remission.
- **9. Inheritance/population:** Autosomal recessive (allelic dominant SCA48); ultra-rare (~16 kindreds by 2020; 0.4% of an ataxia cohort; est. <1/1,000,000). Highly penetrant with variable expressivity. Reported across East Asian and European populations; no strong sex bias for ataxia.
- **10. Diagnostics:** WES/WGS or ataxia panel identifying biallelic *STUB1* + MRI cerebellar atrophy; functional assays for VUS; concurrent *TBP* testing; endocrine work-up. Differential: other AR ataxias, SCA17, other GHS genes (*RNF216, OTUD4, PNPLA6*), SCA48.
- **11. Prognosis:** Chronic progressive disability; no defined survival statistic; severe encephalopathic cases at poor-outcome end.
- **12. Treatment:** Symptomatic/supportive only (rehabilitation, hormone replacement, symptomatic pharmacotherapy). No approved gene/RNA/cell therapy; gene replacement is a rational future LoF strategy.
- **13. Prevention:** Genetic counseling, carrier/cascade testing, prenatal/preimplantation options; no population screening or immunization.
- **14. Other species:** Highly conserved *STUB1*/CHIP; mouse *Stub1* (Gene 56424), zebrafish *stub1*, *C. elegans chn-1*. No documented natural companion-animal/wildlife equivalent (no OMIA entry); non-zoonotic.
- **15. Model organisms:** See Finding 7 table. Mouse best recapitulates ataxia+hypogonadism; zebrafish links ligase loss to Purkinje cells; no single model reproduces the full human multisystem spectrum. Resources: MGI, ZFIN, WormBase, Cellosaurus.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** With ~16–20 reported kindreds worldwide, epidemiological parameters (precise prevalence, incidence, carrier frequency, penetrance, sex ratio) are not robustly established. The 0.4% cohort figure derives from a single Taiwanese series.
2. **Incomplete genotype–phenotype correlation.** The extreme variability in onset (14–76 y) and severity (isolated ataxia to fatal encephalopathy) is unexplained; modifiers beyond *TBP* are likely but uncharacterized.
3. **GnRH-neuron mechanism inferred.** Hypogonadism is attributed to hypothalamic GnRH-neuron dysfunction from phenotype and mouse reproductive impairment, but direct human cell-type-specific evidence is lacking.
4. **No validated biomarkers.** MRI cerebellar atrophy is supportive but nonspecific; no fluid biomarker exists for diagnosis, progression, or treatment response.
5. **No therapeutic evidence.** No clinical trials or disease-modifying interventions; all treatment recommendations are supportive/extrapolated.
6. **Recessive vs dominant boundary blurred.** The SCAR16–SCA48 continuum and the role of dominant-negative vs haploinsufficient effects remain unresolved.

---

## Proposed Follow-up Experiments / Actions

1. **International natural-history registry.** Pool scattered kindreds (SARA scores, MRI volumetrics, endocrine panels) to quantify progression rate, onset distribution, and survival.
2. **Genotype–phenotype and modifier study.** Systematically genotype *TBP* repeats and candidate modifiers (chaperone/proteostasis network) across all *STUB1* patients to explain phenotypic variability and penetrance.
3. **Functional VUS pipeline.** Standardize an assay battery (ligase activity, tau aggregation, mitophagy, CHIP self-aggregation) to reclassify missense VUS per ACMG PS3/BS3.
4. **Cerebellar organoid / iPSC-Purkinje models.** Extend patient iPSC work to Purkinje-enriched organoids to define cell-type-specific proteostasis/mitophagy defects and screen candidate small molecules (chaperone inducers, mitophagy enhancers).
5. **Biomarker discovery.** Apply CSF/plasma proteomics (tau species, neurofilament light) to identify diagnostic/progression biomarkers.
6. **Preclinical therapeutic testing.** Use CHIP-null mice, U-box-truncated zebrafish and *chn-1* C. elegans to test proteostasis-restoring and mitophagy-modulating interventions.
7. **Endocrine mechanism.** Characterize GnRH-neuron development/function in CHIP-loss models to confirm the hypogonadism mechanism and guide hormone-replacement timing.

---

*Report compiled from 9 confirmed findings and 32 reviewed papers. All mechanistic and clinical claims are anchored to primary literature with verified abstract quotations; ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) support downstream knowledge-base curation.*


## Artifacts

- [OpenScientist final report](Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Recessive_Spinocerebellar_Ataxia_16-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000765` (1 mention) - the report calls it "Autonomic dysfunction"; HP calls it **Abnormal thorax morphology**
- `UBERON:0002037` (1 mention) - the report calls it "Primary:** central nervous system — cerebellum"; UBERON calls it **cerebellum**
- `UBERON:0002298` (1 mention) - the report calls it "Secondary/associated:** brainstem"; UBERON calls it **brainstem**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001251` (1 mention) - the report calls it "Cerebellar ataxia (gait & limb)"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `GO:0043161` (2 mentions) - the report calls it "proteasome-mediated ubiquitin-dependent protein catabolism"; GO calls it **proteasome-mediated ubiquitin-dependent protein catabolic process**