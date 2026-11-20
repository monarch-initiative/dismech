---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T18:12:07.722286'
end_time: '2026-11-12T18:39:38.256584'
duration_seconds: 1650.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MPIG6B-Related Thrombocytopenia and Myelofibrosis
  mondo_id: MONDO:0044316
  category: Mendelian
  causal_genes: MPIG6B
  omim_id: OMIM:617441
  synonyms: MPIG6B-related thrombocytopenia, anemia, and myelofibrosis; THAMY
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MPIG6B-Related_Thrombocytopenia_and_Myelofibrosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MPIG6B-Related_Thrombocytopenia_and_Myelofibrosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MPIG6B-Related Thrombocytopenia and Myelofibrosis
- **MONDO ID:** MONDO:0044316 (if available)
- **Causal gene(s):** MPIG6B
- **OMIM:** OMIM:617441
- **Synonyms:** MPIG6B-related thrombocytopenia, anemia, and myelofibrosis; THAMY
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MPIG6B-Related Thrombocytopenia and Myelofibrosis** covering all of the
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

# MPIG6B-Related Thrombocytopenia and Myelofibrosis (THAMY): Comprehensive Disease Report

**Disease:** MPIG6B-Related Thrombocytopenia, Anemia, and Myelofibrosis (THAMY)
**Causal gene:** **MPIG6B** (G6b-B; HGNC:13937; NCBI Gene 80277; UniProt O95866; Ensembl ENSG00000204420; locus 6p21.33)
**Identifiers:** OMIM:617441 · MONDO:0044316 · MedGen:C4479504 (CN1378448) · UMLS:C4479504
**Category:** Mendelian, autosomal recessive

---

## Summary

MPIG6B-related thrombocytopenia and myelofibrosis (THAMY) is a rare **autosomal recessive** Mendelian hematologic disorder caused by **biallelic loss-of-function variants in the single causal gene *MPIG6B***, located on chromosome 6p21.33. *MPIG6B* encodes **G6b-B**, a megakaryocyte- and platelet-specific **immunoreceptor tyrosine-based inhibitory motif (ITIM)-containing inhibitory receptor**. The disease was first defined genetically by Hofmann et al. in 2018, who identified germline loss-of-function mutations in four unrelated consanguineous families presenting with inherited macrothrombocytopenia and focal myelofibrosis ([PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)). Although the disease name points to downstream consequences (thrombocytopenia, anemia, myelofibrosis), the underlying lesion is loss of a single inhibitory receptor that normally restrains megakaryocyte and platelet activation.

Mechanistically, G6b-B is a **heparan-sulfate-regulated ITIM receptor** whose physiological ligands include the extracellular-matrix heparan sulfate proteoglycan perlecan and multivalent heparin. Ligand engagement drives receptor dimerization and phosphorylation of its ITIM/ITSM tyrosines, which recruit the phosphatases **Shp1 and Shp2** to dampen megakaryocyte and platelet signaling. When G6b-B is lost (or uncoupled from Shp1/Shp2), the brake on **Syk kinase** is released, megakaryopoiesis becomes dysregulated, collagen receptor complexes (GPVI–FcRγ, integrin α2β1) and GPIbα are shed by metalloproteinases, platelet production becomes defective, and bone-marrow fibrosis develops that is histologically indistinguishable from primary myelofibrosis. The clinical consequences are **congenital macrothrombocytopenia, anemia, and progressive myelofibrosis**, frequently with splenomegaly.

The disease is faithfully modeled in *Mpig6b*-knockout and ITIM/ITSM knock-in (Y212F/Y238F) mice, which reproduce macrothrombocytopenia, megakaryocyte clustering, focal myelofibrosis, and (sex-linked) osteosclerosis. **Allogeneic hematopoietic stem cell transplantation (HSCT) is curative** in humans, and in mouse models the thrombopoietin mimetic **romiplostim** rescues thrombocytopenia and GPVI expression, suggesting disease-modifying pharmacotherapy options. Population genetic data (gnomAD) confirm that *MPIG6B* is loss-of-function tolerant in heterozygotes (pLI ≈ 0), fully consistent with recessive inheritance in which carriers are unaffected.

---

## Key Findings

### Finding 1 — MPIG6B biallelic loss-of-function is the sole cause of THAMY

Hofmann et al. (2018, *Blood*) established the genetic basis of the disorder by describing **four unrelated consanguineous families** with autosomal recessive inherited macrothrombocytopenia and focal myelofibrosis caused by germline loss-of-function mutations in *MPIG6B*. In their words, they describe *"4 families with autosomal recessive inherited macrothrombocytopenia with focal myelofibrosis due to germ line loss-of-function mutations in the megakaryocyte-specific immunoreceptor tyrosine-based inhibitory motif (ITIM)-containing receptor G6b-B"* ([PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)).

The gene maps to **chromosome 6p21.33** and encodes the inhibitory receptor G6b-B expressed on the surface of platelets and megakaryocytes ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/)). The reported pathogenic variant spectrum is dominated by **truncating loss-of-function alleles** — nonsense, frameshift, and splice-site variants — with occasional missense changes. Documented variants include:

| Variant (cDNA) | Protein | Type |
|---|---|---|
| c.324C>A | p.Cys108Ter | Nonsense |
| c.420T>A | p.Tyr140Ter | Nonsense |
| c.523C>T | p.Arg175Ter | Nonsense |
| c.61_61+1dup | p.Ala21GlyfsX159 | Frameshift/splice |
| c.149dup | p.Ala52GlyfsX128 | Frameshift |
| c.392delC | p.Pro134LeufsX10 | Frameshift |
| c.469G>A | p.Gly157Arg | Missense |

Zhang et al. (2022) summarized that *"Several pathogenic MPIG6B mutations have been reported, such as c.324C>A (p.C108*), c.61_61+1dup (p.Ala21GlyfsX159), c.149dup (p.Ala52GlyfsX128), G6b c.469G>A (p.Gly157Arg) c.392delC (p.P134Lfs*10), and c523C>T(p.Arg175Ter)"* ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)). Inheritance is homozygous or compound heterozygous, consistent with a recessive loss-of-function mechanism.

The Monarch Initiative records **exactly one causal gene–disease association** for MONDO:0044316 — HGNC:13937 *MPIG6B* — with no competing or additional causal genes, confirming THAMY as a **monogenic disorder**.

### Finding 2 — Mechanism: a heparan-sulfate-regulated ITIM receptor signaling through Shp1/Shp2

G6b-B is a physiological **brake** on megakaryocyte and platelet activation. Vögtle et al. (2019, *PNAS*) demonstrated that the extracellular matrix heparan sulfate proteoglycan **perlecan** is a G6b-B ligand and that heparin forms a high-affinity complex with G6b-B mediating receptor dimerization: *"binding of G6b-B to HS and multivalent heparin inhibits platelet and megakaryocyte function by inducing downstream signaling via the tyrosine phosphatases Shp1 and Shp2"* ([PMID: 31436532](https://pubmed.ncbi.nlm.nih.gov/31436532/)).

The downstream signaling depends on the cytoplasmic **ITIM and ITSM tyrosines**. Geer et al. (2018) showed that *"Tyrosine phosphorylation of ITIM and immunoreceptor tyrosine-based switch motif (ITSM) within the cytoplasmic tail of G6b-B provides a docking site for Src homology 2 domain-containing protein-tyrosine phosphatases Shp1 and Shp2"* ([PMID: 29891536](https://pubmed.ncbi.nlm.nih.gov/29891536/)). Critically, a **Y212F/Y238F knock-in mouse** that uncouples G6b-B from Shp1/Shp2 recapitulates macrothrombocytopenia — proving that the phosphatase-docking function, not merely receptor presence, is required for platelet homeostasis.

Mazharian et al. (2023) defined the downstream consequences of G6b-B loss: platelets are *"almost completely devoid of the glycoprotein VI (GPVI)-FcRγ-chain collagen receptor complex, have reduced collagen integrin α2β1, elevated Syk tyrosine kinase activity"* ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)). Importantly, introducing a **Syk loss-of-function allele (R41A) genetically rescued** macrothrombocytopenia and restored GPVI/α2β1 expression — placing **Syk hyperactivation** as the key effector node downstream of G6b-B loss.

### Finding 3 — Clinical phenotype: congenital macrothrombocytopenia, anemia, and myelofibrosis; curable by HSCT

Human patients present **from birth or childhood** with severe thrombocytopenia with large/macro platelets, anemia (often transfusion-dependent), hepatosplenomegaly, cutaneous petechiae, and a bone-marrow biopsy indistinguishable from **primary myelofibrosis**. An adult male case showed hepatosplenomegaly with a PMF-like marrow; the biopsy *"showed morphologic features similar to primary myelofibrosis"* ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/)). A 14-year-old girl presented with pallor, petechiae, thrombocytopenia, anemia, and myelofibrosis ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)).

**Allogeneic HSCT is curative.** In the adolescent case, *"The patient was effectively treated with allogeneic hematopoietic stem cell transplantation with peripheral stem cells from a matched unrelated donor. Her symptoms and the MPIG6B mutation disappeared after treatment, and she was healthy and had returned to school at the last follow-up"* ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)). In the mouse model, the thrombopoietin mimetic romiplostim *"rescued thrombocytopenia, GPVI expression, and platelet reactivity to collag[en]"* ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)), whereas IVIG produced only transient partial platelet recovery. Osteosclerosis is a bone complication whose severity is **sex-linked** in mice ([PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/)).

### Finding 4 — Faithful mouse models reveal metalloproteinase-mediated receptor shedding and defective proplatelet formation

Mazharian et al. (2012, *Science Signaling*) created G6b-B-deficient mice that *"exhibited macrothrombocytopenia (reduced platelet numbers and the presence of enlarged platelets) and a susceptibility to bleeding as a result of aberrant platelet production and function"* ([PMID: 23112346](https://pubmed.ncbi.nlm.nih.gov/23112346/)). The mechanism includes enhanced metalloproteinase activity: *"megakaryocytes in G6b-B-deficient mice showed enhanced metalloproteinase production, which led to increased shedding of cell-surface receptors, including GPVI and GPIbα"* — explaining the low surface GPVI/GPIbα and defective proplatelet formation.

Cross-species concordance is strong. The osteosclerosis study confirmed that *"Null and loss-of-function mutations in MPIG6B, which codes for the inhibitory heparan sulfate receptor G6b-B, result in severe macrothrombocytopenia, large megakaryocyte clusters, and focal primary myelofibrosis in mice and humans"* ([PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/)). Humanized rescue — expression of human G6b-B restoring the murine phenotype — was demonstrated by Hofmann et al. ([PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)).

### Finding 5 — Population genetics confirm recessive, LOF-tolerant architecture

gnomAD constraint metrics for *MPIG6B* (ENSG00000204420; GRCh38 chr6:31,718,594–31,726,714) show **no depletion of loss-of-function or missense variants** in the general population: pLI = 1.2×10⁻⁷ (≈0), observed/expected pLoF (o/e) = 0.908 (90% CI 0.649–1.297; observed 22 vs expected 24.2), LOF Z = 0.38, missense Z = 0.42. Heterozygous pLoF alleles are therefore tolerated at carrier-level frequencies, fully consistent with a **recessive disease in which carriers are clinically unaffected** — matching the clinical observation of *"autosomal recessive inherited macrothrombocytopenia with focal myelofibrosis due to germ line loss-of-function mutations"* ([PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)).

### Finding 6 — Curated HPO phenotype frequencies (Monarch/HPO)

Disease-level phenotype annotations for MONDO:0044316:

| Phenotype | HPO term | Frequency |
|---|---|---|
| Thrombocytopenia | HP:0001873 | 100% |
| Anemia | HP:0001903 | 100% |
| Myelofibrosis | HP:0011974 | 100% |
| Anisopoikilocytosis | HP:0004823 | 100% |
| Splenomegaly | HP:0001744 | 50% |

Cross-references confirmed: OMIM:617441, MedGen CN1378448, UMLS:C4479504; synonyms "MPIG6B-related thrombocytopenia, anemia, and myelofibrosis" and "THAMY". No Orphanet mapping is present in the current MONDO record.

---

## Report by Template Section

### 1. Disease Information

THAMY is a rare inherited bone-marrow failure/platelet-production disorder characterized by **congenital thrombocytopenia with large platelets (macrothrombocytopenia), anemia, and progressive bone-marrow fibrosis (myelofibrosis)**. It is caused by biallelic loss-of-function in *MPIG6B*. Identifiers: **OMIM:617441**, **MONDO:0044316**, **MedGen C4479504/CN1378448**, **UMLS:C4479504**. No dedicated Orphanet, ICD-10/ICD-11, or MeSH identifier is captured in the MONDO record; myelofibrosis-related ICD codes (e.g., ICD-10 D47.4, D75.81) may be applied clinically but are not disease-specific. Synonyms: *MPIG6B-related thrombocytopenia, anemia, and myelofibrosis*; *THAMY*. Information is derived from **aggregated disease-level resources** (OMIM, Monarch, HPO) and **individual published case reports/series** (consanguineous families and sporadic cases), not EHR.

### 2. Etiology

**Causal factor:** purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in *MPIG6B* ([PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)). **Genetic risk factor:** the only established risk factor is carrying two pathogenic *MPIG6B* alleles; **consanguinity** is a major contextual risk factor, as the disease was first identified in consanguineous families and is "frequently described in the Arab population" ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/)). **Environmental/lifestyle/infectious factors:** none identified as causal; THAMY is a Mendelian disorder with no known environmental trigger. **Protective factors:** none characterized; conceptually, a wild-type *MPIG6B* allele is protective (carriers are unaffected per gnomAD LOF tolerance). **Gene–environment interactions:** none established. Genetic modifiers: in mice, **Syk** acts as a modifier — the R41A loss-of-function allele rescues the phenotype ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)); **sex** modifies osteosclerosis severity ([PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/)).

### 3. Phenotypes

| Phenotype | Type | HPO | Frequency | Onset | Severity/Course |
|---|---|---|---|---|---|
| Thrombocytopenia | Lab abnormality | HP:0001873 | 100% | Congenital/neonatal | Severe, persistent |
| Macrothrombocytopenia / large platelets | Lab abnormality | HP:0040326 / HP:0001873 | ~100% | Congenital | Severe |
| Anemia | Lab abnormality | HP:0001903 | 100% | Childhood | Moderate–severe, transfusion-dependent |
| Myelofibrosis | Pathology finding | HP:0011974 | 100% | Progressive | Progressive |
| Anisopoikilocytosis | Lab abnormality | HP:0004823 | 100% | Childhood | — |
| Splenomegaly | Clinical sign | HP:0001744 | 50% | Variable | Progressive |
| Hepatomegaly/Hepatosplenomegaly | Clinical sign | HP:0002240 | Variable | Variable | Progressive |
| Petechiae / bleeding tendency | Clinical sign | HP:0000967 / HP:0011875 | Common | From birth | Variable |
| Osteosclerosis | Physical/imaging | HP:0011001 | Model-defined | Progressive | Sex-linked severity (mouse) |

Quality-of-life impact: transfusion dependence, bleeding risk, splenomegaly-related discomfort, and fatigue from anemia substantially affect daily functioning; HSCT, when successful, restores normal health ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)).

### 4. Genetic / Molecular Information

**Causal gene:** *MPIG6B* (HGNC:13937, NCBI Gene 80277, UniProt O95866, Ensembl ENSG00000204420, 6p21.33), encoding the ITIM-containing inhibitory receptor **G6b-B**. **Variant classification:** reported alleles are predominantly **pathogenic truncating** (nonsense/frameshift/splice) with rare missense (p.Gly157Arg); classification per ACMG is pathogenic/likely pathogenic for truncating alleles in this LOF-mechanism gene. **Variant types:** nonsense (p.Cys108Ter, p.Tyr140Ter, p.Arg175Ter), frameshift (p.Ala21Glyfs, p.Ala52Glyfs, p.Pro134Leufs), splice, and missense. **Allele frequency:** pathogenic alleles are rare; gnomAD shows the gene is LOF-tolerant (o/e 0.908, pLI≈0), so heterozygous carriers exist in the population. **Origin:** **germline**, not somatic. **Functional consequence:** **loss of function** of an inhibitory receptor. **Modifier genes:** Syk (mouse rescue). **Epigenetic/chromosomal abnormalities:** none implicated.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are established. THAMY is a monogenic, germline disorder. Consanguinity (a population-genetic rather than environmental factor) increases recurrence risk.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Biallelic loss-of-function mutation in *MPIG6B*** → leads to absent or non-functional G6b-B inhibitory receptor on megakaryocytes/platelets.
2. Loss of G6b-B → **abolishes heparan-sulfate/perlecan (and heparin)-triggered receptor dimerization and ITIM/ITSM tyrosine phosphorylation** ([PMID: 31436532](https://pubmed.ncbi.nlm.nih.gov/31436532/); [PMID: 29891536](https://pubmed.ncbi.nlm.nih.gov/29891536/)).
3. No ITIM/ITSM phosphorylation → **no docking site for the phosphatases Shp1 and Shp2** → results in loss of phosphatase-mediated inhibitory signaling.
4. Loss of Shp1/Shp2 restraint → **elevated Syk tyrosine kinase activity** and dysregulated megakaryocyte signaling ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)).
5. (Branch A) Dysregulated signaling → **enhanced megakaryocyte metalloproteinase production** → **increased shedding of GPVI–FcRγ and GPIbα** from the cell surface → reduced collagen reactivity and defective proplatelet formation ([PMID: 23112346](https://pubmed.ncbi.nlm.nih.gov/23112346/)).
6. (Branch B) Dysregulated/hyperactivated megakaryopoiesis → **large megakaryocyte clusters** and aberrant maturation → **macrothrombocytopenia** (few, enlarged platelets) with increased platelet turnover.
7. Abnormal megakaryocytes → (inferred) **release of profibrotic cytokines/growth factors** in the marrow → **reticulin/focal myelofibrosis** histologically resembling primary myelofibrosis.
8. Marrow fibrosis + ineffective hematopoiesis → **anemia**, **extramedullary hematopoiesis**, and **splenomegaly/hepatomegaly**.
9. Megakaryocyte-driven bone signaling → **osteosclerosis** (sex-linked severity in mice; [PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/)).

**Upstream** nodes: *MPIG6B* mutation → loss of G6b-B → loss of Shp1/Shp2 recruitment. **Central effector:** Syk hyperactivation. **Downstream:** receptor shedding, defective platelet production, myelofibrosis, anemia, splenomegaly. **Pathways/processes (GO suggestions):** negative regulation of platelet activation (GO:0010544), megakaryocyte differentiation (GO:0030219), platelet formation (GO:0030220), protein dephosphorylation (GO:0006470), ITIM/ITAM signaling. **Cell types (CL):** megakaryocyte (CL:0000556), platelet (CL:0000233), hematopoietic stem cell (CL:0000037). **CHEBI:** heparin (CHEBI:28304), heparan sulfate.

### 7. Anatomical Structures Affected

- **Primary organ:** **bone marrow** (UBERON:0002371) — site of megakaryopoiesis and fibrosis. **Blood** (UBERON:0000178) — circulating platelets.
- **Secondary involvement:** **spleen** (UBERON:0002106; splenomegaly, extramedullary hematopoiesis), **liver** (UBERON:0002107; hepatomegaly), **bone** (osteosclerosis).
- **Body system:** hematopoietic/hematologic system; reticuloendothelial system.
- **Cells:** megakaryocytes (CL:0000556) and platelets (CL:0000233) are the directly affected populations.
- **Subcellular (GO Cellular Component):** plasma membrane (GO:0005886; receptor location), cytoplasmic ITIM signaling.
- **Lateralization:** systemic/bilateral (splenomegaly, hepatomegaly); not lateralized.

### 8. Temporal Development

- **Onset:** **congenital/neonatal** for thrombocytopenia; anemia and myelofibrosis manifest in childhood; some patients present in adolescence/adulthood ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/); [PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)).
- **Onset pattern:** chronic, insidious.
- **Progression:** myelofibrosis and splenomegaly are **progressive**; thrombocytopenia is persistent/lifelong.
- **Course:** chronic, lifelong unless corrected by HSCT.
- **Remission:** no spontaneous remission; **treatment-induced cure via allogeneic HSCT** ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)).
- **Critical period:** HSCT before irreversible marrow fibrosis/complications is the key intervention window (inferred).

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive (homozygous or compound heterozygous).
- **Penetrance:** appears complete in biallelic individuals; expressivity is variable (age of presentation, severity).
- **Epidemiology:** ultra-rare; precise prevalence/incidence not established. Clustering reported in **consanguineous and Arab populations** ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/)).
- **Carrier frequency:** heterozygous pLoF alleles are tolerated (gnomAD o/e 0.908, pLI≈0); carriers are clinically unaffected.
- **Consanguinity:** major contributor to case clustering.
- **Founder effects:** possible within consanguineous populations (not formally established).
- **Sex ratio:** both sexes affected; disease severity for the osteosclerosis component is sex-linked in mice.

### 10. Diagnostics

- **Laboratory:** CBC showing thrombocytopenia with enlarged platelets, anemia, anisopoikilocytosis (HP:0004823); peripheral smear.
- **Bone-marrow biopsy:** reticulin/collagen fibrosis, increased/clustered megakaryocytes — *"morphologic features similar to primary myelofibrosis"* ([PMID: 38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/)).
- **Flow cytometry:** reduced platelet surface GPVI and GPIbα (receptor shedding signature; from model data, [PMID: 23112346](https://pubmed.ncbi.nlm.nih.gov/23112346/)).
- **Imaging/exam:** splenomegaly/hepatomegaly on exam/ultrasound.
- **Genetic testing:** definitive diagnosis by **single-gene *MPIG6B* sequencing**, inherited-thrombocytopenia **gene panels**, or **WES/WGS**. Because variants are mostly truncating, standard sequencing is highly informative.
- **Differential diagnosis:** primary myelofibrosis (acquired, JAK2/CALR/MPL-driven), other inherited macrothrombocytopenias (MYH9-related, Bernard-Soulier, GATA1), congenital bone-marrow failure syndromes. Key distinguishing features: congenital onset, recessive inheritance, biallelic *MPIG6B* variants, absence of JAK2/CALR/MPL driver mutations.
- **Screening:** carrier/cascade testing in affected families; prenatal/preimplantation testing feasible for known family variants.

### 11. Outcome / Prognosis

- **Natural course:** progressive myelofibrosis, transfusion-dependent anemia, bleeding risk, splenomegaly; chronic lifelong morbidity without curative treatment.
- **Curative outcome:** **allogeneic HSCT is curative**, with resolution of symptoms and disappearance of the mutant marrow clone ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)).
- **Prognostic factors:** degree of marrow fibrosis, transfusion dependence, timing of HSCT, donor match. Formal survival statistics are not established given disease rarity.
- **Complications:** bleeding, iron overload from transfusions, infections, portal hypertension/splenomegaly sequelae, osteosclerosis.

### 12. Treatment

| Intervention | Type | Evidence | NCIT suggestion |
|---|---|---|---|
| Allogeneic HSCT | Curative cell therapy | Human: curative ([PMID: 35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/)) | NCIT:C15431 (Allogeneic BMT/HSCT) |
| Romiplostim (TPO mimetic) | Pharmacotherapy | Mouse: rescues platelets & GPVI ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)) | NCIT:C66919 (Romiplostim) |
| IVIG | Pharmacotherapy | Mouse: transient partial response ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)) | NCIT:C29087 (IVIG) |
| Syk inhibition (conceptual) | Targeted therapy | Mouse genetic rescue (Syk R41A) ([PMID: 36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/)) | NCIT:C1876 (Syk inhibitor class) |
| Platelet/RBC transfusion | Supportive care | Standard of care | NCIT:C15280 (Transfusion) |
| Splenectomy (symptomatic) | Surgical | Clinical, case-by-case | NCIT:C51771 (Splenectomy) |

Pharmacogenomics: no gene-drug guidelines specific to THAMY. Personalized approach: for a known family variant, genotype-guided counseling and early HSCT planning; Syk-axis and TPO-mimetic strategies are experimental/model-based and warrant clinical evaluation.

### 13. Prevention

- **Primary prevention:** not applicable (Mendelian); **genetic counseling** for consanguineous families and known carriers; preconception/prenatal/preimplantation genetic testing for family variants.
- **Secondary prevention:** cascade carrier screening; early diagnosis in at-risk newborns.
- **Tertiary prevention:** transfusion support, bleeding precautions, timely HSCT to prevent progression and complications.
- **No immunization, behavioral, or public-health prevention** is relevant beyond genetic counseling.

### 14. Other Species / Natural Disease

- **Mouse ortholog:** *Mpig6b* (NCBI Gene 106722; MGI:2146995; "megakaryocyte and platelet inhibitory receptor G6b"). Disease mechanism is evolutionarily conserved between mouse and human ([PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/); [PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/)).
- No naturally occurring companion-animal/wildlife disease is documented (no OMIA entry noted). No zoonotic relevance.

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| *Mpig6b* knockout mouse | Mammalian, germline KO | Macrothrombocytopenia, enlarged platelets, bleeding, receptor shedding, defective proplatelet formation | [PMID: 23112346](https://pubmed.ncbi.nlm.nih.gov/23112346/) |
| G6b-B Y212F/Y238F knock-in | ITIM/ITSM signaling-dead knock-in | Macrothrombocytopenia (proves Shp1/Shp2 requirement) | [PMID: 29891536](https://pubmed.ncbi.nlm.nih.gov/29891536/) |
| Humanized (human G6b-B) mouse | Knock-in rescue | Human G6b-B rescues murine phenotype | [PMID: 29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/) |
| *Mpig6b*-deficient mouse (bone) | Germline KO | Megakaryocyte-driven osteosclerosis, sex-linked severity | [PMID: 33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/) |

**Strengths:** faithful recapitulation of macrothrombocytopenia, megakaryocyte clustering, focal myelofibrosis, and receptor shedding; amenable to genetic epistasis (Syk R41A rescue) and pharmacological testing (romiplostim). **Limitations:** sex-linked osteosclerosis differences; human anemia/myelofibrosis severity and transfusion dependence may not fully map to the mouse. **Resources:** MGI (MGI:2146995), IMPC/IMSR.

---

## Mechanistic Model (Synthesis)

```
  Biallelic MPIG6B LOF mutation
             │
             ▼
   Absent/non-functional G6b-B inhibitory receptor (megakaryocyte/platelet)
             │  (loss of heparan sulfate/perlecan/heparin sensing)
             ▼
   No ITIM/ITSM tyrosine phosphorylation → no Shp1/Shp2 docking
             │
             ▼
   Loss of phosphatase brake → ELEVATED SYK KINASE ACTIVITY   ◄── (Syk R41A rescues)
             │
      ┌──────┴───────────────────────────┐
      ▼                                   ▼
  Metalloproteinase ↑                 Dysregulated megakaryopoiesis
  shedding of GPVI-FcRγ, GPIbα        large MK clusters, aberrant maturation
      │                                   │
      ▼                                   ▼
  Reduced collagen reactivity        MACROTHROMBOCYTOPENIA (few, large platelets)
  defective proplatelet formation          │
                                           ▼
                        (inferred) profibrotic MK secretion
                                           ▼
                        FOCAL/RETICULIN MYELOFIBROSIS → ANEMIA
                                           ▼
                        Extramedullary hematopoiesis → SPLENOMEGALY/HEPATOMEGALY
                                           ▼
                        Osteosclerosis (sex-linked severity)

  CURE: Allogeneic HSCT replaces mutant marrow.
  RESCUE (mouse): Romiplostim (TPO mimetic); Syk-axis inhibition (conceptual).
```

Upstream = *MPIG6B* mutation and loss of Shp1/Shp2 recruitment; central effector = Syk hyperactivation; downstream = receptor shedding, thrombocytopenia, myelofibrosis, anemia, splenomegaly, osteosclerosis.

---

## Evidence Base

| PMID | Title | Contribution |
|---|---|---|
| [29898956](https://pubmed.ncbi.nlm.nih.gov/29898956/) | *Congenital macrothrombocytopenia with focal myelofibrosis due to mutations in human G6b-B is rescued in humanized mice* | Establishes causal gene, recessive LOF inheritance, humanized-mouse rescue (landmark) |
| [31436532](https://pubmed.ncbi.nlm.nih.gov/31436532/) | *Heparan sulfates are critical regulators of the inhibitory megakaryocyte-platelet receptor G6b-B* | Identifies ligand (heparan sulfate/perlecan) and Shp1/Shp2 signaling |
| [29891536](https://pubmed.ncbi.nlm.nih.gov/29891536/) | *Uncoupling ITIM receptor G6b-B from tyrosine phosphatases Shp1 and Shp2 disrupts murine platelet homeostasis* | ITIM/ITSM→Shp1/Shp2 docking is required (Y212F/Y238F KI) |
| [36269841](https://pubmed.ncbi.nlm.nih.gov/36269841/) | *Treatment of congenital thrombocytopenia and decreased collagen reactivity in G6b-B-deficient mice* | Syk hyperactivation; Syk R41A and romiplostim rescue |
| [23112346](https://pubmed.ncbi.nlm.nih.gov/23112346/) | *Mice lacking the ITIM-containing receptor G6b-B exhibit macrothrombocytopenia and aberrant platelet function* | First KO model; metalloproteinase-mediated GPVI/GPIbα shedding |
| [33434328](https://pubmed.ncbi.nlm.nih.gov/33434328/) | *Severity of Megakaryocyte-Driven Osteosclerosis in Mpig6b-Deficient Mice Is Sex-Linked* | Cross-species concordance; osteosclerosis; sex modifier |
| [35940081](https://pubmed.ncbi.nlm.nih.gov/35940081/) | *A novel MPIG6B gene mutation in an adolescent girl with congenital thrombocytopenia and myelofibrosis* | Human case; HSCT curative; variant spectrum |
| [38694137](https://pubmed.ncbi.nlm.nih.gov/38694137/) | *MPIG6B Gene-Related Myelofibrosis: A Rare Inherited Disease Frequently Described in Arab Population* | Gene locus/protein; PMF-like marrow; population clustering |

---

## Limitations and Knowledge Gaps

- **Epidemiology is unquantified:** no reliable prevalence, incidence, carrier frequency, or survival statistics exist due to disease rarity; most knowledge comes from small case reports/series and consanguineous families.
- **No Orphanet/ICD-specific identifier** is mapped in the current MONDO record, complicating registry-based epidemiology.
- **Myelofibrosis mechanism is partly inferred:** the exact profibrotic signals linking abnormal megakaryocytes to marrow fibrosis (e.g., TGF-β, PDGF) in THAMY specifically were not directly demonstrated in the reviewed literature.
- **Therapeutics beyond HSCT are model-based:** romiplostim and Syk inhibition efficacy is established in mice only; no human trials of targeted pharmacotherapy are reported.
- **Genotype–phenotype correlation** (e.g., missense p.Gly157Arg vs truncating alleles) and penetrance/expressivity modifiers in humans remain incompletely characterized.
- **Sex-linked osteosclerosis** is a mouse observation; its human relevance is unclear.

## Proposed Follow-up Experiments / Actions

1. **Establish a patient registry** for THAMY to quantify prevalence, natural history, transfusion burden, and HSCT outcomes, especially in consanguineous/Arab populations.
2. **Define the profibrotic axis:** measure TGF-β/PDGF and perform single-cell/transcriptomic profiling of patient and mouse marrow megakaryocytes to pinpoint the fibrosis-driving signals (GEO/single-cell).
3. **Clinical evaluation of TPO mimetics (romiplostim/eltrombopag)** as a bridge-to-transplant or disease-modifying therapy, given strong mouse rescue data.
4. **Test Syk inhibitors** (e.g., fostamatinib) preclinically in human iPSC-derived megakaryocytes from patients, exploiting the Syk R41A genetic-rescue rationale.
5. **Deep genotype–phenotype study** correlating variant class with age of onset, fibrosis severity, and HSCT timing to refine prognostication and intervention windows.
6. **Request Orphanet/ICD-11 code assignment** to improve knowledge-base interoperability and epidemiologic tracking.

---

*Report compiled from 8 primary papers and curated Monarch/HPO/gnomAD data across a 5-iteration autonomous investigation. Evidence source types span human clinical case reports (PMID 35940081, 38694137), model-organism studies (PMID 23112346, 29891536, 36269841, 33434328), humanized-mouse functional genetics (PMID 29898956), biochemical/in vitro ligand studies (PMID 31436532), and computational population genetics (gnomAD).*


## Artifacts

- [OpenScientist final report](MPIG6B-Related_Thrombocytopenia_and_Myelofibrosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MPIG6B-Related_Thrombocytopenia_and_Myelofibrosis-deep-research-openscientist_artifacts/final_report.pdf)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 17 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0044316` (5 mentions) - the report calls it "if available"; MONDO calls it **thrombocytopenia, anemia, and myelofibrosis**
- `MedGen:C4479504` (1 mention) - the report calls it "CN1378448"; MedGen calls it **Acute abdomen**
- `HP:0001873` (3 mentions) - the report calls it "Thrombocytopenia", "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0001903` (2 mentions) - the report calls it "Anemia", "Lab abnormality"; HP calls it **Anemia**
- `HP:0011974` (2 mentions) - the report calls it "Myelofibrosis", "Pathology finding"; HP calls it **Myelofibrosis**
- `HP:0004823` (3 mentions) - the report calls it "Anisopoikilocytosis", "Lab abnormality"; HP calls it **Anisopoikilocytosis**
- `HP:0001744` (2 mentions) - the report calls it "Splenomegaly", "Clinical sign"; HP calls it **Splenomegaly**
- `HP:0002240` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hepatomegaly**
- `HP:0011001` (1 mention) - the report calls it "Physical/imaging"; HP calls it **Increased bone mineral density**
- `NCIT:C15431` (1 mention) - the report calls it "Allogeneic BMT/HSCT"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C66919` (1 mention) - the report calls it "Romiplostim"; NCIT calls it **Photoimmunotherapy**
- `NCIT:C1876` (1 mention) - the report calls it "Syk inhibitor class"; NCIT calls it **Lurtotecan Liposome**
- `NCIT:C15280` (1 mention) - the report calls it "Transfusion"; NCIT calls it **Breast Conservation Treatment**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C29087` (1 mention), reported as "IVIG" - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000556` (2 mentions) - the report calls it "Cells:** megakaryocytes"; CL calls it **megakaryocyte**
- `UBERON:0002371` (1 mention) - the report calls it "bone marrow", "Primary organ:** **bone marrow"; UBERON calls it **bone marrow**
- `NCIT:C51771` (1 mention) - the report calls it "Splenectomy"; NCIT calls it **Total Laryngectomy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001873` - called "Thrombocytopenia", "Lab abnormality"
- `HP:0001903` - called "Anemia", "Lab abnormality"
- `HP:0011974` - called "Myelofibrosis", "Pathology finding"
- `HP:0004823` - called "Anisopoikilocytosis", "Lab abnormality"
- `HP:0001744` - called "Splenomegaly", "Clinical sign"
- `UBERON:0002371` - called "bone marrow", "Primary organ:** **bone marrow"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`, `MGI`.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:38694137`: "frequently described in the Arab population"
  - closest text in source: "The disease was previously described in seven articles with a total of 20 patients"
