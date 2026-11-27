---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T15:17:55.452028'
end_time: '2026-11-25T15:23:50.379791'
duration_seconds: 354.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: RTTN-Related Microcephalic Primordial Dwarfism
  mondo_id: MONDO:0018764
  category: Mendelian
  causal_genes: RTTN
  omim_id: OMIM:614833
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
  num_turns: 16
  total_cost_usd: 0.9974006400000002
  session_id: 249db535-3e6d-405c-a5d2-04368de9a5e5
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 31
  retrieval_calls: 29
  assistant_text_blocks: 3
citation_count: 13
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:30879067
  relevance_assessed: 25
  on_topic: 19
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 49
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 22
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0018764
    reported_labels:
    - cross-referenced in GARD
    ontology_label: microcephalic primordial dwarfism due to RTTN deficiency
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  service_unreachable: 21
  obsolescence_unchecked: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RTTN-Related Microcephalic Primordial Dwarfism
- **MONDO ID:** MONDO:0018764 (if available)
- **Causal gene(s):** RTTN
- **OMIM:** OMIM:614833
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RTTN-Related Microcephalic Primordial Dwarfism** covering all of the
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

I'm gathering primary literature: I have the key papers, and I'm pulling their PMIDs and abstract quotes.

Europe PMC returned all 25 hits (`hitCount` 25, pageSize 40, so no second page). The API did not fail, so I did not use the fallback URL. The source is not on the preapproved list, so quotes are capped at 125 characters, and titles are shortened where they run longer.

**Read:** https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:RTTN%20OR%20TITLE:rotatin)&resultType=core&pageSize=40&format=json (offsets 0, 39849, 79698, 119547, 139849). Verbatim text covers the first 179,698 of 211,275 characters. The last ~31.5k was only model-summarized, which covers four records (Grandone, Kheradmand Kia, Chatterjee, Faisst). Their metadata is unverified and I have no verbatim abstract for them.

**Corrections to your PMIDs:**
- PMID 29967526 is Wambach JA 2018 (Pediatr Res), not Cavallin. Cavallin 2018 is **30121372**.
- PMID 30121372 is Cavallin, not Stouffs. Stouffs 2018 is **29883675**.

**All 25 results (newest first)**

| # | PMID | First author | Year | Title (shortened where marked) | Journal |
|---|---|---|---|---|---|
| 1 | none (bioRxiv, PPR1300567) | Hadar A | 2026 | "RTTN moonlights beyond the centrosome to control ribosome biogenesis and tRNA modification in human brain organoids" | bioRxiv (preprint) |
| 2 | 41524969 | Sun J | 2026 | "Uncovering the oncogenic role of RTTN in melanoma pathogenesis and its therapeutic implications." | Mol Biol Rep |
| 3 | 41719742 | Guguin J | 2026 | "Generation of the iPSC line CRNLi001-A from a patient with microcephaly..." (shortened) | Stem Cell Res |
| 4 | 40151166 | Gins C | 2025 | "Radial Microbrain (Micrencephaly) Is Caused by a Recurrent Variant in the RTTN Gene." | Neurol Genet |
| 5 | 39680576 | Guguin J | 2024 | "A Taybi-Linder syndrome-related RTTN variant impedes neural rosette formation in human cortical organoids." | PLoS Genet |
| 6 | none (medRxiv, PPR832522) | Guguin J | 2024 | "A TALS-like RTTN mutation impedes neural rosette formation in human cortical organoids" | medRxiv (preprint) |
| 7 | 38178912 | Romano F | 2023 | "Case Report: Novel biallelic moderately damaging variants in RTTN in a patient with cerebellar dysplasia." | Front Pediatr |
| 8 | 37371259 | Mudassir BU | 2023 | "Microcephaly, Short Stature, Intellectual Disability, Speech Absence and Cataract..." (shortened; Seckel-like case report) | Children (Basel) |
| 9 | 34207628 | Chou EJ | 2021 | "Human Microcephaly Protein RTTN Is Required for Proper Mitotic Progression and Correct Spindle Position." | Cells |
| 10 | 34012324 | Imran Naseer M | 2021 | "Exome sequencing reveled a compound heterozygous mutations in RTTN gene..." (shortened) | Saudi J Biol Sci |
| 11 | 33510049 | Cho DG | 2021 | "Anastral Spindle 3/Rotatin Stabilizes Sol narae and Promotes Cell Survival in Drosophila melanogaster." | Mol Cells |
| 12 | 30946475 | Uzquiano A | 2019 | "Rotatin' the phenotypes." (a Comment on PMID 30879067) | Brain |
| 13 | 30927481 | Zakaria M | 2019 | "Primary microcephaly, primordial dwarfism, and brachydactyly in adult cases with biallelic skipping of RTTN exon 42." | Hum Mutat |
| 14 | 30879067 | Vandervore LV | 2019 | "Heterogeneous clinical phenotypes and cerebral malformations reflected by rotatin cellular dynamics." | Brain |
| 15 | 30168418 | Sydor AM | 2018 | "PPP1R35 is a novel centrosomal protein that regulates centriole length in concert with the microcephaly protein RTTN." | eLife |
| 16 | 30121372 | Cavallin M | 2018 | "Recurrent RTTN mutation leading to severe microcephaly, polymicrogyria and growth restriction." | Eur J Med Genet |
| 17 | 29967526 | Wambach JA | 2018 | "Functional characterization of biallelic RTTN variants identified in an infant with microcephaly..." (shortened) | Pediatr Res |
| 18 | 29883675 | Stouffs K | 2018 | "Biallelic mutations in RTTN are associated with microcephaly, short stature and a wide range of brain malformations." | Eur J Med Genet |
| 19 | 29356416 | Chartier S | 2018 | "A neuropathological study of novel RTTN gene mutations causing a familial microcephaly with simplified gyral pattern." | Birth Defects Res |
| 20 | 28811500 | Chen HY | 2017 | "Human microcephaly protein RTTN interacts with STIL and is required to build full-length centrioles." | Nat Commun |
| 21 | 26940245 | Grandone A | 2016 | "Expanding the phenotype of RTTN variations..." (shortened; summary-only) | Clin Genet |
| 22 | 26608784 | Shamseldin H | 2015 | "RTTN Mutations Cause Primary Microcephaly and Primordial Dwarfism in Humans." | Am J Hum Genet |
| 23 | 22939636 | Kheradmand Kia S | 2012 | "RTTN mutations link primary cilia function to organization of the human cerebral cortex." (summary-only) | Am J Hum Genet |
| 24 | 17551791 | Chatterjee B | 2007 | "Nt mutation causing laterality defects associated with deletion of rotatin." (summary-only) | Mamm Genome |
| 25 | 11900971 | Faisst AM | 2002 | "Rotatin is a novel gene required for axial rotation and left-right specification in mouse embryos." (summary-only) | Mech Dev |

**Verbatim abstract quotes (each under 125 characters)**

Records not listed here have no verbatim abstract in the read text. Kheradmand Kia 2012, Grandone 2016, Faisst 2002 and Chatterjee 2007 fall in that group, and I have not quoted them.

- Shamseldin 2015 (26608784): "Our results expand the phenotype of RTTN-related disorders, hitherto limited to polymicrogyria" and "RT-PCR confirmed that this change creates a cryptic splice donor"
- Cavallin 2018 (30121372): "We identified, by trio based whole exome sequencing, a homozygous missense mutation in the RTTN gene"
- Stouffs 2018 (29883675): "We here report three individuals from two unrelated families with novel mutations in the RTTN gene."
- Vandervore 2019 (30879067): "We show that the severity of the phenotype is related to residual function of the protein"
- Chen HY 2017 (28811500): "RTTN directly interacts with STIL and acts downstream of STIL-mediated centriole assembly"
- Guguin 2024 PLoS Genet (39680576): "In cortical organoids, we discovered an additional function of RTTN in the self-organisation of NSC into neural rosettes"
- Chou 2021 (34207628): "Here, we show that RTTN is required for normal mitotic progression and correct spindle position."
- Gins 2025 (40151166): "Our data show that the homozygous c.2953A>G substitution in RTTN is a recurrent variant responsible for radial microbrain" (HTML tags removed)
- Hadar 2026 preprint: "Our findings redefine RTTN as a regulator of ribosome homeostasis and mRNA translation"
- Sun 2026 (41524969): "RTTN is significantly upregulated in melanoma tissues and cell lines compared to normal controls"
- Guguin 2026 iPSC (41719742): "This line represents a useful tool to study RTTN deficiency in tissue development, notably the brain."

**Your specific asks**
- Kheradmand Kia 2012, Grandone 2016, Faisst 2002: no verbatim abstract was readable (summary only). Please check PubMed for the abstracts.
- Zebrafish: none in these 25 results.
- Mouse: Faisst 2002 and Chatterjee 2007 (summary only).
- iPSC/organoid: Guguin 2024 (PLoS Genet and preprint), Guguin 2026, and Hadar 2026.
- Drosophila: Cho 2021.
- 2020–2026 (11 records): Hadar, Sun, Guguin 2026, Gins, Guguin 2024 (×2), Romano, Mudassir, Chou, Imran Naseer, Cho.
- Not present in these results: Sirisi 2023, CEP295, MOPD, or any PPP1R35 paper after 2018 (Sydor 2018 is the only PPP1R35 record).

**Interpretation and scope.** This report covers MONDO:0018764 / OMIM:614833, the autosomal recessive disorder caused by biallelic variants in **RTTN** (rotatin; OMIM gene 610436). OMIM calls it "Microcephaly, short stature, and polymicrogyria with or without seizures" and Orphanet calls it "Microcephalic primordial dwarfism due to RTTN deficiency" (ORPHA:468631). Both describe one RTTN-related spectrum.

**Retrieval limits.** PubMed pages could not be loaded in this session, so PMIDs and abstract content come from the Europe PMC REST API and PMC full texts.
- Quotes marked **[verbatim]** were read directly from those sources.
- Content marked **[summary]** comes from a model-generated summary of a record I could not read verbatim. Check it before curating it.
- The reported 125-character limit on quotes from non-preapproved sources means the quotes here are short excerpts, not full abstract sentences.
- I did not retrieve HGNC, gnomAD, ClinVar or ICD codes for this condition. Fields that depend on them are marked as not retrieved, not filled from memory.

---

## 1. Disease Information

**Overview.** This is an autosomal recessive neurodevelopmental disorder caused by biallelic RTTN variants. Its core features are:
- primary (congenital) microcephaly;
- pre- and/or postnatal growth restriction, which can amount to primordial dwarfism;
- intellectual disability, often with absent speech;
- a range of cortical malformations: polymicrogyria, lissencephaly/pachygyria, simplified gyral pattern, periventricular heterotopia, and hypoplasia of the corpus callosum and vermis;
- seizures in some patients.

The disorder was first described as bilateral diffuse polymicrogyria (Kheradmand Kia 2012, PMID 22939636). The phenotype was then extended to microcephalic primordial dwarfism (Shamseldin 2015, PMID 26608784). Shamseldin et al. wrote: *"Our results expand the phenotype of RTTN-related disorders, hitherto limited to polymicrogyria"* [verbatim].

Vandervore et al. 2019 (PMID 30879067) reviewed 23 published and 5 unpublished cases. They defined a core phenotype of intellectual disability, short stature, microcephaly and cortical malformations, and reported that *"the severity of the phenotype is related to residual function of the protein"* [verbatim].

GARD describes moderate to severe intellectual disability and global developmental delay, with short stature that can be severe ([GARD](https://rarediseases.info.nih.gov/assets/singles/17841.json)).

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0018764 (cross-referenced in GARD) |
| OMIM phenotype | 614833 |
| OMIM gene | 610436 (RTTN) ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/RTTN)) |
| Orphanet | ORPHA:468631 ([GARD](https://rarediseases.info.nih.gov/assets/singles/17841.json); [NORD/MONDO page](https://rarediseases.org/mondo-disease/microcephalic-primordial-dwarfism-due-to-rttn-deficiency/)) |
| ICD-10 / ICD-11 / MeSH | Not retrieved. No disease-specific code was found. |

**Synonyms**
- Microcephaly, short stature, and polymicrogyria with or without seizures (MSSP / MMPSS, OMIM)
- Microcephalic primordial dwarfism due to RTTN deficiency (Orphanet)
- RTTN-related primary microcephaly
- Polymicrogyria with seizures (historical label for the RTTN p.L932F family)

**Data provenance.** The information comes from aggregated case reports and small case series, not from EHR cohorts.

## 2. Etiology

**Causal factors**
- Germline biallelic (homozygous or compound heterozygous) loss- or reduction-of-function variants in RTTN.
- The effects are mainly hypomorphic: missense, splice, and deep-intronic or cryptic-splice variants.
- Vandervore 2019 linked severity to residual rotatin function (PMID 30879067).

**Genetic risk factors**
- Parental consanguinity recurs throughout the reported families: Kheradmand Kia 2012, Shamseldin 2015, Grandone 2016 [summary], and Zakaria 2019, whose consanguineous family had three affected adults (PMID 30927481).
- **Recurrent variant c.2953A>G, p.(Arg985Gly) (NM_173630.4, exon 23):**
  - first reported in a Moroccan patient (Cavallin 2018, PMID 30121372);
  - later found in 5 of 50 individuals in a microcephaly series and in 2 fetuses (Gins 2025, PMID 40151166);
  - also found in a patient with a Taybi-Linder syndrome–like phenotype (Guguin 2024, PMID 39680576).
- No modifier genes have been described.

**Environmental risk factors, protective factors and gene–environment interactions.** None have been reported. This is a monogenic disorder, and CTD or GWAS data are not relevant.

## 3. Phenotypes

The frequencies below come from the 28-case table in Vandervore 2019 (PMID 30879067; [Oxford Academic table](https://academic.oup.com/view-large/134257786)), as relayed by search summaries. Denominators are the individuals assessed.

| Phenotype | Suggested HPO term | Frequency | Onset / course |
|---|---|---|---|
| Primary microcephaly | HP:0011451 Primary microcephaly | 17/21 (81%) | Congenital. Can be extreme: radial microbrain, with fetal cortical plate reduced about 70% (PMID 40151166) |
| Primordial dwarfism / IUGR | HP:0003561 Birth length less than 3rd percentile; HP:0001511 Intrauterine growth retardation | 7/20 (35%) | Prenatal onset |
| Postnatal short stature | HP:0004322 Short stature | 10/23 (43%) | Childhood; stable |
| Lissencephaly / pachygyria | HP:0001339 Lissencephaly; HP:0001302 Pachygyria | 11/23 (48%) | Congenital |
| Polymicrogyria / dysgyria / schizencephaly | HP:0002126 Polymicrogyria | 7/23 (30%) | Congenital |
| Seizures | HP:0001250 Seizure | 4/23 (17%) | Infancy or childhood. Intractable epilepsy is noted in radial microbrain |
| Intellectual disability / global developmental delay | HP:0001249; HP:0001263 | Core feature, near-universal. Moderate to severe (GARD) | Lifelong |
| Absent speech | HP:0001344 | All 5 patients with p.R985G in Gins 2025 | Lifelong |
| Stereotypies | HP:0000733 | 5/5 in Gins 2025 | — |
| Corpus callosum hypoplasia, vermis hypoplasia, colpocephaly | HP:0002079; HP:0001320; HP:0030048 | Reported (Stouffs 2018, PMID 29883675) | Congenital |
| Periventricular / neuronal heterotopia | HP:0007165 | Reported (PMID 30879067; 40151166) | Congenital |
| Simplified gyral pattern | HP:0009879 | Fetal neuropathology (Chartier 2018, PMID 29356416 [summary]) | Prenatal |
| Pontocerebellar hypoplasia | HP:0012110 | Single infant (Wambach 2018, PMID 29967526 [summary]) | Neonatal |
| Cerebellar dysplasia | HP:0007033 | Case report (Romano 2023, PMID 38178912; title only) | — |
| Brachydactyly | HP:0001156 | 3 adults (PMID 30927481) | Stable to age 60 |
| Dermatitis | HP:0011123 | One family (Grandone 2016, PMID 26940245 [summary]) | — |
| Cataract | HP:0000518 | Seckel-like case (Mudassir 2023, PMID 37371259; title only) | — |

**Quality of life.** No formal QoL measures (EQ-5D, SF-36, PROMIS) have been reported. The main driver of lifelong dependence is severe intellectual disability with absent speech.

## 4. Genetic / Molecular Information

**Gene.** RTTN, rotatin (OMIM 610436). The HGNC ID was not retrieved.

**Function:**
- RTTN is a centrosomal and centriolar protein.
- It localizes to the basal body and ciliary axoneme (PMID 30879067).
- It *"directly interacts with STIL and acts downstream of STIL-mediated centriole assembly"* (Chen 2017, PMID 28811500) [verbatim].
- It forms a complex with PPP1R35 and acts upstream of it in centriole elongation (Sydor 2018, PMID 30168418; [eLife](https://elifesciences.org/articles/37846)).

**Reported pathogenic variants (examples)**

| Variant | Type | Phenotype / source |
|---|---|---|
| p.(Leu932Phe), homozygous | Missense | Polymicrogyria with seizures, consanguineous Turkish family (Kheradmand Kia 2012, PMID 22939636, per OMIM summary) |
| Intronic variant creating a cryptic splice donor | Splice | MPD: *"RT-PCR confirmed that this change creates a cryptic splice donor"* (PMID 26608784) [verbatim] |
| c.2953A>G, p.(Arg985Gly), homozygous | Missense that also alters exon 23 splicing | Recurrent variant in Moroccan families; severe microcephaly/PMG/growth restriction (PMID 30121372) and radial microbrain (PMID 40151166) |
| c.5648-5T>A, homozygous | Splice; exon 42 skipping → p.Ala1883Glyfs*6 | MPD with brachydactyly in adults (PMID 30927481) |
| p.(Ala578Pro) | Missense | Reduced STIL binding; blocks centriole duplication (PMID 28811500 [summary]) |
| Compound heterozygous variants | Various | PMIDs 29356416, 29967526, 34012324, 38178912 |

**ClinVar/ACMG classifications and gnomAD frequencies were not retrieved.**
- Variants are germline.
- The functional consequence is partial loss of function (hypomorphic).
- Complete loss is presumed incompatible with life, by inference from the embryonic lethality of the mouse knockout (PMID 11900971).

**Not reported:** modifier genes, epigenetic alterations, and chromosomal abnormalities.

## 5. Environmental Information

Not applicable. No environmental, lifestyle or infectious contributors have been reported.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. Biallelic hypomorphic RTTN variants (missense or splice) **lead to** reduced or mislocalized rotatin protein. Severity correlates with residual function (PMID 30879067; human fibroblasts).
2. Reduced rotatin **impairs** centriole elongation downstream of STIL-mediated procentriole assembly, so centrioles are short or incomplete (PMID 28811500; 30168418; human cell lines). The PPP1R35 complex and CEP295-mediated loading of distal centriole proteins also act in this step.
3. Defective centrioles **result in** centrosome amplification, γ-tubulin dispersion, and monopolar or multipolar spindles. They also cause fewer and shorter astral microtubules and loss of NuMA/p150Glued from the cortex, which misorients the spindle (Chou 2021, PMID 34207628; *"RTTN is required for normal mitotic progression and correct spindle position"* [verbatim]). The same defects are seen in patient fibroblasts (PMID 30879067).
4. Mitotic failure **leads to** aneuploidy, cell-cycle arrest and apoptosis of neural stem and progenitor cells. This was shown in CRISPR-edited iPSC-derived neural stem cells (PMID 39680576).
5. **Branch A:** loss of neural stem cells **results in** a reduced radial glial scaffold (50% loss of radial glial columns) and a thinner cortical plate (about 70% thinner) in fetuses with p.R985G (PMID 40151166). The outcome is **primary microcephaly / radial microbrain**. Delayed polarization and rosette formation in organoids is a further early defect (PMID 39680576: *"an additional function of RTTN in the self-organisation of NSC into neural rosettes"* [verbatim]).
6. **Branch B:** basal body and cilia defects (fewer and shorter primary cilia) **impair** ciliary signalling. Patient fibroblasts showed reduced BMP4, WNT5A and WNT2B expression (PMID 22939636, per OMIM summary; PMID 29967526 [summary]). The link to **cortical patterning defects and polymicrogyria** is inferred.
7. **Branch C:** rotatin sits at the leading-edge centrosome of migrating iPSC-derived neurons and binds non-muscle myosin heavy chains (PMID 30879067). Loss of this function is proposed to cause **defective neuronal migration**, leading to lissencephaly and heterotopia. This step is inferred from localization and interaction data.
8. Systemic proliferation defects across tissues **are presumed to cause** pre- and postnatal growth restriction (primordial dwarfism). This is inferred by analogy with other centrosomal MPD genes and has not been shown directly.
9. **Emerging and unconfirmed:** a 2026 bioRxiv preprint (Hadar et al.) proposes that RTTN regulates ribosome biogenesis, tRNA modification and mRNA translation in brain organoids.

**Suggested GO terms**
- GO:0007099 centriole replication
- GO:0061511 centriole elongation
- GO:0060271 cilium assembly
- GO:0007052 mitotic spindle organization
- GO:0040001 establishment of mitotic spindle localization
- GO:0001764 neuron migration
- GO:0021987 cerebral cortex development
- GO:0007368 determination of left/right symmetry (from the mouse model)

**Suggested CL terms**
- CL:0000681 radial glial cell
- CL:0000047 neuronal stem cell
- CL:0011020 neural progenitor cell
- CL:0000540 neuron
- CL:0000057 fibroblast (patient cell model)

**Not available:** metabolic, immune, transcriptomic or proteomic disease signatures. The one exception is the rotatin interactome reported in PMID 30879067.

## 7. Anatomical Structures Affected

- **Primary organ:** brain, especially the cerebral cortex (UBERON:0000955; UBERON:0000956). Also affected:
  - corpus callosum (UBERON:0002336);
  - cerebellar vermis (UBERON:0004720);
  - pons and cerebellum in some cases.
- **Systemic:** skeletal growth, with short stature and brachydactyly (hand, UBERON:0002398). The eye (cataract) and skin (dermatitis) are involved in isolated reports.
- **Cells:** see the CL terms in Section 6.
- **Subcellular locations (GO cellular component):**
  - centriole (GO:0005814)
  - centrosome (GO:0005813)
  - ciliary basal body (GO:0036064)
  - axoneme (GO:0005930)
  - spindle pole (GO:0000922)
- **Laterality:** cortical malformations are bilateral and diffuse (bilateral diffuse PMG). Human laterality defects have not been reported, in contrast to the mouse.

## 8. Temporal Development

- **Onset:** congenital or prenatal. Microcephaly and abnormal gyration can be detected in fetuses (PMID 29356416; 40151166).
- **Course:** a static neurodevelopmental disorder. Features stayed stable into the seventh decade in the exon-42 family (PMID 30927481).
- **Critical period:** cortical neurogenesis in the first and second trimesters (inferred).
- **Remission:** none.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM; PanelApp).
- **Prevalence and incidence:** unknown. About 28 cases had been reported by 2019 (PMID 30879067), and further cases have been reported since. The disorder is ultra-rare (fewer than 1/1,000,000, inferred from case counts).
- **Penetrance:** apparently complete for biallelic variants.
- **Expressivity:** highly variable, from isolated PMG to MPD to radial microbrain, partly explained by residual function.
- **Consanguinity:** frequent.
- **Founder or recurrent allele:** p.R985G in Moroccan/North African families (PMID 30121372; 40151166). Its haplotype status was not retrieved.
- **Other populations reported:** Turkish, Saudi Arabian (PMID 26608784; 34012324) and Pakistani (PMID 37371259) families.
- **Sex ratio:** no bias expected; 4 of the 5 radial microbrain patients were female.
- **Not reported:** carrier frequency, anticipation and germline mosaicism.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing is first-line, by trio WES in Cavallin 2018 and Gins 2025. RTTN is on Genomics England PanelApp panels for:
  - microcephaly (primordial dwarfism panel 162);
  - malformations of cortical development (panel 96);
  - early onset or syndromic epilepsy (panel 402).
- **RNA studies:** RT-PCR of patient fibroblast RNA is valuable because splice and deep-intronic variants are common (PMID 26608784; 30927481; 30879067).
- **Functional assay:** patient fibroblasts show reduced cilium number and length, which has been proposed as a way to support variant pathogenicity (PMID 29967526 [summary]).
- **Imaging:** brain MRI and prenatal ultrasound or MRI show microcephaly and PMG, pachygyria, simplified gyration or heterotopia.
- **Neuropathology:** fetal brains show a thin cortical plate, loss of radial glial columns and heterotopia (PMID 40151166; 29356416).
- **EEG:** used for seizures.
- **Differential diagnosis:**
  - other primary microcephaly genes (MCPH; e.g., ASPM, WDR62, CENPJ, STIL);
  - Seckel syndrome;
  - MOPD II (PCNT);
  - Taybi-Linder syndrome (RNU4ATAC), which an RTTN case phenocopied (PMID 39680576);
  - tubulinopathies;
  - congenital infections such as CMV and Zika, which also cause microcephaly with PMG.
- **No standardized diagnostic criteria exist, and no newborn screening is available.**

## 11. Outcome / Prognosis

- **Survival:** has not been quantified.
  - Survival into adulthood (ages 43–60) is documented (PMID 30927481).
  - Radial microbrain is described as often leading to early lethality through intractable epilepsy (PMID 40151166 discussion, via search summary).
  - Some pregnancies were terminated after fetal diagnosis (PMID 29356416; 40151166).
- **Morbidity:** severe intellectual disability, absent speech and dependence in daily living.
- **Prognostic factors:** residual RTTN function and the severity of the cortical malformation (PMID 30879067).
- **Not available:** biomarkers and formal QoL data.

## 12. Treatment

No disease-specific, gene, RNA or cell therapy exists, and no trials were found. Care is supportive:
- antiseizure medication (NCIT: Anticonvulsant Agent);
- growth and nutritional monitoring;
- physical, occupational and speech therapy (NCIT: Physical Therapy; Speech Therapy);
- developmental and educational support.

No pharmacogenomic data or treatment-outcome data were found.

## 13. Prevention

- No primary prevention exists.
- Options are genetic counseling with a 25% recurrence risk for carrier parents, carrier testing of relatives, and prenatal or preimplantation genetic testing once familial variants are known. Prenatal fetal diagnosis is documented (PMID 29356416; 40151166).
- Consanguinity counseling is relevant in affected communities.
- Vaccines, prophylaxis and public-health measures do not apply.

## 14. Other Species / Natural Disease

- **Natural disease:** none reported in OMIA searches (not specifically retrieved).
- **Orthologs:**
  - mouse *Rttn* (MGI:2179288; [MGI](https://www.informatics.jax.org/marker/MGI:2179288));
  - *Drosophila* *ana3* (Anastral spindle 3).
- **Conservation:** Ana3 is *"required for the structural integrity of both centrioles and basal bodies"* (Stevens 2009, PMID 19948479) [verbatim]. Ana3 is not needed for centriole duplication but is needed for centriole cohesion and for basal bodies in sensory neurons ([JCB](https://rupress.org/jcb/article/187/3/355/35607/Ana3-is-a-conserved-protein-required-for-the)). This conserved centriole and cilium role across flies, mice and humans supports the mechanism.
- **Zoonotic potential:** none.

## 15. Model Organisms

| Model | Findings | Recapitulation |
|---|---|---|
| Mouse *Rttn* insertional knockout (Faisst 2002, PMID 11900971 [summary]; MGI) | Embryonic lethality with failed axial rotation. Abnormal nodal/lefty/Pitx2 expression and randomized heart looping. Delayed neural tube closure | Poor for the human brain phenotype: null alleles are lethal and laterality defects are not seen in patients. Shows that rotatin is essential |
| Mouse *Nt* ("no turning") mutation (Chatterjee 2007, PMID 17551791 [summary]) | Laterality defects linked to a deletion that includes *Rttn* | As above |
| *Drosophila ana3* (PMID 19948479; Cho 2021, PMID 33510049) | Centriole and basal body integrity, male sterility, loss of sensory cilia. Ana3 stabilizes Sol narae and promotes cell survival | Mechanistic only |
| Patient fibroblasts (PMID 22939636; 29967526; 30879067) | Cilia defects, mitotic failure, centrosome amplification, aneuploidy | Cellular phenotypes |
| RPE1 / U2OS RTTN-depletion lines (PMID 28811500; 34207628) | Short centrioles, spindle defects | Mechanistic |
| CRISPR iPSC-derived neural stem cells and cortical organoids carrying p.R985G (PMID 39680576); patient iPSC line CRNLi001-A (PMID 41719742) | Neural stem cell death, aneuploidy, delayed rosette formation, small organoids | Good for microcephaly |
| Unrelated finding | RTTN upregulated in melanoma (PMID 41524969) | Not relevant to this disease |

**Gaps:**
- No zebrafish or conditional (brain-specific) mouse model was found.
- A conditional or hypomorphic mouse allele would be needed to model the cortical phenotype.

---

**Key sources:**
- PMIDs (Europe PMC records): 22939636, 26608784, 26940245, 28811500, 29356416, 29883675, 29967526, 30121372, 30168418, 30879067, 30927481, 34207628, 39680576, 40151166, 41719742, 11900971, 17551791, 19948479
- [Gins 2025, PMC11949245](https://pmc.ncbi.nlm.nih.gov/articles/PMC11949245)
- [Chen 2017, PMC5558016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5558016)
- [Sydor 2018, eLife](https://elifesciences.org/articles/37846)
- [Vandervore 2019, Erasmus repository PDF](https://repub.eur.nl/pub/118248/REPUB_118248-OA.pdf)
- [Vandervore 2019 phenotype table](https://academic.oup.com/view-large/134257786)
- [GARD](https://rarediseases.info.nih.gov/assets/singles/17841.json)
- [NORD/MONDO page](https://rarediseases.org/mondo-disease/microcephalic-primordial-dwarfism-due-to-rttn-deficiency/)
- [PanelApp](https://panelapp.genomicsengland.co.uk/panels/96/gene/RTTN/)
- [MGI](https://www.informatics.jax.org/marker/MGI:2179288)
- [Stevens 2009, PMC2779252](https://pmc.ncbi.nlm.nih.gov/articles/PMC2779252)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 25 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30879067` *(abstract only)*: "Rotatin' the phenotypes."
  - Text part not found as substring: 'Rotatin' the phenotypes.' (note: only abstract available for PMID:30879067, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 22 |
| Terms whose name was checked | 9 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018764` (2 mentions) - the report calls it "cross-referenced in GARD"; MONDO calls it **microcephalic primordial dwarfism due to RTTN deficiency**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000733` (1 mention) - the report calls it "Stereotypies"; HP calls it **Motor stereotypy**, and lists "Stereotyped" among its other names

### Terms the ontology service could not be reached for

21 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `ORPHA:468631` (2 mentions)
- `HP:0011451` (1 mention)
- `HP:0003561` (1 mention)
- `HP:0012110` (1 mention)
- `HP:0011123` (1 mention)
- `GO:0007099` (1 mention)
- `GO:0061511` (1 mention)
- `GO:0060271` (1 mention)
- `GO:0040001` (1 mention)
- `CL:0000681` (1 mention)
- `CL:0000047` (1 mention)
- `CL:0000540` (1 mention)
- `CL:0000057` (1 mention)
- `UBERON:0000955` (1 mention)
- `UBERON:0000956` (1 mention)
- `UBERON:0004720` (1 mention)
- `GO:0005814` (1 mention)
- `GO:0005813` (1 mention)
- `GO:0036064` (1 mention)
- `GO:0005930` (1 mention)
- `MGI:2179288` (4 mentions)

### Terms whose obsolescence could not be checked

7 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0030048` (1 mention)
- `HP:0007165` (1 mention)
- `HP:0001156` (1 mention)
- `CL:0011020` (1 mention)
- `UBERON:0002336` (1 mention)
- `UBERON:0002398` (1 mention)
- `GO:0000922` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.