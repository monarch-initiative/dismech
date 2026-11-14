---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-11-11T15:19:56.788263'
end_time: '2026-11-11T15:34:55.719327'
duration_seconds: 898.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Mesoblastic Nephroma
  mondo_id: MONDO:0017043
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: CMN; stromal nephroma, malignant
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
  web_search_requests: 17
  num_turns: 81
  total_cost_usd: 8.834759
  session_id: e52ae353-c5e9-4161-a81e-3cbd7e35a292
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 25
reference_validation:
  total_references: 68
  verified: 68
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 35
  quotes_valid: 33
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:36010301
  - PMID:42189790
  relevance_assessed: 68
  on_topic: 23
  off_topic: 1
  off_topic_references:
  - DOI:10.1158/2159-8290.CD-15-0654
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 97
  verified: 95
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 4
  labels_variant: 4
  obsolete_terms:
  - term_id: NCIT:C16722
    ontology_label: Immunohistochemistry
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Mesoblastic Nephroma
- **MONDO ID:** MONDO:0017043 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** CMN; stromal nephroma, malignant
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Mesoblastic Nephroma** covering all of the
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

# Congenital Mesoblastic Nephroma (MONDO:0017043) — Comprehensive Disease Research Report

*Prepared 11 November 2026. Evidence tiers are marked throughout: **[VERIFIED]** = quoted verbatim from a primary abstract/full text read during this review; **[SECONDARY]** = taken from a review, database entry, or search summary and not independently confirmed against the primary source; **[LEAD]** = a claim worth pursuing but whose primary source was not read.*

---

## 0. Executive Summary and the Causal-Gene Question

**Congenital mesoblastic nephroma (CMN) has no germline causal gene.** It is a **somatically driven**, mesenchymal/myofibroblastic renal neoplasm of fetal and early infant life, and its drivers are acquired kinase lesions that segregate by histological subtype:

| Driver | HGNC | Subtype association | Lesion class |
|---|---|---|---|
| **EGFR** internal tandem duplication (ITD) / kinase domain duplication (KDD) of exons 18–25 | `hgnc:3236` | **Classic** and **mixed** CMN | Somatic intragenic tandem duplication |
| **ETV6::NTRK3** fusion from t(12;15)(p13;q25) | `hgnc:3495` / `hgnc:8033` | **Cellular** (and some mixed) CMN | Somatic reciprocal translocation |
| **BRAF** intragenic rearrangement / **KLHL7::BRAF** fusion | `hgnc:1097` | Rare cellular CMN | Somatic intragenic rearrangement / fusion |
| **NTRK1** fusions (**TPM3::NTRK1**, LMNA::NTRK1) | `hgnc:8031` / `hgnc:12012` / `hgnc:6636` | Rare, reported in aggressive cellular CMN | Somatic fusion |
| **EML4::NTRK3**, **EML4::ALK** | `hgnc:1316` / `hgnc:427` | Rare variants | Somatic fusion |

The disease identifier given in the task (`MONDO:0017043`) was confirmed against this repository's committed MONDO term cache as **`MONDO:0017043` "congenital mesoblastic nephroma"** — the correct anchor for this entry. There is **no OMIM phenotype entry** for CMN, consistent with its purely somatic origin; the relevant OMIM records are gene records (EGFR, ETV6, NTRK3, BRAF), not disease records.

The unifying mechanism is **constitutive, ligand-independent receptor tyrosine kinase activation feeding the RAS–MAPK (and, for NTRK fusions, PI3K–AKT) cascade in a renal/perirenal mesenchymal progenitor**, producing a spindle-cell myofibroblastic proliferation that is locally expansile and, in the cellular subtype, capable of metastasis.

---

## 1. Disease Information

### 1.1 Overview

CMN is the most common renal neoplasm of the neonate and young infant. The largest contemporary cohort states it plainly:

> "Congenital mesoblastic nephroma (CMN) is the most common renal neoplasm diagnosed in the very first months of life. Complete nephrectomy only is the gold standard treatment."
> — Quarello et al., *PLoS One* 2026; **PMID:42189790**, DOI:10.1371/journal.pone.0349345 **[VERIFIED]**

It was defined as an entity by Bolande roughly 60 years ago and was originally considered uniformly benign:

> "Fifty years ago, Bolande described Congenital Mesoblastic Nephroma (CMN) as a benign lesion. Unexpected aggressive clinical behaviors prompted a sub-classification based on histology."
> — Jehangir et al., *Pediatr Surg Int* 2017; **PMID:28856451** **[VERIFIED]**

Modern framing (WHO 2022, *Urinary and Male Genital Tumours*) places it among **paediatric renal mesenchymal tumours** as a *mesenchymal/myofibroblastic tumour of low malignant potential* with three morphological subtypes — **classic**, **cellular**, **mixed**. **[SECONDARY]**

A central conceptual point for knowledge-base modelling: **cellular CMN is not biologically a "nephroma" at all.** It is the renal manifestation of infantile (congenital) fibrosarcoma:

> "Our studies indicate that classical and cellular CMN have different genetic features and support the concept that cellular CMN is histogenetically related to CFS."
> — Knezevich et al., *Cancer Res* 1998; **PMID:9823307** **[VERIFIED]**

> "CMN and CFS are pathogenetically related, and it is likely that they represent a single neoplastic entity, arising in either renal or soft tissue locations."
> — Rubin et al., *Am J Pathol* 1998; **PMID:9811336** **[VERIFIED]**

> "The absence of expression of stem cell markers and markers involved in urogenital development suggests that MN is not a nephroma and most likely represents a soft tissue tumour, with congenital infantile fibrosarcoma representing cellular MN with a predilection to arise in the kidney."
> — El Demellawy et al., *Pathology* 2016; **PMID:27020209** **[VERIFIED]**

### 1.2 Key Identifiers

| Resource | Identifier | Status |
|---|---|---|
| Mondo | **MONDO:0017043** "congenital mesoblastic nephroma" | **[VERIFIED]** against `cache/mondo/terms.csv` |
| Orphanet | **ORPHA:2665** "Congenital mesoblastic nephroma" | **[SECONDARY]** (Orphanet listing via search) |
| ICD-O-3.2 | **8960/1** — mesoblastic nephroma; subtypes: classic, cellular, mixed CMN | **[SECONDARY]** (ICD-O-3.2 update tables, WHO 2022) |
| MeSH | "Nephroma, Mesoblastic" | **[VERIFIED]** — the MeSH descriptor appears in the indexed MEDLINE records of PMID:42189790, 29286563, 32590884, 35039190 |
| OMIM | **No phenotype entry** (somatic tumour) | **[VERIFIED by absence]** |
| ICD-10 | Best fit **D41.0** (neoplasm of uncertain/unknown behaviour of kidney) given the `/1` behaviour code; cellular CMN with metastasis is coded as **C64** in practice | **[LEAD]** — needs confirmation against an ICD browser before binding |
| ICD-11 | Not resolved in this review | **[NOT AVAILABLE]** |
| UMLS | Not resolved in this review | **[NOT AVAILABLE]** |

### 1.3 Synonyms and Alternative Names

- Congenital mesoblastic nephroma (CMN); mesoblastic nephroma (MN)
- **Bolande tumour**
- **Fetal renal hamartoma**; **leiomyomatous hamartoma** — the latter appears verbatim in **PMID:31388496** ("Congenital mesoblastic nephroma (CMN) also called leimyomatous harmartoma is a mesenchymal renal tumor") **[VERIFIED]**
- **Stromal nephroma, malignant** (the synonym supplied in the task header; this is a historical/registry synonym and is **not** recommended as a display name — it misrepresents the classic subtype)
- Subtype names: classic (conventional) CMN; cellular CMN; mixed CMN

**Naming recommendation:** retain **"Congenital Mesoblastic Nephroma"** as the entry name. It is the WHO/ICD-O/MONDO-preferred term, covers exactly the scope of the entry (all three subtypes), and avoids the misleading "malignant" qualifier.

### 1.4 Data Provenance

Nearly all quantitative knowledge is **aggregated disease-level** rather than EHR/individual-patient: four trial-registry cohorts (SIOP 93-01, SIOP WT 2001, UK-IMPORT, AIEOP; n=376), the SIOP/GPOH nephroblastoma study (n=111), the SIOP-RTSG radiology panel (n=52 MRIs), plus institutional pathology series (n=9–22) and a large case-report literature. No population-based EHR phenotype study of CMN was identified.

---

## 2. Etiology

### 2.1 Primary Causal Factors

CMN is caused by **somatic oncogenic kinase lesions arising in utero**. The three-way molecular architecture was established over two decades:

1. **ETV6::NTRK3** — first cloned in congenital fibrosarcoma:
   > "By cloning the chromosome breakpoints, we show that the rearrangement fuses the ETV6 (also known as TEL) gene from 12p13 with the 15q25 NTRK3 neurotrophin-3 receptor gene (also known as TRKC)."
   > — Knezevich et al., *Nat Genet* 1998; **PMID:9462753** **[VERIFIED]**

   Then shown in cellular CMN (PMID:9823307, PMID:9811336).

2. **EGFR internal tandem duplication** — the defining lesion of classic/mixed CMN, discovered by whole-genome/transcriptome sequencing of fusion-negative tumours:
   > "A key finding is recurrent mutation of EGFR in CMN by internal tandem duplication of the kinase domain, thus delineating CMN from other childhood renal tumors."
   > — Wegert et al., *Nat Commun* 2018; **PMID:29915264**, DOI:10.1038/s41467-018-04650-6 **[VERIFIED]**

   The duplicated interval is tight: *"breakpoints clustered in a narrow genomic window around the kinase domain of EGFR encoded in exons 18−25."* **[VERIFIED from full text]**

3. **BRAF intragenic rearrangements / KLHL7::BRAF** — a rare third driver:
   > "Furthermore, we identify BRAF intragenic rearrangements in CMN and IFS." (**PMID:29915264**) **[VERIFIED]**
   > "Rare cellular CMNs may harbour non-canonical mutations such as the KLHL7-BRAF fusion, which was found in one case." — Zhao et al., *Histopathology* 2020; **PMID:32590884** **[VERIFIED]**

**Genomes are otherwise quiet.** Wegert et al. report a *"median of 45 substitutions and 9 insertions or deletions per genome"* **[VERIFIED from full text]** — i.e. CMN is a single-driver tumour with essentially no cooperating mutational background, which is why it behaves as a developmental lesion rather than a progressively evolving cancer.

### 2.2 Genetic Risk Factors

- **No inherited predisposition is established.** No germline susceptibility gene, GWAS locus, or familial clustering has been demonstrated for CMN. **[VERIFIED by absence across all sources reviewed]**
- A **small number of CMN cases in Beckwith–Wiedemann syndrome** have been reported, but the association is anecdotal and far weaker than the BWS–Wilms association. **[LEAD]**
- **Secondary (non-driver) cytogenetic changes** are acquired and are consequences, not predispositions: trisomy 11 and polysomies of 8, 17, 20:
  > "we found trisomy 11 only in cellular or mixed CMNs with the ETV6-NTRK3 gene fusion" (**PMID:9823307**) **[VERIFIED]**
  > "These findings demonstrate that t(12;15) translocation, and the associated ETV6-NTRK3 fusion, can antedate acquisition of chromosome polysomies in CMN and CFS." (**PMID:9811336**) **[VERIFIED]**

  This ordering matters mechanistically: **the fusion is the initiating event; polysomies are later clonal-progression events.**

### 2.3 Environmental Risk Factors

**None identified.** No toxin, drug, radiation, dietary, infectious, or maternal exposure has been linked to CMN in any source reviewed. Given that the tumour is present at or before birth and carries an essentially unmutated genome, an environmental mutagenic aetiology is biologically implausible. Demographic associations that do exist are weak and descriptive:

- **Sex:** modest male predominance, M:F **1.4:1** (221 males / 155 females) in the SIOP cohort **[VERIFIED from PMC13210389]**; 2:1 in one small Chinese series (PMID:41810180) **[VERIFIED]**; 67.6% male among prenatally detected fetuses **[VERIFIED from PMC9406745]**.
- **Age:** overwhelmingly the first 3 months of life (see §9).
- **Laterality:** 64.7% left-sided in the prenatal series **[VERIFIED from PMC9406745]**, but 7/9 right-sided in one postnatal series (PMID:41810180) — **no consistent laterality**; report as unestablished.

### 2.4 Protective Factors

**Not applicable / none known.** No protective allele, diet, or exposure has been studied. Note one clinically important point that is sometimes mistaken for a protective factor: **ETV6::NTRK3 positivity within the cellular subtype is prognostically favourable**, not protective against developing the disease:

> "Within the group of cellular MN, patients having translocation-positive tumours had a significantly superior RFS (5-year RFS: 100% vs. 73%)."
> — Vokuhl et al., *Pediatr Blood Cancer* 2018; **PMID:29286563** **[VERIFIED]**

### 2.5 Gene–Environment Interactions

**No data.** No GxE study of CMN exists. CTD/PheGenI contain no CMN-specific gene–chemical interactions.

---

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes with Suggested HPO Bindings

All HPO CURIE/label pairs below were **verified against this repository's committed `cache/hp/terms.csv`** (derived from HPO), not written from memory.

| Phenotype | HPO term | Type | Onset | Frequency | Severity / course |
|---|---|---|---|---|---|
| Abdominal mass (the presenting sign in the great majority) | **HP:0031500** *Abdominal mass* | Clinical sign | Congenital/neonatal | ~90% of postnatal presentations (9/10 in PMID:41810180) **[VERIFIED]**; "most commonly discovered as a palpable abdominal mass" **[SECONDARY, Orphanet]** | Stable→progressive until resection |
| Renal neoplasm | **HP:0009726** *Renal neoplasm* | Structural/neoplastic | Congenital | 100% (definitional) | — |
| Hypertension | **HP:0000822** *Hypertension* | Clinical sign / lab | Neonatal | Commonly cited; **frequency disputed** — Orphanet lists it as an occasional feature, while some reviews claim up to 80%. **Do not curate a high frequency without a primary series.** | Resolves after nephrectomy |
| Increased circulating renin | **HP:0000848** *Increased circulating renin concentration* | Lab abnormality | Neonatal | Rare ("rarely with hypercalcemia or hyperreninemia" — Orphanet) **[SECONDARY]** | Normalises post-nephrectomy **[LEAD: PMID:2544716]** |
| Hypercalcemia | **HP:0003072** *Hypercalcemia* | Lab abnormality | Neonatal | Uncommon; "up to 20%" quoted in review literature **[SECONDARY]** — treat as a paraneoplastic rarity | Can be **severe/life-threatening**; resolves after resection |
| Elevated PTH (post-operative, transient) | **HP:0003165** *Elevated circulating parathyroid hormone level* | Lab abnormality | Post-nephrectomy | In PTHrP-driven cases | Transient, 6–12 weeks |
| Hypophosphatemia | **HP:0002148** | Lab abnormality | Peri-operative | With hungry-bone phase | Transient |
| Hematuria | **HP:0000790** *Hematuria* | Clinical sign | Neonatal | Recognised presentation (PMID:35039190 list) **[VERIFIED]** | Usually mild |
| Polyuria | **HP:0000103** *Polyuria* | Clinical sign | Neonatal | Recognised presentation (PMID:35039190) **[VERIFIED]** | — |
| Vomiting | **HP:0002013** *Vomiting* | Symptom | Neonatal/infant | Non-specific; prominent in the canine cases | — |
| Abdominal distention | **HP:0003270** *Abdominal distention* | Clinical sign | Neonatal | Common with large tumours | Progressive |
| Anemia | **HP:0001903** *Anemia* | Lab abnormality | Neonatal | Reported with large/haemorrhagic tumours | — |
| Thrombocytosis | **HP:0001894** *Thrombocytosis* | Lab abnormality | Neonatal | Occasional paraneoplastic finding **[LEAD]** | — |
| Neoplasm of the lung (metastasis) | **HP:0100526** *Neoplasm of the lung* | Structural | Infant | **39% of metastatic cases** (PMID:28856451) **[VERIFIED]** | Severe |
| Abnormality of the liver (metastasis) | **HP:0001392** | Structural | Infant | **29% of metastatic cases** (PMID:28856451) **[VERIFIED]** | Severe |
| Osteolysis / bone metastasis | **HP:0002797** *Osteolysis* | Structural | Infant | Rare; documented with dramatic remodelling under larotrectinib (PMID:29893456) **[VERIFIED]** | Severe, reversible on TRK inhibition |
| Congestive heart failure (high-output / compression) | **HP:0001635** | Clinical sign | Neonatal | Rare | Severe |
| Neonatal death | **HP:0003811** | Outcome | Perinatal | 12.2% of **prenatally detected** fetal CMN (**PMC9406745**) **[VERIFIED]** | — |

### 3.2 Fetal / Perinatal Phenotypes (the under-appreciated severity axis)

Fetal CMN behaves very differently from neonatal CMN. The Tongsong systematic review of 41 fetal cases (**PMID:36010301**, *Diagnostics* 2022) is the key source:

> "In contrast to CMN in neonates, fetal CMN is much more serious since it significantly impacts adverse pregnancy outcomes and perinatal morbidity and mortality." **[VERIFIED]**

| Fetal phenotype | HPO term | Frequency (41 fetal cases) | Source |
|---|---|---|---|
| Polyhydramnios | **HP:0001561** | **65.8%** (25/38) | PMC9406745 **[VERIFIED]** |
| Premature birth | **HP:0001622** | **61.5%** (24/39); mean GA at delivery 34.7 wk (25–40) | PMC9406745 **[VERIFIED]** |
| Hydrops fetalis | **HP:0001789** | **7.3%** (3/41); **all three died** — "an ominous sign" | PMC9406745 **[VERIFIED]** |
| Perinatal death | **HP:0003811** | **12.2%** (5/41), "associated with hydrops fetalis and immaturity" | PMC9406745 **[VERIFIED]** |
| Small for gestational age / low birth weight | **HP:0001518** *Small for gestational age* | "Preterm birth and low birth weight are the most common adverse pregnancy outcomes" | PMID:36010301 **[VERIFIED]** |

Detection timing is diagnostically decisive:

> "No single case has been diagnosed in the first half of pregnancy. No cases were detected during routine anomaly screening at mid-pregnancy. All cases were detected in the third trimester or late second trimester." (**PMID:36010301**) **[VERIFIED]**

Mean gestational age at detection: **32.2 weeks (range 22–40)** **[VERIFIED from PMC9406745]**.

### 3.3 A Single Reported Co-Occurring Malformation

> "Histopathological examination confirmed the diagnosis of CMN along with fetal pachygyria/lissencephaly... To the best to our knowledge, the association of CMN with lissencephaly has not been described in the literature so far."
> — Zakić et al., *Biomedicines* 2025; **PMID:39857780** **[VERIFIED]**

HPO: **HP:0001339** *Lissencephaly*. **Curate as a single case report, not as a disease–phenotype association.** One co-occurrence in a disease detected prenatally alongside routine CNS imaging is not evidence of a shared mechanism.

### 3.4 Quality-of-Life Impact

**No disease-specific QoL instrument data exist for CMN.** No EQ-5D, SF-36, PROMIS, or PedsQL study was identified. This is a genuine evidence gap. The relevant long-term QoL burden is inferred rather than measured and derives from:
- **Solitary kidney after unilateral nephrectomy** (lifelong; the SIOP authors recommend "long-term follow-up for late effects from nephrectomy and chemotherapy" **[VERIFIED from PMC13210389]**);
- **Prematurity sequelae** in the prenatally detected group (61.5% preterm);
- **Chemotherapy late effects** in the ~21% who receive it.

---

## 4. Genetic / Molecular Information

### 4.1 Causal Genes (all somatic)

| Gene | HGNC (verified) | Locus | Lesion in CMN | Consequence |
|---|---|---|---|---|
| **EGFR** | `hgnc:3236` | 7p11.2 | In-frame ITD of exons 18–25 (kinase-domain duplication, KDD) | **Gain of function** — ligand-independent activation |
| **ETV6** | `hgnc:3495` | 12p13 | 5′ partner in t(12;15)(p13;q25) | Contributes SAM/PNT oligomerisation domain |
| **NTRK3** | `hgnc:8033` | 15q25 | 3′ partner — PTK domain | **Gain of function** — constitutive TRKC kinase |
| **BRAF** | `hgnc:1097` | 7q34 | Intragenic rearrangement; KLHL7::BRAF fusion; CR1 deletion + exon-2 tandem duplication | **Gain of function** — loss of autoinhibition |
| **NTRK1** | `hgnc:8031` | 1q23.1 | TPM3::NTRK1; LMNA::NTRK1 | **Gain of function** |
| **TPM3** | `hgnc:12012` | 1q21.3 | 5′ fusion partner | Oligomerisation domain donor |
| **LMNA** | `hgnc:6636` | 1q22 | 5′ fusion partner **[LEAD]** | Oligomerisation domain donor |
| **EML4** | `hgnc:1316` | 2p21 | EML4::NTRK3, EML4::ALK **[LEAD]** | Oligomerisation domain donor |
| **ALK** | `hgnc:427` | 2p23.2 | 3′ partner (rare) **[LEAD]** | Gain of function |
| **KLHL7** | *not in local cache — look up before binding* | 7p15.3 | 5′ partner of KLHL7::BRAF | — |

### 4.2 Genotype–Phenotype Correlation (the central structure of this disease)

This is the most important curatable fact in CMN and is supported by several independent series:

| Series | Classic | Cellular | Mixed |
|---|---|---|---|
| Knezevich 1998 (**PMID:9823307**) | 0/4 ETV6::NTRK3 | 8/9 ETV6::NTRK3 | 2/2 ETV6::NTRK3 |
| Rubin 1998 (**PMID:9811336**) | — | 5/6 CMN fusion+ (mixed cohort) | — |
| El Demellawy 2016 (**PMID:27020209**) | 0/5 | 8/8 | 5/6 |
| Vokuhl 2018, SIOP/GPOH (**PMID:29286563**) | 0/n (all negative) | 17/29 (58%) | 0/n (all negative) |
| Wegert 2018 (**PMID:29915264**) | 10/10 EGFR-ITD | 2/17 EGFR-ITD | 2/4 EGFR-ITD |
| Zhao 2020 (**PMID:32590884**) | **12/12 EGFR-ITD** | 4/5 ETV6::NTRK3, 1 KLHL7::BRAF | 4/5 EGFR-ITD, 1 ETV6::NTRK3 |
| Chami 2024 (**DOI:10.1002/gcc.23266**) | 7/8 classic-or-mixed EGFR-ITD | 0/5 EGFR-ITD | (included above) |

Verbatim anchors:

> "All 12 classic CMNs had EGFR ITD. Of the five cellular CMNs, four had the ETV6-NTRK3 fusion and one had the KLHL7-BRAF fusion. Of the five mixed CMNs, four had EGFR ITD, and one had the ETV6-NTRK3 fusion." (**PMID:32590884**) **[VERIFIED]**

> "All classical and mixed MN were translocation negative. Seventeen out of 29 (58%) cellular MN harbored the ETV6-NTRK3 translocation." (**PMID:29286563**) **[VERIFIED]**

> "Classical and mixed congenital mesoblastic nephroma (CMN) are characterized by an internal tandem duplication (ITD) of the EGFR gene, in contrast to cellular CMN that usually harbors an ETV6::NTRK3 gene fusion." (**DOI:10.1002/gcc.23266**) **[VERIFIED]**

**Note the discordance to curate honestly:** the Vokuhl SIOP/GPOH series found **0%** fusion positivity in mixed CMN, while Knezevich, El Demellawy and Zhao all found mixed tumours split between the two drivers. The likely explanation is sampling of a histologically heterogeneous tumour, plus method sensitivity (FISH/RT-PCR vs NGS anchored multiplex PCR). Do not present "mixed CMN = EGFR-ITD" as settled.

**Molecular classification proposed:**
> "CMN can be molecularly classified into NTRK3 fusion type, EGFR activation type and others."
> — Lei et al., *Pract Lab Med* 2020; **PMID:32490123** **[VERIFIED]**

### 4.3 Variant Classification, Type, and Frequency

- **Variant class:** structural — intragenic tandem duplication (EGFR, BRAF) and balanced translocation-derived gene fusion (ETV6::NTRK3, NTRK1 fusions). **No recurrent point mutation defines CMN.**
- **ACMG/AMP classification:** not applicable — these are **somatic** oncogenic drivers graded on the AMP/ASCO/CAP somatic tiering system (Tier I/II oncogenic drivers), not the germline ACMG framework.
- **Population allele frequency (gnomAD etc.): not applicable** — somatic, absent from germline databases.
- **Functional consequence:** uniformly **GAIN_OF_FUNCTION**. For KB purposes this belongs in `GeneticContext.functional_impact_category: GAIN_OF_FUNCTION` with `variant_origin: SOMATIC`, and the corresponding pathway node carries `modifier: GAIN_OF_FUNCTION` (the activation is qualitative — escape from ligand/regulatory control — not merely `INCREASED`).
- **COSMIC/cBioPortal:** EGFR-KDD is catalogued as a rare oncogenic EGFR alteration across lung, glioma and soft-tissue tumours (**PMID:26286086**) **[VERIFIED]**; in CMN it is near-universal in the classic subtype, i.e. **the same allele is ultra-rare in adults and defining in infants**.

### 4.4 Modifier Genes

**None identified.** The secondary polysomies (8, 11, 17, 20) are the closest thing to a modifier and are clonal-progression markers rather than germline modifiers.

### 4.5 Epigenetics

**No CMN-specific methylation or chromatin study was identified.** Methylation-array classification has been applied to infant soft-tissue tumours as part of the Wegert work (the author list includes the DKFZ methylation-classifier groups: Koelsche, Jones, Pfister) but no CMN-specific epigenetic driver has been reported. **Genuine gap.**

### 4.6 Chromosomal Abnormalities

- **t(12;15)(p13;q25)** — cryptic; not reliably visible on conventional karyotype, which is why FISH/RT-PCR/NGS are required. This cryptic nature is historically why CMN was karyotypically described mainly by its **polysomies**.
- **Trisomy 11** — associated specifically with fusion-positive cellular/mixed CMN (**PMID:9823307**) **[VERIFIED]**.
- **Polysomy 8, 11, 17, 20** — shared with congenital fibrosarcoma (**PMID:9811336**) **[VERIFIED]**.
- **Chromosomal microarray** will **not** detect the balanced t(12;15); it may detect the EGFR ITD as a focal intragenic gain and the polysomies.

---

## 5. Environmental Information

- **Environmental factors:** none established. **[NOT APPLICABLE]**
- **Lifestyle factors:** not applicable (congenital/neonatal disease).
- **Infectious agents:** none. CMN is not infection-associated.
- **Maternal/obstetric factors:** polyhydramnios and preterm birth are **consequences** of the fetal tumour, not causes. Model them as downstream phenotypes, never as environmental exposures.

For KB modelling: this entry should carry **no `environmental:` block**, or, if one is required by workflow, a `review_notes` waiver beginning `Left deliberately uncited.` documenting that ECTO and the CTD/TOXNET literature were searched and that CMN has no reported exposure association — consistent with a single-driver congenital tumour with a near-silent genome.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain

**Branch A — Cellular CMN (ETV6::NTRK3-driven)**

1. **A somatic t(12;15)(p13;q25) occurs in a renal/perirenal mesenchymal progenitor in utero** → **leads to** an in-frame **ETV6::NTRK3** fusion gene joining the ETV6 SAM/PNT oligomerisation domain to the NTRK3 (TRKC) protein tyrosine kinase domain. *[Demonstrated — PMID:9462753, 9811336, 9823307]*
2. The ETV6 SAM domain **drives ligand-independent self-association (polymerisation) of the chimeric protein** → **results in** trans-autophosphorylation of the NTRK3 activation-loop tyrosines. *[Demonstrated in vitro; SAM salt-bridge mutants abolish it — **SECONDARY**, J Biol Chem/Oncogene literature]*
3. Constitutive TRKC kinase activity **recruits IRS-1 and forms a tripartite complex with IGF1R**, required for membrane localisation and transformation. *[Demonstrated in vitro — Tognon et al., *Oncogene* 2012, DOI:10.1038/onc.2011.323]* **[VERIFIED reference; abstract text unavailable in cache — re-fetch before quoting]*
4. This **dually activates the RAS–MAPK (ERK1/2) mitogenic cascade and the PI3K–AKT survival cascade**; both are required for transformation. *[Demonstrated in vitro — **SECONDARY**]*
5. **Leads to** sustained proliferation, apoptosis resistance, and migratory capacity of a spindle (fibroblastic/myofibroblastic) cell population → **a densely cellular, mitotically active spindle-cell tumour** histologically identical to infantile fibrosarcoma. *[Demonstrated — PMID:9823307, 27020209]*
6. **Clonal progression:** acquisition of **trisomy 11** and polysomies 8/17/20 *after* the fusion. *[Demonstrated — PMID:9811336, 9823307]*
7. **Results in** local invasion of perirenal tissue and, in a minority, haematogenous metastasis to **lung (39%) and liver (29%)**. *[Demonstrated — PMID:28856451]*
8. In rare cases, **NTRK1 fusions (TPM3::NTRK1)** substitute at step 1 and appear to produce a **more aggressive** course. *[Single case — PMID:38984028]*

**Branch B — Classic / mixed CMN (EGFR-ITD-driven)**

1. **A somatic intragenic in-frame tandem duplication of EGFR exons 18–25 arises in a renal mesenchymal progenitor** → duplicates the entire kinase domain within one receptor molecule. *[Demonstrated — PMID:29915264, full text: "breakpoints clustered in a narrow genomic window around the kinase domain of EGFR encoded in exons 18−25"]*
2. The tandem kinase domains **form an intramolecular asymmetric (activator–receiver) dimer**, which **results in** **ligand-independent, constitutive EGFR activation** without any EGF requirement. *[Mechanism demonstrated for EGFR-KDD in lung cancer — PMID:26286086; structure–function follow-up **SECONDARY**]*
3. **Leads to** constitutive **RAS → RAF → MEK1/2 → ERK1/2 (MAPK) signalling**. *[Demonstrated in CMN tissue — PMID:39921750: "p-Mek1/2 and p-Erk1/2 immunoreactivity was significantly increased in the EGFR-ITDs tumour group (p = 0.018 and p = 0.017)"; transcriptomic GO enrichment for MAPK signalling]*
4. **Results in** proliferation of elongated, interdigitating spindle cells with **low mitotic activity and infiltrative but non-destructive growth** at the tumour–kidney interface → the **classic** morphology.
5. **Leads to** a **locally expansile, essentially benign lesion** cured by complete excision; relapse is rare but not zero (3 of 16 relapses in the SIOP cohort were classic — **PMID:42189790**).

**Branch C — BRAF-rearranged CMN (rare)**

1. Somatic BRAF intragenic rearrangement (CR1 deletion + exon-2 tandem duplication) or **KLHL7::BRAF** fusion → **removes the autoinhibitory N-terminal regulatory region**.
2. **Results in** constitutive BRAF kinase activity: *"Mutated tumors displayed intense staining of phosphorylated ERK by immunohistochemistry, consistent with activated signaling downstream of BRAF"* (**PMID:29915264**, full text) **[VERIFIED]**.
3. **Converges on the same MEK–ERK output** as Branches A and B.

**Convergence point:** all three branches converge on **constitutive RAS–MAPK signalling in a renal mesenchymal/myofibroblastic cell**, which is why the three genotypes produce overlapping morphology and why MEK inhibition is a proposed genotype-agnostic strategy (**PMID:39921750**).

### 6.2 Paraneoplastic Sub-Chains (branch from the tumour node, not from the driver)

**Hypercalcaemia — two distinct, documented mechanisms:**

*Chain C1 (PTHrP):*
1. Tumour cells express **PTHrP** (`PTHLH`, `hgnc:9607`) → "Immunohistochemical staining of tumor cells was positive for PTHrP" (**PMID:21161280**) **[VERIFIED]**
2. Circulating PTHrP engages PTH1R on bone and kidney → **increased osteoclastic bone resorption and renal tubular calcium reabsorption**
3. → **severe hypercalcaemia** (**HP:0003072**)
4. After nephrectomy: "Following resection of the tumor serum PTHrP normalized" → **rebound 'hungry bone'-like state**: "the infants developed elevated serum parathyroid hormone with low-normal serum Ca and P, and undetectable urinary Ca and P, probably due to their movement into bone" (**PMID:21161280**) **[VERIFIED]**
5. → requires **calcitriol, Ca and P supplementation for 6–12 weeks** (**PMID:21161280**) **[VERIFIED]**

*Chain C2 (prostaglandin-mediated, the older and rarer mechanism):*
1. Tumour synthesises **prostaglandin E** — "A large quantity of PGE was extracted from the tumor by radioimmunoassay after incubation" (**PMID:3017143**) **[VERIFIED]**
2. "During surgery a prostaglandin arteriovenous gradient was demonstrated" with **normal PTH** (**PMID:3017143**) **[VERIFIED]**
3. → PGE-driven bone resorption → hypercalcaemia
4. "Both blood calcium and urinary prostaglandins returned to normal after nephrectomy" (**PMID:3017143**) **[VERIFIED]**

**Hypertension chain:**
1. Tumour compresses/entraps adjacent renal parenchyma → **local ischaemia of juxtaglomerular apparatus** (and in some reports direct renin production by tumour tissue)
2. → **renin (REN, `hgnc:9958`) hypersecretion** → **HP:0000848**
3. → angiotensin II generation, secondary hyperaldosteronism
4. → **neonatal hypertension (HP:0000822)**, reversing after nephrectomy
*[Mechanism is **SECONDARY/LEAD** — the primary citation to chase is PMID:2544716 "Congenital mesoblastic nephroma, renin production, and hypertension". Do not curate the "80% of CMN have hypertension" figure circulating in review literature; it is not supported by any primary series read here.]*

**Mass-effect chain:**
1. Large tumour → raised intra-abdominal pressure → **chronic abdominal compartment syndrome**
2. → "significant compression of local vascular and solid structures, resulting in multi-systemic end-organ dysfunction" (**PMID:36415355**) **[VERIFIED]**

**Fetal chain:**
1. Fetal renal mass → impaired fetal urine handling / unexplained third-trimester growth
2. → **polyhydramnios (65.8%)** → uterine over-distension
3. → **preterm birth (61.5%)**, low birth weight
4. In a minority → **hydrops fetalis (7.3%)** → **perinatal death (12.2%)**
*[Chain demonstrated epidemiologically; the step 1→2 mechanism is inferred, not demonstrated — PMID:36010301 / PMC9406745]*

### 6.3 Ontology Suggestions for Mechanism Nodes

All CURIEs below **verified against this repository's committed term caches**.

**GO biological process / molecular function:**
- `GO:0007173` *epidermal growth factor receptor signaling pathway* — Branch B node
- `GO:0005006` *epidermal growth factor receptor activity* — EGFR-ITD molecular function
- `GO:0004714` *transmembrane receptor protein tyrosine kinase activity* — ETV6::NTRK3 chimeric kinase
- `GO:0007169` *cell surface receptor protein tyrosine kinase signaling pathway*
- `GO:0046777` *protein autophosphorylation* — the oligomerisation→autophosphorylation step
- `GO:0000165` *MAPK cascade* and `GO:0043410` *positive regulation of MAPK cascade* — the convergence node
- `GO:0008284` *positive regulation of cell population proliferation*
- `GO:0048146` *positive regulation of fibroblast proliferation*
- `GO:0043066` *negative regulation of apoptotic process* — PI3K–AKT arm
- `GO:0030335` *positive regulation of cell migration* / `GO:0016477` *cell migration* — invasion/metastasis
- `GO:0030316` *osteoclast differentiation* — PTHrP hypercalcaemia chain
- `GO:0002018` *renin-angiotensin regulation of aldosterone production* and `GO:0003081` *regulation of systemic arterial blood pressure by renin-angiotensin* — hypertension chain
- `GO:0001822` *kidney development* — developmental context

*(PI3K-specific GO terms were not present in the local cache; look up `phosphatidylinositol 3-kinase signaling` before binding.)*

**CL cell types:**
- `CL:0000186` *myofibroblast cell* — the best match for the CMN tumour cell
- `CL:0000057` *fibroblast* — alternative/parent
- `CL:0000192` *smooth muscle cell* — reflects SMA positivity
- `CL:0000134` *mesenchymal stem cell* — putative progenitor (bind with caution; not demonstrated)
- `CL:0000648` *kidney granular cell* — juxtaglomerular renin-producing cell, for the hypertension chain
- `CL:0000669` *pericyte*, `CL:0000650` *mesangial cell* — candidate related renal mesenchymal lineages

**UBERON anatomy:** `UBERON:0002113` *kidney*; `UBERON:0001225` *cortex of kidney*; `UBERON:0000362` *renal medulla*; `UBERON:0001224` *renal pelvis*; `UBERON:0003220` *metanephric mesenchyme*; `UBERON:0002048` *lung*; `UBERON:0002107` *liver*; `UBERON:0001474` *bone element*; `UBERON:0000173` *amniotic fluid* (polyhydramnios).

**CHEBI:** `CHEBI:29108` *calcium(2+)*; `CHEBI:15551` *prostaglandin E2*; `CHEBI:17823` *calcitriol*.

### 6.4 Molecular Profiling

- **Transcriptomics:** Hamada et al. (**PMID:39921750**) applied nCounter gene-expression profiling to 11 CMNs. *"PCA revealed differences in mutation patterns between the EGFR-ITDs and NTRK fusion tumor groups. Gene ontology analysis of the highly expressed genes in the EGFR-ITDs tumor group revealed enrichment related to the mitogen-activated protein kinase (MAPK) signaling pathway."* **[VERIFIED]** — i.e. **the two genotypes are transcriptionally separable.**
- **Proteomics (IHC surrogate):** p-MEK1/2 and p-ERK1/2 significantly increased in EGFR-ITD tumours (p=0.018, p=0.017); **EGFR IHC itself is useless** as a surrogate (**PMID:39921750**, **PMID:32590884**) **[VERIFIED]**.
- **Metabolomics / lipidomics:** **no data**.
- **Single-cell / spatial transcriptomics:** **no CMN study identified** — a clear gap, especially for resolving the cell of origin.
- **Functional genomics (CRISPR/RNAi):** no CMN-specific screen; DepMap has no CMN line.

---

## 7. Anatomical Structures Affected

**Primary organ:** kidney (`UBERON:0002113`), **unilateral and solitary** — Orphanet's definition: *"a unilateral, solitary, well demarcated, mesenchymal/myofibroblastic neoplasm occurring in very young children"* **[SECONDARY]**. Bilateral CMN is not a recognised presentation.

**Site within kidney:** the tumour is characteristically **centred on the renal sinus / medullary region and infiltrates outward**, which is the anatomical basis of the imaging "ring sign". Sources describe CMN as arising "from the infantile renal sinus" **[SECONDARY]**. (A UBERON term for *renal sinus* was not present in the local cache — look it up before binding; `UBERON:0001224` *renal pelvis* and `UBERON:0000362` *renal medulla* are available fallbacks.)

**Secondary organ involvement (cellular subtype only, and uncommon):**
- **Lung** (`UBERON:0002048`) — 39% of metastatic cases
- **Liver** (`UBERON:0002107`) — 29%
- **Bone** (`UBERON:0001474`) — rare (PMID:29893456)
- **Peritoneum** — reported in the TPM3::NTRK1 case (PMID:38984028)
- **Brain** (`UBERON:0000955`) — only in the single lissencephaly co-occurrence, which is a developmental malformation, **not metastasis**

**Body systems:** urinary/renal (primary); cardiovascular (renin-mediated hypertension); musculoskeletal/mineral (PTHrP hypercalcaemia, osteolysis); respiratory and hepatobiliary (metastatic); gastrointestinal (mass effect).

**Tissue level:** connective/mesenchymal tissue — interlacing fascicles of spindle cells in a myxoid-to-collagenous stroma. Verbatim from the veterinary literature (which describes the identical morphology): *"neoplastic spindle cells forming interlacing fascicles, bundles and whorls, within a loose myxoid to dense collagenous stroma"* (**PMID:23020172**) **[VERIFIED]**.

**Cell level:** myofibroblastic (`CL:0000186`), vimentin+ and smooth-muscle-actin+ (**PMID:23020172**) **[VERIFIED]**. Notably **negative** for urogenital-development and stem-cell markers:
> "we identified 19 cases of MN... and examined each case for markers known to be important in urogenital embryological development (PAX8, WT1 and RCC), stem cell associated markers (Oct 4, CD34 and c-kit)... The absence of expression of stem cell markers and markers involved in urogenital development suggests that MN is not a nephroma" (**PMID:27020209**) **[VERIFIED]**

**Subcellular:** plasma membrane (both drivers are membrane-proximal RTK lesions; ETV6::NTRK3 membrane localisation specifically requires the IRS1/IGF1R complex) and cytosol (MAPK/PI3K effectors). GO cellular-component terms were not verified in this review.

**Lateralisation:** **unilateral**, with no established side preference (64.7% left in the prenatal series vs 7/9 right in one postnatal series).

---

## 8. Temporal Development

### 8.1 Onset

- **Congenital.** The tumour is present at birth and frequently detected in the **third trimester** (mean 32.2 weeks). Never detected in the first half of pregnancy (**PMID:36010301**).
- **Median age at diagnosis: 28 days** (range 0–953 days); **71.5% diagnosed within the first 3 months**, **88% by 6 months** (**PMID:42189790** / PMC13210389) **[VERIFIED]**.
- **Onset pattern:** congenital, with **rapid late-gestation growth** — "mesoblastic nephroma usually manifests in the third trimester, with a rapid and unexplained increase in tumor size" **[SECONDARY]**.
- The outer bound of the age range (953 days ≈ 2.6 years in SIOP; 93 months in one Chinese series) means **"congenital" describes origin, not the age ceiling of presentation** — a point worth capturing in the entry's notes.

### 8.2 Progression and Stage

Staging uses the **SIOP-RTSG / COG renal tumour staging systems** (no CMN-specific staging exists). SIOP 376-patient distribution:

| Stage | n/N | % |
|---|---|---|
| I | 92/337 | **27.4%** |
| II | 177/337 | **52.6%** |
| III | 67/337 | **20%** |
| IV | 1 (liver metastases) | <1% |

**[VERIFIED — PMID:42189790 / PMC13210389]**

**Course:** The overwhelmingly typical course is **a single growth phase followed by surgical cure** — self-limited once resected, not chronic. The minority course is **early local recurrence**:

> "The cumulative 5-year incidence of relapse was 5.3%, with a median time to recurrence of 4 months." (**PMID:42189790**) **[VERIFIED]**; full text gives *"median time to recurrence was 3.6 months (range: 1–9.5 months)"* **[VERIFIED]**

> "Median time to recurrence was 6 months (range 1-12 months)." (**PMID:28856451**) **[VERIFIED]**

**Critical period for intervention:** the first ~12 months after primary surgery.

> "Children with cellular and mixed CMN require close clinical and radiological follow-up for a minimum of 12 months after primary surgery." (**PMID:28856451**) **[VERIFIED]**

The SIOP group recommends **oncological surveillance for 18–24 months**, plus long-term follow-up for nephrectomy and chemotherapy late effects **[VERIFIED from PMC13210389]**.

**A second critical period runs the other way:** the first weeks of life are the window of maximum **treatment** risk, not disease risk —

> "The risk of treatment-related mortality (both surgery- and chemotherapy-related) is relatively high in the first weeks of life, indicating that these young patients deserve special attention with respect to timing and type of treatment." (**PMID:28124468**) **[VERIFIED]**

**Remission:** treatment-induced (surgical) in essentially all cured cases. **Spontaneous regression is not described.**

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| Share of paediatric renal neoplasms | **3–5%** | **PMID:27020209** ("accounts for 3-5% of all paediatric renal neoplasms") **[VERIFIED]**; **PMID:29286563** ("approximately 5%") **[VERIFIED]**; **PMID:39857780** gives the wider "3–10%" **[VERIFIED]** |
| Rank among renal tumours of the first 3 months | **Most common** | **PMID:42189790**, **PMID:38609702** **[VERIFIED]** |
| Incidence | ~**8 per million live births**; alternatively quoted as **1:125,000** | **[SECONDARY]** — both figures come from review literature; no primary population-based study was identified |
| Sex ratio (M:F) | **1.4:1** (221:155, n=376) | PMC13210389 **[VERIFIED]** |
| Median age at diagnosis | **28 days** (0–953 d) | **PMID:42189790** **[VERIFIED]** |
| Prevalence (Orphanet) | Not specified | **[SECONDARY]** |

**Prevalence class for KB purposes:** CMN is best recorded as **`BIRTH_PREVALENCE`** (or `ANNUAL_INCIDENCE` with `rate_denominator: LIVE_BIRTHS`) in the band **`BELOW_1_IN_1000000`** if the 8-per-million figure is used (8/1,000,000 = 0.8 per 100,000 births) — but **flag the figure as secondary**. Qualitatively: **ULTRA_RARE** as a population disease, yet **COMMON within its own age/organ niche**.

### 9.2 Inheritance

- **Inheritance pattern: not applicable — somatic.** CMN is not inherited. There is no Mendelian mode, no penetrance or expressivity to describe, no anticipation, no founder effect, no consanguinity role, and **no carrier frequency**.
- **Germline mosaicism:** not described.
- **Recurrence risk for siblings:** none established; genetic counselling for CMN per se is reassurance, not risk quantification.
- For KB encoding: do **not** add an `inheritance:` block. The disease is encoded through `genetic_context.variant_origin: SOMATIC` on the driver nodes. `HP:0001442` (typified by somatic mosaicism) is **not** appropriate: CMN is a neoplasm with a somatic driver, not a post-zygotic mosaic developmental disorder.

### 9.3 Population Demographics

- **Ethnic/ancestral predilection:** none reported. Cohorts span European (SIOP/GPOH, AIEOP, UK-IMPORT), Chinese (Nanjing), Singaporean, Japanese, and North American series with concordant findings.
- **Geographic distribution:** worldwide; no endemic pattern.
- **Age distribution:** sharply concentrated in the first 3 months, 88% by 6 months, with a long thin tail into early childhood.
- **Geographic distribution of specific variants:** none — the EGFR-ITD/ETV6::NTRK3 split reproduces across European, North American, Singaporean, Japanese and Chinese series.

---

## 10. Diagnostics

### 10.1 Imaging

**Ultrasound** is the primary prenatal and first-line postnatal modality. Prenatal features from 41 fetal cases **[VERIFIED from PMC9406745]**:
- Solid: **88%** (22/25); well-demarcated: **95.5%** (21/22)
- Echogenicity heterogeneous 50%, homogeneous 33.3%
- Strong vascularisation: **63.6%** (7/11)
- Mean diameter 5.2 ± 1.5 cm (2.8–9.0 cm)

The **"ring sign"** was described in 1987 and remains characteristic:
> "A distinctive 'ring sign' on renal sonography was commonly seen in patients with typical intrarenal CMN." (**PMID:3037055**) **[VERIFIED]**

**MRI** is now the preferred modality (SIOP-RTSG). The largest MRI series (n=52) **[VERIFIED — PMID:38609702]**:
- Classic type: **homogeneous**, lacking haemorrhage/necrosis/cysts; **concentric ring sign in 14/24 (58.3%)**
- Cellular/mixed: **heterogeneous and markedly larger** — mean volumes **311.6 cm³ (cellular)** and **174.2 cm³ (mixed)** vs **41.0 cm³ (classic)**, *P*<0.001
- All: **T2-weighted isointense, T1-weighted hypointense**
- Mean ADC **1.05–1.10 × 10⁻³ mm²/s**

> "classic type congenital mesoblastic nephroma predominantly presented as a homogeneous T2-weighted isointense mass with a typical concentric ring sign, whereas the cellular type appeared more heterogeneous." (**PMID:38609702**) **[VERIFIED]**

Crucially, the same paper concedes the core diagnostic problem:
> "discriminating congenital mesoblastic nephroma, especially from the more common Wilms tumor, solely based on imaging remains difficult." **[VERIFIED]**

**NCIT bindings (verified):** `NCIT:C17230` *Ultrasound Imaging*; `NCIT:C16809` *Magnetic Resonance Imaging*; `NCIT:C17204` *Computed Tomography*.

### 10.2 Histopathology and Immunohistochemistry

- **Classic:** elongated, interdigitating spindle cells in fascicles, low mitotic rate, infiltrative margin.
- **Cellular:** densely packed plump spindle cells, high mitotic rate — indistinguishable from infantile fibrosarcoma.
- **Mixed:** both patterns in one tumour.
- **IHC:** vimentin+, smooth muscle actin+ (**PMID:23020172**); **negative** for PAX8, WT1, RCC, OCT4, CD34, c-kit (**PMID:27020209**).
- **Cyclin D1 and β-catenin** discriminate subtypes: *"cyclin D1 and beta-catenin may be useful markers for differentiating between cellular MN and classic MN when the histology is not conclusive"* (**PMID:27020209**) **[VERIFIED]**.
- **Pan-TRK IHC is the single best surrogate marker:** *"Pan-Trk immunoreactivity was 100% sensitive and 94.1% specific for the presence of NTRK rearrangement. However, EGFR staining was only 62.5% sensitive and 33.3% specific for EGFR ITD."* (**PMID:32590884**) **[VERIFIED]**
- **For EGFR-ITD, use phospho-MEK1/2 and phospho-ERK1/2 instead of EGFR:** (**PMID:39921750**) **[VERIFIED]**.

**NCIT:** `NCIT:C16722` *Immunohistochemistry*.

### 10.3 Molecular Testing

**Recommended approach** (synthesised from PMID:32590884, 32490123, 35801295, 39921750):
1. **Pan-TRK IHC** as a screen.
2. **FISH (ETV6 break-apart)** or **RT-PCR** for ETV6::NTRK3 — `NCIT:C17563` *Fluorescence In Situ Hybridization*.
3. If fusion-negative, **NGS capable of detecting intragenic tandem duplications** — `NCIT:C101293` *Next Generation Sequencing*. This step is non-optional and is the single most actionable technical message in the recent literature:
   > "We also highlight the importance of appropriate test selection and bioinformatic analysis for identification of this genomic alteration that is unexpectedly common in congenital and infantile spindle cell tumors." (**PMID:35801295**) **[VERIFIED]**

   Standard RT-PCR fusion panels **miss EGFR ITD entirely**: Koo et al. found EGFR ITD in **3/18 (17%)** of under-1-year tumours previously called fusion-negative by clinical RT-PCR **[VERIFIED]**.
4. **Anchored multiplex PCR NGS** detects both fusion and ITD classes (**PMID:32590884**).

**Not useful:** karyotyping alone (the t(12;15) is cryptic); chromosomal microarray (will not see the balanced translocation); germline WES/WGS (no germline lesion); mitochondrial or repeat-expansion testing (not applicable).

### 10.4 Laboratory Tests

Serum calcium, phosphate, PTH, PTHrP; plasma renin activity; urinalysis for haematuria; full blood count. LOINC bindings were not resolved in this review — **do not type LOINC codes from memory**; seed them through the repository's LOINC cache workflow before binding.

### 10.5 Clinical Criteria and Differential Diagnosis

There are **no consensus clinical diagnostic criteria**; diagnosis is histological plus molecular. The practical rule used by SIOP-RTSG is age-based:

> "patients <3 months of age are advised to undergo upfront nephrectomy, whereas invasive procedures at diagnosis in patients ≥3 months of age are discouraged by the International Society of Pediatric Oncology-Renal Tumor Study Group (SIOP-RTSG)." (**PMID:38609702**) **[VERIFIED]**

**Differential diagnosis — with distinguishing features:**

| Alternative | Distinguishing features |
|---|---|
| **Wilms tumour** (`MONDO:0006058`; HP:0002667 *Nephroblastoma*) | Older (median ~3 y); triphasic blastemal/epithelial/stromal histology; WT1/PAX8+; heterogeneous with necrosis on MRI |
| **Clear cell sarcoma of the kidney** (`MONDO:0005006`) | **The dangerous one** — bone-metastasising, and documented to have been misdiagnosed as CMN: *"The patient had a history of a renal mass three years earlier, for which radical nephrectomy had been performed, and histopathologic diagnosis was compatible with mesoblastic nephroma"*, later proven metastatic CCSK (**PMID:23634181**) **[VERIFIED]**. BCOR-ITD positive. |
| **Rhabdoid tumour of the kidney** (`MONDO:0002729`) | SMARCB1/INI1 loss; also presents in infancy; aggressive |
| **Infantile fibrosarcoma** (`MONDO:0004557` *congenital fibrosarcoma*) | Same genetics, **extrarenal** site |
| **Ossifying renal tumour of infancy, metanephric stromal tumour, renal cyst** | Imaging/histology |
| **Pediatric fibromatosis** | Lacks EGFR ITD — *"none of the five cellular CMNs... Of 11 cases of fibromatosis (six plantar, two digital, and three desmoid), none were positive for EGFR ITD"* (**DOI:10.1002/gcc.23266**) **[VERIFIED]** |

### 10.6 Screening

- **No population screening exists or is warranted.**
- CMN is a **serendipitous finding of third-trimester obstetric ultrasound**. The prenatal review makes the case for recognising it when it appears:
  > "Prenatal diagnosis is essential since it is critical for the antenatal plan, comprising either referral to a tertiary care center or proper surveillance to prevent serious obstetric complications, especially preterm birth." (**PMID:36010301**) **[VERIFIED]**
- **No newborn screening, carrier screening, or cascade screening** — the disease is somatic.

---

## 11. Outcome / Prognosis

### 11.1 Survival

| Metric | Value | Cohort |
|---|---|---|
| 5-year **EFS** | **93.8%** | SIOP/UK-IMPORT/AIEOP, n=376 (**PMID:42189790**) **[VERIFIED]** |
| 5-year **OS** | **96.9%** | same **[VERIFIED]** |
| 5-year **RFS** | **93.2%** | SIOP/GPOH, n=111 (**PMID:29286563**) **[VERIFIED]** |
| 5-year **OS** | **96.8%** | same **[VERIFIED]** |
| 5-year **cumulative incidence of relapse** | **5.3%** | n=376 **[VERIFIED]** |
| Long-term (1987 series) | **"All 17 patients were alive with no evidence of disease at a mean follow-up of 10 years"** | **PMID:3037055** **[VERIFIED]** |
| Single-centre modern series | OS 88.9%, EFS 77.8% (n=9, median FU 36 mo) | **PMID:41810180** **[VERIFIED]** — small-n, relapse-enriched |

**By subtype (5-year RFS):** classic **98%**, cellular **89%**, mixed **80%**; 5-year OS similar across subtypes (98%, 93%, 96%) (**PMID:29286563**) **[VERIFIED]**.

**Deaths and their causes (n=376):** 11 deaths — **6 from disease progression, 2 treatment-related (sepsis; surgical complications), 1 cardiac failure, 1 SIDS** **[VERIFIED from PMC13210389]**. That **~18% of deaths were treatment-related** is the key safety signal and echoes the 2017 review's warning.

### 11.2 The Relapse/Metastasis Subgroup — a Much Worse Picture

> "Of the 38 children with local recurrence and/or metastasis, 59% were girls... The commonest sites of metastases were the lung (39%) and liver (29%). **Fifty percent of these children died of disease.** The outcome of additional chemotherapy (p = 0.5) did not differ from that of surgery alone. The choice of chemotherapy did not influence the outcome (p = 0.6)."
> — **PMID:28856451** **[VERIFIED]**

> "Recurrence and metastasis in cellular CMN are much more common than described earlier and carry a high mortality." **[VERIFIED]**

### 11.3 Prognostic Factors

1. **Histological subtype** — classic best, mixed/cellular worse for relapse (but note the 2026 SIOP caution below).
2. **ETV6::NTRK3 status within cellular CMN** — fusion-positive is **favourable**: 5-year RFS **100% vs 73%** (**PMID:29286563**) **[VERIFIED]**. All seven relapses in that cohort occurred in **translocation-negative** tumours **[VERIFIED]**.
3. **Completeness of resection** — the dominant modifiable factor.
4. **Age >3 months with incomplete resection** — the historical criterion for adjuvant therapy (**PMID:3037055**).
5. **Non-canonical fusions** — `TPM3::NTRK1` associated with a fatal course in the one reported case (**PMID:38984028**).
6. **Hydrops fetalis** — in prenatally detected disease, uniformly fatal in the 3 reported cases **[VERIFIED from PMC9406745]**.

**A 2026 correction to conventional teaching:** the SIOP 376-patient study found relapses in all three subtypes —
> "we highlight that recurrences, though infrequent, tend to occur early and are not restricted to the cellular subtype. Of the 16 relapse cases, 8 were in the cellular subtype, 5 in the mixed subtype, and 3 in the classical subtype." (**PMID:42189790**) **[VERIFIED]**

So "classic CMN is benign" is an over-simplification that should not be curated as an absolute.

### 11.4 Morbidity, Disability, Recovery

- **Recovery potential is excellent**: complete resection is curative in the large majority.
- **Long-term morbidity** derives from solitary kidney, prematurity, and (in the 21% who receive it) chemotherapy exposure. **No published long-term renal-function or neurodevelopmental cohort for CMN survivors was identified** — a genuine gap, and the most clinically useful study someone could run.
- **GBD / disability-weight data:** none for CMN specifically.

---

## 12. Treatment

### 12.1 Surgery — the definitive treatment

> "Complete nephrectomy only is the gold standard treatment." (**PMID:42189790**) **[VERIFIED]**
> "Complete surgical removal is curative in most cases." (**PMID:28124468**) **[VERIFIED]**
> "This study confirms that CMN patients have an excellent outcome, with complete surgical resection being curative in the majority of cases." (**PMID:42189790**) **[VERIFIED]**

**Practice pattern (n=314):** upfront surgery **79%** (248), preoperative chemotherapy **21%** (66) **[VERIFIED]**.

**Approach:** radical (total) unilateral nephrectomy with wide margins, taking perirenal fat; laparoscopic nephrectomy has been reported in selected cases (**PMID:31388496**) **[VERIFIED]**.

**NCIT bindings (verified):** `NCIT:C15284` *Nephrectomy*; `NCIT:C51778` *Radical Nephrectomy*; `NCIT:C15329` *Surgical Procedure*.

Historic but still-cited margin guidance:
> "Nephrectomy was probably also adequate therapy for infants 3 months of age or younger with atypical CMN, even if the tumor extended to the surgical resection margins and into the perinephric connective tissues." (**PMID:3037055**) **[VERIFIED]**

### 12.2 Chemotherapy — selective, and newly shown to work preoperatively

CMN is **chemosensitive**, which was not firmly established before 2026:
> "Among the latter group, 60% of patients showed a measurable reduction in tumor volume, indicating a favorable response to chemotherapy... Chemosensitivity is observed in a significant proportion, suggesting that neoadjuvant chemotherapy may be a viable option in selected cases." (**PMID:42189790**) **[VERIFIED]**

**Indications** (synthesised):
- Inoperable or incompletely resected tumour
- Stage III disease, particularly cellular subtype
- Relapse/metastasis (though with disappointing results — see below)
- Historical: "Adjuvant chemotherapy or radiation or both should be reserved for patients older than 3 months who have grossly unresected tumors and for those patients whose tumors have an unequivocally malignant histologic appearance or evidence of aggressive biologic behavior." (**PMID:3037055**) **[VERIFIED]**

**Regimens used (reported, not protocolised for CMN):** VAC (vincristine–dactinomycin–cyclophosphamide) and ICE (ifosfamide–carboplatin–etoposide); in the Nanjing series these "showed limited efficacy" at relapse (**PMID:41810180**) **[VERIFIED]**.

**Agents with verified CURIEs:** vincristine `CHEBI:28445` / `NCIT:C933`; dactinomycin `NCIT:C412`; cyclophosphamide `CHEBI:4027`; ifosfamide `CHEBI:5864`; carboplatin `CHEBI:31355`; etoposide `CHEBI:4911`; doxorubicin `CHEBI:28748`. Treatment action: `NCIT:C15632` *Chemotherapy*.

**Critical caveat:** in the relapsed/metastatic setting, chemotherapy did **not** improve outcome over surgery alone (p=0.5), and choice of regimen did not matter (p=0.6) (**PMID:28856451**) **[VERIFIED]**.

### 12.3 Targeted Therapy — the main therapeutic advance

**TRK inhibitors for NTRK-fusion CMN.** `NCIT:C93352` *Targeted Therapy*; `NCIT:C1967` *Tyrosine Kinase Inhibitor*.

> "Mesoblastic nephroma is the most frequent renal tumor in newborns and young infants, and the cellular type is characterized by an ETV6-NTRK fusion, which constitutively activates the tropomyosin-related kinase (TRK) signaling pathway. Larotrectinib is a highly selective TRK inhibitor with activity in adult and pediatric patients who have TRK fusions. We present a rare case of a patient with mesoblastic nephroma metastatic to bone who had a dramatic response to larotrectinib."
> — Halalsheh et al., *Pediatr Blood Cancer* 2018; **PMID:29893456** **[VERIFIED]**

- **Larotrectinib** — `NCIT:C115977`
- **Entrectinib** — `NCIT:C114984`, `CHEBI:195558`
- **Repotrectinib (Augtyro)** — FDA accelerated approval **13 June 2024** for adult and paediatric patients **≥12 years** with NTRK fusion-positive locally advanced/metastatic solid tumours, or where resection would cause severe morbidity, after progression on prior therapy (TRIDENT-1, NCT03093116). **[SECONDARY — FDA/ASCO Post/OncLive reporting]** Note the ≥12-year age floor makes repotrectinib largely **unavailable** to the CMN population; larotrectinib and entrectinib carry paediatric indications and are the practical options.

**Acquired resistance is real and documented in CMN:**
> "the patient ultimately died as the tumor became resistant to larotrectinib... we still need to pay attention to the phenomenon of drug resistance to larotrectinib caused by site mutations of TRKA." (**PMID:38984028**) **[VERIFIED]**

**EGFR-directed therapy for EGFR-ITD/KDD CMN.** Rationale transfers from lung cancer, where EGFR-KDD is *"constitutively active"* and *"the index patient had a partial response to the EGFR TKI afatinib"* (**PMID:26286086**) **[VERIFIED]**. In CMN:
> "another with EGFR-KDD experienced disease stabilization after afatinib plus programmed cell death protein 1 (PD-1) blockade following progression on entrectinib and anlotinib." (**PMID:41810180**) **[VERIFIED]**

Afatinib: `CHEBI:61390`. **This is a single case of stable disease, not an established therapy** — curate accordingly.

**MEK inhibition — a proposed but untested strategy:**
> "p-Mek1/2 and p-Erk1/2 immunoreactivity may be useful markers for EGFR-ITDs. Thus, MEK1/2 inhibitors possess the potential to be used as a targeted therapy for CMN with EGFR-ITDs." (**PMID:39921750**) **[VERIFIED]** — note the modal verb: this is a hypothesis generated from IHC and transcriptomics, with **no clinical data**.

### 12.4 Supportive Care

**Hypercalcaemia management** (pre-operative, documented repeatedly):
> "Pre-operatively hypercalcemia was corrected with saline hydration, furosemide, calcitonin and/or pamidronate." (**PMID:21161280**) **[VERIFIED]**
> "Preoperatively, hypercalcemia was corrected with hydration, furosemide, pamidronate, and low-calcium infant formula." (**PMID:35039190**) **[VERIFIED]**

**Post-operative hungry-bone management:**
> "Children needed treatment with calcitriol, Ca and P supplementation for 6-12 weeks until PTH normalized and urinary Ca and P were detected, suggesting bone replenishment." (**PMID:21161280**) **[VERIFIED]**

Agents: furosemide `CHEBI:47426`; pamidronate `CHEBI:7903`; calcitriol `CHEBI:17823`; calcium(2+) `CHEBI:29108`. Action: `NCIT:C15747` *Supportive Care*; `NCIT:C15986` *Pharmacotherapy*.

**Anaesthetic/peri-operative care** is non-trivial in neonates with large tumours and chronic abdominal compartment syndrome (**PMID:36415355**) **[VERIFIED]**.

### 12.5 Radiotherapy

Reserved historically for unresectable/aggressive disease (**PMID:3037055**) and **essentially obsolete** in modern practice given the toxicity profile in neonates. `NCIT:C15313` *Radiation Therapy*.

### 12.6 Treatment Algorithm (synthesised)

```
Prenatal detection (3rd trimester)
  └─ polyhydramnios surveillance; tertiary-centre referral; prevent/anticipate preterm birth
Postnatal
  ├─ Age <3 months  → UPFRONT RADICAL NEPHRECTOMY (no biopsy, no preop chemo)
  └─ Age ≥3 months  → imaging ± biopsy; SIOP preop chemotherapy pathway as for Wilms
Pathology + mandatory molecular work-up
  ├─ pan-TRK IHC → ETV6 FISH/RT-PCR
  └─ if fusion-negative → NGS able to call intragenic ITD (EGFR exons 18–25, BRAF)
Stage I–II, complete resection, any subtype
  └─ Surgery alone + surveillance 18–24 months (imaging most intensive in first 12 months)
Stage III / incomplete resection / cellular or mixed
  └─ Consider adjuvant chemotherapy (benefit uncertain; weigh neonatal toxicity)
Relapse / metastasis
  ├─ Resect if operable (mainstay)
  ├─ NTRK fusion  → larotrectinib or entrectinib; monitor for TRK kinase-domain resistance mutations
  ├─ EGFR-ITD/KDD → EGFR TKI (afatinib) — investigational, single-case evidence
  └─ Chemotherapy only if inoperable (no survival advantage demonstrated)
```

### 12.7 Clinical Trials

No CMN-specific trial exists. Relevant trials are **histology-agnostic NTRK fusion baskets** that enrol infants: SCOUT (larotrectinib, paediatric, **NCT02637687**), NAVIGATE (larotrectinib, **NCT02576431**), STARTRK-NG (entrectinib, paediatric, **NCT02650401**), TRIDENT-1 (repotrectinib, **NCT03093116**). **[LEAD — NCT numbers from general knowledge of the TRK-inhibitor programme; verify each against ClinicalTrials.gov before citing in a knowledge base, and note that only TRIDENT-1 was confirmed in this review.]**

---

## 13. Prevention

- **Primary prevention: none possible.** CMN arises from a spontaneous somatic event in utero with no known modifiable cause. No vaccine, exposure reduction, or behavioural intervention applies.
- **Secondary prevention:** the only effective "prevention" is **prevention of complications through prenatal recognition**. Third-trimester detection enables tertiary-centre delivery planning and anticipation of preterm birth — the dominant source of perinatal morbidity (**PMID:36010301**).
- **Tertiary prevention:**
  - **Complete primary resection** — the single most effective action against relapse.
  - **Structured surveillance**: close clinical and radiological follow-up for ≥12 months (**PMID:28856451**); SIOP recommends 18–24 months of oncological surveillance plus long-term nephrology/late-effects follow-up **[PMC13210389]**.
  - **Accurate molecular diagnosis** prevents both under-treatment (missed CCSK — **PMID:23634181**) and over-treatment (chemotherapy for a classic EGFR-ITD tumour cured by surgery).
  - **Minimising neonatal treatment toxicity** is itself tertiary prevention, given that ~18% of deaths in the largest cohort were treatment-related.
- **Genetic screening / counselling:** **not applicable.** No carrier screening, no PGD, no prenatal genetic testing, and **no increased sibling or offspring risk**. Counselling content is reassurance that the tumour is sporadic and somatic.
- **Immunisation, public-health and environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

CMN is one of the few paediatric renal tumours with a documented **naturally occurring canine counterpart** — valuable as comparative pathology and, potentially, as a spontaneous large-animal model.

**Species:** *Canis lupus familiaris* — **`NCBITaxon:9615`** (verified).

**Case 1 — Basset Hound:**
> "An 18-month-old male basset hound was presented with vomiting, diarrhoea and depression... Histologically the mass was composed of neoplastic spindle cells forming interlacing fascicles, bundles and whorls, within a loose myxoid to dense collagenous stroma. Immunohistochemically neoplastic cells were positive for vimentin and smooth muscle actin. Based on these findings the tumour was diagnosed as a congenital mesoblastic nephroma, classical variant. After a two-and-a-half-year follow-up the dog was clinically healthy, indicating a benign behaviour."
> — Soldati et al., *J Small Anim Pract* 2012; **PMID:23020172** **[VERIFIED]**

**Case 2 — Entlebucher Mountain Dog (2026, the newest report):**
> "An intact 16-month-old female Entlebucher Mountain Dog... Immunohistochemically, neoplastic cells diffusely labelled for vimentin and partially for S-100 protein and p75NTR... The expression of p75NTR has not been described in this tumour entity before and its significance with regard to tumour promoting or tumour suppressing function or indication of a neurogenic differentiation remains undetermined. After a 3-year follow-up the dog was clinically healthy."
> — Lockow et al., *J Comp Pathol* 2026; **PMID:41265286** **[VERIFIED]**

**The p75NTR finding is mechanistically intriguing** and worth flagging: p75NTR (NGFR) is the low-affinity neurotrophin co-receptor that partners the TRK family, the same family whose kinase domain drives cellular CMN. Whether this reflects a shared neurotrophin-axis biology or is incidental is explicitly undetermined by the authors. **Do not over-interpret.**

**Breed (VBO):** Basset Hound and Entlebucher Mountain Dog — VBO identifiers not resolved in this review. **[NOT AVAILABLE]**

**Orthologous genes:** canine *EGFR*, *ETV6*, *NTRK3*, *BRAF* orthologs exist but **no molecular characterisation of canine CMN has been performed** — neither case was tested for ETV6::NTRK3 or EGFR ITD. **This is the obvious next experiment** and would establish whether the canine lesion is mechanistically homologous or merely morphologically convergent.

**Comparative pathology:** the canine tumours reproduce the classic human morphology (interlacing spindle fascicles, myxoid-to-collagenous stroma, vimentin+/SMA+) and the benign behaviour after nephrectomy. **Difference:** the dogs were 16–18 months old (young adult), not neonates, so the "congenital" framing is questionable in the canine setting — the authors of the 2026 report titled it "Mesoblastic nephroma", dropping "congenital", which is a deliberate and sensible choice.

**Zoonotic potential / transmission:** not applicable (neoplasm).

**Evolutionary conservation:** EGFR, ETV6, NTRK3 and BRAF are deeply conserved; the RTK→RAS→MAPK axis is conserved across vertebrates. The disease-level conservation remains untested.

---

## 15. Model Organisms

### 15.1 Available Models

**There is no mouse model of congenital mesoblastic nephroma.** This is the single largest experimental gap in the field. What exists are models of the *drivers* in other tissues:

**1. ETV6::NTRK3 conditional knock-in mouse (Li et al., *Cancer Cell* 2007; PMID:18068631)** **[SECONDARY]**
- Cre-Lox knock-in of the human NTRK3 PTK-domain cDNA into *Etv6* exon 6, with a floxed stop cassette
- Wap-Cre activation in mammary tissue → fully penetrant multifocal breast cancer, modelling human **secretory breast carcinoma**
- **Relevance to CMN:** establishes ETV6::NTRK3 as a bona fide transforming oncogene in vivo and provides a conditional allele that could, in principle, be driven by a **renal-stromal or metanephric-mesenchyme Cre** (e.g. Foxd1-Cre) to make the first genuine CMN model. **Nobody appears to have done this.**

**2. EPO-GEMM ETV6::NTRK3 sarcoma model (Imle et al., *Nat Commun* 2025; PMID:40523919)** — the newest and most relevant platform:
> "This EPO-GEMM (EPO-based genetically engineered mouse model) platform allows the generation of ten genetically distinct sarcomas on an isogenic background, **including the first model of ETV6::NTRK3-driven sarcoma**... Comparison of syngeneic allografting methods enables reliable preservation and scalability of sarcoma-EPO-GEMMs for preclinical treatment trials, such as **NTRK inhibitor therapy in an immunocompetent background**." **[VERIFIED]**

- **Method:** somatic gene delivery by **muscle electroporation** in wild-type mice — no germline engineering needed
- **Relevance to CMN:** this is the closest available model of the *cellular* CMN / infantile fibrosarcoma lesion, and it is explicitly built for **NTRK-inhibitor preclinical trials in an immunocompetent host** — directly relevant to the larotrectinib-resistance problem documented in **PMID:38984028**
- **Limitation:** it is a **muscle/soft-tissue sarcoma model, not a renal one.** It does not reproduce the kidney site, the neonatal developmental context, or the renal-sinus growth pattern. It models the oncogene, not the disease.

**3. ETV6-NTRK3 ALL models** (Blood 2018) — leukaemia, not relevant to CMN morphology but useful for TRK-inhibitor pharmacology. **[SECONDARY]**

**4. In vitro:** NIH 3T3 fibroblast transformation assays are the historical workhorse for ETV6::NTRK3 (demonstrating the IRS-1/IGF1R requirement and the RAS-MAPK/PI3K-AKT dual dependency). **[SECONDARY]**

**5. EGFR-KDD models:** Ba/F3 and lung-cancer cell line systems established constitutive activity and afatinib sensitivity (**PMID:26286086**) **[VERIFIED]**. **No EGFR-ITD renal or mesenchymal model exists.**

### 15.2 Phenotype Recapitulation and Limitations

| Model | Recapitulates | Fails to recapitulate |
|---|---|---|
| ETV6::NTRK3 knock-in (Wap-Cre) | Oncogenic transformation by the fusion in vivo; AP1-dependent mechanism | Kidney site; cell of origin; infant/neonatal context; morphology |
| EPO-GEMM ETV6::NTRK3 sarcoma | Fusion-driven spindle-cell sarcoma; immunocompetent setting; TRK-inhibitor response | Renal origin; congenital timing; classic-subtype biology entirely |
| EGFR-KDD Ba/F3 / lung lines | Constitutive EGFR activation; TKI sensitivity | Mesenchymal lineage; renal context; the infantile phenotype |
| Canine spontaneous CMN | Morphology, IHC, benign post-nephrectomy course, intact immune system | Not molecularly characterised; young-adult rather than neonatal onset; not experimentally tractable |

**What no model captures:** the **classic, EGFR-ITD subtype** — which is the *most common* form of CMN (41.5% of the SIOP cohort) — has **no in vivo model of any kind**. Given that MEK inhibition has been proposed for exactly this subtype on the basis of IHC alone (**PMID:39921750**), building one is the clear priority experiment.

### 15.3 Research Applications and Resources

- **Applications possible today:** NTRK-inhibitor efficacy and resistance (EPO-GEMM); fusion-driven transformation mechanism (knock-in, 3T3); EGFR-KDD pharmacology (Ba/F3).
- **Applications not possible today:** cell of origin; why the same fusion yields a renal tumour in one infant and a soft-tissue tumour in another; what determines the classic-vs-cellular morphological split; whether EGFR-ITD tumours are MEK-dependent.
- **Databases:** MGI (mouse alleles), IMSR/MMRRC (strain availability), Alliance of Genome Resources (orthology), OMIA (the canine cases should be submitted there if not already), Cellosaurus (no CMN-derived line identified).

---

## 16. Knowledge Gaps — Candidate `KNOWLEDGE_GAP` Discussions

For knowledge-base purposes, these are the open questions a curator should encode rather than paper over:

1. **Cell of origin is unknown.** The IHC evidence argues *against* a nephrogenic/urogenital origin (**PMID:27020209**), but no single-cell or lineage-tracing study has identified the progenitor. Attaches to: `pathophysiology#` origin node.
2. **No model of classic (EGFR-ITD) CMN exists**, despite it being the commonest subtype. `HUMAN_MODEL_MISMATCH` is the right kind for the EPO-GEMM link: a fusion-driven *muscle* sarcoma stands in for a congenital *renal* tumour.
3. **Why does the same ETV6::NTRK3 fusion give CMN in the kidney and infantile fibrosarcoma in soft tissue?** The two are arguably one entity (**PMID:9811336**); what determines the site is unknown.
4. **Why is EGFR-ITD essentially restricted to infant tumours?** It is ultra-rare in adult cancers and near-universal in classic CMN.
5. **Fusion-negative, EGFR-wild-type CMN** ("others" in the Lei classification) has no identified driver.
6. **Is MEK inhibition actually effective in EGFR-ITD CMN?** Proposed from IHC/transcriptomics only (**PMID:39921750**); zero clinical or in vivo data.
7. **Does the canine tumour carry the same drivers?** Two well-documented canine cases, neither sequenced.
8. **No long-term outcome cohort** for renal function, growth, or neurodevelopment in CMN survivors.
9. **Hypertension frequency is unresolved** — review literature quotes figures from "rare" to "80%" with no primary series adjudicating.
10. **No quality-of-life measurement** of any kind.

---

## 17. Curation Notes for Knowledge-Base Ingestion

- **Entry type:** `DISEASE`, bound to `MONDO:0017043`. The three morphological subtypes belong as **`has_subtypes`** rows (`Classic`, `Cellular`, `Mixed`), **not** as separate entries — they share an organ, an age, a surgical management, and a staging system, and differ on one axis (driver + relapse risk). Stratify phenotype, genetic and prevalence rows with `subtype:` foreign keys.
- **Cancer cell of origin** is **derived, not a slot**: mark the driver node with `genetic_context.variant_origin: SOMATIC` and `functional_impact_category: GAIN_OF_FUNCTION`, and bind `cell_types` there (`CL:0000186` *myofibroblast cell*). Be aware this entry will legitimately derive **more than one origin node** (EGFR-ITD and ETV6::NTRK3 branches) — that is the lump/split signal firing correctly on a genuinely two-driver disease, and the right response is the subtype structure above plus a note, not a split into two entries.
- **Module conformance candidates:** the hallmarks-of-cancer `sustaining_proliferative_signaling` module is the obvious target for both driver branches; `invasion_and_metastasis` for the cellular arm. Check `just list-modules` for a fusion-oncogene or RTK-activation module before creating anything new.
- **Do not curate** any `environmental:` block (see §5), any `inheritance:` block (see §9.2), or `HP:0001442`.
- **Verify before binding:** ORPHA:2665, the ICD-10/ICD-11 codes, the KLHL7 HGNC id, the VBO breed terms, all LOINC codes, and the NCT identifiers in §12.7. None of these was confirmed against an authoritative lookup in this review, and several were taken from search summaries.
- **Do not repeat** the "hypertension in 80% of CMN" claim or the "incidence 8 per million" figure without a primary source — both circulate widely in review literature and neither was traceable to a primary series here.

---

## Sources

**Primary literature (abstracts or full texts read during this review):**

- Quarello P, et al. Characteristics and outcome of congenital mesoblastic nephroma: a report of 376 patients registered in the SIOP 93-01, SIOP WT 2001, UK-IMPORT, and AIEOP protocols. *PLoS One* 2026. PMID:42189790. DOI:10.1371/journal.pone.0349345 — [PMC13210389](https://pmc.ncbi.nlm.nih.gov/articles/PMC13210389/)
- Gooskens SL, et al. Congenital mesoblastic nephroma 50 years after its recognition: a narrative review. *Pediatr Blood Cancer* 2017. PMID:28124468. DOI:10.1002/pbc.26437
- Wegert J, et al. Recurrent intragenic rearrangements of EGFR and BRAF in soft tissue tumors of infants. *Nat Commun* 2018;9:2378. PMID:29915264. DOI:10.1038/s41467-018-04650-6 — [PMC6006309](https://pmc.ncbi.nlm.nih.gov/articles/PMC6006309/)
- Zhao M, et al. Congenital mesoblastic nephroma is characterised by kinase mutations including EGFR internal tandem duplications, the ETV6–NTRK3 fusion, and the rare KLHL7–BRAF fusion. *Histopathology* 2020. PMID:32590884. DOI:10.1111/his.14194
- Vokuhl C, et al. ETV6–NTRK3 in congenital mesoblastic nephroma: a report of the SIOP/GPOH nephroblastoma study. *Pediatr Blood Cancer* 2018. PMID:29286563. DOI:10.1002/pbc.26925
- Lei L, et al. Recurrent EGFR alterations in NTRK3 fusion negative congenital mesoblastic nephroma. *Pract Lab Med* 2020. PMID:32490123. DOI:10.1016/j.plabm.2020.e00164
- Koo SC, et al. EGFR internal tandem duplications in fusion-negative congenital and neonatal spindle cell tumors. *Genes Chromosomes Cancer* 2023. PMID:35801295. DOI:10.1002/gcc.23087
- Chami R, Marrano P, Thorner PS. Pediatric fibromatosis lacks the internal tandem duplication of EGFR seen in congenital mesoblastic nephroma. *Genes Chromosomes Cancer* 2024. [DOI:10.1002/gcc.23266](https://onlinelibrary.wiley.com/doi/10.1002/gcc.23266)
- Hamada H, et al. Adjunctive diagnostic tool for histopathological classification of congenital mesoblastic nephroma based in molecular genetic findings. *J Cancer Res Clin Oncol* 2025;151:69. PMID:39921750. DOI:10.1007/s00432-025-06116-x
- Knezevich SR, et al. A novel ETV6-NTRK3 gene fusion in congenital fibrosarcoma. *Nat Genet* 1998. PMID:9462753. DOI:10.1038/ng0298-184
- Knezevich SR, et al. ETV6-NTRK3 gene fusions and trisomy 11 establish a histogenetic link between mesoblastic nephroma and congenital fibrosarcoma. *Cancer Res* 1998. PMID:9823307
- Rubin BP, et al. Congenital mesoblastic nephroma t(12;15) is associated with ETV6-NTRK3 gene fusion. *Am J Pathol* 1998. PMID:9811336
- El Demellawy D, et al. Congenital mesoblastic nephroma: a study of 19 cases using immunohistochemistry and ETV6-NTRK3 fusion gene rearrangement. *Pathology* 2016. PMID:27020209. DOI:10.1016/j.pathol.2015.11.007
- van der Beek JN, et al. Diagnostic MRI characteristics of congenital mesoblastic nephroma: a SIOP-RTSG radiology panel study. *Pediatr Radiol* 2024. PMID:38609702. [DOI:10.1007/s00247-024-05918-4](https://link.springer.com/article/10.1007/s00247-024-05918-4)
- Tongsong T, et al. Prenatal course and sonographic features of congenital mesoblastic nephroma. *Diagnostics (Basel)* 2022;12:1951. PMID:36010301. [DOI:10.3390/diagnostics12081951](https://www.mdpi.com/2075-4418/12/8/1951) — [PMC9406745](https://pmc.ncbi.nlm.nih.gov/articles/PMC9406745/)
- Chan HS, et al. Congenital mesoblastic nephroma: a clinicoradiologic study of 17 cases. *J Pediatr* 1987. PMID:3037055
- Jehangir S, et al. Recurrent and metastatic congenital mesoblastic nephroma: where does the evidence stand? *Pediatr Surg Int* 2017. PMID:28856451. [DOI:10.1007/s00383-017-4149-5](https://link.springer.com/article/10.1007/s00383-017-4149-5)
- Srivastava T, et al. Parathyroid-hormone-related protein-mediated hypercalcemia in benign congenital mesoblastic nephroma. *Pediatr Nephrol* 2011. PMID:21161280. DOI:10.1007/s00467-010-1728-2
- Vido L, et al. Congenital mesoblastic nephroma with hypercalcemia. Pathogenetic role of prostaglandins. *Am J Pediatr Hematol Oncol* 1986. PMID:3017143
- Tanné C, et al. Severe neonatal hypercalcemia revealing congenital mesoblastic nephroma. *Arch Pediatr* 2022. PMID:35039190. DOI:10.1016/j.arcped.2021.11.013
- Halalsheh H, et al. Dramatic bone remodeling following larotrectinib administration for bone metastasis in a patient with TRK fusion congenital mesoblastic nephroma. *Pediatr Blood Cancer* 2018. PMID:29893456. DOI:10.1002/pbc.27271
- Laetsch TW, Nagasubramanian R, Casanova M. Targeting NTRK fusions for the treatment of congenital mesoblastic nephroma. *Pediatr Blood Cancer* 2018. PMID:28440051. DOI:10.1002/pbc.26593
- Sun M, et al. Poor outcome in congenital mesoblastic nephroma with TPM3::NTRK1 fusion. *Transl Pediatr* 2024. PMID:38984028. DOI:10.21037/tp-24-126
- Li J, et al. Congenital mesoblastic nephroma: a single-center retrospective study. *Transl Pediatr* 2026. PMID:41810180. [DOI:10.21037/tp-2025-aw-770](https://tp.amegroups.org/article/view/149438/html)
- Gallant JN, et al. EGFR kinase domain duplication (EGFR-KDD) is a novel oncogenic driver in lung cancer that is clinically responsive to afatinib. *Cancer Discov* 2015. PMID:26286086. DOI:10.1158/2159-8290.CD-15-0654
- Imle R, et al. Somatic gene delivery faithfully recapitulates a molecular spectrum of high-risk sarcomas. *Nat Commun* 2025. PMID:40523919. DOI:10.1038/s41467-025-60519-5
- Li Z, et al. ETV6-NTRK3 fusion oncogene initiates breast cancer from committed mammary progenitors via activation of AP1 complex. *Cancer Cell* 2007. PMID:18068631 — [PMC2175032](https://pmc.ncbi.nlm.nih.gov/articles/PMC2175032/)
- Tognon CE, et al. A tripartite complex composed of ETV6-NTRK3, IRS1 and IGF1R is required for ETV6-NTRK3-mediated membrane localization and transformation. *Oncogene* 2012. DOI:10.1038/onc.2011.323
- Grosinger L, Salik I, Mehta B. Infantile congenital mesoblastic nephroma leading to multi-systemic end-organ disease. *Cureus* 2022. PMID:36415355. DOI:10.7759/cureus.30513
- Zakić H, et al. Coexisting congenital mesoblastic nephroma and lissencephaly. *Biomedicines* 2025. PMID:39857780. [DOI:10.3390/biomedicines13010196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11762540/)
- Alavi S, et al. Clear cell sarcoma of the kidney misdiagnosed as mesoblastic nephroma. *Ecancermedicalscience* 2013. PMID:23634181. DOI:10.3332/ecancer.2013.311
- Anakievski D, Ivanova P, Kitanova M. Laparoscopic management of congenital mesoblastic nephroma. *Urol Case Rep* 2019. PMID:31388496. DOI:10.1016/j.eucr.2019.100979
- Soldati S, et al. Congenital mesoblastic nephroma in a young basset hound dog. *J Small Anim Pract* 2012. PMID:23020172. DOI:10.1111/j.1748-5827.2012.01289.x
- Lockow S, et al. Mesoblastic nephroma in a young Entlebucher Mountain Dog. *J Comp Pathol* 2026. PMID:41265286. DOI:10.1016/j.jcpa.2025.11.001

**Databases, guidelines and secondary sources consulted:**

- [Orphanet — Congenital mesoblastic nephroma (ORPHA:2665)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=2665&Lng=GB)
- [Monarch Initiative — MONDO:0017043](https://monarchinitiative.org/MONDO:0017043)
- [WHO 2022 Classification of Tumours of the Urinary System and Male Genital Organs, Part A (European Urology)](https://www.europeanurology.com/article/S0302-2838(22)02467-8/fulltext); [ICD-O-3.2 update code list](https://www.alabamapublichealth.gov/ASCR/assets/ascr-2024-icd-o-3.2-update-codes-and-terms-numerical.pdf)
- [ICCR dataset for reporting paediatric renal tumours (PMC12232243)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232243/)
- [Rationale for the treatment of Wilms tumour in the UMBRELLA SIOP–RTSG 2016 protocol (*Nat Rev Urol*)](https://www.nature.com/articles/nrurol.2017.163)
- [NCI PDQ — Wilms Tumor and Other Childhood Kidney Tumors Treatment (Health Professional)](https://www.cancer.gov/types/kidney/hp/wilms-treatment-pdq)
- [Pathology Outlines — Congenital mesoblastic nephroma](https://www.pathologyoutlines.com/topic/kidneytumormesoblastic.html)
- [Atlas of Genetics and Cytogenetics in Oncology — Congenital mesoblastic nephroma](https://atlasgeneticsoncology.org/solid-tumor/209012/congenital-mesoblastic-nephroma)
- [FDA D.I.S.C.O. — Augtyro (repotrectinib) approval for NTRK fusion-positive solid tumors](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-disco-burst-edition-fda-approvals-augtyro-repotrectinib-ntrk-gene-fusion-positive-solid-tumors); [ASCO Post coverage, 13 June 2024](https://ascopost.com/issues/june-25-2024/fda-grants-accelerated-approval-to-repotrectinib-for-ntrk-fusion-positive-solid-tumors/)
- [Structure–function analysis of oncogenic EGFR kinase domain duplication](https://par.nsf.gov/biblio/10230524-structurefunction-analysis-oncogenic-egfr-kinase-domain-duplication-reveals-insights-activation-potential-approach-therapeutic-targeting)
- [ETV6-NTRK3 transformation requires IGF1R signaling (*Oncogene*)](https://www.nature.com/articles/1205669); [Cellular transformation and PI3K-Akt activation by ETV6-NTRK3 requires c-Src (*Cancer Res*)](https://aacrjournals.org/cancerres/article/67/7/3192/534559/Cellular-Transformation-and-Activation-of-the)
- [Congenital mesoblastic nephroma, renin production, and hypertension (PMID:2544716)](https://pubmed.ncbi.nlm.nih.gov/2544716/) — identified but not read
- Ontology CURIEs (HP, GO, CL, UBERON, CHEBI, NCIT, HGNC, MONDO, NCBITaxon) were verified against this repository's committed, ontology-derived term caches rather than written from memory; items explicitly flagged as unverified were not found in those caches and must be looked up at source before binding.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 68 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 35 |
| Quoted claims found in source | 33 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 68 |
| On topic | 23 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36010301` *(abstract only)*: "No single case has been diagnosed in the first half of pregnancy. No cases were detected during routine anomaly screening at mid-pregnancy. All cases were detected in the third trimester or late second trimester."
  - closest text in source: "Results: The findings derived from 41 cases of review are as follows: (1) No single case has been diagnosed in the first half of pregnancy"
- `PMID:42189790` *(abstract only)*: "we highlight that recurrences, though infrequent, tend to occur early and are not restricted to the cellular subtype. Of the 16 relapse cases, 8 were in the cellular subtype, 5 in the mixed subtype, and 3 in the classical subtype."
  - closest text in source: "While age at diagnosis, histological subtype, and survival outcomes are consistent with previous reports, we highlight that recurrences, though infrequent, tend to occur early and are not restricted to the cellular subtype"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1158/2159-8290.CD-15-0654` (1 mention) - <i>EGFR</i>
                    Kinase Domain Duplication (
                    <i>EGFR</i>
                    -KDD) Is a Novel Oncogenic Driver in Lung Cancer That Is Clinically Responsive to Afatinib
  - shared terms: cell, egfr

Weighed against this report's own most characteristic terms: `cmn`, `verified`, `tumour`, `cellular`, `congenital`, `renal`, `disease`, `ntrk3`, `etv6`, `cell`, `fusion`, `nephroma`, `classic`, `mesoblastic`, `egfr`, `secondary`, `subtype`, `mixed`, `egfr-itd`, `gene`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 97 |
| Resolved | 95 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C16722` (Immunohistochemistry) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000822` (2 mentions) - the report calls it "→ **neonatal hypertension"; HP calls it **Hypertension**, and lists "Arterial hypertension" among its other names
- `HP:0001392` (1 mention) - the report calls it "Abnormality of the liver (metastasis)"; HP calls it **Abnormality of the liver**
- `HP:0001635` (1 mention) - the report calls it "Congestive heart failure (high-output / compression)"; HP calls it **Congestive heart failure**
- `HP:0003811` (2 mentions) - the report calls it "Neonatal death", "Perinatal death"; HP calls it **Neonatal death**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003811` - called "Neonatal death", "Perinatal death"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

95 of 97 terms resolved to a current term; the rest could not be looked up either way.