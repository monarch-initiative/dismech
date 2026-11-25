---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-11-17T04:10:26.285384'
end_time: '2026-11-17T04:22:34.963544'
duration_seconds: 728.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SNCA-Related Parkinson Disease
  mondo_id: MONDO:0008200
  category: Mendelian
  causal_genes: SNCA
  omim_id: OMIM:168601
  synonyms: autosomal dominant Parkinson disease type 1
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 28
  num_turns: 57
  total_cost_usd: 7.140437384999999
  session_id: 7bb320dd-329c-4161-8758-ed1e064bf01f
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 70
  retrieval_calls: 65
  assistant_text_blocks: 2
citation_count: 104
reference_validation:
  total_references: 109
  verified: 108
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.009
  quotes_checked: 57
  quotes_valid: 23
  quotes_unsupported: 34
  unsupported_quote_references:
  - PMID:35328025
  - PMC:PMC8950888
  - PMID:30357936
  - PMID:32849182
  - PMID:23526723
  - PMID:23457019
  - PMID:19139307
  - PMID:18571778
  - PMID:15159488
  - PMID:21863007
  - PMID:27938414
  - PMID:29771508
  - PMID:38424059
  - PMID:12062037
  - PMID:29895861
  - PMID:32954426
  - PMID:23161999
  - PMID:37868923
  - PMC:PMC5819572
  - PMID:30619023
  - PMC:PMC12198753
  - PMID:18574253
  quotes_not_checkable: 1
  relevance_assessed: 108
  on_topic: 54
  unresolved_references:
  - PMID:32595456
  needs_review: true
  validator_version: 0.6.0
term_validation:
  total_terms: 108
  verified: 106
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0008200
    reported_labels:
    - OLS4 API
    ontology_label: autosomal dominant Parkinson disease 1
  - term_id: DOID:0060367
    reported_labels:
    - DOID
    ontology_label: Parkinson's disease 1
  - term_id: MONDO:0011764
    reported_labels:
    - autosomal dominant Parkinson disease 8
    - OLS4 API
    ontology_label: autosomal dominant Parkinson disease 8
  - term_id: NCIT:C15986
    reported_labels:
    - Dopamine agonists
    - MAO-B inhibitors
    - COMT inhibitor
    - Amantadine (for dyskinesia)
    - Atypical antipsychotic for PD psychosis
    - Cholinesterase inhibitor for PD dementia
    ontology_label: Pharmacotherapy
  obsolete_terms:
  - term_id: GO:0015872
    ontology_label: obsolete dopamine transport
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SNCA-Related Parkinson Disease
- **MONDO ID:** MONDO:0008200 (if available)
- **Causal gene(s):** SNCA
- **OMIM:** OMIM:168601
- **Synonyms:** autosomal dominant Parkinson disease type 1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SNCA-Related Parkinson Disease** covering all of the
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

Working on it: reading the existing SNCA entry for cited sources, then running web searches.

# Comprehensive Research Report: SNCA-Related Parkinson Disease (MONDO:0008200)

**Scope note / interpretation adopted.** This report covers Parkinson disease caused by pathogenic variation in **SNCA** (α-synuclein; HGNC **hgnc:11138**, label `SNCA`, read from this repository's authority-backed term cache `cache/hgnc/terms.csv`). The template supplies MONDO:0008200 and OMIM:168601, which correspond to the **missense/point-mutation** form historically designated **PARK1**; the **multiplication** form (duplication/triplication of the SNCA locus) was historically designated **PARK4** (OMIM 605543). Because the two are allelic and are treated as one gene-defined entity by current reviews, both are covered here and labelled explicitly wherever the evidence differs between them. The repository's existing stub for this entry already lists both PARK1 and PARK4 as synonyms (`kb/disorders/SNCA-Related_Parkinson_Disease.yaml`), which is consistent with that reading.

**Retrieval limitations, stated up front.** NCBI Bookshelf (GeneReviews *Monogenic Parkinson Disease Overview*, NBK1223) and PubMed abstract pages returned bot-check/cookie interstitials to the tools available in this session, as did one PMC article (PMC11775907). Where a figure comes only from a secondary source quoting the primary paper, this is said so in the text. Sections where I could not retrieve adequate primary support — notably epigenetics, metabolomics/lipidomics, naturally occurring disease in other species, and formal quality-of-life instrument data — say so rather than being filled from memory. No ontology identifier in this report was written from memory: HPO, GO, CL, UBERON, CHEBI and NCIT CURIEs were read from this repository's committed term caches (`cache/<prefix>/terms.csv`), and the two MONDO records were read live from the EBI Ontology Lookup Service.

---

## 1. Disease Information

**Overview.** SNCA-related Parkinson disease is an autosomal dominant synucleinopathy in which heterozygous missense variants in *SNCA*, or increased *SNCA* copy number (duplication or triplication of the locus), cause parkinsonism with Lewy-body pathology. Relative to idiopathic PD it is characterised by earlier age at onset, a higher burden of non-motor features — particularly cognitive decline, psychosis and dysautonomia — and, in the higher-dosage and some missense forms, more rapid progression. The 2022 review *Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing* states plainly that "*SNCA* mutations cause autosomal dominant PD and can be due to different mutation types, including missense variants and multiplications" (Jia, Fellner & Kumar, *Genes (Basel)* 2022;13(3):471; PMID:35328025, PMC8950888).

**Identifiers.** Read live from OLS4 for MONDO:0008200:

| Resource | Value |
|---|---|
| MONDO | **MONDO:0008200**, label `autosomal dominant Parkinson disease 1` |
| OMIM | 168601 (`MONDO:equivalentTo`) |
| DOID | DOID:0060367 |
| MeSH | C566823 |
| MedGen | 357008 |
| UMLS | C1868595 |
| GARD | 0018474 |
| HGNC (gene) | hgnc:11138 (`SNCA`) |

Notes from the MONDO record itself: it carries **no Orphanet and no ICD cross-reference**, and its only `description` field is an editor note — "Editor note: DO def states any mutation in SNCA, but this would include PARK4; def needs to state that this is het mutation" — i.e. MONDO's own curators flag the PARK1/PARK4 boundary as unresolved in this term. That is directly relevant to the scope decision taken above and should be recorded in any KB entry's `notes`. Exact synonym: `autosomal dominant Parkinson disease 1`; related synonym (abbreviation): `PARK1`. Further synonyms in the flat list: `Parkinson disease 1, autosomal dominant`, `autosomal dominant Parkinson disease type 1`. For comparison, the sibling LRRK2 term MONDO:0011764 (`autosomal dominant Parkinson disease 8`) *does* carry a gene-pattern definition ("Any Parkinson disease in which the cause of the disease is a mutation in the LRRK2 gene"), which MONDO:0008200 lacks — a candidate upstream term-request.

**Common synonyms and alternative names.** PARK1; PARK4; autosomal dominant Parkinson disease 1; autosomal dominant Parkinson disease 4; PARK-SNCA (the MDS nomenclature form); α-synuclein Parkinson disease. Historical kindred-based names appear in the literature (the *Contursi kindred* for A53T, the *Iowa kindred* for the triplication).

**Information provenance.** Essentially all of the evidence below is **aggregated, disease-level** (family reports, multicentre cohort studies, systematic reviews, meta-analysis of pedigrees, model-organism and in-vitro work). The two largest genotype–phenotype resources are both aggregations of published pedigrees: the MDSGene systematic review (Trinh et al., *Mov Disord* 2018;33(12):1857–1870; PMID:30357936) and the GEoPD multiplication meta-analysis (Book et al., *Front Neurol* 2018;9:1021; PMID:30619023). No EHR-derived or individual-patient-level registry resource specific to SNCA PD was retrieved. One prospectively phenotyped multicentre clinical cohort exists (Lesage et al., *Front Neurol* 2020;11:682; PMID:32849182).

---

## 2. Etiology

### 2.1 Disease causal factors

The primary cause is **genetic and monogenic**: a heterozygous *SNCA* missense variant, or an increase in *SNCA* copy number. Two distinct molecular routes to the same disease are documented.

1. **Point mutation.** The founding observation — an alanine-to-threonine substitution at codon 53 — was reported by Polymeropoulos et al. in *Science* 1997;276(5321):2045 (DOI 10.1126/science.276.5321.2045) in the Contursi kindred and three Greek families. *Caveat:* only one secondary page in this session carried a PMID for that paper (9197268) and it was not independently confirmed; cite the DOI, or re-fetch the PubMed record, before writing a PMID into a KB entry.
2. **Gene dosage.** Singleton et al. demonstrated that triplication of the *SNCA* locus alone causes PD (*Science* 2003;302(5646):841; **PMID:14593171**), and duplication was shown to do the same the following year in two back-to-back *Lancet* reports: Chartier-Harlin et al. (**PMID:15451224**) and Ibáñez et al. (**PMID:15451225**). The dosage route is the cleanest available demonstration that α-synuclein *quantity*, with no change to its sequence, is sufficient to cause human Parkinson disease — the single most load-bearing causal fact about this disease.

### 2.2 Risk factors

**Genetic — causal.** See §4. In carriers, the relevant modifier of risk and of onset age is **copy number itself**: Book et al. report a mean age of motor onset of **46.9 ± 10.5 years for CNV3 (heterozygous duplication) versus 34.5 ± 7.4 years for CNV4, p = 0.003** (PMID:30619023). Jia et al. summarise the resulting ladder as "early, intermediate, and late onset for triplications, missense mutations, and duplications, respectively" (PMID:35328025).

**Genetic — susceptibility at the same locus.** *SNCA* is also one of the strongest common-variant risk loci for sporadic PD, which is mechanistically continuous with the Mendelian form: both act through α-synuclein dose. The Rep1 dinucleotide repeat ~10 kb upstream of the *SNCA* transcription start site modulates transcription, with longer alleles associated with higher expression and higher PD risk (collaborative analysis: Maraganore et al., *JAMA* 2006;296:661–670 — identified through citing records in this session; the primary abstract could not be retrieved, so treat the citation as bibliographic rather than quote-verified). GWAS confirms the locus: rs2736990 in *SNCA*, OR = 1.23, P = 2.24 × 10⁻¹⁶ (Simón-Sánchez et al., **PMID:19915575**). Approximately 90 independent risk loci were reported in the European-ancestry meta-analysis of Nalls et al., *Lancet Neurol* 2019;18(12):1091–1102, and 78 loci including 12 potentially novel ones in the later multi-ancestry meta-analysis (**PMID:38155330**). Common *SNCA* variants have also been associated with clinical heterogeneity and non-motor progression in sporadic PD (systematic review, PMC8249472; Rep1 length and non-motor decline, PMC7655210 and PMC11892927; progression in newly diagnosed patients, PMC7902914).

**Environmental.** No environmental factor has been shown to cause or to be necessary for SNCA-related PD; it is a monogenic disease. For *sporadic* PD at the *SNCA* locus there is a case-control literature on interaction (§2.4). **Age** is the dominant non-genetic determinant of onset within carrier families (penetrance is age-dependent, §9). **Sex** effects specific to SNCA carriers were not retrieved.

### 2.3 Protective factors

No *SNCA*-specific protective allele was retrieved. For PD generally, caffeine (CHEBI:27732) and nicotine are the classical inverse-association exposures, but I did not retrieve a primary source in this session that establishes either within SNCA carriers, and the report declines to assert it. **This section is under-supported and should be curated as a gap rather than populated.** One mechanistically relevant negative finding: silencing α-synuclein in mature nigral neurons produced neuroinflammation and subsequent toxicity (PMC5819572) — i.e. less α-synuclein is not monotonically protective, which bears directly on the therapeutic strategy in §12.

### 2.4 Gene–environment interactions

Retrieved only for the common-variant form of the locus, not for the Mendelian form: a case-control study of α-synuclein genotype, pesticide exposure and PD (**PMID:18322262**) and a study of head injury together with *SNCA* genetic variability (**PMID:25370538**). Both are association studies in sporadic PD; neither establishes an interaction in *SNCA* mutation carriers. Candidate ontology bindings for exposures would need to be looked up in ECTO at curation time and are deliberately not asserted here.

---

## 3. Phenotypes

Frequencies below are given with their denominators and their source, because the two main aggregations disagree in places and the subgroups are small. **Do not pool them.**

### 3.1 Core motor phenotype

All reports describe levodopa-responsive parkinsonism as the core presentation. In the French multicentre cohort, **15/15 (100%)** of assessable *SNCA* duplication carriers were levodopa-responsive (defined as ">30% improvement in subjective perceived motor symptoms"), with dyskinesias in **9/15 (60%)** and motor fluctuations in **8/15 (53.3%)** (PMID:32849182). The authors summarise: "*SNCA* mutation carriers had motor features similar to those of idiopathic PD, but an overall earlier AAO, a shorter disease course, a higher frequency of motor complications, a higher frequency of non-motor signs and symptoms."

| Phenotype | HP term (verified against `cache/hp/terms.csv`) | Type | Frequency / notes |
|---|---|---|---|
| Parkinsonism | HP:0001300 `Parkinsonism` | clinical sign | Obligate; defining |
| Bradykinesia | HP:0002067 `Bradykinesia` | clinical sign | Reported in essentially all series; "bradykinesia and early onset of levodopa-induced dyskinesia are the characteristic clinical features" of A53E (Martikainen et al., PMID:27066564) |
| Rigidity | HP:0002063 `Rigidity` | clinical sign | Common; reported in the Turkish duplication sibship (PMID:41738528) |
| Resting tremor | HP:0002322 `Resting tremor` | clinical sign | Presenting feature in individual cases (e.g. G51D case 1, "presented at age 19 with left hand tremor"; H50Q case, "right hand tremor at age 71") — Kiely et al., PMID:26306801 |
| Postural instability | HP:0002172 `Postural instability` | clinical sign | Progression-dependent |
| Dyskinesia | HP:0100660 `Dyskinesia` | clinical sign | 60% of duplication carriers (9/15), PMID:32849182 |
| Dysarthria | HP:0001260 `Dysarthria` | clinical sign | "severe dysarthria" in an A53T carrier, PMID:32849182 |
| Freezing of gait | HP:0031825 `Freezing of gait` | clinical sign | Reported in advanced disease; no SNCA-specific frequency retrieved |

### 3.2 Cognitive and psychiatric phenotype — the discriminating axis

This is where SNCA-related PD departs most from idiopathic PD, and it is dosage-graded.

| Phenotype | HP term | Frequency / source |
|---|---|---|
| Dementia | HP:0000726 `Dementia` | **31/55 probands (56.4%)** in the multiplication meta-analysis Results; the same paper's abstract states **50.9%** — the two figures **do not agree** and a KB entry should record the discrepancy rather than pick one (PMID:30619023) |
| Cognitive impairment | HP:0100543 `Cognitive impairment` | 33/55 positive overall; by group **26/47 CNV3 (55%)** vs **7/8 CNV4 (88%)** (percentages computed from Table 1 denominators, not stated in the paper) — PMID:30619023. Much lower in the prospective French duplication subgroup: "cognitive decline was less frequent (18.8%, 3/16)" by MMSE <24/30 (PMID:32849182) |
| Hallucinations / psychosis | HP:0000738 `Hallucinations`; HP:0002367 `Visual hallucination`; HP:0000709 `Psychosis` | 30 positive / 14 negative / 11 not available (PMID:30619023); "persistent visual hallucinations and paranoid delusions were problematic" in G51D (PMID:26306801) |
| Depression | HP:0000716 `Depression` | 4/16 (25%) in the duplication subgroup, grouped as depression/neuropsychiatric disorders (PMID:32849182) |
| Anxiety | HP:0000739 `Anxiety` | Presenting symptom in all three G51D cases; "prominent behavioural disturbance, anxiety, irritability" in case 3 (PMID:26306801) |
| Apathy | HP:0000741 `Apathy` | Reported in PD generally; no SNCA-specific frequency retrieved |
| Impulsivity | HP:0100710 `Impulsivity` | "rapid impulse control disorders" in an A53T carrier (PMID:32849182) |

The MDSGene review's headline finding on this axis — retrieved via citing sources, since the PubMed abstract page was blocked — is that *SNCA* carriers had younger age at onset than *LRRK2* and *VPS35* carriers (P < 0.001) and that "pooled data also revealed that SNCA mutation carriers more frequently experienced psychiatric symptoms" (Trinh et al., PMID:30357936). Dementia onset is also dosage-graded: **58.9 ± 8.8 years (n = 20) in CNV3 vs 42.2 ± 7.3 years (n = 6) in CNV4, p < 0.001**, and "46% of dementia diagnoses came within 5 years of motor onset" (PMID:30619023).

### 3.3 Autonomic and sleep phenotype

| Phenotype | HP term | Frequency / source |
|---|---|---|
| Orthostatic hypotension | HP:0001278 `Orthostatic hypotension` | A component of the composite "dysautonomia" definition below; explicitly prominent in A30G (PMID:35328025) |
| Dysautonomia (composite) | — (use the component terms) | **21 positive / 10 negative / 24 not available** (PMID:30619023). In the French cohort, 6/16 (37.5%) of duplication carriers, where dysautonomia was defined as "at least one of the following three signs: orthostatic hypotension, erectile dysfunction, and/or urinary problems" (PMID:32849182) |
| Urinary incontinence | HP:0000020 `Urinary incontinence` | Reported as common in the Turkish duplication sibship (PMID:41738528) |
| Constipation | HP:0002019 `Constipation` | Expected in synucleinopathy; no SNCA-specific frequency retrieved |
| REM sleep behaviour disorder | HP:5200291 `REM sleep behavior disorder` | **16 positive / 14 negative / 25 not available**; by group 13/25 CNV3 vs 3/5 CNV4 (PMID:30619023); also reported in the Turkish sibship (PMID:41738528) |
| Hyposmia | HP:0004409 `Hyposmia` | Central to SAA-defined phenotyping in sporadic PD (PMID:37059509); no SNCA-carrier frequency retrieved |

### 3.4 Pyramidal and atypical features (largely missense-specific)

G51D is the clearest example of a missense variant producing a phenotype *outside* the typical PD picture. Lesage et al. described a parkinsonian–pyramidal syndrome with "early disease onset, moderate response to levodopa, rapid progression, and marked pyramidal signs including bilateral extensor plantar reflexes, occasionally spasticity, and frequently psychiatric symptoms" (*Ann Neurol* 2013;73:459–471; **PMID:23526723**); Kiely et al. independently reported G51D in a British family with young-onset PD (**PMID:23404372**). In Kiely's 2015 comparison, pyramidal signs were present in all three G51D cases and in the duplication case, and absent in the H50Q case (PMID:26306801). Relevant HP terms: HP:0003487 `Babinski sign`, HP:0001257 `Spasticity`. For A53T, an atypical presentation with "a poor response to levodopa, early motor fluctuations and cerebellar signs" is described in one carrier who also carried a heterozygous *PRKN* variant (PMID:32849182) — note the confounder.

### 3.5 Onset, severity, progression, variability

- **Onset:** adult, typically 4th–6th decade, with the dosage ladder above. The observed extremes in individual series are wide: G51D cases at **19, 69 and 46 years** in one three-case series (PMID:26306801); duplication carriers 36–56 years and A53T 26–40 years in the French cohort (PMID:32849182).
- **Severity:** variable, and variability is itself a documented feature. Book et al. note "An atypical or more severe clinical course was described in several patients (n = 24)" (PMID:30619023). One duplication case presented clinically as **frontotemporal dementia** with marked behavioural change and only transiently levodopa-responsive parkinsonism (PMID:26306801); a 6.4 Mb duplication caused FTD with parkinsonism (**PMID:25003242**).
- **Progression:** progressive and non-remitting. Mean disease duration in the French duplication group was **6.3 ± 3.9 years (range 1–16)** at cross-sectional assessment; G51D durations were 29, 6 and 6 years and the duplication and H50Q cases 12 years each (PMID:26306801, PMID:32849182).
- **Quality of life:** **no SNCA-specific EQ-5D, SF-36 or PROMIS data were retrieved.** Functional impact must be inferred from the dementia, psychosis and dysautonomia frequencies above and should be curated as a gap, not asserted.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SNCA*, **hgnc:11138** (from `cache/hgnc/terms.csv`), encoding α-synuclein. OMIM phenotype entries: 168601 (PARK1, cross-referenced by MONDO:0008200 per the OLS record above) and 605543 (PARK4; not independently retrieved in this session — verify before writing it into an entry).

**Pathogenic missense variants.** Jia et al. enumerate them exactly: "So far, there have been eight missense variants identified as causing autosomal dominant PD: p.A30G, p.A30P, p.E46K, p.H50Q, p.G51D, p.A53E, p.A53T, and p.A53V" (PMID:35328025). Primary reports retrieved:

| Variant | Primary report | Identifier retrieved |
|---|---|---|
| p.A53T | Polymeropoulos et al., *Science* 1997;276:2045 | DOI 10.1126/science.276.5321.2045 (PMID not independently confirmed) |
| p.A30P | Krüger et al., *Nat Genet* 1998;18(2):106–108 | DOI 10.1038/ng0298-106 (PMID not retrieved) |
| p.E46K | Zarranz et al., *Ann Neurol* 2004;55(2):164–173 | DOI 10.1002/ana.10795 (PMID not retrieved); later family of Russian ancestry, **PMID:38661277** |
| p.H50Q | Appel-Cresswell et al., *Mov Disord* 2013;28(6):811–813 | **PMID:23457019** |
| p.G51D | Lesage et al., *Ann Neurol* 2013;73:459–471 (**PMID:23526723**); Kiely et al., *Acta Neuropathol* 2013 (**PMID:23404372**) | both confirmed |
| p.A53E | Pasanen et al., *Neurobiol Aging* 2014 (**PMID:24746362**); clinical/imaging follow-up **PMID:27066564**; first East Asian case **PMID:38867354** | confirmed |
| p.A30G | Liu et al., *Mov Disord* 2021;36(7):1624–1633 (PMID reported as 33617693 by citing records; not directly confirmed); Greek cohort follow-up PMC11775907 (page blocked); comment and reply **PMID:34543462** / **PMID:34543467** | partially confirmed |
| p.A53V | Listed as pathogenic by Jia et al.; comparative biophysics at the A53 site, **PMID:29771508** | — |

**Variant classification caveat that must survive into the KB.** H50Q's pathogenicity is contested: Jia et al. state "there is evidence that the p.H50Q variant is not enriched in cases versus controls" and that it "may not have sufficient evidence to be considered pathogenic" (PMID:35328025). Independently, the French cohort reports a His50Gln **homozygote** whose pathogenicity "remains inconclusive" (PMID:32849182). Under this repository's conventions a contested locus is a `genetic:` row graded `DISPUTED`, never a `has_subtypes` row. A further candidate, p.T72M in two Turkish families, is reported but not in Jia's pathogenic list (**PMID:34229155**).

**Structural note.** The pathogenic missense substitutions cluster: "α-Synuclein mutations cluster around a putative protein loop" (**PMID:23669636**), and all eight fall within the N-terminal, membrane-binding, amphipathic helical region. Appel-Cresswell et al. argued H50Q's pathogenicity partly on the grounds that it "disrupts the same amphipathic alpha-helical structure as previously known pathogenic SNCA mutations" (PMID:23457019).

**Copy-number variants.** Whole-locus duplication and triplication. Mechanism: "SNCA genomic duplication results from intra-allelic or inter-allelic recombination with unequal crossing-over, whereas both mechanisms appear to be required for genomic SNCA triplication" (Ross et al., **PMID:19139307**; see also **PMID:18571778**). The Iowa triplication was initially narrowed to 1.61–2.04 Mb containing 17 genes and later fine-mapped (PMC6003950). Critically, **multiplication size and gene count were not associated with motor onset or dementia** in the meta-analysis (PMID:30619023) — i.e. the phenotype tracks *SNCA* copy number, not the number of co-duplicated genes, which is strong evidence that *SNCA* is the driver within the CNV. Duplications are also found, rarely, in apparently sporadic PD (**PMID:17625105**).

**Allele frequency / relative frequency.** Jia et al.'s Table 1 gives the frequency of *SNCA* mutations as "Rare, with a frequency from 0.045% to 1.1% in recent studies," with ethnic distribution "Majority European, then Asians and Hispanics" (PMID:35328025). The upper bound of that range is the French multicentre figure (§9). Retrieved per-cohort yields: 1/144 dominant-family Italian probands (0.7%, **PMID:19833540**); **0** among 101 familial probands, 325 sporadic cases and 65 DLB patients in a 2004 screen, whose authors "conclude this mutation is a rare cause of disease" (**PMID:15304594**); and "previously described mutations and/or missense and/or structural variants of the SNCA gene were not identified" in 651 Indian cases vs 1,327 controls (PMC11018851). Population-database frequencies (gnomAD) for the individual missense alleles were **not** retrieved in this session and should not be asserted.

**Somatic vs germline.** Germline and heterozygous in all established pathogenic cases. A somatic-mutation hypothesis with preliminary data exists (**PMID:23674490**) but is not established; do not encode `variant_origin: SOMATIC`, and the entry does not meet the criteria in the `somatic-mosaicism` skill.

**Functional consequence.** Not loss of function. The missense variants are **gain-of-function at the level of aggregation propensity and membrane interaction**, and the CNVs are a **dosage/hypermorphic** effect. The distinction matters for slot choice: under this repository's rules a variant's consequence belongs in `GeneticContext.functional_impact_category` (`GAIN_OF_FUNCTION`, or `HYPERMORPHIC` for the CNVs), while the *state* of a pathway node takes `Descriptor.modifier`. Mechanistic detail in §6.

**Modifier genes.** None established specifically for SNCA-related PD in the sources retrieved. The one concrete observation is a confounding co-occurrence rather than a modifier: an A53T carrier who also carried a heterozygous *PRKN* variant and had an atypical course (PMID:32849182). *MAPT* interacts with *SNCA* in sporadic PD risk (**PMID:21391235**), but that is the common-variant setting.

**Epigenetics.** **Not retrieved.** *SNCA* intron-1 methylation is a known topic in the sporadic-PD literature, but no primary source was retrieved here and nothing is asserted. Curate as a gap.

**Chromosomal abnormalities.** The CNVs above are the relevant large-scale changes. One large duplication (6.4 Mb) produced a distinct FTD-parkinsonism phenotype, and that report noted a trend "toward increasing disease severity and disease penetrance with increasing duplication size" (**PMID:25003242**) — which stands in tension with the meta-analysis finding that size was *not* associated with onset or dementia (PMID:30619023). Record both; the question is open.

---

## 5. Environmental Information

Not applicable as a cause. SNCA-related PD is monogenic, and no environmental trigger is required. The honest statement for a KB entry is that this section is empty of established disease-level content, with two qualifications:

- **For the locus in sporadic PD**, interaction studies with pesticide exposure (**PMID:18322262**) and head injury (**PMID:25370538**) exist and are association-level.
- **Infectious agents:** not applicable. No pathogen is implicated.
- **Lifestyle factors:** no SNCA-carrier-specific evidence retrieved.

Under this repository's conventions, an `environmental:` block here would need either citable evidence or an explicit `review_notes:` waiver recording what was searched; on the present retrieval, the waiver route is the accurate one.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, as an ordered sequence

**Branch A — gene dosage (duplication/triplication).**

1. Increased *SNCA* copy number (3 or 4 copies) **leads to** proportionally increased *SNCA* transcription and α-synuclein protein. *Demonstrated:* triplication "causes two-fold up-regulation of the alpha-synuclein protein in the brain"; measured in blood and brain of triplication carriers, where "the effect on the aggregated fraction was larger than the effect on soluble alpha-synuclein levels" (Miller et al., **PMID:15159488**), and reproduced in patient iPSC where "SNCA expression is doubled in selected iPSC lines when controlling for efficiency of neuralization" (Devine et al., *Nat Commun* 2011;2:440, **PMID:21863007**).
2. Elevated monomer concentration **results in** exceedance of the concentration threshold for nucleation, hence increased oligomer and fibril formation. *Mechanistically inferred from* the concentration dependence of aggregation plus the measured shift into the aggregated fraction (PMID:15159488).
3. → joins Branch C at step 6.

**Branch B — missense substitution.**

1. A missense substitution in the N-terminal amphipathic region **alters** the protein's conformational equilibrium and its lipid interaction. *Demonstrated per-variant:* "The p.A30P and p.A53T mutations stimulate protofibril formation and smaller to larger aggregates"; "The p.E46K mutation increases the N-terminal positive charge and enhances N-terminal and C-terminal contacts" (PMID:35328025). E46K "markedly increased α-synuclein's binding to negatively charged liposomes" and "increased the rate of filament assembly to the same extent as the A53T mutation" (FEBS Lett 2004, retrieved via secondary summary — re-verify before quoting). A30G shows "rapid conformational change, increase in backbone flexibility near the site of mutation and decrease in α-helical propensity" by molecular dynamics (**PMID:36961209**, computational).
2. **Not all variants accelerate aggregation, and this is important.** A53E "attenuated α-Syn aggregation and amyloid formation without altering the major secondary structure and initial oligomerization tendency" and "showed reduced membrane binding affinity compared to A53T and WT" (**PMID:25268550**; see also **PMID:27938414**, **PMID:29771508**). So the chain through step 2 is **variant-specific, and a single node asserting "mutation increases aggregation" would be false for A53E.** A second route for G51D is tetramer destabilisation: "decreased α-synuclein tetramer-monomer ratios promote Parkinson's disease phenotypes" (**PMID:38424059**, mouse).
3. → joins Branch C at step 6.

**Branch C — the shared downstream cascade.**

6. Misfolded α-synuclein **assembles into** oligomers and then β-sheet-rich amyloid fibrils. *Demonstrated:* fibrils in A53T transgenic mouse inclusions were "10-16 nm wide fibrils resembling those in human pathological inclusions" (Giasson et al., *Neuron* 2002;34:521–533, **PMID:12062037**).
7. Fibril assembly **results in** cytoplasmic inclusion formation — Lewy bodies and Lewy neurites. α-Synuclein is the principal component of Lewy bodies (Spillantini et al., *Nature* 1997;388:839–840, DOI 10.1038/42166; PMID not retrieved).
8. Aggregated α-synuclein **impairs** protein-degradation pathways, which **further raises** the aggregating load — a feed-forward loop. *Demonstrated in vitro:* "A53T and A30P mutants of alpha-synuclein are poorly degraded by CMA, but are instead degraded by macroautophagy," and A30P inhibits chaperone-mediated autophagy (retrieved via citing abstracts; re-verify the primary Cuervo reference before quoting).
9. In parallel, excess α-synuclein **induces** ER stress and the unfolded protein response. *Demonstrated in the patient-derived system:* "Alpha-synuclein induces the unfolded protein response in Parkinson's disease SNCA triplication iPSC-derived neurons" (**PMID:28973645**).
10. Aggregates **cause** mitochondrial dysfunction and bioenergetic failure. *Demonstrated:* "Parkinson's disease alpha-synuclein transgenic mice develop neuronal mitochondrial degeneration and cell death" (**PMID:16399671**); "Cellular α-synuclein pathology is associated with bioenergetic dysfunction in Parkinson's iPSC-derived dopamine neurons" (PMC6548224); oligomers "interact with ATP synthase and open the permeability transition pore" (**PMID:29895861**).
11. Aggregates also **disrupt** synaptic vesicle trafficking and dopamine handling (α-synuclein's physiological role is presynaptic), and **impair nuclear function** — "impaired nuclear function caused by familial Parkinson's disease SNCA mutations" (**PMID:32954426**).
12. Pathological species **transfer** between neurons and **template** aggregation in recipient cells — prion-like propagation. *Demonstrated in vivo:* a single intrastriatal inoculation of synthetic fibrils in wild-type non-transgenic mice "led to cell-to-cell transmission of pathologic α-Syn and Parkinson's-like Lewy pathology in anatomically interconnected regions" (Luk et al., *Science* 2012;338:949–953, **PMID:23161999**; see also **PMID:23436630**). Pathogenic missense variants differ in their transmission efficiency (**PMID:32595456**).
13. Inclusion burden **causes** selective degeneration of dopaminergic neurons of the substantia nigra pars compacta. *Demonstrated with anatomical selectivity:* Lewy pathology accumulation "caused progressive loss of dopamine neurons in the substantia nigra pars compacta, but not in the adjacent ventral tegmental area" (PMID:23161999).
14. Nigral loss **results in** striatal dopamine depletion, "accompanied by reduced dopamine levels culminating in motor deficits" (PMID:23161999) → the motor phenotype of §3.1.
15. **Branch D (cortical/limbic):** where aggregate burden extends to neocortical and limbic regions — characteristic of triplication and of G51D — it **produces** the dementia and psychosis of §3.2. *Demonstrated pathologically:* triplication autopsy showing "severe degeneration of the substantia nigra, widespread subcortical and cortical Lewy bodies, and hippocampal gliosis" compatible with diffuse Lewy body disease (PMC6003950); G51D with "widespread cortical and subcortical neuronal α-synuclein inclusions" (PMID:26306801).
16. **Branch E (neuroinflammation):** aggregates **activate** microglia, and the resulting inflammation is believed to amplify degeneration. Supported by the synucleinopathy neuroinflammation literature (**PMID:26940152**) and by T-cell involvement (**PMID:35034753**); the causal position of this branch (driver vs consequence) was not settled by anything retrieved here, and should be curated as such.

### 6.2 Ontology suggestions for the mechanism nodes

All GO and CL CURIEs below were read from this repository's committed caches.

| Mechanistic step | GO / CL term (verified) |
|---|---|
| Fibril assembly (step 6) | GO:1990000 `amyloid fibril formation` |
| Oligomer/complex assembly | GO:0065003 `protein-containing complex assembly` |
| Inclusion body formation (step 7) | GO:0016234 `inclusion body`; GO:0016235 `aggresome` |
| Membrane/lipid interaction (branch B step 1) | GO:0005543 `phospholipid binding`; GO:0008289 `lipid binding` |
| CMA / macroautophagy failure (step 8) | GO:0061684 `chaperone-mediated autophagy`; GO:0016236 `macroautophagy`; GO:0097352 `autophagosome maturation`; GO:0005776 `autophagosome` |
| Proteasomal route | GO:0010498 `proteasomal protein catabolic process`; GO:0000502 `proteasome complex` |
| ER stress / UPR (step 9) | GO:0034976 `response to endoplasmic reticulum stress` |
| Mitochondrial dysfunction (step 10) | GO:0051882 `mitochondrial depolarization`; GO:0005757 `mitochondrial permeability transition pore complex`; GO:0005743 `mitochondrial inner membrane` |
| Oxidative stress | GO:0034599 `cellular response to oxidative stress` |
| Synaptic vesicle disruption (step 11) | GO:0008021 `synaptic vesicle`; GO:0048488 `synaptic vesicle endocytosis`; GO:0016079 `synaptic vesicle exocytosis`; GO:0035493 `SNARE complex assembly` |
| Dopamine handling | GO:0014059 `regulation of dopamine secretion`; GO:0014046 `dopamine secretion`; GO:0015872 `dopamine transport` |
| Cell-to-cell transfer (step 12) | GO:0009306 `protein secretion` |
| Neuronal death (step 13) | GO:0051402 `neuron apoptotic process` |
| Microglial activation (branch E) | GO:0001774 `microglial cell activation`; GO:0006954 `inflammatory response` |
| Cell types | CL:0000700 `dopaminergic neuron`; CL:0000540 `neuron`; CL:0000129 `microglial cell`; CL:0000127 `astrocyte`; CL:0000128 `oligodendrocyte` (for the GCI-like inclusions in G51D); CL:0007011 `enteric neuron`; CL:0011103 `sympathetic neuron` (dysautonomia) |

### 6.3 Molecular profiling

- **Transcriptomics/proteomics:** the cardinal finding is quantitative and about the gene product itself — a roughly two-fold increase in α-synuclein in triplication brain and blood (PMID:15159488), reproduced in iPSC (PMID:21863007). Expression in iPSC-derived cultures was "heterogeneous," a methodological caveat worth carrying.
- **Metabolomics / lipidomics:** **no SNCA-specific data retrieved.** Curate as a gap.
- **Single-cell / spatial transcriptomics:** none retrieved for SNCA carriers.
- **Functional genomics screens:** none retrieved for this gene in this session.
- **Organoid models:** SNCA-triplication iPSC cortical organoids used to model Lewy body disease and screen drugs (PMC11389790); midbrain organoids from a familial PD patient showing "Lewy Body-like Pathology and Loss of Dopaminergic Neurons" (**PMID:36831291**); isogenic iPSC lines with SNCA multiplications (PMC9581971).

---

## 7. Anatomical Structures Affected

UBERON CURIEs verified against `cache/uberon/terms.csv`.

**Primary.** Nervous system. The substantia nigra pars compacta is the defining site: UBERON:0001965 `substantia nigra pars compacta` (and UBERON:0002038 `substantia nigra`), with selectivity over the adjacent ventral tegmental area demonstrated experimentally (PMID:23161999). Its projection target, UBERON:0002435 `striatum` — UBERON:0001873 `caudate nucleus`, UBERON:0001874 `putamen` — is where dopamine depletion is expressed; Kiely et al. recorded mild caudate neuronal loss in all three G51D cases and none in the H50Q or duplication cases (PMID:26306801).

**Secondary / extranigral.** UBERON:0000956 `cerebral cortex` and UBERON:0001950 `neocortex` (cortical Lewy bodies in triplication and G51D); UBERON:0001876 `amygdala`; UBERON:0002148 `locus ceruleus`; UBERON:0002298 `brainstem`; UBERON:0002870 `dorsal motor nucleus of vagus nerve`; UBERON:0002264 `olfactory bulb` (α-synuclein spread from the olfactory bulb causes hyposmia, anxiety and memory loss in BAC-SNCA mice, **PMID:33547846**); UBERON:0002005 `enteric nervous system` and UBERON:0000948 `heart` for the autonomic involvement behind §3.3. Hippocampal gliosis is described at autopsy in the Iowa triplication kindred (PMC6003950), though `hippocampus` was not in the local cache and its CURIE should be looked up before binding.

**Body systems.** Central nervous, autonomic (sympathetic and parasympathetic), enteric; the urogenital system secondarily (urinary dysfunction, erectile dysfunction, both components of the French cohort's dysautonomia definition).

**Tissue and cell level.** Nervous tissue. Dopaminergic neurons (CL:0000700) are the primary target; cortical and limbic neurons (CL:0000540) in the dementia branch; oligodendrocytes (CL:0000128) carry the GCI-like inclusions that distinguish G51D; microglia (CL:0000129) and astrocytes (CL:0000127) in the inflammatory response — note that astrocytic expression of A53T α-synuclein is itself sufficient to cause neurodegeneration in mice (PMC2873589).

**Subcellular.** Presynaptic terminal and synaptic vesicle (GO:0008021); cytoplasmic inclusion (GO:0016234); mitochondria (GO:0005743, GO:0005741); lysosome/autophagosome (GO:0005765, GO:0005776); nucleus (impaired nuclear function, PMID:32954426).

**Lateralization.** Clinical onset is characteristically **asymmetric** — the individual case descriptions retrieved begin unilaterally ("left hand tremor," "right hand tremor," PMID:26306801) — becoming bilateral with progression. Pathology is bilateral.

---

## 8. Temporal Development

**Onset.** Adult. Insidious, not acute. Age at onset is dosage- and variant-graded; the best-powered figures are Book et al.'s **46.9 ± 10.5 y (CNV3, n = 47, range 30–73)** vs **34.5 ± 7.4 y (CNV4, n = 8, range 28–48)**, p = 0.003 (PMID:30619023), and the French cohort's by-genotype means: A53T 34.7 ± 7.6 (range 26–40), triplication 42 ± 8.5 (36–48), G51D 42.0 ± 15.7 (31–60), duplication 45.3 ± 6.3 (36–56) (PMID:32849182). For context, the same cohort gives *LRRK2* G2019S 51.6 ± 12.8 and *VPS35* D620N 57.1 ± 10.7, against 47.3 in genetically undefined PD. The abstract notes *SNCA* mutations "tended to have earlier age at onset disease (≤ 50 years, p = 0.06)" — 1.5% (16/1,063) of early-onset vs 0.5% (3/636) of late-onset cases.

**A caution on the primary figures.** Book et al.'s Results section states the two means in a direction that reverses the abstract's assignment. The abstract's assignment (higher copy number = earlier onset) is the one consistent with the rest of the paper and with every other source retrieved. A KB entry should cite the abstract's direction and record the internal inconsistency in `notes`.

**Progression.** Progressive and chronic-lifelong; there is no remission, spontaneous or treatment-induced. Levodopa modifies symptoms, not course. Rate is dosage-graded: triplications "cause rapidly progressive PD with earlier onset and extensive Lewy Body pathology," whereas "SNCA duplications cause a phenotype resembling idiopathic PD" (PMID:35328025). Disease duration figures are in §3.5.

**Stages.** No SNCA-specific staging system exists. Two general frameworks apply: Braak/pathological staging — Kiely et al. assigned "PD type, Braak stage 6" to both the duplication and H50Q cases (PMID:26306801) — and, prospectively, the biological staging now being built on seed amplification assays and dopaminergic imaging in sporadic and genetic PD (PMID:37059509).

**Critical periods.** The therapeutically relevant window is the **prodromal period before motor onset**, when an asymptomatic carrier is identifiable by genotype. Two retrieved observations bound it: asymptomatic duplication carriers did **not** show the occipital hypometabolism seen in symptomatic carriers on FDG-PET (Nishioka et al., reported via **PMID:19562770**'s literature context), and in *LRRK2* non-manifesting carriers αSyn-SAA "is negative in the vast majority of NMC," read as suggesting "CSF aggregates are acquired relatively close to disease onset rather than being lifelong" (preprint; treat as provisional). Whether that generalises to *SNCA* carriers — who have the lesion from conception — is an open and mechanistically important question, and a good candidate for a `KNOWLEDGE_GAP` discussion.

**Genetic anticipation.** Reported but not established. A 2023 review observed "a younger onset age in offspring than parent in familial SNCA multiplication PD cases, which supports genetic anticipation" (**PMID:37868923**). There is no repeat-expansion mechanism here to support anticipation in the classical sense; ascertainment bias is the obvious alternative explanation and should be stated alongside.

---

## 9. Inheritance and Population

**Inheritance.** Autosomal dominant — HP:0000006 `Autosomal dominant inheritance` (verified in cache). Heterozygous in all established cases. Two exceptions worth recording: two subjects with **homozygous** duplication in the meta-analysis, and the His50Gln homozygote of inconclusive significance (PMID:30619023, PMID:32849182).

**Penetrance.** **Do not state a penetrance figure.** The meta-analysis is explicit that "the penetrance has yet to be formally defined," reporting only an age-associated cumulative incidence (Kaplan-Meier) computed with affected subjects only and **no censoring for asymptomatic heterozygotes** — i.e. not a penetrance estimate (PMID:30619023). The same paper's introduction notes duplication carriers "may also remain non-penetrant even with advanced age." Against this, one iPSC paper describes triplication as causing "a fully penetrant, aggressive form of Parkinson's disease with dementia" — a statement about one high-dosage genotype, not a quantified estimate. The defensible summary: **age-dependent and incomplete, with penetrance apparently rising with copy number, and formally unquantified.**

**Expressivity.** Markedly variable, within as well as between families. The strongest single illustration is three G51D cases with ages at onset of 19, 69 and 46 years (PMID:26306801). Cross-phenotype variability is equally wide: one duplication presenting as frontotemporal dementia, another family presenting as classic young-onset PD.

**Germline mosaicism, founder effects, consanguinity, carrier frequency.** No germline-mosaicism report retrieved. No classical founder effect retrieved, although p.A30G appears concentrated in Greek families and was described as "an important, albeit rare, cause of genetic PD in the Greek population" after screening an additional 664 unrelated Greek PD patients (PMC11775907, retrieved via search summary — the article itself was blocked, so re-verify before quoting). Consanguinity is not relevant to a dominant disorder. **Carrier frequency is not an applicable concept here** (dominant, adult-onset, no silent carrier state); the relevant figure is mutation frequency among PD patients, below.

**Epidemiology.** **There is no published prevalence or incidence for SNCA-related PD per 100,000, and none should be invented.** What exists is mutation frequency among PD patients, which is the quantity the literature reports:

| Cohort | *SNCA* yield | Source |
|---|---|---|
| 1,805 French/North African index PD cases | **19 (1.1%)** with point mutations or genomic rearrangements: 14 duplications (0.78%), 1 triplication, 3 A53T, 1 G51D; 29 carriers in total | PMID:32849182 |
| Range across recent studies | **0.045%–1.1%** | PMID:35328025 (Table 1) |
| 144 Italian dominant-family probands | 1 duplication (0.7%) | PMID:19833540 |
| 101 familial + 325 sporadic PD + 65 DLB | 0 | PMID:15304594 |
| 651 Indian cases | 0 | PMC11018851 |

Monogenic forms account for roughly 5–10% of all PD (GeneReviews *Monogenic Parkinson Disease Overview*, quoted via search summary as "an estimated 5%-10% of all Parkinson disease (PD) attributed to pathogenic variants in single genes"; the chapter itself could not be fetched). *SNCA* is a small minority within that minority. Among *SNCA* mechanisms, "duplications are more common than missense mutations or triplications" (PMID:35328025).

**Population demographics.** Ethnic distribution "Majority European, then Asians and Hispanics" (PMID:35328025, Table 1). Multiplication families are "rare and globally-distributed" (PMID:30619023; 59 families, 766 individuals in pedigrees). Individual-variant geography: A53T in Italian (Contursi) and Greek families; A30G in Greek families; A53E in Finland, with a first East Asian case (PMID:38867354); E46K in Spanish and Russian-ancestry families (PMID:38661277); G51D in British and French families; triplication in the Iowa kindred; duplications reported from France, Italy, Japan, Turkey and elsewhere. **Sex ratio:** no SNCA-specific figure retrieved.

---

## 10. Diagnostics

**Genetic testing is the diagnostic test**, and the approach must cover two different variant classes, which is the single most practically important point in this section:

1. **Sequencing** (single-gene, multigene PD panel, WES or WGS) detects the eight missense variants. *SNCA* is included on PD panels; Jia et al. report it among the genes present in all panels surveyed (retrieved from that article's model-generated summary rather than verbatim text — verify before quoting).
2. **Copy-number analysis** is required separately, because standard sequencing pipelines miss whole-gene duplications. The methods used in the primary literature are semi-quantitative multiplex PCR, quantitative real-time PCR of *SNCA* exons, **MLPA**, and FISH for confirmation (PMID:14593171, PMID:15451224, PMID:32849182). **A sequencing-only workup will miss the commonest *SNCA* mechanism.** Chromosomal microarray can detect the CNVs; karyotyping cannot. Repeat-expansion and mtDNA testing are not applicable.

**Biomarkers.** The α-synuclein **seed amplification assay (SAA)** on CSF is the major recent development. Siderowf et al. report sensitivity of **98.6% (95% CI 96.4–99.4)** in sporadic PD with typical olfactory deficit, and conclude the assay separates PD from controls with high sensitivity and specificity, reveals molecular heterogeneity, and detects prodromal individuals before diagnosis (*Lancet Neurol* 2023;22:407–417, **PMID:37059509**; commentary **PMID:37059498**; see also **PMID:37100894**). Two caveats carry directly into genetic PD: SAA positivity is **genotype-dependent** — in a 98-participant cohort all 14/14 iPD and 14/14 GBA1-PD were positive versus only 5/13 LRRK2-PD — and absent in *VPS35* D620N and *LRRK2* Y1699C PD (**PMID:41912440**, **PMID:41574889**). For *SNCA* carriers specifically, CSF α-synuclein seeding has been reported alongside PET-MRI in triplication (PMC9476413). Quantitative SAA variants are emerging (**PMID:41042913**), and serial-result consistency has been assessed in PPMI (**PMID:41959813**). Peripheral α-synuclein is elevated in triplication carriers — roughly doubled in blood (PMID:15159488) — which is a biomarker of the dosage lesion rather than of the aggregation state.

**Imaging.** Dopaminergic imaging (DAT-SPECT/PET) documents nigrostriatal denervation, as in idiopathic PD. FDG-PET showed occipital hypometabolism in symptomatic duplication carriers and not in asymptomatic ones (reported via PMID:19562770's context). Structural MRI is used to exclude alternatives. No SNCA-specific imaging signature is established.

**Laboratory tests, electrophysiology, functional tests.** No disease-specific laboratory abnormality. There is no enzyme assay and no circulating metabolite diagnostic. LOINC codes are therefore not asserted here: under this repository's rules a LOINC binding must be read from the cache or the authority at the moment of writing, and no SNCA-specific measurement with a disease-owned cut-off was identified. Note the consequence for the pathograph — several phenotypes here are clinical, not laboratory, readouts.

**Biopsy / pathology.** Diagnosis of synucleinopathy is definitive only at autopsy. Findings: α-synuclein- and ubiquitin-positive Lewy bodies in cortical and subcortical regions with substantia nigra atrophy and no Alzheimer pathology (E46K family, Zarranz et al., DOI 10.1002/ana.10795); diffuse Lewy body disease with severe nigral degeneration, widespread cortical and subcortical Lewy bodies and hippocampal gliosis (triplication, PMC6003950); and for G51D, "widespread cortical and subcortical neuronal α-synuclein inclusions" plus "small numbers of inclusions resembling glial cytoplasmic inclusions (GCIs) in oligodendrocytes," giving pathology with "characteristics of both PD and MSA" (PMID:26306801; see also **PMID:23404372**). That GCI-like oligodendroglial component is the one neuropathological feature that **distinguishes a specific SNCA genotype** from idiopathic PD, and it was absent in the H50Q case and only "sparse coiled-body type" in the duplication case. Relevant HP term: HP:0045007 `Abnormal substantia nigra morphology`.

**Clinical criteria and differential diagnosis.** Diagnosis uses the standard clinical PD criteria (MDS criteria); there are no SNCA-specific criteria. Differential: idiopathic PD (the duplication phenotype is essentially indistinguishable); **multiple system atrophy** (especially for G51D, given both the pyramidal signs and the GCI-like pathology — **PMID:23404372** asks directly whether G51D is "a link between Parkinson's disease and multiple system atrophy?"); dementia with Lewy bodies (for the triplication and E46K phenotypes — Zarranz et al. concluded that "dementia with Lewy bodies is related to α-synuclein mutation"); frontotemporal dementia and FTDP-17 (one duplication case was clinically diagnosed as possible FTDP-17, with no *MAPT* mutation found, PMID:26306801); other monogenic PD (*LRRK2*, *VPS35*, *PRKN*, *PINK1*, *PARK7*, *GBA1*), distinguishable by gene.

**Screening.** No newborn or population screening; neither appropriate nor available for an adult-onset dominant condition. The applicable modality is **cascade predictive testing of at-risk relatives**, which GeneReviews addresses for "SNCA-related adult-onset autosomal dominant PD" (quoted via search summary; chapter not fetched). Because penetrance is unquantified (§9) and no disease-modifying therapy exists (§12), predictive testing here is a counselling-intensive decision rather than a clinical recommendation — see §13.

---

## 11. Outcome / Prognosis

**Survival and mortality.** **No survival rate, life-expectancy figure or mortality rate specific to SNCA-related PD was retrieved**, and none should be stated. The meta-analysis reports no survival or death data in its text; its Figure 2 marks deceased patients but the underlying data are not in the text (PMID:30619023). What that paper does say is directional: age at motor onset and "rate of motor progression to death are correlated with the level of SNCA expression," with higher copy number and overexpression "generally resulting in an earlier demise." In mice, the A53T M83 model is unambiguous — mutant animals "developed a severe and complex motor impairment leading to paralysis and death" (PMID:12062037) — but that is a model-organism result at supraphysiological expression and is not a human prognostic claim.

**Morbidity and function.** The dominant morbidity burden is cognitive and neuropsychiatric rather than purely motor, which is what separates this entity prognostically from idiopathic PD. Dementia in roughly half of multiplication probands (§3.2), with onset at 42.2 ± 7.3 years in CNV4, and 46% of dementia diagnoses arriving within five years of motor onset (PMID:30619023). The longest recorded dementia-free interval was "22 years for CNV3 and 12 years for CNV4." Motor complications are frequent and early: dyskinesias in 60% and fluctuations in 53% of duplication carriers at a mean disease duration of only 6.3 years (PMID:32849182). **Formal quality-of-life instrument data (EQ-5D, SF-36, PROMIS, PDQ-39) specific to SNCA carriers were not retrieved** — curate as a gap.

**Complications.** Dementia; psychosis with visual hallucinations and paranoid delusions; dysautonomia with orthostatic hypotension, urinary and erectile dysfunction; dysphagia (HP:0002015) and its aspiration risk in advanced disease; falls from postural instability; levodopa-induced dyskinesia and motor fluctuations; impulse control disorders. Drug-induced psychosis is a recognised management problem — clozapine (CHEBI:3766) was required for delusions in one A53T carrier (PMID:32849182).

**Recovery potential.** None. Symptomatic treatment produces substantial and sometimes sustained functional improvement, but no retrieved intervention alters the degenerative course.

**Prognostic factors.** The best-evidenced predictor is **genotype**: copy number predicts both onset age and dementia onset age (PMID:30619023), and mechanism class predicts course ("duplications cause a phenotype resembling idiopathic PD"; "triplications cause rapidly progressive PD with earlier onset and extensive Lewy Body pathology," PMID:35328025). Secondary factors: early cognitive involvement; pyramidal signs and poor levodopa response (G51D, A53E) as markers of an atypical, faster course. **Prognostic biomarkers:** CSF SAA seeding kinetics have been linked to cognitive decline in PD, and GBA carrier status to 4/4-positive seeding replicates, in the sporadic/other-genotype setting (retrieved via search summaries); whether seeding quantity predicts progression in *SNCA* carriers was not established by anything retrieved, and the assay's value as a progression marker is explicitly contested (**PMID:41235570**).

---

## 12. Treatment

**There is no disease-modifying therapy for SNCA-related Parkinson disease.** Management is the symptomatic management of parkinsonism, plus treatment of the non-motor burden. Nothing retrieved supports a genotype-specific pharmacological recommendation.

### 12.1 Pharmacotherapy

The agents are those of PD generally. NCIT and CHEBI CURIEs below were read from this repository's committed caches; the pattern follows this repository's convention of a generic NCIT action term plus a `therapeutic_agent` binding.

| Treatment | NCIT action term (verified) | `therapeutic_agent` (verified) |
|---|---|---|
| Levodopa/carbidopa | NCIT:C15986 `Pharmacotherapy` | CHEBI:15765 `L-dopa` (also NCIT:C611 `Levodopa`); CHEBI:3395 `carbidopa` |
| Dopamine agonists | NCIT:C15986 | CHEBI:8356 `pramipexole`; CHEBI:8888 `ropinirole`; CHEBI:48538 `apomorphine`; class term NCIT:C66884 `Dopamine Agonist` |
| MAO-B inhibitors | NCIT:C15986 | CHEBI:63620 `rasagiline`; CHEBI:50217 `selegiline` |
| COMT inhibitor | NCIT:C15986 | CHEBI:4798 `entacapone` |
| Amantadine (for dyskinesia) | NCIT:C15986 | CHEBI:2618 `amantadine` |
| Atypical antipsychotic for PD psychosis | NCIT:C15986 | CHEBI:3766 `clozapine`; CHEBI:8707 `quetiapine` |
| Cholinesterase inhibitor for PD dementia | NCIT:C15986 | CHEBI:8874 `rivastigmine` |

Levodopa responsiveness is the rule but is genotype-patterned, and this is the one clinically actionable genotype–treatment observation retrieved: **100% (15/15) of duplication carriers responsive**, versus **0/2 triplication carriers (poor)** and 2/3 A53T carriers; G51D carriers showed a "mild-to-moderate" response, with one case's good response waning after three years (PMID:32849182, PMID:26306801). **Pharmacogenomics:** nothing *SNCA*-specific retrieved; no PharmGKB/CPIC guideline for this gene was identified.

### 12.2 Advanced therapeutics

- **Immunotherapy (α-synuclein-directed monoclonal antibody).** Prasinezumab is the furthest-developed. The PASADENA phase 2 trial (NCT03100149) was negative on its primary and imaging endpoints: "Prasinezumab therapy had no meaningful effect on global or imaging measures of Parkinson's disease progression as compared with placebo and was associated with infusion reactions" (**PMID:35921451**). A post-hoc exploratory analysis suggested slower motor progression in rapidly progressing participants, with the authors cautioning it is exploratory (**PMID:38622249**), and an open-label extension reported a sustained effect (**PMID:39379705**); a Bayesian re-analysis exists (PMC12006898). Suggested NCIT term: NCIT:C20401 `Monoclonal Antibody` as `therapeutic_agent` with NCIT:C15986. **These trials enrolled early-stage PD generally, not *SNCA* carriers**; extending the result to this entity is an inference, not a finding.
- **SNCA-lowering (ASO / siRNA / gene silencing).** Mechanistically the most rational strategy for a dosage disease, and **entirely preclinical** on the evidence retrieved: siRNA review including exosome-mimetic delivery (**PMID:42234812**), non-coding RNA regulation of *SNCA* (**PMID:39094523**), naked siRNA silencing in vivo (PMC2612658), and moderate RNAi normalisation of overexpressed α-synuclein (**PMID:25965551**). **No clinical trial of an SNCA-directed ASO or siRNA was identified in this session.** A safety signal argues for dose caution rather than maximal knockdown: silencing α-synuclein in mature nigral neurons caused "rapid neuroinflammation and subsequent toxicity" (PMC5819572). If curated, this would take `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE` or `SIRNA` with an `oligonucleotide_details` block naming `target_gene: hgnc:11138` and `oligonucleotide_mechanism: RNASE_H_KNOCKDOWN` / `RNAI_KNOCKDOWN` — but only for a specific, sourced agent, not as a generic placeholder.
- **Gene therapy / gene editing / cell therapy.** NCIT:C15238 `Gene Therapy` exists as a term, but no *SNCA*-directed clinical programme was retrieved. Not applicable at present.

### 12.3 Surgical and interventional

**Deep brain stimulation** (NCIT:C21024 `Deep Brain Stimulation`; NCIT:C15329 `Surgical Procedure`). The *SNCA* evidence is **a handful of cases and one very small retrospective series**, and must be reported as such. A multicentre retrospective study of bilateral STN DBS in *SNCA* carriers included **four patients** (three duplications, one missense); the missense carrier had an unfavourable result, though stimulation still helped fluctuations and dyskinesia through last follow-up (PMC8865141). Individual reports: sustained motor improvement four years after surgery with a large LEDD reduction and no post-surgical cognitive impairment in a duplication carrier (PMC12371441); a 60-year-old duplication carrier walking unassisted and independent for most ADLs at one year "without requiring any anti-Parkinson's medication" (**PMID:38145277**). Jia et al.'s Table 1 summarises DBS as "appears to have a good response for duplications, poor response for missense mutations" (PMID:35328025) — a reasonable reading of a very thin evidence base, and one that aligns with the levodopa-response pattern. The broader monogenic-PD DBS meta-analysis reported no *SNCA*-specific result (**PMID:30707228**).

Under this repository's `effect_modifiers` conventions, the duplication-vs-missense difference in both levodopa and DBS response is a candidate `TreatmentEffectModifier` with `effect_modifier_type: GENOTYPE` — but with `modification_analysis: CROSS_STUDY_COMPARISON` or `CROSS_STRATUM_COMPARISON` and no interaction test, which is the weakest basis available.

### 12.4 Supportive and rehabilitative

NCIT:C15747 `Supportive Care`; NCIT:C15315 `Rehabilitation`; NCIT:C15302 `Physical Therapy`; NCIT:C121351 `Occupational Therapy`; speech and swallowing therapy (the NCIT speech-therapy term was not in the local cache and should be looked up before binding). Management of orthostatic hypotension, constipation, urinary dysfunction, and sleep; caregiver support for the dementia burden. All generic to PD; no SNCA-specific protocol retrieved.

### 12.5 Treatment strategy

Genotype-guided care is, at present, limited to **prognostic counselling** (expect earlier onset, earlier and more frequent dementia, earlier motor complications) and to **setting expectations for levodopa and DBS response by mechanism class**. There is no personalised pharmacotherapy. For a *SNCA* carrier the realistic precision-medicine proposition is enrolment in α-synuclein-targeted disease-modification trials, for which this genotype is the mechanistically purest population — the meta-analysis authors conclude exactly that, that these families "may inform SNCA-targeted therapies" (PMID:30619023).

---

## 13. Prevention

**Primary prevention: not available.** The disease is caused by a germline lesion; there is no modifiable risk factor and no immunisation. The only interventions that prevent occurrence are reproductive, below. Nothing retrieved supports a behavioural or environmental prevention claim, and none should be written.

**Secondary prevention (early detection).** Two routes exist, both for already-identified families: cascade genetic testing of at-risk relatives, and — prospectively, not as established practice — biomarker surveillance of asymptomatic carriers using CSF SAA and dopaminergic imaging, on the strength of SAA's demonstrated ability to detect "prodromal individuals before diagnosis" in sporadic PD (PMID:37059509). **Early detection does not currently change outcome**, because no disease-modifying therapy exists, and that is the central ethical fact about screening here.

**Tertiary prevention.** Preventing complications rather than disease: falls prevention and physiotherapy; management of orthostatic hypotension; swallowing assessment to reduce aspiration risk; avoiding dopamine-blocking agents; careful use of dopamine agonists given the impulse-control-disorder signal in carriers (PMID:32849182); early cognitive and psychiatric surveillance given the high dementia and psychosis frequencies.

**Genetic counselling** (NCIT:C15240 `Genetic Counseling`) is the principal preventive intervention, and the counselling problem is unusually sharp: autosomal dominant transmission gives a 50% recurrence risk per pregnancy, while penetrance is formally undefined (§9) and expressivity is wide enough that onset in one G51D family spanned 19 to 69 years. Reproductive options — prenatal testing and preimplantation genetic diagnosis — are technically applicable to a known familial variant, including the CNVs. Predictive testing of asymptomatic adult relatives is addressed by GeneReviews for SNCA-related adult-onset dominant PD (quoted via search summary only; the chapter could not be fetched in this session, and the specific guidance should be read from NBK1223 before being relied on in a KB entry).

**Public health and environmental interventions.** Not applicable to a monogenic disease.

---

## 14. Other Species / Natural Disease

**Taxonomy.** Human disease: *Homo sapiens*, NCBITaxon:9606. Model species are listed in §15.

**Orthologous genes.** *SNCA* orthologs exist across vertebrates (mouse *Snca*, rat *Snca*, zebrafish paralogs). **I did not retrieve the MOD identifiers (MGI, RGD, ZFIN) in this session, and per this repository's rules they must be looked up at the Alliance or NCBI Gene at the moment of writing and committed with their cache rows — never written from memory.** Note the binding rule that applies here: a mouse model's `genes` takes `MGI:`, not `hgnc:11138`, and an uncached MOD identifier passes `just validate-terms` with any label at all, so `just check-gene-namespaces-online` must be run after adding one. Note also that *Drosophila* and *C. elegans* have **no α-synuclein ortholog** — which is why the fly model (§15) works by expressing the *human* protein, and which is a genuine interpretive limitation rather than a footnote.

**Naturally occurring disease in other species.** **No naturally occurring *SNCA*-mutation disease in a non-human species was retrieved**, and OMIA was not consulted in this session. Spontaneous Lewy-body-like pathology has been described in aged non-human primates in the general PD literature, but nothing retrieved here establishes an *SNCA*-genetic counterpart. This section should be curated as a gap, not populated.

**Comparative biology.** α-Synuclein is vertebrate-conserved; evolutionary and structural analysis of the gene with pathological implications has been published (**PMID:27080380**). The mechanistic core — aggregation of a conserved presynaptic protein into fibrillar inclusions that template further aggregation — is conserved well enough that heterologous expression of human α-synuclein reproduces the key features in flies (**PMID:10746727**), which is itself the evidence for conservation of the downstream vulnerability.

**Transmission.** No zoonotic potential; not an infectious disease. The word "prion-like" in §6 describes an intracellular-to-intercellular templating mechanism within an organism (PMID:23161999) and emphatically **not** interorganism transmissibility.

---

## 15. Model Organisms

### 15.1 Mouse

- **A53T transgenic (M83 line).** The reference in-vivo model of a *SNCA* missense mutation. "Mice expressing mutant, but not wild-type, alpha-synuclein developed a severe and complex motor impairment leading to paralysis and death," with age-dependent inclusions whose "10-16 nm wide fibrils resembl[ed] those in human pathological inclusions" (Giasson et al., *Neuron* 2002;34:521–533, **PMID:12062037**). Misfolded α-synuclein is detectable subclinically in M83 blood (**PMID:40637864**). Synucleinopathy is exacerbated on an *Snca*-null background (**PMID:15585343**). **Limitation:** the phenotype is a fatal ascending motor syndrome with prominent spinal/brainstem pathology, driven by supraphysiological prion-promoter-driven expression — it is not nigral-predominant PD. Candidate `ModelMechanismLink`: `PARTIALLY_RECAPITULATES` against the aggregation node, with `divergences` of type `SUPRAPHYSIOLOGICAL_EXPRESSION` and `INCOMPLETE_PHENOTYPE`.
- **A53T mitochondrial model.** "Parkinson's disease alpha-synuclein transgenic mice develop neuronal mitochondrial degeneration and cell death" (**PMID:16399671**) — links the transgene to the step-10 mitochondrial node. Reversible mitochondrial deficits in primary cortical neurons from human A53T (PMC3877382).
- **G51D and "3D" knock-in mice.** "Generation of G51D and 3D mice reveals decreased α-synuclein tetramer-monomer ratios promote Parkinson's disease phenotypes" (**PMID:38424059**) — mechanistically distinct from simple overexpression, and the best available model of a tetramer-destabilising mechanism. A knock-in *Snca* G51D also "disrupts the synaptic localisation of α-synuclein and enhances its propensity for synucleinopathy" (PMC12198753).
- **Astrocyte-targeted A53T.** "Astrocytic expression of Parkinson's disease-related A53T α-synuclein causes neurodegeneration in mice" (PMC2873589) — evidence that the lesion need not be neuron-autonomous.
- **BAC-SNCA.** "α-Synuclein Spread from Olfactory Bulb Causes Hyposmia, Anxiety, and Memory Loss in BAC-SNCA Mice" (**PMID:33547846**) — models the prodromal non-motor features and the propagation route.
- **Fibril-inoculation (non-transgenic).** Not a genetic model but the key mechanistic one: intrastriatal synthetic fibrils in wild-type mice produce interconnected-region Lewy pathology, SNpc-selective (not VTA) dopaminergic loss, dopamine reduction and motor deficits (Luk et al., **PMID:23161999**; **PMID:23436630**). Structurally distinct fibril strains induce different pathology (**PMID:31643109**).

### 15.2 Invertebrate

**Drosophila.** Feany & Bender, *Nature* 2000;404:394–398 (**PMID:10746727**): expression of normal and mutant human α-synuclein in flies produced "adult-onset loss of dopaminergic neurons, filamentous inclusions containing alpha-synuclein, and locomotor dysfunction," and the authors concluded the model "recapitulates the essential features of the human disorder." **Limitations, both important:** the fly has no endogenous α-synuclein, so this is a heterologous gain-of-function system and says nothing about dosage of a native gene; and replication has been contested — one review notes that "some groups have replicated the results while others have failed to, and have argued that dopaminergic histology protocols may undercount these neurons" (see also the methods paper **PMID:18574253**). A larval model has been validated and optimised more recently (**PMID:41040970**).

### 15.3 Human cellular models — the ones that match this disease best

These are the models whose lesion is *the actual human lesion at the actual human dosage*, which is why they matter more here than in most diseases.

- **SNCA-triplication iPSC.** Devine et al., *Nat Commun* 2011;2:440 (**PMID:21863007**): patient-derived iPSC in which "SNCA expression is doubled in selected iPSC lines when controlling for efficiency of neuralization," with doubled gene dosage confirmed by quantitative genomic PCR of exons 1 and 4. Caveat recorded by the authors: "α-synuclein expression in iPSC-derived neuronal cultures was heterogeneous." Also **PMID:22332244**.
- **Mechanistic findings in that system.** The UPR is induced in SNCA-triplication iPSC-derived neurons (**PMID:28973645**); α-synuclein pathology is associated with bioenergetic dysfunction in PD iPSC dopamine neurons (PMC6548224); α-synuclein dynamics characterised in PARK4 triplication iPSC dopaminergic neurons (PMC7876504); isogenic iPSC lines with *SNCA* multiplications model native and seeded aggregation (PMC9581971); *SNCA* alterations modulate tyrosine hydroxylase in human iPSC-derived neurons (PMC11204703).
- **Organoids.** SNCA-triplication iPSC-derived cortical organoids used to model Lewy body disease and identify therapeutic drugs (PMC11389790); midbrain organoids from a familial PD patient showing "Lewy Body-like Pathology and Loss of Dopaminergic Neurons" (**PMID:36831291**).
- **Discordant monozygotic twins.** iPSC-derived dopamine neurons revealing differences between monozygotic twins discordant for PD (**PMID:25456120**) — a design that isolates non-genetic contributions.
- **Detection methods.** Pathological α-synuclein aggregates can be detected in human iPSC-derived neurons and tissue (**PMID:33733241**).

### 15.4 Phenotype recapitulation and limitations, summarised

| Model | Recapitulates | Does not capture |
|---|---|---|
| A53T M83 mouse | Aggregation, fibrillar inclusions, progressive motor failure, mitochondrial degeneration | Nigral-predominant degeneration; physiological expression level; levodopa-responsive parkinsonism |
| G51D/3D knock-in mouse | Tetramer–monomer shift, synaptic mislocalisation | Human cortical/limbic dementia phenotype; the pyramidal syndrome |
| Fibril inoculation, wild-type mouse | SNpc-selective loss, propagation, dopamine deficit, motor deficits | The genetic lesion itself; the human time course |
| Drosophila (human α-syn) | Dopaminergic loss, inclusions, locomotor deficit | Endogenous ortholog/dosage biology; contested dopaminergic counts |
| SNCA-triplication iPSC / organoid | **The exact human dosage lesion**; UPR, bioenergetic failure, aggregation | Circuit- and organism-level phenotype; aging; cell-type heterogeneity of the intact brain |

**Resources.** Alliance of Genome Resources, MGI, IMSR, ZFIN, FlyBase for the genetic models; Cellosaurus and the iPSC repositories for the triplication lines. I did not retrieve specific repository accession numbers or MOD allele identifiers in this session; they must be read from the source at curation time.

---

## Summary of gaps for curation

Recording these as gaps is more useful than filling them from memory, and several are genuine open questions rather than retrieval failures:

1. **Penetrance is formally undefined** by the field's own primary source (PMID:30619023) — a `KNOWLEDGE_GAP`, not a missing number.
2. **No prevalence/incidence per 100,000 exists**; only mutation frequency among PD patients (0.045%–1.1%). A `Prevalence` record here should use `measure_type: UNKNOWN` or be omitted rather than converting a mutation yield into a population rate.
3. **Book et al. report conflicting dementia frequencies** (50.9% abstract vs 31/55 = 56.4% Results) and state the two age-at-onset means in opposite directions in abstract vs Results. Record the discrepancy.
4. **H50Q pathogenicity is disputed** — `relationship_type: DISPUTED`, never a `has_subtypes` row.
5. **Duplication size vs severity is contradicted** between PMID:25003242 (trend with size) and PMID:30619023 (no association).
6. **No SNCA-specific survival, QoL-instrument, metabolomic, lipidomic, epigenetic, or single-cell data** were retrieved.
7. **No naturally occurring non-human *SNCA* disease** retrieved; OMIA not consulted.
8. **Prasinezumab evidence is from unselected early PD**, not from *SNCA* carriers — do not let a treatment record imply otherwise.
9. **SAA positivity in asymptomatic *SNCA* carriers** is unresolved and is the most consequential open question for trial design in this entity: the lesion is lifelong, but LRRK2 data suggest seeds appear near onset.
10. **GeneReviews NBK1223 and the MDSGene abstract could not be fetched here**; both must be read directly before their figures are written into a KB entry, and every PMID flagged "not confirmed" above (notably Polymeropoulos 1997, Krüger 1998, Zarranz 2004, Spillantini 1997, Maraganore 2006, Nalls 2019, Liu 2021) must be re-derived with `just fetch-reference` rather than copied from this report.

---

### Sources

[Polymeropoulos 1997 context (Sigma-Aldrich)](https://sigmaaldrich.com/CH/it/tech-docs/paper/78838) · [NHGRI 1997 release, first Parkinson's gene](https://www.genome.gov/10000900/1997-release-first-parkinsons-gene) · [Singleton 2003, triplication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/14593171/) · [Alzforum: Synuclein and Parkinson's—It's All in the Dose](https://alzforum.org/node/35956) · [Chartier-Harlin 2004, duplication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15451224/) · [Ibáñez 2004, causal relation (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15451225/) · [Trinh 2018, MDSGene (PubMed)](https://pubmed.ncbi.nlm.nih.gov/30357936/) · [Book 2018, multiplication meta-analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6297377/) · [Lesage 2020, French multicentre cohort (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7399219/) · [Jia 2022, Monogenic PD review (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8950888/) · [GeneReviews, Monogenic Parkinson Disease Overview](https://www.ncbi.nlm.nih.gov/sites/books/NBK1223/) · [Zarranz 2004, E46K](https://zendy.io/title/10.1002/ana.10795) · [Lesage 2013, G51D parkinsonian-pyramidal (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23526723/) · [Kiely 2013, G51D PD/MSA link (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23404372/) · [Kiely 2015, G51D vs duplication vs H50Q (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4549856/) · [Appel-Cresswell 2013, H50Q (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23457019/) · [Pasanen 2014, A53E (PubMed)](https://pubmed.ncbi.nlm.nih.gov/24746362/) · [Martikainen, A53E clinical/imaging (PubMed)](https://pubmed.ncbi.nlm.nih.gov/27066564/) · [Ghosh, A53E biophysics (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25268550/) · [A53-site mutation comparison (PubMed)](https://pubmed.ncbi.nlm.nih.gov/29771508/) · [A30G complex phenotype (PubMed)](https://pubmed.ncbi.nlm.nih.gov/34543462/) · [Liu reply on A30G (PubMed)](https://pubmed.ncbi.nlm.nih.gov/34543467/) · [A30G Greek cohort (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11775907/) · [A30G conformational dynamics (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36961209) · [E46K Russian-ancestry family (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38661277/) · [T72M Turkish families (PubMed)](https://pubmed.ncbi.nlm.nih.gov/34229155/) · [First East Asian A53E case (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38867354) · [Mutations cluster around a protein loop (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23669636/) · [SNCA rearrangements: frequency, phenotype, mechanisms (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19139307) · [Genomic investigation of multiplication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/18571778/) · [Iowa triplication fine-mapping (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6003950) · [6.4 Mb duplication, FTD-parkinsonism (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25003242/) · [Expanding the phenotype of duplication carriers (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19562770/?dopt=Abstract) · [SNCA multiplication not a common cause (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15304594/) · [Italian multiplication analysis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19833540/) · [Duplication in sporadic PD (PubMed)](https://pubmed.ncbi.nlm.nih.gov/17625105/?dopt=Abstract) · [Characterization of SNCA multiplication, 2 new cases (PubMed)](https://pubmed.ncbi.nlm.nih.gov/37868923/) · [Turkish duplication sibship (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41738528/) · [Indian SNCA locus resequencing (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11018851/) · [Miller, α-synuclein in blood and brain, triplication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15159488/) · [Devine 2011, triplication iPSC (PubMed)](https://pubmed.ncbi.nlm.nih.gov/21863007/) · [UPR in triplication iPSC neurons (PubMed)](https://pubmed.ncbi.nlm.nih.gov/28973645/) · [Bioenergetic dysfunction in PD iPSC dopamine neurons (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6548224/) · [α-synuclein dynamics in PARK4 triplication iPSC (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7876504/) · [Isogenic iPSC lines with SNCA multiplications (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9581971/) · [Triplication cortical organoids (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11389790/) · [Midbrain organoids, familial PD (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36831291/) · [Discordant monozygotic twins iPSC (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25456120/) · [Detecting aggregates in iPSC neurons and tissue (PubMed)](https://pubmed.ncbi.nlm.nih.gov/33733241/) · [Triplication PET-MRI and CSF seeding (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9476413/) · [Impaired nuclear function from SNCA mutations (PubMed)](https://pubmed.ncbi.nlm.nih.gov/32954426/) · [Oligomers, ATP synthase, permeability transition pore (PubMed)](https://pubmed.ncbi.nlm.nih.gov/29895861) · [A53T mice, mitochondrial degeneration (PubMed)](https://pubmed.ncbi.nlm.nih.gov/16399671/?dopt=Abstract) · [Giasson 2002, M83 A53T mouse (PubMed)](https://pubmed.ncbi.nlm.nih.gov/12062037/) · [Exacerbated synucleinopathy on Snca-null background (PubMed)](https://pubmed.ncbi.nlm.nih.gov/15585343/) · [Misfolded α-synuclein in M83 blood (PubMed)](https://pubmed.ncbi.nlm.nih.gov/40637864/) · [G51D and 3D mice, tetramer-monomer ratio (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38424059/) · [Snca G51D knock-in, synaptic mislocalisation (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12198753/) · [Astrocytic A53T causes neurodegeneration (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2873589/) · [BAC-SNCA olfactory bulb spread (PubMed)](https://pubmed.ncbi.nlm.nih.gov/33547846/) · [Luk 2012, pathological α-synuclein transmission (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23161999/) · [α-synuclein inoculation in nontransgenic mice (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23436630/) · [Structurally distinct fibrils (PubMed)](https://pubmed.ncbi.nlm.nih.gov/31643109/) · [Mutation-dependent cell-to-cell transmission (PubMed)](https://pubmed.ncbi.nlm.nih.gov/32595456/) · [Feany & Bender 2000, Drosophila model (PubMed)](https://pubmed.ncbi.nlm.nih.gov/10746727/?dopt=Abstract&holding=npg) · [Drosophila dopaminergic histology method (PubMed)](https://pubmed.ncbi.nlm.nih.gov/18574253/) · [Validated Drosophila larval synucleinopathy model (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41040970/) · [SNCA evolutionary and structural insights (PubMed)](https://pubmed.ncbi.nlm.nih.gov/27080380/) · [Neuroinflammation in synucleinopathies (PubMed)](https://pubmed.ncbi.nlm.nih.gov/26940152/) · [T cells, α-synuclein and PD (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35034753/) · [Siderowf 2023, PPMI SAA (PubMed)](https://pubmed.ncbi.nlm.nih.gov/37059509/) · [SAA commentary (PubMed)](https://pubmed.ncbi.nlm.nih.gov/37059498) · [A seed amplification assay to detect PD pathology (PubMed)](https://pubmed.ncbi.nlm.nih.gov/37100894/) · [Quantitative CSF α-synuclein seeds (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41042913/) · [SAA in GBA1 and LRRK2 carriers (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41574889/) · [No CSF seeding in VPS35 D620N / LRRK2 Y1699C (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41912440/) · [Serial SAA consistency in PPMI (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41959813/) · [SAA as progression marker: evidence and uncertainties (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41235570/) · [PASADENA, prasinezumab phase 2 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35921451/) · [Prasinezumab in rapid progressors (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38622249/) · [PASADENA open-label extension (PubMed)](https://pubmed.ncbi.nlm.nih.gov/39379705/) · [PASADENA trial registration NCT03100149](https://clinicaltrials.gov/study/NCT03100149) · [Exosome-mimetic siRNA targeting α-synuclein (PubMed)](https://pubmed.ncbi.nlm.nih.gov/42234812/) · [Non-coding RNAs regulating SNCA (PubMed)](https://pubmed.ncbi.nlm.nih.gov/39094523/) · [In vivo silencing with naked siRNA (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2612658/) · [Moderate RNAi normalisation of α-synuclein (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25965551) · [Silencing α-synuclein in mature nigral neurons causes toxicity (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5819572/) · [STN DBS in SNCA carriers, 10-year follow-up (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8865141/) · [One-year STN DBS in SNCA duplication (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38145277/) · [DBS in α-synuclein-gene-associated PD (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12371441/) · [STN DBS in monogenic PD, meta-analysis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/30707228/) · [Simón-Sánchez GWAS, SNCA rs2736990 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19915575/) · [Multi-ancestry PD GWAS meta-analysis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/38155330/) · [MAPT and SNCA joint effects (PubMed)](https://pubmed.ncbi.nlm.nih.gov/21391235/?dopt=Abstract) · [Common SNCA variants and clinical heterogeneity (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8249472/) · [SNCA risk polymorphisms and progression (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7902914/) · [Rep1 length and non-motor symptoms (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7655210/) · [Rep1 carriers, 4-year non-motor decline (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11892927/) · [α-synuclein, pesticides and PD (PubMed)](https://pubmed.ncbi.nlm.nih.gov/18322262/) · [Head injury and SNCA variability (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25370538/) · [Somatic SNCA mutations hypothesis (PubMed)](https://pubmed.ncbi.nlm.nih.gov/23674490/) · [Alpha-synuclein and familial PD review (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19412953/) · [MONDO:0008200 (OLS4 API)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0008200) · [MONDO:0011764 (OLS4 API)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0011764)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 109 |
| Resolved | 108 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 57 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 34 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 108 |
| On topic | 54 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:32595456` (3 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

30 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35328025` *(abstract only)*: "*SNCA* mutations cause autosomal dominant PD and can be due to different mutation types, including missense variants and multiplications"
  - closest text in source: "Well-established Parkinson's disease genes include autosomal dominant forms (SNCA, LRRK2, and VPS35) and autosomal recessive forms (PRKN, PINK1 and DJ1)"
- `PMC:PMC8950888` *(abstract only)*: "*SNCA* mutations cause autosomal dominant PD and can be due to different mutation types, including missense variants and multiplications"
  - closest text in source: "Well-established Parkinson's disease genes include autosomal dominant forms (SNCA, LRRK2, and VPS35) and autosomal recessive forms (PRKN, PINK1 and DJ1)"
- `PMID:35328025` *(abstract only)*: "early, intermediate, and late onset for triplications, missense mutations, and duplications, respectively"
  - closest text in source: "Additionally, we discuss the role of heterozygous mutations in autosomal recessive genes, the effect of having mutations in two Parkinson's disease genes, the outcome of deep brain stimulation, and the role of genetic testing"
- `PMID:30357936` *(abstract only)*: "pooled data also revealed that SNCA mutation carriers more frequently experienced psychiatric symptoms"
  - closest text in source: "SNCA mutation carriers often have additional psychiatric symptoms, and although not exclusive to only LRRK2 or VPS35 mutation carriers, LRRK2 mutation carriers have a typical form of PD, and, lastly, VPS35 mutation carriers have good response to l-dopa"
- `PMID:32849182` *(abstract only)*: "at least one of the following three signs: orthostatic hypotension, erectile dysfunction, and/or urinary problems"
  - closest text in source: "In the absence of this mutation, the coding sequences of the three genes were analyzed by Sanger sequencing and/or next-generation sequencing"
- `PMID:23526723` *(abstract only)*: "early disease onset, moderate response to levodopa, rapid progression, and marked pyramidal signs including bilateral extensor plantar reflexes, occasionally spasticity, and frequently psychiatric symptoms"
  - closest text in source: "G51D was associated with an unusual PD phenotype characterized by early disease onset, moderate response to levodopa, rapid progression leading to loss of autonomy and death within a few years, marked pyramidal signs including bilateral extensor plantar reflexes, occasionally spasticity, and frequently psychiatric symptoms"
- `PMID:35328025` *(abstract only)*: "So far, there have been eight missense variants identified as causing autosomal dominant PD: p.A30G, p.A30P, p.E46K, p.H50Q, p.G51D, p.A53E, p.A53T, and p.A53V"
  - closest text in source: "Well-established Parkinson's disease genes include autosomal dominant forms (SNCA, LRRK2, and VPS35) and autosomal recessive forms (PRKN, PINK1 and DJ1)"
- `PMID:35328025` *(abstract only)*: "may not have sufficient evidence to be considered pathogenic"
  - closest text in source: "Parkinson's disease may be caused by a single pathogenic variant (monogenic) in 5-10% of cases, but investigation of these disorders provides valuable pathophysiological insights"
- `PMID:32849182` *(abstract only)*: "remains inconclusive"
  - Text part not found as substring: 'remains inconclusive' (note: only abstract available for PMID:32849182, full text may contain this excerpt)
- `PMID:23457019` *(abstract only)*: "disrupts the same amphipathic alpha-helical structure as previously known pathogenic SNCA mutations"
  - closest text in source: "CONCLUSIONS: The substitution's evolutionary conservation and protein modeling provide additional support for pathogenicity as the amino acid perturbs the same amphipathic alpha helical structure as the previously described pathogenic mutations."
- `PMID:19139307` *(abstract only)*: "SNCA genomic duplication results from intra-allelic or inter-allelic recombination with unequal crossing-over, whereas both mechanisms appear to be required for genomic SNCA triplication"
  - closest text in source: "Furthermore, our results indicate that the phenotype associated with SNCA multiplications correlates with the number of copies of the gene and provides the first insight into the mechanisms underlying SNCA multiplication."
- `PMID:18571778` *(abstract only)*: "SNCA genomic duplication results from intra-allelic or inter-allelic recombination with unequal crossing-over, whereas both mechanisms appear to be required for genomic SNCA triplication"
  - closest text in source: "SNCA genomic duplication results from intraallelic (segmental duplication) or interallelic recombination with unequal crossing over, whereas both mechanisms appear to be required for genomic SNCA triplication."
- `PMID:35328025` *(abstract only)*: "Majority European, then Asians and Hispanics"
  - Text part not found as substring: 'Majority European, then Asians and Hispanics' (note: only abstract available for PMID:35328025, full text may contain this excerpt)
- `PMID:15159488` *(abstract only)*: "the effect on the aggregated fraction was larger than the effect on soluble alpha-synuclein levels"
  - closest text in source: "However, at the protein level in brain, there was a greater effect on deposition of aggregated forms into insoluble fractions than on net expression of soluble alpha-synuclein."
- `PMID:21863007`: "SNCA expression is doubled in selected iPSC lines when controlling for efficiency of neuralization"
  - closest text in source: "We found that AST-derived neurons expressed approximately double the quantity of SNCA mRNA as NAS-derived neurons, when controlling for efficiency of neuralization by normalizing to the pan-neuronal marker MAPT (Fig"
- `PMID:35328025` *(abstract only)*: "The p.E46K mutation increases the N-terminal positive charge and enhances N-terminal and C-terminal contacts"
  - Text part not found as substring: 'The p.E46K mutation increases the N-terminal positive charge and enhances N-terminal and C-terminal contacts' (note: only abstract available for PMID:35328025, full text may contain this excerpt)
- `PMID:27938414` *(abstract only)*: "showed reduced membrane binding affinity compared to A53T and WT"
  - Text part not found as substring: 'showed reduced membrane binding affinity compared to A53T and WT' (note: only abstract available for PMID:27938414, full text may contain this excerpt)
- `PMID:29771508` *(abstract only)*: "showed reduced membrane binding affinity compared to A53T and WT"
  - closest text in source: "Although in the presence of membrane-mimicking environments, the A53V mutation showed an extent of helix induction capacity similar to that of the WT protein, it exhibited less binding to lipid vesicles"
- `PMID:38424059` *(abstract only)*: "decreased α-synuclein tetramer-monomer ratios promote Parkinson's disease phenotypes"
  - closest text in source: "Mutations in the α-Synuclein (αS) gene promote αS monomer aggregation that causes neurodegeneration in familial Parkinson's disease (fPD)"
- `PMID:12062037` *(abstract only)*: "10-16 nm wide fibrils resembling those in human pathological inclusions"
  - closest text in source: "Moreover, immunoelectron microscopy revealed that the alpha-synuclein inclusions contained 10-16 nm wide fibrils similar to human pathological inclusions"
- `PMID:29895861` *(abstract only)*: "interact with ATP synthase and open the permeability transition pore"
  - closest text in source: "Inducible pluripotent stem cells (iPSC)-derived neurons bearing SNCA triplication, generate α-synuclein aggregates that interact with the ATP synthase and induce PTP opening, leading to neuronal death"
- `PMID:32954426` *(abstract only)*: "impaired nuclear function caused by familial Parkinson's disease SNCA mutations"
  - closest text in source: "Alpha-synuclein SNCA has been implicated in the etiology of Parkinson's disease (PD); however, the normal function of alpha-synuclein protein and the pathway that mediates its pathogenic effect is yet to be discovered"
- `PMID:23161999`: "led to cell-to-cell transmission of pathologic α-Syn and Parkinson's-like Lewy pathology in anatomically interconnected regions"
  - closest text in source: "Here, we found that in wild-type nontransgenic mice, a single intrastriatal inoculation of synthetic α-Syn fibrils led to the cell-to-cell transmission of pathologic α-Syn and Parkinson's-like Lewy pathology in anatomically interconnected regions"
- `PMID:23161999`: "caused progressive loss of dopamine neurons in the substantia nigra pars compacta, but not in the adjacent ventral tegmental area"
  - closest text in source: "Lewy pathology accumulation resulted in progressive loss of dopamine neurons in the substantia nigra pars compacta, but not in the adjacent ventral tegmental area, and was accompanied by reduced dopamine levels culminating in motor deficits"
- `PMID:35328025` *(abstract only)*: "SNCA duplications cause a phenotype resembling idiopathic PD"
  - closest text in source: "In this review, we discuss each genetic form with a focus on genotype, phenotype, pathophysiology, and the geographic and ethnic distribution"
- `PMID:37868923` *(abstract only)*: "a younger onset age in offspring than parent in familial SNCA multiplication PD cases, which supports genetic anticipation"
  - closest text in source: "We also illustrate a younger onset age in offspring than parent in familial SNCA multiplication PD cases"
- `PMID:35328025` *(abstract only)*: "duplications are more common than missense mutations or triplications"
  - closest text in source: "Additionally, we discuss the role of heterozygous mutations in autosomal recessive genes, the effect of having mutations in two Parkinson's disease genes, the outcome of deep brain stimulation, and the role of genetic testing"
- `PMID:35328025` *(abstract only)*: "Majority European, then Asians and Hispanics"
  - Text part not found as substring: 'Majority European, then Asians and Hispanics' (note: only abstract available for PMID:35328025, full text may contain this excerpt)
- `PMC:PMC5819572` *(abstract only)*: "rapid neuroinflammation and subsequent toxicity"
  - closest text in source: "Here we aimed to test the hypothesis that loss of α-syn function within nigrostriatal neurons results in neuronal dysfunction, which subsequently stimulates neuroinflammation"
- `PMID:35328025` *(abstract only)*: "appears to have a good response for duplications, poor response for missense mutations"
  - closest text in source: "Additionally, we discuss the role of heterozygous mutations in autosomal recessive genes, the effect of having mutations in two Parkinson's disease genes, the outcome of deep brain stimulation, and the role of genetic testing"
- `PMID:30619023`: "may inform SNCA-targeted therapies"
  - Text part not found as substring: 'may inform SNCA-targeted therapies'
- `PMID:12062037` *(abstract only)*: "10-16 nm wide fibrils resembl[ed] those in human pathological inclusions"
  - closest text in source: "Moreover, immunoelectron microscopy revealed that the alpha-synuclein inclusions contained 10-16 nm wide fibrils similar to human pathological inclusions"
- `PMC:PMC12198753` *(abstract only)*: "disrupts the synaptic localisation of α-synuclein and enhances its propensity for synucleinopathy"
  - closest text in source: "In summary, G51D mutagenesis of the endogenous Snca rat gene caused reduced synaptic localisation of αSyn, proteomic evidence of early synaptic dysfunction, and enhanced propensity for αSyn pathology."
- `PMID:18574253` *(abstract only)*: "some groups have replicated the results while others have failed to, and have argued that dopaminergic histology protocols may undercount these neurons"
  - closest text in source: "Since then, a number of studies have been published that validate the model or build on it; conversely, a number report an inability to replicate the results and suggest that most protocols for dopaminergic histology underreport the actual numbers of dopaminergic neurons in the insect brain"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:23436630`: "led to cell-to-cell transmission of pathologic α-Syn and Parkinson's-like Lewy pathology in anatomically interconnected regions"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 108 |
| Resolved | 106 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008200` (9 mentions) - the report calls it "OLS4 API"; MONDO calls it **autosomal dominant Parkinson disease 1**
- `DOID:0060367` (1 mention) - the report calls it "DOID"; DOID calls it **Parkinson's disease 1**
- `MONDO:0011764` (4 mentions) - the report calls it "autosomal dominant Parkinson disease 8", "OLS4 API"; MONDO calls it **autosomal dominant Parkinson disease 8**
- `NCIT:C15986` (8 mentions) - the report calls it "Dopamine agonists", "MAO-B inhibitors", "COMT inhibitor", "Amantadine (for dyskinesia)", "Atypical antipsychotic for PD psychosis", "Cholinesterase inhibitor for PD dementia"; NCIT calls it **Pharmacotherapy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0015872` (obsolete dopamine transport) (1 mention)

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0011764` - called "autosomal dominant Parkinson disease 8", "OLS4 API"
- `NCIT:C15986` - called "Dopamine agonists", "MAO-B inhibitors", "COMT inhibitor", "Amantadine (for dyskinesia)", "Atypical antipsychotic for PD psychosis", "Cholinesterase inhibitor for PD dementia"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.