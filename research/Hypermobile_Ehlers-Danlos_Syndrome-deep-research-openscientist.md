---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-01T23:18:52.384405'
end_time: '2026-08-01T23:36:46.879410'
duration_seconds: 1074.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypermobile Ehlers-Danlos Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypermobile_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypermobile_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypermobile Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypermobile Ehlers-Danlos Syndrome** covering all of the
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

# Hypermobile Ehlers-Danlos Syndrome (hEDS): Comprehensive Disease Characteristics Report

*Autonomous literature-based discovery report. Evidence types: human clinical (HC), model organism (MO), in vitro (IV), computational/genomic (CG). PMIDs cited throughout.*

---

## Summary (Answer to the Research Question)

Hypermobile Ehlers-Danlos syndrome (hEDS) is the most common subtype of the Ehlers-Danlos syndromes—a group of heritable connective-tissue disorders—defined clinically by generalized joint hypermobility, joint instability/recurrent dislocations, chronic musculoskeletal pain, mild skin involvement, and a broad multisystem comorbidity profile (autonomic dysfunction/POTS, mast cell activation, gastrointestinal/gut–brain disorders, fatigue, and psychiatric conditions). It is inherited in an autosomal dominant pattern and, uniquely among the 13 EDS subtypes, has **no confirmed causal gene**; diagnosis rests on the **2017 International Classification clinical criteria** (Malfait et al., PMID 28306229). Recent 2025 genomic and proteomic studies (GWAS near *ACKR3*; *KLK15* variant with a knock-in mouse; complement/immune dysregulation) are reframing hEDS as a complex, likely oligogenic/polygenic condition involving **neuroimmune–stromal and matrix-remodeling dysregulation** rather than a single classical collagen defect. Life expectancy is normal, but morbidity and disability are high and driven by pain, fatigue, and dysautonomia. Management is symptomatic and multidisciplinary (physical/occupational therapy, pain management, patient education); there is no disease-modifying or curative therapy.

---

## 1. Disease Information

**Overview.** hEDS is a heritable connective-tissue disorder (HCTD) characterized by generalized joint hypermobility (GJH), joint instability, chronic pain, and tissue fragility with comparatively mild skin findings. It is the most common symptomatic joint-hypermobility condition in clinical practice (PMID 33856167, HC). The 2017 classification replaced the older terms "EDS hypermobility type" and "joint hypermobility syndrome (JHS)," and introduced **hypermobility spectrum disorders (HSD)** for symptomatic patients not meeting full hEDS criteria (PMID 33856167).

**Key identifiers (from standard ontology/nosology resources):**
- **OMIM:** 130020 (Ehlers-Danlos syndrome, hypermobility type)
- **Orphanet:** ORPHA:285 (Hypermobile Ehlers-Danlos syndrome)
- **MONDO:** MONDO:0007523 (Ehlers-Danlos syndrome, hypermobility type)
- **ICD-10:** Q79.6 (Ehlers-Danlos syndrome); **ICD-11:** LD28.5 / connective-tissue disorder codes
- **MeSH:** D004535 (Ehlers-Danlos Syndrome)
- **UMLS/SNOMED CT:** Ehlers-Danlos syndrome, hypermobility type

**Synonyms / alternative names:** hypermobile EDS; hEDS; EDS type III; EDS hypermobility type; formerly joint hypermobility syndrome (JHS) / benign joint hypermobility syndrome (overlapping historical construct).

**Data source type.** Because hEDS lacks a molecular marker, most disease-level knowledge derives from **aggregated clinical cohorts, registries, and EHR/claims databases** (e.g., Wales national e-cohort PMID 31685485; US PearlDiver claims PMID 39465806) plus expert-consensus nosology (PMID 28306229). *(HC/CG)*

---

## 2. Etiology

**Primary cause: genetic, but gene(s) unidentified.** Of the 13 EDS subtypes in the 2017 classification, **12 have a recognized causal gene; hEDS does not** (Malfait 2017, PMID 28306229; Riley 2020, PMID 31904772, HC). Quote: *"hypermobile EDS (hEDS) currently has no identifiable associated gene"* (PMID 31904772). Inheritance is **autosomal dominant** (PMID 33856167).

**Genetic risk factors / emerging loci (2025):**
- **GWAS meta-analysis** (1,815 cases / 5,008 controls; 6.2M variants): two genome-wide significant loci, including a **regulatory region near *ACKR3* (atypical chemokine receptor 3)**—first evidence of common-variant contribution; supports a *"complex, multisystem model involving neuroimmune-stromal dysregulation"* (PMID 41001447, CG).
- ***KLK15*** (kallikrein-15): recurrent missense **p.Gly226Asp** from WES of 200 patients, segregating in families; dominant-negative effect on ECM compartmentalization with lysyl oxidase (LOX) (PMID 40949095, CG/MO).
- **Complement/immune genes and proteins**: serum proteomics showing complement-cascade dysregulation (PMID 40972649, HC/IV).
- **Modifier / overlapping genes**: ***TNXB*** (tenascin-X) haploinsufficiency produces a mild hypermobility phenotype (CAH-X) and complete deficiency causes classical-like EDS (PMID 37007968, 35476220).

**Environmental / non-genetic risk & modifiers:**
- **Sex/hormones:** strong female predominance (~90–95% of clinical cohorts; 70% in population EHR data, PMID 31685485). Females report symptom worsening at hormonal transitions (puberty, menstrual cycle, pregnancy) and some improvement post-menopause (PMID 41637690, HC).
- **Family history** is a formal diagnostic feature (Feature B, PMID 28306229).
- No established infectious or toxic cause. No confirmed protective variants/factors. Regular graded exercise/physiotherapy is broadly beneficial (tertiary, PMID 28306230).

**Gene–environment interactions.** Hypothesized hormone × connective-tissue-gene interactions underlie female predominance and cyclic symptom variation, but no validated GxE mechanism is established (data limited; PMID 41637690). *(HC)*

---

## 3. Phenotypes (with HPO terms, frequencies, characteristics)

| Phenotype | HPO term | Type | Onset | Frequency / notes |
|---|---|---|---|---|
| Generalized joint hypermobility | HP:0001382 | Physical sign | Childhood | Required for diagnosis (100% by criteria) |
| Recurrent joint dislocations/subluxations | HP:0001373 / HP:0033729 | Sign | Childhood–adolescence | Very common |
| Chronic musculoskeletal pain / arthralgia | HP:0002829, HP:0003422 | Symptom | Pain onset ~10 yr, chronic by ~20 yr (PMID 31075184) | ~97% severe chronic pain (PMID 31075184) |
| Soft/hyperextensible skin | HP:0000974, HP:0000957 | Sign | Congenital | Common, milder than classical EDS |
| Atrophic scars / striae | HP:0000993 / HP:0001065 (piezogenic papules) | Sign | Childhood+ | Feature A criteria |
| Recurrent hernias | HP:0100790 | Sign | Variable | Feature A |
| Mitral valve prolapse | HP:0001634 | Sign | Variable | Included in criteria; significant cardiac abnormality rare (PMID 36866504) |
| Aortic root dilatation | HP:0002616 | Sign | Variable | Usually mild/non-progressive (PMID 36866504) |
| Fatigue | HP:0012378 | Symptom | Adolescence+ | Major QoL driver (PMID 30703284) |
| Orthostatic intolerance / POTS | HP:0031013 / HP:0012432 | Sign | Adolescence–young adult | 51–79% in cohorts (PMID 42399338, 42229474) |
| Functional GI / IBS | HP:0002020 (GERD), HP:0002574 (IBS-like) | Symptom | Childhood+ | Digestive disorders 54.6% (PMID 39465806) |
| Anxiety / depression | HP:0000739 / HP:0000716 | Behavioral | Adolescence+ | Highly prevalent (PMID 40293579, 33856167) |
| ADHD / autistic traits | HP:0007018 | Behavioral | Childhood | Over-represented (PMID 33603376) |
| Small-fiber neuropathy (paresthesia) | HP:0003401 | Sign/lab | Young adult | Skin-biopsy nerve-fiber loss (PMID 42399338) |
| Pelvic floor / bladder dysfunction | HP:0000020 | Sign | Adult | Common in females (PMID 41512700, 42311207) |
| Temporomandibular disorder | HP:0030766 (jaw pain) | Sign | Adult | up to 98% of women (PMID 38661350) |

**Characteristics.** Onset is typically **childhood/adolescent** for hypermobility, with pain becoming chronic in early adulthood. Severity is **variable**; course is **chronic, fluctuating/progressive** (75% report gradually increasing pain, PMID 31075184). **Quality of life** is substantially reduced; **fatigue and pain are the strongest predictors of reduced PedsQL scores**, and psychiatric comorbidity further lowers QoL (PMID 30703284, HC).

---

## 4. Genetic / Molecular Information

- **Causal genes:** **None confirmed** for idiopathic hEDS (PMID 28306229, 31904772). This is the defining molecular feature.
- **Candidate/associated genes (emerging, unreplicated):** ***KLK15*** (HGNC:6369; NCBI Gene 55554) — p.Gly226Asp missense, proposed dominant-negative (PMID 40949095); ***ACKR3***/CXCR7 (HGNC:23692) regulatory locus (GWAS, PMID 41001447); complement genes *C1QA, C3, C8A, C8B, C9* (proteomic, PMID 40972649).
- **Overlapping/differential genes (define related, non-hEDS subtypes):** ***TNXB*** (HGNC:11976; Gene 7148) — clEDS/CAH-X; collagen genes *COL1A1, COL1A2, COL3A1, COL5A1, COL5A2* and *TGFB2/3, TGFBR1/2, SMAD3, FBN1* are tested to **exclude** other HCTDs (PMID 40653826, 28306229).
- **Variant classification/type:** For candidate genes, variants are rare/low-frequency missense (e.g., *KLK15* p.Gly226Asp) and currently **VUS** under ACMG/AMP pending replication. No recurrent pathogenic variant is established. Allele frequencies of candidates are low in gnomAD.
- **Origin:** Germline (heritable, AD). No somatic component.
- **Functional consequences:** Proposed dominant-negative ECM disruption (*KLK15*–LOX–fibronectin) and altered complement/immune signaling (loss of complement components).
- **Modifier genes:** *TNXB* haploinsufficiency modifies hypermobility phenotype (PMID 35476220). Hereditary alpha-tryptasemia (*TPSAB1* copy number) associates with hEDS/POTS/MCAS (PMID 39527936).
- **Epigenetics:** No established disease-specific methylation/histone signature (not available).
- **Chromosomal abnormalities:** None characteristic; *CYP21A2→TNXB* contiguous deletion produces CAH-X chimera (PMID 35476220).

---

## 5. Environmental Information

- **Environmental factors/toxins:** None causally established. hEDS is fundamentally genetic.
- **Lifestyle factors:** Physical deconditioning and fear-avoidance worsen disability; graded exercise is protective/therapeutic (PMID 41637690, 28306230). Hormonal status modulates symptoms in females.
- **Infectious agents:** None; hEDS is not infectious. (Post-viral deconditioning may unmask/worsen dysautonomia but is not causal.)

---

## 6. Mechanism / Pathophysiology

**Overall model (2025 synthesis):** hEDS is increasingly viewed as a **neuroimmune–stromal / matrix-remodeling disorder** rather than a pure structural collagen defect (PMID 41001447, 40949095, 40972649).

**Causal chain (proposed):**
1. **Upstream (genetic/molecular):** heritable variants affecting ECM regulation (*KLK15*–LOX–fibronectin cross-linking; PMID 40949095) and immune/complement signaling (*ACKR3* chemokine axis, complement components; PMID 41001447, 40972649).
2. **Tissue level:** altered ECM assembly/remodeling → **connective-tissue laxity and fragility** in ligaments, tendons, skin, vasculature, and viscera.
3. **Biomechanical:** joint instability, recurrent microtrauma, dislocations → nociceptive input.
4. **Neurological amplification:** **central sensitization** (lowered thermal pain thresholds, increased wind-up ratio; PMID 26919608) and **peripheral small-fiber neuropathy** (intraepidermal nerve-fiber loss; PMID 42399338) → chronic widespread/neuropathic pain.
5. **Autonomic/immune (downstream):** connective-tissue laxity → venous pooling/reduced preload → **POTS**; **mast cell activation** and complement dysregulation → immune/inflammatory and GI (gut–brain) manifestations (PMID 42229474, 40972649).

**Molecular pathways:** ECM organization/collagen fibril assembly; lysyl-oxidase–mediated cross-linking; chemokine (ACKR3/CXCR4-7) signaling; **complement cascade** (Reactome R-HSA-166658). **Cellular processes:** ECM remodeling, inflammation, mast cell degranulation, neuronal sensitization. **Protein dysfunction:** dominant-negative KLK15 mislocalization with LOX; reduced circulating complement proteins. **Immune involvement:** complement dysregulation + profibrotic cytokines (PMID 40972649); MCAS clustering (PMID 42229474).

**Molecular profiling available:** Proteomics (serum, PMID 40972649); GWAS/TWAS/eQTL (PMID 41001447); WES (PMID 40949095). Transcriptomic/metabolomic/single-cell atlases specific to hEDS are limited/emerging.

**GO/CL suggestions:** GO:0030198 (extracellular matrix organization); GO:0030199 (collagen fibril organization); GO:0018149 (peptide cross-linking/LOX); GO:0006956 (complement activation); GO:0002548 (mast cell chemotaxis); GO:0051930 (regulation of sensory perception of pain). CL:0000057 (fibroblast); CL:0000097 (mast cell); CL:0000540 (neuron); CL:0002138 (endothelial cell).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **Musculoskeletal** (joints, ligaments, tendons — primary); **skin** (integumentary); **cardiovascular** (mitral valve, aortic root, autonomic vasoregulation); **digestive/gut–brain**; **nervous/autonomic**; **genitourinary/pelvic floor**; **immune** (mast cells). Secondary: TMJ, dental.
- **Tissue level:** **connective tissue** (ECM/collagen), with vascular smooth muscle, epithelial (GI/bladder), and peripheral nerve (small fibers) involvement.
- **Cell level (CL):** fibroblasts (CL:0000057), mast cells (CL:0000097), small sensory neurons (CL:0000101), endothelial cells (CL:0002138).
- **Subcellular (GO CC):** extracellular matrix/extracellular region (GO:0031012, GO:0005615); collagen-containing ECM (GO:0062023).
- **Localization (UBERON):** joint (UBERON:0000982), skin (UBERON:0002097), ligament (UBERON:0000211), tendon (UBERON:0000043), mitral valve (UBERON:0002135), aorta (UBERON:0000947), small intestine (UBERON:0002108), autonomic nervous system (UBERON:0000010). Involvement is typically **bilateral/generalized**.

---

## 8. Temporal Development

- **Onset:** Joint hypermobility often **congenital/childhood**; pain onset ~10 years, becoming chronic ~20 years (PMID 31075184). Insidious/chronic pattern.
- **Progression:** **Chronic, lifelong**; variable rate. Pain frequently progressive (75%, PMID 31075184); comorbidities (POTS, GI, fatigue) typically accrue through adolescence/young adulthood. Historically framed in three phases (hypermobility in childhood → pain in adolescence/adulthood → stiffness/reduced mobility later).
- **Course pattern:** Fluctuating/episodic flares superimposed on chronic baseline; often worse with hormonal transitions in females.
- **Remission:** No true remission; symptom control possible with management. Some females report improvement after menopause (PMID 41637690).
- **Critical periods:** Puberty, pregnancy/postpartum, and menstrual cycle are windows of symptom exacerbation and intervention opportunity (PMID 41637690, 38748660).

---

## 9. Inheritance and Population

- **Prevalence:** Diagnosed EDS/JHS combined **194.2 per 100,000 (~1 in 500)** in Wales (2016/17; PMID 31685485). Physical-activity review cites **~1 in 500** for HSD/hEDS (PMID 41637690). Incidence not well quantified.
- **Inheritance:** **Autosomal dominant** (PMID 33856167). **Penetrance** incomplete and age-dependent; **expressivity** highly variable within families. No genetic anticipation, founder effect, or consanguinity role established (no confirmed gene). **Carrier frequency** not applicable (dominant; gene unknown).
- **Demographics:** **Strong female predominance** (~90–95% clinical, 70% EHR; PMID 31685485). Mean diagnosis **8.5 years later in women** (PMID 31685485). Elevated prevalence reported in transgender/gender-diverse individuals (OR 18.45; PMID 40986523). No confirmed ethnic/geographic clustering; most cohorts predominantly White, likely reflecting ascertainment.
- **Sex ratio:** ~F:M 3:1 (EHR) to ~9:1 (specialty clinics).

---

## 10. Diagnostics

- **Clinical criteria (gold standard):** **2017 International Classification** — three mandatory criteria: (1) **GJH** by Beighton score (≥6 prepubertal, ≥5 pubertal–age 50, ≥4 over 50); (2) **≥2 of** Feature A (systemic connective-tissue signs), Feature B (family history), Feature C (musculoskeletal complications: chronic pain ≥3 months, recurrent dislocations); (3) **exclusion** of other HCTDs (PMID 28306229). Pediatric framework uses **Beighton ≥6/9** and four components (PMID 37143135). Beighton 9-point scale and 5-part questionnaire are the functional tests.
- **No diagnostic lab test or biomarker** currently exists. Emerging candidate biomarkers: serum complement proteins (C1QA, C3, C8A/B, C9) and cytokines (research-only; PMID 40972649).
- **Genetic testing:** Used to **exclude** other EDS/HCTDs, not to confirm hEDS. Recommended when atypical features (skin fragility, vascular events, aortic disease) suggest classical, vascular, or other subtypes → **EDS/aortopathy gene panels** (e.g., *COL1A1/2, COL3A1, COL5A1/2, TNXB, FBN1, TGFBR1/2, SMAD3*), **WES/WGS** for research (PMID 40653826). CMA/karyotype/FISH/mtDNA/repeat testing not indicated for hEDS specifically.
- **Imaging/functional adjuncts:** Echocardiography (baseline MVP/aortic root; PMID 36866504); tilt-table/active stand for POTS; skin biopsy (intraepidermal nerve-fiber density) for small-fiber neuropathy (PMID 42399338); CT/CTA/MRA for abdominal compression syndromes (MALS, May–Thurner; PMID 40653826).
- **Differential diagnosis:** Classical EDS, vascular EDS, Marfan syndrome, Loeys–Dietz, other HCTDs, HSD, fibromyalgia, generalized hypermobility spectrum (PMID 28306229, 33856167).
- **Screening:** No newborn/carrier screening (gene unknown). **Cascade clinical evaluation** of at-risk relatives is used.

---

## 11. Outcome / Prognosis

- **Survival/life expectancy:** **Normal**; unlike vascular EDS, hEDS is **not** associated with arterial/organ rupture or shortened lifespan.
- **Morbidity/disability:** **High.** Disability across all six WHO life domains (PMID 42298945); 58% report symptoms not well-managed (PMID 42298945). Chronic pain, fatigue, dysautonomia, and psychiatric burden dominate. Daily mental-health burden ~61% in an orthopaedic survey (PMID 40638721).
- **QoL measures:** PedsQL, SF-36, EQ-5D, PROMIS; **fatigue and pain are strongest QoL predictors** (PMID 30703284).
- **Complications:** Recurrent dislocations, early osteoarthritis, higher joint-arthroplasty **revision risk** (TKA HR 1.50; THA HR 2.32; PMID 38936437); complex regional pain syndrome (~11-fold higher; PMID 42398975); abdominal compression syndromes (MALS; PMID 40653826); pelvic organ prolapse (>2-fold; PMID 41512700); pregnancy complications.
- **Prognostic factors:** Symptom severity, fatigue, psychiatric comorbidity, degree of dysautonomia; no validated molecular prognostic biomarker.

---

## 12. Treatment (with MAXO terms)

**No disease-modifying or curative therapy exists.** Care is **symptomatic and multidisciplinary** (PMID 33856167, 31904772).

- **Rehabilitation (cornerstone):** Physical therapy (MAXO:0000004), occupational therapy (MAXO:0000058), graded exercise/strengthening/proprioception, bracing/orthoses; ICF framework (PMID 28306230). Hippotherapy shown beneficial in a case (PMID 39542503). Evidence base limited; RCTs needed.
- **Pain management (MAXO:0001152):** Multimodal—physiotherapy, analgesics/NSAIDs, neuropathic agents (given central sensitization/SFN; PMID 26919608, 42399338), interventional (e.g., intercostal nerve RFA for slipping rib; PMID 41618773); opioids generally avoided.
- **Pharmacotherapy for comorbidities:** POTS—fluids/salt, compression, beta-blockers, ivabradine, midodrine, fludrocortisone; MCAS—H1/H2 antihistamines, mast-cell stabilizers; GI/DGBI—neuromodulators, dietary measures (AGA 2025 Update, PMID 40387691). Psychiatric—SSRIs/therapy (note cardiac-electrophysiology considerations, PMID 42242906).
- **Surgical/interventional (MAXO:0000424):** Joint stabilization when indicated—**but higher failure/revision rates** (PMID 38936437, 40638721); vascular decompression for MALS/May–Thurner (PMID 40653826). Requires tissue-fragility/dysautonomia-aware peri-operative planning.
- **Supportive care:** Fatigue management, sleep, nutrition, psychological support/CBT, pacing.
- **Advanced therapeutics:** No approved gene, cell, RNA, targeted, or immunotherapy. No hEDS-specific pharmacogenomics established.
- **Experimental:** No definitive disease-modifying trials; management guidelines evolving (pregnancy guidelines PMID 38748660).

---

## 13. Prevention

- **Primary prevention:** Not possible (genetic, AD). 
- **Secondary prevention:** Early clinical recognition and multidisciplinary referral; baseline echocardiography; screening for POTS/MCAS/GI comorbidities (PMID 40387691); risk stratification of at-risk relatives.
- **Tertiary prevention (main lever):** Joint protection, graded exercise/physiotherapy to prevent injury and deconditioning, injury-avoidance education, peri-operative precautions, pregnancy planning (PMID 28306230, 38748660).
- **Genetic counseling:** Autosomal dominant with **50% recurrence risk** per pregnancy; counseling emphasizes variable expressivity/incomplete penetrance and absence of a confirmatory genetic test (PMID 33856167, 39924336). No carrier/prenatal/PGT test available (gene unknown).
- **Public-health/behavioral:** Clinician education to reduce diagnostic delay (notably in women, PMID 31685485); no immunization or environmental measures applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Studied primarily in *Homo sapiens* (NCBI:txid9606) and *Mus musculus* (NCBI:txid10090).
- **Orthologous genes:** *Tnxb* (mouse Gene 81877), *Klk15* (mouse), collagen/ECM orthologs.
- **Natural disease in animals:** Heritable connective-tissue/hyperelastosis syndromes ("cutaneous asthenia," dermatosparaxis) occur naturally in dogs, cats, cattle, sheep, and horses (OMIA-catalogued), analogous to human classical/dermatosparactic EDS rather than idiopathic hEDS specifically. No natural animal analog of idiopathic hEDS is confirmed.
- **Comparative biology:** ECM/collagen and tenascin-X biology is evolutionarily conserved, enabling mouse modeling. **No zoonotic potential** (non-infectious, genetic).

---

## 15. Model Organisms

- **Mouse (primary):**
  - ***Klk15* p.Gly226Asp knock-in mouse** — **first mouse model developed specifically for hEDS**; recapitulates **tendon and cardiac-valve abnormalities** and **dysregulated cytokine profiles**, supporting a matrix-remodeling + immune mechanism (PMID 40949095, MO). *Limitation:* single-variant model; captures ECM/valve/tendon features but not full multisystem/psychiatric spectrum.
  - ***Tnxb−/−* (tenascin-X-deficient) mouse** — established model of a hypermobility-type/classical-like EDS connective-tissue disorder; reproduces **skin/connective-tissue fragility, mechanical hyperalgesia, and pain** phenotypes (PMID 37007968, MO). *Limitation:* models TNX-deficiency (clEDS/CAH-X), not idiopathic hEDS.
- **Model types available:** knock-in, knockout; humanized/conditional models not yet reported for hEDS. iPSC/fibroblast and organoid systems are emerging for ECM studies.
- **Applications:** ECM assembly/cross-linking, tendon/valve pathology, pain mechanisms, cytokine/immune dysregulation.
- **Resources:** MGI (*Tnxb*, *Klk15*), IMPC, IMSR.

---

## Supported Hypotheses (all evidence-backed)

| ID | Statement | Status | Key evidence (PMID) |
|---|---|---|---|
| H001 | hEDS is the only EDS subtype without an identified causal gene; clinical diagnosis, AD | Supported | 28306229, 31904772, 33856167 |
| H002 | Immune/complement + matrix-remodeling dysregulation (ACKR3, KLK15, complement) beyond collagen | Supported | 41001447, 40949095, 40972649 |
| H003 | Multisystem disorder; high GI/CV/POTS/MCAS/psychiatric burden; female predominance | Supported | 39465806, 33856167 |
| H004 | Chronic pain driven by central sensitization (not nerve damage) | Supported | 26919608, 31075184 |
| H005 | Diagnosed prevalence ~194/100,000; female predominance; delayed diagnosis in women | Supported | 31685485 |
| H006 | TNXB defines a hypermobility CT disorder with a validated mouse model | Supported | 37007968, 35476220 |
| H007 | Fatigue and pain (not hypermobility per se) are strongest QoL/disability determinants | Supported | 30703284 |
| H008 | POTS + small-fiber neuropathy + MCAS + gut–brain disorders form a comorbidity triad | Supported | 42399338, 42229474, 41952073 |

---

## Limitations and Future Directions

**Limitations.** (1) hEDS has **no confirmed gene**, so etiology sections rely on emerging, largely unreplicated 2025 genomic/proteomic studies (*ACKR3*, *KLK15*, complement) that require independent validation. (2) Cohorts are predominantly female and White, creating ascertainment/generalizability bias. (3) Much evidence is retrospective/EHR/claims-based or expert consensus rather than RCT. (4) Diagnostic criteria evolve, complicating cross-study comparison (pre/post-2017). (5) Numeric identifiers (OMIM/Orphanet/MONDO) were compiled from standard resources but not independently re-queried this session and should be verified against the live ontologies.

**Future directions.** Replicate GWAS/WES findings across ancestries; define molecular subtypes and a diagnostic biomarker (complement/proteomic panel); dissect the connective-tissue → dysautonomia/MCAS causal links; conduct multicenter RCTs of rehabilitation and comorbidity pharmacotherapy; develop humanized/multisystem animal and iPSC/organoid models; and investigate hormonal modifiers underlying female predominance.

*Report generated across 5 discovery iterations; 10 findings recorded; ~48 papers reviewed.*


## Artifacts

- [OpenScientist final report](Hypermobile_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypermobile_Ehlers-Danlos_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)