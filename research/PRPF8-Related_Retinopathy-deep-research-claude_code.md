---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-25T16:35:48.201156'
end_time: '2026-10-25T16:36:52.714116'
duration_seconds: 64.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PRPF8-Related Retinopathy
  mondo_id: MONDO:0700234
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7975416000000001
  session_id: d98baee9-c229-5d8a-96f8-a4aee10f9c40
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 19
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000501
    reported_labels:
    - Attenuated retinal vessels
    ontology_label: Glaucoma
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRPF8-Related Retinopathy
- **MONDO ID:** MONDO:0700234 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRPF8-Related Retinopathy** covering all of the
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

# PRPF8-Related Retinopathy (RP13): research report

**Scope and verification.** I ran three web searches. This report relies on what they returned: the Atkinson 2024 and Arzalluz-Luque 2021 papers, the 2018 CRISPR iPSC-RPE paper, the OMIM #600059 synopsis, and the PanelApp and GenCC listings. I did not open full texts. I give PMC or URL links instead of PMIDs where I couldn't confirm the PMID. Anything marked **[unverified]** is background knowledge that this session's searches did not confirm. Run `just fetch-reference` and `just preflight-dr` before any of it goes into the KB. Most of the PRPF8 literature on penetrance, frequency, and variant spectrum (for example McKie 2001, Towns 2010, Maubaret 2011) was not retrieved. I did not look for ClinGen, Orphanet, ClinicalTrials.gov, gnomAD or ClinVar records.

## 1. Disease information

- **Overview.** PRPF8-related retinopathy is autosomal dominant retinitis pigmentosa 13 (RP13). It is non-syndromic rod-cone degeneration caused by heterozygous variants in *PRPF8*. The PRPF8 protein is a core scaffold of the U5 snRNP and spliceosome. The OMIM #600059 synopsis lists night blindness, retinal degeneration, bone-spicule pigment clumping, attenuated vessels, a pale optic disc, constricted visual fields, and in some patients subcapsular cataract and cystoid macular edema. ([OMIM #600059 mirror](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/600059), [FindZebra](https://www.findzebra.com/details/N607VV0-retinitis-pigmentosa-13))
- **Identifiers.**
  - OMIM phenotype 600059 (RP13); gene OMIM 607300; locus 17p13.3.
  - MedGen UID 325486 cross-references OMIM 600059 ([MedGen](https://https.ncbi.nlm.nih.gov/medgen/325486)).
  - MONDO:0700234 comes from the task template, not from my searches.
  - Orphanet code, ICD-10/11 and MeSH: not found. Look up the Orphanet code (likely under the "retinitis pigmentosa" ORPHA:791 family) before use.
- **Synonyms.** RP13; retinitis pigmentosa 13; PRPF8-associated retinitis pigmentosa; RP13-PRPF8; spliceosomal (PRPF-associated) retinitis pigmentosa.
- **Data source.** The OMIM and PanelApp content is aggregated disease-level information. The iPSC studies come from individual patients (H2309P).

## 2. Etiology

- **Causal factor.** Heterozygous *PRPF8* variants, clustered in the C-terminal region (exon 42; the Brr2-regulating Jab1/MPN domain region). PanelApp reports that variants typically cluster in exon 42, with variable expressivity and incomplete penetrance ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/285/gene/PRPF8/)).
- **Hotspot.** The Atkinson 2024 study states that the PRPF8 carboxy-terminus, which regulates the RNA helicase Brr2, is a hotspot for RP13 mutations ([Nat Commun 2024, PMC11009313](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11009313/)).
- **Number of mutations.** More than 20 RP-associated PRPF8 mutations have been reported in patients ([Drosophila RP13 model, DMM 2020, via search result](https://eprints.whiterose.ac.uk/id/eprint/216738/)).
- **Risk, protective and environmental factors.** None established in the sources found. Modifier alleles and gene-environment interactions are not documented, so I would record them as not available. Incomplete penetrance implies unidentified modifiers.
- **Separate association.** PanelApp lists a less established *PRPF8* association with a developmental disorder and intellectual disability, with some variants possibly non-pathogenic. This is probably a distinct entity and should not be merged into this entry.

## 3. Phenotypes

Frequencies are not quantified in the retrieved sources. HP IDs are suggestions and must be looked up before binding.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Night blindness | HP:0000662 | Onset from early childhood to the mid-thirties (OMIM). In a South African kindred, first symptoms appeared at ages 4–10 (FindZebra). |
| Rod-cone dystrophy / retinal degeneration | HP:0000510 (rod-cone dystrophy), HP:0000546 (retinal degeneration) | Severity varies from severe to near-normal retinal appearance in British families. |
| Bone-spicule pigmentation | HP:0007737 | |
| Attenuated retinal vessels | HP:0000501 | |
| Pale optic disc | HP:0000543 | |
| Constricted visual fields | HP:0001133 | |
| Cataract (subcapsular) | HP:0000518 | Present in some patients. |
| Cystoid macular edema | HP:0011505 | Present in some patients. |

- **Severity and course.** An Italian P2301S family had a milder course with partly preserved cone function ([IRIS-CNR](https://iris.cnr.it/handle/20.500.14243/37945)). Severity is variable and penetrance is incomplete.
- **Quality of life.** No data found.

## 4. Genetic and molecular information

- **Gene.** *PRPF8* (hgnc:17340 **[unverified; confirm in HGNC]**), 17p13.3.
- **Variant class.** Mostly missense or in-frame changes in the C-terminal domain, not null alleles. Examples are H2309P, which is the best-characterised, and P2301S in the Italian family.
- **Functional consequence.**
  - The mechanism is not simple haploinsufficiency.
  - In the patient iPSC model (H2309P), the authors link PRPF8/Brr2 dysregulation to impaired 5′ splice-site selection: weak or suboptimal 5′SS selection and enhanced cryptic splicing, predominantly in ciliary and retinal-specific transcripts. They also report altered spliceosome kinetics ([Atkinson 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11009313/)).
  - In Drosophila, the pathogenicity of RP-Prp8 mutations correlated with the severity of the equivalent human clinical phenotypes.
  - Whether the effect is a loss of function, a dominant negative, or a hypomorphic mechanism is not settled in the sources found.
- **Origin.** Germline.
- **Modifiers, epigenetics, chromosomal changes.** None documented.
- **Related genes.** *PRPF3*, *PRPF4*, *PRPF6*, *PRPF31* and *SNRNP200* cause similar spliceosomal RP. This is the basis for a possible grouping.
- **Population frequency and ClinVar/ClinGen classification.** Not retrieved. Check ClinVar, gnomAD and the GenCC record ([GenCC submission](https://thegencc.org/submissions/SGC-106261.2)) before assigning any `gene_disease_validity`.

## 5. Environmental information

No environmental, lifestyle or infectious factors are documented. Leave these sections absent.

## 6. Mechanism / pathophysiology

**Causal chain.** Steps marked (inferred) are not directly demonstrated in the sources.

1. A heterozygous C-terminal *PRPF8* variant (such as H2309P) alters the Brr2-regulating region of PRPF8 (demonstrated structurally and in cells).
2. This dysregulates the Brr2 helicase, which changes spliceosome kinetics and 5′ splice-site selection (Atkinson 2024).
3. The altered selection causes weak-site use and enhanced cryptic splicing. The effects are enriched in ciliary and retinal-specific transcripts, so a retina-specific splicing program is disproportionately affected (Atkinson 2024; Arzalluz-Luque 2021).
4. In patient iPSC-derived RPE, there are widespread splicing changes in spliceosome components, with global changes in splice-site selection and exon inclusion ([Frontiers Neurosci 2021, PMC8116631](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8116631/)).
5. In retinal organoids, the phenotype includes photoreceptor loss, apical-basal polarity defects and ciliary defects (Atkinson 2024).
6. Progressive rod loss followed by cone loss produces night blindness, field constriction and the fundus changes (inferred from the clinical course).
7. **Branch, RPE phagocytosis (disputed).**
   - Prpf8 H2309P/H2309P mouse RPE shows reduced phagocytosis and loss of its diurnal rhythm.
   - Patient iPSC-RPE phagocytosed outer segments at wild-type capacity and established apicobasal polarity ([PMC6321630](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6321630/)).
   - Whether RPE dysfunction contributes in humans is therefore unresolved. Record this as a `HUMAN_MODEL_MISMATCH` discussion.
8. **Open question: why the retina.** PRPF8 is ubiquitous, so the retina-restricted phenotype remains unexplained. Proposed explanations are retina-specific splicing programs and the high splicing demand of photoreceptors. These are hypotheses.

**Suggested terms (look up before binding):** GO mRNA splicing, via spliceosome (GO:0000398); U5 snRNP; cilium organization; CL rod photoreceptor cell (CL:0000604); retinal pigment epithelial cell (CL:0002586). Unlike many retinal conditions, there is no immune or metabolic arm.

## 7. Anatomical structures affected

- **Organ and tissue.** Retina (UBERON:0000966) in both eyes, mainly the rod photoreceptor layer and the RPE. The lens is secondarily affected (cataract).
- **Subcellular.** The nucleus and spliceosome (U5 snRNP); the photoreceptor connecting cilium.
- **Laterality.** Bilateral.

## 8. Temporal development

- **Onset.** Childhood to the mid-thirties, which is variable. The age of onset in the South African kindred was 4–10 years.
- **Progression.** Progressive rod-cone degeneration with a variable rate. Some carriers remain nearly normal because of incomplete penetrance.
- **Duration.** Lifelong. No remission is described.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant (HP:0000006), with incomplete penetrance and variable expressivity (OMIM; two British families showed marked intrafamilial variability).
- **Prevalence.** Not found. Do not enter a rate. The broader RP prevalence is roughly 1 in 4,000 **[unverified]**. *PRPF8* accounts for only a small share of adRP **[unverified]**.
- **Founder effects, sex ratio, anticipation, mosaicism.** Not documented here. Family reports come from South Africa, the UK and Italy.

## 10. Diagnostics

- **Clinical.** Fundus examination, visual field testing, full-field ERG (rod-dominant reduction), OCT (ellipsoid-zone loss, macular edema) and autofluorescence.
- **Genetic.** An inherited retinal disease gene panel or exome sequencing that includes *PRPF8* exon 42. Check that the panel covers the C-terminal exons. Interpret VUS cautiously, since PanelApp notes some variants may not be pathogenic.
- **Differential.** Other adRP genes, especially the other spliceosomal genes (*PRPF31*, *PRPF3*, *SNRNP200*, *PRPF6*, *PRPF4*) and rhodopsin (*RHO*) RP.
- **GeneReviews.** Not checked. Run `just check-genereviews` for this entry.

## 11. Outcome and prognosis

Not quantified in the retrieved sources. Expect gradual loss of peripheral vision and, in severe families, eventual loss of central vision. Complications are cataract and cystoid macular edema. Severity within families is variable, so prognosis is hard to predict from genotype alone.

## 12. Treatment

- **Approved disease-modifying therapy.** None found for *PRPF8*. The approved voretigene therapy targets *RPE65* and does not apply here.
- **Supportive.** Low-vision rehabilitation (NCIT:C15315 Rehabilitation), cataract surgery (NCIT:C15329 Surgical Procedure) and treatment of macular edema with carbonic anhydrase inhibitors **[unverified]**. Genetic counseling is NCIT:C15240.
- **Experimental.** In the mechanistic literature, the main therapeutic lead is gene-supplementation or splicing-correction approaches. A thesis reported PRPF31 supplementation rescuing phagocytosis in PRPF31-linked cells, but that is a different gene. No PRPF8 trial was found, and I did not search ClinicalTrials.gov.

## 13. Prevention

- Genetic counseling and cascade testing of relatives.
- Prenatal or preimplantation testing are options for known familial variants.
- Incomplete penetrance complicates risk estimates for asymptomatic carriers.
- No behavioral, environmental or immunization strategies apply.

## 14. Other species and natural disease

No naturally occurring *PRPF8* retinopathy in animals was found. I did not check OMIA. The Drosophila ortholog is *Prp8*.

## 15. Model organisms

- **Mouse.** Prpf8 H2309P knock-in (homozygous). RPE shows reduced phagocytosis and loss of its diurnal rhythm. I did not retrieve the retinal phenotype. Heterozygous mice, which are the closer genetic match, were not covered. (From the search summary of the iPSC-RPE paper.)
- **Drosophila.** RP-Prp8 mutations modeled in flies; the severity of the fly phenotype correlates with the human clinical severity (DMM 2020, [Whiterose eprint](https://eprints.whiterose.ac.uk/id/eprint/216738/)). This supports a `PARTIALLY_RECAPITULATES` or `RECAPITULATES` link with `fidelity: MODERATE`.
- **Human iPSC models.**
  - Patient iPSC-derived RPE (p.H2309P) with CRISPR-corrected isogenic clones ([PMC6321630](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6321630/)). It shows normal phagocytosis and polarity.
  - iPSC-derived RPE showing widespread splicing changes ([PMC8116631](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8116631/)).
  - Retinal organoids showing photoreceptor loss, polarity defects and ciliary defects ([PMC11009313](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11009313/)).
- **Limitations.** The mouse and iPSC-RPE phagocytosis findings conflict. Overlapping cell lines may make the iPSC papers non-independent. Organoids lack the full RPE and photoreceptor interface.

## Curation notes for dismech

1. Use `inheritance_term` HP:0000006 (autosomal dominant) with the incomplete penetrance and variable expressivity noted in the description.
2. Do not set a `gene_disease_validity` tier without a ClinGen or GenCC record. The GenCC submission SGC-106261.2 is a lead only; open it and read the classification.
3. Every PMID must be fetched with `just fetch-reference` and quoted exactly. This report contains no verified snippets.
4. Open `HUMAN_MODEL_MISMATCH` for the RPE phagocytosis conflict and `KNOWLEDGE_GAP` for the retina-specificity question.
5. Consider a covering `Grouping` for spliceosomal (PRPF-associated) RP.

## Sources

- [Atkinson et al., Nat Commun 2024 (PMC11009313)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11009313/)
- [Arzalluz-Luque et al., Front Neurosci 2021 (PMC8116631)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8116631/)
- [Functional assessment of patient-derived RPE edited by CRISPR/Cas9 (PMC6321630)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6321630/)
- [Drosophila RP13 model (Whiterose eprint)](https://eprints.whiterose.ac.uk/id/eprint/216738/)
- [OMIM #600059 mirror](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/600059)
- [FindZebra RP13](https://www.findzebra.com/details/N607VV0-retinitis-pigmentosa-13)
- [Genomics England PanelApp, PRPF8](https://panelapp.genomicsengland.co.uk/panels/285/gene/PRPF8/)
- [GenCC submission SGC-106261.2](https://thegencc.org/submissions/SGC-106261.2)
- [IRIS-CNR, Italian P2301S family](https://iris.cnr.it/handle/20.500.14243/37945)
- [MedGen 325486](https://https.ncbi.nlm.nih.gov/medgen/325486)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000501` (1 mention) - the report calls it "Attenuated retinal vessels"; HP calls it **Glaucoma**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007737` (1 mention) - the report calls it "Bone-spicule pigmentation"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone spicule pigmentation of the retina" among its other names
- `HP:0000543` (1 mention) - the report calls it "Pale optic disc"; HP calls it **Optic disc pallor**, and lists "Pale optic discs" among its other names
- `HP:0000518` (1 mention) - the report calls it "Cataract (subcapsular)"; HP calls it **Cataract**, and lists "Cataracts" among its other names
- `HP:0000006` (2 mentions) - the report calls it "autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.