---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T13:37:39.732993'
end_time: '2026-10-14T13:41:29.991046'
duration_seconds: 230.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurocardiorenal Malformation Syndrome
  mondo_id: MONDO:0980704
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
  web_search_requests: 3
  num_turns: 24
  total_cost_usd: 2.3464641
  session_id: 4ff0ac01-8229-42a0-aef8-69b998d43eb1
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 71
  verified: 71
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0980704
    reported_labels:
    - MONDO
    ontology_label: neurocardiorenal malformation syndrome
  - term_id: HP:0011344
    reported_labels:
    - "1 never walked; others walked at 2\u20134 y, with support or wide-based gait"
    ontology_label: Severe global developmental delay
  - term_id: HP:0004322
    reported_labels:
    - "\u22123 and \u22123.3 SD (Ind. 1, 2)"
    ontology_label: Short stature
  - term_id: UBERON:0000955
    reported_labels:
    - frontal lobe
    ontology_label: brain
  - term_id: UBERON:0000948
    reported_labels:
    - interventricular septum
    ontology_label: heart
  - term_id: UBERON:0002113
    reported_labels:
    - horseshoe fusion; collecting system dilatation
    ontology_label: kidney
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurocardiorenal Malformation Syndrome
- **MONDO ID:** MONDO:0980704 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurocardiorenal Malformation Syndrome** covering all of the
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

I've got the gene (TM2D3), OMIM 621379, and the MedGen phenotype list. Now I'm trying to get the full text of the 2025 paper for patient-level detail.

I have enough to write the report. The main source is the 2025 AJHG paper (full text via PMC); MedGen, PanelApp, IMPC and the Drosophila and mouse Notch studies fill in the rest.

# Neurocardiorenal Malformation Syndrome (NCRMS; TM2D3-related): Research Report

**Prepared:** 2026-10-14 · **MONDO:** MONDO:0980704 · **OMIM phenotype:** #621379 · **Gene:** *TM2D3* (OMIM *610014, 15q26.3)

> **About the CURIEs in this report.** Identifiers below that were read from a source in this session are marked ✅. Ontology terms marked 🔎 are suggestions to look up with `runoak` / `just validate-terms` before binding. Under the repository's CURIE rule they are leads, not checked bindings.

---

## 1. Disease Information

**Overview.** NCRMS is an autosomal recessive syndrome that is mainly a severe neurodevelopmental disorder, with structural heart and kidney malformations. MedGen gives the OMIM-derived definition: *"Neurocardiorenal malformation syndrome (NCRMS) is an autosomal recessive severe neurodevelopmental disorder associated with microcephaly, distinctive facial features, and multiorgan involvement including cardiac and renal malformations"* ([MedGen C6024737](https://www.ncbi.nlm.nih.gov/medgen/1887965)).

The syndrome was defined by one report: Gabillard-Lefort et al. 2025, *Am J Hum Genet* 112(7):1711–1721, **PMID:40449487** ✅ (PMC12256896, free in Europe PMC; abstract cached at `references_cache/PMID_40449487.md`). Abstract quote:

> "We identified via exome sequencing bi-allelic variants in TM2D3 in four affected individuals from four unrelated families with overlapping clinical presentations, including microcephaly, severe global developmental delay with absent speech, autistic features, heart malformation, and dysmorphic facial features."

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0980704 | ✅ MedGen xref |
| OMIM (phenotype) | 621379 | ✅ MedGen, PanelApp |
| OMIM (gene) | 610014 (*TM2D3*) | ✅ PanelApp |
| MedGen | C6024737 (UID 1887965) | ✅ |
| Orphanet | none found | MedGen lists no ORPHA code |
| ICD-10 / ICD-11 / MeSH | no specific code | would fall under generic "multiple congenital anomalies" codes |
| Ensembl | ENSG00000184277 | ✅ PanelApp |

**Synonyms:** NCRMS. GeneCards also lists "severe neurodevelopmental disorder with facial dysmorphism, cerebral-renal-cardiac anomalies" ([GeneCards TM2D3](https://www.genecards.org/card/TM2D3)).

**Data provenance:** all clinical data come from individual patients in a single case series (n = 4, four families). There is no registry or EHR cohort.

**Lump/split note for curation.** *TM2D3* is also linked to late-onset Alzheimer disease risk through the heterozygous p.Pro155Leu variant (PMID:27764101 ✅). That is a separate, susceptibility-type association. It should not be merged into this entry, though it is worth a sentence in `notes` or `genetic[].notes`.

---

## 2. Etiology

- **Cause:** biallelic germline loss-of-function or hypomorphic variants in *TM2D3*. In all four families the parents were heterozygous carriers, and two healthy sisters of Individual 2 were also heterozygous (PMID:40449487 full text).
- **Genetic risk factors:** none beyond the causal genotype. The recurrent c.503G>A (p.Gly168Asp) allele was found in 3 of the 4 families (France ×2, Italy). These were non-consanguineous families of different origins, which fits a recurrent allele rather than a confirmed founder effect; no haplotype analysis was reported.
- **Environmental, protective, and gene–environment factors:** none reported. The mechanism study used tunicamycin as an *experimental* ER stressor. The authors' "exacerbated ER-stress sensitivity" framing raises the idea that physiological stress could modify severity, but this has not been tested in patients and should not be curated as an environmental factor.

---

## 3. Phenotypes

The cohort is n = 4, so the frequencies below are counts, not population estimates. Sources: the PMID:40449487 full text (Table 1) and the HPO annotation list in [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1887965), which includes 87 HPO features.

| Phenotype | Freq. | Detail | Suggested HP 🔎 |
|---|---|---|---|
| Microcephaly, postnatal/progressive | 4/4 | OFC −5, −3.6, −2.5, −4 SD | HP:0000252 Microcephaly; HP:0000253 Progressive microcephaly; HP:0005484 Secondary microcephaly |
| Severe global developmental delay | 4/4 | 1 never walked; others walked at 2–4 y, with support or wide-based gait | HP:0011344 |
| Absent or severely limited speech | 4/4 | Ind. 3 used bisyllabic words | HP:0001344 Absent speech |
| Autistic features | several | — | HP:0000729 Autistic behavior |
| Anxiety, agitation, self-injury, aggression, stereotypies | several | — | HP:0000739; HP:0000713; HP:0100716; HP:0000718; HP:0000733 |
| Seizures | 2/4 | Ind. 2: focal, onset 22 mo. Ind. 3: onset 2 mo, with episodes of alternating hemiplegia | HP:0001250; HP:0007359 Focal-onset seizure; "Episodic hemiplegia" per MedGen |
| Structural brain anomalies | 3/4 on MRI | small frontal lobes (2), abnormal gyration (2), thick corpus callosum (1), vermis hypoplasia (1); Ind. 4 had a pineal cyst on CT | HP:0007333 Hypoplasia of the frontal lobes; HP:0002536 Abnormal cortical gyration; HP:0001320 Cerebellar vermis hypoplasia; HP:0007074 Thick corpus callosum |
| **Congenital heart defect** | **4/4** | VSD (3/4, three VSDs in Ind. 3); PDA + PFO (Ind. 1); polyvalvular dysplasia (Ind. 2); duplicated vena cava (Ind. 3) | HP:0001629 VSD; HP:0001643 PDA; HP:0001655 PFO; "Bilateral superior vena cava" per MedGen |
| **Renal anomaly** | **3/4** | horseshoe kidney (2/4); mild pyelocaliceal dilatation (1/4); Ind. 4 normal | HP:0000085 Horseshoe kidney; "Dilatation of renal calices" per MedGen |
| Genital anomalies (males) | 2/2 | scrotal hypoplasia (2), cryptorchidism (1) | HP:0000046 Small scrotum; HP:0000028 Cryptorchidism |
| Prenatal findings | 4/4 | IUGR and/or polyhydramnios; decreased fetal movement | HP:0001511; HP:0001561; HP:0001558 |
| Short stature | 2/4 | −3 and −3.3 SD (Ind. 1, 2) | HP:0004322 |
| Ocular | 3/4 | hypermetropia (2), strabismus (2), legal blindness (1), optic disc drusen | HP:0000540; HP:0000486; HP:0000618 |
| Facial dysmorphism | 4/4 | mild coarse features, convex nasal ridge, low columella, pinched or narrow mouth, sparse eyebrows, thin upper lip, low-set or posteriorly rotated ears, micrognathia | HP:0000444 Convex nasal ridge; HP:0000160 Narrow mouth; HP:0000347 Micrognathia |
| Hand and foot | some | 2–3 toe syndactyly, 3–4 finger cutaneous syndactyly, single transverse palmar crease | per MedGen |
| Tone and motor | some | axial hypotonia, limb hypertonia, dystonia, gait ataxia | HP:0008936; HP:0002509; HP:0001332; HP:0002066 |
| Other | isolated | laryngomalacia, recurrent pneumonia, sleep apnea, feeding difficulties, constipation, syringomyelia, Horner syndrome, scoliosis, dental anomalies (microdontia, delayed eruption) | per MedGen |

**Course:** onset is congenital or prenatal, and microcephaly is postnatal and progressive. The authors note *no regression* in any patient. The oldest patient was 26 years old at last exam, so survival into adulthood occurs.

**Quality of life:** no formal measure (EQ-5D, PROMIS) has been reported. The impact is inferred from profound intellectual and motor disability and absent speech, with lifelong dependence.

---

## 4. Genetic / Molecular Information

**Gene:** *TM2D3* (TM2 domain containing 3; also BLP2, β-amyloid peptide binding protein-like 2). It encodes a protein with a signal peptide and two transmembrane domains joined by a conserved intracellular DRF motif (PMID:34905536 ✅). It has two splice isoforms (v1 and v2), which differ by 26 residues near the signal peptide (PMID:38016980 ✅). HGNC ID 🔎 should be looked up; use the lowercase `hgnc:` form.

**Reported variants** (PMID:40449487 Table 2; ClinVar SCV005387825–SCV005387828)

| Variant | Type | Families / zygosity | gnomAD AF | In silico |
|---|---|---|---|---|
| c.503G>A p.(Gly168Asp) | missense (first base of exon 5; no splice effect on cDNA) | Ind. 3 homozygous; Ind. 1 and 2 compound het | 1×10⁻⁵ | CADD 36; AlphaMissense 0.987; PolyPhen-2 1 |
| c.7G>T p.(Gly3\*) | nonsense (NMD predicted) | Ind. 1, in trans with Gly168Asp | ~5×10⁻⁶ | — |
| c.153dup p.(Val52Serfs\*9) | frameshift | Ind. 2, in trans with Gly168Asp | absent | — |
| c.677C>T p.(Thr226Met) | missense | Ind. 4 | 1.05×10⁻⁵ | CADD 30; REVEL 0.72 |
| del15q26.3 (~33 kb, exons 1–6; chr15:102182681–102215940, GRCh37) | intragenic deletion | Ind. 4, in trans with Thr226Met | — | — |

- **Classification:** the paper's figure legend calls Gly168Asp "likely pathogenic". Formal ACMG calls per variant are not in the main text.
- **Functional class:** every genotype pairs a predicted-null allele with a missense allele, or has homozygous missense. No patient had two null alleles, which fits IMPC complete preweaning lethality in *Tm2d3* homozygous knockout mice (see §15). The authors suggest the missense alleles are **hypomorphic**. Gly168Asp restored basal GRP78 in rescue experiments but showed a trend toward abnormal accumulation under stress (p = 0.09), which they read as partial loss of function. The `functional_impact_category` options are `LOSS_OF_FUNCTION` for the null alleles and `PARTIAL_LOSS_OF_FUNCTION` for Gly168Asp, the latter only if a curator accepts that inference.
- **Gene–disease validity:** ClinGen has not assessed it. Gene2Phenotype rates it *moderate*. Genomics England PanelApp rates it Amber on the Severe Microcephaly panel and it is tagged for promotion to Green in Q1 2026 ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/TM2D3/)). Under the repo rule, **do not populate `gene_disease_validity`**, because no ClinGen record exists.
- **Chromosomal context:** *TM2D3* sits in distal 15q26.3. Terminal 15q26 deletions and ring 15 include it (e.g., PMID:27160288, PMID:18194513, PMID:29223476). These are hemizygous and contiguous-gene events, so they are not NCRMS.
- **Modifier genes and epigenetics:** none reported.

---

## 5. Environmental Information

Not applicable. No environmental, lifestyle, or infectious factors have been reported. Leave the `environmental:` section empty rather than inventing one.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *TM2D3* variants** (one null plus one hypomorphic missense, or homozygous missense) **lead to** reduced TM2D3 function. *Demonstrated* for null alleles by the variant class. *Partially demonstrated* for Gly168Asp by rescue assays (PMID:40449487).
2. **Loss of TM2D3, an ER-resident transmembrane protein, results in a dysregulated ER unfolded-protein response.** KO SNB75 cells showed mildly *decreased* ATF4, HSPA5 and DDIT3 at baseline and a *dramatic increase* after tunicamycin. Patient fibroblasts showed decreased HSPA5 at baseline and a strong HSPA5 rise under stress. TEM showed **ER luminal swelling**. *Demonstrated in vitro* (PMID:40449487).
   - Quote (abstract): "revealed an impact of TM2D3 on ER-stress response, with dysregulated expression of ATF4, HSPA5, and DDIT3."
3. **ER dysfunction leads to secondary mitochondrial changes:** longer mitochondria, wider cristae, a larger ER–mitochondria distance, and higher OPA1. Respiratory-chain activity and oxygen consumption were **normal**, so this is structural, not bioenergetic. The authors propose disturbed DNM1L-mediated fission at ER–mitochondria contacts. *Morphology demonstrated; fission mechanism inferred.*
4. **Branch A, ECM / neuronal migration (inferred).** Fibroblast RNA-seq found 21 DEGs: up EYA2, DPT, COMP, TNC, LRRC20; down TLR4, EBF2, KRT19, LGR4, among others. The ECM genes TNC, DPT and COMP are implicated in neuronal-precursor migration. This is a *transcriptional association in a non-neural cell type*, and the causal role is not shown.
5. **Branch B, Notch signaling (inferred for the human disease).** TM2D3 promotes **cell-surface presentation of NOTCH1 and NOTCH2**, and *Tm2d3*⁻/⁻ mouse embryonic fibroblasts show lower surface Notch (PMID:38016980 ✅). Fly orthologs (*almondex*, *amaretto*, *biscotti*) are required for Notch signaling at the γ-secretase step (PMID:34905536 ✅). Quote: "cell surface expression of Notch1 and Notch2 is reduced in Tm2d3-deficient cells." The NCRMS paper **did not test Notch** and found no Notch signature among its DEGs. Notch dysfunction is a plausible link to the heart, kidney and neurogenesis phenotypes, but it is not demonstrated in patients. Model it as an `EMERGING` hypothesis group.
6. **Neural progenitor depletion or mis-migration (inferred) leads to** postnatal microcephaly, frontal hypoplasia and gyral anomalies, which **result in** severe developmental delay, absent speech, autism and seizures.
7. **Disrupted organogenesis (mechanism unknown; Notch suggested) results in** VSD/PDA/valve dysplasia and horseshoe kidney. *No direct evidence.*

**Suggested ontology terms** 🔎

- **GO:** GO:0030968 endoplasmic reticulum unfolded protein response; GO:0034976 response to endoplasmic reticulum stress; GO:0007219 Notch signaling pathway; GO:0045747 positive regulation of Notch signaling pathway; GO:0007005 mitochondrion organization; GO:0000266 mitochondrial fission; GO:0001764 neuron migration; GO:0007405 neuroblast proliferation; GO:0007507 heart development; GO:0001822 kidney development.
- **GO cellular component:** GO:0005783 endoplasmic reticulum; GO:0044233 mitochondria-associated ER membrane contact site.
- **CL:** CL:0000057 fibroblast (assay system); CL:0011020 neural progenitor cell; CL:0000540 neuron.
- **Proteins:** ATF4, HSPA5/GRP78, DDIT3/CHOP, OPA1, NOTCH1, NOTCH2.
- **Biological scale tags:** step 2 = CELLULAR; step 3 = CELLULAR; steps 6–7 = TISSUE.

**Molecular profiling:** fibroblast bulk RNA-seq (3 patients vs 4 parents). No single-cell, proteomics, metabolomics, or GEO accession was reported, so do not add `datasets:` without an accession.

---

## 7. Anatomical Structures Affected 🔎

- **Brain** UBERON:0000955: frontal lobe (UBERON:0016525), cerebral cortex (UBERON:0000956), cerebellar vermis (UBERON:0004720), corpus callosum (UBERON:0002336).
- **Heart** UBERON:0000948: interventricular septum (UBERON:0002094), ductus arteriosus (UBERON:0004145), cardiac valves.
- **Kidney** UBERON:0002113 (horseshoe fusion; collecting system dilatation).
- **Male genitalia:** scrotum, testis.
- **Eye.**
- **Subcellular:** ER (primary site); mitochondria (secondary).
- **Laterality:** the malformations are midline or fusion defects. No lateralization is reported.

---

## 8. Temporal Development

- **Onset:** prenatal (IUGR, polyhydramnios, structural defects present at birth), with postnatal progressive microcephaly. Seizure onset ranged from 2 months to 22 months.
- **Course:** a static neurodevelopmental encephalopathy with no regression. Microcephaly progresses in relative terms. The disease is lifelong.
- **Stages:** none defined. Ages at last exam were 5½–26 y; the text says "5–24 y", one of several internal inconsistencies in the paper.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007 🔎). Penetrance appears complete in biallelic individuals; heterozygous carriers are unaffected.
- **Expressivity:** variable. Renal involvement is 3/4, seizures 2/4, and growth failure 2/4.
- **Epidemiology:** 4 reported cases worldwide (France ×2, Italy, USA). Prevalence is unknown. Suggested record: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: BELOW_1_IN_1000000` or `ULTRA_RARE`, with evidence PMID:40449487.
- **Sex:** 2 M, 2 F.
- **Consanguinity:** none in the 4 families.
- **Carrier frequency:** the variants are each ~10⁻⁵ in gnomAD. No aggregate carrier frequency has been published.

---

## 10. Diagnostics

- **Genetic:** exome sequencing was the diagnostic route in all four families. CNV calling, or CMA/genome sequencing, is needed because one allele was a 33 kb intragenic deletion. *TM2D3* is on the PanelApp Severe Microcephaly, Intellectual Disability and DDG2P panels.
- **Supportive clinical work-up:** echocardiography (VSD/PDA), renal ultrasound (horseshoe kidney), brain MRI (frontal hypoplasia, gyral anomalies, vermis hypoplasia), EEG, ophthalmologic exam.
- **Biomarkers:** none are validated. Raised HSPA5/GRP78 after ER-stress challenge in fibroblasts is a research assay only.
- **Differential diagnosis** (suggested from phenotype overlap; not from the paper): *TMEM260* structural heart defects and renal anomalies syndrome (OMIM #617478), whose neurodevelopmental, cardiac and renal triad overlaps; 15q26 terminal deletion and ring 15; and primary microcephaly genes with congenital heart disease. Use any of these only with a citation.
- **Screening:** no newborn screening. Cascade carrier testing and prenatal or PGT-M testing are possible once familial variants are known.

---

## 11. Outcome / Prognosis

- No survival data exist. One patient reached 26 years.
- Expect severe lifelong intellectual and motor disability and dependence, plus legal blindness in one patient.
- Complications: seizures, recurrent pneumonia or bronchitis, sleep apnea, feeding difficulties, scoliosis.
- No prognostic factors or biomarkers are known.

---

## 12. Treatment

No disease-specific therapy exists. Management is supportive and symptomatic (NCIT suggestions 🔎; these must sit under NCIT:C25218):

| Intervention | NCIT 🔎 |
|---|---|
| Antiseizure pharmacotherapy | NCIT:C15986 Pharmacotherapy (no specific agents reported) |
| Cardiac surgical repair of VSD/PDA, as indicated | NCIT:C15329 Surgical Procedure |
| Physical, occupational and speech therapy | NCIT:C15302; NCIT:C121351; NCIT:C159273 |
| Genetic counseling | NCIT:C15240 |
| Supportive care (feeding, respiratory) | NCIT:C15747 |

No ER-stress-modulating drugs (e.g., chemical chaperones such as 4-PBA or TUDCA) have been tested. Mention them only as a knowledge gap. There are no clinical trials (no NCT or ICTRP entries found).

---

## 13. Prevention

- Primary prevention is not applicable.
- Genetic counseling covers 25% recurrence risk for carrier parents, carrier testing of siblings, and prenatal diagnosis or PGT-M.
- Tertiary prevention: cardiac and renal surveillance, seizure management, ophthalmology follow-up.

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease has been reported (OMIA not checked in this session). TM2D3 is conserved across metazoans; the *Drosophila* ortholog is *almondex* (*amx*). Human TM2D3 provides about 50% of fly Amx activity in rescue assays (PMID:34905536).

---

## 15. Model Organisms

| Model | Findings | Relevance to NCRMS | Ref |
|---|---|---|---|
| **Mouse *Tm2d3*<sup>em1(IMPC)J</sup>** (IMPC) | Homozygous: **preweaning lethality, complete penetrance**; E15.5 edema and hemorrhage. Heterozygous: increased anxiety-related response, decreased lean mass, decreased grip strength | The null is lethal, which fits patients carrying ≥1 hypomorphic allele. Embryonic edema and hemorrhage may reflect a cardiovascular defect (not established) | IMPC genotype-phenotype API ([mousephenotype.org](https://www.mousephenotype.org)); cited in PMID:40449487 discussion |
| **Mouse *Tm2d3*⁻/⁻ MEFs** (CRISPR exon-5 deletion) | ~40% lower Notch1 full-length protein; reduced surface NOTCH1 and NOTCH2; mRNA unchanged | Mechanistic, in vitro | PMID:38016980 ✅ |
| ***Drosophila* *amx*, *amrt*, *bisc* nulls** | Maternal-effect neurogenic phenotype (loss of Notch lateral inhibition); act at γ-secretase S3 cleavage; shortened lifespan; progressive motor and electrophysiological decline | Notch link; neuronal maintenance; not a malformation model | PMID:34905536 ✅ |
| ***Drosophila* *amx* embryo** | Impaired endocytosis of the Notch extracellular domain and Delta | Mechanism of surface presentation | PMID:38016980 ✅ |
| **SNB75 TM2D3-KO cells; patient fibroblasts** | ER localization, ER stress, mitochondrial morphology | Main disease-mechanism evidence | PMID:40449487 ✅ |

- **Limitations:** no model recapitulates the human malformation spectrum. The fly phenotypes are maternal-effect and Notch-centric. The mouse null is lethal, and no hypomorphic (Gly168Asp knock-in) model exists. This is a good candidate for a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.
- **`evidence_source`:** MODEL_ORGANISM for the fly and IMPC data; IN_VITRO for the MEF, SNB75 and fibroblast data.

---

## Key evidence quotes for curation

| Claim | Reference | Exact abstract quote |
|---|---|---|
| Core phenotype, AR biallelic | PMID:40449487 | "bi-allelic variants in TM2D3 in four affected individuals from four unrelated families with overlapping clinical presentations, including microcephaly, severe global developmental delay with absent speech, autistic features, heart malformation, and dysmorphic facial features" |
| ER localization | PMID:40449487 | "we show that TM2D3 is an endoplasmic reticulum (ER) protein" |
| ER-stress dysregulation | PMID:40449487 | "revealed an impact of TM2D3 on ER-stress response, with dysregulated expression of ATF4, HSPA5, and DDIT3" |
| Mitochondrial alterations | PMID:40449487 | "Transmission electron microscopy highlighted ER swelling as well as unexpected secondary mitochondrial alterations including increased length, cristae width, and ER-mitochondria distance" |
| ECM DEGs | PMID:40449487 | "disclosed 21 differentially expressed genes, including genes coding for extracellular matrix components involved in the migration of neuronal precursors" |
| Notch surface presentation | PMID:38016980 | "cell surface expression of Notch1 and Notch2 is reduced in Tm2d3-deficient cells" |
| Fly Notch / γ-secretase | PMID:34905536 | "Overexpression of the most conserved region of the TM2D proteins acts as a potent inhibitor of Notch signaling at the γ-secretase cleavage step." |

**Caveats for snippet validation**

- The PMID:40449487 cache is **abstract-only**. The counts "kidney malformation (2/4: horseshoe kidney)" and "heart malformation (4/4: …)" come from the full text. They will not validate against the current cache unless full text is fetched; otherwise attach those phenotype claims to an abstract quote or leave them unquoted.
- The abstract does **not** mention renal anomalies. The renal component rests on the full-text table and the OMIM/MedGen synopsis.

---

## Sources

- Gabillard-Lefort C et al. *Am J Hum Genet* 2025;112:1711–1721. PMID:40449487; [PMC12256896](https://pmc.ncbi.nlm.nih.gov/articles/PMC12256896/); [FLORE record](https://flore.unifi.it/handle/2158/1460472)
- Masuda W et al. *Sci Rep* 2023. PMID:38016980
- Salazar JL et al. *PLoS Genet* 2021. PMID:34905536
- Jakobsdottir J et al. *PLoS Genet* 2016. PMID:27764101 (Alzheimer-risk association; distinct entity)
- [MedGen C6024737 – NCRMS](https://www.ncbi.nlm.nih.gov/medgen/1887965)
- [Genomics England PanelApp – TM2D3](https://panelapp.genomicsengland.co.uk/panels/162/gene/TM2D3/)
- [GeneCards – TM2D3](https://www.genecards.org/card/TM2D3)
- [IMPC – Tm2d3 genotype–phenotype records](https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Tm2d3)
- [MedGen search (TMEM260 differential)](https://ncbi.nlm.nih.gov/medgen/C4540004)
- Jakobsdottir 2016 coverage: [DOAJ](https://doaj.org/article/03cd00851ca345d0aedc6937fe264fab), [Technology Networks](https://www.technologynetworks.com/neuroscience/news/novel-alzheimer-s-disease-risk-gene-among-icelanders-discovered-284671)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0980704` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurocardiorenal malformation syndrome**
- `HP:0011344` (1 mention) - the report calls it "1 never walked; others walked at 2–4 y, with support or wide-based gait"; HP calls it **Severe global developmental delay**
- `HP:0004322` (1 mention) - the report calls it "−3 and −3.3 SD (Ind. 1, 2)"; HP calls it **Short stature**
- `UBERON:0000955` (1 mention) - the report calls it "frontal lobe"; UBERON calls it **brain**
- `UBERON:0000948` (1 mention) - the report calls it "interventricular septum"; UBERON calls it **heart**
- `UBERON:0002113` (1 mention) - the report calls it "horseshoe fusion; collecting system dilatation"; UBERON calls it **kidney**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15747` (1 mention) - the report calls it "Supportive care (feeding, respiratory)"; NCIT calls it **Supportive Care**