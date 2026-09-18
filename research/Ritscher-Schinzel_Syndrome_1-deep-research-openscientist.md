---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T07:14:02.022277'
end_time: '2026-09-03T07:51:57.850010'
duration_seconds: 2275.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ritscher-Schinzel Syndrome 1
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ritscher-Schinzel_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ritscher-Schinzel_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ritscher-Schinzel Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ritscher-Schinzel Syndrome 1** covering all of the
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

# Ritscher-Schinzel Syndrome 1 (RSS1 / 3C Syndrome): Comprehensive Disease Report

## Summary

**Ritscher-Schinzel Syndrome 1 (RSS1)**, also known as **cranio-cerebello-cardiac (3C) syndrome**, is a rare autosomal-recessive congenital multiple-malformation disorder (OMIM **#220210**) defined by the diagnostic triad of distinctive **craniofacial dysmorphism**, **cerebellar / posterior-fossa malformations** (Dandy-Walker spectrum), and **congenital heart defects**, accompanied by developmental delay and intellectual disability. RSS1 specifically is caused by **biallelic hypomorphic loss-of-function variants in *WASHC5* (formerly *KIAA0196*)**, the gene encoding **strumpellin**, a core subunit of the endosomal **WASH actin-nucleating complex** ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)).

Mechanistically, strumpellin deficiency destabilizes the WASH complex, which normally activates the Arp2/3 complex to nucleate branched F-actin on endosomes. This actin machinery, working in concert with the **retromer** and the **CCC/Commander** complexes, drives the sorting and recycling of transmembrane cargo (e.g., LDLR, integrins, the copper transporter ATP7A) back to the plasma membrane and away from lysosomal degradation. Loss of strumpellin therefore impairs endosomal cargo recycling, disrupting membrane-protein homeostasis during a critical window of embryonic development and producing the characteristic cranio-cerebello-cardiac malformation spectrum ([PMID: 26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/), [PMID: 22070227](https://pubmed.ncbi.nlm.nih.gov/22070227/), [PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).

Ritscher-Schinzel syndrome as a clinical entity is **genetically heterogeneous**: RSS1 (*WASHC5*, autosomal recessive), RSS2 (*CCDC22*, X-linked recessive), RSS3 (*VPS35L*), and RSS4 (*DPYSL5*) — all but DPYSL5 converge on the same **WASH / retromer / Commander endosomal trafficking module** ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/), [PMID: 31712251](https://pubmed.ncbi.nlm.nih.gov/31712251/)). No disease-modifying therapy exists; management is symptomatic and multidisciplinary. This report covers all 15 requested disease-characteristic sections, drawing on 9 confirmed findings and 30 reviewed papers.

> **Note on nomenclature:** OMIM assigns *WASHC5*-related disease as RSS1 (#220210) and *CCDC22* as RSS2 (#300963). One review ([PMID: 34020006](https://pubmed.ncbi.nlm.nih.gov/34020006/)) inverts these labels; this report follows the OMIM/dosage convention in which **WASHC5 = RSS1** as specified by the research question.

---

## Key Findings

### Finding 1 — RSS1 is caused by biallelic *WASHC5*/strumpellin loss of function (autosomal recessive; OMIM #220210)

The molecular cause of RSS1 was identified by homozygosity mapping plus Sanger sequencing in **8 First Nations patients from northern Manitoba** with classic Ritscher-Schinzel/3C syndrome. All eight were homozygous for a novel splice-site mutation in *KIAA0196* (now *WASHC5*) at chromosome **8q24.13**. The functional consequence was demonstrated at both RNA and protein level: RNA analysis showed an approximately **eightfold reduction** in the transcript lacking exon 27, and Western blot showed a **~60% reduction in strumpellin protein** ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)).

> *"All eight patients were homozygous for a novel splice site mutation in KIAA0196. RNA analysis revealed an approximate eightfold reduction in the relative amount of a KIAA0196 transcript lacking exon 27. A 60% reduction in the amount of strumpellin protein was observed on western blot."* — Elliott et al. 2013

This establishes strumpellin — a subunit of the WASH endosomal actin-nucleation complex — as the RSS1 disease protein and shows that RSS1 arises from a **hypomorphic (partial loss-of-function) allele** retaining ~40% of protein, not a complete null.

### Finding 2 — Ritscher-Schinzel syndrome is genetically heterogeneous (four genes)

Four genes are implicated in the RSS spectrum, all converging on endosomal trafficking machinery:

| Subtype | Gene | Inheritance | OMIM | Complex |
|---------|------|-------------|------|---------|
| **RSS1** | ***WASHC5*** (KIAA0196, strumpellin) | Autosomal recessive | #220210 | WASH complex |
| RSS2 | *CCDC22* | X-linked recessive | #300963 | CCC / Commander |
| RSS3 | *VPS35L* | Autosomal recessive | — | Retriever / Commander |
| RSS4 | *DPYSL5* | Autosomal dominant | — | (cytoskeletal / CRMP) |

> *"The first two genes described were the autosomal recessive inherited gene WASHC5 associated with Ritscher-Schinzel syndrome 1 (RTSCS1), and CCDC22, an X-linked recessive gene causing Ritscher-Schinzel syndrome 2 (RTSCS2). In recent years, two other genes have been identified: VPS35L (RTSCS3) and DPYSL5 (RTSCS4)."* — Neri et al. 2022 ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/))

RSS1 (*WASHC5*) and RSS2 (*CCDC22*) patients share a **similar facial gestalt**, reflecting the shared pathway ([PMID: 34020006](https://pubmed.ncbi.nlm.nih.gov/34020006/)). Biallelic *VPS35L* variants cause a 3C/RSS-like syndrome through **retriever-complex** dysfunction ([PMID: 31712251](https://pubmed.ncbi.nlm.nih.gov/31712251/)).

### Finding 3 — Mechanism: WASH + CCC complexes mediate endosomal cargo recycling; strumpellin loss impairs receptor recycling and lysosomal function

The **COMMD/CCDC22/CCDC93 (CCC)** and **WASH** complexes are both required for endosomal sorting of transmembrane cargo. Using LDL receptor (LDLR) as a model cargo, inactivation of the WASH complex was shown to cause **LDLR mislocalization, increased lysosomal degradation of LDLR, and impaired LDL uptake**; strikingly, a mutation in *KIAA0196* (strumpellin) is associated with human **hypercholesterolaemia** ([PMID: 26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/)).

> *"Inactivation of the CCC-associated WASH complex causes LDLR mislocalization, increased lysosomal degradation of LDLR and impaired LDL uptake. Furthermore, a mutation in the WASH component KIAA0196 (strumpellin) is associated with hypercholesterolaemia in humans."* — Bartuzi et al. 2016

The upstream recruitment step is defined: the WASH complex is targeted to endosomes through the extended, unstructured "tail" domain of **FAM21** binding the retromer subunit **VPS35** ([PMID: 22070227](https://pubmed.ncbi.nlm.nih.gov/22070227/)).

> *"the retromer-WASH complex interaction occurs through the long unstructured 'tail' domain of the WASH complex-Fam21 protein binding to Vps35, an interaction that is necessary and sufficient to target the WASH complex to endosomes"* — Harbour et al. 2012

Downstream, strumpellin loss produces **lysosomal abnormalities** through failed endosomal tubule fission and disrupted mannose-6-phosphate-receptor sorting ([PMID: 28389476](https://pubmed.ncbi.nlm.nih.gov/28389476/)).

### Finding 4 — *WASHC5* allelic series: dominant missense → SPG8; biallelic hypomorphic loss → RSS1; complete null → embryonic lethal

*WASHC5* exhibits a striking **allelic series** governed by dosage:

- **Dominant missense mutations** cause **hereditary spastic paraplegia type 8 (SPG8)**, an adult-onset (3rd–4th decade) pure spastic paraparesis ([PMID: 31814071](https://pubmed.ncbi.nlm.nih.gov/31814071/), [PMID: 26572744](https://pubmed.ncbi.nlm.nih.gov/26572744/)).
- **Biallelic hypomorphic loss** (retaining ~40% protein) causes **RSS1** ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)).
- **Complete loss (null)** is **embryonic lethal** in mouse.

> *"Homozygous but not heterozygous mice showed early embryonic lethality. No transcripts from the knockout allele were detected, and the previously suggested compensation by the wild-type allele upon heterozygosity was disproven."* — Jahic et al. 2015 ([PMID: 26572744](https://pubmed.ncbi.nlm.nih.gov/26572744/))

This dosage sensitivity explains why RSS1-causing alleles must be hypomorphic rather than complete nulls: complete loss of strumpellin is incompatible with life, and constrains gene-replacement strategies.

### Finding 5 — RSS core clinical triad and phenotype frequencies (26-patient cohort)

In a cohort of **26 RSS patients** ([PMID: 28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/)):

| Phenotype | Frequency | HPO term (suggested) |
|-----------|-----------|----------------------|
| Ocular disorders (any) | **100%** | HP:0000478 (Abnormality of the eye) |
| Megalocornea | 69% | HP:0000485 |
| Low-set ears | 80.7% | HP:0000369 |
| Septal heart defects | 68.7% | HP:0001671 |
| Delayed neurodevelopment / ID | 84% | HP:0001263 / HP:0001249 |
| Skeletal anomalies (camptodactyly, single palmar crease, overlapping fingers, vertical talus, nail hypoplasia) | 96% | HP:0012385 / HP:0000954 |
| Megacisterna magna | 31.8% | HP:0002280 |
| Dandy-Walker malformation | 27% | HP:0001305 |
| Male sex | 69% | — |

> *"All of them presented ocular disorders, and megalocornea was the most frequent ocular manifestation (69%), whereas low-set ears (80.7%) and septal heart defects (68.7%) were the most common facial and cardiac malformations, respectively. The most frequent malformations of the posterior fossa were megacisterna magna (31.8%) and Dandy-Walker malformation (27%). 84% of the cases had delayed neurodevelopment or intellectual disability."* — Pira-Paredes et al. 2017

Neri et al. 2022 add that **craniofacial dysmorphism** (macrocephaly, down-slanted palpebral fissures, low-set ears), **developmental delay/ID**, and **ataxic gait** were present in essentially all *WASHC5*/*CCDC22* patients, and that **elevated first-trimester nuchal translucency** was observed in 3 *WASHC5* fetuses ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/)). The 69% male predominance in mixed cohorts likely reflects inclusion of X-linked RSS2 (*CCDC22*) cases; autosomal RSS1 is expected ~1:1.

### Finding 6 — WASH functionally couples to the Commander (CCC + retriever) assembly, linking RSS to NF-κB and copper homeostasis

The **Commander complex** is a 16-protein assembly (COMMD1–10, CCDC22, CCDC93, DENND10, VPS26C, VPS29, VPS35L) that governs endosomal cargo and cell homeostasis and is linked to Wilson's disease and atherosclerosis ([PMID: 34943955](https://pubmed.ncbi.nlm.nih.gov/34943955/)).

> *"Commander complex is a 16-protein complex that plays multiple roles in various intracellular events in endosomal cargo and in the regulation of cell homeostasis, cell cycle and immune response. It consists of COMMD1-10, CCDC22, CCDC93, DENND10, VPS26C, VPS29, and VPS35L."* — Laulumaa & Varjosalo 2021

CCDC22 binds all COMMD proteins and is required for NF-κB activation via IκB ubiquitination/degradation; CCDC22 deficiency blunts proinflammatory NF-κB signaling and can produce ectodermal-dysplasia features and X-linked intellectual disability ([PMID: 23563313](https://pubmed.ncbi.nlm.nih.gov/23563313/)).

> *"we demonstrate that all COMMD proteins bind to CCDC22, a factor recently implicated in X-linked intellectual disability (XLID). We showed that an XLID-associated CCDC22 mutation decreased CCDC22 protein expression and impaired its binding to COMMD proteins."* — Starokadomskyy et al. 2013

Because RSS-causal genes *CCDC22* (RSS2) and *VPS35L* (RSS3) are Commander subunits while *WASHC5* (RSS1) is in the WASH complex that cooperates with retromer/Commander, all RSS subtypes share a single endosomal trafficking module — explaining their overlapping phenotype.

### Finding 7 — Full malformation spectrum and minimal diagnostic criteria

Leonardi et al. 2001 described RSS as a rare autosomal-recessive syndrome and catalogued the full malformation spectrum ([PMID: 11484200](https://pubmed.ncbi.nlm.nih.gov/11484200/)):

> *"Cardiac manifestations include ventricular septal defect, atrial septal defect, tetralogy of Fallot, double outlet right ventricle, hypoplastic left heart, aortic stenosis, pulmonic stenosis and other valvular anomalies. Central nervous system anomalies include Dandy-Walker malformation, cerebellar vermis hypoplasia and enlargement of the cisterna magna."*

- **Cardiac:** VSD, ASD, tetralogy of Fallot, double-outlet right ventricle, hypoplastic left heart, aortic stenosis, pulmonic stenosis, valvular anomalies (a broad conotruncal + left-heart spectrum).
- **CNS:** Dandy-Walker malformation, cerebellar vermis hypoplasia, enlarged cisterna magna, posterior fossa cyst, hydrocephalus.
- **Craniofacial:** cleft palate, ocular coloboma, prominent occiput, low-set ears, hypertelorism, down-slanting palpebral fissures, depressed nasal bridge, micrognathia.

Revised **minimal diagnostic criteria** (cardiac malformation other than isolated PDA + posterior-fossa malformation + certain dysmorphic features) are discussed by Gjerulfsen et al. 2021, who caution these are **not present in all patients** ([PMID: 34020006](https://pubmed.ncbi.nlm.nih.gov/34020006/)).

### Finding 8 — Strumpellin molecular function: WASH-mediated Arp2/3 actin polymerization drives cargo trafficking, endolysosomal integrity, and neuronal plasticity

The WASH complex activates **Arp2/3-mediated actin polymerization** and is pivotal for endosomal membrane trafficking. Strumpellin knockdown in cortical neurons reduced dendritic arborization, synapse formation, and dendritic F-actin clusters and caused abnormal motor coordination in mice — rescued by wild-type strumpellin ([PMID: 37392480](https://pubmed.ncbi.nlm.nih.gov/37392480/)).

> *"WASH complex activates actin-related protein-2/3-mediated actin polymerization and plays a pivotal role in intracellular membrane trafficking in endosomes... Strumpellin knockdown using shRNA attenuated dendritic arborization and synapse formation in cultured cortical neurons, and this effect was rescued by wild-type strumpellin expression."*

Additional concrete cargo readouts: strumpellin-deficient murine platelets show ~20% reduced integrin αIIbβ3 surface expression and delayed fibrinogen uptake ([PMID: 37308549](https://pubmed.ncbi.nlm.nih.gov/37308549/)); SPG8 mutations impair CAV1-dependent integrin-mediated cell adhesion ([PMID: 31911435](https://pubmed.ncbi.nlm.nih.gov/31911435/)); and N471D strumpellin produces endolysosomal defects ([PMID: 30061306](https://pubmed.ncbi.nlm.nih.gov/30061306/)).

> *"Strumpellin-deficient murine platelets display an approximately 20% reduction in integrin αIIbβ3 surface expression. While exposure of the internal αIIbβ3 pool after platelet activation was unaffected, the uptake of the αIIbβ3 ligand fibrinogen was delayed."* — Schurr et al. 2023

A **N471D *Washc5* knock-in mouse** recapitulates RSS-relevant features: mild dilated cardiomyopathy, decreased acoustic startle, thinner eye lenses, gait instability, and brain BPTF up / KLHL11 down; biallelic *Washc5* ablation is prenatally lethal ([PMID: 34312900](https://pubmed.ncbi.nlm.nih.gov/34312900/)).

> *"Homozygous N471D Washc5 knock-in mice showed mild dilated cardiomyopathy, decreased acoustic startle reactivity, thinner eye lenses... While biallelic ablation of Washc5 was prenatally lethal, expression of N471D mutated WASHC5 led to several mild clinical and laboratory parameter[s]..."*

### Finding 9 — WASH complex regulates endosomal recycling of the copper transporter ATP7A via the CCC complex

COMMD1 is linked to early endosomes through the CCC complex (COMMD/CCDC22/CCDC93/C16orf62 = VPS35L), which interacts with the WASH complex required for endosomal F-actin deposition and cargo trafficking with retromer; FAM21 recruits the CCC complex to endosomes. Depletion of CCC components blocks copper-dependent movement of **ATP7A** from endosomes, causing **intracellular copper accumulation**, and humans with *CCDC22* mutations show altered copper homeostasis ([PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).

> *"This COMMD/CCDC22/CCDC93 (CCC) complex interacts with the multisubunit WASH complex... required for endosomal deposition of F-actin and cargo trafficking in conjunction with the retromer... depletion of CCC complex components leads to lack of copper-dependent movement of the copper transporter ATP7A from endosomes, resulting in intracellular copper accumulation"* — Phillips-Krawczak et al. 2015

This adds a defined **copper-metabolism branch** (CHEBI:29036 copper(2+)) to the RSS trafficking pathophysiology.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic loss-of-function variant in *WASHC5*** (e.g., splice-site variant skipping exon 27) **leads to** ~40% residual strumpellin protein. *(demonstrated — [PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/))*
2. Reduced strumpellin **results in** destabilization of the pentameric **WASH complex** (WASHC1–5 + FAM21) and lowers its endosomal branched-actin nucleation activity. *(demonstrated for actin function; inferred for RSS1 complex destabilization — [PMID: 37392480](https://pubmed.ncbi.nlm.nih.gov/37392480/))*
3. Because WASH is recruited to endosomes via **FAM21 binding retromer (VPS35)**, WASH deficiency **impairs** localized **Arp2/3** activation and endosomal recycling-tubule formation. *(demonstrated in vitro — [PMID: 22070227](https://pubmed.ncbi.nlm.nih.gov/22070227/))*
4. Loss of endosomal F-actin **leads to** failed tubule fission, so transmembrane cargo is **not returned** to the surface. Parallel branches:
   - **4a.** LDLR mislocalized and degraded → impaired LDL uptake / hypercholesterolaemia ([PMID: 26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/)).
   - **4b.** Integrins (αIIbβ3, CAV1-dependent) show reduced surface expression / adhesion defects ([PMID: 37308549](https://pubmed.ncbi.nlm.nih.gov/37308549/), [PMID: 31911435](https://pubmed.ncbi.nlm.nih.gov/31911435/)).
   - **4c.** Via CCC/Commander coupling, ATP7A copper-transporter recycling fails → intracellular copper dyshomeostasis ([PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).
   - **4d.** Tubule-fission failure disrupts M6PR sorting → **lysosomal dysfunction** ([PMID: 28389476](https://pubmed.ncbi.nlm.nih.gov/28389476/)).
5. Disrupted membrane-protein homeostasis during embryogenesis **impairs** morphogenetic signaling and cell adhesion/migration in developing brain, heart, eye, and neural-crest–derived craniofacial structures. *(inferred — the specific developmental cargo(es) responsible for each malformation is not established)*
6. This **produces** the clinical triad: **posterior-fossa/cerebellar malformation**, **congenital heart defects**, and **craniofacial dysmorphism**, plus **developmental delay/intellectual disability** ([PMID: 28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/), [PMID: 11484200](https://pubmed.ncbi.nlm.nih.gov/11484200/)).
7. In neurons, reduced WASH-dependent actin plasticity **contributes to** reduced dendritic arborization/synapse formation and ataxic gait ([PMID: 37392480](https://pubmed.ncbi.nlm.nih.gov/37392480/)).

```
 WASHC5 biallelic hypomorph (~40% strumpellin)
              │
              ▼
   WASH complex destabilized on endosomes ◄── recruited by FAM21–VPS35 (retromer)
              │
              ▼
   ↓ Arp2/3 branched-actin nucleation on endosomes
              │
     ┌────────┼─────────────┬───────────────┬──────────────┐
     ▼        ▼             ▼               ▼              ▼
  LDLR      integrins   ATP7A/copper    M6PR/lysosome   neuronal
 recycling   surface     (via CCC/       function        actin
  fails      ↓            Commander)      impaired        plasticity ↓
     │        │             │               │              │
     └────────┴─────┬───────┴───────────────┴──────────────┘
                    ▼
     Disrupted membrane-protein homeostasis in development (inferred)
                    ▼
   Cranio-cerebello-cardiac malformations + ID  (RSS1 clinical triad)
```

**Upstream vs downstream:** The mutation and WASH-complex destabilization are the most upstream events; Arp2/3-actin failure is the central node; the specific cargo-recycling failures are parallel downstream branches; organ malformation is the terminal, integrated readout.

**Suggested ontology terms.** GO biological process: endosome to plasma membrane protein transport (GO:0099638), Arp2/3 complex-mediated actin nucleation (GO:0034314), retrograde transport endosome to Golgi (GO:0042147), endocytic recycling (GO:0032456). GO cellular component: WASH complex (GO:0071203), early endosome membrane (GO:0031901), lysosome (GO:0005764). Cell types (CL): cerebellar Purkinje (CL:0000121) and granule (CL:0000120) neurons, cardiomyocyte (CL:0000746), neural crest cell (CL:0000333), corneal epithelial cell (CL:0000575). Chemical entity (CHEBI): copper(2+) (CHEBI:29036), cholesterol (CHEBI:16113).

---

## Section-by-Section Report

### 1. Disease Information
- **Overview:** RSS1 is a rare autosomal-recessive congenital malformation syndrome (3C = cranio-cerebello-cardiac) characterized by the triad of craniofacial dysmorphism, cerebellar/posterior-fossa malformation, and congenital heart disease, with developmental delay/intellectual disability. First delineated by Ritscher & Schinzel (1987); reviewed with proposed diagnostic criteria by Leonardi et al. 2001 ([PMID: 11484200](https://pubmed.ncbi.nlm.nih.gov/11484200/)).
- **Identifiers:** OMIM **#220210** (disease); *WASHC5* gene OMIM **610657**; Orphanet **ORPHA:7** (3C syndrome); MONDO (suggested) **MONDO:0009353** (Ritscher-Schinzel syndrome); ICD-10 **Q87.8**; ICD-11 **LD2F** (multiple developmental anomalies); no dedicated MeSH term (indexed under "Abnormalities, Multiple"/"Dandy-Walker Syndrome").
- **Synonyms:** 3C syndrome; cranio-cerebello-cardiac dysplasia/syndrome; cranio-cerebro-cardiac syndrome; Ritscher-Schinzel syndrome (type 1).
- **Data source:** Aggregated disease-level knowledge from case reports and small cohorts (largest ~26 patients, [PMID: 28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/); 8-patient founder cohort, [PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)) plus molecular studies — not EHR-derived.

### 2. Etiology
- **Primary cause:** purely **genetic** — biallelic hypomorphic loss-of-function variants in *WASHC5* (autosomal recessive) ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)).
- **Genetic risk factors:** causal *WASHC5* variants; a **founder splice allele** in an isolated northern-Manitoba First Nations community produced a geographic cluster. Modifier genes not established; candidate modifiers are other WASH/CCC/retriever subunits.
- **Environmental risk / protective factors:** none identified; not applicable to a monogenic disorder. **Consanguinity** increases recurrence risk for a recessive disorder ([PMID: 15704124](https://pubmed.ncbi.nlm.nih.gov/15704124/)).
- **Gene–environment interactions:** none documented; disease is essentially fully genotype-determined.

### 3. Phenotypes
See Finding 5 table. Additional detail and suggested HPO terms:
- **Ocular** (100% affected): megalocornea (HP:0000485), coloboma (HP:0000589), posterior embryotoxon (HP:0000627), ptosis (HP:0000508).
- **Craniofacial:** low-set ears (HP:0000369), prominent occiput (HP:0000269), macrocephaly (HP:0000256), hypertelorism (HP:0000316), down-slanting palpebral fissures (HP:0000494), depressed nasal bridge (HP:0005280), cleft palate (HP:0000175), micrognathia (HP:0000347), foramina parietalia (HP:0002697).
- **CNS:** Dandy-Walker malformation (HP:0001305), cerebellar vermis hypoplasia (HP:0001320), megacisterna magna (HP:0002280), hydrocephalus (HP:0000238), intellectual disability (HP:0001249), ataxic gait (HP:0002066), hypotonia (HP:0001252). Epilepsy is generally **absent** in WASHC5 RSS1 ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/)).
- **Cardiac:** ASD/VSD (HP:0001631/HP:0001629), tetralogy of Fallot (HP:0001636), double-outlet right ventricle (HP:0011723), hypoplastic left heart (HP:0004383), pulmonary hypertension (HP:0002092).
- **Skeletal:** camptodactyly (HP:0012385), single transverse palmar crease (HP:0000954), nail hypoplasia (HP:0001792).
- **Onset/severity/progression:** congenital and structural (stable/non-progressive), but sequelae cause substantial lifelong disability; severity variable (from prenatal lethality to survival with moderate ID). **QoL:** intellectual disability, motor/gait impairment, and cardiac/surgical morbidity affect independence and daily functioning; formal EQ-5D/SF-36 data unavailable for this rare disease.

### 4. Genetic / Molecular Information
- **Causal gene (RSS1):** *WASHC5* (HGNC:28984; alias KIAA0196/SPG8; NCBI Gene 9897; Ensembl ENSG00000129680; UniProt Q12768), 8q24.13, encoding **strumpellin** (~134 kDa, spectrin-repeat-containing WASH-complex subunit). Gene OMIM 610657.
- **Variant types:** splice-site (First Nations founder allele skipping exon 27, [PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/)); compound-heterozygous missense/LoF combinations ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/)). RSS1 alleles are **hypomorphic**. ACMG: pathogenic/likely pathogenic for reported recessive alleles; many novel variants remain VUS given rarity.
- **Allele frequency:** individual pathogenic variants are ultra-rare/absent in gnomAD; the Manitoba splice allele is population-restricted.
- **Origin:** germline (constitutional, biallelic).
- **Functional consequence:** loss of function (reduced strumpellin → destabilized WASH complex). Distinct from dominant SPG8 alleles (Finding 4).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established for RSS1. Phenotypically overlapping 6p25 subtelomeric deletions (FOX genes) cause a *distinct* 3C-like syndrome, not RSS1 ([PMID: 15704124](https://pubmed.ncbi.nlm.nih.gov/15704124/)).

### 5. Environmental Information
Not applicable — RSS1 is monogenic. No environmental, lifestyle, or infectious factors are implicated in causation. Infectious/respiratory complications may occur secondarily (e.g., pulmonary hypertension/respiratory failure in a preterm infant, [PMID: 23072186](https://pubmed.ncbi.nlm.nih.gov/23072186/)).

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the ordered causal chain, branch diagram, and GO/CL/CHEBI term suggestions. Core pathway: **WASH complex → Arp2/3-mediated endosomal actin nucleation → retromer/CCC(Commander)-coupled cargo recycling**, with downstream branches to cholesterol/LDLR, integrin adhesion, NF-κB (via CCC/COMMD), copper homeostasis (ATP7A), and lysosomal function. Disease-specific human omics signatures are unavailable; a mouse-brain proteomic signature (BPTF up, KLHL11 down) exists for the N471D knock-in ([PMID: 34312900](https://pubmed.ncbi.nlm.nih.gov/34312900/)).

### 7. Anatomical Structures Affected
- **Organ (primary):** cerebellum / posterior fossa (UBERON:0002037; vermis UBERON:0004720), heart (UBERON:0000948; septa, outflow tract), eyes/cornea (UBERON:0000970/UBERON:0000964), craniofacial skeleton (UBERON:0010323).
- **Secondary:** ventricular system/CSF (hydrocephalus, UBERON:0002289), lungs/pulmonary vasculature, limbs/digits.
- **Body systems:** nervous, cardiovascular, musculoskeletal, ocular/visual, craniofacial.
- **Tissue/cell:** neuroectoderm-derived cerebellar neurons; **neural crest** derivatives (craniofacial mesenchyme, cardiac outflow). Strumpellin is ubiquitous → cell-autonomous defect across many cell types.
- **Subcellular:** early/recycling endosome membrane (GO:0031901/GO:0055037), WASH complex (GO:0071203), lysosome (GO:0005764), trans-Golgi network, ER–endosome contact sites ([PMID: 28389476](https://pubmed.ncbi.nlm.nih.gov/28389476/)).
- **Laterality:** typically **bilateral/midline** (cerebellar vermis, septal defects), consistent with a developmental mechanism.

### 8. Temporal Development
- **Onset:** congenital/prenatal; malformations form in utero; elevated first-trimester nuchal translucency is an early marker in some fetuses ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/)). Diagnosis often neonatal/first year (42% <1 year in the Colombian cohort; [PMID: 28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/)).
- **Course:** core malformations are **static/non-progressive**; neurodevelopmental disability is lifelong; prognosis dominated by cardiac/respiratory severity in infancy ([PMID: 23072186](https://pubmed.ncbi.nlm.nih.gov/23072186/)).
- **Critical period:** embryonic organogenesis (cardiac septation ~weeks 4–8, cerebellar/posterior-fossa, neural-crest craniofacial development); no post-developmental window reverses malformations.
- **Duration:** chronic, lifelong.

### 9. Inheritance and Population
- **Inheritance:** autosomal recessive (RSS1). Penetrance essentially complete for biallelic genotype; expressivity **variable**. No anticipation (not a repeat disorder).
- **Founder effect / consanguinity:** founder splice allele in northern Manitoba First Nations; consanguinity enhances recessive recurrence ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/), [PMID: 15704124](https://pubmed.ncbi.nlm.nih.gov/15704124/)).
- **Epidemiology:** very rare; precise prevalence/incidence not established (<1/1,000,000 order of magnitude implied; <~50 molecularly confirmed cases worldwide). ~26-patient clinical cohort with 69% male (partly reflecting X-linked RSS2 inclusion) ([PMID: 28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/)); autosomal RSS1 expected ~1:1.
- **Geographic distribution:** reported in Canada/First Nations, Austria, Colombia, China, and Europe; no endemic region beyond the founder cluster. Carrier frequency not formally estimated (elevated in the founder population).

### 10. Diagnostics
- **Genetic testing (definitive):** WES/WGS or multigene malformation panels including *WASHC5*, *CCDC22*, *VPS35L*, *DPYSL5*; targeted founder-variant testing in the northern Manitoba First Nations population; Sanger segregation. CMA/karyotype to exclude phenocopies (e.g., 6p25 deletion). Research-grade confirmation: reduced strumpellin on Western blot / transcript analysis ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/), [PMID: 24916641](https://pubmed.ncbi.nlm.nih.gov/24916641/)).
- **Imaging:** brain MRI (Dandy-Walker spectrum, vermis hypoplasia, megacisterna magna), echocardiography (septal/conotruncal defects, PDA, coarctation, pulmonary hypertension), ophthalmologic exam (megalocornea, coloboma).
- **Clinical criteria:** cardiac malformation (other than isolated PDA) + posterior-fossa malformation + characteristic dysmorphism, acknowledging incomplete criteria in some patients ([PMID: 34020006](https://pubmed.ncbi.nlm.nih.gov/34020006/)).
- **Laboratory / biomarkers:** consider lipid profile (LDLR trafficking defect → possible hypercholesterolaemia, [PMID: 26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/)); no validated RSS1-specific biomarker.
- **Differential diagnosis:** 6p25 subtelomeric deletion syndrome ([PMID: 15704124](https://pubmed.ncbi.nlm.nih.gov/15704124/)), Dandy-Walker malformation of other cause, RSS subtypes 2–4, Joubert/CHARGE (for coloboma/posterior fossa).
- **Screening:** cascade/carrier testing in founder and consanguineous families; prenatal testing if familial variants known.

### 11. Outcome / Prognosis
- **Survival/mortality:** variable, driven chiefly by **cardiac and respiratory** severity; life-threatening features are generally cardiac ([PMID: 23072186](https://pubmed.ncbi.nlm.nih.gov/23072186/)). Severe cases include prenatal lethality/terminated pregnancies; milder cases survive into childhood/adulthood with disability ([PMID: 36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/)). No systematic survival statistics exist given rarity.
- **Morbidity/function:** lifelong intellectual disability (84%), ataxia, motor and feeding difficulties, visual impairment; malformations non-progressive but disabling.
- **Complications:** heart failure, pulmonary hypertension, hydrocephalus, feeding difficulty/failure to thrive, recurrent infections.
- **Prognostic factors:** severity of congenital heart defect, degree of hydrocephalus/cerebellar malformation, and overall malformation burden. No validated molecular prognostic biomarker.

### 12. Treatment
No disease-modifying or curative therapy exists; management is **symptomatic and multidisciplinary** (NCIT: Supportive Care Intervention).
- **Surgical/interventional:** congenital heart defect repair (ASD/VSD closure, PDA ligation, coarctation repair; NCIT cardiac surgical procedures); CSF diversion/ventriculoperitoneal shunt for hydrocephalus; ophthalmologic and craniofacial/orthopedic surgery as indicated.
- **Supportive/rehabilitative:** feeding support (NG/gastrostomy for hypotonia/feeding difficulty, [PMID: 33059814](https://pubmed.ncbi.nlm.nih.gov/33059814/)), physical/occupational/speech therapy, developmental and special-education services, respiratory support and pulmonary-hypertension management ([PMID: 23072186](https://pubmed.ncbi.nlm.nih.gov/23072186/)).
- **Pharmacotherapy:** symptom-directed only (heart-failure and pulmonary-hypertension agents); dyslipidaemia monitoring is biologically plausible but not a validated indication. No RSS1-specific pharmacogenomics.
- **Advanced/experimental:** none approved or in trials; gene replacement is constrained by strumpellin **dosage sensitivity** (null is embryonic-lethal; overexpression potentially harmful, [PMID: 26572744](https://pubmed.ncbi.nlm.nih.gov/26572744/)).
- **Genetic counseling** is core (25% recurrence risk for AR RSS1; carrier testing).

### 13. Prevention
- **Primary:** not possible for occurrence; genetic counseling, carrier screening in at-risk/founder/consanguineous families, and preimplantation or prenatal genetic testing where familial variants are known.
- **Secondary:** prenatal ultrasound/MRI and molecular testing for early diagnosis; postnatal echocardiography/brain MRI for early complication detection.
- **Tertiary:** proactive cardiac, neurosurgical, and developmental surveillance.
- **Immunization/public-health/environmental:** not applicable (no infectious/environmental cause).

### 14. Other Species / Natural Disease
- **Orthologs:** *Washc5* (mouse, *Mus musculus* NCBITaxon:10090); strumpellin is highly conserved and ubiquitously expressed, with the WASH complex conserved to *Dictyostelium* and *Drosophila* ([PMID: 24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/), [PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).
- **Natural disease:** no well-characterized naturally occurring RSS1 phenotype in other species (no established OMIA *Washc5* entry). Related CCC-complex biology is disease-relevant in dogs: **COMMD1 deficiency causes copper toxicosis** in Bedlington Terriers, a comparative Commander-complex disorder ([PMID: 34943955](https://pubmed.ncbi.nlm.nih.gov/34943955/)).
- **Comparative biology:** the WASH–retromer–Commander module is evolutionarily conserved, validating cross-species mechanistic study. **Transmission:** not applicable (non-communicable genetic disorder).

### 15. Model Organisms
- **Mouse *Washc5* knockout:** homozygous null → early embryonic/prenatal lethality; heterozygotes viable with no wild-type compensation ([PMID: 26572744](https://pubmed.ncbi.nlm.nih.gov/26572744/), [PMID: 34312900](https://pubmed.ncbi.nlm.nih.gov/34312900/)). *Limitation:* complete null cannot model the viable hypomorphic RSS1 state.
- **N471D *Washc5* knock-in mouse (SPG8 allele, partially RSS-informative):** homozygotes show mild dilated cardiomyopathy, thinner eye lenses, gait instability, decreased acoustic startle, brain BPTF/KLHL11 dysregulation ([PMID: 34312900](https://pubmed.ncbi.nlm.nih.gov/34312900/)) — cardiac/ocular features are RSS-relevant, though the allele is missense rather than an RSS1 hypomorph.
- **VPS35L knockout mouse (RSS3 model):** demonstrates biallelic *VPS35L* loss causes a 3C/RSS-like syndrome via retriever dysfunction ([PMID: 31712251](https://pubmed.ncbi.nlm.nih.gov/31712251/)).
- **Cellular/in-vitro:** strumpellin-knockdown cortical neurons (dendritic/synaptic deficits, [PMID: 37392480](https://pubmed.ncbi.nlm.nih.gov/37392480/)); strumpellin-deficient platelets (integrin trafficking, [PMID: 37308549](https://pubmed.ncbi.nlm.nih.gov/37308549/)); N471D cell models (endolysosomal defects, [PMID: 30061306](https://pubmed.ncbi.nlm.nih.gov/30061306/)); WASH/CCC-knockdown lines (LDLR, ATP7A trafficking, [PMID: 26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/), [PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).
- **Gaps:** conditional/hypomorphic mouse and iPSC/organoid models are lacking. No single model reproduces the complete human cranio-cerebello-cardiac triad.

---

## Evidence Base

| PMID | Paper (short) | Role in this report |
|------|---------------|---------------------|
| [24065355](https://pubmed.ncbi.nlm.nih.gov/24065355/) | *Novel KIAA0196 mutation in First Nations 3C cohort* | **Establishes WASHC5/strumpellin as RSS1 cause** (F001) |
| [36130690](https://pubmed.ncbi.nlm.nih.gov/36130690/) | *Pre/postnatal phenotype of WASHC5 & CCDC22 RSS* | Four-gene heterogeneity; phenotype/NT data (F002, F005) |
| [34020006](https://pubmed.ncbi.nlm.nih.gov/34020006/) | *Expansion of CCDC22 RSS; diagnostic criteria* | Shared facial gestalt; minimal criteria (F002, F007) |
| [26965651](https://pubmed.ncbi.nlm.nih.gov/26965651/) | *CCC/WASH sorting of LDLR* | WASH cargo-recycling function; hypercholesterolaemia (F003) |
| [22070227](https://pubmed.ncbi.nlm.nih.gov/22070227/) | *FAM21–Vps35 recruits WASH* | Upstream endosomal recruitment step (F003) |
| [28389476](https://pubmed.ncbi.nlm.nih.gov/28389476/) | *ER–endosome contacts / lysosome function in HSP* | Lysosomal consequence of strumpellin loss (F003) |
| [26572744](https://pubmed.ncbi.nlm.nih.gov/26572744/) | *KIAA0196 spectrum + murine knockout* | Allelic series; null embryonic lethal (F004) |
| [28555453](https://pubmed.ncbi.nlm.nih.gov/28555453/) | *26-patient RSS phenotype series* | Quantitative phenotype frequencies (F005) |
| [11484200](https://pubmed.ncbi.nlm.nih.gov/11484200/) | *Leonardi RSS review, 4 new cases* | Full malformation spectrum; AR inheritance (F007) |
| [34943955](https://pubmed.ncbi.nlm.nih.gov/34943955/) | *Commander Complex review* | Commander composition; RSS gene network (F006) |
| [23563313](https://pubmed.ncbi.nlm.nih.gov/23563313/) | *CCDC22 & NF-κB* | CCC/NF-κB; XLID link (F006) |
| [25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/) | *COMMD1–WASH–ATP7A* | Copper-homeostasis branch (F009) |
| [37392480](https://pubmed.ncbi.nlm.nih.gov/37392480/) | *Strumpellin & cortical neuron plasticity* | Arp2/3 function; neurodevelopmental role (F008) |
| [37308549](https://pubmed.ncbi.nlm.nih.gov/37308549/) | *Strumpellin & platelet integrin trafficking* | Concrete cargo readout (F008) |
| [34312900](https://pubmed.ncbi.nlm.nih.gov/34312900/) | *N471D Washc5 knock-in mice* | Model recapitulating cardiac/ocular features (F008, §15) |
| [31911435](https://pubmed.ncbi.nlm.nih.gov/31911435/) | *SPG8 mutations & CAV1/integrin adhesion* | Integrin/adhesion mechanism (F008) |
| [30061306](https://pubmed.ncbi.nlm.nih.gov/30061306/) | *N471D strumpellin endolysosomal defects* | Endolysosomal phenotype (F008) |
| [31712251](https://pubmed.ncbi.nlm.nih.gov/31712251/) | *VPS35L → 3C/RSS-like via retriever* | RSS3; retriever/Commander convergence (F002) |
| [24916641](https://pubmed.ncbi.nlm.nih.gov/24916641/) | *CCDC22 XLID with RSS features* | RSS2; phenotypic overlap; WES diagnostics |
| [15704124](https://pubmed.ncbi.nlm.nih.gov/15704124/) | *6p25 subtelomeric deletion overlap* | Differential diagnosis / phenocopy |
| [31814071](https://pubmed.ncbi.nlm.nih.gov/31814071/) | *SPG8 in Italian families* | Dominant-missense SPG8 arm of allelic series (F004) |
| [23072186](https://pubmed.ncbi.nlm.nih.gov/23072186/) | *Preterm infant, RSS respiratory problems* | Cardiac/pulmonary prognosis |
| [33059814](https://pubmed.ncbi.nlm.nih.gov/33059814/) | *CCDC22 RSS case, feeding difficulty/hypotonia* | Supportive-care features |

**Evidence source types:** human clinical (cohort/case series: 24065355, 28555453, 36130690, 34020006, 11484200, 24916641); model organism (mouse: 26572744, 34312900, 31712251); in-vitro/cell biology (26965651, 22070227, 25355947, 37392480, 37308549, 30061306, 28389476); review/computational (34943955).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** Fewer than ~50 molecularly confirmed RSS patients exist across all genes; precise prevalence, incidence, sex ratio, and survival for RSS1 specifically are not established. Mixed "3C cohorts" combine WASHC5 (AR) and CCDC22 (X-linked) patients, confounding sex-ratio and frequency estimates.
2. **Nomenclature ambiguity.** OMIM and some literature label WASHC5- vs CCDC22-related disease inconsistently; this report follows OMIM #220210 = *WASHC5* = RSS1 per the research question.
3. **Developmental causal link is inferred, not demonstrated.** The specific WASH-dependent cargo(es) whose mis-trafficking produces cerebellar, cardiac, and craniofacial malformations are not identified; steps 4→6 of the causal chain are mechanistically plausible but not proven in developing human tissue.
4. **No RSS1 patient-tissue omics.** Transcriptomic, proteomic, metabolomic, or single-cell data from RSS1 patients are unavailable; mechanism is extrapolated from cell lines and heterologous models (platelets, cortical neurons, SPG8 knock-in mice).
5. **No faithful animal model of RSS1.** The null mouse is embryonic lethal; the available knock-in carries an SPG8 (dominant) allele, not a biallelic RSS1 hypomorph.
6. **No treatment/trials.** There is no targeted therapy, no clinical trial, and no validated biomarker; QoL and natural-history data are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a biallelic *Washc5* hypomorphic mouse** (e.g., the exon-27 splice allele or a graded-expression conditional allele) to model the viable ~40%-protein RSS1 state and test whether it reproduces the cranio-cerebello-cardiac triad.
2. **Patient iPSC-derived cerebellar organoids and cardiomyocytes** to define which endosomal cargoes are mis-recycled in disease-relevant cell types (single-cell RNA-seq + surface proteomics), linking specific cargo defects to specific malformations.
3. **Systematic cargo screen** (surface-proteome comparison of strumpellin-deficient vs rescued cells) to build the definitive list of WASH-dependent developmental cargoes beyond LDLR/integrins/ATP7A/M6PR.
4. **Copper-homeostasis biomarker study** in RSS1/CCDC22 patients (serum copper, ceruloplasmin, ATP7A trafficking assays) to test whether the copper branch is clinically measurable and potentially actionable ([PMID: 25355947](https://pubmed.ncbi.nlm.nih.gov/25355947/)).
5. **International RSS registry** combining WASHC5/CCDC22/VPS35L/DPYSL5 cases with genotype–phenotype and natural-history data to establish penetrance, expressivity, survival, and refined diagnostic criteria.
6. **Structural/biophysical characterization** of RSS1 vs SPG8 strumpellin variants within the reconstituted WASH complex to explain the dominant-missense vs recessive-hypomorph allelic dichotomy at the molecular level.

---

*Report compiled from 9 confirmed findings and 30 reviewed papers over 5 investigation iterations. All quoted text is verbatim from the cited PubMed abstracts. Evidence types: human clinical, model organism, in-vitro cell biology, and computational/review, as cited by PMID above.*


## Artifacts

- [OpenScientist final report](Ritscher-Schinzel_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ritscher-Schinzel_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 57 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000369` (2 mentions) - the report calls it "Craniofacial:** low-set ears"; HP calls it **Low-set ears**
- `HP:0012385` (2 mentions) - the report calls it "Skeletal:** camptodactyly"; HP calls it **Camptodactyly**
- `HP:0001305` (2 mentions) - the report calls it "CNS:** Dandy-Walker malformation"; HP calls it **Dandy-Walker malformation**

56 of 57 terms resolved to a current term; the rest could not be looked up either way.
