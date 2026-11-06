---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-01T23:02:41.374080'
end_time: '2026-11-01T23:06:06.086198'
duration_seconds: 204.71
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: RNU4-2-Related Autosomal Recessive Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
  causal_genes: RNU4-2
  omim_id: not recorded
  synonyms: Recessive RNU4-2-related neurodevelopmental disorder; Recessive RNU4-2-associated
    neurodevelopmental disorder; Recessive RNU4-2 syndrome; Biallelic RNU4-2 neurodevelopmental
    syndrome
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
  num_turns: 16
  total_cost_usd: 2.6470166
  session_id: d98baee9-c229-5d8a-96f8-a4aee10f9c40
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 57
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0031936
    reported_labels:
    - 28/30; median first steps at 2.5 years
    ontology_label: Delayed ability to walk
  - term_id: HP:0001272
    reported_labels:
    - 12/24 (50%); OR 22.0 vs ReNU
    ontology_label: Cerebellar atrophy
  - term_id: HP:0000486
    reported_labels:
    - 15/28 (53.6%); eye involved 77.4%
    ontology_label: Strabismus
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RNU4-2-Related Autosomal Recessive Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Causal gene(s):** RNU4-2
- **OMIM:** not recorded
- **Synonyms:** Recessive RNU4-2-related neurodevelopmental disorder; Recessive RNU4-2-associated neurodevelopmental disorder; Recessive RNU4-2 syndrome; Biallelic RNU4-2 neurodevelopmental syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RNU4-2-Related Autosomal Recessive Neurodevelopmental Disorder** covering all of the
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

Reading the cached references for RNU4-2 that are already in the repository.

Writing the report now. First I'm checking the ontology IDs I plan to suggest against the repository's term caches, so none of them come from memory.

# RNU4-2-Related Autosomal Recessive Neurodevelopmental Disorder: Research Report

**Scope.** This disorder is caused by biallelic variants in **RNU4-2** (`hgnc:10193`). RNU4-2 is a non-protein-coding gene that makes the U4 small nuclear RNA (snRNA), a core part of the major spliceosome. This is a different disease from the dominant, usually de novo **ReNU syndrome**, even though both come from the same 145-nucleotide gene.

**Where the evidence comes from.** Almost everything known rests on three studies, all from 2026:

- **Rius et al. 2026, *Nat Genet*** (PMID:41951959): the disease-defining clinical cohort.
- **De Jonghe et al. 2026, *Nature*** (PMID:41951737): the companion saturation-editing study that found the disease.
- **Hayashi et al. 2026, *J Hum Genet*** (PMID:41408479): an independent Japanese/international series.

All three are already in `references_cache/`. Quotes below are copied from those cached files. A `kb/disorders/RNU4-2-Related_Autosomal_Recessive_Neurodevelopmental_Disorder.yaml` entry already exists and already uses most of this material.

---

## 1. Disease information

**Overview.** This is a moderate-to-severe syndromic neurodevelopmental disorder (NDD) caused by homozygous or compound heterozygous RNU4-2 variants. The variants lie outside the 18-nucleotide ReNU critical region. Its hallmark is a distinctive pattern of white-matter change on brain MRI.

- Rius et al.: "Here we describe a new recessive NDD associated with homozygous and compound heterozygous variants in RNU4-2." (PMID:41951959)
- Rius et al.: "we have characterized the phenotype associated with biallelic variants in RNU4-2 as a moderate-to-severe syndromic neurodevelopmental disorder with distinct white matter abnormalities." (PMID:41951959)
- De Jonghe et al.: "We show that these variants cause a new recessive neurodevelopmental disorder that is distinct from ReNU syndrome." (PMID:41951737)

**Identifiers**

| Resource | Status |
|---|---|
| MONDO | **No specific class found.** The existing entry records that an OLS4 search on 2026-11-01 found none. It uses `MONDO:0100500` (Mendelian neurodevelopmental disorder) as a `skos:broadMatch`. The ReNU syndrome class is MONDO:0971172. |
| OMIM | Not recorded. No OMIM phenotype entry turned up in web searches. |
| Orphanet, ICD-10, ICD-11, MeSH | No disease-specific codes found. MeSH indexing uses "Neurodevelopmental Disorders/genetics" and "RNA, Small Nuclear/genetics". |
| Gene | RNU4-2, `hgnc:10193`, RefSeq NR_003137.3, chr12 (GRCh38 chr12:120291753–120291903, from the SGE paper's methods) |

**Synonyms:** recessive RNU4-2-related (or -associated) NDD; recessive RNU4-2 syndrome; biallelic RNU4-2 neurodevelopmental syndrome.

**Data source.** The data are aggregated cohort data from individual patients in rare-disease sequencing programmes, not EHR data. The programmes are Genomics England 100,000 Genomes Project and NHS GMS, CaRDinal, SeqOIA/Auragen (PFMG 2025), UDN, Broad CMG and GREGoR. Controls came from UK Biobank and All of Us.

## 2. Etiology

**Cause.** The disease is caused by biallelic loss-of-function variants in RNU4-2. The variants fall in parts of U4 that bind other spliceosome components:

- "We identify 38 individuals with biallelic variants outside the 18-nucleotide ReNU syndrome region that cluster within other functionally important elements of U4: Stem II, the k-turn and the Sm protein binding site." (PMID:41951959)
- "These biallelic variants map to regions of U4 that are important for binding to other spliceosome components: the Stem II region of interaction with U6, the Sm protein binding site that is essential for snRNA biogenesis and stability, and the k-turn structure in the 5′ stem loop that binds to SNU13/15.5k." (PMID:41951959)

**Genetic risk factors**

- **Parental consanguinity.** "Eight individuals from five families, all of whom had homozygous variants, had consanguineous parents." (PMID:41951959)
- **High mutation rate at the locus.** "RNU4-2, like other snRNA genes, has a substantially elevated mutation rate" (PMID:41951959). The same paper notes that negative selection keeps every variant very rare. This lowers the chance of homozygosity in outbred populations.

**Modifier genes.** None established. RNU4-1, the paralog, is upregulated in affected people but does not compensate fully (see section 6).

**Environmental, protective and gene–environment factors.** None reported. The disease is purely genetic.

## 3. Phenotypes

The figures below come from 31 individuals with detailed data (21 male, 10 female; median age at last follow-up 10 years, range 6 weeks to 32 years) in Rius et al. 2026, Table 1 (PMID:41951959). All suggested HP IDs were checked against `cache/hp/terms.csv`.

| Phenotype | Frequency | Suggested HPO | Key quote / note |
|---|---|---|---|
| Global developmental delay / ID | 30/30 (100%); severe 51.7%, moderate 44.8% | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | "Global developmental delay (GDD) or intellectual disability (ID) was present in all individuals (n = 30)." |
| Delayed language | 29/29 (100%) | HP:0000750 | "All individuals (n = 29; 100%) exhibited delayed language development." |
| Absent speech | 15/29 (51.7%) | HP:0001344 | "Fifteen (51.7%) individuals older than 2 years were nonverbal or had no meaningful spoken language." |
| Delayed walking | 28/30; median first steps at 2.5 years | HP:0031936 | Inability to walk at age 5 or older: 7/25 (28%) |
| Hypotonia (neonatal onset in 64%) | 26/31 (83.9%) | HP:0001252 | "Most individuals had a history of hypotonia (83.9%; 26 of 31), with neonatal onset in 64% (19 of 26), which was commonly associated with feeding difficulties." |
| Feeding difficulties | 12/25 (48%) | HP:0011968 | |
| Seizures (median onset 2.2 years) | 19/31 (61–63%) | HP:0001250 | Mostly respond to treatment; 3/19 are pharmacoresistant; no status epilepticus |
| Spasticity | 15/30 (50%) | HP:0001257 | |
| Movement disorder | 13/30 (43.3%) | HP:0001251 Ataxia (n=9); HP:0001332 Dystonia (n=3); HP:0001266 Choreoathetosis (n=1) | |
| Abnormal brain MRI | 24/27 (88.9%) | HP:0002500 Abnormal cerebral white matter morphology | |
| Dilated perivascular spaces | 18/23 (78.3%) | No HP term in the local cache; search HPO for "perivascular space" before binding | "the recessive disorder frequently presents dilated perivascular spaces that can mimic a compact microcystic appearance (18 of 23; 78.3%" |
| White matter volume loss | common, not counted separately | HP:0034295 Reduced cerebral white matter volume | |
| Cerebellar atrophy | 12/24 (50%); OR 22.0 vs ReNU | HP:0001272 | Both the hemispheres and the vermis can be involved |
| Corpus callosum abnormality | 11/21 (52.4%) | HP:0033725 Thin corpus callosum | Also common in ReNU syndrome |
| Ventriculomegaly (early scans) | seen in several individuals | HP:0002119 | |
| Strabismus | 15/28 (53.6%); eye involved 77.4% | HP:0000486 | |
| Facial dysmorphism | 24/30 (80%) | HP:0009890 High anterior hairline; HP:0000664 Synophrys; HP:0000582 Upslanted palpebral fissure; HP:0000219 Thin upper lip vermilion; HP:0000699 Diastema | GestaltMatcher distinguishes this face from the ReNU face |
| Microcephaly | 13/30 (43.3%) | HP:0000252 | |
| Short stature | 13/30 (43.3%) | HP:0004322 | |
| Male genital anomalies | 9/21 males (42.8%) | HP:0000054 Micropenis; HP:0000028 Cryptorchidism | None reported in females |
| Skin and nail findings | 17/28 (60.7%) | HP:0000998 Hypertrichosis; HP:0033505 Livedo reticularis | Also acrokeratosis verruciformis, hypoplastic nails |
| Behavioural abnormality | 14/23 (60.9%) | HP:0000718 Aggressive behavior; HP:0100716 Self-injurious behavior; HP:0000712 Emotional lability | OCD traits in 6 |
| Autism spectrum disorder | 6/21 (28.6%) | HP:0000717 | |
| Failure to thrive | 7/26 (26.9%) | HP:0001508 | |
| Dental, skeletal and endocrine anomalies | 42%, 30%, 31% | — | |

**Onset.** "Most individuals had infantile-onset phenotypes (n = 16; 51.6%), while ten (32.2%) had congenital or neonatal onset and five (16.1%) had childhood onset." (PMID:41951959)

**Severity relative to ReNU syndrome.** The two available sources differ:

- Hayashi et al. describe their biallelic cases as milder: "individuals with biallelic variants exhibited developmental delay and intellectual disability that were similar to but milder than those with monoallelic variants, notably lacking extracerebral organ involvement" (PMID:41408479). That cohort had only 4 individuals from 2 families.
- Rius et al. report GDD, speech delay and seizure frequencies similar to ReNU, plus extracerebral involvement (genital, skin, dental).

**Quality of life.** No validated QoL instrument data exist. Lifelong dependence can be inferred from the high rates of nonverbal status and non-ambulation.

## 4. Genetic and molecular information

**Gene.** RNU4-2 (`hgnc:10193`) encodes the U4 snRNA. Alignment with its paralog RNU4-1 shows mismatches at "only 4 of the 145 nt" (PMID:41951737).

**Variant spectrum (Rius et al.)**

- 35 unique variants in 38 included individuals: 7 homozygous variants (13 individuals) and 31 compound heterozygous variants (25 individuals).
- Variants seen in both the homozygous and compound heterozygous state: n.127C>T, n.119A>G and n.7G>C.
- The broader search found 43 individuals from 33 families. "Fifteen individuals from 11 families had homozygous variants, and 27 individuals from 22 families had compound heterozygous variants." Five were later excluded because their SGE scores were similar to those in the population.

**Variant types.** Mostly single-nucleotide variants, plus small indels such as n.7_8insA and n.43_44insT. This is a noncoding RNA, so "missense" and "nonsense" do not apply.

**Structural regions.** The SGE paper defines these coordinates (PMID:41951737):

| Region | Nucleotides | Binding partner / role |
|---|---|---|
| Stem II | n.3–16 (central core n.6–11) | Pairs with U6 |
| k-turn of the 5′ stem loop | n.27–35 and n.41–46 | Binds SNU13/15.5K |
| Sm site | n.118–126 | Sm protein ring; biogenesis and stability |
| Terminal stem loop | n.127–144 (pairing n.129–131 with n.140–142) | — |

The ReNU critical region (T-loop n.62–70, Stem III n.75–78) is spared in this disorder. Population variants are instead enriched in the 3′ stem loop (n.85–117): 7 of 14 UK Biobank variants versus 0 of 35 case variants, P = 5.0×10⁻⁴.

**Equivalent RNU4ATAC variants.** Thirteen of the 35 variants (37.1%) sit at nucleotides where the equivalent RNU4ATAC variant is pathogenic or likely pathogenic. Five exact equivalents are listed in the SGE paper: n.32G>A, n.45G>C, n.46G>A, n.119A>G and n.122T>G. For n.119A>G, the RNU4ATAC equivalent n.117A>G is ClinVar ID 1525441. n.119A>G was homozygous in two individuals and compound heterozygous in three (PMID:41951737).

**ACMG/AMP classification**

- Of the 35 variants: 1 pathogenic, 8 likely pathogenic, the rest VUS.
- Per individual: 10/38 (26.3%) had P/LP variants on both alleles, 4/38 had one P/LP allele, and 24/38 (63.2%) had VUS on both alleles (PMID:41951959).
- No phenotype frequency differed between the P/LP–P/LP group and everyone else.

**Using the SGE function scores clinically**

- A variant counts as significantly depleted (deleterious) when its function score is below −0.302.
- The SGE authors recommend that "PS3 supporting evidence be assigned to significantly depleted variants outside the CR" (PMID:41951737).
- A normal score does not show a variant is benign: "normal SGE scores should not be used as evidence of benignity in a recessive context" (PMID:41951959).
- Only 20 of 35 case variants (57.1%) were SGE-significant.

**Population frequency**

- SGE-depleted variants outside the critical region are carried by 0.12% of UK Biobank and 0.094% of All of Us participants (PMID:41951737).
- Only 11 UK Biobank participants were biallelic; none had a neurodevelopmental phenotype.
- Only one UK Biobank / All of Us individual was homozygous for an SGE-depleted variant (n.31T>G, score −0.730). That person reported cognitive and functional difficulties suggestive of possible ID (PMID:41951737).

**Other genetic features**

- **Origin:** germline, inherited from carrier parents.
- **Parental origin of alleles:** maternal and paternal alleles had similar SGE scores (P = 0.095).
- **Heterozygous carriers:** carriers of depleted variants outside the critical region (n = 592 in UK Biobank) showed no differences in fluid intelligence, developmental diagnoses or education.
- **Epigenetics and chromosomal abnormalities:** none reported. The disease is not caused by copy-number change.

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors are reported.

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic germline variants arise in RNU4-2 in Stem II, the 5′-stem-loop k-turn, the Sm site or the terminal stem loop. These variants **disrupt** U4's binding to U6, SNU13/15.5K or the Sm ring. This step is inferred from structure, from yeast U4 mutagenesis and from in vitro SNU13 binding data, as cited in PMID:41951737.
2. → This **leads to** reduced steady-state U4 (RNU4-2) RNA. This is shown in blood RNA-seq: mean 314 TPM versus 1,645 TPM in controls, P = 0.012 (PMID:41951959). Impaired biogenesis or stability is the presumed route, which is inferred, especially for Sm-site variants.
3. → This is accompanied by compensatory upregulation of RNU4-1 (1,952 vs 346 TPM). The RNU4-2:RNU4-1 ratio shifts from 5.4 in controls to 0.2 (P = 0.003). Rius et al.: "Our data suggest that RNU4-1 cannot fully compensate for loss of RNU4-2." The reason is not known. Their three candidate explanations are functional divergence, insufficient upregulation, or tissue-specific failure in the brain.
4. → The net result is **partial loss of function** of U4-containing complexes (U4/U6 di-snRNP and U4/U6·U5 tri-snRNP) and the major spliceosome. Cell-fitness loss is shown in haploid HAP1 cells by SGE. The specific splicing defect has **not been demonstrated**:
   - No ReNU-type 5′ splice-site signature appears in lymphocyte RNA-seq.
   - No excess intron retention appears in blood, unlike RNU4ATAC disease.
   - The authors suggest the defect is subtle, because a global defect across U2-type introns would be nonviable.
5. → In the nervous system this **results in** abnormal development and white-matter integrity: dilated perivascular spaces, white-matter volume loss, cerebellar atrophy and a thin corpus callosum. Serial imaging shows these can be progressive. The cell-level link between U4 loss and these findings is unknown. Oligodendrocyte or glial vulnerability is a hypothesis only.
6. → This **produces** the clinical picture: GDD/ID, absent speech, hypotonia, spasticity and ataxia, and seizures.
   - Branch: an extracerebral, multisystem arm (genital, skin, dental, growth). Its mechanism is not studied.

**How it differs from ReNU syndrome**

- ReNU variants (T-loop and Stem III) mis-position the U6 ACAGAGA box. This alters 5′ splice-site selection, a dominant mechanism.
- In ReNU, RNU4-2 RNA is *raised* (2,699 TPM) rather than reduced.
- "Together, these data suggest that dominant and recessive RNU4-2 disorders are driven by different molecular processes and are consistent with a loss-of-function mechanism in the recessive condition." (PMID:41951959)

**Suggested ontology terms** (checked against the local caches)

- **GO:**
  - GO:0005687 U4 snRNP
  - GO:0046540 U4/U6 x U5 tri-snRNP complex
  - GO:0000244 spliceosomal tri-snRNP complex assembly
  - GO:0000387 spliceosomal snRNP assembly
  - "mRNA splicing, via spliceosome" is **not** in the local cache; look it up before use.
- **CL:** CL:0000540 neuron; CL:0000128 oligodendrocyte; CL:0000127 astrocyte; CL:0000121 Purkinje cell (relevant given cerebellar atrophy; speculative); CL:0000542 lymphocyte (the tissue in which RNA changes were measured).
- **Model and assay context:** the SGE assay was run in HAP1-LIG4-KO cells; evidence from it is IN_VITRO.

**Omics**

- Blood RNA-seq from the Genomics England NGRL (n = 7,826; 3 biallelic cases).
- Lymphocyte RNA-seq (3 biallelic cases, 19 ReNU, 20 controls).
- No proteomic, metabolomic, single-cell or spatial data exist.

## 7. Anatomical structures affected

- **Primary:** brain.
  - Cerebral white matter: periventricular and deep, peritrigonal.
  - Cerebellum (UBERON:0002037): both hemispheres and vermis.
  - Corpus callosum (UBERON:0002336).
  - Lateral ventricles (ventriculomegaly).
  - "Cerebral white matter" is not in the local UBERON cache; look it up before use.
- **Secondary:** eye (strabismus), male external genitalia, skin and nails, teeth, skeleton, endocrine system, and growth.
- **Subcellular:** nucleus, specifically the spliceosomal snRNPs (GO:0005687, GO:0046540).
- **Laterality:** the white-matter changes are bilateral and symmetric (for example, "peritrigonal region bilaterally").

## 8. Temporal development

- **Onset:** congenital or neonatal in 32%, infantile in 52%, childhood in 16%. Hypotonia is often neonatal.
- **Course:** a static neurodevelopmental disorder in which imaging can progress. Two siblings imaged serially from infancy at first showed only ventriculomegaly. Follow-up "revealed progressive pathology, including perivascular space dilation, white matter volume loss and cerebellar atrophy." Perivascular dilation also increased between 32 months and 7 years in another individual (PMID:41951959).
- **Within families:** siblings were largely concordant, but expressivity varied. In three sibships, one child walked and the other did not.
- **Duration:** lifelong. The oldest reported individual was 32. No remission has been described.
- **Critical period:** early childhood, when white-matter change appears to evolve. This is not formally established.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007), homozygous or compound heterozygous.
- **Penetrance:** not established. Rius et al. note that some included individuals may be false positives and that some excluded individuals may be true cases.
- **Expressivity:** variable, including within sibships.
- **Anticipation and germline mosaicism:** none reported.
- **Founder effects:** none reported.
- **Consanguinity:** important. All five consanguineous families carried homozygous variants.
- **Frequency:** much rarer than ReNU syndrome. "while we identified 61 individuals with ReNU syndrome in 8,841 individuals (0.69%) with previously undiagnosed NDD in the Genomics England 100,000 Genomes Project, we only identified seven (0.08%) with biallelic variants in the same cohort." (PMID:41951959)
- **Case enrichment:** 6/5,386 undiagnosed NDD trios versus 0/4,776 non-NDD trios (P = 3.3×10⁻³).
- **Population prevalence and incidence:** unknown. The authors expect higher frequency in populations with more consanguinity.
- **Carrier frequency:** about 0.1% carry SGE-depleted variants outside the critical region (UK Biobank 0.12%, All of Us 0.094%). This is a ceiling on the frequency of deleterious alleles, not a confirmed carrier rate.
- **Sex:** 21 male and 10 female in the clinical cohort. This is probably ascertainment, not biology; a recessive autosomal locus should affect both sexes.
- **Geography:** cases from the UK, France, Germany, the USA, Australia, Turkey and Pakistan, plus a Japanese/Israeli/Malaysian/Brazilian series in Hayashi et al. No endemic clustering has been reported.

## 10. Diagnostics

- **Genetic testing is required.** RNU4-2 is noncoding and is missed by standard exome capture.
  - Whole-genome sequencing (NCIT:C101294) is the recommended test.
  - Extended-exome designs that capture snRNA genes also work. PMID:42502410 reports WGS reanalysis of 1,578 unsolved probands that found RNU4-2 cases, and recommends extended-exome screening.
  - Variant calling must allow for paralog and pseudogene homology with RNU4-1.
- **Phasing:** use parental testing, or read-backed phasing in IGV when parents are unavailable.
- **Variant interpretation:**
  - Use the SGE function scores at **supporting** strength (PS3_supporting) for significantly depleted variants outside the critical region.
  - Check whether the equivalent RNU4ATAC nucleotide is pathogenic.
  - Check the structural region.
- **Imaging:** MRI (NCIT:C16809). Marked periventricular perivascular-space dilation with a "tightly packed microcystic" appearance should prompt RNU4-2 analysis: "The presence of these changes on MRI, particularly the marked periventricular perivascular space dilation, should prompt sequencing and analysis of variants in RNU4-2." (PMID:41951959)
- **Candidate RNA biomarker (not yet validated):** the RNU4-2:RNU4-1 expression ratio in rRNA-depleted blood RNA-seq. "it could be a useful diagnostic biomarker for the recessive disorder, if validated in additional cohorts." (PMID:41951959)
- **Facial gestalt:** GestaltMatcher separates biallelic cases from ReNU cases (biallelic–biallelic pairs P = 1.8×10⁻⁵; ReNU–biallelic pairs P = 0.37).
- **EEG:** obtain one when seizures occur. No characteristic pattern has been reported.
- **Differential diagnosis:**
  - ReNU syndrome. Distinguished by a heterozygous T-loop or Stem III variant, the 5′ splice-site signature, raised RNU4-2 RNA, myopathic facies and no cerebellar atrophy.
  - Recessive RNU2-2 disorder.
  - RNU4ATAC disorders (MOPD I, Lowry–Wood, Roifman).
  - RNU12 disorder.
  - Other leukodystrophies and metabolic disorders with enlarged perivascular spaces, such as mucopolysaccharidoses.
  - Hypomyelinating leukodystrophies.
- **Screening:** there is no newborn screening. Carrier and prenatal testing are possible once the familial variants are known.

## 11. Prognosis

- No mortality or survival data exist. Individuals up to 32 years old have been reported.
- Disability is substantial: about half are nonverbal, and 28% are non-ambulatory after age 5.
- Epilepsy is mostly controllable: 13 of 17 treated individuals were on monotherapy, 3 were pharmacoresistant, and none had status epilepticus.
- Prognostic factors are not established. More severe perivascular dilation went with lower mean SGE scores, but not significantly (P = 0.056, n = 5 per group).

## 12. Treatment

No disease-specific treatment exists. Management is symptomatic.

- **Antiseizure medication:** NCIT:C15986 Pharmacotherapy, with NCIT:C264 Anticonvulsant Agent as the agent class.
- **Therapies:** physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351) and speech-language therapy (NCIT:C159273), including AAC for nonverbal patients.
- **Supportive care** (NCIT:C15747) for feeding difficulties, plus ophthalmology for strabismus, and urology or endocrine follow-up.
- **Genetic counselling:** NCIT:C15240.
- **Experimental:** no clinical trials were found. Because the disease is loss of function, restoring or augmenting U4 (for example, upregulating RNU4-1) is a conceivable future approach. This is speculative, and the SGE authors frame their data only as a resource for "therapeutic development."
- **Pharmacogenomics:** none known.

## 13. Prevention

- **Primary prevention:** genetic counselling. The recurrence risk is 25% for carrier couples.
- **Carrier, prenatal and preimplantation testing:** possible once both familial variants are identified. Carrier screening is especially relevant in consanguineous families.
- **Tertiary prevention:** seizure control, orthopaedic care for spasticity, and nutritional support.
- **Vaccines and public-health measures:** not applicable.

## 14. Other species

No naturally occurring animal disease has been reported, and there is no OMIA entry. U4 snRNA is deeply conserved. The RNU4-2 upstream region "is both unique and poorly conserved across species" (PMID:41951737). Yeast U4 mutagenesis implicates the same regions (stem II, k-turn, Sm site) as essential for function. Copy-number and paralog structure differ between species, so a one-to-one ortholog mapping needs care. No NCBI Gene orthology details were checked here.

## 15. Model systems

- **In vitro:** saturation genome editing in HAP1-LIG4-KO haploid human cells. All possible SNVs across the 145-nt transcript plus 6 nt 3′ (539 variants) were tested, with a cell-fitness readout (PMID:41951737).
  - Strength: it found the recessive disease and gives variant-level function scores.
  - Limitations:
    - It does not separate dominant from recessive effects; a diploid HAP1 screen did not either.
    - It does not measure the splicing mechanism.
    - It reports nothing about brain cells.
    - It is less sensitive for recessive variants.
- **Patient-derived samples:** lymphocyte cultures and whole blood (RNA-seq).
- **Animal models:** none reported (no mouse, zebrafish or fly).
- **Gaps:** neural iPSC models, organoids, or oligodendrocyte or glial models are needed to find the splicing defect and explain the white-matter pathology. Rius et al. say a splicing defect "may require additional samples sequenced at higher depth or sequencing of disease-relevant cell types and tissues."

---

## Points for the curator

- **No MONDO or OMIM identifiers exist yet.** Keep the `broadMatch` to MONDO:0100500 until MONDO adds a class.
- **Two sources disagree on severity.** Hayashi et al. (n = 4) describe the disorder as milder and without extracerebral involvement; Rius et al. (n = 31) report extracerebral features. Record this as a disagreement rather than resolving it.
- **No splicing signature has been shown.** The loss-of-function claim rests on reduced RNU4-2 RNA and on analogy with RNU4ATAC disease, not on any demonstrated splicing defect. The `KNOWLEDGE_GAP` and `HUMAN_MODEL_MISMATCH` discussion kinds both fit here.
- **Two terms need lookup before binding.** "Dilated perivascular spaces" (HPO) and "mRNA splicing, via spliceosome" (GO) are not in the local caches. Look both up rather than writing an ID.

## Sources

- Rius R et al. Biallelic variants in the noncoding RNA gene RNU4-2 cause a recessive neurodevelopmental syndrome with distinct white matter changes. *Nat Genet* 2026. PMID:41951959. [nature.com/articles/s41588-026-02554-6](https://www.nature.com/articles/s41588-026-02554-6); preprint at [medRxiv 2025.08.13.25333306](https://www.medrxiv.org/content/10.1101/2025.08.13.25333306v1.full.pdf); [Crick record](https://www.crick.ac.uk/research/publications/biallelic-variants-in-the-non-coding-rna-gene-rnu4-2-cause-a-recessive-neurodevelopmental-syndrome-with-distinct-white-matter-changes)
- De Jonghe J et al. Saturation editing of RNU4-2 reveals distinct dominant and recessive disorders. *Nature* 2026. PMID:41951737. [nature.com/articles/s41586-026-10334-9](https://www.nature.com/articles/s41586-026-10334-9)
- Hayashi Y et al. Monoallelic and biallelic RNU4-2 variants in neurodevelopmental disorders. *J Hum Genet* 2026. PMID:41408479. [nature.com/articles/s10038-025-01442-x](https://www.nature.com/articles/s10038-025-01442-x); [PubMed](https://pubmed.ncbi.nlm.nih.gov/41408479/)
- Whole-genome discovery of pathogenic snRNA variants and efficient extended-exome screening. PMID:42502410 (cached)
- Background on dominant ReNU syndrome: Chen Y et al. 2024 *Nature* (PMID:38991538); Greene D et al. 2024 *Nat Med* (PMID:38821540); dismech [ReNU Syndrome page](https://dismech.monarchinitiative.org/pages/disorders/ReNU_Syndrome.html)
- Related recessive snRNA disorder: [RNU2-2 medRxiv preprint](https://www.medrxiv.org/content/10.1101/2025.09.02.25334957.full.pdf)
- Oxford bibliographic record: [ndm.ox.ac.uk publication 2404058](https://www.ndm.ox.ac.uk/publications/publication_modal/2404058)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 57 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031936` (1 mention) - the report calls it "28/30; median first steps at 2.5 years"; HP calls it **Delayed ability to walk**
- `HP:0001272` (1 mention) - the report calls it "12/24 (50%); OR 22.0 vs ReNU"; HP calls it **Cerebellar atrophy**
- `HP:0000486` (1 mention) - the report calls it "15/28 (53.6%); eye involved 77.4%"; HP calls it **Strabismus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C16809` (1 mention) - the report calls it "Imaging:** MRI"; NCIT calls it **Magnetic Resonance Imaging**, and lists "MR Imaging" among its other names
- `NCIT:C15302` (1 mention) - the report calls it "Therapies:** physical therapy"; NCIT calls it **Physical Therapy**
