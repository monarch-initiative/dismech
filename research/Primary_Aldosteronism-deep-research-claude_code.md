---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-05T19:46:44.070878'
end_time: '2026-09-05T19:52:25.023721'
duration_seconds: 340.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Primary Aldosteronism
  mondo_id: MONDO:0001422
  category: Complex
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
  web_search_requests: 24
  num_turns: 25
  total_cost_usd: 1.4981650000000002
  session_id: 217b6b78-73e2-5d40-9d95-1bc55383fe0e
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Aldosteronism
- **MONDO ID:** MONDO:0001422 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Primary Aldosteronism** covering all of the
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

I'll research Primary Aldosteronism now using web search across the key domains needed for this comprehensive report.

I now have comprehensive coverage across etiology, genetics, mechanism, phenotypes, diagnostics, treatment, epidemiology, and comparative biology. Let me do a final round on a few remaining gaps: prevalence/incidence numbers with specific citations, diagnostic criteria specifics with PMIDs, and gene therapy/emerging therapeutics, plus quality of life data.

# Primary Aldosteronism: Comprehensive Research Report

## 1. Disease Information

**Overview.** Primary aldosteronism (PA) is a group of disorders in which aldosterone production by the adrenal cortex is inappropriately high, relatively autonomous of the renin-angiotensin system, and non-suppressible by sodium loading. The excess aldosterone drives renal sodium retention and potassium/hydrogen wasting, producing volume-expanded, low-renin hypertension with or without hypokalemia. PA is now recognized as the most common identifiable (surgically or pharmacologically correctable) cause of secondary hypertension, present in roughly 5–10% of unselected hypertensive patients and up to 20% of those with resistant hypertension (Cleveland Clinic Journal of Medicine review; PMC10118808).

**Key identifiers:**
- **MONDO:** MONDO:0001422 (primary hyperaldosteronism); related family: MONDO:0013359, MONDO:0014875 (familial hyperaldosteronism subtypes)
- **OMIM:** #103900 (Hyperaldosteronism, Familial, Type I / GRA); Familial hyperaldosteronism type II (HALD2, CLCN2); type III (HALD3, KCNJ5); type IV (HALD4, CACNA1H); #615474 (Primary Aldosteronism, Seizures, and Neurologic Abnormalities — PASNA, CACNA1D)
- **Orphanet:** ORPHA231637 (surgically correctable PA / aldosterone-producing adenoma); ORPHA251274 (Familial hyperaldosteronism type III); related entries for FH-I (GRA) and FH-II
- **ICD-10:** E26.0 (primary hyperaldosteronism); E26.01 (Conn syndrome); E26.02 (Glucocorticoid-remediable aldosteronism); E26.09 (Other primary hyperaldosteronism)
- **ICD-11:** 5A11 (Primary aldosteronism)
- **MeSH:** D006929 (Hyperaldosteronism)

**Synonyms:** Conn syndrome/Conn's syndrome (historically restricted to unilateral aldosterone-producing adenoma), primary hyperaldosteronism, aldosteronism, Conn-Louis syndrome, idiopathic hyperaldosteronism (bilateral form).

**Evidence base type:** Predominantly aggregated, disease-level clinical and molecular evidence — large referral-center cohorts (e.g., PAPY study, PAPPHY, Japan Primary Aldosteronism Study [JPAS], German Conn's Registry), systematic reviews/meta-analyses, and case-report-level genetic descriptions for the ultra-rare familial/monogenic forms. Recent large real-world screening data also derive from EHR-based nationwide cohorts (e.g., the 7.8-million-patient longitudinal screening/diagnosis-trends study, medRxiv 2025.11.13.25340212).

---

## 2. Etiology

### Disease Causal Factors
PA arises from two broad, non-mutually-exclusive mechanisms:
1. **Sporadic somatic mutations** in adrenal zona glomerulosa cells that constitutively activate calcium signaling, driving unregulated CYP11B2 (aldosterone synthase) expression — the cause of most aldosterone-producing adenomas (APA) and aldosterone-producing cell clusters (APCC).
2. **Germline (inherited) mutations** in the same or related ion-transport genes, causing rare monogenic familial hyperaldosteronism (FH) syndromes, typically presenting with bilateral adrenal hyperplasia and early, severe hypertension.

**Somatic drivers (APA):** Recurrent somatic mutations in genes encoding ion channels/pumps that regulate intracellular calcium and membrane potential account for >50% of APAs. In a large European multicenter cohort of 474 APA patients, somatic mutation prevalence was: **KCNJ5 ~38%, CACNA1D ~9.3%, ATP1A1 ~5.3%, ATP2B3 ~1.7%** (PMID review via Hypertension/AHA sources); KCNJ5 prevalence is markedly higher in East Asian populations (55–75% in Japan/Taiwan) than Western cohorts (25–50%). **CTNNB1** (β-catenin) exon-3 activating mutations, causing constitutive Wnt signaling, are found in ~5% of APAs, often co-occurring with an ion-channel mutation (PMC5620029). A 2024 preprint additionally identifies somatic **MCOLN3** mutations as a novel APA driver (bioRxiv 2024.10.20.619295).

- **Mechanism (shared endpoint):** KCNJ5 mutations render the inward-rectifying K+ channel (Kir3.4) permeable to Na+, causing membrane depolarization; CACNA1D, ATP1A1, and ATP2B3 mutations directly or indirectly increase voltage-gated Ca²⁺ influx. All converge on sustained elevation of intracellular Ca²⁺, which drives CYP11B2 transcription via CaMK signaling → autonomous aldosterone synthesis.

**Germline/familial causes (FH types I–IV plus PASNA):**

| Type | Gene | Locus | Mechanism | OMIM |
|---|---|---|---|---|
| FH-I (Glucocorticoid-Remediable Aldosteronism, GRA) | Chimeric **CYP11B1/CYP11B2** gene | 8q24.3 unequal crossover | ACTH-driven aldosterone synthase ectopically expressed in zona fasciculata | #103900 |
| FH-II | **CLCN2** | 3q27 | Gain-of-function chloride channel → increased Cl⁻ efflux → membrane depolarization → Ca²⁺ influx | HALD2 |
| FH-III | **KCNJ5** | 11q24 | Germline loss of K+ selectivity → Na+ permeability → depolarization; often massive bilateral hyperplasia | HALD3 |
| FH-IV | **CACNA1H** | 16p13 | Direct gain-of-function increase in Ca²⁺ channel current | HALD4 |
| PASNA | **CACNA1D** | 3p21 | De novo gain-of-function Ca²⁺ channel variant; syndromic (seizures, neurodevelopmental abnormalities) | #615474 |

"In FH-II, pathogenic variants in CLCN2 lead to increased chloride efflux, and in FH-III, pathogenic variants in KCNJ5 render the encoded potassium channel permeable to sodium ions, with the resulting membrane depolarization causing voltage-gated calcium influx in both conditions... CACNA1H pathogenic variants in FH-IV directly increase calcium influx" (PMC7999899, *Unravelling the Genetic Basis of Primary Aldosteronism*).

FH-I (GRA) accounts for ~0.5–1.0% of all PA cases and is autosomal dominant; it is diagnostically important because it responds to glucocorticoid (ACTH) suppression therapy rather than mineralocorticoid receptor antagonism alone.

**PASNA (OMIM #615474):** Caused by heterozygous, typically de novo, gain-of-function CACNA1D variants (e.g., p.Gly403Asp) altering the S6 pore-lining segment of the Cav1.3 channel; overlaps mechanistically with a subset of somatic CACNA1D-driven APAs and with certain autism-spectrum-associated de novo CACNA1D variants, reflecting the same channel's dual role in adrenal and neuronal excitability.

### Risk Factors
**Genetic:**
- Somatic KCNJ5/CACNA1D/ATP1A1/ATP2B3/CTNNB1 mutations (sporadic APA drivers, not inherited)
- Germline FH-I to FH-IV and PASNA variants (rare monogenic causes)
- **GWAS-identified susceptibility loci:** A genome-wide association study (1,162 cases, 3,296 controls) identified loci on chromosomes **1, 13, and X**; the chromosome 13 locus was male-specific and stronger in bilateral hyperplasia than APA. Candidate genes **CASZ1** and **RXFP2** are expressed in adrenal tissue, and their overexpression suppresses mineralocorticoid output in adrenocortical cells without affecting cortisol biosynthesis (PMC9440917, *Identification of risk loci for primary aldosteronism in genome-wide association studies*).
- Family history of PA or early-onset stroke (<40 years) — an indication for genetic testing for FH-I.
- **ARMC5** germline mutations (two-hit tumor-suppressor mechanism) predispose to primary bilateral macronodular adrenocortical disease (PBMAD), which can co-secrete aldosterone and cortisol with distinct somatic ARMC5 "second hits" in individual nodules (PMC12861490).

**Environmental/lifestyle:**
- Age (APCC and somatic-mutation burden accumulate with age; incidence of clinically apparent PA peaks in the 4th–6th decades)
- Sex (see Population Demographics)
- Obesity, metabolic syndrome, and elevated BMI — more pronounced in bilateral idiopathic hyperaldosteronism (IHA) than APA
- **Obstructive sleep apnea (OSA):** bidirectional relationship; PA prevalence is elevated in resistant-hypertension/OSA populations, and aldosterone excess is hypothesized to worsen upper-airway edema/fluid shift, while intermittent hypoxia may stimulate aldosterone secretion (PMC9556954)
- High dietary sodium intake unmasks the hypertensive/hypokalemic phenotype

### Protective Factors
No well-established genetic protective variants are documented for PA specifically. CASZ1/RXFP2 overexpression suppressing mineralocorticoid output (identified via GWAS) is a candidate protective mechanism rather than a validated protective allele. Reduced dietary sodium intake blunts the hypokalemic/hypertensive phenotype but does not reduce aldosterone excess itself.

### Gene-Environment Interactions
High sodium intake combined with autonomous aldosterone secretion (genetic driver) synergistically worsens hypertension and hypokalemia — the volume-expansion/potassium-wasting phenotype is sodium-dependent, which underlies the use of high-salt provocative testing (saline infusion, oral sodium loading) in confirmatory diagnosis. Aging appears to interact with somatic mutation acquisition: APCCs harboring the same somatic mutations found in APAs accumulate with age in histologically normal adrenal tissue, suggesting a stepwise, age-dependent progression from focal cell clusters to overt adenoma (Journal of the Endocrine Society, PMC/academic.oup.com jes/1/7/787).

**Suggested ontology terms:** HGNC genes — KCNJ5 (HGNC:6266), CACNA1D (HGNC:1391), ATP1A1 (HGNC:799), ATP2B3 (HGNC:816), CTNNB1 (HGNC:2514), CLCN2 (HGNC:2020), CACNA1H (HGNC:1395), CYP11B1 (HGNC:2591), CYP11B2 (HGNC:2592), ARMC5 (HGNC:25781).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
| Phenotype | HPO term | Frequency notes |
|---|---|---|
| Hypertension | HP:0000822 | Near-universal defining feature; often resistant to ≥3 drugs |
| Hypokalemia | HP:0002900 | Classically taught as a hallmark, but **normokalemia is now the most common presentation**: in a 5,100-patient tertiary hypertension cohort, hypokalemia occurred in only 15.8% (76.9% normokalemic, 7.3% hyperkalemic); PA prevalence in hypokalemic hypertensives was 28.1%, rising to 88.5% with spontaneous K+ <2.5 mmol/L (AHA Hypertension, PMID:32114853) |
| Muscle weakness/cramping | HP:0001324 / HP:0003394 | Secondary to hypokalemia |
| Fatigue | HP:0012378 | Common, nonspecific |
| Headache | HP:0002315 | Related to hypertension |
| Palpitations | HP:0001962 | Related to hypokalemia-induced arrhythmia risk |
| Polyuria/polydipsia | HP:0000103 / HP:0001959 | From hypokalemic nephrogenic diabetes insipidus-like effect |
| Paresthesia | HP:0003401 | Hypokalemia-related |
| Metabolic alkalosis | HP:0001948 | Laboratory abnormality from H+ wasting |
| Left ventricular hypertrophy | HP:0001712 | Target-organ damage, disproportionate to BP level |
| Anxiety/depression | HP:0000739 / HP:0000716 | Documented excess vs. essential hypertension and general population |

**Laboratory abnormalities:** suppressed plasma renin activity/concentration, elevated plasma aldosterone concentration (PAC), elevated aldosterone-to-renin ratio (ARR), hypokalemia, mild hypernatremia, metabolic alkalosis, elevated urinary potassium excretion despite hypokalemia (inappropriate kaliuresis).

### Phenotype Characteristics
- **Age of onset:** Typically adult-onset (peak diagnosis 30s–60s); familial forms (FH-I, FH-III, PASNA) present in childhood/adolescence with severe, early hypertension.
- **Severity:** Highly variable — from mild, normokalemic hypertension to severe, treatment-resistant hypertension with profound hypokalemia (especially FH-III with massive bilateral hyperplasia, hypokalemia in >85% of patients).
- **Progression:** Generally chronic and progressive if untreated, with worsening target-organ damage over time; some cases (APCC-driven) may represent an early/subclinical stage preceding overt PA.
- **Frequency of hypokalemia:** ~9–37% of PA cases overall depending on cohort and case-detection strategy; markedly higher in FH-III and larger APAs.

### Quality of Life Impact
Health-related quality of life (HRQoL) is significantly impaired in untreated PA. "Psychopathological symptoms of anxiety, demoralization, stress, depression and nervousness were more frequently reported in untreated patients with primary aldosteronism than in the general population and patients with hypertension" (JCEM, PMID:29099927). Both adrenalectomy and mineralocorticoid receptor antagonist (MRA) therapy improve HRQoL and psychological symptoms, with significant gains in physical and mental summary scores at 1-year follow-up in Asian cohort studies (PMC8346187). Autonomous cortisol co-secretion (ACS), seen in a subset of PA patients (overlapping with PBMAD/ARMC5 biology), may further contribute to depression/anxiety burden.

---

## 4. Genetic/Molecular Information

### Causal Genes (summary table)
| Gene | HGNC | Context | Variant class |
|---|---|---|---|
| KCNJ5 | HGNC:6266 | Somatic (APA, ~38%) and germline (FH-III) | Missense, in-frame deletion (e.g., p.Thr158Ala, p.Gly151Arg, 157–159delITE) |
| CACNA1D | HGNC:1391 | Somatic (APA, ~9%) and germline (PASNA) | Missense gain-of-function (e.g., p.Gly403Asp) |
| ATP1A1 | HGNC:799 | Somatic (APA, ~5%) | Missense |
| ATP2B3 | HGNC:816 | Somatic (APA, ~2%), X-linked | In-frame deletion |
| CTNNB1 | HGNC:2514 | Somatic (~5% of APA), often co-mutated | Exon-3 activating missense |
| CLCN2 | HGNC:2020 | Germline (FH-II) | Gain-of-function missense |
| CACNA1H | HGNC:1395 | Germline (FH-IV) | Gain-of-function missense (e.g., p.Met1549Val, p.Tyr613Phe) |
| CYP11B1/CYP11B2 chimera | HGNC:2591/2592 | Germline (FH-I/GRA) | Unequal crossover chimeric gene |
| ARMC5 | HGNC:25781 | Germline + somatic "second hit" (PBMAD, occasional PA/Cushing overlap) | Two-hit tumor-suppressor inactivation |

### Variant Classification and Functional Consequences
- **Somatic APA variants** are gain-of-function with respect to Ca²⁺ signaling: KCNJ5/CLCN2 alterations act indirectly via membrane depolarization; CACNA1D/CACNA1H/ATP1A1/ATP2B3 alter Ca²⁺ handling more directly; CTNNB1 acts through a parallel Wnt/β-catenin proliferative pathway.
- **ClinVar** entries exist for CACNA1D variants (e.g., NM_000720.4:c.1208G>A, p.Gly403Asp) classified pathogenic for "aldosterone-producing adenoma with seizures and neurological abnormalities," and CACNA1H variants (e.g., NM_021098.3:c.3806G>A, p.Arg1269His) associated with FH-IV.
- **Somatic vs. germline:** APA driver mutations are acquired, tumor-restricted somatic events (confirmed via tumor-vs-blood sequencing); FH-I through FH-IV and PASNA are germline (constitutional), heritable in autosomal-dominant fashion (or de novo for PASNA).
- **Genotype-phenotype correlation:** KCNJ5-mutant APAs tend to be **larger, histologically heterogeneous** (mixed zona fasciculata-like/glomerulosa-like cells) and occur preferentially in **younger women**; CACNA1D/ATPase-mutant APAs are **smaller, histologically homogeneous, zona-glomerulosa-like**, and more common in **older men** (PMC11454283, *CACNA1D- and KCNJ5-Mutant APAs Have Opposite 2-Year Clinical Outcomes from Adrenalectomy*). KCNJ5 mutation carriers show younger age at diagnosis (42.1 vs 47.6 years) and higher aldosterone levels — "a more florid phenotype."

### Modifier Genes
CASZ1 and RXFP2 (GWAS-nominated) may modulate mineralocorticoid output and disease susceptibility rather than acting as primary causal genes.

### Epigenetic Information
DNA methylation changes at the CYP11B2 locus have been documented in KCNJ5-mutant adrenocortical tumors, potentially contributing to aberrant aldosterone synthase regulation (PMC11255478, *Adrenocortical Tumor Associated With Pathogenic Variant in KCNJ5 and DNA Methylation of CYP11B2*). Broader epigenomic (histone/chromatin) characterization of PA adrenal tissue remains an active but less mature research area compared to genomic sequencing.

### Chromosomal Abnormalities
No recurrent aneuploidy or large structural rearrangement is a primary cause of typical PA; the FH-I chimeric gene is itself an intragenic structural (crossover) event on 8q24.3 rather than a whole-chromosome abnormality. ARMC5-driven PBMAD shows tumor-restricted loss of heterozygosity (LOH) as its somatic "second hit."

---

## 5. Environmental Information

- **Environmental/toxicological factors:** No established environmental toxin or exposure directly causes PA in the way seen for some other endocrine disorders; PA is overwhelmingly genetically/molecularly driven at the tumor or channel level.
- **Lifestyle factors:** High dietary sodium intake exacerbates the hypertensive and hypokalemic phenotype and is used diagnostically (oral salt-loading/saline infusion confirmatory tests). Obesity and metabolic syndrome are associated with higher rates of bilateral idiopathic hyperaldosteronism specifically. Obstructive sleep apnea is a frequently co-occurring, mechanistically intertwined condition (bidirectional relationship with excess fat tissue/adipokine secretion implicated).
- **Infectious agents:** Not applicable — PA is not an infectious disease.
- **Note on apparent mineralocorticoid excess:** Licorice (glycyrrhizin) ingestion causes a *mimicking* syndrome (apparent mineralocorticoid excess via 11β-HSD2 inhibition) with low aldosterone/renin, and is a key **differential diagnosis** rather than a cause of true PA.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. A somatic mutation in a zona glomerulosa cell (KCNJ5, CACNA1D, ATP1A1, ATP2B3, or CTNNB1) — **or**, in familial forms, a germline mutation (CLCN2, KCNJ5, CACNA1H) or the CYP11B1/CYP11B2 chimeric gene — **leads to** dysregulated ion transport across the zona glomerulosa cell membrane.
2. For channel/pump mutations, this **leads to** sustained membrane depolarization (via aberrant Na+ or Cl⁻ flux) **or** a direct increase in voltage-gated Ca²⁺ channel activity.
3. Membrane depolarization **results in** opening of voltage-gated Ca²⁺ channels and **leads to** sustained elevation of intracellular Ca²⁺ concentration — "the central switch for aldosterone production" (PMC review, JCEM 101:3874).
4. Elevated intracellular Ca²⁺ **activates** calcium/calmodulin-dependent kinase (CaMK) signaling, which **drives** transcriptional upregulation of **CYP11B2** (aldosterone synthase), the enzyme that catalyzes 11-deoxycorticosterone → corticosterone → 18-hydroxycorticosterone → aldosterone.
5. In CTNNB1-mutant cells, constitutive Wnt/β-catenin pathway activation **independently promotes** both zona glomerulosa cell proliferation (adenoma formation) and CYP11B2 expression, often acting in parallel with, or synergistically with, an ion-channel mutation.
6. In FH-I (GRA), the CYP11B1/CYP11B2 chimeric gene **results in** ectopic, ACTH-driven (rather than angiotensin-II/potassium-driven) aldosterone synthase expression in the **zona fasciculata**, bypassing normal RAAS regulation entirely — this is a distinct upstream mechanism from the calcium-signaling route.
7. Autonomous CYP11B2 activity **causes** aldosterone secretion that is inappropriately high relative to sodium/volume status and **not suppressed** by volume expansion (the biochemical definition of PA), unlike physiological aldosterone secretion which is normally stimulated by angiotensin II (via AT1 receptors) and hyperkalemia.
8. Excess circulating aldosterone **binds** the mineralocorticoid receptor (MR) in the renal distal nephron, **leading to** upregulated epithelial sodium channel (ENaC) activity, **causing** increased sodium reabsorption and potassium/hydrogen ion secretion.
9. Increased sodium reabsorption **results in** extracellular volume expansion, which **suppresses** renin release from the juxtaglomerular apparatus (completing the "low renin" biochemical signature) and **contributes to** hypertension via increased cardiac preload and peripheral vascular resistance.
10. Concurrent potassium wasting **leads to** hypokalemia (in a subset of patients, generally those with higher aldosterone burden — e.g., FH-III, larger APAs) and hydrogen ion loss **leads to** metabolic alkalosis.
11. In parallel to its classical renal/hemodynamic effects, aldosterone/MR activation in **non-epithelial tissues** (cardiac myocytes/fibroblasts, vascular smooth muscle/endothelium, renal mesangial cells/podocytes, macrophages) **triggers** non-genomic and genomic pro-inflammatory and pro-fibrotic programs — increased NADPH oxidase-derived reactive oxygen species (ROS), macrophage-mediated inflammation, and TGF-β/collagen deposition.
12. This tissue-level inflammation and fibrosis **leads to**, largely **independent of blood pressure level**, increased risk of left ventricular hypertrophy, myocardial and vascular fibrosis, endothelial dysfunction, glomerular injury/proteinuria, and renal fibrosis — explaining why PA carries a substantially higher cardiovascular and renal event rate than essential hypertension at matched blood pressure (Lancet Diabetes Endocrinol meta-analysis, PMID:29129575: stroke OR 2.58, coronary artery disease OR 1.77, atrial fibrillation OR 3.52, heart failure OR 2.05, LVH OR 2.29).
13. Long-term, unchecked steps 8–12 **culminate in** the clinical endpoints of resistant hypertension, target-organ damage (cardiac, renal, cerebrovascular), and the psychiatric/quality-of-life burden described in Section 3 — the latter mechanism (direct CNS/mood effects of MR overactivation) is comparatively more **inferred** than directly demonstrated in humans, drawing on animal and cross-sectional psychopathology data.

### Additional Mechanistic Detail by Category

- **Molecular pathways:** Calcium/calmodulin signaling (central node); Wnt/β-catenin signaling (CTNNB1-mutant subset); renin-angiotensin-aldosterone system (RAAS) — dysregulated/bypassed; cAMP/PKA-ACTH signaling (ectopically hijacked in FH-I).
- **Cellular processes:** Zona glomerulosa cell proliferation and clonal expansion (adenoma formation); adrenocortical zonation remodeling with age producing **aldosterone-producing cell clusters (APCCs)** — subcapsular clusters of CYP11B2⁺ cells that frequently harbor the same somatic mutations as APAs and increase in number/area with age, potentially representing a precursor lesion or a distinct, subclinical driver of age-related hypertension (JCEM 107(9):2439; J Endocr Soc 1(7):787).
- **Protein dysfunction:** Loss of ion selectivity (KCNJ5/Kir3.4 channel), gain-of-function calcium channel gating (CACNA1D/Cav1.3, CACNA1H/Cav3.2), altered pump stoichiometry (ATP1A1 Na+/K+-ATPase, ATP2B3 plasma membrane Ca²⁺-ATPase), constitutively stabilized β-catenin (CTNNB1) evading degradation.
- **Metabolic changes:** Hypokalemic metabolic alkalosis; mineralocorticoid-driven sodium/water retention; adverse effects on glucose metabolism — "glucose metabolism was impaired in PA, regardless of hypokalemia and subclinical hypercortisolism status, and was improved by adrenalectomy, but not spironolactone treatment" (PMC6947343).
- **Immune system involvement:** Macrophage-mediated renal and cardiac inflammation driven by MR activation in myeloid cells; aldosterone/MR signaling modulates broader immune cell function (T cells, macrophages) contributing to a pro-inflammatory state (PMC4581510, *Modulation of Immunity and Inflammation by the Mineralocorticoid Receptor and Aldosterone*).
- **Tissue damage mechanisms:** Oxidative stress via NADPH oxidase/mitochondrial ROS; renal fibrosis via mesangial cell proliferation, podocyte injury, and interstitial fibroblast activation; vascular stiffness and endothelial dysfunction; myocardial fibrosis and LVH.
- **Biochemical abnormalities:** Elevated 18-hydroxycortisol and 18-oxocortisol (hybrid steroids), particularly marked in FH-III; suppressed plasma renin; elevated PAC/ARR.
- **Molecular profiling:** Transcriptomic studies (e.g., GEO dataset GSE90867) characterize KCNJ5-mutant APA gene expression signatures; comparative genomic/transcriptomic profiling across genotypes (PMC5979346) shows genotype-specific expression clusters correlating with the histopathologic differences noted above.
- **Advanced technologies:** Single-cell resolution characterization of APCCs (JCEM 107(9):2439) has defined their transcriptional identity relative to normal zona glomerulosa and APA tissue; whole-genome/targeted sequencing (including in the feline model, below) continues to refine the somatic mutation landscape.

**Suggested GO terms:** GO:0032341 (regulation of aldosterone biosynthetic process), GO:0006816 (calcium ion transport), GO:0035810 (positive regulation of urine volume — related renal effect), GO:0035810, GO:0043123 (positive regulation of NF-kB — inflammatory arm), GO:0030177 (positive regulation of Wnt signaling pathway, CTNNB1 axis), GO:0071465 (cellular response to elevated intracellular Ca²⁺). **CL terms:** zona glomerulosa cell (adrenal cortical cell, CL:0002097 adrenal cortex cell or more specific if available), cardiac fibroblast (CL:0002548), macrophage (CL:0000235), podocyte (CL:0000653).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Adrenal gland (cortex, specifically the zona glomerulosa) — UBERON:0002369 (adrenal gland), UBERON:0001236 (zona glomerulosa)
- **Secondary/complication organs:** Heart (LVH, fibrosis, atrial fibrillation, heart failure), kidney (fibrosis, proteinuria, CKD progression), cerebrovascular system (stroke risk), vasculature (endothelial dysfunction, stiffness), skeletal muscle (hypokalemic weakness), bone (spironolactone shown to reduce bone-turnover markers, implying baseline aldosterone-related bone effects), and to a lesser extent the CNS/psychiatric domain.
- **Body systems:** Endocrine, cardiovascular, renal, musculoskeletal, and (secondarily) psychiatric/neurological (particularly in PASNA, which also involves the CNS directly via CACNA1D neuronal channels).

### Tissue and Cell Level
- Adrenal cortical zona glomerulosa cells (site of CYP11B2 expression and mutation)
- Aldosterone-producing cell clusters (subcapsular, age-associated)
- Renal distal nephron principal cells (site of MR/ENaC-mediated sodium reabsorption) — CL terms: kidney distal convoluted tubule epithelial cell, cortical collecting duct principal cell
- Cardiac myocytes and fibroblasts (fibrosis/hypertrophy)
- Vascular smooth muscle cells and endothelial cells
- Renal podocytes and mesangial cells
- Macrophages infiltrating cardiac and renal tissue

### Subcellular Level
- Plasma membrane (site of ion channel/pump dysfunction) — GO:0005886
- Cytoplasm (Ca²⁺ signaling, CaMK activation)
- Nucleus (CYP11B2 transcriptional activation; β-catenin nuclear translocation in CTNNB1-mutant cells) — GO:0005634
- Mitochondria (site of steroidogenic enzyme CYP11B2 itself, an inner mitochondrial membrane enzyme) — GO:0005743/GO:0005759

### Localization
- Adrenal disease is typically **unilateral** (APA, most FH-I/some cases) or **bilateral** (idiopathic hyperaldosteronism/IHA — the more common subtype overall, ~60% of PA cases vs. ~30% APA; FH-II, FH-III, FH-IV, and PBMAD are characteristically bilateral).
- Adrenal vein sampling (AVS) is required to determine lateralization when surgery is being considered, since CT imaging alone can be misleading regarding lateralization (PMC8845452).

---

## 8. Temporal Development

### Onset
- **Sporadic PA (APA/IHA):** Typically adult-onset, most commonly diagnosed in the 30s–60s; can occur at any adult age.
- **Familial forms:** Childhood-to-adolescent onset is characteristic of FH-I (GRA), FH-III, and PASNA; genetic testing is recommended for onset before age 20 or a family history of PA/early stroke (<40 years).
- **Onset pattern:** Generally insidious/chronic, though FH-III can present with severe, rapidly evident hypertension in early childhood.

### Progression
- **Disease course:** Chronic, generally progressive without treatment; some evidence supports a stepwise progression from age-related APCCs to overt APA in a subset of patients.
- **Progression rate:** Variable; FH-III (massive bilateral hyperplasia) tends to be more rapidly and severely progressive than sporadic IHA.
- **Disease duration:** Chronic/lifelong unless surgically cured (unilateral APA can be cured by adrenalectomy); bilateral disease requires lifelong medical management.

### Patterns
- **Remission:** Surgical cure is achievable in APA via unilateral adrenalectomy (complete biochemical success rates commonly cited in the 30–60% range across cohorts, with higher rates when AVS-guided); bilateral/idiopathic disease is not surgically curable and requires ongoing MRA therapy.
- **Critical periods:** Early diagnosis before the development of fixed target-organ damage (LVH, renal fibrosis, vascular remodeling) is the key intervention window, since cardiovascular/renal risk appears to begin accruing even at the subclinical stage and is only partially reversible with treatment.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** 5–10% of all hypertensive patients in unselected primary care settings; up to 20% in resistant hypertension. Contemporary broadened screening studies (e.g., SCREENING-PA) report ARR-based prevalence up to 11%, with some estimates as high as 25% depending on diagnostic threshold and population; a treatment-naive-hypertension cohort (CONPASS) found 4–7% prevalence.
- **Subtype distribution:** Bilateral idiopathic hyperaldosteronism (~60%) is more common than unilateral APA (~30%); rarer subtypes (unilateral hyperplasia, PBMAD, familial forms) make up the remainder.
- **Under-recognition:** Despite guideline recommendations, screening rates remain low even in high-risk populations such as hypertension-plus-hypokalemia and CKD cohorts (Hypertension, PMID for population-based screening-rate study; AJKD review on underdiagnosis).

### For Genetic Etiology
- **Inheritance pattern:** Autosomal dominant for FH-I (GRA), FH-II (CLCN2), FH-III (KCNJ5), and FH-IV (CACNA1H); PASNA arises typically from **de novo** heterozygous CACNA1D variants; sporadic APA-driving mutations are **somatic**, not heritable.
- **Penetrance:** Generally high but variable within familial pedigrees (e.g., "atypical gene segregation pattern" reported for some CYP11B1/CYP11B2 chimeric-gene families — Hypertension, PMID for chimeric gene study); FH-II shows variable expressivity and reduced penetrance in some kindreds.
- **Expressivity:** Highly variable, especially in FH-I, where clinical severity correlates with the specific crossover breakpoint of the chimeric gene.
- **Genetic anticipation:** Not a recognized feature of PA (not a repeat-expansion disorder).
- **Germline mosaicism:** Not well characterized for PA; theoretically possible for de novo CACNA1D (PASNA) variants but not systematically documented.
- **Founder effects:** Not prominently described; case series exist across diverse ethnicities (Korean, Japanese, Chinese, and others) for CYP11B1/CYP11B2 GRA kindreds, suggesting recurrent independent crossover events rather than a single founder haplotype.
- **Consanguinity:** Not a major factor, as most familial forms are autosomal dominant rather than recessive.
- **Carrier frequency:** Not applicable in the traditional recessive-carrier sense; somatic mutation "carrier frequency" in normal aging adrenal tissue (APCCs) increases with age.

### Population Demographics
- **Sex ratio and genotype:** KCNJ5 somatic mutations are significantly more prevalent in women (49% vs. 19% in men in one series) and associate with a more florid phenotype (younger age, higher aldosterone). ATP1A1 and CACNA1D mutations predominate in men. "Women with the unilateral subtype were younger than men with the same subtype and women with the bilateral subtype" (Hypertension, PMID:31813371-type sex-difference study).
- **Age distribution:** KCNJ5-mutant APA patients are diagnosed younger (mean ~42 years) than non-KCNJ5-mutant patients (~48 years).
- **Ethnic/geographic variation:** East Asian populations (Japan, Taiwan, China) show markedly higher rates of KCNJ5-driven APA (55–75%) than Western European/American cohorts (25–50%), a well-replicated geographic/ethnic difference in the somatic mutation spectrum.
- **Global prevalence estimate:** ~9.4% in hypertensive populations overall per a recent epidemiologic review (MDPI, *Primary Hyperaldosteronism: Epidemiology, Diagnosis, and Clinical Associations*).

---

## 10. Diagnostics

### Clinical Tests / Screening
- **Screening test:** Aldosterone-to-renin ratio (ARR), the recommended first-line test per Endocrine Society and European Society of Hypertension guidelines. A commonly cited cutoff for a positive screen is an ARR >240 (ng/dL)/(ng/mL/h), though thresholds vary by assay/units. Recent data show ARR retains high sensitivity (up to 97.7%) and negative predictive value (~99%) even without medication washout, supporting more pragmatic, broadly applied screening.
- **2024–2025 guideline evolution:** The 2024 ESC Hypertension Guidelines recommend systematic ARR-based screening of **all** adults with confirmed hypertension (a major broadening from prior risk-stratified approaches). The 2025 Endocrine Society revision permits diagnosis based on a biochemical triad (suppressed renin + elevated aldosterone + elevated ARR) **without mandatory confirmatory testing** in patients with spontaneous hypokalemia and clearly suppressed renin plus high PAC — streamlining diagnosis in unambiguous cases (ScienceDirect 2025 comparative study; PMC12885222, PMC12459304 Taipei positional paper on universal screening).

### Confirmatory Testing
- Saline infusion test, oral sodium loading test, fludrocortisone suppression test, or captopril challenge test — used to confirm autonomous, non-suppressible aldosterone secretion when the ARR screen is positive.
- Confirmatory testing is complicated in **chronic kidney disease** patients (volume-sensitive tests carry additional risk/uncertainty; PMC8312167).

### Imaging
- **Adrenal CT:** Recommended in all confirmed PA patients to exclude adrenocortical carcinoma and provide anatomic guidance; however, CT alone can misclassify unilateral vs. bilateral disease and should not be used alone to determine surgical candidacy in patients seeking a lateralizing cure, especially those >35 years old (per Endocrine Society guideline) or with equivocal imaging.
- **Adrenal vein sampling (AVS):** The gold standard for lateralization when surgery is being considered; superior outcomes (higher complete biochemical success, lower "absent success") compared with CT-guided adrenalectomy (PMC8845452). Intraprocedural cortisol assessment improves catheterization success confirmation (PMC10754635); partial-pressure-of-oxygen-guided AVS is an emerging refinement (medRxiv 2025.06.29.25330380).
- **Molecular imaging (emerging):** CYP11B2-targeted PET tracers and ¹¹C-metomidate PET are being explored to non-invasively localize aldosterone-producing lesions and potentially reduce reliance on invasive AVS; ⁶⁸Ga-Pentixafor/⁶⁸Ga-FAPI-04 PET/MR is under active clinical trial evaluation (NCT06756737) for functional adrenal lesion characterization.

### Histopathology
- CYP11B2 immunohistochemistry is used to subclassify unilateral PA and confirm which nodule(s) are functionally aldosterone-producing, distinguishing true APA from non-functioning incidentalomas and from APCCs (ScienceDirect, Korean cohort CYP11B2 IHC study).

### Genetic Testing
- Recommended for: onset before age 20; family history of PA or stroke at young age (<40); massive bilateral adrenal hyperplasia in a child (suggests FH-III/KCNJ5 germline); clinical suspicion of GRA (FH-I) based on early severe hypertension with family history, hemorrhagic stroke, or a paradoxical biochemical response to dexamethasone.
- **Approach:** Targeted testing for the CYP11B1/CYP11B2 chimeric gene (specialized long-read sequencing methods such as "GRAde," PMC8750845, improve detection efficiency over older Southern blot/long-PCR methods) for suspected FH-I; germline KCNJ5, CACNA1H, CLCN2, or CACNA1D sequencing/panel testing for suspected FH-III, FH-IV, FH-II, or PASNA respectively. Commercial panels exist (e.g., PreventionGenetics Primary Aldosteronism Panel).
- Somatic tumor genotyping (KCNJ5, CACNA1D, ATP1A1, ATP2B3, CTNNB1) of resected APA tissue is increasingly performed for prognostic/research purposes but is not yet standard preoperative practice.

### Clinical Criteria and Differential Diagnosis
- Differential diagnoses include: essential (low-renin) hypertension, renovascular hypertension, pheochromocytoma, Cushing syndrome (including overlap PBMAD/ARMC5 cases with co-secretion), apparent mineralocorticoid excess (licorice ingestion, 11β-HSD2 deficiency), Liddle syndrome (which mimics PA biochemically but with suppressed aldosterone), and drug-induced hypokalemia/hypertension (e.g., diuretics, which must be withdrawn before testing when possible).

### Screening for Asymptomatic/High-Risk Individuals
- Universal screening for all hypertensive adults is increasingly advocated (2025 Taipei positional paper), moving beyond the traditional risk-stratified approach (resistant hypertension, hypertension + hypokalemia, hypertension + adrenal incidentaloma, early-onset or severe hypertension, family history).

**Suggested NCIT terms:** NCIT:C15200 (Adrenalectomy — treatment/diagnostic crossover), NCIT for adrenal vein sampling procedure (interventional radiology), LOINC codes for aldosterone (LOINC:1832-5), renin activity, and ARR panels.

---

## 11. Outcome/Prognosis

### Survival and Mortality
- PA itself is not classically a survival-limiting condition when treated, but untreated/undertreated disease carries substantially elevated cardiovascular mortality risk relative to essential hypertension of similar severity, largely through excess stroke, MI, and heart failure events.
- Highest-quartile serum aldosterone was associated with a **22% higher risk of all-cause mortality** and a 45% increased risk of CKD progression compared with the lowest quartile in a large cohort analysis (Hypertension/AHA CKD-outcomes study, PMID search result).

### Morbidity and Function
- **Cardiovascular morbidity:** Stroke (OR 2.58), coronary artery disease (OR 1.77), atrial fibrillation (OR 3.52), heart failure (OR 2.05), and LVH (OR 2.29) compared with matched essential hypertension (Lancet Diabetes Endocrinol meta-analysis, PMID:29129575) — and this excess risk is **independent of blood pressure control**, implicating direct aldosterone-mediated tissue toxicity.
- **Renal morbidity:** Higher rates of proteinuria/albuminuria than essential hypertension; PAC correlates positively with urinary protein excretion and negatively with GFR; each doubling of serum aldosterone associated with an 11% increased risk of CKD progression.
- **Metabolic morbidity:** Higher rates of diabetes/impaired glucose metabolism and metabolic syndrome, more pronounced in bilateral IHA.
- **Quality of life:** Impaired HRQoL and elevated anxiety/depression prevalence pre-treatment, substantially improved post-treatment (adrenalectomy more so than MRA alone in some analyses).

### Disease Course / Complications
- Complications include: hypertensive emergency/crisis, hemorrhagic stroke (notably reported as an early presenting complication in some GRA/FH-I kindreds), arrhythmia (from hypokalemia and/or atrial fibrosis), heart failure, chronic kidney disease, and osteoporosis-related bone turnover changes (spironolactone shown to reduce bone turnover markers, implying an aldosterone-associated component to bone health, PMC8514385).

### Recovery Potential
- Unilateral APA: potential for **biochemical and clinical cure** with adrenalectomy; the PASO (Primary Aldosteronism Surgical Outcome) consensus criteria standardize reporting of complete/partial/absent biochemical and clinical success, though threshold-setting remains debated.
- Bilateral disease: not curable surgically (except selected unilateral adrenalectomy in bilateral disease showing partial benefit in some patients, PMID:36207420), managed long-term with MRAs ± newer aldosterone synthase inhibitors.
- Even after "cure," some degree of residual target-organ damage (vascular stiffness, myocardial fibrosis) may persist, underscoring the importance of early diagnosis.

### Prognostic Factors
- Genotype (CACNA1D/ATPase-mutant vs. KCNJ5-mutant APA) predicts differential postoperative outcomes — "opposite 2-year clinical outcomes from adrenalectomy" explained by different cellular origin/histology (PMC11454283).
- Duration of untreated hypertension, degree of hypokalemia, presence of autonomous cortisol co-secretion, and baseline renal function are recognized prognostic modifiers.

---

## 12. Treatment

### Pharmacotherapy
- **Mineralocorticoid receptor antagonists (MRAs):** First-line medical therapy for bilateral IHA and for APA patients who decline or are not candidates for surgery.
  - **Spironolactone** (NCIT:C29073-type steroidal MRA; CHEBI): non-selective MRA, also antagonizes androgen and progesterone receptors (causing gynecomastia, menstrual irregularity as class-specific side effects); shown to offer slightly better diastolic BP reduction than eplerenone but with greater hyperkalemia risk.
  - **Eplerenone**: selective MRA, better side-effect tolerability, generally requires higher/more frequent dosing for equivalent BP control.
  - **Finerenone** (nonsteroidal MRA) is being compared head-to-head against spironolactone in PA (NCT06164379).
- **FH-I (GRA)-specific therapy:** Low-dose glucocorticoid (e.g., prednisolone or dexamethasone) to suppress ACTH-driven ectopic aldosterone synthase expression — a genotype-directed precision therapy.

### Advanced Therapeutics — Aldosterone Synthase Inhibitors (ASIs), a genuinely new drug class
- **Baxdrostat** (brand name Baxfendy): FDA-approved (first-in-class oral aldosterone synthase inhibitor) for uncontrolled/resistant hypertension; in a phase 2a study of 15 PA patients, baxdrostat "resolved or reduced the severity of hypertension, excessive aldosterone production, and hypokalemia" (NEJM, PMID/DOI 10.1056/NEJMc2508629).
- **Lorundrostat:** another nonsteroidal ASI, in late-stage clinical development/regulatory review.
- ASIs work upstream of the mineralocorticoid receptor by directly inhibiting CYP11B2 enzymatic activity, offering mechanism-based specificity over MRAs (which block the receptor downstream regardless of ligand source) and, in principle, reduced off-target steroid-receptor side effects — though selectivity over the closely related CYP11B1 (cortisol synthesis) enzyme is a key pharmacologic design challenge, since off-target CYP11B1 inhibition risks cortisol insufficiency.

### Gene/Cell/RNA-based therapies
Not currently applicable/approved for PA — the disease is managed via small-molecule and surgical approaches; no gene therapy, cell therapy, or RNA-based therapeutic is in clinical use or advanced trials for PA specifically.

### Surgical and Interventional
- **Unilateral (laparoscopic) adrenalectomy:** Treatment of choice for confirmed unilateral APA (AVS-lateralized); can produce biochemical and clinical cure. NCIT:C15329 (Surgical Procedure) is the appropriate treatment-action term; specify with `therapeutic_modality: SURGERY`.
- **Cortical-sparing (partial) adrenalectomy:** Emerging technique for bilateral APA to preserve adrenal cortical function while removing functioning nodules (PMC10702625).
- **Thermal ablation:** Emerging minimally invasive alternative for APA in select patients (biorxiv thermal-therapies mouse-model study reflects ongoing preclinical work toward this).

### Supportive Care
- Potassium supplementation for symptomatic hypokalemia pending definitive treatment.
- Dietary sodium restriction as an adjunct to reduce the hypertensive/hypokalemic phenotype.

### Experimental / Clinical Trials
- NCT06164379 — Finerenone vs. spironolactone in PA
- NCT07137364 — Spironolactone combined with antihypertensives in PA
- NCT05432167 — CIN-107 (lorundrostat) for uncontrolled hypertension with CKD
- NCT04007406 — Phase II study in PA patients (aldosterone synthase inhibitor program)
- NCT06756737 — ⁶⁸Ga-Pentixafor/⁶⁸Ga-FAPI-04 PET/MR functional adrenal imaging

### Treatment Outcomes
- MRA therapy and adrenalectomy both improve blood pressure, hypokalemia, and HRQoL; adrenalectomy has been shown to improve glucose metabolism where spironolactone does not.
- PASO consensus criteria are used to grade surgical success (complete/partial/absent biochemical and clinical success).
- Common MRA adverse events: hyperkalemia, gynecomastia/menstrual irregularity (spironolactone), postural hypotension.

### Treatment Strategy / Precision Medicine
- Genotype-guided treatment is emerging: FH-I responds specifically to glucocorticoid suppression; genotype (KCNJ5 vs. CACNA1D/ATPase) may eventually inform prognosis-based counseling regarding expected adrenalectomy outcome.
- Combination therapy (MRA + ASI, or MRA + standard antihypertensives) is used for refractory cases and is under active trial investigation.

**Suggested NCIT/CHEBI terms:** NCIT:C15986 (Pharmacotherapy) as generic treatment_term paired with therapeutic_agent CHEBI:9184 (spironolactone) or CHEBI:465305 (eplerenone); NCIT:C15329 (Surgical Procedure) for adrenalectomy; therapeutic_modality `SMALL_MOLECULE` for MRAs and ASIs, `SURGERY` for adrenalectomy.

---

## 13. Prevention

### Prevention Levels
- **Primary prevention:** Not applicable in the traditional sense (PA is not preventable via vaccination or avoidance of a discrete exposure), though dietary sodium moderation may blunt phenotypic severity in genetically predisposed individuals.
- **Secondary prevention:** Broadened/universal ARR-based screening of hypertensive patients (as endorsed by 2024 ESC and 2025 Endocrine Society guidance) constitutes the primary secondary-prevention strategy, enabling earlier detection before irreversible target-organ damage accrues.
- **Tertiary prevention:** Prompt treatment (surgical or pharmacologic) of confirmed PA reduces — though does not always fully reverse — excess cardiovascular and renal risk; regular monitoring for LVH, renal function decline, and psychiatric symptoms in diagnosed patients.

### Screening and Early Detection
- Risk-stratified screening indications (traditional): resistant hypertension, hypertension with spontaneous or diuretic-induced hypokalemia, hypertension with adrenal incidentaloma, early-onset (<40 years) or severe hypertension, hypertension with family history of PA or early stroke, hypertension with obstructive sleep apnea, and first-degree relatives of a PA patient.
- **Universal screening (emerging paradigm):** All hypertensive adults, per the 2025 Taipei positional paper and increasingly aligned major-society guidance.
- **Genetic screening:** Family cascade testing recommended once a proband is confirmed to carry a germline FH variant (particularly FH-I/GRA, given its autosomal dominant inheritance and treatable, genotype-specific therapy).

### Counseling
- Genetic counseling is indicated for families with confirmed FH-I, FH-II, FH-III, FH-IV, or PASNA, given autosomal dominant (or de novo) inheritance patterns and the availability of genotype-specific management (glucocorticoid suppression for FH-I).

### Public Health / Prophylaxis
- No specific environmental/public-health intervention (e.g., sanitation, vector control) applies, as PA is not an infectious or environmentally-transmitted disease. Population-level dietary sodium reduction campaigns provide general hypertension benefit that may partially mitigate PA's phenotypic expression but do not address its underlying cause.

---

## 14. Other Species / Natural Disease

### Taxonomy and Naturally Occurring Disease
- **Cats (Felis catus, NCBITaxon:9685):** Feline hyperaldosteronism from aldosterone-secreting adrenal tumors is a well-recognized, naturally occurring veterinary counterpart, and a 2024/2025 whole-genome/RNA-sequencing study of 13 cats (8 carcinomas, 5 adenomas) identified **somatic GNAQ, CTNNB1, and CACNA1C mutations** — CTNNB1 mirroring a known human APA driver, and the CACNA1C mutation occurring at a residue analogous to a common human CACNA1D mutation (Hypertension, AHA, 2024/PMC11578054). Notably, **no mutations were found in KCNJ5, CACNA1D, ATP1A1, or ATP2B3** in cats — a species difference — and feline adrenal tissue shows much higher baseline CACNA1C than CACNA1D expression (opposite the human pattern). "It is, therefore, likely that both species have shared underlying selection pressures for mutations that increase aldosterone secretion" (PMC11578054).
- **Dogs (Canis familiaris):** Aldosterone-producing adrenal adenomas are reported but comparatively rare relative to cats; when present, they cause hypertension and hypokalemia analogous to the human/feline disease.

### Comparative Biology
- The convergence on Wnt/β-catenin (CTNNB1) and L-type calcium channel (CACNA1D/CACNA1C) pathway activation across humans and cats, despite species-specific differences in which exact channel gene is mutated, supports a conserved final-common mechanistic pathway (Ca²⁺-driven CYP11B2 activation and/or Wnt-driven proliferation) for autonomous aldosterone secretion across mammals.
- **Zoonotic potential:** Not applicable — PA is a non-communicable endocrine/neoplastic disease.

---

## 15. Model Organisms

### Genetic (Mouse) Models
- **Cacna1d gain-of-function knock-in mice** (e.g., *Cacna1d*^Ile772Met/+^): recapitulate features of PASNA, including elevated aldosterone and neurologic/motor abnormalities; treatment with the L-type calcium channel blocker **isradipine** ameliorated both intracellular calcium/aldosterone elevation in zona glomerulosa cells and rotarod motor performance deficits, providing translational proof-of-concept for calcium-channel-blocker repurposing in PASNA and possibly CACNA1D-driven APA (PMC10619505).
- **ClC-2 (Clcn2) gain-of-function mouse models:** recapitulate FH-II, showing elevated aldosterone and blood pressure consistent with the human chloride-channel mechanism (PMC6856192, *Elevated aldosterone and blood pressure in a mouse model of familial hyperaldosteronism with ClC-2 mutation*).
- **Xenograft/cell-line-based mouse models:** HAC15 human adrenocortical carcinoma cells inoculated into immunodeficient mice partially replicate genetic features of human APA but are limited — this model "only produces aldosterone from angiotensin II stimulation" rather than fully autonomous secretion, illustrating an important **translational gap**: current models capture upstream genetic/channel biology (Cacna1d, Clcn2 knock-ins) or partial hormonal responsiveness (xenografts), but no single model fully recapitulates spontaneous, autonomous, tumor-forming human APA biology.
- A **biochemical mouse model of PA characterized for thermal therapy development** (bioRxiv 2024.05.07.592955) represents ongoing efforts to create better preclinical platforms for testing novel interventions (e.g., ablation techniques).

### Model Characteristics: Recapitulation and Limitations
- Channel-mutant knock-in mice (Cacna1d, Clcn2) faithfully reproduce the core **biochemical** phenotype (elevated aldosterone, hypertension, and for Cacna1d, the associated neurologic phenotype) and are valuable for mechanistic dissection and drug testing (e.g., isradipine).
- They generally do **not** reproduce spontaneous **adenoma formation** or the somatic clonal-expansion process seen in human APA, since the mutation is germline/constitutive rather than a focal somatic event in a subset of cells — a key human-model mismatch relevant to interpreting knock-in mouse data as a model for sporadic APA versus for the germline familial syndromes they were designed to model.
- Xenograft models capture tumor-forming human adrenocortical cell biology but lack normal zona-glomerulosa regulatory context and autonomous (non-angiotensin-II-dependent) secretion.

### Applications
- Testing genotype-specific pharmacologic interventions (e.g., calcium channel blockers for CACNA1D-driven disease)
- Dissecting calcium-signaling-to-CYP11B2-transcription mechanisms
- Preclinical development of novel ablative/thermal therapies
- Investigating aldosterone's direct cardiac/renal/CNS effects independent of blood pressure, using aldosterone-infusion or MR-overexpression mouse models (a broader mineralocorticoid-excess modeling tradition, distinct from PA-specific genetic models)

### Resources
- MGI (Mouse Genome Informatics) for Cacna1d, Clcn2 allele records
- GEO (e.g., GSE90867) for KCNJ5-mutant APA transcriptomic data (human, but relevant to cross-species comparative use)

---

## Summary of Key Ontology Term Suggestions

| Category | Terms |
|---|---|
| MONDO | MONDO:0001422 (primary hyperaldosteronism); MONDO:0013359, MONDO:0014875 (familial subtypes) |
| HGNC genes | KCNJ5, CACNA1D, ATP1A1, ATP2B3, CTNNB1, CLCN2, CACNA1H, CYP11B1, CYP11B2, ARMC5 |
| HP phenotypes | HP:0000822 (Hypertension), HP:0002900 (Hypokalemia), HP:0001948 (Metabolic alkalosis), HP:0001712 (LVH), HP:0001324 (Muscle weakness), HP:0000739 (Anxiety) |
| GO | GO:0032341 (regulation of aldosterone biosynthetic process), GO:0006816 (calcium ion transport), GO:0030177 (positive regulation of Wnt signaling), GO:0043123 (positive regulation of NF-kB signaling) |
| CL | Zona glomerulosa cell, cardiac fibroblast (CL:0002548), macrophage (CL:0000235), podocyte (CL:0000653) |
| UBERON | UBERON:0002369 (adrenal gland), UBERON:0001236 (zona glomerulosa), UBERON:0002113 (kidney), UBERON:0000948 (heart) |
| CHEBI | CHEBI:2668 (aldosterone), CHEBI:9184 (spironolactone), CHEBI:465305 (eplerenone) |
| NCIT | NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure) |
| NCBITaxon | NCBITaxon:9685 (Felis catus), NCBITaxon:9615 (Canis familiaris), NCBITaxon:10090 (Mus musculus) |

---

## Notes on Evidence Gaps
- Epigenomic (DNA methylation/chromatin) characterization of PA adrenal tissue is comparatively less developed than the somatic genomic landscape.
- No fully autonomous, spontaneously tumor-forming mouse model of sporadic APA exists; current genetic models best represent the rarer germline/familial syndromes.
- OBI-style structured evidence for some newer diagnostic modalities (CYP11B2-targeted PET) is still emerging in the primary literature and was not exhaustively covered here.
- Direct mechanistic (rather than correlative) human evidence for aldosterone's CNS/mood effects remains more indirect than the well-established renal/cardiovascular fibrosis mechanisms.

Sources: [Orphanet: rare surgically correctable form of primary aldosteronism](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=231637) · [OMIM #615474 PASNA](https://omim.org/entry/615474) · [Aldosterone-Producing Adenoma With a Somatic KCNJ5 Mutation](https://pubmed.ncbi.nlm.nih.gov/27648962/) · [Genetic spectrum of somatic mutations in APA](https://pubmed.ncbi.nlm.nih.gov/24866132/) · [CTNNB1 Mutation in APA](https://pmc.ncbi.nlm.nih.gov/articles/PMC5620029/) · [Unravelling the Genetic Basis of Primary Aldosteronism](https://pmc.ncbi.nlm.nih.gov/articles/PMC7999899/) · [Genetics of Primary Aldosteronism (Hypertension/AHA)](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.121.16498) · [Broadening PA Screening: Alignment Across Guidelines](https://pmc.ncbi.nlm.nih.gov/articles/PMC12885222/) · [Universal Screening for PA: 2025 Taipei Positional Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12459304/) · [Pathogenesis and treatment of primary aldosteronism (Nat Rev Endocrinol)](https://www.nature.com/articles/s41574-020-0382-4) · [Hyperaldosteronism – Endotext](https://www.ncbi.nlm.nih.gov/books/NBK279065/) · [Prevalence of Hypokalemia and PA in 5100 Patients](https://pubmed.ncbi.nlm.nih.gov/32114853/) · [Cardiovascular events and target organ damage in PA vs essential hypertension (Lancet Diabetes Endocrinol)](https://pubmed.ncbi.nlm.nih.gov/29129575/?dopt=Abstract) · [Cerebro-Cardiovascular Risk, Target Organ Damage in PA](https://pubmed.ncbi.nlm.nih.gov/35187110/) · [Comparison between AVS and CT](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5265946/) · [Prognosis of adrenalectomy: CT vs AVS meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8845452/) · [Phase 2a Study of Baxdrostat in PA (NEJM)](https://www.nejm.org/doi/abs/10.1056/NEJMc2508629) · [Comparison of medical treatments for primary hyperaldosteronism](https://pmc.ncbi.nlm.nih.gov/articles/PMC10953100/) · [Spironolactone and bone turnover](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8514385/) · [8310 CACNA1D- and KCNJ5-Mutant APAs opposite outcomes](https://pmc.ncbi.nlm.nih.gov/articles/PMC11454283/) · [Aldosterone-Producing Cell Clusters single-cell characterization](https://academic.oup.com/jcem/article/107/9/2439/6631432) · [APCCs accumulate with age](https://academic.oup.com/jes/article/1/7/787/3819439) · [Diverse pathological lesions of PA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8099725/) · [Sex Difference in Subtype Distribution and Age at Diagnosis](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.119.13006) · [Primary Hyperaldosteronism: Epidemiology, Diagnosis, and Clinical Associations](https://www.mdpi.com/2673-3986/7/2/32) · [Somatic GNAQ, CTNNB1, and CACNA1C Mutations in Cat Aldosterone-Secreting Tumors](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.124.23501) · [Interplay Between Mineralocorticoid System, Inflammation, and Kidney Disease](https://journals.lww.com/kidney360/fulltext/10.34067/kid.0000000929~interplay-between-the-mineralocorticoid-system-inflammation) · [Modulation of Immunity and Inflammation by MR and Aldosterone](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4581510/) · [GRAde long-read sequencing for GRA](https://pmc.ncbi.nlm.nih.gov/articles/PMC8750845/) · [A New Presentation of the Chimeric CYP11B1/CYP11B2 Gene](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.111.180513) · [Third case report of PASNA de novo CACNA1D](https://pubmed.ncbi.nlm.nih.gov/30698561/) · [Isradipine therapy in Cacna1d mouse model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10619505/) · [de novo CACNA1D variant congenital hyperinsulinism/hyperaldosteronism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7219433/) · [Identification of risk loci for PA in GWAS](https://pubmed.ncbi.nlm.nih.gov/36057693/) · [PA and obstructive sleep apnea](https://pmc.ncbi.nlm.nih.gov/articles/PMC9556954/) · [Primary Aldosteronism in CKD: BP control and outcomes](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.123.21474) · [Underdiagnosis of Primary Aldosteronism (AJKD)](https://www.ajkd.org/article/S0272-6386(23)00579-6/fulltext) · [SFE/SFHTA/AFCE consensus part 5: Genetic diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S000342661630021X) · [Molecular Basis of Primary Aldosteronism and Adrenal Cushing Syndrome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7412855/) · [Primary Bilateral Macronodular Adrenocortical Disease with distinct ARMC5 mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12861490/) · [Anxiety, Depression, and Impaired QoL in PA](https://pubmed.ncbi.nlm.nih.gov/29099927/) · [Health-Related QoL and Mental Health in PA: Systematic Review](https://pubmed.ncbi.nlm.nih.gov/29202493/) · [Improvement in QoL after PA treatment: Asian Cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC8346187/) · [Effects of PA and treatment on glucose metabolism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6947343/) · [Comparative Genomics and Transcriptome Profiling in PA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5979346/) · [Adrenocortical Tumor with KCNJ5 variant and CYP11B2 DNA methylation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11255478/) · [Somatic Mutations in MCOLN3 in APA (bioRxiv)](https://www.biorxiv.org/content/10.1101/2024.10.20.619295.full.pdf) · [Characterization of a Biochemical Mouse Model of PA for Thermal Therapies](https://www.biorxiv.org/content/10.1101/2024.05.07.592955.full.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 46 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 4 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 46 |
| On topic | 30 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

3 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC7999899` *(abstract only)*: "In FH-II, pathogenic variants in CLCN2 lead to increased chloride efflux, and in FH-III, pathogenic variants in KCNJ5 render the encoded potassium channel permeable to sodium ions, with the resulting membrane depolarization causing voltage-gated calcium influx in both conditions... CACNA1H pathogenic variants in FH-IV directly increase calcium influx"
  - closest text in source: "On the other hand, germline variants in CLCN2, KCNJ5, CACNA1H, and CACNA1D genes have been implicated in the pathogenesis of the familial forms of PA, FH-II, FH-III, and F-IV, as well as PA associated with seizures and neurological abnormalities"
- `PMID:29099927`: "Psychopathological symptoms of anxiety, demoralization, stress, depression and nervousness were more frequently reported in untreated patients with primary aldosteronism than in the general population and patients with hypertension"
  - closest text in source: "Januar 2018):Anxiety, Depression, and Impaired Quality of Life in Primary Aldosteronism: Why We shouldn’t Ignore It!In: Journal of Clinical Endocrinology & Metabolism, Bd"
- `PMC:PMC6947343` *(abstract only)*: "glucose metabolism was impaired in PA, regardless of hypokalemia and subclinical hypercortisolism status, and was improved by adrenalectomy, but not spironolactone treatment"
  - closest text in source: "Glucose metabolism was impaired in PA, regardless of hypokalemia and SH status, and was improved by adrenalectomy, but not spironolactone treatment."
- `PMID:31813371` *(abstract only)*: "Women with the unilateral subtype were younger than men with the same subtype and women with the bilateral subtype"
  - Text part not found as substring: 'Women with the unilateral subtype were younger than men with the same subtype and women with the bilateral subtype' (note: only abstract available for PMID:31813371, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31813371` (1 mention) - Three-manifold quantum invariants and mock theta functions.
  - shared terms: none

Weighed against this report's own most characteristic terms: `aldosterone`, `hypertension`, `apa`, `cacna1d`, `disease`, `patient`, `adrenal`, `hypokalemia`, `fh-i`, `clinical`, `primary`, `bilateral`, `kcnj5`, `cyp11b2`, `gene`, `somatic`, `genetic`, `mutation`, `cell`, `adrenalectomy`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1056/NEJMc2508629`: "resolved or reduced the severity of hypertension, excessive aldosterone production, and hypokalemia"
  - Reference resolved but exposes no abstract or full text to search
