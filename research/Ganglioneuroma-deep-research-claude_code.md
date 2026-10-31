---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-10-28T16:16:26.010031'
end_time: '2026-10-28T16:38:09.357909'
duration_seconds: 1303.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Ganglioneuroma
  mondo_id: MONDO:0005033
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: ganglioneuroma (Schwannian Stroma-dominant); ganglioneuroma (disease);
    ganglioneuroma, benign; neural Crest tumor, benign
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
  - claude-opus-5
  web_search_requests: 31
  num_turns: 85
  total_cost_usd: 10.892519250000001
  session_id: 2398d584-f6a4-484b-a163-53ed2ff935ec
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 92
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ganglioneuroma
- **MONDO ID:** MONDO:0005033 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** ganglioneuroma (Schwannian Stroma-dominant); ganglioneuroma (disease); ganglioneuroma, benign; neural Crest tumor, benign
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Ganglioneuroma** covering all of the
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

I'll research this now across the key domains in parallel.

# Research Report: Ganglioneuroma (MONDO:0005033)

## 0. Scope note and the gene question

**Ganglioneuroma (GN) has no causal germline gene, and none is recorded for MONDO:0005033.** It is a sporadic, benign, fully differentiated neoplasm of the peripheral sympathetic nervous system — the most mature member of the peripheral neuroblastic tumour (pNT) family, alongside neuroblastoma (MONDO:0005072) and ganglioneuroblastoma (MONDO:0005035). The genes that bear on it fall into three distinct classes, and conflating them is the main hazard in curating this entry:

| Class | Genes | What the gene actually does here |
|---|---|---|
| **Somatic driver pathway** (demonstrated in model, inferred in human) | `AKT1` hgnc:391 / `AKT2` hgnc:392 / `AKT3` hgnc:393, `MTOR` hgnc:3942, `PTEN` hgnc:9588 | Constitutively activated AKT is *necessary and sufficient* to produce GN in zebrafish; the AKT–mTOR–S6 axis is active in 10/11 human GN (PMID:32728700) |
| **Germline predisposition syndromes** | `RET` hgnc:9967 (MEN2B), `NF1` hgnc:7765, `PTEN` hgnc:9588 (Cowden/PHTS) | Confer risk of GN / diffuse ganglioneuromatosis; GN is often the **presenting** sign |
| **Maturation / stromal crosstalk** (not causal) | `NTRK1` hgnc:8031, `NRG1` hgnc:7997, `NGF` hgnc:7808, `EGFL8`, `SOX10` hgnc:11190, `PHOX2B` hgnc:9143 | Govern whether a neuroblastic tumour differentiates into GN-like tissue |

`MYCN` hgnc:7559 amplification — the defining adverse lesion of neuroblastoma — is **absent** in GN, and this is one of the most consistent negative facts in the literature.

Two mutually incompatible origin models are live in the current literature; both are well-supported, and §6 presents each as its own causal chain. This is, in dismech terms, a genuine competing-hypothesis situation rather than a knowledge gap.

Identifier verification: every CURIE in this report was resolved in-session against `cache/*/terms.csv`, the EBI OLS4 API, or `rest.genenames.org`. Items I could **not** resolve are flagged `[UNVERIFIED — look up before binding]`.

---

## 1. Disease Information

### 1.1 Overview

Ganglioneuroma is a rare, benign, well-differentiated tumour of neural-crest origin arising from the sympathetic nervous system, composed of mature ganglion cells embedded in a dominant Schwannian (Schwann-cell + collagen) stroma. It arises anywhere along the sympathetic chain from skull base to pelvis, most often retroperitoneum, posterior mediastinum, adrenal gland and pelvis.

Orphanet's definition, verbatim:

> "Ganglioneuroma is a rare tumor of neuroepithelial tissue, a benign and well-differentiated tumor of neural crest origin"
> — [Orphanet, ORPHA:251992](https://www.orpha.net/en/disease/detail/251992)

Orphanet continues that it "originates from the sympathetic nervous system and comprises ganglion cells and stromal Schwann cells," with common sites "adrenal glands, retroperitoneum, posterior mediastinum, and pelvis," and records associations with "neurofibromatosis type I, multiple endocrine neoplasia type 2B, and Turner syndrome."

### 1.2 Position in the INPC

The International Neuroblastoma Pathology Classification (INPC, the "Shimada system") defines **four** pNT categories (Shimada et al., *Cancer* 1999;86:349–363, **PMID:10421272**; and *Cancer* 1999;86:364–372, **PMID:10421273**):

1. Neuroblastoma — **Schwannian stroma-poor**
2. Ganglioneuroblastoma, intermixed — **Schwannian stroma-rich** (MONDO:0003326)
3. **Ganglioneuroma — Schwannian stroma-dominant** ← this entry
4. Ganglioneuroblastoma, nodular — **composite** (MONDO:0003325); revised into favourable/unfavourable subsets by Peuchmaur et al., *Cancer* 2003;98:2274–2281, **PMID:14601099**

GN has two histological subtypes, **maturing** and **mature**, and *both* are Favorable Histology regardless of patient age (Shimada H, Sano H, Hazard FK. *Clin Pediatr Hematol Oncol* 2020;27:73–86, [doi:10.15264/cpho.2020.27.2.73](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73)). That review states GN represents approximately **3%** of cases reviewed at the COG Neuroblastoma Pathology Reference Laboratory.

A 2026 update of the pathology of pNTs is available: Conces MR, Shibui Y, Shimada H. "Pathology of peripheral neuroblastic tumors." *Diagnostic Pathology* 2026;21:22, [doi:10.1186/s13000-026-01758-y](https://link.springer.com/article/10.1186/s13000-026-01758-y) — open access (full text was paywall-redirected in this session; the abstract confirms the 1984→1999→2003 INPC lineage).

### 1.3 Key identifiers

| System | Value | Verification |
|---|---|---|
| MONDO | **MONDO:0005033** `ganglioneuroma` | Resolved in `cache/mondo/terms.csv` (retrieved 2026-10-28) |
| HPO (as a phenotype) | **HP:0003005** `Ganglioneuroma` | Resolved in `cache/hp/terms.csv` |
| Orphanet | **ORPHA:251992** | Orphanet disease page |
| ICD-10 | **D36.1** (benign neoplasm, peripheral nerves and autonomic nervous system) | Orphanet cross-reference |
| ICD-O-3 morphology | **9490/0** Ganglioneuroma | ICD-O-3 morphology listings |
| ICD-11 | **2A00.21** as recorded by Orphanet | `[Attribution: Orphanet mapping only — this code reads as a CNS/benign-neoplasm stem and was not verified against the WHO ICD-11 browser. Morphology stem XH03L9 appears in third-party aggregators. UNVERIFIED]` |
| OMIM | none | Orphanet records no OMIM entry ("brak danych") |
| MeSH | Ganglioneuroma, D005729 | `[From aggregator listing; UNVERIFIED against NLM MeSH]` |

Related MONDO terms confirmed present in the local cache: MONDO:0003325 `nodular ganglioneuroblastoma`, MONDO:0003326 `intermixed schwannian stroma-rich ganglioneuroblastoma`, MONDO:0005035 `ganglioneuroblastoma`, MONDO:0005072 `neuroblastoma`, MONDO:0006076 `adrenal gland neuroblastoma`.

### 1.4 Synonyms

ganglioneuroma (Schwannian stroma-dominant); mature ganglioneuroma; maturing ganglioneuroma; benign ganglioneuroma; benign neural crest tumour. Site-qualified variants in common use: adrenal ganglioneuroma (AGN), retroperitoneal ganglioneuroma (RGN), paraspinal/dumbbell ganglioneuroma, presacral ganglioneuroma, **intestinal/diffuse ganglioneuromatosis** (a distinct, usually syndromic, polytopic form — see §2.2 and §6.3).

### 1.5 Evidence provenance

**All content below is from aggregated disease-level resources and institutional/registry case series. There are no EHR-derived or patient-level datasets for GN.** The three largest modern series — 259 (UK national registry), 101 (single institution, 30 years), 51 (single sarcoma centre) — are all retrospective chart reviews. No randomised trial exists, and none is plausible at this incidence.

---

## 2. Etiology

### 2.1 Disease causal factors

GN is a **somatic neoplasm of a sympathoadrenal neural-crest derivative**. There is no infectious, dietary, or occupational cause described anywhere in the literature reviewed. Two causal models compete (detailed in §6):

- **Terminal-maturation model (INPC consensus).** GN is the end-state of a neuroblastic tumour that differentiated. Shimada et al. state this explicitly: ganglioneuromas represent the "final stage of tumor maturation," such that **"all Ganglioneuromas were once Neuroblastomas in their early stage of tumor development"** ([Shimada 2020](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73)).
- **De novo AKT-driven model.** Tao et al. found an active AKT–mTOR–S6 axis in human GN but not neuroblastoma, and showed that constitutive AKT in the zebrafish sympathetic nervous system produces GN **without** passing through a neuroblastoma state (**PMID:32728700**). Verbatim from the abstract:

  > "Zebrafish transgenic for constitutively activated myr-Akt2 in the sympathetic nervous system were found to develop ganglioneuroma without progression to neuroblastoma."
  > "Our results implicate activated AKT as a tumorigenic driver in ganglioneuroma."

These are not reconcilable as stated, and the field has not resolved them. Note what each predicts about the *same* patient: the maturation model predicts GN should carry residual neuroblastoma-type segmental aberrations; the de novo model predicts it should not. The telomere data in §4.2 are the best available discriminating evidence and favour a genomically distinct entity.

### 2.2 Genetic risk factors

**Germline syndromes.** GN is not itself inherited, but three autosomal-dominant syndromes carry a materially raised risk, and in each the ganglioneuromatous lesion is frequently the **first** manifestation:

- **MEN2B (`RET` hgnc:9967).** A single germline mutation at codon 918 (**M918T**, exon 16) accounts for ~**95%** of MEN2B. Diffuse **intestinal ganglioneuromatosis** is a universal extra-endocrine feature and typically precedes medullary thyroid carcinoma by years. Gastrointestinal onset occurred in **29/55 (52.3%)** of reported cases **before age 1**, and constipation was the commonest symptom (**72.7%**) ([Intestinal ganglioneuromatosis as an early extra-endocrine manifestation of MEN2B, PMC10848182](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848182); [Timely diagnosis of MEN2B by identification of intestinal ganglioneuromatosis, Springer](https://link.springer.com/article/10.1007/s12020-021-02607-2); [role of rectal biopsy, PMID:27899172](https://pubmed.ncbi.nlm.nih.gov/27899172/)). Germline codon-918 mutation has also been found in **apparently isolated** intestinal ganglioneuromatosis ([J Clin Endocrinol Metab 1998;83:4191](https://academic.oup.com/jcem/article/83/12/4191/2865226)).
- **PTEN hamartoma tumour syndrome / Cowden syndrome (`PTEN` hgnc:9588).** Ganglioneuromatous polyposis, diffuse gastric ganglioneuromatosis, and uveal ganglioneuroma are all reported presentations ([PMC5889855](https://pmc.ncbi.nlm.nih.gov/articles/PMC5889855/); [PMC4862217](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4862217/); [PMID:23512313](https://pubmed.ncbi.nlm.nih.gov/23512313/); [uveal ganglioneuroma, PMC5566766](https://pmc.ncbi.nlm.nih.gov/articles/PMC5566766/)).
- **Neurofibromatosis type 1 (`NF1` hgnc:7765).** GN in NF1 is real but **uncommon**. In an Italian multicentre registry study, 8 children with neuroblastic tumours (**0.2%** of registered patients) met NF1 criteria; of those, 5 were neuroblastoma, 1 ganglioneuroblastoma, **2 ganglioneuroma** ([PMC9673013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9673013/)). Co-occurrence with pheochromocytoma is described ([PMID:17954422](https://pubmed.ncbi.nlm.nih.gov/17954422/)), and bladder and cervical GN have been reported in NF1 ([PMC9776796](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9776796/); [PMC13492013](https://pmc.ncbi.nlm.nih.gov/articles/PMC13492013/)).
- **Turner syndrome** — recorded by Orphanet as an association. `[No primary citation located in this session; treat as Orphanet-level only.]`

**`PHOX2B` hgnc:9143 — one reported instance, not a susceptibility claim.** In a familial neuroblastic-tumour report, a *PHOX2B* variant inherited from the father was followed by that father developing a **well-differentiated ganglioneuroma at age 40** — the single clearest human observation that a germline neurocristopathy allele can yield a differentiated rather than malignant tumour ([Identifying a novel PHOX2B gene variant in a neuroblastoma family, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405844024026124); see also [Analysis of sporadic neuroblastic tumors reveals a novel PHOX2B mutation](https://www.sciencedirect.com/science/article/abs/pii/S2452014418300396)). *n*=1; do not curate as a susceptibility locus.

**Susceptibility loci / GWAS.** No GWAS, no polygenic risk score, and no common-variant association for GN. The neuroblastoma GWAS literature does not stratify by INPC category.

### 2.3 Environmental risk factors

- **Prior therapeutic irradiation** is the one documented exogenous risk factor, and it acts on *outcome* rather than occurrence: MPNST has arisen inside a benign ganglioneuroma 12 years after radiotherapy for a childhood neuroblastic tumour ([PMID:10755757](https://pubmed.ncbi.nlm.nih.gov/10755757/)), and after radiotherapy for a cerebellopontine-angle ganglioneuroma ([PMID:42120254](https://pubmed.ncbi.nlm.nih.gov/42120254/)).
- **Age** is the strongest demographic correlate (see §9).
- No toxin, pollutant, occupational exposure, dietary factor, smoking, or alcohol association is reported.

### 2.4 Protective factors

**None documented, genetic or environmental.** The absence is informative rather than a gap in searching: GN has no modifiable risk factor to protect against, and no gnomAD-level protective allele has been sought. Plausibly the closest thing to a "protective factor" in the pNT family is the differentiation-promoting Schwann-cell stroma itself (§6.2) — but that is a mechanism *within* the tumour, not a population-level exposure, and should not be curated as `PROTECTS_AGAINST`.

### 2.5 Gene–environment interactions

Only one interaction is evidenced, and it is iatrogenic: **germline `NF1` loss + therapeutic irradiation → MPNST arising within a ganglioneuroma**. The 2025 rectovaginal-septum case is the worked example — a 29-year-old woman with NF1 whose lesion was called ganglioneuroma on biopsy and proved MPNST on resection ([PMC12221925](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221925)). No CTD/PheGenI GxE entry exists for GN.

---

## 3. Phenotypes

### 3.1 The dominant phenotype is *absence* of phenotype

Across all three modern series, most GN are incidental:

| Series | n | Incidental |
|---|---|---|
| Texakalidis 2026, *J Neurosurg* (**PMID:42537227**) | 101 | **72%** |
| Li 2025, *Front Surg* (**PMID:41306794**) | 51 | **56.9%** |
| Burnand 2025, UK CCLG (**PMID:39582110**) | 259 | — (symptom data by site) |

Verbatim: *"Most lesions (72%) were incidental findings."* (PMID:42537227)

This matters for the KB entry: the modal patient has **no** phenotype, and symptomatic phenotypes are almost all **mass effect**, not tumour biology.

### 3.2 Phenotype table with HPO bindings

All HP CURIEs below were resolved in `cache/hp/terms.csv` this session except where flagged.

| Phenotype | HPO term | Type | Frequency / source |
|---|---|---|---|
| Ganglioneuroma (the lesion itself) | **HP:0003005** Ganglioneuroma | Neoplasm | 100% by definition |
| Abdominal pain | **HP:0002027** Abdominal pain | Symptom | **31.4%** of retroperitoneal GN (PMID:41306794) |
| Back pain / lumbago | **HP:0003418** Back pain | Symptom | **5.8%** (PMID:41306794) |
| Abdominal mass | **HP:0031500** Abdominal mass | Clinical sign | Common in paediatric presentation |
| Abdominal distention | **HP:0003270** Abdominal distention (OLS4, hp) | Clinical sign | Reported with pressure effects |
| Vomiting (bowel obstruction) | **HP:0002013** Vomiting | Symptom | Reported |
| Constipation | **HP:0002019** Constipation | Symptom | **72.7%** in MEN2B intestinal ganglioneuromatosis ([PMC10848182](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848182)) |
| Chronic watery diarrhoea (VIP) | **HP:0002014** Diarrhea | Symptom | Rare; VIP-secreting GN ([PMID:1211964](https://pubmed.ncbi.nlm.nih.gov/1211964/); [PMID:7376870](https://pubmed.ncbi.nlm.nih.gov/7376870); [PMID:2833214](https://pubmed.ncbi.nlm.nih.gov/2833214/)) |
| Hypokalaemia (secretory diarrhoea) | **HP:0002900** Hypokalemia | Lab abnormality | With VIP syndrome |
| Failure to thrive | **HP:0001508** Failure to thrive | Clinical sign | With VIP syndrome ([PMID:2833214](https://pubmed.ncbi.nlm.nih.gov/2833214/)) |
| Hypertension | **HP:0000822** Hypertension | Clinical sign | Catecholamine-secreting GN ([Blood Press 2013](https://www.tandfonline.com/doi/full/10.3109/08037051.2013.796103)) |
| Flushing | **HP:0031284** Flushing | Clinical sign | Hormonally active GN |
| Hyperhidrosis / diaphoresis | **HP:0000975** Hyperhidrosis | Clinical sign | Hormonally active GN |
| Palpitations | **HP:0001962** Palpitations | Symptom | Hormonally active GN |
| Tremor | **HP:0001337** Tremor | Clinical sign | Hormonally active GN |
| Anxiety | **HP:0000739** Anxiety | Behavioural | Hormonally active GN |
| Headache | **HP:0002315** Headache | Symptom | Hormonally active GN |
| Horner syndrome | **HP:0002277** Horner syndrome | Clinical sign | Cervical/apical thoracic GN; also a *post-operative complication* ([PMC13492013](https://pmc.ncbi.nlm.nih.gov/articles/PMC13492013/)) |
| Spinal cord compression | **HP:0002176** Spinal cord compression | Clinical sign | Dumbbell/paraspinal GN |
| Paraparesis | **HP:0002385** Paraparesis | Clinical sign | Dumbbell GN; also transient post-operatively ([J Neurosurg Spine 2022;37:130](https://thejns.org/spine/view/journals/j-neurosurg-spine/37/1/article-p130.xml)) |
| Scoliosis | **HP:0002650** Scoliosis | Physical manifestation | Paraspinal GN |
| Dyspnoea | **HP:0002094** Dyspnea | Symptom | Mediastinal GN |
| Cough | **HP:0012735** Cough | Symptom | Mediastinal GN |
| Chest pain / tightness | **HP:0100749** Chest pain | Symptom | **5.8%** "other" group (PMID:41306794) |
| Hydronephrosis | **HP:0000126** Hydronephrosis | Imaging/lab | Ureteric compression |
| Urinary incontinence | **HP:0000020** Urinary incontinence | Symptom | Presacral/sacral GN |
| Virilization | `[HP term UNVERIFIED]` | Clinical sign | Androgen-secreting GN (very rare) |

**Deliberately excluded:** opsoclonus (HP:0010543) and myoclonus (HP:0001336) — opsoclonus-myoclonus syndrome is a neuroblastoma/GNB paraneoplastic phenomenon; I found no evidence it occurs with pure GN, and binding it here would import a neuroblastoma phenotype.

### 3.3 Phenotype characteristics

- **Age of onset.** Bimodal by series type. Paediatric registry: median **62 months** (UK CCLG, n=259, PMID:39582110). Adult/neurosurgical: mean **26.9 ± 15.9 years** (PMID:42537227); median **28 years**, range 12–73, with **74.5% under 40** (PMID:41306794); median **42 years** in a 25-patient adult oncology series (**PMID:41561749**). Secondary literature states ~**60% of cases occur under age 20**.
- **Severity.** Mild in the great majority; severity is set by *size and location*, not by grade. Mean maximal dimension **8.5 ± 3.8 cm** on MRI (PMID:42537227); mean **13.06 ± 5.77 cm** (range 4.1–30.2) in the retroperitoneal cohort, where **66.7% encased major vasculature** (PMID:41306794).
- **Progression.** Indolent and near-static. Median growth **0.3 cm/year** (Alexander 2018, **PMID:29369484**); in the observation arm of the 2026 series, *"2 tumors exhibited minimal interval growth (0.08–0.17 cm/year)"* and *"No patient in the observation group developed new symptoms"* (PMID:42537227).
- **Frequency among affected individuals** — see the table above; the honest summary is that no individual symptom reaches 50%, and asymptomatic status does.

### 3.4 Quality of life

**No EQ-5D, SF-36, PROMIS, or GN-specific PRO data exist.** This is a real gap, not a search failure. The three available surrogates are all clinician-rated:

- Complete symptom control after gross total resection vs non-GTR: **43% vs 24%** (PMID:39582110).
- Global functional status at final follow-up (mean 33.8 months): *"46.5% of patients were stable, 42.3% had improved, and 11.3% had worsened from baseline"* (PMID:42537227).
- Mean hospital length of stay **4.6 ± 3.7 days** (PMID:42537227).

The 11.3% who worsened are the clinically important group, and in a benign tumour with no recurrence they are overwhelmingly worsened by **surgery**, not by disease.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

**None.** No gene is causative for sporadic ganglioneuroma, and no OMIM entry exists. Do not populate a `CAUSATIVE` `relationship_type` for this entry.

### 4.2 Somatic molecular profile — what GN *is not*

The most robust molecular statements about GN are negative, and they are what separate it from neuroblastoma.

**Telomere maintenance (Sugawara M, Haruta M, Ohira M, et al. *Oncol Lett* 2026;31(5):156, PMID:41858373, doi:10.3892/ol.2026.15509).** 321 neuroblastic tumours, including **18 GN**. Verbatim:

> "ALT was identified in 38 NB cases (38/255, 15%) and 6 GNB cases (6/48, 12.5%), but not in GN."
> "High *TERT* expression was observed in 38% (64/169), 23% (7/31) and 14% (1/7) of NB, GNB and GN cases, respectively."

No *TERT* rearrangements and no `ATRX` hgnc:886 alterations were identified in GN. **Interpretation:** GN activates neither of the two telomere-maintenance routes that immortalise neuroblastoma. That is the strongest single piece of evidence that GN is *not* simply a differentiated neuroblastoma — a matured tumour would be expected to carry its precursor's immortalisation lesion.

**`MYCN` hgnc:7559.** MYCN amplification is not observed in GN (PMID:41858373). A separate Chinese paediatric neuroblastoma series reports low-level *MYCN* **gain** (not amplification) in a small number of ganglioneuroma cases `[attribution ambiguous in the available abstract; UNVERIFIED — re-read the primary before quoting a figure]`.

**Segmental chromosomal aberrations.** 1p loss, 11q loss and 17q gain are neuroblastoma prognostic markers. I found **no** GN-specific frequency data for them. Older comparative-genomic-hybridisation work on ganglioneuroblastoma found that some samples showed **no** chromosomal abnormalities at all ([PMID:8108298](https://pubmed.ncbi.nlm.nih.gov/8108298/); [PMID:11801306](https://pubmed.ncbi.nlm.nih.gov/11801306/)). Do not transfer 17q/11q frequencies from ALT-positive mixed cohorts onto GN — that was an available-but-wrong inference I specifically checked and rejected.

### 4.3 The one positive somatic finding: an active AKT–mTOR–S6 axis

Tao T, Shi H, Wang M, Perez-Atayde AR, London WB, Gutierrez A, Lemos B, Durbin AD, Look AT. *J Exp Med* 2020;217(10):e20191871. **PMID:32728700**, doi:10.1084/jem.20191871.

Immunohistochemistry on 11 human GN vs 15 poorly differentiated neuroblastomas:

| Marker | GN | Poorly differentiated NB | p |
|---|---|---|---|
| phospho-AKT (Ser473) | **10/11 (90.9%)** | 1/15 (6.7%) | < 0.0001 |
| phospho-mTOR (Ser2448) | **9/11 (81.8%)** | 5/15 (33.3%) | 0.0214 |
| phospho-S6 (Ser235/236) | **10/11 (90.9%)** | 7/15 (46.7%) | 0.0362 |
| pan-AKT (total) | 11/11 | 14/15 | 1.00 (ns) |

Verbatim: *"Phosphorylated, activated AKT and the downstream effectors mTOR and ribosomal protein S6 were more frequently detected in human primary ganglioneuromas than in poorly differentiated human neuroblastomas."*

**Crucially, the upstream lesion in humans is unidentified.** The authors did **not** find somatically acquired `PTEN` or `AKT` mutations, and wrote: *"Somatically acquired mutations or epigenetic alterations affecting the expression levels of proteins in the PI3K–AKT–mTOR pathway may be responsible for initiating ganglioneuroma in individual patients."* One cohort patient had juvenile polyposis syndrome (a `PTEN`/`BMPR1A` hgnc:1076 context).

This is the right level of precision for the KB: the **pathway state** is demonstrated (`modifier: GAIN_OF_FUNCTION` or `INCREASED` on a `MolecularFunctionDescriptor`), the **variant** is not (no `genetic_context` / `functional_impact_category` is supportable).

### 4.4 Transcriptional identity

From the same study, GN and NB run opposite transcriptional programmes:

- The **adrenergic core regulatory circuit** TFs highly expressed in neuroblastoma — `TFAP2B`, `ISL1`, `GATA3`, `PHOX2A`, `PHOX2B` hgnc:9143 — are **down**-regulated in ganglioneuroma.
- `SOX10` hgnc:11190 (neural crest / Schwann-cell lineage) is **up**-regulated in GN and down-regulated in NB.

This is internally consistent with the IHC literature (§10.5): GN's identity is carried by its Schwannian compartment.

### 4.5 Modifier genes

None described.

### 4.6 Epigenetics

**No GN-specific DNA-methylation, histone-modification, or chromatin data were found** in ENCODE, Roadmap, MethBase or DiseaseMeth-adjacent literature. Tao et al. raise epigenetic silencing as a *candidate* upstream mechanism for pathway activation (quoted in §4.3) but did not test it. This is a clean, specific, fundable knowledge gap: **methylation profiling of ganglioneuroma against neuroblastoma and against normal sympathetic ganglion.**

### 4.7 Chromosomal abnormalities

No recurrent aneuploidy, translocation, or inversion is described. GN is not a karyotype-driven entity, and chromosomal microarray has no established role.

---

## 5. Environmental Information

- **Environmental factors:** none established. No CTD/TOXNET/EPA association.
- **Lifestyle factors:** none established.
- **Infectious agents:** **not applicable.** GN has no infectious aetiology and no `infectious_agent` should be curated.
- **Ionising radiation:** prior therapeutic irradiation is associated with later MPNST *within* a GN (§2.3), i.e. the exposure modifies malignant-transformation risk rather than causing the GN. If curated, this is best modelled as an `environmental[]` entry with `environmental_effect: PREDISPOSES` pointing at a transformation node, not at the GN itself.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain — Model A: terminal maturation of a neuroblastic tumour

This is the INPC/consensus chain. Steps 1–2 are inferred; steps 3–6 are demonstrated in human tissue and in vitro.

1. A somatic lesion arises in a **sympathoadrenal progenitor derived from the migrating neural crest** (`CL:0011012` neural crest cell → `CL:0002676` neural crest derived neuroblast) during sympathetic nervous system development (`GO:0048485` sympathetic nervous system development), **leading to** clonal neuroblastic proliferation — a neuroblastoma. *[Inferred for GN specifically; this step is observed for neuroblastoma, not for GN.]*
2. In favourable-biology tumours, the tumour cell retains high `NTRK1`/TrkA expression, which **results in** upregulated `NRG1` (neuregulin-1) mRNA. *[Demonstrated in vitro]*
3. Secreted NRG1 **leads to** proliferation and migration of adjacent Schwann cells (`CL:0002573` Schwann cell; `CL:0002375` Schwann cell precursor) into the tumour, i.e. recruitment of the Schwannian stroma. *[Demonstrated: media conditioned by NTRK1-expressing NB cells induced SC proliferation and migration — [PMC4294349](https://pmc.ncbi.nlm.nih.gov/articles/PMC4294349/)]*
4. The recruited Schwann cells **adopt a repair-like phenotype**, co-expressing nerve-injury/repair genes, and **secrete** NGF plus `EGFL8`. *[Demonstrated: Weiss T, Taschner-Mandl S, et al. Nat Commun 2021;12:1624, **PMID:33712610**. Verbatim: "stromal SCs in ganglioneuromas and repair SCs share the expression of nerve repair-associated genes."]*
5. Paracrine NGF and EGFL8 **result in** TrkA/neurotrophin-receptor signalling (`GO:0048011` neurotrophin TRK receptor signaling pathway) and kinase rewiring in the neuroblastic cells, which **leads to** neuronal differentiation (`GO:0030182` neuron differentiation), neurite outgrowth (`GO:0031175` neuron projection development) and **reduced proliferation**. *[Demonstrated: "Neuroblastoma cells, derived from aggressive tumors, respond to primary repair-related SCs and their secretome with increased neuronal differentiation and reduced proliferation." (PMID:33712610)]*
6. Differentiated cells become **mature ganglion cells**; Schwann cells ensheathe the neurites until *"all neuritic processes produced by ganglion cells are immediately incorporated in the cytoplasm of Schwann cells, so that no naked neuritic processes are detected"* — the histological definition of **mature** GN. Where incorporation is incomplete, the tumour is **maturing** GN. *[Demonstrated histologically — [Shimada 2020](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73)]*
7. The resulting mass is **mitotically inert** (Ki-67 hotspot <1%) and causes disease solely by **space occupation** — vascular encasement, nerve-root and cord compression, ureteric and airway compression (§3.2). *[Demonstrated]*

**Branch at step 5:** If residual naked neurites and microscopic neuroblastic foci persist, the tumour is **ganglioneuroblastoma, intermixed** (MONDO:0003326), not GN. If a discrete neuroblastic nodule arises within ganglioneuromatous tissue, it is **ganglioneuroblastoma, nodular** (MONDO:0003325) — and *that* carries real mortality (8-year OS 90.5% favourable subset vs **33.2%** unfavourable subset, PMID:14601099). The clinical consequence is in §10.6.

**Note this is a positive-feedback loop, not a linear cascade:** differentiating tumour cell → NRG1 → Schwann cell → NGF/EGFL8 → more differentiation. It is self-reinforcing, which is why the mature end-state is stable and why spontaneous *de*-differentiation is not observed.

### 6.2 Ordered causal chain — Model B: de novo AKT activation

1. An unidentified somatic or epigenetic event **activates** the PI3K–AKT axis in a sympathoadrenal cell. *[Mechanism demonstrated by transgene; the initiating human lesion is **unknown** — no PTEN or AKT mutation found (PMID:32728700)]*
2. Activated AKT **leads to** phosphorylation of mTOR (Ser2448) (`GO:0043491` PI3K/AKT signal transduction → `GO:0031929` TOR signaling, `GO:0032008` positive regulation of TOR signaling). *[Demonstrated in human tissue, 9/11]*
3. mTOR activation **results in** phosphorylation of ribosomal protein S6 (Ser235/236) and 4E-BP1/EIF4EBP1 (Thr37/46), **leading to** increased cap-dependent translation and enhanced survival. *[Demonstrated]*
4. This **results in** expansion and hypertrophy of **differentiated, mature ganglion cells**, with simultaneous **down**-regulation of the adrenergic core regulatory circuit and **up**-regulation of `SOX10`. *[Demonstrated]*
5. The lesion **does not progress** to neuroblastoma. *[Demonstrated in zebrafish over 29 weeks at 40–50% penetrance; the same promoter driving MYCN or c-MYC gives high-grade neuroblastoma instead]*
6. mTOR inhibition **reverses** step 3, **leading to** increased apoptosis (TUNEL-confirmed) and a 30–40% reduction in tumour burden. *[Demonstrated pharmacologically — §12.4]*

### 6.3 Branch: enteric ganglioneuromatosis (a different anatomical compartment, the same pathway)

This chain is independently demonstrated and is the strongest corroboration of Model B.

1. Loss of `PTEN` — the negative regulator immediately upstream of AKT — in neural-crest-derived enteric nervous system cells (`CL:0007011` enteric neuron; `CL:0002607` migratory enteric neural crest cell) **leads to** AKT and S6 hyperphosphorylation. *[Demonstrated: Puig I, Champeval D, De Santa Barbara P, Jaubert F, Lyonnet S, Larue L. J Clin Invest 2009;119:3586–96, **PMID:19884655**, doi:10.1172/JCI39929. Verbatim: "S6 and AKT phosphorylation levels were clearly higher in HM than in WT samples, this effect being particularly marked for AKT."]*
2. This **results in** enteric neuronal **hyperplasia** (cell counts 3× wild type) and **hypertrophy** (cells double the size), i.e. **ganglioneuromatosis**. *[Demonstrated]*
3. Ganglioneuromatosis of the myenteric plexus **leads to** dysmotility → chronic intestinal pseudo-obstruction, cecal dilation, and death between P13 and P20 with 100% penetrance. *[Demonstrated in mouse]*
4. Pharmacological AKT inhibition (API2) **prevents** step 2: *"After API2 treatment, numbers of TUJ1-positive cells in embryos treated with API2 did not significantly differ between WT and HM."* **This is a rescue experiment, and it establishes direction of causation.**
5. Human corroboration: PTEN expression in the ENS was significantly lower in **2 of 7** chronic intestinal pseudo-obstruction patients, with concomitantly increased S6 phosphorylation. *[Demonstrated, small n]*

**Parallel branch — RET gain of function (MEN2B).** Germline `RET` M918T **leads to** constitutive RET kinase activity signalling through **both** MAPK **and** PI3K/AKT, which **results in** diffuse hyperplasia of the myenteric and submucosal plexuses → intestinal ganglioneuromatosis → constipation, feeding intolerance, megacolon in the first year of life. Competing/additional proposed mechanisms in this compartment: overexpression of nerve growth factor ([NEJM 1983;308:634](https://www.nejm.org/doi/abs/10.1056/NEJM198303173081106)), and increased GDNF `GDNF` hgnc:4232 / neurturin expression (`GO:0035860` GDNF receptor signaling pathway) ([PMID:19353842](https://pubmed.ncbi.nlm.nih.gov/19353842/)). *[The NGF-overproduction hypothesis is 40 years old and has not been confirmed; label it EMERGING or record it as a knowledge gap rather than a node.]*

Note that RET loss-of-function causes **Hirschsprung aganglionosis** and RET gain-of-function causes **ganglioneuromatosis** — the same gene, opposite dose, mirror-image enteric phenotypes. That symmetry is worth capturing.

### 6.4 Where the two models leave the field

| Question | Model A (maturation) | Model B (de novo AKT) | Best discriminating evidence |
|---|---|---|---|
| Was every GN once a neuroblastoma? | Yes (explicit) | No | GN has **no ALT and essentially no high TERT** (PMID:41858373) — a matured NB should retain its immortalisation lesion. Favours B. |
| Why is Schwannian stroma dominant? | It is the *cause* of maturation | Consequence of SOX10-high lineage programme | Zebrafish AKT tumours have **poor** Schwannian stroma (PMID:32728700) — Model B's own model fails to reproduce GN's defining feature. Favours A. |
| Is there a documented NB→GN transition in a patient? | Yes, case-level ([PMID:34054050](https://pubmed.ncbi.nlm.nih.gov/34054050/); [complete maturation of NB with bone metastases](https://www.sciencedirect.com/science/article/abs/pii/0022346875901992); [maturation of mass-screened localized adrenal NB](https://www.sciencedirect.com/science/article/abs/pii/S0022346801387067)) | Would call these GNB/NB with maturation, not GN | Case reports; cannot exclude sampling. |

**Recommended curation:** two `mechanistic_hypotheses` groups (`maturation_of_neuroblastic_precursor`, status `CANONICAL`; `de_novo_akt_activation`, status `EMERGING`), with causal edges opting into the relevant group via `hypothesis_groups`, plus a `HUMAN_MODEL_MISMATCH` discussion for the zebrafish stroma discrepancy (§15.3). Do not pick a winner in the entry prose.

### 6.5 Mechanism checklist coverage

- **Molecular pathways:** PI3K–AKT–mTOR–S6 (`GO:0043491`, `GO:0031929`); neurotrophin/TRK (`GO:0048011`); GDNF/RET (`GO:0035860`); MAPK (RET-driven, MEN2B); retinoic acid receptor signalling (`GO:0048384`) — the latter as the pharmacological analogue of the maturation programme, not as a disease mechanism. KEGG/Reactome have no GN-specific map.
- **Cellular processes:** neuronal differentiation and maturation (`GO:0030182`, `GO:0048667`); neurite outgrowth (`GO:0031175`); cell-cycle exit / reduced proliferation; Schwann cell differentiation (`GO:0014037`) and PNS myelination (`GO:0022011`, `GO:0042552`); apoptosis (the mTOR-inhibitor effector). **Notably absent:** no genome instability, no telomere maintenance, no invasion/metastasis programme — GN conforms to essentially *none* of the cancer hallmarks, which is unusual for an entry with an ICD-O morphology code.
- **Protein dysfunction:** constitutive AKT kinase activity (gain of function); PTEN phosphatase loss of function (enteric branch); RET kinase gain of function (MEN2B branch). No misfolding or aggregation.
- **Metabolic changes:** increased cap-dependent protein synthesis downstream of mTOR is the only one documented. In the minority of secretory GN, retained catecholamine biosynthesis (`GO:0042423` catecholamine biosynthetic process) producing dopamine `CHEBI:18243` and its metabolite homovanillic acid `CHEBI:545959`. No metabolomics or lipidomics study of GN exists (MetaboLights, Metabolomics Workbench, HMDB: nothing).
- **Immune involvement:** none established. The pNT single-cell study that includes GN describes an immune microenvironment with low cytotoxic T-lymphocyte content across pNTs ([GSE192906](https://www.omicsdi.org/dataset/geo/GSE192906)) but does not isolate a GN-specific immune mechanism.
- **Tissue damage mechanisms:** **mechanical compression only** — no oxidative stress, ischaemia, fibrosis, or necrosis mechanism. This is the single most important negative in the pathophysiology: GN damages tissue by occupying space.
- **Biochemical abnormalities:** none intrinsic. VIP (`VIP` hgnc:12693, verified at rest.genenames.org) hypersecretion in the rare VIPoma-like presentation; catecholamine hypersecretion in a minority (§10.1).
- **Molecular profiling:** transcriptomics as above. **Proteomics** — the Weiss 2021 study performed secretome proteomics of repair Schwann cells (PRIDE-depositable; accession not verified here). **No GN proteome, metabolome, or lipidome.**
- **Single-cell / spatial:** `GSE192906` — *"Single-cell RNA-sequencing of peripheral neuroblastic tumors reveals an aggressive transitional cell state at the junction of an adrenergic-mesenchymal transdifferentiation trajectory"*, *Homo sapiens*, 10 pNTs, deposited 2022-10-04. Weiss 2021 lists `GSE90711`, `GSE94035`, `GSE147635`, and uses `GSE45547` (Kocak) and `GSE85047` (NRC) as validation cohorts. `[Accession-to-GN-sample mapping NOT verified; before curating any of these as a `datasets:` record, run `just verify-datasets` and confirm the series actually contains ganglioneuroma samples — the §Dataset-curation rule about relevance triage applies directly, since a search on "neuroblastic tumor" returns neuroblastoma series.]`
- **Functional genomics screens:** no DepMap GN line exists (there is no ganglioneuroma cell line). This is a hard structural limit on GN functional genomics and is worth stating.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

| Site | Frequency | UBERON |
|---|---|---|
| Retroperitoneum | **45.5%** (n=46/101, PMID:42537227); 32–52% in review literature | **UBERON:0003693** retroperitoneal space (OLS4) |
| Posterior mediastinum / thoracic paraspinal | **32.7%** (PMID:42537227); 39–43% in review literature | **UBERON:0008822** posterior mediastinum (OLS4); **UBERON:0003728** mediastinum |
| Presacral space | **17.8%** (PMID:42537227) | `[No UBERON term verified; UNVERIFIED]` |
| Cervical region | **4%** (PMID:42537227) | **UBERON:0000974** neck |
| Adrenal gland | Relatively rare as a primary site; increases with age ([PMID:40799243](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339323/)) | **UBERON:0002369** adrenal gland; **UBERON:0001236** adrenal medulla |
| Sympathetic chain generally | Skull base → pelvis | **UBERON:0001806** sympathetic ganglion; **UBERON:0001807** paravertebral ganglion; **UBERON:0001805** autonomic ganglion |
| Gastrointestinal tract (ganglioneuromatosis) | Syndromic (MEN2B, PHTS, NF1) | `[colon/stomach UBERON terms not verified this session]` |
| Rare: CNS, heart, bone, bladder, uvea, paratesticular, larynx | Case-level | — |

**Secondary organ involvement** is compressive, not metastatic: spinal cord (**UBERON:0002240**) compression from dumbbell extension; ureter/kidney (hydronephrosis); great vessels (aorta, IVC, SMA, renal vessels encased in **66.7%** of retroperitoneal cases, PMID:41306794); airway.

**Body systems:** peripheral/autonomic nervous system (primary); endocrine (adrenal site, and secretory variants); gastrointestinal (ganglioneuromatosis, obstruction); musculoskeletal (scoliosis, vertebral/foraminal remodelling); genitourinary (compression).

### 7.2 Tissue and cell level

| Compartment | Cell type | CL |
|---|---|---|
| Neuronal (the "ganglio-" half) | mature ganglion cell / sympathetic neuron | **CL:0011103** sympathetic neuron (OLS4); **CL:0008025** noradrenergic neuron; **CL:0000107** autonomic neuron |
| Stromal (the "-neuroma" half, and dominant by volume) | Schwann cell | **CL:0002573** Schwann cell; **CL:0000218** myelinating Schwann cell; **CL:0002375** Schwann cell precursor |
| Perineuronal | satellite cell covering mature ganglion cells | `[No CL term verified; UNVERIFIED]` |
| Precursor lineage | neural crest cell / neural-crest-derived neuroblast | **CL:0011012** neural crest cell; **CL:0000333** migratory neural crest cell; **CL:0002676** neural crest derived neuroblast |
| Adrenal context | chromaffin cell | **CL:0000166** chromaffin cell; **CL:0000336** adrenal medulla chromaffin cell |
| Enteric ganglioneuromatosis | enteric neuron | **CL:0007011** enteric neuron; **CL:0002607** migratory enteric neural crest cell |

Tissue types: nervous tissue (both neuronal and glial) plus connective tissue (collagen fibres interlacing with Schwann-cell bundles — the origin of the **whorled sign** on MRI, §10.3) and myxoid stroma.

### 7.3 Subcellular level

Ganglion cells show **Nissl substance** — abundant rough endoplasmic reticulum — granular eosinophilic cytoplasm, a round nucleus with open chromatin and a prominent nucleolus. The relevant GO cellular-component terms (rough ER, nucleolus) `[were not resolved this session; UNVERIFIED]`. No mitochondrial, lysosomal or autophagic compartment pathology is described.

### 7.4 Localization and laterality

Solitary and **unilateral** in the overwhelming majority. Side distribution in the retroperitoneal cohort: **58.8% right, 41.2% left** (PMID:41306794) — consistent with chance, and not a biological asymmetry. Bilateral/multifocal disease should prompt a syndromic work-up (MEN2B, NF1, PHTS) rather than being treated as sporadic GN. Dumbbell (intraspinal + paraspinal) morphology is the configuration with the highest neurological stakes.

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** see §3.3. Median **62 months** in a national paediatric cohort vs mean **26.9 years** in a neurosurgical cohort — the discrepancy is **ascertainment**, not two diseases: paediatric GN is found through neuroblastic-tumour pathways, adult GN through incidental imaging.
- **Pattern: insidious and chronic.** The tumour is typically present for years before detection. Acute presentation occurs only via a complication (obstruction, cord compression).
- **Congenital?** Not described as congenital. Secondary GN maturing from a neuroblastoma presents in young children; primary GN in late childhood and adulthood.

### 8.2 Progression

- **No disease-specific staging system.** GN is non-metastatic by definition; where a stage is recorded it is borrowed (INSS/INRGSS) from the pNT family. For surgical planning, **imaging-defined risk factors (IDRFs)** are the operative analogue of stage — and they predict *complications*, not outcome: IDRF presence correlated with post-operative complications at **p = 0.005** (PMID:29369484).
- **Progression rate: slow, often zero.** Median **0.3 cm/year** (PMID:29369484); **0.08–0.17 cm/year** in the two growing tumours of a 31-patient observation arm followed a mean of **90.9 ± 151 months** (PMID:42537227).
- **Course: stable to very slowly progressive.** Not episodic, not relapsing-remitting. In the Alexander series, at median 2.2 years: 27 complete + 10 partial responses, 19 stable, **6 progressive** of 67.
- **Duration: lifelong** if unresected, with no natural resolution. Spontaneous regression — the hallmark of infant neuroblastoma — is **not** a feature of GN.
- **The one real progression risk is reclassification, not growth.** In the UK CCLG cohort, *"In 45 cases (39%), surgical pathology was different from pathology at biopsy, and in 14 (12%) the pathology changed from GN/GNBi to neuroblastoma/GNB nodular."* (PMID:39582110). Contrast with the single-centre Toronto series, where *"Pathology classification changed at resection for three cases, but no GN was reclassified to NB"* (PMID:29369484). The two findings are not contradictory — 12% of 259 vs 0% of 67 is within sampling range — but the larger cohort is the one to plan around.

### 8.3 Patterns

- **Remission:** treatment-induced only (resection). No spontaneous remission.
- **Critical periods:** two, both iatrogenic. (i) The **first year of life** in MEN2B, when intestinal ganglioneuromatosis presents and a rectal biopsy can make the diagnosis years before medullary thyroid carcinoma — the single highest-yield intervention window in the whole GN space. (ii) The **decision point at diagnosis** in sporadic GN, where the choice between resection and surveillance determines the 20–43% complication exposure (§11.2). There is no window in which GN itself becomes more dangerous with time, which is precisely why surveillance is defensible.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence ≈ 1 per million population.** Verbatim: *"Ganglioneuroma is a rare neurogenic tumor with a prevalence of one per million population"* ([Cureus 2023;15:e43914, **PMID:37746449**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10512760/)). `[This is a secondary/tertiary claim repeated across the case-report literature; its primary source was not traced. Treat as PrevalenceClassEnum BELOW_1_IN_1000000 / BAND_1_9_PER_1000000 with measure_type UNKNOWN and record the attribution honestly.]`
- **Proportion of primary retroperitoneal tumours: 0.72–1.6%** (same source, verbatim: *"Ganglioneuromas constitute only 0.72%–1.6% of all primary retroperitoneal tumors"*).
- **0.1–0.5% of all neurogenic tumours** (review literature).
- **≈3% of peripheral neuroblastic tumours** reviewed at the COG Neuroblastoma Pathology Reference Laboratory ([Shimada 2020](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73)) — the most defensible denominator-based figure available.
- **Incidence:** no population-based incidence rate exists. GN is not separately reported in SEER (SEER work exists for ganglioneuroblastoma: 1,194 patients, 5-year survival ~88%, [PMC11107237](https://pmc.ncbi.nlm.nih.gov/articles/PMC11107237/)); because GN is coded benign (ICD-O 9490/**0**), US cancer registries do not capture it. **This is the structural reason no incidence figure exists, and it should be stated rather than approximated.**

### 9.2 Genetic etiology parameters

GN itself is **not inherited**; the predisposing syndromes are:

| Syndrome | Gene | Inheritance | Penetrance for the ganglioneuromatous feature |
|---|---|---|---|
| MEN2B | `RET` hgnc:9967 | Autosomal dominant; ~50% de novo | Diffuse intestinal ganglioneuromatosis described as a **universal** extra-endocrine feature; GI symptom onset <1 year in 52.3% |
| Cowden / PHTS | `PTEN` hgnc:9588 | Autosomal dominant | Low/undefined for GN specifically; PTEN LOF in ~80% of Cowden |
| NF1 | `NF1` hgnc:7765 | Autosomal dominant; ~50% de novo | Very low — 2 GN among 8 NF1 patients within 0.2% of an Italian neuroblastic-tumour registry |

- **Founder effects / carrier frequency / consanguinity / anticipation / germline mosaicism:** **not applicable to GN.** These belong to the syndrome entries, not here. Do not populate them.
- **Expressivity:** highly variable in MEN2B — the same M918T allele gives everything from isolated intestinal ganglioneuromatosis to the full MTC/pheochromocytoma/marfanoid syndrome.

### 9.3 Population demographics

- **Sex.** Adult surgical series are consistently **female-predominant**: 62.3% female (n=101, PMID:42537227); 33/51 = 64.7% female (PMID:41306794); 18/25 = 72% female (PMID:41561749). Paediatric review literature quotes M:F ≈ **2:3**. One adrenal-GN review states *"There are no significant sex differences in morbidity"* ([PMID:40799243](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339323/)). **Interpretation:** a modest female excess in resected series, possibly reflecting imaging utilisation rather than biology. Record it as observed, not as a sex-specific disease.
- **Age distribution.** ~60% under 20 at diagnosis in paediatric-weighted literature; adrenal GN specifically is *"rare in children under 10 years of age, with a higher incidence in adults than in children, and its incidence increases with age"* (PMID:40799243) — i.e. site and age interact.
- **Ancestry / geography.** No ethnic predilection and no endemic region described. No HANCESTRO-bindable population effect exists. `[Do not curate a population_effects record: there are no population-stratified data.]`

---

## 10. Diagnostics

### 10.1 Laboratory tests and biomarkers

- **Core panel:** plasma/urinary metanephrines and catecholamines, urinary **VMA** (`CHEBI:20106` vanillylmandelic acid) and **HVA** (`CHEBI:545959` homovanillic acid), plus adrenal-incidentaloma screening (cortisol excess, aldosterone/renin) where adrenal.
- **The expected result is normal.** In the 51-patient retroperitoneal cohort, catecholamine/VIP testing was performed in 13 patients and **all were negative** (PMID:41306794).
- **The informative abnormal pattern** is dopamine/HVA elevation with normal adrenaline, noradrenaline and VMA — reported in four children with GN, and the mirror image of neuroblastoma (where noradrenaline, dopamine, HVA **and** VMA are typically raised) ([*Pathology* / catecholamines in urine and tumour tissue](https://www.sciencedirect.com/science/article/abs/pii/S0031302516393552)). This asymmetry is mechanistically sensible: mature ganglion cells retain upstream synthesis (`GO:0042423`) without the full secretory phenotype.
- **~30% of adrenal GN reported with elevated catecholamines** — widely repeated but `[secondary claim, primary source not traced; UNVERIFIED]`. Case reports document raised norepinephrine, normetanephrine, VMA and dopamine with suppressed epinephrine ([PMC9242669](https://pmc.ncbi.nlm.nih.gov/articles/PMC9242669/)).
- **Rare secretory syndromes:** VIP (`VIP` hgnc:12693) → watery diarrhoea, hypokalaemia, failure to thrive; ACTH/cortisol; androgens → virilization. One 80-case adrenal series reported 3 patients with elevated 24-hour urinary cortisol (PMID:40799243).
- **LOINC.** The relevant measurements (VMA, HVA, plasma free metanephrines, VIP) all have LOINC codes, but **none was looked up in this session.** Per the repo's rule, do **not** type a LOINC label from memory — run `just loinc-seed-cache` and commit `cache/loinc/terms.csv` with the entry. `[UNVERIFIED]`

### 10.2 Biomarkers for prognosis

None. There is no prognostic biomarker for GN because there is nothing to prognosticate — survival is essentially 100% (§11.1). The only predictive marker of interest is **phospho-S6 / phospho-AKT status** as a candidate biomarker for mTOR-inhibitor responsiveness, which has never been tested prospectively.

### 10.3 Imaging

**CT** (`NCIT:C17204` Computed Tomography):
- Low attenuation, **< 40 HU** unenhanced; homogeneous or slightly heterogeneous.
- **Gradual and delayed enhancement** — minimal arterial-phase, progressive portal and delayed-phase enhancement. This pattern reflects the myxoid, hypovascular Schwannian stroma and is one of the better discriminators from pheochromocytoma.
- **Calcification in 42–60%**, characteristically **discrete and punctate** rather than the amorphous coarse calcification of neuroblastoma.
([AJR imaging reviews](https://ajronline.org/doi/10.2214/AJR.16.16018); [*Diagnostics* 2023;13:2190, PMC10341194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10341194/); [PMID:22573298](https://pubmed.ncbi.nlm.nih.gov/22573298/))

**MRI** (`NCIT:C16809` Magnetic Resonance Imaging):
- **T1: low** signal; **T2: heterogeneously high** signal; gradual delayed enhancement.
- **"Whorled sign"** — interlacing thick bundles of Schwann cells and collagen — reported in about **80%** of patients and the most characteristic MRI feature ([PMC10341194](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10341194/); [PMC6647925](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647925/)).
- Mean dimensions **8.5 ± 3.8 × 6.6 ± 3.2 × 5.8 ± 3.7 cm** (PMID:42537227).

**Functional imaging:** **low or absent MIBG uptake** and no significant FDG avidity — in contrast to neuroblastoma and pheochromocytoma. Note the exception: an adrenal GN with nodal involvement showing uptake on both ¹²³I-MIBG SPECT/CT and ¹⁸F-FDG PET/CT has been published ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1930043324007155)), so low uptake is a tendency, not a rule.

**The imaging pitfall is over-reliance.** A giant retroperitoneal GN was misdiagnosed on radiology alone (PMID:37746449) — the paper's title is literally *"Overreliance on Radiological Findings Leading to Misdiagnosed Giant Retroperitoneal Ganglioneuroma."* Imaging narrows, histology decides.

### 10.4 Functional tests and electrophysiology

No role in diagnosis. Intra-operative neuromonitoring is used during paraspinal/dumbbell resection to limit the 22.2% neurological-deficit rate (§11.2), which is a surgical adjunct rather than a diagnostic test.

### 10.5 Biopsy, histopathology and immunohistochemistry

**Gross:** well-circumscribed, firm, grey-white to tan, often lobulated, with a whorled cut surface.

**Microscopic:** mature ganglion cells with granular eosinophilic cytoplasm, round nuclei with prominent nucleoli and Nissl substance, scattered individually or in small clusters, embedded in a **dominant** stroma of spindled Schwann cells and collagen within a myxoid background. Satellite cells cover the mature ganglion cells. **Mitoses absent**; Ki-67 hotspot index **<1%** ([PMID:40799243](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339323/)).

The **maturing vs mature** distinction turns entirely on neurite incorporation ([Shimada 2020](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73)):

| Subtype | Criterion |
|---|---|
| **Maturing** GN | Neuritic processes from neuroblastic cells are **incompletely** incorporated into Schwann-cell cytoplasm; a mixture of mature and maturing ganglion cells |
| **Mature** GN | *"composed only of completely mature ganglion cells covered with satellite cells"*; *"all neuritic processes produced by ganglion cells are immediately incorporated in the cytoplasm of Schwann cells, so that no naked neuritic processes are detected"* |
| **Ganglioneuroblastoma, intermixed** (not GN) | *"foci of naked neurites are still identified microscopically"* |

**Immunohistochemistry — note a genuine conflict in the literature:**

| Marker | Compartment | Reported |
|---|---|---|
| **S100** | Schwannian stroma | Positive (consistent across sources) |
| **SOX10** | Schwannian stroma | Positive; `SOX10` is transcriptionally **up** in GN (PMID:32728700) |
| **Synaptophysin** | Ganglion cells | Positive |
| **NSE** | Ganglion cells | Positive |
| **Neurofilament** | Ganglion cells / neurites | Positive (composite-tumour literature) |
| **PHOX2B** | Ganglion cell nuclei | **Conflict.** A 2025 adrenal-GN report records PHOX2B **negative** ([PMID:40799243](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339323/)), whereas the diagnostic-IHC literature reports *"Phox2b expression was seen in all neuroblastomas, ganglioneuroblastomas, and ganglioneuromas"* with *"nuclear positivity in all of the ganglion cells across the different phases of differentiation"*, and 70/76 (92%) of pNTs positive overall ([PMID:28640941](https://pubmed.ncbi.nlm.nih.gov/28640941/); [PHOX2B immunolabeling](https://www.researchgate.net/publication/229081877_PHOX2B_Immunolabeling_A_Novel_Tool_for_the_Diagnosis_of_Undifferentiated_Neuroblastomas_Among_Childhood_Small_Round_Blue-cell_Tumors)) |
| **Tyrosine hydroxylase (TH)** | Ganglion cells | **Conflict**, same pattern: reported negative in one adrenal GN (PMID:40799243) but *"Strong expression of PHOX2A, PHOX2B, and TH in both neuroblastoma and ganglioneuroma"* elsewhere, and strongly reactive in all cell types of composite pheochromocytoma-ganglioneuroma ([PMC3685741](https://pmc.ncbi.nlm.nih.gov/articles/PMC3685741/)) |
| **Chromogranin A** | — | Generally negative in GN (positive in pheochromocytoma) |

**How to curate the conflict:** the case-report negatives are *n*=1–2 observations on a single adrenal tumour; the systematic IHC studies are cohort-level and consistently positive. Bind PHOX2B and TH as expressed in ganglion cells, and record the discordant case-level reports in `notes:` rather than as a `REFUTE` evidence item — they most likely reflect antibody, fixation, or a tumour whose ganglion cells are too few to sample, not a biological disagreement.

**Differential diagnosis**

| Entity | Distinguishing features |
|---|---|
| Neuroblastoma | Undifferentiated/poorly differentiated neuroblasts, **Schwannian stroma-poor**, high mitosis-karyorrhexis index; **PHOX2B and NB84 strongly positive**; raised VMA/HVA; avid MIBG; MYCN may be amplified |
| Ganglioneuroblastoma, intermixed | Microscopic **naked neurite** foci persist |
| **Ganglioneuroblastoma, nodular** | Discrete neuroblastic nodule within ganglioneuromatous tissue — the one differential with real mortality (8-yr OS 33.2% in the unfavourable subset, PMID:14601099) |
| Pheochromocytoma | Catecholamine excess; chromogranin A, TH positive; avid MIBG; Zellballen architecture |
| Schwannoma | Alternating Antoni A/B, nuclear palisading, **Verocay bodies**, no ganglion cells |
| Neurofibroma | No ganglion cells; different stromal architecture |
| **Composite pheochromocytoma–ganglioneuroma** | Both components present; **<3% of sympathoadrenal pheochromocytomas**, reported range 1–9% of pheochromocytomas; MEN2A association ([PMC3685741](https://pmc.ncbi.nlm.nih.gov/articles/PMC3685741/); [Am J Surg Pathol 1997](https://www.ovid.com/jnls/ajsp/abstract/00000478-199701000-00011~composite-pheochromocytomaganglioneuroma-of-the-adrenal?redirectionsource=fulltextview); [PMC9518729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9518729/)) |
| Adrenal schwannoma with GN component | Reported ([PMC11446904](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11446904/)) |
| Retroperitoneal sarcoma | The practical misdiagnosis in adults with large masses |

### 10.6 The central diagnostic problem: biopsy understaging

This deserves its own statement because it governs management. **A needle biopsy showing ganglioneuroma does not exclude a neuroblastic nodule elsewhere in the lesion.** The UK CCLG national cohort is the key evidence: *"In 45 cases (39%), surgical pathology was different from pathology at biopsy, and in 14 (12%) the pathology changed from GN/GNBi to neuroblastoma/GNB nodular."* And the authors' own caveat: *"a small proportion of patients in the observation group had their diagnosis revised to malignant at surgery"* (PMID:39582110).

Mechanistically this is unavoidable: GNB-nodular is **defined** by focal heterogeneity, so any sampling strategy short of whole-tumour examination has a non-zero miss rate. This is the strongest argument against unqualified "watch and wait", and the reason the 2026 recommendation is *individualised*, not surveillance-by-default.

### 10.7 Genetic testing

**For sporadic GN: none indicated.** WGS, WES, gene panels, CMA, karyotyping, FISH, mtDNA testing and repeat-expansion testing have **no established role**, because there is no causal gene and no recurrent somatic lesion.

**For syndromic suspicion, targeted single-gene testing is high-yield:**
- `RET` (exon 16, M918T) when there is mucosal neuroma, marfanoid habitus, alacrima, early-onset constipation, or **any** diffuse intestinal ganglioneuromatosis. **Rectal biopsy is an established early-diagnosis route to MEN2B** ([PMID:27899172](https://pubmed.ncbi.nlm.nih.gov/27899172/)).
- `PTEN` for ganglioneuromatous polyposis, diffuse gastric ganglioneuromatosis, macrocephaly, or Cowden features.
- `NF1` where café-au-lait macules/neurofibromas coexist.

### 10.8 Omics-based diagnostics

**None clinically available or validated.** No RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic exists for GN. The honest statement for the KB is that GN diagnosis is histological, and the molecular layer is research-only.

### 10.9 Clinical criteria and screening

- **Diagnostic criteria:** INPC histological criteria (§10.5) are the standard; there is no clinical criterion set, no DSM/ICD symptom checklist, and no society guideline specific to GN.
- **Screening of asymptomatic individuals:** no population screening. Historically, Japanese infant neuroblastoma mass screening detected maturing/localised adrenal lesions ([maturation of mass-screened localized adrenal neuroblastoma](https://www.sciencedirect.com/science/article/abs/pii/S0022346801387067)) — relevant context, but mass screening was abandoned for overdiagnosis, which is itself the central argument of this entry in miniature.
- **Cascade/targeted screening is justified only in the syndromes:** `RET` cascade testing in MEN2B families; periodic biochemical and imaging evaluation in NF1 given raised pheochromocytoma and GN prevalence.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality — essentially unaffected

| Series | n | Follow-up | Outcome |
|---|---|---|---|
| Burnand 2025, UK CCLG (PMID:39582110) | 259 (163 GN, 93 GNBi) | 1990–2020 | **Overall survival 98%** |
| Li 2025, *Front Surg* (PMID:41306794) | 51 retroperitoneal | median **62 months**, 90.2% complete | *"no recurrences, metastases, or disease-specific deaths occurred"* |
| Texakalidis 2026, *J Neurosurg* (PMID:42537227) | 101 | mean 33.8 ± 42.6 months | Recurrence **2/70 (2.9%)**; *"No malignant transformations were observed"* |
| Ozcelik 2026, *Front Oncol* (PMID:41561749) | 25 adults | median **88.3 months** (16.2–217.8) | *"no distant metastases or recurrences were observed during follow-up"* |
| Alexander 2018 (PMID:29369484) | 67 | median 2.2 years | All patients alive |

Life expectancy is normal. Disease-specific mortality is effectively zero — and note that the one death in the 51-patient cohort was **operative** (post-operative day 8, bowel ischaemia with septic shock), not from GN.

**Regional lymph node involvement occurs and does not matter.** Ozcelik et al. found nodal metastases in **2/25 (8%)** — 5/12 nodes positive in one patient, 4/4 in another — with no distant metastasis or recurrence at median 88.3 months. Their title states the finding: *"Ganglioneuroma has a potential for lymph node metastasis, not impacting recurrence."* Pathologically this looks alarming on a report; prognostically it is inert. `[Important for curation: do not model nodal involvement as a metastasis node with adverse consequence.]`

**Malignant transformation** to MPNST is the only lethal trajectory, and it is vanishingly rare: approximately **ten reported cases** of MPNST arising in GN, de novo or at a previously irradiated site, as of the early 2000s ([PMID:10755757](https://pubmed.ncbi.nlm.nih.gov/10755757/); [Drago 1997, *Med Pediatr Oncol*](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1096-911X(199703)28:3%3C216::AID-MPO13%3E3.0.CO;2-C); [PMC12221925](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221925)). Both of the two largest modern cohorts observed **zero** transformations.

### 11.2 Morbidity is iatrogenic, and it is substantial

This is the real outcome story, and the asymmetry between it and §11.1 is what the whole management literature is about.

| Series | Complication rate | Detail |
|---|---|---|
| Texakalidis 2026 (PMID:42537227) | **43.1%** short-term | *"most commonly neurological deficits (22.2%)"* |
| Alexander 2018 (PMID:29369484) | **30%** (15/50) | IDRF presence correlated with complications, **p = 0.005** |
| Li 2025 (PMID:41306794) | **21.6%** | Clavien-Dindo I/II in 90.9%; **Grade V (death) 9.1% of complications** = 1 patient. Gastroparesis ×3, pancreatic fistula ×3, transaminitis ×2, wound infection ×2. Multivisceral resection in **27.5%** |
| Burnand 2025 (PMID:39582110) | **19%** with GTR | — |

Dumbbell/paraspinal resection carries the highest neurological cost. A systematic review of dumbbell spinal tumours with nerve-root sacrifice (121 patients, 12 studies) found immediate motor deficits in **46%** (95% CI 31–62%) and persistent deficits in **21%** (95% CI 14–31%) ([Eur Spine J](https://link.springer.com/article/10.1007/s00586-026-09903-3)). A GN-specific paraspinal series of 15 reported **no permanent** neurological deficits, with one transient bilateral lower-extremity weakness resolving in 4 weeks ([J Neurosurg Spine 2022;37:130](https://thejns.org/spine/view/journals/j-neurosurg-spine/37/1/article-p130.xml)).

### 11.3 Complications

Of the **disease**: compressive — cord compression, radiculopathy, hydronephrosis, bowel obstruction (especially in ganglioneuromatosis), scoliosis, airway compression; secretory diarrhoea/hypokalaemia; hypertension.
Of **treatment**: neurological deficit, Horner syndrome, chylothorax, nephrectomy, pancreatic fistula, haemorrhage, gastroparesis, infection, death.
Of **radiotherapy**: late MPNST.

### 11.4 Recovery potential and prognostic factors

Recovery after resection is good: 42.3% improved and 46.5% stable from baseline (PMID:42537227); complete symptom control in 43% with GTR vs 24% without (PMID:39582110).

**Prognostic factors — note what they are *for*.** Nothing predicts survival, because survival is near-universal. What is predictable is **surgical morbidity**, and it is predicted by: IDRF presence (p=0.005), vascular encasement (66.7% of large retroperitoneal tumours), tumour size, intraspinal/dumbbell extension, and need for multivisceral resection. **Subtotal resection does not worsen outcome:** *"STR provides excellent long-term control when required to avoid morbidity"* (PMID:42537227), and the 6 R2-resection patients in the retroperitoneal cohort showed stable disease without progression (PMID:41306794). That is the single most actionable prognostic statement in the literature.

---

## 12. Treatment

### 12.1 The treatment principle

Surgery is the only established therapy, and the only question is whether to use it. Verbatim from Tao et al.: *"Surgery is the only effective therapy for ganglioneuroma, which may be challenging due to the location of the tumor and involvement of surrounding structures."* (PMID:32728700)

### 12.2 Surgical and interventional

| Treatment | NCIT (verified in `cache/ncit/terms.csv`) | Notes |
|---|---|---|
| Surgical resection | **NCIT:C15329** Surgical Procedure; **NCIT:C154430** Definitive Surgical Resection; **NCIT:C164212** Tumor Resection | GTR achieved in **73.6%** (PMID:42537227), **79%** (PMID:39582110); R0/R1 in **88.2%** (PMID:41306794) |
| Gross total resection | **NCIT:C131672** Gross Total Resection; **NCIT:C175027** Complete Resection | Best symptom control (43% vs 24%) |
| Subtotal / debulking | — | **Deliberate** strategy when adjacent to critical structures; excellent long-term control |
| Adrenalectomy (laparoscopic) | **NCIT:C15177** Adrenalectomy | *"Laparoscopic resection is the primary treatment for AGN"*, and *"laparoscopic surgery is still applicable even when the tumor diameter exceeds 6 cm"* (PMID:40799243). Open 80.4% vs laparoscopic 19.6% in the large-tumour retroperitoneal cohort (PMID:41306794) |

**Where it should be done:** *"While surgical resection remains the cornerstone of management, it is best undertaken at specialized, high-volume sarcoma centers to mitigate operative risks."* (PMID:41306794)

### 12.3 Active surveillance — a first-line treatment, not a non-treatment

| Treatment | NCIT | Evidence |
|---|---|---|
| Observation / active surveillance | **NCIT:C15722** Patient Observation | 58/259 = **22%** observed, OS 98%; **21/58 (36%)** required subsequent surgery, 52% of those for progressive growth (PMID:39582110). 31/101 observed, mean follow-up **90.9 months**, no new symptoms, 2 tumours grew 0.08–0.17 cm/yr; observation chosen for **proximity to major vascular or neural structures in 74.2%** (PMID:42537227). 21/67 observed, 4 later resected (PMID:29369484) |

Verbatim conclusions, which diverge in emphasis and should both be recorded:
- *"Watch and wait approaches should be considered for some GN and GNB-I."* (PMID:29369484)
- *"Watchful active observation can be a safe approach, with surgical resection reserved for symptomatic patients. However, a small proportion of patients in the observation group had their diagnosis revised to malignant at surgery."* (PMID:39582110)
- *"Observation is safe for asymptomatic tumors, particularly when adjacent to critical structures... These findings support an individualized, risk-based approach to management."* (PMID:42537227)

Also reported: a presacral GN followed **6 years without surgery** ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S193004332030282X)).

### 12.4 Pharmacotherapy — mTOR inhibition is the one real therapeutic hypothesis

There is **no approved drug for GN and no completed or active clinical trial.** What exists is a well-constructed preclinical proposal.

| Agent | CHEBI | NCIT | Preclinical result (PMID:32728700) |
|---|---|---|---|
| Sirolimus (rapamycin) | **CHEBI:9168** | **NCIT:C1212** | Adult fish with primary GN, 35 days: **30–40% tumour-burden reduction** vs ~1.5-fold increase in DMSO controls. ~50% reduction in transplant assay (p<0.0001) |
| Everolimus | **CHEBI:68478** | **NCIT:C48387** | Same, 30–40% reduction |
| INK128 (TORC1/2) | — | — | ~50% reduction in transplant assay; strongest 4E-BP1 inhibition |
| MK-2206 (AKT inhibitor) | — | — | **No effect** — expected negative control against a myristoylated, membrane-targeted AKT |

Drug class: **NCIT:C2201** mTOR Inhibitor. `[If curating as therapeutic_agent, NCIT:C2201 must be checked against the ChemicalEntityTerm dynamic enum rooted at NCIT:C1909 Pharmacologic Substance — run just validate-terms after binding. Prefer the CHEBI terms for the named drugs.]`

Mechanism of the response: increased apoptosis (sub-G1 fraction, TUNEL-confirmed) with marked inhibition of phospho-S6.

The authors' proposal, verbatim: *"We propose a clinical trial of mTOR inhibitors as a means to shrink large ganglioneuromas before resection in order to reduce surgical morbidity."* The commentary notes sirolimus and everolimus are already FDA-approved in paediatric patients and that mTOR inhibition is established in tuberous sclerosis, so safety is not the barrier ([*Mol Cell Oncol* 2020, PMID:33553609](https://pmc.ncbi.nlm.nih.gov/articles/PMC7849689)).

**Why this is strategically the right target:** GN kills essentially nobody, so there is no survival endpoint to improve. The morbidity is surgical and scales with tumour size and anatomical entanglement. A neoadjuvant agent that shrinks the tumour attacks the **actual** source of harm. That reframing — treat the surgery, not the tumour — is the most interesting clinical idea in this disease.

**No trial exists.** A search of ClinicalTrials.gov returned mTOR-inhibitor trials in MPNST (NCT03433183 selumetinib+sirolimus; NCT01661283 everolimus+bevacizumab) and NF1 plexiform neurofibroma (NCT00634270 sirolimus), **none in ganglioneuroma**. `[No NCT identifier is curatable for this entry. Record the proposal as a mechanistic_hypotheses / KNOWLEDGE_GAP with proposed_experiments, not as a clinical_trials entry.]`

### 12.5 What has no role

- **Chemotherapy** (`NCIT:C15632`): no role in GN.
- **Radiotherapy** (`NCIT:C15313`): no role, and it is the one documented exogenous risk factor for later MPNST within a GN. This is a treatment that should be recorded with its harm, not just its absence of benefit.
- **Gene therapy, cell therapy, CAR-T, RNA therapeutics (ASO/siRNA), immunotherapy, checkpoint inhibitors:** none, none proposed, none plausible for a benign non-progressive lesion. `[Leave therapeutic_modality and oligonucleotide_details absent.]`
- **Pharmacogenomics:** nothing — no drug, no PharmGKB/CPIC entry.

### 12.6 Supportive, rehabilitative and counselling

- **NCIT:C15747** Supportive Care — analgesia, bowel management in ganglioneuromatosis, nutritional support with secretory diarrhoea, alpha-blockade before resecting a catecholamine-secreting lesion `[perioperative blockade protocol not sourced in this session; UNVERIFIED]`.
- **NCIT:C15315** Rehabilitation — post-operative physical therapy for the 22.2% with neurological deficits.
- **NCIT:C15240** Genetic Counseling — for MEN2B/PHTS/NF1 families, including cascade testing and reproductive options.

### 12.7 Treatment algorithm

1. Lesion identified → cross-sectional imaging (CT/MRI) looking for the GN signature (low HU, delayed enhancement, punctate calcification, whorled sign, low MIBG).
2. Biochemical screen (metanephrines/catecholamines, VMA/HVA; adrenal panel if adrenal).
3. Tissue diagnosis — **and read §10.6 before trusting it.**
4. Screen for a syndrome if multifocal, GI-diffuse, or syndromic stigmata → `RET` / `PTEN` / `NF1`.
5. Decide on the morbidity axis, not the oncology axis:
   - **Symptomatic, or growing, or resectable without critical-structure risk** → resection, at a high-volume centre, aiming for GTR but accepting STR over deficit.
   - **Asymptomatic and abutting major vessels/nerves** → active surveillance with interval imaging, accepting a ~36% eventual-surgery rate and a small reclassification risk.
6. Residual tumour after STR → surveillance; it stays stable.
7. **No** adjuvant chemotherapy or radiotherapy.

**Personalised medicine:** phospho-AKT/phospho-S6 status is the only candidate stratifier (90.9%/90.9% positive), and it has never been used to select therapy. No CIViC, OncoKB or My Cancer Genome entry exists for GN.

---

## 13. Prevention

### 13.1 Primary prevention

**None exists for sporadic GN** — there is no modifiable risk factor to remove, no vaccine target, no behavioural intervention, and no prophylactic agent. This should be stated as a fact about the disease, not a gap.

The one genuine primary-prevention statement is negative and iatrogenic: **avoid radiotherapy to a ganglioneuroma or its site**, because the small MPNST risk is concentrated in previously irradiated lesions.

### 13.2 Secondary prevention — early detection where it changes outcome

The high-value prevention in this space is **not** about GN at all; it is about using GN as a sentinel.

- **Rectal biopsy for intestinal ganglioneuromatosis in an infant with severe constipation → `RET` testing → MEN2B diagnosis → prophylactic thyroidectomy before medullary thyroid carcinoma.** GI symptoms precede age 1 in 52.3% of MEN2B cases, and MTC is the cause of death. This converts a benign nerve lesion into a life-saving diagnostic ([PMID:27899172](https://pubmed.ncbi.nlm.nih.gov/27899172/); [Springer 2021](https://link.springer.com/article/10.1007/s12020-021-02607-2); [Pediatrics 2024, "Clues for Early Diagnosis of MEN2B Syndrome Before Medullary Thyroid Carcinoma"](https://publications.aap.org/pediatrics/article/154/3/e2022059517/198957/Clues-for-Early-Diagnosis-of-MEN2B-Syndrome-Before)).
- **NF1 surveillance:** periodic clinical evaluation with biochemical testing and imaging, justified by the raised prevalence of pheochromocytoma and GN.
- **PHTS/Cowden:** standard PTEN surveillance (breast, thyroid, endometrial, renal, GI), with ganglioneuromatous polyposis as a possible index finding.

- **Population screening: not indicated, and actively harmful.** There is no newborn or population screening for GN, and the Japanese infant neuroblastoma mass-screening experience is the cautionary precedent — screening detected lesions that would have matured or regressed.

### 13.3 Tertiary prevention

- Interval imaging surveillance of unresected or subtotally resected tumours (no growth expected; two of 31 grew 0.08–0.17 cm/yr).
- Long-term follow-up after incomplete resection **and especially after radiotherapy**, given the MPNST signal: the literature stresses *"the importance of close clinical and radiologic follow-up in patients with high-risk ganglioneuroma... particularly after incomplete resection and radiotherapy."*
- Operate at high-volume centres to reduce the 20–43% complication exposure — the highest-yield tertiary prevention available.
- Bowel management and nutritional support in ganglioneuromatosis to prevent obstruction and failure to thrive.

### 13.4 Immunization, public health, environmental interventions

**Not applicable.** No vaccine, no sanitation/vector/health-education intervention, no environmental exposure to reduce. Record as not applicable rather than absent.

### 13.5 Genetic screening and counselling

- **Carrier screening, prenatal testing, PGD:** available for the *syndromes* (`RET`, `PTEN`, `NF1`) and inappropriate for GN itself.
- **Risk stratification:** the only meaningful stratifier is "syndromic vs sporadic", determined clinically (multifocality, diffuse GI involvement, marfanoid habitus, mucosal neuromas, macrocephaly, café-au-lait macules).

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and natural occurrence

Species with naturally occurring ganglioneuroma or ganglioneuromatosis reported in the veterinary literature (all NCBITaxon CURIEs verified in `cache/ncbitaxon/terms.csv`):

| Species | NCBITaxon | Report |
|---|---|---|
| Human | **NCBITaxon:9606** | — |
| Dog | **NCBITaxon:9615** | Intestinal ganglioneuromatosis reported; a single cutaneous GN case existed in the dog literature as of 2011. Adrenal **neuroblastoma** also described in a young dog ([Front Vet Sci 2019;6:161](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00161/pdf)) |
| Cattle | **NCBITaxon:9913** | **First report of cutaneous ganglioneuroma in cattle**, 2011 ([ResearchGate](https://www.researchgate.net/publication/226171812_Cutaneous_ganglioneuroma_in_a_cattle_case_report)) |
| Goat (Boer) | **NCBITaxon:9925** | Intestinal ganglioneuromatosis |
| Pig (piglet) | **NCBITaxon:9823** | Intestinal ganglioneuromatosis |
| Horse | **NCBITaxon:9796** | Intestinal ganglioneuromatosis |

Summary from the veterinary literature: *"Intestinal ganglioneuromatosis is exceedingly rare in domestic animals and has only been reported in dogs, a Boer goat, a piglet, and a horse."*

### 14.2 Breed and OMIA

**No breed predisposition (no VBO term) and no OMIA entry for ganglioneuroma were located.** This is expected — OMIA catalogues inherited traits, and no animal GN has been shown to be heritable. `[Searched; absent rather than unsearched.]`

### 14.3 Orthologous genes

Orthologues exist for every gene in §0 (`AKT1/2/3`, `MTOR`, `PTEN`, `RET`, `NF1`, `PHOX2B`, `NTRK1`, `SOX10`) across mouse, rat and zebrafish. `[Specific NCBI Gene IDs for non-human orthologues were not resolved this session; UNVERIFIED.]` Note that the zebrafish model (§15.1) used **murine** *myr-Akt2* driven by a **zebrafish** *dβh* promoter — a cross-species construct, which matters for how faithfully it models human AKT biology.

### 14.4 Comparative biology and evolutionary conservation

The sympathoadrenal developmental programme — neural crest migration, PHOX2B/HAND2-driven noradrenergic specification, RET/GDNF-dependent enteric colonisation, and PI3K/AKT control of progenitor survival — is deeply conserved across vertebrates. That conservation is what makes both the zebrafish and mouse models (§15) interpretable at all. The **divergence** worth recording: the zebrafish interrenal gland substitutes for the mammalian adrenal medulla, and the zebrafish AKT tumour has **poor** Schwannian stroma where the human tumour is stroma-*dominant* — so the conserved part is the neuronal arm, and the glial/stromal arm is not reproduced.

### 14.5 Transmission

**Not applicable.** GN is a neoplasm: no zoonotic potential, no cross-species susceptibility, no transmission of any kind.

---

## 15. Model Organisms

### 15.1 Zebrafish — the only dedicated ganglioneuroma model

**Tao T, Shi H, Wang M, Perez-Atayde AR, London WB, Gutierrez A, Lemos B, Durbin AD, Look AT. *J Exp Med* 2020;217(10):e20191871. PMID:32728700.**

| Attribute | Detail |
|---|---|
| Species | *Danio rerio*, **NCBITaxon:7955** |
| Model type | Stable transgenic (two independent lines, myr-Akt2#1 and #2) |
| Construct | `Tg(dβh:mCherry; dβh:myr-Akt2)` — constitutively activated **murine** myristoylated Akt2 under the zebrafish *dopamine-β-hydroxylase* promoter |
| Target lineage | Peripheral sympathetic nervous system progenitors; lesions arise in the **interrenal gland** (zebrafish adrenal-medulla equivalent) from differentiated sympathoadrenal cells |
| Onset / penetrance | Tumours from **13 weeks post-fertilisation**; **40–50% penetrance by 29 wpf** |
| Phenotype recapitulated | Differentiated, large, mature ganglion cells; low N:C ratio; open chromatin; prominent nucleoli; abundant eosinophilic cytoplasm. HuC+, synaptophysin+. **No progression to neuroblastoma over 29 weeks.** Adrenergic CRC (`TFAP2B`, `ISL1`, `GATA3`, `PHOX2A`, `PHOX2B`) down; `SOX10` up — matching human GN |
| Pharmacological validation | Sirolimus and everolimus each reduced tumour burden 30–40% over 35 days; INK128 ~50% in transplant assay; MK-2206 no effect (expected) |
| Research applications | Mechanism of AKT-driven ganglion-cell expansion; preclinical mTOR-inhibitor testing; transplantation-based drug screening in *casper* recipients |
| Resource | ZFIN |

**Limitation — and it is the defining one.** The model's tumours *"were composed of differentiated, mature ganglion cells with **poor Schwannian stroma**."* Human ganglioneuroma is, by its INPC definition, **Schwannian stroma-dominant**. So the model reproduces the neuronal half of the disease and not the half the disease is named for — and therefore cannot address the Schwann-cell crosstalk mechanism (§6.1) at all. This is a textbook `HUMAN_MODEL_MISMATCH`, not a generic knowledge gap: the evidence exists in the model, and its translational validity to the defining human feature is the open question. Recommended curation: `kind: HUMAN_MODEL_MISMATCH` with a `prompt` asking whether AKT-driven ganglion-cell expansion without Schwannian stroma is the same disease as human Schwannian stroma-dominant ganglioneuroma, and `modeled_mechanisms` links carrying `relationship: PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`, a `BOUNDARY_OMISSION` divergence (Schwannian stroma absent from the model) and a `SPECIES_MISMATCH` divergence (murine Akt2 in a teleost interrenal gland).

Second limitation: the construct enforces constitutive membrane-targeted AKT, which is **not** the human lesion — no somatic `AKT` or `PTEN` mutation was found in the human cohort. The model demonstrates sufficiency of the pathway state; it does not model the human initiating event.

### 15.2 Mouse — enteric ganglioneuromatosis

**Puig I, Champeval D, De Santa Barbara P, Jaubert F, Lyonnet S, Larue L. *J Clin Invest* 2009;119(12):3586–96. PMID:19884655, doi:10.1172/JCI39929.**

| Attribute | Detail |
|---|---|
| Species | *Mus musculus*, **NCBITaxon:10090** |
| Model type | Conditional knockout: `Tyr:Cre/°; PTEN^F/F` (exon 5 floxed), homozygous = "HM" |
| Target lineage | Tyrosinase-expressing cells, which include **enteric nervous system cells** (plus melanoblasts and a subset of smooth-muscle precursors) |
| Phenotype | Enteric neuronal **hyperplasia** (3× cell count) and **hypertrophy** (2× cell size) = ganglioneuromatosis; chronic intestinal pseudo-obstruction with cecal dilation and empty colon; **death P13–P20 with 100% penetrance** |
| Pathway | *"S6 and AKT phosphorylation levels were clearly higher in HM than in WT samples, this effect being particularly marked for AKT."* |
| Rescue | AKT inhibitor **API2** prevented the hyperplasia: TUJ1+ cell counts in treated HM embryos did not differ from WT, versus double WT in untreated HM |
| Human validation | PTEN expression significantly lower in **2/7** CIPO patients, with increased S6 phosphorylation |
| Resource | MGI, IMSR |

**Limitations:** (i) the compartment is the **enteric** nervous system, so this is a model of intestinal ganglioneuromatosis, not of sympathetic-chain ganglioneuroma; (ii) the Cre driver is not ENS-specific (tyrosinase is also active in melanoblasts and cardiac/ductus smooth-muscle precursors), so the phenotype is not cell-autonomously attributed with certainty; (iii) perinatal lethality precludes any study of tumour natural history, growth rate, or ageing; (iv) human Cowden-syndrome tissue was not obtainable — *"we were unable to obtain appropriate material for immunohistochemical analyses."*

**Why it still matters:** it is the only **rescue** experiment in this entire disease. The API2 result establishes direction of causation from AKT activity to ganglion-cell expansion, which no human or zebrafish observation does.

### 15.3 Genetic model types available

| Type | Available for GN? |
|---|---|
| Transgenic (overexpression) | Yes — zebrafish `dβh:myr-Akt2` |
| Conditional knockout | Yes — mouse `Tyr:Cre; Pten^F/F` |
| Knockout (constitutive) | Not for GN |
| Knock-in | Not for GN. `RET` M918T knock-in mice exist for MEN2B; `[their enteric ganglioneuromatosis phenotype was not characterised in this session — UNVERIFIED and a good follow-up]` |
| Humanised | None |
| Induced (drug/surgical/environmental) | None |
| Adjacent NF1/PTEN Schwann-cell models | `Dhh-Cre; Nf1^fl; Pten^fl` and `Pten`/EGFR Schwann-cell models produce **neurofibroma and MPNST**, not ganglioneuroma ([PMID:22700876](https://pubmed.ncbi.nlm.nih.gov/22700876/?dopt=Abstract); [PMC3539440](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3539440/)) — informative for the transformation branch, not for GN itself |

### 15.4 In vitro and cellular systems

- **There is no ganglioneuroma cell line.** No ATCC/Cellosaurus entry, no DepMap model. GN is post-mitotic, which makes a line essentially impossible — a hard structural limit, and the reason all functional work uses neuroblastoma lines as surrogates.
- **Neuroblastoma + Schwann cell co-culture** is the working in vitro model of the maturation mechanism: NTRK1-expressing NB cells, primary human repair Schwann cells, conditioned media, and recombinant EGFL8, with neurite outgrowth and proliferation as readouts (**PMID:33712610**; [PMC4294349](https://pmc.ncbi.nlm.nih.gov/articles/PMC4294349/)). Lines used across this literature include SH-SY5Y and SK-N-SH.
- **Retinoic-acid differentiation** (`CHEBI:15367` all-trans-retinoic acid; `CHEBI:26536` retinoic acid) is the pharmacological proxy for maturation — ATRA causes a ~3-fold increase in TrkA expression and raises `NTRK1`/`RET` mRNA in NB lines ([systematic ATRA analysis, PMC7053487](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7053487/)). **Important caveat for curation:** ATRA-driven differentiation of a neuroblastoma line is *not* a model of ganglioneuroma — it is a model of neuroblastoma differentiation, which is only the same thing if Model A (§6.1) is correct. Grade any such evidence `IN_VITRO` with `directness: INDIRECT`.
- **Human nerve-injury tissue** served as the repair-Schwann-cell comparator in Weiss 2021, which is an unusual and well-chosen control: it tests whether GN stroma resembles a physiological repair state rather than a neoplastic one. It does.

### 15.5 What the models collectively cannot do

Worth recording explicitly, because it defines the research frontier:

1. **No model reproduces Schwannian stroma dominance** — the disease's defining feature.
2. **No model has the human initiating lesion**, because that lesion is unknown.
3. **No model of the sporadic human sympathetic-chain tumour** exists in a mammal.
4. **No model of malignant transformation** (GN → MPNST).
5. **No model permits long-term natural-history study** — the mouse dies at P20 and the zebrafish is not followed beyond 29 wpf.

### 15.6 Resources

ZFIN (zebrafish), MGI / IMPC / KOMP / IMSR / EMMA / MMRRC (mouse), Alliance of Genome Resources, Cellosaurus and DepMap (both empty for GN).

---

## Appendix A — Verified ontology term suggestions

Every CURIE below was resolved this session in `cache/<prefix>/terms.csv`, the EBI OLS4 API, or `rest.genenames.org`. **Nothing here was written from memory.** Items marked `[UNVERIFIED]` in the body are deliberately excluded from this table.

**Disease:** MONDO:0005033 ganglioneuroma · MONDO:0003326 intermixed schwannian stroma-rich ganglioneuroblastoma · MONDO:0003325 nodular ganglioneuroblastoma · MONDO:0005035 ganglioneuroblastoma · MONDO:0005072 neuroblastoma · MONDO:0006076 adrenal gland neuroblastoma

**Phenotype (HP):** HP:0003005 Ganglioneuroma · HP:0006747 Ganglioneuroblastoma · HP:0003006 Neuroblastoma · HP:0002666 Pheochromocytoma · HP:0002027 Abdominal pain · HP:0003418 Back pain · HP:0031500 Abdominal mass · HP:0003270 Abdominal distention · HP:0002013 Vomiting · HP:0002019 Constipation · HP:0002014 Diarrhea · HP:0002900 Hypokalemia · HP:0001508 Failure to thrive · HP:0000822 Hypertension · HP:0031284 Flushing · HP:0000975 Hyperhidrosis · HP:0001962 Palpitations · HP:0001337 Tremor · HP:0000739 Anxiety · HP:0002315 Headache · HP:0002277 Horner syndrome · HP:0002176 Spinal cord compression · HP:0002385 Paraparesis · HP:0010550 Paraplegia · HP:0002650 Scoliosis · HP:0002094 Dyspnea · HP:0012735 Cough · HP:0100749 Chest pain · HP:0000126 Hydronephrosis · HP:0000020 Urinary incontinence

**Cell type (CL):** CL:0011103 sympathetic neuron · CL:0008025 noradrenergic neuron · CL:0000107 autonomic neuron · CL:0002573 Schwann cell · CL:0000218 myelinating Schwann cell · CL:0002375 Schwann cell precursor · CL:0011012 neural crest cell · CL:0000333 migratory neural crest cell · CL:0002676 neural crest derived neuroblast · CL:0000166 chromaffin cell · CL:0000336 adrenal medulla chromaffin cell · CL:0007011 enteric neuron · CL:0002607 migratory enteric neural crest cell

**Anatomy (UBERON):** UBERON:0003693 retroperitoneal space · UBERON:0008822 posterior mediastinum · UBERON:0003728 mediastinum · UBERON:0002369 adrenal gland · UBERON:0001236 adrenal medulla · UBERON:0001806 sympathetic ganglion · UBERON:0001807 paravertebral ganglion · UBERON:0001805 autonomic ganglion · UBERON:0000974 neck · UBERON:0002240 spinal cord

**Biological process (GO):** GO:0048485 sympathetic nervous system development · GO:0007422 peripheral nervous system development · GO:0001755 neural crest cell migration · GO:0030182 neuron differentiation · GO:0045664 regulation of neuron differentiation · GO:0048667 cell morphogenesis involved in neuron differentiation · GO:0048663 neuron fate commitment · GO:0031175 neuron projection development · GO:0010975 regulation of neuron projection development · GO:0048011 neurotrophin TRK receptor signaling pathway · GO:0014037 Schwann cell differentiation · GO:0022011 myelination in peripheral nervous system · GO:0042552 myelination · GO:0043491 phosphatidylinositol 3-kinase/protein kinase B signal transduction · GO:0031929 TOR signaling · GO:0032008 positive regulation of TOR signaling · GO:0035860 glial cell-derived neurotrophic factor receptor signaling pathway · GO:0048384 retinoic acid receptor signaling pathway · GO:0042423 catecholamine biosynthetic process

**Gene (HGNC, lowercase per repo convention):** hgnc:391 AKT1 · hgnc:392 AKT2 · hgnc:393 AKT3 · hgnc:3942 MTOR · hgnc:9588 PTEN · hgnc:9967 RET · hgnc:7765 NF1 · hgnc:9143 PHOX2B · hgnc:427 ALK · hgnc:8031 NTRK1 · hgnc:7997 NRG1 · hgnc:7808 NGF · hgnc:11190 SOX10 · hgnc:4232 GDNF · hgnc:7559 MYCN · hgnc:11782 TH · hgnc:2689 DBH · hgnc:11730 TERT · hgnc:886 ATRX · hgnc:1076 BMPR1A · hgnc:12693 VIP (resolved at rest.genenames.org)

**Chemical (CHEBI):** CHEBI:33569 noradrenaline · CHEBI:33568 adrenaline · CHEBI:18243 dopamine · CHEBI:545959 homovanillic acid · CHEBI:20106 vanillylmandelic acid · CHEBI:9168 sirolimus · CHEBI:68478 everolimus · CHEBI:15367 all-trans-retinoic acid · CHEBI:26536 retinoic acid

**Treatment (NCIT):** NCIT:C15329 Surgical Procedure · NCIT:C154430 Definitive Surgical Resection · NCIT:C164212 Tumor Resection · NCIT:C131672 Gross Total Resection · NCIT:C175027 Complete Resection · NCIT:C15177 Adrenalectomy · NCIT:C15722 Patient Observation · NCIT:C15986 Pharmacotherapy · NCIT:C2201 mTOR Inhibitor · NCIT:C1212 Sirolimus · NCIT:C48387 Everolimus · NCIT:C15747 Supportive Care · NCIT:C15315 Rehabilitation · NCIT:C15240 Genetic Counseling · NCIT:C15313 Radiation Therapy · NCIT:C17204 Computed Tomography · NCIT:C16809 Magnetic Resonance Imaging

**Taxon (NCBITaxon):** NCBITaxon:9606 Homo sapiens · NCBITaxon:7955 Danio rerio · NCBITaxon:10090 Mus musculus · NCBITaxon:9615 Canis lupus familiaris · NCBITaxon:9913 Bos taurus · NCBITaxon:9925 Capra hircus · NCBITaxon:9823 Sus scrofa · NCBITaxon:9796 Equus caballus

---

## Appendix B — Primary citations, with PMIDs and quotable abstract sentences

Each snippet below was read from the PubMed record or publisher page in this session and is an exact substring of that abstract. They are offered as candidate `snippet:` values; each still needs `just fetch-reference PMID:<id>` and `just count-verified-snippets` before commit.

| PMID | Citation | Candidate exact quote |
|---|---|---|
| **32728700** | Tao T, et al. *J Exp Med* 2020;217(10):e20191871 | "Zebrafish transgenic for constitutively activated myr-Akt2 in the sympathetic nervous system were found to develop ganglioneuroma without progression to neuroblastoma." · "Here, we found that an AKT-mTOR-S6 pathway was active in human ganglioneuroma but not neuroblastoma samples." · "Surgery is the only effective therapy for ganglioneuroma, which may be challenging due to the location of the tumor and involvement of surrounding structures." |
| **33712610** | Weiss T, Taschner-Mandl S, et al. *Nat Commun* 2021;12:1624 | "Indeed, stromal SCs in ganglioneuromas and repair SCs share the expression of nerve repair-associated genes." · "Neuroblastoma cells, derived from aggressive tumors, respond to primary repair-related SCs and their secretome with increased neuronal differentiation and reduced proliferation." |
| **19884655** | Puig I, et al. *J Clin Invest* 2009;119:3586–96 | "Intestinal ganglioneuromatosis is a benign proliferation of nerve ganglion cells, nerve fibers, and supporting cells of the enteric nervous system (ENS)..." · "S6 and AKT phosphorylation levels were clearly higher in HM than in WT samples, this effect being particularly marked for AKT." |
| **39582110** | Burnand KM, et al. *Pediatr Blood Cancer* 2025;72(2):e31445 | "A total of 259 patients were identified (163 GN, 93 GNBi, median age 62 months)." · "In 45 cases (39%), surgical pathology was different from pathology at biopsy, and in 14 (12%) the pathology changed from GN/GNBi to neuroblastoma/GNB nodular." · "Watchful active observation can be a safe approach, with surgical resection reserved for symptomatic patients." |
| **42537227** | Texakalidis P, Gogoi R, Spinner RJ. *J Neurosurg* 2026;145(4):1223–9 | "Most lesions (72%) were incidental findings." · "Short-term postoperative complications occurred in 43.1% of cases, most commonly neurological deficits (22.2%)." · "GNs demonstrate indolent behavior, low recurrence rates, and no observed malignant transformation in this large cohort." · "No patient in the observation group developed new symptoms, and 2 tumors exhibited minimal interval growth (0.08-0.17 cm/year)." |
| **41306794** | Li W, Xiao M, Miao C, et al. *Front Surg* 2025;12:1701114 | "no recurrences, metastases, or disease-specific deaths occurred" · "While surgical resection remains the cornerstone of management, it is best undertaken at specialized, high-volume sarcoma centers to mitigate operative risks." |
| **41858373** | Sugawara M, Haruta M, Ohira M, et al. *Oncol Lett* 2026;31(5):156 | "ALT was identified in 38 NB cases (38/255, 15%) and 6 GNB cases (6/48, 12.5%), but not in GN." · "High TERT expression was observed in 38% (64/169), 23% (7/31) and 14% (1/7) of NB, GNB and GN cases, respectively." |
| **41561749** | Ozcelik EE, et al. *Front Oncol* 2026;15:1632294 | "no distant metastases or recurrences were observed during follow-up" |
| **29369484** | Alexander N, Sullivan K, Shaikh F, Irwin MS. *Pediatr Blood Cancer* 2018;65(5):e26964 | "GN and GNB-I have a slow growth rate and resection can be associated with significant morbidity." · "Watch and wait approaches should be considered for some GN and GNB-I." · "There were post-operative complications in 15 of the 50 (30%) surgical patients." |
| **10421272** | Shimada H, et al. *Cancer* 1999;86:349–63 — "Terminology and morphologic criteria of neuroblastic tumors" | The four-category INPC definition (quote to be lifted from the fetched record) |
| **10421273** | Shimada H, et al. *Cancer* 1999;86:364–72 — "The International Neuroblastoma Pathology Classification (the Shimada system)" | 3-year EFS 85% favourable vs 41% unfavourable histology |
| **14601099** | Peuchmaur M, et al. *Cancer* 2003;98:2274–81 | "8-year event free survival rate: 86.1% vs. 32.2%; P = 0.0003; overall survival rate: 90.5% vs. 33.2%" |
| **37746449** | *Cureus* 2023;15:e43914 | "Ganglioneuroma is a rare neurogenic tumor with a prevalence of one per million population" · "Ganglioneuromas constitute only 0.72%-1.6% of all primary retroperitoneal tumors" |
| **40799243** | *Front Oncol* 2025;15:1619030 — adrenal GN review | "AGN is rare in children under 10 years of age, with a higher incidence in adults than in children, and its incidence increases with age." · "Laparoscopic resection is the primary treatment for AGN." |
| **33553609** | *Mol Cell Oncol* 2020 — "Targeting ganglioneuromas with mTOR inhibitors" | Commentary on PMID:32728700 |
| **28640941** | "PHOX2B reliably distinguishes neuroblastoma among small round blue cell tumours" | PHOX2B sensitivity/specificity in pNTs |
| — | Shimada H, Sano H, Hazard FK. *Clin Pediatr Hematol Oncol* 2020;27:73–86, doi:10.15264/cpho.2020.27.2.73 | "composed only of completely mature ganglion cells covered with satellite cells" · "all neuritic processes produced by ganglion cells are immediately incorporated in the cytoplasm of Schwann cells, so that no naked neuritic processes are detected" · "all Ganglioneuromas were once Neuroblastomas in their early stage of tumor development" |
| — | Conces MR, Shibui Y, Shimada H. *Diagnostic Pathology* 2026;21:22, doi:10.1186/s13000-026-01758-y | Current INPC review; full text paywall-redirected in this session, **fetch before curating from it** |

---

## Appendix C — Explicit gaps and unverified items

Carried forward so nothing here is mistaken for an established fact.

1. **ICD-11 code.** Orphanet records 2A00.21; this was not verified against the WHO ICD-11 browser, and the morphology stem XH03L9 comes only from third-party aggregators.
2. **MeSH D005729** taken from an aggregator listing, not NLM directly.
3. **LOINC codes** for VMA, HVA, metanephrines and VIP — none looked up. Do not type a LOINC label; use `just loinc-seed-cache`.
4. **"~30% of adrenal GN have elevated catecholamines"** — widely repeated secondary claim, primary source not traced.
5. **"1 per million" prevalence** and **"60% under age 20"** — both secondary/tertiary claims.
6. **MYCN gain in GN** — the one quantitative figure encountered (1.8%) has ambiguous attribution in the available abstract.
7. **Turner syndrome association** — Orphanet-level only, no primary citation located.
8. **HPO term for virilization**, **UBERON term for presacral space**, **CL term for satellite cell**, and **GO cellular-component terms for Nissl substance/rough ER** — all unresolved.
9. **GEO accessions** (GSE192906, GSE90711, GSE94035, GSE147635, GSE45547, GSE85047) — the GN-sample composition of each was **not** confirmed. Relevance triage is mandatory before curating any as a `datasets:` record.
10. **PRIDE accession** for the Weiss 2021 secretome proteomics — not resolved.
11. **RET M918T knock-in mouse enteric phenotype** — not characterised in this session; a likely fourth model organism.
12. **Perioperative alpha-blockade protocol** for secretory GN — not sourced.
13. **Non-human orthologue NCBI Gene IDs** — not resolved.
14. **No GN-specific epigenomic, proteomic, metabolomic or lipidomic study exists.** Searched; genuinely absent.
15. **No GN-specific QoL instrument data exist.** Searched; genuinely absent.
16. **No clinical trial, past or present, in ganglioneuroma.** Searched ClinicalTrials.gov; genuinely absent.

---

## Sources

- [Orphanet: Ganglioneuroma (ORPHA:251992)](https://www.orpha.net/en/disease/detail/251992) · [Orphanet mirror with codes](https://chorobyrzadkie.gov.pl/en/disease_card/251992)
- [Tao et al., Ganglioneuromas are driven by activated AKT and can be therapeutically targeted with mTOR inhibitors (J Exp Med 2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7537400/) · [publisher page](https://rupress.org/jem/article/217/10/e20191871/151986/Ganglioneuromas-are-driven-by-activated-AKT-and) · [commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC7849689)
- [Weiss et al., Schwann cell plasticity regulates neuroblastic tumor cell differentiation via EGFL8 (Nat Commun 2021)](https://www.nature.com/articles/s41467-021-21859-0) · [NTRK1–Schwann cell crosstalk](https://pmc.ncbi.nlm.nih.gov/articles/PMC4294349/)
- [Puig et al., Deletion of Pten in the mouse enteric nervous system induces ganglioneuromatosis (JCI 2009)](https://www.jci.org/articles/view/39929)
- [Burnand et al., UK CCLG nationwide study (Pediatr Blood Cancer 2025)](https://onlinelibrary.wiley.com/doi/full/10.1002/pbc.31445) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/39582110/?dopt=Abstract) · [open-access PDF](https://pure-oai.bham.ac.uk/ws/files/250952117/Pediatric_Blood_Cancer_-_2024_-_Burnand_-_Management_of_Ganglioneuroma_and_Ganglioneuroblastoma_Intermixed_A_United.pdf)
- [Texakalidis et al., 30-year experience of 101 patients (J Neurosurg 2026)](https://doi.org/10.3171/2026.2.jns252992) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42537227/)
- [Li et al., primary retroperitoneal ganglioneuroma, 51 patients (Front Surg 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12644016/)
- [Sugawara et al., Telomere maintenance mechanisms in ganglioneuroblastoma and ganglioneuroma (Oncol Lett 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12997032/)
- [Ozcelik et al., Ganglioneuroma has a potential for lymph node metastasis (Front Oncol 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12812659/)
- [Alexander et al., Characteristics and management of GN and GNB-I (Pediatr Blood Cancer 2018)](https://pubmed.ncbi.nlm.nih.gov/29369484/)
- [Shimada et al., The International Neuroblastoma Pathology Classification (Cancer 1999)](https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0142(19990715)86:2%3C364::AID-CNCR21%3E3.0.CO%3B2-7) · [Terminology and morphologic criteria (Cancer 1999)](https://acsjournals.onlinelibrary.wiley.com/doi/full/10.1002/(SICI)1097-0142(19990715)86:2%3C349::AID-CNCR20%3E3.0.CO;2-Y) · [Peuchmaur et al., INPC revision (Cancer 2003)](https://acsjournals.onlinelibrary.wiley.com/doi/full/10.1002/cncr.11773)
- [Shimada, Sano, Hazard, Pathology of Peripheral Neuroblastic Tumors (Clin Pediatr Hematol Oncol 2020)](https://www.cpho.or.kr/journal/view.html?doi=10.15264%2Fcpho.2020.27.2.73) · [Conces, Shibui, Shimada, Pathology of peripheral neuroblastic tumors (Diagnostic Pathology 2026)](https://link.springer.com/article/10.1186/s13000-026-01758-y) · [CAP neuroblastoma protocol](https://documents.cap.org/protocols/Neuroblastoma_5.0.0.0.REL_CAPCP.pdf) · [ICCR neuroblastoma reporting guide](https://www.iccr-cancer.org/wp-content/uploads/2023/11/ICCR-Neuroblastoma-1st-ed-v1.0-bookmark.pdf)
- [Imaging of Ganglioneuroma: a literature review (Diagnostics 2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10341194/) · [Imaging analysis and quantitative analysis of paraspinal ganglioneuroma](https://pmc.ncbi.nlm.nih.gov/articles/PMC6647925/) · [CT and MRI findings of thoracic ganglioneuroma](https://pubmed.ncbi.nlm.nih.gov/22573298/) · [Imaging of thoracic neurogenic tumors (AJR)](https://ajronline.org/doi/10.2214/AJR.16.16018) · [Adrenal GN with nodal metastases on MIBG/FDG](https://www.sciencedirect.com/science/article/pii/S1930043324007155)
- [Adrenal ganglioneuroma: two case reports and literature review (Front Oncol 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339323/) · [Overreliance on radiological findings (Cureus 2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10512760/)
- [Intestinal ganglioneuromatosis as an early extra-endocrine manifestation of MEN2B](https://pmc.ncbi.nlm.nih.gov/articles/PMC10848182) · [Germline RET codon 918 mutation in apparently isolated intestinal ganglioneuromatosis (JCEM 1998)](https://academic.oup.com/jcem/article/83/12/4191/2865226) · [Comprehensive review on MEN2B](https://erc.bioscientifica.com/view/journals/erc/25/2/ERC-17-0209.xml) · [Rectal biopsy for early MEN2B diagnosis](https://pubmed.ncbi.nlm.nih.gov/27899172/) · [Timely diagnosis of MEN2B](https://link.springer.com/article/10.1007/s12020-021-02607-2) · [Clues for early diagnosis of MEN2B before MTC (Pediatrics 2024)](https://publications.aap.org/pediatrics/article/154/3/e2022059517/198957/Clues-for-Early-Diagnosis-of-MEN2B-Syndrome-Before) · [Intestinal ganglioneuromatosis: overproduction of NGF? (NEJM 1983)](https://www.nejm.org/doi/abs/10.1056/NEJM198303173081106) · [GDNF/neurturin in diffuse ganglioneuromatosis](https://pubmed.ncbi.nlm.nih.gov/19353842/)
- [Uveal ganglioneuroma due to germline PTEN mutation](https://pmc.ncbi.nlm.nih.gov/articles/PMC5566766/) · [Diffuse gastric ganglioneuromatosis in PTEN hamartoma syndrome](https://pmc.ncbi.nlm.nih.gov/articles/PMC5889855/) · [Cowden syndrome with ganglioneuromatous polyposis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4862217/) · [Intestinal ganglioneuromatosis as unusual presentation of Cowden syndrome](https://pubmed.ncbi.nlm.nih.gov/23512313/) · [Colonic ganglioneuroma: 43 patients (Diseases 2023)](https://www.mdpi.com/2079-9721/11/2/69)
- [Neuroblastic tumors and NF1: Italian multicenter study and systematic review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9673013/) · [Ganglioneuroma of the bladder in NF1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9776796/) · [Cervical ganglioneuroma in NF1 with postoperative Horner syndrome](https://pmc.ncbi.nlm.nih.gov/articles/PMC13492013/) · [Pheochromocytoma and ganglioneuroma in NF1](https://pubmed.ncbi.nlm.nih.gov/17954422/)
- [MPNST arising in previously irradiated neuroblastoma](https://pubmed.ncbi.nlm.nih.gov/10755757/) · [MPNST arising in a "de novo" ganglioneuroma (Drago 1997)](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1096-911X(199703)28:3%3C216::AID-MPO13%3E3.0.CO;2-C) · [Malignant transformation of rectovaginal ganglioneuroma to MPNST in NF1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12221925) · [Mandibular MPNST after radiotherapy for CPA ganglioneuroma](https://pubmed.ncbi.nlm.nih.gov/42120254/)
- [Composite pheochromocytoma-ganglioneuroma: immunohistochemical study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3685741/) · [Composite pheo-GN with MEN2A (Am J Surg Pathol 1997)](https://www.ovid.com/jnls/ajsp/abstract/00000478-199701000-00011~composite-pheochromocytomaganglioneuroma-of-the-adrenal?redirectionsource=fulltextview) · [Composite pheo-GN with two distinct radiographic components](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9518729/) · [Adrenal schwannoma associated with ganglioneuroma](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11446904/)
- [Watery diarrhoea and ganglioneuroma with VIP secretion](https://pubmed.ncbi.nlm.nih.gov/1211964/) · [VIP-producing ganglioneuroma in a child with chronic diarrhea](https://pubmed.ncbi.nlm.nih.gov/7376870) · [VIP-secreting tumours in children](https://pubmed.ncbi.nlm.nih.gov/2833214/) · [Hormone-secreting large adrenal ganglioneuroma (Blood Press 2013)](https://www.tandfonline.com/doi/full/10.3109/08037051.2013.796103) · [Catecholamines in urine and tumour tissue in phaeochromocytoma, ganglioneuroma and neuroblastoma](https://www.sciencedirect.com/science/article/abs/pii/S0031302516393552) · [Large catecholamine-secreting ganglioneuroma](https://pmc.ncbi.nlm.nih.gov/articles/PMC9242669/)
- [PHOX2B reliably distinguishes neuroblastoma among small round blue cell tumours](https://pubmed.ncbi.nlm.nih.gov/28640941/) · [PHOX2B immunolabeling](https://www.researchgate.net/publication/229081877_PHOX2B_Immunolabeling_A_Novel_Tool_for_the_Diagnosis_of_Undifferentiated_Neuroblastomas_Among_Childhood_Small_Round_Blue-cell_Tumors)
- [Identifying a novel PHOX2B gene variant in a neuroblastoma family](https://www.sciencedirect.com/science/article/pii/S2405844024026124) · [Analysis of sporadic neuroblastic tumors reveals a novel PHOX2B mutation](https://www.sciencedirect.com/science/article/abs/pii/S2452014418300396) · [ALK germline mutations in neuroblastoma](https://www.nature.com/articles/ejhg2011195) · [ALK-F1174L impairs differentiation of neural crest progenitors in sympathetic ganglia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6477091/)
- [ATRA-triggered neuroblastoma differentiation and NTRK2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7053487/) · [Neuroblastoma pathogenesis: deregulation of embryonic neural crest development](https://pmc.ncbi.nlm.nih.gov/articles/PMC5918240/) · [Single-cell atlas of developing murine adrenal gland and Schwann cell precursor signature (PNAS)](https://www.pnas.org/doi/10.1073/pnas.2022350118) · [GSE192906 (pNT scRNA-seq)](https://www.omicsdi.org/dataset/geo/GSE192906)
- [Unusual spontaneous regression from neuroblastoma to ganglioneuroma](https://pubmed.ncbi.nlm.nih.gov/34054050/) · [Complete maturation of neuroblastoma with bone metastases](https://www.sciencedirect.com/science/article/abs/pii/0022346875901992) · [Maturation of mass-screened localized adrenal neuroblastoma](https://www.sciencedirect.com/science/article/abs/pii/S0022346801387067) · [Nodular GNB neuroblastoma and ganglion components are genetically similar (Mod Pathol)](https://www.nature.com/articles/modpathol201490) · [Evidence for molecular heterogeneity in human ganglioneuroblastoma](https://pubmed.ncbi.nlm.nih.gov/8108298/) · [CGH in ganglioneuroblastomas](https://pubmed.ncbi.nlm.nih.gov/11801306/)
- [Clinical outcomes following resection of paraspinal ganglioneuromas (J Neurosurg Spine 2022)](https://thejns.org/spine/view/journals/j-neurosurg-spine/37/1/article-p130.xml) · [Neurological outcomes after nerve root sacrifice in dumbbell tumors (Eur Spine J)](https://link.springer.com/article/10.1007/s00586-026-09903-3) · [Presacral ganglioneuroma, 6-year follow-up without surgery](https://www.sciencedirect.com/science/article/pii/S193004332030282X) · [Dumbbell ganglioneuroma of the lumbar spine](https://pmc.ncbi.nlm.nih.gov/articles/PMC12665655/)
- [Cutaneous ganglioneuroma in cattle](https://www.researchgate.net/publication/226171812_Cutaneous_ganglioneuroma_in_a_cattle_case_report) · [Adrenal neuroblastoma in a young dog (Front Vet Sci 2019)](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00161/pdf)
- [PTEN and NF1 inactivation in Schwann cells promotes nerve sheath tumors](https://pubmed.ncbi.nlm.nih.gov/22700876/?dopt=Abstract) · [Conditional Pten inactivation with EGFR overexpression models sporadic MPNST](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3539440/)
- [SARC031 selumetinib + sirolimus (NCT03433183)](https://clinicaltrials.gov/study/NCT03433183) · [Sirolimus in NF1 plexiform neurofibromas (NCT00634270)](https://clinicaltrials.gov/study/NCT00634270)
- [SEER-based prognostic nomogram for ganglioneuroblastoma](https://pmc.ncbi.nlm.nih.gov/articles/PMC11107237/)
- Identifier resolution: [EBI OLS4 API](https://www.ebi.ac.uk/ols4) · [HGNC REST](https://rest.genenames.org) · [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) · local `cache/*/terms.csv` in this checkout

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 82 |
| Resolved | 82 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 82 |
| On topic | 29 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 117 |
| Resolved | 116 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005033` (5 mentions) - the report calls it "if available"; MONDO calls it **ganglioneuroma**
- `MONDO:0003325` (4 mentions) - the report calls it "composite", "Ganglioneuroblastoma, nodular — **composite", "ganglioneuroblastoma, nodular"; MONDO calls it **nodular ganglioneuroblastoma**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0003326` (4 mentions) - the report calls it "Schwannian stroma-rich", "Ganglioneuroblastoma, intermixed — **Schwannian stroma-rich", "ganglioneuroblastoma, intermixed"; MONDO calls it **intermixed schwannian stroma-rich ganglioneuroblastoma**
- `CHEBI:9168` (2 mentions) - the report calls it "Sirolimus (rapamycin)"; CHEBI calls it **sirolimus**, and lists "sirolimusum" among its other names
- `NCBITaxon:9913` (2 mentions) - the report calls it "Cattle"; NCBITaxon calls it **Bos taurus**, and lists "domestic cattle" among its other names
- `NCBITaxon:9925` (2 mentions) - the report calls it "Goat (Boer)"; NCBITaxon calls it **Capra hircus**, and lists "goat" among its other names
- `NCBITaxon:9823` (2 mentions) - the report calls it "Pig (piglet)"; NCBITaxon calls it **Sus scrofa**, and lists "pig" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0003326` - called "Schwannian stroma-rich", "Ganglioneuroblastoma, intermixed — **Schwannian stroma-rich", "ganglioneuroblastoma, intermixed"
- `MONDO:0003325` - called "composite", "Ganglioneuroblastoma, nodular — **composite", "ganglioneuroblastoma, nodular"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
