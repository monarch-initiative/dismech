---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-26T20:24:10.823119'
end_time: '2026-10-26T20:25:35.190331'
duration_seconds: 84.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: GRHL3-related Orofacial Clefting
  mondo_id: MONDO:0100579
  category: Mendelian
  causal_genes: GRHL3
  omim_id: not recorded
  synonyms: Van der Woude syndrome 2; GRHL3-related cleft palate; VWS2
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
  num_turns: 8
  total_cost_usd: 0.7675020999999999
  session_id: 402da01d-554f-59a0-9730-4f6c8133551c
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 1
citation_count: 12
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 5
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GRHL3-related Orofacial Clefting
- **MONDO ID:** MONDO:0100579 (if available)
- **Causal gene(s):** GRHL3
- **OMIM:** not recorded
- **Synonyms:** Van der Woude syndrome 2; GRHL3-related cleft palate; VWS2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **GRHL3-related Orofacial Clefting** covering all of the
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

# GRHL3-related Orofacial Clefting (Van der Woude syndrome 2, VWS2): research report

**Method and limits.** I could not use PubMed. The PubMed tools were permission-denied in this session. The report rests on three web searches whose results included PubMed, PMC, ZFIN, eScholarship and Dundee records. The searches returned abstract-level text, not full texts.

- **Verified:** claims with a source named in the sentence.
- **Model inference:** marked as such, and not sourced.
- **Not checked:** I did not look up the MONDO ID, OMIM disease number, Orphanet, HPO or GO identifiers, ClinGen or ClinVar. Treat any identifier below as a lead until it is checked.
- **Quotes:** quotation marks are used only for text that appeared verbatim in the search output. That text may itself be a tool's rendering of the abstract, so re-check it against the abstract before using it as an evidence `snippet`.

## 1. Disease information

The causal gene is **GRHL3** (grainyhead-like transcription factor 3, chromosome 1p36). The disease is an autosomal dominant orofacial clefting disorder. It ranges from classic Van der Woude syndrome (VWS2: lip pits plus cleft lip and/or palate) to isolated cleft palate.

- **Source for the gene–disease link.** Peyrard-Janvid et al. 2014 (Am J Hum Genet 94:23–32; PMID 24360809, from the PubMed URL in the search results; [PubMed](https://pubmed.ncbi.nlm.nih.gov/24360809/), [PMC3882735](https://pmc.ncbi.nlm.nih.gov/articles/PMC3882735/)) reports: "In 8 of 45 VWS-affected families lacking a mutation in IRF6, we found coding mutations in grainyhead-like 3 (GRHL3)." Source class: primary literature, human clinical.
- **OMIM.** Per the search summary, OMIM states that "van der Woude syndrome-2 (VWS2) is caused by heterozygous mutation in the GRHL3 gene (608317) on chromosome 1p36." I did not retrieve the OMIM disease number (my recollection is 606713, unverified), so I have not recorded it. The OMIM text reached me through a search-engine summary, so quote it only after reading the OMIM entry itself.
- **Lump/split question.** The brief gives the MONDO ID as "if available". I did not verify MONDO:0100579. Two points for the curator:
  - VWS2 is a gene-specific subtype of Van der Woude syndrome (the IRF6 form is VWS1). Should the entry be a `SUBTYPE` of a VWS parent or a standalone disease?
  - The same gene also gives non-syndromic cleft palate. That phenotype is part of the entry's spectrum, so the name "GRHL3-related Orofacial Clefting" fits it better than "VWS2".
- **Synonyms (from the brief):** Van der Woude syndrome 2; GRHL3-related cleft palate; VWS2.
- **Data source.** This report uses aggregated, published disease-level data. No individual-patient or EHR data were used.

## 2. Etiology

- **Primary cause.** Heterozygous coding variants in GRHL3 (Peyrard-Janvid 2014, PMID 24360809).
- **Dominant-negative suggestion.** In the same study, "the disease-associated GRHL3 mutations abrogated periderm development and were consistent with a dominant-negative effect", unlike the haploinsufficiency seen in most IRF6 VWS. The finding comes from a zebrafish assay, so it is model-organism evidence for a mechanism in humans. I did not retrieve the variant list. That list matters because it determines the mix of missense and truncating variants, so check it in the full text.
- **Truncating variants and loss of function.**
  - Eshete et al. 2018 sequenced GRHL3 exons in "a total of 134 nonsyndromic cases" from African cohorts (J Dent Res; [DOI 10.1177/0022034517729819](https://doi.org/10.1177/0022034517729819)). Variant: "4 variants were functionally null or hypomorphic, while 1 was dominant negative".
  - Those cases had isolated cleft palate (title: "Loss-of-Function GRHL3 Variants Detected in African Patients with Isolated Cleft Palate"). So both loss-of-function and dominant-negative mechanisms are reported. Mechanism is therefore not settled.
  - A separate GRHL3 coding-region sequencing study reported "rare truncating mutations and a common susceptibility variant for nonsyndromic cleft palate" ([ResearchGate title record](https://www.researchgate.net/publication/299416545_Sequencing_the_GRHL3_Coding_Region_Reveals_Rare_Truncating_Mutations_and_a_Common_Susceptibility_Variant_for_Nonsyndromic_Cleft_Palate)). I did not get authors or a PMID, and I did not confirm the first author I had in mind, so I have not attributed it.
- **Common susceptibility variant.** A GWAS of non-syndromic cleft palate "identifies an etiologic missense variant in GRHL3", reported as rs41268753 and replicated independently ([ScienceDirect, AJHG 2016](https://www.sciencedirect.com/science/article/pii/S0002929716000653)). I did not confirm authors or PMID.
- **Non-replication in another population.** A Han Chinese study reported no association of two GRHL3 SNPs (rs2486668, rs545809) with non-syndromic orofacial clefts ([PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0159940)). Note that these are different SNPs from the GWAS missense variant, so this is not a direct failure to replicate it.
- **Modifier genes.** Mouse double heterozygotes (Irf6+/−; Grhl3+/−) showed "no epistasis… suggesting that they function in separate but convergent pathways" (search-summarised quote from the mouse literature; I did not identify the paper).
- **Environmental risk factors, protective factors, gene–environment interaction.** I found no GRHL3-specific data. Do not extrapolate from general orofacial cleft risk factors such as maternal smoking, folate and anticonvulsants. Record these as a gap.

## 3. Phenotypes

I found no frequency tables in the sources I reached. The items below are from the clinical definition and abstracts. I have not assigned frequencies.

| Phenotype | HPO term (to verify, I did not look it up) | Source |
|---|---|---|
| Cleft palate | HP:0000175 | Peyrard-Janvid 2014; Eshete 2018 |
| Cleft lip (with or without cleft palate) | HP:0000204 / HP:0410030 | Peyrard-Janvid 2014 (VWS phenotype; subtype split not retrieved) |
| Lower lip pits | HP:0000196 | Defining VWS feature; not quoted from the sources I reached |

- **Onset.** Congenital for the cleft. This follows from the structural nature of the lesion and is not a quoted source claim.
- **Pediatric framing (model inference, not sourced).** Care is shaped by surgical repair in infancy, speech and feeding, and ear and dental management. The sources I reached do not cover this for GRHL3 specifically.
- **Quality of life.** No GRHL3-specific data found.

## 4. Genetic and molecular information

- **Gene.** GRHL3, HGNC lowercase form `hgnc:` in this KB. I did not look up the HGNC ID. Do not write it from memory.
- **Variant spectrum.**
  - VWS2 families: coding mutations (Peyrard-Janvid 2014).
  - Isolated cleft palate, African cohorts: null, hypomorphic and dominant-negative variants (Eshete 2018).
  - Isolated cleft palate, European ancestry: the common missense variant rs41268753 as a susceptibility allele.
- **Origin.** Germline.
- **Classification and allele frequency.** Not retrieved (ClinVar, ClinGen, gnomAD). ClinGen validity for the GRHL3–orofacial cleft pair was not checked. If the curator cites ClinGen, it must be a `CGGV:` record.
- **Epigenetic and chromosomal.** Nothing found. Note that 1p36 deletions include GRHL3. I did not check cleft phenotypes in that deletion syndrome, so it is not claimed here.

## 5. Environmental information

No GRHL3-specific environmental, lifestyle or infectious data found. Gap.

## 6. Mechanism and pathophysiology

**Causal chain.** Steps 1–3 are sourced. Step 4 is partly inferred.

1. A heterozygous GRHL3 variant alters the transcription factor. For some alleles this is dominant-negative (zebrafish assay, Peyrard-Janvid 2014); for others loss of function (Eshete 2018).
2. This reduces **oral periderm** development in the embryo. Periderm is the superficial epithelial layer on the palatal shelves. Source: Peyrard-Janvid 2014, where "the disease-associated GRHL3 mutations abrogated periderm development".
3. Failure of periderm function leads to abnormal epithelial behaviour in the oral cavity. In mouse, "all embryos lacking Grhl3 exhibited abnormal oral periderm and 17% developed a cleft palate." Grhl3−/− embryos at E15.5 had "bilateral oral epithelial adhesions" (mouse literature, summarised by search; paper not identified).
4. *Inferred, not demonstrated here:* abnormal adhesion or failed fusion of palatal shelves then yields cleft palate. The 17% cleft penetrance in mouse suggests incomplete penetrance in that model, a point the curator should check against the primary paper.

**Branch: the IRF6 axis.** "In Irf6 deficient mouse embryos, Grhl3 expression in the periderm and oral epithelium is virtually absent. These results indicate that Grhl3 is a key effector of Irf6 in periderm differentiation." (Search-summarised quote; source paper not identified.) The double-heterozygote cross showed no epistasis, so the pathways are described as separate but convergent. One review notes that extensive oral epithelial adhesions are a feature of Irf6 mutants but "not reported in the Grhl3 mutant".

**Other points.**
- **Suggested terms (to be verified before binding):** cell type, periderm or oral epithelial cell (CL: not looked up); process, epithelial cell differentiation and palate development (GO: not looked up).
- **Other omics, proteomics, metabolomics:** nothing found.
- **Conflict worth flagging.** The brief frames this as a clefting disorder. The same gene is also associated with a neural tube phenotype in mouse. I did not find that literature in this session, so I make no claim about it.

## 7. Anatomical structures affected

- Primary site: palate and lip, with the oral periderm as the likely cellular site. Source for periderm: Peyrard-Janvid 2014. Lateralization was not retrieved.
- Skin: Grhl3 mutant mice show a skin phenotype per the review comparison with Irf6. I did not retrieve human skin findings.
- UBERON and CL terms were not looked up.

## 8. Temporal development

- Congenital. The critical period is embryonic palatal fusion (a mouse stage of E15.5 was noted in the source above). Human gestational timing was not retrieved.
- Disease course: structural, non-progressive (model inference, not sourced).

## 9. Inheritance and population

- Autosomal dominant (OMIM statement, as above).
- Penetrance: not quantified in the sources I reached. The 17% cleft palate rate in Grhl3-null mouse is not a human penetrance estimate.
- Populations: the Eshete 2018 cohorts are African (Nigeria, Ghana, Ethiopia, per the author list). The GWAS signal was in European ancestry cases. The Han Chinese study was negative for two other SNPs.
- Prevalence and incidence of GRHL3-specific disease: not found. Orphanet was not checked.
- Founder effects, anticipation, mosaicism, consanguinity, carrier frequency: no data found.

## 10. Diagnostics

I found nothing on this beyond the genetic basis. Reasonable lines to check against GeneReviews (not retrieved): clinical diagnosis of VWS by lip pits and clefting, then IRF6 testing first, then GRHL3 testing. The Peyrard-Janvid 2014 result supports that sequence, since GRHL3 variants were found in families without an IRF6 mutation. The testing approach itself is my inference from this.

## 11. Outcome and prognosis

No GRHL3-specific data found.

## 12. Treatment

No GRHL3-specific data found. Standard multidisciplinary cleft care (surgical repair, speech, hearing and dental care) would apply. This is general knowledge, not sourced from this search. NCIT terms were not looked up.

## 13. Prevention

Genetic counseling for an autosomal dominant condition applies (inference). No GRHL3-specific prevention data found.

## 14. Other species and natural disease

I did not search OMIA. Not claimed.

## 15. Model organisms

| Model | Finding | Source |
|---|---|---|
| Mouse, Grhl3 null | Abnormal oral periderm in all embryos; 17% cleft palate; bilateral oral epithelial adhesions at E15.5 | Mouse literature as summarised by search; paper not identified. Peyrard-Janvid 2014 reports the 17% figure |
| Mouse, Irf6+/−; Grhl3+/− | No epistasis | Search-summarised quote above |
| Zebrafish | Periderm development assay for GRHL3 variants; used to infer dominant-negative effect | Peyrard-Janvid 2014 ([ZFIN publication record](https://www.zfin.org/ZDB-PUB-140220-21)) |

- **Fidelity and limitations.** Mouse cleft penetrance (17%) is lower than the human VWS phenotype. Mouse and zebrafish evidence should not be the sole support for human phenotypes. Keep `evidence_source: MODEL_ORGANISM` for these.
- **Expected `HUMAN_MODEL_MISMATCH` question.** The mouse null phenotype is milder than the human dominant disease. That fits a dominant-negative mechanism in humans but is not demonstrated here.

## Gaps and cautions for the curator

1. **PMIDs.** Only one is confirmed from a URL: 24360809. All other citations above lack verified PMIDs; run `just fetch-reference` after looking them up.
2. **Not verified:** MONDO:0100579, the OMIM disease number, Orphanet, HPO, GO, CL and UBERON identifiers, the HGNC ID, ClinGen, ClinVar and gnomAD.
3. **Unsourced material.** No frequencies, no environmental data, no prognosis, no treatment-outcome data, no veterinary data.
4. **Two quote provenance caveats.** The Irf6/Grhl3 quotes and the 17% figure came through search summaries. The primary paper behind them is unidentified except for the 17% figure, which also appears in the Peyrard-Janvid abstract.

## Sources

- [Peyrard-Janvid et al. 2014, PubMed 24360809](https://pubmed.ncbi.nlm.nih.gov/24360809/)
- [Peyrard-Janvid et al. 2014, PMC3882735](https://pmc.ncbi.nlm.nih.gov/articles/PMC3882735/)
- [ZFIN record for the same paper](https://www.zfin.org/ZDB-PUB-140220-21)
- [Eshete et al. 2018, DOI](https://doi.org/10.1177/0022034517729819)
- [Dundee record for Eshete et al.](https://discovery.dundee.ac.uk/en/publications/loss-of-function-grhl3-variants-detected-in-african-patients-with/)
- [GWAS of non-syndromic cleft palate, AJHG 2016](https://www.sciencedirect.com/science/article/pii/S0002929716000653)
- [GRHL3 coding-region sequencing, title record](https://www.researchgate.net/publication/299416545_Sequencing_the_GRHL3_Coding_Region_Reveals_Rare_Truncating_Mutations_and_a_Common_Susceptibility_Variant_for_Nonsyndromic_Cleft_Palate)
- [Han Chinese GRHL3 SNP study, PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0159940)
- [eScholarship record](https://escholarship.org/uc/item/45g0p0vb), [PMC5552062](https://pmc.ncbi.nlm.nih.gov/articles/PMC5552062), [PMC3541433](https://pmc.ncbi.nlm.nih.gov/articles/PMC3541433), [PMC4743694](https://pmc.ncbi.nlm.nih.gov/articles/PMC4743694): returned by the mouse search, which gave me only the summaries above and did not give me their authors or titles.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000196` (1 mention) - the report calls it "Lower lip pits"; HP calls it **Lower lip pit**

Every term resolved, and every label the report gave matched.