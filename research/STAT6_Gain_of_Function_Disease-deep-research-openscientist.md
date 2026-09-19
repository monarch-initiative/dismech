---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-29T22:20:45.672975'
end_time: '2026-07-29T22:47:56.771194'
duration_seconds: 1631.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: STAT6 Gain-of-Function Disease
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: STAT6_Gain_of_Function_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: STAT6_Gain_of_Function_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** STAT6 Gain-of-Function Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **STAT6 Gain-of-Function Disease** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# STAT6 Gain-of-Function Disease (Hyper-IgE Syndrome 6, HIES6): A Comprehensive Disease Characterization Report

## Summary

**STAT6 gain-of-function (GOF) disease** is a rare, recently described (2023) autosomal-dominant **primary atopic disorder (PAD)**—one of a growing group of inborn errors of immunity (IEIs) in which a single germline gene defect produces severe, early-onset allergic disease. It is caused by germline heterozygous **activating (gain-of-function) missense variants in *STAT6*** (Signal Transducer and Activator of Transcription 6; chromosome 12q13.3; HGNC:11364; NCBI Gene 6778; OMIM 601512). Pathogenic variants cluster in the **DNA-binding domain**, with a recurrent hotspot at codon **Asp419 (D419H/Y/G/N)** and additional recurrent variants including E372K, E377K, E382Q, and D519H/N. These variants produce **constitutive and/or ligand-hypersensitive IL-4/IL-13–JAK–STAT6 signaling**, with sustained STAT6 phosphorylation, enhanced nuclear translocation (in some cases even without phosphorylation), increased STAT6 target-gene expression, and pathological **TH2 skewing** of the adaptive immune system.

Clinically, the disease presents in **infancy (100% of the founding cohort)** with a profound, multi-system allergic phenotype: **widespread treatment-resistant atopic dermatitis (94%)**, **hypereosinophilia and markedly elevated serum IgE (94%)**, **IgE-mediated food allergy (94%)**, **asthma (69%)**, **eosinophilic gastrointestinal disease (63%)**, and **anaphylaxis (56%)**. Variable features include recurrent skin/respiratory/viral infections, short stature, osteoporosis, and a small but important risk of **B-cell/follicular lymphoma (~6%)**, mechanistically linked to the same DNA-binding-domain residues that are recurrently mutated somatically in follicular lymphoma. The disorder is catalogued as **OMIM #620532** ("Hyper-IgE syndrome 6, autosomal dominant, with recurrent infections; HIES6") and **MONDO:0957807**.

The disease is **highly actionable**: because the driver is a hyperactive, druggable signaling axis, **pathway-targeted therapy is transformative**. The anti–IL-4Rα monoclonal antibody **dupilumab** and **JAK inhibitors (e.g., ruxolitinib)** improve both clinical manifestations and immunological biomarkers. Diagnosis relies on exome/genome sequencing with functional confirmation of STAT6 hyperactivation. Two constitutively active mouse models (Stat6VT transgenic and patient-derived D419N knock-in) recapitulate the human TH2/allergic phenotype and validate the causal mechanism. This report synthesizes 9 confirmed findings drawn from 11 reviewed papers into a full disease knowledge-base entry organized along the 15 requested characteristic domains, followed by a mechanistic model, evidence base, limitations, and proposed follow-up actions.

---

## Key Findings

### Finding 1 — STAT6 GOF disease is a novel autosomal-dominant primary atopic disorder caused by germline heterozygous gain-of-function *STAT6* variants

The defining evidence comes from a landmark international cohort of **16 patients from 10 families across three continents** (Sharma et al., 2023). **All patients carried monoallelic (heterozygous) rare variants in *STAT6***, and functional studies established a gain-of-function phenotype. As the authors state verbatim: *"All patients carried monoallelic rare variants in STAT6 and functional studies established their gain-of-function (GOF) phenotype with sustained STAT6 phosphorylation, increased STAT6 target gene expression, and TH2 skewing"* and *"This study identifies heterozygous GOF variants in STAT6 as a novel autosomal dominant allergic disorder"* ([PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/)). Inheritance was **sporadic (de novo) in 7 kindreds and autosomal dominant in 3 kindreds**, consistent with a dominant, GOF (not loss-of-function/haploinsufficiency) mechanism.

**Evidence source:** human clinical/genetic (multi-family cohort with functional validation).

### Finding 2 — Core clinical phenotype: early-onset treatment-resistant atopic dermatitis, hypereosinophilia, eosinophilic GI disease, asthma, elevated IgE, food allergy and anaphylaxis

The founding cohort described *"a profound phenotype of early-life onset allergic immune dysregulation, widespread treatment-resistant atopic dermatitis, hypereosinophilia with esosinophilic gastrointestinal disease, asthma, elevated serum IgE, IgE-mediated food allergies, and anaphylaxis"* ([PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/)). This multi-system atopic constellation is the diagnostic signature and is independently replicated in single-case/kindred reports: Baris et al. (E372K), Suratannon/independent (E377K), Minskaia (D419H), and Samra (D519N) each describe severe atopic dermatitis, eosinophilia, elevated IgE, and food allergy.

**Evidence source:** human clinical.

### Finding 3 — Recurrent pathogenic variants cluster in the STAT6 DNA-binding domain and cause constitutive/enhanced IL-4/JAK/STAT6 signaling

Reported germline missense variants include **p.E372K (c.1114G>A), p.E377K (c.1129G>A), p.E382Q (c.1144G>C), p.D419H (c.1255G>C), p.D419Y (c.1255G>T), p.D419G (c.1256A>G), p.D419N (c.1255G>A), and p.D519H/N (c.1555G>C)**—several within the **DNA-binding domain (DBD)**. Direct quotes anchor the mechanism:
- *"a missense mutation in the DNA binding domain of STAT6 (c.1114G>A, p.E372K)"* ([PMID: 36758835](https://pubmed.ncbi.nlm.nih.gov/36758835/)).
- *"a novel heterozygous germline mutation STAT6 c.1255G > C, p.D419H leading to overactivity of IL-4 JAK/STAT signalling pathway"* ([PMID: 37316763](https://pubmed.ncbi.nlm.nih.gov/37316763/)).
- Ligand independence was shown for D419N: *"even in the absence of IL-4 stimulation, we observed the translocation of mutant STAT6 in its unphosphorylated state, which activated gene expression"* ([PMID: 40603028](https://pubmed.ncbi.nlm.nih.gov/40603028/)).

Thus, some variants confer **hypersensitivity to IL-4** (elevated total/phospho-STAT6 at baseline and after IL-4, e.g., D419H) while others confer **constitutive, phosphorylation-independent nuclear translocation and transcription** (D419N).

**Evidence source:** human genetic + in vitro functional (HEK293T, patient PBMC, gastric organoids).

### Finding 4 — Targeted therapy: dupilumab and JAK inhibitors are effective; disease is associated with follicular lymphoma risk

Because the disease is driven by a hyperactive IL-4/IL-13–JAK–STAT6 axis, **blocking that axis is therapeutic**. *"Precision treatment with the anti-IL-4Rα antibody, dupilumab, was highly effective improving both clinical manifestations and immunological biomarkers"* ([PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/)); dupilumab was also effective for the D519N variant (Samra 2025, [PMID: 40502541](https://pubmed.ncbi.nlm.nih.gov/40502541/)). JAK inhibition targets the upstream kinases: *"The selective JAK1/JAK2 inhibitor ruxolitinib reduced pSTAT6 levels in D419H HEK293T cells and patient PBMC"* ([PMID: 37316763](https://pubmed.ncbi.nlm.nih.gov/37316763/)). Critically, the same Minskaia kindred (D419H) included **follicular lymphoma**, linking germline STAT6 GOF to lymphomagenesis.

**Evidence source:** human clinical (treatment response) + in vitro (pharmacodynamic).

### Finding 5 — Nosology and identifiers: OMIM #620532 (HIES6) / MONDO:0957807

STAT6 GOF disease is catalogued as **OMIM #620532** = "HYPER-IgE SYNDROME 6, AUTOSOMAL DOMINANT, WITH RECURRENT INFECTIONS; HIES6." The Mondo term **MONDO:0957807** ("hyper-IgE syndrome 6, autosomal dominant, with recurrent infections") cross-references OMIM:620532, GARD:0026874, MedGen:1851769, and UMLS:C5848786. The causal gene *STAT6* = OMIM 601512, HGNC:11364, NCBI Gene 6778, UniProt P42226. NCI Thesaurus **C212086** = "Activating STAT6 Gene Mutation." **No dedicated Orphanet/ORDO code** was identified at the time of research.

**Evidence source:** aggregated disease-level resources (OMIM, Mondo, MedGen, NCIt).

### Finding 6 — Quantitative phenotype frequencies (HPO annotations, n=16 founding cohort)

Official HPO disease annotations (OMIM:620532 / MONDO:0957807), all sourced to [PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/), provide curated frequencies (see the phenotype table in Section 3). They derive from the cohort description: *"widespread treatment-resistant atopic dermatitis, hypereosinophilia with esosinophilic gastrointestinal disease, asthma, elevated serum IgE, IgE-mediated food allergies, and anaphylaxis."*

**Evidence source:** curated ontology annotation of human clinical cohort.

### Finding 7 — ClinVar variant spectrum and gnomAD constraint support a DBD missense GOF mechanism (not haploinsufficiency)

ClinVar (transcript NM_003153.5) lists germline Pathogenic/Likely-pathogenic *STAT6* variants for "Hyper-IgE syndrome 6": c.1114G>A p.Glu372Lys (P), c.1144G>C p.Glu382Gln (P), c.1255G>C p.Asp419His (LP), c.1255G>T p.Asp419Tyr (P), c.1256A>G p.Asp419Gly (P), and c.1555G>C p.Asp519His (P). **Codon 419 is a recurrent hotspot.** gnomAD constraint metrics show *STAT6* is **LoF-tolerant** (pLI = 0.057; oe_lof upper bound = 0.54) but **missense-constrained** (mis_z = 3.47). This constraint signature—tolerant of loss-of-function but intolerant of missense change, combined with recurrent, clustered, dominant missense variants—is the classic fingerprint of a **gain-of-function**, not haploinsufficiency, disease mechanism.

**Evidence source:** population genomics / variant databases (computational).

### Finding 8 — Constitutively active STAT6 mouse models recapitulate the human TH2/allergic phenotype

Two independent mouse models validate causality. The **Stat6VT transgenic** expresses a constitutively active STAT6 in T cells and *"develop[s] spontaneous inflammation of the skin"* (allergic dermatitis) plus allergic airway disease ([PMID: 28653395](https://pubmed.ncbi.nlm.nih.gov/28653395/)). The **patient-derived D419N knock-in mouse** *"elicited an abnormal TH2-dominant immune response in vivo, with findings similar to those observed in patients"* ([PMID: 40603028](https://pubmed.ncbi.nlm.nih.gov/40603028/)). Together, these models reproduce the cardinal human features (atopic skin disease, airway disease, TH2 skewing).

**Evidence source:** model organism (mouse).

### Finding 9 — PARP14 links STAT6 GOF allergic disease to lymphomagenesis as a druggable co-activator

PARP14 (ARTD8) is an IL-4/STAT6-induced transcriptional co-activator: *"the presence of interleukin-4 (IL-4) and activated Stat6 induces the enzymatic activity of PARP14 that promotes T helper type 2 differentiation and allergic airway disease"* ([PMID: 28653395](https://pubmed.ncbi.nlm.nih.gov/28653395/)). PARP14 is also *"a novel target in STAT6 mutant follicular lymphoma"* ([PMID: 35851155](https://pubmed.ncbi.nlm.nih.gov/35851155/)). Because germline STAT6 GOF and somatic follicular-lymphoma STAT6 mutations affect the **same DNA-binding-domain residues (notably D419)**, PARP14 represents a shared, druggable downstream node connecting the allergic and oncologic ends of the disease spectrum.

**Evidence source:** model organism + in vitro / cancer genomics.

---

## Full Disease Characterization (15 Domains)

### 1. Disease Information

STAT6 GOF disease is a **monogenic, autosomal-dominant primary atopic disorder / inborn error of immunity** characterized by early-onset, severe, multi-system allergic disease driven by constitutive TH2 signaling. It was first defined as a distinct entity in 2023.

| Identifier type | Value |
|---|---|
| OMIM (disease) | #620532 (Hyper-IgE syndrome 6, autosomal dominant, with recurrent infections; HIES6) |
| Mondo | MONDO:0957807 |
| GARD | 0026874 |
| MedGen | 1851769 |
| UMLS | C5848786 |
| NCIt | C212086 (Activating STAT6 Gene Mutation) |
| Gene (OMIM) | *STAT6* 601512 |
| HGNC | 11364 |
| NCBI Gene | 6778 |
| UniProt | P42226 |
| Orphanet | None dedicated identified |
| ICD-10/ICD-11 | No specific code; mapped under primary immunodeficiency/atopic categories |
| MeSH | No dedicated term; indexed via STAT6 / hyper-IgE / hypersensitivity |

**Synonyms/alternative names:** STAT6 gain-of-function disease; STAT6-GOF; Hyper-IgE syndrome 6 (HIES6); autosomal dominant STAT6 GOF; STAT6-associated primary atopic disorder.

**Information source type:** Predominantly **aggregated disease-level resources** (OMIM, Mondo, HPO) built from a small number of **individual-patient case cohorts/reports** (n≈16 founding + additional single cases). This is a very rare, newly described disease, so all knowledge derives from individual patients described in the literature, not EHR-scale populations.

### 2. Etiology

- **Primary cause:** germline heterozygous **gain-of-function missense variants in *STAT6***. The disease is monogenic and genetic; no environmental or infectious cause is required.
- **Genetic risk factors:** the causal variants themselves (DBD hotspot D419 and neighbors E372, E377, E382, D519). No modifier loci are established.
- **Environmental risk factors:** none required for disease causation. Allergen exposure, as in common atopy, may trigger/exacerbate individual manifestations (food allergy, anaphylaxis, asthma), but the disease penetrates independent of specific exposures.
- **Protective factors:** none established genetically or environmentally. Therapeutically, IL-4Rα blockade and JAK inhibition suppress the disease phenotype (see Section 12).
- **Gene–environment interactions:** the hyperactive STAT6 axis lowers the threshold for TH2 responses to environmental allergens; thus environment shapes *which* allergic manifestations appear, while genotype drives the underlying diathesis. No formal GxE quantification exists.

### 3. Phenotypes

Quantitative HPO-annotated frequencies (n=16 founding cohort, [PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/)):

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Infantile onset | HP:0003593 | 16/16 (100%) | onset |
| Atopic dermatitis | HP:0001047 | 15/16 (94%) | clinical sign / skin |
| Food allergy | HP:0500093 | 15/16 (94%) | clinical sign |
| Increased eosinophil count | HP:0001880 | 15/16 (94%) | lab abnormality |
| Increased circulating IgE | HP:0003212 | present (high) | lab abnormality |
| Asthma | HP:0002099 | 11/16 (69%) | clinical sign / respiratory |
| Gastrointestinal eosinophilia | HP:0032064 | 10/16 (63%) | lab / histopathology |
| Anaphylactic shock | HP:0100845 | 9/16 (56%) | clinical sign |
| Recurrent skin infections | HP:0001581 | 7/16 (44%) | clinical sign |
| Short stature | HP:0004322 | 7/16 (44%) | physical manifestation |
| Recurrent respiratory infections | HP:0002205 | 5/16 (31%) | clinical sign |
| Gastroesophageal reflux | HP:0002020 | 4/16 (25%) | clinical sign |
| Osteoporosis | HP:0000939 | 3/16 (19%) | lab / imaging |
| Recurrent viral infections | HP:0004429 | 2/16 (13%) | clinical sign |
| B-cell lymphoma | HP:0012191 | 1/16 (6%) | neoplasm |
| Eosinophilic esophagitis | HP:0410151 | present | histopathology |
| Autosomal dominant inheritance | HP:0000006 | — | inheritance |

**Characteristics:** age of onset is **neonatal/infantile (100%)**; severity is generally **severe** (treatment-resistant atopic dermatitis); course is **chronic/progressive** with episodic anaphylaxis; **variable expressivity** is documented even within families (e.g., E377K kindred showed clinical heterogeneity, [PMID: 36216080](https://pubmed.ncbi.nlm.nih.gov/36216080/)). **Quality-of-life impact** is substantial: severe pruritic dermatitis, dietary restriction from food allergy, anaphylaxis risk, and growth impairment—though formal EQ-5D/SF-36 data are not available for this rare disease.

### 4. Genetic/Molecular Information

- **Causal gene:** *STAT6* (12q13.3; OMIM 601512; HGNC:11364; NCBI Gene 6778; UniProt P42226).
- **Pathogenic variants (germline, dominant):** E372K (c.1114G>A), E377K (c.1129G>A), E382Q (c.1144G>C), D419H (c.1255G>C), D419Y (c.1255G>T), D419G (c.1256A>G), D419N (c.1255G>A), D519H/N (c.1555G>C). **Codon D419 is the recurrent hotspot.**
- **Variant classification (ACMG/AMP, ClinVar):** Pathogenic (E372K, E382Q, D419Y, D419G, D519H) or Likely pathogenic (D419H).
- **Variant type:** exclusively **missense** to date.
- **Allele frequency:** these variants are **absent or ultra-rare** in gnomAD; *STAT6* is missense-constrained (mis_z = 3.47) and LoF-tolerant (pLI = 0.057, oe_lof upper = 0.54).
- **Somatic vs germline:** the disease variants are **germline**; notably, **somatic** STAT6 DBD mutations at the same residues (D419) recur in follicular lymphoma.
- **Functional consequence:** **gain of function** — constitutive and/or IL-4-hypersensitive STAT6 activation.
- **Modifier genes:** none established. **Epigenetic changes / chromosomal abnormalities:** none reported; disease is a point-mutation disorder.

### 5. Environmental Information

No environmental toxin, occupational exposure, lifestyle factor, or infectious agent **causes** STAT6 GOF disease. Environmental allergens act as **triggers** for individual atopic manifestations. Recurrent infections (skin/respiratory/viral) reflect immune dysregulation intrinsic to the genotype rather than an environmental etiology.

### 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

```
Germline STAT6 DBD missense variant (e.g., D419H/N, E372K)
        │
        ▼
Constitutive / IL-4-hypersensitive STAT6 activation
  • sustained tyrosine phosphorylation (pSTAT6)
  • ligand-independent nuclear translocation (D419N, even unphosphorylated)
        │
        ▼
Increased STAT6 target-gene transcription (e.g., PARP14, GATA3 program)
        │
        ▼
Pathological TH2 skewing of CD4+ T cells (IL-4, IL-5, IL-13 ↑)
        │
        ├──► B-cell IgE class switching  → hyper-IgE, food allergy, anaphylaxis
        ├──► Eosinophil recruitment/survival → hypereosinophilia, eosinophilic GI disease
        ├──► Skin barrier/Th2 inflammation → treatment-resistant atopic dermatitis
        ├──► Airway Th2 inflammation → asthma
        └──► Chronic B-cell proliferation + PARP14 co-activation → follicular lymphoma risk
```

- **Molecular pathway:** IL-4/IL-13 → JAK1/JAK2/TYK2 → **STAT6** (KEGG JAK-STAT signaling; Reactome IL-4/IL-13 signaling). Upstream node = JAK kinases (JAK-inhibitor target); membrane receptor = IL-4Rα (dupilumab target).
- **Cellular processes:** TH2 differentiation, IgE class-switch recombination, eosinophilia, type-2 inflammation.
- **Protein dysfunction:** gain of function — enhanced DNA binding / nuclear retention of STAT6 (a transcription factor). Not misfolding or aggregation.
- **Immune involvement:** immune **dysregulation** (allergy axis) with partial immunodeficiency (recurrent infections).
- **Transcriptional co-activator:** **PARP14** amplifies the STAT6/TH2 program and connects to lymphomagenesis.
- **Suggested GO terms:** GO:0042092 (type 2 immune response), GO:0045064 (T-helper 2 cell differentiation), GO:0043330 (response to exogenous dsRNA — not applicable; use GO:0070670 response to IL-4), GO:0006357 (regulation of transcription by RNA Pol II), GO:0042113 (B-cell activation). **Suggested CL terms:** CL:0000546 (T-helper 2 cell), CL:0000236 (B cell), CL:0000771 (eosinophil), CL:0000097 (mast cell). **Subcellular:** GO:0005634 (nucleus) — the site of STAT6 dysfunction.

### 7. Anatomical Structures Affected

- **Primary organs / systems:** skin (UBERON:0002097), immune/hematopoietic system (UBERON:0002405), gastrointestinal tract—esophagus (UBERON:0001043), stomach, gut—and respiratory system/lung (UBERON:0002048).
- **Secondary:** skeletal system (short stature, osteoporosis); lymphoid tissue (lymphoma).
- **Tissues/cells:** epithelial (skin/GI/airway barrier), and immune cell populations — **TH2 cells (CL:0000546)**, **eosinophils (CL:0000771)**, **B cells/plasma cells (CL:0000236)**, mast cells.
- **Subcellular:** nucleus (transcription-factor dysfunction).
- **Lateralization:** systemic/**bilateral** (dermatitis, asthma); not lateralized.

### 8. Temporal Development

- **Onset:** congenital/**infantile (100%)**, insidious-to-chronic.
- **Progression:** chronic, lifelong; atopic dermatitis is persistent and treatment-resistant; anaphylaxis is **episodic**; lymphoma is a late, rare complication.
- **Course:** progressive multi-system atopy without treatment; **treatment-induced remission/control** achievable with dupilumab/JAK inhibitors.
- **Critical periods:** early childhood — window for diagnosis and initiation of targeted therapy to prevent morbidity.

### 9. Inheritance and Population

- **Inheritance:** **autosomal dominant**; ~70% sporadic/de novo (7/10 kindreds), ~30% inherited (3/10 kindreds) in the founding cohort.
- **Penetrance:** appears high but with **variable expressivity** (intra-familial heterogeneity documented).
- **Epidemiology:** **ultra-rare**; exact prevalence/incidence unknown (fewer than ~20 published families as of 2025). No founder effect, consanguinity role, or carrier-frequency data (dominant, de novo–enriched).
- **Demographics:** reported across three continents; no ethnic predilection established; no clear sex ratio.

### 10. Diagnostics

- **Laboratory:** markedly **elevated serum total IgE** (LOINC-mappable IgE assays), **peripheral hypereosinophilia** (CBC/differential), tissue eosinophilia on GI biopsy.
- **Biomarkers:** **STAT6 target-gene expression** and **pSTAT6** (functional readouts); TH2 cytokine skewing.
- **Genetic testing (definitive):** **whole-genome or whole-exome sequencing** is the recommended upfront approach for primary atopic disorders (*"Upfront genome-wide analysis by whole genome sequencing (WGS) will shorten the time to diagnosis"*, [PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)); targeted *STAT6* single-gene or PAD gene-panel testing is an alternative. **Functional confirmation** (sustained pSTAT6, enhanced nuclear translocation, luciferase/EMSA reporter assays, patient PBMC signaling) distinguishes GOF variants from VUS.
- **Histopathology:** eosinophilic infiltration of esophagus/GI tract; atopic dermatitis skin changes.
- **Differential diagnosis:** other primary atopic disorders / transcription-factor IEIs — **STAT3 loss-of-function (Job syndrome), FOXP3 deficiency (IPEX), T-bet deficiency, DOCK8 deficiency, Netherton syndrome** ([PMID: 37727514](https://pubmed.ncbi.nlm.nih.gov/37727514/)). STAT6 GOF is distinguished by the constitutive STAT6-activation signature and dupilumab responsiveness.
- **Screening:** cascade genetic testing of at-risk relatives in inherited kindreds.

### 11. Outcome/Prognosis

- **Survival/mortality:** no disease-specific mortality data; anaphylaxis and lymphoma are the principal life-threatening risks.
- **Morbidity:** high — severe dermatitis, dietary restriction, growth impairment, recurrent infections; substantial quality-of-life burden (no formal EQ-5D/SF-36 data).
- **Complications:** anaphylaxis, eosinophilic GI disease, recurrent infections, osteoporosis, and **B-cell/follicular lymphoma (~6%)**.
- **Prognostic factors:** the disease is highly **treatment-responsive**; early targeted therapy markedly improves outcomes. Lymphoma surveillance is warranted given the PARP14/STAT6 link.

### 12. Treatment

| Therapy | Class / target | Mechanism | Evidence | MAXO |
|---|---|---|---|---|
| **Dupilumab** | anti–IL-4Rα monoclonal antibody | Blocks IL-4/IL-13 receptor upstream of STAT6 | *"highly effective improving both clinical manifestations and immunological biomarkers"* ([PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/)); effective for D519N ([PMID: 40502541](https://pubmed.ncbi.nlm.nih.gov/40502541/)) | MAXO monoclonal-antibody therapy |
| **Ruxolitinib / JAK inhibitors** | JAK1/JAK2 inhibitor | Reduces pSTAT6 by blocking upstream kinases | *"ruxolitinib reduced pSTAT6 levels in D419H HEK293T cells and patient PBMC"* ([PMID: 37316763](https://pubmed.ncbi.nlm.nih.gov/37316763/)) | MAXO pharmacotherapy / targeted therapy |
| Supportive atopic care | Topical steroids, emollients, allergen avoidance, epinephrine | Symptom control | Standard atopy management | MAXO supportive care |
| **PARP14 inhibition** (experimental) | small-molecule co-activator inhibitor | Blocks downstream STAT6 co-activator; also anti-lymphoma | Preclinical ([PMID: 35851155](https://pubmed.ncbi.nlm.nih.gov/35851155/); [PMID: 28653395](https://pubmed.ncbi.nlm.nih.gov/28653395/)) | MAXO experimental therapy |

**Personalized medicine:** the disease is a paradigm of **genotype-guided precision therapy** — a druggable, hyperactive signaling axis directly matched to approved biologics (dupilumab) and JAK inhibitors. **Pharmacogenomics:** not specifically characterized. No gene/cell therapy is in clinical use.

### 13. Prevention

- **Primary prevention:** none (monogenic, largely de novo). **Genetic counseling** for inherited kindreds; prenatal/preimplantation genetic testing is theoretically possible for known familial variants.
- **Secondary prevention:** early genomic diagnosis and initiation of targeted therapy; allergen/anaphylaxis risk management.
- **Tertiary prevention:** dupilumab/JAK inhibitors to prevent complications; **lymphoma surveillance**; infection prophylaxis as needed.
- No immunization or population public-health intervention is applicable.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** *STAT6* is conserved; mouse *Stat6* (NCBI Gene 20852). No naturally occurring companion-animal/wildlife equivalent of germline STAT6 GOF disease is catalogued (no OMIA entry identified). **Comparative biology:** the IL-4/STAT6/TH2 axis is evolutionarily conserved, underpinning the validity of mouse models. No zoonotic relevance.

### 15. Model Organisms

| Model | Type | Genetic design | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| **Stat6VT** | Mouse (transgenic) | Constitutively active STAT6 in T cells | Spontaneous allergic skin inflammation + allergic airway disease; PARP14-dependent TH2 program | [PMID: 28653395](https://pubmed.ncbi.nlm.nih.gov/28653395/) |
| **STAT6 D419N knock-in** | Mouse (patient-variant knock-in) | Germline D419N | *"abnormal TH2-dominant immune response in vivo, with findings similar to those observed in patients"* | [PMID: 40603028](https://pubmed.ncbi.nlm.nih.gov/40603028/) |
| Patient cells / HEK293T | In vitro | Overexpressed variant STAT6 | pSTAT6 elevation, nuclear translocation, reporter activation; ruxolitinib response | [PMID: 37316763](https://pubmed.ncbi.nlm.nih.gov/37316763/), [PMID: 36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/) |
| Gastric organoids | In vitro (patient-derived) | E377K | Downstream effector-cytokine studies | [PMID: 36216080](https://pubmed.ncbi.nlm.nih.gov/36216080/) |

**Applications:** mechanism of TH2 skewing, allergic skin/airway disease, target validation for dupilumab/JAK/PARP14. **Limitations:** mouse models capture allergic dermatitis and TH2 skewing but do not fully model the human lymphoma continuum or the complete multi-system phenotype.

---

## Mechanistic Model / Interpretation

STAT6 GOF disease is best understood as a **"single-node type-2 immune amplifier" disorder**. A germline missense change in the STAT6 DNA-binding domain converts a normally ligand-controlled transcription factor into a **hyperactive or constitutively active driver of the TH2 gene program**. The location of the mutations is mechanistically decisive: the DBD hotspot (D419) either stabilizes STAT6 in a DNA-bound/nuclear-retained state or lowers the activation threshold for IL-4 signaling. This produces the entire downstream cascade of type-2 immunity—IgE class switching, eosinophilia, and barrier-tissue inflammation—explaining why one gene defect yields such a broad, coherent, multi-organ atopic phenotype.

Three lines of evidence converge on gain-of-function rather than haploinsufficiency: (1) the **dominant inheritance with recurrent, clustered missense variants**; (2) **gnomAD constraint** showing LoF tolerance but strong missense intolerance (mis_z = 3.47); and (3) **direct functional assays** showing sustained/ligand-independent STAT6 activation. The mouse models close the causal loop: constitutively active STAT6 alone is sufficient to produce spontaneous allergic skin and airway disease.

The disease also illuminates a **shared germline–somatic axis**. The identical DBD residues mutated germline in this atopic disorder are recurrently mutated somatically in follicular lymphoma, and **PARP14** functions as a common downstream co-activator in both settings. This explains the small but real lymphoma risk and nominates PARP14 as a mechanistic bridge and therapeutic target spanning allergy and oncology.

Clinically, the model is directly **actionable**: blocking the axis at the receptor (dupilumab/IL-4Rα) or upstream kinase (JAK inhibitor) reverses both symptoms and biomarkers, making STAT6 GOF disease a textbook example of precision medicine in inborn errors of immunity.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [36884218](https://pubmed.ncbi.nlm.nih.gov/36884218/) | *Human germline heterozygous GOF STAT6 variants cause severe allergic disease* | **Defining cohort (n=16)**: GOF mechanism, AD inheritance, core phenotype, dupilumab efficacy |
| [36216080](https://pubmed.ncbi.nlm.nih.gov/36216080/) | *A germline STAT6 GOF variant is associated with early-onset allergies* | E377K DBD variant; spontaneous STAT6 activation; gastric organoids; variable expressivity |
| [36758835](https://pubmed.ncbi.nlm.nih.gov/36758835/) | *Severe allergic dysregulation due to a GOF mutation in STAT6* | E372K DBD variant |
| [37316763](https://pubmed.ncbi.nlm.nih.gov/37316763/) | *Autosomal dominant STAT6 GOF causes severe atopy associated with lymphoma* | D419H variant; ruxolitinib reduces pSTAT6; follicular lymphoma link |
| [40603028](https://pubmed.ncbi.nlm.nih.gov/40603028/) | *Mechanism of pathogenesis by a GOF STAT6 variant* | D419N: ligand-independent nuclear translocation; knock-in mouse recapitulation |
| [40502541](https://pubmed.ncbi.nlm.nih.gov/40502541/) | *STAT6 GOF: p.D519N responds to dupilumab* | New variant; expands phenotype; dupilumab response |
| [38238227](https://pubmed.ncbi.nlm.nih.gov/38238227/) | *Human germline GOF STAT6: from allergy to lymphoma* | Review; allergy-to-lymphoma spectrum; targeted-treatment overview |
| [37727514](https://pubmed.ncbi.nlm.nih.gov/37727514/) | *Transcription factor defects in IEIs with atopy* | Places STAT6 GOF among TF-defect atopic IEIs; differential diagnosis |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | *Rapid identification of PAD by upfront genomic sequencing* | Diagnostic strategy: upfront WGS for primary atopic disorders |
| [28653395](https://pubmed.ncbi.nlm.nih.gov/28653395/) | *PARP14 limits severity of allergic skin disease* | Stat6VT mouse; PARP14 as STAT6 co-activator in TH2/allergic disease |
| [35851155](https://pubmed.ncbi.nlm.nih.gov/35851155/) | *PARP14 is a novel target in STAT6 mutant follicular lymphoma* | PARP14 druggability; germline–somatic mechanistic bridge |

All eleven papers are mutually consistent; none challenge the core GOF model. Evidence spans human clinical/genetic cohorts, in vitro functional assays, and two mouse models, providing multi-modal validation.

---

## Limitations and Knowledge Gaps

1. **Very small sample size.** Fewer than ~20 families are published; frequencies (e.g., lymphoma 6%) derive from n=16 and carry wide confidence intervals. True prevalence/incidence is unknown.
2. **No dedicated Orphanet/ICD code**, complicating registry-based epidemiology.
3. **Penetrance and expressivity** are incompletely quantified; intra-familial heterogeneity is described but not modeled.
4. **Long-term outcomes** (life expectancy, lymphoma lifetime risk, treatment durability) are unknown given the disease's recency.
5. **Genotype–phenotype correlations** (e.g., whether specific DBD residues predict lymphoma vs pure atopy) are not yet resolved.
6. **No formal QoL instruments, pharmacogenomics, or gene/cell-therapy data.**
7. **PARP14 inhibition** remains preclinical for this indication.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international STAT6-GOF registry** to refine prevalence, penetrance, lymphoma risk, and natural history.
2. **Systematic genotype–phenotype mapping** across all reported variants (D419 hotspot vs others) to test whether specific residues predict lymphoma risk or dupilumab responsiveness.
3. **Prospective dupilumab and JAK-inhibitor trials** with standardized clinical and biomarker (pSTAT6, IgE, eosinophil) endpoints and QoL instruments (EQ-5D, PROMIS).
4. **Lymphoma surveillance protocol** development, leveraging the shared germline–somatic DBD/PARP14 axis.
5. **PARP14 inhibitor preclinical testing** in the D419N knock-in mouse for both allergic and lymphoma endpoints.
6. **Deep functional characterization** of each variant (constitutive vs ligand-hypersensitive) to guide therapy selection (receptor blockade vs kinase inhibition).
7. **Assign a dedicated Orphanet/ICD-11 code** and complete HPO annotation for downstream variants.


## Artifacts

- [OpenScientist final report](STAT6_Gain_of_Function_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](STAT6_Gain_of_Function_Disease-deep-research-openscientist_artifacts/final_report.pdf)