---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-04T17:46:11.514523'
end_time: '2026-11-04T17:52:55.638183'
duration_seconds: 404.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Periventricular Nodular Heterotopia 2
  mondo_id: MONDO:0011966
  category: Mendelian
  causal_genes: ARFGEF2
  omim_id: OMIM:608097
  synonyms: PVNH2; ARFGEF2-related periventricular nodular heterotopia; Autosomal
    recessive periventricular heterotopia with microcephaly
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
  num_turns: 29
  total_cost_usd: 2.788892699999999
  session_id: 64fbaae1-f4b6-4b72-9c4f-cf88620fa618
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42200925
  relevance_assessed: 21
  on_topic: 14
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 67
  verified: 65
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 15
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0025430
    reported_labels:
    - verify
    ontology_label: High-pitched cry
  - term_id: UBERON:0000948
    reported_labels:
    - Secondary:** heart, through cardiomyopathy
    ontology_label: heart
  - term_id: NCIT:C15986
    reported_labels:
    - symptomatic
    ontology_label: Pharmacotherapy
  - term_id: NCIT:C15240
    reported_labels:
    - AR recurrence risk of 25%; prenatal or preimplantation testing
    ontology_label: Genetic Counseling
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Periventricular Nodular Heterotopia 2
- **MONDO ID:** MONDO:0011966 (if available)
- **Causal gene(s):** ARFGEF2
- **OMIM:** OMIM:608097
- **Synonyms:** PVNH2; ARFGEF2-related periventricular nodular heterotopia; Autosomal recessive periventricular heterotopia with microcephaly
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Periventricular Nodular Heterotopia 2** covering all of the
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

I'm looking up the cached ARFGEF2 papers, then I'll search the literature for anything still missing.

I have the main ARFGEF2 case literature. Next I'm getting the abstracts of the key papers so I can quote them.

# Research Report: Periventricular Nodular Heterotopia 2 (PVNH2; MONDO:0011966; OMIM 608097)

**Causal gene: *ARFGEF2*** (`hgnc:15853`; OMIM gene *605371; chromosome 20q13). *ARFGEF2* encodes BIG2, the brefeldin A-inhibited guanine nucleotide-exchange factor 2. PVNH2 is the disorder MONDO labels "periventricular heterotopia with microcephaly, autosomal recessive" (ARPHM). It is caused by biallelic, mostly truncating *ARFGEF2* variants. It is a different disease from X-linked dominant *FLNA*-related PVNH (PVNH1). The serial-number name does not create a gene conflict here: MONDO, OMIM 608097 and the literature all point to *ARFGEF2*.

**How this was researched:**
- Primary literature was found through PubMed E-utilities and the Europe PMC REST API.
- Some abstracts were read from the repository's `references_cache/`. The full text was read only for the 2026 review (PMID:42200925).
- Quoted snippets were copied from abstracts or that review's full text. Quotes taken through Europe PMC should be checked against `just fetch-reference` output before they are used as evidence `snippet:` values.
- The search tools hit rate limits, so a few identifiers are marked **unverified**.

---

## 1. Disease Information

**Overview.** PVNH2 is a rare autosomal recessive malformation of cortical development. Its defining features are:
- bilateral, often near-contiguous periventricular nodular heterotopia (PVNH), meaning grey-matter nodules lining the lateral ventricles;
- **congenital or, more typically, progressive (acquired) microcephaly**;
- severe developmental delay with hypotonia and tetraparesis;
- frequent early-onset epilepsy, often infantile spasms or West syndrome;
- frequent dyskinetic or dystonic movement disorders.

A 2026 review counted 21 published patients (Andreoli et al., PMID:42200925):

> "Among recessive forms, ARFGEF2-related disorder is uniquely characterised by the association of diffuse PVNH and progressive microcephaly."

Defining paper (Sheen et al. 2004, *Nat Genet*, PMID:14647276):

> "an autosomal recessive condition characterized by microcephaly and periventricular heterotopia maps to chromosome 20 and is caused by mutations in the gene ADP-ribosylation factor guanine nucleotide-exchange factor-2 (ARFGEF2)."

The clinical entity was first described a year earlier (Sheen et al. 2003, *Neurology*, "Autosomal recessive form of periventricular heterotopia", PMID:12682315).

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0011966, "periventricular heterotopia with microcephaly, autosomal recessive" | in KB |
| OMIM | #608097 (disease); *605371 (ARFGEF2) | confirmed |
| Orphanet | ORPHA:2149 (via the ClinVar condition record) | **unverified on orpha.net**; no `ORPHA_2149` cache file exists |
| MedGen | C1842563 | from search results |
| GenCC | ARFGEF2 → ARPHM: **Definitive** | GenCC page; a ClinGen `CGGV:` record was not located |
| ICD-10 | Q04.8 (other specified congenital malformations of brain), by convention for heterotopia | not disease-specific |
| MeSH | Periventricular Nodular Heterotopia (D054220) | parent concept |

**Synonyms:** PVNH2; ARPHM; ARFGEF2-related periventricular nodular heterotopia; autosomal recessive periventricular heterotopia with microcephaly; ARFGEF2-related disorder.

**Data provenance:** all knowledge comes from aggregated case reports and small family series, about 13 families, 21 to roughly 25 individuals as of 2026. There are no EHR cohorts or registries.

## 2. Etiology

- **Cause:** biallelic germline loss-of-function variants in *ARFGEF2*. Nearly all patients are homozygous (20/21) and born to consanguineous parents (20/21) (PMID:42200925).
- **Genetic risk factors:**
  - Parental consanguinity is the dominant risk factor.
  - Founder or recurrent alleles are known: c.242_249delins7 in Turkish families, and c.1958+1G>A in Palestinian and Saudi families (see §4).
- **Modifier genes:** none established. Andreoli et al. propose that the phenotypic variability "may reflect modifying factors (such as residual expression, genetic background, or environmental influences)", but this is speculation.
- **Common-variant link:** an early-life head-circumference GWAS meta-analysis (Vogelezang et al. 2022, PMID:35659227) is cited by Andreoli et al. as identifying *ARFGEF2* as a head-size determinant. **Unverified:** I did not confirm ARFGEF2 in that paper's results.
- **Environmental, protective and gene-environment factors:** none reported. Brefeldin A pharmacologically phenocopies BIG2 inhibition in vitro, but it is not a human exposure.

## 3. Phenotypes

Frequencies come from the 21-patient review table (PMID:42200925) unless stated otherwise.

| Phenotype | Suggested HPO | Frequency | Onset / course | Key source |
|---|---|---|---|---|
| Periventricular nodular heterotopia (bilateral, often near-contiguous or diffuse) | HP:0032388 | 21/21 | congenital (prenatal) | PMID:14647276, 42200925 |
| Progressive (acquired) microcephaly; HC −2 to −5 SD after 6 months, often normal at birth | HP:0000253 Progressive microcephaly (or HP:0005484 Postnatal microcephaly); HP:0000252 | ~20/21 | infancy, progressive | PMID:25160555, 42200925 |
| Severe global developmental delay | HP:0011344 / HP:0001263 | 21/21 | infancy | PMID:42200925 |
| Hypotonia (axial) | HP:0001252 / HP:0008936 | 21/21 | infancy | PMID:42200925 |
| Spastic or dystonic tetraparesis / quadriplegia | HP:0002273 Tetraparesis | 21/21 | infancy | PMID:23755938 |
| Epilepsy (early onset, often drug-resistant) | HP:0001250; HP:0002373 | 13/21 (~62%) | 6–18 months | PMID:42200925 |
| Infantile spasms / West syndrome, evolving to Lennox-Gastaut | HP:0012469; HP:0012469 + HP:0002521 Hypsarrhythmia | 6/21 (5 Banne family + Andreoli case) | before age 1 | PMID:23812912 |
| Hypsarrhythmia | HP:0002521 | 7/21 | infancy | PMID:42200925 |
| Movement disorder: dystonia, chorea, athetosis, dyskinesia | HP:0001332 Dystonia; HP:0002072 Chorea; HP:0002305 Athetosis | 10/21 (~48%) | infancy/childhood | PMID:19384555, 25160555 |
| Thin or hypoplastic corpus callosum | HP:0002079 | 14/21 | congenital | PMID:23812912 |
| Cerebral / cortico-subcortical atrophy | HP:0002059 | 11/21 | progressive | PMID:23755938 |
| Basal ganglia (putaminal) signal abnormality or atrophy | HP:0012751 Abnormal basal ganglia MRI signal intensity (verify) | 9/21 | childhood | PMID:19384555 |
| Hippocampal atrophy | HP:0025430 (verify) | several | — | PMID:23755938 |
| Delayed myelination | HP:0012448 | 3/21 | infancy | PMID:42200925 |
| Ventriculomegaly | HP:0002119 | case-level | — | PMID:42200925 |
| Growth impairment / failure to thrive | HP:0001510 / HP:0001508 | 13/21 | infancy | PMID:42200925 |
| Feeding difficulties, dysphagia, gastrostomy | HP:0011968; HP:0002015 | 10/21 | infancy | PMID:42200925 |
| Recurrent respiratory infections, often aspiration | HP:0002205; HP:0002835 Aspiration | 8/21 | childhood | PMID:42200925 |
| Cardiomyopathy: obstructive / hypertrophic; LV non-compaction | HP:0001638; HP:0011664 LV noncompaction | 2/21 | childhood | PMID:23755938, 26126837 |
| Vomiting, drooling | HP:0002013; HP:0002307 | 4–5/21 | — | PMID:42200925 |
| Early death (5–13 years in 4 reported patients) | — | 4/21 with known age | childhood | PMID:42200925 |

Note that `HP:` identifiers marked "verify", and all the others, should be confirmed with `runoak` or the cache before binding. They were not looked up in this session.

**Supporting quotes:**
- Tanyalçin et al. 2013, PMID:23755938: "The clinical phenotype was characterized by dystonic quadriplegia, marked developmental delay"; "Brain MRI revealed bilateral periventricular heterotopia, small corpus callosum, cerebral and hippocampal atrophy".
- de Wit et al. 2009, PMID:19384555: "The brain MRI shows bilateral hyperintensity of the putamen, BPNH, and generalized atrophy."
- Yilmaz et al. 2016, PMID:26126837: "Her echocardiographic examination revealed left ventricular non-compaction cardiomyopathy."
- Bardón-Cancho et al. 2014, PMID:25160555: "He exhibited axial hypotonia with a prominent dystonic-athetoid component."

**Phenotype expansion.** Naqvi et al. 2026 (PMID:42852362) report a family whose affected sibs "do not have the typical ARPHM symptoms of seizures, hypsarrhythmia, or microcephaly." Microcephaly and epilepsy are therefore not obligatory.

**Quality of life.** No formal QoL instrument data exist. The impact is profound: non-ambulatory, minimally verbal (Griffiths DQ <20 in the Andreoli case), with gastrostomy dependence and frequent hospitalisations.

## 4. Genetic / Molecular Information

- **Gene:** *ARFGEF2* (BIG2, ~1,785 aa, >200 kDa). It has a Sec7 ARF-GEF domain, an N-terminal DCB/HUS region that binds Exo70, AKAP motifs that bind PKA, and a C-terminal GABA-A receptor β-subunit interaction (review in PMID:25097827). Reference transcript: NM_006420.
- **Variant spectrum.** All published variants are germline and biallelic. Every variant except one missense is truncating or splice-altering, which supports a loss-of-function (LoF) mechanism.

| Variant (NM_006420) | Type | Zygosity / population | Ref |
|---|---|---|---|
| c.625G>A p.(Glu209Lys) | missense | homozygous; Turkish | Sheen 2004, PMID:14647276 |
| c.242_249delins7 p.(Pro81fs) | frameshift | homozygous; Turkish, recurrent in 3 families | PMID:14647276, 23755938 |
| c.2031_2038dup + c.3798_3802del | frameshift ×2 | compound heterozygous; Dutch, non-consanguineous | de Wit 2009, PMID:19384555 |
| c.1958+1G>A (reported as c.1957+1?) | splice donor | homozygous; Palestinian (5 patients), Saudi | Banne 2013, PMID:23812912; Alojair 2018 |
| c.388C>T (p.Arg130*) | nonsense, exon 4 | homozygous | Bardón-Cancho 2014, PMID:25160555 |
| c.5126G>A p.(Trp1709*) | nonsense | homozygous; Turkish | Yilmaz 2016, PMID:26126837 |
| c.3974G>A p.(Trp1325*) | nonsense | homozygous; Saudi | Al Neghery 2018 |
| c.2776C>T p.(Arg926*) | nonsense, exon 20 | homozygous; Pakistani; ACMG pathogenic (PVS1, PM2, PP4, PP1) | Andreoli 2026, PMID:42200925 |
| c.5181+1G>T | splice; minigene assay shows exon 38 skipping, 118-bp deletion | homozygous | Liu 2026, PMID:42255913 |
| c.4455-1G>A | splice acceptor; exon 33 skipping predicted | homozygous; Pakistani | Naqvi 2026, PMID:42852362 |

The Andreoli table writes the Banne variant as "c.1958 (+1) G > A". The original abstract gives no HGVS, so confirm the variant against Banne et al.'s full text or ClinVar.

- **Classification and frequency:**
  - Most of these variants are absent from gnomAD (stated, for example, for p.Arg926*).
  - ARFGEF2 is LoF-intolerant in population data; check the current gnomAD pLI/LOEUF values directly.
  - Carriers are asymptomatic: obligate heterozygous parents are healthy, and heterozygous *Arfgef2* gene-trap mice are normal (PMID:20857375).
- **Functional consequence:** LoF. "No strong genotype–phenotype correlation emerged… suggesting that complete loss of function represents the critical pathogenic threshold" (PMID:42200925). The p.Glu209Lys missense lies in the N-terminal DCB/HUS region. Sheen et al. reported it alters subcellular localization, but I did not confirm this from the abstract.
- **Epigenetics and chromosomal abnormalities:** none reported for PVNH2. Copy-number PVNH, such as 5q14.3–q15 (PMID:19073947) or 6q terminal deletion, belongs to other loci and should not be confused with this disease.

## 5. Environmental Information

There are no environmental, lifestyle or infectious contributors. Not applicable.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *ARFGEF2* LoF variants** lead to absent BIG2 protein, through nonsense-mediated decay or splice disruption (human genetic evidence: PMID:42200925, 42255913).
2. **Loss of BIG2 Sec7 GEF activity** results in reduced GDP→GTP exchange on class I ARFs (ARF1, ARF3) at the trans-Golgi network (TGN) and recycling endosomes (PMID:14647276, 25097827).
3. **Impaired TGN-to-plasma-membrane vesicle trafficking and Arf1-dependent peripheral endocytosis** leads to mislocalized adhesion and junction cargo. E-cadherin and β-catenin are retained in the Golgi (PMID:14647276), and transport of filamin A (FLNA) to the cell surface is reduced (PMID:16320251; in vitro, SH-SY5Y cells).
4. **This branches into two arms:**
   - **4a. Proliferative arm.** Reduced neural progenitor (radial glial) proliferation lowers neuron output, which **results in microcephaly**, characteristically progressive. Evidence: BFA or dominant-negative BIG2 "decreases cell proliferation in vitro, suggesting a cell-autonomous regulation of neural expansion" (PMID:14647276). The link to human microcephaly is inferred.
   - **4b. Adhesion / neuroependymal arm.** Loss of cell-cell (cadherin/β-catenin) and cell-ECM (integrin/paxillin, focal adhesion) membrane complexes leads to **disrupted neuroependymal integrity** (denudation of the ventricular lining) and loss of radial glial scaffold anchoring (PMID:18996916, mouse and human post-mortem tissue; PMID:24089482).
5. **FLNA-BIG2 crosstalk** (modifying step):
   - BIG2 loss raises phospho-FlnA (Ser2152), which reduces FlnA-actin binding and alters focal-adhesion size and number, which in turn impairs neuronal motility (PMID:22956851, mouse).
   - In the reverse direction, phospho-FlnA relocalizes BIG2 from the Golgi to the membrane to activate Arf1 (PMID:24089482).
   - Together this places PVNH2 and *FLNA*-PVNH on a shared endocytic pathway (PMID:24709996, 25097827).
6. **Failure of early neurons to leave the ventricular zone** leads to periventricular nodules made **mainly of later-born neurons**, which **results in PVNH** (PMID:18996916). The apical-abscission model, in which delayed detachment of the neuron from the ventricular surface is the cause, is a hypothesis (PMID:25097827).
7. **Downstream network effects:**
   - Heterotopic nodules plus cortical malformation lead to abnormal cortico-heterotopic connectivity, which results in **early-onset, drug-resistant epilepsy** and severe developmental delay (inferred).
   - A parallel branch: putaminal and basal-ganglia vulnerability, attributed to high ARFGEF2 expression in the ganglionic eminences, leads to **dystonia and chorea** (hypothesis: PMID:19384555, 42200925).
   - Progressive cerebral and hippocampal atrophy suggests a postnatal, possibly degenerative component (inferred from serial MRI).
8. **Extra-CNS branch:** cardiomyopathy and failure to thrive. The mechanism is unknown. Feeding problems are partly secondary to bulbar dysfunction, which causes aspiration and recurrent infections.

**Key quotes:**
- Sheen 2004, PMID:14647276: "Inhibition of BIG2 also disturbed the intracellular localization of such molecules as E-cadherin and beta-catenin by preventing their transport from the Golgi apparatus to the cell surface."
- Ferland 2009, PMID:18996916: "periventricular nodules were primarily composed of later-born neurons, and that the neuroependyma was disrupted in all PH cases." The same paper concludes that "PH formation arises from a final common pathway involving disruption of vesicle trafficking, leading to impaired cell adhesion and loss of neuroependymal integrity."
- Zhang 2013, PMID:24089482: "Loss of FlnA phosphorylation or Big2 function impairs Arf1-dependent vesicle trafficking at the periphery, and Arf1 is required for maintenance of cell-cell junction connectivity and focal adhesion assembly."
- Lu 2006, PMID:16320251: "BIG2 protein immunoreactivity was most strongly localized to the neural progenitors".

**Suggested GO terms:**
- guanyl-nucleotide exchange factor activity (GO:0005085)
- ARF protein signal transduction (GO:0032011)
- Golgi vesicle transport (GO:0048193)
- endocytosis (GO:0006897)
- neural precursor cell proliferation (GO:0061351)
- neuron migration (GO:0001764)
- cell-cell adhesion (GO:0098609)
- focal adhesion assembly (GO:0048041)
- cerebral cortex development (GO:0021987)

**Suggested CL terms:** radial glial cell (CL:0000681), neural progenitor cell (CL:0011020), neuron (CL:0000540), ependymal cell (CL:0000065).

All GO and CL IDs above must be checked with a lookup before binding.

**Molecular profiling:** no transcriptomic, proteomic, metabolomic, single-cell or patient-iPSC data have been published for PVNH2.

**KB link:** the repository module `kb/modules/apical_neuroependyma_integrity_failure.yaml` already references ARFGEF2 and is the natural `conforms_to` target for step 4b.

## 7. Anatomical Structures Affected

- **Primary:**
  - cerebral cortex (UBERON:0000956)
  - lateral ventricle ependyma / ventricular zone (UBERON:0002149 ependyma; UBERON:0004040 ventricular zone, verify)
  - periventricular white matter
  - corpus callosum (UBERON:0002336)
  - putamen / basal ganglia (UBERON:0001874; UBERON:0002420)
  - hippocampus (UBERON:0002421)
- **Secondary:** heart, through cardiomyopathy (UBERON:0000948); gastrointestinal and bulbar function; lungs, through aspiration.
- **Subcellular (GO CC):** trans-Golgi network (GO:0005802), recycling endosome (GO:0055037), plasma membrane, and adherens junction (GO:0005912).
- **Lateralization:** bilateral and symmetric in nearly all patients; one patient had focal PVNH.

## 8. Temporal Development

- **Onset:** prenatal malformation. Head circumference is often normal at birth, then microcephaly develops postnatally. Developmental delay is evident by 3–6 months, and seizures begin at 6–18 months.
- **Course:** lifelong and static-to-progressive. Microcephaly, cerebral and hippocampal atrophy, dysphagia and drug-resistant epilepsy progress, and motor regression has been reported (PMID:42200925).
- **Remission:** none.
- **Critical period:** corticogenesis, in the first and second trimesters, is when the malformation forms. Early infancy is the window for seizure control and nutritional and respiratory surveillance.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007). Penetrance in biallelic individuals appears complete, with variable expressivity (PMID:42852362).
- **No anticipation and no mosaicism reported.**
- **Prevalence:** unknown; ultra-rare, with about 13 families and roughly 25 patients reported worldwide. A suitable prevalence encoding is `CASES_IN_LITERATURE` with `ULTRA_RARE`.
- **Populations:** Turkish, Palestinian, Saudi, Pakistani and Dutch families, and one Chinese family (PMID:42255913, origin not confirmed). Recurrent alleles occur in Turkish families (c.242_249delins7) and in Palestinian and Saudi families (c.1958+1G>A).
- **Consanguinity:** 20/21 patients. There is no sex predominance.
- **Carrier frequency:** not established.

## 10. Diagnostics

- **Imaging (key):**
  - Brain MRI shows bilateral contiguous PVNH with a thin corpus callosum, cortico-subcortical atrophy, putaminal T2 hyperintensity or atrophy, hippocampal atrophy and delayed myelination.
  - The combination of **PVNH, progressive microcephaly and basal-ganglia signal change with dyskinesia** strongly suggests ARFGEF2 (PMID:25160555, 23755938).
- **EEG:** hypsarrhythmia, slow background and multifocal discharges. An unusual asynchronous 14–15 Hz "comb-like" fast activity was reported in one case (PMID:42200925).
- **Cardiac:** echocardiography to screen for cardiomyopathy or LV non-compaction (PMID:26126837).
- **Genetic testing:**
  - Exome sequencing, or a malformation-of-cortical-development / developmental and epileptic encephalopathy panel that includes *ARFGEF2*, is the standard approach. Most recent diagnoses came from homozygosity mapping plus exome sequencing or a large panel.
  - Genome sequencing helps with deep-intronic or splice variants.
  - RNA or minigene studies can confirm splice variants (PMID:42255913).
  - Chromosomal microarray is useful for excluding CNV-related PVNH.
- **Biomarkers or laboratory tests:** none specific.
- **Differential diagnosis:**
  - *FLNA* PVNH: X-linked dominant, female predominance, usually normocephalic, often normal intellect (PMID:16684786).
  - *MAP1B*, *NEDD4L*, *DCHS1*/*FAT4* (Van Maldergem syndrome), *ERMARD*, *ARF1*/*ARF3* Golgipathies, and 5q14.3 or 6q deletions.
  - Microcephaly–lissencephaly spectrum disorders and congenital infection.
- **Screening:** there is no newborn screening. Carrier and cascade testing is possible in consanguineous families.

## 11. Outcome / Prognosis

- Every reported patient has severe developmental disability. Most are non-ambulatory and non-verbal.
- **Mortality:** 4 deaths at ages 5 y 11 m to 13 y among patients with known follow-up (PMID:42200925). Causes include respiratory infection and cardiac disease. Life expectancy is reduced, but no survival data exist.
- **Poor prognostic indicators (qualitative):** refractory epilepsy, aspiration and cardiomyopathy.
- **Prognostic biomarkers:** none.

## 12. Treatment

There is no disease-modifying therapy, and there are no clinical trials for ARFGEF2 or PVNH2 on ClinicalTrials.gov as far as this search found.

| Intervention | Notes | Suggested NCIT |
|---|---|---|
| Antiseizure medication: vigabatrin for spasms (partial response); valproate (one responder); levetiracetam, clobazam, topiramate (often refractory) | phenotype-driven (PMID:42200925) | Pharmacotherapy NCIT:C15986 + `therapeutic_agent` CHEBI terms |
| Gastrostomy / nutritional support | 10/21 have feeding problems | NCIT:C15329 Surgical Procedure (verify a gastrostomy term) |
| Management of dystonia / movement disorder | symptomatic | NCIT:C15986 |
| Cardiology surveillance and heart-failure management | recommended because of cardiomyopathy (PMID:26126837) | Supportive Care NCIT:C15747 |
| Physical, occupational and speech therapy | rehabilitative | NCIT:C15302; NCIT:C121351; NCIT:C159273 |
| Genetic counseling | AR recurrence risk of 25%; prenatal or preimplantation testing | NCIT:C15240 |

Most patients in the table did not receive steroids or ACTH for spasms, because of their fragile clinical state. Pharmacogenomic considerations are none specific to this disease.

## 13. Prevention

- **Primary prevention:** carrier testing in consanguineous kindreds; prenatal diagnosis or preimplantation genetic testing once the familial variants are known (PMID:42200925).
- **Secondary prevention:** early genetic diagnosis to guide surveillance.
- **Tertiary prevention:** cardiac screening, aspiration prevention (gastrostomy) and seizure control.
- **Not applicable:** vaccines and public-health measures.

## 14. Other Species / Natural Disease

- No naturally occurring animal disease is recorded in OMIA as far as this search found.
- Orthologues: mouse *Arfgef2* (MGI) and zebrafish *arfgef2*. The Sec7 ARF-GEF family is conserved to yeast (Sec7 / Gea), and an ARF-GEF orthologue in *C. elegans* affects axon integrity through RAB-35 (PMID:42312793). That last link is distant and its ortholog identity was not confirmed.
- Zoonotic potential: not applicable.

## 15. Model Organisms

- **Mouse gene-trap (*Arfgef2* disrupted):** embryonic lethal. "no homozygous embryos were obtained from breeding heterozygous females and males", meaning "murine BIG2 is essential for early embryonic development" (Grzmil et al. 2010, PMID:20857375). Heterozygotes are normal.
  - **Limitation:** this model cannot assess corticogenesis, so it is an example of `FAILS_TO_RECAPITULATE` or human–model mismatch.
- **Mouse *Arfgef2*-null lines (Sheen lab):** "Arfgef2 null mice develop PH and exhibit impaired neural migration with increased protein expression" of FlnA and phospho-FlnA (Zhang et al. 2012, PMID:22956851).
  - **Unresolved discrepancy:** this conflicts with the gene-trap lethality. The allele type and genetic background need checking in the full text, and the disagreement could be curated as a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.
- **Acute knockdown:** in utero shRNA knockdown or dominant-negative BIG2 in embryonic mouse cortex impairs migration and adhesion and disrupts neuroependymal integrity (PMID:18996916, 22956851).
- **In vitro:** brefeldin A or dominant-negative ARFGEF2 in neural progenitors reduces proliferation and causes Golgi retention of E-cadherin and β-catenin (PMID:14647276). In SH-SY5Y cells it impairs FLNA transport (PMID:16320251).
- **Related phenocopy:** the *hyh* mouse (*Napa*, α-SNAP) shows neuroepithelial denudation and periventricular nodules, supporting a shared vesicle-trafficking pathway (PMID:18996916).
- **Not available:** no patient iPSC or organoid model, no zebrafish model, and no IMPC phenotype data were found.

---

## Notes for the existing KB entry (`kb/disorders/Periventricular_Nodular_Heterotopia_2.yaml`)

- **Gaps:**
  - The entry has no evidence items yet.
  - Phenotypes the entry lacks: progressive microcephaly, tetraparesis, hypotonia, dystonia/chorea, infantile spasms, thin corpus callosum, basal-ganglia MRI change, feeding difficulties, recurrent infections, cardiomyopathy.
  - Pathophysiology nodes the entry lacks: adhesion and neuroependymal integrity loss, and FLNA crosstalk, with `conforms_to: apical_neuroependyma_integrity_failure#…`.
  - No animal models, and no phenotype frequencies.
- **Already cached abstracts for evidence:** PMID:14647276, 42200925 (full text), 18996916, 24089482, 25097827, 16684786.
- **Fetch with `just fetch-reference`:** 23812912, 23755938, 19384555, 26126837, 25160555, 20857375, 22956851, 16320251, 12682315, 42255913, 42852362.
- **Still to confirm before curating:** ORPHA:2149, every HPO/GO/CL/NCIT identifier above, the Banne variant HGVS, and the ARFGEF2 hit in the head-circumference GWAS (PMID:35659227).

## Sources
- PubMed / Europe PMC records for PMIDs 14647276, 12682315, 23812912, 23755938, 19384555, 26126837, 25160555, 20857375, 22956851, 24089482, 24709996, 25097827, 16320251, 18996916, 42200925, 42255913, 42852362, 35659227 (https://pubmed.ncbi.nlm.nih.gov/ ; https://www.ebi.ac.uk/europepmc/)
- [ClinVar RCV000273072 (ARPHM; Orphanet 2149 / OMIM 608097)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000273072)
- [GenCC: ARFGEF2](https://search.thegencc.org/genes/HGNC:15853)
- [MedGen C1842563](https://ncbi.nlm.nih.gov/medgen/C1842563)
- [OMIM 605371](https://view.ncbi.nlm.nih.gov/omim/605371)
- [PhenoDis ARPHM](https://iegext02.helmholtz-munich.de/phenodis/disease/show/11066)
- [MalaCards ARPHM](https://www.malacards.org/card/periventricular_heterotopia_with_microcephaly_autosomal_recessive)
- [Grzmil et al. 2010, Int J Dev Biol](https://ijdb.ehu.eus/article/pdf/092959pg)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:42200925`: "No strong genotype–phenotype correlation emerged… suggesting that complete loss of function represents the critical pathogenic threshold"
  - closest text in source: "Most reported cases with truncating variants—whether occurring early or late in the coding sequence—present with broadly similar phenotypes, suggesting that complete loss of function represents the critical pathogenic threshold"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 65 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025430` (1 mention) - the report calls it "verify"; HP calls it **High-pitched cry**
- `UBERON:0000948` (1 mention) - the report calls it "Secondary:** heart, through cardiomyopathy"; UBERON calls it **heart**
- `NCIT:C15986` (2 mentions) - the report calls it "symptomatic"; NCIT calls it **Pharmacotherapy**
- `NCIT:C15240` (1 mention) - the report calls it "AR recurrence risk of 25%; prenatal or preimplantation testing"; NCIT calls it **Genetic Counseling**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0032388` (1 mention) - the report calls it "Periventricular nodular heterotopia (bilateral, often near-contiguous or diffuse)"; HP calls it **Periventricular nodular heterotopia**
- `HP:0002079` (1 mention) - the report calls it "Thin or hypoplastic corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `HP:0002059` (1 mention) - the report calls it "Cerebral / cortico-subcortical atrophy"; HP calls it **Cerebral atrophy**
- `UBERON:0002421` (1 mention) - the report calls it "hippocampus"; UBERON calls it **hippocampal formation**, and lists "hippocampus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.