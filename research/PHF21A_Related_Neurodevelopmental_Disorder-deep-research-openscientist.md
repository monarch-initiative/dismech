---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T20:37:55.887237'
end_time: '2026-08-28T20:57:20.478036'
duration_seconds: 1164.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PHF21A Related Neurodevelopmental Disorder
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
citation_count: 10
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 28
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 3
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0008872
    reported_labels:
    - Postnatal overgrowth
    ontology_label: Feeding difficulties in infancy
  - term_id: HP:0045025
    reported_labels:
    - sparse eyebrows
    ontology_label: Narrow palpebral fissure
  - term_id: UBERON:0000033
    reported_labels:
    - "Craniofacial skeleton** \u2014 head/face"
    ontology_label: head
  labels_variant: 8
  obsolete_terms:
  - term_id: GO:0034720
    ontology_label: obsolete histone H3-K4 demethylation
  - term_id: GO:0019933
    ontology_label: obsolete cAMP-mediated signaling
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PHF21A_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PHF21A_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PHF21A Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PHF21A Related Neurodevelopmental Disorder** covering all of the
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

# PHF21A-Related Neurodevelopmental Disorder (IDDBCS): A Comprehensive Disease Characterization

## Summary

**PHF21A-related neurodevelopmental disorder** — formally *intellectual developmental disorder with behavioral abnormalities and craniofacial dysmorphism with or without seizures* (**IDDBCS**; OMIM **#618725**; MONDO:**0032883**) — is a rare, autosomal-dominant Mendelian condition caused by heterozygous loss-of-function of the *PHF21A* gene (also known as *BHC80*) at chromosome band **11p11.2**. Nearly all reported cases arise from *de novo* variants, and the underlying molecular mechanism is **haploinsufficiency**: a single functional copy of *PHF21A* is insufficient for normal neurodevelopment. This is strongly supported by population genetics, where *PHF21A* is among the most loss-of-function-intolerant genes in the genome (gnomAD pLI ≈ 1.00, LOEUF ≈ 0.22).

Mechanistically, PHF21A/BHC80 is a **chromatin "reader"** protein whose PHD finger recognizes **unmethylated histone H3 lysine 4 (H3K4me0)** and thereby anchors the **LSD1(KDM1A)/CoREST/HDAC1-2 (BHC/BRAF-HDAC) transcriptional repressor complex** to chromatin. Loss of one PHF21A allele weakens this repressive machinery, leading to **derepression of neuronal target genes** (e.g., the sodium channel gene *SCN3A*), **blunted cAMP/CREB-dependent activity-dependent transcription**, and **dysregulated synaptogenesis**. These molecular defects converge on the developing brain and craniofacial skeleton.

Clinically, IDDBCS produces **near-universal intellectual disability/developmental delay and craniofacial dysmorphism**, with frequent **postnatal overgrowth**, **behavioral abnormalities** (ADHD, autism spectrum disorder), **hypotonia**, and **epilepsy** — the latter often severe, presenting as infantile epileptic spasms syndrome and developmental and epileptic encephalopathy (DEE). Diagnosis relies on exome/genome sequencing, chromosomal microarray, or karyotype (for translocations/deletions). No targeted or curative therapy exists; management is supportive, centered on developmental therapies and antiseizure medication (with vigabatrin effective for spasms). This report synthesizes nine confirmed findings across disease definition, molecular mechanism, phenotype spectrum, variant landscape, model organisms, and clinical management.

---

## 1. Disease Information

**Overview.** PHF21A-related neurodevelopmental disorder is a rare monogenic neurodevelopmental syndrome characterized by the triad of intellectual disability/developmental delay, craniofacial dysmorphism, and behavioral abnormalities, with or without seizures. It belongs to the family of chromatin-remodeling ("chromatinopathy") disorders and, because of frequent postnatal overgrowth, overlaps clinically with the overgrowth–intellectual disability (OGID) syndromes (e.g., Sotos, Weaver).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Disease name | Intellectual developmental disorder with behavioral abnormalities and craniofacial dysmorphism with or without seizures (**IDDBCS**) |
| OMIM (disease) | **#618725** |
| MONDO | **MONDO:0032883** (verified via EBI OLS4) |
| Gene | *PHF21A* (PHD finger protein 21A) |
| Gene aliases | *BHC80*, *BM-006* |
| HGNC | HGNC:24156 |
| NCBI Gene | 51317 |
| Ensembl | ENSG00000135365 |
| UniProt | Q96BD5 (680 aa) |
| Gene OMIM | 608325 |
| Cytogenetic locus | 11p11.2 |

**Synonyms / alternative names.** "PHF21A-related neurodevelopmental disorder(s)"; "IDDBCS"; historically indexed as **NEDMS**; *BHC80*-related disorder. Older literature also describes overlap with **Potocki–Shaffer syndrome** (the 11p11.2 contiguous gene deletion), from which PHF21A was dissected out as the gene responsible for the intellectual disability and craniofacial anomaly components.

**Source of information.** The knowledge base is derived from **aggregated disease-level resources** (OMIM, MONDO, ClinVar, gnomAD) and **individual patient case series/reports** in the primary literature (cohorts of 12–15 patients), rather than from population EHR data. The disorder is ultra-rare, so all epidemiologic inference comes from case aggregation.

The modern clinical entity is defined by Gavilán/Iwase (2025) [PMID: 40622422](https://pubmed.ncbi.nlm.nih.gov/40622422/): *"PHF21A heterozygosity is associated with intellectual disability, behavioral issues, and craniofacial dysmorphism, with or without seizures (IDDBCS), also known as PHF21A-related neurodevelopmental disorders."*

---

## 2. Etiology

**Primary cause — genetic.** IDDBCS is a monogenic disorder caused by heterozygous loss-of-function of *PHF21A*. Kim et al. (2012) mapped the intellectual disability (ID) and craniofacial anomaly (CFA) phenotypes to single-gene haploinsufficiency of *PHF21A* using balanced translocation breakpoints and deletion mapping at 11p11.2 ([PMID: 22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/)): *"the ID and CFA phenotypes are both caused by haploinsufficiency of a single gene, PHF21A, at 11p11.2."*

**Genetic risk factors.** The causal genetic events are:
- *De novo* truncating variants (frameshift, nonsense) — the dominant class.
- *De novo* missense variants (rare, e.g., a splice-affecting AT-hook variant).
- Balanced translocations disrupting *PHF21A*.
- Intragenic deletions and larger 11p11.2 contiguous-gene deletions encompassing *PHF21A*.

There are **no known common susceptibility loci or modifier genes** established for this ultra-rare Mendelian disorder; all pathogenic alleles are private/de novo.

**Environmental risk factors.** None established. As a *de novo* dominant Mendelian disorder, there are no recognized environmental, occupational, lifestyle, or infectious contributors. Advanced parental age is a plausible but unquantified contributor to *de novo* mutation rate (general principle, not specifically demonstrated for *PHF21A*).

**Protective factors.** None established (genetic or environmental).

**Gene–environment interactions.** None established.

---

## 3. Phenotypes

The phenotype spectrum has been characterized in three overlapping case series. Core features (ID/DD and craniofacial dysmorphism) are essentially universal; associated features vary in frequency.

### Phenotype frequency table (pooled from primary cohorts)

| Phenotype | HPO suggestion | Frequency | Source |
|---|---|---|---|
| Intellectual disability / developmental delay | HP:0001249 / HP:0001263 | 100% (12/12; 15/15) | Chen 2023; Wu 2023 |
| Craniofacial dysmorphism | HP:0001999 | 100% (15/15) | Wu 2023 |
| Postnatal overgrowth | HP:0008872 | 100% (Chen); 83% (5/6 Poole); 8/15 (Wu) | Chen 2023; Poole 2023; Wu 2023 |
| Behavioral abnormalities | HP:0000708 | 12/15 (80%) | Wu 2023 |
| ADHD | HP:0007018 | ~78% (Chen) | Chen 2023 |
| Hypotonia | HP:0001252 | 70% (Chen); 64% (7/11 Poole) | Chen 2023; Poole 2023 |
| Epilepsy / seizures | HP:0001250 | 58% (7/12 Chen); 9/15 Wu; 50% (6/12 Poole) | Chen 2023; Wu 2023; Poole 2023 |
| Developmental & epileptic encephalopathy (DEE) | HP:0200134 | 71% of those with epilepsy (5/7) | Chen 2023 |
| Autism spectrum disorder | HP:0000729 | ~50% | Chen 2023 |
| Sleep disorder | HP:0002360 | ~33% | Chen 2023 |

**Epilepsy characteristics.** Chen et al. (2023) reported ([PMID: 37633153](https://pubmed.ncbi.nlm.nih.gov/37633153/)): *"Seven of the 12 patients (58.33%) had an epileptic phenotype, and the majority (5/7, 71.42%) of affected individuals developed developmental and epileptic encephalopathy (DEE),"* often manifesting as **infantile epileptic spasms syndrome**. The associated features were quantified as: *"Overgrowth, ADHD, hypotonia, ASD, and sleep disorders were observed in 100%, 77.78%, 70%, 50%, and 33.33% of patients, respectively."*

Wu et al. (2023) independently corroborated core frequencies ([PMID: 37528014](https://pubmed.ncbi.nlm.nih.gov/37528014/)): *"intellectual disability or developmental delay (15 patients), craniofacial anomalies (15 patients), behavioral abnormalities (12 patients), seizures (9 patients), and overgrowth (8 patients)."* Poole et al. (2023) placed PHF21A firmly among overgrowth syndromes ([PMID: 36876344](https://pubmed.ncbi.nlm.nih.gov/36876344/)): *"postnatal overgrowth was reported in 5/6 (83%)."*

**Craniofacial gestalt.** Recurrent facial features include a **tall, broad/prominent forehead** (HP:0000337), **sparse eyebrows** (HP:0045025), **broad nasal bridge/tip** (HP:0000431/HP:0000455), **anteverted nares** (HP:0000463), **full cheeks**, and a **downturned mouth with a tent-shaped upper lip**.

**Phenotype characteristics.**
- **Age of onset:** Congenital/neonatal to early childhood; developmental delay and hypotonia often evident in infancy; overgrowth is postnatal; epileptic spasms typically infantile.
- **Severity:** Variable; ID ranges mild to severe; epilepsy skews toward severe (DEE).
- **Progression:** Largely stable/non-degenerative developmental disability; epilepsy course varies.
- **Expressivity:** Variable, even for identical variants (see recurrent p.Arg580*).

**Quality of life impact.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder. Impact is inferred from the phenotype: intellectual disability, behavioral comorbidities (ADHD/ASD), and epilepsy (particularly DEE) impose substantial lifelong functional and caregiving burden.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PHF21A* (PHD finger protein 21A; alias *BHC80*), gene OMIM 608325, HGNC:24156, NCBI Gene 51317, Ensembl ENSG00000135365, UniProt Q96BD5 (680 aa), at 11p11.2.

**Pathogenic variant landscape.** The variant spectrum is dominated by *de novo* loss-of-function alleles. Chen et al. (2023) pooled 12 patients ([PMID: 37633153](https://pubmed.ncbi.nlm.nih.gov/37633153/)): all variants were *de novo* heterozygous; *"The most common types of variants were frameshift variants (7/12, 58.33%), followed by nonsense variants (4/12, 33.33%) and missense variants (1/12, 8.33%)."*

| Variant class | Frequency (Chen 2023, n=12) | Consequence |
|---|---|---|
| Frameshift | 58% (7/12) | Loss of function / haploinsufficiency |
| Nonsense | 33% (4/12) | Loss of function / haploinsufficiency |
| Missense | 8% (1/12) | Reduced dosage (splicing) |
| Structural (translocation/deletion) | Additional cases | Gene disruption / haploinsufficiency |

**Recurrent hotspot.** The nonsense variant **p.Arg580\*** recurs and shows variable expressivity: *"Three of the 12 patients (25%) had the same variant (p.Arg580\*)."*

**Functional consequence — haploinsufficiency (loss of function).** Hamanaka et al. (2019) reported *de novo* truncating variants and concluded ([PMID: 31649809](https://pubmed.ncbi.nlm.nih.gov/31649809/)): *"haploinsufficiency is the likely underlying mechanism in the phenotype."* Notably, even the only recurrent **missense** variant (c.1285G>A, at the last nucleotide of exon 13 in the AT-hook motif) acts by **reducing splicing efficiency/dosage** while preserving DNA binding — Gavilán/Iwase (2025) concluded ([PMID: 40622422](https://pubmed.ncbi.nlm.nih.gov/40622422/)): *"reduced dosage rather than impaired DNA binding likely contributes to the cognitive impairments."* This argues against dominant-negative or gain-of-function mechanisms; **reduced gene dosage is the unifying pathomechanism**. Truncations tend to converge on the **AT-hook domain** and a C-terminal intrinsically disordered region.

**Population constraint (supports haploinsufficiency).** gnomAD constraint metrics for *PHF21A* place it among the most LoF-intolerant genes:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.00 | Extreme LoF intolerance |
| oe_lof (observed/expected) | 0.133 (11 obs vs 82.5 exp) | Strong depletion of LoF |
| LOEUF | 0.221 | Highly constrained |
| LoF Z | 6.68 | Strong LoF constraint |
| Missense Z | 3.81 | Missense-constrained |
| Synonymous Z | 0.20 | Neutral (as expected) |

No common LoF alleles exist in the general population; disease-causing variants are private/de novo.

**ClinVar summary.** ClinVar contains ~427 *PHF21A* variant records: the large majority (~370) are **variants of uncertain significance (VUS)**, ~21 likely pathogenic, and dozens pathogenic (the pathogenic set includes large 11p11.2 contiguous deletions encompassing *PHF21A*). The VUS-heavy landscape reflects both the gene's constraint and limited functional annotation.

**Allele frequency.** Pathogenic alleles are absent/singleton in gnomAD (private, *de novo*); no recurrent population allele.

**Somatic vs germline.** Germline (constitutional), typically *de novo*.

**Modifier genes.** None established.

**Epigenetic information.** As a chromatin-reader deficiency, the disorder alters the epigenomic repression state at target loci (loss of LSD1/CoREST/HDAC recruitment reduces H3K4 demethylation and histone deacetylation at target promoters), but a defined patient DNA-methylation "episignature" has not been confirmed here.

**Chromosomal abnormalities.** Balanced translocations disrupting *PHF21A*; intragenic deletions; and larger 11p11.2 contiguous-gene deletions (overlapping the Potocki–Shaffer region).

---

## 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents are implicated in this *de novo* Mendelian chromatinopathy. Disease is fully explained by the germline genetic lesion.

---

## 6. Mechanism / Pathophysiology

### Molecular reader function

PHF21A/BHC80 is a **histone reader**. Lan et al. (2007) showed ([PMID: 17687328](https://pubmed.ncbi.nlm.nih.gov/17687328/)): *"the PHD finger of BHC80 binds unmethylated H3K4 (H3K4me0), and this interaction is specifically abrogated by methylation of H3K4."* PHF21A also binds DNA via an **AT-hook motif**. By reading the "unmodified/repressive" H3K4me0 mark, PHF21A anchors a repressor complex to chromatin.

### The LSD1/CoREST/HDAC (BHC) complex

PHF21A is a core subunit of the LSD1(KDM1A)/CoREST/HDAC1-2 complex. Shi et al. (2005) established ([PMID: 16140033](https://pubmed.ncbi.nlm.nih.gov/16140033/)): *"LSD1 is associated with HDAC1/2; CoREST, a SANT domain-containing corepressor; and BHC80, a PHD domain-containing protein."* Within this complex there is **reciprocal dependence**: BHC80 (PHF21A) and LSD1 depend on each other for stable chromatin association. Critically, PHF21A is required for repression — Lan et al. showed ([PMID: 17687328](https://pubmed.ncbi.nlm.nih.gov/17687328/)): *"Knockdown of BHC80 by RNA inhibition results in the de-repression of LSD1 target genes."*

### REST/NRSF neuronal gene silencing

The BHC complex silences **neuron-specific genes** through the **RE1/neural restrictive silencer (NRS) element** — the **REST/NRSF pathway**. Kim et al. (2012) confirmed ([PMID: 22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/)): *"PHF21A, also known as BHC80, is a component of the BRAF-histone deacetylase complex that represses target-gene transcription."*

### Downstream consequences of haploinsufficiency

1. **Target-gene derepression.** In translocation-patient lymphoblasts, PHF21A disruption derepressed the neuronal gene *SCN3A* with reduced LSD1 occupancy — Kim et al. ([PMID: 22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/)): *"we observed derepression of the neuronal gene SCN3A and reduced LSD1 occupancy at the SCN3A promoter."*

2. **Broad transcriptional dysregulation & impaired cAMP/CREB signaling.** RNA-seq of two PHF21A-haploinsufficient patient cell lines identified 1,885 commonly misregulated genes. Porter/Iwase (2018) reported ([PMID: 28571721](https://pubmed.ncbi.nlm.nih.gov/28571721/)): *"The patient cells displayed down-regulation of key pathways relevant to learning and memory, including Cyclic Adenosine Monophosphate (cAMP)-signaling pathway genes,"* and functionally *"PHF21A-deficient patient-derived cells exhibited a delayed induction of immediate early genes following forskolin stimulation"* — i.e., impaired activity-dependent (CREB-driven) transcription.

3. **Dysregulated synaptogenesis via neuronal microexon splicing.** PHF21A and LSD1 both undergo neuron-specific microexon splicing. Nagai/Iwase (2024) showed the PHF21A neuronal microexon (exon 14) interferes with nucleosome binding, producing stepwise deactivation of the LSD1–PHF21A complex during neuronal maturation. Forcing the canonical (non-neuronal) PHF21A isoform in neurons causes excess synapses — [PMID: 39395799](https://pubmed.ncbi.nlm.nih.gov/39395799/): *"Phf21a neuronal splicing prevents excess synapse formation that otherwise would occur when canonical PHF21A is expressed in neurons."*

### Causal chain (upstream → downstream)

```
Heterozygous PHF21A LoF (de novo)          [UPSTREAM]
        │  (haploinsufficiency; ~50% protein dose)
        ▼
Weakened H3K4me0 reading / reduced LSD1-CoREST-HDAC
chromatin anchoring at RE1/NRS neuronal loci
        │
        ▼
Derepression of neuronal target genes (e.g., SCN3A)
+ impaired cAMP/CREB activity-dependent transcription
+ dysregulated synaptogenesis (microexon isoform balance)
        │
        ▼
Aberrant neuronal differentiation, synapse number,
and network excitability; craniofacial developmental defects
        │
        ▼
Intellectual disability, behavioral abnormalities,       [DOWNSTREAM]
craniofacial dysmorphism, overgrowth, epilepsy (DEE)
```

**Cell types & processes.** Neurons (CL:0000540) and neural progenitors; craniofacial/neural crest derivatives. GO biological processes: negative regulation of transcription (GO:0000122), histone H3-K4 demethylation (GO:0034720), chromatin organization (GO:0006325), regulation of synapse assembly (GO:0051963), learning or memory (GO:0007611), cAMP-mediated signaling (GO:0019933). GO cellular components: nucleus (GO:0005634), chromatin (GO:0000785), CoREST/LSD1/HDAC complex.

**Protein dysfunction.** Loss of function via truncation/dosage reduction; the enzymatically inactive neuronal complex interacts with neuron-specific partners including **MYT1-family transcription factors** and **VIRMA**.

**Metabolic / immune / tissue-damage mechanisms.** No primary metabolic, immune, or tissue-necrosis mechanism; this is a developmental transcriptional-regulatory disorder.

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Primary:** Central nervous system — brain (UBERON:0000955); nervous system (UBERON:0001016).
- **Craniofacial skeleton** — head/face (UBERON:0000033), reflecting neural crest/craniofacial developmental involvement.
- **Body systems:** Nervous system (cognition, seizures, behavior); musculoskeletal/growth axis (postnatal overgrowth, hypotonia).

**Tissue and cell level.** Nervous tissue; neurons (CL:0000540) and neural progenitor cells (CL:0011020); neural-crest-derived craniofacial mesenchyme.

**Subcellular level.** Nucleus (GO:0005634) and chromatin (GO:0000785) — PHF21A is a nuclear chromatin-associated protein.

**Localization / lateralization.** Craniofacial features are bilateral/symmetric; brain involvement is diffuse rather than focal.

---

## 8. Temporal Development

**Onset.** Congenital to infantile. Hypotonia and developmental delay are often apparent in infancy; craniofacial features are present from birth/early childhood; postnatal overgrowth emerges after birth; epileptic spasms are typically infantile in onset.

**Progression.** The intellectual disability is a **stable, non-degenerative** developmental disability rather than a progressive neurodegeneration. Epilepsy course is variable; a substantial subset evolves into **developmental and epileptic encephalopathy (DEE)** with attendant developmental impact.

**Disease duration.** Chronic, lifelong.

**Critical periods.** Neurodevelopmental windows (fetal/infantile neuronal differentiation and synaptogenesis) are the mechanistically relevant vulnerable periods, given PHF21A's role in the LSD1-complex "handoff" during neuronal maturation. Early seizure control (infancy) is the primary time-sensitive intervention opportunity.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare; precise prevalence/incidence are not established. Fewer than ~40 patients are described in aggregate cohorts (12, 15, and 13 patients in the three main series). No population registry estimates exist.

**Inheritance pattern.** **Autosomal dominant**, almost always **de novo**. Because PHF21A is on 11p (autosome), inheritance is not sex-linked.

**Penetrance.** Effectively complete for the neurodevelopmental phenotype in reported *de novo* cases; **expressivity is variable** even for the identical recurrent p.Arg580\* variant (present in 3/12 patients with differing severity).

**Genetic anticipation.** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism / founder effects / consanguinity.** Not established as relevant; disease is *de novo* dominant, so consanguinity is not a driver and there are no founder alleles. Recurrence risk for parents of an affected *de novo* proband is low but non-zero owing to the theoretical possibility of parental gonadal mosaicism.

**Carrier frequency.** Not applicable (dominant, *de novo*; gnomAD shows no common LoF carriers).

**Population demographics.** No ethnic or geographic predilection reported; no established sex ratio skew. Age distribution reflects a pediatric-onset lifelong condition.

---

## 10. Diagnostics

**Genetic testing is the diagnostic cornerstone.**

| Modality | Utility for IDDBCS |
|---|---|
| Whole-exome sequencing (WES) | High — detects *de novo* SNV/indel (frameshift, nonsense, missense); trio testing establishes *de novo* status |
| Whole-genome sequencing (WGS) | High — additionally resolves structural variants/translocation breakpoints |
| Chromosomal microarray (CMA) | Detects intragenic and 11p11.2 contiguous-gene deletions |
| Karyotype / FISH | Detects balanced translocations disrupting *PHF21A* (as in original mapping) |
| Multigene NDD/epilepsy/overgrowth panels | *PHF21A* is included on many ID/DD, epilepsy, and overgrowth panels |
| Single-gene testing | Confirmatory when a specific variant is suspected |

**Clinical evaluation.** Developmental/cognitive assessment; EEG and MRI for seizures; growth monitoring (overgrowth); behavioral/psychiatric evaluation (ADHD/ASD, sleep). No specific biochemical biomarker, imaging signature, or laboratory abnormality is diagnostic; there is no metabolic marker.

**Diagnostic criteria.** No formal consensus criteria; diagnosis is molecular (pathogenic/likely pathogenic *PHF21A* variant) in a patient with a compatible phenotype (ID/DD, craniofacial dysmorphism ± behavioral abnormalities ± seizures ± overgrowth).

**Differential diagnosis.** Other **overgrowth–intellectual disability (OGID) syndromes** (Sotos/*NSD1*, Weaver/*EZH2*, Tatton-Brown–Rahman/*DNMT3A*, Malan/*NFIX*), other **chromatinopathies**, and **Potocki–Shaffer syndrome** (larger 11p11.2 deletion). Molecular testing distinguishes them.

**Screening.** No newborn or population carrier screening (disorder is *de novo*, ultra-rare). Cascade testing of parents is chiefly to establish *de novo* status and recurrence risk.

---

## 11. Outcome / Prognosis

**Survival / mortality.** No specific life-expectancy or mortality data are established. The disorder is not intrinsically lethal; prognosis is dominated by neurodevelopmental disability and seizure burden rather than early mortality. Severe DEE carries the usual associated risks of refractory infantile epilepsy.

**Morbidity / function.** Lifelong intellectual disability and behavioral comorbidities produce substantial functional impairment and dependency. Hypotonia affects early motor development.

**Disease course.** Non-progressive developmental disability with chronic, lifelong needs; epilepsy (when present) is a major determinant of outcome, and DEE portends worse cognitive trajectory.

**Prognostic factors.** Presence and severity of epilepsy (particularly DEE/infantile spasms) is the key prognostic modifier; degree of ID is variable. No molecular prognostic biomarker beyond variant presence is established (variable expressivity limits genotype–phenotype prediction).

---

## 12. Treatment

**No targeted or disease-modifying therapy exists.** Management is **supportive and symptom-directed**.

| Domain | Intervention | NCIT-style term |
|---|---|---|
| Seizures | Antiseizure medications; **vigabatrin** effective for infantile spasms | Anticonvulsant Agent |
| Developmental | Early intervention; physical, occupational, and speech therapy | Rehabilitation Therapy |
| Behavioral | ADHD/ASD management (behavioral therapy ± stimulants/other agents) | Behavioral Therapy |
| Sleep | Sleep hygiene / targeted management | Supportive Care |
| Growth/feeding | Monitoring of overgrowth; nutritional support | Supportive Care |

**Pharmacotherapy.** Antiseizure medication is the principal pharmacologic intervention; vigabatrin is highlighted for infantile epileptic spasms syndrome. ADHD and ASD are treated per standard symptomatic approaches.

**Advanced therapeutics.** No approved gene therapy, cell therapy, RNA-based therapy, or targeted small molecule. Given the **dosage-reduction** mechanism, dosage-restorative strategies (e.g., approaches that raise residual PHF21A expression) are conceptually attractive but experimental. No pharmacogenomic guidance is established.

**Experimental treatments / clinical trials.** None identified specific to IDDBCS.

**Treatment strategy.** Multidisciplinary care (neurology, developmental pediatrics, genetics, therapy services); early aggressive seizure control; individualized developmental and behavioral supports.

---

## 13. Prevention

**Primary prevention.** Not applicable — *de novo* dominant Mendelian disorder cannot be prevented by risk-factor modification, immunization, or public-health measures.

**Secondary prevention / early detection.** Early molecular diagnosis (trio exome/genome) enables prompt developmental intervention and early, targeted seizure management (vigabatrin for spasms), which is the most impactful available "preventive" action for downstream disability.

**Genetic counseling.** Central to family management: for a *de novo* proband, recurrence risk for future siblings is low but non-zero (parental gonadal mosaicism). Affected individuals who reproduce would have 50% transmission risk (autosomal dominant). Prenatal/preimplantation testing is possible once a familial variant is known.

**Screening.** No population or newborn screening.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.**
- **Mouse:** *Phf21a* (NCBI Gene 192285; Ensembl ENSMUSG00000058318), *Mus musculus* (NCBI Taxon 10090).
- **Zebrafish:** *phf21a* ortholog, *Danio rerio* (NCBI Taxon 7955).

**Naturally occurring disease.** No naturally occurring companion-animal or wildlife disease attributable to *PHF21A* is documented (no OMIA entry identified here). Relevance is confined to engineered/experimental models.

**Comparative biology / evolutionary conservation.** The LSD1/CoREST/PHF21A repressor module and the neuron-specific microexon-splicing program are conserved across vertebrates, underpinning the utility of mouse and zebrafish models for studying the disorder's mechanism.

**Transmission / zoonotic potential.** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

| Model | System | Key finding | Source |
|---|---|---|---|
| **Zebrafish** *phf21a* morphant | Vertebrate, morpholino knockdown | Craniofacial abnormalities + neuronal apoptosis | Kim 2012 ([PMID: 22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/)) |
| **Mouse** *Phf21a* mutant models (two) | Mammalian genetic | Forcing canonical (non-neuronal) PHF21A in neurons causes excess synapse formation; neuronal splicing restrains synaptogenesis | Nagai/Iwase 2024 ([PMID: 39395799](https://pubmed.ncbi.nlm.nih.gov/39395799/)) |
| **Human patient-derived cells** (lymphoblasts, cell lines) | In vitro | SCN3A derepression, reduced LSD1 occupancy; 1,885 misregulated genes; impaired cAMP/CREB IEG induction | Kim 2012; Porter/Iwase 2018 ([PMID: 28571721](https://pubmed.ncbi.nlm.nih.gov/28571721/)) |

**Phenotype recapitulation.** The zebrafish morphant recapitulates the **craniofacial** dimension and demonstrates **neuronal apoptosis** — Kim et al. ([PMID: 22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/)): *"suppression of the latter led to both craniofacial abnormalities and neuronal apoptosis."* Mouse models illuminate the **synaptogenesis-control** mechanism via neuronal microexon splicing.

**Limitations.** Morpholino knockdown has known off-target/transient caveats; mouse "forced-isoform" experiments model a mechanistic axis rather than the exact human haploinsufficient genotype; cognitive/behavioral recapitulation of human ID is inherently limited. **Resources:** MGI (mouse), ZFIN (zebrafish).

---

## Mechanistic Model / Interpretation

The disorder is best understood as a **chromatin-reader haploinsufficiency**. A single functional *PHF21A* allele cannot fully staff the LSD1/CoREST/HDAC repressor complex at neuronal RE1/NRS loci. The resulting partial loss of repression **derepresses neuronal genes prematurely/inappropriately** (SCN3A being a validated example) and **weakens activity-dependent cAMP/CREB transcriptional responses**, while the finely tuned **neuronal microexon-splicing "handoff"** that normally throttles synapse formation is perturbed. Because PHF21A is required at a developmental inflection point — the transition of the LSD1 complex from a proliferative/progenitor configuration to a neuronal one — the phenotype manifests as a fixed developmental disorder (ID, dysmorphism, overgrowth) with a superimposed excitability phenotype (epilepsy/DEE).

The convergence of three independent lines of evidence — (1) gnomAD extreme LoF-intolerance (pLI = 1.0, LOEUF = 0.22), (2) uniformly *de novo* truncating variants, and (3) the missense-splice variant that reduces dosage without impairing DNA binding — makes **haploinsufficiency** the unambiguous mechanism, effectively excluding dominant-negative and gain-of-function models.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [22770980](https://pubmed.ncbi.nlm.nih.gov/22770980/) (Kim 2012) | Maps ID+CFA to *PHF21A* haploinsufficiency at 11p11.2; SCN3A derepression; zebrafish craniofacial defects & neuronal apoptosis | Human genetics + zebrafish + in vitro |
| [17687328](https://pubmed.ncbi.nlm.nih.gov/17687328/) (Lan 2007) | PHF21A/BHC80 PHD finger reads H3K4me0; knockdown derepresses LSD1 targets | In vitro/molecular |
| [16140033](https://pubmed.ncbi.nlm.nih.gov/16140033/) (Shi 2005) | Defines BHC80/PHF21A as subunit of LSD1/CoREST/HDAC complex | In vitro/molecular |
| [37633153](https://pubmed.ncbi.nlm.nih.gov/37633153/) (Chen 2023) | 12-patient cohort: phenotype frequencies, variant classes, p.Arg580\* hotspot | Human clinical |
| [37528014](https://pubmed.ncbi.nlm.nih.gov/37528014/) (Wu 2023) | 15-patient review corroborating core/associated phenotypes | Human clinical |
| [36876344](https://pubmed.ncbi.nlm.nih.gov/36876344/) (Poole 2023) | 13-patient series; overgrowth 83%, hypotonia, seizures | Human clinical |
| [31649809](https://pubmed.ncbi.nlm.nih.gov/31649809/) (Hamanaka 2019) | *De novo* truncating variants; states haploinsufficiency mechanism | Human genetics |
| [28571721](https://pubmed.ncbi.nlm.nih.gov/28571721/) (Porter/Iwase 2018) | Patient-cell RNA-seq; impaired cAMP/CREB IEG induction | In vitro |
| [39395799](https://pubmed.ncbi.nlm.nih.gov/39395799/) (Nagai/Iwase 2024) | Neuronal microexon splicing restrains synaptogenesis (mouse) | Model organism |
| [40622422](https://pubmed.ncbi.nlm.nih.gov/40622422/) (Gavilán/Iwase 2025) | Defines IDDBCS entity; recurrent missense acts by dosage reduction | Human genetics + in vitro |

---

## Limitations and Knowledge Gaps

- **Small cohorts.** All clinical data derive from case series totaling ~40 patients; frequency estimates have wide uncertainty and possible ascertainment bias toward severe phenotypes.
- **No epidemiologic estimates.** Prevalence/incidence, mortality, and life expectancy are unquantified.
- **VUS-dominated ClinVar.** ~370/427 variants are VUS; functional annotation is limited, complicating classification of new variants.
- **No episignature confirmed.** A patient DNA-methylation signature (useful for diagnostics) has not been validated here.
- **No QoL instruments** applied specifically to IDDBCS.
- **Genotype–phenotype prediction is weak** given variable expressivity (identical p.Arg580\* with divergent severity).
- **No approved targeted therapy** and no clinical trials identified.
- **Citation verification.** Quotes are drawn from provided abstract snippets; they should be re-verified against source abstracts before formal publication.

---

## Proposed Follow-up Experiments / Actions

1. **Reclassify ClinVar VUS** via a high-throughput functional assay (e.g., saturation genome editing or splicing/reporter assays) leveraging the established dosage-reduction mechanism, to convert VUS to actionable calls.
2. **Define a blood DNA-methylation episignature** across a patient cohort to enable a cheap, robust clinical diagnostic and VUS-arbitration tool (mirroring successful approaches for other chromatinopathies).
3. **Natural-history / registry study** to establish prevalence, developmental trajectories, seizure outcomes (including DEE risk factors), and QoL using standardized instruments (Vineland, PROMIS).
4. **iPSC-derived neuron / organoid modeling** of patient variants to map the transcriptional derepression program and test whether pharmacologic modulation (e.g., HDAC/LSD1-axis or cAMP/CREB enhancers) rescues activity-dependent transcription.
5. **Dosage-restoration proof-of-concept** (e.g., ASO- or CRISPRa-mediated upregulation of the residual allele) in mouse/zebrafish, since haploinsufficiency is a favorable target for gene-dosage therapies.
6. **Seizure-management evidence synthesis** — formally evaluate vigabatrin and other agents for PHF21A-related infantile spasms to build a genotype-informed treatment guideline.

---

## Consensus Answer

PHF21A-related neurodevelopmental disorder (IDDBCS; OMIM #618725; MONDO:0032883) is a rare autosomal-dominant, almost always *de novo* Mendelian condition caused by heterozygous loss-of-function (haploinsufficiency) of *PHF21A/BHC80* at 11p11.2. PHF21A is a chromatin reader of unmethylated H3K4 that anchors the LSD1/CoREST/HDAC repressor complex, so its loss derepresses neuronal target genes (e.g., *SCN3A*), blunts cAMP/CREB-dependent transcription, and dysregulates synaptogenesis — producing near-universal intellectual disability/developmental delay and craniofacial dysmorphism with frequent postnatal overgrowth, behavioral problems (ADHD/ASD), hypotonia, and epilepsy (often infantile spasms/DEE). Diagnosis is by exome/genome sequencing or CMA/karyotype, and management is supportive (developmental therapies and antiseizure medication, with vigabatrin effective for spasms), as no targeted or curative therapy exists.


## Artifacts

- [OpenScientist final report](PHF21A_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PHF21A_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008872` (1 mention) - the report calls it "Postnatal overgrowth"; HP calls it **Feeding difficulties in infancy**
- `HP:0045025` (1 mention) - the report calls it "sparse eyebrows"; HP calls it **Narrow palpebral fissure**
- `UBERON:0000033` (1 mention) - the report calls it "Craniofacial skeleton** — head/face"; UBERON calls it **head**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0034720` (obsolete histone H3-K4 demethylation) (1 mention)
- `GO:0019933` (obsolete cAMP-mediated signaling) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001999` (1 mention) - the report calls it "Craniofacial dysmorphism"; HP calls it **Abnormal facial shape**, and lists "Facial dysmorphism" among its other names
- `HP:0000708` (1 mention) - the report calls it "Behavioral abnormalities"; HP calls it **Atypical behavior**, and lists "Behavioral abnormality" among its other names
- `HP:0001250` (1 mention) - the report calls it "Epilepsy / seizures"; HP calls it **Seizure**, and lists "Epileptic seizure" among its other names
- `HP:0200134` (1 mention) - the report calls it "Developmental & epileptic encephalopathy (DEE)"; HP calls it **Epileptic encephalopathy**
- `HP:0000729` (1 mention) - the report calls it "Autism spectrum disorder"; HP calls it **Autistic behavior**, and lists "Autism spectrum disorder" among its other names
- `HP:0002360` (1 mention) - the report calls it "Sleep disorder"; HP calls it **Sleep disturbance**
- `HP:0000337` (1 mention) - the report calls it "tall, broad/prominent forehead"; HP calls it **Broad forehead**
- `UBERON:0000955` (1 mention) - the report calls it "Primary:** Central nervous system — brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names