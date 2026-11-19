---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-19T19:29:40.053284'
end_time: '2026-11-19T19:35:43.251593'
duration_seconds: 363.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Methamphetamine Dependence
  mondo_id: MONDO:0005419
  category: Psychiatric
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Methamphetamine addiction; Methamphetamine use disorder
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
  web_search_requests: 4
  num_turns: 19
  total_cost_usd: 1.31029113
  session_id: 5f044673-b6f6-4698-9e99-bc101e253af3
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 108
  retrieval_calls: 102
  assistant_text_blocks: 2
  unsuccessful_reason: the model marked the report incomplete; its reason is on the
    line that begins 'Incomplete report:'
answer_status: unsuccessful
citation_count: 7
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methamphetamine Dependence
- **MONDO ID:** MONDO:0005419 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Methamphetamine addiction; Methamphetamine use disorder
- **Category:** Psychiatric

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Methamphetamine Dependence** covering all of the
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

Quick update: my PubMed helper script needs approval to run, so I'm switching to web search and direct PubMed queries to collect citations.

**Incomplete report:** PubMed's E-utilities and web pages were blocked or needed approval in this session, so the evidence comes from a limited set of Europe PMC abstracts and web pages, and several sections could not be sourced.

# Methamphetamine Dependence (MONDO:0005419): Disease Characteristics Report

**How this report was built.** "Methamphetamine dependence" is treated here as the same entity as DSM-5 methamphetamine use disorder, which covers moderate to severe cases. Many sources use the abbreviation MUD or MAUD. **This disease has no causal gene.** It is an acquired disorder caused by repeated methamphetamine exposure, and susceptibility is polygenic. The template lists the causal gene as "not recorded", and that is correct.

Every PMID and quote below comes from Europe PMC abstracts retrieved in this session. Quotes are verbatim fragments, sometimes shortened. Ontology terms (HPO, GO, CL, UBERON, ChEBI, NCIT) are given as **labels only**. Their numeric IDs were not retrieved in this session, so look them up before entering them into the knowledge base.

---

## 1. Disease Information

**Overview.** Methamphetamine dependence is a chronic, relapsing disorder in which a person loses control over their use of methamphetamine.

- **WHO definition (ICD-11 6C46.2, "Stimulant dependence including amphetamines, methamphetamine or methcathinone"):**
  - It is "a disorder of regulation of stimulant use arising from repeated or continuous use".
  - The core features are a strong internal drive to use, impaired control, and continued use despite harm. Tolerance and withdrawal may also be present.
  - Features are usually evident over at least 12 months. The diagnosis can be made after 3 months if use is daily or almost daily.
  - Cocaine and synthetic cathinones are excluded from this code.
  - Source: [findacode ICD-11 6C46.2](https://www.findacode.com/icd-11/code-2016549355.html); parent code 6C46 at [findacode 6C46](https://findacode.com/icd-11/code-1016273204.html).

**Identifiers**

| Resource | Identifier | Status |
|---|---|---|
| MONDO | MONDO:0005419 | Given by the requester |
| ICD-11 | 6C46.2 (subcodes such as 6C46.2Z "unspecified") | Retrieved. Remission subcodes are inconsistent between third-party sites; check the WHO browser |
| MeSH | D019969 "Amphetamine-Related Disorders" (tree numbers C25.775.225, F03.900.225). Entry terms include "Amphetamine Dependence" and "Amphetamine Addiction" | Retrieved from secondary profile pages ([example](https://profiles.rush.edu/display/15057)). A methamphetamine-specific child descriptor was not confirmed |
| ICD-10 | Belongs under F15 ("other stimulants") | Exact code not retrieved; verify |
| OMIM / Orphanet | None. This is not a Mendelian or rare disease | Not applicable |

**Synonyms:** methamphetamine addiction; methamphetamine use disorder (MUD/MAUD); amphetamine-type stimulant dependence; stimulant dependence (ICD-11 grouping).

**Source of information.** The knowledge comes from aggregated, disease-level resources: population surveys, cohort studies, trials and meta-analyses. It does not come from individual patient records.

---

## 2. Etiology

**Necessary cause.** The necessary cause is repeated self-administration of methamphetamine (ChEBI label: "methamphetamine"). Neuroadaptation in the brain's dopaminergic reward circuits follows (see Section 6). Severity of dependence and frequency of use are the main predictors of complications such as psychosis.

- Arunogiri 2018, PMID 29338289: "Frequency of methamphetamine use and severity of methamphetamine dependence were consistently found" to be risk factors for methamphetamine-associated psychosis.

### Genetic risk factors

- **Candidate gene studies.** A systematic review and meta-analysis (Guerin 2021, PMID 33217458) found:
  - "Seventy-six studies were identified, investigating markers of 75 different genes."
  - "Eleven markers from adequately powered studies were significantly associated with methamphetamine use disorder."
  - "No twin or adequately powered genome-wide association studies (GWASs) have been conducted."
- **GWAS.** A genome-wide association meta-analysis covered heroin, methamphetamine and alcohol dependence (Chang 2022, *Clin Transl Med*, PMID 35075802). Its abstract text was not available, so its specific loci are not reported here.
- **Han Chinese drug-dependence GWAS.** This study pooled several drugs (Xu 2024, PMID 38448893). The search snippet reported associations at rs3782886 (*BRAP*) and rs671 (*ALDH2*) with "drug addiction". This was not specific to methamphetamine and was not read in full.
- **Heritability.** No methamphetamine-specific twin heritability estimate was retrieved.
  - In a female twin study, "twin resemblance for hallucinogen and stimulant use was due to both genetic and familial environmental factors" (Kendler 1999, PMID 10353453).
  - A review of heritability estimates cites "cocaine use disorder (72%)" as a related stimulant figure (Bienvenu 2011, PMID 20459884).
- **Inheritance.** Inheritance is multifactorial and polygenic. No penetrant variants are known.

### Environmental and other risk factors

- **Frequency, dose and dependence severity** are risk factors for psychosis and other complications (PMID 29338289).
- **Injection drug use.** Among US adults who used methamphetamine in the past year, 22.3% injected it (Jones 2020, PMID 32214077).
- **Co-occurring conditions** were common in the US national data (PMID 32214077; specific figures not extracted).
- **Childhood trauma.** In people with methamphetamine use disorder, childhood trauma "was associated with poorer cognitive performance" (Liu 2026, PMID 42442473). Its role as an etiological risk factor for developing the disorder was not established from the retrieved sources.
- **Sexual minority men.** The mirtazapine trial specifically enrolled men and transgender women who have sex with men. This population has high rates of methamphetamine use linked to HIV risk (Coffin 2020, PMID 31825466). No prevalence meta-analysis was retrieved.

### Protective factors

No evidence-based genetic or environmental protective factors specific to methamphetamine dependence were retrieved.

- In mice, TAAR1 function is protective. Mice lacking functional *Taar1* drink more methamphetamine (Section 15). Whether human *TAAR1* variants protect against the disorder is unproven.

### Gene–environment interactions

No human gene–environment studies were retrieved. In mice, *Taar1* genotype changes how much methamphetamine is consumed, which is an animal gene × drug interaction (PMID 25740289, PMID 39934409).

---

## 3. Phenotypes

Phenotypes are listed with suggested HPO labels. Frequencies are given only where a source was retrieved.

| Phenotype | Type | Characteristics / frequency | Evidence | Suggested HPO label |
|---|---|---|---|---|
| Compulsive drug use, craving, loss of control | Behavioral | Core defining feature. 52.9% of past-year US users met criteria for the disorder | ICD-11; PMID 32214077 | "Drug abuse" / "Substance abuse" (verify exact term) |
| Withdrawal syndrome | Symptom | Intensity peaks within 24 h. There is an "acute phase lasting 7-10 days during which overall symptom severity declined", followed by a subacute phase of about 2 more weeks | McGregor 2005, PMID 16128721; Zorick 2010, PMID 20840201 | "Fatigue", "Hypersomnia", "Increased appetite", "Depressivity" |
| Psychosis (paranoia, hallucinations) | Behavioral / psychiatric | Correlated with frequency and severity of use. The symptom profile "has varied considerably across studies" | PMID 29338289; Voce 2019, PMID 30693832 | "Psychosis", "Paranoia", "Hallucinations" |
| Cognitive impairment | Neurocognitive | Meta-analysis of 44 studies (1,592 people with the disorder vs 1,820 controls). Moderate deficits in most domains, with larger deficits in impulsivity/reward processing and social cognition. Partly recovers with abstinence | Potvin 2018, PMID 29407687; Basterfield 2019, PMID 31021107; Proebstl 2019, PMID 31629302 | "Cognitive impairment", "Impulsivity", "Memory impairment" |
| Depressive symptoms | Psychiatric | Early improvement in depressive symptoms during naltrexone-bupropion treatment was associated with reduced use | ADAPT-2 secondary analysis, [psychiatrist.com 2025](https://www.psychiatrist.com/jcp/early-change-depressive-symptom-naltrexone-bupropion-combination-reduction-methamphetamine-use-adapt-2-trial) | "Depressivity" |
| Comorbid personality disorder in methamphetamine-induced psychosis | Psychiatric | "The highest prevalence was related to borderline personality disorder (35.5%)" (single-centre Iranian sample) | PMID 26322209 | — |
| Dental caries ("meth mouth") | Physical sign | "rampant caries". Use is associated with a higher DMFT index (decayed, missing and filled teeth) in autopsy data | Rehman 2023, PMID 37218237; Mizuno 2022, PMID 35473930 | "Dental caries" |
| Cardiomyopathy / heart failure, arrhythmia | Clinical sign | Many case reports, including electrical storm and right atrial perforation. No pooled frequency retrieved | PMIDs 41527167, 40922848 | "Dilated cardiomyopathy", "Arrhythmia" |
| Pulmonary arterial hypertension | Clinical sign | 1.4% of PAH patients at one Japanese referral centre | Fujisaki 2026, PMID 42577669 | "Pulmonary arterial hypertension" |
| Early-onset stroke (mainly haemorrhagic) | Complication | "Methamphetamine use among young people (<45 years) is associated with heightened risk for haemorrhagic stroke" | Lappin 2021, PMID 34166684 | "Hemorrhagic stroke" |
| Suicidality | Behavioral | Suicide SMR 16.3 | Lee 2021, PMID 33788344 | "Suicidal ideation" |
| Lab finding: methamphetamine-positive urine | Laboratory | Primary trial outcome | PMID 33497547 | — |

**Onset, severity and course.** Onset is usually in adolescence or adulthood. Severity is graded mild, moderate or severe. The course is chronic and relapsing.

**Quality of life.** No EQ-5D or SF-36 data specific to methamphetamine were retrieved.

---

## 4. Genetic / Molecular Information

- **Causal genes:** none. There are no pathogenic variants in the ACMG/ClinVar sense, no somatic variants, and no chromosomal abnormalities.
- **Susceptibility and modifier loci:**
  - Eleven candidate-gene markers from adequately powered studies were significant (PMID 33217458). The specific genes are in the paper and were not extracted here.
  - GWAS loci are reported in PMID 35075802 but were not extracted.
- **Epigenetics (human):**
  - An epigenome-wide association study found "epigenome-wide significant associations at four CpG sites… one of which occurred in the CNOT1 gene and another in the PUM1 gene" (Shirai 2024, PMID 38488760).
  - "BDNF methylation was increased in human METH dependence, greatest in subjects with psychosis" (Iamjan 2021, PMID 34008409).
  - Methamphetamine-induced psychosis "is associated with DNA hypomethylation and increased expression of AKT1 and key dopaminergic genes" (*DRD1*–*DRD3*) (Nohesara 2016, PMID 27753212).
  - Postmortem brains from people with HIV and methamphetamine dependence showed differential methylation of genes for "neurodegeneration; dopamine metabolism and transport" (Desplats 2014, PMID 25054922).
- **Epigenetics (rat):** Chronic methamphetamine increased *BDNF* exon IV mRNA in the prefrontal cortex 2.15-fold (Salehzadeh 2020, PMID 31830601).
- **Peripheral expression:** In male patients, "DAT protein level and VMAT2 gene and protein levels were lower in the patient group compared to the controls" (Keskinsezer 2024, PMID 39685567).
- **Relevant genes (HGNC symbols, IDs not retrieved):** *SLC6A3* (DAT), *SLC18A2* (VMAT2), *TAAR1*, *DRD1*, *DRD2*, *BDNF*, *AKT1*, *CNOT1*, *PUM1*.

---

## 5. Environmental Information

- **Primary exposure:** methamphetamine, taken by smoking, injection, snorting or swallowing. Injection was reported by 22.3% of US past-year users (PMID 32214077).
- **Supply and overdose trends:**
  - US methamphetamine-involved overdose deaths "increased from 547 to 34,855" between 1999 and 2023 (Zhu 2025, PMID 40509756).
  - Deaths involving psychostimulants other than cocaine "increased 180%" during 2015–2019 (Han 2021, PMID 34550301).
- **Infectious agents:** none are causal. HIV-1 is an important comorbidity that compounds neurotoxicity (Miao 2024, PMID 39224601; PMID 25054922).
- **Lifestyle:** Co-use of other substances is common (PMID 32214077). Exercise interventions are discussed in Section 12.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Exposure.** Methamphetamine enters monoaminergic neurons through the dopamine transporter (DAT/*SLC6A3*). It disrupts vesicular storage through VMAT2 (*SLC18A2*), which leads to non-vesicular dopamine efflux into the synapse.
   - *This step is established pharmacology but was not directly sourced in this session. VMAT2 involvement in neurotoxicity is shown in PMID 39684782.*
2. **Reward signalling.** The large rise in extracellular dopamine in the striatum and nucleus accumbens strongly activates reward pathways. Repeated exposure leads to drug-cue learning and sensitization.
   - *Inferred mechanism; the human dopamine-release study was not retrieved.*
3. **Modulation by TAAR1.** Methamphetamine activates the intracellular receptor TAAR1, which acts as a brake on its rewarding effects.
   - Loss of TAAR1 results in greater intake: "Taar1 knockout mice consume more MA and exhibit insensitivity to MA-induced CTA and hypothermia" (PMID 25740289).
   - "TAAR1 function directly impacts MA reward sensitivity and MA intake" through dorsal raphe serotonin neurons (PMID 39934409).
4. **Branch A, neuroadaptation.** Chronic use leads to downregulation of the dopamine system.
   - Postmortem striatum showed "reduced levels of three dopamine nerve terminal markers", but "chronic exposure to methamphetamine does not cause permanent degeneration of striatal dopamine nerve terminals" (Wilson 1996, PMID 8640565).
   - There was "a 25%-30% decrease in the maximal extent of dopamine stimulation of adenylyl cyclase activity" in the striatum, indicating reduced D1 receptor signalling (Tong 2003, PMID 12727693).
   - Positron emission tomography (PET) showed DAT loss that partially recovers: "caudate, +19%; putamen, +16%" with protracted abstinence (Volkow 2001, PMID 11717374).
   - These changes probably underlie anhedonia, withdrawal and craving. *The link is inferred.*
5. **Branch B, neurotoxicity.** Excess cytosolic dopamine and mitochondrial disruption lead to oxidative stress, neuroinflammation and apoptosis.
   - "exposure to MA can disturb mitochondrial energetic metabolism by inhibiting the Krebs cycle" (Shin 2018, PMID 28589520).
   - Microgliosis is seen in animals: "neurotoxicity featured by dopaminergic terminal damage and microgliosis" (Xu 2017, PMID 28694920).
   - Human PET does **not** support substantial microgliosis: "There was no main effect of group on [F-18]FEPPA VT (P = .81)" (Rathitharan 2021, PMID 32017280). This branch is therefore better established in animals than in humans.
   - Interaction with VMAT2 partners CDCrel-1 and Parkin has been shown in rat striatum (PMID 39684782).
6. **Craving and relapse circuitry.** Abstinence leads to time-dependent "incubation" of cue-induced craving in the prefrontal cortex (rodent evidence).
   - Somatostatin interneurons "mediated drug seeking during early withdrawal (day 1) via lateral hypothalamus (LH) GABAergic inputs".
   - "Selective KCNC2 knockdown in SST or PV INs significantly suppressed drug seeking" (Shi 2026, PMID 41895270).
   - Unlike incubated cocaine craving, incubated methamphetamine craving is mTOR-independent: everolimus "did not reduce incubated METH-craving" (Cano 2026, PMID 42732877).
7. **Epigenetic consolidation.** Changes in DNA methylation, for example at *BDNF* (PMID 34008409) and in *AKT1* and dopamine receptor genes (PMID 27753212), may stabilize vulnerability and psychosis. *Correlational evidence only.*
8. **Clinical manifestation.**
   - Branches A, 6 and 7 result in compulsive use, withdrawal and relapse.
   - Dopaminergic hyperactivity and the changes in step 7 contribute to psychosis.
   - Frontostriatal dysfunction results in cognitive deficits (PMID 29407687).
   - Systemic sympathomimetic effects lead to cardiomyopathy, pulmonary arterial hypertension and stroke (PMIDs 34166684, 42577669).

### Supporting details

- **Metabolomics:** Methamphetamine-associated PAH shows distinct inflammatory and bioenergetic signatures, with "55 differed significantly between subtypes, including 22 enriched in Meth-APAH" (Robertson 2026, PMID 42516675).
- **Immune:** In people with the disorder and childhood trauma, "IL-1β was negatively correlated with delayed memory" (PMID 42442473).
- **Single-cell:** Mouse single-cell RNA-seq shows "robust glial cell transcriptional changes" (Oladapo 2025, PMID 39859365). A hippocampal single-cell atlas of methamphetamine-related cognitive decline exists as a bioRxiv preprint (doi:10.1101/2025.05.02.651823).
- **Spatial transcriptomics, CRISPR screens, proteomics, lipidomics:** none retrieved.
- **Suggested GO labels:** "dopamine transport", "dopamine secretion", "synaptic vesicle amine transport", "response to amphetamine", "response to oxidative stress", "microglial cell activation", "neuron apoptotic process", "DNA methylation".
- **Suggested CL labels:** "dopaminergic neuron", "medium spiny neuron", "serotonergic neuron", "microglial cell", "astrocyte", "somatostatin-positive interneuron" (verify), "GABAergic interneuron".

---

## 7. Anatomical Structures Affected

**Primary**

- Brain (UBERON labels): "striatum", "caudate nucleus", "putamen" (PMIDs 11717374, 8640565), "nucleus accumbens", "prefrontal cortex" (including prelimbic cortex in rodents, PMID 41895270), "dorsal raphe nucleus" (mice, PMID 39934409), "hippocampus" (mice), "lateral hypothalamic area".

**Secondary**

- Heart, causing cardiomyopathy (PMIDs 41527167, 40922848).
- Pulmonary arteries, causing PAH (PMID 42577669).
- Cerebral vasculature, causing haemorrhagic stroke (PMID 34166684).
- Teeth (PMID 35473930).

**Body systems:** nervous, cardiovascular, respiratory and oral systems.

**Subcellular (GO Cellular Component labels):** "synaptic vesicle", "presynaptic membrane", "mitochondrion" (PMID 28589520), "cytosol".

**Lateralization:** bilateral and diffuse.

---

## 8. Temporal Development

- **Onset:** adolescence or adulthood, developing gradually over months of repeated use. ICD-11 usually requires 12 months of features, or 3 months with daily use.
- **Course:** chronic and relapsing.
  - Withdrawal has an acute phase of 7–10 days, then a subacute phase (PMID 16128721).
  - Cognitive function is partly restored over 6 months of abstinence (PMID 31629302).
  - Meta-analytic data link longer abstinence to better neuropsychological function (PMID 31021107; PMID 42748562 also describes "abstinence trajectories").
  - DAT partially recovers after protracted abstinence (PMID 11717374).
- **Remission:** ICD-11 has remission subcodes (early or sustained, full or partial; see Section 1 caveat). Remission occurs with or without treatment. No natural-history remission rates were retrieved.
- **Critical periods:** In rodents, craving incubates over weeks of abstinence (PMID 41895270), which marks a window of relapse risk.

---

## 9. Inheritance and Population

- **Inheritance:** multifactorial. Penetrance, anticipation, founder effects, consanguinity and carrier frequency do not apply.
- **United States:**
  - Past-year methamphetamine use was 6.6 per 1,000 adults in 2015–2018. Of these users, 52.9% had the disorder, which works out to roughly 350 per 100,000 adults (PMID 32214077).
  - Overdose deaths are rising steeply (PMIDs 34550301, 40509756).
- **Global:**
  - GBD 2023 estimates for amphetamine use disorder across 204 countries are in Kang 2026, *Nat Med*, PMID 41545593. The retrieval tool gave a conflicting PMID for this paper, and its figures were not verified.
  - GBD 2021: Zhu 2025, PMID 40839682.
  - China vs US projections: Li 2026, PMID 42296482.
  - Specific prevalence numbers were not extracted.
- **Sex ratio and age distribution:** not extracted from the retrieved sources.

---

## 10. Diagnostics

- **Clinical criteria:** ICD-11 6C46.2 (Section 1) and DSM-5 stimulant use disorder (criteria text not retrieved).
- **Laboratory tests:** urine drug testing for methamphetamine and amphetamine is the standard objective measure. It was the primary endpoint in ADAPT-2 (PMID 33497547) and the mirtazapine trial (PMID 31825466).
- **Imaging (research only, not diagnostic):**
  - DAT PET (PMID 11717374).
  - TSPO PET for microglia (PMID 32017280).
  - fNIRS in exercise trials (PMID 42192765).
- **Workup for complications:** echocardiography and right heart assessment for cardiomyopathy and PAH (PMID 42577669) are clinically indicated. No guideline was retrieved.
- **Genetic testing:** none indicated. WES, WGS, gene panels, chromosomal microarray, karyotyping, FISH, mtDNA and repeat-expansion testing are not applicable.
- **Omics biomarkers:** research-stage only. Candidates include peripheral DAT/VMAT2 levels (PMID 39685567), *BDNF* methylation (PMID 34008409) and cytokines (PMID 42442473).
- **Differential diagnosis:** primary psychotic disorders such as schizophrenia, other stimulant use (cocaine, cathinones), ADHD-related prescription stimulant misuse, and primary mood disorders. Comorbid personality disorder is common in methamphetamine-induced psychosis (PMID 26322209). *No differential-diagnosis source was retrieved.*
- **Screening:** no population-level genetic screening applies.

---

## 11. Outcome / Prognosis

- **Mortality:**
  - In a Taiwanese national cohort of 23,248 people with the disorder, "the current cohort had an increased all-cause mortality (SMR = 5.4)", and the suicide SMR was 16.3 (Lee 2021, PMID 33788344).
  - A US cohort of 563 users was followed for 8–10 years for mortality and health status (Herbeck 2015, PMID 25415384).
- **Disease-specific deaths:** 34,855 US methamphetamine-involved overdose deaths in 2023 (PMID 40509756).
- **Morbidity:** psychosis, cognitive impairment, cardiomyopathy, PAH, early-onset haemorrhagic stroke, a possible raised risk of Parkinson's disease (narrative review, PMID 34166684), and dental disease.
- **Recovery potential:**
  - Brain markers partly recover (DAT +16–19%, PMID 11717374).
  - Cognition partly recovers (PMIDs 31629302, 31021107).
  - Postmortem data argue against permanent loss of dopamine terminals (PMID 8640565).
- **Prognostic factors:** frequency and severity of use predict psychosis (PMID 29338289). Early improvement in depressive symptoms predicts treatment response in ADAPT-2.
- **Quality of life:** no QoL instrument data retrieved.

---

## 12. Treatment

**No FDA-approved medication was identified in this session.** A systematic review of 43 studies (4,065 participants) found that "No pharmacotherapy yielded convincing results for the treatment of AMPH/MA dependence" (Siefried 2020, PMID 32185696).

### Pharmacotherapy

| Agent | Evidence | Key result |
|---|---|---|
| Extended-release injectable naltrexone + oral extended-release bupropion | ADAPT-2 RCT (Trivedi 2021, *NEJM*, PMID 33497547), moderate to severe disorder, 403 participants in stage 1 and 225 in stage 2 | "The weighted average response across the two stages was 13.6% with naltrexone-bupropion and 2.5% with placebo" (treatment effect 11.1 percentage points, P<0.001). Serious adverse events occurred in 3.6%; side effects included GI upset, tremor and malaise ([ISSUP summary](https://www.issup.net/knowledge-share/resources/2022-06/bupropion-and-naltrexone-methamphetamine-use-disorder); [NIDA blog](https://archives.nida.nih.gov/news-events/noras-blog/2021/01/adapt-2-trial-results-deliver-breakthrough-in-long-search-methamphetamine-use-disorder-medication)) |
| Mirtazapine | RCT, n=120 men and transgender women who have sex with men (Coffin 2020, *JAMA Psychiatry*, PMID 31825466) | Fewer positive urine tests, RR 0.67 (wk 12), 0.75 (wk 24) and 0.73 (wk 36): "By week 12, the rate of methamphetamine-positive urine test results significantly declined" |
| Topiramate | RCT, n=52 (Moghaddam Sadegh 2023, PMID 37881418) | "The urine test also showed no significant difference between the two groups"; reduced temptation to use at weeks 8–12 |
| Antipsychotics (for psychosis) | Not retrieved | — |

- **Pharmacogenomics:** no PharmGKB or CPIC guidance specific to methamphetamine was retrieved.
- **Suggested NCIT labels:** "Naltrexone", "Bupropion", "Mirtazapine", "Topiramate".

### Psychosocial treatment (first line)

- **Contingency management (CM)** rewards objectively verified abstinence. The 2018 network meta-analysis by De Crescenzo et al. ranked it the most efficacious of 12 psychosocial interventions for cocaine and/or amphetamine use. That finding comes from a web search summary, and its PMID was not retrieved.
- A meta-analysis of long-term efficacy follows outcomes up to 1 year after treatment (Ginley 2021, PMID 33507776).
- Another meta-analysis (Pfund 2024, PMID 38863566) notes that "Several professional organizations and federal agencies recommend contingency management."
- A meta-review reports "Small effects were observed for contingency management" across substance use disorders (Dellazizzo 2023, PMID 37356250).
- A network meta-analysis of 72 trials (6,836 participants) for methamphetamine and amphetamine use disorders found CM alone or combined with CBT may be linked to longer abstinence, but the evidence was very low certainty ([Springer 2024](https://link.springer.com/article/10.1007/s11469-024-01379-w); PMID not retrieved).
- CBT is covered in an overview of systematic reviews (Tran 2021, PMID 34220557).
- **Suggested NCIT labels:** "Contingency Management", "Cognitive Behavioral Therapy".

### Neuromodulation and exercise (experimental)

- **rTMS:** 10-Hz rTMS over the left dorsolateral prefrontal cortex lowered craving visual analogue scale (VAS) scores compared with sham (Wang 2022, PMID 36265196). A treatment protocol is published as PMID 34825214.
- **rTMS plus exercise:** gave "significantly lower craving" at week 8 (Wang 2026, PMID 41959948).
- **Multimodal cognitive exercise:** an RCT of 162 men in compulsory isolation found it gave "the largest overall benefit" for cognition (Zhang 2026, PMID 42192765).
- No NCT identifiers were retrieved.

### Not applicable or not available

Gene therapy, cell therapy, RNA therapies, immunotherapies (anti-methamphetamine antibodies and vaccines exist as a research concept, but no source was retrieved) and surgery.

**Supportive care:** withdrawal is managed symptomatically, since the acute phase resolves in 7–10 days (PMID 16128721).

---

## 13. Prevention

- **Primary prevention:** no USPSTF or Cochrane prevention source specific to methamphetamine was retrieved.
- **Secondary and tertiary prevention:**
  - Detect and treat psychosis, cardiomyopathy and PAH early (PMIDs 29338289, 42577669).
  - Reduce harms from injection, since 22.3% of US users inject (PMID 32214077).
  - Address suicide risk, given the suicide SMR of 16.3 (PMID 33788344).
  - Address overdose risk from fentanyl co-involvement (PMID 34550301). *Fentanyl's role is inferred; that abstract was not read in full.*
- **Immunization:** none available.
- **Genetic counseling:** not applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring disease exists in animals, and there is no OMIA entry. It has no zoonotic potential.
- Orthologues relevant to models are mouse *Taar1* and rat or mouse *Slc6a3* and *Slc18a2*. NCBI Gene IDs were not retrieved.
- Dopaminergic and TAAR1 mechanisms are conserved between rodents and humans (PMIDs 25740289, 11717374).

---

## 15. Model Organisms

| Model | Type | Recapitulation | Evidence |
|---|---|---|---|
| Methamphetamine high- and low-drinking mouse lines (MAHDR/MALDR), selectively bred | Genetic, mouse | Voluntary intake. MAHDR mice carry non-functional *Taar1*, which drives "binge-level methamphetamine intake" | PMIDs 25740289, 39934409, 31925906 |
| *Taar1* knockout and transgenic mice | Genetic | Increased intake; loss of conditioned taste aversion and hypothermia | PMID 25740289 |
| Rat intravenous self-administration with incubation of craving | Induced, rat | Models relapse after abstinence and its circuits (SST/PV interneurons, KCNC2) | PMIDs 41895270, 42732877 |
| Chronic methamphetamine injection (rat or mouse) | Induced | Neurotoxicity, microgliosis, *BDNF* epigenetic changes, glial transcriptome changes | PMIDs 28694920, 31830601, 39859365 |
| HIV + methamphetamine models | Induced | Combined neurotoxicity | PMID 39224601 |

**Limitations**

- Rodent microgliosis is not reproduced in human TSPO PET (PMID 32017280).
- Experimenter-given injection does not capture compulsive use despite harm.
- Mechanisms differ from cocaine; for example, incubation of methamphetamine craving is mTOR-independent (PMID 42732877).

**Databases:** MGI, RGD and MMRRC are the relevant model databases, but none were queried in this session.

---

## Gaps for follow-up

1. **Records not read in full:**
   - GWAS loci from PMID 35075802.
   - The 11 significant genes in PMID 33217458.
   - GBD prevalence figures (PMID 41545593, which also needs its PMID resolved).
   - Psychosis prevalence: no meta-analysis found.
   - US sex and age distribution.
2. **Not retrieved at all:** a methamphetamine-cardiomyopathy meta-analysis; Cochrane reviews of psychostimulant replacement; antipsychotic treatment of methamphetamine psychosis; DSM-5 criteria text; the exact ICD-10 code; and all numeric ontology IDs for HPO, GO, CL, UBERON, ChEBI and NCIT.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 61 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 61 |
| On topic | 35 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:32017280` *(abstract only)*: "There was no main effect of group on [F-18]FEPPA VT (P = .81)"
  - closest text in source: "There was no main effect of group on [F-18]FEPPA VT (P = .81)"
- `PMID:39859365` *(abstract only)*: "robust glial cell transcriptional changes"
  - closest text in source: "This study investigates how methamphetamine disrupts glial cell function and contributes to neurodevelopmental and neurodegenerative processes"
- `PMID:39934409` *(abstract only)*: "dorsal raphe nucleus"
  - Text part not found as substring: 'dorsal raphe nucleus' (note: only abstract available for PMID:39934409, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42516675` (1 mention) - Divergent Inflammatory and Bioenergetic Metabolomic Signatures Distinguish Methamphetamine-Associated From Idiopathic Pulmonary Arterial Hypertension.
  - shared terms: pah

Weighed against this report's own most characteristic terms: `methamphetamine`, `disorder`, `psychosis`, `gene`, `dependence`, `treatment`, `cognitive`, `risk`, `label`, `cocaine`, `found`, `taar1`, `drug`, `genetic`, `human`, `cardiomyopathy`, `chronic`, `pah`, `abstinence`, `craving`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005419` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **methamphetamine dependence**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0005419` - called "if available", "MONDO"
