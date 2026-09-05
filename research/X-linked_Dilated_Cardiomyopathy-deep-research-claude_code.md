---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: true
start_time: '2026-09-03T15:02:20.571728'
end_time: '2026-09-03T15:02:20.575829'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: X-linked Dilated Cardiomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 24
  total_cost_usd: 1.4517296000000002
  session_id: eccb37f5-d277-53f4-9bc9-b541745fd0d8
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Dilated Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked Dilated Cardiomyopathy** covering all of the
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

I'll research this now via targeted web searches covering genetics, mechanism, phenotype, and clinical management of X-linked dilated cardiomyopathy (XLCM), then compile the full report.

# X-Linked Dilated Cardiomyopathy: Comprehensive Research Report

## 1. Disease Information

### Overview

X-linked dilated cardiomyopathy (XLDCM, also abbreviated XLCM) is a cardiospecific phenotype of dystrophinopathy — the same gene (*DMD*, encoding dystrophin) that causes Duchenne (DMD) and Becker (BMD) muscular dystrophy, but expressed almost exclusively as heart muscle disease with minimal or absent skeletal myopathy. It was first delineated as a distinct clinical entity by **Berko and Swift (1987)**, who described a five-generation kindred with 11 young males exhibiting rapidly progressive dilated cardiomyopathy (DCM) and congestive heart failure with onset between ages 15–21, and death within 5–12 months of symptom onset; carrier mothers developed a milder, later-onset (40s) DCM ([N Engl J Med 1987;316(19):1186-91](https://www.nejm.org/doi/full/10.1056/NEJM198705073161904), PMID:3574369). Molecular linkage of this phenotype to the centromeric portion of the dystrophin (*DMD*) locus at Xp21 was established by **Towbin et al.** (combined maximum LOD score +4.33) ([PMID:8504498](https://pubmed.ncbi.nlm.nih.gov/8504498/)).

Mechanistically, XLDCM is now understood as one end of a phenotypic continuum produced by *DMD* gene mutations — ranging from classic Duchenne muscular dystrophy (severe, out-of-frame, both skeletal and cardiac muscle affected) through Becker muscular dystrophy (milder, in-frame) to "cardiac-only" XLDCM, in which mutations selectively abolish or destabilize the cardiac (M) dystrophin isoform while sparing skeletal muscle function, often through compensatory up-regulation of brain (B) and Purkinje (P) dystrophin isoforms in skeletal muscle but not in the ventricular myocardium (Muntoni et al., PMID:8361506; Neri et al. 2012, PMID:22455600) — see [Mechanism, §6].

### Key Identifiers

| System | Identifier |
|---|---|
| OMIM | **#302045** — Cardiomyopathy, Dilated, 3B (CMD3B); phenotype MIM caused by *DMD* mutations, Xp21.2-p21.1 ([omim.org/entry/302045](https://omim.org/entry/302045)) |
| Gene (OMIM) | *DMD*, †300377 |
| HGNC | *DMD* HGNC:2928 |
| Inheritance | X-linked (recessive in classic form; manifesting carriers common) |
| ICD-10-CM | I42.8 (Other cardiomyopathies) — no dedicated XLDCM code; some coders use G71.0 (muscular dystrophy) as a cross-reference when dystrophinopathy is documented |
| MeSH | Cardiomyopathy, Dilated (D002311); cross-referenced with Muscular Dystrophy, Duchenne (D009136) |
| Orphanet | XLDCM is not separately coded; it is discussed as a phenotype within the dystrophinopathy spectrum (ORPHA:98896 Duchenne muscular dystrophy / ORPHA:98895 Becker muscular dystrophy) |
| MONDO | Not confirmed via a direct database lookup in this research session — flag this as unresolved; the entity is likely represented indirectly through MONDO's dystrophinopathy/DCM hierarchy rather than as a standalone term. **Verify directly against the MONDO release before curation.** |

### Synonyms
X-linked dilated cardiomyopathy; XLCM; XLDCM; dystrophin-associated dilated cardiomyopathy; cardiac-specific dystrophinopathy; "5′ X-linked dilated cardiomyopathy" (for the promoter/exon-1 subtype).

### Data provenance note
Much of the foundational literature (Berko & Swift 1987; Towbin 1993; Muntoni 1993) derives from **individual pedigree/family case series** rather than large aggregated disease-level registries — XLDCM as a discrete label is a rare, historically pedigree-defined entity. More recent aggregate data on *DMD*-associated DCM prevalence come from cohort screening studies of idiopathic/familial DCM populations (e.g., Italy, Japan, USA cohorts cited below), which are aggregated clinical-genetic studies, not single-patient reports.

---

## 2. Etiology

### Disease Causal Factor
XLDCM is **monogenic**, caused by pathogenic variants in ***DMD*** (dystrophin), Xp21.2-p21.1, the largest known human gene (~2.2 Mb, 79 exons). There is no meaningful environmental or infectious causal contribution to the primary disease process, though secondary modifiers exist (below).

### Genetic Risk Factors
- **Causal variants**: A specific subset of *DMD* mutations produces the cardiac-selective phenotype rather than classic DMD/BMD (detailed in §4 and §6). These cluster in:
  - The muscle-specific promoter and exon 1 (5′ end) — deletions here abolish transcription of the muscle dystrophin isoform (Muntoni et al. 1993, PMID:8361506).
  - Exons 45–55 ("hot-spot" deletion region) — large in-frame or borderline deletions here are disproportionately associated with cardiac-predominant phenotypes with mild/absent skeletal disease and comparatively good response to standard heart-failure therapy (Nakamura et al. 2008, PMID:18261911).
  - Missense variants in the N-terminal actin-binding domain (e.g., K18N in exon 2) and elsewhere (e.g., F3228L in exon 67) that destabilize dystrophin without abolishing production.
  - Splice-site and retrotransposon-insertion mutations (intron 1 splice mutations; L1 element insertions in exon 1 producing frameshift; Yoshida et al. 1993/1998, PMID:8413368, PMID:9618170).
- **Modifier genes**: Utrophin (autosomal paralog of dystrophin) up-regulation partially compensates in skeletal but not cardiac muscle in some genotypes; polymorphisms in genes such as *LTBP4*, *SPP1* (osteopontin), and *ACTN3* are established modifiers of skeletal disease severity in DMD/BMD and are plausible (though less well-studied) modifiers of the cardiac phenotype.
- **Susceptibility in *DMD* carrier females**: Skewed X-chromosome inactivation is the principal genetic risk factor for "manifesting carrier" cardiomyopathy — a higher proportion of X-inactivation of the wild-type allele in cardiomyocytes correlates with more severe cardiac phenotype (source: PMC7397028, review "Cardiac Involvement in Dystrophin-Deficient Females," 2020).

### Environmental / Lifestyle Risk Factors
- **Exercise / mechanical stress ("use hypothesis")**: In dystrophin-deficient (mdx) mice, physical/exercise stress accelerates myocardial damage, supporting a "second hit" mechanotransduction-stress model layered on top of the genetic lesion (Nakamura et al., cited in PMC4491663 review).
- **Age** is a major modifier: cardiomyopathy penetrance in male dystrophinopathy patients is essentially 100% by young adulthood; carrier females typically manifest later (40s–50s).
- **Sex** is intrinsic to X-linked inheritance: males are hemizygous and more severely/uniformly affected; females are heterozygous carriers with variable, X-inactivation-dependent expressivity.
- No specific toxin, occupational, dietary, or infectious risk factor is established for the primary genetic lesion; standard DCM risk modifiers (e.g., alcohol, anthracycline exposure) could theoretically exacerbate cardiac dysfunction in a mutation carrier but are not disease-specific.

### Protective Factors
- **In-frame, exon 45–55 deletions** are relatively "protective" against skeletal myopathy compared with out-of-frame mutations (reading-frame rule; see §4), and this same mutation class is associated with better long-term prognosis and more favorable response to ACE inhibitor/beta-blocker therapy in the cardiac-only phenotype (PMC4491663).
- **Early ACE-inhibitor and beta-blocker initiation** functions as a clinical/pharmacological protective intervention rather than a genetic/environmental one (see §12).
- No validated protective genetic variant (e.g., a modifier allele that prevents cardiomyopathy in a dystrophin-null background) has been established in humans; utrophin up-regulation is protective in model systems (§15) but is not a naturally occurring human protective polymorphism of established effect size.

### Gene-Environment Interactions
The clearest documented gene-environment interaction is the exercise/mechanical-stress interaction in dystrophin-deficient cardiac muscle: the DGC's mechanotransduction role means that mechanical loading (physical exertion) interacts with the underlying membrane fragility to accelerate cardiomyocyte injury — demonstrated in mdx mice and inferred clinically (PMC4491663; PMC9515174, "The role of the dystrophin glycoprotein complex in muscle cell mechanotransduction," *Commun Biol* 2022, PMID:36168044).

---

## 3. Phenotypes

XLDCM's defining phenotypic feature is a **cardiac phenotype occurring in relative or complete isolation from skeletal myopathy** — this is what separates it clinically from typical DMD/BMD cardiomyopathy, which occurs against a background of overt limb-girdle weakness.

### Cardiac phenotypes
| Phenotype | HPO term (suggested) | Onset/Course | Frequency notes |
|---|---|---|---|
| Congestive heart failure | HP:0001635 (Congestive heart failure) | Typically ages 10–20 in classic XLDCM pedigrees; can present later (40s–50s) in manifesting carrier females | Presenting feature in most reported cases |
| Dilated cardiomyopathy (left ventricular dilation/dysfunction) | HP:0001644 (Dilated cardiomyopathy) | Progressive; rapid deterioration in classic pedigrees (symptom-to-death interval 5–12 months in the original Berko & Swift kindred) | Defining feature |
| Reduced left ventricular ejection fraction | HP:0012664 (Ejection fraction reduced) | Progressive | Core diagnostic feature |
| Ventricular arrhythmia | HP:0004308 (Ventricular arrhythmia) | Emerges with disease progression; a major cause of sudden death | Frequent, contributes to mortality |
| Cardiac conduction abnormality | HP:0011675 (Arrhythmia) | Variable | ECG often abnormal before symptoms |
| Elevated R/S ratio in V1–V2 on ECG | (procedural finding, not a standard HPO term) | Present early, sometimes pre-symptomatic | Characteristic ECG signature described across dystrophinopathy cardiac literature |
| Deep Q waves in lateral/inferior leads | (procedural finding) | Early | Characteristic |
| Sudden cardiac death | HP:0001645 (Sudden death) | Can occur without preceding overt heart failure | Documented, including with post-mortem NT-proBNP elevation in pericardial fluid used diagnostically (PMC7476613, PMID:32939432) |

### Skeletal/muscular phenotypes (minimal or absent by definition)
- Exertional myalgia, calf pseudohypertrophy (HP:0003707), and mildly elevated CK can occur even in "pure" XLDCM, and some patients show subclinical myopathic changes on biopsy despite normal strength — the "cardiospecific" label describes the dominant/presenting phenotype, not necessarily complete absence of any skeletal-muscle molecular abnormality.
- Frank proximal weakness, Gowers sign, and progressive ambulatory loss (hallmarks of DMD) are **absent by definition** in classic XLDCM; when present, the case is better classified as DMD/BMD-associated cardiomyopathy rather than "pure" XLDCM.

### Laboratory abnormalities
- **Creatine kinase (CK)**: Ranges from normal (notably in exon 45–55 hotspot deletions and in some late-onset/female cases) to markedly elevated (>2,500 IU/L, versus normal 62–287 IU/L) — CK is not reliably discriminating for XLDCM the way it is for DMD.
- **NT-proBNP**: The most useful serum biomarker for tracking systolic dysfunction; an NT-proBNP threshold >200 pg/mL discriminated severe systolic dysfunction with 90.5% sensitivity / 90.9% specificity in a DMD cardiomyopathy cohort, and NT-proBNP (unlike BNP or troponin) was independently associated with mortality (Circ Heart Fail 2024, [ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.123.010700](https://www.ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.123.010700)).
- **Troponin I**: Transient elevations ("troponin leak") occur even in asymptomatic dystrophinopathy patients and correlate with late gadolinium enhancement (LGE) on cardiac MRI, but standard cardiac biomarkers overall correlate poorly with CMR-defined cardiomyopathy progression (PMC8866537, PMID:34429516) — an important caveat for using troponin as a toxicity/monitoring marker in clinical trials.

### Age of onset, severity, progression, frequency
- **Onset**: Classic XLDCM — adolescence to early adulthood (10–20 years) in males; 4th–5th decade in manifesting female carriers. Later-onset (>50 years) cases with normal CK have also been reported (case report cited in PMC4491663).
- **Severity/progression**: Highly genotype-dependent. Promoter/exon-1 mutations (5′ XLDCM) tend toward rapid, severe progression; exons 45–55 deletions tend toward a milder course with better pharmacologic responsiveness.
- **Frequency of *DMD* mutations among DCM cohorts** (i.e., how often "idiopathic"/familial DCM turns out to be dystrophin-related): Italy 13/201 (6.5%) (Arbustini et al. 2000, PMID:10841222); Japan 3/99 (3%) (Shimizu et al. 2005, PMID:15671604); USA pediatric cohort 3/22 (13.6%) (source: PMC4491663 synthesis).

### Quality of life impact
No disease-specific QOL instrument for XLDCM was identified in this search; QOL burden is inferred from the DMD/BMD cardiomyopathy literature and general pediatric heart-failure QOL data (PedsQL, EQ-5D), where progressive heart failure, arrhythmia burden, and — particularly for classic XLDCM — a compressed, unpredictable disease course (death within months of symptom onset in the original kindred) impose severe QOL and psychosocial burden on both patients and, given the late-onset carrier phenotype, mothers as well.

---

## 4. Genetic/Molecular Information

### Causal Gene
- ***DMD*** (dystrophin), Xp21.2-p21.1; HGNC:2928; OMIM gene *300377. The gene spans ~2.2 Mb (largest in the human genome), with multiple tissue-specific promoters driving distinct transcripts/isoforms (full-length muscle [Dp427m], brain [Dp427c], and Purkinje [Dp427p] isoforms from the 5′ end, plus shorter internal-promoter isoforms Dp260, Dp140, Dp116, Dp71).

### Pathogenic Variant Classes Specific to XLDCM
1. **Muscle-promoter/exon 1 deletions** ("5′ XLDCM") — abolish Dp427m (muscle) transcription while leaving Dp427c (brain/Purkinje) isoform loci intact; skeletal muscle compensates by up-regulating the brain isoform, but the ventricular myocardium does not, because Dp427c is normally expressed there only in atria and conduction tissue, not ventricles (Muntoni et al. 1993, PMID:8361506; mechanistic confirmation in Neri et al. 2012, PMID:22455600, "The absence of dystrophin brain isoform expression in healthy human heart ventricles explains the pathogenesis of 5′ X-linked dilated cardiomyopathy," *BMC Med Genet*).
2. **Exons 45–55 hotspot deletions** — the single most common deletion region in dystrophinopathy generally; in-frame deletions here can produce a cardiac-predominant phenotype with mild/absent skeletal involvement (Nakamura et al. 2008, PMID:18261911).
3. **Missense variants** in the actin-binding domain (e.g., p.Lys18Asn in exon 2) or elsewhere (e.g., p.Phe3228Leu in exon 67) that destabilize the protein without eliminating expression.
4. **A recently reported de novo missense variant, p.Asp3368Gly**, associated with XLDCM plus skeletal myopathy, characterized with clinical and in silico structural analysis (PMC10931831, 2024).
5. **Splice-site mutations** (e.g., intron 1, IVS5+1 in intron 5) and **retrotransposon (L1) insertions** in exon 1 causing frameshift (Yoshida et al., PMID:8413368, PMID:9618170).
6. **A recurrent frameshift, c.3779_3785delCTTTGGAinsGG** in exon 27, reported in the XLDCM literature.

### Reading-Frame Rule
The classic dystrophinopathy genotype-phenotype correlate: **out-of-frame** deletions/duplications disrupt the reading frame and produce a truncated, non-functional protein → severe DMD phenotype; **in-frame** mutations preserve the reading frame, yielding a partially functional, internally truncated protein → milder BMD phenotype. XLDCM occupies a distinctive niche within (and sometimes outside) this rule — cardiac-restricted phenotypes can arise from in-frame mutations in regions dispensable for skeletal-muscle function but critical for cardiac-specific dystrophin-binding partner interactions (e.g., nNOS binding via the rod-domain repeats 16–17), or from mutations that differentially affect tissue-specific isoform/promoter usage rather than obeying the frame rule at all.

### Variant Classification and Population Frequency
- ClinVar/ACMG classification of specific XLDCM-associated variants should be verified per-variant; the deletions and point mutations cited above are generally classified pathogenic/likely pathogenic in the literature reporting them, based on segregation with the cardiac phenotype and (for deletions) reading-frame/isoform-disruption logic.
- Population allele frequency in gnomAD for large structural *DMD* deletions is expected to be essentially zero given the severity of the classic phenotype; specific missense variants (e.g., K18N, F3228L, D3368G) should be checked individually against gnomAD — this was not independently verified via database query in this session and should be confirmed before curation.
- **Somatic vs. germline**: XLDCM-causing variants are germline; there is no established somatic-mosaicism disease model for this entity beyond the general phenomenon of germline/somatic mosaicism recognized across dystrophinopathies (relevant to recurrence-risk counseling).

### Functional Consequences
Predominantly **loss of function** (null/near-null muscle-isoform expression from promoter/exon-1 mutations) or **partial loss of function / destabilization** (missense variants, in-frame deletions) rather than gain-of-function or dominant-negative mechanisms — consistent with dystrophin's structural/scaffolding role (see §6).

### Modifier Genes
No XLDCM-specific modifier gene has been rigorously validated in this literature search; general DMD/BMD skeletal-muscle severity modifiers (*LTBP4*, *SPP1/osteopontin*, *ACTN3*) are candidates for cardiac modifier study but are not established as such.

### Chromosomal Abnormalities
XLDCM is caused by intragenic *DMD* deletions/duplications/point mutations rather than large chromosomal rearrangements; contiguous gene deletion syndromes involving *DMD* plus neighboring genes (e.g., glycerol kinase deficiency, congenital adrenal hypoplasia) produce a different, syndromic phenotype and are not the XLDCM entity per se.

### Epigenetics
No XLDCM-specific epigenetic (DNA methylation/histone) mechanism was identified in this search; the isoform-switching mechanism (§6) is transcriptional/promoter-based rather than classically epigenetic, though promoter-region deletions functionally abolish the regulatory element itself rather than altering its methylation state.

---

## 5. Environmental Information

XLDCM is a monogenic disorder with no established primary environmental, toxic, or infectious causal agent. The relevant environmental modifiers are:

- **Physical exertion / mechanical loading**: proposed as a "second hit" that accelerates myocardial injury on a dystrophin-null background (the "use hypothesis," supported in mdx mouse exercise studies cited in PMC4491663). This has direct clinical translation — activity restriction is often part of dystrophinopathy cardiac management guidance, though formal evidence specific to XLDCM (as opposed to DMD generally) is limited.
- **Cardiotoxic exposures** (e.g., anthracyclines, alcohol) are not disease-specific risk factors but would be expected to compound dysfunction in a mutation carrier, by general cardiology principles; no XLDCM-specific literature on this interaction was found.
- **Infectious agents**: no infectious trigger or myocarditis-superimposition literature specific to XLDCM was identified in this search (in contrast to some other DCM etiologies, e.g., viral myocarditis-triggered DCM).

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from initiating lesion to clinical manifestation)

1. A germline pathogenic *DMD* variant (promoter/exon-1 deletion, hotspot exon 45–55 deletion, or destabilizing missense/splice variant) **disrupts production, stability, or tissue-specific isoform expression** of dystrophin — demonstrated directly. (Muntoni 1993, PMID:8361506; Towbin 1993, PMID:8504498)
2. For promoter/exon-1 (5′) mutations specifically, this **abolishes transcription of the muscle (Dp427m) dystrophin isoform**. In skeletal muscle, this loss is **compensated** by transcriptional up-regulation of the brain (Dp427c) and Purkinje (Dp427p) isoforms from intact downstream promoters — demonstrated. (Muntoni 1993)
3. In **ventricular myocardium**, the brain isoform is not normally expressed (it is confined to atria and cardiac conduction tissue in the healthy heart), so **no compensatory isoform is available** — this step is the direct explanation for cardiac-selective vulnerability and is demonstrated by isoform-expression mapping of healthy human hearts. (Neri et al. 2012, PMID:22455600) → **leads to** unmitigated loss of functional dystrophin specifically in ventricular cardiomyocytes.
4. Loss (or destabilization) of dystrophin **disrupts the dystrophin-glycoprotein complex (DGC)**, which normally links the intracellular actin cytoskeleton through the sarcolemma to the extracellular matrix (laminin-α2) — demonstrated structurally and biochemically. (PMC9515174, *Commun Biol* 2022, PMID:36168044) → **results in** loss of sarcolemmal mechanical integrity and disrupted mechanotransduction signaling.
5. A structurally compromised sarcolemma is **mechanically fragile under contractile/mechanical stress** — demonstrated in cell and animal models — **leading to** microtears in the cardiomyocyte membrane during normal cardiac cycling, exacerbated by physical exertion (the "use hypothesis"; mdx mouse exercise data cited in PMC4491663).
6. Membrane microdamage **causes pathological calcium influx and intracellular calcium mishandling/overload** — demonstrated mechanistically in cardiomyocyte models (PMC7074327, "Dysregulation of Calcium Handling in Duchenne Muscular Dystrophy-Associated Dilated Cardiomyopathy") → **results in** activation of calcium-dependent proteases (calpains), mitochondrial calcium overload, and downstream cell-death signaling.
7. Chronic calcium dysregulation and membrane injury **drive cardiomyocyte necrosis and apoptosis**, with secondary **replacement fibrosis and fatty infiltration**, characteristically beginning in the **left ventricular posterobasal/inferolateral wall** — demonstrated on myocardial biopsy and cardiac MRI (late gadolinium enhancement) across dystrophinopathy cardiomyopathy studies, and specifically noted for XLDCM in the PMC4491663 synthesis.
8. Progressive myocyte loss and fibrotic replacement **impair contractile function and electrical conduction**, **leading to** progressive left ventricular dilation, reduced ejection fraction, and re-entrant/ectopic arrhythmia substrate — demonstrated clinically (echocardiography, ECG).
9. This **culminates in** the clinical syndrome of congestive heart failure, ventricular arrhythmia, and — in a substantial subset — **sudden cardiac death**, sometimes as the presenting event (documented post-mortem via elevated pericardial-fluid NT-proBNP; PMC7476613, PMID:32939432).

**Branch point (inferred, not fully demonstrated in humans):** A parallel/contributing pathway proposes that certain missense or in-frame mutations act principally by **destabilizing dystrophin's interaction with binding partners**, notably **neuronal nitric oxide synthase (nNOS)** via the rod-domain spectrin repeats 16–17, rather than (or in addition to) abolishing DGC mechanical linkage outright — this would perturb nitric-oxide-dependent vascular and metabolic regulation in the myocardium. This mechanism is proposed in the literature (Franz et al., cited in PMC4491663) but is less directly demonstrated for the cardiac-selective phenotype than the isoform-compensation mechanism above, and should be treated as a secondary/candidate branch rather than an established parallel causal chain.

### Molecular pathways and cellular processes
- **DGC/mechanotransduction signaling** (GO:0007169-adjacent mechanosensitive pathways) — primary disrupted pathway.
- **Calcium-handling/excitation-contraction coupling** — secondarily dysregulated (GO:0086001, cardiac muscle cell action potential; GO:0086036, regulation of cardiac muscle cell membrane potential are candidate GO terms).
- **Fibrotic remodeling response** — cardiac fibroblast activation and extracellular matrix deposition following myocyte loss (a process the dismech KB models generically via the `fibrotic_response` module — relevant `conforms_to` target if curating this entry: e.g., a node such as "Cardiac Fibroblast Activation" conforming to `fibrotic_response#Mesenchymal Cell Activation`).
- **Apoptosis/necrosis** — GO:0006915 (apoptotic process) and necrotic cell-death pathways downstream of calcium overload.
- **Nitric oxide signaling** (nNOS-dystrophin axis) — candidate secondary pathway (GO:0006809, nitric oxide biosynthetic process).

### Protein dysfunction
Loss of function (null) or destabilization (reduced half-life / disrupted binding-partner interactions) of the 427-kDa full-length dystrophin protein; UniProt P11532 (human DMD/dystrophin). No gain-of-function or dominant-negative mechanism is established for XLDCM specifically.

### Cell types and biological processes (candidate CL/GO term suggestions for KB curation)
- **Cell types**: cardiac muscle cell (CL:0000746), ventricular cardiac myocyte, cardiac fibroblast (CL:0002548).
- **Anatomical/subcellular**: sarcolemma (GO:0042383, sarcolemma — Cellular Component), sarcoplasmic reticulum, mitochondrion (secondary calcium-overload target).

### Molecular profiling and advanced technologies
No large-scale transcriptomic/proteomic/single-cell dataset specific to human XLDCM cardiac tissue was identified in this search — the rarity and lethality of the classic phenotype has historically limited access to fresh myocardial tissue for such profiling. Isoform-expression mapping (Neri et al. 2012) used targeted RT-PCR/immunohistochemistry on autopsy/explanted human ventricular tissue rather than genome-wide profiling. Human iPSC-derived cardiomyocyte (hiPSC-CM) models are an emerging platform for preclinical mechanistic and exon-skipping efficacy testing in dystrophin-deficient cardiomyocytes (cited in PMC4491663, referencing exon-51-skipping antisense oligonucleotide studies achieving ~30% wild-type dystrophin restoration in hiPSC-CMs).

---

## 7. Anatomical Structures Affected

- **Organ level**: Heart (primary); specifically **left ventricle** (predominant chamber affected, particularly the posterobasal/inferolateral free wall). Skeletal muscle is spared or only mildly/subclinically involved by definition of the "pure" XLDCM phenotype (UBERON:0000948 heart; UBERON:0002084 heart left ventricle).
- **Secondary/complication-level organ involvement**: lungs (pulmonary congestion from heart failure), liver (congestive hepatopathy), kidneys (cardiorenal syndrome) — standard heart-failure sequelae, not primary disease targets.
- **Body systems**: Cardiovascular system primarily; the neuromuscular system is the "other" system implicated by the causal gene but is the *spared* system in this specific phenotype, which is the disease's defining clinical feature.
- **Tissue/cell level**: Cardiac (striated) muscle tissue; ventricular cardiomyocytes as the principal affected cell population; cardiac fibroblasts secondarily activated in the fibrotic-replacement process; cardiac conduction system tissue (implicated in arrhythmia generation).
- **Subcellular level**: Sarcolemma (site of primary DGC disruption), sarcoplasmic reticulum and mitochondria (secondary calcium-handling/energetic dysfunction), cytoskeleton (actin-dystrophin linkage).
- **Localization**: Typically **bilateral-chamber but LV-predominant**; myocardial biopsy/CMR literature specifically flags the LV posterobasal wall as an early and characteristic site of fibrofatty replacement.

---

## 8. Temporal Development

- **Onset**: Classic XLDCM manifests in **adolescence/young adulthood** (10–20 years) in hemizygous males; **manifesting female carriers** typically present later, in the **4th–5th decade**. Some case reports describe onset as late as the 6th decade (a 50-year-old patient with normal CK, cited in PMC4491663). Onset pattern is generally **insidious**, with pre-symptomatic ECG or biomarker abnormalities often detectable before overt heart failure.
- **Progression**: Rate is strongly genotype-dependent — the original Berko & Swift kindred showed **rapid, lethal progression** (death 5–12 months after symptom onset); a documented case showed cardiothoracic ratio increasing from 47% (age 12) to 71% (age 18) before death. In contrast, exon 45–55 hotspot deletions are associated with a **more indolent course** and better medication responsiveness. Overall course is **progressive** rather than relapsing-remitting, though rate of decline is highly variable by genotype.
- **Stages**: Not formally staged with a disease-specific system; standard heart-failure staging (ACC/AHA Stage A–D, NYHA functional class) is applied clinically.
- **Remission**: No spontaneous remission is described; pharmacologic stabilization of LV function (with ACE inhibitors/beta-blockers) can arrest or slow progression in some genotypes, but this is disease modification/stabilization rather than remission.
- **Critical periods**: Early adolescence (for males) appears to be a key window for **pre-symptomatic surveillance** — standard dystrophinopathy cardiac-care guidelines recommend baseline cardiac evaluation by age 6 and annual evaluation from approximately age 10 onward, precisely because subclinical cardiac dysfunction can precede symptoms by years (see §10).

---

## 9. Inheritance and Population

### Epidemiology
- XLDCM as a narrowly defined "cardiac-only" entity is **very rare**, historically reported as individual pedigrees rather than population-based incidence/prevalence figures — no dedicated incidence/prevalence estimate for the isolated cardiac phenotype was located in this search.
- Broader context: **non-ischemic DCM overall** has an estimated prevalence around **1 in 220** by cardiac MRI-based studies, with prevalence roughly **twice as high in men** as women, and asymptomatic idiopathic DCM prevalence potentially ≥1 in 250 ([Nat Rev Cardiol epidemiology review](https://www.nature.com/articles/s41569-026-01300-z)).
- Within cohorts of "idiopathic"/familial DCM screened for *DMD* mutations, the yield is **3–13.6%** depending on population and case-ascertainment (Italy 6.5%, PMID:10841222; Japan 3%, PMID:15671604; a US pediatric cohort 13.6%, per PMC4491663) — indicating *DMD* mutations are a clinically meaningful, likely underrecognized, cause of pediatric and young-adult DCM presenting without overt skeletal myopathy.

### Inheritance Pattern
**X-linked**, classically recessive at the population level but with frequent **manifesting heterozygotes** (carrier females) due to skewed X-inactivation — clinically this produces a pattern of early-onset disease in males and later-onset, generally milder (but not trivial) disease in obligate carrier females, **with no male-to-male transmission** (a key pedigree clue distinguishing X-linked from autosomal dominant DCM).

### Penetrance and Expressivity
- **Penetrance in males**: Essentially complete for cardiac disease by adulthood in classic XLDCM pedigrees, though age of onset and rate of progression are highly variable by mutation type.
- **Penetrance/expressivity in female carriers**: **Variable and X-inactivation-dependent** — cardiomyopathy is common in DMD carriers (estimates from the broader dystrophinopathy-carrier literature suggest cardiac abnormalities in up to ~40s% of carriers screened by CMR/echo over time, though estimates vary by study and modality), and carrier cardiomyopathy may be the **initial or only manifestation** of the underlying mutation (PMC7397028, "Cardiac Involvement in Dystrophin-Deficient Females," *Genes* 2020, PMID cross-referenced via DOI:10.3390/genes11070765).
- **Genetic anticipation**: Not a recognized feature of *DMD*-associated cardiomyopathy (unlike repeat-expansion disorders).
- **Germline mosaicism**: Recognized generally in dystrophinopathy (relevant to recurrence-risk counseling for de novo cases) but not specifically quantified for the XLDCM subphenotype.
- **Founder effects / carrier frequency**: No XLDCM-specific founder mutation was identified in this search; the exons 45–55 deletion hotspot is a recurrent, non-founder mutational hotspot common to dystrophinopathy generally (attributable to the region's susceptibility to Alu-mediated recombination), not a single population-specific founder allele.
- **Consanguinity**: Not a relevant risk factor for an X-linked condition in the way it is for autosomal recessive disease (though it can increase homozygosity in rare affected females).

### Population Demographics
- **Sex ratio**: Overwhelmingly male-predominant for the classic, early/severe phenotype, consistent with X-linked inheritance; carrier females represent a distinct, later-onset risk group rather than an equally affected group.
- **Ethnic/geographic distribution**: No specific ethnic or geographic enrichment for XLDCM was identified; *DMD*-mutation-attributable DCM has been documented across multiple studied populations (Italian, Japanese, American cohorts cited above), suggesting the phenomenon is not geographically restricted, though systematic global prevalence data are lacking.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **Creatine kinase (CK)**: Variably elevated (normal to markedly elevated, e.g., >2,500 IU/L); notably **can be normal**, especially with exon 45–55 hotspot deletions or in later-onset/female cases — CK is a supportive but non-discriminating test for XLDCM specifically (in contrast to its high sensitivity for classic DMD).
- **NT-proBNP**: The best-validated serum biomarker for tracking systolic dysfunction and mortality risk in dystrophinopathy cardiomyopathy broadly; threshold >200 pg/mL for severe systolic dysfunction (90.5%/90.9% sensitivity/specificity) (Circ Heart Fail 2024).
- **Troponin I**: Detects subclinical myocardial injury ("troponin leak") correlating with LGE on CMR, but is not well correlated with overall cardiomyopathy progression and should be interpreted cautiously, especially in the context of drug-toxicity monitoring in trials (PMID:34429516).

### Imaging
- **Echocardiography**: First-line, serial modality for LV size/function; shows LV enlargement, wall-motion abnormality, systolic/diastolic dysfunction.
- **Cardiac MRI (CMR)**: Recommended to be incorporated into surveillance by early adolescence; detects **late gadolinium enhancement (LGE)**, the imaging correlate of the characteristic LV posterobasal/inferolateral fibrofatty replacement, often preceding overt systolic dysfunction on echo.

### Electrophysiology
- **ECG**: Characteristic (though not pathognomonic) findings — high R/S ratio (R/S >1) in right precordial leads (V1–V2), deep Q waves in lateral (I, aVL, V5–V6) or inferior leads, sinus tachycardia, shortened PR interval, and various arrhythmias (sinus arrhythmia, atrial/ventricular ectopy). These findings can precede symptomatic heart failure and are part of recommended baseline/surveillance evaluation.

### Biopsy/Pathology
- **Skeletal muscle biopsy**: In "pure" XLDCM, shows only mild myogenic changes (fiber-size variation, occasional necrosis, centronuclear fibers) despite normal strength; **dystrophin immunostaining shows absence or reduction of dystrophin**, confirming the molecular diagnosis even in the absence of clinical myopathy.
- **Myocardial biopsy** (rarely performed given risk, more often assessed via CMR or at transplant/autopsy): replacement fibrosis/fatty infiltration, especially LV posterobasal wall; atrophic myocyte changes with loss of striation, vacuolation, and nuclear degeneration.

### Genetic Testing
- **Multiplex ligation-dependent probe amplification (MLPA) or targeted deletion/duplication analysis** of *DMD* is the recommended first-tier test given that ~65–70% of dystrophinopathy-causing mutations are deletions/duplications; **sequencing** (gene panel, exome, or genome) is needed to detect point mutations, small indels, and deep intronic/splice variants (e.g., the K18N, F3228L, D3368G missense variants and splice-site mutations described above).
- **Muscle-promoter/exon-1-specific analysis** is particularly relevant when XLDCM is clinically suspected (cardiac-predominant phenotype with normal/near-normal strength), since standard multi-exon deletion panels can sometimes under-detect isolated promoter-region lesions if probe coverage is incomplete.
- **Family segregation studies / carrier testing**: Central to counseling in this X-linked condition — once a proband's variant is identified, targeted testing of at-risk female relatives (mothers, sisters, maternal aunts) for carrier status and subsequent cardiac screening is standard practice.

### Clinical Criteria / Differential Diagnosis
XLDCM should be distinguished from:
- Classic DMD/BMD-associated cardiomyopathy (skeletal myopathy present and typically dominates the clinical picture).
- **Barth syndrome** (*TAZ*/tafazzin, Xq28) — X-linked, presents in infancy/early childhood with DCM ± LV noncompaction, endocardial fibroelastosis, skeletal myopathy, neutropenia, growth delay, and 3-methylglutaconic aciduria; a metabolically and clinically distinct X-linked cardiomyopathy (see §14 for detail).
- **Danon disease** (*LAMP2*, Xq24) — X-linked dominant lysosomal disorder; predominantly **hypertrophic** cardiomyopathy in males (dilated/hypertrophic mix in females), with Wolff-Parkinson-White pattern (68% of males, 27% of females), skeletal myopathy, and intellectual disability — mechanistically and phenotypically distinct from dystrophin-related XLDCM despite both being X-linked cardiomyopathies.
- **X-linked Emery-Dreifuss muscular dystrophy** (*EMD*/emerin, Xq28) — joint contractures plus cardiac conduction defects/arrhythmia progressing to dilated cardiomyopathy; some *EMD* missense variants have been reported to cause **isolated dilated cardiomyopathy without the classic EDMD triad** (PMC12185710, 2025), making this an important differential/mimic for "isolated" X-linked DCM alongside dystrophin-related XLDCM.
- Non-genetic causes of pediatric/young-adult DCM (myocarditis, etc.) should be excluded per standard DCM work-up.

### Screening
No population-based newborn screening exists specifically for XLDCM (newborn CK-based screening programs for DMD exist in some regions/countries but are aimed at classic DMD, not the cardiac-only phenotype). **Cascade/targeted screening** of at-risk relatives once a family *DMD* variant is known — and routine cardiac screening of DMD/BMD carrier females — is the relevant applied screening paradigm (ACMG/genetic-counseling guidance for dystrophinopathy carriers recommends baseline and periodic cardiac evaluation).

---

## 11. Outcome/Prognosis

- **Survival**: Highly genotype-dependent. In the original Berko & Swift kindred, affected males survived only **5–12 months from symptom onset**, dying typically in their late teens/early 20s. In contrast, patients with exons 45–55 deletions have been reported to have **relatively good life expectancy** with appropriate heart-failure therapy. Comparative registry data on DMD- vs. BMD- vs. other-etiology DCM show **5-year survival after cardiomyopathy diagnosis of 57% in DMD, 100% in BMD, and 71% in other DCM etiologies** (Pediatric Cardiomyopathy Registry, PMID:18513510) — though this compares classic DMD/BMD (with skeletal disease) rather than isolated XLDCM specifically, it is the best available comparative mortality benchmark in the *DMD*-cardiomyopathy space.
- **Cause of death**: Progressive heart failure and/or lethal ventricular arrhythmia/sudden cardiac death; sudden death can occur without prior overt heart-failure symptoms (documented via elevated pericardial NT-proBNP at autopsy, PMID:32939432).
- **Heart transplantation outcomes**: For dystrophinopathy-associated cardiomyopathy patients who reach transplant, survival is comparable to non-dystrophinopathy transplant recipients — **89% vs. 91% at 1 year and 83% vs. 78% at 5 years**, with no significant difference in rejection, infection, or allograft vasculopathy rates (cited via ScienceDirect summary, "Clinical outcomes after cardiac transplantation in muscular dystrophy patients"). A more recent single-center case series reported **100% survival** at median 16-month follow-up with good functional capacity, albeit with some postoperative respiratory/swallowing complications reflecting underlying neuromuscular comorbidity (PMID:28580208, "Heart transplantation in patients with dystrophinopathic cardiomyopathy: Review of the literature and personal series").
- **Prognostic factors**: Mutation location/type (5′ promoter-exon 1 mutations portend more severe cardiac-selective disease; exon 45–55 deletions portend milder, more treatable disease), degree of X-inactivation skewing in carrier females, presence and extent of LGE on CMR, and NT-proBNP level.
- **Morbidity**: Progressive heart failure symptoms, arrhythmia burden (requiring, in some cases, ICD/pacemaker), and — in patients who also carry some skeletal-muscle involvement — additive neuromuscular disability; QOL burden is substantial given the often rapid, unpredictable course in the severe subtype.

---

## 12. Treatment

### Pharmacotherapy (standard heart-failure therapy, first line)
- **ACE inhibitors** (e.g., perindopril, lisinopril) — foundational therapy; NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to the specific agent.
- **Beta-blockers** (e.g., bisoprolol) — combination ACE-inhibitor + beta-blocker therapy showed significant improvement in LV fractional shortening compared with ACE-inhibitor monotherapy in the dystrophinopathy-cardiomyopathy literature cited in PMC4491663.
- **Angiotensin receptor blockers (ARBs)** (e.g., losartan) — a randomized double-blind trial of lisinopril vs. losartan in DMD cardiomyopathy showed both effective, without conclusively establishing superiority of one over the other (PMC3871420).
- **Mineralocorticoid receptor antagonists, diuretics, digoxin** — standard adjuncts for symptomatic heart failure.
- **Prophylactic (pre-symptomatic) ACE-inhibitor/beta-blocker therapy**: The **DMD Heart Protection Study** (randomized, placebo-controlled trial of perindopril + bisoprolol in boys with DMD aged 5–13 with normal LV function) found **no significant difference in LV function between early/prophylactic and delayed treatment arms at 36 or 60 months** of follow-up, raising an open question about whether prophylactic therapy confers meaningful benefit over prompt treatment once dysfunction is first detected (PMID:30573480 protocol; PMID:40130400 long-term follow-up, *Eur J Neurol* 2025). This is an important, recent (2025) nuance for clinical guidance — prophylactic therapy is not unambiguously superior to a "treat at first detected dysfunction" strategy in trial data, though the trial itself notes methodological limitations (small numbers, no untreated control arm at long-term follow-up, echo insensitivity).
- **Corticosteroids**: Beneficial for skeletal and cardiac outcomes in classic DMD but **not specifically recommended** for the isolated XLDCM cardiac phenotype, per the PMC4491663 synthesis.

### Advanced/Interventional Therapies
- **Cardiac resynchronization therapy / pacemakers**: For ventricular dyssynchrony or conduction disease.
- **Implantable cardioverter-defibrillator**: Relevant given the arrhythmia/sudden-death risk, though disease-specific ICD-outcome data for XLDCM specifically were not located in this search.
- **Partial left ventriculectomy (Batista procedure)** and **LV assist devices**: Described as options in the dystrophinopathy cardiomyopathy literature for advanced/refractory disease.
- **Heart transplantation**: The only curative option for end-stage dystrophinopathy-associated heart failure refractory to medical therapy; outcomes are comparable to non-dystrophinopathy transplant recipients (see §11), making transplant a reasonable option specifically in patients whose skeletal/pulmonary status (in "pure" XLDCM, typically preserved) does not preclude major surgery — an important point of differentiation from classic DMD, where respiratory/neuromuscular comorbidity often complicates transplant candidacy.

### Experimental / Gene-Targeted Therapeutics (Duchenne/dystrophinopathy pipeline, cardiac-relevant)
- **Exon-skipping antisense oligonucleotides** (e.g., eteplirsen [exon 51], golodirsen, viltolarsen, casimersen — FDA-approved for skeletal-muscle indications in eligible DMD genotypes) convert out-of-frame to in-frame mutations at the RNA level; cardiac delivery efficiency is a recognized limitation relative to skeletal muscle. hiPSC-cardiomyocyte studies show exon-51-skipping AOs can restore dystrophin to ~30% of wild-type levels in vitro (cited in PMC4491663).
- **AAV micro-dystrophin gene therapy**: Multiple constructs in clinical development for DMD skeletal-muscle disease (e.g., fordadistrogene movaparvovec, delandistrogene moxeparvovec). Cardiac efficacy data are earlier-stage: a micro-dystrophin construct optimized for skeletal efficacy (AAV-μDys5) fully prevented cardiac pathology and preserved ejection fraction (>45%) through 18 months in a severe DMD mouse model (Fiona/dko), while **some other microdystrophin constructs paradoxically accelerated cardiac disease**, apparently via competition between micro-dystrophin and utrophin at the cardiomyocyte membrane — a significant, actively studied safety signal (PMC11382885, "Potential limitations of microdystrophin gene therapy for Duchenne muscular dystrophy," 2024). Because DMD cardiomyopathy typically emerges in the teens while current gene-therapy trials are conducted in young boys, **it will likely be a decade before human cardiac clinical outcomes from these gene therapies are known** — an important caveat for current disease-modeling/treatment-planning purposes.
- **Membrane sealants** (e.g., poloxamer 188): improved ventricular geometry in dystrophic mice and prevented cardiac injury/dilation in dystrophic dogs (Metzger et al., cited in PMC4491663) — a mechanistically distinct, membrane-stabilizing (rather than gene-restorative) therapeutic strategy.
- **AAV-microutrophin**: Reported to confer durable cardioprotection against pharmacologic and exercise-induced injury in the mdx mouse (2025 preclinical study).

### Treatment Algorithm / Strategy
Standard approach: (1) baseline and serial cardiac surveillance (§10) from diagnosis; (2) initiate ACE-inhibitor/ARB ± beta-blocker at first detection of LV dysfunction (with an open question, per the 2025 DMD Heart Protection Study follow-up, about whether earlier prophylactic initiation adds benefit over prompt treatment at first detected dysfunction); (3) escalate to standard advanced heart-failure therapies (MRA, device therapy) as needed; (4) consider transplantation for refractory end-stage disease, particularly favorable in "pure" XLDCM given typically preserved skeletal/respiratory status relative to classic DMD.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the classic sense for a monogenic disorder, other than **reproductive genetic counseling** — carrier testing of at-risk female relatives, prenatal diagnosis, and preimplantation genetic testing (PGT) are the relevant "primary prevention" tools once a familial *DMD* variant is identified.
- **Secondary prevention (early detection)**: **Systematic cardiac screening of at-risk individuals** — both males in families with known *DMD* mutations and, critically, **female carriers**, who are often clinically silent for skeletal disease but at meaningful risk of cardiomyopathy. Dystrophinopathy-specific guidelines (per GeneReviews/multidisciplinary cardiac-care consensus) recommend baseline cardiac evaluation (ECG + echo and/or CMR) at diagnosis or by age 6, with at least annual complete cardiac evaluation from ~age 10 in DMD (more frequent — every 6 months — once ventricular dysfunction is detected) and at least biennial evaluation from diagnosis in BMD; carrier females warrant baseline evaluation with periodic follow-up given their variable, X-inactivation-dependent risk (PMC9577913, "Cardiac care of children with dystrophinopathy and females carrying DMD-gene variations").
- **Tertiary prevention**: Early pharmacotherapy at first detection of LV dysfunction (§12) to slow progression and prevent complications (arrhythmia, sudden death, decompensated heart failure).
- **Genetic counseling**: Central to management given X-linked inheritance — recurrence-risk counseling for carrier mothers, discussion of variable expressivity/manifesting-carrier risk, and cascade testing of at-risk relatives.
- **No immunization or infectious-prevention component** is relevant, and no population-level public-health/environmental intervention applies, given the monogenic, non-infectious, non-environmentally-triggered etiology.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: Naturally occurring dystrophin-deficient cardiomyopathy is well documented in **dogs** (multiple breeds) and has been modeled in additional species below (NCBI Taxonomy: *Canis lupus familiaris* NCBITaxon:9615; *Mus musculus* NCBITaxon:10090).
- **Golden Retriever Muscular Dystrophy (GRMD)**: A naturally occurring, genetically homologous canine dystrophinopathy model. Cardiac phenotyping shows early ECG changes, elevated heart rate, reduced cardiac chamber size, disproportionately reduced myocardial mass, and — in older dogs — fatty infiltration and vascular hypertrophy correlating with lesion severity (biorxiv 2024, "Early Natural History of Cardiomyopathy and Cardiac Stress Response in Young Dogs with Golden Retriever Muscular Dystrophy"; PMC5438519, "The golden retriever model of Duchenne muscular dystrophy"). GRMD clinical severity (progressive gait impairment, dyspnea, dysphagia, delayed dilated cardiomyopathy) more closely parallels the progressive human DMD course than rodent models do, making it an important translational bridge (PMC5438519).
- **X-linked muscular dystrophy in Labrador Retrievers**: A second, independently characterized canine dystrophinopathy strain with phenotypic and molecular characterization reported (PMC7412789).
- **Comparative biology**: The dystrophin gene and DGC structure are highly conserved across mammals; the canine models in particular recapitulate both the skeletal and cardiac phenotype spectrum, supporting cross-species mechanistic inference for the human cardiac-selective (XLDCM) phenotype specifically, though most canine cardiac-phenotyping work characterizes the "typical" (skeletal + cardiac) dystrophinopathy course rather than an isolated cardiac-only canine analog of XLDCM.
- **Zoonotic potential**: None — this is a non-infectious, inherited, non-transmissible disease; not applicable.

---

## 15. Model Organisms

| Model | Type | Key cardiac-phenotype findings |
|---|---|---|
| **mdx mouse** | Genetic (spontaneous dystrophin-null point mutation) | Standard, most widely used DMD model; shows dilated cardiomyopathy with decreased fractional shortening and impaired fatty-acid metabolism, but **cardiac dysfunction is milder and later-onset than in humans** — young adult mdx mice do not show overt cardiac functional deficits, a recognized model limitation (PMC4348559, "Animal models of Duchenne muscular dystrophy: from basic mechanisms to gene therapy"). **Aged female mdx mice** are noted as a genetically and phenotypically closer match to human dystrophic cardiomyopathy than young male mice. |
| **Cmah−/−;mdx (Cmah-deficient mdx)** | Enhanced genetic model (double knockout) | Accelerated cardiac phenotype vs. standard mdx — earlier reduction in RV ejection fraction/stroke volume (by 12 weeks) and LV diastolic volume/stroke volume deficits (by 24 weeks) (PMID:30281092). |
| **Fiona/dko (dystrophin/utrophin double-knockout background)** | Enhanced genetic model | Severe DMD cardiomyopathy model used to test AAV-μDys5 microdystrophin gene therapy, which fully prevented cardiac pathology and preserved EF >45% through 18 months (PMC8119181, PMC9981810). |
| **Dmdmdx rat** | Genetic (CRISPR-generated dystrophin-null rat) | Proposed as a cardiovascular-phenotyping model potentially better suited than mice for capturing the human-like cardiovascular course (PMC7927653, "Cardiovascular phenotype of the Dmdmdx rat"). |
| **GRMD / Labrador X-linked muscular dystrophy dogs** | Naturally occurring large-animal model | See §14 — closest large-animal phenocopy of human dystrophinopathy cardiomyopathy progression; used for AAV/gene-therapy and membrane-sealant (poloxamer 188) preclinical efficacy testing. |
| **Human iPSC-derived cardiomyocytes (hiPSC-CMs)** | In vitro/cellular model | Emerging platform for mechanistic study and exon-skipping/AAV efficacy testing directly in dystrophin-deficient human cardiomyocytes; exon-51-skipping AOs restored dystrophin to ~30% of wild-type in this system (cited in PMC4491663). |
| **Tafazzin (Taz) knockdown mouse** (Barth syndrome model, distinct X-linked cardiomyopathy gene, included for comparative context) | Genetic knockdown | Recapitulates hypertrophic-cardiomyopathy-like features of Barth syndrome; used in a 2025 study testing whether pharmacological ketone elevation could alleviate the cardiomyopathy — it did **not** alleviate the phenotype, an informative negative preclinical result (PMC12711585). |

### Model limitations (general, relevant to XLDCM translational work)
Standard mouse models substantially under-recapitulate the severity and tempo of human dystrophinopathy cardiomyopathy, necessitating enhanced genetic backgrounds (Cmah-null, dystrophin/utrophin double-knockout) or large-animal (canine) models for therapies intended to translate to the human cardiac phenotype. No model organism was identified in this search that specifically and selectively recapitulates the **"cardiac-only" (skeletal-sparing)** XLDCM phenotype as opposed to the combined skeletal-plus-cardiac phenotype typical of DMD/BMD models — this is a notable translational gap: the isoform-compensation mechanism thought to underlie human XLDCM's tissue selectivity (§6) has not, per this search, been specifically reproduced and validated as a standalone cardiac-selective model.

---

## Key Differential/Related X-linked Cardiomyopathy Genes (Summary Table)

| Gene (locus) | Disorder | Cardiac phenotype | Distinguishing extracardiac features |
|---|---|---|---|
| *DMD* (Xp21.2-p21.1) | XLDCM / dystrophinopathy cardiomyopathy | Dilated CM, ventricular arrhythmia | Skeletal myopathy absent/minimal (XLDCM) to severe (DMD/BMD) |
| *TAZ* (Xq28) | Barth syndrome | DCM ± LV noncompaction, endocardial fibroelastosis, HCM variants; onset typically infancy/first year of life | Skeletal myopathy, neutropenia, growth delay, 3-methylglutaconic aciduria |
| *LAMP2* (Xq24) | Danon disease | Predominantly hypertrophic CM (males); mixed HCM/DCM (females); WPW pattern | Skeletal myopathy, intellectual disability, glycogen accumulation |
| *EMD* (Xq28) | Emery-Dreifuss muscular dystrophy 1 / isolated DCM | Conduction disease progressing to DCM; some variants cause isolated DCM without classic EDMD triad | Joint contractures, humero-peroneal weakness (classic EDMD1); can be absent in isolated-DCM EMD variants |

---

## Notes on Evidence Gaps and Confidence

- The classic "XLDCM" literature is largely composed of **historical pedigree studies** (1987–1990s) supplemented by more recent **mechanistic** (isoform-expression) and **case-report/case-series** work; large modern epidemiological or multi-omic datasets specific to the isolated cardiac phenotype are sparse. Statements about frequency (e.g., "3–13.6% of DCM cohorts") reflect *DMD*-mutation yield in general DCM screening cohorts, not the narrower "pure" XLDCM phenotype specifically, and should be flagged as such in any KB curation.
- MONDO ID mapping for this specific entity was **not confirmed** in this session (OMIM #302045 was located, but a direct MONDO cross-reference lookup was not performed) — verify before use in structured curation.
- The 2025 DMD Heart Protection Study long-term follow-up (PMID:40130400) is a genuinely recent, clinically important update: it tempers earlier assumptions that prophylactic ACE-inhibitor/beta-blocker therapy is unambiguously superior to treatment initiated at first detected dysfunction — this should be represented with appropriate caveats given it is a single (if well-designed) trial with acknowledged methodological limitations.
- The 2024 microdystrophin gene-therapy cardiac-safety signal (PMC11382885 — some constructs *accelerating* cardiac disease via microdystrophin/utrophin membrane competition) is an important, very recent (2024) caveat for the gene-therapy pipeline's cardiac relevance and should not be omitted when discussing gene therapy as a treatment prospect for dystrophinopathy cardiomyopathy generally, including XLDCM.

---

## Sources

- [X-Linked Dilated Cardiomyopathy — Berko & Swift, N Engl J Med 1987;316(19):1186-91](https://www.nejm.org/doi/full/10.1056/NEJM198705073161904) (PMID:3574369)
- [X-linked dilated cardiomyopathy. Molecular genetic evidence of linkage to the Duchenne muscular dystrophy (dystrophin) gene at the Xp21 locus — PubMed](https://pubmed.ncbi.nlm.nih.gov/8504498/) (PMID:8504498)
- [Deletion of the Dystrophin Muscle-Promoter Region Associated with X-Linked Dilated Cardiomyopathy — NEJM 1993](https://www.nejm.org/doi/full/10.1056/NEJM199309233291304) (Muntoni et al., PMID:8361506)
- [The absence of dystrophin brain isoform expression in healthy human heart ventricles explains the pathogenesis of 5' X-linked dilated cardiomyopathy — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3331845/) (PMID:22455600)
- [X-Linked Dilated Cardiomyopathy: A Cardiospecific Phenotype of Dystrophinopathy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4491663/)
- [302045 - CARDIOMYOPATHY, DILATED, 3B; CMD3B — OMIM](https://omim.org/entry/302045)
- [X-linked dilated cardiomyopathy — MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/x-linked-dilated-cardiomyopathy/)
- [De Novo p.Asp3368Gly Variant of Dystrophin Gene Associated with X-Linked Dilated Cardiomyopathy and Skeletal Myopathy — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10931831/)
- [DMD-Associated Dilated Cardiomyopathy: Genotypes, Phenotypes, and Phenocopies — Circulation: Genomic and Precision Medicine](https://www.ahajournals.org/doi/10.1161/CIRCGEN.123.004221)
- [The role of the dystrophin glycoprotein complex in muscle cell mechanotransduction — Communications Biology 2022](https://www.nature.com/articles/s42003-022-03980-y) (PMID:36168044)
- [Dysregulation of Calcium Handling in Duchenne Muscular Dystrophy-Associated Dilated Cardiomyopathy — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7074327/)
- [Cardiac Involvement in Dystrophin-Deficient Females — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7397028/) / [Genes 2020, DOI](https://doi.org/10.3390/genes11070765)
- [Myocardial late gadolinium enhancement is associated with clinical presentation in Duchenne muscular dystrophy carriers — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5034448/)
- [Left ventricular noncompaction cardiomyopathy in Duchenne muscular dystrophy carriers — PubMed](https://pubmed.ncbi.nlm.nih.gov/30546524/)
- [Danon disease: focusing on heart — Journal of Human Genetics 2012](https://www.nature.com/articles/jhg201272)
- [Intrafamilial variability for novel TAZ gene mutation — ScienceDirect / PubMed](https://pubmed.ncbi.nlm.nih.gov/23031367/)
- [Barth syndrome cardiomyopathy: targeting the mitochondria with elamipretide — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7895793/)
- [Long-term efficacy and safety of elamipretide in patients with Barth syndrome: 168-week open-label extension results of TAZPOWER — PubMed](https://pubmed.ncbi.nlm.nih.gov/38602181/)
- [EMD missense variant causes X-linked isolated dilated cardiomyopathy with myocardial emerin deficiency — PMC 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12185710/)
- [Emery-Dreifuss Muscular Dystrophy — GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1436/)
- [310300 - EMERY-DREIFUSS MUSCULAR DYSTROPHY 1 — OMIM](https://omim.org/entry/310300)
- [Dystrophinopathies — GeneReviews](https://www.ncbi.nlm.nih.gov/sites/books/NBK1119/)
- [Cardiac care of children with dystrophinopathy and females carrying DMD-gene variations — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9577913/)
- [Randomised placebo-controlled trial of combination ACE inhibitor and beta-blocker therapy to prevent cardiomyopathy in children with Duchenne muscular dystrophy (DMD Heart Protection Study): protocol — PubMed](https://pubmed.ncbi.nlm.nih.gov/30573480/)
- [Preventing Cardiomyopathy in Duchenne Muscular Dystrophy: Long-Term Follow-Up... Perindopril and Bisoprolol — Eur J Neurol 2025, PubMed](https://pubmed.ncbi.nlm.nih.gov/40130400/)
- [A Randomized, Double-Blind Trial of Lisinopril and Losartan for the Treatment of Cardiomyopathy in Duchenne Muscular Dystrophy — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3871420/)
- [Duchenne Dilated Cardiomyopathy: Cardiac Management from Prevention to Advanced Cardiovascular Therapies — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7600130/)
- [Imaging and Serum Biomarkers for Cardiomyopathy in Duchenne Muscular Dystrophy — Circulation: Heart Failure 2024](https://www.ahajournals.org/doi/10.1161/CIRCHEARTFAILURE.123.010700)
- [Duchenne muscular dystrophy patients: troponin leak in asymptomatic and implications for drug toxicity studies — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8866537/) (PMID:34429516)
- [Sudden cardiac death of Duchenne muscular dystrophy with NT-proBNP in pericardial fluid as a useful biomarker — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7476613/) (PMID:32939432)
- [Characteristics and outcomes of cardiomyopathy in children with Duchenne or Becker muscular dystrophy: Pediatric Cardiomyopathy Registry — PubMed](https://pubmed.ncbi.nlm.nih.gov/18513510/)
- [Heart transplantation in patients with dystrophinopathic cardiomyopathy: Review of the literature and personal series — PubMed](https://pubmed.ncbi.nlm.nih.gov/28580208/)
- [Potential limitations of microdystrophin gene therapy for Duchenne muscular dystrophy — PMC 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11382885/)
- [Micro-dystrophin gene therapy prevents heart failure in an improved Duchenne muscular dystrophy cardiomyopathy mouse model — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119181/)
- [Micro-dystrophin gene therapy demonstrates long-term cardiac efficacy in a severe Duchenne muscular dystrophy model — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9981810/)
- [AAV-microutrophin gene therapy confers durable cardioprotection... in the mdx mouse — ScienceDirect 2025](https://www.sciencedirect.com/science/article/abs/pii/S1525001625005489)
- [Animal models of Duchenne muscular dystrophy: from basic mechanisms to gene therapy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4348559/)
- [Cmah-dystrophin deficient mdx mice display an accelerated cardiac phenotype... — PubMed](https://pubmed.ncbi.nlm.nih.gov/30281092/)
- [Cardiovascular phenotype of the Dmdmdx rat — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7927653/)
- [Early Natural History of Cardiomyopathy and Cardiac Stress Response in Young Dogs with Golden Retriever Muscular Dystrophy — bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.08.19.608721v1.full)
- [The golden retriever model of Duchenne muscular dystrophy — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5438519/)
- [X-linked muscular dystrophy in a Labrador Retriever strain: phenotypic and molecular characterisation — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7412789/)
- [Pharmacological increases in circulating ketones fail to alleviate the hypertrophic cardiomyopathy present in the Tafazzin knockdown mouse model of Barth syndrome — PMC 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12711585/)
- [Epidemiology of non-ischaemic dilated cardiomyopathy — Nature Reviews Cardiology](https://www.nature.com/articles/s41569-026-01300-z)