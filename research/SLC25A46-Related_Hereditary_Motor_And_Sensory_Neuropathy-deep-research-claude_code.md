---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-03T03:37:40.389384'
end_time: '2026-11-03T03:40:00.786682'
duration_seconds: 140.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SLC25A46-Related Hereditary Motor And Sensory Neuropathy
  mondo_id: MONDO:0014671
  category: Mendelian
  causal_genes: SLC25A46
  omim_id: OMIM:616505
  synonyms: CMT6B; Charcot-Marie-Tooth disease, type 6B; HMSN 6B; HMSN6B; SLC25A46
    hereditary motor and sensory neuropathy type 6; hereditary motor and sensory neuropathy
    type 6 caused by mutation in SLC25A46; neuropathy, hereditary motor and sensory,
    type VIB
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
  num_turns: 10
  total_cost_usd: 1.9456412
  session_id: 0fd23c93-4567-4fe6-abeb-653e776d4285
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 12
  validator_version: 0.5.1
term_validation:
  total_terms: 49
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014671
    reported_labels:
    - MONDO
    ontology_label: neuropathy, hereditary motor and sensory, type 6B
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC25A46-Related Hereditary Motor And Sensory Neuropathy
- **MONDO ID:** MONDO:0014671 (if available)
- **Causal gene(s):** SLC25A46
- **OMIM:** OMIM:616505
- **Synonyms:** CMT6B; Charcot-Marie-Tooth disease, type 6B; HMSN 6B; HMSN6B; SLC25A46 hereditary motor and sensory neuropathy type 6; hereditary motor and sensory neuropathy type 6 caused by mutation in SLC25A46; neuropathy, hereditary motor and sensory, type VIB
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SLC25A46-Related Hereditary Motor And Sensory Neuropathy** covering all of the
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

# SLC25A46-Related Hereditary Motor and Sensory Neuropathy (CMT6B / HMSN6B): Research Report

**Target:** MONDO:0014671 · OMIM:616505 · causal gene **SLC25A46** (solute carrier family 25 member 46; chromosome 5q22.1)

> **Scope and verification.** This report was assembled from web searches. Some citations were confirmed against PubMed or PMC records during the search; others are given from prior knowledge, with their PMIDs marked **[verify]**. Text in quotation marks comes from search-result excerpts of the cited papers, not from a fetched abstract. Re-check every quote with `just fetch-reference` and `just count-verified-snippets` before using it as a dismech snippet. Treat every CURIE below as a lead, per the repository's term contract: look each one up before binding it.

---

## 1. Disease information

**Overview.** CMT6B (HMSN6B) is an autosomal recessive neurodegenerative disorder caused by **biallelic loss-of-function variants in SLC25A46**. The core phenotype combines:
- early-onset **optic atrophy**; and
- **axonal sensorimotor peripheral neuropathy** (CMT2-like).

Many patients also have **cerebellar ataxia** and **cerebellar atrophy**. Abrams et al. (2015) reported the gene after whole-exome sequencing of patients with optic atrophy and CMT2 identified four families with recessive SLC25A46 mutations. They described it as an "optic atrophy spectrum disorder" that overlaps clinically with OPA1- and MFN2-related disease (Abrams et al., *Nat Genet* 2015;47:926–932, **PMID:26168012** — confirmed).

The disorder sits on a severity spectrum:
- **Mildest:** isolated or mild optic atrophy with survival into adulthood.
- **Classic:** optic atrophy plus axonal neuropathy (HMSN6B).
- **Intermediate:** progressive myoclonic ataxia with optic atrophy and neuropathy (Charlesworth et al., *Mov Disord* 2016;31:1249–1251, doi:10.1002/mds.26716).
- **Ataxia-predominant:** autosomal recessive cerebellar ataxia without optic atrophy (Hammer et al., *Neurodegener Dis* 2017;17:208–212, doi:10.1159/000464445).
- **Severe:** Leigh syndrome (Janer et al., *EMBO Mol Med* 2016, **PMID:27390132** — confirmed).
- **Most severe:** lethal congenital pontocerebellar hypoplasia (Wan et al., *Brain* 2016;139:2877, **PMID:27543974** — confirmed).

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0014671 |
| OMIM (phenotype) | 616505 (HMSN6B) |
| OMIM (gene) | 610826 **[verify]** |
| HGNC | hgnc:25198 **[verify]** |
| Orphanet | Hereditary motor and sensory neuropathy type 6 group, ORPHA:90120 **[verify]** |
| ICD-10 | G60.0 (hereditary motor and sensory neuropathy) |
| MeSH | Charcot-Marie-Tooth Disease (D002607); Optic Atrophy (D009896) |

**Synonyms.** CMT6B; Charcot-Marie-Tooth disease type 6B; HMSN6B; neuropathy, hereditary motor and sensory, type VIB; SLC25A46 hereditary motor and sensory neuropathy type 6.

**Source of the information.** All of it comes from aggregated case reports and small family series. There are no EHR-derived cohorts. A natural-history study is registered: **NCT04594590**, "Natural History Study of SLC25A46 Mutation-related Mitochondriopathy."

**Naming note for curation.** MONDO:0014671 and OMIM:616505 refer to the HMSN6B phenotype. The Leigh syndrome and pontocerebellar hypoplasia presentations are best treated as allelic severity strata. They can be modeled as `has_subtypes` or recorded in the notes, but they should not be described as a separate gene's disease.

---

## 2. Etiology

- **Causal factor.** The cause is genetic: biallelic (homozygous or compound heterozygous) germline variants in SLC25A46. No environmental cause has been described.
- **Genetic risk factors.** Consanguinity raises risk, since many reported families are consanguineous, including the North African and Middle Eastern families. No susceptibility loci or modifier genes are established.
- **Allelic severity correlation.** Disease severity correlates inversely with how stable the mutant protein is. Wan et al. (2016) reported that "missense mutations causing lethal congenital pontocerebellar hypoplasia markedly destabilize the protein," and that variants associated with isolated optic atrophy do not cause instability. Abrams et al. (2018, *Hum Mutat*, **PMID:30178502** — confirmed) proposed two pathogenic routes:
  1. protein destabilization; and
  2. altered molecular interactions, seen with p.R257Q and p.G249D in a domain not tied to transport function.
- **Protective factors and gene–environment interactions.** None reported.

---

## 3. Phenotypes

| Phenotype | Suggested HPO term | Frequency / characteristics |
|---|---|---|
| Optic atrophy | HP:0000648 Optic atrophy | Very frequent; onset in childhood (often in the first decade); progressive; the defining feature |
| Reduced visual acuity | HP:0007663 Reduced visual acuity | Frequent; progressive |
| Axonal sensorimotor neuropathy | HP:0003477 Peripheral axonal neuropathy (or HP:0007108 Demyelinating peripheral neuropathy only if documented) | Very frequent in the HMSN6B core; childhood onset; slowly progressive |
| Distal muscle weakness | HP:0002460 Distal muscle weakness | Frequent |
| Distal amyotrophy | HP:0003693 Distal amyotrophy | Frequent |
| Pes cavus | HP:0001761 Pes cavus | Common in CMT |
| Areflexia / hyporeflexia | HP:0001284 Areflexia | Frequent |
| Distal sensory loss | HP:0002936 Distal sensory impairment | Frequent |
| Cerebellar ataxia | HP:0001251 Ataxia / HP:0001272 Cerebellar atrophy | Variable; prominent in the ataxia-predominant and myoclonic forms |
| Myoclonus | HP:0001336 Myoclonus | Rare (Charlesworth 2016) |
| Nystagmus | HP:0000639 Nystagmus | Variable |
| Dysarthria | HP:0001260 Dysarthria | Variable |
| Spasticity / pyramidal signs | HP:0001257 Spasticity | Reported (optic atrophy with limb spasticity; Kodal et al. 2022) |
| Pontocerebellar hypoplasia | HP:0012110 Hypoplasia of the pons; HP:0001321 Cerebellar hypoplasia | Severe allelic form; congenital; lethal |
| Respiratory insufficiency / neonatal death | HP:0002093; HP:0003811 | Severe form |
| Leigh-like basal ganglia/brainstem lesions | HP:0001337? — use HP:0007103 / Leigh syndrome terms **[verify]** | Rare (Janer 2016) |
| Lactic acidosis / increased lactate:pyruvate ratio | HP:0003128 Lactic acidosis | Some severe cases, in fibroblasts or blood |

**Quality of life.** Combined visual and motor disability is substantial: legal blindness in advanced optic atrophy, gait impairment, and use of orthotics or wheelchairs in later disease. No validated QoL instrument data have been published for this disease.

**Two caveats on the HPO suggestions:**
- Bind HP:0007108 only where a source documents demyelination. The published electrophysiology is predominantly axonal.
- HP:0001337 is "Tremor". It is not a Leigh syndrome term, which is why it carries a question mark in the table. Look up the correct term for Leigh-like lesions before binding anything.

---

## 4. Genetic and molecular information

- **Gene.** SLC25A46, at 5q22.1. It encodes an atypical member of the mitochondrial carrier family (SLC25) that sits in the **outer mitochondrial membrane (OMM)**. It is a distant homolog of yeast **Ugo1**. Abrams et al. (2015) put it this way: "SLC25A46, like Ugo1, is a modified carrier protein that has been recruited to the outer mitochondrial membrane and interacts with the inner membrane remodeling protein mitofilin (Fcj1)."
- **Variant classes reported.** Missense variants dominate, including:
  - p.T142I, p.R257Q, p.E335D, p.G249D;
  - p.L341P (the PCH-associated variant in Wan et al. 2016) **[verify]**;
  - p.Trp160Ser, in North African ataxia families.

  The other reported classes are frameshift and nonsense variants, a splice-site variant, and exonic deletions (an exonic deletion in a PCH family; Wan et al. 2016). Novel compound-heterozygous variants were found on exome reanalysis in a Leigh-syndrome infant (*J Pers Med* 2021, PMC8703603).
- **Classification.** Most published variants are listed in ClinVar as Pathogenic or Likely pathogenic. ClinGen gene–disease validity: not found during this search. Check `just list-gene-validity` and the CGGV records before recording a tier, and **do not assign one**.
- **Population frequency.** Pathogenic alleles are very rare in gnomAD. There are no common founder alleles, apart from possible local recurrence in North African families.
- **Origin.** Germline.
- **Functional consequence.** Loss of function, in two forms:
  - many variants destabilize the protein, which is then rapidly removed by the ubiquitin–proteasome system (Steffen et al., *Mol Biol Cell* 2017, PMID:28057766 **[verify]**);
  - milder variants disrupt the SLC25A46–MIC60 complex.

  No dominant-negative effect has been reported.
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

---

## 5. Environmental information

There are no known environmental, lifestyle or infectious contributors. Not applicable.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. Biallelic SLC25A46 loss-of-function variants **lead to** absent, unstable or interaction-defective SLC25A46 protein in the outer mitochondrial membrane.
   - Destabilizing missense variants are degraded by the ubiquitin–proteasome system (Steffen 2017 **[verify]**; Wan 2016; Janer 2016).
2. Loss of SLC25A46 **results in** an imbalance of fission and fusion towards **MFN1/2-mediated mitochondrial hyperfusion**, giving elongated, hyperconnected networks.
   - Shown in patient fibroblasts, knockout cells and zebrafish (Abrams 2015; Janer 2016).
   - SLC25A46 interacts with MFN2 and OPA1. A 2023 *Life Science Alliance* study in knockout fibroblasts (testing p.T142I, p.R257Q and p.E335D) localized SLC25A46 to discrete foci involved in fission and fusion.
   - A 2024 *C. elegans* preprint argues instead for a role in promoting fusion through FZO-1. That preprint is not peer-reviewed.
3. **Branch A, cristae and membrane lipids.** Loss of the SLC25A46–MIC60 (MICOS) interaction **leads to** abnormal cristae architecture and altered mitochondrial phospholipid composition. Janer et al. (2016) report that SLC25A46 functions upstream of MICOS and is required for cristae maintenance, with changes in ER morphology suggesting a defect at ER–mitochondria contact sites.
4. **Branch B, organelle distribution.** Enlarged, hyperfused mitochondria **lead to** impaired axonal transport and abnormal distribution in long axons. This was shown in Slc25a46-knockout mouse neurons (Li et al., *Hum Mol Genet* 2017;26:3776, PMID:28934388 **[verify]**).
5. Defective cristae and impaired mitophagy or quality control **lead to** reduced oxidative phosphorylation. Reported findings include:
   - impaired respiration;
   - reduced respiratory-chain complex activities and a raised lactate:pyruvate ratio in some patient fibroblasts;
   - premature senescence (Janer 2016).

   The link between step 4 and the energy deficit is inferred from cell and mouse data.
6. A bioenergetic and trafficking deficit in neurons with long axons and high energy demand **results in** degeneration of:
   - **retinal ganglion cells** and optic nerve axons, causing optic atrophy;
   - **peripheral motor and sensory axons**, causing axonal neuropathy;
   - **cerebellar Purkinje cells**, causing ataxia and cerebellar atrophy.

   All three are shown in knockout mice (Li 2017; Terzenidou et al., *PLoS Genet* 2017, PMC5380310, PMID:28376086 **[verify]**).
7. In the most destabilizing genotypes, near-complete loss during brain development **leads to** pontocerebellar hypoplasia and neonatal death (Wan 2016) or to Leigh syndrome (Janer 2016). The genotype–severity relationship is graded.

### Suggested GO, CL and UBERON terms

**GO biological processes** (look up each one):
- GO:0000266 mitochondrial fission
- GO:0008053 mitochondrial fusion
- GO:0042407 cristae formation
- GO:0047497 mitochondrion transport along microtubule
- GO:0000423 mitophagy
- GO:0006119 oxidative phosphorylation
- GO:0007005 mitochondrion organization

**GO cellular components:**
- GO:0005741 mitochondrial outer membrane
- GO:0061617 MICOS complex

**CL cell types:**
- CL:0000740 retinal ganglion cell
- CL:0000121 Purkinje cell
- CL:0000100 motor neuron
- CL:0000101 sensory neuron
- CL:0000057 fibroblast (patient-derived cell model only)

**UBERON anatomy:**
- UBERON:0000941 cranial nerve II (optic nerve)
- UBERON:0001021 nerve (peripheral nerve)
- UBERON:0002037 cerebellum
- UBERON:0000988 pons

**Molecular profiling.** No transcriptomic, proteomic, metabolomic or single-cell datasets specific to this disease were found. Lipidomic changes in mitochondria were reported by Janer et al. (2016).

---

## 7. Anatomical structures affected

- **Primary:** the optic nerve and retinal ganglion cells, and peripheral nerves (length-dependent axonal involvement).
- **Variable:** the cerebellum (Purkinje cells, atrophy) and, in severe forms, the pons, brainstem and basal ganglia.
- **Secondary:** distal limb musculature (neurogenic atrophy) and the feet (pes cavus).
- **Subcellular:** the mitochondrial outer membrane, inner-membrane cristae through MICOS, and ER–mitochondria contacts.
- **Laterality:** bilateral and symmetric.

---

## 8. Temporal development

- **Onset.**
  - Classic HMSN6B begins in childhood (often in the first decade) with visual loss and/or gait difficulty.
  - Ataxia-predominant forms begin in childhood or adolescence.
  - PCH forms are congenital or neonatal.
- **Course.** Chronic and slowly progressive. There is no remission.
- **Duration.** Lifelong. The severe forms are lethal in infancy.
- **Critical period.** In severe genotypes, CNS development (prenatal and neonatal) is the vulnerable window. Natural-history data are being collected under NCT04594590.

---

## 9. Inheritance and population

| Feature | Finding |
|---|---|
| Inheritance | Autosomal recessive (HP:0000007) |
| Penetrance | Apparently complete for biallelic pathogenic variants |
| Expressivity | Highly variable, both allelic and within families |
| Anticipation | None |
| Founder effects | Possible within North African families; none established |
| Consanguinity | Frequent in reported pedigrees |
| Prevalence | Ultra-rare: on the order of a few dozen published patients worldwide. No population estimate exists, so use `CASES_IN_LITERATURE` / `ULTRA_RARE` rather than a numeric band. |
| Sex ratio | Not skewed |
| Geography | Families reported from the USA/Europe, North Africa, the Middle East and Asia |

---

## 10. Diagnostics

- **Electrophysiology.** Nerve conduction studies show reduced or absent sensory and motor amplitudes with relatively preserved conduction velocities, i.e. an axonal pattern. EMG shows chronic denervation.
- **Ophthalmology.** Fundoscopy shows optic disc pallor. OCT shows thinning of the retinal nerve fiber layer. Visual evoked potentials are abnormal.
- **Imaging.** Brain MRI may show cerebellar atrophy, pontocerebellar hypoplasia in severe cases, or Leigh-type lesions.
- **Laboratory.** Lactate and the lactate:pyruvate ratio are raised in some patients. Respiratory-chain enzymology in fibroblasts or muscle may show combined deficiency.
- **Pathology.** Nerve biopsy (where performed) shows axonal loss. In fibroblasts, hyperfused mitochondrial networks support functional confirmation.
- **Genetic testing.** Exome or genome sequencing, or a CMT/hereditary optic neuropathy panel that includes SLC25A46. Deletion/duplication analysis is needed because exonic deletions have been reported. Confirm biallelic phase by parental testing.
- **Differential diagnosis.** MFN2-related CMT2A with optic atrophy (CMT6A), OPA1 "plus" disease, Friedreich ataxia, other mitochondrial disorders (POLG, NDUFS), Behr syndrome (OPA1, OPA3), and other forms of pontocerebellar hypoplasia (TSEN, EXOSC3).
- **Clinical criteria and screening.** There are no formal criteria and no newborn screening. Cascade carrier testing and prenatal or preimplantation diagnosis are available once the familial variants are known.

---

## 11. Outcome and prognosis

- **Classic HMSN6B:** survival into adulthood with progressive visual and motor disability.
- **PCH and Leigh forms:** death in the neonatal period or infancy (Wan 2016; Janer 2016; *J Pers Med* 2021).
- **Prognostic factor:** protein stability of the variant, i.e. destabilizing variants carry a worse outcome (Wan 2016; Abrams 2018).
- **Data gaps:** no survival statistics or QoL data are available.

---

## 12. Treatment

There is **no disease-modifying therapy**. Management is supportive:

| Intervention | Suggested NCIT term |
|---|---|
| Physical therapy | NCIT:C15302 Physical Therapy |
| Rehabilitation | NCIT:C15315 Rehabilitation |
| Orthotic management (ankle-foot orthoses) | Bind a clinical action. NCIT device terms do not belong in `TreatmentTerm`. |
| Orthopedic surgery for foot deformity | NCIT:C16186 Orthopedic Surgical Procedure |
| Low-vision support | Supportive Care, NCIT:C15747 |
| Genetic counseling | NCIT:C15240 Genetic Counseling |

Mitochondrial "cocktails" (coenzyme Q10, riboflavin) have been used empirically, but there is no evidence of benefit. Idebenone, approved for LHON in Europe, has not been studied in this disease. No interventional trials were found; NCT04594590 is an observational natural-history study.

---

## 13. Prevention

There is no primary prevention. The available measures are:
- genetic counseling, with 25% recurrence risk for carrier parents;
- carrier testing of relatives;
- prenatal or preimplantation genetic diagnosis;
- tertiary care for the feet, falls and vision.

---

## 14. Other species and natural disease

- No naturally occurring animal disease is recorded in OMIA (to be confirmed).
- Orthologs:
  - mouse *Slc25a46*;
  - zebrafish *slc25a46*;
  - *C. elegans* *slc-25A46*;
  - yeast *UGO1*, which is a distant functional analog rather than a strict ortholog.
- The protein's role in mitochondrial dynamics is conserved from yeast (Ugo1 links Fzo1 and Mgm1 in fusion) to vertebrates.

---

## 15. Model organisms

| Model | Phenotype and recapitulation | Reference |
|---|---|---|
| Zebrafish morphants | Increased mitochondrial connectivity; impaired neuronal development and maintenance | Abrams 2015 (PMID:26168012) |
| Slc25a46 knockout mouse (CRISPR 46-bp exon 8 deletion) | Severe ataxia from Purkinje cell degeneration; optic atrophy (retinal ganglion cell loss, small and unmyelinated optic nerve axons); axonal peripheral neuropathy with demyelination; large mitochondria with abnormal transport; early lethality | Li et al., *Hum Mol Genet* 2017;26(19):3776 (PMID:28934388 **[verify]**) |
| Forward-genetic *atc* mutant mouse | Lethal ataxia, optic atrophy, cerebellar hypoplasia and NMJ abnormalities; rescued by the human ortholog | Terzenidou et al., *PLoS Genet* 2017 (PMC5380310) |
| Patient fibroblasts / knockout human fibroblasts | Hyperfusion, cristae and lipid defects, impaired respiration; variant testing | Janer 2016; Life Sci Alliance 2023 (e202301914) |
| *C. elegans* slc-25A46 mutants | Neuronal morphological degeneration; FZO-1-dependent effects | bioRxiv 2024 (preprint) |

**Limitations of these models:**
- The mouse models are more severe than classic human HMSN6B and resemble the PCH end of the spectrum.
- No knock-in mice carrying the milder human missense variants have been reported.
- No iPSC-derived motor neuron or RGC model was identified.

---

## Key references

**Confirmed during this search**
1. Abrams AJ et al. *Nat Genet* 2015;47:926–32. **PMID:26168012**
2. Janer A et al. *EMBO Mol Med* 2016;8:1019–38. **PMID:27390132**
3. Wan J et al. *Brain* 2016;139:2877–90. **PMID:27543974**
4. Abrams AJ et al. *Hum Mutat* 2018. **PMID:30178502**

**PMID still to verify**
5. Li Z et al. *Hum Mol Genet* 2017;26:3776. PMID:28934388 **[verify]**
6. Terzenidou ME et al. *PLoS Genet* 2017;13:e1006656. PMID:28376086 **[verify]**
7. Steffen J et al. *Mol Biol Cell* 2017. PMID:28057766 **[verify]**
8. Charlesworth G et al. *Mov Disord* 2016;31:1249. PMID **[verify]**
9. Hammer MB et al. *Neurodegener Dis* 2017;17:208. PMID **[verify]**
10. Kodal LS et al. *Front Neurol* 2022. doi:10.3389/fneur.2022.1066040
11. Life Science Alliance 2023;6(6):e202301914. PMID **[verify]**
12. NCT04594590 (ClinicalTrials.gov)

## Sources
- [Nature Genetics – Abrams 2015](https://www.nature.com/articles/ng.3354)
- [Weill Cornell VIVO – PMID 26168012](https://vivo.weill.cornell.edu/display/pubid26168012)
- [Janer 2016 (PMC5009808)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5009808/)
- [SGD reference 27390132](https://www.yeastgenome.org/reference/27390132)
- [PubMed 27543974 – Wan 2016](https://pubmed.ncbi.nlm.nih.gov/27543974/)
- [Brain – Wan 2016](https://academic.oup.com/brain/article/139/11/2877/2422119)
- [Abrams 2018 (PMC6240357)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6240357)
- [HMG – Loss of SLC25A46 in mice](https://academic.oup.com/hmg/article/26/19/3776/3930120)
- [eScholarship – mouse paper](https://escholarship.org/uc/item/1d29m7v9)
- [PLoS Genet – Terzenidou 2017](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1006656)
- [Reanalysis – Leigh syndrome (PMC8703603)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8703603/)
- [UCL Discovery – Charlesworth 2016](https://discovery.ucl.ac.uk/id/eprint/10052524)
- [Bordeaux Neurocampus – Hammer 2017](https://www.bordeaux-neurocampus.fr/?p=146021)
- [Frontiers in Neurology – Kodal 2022](https://www.frontiersin.org/articles/10.3389/fneur.2022.1066040/full)
- [Life Science Alliance 2023](https://www.life-science-alliance.org/content/6/6/e202301914)
- [bioRxiv 2024 – C. elegans](https://www.biorxiv.org/content/10.1101/2024.02.11.579862.full.pdf)
- [IntechOpen review chapter](https://www.intechopen.com/chapters/63612)
- [ClinicalTrials.gov NCT04594590](https://clinicaltrials.gov/study/NCT04594590)
- [WikiPathways WP5521](https://www.wikipathways.org/pathways/WP5521.html)
- [GeneCards SLC25A46](https://www.genecards.org/card/SLC25A46)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014671` (3 mentions) - the report calls it "MONDO"; MONDO calls it **neuropathy, hereditary motor and sensory, type 6B**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (1 mention) - the report calls it "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.