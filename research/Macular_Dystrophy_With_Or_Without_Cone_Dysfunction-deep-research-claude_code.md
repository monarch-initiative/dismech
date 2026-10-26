---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-24T15:43:48.274949'
end_time: '2026-10-24T15:45:23.414898'
duration_seconds: 95.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Macular Dystrophy with or without Cone Dysfunction
  mondo_id: MONDO:0958326
  category: Mendelian
  causal_genes: SAMD7
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 0.8306493
  session_id: 854e4ee6-1dd8-597a-ba53-1d9e860afb7a
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 5
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 7
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Macular Dystrophy with or without Cone Dysfunction
- **MONDO ID:** MONDO:0958326 (if available)
- **Causal gene(s):** SAMD7
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Macular Dystrophy with or without Cone Dysfunction** covering all of the
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

I'll load the search tools first, then run the searches.

I have the key AJHG paper and the PNAS mouse paper. Next I'm pulling the PNAS abstract and the PanelApp and ClinVar details to complete the report.

# SAMD7-related autosomal recessive macular dystrophy with or without cone dysfunction

**Disease:** Macular dystrophy with or without cone dysfunction (MONDO:0958326, as supplied in the request). **Causal gene:** SAMD7 (sterile alpha motif domain containing 7; HGNC ID not looked up in this session).

**Provenance and gaps.**
- Sources used: one primary clinical paper (PMID 38272031), one primary mouse and zebrafish paper (PMID 39531499), one mouse expression paper from memory of search output (PMID unknown), and one structured database (Genomics England PanelApp).
- Full text could not be read. PMC returned a CAPTCHA page, and Europe PMC returned only truncated abstract-level text. Everything below on the clinical series comes from abstract-level summaries and the PanelApp review, not the full paper.
- I could not verify the MONDO:0958326 identifier. No search result returned that term. PanelApp lists OMIM:620762 for the phenotype and an earlier, now-replaced MONDO:0031166 (macular dystrophy, retinal). Treat the MONDO ID as supplied, not confirmed.
- Pediatric framing: the published series is adult-onset (mean age at first presentation about 35 years, range 14–51). Nothing I found describes a childhood presentation.
- Numbers I could not verify from a source are marked "not retrieved". I have not filled them in from memory.

## 1. Disease information

SAMD7-related disease is an autosomal recessive retinal disorder. It is characterized by macular dystrophy, with or without generalized cone dysfunction.

- **Primary report:** Bauwens M et al., *Am J Hum Genet* 2024, "Mutations in SAMD7 cause autosomal-recessive macular dystrophy with or without cone dysfunction" (PMID:38272031; source class: primary literature, abstract-level via Europe PMC).
- **Identifiers found:**
  - OMIM:620762 (phenotype entry), per PanelApp.
  - MONDO:0031166 (macular dystrophy, retinal), the earlier PanelApp phenotype.
  - HP:0030637 (congenital stationary cone dysfunction), also an earlier PanelApp entry, since replaced.
- **Not found:** Orphanet, ICD-10/11 and MeSH identifiers. Synonyms are not recorded.
- **Data source:** The data are patient-level, from clinical cohorts (the AJHG families plus three Genomics England cases), not an aggregated disease resource.

## 2. Etiology

- **Cause:** Biallelic (homozygous in the reported families) SAMD7 variants.
- **Variants:** Five variants in six unrelated families of varied ethnic backgrounds (PanelApp review of PMID:38272031). The abstract-level summary says four variants affect splicing and one is a missense variant. The missense variant alters SAMD7's repression of CRX-dependent promoter activity in vitro.
- **Environmental, protective and gene–environment factors:** None reported in what I retrieved.
- **Modifier genes:** None identified in the retrieved sources.

## 3. Phenotypes

Data below are from the PanelApp review of PMID:38272031 and the abstract-level summary.

| Phenotype | Suggested HPO | Frequency / notes |
|---|---|---|
| Macular dystrophy / macular atrophy involving the fovea | Macular dystrophy (term ID not looked up) | All affected individuals in the series |
| Reduced visual acuity | Reduced visual acuity (term ID not looked up) | MedGen describes it as the core feature (via a search summary) |
| Generalized cone dysfunction, mild | Cone dysfunction / HP:0030637 (congenital stationary cone dysfunction, an earlier PanelApp phenotype) | 4 of 6 families (cone dysfunction) vs 2 of 6 (without) |

- **Onset:** Mean age at first presentation was 34.8 years (range 14–51), per a curation summary in the search results. I did not see this figure in a primary text.
- **Progression:** MedGen describes the condition as progressive. I did not verify this against the paper.
- **Cohort size:** Eight individuals from six families in the paper. PanelApp notes three additional cases in the Genomics England Clinical Variant Archive.
- **Quality-of-life data:** Not retrieved.
- **Exact phenotype frequencies and HPO term IDs:** Not retrieved. These need the full text or a HPO lookup.

## 4. Genetic and molecular information

- **Gene:** SAMD7 (HGNC and OMIM gene IDs not looked up). The variant list is not retrieved at nucleotide or protein level.
- **Mechanism class:** Four of the five variants affect splicing, so loss of function is plausible. PanelApp records "mode of pathogenicity: Other". I am inferring loss of function for the splice variants; the abstract-level text does not state it.
- **Missense variant:** Alters the repressive effect on CRX-dependent promoter activity in vitro (PMID:38272031).
- **Origin:** Germline (inferred from recessive inheritance in families).
- **Validity:** PanelApp Green (high evidence) for the retinal disorders panel, rating set Feb 2024 and raised from Amber to Green on 26 September 2024. Penetrance is listed as unknown.
- **Not found:** A ClinGen validity assertion (no CGGV record located), gnomAD frequencies, and epigenetic or chromosomal data.
- **ClinVar:** A ClinVar record (RCV003985688) appeared in search results, but I did not open it.

## 5. Environmental information

None found.

## 6. Mechanism / pathophysiology

Ordered chain. The links marked "inferred" are my reading of the sources, not demonstrated causation.

1. **Biallelic SAMD7 variants** (mostly splice-disrupting) reduce or alter SAMD7 function. Splicing effects are reported in the abstract-level summary. The loss-of-function link is inferred.
2. **SAMD7 is a CRX-regulated transcriptional repressor.** It is a component of Polycomb repressive complex 1 (per the AJHG abstract summary). In the 2013 PLOS ONE study, Samd7 dampened CRX-driven transcription and its own transcription depended on conserved CRX motifs (PMC3615016; year and findings from a search summary, not read directly).
3. **Loss of repression leads to derepression of CRX-dependent genes** in photoreceptors. This is inferred from the repressor function and the missense assay. It has not been shown in human retina.
4. **Photoreceptor dysfunction** follows (inferred), including cone dysfunction in some patients and macular degeneration.
5. **Clinical result:** Macular atrophy and reduced acuity, with or without generalized cone dysfunction.

**Localization.** Immunostaining showed SAMD7 in the nuclei of rods, cones and inner nuclear layer cells in human retina (AJHG abstract summary). PanelApp's review says SAMD7 localizes to the inner and outer nuclear layers.

**Why the macula is selectively affected:** Not explained in anything I retrieved. This is an open question.

**Suggested ontology terms** (not looked up, so treat as leads): GO negative regulation of transcription by RNA polymerase II; CL rod photoreceptor cell, cone photoreceptor cell; UBERON macula lutea, retina.

**Omics, single-cell, and CRISPR screens:** None found.

## 7. Anatomical structures affected

- **Primary:** Retina, specifically macula/fovea, plus cone and rod photoreceptors.
- **Secondary:** None reported.
- **Subcellular:** Nucleus.
- **Lateralization:** Not retrieved. Presumed bilateral, which I am inferring, not citing.

## 8. Temporal development

- Presentation was in adulthood, mean about 35 years (range 14–51).
- Course is described as progressive by MedGen (via a search summary).
- Staging, remission and critical periods: not retrieved.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (PanelApp: BIALLELIC).
- **Ancestry:** Six families "of varied ethnic backgrounds" (PanelApp review). I found no founder effect, consanguinity data, prevalence, incidence, carrier frequency, or sex ratio.
- **Reduced penetrance or expressivity:** Cone involvement varied between families (4 of 6 with, 2 of 6 without). Whether this reflects variant or modifier effects is unknown.

## 10. Diagnostics

- **Genetic testing:** SAMD7 is on the Genomics England retinal disorders panel (Green). I did not find which commercial gene panels include it.
- **Differential:** Stargardt disease and other macular dystrophies. The Australian PanelApp panel "Macular Dystrophy/Stargardt Disease" also lists SAMD7.
- **Electrophysiology and imaging findings, criteria, screening:** Not retrieved from primary text. Cone dysfunction would be assessed by electroretinography, but this is general knowledge, not cited.

## 11. Outcome / prognosis

Not retrieved. No survival, visual outcome, or complication data. Visual prognosis is expected to be limited by macular atrophy (inference).

## 12. Treatment

- No disease-specific therapy found.
- No gene therapy or clinical trial identified (no NCT searched in this session).
- Management would be supportive, such as low-vision rehabilitation, which is general practice and not cited.
- NCIT suggestions (leads, IDs unverified): supportive care (NCIT:C15747 from the repository documentation), genetic counseling (NCIT:C15240).

## 13. Prevention

Genetic counseling for an autosomal recessive condition (general principle, not cited here). No screening program found.

## 14. Other species

- **Mouse:** *Samd7* is a CRX-regulated repressor. A search summary says *Samd7*-null mice show rod dysfunction and ectopic expression of non-rod genes (for example S-opsin) in rods. I could not locate the primary paper for this claim, so treat it as a lead.
- **Mouse and zebrafish, PMID:39531499** (Volkov LI et al., *PNAS* 2024;121(47):e2402121121, DOI 10.1073/pnas.2402121121):
  - Zebrafish: Samd7 promotes rod differentiation and represses short-wavelength cone genes in long-wavelength cones.
  - In knockout zebrafish retinas, "red cones are transformed into hybrid red/ultraviolet (UV) cones". Green cones are absent, blue cones are roughly doubled and rods are greatly reduced.
  - Mouse: Samd7 represses S-opsin in dorsal M-cones.
- **Human–mouse difference:** The AJHG authors report that SAMD7's role differs between human and mouse retina (abstract-level summary). A review noted that no retinal phenotype exclusively linked to SAMD7 deficiency had been reported in humans before 2024.
- **Taxon and gene IDs, OMIA, breeds:** Not looked up.

## 15. Model organisms

- **Models:** Mouse (*Samd7* knockout) and zebrafish (*samd7* knockout) per above. A *Samd7/Samd11* double knockout has shortened outer segments and more upregulated retinal genes than *Samd7* alone, suggesting partial redundancy (search summary, primary source not identified).
- **Fidelity:** Moderate to low for the human macular phenotype. Rodents lack a macula, and the AJHG authors note species differences. The zebrafish cone-subtype transformation does not map directly onto human macular atrophy.
- **Evidence source class:** MODEL_ORGANISM for all of the above.
- **Gaps:** No human iPSC or organoid data found. MGI, ZFIN and IMPC phenotype pages were not checked.

## Suggested curation notes

- **Lump/split:** This looks like a single Mendelian entry with one gene. The "with or without cone dysfunction" wording is part of the OMIM name, so a subtype split is not supported unless the full text shows a genotype split.
- **Items to verify before curation:**
  - MONDO:0958326 against the entry's `disease_term`.
  - HGNC ID for SAMD7.
  - Exact variants and HPO frequencies from the full text of PMID:38272031.
  - Whether a ClinGen validity record exists.

## Sources

- [Bauwens et al. 2024, AJHG (PMID:38272031), via Europe PMC search results](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SAMD7%20AND%20(macular%20OR%20retina)&format=json&pageSize=15&resultType=core)
- [PMC10870129 (AJHG full text; not readable here)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10870129)
- [Volkov et al. 2024, PNAS (PMID:39531499)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:39531499%20AND%20SRC:MED&format=json&resultType=core)
- [Genomics England PanelApp, SAMD7](https://panelapp.genomicsengland.co.uk/panels/307/gene/SAMD7)
- [Samd7 is a Crx-regulated repressor, PLOS ONE (PMC3615016; read only through search summaries)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3615016/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030637` (2 mentions) - the report calls it "congenital stationary cone dysfunction", "congenital stationary cone dysfunction, an earlier PanelApp phenotype"; HP calls it **Congenital stationary cone dysfunction**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0030637` - called "congenital stationary cone dysfunction", "congenital stationary cone dysfunction, an earlier PanelApp phenotype"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `EXT_ID`.

5 of 7 terms resolved to a current term; the rest could not be looked up either way.