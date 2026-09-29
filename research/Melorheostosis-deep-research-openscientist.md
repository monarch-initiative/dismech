---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T12:38:27.984104'
end_time: '2026-09-08T12:51:05.244832'
duration_seconds: 757.26
template_file: /tmp/melo_prompt.md
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
  path: Melorheostosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Melorheostosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Melorheostosis
- **MONDO ID:** MONDO:0007970 (if available)
- **Category:** Somatic mosaic sclerosing bone dysplasia with segmental hyperostosis

## Research Objectives

Please provide a comprehensive research report on **Melorheostosis** covering all of the
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

# Comprehensive Disease Characterization Report: Melorheostosis

**Disease:** Melorheostosis (Léri disease / Léri–Joanny syndrome)
**MONDO ID:** MONDO:0007970
**Category:** Somatic mosaic sclerosing bone dysplasia with segmental hyperostosis
**Report date:** 2026-09-08
**Evidence base:** ~35 primary papers and reviews (PMIDs cited inline). Evidence source types are marked: *[human clinical]*, *[in vitro]*, *[model organism]*, *[review]*.

---

## Summary (Answer to the Research Question)

Melorheostosis is an ultra-rare (~0.9 per million), sporadic, non-hereditary sclerosing bone dysplasia characterized by asymmetric, segmental (sclerotomal) cortical and medullary hyperostosis that produces the pathognomonic radiographic "dripping candle wax" appearance, typically in the appendicular skeleton, accompanied by pain, deformity, joint contractures, and overlying soft-tissue changes. It is caused predominantly by **post-zygotic somatic mosaic gain-of-function mutations in *MAP2K1* (MEK1)** that hyperactivate the RAS–MAPK/ERK pathway in osteoblast-lineage cells, with genetically distinct subtypes driven by somatic *SMAD3* (TGF-β/SMAD), *KRAS*, and — in the osteopoikilosis/Buschke–Ollendorff spectrum only — germline *LEMD3*. There is no cure; management is symptom-directed (NSAIDs, bisphosphonates, physiotherapy, surgery), with MEK- and CDK4-inhibitor targeted therapy emerging from preclinical work.

---

## 1. Disease Information

**Overview.** Melorheostosis is a rare, benign, progressive sclerosing bone dysplasia of mesodermal origin featuring exuberant cortical bone overgrowth, most often in a single limb, that flows along the bone like melted wax. It was first described by Léri and Joanny (1922). *[review]* "Melorheostosis is a rare bone disease characterized by abundant bone formation with a characteristic radiographic appearance that resembles 'dripping candle wax'" (PMID 39776616).

**Key identifiers.**
- **MONDO:** MONDO:0007970
- **OMIM:** 155950 (Melorheostosis, isolated)
- **Orphanet:** ORPHA:2485
- **ICD-10:** Q78.8 (Other specified osteochondrodysplasias); **ICD-11:** LD24.Y / FB80.Y (other specified osteopathies) — often coded under other specified osteochondrodysplasias
- **MeSH:** D008586 (Melorheostosis; MeSH tree C05.116.099.708.410)
- **UMLS/SNOMED CT:** Melorheostosis (disorder), SCTID 43994001

**Synonyms / alternative names.** Léri disease; Léri–Joanny syndrome; "flowing hyperostosis"; "candle wax bone disease"; rheostosis; osteosis eburnisans monomelica.

**Source of information.** Derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual-patient case reports/case series** plus a single institution's prospective **natural-history cohort** (NIH; PMIDs 31485554, 35403375). There is no large EHR/registry dataset given the rarity.

---

## 2. Etiology

**Primary causal factor: genetic (somatic mosaicism).** Melorheostosis is caused by **post-zygotic (somatic) mosaic activating mutations** arising in mesenchymal/osteoblast-lineage precursors during development. There is **no infectious, environmental, or dietary cause**; it is not inherited.

**Genetic risk factors (causal variants).**
- ***MAP2K1* (MEK1)** — the major driver. Recurrent activating missense variants cluster in the MEK1 negative-regulatory domain: **p.Gln56Pro (Q56P), p.Lys57Glu (K57E), p.Lys57Asn (K57N)**, and a catalytic-domain variant **p.Cys121Ser (C121S)** (PMIDs 29643386, 32387835). *[human clinical / in vitro]* "we identify somatic mosaic MAP2K1 mutations in affected, but not unaffected, bone of eight unrelated patients ... The activating mutations (Q56P, K57E and K57N) cluster tightly in the MEK1 negative regulatory domain" (PMID 29643386).
- ***SMAD3*** — somatic activating mutations in **endosteal-pattern** melorheostosis (PMID 32232430).
- ***KRAS*** — somatic activating variants in a subset (osteopathia-striata-like pattern) (PMID 30989250).
- ***LEMD3* (MAN1)** — **germline** loss-of-function mutations cause osteopoikilosis (OPK) and Buschke–Ollendorff syndrome (BOS); they do **not** cause isolated sporadic melorheostosis (PMIDs 17087626, 19438932, 31129707).

**Modifier genes.** None firmly established. Because lesions are clonal and mosaic, disease extent likely reflects the developmental timing and location of the somatic mutation rather than trans-acting modifiers.

**Environmental risk factors.** None identified (toxins, occupation, radiation, age, sex, family history all non-contributory). Trauma is sometimes an incidental discovery trigger, not a cause (PMID 41938408).

**Protective factors.** None identified (genetic or environmental).

**Gene–environment interactions.** None documented; the disease is monogenic-somatic.

---

## 3. Phenotypes

Melorheostosis is highly variable ("variable severity, progressive/insidious course"). Core phenotypes with suggested HPO terms and frequency (from the 47-patient natural-history cohort and case series; PMIDs 31485554, 35403375, 39776616):

| Phenotype | Type | HPO term | Onset | Severity/Course | Frequency |
|---|---|---|---|---|---|
| Bone/limb pain | Symptom | Bone pain HP:0002653 | Childhood–adult | Chronic, progressive | Very frequent (presenting complaint) |
| Cortical hyperostosis / sclerosis | Physical sign (imaging) | Cortical thickening of long bones HP:0005791; Hyperostosis HP:0100774 | Congenital lesion, symptoms later | Progressive | Defining feature (~100%) |
| Joint contracture | Clinical sign | Joint contracture HP:0034392 | Childhood–adult | Progressive | Frequent |
| Limited range of motion | Clinical sign | Limitation of joint mobility HP:0001376 | Variable | Progressive | Frequent |
| Limb deformity / length discrepancy | Physical | Limb deformity; Limb undergrowth | Childhood | Progressive | Frequent |
| Limb swelling / soft-tissue mass | Sign | Localized skin lesion; Soft tissue swelling | Variable | Stable/progressive | Common |
| Overlying skin changes (hyperpigmentation, sclerotic/nevoid skin, hemangioma) | Physical | Abnormality of the skin HP:0000951 | Variable | Stable | Subset |
| Neurological compromise (nerve entrapment, myelopathy in spinal disease) | Sign | Peripheral neuropathy; Myelopathy | Variable | Progressive | Rare (axial disease) |
| Fatigue (general/physical) | Symptom | Fatigue HP:0012378 | Adult | Chronic | Prominent functional burden |

**Laboratory abnormalities:** characteristically **absent** — serum calcium, phosphate, alkaline phosphatase, ESR, CRP are **normal** (PMIDs 42559563, 41938408). Normal biochemistry is itself a diagnostic clue.

**Age of onset.** Lesions are congenital/developmental but frequently present in childhood or adulthood; late-onset monomelic presentations occur (PMID 42559563).

**Quality-of-life impact.** *[human clinical]* Substantial functional burden: high-demand leisure activities were the least retained and most often given up (27%); general and physical fatigue were the most limiting constructs, with physical fatigue moderately negatively correlated with activity engagement (r = −0.524, p < .001) (PMID 35403375).

---

## 4. Genetic / Molecular Information

**Causal genes (gene symbol; HGNC; OMIM; locus).**
- ***MAP2K1*** — HGNC:6840; NCBI Gene 5604; OMIM 176872; 15q22.31; encodes MEK1 (UniProt Q02750). Major driver.
- ***SMAD3*** — HGNC:6769; NCBI Gene 4088; OMIM 603109; 15q22.33. Endosteal subtype.
- ***KRAS*** — HGNC:6407; NCBI Gene 3845; OMIM 190070; 12p12.1. Rare subset.
- ***LEMD3*** — HGNC:28887; NCBI Gene 23592; OMIM 607844; 12q14.3. Germline; OPK/BOS spectrum (not isolated MEL).

**Pathogenic variants.**
- **Type/class:** missense, gain-of-function (activating). *MAP2K1*: Q56P, K57E, K57N (negative-regulatory domain, exon 2 hotspot); C121S (catalytic domain).
- **Classification:** Pathogenic (activating) per functional evidence; these are established oncogenic hotspots (also seen in Langerhans-cell histiocytosis, arteriovenous malformations, and some cancers).
- **Somatic vs germline:** **Somatic/mosaic**, present in affected bone and overlying skin but **not** in unaffected tissue or blood (PMID 29643386); mosaicism detected in overlying skin in 4/5 patients tested. Skin distribution of somatic variants was mapped in PMID 32791068.
- **Allele frequency:** Absent from population databases (gnomAD/1000G) as constitutional variants — they are somatic and, as germline events, would be embryonic-lethal or oncogenic.
- **Functional consequence:** Gain of function → constitutive MEK1 kinase activity → increased phospho-ERK1/2 (*MAP2K1*); enhanced TGF-β/SMAD transcriptional activity (*SMAD3*).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes, no recurrent epigenetic signature, and **no chromosomal abnormalities** (aneuploidy/translocation/CNV) are implicated. A subset of clinically classical cases has **no identifiable mutation** in *MAP2K1/SMAD3/LEMD3/KRAS* (PMID 32387835), indicating additional undiscovered drivers.

---

## 5. Environmental Information

- **Environmental factors:** None implicated (no toxin, radiation, pollution, or occupational association).
- **Lifestyle factors:** None (no smoking/diet/alcohol/exercise association).
- **Infectious agents:** **Not applicable** — melorheostosis is not infectious.

*This section is largely not applicable: melorheostosis is a somatic genetic disease with no known environmental contribution.*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**MAPK branch (classical "dripping candle wax", MAP2K1):**
1. A **post-zygotic somatic *MAP2K1* mutation** arises in an osteoblast/mesenchymal precursor during development → **leads to** a mosaic clone of mutant cells confined to a sclerotome/limb segment.
2. The mutation (e.g., K57N) **causes** constitutive MEK1 kinase activity (loss of negative autoregulation).
3. Constitutive MEK1 **results in** increased phospho-ERK1/2 signaling, detectable as a mosaic pattern (two osteoblast populations with distinct p-ERK levels) (PMID 29643386).
4. ERK hyperactivation **leads to** increased osteoprogenitor proliferation via cell-cycle activation (elevated phospho-Rb, Ki-67, higher S-phase fraction; CDK4-dependent) (PMIDs 29643386, 41395834).
5. Mutant cells **secrete increased VEGF**, driving hypervascularity/angiogenesis; VEGF is *sufficient alone* to increase mineralization of osteogenic cultures (PMID 37737377). *[in vitro]*
6. In parallel, the mutation **impairs BMP2-mediated terminal mineralization/differentiation**, which **results in** accumulation of excess unmineralized osteoid alongside dense cortical/woven bone (PMID 29643386).
7. The net effect **results in** segmental cortical/medullary hyperostosis → clinically pain, deformity, contractures, limb swelling; paradoxically the bone is *harder and mechanically stronger* despite decreased mineral density (inferred from geometry/microstructure; PMID 31689526). *[model organism]*

**TGF-β/SMAD branch (endosteal pattern, SMAD3):**
1b. A **somatic *SMAD3*-activating mutation** → **enhances** TGF-β/SMAD nuclear translocation and target-gene expression in osteoblasts (PMID 32232430).
2b. This **stimulates** osteoblast differentiation and mineralization (antagonized by BMP2) → **endosteal-pattern** hyperostosis.

*(KRAS-driven cases converge on RAS–MAPK activation, upstream of MEK1.)*

### Detail by category
- **Molecular pathways:** RAS–**MAPK/ERK** cascade (KEGG hsa04010; Reactome R-HSA-5673001 "RAF/MAP kinase cascade"); **TGF-β/SMAD** signaling (KEGG hsa04350; Reactome R-HSA-170834). BMP signaling is antagonistic/dysregulated. GO: MAPK cascade GO:0000165; ERK1/ERK2 cascade GO:0070371; transforming growth factor beta receptor signaling pathway GO:0007179.
- **Cellular processes:** increased cell proliferation (GO:0008284), dysregulated osteoblast differentiation (GO:0001649) and ossification (GO:0001503), angiogenesis (GO:0001525). Cell-cycle dysregulation (phospho-Rb/CDK4). No apoptosis or inflammation signature is prominent.
- **Protein dysfunction:** **Gain of function** — constitutively active MEK1 kinase; hyperactive SMAD3 transcription factor. Not misfolding/aggregation.
- **Metabolic changes:** No systemic metabolic derangement (normal Ca/PO4/ALP). Local: increased collagen I/IV secretion by mutant iMSCs (PMID 37737377).
- **Immune system involvement:** Not a primary feature; co-expression clustering noted altered interferon signaling in SMAD3 lesions (PMID 32232430) — significance uncertain.
- **Tissue damage mechanisms:** Mechanical (mass effect → contracture, nerve/cord compression), not oxidative/ischemic/fibronecrotic.
- **Molecular profiling:** RNAseq/GSEA of lesional tissue shows **upregulation of proliferative pathways** (PMID 32387835) and TGF-β/ossification/ECM-organization programs (PMID 32232430). Proteomic: elevated VEGF and collagen secretion (PMID 37737377).
- **Functional genomics:** iPSC→iMSC→osteoblast patient models and MEK1DD mouse (see §15).

**Cell types (CL):** osteoblast CL:0000062; osteoprogenitor/mesenchymal stem cell CL:0000134; fibroblast CL:0000057 (overlying skin carries the mutation). **Chemical entities (CHEBI):** zoledronic acid CHEBI:46557; palbociclib CHEBI:85993; trametinib CHEBI:75998 (MEK inhibitor class).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Bone (UBERON:0002481 bone tissue; UBERON:0001474 bone element), predominantly **long bones of the limbs** (appendicular skeleton). Lower-extremity long bones (femur, tibia, fibula) most common; upper extremity (humerus, radius, ulna, hand) frequent. Cohort: 30/47 lower extremity, 14/47 upper extremity, 1 both (PMID 35403375).
- **Secondary involvement / body systems:** **Musculoskeletal** (joints — contracture; muscle/soft tissue — swelling, sclerosis, ossification), **integumentary** (overlying skin — hyperpigmentation, scleroderma-like/nevoid changes), **nervous** (peripheral nerve entrapment; spinal cord compression/myelopathy in rare axial disease, PMID 41852826), **vascular** (hemangioma/hypervascularity). Axial sites reported: spine (C-spine, PMID 41852826), pubis (PMID 42047352).
- **Tissue/cell level:** cortical and endosteal **bone** (dense cortical, woven bone, hypervascular); connective tissue of skin (collagen/elastin). Target cells: osteoblasts (CL:0000062), osteoprogenitors/MSCs (CL:0000134).
- **Subcellular (GO cellular component):** nucleus GO:0005634 (SMAD3 translocation), cytoplasm/plasma membrane (MEK1/ERK signaling GO:0005886), extracellular region/matrix GO:0005576 (osteoid, collagen).
- **Localization/UBERON:** femur UBERON:0000981; tibia UBERON:0000979; fibula UBERON:0001446; humerus UBERON:0000976; radius UBERON:0001423; ulna UBERON:0001424; vertebral column UBERON:0001130.
- **Lateralization:** Characteristically **unilateral, asymmetric, monomelic**, in a **sclerotomal** distribution; bilateral/multifocal is uncommon (PMIDs 41938408, 39776616).

---

## 8. Temporal Development

- **Onset:** Congenital/developmental lesion (somatic mutation occurs in utero); clinical onset is typically **insidious**, presenting in childhood or adulthood; late-onset adult presentations occur.
- **Onset pattern:** Chronic, insidious (not acute).
- **Progression:** **Slowly progressive**, lifelong. Bone overgrowth and contractures accrue over years to decades (e.g., 20-year progressive history, PMID 42555496). No formal staging system exists.
- **Course pattern:** Progressive/stable; not relapsing-remitting or episodic.
- **Duration:** Chronic, lifelong (not self-limited).
- **Remission:** No spontaneous remission of bone lesions; symptom control (pain) is achievable with treatment.
- **Critical periods:** Developmental window (timing/location of the somatic mutation) determines lesion distribution/extent; there is no defined therapeutic "critical window," though early physiotherapy may limit contractures.

---

## 9. Inheritance and Population

- **Epidemiology — prevalence:** ultra-rare, **~0.9 per million** (i.e., ~0.00009 per 100,000); global prevalence **< 1 per million** (PMIDs 41938408, 42559563). Incidence not reliably estimated. *[review/case series]* "an estimated prevalence of 0.9 per million" (PMID 41938408).
- **Inheritance pattern:** **Sporadic, non-hereditary** — driven by somatic mosaicism; **not** Mendelian. (Germline *LEMD3* → autosomal dominant OPK/BOS is a separate, related entity.)
- **Penetrance/expressivity:** Not applicable in the classical sense (somatic); lesion expressivity is highly variable.
- **Genetic anticipation / germline mosaicism / founder effects / consanguinity / carrier frequency:** **Not applicable** — no vertical transmission, no carriers, no founder or consanguinity effect.
- **Population demographics:** No ethnic or geographic predilection; reported worldwide. **Sex ratio ~1:1** (no strong sex predilection). **Age distribution:** diagnosed across pediatric to older-adult ages.

---

## 10. Diagnostics

**Diagnosis is primarily radiographic**, supported by normal biochemistry and (non-specific) histology; molecular confirmation requires **lesional tissue**.

- **Imaging (cornerstone):** Plain radiograph/**CT** — flowing cortical **hyperostosis resembling "dripping/melting candle wax"** in a sclerotomal distribution (pathognomonic). *[review/case]* "a pathognomonic imaging appearance of flowing hyperostosis resembling melted candle wax" (PMID 32994853). **MRI** delineates soft-tissue involvement/extent; **Tc-99m-MDP bone scintigraphy** shows increased uptake reflecting activity (PMID 42555496); **FDG/PSMA PET** may be positive incidentally (PMIDs 42313078, 42047352). RadLex: hyperostosis.
- **Laboratory tests/biomarkers:** No diagnostic blood/urine biomarker; serum Ca, PO4, ALP, ESR, CRP **normal** (LOINC panels for these analytes). Normality helps exclude Paget disease and metabolic bone disease.
- **Biopsy/histopathology (supportive, non-specific):** dense cortical bone (73.3%), woven bone (60%), hypervascularity/increased porosity (66.7%), prominent cement lines (33%) (PMID 31386640); hyalinized collagen with dystrophic calcification also described (PMID 42559563). Biopsy is often *avoidable* when imaging is classic.
- **Genetic testing:** **Sequencing of affected lesional tissue (bone and/or overlying skin), not blood**, because variants are somatic/mosaic. WES, WGS, and RNAseq of affected-vs-unaffected tissue are the definitive research/clinical approach and identified *MAP2K1*/*SMAD3*/novel variants (PMIDs 29643386, 32232430, 32387835). Targeted single-gene/panel testing (*MAP2K1, SMAD3, KRAS, LEMD3*) on lesional DNA is reasonable. Karyotype/CMA/FISH/mtDNA/repeat testing: **not indicated** (no such abnormalities).
- **Omics-based diagnostics:** RNAseq of lesion (proliferative-pathway upregulation) is research-grade; no validated clinical omics/liquid-biopsy assay exists.
- **Clinical criteria / differential diagnosis:** No formal consensus criteria; diagnosis is clinicoradiologic. **Differential:** osteoma/osteoid osteoma, **osteoblastoma** (can mimic and recur — PMID 42004422), **osteosarcoma/parosteal osteosarcoma**, fibrous dysplasia, **Paget disease of bone**, osteopathia striata, **osteopoikilosis**, and mixed sclerosing bone dysplasia; distinguishing features are the flowing candle-wax pattern, sclerotomal distribution, normal labs, and benign non-aggressive behavior (PMIDs 32994853, 41214899).
- **Screening:** No population/newborn/carrier screening is applicable (somatic, non-heritable).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Benign** disease; **normal life expectancy**; not directly life-limiting. No disease-specific mortality data (deaths are not attributable to melorheostosis itself). Malignant transformation is a *theoretical* concern but has **not been clinically reported** (PMID 41938408).
- **Morbidity/disability:** Chief morbidity is **chronic pain, deformity, contracture, and reduced mobility**, producing disability and reduced participation in high-demand activities; fatigue is prominent (PMID 35403375). Rare severe morbidity: neurological deficit from nerve entrapment or spinal cord compression (PMIDs 41852826, 41717511).
- **Quality of life:** Impaired via pain/fatigue/loss of leisure activities (natural-history cohort, PMID 35403375). No disease-specific validated QoL instrument; generic tools used (Activity Card Sort, Multidimensional Fatigue Inventory, Lower/Upper Extremity Functional scales).
- **Complications:** contractures, limb-length discrepancy, joint dysfunction, soft-tissue ossification, fibrolipomatous/vascular masses, nerve/cord compression; rare fragility fracture at unaffected sites (PMID 32057643).
- **Recovery potential:** Bone lesions do not regress; symptoms are manageable. Function may improve with physiotherapy/analgesia and appropriately timed surgery.
- **Prognostic factors:** Lesion extent, axial (spinal) involvement (worse — neurological risk), degree of contracture, and pain severity. **Prognostic biomarkers:** none validated; *MAP2K1* vs *SMAD3* genotype correlates with radiographic subtype and may predict therapy response (predictive, not prognostic).

---

## 12. Treatment

**No cure and no established guideline exist; management is multidisciplinary and symptom-directed** (PMID 42273437). *[review/case]* "There are no established guidelines for its management, as it is not a curable condition. Treatment primarily focuses on symptom relief."

- **Pharmacotherapy:**
  - **NSAIDs** (e.g., celecoxib) for pain — VAS pain reduced to 1/10 with celecoxib + physiotherapy (PMID 42559563). NCIT: Nonsteroidal Anti-inflammatory Agent.
  - **Bisphosphonates** — IV **zoledronic acid** and **pamidronate** reduce pain and disease severity (PMIDs 42273437, 34169026, 32057643). NCIT: Bisphosphonate; Zoledronic Acid (CHEBI:46557).
  - **Pharmacogenomics:** none specific.
- **Targeted / advanced therapeutics (experimental):**
  - **MEK inhibitors** (trametinib/selumetinib class) — mechanistically rational (block MEK1→ERK); proposed by discovery authors as a treatment avenue (PMID 29643386). NCIT: MEK Inhibitor.
  - **CDK4/6 inhibitor palbociclib** — FDA-approved; reduced phospho-Rb, proliferation, and mineralization in *MAP2K1*-mutant patient iMSCs/osteoblasts, "opening a pathway to treatment" (PMID 41395834). *[in vitro]* NCIT: Cyclin-Dependent Kinase Inhibitor.
  - Gene/cell/RNA therapy: none in use.
- **Surgical/interventional:** osteotomy/contracture release, excision of exostoses/soft-tissue masses, limb-lengthening/deformity correction, and **decompression/fusion** for spinal cord compression; reserved for severe deformity, refractory pain, or neurological compromise (PMIDs 41852826, 41938408). Recurrence after excision is common. NCIT: Orthopedic Surgery; Osteotomy.
- **Supportive/rehabilitative:** **Physical/occupational therapy** for range of motion, contracture prevention, and function; pain management; splinting (PMIDs 35403375, 41717511). NCIT: Physical Therapy; Rehabilitation Therapy.
- **Experimental / clinical trials:** An NIH natural-history study (NCT02504879) has characterized the disease; no approved disease-modifying drug trial has reported results. MEK/CDK4 inhibition remains preclinical.
- **Treatment outcomes/adverse events:** Bisphosphonate response is variable (only ~9 zoledronate reports to date; PMID 42273437); adverse events per drug class (bisphosphonate: acute-phase reaction, osteonecrosis of the jaw; MEK inhibitors: rash, ocular/cardiac toxicity; CDK4/6i: cytopenias).
- **Personalized medicine:** Genotype-guided targeting (MEK inhibitor for *MAP2K1*; potential TGF-β–directed approaches for *SMAD3*) is the emerging paradigm.

---

## 13. Prevention

- **Primary prevention:** **Not possible** — the causal somatic mutation arises sporadically in utero; no modifiable risk factor exists.
- **Secondary prevention (early detection):** Early radiographic recognition prevents misdiagnosis, unnecessary biopsy, and enables early physiotherapy to limit contractures (PMIDs 30647832, 34169026).
- **Tertiary prevention:** Physiotherapy, analgesia, bisphosphonates, and timely surgery to prevent/limit contracture, deformity, and neurological complications.
- **Immunization / behavioral / public-health / environmental interventions:** **Not applicable.**
- **Genetic counseling:** Reassurance that the disease is **sporadic and non-heritable**, with **negligible recurrence risk** to offspring or siblings (the mutation is somatic, not germline). Prenatal/carrier/PGD testing not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** Melorheostosis is essentially a **human-specific** clinical entity; a well-defined naturally occurring homolog in companion animals or wildlife is **not established** (no OMIA entry for a melorheostosis phenotype). Human: *Homo sapiens* NCBI:txid9606.
- **Orthologous genes:** *Map2k1* (mouse, NCBI Gene 26395; NCBI:txid10090), *smad3* (mouse 17127), *Kras* (mouse 16653) — highly conserved.
- **Comparative biology / evolutionary conservation:** The RAS–MAPK and TGF-β/SMAD pathways are deeply conserved across vertebrates; the disease mechanism is modeled in mouse (see §15). **Zoonotic potential:** none (not transmissible).

*This section is largely not applicable as a naturally occurring cross-species disease; relevance is via engineered model organisms.*

---

## 15. Model Organisms

- **Mammalian (mouse):** **MEK1DD conditional transgenic mouse** expressing constitutively active MEK1 in osteoprogenitors postnatally. *[model organism]* Recapitulates "extra-cortical bone formation, abundant osteoid formation, decreased mineral density, and increased porosity," with paradoxically stronger bone due to altered geometry/microstructure (PMID 31689526). Model type: conditional/transgenic gain-of-function (Cre-driven in osteoprogenitors). Resources: MGI (*Map2k1*, MGI:1346866).
  - **Limitations:** does not reproduce the **mosaic/segmental (sclerotomal)** distribution, the overlying soft-tissue/skin involvement, or the natural somatic-mutation timing; expression is broader than the human clonal patch.
- **Human in vitro / iPSC models:** Patient-derived iPSCs reprogrammed (Sendai) from *MAP2K1*-mutant **skin fibroblasts**, differentiated to **induced MSCs → osteoblasts**; retain the mutation, show elevated MEK1/ERK activity, increased **VEGF**, proliferation, collagen I/IV, and mineralization (PMIDs 37737377, 41395834). Isogenic unaffected fibroblasts serve as controls. Cellosaurus/ATCC: patient-specific lines (not standardized).
- **Applications:** dissecting MAPK→proliferation/VEGF mechanisms, testing MEK and CDK4/6 inhibitors (palbociclib), and modeling the mineralization paradox.
- **Model databases:** MGI (mouse), Alliance of Genome Resources.

---

## Supported vs Refuted Hypotheses

**Supported:**
- Somatic mosaic activating *MAP2K1* mutations cause classical melorheostosis via MEK1→ERK hyperactivation (PMID 29643386). ✔
- Genetic heterogeneity: *SMAD3*/TGF-β drives the endosteal subtype; *KRAS* a rare subset (PMIDs 32232430, 30989250). ✔
- VEGF is a sufficient downstream driver of increased bone mineralization in mutant cells (PMID 37737377). ✔
- MEK1DD mouse recapitulates core skeletal features (PMID 31689526). ✔
- CDK4 inhibition (palbociclib) reduces mutant-cell proliferation/mineralization (PMID 41395834). ✔

**Refuted / not supported:**
- Germline *LEMD3* mutation causes isolated sporadic melorheostosis — **refuted**; *LEMD3* underlies OPK/BOS but not isolated MEL (PMIDs 17087626, 19438932, 31129707).
- Environmental/infectious/inherited causation — **not supported**; disease is sporadic-somatic.

## Limitations and Future Directions

- Evidence rests on **small cohorts and case reports** (ultra-rare disease); a subset of classical cases has **no identified mutation**, implying additional drivers to discover.
- **No controlled therapeutic trials**; bisphosphonate and targeted-therapy evidence is anecdotal/preclinical. MEK- and CDK4/6-inhibitor efficacy/safety in patients is unproven.
- Genotype–phenotype correlations (subtype-specific therapy) and single-cell/spatial characterization of the mosaic lesion are priority future work.

---

### Key ontology annotations (summary)
- **MONDO:** MONDO:0007970 · **HPO:** HP:0002653, HP:0100774, HP:0005791, HP:0034392, HP:0001376, HP:0012378
- **Genes (HGNC):** MAP2K1 (HGNC:6840), SMAD3 (HGNC:6769), KRAS (HGNC:6407), LEMD3 (HGNC:28887)
- **GO:** GO:0000165, GO:0070371, GO:0007179, GO:0001503, GO:0001649, GO:0008284, GO:0001525
- **CL:** CL:0000062 (osteoblast), CL:0000134 (MSC), CL:0000057 (fibroblast)
- **UBERON:** UBERON:0001474 (bone element), UBERON:0000981 (femur), UBERON:0000979 (tibia), UBERON:0001446 (fibula)
- **CHEBI:** CHEBI:46557 (zoledronic acid), CHEBI:85993 (palbociclib), CHEBI:75998 (trametinib)
- **NCIT:** Bisphosphonate Therapy, NSAID, MEK Inhibitor, CDK Inhibitor, Orthopedic Surgery, Physical Therapy


## Artifacts

- [OpenScientist final report](Melorheostosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Melorheostosis-deep-research-openscientist_artifacts/final_report.pdf)