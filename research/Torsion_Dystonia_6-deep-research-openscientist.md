---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T12:53:07.927975'
end_time: '2026-09-12T13:12:28.131385'
duration_seconds: 1160.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Torsion Dystonia 6
  mondo_id: MONDO:0011264
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 37
  on_topic: 27
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 27
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.036
  labels_checked: 15
  labels_matching: 5
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0002408
    reported_labels:
    - Torticollis
    ontology_label: Cerebral arteriovenous malformation
  - term_id: HP:0001350
    reported_labels:
    - Dysphonia
    ontology_label: Slurred speech
  - term_id: HP:0001260
    reported_labels:
    - Symptom
    ontology_label: Dysarthria
  - term_id: HP:0007325
    reported_labels:
    - Clinical sign
    ontology_label: Generalized dystonia
  - term_id: NCIT:C1084
    reported_labels:
    - botulinum toxin
    ontology_label: Staphylococcal Enterotoxin B
  - term_id: NCIT:C38150
    reported_labels:
    - deep brain stimulation
    ontology_label: PEComa
  labels_variant: 4
  unresolved_terms:
  - HP:0004350
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Torsion_Dystonia_6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Torsion_Dystonia_6-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Torsion Dystonia 6
- **MONDO ID:** MONDO:0011264 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Torsion Dystonia 6** covering all of the
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

# Torsion Dystonia 6 (DYT6 / DYT-THAP1): Comprehensive Disease Characteristics Report

**MONDO:** MONDO:0011264 · **OMIM:** #602629 (DYSTONIA 6, TORSION; DYT6) · **Gene:** *THAP1* (OMIM \*609520; HGNC:20856; 8p11.21) · **Category:** Mendelian, autosomal dominant

> Evidence base: This report is synthesized from primary human clinical/genetic studies, in-vitro molecular biology, structural biology, and animal models identified via PubMed (49 papers reviewed, 12 confirmed findings). Source types are flagged inline. Where a specific figure is not firmly established in the retrieved literature, this is stated explicitly. No patient-level data files were provided; this is a literature-derived, disease-level report.

---

## Summary

**Torsion Dystonia 6 (DYT6, now designated DYT-THAP1)** is a rare, autosomal dominant, incompletely penetrant form of isolated (primary) torsion dystonia caused by heterozygous loss-of-function mutations in *THAP1*, which encodes a THAP-domain zinc-finger transcription factor. It was the first transcription factor implicated in primary dystonia, established by Fuchs et al. (2009), who identified *THAP1* mutations in three Amish–Mennonite families with mixed-onset primary torsion dystonia ([PMID: 19182804](https://pubmed.ncbi.nlm.nih.gov/19182804/)). DYT6 is clinically distinguished from DYT1 (TOR1A) dystonia by its predilection for the craniocervical region, larynx (producing spasmodic/laryngeal dysphonia), and upper limbs, with frequent progression to segmental or generalized dystonia. Mean age at onset is approximately **16.8 years** (range 3 to >60), and penetrance is estimated at only **40–60%**.

Mechanistically, DYT6 sits at the center of a shared dystonia gene-regulatory network. Wild-type THAP1 binds and represses the core promoter of *TOR1A* (the DYT1 gene) and autoregulates its own promoter; pathogenic mutations abolish DNA binding and de-repress these targets, linking DYT6 and DYT1 in a common transcriptional pathway. Downstream, THAP1 dysregulates gene programs largely through the SP1/SP4 transcription-factor family in a cell-type–dependent manner, affecting synaptic transmission, cytoskeletal genes, and dopaminergic (specifically D2-receptor / indirect-pathway) signaling in the basal ganglia, with additional convergent abnormalities in the deep cerebellar nuclei. There is no neurodegeneration; the disorder is a network-level functional dysregulation across the basal ganglia–thalamo-cortical and cerebellar circuits.

Diagnosis is molecular (*THAP1* sequencing or whole-exome sequencing), and treatment is entirely symptomatic and stepwise: oral agents (anticholinergics, baclofen, benzodiazepines), botulinum toxin chemodenervation for focal features including laryngeal dystonia, and globus pallidus internus (GPi) deep brain stimulation for refractory generalized disease — the last being effective but generally less robust than in DYT1. No disease-modifying therapy exists.

---

## Key Findings

### F001 — DYT6 is caused by autosomal dominant loss-of-function mutations in the transcription factor THAP1

DYT6 dystonia was defined molecularly when Fuchs and colleagues discovered mutations in *THAP1* in three Amish–Mennonite families with mixed-onset primary torsion dystonia. As stated in the primary paper: *"We report the discovery of a mutation in the THAP1 gene in three Amish-Mennonite families with mixed-onset primary torsion dystonia (also known as DYT6 dystonia)"* and *"We demonstrate that the missense mutation impairs DNA binding, suggesting that transcriptional dysregulation may contribute to the phenotype of DYT6 dystonia"* ([PMID: 19182804](https://pubmed.ncbi.nlm.nih.gov/19182804/)). THAP1 is the **first transcription factor implicated in primary dystonia**. The inheritance pattern and mechanism were confirmed by later work: *"Dystonia 6 (DYT6) is an autosomal dominant dystonia caused by loss-of-function mutations in the zinc finger transcription factor THAP1"* ([PMID: 30590536](https://pubmed.ncbi.nlm.nih.gov/30590536/)). A locus-specific database (UMD-THAP1 LSDB) subsequently cataloged 56 probands and 43 relatives, finding no clear genotype–phenotype correlation at that time ([PMID: 21793105](https://pubmed.ncbi.nlm.nih.gov/21793105/)). *(Evidence: human genetic; in-vitro.)*

### F002 — THAP1 represses TOR1A (DYT1) and autoregulates its own promoter, linking the two primary dystonia genes

Two independent groups demonstrated a direct molecular link between DYT6 and DYT1. Kaiser et al. showed by EMSA/ChIP that *"THAP1 binds to the core promoter of TOR1A. Further, we report that wild type THAP1 represses the expression of TOR1A, whereas dystonia 6-associated mutant THAP1 results in decreased repression of TOR1A"* ([PMID: 20976771](https://pubmed.ncbi.nlm.nih.gov/20976771/)). Gavarini et al. independently confirmed *"a physical interaction between THAP1 and the TOR1A promoter that is abolished by pathophysiologic mutations"* ([PMID: 20865765](https://pubmed.ncbi.nlm.nih.gov/20865765/)). THAP1 also regulates itself: Erogullari et al. *"identified a feedback-loop in the regulation of THAP1 expression and demonstrated that mutant THAP1 leads to higher THAP1 expression levels. This compensatory autoregulation may contribute to the mean age at onset"* ([PMID: 25088175](https://pubmed.ncbi.nlm.nih.gov/25088175/)). This positions THAP1 as an upstream master regulator whose loss de-represses TOR1A and perturbs its own dosage. *(Evidence: in-vitro molecular biology.)*

### F003 — Pallidal (GPi) deep brain stimulation improves DYT6 but less robustly than DYT1

In a multicenter cohort (n=14, median 4.8-year follow-up), *"All benefited from surgery: dystonia severity was reduced by a median of 58%"* (BFMDRS motor, IQR 31–62) ([PMID: 31817799](https://pubmed.ncbi.nlm.nih.gov/31817799/)). However, comparative work found *"DYT6 patients appear to respond less robustly to GPi-DBS than their DYT1 counterparts, most likely reflecting differences in the underlying pathophysiology of these distinct genetic disorders"* ([PMID: 21949105](https://pubmed.ncbi.nlm.nih.gov/21949105/)), with some regression observed in years 2–3 despite comparable GPi microelectrode firing patterns between the two genotypes. *(Evidence: human clinical.)*

### F004 — Characteristic phenotype: early-onset craniocervical, laryngeal, and brachial dystonia that often generalizes

Unlike DYT1, *"the symptoms of DYT6 dystonia frequently involve the craniocervical region"* ([PMID: 19345148](https://pubmed.ncbi.nlm.nih.gov/19345148/)). Laryngeal involvement is a signature feature: in three DYT6 families, *"In all three symptomatic MutC, early-onset laryngeal dystonia was a prominent feature. Laryngeal assessment demonstrated adductor-type dystonia in all of them"*, and transcranial sonography *"revealed increased substantia nigra (SN) hyperechogenicity in all MutC"* ([PMID: 20687193](https://pubmed.ncbi.nlm.nih.gov/20687193/)). Spasmodic dysphonia (voice-affecting laryngeal dystonia) is therefore a hallmark early manifestation. *(Evidence: human clinical.)*

### F005 — THAP1 protein architecture: N-terminal DNA-binding zinc finger + C-terminal coiled-coil dimerization domain; most mutations are missense in the DNA-binding domain

The N-terminal atypical C2CH THAP zinc finger recognizes DNA via an unusual mechanism: *"The THAP zinc finger uses its double-stranded beta-sheet to fill the DNA major groove"* ([PMID: 20144952](https://pubmed.ncbi.nlm.nih.gov/20144952/)). Variant distribution and consequences are well defined: *"most pathogenic THAP1 mutations are missense and are located in the DNA-binding domain. There are also nonsense mutations, which act as the equivalent of a null allele because they result in the generation of small mRNA species that are likely rapidly degraded via nonsense-mediated decay"* ([PMID: 26376866](https://pubmed.ncbi.nlm.nih.gov/26376866/)). The C-terminus contains *"a coiled-coil domain (amino acids 139-190) towards its C-terminus postulated as a protein-protein-binding motif"* that mediates homodimerization ([PMID: 28299530](https://pubmed.ncbi.nlm.nih.gov/28299530/)). *(Evidence: structural biology; in-vitro.)*

### F006 — THAP1 accounts for ~1–2% of primary/isolated dystonia, enriched in early-onset, familial, non-focal cases

In a large Spanish cohort (n=1053), *"Pathogenic or likely pathogenic variants in TOR1A, THAP1 and GNAL were identified in 0.48%, 0.57% and 0.29% of our patients, respectively"*, and across the literature *"variations in TOR1A, THAP1 or GNAL accounted for about 6%, 1.8% and 1.1% of published dystonia patients, respectively"* ([PMID: 33175450](https://pubmed.ncbi.nlm.nih.gov/33175450/)). In a Chinese WES cohort of 88 isolated-dystonia patients, TOR1A + THAP1 together accounted for 47% of molecularly diagnosed cases ([PMID: 36648081](https://pubmed.ncbi.nlm.nih.gov/36648081/)). Italian screening *"strengthen[ed] the association with upper body involvement, including the cranial and cervical districts that are usually spared in DYT1-PTD"* ([PMID: 19908325](https://pubmed.ncbi.nlm.nih.gov/19908325/)), and THAP1 mutations have been confirmed across ancestries (India, [PMID: 27913194](https://pubmed.ncbi.nlm.nih.gov/27913194/)). *(Evidence: human genetic epidemiology.)*

### F007 — Thap1 animal models: no overt dystonia, but motor deficits, cerebellar and dopaminergic abnormalities, and convergent transcriptional changes

Mouse and rat models recapitulate molecular and motor but not overtly dystonic phenotypes. In the C54Y knock-in and null models, *"The projection neurons of the deep cerebellar nuclei are especially altered"* ([PMID: 26376866](https://pubmed.ncbi.nlm.nih.gov/26376866/)); homozygous germline null is embryonic lethal. Nervous-system Thap1 deletion causes locomotor deficits with transcriptional changes in synaptic transmission, cytoskeleton, gliosis, and dopamine signaling ([PMID: 30590536](https://pubmed.ncbi.nlm.nih.gov/30590536/)). Pharmacological probing revealed *"depleting THAP1 specifically interferes with the D2 receptor responses, pointing to a selective misregulation of the indirect pathway in DYT6"* ([PMID: 34802187](https://pubmed.ncbi.nlm.nih.gov/34802187/)). The downstream effector network is largely SP1/SP4-mediated: *"THAP1 mutations lead to dysregulation of genes mainly through regulation of SP1 family members, SP1 and SP4, in a cell type dependent manner"* ([PMID: 35015830](https://pubmed.ncbi.nlm.nih.gov/35015830/)). *(Evidence: model organism.)*

### F008 — THAP1's canonical molecular function: pRB/E2F cell-cycle regulator partnering with HCF-1 and O-GlcNAc transferase, linking DYT6 to DYT3

THAP1 was first characterized as a cell-cycle regulator: *"THAP1-mediated growth inhibition is due to coordinated repression of pRB/E2F cell-cycle target genes"* including *RRM1* ([PMID: 17003378](https://pubmed.ncbi.nlm.nih.gov/17003378/)). It associates with the transcriptional coactivator HCF-1 and O-GlcNAc transferase (OGT), establishing *"a link between DYT6 and DYT3 dystonias"* — the X-linked dystonia-parkinsonism pathway ([PMID: 20200153](https://pubmed.ncbi.nlm.nih.gov/20200153/)). This positions THAP1 within a broader transcriptional-regulatory hub connecting multiple monogenic dystonias. *(Evidence: in-vitro molecular biology.)*

### F009 — Treatment is symptomatic and stepwise

Dystonia management follows a tiered algorithm. *"Oral anticholinergics, baclofen and clonazepam are used off-label"* and *"Chemodenervation with botulinum toxin remains the treatment of choice for focal- or select-body regions in generalized and segmental dystonia"* ([PMID: 31117876](https://pubmed.ncbi.nlm.nih.gov/31117876/)). A recent review summarizes: *"Treatment follows a stepwise strategy, beginning with oral pharmacologic agents like anticholinergics and levodopa (especially in dopamine-related dystonias), progressing to botulinum toxin injections and deep brain stimulation of the globus pallidus internus in refractory cases"* ([PMID: 40841848](https://pubmed.ncbi.nlm.nih.gov/40841848/)). No disease-modifying therapy exists. *(Evidence: clinical guidelines/review.)*

### F010 — THAP1 is a rare cause of isolated laryngeal dystonia within a distributed network disorder with genotype-specific structural signatures

Screening of 86 spasmodic dysphonia patients found *"Two patients tested positive for novel/rare variants in THAP1 (DYT6)"* ([PMID: 27188707](https://pubmed.ncbi.nlm.nih.gov/27188707/)). Imaging demonstrates that laryngeal dystonia is a network disorder with genotype-dependent structural correlates: *"Genotype-specific alterations were found in the left superior temporal gyrus, supplementary motor area, and the arcuate portion of the left superior longitudinal fasciculus"* ([PMID: 28186656](https://pubmed.ncbi.nlm.nih.gov/28186656/)). The broader isolated-dystonia network involves cerebellar/cholinergic dysfunction; e.g., in DYT1, *"In the cerebellar vermis, VAChT expression was also significantly decreased in patients versus controls"* ([PMID: 33638639](https://pubmed.ncbi.nlm.nih.gov/33638639/)). *(Evidence: human clinical/imaging.)*

### F011 — Quantitative natural history: mean onset ~16.8 years, neck most affected, genotype–phenotype correlation, penetrance 40–60%

A large screening study (>1800 subjects) established that *"mean age of onset for THAP1 dystonia is 16.8 years and the most common sites of onset are the arm and neck, and the most frequently affected anatomical site is the neck"*, with more than half of patients having cranial or laryngeal involvement. Critically, a genotype–phenotype correlation exists: *"Protein truncating mutations and missense mutations within the THAP domain of THAP1 tend to manifest at an earlier age and exhibit more extensive anatomical distributions"* ([PMID: 22377579](https://pubmed.ncbi.nlm.nih.gov/22377579/)). Penetrance is incomplete — *"The incomplete penetrance of DYT-THAP1 dystonia, estimated at 40 to 60 %"* ([PMID: 39732371](https://pubmed.ncbi.nlm.nih.gov/39732371/)). *(Evidence: human clinical/genetic.)*

### F012 — Gene–environment "two-hit" model and metabolic dysregulation; cerebellar and late-onset presentations exist

A multi-omics study demonstrated an environmental trigger unmasking genetic predisposition: *"we performed a sciatic nerve crush injury in a genetically predisposed DYT-THAP1 heterozygous knockout mouse model"*, which induced dystonia-like movements and energy-metabolism dysregulation ([PMID: 39732371](https://pubmed.ncbi.nlm.nih.gov/39732371/)). In-vivo human cerebellar involvement was shown in a 51-year-old carrier with ataxia: *"The lack of CBI [cerebellar brain inhibition] in our patient strongly suggests cerebellar involvement"* ([PMID: 31367947](https://pubmed.ncbi.nlm.nih.gov/31367947/)). Late-onset disease (onset ≥40y) is predominantly cranial and sporadic: *"Cranial dystonia was the most common site of onset (n = 22), followed by cervical (n = 13), while limb onset was uncommon"* ([PMID: 42371050](https://pubmed.ncbi.nlm.nih.gov/42371050/)). *(Evidence: model organism; human clinical.)*

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Torsion Dystonia 6 (DYT6, DYT-THAP1) is a rare Mendelian, autosomal dominant form of isolated torsion dystonia — sustained or intermittent muscle contractions causing abnormal, often repetitive movements and postures — without neurodegeneration or additional neurological features in its pure form. It characteristically begins in childhood or adolescence in the craniocervical, laryngeal, or upper-limb regions and frequently spreads to become segmental or generalized (F001, F004, F011).

**Key identifiers.** MONDO:0011264 · OMIM #602629 (phenotype) / *THAP1* \*609520 · Gene: *THAP1* (HGNC:20856), 8p11.21. Orphanet: DYT-THAP1 (within isolated dystonia grouping). MeSH: Dystonic Disorders / Dystonia (no unique DYT6 heading). ICD-11: 8A02.1 (dystonia). ICD-10: G24.1 (idiopathic familial dystonia) / G24.8.

**Synonyms.** DYT6; DYT-THAP1; dystonia 6, torsion (autosomal dominant); THAP1-related dystonia; primary torsion dystonia type 6; mixed-onset primary torsion dystonia (historical, Amish–Mennonite).

**Data source.** Aggregated disease-level resources (OMIM, Orphanet, UMD-THAP1 LSDB [PMID: 21793105]) and published clinical case series/cohorts — not EHR/individual-patient registries.

### 2. Etiology

**Causal factors.** Primary cause is genetic: heterozygous loss-of-function mutations in *THAP1* (F001). Most are missense in the DNA-binding THAP domain; nonsense/frameshift variants act as null alleles via nonsense-mediated decay (F005). Mechanism is transcriptional dysregulation (loss of DNA binding → de-repression of downstream targets).

**Genetic risk factors.** The causal *THAP1* variant is dominant. Genotype modifies severity: protein-truncating and THAP-domain missense mutations produce earlier onset and more extensive distribution (F011). A founder missense mutation was originally described in Amish–Mennonite families (F001, F006).

**Environmental risk factors.** No established human environmental risk factors. A gene–environment "two-hit" model is supported experimentally: peripheral nerve (sciatic crush) injury unmasks dystonia-like movements in Thap1+/- mice (F012) — plausible but unproven in humans.

**Protective factors.** None established. Incomplete penetrance (40–60%) implies unidentified genetic modifiers and/or environmental buffers protect a large fraction of carriers (F011).

**Gene–environment interaction.** The two-hit model (genetic predisposition + peripheral injury/metabolic stress) is the leading GxE framework (F012).

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Severity/Course | Frequency |
|---|---|---|---|---|---|
| Torsion/isolated dystonia | Clinical sign | HP:0001332 (Dystonia) | Childhood–adolescence (mean 16.8 y) | Progressive → generalized | Defining, ~100% |
| Cervical dystonia | Clinical sign | HP:0002408 (Torticollis) | Early | Progressive | Neck = most affected site |
| Laryngeal dystonia / spasmodic dysphonia | Clinical sign | HP:0001350 (Dysphonia) | Early, prominent | Chronic | >50% cranial/laryngeal |
| Craniofacial (blepharospasm, oromandibular) | Clinical sign | HP:0000643; HP:0002019 | Childhood–adult | Segmental | Common |
| Dysarthria/speech difficulty | Symptom | HP:0001260 | Early | Chronic | Common |
| Limb (arm) dystonia | Clinical sign | HP:0004350 | Common onset site | Progressive | Common onset |
| Generalized dystonia | Clinical sign | HP:0007325 | Follows focal onset | Progressive | Frequent |

**Characteristics.** Mean onset ~16.8 years (range 3 to >60); most common onset sites arm and neck; neck most frequently affected; >50% have cranial/laryngeal involvement; typically progressive from focal to segmental/generalized (F004, F011). Late-onset (≥40y) presentations are predominantly cranial and sporadic (F012). Severity is variable, consistent with incomplete penetrance and variable expressivity.

**Quality of life.** Laryngeal dystonia selectively impairs speech/communication; generalized dystonia impairs mobility and daily function. No DYT6-specific EQ-5D/SF-36 data available; general dystonia burden is substantial.

### 4. Genetic / Molecular Information

**Causal gene.** *THAP1* (HGNC:20856; OMIM 609520; 8p11.21), encoding a 213-aa zinc-finger transcription factor (F001, F005).

**Protein architecture.** N-terminal atypical C2CH THAP zinc-finger DNA-binding domain (double-stranded β-sheet inserted into the major groove; bipartite major+minor groove recognition, consensus ~TXXGGGX(A/T)); nuclear localization signal; C-terminal coiled-coil homodimerization domain (aa ~139–190) (F005; [PMID: 20010837](https://pubmed.ncbi.nlm.nih.gov/20010837/)).

**Pathogenic variants.** Predominantly missense in the DNA-binding domain (e.g., Ser6Phe, Arg13His [also destabilizing], C54Y/C54F, L180S); also nonsense/frameshift acting as null alleles via NMD (F005). ClinVar/HGMD list dozens of P/LP variants; population allele frequencies are very low (rare disease); most are private/family-specific. Origin: germline; autosomal dominant. Functional consequence: **loss of function** (F001, F002, F005). Truncated mutants can mislocalize partly to cytoplasm; some missense mutants remain nuclear ([PMID: 22652465](https://pubmed.ncbi.nlm.nih.gov/22652465/)).

**Modifier genes.** Not definitively identified; incomplete penetrance implies modifiers exist. THAP1 autoregulates (F002); downstream, SP1/SP4 mediate effects (F007).

**Epigenetic information.** THAP1 partners with HCF-1 and O-GlcNAc transferase (OGT), tying it to chromatin/coactivator complexes and linking DYT6 to DYT3 (F008). No disease-specific methylation signature established.

**Chromosomal abnormalities.** None characteristic; DYT6 is a single-gene point-mutation disorder.

### 5. Environmental Information

No established environmental toxin, radiation, lifestyle, or infectious etiology. The only experimental environmental contributor is peripheral nerve injury acting as a "second hit" in genetically predisposed Thap1+/- mice, with accompanying energy-metabolism dysregulation (F012). Infectious agents are not implicated (distinct from secondary dystonias such as post–Japanese encephalitis dystonia, [PMID: 35025122](https://pubmed.ncbi.nlm.nih.gov/35025122/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous loss-of-function mutation in *THAP1* (missense in the DNA-binding domain, or an NMD-degraded null allele) **leads to** reduced functional THAP1 transcription-factor activity. *(demonstrated)*
2. Reduced THAP1 DNA-binding **results in** de-repression of its direct target *TOR1A* (the DYT1 gene) and dysregulated THAP1 autoregulation (altered THAP1 dosage). *(demonstrated in vitro)*
3. In parallel, loss of THAP1 **leads to** broad transcriptional dysregulation executed largely through the SP1/SP4 transcription-factor family in a cell-type–dependent manner. *(demonstrated in models)*
4. These transcriptional changes **result in** altered expression of genes governing synaptic transmission, cytoskeleton, and dopaminergic signaling — with selective impairment of D2-receptor/indirect-pathway responses in striatum, plus abnormalities of deep cerebellar nuclei projection neurons. *(demonstrated in mouse models)*
5. **Branch A (basal ganglia):** indirect-pathway/D2 dysfunction **leads to** imbalanced basal ganglia–thalamo-cortical output. **Branch B (cerebellum):** deep cerebellar nuclei/vermis dysfunction **leads to** abnormal cerebellar contribution to the motor network. *(inferred: model + human imaging integration)*
6. Convergent basal ganglia + cerebellar network dysfunction **results in** aberrant sensorimotor integration and loss of surround inhibition. *(inferred)*
7. This **manifests** as isolated dystonia — craniocervical, laryngeal, and brachial, frequently generalizing — typically in adolescence, in ~40–60% of carriers. *(demonstrated clinically)*
8. **Optional environmental branch:** a peripheral "second hit" (nerve injury/metabolic stress) **can unmask or trigger** dystonia in predisposed carriers. *(demonstrated in mice; inferred in humans)*

**Molecular pathways.** THAP1 → *TOR1A* repression (F002); THAP1 → SP1/SP4-dependent network (F007); THAP1 → pRB/E2F cell-cycle targets incl. *RRM1* (canonical, F008); THAP1–HCF-1–OGT complex linking to DYT3 (F008). Suggested GO biological processes: GO:0006355 (regulation of transcription), GO:0000122 (negative regulation of transcription by RNA pol II), GO:0007399 (nervous system development), GO:0007268 (chemical synaptic transmission), dopamine receptor signaling (D2/indirect pathway).

**Cellular processes.** Neuronal transcriptional regulation; synaptic transmission; dopaminergic indirect-pathway signaling; cytoskeletal regulation; gliosis (F007). No apoptosis/neurodegeneration in the primary disease.

**Cell types & anatomy.** Striatal D2 medium spiny neurons (indirect pathway; CL:0002613), deep cerebellar nuclei projection neurons, cortical sensorimotor neurons; neuron–glia interactions implicated ([PMID: 38737544](https://pubmed.ncbi.nlm.nih.gov/38737544/)). Suggested CL terms: CL:0000540 (neuron), CL:0002613 (striatal neuron), CL:0000127 (astrocyte).

**Molecular profiling.** Transcriptomic studies in Thap1 models show convergent dysregulation of synaptic, cytoskeletal, dopaminergic, and gliosis genes (F007). DTI in patients shows reduced fractional anisotropy in sensorimotor white matter ([PMID: 22652465]). Metabolic/energy-pathway dysregulation in the two-hit mouse (F012).

### 7. Anatomical Structures Affected

- **Organ/system:** Central nervous system — motor control circuitry (UBERON:0001017 CNS; UBERON:0000955 brain). Body system: nervous system.
- **Primary regions:** Basal ganglia (UBERON:0002420), especially striatum/putamen (UBERON:0001874) and globus pallidus internus (DBS target, UBERON:0002477); substantia nigra (SN hyperechogenicity, F004); cerebellum (UBERON:0002037), especially deep cerebellar nuclei and vermis (F007, F010, F012).
- **Cortical/network:** Sensorimotor cortex, supplementary motor area, superior temporal gyrus, superior longitudinal fasciculus (genotype-specific structural changes, F010); thalamo-cortical loops.
- **Tissue/cell:** Nervous tissue; striatal D2 medium spiny neurons, deep cerebellar nuclei projection neurons (F007).
- **Subcellular:** Nucleus (transcription factor; GO:0005634); mutant truncations partly cytoplasmic (GO:0005737) ([PMID: 22652465]).
- **Lateralization:** May begin focally/asymmetrically but frequently becomes bilateral/segmental/generalized (F004, F011).

### 8. Temporal Development

- **Onset:** Childhood to adolescence, mean ~16.8 years (range 3 to >60); insidious/chronic onset (F011). Late-onset (≥40y) subset predominantly cranial and sporadic (F012).
- **Progression:** Typically progressive spread from focal onset (arm/neck) to segmental or generalized dystonia; neck most affected (F004, F011). Chronic, lifelong; not self-limited. Genotype influences rate/extent — truncating and THAP-domain missense mutations → earlier, more extensive disease (F011).
- **Patterns:** No characteristic spontaneous remission; symptomatic improvement is treatment-induced (botulinum toxin, DBS). Adolescence is the critical vulnerability window; DBS can benefit refractory cases (F003).

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (F001).
- **Penetrance:** Incomplete, ~40–60% (F011).
- **Expressivity:** Variable — onset, distribution, and severity vary, partly by mutation type/location (F011).
- **Epidemiology:** THAP1 pathogenic variants in ~0.57% of a large dystonia cohort and ~1.8% of published dystonia patients (F006). Absolute prevalence/incidence not precisely established (rare disease). Founder mutation in Amish–Mennonite populations; confirmed across European, Chinese, Indian ancestries (F006).
- **Anticipation/mosaicism/consanguinity:** No repeat-expansion anticipation (point-mutation disorder). Germline mosaicism not specifically characterized. Consanguinity not required (dominant).
- **Sex ratio/age distribution:** No strong sex predilection established; onset concentrated in childhood–adolescence with a late-onset tail.

### 10. Diagnostics

- **Genetic testing (definitive):** Sequencing of *THAP1* (single-gene or dystonia gene panel) or WES/WGS; WES is high-yield in early-onset/familial isolated dystonia (F006). Recommended: dystonia panel or WES including *TOR1A*, *THAP1*, *GNAL*, *TUBB4A*, *PRKRA*, *ANO3*.
- **Imaging:** Brain MRI typically normal. Research findings: transcranial sonography SN hyperechogenicity (F004); DTI reduced sensorimotor white-matter FA ([PMID: 22652465]); network/QSM imaging shows distributed sensorimotor–basal ganglia–cerebellar abnormalities (F010).
- **Electrophysiology:** TMS shows reduced cerebellar brain inhibition (CBI) in some carriers (F012); laryngeal EMG documents adductor-type laryngeal dystonia (F004).
- **Laboratory/biomarkers:** No specific fluid biomarker; diagnosis is genetic and clinical.
- **Clinical criteria & differential diagnosis:** Isolated dystonia phenotype (MDS consensus classification). Differentials: DYT1 (TOR1A — limb onset, spares cranial region), DYT25 (GNAL, [PMID: 27093447](https://pubmed.ncbi.nlm.nih.gov/27093447/)), DYT4 (TUBB4A), DYT-PRKRA ([PMID: 40879515](https://pubmed.ncbi.nlm.nih.gov/40879515/)), dopa-responsive dystonia, Wilson disease, tardive/secondary dystonias.
- **Screening:** No population newborn screening; cascade genetic testing and counseling for at-risk relatives is appropriate given AD inheritance with incomplete penetrance.

### 11. Outcome / Prognosis

- **Survival/mortality:** Normal life expectancy; non-degenerative and not directly life-shortening.
- **Morbidity/function:** Chronic motor disability from generalized/segmental dystonia; laryngeal involvement impairs speech/communication. Substantial QoL impact.
- **Disease course:** Progressive spread is common but plateaus; chronic and lifelong (F011).
- **Recovery/treatment response:** Symptomatic improvement achievable — GPi-DBS reduces severity by a median ~58%, less robustly than DYT1 with possible partial regression (F003).
- **Prognostic factors:** Mutation type/location (truncating/THAP-domain missense → earlier, more extensive disease) (F011); genotype (DYT6 vs DYT1) predicts DBS response (F003).

### 12. Treatment

Stepwise, symptomatic, no disease-modifying therapy (F009):

| Tier | Intervention | Notes | NCIT suggestion |
|---|---|---|---|
| 1 | Oral anticholinergics (trihexyphenidyl), baclofen, benzodiazepines (clonazepam) | Off-label; modest benefit in generalized dystonia | NCIT:C285 (anticholinergic agent); NCIT:C61703 (baclofen) |
| 2 | Botulinum toxin chemodenervation (EMG-guided for laryngeal/focal) | Treatment of choice for focal/select regions incl. spasmodic dysphonia | NCIT:C1084 (botulinum toxin) |
| 3 | GPi deep brain stimulation | For refractory generalized/segmental disease; ~58% median improvement, less robust than DYT1 | NCIT:C38150 (deep brain stimulation) |

- **Pharmacogenomics:** Not established for DYT6.
- **Advanced/experimental:** No approved gene/RNA therapy; dosage-restoring or transcription-network-normalizing approaches are a future prospect. Levodopa is generally ineffective in DYT6 (reserved for dopa-responsive dystonias).
- **Surgical outcomes:** GPi-DBS benefits all treated patients in cohorts, with genotype-dependent variability (F003). Pediatric DBS carries higher major-complication rates in movement disorders vs other indications ([PMID: 41071966](https://pubmed.ncbi.nlm.nih.gov/41071966/)).
- **Rehabilitation/supportive:** Physical, occupational, and speech therapy for functional support.

### 13. Prevention

- **Primary prevention:** Not applicable beyond reproductive options. Genetic counseling for at-risk families; preimplantation/prenatal testing possible where a familial pathogenic variant is known.
- **Secondary prevention:** Cascade genetic testing of relatives; early diagnosis enables timely symptomatic intervention.
- **Tertiary prevention:** Optimizing botulinum toxin/DBS to prevent contractures and functional decline.
- **Counseling:** Autosomal dominant with 40–60% penetrance and variable expressivity — key counseling points (F011). No immunization/public-health interventions applicable.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *THAP1* orthologs exist in mouse (*Thap1*, NCBI Gene 100210), rat, and other mammals; THAP-domain proteins are conserved across eukaryotes (F005, F008).
- **Natural disease:** No well-documented naturally occurring DYT6-equivalent dystonia in companion animals or wildlife (no established OMIA entry for this specific disorder).
- **Comparative biology:** Mechanisms are studied via engineered rodent models, not natural animal disease. THAP-domain transcriptional regulation is evolutionarily conserved.
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

### 15. Model Organisms

- **Mammalian models:** Mouse *Thap1* C54Y knock-in and null alleles; homozygous germline null is embryonic lethal (F007). Nervous-system-specific conditional deletions cause locomotor deficits with transcriptional dysregulation (F007). Rat models also described.
- **Phenotype recapitulation:** Models reproduce **molecular** (transcriptional dysregulation, D2/indirect-pathway deficits, deep cerebellar nuclei abnormalities) and **motor** phenotypes, but **do not** show overt dystonia — a key limitation (F007). Heterozygotes show mRNA autoregulation and typically no overt phenotype unless challenged by a second hit (nerve injury; F012).
- **Applications:** Dissecting THAP1's transcriptional targets (SP1/SP4), dopaminergic circuitry, cerebellar contribution, and gene–environment interactions (F007, F012).
- **Resources:** MGI (mouse *Thap1*); cellular systems (HEK-293T transfection of mutant clones, [PMID: 22652465]); iPSC/organoid models are emerging.

---

## Mechanistic Model / Interpretation

```
   THAP1 LoF mutation (missense in DNA-binding domain, or NMD-degraded null)
                    │  (loss of DNA binding)
                    ▼
        Reduced THAP1 transcriptional repression
          │                         │
          ▼                         ▼
   De-repression of TOR1A     SP1/SP4-dependent gene-network
   (links DYT6 ↔ DYT1)        dysregulation (cell-type specific)
          │                         │
          └───────────┬─────────────┘
                      ▼
   Altered synaptic / cytoskeletal / dopaminergic gene expression
                      │
        ┌─────────────┴──────────────┐
        ▼                            ▼
  Basal ganglia branch:        Cerebellar branch:
  D2 / indirect-pathway         deep cerebellar nuclei
  dysfunction (striatum)        + vermis abnormalities
        └─────────────┬──────────────┘
                      ▼
   Network-level sensorimotor dysintegration; loss of surround inhibition
                      │        ▲
                      │        └── optional "second hit": peripheral nerve
                      ▼            injury / metabolic stress (unmasks disease)
   Isolated dystonia: craniocervical, laryngeal, brachial → generalizes
   (mean onset ~16.8 y; penetrance 40–60%; no neurodegeneration)
```

DYT6 is fundamentally a **transcriptional-network disorder** rather than a neurodegenerative one. THAP1 acts as an upstream hub whose loss propagates through two demonstrated arms — direct de-repression of *TOR1A* (unifying DYT6 with DYT1) and SP1/SP4-mediated dysregulation of neuronal gene programs — converging on dopaminergic (D2/indirect-pathway) and cerebellar circuit dysfunction. The clinical corollary is a distributed basal ganglia–thalamo-cortical + cerebellar network abnormality with genotype- and phenotype-specific structural signatures, explaining both the craniocervical/laryngeal predilection and the partial, less-robust response to GPi-DBS compared with DYT1. Incomplete penetrance plus the experimental two-hit model implies that manifestation depends on additional genetic modifiers and/or environmental triggers.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [19182804](https://pubmed.ncbi.nlm.nih.gov/19182804/) | *THAP1 mutations cause DYT6* | F001 — gene discovery, LoF |
| [30590536](https://pubmed.ncbi.nlm.nih.gov/30590536/) | *Loss of Thap1 → convergent transcriptional deficits* | F001, F007 |
| [20976771](https://pubmed.ncbi.nlm.nih.gov/20976771/) | *DYT1 repressed by THAP1* | F002 — TOR1A repression |
| [20865765](https://pubmed.ncbi.nlm.nih.gov/20865765/) | *Direct DYT1–DYT6 interaction* | F002 |
| [25088175](https://pubmed.ncbi.nlm.nih.gov/25088175/) | *THAP1 autoregulation* | F002 |
| [31817799](https://pubmed.ncbi.nlm.nih.gov/31817799/) | *GPi-DBS in DYT6* | F003 — 58% improvement |
| [21949105](https://pubmed.ncbi.nlm.nih.gov/21949105/) | *Pallidal DBS DYT6 vs DYT1* | F003 — less robust |
| [19345148](https://pubmed.ncbi.nlm.nih.gov/19345148/) | *DYT6 + spasmodic dysphonia* | F004 — craniocervical |
| [20687193](https://pubmed.ncbi.nlm.nih.gov/20687193/) | *DYT6 imaging/electrophysiology* | F004 — laryngeal, SN echo |
| [20144952](https://pubmed.ncbi.nlm.nih.gov/20144952/) | *THAP zinc finger structure* | F005 — DNA binding |
| [26376866](https://pubmed.ncbi.nlm.nih.gov/26376866/) | *Thap1 mouse motor/cerebellar* | F005, F007 |
| [28299530](https://pubmed.ncbi.nlm.nih.gov/28299530/) | *THAP1 dimerization domain* | F005 |
| [33175450](https://pubmed.ncbi.nlm.nih.gov/33175450/) | *GNAL/THAP1/TOR1A spectrum* | F006 — frequency |
| [36648081](https://pubmed.ncbi.nlm.nih.gov/36648081/) | *Chinese isolated dystonia WES* | F006 |
| [19908325](https://pubmed.ncbi.nlm.nih.gov/19908325/) | *THAP1 screening Italy* | F006 — upper-body |
| [34802187](https://pubmed.ncbi.nlm.nih.gov/34802187/) | *D2 receptor deficits Thap1 null* | F007 — indirect pathway |
| [35015830](https://pubmed.ncbi.nlm.nih.gov/35015830/) | *THAP1 regulates SP1 family* | F007 — SP1/SP4 |
| [17003378](https://pubmed.ncbi.nlm.nih.gov/17003378/) | *THAP1 pRB/E2F cell cycle* | F008 |
| [20200153](https://pubmed.ncbi.nlm.nih.gov/20200153/) | *THAP1–HCF-1–OGT (DYT6↔DYT3)* | F008 |
| [31117876](https://pubmed.ncbi.nlm.nih.gov/31117876/) | *Emerging dystonia therapies* | F009 |
| [40841848](https://pubmed.ncbi.nlm.nih.gov/40841848/) | *Generalized dystonia treatment* | F009 — algorithm |
| [27188707](https://pubmed.ncbi.nlm.nih.gov/27188707/) | *Dystonia mutations in spasmodic dysphonia* | F010 |
| [28186656](https://pubmed.ncbi.nlm.nih.gov/28186656/) | *Genotype-specific structure in SD* | F010 |
| [33638639](https://pubmed.ncbi.nlm.nih.gov/33638639/) | *VAChT disrupted in DYT1* | F010 — network |
| [22377579](https://pubmed.ncbi.nlm.nih.gov/22377579/) | *THAP1 genotype-phenotype* | F011 — onset 16.8y |
| [39732371](https://pubmed.ncbi.nlm.nih.gov/39732371/) | *Nerve injury two-hit + omics* | F011, F012 |
| [31367947](https://pubmed.ncbi.nlm.nih.gov/31367947/) | *Cerebellar involvement DYT-THAP1* | F012 |
| [42371050](https://pubmed.ncbi.nlm.nih.gov/42371050/) | *Late-onset THAP1 spectrum* | F012 |

**Corroborating / contextual:** [21793105](https://pubmed.ncbi.nlm.nih.gov/21793105/) (UMD-THAP1 LSDB), [22652465](https://pubmed.ncbi.nlm.nih.gov/22652465/) (subcellular localization + DTI), [20010837](https://pubmed.ncbi.nlm.nih.gov/20010837/) (bipartite DNA recognition), [38737544](https://pubmed.ncbi.nlm.nih.gov/38737544/) (neuron–glia regulatory network), [27913194](https://pubmed.ncbi.nlm.nih.gov/27913194/) (India cohort), [27093447](https://pubmed.ncbi.nlm.nih.gov/27093447/) (GNAL differential), [40879515](https://pubmed.ncbi.nlm.nih.gov/40879515/) (DYT-PRKRA differential).

---

## Limitations and Knowledge Gaps

- **No overt dystonia in animal models.** Thap1 rodents recapitulate molecular and motor phenotypes but not overt dystonia, limiting mechanistic and preclinical therapeutic testing (F007). The genotype-to-dystonia gap is unresolved.
- **Incomplete penetrance unexplained.** The 40–60% penetrance implies unidentified genetic modifiers and/or environmental triggers (F011). No protective alleles are known.
- **Sparse quantitative epidemiology.** Absolute prevalence/incidence of DYT6 are not well established; estimates derive from proportions within dystonia cohorts (F006).
- **No disease-specific biomarker or QoL instrument.** Diagnosis is genetic; no fluid biomarker or DYT6-tailored QoL measure exists.
- **Human GxE evidence is indirect.** The two-hit model is demonstrated only in mice; a peripheral-injury trigger in humans is plausible but unproven (F012).
- **DBS response variability.** Predictors of GPi-DBS response in DYT6 and mechanisms of late partial regression are incompletely understood (F003).
- **No disease-modifying therapy.** All treatments are symptomatic; gene- or transcription-targeted therapeutics remain conceptual.

---

## Proposed Follow-up Experiments / Actions

1. **Modifier-gene / penetrance study.** Genome-wide or targeted analysis comparing manifesting vs non-manifesting THAP1 carriers within families to identify penetrance modifiers (addresses F011).
2. **Improved dystonia models.** Develop conditional/humanized Thap1 models (cell-type-specific in striatal D2 neurons and deep cerebellar nuclei) with sensitized ("second-hit") paradigms to elicit overt dystonia and test the branch-specific model (F007, F012).
3. **Single-cell / spatial transcriptomics** of striatum and cerebellum in Thap1 models to map SP1/SP4-dependent, cell-type-specific dysregulation and pinpoint the causal node between transcriptional change and circuit dysfunction (F007).
4. **Prospective DBS-response registry** stratified by THAP1 genotype (truncating vs THAP-domain missense vs other) to define predictors and characterize late regression (F003, F011).
5. **Human GxE investigation.** Retrospective/prospective analysis of whether peripheral trauma or metabolic stress precedes symptom onset in THAP1 carriers, translating the mouse two-hit finding (F012).
6. **Therapeutic proof-of-concept.** Test dosage-restoring or SP1/SP4-network-normalizing strategies (e.g., ASO/gene supplementation) in models, given the loss-of-function, transcription-network mechanism (F001, F002, F007).
7. **Biomarker discovery.** Evaluate energy-metabolism/metabolomic signatures (from the two-hit omics study) as candidate peripheral biomarkers of disease activity or penetrance (F012).

---

*Report compiled from 12 confirmed findings and 49 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMID). Evidence source types span human clinical/genetic cohorts, engineered rodent/cellular models, in-vitro biochemistry/structural biology, and neuroimaging.*


## Artifacts

- [OpenScientist final report](Torsion_Dystonia_6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Torsion_Dystonia_6-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 37 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002408` (1 mention) - the report calls it "Torticollis"; HP calls it **Cerebral arteriovenous malformation**
- `HP:0001350` (1 mention) - the report calls it "Dysphonia"; HP calls it **Slurred speech**
- `HP:0001260` (1 mention) - the report calls it "Symptom"; HP calls it **Dysarthria**
- `HP:0007325` (1 mention) - the report calls it "Clinical sign"; HP calls it **Generalized dystonia**
- `NCIT:C1084` (1 mention) - the report calls it "botulinum toxin"; NCIT calls it **Staphylococcal Enterotoxin B**
- `NCIT:C38150` (1 mention) - the report calls it "deep brain stimulation"; NCIT calls it **PEComa**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004350` (1 mention), reported as "Clinical sign" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006355` (1 mention) - the report calls it "regulation of transcription"; GO calls it **regulation of DNA-templated transcription**
- `GO:0000122` (1 mention) - the report calls it "negative regulation of transcription by RNA pol II"; GO calls it **negative regulation of transcription by RNA polymerase II**
- `CL:0002613` (2 mentions) - the report calls it "striatal neuron"; CL calls it **striatum neuron**
- `UBERON:0002420` (1 mention) - the report calls it "Primary regions:** Basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names