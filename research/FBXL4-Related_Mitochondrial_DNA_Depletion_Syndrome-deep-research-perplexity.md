---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T22:37:32.984539'
end_time: '2026-09-28T22:43:17.283133'
duration_seconds: 344.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: FBXL4-Related Mitochondrial DNA Depletion Syndrome
  mondo_id: MONDO:0014198
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FBXL4-Related Mitochondrial DNA Depletion Syndrome
- **MONDO ID:** MONDO:0014198 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FBXL4-Related Mitochondrial DNA Depletion Syndrome** covering all of the
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

# FBXL4-Related Mitochondrial DNA Depletion Syndrome (MTDPS13): Comprehensive Disease Characteristics

FBXL4-related mitochondrial DNA depletion syndrome, also known as mitochondrial DNA depletion syndrome 13 (encephalomyopathic type, MTDPS13), is a rare, severe autosomal recessive disorder of mitochondrial maintenance caused by biallelic pathogenic variants in the nuclear gene *FBXL4*.[1][2][6][10] The disease typically presents in the neonatal period or early infancy with profound encephalomyopathy, including hypotonia, global developmental delay, and cerebral atrophy, accompanied by persistent lactic acidosis, failure to thrive, feeding difficulties, and often multisystem involvement such as cardiac disease, craniofacial dysmorphism, and ocular anomalies.[2][7][10][11][17] At the molecular level, FBXL4 encodes a mitochondrial outer-membrane F-box and leucine-rich repeat protein that functions as the substrate adaptor of an SCF (SKP1–CUL1–F-box) E3 ubiquitin ligase complex; loss of FBXL4 impairs ubiquitin-dependent turnover of the mitophagy receptors BNIP3 and BNIP3L/NIX, leading to excessive mitophagy, global loss of mitochondrial content, and secondary depletion of mitochondrial DNA with multi-complex respiratory chain deficiency.[6][7][8][9][13] Clinical series and case reports suggest extremely poor prognosis, with high infant and early childhood mortality and severe permanent neurodevelopmental impairment in survivors, while current treatments are largely supportive and “mitochondrial medications” have not shown efficacy.[7][10][11][12] Recent mechanistic work in patient fibroblasts, CRISPR/Cas9 knockout human cell lines, and *Fbxl4* knockout mice has clarified that FBXL4 safeguards mitochondrial abundance by suppressing lysosomal removal of mitochondria, pointing toward future therapeutic strategies that might target mitophagy pathways in this devastating disease.[9][11][13]

## 1. Disease Information

### 1.1 Overview and Disease Definition

FBXL4-related mitochondrial DNA depletion syndrome is classified among the nuclear-gene–encoded mitochondrial DNA maintenance disorders, a subset of mitochondrial DNA depletion syndromes (MTDPS) characterized by a profound reduction in mitochondrial DNA (mtDNA) copy number within affected tissues, leading to impaired oxidative phosphorylation and energy failure.[2][7][11][12] Specifically, MTDPS13 refers to a predominantly encephalomyopathic phenotype arising from biallelic loss-of-function variants in *FBXL4* (F-box and leucine-rich repeat protein 4), a gene located on chromosome 6q16.1–q16.2.[1][2][3][8] Individuals typically present with early-onset and often congenital neurologic dysfunction, including hypotonia, encephalopathy, and severe developmental delay, in combination with persistent lactic acidosis, failure to thrive, and variable involvement of other organ systems such as heart, bone marrow, immune system, and craniofacial structures.[2][7][10][11][17] Cells derived from affected patients show combined respiratory chain deficiencies and marked mtDNA depletion, confirming that this disease represents a disorder of mitochondrial maintenance rather than a primary structural or assembly defect of individual respiratory chain complexes.[6][7][10][14] As a Mendelian condition, FBXL4-related MTDPS13 is inherited in an autosomal recessive pattern, with affected individuals harboring pathogenic variants on both alleles of *FBXL4* and heterozygous carriers generally being clinically asymptomatic.[1][2][10][11]

The initial molecular delineation of this disorder came from whole-exome sequencing studies in consanguineous families with severe, fatal infantile encephalopathy, lactic acidosis, and mtDNA depletion, which identified recessive nonsense and splice-site mutations in *FBXL4* segregating with disease.[6][14] Subsequent clinical reviews and case reports have expanded the phenotype, but the core picture remains that of a severe, early-onset multisystem mitochondrial disease with prominent brain involvement and biochemical evidence of defective oxidative phosphorylation.[7][10][11][12] MedGen, GeneReviews, Orphanet, OMIM, and MedlinePlus consistently describe FBXL4-related MTDPS13 as a “multi-system disorder characterized primarily by congenital or early-onset lactic acidosis and growth failure, feeding difficulty, hypotonia, and developmental delay,” with additional neurologic features including seizures, movement disorders, ataxia, autonomic dysfunction, and stroke-like episodes in some cases.[2][11][17] Taken together, these aggregated descriptions from curated resources and the primary literature provide a coherent disease concept that integrates clinical, biochemical, genetic, and mechanistic dimensions.

### 1.2 Key Identifiers and Ontology Mappings

FBXL4-related MTDPS13 is represented in multiple disease ontologies and clinical classification systems, facilitating its integration into genomic databases and clinical decision support tools.[1][2][3][17][18] OMIM assigns the gene *FBXL4* the entry number 605654 and the associated mitochondrial DNA depletion syndrome 13 (encephalomyopathic type) the phenotype MIM number 615471.[1][2] Orphanet designates the condition “Mitochondrial DNA depletion syndrome, encephalomyopathic form with variable craniofacial anomalies” under ORPHA:369897.[3] MedGen lists the concept “Mitochondrial DNA depletion syndrome 13 (encephalomyopathic type)” with identifier C3809592 and notes synonyms such as “FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome.”[2][18] The Monarch Initiative maps this disease to MONDO:0014198, corresponding to the Mondo Disease Ontology term used in the user’s query.[2][4] SNOMED CT includes a code 765403009 associated with the FBXL4 gene entry, aligning the genetic defect with clinical terminologies used in electronic health records.[1]

The table below summarizes key identifiers and mappings for this disease based on curated resources.

| Resource | Identifier / Term | Notes |
|---------|-------------------|-------|
| OMIM gene | 605654 (*FBXL4*) | Nuclear gene encoding F-box/LRR protein 4[1][8] |
| OMIM phenotype | 615471 (MTDPS13) | “Mitochondrial DNA depletion syndrome 13 (encephalomyopathic type)”[1][2] |
| Orphanet | ORPHA:369897 | “Mitochondrial DNA depletion syndrome, encephalomyopathic form with variable craniofacial anomalies”[3] |
| MedGen | C3809592 | “Mitochondrial DNA depletion syndrome 13 (encephalomyopathic type)”[2][18] |
| MONDO | MONDO:0014198 | FBXL4-related encephalomyopathic mtDNA depletion syndrome[2][4] |
| SNOMED CT | 765403009 | Associated with FBXL4 gene; mitochondrial disease context[1] |

These identifiers allow cross-linking of FBXL4-related MTDPS13 across resources such as GeneReviews, ClinVar, the Genetic Testing Registry (GTR), and research data repositories, and underpin ontology-based annotation for knowledge bases focused on Mendelian diseases.[3][8][11][18] For example, the GeneReviews chapter “FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome” underlines the OMIM and Orphanet identifiers and provides diagnostic and management guidance, further embedding these mappings within clinical genomics practice.[11][12]

Suggested ontology terms for the disease entity include the Mondo term “FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome” (MONDO:0014198), the Orphanet term noted above, and the Human Phenotype Ontology (HPO) category “Mitochondrial DNA depletion syndrome” (HP:0031486) for grouping with related disorders caused by defects in mtDNA replication and maintenance.[2][3][18]

### 1.3 Synonyms and Alternative Names

The disease is known under several closely related names that reflect its causal gene, pathologic mechanism, and clinical presentation.[2][3][11][17] MedGen and MedlinePlus list “FBXL4-related encephalomyopathic mitochondrial DNA (mtDNA) depletion syndrome” as the primary descriptive name, emphasizing both the genetic origin in *FBXL4* and the combined brain–muscle involvement typical of encephalomyopathies.[2][17] OMIM uses the standardized designation “Mitochondrial DNA depletion syndrome 13 (encephalomyopathic type)” to distinguish this form from other numbered MTDPS subtypes caused by different nuclear genes.[1][2] Orphanet describes the same condition as “Mitochondrial DNA depletion syndrome, encephalomyopathic form with variable craniofacial anomalies,” highlighting the frequent presence of facial dysmorphic features.[3][10]

Other common synonyms include “FBXL4 deficiency,” “FBXL4-related early-onset mitochondrial encephalopathy,” “MTDPS13,” and “FBXL4-related mitochondrial DNA depletion syndrome.”[2][11][17] GeneReviews adopts “FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome” as its title and cross-references the OMIM numbers for both gene and phenotype.[11][12] These synonymous labels all refer to an identical clinical and genetic entity and differ mainly in emphasis rather than content. For ontology-based annotation, it is important to recognize all of these as alternative labels for MONDO:0014198 and ensure that they point to the same underlying disease concept.[2][3][18]

### 1.4 Source of Information: Patient-Level vs Aggregated Data

Information about FBXL4-related MTDPS13 in curated resources such as OMIM, Orphanet, MedGen, GeneReviews, and MedlinePlus is derived from aggregated analyses of published case reports, clinical series, and mechanistic studies, rather than directly from raw electronic health records.[1][2][3][10][11][12][17] For instance, OMIM synthesizes findings from the original gene discovery paper by Bonnen et al. (2013), the larger cohort described by Huemer et al. (2015), and additional case reports and biochemical characterizations.[1][6][10][14] Orphanet and MedGen similarly summarize clinical features and genetic associations from multiple published sources, noting that “to date FBXL4-related mtDNA depletion syndrome has been reported in 50 individuals,” a figure based on aggregated case counts up to circa 2017.[2][3]

GeneReviews provides an expert-authored narrative synthesis that integrates clinical, biochemical, genetic, and management information from primary literature and has been updated periodically as new cases and mechanistic insights have emerged.[11][12] MedlinePlus offers a patient-facing summary that distills key points from OMIM, GeneReviews, and NIH genetic databases into accessible language.[17] While individual case descriptions in the literature derive from patient-level data such as clinical histories, imaging, and tissue biopsies, the disease-level resources consulted here represent curated, aggregated knowledge designed for clinical and research use. This distinction is important for the knowledge base, as disease characteristics reported below reflect consensus patterns and ranges gleaned from multiple patients, rather than idiosyncratic features of single individuals.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis in FBXL4

The primary causal factor for FBXL4-related MTDPS13 is the presence of biallelic pathogenic or likely pathogenic variants in the nuclear gene *FBXL4*, encoding F-box and leucine rich repeat protein 4.[1][2][6][8][10][11] OMIM and MedGen both state that mitochondrial DNA depletion syndrome 13 is an autosomal recessive disorder associated with FBXL4 located at cytogenetic position 6q16.1–q16.2.[1][2] NCBI Gene describes *FBXL4* as a protein-coding gene encoding a member of the F-box protein family, characterized by an approximately 40 amino acid F-box motif that mediates interaction with SKP1 and incorporation into SCF (SKP1–Cullin–F-box) E3 ubiquitin ligase complexes, as well as multiple leucine-rich repeats that function in substrate recognition.[8] The gene is ubiquitously expressed across tissues, including thyroid, kidney, and at least 25 other sites, consistent with the multi-organ nature of the disease.[8]

Through whole-exome sequencing of consanguineous kindreds with fatal infantile encephalopathy, lactic acidosis, and severe mtDNA depletion, Bonnen et al. identified recessive nonsense and splicing mutations in *FBXL4* segregating with disease, thereby establishing FBXL4 as a mitochondrial protein essential for maintaining mtDNA integrity and stability.[6][14] In their words:

> “Through whole-exome sequencing, we identified recessive nonsense and splicing mutations in FBXL4 segregating in three unrelated consanguineous kindreds in which affected children present with a fatal encephalopathy, lactic acidosis, and severe mtDNA depletion in muscle.”[6][14]

Subsequent cohorts and case reports have identified a wide range of pathogenic variants across the gene, including truncating frameshift mutations, canonical splice-site deletions, nonsense mutations, and missense substitutions clustering in functionally important domains.[7][10][12][15][16] Huemer et al. reviewed 21 individuals with genetically confirmed FBXL4 deficiency and reported that “mutations were detected throughout the FBXL4 gene albeit with no clear delineation of a genotype–phenotype correlation,” underscoring that loss-of-function is the critical determinant rather than disruption of specific subdomains.[10]

ClinVar entries document several individual pathogenic variants associated with MTDPS13, including NM_001278716.2(FBXL4):c.1698A>G (p.Ile566Met), NM_001278716.2:c.1241T>C (p.Leu414Pro), NM_001278716.2:c.1389+3_1389+6del (splice-site deletion), and NM_001278716.2:c.1232G>A (p.Cys411Tyr).[4][5][15][16] These submissions, based on clinical testing and research studies, classify the variants as pathogenic or likely pathogenic under ACMG guidelines, and explicitly associate them with the clinical entity “Mitochondrial DNA depletion syndrome 13 (encephalomyopathic type)” with identifiers MONDO:0014198, OMIM:615471, and MedGen:C3809592.[4][5][15][16] Thus, the etiological foundation of FBXL4-related MTDPS13 is firmly established as nuclear gene loss-of-function affecting a mitochondrial quality control factor.

From a mechanistic standpoint, the disease reflects a deficiency of FBXL4’s role as the F-box substrate adaptor within an SCF ubiquitin ligase localized to the mitochondrial outer membrane, which normally mediates the ubiquitination and degradation of BNIP3 and BNIP3L/NIX mitophagy receptors to suppress mitophagy.[8][9][13] The Autophagy commentary by Kulkarni et al. succinctly states:

> “Here, we discuss our recent discovery that the SKP1-CUL1-F-box (SCF)-FBXL4 (F-box and leucine-rich repeat protein 4) E3 ubiquitin ligase localizes to the mitochondrial outer membrane, where it constitutively mediates the ubiquitination and degradation of BNIP3L/NIX and BNIP3 mitophagy receptors to suppress mitophagy.”[13]

Loss of FBXL4 thus leads to excessive mitophagy, reduced mitochondrial content, mtDNA depletion, and consequent respiratory chain dysfunction, providing a direct link from genetic lesion to pathophysiology.[7][9][13]

### 2.2 Genetic Risk Factors and Variant Spectrum

Under the autosomal recessive model, the main genetic risk factor for FBXL4-related MTDPS13 is being homozygous or compound heterozygous for pathogenic variants in *FBXL4*, typically in the context of parental consanguinity or small, isolated populations where founder mutations may be enriched.[6][10][11][16] Bonnen et al. emphasized that all their affected children were from consanguineous families and carried biallelic truncating or splice-site mutations, consistent with a recessive pattern in which carrier parents are unaffected.[6][14] Huemer et al. found that the majority of their 21 patients arose from consanguineous unions and reported that “the genetic diagnosis of FBXL4 deficiency has been established in 28 individuals” worldwide at the time of their publication, suggesting that clustering in certain families and communities may reflect founder effects and increased homozygosity.[10]

ClinVar and related genomic databases provide detailed insight into the variant spectrum of *FBXL4* and its clinical classification.[4][5][15][16] For example, the variant NM_001278716.2(FBXL4):c.1389+3_1389+6del is classified as pathogenic based on ACMG guidelines, with submission by the Wong Mito Lab stating that “FBXL4 defects are common in patients with congenital lactic acidemia and encephalomyopathic mitochondrial DNA depletion syndrome.”[15] This splice-site deletion is expected to disrupt normal RNA splicing and lead to loss of functional protein, representing a clear loss-of-function allele. Similarly, NM_001278716.2(FBXL4):c.1232G>A (p.Cys411Tyr) is classified as likely pathogenic, having been identified both in homozygous form and as part of compound heterozygous combinations in individuals with MTDPS13.[16] The ClinVar summary notes that although this missense variant is present at low frequency in the general population, its occurrence in affected individuals and functional domain suggests pathogenicity consistent with a recessive carrier model.[16]

Overall, the pathogenic variants in *FBXL4* span nonsense, frameshift, splice-site, and missense changes, with truncating mutations generally assumed to cause complete loss of function, while certain missense alterations may severely compromise protein stability, localization, or substrate interactions.[6][7][10][12][15][16] There is currently no strong evidence for dominant-negative or gain-of-function mechanisms; instead, all human data indicate that FBXL4-related MTDPS13 arises when overall FBXL4 activity is markedly reduced or absent due to biallelic loss-of-function, consistent with autosomal recessive inheritance.[6][10][11][13]

### 2.3 Environmental and Non-Genetic Risk Factors

No specific environmental toxins, infections, or lifestyle factors have been identified as primary causal agents or major risk modifiers for FBXL4-related MTDPS13, reflecting the disease’s origin as a monogenic, nuclear-encoded mitochondrial disorder.[2][10][11] Orphanet and MedlinePlus describe the condition as a genetic syndrome caused by mutations in *FBXL4* and do not list environmental exposures as independent risk factors.[3][17] GeneReviews and Huemer et al. emphasize that affected individuals present in the neonatal period or early infancy with severe lactic acidosis and encephalopathy, often in the absence of identifiable external precipitating events, and that the disease course is dominated by intrinsic mitochondrial dysfunction.[10][11]

Nevertheless, clinical experience suggests that common stressors such as intercurrent infections, surgical procedures, or fasting may exacerbate metabolic decompensation and lactic acidosis in affected children, analogous to other mitochondrial disorders.[10][11][12] While these episodes can precipitate acute deterioration and may contribute to mortality, they are best understood as triggers that unmask or worsen underlying mitochondrial failure rather than primary etiologic factors. To date, no epidemiological or mechanistic studies have systematically examined specific environmental exposures, dietary components, or maternal factors as modifiers of disease risk or severity in FBXL4-related MTDPS13, and thus, the knowledge base should regard environmental risk as largely speculative and secondary.

### 2.4 Protective Factors and Potential Modifiers

Given the rarity and severity of FBXL4-related MTDPS13, there is limited evidence regarding genetic or environmental protective factors that modulate susceptibility or disease course. Heterozygous carriers of pathogenic *FBXL4* variants, such as parents of affected children, are generally clinically normal, indicating that one functional allele suffices to maintain mitochondrial quality control under usual conditions.[6][10][11][16] This observation can be interpreted as a form of protection conferred by the intact allele, but it reflects the inherent recessive model rather than a specific variant-based protective effect.

Within affected individuals, variability in phenotype severity and survival suggests that residual FBXL4 function from hypomorphic missense alleles or alternative splicing might modulate disease, but published series have not identified clear genotype–phenotype correlations.[7][10][12] Huemer et al. explicitly reported that “mutations were detected throughout the FBXL4 gene albeit with no clear delineation of a genotype–phenotype correlation,” implying that any modifying effects are subtle or overshadowed by overall loss of function.[10] No modifier genes have been formally identified in human cohorts, though mechanistic work points to BNIP3 and BNIP3L/NIX as functionally downstream targets whose abundance and activity directly affect mitophagy, suggesting that variation in these genes could, in principle, alter disease severity.[9][13] However, this remains hypothetical and has not been demonstrated in clinical populations.

Environmental protective factors, such as optimized nutrition, avoidance of metabolic stress, and early supportive care, likely improve short-term outcomes and quality of life but do not fundamentally alter the underlying mitochondrial defect.[10][11][12] No dietary supplements, vitamins, or pharmacologic agents have proven protective in prospective trials, and Huemer et al. concluded that “treatment with ‘mitochondrial medications’ did not prove effective,” underscoring the absence of established protective therapies.[10] Therefore, for the current knowledge base, it is reasonable to state that no specific genetic or environmental protective factors have been validated for FBXL4-related MTDPS13, beyond the general benefit of standard supportive care in severe pediatric mitochondrial disorders.

### 2.5 Gene–Environment Interactions

Given the monogenic etiology of FBXL4-related MTDPS13 and the absence of identified external causal agents, gene–environment interactions in this disease are not well characterized and are likely to be indirect. The primary interaction involves the way that environmental stressors—such as infection, fever, fasting, or surgery—increase energy demands and metabolic load on tissues that are already compromised by mitochondrial dysfunction, thereby exacerbating lactic acidosis, encephalopathy, and organ failure.[10][11][12] This pattern, common in many mitochondrial diseases, reflects a generic gene–environment interplay where a genetically determined defect in oxidative phosphorylation diminishes physiologic reserve, making affected individuals vulnerable to otherwise manageable stressors.

Mechanistic studies in cell lines and mice have shown that FBXL4 deficiency leads to increased lysosomal turnover of mitochondria and upregulation of lysosomal proteins, indicating that environmental or pharmacologic factors influencing autophagy or lysosomal function could, in principle, modify disease phenotype.[9][13] For example, the EMBO Molecular Medicine study demonstrated that inhibition of lysosomal function in FBXL4-deficient fibroblasts reversed the mitochondrial phenotype, suggesting that environmental or therapeutic modulation of lysosomal activity might interact with the genetic defect to alter mitochondrial content and function.[9] Kulkarni et al. further discussed how cellular conditions or signaling events that prevent FBXL4-mediated turnover of BNIP3L and BNIP3 would facilitate selective removal of specific mitochondria, implying that stress pathways activating these mitophagy receptors may amplify disease in the absence of FBXL4.[13]

Despite these insights, there are no human data demonstrating specific environmental interventions that consistently ameliorate or exacerbate FBXL4-related MTDPS13 via defined molecular mechanisms. Accordingly, the knowledge base should treat gene–environment interactions as an area of emerging mechanistic interest rather than established clinical doctrine, noting that future work on mitophagy and autophagy modulation may yield more detailed interaction models.

## 3. Phenotypes

### 3.1 Global Clinical Phenotype and Age of Onset

FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome presents as a severe, multisystem disorder that almost invariably begins in the neonatal period or early infancy.[2][10][11][17] MedGen and MedlinePlus emphasize that the condition “is a severe condition that begins in infancy and affects multiple body systems,” and that infants have weak muscle tone (hypotonia), difficulty growing and gaining weight, and lactic acidosis.[2][17] Huemer et al., reviewing 21 individuals with genetically confirmed FBXL4 deficiency, reported that “neonatal/early-onset severe lactic acidosis, muscular hypotonia, feeding problems and failure to thrive is the characteristic pattern at first presentation,” underscoring the consistency of early severe manifestations.[10] GeneReviews similarly notes that onset is typically in the neonatal period or the first months of life, with very few patients surviving beyond early childhood and all survivors having profound neurodevelopmental disability.[11][12]

Symptom severity is generally marked; MTDPS13 is among the more severe mtDNA depletion syndromes, with high mortality and extensive multisystem involvement.[7][10][11][12] The disease course is progressive, with ongoing neurodegeneration, worsening brain atrophy, and accumulation of metabolic derangements, although some features such as facial dysmorphism and congenital cataracts are static anomalies present from birth.[7][10][12] Clinical variability exists, particularly regarding the presence or absence of cardiac involvement, craniofacial anomalies, and immune or bone marrow dysfunction, but the core encephalomyopathic phenotype and lactic acidosis are nearly universal in reported cases.[7][10][11][17]

Quality of life impact is profound. Surviving children exhibit severe psychomotor retardation, are typically non-ambulatory and non-verbal, require extensive feeding support, and often depend on caregivers for all activities of daily living.[10][11][12] Frequent hospitalizations for metabolic crises, infections, or cardiac events further compromise well-being and impose substantial burden on families. In Huemer’s cohort, all survivors had severe developmental delay, and several had significant feeding problems requiring interventions.[10] Taken together, FBXL4-related MTDPS13 can be characterized as a globally disabling pediatric mitochondrial encephalomyopathy with early onset, severe and progressive course, and major negative impact on quality of life.

Suggested high-level HPO terms for the general disease phenotype include “Encephalopathy” (HP:0001298), “Hypotonia” (HP:0001252), “Global developmental delay” (HP:0001263), “Lactic acidosis” (HP:0003128), and “Failure to thrive” (HP:0001508).[2][10][11][17]

### 3.2 Neurologic and Developmental Phenotypes

Neurologic involvement is central to FBXL4-related MTDPS13 and largely defines its clinical identity as an encephalomyopathic syndrome.[2][6][7][10][11][12][17] Bonnen et al. described affected children as presenting with “a fatal encephalopathy, lactic acidosis, and severe mtDNA depletion in muscle,” noting features such as microcephaly, severe global developmental delay, hypotonia, and cerebral atrophy on MRI.[6][14] In their series, many children had congenital microcephaly, generalized cerebral atrophy, and progressive neurodegeneration, with age at death typically within the first few years of life.[14] Huemer et al. similarly found that “all survivors developed severe psychomotor retardation,” and that brain imaging in neonates was initially nonspecific but evolved to show rapidly progressive brain atrophy.[10]

Common neurologic phenotypes include generalized hypotonia, global developmental delay, microcephaly, seizures, movement disorders, and abnormalities of tone and reflexes.[7][10][11][12] Hypotonia is often noted at birth and persists throughout life, contributing to delayed motor milestones, poor head control, and inability to sit or walk independently.[10][11][12] Global developmental delay encompasses deficits across gross motor, fine motor, speech, and cognitive domains, with many children lacking meaningful language or interactive behaviors.[10][11] Microcephaly, defined by head circumference below the third centile, is present in a substantial proportion of patients, reflecting underlying brain growth impairment.[6][10][11][14] Seizures, including generalized tonic–clonic and focal events, have been reported in several cases, sometimes associated with cortical atrophy or white matter lesions on MRI.[7][10][12]

Brain imaging findings are notable. Huemer et al. reported that neonatal MRI was often nonspecific, but later imaging showed a pattern of rapidly progressive brain atrophy.[10] In one patient described by Gai et al. and later in Huemer’s series, cystic white matter lesions and marked cerebral atrophy were observed, correlating with severe encephalopathy.[7][10] A case report summarized by Almannai et al. described a girl with FBXL4-related MTDPS13 who developed cerebral atrophy and significant neurodevelopmental delay, with MRI demonstrating progressive cortical thinning.[12] These imaging features suggest selective vulnerability of cortical and white matter neurons to mitochondrial dysfunction and mtDNA depletion.

Quality of life impact of neurologic involvement is extreme. Children are often unable to communicate, ambulate, or participate in age-appropriate activities, and may experience recurrent seizures and distressing episodes of encephalopathy.[10][11][12] Suggested HPO terms for specific neurologic phenotypes include “Encephalopathy” (HP:0001298), “Hypotonia” (HP:0001252), “Global developmental delay” (HP:0001263), “Microcephaly” (HP:0000252), “Seizures” (HP:0001250), “Cerebral atrophy” (HP:0002059), and “White matter abnormalities” (HP:0002500).[6][7][10][11][12][14]

### 3.3 Muscular, Growth, and Feeding Phenotypes

Muscular weakness and growth failure are prominent features of FBXL4-related MTDPS13 and strongly impact clinical management.[2][7][10][11][17] MedlinePlus notes that infants with FBXL4-related encephalomyopathic mtDNA depletion syndrome “have weak muscle tone (hypotonia) and difficulty growing and gaining weight at the expected rate (faltering weight).”[17] Huemer et al. described “muscular hypotonia, feeding problems and failure to thrive” as part of the characteristic initial pattern, with elevated creatine kinase observed in approximately 45% of measurements, suggesting muscle membrane or metabolic stress.[10] Bonnen et al. likewise reported muscular hypotonia and a severe respiratory chain defect in muscle biopsies, consistent with an underlying myopathy.[6][14]

Failure to thrive manifests as poor weight gain, short stature, and reduced muscle bulk, despite adequate caloric intake, reflecting chronic energy deficit due to impaired oxidative phosphorylation.[10][11][17] Feeding difficulties include poor suck, dysphagia, vomiting, and aspiration risk, often necessitating nasogastric or gastrostomy tube feeding for long-term nutritional support.[10][11][12] These issues contribute to increased healthcare utilization and caregiver burden and create ongoing challenges in maintaining adequate caloric and protein intake in a child with high metabolic vulnerability.

Muscle biopsies in some patients reveal non-specific myopathic changes, combined respiratory chain defects, and mtDNA depletion, identifying a biochemical myopathy underlying the clinical hypotonia and weakness.[6][7][10][14] Functional tests, such as electromyography, have not been systematically reported but are likely to show myopathic patterns. Quality of life impact includes reduced mobility, dependence on assistive devices and caregivers, and frequent feeding interventions.

Suggested HPO terms include “Muscular hypotonia” (HP:0001252), “Myopathy” (HP:0003198), “Failure to thrive” (HP:0001508), “Feeding difficulties” (HP:0011010), and “Elevated serum creatine kinase” (HP:0003236).[7][10][11][17]

### 3.4 Metabolic Phenotypes: Lactic Acidosis and Hyperammonemia

Metabolic derangements, especially persistent lactic acidosis, are hallmark features of FBXL4-related MTDPS13 and reflect underlying defects in oxidative phosphorylation and energy metabolism.[2][6][7][10][11][17] MedlinePlus states that “All individuals with FBXL4-related encephalomyopathic mtDNA depletion syndrome have a buildup of a chemical called lactic acid in the body (lactic acidosis), and about half of individuals have an accumulation of ammonia in the blood,” emphasizing the near-universal presence of lactic acidosis and frequent hyperammonemia.[17] Huemer et al. found elevated blood lactate and metabolic acidosis in all 21 individuals in their cohort, with creatine kinase elevation in 45% of measurements, and described the lactic acidosis as “persistent” and often severe.[10] Bonnen et al. likewise reported lactic acidosis in affected children and demonstrated severe combined respiratory chain defects, consistent with impaired oxidative phosphorylation driving increased anaerobic glycolysis and lactate accumulation.[6][14]

Hyperammonemia, while not universal, occurs in a substantial subset of patients and may exacerbate encephalopathy and contribute to episodes of acute decompensation.[2][10][17] In MedlinePlus, it is noted that “about half of individuals have an accumulation of ammonia in the blood,” implying a frequency of approximately 50% among reported cases.[17] Elevated ammonia likely reflects secondary effects on hepatic function or urea cycle activity, potentially due to mitochondrial dysfunction in hepatocytes and other tissues.

Other metabolic abnormalities include elevated transaminases, metabolic acidosis, and abnormal acylcarnitine profiles, though these are less consistently reported.[7][10][12] Collectively, these biochemical features confirm that FBXL4 deficiency causes a broad mitochondrial energy metabolism defect, in which decreased mtDNA copy number and respiratory chain function force reliance on glycolysis and perturb intermediary metabolism.

Quality of life impact is considerable, as recurrent metabolic crises necessitate frequent hospitalizations, intravenous bicarbonate or other interventions, and careful management of nutrition and infections.[10][11][12] Suggested HPO terms include “Lactic acidosis” (HP:0003128), “Metabolic acidosis” (HP:0001942), “Hyperammonemia” (HP:0001987), and “Elevated serum lactate” (HP:0002151).[2][10][17]

### 3.5 Cardiac Phenotypes

Cardiac involvement is increasingly recognized as a prominent feature of FBXL4-related MTDPS13 and contributes significantly to morbidity and mortality.[7][9][10][11] Huemer et al. reported central nervous system and cardiac involvement in their neonate with total FBXL4 deficiency, including cardiomyopathy and arrhythmias, and broader case series have documented congenital heart malformations and pulmonary hypertension.[7][10] A comprehensive review of mitochondrial DNA depletion syndromes and their cardiac manifestations in Frontiers in Cardiovascular Medicine summarized FBXL4-related MTDPS13 as having cardiac involvement in 54% of cases, including cardiomyopathy (27%), congenital heart malformations (19%), arrhythmia (15%), and pulmonary hypertension (11%).[11] In their table, FBXL4 is categorized under “Other pathways: protein homeostasis” with clinical features described as encephalomyopathy and mtDNA depletion.[11]

The review further notes that “Among the MTDPS13, the cardiac involvement was observed in 54% of cases (20/37), with specific manifestations including cardiomyopathy (27%, 10/37), congenital heart malformations (19%, 7/37), arrhythmia (15%, 6/41), and pulmonary hypertension (11%, 4/37).”[11] This quantitative summary underscores that more than half of reported patients have some form of cardiac pathology, and that cardiomyopathy is the single most common cardiac phenotype. Mechanistic work in adult mouse models of heart failure with preserved ejection fraction has shown that transfection of FBXL4 can rescue cardiac geometry and mitochondrial integrity with altered mitochondrial dynamics, providing experimental support that FBXL4 plays a protective role in cardiac mitochondrial homeostasis.[11]

Cardiac phenotypes in FBXL4-related MTDPS13 likely arise from the same mechanistic pathway as neurologic and muscular involvement—namely, excessive mitophagy leading to reduced mitochondrial content, mtDNA depletion, and respiratory chain dysfunction in cardiomyocytes, resulting in energy failure, structural remodeling, and conduction system abnormalities.[9][11][13] Clinically, cardiomyopathy may present as dilated or hypertrophic patterns, with reduced systolic or diastolic function, while arrhythmias can include tachycardias or conduction blocks.[7][10][11] Pulmonary hypertension may result from chronic hypoxia or structural cardiac anomalies.

Quality of life impact includes increased risk of heart failure, sudden cardiac death, limitations in physical activity, and additional treatment burden from medications, device therapies, or hospitalizations.[10][11] Suggested HPO terms include “Cardiomyopathy” (HP:0001626), “Congenital heart malformation” (HP:0001272), “Arrhythmia” (HP:0011675), and “Pulmonary hypertension” (HP:0002093).[7][10][11]

### 3.6 Craniofacial and Dysmorphic Phenotypes

Craniofacial anomalies and facial dysmorphism are common in FBXL4-related MTDPS13 and contribute to the characteristic clinical gestalt.[7][10][11][12] Huemer et al. reported that “facial dysmorphic features are present in 67% of cases,” indicating that approximately two-thirds of affected individuals show recognizable craniofacial differences.[10] These may include deep-set eyes, high-arched palate, micrognathia, and other subtle anomalies, though precise patterns vary among patients and are not currently linked to specific genotypes.[7][10][12]

Orphanet describes the disease as “encephalomyopathic form with variable craniofacial anomalies,” highlighting that dysmorphism is an important but variable component.[3] GeneReviews and case reports also mention craniofacial dysmorphism, though they focus primarily on functional deficits rather than detailed morphological description.[11][12] In the case study summarized by Almannai et al., the girl with homozygous nonsense FBXL4 mutation had dysmorphic features and cerebral atrophy, further supporting the association.[12]

Quality of life impact of craniofacial anomalies is generally minor compared to the profound neurologic and metabolic impairments, but they can aid in clinical recognition and may have implications for feeding, speech, and airway management.[10][11][12] Suggested HPO terms include “Facial dysmorphism” (HP:0001999), “Craniofacial dysmorphism” (HP:0001999), and more specific terms as needed (e.g., “Micrognathia” HP:0000347) once detailed phenotyping is available.[3][10][11]

### 3.7 Ophthalmologic Phenotypes

Ophthalmologic involvement, particularly congenital cataracts, has been observed in several patients with FBXL4-related MTDPS13 and may be part of the broader encephalomyopathic phenotype.[7][10][11] Huemer et al. mention “congenital cataract” among the variable clinical findings in their cohort, although exact frequencies are not specified.[7][10] Bonnen et al. reported eye involvement in some subjects, including cataracts and optic nerve abnormalities, aligning with a general pattern of mitochondrial disease affecting high-energy tissues such as the retina and lens.[6][14]

While ocular phenotypes are not as prominent or universal as neurologic, metabolic, or cardiac features, they can contribute to visual impairment and may complicate developmental assessment and rehabilitation.[10][11][12] Suggested HPO terms include “Congenital cataract” (HP:0000519) and “Visual impairment” (HP:0000505), with more specific terms added as detailed case descriptions accumulate.[7][10][11]

### 3.8 Immune, Hematologic, and Other Systemic Phenotypes

FBXL4-related MTDPS13 can involve multiple additional organ systems, including bone marrow, immune system, and lungs, though these features are less systematically reported.[7][10][11] In the detailed biochemical characterization by Gai et al., a neonate with total FBXL4 deficiency exhibited “CNS, cardiac, and bone marrow involvement, and multicomplex respiratory chain dysfunction associated with mtDNA depletion,” suggesting that hematopoietic tissues may be affected by mitochondrial dysfunction.[7] Huemer et al. noted immunodeficiency in one severely affected patient, with recurrent infections and laboratory evidence of immune compromise.[7][10] Pulmonary hypertension, as noted in the cardiac section, reflects interactions between cardiac and pulmonary vascular systems.[11]

These multisystem features reinforce that FBXL4 is widely expressed and participates in mitochondrial quality control across diverse tissues, so its loss can manifest in any high-energy organ or cell type.[8][9][13] Quality of life and morbidity impacts include recurrent infections, anemia or cytopenias, and respiratory complications, all of which require specialized management and increase overall disease burden.[10][11]

Suggested HPO terms for these features include “Immunodeficiency” (HP:0002721), “Bone marrow failure” (HP:0001876), “Recurrent respiratory infections” (HP:0002205), and “Pulmonary hypertension” (HP:0002093).[7][10][11]

### 3.9 Phenotype Frequencies and Summary Table

Published series provide approximate frequencies for key phenotypes, although numbers are limited and may evolve as more cases are reported. Huemer et al. described 21 individuals in detail, while the Frontiers in Cardiovascular Medicine review summarized cardiac involvement in 37 cases.[10][11] The table below synthesizes available data on selected phenotypes.

| Phenotype | Type | Approximate Frequency among reported cases | Evidence |
|-----------|------|--------------------------------------------|----------|
| Neonatal/early-onset lactic acidosis | Metabolic symptom | Nearly 100% (all individuals in Huemer cohort) | Huemer et al. 2015[10]; MedlinePlus[17] |
| Muscular hypotonia | Clinical sign | Nearly 100% | Huemer et al. 2015[10]; MedGen[2] |
| Feeding problems/failure to thrive | Symptom | Nearly 100% | Huemer et al. 2015[10]; MedlinePlus[17] |
| Severe global developmental delay | Symptom | Nearly 100% among survivors | Huemer et al. 2015[10]; GeneReviews[11] |
| Facial dysmorphic features | Physical manifestation | ~67% (14/21) | Huemer et al. 2015[10] |
| Cardiac involvement (any) | Organ involvement | ~54% (20/37) | Frontiers CVMed review[11] |
| Cardiomyopathy | Organ involvement | ~27% (10/37) | Frontiers CVMed review[11] |
| Congenital heart malformations | Organ involvement | ~19% (7/37) | Frontiers CVMed review[11] |
| Arrhythmia | Organ involvement | ~15% (6/41) | Frontiers CVMed review[11] |
| Pulmonary hypertension | Organ involvement | ~11% (4/37) | Frontiers CVMed review[11] |
| Hyperammonemia | Laboratory abnormality | ~50% | MedlinePlus[17]; MedGen[2] |

These frequencies should be interpreted cautiously due to small sample sizes and potential ascertainment bias, but they provide useful quantitative anchors for phenotype annotation in the knowledge base.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: FBXL4

FBXL4 (F-box and leucine rich repeat protein 4) is the sole causal gene currently known for MTDPS13 and is central to the disease’s genetic and molecular profile.[1][2][3][6][8][9][11][13] The gene is located on chromosome 6q16.1–q16.2, as mapped by initial cytogenetic studies and later refined by genomic coordinates (GRCh38: 6:98,868,535–98,947,946).[1][3] It encodes a protein that belongs to the F-box family, characterized by an approximately 40 amino acid F-box motif that mediates binding to SKP1 and incorporation into SCF ubiquitin ligase complexes.[8] In addition to the F-box domain, FBXL4 contains at least nine tandem leucine-rich repeats (LRRs), which typically function in substrate recognition and protein–protein interactions.[8]

NCBI Gene summarizes FBXL4’s function as follows:

> “This gene encodes a member of the F-box protein family, which are characterized by an approximately 40 amino acid motif, the F-box. F-box proteins constitute one subunit of modular E3 ubiquitin ligase complexes, called SCF complexes, which function in phosphorylation-dependent ubiquitination. The F-box domain mediates protein–protein interactions and binds directly to S-phase kinase-associated protein 1. In addition to an F-box domain, the encoded protein contains at least 9 tandem leucine-rich repeats. The ubiquitin ligase complex containing the encoded protein may function in cell-cycle control by regulating levels of lysine-specific demethylase 4A. Alternative splicing results in multiple transcript variants.”[8]

Recent work has refined this understanding in the mitochondrial context, showing that the SCF-FBXL4 complex localizes to the mitochondrial outer membrane and specifically targets the mitophagy receptors BNIP3L/NIX and BNIP3 for ubiquitination and proteasomal degradation, thereby suppressing mitophagy.[9][13] Gene Ontology annotations in NCBI Gene indicate that FBXL4 enables protein binding and “ubiquitin-like ligase-substrate adaptor activity” and is involved in “SCF-dependent proteasomal ubiquitin-dependent protein catabolic process,” “autophagy of mitochondrion,” and “negative regulation of mitophagy,” among other processes.[8]

Alternative splicing generates multiple transcript variants of FBXL4, some of which may differ in subcellular localization or regulatory properties, though the majority of disease-causing mutations appear to affect exons common to all major isoforms.[8][10][12] FBXL4 is expressed ubiquitously, with detectable levels in thyroid, kidney, and at least 25 other tissues, aligning with the multi-organ nature of FBXL4-related MTDPS13.[8]

Suggested ontology terms for FBXL4 include the HGNC gene symbol “FBXL4” (HGNC:13601), the UniProtKB entry Q9UKA2, and GO terms such as “mitophagy” (GO:0000422), “SCF-dependent proteasomal ubiquitin-dependent protein catabolic process” (GO:0010498), and “mitochondrial outer membrane” (GO:0005741).[3][8][9][13]

### 4.2 Pathogenic Variants: Types, Classification, and Frequencies

Pathogenic variants in *FBXL4* associated with MTDPS13 span a wide spectrum of types, including nonsense mutations, frameshift insertions/deletions, canonical splice-site mutations, and missense variants in conserved domains.[6][7][10][12][15][16] Bonnen et al. identified recessive nonsense and splicing mutations in FBXL4 segregating in affected children, including truncating mutations such as c.1555C>T (p.Gln519*) and splice-site changes that lead to aberrant transcripts and loss of function.[6][14] Huemer et al. reported multiple variants across the gene, with no clear clustering by exon or domain, and noted that genotypes included both homozygous and compound heterozygous combinations.[10]

ClinVar provides detailed classification of several FBXL4 variants, many of which are documented in individuals with MTDPS13.[4][5][15][16] For example, NM_001278716.2(FBXL4):c.1698A>G (p.Ile566Met) is a missense single nucleotide variant located at cytogenetic position 6q16.1, and is associated with MTDPS13; while its clinical significance is not fully elaborated in the summary, it is listed under single nucleotide variant type and linked to the disease concept via MONDO:0014198 and OMIM:615471, implying pathogenic or likely pathogenic classification by submitters.[4] Another variant, NM_001278716.2(FBXL4):c.1241T>C (p.Leu414Pro), is a missense change at genomic location Chr6:98899344 (GRCh38) and is explicitly associated with MTDPS13; multiple submissions classify it under pathogenic categories, and it likely disrupts protein function within the LRR domain or adjacent regions.[5]

Splice-site variants such as NM_001278716.2(FBXL4):c.1389+3_1389+6del are particularly informative. This variant involves deletion of nucleotides at the +3 to +6 positions of the intron following exon 11, disrupting normal splicing signals and causing aberrant transcripts. The Wong Mito Lab classified this variant as pathogenic based on ACMG guidelines and emphasized that “FBXL4 defects are common in patients with congenital lactic acidemia and encephalomyopathic mitochondrial DNA depletion syndrome.”[15] The deletion is cataloged under dbSNP rs1554216735, with genomic coordinates NC_000006.12:g.98880549_98880552del.[15]

The missense variant NM_001278716.2(FBXL4):c.1232G>A (p.Cys411Tyr) has received particular attention. ClinVar summarizes that this variant is classified as likely pathogenic by multiple laboratories, including Baylor College of Medicine, Fulgent Genetics, and the Broad Center for Mendelian Genomics, based on ACMG criteria.[16] It has been observed both in homozygous form and as part of compound heterozygous genotypes in individuals with MTDPS13, and its low allele frequency in population databases is consistent with a recessive carrier model.[16] The ClinVar summary notes that “Computational prediction tools and conservation analyses do not provide strong support for or against an impact to the protein. In summary, although additional studies are required to fully establish its clinical significance, this variant is likely pathogenic,” illustrating the nuanced interpretation of missense variants in critical domains.[16]

In terms of allele frequencies, ClinVar notes that p.Cys411Tyr is present in the general population at a very low frequency, compatible with an autosomal recessive disorder where carriers are rare but do exist.[16] Precise gnomAD frequency data are not provided in the search results, but the overall pattern indicates that pathogenic FBXL4 variants are extremely rare, consistent with the rarity of MTDPS13.[10][11][16] All pathogenic variants described are germline in origin; ClinVar explicitly notes that somatic classification and oncogenicity categories are “None” for these entries, reflecting that FBXL4-related MTDPS13 is a germline Mendelian disease rather than a somatic cancer syndrome.[4][5][15][16]

From a functional perspective, most truncating and splice-site variants are assumed to cause complete loss of FBXL4 function, whether through nonsense-mediated decay, production of truncated proteins lacking critical domains, or aberrant splicing leading to nonfunctional products.[6][7][10][12][15] Missense variants are believed to cause loss of function by destabilizing the protein, disrupting substrate binding, or impairing interactions with SKP1 or other SCF components, though detailed biochemical characterization is available for only a subset.[7][9][13][16] No FBXL4 variants have been reported to cause gain-of-function or dominant-negative effects in humans, and there is no evidence for somatic variants driving cancer or other adult-onset disorders in the current literature.[4][5][15][16]

### 4.3 Modifier Genes and Genetic Interactions

No definitive modifier genes have been identified for FBXL4-related MTDPS13 in human cohorts, despite variability in phenotype severity and organ involvement among individuals with similar genotypes.[7][10][11][12] Mechanistically, the downstream targets of FBXL4, BNIP3 and BNIP3L/NIX, are likely candidates for genetic interactions, as their abundance and activity directly influence mitophagy and mitochondrial turnover.[9][13] The EMBO Molecular Medicine study demonstrated that FBXL4 deficiency leads to accumulation of BNIP3 and BNIP3L, driving excessive mitophagy via lysosomal pathways and decreasing mitochondrial content.[9] Kulkarni et al. highlighted that FBXL4-mediated ubiquitination and degradation of BNIP3 and BNIP3L is a key suppressive mechanism for mitophagy, and that disruptions to this pathway in MTDPS13 lead to elevated mitophagy.[13]

It is therefore plausible that genetic variation in BNIP3, BNIP3L, or other mitophagy regulators (such as PINK1, PRKN/Parkin, and FUNDC1) might modulate disease severity in FBXL4-deficient individuals, though this remains speculative in the absence of direct evidence.[9][13] Similarly, genes involved in mtDNA replication and maintenance (e.g., *POLG*, *TK2*, *DGUOK*) could interact with FBXL4 deficiency to further impact mtDNA copy number, but again, human data are lacking.[11][12]

For now, the knowledge base should note that no validated modifier genes have been published for FBXL4-related MTDPS13, while acknowledging mechanistic hypotheses that may guide future investigations.

### 4.4 Epigenetic and Chromosomal Abnormalities

There is currently no evidence that epigenetic alterations, such as DNA methylation or histone modifications at the *FBXL4* locus, play a primary role in the etiology of MTDPS13, nor that large-scale chromosomal abnormalities involving 6q16.1–q16.2 are common in affected individuals.[1][2][10][11] OMIM and MedGen characterize the disease as arising from sequence-level mutations within the FBXL4 gene, and neither resource mentions chromosomal rearrangements or epigenetic dysregulation as typical features.[1][2] Huemer et al. and other clinical series likewise focus on point mutations and small indels identified by sequencing, without reporting karyotypic anomalies or imprinting defects.[10][11][12]

DECIPHER and similar structural variant databases are not referenced in the search results, suggesting that no recurrent deletions or duplications encompassing FBXL4 have been firmly linked to MTDPS13. Epigenetic profiling of FBXL4-related MTDPS13 has not been reported in the literature identified here, and thus any epigenetic contributions remain speculative. The pathophysiology appears to be driven primarily by protein-level loss of function due to DNA sequence variants, rather than by regulatory epigenetic changes.

## 5. Environmental Information

### 5.1 Environmental Factors

As a classic monogenic mitochondrial maintenance disorder, FBXL4-related MTDPS13 does not have known primary environmental causes, and environmental factors are best viewed as modulators of disease expression rather than etiologic agents.[2][10][11][17] Neither MedGen nor MedlinePlus lists toxins, radiation, pollution, or occupational exposures as causative factors; instead, they emphasize that “As its name suggests, FBXL4-related encephalomyopathic mtDNA depletion syndrome is caused by mutations in the FBXL4 gene.”[2][17] Orphanet similarly categorizes the disease under genetic disorders and does not mention environmental triggers.[3]

Nevertheless, clinical experience in mitochondrial medicine indicates that environmental stressors can exacerbate symptoms and precipitate acute decompensation. In FBXL4-related MTDPS13, infections, fasting, fever, and surgical procedures may increase energy demand and metabolic strain on tissues already compromised by respiratory chain defects, leading to worsening lactic acidosis, encephalopathy, and organ dysfunction.[10][11][12] For example, episodes of severe lactic acidosis in Huemer’s cohort were often associated with intercurrent illnesses or surgical stress, although underlying metabolic vulnerability persists independent of such events.[10] These environmental interactions are nonspecific and common to many mitochondrial disorders, lacking disease-specific evidence in FBXL4 deficiency.

No studies have systematically assessed environmental pollutants, drugs, or dietary components as risk factors or triggers for MTDPS13, and thus the knowledge base should not list specific environmental agents as established contributors. The primary environmental recommendation remains to minimize metabolic stress and avoid exposures known to exacerbate mitochondrial dysfunction, such as certain anesthetic agents or valproic acid, in line with general mitochondrial disease guidelines, but these are extrapolations rather than FBXL4-specific findings.[10][11]

### 5.2 Lifestyle and Infectious Factors

Lifestyle factors such as smoking, alcohol consumption, and exercise patterns are generally not relevant in the neonatal and early childhood population affected by FBXL4-related MTDPS13, and no studies have linked parental lifestyle to disease risk.[10][11][17] Similarly, infectious agents are not known to cause this disease, although infections may precipitate metabolic crises and contribute to morbidity and mortality.[10][11][12] Immune impairment in some patients may predispose to recurrent infections, but this is a consequence of disease rather than an external risk factor.[7][10]

Given this context, environmental and lifestyle information for FBXL4-related MTDPS13 can be summarized as follows: the disease is primarily genetic, environmental exposures are not known to cause or prevent it, and the main environmental considerations involve supportive management to avoid metabolic stress and promptly treat infections.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

Step 1: Biallelic loss-of-function mutations in *FBXL4* lead to deficient or absent FBXL4 protein function in the mitochondrial outer membrane SCF-FBXL4 E3 ubiquitin ligase complex.[6][8][9][13]

Step 2: Loss of FBXL4 activity results in reduced ubiquitination and proteasomal degradation of the mitophagy receptors BNIP3 and BNIP3L/NIX, causing their accumulation on the mitochondrial outer membrane and inferred increased mitophagy signaling.[9][13]

Step 3: Accumulated BNIP3/BNIP3L, together with other mitophagy machinery, leads to excessive autophagic removal of mitochondria via lysosomal pathways, resulting in a global decrease in cellular mitochondrial content; this is demonstrated in patient fibroblasts, FBXL4 knockout mice, and CRISPR/Cas9 FBXL4 knockout human cell lines.[7][9][13]

Step 4: Reduced mitochondrial content is accompanied by depletion of mtDNA copy number and decreased steady-state levels of multiple mitochondrial proteins, including respiratory chain components, resulting in combined multiple respiratory chain complex deficiencies and impaired oxidative phosphorylation.[6][7][9][10][14]

Step 5: Impaired oxidative phosphorylation leads to decreased ATP production, loss of mitochondrial membrane potential, fragmentation of the mitochondrial network, and enlarged mitochondrial nucleoids, as demonstrated in patient fibroblasts, contributing to cellular energy failure and metabolic reprogramming toward glycolysis.[6][7][14]

Step 6: Reliance on glycolysis and reduced oxidative phosphorylation result in systemic lactic acidosis and metabolic acidosis, with elevated lactate and frequent hyperammonemia in affected individuals, as consistently observed in clinical cohorts.[2][10][17]

Step 7: Chronic energy deficit and metabolic derangements in high-demand tissues such as brain, heart, and skeletal muscle cause encephalopathy, hypotonia, cardiomyopathy, failure to thrive, and multi-organ dysfunction, leading to the clinical phenotype of FBXL4-related MTDPS13 and, frequently, early death.[6][7][10][11][12][14]

Step 8: In some patients, additional downstream consequences include immune dysfunction, bone marrow involvement, and pulmonary hypertension, inferred to arise from mitochondrial failure in hematopoietic and vascular tissues, although mechanisms are less directly demonstrated.[7][10][11]

This causal chain integrates demonstrated molecular and cellular mechanisms with inferred tissue-level and clinical outcomes, providing a coherent pathophysiological narrative.

### 6.2 Molecular Pathways: SCF-FBXL4, Mitophagy, and Autophagy

The core molecular pathway implicated in FBXL4-related MTDPS13 is the SCF-FBXL4 ubiquitin ligase–mediated suppression of mitophagy via BNIP3 and BNIP3L/NIX turnover.[8][9][13] FBXL4 serves as the F-box substrate adaptor within an SCF-type E3 ubiquitin ligase complex composed of SKP1, CUL1, and RBX1, localized to the mitochondrial outer membrane.[8][13] Under normal conditions, this SCF-FBXL4 complex constitutively ubiquitinates BNIP3L/NIX and BNIP3, tagging them for proteasomal degradation and thereby preventing excessive activation of mitophagy.[9][13]

Kulkarni et al. summarize this mechanism:

> “Our recent discovery that the SKP1-CUL1-F-box (SCF)-FBXL4 (F-box and leucine-rich repeat protein 4) E3 ubiquitin ligase localizes to the mitochondrial outer membrane, where it constitutively mediates the ubiquitination and degradation of BNIP3L/NIX and BNIP3 mitophagy receptors to suppress mitophagy.”[13]

In FBXL4 deficiency, this pathway is disrupted. EMBO Molecular Medicine’s study of FBXL4 knockout mice, patient fibroblasts, and CRISPR/Cas9 knockout human cells demonstrated that FBXL4-deficient cells have reduced steady-state levels of mitochondrial proteins, mtDNA depletion, and upregulation of lysosomal proteins.[9] Proteomic analyses revealed a global reduction in mitochondrial proteins and concomitant increase in lysosomal components, suggesting that increased autophagic turnover of mitochondria via lysosomes, rather than proteasomal degradation, accounts for the loss of mitochondrial content.[9]

The EMBO study concluded:

> “We present data showing that the molecular phenotype instead is explained by increased autophagic removal of mitochondria, leading to a global decrease in cellular mitochondrial content. Inhibition of lysosomal function in these cells reverses the mitochondrial phenotype, whereas proteasomal inhibition has no effect.”[9]

This indicates that the SCF-FBXL4 complex indirectly controls lysosomal mitophagy pathways by regulating the abundance of BNIP3 and BNIP3L, and that FBXL4 deficiency tips the balance toward excessive lysosomal degradation of mitochondria. Gene Ontology terms relevant to this process include “mitophagy” (GO:0000422), “autophagy of mitochondrion” (GO:0000422), “negative regulation of mitophagy” (GO:1901524), and “SCF-dependent proteasomal ubiquitin-dependent protein catabolic process” (GO:0010498).[8][9][13]

### 6.3 Cellular Processes: Mitochondrial Dynamics, Respiratory Chain, and Energy Failure

At the cellular level, FBXL4 deficiency impacts multiple processes, including mitochondrial dynamics, respiratory chain function, membrane potential, and nucleoid distribution.[6][7][9][14] Bonnen et al. showed that loss-of-function and splice mutations in FBXL4 result in “a severe respiratory chain deficiency, loss of mitochondrial membrane potential, and a disturbance of the dynamic mitochondrial network and nucleoid distribution in fibroblasts from affected individuals.”[6][14] They further demonstrated that expression of wild-type FBXL4 in patient cells fully rescued mtDNA copy number and corrected the mitochondrial biochemical deficit, confirming that FBXL4 plays a critical role in mtDNA maintenance and stability.[6][14]

Gai et al. and Huemer et al. found multiple deficiencies of respiratory chain activities in patient tissues, with severe combined defects across complexes I, II, III, and IV, and associated mtDNA depletion.[7][10] In a neonate with total FBXL4 deficiency, Gai et al. described “profound reductions in complex I-, II- and ETF-linked substrate-dependant respiration, a loss of inner membrane potential, and fragmentation of the mitochondrial network with no parallel decrease in mitochondrial content,” highlighting functional failure even before overt reduction in mitochondrial mass.[7] Later work, including the EMBO study, refined this picture to show that increased mitophagy eventually leads to decreased mitochondrial content, compounding the initial functional defects.[9]

Cellular processes involved include mitochondrial fusion and fission, nucleoid organization, and interactions with autophagosomes and lysosomes. The disturbance of the dynamic mitochondrial network suggests impaired fusion, potentially due to altered expression or function of fusion proteins such as MFN1, MFN2, or OPA1, though FBXL4’s role appears more focused on mitophagy than on direct fusion regulation.[6][7][9][12] Nucleoid distribution anomalies indicate that mtDNA packaging and segregation are affected, likely secondary to altered mitochondrial turnover and network dynamics.[6][14]

Energy failure is a central cellular outcome, as impaired respiratory chain function and decreased mtDNA copy number reduce ATP production and force cells to rely on glycolysis, leading to lactic acid accumulation.[6][7][10][14][17] This is particularly detrimental in high-energy cell types such as neurons (CL:0000540), cardiomyocytes (CL:0000746), skeletal myocytes (CL:0000737), and hepatocytes (CL:0000182), which depend heavily on mitochondrial ATP and thus experience severe dysfunction in FBXL4 deficiency.[7][9][11][13]

### 6.4 Metabolic Changes and Biochemical Abnormalities

Metabolically, FBXL4-related MTDPS13 is characterized by a shift from oxidative phosphorylation to glycolysis, resulting in lactic acidosis and metabolic acidosis.[2][6][7][10][17] Decreased mtDNA copy number reduces the expression of mtDNA-encoded respiratory chain subunits, leading to diminished electron transport chain activity, reduced oxygen consumption, and decreased ATP generation via oxidative phosphorylation.[6][7][9][14] This energy deficit triggers compensatory upregulation of glycolysis, but glycolytic ATP is insufficient to meet cellular demands in high-energy tissues, and the increased pyruvate production is converted to lactate, causing systemic lactic acidosis.[6][7][10][17]

Biochemical abnormalities observed in patient tissues and cells include combined respiratory chain defects, reduced activities of multiple complexes, and decreased enzyme levels associated with mitochondrial energy metabolism.[7][10] Huemer et al. reported “a severe combined respiratory chain defect with a general decrease of enzymes associated with mitochondrial energy metabolism and a relative depletion of mitochondrial DNA content” in diagnostic workup.[10] Elevated blood lactate and metabolic acidosis were universal in their cohort, and creatine kinase was elevated in 45% of measurements, indicating muscle involvement.[10] Gai et al. described “multicomplex respiratory chain dysfunction associated with mtDNA depletion” in a neonate, confirming the broad impact on energy production.[7]

Metabolic changes extend to other pathways, including potential alterations in fatty acid oxidation, amino acid metabolism, and the urea cycle, as suggested by hyperammonemia in approximately half of patients.[2][10][17] However, detailed metabolomics profiles have not been reported for FBXL4-related MTDPS13, and specific intermediates beyond lactate and ammonia have not been systematically analyzed. HMDB and related metabolomics databases are not referenced in the search results, indicating that metabolomics is an area for future investigation.

Biochemical abnormalities relevant to knowledge base annotation include “enzyme deficiencies” of respiratory chain complexes, “loss of mitochondrial membrane potential,” and “mtDNA depletion” as central defects.[6][7][9][10][14] Suggested GO terms include “oxidative phosphorylation” (GO:0006119), “respiratory electron transport chain” (GO:0022904), and “mitochondrial DNA metabolic process” (GO:0032543).[6][7][9]

### 6.5 Immune System and Tissue Damage Mechanisms

Immune system involvement in FBXL4-related MTDPS13 is less well characterized but has been reported in individual cases, suggesting that mitochondrial dysfunction may impair immune cell function or hematopoiesis.[7][10] Gai et al. described “immunodeficiency” in a neonate with total FBXL4 deficiency, with recurrent infections and laboratory evidence of immune compromise.[7] Huemer et al. mentioned immunodeficiency as part of the clinical phenotype in some patients, though not quantified.[10] Tissue damage mechanisms likely include oxidative stress, apoptosis, and necrosis in cells unable to maintain energy homeostasis, but detailed immunologic profiling is lacking.

Tissue injury in brain, heart, and other organs manifests as neuronal loss, cardiomyocyte degeneration, and organ atrophy or fibrosis, inferred from imaging and clinical features.[6][7][9][10][11][12][14] In the brain, progressive cerebral atrophy and cystic white matter lesions suggest neuronal and glial cell death, possibly via apoptotic and necrotic pathways triggered by energy failure and oxidative stress.[6][7][10][14] In the heart, cardiomyopathy likely results from cardiomyocyte loss and remodeling, with potential contributions from mitochondrial ROS and inflammatory responses.[7][9][11] In skeletal muscle, myopathy and elevated creatine kinase reflect muscle fiber damage.

Gene Ontology terms relevant to tissue damage include “apoptotic process” (GO:0006915), “oxidative stress” (GO:0006979), and “necrotic cell death” (GO:0070265), although direct evidence for these specific mechanisms in FBXL4-related MTDPS13 is limited and largely inferred from general mitochondrial disease biology.[7][9][10][11]

### 6.6 Molecular Profiling and Advanced Technologies

Proteomic profiling has played a key role in elucidating FBXL4-related MTDPS13 pathophysiology. EMBO Molecular Medicine’s study used proteomic approaches in FBXL4 knockout mice, patient fibroblasts, and human FBXL4 knockout cells to show “a general decrease in mitochondrial proteins accompanied by an increase in lysosomal proteins,” highlighting the shift in mitochondrial and lysosomal content.[9] This proteomic signature is consistent with increased autophagic removal of mitochondria and compensatory lysosomal expansion.

Transcriptomic profiling and single-cell analyses have not been extensively reported for FBXL4-related MTDPS13 in the available search results, and thus specific gene expression changes, cell-type heterogeneity, and spatial patterns are unknown. Future studies using RNA-seq, single-cell RNA-seq, and spatial transcriptomics could reveal how FBXL4 deficiency impacts transcriptional programs in neurons, cardiomyocytes, and other cell types, but such data are not yet available.[9][13]

CRISPR/Cas9 functional genomics has been used to generate FBXL4 knockout human cell lines that recapitulate patient phenotypes, including reduced mitochondrial protein levels, mtDNA depletion, and increased lysosomal proteins.[9] These in vitro models serve as platforms for high-throughput screens to identify modifiers of mitophagy or mitochondrial content, but published screens specifically targeting FBXL4-deficient cells are not referenced in the search results.[9][13]

Overall, molecular profiling in FBXL4-related MTDPS13 has focused on proteomics and functional genomics, revealing a clear pattern of increased mitophagy and lysosomal turnover of mitochondria, with secondary respiratory chain defects and mtDNA depletion. Integration of multi-omics data remains an opportunity for future research.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

FBXL4-related MTDPS13 affects multiple organs, with primary involvement of the central nervous system, skeletal muscle, heart, and to a lesser extent liver, bone marrow, and immune system.[6][7][9][10][11][12][17] The brain (UBERON:0000955) is the most severely affected organ, with encephalopathy, cerebral atrophy, microcephaly, seizures, and white matter lesions.[6][7][10][11][12][14] Skeletal muscle (UBERON:0001630) exhibits hypotonia, myopathy, and elevated creatine kinase, reflecting mitochondrial dysfunction in muscle fibers.[7][10] The heart (UBERON:0000948) shows cardiomyopathy, congenital malformations, arrhythmias, and pulmonary hypertension in a substantial subset of patients.[7][10][11] The liver (UBERON:0002107) may contribute to hyperammonemia and metabolic disturbances, although specific hepatopathy is not consistently reported.[2][10][17]

Bone marrow (UBERON:0002371) and immune system organs such as spleen (UBERON:0002106) and lymph nodes (UBERON:0001968) may be involved in cases with immunodeficiency and hematologic abnormalities.[7][10] The lungs (UBERON:0002048) are indirectly affected via pulmonary hypertension and potential respiratory failure.[11] The eyes (UBERON:0000970) can show congenital cataracts and other anomalies, while craniofacial bones and soft tissues (UBERON:0002385) manifest dysmorphic features.[7][10][11][12]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, FBXL4-related MTDPS13 primarily affects nervous tissue (UBERON:0001016), skeletal muscle tissue (UBERON:0001134), cardiac muscle tissue (UBERON:0001133), and in some cases hematopoietic tissue (UBERON:0002385).[6][7][9][10][11][12] Within the nervous system, neurons (CL:0000540) and glial cells such as oligodendrocytes (CL:0000128) and astrocytes (CL:0000127) are likely involved, as evidenced by cerebral atrophy and white matter changes.[6][7][10][14] Cardiac involvement implicates cardiomyocytes (CL:0000746), conduction system cells, and vascular smooth muscle cells (CL:0000743).[7][9][11] Skeletal myocytes (CL:0000737) are affected in myopathy and hypotonia.[7][10]

Hematopoietic involvement may affect hematopoietic stem cells (CL:0000037) and related lineages, contributing to bone marrow failure or immunodeficiency.[7][10] Immune cell types such as T lymphocytes (CL:0000084) and B lymphocytes (CL:0000236) may be compromised, though specific cell-type data are sparse.[7][10]

### 7.3 Subcellular Compartments

FBXL4-related MTDPS13 is fundamentally a mitochondrial disease, and subcellular involvement centers on mitochondria (GO:0005739), the mitochondrial outer membrane (GO:0005741), mitochondrial inner membrane (GO:0005743), mitochondrial matrix (GO:0005759), and lysosomes (GO:0005764).[6][7][8][9][13][14] FBXL4 localizes to the mitochondrial outer membrane, where it participates in SCF-type ubiquitin ligase activity targeting BNIP3 and BNIP3L.[9][13] Mitochondrial nucleoid structures are disrupted, as evidenced by altered nucleoid distribution in patient fibroblasts.[6][14] Mitochondrial membrane potential is reduced, and the dynamic mitochondrial network is fragmented.[6][7][14]

Lysosomes are upregulated and expanded in FBXL4-deficient cells, reflecting increased lysosomal turnover of mitochondria via mitophagy.[9] Autophagosomes (GO:0005776) and autolysosomes participate in the removal of damaged mitochondria. Proteasomes (GO:0000502) are involved in the degradation of ubiquitinated BNIP3/BNIP3L under normal conditions, but in FBXL4 deficiency, lysosomal pathways dominate mitochondrial turnover.[9][13]

### 7.4 Localization and Lateralization

Anatomical localization of brain lesions in FBXL4-related MTDPS13 is typically diffuse and bilateral, reflecting global cerebral atrophy and widespread white matter abnormalities rather than focal unilateral lesions.[6][7][10][14] MRI studies report generalized cortical thinning, ventricular enlargement, and diffuse white matter changes, without consistent lateralization.[6][10][14] Cardiac involvement affects the whole heart, including ventricles and conduction system, rather than specific localized segments.[7][10][11]

Pulmonary hypertension involves the pulmonary vasculature bilaterally, and skeletal muscle involvement is generalized across limb and axial muscles.[7][10][11] Craniofacial dysmorphism impacts midface, jaw, and cranial vault symmetrically in most reported cases.[10][12] As such, lateralization does not play a major role in FBXL4-related MTDPS13, and anatomical localization is best described as systemic and bilateral.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

FBXL4-related MTDPS13 is a congenital or early infantile-onset disease, with symptoms typically manifesting at birth or within the first few months of life.[2][10][11][17] MedlinePlus notes that the condition “begins in infancy and affects multiple body systems,” and that infants have hypotonia and growth difficulties early on.[17] Huemer et al. described “neonatal/early-onset severe lactic acidosis, muscular hypotonia, feeding problems and failure to thrive” as the characteristic pattern at first presentation, indicating onset in the neonatal period or early infancy.[10] GeneReviews agrees that onset is usually in the first few months of life, occasionally later in infancy or early childhood, but not in adolescence or adulthood.[11][12]

The onset pattern is acute to subacute, with rapid emergence of lactic acidosis and encephalopathy in the neonatal period, followed by chronic progression of developmental delays and organ involvement.[10][11][12] In some cases, lactic acidosis is detected immediately after birth, while in others it develops over days to weeks as feeding and growth difficulties become apparent.[10][11] For modeling purposes, FBXL4-related MTDPS13 can be categorized as a pediatric, early-onset mitochondrial disease.

### 8.2 Disease Progression, Rate, and Course

Disease progression in FBXL4-related MTDPS13 is generally rapid and progressive, with severe deterioration over months to years, leading to early childhood death in many cases.[6][7][10][11][12][14] Huemer et al. reported that seven children died at a mean age of 37 months, while eleven were alive at a mean follow-up age of 46 months, with three lost to follow-up; all survivors had severe psychomotor retardation.[10] Bonnen et al. described affected children with progressive encephalopathy and lactic acidosis who died in early childhood, often by age 3–4 years.[6][14]

Brain imaging demonstrates a progression from nonspecific findings in neonates to rapidly progressive brain atrophy, indicating ongoing neurodegeneration.[10][14] Cardiac involvement may develop later in infancy or childhood, adding to the risk of heart failure and death.[7][10][11] Metabolic derangements such as lactic acidosis and hyperammonemia can fluctuate with intercurrent illnesses but generally persist as chronic features.[2][10][17]

Disease stages can be conceptualized as early neonatal presentation with lactic acidosis and hypotonia, intermediate childhood with progressive developmental delay and emerging organ involvement, and advanced stage with severe encephalopathy, organ failure, and high mortality risk.[10][11][12] The course is largely progressive and does not exhibit remission or relapsing–remitting patterns; any transient improvements reflect supportive therapy rather than disease reversal.[10][11]

### 8.3 Critical Periods and Windows of Intervention

The neonatal and early infancy period constitutes a critical window of vulnerability in FBXL4-related MTDPS13, as metabolic crises and encephalopathy early in life can irreversibly damage developing brain and other organs.[10][11][12] Early recognition and supportive management—such as aggressive treatment of lactic acidosis, provision of adequate nutrition, and avoidance of mitochondrial-toxic drugs—may mitigate immediate complications but do not fundamentally alter the disease trajectory.[10][11]

In experimental models, the perinatal period is also critical. EMBO Molecular Medicine’s Fbxl4 knockout mice exhibited predominant perinatal lethality, with only a few animals surviving into adulthood; surviving mice appeared normal until 8–12 months of age, when they gradually developed signs of mitochondrial dysfunction and weight loss.[9] This suggests that developmental timing of mitochondrial quality control is crucial in both humans and mice, and that early FBXL4 deficiency imposes a high risk of perinatal organ failure.

Given the autosomal recessive inheritance, preconception and prenatal windows offer opportunities for genetic prevention via carrier screening and prenatal diagnosis, as discussed in GeneReviews.[11][12] These interventions can prevent the birth of affected children but do not alter disease progression in already-affected individuals.

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

FBXL4-related MTDPS13 follows an autosomal recessive inheritance pattern, with affected individuals carrying pathogenic variants on both alleles and heterozygous carriers being asymptomatic.[1][2][6][10][11][16] MedGen explicitly lists “autosomal recessive inheritance” for MTDPS13, referencing Orphanet and OMIM.[2][18] Bonnen et al. reported recessive nonsense and splicing mutations segregating in consanguineous kindreds, with carrier parents unaffected, consistent with autosomal recessive transmission.[6][14] ClinVar entries and GeneReviews also classify FBXL4-related MTDPS13 as autosomal recessive.[11][15][16]

Penetrance appears to be complete among individuals with biallelic loss-of-function variants, as all known homozygous or compound heterozygous carriers of clearly pathogenic FBXL4 variants exhibit clinical disease.[6][10][11][16] Variation in expressivity is present, however, particularly in the severity and spectrum of organ involvement; some patients have prominent cardiac phenotypes, craniofacial anomalies, or immunodeficiency, while others exhibit primarily neurologic and metabolic features.[7][10][11][12] Huemer et al. reported no clear genotype–phenotype correlation, suggesting that expressivity is influenced by factors beyond the specific FBXL4 variant, such as genetic background or environmental exposures.[10]

There is no evidence of genetic anticipation, as the disease does not involve repeat expansions or progressive worsening across generations; instead, disease severity appears similar among affected siblings, conditioned on their shared genotype and environment.[10][11] Germline mosaicism has not been reported in FBXL4-related MTDPS13, but it cannot be entirely excluded; however, the autosomal recessive model predominates, and recurrence risk in families is best estimated based on carrier status rather than mosaicism probabilities.[11][12]

### 9.2 Epidemiology: Prevalence and Incidence

FBXL4-related MTDPS13 is an extremely rare disorder, with only a few dozen cases reported worldwide in the literature and curated resources.[2][3][10][11][12] MedGen notes that “To date FBXL4-related mtDNA depletion syndrome has been reported in 50 individuals,” summarizing case counts up to approximately 2017.[2] Huemer et al. stated that “to date, the genetic diagnosis of FBXL4 deficiency has been established in 28 individuals,” reflecting the status at the time of their 2015 publication.[10] GeneReviews likely updates these numbers as new cases are reported but still characterizes the disease as very rare.[11][12]

Given these counts and the global population, the prevalence of FBXL4-related MTDPS13 is likely less than 1 per million, possibly closer to 1 per several million, placing it in the Orphanet category of “rare diseases” and supporting its inclusion in orphan disease registries.[3][11] Incidence data are unavailable due to the rarity and lack of population-based screening, but given autosomal recessive inheritance and low carrier frequencies, incident cases are expected to be sporadic and often arise in consanguineous families or small founder populations.[6][10][11]

### 9.3 Population Demographics, Consanguinity, and Founder Effects

A notable proportion of reported FBXL4-related MTDPS13 cases arise from consanguineous families, particularly in regions where consanguineous marriages are culturally prevalent.[6][10][11][12][16] Bonnen et al. identified affected children in three unrelated consanguineous kindreds, emphasizing that recessive nonsense and splice mutations segregated with disease.[6][14] Huemer et al. mentioned consanguinity in many of their cases, and GeneReviews notes that the disease is more likely to occur in families with consanguineous unions.[10][11][12]

Founder effects have been suggested but not conclusively proven for specific variants. The p.Cys411Tyr missense variant has been reported in multiple unrelated patients, including a compound heterozygous combination with Arg435Gln and a homozygous case, suggesting possible enrichment in certain populations.[16] A Norwegian child with encephalomyopathic MTDPS13 was reported to carry a novel FBXL4 mutation, hinting at geographic clustering of certain alleles.[8] However, detailed population genetics analyses are lacking.

Population demographics such as sex ratio and age distribution are consistent with the autosomal recessive pediatric presentation: affected individuals include both males and females in roughly equal numbers, and all cases present in infancy or early childhood.[6][10][11][12][14] No sex-specific differences in phenotype or outcome have been documented. Geographic distribution of cases appears global, including European, Middle Eastern, and North American families, but precise regional prevalence data are not available.[6][10][11][12]

Carrier frequency estimates are not directly provided in the search results, but given the rarity of disease and the low frequency of known pathogenic variants such as p.Cys411Tyr in population databases, carriers are expected to be rare.[16] GeneReviews suggests carrier testing in at-risk families, but population-level screening is not currently undertaken.[11][12]

## 10. Diagnostics

### 10.1 Clinical and Laboratory Testing

Diagnostic evaluation of suspected FBXL4-related MTDPS13 involves a combination of clinical assessment, laboratory testing, imaging, and genetic analysis.[2][7][10][11][12][17][18] Clinically, the presentation of early-onset encephalopathy, hypotonia, failure to thrive, and persistent lactic acidosis, especially in the context of consanguinity or family history of similar illness, should prompt consideration of mitochondrial DNA depletion syndromes and specifically FBXL4 deficiency.[10][11][17][18] Huemer et al. concluded that “a clinical pattern of early-onset encephalopathy, persistent lactic acidosis, profound muscular hypotonia and typical facial dysmorphism should prompt initiation of molecular genetic analysis of FBXL4.”[10]

Laboratory tests focus on metabolic and mitochondrial parameters. Elevated blood lactate and metabolic acidosis are universal in reported cases, and hyperammonemia is present in about half of individuals.[2][10][17] Creatine kinase is elevated in roughly 45% of measurements, indicating muscle involvement.[10] Additional tests may include plasma amino acids, acylcarnitine profiles, pyruvate levels, and liver function tests, which can help exclude other metabolic disorders but are not specific for FBXL4 deficiency.[10][11][12] LOINC codes and SNOMED CT terms corresponding to lactic acid measurement, ammonia levels, and creatine kinase can be associated with these tests.

Muscle or liver biopsy may be performed to assess respiratory chain enzyme activities and mtDNA copy number. Diagnostic workup in patient tissues has revealed “a severe combined respiratory chain defect with a general decrease of enzymes associated with mitochondrial energy metabolism and a relative depletion of mitochondrial DNA content,” as reported by Huemer et al.[10] Biochemical assays demonstrate decreased activities of multiple respiratory chain complexes (I, II, III, IV) and reduced mtDNA content, confirming a mitochondrial maintenance defect.[6][7][10][14]

Histopathologic examination of muscle may show non-specific myopathic changes, with possible ragged-red fibers or fiber atrophy, though these findings are not pathognomonic.[6][10][14] Immunohistochemistry for mitochondrial proteins and mtDNA-encoded subunits can further support the diagnosis. SNOMED CT pathology terms corresponding to “myopathy” and “mitochondrial disease” can be applied.

### 10.2 Imaging and Electrophysiology

Brain imaging, typically MRI, is critical in diagnosing and characterizing FBXL4-related MTDPS13.[6][7][10][11][12][14] In neonates, MRI may be nonspecific, showing mild abnormalities, but later imaging reveals rapidly progressive brain atrophy, cortical thinning, ventricular enlargement, and white matter lesions.[10][14] Bonnen et al. reported generalized cerebral atrophy and microcephaly in affected children, with MRI imaging confirming widespread cortical and subcortical changes.[6][14] Huemer et al. described “non-specific” neonatal imaging but “later-onset, rapidly progressive brain atrophy,” suggesting that serial imaging is important for tracking disease evolution.[10]

Cardiac imaging, such as echocardiography and cardiac MRI, can reveal cardiomyopathy, congenital malformations, and pulmonary hypertension.[7][10][11] Functional cardiac tests, including electrocardiography (ECG) and Holter monitoring, detect arrhythmias and conduction abnormalities.[10][11] LOINC and RadLex terms corresponding to these imaging and electrophysiologic modalities can be attached in the knowledge base.

Electroencephalography (EEG) may demonstrate diffuse slowing, epileptiform discharges, or other nonspecific encephalopathic patterns, although specific EEG findings in FBXL4-related MTDPS13 are not extensively documented in the available search results.[10][11][12] Similarly, electromyography (EMG) and nerve conduction studies may show myopathic patterns, reflecting muscle involvement.

### 10.3 Genetic Testing Strategies

Genetic testing is central to definitive diagnosis of FBXL4-related MTDPS13. Initially, gene discovery relied on whole-exome sequencing in consanguineous families, as described by Bonnen et al.[6][14] In contemporary clinical practice, diagnostic strategies include targeted gene panels focused on mitochondrial diseases and mtDNA maintenance disorders, whole-exome sequencing (WES), whole-genome sequencing (WGS), and single-gene testing for *FBXL4* in high-suspicion cases.[7][10][11][12]

GeneReviews recommends that for individuals suspected of having FBXL4-related encephalomyopathic mtDNA depletion syndrome based on clinical and biochemical findings, molecular genetic testing should begin with a multigene panel that includes *FBXL4* and other genes known to cause mtDNA depletion syndromes (e.g., *POLG*, *TK2*, *DGUOK*, *RRM2B*).[11][12] If panel testing is inconclusive, WES or WGS can be pursued to identify rare variants in *FBXL4* or novel genes.[6][10][11][12] Single-gene testing for *FBXL4*, using Sanger sequencing or targeted NGS, may be appropriate in families with known pathogenic FBXL4 variants, as part of cascade screening or prenatal diagnosis.[11][12][15][16]

The Genetic Testing Registry (GTR) lists multiple tests for “Mitochondrial DNA depletion syndrome 13,” including panels that assay *FBXL4* along with other mitochondrial maintenance genes and single-gene tests for *FBXL4*.[18] ClinVar entries provide variant interpretations that support clinical decision-making based on genotype.[4][5][15][16]

Chromosomal microarray (CMA), karyotyping, and FISH are generally not diagnostic for FBXL4-related MTDPS13, as the disease arises from sequence-level mutations rather than large-scale structural variants.[1][2][10][11] Mitochondrial DNA sequencing is useful for excluding primary mtDNA mutations but is not sufficient for diagnosing FBXL4-related MTDPS13, which involves nuclear gene defects and secondary mtDNA depletion.[6][7][10][11][14]

### 10.4 Omics-Based Diagnostics and Molecular Biomarkers

While exome and genome sequencing represent genomic omics approaches used to diagnose FBXL4-related MTDPS13, other omics-based diagnostics such as transcriptomics, proteomics, and metabolomics are not yet standard in clinical practice for this disease.[9][11][13] Proteomic analyses have provided mechanistic insight, as described above, but are not used diagnostically.[9] Metabolomics profiling could, in principle, identify specific signatures of mitochondrial dysfunction, but no published studies have defined such signatures for FBXL4 deficiency in clinical cohorts.

Potential molecular biomarkers include reduced mtDNA copy number in muscle or fibroblasts, combined respiratory chain enzyme deficiencies, and elevated BNIP3/BNIP3L levels in patient cells.[6][7][9][10][13][14] However, BNIP3 and BNIP3L measurement has not been translated into clinical diagnostic tests. FDA biomarker databases and related resources do not currently list specific biomarkers for FBXL4-related MTDPS13.

### 10.5 Clinical Diagnostic Criteria and Differential Diagnosis

Formal standardized diagnostic criteria for FBXL4-related MTDPS13, akin to DSM or ICD guidelines, have not been published, but clinical experts and GeneReviews provide practical criteria based on core features.[10][11][12] Huemer et al. emphasized that early-onset encephalopathy, persistent lactic acidosis, profound muscular hypotonia, facial dysmorphism, and combined respiratory chain defects with mtDNA depletion should prompt molecular testing of FBXL4.[10] GeneReviews similarly lists key findings including failure to thrive, neurodevelopmental delays, encephalopathy, cerebral atrophy, hypotonia, and persistent lactic acidosis as the clinical hallmarks, combined with genetic confirmation of biallelic FBXL4 variants.[11][12]

Differential diagnosis includes other mtDNA depletion syndromes caused by defects in nuclear genes such as *POLG* (MTDPS1), *C10orf2/Twinkle* (MTDPS7), *TK2* (MTDPS2), *DGUOK* (MTDPS3), and *RRM2B* (MTDPS8), among others.[2][6][10][11][12] Clinically, these conditions may present with overlapping features of encephalopathy, lactic acidosis, hypotonia, and developmental delay, but they may have distinct organ involvement patterns, such as predominant hepatic failure in *DGUOK* deficiency or myopathic presentations in *TK2* deficiency.[11][12] Genetic testing panels that include FBXL4 and these genes can help distinguish among them. Other conditions to consider include primary mtDNA point mutations, inherited metabolic disorders, urea cycle defects, and non-metabolic causes of encephalopathy and lactic acidosis.

### 10.6 Screening

Population-based screening for FBXL4-related MTDPS13, such as newborn screening, is not currently implemented, given the rarity of the disease and limited treatment options.[11][12][17] However, carrier screening and prenatal diagnosis are recommended in families with known FBXL4 pathogenic variants. GeneReviews advises that carrier testing for at-risk relatives and prenatal testing for pregnancies at increased risk should be offered once the familial FBXL4 variants are identified.[11][12] Preimplantation genetic diagnosis (PGD) may be considered in couples at high risk, allowing selection of embryos without biallelic FBXL4 mutations.[11]

Cascade screening of siblings and extended family members can identify carriers and early affected individuals, though the disease’s early onset means that most affected children will already be symptomatic by the time genetic diagnosis is made in an index case.[11][12] Risk stratification based on genotype can inform reproductive decisions, but does not yet influence treatment strategies for existing patients.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

FBXL4-related MTDPS13 carries a poor prognosis, with high mortality in infancy and early childhood and limited survival into later childhood.[6][7][10][11][12][14] Huemer et al. reported that seven of 21 children died at a mean age of 37 months, while eleven were alive at a mean follow-up age of 46 months.[10] Bonnen et al. described affected children who died between ages 1.5 and 4 years, often from complications of encephalopathy, lactic acidosis, or cardiac disease.[6][14] GeneReviews notes that most individuals with FBXL4-related MTDPS13 die in early childhood, though a few survive longer with severe disability.[11][12]

Life expectancy is therefore significantly reduced compared to the general population. While precise 5-year or 10-year survival rates are not available due to small sample sizes, a rough estimate from existing data would suggest that fewer than half of affected individuals survive beyond age 5, and even fewer beyond age 10.[10][11][12] Mortality is directly attributable to the disease in most cases, due to neurological deterioration, metabolic crises, cardiac failure, or multi-organ dysfunction.[6][7][10][11][12][14]

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in FBXL4-related MTDPS13 is severe and pervasive. Survivors have profound psychomotor retardation, significant hypotonia, feeding difficulties, and often multiple organ system involvement, resulting in major disability and near-total dependence on caregivers.[10][11][12] Huemer et al. reported that “all survivors developed severe psychomotor retardation,” and described persistent lactic acidosis, failure to thrive, and ongoing neurologic and cardiac issues.[10] GeneReviews emphasizes that developmental outcome is poor, with most survivors unable to walk or speak, and many requiring gastrostomy feeding and assistive devices.[11][12]

Quality of life is compromised across domains of mobility, self-care, pain, and emotional well-being. Children may experience recurrent hospitalizations, distress from seizures and metabolic crises, and limited ability to engage in social and educational activities.[10][11][12] Family quality of life is also heavily impacted, as caregivers face emotional, financial, and physical burdens in managing complex medical needs over years.

Standardized quality of life measures such as EQ-5D or SF-36 have not been systematically applied to FBXL4-related MTDPS13, but extrapolation from similar severe pediatric mitochondrial disorders suggests extremely low scores in physical functioning, role limitations, and general health domains.[10][11]

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course is progressive and characterized by accumulating complications over time. Neurological deterioration leads to cerebral atrophy, seizures, and loss of milestones, while cardiac involvement adds risk of heart failure and arrhythmias.[6][7][9][10][11][14] Metabolic crises, including severe lactic acidosis and hyperammonemia, can cause acute encephalopathy and organ failure, often leading to death.[2][10][17] Additional complications may include infections due to immunodeficiency, bone marrow failure, and pulmonary hypertension.[7][10][11]

Recovery potential is limited. Supportive care can stabilize acute crises and improve nutritional status, but does not reverse underlying mitochondrial dysfunction or restore neurodevelopmental capacity.[10][11][12] No disease-modifying therapies have been proven effective, and “mitochondrial medications” such as coenzyme Q10 and vitamins have not altered long-term outcomes.[7][10][11] Huemer et al. concluded that “Treatment with ‘mitochondrial medications’ did not prove effective,” underscoring the lack of recovery-oriented interventions.[10]

### 11.4 Prognostic Factors and Biomarkers

Prognostic factors in FBXL4-related MTDPS13 include age at onset, severity of lactic acidosis, presence of cardiac involvement, and degree of neurodevelopmental impairment.[6][7][10][11][12][14] Early, severe lactic acidosis and encephalopathy may predict worse outcomes, as they reflect profound mitochondrial failure and structural brain damage.[10][11] Cardiac phenotypes such as cardiomyopathy and arrhythmias are associated with increased mortality risk, given the potential for sudden cardiac death or progressive heart failure.[7][10][11]

Genotype–phenotype correlation is limited, and specific prognostic biomarkers such as mtDNA copy number thresholds or BNIP3/BNIP3L expression levels have not been validated in clinical practice.[7][9][10][13][14] Nevertheless, combined respiratory chain enzyme activities and mtDNA depletion degree could be considered surrogate markers of severity, as more pronounced biochemical defects likely correlate with more severe clinical disease.[7][10][14]

In summary, prognosis in FBXL4-related MTDPS13 is generally poor, with limited survival and substantial disability, and available prognostic factors are largely clinical rather than molecular.

## 12. Treatment

### 12.1 Pharmacotherapy and Supportive Medical Management

Currently, there are no disease-specific pharmacologic treatments that correct the underlying mitochondrial maintenance defect in FBXL4-related MTDPS13, and management is predominantly supportive.[7][10][11][12] Standard “mitochondrial medications,” including coenzyme Q10, riboflavin, L-carnitine, and various vitamins and antioxidants, have been empirically used in many mitochondrial diseases, but Huemer et al. reported that in their cohort, “treatment with ‘mitochondrial medications’ did not prove effective,” indicating that these supplements do not significantly alter disease course in FBXL4 deficiency.[10] GeneReviews echoes that no proven pharmacologic therapy exists to modify disease progression.[11][12]

Supportive pharmacotherapy focuses on symptom management and prevention of complications. For lactic acidosis, intravenous bicarbonate and careful fluid management can mitigate acute metabolic acidosis.[10][11][12] For seizures, antiepileptic drugs are used, with caution to avoid mitochondrial-toxic agents such as valproic acid.[10][11] Cardiac medications, including ACE inhibitors, beta-blockers, or diuretics, may be indicated for cardiomyopathy and heart failure.[7][10][11] Antibiotics and immunoglobulin therapy may be used for infections and immunodeficiency, though these are not specific to FBXL4 deficiency.[7][10]

NCIT (NCI Thesaurus) clinical intervention terms relevant to pharmacotherapy include “Mitochondrial disease supportive therapy,” “Antiepileptic therapy,” “Cardiomyopathy management,” and “Metabolic acidosis therapy.” These can be linked to specific drug classes in the knowledge base.

### 12.2 Advanced Therapeutics and Experimental Approaches

Advanced therapeutics such as gene therapy, cell therapy, and RNA-based interventions have not yet been applied clinically to FBXL4-related MTDPS13, but mechanistic insights suggest potential strategies.[9][11][13] Given that FBXL4 deficiency leads to excessive mitophagy via BNIP3/BNIP3L accumulation and lysosomal degradation of mitochondria, interventions aimed at suppressing mitophagy or modulating lysosomal activity could theoretically restore mitochondrial content and improve function.[9][13]

EMBO Molecular Medicine showed that inhibition of lysosomal function in FBXL4-deficient cells reverses the mitochondrial phenotype, whereas proteasomal inhibition does not, indicating that lysosomal pathways are key targets.[9] Kulkarni et al. suggested that “interventions to stop the increased mitochondrial turnover should be considered as a potential treatment for this disease,” pointing toward pharmacologic or genetic modulation of mitophagy receptors or lysosomal pathways.[9][13] For example, small molecules or RNA-based therapies that reduce BNIP3/BNIP3L expression or block their function could restore mitochondrial abundance.

Gene therapy, involving delivery of functional *FBXL4* via viral vectors, could, in principle, correct the defect at its source. The success of FBXL4 transfection in rescuing cardiac geometry and mitochondrial integrity in a mouse model of heart failure with preserved ejection fraction suggests that FBXL4 replacement can restore mitochondrial dynamics in adult tissues.[11] However, translating this to a pediatric mitochondrial disease poses challenges, including delivery to multiple organs and the need to intervene early in life.

Cell therapy, such as transplantation of healthy hematopoietic stem cells, is unlikely to address the global mitochondrial defect affecting neurons and cardiomyocytes. RNA-based therapies, such as antisense oligonucleotides (ASOs) or siRNA targeting BNIP3/BNIP3L, may be more feasible but remain hypothetical.[9][13]

ClinicalTrials.gov and related registries do not list active clinical trials specifically for FBXL4-related MTDPS13 in the available search results, indicating that advanced therapeutics are still at the preclinical stage.

### 12.3 Surgical and Interventional Care

Surgical interventions in FBXL4-related MTDPS13 are primarily supportive and focused on managing complications. Gastrostomy tube placement for enteral feeding may be necessary in children with severe feeding difficulties and aspiration risk.[10][11][12] Cardiac device implantation, such as pacemakers or defibrillators, could be considered in cases with life-threatening arrhythmias, though evidence is anecdotal.[7][10][11] Surgical correction of congenital heart malformations may be attempted, but surgical risk is higher due to metabolic vulnerability and anesthesia concerns.[10][11]

NCIT terms relevant to surgical interventions include “Gastrostomy tube placement,” “Cardiac pacemaker insertion,” and “Congenital heart defect repair.”

### 12.4 Rehabilitation and Supportive Care

Rehabilitation and supportive care are essential components of treatment, aiming to optimize function and quality of life despite irreversible neurologic and metabolic deficits.[10][11][12] Physical therapy can help maintain joint mobility, prevent contractures, and support motor function within the constraints imposed by hypotonia and weakness.[10][11] Occupational therapy can assist with activities of daily living, adaptive equipment, and environmental modifications.[10][11] Speech therapy may address feeding and communication issues, although many children have limited speech due to severe developmental delay.[10][11][12]

Nutritional support, including specialized diets and enteral feeding, is critical to maintain adequate caloric intake and prevent further failure to thrive.[10][11][12] Palliative care services may be involved to support families and manage symptoms such as pain, dyspnea, and distress. NCIT terms relevant to supportive and rehabilitative care include “Physical therapy,” “Occupational therapy,” “Speech therapy,” “Nutritional support therapy,” and “Palliative care.”

### 12.5 Treatment Outcomes and Personalized Medicine

Treatment response in FBXL4-related MTDPS13 is limited. Supportive therapy can reduce acute complications and stabilize metabolic status but does not reverse neurodevelopmental impairment or cure the disease.[10][11][12] No pharmacologic agent has demonstrated clear efficacy in controlled studies, and the use of “mitochondrial medications” has not improved long-term outcomes.[7][10][11]

Personalized medicine approaches currently focus on genetic counseling and reproductive planning, rather than individualized treatment based on genotype, as no genotype-specific therapies exist.[11][12][16] However, understanding the precise FBXL4 variant may influence prognosis and decisions about intensity of care, particularly when variants are predicted to retain partial function versus complete loss-of-function.

Future personalized therapies could involve targeting specific pathways affected by FBXL4 deficiency, such as BNIP3/BNIP3L-mediated mitophagy, but these remain under investigation.[9][13]

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of FBXL4-related MTDPS13 focuses on avoiding the birth of affected children through genetic counseling, carrier testing, and reproductive options such as prenatal diagnosis and preimplantation genetic diagnosis.[11][12] GeneReviews recommends that once the familial FBXL4 pathogenic variants are known, carrier testing for at-risk relatives and prenatal testing for pregnancies at risk should be offered.[11][12] Couples with a history of FBXL4-related MTDPS13 can use PGD to select embryos without biallelic FBXL4 mutations, thereby preventing disease in offspring.[11][12]

Secondary prevention—early detection and treatment of disease to reduce severity—is limited by the disease’s congenital nature and lack of disease-modifying therapies. However, early diagnosis via genetic testing can prevent unnecessary diagnostic procedures and facilitate early supportive care, which may mitigate complications and improve quality of life.[10][11][12] Huemer et al. noted that establishing the diagnosis “permits genetic counselling, prevents patients undergoing unhelpful diagnostic procedures and allows for accurate prognosis,” highlighting the secondary preventive value of timely diagnosis.[10]

Tertiary prevention aims to prevent complications and reduce disability in individuals with established disease. This includes aggressive management of lactic acidosis, cardiac monitoring, infection control, nutritional support, and rehabilitation.[10][11][12] These measures do not prevent disease occurrence but can reduce the impact of complications and improve functional outcomes within the limits set by the underlying mitochondrial defect.

### 13.2 Immunization, Screening, and Counseling

Immunization strategies for FBXL4-related MTDPS13 follow standard pediatric vaccine schedules, with attention to preventing infections that could trigger metabolic crises.[10][11][12] There is no disease-specific vaccine. Newborn screening programs do not currently include FBXL4-related MTDPS13, given its rarity and the absence of effective treatments.[11][12][17]

Genetic screening plays a central role in prevention. Carrier screening in populations with high consanguinity or known FBXL4 mutations can identify couples at risk of having affected children.[6][10][11][12] Risk stratification based on carrier status informs decisions about prenatal testing and PGD. Counseling by genetics professionals, guided by NSGC and ACMG guidelines, is essential to help families understand inheritance patterns, recurrence risks, and available reproductive options.[11][12][16]

Behavioral interventions such as lifestyle modifications have limited direct impact on disease risk, as FBXL4-related MTDPS13 is primarily genetic and early-onset. However, counseling can address family planning, psychological support, and management of caregiver stress.

Public health interventions are not specific to FBXL4 deficiency, but general awareness of rare genetic diseases can support resource allocation and research funding.

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologs

Orthologous genes to human *FBXL4* exist in other species, including mouse (*Fbxl4*) and other vertebrates, reflecting evolutionary conservation of the F-box/LRR protein family and mitochondrial quality control mechanisms.[8][9] NCBI Gene lists *FBXL4* in Homo sapiens, and related articles discuss *Fbxl4* knockout mice used for mechanistic studies.[8][9] The Alliance of Genome Resources and HomoloGene likely map FBXL4 orthologs in mouse, zebrafish, and other model organisms, though specific identifiers are not provided in the search results.

### 14.2 Natural Disease in Animals and Comparative Pathology

No naturally occurring FBXL4-related mitochondrial DNA depletion syndromes have been reported in companion animals or livestock in the available literature, and OMIA does not list such a disease in the search results.[9] Veterinary relevance of FBXL4 deficiency remains primarily theoretical, based on the presence of orthologous genes and the importance of mitochondrial quality control in animal health.

Comparative pathology focuses on similarities between human FBXL4-related MTDPS13 and phenotypes observed in *Fbxl4* knockout mice. EMBO Molecular Medicine’s mouse model demonstrates perinatal lethality, delayed onset mitochondrial dysfunction in survivors, mtDNA depletion, and global reduction in mitochondrial proteins, paralleling human disease features.[9] Weight loss and signs of mitochondrial disease in adult mice resemble chronic energy failure in humans, although neurologic and behavioral phenotypes in mice are less detailed.[9]

Evolutionary conservation of the SCF-FBXL4–BNIP3/BNIP3L pathway suggests that mitochondrial quality control via mitophagy suppression is a conserved mechanism across mammals, and its disruption can cause mitochondrial disease in multiple species.[9][13]

### 14.3 Transmission and Zoonotic Potential

FBXL4-related MTDPS13 is a non-infectious, hereditary disease and has no zoonotic potential. It is not transmissible between individuals via pathogens and does not involve cross-species susceptibility beyond shared genetic mechanisms. Transmission occurs vertically via autosomal recessive inheritance within human families.[6][10][11][12]

## 15. Model Organisms

### 15.1 Fbxl4 Knockout Mouse Model

The most informative model organism for FBXL4-related MTDPS13 is the *Fbxl4* knockout mouse described in the EMBO Molecular Medicine study.[9] Researchers generated homozygous *Fbxl4* knockout mice and found that they displayed predominant perinatal lethality, with only a few animals surviving into adulthood.[9] Surprisingly, the surviving animals were apparently normal until the age of 8–12 months, when they gradually developed signs of mitochondrial dysfunction and weight loss.[9] One-year-old *Fbxl4* knockouts showed a global reduction in mitochondrial proteins and mtDNA depletion, whereas lysosomal proteins were upregulated.[9]

The EMBO study reports:

> “We generated homozygous Fbxl4 knockout mice and found that they display a predominant perinatal lethality. Surprisingly, the few surviving animals are apparently normal until the age of 8–12 months when they gradually develop signs of mitochondrial dysfunction and weight loss. One-year-old Fbxl4 knockouts show a global reduction in a variety of mitochondrial proteins and mtDNA depletion, whereas lysosomal proteins are upregulated.”[9]

Fibroblasts from patients with FBXL4 deficiency and human FBXL4 knockout cells also showed reduced steady-state levels of mitochondrial proteins, attributed to increased mitochondrial turnover.[9] Inhibition of lysosomal function reversed the mitochondrial phenotype, while proteasomal inhibition had no effect, confirming that lysosomal mitophagy drives mitochondrial loss in FBXL4 deficiency.[9]

This mouse model recapitulates key features of human disease at the molecular level, including mtDNA depletion, decreased mitochondrial proteins, and upregulated lysosomal proteins, and demonstrates that FBXL4 plays a critical role in mitochondrial quality control.[9] However, the timing and severity of phenotypes differ: mice exhibit perinatal lethality and late-onset mitochondrial dysfunction in survivors, whereas humans typically show early infantile onset.[9][10][11] Neurologic and cardiac phenotypes in the mouse model are less well characterized, and behavioral outcomes are not extensively described.[9]

### 15.2 Human Cell Line Models and Patient Fibroblasts

Human cell-based models have been crucial for mechanistic studies. CRISPR/Cas9 knockout human cell lines lacking FBXL4 replicate patient fibroblast phenotypes, including reduced mitochondrial proteins, mtDNA depletion, increased lysosomal proteins, and heightened mitophagy.[9][13] Patient-derived fibroblasts from individuals with FBXL4 deficiency exhibit severe respiratory chain deficiency, loss of mitochondrial membrane potential, fragmentation of the mitochondrial network, enlarged nucleoids, and disturbed mtDNA distribution.[6][7][14]

These cellular models allow precise experimental manipulation and high-throughput screening of mitophagy modifiers, making them valuable tools for preclinical therapeutic development.[9][13] They also enable detailed study of SCF-FBXL4–BNIP3/BNIP3L interactions, autophagic flux, and mitochondrial dynamics under controlled conditions.[9][13]

### 15.3 Model Limitations and Applications

Model organisms and cell lines for FBXL4-related MTDPS13 capture many molecular and cellular features of the human disease, such as mtDNA depletion, respiratory chain defects, increased mitophagy, and altered mitochondrial–lysosomal balance.[6][7][9][13][14] However, they have limitations in reproducing the full spectrum of clinical phenotypes, including severe early-onset encephalopathy, craniofacial dysmorphism, and multi-organ involvement seen in human patients.[9][10][11][12]

The mouse model’s late-onset mitochondrial dysfunction contrasts with human early-onset disease, suggesting species differences in developmental timing and mitochondrial resilience.[9][10][11] Behavioral and cognitive phenotypes in mice are not well described, and the model may not fully replicate human neurodevelopmental outcomes. Cell line models lack tissue context and cannot capture organ-level interactions or systemic metabolic responses.[9][13]

Despite these limitations, model organisms and cell lines are highly valuable for studying the molecular pathophysiology of FBXL4 deficiency, testing interventions that modulate mitophagy or lysosomal function, and exploring the role of FBXL4 in other mitochondrial diseases. Applications include screening small molecules that inhibit BNIP3/BNIP3L, assessing gene therapy vectors for FBXL4 delivery, and investigating interactions between FBXL4 and other mitochondrial maintenance genes.[9][13]

## Conclusion

FBXL4-related mitochondrial DNA depletion syndrome (MTDPS13) is a paradigmatic example of a severe, early-onset, nuclear-encoded mitochondrial maintenance disorder that integrates genetic, molecular, cellular, and clinical complexities into a coherent disease entity. Biallelic loss-of-function variants in *FBXL4*, a mitochondrial outer-membrane F-box and leucine-rich repeat protein, disrupt the SCF-FBXL4 E3 ubiquitin ligase’s ability to ubiquitinate and degrade BNIP3 and BNIP3L/NIX mitophagy receptors, leading to excessive mitophagy, lysosomal removal of mitochondria, and global reduction in mitochondrial content and mtDNA copy number.[6][8][9][13][14] The resulting combined respiratory chain defects and energy failure manifest clinically as neonatal or early-infantile encephalopathy, persistent lactic acidosis, hypotonia, failure to thrive, severe developmental delay, and multi-organ involvement, including cardiac disease, craniofacial dysmorphism, and occasional immunodeficiency.[2][6][7][9][10][11][12][14][17]

Curated resources such as OMIM, Orphanet, MedGen, GeneReviews, and MedlinePlus provide consistent disease definitions and identifiers, including OMIM 615471, ORPHA:369897, MedGen C3809592, and MONDO:0014198, and emphasize the autosomal recessive inheritance, high mortality, and severe disability associated with FBXL4-related MTDPS13.[1][2][3][10][11][12][17][18] Clinical series, notably Huemer et al.’s 21-patient cohort, quantify phenotype frequencies and outcomes, showing near-universal lactic acidosis and hypotonia, frequent facial dysmorphism, and cardiac involvement in over half of cases, with mean death around 3 years in those who succumb and severe psychomotor retardation in survivors.[10][11] Mechanistic studies, including Bonnen et al.’s gene discovery work and EMBO Molecular Medicine’s mouse and cell line models, elucidate the central role of FBXL4 in mitochondrial quality control and mtDNA maintenance, while the Autophagy commentary clarifies FBXL4’s specific function in suppressing mitophagy via BNIP3/BNIP3L turnover.[6][9][13][14]

From a diagnostic perspective, FBXL4-related MTDPS13 should be suspected in infants with early-onset encephalopathy, lactic acidosis, hypotonia, failure to thrive, and combined respiratory chain defects with mtDNA depletion, particularly in consanguineous families.[2][6][7][10][11][14][17] Molecular genetic testing via multigene panels, WES, or WGS is essential for definitive diagnosis, and ClinVar provides detailed variant interpretations for numerous pathogenic and likely pathogenic FBXL4 alleles.[4][5][15][16] Treatment remains largely supportive, with no proven disease-modifying pharmacotherapy, and “mitochondrial medications” have not shown efficacy.[7][10][11] Management focuses on metabolic stabilization, cardiac care, nutritional support, rehabilitation, and palliative care, while genetic counseling and reproductive planning offer avenues for primary prevention.[10][11][12][17]

Future directions in FBXL4-related MTDPS13 research and care include further elucidation of modifier genes and gene–environment interactions, development of targeted therapies that modulate mitophagy or lysosomal function, exploration of gene therapy to restore FBXL4 activity, and integration of multi-omics profiling to refine disease mechanisms and biomarkers.[9][11][13] Improved model organisms and cell-based systems will facilitate these efforts, but translation to clinical benefit will require careful consideration of timing, organ targeting, and safety in a vulnerable pediatric population. Until such advances materialize, FBXL4-related MTDPS13 remains a devastating mitochondrial disease that poses significant challenges for affected families and healthcare systems, and comprehensive knowledge base entries—grounded in current evidence and ontology frameworks—are essential for supporting diagnosis, counseling, and future therapeutic innovation.

## Reference Validation

No PMID or DOI references were found in this report.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 72 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 37 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014198` (8 mentions) - the report calls it "if available", "MONDO", "FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome"; MONDO calls it **mitochondrial DNA depletion syndrome 13**
- `HP:0031486` (1 mention) - the report calls it "Mitochondrial DNA depletion syndrome"; HP calls it **Vascular malformation of the lip**
- `HP:0011010` (1 mention) - the report calls it "Feeding difficulties"; HP calls it **Chronic**
- `HP:0001626` (1 mention) - the report calls it "Cardiomyopathy"; HP calls it **Abnormality of the cardiovascular system**
- `HP:0001272` (1 mention) - the report calls it "Congenital heart malformation"; HP calls it **Cerebellar atrophy**
- `HP:0002093` (2 mentions) - the report calls it "Pulmonary hypertension"; HP calls it **Respiratory insufficiency**
- `HP:0001876` (1 mention) - the report calls it "Bone marrow failure"; HP calls it **Pancytopenia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001252` (3 mentions) - the report calls it "Hypotonia", "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0002500` (1 mention) - the report calls it "White matter abnormalities"; HP calls it **Abnormal cerebral white matter morphology**, and lists "White matter abnormalities" among its other names
- `HP:0002151` (1 mention) - the report calls it "Elevated serum lactate"; HP calls it **Increased circulating lactate concentration**, and lists "Increased serum lactate" among its other names
- `HP:0001999` (2 mentions) - the report calls it "Facial dysmorphism", "Craniofacial dysmorphism"; HP calls it **Abnormal facial shape**, and lists "Facial dysmorphism" among its other names
- `HP:0000519` (1 mention) - the report calls it "Congenital cataract"; HP calls it **Developmental cataract**, and lists "Cataract, congenital" among its other names
- `GO:0000422` (3 mentions) - the report calls it "mitophagy", "autophagy of mitochondrion"; GO calls it **autophagy of mitochondrion**, and lists "mitophagy" among its other names
- `GO:0010498` (2 mentions) - the report calls it "SCF-dependent proteasomal ubiquitin-dependent protein catabolic process"; GO calls it **proteasomal protein catabolic process**
- `GO:1901524` (1 mention) - the report calls it "negative regulation of mitophagy"; GO calls it **regulation of mitophagy**
- `GO:0032543` (1 mention) - the report calls it "mitochondrial DNA metabolic process"; GO calls it **mitochondrial translation**, and lists "mitochondrial protein anabolism" among its other names
- `GO:0006979` (1 mention) - the report calls it "oxidative stress"; GO calls it **response to oxidative stress**
- `GO:0070265` (1 mention) - the report calls it "necrotic cell death"; GO calls it **obsolete necrotic cell death**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014198` - called "if available", "MONDO", "FBXL4-related encephalomyopathic mitochondrial DNA depletion syndrome"
- `HP:0001252` - called "Hypotonia", "Muscular hypotonia"
- `HP:0001999` - called "Facial dysmorphism", "Craniofacial dysmorphism"
- `GO:0000422` - called "mitophagy", "autophagy of mitochondrion"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`, `Chr6`.
