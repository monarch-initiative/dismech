---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T23:53:55.212067'
end_time: '2026-09-29T00:11:10.464362'
duration_seconds: 1035.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Campylobacter fetus Infectious Disease
  mondo_id: MONDO:0040728
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41241280
  relevance_assessed: 37
  on_topic: 20
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0012385
    reported_labels:
    - Arthritis
    ontology_label: Camptodactyly
  - term_id: HP:0100687
    reported_labels:
    - Spontaneous abortion
    ontology_label: Polyotia
  - term_id: GO:0030115
    reported_labels:
    - Subcellular:** bacterial S-layer/external encapsulating structure
    ontology_label: S-layer
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0005578
    ontology_label: GO_0005578
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Campylobacter_Fetus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Campylobacter_Fetus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Campylobacter fetus Infectious Disease
- **MONDO ID:** MONDO:0040728 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Campylobacter fetus Infectious Disease** covering all of the
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

# Campylobacter fetus Infectious Disease — Comprehensive Disease Characteristics Report

**Target disease:** Campylobacter fetus Infectious Disease
**MONDO ID:** MONDO:0040728
**Category:** Infectious disease (zoonotic, bacterial)
**Report type:** Disease knowledge-base entry, structured per the 15-section research template

---

## Summary

*Campylobacter fetus* infectious disease is a **zoonotic, foodborne bacterial infection** caused by the Gram-negative, microaerophilic, spiral bacterium *Campylobacter fetus*. Unlike the enteric ("thermophilic") campylobacters *C. jejuni* and *C. coli*, which chiefly cause self-limited diarrhea, *C. fetus* characteristically produces **invasive, extra-intestinal disease** — most importantly bacteremia with a striking predilection for the **vascular endothelium** (mycotic aneurysm, infective endocarditis, endovascular graft/prosthesis infection), together with meningitis, cellulitis, septic arthritis, spontaneous bacterial peritonitis, and transplacental infection causing abortion, stillbirth, and neonatal sepsis/meningitis. The disease concentrates in **elderly and immunocompromised adults**, with reported 30-day mortality of roughly **12–15%** and, in perinatal transmission, fetal/neonatal mortality as high as **80%**.

The central virulence mechanism is a **paracrystalline surface (S-) layer** encoded by a family of *sapA* homologs. The S-layer confers **complement/serum resistance**, enabling the organism to survive in the bloodstream, and it undergoes **high-frequency antigenic variation** by DNA inversion/reciprocal recombination, allowing immune evasion and relapse. This S-layer/complement-resistance axis, intersecting with **host immune competence**, governs disease severity: convergent in-vitro, mouse-model, and clinical evidence supports a single coherent causal model in which S-layer–mediated serum resistance is the upstream determinant of bacteremia, endovascular/CNS/placental seeding, and antigenic-variation-driven relapse, all amplified when host immunity is impaired.

Management relies on **aminoglycosides (gentamicin), carbapenems (meropenem/imipenem), or ampicillin**, because *C. fetus* is **intrinsically resistant to cephalosporins** and increasingly acquires **fluoroquinolone resistance** (via *gyrA*/*parC* mutations). Timely, appropriate antibiotic therapy is independently associated with survival. There is **no licensed human vaccine**; human prevention rests on food safety and hygiene around livestock and reptiles and on protecting vulnerable hosts. The species comprises three reservoir-defined subspecies — **subsp. *fetus*** (cattle/sheep; the main cause of human systemic disease), **subsp. *venerealis*** (bovine genital campylobacteriosis), and the emerging reptile-associated **subsp. *testudinum***. This is an **acquired infectious disease with no heritable genetic basis**; the "genetic" content of this template therefore pertains to *bacterial* virulence and resistance genes rather than human germline variants.

---

## 1. Disease Information

**Overview.** *Campylobacter fetus* infectious disease denotes human (and animal) infection by the bacterium *C. fetus*. In humans it manifests predominantly as **systemic/invasive infection** — bacteremia with frequent secondary endovascular, neurological, musculoskeletal, soft-tissue, and perinatal localizations — rather than as the gastroenteritis typical of *C. jejuni*/*C. coli*. It is a rare but serious pathogen that "mainly affect[s] immunocompromised patients" ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)).

**Key identifiers.**
- **Mondo:** MONDO:0040728 (Campylobacter fetus infectious disease)
- **MeSH:** Campylobacter Infections (D002169); organism *Campylobacter fetus* (NCBI Taxonomy txid **196**)
- **ICD-10:** A04.8 (Other specified bacterial intestinal infections) / A28.8 (other zoonotic bacterial diseases) depending on presentation; specific bacteremia coded per site (e.g., I77.x for mycotic aneurysm complications)
- **ICD-11:** 1A0Z / 1G40-range "bacterial infection of unspecified site" plus site-specific codes
- **OMIM / Orphanet:** Not applicable — this is an acquired infection, not a Mendelian or rare *genetic* disorder, so no OMIM phenotype number or Orphanet rare-disease code applies.

**Synonyms / alternative names.** Campylobacteriosis due to *C. fetus*; *Vibrio fetus* infection (historical name); *C. fetus* bacteremia/septicemia; "campylobacteremia" (in the context of *Campylobacter* bloodstream infection). In cattle: bovine genital campylobacteriosis (BGC)/bovine venereal campylobacteriosis (subsp. *venerealis*) and sporadic/epizootic bovine-ovine abortion (subsp. *fetus*).

**Information source.** The evidence base is **aggregated disease-level** literature — retrospective clinical cohorts, national bacteremia surveillance studies, case series/reviews, microbiological/genomic studies, and animal models — rather than individual EHR-derived patient records.

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by infection with *Campylobacter fetus*, a Gram-negative, oxidase-positive, microaerophilic, S-shaped/curved rod. There is **no genetic (human germline) etiology**; the causal factor is exposure to the bacterium, typically via the fecal–oral/foodborne route from animal reservoirs and subsequent translocation from the gut across the intestinal epithelium into the bloodstream (see §6).

**Risk factors (host/environmental).** The dominant, repeatedly documented risk factors are **advanced age and immunocompromise/comorbidity**:
- Elderly (median ages 68–78 across cohorts) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/); [PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)).
- Immunodepression (43.4% of one national cohort), hematologic malignancy (25.9%), solid tumor (23%), diabetes (22.3%) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)).
- **Asplenia**, **rituximab** maintenance therapy, and **occupational exposure** (e.g., abattoir work) ([PMID: 29984777](https://pubmed.ncbi.nlm.nih.gov/29984777/)).
- HIV infection (associated with relapsing, quinolone-resistant disease) ([PMID: 9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/)).
- Male sex predominance (e.g., 78% male in a meningitis review) ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)).
- Dietary/animal exposures: unpasteurized dairy, undercooked meat, contact with cattle/sheep, and — for subsp. *testudinum* — contact with pet reptiles (turtles/tortoises) ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/); [PMID: 31928704](https://pubmed.ncbi.nlm.nih.gov/31928704/)).

**Genetic risk factors.** No established human susceptibility loci. Host innate-immune competence (complement, LPS-responsiveness) modulates outcome — demonstrated in mice where LPS-responsive C3H/HeN strains suffered higher mortality than LPS-hyporesponsive C3H/HeJ ([PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/)) — but no human polymorphisms are validated.

**Protective factors.** Intact immunity and spleen function; timely, appropriate antibiotic therapy is independently protective against death (OR 0.47, 95% CI 0.24–0.93) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)). No genetic protective variants are described.

**Gene–environment interactions.** The operative interaction is **pathogen-gene × host-environment**: the bacterial S-layer (serum resistance) interacts with the host's immune status to determine whether gut translocation progresses to sustained bacteremia and metastatic seeding (§6, §11).

---

## 3. Phenotypes

*C. fetus* infection is clinically heterogeneous; presentations reflect the site of metastatic seeding after bacteremia. Onset is typically **adult/geriatric**, **acute-to-subacute**, and severity is **moderate-to-severe** (frequently life-threatening).

| Phenotype | Type | Characteristics / frequency | Suggested HPO |
|---|---|---|---|
| Fever / febrile illness | Symptom/sign | Very common presenting feature; acute | HP:0001945 (Fever) |
| Bacteremia / sepsis | Lab + clinical | Hallmark; ~64% of analyzed invasive cases (21/33) had documented bacteremia ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)) | HP:0031864 (Bacteremia); HP:0100806 (Sepsis) |
| Mycotic aneurysm / endovascular infection | Clinical sign | Vascular tropism: 5/7 secondary localizations vascular, 3 mycotic aneurysm ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)); mycotic aortic aneurysm 24% ([PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)) | HP:0031649 (Mycotic aneurysm), HP:0004942 (Aortic aneurysm) |
| Infective endocarditis | Clinical sign | 12 of 80 secondary-localization patients ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)) | HP:0100584 (Endocarditis) |
| Cellulitis | Physical manifestation | 19% in two cohorts ([PMID: 18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/); [PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)) | HP:0100658 (Cellulitis) |
| Meningitis | Clinical sign | Relapse 22%, mortality 5% in a 37-case review; median age 49, 78% male ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)) | HP:0001287 (Meningitis) |
| Septic arthritis / osteoarticular | Clinical sign | 24 of 80 secondary-localization patients ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)) | HP:0012385 (Arthritis) |
| Spontaneous bacterial peritonitis / ascites | Clinical sign | 9 of 80 secondary-localization patients ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/); [PMID: 29853499](https://pubmed.ncbi.nlm.nih.gov/29853499/)) | HP:0030151 (Peritonitis) |
| Abortion / stillbirth / perinatal sepsis | Reproductive | 18/20 pregnancies ended prematurely (13–32 wk); fetal/neonatal mortality 80% ([PMID: 3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/)) | HP:0100687 (Spontaneous abortion) |
| Diarrhea (less common) | Symptom | Possible but not the dominant presentation | HP:0002014 (Diarrhea) |

**Quality-of-life impact.** Invasive disease carries substantial acute morbidity (ICU-level sepsis, vascular surgery for mycotic aneurysm, prolonged IV antibiotics) and, in survivors of endovascular or CNS disease, potential long-term functional impairment; relapsing infection (notably in HIV/immunocompromised hosts and meningitis) prolongs disease burden. Formal EQ-5D/SF-36 data specific to *C. fetus* are **not available**.

---

## 4. Genetic / Molecular Information

**Not applicable as human genetics.** *C. fetus* disease has **no causal human genes, pathogenic germline variants, modifier genes, or chromosomal abnormalities**. The relevant molecular determinants are **bacterial**:

- ***sapA* family (surface-array protein / S-layer proteins).** Multiple *sapA* homologs encode full-length S-layer proteins (98/127/149 kDa) attached serospecifically to type A or B lipopolysaccharide ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/)). This is the principal virulence gene family (see §6).
- ***sapCDEF* — type I secretion system** exporting the S-layer proteins without an N-terminal signal sequence ([PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/)).
- **Virulence/invasion genes:** *ciaB* (invasion), cytolethal distending toxin *cdtA/cdtB/cdtC*, and a **Type IV secretion system (T4SS)** plus *fic*-domain genes carried on genomic islands/plasmids ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/); [PMID: 27049518](https://pubmed.ncbi.nlm.nih.gov/27049518/)).
- **Resistance determinants:** *gyrA* QRDR mutations (e.g., Asp→Tyr; T86I) and *parC* mutations conferring fluoroquinolone resistance; *tet(O)* for tetracycline resistance; intrinsic cephalosporin resistance ([PMID: 9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/); [PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/); [PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

**"Epigenetic"/genomic plasticity (bacterial).** Antigenic variation of the S-layer is achieved by **inversion of a promoter-containing invertible DNA element flanked by *sapA* homologs**, and by reciprocal DNA recombination among *sapA* copies — a programmed genomic-rearrangement mechanism rather than host epigenetics ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/); [PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/)).

**Suggested ontology/chemical terms:** CHEBI lipopolysaccharide (CHEBI:16412); GO external encapsulating structure / S-layer (GO:0030115).

---

## 5. Environmental Information

**Infectious agent.** *Campylobacter fetus* (NCBI Taxonomy **txid196**), subspecies:
- **subsp. *fetus* (Cff)** — intestinal/genital tract of cattle and sheep; sporadic animal abortion and the main source of human systemic disease ([PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/)).
- **subsp. *venerealis* (Cfv)** — host-restricted to the bovine genital tract (BGC) ([PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/)).
- **subsp. *testudinum* (Cft)** — reptile (chelonian: turtle/tortoise) reservoir; emerging cause of human invasive infection ([PMID: 31928704](https://pubmed.ncbi.nlm.nih.gov/31928704/); [PMID: 29853499](https://pubmed.ncbi.nlm.nih.gov/29853499/); [PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

**Environmental/lifestyle factors.** Consumption of **unpasteurized dairy and undercooked/contaminated meat**, occupational/animal contact (livestock, abattoir), and **pet reptile exposure** (for Cft). No toxin, radiation, or pollution etiology applies. The organism is susceptible to zinc-oxide nanoparticles in vitro ([PMID: 30865839](https://pubmed.ncbi.nlm.nih.gov/30865839/)) — relevant to control/antimicrobial contexts, not disease causation.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Ingestion / mucosal exposure** to *C. fetus* from an animal reservoir (foodborne/zoonotic) **leads to** colonization of the intestinal (or, in cattle, genital) mucosa.
2. Expression of the **paracrystalline S-layer (sapA)**, exported by the **sapCDEF type I secretion system**, **results in** a surface capsule that binds serospecifically to LPS ([PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/); [PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/)).
3. The organism **adheres** to mucosal/submucosal surfaces, enhanced by **fibronectin/ECM binding** (S-layer is a major fibronectin-binding site; RGD/integrin-dependent), and **translocates across the intestinal epithelium** (bidirectionally across Caco-2 monolayers, S-layer–independently) **leading to** entry into the bloodstream/submucosa ([PMID: 18388970](https://pubmed.ncbi.nlm.nih.gov/18388970/); [PMID: 20600794](https://pubmed.ncbi.nlm.nih.gov/20600794/)).
4. In the blood, the **S-layer confers complement/serum resistance** (blocks complement-mediated killing), **resulting in** survival and **sustained high-grade bacteremia** ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/); [PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/); [PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/)).
5. Bacteremia **seeds distant sites**, with a hallmark **endovascular tropism** — the branch point — **leading to** mycotic aneurysm, endocarditis, and endovascular graft infection; other branches seed the **meninges** (meningitis), **joints/bone** (septic arthritis/osteomyelitis), **skin** (cellulitis), **peritoneum** (SBP), and — in pregnancy — the **placenta/fetus** (abortion, stillbirth, neonatal sepsis/meningitis) ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/); [PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/); [PMID: 3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/); [PMID: 7246658](https://pubmed.ncbi.nlm.nih.gov/7246658/)).
6. **High-frequency antigenic variation** of the S-layer (via invertible DNA element/reciprocal recombination) **results in** immune evasion and **relapse** (~22% in meningitis) ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/); [PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)).
7. **Host immune status modulates every step:** impaired complement/innate immunity, asplenia, malignancy, and immunosuppression **lead to** higher likelihood of progression to severe/fatal disease ([PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/); [PMID: 29984777](https://pubmed.ncbi.nlm.nih.gov/29984777/); [PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)).

> **Inferred vs. demonstrated:** Steps 2–4 and 6 are directly demonstrated (in vitro + mouse). The specific molecular basis of endovascular tropism (step 5) is clinically well documented but **mechanistically inferred** (fibronectin/ECM adhesion to damaged/atherosclerotic endothelium is a plausible driver but not proven for *C. fetus* endovascular seeding). CDT/T4SS/fic contributions to human tissue injury are **inferred from genomic presence** rather than demonstrated in human disease.

### Category detail
- **Molecular pathways / cellular processes:** complement evasion (S-layer capsule), epithelial translocation, integrin/fibronectin-mediated adhesion (RGD-dependent), CDT-mediated cell-cycle arrest (inferred), T4SS/fic disruption of host-cell processes (inferred). GO suggestions: GO:0030449 (regulation of complement activation — evaded), GO:0007155 (cell adhesion), GO:0009306 (protein secretion), GO:0052572 (response to host immune response).
- **Protein dysfunction:** not host-protein misfolding; rather bacterial S-layer proteins act as a functional immune-evasion armor; outer-membrane vesicles carry the S-layer and are immunoreactive, potentially modulating host response ([PMID: 34412928](https://pubmed.ncbi.nlm.nih.gov/34412928/)).
- **Immune involvement:** innate immunity (complement, LPS/TLR4 signaling) is central; adaptive immunity limited by antigenic variation. Cell types: intestinal epithelial cells (CL:0000584 enterocyte), vascular endothelial cells (CL:0000115), macrophages/neutrophils (CL:0000235/CL:0000775).
- **Tissue damage mechanisms:** endovascular infection → vessel-wall destruction → mycotic (infected) aneurysm and rupture risk; septic emboli; placental infection → fetal loss.

---

## 7. Anatomical Structures Affected

- **Primary sites:** bloodstream (bacteremia). **Endovascular structures** are the signature target: aorta and large arteries (mycotic aneurysm), heart valves/endocardium, vascular grafts/prostheses. UBERON: blood (UBERON:0000178), aorta (UBERON:0000947), endocardium (UBERON:0002165), artery (UBERON:0001637), blood vessel (UBERON:0001981).
- **Secondary/organ involvement:** meninges/CNS (UBERON:0002360 meninges), joints (UBERON:0001485)/bone, skin & subcutaneous tissue (UBERON:0002097; cellulitis), peritoneum (UBERON:0002358; SBP/ascites), placenta and fetus (UBERON:0001987 placenta), gastrointestinal tract (portal of entry; UBERON:0000160 intestine).
- **Body systems:** cardiovascular, nervous, musculoskeletal, integumentary, digestive, and reproductive (perinatal).
- **Tissue/cell level:** intestinal epithelium (translocation); vascular endothelium and ECM/connective tissue (adhesion, damage). Cell Ontology: enterocyte (CL:0000584), endothelial cell (CL:0000115).
- **Subcellular:** bacterial S-layer/external encapsulating structure (GO:0030115); host extracellular matrix/basement membrane (GO:0005578). Outer-membrane vesicles (bacterial) carry surface antigens.
- **Lateralization:** not applicable (systemic/bloodborne); aneurysm location varies by patient.

---

## 8. Temporal Development

- **Onset:** predominantly **adult/geriatric** (median ages 68–78); **acute to subacute**. Perinatal disease presents as prolonged maternal febrile illness or fulminant sepsis with transplacental spread ([PMID: 7246658](https://pubmed.ncbi.nlm.nih.gov/7246658/)).
- **Progression:** from gut colonization → bacteremia (often within minutes to hours in experimental models) → metastatic seeding over days. Untreated or inadequately treated endovascular disease is **rapidly progressive and can be fatal** ([PMID: 7771897](https://pubmed.ncbi.nlm.nih.gov/7771897/)).
- **Course pattern:** acute sepsis; **relapsing-remitting** in a substantial minority (meningitis relapse 22%; relapse notable in HIV/immunocompromised) ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/); [PMID: 9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/)).
- **Duration:** with prompt appropriate therapy, treatable/curable; without it, high mortality. Endovascular/CNS infection usually requires prolonged IV antibiotics ± surgery.
- **Critical intervention window:** early appropriate antimicrobial therapy is the key modifiable determinant of survival ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)).

---

## 9. Inheritance and Population

**Inheritance:** None — acquired infectious disease; no Mendelian pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier-frequency concepts apply.

**Epidemiology.**
- Among *Campylobacter* **bacteremia**, *C. fetus* is a **co-leading species**: 42.6% of 592 cases in a French national 5-year study (vs. *C. jejuni* 42.9%); median age 68 ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)). An earlier Paris series found *C. fetus* in 53% of 183 episodes ([PMID: 18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/)).
- *C. fetus* accounts for only ~**4%** of all *Campylobacter* isolates but has a disproportionately high bacteremia/invasive rate ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)).
- Species other than *C. jejuni*/*C. coli* have higher hospitalization frequency (27.3%); older age, comorbidities, and *C. fetus* infection are associated with bacteremia, and where bacteremia occurs, ~89.5% are hospitalized ([PMID: 41621728](https://pubmed.ncbi.nlm.nih.gov/41621728/)).
- **Sex ratio:** male predominance (e.g., 78% male in meningitis; 62.45% male in a pooled meta-analysis) ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/); [PMID: 42515013](https://pubmed.ncbi.nlm.nih.gov/42515013/)).
- **Age distribution:** skewed to older adults; also neonates via vertical transmission.
- **Geographic distribution:** worldwide, following animal reservoirs; most published cohorts are from Europe, North America, and East Asia (surveillance bias). Precise incidence/prevalence per 100,000 is **not well quantified** for this species specifically.

---

## 10. Diagnostics

**Specimen and detection.** Because disease is **bacteremic/extra-intestinal**, the key test is **blood culture**, not stool. *C. fetus* is frequently **missed by routine stool Campylobacter protocols**, which incubate at 42 °C — a temperature at which *C. fetus* grows poorly ([PMID: 3175020](https://pubmed.ncbi.nlm.nih.gov/3175020/)).

**Phenotypic identification / differentiation.**
| Feature | *C. fetus* | Thermophilic *C. jejuni* |
|---|---|---|
| Growth at 25 °C | Yes | No |
| Growth at 42 °C | Poor/No | Yes |
| Hippurate hydrolysis | **Negative** | Positive |
| Nalidixic acid | Resistant (classically) | Sensitive |
| Cephalothin | Sensitive (classically) | Resistant |
| H₂S (TSI) | Negative | — |

Hippurate hydrolysis differentiates *C. jejuni* (positive) from *C. fetus* and other campylobacters (negative) ([PMID: 3175020](https://pubmed.ncbi.nlm.nih.gov/3175020/)).

**Molecular / advanced identification.** 16S rRNA sequencing, **MALDI-TOF MS**, multiplex PCR (e.g., **ISCfe1** for subsp. *venerealis*), and **whole-genome sequencing/MLST** for species/subspecies and sequence-type confirmation (e.g., ST80) and resistance-gene prediction ([PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/); [PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/); [PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

**Imaging.** For endovascular disease: CT angiography, transesophageal echocardiography (endocarditis), PET-CT for graft/aneurysm infection ([PMID: 7771897](https://pubmed.ncbi.nlm.nih.gov/7771897/)).

**Genetic testing / omics diagnostics for the patient:** Not applicable (no human genetic basis). Pathogen genomics (WGS) is the relevant "omics" diagnostic.

**Differential diagnosis.** Other causes of Gram-negative bacteremia and endovascular infection (e.g., *Salmonella* mycotic aneurysm), other *Campylobacter*/*Helicobacter* species, culture-negative endocarditis; distinguished by culture, MALDI-TOF, and molecular typing.

---

## 11. Outcome / Prognosis

**Mortality.** 30-day mortality is **~12–15%** in adult bacteremia cohorts: 11.7% (French national) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)), 15% (Paris series) ([PMID: 18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/)), and 33% (7/21) in a smaller invasive-infection analysis ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)). Meningitis mortality ~5% but relapse 22% ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)). **Perinatal fetal/neonatal mortality ~80%** ([PMID: 3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/)). Endovascular disease (mycotic aneurysm, prosthetic infection) can be **rapidly fatal** despite surgery and antibiotics ([PMID: 7771897](https://pubmed.ncbi.nlm.nih.gov/7771897/)).

**Prognostic factors.**
- **Adverse:** cancer (OR 5.1 for death), inappropriate/delayed antibiotics, dyspnea, qSOFA > 2, septic shock, endovascular localization ([PMID: 18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/); [PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)).
- **Protective:** appropriate antibiotic therapy (independently associated with 30-day survival; OR 0.47) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)); favorable outcome in 72% of one series where imipenem was most active ([PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)).

**Morbidity/complications.** Mycotic aneurysm (up to 24%), endocarditis, meningitis with neurological sequelae, septic arthritis, cellulitis, SBP, relapse. Systematic reviews report **high antimicrobial resistance, mortality, and relapse risk** for *Campylobacter* bloodstream infection ([PMID: 41820744](https://pubmed.ncbi.nlm.nih.gov/41820744/)).

---

## 12. Treatment

**Pharmacotherapy (first-line).** **Aminoglycosides (gentamicin)**, **carbapenems (meropenem, imipenem)**, and **ampicillin** are the mainstays. Imipenem was the most active agent in one series ([PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)); perinatal cases were successfully treated with **ampicillin + gentamicin** ([PMID: 3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/)); post-transplant meningitis was treated with **meropenem** then de-escalated to **high-dose ampicillin** ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)); postsplenectomy sepsis in an abattoir worker resolved with **meropenem** ([PMID: 29984777](https://pubmed.ncbi.nlm.nih.gov/29984777/)).

**Resistance considerations (critical).**
- **Intrinsic cephalosporin resistance** — third-generation cephalosporins should NOT be relied upon (cefotaxime MIC₉₀ 32 mg/L, ceftriaxone 128 mg/L) ([PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/)).
- **Acquired fluoroquinolone resistance** via *gyrA* (Asp→Tyr; T86I) and *parC* mutations; associated with **relapse**, especially in HIV/immunocompromised hosts ([PMID: 9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/); [PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/); [PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)). Empiric fluoroquinolone monotherapy is therefore risky.
- Tetracycline resistance via *tet(O)* documented in an ST80 strain ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

**Surgical/interventional.** Endovascular disease (mycotic aneurysm, infected graft/prosthesis, endocarditis) often requires **surgical source control** (aneurysm/graft replacement, valve surgery) in addition to prolonged IV antibiotics ([PMID: 7771897](https://pubmed.ncbi.nlm.nih.gov/7771897/); [PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

**Treatment strategy.** Prolonged therapy for endovascular/CNS infection; combination therapy (β-lactam + aminoglycoside) commonly used; susceptibility-guided de-escalation. **Timely, appropriate antibiotics are the single most important survival lever** ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)).

**NCIT suggestions:** Gentamicin (NCIT:C557), Meropenem (NCIT:C1153), Imipenem (NCIT:C608), Ampicillin (NCIT:C258), Antibiotic Therapy (NCIT:C15832).

**Advanced/experimental therapeutics, pharmacogenomics:** No gene, cell, RNA, or targeted/immunotherapies apply; no human pharmacogenomic markers established.

---

## 13. Prevention

**No licensed human vaccine.** Human prevention is **host- and exposure-directed**: food safety (avoid unpasteurized dairy and undercooked meat), hygiene around livestock and reptiles, and heightened precaution/early treatment in immunocompromised, asplenic, elderly, and pregnant individuals.

**Primary prevention:** food-handling and animal-contact hygiene; reptile-exposure counseling (Cft). **Secondary prevention:** prompt blood culture and appropriate therapy in at-risk hosts with fever. **Tertiary prevention:** surgical source control and prolonged antibiotics to prevent endovascular complications/relapse.

**Veterinary/One-Health prevention (subsp. *venerealis*, BGC).** Control relies on **microbiological testing and culling infected bulls**, with vaccination and antibiotics as adjuncts ([PMID: 38441747](https://pubmed.ncbi.nlm.nih.gov/38441747/)). Bacterin vaccines are **non-sterilizing**: vaccinated heifers remained culture- and IHC-positive 4 months post-challenge, with Cfv persisting in the reproductive tract/vaginal mucosa ([PMID: 42085861](https://pubmed.ncbi.nlm.nih.gov/42085861/)). BGC is clinically silent in bulls (persistent preputial carriers), enabling spread absent legislated control ([PMID: 26679515](https://pubmed.ncbi.nlm.nih.gov/26679515/)); it persists even in vaccinating regions (cultured in 6.6% of bulls; positive farms were non-vaccinators) ([PMID: 26412115](https://pubmed.ncbi.nlm.nih.gov/26412115/)). Novel multi-epitope (OmpA/FliK) reverse-vaccinology candidates remain in silico only ([PMID: 38641595](https://pubmed.ncbi.nlm.nih.gov/38641595/)).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Campylobacter fetus* (NCBI Taxon **txid196**); subspecies *fetus*, *venerealis*, *testudinum*.
- **Natural disease in animals:**
  - **Cattle/sheep:** subsp. *fetus* causes **sporadic infectious abortion** and is a main infectious bovine-abortion agent ([PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/); [PMID: 42638448](https://pubmed.ncbi.nlm.nih.gov/42638448/)).
  - **Cattle (venereal):** subsp. *venerealis* causes **bovine genital campylobacteriosis** — "temporary infertility in female cattle, early embryonic mortality, aberrant oestrus cycles, delayed conception, abortions and poor calving rates" ([PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/)); WOAH-listed, trade-relevant ([PMID: 38133216](https://pubmed.ncbi.nlm.nih.gov/38133216/)).
  - **Reptiles (chelonians):** subsp. *testudinum* carried by turtles/tortoises (e.g., *Stigmochelys pardalis*) ([PMID: 31928704](https://pubmed.ncbi.nlm.nih.gov/31928704/)).
- **Zoonotic transmission:** Cff/Cft transmit from animals to humans (foodborne/contact). An invasive human ST80 Cft aortic infection was linked to a **pet soft-shell turtle** — a candidate new host/foodborne vector ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)). Cross-species susceptibility and public-health implications are recognized ([PMID: 32998205](https://pubmed.ncbi.nlm.nih.gov/32998205/); [PMID: 40638214](https://pubmed.ncbi.nlm.nih.gov/40638214/)).
- **Comparative biology:** virulence machinery (S-layer/*sapA*, T4SS, CDT) is conserved across subspecies; niche restriction (Cfv genital tropism vs. Cff/Cft broader) reflects genomic-island content.

---

## 15. Model Organisms

- **Primary model — mouse.** Adult **HA/ICR** (outbred) mice **pretreated with ferric chloride (FeCl₃)** recapitulate *C. fetus* bacteremia after oral challenge ([PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/)). This model demonstrated the S-layer's central role: **S-plus strain LD₅₀ was 43.3-fold lower** than its spontaneous S-minus mutant; high-grade bacteremia occurred only with S-plus strains; **anti-S-protein antiserum reduced 30-min bacteremia 51.6-fold**; and **LPS-responsive C3H/HeN mice had 90% mortality vs 40% in LPS-defective C3H/HeJ**, linking host innate immunity to outcome.
- **Related model — *C. jejuni* mouse.** HA/ICR adult mice model transient bacteremia and gut colonization for enteric campylobacters (contextual comparator) ([PMID: 6832823](https://pubmed.ncbi.nlm.nih.gov/6832823/)).
- **In vitro models.** **Caco-2** and **INT 407** human intestinal epithelial cells for translocation and fibronectin/ECM-mediated adhesion assays ([PMID: 20600794](https://pubmed.ncbi.nlm.nih.gov/20600794/); [PMID: 18388970](https://pubmed.ncbi.nlm.nih.gov/18388970/)); serum-bactericidal assays for complement resistance ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/); [PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/)).
- **Model characteristics.** The FeCl₃ mouse model **recapitulates bacteremia and S-layer–dependent virulence** but requires iron pretreatment and does not fully reproduce human endovascular tropism or metastatic seeding. Bovine models are used for BGC vaccine/persistence studies (vaccinated-heifer challenge) ([PMID: 42085861](https://pubmed.ncbi.nlm.nih.gov/42085861/)).

---

## Key Findings (with evidence)

### Finding 1 — Invasive, vascular-tropic bacteremia in vulnerable hosts, with high mortality
*C. fetus* is a rare but serious pathogen that "mainly affect[s] immunocompromised patients" and causes bacteremia with strong endovascular predilection. In a French invasive-infection study (2000–2021), of 21 bacteremia patients, secondary localizations occurred in 7 (33%), of which **5 were vascular (3 mycotic aneurysms)**, and **7/21 (33%) died within 30 days**; death was associated with dyspnea, qSOFA > 2, and septic shock. The abstract states: *"Secondary localizations were reported for 7 (33%) patients with C. fetus bacteremia, of which 5 exhibited a predilection for vascular infections (including 3 with mycotic aneurysm). Another 7 (33%) patients with C. fetus bacteremia died within 30 days"* ([PMID: 37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/)). A meningitis review of 37 cases found 78% male, median age 49, relapse 22%, mortality 5% ([PMID: 41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/)).

### Finding 2 — The S-layer (sapA) is the central virulence mechanism
The paracrystalline S-layer confers **complement/serum resistance** and undergoes **high-frequency antigenic variation** to facilitate persistent colonization: *"Campylobacter fetus utilizes paracrystalline surface (S-) layer proteins that confer complement resistance and that undergo antigenic variation to facilitate persistent mucosal colonization in ungulates"* ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/)). The S-layer is exported by a **type I secretion system (sapCDEF)** without an N-terminal signal sequence, and *"the virulence of Campylobacter fetus… is mediated in part by the presence of a paracrystalline surface layer (S-layer) that confers serum resistance"* ([PMID: 9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/)). *sapA* disruption abolishes the S-layer and reduces serum survival; revertants restore serum resistance and cause ~10-fold more bacteremia in mice ([PMID: 7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/)).

### Finding 3 — Subspecies, niches, and additional virulence factors
Cff inhabits the cattle/sheep intestinal/genital tract and causes human systemic disease; Cfv is host-restricted to the bovine genital tract: *"Cfv causes syndrome of temporary infertility in female cattle, early embryonic mortality, aberrant oestrus cycles, delayed conception, abortions and poor calving rates"* ([PMID: 32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/)). *C. fetus* carries conserved **T4SS** and **fic-domain** genes on genomic islands/plasmids that *"may disrupt host cell processes"* ([PMID: 27049518](https://pubmed.ncbi.nlm.nih.gov/27049518/)), and invasive strains carry *ciaB*, *cdtABC*, T4SS, and *sapA* ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)). The organism *"was found to translocate equally well in both apical-to-basolateral and basolateral-to-apical directions"* across Caco-2 epithelium, explaining gut-to-blood dissemination ([PMID: 20600794](https://pubmed.ncbi.nlm.nih.gov/20600794/)).

### Finding 4 — Perinatal disease with high fetal mortality
Maternal bacteremia originating from the bowel produces feto-placental involvement: *"Eighteen of 20 pregnancies… ended prematurely at 13-32 weeks of gestation. All of the mothers survived, but fetal/neonatal mortality was 80%"* ([PMID: 3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/)). Transplacental spread *"may result in abortion, stillbirth, or early neonatal meningitis"* ([PMID: 7246658](https://pubmed.ncbi.nlm.nih.gov/7246658/)). Perinatal cases were successfully treated with ampicillin + gentamicin.

### Finding 5 — Treatment and resistance
Treatment relies on aminoglycosides/carbapenems/ampicillin. Quinolone resistance arises via a *gyrA* mutation: *"a G-to-T change that led to an Asp-to-Tyr amino acid substitution at a critical residue frequently associated with quinolone resistance"*, linked to relapse in HIV patients ([PMID: 9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/)). In a Taiwan bacteremia series, *"the majority of the isolates were resistant to third-generation cephalosporins and quinolones"*, with *parC* mutations ([PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/)).

### Finding 6 — Diagnosis by blood culture with characteristic phenotype
*C. fetus* is optimally recovered from **blood culture** and often missed by 42 °C stool protocols; it is **hippurate-negative** (differentiating it from *C. jejuni*): *"Hippurate hydrolisis was used to differentiate C. jejuni (positive) from all the other Campylobacter spp (negative)"* ([PMID: 3175020](https://pubmed.ncbi.nlm.nih.gov/3175020/)). Species/subspecies confirmation uses 16S/multiplex PCR/MALDI-TOF/WGS ([PMID: 22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/)).

### Finding 7 — Mouse model proves S-layer centrality
In the FeCl₃-pretreated HA/ICR mouse model, *"the LD50 for S-plus strain 84-32 was 43.3 times lower than its spontaneous S-minus mutant 84-54"*, and *"these findings in a mouse model point toward the central role of the S-protein in the pathogenesis of C. fetus infection"* ([PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/)). Anti-S antiserum reduced bacteremia 51.6-fold, and host LPS-responsiveness modulated mortality (C3H/HeN 90% vs C3H/HeJ 40%).

### Finding 8 — Emerging reptile-associated subsp. *testudinum*
Cft is carried by chelonians — surveys detected *"one for C. fetus subsp. testudinum (Stigmochelys pardalis)"* ([PMID: 31928704](https://pubmed.ncbi.nlm.nih.gov/31928704/)) — has been isolated from human ascites in chronic kidney disease ([PMID: 29853499](https://pubmed.ncbi.nlm.nih.gov/29853499/)), and an invasive ST80 strain (nalidixic acid/ciprofloxacin/tetracycline resistant; *gyrA* T86I, *tet(O)*; carrying *ciaB*, *cdtABC*, T4SS, *sapA*) caused thoracoabdominal aortic infection, suspected source a pet turtle ([PMID: 40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/)).

### Finding 9 — Host-specific prevention; non-sterilizing bovine vaccines
BGC control = test-and-cull + adjunct vaccination: *"The control of both diseases relies on microbiological testing and culling infected bulls"* ([PMID: 38441747](https://pubmed.ncbi.nlm.nih.gov/38441747/)). Vaccination is non-sterilizing — *"vaccinated animals also remained culture- and IHC-positive at four months post-infection, suggesting that vaccination did not induce sterilizing immunity and did not prevent persistence of Cfv within the reproductive tract"* ([PMID: 42085861](https://pubmed.ncbi.nlm.nih.gov/42085861/)); BGC persists even where vaccination is recommended ([PMID: 26412115](https://pubmed.ncbi.nlm.nih.gov/26412115/)). No licensed human vaccine exists.

### Finding 10 — Epidemiology and prognosis
*C. fetus* is a co-leading cause of *Campylobacter* bacteremia — *"Campylobacter jejuni and Campylobacter fetus were the most commonly identified species (in 42.9% and 42.6%, respectively). The patients were elderly (median age 68 years)"*; appropriate antibiotics were protective (OR 0.47) ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)). Compared with other species, *"patients with C. fetus bacteremia were older (mean age, 69.5 years vs. 55.6 years; P = .001) and were more likely to have cellulitis (19% vs. 7%; P = .03), endovascular infection (13% vs. 1%; P = .007)"* ([PMID: 18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/)); mycotic aortic aneurysm reached 24% in one series ([PMID: 17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/)).

### Finding 11 — Integrated S-layer × host-immunity model
Convergent in-vitro, mouse, and clinical evidence establishes upstream S-layer serum resistance → bacteremia → endovascular/CNS/placental seeding → antigenic-variation-driven relapse, modulated by host immunity. The mouse model *"point[s] toward the central role of the S-protein in the pathogenesis of C. fetus infection"* ([PMID: 2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/)), while the clinical lever is that *"an appropriate antibiotic treatment was independently associated with 30-day survival"* ([PMID: 34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/)).

---

## Mechanistic Model / Interpretation

```
 Animal reservoir (cattle/sheep; reptiles for Cft)
        |  foodborne / contact (zoonotic)
        v
 Gut colonization --(fibronectin/ECM, RGD-integrin adhesion; PMID 18388970)--> epithelial adhesion
        |
        v  epithelial translocation (Caco-2, S-layer-independent; PMID 20600794)
 BLOODSTREAM ENTRY
        |
        v  S-LAYER (sapA) -> complement/serum resistance   <-- HOST IMMUNITY
        |   (PMID 7885229, 9851986, 2318963)                 (complement, spleen,
        v                                                      malignancy, HIV, age)
 SUSTAINED BACTEREMIA ------------------------------------------+
        |                                                       |
        +--> ENDOVASCULAR (hallmark): mycotic aneurysm,         | antigenic variation
        |     endocarditis, graft infection (PMID 37877803,     | (invertible DNA element)
        |     17999095, 34849656)                               | -> immune evasion -> RELAPSE
        +--> MENINGES: meningitis (PMID 41241280)               | (PMID 7885229, 41241280)
        +--> JOINTS/BONE, SKIN (cellulitis), PERITONEUM (SBP)   |
        +--> PLACENTA/FETUS: abortion, stillbirth, neonatal     |
              sepsis/meningitis (PMID 3523697, 7246658) <-------+
        |
        v  MODIFIABLE LEVER: timely appropriate antibiotics (OR 0.47; PMID 34849656)
   OUTCOME: ~12-15% 30-day mortality (adults); ~80% fetal/neonatal mortality (perinatal)
```

**Upstream vs downstream.** The **S-layer/serum-resistance axis is upstream** and necessary for bloodstream persistence; **metastatic seeding, tissue destruction, and relapse are downstream** consequences. **Host immune competence is a parallel upstream modulator** that gates progression at every step. The **actionable node** is prompt, susceptibility-appropriate antibiotic therapy (avoiding cephalosporins; cautious with fluoroquinolones), plus surgical source control for endovascular disease.

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [37877803](https://pubmed.ncbi.nlm.nih.gov/37877803/) | Retrospective clinical (France) | Vascular tropism & 33% 30-day mortality in invasive disease |
| [34849656](https://pubmed.ncbi.nlm.nih.gov/34849656/) | National bacteremia cohort | *C. fetus* co-leads bacteremia; 11.7% mortality; appropriate antibiotics protective |
| [18699745](https://pubmed.ncbi.nlm.nih.gov/18699745/) | Clinical cohort | Older age, endovascular tropism (13% vs 1%), 15% mortality |
| [17999095](https://pubmed.ncbi.nlm.nih.gov/17999095/) | Clinical series | Mycotic aneurysm 24%, cellulitis 19%, imipenem most active |
| [41241280](https://pubmed.ncbi.nlm.nih.gov/41241280/) | Case + literature review | Meningitis: immunocompromised hosts, relapse 22% |
| [7885229](https://pubmed.ncbi.nlm.nih.gov/7885229/) | In vitro/molecular | S-layer confers complement resistance & antigenic variation |
| [9851986](https://pubmed.ncbi.nlm.nih.gov/9851986/) | Molecular | S-layer secreted by type I secretion system; serum resistance |
| [2318963](https://pubmed.ncbi.nlm.nih.gov/2318963/) | Mouse model | S-protein central to virulence; host LPS-responsiveness modulates mortality |
| [20600794](https://pubmed.ncbi.nlm.nih.gov/20600794/) | In vitro (Caco-2) | Bidirectional epithelial translocation (gut→blood) |
| [18388970](https://pubmed.ncbi.nlm.nih.gov/18388970/) | In vitro | Fibronectin/ECM adhesion via S-layer, RGD-integrin dependent |
| [27049518](https://pubmed.ncbi.nlm.nih.gov/27049518/) | Genomics | T4SS & fic-domain virulence factors |
| [40484837](https://pubmed.ncbi.nlm.nih.gov/40484837/) | Genomics/case (ST80 Cft) | Reptile-associated invasive aortic infection; resistance & virulence genes |
| [32867004](https://pubmed.ncbi.nlm.nih.gov/32867004/) | Veterinary genomics | Cfv host-restricted BGC; ISCfe1 typing |
| [3523697](https://pubmed.ncbi.nlm.nih.gov/3523697/) | Case series/review | Perinatal: 80% fetal/neonatal mortality |
| [7246658](https://pubmed.ncbi.nlm.nih.gov/7246658/) | Case report/review | Transplacental spread → abortion/stillbirth/neonatal meningitis |
| [9534967](https://pubmed.ncbi.nlm.nih.gov/9534967/) | Molecular/clinical | gyrA-mediated quinolone resistance & relapse in HIV |
| [22771419](https://pubmed.ncbi.nlm.nih.gov/22771419/) | Bacteremia/AST series | Cephalosporin & quinolone resistance; parC mutations |
| [3175020](https://pubmed.ncbi.nlm.nih.gov/3175020/) | Microbiology | Hippurate-negative differentiation from *C. jejuni* |
| [31928704](https://pubmed.ncbi.nlm.nih.gov/31928704/) | Veterinary survey | Cft carriage in chelonians |
| [29853499](https://pubmed.ncbi.nlm.nih.gov/29853499/) | Genome/case | Cft from human ascites (CKD) |
| [42085861](https://pubmed.ncbi.nlm.nih.gov/42085861/) | Bovine challenge | Non-sterilizing BGC vaccination |
| [38441747](https://pubmed.ncbi.nlm.nih.gov/38441747/) | Veterinary program | Test-and-cull BGC control |
| [29984777](https://pubmed.ncbi.nlm.nih.gov/29984777/) | Case report | Asplenia/rituximab/occupational risk; meropenem cure |
| [41621728](https://pubmed.ncbi.nlm.nih.gov/41621728/) | Meta-analysis | Non-jejuni/coli higher hospitalization; *C. fetus*↔bacteremia |
| [41820744](https://pubmed.ncbi.nlm.nih.gov/41820744/) | Systematic review | High AMR, mortality, relapse in *Campylobacter* BSI |

**Evidence source types:** human clinical (cohorts, case series/reviews), veterinary/animal-reservoir studies, in-vitro molecular/cell-culture, and mouse-model experiments. No human computational/GWAS evidence applies (no heritable basis).

---

## Limitations and Knowledge Gaps

1. **No human genetic architecture.** Sections 4/9 on causal genes, inheritance, penetrance, and carrier frequency are **not applicable**; all "genetic" content concerns bacterial virulence/resistance genes.
2. **Retrospective, surveillance-biased epidemiology.** Cohorts are predominantly European/North American/East Asian; global incidence/prevalence per 100,000 is not well quantified, and *C. fetus*-specific (vs. genus-level) rates are sparse.
3. **Mechanism of endovascular tropism is inferred.** Fibronectin/ECM adhesion is a plausible driver, but the molecular basis for *C. fetus*'s specific affinity for damaged/atherosclerotic vessels is unproven.
4. **CDT/T4SS/fic roles in human disease are genomic inferences**, not demonstrated in human tissue.
5. **Small perinatal and meningitis series** yield wide uncertainty around mortality/relapse estimates.
6. **No human vaccine and limited pharmacogenomics**; treatment evidence is largely observational (no RCTs).
7. **Model limitations:** the FeCl₃ mouse model requires iron pretreatment and does not reproduce endovascular seeding; no widely used organoid or humanized model exists.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify population burden:** systematic estimate of *C. fetus*-specific incidence/prevalence and case-fatality by age/immune status using linked national bacteremia registries and GBD-style modeling.
2. **Dissect endovascular tropism:** endothelial/aortic-explant adhesion-invasion assays (± fibronectin, ± RGD blockade, ± S-layer) and a vascular-injury animal model to test whether ECM exposure drives mycotic-aneurysm seeding.
3. **Resistance surveillance:** prospective WGS-based tracking of *gyrA*/*parC*/*tet(O)* and MIC trends to inform empiric regimens and stewardship, given cephalosporin intrinsic resistance and rising fluoroquinolone resistance.
4. **Antigenic-variation & relapse:** longitudinal genomic tracking of *sapA* inversion/recombination in relapsing (especially HIV/meningitis) patients to link S-layer switching to clinical relapse.
5. **Host-factor immunology:** evaluate complement pathway, splenic function, and innate-immune status as predictors of progression to invasive disease; assess whether biomarkers stratify risk.
6. **One-Health / reptile reservoir:** characterize prevalence and transmission of subsp. *testudinum* from pet/food reptiles and define public-health messaging for immunocompromised owners.
7. **Vaccine science (veterinary and human):** advance multi-epitope (OmpA/FliK) and S-layer/OMV-based candidates from in-silico to in-vivo testing, aiming for sterilizing bovine immunity and exploring feasibility of human high-risk-group vaccination.

---

*Report compiled from 11 confirmed findings and 45 reviewed papers across 5 investigation iterations. Ontology suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, NCBI Taxon) are provided inline per section for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Campylobacter_Fetus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Campylobacter_Fetus_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 37 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41241280` *(abstract only)*: "mainly affect[s] immunocompromised patients"
  - Text part not found as substring: 'mainly affect immunocompromised patients' (note: only abstract available for PMID:41241280, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012385` (1 mention) - the report calls it "Arthritis"; HP calls it **Camptodactyly**
- `HP:0100687` (1 mention) - the report calls it "Spontaneous abortion"; HP calls it **Polyotia**
- `GO:0030115` (2 mentions) - the report calls it "Subcellular:** bacterial S-layer/external encapsulating structure"; GO calls it **S-layer**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005578` (GO_0005578) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030151` (1 mention) - the report calls it "Peritonitis"; HP calls it **Cholangitis**
- `GO:0030449` (1 mention) - the report calls it "regulation of complement activation — evaded"; GO calls it **regulation of complement activation**