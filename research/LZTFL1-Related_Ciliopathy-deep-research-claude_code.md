---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T15:21:59.769408'
end_time: '2026-11-25T15:27:05.195490'
duration_seconds: 305.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: LZTFL1-Related Ciliopathy
  mondo_id: MONDO:1040046
  category: Mendelian
  causal_genes: LZTFL1
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
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 0.67601355
  session_id: acb24f85-f73a-4e2c-8979-a4502ba4a52a
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 33
  retrieval_calls: 31
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 13
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:20301537
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 39
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0034464
    reported_labels:
    - 'Cellular component: BBSome'
    ontology_label: BBSome
  - term_id: CL:0000604
    reported_labels:
    - Suggested CL terms:** rod photoreceptor cell
    ontology_label: retinal rod cell
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  service_unreachable: 9
  obsolescence_unchecked: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LZTFL1-Related Ciliopathy
- **MONDO ID:** MONDO:1040046 (if available)
- **Causal gene(s):** LZTFL1
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

Please provide a comprehensive research report on **LZTFL1-Related Ciliopathy** covering all of the
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

I'm pulling the primary abstracts. PubMed is rate-limiting, so I'm switching to the Europe PMC API.

# LZTFL1-Related Ciliopathy (MONDO:1040046): Research Report

**How I scoped this:** I took "LZTFL1-related ciliopathy" (MONDO:1040046) to be the disease caused by biallelic loss-of-function variants in **LZTFL1** (leucine zipper transcription factor like 1; NCBI Gene 54585). Clinically this disease is Bardet-Biedl syndrome type 17 (**BBS17**; OMIM 615994, per [MedGen C3714980](https://ncbi.nlm.nih.gov/medgen/811538)). I could not retrieve the MONDO record itself, so I have not confirmed its label, definition or cross-references.

**About the sources:**
- PubMed was rate-limiting during this session. I retrieved abstracts through the Europe PMC REST API. Quotes are short verbatim excerpts, up to 125 characters, because of a quoting limit.
- Many sections below are marked "not available" because the published literature is very small. Only about 7–8 patients with biallelic variants have been reported.
- I did not retrieve OMIM, Orphanet, ClinVar or gnomAD records directly. Statements based on those resources are flagged.

---

## 1. Disease Information

**Overview.** LZTFL1-related ciliopathy is an autosomal recessive ciliopathy within the Bardet-Biedl syndrome (BBS) spectrum.
- MedGen, drawing on OMIM, describes BBS17 as an autosomal recessive ciliopathy "characterized by retinitis pigmentosa, cognitive impairment, obesity, renal dysfunction, and hypogenitalism" ([MedGen](https://ncbi.nlm.nih.gov/medgen/811538)).
- A distinctive feature is **mesoaxial (insertional) polydactyly** with Y-shaped or fused metacarpals (Schaefer et al., 2014, PMID 23692385).
- The founding family also had **situs inversus** (Marion et al., 2012, PMID 22510444).

**Identifiers**

| Resource | ID | Retrieved? |
|---|---|---|
| MONDO | MONDO:1040046 (LZTFL1-related ciliopathy, given in the request). [NORD](https://rarediseases.org/mondo-disease/bardet-biedl-syndrome-17/) also has a MONDO-linked page for "Bardet-Biedl syndrome 17" | Partly (the ID itself was not checked) |
| OMIM (phenotype) | 615994 (BBS17) | Via MedGen |
| MedGen | C3714980 | Yes |
| NCBI Gene | 54585 (LZTFL1) | Yes ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/54585)) |
| Orphanet | BBS umbrella (ORPHA:110 is my assumption, not checked) | No |
| ICD-10 | Q87.89 is commonly used for BBS (not checked) | No |
| ICD-11 / MeSH | MeSH "Bardet-Biedl Syndrome" (D052356, not checked) | No |

**Synonyms:** Bardet-Biedl syndrome 17; BBS17; LZTFL1-related Bardet-Biedl syndrome.

**Source type:** The knowledge comes from individual-patient case reports aggregated into disease-level resources (OMIM/MedGen, GeneReviews, Genomics England PanelApp). There are no registry or EHR-derived cohorts.

## 2. Etiology

**Causal factor.** The disease is genetic. Biallelic loss-of-function (LoF) variants in LZTFL1 cause it; NCBI Gene summarizes that "nonsense mutations in this gene cause a form of Bardet-Biedl Syndrome" ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/54585)). Genomics England PanelApp rates LZTFL1 as a **Green** gene on its BBS panel, with inheritance "BIALLELIC, autosomal or pseudoautosomal". The curation cites "at least 3 variants identified in 2 unrelated cases" plus in vitro support ([PanelApp BBS](https://panelapp.genomicsengland.co.uk/panels/543/gene/LZTFL1)). LZTFL1 also appears on the PanelApp ophthalmological and renal ciliopathy panels ([722](https://panelapp.genomicsengland.co.uk/panels/722/gene/LZTFL1/), [725](https://panelapp.genomicsengland.co.uk/panels/725/gene/LZTFL1)).

**Genetic risk factors**
- **Consanguinity.** The founding family was studied by SNP-array homozygosity mapping (PMID 22510444). Nine of the 10 Pakistani BBS families in Nawaz et al. 2023 were consanguineous, including the LZTFL1 family "D" (PMID 37239474).
- **Modifier genes.** None are documented for LZTFL1-BBS.
- **A separate, non-BBS association to keep distinct.** The 3p21.31 locus is the strongest GWAS signal for severe COVID-19. Downes et al. (Nat Genet 2021; 53:1606–1615) nominated LZTFL1 as the effector gene, with rs17713054 as the likely causal variant. Its risk A allele is gain-of-function: it strengthens an enhancer that upregulates LZTFL1 and is implicated in airway epithelial–mesenchymal transition (EMT) ([Nature Genetics](https://www.nature.com/articles/s41588-021-00955-3); [Oxford summary](https://www.imm.ox.ac.uk/publication/1207475)). This is a common-variant susceptibility effect and is **not** part of the Mendelian ciliopathy. I did not retrieve its PMID.

**Environmental risk factors, protective factors and gene–environment interactions:** none are known. They are not applicable to this monogenic disorder beyond general BBS obesity management.

## 3. Phenotypes

The reported cases are:
- Marion 2012: one consanguineous family.
- Schaefer 2014: dizygotic twins.
- Nawaz 2023: one Pakistani family.
- Gana 2024: one boy, described as the seventh patient: "biallelic variants of the LZTFL1 gene have been reported only in six patients with BBS" (PMID 38801250).

Frequencies cannot be estimated reliably; the qualitative ones below come from these reports.

| Phenotype | HPO (suggested) | Type / onset / course | Evidence |
|---|---|---|---|
| Rod-cone dystrophy / retinitis pigmentosa | HP:0000510 Rod-cone dystrophy; HP:0000556 Retinal dystrophy | Sign; childhood onset; progressive | MedGen; twins (PMID 23692385); retinal degeneration in the KO mouse (PMID 27312011) |
| Mesoaxial (insertional) polydactyly, Y-shaped metacarpals | HP:0005732 (Mesoaxial polydactyly) / HP:0010442 Polydactyly | Congenital; stable. Reported in all early families ("Mesoaxial polydactyly is a major feature", PMID 23692385) | PMID 22510444, PMID 23692385 |
| Situs inversus totalis | HP:0001696 | Congenital (founding family) | PMID 22510444 |
| Obesity | HP:0001513 | Childhood onset | MedGen; Gana 2024 "classical BBS features"; mouse hyperphagic obesity (PMID 30423168) |
| Intellectual disability / cognitive impairment | HP:0001249; HP:0002342 (moderate) | Developmental; "more pronounced cognitive impairment" in the 2024 patient | PMID 23692385, PMID 38801250 |
| Renal dysfunction | HP:0000083 Renal insufficiency / HP:0000077 Abnormality of the kidney | Variable | PMID 23692385; MedGen |
| Hypogenitalism / hypogonadism | HP:0000135; HP:0003241 External genital hypoplasia | Pubertal | MedGen |
| Severe short stature | HP:0003510 | Childhood; proposed LZTFL1-associated feature that may differ from other BBS types | PMID 38801250 (low birth weight in KO mice, PMID 27312011) |
| Male infertility / asthenoteratozoospermia (inferred from mouse) | HP:0012207 Reduced sperm motility | Adult | Mouse only (PMID 34023333) |

**Quality of life:** no LZTFL1-specific data exist. In BBS generally, blindness, obesity-related morbidity and cognitive impairment drive disability ([GeneReviews NBK1363](https://www.ncbi.nlm.nih.gov/books/NBK1363/)).

## 4. Genetic/Molecular Information

**Gene.** LZTFL1 sits on chromosome 3p21.31 (NCBI Gene 54585; HGNC:6741 is my assumption, not checked). Its protein has coiled-coil and leucine-zipper domains; the zebrafish ortholog encodes 298 aa (PMID 31293455). It is a BBSome-interacting regulator, not a core BBSome subunit (PMID 22072986).

**Reported pathogenic variants** (transcript NM_020347)

| Variant | Type | Zygosity | Case | Evidence |
|---|---|---|---|---|
| c.402_406del, p.(Pro136Thrfs*5) | Frameshift | Homozygous | Founding family, BBS + situs inversus + insertional polydactyly | PMID 22510444. Quote: "No LZTFL1 transcript was found in the patient's fibroblasts and no protein could be detected." |
| c.260T>C, p.(Leu87Pro) + c.778G>T, p.(Glu260*) | Missense + nonsense | Compound heterozygous | Dizygotic twins | PMID 23692385. Quote: "A major decrease of LZTFL1 transcript and protein was observed in the patient's fibroblasts." |
| c.505A>T, p.(Lys169*) (NM_020347.4) | Nonsense | Homozygous | Pakistani family D | PMID 37239474 |
| Homozygous nonsense (HGVS not given in the abstract) | Nonsense | Homozygous | Italian boy | PMID 38801250 |

- **ACMG classification, ClinVar status and gnomAD allele frequencies:** not retrieved. I could not confirm ClinVar classifications for these variants.
- **Origin:** germline.
- **Functional consequence:** loss of function. The evidence is absent or reduced transcript and protein, consistent with nonsense-mediated decay.
- **Modifier genes, epigenetics and chromosomal abnormalities:** none reported. 3p21.31 deletions spanning LZTFL1 are not documented as a cause in the sources I retrieved.

## 5. Environmental Information

There are no environmental, lifestyle or infectious causes. Diet and physical activity influence the severity of obesity, as in BBS generally. Gene-specific data are not available.

## 6. Mechanism / Pathophysiology

**Causal chain**
1. Biallelic LZTFL1 LoF variants (frameshift or nonsense) **lead to** absent or markedly reduced LZTFL1 mRNA and protein. *Demonstrated in patient fibroblasts* (PMID 22510444, 23692385).
2. Loss of LZTFL1 **results in** dysregulated BBSome ciliary trafficking.
   - In mammalian cells, LZTFL1 restrains BBSome ciliary entry. "Reduction of LZTFL1 restores BBSome trafficking to cilia in BBS3 and BBS5 depleted cells" (Seo 2011, PMID 22072986).
   - In mouse kidney cells, LZTFL1 loss increases ciliary BBS9 (PMID 27312011).
   - In *Chlamydomonas*, LZTFL1 promotes BBS3/ARL6 basal-body targeting, stabilizes IFT25/27 and is needed for BBSome reassembly at the tip; there, "LZTFL1 dysfunction deprives the BBSome of ciliary presence" (PMID 34446551).
   - The direction of the effect differs between systems. The shared conclusion is that BBSome dynamics are disrupted.
3. Disrupted BBSome/IFT cargo trafficking **leads to** mislocalized ciliary membrane receptors.
   - **Branch A, Hedgehog signalling.** Smoothened (SMO) ciliary trafficking is altered (PMID 22072986). Patient fibroblasts show increased SMO and upregulated PTCH1 and GLI2, meaning the SHH pathway is activated (PMID 22510444). LZTFL1 is a negative Hh regulator (zebrafish, PMID 31293455). It is *inferred* that this causes the mesoaxial polydactyly through altered limb-bud patterning.
   - **Branch B, left–right patterning.** Situs inversus is inferred to stem from nodal cilia dysfunction. This is not demonstrated for LZTFL1.
   - **Branch C, photoreceptor connecting cilium.** Outer segments are shortened, the distal axoneme is enlarged and rhodopsin is mislocalized. This **leads to** photoreceptor apoptosis on TUNEL, that is, **retinal degeneration** (mouse, PMID 27312011).
   - **Branch D, hypothalamic leptin signalling.** Leptin-induced pStat3 is abolished in hypothalamic neurons while LepRb membrane levels are normal. This **leads to** leptin resistance and hyperphagia, and then **obesity** ("caused by the loss of Lztfl1 in the brain but not in the adipocytes", PMID 30423168).
   - **Branch E, sperm flagellum.** IFT27 is reduced, which **leads to** astheno-teratozoospermia and reduced male fertility (mouse, PMID 34023333).
4. Together these tissue-level defects **result in** the BBS clinical syndrome. Short stature (PMID 38801250) is mechanistically unexplained; low birth weight in KO mice points to a growth role.

**Further detail**
- **Pathways:** BBSome-mediated ciliary trafficking; IFT-B (IFT25/IFT27); Hedgehog/SMO; leptin–JAK2–STAT3. LZTFL1-interacting proteins involved in actin dynamics have also been proposed (PMID 30423168).
- **Suggested GO terms:**
  - Biological process: cilium assembly (GO:0060271); protein localization to cilium (GO:0061512); negative regulation of smoothened signaling pathway (GO:0045879); intraciliary transport (GO:0042073); photoreceptor cell outer segment organization (GO:0035845); leptin-mediated signaling pathway (GO:0033210); spermatogenesis (GO:0007283).
  - Cellular component: BBSome (GO:0034464); ciliary basal body (GO:0036064); cilium (GO:0005929); photoreceptor connecting cilium (GO:0032391).
- **Suggested CL terms:** rod photoreceptor cell (CL:0000604); hypothalamic neuron (CL:0012001, unchecked); kidney epithelial cell (CL:0002518); spermatid (CL:0000018); fibroblast (CL:0000057).
- **Metabolism and immune involvement:** hyperphagic obesity without altered energy expenditure (mouse, PMID 30423168). There is no immune involvement in the ciliopathy (immune involvement is relevant only to the separate COVID-19 locus, which acts through epithelial EMT).
- **Omics, single-cell, spatial and CRISPR screens:** none are specific to LZTFL1-BBS. Downes 2021 used spatial transcriptomics, but in COVID-19 lung.

## 7. Anatomical Structures Affected

- **Primary:** retina (UBERON:0000966), especially the photoreceptor layer; hand and foot autopods (UBERON:0002398 manus, UBERON:0002387 pes) through mesoaxial polydactyly; brain and hypothalamus (UBERON:0001898); kidney (UBERON:0002113); gonads and genitalia (UBERON:0000991).
- **Developmental and laterality:** thoracic and abdominal viscera in situs inversus.
- **Subcellular:** primary cilium, basal body and connecting cilium (GO terms as in Section 6).
- **Lateralization:** retinal disease and polydactyly are bilateral (the twins had "bilateral insertional polydactyly", PMID 23692385).

## 8. Temporal Development

- **Onset:** congenital for polydactyly and situs; childhood for obesity, short stature and visual symptoms (inferred from the general BBS pattern).
- **Course:** retinal disease is progressive; cognitive impairment is static and developmental; renal course is variable.
- **Staging:** no natural-history data specific to LZTFL1 exist.
- **Critical periods:** early-childhood weight management and early low-vision support (general BBS guidance, [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1363/)).

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive. Penetrance appears complete in the reported cases, with variable expressivity: situs inversus occurred in only one family, and severe ID and short stature in the 2024 case. GeneReviews notes that some biallelic carriers of BBS-gene variants do not meet clinical criteria ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1363/)).
- **Prevalence:** ultra-rare. About 7–8 published patients are known: French families in the Dollfus group reports (I assumed their origin from authorship and did not check it), plus Pakistani and Italian cases.
- **Founder effects, carrier frequency and sex ratio:** not available. Anticipation and germline mosaicism are not reported.

## 10. Diagnostics

- **Clinical diagnosis:** BBS clinical criteria, with primary features (rod-cone dystrophy, polydactyly, obesity, learning disability, hypogonadism, renal anomalies), as summarized in [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1363/). Mesoaxial polydactyly with Y-shaped metacarpals on hand X-ray should prompt a look at LZTFL1 (PMID 23692385).
- **Genetic testing:**
  - Multigene BBS/ciliopathy panels that include LZTFL1 (PanelApp Green), or exome or genome sequencing.
  - All the reported cases were found by WES. The founding case used SNP homozygosity mapping plus exome sequencing (PMID 22510444, 37239474).
  - CMA could detect deletions but none have been reported. Karyotype, FISH, mtDNA and repeat testing are not applicable.
- **Supporting tests:** ERG and fundus imaging; renal ultrasound and function tests; echocardiography or abdominal imaging for situs; limb radiographs.
- **Functional or omics tests:** RT-qPCR and western blot of fibroblasts showing absent LZTFL1 (research use, PMID 22510444).
- **Differential diagnosis:** other BBS genes (about 20+ loci); Alström syndrome (no polydactyly; hearing loss and cardiomyopathy); McKusick-Kaufman syndrome (MKKS); Joubert and Meckel syndromes; primary ciliary dyskinesia for situs inversus (PCD involves motile-cilia respiratory disease).
- **Screening:** cascade carrier testing in families; prenatal or preimplantation testing once familial variants are known.

## 11. Outcome/Prognosis

There are no survival, mortality or QoL data specific to LZTFL1. By analogy with BBS, the main morbidities are progressive vision loss, obesity and metabolic complications, and kidney disease, which is the major driver of mortality in BBS ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1363/)). The 2024 case suggests that some LZTFL1 genotypes come with severe short stature and moderate ID (PMID 38801250); this is a possible prognostic signal but has not been validated.

## 12. Treatment

There is no LZTFL1-specific therapy, and the evidence below is general BBS evidence that I did not retrieve in this session.
- **Pharmacotherapy:** setmelanotide, an MC4R agonist (NCIT term for setmelanotide, not checked), is FDA-approved for obesity in BBS generally. It acts downstream of the leptin–melanocortin pathway. That pathway is disrupted in Lztfl1⁻/⁻ mice (PMID 30423168), which gives it a *mechanistic* rationale, but no LZTFL1 patient data exist.
- **Gene therapy, ASOs and cell therapy:** none. I found no LZTFL1 trials.
- **Supportive care:**
  - Weight and diet management.
  - Low-vision rehabilitation.
  - Renal monitoring, and dialysis or transplant if needed.
  - Hormone replacement for hypogonadism.
  - Surgical excision of extra digits.
  - Special education, plus growth evaluation for short stature.
  - Suggested NCIT concepts: Dietary Intervention; Hormone Therapy; Kidney Transplantation; Surgical Procedure (exact NCIT codes not checked).
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary prevention:** genetic counselling. Recurrence risk is 25% for carrier couples. Carrier testing for relatives, and prenatal or preimplantation diagnosis, are options.
- **Secondary prevention:** early molecular diagnosis in infants with polydactyly.
- **Tertiary prevention:** surveillance for retinal, renal, metabolic and endocrine problems.
- **Vaccines and public health measures:** not applicable.

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** I found no LZTFL1 disease in animals; OMIA was not searched successfully.
- **Orthologs and conservation:** mouse *Lztfl1*, zebrafish *lztfl1* (PMID 31293455) and *Chlamydomonas reinhardtii* LZTFL1 (PMID 34446551). The role in BBSome trafficking is conserved from algae to mammals. NCBI ortholog Gene IDs were not retrieved.
- **Zoonotic potential:** none.

## 15. Model Organisms

| Model | Findings | Recapitulation |
|---|---|---|
| Mouse *Lztfl1* KO (Jiang 2016, PMID 27312011) | "Born with low birth weight", catch-up by 10 weeks, then excess weight; retinal degeneration with shortened outer segments, mislocalized rhodopsin and photoreceptor apoptosis | Obesity, retinal dystrophy and growth: good |
| Mouse global *Lztfl1*⁻/⁻ and floxed *Lztfl1*ᶠ/ᶠ (Wei 2018, PMID 30423168) | Hyperphagic obesity, leptin resistance, obesity driven by brain loss, longer cilia in MEFs | Obesity: good. Conditional line allows tissue dissection |
| Mouse KO testis (Huang 2021, PMID 34023333) | Reduced male fertility, astheno-teratozoospermia, reduced IFT27 | Hypogonadism and infertility aspect |
| Zebrafish (PMID 31293455) | Characterization only; LZTFL1 is a negative Hh regulator | Limited (no mutant phenotype reported in the abstract) |
| *Chlamydomonas* (PMID 34446551) | BBSome basal-body recruitment and tip reassembly defects; phototaxis defect | Mechanistic only |
| Cellular: patient fibroblasts (PMID 22510444, 23692385); RPE/IMCD3-type cell knockdown (Seo 2011, PMID 22072986; exact cell lines not stated in the abstract) | Absent protein; SHH pathway activation; BBSome trafficking rescue | Molecular |

**Limitations of the models:**
- Mesoaxial polydactyly and situs inversus have not been reported in the mouse models.
- Renal phenotypes are under-characterized.

**Resources:** MGI (*Lztfl1*), IMPC and ZFIN entries were not retrieved.

---

### Key sources
- Marion V et al. *J Med Genet* 2012;49:317–21. PMID 22510444 ([full text](https://jmg.bmj.com/content/jmedgenet/early/2012/04/16/jmedgenet-2012-100737.full.pdf))
- Schaefer E et al. *Clin Genet* 2014;85:476–81. PMID 23692385
- Nawaz H et al. *Genes (Basel)* 2023. PMID 37239474
- Gana S et al. *Am J Med Genet A* 2024;194:e63723. PMID 38801250
- Seo S et al. *PLoS Genet* 2011;7:e1002358. PMID 22072986 ([PMC3207910](https://pmc.ncbi.nlm.nih.gov/articles/PMC3207910))
- Jiang J et al. *J Genet Genomics* 2016;43:381–91. PMID 27312011 ([PMC4925197](https://pmc.ncbi.nlm.nih.gov/articles/PMC4925197))
- Wei Q et al. *J Mol Cell Biol* 2018. PMID 30423168
- Wei Q et al. *Front Physiol* 2019. PMID 31293455
- Sun WY et al. *PNAS* 2021. PMID 34446551
- Huang Q et al. *Dev Biol* 2021. PMID 34023333
- Downes DJ et al. *Nat Genet* 2021;53:1606–15 ([link](https://www.nature.com/articles/s41588-021-00955-3)); this is the COVID-19 locus, not the ciliopathy
- [MedGen C3714980](https://ncbi.nlm.nih.gov/medgen/811538); [NCBI Gene 54585](https://www.ncbi.nlm.nih.gov/gene/54585); [PanelApp BBS](https://panelapp.genomicsengland.co.uk/panels/543/gene/LZTFL1); [GeneReviews BBS overview NBK1363](https://www.ncbi.nlm.nih.gov/books/NBK1363/) (PMID 20301537); [NORD BBS17](https://rarediseases.org/mondo-disease/bardet-biedl-syndrome-17/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20301537` (1 mention) - Bardet-Biedl Syndrome Overview.
  - shared terms: syndrome, family

Weighed against this report's own most characteristic terms: `lztfl1`, `bbs`, `obesity`, `gene`, `polydactyly`, `situs`, `disease`, `renal`, `inversus`, `variant`, `patient`, `ciliopathy`, `mesoaxial`, `ncbi`, `retinal`, `stature`, `syndrome`, `family`, `biallelic`, `loss`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0034464` (1 mention) - the report calls it "Cellular component: BBSome"; GO calls it **BBSome**
- `CL:0000604` (1 mention) - the report calls it "Suggested CL terms:** rod photoreceptor cell"; CL calls it **retinal rod cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0060271` (1 mention) - the report calls it "Biological process: cilium assembly"; GO calls it **cilium assembly**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:1040046` - called "LZTFL1-related ciliopathy", "LZTFL1-related ciliopathy, given in the request"

### Terms the ontology service could not be reached for

9 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MONDO:1040046` (3 mentions)
- `HP:0000510` (1 mention)
- `HP:0005732` (1 mention)
- `HP:0001696` (1 mention)
- `HP:0001513` (1 mention)
- `HP:0002342` (1 mention)
- `HP:0000083` (1 mention)
- `HP:0000135` (1 mention)
- `UBERON:0000966` (1 mention)

### Terms whose obsolescence could not be checked

7 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0010442` (1 mention)
- `HP:0012207` (1 mention)
- `GO:0032391` (1 mention)
- `CL:0000604` (1 mention)
- `CL:0002518` (1 mention)
- `CL:0000018` (1 mention)
- `CL:0000057` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.