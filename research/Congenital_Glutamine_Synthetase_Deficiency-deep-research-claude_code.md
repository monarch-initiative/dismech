---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T14:39:28.520619'
end_time: '2026-10-29T14:45:03.840896'
duration_seconds: 335.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Glutamine Synthetase Deficiency
  mondo_id: MONDO:0012393
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
  - claude-opus-5-5
  web_search_requests: 7
  num_turns: 23
  total_cost_usd: 2.5345835
  session_id: ba9c45e4-83a0-5de4-8ae1-3ac1f0ec68ec
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 21
  validator_version: 0.4.0
term_validation:
  total_terms: 56
  verified: 52
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 1
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0012393
    reported_labels:
    - MONDO
    ontology_label: congenital brain dysgenesis due to glutamine synthetase deficiency
  - term_id: DOID:0070544
    reported_labels:
    - DOID
    ontology_label: congenital glutamine deficiency
  - term_id: HP:0002418
    reported_labels:
    - verify
    ontology_label: Abnormal midbrain morphology
  - term_id: HP:0000252
    reported_labels:
    - Pt 4
    ontology_label: Microcephaly
  - term_id: HP:0025090
    reported_labels:
    - verify
    ontology_label: Abnormal large intestinal mucosa morphology
  - term_id: GO:0005829
    reported_labels:
    - Subcellular:** cytosol, the GS location
    ontology_label: cytosol
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0006542
    ontology_label: obsolete glutamine biosynthetic process
    replaced_by: GO:1901704
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Glutamine Synthetase Deficiency
- **MONDO ID:** MONDO:0012393 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Glutamine Synthetase Deficiency** covering all of the
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

Still gathering sources. I'm pinning down PMIDs for the later case reports (2019, 2020, and a prenatal deletion) and for the mouse models before I write the report.

Found the main PubMed literature, including a 2020 homozygous deletion case and newer 2025–2026 papers. Now pulling the abstracts.

# Congenital Glutamine Synthetase Deficiency (GLUL, autosomal recessive): research report

**Target:** MONDO:0012393 · OMIM #610015 · ORPHA:71278 · gene *GLUL* (OMIM *138290, chr 1q25.3)
**Category:** Mendelian, inborn error of amino acid biosynthesis

**Before using this report:**
- **Quotes.** My fetch tool would not return verbatim abstracts, so most source statements below are paraphrased. The few short quoted phrases come from search-engine snippets. None of them is ready to use as an evidence `snippet`. Run `just fetch-reference PMID:…` and copy the exact sentence from the cached abstract.
- **Ontology identifiers.** I did not look up any HP, GO, CL, UBERON, CHEBI or NCIT CURIE in this session. They are leads from memory, and every one must be looked up before it is bound.
- **ORPHA:71278.** This code comes from secondary databases (PhenoDis, the GARD record) and should be confirmed in Orphanet.

---

## 1. Disease information

**Overview.** This is an ultra-rare autosomal recessive disorder caused by biallelic loss-of-function variants in *GLUL*. *GLUL* encodes glutamine synthetase (GS; EC 6.3.1.2), the only enzyme that makes glutamine *de novo* from glutamate and ammonia. Without it, glutamine is almost entirely absent from plasma, urine and CSF. Ammonia detoxification is also impaired, causing chronic hyperammonemia.

The core picture is a neonatal epileptic encephalopathy with prenatal-onset brain malformation, mainly abnormal gyration, white-matter disease and atrophy. Some infants also have necrolytic migratory erythema, enteropathy and multi-organ failure. The 2005 index cases died in the neonatal period [PMID:16267323]. Later patients show that early death is not inevitable [PMID:21353613; PMID:22830360; PMID:30440076].

**Identifiers**

| Resource | ID / label |
|---|---|
| MONDO | MONDO:0012393 |
| OMIM | #610015 "Glutamine deficiency, congenital" (GLND); gene *138290 |
| Orphanet | ORPHA:71278 "Congenital brain dysgenesis due to glutamine synthetase deficiency" (verify) |
| DOID | DOID:0070544 |
| GARD | 9848 |
| ICD-10 | E72.8 (other specified disorders of amino-acid metabolism) |
| MedGen | 400638 |

**Synonyms.** Congenital glutamine deficiency; glutamine synthetase deficiency; GS deficiency; GLUL deficiency; congenital brain dysgenesis due to glutamine synthetase deficiency.

**Source of information.** All of it comes from individual-patient case reports, about seven affected individuals or fetuses in total. No registry or cohort exists.

**Allelic disorder that must be kept separate.** Heterozygous *de novo* start-loss and 5′UTR-splice variants in *GLUL* cause a *dominant* disorder, **Developmental and Epileptic Encephalopathy 116 (DEE116)**. The mechanism is the opposite: a stabilized, feedback-insensitive enzyme rather than a missing one, and plasma and CSF glutamine are normal [PMID:38579670; PMID:39985170; PMID:41083803; PMID:42311234]. A dismech entry for DEE116 already exists. The two should not be lumped. Each entry should cross-reference the other as an allelic disorder with the opposite mechanism.

---

## 2. Etiology

- **Causal factor.** Biallelic germline *GLUL* variants, either missense variants at catalytic residues or a whole-gene deletion. Almost all reported families are consanguineous [PMID:27775558].
- **Genetic risk factors.** The only one is parental consanguinity. No susceptibility loci, GWAS signals or modifier genes have been reported.
- **Environmental modifiers (case-level, not causal):**
  - **Valproate:** precipitated hyperammonemic encephalopathy in two compound-heterozygous siblings [PMID:33150193].
  - **Chronic hyperammonemia:** proposed to cause tyrosine nitration of residual GS, which further lowers its activity. This is a hypothesis to explain the falling glutamine in patient 3 [PMID:27775558].
- **Protective factors.** None are known. Residual enzyme activity, for example p.Arg324Ser compared with p.Arg324Cys, correlates with longer survival [PMID:26836257].
- **Gene–environment interaction.** Not studied. Exogenous glutamine partly bypasses the defect (§12).

---

## 3. Phenotypes

All patients reported so far are listed below. "Pt" numbers follow the minireview [PMID:27775558].

| # | Patient | Genotype | Course |
|---|---|---|---|
| 1 | Turkish boy [PMID:16267323] | c.970C>T p.Arg324Cys homozygous | Died day 2 |
| 2 | Turkish girl [PMID:16267323] | c.1021C>T p.Arg341Cys homozygous | Died day 28 |
| 3 | Sudanese boy [PMID:21353613; PMID:22830360] | c.970C>A p.Arg324Ser homozygous | Died at 6 years (respiratory decompensation) |
| 4 | Girl, 30 months at report [PMID:30440076] | c.121C>T p.Arg41Cys homozygous | Alive at report; improving biochemically on treatment |
| 5 | Fetus [PMID:32888207] | Homozygous whole-gene deletion (also removes *RNASEL*) | Prenatal diagnosis |
| 6–7 | Siblings [PMID:33150193] | p.Arg106\*/p.Lys14Asn compound heterozygous | Myoclonic epilepsy; valproate-associated hyperammonemia |

**Clinical phenotypes**

| Phenotype | Type | Onset | Frequency | HPO lead (verify) |
|---|---|---|---|---|
| Neonatal seizures / epileptic encephalopathy (Pt 3: drug-resistant GTC seizures from day 13; Pt 2: multifocal on EEG) | Sign | Neonatal | 4/4 classic patients | Neonatal seizures HP:0032857 (or Seizure HP:0001250); EEE HP:0200134 |
| Brain malformation: near-agyria/lissencephaly, delayed gyration, cerebral and cerebellar atrophy, small frontal lobe | Sign / imaging | Prenatal | 3/3 imaged early | Lissencephaly / Agyria HP:0031882; Cerebral atrophy HP:0002059; Cerebellar atrophy HP:0001272 |
| Hypomyelination / white-matter abnormality; thin corpus callosum | Imaging | Prenatal to infancy | Pt 2, Pt 3 | CNS hypomyelination HP:0003429; Thin corpus callosum HP:0033725 |
| Subependymal / paraventricular cysts | Imaging | Prenatal | Pt 1, Pt 3 | Subependymal cysts HP:0002418 (verify) |
| Ventriculomegaly; dilated posterior fossa | Prenatal US | Prenatal | Pt 1, Pt 2 | Ventriculomegaly HP:0002119 |
| Polyhydramnios; micromelia | Prenatal | Prenatal | Pt 1 | Polyhydramnios HP:0001561; Micromelia HP:0002983 |
| Hypotonia (axial), with hyperreflexia | Sign | Neonatal | Pt 3, Pt 4 | Hypotonia HP:0001252; Hyperreflexia HP:0001347 |
| Microcephaly | Sign | Infancy | Pt 4 | HP:0000252 |
| Global developmental delay / chronic encephalopathy | Sign | Infancy | All survivors | HP:0001263; Encephalopathy HP:0001298 |
| Necrolytic migratory erythema | Skin | Neonatal (Pt 2); 38 months, brief (Pt 3) | 2/4 | Necrolytic migratory erythema HP:0025090 (verify) |
| Severe enteropathy / voluminous diarrhea | GI | Neonatal | Pt 2 | Diarrhea HP:0002014 |
| Multi-organ failure | Systemic | Neonatal | Pt 1, Pt 2 | Multiple organ failure (verify HP term) |
| Facial dysmorphism (flat nasal root, low-set ears, etc.) | Sign | Congenital | Pt 1, Pt 2, fetus | Abnormal facial shape HP:0001999 |
| Neonatal death | Outcome | Neonatal | 2/4 classic patients | Neonatal death HP:0003811 |

**Laboratory phenotypes** (values from PMID:27775558; Pt 1–2 also in PMID:16267323)

| Analyte | Finding | HPO / LOINC lead |
|---|---|---|
| Plasma/serum glutamine | Pt 1: 2 µmol/L; Pt 2: 6 µmol/L (ref about 300–800); Pt 3: 126 then lower | Decreased plasma glutamine (verify HP; "Decreased glutamine in bodily fluids" appears in PhenoDis) |
| CSF glutamine | Pt 1: 11; Pt 2: 12; Pt 3: 50–238 µmol/L (ref about 350–1,280) | Decreased CSF glutamine (verify) |
| Urine glutamine | Pt 1: undetectable; Pt 2: 8 µmol/g creatinine (ref 640–3,230) | — |
| Ammonia | Mild to moderate chronic hyperammonemia (Pt 1: 140 µmol/L; Pt 3 mean about 94, range 38–424) | Hyperammonemia HP:0001987 |
| Brain glutamine on MRS | Reduced; rose with supplementation [PMID:22830360] | — |
| Leukocyte/fibroblast NAD⁺ | Reduced (secondary) [PMID:25896882] | — |
| GS activity | Pt 1 about 12% of wild type in lymphocytes | — |

**Quality of life.** No formal measurement (EQ-5D, PedsQL) exists. In the patients who survive, the main burdens are profound neurodevelopmental disability and refractory epilepsy.

---

## 4. Genetic and molecular information

- **Gene.** *GLUL*, glutamate-ammonia ligase (HGNC symbol GLUL; use lowercase `hgnc:` and take the CURIE from `cache/hgnc/terms.csv` or HGNC). Chr 1q25.3. The 373-amino-acid enzyme forms a decamer (two pentameric rings) [PMID:18005987, Krajewski 2008 crystal structure].

**Pathogenic variants (recessive disease)**

| Variant (NM_002065) | Protein | Type | State | Functional data |
|---|---|---|---|---|
| c.970C>T | p.Arg324Cys | Missense, ATP site | Homozygous | Loss of direct ATP interaction; severe loss of function [PMID:16267323; PMID:26836257] |
| c.1021C>T | p.Arg341Cys | Missense | Homozygous | Destabilizes R340/helix H8, weakens ATP and glutamate binding [PMID:26836257] |
| c.970C>A | p.Arg324Ser | Missense | Homozygous | Keeps water-mediated ATP contact, so higher residual activity and milder course [PMID:26836257] |
| c.121C>T | p.Arg41Cys | Missense | Homozygous | WES; no functional data [PMID:30440076] |
| Whole-gene deletion (also *RNASEL*) | — | Structural (CNV) | Homozygous | Complete null; fetal immune dysfunction attributed to *RNASEL* loss [PMID:32888207] |
| c.316C>T / c.42G>C | p.Arg106\* / p.Lys14Asn | Nonsense / missense | Compound heterozygous | Clinical match; enzymology limited [PMID:33150193] |

- **ACMG / ClinVar.** The NEJM missense variants are listed as pathogenic in ClinVar (verify each record). No ClinGen gene–disease validity curation of the recessive disorder was found. Check `just list-gene-validity` and the ClinGen site.
- **Population frequency.** These alleles are absent or ultra-rare in gnomAD (verify). Biallelic disease depends on consanguinity.
- **Origin.** Germline, inherited from heterozygous carrier parents.
- **Functional consequence.** Loss of function (`LOSS_OF_FUNCTION`, or `PARTIAL_LOSS_OF_FUNCTION` for p.Arg324Ser).
- **Contrast with DEE116.** The dominant disorder's variants act by gain of stabilization. Translation begins at Met18, downstream of the N-terminal degron. The resulting protein is stable and active but no longer degraded in response to glutamine [PMID:38579670].
- **Modifier genes, epigenetics, chromosomal abnormalities.** None are reported, apart from the *RNASEL* co-deletion described above.

---

## 5. Environmental information

There are no environmental, lifestyle or infectious causes. The only reported precipitant is valproate, which worsens hyperammonemia [PMID:33150193]. An unrelated finding is that the pesticide chlorfenapyr destabilizes GLUL protein in liver [PMID:42570757]. That is an acquired GS deficiency, not this disease, and should not be cited as disease evidence.

---

## 6. Mechanism and pathophysiology

**Ordered causal chain**

1. **Biallelic *GLUL* loss-of-function variants** (missense at the catalytic site or deletion) **lead to** loss of GS catalytic activity. The ATP/glutamate binding step of the reaction is impaired [PMID:16267323; PMID:26836257]. *Demonstrated in vitro and in silico.*
2. **Absent GS activity results in** failure of *de novo* glutamine synthesis (glutamate + NH₄⁺ + ATP → glutamine), **causing** systemic glutamine depletion in plasma, urine and CSF [PMID:16267323]. *Demonstrated in patients.*
   - **2a.** Glutamine deficiency in the placenta and fetus, combined with absent GS in fetal brain, **leads to** abnormal cortical development (agyria, delayed gyration), white-matter disease and cysts. *Inferred: the mechanism linking glutamine supply to gyration has not been shown.* Astrocyte-specific *Glul* knockout mice are born without malformations, which argues that systemic or placental glutamine supply matters [PMID:20140959].
3. **Loss of the GS ammonia-fixing step results in** chronic, usually moderate hyperammonemia. This ammonia-fixation step is the perivenous hepatocyte "scavenger" function [PMID:27775558; liver-KO mouse PMID:25870278]. *Demonstrated.*
4. **Loss of astrocyte glutamine production leads to** disruption of the glutamate–glutamine–GABA cycle and reduced substrate for neuronal glutamate and GABA. This **results in** an excitation/inhibition imbalance and epileptic encephalopathy. *Partly inferred in humans.* Cortical-deletion mice develop spontaneous seizures and neurodegeneration [PMID:30053506]. In astrocyte-KO mice, cortical glutamine falls about 14-fold and the pups die on postnatal day 3 [PMID:20140959].
5. **Glutamine depletion leads to** secondary NAD⁺ deficiency, because glutamine is the amide donor for NAD synthetase. Lower NAD⁺ is proposed to add to cellular energy failure [PMID:25896882]. *Demonstrated in patient cells; the clinical contribution is inferred.*
6. **Systemic glutamine starvation of rapidly dividing and glutamine-dependent tissues** (enterocytes, keratinocytes, immune cells) **leads to** enteropathy, necrolytic migratory erythema and multi-organ failure [PMID:16763901]. *Inferred.*
7. **Chronic hyperammonemia may cause** tyrosine nitration that further inactivates residual GS, a proposed feed-forward loop [PMID:27775558]. *Hypothesis.*

**Branch structure.** Step 2 feeds steps 2a, 4, 5 and 6. Step 3 runs in parallel and feeds step 7, which loops back to step 1.

**Ontology leads (all require lookup)**

- **GO biological process:** glutamine biosynthetic process (GO:0006542); ammonia assimilation cycle (GO:0019676); glutamate metabolic process (GO:0006536); NAD biosynthetic process (GO:0009435); cerebral cortex development (GO:0021987); myelination (GO:0042552).
- **GO molecular function:** glutamine synthetase activity (GO:0004356).
- **CL:** astrocyte (CL:0000127); hepatocyte (CL:0000182); oligodendrocyte (CL:0000128); enterocyte (CL:1000347 or similar, verify); keratinocyte (CL:0000312).
- **CHEBI:** L-glutamine (CHEBI:18050); L-glutamate (CHEBI:16015); ammonium (CHEBI:28938); NAD⁺ (CHEBI:57540); nicotinamide (CHEBI:17154).
- **Biological scale tags for nodes:** GS loss is `MOLECULAR`; glutamine depletion and hyperammonemia are `ORGANISM`; cortical malformation is `TISSUE`.

**Omics.** No transcriptomic, proteomic or single-cell datasets specific to the disease were found. MRS shows brain glutamine and glutamate rising on supplementation [PMID:22830360].

---

## 7. Anatomical structures affected

- **Primary organs:** brain, including the cerebral cortex, cerebellum and periventricular white matter (UBERON:0000955, UBERON:0000956, UBERON:0002037; verify). Liver is affected as the site of the ammonia-scavenging defect (UBERON:0002107).
- **Secondary organs:** skin (UBERON:0002097), intestine (UBERON:0000160), and multiple organs in the neonatal-lethal cases.
- **Cells:** astrocytes, perivenous hepatocytes, oligodendrocytes (inferred from hypomyelination), enterocytes, keratinocytes.
- **Subcellular:** cytosol, the GS location (GO:0005829); mitochondria are relevant through ammonia and NAD⁺ effects.
- **Laterality:** bilateral and symmetric, systemic.

---

## 8. Temporal development

- **Onset:** prenatal. Polyhydramnios, ventriculomegaly and gyral abnormalities are seen on fetal ultrasound or MRI. Seizures begin at birth or in the first two weeks.
- **Course:** chronic, progressive or static encephalopathy. Death ranges from day 2 to 6 years.
- **Remission:** none spontaneous. Glutamine supplementation improves alertness and EEG but not structural brain disease [PMID:22830360].
- **Critical window:** the brain malformations arise *in utero*. Any intervention that could prevent them, such as maternal or fetal glutamine supply, would have to be prenatal. This is untested.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). Carrier parents are unaffected, which suggests complete penetrance for biallelic loss of function.
- **Expressivity:** variable, correlating with residual activity. Neonatal-lethal cases had p.Arg324Cys or p.Arg341Cys. The 6-year survivor had p.Arg324Ser, and the sibling pair had a milder epilepsy phenotype.
- **Prevalence:** fewer than 10 individuals reported worldwide. Use `prevalence_class: BELOW_1_IN_1000000` or `measure_type: CASES_IN_LITERATURE`, citing PMID:27775558, which states the disorder had been reported "in only three unrelated patients since its first description in 2005."
- **Populations:** Turkish (two families), Sudanese, Turkish (Pt 4, Kocaeli), Canadian sibship and Canadian fetus. There is no founder effect and the sex ratio is balanced.
- **Anticipation and mosaicism:** not applicable.

---

## 10. Diagnostics

- **First-line biochemistry:** plasma amino acids. Near-absent glutamine *with* hyperammonemia is pathognomonic, because almost every other hyperammonemic disorder (urea-cycle defects) *raises* glutamine. Confirm with CSF and urine amino acids and plasma ammonia.
  - LOINC leads: Glutamine [Moles/volume] in Serum or Plasma; Glutamine in CSF; Ammonia in Plasma. Seed these with `just loinc-seed-cache` and do not type the labels.
- **Brain MRS:** reduced glutamine peak.
- **Enzyme assay:** GS activity in lymphocytes or fibroblasts; research use only.
- **NAD⁺** in leukocytes as a secondary marker [PMID:25896882].
- **Imaging:** fetal and neonatal MRI showing agyria/pachygyria, delayed gyration, hypomyelination, subependymal cysts and atrophy.
- **EEG:** multifocal epileptiform activity or burst suppression.
- **Genetics:** WES or WGS (Pt 4 was diagnosed by WES), epilepsy or lissencephaly gene panels, and CNV analysis or CMA. CNV analysis is essential because a whole-gene deletion has been reported [PMID:32888207]. Prenatal diagnosis by CMA or exome is feasible.
- **Differential diagnosis:**
  - Urea-cycle disorders and organic acidemias: hyperammonemia but *high* glutamine.
  - Other lissencephalies (*LIS1/PAFAH1B1*, *DCX*, tubulinopathies).
  - Other neonatal epileptic encephalopathies.
  - Glucagonoma or zinc deficiency (other causes of necrolytic erythema).
  - **DEE116** (dominant *GLUL*): normal glutamine.
- **Screening:** not on any newborn-screening panel. MS/MS newborn screening could in principle detect low glutamine, but this has not been validated. Carrier testing is appropriate in affected families.

---

## 11. Outcome and prognosis

- **Mortality:** two of the four classic patients died in the neonatal period (days 2 and 28) of multi-organ failure. One died at 6 years of respiratory decompensation [PMID:16267323; PMID:27775558]. The 2011 report concluded that GS deficiency causes severe neurological disease but is not always early-lethal [PMID:21353613].
- **Morbidity:** profound developmental disability, refractory epilepsy, feeding dependence (gastrostomy) and chronic hyperammonemia.
- **Prognostic factors:** residual enzyme activity as determined by genotype [PMID:26836257]; the severity of the brain malformation.
- **Recovery:** structural brain abnormalities did not improve on treatment.

---

## 12. Treatment

All evidence is single-patient or n-of-2 (HUMAN_CLINICAL, case reports).

| Treatment | Evidence | Modality | NCIT lead (verify) |
|---|---|---|---|
| **Enteral / parenteral L-glutamine**, titrated over 4 weeks from 17 to 1,020 mg/kg/day | Well tolerated. Plasma glutamine normalized; CSF glutamine rose but stayed below the reference range; brain glutamine and glutamate rose on MRS; alertness and EEG improved; ammonia did not worsen [PMID:22830360]. Also used in Pt 4 [PMID:30440076] | SMALL_MOLECULE (nutritional) | Pharmacotherapy NCIT:C15986, or Nutritional Support NCIT:C15433, + therapeutic_agent L-glutamine (CHEBI:18050) |
| **Nicotinamide** | Restored NAD⁺ in patient fibroblasts and leukocytes [PMID:25896882]; used clinically in Pt 4 with biochemical improvement [PMID:30440076] | SMALL_MOLECULE | NCIT:C15986 + nicotinamide (CHEBI:17154) |
| **Carglumic acid** (N-carbamylglutamate) | Lowered ammonia (114→68 and 108→80 µmol/L); ammonia and drug levels were inversely correlated (r = −0.86); no recurrence of hyperammonemic encephalopathy [PMID:33150193] | SMALL_MOLECULE | NCIT:C15986 + carglumic acid (CHEBI lookup) |
| **Avoid valproate** | Precipitated hyperammonemic encephalopathy [PMID:33150193] | — | — |
| Antiseizure medication; gastrostomy feeding; supportive care | Standard care | — / SURGERY / OTHER | Supportive Care NCIT:C15747 |

- **Gene therapy, cell therapy, RNA therapies, trials:** none. No ClinicalTrials.gov record was found (verify).
- **Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary:** genetic counseling (NCIT:C15240) for consanguineous carrier couples; prenatal diagnosis or PGT once the familial variants are known; cascade carrier testing.
- **Secondary:** early recognition of low glutamine with hyperammonemia, and early glutamine supplementation. Prenatal or maternal glutamine supply has not been studied.
- **Tertiary:** avoid valproate and other drugs that raise ammonia; manage catabolic stress.
- **Vaccination / public health:** not applicable.

---

## 14. Other species and natural disease

No naturally occurring GS deficiency has been found in companion or farm animals; OMIA should be checked. GS is among the most conserved enzymes, present in bacteria (GlnA), plants and animals. Mouse *Glul* is MGI:95739. Drosophila carries two GS genes; *Gs1* mutants are lethal [Caggese 1992, PMID:1363402].

---

## 15. Model organisms

| Model | Phenotype | How well it matches human disease | Reference |
|---|---|---|---|
| *Glul* null mouse (LacZ knock-in) | Embryonic lethal at E3.5. Cells survive with glutamine in culture. Heavily chimeric embryos reach E16.5, suggesting the defect is not cell-autonomous after implantation | **Fails to recapitulate**: human total deletion survives into fetal life [PMID:32888207] | He 2007, PMID:17557305 |
| Astrocyte-specific KO (hGFAP-Cre) | No malformations or seizures at birth. Cortical glutamine falls about 14-fold, ammonia rises about 1.6-fold. Feeding failure and death on postnatal day 3, rescued in part by artificial feeding | **Partially recapitulates** brain glutamine depletion, but not the malformations | He 2010, PMID:20140959 |
| Cortex/hippocampus-specific KO | Glial dysfunction and perivascular astrogliosis, then spontaneous seizures and neurodegeneration | **Partially recapitulates** epilepsy | Zhou 2019, PMID:30053506 |
| Liver-specific KO | Systemic hyperammonemia and brain RNA oxidation | Recapitulates the ammonia-scavenging defect | Qvartskhava 2015, PMID:25870278 |
| Patient fibroblasts, leukocytes, immortalized stem cells | NAD⁺ deficiency, rescued by nicotinamide | IN_VITRO model of the secondary NAD⁺ mechanism | Hu 2015, PMID:25896882 |
| COS7 / HEK293 expression; molecular-dynamics simulation | Reduced activity of mutant enzymes; ATP and helix-H8 mechanism | IN_VITRO and COMPUTATIONAL | PMID:16267323; PMID:26836257 |

**Knowledge gap (HUMAN_MODEL_MISMATCH).** Complete GS loss kills mouse embryos before implantation, while a human whole-gene deletion survives into fetal life [PMID:32888207]. The species difference in early embryonic or placental glutamine supply is unexplained. A second open question is why astrocyte-KO mice have no malformations: placental, systemic or other non-astrocytic GS may be what matters for cortical gyration.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 16267323 | Häberle et al., NEJM 2005, index cases (R324C, R341C) | HUMAN_CLINICAL + IN_VITRO |
| 16763901 | Häberle et al., JIMD 2006, enteropathy and necrolytic erythema | HUMAN_CLINICAL |
| 21353613 | Häberle et al., Mol Genet Metab 2011, natural course in the third patient | HUMAN_CLINICAL |
| 22830360 | Häberle et al., Orphanet J Rare Dis 2012, glutamine supplementation | HUMAN_CLINICAL |
| 25896882 | Hu et al., JIMD 2015, secondary NAD⁺ deficiency | IN_VITRO (patient cells) |
| 26836257 | Frieg et al., PLoS Comput Biol 2016, variant mechanisms | COMPUTATIONAL + IN_VITRO |
| 27775558 | Spodenkiewicz et al., Biology 2016, minireview | REVIEW_SYNTHESIS |
| 30440076 | Ünal et al., Neuropediatrics 2019, p.R41C, glutamine + nicotinamide | HUMAN_CLINICAL |
| 32888207 | Roifman et al., Clin Genet 2020, homozygous deletion, prenatal | HUMAN_CLINICAL |
| 33150193 | Bennett et al., Child Neurol Open 2020, siblings, carglumic acid | HUMAN_CLINICAL |
| 17557305 · 20140959 · 30053506 · 25870278 | Mouse models (He 2007; He 2010; Zhou 2019; Qvartskhava 2015) | MODEL_ORGANISM |
| 38579670 · 39985170 · 41083803 · 42311234 | Dominant DEE116 (contrast only; not evidence for this entry) | HUMAN_CLINICAL |

**Sources:**
- [PMC5192420 – Minireview (PMID:27775558)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5192420/)
- [PubMed search: GLUL glutamine synthetase deficiency](https://pubmed.ncbi.nlm.nih.gov/?term=GLUL+glutamine+synthetase+deficiency&size=50)
- [PMID:16267323](https://pubmed.ncbi.nlm.nih.gov/16267323/)
- [PMID:39985170 / PMC11930682](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11930682/)
- [PMC11023914 – Jones et al. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11023914/)
- [Neuropediatrics 2019 (Thieme)](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0038-1675637)
- [Child Neurology Open 2020](https://sage.cnpereading.com/doi/10.1177/2329048X20967880)
- [sonar.ch – Roifman 2020](https://sonar.ch/global/documents/199268)
- [PhenoDis ORPHA:71278](https://iegext02.helmholtz-munich.de/phenodis/disease/show/6204)
- [MedGen 400638](https://https.ncbi.nlm.nih.gov/medgen/400638)
- [Disease Ontology DOID:0070544](https://disease-ontology.org/term/DOID:0070544)
- [LOVD GLND](https://databases.lovd.nl/shared/diseases/02890)
- [MGI Glul allele](https://informatics.jax.org/allele/MGI:3715484)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search)
- [dismech DEE116 page](https://dismech.monarchinitiative.org/pages/disorders/Developmental_and_Epileptic_Encephalopathy_116.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012393` (2 mentions) - the report calls it "MONDO"; MONDO calls it **congenital brain dysgenesis due to glutamine synthetase deficiency**
- `DOID:0070544` (4 mentions) - the report calls it "DOID"; DOID calls it **congenital glutamine deficiency**
- `HP:0002418` (1 mention) - the report calls it "verify"; HP calls it **Abnormal midbrain morphology**
- `HP:0000252` (1 mention) - the report calls it "Pt 4"; HP calls it **Microcephaly**
- `HP:0025090` (1 mention) - the report calls it "verify"; HP calls it **Abnormal large intestinal mucosa morphology**
- `GO:0005829` (1 mention) - the report calls it "Subcellular:** cytosol, the GS location"; GO calls it **cytosol**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006542` (obsolete glutamine biosynthetic process) (1 mention) - replaced by `GO:1901704`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006542` (1 mention) - the report calls it "GO biological process:** glutamine biosynthetic process"; GO calls it **obsolete glutamine biosynthetic process**
- `GO:0004356` (1 mention) - the report calls it "GO molecular function:** glutamine synthetase activity"; GO calls it **glutamine synthetase activity**, and lists "L-glutamine synthetase activity" among its other names
- `CL:0000127` (1 mention) - the report calls it "CL:** astrocyte"; CL calls it **astrocyte**
- `CHEBI:18050` (2 mentions) - the report calls it "CHEBI:** L-glutamine"; CHEBI calls it **L-glutamine**
- `UBERON:0002097` (1 mention) - the report calls it "Secondary organs:** skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names
- `NCIT:C15240` (1 mention) - the report calls it "Primary:** genetic counseling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.