---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T06:06:56.574402'
end_time: '2026-08-30T06:54:40.576573'
duration_seconds: 2864.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metaphyseal Chondrodysplasia, Jansen Type
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
citation_count: 31
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 30
  quotes_valid: 30
  relevance_assessed: 32
  on_topic: 19
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 13
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0007050
    reported_labels:
    - cell cycle arrest
    ontology_label: GO_0007050
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0007050
    ontology_label: GO_0007050
    replaced_by: GO:0051726
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Metaphyseal_Chondrodysplasia_Jansen_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Metaphyseal_Chondrodysplasia_Jansen_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metaphyseal Chondrodysplasia, Jansen Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Metaphyseal Chondrodysplasia, Jansen Type** covering all of the
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

# Metaphyseal Chondrodysplasia, Jansen Type (JMC): Comprehensive Disease Characterization

*A mechanistic and clinical knowledge-base report. Evidence sources: human clinical, mouse model, in vitro, and computational/structural. Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT) are provided where applicable.*

---

## Summary

**Metaphyseal Chondrodysplasia, Jansen type (JMC; OMIM #156400)** is an ultra-rare autosomal dominant skeletal dysplasia caused by **heterozygous gain-of-function (activating) missense mutations in *PTH1R*** (the parathyroid hormone / PTH-related peptide type 1 receptor; HGNC:*PTH1R*, gene OMIM *168468, UniProt Q03431). Five recurrent mutations at three residues are established causes — **H223R (by far the most common), T410P, T410R, I458R, and I458K** — each of which renders the receptor **constitutively active in a ligand-independent manner**, producing basal Gsα–cAMP signaling in the absence of hormone. This single molecular lesion explains the entire disease: it simultaneously delays growth-plate chondrocyte hypertrophy (yielding metaphyseal widening, bowed limbs, and severe short stature) and drives **PTH-independent hypercalcemia** — a biochemical signature nearly unique among skeletal dysplasias and central to diagnosis.

The pathophysiology is now well understood as the mirror image of loss-of-function *PTH1R* disease. Constitutively active PTH1R inhibits cellular **salt-inducible kinases (SIK2/SIK3)**, de-repressing **class IIa histone deacetylases** and phenocopying the skeletal program of combined *Sik2/Sik3* deletion. Within the normal **PTHrP–Indian hedgehog (Ihh) feedback loop**, PTH1R signaling — mediated critically by **Gsα** — restrains chondrocyte hypertrophy; when this signal is "locked on," maturation is pathologically delayed. Downstream renal effects include hypercalciuria, hypophosphatemia (with reported FGF23 elevation), nephrocalcinosis, and, in some patients, progressive chronic kidney disease. JMC is therefore best framed as a **dose-dependent constitutively-active PTH1R disorder** whose severity tracks with the intrinsic constitutive activity of the specific mutation (H223R severe; T410R milder).

**There is no approved disease-specific therapy.** Management is symptomatic — hydration, dietary calcium restriction, bisphosphonate plus thiazide for hypercalciuria, and orthopedic surgery for limb deformities. The leading mechanism-directed strategy is a class of **PTH1R inverse-agonist peptides** that suppress the mutant receptor's basal signaling and partially rescue skeletal defects in mouse models; a synthetic PTH inverse agonist is in clinical development. A key knowledge gap: essentially all molecular-profiling data derive from **mouse and cell models**, not human omics datasets, reflecting the disorder's ultra-rarity and tissue inaccessibility.

---

## 1. Disease Information

**Overview.** JMC is a rare form of short-limbed dwarfism (metaphyseal chondrodysplasia) characterized by severe growth-plate abnormalities with metaphyseal widening/irregularity, progressive skeletal deformity, distinctive craniofacial features, and — uniquely among the metaphyseal chondrodysplasias — **PTH-independent hypercalcemia** with low/normal circulating PTH and PTHrP.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | **#156400** |
| Gene | *PTH1R* (aka PTHR1, PTH/PTHrP receptor); OMIM *168468; HGNC:*PTH1R*; UniProt **Q03431** |
| MONDO | Metaphyseal chondrodysplasia, Jansen type (Mendelian; MONDO ID not resolved in this investigation) |
| Category | Mendelian, autosomal dominant |

**Synonyms / alternative names:** Jansen metaphyseal chondrodysplasia; Jansen-type metaphyseal dysplasia; Jansen's disease; metaphyseal dysostosis, Jansen type; Murk Jansen type metaphyseal chondrodysplasia.

**Source of information.** Because JMC is ultra-rare, the knowledge base derives from **aggregated disease-level resources** (OMIM, Orphanet) and **published case reports / small case series** rather than large EHR cohorts. The largest natural-history dataset assembled to date comprised 24 patients ([PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)).

---

## 2. Etiology

**Primary cause — genetic.** JMC is caused by **heterozygous activating (gain-of-function) missense mutations in *PTH1R***. In HEK293/COS-7 reporter cells the mutant receptors exhibit constitutive, ligand-independent cAMP accumulation. Disease is **autosomal dominant**; most cases arise **de novo**, though multigenerational transmission (e.g., a father and two sons with T410R) is documented (Finding F001; [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/); [PMID: 27160269](https://pubmed.ncbi.nlm.nih.gov/27160269/)).

> "Five different activating PTH/PTH-related peptide (PTHrP) receptor (PTHR1) mutations have been reported as causes of Jansen metaphyseal chondrodysplasia (JMC), a rare disorder characterized by severe growth plate abnormalities and PTH-independent hypercalcemia." — [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)

**Genetic risk factors.** The causal variants themselves are the risk factors; there are no known common susceptibility loci or modifier alleles in humans. Because the mechanism is a dominant, activating point mutation, the mutation is both necessary and sufficient.

**Environmental risk factors.** None established. There are no known toxic, infectious, occupational, or lifestyle causes. Family history is relevant only in the minority of inherited (non-de novo) cases.

**Protective factors.** No genetic or environmental protective factors have been identified.

**Gene–environment interactions.** None established for disease causation. Environmental modulation is limited to **symptom management** (e.g., dietary calcium restriction, hydration reducing the hypercalcemia/hypercalciuria burden).

---

## 3. Phenotypes

JMC is a **multisystem disorder** with a defining skeletal + mineral-ion phenotype plus renal, ocular, and possibly cardiovascular involvement (Findings F002, F009, F012).

### Skeletal / physical manifestations (clinical signs; congenital-to-childhood onset; progressive)
- **Metaphyseal widening and irregularity** of long bones; disorganized growth-plate cartilage. *HPO: HP:0003025 Metaphyseal widening; HP:0000944 Abnormality of the metaphysis.*
- **Short-limbed short stature / dwarfism** — adult heights well below the 3rd percentile in all patients **except** those with the milder T410R mutation (F010; [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)). *HPO: HP:0004322 Short stature.*
- **Bowed limbs / progressive limb deformity**; most patients undergo orthopedic surgery. *HPO: HP:0002751 Kyphoscoliosis; HP:0002986 Radial bowing.*
- **Craniofacial dysmorphism** (prominent supraorbital ridges, midface hypoplasia, micrognathia). *HPO: HP:0000316 Hypertelorism; HP:0000347 Micrognathia.*

### Mineral-ion / laboratory abnormalities (biochemical; childhood-predominant)
- **PTH-independent hypercalcemia** (normal at birth; elevated ~0.15–10 yr, mean 11.8 ± 1.37 mg/dL; tends to normalize in adults, 10.0 ± 1.03 mg/dL). *HPO: HP:0003072 Hypercalcemia. CHEBI:29108 calcium(2+).*
- **Hypercalciuria** (urinary Ca/creatinine children 0.80 ± 0.40; adults 0.28 ± 0.19). *HPO: HP:0002150 Hypercalciuria.*
- **Hypophosphatemia** (lower end of age-specific ranges); reported **FGF23 elevation**. *HPO: HP:0002148 Hypophosphatemia. CHEBI:43474 hydrogenphosphate.*
- **Low / normal PTH** despite hypercalcemia — the diagnostic hallmark.

> "Postnatal calcium levels were normal in most patients, but elevated between 0.15 and 10 years (11.8 ± 1.37 mg/dL) and tended to normalize in adults (10.0 ± 1.03 mg/dL)." — [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)

### Renal (progressive)
- **Nephrocalcinosis** (most patients), nephrolithiasis, and **advanced chronic kidney disease** in a subset (2/24). *HPO: HP:0000121 Nephrocalcinosis; HP:0012622 Chronic kidney disease.*

> "Most patients with JMC had undergone orthopedic surgical procedures, most had nephrocalcinosis, and two had advanced chronic kidney disease." — [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)

### Other systems
- **Ocular findings** characterized in JMC (calcium-deposition context; [PMID: 39108358](https://pubmed.ncbi.nlm.nih.gov/39108358/)).
- **Severe infantile hypertension** proposed as a previously unrecognized feature ([PMID: 31977144](https://pubmed.ncbi.nlm.nih.gov/31977144/)). *HPO: HP:0000822 Hypertension.*

> "Hypertension has not been previously associated with JMC." — [PMID: 31977144](https://pubmed.ncbi.nlm.nih.gov/31977144/)

- **Hypercalcemia symptom complex in infants:** failure to thrive, poor feeding, constipation, polyuria, irritability, lethargy, seizures, hypotonia ([PMID: 33990852](https://pubmed.ncbi.nlm.nih.gov/33990852/)).

> "Hypercalcaemia presents clinically with a range of symptoms including failure to thrive, poor feeding, constipation, polyuria, irritability, lethargy, seizures and hypotonia." — [PMID: 33990852](https://pubmed.ncbi.nlm.nih.gov/33990852/)

**Quality-of-life impact.** Substantial: severe short stature and progressive limb deformity requiring repeated orthopedic surgery impair mobility and function; nephrocalcinosis/CKD add chronic renal morbidity. No disease-specific EQ-5D/SF-36 data are available (ultra-rare disease).

**Onset / severity / progression / frequency (summary):**

| Phenotype | HPO | Onset | Severity | Progression | Frequency |
|---|---|---|---|---|---|
| Short stature | HP:0004322 | Childhood | Severe (except T410R) | Progressive | Nearly all |
| Metaphyseal widening | HP:0003025 | Congenital/childhood | Severe | Progressive | All |
| Hypercalcemia | HP:0003072 | Infancy–childhood | Variable | Peaks in childhood, normalizes in adults | Most |
| Hypercalciuria | HP:0002150 | Childhood | Moderate–severe | Persistent | Consistent |
| Nephrocalcinosis | HP:0000121 | Childhood | Variable | Progressive | Most |
| CKD | HP:0012622 | Later | Severe | Progressive | Subset (2/24) |

---

## 4. Genetic / Molecular Information

**Causal gene:** ***PTH1R*** (chromosome 3p21.31), encoding a class B1 (secretin-family) G-protein-coupled receptor.

**Pathogenic variant spectrum (all heterozygous, activating):**

| Variant | Location | Frequency in largest cohort | Constitutive activity | Phenotype |
|---|---|---|---|---|
| **H223R** | 1st intracellular loop (exon M2) | 18/24 patients (most common) | High | Severe |
| **T410P** | TM helix | Single case | Moderate–high | Severe |
| **T410R** | TM helix | Father + 2 sons | Lower | **Milder** |
| **I458R** | TM7 | Single case | ~8× basal vs WT | Severe-like |
| **I458K** | TM7 | Single case | High | Severe |

(F001; [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/); [PMID: 10487664](https://pubmed.ncbi.nlm.nih.gov/10487664/))

> "The H223R mutation occurred in 18 patients. T410P, I458R and I458K each occurred in single cases; T410R was present in a father and his two sons." — [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)

- **Variant classification (ACMG/AMP):** pathogenic (functional constitutive-activation evidence + segregation). Some newly reported *PTH1R* variants are classified VUS (e.g., p.E465K, [PMID: 37840415](https://pubmed.ncbi.nlm.nih.gov/37840415/)).
- **Variant type:** all **missense**.
- **Allele frequency:** absent from population databases (gnomAD) — private/de novo pathogenic variants.
- **Origin:** **germline** (de novo in most; inherited in some pedigrees). Germline mosaicism is plausible but not systematically documented.
- **Functional consequence:** **gain of function** — constitutive, ligand-independent Gsα–cAMP signaling (F001; [PMID: 27160269](https://pubmed.ncbi.nlm.nih.gov/27160269/)).

> "Constitutive, ligand-independent cAMP accumulation was observed in HEK293T cells expressing the Mut-PTH1R." — [PMID: 27160269](https://pubmed.ncbi.nlm.nih.gov/27160269/)

**Allelic disorder spectrum (differential diagnosis; F007).** *PTH1R* variants cause a spectrum defined by signaling **direction** and **zygosity**:

| Disorder | Zygosity | Effect | Skeletal consequence |
|---|---|---|---|
| **JMC** | Heterozygous | **Gain of function** (constitutive) | Delayed ossification + hypercalcemia |
| **Blomstrand lethal chondrodysplasia** | Homozygous / compound-het | Severe loss of function | Neonatal-lethal, **accelerated** ossification |
| **Eiken syndrome** | Homozygous | Milder LOF | Delayed ossification |
| **PHP-like (hypocalcemia/hyperphosphatemia)** | Homozygous (e.g., R186H) | LOF | Mineral-ion disturbance |
| **Primary failure of tooth eruption (PFE)** | Heterozygous | LOF | Non-syndromic dental |
| **Brachydactyly type E syndrome (H8 variants E465K, E469K)** | Heterozygous | Impaired signaling | Mild short stature, dental anomalies |

> "Heterozygous PTH1R mutations that lead to constitutively activity were identified in Jansen metaphyseal chondrodysplasia, and homozygous or compound heterozygous mutations that lead to less-active or completely inactive receptors were identified in patients with Blomstrand lethal chondrodysplasia." — [PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)

> "Severe loss-of-function homozygous mutations in PTH1R are incompatible with life as in Blomstrand's lethal chondrodysplasia, characterized by accelerated growth plate ossification." — [PMID: 40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/)

**Modifier genes / epigenetics / chromosomal abnormalities.** No human modifier genes are established. Downstream **class IIa HDACs** are key epigenetic effectors of PTH1R signaling in bone (mechanistic, mouse; see §6). No chromosomal abnormalities are involved (JMC is a point-mutation disorder).

---

## 5. Environmental Information

**Not applicable as a cause.** JMC is a purely monogenic, constitutively-active-receptor disorder. No environmental factors, lifestyle factors, or infectious agents cause or trigger the disease. Environmental variables are relevant only to **symptom modulation** (dietary calcium, fluid intake affecting stone/nephrocalcinosis risk).

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)

```
Heterozygous activating PTH1R mutation (H223R / T410P/R / I458R/K)
        │  (stabilizes active receptor conformation)
        ▼
Constitutive, ligand-independent Gsα activation
        │
        ▼
Elevated basal cAMP  →  PKA  →  inhibition of SIK2/SIK3
        │                              │
        │                              ▼
        │                 de-repression of class IIa HDACs / CRTC
        │                              │
        ▼                              ▼
GROWTH PLATE:                    Transcriptional program of
delayed chondrocyte              constitutively-active PTH1R
hypertrophy; prolonged           (= phenocopy of Sik2/Sik3 loss)
hypertrophic zone;                      │
disorganized metaphysis  ◄──────────────┘
        │
        ▼
Metaphyseal widening, bowed limbs, short stature

KIDNEY / MINERAL: constitutive renal PTH1R signaling
   → ↑ Ca reabsorption / bone Ca release → HYPERCALCEMIA (PTH-independent)
   → hypercalciuria, ↑FGF23 → hypophosphatemia
   → nephrocalcinosis → CKD
```

### Molecular pathways
- **PTH/PTHrP receptor → Gsα → adenylyl cyclase → cAMP → PKA** is the primary driver. PTH1R also couples to **Gq/PLC**, but the JMC phenotype is dominated by the Gsα–cAMP arm ([PMID: 15765186](https://pubmed.ncbi.nlm.nih.gov/15765186/); [PMID: 40571720](https://pubmed.ncbi.nlm.nih.gov/40571720/)).
- **cAMP–SIK–HDAC axis:** PTH1R activation inhibits SIKs; combined *Sik2/Sik3* deletion phenocopies constitutively active PTH1R, with **class IIa HDACs** as the key regulated substrates in chondrocytes and osteocytes (F003; [PMID: 31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/)).

> "Combined deletion of Sik2 and Sik3 in osteoblasts and osteocytes led to a dramatic increase in bone mass that closely resembled the skeletal and molecular phenotypes observed when these bone cells express a constitutively active PTH1R that causes Jansen's metaphyseal chondrodysplasia." — [PMID: 31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/)

> "genetic evidence demonstrated that class IIa histone deacetylases were key PTH1R-regulated SIK substrates in both chondrocytes and osteocytes" — [PMID: 31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/)

### Developmental mechanism — the PTHrP–Ihh loop (F006)
In normal endochondral development, **PTHrP** (made in the periarticular growth plate) acts on PTH1R to **keep chondrocytes proliferating and delay hypertrophy**; **Ihh** (from prehypertrophic chondrocytes) induces PTHrP, forming a negative-feedback loop that sets the pace of differentiation and the site of bone-collar formation. **Gsα is the critical mediator**: chondrocyte-specific *Gsα* knockout **accelerates** hypertrophy (phenocopying receptor knockout), whereas constitutive PTH1R activation (JMC) does the opposite — **delaying** hypertrophy.

> "As chondrocytes go through a program of proliferation and then further differentiation into post-mitotic, hypertrophic chondrocytes, PTHrP action keeps chondrocytes proliferating and delays their further differentiation." — [PMID: 16831900](https://pubmed.ncbi.nlm.nih.gov/16831900/)

> "These results show that G(s)alpha negatively regulates chondrocyte differentiation and is the critical signaling mediator of the PTH/PTH-rP receptor in growth plate chondrocytes." — [PMID: 15765186](https://pubmed.ncbi.nlm.nih.gov/15765186/)

Downstream effectors delaying hypertrophy/apoptosis include **Bcl-2 upregulation**, suppression of **p57** and **Runx2**, **SOX9 phosphorylation**, and upregulation of **Zfp521** (a rescue target — see §15).

> "PTHrP increases the expression of Bcl-2, a protein that controls programmed cell death in several cell types, in growth plate chondrocytes both in vitro and in vivo, leading to delays in their maturation towards hypertrophy and apoptotic cell death." — [PMID: 9008714](https://pubmed.ncbi.nlm.nih.gov/9008714/)

### Cellular processes / tissue damage
- **Delayed chondrocyte hypertrophic differentiation** and prolonged persistence of hypertrophic chondrocytes (growth-plate disorganization).
- **High-turnover bone disease:** histomorphometry in H223R children shows irregular architecture, increased osteoid, prolonged osteoid maturation, intense cortical osteoclast activity, marrow fibrosis, and osteocytes with osteoid buildup in lacunae/shortened canaliculi — a **PTH-like bone phenotype** (F009; [PMID: 39950977](https://pubmed.ncbi.nlm.nih.gov/39950977/)).

> "Cortical bone displayed areas of intense osteoclast activity and scattered marrow fibrosis." — [PMID: 39950977](https://pubmed.ncbi.nlm.nih.gov/39950977/)

### Protein dysfunction / structural basis (F011)
PTH1R is a **prototypical class B1 GPCR** coupling to both Gs and Gq (UniProt Q03431). Cryo-EM structures with PTH, PTHrP, abaloparatide, LA-PTH, and M-PTH(1-14) show the agonist N-terminus engaging the **transmembrane bundle** to drive Gαs activation ([PMID: 37148874](https://pubmed.ncbi.nlm.nih.gov/37148874/); [PMID: 40571720](https://pubmed.ncbi.nlm.nih.gov/40571720/)). The JMC mutations map to **activation-critical regions**: H223 in the first intracellular loop near the G-protein interface, and T410/I458 in transmembrane helices — positions where substitutions **stabilize the active conformation**, producing ligand-independent signaling.

> "we describe cryo-EM structures of the PTH1R in complex with fragments of the two hormones, PTH and PTH-related protein, the drug abaloparatide, as well as the engineered tool compounds, long-acting PTH (LA-PTH) and the truncated peptide, M-PTH(1-14)" — [PMID: 37148874](https://pubmed.ncbi.nlm.nih.gov/37148874/)

> "The critical N terminus of each agonist engages the transmembrane bundle in a topologically similar fashion, reflecting similarities in measures of Gαs activation." — [PMID: 37148874](https://pubmed.ncbi.nlm.nih.gov/37148874/)

### Metabolic / immune / molecular profiling
- **Metabolic:** dysregulated calcium/phosphate homeostasis (hypercalcemia, hypophosphatemia, hypercalciuria; FGF23 elevation contributing to renal phosphate wasting).

> "Hypophosphatemia is also a hallmark of JMC, and recently, increased fibroblast growth factor 23 (FGF23) levels have been reported in this syndrome." — [PMID: 22278430](https://pubmed.ncbi.nlm.nih.gov/22278430/)

- **Immune involvement:** none established.
- **Molecular profiling (F013):** No large-scale human transcriptomic/proteomic/metabolomic/single-cell datasets specific to JMC exist in public repositories (GEO/ArrayExpress/PRIDE/MetaboLights). The molecular signature comes from **mouse/cell models** — the SIK–HDAC transcriptional program ([PMID: 31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/)) and the Col2a1-H223R growth-plate delayed-maturation program ([PMID: 9391087](https://pubmed.ncbi.nlm.nih.gov/9391087/)). Human-level "omics" is limited to targeted biochemistry and bone histomorphometry/IHC.

> "immunohistochemical analysis demonstrated increased in PTH1R expression in both osteoblasts and fibroblastic cells on the bone surface" — [PMID: 39950977](https://pubmed.ncbi.nlm.nih.gov/39950977/)

**Suggested GO terms:** GO:0007189 (adenylate cyclase-activating GPCR signaling), GO:0002062 (chondrocyte differentiation), GO:0003416 (endochondral bone growth), GO:0071107 (response to parathyroid hormone), GO:0007050 (cell cycle arrest). **Suggested CL terms:** CL:0000138 (chondrocyte), CL:0000743 (hypertrophic chondrocyte), CL:0000062 (osteoblast), CL:0000137 (osteocyte), CL:0000092 (osteoclast).

---

## 7. Anatomical Structures Affected

**Organ / system level (primary → secondary):**
- **Skeletal system (primary):** long-bone metaphyses, growth plates (physes), cranium, mandible, spine. *UBERON:0002515 metaphysis; UBERON:0002481 growth plate cartilage / physis; UBERON:0001474 bone element.*
- **Urinary system (secondary):** kidney (nephrocalcinosis, CKD). *UBERON:0002113 kidney.*
- **Ocular (secondary):** cornea/eye (calcium deposition). *UBERON:0000970 eye.*
- **Cardiovascular (candidate):** systemic vasculature (infantile hypertension). *UBERON:0001981 blood vessel.*
- **Endocrine / mineral-homeostasis axis** (functionally central).

**Tissue / cell level:**
- **Cartilage / growth-plate chondrocytes** (proliferative and hypertrophic zones). *CL:0000138 chondrocyte; CL:0000743 hypertrophic chondrocyte.*
- **Bone: osteoblasts, osteocytes, osteoclasts** (high-turnover remodeling). *CL:0000062 osteoblast; CL:0000137 osteocyte; CL:0000092 osteoclast.*

**Subcellular level:** plasma membrane (receptor); cytoplasmic cAMP/PKA signaling; nucleus (HDAC/CRTC-regulated transcription). *GO:0005886 plasma membrane; GO:0005737 cytoplasm; GO:0005634 nucleus.*

**Localization / lateralization:** skeletal involvement is **generalized and bilateral/symmetric** (systemic germline receptor activation).

---

## 8. Temporal Development

**Onset:** **congenital-to-early-childhood**; radiographic metaphyseal changes present early; serum calcium **normal at birth**, then rises between ~0.15 and 10 years (F002). Onset pattern is **chronic/insidious**.

**Progression:**
- Skeletal deformity is **progressive** through childhood; short stature is established and permanent (except milder T410R).
- **Hypercalcemia** peaks in childhood and **tends to normalize in adulthood** — a distinctive age-dependent course ([PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)).
- **Renal disease** (nephrocalcinosis → CKD) is progressive in a subset.

**Disease course:** chronic, lifelong. No spontaneous remission of the skeletal phenotype; the hypercalcemia component partially self-attenuates with age.

**Critical periods / windows of opportunity:** the **growth-plate–active childhood window** is the key period for skeletal morbidity and the theoretical window for mechanism-directed (inverse-agonist) intervention before physeal closure.

---

## 9. Inheritance and Population

**Epidemiology.** JMC is **ultra-rare** — only a few dozen well-documented patients worldwide (largest cohort n=24; [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)). Precise prevalence/incidence are not established (Orphanet: <1/1,000,000).

**Inheritance:** **autosomal dominant**. Most cases are **de novo**; vertical transmission occurs (e.g., T410R father→sons; H223R mother→sons).

**Penetrance / expressivity:** high penetrance but **variable expressivity** — an H223R-carrier mother "was never overtly hypercalcemic and was therefore not diagnosed until her sons were found to be affected" (F010; [PMID: 27410178](https://pubmed.ncbi.nlm.nih.gov/27410178/)). Incomplete penetrance has been reported for some novel *PTH1R* variants ([PMID: 37840415](https://pubmed.ncbi.nlm.nih.gov/37840415/)).

> "the now 38-year-old mother was never overtly hypercalcemic and was therefore not diagnosed until her sons were found to be affected by JMC" — [PMID: 27410178](https://pubmed.ncbi.nlm.nih.gov/27410178/)

**Genotype–phenotype correlation (F010):** severity tracks with the **degree of constitutive activity**. H223R → profound hypercalcemia + severe short stature; **T410R → milder** (only mutation with near-normal adult height; near-normal longevity in humanized mice).

> "Adult heights were well below the 3rd percentile for all patients, except for those with the T410R mutation." — [PMID: 29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/)

**Anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** No genetic anticipation (not a repeat-expansion disorder). No founder effects; consanguinity is **not** relevant (dominant, de novo). Carrier frequency is not applicable. (Consanguinity is relevant instead to the *recessive* allelic disorders — Blomstrand, Eiken.)

**Demographics:** no ethnic predilection; no strong sex bias reported (dominant, sporadic). Presents in infancy/childhood.

---

## 10. Diagnostics

**Biochemical (cornerstone):** the diagnostic signature is **hypercalcemia + hypercalciuria + hypophosphatemia with LOW/NORMAL PTH** (PTH-independent hypercalcemia). FGF23 may be elevated. This distinguishes JMC from PTH-dependent hypercalcemias (F002, F012). *LOINC: serum calcium, phosphate, intact PTH; urine calcium/creatinine ratio.*

**Imaging:** skeletal radiographs show **metaphyseal widening/irregularity, cupping, sclerotic and lucent changes**, and progressive deformity — the defining radiographic features (case reports [PMID: 10901979](https://pubmed.ncbi.nlm.nih.gov/10901979/); [PMID: 6974367](https://pubmed.ncbi.nlm.nih.gov/6974367/)). Renal ultrasound demonstrates nephrocalcinosis.

**Genetic testing (confirmatory):** targeted **single-gene sequencing of *PTH1R*** or skeletal-dysplasia/hypercalcemia **gene panels**; WES/WGS in undiagnosed cases. Detection of a heterozygous activating variant (H223R, T410P/R, I458R/K) is confirmatory. Chromosomal microarray/karyotype are not informative (point-mutation disorder).

**Bone biopsy / histomorphometry:** high-turnover changes (increased osteoid, osteoclast activity, marrow fibrosis; increased PTH1R IHC) — research/selected use ([PMID: 39950977](https://pubmed.ncbi.nlm.nih.gov/39950977/)).

**Differential diagnosis (F007, F012):**
- Other **metaphyseal chondrodysplasias** — Schmid, McKusick, Spahr, Shwachman — separable by clinical/radiographic/biochemical criteria; **only JMC has hypercalcemia** ([PMID: 8644413](https://pubmed.ncbi.nlm.nih.gov/8644413/)).
- **Rickets** (a classic radiographic mimic).
- **PTH-dependent hypercalcemias:** neonatal severe hyperparathyroidism, familial hypocalciuric hypercalcemia (FHH) — these have **high PTH** ([PMID: 33990852](https://pubmed.ncbi.nlm.nih.gov/33990852/)).
- **Other PTH-independent pediatric hypercalcemias:** Williams-Beuren syndrome, hypophosphatasia, idiopathic infantile hypercalcemia ([PMID: 34774247](https://pubmed.ncbi.nlm.nih.gov/34774247/)).

> "Other types are Schmid, Spahr, McKusick, Schwachman and Jansen, which can be separated by clinical, radiographic, genetic and biochemical criteria." — [PMID: 8644413](https://pubmed.ncbi.nlm.nih.gov/8644413/)

> "Hypercalcemia can rarely be associated with immobilization, genetic diseases in children such as Williams-Beuren syndrome, Hypophosphatasia, Jansen Metaphyseal Chondrodysplasia (JMC)" — [PMID: 34774247](https://pubmed.ncbi.nlm.nih.gov/34774247/)

**Screening:** No population newborn screening. **Cascade genetic testing** of at-risk relatives is appropriate in familial cases; prenatal/preimplantation testing is feasible once the family variant is known.

---

## 11. Outcome / Prognosis

**Survival / mortality:** JMC is generally **compatible with survival into adulthood** (contrast with neonatal-lethal Blomstrand chondrodysplasia). No formal life-expectancy tables exist; prognosis is dominated by **renal** (CKD from nephrocalcinosis) and **orthopedic** morbidity.

**Morbidity / function:** substantial lifelong disability from **severe short stature and progressive limb deformity** (most patients require orthopedic surgery), plus chronic renal disease in a subset. Hypercalcemia-related symptoms burden infancy/childhood.

**Disease course / complications:** nephrocalcinosis, nephrolithiasis, progressive CKD (2/24 advanced), skeletal deformity requiring surgery, and candidate infantile hypertension.

**Prognostic factors:** the **specific mutation** is the strongest predictor — **T410R milder**, H223R more severe. The natural attenuation of hypercalcemia in adulthood is a favorable biochemical trend.

---

## 12. Treatment

**No approved disease-specific therapy exists.** Management is **symptomatic/supportive** (F004, F008).

**Supportive medical management:**
- Hydration; **dietary calcium restriction**; control of hypercalcemia/hypercalciuria.
- **Bisphosphonate (alendronate)** reduced hypercalciuria in an adult H223R patient; **normocalciuria required adding a thiazide diuretic**; FGF23 remained normal under treatment ([PMID: 22278430](https://pubmed.ncbi.nlm.nih.gov/22278430/)). *NCIT: bisphosphonate therapy; thiazide diuretic.*

> "Treatment with alendronate reduced hypercalciuria; however, normocalciuria was only obtained with the association of thiazide diuretic." — [PMID: 22278430](https://pubmed.ncbi.nlm.nih.gov/22278430/)

**Orthopedic surgery:** frequently required for limb deformity/correction. *NCIT: orthopedic surgical procedure.*

**Rehabilitation / renal care:** physical therapy; nephrology management of nephrocalcinosis/CKD.

**Mechanism-directed / experimental — PTH1R inverse agonists (leading strategy; F004):**
- **N-terminally truncated PTH/PTHrP antagonist peptides act as inverse agonists**, reducing the high basal cAMP of JMC mutant receptors in vitro; [L11,dW12,W23,Y36]PTHrP(7-36) reduced basal cAMP for all five mutants ([PMID: 31693237](https://pubmed.ncbi.nlm.nih.gov/31693237/)).
- An **inverse-agonist ligand partially rescued skeletal defects** in a JMC mouse model ([PMID: 31693237](https://pubmed.ncbi.nlm.nih.gov/31693237/)).
- A **backbone-modified long-acting peptide** functions as an inverse agonist of PTH1R-H223R **in vitro and in vivo** ([PMID: 38417010](https://pubmed.ncbi.nlm.nih.gov/38417010/)).
- A **synthetic PTH inverse agonist (PTH-IA)** is in clinical development, with anti-drug-antibody assays already established ([PMID: 42572867](https://pubmed.ncbi.nlm.nih.gov/42572867/)).

> "we found that certain N-terminally truncated PTH and PTHrP antagonist peptides function as inverse agonists and thus can reduce the high rates of basal cAMP signaling exhibited by the mutant PTHR1s of JMC in vitro" — [PMID: 31693237](https://pubmed.ncbi.nlm.nih.gov/31693237/)

> "a peptidic PTH1R inhibitor that displays prolonged activity as an antagonist of wild-type PTH1R and an inverse agonist of the constitutively active PTH1R-H223R mutant both in vitro and in vivo" — [PMID: 38417010](https://pubmed.ncbi.nlm.nih.gov/38417010/)

**Personalized medicine:** because severity and receptor pharmacology are mutation-specific, an inverse agonist confirmed active against **all five mutants** supports a genotype-agnostic-yet-mechanism-targeted approach. Structure-guided design also extends to **de novo GPCR-targeting miniproteins** ([PMID: 42168559](https://pubmed.ncbi.nlm.nih.gov/42168559/)).

---

## 13. Prevention

- **Primary prevention:** not possible for de novo dominant mutations. In **familial** cases, **genetic counseling**, prenatal diagnosis, and preimplantation genetic testing can prevent recurrence.
- **Secondary prevention:** early biochemical detection (Ca/Pi/PTH) and imaging in symptomatic infants; early nephrology surveillance to limit nephrocalcinosis/CKD.
- **Tertiary prevention:** manage hypercalciuria (bisphosphonate + thiazide) to reduce stone/nephrocalcinosis burden; orthopedic monitoring; renal protection.
- **Counseling:** genetic counseling is central — clarifying **AD inheritance, high de novo rate, and variable expressivity** (a mildly affected/undiagnosed parent may carry the variant; [PMID: 27410178](https://pubmed.ncbi.nlm.nih.gov/27410178/)).
- **Immunization / public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *PTH1R* is highly conserved. Functional models exist in **mouse (*Mus musculus*, NCBI Taxon 10090)**; the ortholog is *Pth1r*. Zebrafish and other vertebrates possess conserved PTH1R signaling.
- **Natural disease in animals:** No well-established naturally-occurring JMC-equivalent (constitutively-active PTH1R) disease is documented in companion animals or wildlife in this investigation (OMIA not confirmed here).
- **Comparative biology:** the PTHrP–Ihh–PTH1R growth-plate circuit is **evolutionarily conserved**; mouse models faithfully reproduce the human causal chain (see §15), making JMC a strong example of conserved endochondral-development mechanisms.
- **Transmission:** not applicable (non-infectious, genetic).

---

## 15. Model Organisms

JMC is unusually well-modeled in the mouse, providing the mechanistic backbone of the field (F005).

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| **Col2a1-HKrk-H223R transgenic** | Constitutively active receptor under α1(II) collagen promoter (chondrocyte-targeted) | Delayed mineralization; decelerated proliferative→hypertrophic conversion; prolonged hypertrophic chondrocytes | [PMID: 9391087](https://pubmed.ncbi.nlm.nih.gov/9391087/) |
| **Col1a1-H223R transgenic** | Osteoblast-targeted | Bone phenotype (↑ cortical bone) mirroring JMC | [PMID: 11713230](https://pubmed.ncbi.nlm.nih.gov/11713230/) |
| **Humanized H223R-hPTH1R knock-in** | Knock-in | Early lethal; cannot breed; **substantially delayed growth-plate chondrocyte maturation** | [PMID: 37808400](https://pubmed.ncbi.nlm.nih.gov/37808400/); [PMID: 40455993](https://pubmed.ncbi.nlm.nih.gov/40455993/) |
| **Humanized T410R-hPTH1R knock-in** | Knock-in (milder allele) | Near-normal longevity/breeding; misshapen long bones, expanded metaphyses, disarrayed growth-plate zones, reduced primary spongiosa | [PMID: 40455993](https://pubmed.ncbi.nlm.nih.gov/40455993/) |
| ***Sik2/Sik3* double KO** | Conditional KO (phenocopy) | Bone phenotype closely resembling constitutively active PTH1R | [PMID: 31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/) |
| ***Zfp521* deletion in Jansen chondrocytes** | Genetic rescue | Restores chondrocyte differentiation; partial rescue of bone length | [PMID: 21642473](https://pubmed.ncbi.nlm.nih.gov/21642473/) |
| **Chondrocyte-specific *Gsα* KO** | Conditional KO (opposite phenotype) | Accelerated hypertrophy (mirror of JMC) | [PMID: 15765186](https://pubmed.ncbi.nlm.nih.gov/15765186/) |

> "The targeted expression of constitutively active PTH/PTHrP receptors led to delayed mineralization, decelerated conversion of proliferative chondrocytes into hypertrophic cells in skeletal segments that are formed by the endochondral process, and prolonged presence of hypertrophic chondr[ocytes]." — [PMID: 9391087](https://pubmed.ncbi.nlm.nih.gov/9391087/)

> "The long bones of T410R mice are markedly misshapen and have expanded metaphyses with disarrayed chondrocyte zones in growth plates and reduced primary spongiosa." — [PMID: 40455993](https://pubmed.ncbi.nlm.nih.gov/40455993/)

> "Its ablation from Jansen chondrocytes restored normal cell differentiation, thus initiating chondrocyte apoptosis at the chondro-osseous junction, leading to partial rescue of endochondral bone formation shown by proper bone length." — [PMID: 21642473](https://pubmed.ncbi.nlm.nih.gov/21642473/)

**Phenotype recapitulation:** Excellent for the growth-plate/skeletal phenotype and for genetic-rescue proof-of-concept (Zfp521; inverse agonists). **Limitations:** the severe H223R humanized model is early-lethal and cannot breed, complicating long-term/therapeutic studies; the milder T410R model was engineered specifically to enable these. Renal/mineral-ion aspects and human natural history (adulthood normalization of calcium) are only partially captured.

**Model applications:** dissecting the PTHrP–Ihh–Gsα–SIK–HDAC pathway; testing **inverse-agonist therapeutics** in vivo; studying genotype–severity relationships. **Resources:** MGI (mouse); model lines maintained by originating academic laboratories.

---

## Mechanistic Model / Interpretation

JMC is best understood as a **"receptor stuck ON" disorder** — the biochemical and developmental inverse of Blomstrand chondrodysplasia (receptor OFF). A single class of lesion (heterozygous activating *PTH1R* missense mutation) produces the entire multisystem phenotype through **constitutive Gsα–cAMP signaling**:

```
      LOSS OF FUNCTION  ◄─────  PTH1R  ─────►  GAIN OF FUNCTION
   (Blomstrand, Eiken,           │            (JANSEN — JMC)
    PFE, PHP-like)               │
   accelerated ossification      │            delayed hypertrophy,
   ± hypocalcemia                │            PTH-INDEPENDENT hypercalcemia
                                 ▼
             constitutive Gsα → cAMP → PKA → ↓SIK2/3 → ↑class IIa HDAC
                                 │
        ┌────────────────────────┼─────────────────────────┐
        ▼                        ▼                          ▼
  GROWTH PLATE              BONE REMODELING            KIDNEY
  delayed hypertrophy       high turnover              ↑Ca reabsorption
  (metaphyseal dysplasia,   (osteoid, osteoclasts,     ↑FGF23 → ↓phosphate
   short stature)            marrow fibrosis)          nephrocalcinosis→CKD
```

**Upstream vs downstream:** the mutation (upstream) → constitutive cAMP (proximal effector) → SIK inhibition / HDAC de-repression (transcriptional node) → cell-type-specific outputs (downstream): delayed chondrocyte hypertrophy in cartilage, high-turnover remodeling in bone, and altered mineral handling in kidney. **Cell types:** growth-plate chondrocytes (proliferative + hypertrophic), osteoblasts, osteocytes, osteoclasts, and renal tubular cells. Therapeutic logic follows directly: **inverse agonists** that suppress the receptor's basal activity restore signaling toward normal and partially rescue the skeletal phenotype in mice — the most promising path to a disease-modifying treatment.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [7701349](https://pubmed.ncbi.nlm.nih.gov/7701349/) | Constitutively active mutant PTH-PTHrP receptor in JMC | Landmark 1995: H223R → constitutive cAMP (F008) |
| [29788189](https://pubmed.ncbi.nlm.nih.gov/29788189/) | Progression of mineral ion abnormalities (n=24) | Mutation spectrum; mineral-ion natural history (F001, F002, F009, F010) |
| [27160269](https://pubmed.ncbi.nlm.nih.gov/27160269/) | Characterization of a PTH1R missense mutation | Constitutive ligand-independent cAMP (F001) |
| [10487664](https://pubmed.ncbi.nlm.nih.gov/10487664/) | Novel PTH1R mutation (I458R) | I458R ~8× basal cAMP; H223R most frequent (F001) |
| [31430259](https://pubmed.ncbi.nlm.nih.gov/31430259/) | SIKs dictate PTH1R action in bone | SIK–HDAC downstream mechanism; molecular signature source (F003, F013) |
| [16831900](https://pubmed.ncbi.nlm.nih.gov/16831900/) | PTHrP and skeletal development | Normal PTH1R role in delaying hypertrophy (F006) |
| [15765186](https://pubmed.ncbi.nlm.nih.gov/15765186/) | Chondrocyte Gsα knockout | Gsα is critical PTH1R mediator (F006) |
| [9008714](https://pubmed.ncbi.nlm.nih.gov/9008714/) | Bcl-2 downstream of PTHrP | Bcl-2 delays chondrocyte maturation (F006) |
| [9391087](https://pubmed.ncbi.nlm.nih.gov/9391087/) | Targeted constitutively active receptors | Original Col2a1-H223R mouse model (F005, F013) |
| [21642473](https://pubmed.ncbi.nlm.nih.gov/21642473/) | Deletion of Zfp521 | Genetic rescue of Jansen growth plate (F005) |
| [40455993](https://pubmed.ncbi.nlm.nih.gov/40455993/) | Humanized JMC mouse model | H223R vs milder T410R knock-ins (F005, F010) |
| [37808400](https://pubmed.ncbi.nlm.nih.gov/37808400/) | Delayed maturation in humanized mice | Growth-plate delay in humanized model (F003, F005) |
| [31693237](https://pubmed.ncbi.nlm.nih.gov/31693237/) | Inverse agonist rescues skeletal defects | Inverse agonists suppress mutant signaling (F004) |
| [38417010](https://pubmed.ncbi.nlm.nih.gov/38417010/) | Backbone-modified long-acting inverse agonist | H223R inverse agonist in vivo (F004) |
| [42572867](https://pubmed.ncbi.nlm.nih.gov/42572867/) | ECL bridging assay for PTH inverse agonist | Clinical development of PTH-IA (F004) |
| [22278430](https://pubmed.ncbi.nlm.nih.gov/22278430/) | Alendronate + thiazide in adult JMC | Symptomatic hypercalciuria management; FGF23 (F002, F008) |
| [39950977](https://pubmed.ncbi.nlm.nih.gov/39950977/) | Bone abnormalities beyond chondrodysplasia | High-turnover histomorphometry; PTH1R IHC (F009, F013) |
| [31977144](https://pubmed.ncbi.nlm.nih.gov/31977144/) | Severe hypertension in JMC | Candidate cardiovascular feature (F009) |
| [39108358](https://pubmed.ncbi.nlm.nih.gov/39108358/) | Ocular findings in JMC | Ocular involvement (F009) |
| [10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/) | Role of PTHrP and Ihh | GOF vs LOF dichotomy (F007) |
| [40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/) | Human diseases from homozygous PTH1R mutations | Blomstrand LOF contrast (F007) |
| [8644413](https://pubmed.ncbi.nlm.nih.gov/8644413/) | Metaphyseal chondrodysplasia vs rickets | Differential diagnosis (F007) |
| [33990852](https://pubmed.ncbi.nlm.nih.gov/33990852/) | Genetic neonatal/infantile hypercalcaemia | JMC in hypercalcemia differential (F012) |
| [34774247](https://pubmed.ncbi.nlm.nih.gov/34774247/) | Rare causes of hypercalcemia | JMC as rare hypercalcemia cause (F012) |
| [27410178](https://pubmed.ncbi.nlm.nih.gov/27410178/) | H223R with/without overt hypercalcemia | Variable expressivity (F010) |
| [37148874](https://pubmed.ncbi.nlm.nih.gov/37148874/) | Peptide agonist engagement with PTH1R | Cryo-EM structural basis (F011) |
| [40571720](https://pubmed.ncbi.nlm.nih.gov/40571720/) | G-protein coupling preference cryo-EM | Class B1 GPCR structure (F011) |
| [42168559](https://pubmed.ncbi.nlm.nih.gov/42168559/) | De novo design of GPCR-targeting miniproteins | Structure-guided therapeutic design (F011) |

**Evidence source types:** human clinical (case series/reports, biochemistry, histomorphometry), model organism (mouse transgenics/knock-ins/rescues), in vitro (HEK293/COS-7 cAMP reporter assays), and computational/structural (cryo-EM, de novo design).

---

## Limitations and Knowledge Gaps

1. **No human omics datasets (F013).** The molecular signature of JMC is inferred from mouse (SIK–HDAC) and cell models, not human transcriptomic/proteomic/metabolomic/single-cell data — a direct consequence of ultra-rarity and inaccessible growth-plate tissue.
2. **Small n / no formal epidemiology.** Prevalence, incidence, precise sex ratio, and life-expectancy tables are not established; the largest cohort is 24 patients.
3. **Newer/candidate features under-characterized.** Ocular findings and infantile hypertension are reported in single/few patients and need replication before being considered core features.
4. **Therapeutics are pre-approval.** Inverse-agonist efficacy is demonstrated in vitro and in mouse models with only partial skeletal rescue; human efficacy, dosing window (before physeal closure), and immunogenicity remain to be established.
5. **MONDO ID not resolved** in this investigation; OMIM #156400 is the authoritative identifier used.
6. **Renal/cardiovascular mechanisms** (FGF23 elevation, hypertension) are incompletely dissected relative to the skeletal phenotype.

---

## Proposed Follow-up Experiments / Actions

1. **Clinical trial of a PTH1R inverse agonist** in JMC patients (building on [PMID: 42572867](https://pubmed.ncbi.nlm.nih.gov/42572867/), [PMID: 38417010](https://pubmed.ncbi.nlm.nih.gov/38417010/)), prioritizing dosing during the growth-active childhood window, with skeletal, mineral-ion, and renal endpoints.
2. **Patient-derived iPSC → chondrocyte/organoid models** to generate the first **human** JMC transcriptomic/proteomic signatures and validate the SIK–HDAC axis in human cells.
3. **Longitudinal natural-history registry** capturing genotype (H223R vs T410R vs others), skeletal growth, renal function trajectory, and the adulthood normalization of hypercalcemia — powering genotype–phenotype and prognostic modeling.
4. **Systematic characterization of the renal and cardiovascular phenotypes** (FGF23 biology, nephrocalcinosis progression, infantile hypertension) in the milder T410R humanized mouse, which permits long-term/breeding studies ([PMID: 40455993](https://pubmed.ncbi.nlm.nih.gov/40455993/)).
5. **Structure-guided next-generation inverse agonists / de novo miniproteins** ([PMID: 42168559](https://pubmed.ncbi.nlm.nih.gov/42168559/)) optimized against all five mutant receptors, using the available cryo-EM structures ([PMID: 37148874](https://pubmed.ncbi.nlm.nih.gov/37148874/)).
6. **Resolve MONDO mapping** and reconcile Orphanet/OMIM/ICD identifiers for knowledge-base ingestion.

---

*Report compiled from 13 confirmed findings and 43 reviewed papers across 5 investigation iterations. Evidence sources span human clinical case series, mouse genetic models, in vitro receptor pharmacology, and cryo-EM structural biology.*


## Artifacts

- [OpenScientist final report](Metaphyseal_Chondrodysplasia_Jansen_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Metaphyseal_Chondrodysplasia_Jansen_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 30 |
| Quoted claims found in source | 30 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0007050` (1 mention) - the report calls it "cell cycle arrest"; GO calls it **GO_0007050**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007050` (GO_0007050) (1 mention) - replaced by `GO:0051726`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003025` (2 mentions) - the report calls it "Metaphyseal widening"; HP calls it **Metaphyseal irregularity**, and lists "Metaphyseal fraying" among its other names
- `GO:0007189` (1 mention) - the report calls it "adenylate cyclase-activating GPCR signaling"; GO calls it **adenylate cyclase-activating G protein-coupled receptor signaling pathway**, and lists "adenylate cyclase-activating GPCR signaling pathway" among its other names