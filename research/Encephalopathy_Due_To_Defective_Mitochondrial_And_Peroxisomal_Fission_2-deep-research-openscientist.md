---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-16T20:45:06.462530'
end_time: '2026-09-16T21:18:44.468908'
duration_seconds: 2018.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Encephalopathy Due To Defective Mitochondrial And Peroxisomal Fission
    2
  mondo_id: MONDO:0014905
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 23
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014905
    reported_labels:
    - MONDO
    ontology_label: encephalopathy due to defective mitochondrial and peroxisomal
      fission 2
  - term_id: DOID:0060994
    reported_labels:
    - DOID
    ontology_label: encephalopathy due to defective mitochondrial and peroxisomal
      fission 2
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Encephalopathy Due To Defective Mitochondrial And Peroxisomal Fission 2
- **MONDO ID:** MONDO:0014905 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Encephalopathy Due To Defective Mitochondrial And Peroxisomal Fission 2** covering all of the
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

# Encephalopathy Due To Defective Mitochondrial And Peroxisomal Fission 2 (EMPF2)

**Disease Knowledge Base Research Report**
**MONDO:0014905 · OMIM #617086 · Orphanet 485421 · Gene: *MFF* (HGNC:24858)**

---

## Summary

**Encephalopathy due to defective mitochondrial and peroxisomal fission 2 (EMPF2)** is an ultra-rare, autosomal-recessive neurodevelopmental/neurodegenerative disorder caused by biallelic **loss-of-function variants in the *MFF* gene** (mitochondrial fission factor). MFF is the outer-membrane receptor that recruits the dynamin-related GTPase **DRP1/DNM1L** to the surface of mitochondria and peroxisomes to execute organelle scission. When MFF is absent, this shared fission machinery cannot be assembled, and affected cells accumulate hyper-elongated, net-like mitochondria and elongated peroxisomes. The disease was first delineated as a distinct entity by Koch and colleagues in 2016 ([PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/)).

Clinically, EMPF2 presents in the **first year of life** with developmental delay, **acquired (secondary) microcephaly**, spasticity and hyperreflexia, seizures (frequently infantile spasms with hypsarrhythmia), optic atrophy, and peripheral neuropathy. Brain MRI shows a **Leigh-like pattern** with bilateral basal-ganglia and subthalamic-nucleus signal change, yet — in a key biochemical distinction from classic Leigh syndrome — **mitochondrial respiratory-chain enzyme activities in skeletal muscle are typically normal**. The disorder is closely related to and is the principal differential diagnosis of **EMPF1** (caused by variants in *DNM1L*/DRP1), because both diseases disrupt the same fission pathway.

There is **no disease-specific therapy**; management is entirely supportive (seizure control, spasticity management, nutrition/feeding support, visual and physical rehabilitation). The strongest mechanistic lead toward a rational therapy comes from mouse genetics: reducing mitochondrial **fusion** (via *Mfn1* deletion) fully rescues the *Mff*-null phenotype, identifying **fission/fusion rebalancing** as a promising therapeutic direction. Naturally occurring animal models exist in *Mff*-knockout mice (fatal dilated cardiomyopathy) and in Bullmastiff dogs carrying a homozygous *MFF* frameshift variant, providing translational platforms.

---

## Key Findings

### Finding 1 — EMPF2 is caused by biallelic loss-of-function *MFF* variants that disrupt DRP1-mediated fission of both mitochondria and peroxisomes

The defining discovery, by Koch et al. (2016), came from exome sequencing of index patients from two families. As the authors state, *"Exome sequencing revealed three different biallelic loss-of-function variants in MFF in both index cases"* ([PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/)). Western blotting demonstrated **absent MFF protein**, and patient fibroblasts displayed **elongated mitochondria and elongated peroxisomes**, directly linking the genotype to an organelle-division defect.

Mechanistically, MFF is the outer-mitochondrial-membrane (and peroxisomal-membrane) receptor that recruits the fission GTPase DRP1/DNM1L. As Liu and Chan's work summarizes, *"the OMM protein mitochondrial fission factor (Mff) is a key receptor for recruiting Drp1 from the cytosol to the mitochondrion"* ([PMID: 34347505](https://pubmed.ncbi.nlm.nih.gov/34347505/)). Because *"components of the fission machinery are partly shared between mitochondria and peroxisomes"* ([PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/)), loss of MFF simultaneously impairs the division of **both** organelles — the molecular basis for the disease name.

This establishes the disease as an **autosomal-recessive loss-of-function disorder** confirmed across multiple unrelated patients.

### Finding 2 — Core clinical phenotype: early-infantile Leigh-like encephalopathy with acquired microcephaly, seizures, spasticity, optic atrophy and peripheral neuropathy, but normal muscle respiratory-chain activity

Koch et al. describe the natural history precisely: *"The patients became symptomatic within the first year of life, exhibiting seizures, developmental delay and acquired microcephaly. Dysphagia, spasticity and optic and peripheral neuropathy developed subsequently"* ([PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/)). Neuroimaging showed a characteristic pattern: *"Brain MRI showed Leigh-like patterns with bilateral changes of the basal ganglia and subthalamic nucleus."*

A crucial diagnostic distinction from classic Leigh syndrome is that *"activities of mitochondrial respiratory chain complexes were found to be normal in skeletal muscle"* ([PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/)). This tells clinicians that a normal muscle biopsy respiratory-chain panel does **not** exclude EMPF2 — the disease is one of organelle *morphology/dynamics*, not primary OXPHOS enzyme deficiency.

An independent patient reported by Panda et al. (2020) corroborated the phenotype and added a specific pathogenic variant: an Indian child with *"global developmental followed by regression of acquired milestones, spasticity, visual and auditory impairment, and was found to harbor a novel pathogenic homozygous MFF truncating variant c.433C>T; p.Arg145Ter"* ([PMID: 32181496](https://pubmed.ncbi.nlm.nih.gov/32181496/)).

### Finding 3 — Downstream mechanism: peroxisome-maturation failure plus mitochondrial Ca²⁺ overload and oxidative stress link organelle dynamics to neuronal dysfunction

Beyond simple elongation, loss of MFF produces functional organelle defects. Passmore et al. (2020) showed that *"loss of MFF results in reduced import-competence of the peroxisomal compartment and leads to the accumulation of pre-peroxisomal membrane structures"* and that *"peroxisomes in MFF-deficient cells display alterations in peroxisomal redox state and intra-peroxisomal pH"* ([PMID: 32224193](https://pubmed.ncbi.nlm.nih.gov/32224193/)). Thus MFF is a critical regulator of **peroxisome maturation**, not merely division.

On the mitochondrial/neuronal side, Sun et al. (2022) differentiated dopaminergic neurons from dental-pulp stem cells with MFF insufficiency and observed impaired neurite outgrowth, elongated mitochondria confined to neurites, and **mitochondrial Ca²⁺-triggered oxidative stress** ([PMID: 35883852](https://pubmed.ncbi.nlm.nih.gov/35883852/)) — connecting the fission defect to the kind of neuronal energetic/oxidative failure that could underlie a Leigh-like phenotype.

In vivo, Chen et al. (2015) showed that *"mutant tissue showed reduced mitochondrial density and respiratory chain activity along with increased mitophagy"* in *Mff*-null mice, and — critically — that *"concomitant deletion of the mitochondrial fusion gene Mfn1 completely rescued heart dysfunction, life span, and respiratory chain function"* ([PMID: 26598616](https://pubmed.ncbi.nlm.nih.gov/26598616/)). This demonstrates the disease is driven by a **fission/fusion imbalance** and is, in principle, reversible by rebalancing organelle dynamics.

### Finding 4 — Naturally occurring and engineered animal models

A **naturally occurring canine model** was identified by Christen et al. (2022): two young Bullmastiffs with progressive gait/behavioural abnormalities (onset ~6 months) and bilateral symmetrical cerebellar-nuclei MRI lesions carried a private homozygous *MFF* frameshift variant. As reported, *"This search revealed a private homozygous frameshift variant in the MFF gene in the affected dog"* (XM_038574000.1:c.471_475delinsCGCTCT, p.(Glu158Alafs*14), truncating ~55% of the ORF), with perfect autosomal-recessive segregation across 4 affected and 70 unaffected dogs. The authors explicitly connect this to the human disease: *"Human patients with pathogenic MFF variants suffer from 'encephalopathy due to defective mitochondrial and peroxisomal fission 2'"* ([PMID: 36085405](https://pubmed.ncbi.nlm.nih.gov/36085405/)).

The **mouse knockout** is more severe systemically: *"Mff mutant mice die at 13 wk as a result of severe dilated cardiomyopathy leading to heart failure"* ([PMID: 26598616](https://pubmed.ncbi.nlm.nih.gov/26598616/)), reflecting the high energetic demand of cardiac tissue.

### Finding 5 — MFF is a physiological AMPK substrate coupling energy stress to fission

MFF sits at a regulatory node linking cellular energy status to mitochondrial dynamics. Zong et al. (2019) showed that *"mitochondrion-localized AMPK is activated to phosphorylate ACC2 and mitochondrial fission factor (MFF) only during severe nutrient stress"* ([PMID: 30948787](https://pubmed.ncbi.nlm.nih.gov/30948787/)). Peng et al. (2022) confirmed that *"the AMPK pathway promoted mitochondrial fission and mitophagy by increasing the recruitment of dynamin-related protein 1 (DRP1) to the mitochondrial outer membrane"* ([PMID: 36374514](https://pubmed.ncbi.nlm.nih.gov/36374514/)). This AMPK→MFF→DRP1 axis is precisely the function lost in EMPF2, and it frames why energy-stressed neurons might be especially vulnerable.

### Finding 6 — EMPF2 is the recessive counterpart of EMPF1 (*DNM1L*/DRP1)

EMPF2 and **EMPF1** disrupt the same fission pathway at adjacent steps (receptor vs. effector GTPase). Keller/Verrigni et al. note that *"Autosomal dominant and recessive variants in DNM1L cause encephalopathy due to defective mitochondrial and peroxisomal fission 1 (EMPF1), which presents as a complex and clinically heterogeneous neurological disorder of variable severity, often accompanied by seizures"* ([PMID: 33387674](https://pubmed.ncbi.nlm.nih.gov/33387674/)). DRP1's role is confirmed: it is *"a cytosolic protein encoded by dynamin 1-like (DNM1L) gene, which relocalizes to the outer mitochondrial membrane, where it assembles, oligomerizes and drives mitochondrial division"* ([PMID: 31868880](https://pubmed.ncbi.nlm.nih.gov/31868880/)). EMPF1 is therefore the primary genetic differential diagnosis of EMPF2.

### Finding 7 — Verified identifiers and cross-references

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014905 |
| OMIM (phenotype) | #617086 |
| Orphanet | ORPHA:485421 |
| DOID | DOID:0060994 |
| GARD | 0017881 |
| MedGen | 934693 |
| UMLS | C4310726 |
| Gene (NCBI) | *MFF*, Gene ID 56947 |
| HGNC | HGNC:24858 |
| Gene OMIM | 614785 |
| Ensembl | ENSG00000168958 |
| Locus | 2q36.3 (GRCh38 chr2:227,325,151–227,361,188, + strand) |
| Aliases | C2orf33, GL004, EMPF2 |
| Ontology synonym | "Leigh-like basal ganglia disease-optic atrophy-peripheral neuropathy syndrome" |

The RefSeq summary states the encoded protein *"recruits dynamin-1-like protein (DNM1L) to mitochondria."* Multiple splice transcript variants and processed pseudogenes (chr 1, 5, X) exist.

### Finding 8 — Quantitative HPO phenotype spectrum and frequencies

Curated HPO annotations for OMIM:617086 / MONDO:0014905 (primary source [PMID: 26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/), n=4 patients unless noted):

| Phenotype | HPO term | Frequency |
|---|---|---|
| Infantile onset | HP:0003593 | 4/4 |
| Secondary (acquired) microcephaly | HP:0005484 | 4/4 |
| Spasticity | HP:0001257 | 4/4 |
| Hyperreflexia | HP:0001347 | 4/4 |
| Motor delay | HP:0001270 | 4/4 |
| Seizure | HP:0001250 | 3/4 |
| Epileptic spasm | HP:0011097 | 2/4 |
| Hypsarrhythmia | HP:0002521 | 3/3 |
| Developmental regression | HP:0002376 | 3/3 |
| Hypotonia | HP:0001252 | 3/3 |
| Muscle weakness | HP:0001324 | 3/3 |
| Dysphagia | HP:0002015 | 3/3 |
| Visual impairment | HP:0000505 | 3/4 |
| Optic disc pallor | HP:0000543 | 3/4 |
| External ophthalmoplegia | HP:0000544 | 3/4 |
| Absent speech | HP:0001344 | 3/4 |
| Cerebellar atrophy | HP:0001272 | 2/3 |
| Growth delay | HP:0001510 | 1/3 |
| Death in childhood | HP:0003819 | 1/4 |
| Optic atrophy | HP:0000648 | OMIM-listed |
| Global developmental delay | HP:0001263 | OMIM-listed |
| Peripheral neuropathy | HP:0009830 | OMIM-listed |
| Inability to walk | HP:0002540 | OMIM-listed |
| Autosomal recessive inheritance | HP:0000007 | (Shamseldin 2012, PMID:22499341) |

### Finding 9 — ClinVar variant spectrum supports the loss-of-function mechanism

A ClinVar query (2026) returned ~251 *MFF* variant records, of which 58 are classified Pathogenic/Likely-pathogenic. The gene-specific P/LP variants are **predominantly loss-of-function**: splice-site (e.g., NM_001277062.2:c.181+2T>A, c.352-2A>C, deep-intronic c.440+2432G>T, c.-40-842G>T), frameshift (c.159del p.Pro54fs), and truncating changes such as c.433C>T (p.Arg145Ter). By contrast, reported **missense** variants (c.226C>G p.Leu76Val; c.611G>A p.Arg204His; c.382C>T p.Arg128Trp; c.223G>A p.Asp75Asn) are largely classified as **Variants of Uncertain Significance (VUS)**. Several "Pathogenic" entries are large 2q chromosomal copy-number gains that merely overlap *MFF* and are not EMPF2-causing. This distribution is consistent with a haploinsufficiency/loss-of-function disease requiring biallelic null or near-null alleles.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *MFF*** (nonsense, frameshift, splice-site, or deletion) → **absent or non-functional MFF protein** (demonstrated: Western blot shows absent protein — PMID:26783368).
2. Absent MFF → **failure to recruit the DRP1/DNM1L GTPase** to the outer membranes of mitochondria and peroxisomes (mechanistically established; MFF is the DRP1 receptor — PMID:34347505).
3. No DRP1 recruitment → **no assembly of the scission machinery** → **organelle fission arrest** → **hyper-elongated, net-like mitochondria and elongated peroxisomes** (demonstrated in patient fibroblasts — PMID:26783368).
4. Branch A (peroxisome): fission arrest → **reduced peroxisomal import-competence, accumulation of pre-peroxisomal membrane structures, and altered redox state / intra-peroxisomal pH** → impaired peroxisomal metabolism (demonstrated — PMID:32224193).
5. Branch B (mitochondria): fission arrest → **impaired mitochondrial quality control (mitophagy dysregulation), reduced mitochondrial density and respiratory-chain activity in high-demand tissue, mitochondrial Ca²⁺ overload and oxidative stress** (demonstrated in vivo, PMID:26598616; and in dopaminergic neurons, PMID:35883852).
6. Branches converge → **energetic and oxidative failure of neurons**, particularly in metabolically demanding basal ganglia, subthalamic nucleus, optic and peripheral nerves → **neuronal dysfunction and neurodegeneration** (inferred from imaging + cellular data).
7. Neuronal injury → **clinical phenotype**: developmental delay/regression, acquired microcephaly, spasticity, seizures, optic atrophy, peripheral neuropathy, Leigh-like MRI (demonstrated clinically — PMID:26783368, PMID:32181496).

Notably, because the primary lesion is one of **organelle morphology/dynamics rather than primary OXPHOS enzymology**, skeletal-muscle respiratory-chain activities are typically normal — a diagnostic hallmark.

### Schematic

```
   MFF (biallelic LoF)
        │  no receptor
        ▼
   DRP1/DNM1L not recruited to OMM/peroxisomal membrane
        │
        ▼
   Fission machinery cannot assemble → SCISSION ARREST
        │
        ├──────────────► Peroxisomes: elongated, immature,
        │                 impaired import, altered redox/pH
        │
        └──────────────► Mitochondria: hyper-elongated network,
                          dysregulated mitophagy, Ca²⁺ overload, ROS↑
                                   │
                                   ▼
                 Neuronal energetic/oxidative failure
                 (basal ganglia, subthalamic nucleus, optic/peripheral nerve)
                                   │
                                   ▼
      Leigh-like encephalopathy: delay/regression, microcephaly,
      spasticity, seizures, optic atrophy, peripheral neuropathy
```

### Regulatory context and therapeutic logic

MFF is a physiological **AMPK substrate** (PMID:30948787, PMID:36374514): energy stress activates AMPK, which phosphorylates MFF to drive DRP1 recruitment, fission and mitophagy. EMPF2 removes this node entirely. The single most actionable mechanistic insight is that **shifting the fission/fusion balance back toward fission-competence rescues the phenotype in vivo** — deletion of the fusion gene *Mfn1* completely rescued *Mff*-null mice (PMID:26598616). This nominates pharmacological or genetic **fusion inhibition / fission promotion** as a rational (though still preclinical) therapeutic strategy.

### Ontology annotations

- **Genes/proteins:** *MFF* (HGNC:24858), *DNM1L*/DRP1 (differential), *MFN1* (modifier).
- **GO biological process:** mitochondrial fission (GO:0000266), peroxisome fission (GO:0016559), mitochondrion organization (GO:0007005), mitophagy (GO:0000422), regulation of mitochondrial fission (GO:0090140).
- **GO cellular component:** mitochondrial outer membrane (GO:0005741), peroxisomal membrane (GO:0005778), mitochondrion (GO:0005739), peroxisome (GO:0005777).
- **Cell types (CL):** neuron (CL:0000540), dopaminergic neuron (CL:0000700), cardiac muscle cell (CL:0000746, model), fibroblast (CL:0000057, patient cells).
- **UBERON:** basal ganglia (UBERON:0002420), subthalamic nucleus (UBERON:0001906), cerebellum (UBERON:0002037), optic nerve (UBERON:0000941), peripheral nervous system (UBERON:0000010), brain (UBERON:0000955).
- **CHEBI (relevant chemistry):** calcium(2+) (CHEBI:29108), reactive oxygen species (CHEBI:26523).

---

## Section-by-Section Report

### 1. Disease Information
EMPF2 is an ultra-rare autosomal-recessive mitochondrial/peroxisomal dynamics disorder producing an early-infantile Leigh-like encephalopathy. Identifiers: **MONDO:0014905, OMIM #617086, ORPHA:485421, DOID:0060994, GARD 0017881, MedGen 934693, UMLS C4310726**. There is no dedicated ICD-10 code; it maps to mitochondrial/metabolic encephalopathy categories (e.g., ICD-10 G31.8 / E88.4x class). Synonyms: "EMPF2," "MFF-related encephalopathy," and the ontology synonym "Leigh-like basal ganglia disease–optic atrophy–peripheral neuropathy syndrome." The knowledge base here is derived from **aggregated disease-level resources** (OMIM, Orphanet, HPO, ClinVar) plus a small number of **individual published patient reports** (PMID:26783368, PMID:32181496), not EHR-scale data.

### 2. Etiology
**Causal factor:** purely genetic — biallelic loss-of-function variants in *MFF* (PMID:26783368). **Genetic risk factors:** the causal variants themselves; carrier parents are unaffected. **Modifier genes:** experimentally, *MFN1* (fusion) modifies severity (rescue in mouse — PMID:26598616); DRP1/DNM1L and PEX11 proteins act in the same pathway. **Environmental/lifestyle/infectious factors and protective factors:** none established; consanguinity increases risk of recessive homozygosity. **Gene–environment interactions:** none demonstrated; the AMPK–MFF energy-sensing axis (PMID:30948787) suggests, hypothetically, that metabolic/energy stress could modulate residual pathway output, but this is not clinically shown.

### 3. Phenotypes
See Finding 8 for the full HPO frequency table. Phenotypes are predominantly **neurological signs and physical manifestations** (spasticity, hyperreflexia, microcephaly, ophthalmoplegia, optic atrophy) plus **developmental/behavioral** features (developmental delay/regression, absent speech). Onset is **infantile** (first year of life), severity is **severe**, and course is **progressive with regression**. Quality-of-life impact is profound: affected children have major motor disability (often inability to walk), feeding difficulty (dysphagia requiring support), visual/auditory impairment, and seizures — a globally dependent care status.

### 4. Genetic/Molecular Information
**Causal gene:** *MFF* (2q36.3; NCBI Gene 56947; gene OMIM 614785). **Variant classes:** predominantly nonsense/frameshift/splice-site loss-of-function (e.g., c.433C>T p.Arg145Ter — PMID:32181496; c.159del p.Pro54fs; splice variants c.181+2T>A, c.352-2A>C). **ACMG classification:** null variants are Pathogenic/Likely-pathogenic; missense variants are largely **VUS** (Finding 9). **Allele frequency:** causal alleles are extremely rare/private in gnomAD, consistent with an ultra-rare recessive disease. **Origin:** germline. **Functional consequence:** loss of function / haploinsufficiency requiring biallelic hits. **Epigenetics/chromosomal abnormalities:** none specific to EMPF2; large 2q copy-number gains overlapping *MFF* in ClinVar are incidental and not disease-causing.

### 5. Environmental Information
Not applicable — EMPF2 is a monogenic disorder with **no established environmental, lifestyle, or infectious contributors**. (Note: the environmental-toxin paper PMID:41296099 concerns Drp1/MFF *upregulation* in fluorine/aluminium neurotoxicity, a distinct context, not EMPF2 causation.)

### 6. Mechanism / Pathophysiology
See the ordered causal chain and schematic above. Upstream lesion: MFF loss → failed DRP1 recruitment → fission arrest. Downstream: peroxisome maturation failure (PMID:32224193) and mitochondrial Ca²⁺ overload/oxidative stress/mitophagy dysregulation (PMID:35883852, PMID:26598616), converging on neuronal energetic failure. Key regulatory pathway: **AMPK→MFF→DRP1** (PMID:30948787, PMID:36374514). Cell types: neurons (esp. dopaminergic and basal-ganglia neurons), with cardiomyocyte involvement in the mouse model.

### 7. Anatomical Structures Affected
**Primary organ:** brain — basal ganglia (UBERON:0002420) and subthalamic nucleus (UBERON:0001906), with Leigh-like bilateral (symmetric) involvement; cerebellar atrophy in some. **Secondary/associated:** optic nerve (optic atrophy), peripheral nerves (neuropathy). **Body system:** central and peripheral nervous system. **Subcellular:** mitochondrial outer membrane (GO:0005741) and peroxisomal membrane (GO:0005778). **Lateralization:** bilateral/symmetric CNS lesions. The mouse model additionally shows cardiac involvement (dilated cardiomyopathy), not prominent in human patients.

### 8. Temporal Development
**Onset:** infantile, within the first year of life (HP:0003593), congenital-to-early-infantile. **Pattern:** insidious then progressive with **developmental regression**. **Course:** progressive neurodegeneration; lifelong. **Critical period:** infancy/early childhood is the window of rapid deterioration; no established intervention window given lack of therapy. Death in childhood occurs in a subset (1/4 in the index series).

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (HP:0000007; PMID:26783368, original locus PMID:22499341). **Penetrance:** presumed complete for biallelic LoF. **Expressivity:** variable in severity and survival. **Epidemiology:** ultra-rare — only a handful of published families worldwide; prevalence not formally estimated (well below Orphanet's <1/1,000,000 threshold). **Consanguinity:** relevant (homozygous truncating variants reported in consanguineous/related settings, e.g., PMID:32181496). **Founder effects/carrier frequency:** none established. **Sex ratio:** no sex bias expected (autosomal). No specific ethnic predilection established.

### 10. Diagnostics
**Genetic testing is definitive:** WES/WGS or targeted *MFF* sequencing identifying biallelic LoF variants (PMID:26783368). **Supportive tests:** brain MRI (Leigh-like bilateral basal-ganglia/subthalamic signal); patient-fibroblast microscopy showing elongated mitochondria and peroxisomes; nerve conduction studies (peripheral neuropathy); EEG (hypsarrhythmia/epileptic spasms); ophthalmologic exam (optic atrophy/pallor). **Key negative:** skeletal-muscle respiratory-chain enzyme activities are typically **normal**, distinguishing EMPF2 from classic Leigh syndrome (PMID:26783368). **Differential diagnosis:** EMPF1 (*DNM1L*/DRP1; PMID:33387674), classic mitochondrial Leigh syndrome (with abnormal OXPHOS), peroxisomal biogenesis disorders. Genetic testing distinguishes these. **Screening:** carrier/cascade testing within affected families; prenatal testing when the familial variants are known.

### 11. Outcome / Prognosis
Prognosis is **poor**: severe, progressive neurodevelopmental disability with regression, inability to walk, dysphagia, seizures, and sensory/visual loss; childhood death occurs in a subset. There are no formal survival statistics given rarity. **Prognostic factors** are not formally validated but likely relate to variant severity (complete null vs. hypomorphic) and seizure burden. **Recovery potential** is minimal; care is supportive.

### 12. Treatment
**No disease-specific or curative therapy exists.** Management is **supportive and symptomatic**: anti-seizure medication (including for infantile spasms; NCIT: Anticonvulsant Agent), spasticity management (e.g., baclofen; physical therapy), nutritional/feeding support for dysphagia (gastrostomy where needed), visual and developmental rehabilitation (physical, occupational, speech therapy). **Rational future directions (preclinical only):** fission/fusion rebalancing — the *Mfn1*-deletion rescue in mice (PMID:26598616) suggests fusion inhibition could be therapeutic; antioxidant strategies targeting mitochondrial Ca²⁺/ROS are hypothesis-generating from the dopaminergic-neuron model (PMID:35883852). No approved gene, cell, or RNA therapies. **Pharmacogenomics:** not applicable.

### 13. Prevention
No primary prevention exists for this monogenic disease. **Genetic counseling** is central: recurrence risk is 25% for carrier couples. **Reproductive options:** carrier/cascade screening in affected families, prenatal diagnosis, and preimplantation genetic testing (PGT-M) when the familial *MFF* variants are known. No immunization, behavioral, or public-health interventions apply. Tertiary prevention = optimized supportive care to limit complications (aspiration, seizure-related injury, contractures).

### 14. Other Species / Natural Disease
**Naturally occurring canine disease:** Bullmastiff dogs with a homozygous *MFF* frameshift (p.Glu158Alafs*14) develop a progressive encephalopathy with bilateral symmetric cerebellar-nuclei lesions, explicitly linked to human EMPF2 (PMID:36085405). **Species/orthologs:** *MFF* is conserved; mouse *Mff*, dog *MFF*. **Comparative pathology:** dogs show cerebellar-nuclei predominant lesions; mice (*Mff*-null) die of dilated cardiomyopathy at ~13 weeks (PMID:26598616) — highlighting species-specific tissue vulnerability (cardiac in mouse, CNS in human/dog). **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms
**Mouse:** constitutive and cardiac *Mff* knockouts — robust model of fission failure, fatal dilated cardiomyopathy, reduced respiratory-chain activity, increased mitophagy; the *Mff/Mfn1* double-knockout provides proof-of-concept rescue (PMID:26598616). **Dog:** spontaneous Bullmastiff model (PMID:36085405). **Cellular/in vitro:** patient fibroblasts (elongated organelles — PMID:26783368); iPSC/dental-pulp-derived dopaminergic neurons with MFF knockdown recapitulating neurite/Ca²⁺/ROS defects (PMID:35883852). **Phenotype recapitulation:** cellular and canine models capture the fission defect and CNS phenotype well; the mouse captures the biochemistry and rescue paradigm but emphasizes cardiac (not encephalopathic) lethality — its main limitation for modeling the human neurological disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / Evidence type | Supports |
|---|---|---|---|
| [26783368](https://pubmed.ncbi.nlm.nih.gov/26783368/) | *Disturbed mitochondrial and peroxisomal dynamics due to loss of MFF...* | Human clinical + cell biology (landmark) | F001, F002, F008 — gene discovery, phenotype, HPO source |
| [32181496](https://pubmed.ncbi.nlm.nih.gov/32181496/) | *EMPF2 caused by a novel MFF mutation in a young child* | Human clinical case | F002 — independent patient, variant p.Arg145Ter |
| [32224193](https://pubmed.ncbi.nlm.nih.gov/32224193/) | *MFF is a critical regulator of peroxisome maturation* | In vitro | F003 — peroxisome maturation/redox defect |
| [35883852](https://pubmed.ncbi.nlm.nih.gov/35883852/) | *Mitochondrial Ca²⁺-triggered oxidative stress in DA neurons with MFF insufficiency* | In vitro (iPSC-derived neurons) | F003 — neuronal Ca²⁺/ROS mechanism |
| [26598616](https://pubmed.ncbi.nlm.nih.gov/26598616/) | *Titration of mitochondrial fusion rescues Mff-deficient cardiomyopathy* | Model organism (mouse) | F003, F004 — in vivo mechanism + Mfn1 rescue |
| [36085405](https://pubmed.ncbi.nlm.nih.gov/36085405/) | *MFF frameshift variant in Bullmastiffs...* | Veterinary / comparative | F004 — natural canine model |
| [34347505](https://pubmed.ncbi.nlm.nih.gov/34347505/) | *Mff oligomerization required for Drp1 activation...* | Molecular/biochemical | F001 — MFF as DRP1 receptor |
| [30948787](https://pubmed.ncbi.nlm.nih.gov/30948787/) | *Hierarchical activation of compartmentalized AMPK...* | Molecular | F005 — MFF as AMPK substrate |
| [36374514](https://pubmed.ncbi.nlm.nih.gov/36374514/) | *AMPK/MFF activation: fission and mitophagy...* | In vitro | F005 — AMPK/MFF→DRP1 axis |
| [33387674](https://pubmed.ncbi.nlm.nih.gov/33387674/) | *De novo DNM1L variant...* | Human clinical | F006 — EMPF1 differential |
| [31868880](https://pubmed.ncbi.nlm.nih.gov/31868880/) | *Impaired turnover of hyperfused mitochondria (DRP1 mutation)* | Human clinical / cell biology | F006 — DRP1 fission role |

Supporting/contextual references also reviewed: peroxisome division/pexophagy reviews (PMID:26434997; PMID:22595523) and muscle-BDNF/AMPK–DRP1–MFF signaling (PMID:34689722).

---

## Limitations and Knowledge Gaps

- **Extreme rarity / small n.** The core clinical picture and all HPO frequencies derive from a handful of patients (n=4 index series plus isolated case reports). Frequencies (e.g., "4/4 spasticity") are statistically fragile and may not generalize.
- **No epidemiological estimates.** Prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unquantified.
- **Genotype–phenotype correlation unestablished.** Too few variants to correlate variant type/position with severity or survival.
- **VUS burden.** Most reported missense *MFF* variants are of uncertain significance; functional assays are needed to classify them.
- **Mechanistic inference.** The link from organelle-level defects to specific neuronal death in basal ganglia is inferred from cellular/animal models, not directly demonstrated in patient brain.
- **Model mismatch.** The mouse knockout's lethal phenotype is cardiac, not encephalopathic, limiting its face validity for the human neurological disease.
- **No therapeutic trials.** Fission/fusion rebalancing is proof-of-concept in mice only; no human or even neuronal-model therapeutic data exist.
- **No natural-history study.** Longitudinal course, survival curves, and prognostic biomarkers are undefined.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry / GeneMatcher-driven cohort** to expand n, quantify HPO frequencies robustly, define natural history and survival, and enable genotype–phenotype analysis.
2. **Functional classification of *MFF* VUS** using patient-fibroblast or knockout-cell complementation assays (mitochondrial/peroxisomal morphology, DRP1 recruitment) to reclassify uncertain missense variants per ACMG PS3/BS3.
3. **Test fission/fusion rebalancing in a neuronal model.** Apply *MFN1/2* knockdown or pharmacological fusion modulation to MFF-deficient iPSC-derived neurons (extending PMID:35883852) to determine whether the mouse cardiac rescue (PMID:26598616) translates to neurons.
4. **Antioxidant / mitochondrial-Ca²⁺ modulation** in the dopaminergic-neuron model to test whether buffering Ca²⁺/ROS restores neurite outgrowth — a druggable downstream node.
5. **Characterize the Bullmastiff model** longitudinally (imaging, neuropathology, peroxisomal biochemistry) as a large-animal platform for preclinical therapeutics (PMID:36085405).
6. **Peroxisomal biomarker discovery** (plasma VLCFA, plasmalogens, bile-acid intermediates) to identify a non-genetic diagnostic/monitoring signature reflecting the peroxisome-maturation defect (PMID:32224193).
7. **Brain-tissue / autopsy studies** where available, to confirm the inferred causal chain from elongated organelles to regional neuronal loss.


## Artifacts

- [OpenScientist final report](Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Encephalopathy_Due_To_Defective_Mitochondrial_And_Peroxisomal_Fission_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 29 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014905` (4 mentions) - the report calls it "MONDO"; MONDO calls it **encephalopathy due to defective mitochondrial and peroxisomal fission 2**
- `DOID:0060994` (2 mentions) - the report calls it "DOID"; DOID calls it **encephalopathy due to defective mitochondrial and peroxisomal fission 2**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005484` (1 mention) - the report calls it "Secondary (acquired) microcephaly"; HP calls it **Secondary microcephaly**
- `GO:0000266` (1 mention) - the report calls it "GO biological process:** mitochondrial fission"; GO calls it **mitochondrial fission**
- `GO:0005741` (2 mentions) - the report calls it "GO cellular component:** mitochondrial outer membrane"; GO calls it **mitochondrial outer membrane**
- `UBERON:0002420` (2 mentions) - the report calls it "UBERON:** basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:24858` - called "MFF", "HGNC", "Genes/proteins:** *MFF"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.