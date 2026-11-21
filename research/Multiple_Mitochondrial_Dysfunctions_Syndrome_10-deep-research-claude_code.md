---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:21.597999'
end_time: '2026-11-18T23:34:28.292261'
duration_seconds: 246.69
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 10
  mondo_id: MONDO:0975806
  category: Mendelian
  causal_genes: CIAO1
  omim_id: OMIM:620960
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
  web_search_requests: 2
  num_turns: 20
  total_cost_usd: 0.8072427
  session_id: a7a4a7fd-2c10-412f-8e92-ae2253d9c7ec
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 19
  retrieval_calls: 18
  assistant_text_blocks: 3
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 10
reference_validation:
  total_references: 12
  verified: 11
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.8.0
term_validation:
  total_terms: 6
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0070737
    reported_labels:
    - Disease Ontology
    ontology_label: multiple mitochondrial dysfunctions syndrome 10
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 10
- **MONDO ID:** MONDO:0975806 (if available)
- **Causal gene(s):** CIAO1
- **OMIM:** OMIM:620960
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 10** covering all of the
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

Reading the primary papers on CIAO1/MMDS10 now (Maio 2024 JCI done; next the rest of that paper and the Genet Med 2024 report).

Checking IMPC mouse knockout data for Ciao1, then I'll write the report.

**Scope note:** This report covers MONDO:0975806 / OMIM:620960, which is caused by biallelic variants in **CIAO1**. Two primary papers, one preprint and several database records were retrieved. I could not reach OMIM, Orphanet or PubMed (blocked or 403), and could not confirm the MONDO ID or any HPO, GO, CL, UBERON or NCIT ID in this session. Ontology terms below are therefore given as labels only, to be mapped before entry. Several sections have no data for this disease and say so.

# Multiple Mitochondrial Dysfunctions Syndrome 10 (MMDS10): research report

## 1. Disease information

**Overview.** MMDS10 is a rare autosomal recessive disorder caused by loss-of-function variants in **CIAO1**, which encodes cytosolic iron-sulfur assembly component 1 (HGNC:14280; previous symbol WDR39; gene at 2q11.2). CIAO1 is the core WD40 protein of the cytosolic iron-sulfur protein assembly (CIA) machinery. The Disease Ontology record mirrored at MGI defines the condition as "a multisystem mitochondrial disorder" with proximal and axial muscle weakness, intermittently raised creatine kinase, respiratory insufficiency, and central nervous system features such as learning difficulties and neurobehavioral problems. It attributes the disease to compound heterozygous CIAO1 variants on 2q11 ([MGI/DO page](https://www.informatics.jax.org/disease/OMIM:620960)).

The founding report is Maio et al., *J Clin Invest* 2024;134(12):e179559, **PMID 38950322**, doi:10.1172/JCI179559. Its medRxiv preprint is **PMID 38196629**. The abstract states: "Our study identifies CIAO1 as a human disease gene" and "Lentivirus-mediated restoration of CIAO1 expression reversed all patient-derived cellular abnormalities." ([JCI](https://www.jci.org/articles/view/179559))

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| OMIM (disease) | 620960 | given in the brief; also in [UniProt O76071](https://rest.uniprot.org/uniprotkb/O76071.txt) |
| OMIM (gene) | 604333 | [HGNC](https://rest.genenames.org/fetch/symbol/CIAO1) |
| MONDO | 0975806 | given in the brief; not checked |
| Disease Ontology | DOID:0070737 | [MGI](https://www.informatics.jax.org/disease/OMIM:620960) |
| Orphanet | ORPHA:727296 | MGI cross-reference; the Orphanet page itself could not be reached |
| UMLS | C5975413 | MGI |
| ICD-10 / ICD-11 / MeSH | none found | no disease-specific codes retrieved |

**Synonyms.** MMDS10. The disease is also described as a "CIAO1-associated neuromuscular disorder". PanelApp shows this was its earlier label before it was renamed MMDS10 ([Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/207/gene/CIAO1/)).

**Evidence source.** Everything below comes from individual case reports with functional work: 4 patients in PMID 38950322, plus 2 CIAO1 patients in PMID 38411040. There are no EHR or registry data.

**Disputed spectrum.** van Karnebeek et al. (*Genet Med* 2024;26(6):101104, **PMID 38411040**, PMC11788579) describe 2 more CIAO1 patients with a much more severe, fatal neurodegenerative phenotype ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788579)). I could not confirm whether OMIM:620960 includes these patients. The knowledge-base entry should treat them as possibly part of the same allelic spectrum and flag that.

## 2. Etiology

- **Cause.** The disease is genetic: biallelic partial loss-of-function variants in CIAO1 (PMID 38950322). These impair maturation of iron-sulfur (Fe-S) proteins in the cytosol and nucleus. The mitochondrial dysfunction is described as secondary.
- **Genetic risk factors.** The only risk factor is carrying two pathogenic CIAO1 alleles. No GWAS or susceptibility loci were found.
- **Environmental risk factors.** None described.
- **Protective factors.** None described, genetic or environmental.
- **Gene-environment interactions.** None described. One possibility is unproven: affected cells show dihydropyrimidine dehydrogenase (DPYD) deficiency (Section 6). By analogy with DPD deficiency, fluoropyrimidine drugs could be dangerous. This is my inference and has not been reported for this disease.

## 3. Phenotypes

### Cohort A: Maio et al. 2024 (PMID 38950322)

Four unrelated patients, aged 17, 14, 25 and 59; mostly female (P1 male). Weakness began at about 1.5 to 17 years ([JCI](https://www.jci.org/articles/view/179559)).

| Phenotype | Suggested HPO label | Frequency | Characteristics |
|---|---|---|---|
| Proximal muscle weakness | Proximal muscle weakness | 4/4 | childhood/adolescent onset; slowly progressive |
| Axial weakness | Axial muscle weakness | 4/4 | slowly progressive |
| Mild facial and bulbar weakness | Facial muscle weakness; Bulbar weakness | reported (count not specified) | mild |
| Fatigability, low endurance | Exercise intolerance; Fatigable weakness | 4/4 | — |
| Joint hyperlaxity | Joint laxity | 4/4 | — |
| Ankle tightness | Ankle contracture / Achilles tendon contracture | 4/4 | — |
| Calf pseudohypertrophy | Calf muscle pseudohypertrophy | 3/4 (not noted in P2) | — |
| Elevated, fluctuating creatine kinase | Elevated circulating creatine kinase concentration | 4/4 | fluctuating (laboratory) |
| Respiratory insufficiency, FVC 51–63% predicted | Respiratory insufficiency; Restrictive ventilatory defect | 4/4 | — |
| Obstructive sleep apnea | Obstructive sleep apnea | 2/4 | — |
| Learning disability | Specific learning disability / Intellectual disability, mild | 4/4 | — |
| Neurobehavioral comorbidities | Behavioral abnormality | 2/4 | — |
| Progressive brain iron deposition (globus pallidus, substantia nigra, red nucleus, dentate nucleus) | Brain iron accumulation | 2/4 | progressive; absent on earlier scans |
| Mild normocytic-to-macrocytic anemia | Normocytic anemia / Macrocytic anemia | 2/4 | mild |
| Constipation and other GI symptoms | Constipation | 2/4 | — |
| Overweight | Overweight | 3/4 | — |
| Dystrophic muscle histology | Abnormal muscle fiber morphology; Increased variability in muscle fiber diameter; Muscle fiber necrosis | 4/4 | biopsy |
| Abnormal mitochondria in muscle on electron microscopy | Abnormal mitochondrial morphology | 2/2 examined | — |
| Reduced respiratory chain complex I, II and IV in muscle | Decreased activity of mitochondrial complex I / II / IV | P1 | — |

Findings that were absent in this cohort: cardiomyopathy (P4 had mild diastolic dysfunction only), neuropathy, eye involvement and hearing involvement.

### Cohort B: van Karnebeek et al. 2024 (PMID 38411040)

Two CIAO1 patients with a severe, fatal course ([PMC11788579](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788579)):

- **P1 (female).** Intrauterine growth restriction. Microcephaly from birth. Simplified gyral pattern on MRI at day 5. Multifocal sharp waves on EEG. Died at 18 months of bronchiolitis with bacterial and fungal superinfection.
- **P2 (male).** Failure to thrive with diarrhea in infancy, recurrent pneumonia, hyperkinetic movement disorder, autism spectrum disorder, and late muscle weakness leading to wheelchair use. Immunodeficiency was excluded. Died at 19 years of multi-organ failure.
- **Laboratory (both).** Markedly raised uracil and thymine in urine; also raised in plasma and CSF. DPYD gene was normal, but DPD enzyme activity was absent at 37 °C.
- **Suggested HPO labels.** Microcephaly; Abnormality of the cerebral gyri / Simplified gyral pattern; Recurrent respiratory infections; Uraciluria / Elevated urinary thymine; Autism; Hyperkinetic movements; Intrauterine growth retardation.

### Quality of life

No EQ-5D, SF-36 or other quality-of-life data exist. Wheelchair dependence (Cohort B, P2) and reduced respiratory capacity are the main functional burdens reported.

## 4. Genetic and molecular information

**Gene.** CIAO1: HGNC:14280; NCBI Gene 9391; Ensembl ENSG00000144021; UniProt O76071; OMIM 604333 ([HGNC](https://rest.genenames.org/fetch/symbol/CIAO1)). The protein is 339 amino acids with seven WD repeats and a LYR motif at residues 176–178 that is needed to bind HSC20 ([UniProt](https://rest.uniprot.org/uniprotkb/O76071.txt); PMID 29309586).

**Reported variants**

| Variant (protein) | cDNA (NM_004804) | Patients | Population frequency | Source |
|---|---|---|---|---|
| p.Arg65Trp | c.193C>T | Maio P2, P3; van Karnebeek P1, P2 | gnomAD AF about 1.0 × 10⁻³ | 38950322, 38411040 |
| p.His302Pro | not in retrieved text | Maio P1, P2, P3 | heterozygous only in gnomAD | 38950322 |
| p.Asp171Gly | not in retrieved text | Maio P4 | heterozygous only in gnomAD | 38950322 |
| p.His251Leu | not in retrieved text | Maio P4 | heterozygous only in gnomAD | 38950322 |
| Exon 7 deletion (p.F250_L339del) | structural | Maio P1, in trans with p.His302Pro | — | 38950322 |
| p.Trp184Cys | c.552G>C | van Karnebeek P2 | absent from gnomAD | 38411040 |
| p.His193Tyr | c.577C>T | van Karnebeek P1 | absent from gnomAD | 38411040 |

Notes on the variants:

- **Allelic configuration.** All patients are compound heterozygous or carry recurrent alleles in trans. Maio states the exon 7 deletion gives a transcript that undergoes nonsense-mediated decay, and RNA-seq confirmed reduced CIAO1 expression.
- **Variant classes.** Mostly missense, plus one large deletion.
- **Origin.** All germline. No somatic involvement has been described.
- **Functional effect.** Partial loss of function. The variant proteins are less stable than wild type: H302P and the other Maio missense variants in HeLa cells, and W184C and H193Y as recombinant proteins. R65W was not destabilized in the van Karnebeek assay. Maio also reports that the variants fail to recruit Fe-S recipient proteins.
- **ClinVar / ACMG classifications.** Not retrieved.

**Curation status.** PanelApp rates CIAO1 Green for this phenotype ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/207/gene/CIAO1/)). A secondary summary says GenCC lists the gene–disease link as "Limited", but I did not open the GenCC record myself.

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

## 5. Environmental information

No environmental, lifestyle or infectious causes are known. Infections act as complications and terminal events in Cohort B, not as causes.

## 6. Mechanism and pathophysiology

### Causal chain

1. Biallelic CIAO1 variants **lead to** unstable, reduced CIAO1 protein (shown in patient fibroblasts and HeLa cells; PMID 38950322, 38411040).
2. Loss of CIAO1 **results in** secondary loss of its CIA partners MMS19, FAM96B (CIAO2B) and FAM96A (CIAO2A) (shown in fibroblasts, PMID 38950322). This differs from acute siRNA knockdown.
3. The weakened CIA targeting complex **leads to** failed delivery of Fe-S clusters to cytosolic and nuclear client proteins (shown: reduced ⁵⁵Fe incorporation into POLD1). Iron supply and early Fe-S cluster assembly stay intact: mitochondrial ISC proteins, IRP1/2, ferritin and mitochondrial iron were all normal.
4. Unloaded client proteins **result in** lower levels of DPYD, POLD1, ERCC2 (XPD), ELP3, RTEL1 and CDKAL1 (shown).
5. The pathway then branches:
   - **5a. Pyrimidine catabolism.** DPYD deficiency **leads to** high uracil and thymine in urine, plasma and CSF (shown in Cohort B; DPYD activity impaired in Cohort A).
   - **5b. DNA replication, repair and genome maintenance.** Loss of POLD1, XPD and RTEL1 (and DNA2, per the abstract) **leads to** impaired DNA metabolism and reduced cell proliferation (proliferation defect shown in Cohort B fibroblasts). The link to neurodevelopmental features is *inferred*.
   - **5c. Muscle mitochondria.** In patient muscle, loss of nucleocytoplasmic Fe-S enzymes **results in** reduced respiratory chain subunits and lower activity of complexes I, II and IV. Ferrochelatase is moderately reduced, and lipoylated PDH and α-KGDH are mildly reduced. ACO2 and mitochondrial mass are unchanged. The authors call this secondary and say the direct cause "could not be definitively identified".
   - **5d. tRNA modification and translation.** Loss of ELP3 and CDKAL1 is expected to impair tRNA modification. The effect on disease is *inferred*.
   - **5e. Antiviral defense** (*hypothesis* from PMID 38411040). Failure of CIA-dependent antiviral factors **may lead to** the severe recurrent infections. Not demonstrated.
6. Steps 5b and 5c together **lead to** dystrophic myopathy with abnormal mitochondria, and so to proximal and axial weakness, raised CK and respiratory insufficiency (association shown, causation partly inferred).
7. Neurodegeneration **leads to** secondary iron deposition in deep brain nuclei, according to the authors' interpretation (inferred). The CNS involvement produces the learning and behavioral features, and in severe cases microcephaly and early death.

### Supporting detail

- **Pathway.** Cytosolic iron-sulfur protein assembly. CIAO1 forms the targeting complex with CIAO2B and MMS19 and links Fe-S maturation to DNA metabolism (Gari 2012, PMID 22678361; Stehling 2012, PMID 22678362; Stehling 2013, PMID 23891004). HSC20 connects de novo cluster biogenesis to CIAO1-mediated transfer (Kim 2018, PMID 29309586). CIAO1 is also part of the MMXD complex involved in chromosome segregation (Ito 2010, PMID 20797633).
- **Fibroblast omics (Cohort B).**
  - Proteomics: 283 of 2,347 proteins altered.
  - Metabolomics: changes in TCA cycle, nucleotide, amino acid and methionine–cysteine metabolism.
  - Lipidomics: 779 of 2,047 lipid species (38%) altered, with more polyunsaturated phosphatidylcholines and triacylglycerols.
- **Immune involvement.** MHC-I upregulation in muscle (Maio P2, P3) and macrophage foci in muscle. Recurrent infections in Cohort B without a demonstrable immunodeficiency.
- **Not studied.** Epigenetic changes, single-cell, spatial and CRISPR-screen data.
- **Suggested GO process labels.** Iron-sulfur cluster assembly; protein maturation by iron-sulfur cluster transfer; DNA repair; DNA replication; pyrimidine nucleobase catabolic process; mitochondrial respiratory chain complex assembly.
- **Suggested CL labels.** Skeletal muscle fiber (type 1 slow fibers most affected); neuron; fibroblast (model cell); erythroid lineage cell (anemia).
- **Suggested CHEBI labels.** Uracil; thymine; iron-sulfur cluster; iron.

## 7. Anatomical structures affected

- **Primary organs.** Skeletal muscle, both proximal limb and axial/paraspinal.
  - Muscle MRI shows sartorius involvement, selective fatty change in medial gastrocnemius, and hypertrophy of lateral gastrocnemius and soleus.
  - Brain: in Cohort A, the globus pallidus, substantia nigra, red nucleus and dentate nucleus; in Cohort B, the cerebral cortex (gyral simplification).
- **Secondary involvement.** Respiratory system, through a restrictive pattern and sleep apnea. Blood (anemia). Gastrointestinal tract. Heart only with mild diastolic dysfunction or septic cardiomyopathy as a terminal event.
- **Subcellular.** Cytoplasm, where CIAO1 is located (UniProt, PMID 23585563). Also the nucleus, where client proteins work, and secondarily the mitochondria, which are enlarged with whorled cristae. Suggested GO component labels: CIA complex; MMXD complex; cytosol; nucleus; mitochondrial inner membrane.
- **Laterality.** Muscle and brain findings are bilateral and symmetric.
- **UBERON IDs.** Not retrieved. Map from the labels above.

## 8. Temporal development

- **Onset.**
  - Milder form (Cohort A): childhood to adolescence, about 1.5 to 17 years, insidious.
  - Severe form (Cohort B): prenatal or neonatal, with intrauterine growth restriction and congenital microcephaly.
- **Course.**
  - Cohort A: slowly progressive weakness into adulthood; one patient was alive at 59. Brain iron deposition progressed between scans.
  - Cohort B: progressive neurodegeneration, with death at 18 months and at 19 years.
- **Remission, staging, critical periods.** None described.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive. Segregation was consistent with this in Maio P1 and P2.
- **Penetrance and expressivity.** Penetrance is unknown. Expressivity varies widely, from adult-surviving myopathy to infant death. The recurrent p.Arg65Trp allele appears in both mild and severe patients, so the second allele may set severity. That is my inference.
- **Anticipation, germline mosaicism, consanguinity.** None reported.
- **Founder effects.** p.His302Pro recurred in 3 unrelated patients; whether it reflects a founder effect was not established. p.Arg65Trp has an allele frequency of about 1 in 1,000 in gnomAD.
- **Prevalence and incidence.** Unknown. Six CIAO1 patients are published across the two cohorts.
- **Sex ratio.** Cohort A was mostly female; Cohort B was 1 female and 1 male. Too few cases to interpret.
- **Geography and ethnicity.** Not in the text I retrieved; Maio gives countries only in a figure.

## 10. Diagnostics

- **Laboratory.**
  - Serum creatine kinase: raised and fluctuating.
  - Urine, plasma and CSF uracil and thymine: raised in Cohort B. This is a useful clue, because a pyrimidine pattern of DPD deficiency with a normal DPYD gene points to a CIA defect.
  - DPD enzyme activity: impaired.
  - Full blood count: may show anemia.
- **Muscle biopsy.** Dystrophic changes with punctate COX- and SDH-strongly positive mitochondrial material in type 1 fibers. There are no COX-negative fibers. Electron microscopy shows abnormal, enlarged mitochondria. Respiratory chain enzyme assays show reduced complexes I, II and IV.
- **Imaging.** Muscle MRI and ultrasound show the pattern in Section 7. Brain MRI with T2, SWI or QSM detects iron deposition.
- **Lung function and sleep.** Spirometry (FVC) and polysomnography.
- **Genetic testing.**
  - Exome or genome sequencing was diagnostic in all published cases.
  - CIAO1 is on Genomics England and Australian neuromuscular panels ([PanelApp AU](https://panelapp-aus.org/panels/206/gene/CIAO1)).
  - Look for copy-number and exon deletions, such as the exon 7 deletion.
  - RNA-seq helped confirm the deletion's effect.
  - Mitochondrial DNA testing excluded mtDNA variants and deletions in Maio P1.
- **Differential diagnosis.**
  - Limb-girdle and congenital muscular dystrophies.
  - Other MMDS and Fe-S disorders, such as NFU1, BOLA3, IBA57 and ISCA2. These primary mitochondrial ISC defects usually show lipoate and complex I/II defects.
  - Primary DPD deficiency (DPYD variants).
  - MMS19 deficiency, which has a similar severe phenotype.
  - Neurodegeneration with brain iron accumulation disorders.
- **Diagnostic criteria and screening.** No formal criteria and no newborn screening. Cascade carrier testing is possible once familial variants are known.

## 11. Outcome and prognosis

- **Survival.** Survival data are too sparse for rates. Cohort A patients are alive at 14–59 years. Both Cohort B patients died, at 18 months (respiratory infection) and at 19 years (multi-organ failure).
- **Main causes of illness and death.** Respiratory insufficiency, recurrent respiratory infections, and progressive neurological impairment.
- **Prognostic factors.** None validated. Early-onset microcephaly or brain malformation appears to predict a fatal course.
- **Quality-of-life measures.** None published.

## 12. Treatment

- **Disease-specific therapy.** None. The only evidence of reversal is preclinical: lentiviral CIAO1 restored CIA components, client Fe-S proteins, POLD1 iron loading and DPYD activity in patient cells (PMID 38950322). Suggested NCIT label: Gene Therapy (preclinical only).
- **Symptomatic treatment reported.** Phenobarbital for EEG abnormalities. Ventilatory support, antibiotics and bronchoalveolar lavage, which failed in Cohort B P1.
- **Supportive care (inferred from the phenotype, not trial-based).**
  - Respiratory monitoring and non-invasive ventilation for restrictive disease or sleep apnea.
  - Physiotherapy and orthotics for ankle contractures.
  - Educational support.
  - Infection prophylaxis or vaccination.
- **Pharmacogenomic caution (inference).** Patients have DPD deficiency, so 5-fluorouracil and capecitabine would be expected to be toxic. This has not been reported for CIAO1 patients.
- **Clinical trials.** No ClinicalTrials.gov entries were retrieved or found.

## 13. Prevention

- **Primary prevention.** Genetic counseling with a 25% recurrence risk per pregnancy for carrier parents. Carrier testing of relatives. Prenatal or preimplantation genetic testing once both familial variants are known.
- **Secondary and tertiary prevention.** Surveillance of respiratory function, sleep, blood counts and infections. Avoiding fluoropyrimidines (inference, as above).
- **Population or newborn screening programs.** None.

## 14. Other species and natural disease

- **Naturally occurring disease in animals.** No OMIA entry was found; none is known.
- **Conservation.** CIA function is conserved from yeast Cia1 (crystal structure: Srinivasan 2007, PMID 17937914) to vertebrates, and Maio notes conservation of the variant residues in zebrafish.
- **Orthologs.** Mouse Ciao1 is MGI:1346998 ([MGI](https://www.informatics.jax.org/marker/MGI:1346998)). The zebrafish ortholog is ciao1; its ZFIN gene ID was not retrieved.
- **Zoonotic potential.** None.

## 15. Model organisms

- **Zebrafish (van Karnebeek 2024).** The ciao1 del26/del26 loss-of-function mutant has reduced body length and head size at 14 days post-fertilization. Homozygous larvae start dying at 13 days and are all dead by 17 days (n = 10). DPD protein is reduced. The model reproduces the microcephaly, early lethality and DPD loss, but not the adult myopathy. mms19 mutants were also made, with abnormalities in adults ([PMC11788579](https://pmc.ncbi.nlm.nih.gov/articles/PMC11788579); [ZFIN pub](https://zfin.org/ZDB-PUB-240227-9)).
- **Mouse.**
  - MGI lists 7 Ciao1 alleles (targeted, gene-trap, chemically induced and radiation-induced) and 21 IMSR lines.
  - IMPC currently shows no phenotype data: 0 of 24 physiological systems tested ([IMPC](https://www.mousephenotype.org/data/genes/MGI:1346998)).
  - Maio notes that only a knockout of the partner gene Mms19 has been described, and it dies before implantation.
  - No published Ciao1 disease-model mouse was found.
- **Cellular models.** Patient fibroblasts, with lentiviral rescue. HeLa cells for protein stability and siRNA work. Patient muscle tissue.
- **Yeast.** Cia1 studies are the basis for the biochemistry (PMID 17937914).
- **Limitations.**
  - Fibroblasts show no respiratory chain defect, because they rely on glycolysis in high-glucose medium.
  - Muscle work used only n = 2 replicates.
  - No animal model reproduces the slowly progressive myopathy.

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 38950322 | Maio N et al. *J Clin Invest* 2024;134(12):e179559 | human clinical + in vitro |
| 38196629 | Maio N et al. medRxiv preprint, 2023 | preprint of the above |
| 38411040 | van Karnebeek CDM et al. *Genet Med* 2024;26(6):101104 | human clinical, omics, zebrafish |
| 22678361 | Gari K et al. *Science* 2012 | MMS19–CIA link to DNA metabolism |
| 22678362 | Stehling O et al. *Science* 2012 | same topic |
| 23891004 | Stehling O et al. *Cell Metab* 2013 | CIA2A/CIA2B and iron homeostasis |
| 23585563 | Seki M et al. *J Biol Chem* 2013 | IOP1 (CIAO3) in human CIA |
| 29309586 | Kim KS et al. *Hum Mol Genet* 2018 | HSC20 and CIAO1-mediated transfer |
| 20797633 | Ito S et al. *Mol Cell* 2010 | MMXD complex |
| 17937914 | Srinivasan V et al. *Structure* 2007 | yeast Cia1 structure |

Other sources: [MGI/DO disease page](https://www.informatics.jax.org/disease/OMIM:620960) · [HGNC](https://rest.genenames.org/fetch/symbol/CIAO1) · [UniProt O76071](https://rest.uniprot.org/uniprotkb/O76071.txt) · [Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/207/gene/CIAO1/) · [PanelApp Australia](https://panelapp-aus.org/panels/206/gene/CIAO1) · [IMPC](https://www.mousephenotype.org/data/genes/MGI:1346998) · [ZFIN](https://zfin.org/ZDB-PUB-240227-9)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

11 of 12 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0070737` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **multiple mitochondrial dysfunctions syndrome 10**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.