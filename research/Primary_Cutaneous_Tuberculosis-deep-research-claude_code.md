---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T22:37:16.103216'
end_time: '2026-11-25T22:39:16.768705'
duration_seconds: 120.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Primary Cutaneous Tuberculosis
  mondo_id: MONDO:0957464
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 9
  num_turns: 11
  total_cost_usd: 0.6329655999999999
  session_id: 9e37f319-b40f-4394-9813-17db6a64ea17
  stop_reason: end_turn
  tool_calls: 10
  retrieval_calls: 10
  assistant_text_blocks: 1
  unsuccessful_reason: the model marked the report incomplete; its reason is on the
    line that begins 'Incomplete report:'
answer_status: unsuccessful
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Cutaneous Tuberculosis
- **MONDO ID:** MONDO:0957464 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Primary Cutaneous Tuberculosis** covering all of the
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

> **Warning:** claude_code reported that it could not answer this question. What follows is its response, not a finished report.

**Incomplete report:** The searches retrieved only a limited set of reviews and case reports, and several knowledge-base fields have no retrievable data, so those fields are left as gaps or marked not applicable rather than filled from memory.

# Primary Cutaneous Tuberculosis (Primary Inoculation Tuberculosis / Tuberculous Chancre): Research Report

**How I read the request:** "Primary cutaneous tuberculosis" is taken here to mean **primary inoculation tuberculosis**, also called the **tuberculous chancre**. This is the exogenous form of cutaneous TB that arises when *Mycobacterium tuberculosis* is inoculated directly into the skin of a person who has never been infected or sensitized to TB (Frankel et al., PMID 20725570, https://pmc.ncbi.nlm.nih.gov/articles/PMC2923933; Santos et al., PMID 24770496).

**Causal gene:** none. The template lists no causal gene, and that is correct. This is an infectious disease caused by *M. tuberculosis*, or less often *M. bovis* or BCG. It is not a Mendelian disorder.

**MONDO ID:** I could not confirm MONDO:0957464 in this session. It is used as supplied.

---

## 1. Disease Information

**Overview.** Cutaneous TB (CTB) is uncommon. It makes up about 1–2% of extrapulmonary TB (An Bras Dermatol 2022, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9073256/), or about 1–1.5% in another review (Pathogens 2023;12(7):920, https://mdpi.com/2076-0817/12/7/920). CTB is grouped by how the bacteria reach the skin:
- **Exogenous:** tuberculous chancre and tuberculosis verrucosa cutis.
- **Endogenous:** spread from an adjacent focus or by autoinoculation (for example, scrofuloderma and orificial TB), or spread through the blood (StatPearls, NBK482220, https://ncbi.nlm.nih.gov/books/NBK482220).

The primary inoculation lesion is described as "equivalent to the primary pulmonary complex" (Haddad et al., PMID 35853774). That means a skin chancre together with swollen regional lymph nodes.

**Identifiers**

| System | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0957464 (as supplied; not checked) | — |
| ICD-10 | A18.4, Tuberculosis of skin and subcutaneous tissue | https://gesund.bund.de/en/icd-code-suche/a18-4 |
| ICD-11 | 1B12.8, Cutaneous tuberculosis. The WHO crosswalk calls it equivalent to A18.4, and its synonym list includes "tuberculous chancre" and "primary inoculation tuberculosis". This came from aggregator sites; check it in the WHO browser. | https://findacode.com/icd-11/code-625292625.html |
| MeSH | D014382, Tuberculosis, Cutaneous | https://meshb.nlm.nih.gov/record/ui?ui=D014382 |
| OMIM / Orphanet | None found | — |

**Synonyms:** primary inoculation tuberculosis; tuberculous chancre; primary tuberculous complex of the skin. "Prosector's wart" is a historical term for occupational inoculation TB in people who prepared dissections (https://en.wikipedia.org/wiki/Primary_inoculation_tuberculosis). Strictly, it refers to the verrucous form, so treat it as a related term, not an exact synonym.

**Evidence source:** The literature is aggregated from case reports and small series. No registry or EHR cohorts were found.

## 2. Etiology

**Cause.** The cause is infection with *M. tuberculosis* (NCBITaxon:1773) entering through broken skin. *M. bovis* and BCG are less common causes (StatPearls NBK482220).

**Routes of entry.** Reported routes include "traumatic injuries or surgical procedures performed with unsterilized materials and even after tattoos or body piercing" (Khadka et al., PMID 30111996). Case reports describe:
- Needlestick injuries in health-care workers. One example is a medical intern injured during a lumbar puncture on a patient with HIV (Clin Case Rep 2015;3(1):39–42).
- A 25-year-old health-care professional whose diagnosis was confirmed by BACTEC culture (https://katalog.lib.cas.cz/KNAV/EdsRecord/cmedm,16334632).
- A surgeon injured during thoracentesis. That report's literature search found "19 cases of inoculation TB secondary to sharp injury in HCWs including the present case" (Saudi J Med Med Sci 2015, https://doaj.org/article/b893819535d24abaadfb83812fe4387b).
- A papular eruption on a tattoo (Wong, Tay, Sim, Australas J Dermatol 2005). Only the citation was retrieved.

**Risk factors**
- **No prior TB sensitization.** This is the defining host condition: the person must be tuberculin-naïve (PMID 20725570).
- **Childhood.** Children are often affected. Common lesion sites are the knees, ankles, buttocks and hands (https://en.wikipedia.org/wiki/Primary_inoculation_tuberculosis).
- **Occupational exposure.** This includes pathologists, prosectors, laboratory staff and health-care workers handling infected material, as in the reports above.
- **Unsterile procedures.** Tattooing, piercing, and injections or surgery with unsterilized instruments (PMID 30111996).

**Genetic risk factors.** None are specific to this disease. In general, inborn errors of IL-12/IFN-γ immunity (Mendelian susceptibility to mycobacterial disease, MSMD) make people prone to mycobacterial disease. For example, biallelic mutations in IL12RB1 cause IL-12Rβ1 deficiency. "M. tuberculosis has also caused disease in some MSMD patients" (MSMD reviews, https://pmc.ncbi.nlm.nih.gov/articles/PMC4104692, https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902). This link to inoculation CTB is inferred, not reported.

**Protective factors.** No data specific to this disease were retrieved. Prior sensitization by BCG or earlier infection changes the presentation rather than giving protection. In a sensitized person, inoculation produces tuberculosis verrucosa cutis instead of a chancre (PMID 24770496).

**Gene–environment interactions.** No data were retrieved.

## 3. Phenotypes

Suggested HPO terms are listed as suggestions only; I did not check them against HPO in this session.

| Phenotype | Description and evidence | Suggested HPO |
|---|---|---|
| Papule or nodule at the inoculation site | A papule appears at the site about 2–4 weeks after inoculation. One source puts chancre development "within 3 weeks" (search summary of case literature). Lesions start as "erythematous papules which form firm nontender ulcers" (Maloney & Cohen 2023, PMC10315778). | HP:0200034 Papule; HP:0200035 Skin plaque |
| Painless cutaneous ulcer | A firm, non-tender ulcer (PMC10315778) | HP:0200042 Skin ulcer |
| Regional lymphadenopathy | Present; it is what makes the lesion equivalent to the pulmonary primary complex (PMID 35853774) | HP:0002716 Lymphadenopathy |
| Tuberculin conversion | The skin test turns from negative to positive. This was documented in a prosector's paronychia case (Goette et al., Arch Dermatol 1978). | — |
| Scarring | Lesions heal with a scar (Wikipedia/PCDS summaries) | HP:0100699 Scarring |

Frequency, severity and quality-of-life data were not available.

**Natural history.** Without treatment, the lesion "heals with scarring after several months, and may occasionally evolve into tuberculosis verrucosa cutis or lupus vulgaris" (https://en.wikipedia.org/wiki/Primary_inoculation_tuberculosis). About one-third of skin TB overall is associated with systemic involvement (Kaul et al., CME Part I, https://www.em-consulte.com/article/1629517/resume/cutaneous-tuberculosis-part-i-pathogenesis-classif).

## 4. Genetic/Molecular Information

Most fields here do not apply because this is an infectious disease:
- Causal human genes, pathogenic variants and ClinVar data: not applicable.
- Chromosomal abnormalities: not applicable.
- Epigenetic data specific to this disease: none found.
- Host susceptibility modifiers: possibly MSMD genes such as IL12RB1 (HGNC:5971), IFNGR1 and others. This is general background on mycobacterial susceptibility, not shown for this disease (PMC4104692).

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (NCBITaxon:1773); less often *M. bovis* (NCBITaxon:1765) or BCG (StatPearls).
- **Exposures:** contaminated sharps, autopsy and laboratory work, tattooing and piercing, and unsterile medical procedures (PMID 30111996; HCW case reports above).
- **Lifestyle:** no data specific to this disease.

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps 1–2 and 6–7 come from the clinical reviews cited. Steps 3–5 are inferred from general TB immunology and were not shown in skin.

1. Trauma breaks the skin barrier, and *M. tuberculosis* is introduced into the dermis of a tuberculin-naïve host. This **leads to** local infection (PMID 20725570, 24770496).
2. Bacilli are taken up by dermal macrophages and neutrophils. With no prior adaptive immunity, bacteria multiply locally, which **results in** an inflammatory papule after about 2–4 weeks (PMC10315778).
3. *Inferred:* bacteria travel through lymphatics to the draining lymph nodes, which **leads to** regional lymphadenitis and forms the "cutaneous primary complex" (PMID 35853774).
4. *Inferred:* dendritic cells prime antigen-specific CD4⁺ Th1 cells in the node. IL-12 drives IFN-γ production, which **leads to** macrophage activation. This axis is the one disrupted in MSMD (PMC4104692).
5. *Inferred:* cell-mediated immunity develops. This **results in** tuberculin conversion and formation of epithelioid granulomas with caseous necrosis.
6. Tissue necrosis **leads to** a firm, painless ulcer (PMC10315778).
7. The outcome then branches:
   - **(a)** With treatment, the lesion resolves; one review reports resolution within about 4 weeks of starting therapy (PMC10315778).
   - **(b)** Without treatment, immune containment **results in** healing with a scar over months.
   - **(c)** Occasionally, persistent infection **leads to** lupus vulgaris or TB verrucosa cutis, and rarely to dissemination (Wikipedia/PCDS summaries; Kaul et al.).

**Suggested ontology terms** (not checked):
- **GO:** GO:0002544 chronic inflammatory response; GO:0006909 phagocytosis; GO:0032729 positive regulation of type II interferon production; GO:0042832 defense response to protozoan, not ideal (the better term is GO:0042742 defense response to bacterium).
- **CL:** CL:0000235 macrophage; CL:0000775 neutrophil; CL:0000451 dendritic cell; CL:0000545 T-helper 1 cell; CL:0000312 keratinocyte.

**Omics, single-cell, spatial and CRISPR data:** none specific to this disease were retrieved.

## 7. Anatomical Structures Affected

- **Primary site:** the skin, specifically the dermis and subcutis (UBERON:0002097 skin of body; UBERON:0002067 dermis).
- **Common lesion sites:** the face and the extremities (hands, knees, ankles), plus the buttocks (https://en.wikipedia.org/wiki/Primary_inoculation_tuberculosis).
- **Secondary involvement:** regional lymph nodes (UBERON:0000029 lymph node).
- **Laterality:** usually a single lesion at the injury site. This is an inference from the case series.
- **Subcellular:** the bacteria live inside the phagosome or phagolysosome of macrophages (GO:0045335 phagocytic vesicle). This is general TB biology.

## 8. Temporal Development

- **Incubation:** about 2–4 weeks from inoculation to the first lesion (PMC10315778; case literature).
- **Typical age:** children and young adults, plus occupationally exposed adults.
- **Onset pattern:** subacute.
- **Course without treatment:** self-limited over months, healing with a scar, with occasional progression to chronic forms (Wikipedia summary).
- **Course with treatment:** rapid response, often within weeks (PMC10315778; HCW case at katalog.lib.cas.cz).

## 9. Inheritance and Population

- **Inheritance:** none. This is an acquired infection.
- **Epidemiology:** CTB overall is 1–2% of extrapulmonary TB (PMC9073256). The primary inoculation form is among the rarest subtypes. No prevalence or incidence figures for it were retrieved.
- **Geography:** it follows TB-endemic regions. One review notes that "the epidemiology of CTB is not well studied" (Pathogens 2023).
- **Sex ratio and age distribution:** no data retrieved.

## 10. Diagnostics

**Histopathology.** A biopsy is needed: "histopathology is needed for diagnosis" (Maloney & Cohen 2023, PMC10315778). Early chancres are reported to show an acute neutrophilic infiltrate with many bacilli, and granulomas with caseation develop later. I could not confirm this sequence in a retrieved source.

**Acid-fast stain and culture.** Use Ziehl–Neelsen staining and mycobacterial culture (BACTEC/MGIT), as in the HCW case confirmed by BACTEC 460TB culture (cmedm,16334632).

**Molecular tests.** Sensitivity varies widely:

| Study | Test and sample | Result |
|---|---|---|
| Clin Epidemiol Glob Health 2025, 41 patients | Xpert MTB/RIF (CB-NAAT) vs. culture | Sensitivity 37.5%, specificity 91%; rifampicin resistance in 3 of 6 positives (https://doaj.org/article/d55a3fb3df644c488964f13a0590a49c) |
| J Pure Appl Microbiol 2021, 76 skin biopsies | Xpert | Detected MTB in 9 cases, all also culture-positive (https://doaj.org/article/d371dc0f9b3447e8b01cfe14ef901986) |
| 2005, 37 biopsies | Conventional PCR vs. culture | Sensitivity 95.2%, specificity 100% (PMC500826) |
| Review table, 2018 | PCR across studies | Sensitivity about 25–95% (PMC6077618) |

A negative PCR therefore does not rule out the disease.

**Immunological tests.** Look for tuberculin skin test conversion or a positive interferon-gamma release assay (IGRA).

**Systemic work-up.** Get a chest X-ray and a review of systems for other extrapulmonary TB (PMC10315778).

**Differential diagnosis** (from general dermatology reviews, not specific sources):
- Sporotrichosis
- *M. marinum* and other nontuberculous mycobacteria
- Cat-scratch disease
- Tularemia
- Syphilitic chancre
- Leishmaniasis
- Pyogenic infection, such as the *S. aureus* that delayed diagnosis in the 2015 intern case

**Genetic testing:** not applicable. An MSMD gene panel could be considered only if mycobacterial disease is unusually severe or disseminated (PMC4104692).

## 11. Outcome/Prognosis

- **Prognosis:** excellent with treatment. The lesion resolves, and healing is rapid with ATT, with or without debridement (cmedm,16334632; PMC10315778).
- **Untreated:** the lesion heals with scarring over months, but can occasionally progress to lupus vulgaris or TB verrucosa cutis (Wikipedia summary).
- **Mortality and quality-of-life data:** none retrieved.

## 12. Treatment

- **Standard regimen:** "All types [of CTB] are treated with 6 months of ATT" (Maloney & Cohen 2023, PMC10315778). This means isoniazid, rifampicin, pyrazinamide and ethambutol for 2 months, then isoniazid and rifampicin for 4 months, following TB guidelines. The 1978 prosector's paronychia case responded to isoniazid, rifampin and pyridoxine (Goette et al., https://scilit.com/publications/5de059afd18b98ea16e171d88098c8e5).
- **Suggested NCIT terms** (not checked): Isoniazid (C569), Rifampin (C797), Pyrazinamide, Ethambutol, Pyridoxine.
- **Drug resistance:** check rifampicin resistance with Xpert. Rifampicin-resistant cases have been reported in CTB (2025 CB-NAAT study).
- **Surgery:** surgical debridement can be added (cmedm,16334632).
- **Pharmacogenomics:** general TB knowledge holds that NAT2 acetylator status affects isoniazid toxicity. No source for this was retrieved in this session.
- **Advanced therapies and trials:** none found.

## 13. Prevention

- **Primary prevention:**
  - Sharps safety and standard precautions for health-care, laboratory and autopsy workers.
  - Sterile tattooing and piercing practice (PMID 30111996).
  - TB control in the community.
  - BCG vaccination. Vaccination is expected to alter the presentation rather than to reliably prevent infection; this is inferred.
- **Secondary prevention:** after a sharps exposure to TB material, test with a tuberculin skin test or IGRA, and keep watch on the wound site. This is inferred from the HCW case literature.
- **Genetic counseling:** not applicable.

## 14. Other Species / Natural Disease

- No natural cutaneous inoculation TB in animals was retrieved.
- *M. bovis* infects cattle and can pass to humans (zoonotic), and it is a recognized cause of CTB (StatPearls NBK482220).
- In rabbits, intradermal live BCG causes granulomas and ulceration, while heat-killed bacteria cause smaller lesions without liquefaction (PMC3073244). This is an experimental model, not natural disease.

## 15. Model Organisms

- **Rabbit:** intradermal BCG produces granulomas and ulceration (PMC3073244).
- **Mouse:** intradermal BCG has been injected into dorsal scapular skin (JoVE protocol). ICAM-1-deficient mice did not mount a delayed-type hypersensitivity response to intradermal mycobacterial antigens (PMC108103).
- **Human:** a controlled human infection study used intradermal BCG and sampled skin on days 3 and 15 (https://scholars.duke.edu/publication/1645823).
- **Limitations:** no retrieved model uses *M. tuberculosis* inoculated into the skin of naïve animals in a way that copies the chancre plus lymphadenopathy complex.

---

**Gaps:**
- MONDO ID not checked.
- No frequency, epidemiology or quality-of-life data specific to this form.
- Histological evolution of the chancre not confirmed in a retrieved source.
- Several PMIDs come from search summaries: PMID 20725570, 24770496, 30111996 and 35853774. PMC10315778 had no PMID shown.

Sources:
- [Frankel et al., PMC2923933](https://pmc.ncbi.nlm.nih.gov/articles/PMC2923933)
- [Santos et al., PMID 24770496](https://pmc.ncbi.nlm.nih.gov/articles/pmid/24770496)
- [Maloney & Cohen 2023, PMC10315778](https://pmc.ncbi.nlm.nih.gov/articles/PMC10315778)
- [An Bras Dermatol 2022, PMC9073256](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9073256/)
- [Pathogens 2023](https://mdpi.com/2076-0817/12/7/920)
- [StatPearls NBK482220](https://ncbi.nlm.nih.gov/books/NBK482220)
- [Kaul et al., CME Part I](https://www.em-consulte.com/article/1629517/resume/cutaneous-tuberculosis-part-i-pathogenesis-classif)
- [Wikipedia, Primary inoculation tuberculosis](https://en.wikipedia.org/wiki/Primary_inoculation_tuberculosis)
- [Saudi J Med Med Sci 2015](https://doaj.org/article/b893819535d24abaadfb83812fe4387b)
- [HCW case report (cmedm,16334632)](https://katalog.lib.cas.cz/KNAV/EdsRecord/cmedm,16334632)
- [Goette et al. 1978](https://scilit.com/publications/5de059afd18b98ea16e171d88098c8e5)
- [ICD-11 1B12.8 (findacode)](https://findacode.com/icd-11/code-625292625.html)
- [ICD-10 A18.4 (gesund.bund.de)](https://gesund.bund.de/en/icd-code-suche/a18-4)
- [MeSH D014382](https://meshb.nlm.nih.gov/record/ui?ui=D014382)
- [CB-NAAT study 2025](https://doaj.org/article/d55a3fb3df644c488964f13a0590a49c)
- [Xpert on skin biopsies 2021](https://doaj.org/article/d371dc0f9b3447e8b01cfe14ef901986)
- [PCR on biopsies 2005, PMC500826](https://pmc.ncbi.nlm.nih.gov/articles/PMC500826)
- [Review table 2018, PMC6077618](https://pmc.ncbi.nlm.nih.gov/articles/PMC6077618)
- [MSMD review, PMC4104692](https://pmc.ncbi.nlm.nih.gov/articles/PMC4104692)
- [MSMD review, PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)
- [Rabbit intradermal BCG, PMC3073244](https://pmc.ncbi.nlm.nih.gov/articles/PMC3073244/figure/F2)
- [ICAM-1-deficient mice, PMC108103](https://pmc.ncbi.nlm.nih.gov/articles/PMC108103)
- [Controlled human infection study (Duke Scholars)](https://scholars.duke.edu/publication/1645823)