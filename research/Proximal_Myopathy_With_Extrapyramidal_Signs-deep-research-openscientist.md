---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T15:02:51.674303'
end_time: '2026-10-14T15:51:48.988579'
duration_seconds: 2937.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Proximal Myopathy With Extrapyramidal Signs
  mondo_id: MONDO:0014300
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
citation_count: 10
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 14
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:24336167
  - PMID:32126877
  relevance_assessed: 18
  on_topic: 11
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 34
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.029
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002071
    reported_labels:
    - Core defining feature
    ontology_label: Abnormality of extrapyramidal motor function
  - term_id: HP:0003236
    reported_labels:
    - Frequent
    ontology_label: Elevated circulating creatine kinase activity
  - term_id: NCIT:C15351
    reported_labels:
    - NCIT suggestions:** Physical therapy
    ontology_label: Adoptive Immunotherapy
  unresolved_terms:
  - HP:0002452
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Proximal_Myopathy_With_Extrapyramidal_Signs-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Proximal_Myopathy_With_Extrapyramidal_Signs-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Proximal Myopathy With Extrapyramidal Signs
- **MONDO ID:** MONDO:0014300 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Proximal Myopathy With Extrapyramidal Signs** covering all of the
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

# Proximal Myopathy With Extrapyramidal Signs (MPXPS): Comprehensive Disease Characteristics Report

**Disease:** Proximal Myopathy With Extrapyramidal Signs (also "Myopathy With Extrapyramidal Signs," MPXPS)
**MONDO:** MONDO:0014300 | **OMIM:** 615673 | **Causal gene:** *MICU1* (HGNC:1530; OMIM 605084)
**Category:** Mendelian, autosomal recessive

---

## Summary

Proximal Myopathy With Extrapyramidal Signs (MPXPS; MONDO:0014300, OMIM 615673) is a rare, autosomal‑recessive, multisystem disorder caused by biallelic loss‑of‑function (LOF) variants in *MICU1*, the EF‑hand, calcium‑sensing **gatekeeper** of the mitochondrial calcium uniporter (MCU). Under resting cytosolic calcium, MICU1 — normally as a MICU1–MICU2 heterodimer — occludes the MCU pore and sets the threshold for mitochondrial Ca²⁺ entry. When MICU1 function is lost, this gate is removed, permitting **uncontrolled mitochondrial Ca²⁺ uptake at low cytosolic Ca²⁺**, mitochondrial Ca²⁺ overload, and severe fragmentation of the mitochondrial network. The two tissues most dependent on tightly tuned mitochondrial Ca²⁺ handling — central nervous system neurons (especially basal ganglia) and skeletal muscle — are preferentially injured, producing the clinical triad that defines the disease.

Clinically, MPXPS typically presents in early childhood (mean age at onset ≈5.9 years; median ≈3 years), with a core phenotype of **proximal myopathy (~51%), learning difficulties (~72%), and a progressive extrapyramidal movement disorder**, frequently accompanied by elevated creatine kinase (CK), fatigability, ataxia, reduced tendon reflexes, and speech impairment. The phenotype is broad: reported cases range from early congenital brain malformations and acute encephalopathy to adult‑onset and atypical distal myopathy presentations. Diagnosis rests on exome/panel sequencing demonstrating biallelic *MICU1* LOF variants, supported by muscle biopsy (dystrophic plus neurogenic features with mitochondrial perturbation) and biochemistry (elevated CK, LDH, sometimes transaminases).

No disease‑specific therapy is approved; management is supportive (physiotherapy, movement‑disorder symptom control, developmental support, surveillance). The most mechanistically rational disease‑modifying strategy — pharmacologic inhibition of the MCU channel to counteract mitochondrial Ca²⁺ overload (e.g., Ru360/Ru265‑class agents) — remains **preclinical/conceptual**. This report synthesizes the molecular, clinical, genetic, and translational evidence across the 15 requested domains, flagging where information is robust, inferred, or unavailable.

---

## Key Findings

### Finding 1 — *MICU1* loss-of-function is the cause of MPXPS, acting through primary mitochondrial Ca²⁺ dysregulation

The seminal study by **Logan et al. (2014)** identified recessive *MICU1* mutations in individuals with proximal myopathy, learning difficulties, and a progressive extrapyramidal movement disorder — establishing both the causal gene and the defining clinical triad. In patient fibroblasts, agonist‑induced mitochondrial Ca²⁺ uptake at **low** cytosolic Ca²⁺ concentrations was paradoxically **increased**, cytosolic Ca²⁺ signals were reduced, and the mitochondrial network was severely fragmented despite an unchanged resting membrane potential. This demonstrated that the disease originates in a **primary defect of mitochondrial Ca²⁺ signaling**, not in a bioenergetic collapse of membrane potential.

> "we report mutations of MICU1 in individuals with a disease phenotype characterized by proximal myopathy, learning difficulties and a progressive extrapyramidal movement disorder" — [PMID: 24336167](https://pubmed.ncbi.nlm.nih.gov/24336167/)

> "agonist-induced mitochondrial Ca(2+) uptake at low cytosolic Ca(2+) concentrations was increased, and cytosolic Ca(2+) signals were reduced … the mitochondrial network was severely fragmented" — [PMID: 24336167](https://pubmed.ncbi.nlm.nih.gov/24336167/)

### Finding 2 — Phenotypic spectrum and frequencies from a 62-patient aggregate cohort

**Beheshti et al. (2026)** combined 7 newly reported Iranian‑Turkish patients with 54 published cases (total 62; 61 deeply phenotyped), providing the most robust phenotype frequencies to date. The disease is a **rare, autosomal‑recessive, multisystem disorder caused by biallelic LOF variants in MICU1**, the calcium‑sensing gatekeeper of the MCU. Mean age at onset was **5.9 ± 7.3 years (median 3 years)**; **61.5%** presented before age 5 and **9.5%** after age 15. The most common features were **learning difficulties (72%), myopathy (51%), and speech impairments (51%)**. Expressivity is largely genotype‑driven: monozygotic twins showed an indistinguishable course, while one atypical adult‑onset patient began at 29 years with faster progression.

> "the mean age at onset was 5.9 ± 7.3 years (median = 3 years); 61.5% presented before age 5, while 9.5% manifested after 15 years" — [PMID: 40898676](https://pubmed.ncbi.nlm.nih.gov/40898676/)

> "common symptoms included learning difficulties (72%), myopathy (51%), and speech impairments (51%)" — [PMID: 40898676](https://pubmed.ncbi.nlm.nih.gov/40898676/)

> "a rare, autosomal-recessive, multisystem disorder caused by biallelic loss-of-function (LOF) variants in MICU1, the calcium-sensing gatekeeper of the mitochondrial calcium uniporter" — [PMID: 40898676](https://pubmed.ncbi.nlm.nih.gov/40898676/)

### Finding 3 — Mechanistic chain: uncontrolled mitochondrial Ca²⁺ uptake drives neurodegeneration and myopathy

Across mouse and human evidence, **Singh et al. (2022)** showed that loss of MICU1 gatekeeping produces **uncontrolled mitochondrial Ca²⁺ uptake underlying the pathogenesis of neurodegeneration**. **Kohlschmidt et al. (2021)** characterized patients carrying nonsense (p.Arg18\*, p.Arg185\*) and exon‑2 deletion variants who presented with ataxia, developmental delay, early‑onset myopathy, clinodactyly, attention deficits, insomnia, and impaired cognitive pain perception; their muscle biopsies revealed **dystrophic and neurogenic atrophy, severe mitochondrial perturbations, altered Golgi structure, vacuoles, and altered lipid homeostasis**. A recent mouse model (**Shams et al., 2026**) confirms that MICU1 LOF is associated with **proximal muscle weakness and myopathy** via elevated mitochondrial Ca²⁺.

> "presenting with ataxia, developmental delay and early onset myopathy, clinodactyly, attention deficits, insomnia and impaired cognitive pain perception" — [PMID: 33428302](https://pubmed.ncbi.nlm.nih.gov/33428302/)

> "Muscle biopsies revealed signs of dystrophy and neurogenic atrophy, severe mitochondrial perturbations, altered Golgi structure, vacuoles and altered lipid homeostasis" — [PMID: 33428302](https://pubmed.ncbi.nlm.nih.gov/33428302/)

> "MICU1 loss-of-function variants in human patients are associated with proximal muscle weakness and myopathy" — [PMID: 42349424](https://pubmed.ncbi.nlm.nih.gov/42349424/)

### Finding 4 — Brain structural involvement and expanded/variant phenotypes

**Wilton et al. (2020)** reported a child with *MICU1* variants and multiple congenital brain malformations — **anterior perisylvian polymicrogyria, dysmorphic basal ganglia, cerebellar dysplasia, and white matter abnormalities** — plus acute encephalopathy, implicating MICU1 in neurodevelopment and directly tying basal‑ganglia (extrapyramidal) pathology to the gene. **Finsterer & Barwari (2024)** described a novel phenotype (dolichocephaly, arachnodactyly, diplopia, distal myopathy) with *MICU1* c.553C>T. **Bitarafan et al. (2021)** reported a 44‑year‑old with learning disability, muscle weakness, easy fatigability, reduced tendon reflexes, ataxia, gait disturbance, elevated hepatic transaminases, and elevated CK and LDH (novel nonsense c.385C>T, p.R129\*), illustrating the diagnostic biochemical signature and late‑recognized disease.

> "she shows anterior perisylvian polymicrogyria, dysmorphic basal ganglia, and cerebellar dysplasia in addition to white matter abnormalities" — [PMID: 32395406](https://pubmed.ncbi.nlm.nih.gov/32395406/)

> "learning disability, muscle weakness, easy fatigability, reduced tendon reflexes, ataxia, gait disturbance, elevated hepatic transaminases, elevated serum creatine kinase (CK), and elevated lactate dehydrogenase (LDH)" — [PMID: 33969448](https://pubmed.ncbi.nlm.nih.gov/33969448/)

### Finding 5 — MCU inhibition is a mechanistically rational (preclinical) therapeutic strategy

Because MICU1 loss removes gatekeeping and causes mitochondrial Ca²⁺ overload, pharmacologic **inhibition of the MCU channel** is the logical countermeasure. The cell‑permeable MCU inhibitor **Ru265 "preserves cortical neuron respiration after lethal oxygen glucose deprivation and reduces hypoxic/ischemic brain injury"** (Novorolsky et al., 2020). Ru360, an MCU‑specific inhibitor, restores altered mitochondrial dynamics in independent disease models. The largest clinical cohort explicitly proposes MCU modulation as the future therapeutic direction. No MPXPS‑specific clinical trial exists; this evidence is **preclinical/conceptual**.

> "preserves cortical neuron respiration after lethal oxygen glucose deprivation and reduces hypoxic/ischemic brain injury" — [PMID: 32126877](https://pubmed.ncbi.nlm.nih.gov/32126877/)

> "Functional studies targeting MCU modulation may provide future therapeutic options." — [PMID: 40898676](https://pubmed.ncbi.nlm.nih.gov/40898676/)

### Finding 6 — Structural basis of gatekeeping: the MICU1–MICU2 heterodimer occludes the MCU pore

Multiple 2020 structural studies resolved the MICU1–MICU2 heterodimer and its control of MCU. **Wu et al. (2020)**: "The MICU1‑MICU2 heterodimer regulates the mitochondrial calcium uniporter (MCU) and mitochondrial calcium uptake." **Wang et al. (2020)** and **Park et al. (2020)** showed MICU1/MICU2 act as a Ca²⁺‑dependent gate setting the threshold for uptake. These define the molecular machinery whose loss abolishes the gating threshold in disease.

> "The MICU1-MICU2 heterodimer regulates the mitochondrial calcium uniporter (MCU) and mitochondrial calcium uptake" — [PMID: 32790952](https://pubmed.ncbi.nlm.nih.gov/32790952/)

### Finding 7 — Paralogs MICU2 and MICU3 contextualize tissue selectivity and are candidate modifiers

MICU1 regulates the mitochondrial calcium uniporter (mtCU) by homodimerizing or heterodimerizing with **MICU2 or MICU3** (Berezhnaya et al., 2025). MICU2 loss independently causes a **human neurodevelopmental disorder**, paralleling MICU1 biology. **MICU3** is a tissue‑specific enhancer of mitochondrial Ca²⁺ uptake, enriched in **neurons and skeletal muscle** (Patron et al., 2019; Ashrafi et al., 2020) — precisely the two tissues preferentially affected in MICU1 disease, offering a mechanistic rationale for its tissue selectivity and nominating MICU2/MICU3 as plausible genetic modifiers.

> "regulated by MICU1, which can be either homodimerized or heterodimerized with MICU2 or MICU3" — [PMID: 41273721](https://pubmed.ncbi.nlm.nih.gov/41273721/)

> "MICU2 loss in patients leads to a neurodevelopmental disorder" — [PMID: 41273721](https://pubmed.ncbi.nlm.nih.gov/41273721/)

### Finding 8 — Skeletal-muscle mechanism: impaired sarcolemmal membrane repair compounds Ca²⁺ overload

**Debattisti et al. (2019)** — *"Dysregulation of Mitochondrial Ca²⁺ Uptake and Sarcolemma Repair Underlie Muscle Weakness and Wasting in Patients and Mice Lacking MICU1"* — demonstrated in MICU1‑null patients and mice that "Muscle function is regulated by Ca," and that loss of MICU1 both dysregulates mitochondrial Ca²⁺ handling **and impairs repair of the injured sarcolemma (plasma membrane)**, producing myofiber weakness and wasting beyond Ca²⁺ overload alone. This complements biopsy findings of combined dystrophic + neurogenic atrophy and the recent mouse model linking elevated mitochondrial Ca²⁺ to proximal weakness.

> "Muscle function is regulated by Ca" — [PMID: 31665639](https://pubmed.ncbi.nlm.nih.gov/31665639/)

---

## Section-by-Section Report

### 1. Disease Information

MPXPS is a Mendelian, autosomal‑recessive multisystem disorder in which biallelic *MICU1* LOF produces a combined **neuromuscular + movement‑disorder** phenotype. It is best understood as a "mitochondrial calcium‑signaling disease" rather than a classic oxidative‑phosphorylation mitochondrial disease, because the primary lesion is dysregulated Ca²⁺ gating rather than loss of membrane potential (Finding 1).

- **Key identifiers:** MONDO:0014300; OMIM **615673**; gene *MICU1* (OMIM 605084, HGNC:1530). Orphanet and ICD‑10/ICD‑11/MeSH do not assign a dedicated disease‑specific code with high confidence in the reviewed sources — it is typically captured under broad categories of hereditary myopathy/muscular dystrophy with movement disorder (**not confirmed in reviewed literature; flagged as a gap**).
- **Synonyms / alternative names:** "Myopathy with extrapyramidal signs" (MPXPS); "MICU1 deficiency"; "MICU1‑related myopathy"; "MICU1‑related disorder." The disorder has been reported within limb‑girdle muscular dystrophy cohorts (e.g., a Dutch LGMD cohort reclassified one family as MICU1‑related myopathy, PMID 33386810).
- **Information source:** Predominantly **aggregated disease‑level resources and published individual case reports/series** (e.g., the 62‑patient aggregate, Finding 2), not EHR‑derived at population scale.

### 2. Etiology

**Causal factor:** Monogenic — biallelic LOF variants in *MICU1*. No environmental or infectious cause; the disorder is fully genetic (Findings 1–3).

**Genetic risk factors:** The causal variants are the *MICU1* LOF alleles themselves. Reported variant classes include nonsense (p.Arg18\*, p.Arg185\*, p.R129\* [c.385C>T], c.553C>T) and whole‑exon deletions (exon 2 / first coding exon homozygous deletions). **Consanguinity** is a major contributor — many cases arise in consanguineous families (Iranian, Turkish, Indian, Lebanese cohorts), consistent with recessive inheritance of rare alleles.

**Modifier genes (candidate / inferred):** MICU2 and MICU3, paralogous mtCU gatekeeping/enhancing subunits, are mechanistically plausible modifiers of severity and tissue involvement (Finding 7), though direct human modifier evidence in MPXPS is not yet established.

**Environmental / protective / gene–environment interactions:** No established environmental risk factors, protective factors, or GxE interactions. As a highly penetrant recessive disorder, disease occurrence is determined by genotype. **(No data — flagged as not applicable/gap.)**

### 3. Phenotypes

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Learning difficulties / intellectual disability | Behavioral / cognitive | ~72% | HP:0001328 / HP:0001249 |
| Proximal myopathy / muscle weakness | Clinical sign | ~51% | HP:0003701 / HP:0003324 |
| Speech impairment | Clinical sign | ~51% | HP:0002167 |
| Extrapyramidal / movement disorder (progressive) | Clinical sign | Core defining feature | HP:0002071 |
| Ataxia / gait disturbance | Clinical sign | Frequent | HP:0001251 / HP:0001288 |
| Elevated creatine kinase | Lab abnormality | Frequent | HP:0003236 |
| Elevated LDH | Lab abnormality | Reported | HP:0025435 |
| Elevated hepatic transaminases | Lab abnormality | Reported | HP:0002910 |
| Reduced/absent tendon reflexes | Clinical sign | Reported | HP:0001265 |
| Fatigability | Symptom | Reported | HP:0003473 |
| Clinodactyly | Physical manifestation | Reported | HP:0030084 |
| Attention deficit | Behavioral | Reported | HP:0007018 |
| Insomnia | Behavioral | Reported | HP:0100785 |
| Brain malformation (polymicrogyria, basal‑ganglia dysmorphism, cerebellar dysplasia) | Structural | Rare/severe end | HP:0002126 / HP:0002452 / HP:0001317 |

**Characteristics:** Onset is predominantly childhood (median ~3 years; 61.5% before age 5) but ranges from congenital to adult‑onset (up to 29 years). Severity is **variable**; the movement disorder is **progressive**. Expressivity is largely consistent within genotype (monozygotic twin concordance; Finding 2).

**Quality‑of‑life impact:** Combined motor (proximal weakness, movement disorder, ataxia) and cognitive/speech impairment substantially affect mobility, communication, education, and independence. Formal EQ‑5D/SF‑36/PROMIS data for MPXPS are **not available** (gap).

### 4. Genetic / Molecular Information

- **Causal gene:** *MICU1* (HGNC:1530; OMIM 605084), encoding the EF‑hand Ca²⁺‑sensing gatekeeper of the MCU.
- **Pathogenic variants:** Nonsense (p.Arg18\*, p.Arg185\*, p.R129\*/c.385C>T, c.553C>T) and structural (homozygous deletion of exon 2 / first coding exon). All reported disease alleles are **loss‑of‑function**; the mechanism is **loss of gatekeeping function** of the mtCU (Findings 1–3, 8).
- **Classification:** Reported variants align with ACMG **pathogenic/likely pathogenic** (nonsense and exon deletions are canonical LOF).
- **Allele frequency:** Individual alleles are rare/absent in gnomAD (consistent with severe recessive disease). Exact per‑variant frequencies not tabulated here (gap).
- **Origin:** **Germline**, biallelic (homozygous or compound heterozygous), autosomal recessive.
- **Functional consequence:** Loss of function → loss of MICU1‑mediated threshold gating of MCU → uncontrolled mitochondrial Ca²⁺ uptake.
- **Modifier genes:** MICU2, MICU3 (candidate; Finding 7).
- **Epigenetic / chromosomal:** No disease‑specific epigenetic signature or recurrent chromosomal abnormality reported (gap), aside from the exon‑level deletions noted.

### 5. Environmental Information

No environmental, lifestyle, or infectious agents are implicated. MPXPS is purely monogenic. **(Not applicable.)**

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LOF mutation in *MICU1*** (nonsense, exon deletion) → **leads to** loss/absence of functional MICU1 protein.
2. Loss of MICU1 → **removes** the MICU1–MICU2 heterodimeric gate that normally occludes the MCU pore at resting cytosolic Ca²⁺ (*demonstrated structurally*, Finding 6).
3. Loss of gating → **results in** a lowered activation threshold and **uncontrolled mitochondrial Ca²⁺ uptake at low cytosolic Ca²⁺**, with reduced cytosolic Ca²⁺ signals (*demonstrated in patient fibroblasts*, Finding 1).
4. Uncontrolled uptake → **causes** mitochondrial Ca²⁺ overload and **severe fragmentation of the mitochondrial network** (*demonstrated*, Finding 1).
5. Mitochondrial Ca²⁺ overload → **drives** (branch A, CNS) neuronal dysfunction and **neurodegeneration**, with structural basal‑ganglia/cerebellar/cortical abnormalities → **progressive extrapyramidal movement disorder, ataxia, learning/speech difficulties** (*mouse + patient*, Findings 3, 4).
6. Mitochondrial Ca²⁺ overload → **drives** (branch B, muscle) myofiber injury; additionally MICU1 loss **impairs mitochondria‑dependent sarcolemmal (plasma membrane) repair** → combined dystrophic + neurogenic atrophy → **proximal myopathy, weakness, wasting, elevated CK** (*patient + mouse*, Findings 3, 8).

**Supporting detail by category:**
- **Molecular pathway:** Mitochondrial Ca²⁺ uniporter (mtCU) signaling — MICU1/MICU2 gating of the MCU pore (Ca²⁺ transport across inner mitochondrial membrane). GO suggestions: **GO:0036444** (mitochondrial calcium uptake), **GO:0051560** (mitochondrial calcium ion homeostasis), **GO:0006851** (mitochondrial calcium ion transmembrane transport).
- **Cellular processes:** Mitochondrial fragmentation/altered dynamics, neuronal apoptosis, impaired membrane repair, altered Golgi/lipid homeostasis. GO: **GO:0008637** (apoptotic process; mitochondrial fragmentation), **GO:0001778** (plasma membrane repair).
- **Protein dysfunction:** Loss of function of the MICU1 EF‑hand Ca²⁺ sensor; abolished gatekeeping of MCU (UniProt Q9BPX6).
- **Metabolic changes:** Secondary bioenergetic stress from Ca²⁺ overload; altered lipid homeostasis in muscle.
- **Tissue damage mechanisms:** Mitochondrial Ca²⁺ overload → oxidative/mitochondrial stress and cell death in neurons; myofiber injury with defective repair.
- **Cell types (CL):** Skeletal muscle myofiber (**CL:0000188**), neuron (**CL:0000540**), basal‑ganglia neurons.
- **Immune involvement:** Not a primary feature.

### 7. Anatomical Structures Affected

- **Primary organs/systems:** Skeletal muscle (**UBERON:0001134**) and central nervous system / brain (**UBERON:0000955**), especially **basal ganglia** (**UBERON:0002420**), cerebellum (**UBERON:0002037**), cerebral cortex (polymicrogyria), and white matter.
- **Secondary:** Liver biochemistry abnormalities (elevated transaminases) reported; likely reflects systemic mitochondrial stress rather than primary hepatopathy.
- **Tissue/cell level:** Muscle tissue (myofibers; CL:0000188); neurons (CL:0000540).
- **Subcellular (GO Cellular Component):** **Mitochondrion** (**GO:0005739**), mitochondrial inner membrane (**GO:0005743**); also implicated Golgi apparatus and plasma membrane/sarcolemma (repair defect).
- **Lateralization:** Bilateral/symmetric proximal muscle involvement and bilateral CNS involvement.

### 8. Temporal Development

- **Onset:** Predominantly early childhood (median ~3 years; 61.5% before age 5); ranges congenital → adult (to 29 years). Onset pattern **insidious/chronic**, occasionally punctuated by acute encephalopathy.
- **Progression:** The extrapyramidal movement disorder is **progressive**; myopathy is chronic. Rate is variable and partly genotype‑dependent (adult‑onset case progressed faster; Finding 2).
- **Course:** Chronic, lifelong. No spontaneous remission reported. A critical window for any future MCU‑targeted intervention is plausibly early (before irreversible neurodegeneration), but this is **inferred**, not demonstrated.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; biallelic LOF.
- **Penetrance / expressivity:** Appears highly penetrant; expressivity variable but genotype‑consistent (MZ‑twin concordance).
- **Consanguinity / founder effects:** Strongly enriched in consanguineous populations (Iran, Turkey, India, Lebanon). No defined global founder allele, but recurrent population‑specific variants exist.
- **Epidemiology:** Ultra‑rare; exact prevalence/incidence undefined. The literature comprises ~62 aggregated patients worldwide (Finding 2) — prevalence is below defined rare‑disease thresholds and not formally quantified (gap).
- **Sex ratio:** Autosomal recessive — expected ~1:1; no strong sex bias reported.
- **Carrier frequency:** Not established (gap).

### 10. Diagnostics

- **Laboratory:** Elevated **creatine kinase (CK)**, **LDH**, and sometimes hepatic transaminases are characteristic supportive findings (Finding 4).
- **Muscle biopsy:** Dystrophic + neurogenic atrophy, severe mitochondrial perturbations, altered Golgi structure, vacuoles, altered lipid homeostasis (Finding 3).
- **Imaging:** Brain MRI may reveal basal‑ganglia dysmorphism, polymicrogyria, cerebellar dysplasia, and white‑matter abnormalities in severe/early cases (Finding 4).
- **Genetic testing (definitive):** **WES/WGS or a muscular‑dystrophy/neuromuscular gene panel** including *MICU1*; confirm biallelic LOF variants. Exon‑deletion detection may require MLPA/CNV analysis (homozygous exon 2 deletions have been reported). The disorder is frequently diagnosed within broad LGMD/muscular‑dystrophy WES programs (PMIDs 33386810, 42553504).
- **Differential diagnosis:** Limb‑girdle muscular dystrophies, congenital/metabolic/mitochondrial myopathies, and other inherited movement disorders; the combination of proximal myopathy + progressive extrapyramidal signs + learning difficulty + raised CK points to MICU1.
- **Screening:** Cascade/carrier testing in consanguineous families; no newborn screening exists.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics; the disorder is chronic and multisystem. Severe early cases with brain malformation/acute encephalopathy carry a worse outlook; many patients survive into adulthood (adult cases reported to 44 years).
- **Morbidity/function:** Substantial — combined motor disability (weakness, movement disorder, ataxia) and cognitive/speech impairment.
- **Disease course:** Progressive movement disorder; chronic myopathy. Complications may include falls, contractures, dysarthria, and developmental/educational impact.
- **Prognostic factors:** Age/mode of onset and genotype appear to influence course (adult‑onset faster progression in one case; MZ‑twin concordance indicates genotype‑driven prognosis). No validated prognostic biomarkers (gap).

### 12. Treatment

- **Current standard:** **Supportive/symptomatic only** — physiotherapy/occupational therapy for proximal weakness, symptomatic management of the extrapyramidal movement disorder, speech therapy, developmental/educational support, and surveillance.
- **Disease‑modifying (preclinical/conceptual):** **MCU channel inhibition** to counteract mitochondrial Ca²⁺ overload — e.g., **Ru360** and the cell‑permeable **Ru265** (neuroprotective in ischemia models; Finding 5). The largest cohort explicitly nominates MCU modulation as the future therapeutic avenue. **No MPXPS‑specific clinical trial (no NCT) currently exists.**
- **Pharmacogenomics / gene / cell / RNA therapies:** None established; gene‑replacement or ASO strategies are theoretically plausible for a recessive LOF gene but untested (gap).
- **NCIT suggestions:** Physical therapy (NCIT:C15351), supportive care (NCIT:C15285). MCU inhibitors are investigational and lack NCIT clinical‑intervention codes.

### 13. Prevention

- **Primary prevention:** Not applicable (monogenic). **Genetic counseling** for consanguineous families and at‑risk couples; carrier/cascade testing; prenatal or preimplantation genetic testing when a familial variant is known.
- **Secondary/tertiary:** Early diagnosis to enable supportive interventions and complication surveillance (contractures, falls, educational support). No population screening program exists.

### 14. Other Species / Natural Disease

- **Model-organism relevance (see Section 15).** No naturally occurring MPXPS‑equivalent disease is documented in companion animals or wildlife in the reviewed literature (gap; OMIA not confirmed).
- **Orthology:** *MICU1* is evolutionarily conserved (mouse *Micu1*; NCBI Gene). Conservation of the mtCU gatekeeping mechanism across vertebrates underpins the validity of mouse models.
- **Zoonotic potential:** Not applicable (genetic disease).

### 15. Model Organisms

- **Mouse (*Mus musculus*):** MICU1‑deficient/LOF mice recapitulate core disease biology — **uncontrolled mitochondrial Ca²⁺ uptake and neurodegeneration** (Singh et al., 2022, PMID 35302860), **muscle weakness and wasting with defective sarcolemma repair** (Debattisti et al., 2019, PMID 31665639), and **proximal muscle weakness from elevated mitochondrial Ca²⁺** (Shams et al., 2026, PMID 42349424). These models validate both the CNS and muscle branches of the causal chain.
- **Cellular / in vitro:** Patient‑derived fibroblasts demonstrating increased mitochondrial Ca²⁺ uptake at low cytosolic Ca²⁺ and network fragmentation (Logan et al., 2014); structural studies of MICU1–MICU2 heterodimers.
- **Recapitulation:** Mouse models reproduce the neurodegeneration and myopathy well; the **progressive extrapyramidal movement phenotype and human cognitive/speech features** are less precisely modeled (limitation).
- **Resources:** MGI (*Micu1*); model details in the cited primary literature.

---

## Mechanistic Model / Interpretation

```
 Biallelic MICU1 LOF (nonsense / exon deletion)
            │  (removes gatekeeper subunit)
            ▼
 Loss of MICU1–MICU2 heterodimeric gate on MCU pore   [structurally demonstrated]
            │  (lowers Ca2+ activation threshold)
            ▼
 Uncontrolled mitochondrial Ca2+ uptake at LOW cytosolic Ca2+;  reduced cytosolic Ca2+
            │
            ▼
 Mitochondrial Ca2+ OVERLOAD  +  severe mitochondrial network FRAGMENTATION
            │
       ┌────┴─────────────────────────────┐
       ▼ (CNS branch)                      ▼ (Muscle branch)
 Neuronal dysfunction /            Myofiber Ca2+ stress  +  IMPAIRED
 neurodegeneration; basal-         sarcolemma (plasma membrane) REPAIR
 ganglia/cerebellar/cortical       │
 structural abnormality            ▼
       │                           Dystrophic + neurogenic atrophy; ↑CK/LDH
       ▼
 Progressive extrapyramidal        Proximal MYOPATHY, weakness, wasting
 movement disorder, ataxia,
 learning & speech difficulty
```

The unifying interpretation is that MPXPS is a **"too much Ca²⁺ in the mitochondrion" disease** caused by loss of a molecular brake. This stands in instructive contrast to several other conditions in the reviewed literature where the *MICU1:MCU ratio* falls (sepsis‑induced ICU‑acquired weakness, PMID 37695737; diabetic vascular remodeling, PMID 40673552) — in those settings reduced MICU1 similarly dysregulates mitochondrial Ca²⁺ and weakens muscle, reinforcing that MICU1 dosage/gatekeeping is a pivotal node for both muscle and neuronal integrity. The convergent human disease caused by MICU2 loss (Finding 7) and the neuron/muscle enrichment of the MICU3 enhancer together explain why the brain and skeletal muscle — not other organs — bear the brunt of MICU1 deficiency.

---

## Evidence Base

| PMID | Study | Type | Role in this report |
|---|---|---|---|
| [24336167](https://pubmed.ncbi.nlm.nih.gov/24336167/) | Logan et al. 2014 | Human + fibroblast | Establishes *MICU1* causation, triad, and Ca²⁺ mechanism (F1) |
| [40898676](https://pubmed.ncbi.nlm.nih.gov/40898676/) | Beheshti et al. 2026 | Human cohort (n=62) | Phenotype frequencies, onset, inheritance, therapy direction (F2, F5) |
| [35302860](https://pubmed.ncbi.nlm.nih.gov/35302860/) | Singh et al. 2022 | Mouse + patient | Uncontrolled mito Ca²⁺ → neurodegeneration (F3) |
| [33428302](https://pubmed.ncbi.nlm.nih.gov/33428302/) | Kohlschmidt et al. 2021 | Human | Expanded phenotype; muscle biopsy pathology (F3) |
| [42349424](https://pubmed.ncbi.nlm.nih.gov/42349424/) | Shams et al. 2026 | Mouse | Elevated mito Ca²⁺ → proximal weakness (F3) |
| [32395406](https://pubmed.ncbi.nlm.nih.gov/32395406/) | Wilton et al. 2020 | Human | Brain malformation incl. basal ganglia (F4) |
| [33969448](https://pubmed.ncbi.nlm.nih.gov/33969448/) | Bitarafan et al. 2021 | Human | Adult case; CK/LDH/transaminase signature (F4) |
| [31665639](https://pubmed.ncbi.nlm.nih.gov/31665639/) | Debattisti et al. 2019 | Patient + mouse | Sarcolemma repair defect in muscle (F8) |
| [32790952](https://pubmed.ncbi.nlm.nih.gov/32790952/) | Wu et al. 2020 | Structural | MICU1–MICU2 heterodimer gates MCU (F6) |
| [32667285](https://pubmed.ncbi.nlm.nih.gov/32667285/) | Wang et al. 2020 | Structural | Gatekeeping threshold mechanism (F6) |
| [32148862](https://pubmed.ncbi.nlm.nih.gov/32148862/) | Park et al. 2020 | Structural | Heterodimer threshold shift (F6) |
| [41273721](https://pubmed.ncbi.nlm.nih.gov/41273721/) | Berezhnaya et al. 2025 | Human + mouse | MICU2/MICU3 paralog architecture; MICU2 disease (F7) |
| [29725115](https://pubmed.ncbi.nlm.nih.gov/29725115/) | Patron et al. 2019 | In vitro | MICU3 tissue‑specific enhancer (F7) |
| [31862210](https://pubmed.ncbi.nlm.nih.gov/31862210/) | Ashrafi et al. 2020 | Neuronal | MICU3 axonal/neuronal enrichment (F7) |
| [32126877](https://pubmed.ncbi.nlm.nih.gov/32126877/) | Novorolsky et al. 2020 | Neuronal model | Ru265 neuroprotection → MCU‑inhibition rationale (F5) |
| [33386810](https://pubmed.ncbi.nlm.nih.gov/33386810/) | Dutch LGMD cohort | Human cohort | MICU1 found within LGMD diagnostic programs |

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** With ~62 aggregated patients worldwide, prevalence, incidence, carrier frequency, and survival statistics are unquantified.
2. **ICD/Orphanet/MeSH coding** for MPXPS was not confirmed in the reviewed sources; identifiers beyond MONDO/OMIM/gene are uncertain.
3. **Phenotype frequencies** derive largely from literature‑aggregated case reports (ascertainment and reporting bias likely over‑represent severe cases).
4. **Therapy is unproven.** MCU inhibition is mechanistically rational but entirely preclinical; no NCT, no human efficacy/safety data in MPXPS; chronic MCU inhibition risks impairing physiological mitochondrial Ca²⁺ signaling.
5. **Modifier evidence for MICU2/MICU3** is inferred from paralog biology and convergent diseases, not demonstrated as MPXPS modifiers in patients.
6. **Movement‑disorder phenotype is imperfectly modeled** in mice; the mechanistic link from basal‑ganglia mitochondrial Ca²⁺ overload to the specific extrapyramidal signs remains partly inferred.
7. **No quality‑of‑life (EQ‑5D/SF‑36/PROMIS) or natural‑history registry data** specific to MPXPS.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a natural‑history registry** for MICU1/MICU2 patients to quantify onset, progression rates, survival, and genotype–phenotype correlations prospectively.
2. **Preclinical MCU‑inhibitor efficacy studies** (Ru265/next‑generation cell‑permeable MCU inhibitors) in MICU1‑LOF mice, with CNS and muscle endpoints, defining the therapeutic window and chronic‑dosing safety.
3. **Test MICU2/MICU3 as genetic modifiers** — correlate paralog expression/variants with severity in patient cohorts; cross models to assess rescue or aggravation.
4. **Deep muscle‑repair mechanistic work** to determine whether enhancing sarcolemmal repair (independent of Ca²⁺) ameliorates myopathy.
5. **Standardized brain imaging + movement‑disorder phenotyping protocol** to improve detection of basal‑ganglia involvement and track extrapyramidal progression.
6. **Variant curation** — compile all reported *MICU1* alleles in ClinVar with ACMG classifications, gnomAD frequencies, and CNV (exon‑deletion) detection recommendations for diagnostic labs.
7. **Formal ontology/identifier reconciliation** (Orphanet, ICD‑11, MeSH) to complete the knowledge‑base entry.

---

*Evidence source legend:* human clinical (Logan 2014; Beheshti 2026; Kohlschmidt 2021; Wilton 2020; Bitarafan 2021; Debattisti 2019 patients), model organism (Singh 2022; Shams 2026; Debattisti 2019 mice), in vitro/structural (Wu/Wang/Park 2020; Patron 2019; Ashrafi 2020), computational/mechanistic inference (MCU‑inhibition rationale; modifier hypotheses).


## Artifacts

- [OpenScientist final report](Proximal_Myopathy_With_Extrapyramidal_Signs-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Proximal_Myopathy_With_Extrapyramidal_Signs-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 18 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24336167` *(abstract only)*: "agonist-induced mitochondrial Ca(2+) uptake at low cytosolic Ca(2+) concentrations was increased, and cytosolic Ca(2+) signals were reduced … the mitochondrial network was severely fragmented"
  - closest text in source: "In fibroblasts from subjects with MICU1 mutations, agonist-induced mitochondrial Ca(2+) uptake at low cytosolic Ca(2+) concentrations was increased, and cytosolic Ca(2+) signals were reduced"
- `PMID:32126877` *(abstract only)*: "preserves cortical neuron respiration after lethal oxygen glucose deprivation and reduces hypoxic/ischemic brain injury"
  - closest text in source: "Unlike Ru360, Ru265 (2-10 µM) reached intracellular concentrations in cultured cortical neurons that preserved cell viability, blocked the protease activity of Ca2+-dependent calpains and maintained mitochondrial respiration and glycolysis after a lethal period of oxygen-glucose deprivation (OGD)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002071` (1 mention) - the report calls it "Core defining feature"; HP calls it **Abnormality of extrapyramidal motor function**
- `HP:0003236` (1 mention) - the report calls it "Frequent"; HP calls it **Elevated circulating creatine kinase activity**
- `NCIT:C15351` (1 mention) - the report calls it "NCIT suggestions:** Physical therapy"; NCIT calls it **Adoptive Immunotherapy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002452` (1 mention) - HP does not contain this term