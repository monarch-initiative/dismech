---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:32.129494'
end_time: '2026-10-23T02:00:10.108195'
duration_seconds: 277.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Microcephaly 26, Primary, Autosomal Dominant
  mondo_id: MONDO:0030928
  category: Mendelian
  causal_genes: LMNB1
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
  web_search_requests: 9
  num_turns: 24
  total_cost_usd: 2.1915379999999995
  session_id: 00b0645a-77c0-4158-bbe5-6095c4775439
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 18
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 58
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 4
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0004322
    reported_labels:
    - Postnatal
    ontology_label: Short stature
  - term_id: HP:0001508
    reported_labels:
    - Infancy
    ontology_label: Failure to thrive
  - term_id: HP:0001250
    reported_labels:
    - Childhood
    ontology_label: Seizure
  - term_id: HP:0002650
    reported_labels:
    - Childhood, progressive
    ontology_label: Scoliosis
  - term_id: HP:0006532
    reported_labels:
    - Likely aspiration-related (inference)
    ontology_label: Recurrent pneumonia
  - term_id: HP:0009879
    reported_labels:
    - Congenital
    ontology_label: Simplified gyral pattern
  - term_id: HP:0000243
    reported_labels:
    - Congenital
    ontology_label: Trigonocephaly
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly 26, Primary, Autosomal Dominant
- **MONDO ID:** MONDO:0030928 (if available)
- **Causal gene(s):** LMNB1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Microcephaly 26, Primary, Autosomal Dominant** covering all of the
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

I'm collecting the primary LMNB1 microcephaly papers. Next I'll read the OMIM molecular-genetics section and the full text of the 2020 AJHG paper.

Checking the ClinGen GenCC record, then writing the report.

# Microcephaly 26, Primary, Autosomal Dominant (MCPH26; MONDO:0030928): research report

**Causal gene: *LMNB1*** (lamin B1; HGNC:6637, written `hgnc:6637` in this repository; 5q23.2; gene MIM 150340). Every MCPH26 case reported so far carries a heterozygous *LMNB1* variant. Do not confuse this disease with two neighbours:
- *LMNB1*-related adult-onset autosomal dominant leukodystrophy (ADLD), which is caused by *LMNB1* duplication or overexpression.
- *LMNB2*-related microcephaly, a sister disease described in the same 2021 cohort paper.

> **Provenance caveats.** The PubMed MCP tool was not authorized in this session, and pubmed.ncbi.nlm.nih.gov would not render through WebFetch. The content below therefore comes from:
> - PMC full texts (PMC7536573, PMC7862057, PMC3226484)
> - an OMIM #619179 mirror
> - GenCC, ClinGen and Genomics England PanelApp pages
>
> The quoted strings are short excerpts returned by the fetch tool. Before using any of them as an evidence `snippet`, check it against `references_cache/` after running `just fetch-reference PMID:<id>`.
>
> The ontology CURIEs offered below are **leads, not bindings**. Per CLAUDE.md, look each one up (`runoak`, OLS, or `cache/*/terms.csv`) in the same step you write it into YAML.

---

## 1. Disease information

**Overview.** OMIM #619179 summarises the disease as follows. It is a primary microcephaly that is congenital and progressive, with global developmental delay. Intellectual development is impaired to a variable degree, from mild learning difficulty to being unable to walk or speak. Some patients also have:
- short stature
- spasticity
- feeding difficulties
- nonspecific dysmorphic facial features
- a simplified gyral pattern or corpus callosum dysgenesis on brain imaging

([OMIM 619179](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/619179))

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0030928 (microcephaly 26, primary, autosomal dominant) |
| OMIM (phenotype) | 619179 (MCPH26) |
| OMIM (gene) | 150340 (LMNB1); OMIM lists allelic variants .0002–.0007 for this disease |
| Orphanet | Under GenCC, Orphanet files *LMNB1* against the broader "Autosomal dominant primary microcephaly" (MONDO:0007988), rated "Supportive" ([GenCC LMNB1](https://thegencc.org/genes/HGNC:6637)) |
| ICD-10 / ICD-11 | No disease-specific code. Q02 (microcephaly) / LD20-family codes apply generically; not verified here |
| MeSH | Microcephaly (D008831), generic; not verified |

**Synonyms:** MCPH26; LMNB1-related primary microcephaly; B-type laminopathy with microcephaly. Parry et al. propose the disease defines a "novel laminopathy" ([PMC7862057](https://pmc.ncbi.nlm.nih.gov/articles/PMC7862057)).

**Data basis:** Everything known comes from aggregated case series: 14 probands across two primary papers plus OMIM, GenCC and PanelApp. There are no EHR- or registry-derived data.

**Gene–disease validity, by source** (from the [GenCC gene page](https://thegencc.org/genes/HGNC:6637))
- **ClinGen: Definitive.** Approved by the ClinGen Leukodystrophy and Leukoencephalopathy GCEP on 2025-12-10; GenCC lists the evaluation date as 2026-01-22. ClinGen scored 8.7 genetic points and 4 experimental points, the experimental points including two mouse models. It counted six missense variants and two in-frame deletions in 13 probands from three publications. ClinGen curates this disease as a separate entity from ADLD "because the phenotype and molecular mechanism differ." Verbatim: "there is definitive evidence supporting the relationship between LMNB1 and autosomal dominant microcephaly 26" ([SGC-179602.1](https://thegencc.org/submissions/SGC-179602.1)).
  - For the KB, this assertion fits `genetic[].gene_disease_validity` with `classified_by: CLINGEN`. Get the `CGGV:` identifier from `just clingen-list`; it was not retrieved here.
- **G2P: Definitive.**
- **Labcorp/Invitae and PanelApp Australia: Strong.**
- **Genomics England PanelApp "Severe microcephaly": Green**, upgraded from Amber in March 2022 ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/LMNB1/)).

---

## 2. Etiology

- **Cause:** a heterozygous germline *LMNB1* variant, monoallelic and autosomal dominant. Almost all are *de novo*. The variants are missense changes or in-frame deletions in the α-helical rod domain, plus one canonical splice-donor variant and one in-frame multi-exon deletion.
- **Not caused by haploinsufficiency:**
  - Large 5q23.2 deletions that include *LMNB1* have mostly been reported without microcephaly.
  - *LMNB1* pLI is 0.55.
  - No truncating variants have been found in patients.
  - *Lmnb1*+/− mice are not microcephalic.
  - (Cristofoli 2020; Parry 2021; [PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/LMNB1/): "suggest[s] a gain-of-function/dominant-negative effect rather than happloinsufficiency" [sic].)
- **Germline / somatic mosaicism in a parent:** In one Cristofoli family, an unaffected father who was ~15% mosaic for c.939+1G>A transmitted it to three affected children. In Parry 2021, an unaffected mosaic mother transmitted an *LMNB2* variant. One Cristofoli deletion arose *de novo* in a mildly affected mother and was passed to her daughter.
- **Environmental risk factors, protective factors, gene–environment interactions:** none reported. Not applicable to the disease as described.
- **Modifier genes:** none reported. Expressivity is highly variable, including between siblings who share the same splice variant (OFC −4.4 SD vs −10 SD).

---

## 3. Phenotypes

The two papers report different spectra:
- **Cristofoli 2020** (n = 7, "pronounced syndromic"): counts below are from its Table 1 ([PMC7536573](https://pmc.ncbi.nlm.nih.gov/articles/PMC7536573)).
- **Parry 2021** (7 *LMNB1* cases among 13 with B-type lamin variants): largely non-syndromic. OFC was −5.85 ± 1.14 SD across the *LMNB1* and *LMNB2* cases, height was mostly normal, there were no major malformations, and brain structure was usually normal ([PMC7862057](https://pmc.ncbi.nlm.nih.gov/articles/PMC7862057)).

| Phenotype | Frequency (Cristofoli, n=7) | Onset / course | Candidate HPO (verify) |
|---|---|---|---|
| Microcephaly, congenital, progressive (−3.6 to −12 SD) | 7/7; reduced at birth in all but one Parry case | Congenital; progressive | HP:0000252 Microcephaly; HP:0011451 Primary microcephaly; HP:0000253 Progressive microcephaly |
| Global developmental delay / intellectual disability (mild to severe) | 7/7 (severe 3, significant GDD 2, mod–severe 1, mild 1) | Infancy; static | HP:0001263; HP:0001249 |
| Absent or poor speech | Common; 3 older Parry children had no speech | Childhood | HP:0001344 Absent speech; HP:0000750 Delayed speech |
| Short stature (length < −2 SD) | 6/7 (Cristofoli); mostly *absent* in Parry | Postnatal | HP:0004322 |
| Feeding difficulty | 5/7, gastrostomy in 3 | Infancy | HP:0011968; HP:0011471 Gastrostomy tube feeding |
| Failure to thrive | Parry (count not extracted) | Infancy | HP:0001508 |
| Seizures (controlled) | 4/7; 4 cases in Parry | Childhood | HP:0001250 |
| Scoliosis | 4/7 (2 severe) | Childhood, progressive | HP:0002650 |
| Kyphosis | OMIM synopsis | — | HP:0002808 |
| Spasticity / spastic tetraparesis / non-ambulatory | 3/7 | — | HP:0001285 Spastic tetraparesis; HP:0002540 Inability to walk |
| Axial hypotonia / hypotonia | 3/7 | Infancy | HP:0008936 Axial hypotonia; HP:0001252 |
| Hyperreflexia | OMIM | — | HP:0001347 |
| Cortical visual impairment | 2/7 (+1 suspected) | — | HP:0100704 |
| Recurrent pneumonia | 3/7 | Likely aspiration-related (inference) | HP:0006532 |
| Simplified gyral pattern | 3/6 MRIs (Cristofoli); 2 Parry cases | Congenital | HP:0009879 |
| Pachygyria | 1/6 | Congenital | HP:0001302 |
| Abnormal corpus callosum (thin, dysgenetic, aplasia) | 3/6; 1 Parry case with aplasia | Congenital | HP:0001273 Abnormal corpus callosum morphology |
| Ventriculomegaly; reduced white matter; increased extra-axial spaces | Parry, 2 cases | — | HP:0002119 |
| Dysmorphism: sloping forehead, bitemporal narrowing, long philtrum, short nose, depressed nasal bridge, pointed chin, hypertelorism, up-slanted or long palpebral fissures | 5/7 nonspecific; no consistent gestalt in Parry | Congenital | HP:0000340 Sloping forehead; HP:0000343 Long philtrum; HP:0003196 Short nose; etc. |
| Gingival overgrowth | 2/7 | — | HP:0000212 |
| Trigonocephaly | Cristofoli (1) | Congenital | HP:0000243 |
| Overlapping toes | OMIM | — | HP:0001845 |
| Hypothyroidism | 2 cases in Parry (gene not separated from *LMNB2*) | — | HP:0000821 |

**Quality of life:** No formal measures (EQ-5D, PedsQL) have been published. The burden comes from severe ID, absent speech, inability to walk, tube feeding and respiratory infections in the severe end of the spectrum.

**Genotype–phenotype pattern (from the case tables):** The two most extreme cases (−12 SD) carry exon-1 head/rod-proximal missense variants, p.Lys33Glu and p.Arg42Trp. p.Lys33Glu recurs in four probands across both papers. The in-frame exon 6–8 deletion gave the mildest picture (−3.6 SD, normal height, mild ID). This is an observation, not a validated correlation.

---

## 4. Genetic and molecular information

**Gene:** *LMNB1*, HGNC:6637. It encodes lamin B1, a type V intermediate filament protein of the nuclear lamina, with a head domain, an α-helical rod (coils 1A, 1B, 2), an Ig-fold tail, and a C-terminal CaaX motif that is farnesylated.

**Reported MCPH26 variants** (NM_005573.3/.4)

| Variant | Domain | Probands | Origin | Source |
|---|---|---|---|---|
| c.97A>G p.(Lys33Glu) | Head/coil 1A boundary | 4 (Cristofoli Ind. 3; Parry P1, P9, P11) | *De novo* | PMID:32910914, 33033404 |
| c.97_99del p.(Lys33del) | Same position | 2 (Parry P2, P3) | *De novo* (P2); P3 untested | PMID:33033404 |
| c.124C>T p.(Arg42Trp) | Coil 1A | 1 | *De novo* | PMID:32910914 |
| c.269G>C p.(Arg90Pro) | Coil 1B | 2 (Parry P10, P13) | *De novo* (P10); P13 untested | PMID:33033404; [ClinVar RCV001292581](https://www.ncbi.nlm.nih.gov/clinvar/RCV001292581/) |
| c.455C>G p.(Ala152Gly) | Coil 1B | 1 | *De novo* | PMID:32910914 |
| c.939+1G>A (splice donor; predicted exon 5 skip or cryptic donor) | Rod | 3 siblings | Paternal ~15% mosaic | PMID:32910914 |
| Intragenic deletion of exons 6–8, in-frame p.(Ser314_Thr497del) | Coil 2 | 1 (mother mildly affected) | Arose *de novo* in the mother | PMID:32910914 |

- **Population frequency:** Parry reports that none of the variants are in gnomAD.
- **ClinVar:** pathogenic or likely pathogenic submissions exist for at least p.Arg90Pro. Check ClinVar for p.Lys33Glu and the others.
- **Functional class:** dominant-negative, possibly with some gain of function. No variant has been reported as a loss-of-function allele. For the KB, `GeneticContext.functional_impact_category: DOMINANT_NEGATIVE` matches the authors' proposal. Record it as the proposed mechanism; it has not been demonstrated for the splice and deletion alleles.
- **Allelic disorder (keep separate):** ADLD, caused by *LMNB1* tandem duplications or upstream deletions that raise *LMNB1* dosage. It presents as an adult-onset, slowly progressive CNS demyelination ([Padiath 2006, PMID:16951681](https://www.nature.com/articles/ng1872.pdf); [GeneReviews NBK338165](https://www.ncbi.nlm.nih.gov/books/NBK338165/)). ADLD and MCPH26 are opposite in direction: excess wild-type lamin B1 in ADLD versus a poisoned lamina in MCPH26. The ADLD-associated missense p.Arg29Trp did *not* disrupt the lamina in Cristofoli's assay.
- **Sister disease:** *LMNB2* heterozygous variants, e.g. the recurrent p.Glu398Lys and p.Asn54His, give an indistinguishable microcephaly (Parry 2021). Handle this as a separate MONDO entity or a grouping, not as a subtype of MCPH26.
- **Chromosomal:** 5q23.2 deletions that include *LMNB1* are generally not associated with microcephaly, which is the argument against haploinsufficiency.
- **Epigenetics:** None reported for MCPH26. Lamin B1 anchors lamina-associated domains (LADs) of heterochromatin. Whether LAD organisation is disturbed in patient cells has not been tested, so this remains an open gap.

---

## 5. Environmental information

There are no environmental, lifestyle or infectious contributors. Congenital microcephaly from TORCH or Zika infection, alcohol, or maternal PKU is a *differential diagnosis*, not a factor in this disease.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous *de novo* *LMNB1* rod- or head-domain variant** (missense, in-frame deletion, or splice variant producing an in-frame product) is expressed alongside the wild-type allele. *(Human genetic, demonstrated.)*
2. **The mutant lamin B1 is predicted to disrupt dimerisation and the head-to-tail or lateral assembly into filaments, poisoning the wild-type polymer.** This leads to an impaired nuclear lamina. *(Proposed by structural modelling on LMNA filaments; the C. elegans p.Lys33del orthologous variant disrupted protofilament assembly in vitro (Parry 2021). Direct in-vitro support comes from that one model only.)*
3. **The lamina is diffuse and poorly bounded, lamin B1 forms aggregates, and lamin B1 mislocalises to the cytoplasm.** In HeLa *LMNB1*-null cells, p.Lys33Glu reduced nuclear lamin B1 by 73% and p.Arg42Trp by 65%. GFP-tagged variants formed nuclear aggregates in both papers. *(In vitro, demonstrated.)*
   - Branch: p.Ala152Gly instead lowers steady-state lamin B1 (56 ± 15% of control in LCLs) and ruffles the lamin A/C envelope.
4. **Nuclear envelope integrity and shape are lost**: bi- or multi-lobed nuclei (p.Lys33Glu, p.Arg42Trp) or condensed nuclei (p.Ala152Gly), seen in transfected HeLa cells *and patient lymphoblastoid cells*. *(In vitro, demonstrated.)*
   - Ploidy (FISH) and spindle morphology in LCLs were normal, so no mitotic defect was shown in that cell type.
5. **In the developing cortex, a fragile nucleus is predicted to fail under the mechanical load of nucleokinesis, the nuclear translocation step of radial neuronal migration, and of interkinetic nuclear migration in progenitors.** This leads to nuclear membrane rupture, DNA damage and death of migrating neurons. *(Inferred for humans from mouse data.)*
   - *Lmnb1*-null and forebrain-conditional mice show "severe defects in neuronal migration and reduced numbers of neurons," single nuclear blebs, and caspase-3 activation ([Coffinier 2011, PMID:21976703, PMC3226484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3226484)).
   - Lamin B1-deficient migrating neurons show nuclear membrane ruptures linked to DNA damage and cell death ([Chen 2019, PNAS, PMID:31796586, PMC6926041](https://pmc.ncbi.nlm.nih.gov/articles/PMC6926041/)).
6. **Branch (proposed, not shown):** altered spindle orientation in neural progenitors drives premature neurogenic division and depletes the progenitor pool (Parry 2021 discussion). The LCL spindle data do not support it, but LCLs are not neural progenitors.
7. **Fewer cortical neurons, together with a depleted progenitor pool, lead to a reduced cortical volume**, i.e. primary microcephaly (HP:0011451). In severe cases it extends to a simplified gyral pattern, pachygyria and callosal dysgenesis, which is consistent with superimposed migration failure. *(Clinical, demonstrated; the link to step 5 is inferred.)*
8. **Reduced cortical neuron number and abnormal cortical organisation lead to developmental delay, intellectual disability, seizures, spasticity and cortical visual impairment.** Feeding difficulty, scoliosis and recurrent aspiration pneumonia are downstream of the neurological impairment. *(Inferred.)*
   - The cause of the short stature is unexplained. It may be a systemic lamina effect, since lamin B1 is ubiquitous; this is speculative.

**Where mice and humans disagree:** Mouse microcephaly requires *homozygous* loss, whereas the human disease is heterozygous dominant-negative. Record this as a `HUMAN_MODEL_MISMATCH` discussion, not as model support for haploinsufficiency (PanelApp reviewer; Parry 2021).

### Suggested ontology anchors (verify each before binding)

| Kind | Candidates |
|---|---|
| GO biological process | nuclear envelope organization (GO:0006998); nuclear membrane organization; neuron migration (GO:0001764); cerebral cortex radially oriented cell migration (GO:0021799); interkinetic nuclear migration (GO:0022027); neural precursor cell proliferation (GO:0061351); intermediate filament organization (GO:0045109) |
| GO cellular component | nuclear lamina (GO:0005652); nuclear envelope (GO:0005635); nuclear inner membrane |
| GO molecular function | structural molecule activity (GO:0005198) |
| CL | radial glial cell (CL:0000681); neural progenitor cell (CL:0011020); migrating neuron / cerebral cortex neuron (CL:0010012); B lymphoblast for the LCL data |
| UBERON | cerebral cortex (UBERON:0000956); brain (UBERON:0000955); corpus callosum (UBERON:0002336); ventricular zone (UBERON:0004040) |
| `biological_scale` | Step 2 MOLECULAR; steps 3–5 CELLULAR; step 7 TISSUE; step 8 ORGANISM |
| Module | Check `just list-modules` for neuronal migration, microcephaly or nuclear-envelope modules (e.g. cortical development or laminopathy) before writing `conforms_to` |

### Molecular profiling

No transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data specific to MCPH26 were found. No patient-derived iPSC or cortical organoid model has been published, which is a clear knowledge gap.

---

## 7. Anatomical structures

- **Primary:** brain, specifically cerebral cortex volume, gyration and corpus callosum. Effects are bilateral and symmetric.
- **Secondary:**
  - spine (scoliosis, kyphosis)
  - feeding and swallowing apparatus
  - lungs (recurrent pneumonia)
  - visual cortex (cortical visual impairment)
  - possibly thyroid (2 Parry cases) and linear growth
- **Cellular:** neural progenitors and migrating cortical neurons (inferred from mouse work). Patient LCLs show the nuclear phenotype.
- **Subcellular:** nuclear lamina and nuclear envelope. Mutant lamin B1 also mislocalises to the cytoplasm.

---

## 8. Temporal development

- **Onset:** congenital; microcephaly is present at birth in nearly all cases.
- **Course:** OFC SD worsens postnatally (progressive microcephaly). The neurodevelopmental impairment is static rather than degenerative. No regression has been described.
- **Ages reported:** 2–11 years in Cristofoli. No adults have been described.
- **Long-term natural history:** unknown.
- **Critical period:** fetal corticogenesis (inferred).
- **Remission:** none.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Most cases are *de novo*. Parental gonadosomatic mosaicism with recurrence in siblings has been documented, giving 3 affected siblings from a ~15% mosaic father.
- **Penetrance:** apparently high. A ~15% mosaic father was unaffected, and a heterozygous *de novo* mother was mildly affected.
- **Expressivity:** highly variable, including within one sibship.
- **Anticipation:** none.
- **Founder effects or consanguinity:** none. The probands were of European and Arabic ancestry.
- **Sex ratio:** 3 male / 4 female in Cristofoli.
- **Prevalence:** unknown, with ~14 published *LMNB1* probands. Use `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE`, or `NOT_YET_DOCUMENTED`, rather than inventing a rate.
- **Carrier frequency:** not applicable (dominant, *de novo*).

---

## 10. Diagnostics

- **Clinical:** serial OFC (≤ −3 SD) with developmental delay.
- **Imaging:** brain MRI to look for a simplified gyral pattern, pachygyria, callosal anomalies or ventriculomegaly, and to exclude acquired causes.
- **Genetic testing:**
  - Trio exome or genome sequencing is the first-line test. Both discovery cohorts used ES/GS (DDD, 100,000 Genomes).
  - Microcephaly gene panels: *LMNB1* is Green on the Genomics England "Severe microcephaly" panel.
  - CMA or exome CNV calling detected the exon 6–8 deletion.
  - Low-level parental mosaicism should be assessed (deep sequencing) for recurrence counselling.
- **Biomarkers:** none clinically validated. Lamin B1 immunofluorescence or nuclear morphology in LCLs or fibroblasts is research-only.
- **Differential diagnosis:**
  - autosomal recessive MCPH (*ASPM*, *WDR62*, *CDK5RAP2*, etc.; consanguinity, usually milder motor involvement)
  - *LMNB2* microcephaly (identical phenotype; distinguished only by gene)
  - other dominant microcephalies (e.g. *KIF11*, *DYRK1A*, *ANKLE2*-related; *TUBA1A*/*TUBB* tubulinopathies when there is a gyral simplification or pachygyria overlap)
  - congenital infections (CMV, Zika)
  - fetal alcohol spectrum disorder
- **Screening:** no newborn screening. Prenatal or preimplantation testing is possible for a known familial variant.

---

## 11. Outcome and prognosis

- **Survival and life expectancy:** no data. No deaths were reported in the cohorts, which only include children.
- **Morbidity:** spans mild learning difficulty to non-ambulatory, non-verbal, gastrostomy-fed children with scoliosis and recurrent pneumonia. Aspiration and respiratory infection are plausibly the main mortality risk (inference).
- **Prognostic factors:** perhaps the variant position. Exon-1 variants were the most severe; this is unvalidated.
- **QoL instruments:** none reported.

---

## 12. Treatment

No disease-modifying therapy exists, and no clinical trials were found. Management is supportive and multidisciplinary.

| Intervention | NCIT lead (verify) | `therapeutic_modality` |
|---|---|---|
| Antiseizure pharmacotherapy (seizures were "controlled" in 4/7) | NCIT:C15986 Pharmacotherapy; attach a specific `therapeutic_agent` only if a source names the drug | SMALL_MOLECULE |
| Gastrostomy / enteral tube feeding | NCIT procedure term (look up) | SURGERY / OTHER |
| Physical therapy (spasticity, hypotonia) | NCIT:C15302 | BEHAVIORAL |
| Speech and language therapy / AAC | NCIT:C159273 | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Scoliosis management (bracing or spinal fusion) | NCIT:C16186 Orthopedic Surgical Procedure | SURGERY |
| Visual rehabilitation for cortical visual impairment | — | BEHAVIORAL |
| Genetic counselling | NCIT:C15240 | — |
| Thyroid replacement if hypothyroid | Pharmacotherapy + levothyroxine | SMALL_MOLECULE |

- **Treatment evidence:** No source cites a treatment-outcome study. Treatment entries should carry evidence only where a source quote exists, or should be left unevidenced with notes.
- **Experimental and pharmacogenomic options:** none. Allele-specific ASO knockdown of the mutant allele is theoretically attractive for a dominant-negative disease, but the developmental window is prenatal, so it is not realistic. This is speculation and should not be curated.

---

## 13. Prevention

- Primary prevention is not possible for *de novo* events.
- Genetic counselling:
  - recurrence risk is low but non-zero because of parental mosaicism, as documented
  - offspring of an affected person have a 50% risk
- Prenatal diagnosis or PGT is available for a known variant.
- Tertiary prevention:
  - seizure control
  - nutritional support and aspiration precautions
  - scoliosis surveillance
  - thyroid screening

---

## 14. Other species and natural disease

- No naturally occurring animal disease is recorded; an OMIA check for *LMNB1* found nothing relevant.
- Orthologues: mouse *Lmnb1* (MGI), zebrafish *lmnb1*, and *C. elegans* *lmn-1*. *C. elegans* has a single lamin, which was used in Parry 2021 to model p.Lys33del.

---

## 15. Model organisms

| Model | Phenotype | Fit to MCPH26 | Evidence |
|---|---|---|---|
| *Lmnb1* gene-trap mutant mouse (homozygous), Vergnes 2004 | Perinatal death; lung and bone defects; misshapen fibroblast nuclei, polyploidy, premature senescence | Loss-of-function model; heterozygotes normal | PMID:15232008 (PMC478588) |
| *Lmnb1*−/− and forebrain-specific *Lmnb1* knockout (Emx1-Cre), Coffinier 2011 | Small forebrain/cortex; disordered layering (excess Ctip2+, few Cux1+ neurons); impaired neuronal migration; single nuclear blebs; asymmetric lamin B2; apoptosis. *Lmnb1/Lmnb2* double forebrain knockout gives near-complete cortical atrophy | `PARTIALLY_RECAPITULATES` microcephaly and neuron loss; `fidelity: LOW–MODERATE`. **Divergence:** homozygous null vs human heterozygous dominant-negative. Typed divergence: `PROXY_QUANTITY`/`OTHER` for allele mechanism, plus `SPECIES_MISMATCH` | PMID:21976703 (PMC3226484) |
| Lamin B1-deficient migrating neurons, Chen 2019 | Nuclear membrane ruptures, DNA damage, neuronal death | Supports the mechanism of step 5 | PMID:31796586 (PMC6926041) |
| *C. elegans* *lmn-1* carrying the p.Lys33del-equivalent | Disrupted protofilament assembly in vitro; nuclear lamin aggregates in vivo | Recapitulates the dominant-acting molecular defect (steps 2–3) | PMID:33033404 |
| HeLa *LMNB1*-null + variant cDNA; patient LCLs (Cristofoli); GFP-variant overexpression (Parry) | Lamina disruption, cytoplasmic mislocalisation, aggregates, abnormal nuclear shape; no aneuploidy or spindle defect in LCLs | `IN_VITRO`; non-neural cells; overexpression artefact possible (Parry noted expression above endogenous levels) | PMID:32910914, 33033404 |

**Missing models:** no heterozygous knock-in mouse carrying a patient allele, and no patient iPSC or cortical organoid model. These are the obvious proposed experiments for a `HUMAN_MODEL_MISMATCH` / `KNOWLEDGE_GAP` discussion.

---

## Evidence leads with short verbatim excerpts (verify against the reference cache)

| PMID | Type | Excerpt as returned by the fetch tool |
|---|---|---|
| 32910914, Cristofoli et al., *Am J Hum Genet* 2020;107:753–762, doi:10.1016/j.ajhg.2020.08.015 | HUMAN_CLINICAL + IN_VITRO | "we confirm this hypothesis with the identification of de novo mutations in LMNB1 in seven individuals" |
| 33033404, Parry et al., *Genet Med* 2021;23:408–414 | HUMAN_CLINICAL + IN_VITRO + MODEL_ORGANISM (C. elegans) | "We identify dominant pathogenic variants in LMNB1 and LMNB2 as a genetic cause of primary microcephaly"; "Recurrent variants were established to be de novo in nine cases" |
| 21976703, Coffinier et al., *Mol Biol Cell* 2011 | MODEL_ORGANISM | "severe defects in neuronal migration and reduced numbers of neurons" |
| 31796586, Chen et al., *PNAS* 2019;116:25870–25879 | MODEL_ORGANISM | Nuclear membrane ruptures and cell death in lamin B1-deficient migrating neurons; quote not retrieved |
| 15232008, Vergnes et al., *PNAS* 2004;101:10428–10433 | MODEL_ORGANISM | Quote not retrieved |
| 16951681, Padiath et al., *Nat Genet* 2006;38:1114–1123 | HUMAN_CLINICAL (allelic ADLD, for contrast only) | "Adult-onset autosomal dominant leukodystrophy (ADLD) is a slowly progressive neurological disorder characterized by symmetrical widespread myelin loss in the central nervous system" |

**Gaps to record in the entry:**
- prevalence
- adult natural history
- the mechanism behind short stature
- direct evidence of dominant-negative action for the splice and deletion alleles
- a human neural model
- whether LAD/chromatin organisation is disturbed
- ClinGen counts 13 probands from **three** publications; the third publication was not identified in this search

---

### Sources
- [OMIM #619179 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/619179)
- [Cristofoli et al. 2020, AJHG (PMC7536573)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7536573) · [PubMed 32910914](https://pubmed.ncbi.nlm.nih.gov/32910914/)
- [Parry et al. 2021, Genet Med (PMC7862057)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7862057) · [Edinburgh research portal](https://www.research.ed.ac.uk/en/publications/heterozygous-lamin-b1-and-lamin-b2-variants-cause-primary-microce/)
- [Coffinier et al. 2011 (PMC3226484)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3226484) · [PubMed 21976703](https://pubmed.ncbi.nlm.nih.gov/21976703)
- [Chen et al. 2019 PNAS (PMC6926041)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6926041/) · [review PMC7529418](https://pmc.ncbi.nlm.nih.gov/articles/PMC7529418/)
- [Vergnes et al. 2004 (PMC478588)](https://pmc.ncbi.nlm.nih.gov/articles/PMC478588)
- [Padiath et al. 2006 Nat Genet](https://www.nature.com/articles/ng1872.pdf) · [GeneReviews: LMNB1-Related ADLD](https://www.ncbi.nlm.nih.gov/books/NBK338165/)
- [GenCC LMNB1 gene page](https://thegencc.org/genes/HGNC:6637) · [ClinGen GenCC submission SGC-179602.1](https://thegencc.org/submissions/SGC-179602.1) · [GenCC LMNB2 SGC-125102.1](https://thegencc.org/submissions/SGC-125102.1)
- [Genomics England PanelApp: LMNB1, Severe microcephaly](https://panelapp.genomicsengland.co.uk/panels/162/gene/LMNB1/)
- [ClinVar RCV001292581 (p.Arg90Pro)](https://www.ncbi.nlm.nih.gov/clinvar/RCV001292581/)
- [MalaCards MCPH26](https://malacards.org/card/microcephaly_26_primary_autosomal_dominant)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004322` (1 mention) - the report calls it "Postnatal"; HP calls it **Short stature**
- `HP:0001508` (1 mention) - the report calls it "Infancy"; HP calls it **Failure to thrive**
- `HP:0001250` (1 mention) - the report calls it "Childhood"; HP calls it **Seizure**
- `HP:0002650` (1 mention) - the report calls it "Childhood, progressive"; HP calls it **Scoliosis**
- `HP:0006532` (1 mention) - the report calls it "Likely aspiration-related (inference)"; HP calls it **Recurrent pneumonia**
- `HP:0009879` (1 mention) - the report calls it "Congenital"; HP calls it **Simplified gyral pattern**
- `HP:0000243` (1 mention) - the report calls it "Congenital"; HP calls it **Trigonocephaly**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001302` (1 mention) - the report calls it "Congenital"; HP calls it **Pachygyria**, and lists "Macrogyria" among its other names
- `NCIT:C15302` (1 mention) - the report calls it "Physical therapy (spasticity, hypotonia)"; NCIT calls it **Physical Therapy**, and lists "Physical Therapeutics" among its other names
- `NCIT:C159273` (1 mention) - the report calls it "Speech and language therapy / AAC"; NCIT calls it **Speech Language Therapy**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**