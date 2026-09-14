---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-03T15:03:01.655336'
end_time: '2026-09-03T15:07:49.212521'
duration_seconds: 287.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Protein S Deficiency
  mondo_id: ''
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
  web_search_requests: 20
  num_turns: 20
  total_cost_usd: 1.0379648000000001
  session_id: eccb37f5-d277-53f4-9bc9-b541745fd0d8
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Protein S Deficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Protein S Deficiency** covering all of the
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

# Protein S Deficiency: Comprehensive Research Report

## 1. Disease Information

**Overview.** Protein S deficiency is an inherited or acquired thrombophilia caused by reduced plasma levels or functional activity of protein S, a vitamin K–dependent plasma glycoprotein that acts as a non-enzymatic cofactor for the anticoagulant proteins activated protein C (APC) and tissue factor pathway inhibitor (TFPI). Deficiency impairs down-regulation of the coagulation cascade, producing a hypercoagulable state manifesting predominantly as venous thromboembolism (VTE) — deep vein thrombosis (DVT), pulmonary embolism (PE), and superficial thrombophlebitis. A rare, severe homozygous/compound-heterozygous form causes neonatal purpura fulminans, a life-threatening disseminated microvascular thrombosis syndrome ([StatPearls, NCBI Bookshelf NBK544344](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).

**Key identifiers:**
- **OMIM (gene):** *176880 — PROS1 (protein S)
- **OMIM (phenotype, autosomal dominant/heterozygous):** #612336 — Thrombophilia due to Protein S Deficiency, Autosomal Dominant (THPH5) ([OMIM 612336](https://omim.org/entry/612336))
- **OMIM (phenotype, autosomal recessive/severe):** #614514 — Thrombophilia due to Protein S Deficiency, Autosomal Recessive (THPH6) ([OMIM 614514](https://omim.org/entry/614514))
- **Orphanet:** ORPHA:743 — Severe hereditary thrombophilia due to congenital protein S deficiency ([Orphanet 743](https://www.orpha.net/en/disease/detail/743))
- **MONDO:** MONDO:0002304
- **Disease Ontology:** DOID:2451
- **HPO (phenotype term):** HP:0004855 (Protein S deficiency)
- **ICD-10-CM:** D68.59 (Other primary thrombophilia — used for hereditary protein S deficiency)
- **Gene locus:** PROS1, chromosome 3q11.1 (HGNC:9457)

**Synonyms:** PS deficiency; hereditary/congenital protein S deficiency; THPH5 (dominant form); THPH6 (recessive/severe form); "protein S Tokushima" for the Japanese K155E/K196E variant designation.

**Evidence base note:** Much of the epidemiological and clinical literature derives from aggregated case-series, thrombophilia-clinic cohorts, and family/kindred studies rather than large population-representative EHR datasets — an important caveat given the assay/pre-analytical variability discussed in Section 10.

---

## 2. Etiology

### Causal factors

Protein S deficiency arises from two broad mechanisms:

1. **Congenital (genetic):** Heterozygous or homozygous/compound-heterozygous pathogenic variants in *PROS1*. Over 200–300+ distinct PROS1 mutations have been catalogued (StatPearls cites >200; other reviews cite >300), including missense variants (most common), nonsense variants, small insertions/deletions, splice-site variants, and large deletions spanning one or multiple exons ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-gene/PROS1/condition/Thrombophilia%20due%20to%20protein%20S%20deficiency,%20autosomal%20recessive/pathogenic); [Human Genome Variation 2024](https://www.nature.com/articles/s41439-024-00286-9)). Most loss-of-function mutations produce premature stop codons and truncated, non-secreted or non-functional protein.

2. **Acquired:** Reduced protein S levels/activity secondary to another physiologic or pathologic state — vitamin K antagonist (warfarin) therapy, vitamin K deficiency, liver disease, nephrotic syndrome (urinary protein loss), disseminated intravascular coagulation (DIC), pregnancy, oral contraceptive/estrogen or hormone-replacement therapy, systemic lupus erythematosus, HIV infection, chronic/acute infection, and myeloproliferative disorders ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/); [Medscape overview](https://emedicine.medscape.com/article/205582-overview)).

### Genetic risk factors
- **Causal PROS1 variants** — dominant heterozygous variants cause the common, milder Type I/III phenotype; biallelic (homozygous or compound heterozygous) variants cause the severe neonatal form.
- **Founder/population-specific variant:** PROS1 c.586A>G (p.Lys196Glu, "K196E"/legacy "K155E," known as "protein S Tokushima") is essentially restricted to Japanese populations, present in ~1.8% of Japanese individuals, and confers an odds ratio of 3.7–8.6 for VTE; it has not been found in Chinese, Korean, or Caucasian populations ([racial-differences PMC7695562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7695562/); [PLOS ONE 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133196)).
- **Combined/modifier genetic factors:** Co-inheritance of Factor V Leiden (FVL) with PROS1 deficiency is well documented and synergistically increases thrombosis risk (see Section 9).

### Environmental / acquired risk factors
Immobility, surgery, trauma, pregnancy/puerperium, estrogen-containing contraceptives or HRT, and long-haul travel are documented precipitants; a large kindred study found that although these factors were common, "almost half of the events were spontaneous" ([ClinVar/OMIM search summary](https://omim.org/entry/612336); [Annals of Internal Medicine 1998](https://www.acpjournals.org/doi/10.7326/0003-4819-128-1-199801010-00002)).

### Protective factors
No specific genetic or environmental protective variant/exposure for protein S deficiency was identified in the literature searched; general VTE risk-reduction measures (avoidance of estrogen therapy, maintaining mobility, prophylactic anticoagulation during high-risk periods) apply, but the review found no dedicated protective-allele literature analogous to, e.g., Factor V Leiden's population-genetics protective hypotheses.

### Gene–environment interaction
The clearest documented interaction is with exogenous estrogen (oral contraceptives, HRT, pregnancy), which itself lowers free protein S levels physiologically and is superimposed on a genetically reduced baseline, precipitating clinical thrombosis in previously asymptomatic carriers ("Protein S levels decrease in pregnancy and can fall into the abnormal-low laboratory range" — [Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/21877-protein-s-deficiency); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).

---

## 3. Phenotypes

### Phenotype categories and suggested HPO terms

| Phenotype | Type | Suggested HPO term |
|---|---|---|
| Deep vein thrombosis | Sign/laboratory-imaging | HP:0002625 (Peripheral thrombosis) / HP:0004936 (Deep venous thrombosis, if available) |
| Pulmonary embolism | Sign | HP:0004942 (Pulmonary embolism) |
| Superficial thrombophlebitis | Sign | HP:0025138 (Phlebitis) or related |
| Purpura fulminans (neonatal) | Sign, severe/congenital | HP:0025282 (Purpura fulminans) |
| Recurrent pregnancy loss | Sign | HP:0032449 (Recurrent miscarriage) |
| Cerebral venous sinus thrombosis | Sign, rare-site | HP:0006956 (Cerebral venous thrombosis, if modeled) |
| Reduced Protein S activity/antigen | Laboratory abnormality | HP:0004855 (Protein S deficiency) |
| Warfarin-induced skin necrosis | Sign, treatment complication | (no direct HP term; model as adverse-drug-reaction phenotype) |
| Post-thrombotic syndrome | Sign, sequela | HP:0025490 (if modeled) |

### Characteristics
- **Onset:** Two clearly separable onset patterns —
  - *Heterozygous/mild congenital or acquired disease:* adult-onset, with median age at first VTE around 29 years in some cohorts; "almost half of all individuals with protein S deficiency become symptomatic before age 55" ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).
  - *Homozygous/compound heterozygous severe disease:* neonatal onset, "manifests several hours to days after birth, with purpura fulminans or massive venous thrombosis" ([NORD/GARD](https://rarediseases.org/rare-diseases/protein-s-deficiency/)).
- **Severity:** Highly variable in the heterozygous form (many carriers remain asymptomatic lifelong — see penetrance below); uniformly severe and life-threatening in the biallelic neonatal form.
- **Progression:** Recurrent/relapsing pattern typical for heterozygous VTE; the neonatal form is acute and rapidly progressive without emergency plasma replacement.
- **Frequency of specific manifestations** among symptomatic patients: DVT ~74%, superficial thrombophlebitis ~72%, PE ~38% (may co-occur); "venous thromboembolism occurring in approximately 50–60% of people with protein S deficiency" who are carriers over their lifetime; involvement of cerebral, visceral, mesenteric, or axillary veins is comparatively rare ([Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/21877-protein-s-deficiency); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).
- **Penetrance:** Among heterozygous carriers, roughly 50% develop venous thromboembolism in their lifetime; 50% remain asymptomatic ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).
- **Quality of life impact:** Not extensively quantified in disease-specific QOL instruments in the literature surveyed; morbidity relates chiefly to recurrent VTE, post-thrombotic syndrome, chronic anticoagulation burden/bleeding risk, and (in severe cases) neurodevelopmental sequelae from neonatal thrombosis/hemorrhage (e.g., a reported case with in utero retinal vessel thrombosis and blindness — [OMIM 614514](https://omim.org/entry/614514)).

---

## 4. Genetic / Molecular Information

### Causal gene
- **PROS1** (Protein S), HGNC:9457, chromosome 3q11.1. OMIM *176880.

### Variant classification and types
- **Type of variants:** predominantly missense; also nonsense, small indels, splice-site, and large exonic deletions ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-gene/PROS1/condition/Thrombophilia%20due%20to%20protein%20S%20deficiency,%20autosomal%20recessive/pathogenic)).
- A 2024–2025 systematic reanalysis of 276 patients with suspected hereditary PS deficiency identified 48 distinct variants across 101 patients — 27 previously reported, 11 present in ClinVar/dbSNP without prior clinical categorization, and 10 entirely novel ([PubMed 42079676](https://pubmed.ncbi.nlm.nih.gov/42079676/)).
- Specific examples: p.Thr78Met (ClinVar RCV000197958), p.Met640Thr (RCV001211450), p.Arg355Cys (RCV000022724), p.Ser501Pro (RCV000205145), p.Val606Ile (RCV000206212), p.Leu584Arg (mesenteric/portal vein thrombosis case, [PMC10682651](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10682651/)), and c.602-2delA (splice acceptor mutation, exon 7, in a Polish VTE patient, [PMC7558706](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7558706/)).
- A stop-codon read-through variant (wobble-position A→T transversion) extends the protein by 14 amino acids before reaching a novel stop codon, illustrating an unusual loss-of-function mechanism.
- **Founder variant:** PROS1 c.586A>G p.Lys196Glu ("K196E"/"K155E," "PS Tokushima") — Japan-specific, ~1.8% allele carriage, associated with Type II-pattern deficiency (normal antigen, reduced APC-cofactor functional activity) ([ClinVar RCV000014246](https://www.ncbi.nlm.nih.gov/clinvar/RCV000014246/); [PMC6178719](https://pmc.ncbi.nlm.nih.gov/articles/PMC6178719/)).

### Functional consequence / laboratory classification (ISTH system)
Three recognized subtypes, based on total antigen, free antigen, and functional (cofactor) activity:
- **Type I:** ↓ total protein S antigen, ↓ free antigen, ↓ activity (quantitative deficiency).
- **Type II:** normal antigen levels (total and free), ↓ functional activity (qualitative/dysfunctional protein — e.g., K196E "PS Tokushima").
- **Type III:** normal total antigen, ↓ free antigen, ↓ activity (abnormal partitioning between free and C4BP-bound forms).
Type II is rare; Types I and III are the most common phenotypes clinically encountered ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK544344/)).

### Modifier genes
- **Factor V Leiden (F5 R506Q)** — most clinically significant co-inherited modifier; markedly amplifies thrombotic risk when combined with PROS1 deficiency (Section 9).

### Population allele frequency
- Founder K196E variant carrier frequency ~1.8% in Japan (estimated ~9,440 individuals homozygous in the Japanese population) ([PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133196)).
- General-population heterozygous ("partial") deficiency prevalence: 0.16–0.21% (Orphanet); blood-donor cohort estimates 0.03–0.13%, rising to 3–5% among patients selected for recurrent thrombosis/strong family history (StatPearls).

### Epigenetics / chromosomal abnormalities
No disease-specific epigenetic mechanism (DNA methylation/histone modification) or recurrent chromosomal structural abnormality was found reported for PROS1-related deficiency in the literature surveyed; the genetic architecture is single-gene Mendelian (with digenic/oligogenic modification by FVL).

---

## 5. Environmental Information

- **Pharmacologic/hormonal exposures:** Vitamin K antagonists (warfarin) directly suppress synthesis of functional (carboxylated) protein S; estrogen-containing oral contraceptives, hormone replacement therapy, and pregnancy physiologically lower free protein S and unmask latent deficiency ([Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/21877-protein-s-deficiency)).
- **Nutritional/vitamin status:** Vitamin K deficiency (malabsorption, dietary insufficiency, antibiotic-associated) reduces γ-carboxylation of protein S, lowering functional activity.
- **Hepatic and renal disease:** Liver disease reduces synthetic production; nephrotic syndrome causes urinary loss of protein S (a smaller, more easily lost molecule relative to some other coagulation factors).
- **Infectious/inflammatory triggers:** Acute infection and DIC consume and lower protein S acutely; chronic infections (e.g., HIV) are associated with acquired deficiency.
- **Autoimmune disease:** Systemic lupus erythematosus is associated with acquired protein S deficiency, sometimes compounded by antiphospholipid antibodies.
- No specific infectious pathogen causally produces the inherited disorder; infection functions as an acquired-deficiency trigger and precipitant of thrombosis, not an etiological agent of the genetic disease itself.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous (or homozygous/compound heterozygous) loss-of-function variant in **PROS1** → **reduced synthesis, secretion, or functional activity of protein S** in hepatocytes and (to a lesser extent) endothelial cells and megakaryocytes.
2. Reduced circulating free/functional protein S → **diminished APC-cofactor activity**, because protein S normally accelerates activated protein C (APC)-mediated proteolytic inactivation of factors Va and VIIIa by roughly 10-fold (a γ-carboxyglutamic-acid–dependent function requiring the Gla domain) ([ASH Blood 2011](https://ashpublications.org/blood/article/117/24/6685/22285/Activated-protein-C-cofactor-function-of-protein-S)).
3. In parallel, reduced protein S → **diminished TFPIα cofactor function**: the Laminin-G1 (LG1) domain of protein S binds TFPIα's K3 domain and enhances TFPIα-mediated inhibition of factor Xa 4- to 10-fold by promoting TFPIα association with phospholipid membrane surfaces ([AHA journals ATVB 2008](https://www.ahajournals.org/doi/10.1161/atvbaha.108.177436); [Science Advances 2024](https://www.science.org/doi/10.1126/sciadv.adk5836)). A 2024 in vivo study found "TFPIα anticoagulant function is highly dependent on protein S in vivo," underscoring this as a major, independent (APC-free) anticoagulant pathway.
4. Loss of these two cofactor functions, plus loss of protein S's **direct inhibition of the intrinsic tenase (FVIIIa–FIXa) and prothrombinase (FVa–FXa) complexes**, leads to **failure to down-regulate thrombin generation**, particularly at sites of vascular injury.
5. Unchecked thrombin generation → **excess fibrin formation and platelet activation**, tipping local hemostatic balance toward pathological clot formation → **venous thrombus formation** (most often in the deep veins of the lower extremity).
6. A propagating or embolizing thrombus → **pulmonary embolism**, or (in unusual/high-risk sites) **cerebral venous sinus, mesenteric, portal, or axillary vein thrombosis**.
7. In the rare biallelic/severe form, near-total absence of protein S (plasma levels <1% reported in purpura-fulminans infants) → **diffuse microvascular thrombosis in skin and viscera within hours to days of birth**, producing purpura fulminans, DIC, and in some cases intracranial hemorrhage or in-utero ocular vascular thrombosis causing blindness ([OMIM 614514](https://omim.org/entry/614514); [PubMed 2231208](https://pubmed.ncbi.nlm.nih.gov/2231208/)).
8. **Branch — Warfarin-induced skin necrosis:** in a protein-deficient patient started on warfarin without heparin bridging, the drug's early, more rapid suppression of already-low protein C/protein S relative to slower-acting procoagulant factor depletion transiently amplifies the pre-existing procoagulant tilt → **microvascular thrombosis in skin/subcutaneous fat**, producing painful purpuric/necrotic skin lesions; this is a recognized (though for protein S specifically, less common than for protein C deficiency) risk. ("Warfarin-induced skin necrosis has been associated with protein C deficiency but only rarely reported in patients with a deficiency of protein S" — [PubMed 1427456](https://pubmed.ncbi.nlm.nih.gov/1427456/); [PubMed 9885367](https://pubmed.ncbi.nlm.nih.gov/9885367/)).
9. **Branch — Combined defect amplification:** co-inheritance of Factor V Leiden (which itself impairs APC-mediated FVa inactivation) with protein S deficiency compounds the loss of APC-pathway regulation through two independent mechanisms simultaneously, synergistically (not merely additively) raising thrombotic risk (Section 9) — a demonstrated "two-hit" model.

### Molecular pathways
KEGG/Reactome-relevant pathways: **Complement and coagulation cascades** (KEGG hsa04610); **Regulation of Complement cascade / Protein C activation**; **Formation of Fibrin Clot (Clotting Cascade)** in Reactome; the **APC-Protein S** and **TFPI-Protein S** anticoagulant sub-pathways.

### Protein structure/dysfunction
Protein S is a multidomain, vitamin K–dependent glycoprotein comprising:
- An N-terminal **Gla domain** (10 γ-carboxyglutamic acid residues, vitamin K–dependently modified — required for phospholipid membrane binding and, notably, for APC-cofactor activity via a specific Gla residue) ([ASH Blood 2011](https://ashpublications.org/blood/article/117/24/6685/22285/Activated-protein-C-cofactor-function-of-protein-S)).
- A **thrombin-sensitive region (TSR)**.
- **Four tandem EGF-like domains.**
- A C-terminal **SHBG-like domain** containing two **Laminin G-type (LG1, LG2) domains**, together constituting >55% of the mature protein's length; the LG1 domain mediates TFPIα cofactor activity and is competitively regulated by C4BP binding, while the first LG domain also binds/activates the receptor tyrosine kinase Tyro3 for non-hemostatic (efferocytosis/immune) signaling ([Blood Advances 2022](https://ashpublications.org/bloodadvances/article/6/2/704/477773/Laminin-G1-residues-of-protein-S-mediate-its-TFPI); [ScienceDirect 2022](https://www.sciencedirect.com/science/article/pii/S2405580822000632)).
- **C4b-binding protein (C4BP) partitioning:** ~60–70% of circulating protein S is bound in a high-affinity 1:1 complex with the C4BP β-chain (via both LG domains) and is anticoagulantly inactive; only the ~30–40% **free** fraction is functionally active as an APC/TFPI cofactor. This is the molecular basis of Type III deficiency, in which free-fraction partitioning is abnormal despite normal total antigen.

### Cellular processes / tissue-level consequences
Endothelial dysfunction and loss of local anticoagulant surface regulation at sites of venous stasis/injury; downstream fibrin deposition and, in purpura fulminans, dermal/subcutaneous ischemic necrosis from occlusive microvascular thrombosis.

### Advanced/omics findings
The literature reviewed did not surface disease-specific transcriptomic, proteomic, or single-cell datasets specific to PROS1 deficiency beyond conventional coagulation-assay and genetic-variant characterization; most mechanistic insight comes from biochemical/structural studies of protein S domains and from murine genetic models (Section 15).

**Suggested ontology terms:** GO:0030195 (negative regulation of blood coagulation); GO:0072378 (blood coagulation, fibrin clot formation); GO:0031093 (platelet alpha granule lumen, n/a — not directly relevant); CL:0000182 (hepatocyte, site of synthesis); UBERON:0001997 (vein, site of thrombosis); CHEBI:29108 (calcium ion, cofactor for Gla-domain phospholipid binding, if relevant to a molecular node).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Cardiovascular system — primarily the **venous** circulation. Primary sites: deep veins of the lower extremities (UBERON:0001474/lower limb vein), pulmonary vasculature (embolic secondary involvement), superficial veins. Less common: cerebral venous sinuses, portal/mesenteric veins, axillary veins. In neonatal purpura fulminans, skin/subcutaneous microvasculature is primarily affected, with potential multi-organ (renal, cerebral, ocular) involvement due to disseminated microthrombosis.
- **Tissue/cell level:** Vascular endothelium (site of anticoagulant cofactor activity), hepatocytes (primary site of protein S synthesis; CL:0000182), platelets (secondary involvement via thrombus formation), dermal/subcutaneous microvasculature (purpura fulminans).
- **Subcellular level:** Not classically compartment-specific for pathology (protein S is a secreted plasma protein); relevant GO Cellular Component for wild-type biology: GO:0005615 (extracellular space), GO:0070062 (extracellular exosome, for some assay contexts).
- **Localization:** Predominantly **bilateral or unilateral lower-extremity DVT**; PE is typically bilateral/multifocal in the pulmonary vasculature. Purpura fulminans lesions are typically symmetric and affect distal extremities, buttocks, and trunk.

---

## 8. Temporal Development

- **Onset pattern (heterozygous/mild form):** Adult-onset, though can occur in adolescence; median age at first VTE reported around 29 years in some cohort analyses; roughly half of carriers become symptomatic before age 55.
- **Onset pattern (severe homozygous/compound heterozygous form):** Neonatal, typically within hours to days of birth (purpura fulminans, massive venous thrombosis, sometimes with evidence of in-utero thrombotic events such as ocular/retinal vessel occlusion).
- **Progression:** Heterozygous disease follows an episodic/recurrent course (discrete VTE events, sometimes provoked, sometimes spontaneous) rather than a steadily progressive one; recurrence is common, especially with inadequate anticoagulation duration or continued risk-factor exposure. The neonatal form is acute and rapidly progressive, requiring emergency plasma-product replacement to prevent death.
- **Disease course pattern:** Relapsing rather than continuously progressive for the common form; post-thrombotic syndrome and chronic venous insufficiency can represent a chronic sequela.
- **Critical periods / windows of vulnerability:** Pregnancy/puerperium (antepartum VTE risk 0.9%, postpartum risk 4.2% in protein S–deficient women — high-risk thrombophilia category), immediate postoperative/post-trauma period, immobilization, initiation of estrogen therapy, and initiation of warfarin without heparin bridging (skin-necrosis window, typically days 3–8 of warfarin therapy based on general VKA-necrosis literature).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence, partial (heterozygous) deficiency:** 0.16–0.21% general population (Orphanet); blood-donor screening estimates 0.03–0.13%.
- **Prevalence, severe (homozygous/compound heterozygous) deficiency:** Unknown precisely, but probably comparable to severe protein C deficiency (~1/500,000) (Orphanet ORPHA:743).
- **Prevalence among thrombophilia/VTE-referral cohorts:** 3–5% (StatPearls); up to 12.7% in Japanese thrombosis patients when the K196E founder variant is included.
- **Neonatal purpura fulminans (combined protein C + protein S causes):** ~1 in 1 million live births.

### Inheritance pattern
- **Autosomal dominant** for the common heterozygous/partial deficiency (OMIM #612336, THPH5) — incomplete penetrance (~50%).
- **Autosomal recessive** for the severe homozygous/compound heterozygous form (OMIM #614514, THPH6) — "very rare and severe hematologic disorder resulting in thrombosis and secondary hemorrhage usually beginning in early infancy" ([OMIM 614514](https://omim.org/entry/614514)).

### Penetrance / expressivity
- Penetrance in heterozygotes ~50% (variable, incomplete).
- Expressivity is markedly variable — from asymptomatic carrier status to recurrent life-threatening VTE — modified by co-inherited thrombophilic factors (see below), hormonal exposures, and other acquired risk factors.

### Genetic anticipation / germline mosaicism
- No genetic-anticipation phenomenon is described (not a repeat-expansion disorder).
- **Germline mosaicism** has been reported: "First report of inherited protein S deficiency caused by paternal PROS1 mosaicism" ([Haematologica](https://haematologica.org/article/view/haematol.2021.278527)), relevant for recurrence-risk counseling when a de novo–appearing variant is found in an affected child.

### Founder effects / population variation
- PROS1 K196E (K155E, "PS Tokushima") is a Japan-specific founder variant, absent in Chinese, Korean, and Caucasian populations, accounting for 9–30% of protein S abnormalities detected in Japan.
- Protein S deficiency overall is reported to be "5 to 10 times more common in Japanese populations than in whites," with general-population prevalence of 0.48–0.63% in Japan vs. 12.7% in Japanese thrombosis patients (StatPearls).

### Consanguinity
Biallelic (severe/recessive) disease is more likely in consanguineous unions, consistent with autosomal recessive inheritance, though this review did not find a dedicated consanguinity-specific epidemiologic study for PROS1.

### Sex and demographic distribution
- Men demonstrate higher baseline protein S antigen levels than women.
- Protein S levels rise with age in women (hormonal influence) but remain relatively stable in men across adulthood — a key pre-analytical consideration for diagnostic interpretation (StatPearls).

### Digenic/combined-defect epidemiology (Factor V Leiden + Protein S deficiency)
- In sibships segregating both PROS1 deficiency and Factor V Leiden, 80% of individuals carrying both defects were symptomatic, versus a much lower rate with either defect alone ([PubMed 9607123](https://pubmed.ncbi.nlm.nih.gov/9607123/)).
- Mean age at first thrombosis: 18.4 years (combined defect) vs. 32.6 years (single defect) — "significantly lower... thrombosis-free survival time was significantly shorter" ([PubMed 8584987](https://pubmed.ncbi.nlm.nih.gov/8584987/)).
- Among symptomatic PROS1-deficient probands, FVL prevalence was 38% (vs. general-population FVL prevalence of ~3–5% in most European populations), consistent with strong ascertainment/selection and a synergistic "two-hit" thrombosis model ([Blood 1998, 150-family study](https://ashpublications.org/blood/article/92/7/2353/249108/Different-Risks-of-Thrombosis-in-Four-Coagulation-)).

---

## 10. Diagnostics

### Laboratory tests
- **Free protein S antigen (immunoturbidimetric/ELISA):** considered "the most reliable way of diagnosing the deficiency" because it reflects the functionally active, non-C4BP-bound fraction.
- **Total protein S antigen (ELISA):** detects Type I deficiency well but **cannot detect Type II or Type III** deficiency, since these have normal total antigen.
- **Functional (clotting-based) protein S activity assay:** measures APC-cofactor–dependent prolongation of clotting time; detects all three types but is technically the most failure-prone assay.
- **Key pre-analytical/assay pitfalls:**
  - **Factor V Leiden causes falsely low functional protein S results** in older clotting-based assays (interference); newer assays with plasma-dilution protocols mitigate this.
  - Levels are altered by pregnancy, oral contraceptives/HRT, acute-phase reaction/inflammation, acute thrombosis itself, vitamin K deficiency, warfarin therapy, and liver disease — testing should be deferred to a stable, non-acute, non-anticoagulated, non-pregnant state where possible.
  - Age- and sex-adjusted reference ranges are essential given the physiologic variation described above.

### ISTH diagnostic criteria (2021 SSC recommendations)
Diagnosis requires **persistently reduced plasma protein S concentration and/or activity below the reference interval, confirmed on at least two abnormal results obtained ≥4 weeks apart** under appropriate testing conditions (i.e., outside acute thrombosis, pregnancy, and anticoagulation) ([Marlar et al., J Thromb Haemost 2021](https://onlinelibrary.wiley.com/doi/10.1111/jth.15109)).

### Genetic testing
- **PROS1 sequencing** (Sanger or NGS-based single-gene test or thrombophilia gene panel) plus deletion/duplication analysis (MLPA or similar) to detect large exonic deletions.
- Available as a clinical test via commercial/academic laboratories (e.g., listed in NCBI GTR) and useful for confirming ambiguous phenotypic results, cascade/family testing, and prenatal or newborn diagnosis in families with known severe (biallelic) disease.
- The ISTH maintains/has maintained a PROS1 mutation database resource to support variant interpretation.
- **ACMG/AMP classification:** PROS1 variants are curated in ClinVar with standard pathogenic/likely pathogenic/VUS/likely benign/benign tiers; as above, a 2024–2025 reanalysis found a substantial fraction of variants in suspected-deficiency patients were novel or previously unclassified, underscoring ongoing curation need.

### Imaging / functional / other studies
- Standard VTE-diagnostic imaging applies (compression ultrasonography for DVT, CT pulmonary angiography for PE, MR venography for cerebral venous sinus thrombosis) — these are general VTE-diagnostic tools, not protein S–specific.
- No disease-specific biopsy/histopathology test exists; skin biopsy in warfarin-induced necrosis may show microvascular thrombosis with hemorrhagic necrosis, supportive but non-specific.

### Differential diagnosis
Antiphospholipid syndrome, antithrombin deficiency, Factor V Leiden/APC resistance, protein C deficiency, prothrombin G20210A mutation, paroxysmal nocturnal hemoglobinuria, and malignancy-associated hypercoagulability — all must be distinguished, and acquired causes of low protein S (pregnancy, vitamin K deficiency, oral contraceptives, hepatic dysfunction, chronic infection) must be excluded before assigning a congenital diagnosis (StatPearls).

### Screening
No population-based newborn screening program for protein S deficiency exists; testing is generally targeted (unprovoked/recurrent VTE, VTE at young age or unusual site, strong family history, neonatal purpura fulminans) and cascade family testing is used once a proband's causal variant is identified.

---

## 11. Outcome/Prognosis

- **Heterozygous/mild disease:** Generally good prognosis with appropriate anticoagulation; "little evidence suggests that thrombophilia related to protein S deficiency results in a deteriorated prognosis for VTE" compared with VTE from other causes, though recurrence risk and chronic anticoagulation-associated bleeding risk represent ongoing morbidity (StatPearls).
- **Severe (biallelic) neonatal disease:** Poor prognosis without aggressive, sustained replacement therapy; complications of repeated plasma infusion (fluid overload) contribute to a historically high infant mortality rate; long-term outcome data remain limited.
- **Recurrence:** Recurrent VTE and post-thrombotic syndrome (chronic venous insufficiency, pain, edema, skin changes) are the dominant morbidity drivers in surviving heterozygous patients; a documented case series highlights recurrent DVT/PE "despite optimal anticoagulation therapies" ([PMC11180491](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11180491/)).
- **Prognostic modifiers:** Co-inherited Factor V Leiden substantially worsens prognosis (earlier onset, shorter thrombosis-free interval, higher penetrance — Section 9); pregnancy is a high-risk period (antepartum VTE 0.9%, postpartum 4.2%).
- **Mortality:** Disease-specific population mortality statistics were not identified in the sources reviewed beyond the neonatal-purpura-fulminans context; adult heterozygous disease mortality is primarily related to PE and anticoagulation-related bleeding rather than the deficiency itself.

---

## 12. Treatment

### Pharmacotherapy (acute/chronic VTE management)
- **Initial/acute phase:** Intravenous unfractionated heparin or subcutaneous low-molecular-weight heparin (LMWH) for a minimum of ~5 days.
- **Maintenance:** Vitamin K antagonist (warfarin) or a direct oral anticoagulant (DOAC, e.g., apixaban, rivaroxaban). DOACs are increasingly favored for efficacy/safety, with warfarin reserved for specific situations (extremes of body weight, large proximal clot burden, massive/submassive PE) — suggest NCIT:C15986 (Pharmacotherapy) as `treatment_term` with `therapeutic_agent` bound to CHEBI (e.g., warfarin CHEBI:10033, apixaban CHEBI:66401) or NCIT drug terms.
- **Duration:** Standard 3–6 months post-VTE; extended/lifelong anticoagulation for life-threatening events, unusual/multiple-site thrombosis, or recurrent unprovoked VTE; shorter courses acceptable when a strong transient provoking factor (surgery/trauma) was present without unusual features.
- **Warfarin-necrosis avoidance:** Heparin bridging during warfarin initiation is critical in protein C/S–deficient patients to avoid the transient hypercoagulable "warfarin necrosis" window; if necrosis occurs, heparin is reinstituted and warfarin may be cautiously restarted at low dose with overlap once the acute event resolves ([PubMed 1427456](https://pubmed.ncbi.nlm.nih.gov/1427456/)).

### Advanced/replacement therapeutics (severe congenital form)
- **Fresh frozen plasma (FFP):** first-line emergency replacement therapy for neonatal purpura fulminans, typically dosed every 8–12 hours and titrated to clinical response.
- **Plasma-derived protein C/protein S concentrate:** an emerging, more targeted replacement option available at some centers, though access remains limited (NORD/GARD; StatPearls).
- **Liver transplantation** has been used as definitive therapy for severe homozygous **protein C** deficiency (analogous rationale could extend to protein S, though this review found the direct evidence base specifically for protein S transplantation to be sparse — flagged as a gap).

### Surgical/interventional
No protein S–deficiency–specific surgical intervention; standard VTE-related interventions (IVC filter in select cases, thrombectomy for massive PE/limb-threatening DVT) apply per general VTE guidelines.

### Supportive/rehabilitative
Compression therapy for post-thrombotic syndrome, physical therapy/mobility rehabilitation, and wound care for purpura fulminans/skin necrosis lesions.

### Pregnancy-specific management
LMWH is preferred throughout pregnancy (does not cross the placenta); warfarin is contraindicated for teratogenicity; specific caution is advised in the first trimester and after 36 weeks gestation, transitioning to LMWH over warfarin in those windows to minimize fetal/maternal bleeding risk. Protein S deficiency is classified as a **high-risk thrombophilia** in pregnancy risk-stratification schemes.

### Prophylaxis in asymptomatic carriers
Risk-adapted prophylactic anticoagulation is recommended around known high-risk exposures (surgery, prolonged immobilization, long-haul travel, pregnancy) rather than universal indefinite anticoagulation for asymptomatic carriers.

### Experimental/trial landscape
The literature surveyed did not identify active gene-therapy, RNA-based, or novel targeted-biologic trials specific to protein S deficiency (unlike, e.g., hemophilia); management remains centered on conventional and plasma-derived anticoagulant/replacement approaches. (This is a notable gap suitable for `just verify-datasets`/ClinicalTrials.gov confirmation before KB citation.)

### Treatment outcomes / adverse events
- Standard anticoagulant bleeding risk applies; cumulative bleeding risk increases with extended/lifelong therapy duration.
- Warfarin-induced skin necrosis is an uncommon but serious adverse event more classically linked to protein C deficiency, with rare case reports in protein S deficiency.

---

## 13. Prevention

- **Primary prevention:** Avoidance of estrogen-containing contraceptives/HRT in known carriers; prophylactic anticoagulation around high-risk exposures (surgery, immobilization, pregnancy, travel).
- **Secondary prevention:** Prompt recognition and treatment of first VTE event to reduce recurrence and post-thrombotic syndrome; screening of family members of an index case via cascade testing.
- **Tertiary prevention:** Extended-duration anticoagulation in patients with life-threatening or recurrent/unusual-site thrombosis to prevent further events; compression therapy to limit post-thrombotic syndrome progression.
- **Genetic/prenatal counseling:** Recommended for families with known severe (biallelic) disease, particularly given documented germline mosaicism and the life-threatening neonatal phenotype; carrier and prenatal testing can be offered in high-risk families once the familial PROS1 variant(s) are characterized.
- **Screening:** No population-based newborn screening program exists; targeted screening is triggered by unprovoked or recurrent VTE at a young age, VTE at an unusual site, strong family history, or neonatal purpura fulminans.
- **Public health/behavioral:** General VTE risk-reduction counseling (mobility, hydration during travel, smoking cessation given compounding vascular risk) applies but is not disease-specific.

---

## 14. Other Species / Natural Disease

- No naturally occurring (spontaneous) animal model of protein S deficiency analogous to human PROS1 disease was identified in this review; by contrast, **congenital protein C deficiency has been reported in a dog** ([PMC7255666](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7255666/)), but an equivalent natural canine/feline protein S deficiency case was not found in the sources searched (OMIA-style entries for this specific condition were not located). This is a notable evidence gap — absence of identified reports, not confirmed absence of the condition in veterinary species.
- **Orthologous gene:** Pros1 is conserved across mammals (mouse Pros1, NCBI Gene); no cross-species comparative pathology literature specific to naturally occurring disease was found.
- **Zoonotic potential:** Not applicable — this is a non-infectious, genetic/acquired hemostatic disorder.

---

## 15. Model Organisms

- **Global Pros1 knockout mice:** Complete (germline) Pros1 knockout is **embryonic lethal**, causing a coagulopathy and vascular dysgenesis phenotype — "Lack of Protein S in mice causes embryonic lethal coagulopathy and vascular dysgenesis" ([JCI](https://www.jci.org/articles/view/39325)), directly paralleling the severe consequences of near-total human protein S loss (as in neonatal purpura fulminans) and confirming an essential, non-redundant role for protein S in vascular/hemostatic development.
- **Conditional (floxed) Pros1 knockout mice:** Because global knockout is lethal, researchers generated a Cre-lox conditional floxed Pros1 allele and crossed it with multiple Cre-driver lines to achieve tissue-specific inactivation — pan-cellular, hepatocyte-specific, endothelial/hematopoietic-specific, and vascular smooth muscle cell (VSMC)-specific knockouts — revealing "dramatic but divergent phenotypes" across tissue compartments and clarifying the relative contributions of different cellular sources of protein S, analyzed alongside the related Axl/Gas6 receptor-ligand knockout mice (protein S's paralog Gas6 signals through the TAM receptor family, of which protein S itself also weakly engages Tyro3).
- **PS K196E (Tokushima) knock-in mouse:** A mouse model carrying the human K196E mutation showed "exacerbated venous thromboembolism," directly demonstrating causality of this Japan-specific variant for thrombotic risk in vivo ([Blood 2015](https://ashpublications.org/blood/article/126/19/2247/34599/Exacerbated-venous-thromboembolism-in-mice)) and confirming that the mutation "reduces its cofactor activity for APC but not for TFPI" — a mechanistically informative dissociation between the two protein S anticoagulant functions ([PMC6178719](https://pmc.ncbi.nlm.nih.gov/articles/PMC6178719/)).
- **Applications:** These murine models have been central to establishing (a) the non-redundant, developmentally essential role of protein S in vascular integrity, (b) tissue-specific sourcing of functionally relevant plasma protein S, and (c) the mechanistic basis (APC- vs. TFPI-cofactor–selective loss) of specific human missense variants.
- **Limitations:** Complete knockout lethality means no adult "null" mouse model exists for studying postnatal severe deficiency physiology directly; conditional models are needed, and cross-species differences in coagulation-factor regulation (e.g., mouse vs. human C4BP stoichiometry) may limit direct translational extrapolation.
- **Resources:** MGI (Mouse Genome Informatics) carries the Pros1 gene and knockout allele records; IMPC/KOMP repositories may hold additional conditional-allele strains (not individually itemized in the sources retrieved here).

---

## Summary of Key Evidence Gaps (flagged for curation)

1. No naturally occurring veterinary (dog/cat) model of protein S deficiency was located, despite a documented canine protein C deficiency case — worth a targeted OMIA search before asserting absence.
2. Disease-specific quality-of-life instrument data (EQ-5D/SF-36) specific to protein S deficiency were not found; QOL impact is inferred from general VTE/anticoagulation morbidity literature.
3. Active gene-therapy/RNA-therapeutic clinical trials specific to protein S deficiency were not identified — the therapeutic landscape remains conventional (anticoagulant/plasma replacement).
4. Precise disease-specific mortality/life-expectancy statistics (beyond neonatal purpura fulminans mortality risk) were not found in a single aggregated source; figures cited (e.g., annual VTE incidence 1.90%, median onset age 29) trace to StatPearls' synthesis rather than a single primary epidemiologic study, and should be traced to primary cohort sources before KB citation.
5. Liver transplantation as definitive therapy is documented for homozygous **protein C** deficiency; direct primary-literature support for protein S–specific transplantation outcomes was not retrieved and should not be assumed by analogy without confirmation.

---

### Sources
- [StatPearls: Protein S Deficiency (NBK544344)](https://www.ncbi.nlm.nih.gov/books/NBK544344/)
- [OMIM #612336 — Thrombophilia due to Protein S Deficiency, Autosomal Dominant](https://omim.org/entry/612336)
- [OMIM #614514 — Thrombophilia due to Protein S Deficiency, Autosomal Recessive](https://omim.org/entry/614514)
- [OMIM *176880 — PROS1](https://omim.org/entry/176880)
- [Orphanet ORPHA:743 — Severe hereditary thrombophilia due to congenital protein S deficiency](https://www.orpha.net/en/disease/detail/743)
- [GARD/NIH — Hereditary thrombophilia due to congenital protein S deficiency](https://rarediseases.info.nih.gov/diseases/16543/hereditary-thrombophilia-due-to-congenital-protein-s-deficiency)
- [NORD — Severe hereditary thrombophilia due to congenital protein S deficiency](https://rarediseases.org/rare-diseases/protein-s-deficiency/)
- [Annals of Internal Medicine 1998 — Clarification of the Risk for Venous Thrombosis Associated with Hereditary Protein S Deficiency](https://www.acpjournals.org/doi/10.7326/0003-4819-128-1-199801010-00002)
- [Human Genome Variation 2024 — Investigation of a novel PROS1 splicing variant](https://www.nature.com/articles/s41439-024-00286-9)
- [PubMed 42079676 — Identification of novel PROS1 variants through systematic analysis](https://pubmed.ncbi.nlm.nih.gov/42079676/)
- [ClinVar Miner — PROS1 pathogenic variants](https://clinvarminer.genetics.utah.edu/variants-by-gene/PROS1/condition/Thrombophilia%20due%20to%20protein%20S%20deficiency,%20autosomal%20recessive/pathogenic)
- [PMC7558706 — Novel Splice Site Mutation in PROS1, Polish Patient](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7558706/)
- [PMC10682651 — PROS1 p.Leu584Arg, portal/mesenteric VTE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10682651/)
- [AHA ATVB 2008 — Protein S as Cofactor for TFPI](https://www.ahajournals.org/doi/10.1161/atvbaha.108.177436)
- [Blood 2011 — Activated protein C cofactor function of protein S](https://ashpublications.org/blood/article/117/24/6685/22285/Activated-protein-C-cofactor-function-of-protein-S)
- [Science Advances 2024 — TFPIα anticoagulant function is highly dependent on protein S in vivo](https://www.science.org/doi/10.1126/sciadv.adk5836)
- [Blood Advances 2022 — Laminin G1 residues of protein S mediate TFPI cofactor function](https://ashpublications.org/bloodadvances/article/6/2/704/477773/Laminin-G1-residues-of-protein-S-mediate-its-TFPI)
- [ScienceDirect 2022 — First laminin G-like domain of protein S and Tyro3 signalling](https://www.sciencedirect.com/science/article/pii/S2405580822000632)
- [PLOS ONE 2015 — ELISA-Based Detection of Protein S K196E Mutation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133196)
- [Blood 2015 — Exacerbated VTE in mice carrying PS K196E mutation](https://ashpublications.org/blood/article/126/19/2247/34599/Exacerbated-venous-thromboembolism-in-mice)
- [PMC6178719 — Protein S K196E reduces APC cofactor activity but not TFPI](https://pmc.ncbi.nlm.nih.gov/articles/PMC6178719/)
- [PMC7695562 — Racial differences in protein S Tokushima and protein C variants](https://pmc.ncbi.nlm.nih.gov/articles/PMC7695562/)
- [JCI — Lack of Protein S in mice causes embryonic lethal coagulopathy and vascular dysgenesis](https://www.jci.org/articles/view/39325)
- [J Thromb Haemost 2021 — ISTH SSC recommendations for protein S deficiency lab testing](https://onlinelibrary.wiley.com/doi/10.1111/jth.15109)
- [PubMed 1427456 — Warfarin-induced skin necrosis in protein S deficiency](https://pubmed.ncbi.nlm.nih.gov/1427456/)
- [PubMed 9885367 — Recurrent warfarin-induced skin necrosis in protein S–deficient kindreds](https://pubmed.ncbi.nlm.nih.gov/9885367/)
- [PubMed 8584987 — Factor V Leiden as additional risk factor in protein S–deficient families](https://pubmed.ncbi.nlm.nih.gov/8584987/)
- [PubMed 9607123 — Combined protein C/S and Factor V Leiden thrombophilia](https://pubmed.ncbi.nlm.nih.gov/9607123/)
- [Blood 1998 — Different Risks of Thrombosis in Four Coagulation Defects (150 families)](https://ashpublications.org/blood/article/92/7/2353/249108/Different-Risks-of-Thrombosis-in-Four-Coagulation-)
- [Haematologica — Paternal PROS1 mosaicism causing inherited protein S deficiency](https://haematologica.org/article/view/haematol.2021.278527)
- [PMC11180491 — Recurrent DVT/PE despite optimal anticoagulation in protein S deficiency](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11180491/)
- [PMC7255666 — Congenital protein C deficiency and thrombosis in a dog](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7255666/)
- [Cleveland Clinic — Protein S Deficiency overview](https://my.clevelandclinic.org/health/diseases/21877-protein-s-deficiency)
- [Medscape — Protein S Deficiency: Practice Essentials](https://emedicine.medscape.com/article/205582-overview)