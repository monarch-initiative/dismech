---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T23:10:28.332760'
end_time: '2026-11-27T23:13:30.694532'
duration_seconds: 182.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lymph Node Tuberculosis
  mondo_id: MONDO:0005831
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: tuberculous adenitis
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
  web_search_requests: 15
  num_turns: 23
  total_cost_usd: 1.0049749
  session_id: 51b84916-d01f-4bda-af0a-abc3b5f2c303
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 22
  retrieval_calls: 16
  assistant_text_blocks: 2
citation_count: 42
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 15
  validator_version: 0.8.0
term_validation:
  total_terms: 36
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0005831
    reported_labels:
    - MONDO
    ontology_label: lymph node tuberculosis
  - term_id: HP:0032270
    reported_labels:
    - verify
    ontology_label: Optic nerve tram-track sign
  - term_id: CL:0000646
    reported_labels:
    - "Langhans giant cell \u2014 verify ID"
    ontology_label: basal cell
  - term_id: UBERON:0002048
    reported_labels:
    - Secondary sites:** Lung
    ontology_label: lung
  - term_id: GO:0045335
    reported_labels:
    - Subcellular level:** Mtb lives in the phagosome
    ontology_label: phagocytic vesicle
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  service_unreachable: 7
  obsolescence_unchecked: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymph Node Tuberculosis
- **MONDO ID:** MONDO:0005831 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** tuberculous adenitis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lymph Node Tuberculosis** covering all of the
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

Bash can't reach PubMed, so I'm switching to web search to gather sources for the report.

**Interpretation:** This report covers lymph node tuberculosis (tuberculous lymphadenitis, TBL) under the identifier supplied, MONDO:0005831. I could not open the MONDO entry to check it. TBL is an infection, so it has **no causal human gene**. It is caused by bacteria of the *Mycobacterium tuberculosis* complex: mainly *M. tuberculosis*, and *M. bovis* in some settings. Human genes only change how susceptible someone is; none is causal.

**Method:** The PubMed/E-utilities tool calls were blocked in this session, so all evidence comes from web search results, which mostly showed abstract excerpts. A PMID is given only where one appeared in a result; otherwise the source is cited by URL. Ontology IDs (HPO, GO, CL, UBERON, NCIT, CHEBI) are **suggested from my own knowledge and were not checked against the ontologies**. Verify them before loading them into the knowledge base.

---

## 1. Disease Information

**Overview.** TBL is infection of lymph nodes by the *M. tuberculosis* complex. It is the most common form of extrapulmonary TB (EPTB), at about 35% of EPTB cases, and systemic symptoms are usually not prominent ([Handa et al., J Infect Dev Ctries 2012](https://jidc.org/index.php/journal/article/download/22240421/653/13477)). It most often affects the cervical nodes and is easy to confuse with other granulomatous diseases (Deveci et al. 2016, PMID 28058405, [PMC5206468](https://pmc.ncbi.nlm.nih.gov/articles/PMC5206468)). An African meta-analysis also calls TBL "the most frequent form of extra-pulmonary TB" ([Mekonnen et al., PLoS One 2019](https://www.gov.uk/research-for-development-outputs/epidemiology-of-tuberculous-lymphadenitis-in-africa-a-systematic-review-and-meta-analysis)).

**Identifiers**

| System | Code | Note |
|---|---|---|
| MONDO | MONDO:0005831 | As supplied; not checked |
| ICD-10(-CM) | A18.2 Tuberculous peripheral lymphadenopathy | "Tuberculous adenitis" is an inclusion term. Excludes bronchial/mediastinal nodes (A15.4) and mesenteric/retroperitoneal nodes (A18.39) ([AAPC](https://www.aapc.com/codes/icd-10-codes/A18.2); [gesund.bund.de](https://gesund.bund.de/en/icd-code-search/a18-2)) |
| ICD-11 | 1B12.6 Tuberculous peripheral lymphadenopathy | Synonyms include scrofula and tuberculous cervical lymphadenitis. Confirmed intrathoracic node TB goes to 1B10.0 ([findacode](https://findacode.com/icd-11/code-870345553.html)). Taken from a third-party site, not the WHO browser |
| MeSH | Tuberculosis, Lymph Node | Descriptor ID not retrieved |
| OMIM / Orphanet | Not applicable | Infectious disease |

**Synonyms:** tuberculous lymphadenitis, tuberculous adenitis, scrofula (cervical form), scrofulous adenitis, peripheral tuberculous lymphadenitis, lymph node TB (LNTB).

**Data source type:** The evidence is aggregated disease-level data: cohorts, case series, meta-analyses and WHO surveillance. No EHR-level data was used.

## 2. Etiology

**Causal factors (infectious)**
- The main cause is *M. tuberculosis* (NCBITaxon:1773).
- *M. bovis* (NCBITaxon:1765) causes zoonotic cervical lymphadenitis, mainly through raw milk. It colonizes the tonsil or pharynx and spreads to the neck nodes ([FAO review](https://www.fao.org/4/y5516e/y5516e04.htm)).
  - In Tunisia, 11 cervical TBL isolates were *M. bovis*, and most patients reported eating raw dairy ([Pasteur Tunis](https://hal-riip.archives-ouvertes.fr/pasteur-01446692)).
  - In rural Tanzania, 16% of cervical adenitis isolates were *M. bovis* ([UK DFID output](https://www.gov.uk/dfid-research-outputs/isolation-of-mycobacterium-bovis-from-human-cases-of-cervical-adenitis-in-tanzania-a-cause-for-concern)).
  - A 2023 Canadian case involved a teenager who drank unpasteurized milk in Turkey ([CMAJ 2023](https://www.cmaj.ca/content/195/34/E1155)).

**Environmental and demographic risk factors**
- **Female sex**
  - In a Liverpool cohort, 74% of LNTB cases were women, compared with 43% of pulmonary TB controls.
  - In a Houston study of HIV-negative adults, female sex had an OR of 2.6 (P<0.01) ([Houston Methodist](https://scholars.houstonmethodist.org/en/publications/extrathoracic-tuberculosis-lymphadenitis-in-adult-hiv-seronegativ/)).
- **Birthplace**
  - Being born in South or Southeast Asia, India, the Eastern Mediterranean or Africa raised risk in the Houston study.
  - Another cohort reported higher risk in women, people aged 45–64 and people born in Southern Asia.
- **Age and migration:** In a California series (Polesky et al., *Medicine* 2005, DOI 10.1097/01.md.0000189090.52626.7a), patients were mostly young foreign-born women, about 5 years after arriving in the US ([record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_68756752)).
- **HIV and immunosuppression**
  - Immunosuppression is a recognized EPTB risk factor ([BMJ Best Practice summary](https://bestpractice-bmj-com.bibliotheek.ehb.be/topics/en-gb/166/epidemiology)).
  - Findings for TBL specifically are mixed: an Indonesian study of 422 patients found no significant association with HIV, but did find associations with age, sex, nutrition, diabetes and BCG status ([WHJ](https://whj.umi.ac.id/index.php/whj/article/download/158/108)).
  - An Ethiopian study compared diagnostic yield by HIV status (PMID 18713500).
- **TNF blockade or CD4 depletion:** Animal and mechanistic work shows these can reactivate disease in nodes (PMID 32790739; see §6).

**Genetic risk factors (susceptibility only, not causal)**
- **Comparative association study** (Bose, Giri & Varma-Basil, *Genes* 2023; PMID 36672948 per [BVS record](https://pesquisa.bvsalud.org/colombia/resource/es/mdl-36672948)): 63 SNPs in 23 immunity genes were tested. Variants in **LTA4H, P2RX7, CD209 (DC-SIGN) and SP110** "showed susceptibility to LNTB and not PTB". Variants in IFNG, IL12, IL4, TNFB (LTA), IL1RN, TLR2 and TLR4 were associated with pulmonary TB but not LNTB ([preprint](https://preprints.org/manuscript/202212.0065/v1)).
- **IL12RB1 and MBL2:** A Han Chinese study reported association of IL12RB1 rs2305740 G (P=0.040) and MBL2 with TB in general, not TBL specifically (PMID 32349793).
- **Mendelian susceptibility to mycobacterial disease (MSMD):** These rare monogenic inborn errors of IFN-γ immunity predispose to mycobacterial disease, including lymphadenitis after BCG. Genes include IFNGR1, IFNGR2, STAT1, JAK1, IRF8, SPPL2A, IL12B, IL12RB1, IL12RB2, IL23R, ISG15, TYK2, RORC, CYBB and NEMO (IKBKG) ([Bustamante 2020, PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)). IL12RB1 and IFNGR1 together account for about 80% of MSMD cases ([PMC10975294](https://pmc.ncbi.nlm.nih.gov/articles/PMC10975294)). See also the overview at PMID 40656276. MSMD is a separate entity and a rare cause of TBL.

**Protective factors**
- BCG vaccination was a significant factor in the Indonesian study (direction not shown in the excerpt).
- Pasteurizing milk removes the *M. bovis* route (inferred from the transmission evidence above).
- No genetic variants protective against TBL specifically were retrieved.

**Gene–environment interaction:** No TBL-specific evidence was retrieved. The general model is that inborn IFN-γ/IL-12 defects combined with mycobacterial exposure produce disease, and that HIV or anti-TNF therapy act as acquired equivalents.

## 3. Phenotypes

| Phenotype | Suggested HPO | Frequency / characteristics | Source |
|---|---|---|---|
| Painless, slowly enlarging cervical lymphadenopathy | HP:0025289 Cervical lymphadenopathy; HP:0002716 Lymphadenopathy | Most common site; chronic, insidious | PMID 28058405 |
| Matted nodes / cold abscess / sinus tract (scrofuloderma) | HP:0025615 Abscess; HP:0100785 Cutaneous sinus tract (approximate) | Later stages | Handa 2012 |
| Fever, night sweats, weight loss | HP:0001945 Fever; HP:0030166 Night sweats; HP:0001824 Weight loss | "Systemic symptoms are not a prominent feature" | [Handa 2012](https://jidc.org/index.php/journal/article/download/22240421/653/13477) |
| Positive tuberculin skin test | HP:0033472 (verify) | 94% | Polesky 2005 |
| Concomitant pulmonary TB | HP:0032270 (verify) | 41% of patients with an abnormal chest X-ray had culture-positive pulmonary TB | Polesky 2005 |
| Mediastinal lymphadenopathy | HP:0100721 | Thoracic nodes are a frequent site | PMID 32790739; [PMC10695755](https://pmc.ncbi.nlm.nih.gov/articles/PMC10695755/) |
| Paradoxical node enlargement during or after treatment | — | See §8 | PMID 23895938 |

**Quality of life:** No EQ-5D or SF-36 data specific to TBL were retrieved. Effects come mainly from cosmetic disfigurement, draining sinuses and a long course of treatment.

## 4. Genetic/Molecular Information
- **Causal genes:** None. This is an infectious disease.
- **Pathogenic variants and ClinVar classification:** Not applicable, except for MSMD genes in rare monogenic predisposition (§2).
- **Modifier/susceptibility genes:** LTA4H, P2RX7, CD209, SP110 (PMID 36672948).
- **Epigenetic findings, chromosomal abnormalities, somatic variants:** None retrieved; not applicable.
- **Pathogen genetics:** Rifampicin resistance arises from *rpoB* mutations and is detected by Xpert (§10).

## 5. Environmental Information
- **Infectious agents:** *M. tuberculosis* complex (NCBITaxon:77643), specifically *M. tuberculosis* and *M. bovis*.
- **Exposures:** Raw or unpasteurized dairy for *M. bovis*. Pastoral communities in Afar, Ethiopia had little knowledge of this route ([PMC3062609](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3062609/)).
- **Social exposures:** Birth in or migration from high-burden countries (§2).
- **Lifestyle factors** (smoking, alcohol, diabetes) are established for TB in general. Diabetes was associated with TBL in the Indonesian study.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. **Exposure.** Inhaled *M. tuberculosis* reaches the alveoli, or ingested *M. bovis* reaches the tonsil or pharyngeal mucosa. This leads to infection of resident macrophages and dendritic cells. *(FAO review; PMID 32790739.)*
2. **Transport to nodes.** Infected dendritic cells carry bacilli and antigen through afferent lymphatics to the draining nodes (hilar/mediastinal, or cervical after oropharyngeal entry). Priming of T cells is delayed until about 9–11 days after infection. In humans this produces the Ghon complex, a lung lesion plus a granuloma in a thoracic node. *(Shown in animal models; PMID 32790739.)*
3. **Granuloma formation.** IL-12/IFN-γ–driven Th1 immunity leads to granulomas of epithelioid macrophages, Langhans giant cells and lymphocytes inside the node. *(Inferred from the MSMD genetics, PMC7275902.)*
4. **Persistence.** Granulomas disrupt and can replace normal node architecture, and "lymph nodes are generally not able to eliminate the infection". This makes nodes niches for persistence. *(Macaque work: Ganchua et al. 2018, [PMC6211753](https://pmc.ncbi.nlm.nih.gov/articles/PMC6211753); PMID 32790739.)*
5. **Caseation.** Central caseous necrosis develops, leading to fluctuant nodes, cold abscess, and sinus tracts or scrofuloderma. *(Human histopathology; PMID 27144076.)*
6. **Branch A, local disease.** Spread from the primary site via lymphatics or blood leads to peripheral (cervical) TBL, often without lung disease (inferred).
7. **Branch B, reactivation and spread.** HIV, CD4 depletion or TNF neutralization leads to new non-necrotizing granulomas next to old mineralized node granulomas. Bacilli then exit via lymph and the subclavian vein, seeding the lungs and other organs. In macaques, relapse after SIV infection started from both lung and thoracic nodes (PMID 40548727). Infected inflammatory dendritic cells can also spread granulomatous inflammation ([PMC4626772](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4626772/)).
8. **Paradoxical reaction.** Treatment releases antigen and restores immunity, which leads to temporary node enlargement or new nodes during or after therapy. This immunopathogenic mechanism is inferred (PMID 23895938).

**Suggested GO terms:** GO:0002432 granuloma formation; GO:0032609 IFN-γ production; GO:0042742 defense response to bacterium; GO:0070266 necroptotic process / GO:0070265 necrotic cell death; GO:0001773 myeloid dendritic cell activation; GO:0002250 adaptive immune response.

**Suggested CL terms:** CL:0000235 macrophage; CL:0000451 dendritic cell; CL:0000624 CD4+ αβ T cell; CL:0000646 (Langhans giant cell — verify ID); epithelioid cell.

**Pathways:** IL-12/IFN-γ–JAK–STAT1 (Reactome "Interferon gamma signaling"); TNF signaling; LTA4H-regulated eicosanoid balance (inferred from the genetic association).

**Omics, single-cell and spatial data:** No human TBL-node datasets were retrieved. Multimodal profiling of macaque granulomas exists for lung granulomas only ([UMass repository](https://repository.escholarship.umassmed.edu/entities/publication/326dfe8a-f0c4-4b45-afc4-bc73ba9bc121)).

## 7. Anatomical Structures Affected
- **Primary site:** Lymph nodes (UBERON:0000029), mainly cervical nodes (UBERON:0002429). Supraclavicular, axillary, mediastinal (UBERON:0002524), hilar and mesenteric nodes can also be involved.
- **Secondary sites:** Lung (UBERON:0002048), skin (scrofuloderma) and disseminated disease.
- **Body system:** Lymphatic/immune system.
- **Cells:** Macrophages, dendritic cells and T cells (§6).
- **Subcellular level:** Mtb lives in the phagosome (GO:0045335).
- **Laterality:** Usually unilateral cervical. Exact proportions were not retrieved.

## 8. Temporal Development
- **Onset:** Insidious and chronic, over weeks to months. Peak age is young to middle-aged adults, and children are also affected.
- **Course:** Untreated disease progresses from discrete enlarged nodes to matted nodes, abscess and sinus formation.
- **Paradoxical upgrading reactions**
  - Incidence is about 5.7% (4/70) in one study ([Henry Ford pilot](https://scholarlycommons.henryford.com/infectiousdiseases_articles/291)).
  - After treatment ends, the incidence is 8.6 per 100 person-years (95% CI 5.8–12.7) in HIV-negative Koreans (PMID 23895938).
  - PR is more common in LNTB than in pulmonary TB ([PMC10695755](https://pmc.ncbi.nlm.nih.gov/articles/PMC10695755/)).
  - A Karachi nested case-control study found the incidence varies with the definition used ([PMC6943110](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943110/)).
- **Remission:** Remission follows treatment. Residual nodes are common at the end of therapy (§12).

## 9. Inheritance and Population
- **Inheritance:** Not applicable. TBL is acquired. MSMD genes follow AR or AD inheritance (PMC7275902).
- **Global burden**
  - About 10.7 million people fell ill with TB and 1.23 million died in 2024 (WHO Global TB Report 2025; [WHO news](https://www.who.int/news/item/12-11-2025-global-gains-in-tuberculosis-response-endangered-by-funding-challenges)).
  - 16% of notified cases were extrapulmonary ([WHO 2025, notifications](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-diagnosis-and-treatment/2-1-case-notifications)).
  - TBL is about 35% of EPTB (Handa 2012). That gives roughly 5–6% of notified TB as TBL, which is my own estimate, not a reported figure.
- **Geography:** India accounts for about a quarter of global cases. Africa is covered by Mekonnen 2019.
- **Sex and age:** More women than men (§2); young and middle-aged adults.
- **TBL-specific incidence per 100,000:** Not retrieved.

## 10. Diagnostics
- **Fine-needle aspiration (FNA):** First-line. It often yields positive cultures, so surgery is rarely needed first in immunocompetent adults (Polesky 2005). Diagnostic pathway: Sivaratnam et al., *Int J Mycobacteriol* 2020 ([PDF](https://applications.emro.who.int/imemrf/545/Int-J-Mycobacteriology-2020-9-2-107-115-eng.pdf)).
- **Histopathology:** Caseating granulomas, epithelioid cells and Langhans giant cells (PMID 27144076; PMID 23449832). Ziehl–Neelsen acid-fast bacilli staining and culture are also used.
- **Xpert MTB/RIF and Xpert Ultra:** Cochrane review, PMID 33448348.
  - In 1,000 people with 100 LNTB cases, Xpert MTB/RIF would give 118 positives, 37 of them false positives.
  - Ultra would detect 70 cases and miss 30.
  - Specificity against culture was 86.2%. Culture is an imperfect reference standard for nodes.
  - Accuracy is also high in children ([PMC9369894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9369894/)). Specimen type does not change accuracy ([PMC6545759](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6545759/)).
- **Immunologic tests:** Tuberculin skin test (94% positive) and IGRA.
- **Imaging:** Ultrasound and CT. EBUS-TBNA for mediastinal nodes (not retrieved in detail).
- **Genetic testing:** Not used for diagnosis. Consider an MSMD gene panel (IL12RB1, IFNGR1, STAT1 and others) for severe, recurrent or BCG-related disease in children.
- **Differential diagnosis:** Nontuberculous mycobacterial lymphadenitis, lymphoma, metastatic carcinoma, sarcoidosis, cat-scratch disease, fungal infection, reactive hyperplasia (PMID 28058405).

## 11. Outcome/Prognosis
- **Survival:** TBL alone carries low mortality. No disease-specific mortality figures were retrieved.
- **Response to treatment:** In India, nodes resolved by 6 months in 517/551 patients (93.8%) ([operational study](https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c491t-11649ef574f76688b4fb3d4e1c7df188fb8c1601d165431448f852c34c5a4373)).
- **Lower cure rates:**
  - *M. bovis* TBL in Tunisia: 55.5% cure after at least 8 months of treatment.
  - A Philippine series: 63.3% cured at 6 months ([Acta Med Philipp](https://actamedicaphilippina.upm.edu.ph/index.php/acta/article/view/4900)).
- **Complications:** Paradoxical reactions, abscess or sinus formation, scarring, drug resistance and spread of disease.
- **Prognostic factors:** HIV status, *M. bovis* (which is naturally resistant to pyrazinamide; general knowledge, not retrieved here), and drug resistance.

## 12. Treatment
- **Standard regimen:** 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol, then 4 months of isoniazid and rifampicin (2HRZE/4HR).
  - NCIT terms (suggest): isoniazid C584, rifampicin C789, pyrazinamide C766, ethambutol C478.
  - CHEBI terms: isoniazid CHEBI:6030, rifampicin CHEBI:28077, pyrazinamide CHEBI:45285, ethambutol CHEBI:4877.
- **6 vs 9 months:**
  - A Korean randomized trial (46 vs 46 patients; 2HERZ/4HER vs 2HERZ/7HER) found no difference in residual nodes or recurrence ([KNU](https://research.knu.ac.kr/en/publications/prospective-randomized-study-of-six-months-chemotherapy-and-nine-/)).
  - In the Indian study, extending to 9 months gave no extra benefit.
  - A 4-month ofloxacin-containing regimen was non-inferior to the 6-month thrice-weekly regimen in South India ([BMC Infect Dis 2024](https://bmcinfectdis.biomedcentral.com/counter/pdf/10.1186/s12879-024-09511-w.pdf)).
  - A 6-month regimen worked in children (BMJ 1990, [PMC1679938](https://pmc.ncbi.nlm.nih.gov/articles/PMC1679938)).
- **Surgery:** Excision or aspiration for abscesses or diagnosis. It is not routinely first-line (Polesky 2005).
- **Paradoxical reaction:** Continue treatment, aspirate the node, and consider corticosteroids. Evidence for this was not retrieved.
- **Pharmacogenomics:** NAT2 acetylator status affects isoniazid toxicity (general knowledge; not retrieved here).
- **Advanced or gene-based therapies:** None.
- **Trials (NCT numbers):** None retrieved.

## 13. Prevention
- **Primary:** BCG vaccination, mainly against severe disease in childhood; pasteurizing milk and controlling bovine TB for *M. bovis*; treating latent TB infection.
- **Secondary:** Contact tracing and screening migrants from high-burden countries.
- **Tertiary:** Completing treatment under direct observation and drug-susceptibility testing (Xpert detects rifampicin resistance).
- **Public health:** Funding for the WHO End TB Strategy was US$5.9 billion against a $22 billion target, and deaths have fallen 29% since 2015 against a milestone of 75% (WHO 2025).
- **Genetic counseling:** Only relevant for MSMD families.

## 14. Other Species / Natural Disease
- **Cattle** (*Bos taurus*, NCBITaxon:9913) get bovine TB from *M. bovis*. Lesions typically affect the retropharyngeal, bronchial and mediastinal nodes, and the disease is zoonotic through milk ([FAO](https://www.fao.org/4/y5516e/y5516e04.htm)). I did not retrieve detailed data on lymph node lesions in cattle.
- **Other hosts:** Wildlife reservoirs (badger, deer) were not retrieved.
- **OMIA:** No relevant entry found.

## 15. Model Organisms
- **Cynomolgus macaques** (*Macaca fascicularis*, NCBITaxon:9541) show the closest match to human disease: caseous granulomas form in thoracic nodes.
  - Nodes are niches for prolonged persistence, and FDG PET avidity tracks live bacteria (Ganchua 2018, [PMC6211753](https://pmc.ncbi.nlm.nih.gov/articles/PMC6211753)).
  - Cynomolgus macaques control node infection later in infection, while rhesus macaques do not.
  - In the SIV-reactivation model, relapse starts from the nodes (PMID 40548727).
- **Mouse:** Used to study DC trafficking and T-cell priming in draining nodes (PMID 32790739). Mice do not form human-like caseous granulomas; this is a known limitation.
- **Zebrafish/*M. marinum* and mouse granuloma models:** Used to study how granulomas spread ([PMC4626772](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4626772/)).
- **MSMD knockout mice** (Il12rb1, Ifngr1, Stat1) model inborn susceptibility. Details were not retrieved.
- **Gap noted by reviewers:** Studies of vaccines and drugs should measure effects in thoracic nodes, not just the lungs (PMID 32790739).

---

**Main gaps:**
- PMIDs were not retrieved for several key sources (Handa 2012, Mekonnen 2019, Polesky 2005, Ganchua 2018).
- No TBL-specific incidence per 100,000 or QoL data were retrieved.
- No TBL-specific omics data were found.
- All ontology IDs need checking.

---

**Sources:**
- [Deveci 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5206468)
- [Handa 2012](https://jidc.org/index.php/journal/article/download/22240421/653/13477)
- [Mekonnen 2019](https://www.gov.uk/research-for-development-outputs/epidemiology-of-tuberculous-lymphadenitis-in-africa-a-systematic-review-and-meta-analysis)
- [Sivaratnam 2020](https://applications.emro.who.int/imemrf/545/Int-J-Mycobacteriology-2020-9-2-107-115-eng.pdf)
- [PR Karachi](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943110/)
- [PR Korea](https://pubmed.ncbi.nlm.nih.gov/23895938/)
- [PR Henry Ford](https://scholarlycommons.henryford.com/infectiousdiseases_articles/291)
- [Mediastinal LNTB](https://pmc.ncbi.nlm.nih.gov/articles/PMC10695755/)
- [Cochrane Xpert](https://pubmed.ncbi.nlm.nih.gov/33448348/)
- [Xpert children](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9369894/)
- [Xpert MA 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6545759/)
- [Korean 6 vs 9 mo RCT](https://research.knu.ac.kr/en/publications/prospective-randomized-study-of-six-months-chemotherapy-and-nine-/)
- [Indian operational study](https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c491t-11649ef574f76688b4fb3d4e1c7df188fb8c1601d165431448f852c34c5a4373)
- [Philippine series](https://actamedicaphilippina.upm.edu.ph/index.php/acta/article/view/4900)
- [Ofloxacin trial](https://bmcinfectdis.biomedcentral.com/counter/pdf/10.1186/s12879-024-09511-w.pdf)
- [BMJ 1990 children](https://pmc.ncbi.nlm.nih.gov/articles/PMC1679938)
- [Houston risk study](https://scholars.houstonmethodist.org/en/publications/extrathoracic-tuberculosis-lymphadenitis-in-adult-hiv-seronegativ/)
- [Indonesia](https://whj.umi.ac.id/index.php/whj/article/download/158/108)
- [Ethiopia HIV](https://pubmed.ncbi.nlm.nih.gov/18713500/)
- [BMJ Best Practice](https://bestpractice-bmj-com.bibliotheek.ehb.be/topics/en-gb/166/epidemiology)
- [Bose Genes 2023](https://preprints.org/manuscript/202212.0065/v1)
- [MBL2/IL12RB1](https://pubmed.ncbi.nlm.nih.gov/32349793/)
- [Bustamante MSMD 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)
- [MSMD 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10975294)
- [MSMD overview](https://pubmed.ncbi.nlm.nih.gov/40656276/)
- [Ganchua 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7425845/)
- [Ganchua 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6211753)
- [Macaque relapse](https://pubmed.ncbi.nlm.nih.gov/40548727/)
- [DC dissemination](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4626772/)
- [Macaque granuloma profiling](https://repository.escholarship.umassmed.edu/entities/publication/326dfe8a-f0c4-4b45-afc4-bc73ba9bc121)
- [WHO 2025 news](https://www.who.int/news/item/12-11-2025-global-gains-in-tuberculosis-response-endangered-by-funding-challenges)
- [WHO 2025 notifications](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-diagnosis-and-treatment/2-1-case-notifications)
- [FAO M. bovis](https://www.fao.org/4/y5516e/y5516e04.htm)
- [CMAJ 2023](https://www.cmaj.ca/content/195/34/E1155)
- [Tunisia](https://hal-riip.archives-ouvertes.fr/pasteur-01446692)
- [Tanzania](https://www.gov.uk/dfid-research-outputs/isolation-of-mycobacterium-bovis-from-human-cases-of-cervical-adenitis-in-tanzania-a-cause-for-concern)
- [Afar](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3062609/)
- [Polesky 2005](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_68756752)
- [ICD-10 A18.2](https://www.aapc.com/codes/icd-10-codes/A18.2)
- [ICD-11 1B12.6](https://findacode.com/icd-11/code-870345553.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 7 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005831` (2 mentions) - the report calls it "MONDO"; MONDO calls it **lymph node tuberculosis**
- `HP:0032270` (1 mention) - the report calls it "verify"; HP calls it **Optic nerve tram-track sign**
- `CL:0000646` (1 mention) - the report calls it "Langhans giant cell — verify ID"; CL calls it **basal cell**
- `UBERON:0002048` (1 mention) - the report calls it "Secondary sites:** Lung"; UBERON calls it **lung**
- `GO:0045335` (1 mention) - the report calls it "Subcellular level:** Mtb lives in the phagosome"; GO calls it **phagocytic vesicle**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1773` (1 mention) - the report calls it "M. tuberculosis"; NCBITaxon calls it **Mycobacterium tuberculosis**, and lists "Bacterium tuberculosis" among its other names
- `NCBITaxon:1765` (1 mention) - the report calls it "M. bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `UBERON:0000029` (1 mention) - the report calls it "Primary site:** Lymph nodes"; UBERON calls it **lymph node**

### Terms the ontology service could not be reached for

7 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0100785` (1 mention)
- `HP:0033472` (1 mention)
- `HP:0100721` (1 mention)
- `GO:0042742` (1 mention)
- `GO:0070266` (1 mention)
- `GO:0002250` (1 mention)
- `UBERON:0002429` (1 mention)

### Terms whose obsolescence could not be checked

8 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0002716` (1 mention)
- `HP:0025615` (1 mention)
- `HP:0001945` (1 mention)
- `HP:0001824` (1 mention)
- `NCBITaxon:77643` (1 mention)
- `GO:0002432` (1 mention)
- `GO:0001773` (1 mention)
- `CL:0000646` (1 mention)