---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T19:15:04.509661'
end_time: '2026-09-04T19:34:27.391074'
duration_seconds: 1162.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spondylo-megaepiphyseal-metaphyseal Dysplasia
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 9
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:10572046
  relevance_assessed: 14
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:17310243
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013228
    reported_labels:
    - MONDO
    ontology_label: spondylo-megaepiphyseal-metaphyseal dysplasia
  - term_id: HP:0006262
    reported_labels:
    - Pseudoepiphyses of the hand bones
    ontology_label: Aplasia/Hypoplasia of the 5th finger
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
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
  path: Spondylo-megaepiphyseal-metaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spondylo-megaepiphyseal-metaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondylo-megaepiphyseal-metaphyseal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondylo-megaepiphyseal-metaphyseal Dysplasia** covering all of the
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

# Spondylo-Megaepiphyseal-Metaphyseal Dysplasia (SMMD): A Comprehensive Disease Characteristics Report

**Disease:** Spondylo-megaepiphyseal-metaphyseal dysplasia (SMMD)
**MONDO:** MONDO:0013228 · **OMIM:** 613330 · **Orphanet:** ORPHA:228387 · **MeSH:** C567639 · **GARD:** 0017154 · **UMLS:** C2750066 · **MedGen:** 412869
**Causal gene:** *NKX3-2* (formerly *BAPX1*), HGNC:951, 4p15.33
**Category:** Mendelian (autosomal recessive)

*Autonomous literature-based discovery report. Evidence note: SMMD is an ultra-rare disorder with only a small number of molecularly/clinically documented patients worldwide. Nearly all clinical evidence derives from small case series and single-case reports (human clinical, descriptive), while mechanistic understanding comes from mouse, chick, and zebrafish developmental biology (model organism / in vitro).*

---

## Summary

Spondylo-megaepiphyseal-metaphyseal dysplasia (SMMD) is an ultra-rare, autosomal recessive skeletal dysplasia caused by biallelic loss-of-function (LoF) mutations in *NKX3-2* (BAPX1), a homeobox transcription factor located on chromosome 4p15.33. The disease is defined by a characteristic disproportion — a short trunk and short neck combined with relatively long limbs — together with a distinctive radiographic picture of delayed/absent vertebral ossification with sagittal and coronal clefts, large "balloon-like" (mega-) epiphyses, wide/abnormal metaphyses, absent pubic ossification, and multiple pseudoepiphyses of the hand and foot tubular bones. The single most clinically important complication is **cervical spine instability with spinal cord compression**, which drives major morbidity and can be life-threatening.

Mechanistically, NKX3-2 sits at the center of the sclerotome-to-cartilage developmental program. It is induced during sclerotome specification by Sonic hedgehog (SHH) signaling combined with BMP antagonism (Noggin), acting upstream of the master chondrogenic transcription factor SOX9. Within the growth plate, NKX3-2 functions downstream of PTHrP to repress the pro-hypertrophy factor RUNX2, thereby restraining premature chondrocyte maturation; independently, it sustains the survival of proliferating chondrocytes through ligand-independent activation of RelA/NF-κB. Biallelic loss of NKX3-2 therefore removes a maturation brake and a survival signal simultaneously, disrupting endochondral ossification and producing the skeletal phenotype. gnomAD constraint metrics (pLI ≈ 0, LOEUF ≈ 1.07) confirm that a single functional allele is sufficient (haplosufficiency), which explains the recessive inheritance pattern — disease requires loss of *both* alleles.

There is no disease-modifying therapy. Management is supportive and centers on early recognition and surveillance of cervical spine instability, surgical stabilization when indicated, respiratory and orthopedic care, and genetic counseling for affected families. Animal models — the *Bapx1*-null mouse and a zebrafish *nkx3.2* mutant — recapitulate the core axial skeletal defects and have illuminated both embryonic and post-embryonic roles of the gene, providing platforms for future mechanistic and therapeutic study.

---

## Section-by-Section Report

### 1. Disease Information

SMMD is a Mendelian skeletal dysplasia affecting the spine (spondylo-), the epiphyses (which become abnormally large — megaepiphyseal), and the metaphyses (metaphyseal). Affected individuals present in infancy/early childhood with disproportionate short stature (short trunk and neck, comparatively long limbs), joint limitation, and progressive skeletal deformity. The disease is characterized clinically and radiographically rather than biochemically.

**Key identifiers (verified programmatically via EBI OLS4 and HGNC REST — Finding F007):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013228 |
| OMIM (phenotype) | 613330 |
| Orphanet | ORPHA:228387 |
| MeSH | C567639 |
| GARD | 0017154 |
| UMLS | C2750066 |
| MedGen | 412869 |
| Gene (HGNC) | HGNC:951 (*NKX3-2*) |
| Gene (NCBI) | 579 |
| Gene (Ensembl) | ENSG00000109705 |
| Gene (UniProt) | P78367 |
| Gene OMIM | *602183 |
| Cytoband | 4p15.33 |

**Synonyms / alternative names:** SMMD; spondylomegaepiphyseal-metaphyseal dysplasia. The causal gene was historically named *BAPX1* (bagpipe homeobox homolog 1), with aliases *NKX3B* and *NKX3.2*.

**Data source type:** Information is derived from aggregated disease-level resources (OMIM, Orphanet, Mondo) and small published patient case series/reports rather than large EHR cohorts, reflecting the disease's rarity.

---

### 2. Etiology

**Disease causal factors — genetic.** SMMD is a monogenic disorder caused by biallelic inactivating (loss-of-function) mutations in *NKX3-2* (Finding F001). Genome-wide homozygosity mapping combined with candidate-gene sequencing in three consanguineous families identified three distinct homozygous inactivating mutations in *NKX3-2* on chromosome 4p15.33 [PMID: 20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/). A later perinatal-lethal neonatal case carried the homozygous frameshift variant c.507-508delCA (p.Gly171Cysfs*55) in exon 2 [PMID: 29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/).

> "Each proband was homozygous for a different inactivating mutation in NKX3-2, a homeobox-containing gene located on chromosome 4p15.33." — [PMID: 20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/)

**Genetic risk factors.** The only established risk factor is inheritance of two loss-of-function *NKX3-2* alleles. **Consanguinity** is a major contributor: the founding cases were identified in consanguineous families through homozygosity mapping, and consanguineous unions increase the probability of homozygosity for a rare recessive allele. Heterozygous carriers are unaffected (see gnomAD constraint, Finding F008).

**Environmental risk factors.** None identified or expected — this is a fully penetrant Mendelian developmental disorder. Age, sex, and lifestyle exposures are not causal contributors.

**Protective factors.** No genetic or environmental protective factors are described. Because a single intact allele is sufficient for normal development (haplosufficiency), the presence of one functional *NKX3-2* allele is fully "protective" in carriers.

**Gene–environment interactions.** None documented; the phenotype is driven by the developmental genetic lesion.

---

### 3. Phenotypes

SMMD phenotypes are physical/skeletal manifestations and clinical/neurological signs. The characteristic radiographic and clinical features derive largely from the six-patient series of Simon et al. and related reports (Finding F003).

| Phenotype | Type | Onset | Severity/Progression | Suggested HPO term |
|---|---|---|---|---|
| Disproportionate short stature (short trunk/neck, long limbs) | Physical manifestation | Congenital/infancy | Moderate–severe, progressive | HP:0004322 (Short stature); HP:0003521 (Disproportionate short-trunk short stature) |
| Delayed/absent vertebral body ossification with sagittal & coronal clefts | Radiographic sign | Congenital | Severe | HP:0008428 (Abnormal vertebral ossification); HP:0003312 (Abnormal form of the vertebral bodies) |
| Cervical spine instability ("swan-neck" deformity, kyknodysostosis) | Clinical/radiographic sign | Early childhood | Severe, progressive | HP:0003316 (Abnormality of the cervical spine); HP:0008443 (Cervical instability) |
| Cervical cord injury → limb spasticity | Neurological sign | Childhood | Severe; life-threatening | HP:0001257 (Spasticity); HP:0002385 (Paraparesis) |
| Large "balloon-like" (mega-) epiphyses of long bones | Radiographic sign | Childhood | — | HP:0003065 (Epiphyseal dysplasia); HP:0010577 (Enlarged epiphyses) |
| Metaphyseal abnormalities | Radiographic sign | Childhood | — | HP:0000944 (Abnormal metaphysis) |
| Multiple pseudoepiphyses of metacarpals/phalanges | Radiographic sign | Childhood | — | HP:0006262 (Pseudoepiphyses of the hand bones) |
| Absent/delayed pubic bone ossification | Radiographic sign | Congenital | — | HP:0008788 (Delayed pubic bone ossification) |
| Perinatal lethality (severe end of spectrum) | Outcome | Neonatal | Fatal | HP:0001522 (Death in infancy) |

> "Radiographs show a severe ossification delay of the vertebral bodies with sagittal and coronal clefts, missing ossification of the pubic bones, large round 'balloon-like' epiphyses of the long bones, and presence of multiple pseudoepiphyses at all metacarpals and phalanges." — [PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)

**Quality-of-life impact.** Cervical cord compression causing spasticity has profound effects on mobility and daily function; short stature and skeletal deformity affect ambulation and independence. No formal EQ-5D/SF-36 data exist for this ultra-rare disease.

---

### 4. Genetic / Molecular Information

**Causal gene.** *NKX3-2* (BAPX1), HGNC:951, NCBI Gene 579, Ensembl ENSG00000109705, UniProt P78367, gene OMIM *602183, cytoband 4p15.33. NKX3-2 is a NK-family homeobox transcription factor.

**Pathogenic variants (Findings F001, F008).**

| Variant | Type | Consequence | Classification | Reference |
|---|---|---|---|---|
| Three distinct homozygous inactivating mutations (3 families) | Inactivating/LoF | Loss of function | Pathogenic | [PMID: 20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/) |
| c.507-508delCA (p.Gly171Cysfs*55), exon 2 | Frameshift deletion | LoF / truncation | Pathogenic (perinatal-lethal) | [PMID: 29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/) |

- **Variant classification:** Pathogenic (biallelic LoF) per ACMG framework (null variants in a gene where LoF is the established mechanism).
- **Variant type/class:** Inactivating LoF, including frameshift/truncating variants.
- **Origin:** Germline.
- **Functional consequence:** Loss of function of the NKX3-2 transcription factor.
- **Allele frequency:** Extremely rare / private variants; not present at appreciable frequency in population databases.

**gnomAD constraint (Finding F008).** For *NKX3-2* (ENSG00000109705, GRCh38): pLI = 0.0009 (LoF-tolerant, not haploinsufficient); LOEUF = 1.07; observed/expected LoF point estimate = 0.67 (13 observed vs 19.4 expected); missense Z = −1.42 (no missense constraint). These metrics confirm that heterozygous LoF is tolerated in the general population, consistent with **haplosufficiency** and the recessive inheritance of SMMD.

**Modifier genes.** *NKX3-1* is a functionally overlapping paralog: in mouse, *Nkx3.1/Nkx3.2* double-null embryos show enhanced vertebral defects and embryonic lethality (E12.5–E17.5) beyond the *Bapx1* single-null phenotype [PMID: 12204261](https://pubmed.ncbi.nlm.nih.gov/12204261/), indicating partial redundancy. Whether *NKX3-1* modifies human SMMD severity is not established. Upstream regulators *Meox1/Meox2* directly activate *Bapx1* transcription and are required for sclerotomal *Bapx1* expression [PMID: 15024065](https://pubmed.ncbi.nlm.nih.gov/15024065/); *MEOX1* loss remodels cranio-cervical joints and alters *Bapx1* expression [PMID: 19520072](https://pubmed.ncbi.nlm.nih.gov/19520072/).

**Epigenetic information / chromosomal abnormalities.** No disease-specific epigenetic signatures or large-scale chromosomal abnormalities are reported; SMMD is caused by point/small LoF mutations rather than structural variants.

---

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in SMMD. It is a purely genetic developmental disorder. This section is **not applicable** beyond noting that consanguinity (a demographic/social factor, not an environmental exposure) increases recessive-disease risk.

---

### 6. Mechanism / Pathophysiology

#### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *NKX3-2*** (germline) → complete loss of functional NKX3-2 transcription factor in developing skeleton (demonstrated; [PMID: 20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/)).
2. Loss of NKX3-2 → **failure of the normal sclerotome→chondrogenesis program**. Normally SHH + BMP-antagonism induce *Pax1/Bapx1(NKX3-2)*, which acts upstream of *Sox9* to launch chondrogenesis; without NKX3-2 this program is impaired (demonstrated in ESC model; [PMID: 25294938](https://pubmed.ncbi.nlm.nih.gov/25294938/)).
3. **Branch A — loss of maturation brake:** NKX3-2 normally represses *RUNX2* downstream of PTHrP to keep chondrocytes proliferating. Its loss → **derepression of RUNX2** → dysregulated/premature chondrocyte maturation (demonstrated in growth-plate models; [PMID: 16421188](https://pubmed.ncbi.nlm.nih.gov/16421188/)).
4. **Branch B — loss of survival signal:** NKX3-2 normally sustains proliferating-chondrocyte viability via ligand-independent RelA/NF-κB activation. Its loss → **reduced chondrocyte survival** (demonstrated in vitro; [PMID: 17310243](https://pubmed.ncbi.nlm.nih.gov/17310243/)).
5. Branches A + B converge → **downregulation of the chondrogenic gene network** (Sox9, Col2a1, Fgfr3, Ihh, Runx2) and failure of normal cartilage differentiation (demonstrated in *Bapx1*-null mouse; [PMID: 10572046](https://pubmed.ncbi.nlm.nih.gov/10572046/)).
6. Disrupted cartilage template → **defective endochondral ossification** of vertebrae, epiphyses, and metaphyses → delayed/cleft vertebral ossification, mega-epiphyses, abnormal metaphyses, pseudoepiphyses, absent pubic ossification (inferred from radiographic phenotype; [PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)).
7. Poor cervical vertebral ossification → **cervical spine instability** ("swan-neck"/kyknodysostosis) → **spinal cord compression** → limb spasticity and neurological compromise (demonstrated clinically in 5/6 patients; [PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)).
8. (Severe genotypes) → perinatal lethality (demonstrated; [PMID: 29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/)).

#### Detail by category

**Upstream induction (Finding F006).** In an embryonic-stem-cell–directed somitic chondrogenesis model, isolated paraxial mesoderm treated with SAG1 (Hedgehog agonist) plus LDN193189 (BMP type-I receptor inhibitor) induced *Pax1* and *Bapx1(NKX3-2)*, then *Sox9*, producing cartilaginous nodules; canonical Wnt (Wnt3a/CHIR99021) + Noggin generated the upstream paraxial mesoderm. TGFβ supported Sox9/chondrogenesis but did *not* induce *Pax1/Bapx1*, showing the sclerotome route is specifically SHH- and BMP-antagonism-dependent.

> "Pax1 and Bapx1 expression was induced when the isolated paraxial mesodermal progeny were treated with SAG1 (a hedgehog receptor agonist) and LDN193189, then Sox9 expression was induced, leading to cartilaginous nodules." — [PMID: 25294938](https://pubmed.ncbi.nlm.nih.gov/25294938/)

**Molecular pathways.** SHH signaling; BMP antagonism (Noggin); canonical Wnt/β-catenin (upstream mesoderm); PTHrP–NKX3-2–RUNX2 growth-plate axis; NF-κB (RelA) survival signaling.

**Cellular processes.** Chondrocyte fate specification, proliferation, maturation/hypertrophy control, and chondrocyte survival (anti-apoptotic).

**Repression of RUNX2 downstream of PTHrP (Finding F002).** Nkx3.2/Bapx1 expression in the growth plate is restricted to the proliferative zone, is lost when PTHrP signaling is absent, and is maintained by ectopic PTHrP. NKX3-2 represses RUNX2, and RUNX2 mis-expression rescues the NKX3-2-induced blockade of maturation — placing NKX3-2 as a PTHrP-controlled brake on chondrocyte hypertrophy.

> "Nkx3.2 represses expression of the chondrocyte maturation factor Runx2, and Runx2 mis-expression can rescue the Nkx3.2-induced blockade of chondrocyte maturation." — [PMID: 16421188](https://pubmed.ncbi.nlm.nih.gov/16421188/)

> "Nkx3.2/Bapx1 expression is lost in the growth plates of mice engineered to lack PTHrP signaling and, conversely, is maintained by ectopic expression of PTHrP." — [PMID: 16421188](https://pubmed.ncbi.nlm.nih.gov/16421188/)

**Chondrocyte survival via RelA/NF-κB (Finding F005).** NKX3-2 sustains proliferating-chondrocyte viability by constitutively activating RelA. It recruits the RelA–IκBα complex into the nucleus by direct protein–protein interaction and activates RelA via proteasome-dependent nuclear IκBα degradation — a stage-specific, ligand-independent mode of NF-κB activation.

> "Nkx3.2 supports chondrocyte survival by constitutively activating RelA." — [PMID: 17310243](https://pubmed.ncbi.nlm.nih.gov/17310243/)

> "Nkx3.2 recruits the RelA-IkappaBalpha heteromeric complex into the nucleus by direct protein-protein interactions and activates RelA through proteasome-dependent IkappaBalpha degradation in the nucleus." — [PMID: 17310243](https://pubmed.ncbi.nlm.nih.gov/17310243/)

**Protein dysfunction.** NKX3-2 is a homeodomain transcription factor; LoF mutations abolish its DNA-binding/transcriptional-regulatory activity (loss of function; not gain of function or dominant negative — consistent with recessive inheritance).

**Downstream target network.** *Bapx1*-null mice show downregulation of Sox9, Col2a1 (α1(II) collagen), Fgfr3, Indian hedgehog (Ihh), and Runx2/Osf2 (Finding F004).

**Cell types & GO terms.** Cell types: chondrocyte (CL:0000138), proliferating chondrocyte, sclerotome-derived chondroprogenitor. Suggested GO biological processes: chondrocyte differentiation (GO:0002062), endochondral ossification (GO:0001958), cartilage development (GO:0051216), negative regulation of chondrocyte differentiation (GO:0032331), positive regulation of NF-κB transcription factor activity (GO:0051092), and somite/sclerotome patterning.

---

### 7. Anatomical Structures Affected

**Organ/system level.** Primary: axial and appendicular skeleton (skeletal system, UBERON:0001434). The vertebral column (UBERON:0001130) — especially the cervical spine (UBERON:0002413) — is most severely affected. Secondary: the **nervous system** via spinal cord (UBERON:0002240) compression from cervical instability. In the mouse model, the spleen is also affected (asplenia), though splenic involvement is not a prominent feature of human SMMD.

**Anatomical sites (UBERON).** Vertebral body (UBERON:0002347), epiphysis (UBERON:0006589), metaphysis (UBERON:0003914), growth plate (UBERON:0003078), pubis (UBERON:0002367), metacarpal/phalangeal bones (UBERON:0002374 / UBERON:0003221).

**Tissue and cell level.** Cartilage tissue (UBERON:0002418) and the chondrocyte (CL:0000138) — specifically proliferating growth-plate chondrocytes — are the central affected cell population. Connective tissue of the developing skeleton is broadly involved.

**Subcellular level (GO Cellular Component).** Nucleus (GO:0005634) — the site of NKX3-2 transcription-factor and RelA/NF-κB activity; proteasome-mediated IκBα degradation (cytoplasm/nucleus) participates in the survival pathway.

**Lateralization.** Bilateral and symmetric (axial midline and paired long bones).

---

### 8. Temporal Development

**Onset.** Congenital; radiographic abnormalities (delayed vertebral/pubic ossification) are present at birth. Clinical presentation is typically in infancy/early childhood. A severe end of the spectrum presents as **perinatal-lethal** disease [PMID: 29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/).

**Onset pattern.** Chronic/insidious for the surviving milder phenotype; the perinatal-lethal form is evident at/before birth.

**Progression.** Skeletal deformity and, critically, cervical spine instability are **progressive**. Cervical instability can worsen and lead to cord injury and spasticity during childhood (5/6 patients in the reported series; [PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)). Disease duration is chronic/lifelong for survivors.

**Critical periods.** Two windows are important: (1) embryonic sclerotome/chondrogenesis (the mechanistic origin, not therapeutically accessible postnatally), and (2) infancy–childhood, when cervical spine surveillance and timely stabilization can prevent catastrophic cord injury (the key intervention window).

---

### 9. Inheritance and Population

**Inheritance pattern.** Autosomal recessive (biallelic LoF *NKX3-2*), OMIM 613330 [PMID: 20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/).

**Penetrance / expressivity.** Penetrance appears complete for biallelic LoF. Expressivity is variable, ranging from perinatal-lethal to survival into childhood/adulthood with progressive skeletal and neurological disease.

**Consanguinity / founder effects.** Consanguinity is a prominent feature of reported families; index cases were identified via homozygosity mapping in consanguineous pedigrees. No specific founder allele is established — the reported mutations are distinct/private.

**Carrier frequency.** Heterozygous carriers are asymptomatic (haplosufficiency confirmed by gnomAD, Finding F008). Given the disease rarity, carrier frequency is very low in the general population.

**Epidemiology.** SMMD is ultra-rare, with only a small number of families/cases reported worldwide; precise prevalence and incidence are not established (below reliable estimation). No strong sex bias is expected for an autosomal recessive disorder (theoretical male:female ≈ 1:1). Age distribution: presents congenitally/in childhood.

---

### 10. Diagnostics

**Imaging (primary diagnostic modality).** Skeletal radiography is central. Characteristic findings (Finding F003): severe ossification delay of vertebral bodies with **sagittal and coronal clefts**, absent pubic bone ossification, large round **"balloon-like" epiphyses** of long bones, and multiple **pseudoepiphyses** at all metacarpals and phalanges. Cervical spine imaging (dynamic flexion/extension radiographs, CT, MRI) is essential to detect instability and cord compression.

> "five of six patients in our series suffered cervical cord injury that manifested clinically as limb spasticity." — [PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)

**Genetic testing (confirmatory).** Molecular confirmation is by sequencing *NKX3-2* — via single-gene testing, a skeletal-dysplasia gene panel, or whole-exome/whole-genome sequencing. Homozygosity mapping was historically used in consanguineous families. Detection of biallelic inactivating *NKX3-2* variants confirms the diagnosis.

**Laboratory tests / biomarkers.** No specific biochemical biomarker exists; diagnosis rests on radiographic pattern + molecular confirmation. Routine biochemistry (calcium, phosphate, ALP) is generally unremarkable, helping distinguish SMMD from metabolic bone disease.

**Clinical criteria / differential diagnosis.** Diagnosis integrates the disproportionate short-trunk phenotype, the characteristic radiographic constellation, and *NKX3-2* genotyping. Differential diagnoses include other spondylometaphyseal/spondyloepimetaphyseal dysplasias, spondyloepiphyseal dysplasia congenita (COL2A1), and other short-trunk dysplasias — distinguished by the unique mega-epiphyses + vertebral clefts + pubic non-ossification pattern and by molecular testing.

**Screening.** Cascade genetic testing of at-risk relatives and prenatal/preimplantation genetic testing are available for families with known *NKX3-2* variants. No population newborn screening exists.

---

### 11. Outcome / Prognosis

**Survival/mortality.** Prognosis spans a wide spectrum. The severe end is **perinatal-lethal** [PMID: 29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/). For survivors, the principal life-threatening risk is **cervical cord injury** from cervical spine instability, which can cause severe neurological disability or death if unrecognized.

**Morbidity/function.** Major morbidity arises from (1) neurological compromise (spasticity, myelopathy) due to cord compression, and (2) skeletal deformity and short stature affecting mobility and daily function. In the reported series, 5 of 6 patients developed cervical cord injury with limb spasticity ([PMID: 22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/)).

**Complications.** Cervical instability/cord compression is the dominant complication; respiratory compromise and orthopedic complications (deformity, contractures) also occur.

**Prognostic factors.** Severity and timing of cervical instability, and whether it is detected and stabilized before cord injury, are the key modifiable prognostic determinants. The specific genotype (e.g., truncating variants associated with perinatal lethality) also influences outcome.

---

### 12. Treatment

**No disease-modifying therapy exists.** Management is entirely supportive and preventive.

- **Surgical/interventional (most important).** Cervical spine **stabilization/fusion** and decompression for instability and cord compression; timely neurosurgical/orthopedic intervention is the key to preventing or limiting neurological injury. (Suggested NCIT: cervical spinal fusion / spinal stabilization procedures.)
- **Supportive care.** Respiratory support, orthopedic management of deformity and contractures, pain management, and mobility aids.
- **Rehabilitation.** Physical and occupational therapy to preserve function and manage spasticity.
- **Genetic counseling.** For affected families given autosomal recessive recurrence risk (25% per pregnancy for carrier couples).
- **Pharmacotherapy / advanced therapeutics.** No pharmacologic, gene, cell, or RNA-based therapies are established or in trials specifically for SMMD. There are no relevant pharmacogenomic considerations.

---

### 13. Prevention

- **Primary prevention.** Not possible for an inherited developmental disorder; the only means of avoiding recurrence is reproductive planning in carrier couples (prenatal diagnosis, preimplantation genetic testing).
- **Secondary prevention.** Early detection and **surveillance of the cervical spine** in diagnosed patients to catch instability before cord injury — the single most impactful preventive measure.
- **Tertiary prevention.** Cervical stabilization, spasticity management, and orthopedic/respiratory care to prevent complications and disability progression.
- **Genetic screening/counseling.** Carrier testing and cascade screening in affected families; genetic counseling regarding 25% recurrence risk and reproductive options.
- Immunization, behavioral, and public-health interventions are **not applicable**.

---

### 14. Other Species / Natural Disease

**Comparative biology (Finding F004).** *NKX3-2/Bapx1* is deeply conserved. It was first identified in *Drosophila* as *bagpipe (bap)*, essential for midgut musculature; the vertebrate ortholog acquired axial/limb skeletogenesis functions after the jawless-fish/gnathostome split [PMID: 11523821](https://pubmed.ncbi.nlm.nih.gov/11523821/). Orthologs include mouse *Bapx1/Nkx3.2* (chromosome 5) and zebrafish *nkx3.2*. Human *BAPX1* has 87% amino-acid identity to the *Drosophila* homeodomain and 100% homeodomain identity to mouse [PMID: 9426254](https://pubmed.ncbi.nlm.nih.gov/9426254/).

**Model organisms as "natural disease" analogs.** No naturally occurring SMMD-equivalent disease is documented in companion animals or wildlife; disease knowledge comes from engineered models (below).

**Suggested NCBI Taxa:** *Homo sapiens* (9606), *Mus musculus* (10090), *Danio rerio* (7955), *Drosophila melanogaster* (7227).

---

### 15. Model Organisms

**Mouse — *Bapx1(Nkx3.2)*-null (Finding F004).** *Bapx1*-null mice display a **perinatal-lethal skeletal dysplasia with asplenia**, featuring severe malformation or absence of vertebral column elements and cranial bones of mesodermal origin (most severe in ventral, notochord-associated structures). Failure of cartilage development is accompanied by downregulation of Sox9, Col2a1, Fgfr3, Ihh, and Runx2/Osf2.

> "Bapx1 null mice are affected by a perinatal lethal skeletal dysplasia and asplenia, with severe malformation or absence of specific bones of the vertebral column and cranial bones of mesodermal origin." — [PMID: 10572046](https://pubmed.ncbi.nlm.nih.gov/10572046/)

> "downregulation of several molecular markers required for normal chondroblast differentiation (α1(II) collagen, Fgfr3, Osf2, Indian hedgehog, Sox9)." — [PMID: 10572046](https://pubmed.ncbi.nlm.nih.gov/10572046/)

**Mouse — *Nkx3.1/Nkx3.2* double-null.** Simultaneous loss of both paralogs causes embryonic lethality (E12.5–E17.5) and enhanced vertebral defects versus *Bapx1* single-null, demonstrating partial functional redundancy [PMID: 12204261](https://pubmed.ncbi.nlm.nih.gov/12204261/).

**Zebrafish — *nkx3.2* mutant (Finding F004).** A zebrafish *nkx3.2* mutant models SMMD and, importantly, reveals **post-embryonic** roles of Nkx3.2 in growth plates and joints — extending mechanistic understanding beyond embryonic patterning [PMID: 33462117](https://pubmed.ncbi.nlm.nih.gov/33462117/).

**Model characteristics.** Recapitulation: the mouse null captures axial skeletal malformation and the chondrogenic gene-network collapse; the zebrafish captures post-embryonic joint/growth-plate roles. Limitations: mouse asplenia is not a prominent human feature; the mouse null's perinatal lethality limits study of postnatal cervical instability, which the zebrafish partly addresses. Genetic model types available: knockout (mouse, zebrafish), double-knockout (Nkx3.1/Nkx3.2), and in vitro ESC/iPSC-directed chondrogenesis systems.

**Resources:** MGI (mouse), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
   SHH agonist + BMP antagonism (Noggin)                [PMID 25294938]
                 │
                 ▼
   Sclerotome specification:  PAX1 ──▶ NKX3-2 (BAPX1)
                 │                        │
                 │                        ▼
                 │                    SOX9  ──▶ chondrogenesis (Col2a1, cartilage template)
                 │
   ┌─────────────┴───────────── NKX3-2 functions in growth plate ─────────────┐
   │                                                                            │
   ▼ Branch A (maturation brake)                        ▼ Branch B (survival)
 PTHrP ──▶ NKX3-2 ──┤ represses RUNX2   [PMID 16421188]  NKX3-2 ──▶ RelA/NF-κB  [PMID 17310243]
   → keeps chondrocytes proliferating                    → proliferating-chondrocyte survival
   │                                                                            │
   └──────────────────────────┬─────────────────────────────────────────────┘
                              ▼
      BIALLELIC LoF NKX3-2  → both brake AND survival signal LOST
                              ▼
   Chondrogenic network collapse (↓Sox9, Col2a1, Fgfr3, Ihh, Runx2)  [PMID 10572046]
                              ▼
   Defective endochondral ossification
     → vertebral clefts, mega-epiphyses, metaphyseal defects,
       pseudoepiphyses, absent pubic ossification            [PMID 22791571]
                              ▼
   Poor cervical vertebral ossification → CERVICAL INSTABILITY
                              ▼
   Spinal cord compression → limb spasticity / neurological injury  [PMID 22791571]
                              ▼
   (severe genotypes) perinatal lethality                  [PMID 29704686]
```

The unifying insight is that NKX3-2 is a **dual-function node**: it both times chondrocyte maturation (by repressing RUNX2 downstream of PTHrP) and protects proliferating chondrocytes from death (via ligand-independent NF-κB/RelA activation). Its complete loss therefore does not merely slow one process — it simultaneously removes a maturation brake and a survival signal, causing a broad collapse of the chondrogenic program and thus the multi-site skeletal dysplasia. Because a single allele suffices for normal development (gnomAD LOEUF ≈ 1.07, pLI ≈ 0), only individuals with biallelic loss are affected, explaining the recessive inheritance and the association with consanguinity.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [20004766](https://pubmed.ncbi.nlm.nih.gov/20004766/) | Homozygous inactivating *NKX3-2* mutations cause SMMD | Causal gene, LoF mechanism, 4p15.33 locus, AR inheritance (F001) |
| [29704686](https://pubmed.ncbi.nlm.nih.gov/29704686/) | Novel *NKX3-2* mutation, perinatal-lethal SMMD | Specific frameshift LoF variant; severe end of spectrum (F001) |
| [22791571](https://pubmed.ncbi.nlm.nih.gov/22791571/) | Cervical spine instability in SMMD | Cervical cord injury frequency (5/6); radiographic features (F003) |
| [16421188](https://pubmed.ncbi.nlm.nih.gov/16421188/) | Nkx3.2/Bapx1 negatively regulates chondrocyte maturation | RUNX2 repression downstream of PTHrP (F002) |
| [17310243](https://pubmed.ncbi.nlm.nih.gov/17310243/) | Constitutive RelA activation by Nkx3.2 | Chondrocyte survival via NF-κB (F005) |
| [25294938](https://pubmed.ncbi.nlm.nih.gov/25294938/) | Small-molecule sclerotome/somitic chondrogenesis | SHH + BMP-antagonism induces Bapx1 upstream of Sox9 (F006) |
| [10572046](https://pubmed.ncbi.nlm.nih.gov/10572046/) | Murine *Bapx1* in axial skeleton & spleen | Mouse KO phenotype; downstream targets (F004) |
| [12204261](https://pubmed.ncbi.nlm.nih.gov/12204261/) | Nkx3.1 & Nkx3.2 overlap in sclerotome | Paralog redundancy; double-null enhanced defects |
| [33462117](https://pubmed.ncbi.nlm.nih.gov/33462117/) | Zebrafish *nkx3.2* SMMD model | Post-embryonic skeletal roles (F004) |
| [11523821](https://pubmed.ncbi.nlm.nih.gov/11523821/) | Bapx1 in axial skeleton development/evolution | Evolutionary conservation; vertebral phenotype |
| [15024065](https://pubmed.ncbi.nlm.nih.gov/15024065/) | Meox proteins activate Bapx1 | Upstream Meox→Bapx1 regulation in sclerotome |
| [19520072](https://pubmed.ncbi.nlm.nih.gov/19520072/) | MEOX1 and cranio-cervical joints | Upstream sclerotome polarity affecting Bapx1 |
| [9426254](https://pubmed.ncbi.nlm.nih.gov/9426254/) | Cloning of human BAPX1 | Gene identification, expression, chromosomal mapping |
| [27158253](https://pubmed.ncbi.nlm.nih.gov/27158253/) | Role of Nkx3.2 in chondrogenesis (review) | Synthesis of NKX3-2 role in chondrocyte fate/survival |

---

## Limitations and Knowledge Gaps

- **Ultra-rarity:** Only a handful of families/cases are reported; there are no reliable prevalence/incidence estimates, no formal natural-history cohorts, and no quality-of-life data.
- **Genotype–phenotype correlation** is incompletely defined — why some biallelic LoF variants are perinatal-lethal while others permit survival into childhood remains unclear.
- **Human vs model discrepancies:** Mouse *Bapx1*-null asplenia is not a prominent human feature; the mouse KO's perinatal lethality limits study of the clinically dominant cervical instability, only partly addressed by the zebrafish model.
- **Mechanistic detail** of how the two NKX3-2 functions (RUNX2 repression vs RelA/NF-κB survival) are individually weighted in human disease is inferred from model systems, not directly demonstrated in patients.
- **No therapeutic pipeline:** There are no disease-modifying agents, gene-therapy programs, or clinical trials specific to SMMD.
- **Modifier gene contribution** (e.g., *NKX3-1*) to human phenotypic variability is untested.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to define prevalence, natural history, genotype–phenotype correlations, and the timeline of cervical instability — directly informing surveillance guidelines.
2. **Standardize cervical-spine surveillance protocols** (dynamic imaging schedule from diagnosis) and evaluate outcomes of prophylactic vs reactive stabilization, given that 5/6 reported patients developed cord injury.
3. **Dissect the two NKX3-2 functions in vivo** using separation-of-function alleles (RUNX2-repression-deficient vs RelA-activation-deficient) in mouse/zebrafish to quantify each branch's contribution to the skeletal phenotype.
4. **Exploit the zebrafish post-embryonic model** ([PMID: 33462117](https://pubmed.ncbi.nlm.nih.gov/33462117/)) to test whether modulating downstream nodes (e.g., RUNX2 dosage, NF-κB activity) can partially rescue growth-plate/joint defects — a route toward candidate therapeutics.
5. **iPSC-derived chondrocyte models** from patient cells (using the ESC/small-molecule sclerotome-chondrogenesis protocol, [PMID: 25294938](https://pubmed.ncbi.nlm.nih.gov/25294938/)) to model human chondrogenesis and screen for corrective compounds.
6. **Test modifier hypotheses** (e.g., *NKX3-1*) via targeted sequencing across the patient cohort to explain variable expressivity.

---

*Report generated from a 5-iteration autonomous discovery investigation: 8 confirmed findings, 14 papers reviewed. Ontology IDs (HP, GO, CL, UBERON) are best-available suggestions and should be verified against current ontology releases before database ingestion.*


## Artifacts

- [OpenScientist final report](Spondylo-megaepiphyseal-metaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spondylo-megaepiphyseal-metaphyseal_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:10572046` *(abstract only)*: "downregulation of several molecular markers required for normal chondroblast differentiation (α1(II) collagen, Fgfr3, Osf2, Indian hedgehog, Sox9)."
  - closest text in source: "We provide evidence that the failure of the formation of skeletal elements in Bapx1 null embryos is a consequence of a failure of cartilage development, as demonstrated by downregulation of several molecular markers required for normal chondroblast differentiation (&agr; 1(II) collagen, Fgfr3, Osf2, Indian hedgehog, Sox9), as well as a chondrocyte-specific alpha1 (II) collagen-lacZ transgene"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:17310243` (9 mentions) - Constitutive RelA activation mediated by Nkx3.2 controls chondrocyte viability.
  - shared terms: survival, genetic

Weighed against this report's own most characteristic terms: `nkx3-2`, `smmd`, `cervical`, `instability`, `skeletal`, `model`, `bapx1`, `cord`, `phenotype`, `spine`, `gene`, `disease`, `mouse`, `vertebral`, `survival`, `function`, `patient`, `via`, `runx2`, `genetic`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013228` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spondylo-megaepiphyseal-metaphyseal dysplasia**
- `HP:0006262` (1 mention) - the report calls it "Pseudoepiphyses of the hand bones"; HP calls it **Aplasia/Hypoplasia of the 5th finger**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000944` (1 mention) - the report calls it "Abnormal metaphysis"; HP calls it **Abnormal metaphysis morphology**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.