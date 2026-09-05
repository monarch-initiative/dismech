---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T07:13:23.890510'
end_time: '2026-09-03T07:29:12.721565'
duration_seconds: 948.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Secondary Erythromelalgia
  mondo_id: ''
  category: Complex
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
citation_count: 26
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Secondary_Erythromelalgia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Secondary_Erythromelalgia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Secondary Erythromelalgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Secondary Erythromelalgia** covering all of the
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

# Secondary Erythromelalgia: A Comprehensive Disease Characteristics Report

## Summary

**Secondary (acquired) erythromelalgia (EM)** is a rare neurovascular acrosyndrome defined by the clinical triad of recurrent, paroxysmal **burning pain, erythema (redness), and increased local temperature (warmth) of the acral extremities**, characteristically provoked by heat, exercise, and limb dependency and relieved by cooling and elevation. Unlike **primary/inherited EM** (an autosomal-dominant *SCN9A*/Na_v1.7 sodium-channel gain-of-function neuropathy), secondary EM is not caused by a germline mutation. It is a **symptom of an underlying acquired disease** — most classically a **myeloproliferative neoplasm (MPN)**, especially essential thrombocythemia (ET) or polycythemia vera (PV), but also autoimmune/collagen-vascular disease (systemic lupus erythematosus), small-fiber peripheral neuropathy, diabetes mellitus, infections, and certain drugs (calcium-channel blockers, bromocriptine).

The best-characterized mechanism is the **MPN-associated (thrombocythemic) form**: somatic driver mutations (*JAK2* V617F, *CALR*, *MPL*) in hematopoietic stem cells produce clonal, hyperreactive platelets that drive **platelet cyclooxygenase (COX-1)/thromboxane-mediated arteriolar inflammation, fibromuscular intimal proliferation, and platelet-rich microthrombosis** of acral end-arterioles, producing localized ischemia experienced as burning pain, redness, and warmth. This form responds **dramatically and pathognomonically to low-dose aspirin** and remits with cytoreduction that normalizes the platelet count. A second, complementary line of evidence points to an **immune/complement-mediated microvascular injury and dysautonomia** mechanism (endothelial C5b-9 membrane-attack-complex deposition, type-I interferon upregulation, and diminished autonomic innervation of eccrine coils and arteries), linking EM to small-fiber neuropathy in non-MPN subtypes.

Clinically, secondary EM matters as a **sentinel of occult MPN**: symptoms can precede the hematologic diagnosis by a median of ~2.5 years, so all patients warrant serial blood counts and *JAK2* testing. Management is **cause-directed**: aspirin plus cytoreduction/phlebotomy for MPN; drug withdrawal for drug-induced disease; neuropathic-pain agents and sodium-channel blockers for the small-fiber/autoimmune subtypes. Epidemiologically it is rare (secondary EM incidence ≈0.2/100,000/year), female-predominant, and adult-onset, and is frequently unilateral/asymmetric — distinguishing it from the bilateral primary form.

---

## Key Findings

### 1. Disease Information — Definition, Classification, and Identifiers

Erythromelalgia is a rare neurovascular acrosyndrome defined by a triad of recurrent burning pain, erythema, and increased temperature of the extremities, worsened by heat/dependency and relieved by cooling/elevation. It is divided into a **PRIMARY** form (inherited or idiopathic; autosomal-dominant *SCN9A*/Na_v1.7 gain-of-function neuropathy, typically early-onset, bilateral, and often aspirin-unresponsive) and a **SECONDARY** form (acquired; associated with an identifiable underlying disorder). Secondary EM associated with MPN classically responds dramatically to aspirin, a feature that both aids diagnosis and points to its mechanism.

> "Secondary erythromelalgia is associated with myeloproliferative disorders, drugs (bromocriptine, calcium channel blockers), or clinical conditions such as rheumatic diseases or viral infection." — [PMID: 27639908](https://pubmed.ncbi.nlm.nih.gov/27639908/)

> "secondary, which is associated with myeloproliferative disorders-related thrombocythemia, polycythemia, collagen-vascular diseases, diabetes mellitus, peripheral neuropathy, autoimmune and infectious diseases, and use of certain medicaments" — [PMID: 15075045](https://pubmed.ncbi.nlm.nih.gov/15075045/)

> "secondary erythromelalgia associated with a myeloproliferative disease such as essential thrombocythemia often responds dramatically to aspirin therapy" — [PMID: 23862006](https://pubmed.ncbi.nlm.nih.gov/23862006/)

**Key identifiers** (finding F011):

| Resource | Identifier |
|----------|-----------|
| MeSH | D004916 (Erythromelalgia) |
| ICD-10 | I73.81 (Erythromelalgia) |
| ICD-11 | EF41.2 / peripheral vascular category |
| Orphanet | ORPHA:90026 (Erythromelalgia) |
| MONDO | MONDO:0008574 (erythromelalgia) |
| OMIM | 133020 — refers specifically to **PRIMARY** (*SCN9A*) erythermalgia; secondary EM has **no distinct OMIM entry** because it is symptomatic of the underlying disease |
| HPO | HP:0012326 (Erythromelalgia) |

**Synonyms/alternative names:** erythermalgia, Mitchell disease, acromelalgia, "red limb" syndrome; secondary EM is also termed *acquired* or *symptomatic* erythromelalgia.

**Information source type:** Knowledge is derived predominantly from **aggregated disease-level resources and clinical case series/reviews** (Michiels series, Olmsted County population studies, single-center Swedish cohort), not from a single EHR-derived patient population. Secondary EM is defined nosologically as symptomatic of an underlying disease.

### 2. Etiology — Causal Factors, Risk Factors, Gene–Environment Interactions

Secondary EM is caused by a diverse set of underlying conditions (finding F009):

1. **Myeloproliferative neoplasms** — essential thrombocythemia and polycythemia vera (most common); also reported with chronic myelogenous leukemia (CML), primary/Philadelphia-positive myelofibrosis, and myelodysplastic syndrome when platelet counts are sufficiently high.
2. **Other hematologic disease** — thrombotic thrombocytopenic purpura (TTP).
3. **Autoimmune/collagen-vascular disease** — systemic lupus erythematosus (SLE), rheumatoid arthritis, vasculitis.
4. **Small-fiber peripheral neuropathy and diabetes mellitus.**
5. **Infectious/viral illnesses.**
6. **Drugs** — calcium-channel blockers (nifedipine, verapamil, diltiazem, felodipine), bromocriptine/dopamine agonists, and others.
7. **Rarely** — paraneoplastic/solid tumors and toxins.

> "secondary, which is associated with myeloproliferative disorders-related thrombocythemia, polycythemia, collagen-vascular diseases, diabetes mellitus, peripheral neuropathy, autoimmune and infectious diseases, and use of certain medicaments... a single common pathogenetic mechanism - microvascular arteriovenous shunting" — [PMID: 15075045](https://pubmed.ncbi.nlm.nih.gov/15075045/)

> "We describe, for the first time, a patient in whom chronic myelogenous leukemia was associated with the development of erythromelalgia" — [PMID: 2643412](https://pubmed.ncbi.nlm.nih.gov/2643412/)

> "We describe a female patient in whom thrombotic thrombocytopenic purpura was associated with erythromelalgia. This has not been previously reported." — [PMID: 1613144](https://pubmed.ncbi.nlm.nih.gov/1613144/)

**Genetic risk factors:** Secondary EM itself is not germline-determined. The relevant genetic lesions are the **somatic** driver mutations of the underlying MPN (see Section 4). *JAK2*/*MPL*-mutated ET carry higher arterial thrombosis risk, which is mechanistically upstream of the acral microthrombosis in EM.

**Environmental risk factors:** Older adult age and female sex (epidemiologic associations); drug exposure (calcium-channel blockers, bromocriptine) is the principal modifiable environmental cause. Environmental **provoking** (not causal) factors are heat, exercise, and limb dependency.

**Protective factors:** No established germline protective variants or dietary/lifestyle protective factors are described. The strongest "protective" intervention is pharmacologic — low-dose aspirin abolishes the thrombocythemic form.

**Gene–environment interactions:** The clearest interaction is between the somatic *JAK2*/*CALR*/*MPL* clone (genetic) and heat/dependency (environmental provocation): the clone establishes hyperreactive thrombocytosis, while environmental heat/dependency triggers the paroxysmal acral attacks superimposed on that substrate.

### 3. Phenotypes

The core phenotype (finding F007) is paroxysmal/episodic attacks of the triad:

| Phenotype | HPO term | Notes / frequency |
|-----------|----------|-------------------|
| Severe burning pain of extremities | HP:0025267 (burning sensation); HP:0012531 (pain) | Cardinal symptom; provoked by heat/exercise/dependency |
| Erythema / red skin | HP:0000988 (skin rash); HP:0500064 (red skin) | Cardinal sign |
| Increased local skin temperature/warmth | — (warmth of acral skin) | Cardinal sign |
| Erythromelalgia (composite) | HP:0012326 | Overall term |
| Acrocyanosis | — | With progression |
| Digital ischemia / necrosis / gangrene | — | Untreated MPN-associated disease |

**Distribution:** Feet more than hands; often the ball of the foot and one or more toes or fingers. In secondary/MPN forms attacks are frequently **UNILATERAL or asymmetric** and **less intense** than in primary EM. **Provoking factors:** environmental heat, exercise, limb dependency. **Relieving factors:** cold exposure and elevation (patients immerse extremities in cold/ice water — a behavior that itself risks immersion/maceration injury).

> "characterized by attacks of severe burning pain, erythema, and warmth of the extremities, primarily the feet and, to a lesser extent, the hands. The distress is provoked by environmental heat, exercise, and dependency; it is relieved by exposure to cold and elevation of the extremity" — [PMID: 2643412](https://pubmed.ncbi.nlm.nih.gov/2643412/)

> "characterized by red, congested distal extremities and painful burning sensations, usually confined to the ball of the foot and one or more toes or fingers. If left untreated, it may progress towards acrocyanosis and even peripheral gangrene" — [PMID: 11208311](https://pubmed.ncbi.nlm.nih.gov/11208311/)

**Associated features in MPN-associated cases:** microvascular neurologic/ocular symptoms (headache, transient visual disturbance, paresthesias, TIA), pruritus, splenomegaly, and sometimes concurrent peripheral sensorimotor axonal neuropathy (documented in a *JAK2* V617F-positive PV patient, [PMID: 25674012](https://pubmed.ncbi.nlm.nih.gov/25674012/)).

**Age of onset:** adult/late-onset (secondary form). **Severity:** variable (often milder than primary). **Progression:** episodic/fluctuating, potentially digit-threatening if untreated. **Quality-of-life impact:** severe during attacks — burning pain interferes with walking, sleep, footwear, work, and social function; compulsive cooling behaviors can cause secondary immersion skin injury.

### 4. Genetic / Molecular Information

Secondary EM is **not caused by a germline mutation**. Its most common underlying disease — MPN — is driven by **somatic, mutually exclusive driver mutations** in hematopoietic stem cells (finding F004):

| Gene | HGNC/OMIM | Frequency in ET | Frequency in PV | Functional consequence |
|------|-----------|-----------------|-----------------|------------------------|
| *JAK2* (V617F) | OMIM 147796 | ~55% | >95% | Gain of function; constitutive JAK-STAT signaling |
| *CALR* (exon 9 indels) | OMIM 109091 | ~25% | rare | Gain of function; mutant CALR–MPL activation |
| *MPL* | OMIM 159530 | ~3% | rare | Gain of function; thrombopoietin-receptor activation |
| Triple-negative | — | ~17% | — | — |

Additional non-driver/clonal mutations occur: *TET2* (9–11%), *ASXL1* (7–20%), *DNMT3A* (~7%), *SF3B1* (~5%). *JAK2*/*MPL*-mutated ET is associated with higher arterial thrombosis risk — the pathophysiologic bridge to acral microthrombosis in EM.

> "Approximately 80% of patients express myeloproliferative neoplasm driver mutations (JAK2, CALR, MPL), in a mutually exclusive manner" — [PMID: 38269572](https://pubmed.ncbi.nlm.nih.gov/38269572/)

> "JAK2, CALR, and MPL mutations are the mutually exclusive 'driver' mutations in ET with respective incidences of 55%, 25%, and 3%; approximately 17% are triple-negative" — [PMID: 27991718](https://pubmed.ncbi.nlm.nih.gov/27991718/)

> "the presence of JAK2/MPL mutations has been associated with higher risk of arterial thrombosis" — [PMID: 27991718](https://pubmed.ncbi.nlm.nih.gov/27991718/)

**Somatic vs. germline origin:** entirely **somatic** for the MPN drivers; **allele frequency in population databases** is not the relevant metric (these are acquired clonal variants, not inherited polymorphisms), though clonal hematopoiesis of indeterminate potential (CHIP) with low variant allele frequency can complicate interpretation ([PMID: 38310350](https://pubmed.ncbi.nlm.nih.gov/38310350/)). **Modifier genes / epigenetics / chromosomal abnormalities:** not specifically defined for the EM phenotype itself; abnormal karyotype and spliceosome mutations modify survival of the underlying MPN.

### 5. Environmental Information

**Environmental factors / toxins:** No established environmental toxin causes secondary EM directly. **Drugs** are the principal non-hematologic environmental cause — calcium-channel blockers (nifedipine, verapamil, diltiazem, felodipine) and bromocriptine/dopamine agonists (F009). **Lifestyle factors:** none causal beyond drug exposure; heat, exercise, and dependency are provocative triggers, not chronic risk factors. **Infectious agents:** viral/infectious illnesses are listed among secondary causes (F001/F009), but no single specified pathogen is established as causal; EM in this setting is best regarded as a reactive/para-infectious phenomenon.

### 6. Mechanism / Pathophysiology

#### Ordered causal chain — MPN-associated (thrombocythemic) secondary EM

1. A **somatic driver mutation** (*JAK2* V617F, *CALR*, or *MPL*) arises in a hematopoietic stem cell → **leads to** constitutive JAK2–STAT signaling and clonal myeloproliferation.
2. Clonal myeloproliferation **results in** thrombocytosis with **hyperreactive platelets** (essential thrombocythemia, or PV with high platelet counts).
3. Hyperreactive platelets, via **platelet cyclooxygenase-1 (COX-1)**, **lead to** increased thromboxane A2 generation and platelet activation in acral end-arterioles.
4. Platelet COX/thromboxane activity **results in** **arteriolar inflammation and fibromuscular intimal proliferation** of dermal/subcutaneous arterioles.
5. This **leads to** **platelet-rich thrombotic occlusion** of the end-arterial microvasculature (skin biopsy: arteriolar inflammation, intimal proliferation, platelet thrombi; shortened platelet survival; elevated β-thromboglobulin, PF4, thrombomodulin; increased urinary thromboxane B2).
6. Microvascular occlusion **results in** localized **acral ischemia** → **branch point:** experienced as **burning pain + erythema + warmth** (the EM triad); if severe/untreated → **acrocyanosis → digital necrosis/gangrene**.
7. **COX inhibition by aspirin/indomethacin** interrupts step 3 → complete, lasting symptom relief and normalization of platelet-activation markers (whereas sodium salicylate, dipyridamole, sulfinpyrazone, ticlopidine, and coumadin do NOT — establishing COX/thromboxane dependence). Cytoreduction that normalizes platelet count removes step 2 → remission; relapse recurs symptoms.

> "Local platelet consumption in erythromelalgic areas became evident by the demonstration of arteriolar fibromuscular intimal proliferation and occlusions by platelet-rich thrombi in skin biopsies, by the findings of shortened platelet survival times, significant higher levels of platelet activation markers beta-thromboglobulin, thrombomoduline and increased urinary thromboxane B2 excretion" — [PMID: 12781799](https://pubmed.ncbi.nlm.nih.gov/12781799/)

> "is caused by platelet cyclo-oxygenase-mediated arteriolar inflammation, fibromuscular intimal proliferation without and with occlusive thrombosis by platelet-rich thrombi in the end-arterial microvasculature" — [PMID: 16510297](https://pubmed.ncbi.nlm.nih.gov/16510297/)

> "Skin punch biopsy samples taken from the affected areas showed typical arteriolar inflammation, fibromuscular intima proliferation, and thrombotic occlusions." — [PMID: 3977194](https://pubmed.ncbi.nlm.nih.gov/3977194/)

#### Alternative / complementary causal chain — immune-mediated microvascular injury & dysautonomia (non-MPN subtypes)

1. An immune trigger (autoimmune disease such as SLE, or idiopathic dysimmunity) → **leads to** complement activation with **microvascular C5b-9 (membrane attack complex) deposition** on dermal endothelium.
2. Endothelial injury with **type-I interferon upregulation** **results in** microvascular dysfunction.
3. Concurrent **diminished autonomic innervation of eccrine coils and arteries** (CD56 evidence; mirroring small-fiber neuropathy) **leads to** dysregulated vasomotor control → maldistributed skin perfusion.
4. This **results in** the same clinical triad, but is **aspirin-unresponsive** and instead treated as neuropathic/autoimmune disease. (Mechanistic details are demonstrated in a small dermatopathology series and are partly *inferred*.)

> "Biopsies showed superficial vascular ectasia in association with microvascular C5b-9 and variable upregulation of type I interferon expression in endothelial cells. CD56 stain revealed diminished autonomic innervation of the eccrine coil and arteries, mirroring similar autonomic denervation seen in small fiber neuropathy." — [PMID: 39846717](https://pubmed.ncbi.nlm.nih.gov/39846717/)

> "Histology commonly shows capillary proliferation, swelling of endothelial cells, perivascular edema, and chronic inflammation with sparse lymphocytic infiltrate." — [PMID: 23334520](https://pubmed.ncbi.nlm.nih.gov/23334520/)

**Unifying hypothesis:** Ljubojević et al. proposed a **single common pathogenetic mechanism** across etiologies — microvascular **arteriovenous shunting** with maldistributed skin perfusion producing tissue hypoxia despite visible erythema and warmth ([PMID: 15075045](https://pubmed.ncbi.nlm.nih.gov/15075045/)).

**Ontology suggestions:**
- **GO biological processes:** platelet activation (GO:0030168), platelet aggregation (GO:0070527), blood coagulation (GO:0007596), prostaglandin biosynthesis / cyclooxygenase pathway (GO:0006693), inflammatory response (GO:0006954), complement activation (GO:0006956), type I interferon signaling (GO:0060337).
- **CL cell types:** platelet (CL:0000233), blood vessel endothelial cell (CL:0000115), smooth muscle cell (CL:0000192).
- **CHEBI:** thromboxane B2 (CHEBI:28728), acetylsalicylic acid/aspirin (CHEBI:15365), prostaglandin.

#### Mechanism schematic

```
 Somatic JAK2/CALR/MPL mutation (HSC)
            |  constitutive JAK-STAT
            v
   Clonal thrombocytosis (ET / PV)
            |  hyperreactive platelets
            v
   Platelet COX-1 -> thromboxane A2  ----(aspirin/indomethacin block here)
            |
            v
 Arteriolar inflammation + fibromuscular intimal proliferation
            |
            v
 Platelet-rich microthrombosis of acral end-arterioles
            |
            v
    Acral ischemia  --> BURNING PAIN + ERYTHEMA + WARMTH
            |
            +--> (untreated) acrocyanosis --> digital necrosis / gangrene

 [Parallel non-MPN route]
 Autoimmune/idiopathic trigger -> endothelial C5b-9 + type I IFN
   + autonomic denervation (eccrine/arteries) -> maldistributed
   perfusion / AV shunting -> same triad (aspirin-unresponsive)
```

### 7. Anatomical Structures Affected

**Organ/system level (F010):** primarily the **skin of acral extremities** and the **peripheral (microvascular) cardiovascular system**; the **peripheral/autonomic nervous system** is involved in neuropathic subtypes.

**Localization (UBERON):** feet (UBERON:0002387) > hands (UBERON:0002398); toes (UBERON:0009551) and fingers (UBERON:0002389); ball/sole of foot; distal/acral. Affected tissue: dermal/subcutaneous **arterioles** (UBERON:0001980) and capillaries.

**Lateralization:** secondary/MPN forms are frequently **unilateral or asymmetric** (versus bilateral in primary EM).

**Cell level (CL):** vascular endothelial cells (CL:0000115), platelets (CL:0000233) forming intraluminal thrombi; arteriolar smooth-muscle/intimal cells; eccrine sweat glands and their small autonomic (C-fiber) innervation in the dysautonomia/SFN subtype.

**Subcellular level:** platelet **cyclooxygenase (COX-1)** enzymatic activity; endothelial **complement (C5b-9)** and **type-I interferon** responses are the key molecular loci.

**Secondary organ involvement/complications:** acrocyanosis, digital ischemia, ulceration, gangrene; in MPN patients, concurrent cerebral/ocular/coronary microvascular territories (headache, visual disturbance, TIA).

> "Skin punch biopsy samples taken from the affected areas showed typical arteriolar inflammation, fibromuscular intima proliferation, and thrombotic occlusions." — [PMID: 3977194](https://pubmed.ncbi.nlm.nih.gov/3977194/)

> "CD56 stain revealed diminished autonomic innervation of the eccrine coil and arteries" — [PMID: 39846717](https://pubmed.ncbi.nlm.nih.gov/39846717/)

### 8. Temporal Development

**Onset:** adult/late-onset; often **insidious** in relation to the underlying MPN. In MPN-associated EM, symptoms **preceded** the diagnosis of the myeloproliferative disease by a **median of ~2.5 years** and can be the presenting manifestation of ET/PV (F008).

**Progression:** episodic/fluctuating course; untreated MPN-EM may progress to acrocyanosis and peripheral gangrene. **Duration:** chronic while the underlying disease persists; resolves when the cause is treated.

**Remission patterns:** treatment-induced remission is the rule — MPN-EM responds immediately to aspirin and remits with platelet-count normalization; drug-induced EM resolves on drug withdrawal. Symptoms **recur** with MPN relapse or aspirin withdrawal ([PMID: 22844295](https://pubmed.ncbi.nlm.nih.gov/22844295/): EM developed within two weeks of aspirin withdrawal and improved within two weeks of restarting).

**Critical period / window of opportunity:** because idiopathic-appearing EM may be an early clonal MPN marker, **periodic blood counts** are recommended so that an abnormal hemoglobin/WBC/platelet count or immature cells prompts evaluation.

> "symptoms of erythromelalgia preceded the onset of a myeloproliferative disease by a median of 2 1/2 years. Therefore, all patients with erythromelalgia should be monitored with periodic blood cell counts" — [PMID: 2643412](https://pubmed.ncbi.nlm.nih.gov/2643412/)

> "Her erythromelalgia immediately disappeared following interventional therapy along with aspirin." — [PMID: 15750823](https://pubmed.ncbi.nlm.nih.gov/15750823/)

### 9. Inheritance and Population (Epidemiology)

Secondary EM is **rare, female-predominant, and adult-onset** (F002). The population-based Olmsted County study (Reed & Davis) reported an overall age/sex-adjusted EM incidence of **1.3/100,000/year** (95% CI 0.8–1.7), split into **primary EM 1.1** and **secondary EM 0.2/100,000/year**. Female incidence (2.0) exceeded male (0.6) per 100,000. The Swedish single-center study (Alhadad) found incidence 0.36/100,000/year, median age 49 (IQR 34–68), 70% women, and a mean diagnostic delay of 4.5 years; 3/27 developed intra-abdominal cancer.

> "The incidence of primary and secondary erythromelalgia was 1.1 (0.7-1.5) and 0.2 (0.02-0.4) per 100,000 people per year, respectively." — [PMID: 18713229](https://pubmed.ncbi.nlm.nih.gov/18713229/)

> "we clinically identified 27 patients with EM. Median age was 49 [IQR (34 - 68)] years, 19 (70 %) were women" — [PMID: 22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/)

**Inheritance pattern:** secondary EM is **acquired/non-heritable**. The underlying MPN driver mutations are **somatic** (not inherited); there is no Mendelian inheritance, penetrance, anticipation, founder effect, consanguinity role, or carrier frequency applicable to secondary EM. (These concepts apply only to primary *SCN9A* EM.)

**Population demographics:** female predominance is confirmed across dermatologic epidemiology ([PMID: 27009931](https://pubmed.ncbi.nlm.nih.gov/27009931/)). No specific ethnic/geographic clustering is established for secondary EM; distribution follows that of the underlying MPN/autoimmune diseases. **Sex ratio:** roughly 2–2.3:1 female:male. **Age distribution:** predominantly middle-aged and older adults.

### 10. Diagnostics

**Diagnosis is clinical** — the triad of burning pain, erythema, and warmth; heat/dependency provokes and cold/elevation relieves. Adjuncts include **infrared thermography, laser Doppler flowmetry, and cold-provocation testing**. The essential task is to **identify the secondary cause** (F005):

| Test | Purpose |
|------|---------|
| Complete blood count (CBC) with differential + peripheral smear | Detect thrombocytosis/erythrocytosis/leukocytosis (MPN) |
| *JAK2* V617F mutation testing (then *CALR*, *MPL* if negative) | Confirm MPN driver |
| Bone marrow biopsy | Confirm ET/PV/prefibrotic myelofibrosis |
| ANA | Screen for SLE/autoimmune cause |
| TSH | Thyroid disease |
| Small-fiber neuropathy testing (skin biopsy for intraepidermal nerve fiber density) | Neuropathic subtype |
| Screen for drugs / malignancy | Drug-induced and paraneoplastic causes |
| Skin punch biopsy | Arteriolar thrombosis (MPN), C5b-9/IFN, autonomic denervation |

> "For erythermalgia, a blood count and even a search for JAK2 mutation are required. A thryoid-stimulating hormon assay, a test for antinuclear antibodies, and a search for small fiber neuropathy are also performed." — [PMID: 35835622](https://pubmed.ncbi.nlm.nih.gov/35835622/)

**Biomarkers / laboratory abnormalities:** thrombocytosis (platelets ≥450 ×10⁹/L; [PMID: 42101597](https://pubmed.ncbi.nlm.nih.gov/42101597/)), erythrocytosis, elevated platelet-activation markers (β-thromboglobulin, PF4, thrombomodulin), increased urinary thromboxane B2.

**Differential diagnosis (F011):** Raynaud phenomenon (color change to white/blue, cold-induced — opposite triggers), complex regional pain syndrome, peripheral neuropathy, cellulitis, acrocyanosis, chilblains/pernio, Fabry disease acroparesthesias, gout, and **primary (*SCN9A*) EM**. The distinguishing feature of EM is **heat/dependency provocation and cold/elevation relief**.

> "Raynaud's syndrome and Raynaud's mimickers, especially painful Raynaud's mimickers, can prove a diagnostic challenge" — [PMID: 38704280](https://pubmed.ncbi.nlm.nih.gov/38704280/)

**Genetic testing:** for the **underlying MPN**, targeted *JAK2*/*CALR*/*MPL* testing (allele-specific PCR/NGS) is standard; WGS/WES are not routinely required. Note that low-VAF *JAK2* may reflect CHIP, and the dominant driver (e.g., *CALR*) determines phenotype ([PMID: 38310350](https://pubmed.ncbi.nlm.nih.gov/38310350/)). No genetic testing is indicated for the EM phenotype itself in the secondary form.

### 11. Outcome / Prognosis

**Overall EM mortality is low and not directly disease-attributable** (Alhadad); however, the **underlying disease drives prognosis**. Untreated MPN-associated EM can progress to acrocyanosis and peripheral gangrene (digit-threatening). Prognosis is **favorable when the cause is treated**: aspirin gives immediate relief and cytoreduction produces remission; drug-induced EM resolves on withdrawal (F008).

The underlying MPN carries its own morbidity/mortality: PV median survival 14.1–27.6 years, with arterial thrombosis in 16% and venous thrombosis in 7% at/before diagnosis, ~12.7% progressing to myelofibrosis and ~6.8% to acute myeloid leukemia ([PMID: 39556352](https://pubmed.ncbi.nlm.nih.gov/39556352/)); ET median survival ~18 years with leukemic transformation <1% at 10 years ([PMID: 32974939](https://pubmed.ncbi.nlm.nih.gov/32974939/)). Thus EM's chief prognostic significance is as a **herald of occult MPN and its thrombotic/leukemic risk**.

**Complications:** digital ischemia, ulceration, gangrene, immersion/maceration skin injury from compulsive cooling; systemic thrombosis (arterial/venous) from the underlying MPN. **Prognostic factors:** platelet count/response to aspirin, presence and control of the underlying MPN, *JAK2*/*MPL* status (arterial thrombosis risk).

### 12. Treatment

Treatment is **cause-directed** (F005), with NCIT term suggestions:

| Clinical scenario | Intervention | NCIT suggestion |
|-------------------|--------------|-----------------|
| MPN-associated EM | **Low-dose aspirin** (dramatic, near-pathognomonic relief) | NCIT:C287 (Aspirin) |
| MPN cytoreduction | **Hydroxyurea** (first-line) | NCIT:C512 (Hydroxyurea) |
| MPN cytoreduction (younger pts) | **Interferon-α / pegylated interferon** | NCIT:C20515 (Interferon Alpha) |
| PV | **Therapeutic phlebotomy** (goal hematocrit <45%) | NCIT:C15325 (Phlebotomy) |
| PV, HU-intolerant/resistant | **Ruxolitinib** (JAK inhibitor) | NCIT:C79809 (Ruxolitinib) |
| Drug-induced EM | **Withdraw offending agent** | — |
| Small-fiber/autoimmune EM | Neuropathic-pain agents (**gabapentin, amitriptyline**), **sodium-channel blockers (mexiletine, lidocaine, carbamazepine)**; treat autoimmune disease | NCIT:C1367 (Gabapentin); NCIT:C614 (Lidocaine); NCIT:C1665 (Mexiletine) |
| Supportive (all) | Cooling, elevation, heat/dependency avoidance | — |

> "Aspirin is a useful treatment of erythromelagia associated with myeloproliferative disorders. Treatment of primary erythromelalgia is difficult, individualized, with sodium channel blockers such as lidocaine, carbamazepine and mexiletine." — [PMID: 27639908](https://pubmed.ncbi.nlm.nih.gov/27639908/)

The aspirin response is so characteristic that MPN cytoreductive guidelines (ET/PV updates, [PMID: 38269572](https://pubmed.ncbi.nlm.nih.gov/38269572/), [PMID: 27561316](https://pubmed.ncbi.nlm.nih.gov/27561316/)) routinely incorporate low-dose aspirin. In one illustrative case, reversal of thrombotic complications was achieved by aspirin and platelet reduction, "and not by coumadin" ([PMID: 16510297](https://pubmed.ncbi.nlm.nih.gov/16510297/)). **Pharmacogenomics:** *JAK2*/*MPL* status guides thrombosis-risk stratification and cytoreduction decisions. **Personalized medicine:** treatment is genotype-/cause-guided rather than one-size-fits-all — the same clinical triad requires opposite drug classes (aspirin vs. sodium-channel blockers) depending on etiology.

### 13. Prevention

Because secondary EM is **acquired/symptomatic, no primary prevention exists** (F011). Prevention is framed at secondary and tertiary levels:

- **Secondary prevention:** early recognition of EM as a **sentinel of occult MPN**, with **serial CBC + *JAK2* testing**, and treatment of thrombocytosis/erythrocytosis.
- **Tertiary prevention:** **aspirin ± cytoreduction/phlebotomy** to prevent digital necrosis and macrovascular thrombosis; **avoid provoking heat/dependency**; for drug-induced disease, **avoid/withdraw the culprit drug**.
- **Genetic counseling / carrier screening / immunization / public-health interventions:** **not applicable** (no germline/heritable or infectious-transmissible basis).

### 14. Other Species / Natural Disease

**No naturally occurring secondary EM is described in companion animals or wildlife** (OMIA); the disease is essentially **human** (F011). Orthologous genes for the underlying MPN drivers exist in model species (mouse *Jak2*, *Calr*, *Mpl*; NCBI Gene IDs available), enabling comparative study of the MPN substrate but not of the EM phenotype per se. There is **no zoonotic potential** and no cross-species transmission.

### 15. Model Organisms

**No validated animal model of SECONDARY erythromelalgia exists** (F011). Available models address only components of the disease:

| Model | What it captures | Limitation for secondary EM |
|-------|------------------|-----------------------------|
| Transgenic/knock-in *SCN9A*/Na_v1.7 gain-of-function mice; patient iPSC-derived sensory neurons | **Primary** EM pain physiology | Models channelopathy, not acquired microvascular disease |
| *JAK2* V617F knock-in mice | Thrombocytosis/thrombosis of the underlying MPN | EM (acral burning/erythema) has **not been specifically scored** |

Thus the field lacks a model that reproduces the platelet-COX-mediated acral microthrombosis or the immune/dysautonomic microvascular injury of human secondary EM — a significant translational gap.

---

## Mechanistic Model / Interpretation

Secondary EM is best understood as a **final common acral microvascular phenotype reached by at least two distinct upstream routes**:

1. **The thrombocythemic (MPN) route** is the best-established and mechanistically the most complete: a somatic *JAK2*/*CALR*/*MPL* clone → hyperreactive thrombocytosis → platelet COX-1/thromboxane-driven arteriolar inflammation and platelet-rich microthrombosis → acral ischemia. The therapeutic "experiment of nature" — complete relief with COX inhibitors (aspirin/indomethacin) but not with anticoagulants (coumadin), antiplatelet agents acting by other mechanisms (ticlopidine, dipyridamole), or non-acetylated salicylate — pins the mechanism firmly on **platelet cyclooxygenase**. This is a distinct, aspirin-responsive **arterial thrombophilia**.

2. **The immune/dysautonomic route** (autoimmune, idiopathic, small-fiber-neuropathy-associated) involves **complement (C5b-9) and type-I interferon-mediated endothelial injury** plus **autonomic denervation** of eccrine glands and arterioles, producing maldistributed perfusion/arteriovenous shunting. This route is aspirin-**unresponsive** and treated as neuropathic/autoimmune disease.

Both converge on Ljubojević's proposed unifying lesion — **microvascular arteriovenous shunting with tissue hypoxia despite visible hyperemia** — reconciling the paradox of a red, warm, yet ischemic and painful extremity. The unifying clinical message is that **the triad is a syndrome, not a diagnosis**: identifying and treating the upstream cause is both diagnostic confirmation and definitive therapy.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|------|------------------|------|
| [12781799](https://pubmed.ncbi.nlm.nih.gov/12781799/) | Platelet-mediated microvascular inflammation and thrombosis in thrombocythemia | Core biochemical/histologic evidence for COX/thromboxane mechanism |
| [3977194](https://pubmed.ncbi.nlm.nih.gov/3977194/) | EM caused by platelet-mediated arteriolar inflammation | Histopathology of arteriolar thrombosis |
| [16510297](https://pubmed.ncbi.nlm.nih.gov/16510297/) | Reversal by aspirin, platelet reduction, not coumadin | Establishes COX/aspirin dependence |
| [39846717](https://pubmed.ncbi.nlm.nih.gov/39846717/) | Cutaneous pathology of EM | Complement/IFN/dysautonomia mechanism (non-MPN) |
| [23334520](https://pubmed.ncbi.nlm.nih.gov/23334520/) | Secondary EM, unusual histology | Typical histopathology |
| [2643412](https://pubmed.ncbi.nlm.nih.gov/2643412/) | EM and myeloproliferative disorders | Phenotype, ~2.5-yr lead time, CML association, monitoring |
| [11208311](https://pubmed.ncbi.nlm.nih.gov/11208311/) | EM — thrombotic complication in MPD | Localization and progression to gangrene |
| [15075045](https://pubmed.ncbi.nlm.nih.gov/15075045/) | Erythromelalgia (review) | Etiologic spectrum + AV-shunting unifying mechanism |
| [1613144](https://pubmed.ncbi.nlm.nih.gov/1613144/) | EM in TTP | TTP as secondary cause |
| [38269572](https://pubmed.ncbi.nlm.nih.gov/38269572/) | ET 2024 update | MPN driver mutations (~80% JAK2/CALR/MPL) |
| [27991718](https://pubmed.ncbi.nlm.nih.gov/27991718/) | PV/ET 2017 update | Driver frequencies; JAK2/MPL & arterial thrombosis |
| [18713229](https://pubmed.ncbi.nlm.nih.gov/18713229/) | Incidence, Olmsted County | Population-based incidence (secondary 0.2/100k/yr) |
| [22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/) | Incidence, Sweden | Age/sex distribution, diagnostic delay |
| [35835622](https://pubmed.ncbi.nlm.nih.gov/35835622/) | Paroxysmal vascular acrosyndromes | Diagnostic workup |
| [27639908](https://pubmed.ncbi.nlm.nih.gov/27639908/) | EM diagnosis & therapy | Cause-directed treatment; drug causes |
| [23862006](https://pubmed.ncbi.nlm.nih.gov/23862006/) | Secondary EM case report | Aspirin responsiveness |
| [15750823](https://pubmed.ncbi.nlm.nih.gov/15750823/) | EM in ET / renovascular HTN | Rapid treatment response |
| [22844295](https://pubmed.ncbi.nlm.nih.gov/22844295/) | EM on aspirin withdrawal | Recurrence with aspirin withdrawal |
| [38704280](https://pubmed.ncbi.nlm.nih.gov/38704280/) | Painful Raynaud's mimics | Differential diagnosis |
| [25674012](https://pubmed.ncbi.nlm.nih.gov/25674012/) | Burning feet in PV | Concurrent axonal neuropathy in JAK2+ PV |
| [39556352](https://pubmed.ncbi.nlm.nih.gov/39556352/) | PV review | Underlying MPN prognosis; EM frequency 5.3% in PV |
| [38310350](https://pubmed.ncbi.nlm.nih.gov/38310350/) | Multiple driver mutations in ET | CHIP vs. dominant driver interpretation |
| [42101597](https://pubmed.ncbi.nlm.nih.gov/42101597/) | Thrombocytosis review | Thrombocytosis definition/workup |
| [32974939](https://pubmed.ncbi.nlm.nih.gov/32974939/) | PV/ET 2021 update | Survival, transformation rates |
| [27561316](https://pubmed.ncbi.nlm.nih.gov/27561316/) | How I treat ET | Aspirin + cytoreduction strategy |

**Consistency:** Multiple independent series (Michiels; Olmsted County; Swedish cohort; ET/PV guideline updates) converge on the same picture. The classic thrombocythemic mechanism is strongly and repeatedly supported; the immune/dysautonomic mechanism rests on a smaller, more recent evidence base (single dermatopathology series) and should be regarded as an emerging but not yet fully validated complementary model.

---

## Limitations and Knowledge Gaps

- **No dedicated secondary-EM animal model.** *JAK2* V617F mice reproduce the MPN substrate but EM has not been scored; there is no model of the immune/dysautonomic route.
- **Immune/complement mechanism is based on a single small series** (9 patients, [PMID: 39846717](https://pubmed.ncbi.nlm.nih.gov/39846717/)) and requires independent replication with quantitative endpoints.
- **Epidemiologic estimates are geographically narrow** (Olmsted County, single Swedish center); global prevalence, ethnic distribution, and secondary-cause proportions are poorly characterized.
- **No prospective controlled trials** define optimal therapy for non-MPN subtypes; treatment recommendations are extrapolated from case series.
- **Frequency data for individual phenotypic features** (e.g., proportion unilateral, proportion progressing to gangrene) in secondary EM specifically are sparse.
- **The AV-shunting unifying hypothesis** remains conceptual and unproven at the tissue level for all subtypes.
- **Molecular profiling (transcriptomics/proteomics/metabolomics) of EM-affected skin** is essentially absent beyond immunohistochemistry.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective natural-history cohort** of idiopathic-appearing EM with serial CBC + *JAK2*/*CALR*/*MPL* testing to quantify the rate and lead time of occult MPN conversion and refine the monitoring interval.
2. **Replicate the complement/interferon/dysautonomia findings** in an independent, larger biopsy cohort with quantitative C5b-9, type-I IFN signature scoring, and intraepidermal nerve-fiber-density measurement, stratified by MPN vs. non-MPN etiology.
3. **Develop a secondary-EM model** by scoring acral thermal/nociceptive phenotypes and skin microvascular thrombosis in *JAK2* V617F knock-in mice ± aspirin, testing whether COX inhibition reverses acral pathology.
4. **Aspirin-response as a diagnostic biomarker study:** formally test the sensitivity/specificity of a dramatic aspirin response for detecting underlying MPN.
5. **Skin single-cell/spatial transcriptomics** of EM-affected vs. unaffected acral skin to map the endothelial, platelet, smooth-muscle, and autonomic-nerve contributions and validate the two-route model.
6. **Registry-based epidemiology** across multiple regions to establish global incidence, secondary-cause proportions, and demographic distribution.
7. **Trial of complement- or interferon-directed therapy** in refractory, aspirin-unresponsive, immune-associated EM, guided by biopsy biomarkers.

---

*Report compiled from 11 confirmed findings across 5 investigation iterations and 35 reviewed papers. Evidence sources are predominantly human clinical case series, population-based epidemiology, and disease-level reviews; mechanistic claims are supported by skin-biopsy histopathology, platelet biochemistry, and pharmacologic-response data.*


## Artifacts

- [OpenScientist final report](Secondary_Erythromelalgia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Secondary_Erythromelalgia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 26 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:22247059` *(abstract only)*: "we clinically identified 27 patients with EM. Median age was 49 [IQR (34 - 68)] years, 19 (70 %) were women"
  - closest text in source: "we clinically identified 27 patients with EM. Median age was 49 [IQR (34 - 68)] years, 19 (70 %) were women"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008574` (1 mention) - the report calls it "erythromelalgia"; MONDO calls it **obsolete Tl antigen**
- `HP:0012326` (2 mentions) - the report calls it "Erythromelalgia", "Erythromelalgia (composite)"; HP calls it **Abnormal celiac artery morphology**
- `NCIT:C512` (1 mention) - the report calls it "Hydroxyurea"; NCIT calls it **Free Radical**
- `NCIT:C15325` (1 mention) - the report calls it "Phlebotomy"; NCIT calls it **Skin Transplantation**
- `NCIT:C79809` (1 mention) - the report calls it "Ruxolitinib"; NCIT calls it **Defactinib**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0008574` (obsolete Tl antigen) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030168` (1 mention) - the report calls it "GO biological processes:** platelet activation"; GO calls it **platelet activation**
- `CL:0000233` (2 mentions) - the report calls it "CL cell types:** platelet"; CL calls it **platelet**, and lists "blood platelet" among its other names
- `CHEBI:28728` (1 mention) - the report calls it "CHEBI:** thromboxane B2"; CHEBI calls it **thromboxane B2**
- `NCIT:C20515` (1 mention) - the report calls it "Interferon Alpha"; NCIT calls it **Interleukin-13**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012326` - called "Erythromelalgia", "Erythromelalgia (composite)"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
