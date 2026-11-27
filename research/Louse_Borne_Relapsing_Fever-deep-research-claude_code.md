---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T18:24:43.912651'
end_time: '2026-11-26T18:31:20.965019'
duration_seconds: 397.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Louse-Borne Relapsing Fever
  mondo_id: MONDO:0001620
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Relapsing fever, louse-borne
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 20
  total_cost_usd: 1.2667770800000002
  session_id: 7872a580-27fa-4e2d-8f4a-1abd6fa976e9
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 24
  retrieval_calls: 19
  assistant_text_blocks: 5
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.8.0
term_validation:
  total_terms: 47
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 16
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0001620
    reported_labels:
    - NORD
    ontology_label: louse-borne relapsing fever
  - term_id: HP:0001873
    reported_labels:
    - "Marked; platelets 22,000\u201348,000/\xB5L in Turin cases"
    ontology_label: Thrombocytopenia
  - term_id: HP:0001649
    reported_labels:
    - common
    ontology_label: Tachycardia
  - term_id: CL:0000115
    reported_labels:
    - endothelium
    - Tissue/cell level:** vascular **endothelium
    ontology_label: endothelial cell
  labels_variant: 3
  service_unreachable: 16
  obsolescence_unchecked: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Louse-Borne Relapsing Fever
- **MONDO ID:** MONDO:0001620 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Relapsing fever, louse-borne
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Louse-Borne Relapsing Fever** covering all of the
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

Searching the literature on louse-borne relapsing fever now; it's caused by the bacterium *Borrelia recurrentis*, not by a gene.

Continuing research. Let me gather a few more key sources via web fetch on the reviews.

Let me fetch the full details of the most important sources.

I have strong material. A couple more targeted searches on identifiers and clinical complications, then I'll write.

I have enough well-sourced material to write the report. One correction surfaced: the template's framing is for a genetic disease, but LBRF is an infectious disease with no causal human gene — its cause is the spirochete bacterium *Borrelia recurrentis*. I'll state that up front and map the template's gene/variant/model-organism-database sections onto the pathogen's biology where they apply, and mark them "not applicable" where they don't.

---

# Louse-Borne Relapsing Fever (*Borrelia recurrentis* infection) — Disease Characteristics Report

**MONDO:0001620 · ICD-11 1C1J.1 · ICD-10 A68.0 · MeSH D012061 (Relapsing Fever) · DOID:13035 · MedGen C0152061/UID 508863**

> **Interpretation note / disambiguation.** This report covers the infectious disease louse-borne relapsing fever (LBRF). Despite the template's "causal gene(s)" field, **LBRF has no human causal gene** — it is not a Mendelian disorder. Its cause is an **infectious agent: the spirochete bacterium *Borrelia recurrentis***, transmitted between humans by the body louse *Pediculus humanus humanus*. Where the template asks about human genes, variants (ACMG/ClinVar), epigenetics, model-organism knockouts (MGI/ZFIN), etc., those sections are marked *not applicable* and, where useful, re-mapped onto the **pathogen genome** and **experimental infection models**. The report is built on aggregated disease-level literature (systematic reviews, case series, genomics), **not** individual EHR/patient-level data. Several mechanistic claims for *B. recurrentis* are **inferred from its tick-borne relatives** (*B. duttonii*, *B. hermsii*); these are flagged explicitly.

Confirmed citation anchors used throughout: Lescot et al. 2008, *PLoS Genet* 4(9):e1000185, **PMID 18787695** (genome); Kahlig, Neumayr, Paris 2021 *PLoS Negl Trop Dis* 15(3):e0008656, **PMID 33705387** (systematic review Part 2 — mortality/JHR/pregnancy); Kahlig, Paris, Neumayr 2021 *PLoS Negl Trop Dis* 15(3):e0008564 (Part 1 — epidemiology/diagnosis, PMC7951878); Lucchini et al. 2016 *Emerg Infect Dis* 22(2):298–301, DOI 10.3201/eid2202.151768 (Turin series); Fekade et al. 1996 *N Engl J Med* 335:311–315 (anti-TNF/JHR trial); Warrell 2019 *Epidemiol Infect* **PMID 30869050**; Lopez/Hovius/Bergström **PMID 33372163**; Cutler 2015 **PMID 26593261**; Guerrier & Doherty 2011 **PMID 21803390**.

---

## 1. Disease Information

**Overview.** Louse-borne relapsing fever is an acute, often severe systemic bacterial infection characterized by recurrent episodes of high fever separated by afebrile intervals, caused by the blood-borne spirochete ***Borrelia recurrentis***. The relapsing pattern is produced by the bacterium's antigenic variation (see §4, §6). Classically, untreated attacks "resolve by crisis after 4 to 10 (average 5) days," are followed by an "afebrile remission of 5 to 9 days," and recur as "up to 5 relapses of diminishing severity" (Kahlig et al. 2021 Part 2, PMID 33705387). LBRF differs from tick-borne relapsing fever (TBRF) in having **fewer relapses** — "a single relapse characterizes louse-borne relapsing fever" per the MSD/Merck Manuals — and in being transmitted human-to-human by the body louse with **no non-human reservoir** ("no other reservoir for this infection is known"; Lucchini et al. 2016).

**Key identifiers.**
- **MONDO:** MONDO:0001620 (as given; confirmed via NCBI MedGen UID 508863 / Concept C0152061)
- **ICD-11:** 1C1J.1 "Louse-borne relapsing fever" (note: the figure 1C1C that sometimes circulates is **not** supported; the current code is 1C1J.1)
- **ICD-10:** A68.0 (louse-borne relapsing fever)
- **MeSH:** D012061 (umbrella heading "Relapsing Fever"; "Borrelia recurrentis Infection" is a narrower term). No separate MeSH UID for the *B. recurrentis* entry was retrieved.
- **Disease Ontology:** DOID:13035
- **OMIM:** not applicable (infectious disease, no Mendelian entry)
- **Orphanet:** no ORPHA number confirmed in this session.

**Synonyms / alternative names:** louse-borne relapsing fever; LBRF; epidemic relapsing fever; *Borrelia recurrentis* infection; (historical) famine fever, tick fever's "epidemic" counterpart. "Relapsing fever, louse-borne" (template synonym) is standard.

**Data source type:** aggregated, disease-level (systematic reviews pooling 1907–2019 literature; genomics; outbreak case series) — **not** individual EHR-derived.

---

## 2. Etiology

**Primary cause — infectious.** The sole cause is infection with ***Borrelia recurrentis*** (phylum Spirochaetota; family Borreliaceae; genus *Borrelia*, sometimes placed in *Borreliella*/relapsing-fever *Borrelia* group). Genomically, *B. recurrentis* "appeared to be a strain of *B. duttonii*, with a decaying genome" — i.e., a vector-specialized, genome-reduced derivative of the tick-borne species *B. duttonii* (Lescot et al. 2008, PMID 18787695). **CHEBI/CL/gene etiology: not applicable** (no human causal gene, no toxin).

**Risk factors (environmental/epidemiologic — the operative category for this disease):**
- **Body-louse infestation (pediculosis)** — the proximate requirement. Transmission is human→louse→human.
- **Crowding, poverty, displacement, cold climate, infrequent changes of clothing** — classic drivers of body-louse epidemics; historically associated with war, famine, refugee movements, and prisons (Warrell 2019, PMID 30869050; Kahlig Part 1).
- **Migration/refugee status from endemic foci.** The 2015 European re-emergence occurred almost entirely in **young male refugees from the Horn of Africa (Somalia, Eritrea, Ethiopia)** travelling via Sudan/Libya (Lucchini et al. 2016; Warrell 2019).
- **Communal living** — e.g., local acquisition suspected in a Turin building housing "≈600 refugees" (Lucchini et al. 2016).
- **Age/sex:** no intrinsic genetic predisposition; the striking male predominance in recent series reflects the demographics of exposed migrant populations, not biological susceptibility.

**Genetic risk/protective factors (human):** none established. **Not applicable** — no GWAS loci, ClinVar variants, or protective alleles are defined for this infection.

**Protective factors (environmental):** delousing, hygiene, laundering/heat treatment of clothing, and prompt antibiotic treatment of cases (interrupts the human reservoir). Robust **supportive care** may blunt the Jarisch-Herxheimer reaction (hypothesized by Lucchini et al. 2016).

**Gene–environment interactions:** not applicable in the human host. The relevant "G×E" axis is **pathogen genotype × vector** — the bacterium's genome reduction is tied to its specialization for the louse vector (see §4, §6).

---

## 3. Phenotypes

Phenotypes are clinical signs/symptoms and laboratory abnormalities (not behavioral/genetic). Frequencies below are drawn from the Turin series (Lucchini et al. 2016), the general manuals, and the Kahlig reviews; small case series limit precision.

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| **Recurrent/relapsing high fever** (abrupt onset, "crisis" resolution) | Symptom/sign | Acute onset; episodic/relapsing course; defining feature; ~100% | HP:0001945 (Fever); HP:0025142 (Episodic fever) |
| **Severe headache** | Symptom | Early, very common | HP:0002315 |
| **Chills/rigors** | Symptom | With fever spikes | HP:0025143 (Chills) |
| **Myalgia / arthralgia / back pain** | Symptom | "diffuse pain"; common | HP:0003326 (Myalgia); HP:0002829 (Arthralgia) |
| **Nausea/vomiting, abdominal pain, diarrhea** | Symptom | Common GI disturbance | HP:0002017; HP:0002027; HP:0002014 |
| **Thrombocytopenia** | Lab abnormality | Marked; platelets 22,000–48,000/µL in Turin cases | HP:0001873 |
| **Elevated CRP / inflammatory markers** | Lab abnormality | CRP 16–115× ULN; procalcitonin 11.4–21 ng/mL | HP:0011227 (Elevated CRP) |
| **Jaundice / hepatic involvement** | Sign | Common; hepatic failure in severe cases | HP:0000952 (Jaundice); HP:0001399 (Hepatic failure) |
| **Splenomegaly / hepatosplenomegaly** | Sign | Variable (only 1/5 in Turin); splenic rupture is a severe complication | HP:0001744; HP:0001433 |
| **Petechiae / epistaxis / bleeding** | Sign | Petechial rash, epistaxis "common"; cerebral/GI bleeding severe | HP:0000979; HP:0000421 (Epistaxis) |
| **Hypotension/shock** | Sign | Severe cases; also feature of JHR | HP:0001639-adjacent; HP:0001978 (Shock-adjacent) |
| **Myocarditis → pulmonary edema; ARDS** | Sign/complication | Severe; a leading cause of death | HP:0012819 (Myocarditis); HP:0100598 (Pulmonary edema) |
| **Neurologic: meningism, altered consciousness, cranial neuropathy** | Sign | Described but **less common than in TBRF** | HP:0002315/HP:0001298 |
| **Tachycardia** | Sign | "common" | HP:0001649 |

**Age of onset:** any age exposed; in epidemics all ages. **Incubation period 3–12 days** (Lucchini et al. 2016). **Severity:** variable — from self-limited febrile illness to fulminant multi-organ failure. **Progression:** episodic/relapsing; first attack most severe, relapses "of diminishing severity" (Kahlig Part 2). **Quality-of-life impact:** acute and generally reversible with treatment; no validated EQ-5D/SF-36 LBRF data were retrieved (gap).

---

## 4. Genetic / Molecular Information

**Human genetics: not applicable.** No causal/modifier human genes, no pathogenic variants, no epigenetic disease signatures, no chromosomal abnormalities. This section is re-mapped to the **pathogen genome** (Lescot et al. 2008, PMID 18787695).

- **Organism & genome size:** *B. recurrentis* strain A1 — a **fragmented genome of ~1,242,163 bp** (chromosome 930,981 bp + plasmids 311,182 bp), versus *B. duttonii* at ~1,574,910 bp. Abstract: *"The 1,242,163–1,574,910-bp fragmented genomes of B. recurrentis and B. duttonii contain a unique 23-kb linear plasmid."*
- **Genome reduction:** *"B. recurrentis exhibited a 20.4% genome size reduction and appeared to be a strain of B. duttonii, with a decaying genome"* (abstract; note the arithmetic on the table values gives ~21%).
- **Gene content:** total ORFs **990 (B. recurrentis) vs 1,308 (B. duttonii)**; chromosomal pseudogenes **20 vs 2** (accumulated gene decay); rRNA 3, tRNA 32 in both.
- **Loss of DNA-repair genes (key mechanistic claim):** decay is *"possibly due to the accumulation of genomic errors induced by the loss of recA and mutS."* Specifically an **in-frame STOP codon in recA** (tga replacing tgg), and a **frameshift in mutS** plus an in-frame STOP in **smf** — all impaired in *B. recurrentis*.
- **Plasmids:** a unique **23-kb linear plasmid (lp23)** carrying the telomere resolvase gene *resT*; *B. recurrentis* lp124 is the counterpart of *B. duttonii* lp165.
- **Surface-lipoprotein / antigenic-variation gene repertoire (basis of relapse):** sharply **contracted** in *B. recurrentis* — **vlp genes 17 vs 68**; **vsp genes 10 vs 14**; predicted lipoproteins **80 vs 171(+13)**; lipoprotein genome fraction 8.72% vs 13.63%. The *p35*-like antigen (BBK32-like) and Repeat Family 44 are **absent** in *B. recurrentis*. These **vmp/vlp/vsp** (variable large/small protein) genes are the substrate for antigenic switching.
- **Variant classification (ACMG/ClinVar/gnomAD/COSMIC):** not applicable (bacterial genome). Somatic vs germline: not applicable.
- **Functional consequence framing:** the repair-gene losses behave as **loss-of-function** lesions driving reductive genome evolution; the *vmp* system is the **gain-of-evasion** machinery.

Comparative/evolutionary parallel drawn by the authors: *B. recurrentis* is to *B. duttonii* as the louse-borne *Rickettsia prowazekii* is to its less-virulent tick-borne relatives — vector specialization driving rapid genome reduction.

---

## 5. Environmental Information

- **Infectious agent:** *Borrelia recurrentis* (NCBI Taxonomy — genus *Borrelia*; exact taxid not retrieved this session). Gram-negative–type spirochete, ~0.5 µm × 8–20 µm, visible on Giemsa/Wright-stained blood films.
- **Vector:** the **human body louse, *Pediculus humanus humanus*** (= *P. h. corporis*). Humans are the only known reservoir.
- **Transmission route (distinctive):** the louse **does not inoculate spirochetes by its bite**; infection occurs when an infected louse is **crushed on the skin** (or scratched into abrasions/mucosa), releasing spirochetes from its hemolymph — *"infection takes place when they are crushed on skin"* (Lucchini et al. 2016). Lice **cannot pass the infection to progeny** (no transovarial transmission).
- **Environmental/lifestyle drivers:** cold weather, crowding, poverty, war/famine, displacement, poor hygiene and infrequent clothing changes (favoring body-louse infestation). No chemical/toxic/occupational exposures, radiation, smoking/alcohol, or diet are etiologic.
- **CTD/TOXNET/NHANES:** not applicable.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating event → clinical manifestation)

1. **Body-louse infestation** of a human in a crowded/displaced setting → the person is bitten and lice feed on blood.
2. A louse feeding on a spirochetemic person **ingests *B. recurrentis***, which multiplies in the louse **hemolymph** (not gut lumen/salivary route). *(demonstrated for the louse biology)*
3. The infested person **crushes/scratches the louse**, releasing spirochete-laden hemolymph → spirochetes **penetrate intact skin or abrasions/mucosa** → bloodstream. **This is the route, not a salivary bite inoculation** (Lucchini et al. 2016).
4. Spirochetes **replicate freely in blood**, reaching high densities (spirochetemia) → **release of bacterial lipoproteins** triggers innate immune activation → massive **pro-inflammatory cytokine output (TNF-α, IL-6, IL-8)** → **fever, rigors, headache, myalgia, hypotension** (cytokine role demonstrated via the anti-TNF trial, Fekade et al. 1996).
5. Host mounts an **antibody response** against the dominant surface variable-major-protein (Vmp) serotype → agglutination/clearance of that population → **febrile crisis and afebrile remission**. *(mechanism established in relapsing-fever Borrelia; inferred for B. recurrentis from vmp repertoire + relatives)*
6. A **minority subpopulation has switched its expressed vmp gene** (whole-gene replacement at the expression site from a silent archive) → the new serotype **escapes the existing antibodies** → **re-expands → relapse** with a new fever spike. Cycle repeats (fewer times in LBRF than TBRF, consistent with the **contracted vlp/vsp repertoire** — 17 vlp vs 68 — reported by Lescot et al. 2008). *(switching mechanism demonstrated in B. hermsii; inferred for B. recurrentis)*
7. High spirochete burden + cytokine storm → **endothelial/microvascular injury, thrombocytopenia, DIC-like bleeding, hepatic and myocardial injury** → **jaundice, petechiae/epistaxis/cerebral or GI hemorrhage, myocarditis → pulmonary edema, ARDS, shock, splenic rupture** in severe cases.
8. **Branch at treatment:** antibiotic → rapid spirochete lysis → **surge of released lipoproteins → TNF-α/IL-6/IL-8 spike → Jarisch-Herxheimer reaction** (rigors, temperature spike, then hypotension), typically 45 min–2 h after the dose. This is a **demonstrated** cytokine-mediated step: in the randomized trial, **anti-TNF-α Fab cut reactions with rigors from 26/29 controls to 10/20 treated (P=0.006)** and blunted the IL-6/IL-8 rise (Fekade et al. 1996).

### Supporting detail by category
- **Molecular pathways:** TLR2-type recognition of spirochetal lipoproteins → NF-κB → TNF-α/IL-6/IL-8 (cytokine axis empirically central per Fekade 1996). Suggested GO: **GO:0006954 inflammatory response; GO:0032755 positive regulation of IL-6 production; GO:0032760 positive regulation of TNF production; GO:0071222 cellular response to lipopolysaccharide/lipoprotein.**
- **Cellular processes:** innate immune activation of monocytes/macrophages and neutrophils; platelet consumption; endothelial activation. Suggested CL: **CL:0000235 macrophage; CL:0000775 neutrophil; CL:0000232 erythrocyte (spirochetes rosette/interact); CL:0000233 platelet.**
- **Protein dysfunction (pathogen side):** truncated/frameshifted **RecA, MutS, Smf** → loss of homologous recombination/mismatch repair → reductive genome decay (Lescot 2008). The **Vmp lipoproteins** are the functional antigenic-variation effectors.
- **Immune system involvement:** antibody-mediated clearance drives the relapse cycle; evasion via surface-protein switching; cytokine-driven pathology. (A targeted search on complement-factor-related evasion was blocked by a content classifier this session and is not reported.)
- **Tissue-damage mechanisms:** cytokine-mediated microvascular injury, coagulopathy/hemorrhage, hepatic and myocardial injury.
- **Molecular profiling / single-cell / spatial / multi-omics / CRISPR screens:** no human disease omics datasets retrieved — **gap/not applicable** (the relevant functional-genetics evidence is the pathogen genome + *B. hermsii* vmp-knockout work in relatives).

---

## 7. Anatomical Structures Affected

- **Primary compartment:** **blood** (UBERON:0000178) — the spirochete is a blood-borne pathogen; bacteremia is the central event.
- **Organs/systems involved (secondary, via spirochetemia + cytokines):**
  - **Liver** (UBERON:0002107) — hepatitis/jaundice/hepatic failure (hepatobiliary system).
  - **Spleen** (UBERON:0002106) — splenomegaly, risk of **rupture**.
  - **Heart** (UBERON:0000948) — myocarditis → pulmonary edema (cardiovascular system).
  - **Lungs** (UBERON:0002048) — ARDS, pulmonary edema (respiratory system).
  - **Brain/meninges / peripheral & cranial nerves** (UBERON:0000955; UBERON:0002360) — meningism, encephalopathy, cranial neuropathy (nervous system; less than in TBRF).
  - **Skin** (UBERON:0002097) — petechial rash; entry site.
  - **Gastrointestinal tract** (UBERON:0001555) — nausea/vomiting/abdominal pain; GI bleeding.
  - **Bone marrow/hematopoietic** — thrombocytopenia (platelet consumption).
- **Tissue/cell level:** vascular **endothelium** (CL:0000115), hepatocytes (CL:0000182), cardiomyocytes (CL:0000746), platelets, macrophages/neutrophils.
- **Subcellular (GO Cellular Component):** bacterial **outer membrane/cell surface (GO:0009279 Gram-negative-type outer membrane; GO:0009986 cell surface)** where Vmp lipoproteins reside.
- **Localization/lateralization:** systemic/bilateral (bloodstream disease); no lateralization.

---

## 8. Temporal Development

- **Onset:** **acute**, abrupt, following an **incubation of 3–12 days** (Lucchini et al. 2016). Any age exposed.
- **Course:** **episodic/relapsing**. First febrile attack ~4–10 days (avg 5), ending in **crisis**; afebrile remission ~5–9 days; then **relapses of diminishing severity** — classically **fewer in LBRF (often a single relapse)** than in TBRF (Kahlig Part 2; MSD/Merck Manuals).
- **Duration:** self-limited over weeks if survived; **rapidly curtailed by antibiotics** (often a single dose).
- **Critical period / intervention window:** early antibiotic treatment is curative but precipitates the **Jarisch-Herxheimer reaction** within ~45 min–2 h — the key short window requiring monitoring/supportive care.

---

## 9. Inheritance and Population

- **Inheritance:** **not applicable** (infectious; no AD/AR/X-linked/mitochondrial pattern, no penetrance/expressivity/anticipation/founder/consanguinity/carrier-frequency concepts).
- **Geographic distribution:** **endemic stronghold = Ethiopia and surrounding Horn of Africa**; historically "reported mostly from Ethiopia and surrounding countries, where it is endemic" and "an extremely common infection with substantial mortality" there (Lucchini et al. 2016; Kahlig Part 1 — "reports of the disease are largely confined to Ethiopia"). **Virtually disappeared from Europe after World War I**, then **re-emerged in 2015** among East African migrants (Germany/Munich, Italy/Turin, Switzerland, Netherlands) (Warrell 2019; Lucchini et al. 2016).
- **Prevalence/incidence:** no reliable modern population rates; the disease is rare globally and concentrated in epidemics/foci. Precise incidence figures were **not retrievable** (gap). The 2015 European cluster: e.g., ~25 cases at one Munich hospital in ~6 months; 5 cases in Turin (Jun–Sep 2015); 4 in Switzerland.
- **Demographics in recent series:** overwhelmingly **young adult males**, reflecting migrant-population exposure rather than biological sex bias.

---

## 10. Diagnostics

- **Microscopy (mainstay):** **Giemsa/Wright-stained thick and thin peripheral blood smears** during fever reveal extracellular spirochetes — frequently detected incidentally on **malaria films** ("negative for malaria parasites but showed spirochetes"; all 5 Turin diagnoses arose this way). Kahlig Part 2 grades microscopy as diagnostic certainty "B," "almost equal" to PCR in epidemic/endemic settings. **LOINC/SNOMED:** blood film for parasites/spirochetes.
- **Molecular (confirmatory):** **PCR** of blood (e.g., **16S rRNA**), with sequencing matching *B. recurrentis* reference strain A1 at "100% identity" (Lucchini et al. 2016); graded certainty "A." Species-specific targets distinguish *B. recurrentis* from TBRF species.
- **Laboratory abnormalities supporting diagnosis:** marked **thrombocytopenia** (22,000–48,000/µL), very high **CRP** (16–115× ULN), elevated **procalcitonin** (11.4–21 ng/mL), elevated transaminases/bilirubin.
- **Serology:** paired (certainty "C") or single-titre (certainty "D") — limited availability and cross-reactivity; not primary.
- **Animal inoculation:** historically used but "not considered a means of conclusive diagnosis."
- **Overall caveat:** "Microscopy remains the most commonly used method to diagnose LBRF. Data are lacking on sensitivity and specificity of most diagnostic methods" (Kahlig Part 1).
- **Imaging/electrophysiology/biopsy:** ancillary only (e.g., splenomegaly on ultrasound; myocarditis workup). No specific imaging signature.
- **Omics-based diagnostics (RNA-seq/proteomics/metabolomics/epigenomics/liquid biopsy):** **not applicable/not used.**
- **Differential diagnosis:** **malaria** (co-endemic; smears overlap), **tick-borne relapsing fever** (clinically identical, microscopically indistinguishable — historically separated by epidemiology), louse-borne typhus, typhoid, leptospirosis, other arboviral/bacterial febrile illnesses (Kahlig Part 1).
- **Genetic testing (WGS/WES/panels/karyotype/FISH/mtDNA/repeat expansion):** **not applicable** to the human host.
- **Screening:** case finding in at-risk migrant/displaced populations by malaria-film review; delousing of contacts.

---

## 11. Outcome / Prognosis

- **Case-fatality — untreated:** historically cited as **15–40%** (MSD/Merck Manuals) and "between 30% and 80%... during major epidemics." However, Kahlig Part 2's pooled analysis finds untreated CFR **"on average significantly lower than frequently assumed"**: Table 3 overall untreated **~6%** (3.1% excluding an outlier prisoner cohort); among microscopy/PCR-confirmed untreated, **~10.2%** (5.5% excluding prisoners). The highest classic series was McCulloch 1925 (Nigeria), **47.1% (32/68)**, skewed by a prison cohort.
- **Case-fatality — treated:** historically "reduced to 2% to 5%" with antibiotics; Kahlig Table 3 treated overall **~4%** (antibiotics 3.3%, arsenicals 5%). In **2010–2019** treated cases (n=127) overall CFR **6.3%**; **Ethiopian subset 13.2%** vs **European subset ~1.4% (1/72)**. The reviewers note overall CFR has "risen in recent years for reasons that remain unclear."
- **Jarisch-Herxheimer reaction (JHR):** the dominant acute-treatment risk. Reported in **"up to 80% to 90% of treated patients"**; pooled across 42 studies **"JHR was observed in 1,452 of the 2,618 reported cases... 55.8%"** (JHR-focused studies 71.8%, others 50.6%; study-level range 0%–100%). The wide range reflects that **"a clear diagnostic threshold defining antibiotic treatment-induced JHR does not exist."** JHR can be fatal and "probably caused one death" in the early European re-emergence cohort.
- **Complications:** myocarditis→pulmonary edema, ARDS, hepatic failure, cerebral/GI hemorrhage, splenic rupture, shock, neurologic involvement.
- **Pregnancy:** adverse outcomes in **"3 out of 4 pregnancies"** (Kahlig Part 2 abstract); historically "abortion or miscarriage is the usual fate of pregnancy."
- **Recovery:** with prompt treatment and JHR support, recovery is usually complete; no chronic carrier state in survivors.
- **Prognostic factors:** promptness of treatment, severity/organ involvement at presentation, pregnancy, and the JHR; endemic-setting care limitations worsen outcomes.
- **QoL instruments / disability metrics (EQ-5D/SF-36/ICF):** none specific retrieved (gap).

---

## 12. Treatment

- **Antibiotics (curative):** relapsing-fever *Borrelia* are highly antibiotic-susceptible; **a single dose is often curative**.
  - **Tetracyclines — doxycycline** (first line) — NCIT: Doxycycline (C542). Also **tetracycline**.
  - **Macrolides — erythromycin** (alternative, e.g., in pregnancy/children) — NCIT: Erythromycin.
  - **Penicillin** (e.g., procaine penicillin) — used historically; associated with slower clearance and sometimes fewer/attenuated JHR.
  - **Ceftriaxone** — used in recent European cases, especially with CNS concern (doxycycline ± ceftriaxone in Turin series).
- **Jarisch-Herxheimer management (critical):** anticipate within 45 min–2 h; provide **close monitoring, IV fluids, antipyretics, and hemodynamic support**. Mechanistic/experimental therapy: **sheep polyclonal anti-TNF-α Fab** significantly suppressed JHR in a randomized, double-blind, placebo-controlled trial of 49 LBRF patients — reactions with rigors **10/20 (antibody) vs 26/29 (control), P=0.006**, with blunted temperature/IL-6/IL-8 rises (Fekade et al. 1996, *NEJM* 335:311–315). Not a licensed routine therapy; supportive care remains standard.
- **Supportive care:** rehydration, correction of coagulopathy, management of organ complications.
- **Pharmacogenomics / targeted / gene / cell / RNA / immuno-oncology therapies:** **not applicable.**
- **Public-health adjunct:** **delousing** of the patient, contacts, and clothing (interrupts transmission) — see §13.
- **Treatment outcomes:** antibiotics reduce mortality to the low-single-digit percentages (above); the principal residual risk is JHR.

---

## 13. Prevention

- **Primary prevention (core):** **vector/louse control** — personal and environmental **delousing**, hygiene, laundering and heat/insecticide treatment of clothing and bedding; reducing crowding; improving conditions in camps/shelters/prisons (public-health interventions; Warrell 2019; CDC). This simultaneously prevents LBRF and other louse-borne diseases (epidemic typhus, trench fever).
- **Secondary prevention:** early case detection (malaria-film review in febrile at-risk individuals) and prompt treatment to shorten the human-reservoir period and limit epidemic spread.
- **Tertiary prevention:** anticipation and supportive management of the JHR and organ complications.
- **Immunization:** **none** — no vaccine exists (antigenic variation is a central obstacle).
- **Prophylaxis / chemoprophylaxis:** not standard; focus is on delousing and surveillance.
- **Genetic screening/counseling (carrier/prenatal/PGD):** **not applicable.**

---

## 14. Other Species / Natural Disease

- **Host range:** ***B. recurrentis* is essentially a human-restricted pathogen** — "no other reservoir for this infection is known" (Lucchini et al. 2016). Humans are the reservoir; the body louse is the obligate vector.
- **Taxonomy:** NCBI Taxonomy — *Borrelia recurrentis* (genus *Borrelia*; relapsing-fever group); vector *Pediculus humanus humanus*. (Numeric taxon IDs not retrieved this session.)
- **Breed (VBO):** not applicable.
- **Orthologous human genes (NCBI Gene):** not applicable.
- **Natural disease in animals / OMIA / VetCompass:** LBRF itself is **not a recognized natural animal disease** (human-and-louse-restricted). The **tick-borne relapsing-fever relatives** (*B. duttonii*, *B. crocidurae*, *B. hermsii*) do infect rodents and other vertebrates and are used experimentally.
- **Comparative biology / evolutionary conservation:** *B. recurrentis* is a **genome-reduced derivative of the tick-borne *B. duttonii*** (Lescot et al. 2008), an informative model of **reductive genome evolution under vector specialization**, paralleling *Rickettsia prowazekii*.
- **Zoonotic potential:** essentially none for *B. recurrentis* (anthroponosis).

---

## 15. Model Organisms

- **Human-host genetic models (MGI/IMPC/KOMP/ZFIN/knockouts):** **not applicable** — no human gene to model.
- **Pathogen/infection models (the relevant category):**
  - **Mice** are the standard experimental host for relapsing-fever *Borrelia* (spirochetemia, relapse, antigenic variation, tick transmission). Most mechanistic understanding of the **Vmp antigenic-variation relapse cycle** comes from **immunocompetent and immunodeficient mouse infection with *B. hermsii***, including a *vmp*-knockout study showing the mutant was "attenuated in mice... and was unable to relapse in animals after its initial spirochetemia" — direct genetic evidence that the *vmp* system drives relapse (a mechanism **inferred, not independently demonstrated, for *B. recurrentis***).
  - ***B. recurrentis*-specific models are limited** — the organism is fastidious and human-restricted; experimental work historically used animal inoculation for diagnosis and relied on relatives for mechanism.
- **Phenotype recapitulation:** mouse models of TBRF species reproduce **spirochetemia, febrile-equivalent cycles, and antigenic-variation-driven relapse** well, and tick transmission; they **do not** reproduce **louse transmission** or the specific **genome-reduced biology/reduced relapse number** of *B. recurrentis*.
- **Model limitations:** louse-borne transmission, human-restricted host range, and the clinical JHR are **not well captured** in standard rodent models.
- **In vitro:** *Borrelia* are cultivable in specialized media (e.g., BSK), but *B. recurrentis* is notoriously difficult to culture; genomics has largely substituted for culture-based study.
- **Resources:** no dedicated LBRF model-organism database; relevant repositories are pathogen-genomics resources (the Lescot 2008 genome; KEGG genome entry for *B. recurrentis* A1, chromosome GenBank **CP000993**).

---

## Key gaps / caveats

- **Inference flags:** the Vmp/vlp antigenic-variation **relapse mechanism** and detailed immune dynamics are **demonstrated in *B. hermsii*/*B. duttonii*** and **inferred for *B. recurrentis*** (supported by its contracted but present vlp/vsp repertoire; Lescot 2008).
- **Numeric discrepancies** exist within sources (e.g., the 20.4% vs ~21% genome-reduction figure; JHR rates 55.8% pooled vs "up to 80–90%"; untreated CFR ~3–6% pooled vs classic 15–40%) — reported here as given, with denominators where available.
- **Not retrieved this session:** precise global incidence/prevalence; validated QoL metrics; Orphanet ORPHA number; exact NCBI taxon IDs; the main review PMC8756760 and the Munich case-series PMID (the Munich series is referenced via PMC4869252 but its PMID was not confirmed). One intended search on complement-related host-interaction mechanisms was blocked by a safety classifier and is therefore omitted rather than filled from memory.

**Sources (URLs):** [Lescot 2008 genome, PLoS Genet / PMC2525819](https://pmc.ncbi.nlm.nih.gov/articles/PMC2525819) · [Kahlig Part 2, PMC7951929](https://pmc.ncbi.nlm.nih.gov/articles/PMC7951929) · [Kahlig Part 1 PDF](https://researchonline.jcu.edu.au/70507/1/70507.pdf) · [Lucchini 2016 Turin, EID](https://wwwnc.cdc.gov/eid/article/22/2/15-1768_article) · [CDC LBRF](https://www.cdc.gov/relapsing-fever/about/about-lbrf.html) · [MSD Manuals — Relapsing Fever](https://www.msdmanuals.com/professional/infectious-diseases/spirochetes/relapsing-fever) · [MSF guidelines — LBRF](https://medicalguidelines.msf.org/en/viewport/CG/english/louse-borne-relapsing-fever-lbrf-16689949.html) · [NCBI MedGen C0152061](https://ncbi.nlm.nih.gov/medgen/508863) · [ICD-11 1C1J.1 (findacode)](https://www.findacode.com/icd-11/code-1379934125.html) · [MeSH D012061](https://meshb.nlm.nih.gov/record/ui?ui=D012061) · [Disease Ontology DOID:13035](https://www.informatics.jax.org/disease/DOID:13035) · [MONDO:0001620 (NORD)](https://rarediseases.org/mondo-disease/louse-borne-relapsing-fever/).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 16 |
| Terms whose name was checked | 9 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001620` (3 mentions) - the report calls it "NORD"; MONDO calls it **louse-borne relapsing fever**
- `HP:0001873` (1 mention) - the report calls it "Marked; platelets 22,000–48,000/µL in Turin cases"; HP calls it **Thrombocytopenia**
- `HP:0001649` (1 mention) - the report calls it "common"; HP calls it **Tachycardia**
- `CL:0000115` (1 mention) - the report calls it "endothelium", "Tissue/cell level:** vascular **endothelium"; CL calls it **endothelial cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0001555` (1 mention) - the report calls it "Gastrointestinal tract"; UBERON calls it **digestive tract**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000178` - called "blood", "Primary compartment:** **blood"
- `CL:0000115` - called "endothelium", "Tissue/cell level:** vascular **endothelium"

### Terms the ontology service could not be reached for

16 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0025142` (1 mention)
- `HP:0002315` (2 mentions)
- `HP:0025143` (1 mention)
- `HP:0002017` (1 mention)
- `HP:0002027` (1 mention)
- `HP:0000952` (1 mention)
- `HP:0001433` (1 mention)
- `HP:0000421` (1 mention)
- `HP:0001639` (1 mention)
- `HP:0001978` (1 mention)
- `HP:0012819` (1 mention)
- `CL:0000233` (1 mention)
- `UBERON:0000178` (1 mention)
- `UBERON:0002107` (1 mention)
- `UBERON:0000948` (1 mention)
- `UBERON:0000955` (1 mention)

### Terms whose obsolescence could not be checked

8 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0001620` (3 mentions)
- `HP:0001945` (1 mention)
- `HP:0003326` (1 mention)
- `HP:0011227` (1 mention)
- `HP:0001399` (1 mention)
- `HP:0001744` (1 mention)
- `HP:0000979` (1 mention)
- `UBERON:0002048` (1 mention)