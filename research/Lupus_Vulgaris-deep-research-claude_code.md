---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T02:02:42.037576'
end_time: '2026-11-26T02:06:28.809729'
duration_seconds: 226.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lupus Vulgaris
  mondo_id: MONDO:0006838
  category: Infectious Disease
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
  web_search_requests: 13
  num_turns: 21
  total_cost_usd: 1.041886625
  session_id: 5b9b2d74-622b-4984-99cb-9af65ead9d22
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 46
  retrieval_calls: 44
  assistant_text_blocks: 2
citation_count: 14
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 14
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:24770496
  quotes_not_checkable: 4
  relevance_assessed: 20
  on_topic: 11
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: EFO:1001023
    reported_labels:
    - EFO
    ontology_label: obsolete_lupus vulgaris
  - term_id: HP:0033349
    reported_labels:
    - positive tuberculin test, if available
    ontology_label: Seizure cluster
  labels_variant: 3
  obsolete_terms:
  - term_id: EFO:1001023
    ontology_label: obsolete_lupus vulgaris
    replaced_by: http://purl.obolibrary.org/obo/MONDO:0006838
  service_unreachable: 1
  obsolescence_unchecked: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lupus Vulgaris
- **MONDO ID:** MONDO:0006838 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lupus Vulgaris** covering all of the
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

I'm checking PMIDs and pulling exact abstract quotes for the main papers before I write the report.

# Lupus Vulgaris (MONDO:0006838): Disease Characteristics Report

**How I read the request:** Lupus vulgaris (LV) is an infectious disease. It is a chronic, paucibacillary form of cutaneous tuberculosis caused by *Mycobacterium tuberculosis* complex organisms. **It has no causal human gene.** The template records none, and I found no gene or OMIM entry attributed to LV. The only "causal" genome is that of the pathogen (*M. tuberculosis*, occasionally *M. bovis* or BCG). The genetic sections below are therefore marked mostly not applicable, with host-susceptibility context given only where I retrieved it. LV is also unrelated to systemic or cutaneous lupus erythematosus, despite the shared name.

**Retrieval limits:** PubMed abstract pages and Europe PMC were partly unavailable during this run (cookie walls and HTTP 503 errors), and a search on animal models was blocked. Each item below is labelled by how it was checked:
- **Verified** means I read the page or record and checked its identifiers.
- **Index** means the PMID or details come from a search-engine result, and I did not read the abstract.

---

## 1. Disease Information

**Overview**
- LV is "a chronic, progressive, paucibacillary form of cutaneous tuberculosis" (Behera et al., *Cureus* 2023, **PMID 37575838**, verified; https://pmc.ncbi.nlm.nih.gov/articles/PMC10420341/).
- "Lupus vulgaris is the most common form of cutaneous tuberculosis in adults" (Pai et al., *Indian Dermatol Online J* 2014, **PMID 25396129**, verified; https://pmc.ncbi.nlm.nih.gov/articles/PMC4228641).
- A 2026 review describes it as "the most common and indolent form in regions of moderate tuberculosis endemicity" (Knecht-Gurwin et al., *J Clin Med* 2026, **PMID 41598640**, verified; https://pmc.ncbi.nlm.nih.gov/articles/PMC12842349/).

**Identifiers**

| Resource | ID | How checked |
|---|---|---|
| MONDO | MONDO:0006838 "lupus vulgaris" | Verified via the OLS4 API |
| MeSH | D008177 "Lupus Vulgaris" | Verified via NLM MeSH lookup and the MONDO xref |
| UMLS | C0024131 | MONDO xref |
| SNOMED CT | 10528009 | MONDO xref |
| MedDRA | 10025143 | MONDO xref |
| MedGen | 9821 | MONDO xref |
| GARD | 0024483 | MONDO xref |
| EFO | EFO:1001023 | MONDO xref |
| ICD-11 foundation | 1292667822 | MONDO xref |
| ICD-10 | A18.4 (tuberculosis of skin and subcutaneous tissue) | Standard code; not retrieved this session |
| OMIM | None (not a Mendelian disorder) | — |
| Orphanet | No entry retrieved | — |

**MONDO definition (inherited from MeSH):** "A form of cutaneous tuberculosis. It is seen predominantly in women and typically involves the nasal mucosa; buccal mucosa; and conjunctival mucosa." This is verified text. Note that recent series report roughly equal sex ratios (Section 9).

**Synonyms:** MONDO lists none. In the literature, LV is also called "lupus vulgaris tuberculosis" and grouped as reinfection or post-primary cutaneous TB, a paucibacillary form.

**Source type:** All evidence is aggregated literature: case series and case reports. None comes from EHR-derived resources.

## 2. Etiology

**Causal factor**
- LV is caused by infection with *M. tuberculosis* complex organisms in a host who already has immunity to them.
- "Lupus vulgaris is caused by hematogenous, lymphatic, or contiguous spread from elsewhere in the body" (PMID 25396129, verified).
- It can also arise by direct inoculation, including from BCG vaccine: "Lupus vulgaris is a paucibacillary form of cutaneous tuberculosis that occurs either via hematogenous spread or direct inoculation" (Parmar et al., *An Bras Dermatol* 2021, **PMID 34272074**, verified).

**Risk factors**
- **Prior sensitisation.** LV "generally affects previously sensitized patients, who have a delayed, strongly positive hypersensitivity reaction to the tuberculin skin test" (Jaka-Moreno et al., *Actas Dermosifiliogr* 2012;103:251-3; https://actasdermo.org/en-lupus-vulgaris-caused-by-mycobacterium-articulo-S1578219012001047; PMID not retrieved).
- **Living in a TB-endemic area.** Indian series dominate the literature (Singal et al., *Int J Dermatol* 2022, DOI 10.1111/ijd.16267; PMID 35583803 per index).
- **Older age in Europe.** One source states that "in Europe, lupus vulgaris is characteristically a disease of elder people, whereas in developing countries younger persons are mostly concerned" (Springer case report, s13555-016-0158-x; search snippet only, paywalled).
- **Exposure to *M. bovis*.** This means contact with infected animals or ingestion of unpasteurised milk (Jaka-Moreno 2012).
- **BCG vaccination.** LV after BCG "occurs in 5 per million vaccinations" (PMID 34272074, verified). The risk is reportedly higher after repeated vaccination (search summary).
- **Immunosuppression and genetic susceptibility** have been proposed, but I retrieved no LV-specific data.

**Genetic risk factors:** No LV-specific genetic association study was found.
- Inborn errors of the IL-12/IFN-γ axis (IL12RB1, IFNGR1, IFNGR2, IL12B, STAT1) cause Mendelian susceptibility to mycobacterial disease (MSMD) and predispose to BCG and mycobacterial disease in general.
- Candidate-gene studies link SNPs in IFNG, IFNGR1, IL12A, IL12B, IL12RB1 and STAT4 to TB in general (e.g., https://pmc.ncbi.nlm.nih.gov/articles/PMC4930082; OMIM 601604).
- None of these studies examined LV directly.

**Protective factors**
- Pasteurisation of milk and eradication of bovine TB lowered the incidence of LV caused by *M. bovis* (Jaka-Moreno 2012).
- Effective treatment of underlying TB foci is also protective. No protective genetic variants are known.

**Gene–environment interaction:** No LV-specific data are available. The general principle is that the host's IFN-γ/Th1 competence shapes the clinical form that follows mycobacterial exposure (Santos et al., *An Bras Dermatol* 2014, **PMID 24770496**, verified): "The clinical manifestations are variable and depend on the interaction of several factors."

## 3. Phenotypes

| Phenotype | Suggested HPO term | Type | Frequency, onset and course | Source |
|---|---|---|---|---|
| Reddish-brown papules and nodules ("lupomas") that merge into plaques | HP:0200034 Papule; HP:0200036 Skin nodule; HP:0200035 Skin plaque | Sign | Defining feature. Plaque type was most common in Pai 2014, with 7 of 14 cases | PMID 25396129; PMID 37575838 ("Plaque-type lesions were most commonly encountered") |
| Apple-jelly colour on diascopy | No specific HPO term; use HP:0000951 Abnormality of the skin plus a free-text note | Sign | Characteristic but not pathognomonic | DermNet NZ (https://pro.dermnetnz.org/bacterial/tuberculosis.html) |
| Dermoscopy: yellow-orange structureless areas, linear and branching vessels, white scale | — | Sign / imaging | Common. Overlaps with sarcoidosis | Search summary of dermoscopy reviews (https://pmc.ncbi.nlm.nih.gov/articles/PMC7734991) |
| Scaling or hyperkeratosis | HP:0040189 Scaling skin | Sign | Variable | Same as above |
| Ulceration | HP:0200042 Skin ulcer | Sign | Ulcerative variant | Search summary of Pai 2014 |
| Atrophic scarring with central healing and peripheral extension | HP:0100699 Scarring; HP:0100679 Lack of skin elasticity / atrophy | Sign | Chronic, progressive | PMID 41598640 |
| Tissue destruction and disfigurement (nose, ear) | HP:0000453 Choanal atresia — **inappropriate**; use HP:0005288 Abnormality of the nose plus free text | Sign | Long-standing, untreated disease | PMID 41598640 ("irreversible tissue damage") |
| Strongly positive tuberculin skin test | HP:0033349 (positive tuberculin test, if available) | Laboratory | Typical | Jaka-Moreno 2012 |
| Non-caseating tuberculoid granulomas without acid-fast bacilli | — | Laboratory / histology | 100% in Behera 2023 | PMID 37575838 |
| Squamous cell carcinoma in the lesion | HP:0002860 Squamous cell carcinoma | Complication | 0.5–10.5% | PMID 31149488 |

**Severity and quality of life**
- Severity is usually mild systemically but can be locally destructive and disfiguring.
- I retrieved no EQ-5D, SF-36 or other validated quality-of-life data. Facial disfigurement is the main impact on quality of life (inferred).
- Onset is usually in adolescence or adulthood (Section 8).

## 4. Genetic/Molecular Information

**Not applicable.** No causal genes, pathogenic variants, ClinVar entries, modifier genes, epigenetic findings or chromosomal abnormalities have been reported for LV.
- The pathogen is the relevant genome: *M. tuberculosis* (NCBITaxon:1773) and *M. bovis* (NCBITaxon:1765).
- *M. bovis* "is inherently resistant to pyrazinamide" (PMID 34272074, verified). This has practical consequences for treatment.
- Multidrug-resistant LV has been reported (*Indian Dermatol Online J* 2017; DOAJ record https://doaj.org/article/7090fd94460d45a39e64692636f0db5e; PMID not retrieved).

## 5. Environmental Information

- **Infectious agents:** *M. tuberculosis* is the usual cause. *M. bovis* is rare: one review found 4 cases of *M. bovis* LV in 20 years (Jaka-Moreno 2012). Attenuated *M. bovis* BCG causes LV at vaccination sites (PMID 34272074; PMID 35024215, index).
- **Exposures:** Raw milk, infected cattle, and residence in TB-endemic regions.
- **Lifestyle factors:** No LV-specific data were retrieved for smoking, alcohol or diet.

## 6. Mechanism / Pathophysiology

**Ordered causal chain**

1. A person previously sensitised to *M. tuberculosis* complex, with a strongly positive tuberculin response, is exposed to mycobacteria (Jaka-Moreno 2012).
2. Bacilli reach the dermis by one of two routes:
   - 2a. Hematogenous or lymphatic spread, or contiguous extension, from an endogenous focus such as the lungs or lymph nodes (PMID 25396129).
   - 2b. Exogenous inoculation, including the BCG vaccination site (PMID 34272074).
3. Dermal macrophages ingest the bacilli. This **leads to** antigen presentation and activation of a Th1 / IFN-γ response. The response in TB "occurs basically via the Th1 pathway" (PMID 24770496). That this step operates in LV specifically is **inferred** from general TB immunology.
4. IFN-γ and TNF **result in** macrophages differentiating into epithelioid cells and Langhans giant cells, which form well-organised tuberculoid granulomas. This is the histology seen in all 19 cases of Behera 2023 (PMID 37575838).
5. Effective but incomplete containment **leads to** a paucibacillary state, in which bacilli are scarce or undetectable and culture is positive in fewer than 10% of cases (Jaka-Moreno 2012). The infection persists as a low-grade, chronic infection.
6. Chronic granulomatous inflammation **results in** papules and plaques that slowly spread at the edge while scarring and atrophy develop in the centre. Destruction of cartilage and soft tissue causes disfigurement over years to decades (PMID 41598640). The disease then branches:
   - 6a. Epidermal reaction leads to pseudoepitheliomatous hyperplasia, which gives hypertrophic or verrucous variants. Alternatively, the epidermis becomes atrophic.
   - 6b. Decades of inflammation and scarring can lead to malignant transformation, usually into squamous cell carcinoma, at a reported rate of 0.5–10.5% (PMID 31149488). The mechanism, a Marjolin-type tumour driven by chronic inflammation, is **inferred** from case reports.

**Checklist coverage**
- **Immune involvement:** Th1-polarised delayed-type hypersensitivity. "There are still no comparative studies of immune status across the clinical forms" (search summary of PMID 24770496).
- **Cellular processes:** GO:0002432 granuloma formation; GO:0042742 defense response to bacterium; GO:0032729 positive regulation of type II interferon (IFN-γ) production; GO:0042110 T cell activation.
- **Cell types:** CL:0000235 macrophage; CL:0000622 epithelioid cell (verify the term); multinucleated giant cell (CL:0000647, verify the ID); CL:0000545 T-helper 1 cell; CL:0000312 keratinocyte (hyperplasia and SCC); lymphocyte.
- **Omics, single-cell, spatial and CRISPR data:** None were retrieved for LV.

## 7. Anatomical Structures Affected

- **Primary organ:** skin of the head and neck (UBERON:0002097 skin of body). The face is most often involved: the nose (UBERON:0000004), cheek (UBERON:0001567) and ear (UBERON:0001690). The MONDO definition also lists nasal, buccal and conjunctival mucosa.
- **Neck:** Neck involvement is uncommon. The Turkish neck case (PMID 21738972, index) was described as the "fifth case in the literature".
- **Extremities and buttocks:** These are reported sites, especially in Indian series (Behera 2023; Pai 2014).
- **BCG-associated LV:** This occurs at the vaccination site, usually the deltoid skin (UBERON:0001482).
- **Tissue level:** dermis (UBERON:0002067) and epidermis (UBERON:0001003). Cartilage is affected in destructive disease.
- **Subcellular level:** phagosome / phagolysosome (GO:0045335, GO:0032010). This is inferred from the general biology of mycobacteria inside macrophages.
- **Laterality:** Usually a single, asymmetric plaque. Multifocal disease occurs.

## 8. Temporal Development

- **Onset:** Insidious and chronic. Diagnosis is often delayed:
  - The mean duration before diagnosis was 15.3 months in the Singal 22-year cohort.
  - A German *M. bovis* case was diagnosed about 20 years after onset (Springer, search snippet).
- **Course:** Slowly progressive over years to decades. Lesions extend at the edge and scar in the centre.
- **Long-standing disease:** SCC has arisen after more than 60 years (PMID 31149488) and after 50 years (PMID 20046107, index).
- **Spontaneous remission:** Rare and incomplete; scarring persists.
- **Remission with treatment:** Antitubercular therapy brings treatment-induced remission (Section 12).
- **BCG-associated LV:** Onset ranges from weeks to years after vaccination, with a reported mean of about 1 year (search summary).
- **Window for intervention:** Early treatment prevents disfigurement and malignant change (PMID 41598640).

## 9. Inheritance and Population

- **Inheritance:** Not applicable (infectious disease).
- **Burden in India:**
  - Cutaneous TB makes up about 0.1–2% of dermatology outpatient attendance in Indian reports (search summary).
  - LV accounted for 40.4% of 1,458 cutaneous TB patients over 22 years in Delhi, ahead of scrofuloderma (32.7%) and lichen scrofulosorum (15.2%). Of the cohort, 803 patients were children (Singal 2022).
  - In smaller series, LV made up 51% (19 of 37) of cutaneous TB in an Indian armed-forces series (https://pmc.ncbi.nlm.nih.gov/articles/PMC3221221) and is cited as 75% of cutaneous TB in Behera 2023.
- **Burden in Europe:** It is "the most common form of CTB in Europe and India" (PMID 24770496, body text). LV "was the most frequent clinical form of true skin tuberculosis until the 1960s" (PMID 31149488). In Europe it now mostly affects elderly people.
- **Sex ratio:**
  - Female-to-male ratio of 1.1:1 in Behera 2023.
  - Equal numbers of each sex in Pai 2014.
  - The MONDO/MeSH definition says LV is predominantly seen in women.
- **Age:** Adults predominate. Scrofuloderma is more common than LV in children (Pai 2014).
- **Population incidence:** No incidence or prevalence per 100,000 was retrieved.

## 10. Diagnostics

**Histopathology (the mainstay)**
- Tuberculoid granulomas made of epithelioid cells, Langhans giant cells and a lymphocytic rim, usually with little or no caseation.
- "Histologically it is charecterised by typical tubercles with or without caseation" (PMID 25396129; spelling as in the source).
- Behera 2023: "all showed a tuberculoid granuloma with no demonstration of acid-fast bacilli" (PMID 37575838).
- The epidermis may be atrophic or show pseudoepitheliomatous hyperplasia.

**Microbiology**
- Ziehl–Neelsen staining is usually negative.
- Culture is positive in fewer than 10% of cases (Jaka-Moreno 2012), but it identifies the species (e.g., *M. bovis*).
- Overall, "almost all of the diagnostic methods confer lower sensitivity and specificities" (Khadka et al., *Dermatol Res Pract* 2018, **PMID 30111996**, verified).

**Molecular tests**
- PCR on tissue has a reported positivity of about 60% in LV, taken from a literature table (search summary).
- Nested PCR on paraffin-embedded tissue was positive in 24 of 30 cutaneous TB samples, but only 2 of these were LV (PMID 30531542, index).
- PCR was negative in the culture-proven German *M. bovis* case.

**Immunological tests**
- The tuberculin skin test is strongly positive (Jaka-Moreno 2012).
- IGRA has not been studied specifically in LV in the sources retrieved.

**Bedside tests**
- Diascopy shows the apple-jelly sign.
- Dermoscopy shows yellow-orange structureless areas, which also occur in sarcoidosis.

**Imaging and other work-up**
- Chest X-ray is used to look for an underlying focus. No LV-specific yield data were retrieved.

**Therapeutic trial**
- When tests are inconclusive, a trial of antitubercular therapy is used diagnostically. The trial duration is debated (see the Ramam-type study in Section 12).

**Differential diagnosis**
- Cutaneous sarcoidosis, discoid lupus erythematosus, leprosy (tuberculoid), basal cell carcinoma, cutaneous leishmaniasis, deep fungal infection, granuloma faciale, and rosacea or granulomatous rosacea (DermNet; search summaries).

**Genetic testing**
- Not applicable. Consider MSMD gene testing (IL12RB1, IFNGR1, etc.) only if mycobacterial disease is disseminated or BCG-associated disease is severe. This is a general principle, not an LV-specific recommendation.

**Screening**
- Asymptomatic people are not screened for LV.

## 11. Outcome/Prognosis

- **Mortality:** LV itself rarely kills. No LV-specific survival or mortality data were retrieved.
- **Morbidity:** Scarring, mutilation of the nose and ears, and contractures.
- **Malignancy:**
  - SCC is the main malignant complication, at a reported rate of 0.5–10.5% (PMID 31149488).
  - "Chronic LV lesions persisting for decades may undergo malignant transformation" (PMID 41598640).
  - Basal cell carcinoma has also been reported (Vora et al., *IJDVL* 1995, per search summary).
  - SCC has also occurred in multidrug-resistant LV (IDOJ 2017).
- **Prognostic factors:** Long disease duration, delayed diagnosis, drug resistance, and tissue destruction (inferred from the case literature).
- **Recovery:** Good with therapy, with residual scarring. The German *M. bovis* case healed completely.

## 12. Treatment

**Pharmacotherapy**
- Standard antitubercular therapy follows WHO guidance: isoniazid, rifampicin, pyrazinamide and ethambutol until susceptibilities are known (search summary of CMAJ 2025, https://www.cmaj.ca/content/197/8/E215).
- Usual adult daily doses are isoniazid 5 mg/kg (maximum 300 mg), rifampicin 10 mg/kg (maximum 600 mg), pyrazinamide 20–25 mg/kg and ethambutol 15–20 mg/kg (dosing table, https://pmc.ncbi.nlm.nih.gov/articles/PMC2923933).
- India's ICMR Standard Treatment Workflow for skin TB is available at https://icmr.gov.in/icmrobject/uploads/STWs/1725964688_7_skin_tuberculosis_18032022.pdf. I did not read its content.
- Suggested NCIT terms: Isoniazid (C576), Rifampin (C787), Pyrazinamide (C774), Ethambutol (C61758). These codes are from memory; **verify them**.

**Treatment response**
- In a 2006 Indian study of 213 cutaneous TB patients on daily rifampicin plus isoniazid for 9 months, "ninety-two per cent of the patients showed resolution of the lesions within the first 6 months," and none relapsed over 3 years (Epistemonikos record https://www.epistemonikos.org/en/documents/1dd3a1455dc994b841da132b1d053ea46522b5aa; PMID not retrieved).
- BCG-related LV: treat for *M. bovis* resistance to pyrazinamide, since the organism is "inherently resistant to pyrazinamide and ethambutol is avoided in children due to its ophthalmologic side effects" (PMID 34272074).

**Surgery**
- "Surgical excision of residual or recalcitrant lesions are crucial to prevent complications" (PMID 41598640).
- Reconstructive surgery is used for deformities.
- SCC arising in LV is managed by excision.

**Historical treatment**
- Niels Finsen received the 1903 Nobel Prize "for treating diseases, especially lupus vulgaris, with concentrated light radiation" (https://www.nobelprize.org/prizes/medicine/1903/finsen/facts/). Antibiotics later replaced phototherapy.

**Gene, cell, RNA, targeted and immune therapies**
- Not applicable. No registered LV-specific trials (NCT numbers) were found.

**Adverse effects**
- These are the standard effects of antitubercular therapy: hepatotoxicity (isoniazid, rifampicin, pyrazinamide) and optic neuritis (ethambutol). This is general pharmacology, not retrieved specifically for LV.

## 13. Prevention

- **Primary prevention:**
  - TB control in general.
  - Milk pasteurisation and eradication of bovine TB, which reduced *M. bovis* LV (Jaka-Moreno 2012).
  - Good BCG technique and avoiding repeat BCG vaccination. BCG itself is a rare cause of LV, at about 5 per million doses.
- **Secondary prevention:** Early biopsy of chronic plaques on the face or neck, and early treatment.
- **Tertiary prevention:**
  - Complete the full course of antitubercular therapy.
  - Excise residual lesions.
  - Follow up long-standing lesions for a long time to catch SCC; the 50-year case authors argued for extended follow-up (PMID 20046107, index).
- **Genetic counselling:** Not applicable.

## 14. Other Species / Natural Disease

- No naturally occurring animal disease equivalent to LV was found (OMIA not applicable).
- **Zoonotic link:** Cattle (*Bos taurus*, NCBITaxon:9913) infected with *M. bovis* are a source of human LV through contact or raw milk (Jaka-Moreno 2012).
- Cutaneous tuberculosis in animals was not researched, because the search was blocked.

## 15. Model Organisms

- **No data were retrieved.** My search on animal models of cutaneous tuberculosis was refused by the tool, so I cannot cite any model of LV.
- I found no established genetic model (MGI, IMPC) that is specific to LV.
- General models of mycobacterial granulomas exist in mice, guinea pigs, rabbits and zebrafish, but I did not verify them this session. They should be sourced separately before they go into the knowledge base.

---

### Key verified citations
- Behera B et al. *Cureus* 2023. PMID 37575838
- Pai VV et al. *Indian Dermatol Online J* 2014. PMID 25396129
- Santos JB et al. *An Bras Dermatol* 2014. PMID 24770496
- Khadka P et al. *Dermatol Res Pract* 2018. PMID 30111996
- Knecht-Gurwin K et al. *J Clin Med* 2026. PMID 41598640
- Miyake T et al. *Int Cancer Conf J* 2017. PMID 31149488
- Parmar NV et al. *An Bras Dermatol* 2021. PMID 34272074

**Index-only, to verify:** PMIDs 20046107, 21738972, 35583803 (Singal 2022), 30531542, 35024215, 17350496.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 4 |
| References weighed for topical relevance | 20 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:24770496`: "occurs basically via the Th1 pathway"
  - closest text in source: "6 The immune response in tuberculosis occurs basically via Th1 pathway, with little or no involvement of Th2 pathway"
- `PMID:24770496`: "There are still no comparative studies of immune status across the clinical forms"
  - closest text in source: "Some case reports describe the patterns of the predominant cytokines for each clinical form, such as lupus vulgaris and tuberculosis verrucosa cutis, however there are still no comparative studies showing variance in the immune status in different forms of TB"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:34272074`: "Lupus vulgaris is a paucibacillary form of cutaneous tuberculosis that occurs either via hematogenous spread or direct inoculation"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:34272074`: "occurs in 5 per million vaccinations"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:34272074`: "is inherently resistant to pyrazinamide"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:34272074`: "inherently resistant to pyrazinamide and ethambutol is avoided in children due to its ophthalmologic side effects"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `EFO:1001023` (1 mention) - the report calls it "EFO"; EFO calls it **obsolete_lupus vulgaris**
- `HP:0033349` (1 mention) - the report calls it "positive tuberculin test, if available"; HP calls it **Seizure cluster**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `EFO:1001023` (obsolete_lupus vulgaris) (1 mention) - replaced by `http://purl.obolibrary.org/obo/MONDO:0006838`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1773` (1 mention) - the report calls it "M. tuberculosis"; NCBITaxon calls it **Mycobacterium tuberculosis**, and lists "Bacterium tuberculosis" among its other names
- `NCBITaxon:1765` (1 mention) - the report calls it "M. bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `UBERON:0002067` (1 mention) - the report calls it "Tissue level:** dermis"; UBERON calls it **dermis**, and lists "vertebrate dermis" among its other names

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `UBERON:0001003` (1 mention)

### Terms whose obsolescence could not be checked

2 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `GO:0045335` (1 mention)
- `NCBITaxon:9913` (1 mention)