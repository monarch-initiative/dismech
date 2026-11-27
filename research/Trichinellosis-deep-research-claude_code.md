---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T20:05:01.433510'
end_time: '2026-11-25T20:08:57.234727'
duration_seconds: 235.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Trichinellosis
  mondo_id: MONDO:0019444
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Trichinella disease or disorder; Trichinella infectious disease; Trichinella
    caused disease or disorder; trichinosis
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
  web_search_requests: 27
  num_turns: 33
  total_cost_usd: 1.5425420000000003
  session_id: dcc50d4a-6cc1-4cfe-ba4f-e13be765a3ab
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 32
  retrieval_calls: 27
  assistant_text_blocks: 3
citation_count: 20
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 4
  quotes_unsupported: 8
  unsupported_quote_references:
  - PMID:19136437
  - PMC:PMC2620635
  - PMID:2797874
  - PMC:PMC1742236
  - PMC:PMC2753907
  quotes_not_checkable: 1
  relevance_assessed: 30
  on_topic: 10
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 58
  verified: 50
  not_found: 1
  obsolete: 1
  unverifiable: 6
  confabulation_rate: 0.019
  labels_checked: 15
  labels_matching: 6
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0019444
    reported_labels:
    - MONDO
    ontology_label: trichinellosis
  - term_id: NCIT:C61633
    reported_labels:
    - Albendazole
    ontology_label: Amiloride
  - term_id: NCIT:C62031
    reported_labels:
    - Mebendazole
    ontology_label: Granisetron
  labels_variant: 6
  unresolved_terms:
  - UBERON:0035537
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  unresolvable_prefixes:
  - ORPHA
  service_unreachable: 5
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trichinellosis
- **MONDO ID:** MONDO:0019444 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Trichinella disease or disorder; Trichinella infectious disease; Trichinella caused disease or disorder; trichinosis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Trichinellosis** covering all of the
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

Let me try PubMed E-utilities directly for primary literature.

Bash can't reach the network here, so I'm using web search for the literature. Next I'm looking up the mechanism, immunology, diagnosis, genomics and burden sources.

I have enough sources now and am writing the report.

# Trichinellosis (MONDO:0019444): Disease Characteristics Research Report

**Scope and limitations.** This report covers human trichinellosis, the infection caused by nematodes of the genus *Trichinella*. It is an infectious disease, so **there is no human causal gene**. The template has no causal gene or OMIM entry recorded, and that is correct. The "causal genes" are those of the parasite.

Command-line access to PubMed (E-utilities) was blocked in this session. All sources come from web searches. PMIDs are given only where a search result showed them. Other sources are cited by PMC ID, DOI or URL. Short quotes are taken from the text the searches returned. Many template sections (variant classification, CMA, karyotyping, gene therapy and similar) do not apply to a parasitic infection and are marked as such.

---

## 1. Disease Information

**Overview.** Trichinellosis is "a worldwide zoonosis caused by the parasitic nematodes belonging to the Trichinella genus" (Bruschi & Dupouy-Camet 2022, https://doi.org/10.1007/978-3-031-00303-5_10). People are infected by "ingestion of Trichinella larvae encysted in the muscle tissue of domestic or wild animal meat" (Gottstein, Pozio & Nöckler, *Clin Microbiol Rev* 2009;22:127–145, PMID 19136437, PMC2620635). The key clinical difficulty is that early diagnosis is hard, because "pathognomonic signs or symptoms are lacking" (PMID 19136437).

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0019444 | NCBI MedGen C0040896 (https://ncbi.nlm.nih.gov/medgen/C0040896) |
| Orphanet | ORPHA:863 | MedGen cross-reference (not checked on Orphanet itself) |
| ICD-10 | B75 (Trichinellosis) | https://aapc.com/codes/icd-10-codes/B75 |
| ICD-11 | 1F6E (Trichinosis) | CISMeF (https://www.cismef.org/page/detail/en/ICD11_CA_284613639); worth checking in the WHO browser |
| MeSH | D014235 (Trichinellosis; tree C01.610.335.508.100.275.882) | https://meshb.nlm.nih.gov/record/ui?ui=D014235 |
| UMLS | C0040896 | MedGen |
| OMIM | Not applicable (not a Mendelian disease) | — |

**Synonyms:** trichinosis, trichiniasis, *Trichinella* infection or infectious disease.

**Data provenance.** The information comes from aggregated, disease-level sources: surveillance systems (CDC, ECDC), outbreak reviews, and guidelines from the International Commission on Trichinellosis (ICT) and FAO/WHO/OIE. It does not come from individual-patient EHR data.

## 2. Etiology

**Causal factors (infectious).** Infection is caused by eating raw or undercooked meat that contains infective first-stage (L1) larvae of *Trichinella* spp.

- The genus has 13 taxa: 10 named species and 3 unnamed genotypes (Pozio 2021 and Sharma et al. 2020, as cited in PMC11033181, https://pmc.ncbi.nlm.nih.gov/articles/PMC11033181/):
  - *T. spiralis* (T1)
  - *T. nativa* (T2)
  - *T. britovi* (T3)
  - *T. pseudospiralis* (T4)
  - *T. murrelli* (T5)
  - *T. nelsoni* (T7)
  - *T. papuae* (T10)
  - *T. zimbabwensis* (T11)
  - *T. patagoniensis* (T12)
  - *T. chanchalensis* (T13)
  - unnamed genotypes T6, T8 and T9
- Species fall into an encapsulated clade and a non-encapsulated clade. The non-encapsulated clade includes *T. pseudospiralis*, which is "the only species capable of infecting both mammals and birds."

**Environmental and behavioural risk factors**

- **Pork.** "The domestic pig is the most important worldwide source of human infection" (PMID 19136437). In 1986–2009, "Pork was the major source of infection; wild game sources were also frequently reported" (Murrell & Pozio, *Emerg Infect Dis* 2011;17:2194–2202, PMC3311199).
- **Horse and wild boar meat** caused European outbreaks "in the past three decades" (PMID 19136437).
- **Bear and other game in the USA.** In 2008–2012, meats other than pork were linked to 54% of US cases, and 91% of those were bear meat. Among patients with cooking information, 47% "reported eating raw or undercooked meat" (CDC MMWR SS 2015;64(SS-1), https://www.cdc.gov/mmwr/preview/mmwrhtml/ss6401a1.htm).
- **Freeze-resistant species.** Freezing wild game "may not effectively kill all worms because some species are freeze-resistant" (CDC, https://www.cdc.gov/trichinellosis/prevention/).
- **Age and sex.** Cases were mostly adults (median age 33.1 years), and men (51%) and women were affected about equally (PMC3311199).
- **Infective dose.** Larger doses give more severe disease and earlier seroconversion (ICT serology recommendations, PMC7034015).

**Genetic risk factors (host)**

- No human susceptibility loci, GWAS hits or HLA associations were found. A search for HLA–trichinellosis studies returned none.
- Mouse data show host genetic control:
  - B10-background congenic strains are "low responders" and susceptible. NIH mice are "highly resistant" (Parasitology, Cambridge, https://www.cambridge.org/core/journals/parasitology/article/genetic-influences-upon-eosinophilia-and-resistance-in-mice-infected-with-trichinella-spiralis/74E8963733D424C4D9CF97378F45BF35).
  - H-2 (MHC) haplotype affects the speed of worm expulsion (B10.M expels faster than B10.Q or B10.BR), and "non-H-2 genes exerted the major influence."
  - Isolate infectivity in mice "is determined by host immune responsiveness" (PMID 2797874).

**Protective factors**

- Proper cooking, freezing of pork, controlled pig housing, and slaughter testing (see Section 13).
- No protective genetic variants are known in humans.

**Gene–environment interactions.** None have been characterised in humans. In mice, H-2 effects on expulsion "much reduced when mice received 400 L1 larvae", which means a high infective dose can mask host genotype effects (PMC1454539/PMC1384515 group of studies).

## 3. Phenotypes

Phenotypes are listed with frequencies from outbreak data. Frequencies vary widely between outbreaks.

| Phenotype | Type | Frequency / timing | Suggested HPO |
|---|---|---|---|
| Myalgia | Symptom | 88% (Israel, n=26); 90.5% (n=138 cohort) | HP:0003326 Myalgia |
| Facial / periorbital edema | Sign | 42% (Israel); 51.4% (n=138) | HP:0000282 Facial edema; HP:0100539 Periorbital edema |
| Fever | Sign | 11–47% | HP:0001945 Fever |
| Eosinophilia (>1,000/mm³) | Lab | 77.3% (n=138); peaks 2–4 weeks after infection | HP:0001880 Eosinophilia |
| Diarrhea / abdominal pain (enteral phase) | Symptom | Major feature among 5,377 cases | HP:0002014 Diarrhea; HP:0002027 Abdominal pain |
| Headache | Symptom | Major feature | HP:0002315 Headache |
| Pruritic maculopapular rash | Sign | About 30% | HP:0000988 Skin rash |
| Myocarditis | Complication | Up to 20%, weeks 3–4 | HP:0012819 Myocarditis |
| Arrhythmia / ECG conduction abnormalities | Sign | Severe cases | HP:0011675 Arrhythmia |
| CNS involvement (encephalitis, meningitis) | Complication | 0.2–52% of cases | HP:0002383 Encephalitis; HP:0001287 Meningitis |
| Elevated creatine kinase | Lab | Common (no frequency retrieved) | HP:0003236 Elevated serum creatine kinase |
| Respiratory myositis / pneumonia | Complication | Severe cases | HP:0002090 Pneumonia |

Sources for the table:
- Israel outbreak: *Emerg Infect Dis* 11(12), https://wwwnc.cdc.gov/eid/article/11/12/05-0461
- n=138 cohort: PMC7611085 table T1
- Pooled major features: PMC3311199
- Rash and eosinophilia kinetics: Merck/MSD Manual, https://www.msdmanuals.com/professional/infectious-diseases/nematodes-roundworms/trichinosis
- Myocarditis: BMJ Best Practice, https://bestpractice.bmj.com/topics/en-us/1140
- CNS involvement: systematic review, PMC8227095
- Elevated CK: **no frequency retrieved**

**Characteristics**
- **Onset:** Systemic signs start "One to 2 weeks after infection" (MSD Manual).
- **Severity:** Ranges from asymptomatic to fatal and depends on dose.
- **Course:** Acute and usually self-limited.

**Quality of life**
- Persistent muscle pain was seen in most of 12 patients 13–18 years after infection (*J Helminthol* 2022, https://www.cambridge.org/core/journals/journal-of-helminthology/article/long-lasting-immunity-in-trichinellosis-insight-from-a-small-study-group/8AAA3E1F41BFEB6DDC367E2FF4573FDC).
- A 10-year controlled study found patients "differed significantly from controls… even after 10 years," but found "insufficient evidence that chronic trichinosis exists as a distinct entity" (PMC1742236).
- No EQ-5D or SF-36 data were retrieved.

## 4. Genetic / Molecular Information

**Human causal genes, pathogenic variants, ACMG classes, allele frequencies, somatic/germline status, chromosomal abnormalities:** not applicable.

**Parasite genomics**
- *T. spiralis* draft genome: 64 Mb, about 15,808 protein-coding genes, about 18% repeats, about 35× coverage. About 45% of genes appear novel (Mitreva et al., *Nat Genet* 2011;43:228–235, PMID 21336279, PMC3057868).
- Korhonen et al. sequenced 16 draft genomes covering all 12 then-recognised taxa. Encapsulated and non-encapsulated clades diverged about 21 million years ago (*Nat Commun* 2016;7:10513, PMC4740406, doi:10.1038/ncomms10513).
- Resources: Ensembl Metazoa *T. spiralis* ISS_195 (https://metazoa.ensembl.org/Trichinella_spiralis/Info/Annotation/) and KEGG genome `tsp`.

**Modifier genes (host)**
- Mouse MHC (H-2, I-A region) shapes the antibody repertoire and the speed of expulsion.
- STAT6 and IL-4Rα are needed for timely expulsion. IL-4-deficient mice expel worms "almost normally," while STAT6-deficient mice are "substantially delayed" (PMC97960; PMC2753907).

**Epigenetics:** No data were retrieved.

## 5. Environmental Information

- **Infectious agent:** *Trichinella* spp. (NCBI Taxon IDs not retrieved in this session).
- **Life cycle:** Adult worms and encysted larvae develop within a single vertebrate host (CDC DPDx, https://www.cdc.gov/dpdx/trichinellosis/).
- **Release of larvae:** Stomach acid and pepsin free the larvae from the meat.
- **Transmission in nature:** Larvae "survive in decaying carcasses for a long time, facilitating transmission by scavenging" (WOAH Terrestrial Manual 3.1.23, https://woah.org/fileadmin/Home/fr/Health_standards/tahm/3.01.23_TRICHINELLOSIS.pdf).
- **Lifestyle factors:** Eating raw or undercooked pork, game or horse meat, home slaughter, hunting, and ethnic or traditional raw-meat dishes.
- **Toxins / CTD:** Not applicable.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. **Ingestion.** Eating meat with encysted L1 larvae leads to their release by gastric acid and pepsin (CDC DPDx).
2. **Intestinal invasion.** Larvae invade the columnar epithelium of the small intestine and moult into adults. This results in mucosal inflammation and enteral symptoms such as diarrhea and abdominal pain (StatPearls NBK536945).
3. **Reproduction.** After about 1 week, females release newborn larvae (CDC DPDx). The adult lifespan in the gut is about 4 weeks.
4. **Migration.** Newborn larvae spread systemically. The lymph/blood route is standard teaching but was not confirmed in the retrieved text. Their passage through tissues leads to:
   - eosinophilia
   - vasculitis-type allergic signs: facial/periorbital edema, rash, fever (MSD Manual). The link to these signs is inferred.
   - **Branch A, heart:** invasion of myocardium that larvae cannot stay in leads to eosinophilic myocarditis and arrhythmias in weeks 3–4 (BMJ Best Practice).
   - **Branch B, CNS:** results in encephalitis or meningitis and focal deficits. Mydriasis is the strongest marker of poor prognosis (positive likelihood ratio 9.08; PMC8227095).
5. **Muscle invasion and nurse cell formation.** Larvae entering striated muscle lead to nurse cell formation. The infected muscle cell "dedifferentiates, reenters cell cycle and arrests at G2/M." Satellite cells are activated, proliferate and differentiate (Wu et al., *Parasit Vectors* 2008;1:27, PMC2538513).
   - The infected myotube "synthesizes a collagen capsule" and gains a capillary supply. This takes about 20 days.
   - Despommier proposed that secreted tyvelose-glycosylated ("tyvelosylated") larval proteins drive this process (hypothesis; PMC3449155-associated text).
   - Myositis in this phase results in myalgia and raised CK.
6. **Immune response.** A Th2 response (IL-4, IL-13, STAT6) leads to expansion of mucosal mast cells and expulsion of adult worms. IL-18 delays expulsion (murine data; Ortega-Pierres et al. review; *Mucosal Immunol* 2008, https://www.nature.com/articles/mi200821.pdf).
7. **Immunomodulation and chronicity.** Excretory-secretory (ES) products:
   - reduce macrophage pro-inflammatory cytokines and increase IL-10, TGF-β and arginase-1 (in vitro; Springer s11010-011-1046-4)
   - make dendritic cells drive CD4⁺CD25⁺Foxp3⁺ Treg cells (PMC6912532, in vitro/mouse)
   - (review: Sofronic-Milosavljevic et al., PMC4465845)

   This leads to long-term survival of larvae in muscle. Larvae can live "for up to 40 years" (StatPearls NBK538511). It may also contribute to persistent sequelae (inferred and debated).

**Suggested GO terms**
- GO:0006954 inflammatory response
- GO:0042092 type 2 immune response
- GO:0043303 mast cell degranulation
- GO:0072676 / GO:0002551 eosinophil- and mast cell-related processes
- GO:0045786 negative regulation of cell cycle
- GO:0030199 collagen fibril organization
- GO:0001525 angiogenesis (VEGF involvement not confirmed in retrieved sources)
- GO:0014812 muscle cell migration / GO:0014816 skeletal muscle satellite cell differentiation
- GO:0002456 T cell mediated immunity
- GO:0045066 regulatory T cell differentiation

**Suggested CL terms**
- CL:0000188 skeletal muscle cell
- CL:0000594 skeletal muscle satellite cell
- CL:0000771 eosinophil
- CL:0000097 mast cell
- CL:0000545 T-helper 2 cell
- CL:0000815 regulatory T cell
- CL:0000235 macrophage
- CL:0000451 dendritic cell
- CL:0000584 enterocyte
- CL:0000746 cardiac muscle cell

**Omics, single-cell, spatial, CRISPR:** No human data were retrieved.

## 7. Anatomical Structures Affected

**Primary sites**
- Small intestine (UBERON:0002108)
- Skeletal muscle tissue (UBERON:0001134). Commonly cited predilection muscles are the diaphragm, tongue and masseter, but these were not confirmed in the retrieved text.

**Secondary sites**
- Heart / myocardium (UBERON:0002349)
- Brain and meninges (UBERON:0000955; UBERON:0002360)
- Lung (UBERON:0002048)
- Kidney (UBERON:0002113; hematuria and renal failure have been reported, NBK538511)
- Skin (UBERON:0002097)
- Periorbital region (UBERON:0035537 or similar)

**Body systems:** musculoskeletal, digestive, cardiovascular, nervous, immune.

**Subcellular level**
- Nurse-cell cytoplasm (GO:0005737)
- Nucleus (GO:0005634; cell-cycle re-entry)
- Collagen-containing extracellular matrix (GO:0062023)

**Lateralization:** Generalized and bilateral.

## 8. Temporal Development

**Onset:** Acute. Enteral symptoms appear in the first week. Systemic signs appear at 1–2 weeks. Eosinophilia peaks at 2–4 weeks. Myocarditis occurs in weeks 3–4. Deaths occur about 4–6 weeks after infection (BMJ Best Practice; NBK538511).

**Stages**
1. Enteral phase (week 1).
2. Parenteral / migratory phase (weeks 2–6).
3. Muscle encapsulation / convalescent phase. Larvae are established by 3–4 weeks (CDC).

**Course:** Usually self-limited over weeks to months. Some patients have long-lasting myalgia and fatigue.

**Critical window:** Anthelmintic treatment works best in the enteral phase. In mice, enteral-phase albendazole gave about a 90% drop in muscle larval load (PMC11010169). In humans, once larvae are in muscle, "treatment may not completely eliminate the infection" (CDC clinical care, https://www.cdc.gov/trichinellosis/hcp/clinical-care/).

## 9. Inheritance and Population

**Inheritance, penetrance, anticipation, founder effects, carrier frequency:** Not applicable (acquired infection).

**Epidemiology**
- **Global, 1986–2009:** 65,818 cases and 42 deaths in 41 countries. The WHO European Region had 87% of cases, and half of those were in Romania (PMC3311199).
- **Global burden:** About 76 DALYs per billion people per year (95% CrI 38–129). Europe accounts for 69% (Devleesschauwer et al., *Int J Parasitol* 2015;45:95–99, https://repub.eur.nl/pub/84929).
- **EU/EEA 2022:** 39 cases, 0.01 per 100,000. Latvia (0.16) and Bulgaria (0.13) had the highest rates (ECDC AER 2022). In 2021 there were 79 cases (0.02 per 100,000).
- **USA 2008–2012:** 90 cases, 0.1 per million per year, median 15 cases per year (MMWR SS6401).
- **Under-reporting:** True incidence is "likely significantly underestimated" (PMID 19136437).

**Demographics:** Adults predominate (median age 33.1 years), with a roughly 1:1 sex ratio. Outbreak clusters follow shared meals, hunting groups and traditional raw-meat foods.

## 10. Diagnostics

**Serology**
- ICT recommends "ELISA using excretory/secretory (ES) antigens," with positives "confirmed by western blot" (Bruschi, Gómez-Morales & Hill, *Food Waterborne Parasitol* 2019, PMC7034015).
- Seroconversion usually occurs in weeks 3–5. IgG is detectable from 15–60 days and can persist for more than 30 years.
- Most commercial human ELISA kits are described as "unreliable."
- Western blot bands of 37–127 kDa have been reported.
- An ELISA validation study is available (PMID 18827188).
- ES antigens from adult worms may improve early detection: 100% sensitivity at 19 days post-infection with some antigen preparations (PMC4579640).
- Combining serology with clinical and epidemiological data is reviewed in *Food Waterborne Parasitol* 2022;27:e00165 (PMC9120223).

**Laboratory:** eosinophil count, CK, LDH, and troponin to screen for myocarditis (BMJ Best Practice).

**Biopsy:** Muscle biopsy (trichinoscopy, histology, PCR) shows larvae and nurse cells. Serology is earlier and more sensitive (PMC2583519).

**Species identification:** Multiplex PCR on larvae from the patient or from the meat (ICT).

**Imaging and electrophysiology:** ECG for conduction abnormalities. Brain CT/MRI for neurotrichinellosis (PMC8227095). EMG for myositis (no data retrieved).

**Clinical criteria:** FAO/WHO/OIE guidelines (Dupouy-Camet & Murrell, eds., 2007) and ICT guidance combine:
- clinical signs (fever, myalgia, facial edema, diarrhea)
- laboratory findings (eosinophilia, CK, serology or biopsy)
- epidemiological link to suspect meat

**Differential diagnosis:** influenza and other viral myositis, eosinophilic syndromes, polymyositis/dermatomyositis, angioedema, toxocariasis, gastroenteritis.

**Genetic, omics and screening tests:** No human genetic testing is relevant. There is no population screening. Screening applies to meat (artificial digestion at slaughter; WOAH).

## 11. Outcome / Prognosis

**Mortality**
- 42 deaths among 65,818 cases (about 0.06%; PMC3311199).
- Deaths usually come from "myocarditis, encephalitis, or pneumonia" (NBK538511).

**Prognostic factors**
- Higher infective dose and older age (qualitative).
- CNS involvement. Mydriasis has a positive likelihood ratio of 9.08 for poor outcome, and reduced reflexes also raise the risk (PMC8227095).
- Myocarditis.

**Morbidity:** About 76 DALYs per billion per year globally. Possible long-term myalgia, fatigue and reduced function (PMC1742236; *J Helminthol* 2022).

**Recovery:** Most patients recover within months.

**Prognostic biomarkers:** Troponin (myocarditis). No validated molecular markers.

## 12. Treatment

**Anthelmintics (CDC)**

| Drug | Dose |
|---|---|
| Albendazole | 400 mg orally twice daily for 8–14 days (adults and children) |
| Mebendazole | 200–400 mg three times daily for 3 days, then 400–500 mg three times daily for 10 days |

- Both are benzimidazoles that inhibit parasite β-tubulin polymerisation.
- Neither is approved for pregnancy or for children under 2 years. Serial blood counts are advised during long courses (bone marrow suppression).
- If treatment starts late, prolonged or repeated courses may be needed.

**Corticosteroids**
- Prednisone 30–60 mg per day for 10–15 days, given with an anthelmintic, for myocarditis, encephalitis or intense myalgia (StatPearls NBK536945).

**Supportive care:** Analgesics and antipyretics, and anti-arrhythmics for myocarditis (BMJ Best Practice).

**Comparative evidence**
- In a randomized 1988 outbreak trial, albendazole alone gave negative serology in 70% of patients, versus 34.5% with tiabendazole followed by flubendazole (Springer BF00931188).
- Data from dogs and cats are also available (PMID 8214900).

**Pharmacogenomics, gene/cell/RNA therapy, targeted therapy, immunotherapy, surgery:** Not applicable. No registered NCT trials were retrieved.

**Suggested NCIT terms**
- Albendazole (NCIT:C61633)
- Mebendazole (NCIT:C62031)
- Prednisone (NCIT:C770)
- Anthelmintic agent (NCIT:C272)
- Corticosteroid therapy

These NCIT codes are from memory and should be verified.

**Suggested CHEBI terms**
- Albendazole (CHEBI:16664)
- Mebendazole (CHEBI:6704)
- Prednisone (CHEBI:8378)

Verify these as well.

## 13. Prevention

**Primary prevention**
- Cook meat to a safe internal temperature and check it with a thermometer (CDC). The commonly cited 71 °C / 160 °F figure was not confirmed in retrieved sources.
- Freeze pork less than 6 inches thick "for 20 days at 5°F (-15°C)." This does not reliably work for game meat (CDC prevention page).
- ICT accepts cooking, freezing of domestic pig meat, and irradiation (PMC7033995).

**Veterinary public health**
- Slaughter inspection of pigs, horses and wild boar by artificial digestion. This is EU practice; the text of Regulation 2015/1375 was not retrieved.
- Controlled-housing pig compartments.
- Rodent control and proper carcass disposal (WOAH Terrestrial Code ch. 8.18).
- Because the burden is low, Devleesschauwer et al. argue for "more cost-effective" inspection programmes.

**Secondary prevention:** Outbreak investigation, tracing the meat source, and early treatment of people exposed to the same meal.

**Vaccines and genetic counselling:** No human vaccine. Genetic counselling is not applicable.

## 14. Other Species / Natural Disease

**Host range**
- Hosts include "humans, pigs, rats, bears, walruses, horses and many other" mammals, plus some birds (*T. pseudospiralis*) and reptiles (*T. papuae*, *T. zimbabwensis*) (WOAH Manual).

**Transmission cycles**
- **Domestic cycle:** Dominated by *T. spiralis* and maintained by domestic swine.
- **Sylvatic cycle:** Maintained in wildlife carnivores and scavengers.

**Veterinary relevance:** Trichinellosis is a WOAH-listed disease (https://www.woah.org/en/disease/trichinellosis/). Infection is usually subclinical in animals.

**Zoonotic potential:** High. Where pig infection is controlled, human cases come mostly from game and horse meat (WOAH).

**Not applicable here:** Breed (VBO) data, OMIA entries and orthologous host genes.

**Parasite phylogeny:** Korhonen et al. 2016 (PMC4740406).

## 15. Model Organisms

**Mouse (primary model)**
- Inbred strains differ in resistance: NIH is resistant; B10 and B10.BR are susceptible.
- Knockouts (IL-4, STAT6, IL-4Rα, IL-18) are used to study intestinal expulsion, mast cell biology and nurse cell formation (PMC97960, PMC2753907, PMC2842902).
- Vaccine-candidate studies are reviewed by Ortega-Pierres et al.

**Rat:** Classic model for muscle larvae and nurse cells. No specific citation was retrieved.

**Pig:** Natural host, used for veterinary diagnostics and vaccine work. No specific citation was retrieved.

**In vitro**
- Macrophage and dendritic-cell assays with ES products (PMC6912532).
- Myoblast and satellite cell systems for nurse-cell studies (PMC2538513).

**Limitations of models**
- Mice need high doses.
- Mouse cardiac and CNS disease and chronic human sequelae are poorly modelled.
- Host genotype and sex change drug efficacy in mice (PMC11010169).

**Resources:** MGI (knockout strains), Ensembl Metazoa and WormBase ParaSite (parasite genomes), and the ICT reference centre for *Trichinella* isolates.

---

### Key sources
- Gottstein B, Pozio E, Nöckler K. *Clin Microbiol Rev* 2009 — PMID 19136437; PMC2620635
- Murrell KD, Pozio E. *Emerg Infect Dis* 2011;17:2194 — PMC3311199
- Mitreva M et al. *Nat Genet* 2011 — PMID 21336279
- Korhonen PK et al. *Nat Commun* 2016 — PMC4740406
- Devleesschauwer B et al. *Int J Parasitol* 2015 — https://repub.eur.nl/pub/84929
- ICT serology recommendations 2019 — PMC7034015; ICT post-harvest/meat — PMC7033995
- CDC MMWR SS 64(1) 2015; CDC Clinical Care; CDC Prevention; CDC DPDx
- ECDC Annual Epidemiological Report 2022
- WOAH Terrestrial Manual ch. 3.1.23 and Terrestrial Code ch. 8.18
- CNS involvement systematic review — PMC8227095
- Nurse cell biology — PMC2538513
- ES immunomodulation — PMC4465845, PMC6912532
- Long-term follow-up — PMC1742236
- StatPearls NBK536945, NBK538511; MSD Manual; BMJ Best Practice 1140

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 8 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 30 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19136437` *(abstract only)*: "ingestion of Trichinella larvae encysted in the muscle tissue of domestic or wild animal meat"
  - closest text in source: "Infection of humans occurs with the ingestion of Trichinella larvae that are encysted in muscle tissue of domestic or wild animal meat"
- `PMC:PMC2620635` *(abstract only)*: "ingestion of Trichinella larvae encysted in the muscle tissue of domestic or wild animal meat"
  - closest text in source: "Infection of humans occurs with the ingestion of Trichinella larvae that are encysted in muscle tissue of domestic or wild animal meat"
- `PMID:19136437` *(abstract only)*: "The domestic pig is the most important worldwide source of human infection"
  - closest text in source: "The most important source of human infection worldwide is the domestic pig, but, e.g., in Europe, meats of horses and wild boars have played a significant role during outbreaks within the past 3 decades"
- `PMID:19136437` *(abstract only)*: "in the past three decades"
  - closest text in source: "The most important source of human infection worldwide is the domestic pig, but, e.g., in Europe, meats of horses and wild boars have played a significant role during outbreaks within the past 3 decades"
- `PMID:2797874` *(abstract only)*: "is determined by host immune responsiveness"
  - closest text in source: "These results are discussed in relation to the interplay of parasite immunogenicity and host immune responsiveness in determining infectivity, and point to the importance of identifying those immunodominant parasite molecules which control the balance of the host-parasite relationship."
- `PMC:PMC1742236` *(abstract only)*: "insufficient evidence that chronic trichinosis exists as a distinct entity"
  - Text part not found as substring: 'insufficient evidence that chronic trichinosis exists as a distinct entity' (note: only abstract available for PMID:11796866, full text may contain this excerpt)
- `PMC:PMC2753907` *(abstract only)*: "substantially delayed"
  - Text part not found as substring: 'substantially delayed' (note: only abstract available for PMID:19191917, full text may contain this excerpt)
- `PMID:19136437` *(abstract only)*: "likely significantly underestimated"
  - Text part not found as substring: 'likely significantly underestimated' (note: only abstract available for PMID:19136437, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1007/978-3-031-00303-5_10`: "a worldwide zoonosis caused by the parasitic nematodes belonging to the Trichinella genus"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 6 |
| Terms whose name was checked | 15 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019444` (2 mentions) - the report calls it "MONDO"; MONDO calls it **trichinellosis**
- `NCIT:C61633` (1 mention) - the report calls it "Albendazole"; NCIT calls it **Amiloride**
- `NCIT:C62031` (1 mention) - the report calls it "Mebendazole"; NCIT calls it **Granisetron**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0035537` (1 mention) - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002349` (1 mention) - the report calls it "Heart / myocardium"; UBERON calls it **myocardium**, and lists "heart myocardium" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `GO:0005737` (1 mention) - the report calls it "Nurse-cell cytoplasm"; GO calls it **cytoplasm**
- `GO:0062023` (1 mention) - the report calls it "Collagen-containing extracellular matrix"; GO calls it **obsolete collagen-containing extracellular matrix**
- `NCIT:C272` (1 mention) - the report calls it "Anthelmintic agent"; NCIT calls it **Antimetabolite**
- `CHEBI:8378` (1 mention) - the report calls it "Prednisone"; CHEBI calls it **prednisolone**

### Terms the ontology service could not be reached for

5 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `GO:0072676` (1 mention)
- `GO:0002551` (1 mention)
- `CL:0000188` (1 mention)
- `CL:0000594` (1 mention)
- `CL:0000451` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `GO:0014812` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.