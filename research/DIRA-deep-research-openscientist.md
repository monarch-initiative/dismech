---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T13:23:37.616822'
end_time: '2026-09-09T13:52:52.508880'
duration_seconds: 1754.89
template_file: /tmp/dira_prompt.md
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DIRA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DIRA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Deficiency of the Interleukin-1 Receptor Antagonist (DIRA)
- **MONDO ID:** MONDO:0013021 (if available)
- **Category:** Autosomal recessive autoinflammatory disease from IL1RN loss causing sterile multifocal osteomyelitis, periostitis and pustulosis

## Research Objectives

Please provide a comprehensive research report on **Deficiency of the Interleukin-1 Receptor Antagonist (DIRA)** covering all of the
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

# Deficiency of the Interleukin-1 Receptor Antagonist (DIRA): A Comprehensive Disease Characterization

**MONDO:0013021 · OMIM #612852 · Orphanet ORPHA:361 · IL1RN (2q14.1)**

*Evidence sources are labeled: [Human clinical], [Model organism], [In vitro], [Review/aggregated]. All claims are cited to PMIDs; verbatim abstract quotes are given in quotation marks.*

---

## Summary (Answer to the Research Question)

DIRA is a rare, autosomal-recessive **autoinflammatory disease** caused by biallelic **loss-of-function mutations in *IL1RN***, the gene encoding the secreted interleukin-1 receptor antagonist (IL-1RA). Without IL-1RA to competitively block the type I IL-1 receptor (IL1R1), IL-1α and IL-1β signal unopposed, producing **NF-κB–driven, neutrophil-mediated sterile inflammation** that classically presents in the **neonatal period** with **multifocal osteomyelitis, periostitis, and pustulosis** plus markedly elevated acute-phase reactants. It is life-threatening if untreated, but **IL-1 blockade with anakinra** (recombinant IL-1RA) produces rapid and durable remission in the large majority of patients — making DIRA a paradigm of mechanism-based targeted therapy. DIRA was first defined in 2009 (Aksentijevich et al., *NEJM*, PMID 19494218) [Human clinical].

---

## 1. Disease Information

**Overview.** DIRA is a monogenic autoinflammatory disorder of skin and bone. Affected neonates/infants present with sterile multifocal osteomyelitis, periostitis, and pustular dermatitis with systemic inflammation, in the absence of infection, high-titer autoantibodies, or autoreactive T cells [Human clinical, PMID 19494218; Review PMID 40060136].

**Key identifiers.**
- **MONDO:** MONDO:0013021
- **OMIM:** #612852 (disease); gene *IL1RN* *147679
- **Orphanet:** ORPHA:361 ("Deficiency of interleukin-1 receptor antagonist")
- **ICD-11:** 4A60.x (autoinflammatory disorders) — DIRA has no unique legacy ICD-10 code; typically coded under M08/M86 (osteomyelitis) or L98 historically
- **MeSH:** DIRA is captured under "Hereditary Autoinflammatory Diseases" (MeSH D056660); MeSH descriptor used in the systematic review was "interleukin-1 receptor antagonist deficiency" (PMID 40060136)
- **HGNC:** IL1RN = HGNC:6000; **UniProt:** P18510

**Synonyms / alternative names.** Deficiency of interleukin-1 receptor antagonist; IL-1RA deficiency; IL-1 receptor antagonist deficiency; DIRA; osteomyelitis, sterile multifocal, with periostitis and pustulosis (OMPP).

**Information source.** Disease-level knowledge derives from **aggregated primary case reports and small case series** plus one PRISMA systematic review (18 studies, 2009–2024; PMID 40060136) — not from large EHR/registry datasets, reflecting the disease's rarity (~30–60 reported genetically confirmed patients worldwide as of the mid-2020s).

---

## 2. Etiology

**Primary cause — genetic.** DIRA is caused by **autosomal recessive, biallelic loss-of-function mutations in *IL1RN*** (2q14.1, within the 2q13 IL-1 gene cluster). "DIRA is developed from the loss-of-function biallelic mutations of the IL1RN gene that encodes IL-1 receptor antagonist (IL-1RA), leading to the unchecked pro-inflammatory signaling and subsequent systemic inflammation" [Review, PMID 38398338].

**Genetic risk factors.**
- *Causal variants:* homozygous or compound-heterozygous null *IL1RN* alleles (nonsense, frameshift, large genomic deletions). Founder alleles cluster geographically (see §9).
- *Modifier genes:* In the mouse model, disease penetrance/expressivity is strongly **background-dependent** and governed by QTLs (chromosome 1 major locus; candidate genes *Mr1, Pla2g4a, Fasl, Prg4, Ptgs2*) [Model organism, PMID 21414240, 22820384, 22942082]. Human modifiers are not yet defined.

**Environmental risk factors.** None established as causal. **Consanguinity** and descent from a founder population increase the chance of being homozygous (see §9). Sex: reported **male predominance** [Review, PMID 40060136], mechanism unknown (not X-linked; *IL1RN* is autosomal, so this is an observational skew).

**Protective factors.** Heterozygous carriers are asymptomatic — "heterozygous carriers were asymptomatic, with no cytokine abnormalities in vitro" [Human clinical/In vitro, PMID 19494218]. No environmental protective factors are described. The single functional protective "factor" is a wild-type *IL1RN* allele.

**Gene–environment interactions.** Not specifically characterized in humans. In *Il1rn*-null mice, the **intestinal microbiome** modulates disease: dysbiosis (↑Helicobacter, ↓Ruminococcus/Prevotella) promotes IL-17/TLR4-dependent arthritis, indicating a microbiome × genotype interaction [Model organism, PMID 28645307]. Whether infections trigger human DIRA flares is inferred but not proven.

---

## 3. Phenotypes

DIRA is dominated by **bone**, **skin**, and **systemic inflammatory** phenotypes with **neonatal onset** and **severe, chronic/episodic** course; frequencies below are qualitative/derived from the small literature (PMID 19494218, 40060136, 38398338).

| Phenotype | Type | Onset | Severity | Frequency | HPO term |
|---|---|---|---|---|---|
| Multifocal sterile osteomyelitis | Clinical/imaging sign | Neonatal | Severe | Very frequent (hallmark) | HP:0002754 (osteomyelitis) |
| Periostitis (periosteal reaction) | Imaging sign | Neonatal | Severe | Very frequent (hallmark) | HP:0002758-related / HP:0100774 |
| Pustulosis / pustular rash | Physical manifestation | Neonatal–infancy | Moderate–severe | Very frequent | HP:0200039 (pustule); HP:0000988 (skin rash) |
| Fever / systemic inflammation | Symptom | Neonatal | Variable | Most common symptom | HP:0001945 (fever) |
| Osteolytic bone lesions | Imaging sign | Neonatal | Severe | Frequent | HP:0002797 (osteolysis) |
| Bone pain / pseudoparalysis | Symptom | Neonatal | Severe | Frequent | HP:0002653 (bone pain) |
| Widened/ballooned ribs, clavicles, long bones | Imaging sign | Neonatal | — | Characteristic | HP:0000892 (rib abnormality) |
| Nail changes (onychia, pustular paronychia) | Physical sign | Infancy | Mild–moderate | Frequent | HP:0001597 (nail dysplasia) |
| Arthralgia / arthritis / joint swelling | Sign | Neonatal–childhood | Variable | Frequent | HP:0002829 / HP:0001369 |
| Respiratory distress / interstitial pneumonitis | Sign | Neonatal | Severe | Occasional–frequent | HP:0002098 |
| Venous / arterial thrombosis, vasculitis | Complication | Variable | Severe | Occasional | HP:0002625 (deep vein thrombosis) |
| Hepatosplenomegaly | Sign | Variable | — | Occasional | HP:0001433 |
| Elevated CRP/ESR, neutrophilic leukocytosis, thrombocytosis, anemia | Laboratory abnormality | Neonatal | — | Near-universal | HP:0011227; HP:0001974; HP:0001894; HP:0001903 |

Supporting quotes: "neonatal onset of sterile multifocal osteomyelitis, periostitis, and pustulosis" [PMID 19494218]; "most common symptoms were fever, followed by osteoarticular manifestations (arthralgia, muscle contracture, fracture, osteolytic lesions, and osteomyelitis), nail changes, pneumonia, venous thrombosis" [PMID 40060136]; skin biopsy shows "neutrophil infiltration in the epidermis and subepidermal pustular dermatosis" [PMID 26100510].

**Onset variability.** Although classically neonatal, **late-onset** DIRA occurs (first symptoms at age 1–12 years) with milder or atypical presentations [Human clinical, PMID 26100510, 31467740].

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease. Qualitatively, untreated DIRA causes severe pain, feeding difficulty, disability from bone deformity/fracture, and high mortality; effective IL-1 blockade dramatically improves QoL and prevents irreversible complications [Review, PMID 32882069].

---

## 4. Genetic / Molecular Information

**Causal gene.** ***IL1RN*** (HGNC:6000; NCBI Gene 3557; Ensembl ENSG00000136689; OMIM *147679), chromosome **2q14.1**, encoding **IL-1 receptor antagonist (IL-1RA; UniProt P18510)**, a secreted competitive antagonist of IL1R1.

**Pathogenic variants (all loss-of-function; germline; ACMG "Pathogenic"):**
- **p.E77X** (nonsense) — Newfoundland founder allele [PMID 19494218, 21792839]
- **2-bp deletion** (frameshift) — Netherlands founder allele [PMID 19494218]
- **Lebanese frameshift** (consanguineous family) [PMID 19494218]
- **~175-kb genomic deletion at 2q13** removing *IL1RN* + five other IL-1-family genes — Puerto Rican founder allele [PMID 22431714, 22431772]
- **c.140delC / p.T47TfsX4** (novel frameshift) in compound het with E77X [PMID 21792839]
- **p.Asp72_Ile76del** (in-frame 15-bp deletion) — recurrent in Brazilian patients; **p.Q45\*** (rs1019766125) nonsense [PMID 32819369]
- **22,216-bp deletion** spanning the first four *IL1RN* exons — Indian patient, likely founder [PMID 28503715]
- **p.R26X** (nonsense) — late-onset Turkish patient [PMID 26100510]

**Variant classes:** nonsense, frameshift, in-frame deletion, and **large structural/genomic deletions**. Because large deletions are common, **copy-number–aware testing (SNP array/CMA or MLPA)** is required in addition to sequencing.

**Allele frequency.** Individually ultra-rare in gnomAD; founder alleles are enriched in specific populations (e.g., high carrier frequency of the 175-kb deletion in Puerto Ricans — "A high carrier frequency of the 175-kb DIRA-associated genomic deletion in the Puerto Rican population…" [PMID 22431714]).

**Somatic vs germline:** exclusively **germline**, biallelic, recessive.

**Functional consequence:** **Loss of function.** "The IL1RN mutations resulted in a truncated protein that is not secreted, thereby rendering cells hyperresponsive to interleukin-1beta stimulation" [In vitro/Human, PMID 19494218]. One most-upstream premature stop codon variant is **hypomorphic** due to translation reinitiation, softening the phenotype [In vitro, PMID 32185578]. No dominant-negative or gain-of-function mechanism.

**Modifier genes:** human modifiers undefined; strong QTL modifiers in mice (§2, §15).

**Epigenetic information:** No DIRA-specific DNA-methylation/histone data available (not applicable/unknown).

**Chromosomal abnormalities:** the disease-relevant "chromosomal" lesion is the **contiguous-gene 2q13 microdeletion** (structural variant) that includes *IL1RN* [PMID 22431714].

GO/molecular annotations: *IL1RN* — **GO:0005152** (IL-1 receptor antagonist activity), **GO:0005615** (extracellular space), **GO:0002526** (acute inflammatory response, negative regulation).

---

## 5. Environmental Information

- **Environmental / toxic / occupational factors:** none causal (monogenic disease).
- **Lifestyle factors:** not applicable (neonatal onset).
- **Infectious agents:** DIRA inflammation is **sterile** — lesions are culture-negative with no organisms on histology [Review, PMID 21788901, 39757386]. Infection is a key differential to exclude, not a cause. In the mouse model, the **commensal microbiome** modulates disease severity [Model organism, PMID 28645307], suggesting microbial context may influence expressivity but is not the trigger.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic null *IL1RN* mutation** (nonsense/frameshift/deletion) **leads to** absent or truncated IL-1RA that **is not secreted** [In vitro, PMID 19494218].
2. Loss of secreted IL-1RA **results in** loss of competitive antagonism at the **type I IL-1 receptor (IL1R1)** on target cells.
3. Unopposed **IL-1α and IL-1β** **bind IL1R1 + accessory protein IL1RAP**, **leading to** recruitment of MyD88 and IRAK4/IRAK1–TRAF6 (canonical IL-1 signaling; GO:0070498).
4. This **results in** sustained activation of **NF-κB** and MAPK — demonstrated as "significantly enhanced and prolonged" nuclear translocation of **NF-κB p65** in IL-1RA-deficient tissue [Model organism/In vitro, PMID 16622029].
5. NF-κB activation **drives transcription of** IL-6, IL-8/CXCL8, CXCL1(KC)/CXCL2(MIP-2), TNF-α, and G-CSF [Model organism, PMID 16622029; In vitro comparison PMID 33314777].
6. Chemokine/cytokine output **leads to** massive **neutrophil recruitment** — "IL-1β is the pivotal cytokine… responsible for the exaggerated production of cytokines and chemokines that induce the recruitment of neutrophils" [Review, PMID 29742056].
7. Branch A — **Skin:** neutrophils accumulate subcorneally **producing** pustulosis/psoriasiform dermatitis with "neutrophil-rich microabscesses… beneath the stratum corneum" [Model organism, PMID 15086551] → clinical **pustular rash**.
8. Branch B — **Bone:** IL-1 activates osteoclastogenic mediators and inflammatory macrophages (elevated caspase-1/IL-1β secretion shown in DIRA monocytes/macrophages) **leading to** osteoclast/osteoblast dysregulation, osteolysis, and periosteal new bone → **multifocal osteomyelitis + periostitis** [In vitro, PMID 33314777].
9. Branch C — **Systemic/vascular:** circulating IL-1/IL-6 **produce** fever, acute-phase response (↑CRP/ESR), and predispose to **thrombosis/vasculitis** (aortitis in the mouse model) [Model organism, PMID 39600116; Human PMID 40060136].
10. Interrupting step 2–3 pharmacologically (anakinra/rilonacept/canakinumab) **restores** antagonism/ligand neutralization and **results in** rapid clinical remission [Human clinical, PMID 19494218, 38398338] — closing the causal loop and confirming IL-1 as the driver.

**Upstream vs downstream.** Upstream/primary: *IL1RN* LOF → unopposed IL1R1 signaling → NF-κB. Downstream/effector: chemokine amplification, neutrophil influx, osteoclast activation, tissue injury.

**Cellular processes:** innate immune activation, chronic sterile inflammation (GO:0006954), neutrophil chemotaxis (GO:0030593), NF-κB signaling (GO:0007249), osteoclast differentiation (GO:0030316).
**Cell types (CL):** neutrophils **CL:0000775**, monocytes/macrophages **CL:0000235**, keratinocytes **CL:0000312**, osteoclasts **CL:0000092**, osteoblasts **CL:0000062**, fibroblast/synoviocytes.
**Protein dysfunction:** loss of function of secreted IL-1RA (misprocessed/non-secreted truncation) [PMID 19494218].
**Metabolic changes:** none disease-specific.
**Chemical entities (CHEBI):** IL-1β and IL-1α (proteins); therapeutic small-molecule/biologic antagonists; reactive mediators nitric oxide (CHEBI:16480), prostaglandins via PTGS2/COX-2.
**Molecular profiling:** no large-scale omics datasets specific to DIRA patients (GEO/PRIDE/MetaboLights: none dedicated). Mechanistic transcriptomics comes from *Il1rn*-KO mice and comparative monocyte studies (PMID 33314777, 39600116).

---

## 7. Anatomical Structures Affected

- **Primary organs:** **Bone / skeletal system** (UBERON:0002481 bone tissue; ribs UBERON:0002228; clavicle UBERON:0001105; long bones/metaphyses; vertebrae UBERON:0002412) and **skin** (UBERON:0002097; epidermis UBERON:0001003; nail UBERON:0001705).
- **Secondary / systemic involvement:** joints (UBERON:0000982), **lungs/respiratory system** (interstitial pneumonitis; UBERON:0002048), **vasculature** (arteries/veins; thrombosis, aortitis UBERON:0000947), liver/spleen (hepatosplenomegaly), CNS rarely.
- **Body systems:** musculoskeletal, integumentary, immune/hematologic, respiratory, cardiovascular.
- **Tissue types:** connective/osseous tissue, epithelial (epidermis, nail matrix), synovium, vascular endothelium.
- **Cell populations:** neutrophils (CL:0000775), macrophages (CL:0000235), keratinocytes (CL:0000312), osteoclasts (CL:0000092).
- **Subcellular (GO CC):** extracellular space (GO:0005615, site of missing IL-1RA); plasma-membrane receptor complex IL1R1/IL1RAP (GO:0045323); nucleus (NF-κB translocation, GO:0005634).
- **Localization / lateralization:** **multifocal and bilateral/asymmetric** bone lesions; diffuse/generalized skin pustulosis. Characteristic sites: ribs, clavicles, long-bone metaphyses, vertebrae, periarticular bone [Human clinical, PMID 28503715 "sterile multifocal osteomyelitis including ribs and clavicles"].

---

## 8. Temporal Development

- **Onset:** typically **congenital/neonatal** (first days–weeks of life), acute-to-subacute; **variable**, with recognized **late-onset** forms (1–12 years) [PMID 19494218, 26100510, 31467740].
- **Progression:** **chronic, progressive or episodic/relapsing** systemic inflammation with flares; untreated disease escalates to organ failure. Progression rate can be **rapid** in neonates (respiratory insufficiency, sepsis-like deterioration) [PMID 37575641, 39757386].
- **Duration:** **chronic, lifelong** — requires continuous therapy; no spontaneous cure.
- **Remission pattern:** **treatment-induced** (IL-1 blockade); relapse on drug withdrawal. Spontaneous remission is not characteristic.
- **Critical period / window of opportunity:** **early initiation of anakinra** (ideally before irreversible bone/organ damage) is the decisive intervention window — "It is imperative to recognize this disease early to achieve adequate response and remission" [PMID 37575641].

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** [PMID 19494218].
- **Penetrance:** essentially **complete** in biallelic-null genotypes (hypomorphic reinitiation alleles can attenuate; PMID 32185578).
- **Expressivity:** **variable** (neonatal severe → late-onset milder), influenced by residual protein and presumed modifiers.
- **Carriers:** asymptomatic, no in-vitro cytokine abnormality [PMID 19494218].
- **Founder effects (variant geography):** Newfoundland (E77X), Netherlands (2-bp del), Puerto Rico (175-kb 2q13 deletion; high local carrier frequency), Lebanon (frameshift), Brazil (p.Asp72_Ile76del), India (22.5-kb deletion) [PMID 19494218, 22431714, 32819369, 28503715].
- **Consanguinity:** contributory (e.g., Lebanese consanguineous family) [PMID 19494218].
- **Anticipation / germline mosaicism:** not described / not applicable.
- **Epidemiology:** **ultra-rare**; ~30–60 genetically confirmed cases reported worldwide; precise prevalence/incidence **not established** (Orphanet lists prevalence as unknown/<1/1,000,000). Systematic review: 18 eligible studies over 15 years (PMID 40060136).
- **Sex ratio:** reported **male-predominant** (~observational; PMID 40060136); disease gene is autosomal.
- **Age distribution:** overwhelmingly infants; clinical recognition often around ~4 years in the aggregate literature (PMID 40060136), reflecting diagnostic delay.

---

## 10. Diagnostics

- **Laboratory (LOINC):** markedly elevated **CRP** (LOINC 1988-5) and **ESR** (LOINC 4537-7); neutrophilic leukocytosis, thrombocytosis, anemia of inflammation [PMID 19494218, 26100510]. HPO: HP:0011227, HP:0001974, HP:0001894, HP:0001903.
- **Imaging (RadLex/Radiopaedia):** radiographs show **osteolytic and/or sclerotic lesions, periosteal new bone, rib/clavicle/long-bone widening, vertebral involvement, heterotopic ossification**; **MRI / whole-body MRI is the sensitivity gold standard** and detects clinically silent lesions — "MRI is more sensitive for detecting CNO and is considered the gold standard for monitoring the disease" [PMID 30031498]; "Whole body MRI is helpful in detecting asymptomatic lesions" [PMID 21788901].
- **Histopathology:** skin — subepidermal/subcorneal **neutrophilic pustular dermatosis** [PMID 26100510]; bone — **sterile osteomyelitis** with "predominant neutrophil infiltration in the absence of autoantibodies and autoreactive T cells" [PMID 21788901]. SNOMED: sterile/chronic nonbacterial osteomyelitis.
- **Genetic testing (definitive):** **single-gene *IL1RN* sequencing** or **NGS autoinflammatory panels / WES**, **plus CMA/SNP-array or MLPA** to capture large deletions (e.g., 175-kb, 22.5-kb) [PMID 22431714, 28503715]. WGS captures both SNVs and structural variants. GTR: *IL1RN*-testing labs available.
- **Functional/biomarker confirmation:** demonstration of absent secreted IL-1RA and IL-1β hyperresponsiveness of patient cells [In vitro, PMID 19494218].
- **Clinical criteria:** no formal consensus criteria; **diagnosis = compatible skin/bone/systemic phenotype + biallelic *IL1RN* LOF variants** (± dramatic anakinra response, sometimes used empirically before genetics; PMID 37575641).
- **Differential diagnosis:** infectious osteomyelitis; **CRMO/CNO**; **Majeed syndrome (*LPIN2*)**; **NOMID/CAPS (*NLRP3*)**; **DITRA (*IL36RN*)/generalized pustular psoriasis**; **PAPA (*PSTPIP1*)**; cherubism; neonatal sepsis; Langerhans cell histiocytosis [PMID 21788901, 39757386, 33314777]. Discriminator: sterile, antibiotic-unresponsive, **anakinra-responsive** disease with biallelic *IL1RN* variants.
- **Screening:** targeted **cascade/carrier testing** in founder populations and relatives; consider *IL1RN* testing (incl. CNV) in any neonate with unexplained pustulosis in high-carrier regions [PMID 22431714]. Not on standard newborn-screening panels.

---

## 11. Outcome / Prognosis

- **Untreated:** **life-threatening**; high morbidity/mortality with respiratory insufficiency, thrombosis, sepsis-like deterioration, multi-organ failure [PMID 38398338, 37575641, 39757386].
- **Treated:** **excellent, durable remission** with IL-1 blockade — "Patients treated with anakinra responded rapidly" [PMID 19494218]; **~88% complete remission** on continued anakinra with mean **Hb +3.18 g/dL, ESR −53.4 mm/h, CRP −135.45 mg/L** [PMID 38398338].
- **Life expectancy:** near-normal with early, sustained treatment; historically poor if undiagnosed.
- **Complications to prevent (tertiary prevention):** bone deformity, pathologic fracture, growth impairment, respiratory failure, thrombosis; chronic autoinflammation carries a theoretical **AA amyloidosis** risk [Review, PMID 32882069].
- **Prognostic factors:** **time-to-diagnosis / time-to-anakinra** (earlier = better), severity/extent of organ involvement, treatment adherence, and residual protein function (hypomorphic alleles milder; PMID 32185578).
- **Prognostic biomarkers:** CRP/ESR normalization tracks treatment response; no validated molecular predictor beyond genotype.

---

## 12. Treatment

**Pharmacotherapy — IL-1 blockade (mechanism-based, first-line):**
- **Anakinra** (recombinant IL-1RA; blocks IL1R1) — **first-line, lifesaving**; rapid response, ~88% remission [PMID 19494218, 38398338]. **NCIT:C1960.** ATC L04AC03. Adverse events: injection-site reactions; rarely **anaphylaxis**, manageable by **desensitization** [PMID 28503715].
- **Rilonacept** (IL-1 "trap" fusion protein neutralizing IL-1α/β) — effective alternative [PMID 32819369]. **NCIT:C48411.**
- **Canakinumab** (anti-IL-1β mAb) — successful in a late-onset case at **150 mg SC q6 weeks** [PMID 26100510]; **but** because DIRA involves unopposed **IL-1α as well as IL-1β**, selective anti-IL-1β can be **insufficient or trigger flares** in some patients [PMID 32819369]. **NCIT:C71708.**
- **Adalimumab** (anti-TNF) — effective in one late-onset case [PMID 31467740]. Corticosteroids give partial/incomplete control [PMID 32819369].

**Pharmacogenomics:** none established; therapy is **genotype-rational** (replace/antagonize IL-1) rather than metabolizer-guided.

**Advanced therapeutics:** No approved gene therapy, cell therapy, or RNA therapy for DIRA; loss-of-function biology makes **gene replacement** a conceptually attractive future approach (not yet clinical).

**Surgical/interventional:** supportive orthopedic management of fractures/deformity; not curative.

**Supportive & rehabilitative:** pain control, wound/skin care, physical therapy for musculoskeletal sequelae, nutritional support.

**Experimental / trials:** no DIRA-specific registered pivotal trials (ultra-rare); management is guideline/expert-based and extrapolated from IL-1-mediated autoinflammation.

**Treatment strategy:** **empiric anakinra** may be started on strong clinical suspicion before genetic confirmation in a deteriorating neonate [PMID 37575641], then transition/optimize once genotype known; **continuous lifelong** IL-1 blockade with dose titration to CRP/ESR and clinical control.

---

## 13. Prevention

- **Primary prevention:** not possible (germline monogenic). **Genetic counseling** for at-risk families; **carrier/cascade testing**; **prenatal testing** or **preimplantation genetic diagnosis** feasible when familial variant is known (incl. CNV assays for deletions) [inferred from PMID 22431714, 28503715].
- **Secondary prevention:** **early recognition** and prompt IL-1 blockade to abort organ damage; targeted testing of neonates with unexplained pustulosis in **founder populations** (e.g., Puerto Rico) [PMID 22431714, 37575641].
- **Tertiary prevention:** sustained IL-1 blockade to prevent flares, bone deformity, thrombosis, and possible amyloidosis [PMID 32882069].
- **Immunization / public-health / behavioral / environmental measures:** not applicable to this monogenic disease.
- **Counseling:** autosomal-recessive **25% recurrence risk** per pregnancy for carrier couples; asymptomatic-carrier reassurance.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** experimental disease in **Mus musculus (NCBI:txid10090)**; no reported spontaneous natural DIRA-equivalent in companion animals or wildlife (OMIA: not established).
- **Orthologous gene:** mouse **Il1rn (NCBI Gene 16181)**; human **IL1RN (3557)** — evolutionarily conserved IL-1 antagonism.
- **Natural disease / veterinary relevance:** no recognized naturally occurring animal DIRA; not zoonotic; no cross-species transmission (genetic disease).
- **Comparative biology:** *Il1rn*-null mice reproduce the core biology (IL-1-driven sterile inflammation of skin, joints, bone, arteries), confirming mechanistic conservation, but disease pattern is **strain/background-dependent** [Model organism, PMID 15086551, 21414240].

---

## 15. Model Organisms

- **Principal model:** **IL-1Ra (Il1rn) knockout mouse** [Model organism]. "Interleukin-1 receptor antagonist knockout (IL-1Ra KO) mice spontaneously develop aortitis, arthritis and dermatitis, and are employed as a model for human inflammatory diseases" [PMID 39600116].
- **Genetic model types:** constitutive **knockout** (BALB/c, DBA/1, C57BL/6 backgrounds); congenic QTL strains; transferable T-cell disease (into nude mice) [PMID 39600116, 21414240].
- **Phenotype recapitulation (strengths):** IL-1-dependent **arthritis, psoriasiform pustular dermatitis with subcorneal neutrophil microabscesses**, **arterial inflammation/aortitis**, and **bone changes** — mirroring human skin+bone+systemic disease [PMID 15086551, 16622029, 39191800, 39600116].
- **Limitations:** disease penetrance is **background-dependent** (BALB/c susceptible, C57BL/6 resistant), governed by **QTLs (chr 1 major locus; candidates *Mr1, Pla2g4a, Fasl, Prg4, Ptgs2*)** and by the **microbiome** — features not central to the human monogenic disease [PMID 21414240, 22820384, 22942082, 28645307]; mice do not fully replicate neonatal multifocal osteomyelitis.
- **Applications:** dissecting IL-1→NF-κB→neutrophil biology, osteoimmunology, microbiome–autoinflammation interactions, and preclinical IL-1-blockade/target validation (e.g., PLD1 inhibition; PMID 23689131).
- **Resources:** MGI, IMSR (Il1rn alleles); Alliance of Genome Resources.

---

## Supported vs Refuted Hypotheses

**Supported:**
- H1: DIRA is caused by biallelic LOF *IL1RN* variants producing non-secreted IL-1RA and IL-1 hyperresponsiveness — **strongly supported** [PMID 19494218].
- H2: Unopposed IL-1 → NF-κB → CXC-chemokine/neutrophil axis drives pustulosis and sterile osteomyelitis — **supported** [PMID 16622029, 29742056, 15086551, 33314777].
- H3: IL-1 blockade (anakinra) achieves rapid, durable remission — **supported** (~88% remission) [PMID 38398338, 19494218].
- H4: Founder alleles explain geographic clustering — **supported** [PMID 22431714, 28503715, 32819369].

**Refuted / not supported:**
- That selective IL-1β blockade is uniformly sufficient — **not supported**; it can be insufficient/flare-inducing because IL-1α is also unopposed [PMID 32819369].
- That an environmental/infectious agent causes DIRA — **refuted**; disease is sterile and monogenic [PMID 21788901].

## Limitations and Future Directions

- **Ultra-rarity** → no prevalence/incidence figures, no QoL instruments, no controlled trials; evidence is aggregated case-level.
- **Human modifiers, epigenetics, and omics** are essentially unstudied; mouse QTL/microbiome findings need human validation.
- Future: DIRA registries and natural-history studies; prospective comparison of anakinra vs rilonacept vs canakinumab; gene-replacement/editing as a potential curative approach; standardized diagnostic criteria and inclusion of *IL1RN* (with CNV detection) in relevant newborn/at-risk screening.

---

### Key References (PMIDs)
19494218 (landmark discovery), 40060136 (systematic review), 38398338 (anakinra meta-analysis), 22431714 & 22431772 (Puerto Rican 175-kb deletion), 28503715 (Indian 22.5-kb deletion), 21792839 (compound het E77X + c.140delC), 32819369 (Brazilian variants; IL-1β-blockade caveat), 26100510 (late-onset R26X, canakinumab), 31467740 (late-onset, adalimumab), 32185578 (hypomorphic reinitiation allele), 16622029 (NF-κB mechanism), 29742056 & 27890235 (IL-1β/neutrophil dermatologic mechanism), 15086551 (psoriasiform KO skin), 39600116 (KO multi-organ inflammation), 39191800 (KO bone), 21414240/22820384/22942082 (QTL modifiers), 28645307 (microbiome), 33314777 (DIRA vs Majeed/NOMID monocyte/osteoclast biology), 21788901 & 30031498 & 39757386 (sterile osteomyelitis/imaging/DDx), 37575641 (early recognition), 32882069 (SAID/amyloidosis).


## Artifacts

- [OpenScientist final report](DIRA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DIRA-deep-research-openscientist_artifacts/final_report.pdf)