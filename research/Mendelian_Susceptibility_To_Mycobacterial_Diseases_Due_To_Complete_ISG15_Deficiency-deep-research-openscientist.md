---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-23T14:56:45.658646'
end_time: '2026-09-23T15:29:15.856865'
duration_seconds: 1950.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mendelian Susceptibility To Mycobacterial Diseases Due To Complete
    ISG15 Deficiency
  mondo_id: MONDO:0014502
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_ISG15_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_ISG15_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mendelian Susceptibility To Mycobacterial Diseases Due To Complete ISG15 Deficiency
- **MONDO ID:** MONDO:0014502 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mendelian Susceptibility To Mycobacterial Diseases Due To Complete ISG15 Deficiency** covering all of the
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

# Mendelian Susceptibility to Mycobacterial Disease due to Complete ISG15 Deficiency
### Comprehensive Disease Characterization Report

**Disease:** Complete ISG15 Deficiency (Immunodeficiency 38 with basal ganglia calcification)
**MONDO:** MONDO:0014502 | **OMIM (disease):** #616126 (IMD38) | **OMIM (gene):** *147571
**Orphanet:** ORPHA:319563 | **Category:** Mendelian, autosomal recessive inborn error of immunity

---

## Summary (Answer to the Research Question)

Complete ISG15 deficiency is a rare **autosomal recessive inborn error of immunity** caused by biallelic loss-of-function variants in **ISG15** (interferon-stimulated gene 15; a ubiquitin-like modifier). It is a **mixed syndrome** that uniquely combines two mechanistically opposite immune defects: (1) **Mendelian Susceptibility to Mycobacterial Disease (MSMD)** — recurrent infection by low-virulence mycobacteria (BCG vaccine strain, environmental mycobacteria) caused by loss of **secreted ISG15**, which is a non-redundant inducer of **IFN-γ** from NK and T lymphocytes; and (2) a **type I interferonopathy** — because **intracellular ISG15 is required to stabilize USP18**, the principal negative regulator of type I IFN (IFN-α/β) signaling. Loss of intracellular ISG15 → USP18 degradation → uncontrolled amplification of IFN-α/β responses → **basal ganglia/intracranial calcification, autoinflammation, and necrotizing/fibrotic skin lesions**. Notably, human ISGylation is largely **redundant for antiviral defense** (patients are not unusually susceptible to viruses), which distinguishes human from mouse biology. Management splits along the two mechanisms: **anti-mycobacterial therapy** for infection and **JAK1/2 inhibition** (baricitinib, ruxolitinib) for the interferonopathy.

**Key primary references:** Bogunovic et al., *Science* 2012 (PMID 22859821); Zhang et al., *Nature* 2015 (PMID 25307056); Martin-Fernandez et al. 2020 (PMID 32402279); Sazeides et al. 2026 (PMID 41743834).

---

## 1. Disease Information

- **Overview:** An autosomal recessive primary immunodeficiency / inborn error of immunity in which complete absence of the ISG15 protein produces a combined phenotype of susceptibility to weakly virulent mycobacteria and a monogenic type I interferonopathy with intracranial calcification and inflammatory skin disease.
- **Key identifiers:**
  - **MONDO:** MONDO:0014502
  - **OMIM disease:** #616126 "Immunodeficiency 38 with basal ganglia calcification; IMD38"
  - **OMIM gene (ISG15):** *147571
  - **Orphanet:** ORPHA:319563 ("Immunodeficiency due to ISG15 deficiency")
  - **HGNC:** HGNC:4053 (ISG15) | **NCBI Gene:** 9636 | **Ensembl:** ENSG00000187608 | **UniProt:** P05161
  - **ICD-10:** D84.8 (other specified immunodeficiencies); **ICD-11:** 4A00.x (primary immunodeficiencies); basal ganglia calcification coded separately.
  - **MeSH:** related terms — "Immunologic Deficiency Syndromes"; "Interferon-Stimulated Gene 15"; "Ubiquitins."
- **Synonyms / alternative names:** Complete ISG15 deficiency; ISG15 deficiency; Immunodeficiency 38 (IMD38); Immunodeficiency 38 with basal ganglia calcification; Mendelian susceptibility to mycobacterial disease due to ISG15 deficiency; ISG15-related type I interferonopathy.
- **Information source:** Aggregated from **individual patient case reports and small kindreds** (the disease is ultra-rare; total reported patients are in the low dozens worldwide), synthesized with **disease-level resources** (OMIM, Orphanet). Not derived from EHR/population cohorts.

---

## 2. Etiology

- **Primary cause (genetic):** Biallelic (homozygous or compound heterozygous) **loss-of-function variants in ISG15** producing complete absence of ISG15 protein and ISGylation. This is a monogenic Mendelian disorder.
- **Genetic risk factors:** The causal variants themselves; **consanguinity** is a major contributor (most families are consanguineous, from Turkey, Iran, Middle East, China, Brazil). No common susceptibility loci or modifier genes are established; MPO variants co-segregating in one kindred were shown to be non-pathogenic (PMID 37984483).
- **Environmental risk factors / triggers:** **BCG vaccination** (live attenuated *Mycobacterium bovis*) is the principal environmental trigger of the infectious phenotype — most patients present after BCG with regional or disseminated BCG disease (BCGitis/BCGosis). **Environmental (non-tuberculous) mycobacteria** are the other trigger. There is no strong sex or occupational exposure signal.
- **Protective factors:** None established genetically. From a preventive standpoint, **avoidance of BCG vaccination** in known-affected families prevents BCG disease.
- **Gene–environment interaction:** The genetic lesion (low IFN-γ inducibility) is **clinically unmasked by mycobacterial exposure** (BCG/environmental mycobacteria). Individuals never exposed to mycobacteria may present instead with the neurologic or dermatologic (interferonopathy) phenotype, which is exposure-independent.

---

## 3. Phenotypes

The syndrome has **three co-dominant clinical presentations** (infectious, neurologic, dermatologic); individual patients may show one, two, or all three.

| Phenotype | Type | HPO suggestion | Onset | Frequency/notes |
|---|---|---|---|---|
| Susceptibility to BCG / environmental mycobacteria (BCGitis, BCGosis, lymphadenitis) | clinical/infectious | HP:0002754 (osteomyelitis), HP:0032262 (atypical mycobacterial infection), HP:0004432 (abnormal mycobacterial immunity) | Infancy/childhood (post-BCG) | Common in exposed patients |
| Intracranial/basal ganglia calcification | imaging/neurologic | HP:0002514 (cerebral calcification), HP:0007146 (bilateral basal ganglia calcification) | Childhood; often asymptomatic detection | Frequent; may be subclinical |
| Seizures | clinical sign | HP:0001250 (seizure) | Variable | Reported subset |
| Necrotizing / ulcerative skin lesions | physical manifestation | HP:0200041 (skin ulcer), HP:0000951 (abnormal skin morphology) | Childhood–adult | Third phenotype (PMID 32402279) |
| Skin fibrosis / impaired wound healing | physical manifestation | HP:0100699 (scarring), HP:0001075 (atrophic scars) | Chronic | PMID 41743834 |
| Recurrent pneumonia / inflammatory lung disease | clinical | HP:0006532 (recurrent pneumonia) | Variable | PMID 37984483 |
| Elevated blood type I IFN signature (ISG upregulation) | laboratory abnormality | HP:0031381 (increased circulating interferon) | Constitutive | Universal (biomarker) |
| Low mycobacterium-induced IFN-γ production | laboratory abnormality | HP:0032218 (decreased IFN-γ production) | Constitutive | Universal in vitro (PMID 22859821) |

- **Severity:** Variable; ranges from asymptomatic calcification to life-threatening disseminated mycobacterial disease. The interferonopathy is generally **milder than USP18 deficiency** (which is lethal in infancy).
- **Progression:** Intracranial calcification tends to be **stable/slowly progressive**; skin disease can be chronic-relapsing; infections are **episodic** and exposure-linked.
- **Quality-of-life impact:** Chronic skin ulcers, recurrent infections, and (in some) neurologic sequelae/seizures impair daily functioning; formal QoL instrument data are not available for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

- **Causal gene:** **ISG15** (ISG15 ubiquitin-like modifier), chromosome **1p36.33**; encodes a ~17 kDa precursor cleaved to a **15 kDa** mature ubiquitin-like protein bearing a C-terminal LRLRGG motif used for conjugation (ISGylation).
- **Pathogenic variants:**
  - **Type/class:** Predominantly **null / loss-of-function** — nonsense, frameshift, and destabilizing missense variants, all resulting in **complete deficiency**. Reported examples include **p.Leu28Gln (c.83T>A)** — a destabilizing missense (ΔΔG −2.4 kcal/mol; PMID 39365299); **p.Tyr140* (Y140X)** nonsense (PMID 37984483); and various frameshift/nonsense alleles in the original Turkish/Iranian kindreds (PMID 22859821, 25307056).
  - **Classification:** Pathogenic/likely pathogenic per ACMG/AMP (loss-of-function is the established disease mechanism; PVS1-supporting).
  - **Allele frequency:** Individually **ultra-rare/private**; homozygosity typically arises through consanguinity. Not present at appreciable frequency in gnomAD.
  - **Origin:** **Germline**, biallelic. No somatic mechanism.
  - **Functional consequence:** **Loss of function** — absence of both free ISG15 (secreted) and conjugated ISG15 (ISGylation), and secondary loss of USP18 stabilization.
- **Modifier genes:** None validated. Digenic contributions have been excluded in reported kindreds (e.g., MPO co-variants non-pathogenic, PMID 37984483).
- **Epigenetics:** No disease-specific methylation/chromatin defect described; however, the disease produces a strongly altered **transcriptional (IFN-driven) program** rather than a primary epigenetic lesion.
- **Chromosomal abnormalities:** None; this is a single-gene disorder, not a copy-number/structural syndrome.

---

## 5. Environmental Information

- **Environmental factors / infectious agents (central to the infectious phenotype):**
  - **Mycobacterium bovis BCG** (vaccine strain) — NCBI Taxon 33892 — principal trigger.
  - **Environmental / non-tuberculous mycobacteria** (e.g., *M. avium* complex) — low-virulence mycobacteria.
  - Predisposition is essentially restricted to **weakly virulent mycobacteria**; classical *M. tuberculosis* and *Salmonella* susceptibility is variable, as in other MSMD.
- **Lifestyle factors:** Not applicable/none identified.
- **Non-infectious environmental toxins/radiation:** No established role.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

**Branch A — Infectious/MSMD phenotype:**
1. Biallelic ISG15 loss-of-function variant **leads to** absence of ISG15 protein.
2. Absence of **secreted (extracellular) ISG15** from leukocytes (especially granulocytes/neutrophils) and epithelial cells **results in** loss of a non-redundant IFN-γ-inducing signal.
3. Loss of ISG15 **binding to the LFA-1 integrin (CD11a/CD18; αLβ2) receptor** on NK and T cells **results in** failure to trigger IFN-γ release (Swaim et al., PMID 29100055, 32553163).
4. Reduced mycobacterium-induced **IFN-γ production leads to** impaired macrophage activation and killing of intracellular mycobacteria.
5. This **results in** susceptibility to BCG and environmental mycobacteria (MSMD). *(demonstrated: PMID 22859821, 29100055)*

**Branch B — Neurologic/dermatologic interferonopathy:**
1. Absence of **intracellular ISG15 leads to** failure to stabilize **USP18** (ISG15 normally protects USP18 from proteasomal degradation).
2. Loss of USP18 **results in** failure to sterically block JAK1 at IFNAR2 → **sustained/amplified IFN-α/β (JAK-STAT/ISGF3) signaling**.
3. Chronic type I IFN over-activity **leads to** an autoinflammatory state resembling Aicardi-Goutières syndrome — **basal ganglia/intracranial calcification** (inferred to arise from IFN-driven vascular/glial injury), autoinflammation.
4. In skin, IFN-I signaling in **keratinocytes, endothelia, and dermal monocytes/macrophages results in** apoptosis, altered macrophage polarization, epithelial-to-mesenchymal transition, and myofibroblast activation → **necrotizing and fibrotic skin lesions and impaired wound healing**. *(demonstrated: PMID 25307056, 32402279, 41743834)*

### Category checklist
- **Molecular pathways:** Type I IFN **JAK–STAT (JAK1/TYK2 → STAT1/STAT2/IRF9/ISGF3)** signaling (overactive); IL-12/IFN-γ axis (underactive); **secreted ISG15 → LFA-1 integrin (ITGAL/ITGB2, CD11a/CD18) → IFN-γ release** (GO:0005178 integrin binding); **ISG15/ISGylation** ubiquitin-like conjugation cascade (E1 UBE1L/UBA7, E2 UBCH8/UBE2L6, E3 HERC5); deISGylation by USP18.
  - **Reactome/KEGG:** IFN-α/β signaling; ISG15 antiviral mechanism.
- **Cellular processes:** Chronic **inflammation**, IFN-I-induced **apoptosis**, **EMT**, myofibroblast activation, altered macrophage polarization.
- **Protein dysfunction:** Complete **loss of function** of ISG15; secondary **destabilization/loss of USP18**. ISG15 is a **diubiquitin-like protein** comprising two tandem ubiquitin-like (Ubl) domains with a C-terminal LRLRGG conjugation motif (InterPro IPR000626 ubiquitin-like domain; Pfam PF00240; UniProt P05161). Structural studies of the USP18–ISG15 complex show USP18 recognizes only the **C-terminal Ubl domain** of ISG15 via a small hydrophobic interface, explaining USP18's ISG15-specific (not ubiquitin) deconjugation activity and the mutual stabilization relationship (mouse USP18–ISG15 crystal structures, PMID 28165509; PDB e.g. 5CHV/5CHW). Destabilizing missense variants (e.g., p.Leu28Gln) increase protein flexibility/ΔΔG and abolish function (PMID 39365299).
- **Immune system involvement:** Combined defect — **immunodeficiency** (hypomorphic IFN-γ, antimycobacterial) plus **autoinflammation** (excess IFN-α/β).
- **Tissue damage mechanisms:** IFN-I-mediated apoptosis, fibrosis, dystrophic calcification.
- **Molecular profiling:** Patient RNA-seq shows strong **upregulation of interferon-stimulated genes** and JAK/STAT hyperactivation (PMID 39365299, 37984483); spatial transcriptomics localizes IFN-I signatures to epidermis/dermal myeloid cells (PMID 41743834).
- **Suggested GO terms:** GO:0060337 (type I interferon signaling pathway), GO:0032479 (regulation of type I interferon production), GO:0032020 (ISG15-protein conjugation), GO:0006954 (inflammatory response), GO:0060333 (interferon-gamma-mediated signaling).
- **Suggested CL terms:** CL:0000775 (neutrophil), CL:0000623 (NK cell), CL:0000576 (monocyte), CL:0000235 (macrophage), CL:0000312 (keratinocyte), CL:0000057 (fibroblast/myofibroblast).

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - **Brain** — basal ganglia and other intracranial sites (calcification). UBERON:0002420 (basal ganglion); UBERON:0000955 (brain).
  - **Skin** — necrotizing/fibrotic lesions, ulcers. UBERON:0002097 (skin of body); UBERON:0001003 (epidermis).
  - **Lymph nodes / lymphatic system** — mycobacterial lymphadenitis. UBERON:0000029 (lymph node).
  - **Lungs** — recurrent pneumonia/inflammatory lung disease. UBERON:0002048 (lung).
- **Body systems:** Immune, nervous (CNS), integumentary; secondarily lymphatic and respiratory.
- **Tissue/cell level:** Epidermal **keratinocytes**, dermal **endothelium**, **monocytes/macrophages**, **neutrophils** (secretion source), **NK/T lymphocytes** (IFN-γ effectors), **fibroblasts/myofibroblasts** (fibrosis).
- **Subcellular level (GO Cellular Component):** Cytoplasm/cytosol (GO:0005829) — site of ISGylation and JAK-STAT signaling; ISG15 conjugated to targets throughout cytoplasm and nucleus.
- **Localization / lateralization:** Intracranial calcification is characteristically **bilateral/symmetric (basal ganglia)**; skin lesions are variable in distribution.

---

## 8. Temporal Development

- **Onset:** Typically **infancy to childhood**. Infectious presentation follows **BCG vaccination** (first months–years of life). Interferonopathy features (calcification) may be detected incidentally in childhood; dermatologic disease can present later, including adulthood.
- **Onset pattern:** Infections are **acute/subacute and episodic**; the interferonopathy is **chronic/insidious**.
- **Progression:** Basal ganglia calcification is generally **stable or slowly progressive**; skin disease chronic-relapsing; the overall interferonopathy is **milder and more survivable** than complete USP18 deficiency (neonatal lethal).
- **Disease course/duration:** **Chronic, lifelong.** No spontaneous cure; remission of inflammation is **treatment-induced** (JAK inhibition).
- **Critical periods:** The **peri-BCG-vaccination window** (infancy) is the key window for the infectious phenotype; earlier initiation of JAK inhibition may better limit inflammatory sequelae, though CNS damage may still progress.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic loss-of-function).
- **Penetrance/expressivity:** Effectively complete at the biochemical level (absent ISG15), but **variable clinical expressivity** — which of the three phenotypes manifests depends partly on environmental (mycobacterial) exposure and unknown modifiers; siblings with identical variants can show divergent presentations (PMID 37984483).
- **Consanguinity / founder effects:** Strong **consanguinity** association; most kindreds are from Turkey, Iran, the Middle East, China, and Brazil. Recurrent identical variants in unrelated families suggest possible local founder alleles (e.g., c.83T>A in Brazil, PMID 39365299).
- **Carrier frequency:** Very low; heterozygous carriers are asymptomatic. No established population carrier screening.
- **Epidemiology:** **Ultra-rare** (Orphanet class; prevalence <1/1,000,000). Fewer than ~several dozen patients reported worldwide since 2012. No reliable incidence/prevalence estimates.
- **Sex ratio:** No strong sex bias reported (autosomal recessive).
- **Geographic distribution:** Reported predominantly in consanguineous populations; specific variants show regional clustering.

---

## 10. Diagnostics

- **Laboratory / functional tests:**
  - **Absent ISG15 protein and ISGylation** by immunoblot of patient cells (diagnostic hallmark).
  - **Reduced IFN-γ production** by PBMCs/whole blood upon **BCG or BCG+IL-12** stimulation (PMID 22859821, 39365299).
  - **Elevated type I IFN signature** — interferon-stimulated gene (ISG) expression score in blood; hyperactivated **JAK/STAT (phospho-STAT1)** signaling (PMID 37984483).
  - Absence of **USP18 accumulation** in patient cells (research assay).
- **Biomarkers:** Blood **IFN signature (ISG score)** — quantified by RT-qPCR of a panel of interferon-stimulated genes (e.g., IFI27, IFI44L, IFIT1, ISG15, RSAD2, SIGLEC1) or by **SIGLEC1/CD169 surface expression on monocytes** (standard type I interferonopathy biomarkers); low mycobacterium-induced IFN-γ; **absent ISG15 protein on Western blot** (the specific molecular hallmark). LOINC-codable functional assay: IFN-γ release after BCG±IL-12 stimulation.
- **Imaging:** **CT/MRI of brain** showing **bilateral basal ganglia (and other intracranial) calcifications** — a key diagnostic clue (RadLex; overlaps AGS/SPENCD imaging).
- **Genetic testing (definitive):** **Whole-exome (WES) or whole-genome sequencing**, or targeted **MSMD/inborn-errors-of-immunity gene panels** including ISG15, followed by **Sanger confirmation** (PMID 39365299). Single-gene ISG15 sequencing is diagnostic once suspected.
- **Clinical criteria / context:** Diagnosis is suspected in a child with **BCG/environmental mycobacterial disease** and/or **unexplained basal ganglia calcification** and/or **necrotizing skin lesions**, confirmed molecularly.
- **Differential diagnosis:** Other **MSMD genes** (IFNGR1/2, IL12B, IL12RB1, STAT1, IRF8, TYK2, SPPL2A) for the infectious phenotype; other **type I interferonopathies** — **Aicardi-Goutières syndrome**, **spondyloenchondrodysplasia (SPENCD)**, **USP18 deficiency**, **STAT2 gain-of-function (R148Q)** — for the neurologic/calcification phenotype (PMID 25307056, 32092142, 35258551). USP18 deficiency is far more severe (neonatal lethal).
- **Screening:** **Cascade genetic testing** of relatives in known families; consider avoiding BCG in at-risk newborns.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** Generally **better than USP18 deficiency** (which is lethal in infancy). Prognosis depends on control of mycobacterial infections and the severity of the interferonopathy; disseminated mycobacterial disease can be life-threatening. No formal survival statistics exist (ultra-rare).
- **Morbidity/function:** Chronic morbidity from **recurrent infections, seizures/neurologic sequelae, and chronic skin ulceration/fibrosis**; disability is variable.
- **Complications:** Disseminated BCG disease, mycobacterial lymphadenitis/osteomyelitis, recurrent pneumonia, neurologic impairment from calcification/inflammation, and multi-organ fibrosis (skin, lung).
- **Prognostic factors:** Extent of mycobacterial dissemination; magnitude of IFN-I signature; timing of JAK-inhibitor initiation; degree of CNS involvement.
- **Recovery potential:** Infections are treatable; the interferonopathy is controllable but not curable pharmacologically; established CNS damage may be irreversible.

---

## 12. Treatment

Therapy is **split along the two mechanisms** (NCIT concepts noted):

- **Anti-mycobacterial therapy** for BCG/environmental mycobacterial disease (multidrug regimens; e.g., rifampin, isoniazid, ethambutol, macrolides per species). NCIT: antimycobacterial agents.
- **Adjunctive IFN-γ:** Recombinant **IFN-γ (IFN-γ1b)** may be considered for refractory mycobacterial infection, as in other MSMD with hypomorphic IFN-γ. NCIT:C1471 (Interferon Gamma).
- **JAK1/2 inhibitors** for the type I interferonopathy (skin, autoinflammation, and to attempt to limit neurologic disease): **baricitinib** and **ruxolitinib**; **tofacitinib** (JAK1/3) has shown benefit for inflammatory skin lesions in related interferonopathies. RNA-seq in ISG15-deficient patients nominated **baricitinib** (PMID 37984483; class evidence PMID 41871482, 37087470, 40176112). NCIT: baricitinib (C123899), ruxolitinib (C79809), tofacitinib (C97662). CHEBI: baricitinib (CHEBI:145303), ruxolitinib (CHEBI:66919), tofacitinib (CHEBI:71200).
  - **Caveat:** JAK inhibitors give limited/heterogeneous benefit on established **neurologic** manifestations, and **CNS calcification can progress despite early treatment** (PMID 38381212, 41871482) — likely due to poor CNS bioavailability.
- **Supportive/rehabilitative:** Wound care for skin ulcers; management of seizures; immunization counseling.
- **Advanced/experimental:** No approved gene/cell therapy; hematopoietic stem cell transplantation is not standard. Recombinant ISG15 or ISG15-blocking agents were proposed conceptually (PMID 23579383) but are not clinical therapies.
- **Pharmacogenomics:** None specific established.

---

## 13. Prevention

- **Primary prevention:** In families with a known affected child, **avoid BCG vaccination** in at-risk newborns to prevent BCG disease; **genetic counseling** for consanguineous families.
- **Secondary prevention:** **Early molecular diagnosis** (WES/panel), **cascade/carrier testing**, and **prenatal/preimplantation genetic testing** where families opt for it.
- **Tertiary prevention:** Prompt anti-mycobacterial treatment; early JAK inhibition to limit inflammatory complications; surveillance neuroimaging and dermatologic care.
- **Counseling:** Autosomal recessive recurrence risk = **25%** for future offspring of carrier couples.
- **Immunization/public health:** The key public-health action is **withholding live BCG** in known-affected kindreds (BCG is routine in many endemic regions, which is why patients often present post-BCG).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, NCBI Taxon 9606). Orthologs studied in **mouse** (*Mus musculus*, Taxon 10090; gene *Isg15*, NCBI Gene 100038882).
- **Comparative biology — critical caveat:** In **mice**, ISG15/ISGylation is a **bona fide antiviral effector** of type I IFN, and mouse Usp18 does **not** require Isg15 for stabilization. In **humans**, ISGylation is **redundant for antiviral defense**, and the disease-defining role is **USP18 stabilization/IFN-I regulation** (PMID 22859821, 25307056). Thus the human phenotype (interferonopathy) is **not recapitulated** by *Isg15*-knockout mice, which instead show altered antiviral responses.
- **Natural disease in other species:** No well-characterized naturally occurring ISG15-deficiency disease reported in companion animals/wildlife (not in OMIA as a defined phenotype). No zoonotic component.

---

## 15. Model Organisms

- **Mouse (*Isg15*−/−, *Ube1L/Uba7*−/−):** Model the **antiviral ISGylation** role and hematopoietic effects (PMID 20591702) but **do not reproduce the human USP18-dependent interferonopathy** — a major limitation. Resources: MGI, IMPC.
- **Human cellular models:** **Patient-derived fibroblasts, B-cell lines, PBMCs**, and **ISG15-knockout human epithelial/fibroblast lines** best recapitulate the human phenotype — showing hyperactive JAK/STAT, IFN-I-induced apoptosis, EMT, and impaired wound healing (PMID 41743834, 37984483). iPSC/organoid and spatial-transcriptomic ex vivo skin models have been used.
- **Applications:** Dissecting IFN-I regulation (USP18/ISG15/STAT2 axis), fibrosis mechanisms, and testing JAK-inhibitor efficacy.

---

## Evidence Table (Key PMIDs)

| PMID | Contribution | Evidence type |
|---|---|---|
| 22859821 | First description; MSMD via loss of secreted ISG15 → low IFN-γ; ISGylation redundant for antiviral immunity | Human clinical + in vitro |
| 29100055 / 32553163 | Extracellular ISG15 receptor is LFA-1 (CD11a/CD18); drives IFN-γ release from NK/T cells | In vitro / mechanistic |
| 25307056 | Intracellular ISG15 stabilizes USP18; loss → IFN-α/β over-amplification, interferonopathy, calcification | Human clinical + mechanistic |
| 32402279 | Third (dermatologic) phenotype; cell-type-specific IFN-I signaling in skin | Human clinical + molecular |
| 41743834 | IFN-I-driven fibrosis: apoptosis, EMT, myofibroblast activation, impaired healing | Ex vivo + in vitro |
| 37984483 | Novel Y140X; divergent sibling phenotypes; JAK/STAT hyperactivation; baricitinib nominated | Human clinical + RNA-seq |
| 39365299 | Recurrent c.83T>A (L28Q) in unrelated Brazilian families; low IFN-γ; transcriptomics | Human clinical + in silico |
| 35258551 | USP18 deficiency (I60N) — mechanistic/differential context | Human clinical |
| 32092142 | STAT2 R148Q phenocopy of USP18 deficiency — differential context | Human clinical |
| 42643649 | MSMD genetic heterogeneity (~22 genes, IFN-γ axis) | Review/case |
| 38381212 / 41871482 | JAK-inhibitor efficacy/limits in interferonopathies (CNS) | Clinical |
| 23579383 | ISG15 as secreted IFN-γ-inducing molecule; therapeutic concepts | Review |
| 28165509 | Crystal structure of USP18–ISG15; C-terminal Ubl domain specificity | Structural |
| 20591702 | Ube1L/ISGylation mouse hematopoietic model | Mouse model |

---

## Supported vs. Refuted Hypotheses

**Supported:**
- ISG15 loss causes MSMD through impaired IFN-γ (secreted-ISG15 mechanism). ✔ (PMID 22859821)
- ISG15 loss causes a type I interferonopathy via failed USP18 stabilization. ✔ (PMID 25307056)
- Disease has three co-dominant phenotypes (infectious/neurologic/dermatologic). ✔ (PMID 32402279)
- JAK1/2 inhibition is the rational therapy for the interferonopathy. ✔ (PMID 37984483, 41871482)

**Refuted / negative findings:**
- Human ISG15 deficiency causes severe viral disease — **refuted** (no unusual viral susceptibility; PMID 22859821).
- Mouse *Isg15* knockouts model the human disease — **largely refuted** (species divergence; mice model antiviral role only).
- Co-inherited MPO variants contribute to pathology — **refuted** in the reported kindred (PMID 37984483).

## Limitations and Future Directions
- Ultra-rare disease: no population epidemiology, survival statistics, or QoL instrument data; evidence rests on case reports/small kindreds.
- Genotype–phenotype determinants of which phenotype manifests remain unexplained (modifiers, exposure).
- CNS-penetrant anti-IFN therapies are an unmet need; current JAK inhibitors inadequately protect the brain.
- Better human models (organoids, iPSC-derived neurons/microglia) are needed given mouse divergence.


## Artifacts

- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_ISG15_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mendelian_Susceptibility_To_Mycobacterial_Diseases_Due_To_Complete_ISG15_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014502` (3 mentions) - the report calls it "if available"; MONDO calls it **Mendelian susceptibility to mycobacterial diseases due to complete ISG15 deficiency**
- `HP:0031381` (1 mention) - the report calls it "increased circulating interferon"; HP calls it **Decreased mitogen-induced T-cell proliferation**
- `NCIT:C1471` (1 mention) - the report calls it "Interferon Gamma"; NCIT calls it **Lamivudine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0032218` (1 mention) - the report calls it "decreased IFN-γ production"; HP calls it **Decreased total CD4+ T cell proportion**, and lists "Decreased helper T cell proportion" among its other names
- `GO:0060337` (1 mention) - the report calls it "type I interferon signaling pathway"; GO calls it **type I interferon-mediated signaling pathway**, and lists "type I interferon signaling pathway" among its other names
- `GO:0060333` (1 mention) - the report calls it "interferon-gamma-mediated signaling"; GO calls it **type II interferon-mediated signaling pathway**, and lists "interferon-gamma-mediated signaling pathway" among its other names
- `CL:0000623` (1 mention) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names
- `CL:0000057` (1 mention) - the report calls it "fibroblast/myofibroblast"; CL calls it **fibroblast**
- `UBERON:0001003` (1 mention) - the report calls it "epidermis"; UBERON calls it **skin epidermis**, and lists "epidermis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
