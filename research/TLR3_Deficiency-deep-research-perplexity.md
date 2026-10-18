---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-03T13:57:11.984188'
end_time: '2026-09-03T14:01:05.018470'
duration_seconds: 233.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TLR3 Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TLR3 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TLR3 Deficiency** covering all of the
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

# TLR3 Deficiency (Immunodeficiency 83, Susceptibility to Viral Infections)

TLR3 deficiency is a rare inborn error of innate immunity caused by germline loss-of-function variants in the **TLR3** gene, resulting in impaired recognition of double-stranded RNA (dsRNA) and defective induction of type I and type III interferon responses in specific cell types, most notably within the central nervous system (CNS) and respiratory epithelium.[3][8][2][6] Clinically, this disorder manifests as a selective predisposition to severe viral infections in otherwise healthy individuals, classically childhood herpes simplex virus type 1 (HSV-1) encephalitis and, more recently, life-threatening influenza A-associated acute respiratory distress syndrome (ARDS), with relatively preserved resistance to most other pathogens.[4][2][13][14][16] Human genetic studies encompassing autosomal dominant and autosomal recessive forms of TLR3 deficiency, together with deficiencies in other components of the TLR3 pathway such as UNC93B1, TRIF, TRAF3, TBK1, and IRF3, have established that **TLR3-mediated, cell-intrinsic type I/III interferon immunity in neurons and pulmonary epithelial cells is nonredundant for protection against specific neurotropic and respiratory viruses, even though TLR3 is largely redundant for systemic antiviral defense.**[4][6][16][17] This report synthesizes current knowledge on disease definitions, etiology, phenotypic spectrum, mechanism, anatomy, temporality, genetics, diagnostics, prognosis, treatment, prevention, and model organisms for TLR3 deficiency, annotated with relevant ontology terms and primary literature evidence, to support construction of a structured disease knowledge base entry.

---

## 1. Disease Information

### 1.1 Definition and Concise Overview

TLR3 deficiency is a Mendelian primary immunodeficiency defined by germline defects in the **TLR3** gene that impair Toll-like receptor 3 signaling, leading to inadequate induction of interferon-α/β and interferon-λ in response to dsRNA and dsRNA-producing viruses in specific tissues.[1][3][8] The Online Mendelian Inheritance in Man (OMIM) entry 613002 designates this condition as **“Immunodeficiency 83, susceptibility to viral infections”**, mapping it to chromosome 4q35.1 and noting both autosomal dominant and autosomal recessive inheritance.[1][8] TLR3 encodes an endosomal transmembrane receptor that recognizes dsRNA and activates signaling cascades culminating in innate antiviral immunity, particularly inducing type I and type III interferons and inflammatory cytokines such as IL-6.[3][8] At the clinical level, the most distinctive and well-established phenotype is childhood HSV-1 encephalitis in otherwise healthy children, often as the only severe infectious episode, thereby exemplifying a **pathogen-specific and tissue-specific primary immunodeficiency**.[4][2][6][16]

The hallmark conceptual advance from the initial discovery of human TLR3 deficiency was the recognition that, contrary to earlier assumptions based largely on murine models, human TLR3 is not globally required for antiviral defense but is vital for natural immunity to HSV-1 in the CNS and, in some patients, influenza A virus in the lung.[4][2][13][14][16] Casanova and colleagues reported that a dominant-negative TLR3 allele was present in children with isolated HSV-1 encephalitis and concluded that “**Human TLR3 appears to be redundant in host defense to most microbes but is vital for natural immunity to HSV-1 in the CNS, which suggests that neurotropic viruses have contributed to the evolutionary maintenance of TLR3.**”[4] Similarly, subsequent work on complete autosomal recessive TLR3 deficiency revealed that affected individuals, despite experiencing childhood HSV-1 encephalitis, remained otherwise normally resistant to infections, underscoring the striking clinical selectivity of this immunodeficiency.[2][6]

In ontology terms, TLR3 deficiency aligns with **MONDO:0024563** for “herpes simplex encephalitis, susceptibility to, 1 (IIAE1)” as referenced in ClinVar, and with the broader OMIM phenotype 613002 “Immunodeficiency 83, susceptibility to viral infections” for TLR3-related primary immunodeficiency.[11][1][8] It belongs to the Human Phenotype Ontology (HPO) category of **“Recurrent viral infections” (HP:0004429)** and more specifically **“Herpes simplex encephalitis” (HP:0006802)**, as well as to the International Union of Immunological Societies (IUIS) primary immunodeficiency classification under inborn errors of immunity affecting intrinsic and innate immunity.[18][16] The disease information is derived primarily from aggregated disease-level resources, including OMIM, ClinVar, and IUIS classifications, as well as detailed case-series and mechanistic studies in the clinical literature, rather than from large-scale EHR-based observational datasets.[1][4][2][6][13][14][16]

### 1.2 Key Identifiers and Coding Systems

The principal genetic and disease identifiers for TLR3 deficiency include several OMIM and related entries. The **TLR3 gene** itself is cataloged under OMIM number 603029, cytogenetic location 4q35.1, and is associated with multiple phenotypes including “HIV-1 infection, resistance to” (OMIM 609423) and “Immunodeficiency 83, susceptibility to viral infections” (OMIM 613002).[3][8] The phenotype “Herpes simplex encephalitis, susceptibility to, 1” is separately designated in OMIM as 610551 and is linked to TLR3 variants as one genetic etiology.[11][4][16] ClinVar records specific pathogenic TLR3 variants such as NM_003265.3:c.2455C>A (p.His819Asn), annotated with the condition “Herpes simplex encephalitis, susceptibility to, 1 (IIAE1)”, with MONDO:0024563 and Orphanet:1930 identifiers.[11]

Orphanet lists “Herpes simplex encephalitis” as a rare disease entity (Orphanet 1930) and recognizes genetic susceptibility forms mediated by TLR3 pathway defects, though detailed Orphanet annotations for “Immunodeficiency 83” per se remain limited compared with OMIM.[11][16] ICD-10 and ICD-11 do not provide specific codes for TLR3 deficiency; rather, clinical cases are coded under broader categories such as “B00.4 Herpesviral encephalitis” for HSV-1 encephalitis and “J10–J11 Influenza due to identified influenza virus” for influenza-associated pneumonitis, with additional codes for ARDS (e.g., “J80 Acute respiratory distress syndrome”), but without a unique ICD code for the underlying inborn error of immunity. The MeSH vocabulary includes **“Toll-Like Receptors” (D050597)** and “Encephalitis, Herpes Simplex” (D004672), which are relevant conceptual descriptors.

In the MONDO ontology, TLR3 deficiency as a primary immunodeficiency is best captured by “Immunodeficiency 83, susceptibility to viral infections” as a Mendelian disease entity, linked to the **TLR3 (HGNC:11850)** gene, and by associated pathogen-specific susceptibility terms such as MONDO:0024563 for HSV encephalitis susceptibility.[11][1][8] For the purposes of a knowledge base, core identifiers would thus include OMIM 613002, OMIM 603029, OMIM 610551, MONDO:0024563, Orphanet 1930, HGNC:11850, and NCBI Gene ID 7098.[3][8][11]

### 1.3 Synonyms and Alternative Names

TLR3 deficiency has accumulated several synonyms reflecting different emphases on its immunologic, genetic, or clinical aspects. OMIM and IUIS refer to it as **“Immunodeficiency 83, susceptibility to viral infections”**, which captures the broader viral susceptibility phenotype and its classification among primary immunodeficiency diseases.[1][18] A more clinically focused synonym is **“Herpes simplex encephalitis, susceptibility to, 1 (IIAE1)”**, which is used particularly when TLR3 variants are discussed in the context of isolated HSV-1 encephalitis.[11][4] Additional descriptive phrases appearing in the literature include “autosomal dominant TLR3 deficiency”, “autosomal recessive complete TLR3 deficiency”, and “inherited TLR3 deficiency underlying severe influenza pneumonitis”, reflecting distinct genetic modes and phenotypic presentations.[2][6][13][14]

Nature Reviews Immunology summarized the initial discovery under the title **“TLR3: rising above redundancy”**, referring to the specific condition as “TLR3 deficiency in two children with HSV-1 encephalitis” and emphasizing that autosomal dominant TLR3 deficiency represents “the second genetic aetiology of isolated HSE” after UNC93B1 deficiency.[15][17] ClinVar records commonly used clinical condition synonyms such as “ENCEPHALOPATHY, ACUTE, INFECTION-INDUCED (HERPES-SPECIFIC), SUSCEPTIBILITY TO, 1”, which correspond to the same underlying entity.[11]

For ontology mapping, suggested synonyms include: “TLR3-associated primary immunodeficiency”, “inborn error of TLR3-mediated innate immunity”, “TLR3-related herpes simplex encephalitis susceptibility”, and “TLR3-related influenza ARDS susceptibility”. These variants support interoperability across resources that emphasize pathogen-specific, organ-specific, or gene-centric views of the disease.

### 1.4 Nature of Available Information

The existing knowledge base for TLR3 deficiency is derived predominantly from aggregated disease-level resources and mechanistic case-based studies rather than from large EHR-based epidemiological cohorts. OMIM provides curated summaries of genetic, clinical, and mechanistic data, drawing on key primary publications.[1][8] IUIS classifications similarly aggregate gene-defect information at the disease level.[18] ClinVar and LOVD list individual variants identified in patients, with varying degrees of clinical interpretation, but remain limited in terms of large-scale genotype–phenotype correlations for this rare condition.[10][11][12]

Primary clinical information stems from relatively small numbers of patients described in the literature, often in depth, with functional assays demonstrating cellular immune defects. For example, the Science article describing autosomal dominant TLR3 deficiency in HSV-1 encephalitis presented detailed immunological characterization of heterozygous fibroblasts and leukocytes.[4] Subsequent work on autosomal recessive complete TLR3 deficiency similarly used patient-derived fibroblasts to prove absent TLR3 signaling and high HSV-1 replication.[2][6] The influenza ARDS series involved three unrelated children heterozygous for rare TLR3 variants, with extensive functional validation of the mutations as loss-of-function and demonstration of impaired pulmonary epithelial cell-intrinsic interferon responses.[13][14] These studies rely on case reports and case series, rather than population-based registries.

Consequently, much of the information is high-quality, mechanistically rich, but limited in sample size and susceptible to ascertainment bias. For the knowledge base, it is essential to represent that current understanding is based on careful aggregation of rare, deeply studied clinical cases and experimental evidence, and not on broad epidemiological surveillance.

---

## 2. Etiology

### 2.1 Disease Causal Factors

TLR3 deficiency is fundamentally a **genetic** disease caused by germline variants in the **TLR3** gene that result in partial or complete loss of function of the TLR3 protein.[1][3][4][2][6] TLR3 is a pattern recognition receptor belonging to the Toll-like receptor family, expressed in endosomal compartments of various cell types including fibroblasts, neurons, epithelial cells, and dendritic cells.[3][8] It recognizes dsRNA associated with viral infection and induces activation of NF-κB and interferon-regulatory factors, driving production of type I interferons (IFN-α/β) and type III interferons (IFN-λ), as well as inflammatory cytokines.[3][8][16] Pathogenic TLR3 variants therefore disrupt dsRNA sensing and downstream signaling, leading to impaired cell-intrinsic antiviral immunity in specific tissues.

The earliest described causal variants were **dominant-negative missense mutations** in TLR3 (such as P533S), which resulted in autosomal dominant TLR3 deficiency in otherwise healthy children with HSV-1 encephalitis.[4][15] The Science report noted: “We report a dominant-negative TLR3 allele in otherwise healthy children with herpes simplex virus 1 (HSV-1) encephalitis. TLR3 is expressed in the central nervous system (CNS), where it is required to control HSV-1, which spreads from the epithelium to the CNS via cranial nerves.”[4] Subsequent work identified an autosomal recessive form of complete TLR3 deficiency in a young man with childhood HSV-1 encephalitis, in whom compound heterozygosity for two loss-of-function alleles abolished TLR3 signaling.[2][6] This established that both autosomal dominant partial deficiency and autosomal recessive complete deficiency can cause the clinical phenotype.

Beyond TLR3 itself, mutations in multiple genes of the TLR3 signaling pathway have been identified as causal factors in HSV-1 encephalitis, including UNC93B1, TRIF (TICAM1), TRAF3, TBK1, and IRF3.[16][17] A comprehensive review summarized that “Mutations of five genes of the Toll-like receptor 3 (TLR3) signaling pathway have been identified in children with HSE: TLR3, UNC93B1, TRIF, and, more surprisingly, TRAF3 and TBK1, which encode downstream, nonspecific components of the pathway. These mutations impair CNS-intrinsic interferon (IFN)-α/β production in response to HSV-1.”[16] Although this report focuses on TLR3 deficiency per se, these pathway defects highlight that the etiologic concept extends to a broader **“TLR3–IFN axis deficiency”** for HSV-1 and influenza susceptibility.

Environmental and infectious factors play a critical role as **triggers** of disease manifestations but are not primary causes of the underlying susceptibility. HSV-1 infection is required for development of HSV-1 encephalitis; influenza A virus infection is required for influenza ARDS. However, these infections occur commonly in the general population, and only individuals with TLR3 or related pathway defects develop severe disease in the absence of other predisposing factors.[4][2][13][14][16] Thus, the etiologic architecture is best conceptualized as **Mendelian genetic susceptibility to specific viral infections**, rather than direct viral causation or environmental pathology.

Mechanistically, TLR3 deficiency causes disease by impairing **cell-intrinsic interferon responses** to viral dsRNA in neurons and epithelial cells, leading to uncontrolled viral replication and tissue injury in the CNS and lung.[2][4][6][13][14][16] These defects occur despite intact adaptive immunity and preserved responses via other pattern recognition receptors in leukocytes, explaining the narrow clinical spectrum and relative sparing of systemic infections.[4][6][16] The disease is therefore a paradigmatic example of a **nonredundant innate immune receptor** whose functional loss has dramatic consequences in specific tissues but minimal systemic impact.

### 2.2 Genetic Risk Factors

The principal genetic risk factors for TLR3 deficiency are **rare, high-penetrance germline variants in TLR3 and interacting pathway genes**. For TLR3 itself, both missense and truncating variants have been implicated. Autosomal dominant TLR3 deficiency is typically associated with heterozygous missense mutations that act as loss-of-function or dominant-negative alleles, such as the P533S mutation initially described in children with HSV-1 encephalitis.[4][15] Casanova’s group demonstrated that heterozygosity for P533S was causally related to impaired TLR3 signaling, weakened interferon production, enhanced viral replication, and increased fibroblast cell death upon HSV-1 infection.[15] 

ClinVar lists NM_003265.3:c.2455C>A (p.His819Asn) in TLR3 as a pathogenic or likely pathogenic variant for “Herpes simplex encephalitis, susceptibility to, 1 (IIAE1)”, with evidence supporting its role as a germline missense variant altering TLR3 protein structure.[11] Additional heterozygous missense variants (P554S and P680L) have been identified in three unrelated children with severe influenza A virus–associated ARDS, where functional studies confirmed autosomal dominant TLR3 deficiency with impaired responses to poly(I:C) and viral infection.[13][14] The influenza study noted: “Two heterozygous missense LOF mutations were found to underlie AD TLR3 deficiency in three unrelated children with IAV-ARDS.”[14]

Autosomal recessive TLR3 deficiency has been described in at least one patient who was compound heterozygous for two loss-of-function alleles. In that case, complete absence of TLR3 responses in fibroblasts led to profoundly impaired IFN-β and IFN-λ production and high HSV-1 replication.[2][6] The PubMed report summarized: “This patient is compound heterozygous for two loss-of-function TLR3 alleles, resulting in an absence of response to TLR3 activation by poly(I:C) and related agonists in his fibroblasts.”[6] These data underscore that both heterozygous and biallelic TLR3 variants can confer strong genetic risk.

Variants of uncertain significance (VUS) in TLR3 have also been cataloged in ClinVar; for example, NM_003265.3:c.441G>A (p.Lys147=) is a synonymous variant at the last nucleotide of exon 2, not present in population databases and predicted not to disrupt splicing, currently classified as VUS for HSV-1 encephalitis susceptibility.[12] Such variants illustrate that not all rare TLR3 alleles are clearly pathogenic and that functional validation is essential.

Beyond TLR3, rare variants in UNC93B1, TRIF, TRAF3, TBK1, and IRF3 constitute genetic risk factors for clinically similar phenotypes, though these are technically distinct disorders.[16][17] For example, UNC93B1 deficiency impairs trafficking of nucleic acid–sensing TLRs, including TLR3, and has been associated with HSV-1 encephalitis.[17][16] IRF3 haploinsufficiency can cause a broader antiviral interferon induction defect affecting TLR3 and other pathways, underlying childhood HSE.[16] In the context of a TLR3 deficiency knowledge base entry, these gene defects can be recorded as **modifier or pathway genes** contributing to overlapping susceptibility profiles.

### 2.3 Environmental and Lifestyle Risk Factors

Environmental and lifestyle factors do not directly cause TLR3 deficiency but can influence infection risk and severity. Age is a critical factor: HSV-1 encephalitis due to TLR3 deficiency typically presents in **childhood**, often between 3 months and 15 years, reflecting developmental windows of vulnerability when CNS-intrinsic innate immunity has heightened importance.[4][2][6][16] Influenza ARDS associated with TLR3 deficiency likewise occurs in children, generally during acute influenza seasons.[13][14] These age-related patterns suggest that young brain and lung tissues may rely more heavily on TLR3-mediated immunity than adult tissues.

Sex does not appear to be a strong risk factor; reported cases include both male and female patients, without clear sex bias.[4][2][6][13][14][16] Family history of HSV-1 encephalitis or severe influenza may point to inherited susceptibility, particularly in autosomal dominant cases, but de novo mutations have also been described. There is no evidence that lifestyle factors such as smoking, diet, or exercise directly modify penetrance or severity in TLR3 deficiency, although smoking and air pollution may exacerbate influenza-related ARDS in general populations.

Occupational exposures are irrelevant for the childhood presentations typical of TLR3 deficiency. Geographic location may influence exposure to influenza strains and HSV-1 seroprevalence, but TLR3 deficiency cases have been reported from diverse countries, indicating no obvious endemic concentration.[4][6][13][14][16] Overall, environmental risk factors are **secondary**, primarily modulating infection risk (timing and strain) rather than susceptibility per se.

### 2.4 Protective Factors

Protective factors in TLR3 deficiency can be conceptualized at both genetic and environmental levels, although formal evidence remains limited. Genetically, **intact function of other pathogen recognition receptors and interferon pathways** appears to largely compensate for the absence or impairment of TLR3 in leukocytes and many epithelial cells, thereby protecting patients against the majority of viral infections.[4][2][6][16] Human TLR3 is redundant for responses to dsRNA and HSV-1 in various leukocytes, as summarized by the autosomal recessive TLR3 deficiency study: “They also indicate that human TLR3 is largely redundant for responses to double-stranded RNA and HSV-1 in various leukocytes, probably accounting for the redundancy of TLR3 for host defense against viruses, including HSV-1, outside the CNS.”[6]

Protective genetic variants that mitigate TLR3 deficiency have not been systematically described, but polymorphisms in other antiviral genes such as IFIH1 (MDA5), DDX58 (RIG-I), or cGAS–STING pathway components could, in principle, enhance non-TLR3 dsRNA or DNA sensing and confer partial protection. This remains speculative, as no explicit modifier alleles have been documented in patient cohorts.

Environmentally, **routine childhood vaccination** against other viral pathogens (e.g., measles, mumps, rubella, varicella, influenza) reduces infection burden and indirectly protects TLR3-deficient individuals from multifactorial viral insults, although HSV-1 and most seasonal influenza strains are not eliminated by current vaccines.[13][14] For influenza, annual vaccination may lower the probability of infection and thus ARDS risk, but it does not address the underlying innate immune defect. Avoidance of household transmissible infections during outbreak periods, early treatment of influenza with antiviral drugs, and rapid supportive care in ARDS may function as protective factors in a broad sense.

In sum, protective factors for TLR3 deficiency are mostly **non-specific**, based on redundancy in innate immune sensing, existence of intact adaptive immunity, and public health measures that reduce exposure to severe viral infections.

### 2.5 Gene–Environment Interactions

TLR3 deficiency exemplifies gene–environment interactions in which **common environmental exposures (viral infections) have rare but severe consequences in genetically susceptible hosts**. HSV-1 infection is ubiquitous; most individuals acquire HSV-1 in childhood and remain asymptomatic or have mild mucocutaneous disease. In TLR3-deficient children, however, primary HSV-1 infection can lead to encephalitis, because their CNS neurons and glial cells lack effective TLR3-mediated interferon responses to dsRNA intermediates of HSV-1 replication.[4][2][6][16] The Science article emphasized that TLR3 is expressed in the CNS where it is required to control HSV-1, which spreads from the epithelium to the CNS via cranial nerves.[4] Thus, the same environmental exposure (HSV-1 infection) causes dramatically different outcomes depending on TLR3 genotype.

Influenza A virus infection likewise interacts with TLR3 deficiency. In the influenza ARDS study, three children heterozygous for TLR3 loss-of-function variants developed life-threatening ARDS upon infection with IAV, whereas their relatives and community contacts infected with the same virus had milder disease.[13][14] The authors concluded that autosomal dominant TLR3 deficiency may underlie IAV-ARDS by impairing TLR3-dependent type I/III IFN-mediated pulmonary epithelial cell-intrinsic immunity.[13][14] Here, environmental exposure (seasonal influenza) interacts with a monogenic susceptibility to produce severe lung injury.

These interactions are **not additive risk factors but conditional triggers**, in which infection is necessary but not sufficient for disease; TLR3 deficiency is necessary but not sufficient, as many TLR3-deficient individuals may never encounter the specific viral load or timing to precipitate encephalitis or ARDS. The penetrance of TLR3 deficiency is therefore age-dependent and infection-dependent, with **stochastic gene–environment interactions** determining clinical manifestations.

For ontology annotation, gene–environment interaction concepts can be mapped to **GO:0006955 (immune response)** and **MONDO terms for “infectious disease susceptibility”**, while environmental exposures are classified through NCBI Taxonomy for HSV-1 and influenza A virus.

---

## 3. Phenotypes

### 3.1 Overview of Phenotypic Spectrum

The phenotypic spectrum of TLR3 deficiency is characterized by **severe, organ-specific viral infections in otherwise healthy individuals, with minimal baseline immunologic abnormalities**.[4][2][6][13][14][16] The cardinal clinical phenotype is **herpes simplex virus type 1 encephalitis (HSV-1 HSE)** in childhood, which is often the presenting and sometimes the only severe illness in autosomal dominant or recessive TLR3-deficient patients.[4][2][6][16] More recently, **severe influenza A virus pneumonitis, manifesting as acute respiratory distress syndrome (ARDS)**, has been recognized as another major phenotype associated with autosomal dominant TLR3 deficiency.[13][14] These conditions represent **symptomatic phenotypes** (fever, seizures, respiratory distress) arising from underlying **signs** (neurological deficits, hypoxemia), as well as **laboratory abnormalities** (elevated inflammatory markers, CSF pleocytosis, imaging findings).

In contrast to many primary immunodeficiencies, TLR3 deficiency does not cause chronic or recurrent bacterial infections, opportunistic infections, or generalized immunodeficiency. Most patients have normal growth, development, and health outside episodes of encephalitis or ARDS.[4][2][6][13][14][16] Quality of life impact is therefore highly variable: some patients recover fully from acute episodes, while others develop long-term neurological deficits or respiratory complications that significantly impair daily functioning.

### 3.2 Herpes Simplex Virus Type 1 Encephalitis

HSV-1 encephalitis is the most thoroughly studied phenotype of TLR3 deficiency. Clinically, HSV-1 HSE presents with **acute onset of fever, headache, altered mental status, focal neurological deficits, seizures, and sometimes coma**, typically in children without other health problems.[4][2][6][16] It is a **symptom and sign phenotype**, captured by HPO terms such as **“Encephalitis” (HP:0006846)**, **“Seizures” (HP:0001250)**, **“Fever” (HP:0001945)**, **“Altered consciousness” (HP:0001658)**, and **“Focal neurologic deficits” (HP:0002190)**. Laboratory abnormalities include **CSF pleocytosis**, elevated protein, and detection of HSV-1 DNA by PCR; imaging shows **temporal lobe involvement** with hyperintensities on MRI (HP:0007062 “Abnormal brain MRI”) and often **brain edema**.

Age of onset for HSV-1 encephalitis in TLR3-deficient patients is **childhood**, with reported cases from infancy to adolescence, though classic sporadic HSE also occurs in adults.[4][2][6][16] Symptom severity is typically **severe**, as HSE is a life-threatening emergency. Symptom progression is **acute**, with rapid deterioration over days. Frequency within TLR3-deficient individuals appears high, though exact percentages are unknown due to small sample sizes. In autosomal dominant TLR3 deficiency families, penetrance for HSE is incomplete; some heterozygous carriers remain asymptomatic, suggesting that viral exposure timing and other factors influence clinical expression.[4][16]

Quality of life impact of HSV-1 encephalitis is substantial. Survivors may experience long-term neurological sequelae, including cognitive impairment, motor deficits, epilepsy, and behavioral changes, captured by HPO terms such as **“Intellectual disability” (HP:0001249)**, **“Motor impairment” (HP:0001270)**, and **“Behavioral abnormality” (HP:0000708)**. These deficits can affect schooling, employment, and social interactions, leading to reduced scores on SF-36 and other quality-of-life measures, although specific TLR3-deficiency cohorts have not systematically reported such metrics.

Mechanistically, the phenotype is caused by impaired TLR3-mediated interferon responses in CNS cells. The Science article noted: “TLR3 is expressed in the central nervous system (CNS), where it is required to control HSV-1, which spreads from the epithelium to the CNS via cranial nerves.”[4] The autosomal recessive deficiency study further demonstrated that patient fibroblasts had absent IFN-β and IFN-λ production upon HSV-1 infection, resulting in high viral replication and cell death.[6] Suggested GO terms include **GO:0034340 (response to type I interferon)** and **GO:0006955 (immune response)**; CL terms include **CL:0000127 (neuron)** and **CL:0000124 (astrocyte)**; UBERON terms include **UBERON:0000955 (brain)**, **UBERON:0001950 (cerebral cortex)**, and **UBERON:0001871 (temporal lobe)**.

### 3.3 Severe Influenza A Virus Pneumonitis and ARDS

A second major phenotype is **severe influenza A virus pneumonitis manifesting as acute respiratory distress syndrome (IAV-ARDS)** in children with autosomal dominant TLR3 deficiency.[13][14] Clinically, affected patients present with **fever, cough, dyspnea, hypoxemia, and respiratory failure**, requiring mechanical ventilation and intensive care. Radiologically, they show **diffuse bilateral pulmonary infiltrates**, decreased lung compliance, and gas exchange abnormalities consistent with ARDS.[13][14][19] HPO terms include **“Acute respiratory distress syndrome” (HP:0033677)**, **“Hypoxemia” (HP:0012418)**, **“Respiratory failure” (HP:0002878)**, and **“Diffuse pulmonary infiltrates” (HP:0011953)**.

The influenza ARDS study described three unrelated children with IAV infection presenting as ARDS, heterozygous for rare TLR3 variants (P554S in two patients and P680L in the third) causing autosomal dominant TLR3 deficiency.[13][14] They wrote: “This study identifies AD TLR3 deficiency as a novel human genetic etiology of life-threatening childhood pulmonary influenza. Two heterozygous missense LOF mutations were found to underlie AD TLR3 deficiency in three unrelated children with IAV-ARDS.”[14] Age of onset was childhood, typically during seasonal influenza outbreaks. Symptom severity was **life-threatening**, progression was **acute**, and disease course was **episodic**, centered on the acute infection period.

Quality of life impact varies with recovery. Some children may regain normal lung function, while others could develop chronic lung disease, reduced exercise tolerance, or psychosocial effects from intensive care experiences. Long-term outcomes have not been extensively documented, but ARDS survivorship generally involves substantial risk of persistent physical and cognitive impairments.[19] Suggested UBERON terms include **UBERON:0002048 (lung)** and **UBERON:0002406 (respiratory system)**; CL terms include **CL:0002062 (type II pneumocyte)** and **CL:0002063 (type I pneumocyte)**; GO terms include **GO:0034341 (response to interferon-γ)**, **GO:0006955 (immune response)**, and **GO:0006954 (inflammatory response)**.

### 3.4 Other Viral Susceptibility Phenotypes

OMIM notes that TLR3 is implicated in host defense against multiple viruses, including potential roles in resistance to HIV-1 infection.[8] However, in TLR3-deficient patients, **clinical susceptibility to viral infections outside the CNS and lung appears minimal**, with no consistent pattern of recurrent viral illnesses or opportunistic infections.[2][4][6][16] The autosomal recessive deficiency report stated: “This patient…developed HSE in childhood but remained normally resistant to other infections.”[6] Similarly, autosomal dominant TLR3-deficient children with HSV-1 encephalitis did not show increased susceptibility to other pathogens.[4] The influenza ARDS cohort did not reveal broader immunodeficiency either.[13][14]

Some reports have explored associations between common TLR3 polymorphisms and hepatitis B or C infections, HIV susceptibility, or other viral outcomes in population studies, but these involve **low-risk variants** with modest effect sizes and are distinct from the rare, highly penetrant mutations that define TLR3 deficiency as a primary immunodeficiency.[5][8] For the knowledge base, the core phenotype is thus **pathogen-specific severe disease (HSV-1 HSE and IAV-ARDS)** rather than generalized viral susceptibility.

### 3.5 Laboratory Abnormalities

Laboratory abnormalities in TLR3 deficiency are primarily **functional immunologic defects**, rather than baseline hematologic or biochemical abnormalities. Routine blood counts, immunoglobulin levels, and lymphocyte subsets are typically normal.[4][2][6][13][14][16] Specialized assays reveal impaired responses to TLR3 ligands in patient-derived cells. For example, fibroblasts from autosomal recessive TLR3-deficient patients fail to produce IFN-β and IFN-λ when stimulated with poly(I:C) or infected with HSV-1, and show increased viral replication and cell death.[2][6] This corresponds to the laboratory phenotype **“Decreased interferon-β secretion”** and **“Decreased interferon-λ secretion”**, which could be captured by HPO extensions or GO process annotations.

In autosomal dominant TLR3 deficiency, fibroblasts and other cell types exhibit **impaired but not abolished induction of IFN-β and -λ** upon TLR3 stimulation.[2][6] The PubMed abstract noted: “This defect is partial, as it results in impaired, but not abolished induction of IFN-β and -λ in fibroblasts in response to TLR3 stimulation.”[6] These laboratory findings are crucial for diagnosis and mechanistic understanding but are not routinely measured in clinical practice.

In influenza ARDS patients with TLR3 deficiency, pulmonary epithelial cells (PECs) show defective type I/III IFN-mediated intrinsic immunity to IAV, as evidenced by reduced IFN responses and increased viral replication in vitro.[13][14] These can be annotated with GO terms such as **GO:0034340 (response to type I interferon)** and **GO:0019221 (cytokine-mediated signaling pathway)**.

### 3.6 Quality of Life Impact

Quality of life impact in TLR3 deficiency is **episodic and organ-specific**, reflecting the consequences of acute CNS or lung injury. Children with HSV-1 encephalitis may experience prolonged hospitalizations, rehabilitation, and long-term neurocognitive impairments affecting schooling, social integration, and independence. Domains affected include physical functioning, cognitive function, emotional well-being, and social participation, as measured by tools like SF-36 or PROMIS, though disease-specific data are sparse. Similarly, children with influenza ARDS may suffer from persistent fatigue, dyspnea, anxiety, and post-intensive care syndrome, impacting their HRQoL.

At baseline, between episodes, many TLR3-deficient individuals lead normal lives without chronic symptoms, reflecting the **selective** nature of their immunodeficiency.[4][2][6][13][14][16] Thus, quality of life is highly heterogeneous, depending on severity and recovery from acute episodes. From a knowledge base perspective, this underscores the importance of capturing **episodic severe morbidity with possible long-term sequelae**, rather than chronic disease burden.

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: TLR3

The **TLR3** gene (toll-like receptor 3) is the central causal gene in TLR3 deficiency. It is located on chromosome 4q35.1, as confirmed by OMIM and NCBI Gene, and encodes an endosomal transmembrane receptor in the Toll-like receptor family.[3][8][1] TLR3 is a type I transmembrane protein with a large extracellular ectodomain containing leucine-rich repeats (LRRs) that bind dsRNA, a single transmembrane segment, and a cytoplasmic Toll/IL-1 receptor (TIR) domain that interacts with adaptor proteins to initiate signaling.[3][8] The NCBI Gene entry notes: “The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. It recognizes dsRNA associated with viral infection, and induces the activation of NF-kappaB and the production of type I interferons.”[3]

TLR3 belongs to a conserved family of TLRs from Drosophila to humans, with structural and functional similarities.[3][5][8] Human TLR3 is expressed in various tissues, including brain, epithelial surfaces, and immune cells, but its nonredundant function is particularly evident in CNS and lung innate immunity to HSV-1 and IAV.[4][2][6][13][14][16] The gene has HGNC ID 11850 and Entrez Gene ID 7098.[3][10] OMIM associates TLR3 with phenotypes such as HIV-1 infection resistance, immunodeficiency 83, and HSV-1 encephalitis susceptibility.[8][1][11]

### 4.2 Pathogenic Variants: Types, Classification, and Consequences

Pathogenic variants in TLR3 associated with deficiency include **missense, nonsense, frameshift, and splice-site mutations**, mostly affecting conserved residues in the ectodomain or TIR domain, resulting in loss-of-function or dominant-negative effects.[4][2][6][13][14][11] Variant classification follows ACMG/AMP guidelines, with many disease-associated variants designated pathogenic or likely pathogenic in ClinVar and OMIM, while others remain VUS.[11][12]

Autosomal dominant TLR3 deficiency is typically caused by **heterozygous missense variants** that impair TLR3 signaling without fully abolishing protein expression. The P533S missense mutation, located in the ectodomain, was characterized as dominant-negative; fibroblasts from heterozygous patients showed defective responses to poly(I:C) and increased HSV-1 replication.[4][15] Nature Reviews Immunology summarized: “There was a causal relationship between heterozygosity for the P533S TLR3 mutation and impaired TLR3 signalling, abnormally weak IFN production, enhanced viral replication and higher levels of fibroblast cell death upon viral infection.”[15] The influenza ARDS study described P554S and P680L missense variants as **loss-of-function** alleles, causing autosomal dominant TLR3 deficiency.[13][14] These variants are classified as pathogenic or likely pathogenic based on functional assays and segregation.

Autosomal recessive TLR3 deficiency involves **biallelic loss-of-function variants**, often nonsense or frameshift mutations that truncate the protein or disrupt key domains. In the reported case, compound heterozygosity for two LOF alleles abolished TLR3 responses in fibroblasts, with complete absence of IFN production upon poly(I:C) stimulation.[2][6] These alleles are clearly pathogenic and confer complete deficiency.

ClinVar example NM_003265.3:c.2455C>A (p.His819Asn) is a missense variant near the C-terminal region, associated with HSV-1 encephalitis susceptibility.[11] Functional data suggest it disrupts TLR3 signaling. In contrast, NM_003265.3:c.441G>A (p.Lys147=) is a synonymous variant affecting the last nucleotide of exon 2; while such variants can impair splicing, in silico predictions indicate no significant effect, and population data show absence in gnomAD, leading to its classification as VUS.[12] The ClinVar comment states: “Algorithms developed to predict the effect of sequence changes on RNA splicing suggest that this variant is not likely to affect RNA splicing. In summary, the available evidence is currently insufficient to determine the role of this variant in disease.”[12]

Allele frequencies of pathogenic TLR3 variants are generally **extremely low or absent** in population databases such as gnomAD, consistent with their rarity and high penetrance.[12][13][14] This supports their designation as Mendelian disease-causing mutations rather than common susceptibility polymorphisms. All documented disease-causing TLR3 variants are **germline** rather than somatic; there is no evidence that somatic mutations in TLR3 drive cancer or other acquired disorders in humans, although TLR3 signaling may be altered in tumors by other mechanisms.

Functionally, pathogenic variants cause **loss-of-function** of TLR3 signaling, sometimes with dominant-negative effects in heterozygous states. Loss-of-function leads to decreased binding to dsRNA, impaired interaction with the adaptor TRIF, disrupted downstream activation of TBK1, IRF3, and NF-κB, and reduced interferon and cytokine production.[4][2][6][13][14][16] Dominant-negative variants may interfere with normal TLR3 molecules via oligomerization or misfolding, further reducing signaling capacity.

### 4.3 Modifier Genes and Pathway Components

Several genes modulate the clinical expression of TLR3 deficiency by participating in the same signaling pathway. UNC93B1 encodes an endoplasmic reticulum protein that transports nucleic acid–sensing TLRs, including TLR3, from the ER to endosomes.[17][16] Mutations in UNC93B1 cause human UNC-93B deficiency, leading to impaired surface localization of TLR3 and susceptibility to HSV-1 encephalitis.[17] The Science paper highlighted this connection under the title “Herpes Simplex Virus Encephalitis in Human UNC-93B Deficiency”.[17] Thus, UNC93B1 acts as a **modifier and upstream facilitator** of TLR3 function.

TRIF (TICAM1) is the primary adaptor molecule for TLR3, transmitting signals from the TIR domain to downstream kinases.[16] TRAF3 and TBK1 are involved in signaling cascades leading to IRF3 activation and interferon production.[16] IRF3 itself is a transcription factor that drives IFN-α/β gene expression. Mutations in TRIF, TRAF3, TBK1, and IRF3 have been found in children with HSV-1 encephalitis, underscoring their roles as **critical TLR3 pathway components**.[16] The review noted: “TLR3, UNC93B1, TRIF, TRAF3, TBK1, and IRF3 deficiencies are associated with impaired IFN-α/β and/or IFN-λ production upon stimulation of TLR3 or infection with HSV-1.”[16] IRF7 and IRF9 deficiencies impair type I and III IFN immunity and underlie severe influenza pneumonitis, further supporting the central role of the IFN axis in ARDS phenotypes.[13][14]

These genes do not necessarily modify the severity of disease in TLR3-deficient individuals, but their defects produce similar immunologic phenotypes, and they collectively form an **extended genetic network** of TLR3–IFN pathway disorders.

### 4.4 Epigenetic Information and Chromosomal Abnormalities

There is currently no strong evidence that epigenetic modifications directly cause or modulate TLR3 deficiency as a Mendelian disorder. TLR3 expression can be regulated by epigenetic mechanisms such as histone acetylation and DNA methylation in various contexts, including cancer and inflammatory diseases, but these have not been specifically implicated in familial HSV-1 encephalitis or influenza ARDS due to TLR3 variants.

Chromosomal abnormalities involving 4q35.1 have not been described as causes of TLR3 deficiency. The TLR3 locus is a single gene region; large deletions encompassing TLR3 could, in theory, cause haploinsufficiency, but such structural variants have not yet been documented in TLR3 deficiency cohorts. DECIPHER and related databases might record copy number variants that include TLR3, but their clinical relevance to HSV-1 encephalitis or influenza ARDS remains undetermined. Therefore, TLR3 deficiency is best conceptualized as a **single-gene point mutation disorder** with minimal involvement of chromosomal rearrangements or epigenetic drivers.

---

## 5. Environmental and Infectious Information

### 5.1 Environmental Factors

Non-genetic environmental factors contribute primarily as **infection triggers** and **modifiers of disease severity**, rather than as direct etiologic agents of TLR3 deficiency. Air pollution, tobacco smoke, and other inhaled toxins can exacerbate respiratory disease in general, and may worsen ARDS outcomes, but they have not been specifically investigated in TLR3-deficient influenza ARDS patients.[19] Similarly, neurotoxic exposures could influence recovery from encephalitis but do not cause the susceptibility.

Radiation, occupational exposures, and chemical toxins are not known contributors in the pediatric presentations typical of TLR3 deficiency.[4][2][6][13][14][16] Given the rarity of the disorder and its strong genetic basis, environmental risk factors beyond viral infections have limited relevance for etiology.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, diet, exercise, and alcohol consumption are generally not pertinent in the pediatric cases described to date. However, as TLR3 deficiency variants may be present in adults who could develop late-onset viral complications, lifestyle influences on lung or brain health might become relevant. For instance, smoking can impair pulmonary epithelial integrity and immune responses, potentially exacerbating influenza ARDS in TLR3-deficient adults, but such scenarios remain speculative.

Family planning and infection-control practices (hand hygiene, avoidance of sick contacts during viral outbreaks) could influence exposure risk and thus indirectly modify disease probability, but these are **general preventive factors** rather than specific lifestyle determinants of TLR3 deficiency.

### 5.3 Infectious Agents

The key infectious agents involved in TLR3 deficiency manifestations are **herpes simplex virus type 1 (HSV-1)** and **influenza A virus (IAV)**. HSV-1 is a double-stranded DNA virus that produces dsRNA intermediates during replication, which are recognized by TLR3.[4][15][16] Nature Reviews Immunology explained: “HSV1 is a double-stranded DNA (dsDNA) virus with dsRNA intermediates, and TLR3 recognizes dsRNA.”[15] TLR3-mediated sensing of dsRNA in CNS cells is crucial for restricting HSV-1 replication and preventing encephalitis.[4][2][6][16]

Influenza A virus is an RNA virus whose replication and transcripts generate dsRNA structures detected by TLR3 in pulmonary epithelial cells.[13][14] In TLR3-deficient children, impaired epithelial cell-intrinsic IFN responses to IAV lead to uncontrolled viral replication and severe lung inflammation, culminating in ARDS.[13][14] The influenza ARDS study concluded that TLR3 deficiency “may, therefore, lead to influenza ARDS due to the impairment of TLR3-dependent, IFN-α/β– and/or IFN-λ–mediated, PEC-intrinsic immunity to IAV.”[14]

Other viruses may interact with TLR3 pathways, but clinical susceptibility to them has not been consistently observed in TLR3-deficient patients. HIV, hepatitis B, and hepatitis C have been linked to TLR3 polymorphisms in population studies, suggesting that TLR3 may modulate responses to these infections, but rare Mendelian TLR3 deficiency does not appear to produce overt susceptibility in the small number of documented patients.[5][8]

---

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

Step 1: Germline loss-of-function or dominant-negative mutations in the **TLR3** gene lead to defective TLR3 protein structure or function, impairing dsRNA recognition and signaling in specific cell types, particularly CNS neurons and pulmonary epithelial cells.[3][4][2][6][13][14][16]

Step 2: Defective TLR3 signaling leads to impaired activation of the adaptor TRIF and downstream kinases (TBK1, IKKε) and transcription factors (IRF3, NF-κB) upon viral dsRNA exposure, resulting in reduced type I (IFN-α/β) and type III (IFN-λ) interferon production, as well as altered inflammatory cytokine responses.[3][4][2][6][13][14][16]

Step 3: Reduced interferon production leads to impaired induction of interferon-stimulated genes (ISGs) in CNS neurons, glial cells, and pulmonary epithelial cells, resulting in diminished cell-intrinsic antiviral states, which facilitates enhanced viral replication of HSV-1 in the brain and IAV in the lung.[2][4][6][13][14][16]

Step 4: Enhanced viral replication leads to direct cytopathic effects, cell death, and tissue damage in affected organs, accompanied by dysregulated local inflammatory responses, which result in acute encephalitis (in the case of HSV-1) or diffuse alveolar damage and ARDS (in the case of influenza A).[4][2][6][13][14][16][19]

Step 5: Acute organ damage leads to clinical manifestations such as seizures, altered consciousness, and focal neurological deficits in HSV-1 encephalitis, or hypoxemia, respiratory failure, and multi-organ dysfunction in influenza ARDS, with outcomes modulated by host factors, treatment, and secondary complications.[4][2][6][13][14][16][19]

These steps are supported by experimental evidence in patient-derived cells and model systems, though some aspects (e.g., specific cell type contributions and tissue-level inflammatory cascades) are inferred rather than fully demonstrated in humans.

### 6.2 Molecular Pathways

TLR3 deficiency disrupts a well-defined molecular pathway centered on **dsRNA recognition and interferon induction**. TLR3, located in endosomal compartments, binds dsRNA via its ectodomain and signals through its cytoplasmic TIR domain by recruiting the adaptor **TRIF (TICAM1)**.[3][8][16] TRIF then interacts with TRAF3 and TBK1, leading to phosphorylation and activation of IRF3, which translocates to the nucleus and drives transcription of type I interferon genes.[16] Concurrently, TRIF can activate NF-κB through TRAF6 and RIP1, inducing pro-inflammatory cytokines such as IL-6 and TNF.[3][8][16]

This pathway can be mapped onto KEGG and Reactome entries for **“Toll-like receptor signaling”** and **“Cytosolic DNA-sensing and RNA-sensing pathways”**, with GO terms such as **GO:0002224 (toll-like receptor signaling pathway)**, **GO:0034142 (toll-like receptor 3 signaling pathway)**, **GO:0034340 (response to type I interferon)**, and **GO:0006954 (inflammatory response)**. In TLR3 deficiency, mutations impair receptor function at the first step, thereby weakening the entire downstream cascade.

TLR3 is unique among TLRs in its specificity for dsRNA and its nonredundant role in certain tissues. Other dsRNA sensors such as **MDA5 (IFIH1)** and **RIG-I (DDX58)** also activate interferon pathways via MAVS and TBK1–IRF3, providing partial redundancy in many cell types.[16] However, in CNS neurons and pulmonary epithelial cells, TLR3 appears to be a crucial sensor whose loss cannot be fully compensated, especially during primary infections in childhood.[4][2][6][13][14][16]

The TLR3 pathway also intersects with other genes involved in severe influenza pneumonitis, such as IRF7 and IRF9, which are transcription factors and co-factors for interferon signaling.[13][14] Autosomal recessive IRF7 and IRF9 deficiencies impair type I and III IFN immunity and underlie severe influenza, analogous to TLR3 deficiency.[13][14] This highlights a broader **IFN axis** as the key molecular pathway, with TLR3 functioning as an upstream sensor.

### 6.3 Cellular Processes

At the cellular level, TLR3 deficiency affects several processes, including **cell-intrinsic antiviral immunity, apoptosis, and inflammatory signaling**. In normal cells, TLR3 activation by dsRNA induces interferons and ISGs that establish an antiviral state, limiting viral replication and promoting survival.[3][16] In TLR3-deficient fibroblasts, neurons, and epithelial cells, interferon production is reduced or absent, leading to uncontrolled viral replication and increased cell death upon infection.[2][4][6][13][14]

The autosomal recessive TLR3 deficiency study reported that patient fibroblasts had high levels of HSV-1 replication and cell death compared to controls, reflecting failure of antiviral defense.[6] This involves cellular processes such as **GO:0006955 (immune response)**, **GO:0016032 (viral process)**, **GO:0006915 (apoptotic process)**, and **GO:0034097 (response to cytokine)**. Enhanced viral replication induces stress pathways and apoptosis, contributing to tissue injury.

Inflammatory processes are also dysregulated. While interferon responses are blunted, inflammatory cytokine production via NF-κB may be variably affected, potentially leading to skewed inflammatory profiles that exacerbate tissue damage. In ARDS, lung microvascular thrombosis, endothelial activation, and leak of inflammatory mediators into systemic circulation contribute to multi-organ dysfunction.[19] TLR3 deficiency may modulate these cascades by altering the balance of antiviral and pro-inflammatory signals.

### 6.4 Protein Dysfunction

Protein dysfunction in TLR3 deficiency stems from **altered folding, dsRNA binding, oligomerization, or intracellular trafficking** of the TLR3 receptor. Missense mutations in the ectodomain (e.g., P533S, P554S, P680L) can disrupt the LRR structure required for dsRNA binding or receptor dimerization, thereby impairing signal initiation.[4][15][13][14] Dominant-negative effects may arise when mutant TLR3 interferes with the function of wild-type TLR3 by forming nonfunctional oligomers or by sequestering adaptor molecules.

Nonsense and frameshift mutations can truncate the TLR3 protein, removing the TIR domain or key transmembrane segments, leading to nonfunctional or unstable proteins subject to degradation.[2][6] Synonymous variants may affect splicing if they alter consensus splice sites, though in the case of NM_003265.3:c.441G>A, predictive algorithms suggest minimal impact.[12]

UNC93B1 deficiency illustrates another form of protein dysfunction: defective trafficking of TLR3 from the ER to endosomes, resulting in reduced surface localization and signaling.[17][16] Thus, protein dysfunction in TLR3 deficiency involves both **intrinsic structural defects** and **altered subcellular localization**.

### 6.5 Immune System Involvement

TLR3 deficiency is an **innate immune system disorder**, specifically affecting **pattern recognition receptor activity and interferon-mediated antiviral responses**.[3][8][16] Adaptive immunity, including T-cell and B-cell responses, remains largely intact in patients, explaining the absence of broad immunodeficiency. Innate immune GO terms include **GO:0045087 (innate immune response)** and **GO:0002218 (activation of innate immune response)**.

The immune system involvement is **tissue-specific**. In leukocytes, TLR3 is redundant for many antiviral responses because other receptors (e.g., TLR7, TLR9, RIG-I, MDA5) can compensate.[4][6][16] In CNS neurons and pulmonary epithelial cells, however, TLR3 appears to be a crucial sensor requisite for adequate interferon induction. Immune processes in these cells are best captured by cell ontology terms such as **CL:0000127 (neuron)** and **CL:0002062 (type II pneumocyte)**, and by process terms like **GO:0034340 (response to type I interferon)**.

Inflammatory responses, including cytokine production and leukocyte recruitment, are downstream of TLR3 signaling and may be altered in deficiency. However, the overall immune involvement is more characterized by **failure of protective antiviral immunity** rather than excessive autoimmunity or chronic inflammation.

### 6.6 Tissue Damage Mechanisms

Tissue damage in TLR3 deficiency arises from **viral cytopathicity and inflammatory injury**. In HSV-1 encephalitis, uncontrolled viral replication in neurons and glia leads to necrosis, apoptosis, and inflammatory infiltration, causing edema, hemorrhage, and necrotic lesions in temporal lobes.[4][2][6][16] The lack of TLR3-mediated interferon responses exacerbates viral spread and tissue destruction. Mechanisms include oxidative stress, excitotoxicity, and disruption of the blood-brain barrier, though these are inferred from HSE pathophysiology rather than specific TLR3-deficiency models.

In influenza ARDS, diffuse alveolar damage results from severe viral infection of epithelial cells, endothelial activation, and microvascular thrombosis.[19] The Lancet review of ARDS noted mechanisms such as platelet and endothelial activation with lung microvascular thrombosis, obstruction or destruction of the lung vascular bed, increased dead space ventilation, and leak of lung inflammatory mediators into systemic circulation, leading to systemic inflammatory response syndrome and multi-organ dysfunction.[19] In TLR3-deficient patients, impaired antiviral immunity allows greater viral burden, intensifying these injury mechanisms.

Tissue damage can be annotated with GO terms like **GO:0006954 (inflammatory response)**, **GO:0008219 (cell death)**, and **GO:0001932 (regulation of blood vessel remodeling)**, and with UBERON terms for affected organs.

### 6.7 Biochemical Abnormalities

Biochemical abnormalities in TLR3 deficiency are centered on **defective signal transduction and cytokine production** rather than classical metabolic derangements. Key biochemical features include reduced phosphorylation of IRF3, diminished transcription of interferon genes, altered NF-κB activation, and imbalances in cytokine profiles (e.g., low IFN-α/β, IFN-λ; variable IL-6, TNF).[2][4][6][13][14][16] These can be mapped to GO terms such as **GO:0032755 (positive regulation of interleukin-6 production)**, **GO:0032727 (positive regulation of interferon-alpha production)**, and **GO:0032728 (positive regulation of interferon-beta production)**, which are curtailed in deficiency.

There are no known systemic biochemical markers specific to TLR3 deficiency, such as abnormal serum metabolite profiles. Biochemical analysis thus focuses on cytokines and signaling molecules measured in vitro or in CSF during infections.

### 6.8 Molecular Profiling

Detailed molecular profiling (transcriptomics, proteomics, metabolomics) has been applied primarily in experimental settings to study TLR3 pathways, but not extensively in clinical TLR3-deficient cohorts due to small numbers. However, patient-derived fibroblasts, neurons, and epithelial cells have been analyzed for gene expression changes upon poly(I:C) stimulation or viral infection, revealing reduced induction of interferon-stimulated genes in TLR3 deficiency.[2][4][6][13][14][16]

Single-cell RNA sequencing and spatial transcriptomics could, in principle, elucidate cell-type specific mechanisms in CNS and lung tissues, but such technologies have not yet been widely applied in this rare disease context. Similarly, multi-omics integration based on TCGA or other cancer datasets is not directly relevant, as TLR3 deficiency is not a malignant condition.

Functional genomics screens (e.g., CRISPR knockouts of TLR3 pathway genes) have identified TLR3, UNC93B1, TRIF, TRAF3, TBK1, and IRF3 as key host factors for HSV-1 and IAV susceptibility in vitro, corroborating clinical findings, though these studies are not specifically aimed at TLR3 deficiency. Nonetheless, they support the causal chain described above.

### 6.9 Cell Types and GO/CL Terms

Key cell types involved in TLR3 deficiency pathophysiology include:

CNS neurons (CL:0000127), astrocytes (CL:0000124), and possibly oligodendrocytes (CL:0000128), which express TLR3 and participate in innate antiviral responses to HSV-1.[4][16] Pulmonary epithelial cells, particularly type II pneumocytes (CL:0002062) and type I pneumocytes (CL:0002063), express TLR3 and constitute the primary target cells in influenza ARDS.[13][14] Fibroblasts (CL:0000057) are commonly used in vitro to study TLR3 signaling and interferon responses.[2][4][6] Dendritic cells (CL:0000451) and other leukocytes express TLR3 but rely on redundant sensors, so their involvement is less critical in TLR3 deficiency.[4][6][16]

Suggested GO terms include **GO:0006955 (immune response)**, **GO:0045087 (innate immune response)**, **GO:0002224 (toll-like receptor signaling pathway)**, **GO:0034142 (toll-like receptor 3 signaling pathway)**, **GO:0034340 (response to type I interferon)**, and **GO:0006954 (inflammatory response)**.

---

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organs affected in TLR3 deficiency are the **brain** and the **lungs**. HSV-1 encephalitis targets the **central nervous system (CNS)**, particularly the **temporal lobes** and limbic structures.[4][2][6][16] UBERON terms include **UBERON:0000955 (brain)**, **UBERON:0001893 (cerebrum)**, and **UBERON:0001950 (cerebral cortex)**, with more specific references to **UBERON:0001871 (temporal lobe)**. Secondary organ involvement in HSV-1 encephalitis can include the meninges (UBERON:0002028), but TLR3 deficiency does not directly affect peripheral organs outside CNS viral pathology.

Influenza ARDS primarily affects the **lungs** (UBERON:0002048) and the **respiratory system** (UBERON:0002406).[13][14][19] Acute lung injury involves alveoli (UBERON:0002049), pulmonary capillaries (UBERON:0001985), and airways. Secondary organ involvement includes the cardiovascular system (UBERON:0004535) due to right heart failure, and other organs impacted by systemic inflammatory response and hypoxia, such as kidneys (UBERON:0002113) and liver (UBERON:0002107), as part of multi-organ dysfunction in severe ARDS.[19]

Body systems involved include the **nervous system**, **respiratory system**, and **immune system**, although immune system involvement is functional rather than anatomical. TLR3 deficiency does not cause structural anomalies of immune organs.

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, TLR3 deficiency affects **nervous tissue** and **epithelial tissue**. Nervous tissue includes neurons and glia; epithelial tissue includes respiratory epithelium and possibly other epithelia expressing TLR3. Connective tissues (fibroblasts) contribute experimentally but are not primary pathological targets.

Specific cell populations include CNS neurons (CL:0000127), astrocytes (CL:0000124), type I and type II pneumocytes (CL:0002063 and CL:0002062), and fibroblasts (CL:0000057).[2][4][6][13][14][16] Dendritic cells and monocytes may express TLR3 but rely on alternative sensors, making their involvement less critical.

### 7.3 Subcellular Localization

TLR3 is localized to **endosomal compartments** within cells, with GO Cellular Component terms such as **GO:0005768 (endosome)**, **GO:0005769 (early endosome)**, and **GO:0005770 (late endosome)**.[3][8] The receptor’s function depends on correct trafficking from the ER to endosomes, mediated by UNC93B1.[17][16] TLR3 acts at the interface of endosomal membranes and cytosolic signaling machinery, engaging cytoplasmic TRIF in the TIR domain.

Downstream signaling occurs in the **cytoplasm** (GO:0005737) and **nucleus** (GO:0005634), where IRF3 and NF-κB influence gene expression. Thus, subcellular compartments involved in TLR3 deficiency include endosomes, cytoplasm, and nucleus.

### 7.4 Localization and Lateralization

Anatomical localization of HSV-1 encephalitis lesions often shows **asymmetric involvement of temporal lobes**, but TLR3 deficiency does not impose a specific lateralization; lesions can be unilateral or bilateral depending on viral spread.[4][16] ARDS presents as bilateral diffuse lung infiltrates.[13][14][19] There is no inherent left-right bias in disease expression related to TLR3 genotype.

---

## 8. Temporal Development

### 8.1 Onset

Typical age of onset for TLR3 deficiency manifestations is **pediatric**, often between infancy and adolescence.[4][2][6][13][14][16] HSV-1 encephalitis in TLR3-deficient children generally presents in early childhood, consistent with primary HSV-1 infection exposure during that period. Onset is **acute**, with sudden appearance of neurological symptoms over one to several days.

Influenza ARDS in TLR3-deficient patients likewise occurs in childhood during influenza seasons, with acute onset of respiratory distress.[13][14] There is no evidence of congenital or neonatal TLR3 deficiency manifestations independent of infections, and adult-onset disease appears rare, though not impossible.

### 8.2 Disease Progression

Disease stages in HSV-1 encephalitis can be conceptually described as **early (prodromal)**, **intermediate (acute encephalitic)**, and **advanced (severe encephalitis or recovery)**. Early stage involves fever and nonspecific symptoms; intermediate stage comprises prominent neurological signs; advanced stage includes coma, refractory seizures, or recovery with or without sequelae. Progression is **rapid**, over days, and requires urgent antiviral therapy.

In influenza ARDS, progression from flu-like symptoms to respiratory failure can occur over several days, leading to full-blown ARDS characterized by diffuse alveolar damage and severe hypoxemia.[13][14][19] Disease course is **episodic**, centered around acute infections; between episodes, patients are generally stable.

Duration of each episode is **self-limited** if successfully treated, but neurological or pulmonary sequelae can be **chronic lifelong**. There is no chronic progressive course independent of infections.

### 8.3 Patterns and Critical Periods

Remission patterns in TLR3 deficiency are predominantly **treatment-induced**; antiviral therapy (acyclovir for HSV-1, oseltamivir for influenza) and supportive care drive recovery. Spontaneous remission of HSE is rare and often incomplete; ARDS may resolve more variably.

Critical periods include early childhood, when primary HSV-1 infection and influenza exposures are common and CNS and lung tissues may be particularly vulnerable to impaired innate immunity.[4][2][6][13][14][16] This suggests **developmental windows of vulnerability** where TLR3-mediated defenses are crucial.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

TLR3 deficiency is an **extremely rare** primary immunodeficiency. Precise prevalence and incidence data are unavailable due to the small number of documented cases worldwide and lack of systematic registries.[4][2][6][13][14][16][18] HSV-1 encephalitis itself has an estimated incidence of 1–2 per 500,000 per year in general populations, but only a fraction of these cases are attributable to TLR3 or pathway deficiencies.[4][16] Similarly, influenza ARDS occurs sporadically and is underdiagnosed; TLR3 deficiency may explain a small subset.

Given the rarity, prevalence likely falls well below 1 per million. Global burden of disease estimates do not specifically recognize TLR3 deficiency as a distinct entity, treating HSV-1 encephalitis and ARDS as broader conditions.

### 9.2 Inheritance Patterns

TLR3 deficiency exhibits both **autosomal dominant (AD)** and **autosomal recessive (AR)** inheritance.[1][4][2][6][13][14][16] OMIM entry 613002 notes “Autosomal dominant; Autosomal recessive” as inheritance patterns for immunodeficiency 83.[1][8] Autosomal dominant TLR3 deficiency arises from heterozygous missense loss-of-function or dominant-negative mutations such as P533S, P554S, and P680L.[4][15][13][14] Autosomal recessive deficiency involves biallelic loss-of-function variants causing complete absence of signaling.[2][6]

Penetrance in AD TLR3 deficiency appears **incomplete** and **age-dependent**. Some heterozygous carriers remain asymptomatic despite pathogenic variants,[4][16][13][14] suggesting that penetrance depends on viral exposure timing, host factors, and stochastic influences. Expressivity is **variable**, with some individuals experiencing HSV-1 encephalitis, others influenza ARDS, and some no severe infections. There is no evidence of genetic anticipation or germline mosaicism in reported cases.

AR TLR3 deficiency likely has **high penetrance** for at least one severe viral episode (e.g., childhood HSE), but sample size is too small to generalize. Consanguinity may increase risk for AR forms in populations with high consanguinity, but published cases have not systematically addressed this.

Founder effects and carrier frequencies have not been established, as pathogenic variants are extremely rare and scattered across populations. gnomAD frequencies for known pathogenic variants are extremely low or absent.[12][13][14]

### 9.3 Population Demographics

Affected populations include individuals from diverse ethnic backgrounds, reflecting the global distribution of HSV-1 and influenza and the sporadic nature of TLR3 variants.[4][2][6][13][14][16] Geographic distribution of specific variants may show clustering in families or regions, but no clear endemic patterns have been reported.

Sex ratio appears approximately equal; both males and females are affected, consistent with autosomal inheritance.[4][2][6][13][14][16] Age distribution is skewed toward childhood, as previously noted, with rare adult presentations.

---

## 10. Diagnostics

### 10.1 Clinical Tests and Biomarkers

Diagnosis of TLR3 deficiency begins with clinical identification of **unusually severe, organ-specific viral infections in otherwise healthy individuals**, especially HSV-1 encephalitis and influenza ARDS.[4][2][6][13][14][16] Standard clinical tests confirm the viral disease: lumbar puncture and CSF PCR detection of HSV-1, brain MRI for encephalitis, or nasopharyngeal swabs and PCR for influenza, chest imaging, and arterial blood gases for ARDS.[4][13][14][19]

There are no routine blood biomarkers specific to TLR3 deficiency. However, functional assays in specialized laboratories can measure impaired responses to poly(I:C) or viral infection in patient-derived cells, such as reduced IFN-β and IFN-λ production in fibroblasts.[2][6] These assays serve as diagnostic biomarkers of TLR3 pathway dysfunction, though they are not widely available.

### 10.2 Genetic Testing

Genetic testing is central to definitive diagnosis. Recommended approaches include **whole-exome sequencing (WES)** or **targeted gene panels** covering TLR3 and related pathway genes (UNC93B1, TRIF, TRAF3, TBK1, IRF3, IRF7, IRF9) in patients with HSE or severe influenza ARDS.[16][13][14] WES is particularly useful in rare, heterogeneous disorders, allowing identification of novel variants and differential diagnosis.

Single-gene testing of TLR3 via Sanger sequencing or NGS can be ordered when clinical suspicion is high, especially in familial cases. ClinVar and LOVD provide variant databases for TLR3.[10][11][12] Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion testing are generally not informative, as TLR3 deficiency is a point mutation disorder without known structural or mitochondrial aberrations.

Omics-based diagnostics (RNA-seq, proteomics, metabolomics) are not standard but could complement genetic testing by demonstrating functional consequences. For example, RNA-seq could reveal reduced interferon-stimulated gene induction after poly(I:C) stimulation in patient cells.

### 10.3 Clinical Criteria and Differential Diagnosis

Standardized diagnostic criteria for TLR3 deficiency are not yet formalized in society guidelines. However, a practical clinical approach involves:

Identification of HSV-1 encephalitis or severe influenza ARDS in an otherwise healthy child, often with family history of similar infections.[4][2][6][13][14][16] Exclusion of secondary immunodeficiencies (HIV, chemotherapy, severe malnutrition). Genetic testing for TLR3 and pathway genes. Functional validation of variants via in vitro assays of TLR3 signaling and interferon responses.

Differential diagnosis for HSV-1 encephalitis includes sporadic HSE without genetic predisposition, other viral encephalitides (e.g., arboviruses), autoimmune encephalitis, and CNS vasculitis. Distinguishing features of TLR3 deficiency include early age, recurrent or familial cases, and demonstration of TLR3 pathway defects.[4][16] For influenza ARDS, differential diagnosis includes ARDS due to bacterial pneumonia, sepsis, aspiration, and other viral infections; TLR3 deficiency is suspected when ARDS occurs in a child with no risk factors and when genetic analysis reveals pathogenic TLR3 variants.[13][14]

### 10.4 Screening

Screening for TLR3 deficiency in asymptomatic individuals is not currently performed, given the rarity, incomplete penetrance, and lack of specific preventive interventions. Newborn screening is not indicated. Cascade screening in families with known pathogenic TLR3 variants may be considered, combined with genetic counseling, to identify carriers and inform risk assessments for HSV-1 and influenza, but formal guidelines are lacking.

---

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Survival and mortality in TLR3 deficiency depend on the severity of viral infections and effectiveness of treatment. HSV-1 encephalitis carries a significant risk of mortality and severe neurological sequelae if untreated or treated late, with historical mortality rates up to 70% and reduced to 20–30% with prompt acyclovir.[4][16] In TLR3-deficient patients, mortality risk may be similar, though small sample sizes preclude precise estimates. Influenza ARDS in children has substantial mortality risk, often 20–40% in severe cases, with TLR3 deficiency potentially increasing risk due to impaired antiviral responses.[13][14][19]

Life expectancy of TLR3-deficient individuals who survive acute episodes may approach normal, provided no further severe infections occur and chronic sequelae are managed. There is no evidence of progressive deterioration independent of infections.

### 11.2 Morbidity and Function

Morbidity includes acute organ failure and long-term functional impairments. HSV-1 encephalitis survivors may suffer cognitive deficits, seizures, motor impairments, and psychiatric symptoms, leading to disability and reduced quality of life.[4][16] ARDS survivors may experience chronic lung disease, reduced exercise tolerance, and neurocognitive deficits as part of post-intensive care syndrome.[19] These impacts can be categorized under ICF domains of body functions, activities, and participation.

Quality of life measures (SF-36, EQ-5D) have not been systematically reported for TLR3 deficiency, but general HSE and ARDS literature indicate substantial impairments across domains.

### 11.3 Disease Course and Complications

Complications of HSV-1 encephalitis include chronic epilepsy, behavioral changes, learning difficulties, and secondary infections during hospitalization. ARDS complications include ventilator-associated pneumonia, barotrauma, thromboembolism, and multi-organ failure.[19] Recovery potential varies; some patients recover fully, others have partial recovery with residual deficits, and some die.

### 11.4 Prognostic Factors and Biomarkers

Prognostic factors include age at infection, timing of antiviral therapy, severity of organ damage at presentation, and presence of comorbidities. Genetic factors such as type of TLR3 variant (AD vs AR) may influence severity, though data are limited. Prognostic biomarkers specific to TLR3 deficiency are not established, but interferon levels and viral loads during infection could serve as indicators of disease course.

---

## 12. Treatment

### 12.1 Pharmacotherapy

Treatment of TLR3 deficiency focuses on managing acute viral infections and supporting organ function. For HSV-1 encephalitis, **intravenous acyclovir** (NCIT:C288) is standard of care, inhibiting viral replication and improving outcomes. For influenza ARDS, **neuraminidase inhibitors such as oseltamivir** (NCIT:C65858) are used to reduce viral load, alongside supportive care.[13][14][19]

Given the central role of interferons in pathophysiology, **interferon therapy** has been proposed. The TLR3–IFN pathway review suggested that IFN-α treatment may be beneficial in patients with impaired TLR3–IFN intrinsic immunity, particularly in HSV-1 encephalitis.[16] Interferon-α (NCIT:C205) and interferon-β (NCIT:C207) could theoretically enhance antiviral responses in TLR3-deficient cells, though clinical trials are lacking.

Anti-inflammatory drugs, anticoagulants, and lung-protective ventilation strategies are used in ARDS, based on general ARDS guidelines.[19] Corticosteroids have controversial roles in viral ARDS and are not specific to TLR3 deficiency.

Pharmacogenomics issues related to TLR3 variants are not defined; TLR3 deficiency does not influence drug metabolism but may affect responses to immunomodulators.

### 12.2 Advanced Therapeutics

Gene therapy and gene editing for TLR3 deficiency are currently theoretical. CRISPR-based correction of TLR3 mutations in hematopoietic stem cells or CNS cells would be challenging due to tissue accessibility and safety concerns. No clinical trials of TLR3-directed gene therapy are listed to date.

Cell therapies, such as stem cell transplant, are not indicated because the primary defect lies in nonhematopoietic cells (neurons and epithelial cells), and hematopoietic stem cell transplantation would not correct CNS-intrinsic or PEC-intrinsic defects.[16]

RNA-based therapies targeting viral replication (e.g., siRNA against HSV-1 or IAV) could be adjunctive, but are not specific to TLR3 deficiency.

### 12.3 Surgical and Supportive Interventions

Surgical interventions are not primary treatments. In ARDS, occasional use of extracorporeal membrane oxygenation (ECMO) may be needed to support gas exchange. Neurosurgical procedures such as intracranial pressure monitoring or decompressive craniectomy may be used in severe encephalitis with elevated ICP.

Supportive care is essential, including intensive care management, anticonvulsants for seizures, rehabilitation (physical, occupational, speech therapy), and neuropsychological support. These interventions are captured by NCIT terms such as **NCIT:C15371 (Supportive Care)** and **NCIT:C17057 (Physical Therapy)**.

### 12.4 Experimental Treatments and Personalized Medicine

Experimental treatments for TLR3 deficiency have not been systematically explored. However, personalized medicine approaches can incorporate genetic diagnosis to inform infection risk and treatment strategies. For example, children with TLR3 deficiency may receive **rapid antiviral therapy** at signs of HSV-1 or influenza infection, and be considered for prophylactic antiviral use during outbreaks.

Precision immunology approaches, including ex vivo functional assays of patient cells, can guide decisions about interferon therapy and other targeted interventions. NCIT terms related to personalized therapy, such as **NCIT:C25819 (Precision Medicine)**, are applicable.

---

## 13. Prevention

### 13.1 Primary Prevention

Primary prevention focuses on **reducing infection risk**, as TLR3 deficiency cannot currently be prevented genetically. Vaccination against influenza and other viruses reduces exposure and severity, though efficacy for ARDS prevention in TLR3-deficient individuals is uncertain.[13][14] HSV-1 vaccines are not widely available.

General infection-control measures (hand hygiene, avoiding contact with sick individuals, prompt isolation during outbreaks) are beneficial. Genetic counseling can inform at-risk families about potential disease manifestations, but does not prevent the disorder.

### 13.2 Secondary and Tertiary Prevention

Secondary prevention involves early detection and treatment of infections to prevent severe organ damage. For TLR3-deficient individuals, **low thresholds for testing and initiating antiviral therapy** during febrile illnesses are warranted. Regular monitoring during flu seasons and early imaging or lumbar puncture when neurological or respiratory symptoms appear can reduce morbidity.

Tertiary prevention aims to prevent complications and improve recovery through rehabilitation, seizure management, and long-term follow-up. Genetic counseling supports family planning and informs relatives about carrier status.

### 13.3 Screening and Counseling

Population screening for TLR3 deficiency is not justified by its rarity. Targeted genetic screening in families with known pathogenic variants, especially in siblings of affected children, can help identify carriers and inform risk stratification. Counseling by clinical geneticists and immunologists is crucial, guided by NSGC and ACMG resources.

Public health interventions such as vaccination campaigns and health education about viral infections support general prevention, but are not specific to TLR3 deficiency.

---

## 14. Other Species and Natural Disease

### 14.1 Orthologous Genes and Animal Susceptibility

TLR3 orthologs exist in multiple species, including mouse (**Tlr3**, NCBI Gene ID 142980), rat (Tlr3, Gene ID 364594), and other rodents.[5][7][9] The mouse Tlr3 gene is located on chromosome 8 and shares functional properties with human TLR3, enabling recognition of dsRNA and activation of NF-κB and interferon pathways.[5] Mouse Tlr3 is expressed in blood, brain, and submandibular gland primordium, reflecting broad tissue distribution.[5]

Natural TLR3 deficiencies have not been extensively reported in animals as Mendelian disorders, though experimental models use knockout mice to study Tlr3's role in viral infections.

### 14.2 Comparative Biology and Pathology

Comparative pathology reveals that Tlr3 knockout mice have altered responses to viral infections, including West Nile virus, HSV, and influenza, but the phenotypes are often milder or different than in humans.[16] This reflects species-specific differences in innate immune redundancy and the relative importance of TLR3 vs other sensors.

Evolutionary conservation of TLR3 suggests its importance in host defense, but human genetic data show that complete deficiency can be surprisingly compatible with life, with relatively narrow susceptibility to specific viruses, implying that **neurotropic and respiratory viruses may have driven evolutionary maintenance of TLR3**.[4] This is highlighted by Casanova’s comment that neurotropic viruses contributed to TLR3 evolution.[4][15]

There is no evidence of zoonotic aspects or cross-species transmission relevant to TLR3 deficiency; HSV-1 and influenza A are human pathogens with some animal reservoirs but TLR3 deficiency does not alter their zoonotic potential.

---

## 15. Model Organisms

### 15.1 Mouse Models

Mouse **Tlr3 knockout models** are key tools for studying TLR3 pathways. Tlr3−/− mice have defects in dsRNA recognition and interferon induction, resulting in altered susceptibility to viral infections.[5][16] They show impaired responses to poly(I:C) and modified immunopathology in various infection models, though often with partial redundancy from other sensors.

Phenotype recapitulation in Tlr3−/− mice is partial compared to human TLR3 deficiency. Mice may have increased susceptibility to certain viruses, but do not necessarily develop HSV-1 encephalitis or influenza ARDS mirroring human presentations, due to differences in viral tropism, innate immune networks, and experimental conditions.[16] Thus, Tlr3−/− mice capture molecular aspects of TLR3 deficiency but not the full human disease phenotype.

### 15.2 Other Models and Applications

Other model organisms such as rats, zebrafish, and invertebrates have TLR-like receptors and are used to study innate immunity, but specific TLR3 deficiency models are less developed. Cell lines, including human fibroblasts, CNS organoids, and iPSC-derived neurons or pulmonary epithelial cells, are increasingly used to model TLR3 deficiency in vitro, allowing detailed functional studies of patient mutations.[2][4][6][13][14][16]

Applications of these models include dissecting TLR3 signaling, testing antiviral drugs, evaluating interferon therapies, and exploring gene editing strategies. Limitations include incomplete recapitulation of tissue microenvironments and systemic factors, and species differences in gene regulation.

---

## Conclusion

TLR3 deficiency, designated in OMIM as **Immunodeficiency 83, susceptibility to viral infections** and encompassing autosomal dominant and recessive forms, represents a paradigmatic inborn error of innate immunity characterized by **selective susceptibility to severe viral disease in specific organs despite otherwise normal health.**[1][4][2][6][13][14][16] Germline loss-of-function or dominant-negative mutations in the TLR3 gene impair dsRNA sensing and downstream signaling via TRIF–TRAF3–TBK1–IRF3, leading to defective interferon-α/β and interferon-λ production and diminished cell-intrinsic antiviral states in CNS neurons and pulmonary epithelial cells.[3][8][4][2][6][13][14][16] This predisposes affected individuals to childhood HSV-1 encephalitis and influenza A virus–associated ARDS, with high morbidity and mortality but limited broader infectious susceptibility.[4][2][6][13][14][16]

The disease’s mechanistic chain from mutation to clinical manifestation involves defective receptor function, impaired interferon induction, enhanced viral replication, tissue damage via cytopathicity and inflammation, and resultant organ failure. These steps are delineated and supported by patient-derived cell studies and animal models, though some tissue-level processes remain inferred. Ontologically, TLR3 deficiency can be annotated using MONDO disease identifiers, HGNC gene entries, HPO phenotypes (e.g., encephalitis, ARDS), GO processes (toll-like receptor signaling, innate immune response), CL cell types (neurons, pneumocytes), and UBERON anatomical structures (brain, lung).[1][3][8][11][13][14][16][19]

Diagnostics rely on recognizing severe viral infections in otherwise healthy children, confirming viral etiologies, and performing genetic testing for TLR3 and pathway genes, complemented by functional assays of TLR3 signaling when available. Prognosis depends on timely antiviral therapy and supportive care, with outcomes ranging from full recovery to lifelong neurological or pulmonary sequelae. Treatment currently centers on standard antiviral drugs and organ support, with interferon therapy as a potential but unproven adjunct. Preventive strategies focus on infection control and vaccination rather than genetic modification.

Research on TLR3 deficiency has illuminated fundamental principles of human innate immunity, including the tissue-specific nonredundancy of TLR3, the importance of cell-intrinsic interferon responses, and the concept of monogenic susceptibility to common viral infections. Continued study will refine epidemiological estimates, expand variant catalogs, explore therapeutic innovations, and deepen our understanding of TLR3’s role in human health and disease, enriching disease knowledge bases and guiding precision immunology.